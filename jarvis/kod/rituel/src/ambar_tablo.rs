//! `tools/ambar-tablo.py` karşılığı: BAĞLAM VERİ AMBARI v0 (deneysel m.29). Aynı SQLite'ta ayrı şema (önek `amb_`).
//! Bronz kosum-olay.jsonl (işçi-ajan transkriptlerinden) + tahmin/hüküm kütükleri → `amb_*` tabloları/görünümleri, sözleşme JSON'ları, gold CSV martları.
//! Kullanım: ambar-tablo [--repo] [--proje-dizin] [--kuru] [--sessiz]. Çıkış: 3 = sözleşme testlerinde ERROR · 1 = Python'da yakalanmamış istisna olan durumlar.
//! Bilinçli ayrışma: metin dosyaları LF yazılır (Python CRLF yazabilir); CSV satır sonu LF.
use crate::argparse::{Ayrisan, Secenek};
use crate::py::{self, float_repr};
use crate::harness_anahtar;
use jarvis_hook::ortak::{py_dumps, py_str, py_truthy};
use regex::Regex;
use rusqlite::{Connection, params_from_iter, types::Value as Sql, types::ValueRef};
use serde_json::{Map, Value, json};
use std::collections::{BTreeMap, HashMap, HashSet};
use std::path::Path;

const TOKEN_ALANLAR: [&str; 4] = ["input_tokens", "output_tokens", "cache_read_input_tokens", "cache_creation_input_tokens"];

type Sonuc<T> = Result<T, String>;

fn ayrisan() -> Ayrisan {
    Ayrisan::yeni(
        "ambar-tablo.py",
        None,
        vec![
            Secenek::deger(&["--repo"], "repo", None),
            Secenek::deger(&["--proje-dizin"], "proje_dizin", None),
            Secenek::bayrak(&["--kuru"], "kuru", None),
            Secenek::bayrak(&["--sessiz"], "sessiz", None),
        ],
    )
}

// ---------------------------------------------------------------- Python değer yardımcıları

/// SQLite değerinin Python `str()` karşılığı (None → "None").
fn sql_str(d: ValueRef) -> String {
    match d {
        ValueRef::Null => "None".into(),
        ValueRef::Integer(i) => i.to_string(),
        ValueRef::Real(f) => float_repr(f),
        ValueRef::Text(t) => String::from_utf8_lossy(t).into_owned(),
        ValueRef::Blob(b) => format!("b'{}'", String::from_utf8_lossy(b)),
    }
}

/// `csv.writer` alanı (QUOTE_MINIMAL; None → boş).
fn csv_alan(d: ValueRef) -> String {
    let ham = match d {
        ValueRef::Null => String::new(),
        other => sql_str(other),
    };
    if ham.contains([',', '"', '\r', '\n']) { format!("\"{}\"", ham.replace('"', "\"\"")) } else { ham }
}

fn sql_deger(v: &Value) -> Sql {
    match v {
        Value::Null => Sql::Null,
        Value::Bool(b) => Sql::Integer(*b as i64),
        Value::Number(n) => match n.as_i64() {
            Some(i) => Sql::Integer(i),
            None => Sql::Real(n.as_f64().unwrap_or(0.0)),
        },
        Value::String(s) => Sql::Text(s.clone()),
        other => Sql::Text(py_dumps(other)),
    }
}

fn al(m: &Map<String, Value>, k: &str) -> Value {
    m.get(k).cloned().unwrap_or(Value::Null)
}

/// Python `int(x or 0)` (yalnız sayı/bool/metin).
fn int_or0(v: Option<&Value>) -> i64 {
    match v {
        Some(Value::Number(n)) => n.as_i64().unwrap_or_else(|| n.as_f64().map(|f| f as i64).unwrap_or(0)),
        Some(Value::Bool(b)) => *b as i64,
        Some(Value::String(s)) => py::int(s).map(|i| i as i64).unwrap_or(0),
        _ => 0,
    }
}

/// `open(..., encoding="utf-8")` ile satır satır okuma (evrensel satır sonu); bozuk bayt `replace`.
fn satirlar(yol: &Path) -> std::io::Result<Vec<String>> {
    let b = std::fs::read(yol)?;
    let s = py::evrensel_satir(&String::from_utf8_lossy(&b));
    let mut v: Vec<String> = s.split('\n').map(String::from).collect();
    if v.last().is_some_and(|x| x.is_empty()) {
        v.pop();
    }
    Ok(v)
}

/// `{` ile başlayan satırları JSON olarak okur (bozuk JSON Python'da çöker).
fn jsonl_oku(yol: &Path) -> Sonuc<Vec<Map<String, Value>>> {
    let mut r = vec![];
    if !yol.exists() {
        return Ok(r);
    }
    for l in satirlar(yol).map_err(|e| format!("{}: {e}", yol.display()))? {
        if l.starts_with('{') {
            match serde_json::from_str::<Value>(&l) {
                Ok(Value::Object(m)) => r.push(m),
                _ => return Err(format!("{}: JSON çözülemedi", yol.display())),
            }
        }
    }
    Ok(r)
}

// ---------------------------------------------------------------- ISO zaman (datetime.fromisoformat alt kümesi)

