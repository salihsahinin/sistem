//! `tools/baglam-seyir.py` karşılığı: BAĞLAM KOMPOZİSYONU ölçüm hattı (KB-50 (a), Karar 61; KB-52 (a) 128K uyarısı; İB-22).
//! Bronz (`veri/bronz/baglam-olay.jsonl`, transkript usage ham + provenans) -> silver (`baglam_olay`) -> gold (`v_baglam_seyri`, `v_baglam_gunluk`, CSV).
//! Çıkış: 0 tamam · 1 transkript dizini yok (Python `sys.exit(metin)`) · 3 veri-testi ERROR.
//! Python'da yakalanmamış istisna olurdu (kayıtlarda beklenmedik tür/eksik anahtar) durumlar `py::coker` ile çıkış 1'dir.
use crate::argparse::{Ayrisan, Secenek};
use crate::harness_anahtar;
use crate::py::{self, float_repr};
use chrono::{Datelike, Duration, Local, NaiveDate, NaiveDateTime, NaiveTime, TimeZone, Timelike};
use jarvis_hook::ortak::{py_dumps, py_truthy};
use rusqlite::{Connection, params_from_iter, types::Value as Sql, types::ValueRef};
use serde_json::{Map, Value, json};
use std::collections::{HashMap, HashSet};
use std::io::Write;
use std::path::Path;

const ESIK_128K: i64 = 128_000;
const ESIK_STATIK: i64 = 60_000;
/// Python metin kipi (`open(.., "a"/"w")`, `newline` verilmemiş): Windows'ta `\n` -> `\r\n`.
const SATIR_SONU: &str = if cfg!(windows) { "\r\n" } else { "\n" };

type Kayit = Map<String, Value>;

fn ayrisan() -> Ayrisan {
    Ayrisan::yeni(
        "baglam-seyir.py",
        None,
        vec![
            Secenek::deger(&["--proje-dizin"], "proje_dizin", None),
            Secenek::deger(&["--repo"], "repo", None),
            Secenek::bayrak(&["--kuru"], "kuru", None),
            Secenek::bayrak(&["--sessiz"], "sessiz", None),
        ],
    )
}

// ---------------------------------------------------------------- zaman

/// Python 3.11 `datetime.fromisoformat` alt kümesi: `HH[:MM[:SS[.f]]]` ya da bitişik biçim; çıktı (HH, MM, SS, µs).
fn saat_ayristir(s: &str) -> Option<(u32, u32, u32, u32)> {
    let b = s.as_bytes();
    let rakam2 = |i: usize| -> Option<u32> {
        if i + 2 <= b.len() && b[i].is_ascii_digit() && b[i + 1].is_ascii_digit() { Some(((b[i] - b'0') * 10 + (b[i + 1] - b'0')) as u32) } else { None }
    };
    let sa = rakam2(0)?;
    let mut poz = 2;
    let (mut dk, mut sn, mut us) = (0, 0, 0);
    if poz < b.len() {
        let ayrac = b[poz] == b':';
        if ayrac {
            poz += 1;
        }
        dk = rakam2(poz)?;
        poz += 2;
        if poz < b.len() {
            if ayrac {
                if b[poz] != b':' {
                    return None;
                }
                poz += 1;
            }
            sn = rakam2(poz)?;
            poz += 2;
            if poz < b.len() {
                if b[poz] != b'.' && b[poz] != b',' {
                    return None;
                }
                poz += 1;
                let kalan = &b[poz..];
                if kalan.is_empty() || !kalan.iter().all(u8::is_ascii_digit) {
                    return None;
                }
                let al = kalan.len().min(6);
                let mut v: u32 = std::str::from_utf8(&kalan[..al]).ok()?.parse().ok()?;
                for _ in al..6 {
                    v *= 10;
                }
                us = v;
            }
        }
    }
    Some((sa, dk, sn, us))
}