/// (naif mikrosaniye, UTC sapması sn); sapma yoksa naif.
fn iso_coz(s: &str) -> Option<(i128, Option<i64>)> {
    let c: Vec<char> = s.chars().collect();
    if c.len() < 10 || !c[..10].iter().all(|x| x.is_ascii()) {
        return None;
    }
    let sayi = |a: usize, b: usize| -> Option<i64> {
        let t: String = c.get(a..b)?.iter().collect();
        if t.chars().all(|x| x.is_ascii_digit()) && !t.is_empty() { t.parse().ok() } else { None }
    };
    if c[4] != '-' || c[7] != '-' {
        return None;
    }
    let (y, mo, d) = (sayi(0, 4)?, sayi(5, 7)?, sayi(8, 10)?);
    if y < 1 {
        return None;
    }
    let tarih = chrono::NaiveDate::from_ymd_opt(y as i32, mo as u32, d as u32)?;
    let gun = tarih.signed_duration_since(chrono::NaiveDate::from_ymd_opt(1970, 1, 1)?).num_days() as i128;
    let (mut h, mut mi, mut sn, mut mik) = (0i64, 0i64, 0i64, 0i64);
    let mut sapma = None;
    if c.len() > 10 {
        let r: String = c[11..].iter().collect();
        let (zaman, tz) = match r.find(['+', '-']) {
            Some(i) => (r[..i].to_string(), Some(r[i..].to_string())),
            None => (r.clone(), None),
        };
        let (govde, kesir) = match zaman.split_once('.') {
            Some((a, b)) => (a.to_string(), Some(b.to_string())),
            None => (zaman.clone(), None),
        };
        let g: Vec<&str> = if govde.contains(':') { govde.split(':').collect() } else {
            match govde.len() {
                2 => vec![&govde[..]],
                4 => vec![&govde[..2], &govde[2..]],
                6 => vec![&govde[..2], &govde[2..4], &govde[4..]],
                _ => return None,
            }
        };
        let num = |x: &str| -> Option<i64> { if x.len() == 2 && x.chars().all(|c| c.is_ascii_digit()) { x.parse().ok() } else { None } };
        h = num(g.first()?)?;
        if g.len() > 1 {
            mi = num(g[1])?;
        }
        if g.len() > 2 {
            sn = num(g[2])?;
        }
        if g.len() > 3 {
            return None;
        }
        if let Some(k) = kesir {
            if g.len() != 3 || k.is_empty() || !k.chars().all(|c| c.is_ascii_digit()) {
                return None;
            }
            let t: String = k.chars().chain("000000".chars()).take(6).collect();
            mik = t.parse().ok()?;
        }
        if h > 23 || mi > 59 || sn > 59 {
            return None;
        }
        if let Some(tz) = tz {
            let isaret = if tz.starts_with('-') { -1 } else { 1 };
            let t = &tz[1..];
            let (t, _) = t.split_once('.').unwrap_or((t, ""));
            let p: Vec<&str> = if t.contains(':') { t.split(':').collect() } else {
                match t.len() {
                    2 => vec![&t[..]],
                    4 => vec![&t[..2], &t[2..]],
                    6 => vec![&t[..2], &t[2..4], &t[4..]],
                    _ => return None,
                }
            };
            let th = num(p.first()?)?;
            let tm = if p.len() > 1 { num(p[1])? } else { 0 };
            let ts = if p.len() > 2 { num(p[2])? } else { 0 };
            if p.len() > 3 || th > 23 || tm > 59 || ts > 59 {
                return None;
            }
            sapma = Some(isaret * (th * 3600 + tm * 60 + ts));
        }
    } else if c.len() != 10 {
        return None;
    }
    let mikro = (gun * 86400 + (h * 3600 + mi * 60 + sn) as i128) * 1_000_000 + mik as i128;
    Some((mikro, sapma))
}

/// `(t1 - t0).total_seconds()`; naif/bilinçli karışımı (TypeError) → None.
fn sure_hesapla(t0: &Value, t1: &Value) -> Option<f64> {
    let (Value::String(a), Value::String(b)) = (t0, t1) else { return None };
    let a = iso_coz(&a.replace('Z', "+00:00"))?;
    let b = iso_coz(&b.replace('Z', "+00:00"))?;
    let (x, y) = match (a.1, b.1) {
        (None, None) => (a.0, b.0),
        (Some(p), Some(q)) => (a.0 - p as i128 * 1_000_000, b.0 - q as i128 * 1_000_000),
        _ => return None,
    };
    Some((y - x) as f64 / 1e6)
}

// ---------------------------------------------------------------- Ajan transkripti özeti

fn bosluk_sikistir(s: &str) -> String {
    let mut o = String::new();
    let mut onceki = false;
    for ch in s.chars() {
        if py::bosluk_mu(ch) {
            if !onceki {
                o.push(' ');
            }
            onceki = true;
        } else {
            o.push(ch);
            onceki = false;
        }
    }
    o
}

fn ajan_ozeti(yol: &str, re_rol: &Regex, re_aile: &Regex) -> Sonuc<Option<Map<String, Value>>> {
    let mut rows: Vec<Value> = vec![];
    for l in satirlar(Path::new(yol)).map_err(|e| format!("{yol}: {e}"))? {
        if let Ok(v) = serde_json::from_str::<Value>(&l) {
            rows.push(v);
        }
    }
    if rows.is_empty() {
        return Ok(None);
    }
    let bos = Map::new();
    let mut ts: Vec<Value> = vec![];
    for d in &rows {
        let Value::Object(d) = d else { return Err("ajan satırı JSON nesnesi değil".into()) };
        if let Some(t) = d.get("timestamp")
            && py_truthy(t)
        {
            ts.push(t.clone());
        }
    }
    let mut models: BTreeMap<String, i64> = BTreeMap::new();
    let mut tok = [0i64; 4];
    let mut arac = 0i64;
    let mut ilk: Option<String> = None;
    for d in &rows {
        let Value::Object(d) = d else { continue };
        let m = match d.get("message") {
            Some(Value::Object(m)) => m,
            _ => &bos,
        };
        let tur = d.get("type").and_then(|t| t.as_str());
        if tur == Some("user") && ilk.is_none() {
            match m.get("content") {
                Some(Value::String(s)) => ilk = Some(s.clone()),
                Some(Value::Array(a)) if !a.is_empty() && a[0].is_object() => match a[0].get("text") {
                    None => ilk = Some(String::new()),
                    Some(Value::Null) => {}
                    Some(Value::String(s)) => ilk = Some(s.clone()),
                    Some(o) => ilk = Some(py_str(o)),
                },
                _ => ilk = Some(String::new()),
            }
        }
        if tur == Some("assistant") {
            if let Some(md) = m.get("model")
                && py_truthy(md)
            {
                *models.entry(py_str(md)).or_insert(0) += 1;
            }
            if let Some(Value::Object(u)) = m.get("usage") {
                for (i, k) in TOKEN_ALANLAR.iter().enumerate() {
                    tok[i] += int_or0(u.get(*k));
                }
            }
            if let Some(Value::Array(a)) = m.get("content") {
                for x in a {
                    if x.get("type").and_then(|t| t.as_str()) == Some("tool_use") && x.is_object() {
                        arac += 1;
                    }
                }
            }
        }
    }
    let ilk = ilk.unwrap_or_default();
    let rol = re_rol.captures(&ilk).and_then(|c| c.get(1)).map(|g| py::ilk(py::strip(g.as_str()), 80));
    let aile = re_aile.captures(&ilk).and_then(|c| c.get(1)).map(|g| g.as_str().to_string());
    let sure = match (ts.first(), ts.last()) {
        (Some(a), Some(b)) => sure_hesapla(a, b),
        _ => None,
    };
    let mut o = Map::new();
    o.insert("ts_bas".into(), ts.first().cloned().unwrap_or(Value::Null));
    o.insert("ts_son".into(), ts.last().cloned().unwrap_or(Value::Null));
    o.insert("sure_sn".into(), sure.and_then(serde_json::Number::from_f64).map(Value::Number).unwrap_or(Value::Null));
    o.insert("modeller".into(), json!(models.keys().cloned().collect::<Vec<_>>().join(",")));
    o.insert("asistan_mesaj".into(), json!(models.values().sum::<i64>()));
    o.insert("arac_cagrisi".into(), json!(arac));
    for (i, k) in TOKEN_ALANLAR.iter().enumerate() {
        o.insert((*k).into(), json!(tok[i]));
    }
    o.insert("rol".into(), rol.map(Value::String).unwrap_or(Value::Null));
    o.insert("aile".into(), aile.map(Value::String).unwrap_or(Value::Null));
    o.insert("ilk_prompt_kisa".into(), json!(py::ilk(&bosluk_sikistir(&ilk), 160)));
    Ok(Some(o))
}