/// Python `parse_ts`: UTC anına çevrilmiş saf zaman; ayrıştırılamazsa `None`. Saat dilimsiz değer yerel saat sayılır (`astimezone`).
fn parse_ts(ts: &str) -> Option<NaiveDateTime> {
    let s = ts.replace('Z', "+00:00");
    if !s.is_ascii() || s.len() < 7 {
        return None;
    }
    let b = s.as_bytes();
    let rakamlar = |a: usize, z: usize| -> Option<u32> {
        let p = s.get(a..z)?;
        if p.bytes().all(|c| c.is_ascii_digit()) { p.parse().ok() } else { None }
    };
    let (y, ay, gun, tarih_uz) = if b.len() >= 10 && b[4] == b'-' && b[7] == b'-' {
        (rakamlar(0, 4)?, rakamlar(5, 7)?, rakamlar(8, 10)?, 10)
    } else if b.len() >= 8 {
        (rakamlar(0, 4)?, rakamlar(4, 6)?, rakamlar(6, 8)?, 8)
    } else {
        return None;
    };
    if y < 1 {
        return None;
    }
    let tarih = NaiveDate::from_ymd_opt(y as i32, ay, gun)?;
    let (mut zaman, mut dilim): (NaiveTime, Option<i64>) = (NaiveTime::MIN, None);
    if b.len() > tarih_uz {
        let sat = &s[tarih_uz + 1..];
        let kes = sat.find(['+', '-']);
        let (govde, tz) = match kes {
            Some(i) => (&sat[..i], Some(&sat[i..])),
            None => (sat, None),
        };
        let (sa, dk, sn, us) = saat_ayristir(govde)?;
        zaman = NaiveTime::from_hms_micro_opt(sa, dk, sn, us)?;
        if let Some(tz) = tz {
            let isaret: i64 = if tz.starts_with('-') { -1 } else { 1 };
            let (h, m, sec, _us) = saat_ayristir(&tz[1..])?;
            let toplam = h as i64 * 3600 + m as i64 * 60 + sec as i64;
            if toplam >= 86_400 {
                return None;
            }
            dilim = Some(isaret * toplam);
        }
    }
    let ndt = tarih.and_time(zaman);
    match dilim {
        Some(o) => Some(ndt - Duration::seconds(o)),
        None => Local.from_local_datetime(&ndt).earliest().map(|d| d.naive_utc()),
    }
}

/// UTC anı -> (ts_tr isoformat, tarih_tr, saat_tr); Python `astimezone(TR)` taşması `Err`.
fn tr_bicim(utc: NaiveDateTime) -> Result<(String, String, String), String> {
    let yil_ok = |d: &NaiveDateTime| (1..=9999).contains(&d.year());
    if !yil_ok(&utc) {
        return Err("OverflowError: date value out of range".into());
    }
    let tr = utc + Duration::hours(3);
    if !yil_ok(&tr) {
        return Err("OverflowError: date value out of range".into());
    }
    let us = tr.nanosecond() / 1000;
    let tarih = format!("{:04}-{:02}-{:02}", tr.year(), tr.month(), tr.day());
    let saat = format!("{:02}:{:02}:{:02}", tr.hour(), tr.minute(), tr.second());
    let mikro = if us != 0 { format!(".{us:06}") } else { String::new() };
    Ok((format!("{tarih}T{saat}{mikro}+03:00"), tarih, saat))
}

// ---------------------------------------------------------------- değer yardımcıları (Python `or`/tür kuralları)

/// `d.get(k) or 0` ile toplanabilir tamsayı; beklenmedik tür Python'da `TypeError` olurdu.
fn say(v: Option<&Value>) -> Result<i64, String> {
    let v = match v {
        None => return Ok(0),
        Some(v) => v,
    };
    if !py_truthy(v) {
        return Ok(0);
    }
    match v {
        Value::Bool(b) => Ok(*b as i64),
        Value::Number(n) => n.as_i64().ok_or_else(|| format!("sayı tamsayı değil: {n}")),
        other => Err(format!("sayısal olmayan değer: {}", py_dumps(other))),
    }
}

/// Metin ya da `None`; başka tür Python'da veritabanı bağlamada/karşılaştırmada çökerdi.
fn metin_ya_yok(v: Option<&Value>, ad: &str) -> Result<Option<String>, String> {
    match v {
        None | Some(Value::Null) => Ok(None),
        Some(Value::String(s)) => Ok(Some(s.clone())),
        Some(o) => Err(format!("{ad} metin değil: {}", py_dumps(o))),
    }
}