/// `glob(<proje>/*/subagents/**/agent-*.jsonl, recursive=True)` (gizli adlar atlanır; Windows'ta ad eşleme büyük/küçük harfsiz).
fn agent_dosyalari(proje: &str) -> Vec<String> {
    fn gez(d: &str, sonuc: &mut Vec<String>) {
        let Ok(rd) = std::fs::read_dir(d) else { return };
        for e in rd.flatten() {
            let ad = e.file_name().to_string_lossy().into_owned();
            if ad.starts_with('.') {
                continue;
            }
            let y = py::join(d, &ad);
            let k = if cfg!(windows) { ad.to_lowercase() } else { ad.clone() };
            if k.starts_with("agent-") && k.ends_with(".jsonl") && k.len() >= "agent-.jsonl".len() {
                sonuc.push(y.clone());
            }
            if Path::new(&y).is_dir() {
                gez(&y, sonuc);
            }
        }
    }
    let mut sonuc = vec![];
    if let Ok(rd) = std::fs::read_dir(proje) {
        for e in rd.flatten() {
            let ad = e.file_name().to_string_lossy().into_owned();
            if ad.starts_with('.') {
                continue;
            }
            let alt = py::join(&py::join(proje, &ad), "subagents");
            if Path::new(&alt).is_dir() {
                gez(&alt, &mut sonuc);
            }
        }
    }
    sonuc.sort();
    sonuc
}

fn bronz_kosum(proje: &str, re_rol: &Regex, re_aile: &Regex) -> Sonuc<Vec<Map<String, Value>>> {
    let mut olaylar = vec![];
    for yol in agent_dosyalari(proje) {
        let parcalar: Vec<&str> = yol.split(py::SEP).collect();
        let Some(i) = parcalar.iter().position(|p| *p == "subagents") else { return Err("'subagents' bölümü bulunamadı".into()) };
        if i == 0 {
            return Err("oturum dizini bulunamadı".into());
        }
        let oturum = parcalar[i - 1].to_string();
        let wf = parcalar.iter().find(|p| p.starts_with("wf_")).map(|p| p.to_string());
        let taban = yol.rsplit(|c| c == '\\' || c == '/').next().unwrap_or(&yol).to_string();
        let agent_id: String = {
            let k: Vec<char> = taban.chars().collect();
            k[6..k.len() - 6].iter().collect()
        };
        let mut meta = Value::Null;
        let my = format!("{}.meta.json", &yol[..yol.len() - ".jsonl".len()]);
        if Path::new(&my).exists()
            && let Ok(b) = std::fs::read(&my)
            && let Ok(s) = String::from_utf8(b)
            && let Ok(v) = serde_json::from_str::<Value>(&s)
        {
            meta = v;
        }
        let Some(oz) = ajan_ozeti(&yol, re_rol, re_aile)? else { continue };
        let mut o = Map::new();
        o.insert("kosum_id".into(), json!(format!("{}:{agent_id}", wf.clone().unwrap_or_else(|| "agent".into()))));
        o.insert("wf_id".into(), wf.map(Value::String).unwrap_or(Value::Null));
        o.insert("agent_id".into(), json!(agent_id));
        o.insert("agent_type".into(), meta.get("agentType").cloned().unwrap_or(Value::Null));
        o.insert("oturum".into(), json!(oturum));
        o.insert("kaynak_dosya".into(), json!(py::relpath(&yol, proje)?));
        for (k, v) in oz {
            o.insert(k, v);
        }
        olaylar.push(o);
    }
    Ok(olaylar)
}

// ---------------------------------------------------------------- SQL