/// `(d.get(k) or "")`.
fn metin_ya_bos(v: Option<&Value>, ad: &str) -> Result<String, String> {
    match v {
        Some(Value::String(s)) => Ok(s.clone()),
        Some(o) if !py_truthy(o) => Ok(String::new()),
        None => Ok(String::new()),
        Some(o) => Err(format!("{ad} metin değil: {}", py_dumps(o))),
    }
}

// ---------------------------------------------------------------- bronz

/// Transkriptte aynı asistan mesajı birden çok satırda yinelenir (uuid aynı, usage özdeş): uuid başına İLK satır alınır.
fn bronz_topla(proje_dizin: &str) -> Result<Vec<Kayit>, String> {
    let mut adlar: Vec<String> = match std::fs::read_dir(proje_dizin) {
        Ok(d) => d
            .flatten()
            .map(|e| e.file_name().to_string_lossy().into_owned())
            .filter(|a| !a.starts_with('.') && (if cfg!(windows) { a.to_lowercase().ends_with(".jsonl") } else { a.ends_with(".jsonl") }))
            .collect(),
        Err(_) => vec![],
    };
    adlar.sort();
    let (mut olaylar, mut gorulen): (Vec<Kayit>, HashSet<String>) = (vec![], HashSet::new());
    for kaynak in adlar {
        let yol = py::join(proje_dizin, &kaynak);
        let ham = std::fs::read(&yol).map_err(|e| format!("{yol}: {e}"))?;
        let metin = py::evrensel_satir(&String::from_utf8_lossy(&ham));
        let oturum_ad: String = {
            let n = kaynak.chars().count();
            kaynak.chars().take(n.saturating_sub(6)).collect()
        };
        for satir in metin.split('\n') {
            let r: Value = match serde_json::from_str(satir) {
                Ok(v) => v,
                Err(_) => continue,
            };
            let r = match r {
                Value::Object(o) => o,
                diger => return Err(format!("transkript satırı nesne değil: {}", py_dumps(&diger))),
            };
            if r.get("type") != Some(&Value::String("assistant".into())) {
                continue;
            }
            let m = match r.get("message") {
                Some(v) if py_truthy(v) => v.clone(),
                _ => json!({}),
            };
            let u = match &m {
                Value::Object(mo) => mo.get("usage"),
                _ => None,
            };
            let u = match u {
                Some(Value::Object(u)) => u,
                _ => continue,
            };
            let uuid = match r.get("uuid") {
                Some(v) if py_truthy(v) => v,
                _ => continue,
            };
            let uuid_s = match uuid {
                Value::String(s) => s.clone(),
                diger => return Err(format!("uuid metin değil: {}", py_dumps(diger))),
            };
            if !gorulen.insert(uuid_s) {
                continue;
            }
            let mo = m.as_object().unwrap();
            let oturum = match r.get("sessionId") {
                Some(v) if py_truthy(v) => v.clone(),
                _ => Value::String(oturum_ad.clone()),
            };
            let al = |k: &str| r.get(k).cloned().unwrap_or(Value::Null);
            let ual = |k: &str| u.get(k).cloned().unwrap_or(Value::Null);
            let dusunme = match u.get("output_tokens_details") {
                Some(Value::Object(d)) => d.get("thinking_tokens").cloned().unwrap_or(Value::Null),
                _ => Value::Null,
            };
            let mut o = Kayit::new();
            o.insert("olay_id".into(), uuid.clone());
            o.insert("ts".into(), al("timestamp"));
            o.insert("oturum".into(), oturum);
            o.insert("request_id".into(), al("requestId"));
            o.insert("model".into(), mo.get("model").cloned().unwrap_or(Value::Null));
            o.insert("effort".into(), al("effort"));
            o.insert("is_sidechain".into(), Value::Bool(r.get("isSidechain").is_some_and(py_truthy)));
            o.insert("input_tokens".into(), ual("input_tokens"));
            o.insert("cache_creation_input_tokens".into(), ual("cache_creation_input_tokens"));
            o.insert("cache_read_input_tokens".into(), ual("cache_read_input_tokens"));
            o.insert("output_tokens".into(), ual("output_tokens"));
            o.insert("thinking_tokens".into(), dusunme);
            o.insert("kaynak_dosya".into(), Value::String(kaynak.clone()));
            olaylar.push(o);
        }
    }
    Ok(olaylar)
}

// ---------------------------------------------------------------- silver

struct Silver {
    olay_id: String,
    ts_utc: Option<String>,
    ts_tr: Option<String>,
    tarih_tr: Option<String>,
    saat_tr: Option<String>,
    oturum_id: String,
    oturum_kisa: String,
    sira: i64,
    model: Option<String>,
    effort: Option<String>,
    is_sidechain: i64,
    input_tokens: i64,
    cache_creation: i64,
    cache_read: i64,
    baglam: i64,
    output_tokens: i64,
    thinking: Sql,
    ustu_128k: i64,
    request_id: Option<String>,
    kaynak_dosya: Option<String>,
}

fn silver_satirlari(tum: &[&Kayit]) -> Result<Vec<Silver>, String> {
    let mut sira: HashMap<String, i64> = HashMap::new();
    let mut cikti = Vec::with_capacity(tum.len());
    for o in tum {
        let olay_id = match o.get("olay_id") {
            Some(Value::String(s)) => s.clone(),
            _ => return Err("olay_id metin değil".into()),
        };
        let ts_utc = metin_ya_yok(o.get("ts"), "ts")?;
        let oturum = match o.get("oturum") {
            Some(Value::String(s)) => s.clone(),
            diger => return Err(format!("oturum metin değil: {}", diger.map(py_dumps).unwrap_or_else(|| "(yok)".into()))),
        };
        let (ts_tr, tarih_tr, saat_tr) = match parse_ts(ts_utc.as_deref().unwrap_or("")) {
            Some(u) => {
                let (a, b, c) = tr_bicim(u)?;
                (Some(a), Some(b), Some(c))
            }
            None => (None, None, None),
        };
        let n = sira.entry(oturum.clone()).or_insert(0);
        *n += 1;
        let inp = say(o.get("input_tokens"))?;
        let cc = say(o.get("cache_creation_input_tokens"))?;
        let cr = say(o.get("cache_read_input_tokens"))?;
        let baglam = inp.checked_add(cc).and_then(|x| x.checked_add(cr)).ok_or("tamsayı taşması")?;
        let model = metin_ya_bos(o.get("model"), "model")?.replace("claude-", "");
        let thinking = match o.get("thinking_tokens") {
            None | Some(Value::Null) => Sql::Null,
            Some(Value::Bool(b)) => Sql::Integer(*b as i64),
            Some(Value::Number(x)) => match x.as_i64() {
                Some(i) => Sql::Integer(i),
                None => Sql::Real(x.as_f64().ok_or("thinking_tokens sayı değil")?),
            },
            Some(d) => return Err(format!("thinking_tokens sayı değil: {}", py_dumps(d))),
        };
        cikti.push(Silver {
            olay_id,
            ts_utc,
            ts_tr,
            tarih_tr,
            saat_tr,
            oturum_kisa: oturum.chars().take(8).collect(),
            oturum_id: oturum,
            sira: *n,
            model: if model.is_empty() { None } else { Some(model) },
            effort: metin_ya_yok(o.get("effort"), "effort")?,
            is_sidechain: o.get("is_sidechain").is_some_and(py_truthy) as i64,
            input_tokens: inp,
            cache_creation: cc,
            cache_read: cr,
            baglam,
            output_tokens: say(o.get("output_tokens"))?,
            thinking,
            ustu_128k: (baglam > ESIK_128K) as i64,
            request_id: metin_ya_yok(o.get("request_id"), "request_id")?,
            kaynak_dosya: metin_ya_yok(o.get("kaynak_dosya"), "kaynak_dosya")?,
        });
    }
    Ok(cikti)
}