const SQL_1: &str = r##"
    CREATE TABLE IF NOT EXISTS amb_olgu_kosum (
      kosum_id TEXT PRIMARY KEY, wf_id TEXT, agent_id TEXT, agent_type TEXT, oturum TEXT, aile TEXT, rol TEXT, modeller TEXT,
      valid_time_bas TEXT, valid_time_son TEXT, sure_sn REAL, asistan_mesaj INTEGER, arac_cagrisi INTEGER,
      input_tokens INTEGER, output_tokens INTEGER, cache_read_input_tokens INTEGER, cache_creation_input_tokens INTEGER,
      ilk_prompt_kisa TEXT, kaynak_dosya TEXT, system_time TEXT, kod_sha TEXT
    );
    DELETE FROM amb_olgu_kosum;
    DROP TABLE IF EXISTS amb_olgu_prompt;
    CREATE TABLE amb_olgu_prompt AS
      SELECT prompt_id, oturum_id, sira, tur, sonraki_skill, sonraki_model, uzunluk_kar, kelime, metin_kisa,
             ts_utc AS valid_time, yuklendi_head AS kod_sha, datetime('now') AS system_time FROM prompt;
    DROP TABLE IF EXISTS amb_olgu_karar_borcu;
    CREATE TABLE amb_olgu_karar_borcu AS
      SELECT borc_id, kume, katman, karar_sahibi, durum, tur, masa_sirasi, kayit_tarihi AS valid_from, NULL AS valid_to,
             snapshot_tarih AS system_time, snapshot_sha AS kod_sha, baslik FROM karar_borcu;
    CREATE VIEW IF NOT EXISTS amb_boyut_anahtar AS
      SELECT anahtar_id AS anahtar_sk, anahtar_id, tur, deger, durum, replaced_by,
             COALESCE(gecerli_bas, ilk_gorulme) AS gecerli_bas, gecerli_bitis,
             CASE WHEN gecerli_bitis IS NULL OR gecerli_bitis='' THEN 1 ELSE 0 END AS guncel_mi,
             referans_sayisi, sicak_referans_sayisi FROM anahtar;
    CREATE VIEW IF NOT EXISTS amb_kopru_olay_nesne AS
      SELECT r.kayit_id AS olay_id, r.ref_deger AS nesne_id, r.ref_turu AS qualifier, r.hedef_var, k.dosya_id, d.katman, k.tarih_iso AS valid_time
      FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id JOIN dosya d ON d.dosya_id=k.dosya_id;
    CREATE VIEW IF NOT EXISTS amb_boyut_vardiya AS
      SELECT dosya_id AS teslim_dosya, baslik, ilk_commit AS teslim_zamani, boyut_bytes FROM dosya WHERE tur='teslim' ORDER BY ilk_commit;
    CREATE VIEW IF NOT EXISTS v_amb_kosum_maliyet AS
      SELECT wf_id, COUNT(*) AS ajan, GROUP_CONCAT(DISTINCT modeller) AS modeller, MIN(valid_time_bas) AS bas, MAX(valid_time_son) AS son,
             ROUND(SUM(sure_sn)/60.0,1) AS ajan_dk_toplam, SUM(output_tokens) AS output_tokens, SUM(input_tokens) AS input_tokens,
             SUM(cache_read_input_tokens) AS cache_read, SUM(cache_creation_input_tokens) AS cache_create, SUM(arac_cagrisi) AS arac_cagrisi
      FROM amb_olgu_kosum GROUP BY wf_id ORDER BY bas DESC;
    CREATE VIEW IF NOT EXISTS v_amb_acilis_brifi AS
      SELECT (SELECT kod_sha FROM amb_olgu_kosum LIMIT 1) AS kod_sha,
             (SELECT COUNT(*) FROM amb_olgu_karar_borcu WHERE karar_sahibi LIKE 'Salih%' AND durum NOT IN ('kapandı')) AS acik_salih_karari,
             (SELECT COUNT(*) FROM amb_olgu_karar_borcu WHERE karar_sahibi='Jarvis' AND durum!='kapandı') AS acik_icra_borcu,
             (SELECT metin_kisa FROM amb_olgu_prompt ORDER BY valid_time DESC LIMIT 1) AS son_prompt,
             (SELECT valid_time FROM amb_olgu_prompt ORDER BY valid_time DESC LIMIT 1) AS son_prompt_zamani,
             (SELECT COUNT(*) FROM amb_olgu_prompt WHERE date(valid_time)=date('now')) AS bugun_prompt,
             (SELECT teslim_dosya FROM amb_boyut_vardiya ORDER BY teslim_zamani DESC LIMIT 1) AS son_teslim,
             (SELECT wf_id||' · '||ajan||' ajan · '||output_tokens||' out-token' FROM v_amb_kosum_maliyet LIMIT 1) AS son_kosum,
             (SELECT COUNT(*) FROM amb_boyut_anahtar WHERE guncel_mi=1) AS guncel_anahtar,
             (SELECT COUNT(*) FROM amb_kopru_olay_nesne) AS kopru_satiri;
    CREATE TABLE IF NOT EXISTS amb_olgu_tahmin (
      tahmin_id TEXT PRIMARY KEY, gorev_emri_dosya TEXT, gorev_emri_satir INTEGER, rol TEXT, model_sinifi TEXT, effort TEXT,
      tahmin_cikti_min INTEGER, tahmin_cikti_max INTEGER, tahmin_girdi_min INTEGER, tahmin_girdi_max INTEGER,
      tahmin_arac_min INTEGER, tahmin_arac_max INTEGER, tahmin_sure_min_sn INTEGER, tahmin_sure_max_sn INTEGER,
      tahmin_serbest_metin TEXT, tahmin_formul_mu INTEGER, tahmin_kaynagi TEXT, wf_id TEXT,
      kaynak_rapor_dosya TEXT, kaynak_rapor_satir TEXT, system_time TEXT, kod_sha TEXT
    );
    DELETE FROM amb_olgu_tahmin;
    CREATE TABLE IF NOT EXISTS amb_olgu_kosum_sonuc (
      kosum_id TEXT PRIMARY KEY, sonuc TEXT, kaynak TEXT, aciklama TEXT, system_time TEXT, kod_sha TEXT, wf_id TEXT
    );
    DELETE FROM amb_olgu_kosum_sonuc;
    CREATE VIEW IF NOT EXISTS v_kosum_tahmin_sapma AS
      WITH k AS (
        SELECT wf_id, aile,
          CASE WHEN rol LIKE '%ANTİTEZ%' THEN 'ANTİTEZ'
               WHEN rol LIKE '%TEZ%' THEN 'TEZ'
               WHEN rol LIKE '%V26%' THEN 'V26'
               WHEN rol LIKE '%HAKEM%' THEN 'HAKEM'
               ELSE NULL END AS rol_norm,
          modeller, output_tokens, input_tokens + cache_creation_input_tokens AS yeni_girdi_tokens, arac_cagrisi, sure_sn
        FROM amb_olgu_kosum WHERE wf_id IS NOT NULL)
      SELECT t.tahmin_id, t.wf_id, k.aile, t.rol, t.model_sinifi, k.modeller AS gercek_model,
             t.tahmin_cikti_min, t.tahmin_cikti_max, k.output_tokens AS gercek_cikti,
             CASE WHEN t.tahmin_formul_mu=1 THEN 'FORMÜL'
                  WHEN t.tahmin_cikti_min IS NULL THEN 'TAHMİN-YOK'
                  WHEN k.output_tokens IS NULL THEN 'GERÇEK-YOK'
                  WHEN k.output_tokens < t.tahmin_cikti_min THEN 'ALTINDA'
                  WHEN k.output_tokens > t.tahmin_cikti_max THEN 'ÜSTÜNDE' ELSE 'BANDA' END AS cikti_durum,
             ROUND(k.output_tokens*1.0/NULLIF(t.tahmin_cikti_max,0), 2) AS cikti_gercek_bolu_tahmin_ust,
             t.tahmin_arac_min, t.tahmin_arac_max, k.arac_cagrisi AS gercek_arac,
             CASE WHEN t.tahmin_arac_min IS NULL THEN 'TAHMİN-YOK' WHEN k.arac_cagrisi IS NULL THEN 'GERÇEK-YOK'
                  WHEN k.arac_cagrisi < t.tahmin_arac_min THEN 'ALTINDA'
                  WHEN k.arac_cagrisi > t.tahmin_arac_max THEN 'ÜSTÜNDE' ELSE 'BANDA' END AS arac_durum,
             t.tahmin_sure_min_sn, t.tahmin_sure_max_sn, ROUND(k.sure_sn,0) AS gercek_sure_sn,
             CASE WHEN t.tahmin_sure_min_sn IS NULL THEN 'TAHMİN-YOK' WHEN k.sure_sn IS NULL THEN 'GERÇEK-YOK'
                  WHEN k.sure_sn < t.tahmin_sure_min_sn THEN 'ALTINDA'
                  WHEN k.sure_sn > t.tahmin_sure_max_sn THEN 'ÜSTÜNDE' ELSE 'BANDA' END AS sure_durum,
             t.tahmin_girdi_min, t.tahmin_girdi_max, k.yeni_girdi_tokens AS gercek_yeni_girdi,
             t.tahmin_serbest_metin, t.gorev_emri_dosya
      FROM amb_olgu_tahmin t
      LEFT JOIN k ON k.wf_id = t.wf_id AND k.rol_norm = t.rol
      ORDER BY t.wf_id, t.rol, k.aile;
    DROP VIEW IF EXISTS v_skill_kosum;
    CREATE VIEW v_skill_kosum AS
      SELECT 'ana-sira-prompt' AS kaynak, TRIM(je.value) AS skill, p.sonraki_model AS model,
             COUNT(*) AS n, NULL AS output_tokens, NULL AS sure_dk, NULL AS sonuc_n, NULL AS fail_n
      FROM amb_olgu_prompt p, json_each('["'||REPLACE(TRIM(p.sonraki_skill), ',', '","')||'"]') je
      WHERE p.sonraki_skill IS NOT NULL AND TRIM(p.sonraki_skill) <> ''
      GROUP BY TRIM(je.value), p.sonraki_model
      UNION ALL
      SELECT 'ajan-kosum-vekil',
             CASE WHEN k.agent_type='atlas' THEN 'atlas-kosum' ELSE NULL END AS skill,
             k.modeller, COUNT(*), SUM(k.output_tokens), ROUND(SUM(k.sure_sn)/60.0,1),
             COUNT(s.kosum_id), SUM(CASE WHEN s.sonuc='FAIL' THEN 1 ELSE 0 END)
      FROM amb_olgu_kosum k LEFT JOIN amb_olgu_kosum_sonuc s ON s.kosum_id=k.kosum_id
      GROUP BY CASE WHEN k.agent_type='atlas' THEN 'atlas-kosum' ELSE NULL END, k.modeller
      ORDER BY kaynak, n DESC;
    "##;

const SQL_2: &str = r##"
    CREATE TABLE IF NOT EXISTS amb_olgu_tartisma_notu (
      not_id TEXT PRIMARY KEY, valid_time TEXT, konu TEXT, tetikleyen TEXT, cevap_ozeti TEXT, acik_soru TEXT, katman INTEGER, durum TEXT,
      oturum TEXT, prompt_sayisi INTEGER, kaynak_kuyruk TEXT, system_time TEXT, kod_sha TEXT
    );
    DELETE FROM amb_olgu_tartisma_notu;
    CREATE TABLE IF NOT EXISTS amb_kopru_not_prompt (not_id TEXT, prompt_id TEXT, sira INTEGER, qualifier TEXT);
    DELETE FROM amb_kopru_not_prompt;
    CREATE VIEW IF NOT EXISTS v_tartisma_notu AS
      SELECT n.not_id, n.valid_time AS tarih, n.durum, n.konu, n.acik_soru, n.prompt_sayisi,
             (SELECT GROUP_CONCAT(substr(p.ts_tr,12,5)||' '||p.tur||': '||substr(p.metin_kisa,1,60), ' ¦ ') FROM amb_kopru_not_prompt k JOIN prompt p ON p.prompt_id=k.prompt_id WHERE k.not_id=n.not_id) AS prompt_ozet
      FROM amb_olgu_tartisma_notu n ORDER BY n.valid_time DESC;
    "##;