const SEMA: &str = "
        CREATE TABLE IF NOT EXISTS baglam_olay (
          olay_id TEXT PRIMARY KEY, ts_utc TEXT, ts_tr TEXT, tarih_tr TEXT, saat_tr TEXT, oturum_id TEXT NOT NULL, oturum_kisa TEXT, sira INTEGER,
          model TEXT, effort TEXT, is_sidechain INTEGER, input_tokens INTEGER, cache_creation_input_tokens INTEGER, cache_read_input_tokens INTEGER,
          baglam INTEGER, output_tokens INTEGER, thinking_tokens INTEGER, ustu_128k INTEGER, request_id TEXT, kaynak_dosya TEXT
        );
        DELETE FROM baglam_olay;
        CREATE VIEW IF NOT EXISTS v_baglam_seyri AS
          SELECT oturum_kisa, MIN(tarih_tr) AS tarih, MIN(saat_tr) AS ilk_saat, MAX(saat_tr) AS son_saat, COUNT(*) AS tur,
                 (SELECT b2.baglam FROM baglam_olay b2 WHERE b2.oturum_id=b.oturum_id AND b2.is_sidechain=0 ORDER BY b2.sira LIMIT 1) AS ilk_tur_baglam,
                 MAX(baglam) AS max_baglam, (SELECT b3.baglam FROM baglam_olay b3 WHERE b3.oturum_id=b.oturum_id ORDER BY b3.sira DESC LIMIT 1) AS son_baglam,
                 SUM(ustu_128k) AS tur_128k_ustu, SUM(output_tokens) AS toplam_cikti, SUM(COALESCE(thinking_tokens,0)) AS toplam_thinking,
                 SUM(is_sidechain) AS yan_zincir_tur, MAX(model) AS model
          FROM baglam_olay b GROUP BY oturum_id ORDER BY tarih DESC, ilk_saat DESC;
        CREATE VIEW IF NOT EXISTS v_baglam_gunluk AS
          SELECT tarih_tr, model, COUNT(*) AS tur, COUNT(DISTINCT oturum_id) AS oturum, MAX(baglam) AS max_baglam, ROUND(AVG(baglam)) AS ort_baglam,
                 SUM(ustu_128k) AS tur_128k_ustu, SUM(output_tokens) AS toplam_cikti, SUM(cache_read_input_tokens) AS toplam_cache_read,
                 SUM(cache_creation_input_tokens) AS toplam_cache_create
          FROM baglam_olay GROUP BY tarih_tr, model ORDER BY tarih_tr DESC, model;
        ";

// ---------------------------------------------------------------- CSV (Python `csv.writer`, excel kipi)

fn csv_alan(d: ValueRef) -> String {
    let ham = match d {
        ValueRef::Null => String::new(),
        ValueRef::Integer(i) => i.to_string(),
        ValueRef::Real(f) => float_repr(f),
        ValueRef::Text(t) => String::from_utf8_lossy(t).into_owned(),
        ValueRef::Blob(_) => String::new(),
    };
    if ham.contains([',', '"', '\r', '\n']) { format!("\"{}\"", ham.replace('"', "\"\"")) } else { ham }
}

fn gorunum_csv(con: &Connection, ad: &str, yol: &str) -> Result<(), String> {
    let mut st = con.prepare(&format!("SELECT * FROM {ad}")).map_err(|e| e.to_string())?;
    let sutunlar: Vec<String> = st.column_names().iter().map(|s| s.to_string()).collect();
    let n = sutunlar.len();
    let mut cikti = sutunlar.join(",");
    cikti.push_str("\r\n");
    let mut satirlar = st.query([]).map_err(|e| e.to_string())?;
    while let Some(r) = satirlar.next().map_err(|e| e.to_string())? {
        let alanlar: Vec<String> = (0..n).map(|i| csv_alan(r.get_ref_unwrap(i))).collect();
        cikti.push_str(&alanlar.join(","));
        cikti.push_str("\r\n");
    }
    std::fs::write(yol, cikti).map_err(|e| format!("{yol}: {e}"))
}

// ---------------------------------------------------------------- ana akış

fn calistir(proje_dizin: &str, repo: &str, kuru: bool, sessiz: bool) -> Result<i32, String> {
    let bronz_yol = py::join(&py::join(&py::join(repo, "veri"), "bronz"), "baglam-olay.jsonl");
    let mut mevcut: HashMap<String, Kayit> = HashMap::new();
    if Path::new(&bronz_yol).exists() {
        let metin = match py::oku_kati(Path::new(&bronz_yol)) {
            Ok(t) => t,
            Err(py::OkuHata::Io(e)) => return Err(format!("{bronz_yol}: {e}")),
            Err(py::OkuHata::Kod) => return Err(format!("{bronz_yol}: UnicodeDecodeError")),
        };
        for satir in metin.split('\n') {
            if let Ok(Value::Object(o)) = serde_json::from_str::<Value>(satir) {
                match o.get("olay_id") {
                    Some(Value::String(s)) => {
                        mevcut.insert(s.clone(), o);
                    }
                    Some(Value::Array(_)) | Some(Value::Object(_)) | None => {}
                    Some(d) => return Err(format!("olay_id metin değil: {}", py_dumps(d))),
                }
            }
        }
    }
    let toplanan = bronz_topla(proje_dizin)?;
    let yeni: Vec<Kayit> = toplanan
        .into_iter()
        .filter(|o| match o.get("olay_id") {
            Some(Value::String(s)) => !mevcut.contains_key(s),
            _ => true,
        })
        .collect();
    if !kuru && !yeni.is_empty() {
        let dizin = py::join(&py::join(repo, "veri"), "bronz");
        std::fs::create_dir_all(&dizin).map_err(|e| format!("{dizin}: {e}"))?;
        let mut f = std::fs::OpenOptions::new().append(true).create(true).open(&bronz_yol).map_err(|e| format!("{bronz_yol}: {e}"))?;
        let mut tampon = String::new();
        for o in &yeni {
            tampon.push_str(&py_dumps(&Value::Object(o.clone())));
            tampon.push_str(SATIR_SONU);
        }
        f.write_all(tampon.as_bytes()).map_err(|e| format!("{bronz_yol}: {e}"))?;
    }
    let mut anahtarli: Vec<(String, String, &Kayit)> = Vec::new();
    for o in mevcut.values().chain(yeni.iter()) {
        let ts = metin_ya_bos(o.get("ts"), "ts")?;
        let id = match o.get("olay_id") {
            Some(Value::String(s)) => s.clone(),
            _ => return Err("olay_id metin değil".into()),
        };
        anahtarli.push((ts, id, o));
    }
    anahtarli.sort_by(|a, b| (&a.0, &a.1).cmp(&(&b.0, &b.1)));
    let tum: Vec<&Kayit> = anahtarli.into_iter().map(|(_, _, o)| o).collect();
    let satirlar = silver_satirlari(&tum)?;

    let db_yol = py::join(&py::join(repo, "veri"), "baglam.sqlite");
    let mut testler: Vec<(&str, i64, &str)> = vec![];
    let mut uyarilar: Vec<String> = vec![];
    if !kuru {
        let mut con = Connection::open(&db_yol).map_err(|e| format!("{db_yol}: {e}"))?;
        con.execute_batch(SEMA).map_err(|e| e.to_string())?;
        {
            let tx = con.transaction().map_err(|e| e.to_string())?;
            {
                let mut st = tx
                    .prepare("INSERT INTO baglam_olay VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
                    .map_err(|e| e.to_string())?;
                let m = |s: &Option<String>| s.clone().map(Sql::Text).unwrap_or(Sql::Null);
                for s in &satirlar {
                    let p: Vec<Sql> = vec![
                        Sql::Text(s.olay_id.clone()),
                        m(&s.ts_utc),
                        m(&s.ts_tr),
                        m(&s.tarih_tr),
                        m(&s.saat_tr),
                        Sql::Text(s.oturum_id.clone()),
                        Sql::Text(s.oturum_kisa.clone()),
                        Sql::Integer(s.sira),
                        m(&s.model),
                        m(&s.effort),
                        Sql::Integer(s.is_sidechain),
                        Sql::Integer(s.input_tokens),
                        Sql::Integer(s.cache_creation),
                        Sql::Integer(s.cache_read),
                        Sql::Integer(s.baglam),
                        Sql::Integer(s.output_tokens),
                        s.thinking.clone(),
                        Sql::Integer(s.ustu_128k),
                        m(&s.request_id),
                        m(&s.kaynak_dosya),
                    ];
                    st.execute(params_from_iter(p)).map_err(|e| e.to_string())?;
                }
            }
            tx.commit().map_err(|e| e.to_string())?;
        }
        for (ad, sql) in [
            ("baglam_olay.olay_id unique", "SELECT COUNT(*) FROM (SELECT olay_id FROM baglam_olay GROUP BY olay_id HAVING COUNT(*)>1)"),
            ("baglam_olay.oturum_id not_null", "SELECT COUNT(*) FROM baglam_olay WHERE oturum_id IS NULL OR oturum_id=''"),
            ("baglam_olay.baglam ≥ 0", "SELECT COUNT(*) FROM baglam_olay WHERE baglam < 0"),
        ] {
            let n: i64 = con.query_row(sql, [], |r| r.get(0)).map_err(|e| e.to_string())?;
            testler.push((ad, n, if n == 0 { "PASS" } else { "ERROR" }));
        }
        let sdir = py::join(&py::join(repo, "veri"), "sozlesme");
        std::fs::create_dir_all(&sdir).map_err(|e| format!("{sdir}: {e}"))?;
        let syol = py::join(&sdir, "baglam_olay.json");
        if !Path::new(&syol).exists() {
            let mut st = con.prepare("PRAGMA table_info(baglam_olay)").map_err(|e| e.to_string())?;
            let kolonlar: Vec<Value> = st
                .query_map([], |r| {
                    let ad: String = r.get(1)?;
                    let tip: String = r.get(2)?;
                    let nn: i64 = r.get(3)?;
                    let pk: i64 = r.get(5)?;
                    Ok(json!({"ad": ad, "tip": if tip.is_empty() { "ANY".to_string() } else { tip }, "not_null": nn != 0, "pk": pk != 0}))
                })
                .map_err(|e| e.to_string())?
                .collect::<Result<_, _>>()
                .map_err(|e: rusqlite::Error| e.to_string())?;
            let belge = json!({"tablo": "baglam_olay", "surum": "1.0.0-deneysel-m29", "katman": "silver",
                "grain": "1 satır = 1 asistan turu (API çağrısı) usage kaydı; baglam = input+cache_creation+cache_read",
                "kolonlar": kolonlar, "kural": "additive-only; kırıcı = silme/tip/kısıt/yeniden-ad", "kaynak": "tools/baglam-seyir.py (KB-50/52 a, İB-22, 2026-08-22)"});
            let metin = py::json_girintili(&belge);
            let metin = if cfg!(windows) { metin.replace('\n', "\r\n") } else { metin };
            std::fs::write(&syol, metin).map_err(|e| format!("{syol}: {e}"))?;
        }
        let gdir = py::join(&py::join(repo, "veri"), "gorunum");
        std::fs::create_dir_all(&gdir).map_err(|e| format!("{gdir}: {e}"))?;
        for v in ["v_baglam_seyri", "v_baglam_gunluk"] {
            gorunum_csv(&con, v, &py::join(&gdir, &format!("{v}.csv")))?;
        }
        let mut st = con
            .prepare("SELECT oturum_kisa, tarih, max_baglam, ilk_tur_baglam, tur_128k_ustu FROM v_baglam_seyri")
            .map_err(|e| e.to_string())?;
        let satir: Vec<(Option<String>, Option<String>, Option<i64>, Option<i64>, Option<i64>)> = st
            .query_map([], |r| Ok((r.get(0)?, r.get(1)?, r.get(2)?, r.get(3)?, r.get(4)?)))
            .map_err(|e| e.to_string())?
            .collect::<Result<_, _>>()
            .map_err(|e: rusqlite::Error| e.to_string())?;
        let goster = |s: &Option<String>| s.clone().unwrap_or_else(|| "None".into());
        for (ok, tarih, max_b, ilk_b, n128) in &satir {
            let max_b = max_b.unwrap_or(0);
            if max_b > ESIK_128K {
                uyarilar.push(format!(
                    "UYARI 128K: oturum {} ({}) max bağlam {max_b} · {} tur üstte (KB-52 uzun-koşum politikası)",
                    goster(ok),
                    goster(tarih),
                    n128.unwrap_or(0)
                ));
            }
            if ilk_b.unwrap_or(0) > ESIK_STATIK {
                uyarilar.push(format!(
                    "UYARI statik-önek: oturum {} ({}) ilk-tur bağlamı {} > {ESIK_STATIK} (KB-50 a ≤~60k; kestirim = ilk mesaj dahil)",
                    goster(ok),
                    goster(tarih),
                    ilk_b.unwrap_or(0)
                ));
            }
        }
    }
    // --- çıktı ---
    let oturumlar: HashSet<&str> = tum.iter().filter_map(|o| o.get("oturum").and_then(Value::as_str)).collect();
    py::print(&format!(
        "baglam-seyir: bronz +{} yeni / {} toplam tur · {} oturum · silver baglam_olay {} · gold v_baglam_seyri/v_baglam_gunluk{}",
        yeni.len(),
        tum.len(),
        oturumlar.len(),
        if kuru { 0 } else { satirlar.len() },
        if kuru { " · KURU" } else { "" }
    ));
    if !sessiz {
        for (ad, n, s) in &testler {
            py::print(&format!("  [{s}] test {ad} → ihlal {n}"));
        }
        if !kuru {
            let con = Connection::open(&db_yol).map_err(|e| format!("{db_yol}: {e}"))?;
            let mut st = con
                .prepare("SELECT oturum_kisa, tarih, tur, ilk_tur_baglam, max_baglam, son_baglam, tur_128k_ustu, toplam_cikti FROM v_baglam_seyri LIMIT 8")
                .map_err(|e| e.to_string())?;
            let mut rows = st.query([]).map_err(|e| e.to_string())?;
            let s = |d: ValueRef| -> String {
                match d {
                    ValueRef::Null => "None".into(),
                    ValueRef::Integer(i) => i.to_string(),
                    ValueRef::Real(f) => float_repr(f),
                    ValueRef::Text(t) => String::from_utf8_lossy(t).into_owned(),
                    ValueRef::Blob(_) => String::new(),
                }
            };
            while let Some(r) = rows.next().map_err(|e| e.to_string())? {
                let g = |i: usize| s(r.get_ref_unwrap(i));
                py::print(&format!(
                    "  {} {} tur {} · ilk {} · max {} · son {} · 128k+ {} · çıktı {}",
                    g(0),
                    g(1),
                    py::saga_hizala(&g(2), 4),
                    py::saga_hizala(&g(3), 7),
                    py::saga_hizala(&g(4), 7),
                    py::saga_hizala(&g(5), 7),
                    py::saga_hizala(&g(6), 3),
                    g(7)
                ));
            }
        }
    }
    let n128 = uyarilar.iter().filter(|u| u.starts_with("UYARI 128K")).count();
    let nst = uyarilar.iter().filter(|u| u.starts_with("UYARI statik")).count();
    if !uyarilar.is_empty() {
        py::err(&format!(
            "UYARI baglam-seyir: {n128} oturum 128K üstü · {nst} oturum statik-önek >60k (KB-50/52 a; tam liste veri/gorunum/v_baglam_seyri.csv)\n"
        ));
        for u in uyarilar.iter().take(3) {
            py::err(&format!("  {u}\n"));
        }
    }
    Ok(if testler.iter().any(|t| t.2 == "ERROR") { 3 } else { 0 })
}

pub fn kos(argv: &[String]) -> i32 {
    let a = match ayrisan().ayristir(argv) {
        Ok(a) => a,
        Err(k) => return k,
    };
    let cwd = std::env::current_dir().map(|d| d.to_string_lossy().into_owned()).unwrap_or_default();
    let proje_dizin = a.metin("proje_dizin").map(String::from).unwrap_or_else(|| harness_anahtar::proje_dizin(None));
    let repo = py::abspath(a.metin("repo").unwrap_or(&cwd));
    if !Path::new(&proje_dizin).is_dir() {
        py::err(&format!("[HATA] transkript dizini yok: {proje_dizin}\n"));
        return 1;
    }
    match calistir(&proje_dizin, &repo, a.bayrak("kuru"), a.bayrak("sessiz")) {
        Ok(k) => k,
        Err(e) => py::coker(&e),
    }
}