const SAYIM_TESTLERI: [(&str, &str); 8] = [
    ("amb_olgu_kosum.kosum_id unique", "SELECT COUNT(*) FROM (SELECT kosum_id FROM amb_olgu_kosum GROUP BY kosum_id HAVING COUNT(*)>1)"),
    ("amb_olgu_kosum.output_tokens not_null", "SELECT COUNT(*) FROM amb_olgu_kosum WHERE output_tokens IS NULL"),
    ("amb_olgu_prompt → prompt 1:1", "SELECT ABS((SELECT COUNT(*) FROM amb_olgu_prompt)-(SELECT COUNT(*) FROM prompt))"),
    ("amb_kopru_not_prompt.prompt_id → prompt", "SELECT COUNT(*) FROM amb_kopru_not_prompt k LEFT JOIN prompt p ON p.prompt_id=k.prompt_id WHERE p.prompt_id IS NULL"),
    ("amb_olgu_tahmin.tahmin_id unique", "SELECT COUNT(*) FROM (SELECT tahmin_id FROM amb_olgu_tahmin GROUP BY tahmin_id HAVING COUNT(*)>1)"),
    ("amb_olgu_tahmin.wf_id → amb_olgu_kosum", "SELECT COUNT(*) FROM amb_olgu_tahmin t WHERE t.wf_id IS NOT NULL AND NOT EXISTS (SELECT 1 FROM amb_olgu_kosum k WHERE k.wf_id=t.wf_id)"),
    ("amb_olgu_kosum_sonuc.sonuc accepted_values", "SELECT COUNT(*) FROM amb_olgu_kosum_sonuc WHERE sonuc NOT IN ('PASS','FAIL')"),
    ("amb_olgu_kosum_sonuc → amb_olgu_kosum (kosum_id ∨ wf_id; İB-50)", "SELECT COUNT(*) FROM amb_olgu_kosum_sonuc s LEFT JOIN amb_olgu_kosum k ON k.kosum_id=s.kosum_id LEFT JOIN (SELECT DISTINCT wf_id FROM amb_olgu_kosum WHERE wf_id IS NOT NULL AND wf_id<>'') w ON w.wf_id=s.wf_id WHERE k.kosum_id IS NULL AND w.wf_id IS NULL"),
];

fn hata<E: std::fmt::Display>(e: E) -> String {
    e.to_string()
}

fn ekle(con: &Connection, sql: &str, v: Vec<Value>) -> Sonuc<()> {
    con.execute(sql, params_from_iter(v.iter().map(sql_deger))).map_err(hata)?;
    Ok(())
}

fn tablo_sozlesmesi(con: &Connection, tablo: &str) -> Sonuc<Value> {
    let mut st = con.prepare(&format!("PRAGMA table_info({tablo})")).map_err(hata)?;
    let satirlar = st
        .query_map([], |r| {
            let tip: Option<String> = r.get(2)?;
            let tip = tip.filter(|t| !t.is_empty()).unwrap_or_else(|| "ANY".into());
            Ok(json!({"ad": r.get::<_, String>(1)?, "tip": tip, "not_null": r.get::<_, i64>(3)? != 0, "pk": r.get::<_, i64>(5)? != 0}))
        })
        .map_err(hata)?
        .collect::<Result<Vec<_>, _>>()
        .map_err(hata)?;
    Ok(Value::Array(satirlar))
}

fn sozlesme_yaz(con: &Connection, repo: &str, dosya: &str, tablo: &str, surum: &str, grain: &str, kural: &str) -> Sonuc<()> {
    let yol = py::join(&py::join(&py::join(repo, "veri"), "sozlesme"), dosya);
    if Path::new(&yol).exists() {
        return Ok(());
    }
    let cols = tablo_sozlesmesi(con, tablo)?;
    let v = json!({"tablo": tablo, "surum": surum, "katman": "ambar", "grain": grain, "kolonlar": cols, "kural": kural});
    std::fs::write(&yol, py::json_girintili(&v)).map_err(|e| format!("{yol}: {e}"))
}

fn simdi_utc() -> String {
    let n = chrono::Utc::now();
    let mik = n.timestamp_subsec_micros();
    if mik == 0 { n.format("%Y-%m-%dT%H:%M:%S+00:00").to_string() } else { format!("{}.{mik:06}+00:00", n.format("%Y-%m-%dT%H:%M:%S")) }
}

fn calis(a: &crate::argparse::Sonuc) -> Sonuc<i32> {
    let repo = py::abspath(&a.metin("repo").map(String::from).unwrap_or_else(harness_anahtar::jarvis));
    let proje_dizin = a.metin("proje_dizin").map(String::from).unwrap_or_else(|| harness_anahtar::proje_dizin(None));
    let kuru = a.bayrak("kuru");
    if !Path::new(&repo).is_dir() {
        return Err(format!("git cwd bulunamadı: {repo}"));
    }
    let head = py::sh(&["rev-parse", "--short", "HEAD"], Path::new(&repo));
    let simdi = simdi_utc();
    let re_rol = Regex::new(r"ROL:\s*(.+?)(?:\s+—|\n|$)").map_err(hata)?;
    let re_aile = Regex::new(r"aile\s+([A-Z]{1,3})\b").map_err(hata)?;

    // --- BRONZ: koşum olayları (append-only, tekil kosum_id) ---
    let olaylar = bronz_kosum(&proje_dizin, &re_rol, &re_aile)?;
    let byol = py::join(&py::join(&py::join(&repo, "veri"), "bronz"), "kosum-olay.jsonl");
    let mut mevcut: Vec<Map<String, Value>> = vec![];
    let mut dizin: HashMap<String, usize> = HashMap::new();
    for d in jsonl_oku(Path::new(&byol))? {
        let Some(Value::String(k)) = d.get("kosum_id").cloned() else { return Err("kosum_id yok".into()) };
        match dizin.get(&k) {
            Some(&i) => mevcut[i] = d,
            None => {
                dizin.insert(k, mevcut.len());
                mevcut.push(d);
            }
        }
    }
    let yeni: Vec<&Map<String, Value>> = olaylar.iter().filter(|o| !dizin.contains_key(o["kosum_id"].as_str().unwrap_or(""))).collect();
    let damga = |o: &Map<String, Value>| -> Map<String, Value> {
        let mut m = o.clone();
        m.insert("yuklendi_head".into(), json!(head));
        m.insert("yuklendi_ts".into(), json!(simdi));
        m
    };
    if !kuru {
        let bd = py::join(&py::join(&repo, "veri"), "bronz");
        std::fs::create_dir_all(&bd).map_err(|e| format!("{bd}: {e}"))?;
        let mut metin = String::new();
        if !Path::new(&byol).exists() {
            metin.push_str("# veri/bronz/kosum-olay.jsonl — BRONZ: işçi-ajan koşum olayları (Workflow/Agent alt-ajan transkriptlerinden; 1 satır = 1 ajan koşumu; append-only; tekil anahtar kosum_id; token alanları ham usage). Üretici tools/ambar-tablo.py.\n");
        }
        for o in &yeni {
            metin.push_str(&py_dumps(&Value::Object(damga(o))));
            metin.push('\n');
        }
        use std::io::Write;
        let mut f = std::fs::OpenOptions::new().create(true).append(true).open(&byol).map_err(|e| format!("{byol}: {e}"))?;
        f.write_all(metin.as_bytes()).map_err(hata)?;
    }
    let mut hepsi: Vec<Map<String, Value>> = mevcut;
    hepsi.extend(yeni.iter().map(|o| damga(o)));

    // --- BRONZ: tahmin olayları + koşum hükümleri (yalnız okunur) ---
    let bronz = py::join(&py::join(&repo, "veri"), "bronz");
    let tahminler = jsonl_oku(Path::new(&py::join(&bronz, "tahmin-olay.jsonl")))?;
    let hukumler = jsonl_oku(Path::new(&py::join(&bronz, "kosum-sonuc.jsonl")))?;

    if kuru {
        let wf: HashSet<&str> = olaylar.iter().filter_map(|o| o.get("wf_id").and_then(|v| v.as_str())).filter(|s| !s.is_empty()).collect();
        py::print(&format!("(kuru) bronz koşum: {} ajan koşumu ({} yeni) · wf sayısı {}", olaylar.len(), yeni.len(), wf.len()));
        return Ok(0);
    }
    let con = Connection::open(py::join(&py::join(&repo, "veri"), "baglam.sqlite")).map_err(|e| format!("sqlite3.OperationalError: {e}"))?;
    con.execute_batch(SQL_1).map_err(|e| format!("sqlite3.OperationalError: {e}"))?;
    // tartışma notları (bronz: veri/tartisma-notu.jsonl)
    let notlar = jsonl_oku(Path::new(&py::join(&py::join(&repo, "veri"), "tartisma-notu.jsonl")))?;
    con.execute_batch(SQL_2).map_err(|e| format!("sqlite3.OperationalError: {e}"))?;
    for n in &notlar {
        let gerekli = |k: &str| n.get(k).cloned().ok_or_else(|| format!("KeyError: '{k}'"));
        let pid: Vec<Value> = match n.get("prompt_id") {
            Some(Value::Array(a)) => a.clone(),
            Some(Value::String(s)) => s.chars().map(|c| json!(c.to_string())).collect(),
            _ => vec![],
        };
        ekle(
            &con,
            "INSERT INTO amb_olgu_tartisma_notu VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            vec![
                gerekli("not_id")?,
                gerekli("tarih")?,
                gerekli("konu")?,
                al(n, "tetikleyen"),
                al(n, "cevap_ozeti"),
                al(n, "acik_soru"),
                al(n, "katman"),
                al(n, "durum"),
                al(n, "oturum"),
                json!(pid.len()),
                al(n, "kaynak_kuyruk"),
                json!(simdi),
                json!(head),
            ],
        )?;
        for (i, p) in pid.iter().enumerate() {
            ekle(&con, "INSERT INTO amb_kopru_not_prompt VALUES (?,?,?,?)", vec![n["not_id"].clone(), p.clone(), json!(i + 1), json!("tartisma-konusu")])?;
        }
    }
    for o in &hepsi {
        let gerekli = |k: &str| o.get(k).cloned().ok_or_else(|| format!("KeyError: '{k}'"));
        let mut v = vec![gerekli("kosum_id")?, gerekli("wf_id")?, gerekli("agent_id")?, gerekli("agent_type")?, gerekli("oturum")?];
        for k in [
            "aile",
            "rol",
            "modeller",
            "ts_bas",
            "ts_son",
            "sure_sn",
            "asistan_mesaj",
            "arac_cagrisi",
            "input_tokens",
            "output_tokens",
            "cache_read_input_tokens",
            "cache_creation_input_tokens",
            "ilk_prompt_kisa",
            "kaynak_dosya",
            "yuklendi_ts",
            "yuklendi_head",
        ] {
            v.push(al(o, k));
        }
        ekle(&con, "INSERT INTO amb_olgu_kosum VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", v)?;
    }
    for t in &tahminler {
        let tid = t.get("tahmin_id").cloned().ok_or("KeyError: 'tahmin_id'")?;
        let mut v = vec![tid];
        for k in [
            "gorev_emri_dosya",
            "gorev_emri_satir",
            "rol",
            "model_sinifi",
            "effort",
            "tahmin_cikti_min",
            "tahmin_cikti_max",
            "tahmin_girdi_min",
            "tahmin_girdi_max",
            "tahmin_arac_min",
            "tahmin_arac_max",
            "tahmin_sure_min_sn",
            "tahmin_sure_max_sn",
            "tahmin_serbest_metin",
        ] {
            v.push(al(t, k));
        }
        v.push(json!(if t.get("tahmin_formul_mu").is_some_and(py_truthy) { 1 } else { 0 }));
        for k in ["tahmin_kaynagi", "wf_id", "kaynak_rapor_dosya", "kaynak_rapor_satir", "yuklendi_ts", "yuklendi_head"] {
            v.push(al(t, k));
        }
        ekle(&con, "INSERT INTO amb_olgu_tahmin VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", v)?;
    }
    // İB-50: wf-düzeyi hüküm köprüsü + süpersede
    let var: bool = {
        let mut st = con.prepare("PRAGMA table_info(amb_olgu_kosum_sonuc)").map_err(hata)?;
        let adlar = st.query_map([], |r| r.get::<_, String>(1)).map_err(hata)?.collect::<Result<Vec<_>, _>>().map_err(hata)?;
        adlar.iter().any(|x| x == "wf_id")
    };
    if !var {
        con.execute("ALTER TABLE amb_olgu_kosum_sonuc ADD COLUMN wf_id TEXT", []).map_err(hata)?;
    }
    let susp: HashSet<String> = hukumler.iter().filter_map(|h| h.get("supersedes")).filter(|v| py_truthy(v)).map(py_str).collect();
    for h in &hukumler {
        let kid = h.get("kosum_id").cloned().ok_or("KeyError: 'kosum_id'")?;
        let kid_s = py_str(&kid);
        if susp.contains(&kid_s) {
            continue;
        }
        let wf = match h.get("wf_id") {
            Some(w) if py_truthy(w) => w.clone(),
            _ if kid_s.starts_with("wf_") => kid.clone(),
            _ => Value::Null,
        };
        ekle(&con, "INSERT INTO amb_olgu_kosum_sonuc VALUES (?,?,?,?,?,?,?)", vec![kid, al(h, "sonuc"), al(h, "kaynak"), al(h, "aciklama"), al(h, "yuklendi_ts"), al(h, "yuklendi_head"), wf])?;
    }
    // sözleşmeler (ilk kez)
    sozlesme_yaz(&con, &repo, "amb_olgu_kosum.json", "amb_olgu_kosum", "0.1.0-deneysel-m29", "1 satır = 1 işçi-ajan koşumu (Workflow/Agent alt-ajanı)", "additive-only; token kolonları OTel gen_ai.usage.* eşleme sözlüğüne bağlanır (kolon adı olarak gömülmez)")?;
    sozlesme_yaz(&con, &repo, "amb_olgu_tahmin.json", "amb_olgu_tahmin", "0.1.0-deneysel-m29", "1 satır = 1 (görev-emri, rol) tahmini — aile-BAĞIMSIZ (KB-02; gerçek aile-bazlı, JOIN v_kosum_tahmin_sapma'da)", "additive-only; üst model (fable) satırlarında tahmin alanları NULL; formül tahminlerde bant NULL + tahmin_formul_mu=1")?;
    sozlesme_yaz(&con, &repo, "amb_olgu_kosum_sonuc.json", "amb_olgu_kosum_sonuc", "0.1.0-ONERI-karar52", "1 satır = 1 ajan koşumunun done-yüklemi hükmü (PASS/FAIL)", "ÖNERİ-damgalı alan (Salih 08-21 Karar 52; nihai Katman-1 şema imzası AÇIK); hüküm orkestratörce teslim-al adımında yazılır, transkriptten türetilmez")?;
    let mut testler: Vec<(&str, i64, &str)> = vec![];
    for (ad, sql) in SAYIM_TESTLERI {
        let n: i64 = con.query_row(sql, [], |r| r.get(0)).map_err(hata)?;
        testler.push((ad, n, if n == 0 { "PASS" } else { "ERROR" }));
    }
    // GOLD CSV
    let gdir = py::join(&py::join(&repo, "veri"), "gorunum");
    for v in ["v_amb_kosum_maliyet", "v_amb_acilis_brifi", "v_tartisma_notu", "v_kosum_tahmin_sapma", "v_skill_kosum"] {
        let mut st = con.prepare(&format!("SELECT * FROM {v}")).map_err(hata)?;
        let kolonlar: Vec<String> = st.column_names().iter().map(|s| s.to_string()).collect();
        let n = kolonlar.len();
        let mut metin = String::new();
        let satir_yaz = |metin: &mut String, alanlar: Vec<String>| {
            if alanlar.len() == 1 && alanlar[0].is_empty() {
                metin.push_str("\"\"");
            } else {
                metin.push_str(&alanlar.join(","));
            }
            metin.push('\n');
        };
        satir_yaz(&mut metin, kolonlar.iter().map(|k| csv_alan(ValueRef::Text(k.as_bytes()))).collect());
        let mut rows = st.query([]).map_err(hata)?;
        while let Some(r) = rows.next().map_err(hata)? {
            let alanlar: Vec<String> = (0..n).map(|i| r.get_ref(i).map(csv_alan)).collect::<Result<_, _>>().map_err(hata)?;
            satir_yaz(&mut metin, alanlar);
        }
        let yol = py::join(&gdir, &format!("{v}.csv"));
        std::fs::write(&yol, metin).map_err(|e| format!("{yol}: {e}"))?;
    }
    let (bcols, brif): (Vec<String>, Vec<String>) = {
        let mut st = con.prepare("SELECT * FROM v_amb_acilis_brifi").map_err(hata)?;
        let c: Vec<String> = st.column_names().iter().map(|s| s.to_string()).collect();
        let n = c.len();
        let mut rows = st.query([]).map_err(hata)?;
        let b = match rows.next().map_err(hata)? {
            Some(r) => (0..n).map(|i| r.get_ref(i).map(sql_str)).collect::<Result<Vec<_>, _>>().map_err(hata)?,
            None => return Err("brif satırı yok".into()),
        };
        (c, b)
    };
    let n_kosum: (i64, i64) = con.query_row("SELECT COUNT(*), COUNT(DISTINCT wf_id) FROM amb_olgu_kosum", [], |r| Ok((r.get(0)?, r.get(1)?))).map_err(hata)?;
    drop(con);
    if !a.bayrak("sessiz") {
        py::print(&format!("ambar v0: amb_olgu_kosum {} ajan koşumu / {} workflow ({} yeni bronz olay) · amb_olgu_tahmin {} tahmin · amb_olgu_kosum_sonuc {} hüküm (ÖNERİ) · amb_olgu_prompt · amb_olgu_karar_borcu · görünümler amb_boyut_anahtar/amb_kopru_olay_nesne/amb_boyut_vardiya · martlar v_amb_kosum_maliyet + v_amb_acilis_brifi + v_kosum_tahmin_sapma + v_skill_kosum (CSV)", n_kosum.0, n_kosum.1, yeni.len(), tahminler.len(), hukumler.len()));
        for t in &testler {
            py::print(&format!("  [{}] {} ihlal {}", t.2, t.0, t.1));
        }
        let parcalar: Vec<String> = bcols.iter().zip(brif.iter()).map(|(k, v)| format!("{k}={}", py::ilk(v, 60))).collect();
        py::print(&format!("  açılış-brifi martı: {}", parcalar.join(" · ")));
    }
    Ok(if testler.iter().any(|t| t.2 == "ERROR") { 3 } else { 0 })
}

pub fn kos(argv: &[String]) -> i32 {
    let a = match ayrisan().ayristir(argv) {
        Ok(a) => a,
        Err(k) => return k,
    };
    match calis(&a) {
        Ok(k) => k,
        Err(e) => py::coker(&e),
    }
}
