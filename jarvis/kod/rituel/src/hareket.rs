//! `tools/hareket-tablo.py` karşılığı: Jarvis'in TÜM HAREKETLERİNİ (araç çağrılarını) transkriptten repoya indirir:
//! BRONZ (`veri/bronz/hareket-olay.jsonl`) → SİLVER (`veri/baglam.sqlite` tablosu `hareket`) → GOLD (`veri/gorunum/*.csv`)
//! + insan-yüzü günlük (`raporlar/hareket/hareket-gunlugu-YYYY-MM-DD.md`).
//!
//! Bilinçli ayrışmalar (Python'da traceback olan durumlar `py::coker` ile stderr + çıkış 1):
//! beklenmedik JSON tipleri (ör. `message` sözlük değil, `timestamp` metin değil, `id` metin değil) çöker;
//! yazılan dosyalarda satır sonu her zaman LF (Python Windows'ta CRLF yazar; CSV her yerde CRLF'tir ve öyle kalır).
use crate::argparse::{Ayrisan, Secenek};
use crate::py::{self, float_repr};
use crate::harness_anahtar;
use chrono::{Datelike, Duration, NaiveDate, NaiveDateTime, NaiveTime, TimeZone};
use jarvis_hook::ortak::{py_dumps, py_truthy};
use regex::Regex;
use rusqlite::{Connection, params_from_iter, types::ValueRef};
use serde_json::{Map, Value, json};
use std::collections::{HashMap, HashSet};
use std::io::Write;
use std::path::Path;

/// `Err` = Python'da yakalanmamış istisna olurdu (gerekçe metni).
type S<T> = Result<T, String>;

const FIILLER: &[(&str, &str)] = &[
    ("Write", "yazdı"),
    ("Edit", "düzenledi"),
    ("MultiEdit", "düzenledi"),
    ("NotebookEdit", "düzenledi"),
    ("Read", "okudu"),
    ("Bash", "koştu"),
    ("Grep", "aradı"),
    ("Glob", "aradı"),
    ("Agent", "ajan gönderdi"),
    ("Task", "ajan gönderdi"),
    ("Skill", "skill çağırdı"),
    ("Workflow", "workflow başlattı"),
    ("WebFetch", "web'e baktı"),
    ("WebSearch", "web'e baktı"),
    ("TodoWrite", "görev listesi"),
    ("TaskCreate", "görev listesi"),
    ("TaskUpdate", "görev listesi"),
    ("TaskList", "görev listesi"),
    ("TaskGet", "görev listesi"),
    ("TaskOutput", "görev listesi"),
    ("TaskStop", "görev listesi"),
    ("AskUserQuestion", "sordu"),
    ("SendMessage", "mesaj yolladı"),
    ("ToolSearch", "araç aradı"),
    ("EnterPlanMode", "plan modu"),
    ("ExitPlanMode", "plan modu"),
    ("Monitor", "izledi"),
];

const BRONZ_BASLIK: &str = "# veri/bronz/hareket-olay.jsonl — BRONZ: Jarvis'in araç çağrısı olay kütüğü (1 satır = 1 çağrı; hedef var, içerik yok; append-only; tekil anahtar hareket_id). Üretici tools/hareket-tablo.py. Okunabilirlik ilkesi 08-17. md.49: yalnız jarvis transkriptleri.\n";

const SILVER_BETIK: &str = "
        CREATE TABLE IF NOT EXISTS hareket (
          hareket_id TEXT PRIMARY KEY, ts_utc TEXT, ts_tr TEXT, tarih_tr TEXT, saat_tr TEXT, oturum_id TEXT, oturum_kisa TEXT, sira INTEGER,
          arac TEXT NOT NULL, fiil TEXT, hedef TEXT, dosya TEXT, repo_ici INTEGER, sonuc TEXT, model TEXT, kaynak_dosya TEXT, yuklendi_head TEXT,
          okuma_tipi TEXT
        );
        DELETE FROM hareket;
        CREATE VIEW IF NOT EXISTS v_okuma_orani AS
          SELECT tarih_tr, oturum_kisa,
                 SUM(CASE WHEN okuma_tipi='aralik' THEN 1 ELSE 0 END) AS aralik,
                 SUM(CASE WHEN okuma_tipi='butun' THEN 1 ELSE 0 END) AS butun,
                 ROUND(1.0*SUM(CASE WHEN okuma_tipi='aralik' THEN 1 ELSE 0 END) / NULLIF(SUM(CASE WHEN okuma_tipi IN ('aralik','butun') THEN 1 ELSE 0 END),0), 3) AS aralik_orani,
                 SUM(CASE WHEN okuma_tipi='aralik' AND arac='Read' THEN 1 ELSE 0 END) AS read_aralik,
                 SUM(CASE WHEN okuma_tipi='butun' AND arac='Read' THEN 1 ELSE 0 END) AS read_butun
          FROM hareket WHERE okuma_tipi IS NOT NULL GROUP BY tarih_tr, oturum_kisa ORDER BY tarih_tr DESC, oturum_kisa;
        CREATE VIEW IF NOT EXISTS v_hareket_gunluk AS
          SELECT tarih_tr, oturum_kisa, fiil, COUNT(*) AS n, MIN(saat_tr) AS ilk, MAX(saat_tr) AS son,
                 SUM(CASE WHEN sonuc='hata' THEN 1 ELSE 0 END) AS hata, COUNT(DISTINCT CASE WHEN fiil IN ('yazdı','düzenledi') THEN dosya END) AS yazilan_dosya
          FROM hareket GROUP BY tarih_tr, oturum_kisa, fiil ORDER BY tarih_tr DESC, oturum_kisa, n DESC;
        CREATE VIEW IF NOT EXISTS v_son_hareketler AS
          SELECT ROW_NUMBER() OVER (ORDER BY ts_utc DESC) AS n, tarih_tr, saat_tr, oturum_kisa, sira, fiil, arac, hedef, sonuc, model, hareket_id
          FROM hareket ORDER BY ts_utc DESC LIMIT 300;
        ";

fn ayrisan() -> Ayrisan {
    Ayrisan::yeni(
        "hareket-tablo.py",
        None,
        vec![
            Secenek::deger(&["--repo"], "repo", None),
            Secenek::deger(&["--proje-dizin"], "proje_dizin", None),
            Secenek::deger(&["--tarih"], "tarih", None),
            Secenek::bayrak(&["--tum"], "tum", None),
            Secenek::bayrak(&["--kuru"], "kuru", None),
            Secenek::bayrak(&["--sessiz"], "sessiz", None),
        ],
    )
}

struct Rx {
    bosluk: Regex,
    aralik: Regex,
    butun: Regex,
    is_adi: Regex,
}

impl Rx {
    fn yeni() -> Self {
        // Python `\s` (str deseni) \x1c-\x1f'i de boşluk sayar; Rust `\s` saymaz: sınıf açık yazıldı.
        Rx {
            bosluk: Regex::new(r"[\s\x1c-\x1f]+").unwrap(),
            aralik: Regex::new(r#"(sed[\s\x1c-\x1f]+-n[\s\x1c-\x1f]+['"]?\d+(,\d+)?p|\bhead[\s\x1c-\x1f]+(-n[\s\x1c-\x1f]*)?-?\d+|\btail[\s\x1c-\x1f]+(-n[\s\x1c-\x1f]*)?[-+]?\d+|\bawk[\s\x1c-\x1f]+['"]NR[\s\x1c-\x1f]*[<>=]|\bhead[\s\x1c-\x1f]+-c[\s\x1c-\x1f]*\d+)"#).unwrap(),
            butun: Regex::new(r"(^|[;&|][\s\x1c-\x1f]*)cat[\s\x1c-\x1f]+[^|<>;&]+\.(md|py|json|jsonl|txt|sh|sql|d2|csv)\b").unwrap(),
            is_adi: Regex::new(r#"name:[\s\x1c-\x1f]*['"]([^'"]+)"#).unwrap(),
        }
    }
}

// ---------------------------------------------------------------- Python değer yardımcıları
/// Python `repr(v)` (JSON'dan gelen değerler için).
fn py_repr_v(v: &Value) -> String {
    match v {
        Value::Null => "None".into(),
        Value::Bool(true) => "True".into(),
        Value::Bool(false) => "False".into(),
        Value::Number(n) => {
            if let Some(i) = n.as_i64() {
                i.to_string()
            } else if let Some(u) = n.as_u64() {
                u.to_string()
            } else {
                float_repr(n.as_f64().unwrap_or(0.0))
            }
        }
        Value::String(s) => py::repr(s),
        Value::Array(a) => format!("[{}]", a.iter().map(py_repr_v).collect::<Vec<_>>().join(", ")),
        Value::Object(o) => format!("{{{}}}", o.iter().map(|(k, v)| format!("{}: {}", py::repr(k), py_repr_v(v))).collect::<Vec<_>>().join(", ")),
    }
}

/// Python `str(v)`.
fn py_str(v: &Value) -> String {
    match v {
        Value::String(s) => s.clone(),
        _ => py_repr_v(v),
    }
}

fn py_str_ops(v: Option<&Value>) -> String {
    v.map(py_str).unwrap_or_else(|| "None".into())
}

/// `d.get(a) or d.get(b) or ...`: ilk doğru değer; hiçbiri doğru değilse sonuncusu (ya da yok).
fn yada<'a>(m: &'a Map<String, Value>, anahtarlar: &[&str]) -> Option<&'a Value> {
    let mut son = None;
    for a in anahtarlar {
        son = m.get(*a);
        if let Some(v) = son
            && py_truthy(v)
        {
            return Some(v);
        }
    }
    son
}

/// `(değer or "")` metin beklenen yerde: yok/yanlış → "", metin → kendisi, başka doğru değer → Python'da istisna.
fn metin_ya_bos(v: Option<&Value>, ne: &str) -> S<String> {
    match v {
        None => Ok(String::new()),
        Some(Value::String(s)) => Ok(s.clone()),
        Some(x) if !py_truthy(x) => Ok(String::new()),
        Some(x) => Err(format!("{ne}: metin beklenirken {}", py_repr_v(x))),
    }
}

/// `(değer or {})` sonrası `.get`: sözlük olmayan doğru değer → AttributeError.
fn nesne_ya_bos<'a>(v: Option<&'a Value>, bos: &'a Map<String, Value>, ne: &str) -> S<&'a Map<String, Value>> {
    match v {
        None => Ok(bos),
        Some(Value::Object(m)) => Ok(m),
        Some(x) if !py_truthy(x) => Ok(bos),
        Some(x) => Err(format!("{ne}: sözlük beklenirken {}", py_repr_v(x))),
    }
}

/// `for x in (değer or [])`: yalnız sözlük öğeler ilgilendirir (metin/sözlük yinelemesi sözlük öğe vermez); sayı → TypeError.
fn elemanlar<'a>(v: Option<&'a Value>, ne: &str) -> S<Vec<&'a Value>> {
    match v {
        None => Ok(vec![]),
        Some(x) if !py_truthy(x) => Ok(vec![]),
        Some(Value::Array(a)) => Ok(a.iter().collect()),
        Some(Value::String(_) | Value::Object(_)) => Ok(vec![]),
        Some(x) => Err(format!("{ne}: yinelenemez {}", py_repr_v(x))),
    }
}

fn opt_metin(v: Option<&Value>, ne: &str) -> S<Option<String>> {
    match v {
        None | Some(Value::Null) => Ok(None),
        Some(Value::String(s)) => Ok(Some(s.clone())),
        Some(x) => Err(format!("{ne}: metin beklenirken {}", py_repr_v(x))),
    }
}

// ---------------------------------------------------------------- Yol / özet
fn kisa_yol(p: Option<&Value>, repo: &str, ev: &str) -> S<(Option<String>, Option<String>, bool)> {
    let p = match p {
        None => return Ok((None, None, false)),
        Some(x) if !py_truthy(x) => return Ok((None, None, false)),
        Some(Value::String(s)) => s.as_str(),
        Some(x) => return Err(format!("yol metin değil: {}", py_repr_v(x))),
    };
    let ap = if !p.starts_with('/') { py::abspath(&py::expanduser(p)) } else { p.to_string() };
    let onek = format!("{repo}{}", py::SEP);
    if ap.starts_with(&onek) {
        let g: String = ap[onek.len()..].to_string();
        return Ok((Some(g.clone()), Some(g), true));
    }
    Ok((Some(ap.replace(ev, "~")), None, false))
}

fn girdi_ozet(arac: &str, inp: &Map<String, Value>, repo: &str, ev: &str, rx: &Rx) -> S<(String, Option<String>, bool)> {
    let mut dosya = None;
    let mut repo_ici = false;
    let h: String = if matches!(arac, "Write" | "Edit" | "MultiEdit" | "NotebookEdit" | "Read") {
        let (h0, d, r) = kisa_yol(yada(inp, &["file_path", "notebook_path"]), repo, ev)?;
        dosya = d;
        repo_ici = r;
        if arac == "Read" {
            let h0 = h0.unwrap_or_else(|| "None".into());
            let ofs = inp.get("offset").filter(|v| !v.is_null());
            let lim = inp.get("limit").filter(|v| !v.is_null());
            if ofs.is_some() || lim.is_some() {
                format!("{h0} [aralık {}+{}]", ofs.map(py_str).unwrap_or_else(|| "0".into()), lim.map(py_str).unwrap_or_else(|| "∞".into()))
            } else {
                format!("{h0} [bütün]")
            }
        } else {
            h0.unwrap_or_default()
        }
    } else if arac == "Bash" {
        let komut = metin_ya_bos(inp.get("command"), "Bash command")?;
        let c = py::strip(&rx.bosluk.replace_all(&komut, " ")).to_string();
        let acik = metin_ya_bos(inp.get("description"), "Bash description")?;
        let uzun = c.chars().count() > 150;
        let h = format!("{} ⟨{}{}⟩", py::strip(&acik), py::ilk(&c, 150), if uzun { "…" } else { "" });
        repo_ici = c.contains("jarvis");
        h
    } else if matches!(arac, "Grep" | "Glob") {
        let (yol, _, _) = kisa_yol(inp.get("path"), repo, ev)?;
        let yol = yol.filter(|y| !y.is_empty()).unwrap_or_else(|| ".".into());
        let desen = inp.get("pattern").map(py_str).unwrap_or_default();
        format!("{desen}  ({yol})")
    } else if matches!(arac, "Agent" | "Task") {
        let tip = match yada(inp, &["subagent_type", "agentType"]) {
            Some(v) if py_truthy(v) => py_str(v),
            _ => "agent".to_string(),
        };
        let acik = match inp.get("description") {
            Some(v) if py_truthy(v) => py_str(v),
            _ => py::ilk(&metin_ya_bos(inp.get("prompt"), "Agent prompt")?, 100),
        };
        format!("[{tip}] {acik}")
    } else if arac == "Skill" {
        let args = match inp.get("args") {
            Some(v) if py_truthy(v) => py_str(v),
            _ => String::new(),
        };
        py::strip(&format!("{} {args}", py_str_ops(inp.get("skill")))).to_string()
    } else if arac == "Workflow" {
        let sc = metin_ya_bos(inp.get("script"), "Workflow script")?;
        match rx.is_adi.captures(&sc) {
            Some(m) => m[1].to_string(),
            None => match yada(inp, &["name", "scriptPath"]) {
                Some(Value::String(s)) if !s.is_empty() => s.clone(),
                Some(x) if py_truthy(x) => return Err(format!("Workflow adı metin değil: {}", py_repr_v(x))),
                _ => "script".to_string(),
            },
        }
    } else if arac == "WebFetch" {
        match inp.get("url") {
            None => String::new(),
            v => metin_ya_bos(v, "WebFetch url")?,
        }
    } else if arac == "WebSearch" {
        match inp.get("query") {
            None => String::new(),
            v => metin_ya_bos(v, "WebSearch query")?,
        }
    } else if arac == "AskUserQuestion" {
        let mut parcalar = vec![];
        for q in elemanlar(inp.get("questions"), "AskUserQuestion questions")? {
            if let Value::Object(q) = q {
                parcalar.push(py::ilk(&metin_ya_bos(q.get("question"), "AskUserQuestion question")?, 80));
            }
        }
        parcalar.join("; ")
    } else if arac == "SendMessage" {
        format!("→ {}", inp.get("to").map(py_str).unwrap_or_default())
    } else if arac.starts_with("mcp__") {
        let on = arac.split("__").last().unwrap_or("");
        format!("{on} {}", ilk3_dumps(inp))
    } else {
        ilk3_dumps(inp)
    };
    Ok((py::ilk(&h, 300), dosya, repo_ici))
}

/// `json.dumps({k: str(v)[:60] for k, v in list(inp.items())[:3]}, ensure_ascii=False)`.
fn ilk3_dumps(inp: &Map<String, Value>) -> String {
    let mut m = Map::new();
    for (k, v) in inp.iter().take(3) {
        m.insert(k.clone(), Value::String(py::ilk(&py_str(v), 60)));
    }
    py_dumps(&Value::Object(m))
}

/// İB-29 (KB-53 (a) Karar 62): okuma hareketini "aralik" | "butun" | None olarak sınıflar (yalnız argümandan).
fn okuma_tipi(arac: &str, inp: &Map<String, Value>, rx: &Rx) -> S<Option<&'static str>> {
    if arac == "Read" {
        let var = |k: &str| inp.get(k).is_some_and(|v| !v.is_null());
        return Ok(Some(if var("offset") || var("limit") { "aralik" } else { "butun" }));
    }
    if arac == "Bash" {
        let c = metin_ya_bos(inp.get("command"), "Bash command")?;
        if rx.aralik.is_match(&c) {
            return Ok(Some("aralik"));
        }
        if rx.butun.is_match(&c) {
            return Ok(Some("butun"));
        }
    }
    Ok(None)
}

// ---------------------------------------------------------------- Bronz
#[derive(Clone)]
struct Olay {
    hareket_id: String,
    ts: Option<String>,
    oturum: String,
    arac: String,
    girdi_ozet: Option<String>,
    okuma_tipi: Option<String>,
    dosya: Option<String>,
    repo_ici: bool,
    sonuc: Option<String>,
    model: Option<String>,
    kaynak_dosya: Option<String>,
    yuklendi_head: Option<String>,
}

fn bos_ya_metin(o: &Option<String>) -> Value {
    o.as_ref().map(|s| Value::String(s.clone())).unwrap_or(Value::Null)
}

impl Olay {
    /// `{**o, "yuklendi_head": head}` (anahtar sırası Python sözlüğüyle aynı).
    fn bronz_satir(&self, head: &str) -> String {
        let mut m = Map::new();
        m.insert("hareket_id".into(), json!(self.hareket_id));
        m.insert("ts".into(), bos_ya_metin(&self.ts));
        m.insert("oturum".into(), json!(self.oturum));
        m.insert("arac".into(), json!(self.arac));
        m.insert("girdi_ozet".into(), bos_ya_metin(&self.girdi_ozet));
        m.insert("okuma_tipi".into(), bos_ya_metin(&self.okuma_tipi));
        m.insert("dosya".into(), bos_ya_metin(&self.dosya));
        m.insert("repo_ici".into(), json!(self.repo_ici));
        m.insert("sonuc".into(), bos_ya_metin(&self.sonuc));
        m.insert("model".into(), bos_ya_metin(&self.model));
        m.insert("kaynak_dosya".into(), bos_ya_metin(&self.kaynak_dosya));
        m.insert("yuklendi_head".into(), json!(head));
        py_dumps(&Value::Object(m))
    }

    /// Bronz satırından (sözlük) olay; eksik zorunlu anahtar / beklenmedik tip Python'da istisnadır.
    fn bronzdan(v: &Value) -> S<Olay> {
        let Value::Object(m) = v else { return Err("bronz satırı sözlük değil".into()) };
        let zorunlu = |k: &str| -> S<String> {
            match m.get(k) {
                Some(Value::String(s)) => Ok(s.clone()),
                Some(x) => Err(format!("bronz {k}: metin beklenirken {}", py_repr_v(x))),
                None => Err(format!("bronz {k}: KeyError")),
            }
        };
        Ok(Olay {
            hareket_id: zorunlu("hareket_id")?,
            ts: opt_metin(m.get("ts"), "bronz ts")?,
            oturum: zorunlu("oturum")?,
            arac: zorunlu("arac")?,
            girdi_ozet: opt_metin(m.get("girdi_ozet"), "bronz girdi_ozet")?,
            okuma_tipi: opt_metin(m.get("okuma_tipi"), "bronz okuma_tipi")?,
            dosya: opt_metin(m.get("dosya"), "bronz dosya")?,
            repo_ici: m.get("repo_ici").is_some_and(py_truthy),
            sonuc: opt_metin(m.get("sonuc"), "bronz sonuc")?,
            model: opt_metin(m.get("model"), "bronz model")?,
            kaynak_dosya: opt_metin(m.get("kaynak_dosya"), "bronz kaynak_dosya")?,
            yuklendi_head: opt_metin(m.get("yuklendi_head"), "bronz yuklendi_head")?,
        })
    }
}

/// `glob.glob(join(dizin, "*.jsonl"))` sıralı: gizli ad (`.` ile başlayan) atlanır; Windows'ta uzantı büyük/küçük harf duyarsız.
fn jsonl_dosyalar(dizin: &str) -> Vec<String> {
    let Ok(rd) = std::fs::read_dir(dizin) else { return vec![] };
    let mut adlar: Vec<String> = rd
        .filter_map(|e| e.ok())
        .map(|e| e.file_name().to_string_lossy().into_owned())
        .filter(|a| !a.starts_with('.') && if cfg!(windows) { a.to_lowercase().ends_with(".jsonl") } else { a.ends_with(".jsonl") })
        .collect();
    adlar.sort();
    adlar
}

fn bronz_topla(proje_dizin: &str, repo: &str, ev: &str, rx: &Rx) -> S<Vec<Olay>> {
    let bos = Map::new();
    let mut olaylar = vec![];
    for ad in jsonl_dosyalar(proje_dizin) {
        let yol = py::join(proje_dizin, &ad);
        let oturum: String = {
            let n = ad.chars().count();
            ad.chars().take(n.saturating_sub(6)).collect()
        };
        let bayt = std::fs::read(&yol).map_err(|e| format!("{yol}: {e}"))?;
        let metin = py::evrensel_satir(&String::from_utf8_lossy(&bayt));
        let mut rows: Vec<Value> = vec![];
        for l in metin.split('\n') {
            if let Ok(v) = serde_json::from_str::<Value>(l) {
                rows.push(v);
            }
        }
        let mut sonuc: HashMap<String, &'static str> = HashMap::new(); // tool_result → is_error haritası
        for r in &rows {
            let Value::Object(r) = r else { return Err(format!("{yol}: satır sözlük değil ({})", py_repr_v(r))) };
            if r.get("type").and_then(Value::as_str) == Some("user") {
                let msg = nesne_ya_bos(r.get("message"), &bos, "message")?;
                for x in elemanlar(msg.get("content"), "content")? {
                    let Value::Object(x) = x else { continue };
                    if x.get("type").and_then(Value::as_str) == Some("tool_result") {
                        match x.get("tool_use_id") {
                            Some(Value::String(id)) => {
                                sonuc.insert(id.clone(), if x.get("is_error").is_some_and(py_truthy) { "hata" } else { "tamam" });
                            }
                            Some(Value::Array(_) | Value::Object(_)) => return Err("tool_use_id: unhashable type".into()),
                            _ => {}
                        }
                    }
                }
            }
        }
        for r in &rows {
            let Value::Object(r) = r else { unreachable!() };
            if r.get("type").and_then(Value::as_str) != Some("assistant") {
                continue;
            }
            let msg = nesne_ya_bos(r.get("message"), &bos, "message")?;
            for x in elemanlar(msg.get("content"), "content")? {
                let Value::Object(x) = x else { continue };
                if x.get("type").and_then(Value::as_str) != Some("tool_use") {
                    continue;
                }
                let arac = match x.get("name") {
                    Some(Value::String(s)) if !s.is_empty() => s.clone(),
                    Some(v) if py_truthy(v) => return Err(format!("name metin değil: {}", py_repr_v(v))),
                    _ => "?".to_string(),
                };
                let hid = match x.get("id") {
                    Some(Value::String(s)) if !s.is_empty() => s.clone(),
                    Some(v) if py_truthy(v) => return Err(format!("id metin değil: {}", py_repr_v(v))),
                    _ => format!("{oturum}:{}:{arac}", py_str_ops(r.get("uuid"))),
                };
                let girdi = nesne_ya_bos(x.get("input"), &bos, "input")?;
                let (ozet, dosya, repo_ici) = girdi_ozet(&arac, girdi, repo, ev, rx)?;
                olaylar.push(Olay {
                    ts: opt_metin(r.get("timestamp"), "timestamp")?,
                    oturum: oturum.clone(),
                    okuma_tipi: okuma_tipi(&arac, girdi, rx)?.map(String::from),
                    girdi_ozet: Some(ozet),
                    dosya,
                    repo_ici,
                    sonuc: Some(sonuc.get(&hid).copied().unwrap_or("yok").to_string()),
                    model: opt_metin(msg.get("model"), "model")?,
                    kaynak_dosya: Some(ad.clone()),
                    yuklendi_head: None,
                    hareket_id: hid,
                    arac,
                });
            }
        }
    }
    Ok(olaylar)
}

// ---------------------------------------------------------------- Zaman
/// `datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(TR)`; ayrıştırılamazsa `None`.
/// Desteklenen: `YYYY-MM-DD` / `YYYYMMDD`, ayraç tek karakter, `HH[:MM[:SS[.f+]]]` ya da bitişik `HHMM[SS[.f+]]`, `+HH[:MM[:SS]]` / `+HHMM[SS]`.
fn iso_tr(s: &str) -> Option<NaiveDateTime> {
    let s = s.replace('Z', "+00:00");
    let c: Vec<char> = s.chars().collect();
    let say = |a: usize, b: usize| -> Option<u32> {
        let p = c.get(a..b)?;
        if p.iter().all(|x| x.is_ascii_digit()) { p.iter().collect::<String>().parse().ok() } else { None }
    };
    let (y, mo, d, sonra) = if c.len() >= 10 && c[4] == '-' && c[7] == '-' {
        (say(0, 4)?, say(5, 7)?, say(8, 10)?, 10)
    } else if c.len() >= 8 && c[..8].iter().all(|x| x.is_ascii_digit()) {
        (say(0, 4)?, say(4, 6)?, say(6, 8)?, 8)
    } else {
        return None;
    };
    if !(1..=9999).contains(&y) {
        return None;
    }
    let tarih = NaiveDate::from_ymd_opt(y as i32, mo, d)?;
    let (saat, ofset): (NaiveTime, Option<i64>) = if sonra == c.len() {
        (NaiveTime::from_hms_opt(0, 0, 0)?, None)
    } else {
        let zaman: Vec<char> = c[sonra + 1..].to_vec();
        if zaman.is_empty() {
            return None;
        }
        let tz_bas = zaman.iter().position(|x| *x == '+' || *x == '-');
        let (zs, tz) = match tz_bas {
            Some(i) => (&zaman[..i], Some(&zaman[i..])),
            None => (&zaman[..], None),
        };
        let zs: String = zs.iter().collect();
        let sayi = |t: &str| -> Option<u32> { if !t.is_empty() && t.chars().all(|x| x.is_ascii_digit()) { t.parse().ok() } else { None } };
        let (govde, kesir) = match zs.find(['.', ',']) {
            Some(i) => (zs[..i].to_string(), Some(zs[i + 1..].to_string())),
            None => (zs.clone(), None),
        };
        let parcalar: Vec<&str> = if govde.contains(':') {
            govde.split(':').collect()
        } else if govde.len() == 2 || govde.len() == 4 || govde.len() == 6 {
            govde.as_bytes().chunks(2).map(|b| std::str::from_utf8(b).unwrap_or("")).collect()
        } else {
            return None;
        };
        if parcalar.is_empty() || parcalar.len() > 3 || parcalar.iter().any(|p| p.len() != 2) || (kesir.is_some() && parcalar.len() != 3) {
            return None;
        }
        let hh = sayi(parcalar[0])?;
        let mm = parcalar.get(1).map(|p| sayi(p)).unwrap_or(Some(0))?;
        let ss = parcalar.get(2).map(|p| sayi(p)).unwrap_or(Some(0))?;
        let mikro = match kesir {
            Some(k) => {
                if !k.chars().all(|x| x.is_ascii_digit()) {
                    return None;
                }
                let mut k6: String = k.chars().take(6).collect();
                while k6.len() < 6 {
                    k6.push('0');
                }
                k6.parse::<u32>().ok()?
            }
            None => 0,
        };
        let saat = NaiveTime::from_hms_micro_opt(hh, mm, ss, mikro)?;
        let ofset = match tz {
            None => None,
            Some(t) => {
                let isaret: i64 = if t[0] == '+' { 1 } else { -1 };
                let g: String = t[1..].iter().collect();
                let p: Vec<&str> = if g.contains(':') {
                    g.split(':').collect()
                } else if g.len() == 2 || g.len() == 4 || g.len() == 6 {
                    g.as_bytes().chunks(2).map(|b| std::str::from_utf8(b).unwrap_or("")).collect()
                } else {
                    return None;
                };
                if p.is_empty() || p.len() > 3 || p.iter().any(|x| x.len() != 2) {
                    return None;
                }
                let h = sayi(p[0])? as i64;
                let m = p.get(1).map(|x| sayi(x)).unwrap_or(Some(0))? as i64;
                let sn = p.get(2).map(|x| sayi(x)).unwrap_or(Some(0))? as i64;
                let top = isaret * (h * 3600 + m * 60 + sn);
                if top.abs() >= 86400 {
                    return None;
                }
                Some(top)
            }
        };
        (saat, ofset)
    };
    let yerel = NaiveDateTime::new(tarih, saat);
    let utc = match ofset {
        Some(o) => yerel.checked_sub_signed(Duration::seconds(o))?,
        None => chrono::Local.from_local_datetime(&yerel).earliest()?.naive_utc(), // `astimezone` saf tarihi yerel saat sayar
    };
    // Python `astimezone`: ara UTC ya da sonuç 1..=9999 yıl dışına taşarsa OverflowError (yakalanır, `None`)
    let tr = utc.checked_add_signed(Duration::hours(3))?;
    if !(1..=9999).contains(&utc.date().year()) || !(1..=9999).contains(&tr.date().year()) {
        return None;
    }
    Some(tr)
}


// ---------------------------------------------------------------- Silver
struct Satir {
    hareket_id: String,
    ts_utc: Option<String>,
    ts_tr: Option<String>,
    tarih_tr: Option<String>,
    saat_tr: Option<String>,
    oturum_id: String,
    oturum_kisa: String,
    sira: i64,
    arac: String,
    fiil: String,
    hedef: Option<String>,
    dosya: Option<String>,
    repo_ici: i64,
    sonuc: Option<String>,
    model: Option<String>,
    kaynak_dosya: Option<String>,
    yuklendi_head: String,
    okuma_tipi: Option<String>,
}

fn fiil_bul(arac: &str) -> &'static str {
    if let Some((_, f)) = FIILLER.iter().find(|(a, _)| *a == arac) {
        return f;
    }
    if arac.starts_with("mcp__") { "MCP aracı" } else { "araç" }
}

fn fiil_enum() -> Vec<String> {
    let mut v: Vec<String> = FIILLER.iter().map(|(_, f)| f.to_string()).collect();
    v.push("MCP aracı".into());
    v.push("araç".into());
    v.sort();
    v.dedup();
    v
}

fn satir_uret(hepsi: &[Olay], head: &str) -> Vec<Satir> {
    let mut sira: HashMap<&str, i64> = HashMap::new();
    let mut satirlar = vec![];
    for o in hepsi {
        let n = sira.entry(o.oturum.as_str()).or_insert(0);
        *n += 1;
        let ttr = o.ts.as_deref().and_then(iso_tr);
        let model = o.model.clone().unwrap_or_default().replace("claude-", "");
        satirlar.push(Satir {
            hareket_id: o.hareket_id.clone(),
            ts_utc: o.ts.clone(),
            ts_tr: ttr.map(|t| {
                let mikro = t.and_utc().timestamp_subsec_micros();
                format!("{}{}+03:00", t.format("%Y-%m-%dT%H:%M:%S"), if mikro != 0 { format!(".{mikro:06}") } else { String::new() })
            }),
            tarih_tr: ttr.map(|t| t.format("%Y-%m-%d").to_string()),
            saat_tr: ttr.map(|t| t.format("%H:%M:%S").to_string()),
            oturum_id: o.oturum.clone(),
            oturum_kisa: py::ilk(&o.oturum, 8),
            sira: *n,
            arac: o.arac.clone(),
            fiil: fiil_bul(&o.arac).to_string(),
            hedef: o.girdi_ozet.clone(),
            dosya: o.dosya.clone(),
            repo_ici: i64::from(o.repo_ici),
            sonuc: o.sonuc.clone(),
            model: if model.is_empty() { None } else { Some(model) },
            kaynak_dosya: o.kaynak_dosya.clone(),
            yuklendi_head: o.yuklendi_head.clone().filter(|h| !h.is_empty()).unwrap_or_else(|| head.to_string()),
            okuma_tipi: o.okuma_tipi.clone(),
        });
    }
    satirlar
}

// ---------------------------------------------------------------- CSV (Python csv.writer, QUOTE_MINIMAL, "\r\n")
fn csv_alan(s: &str) -> String {
    if s.contains([',', '"', '\r', '\n']) { format!("\"{}\"", s.replace('"', "\"\"")) } else { s.to_string() }
}

fn csv_yaz(con: &Connection, gorunum: &str) -> S<String> {
    let mut st = con.prepare(&format!("SELECT * FROM {gorunum}")).map_err(|e| e.to_string())?;
    let kolonlar: Vec<String> = st.column_names().iter().map(|s| s.to_string()).collect();
    let mut cikti = format!("{}\r\n", kolonlar.iter().map(|k| csv_alan(k)).collect::<Vec<_>>().join(","));
    let mut rows = st.query([]).map_err(|e| e.to_string())?;
    while let Some(r) = rows.next().map_err(|e| e.to_string())? {
        let mut alanlar = vec![];
        for i in 0..kolonlar.len() {
            let a = match r.get_ref(i).map_err(|e| e.to_string())? {
                ValueRef::Null => String::new(),
                ValueRef::Integer(n) => n.to_string(),
                ValueRef::Real(f) => float_repr(f),
                ValueRef::Text(t) => csv_alan(&String::from_utf8_lossy(t)),
                ValueRef::Blob(b) => csv_alan(&format!("b{}", py::repr(&String::from_utf8_lossy(b)))),
            };
            alanlar.push(a);
        }
        cikti.push_str(&alanlar.join(","));
        cikti.push_str("\r\n");
    }
    Ok(cikti)
}

fn yaz(yol: &str, icerik: &str) -> S<()> {
    std::fs::write(yol, icerik.as_bytes()).map_err(|e| format!("{yol}: {e}"))
}

fn dizin_yap(yol: &str) -> S<()> {
    std::fs::create_dir_all(yol).map_err(|e| format!("{yol}: {e}"))
}

fn sq(e: rusqlite::Error) -> String {
    format!("sqlite3: {e}")
}

// ---------------------------------------------------------------- Günlük
fn gunluk_metin(gun: &str, satirlar: &[Satir], head: &str) -> String {
    let gs: Vec<&Satir> = satirlar.iter().filter(|s| s.tarih_tr.as_deref() == Some(gun)).collect();
    // defaultdict(list): ilk görülme sırası
    let mut sirali: Vec<(&str, Vec<&Satir>)> = vec![];
    for s in &gs {
        match sirali.iter_mut().find(|(k, _)| *k == s.oturum_id) {
            Some((_, v)) => v.push(s),
            None => sirali.push((s.oturum_id.as_str(), vec![s])),
        }
    }
    let mut l: Vec<String> = vec![
        format!("# Hareket günlüğü — {gun} (Jarvis'in araç çağrıları; kaynak transkript → `tools/hareket-tablo.py`; HEAD `{head}`)\n"),
        format!("*Okunabilirlik ilkesi (Salih 08-17): Jarvis'in o gün YAPTIĞI her şey — dosya yazma/düzenleme, komut, okuma, arama, ajan/skill/workflow çağrısı — burada düz satır. Hedef gösterilir, içerik gösterilmez (içerik dosyanın kendisinde ya da git log'da). Makine-yüzü: silver `hareket` (`veri/baglam.sqlite`), gold `veri/gorunum/v_hareket_gunluk.csv` · `v_son_hareketler.csv`; bronz `veri/bronz/hareket-olay.jsonl`. Toplam bugün: {} çağrı, {} oturum.*\n", gs.len(), sirali.len()),
    ];
    // sorted(..., key=ilk satırın ts_utc or ""): kararlı
    sirali.sort_by(|a, b| a.1[0].ts_utc.as_deref().unwrap_or("").cmp(b.1[0].ts_utc.as_deref().unwrap_or("")));
    for (oid, ss) in &sirali {
        // Counter: ilk görülme sırası; most_common(): sayıya göre azalan, eşitlikte ekleme sırası
        let mut c: Vec<(&str, usize)> = vec![];
        for s in ss {
            match c.iter_mut().find(|(k, _)| *k == s.fiil) {
                Some((_, n)) => *n += 1,
                None => c.push((s.fiil.as_str(), 1)),
            }
        }
        let mut yz: Vec<&str> = ss.iter().filter(|s| s.dosya.as_deref().is_some_and(|d| !d.is_empty()) && (s.fiil == "yazdı" || s.fiil == "düzenledi")).map(|s| s.dosya.as_deref().unwrap()).collect();
        yz.sort();
        yz.dedup();
        let hata = ss.iter().filter(|s| s.sonuc.as_deref() == Some("hata")).count();
        let mut mc: Vec<(&str, usize)> = vec![];
        for s in ss {
            if let Some(m) = s.model.as_deref().filter(|m| !m.is_empty()) {
                match mc.iter_mut().find(|(k, _)| *k == m) {
                    Some((_, n)) => *n += 1,
                    None => mc.push((m, 1)),
                }
            }
        }
        let mut en: Option<(&str, usize)> = None; // max(): eşitlikte ilk
        for (k, n) in &mc {
            if en.is_none_or(|(_, b)| *n > b) {
                en = Some((k, *n));
            }
        }
        let gos = |o: &Option<String>| o.clone().unwrap_or_else(|| "None".into());
        l.push(format!("## Oturum `{}` — {}→{} · {} çağrı · model {} · hata {hata}", py::ilk(oid, 8), gos(&ss[0].saat_tr), gos(&ss[ss.len() - 1].saat_tr), ss.len(), en.map(|(k, _)| k).unwrap_or("?")));
        c.sort_by(|a, b| b.1.cmp(&a.1));
        let ozet = c.iter().map(|(k, v)| format!("{k} {v}")).collect::<Vec<_>>().join(" · ");
        let ek = if yz.is_empty() { String::new() } else { format!("\n**Yazılan/düzenlenen dosyalar ({}):** {}", yz.len(), yz.iter().map(|d| format!("`{d}`")).collect::<Vec<_>>().join(" · ")) };
        l.push(format!("**Özet:** {ozet}{ek}"));
        l.push("\n| # | saat | fiil | hedef | sonuç |\n|---|---|---|---|---|".to_string());
        for s in ss {
            l.push(format!("| {} | {} | {} | {} | {} |", s.sira, gos(&s.saat_tr), s.fiil, s.hedef.clone().unwrap_or_default().replace('|', "¦"), gos(&s.sonuc)));
        }
        l.push(String::new());
    }
    if gs.is_empty() {
        l.push("_Bu gün için kayıt yok._".to_string());
    }
    format!("{}\n", l.join("\n"))
}

// ---------------------------------------------------------------- Ana akış
fn calis(argv: &[String]) -> Result<i32, String> {
    let a = match ayrisan().ayristir(argv) {
        Ok(a) => a,
        Err(k) => return Ok(k),
    };
    let ev = py::expanduser("~");
    let rx = Rx::yeni();
    let repo = py::abspath(&a.metin("repo").map(String::from).unwrap_or_else(harness_anahtar::jarvis));
    let proje_dizin = a.metin("proje_dizin").map(String::from).unwrap_or_else(|| harness_anahtar::proje_dizin(None));
    let kuru = a.bayrak("kuru");
    let tum = a.bayrak("tum");
    if !Path::new(&repo).is_dir() {
        return Err(format!("{repo}: git çalışma dizini yok (subprocess cwd)"));
    }
    let head = py::sh(&["rev-parse", "--short", "HEAD"], Path::new(&repo));
    let bugun = match a.metin("tarih") {
        Some(t) if !t.is_empty() => t.to_string(),
        _ => (chrono::Utc::now() + Duration::hours(3)).format("%Y-%m-%d").to_string(),
    };

    // --- BRONZ ---
    let olaylar = bronz_topla(&proje_dizin, &repo, &ev, &rx)?;
    let bdir = py::join(&py::join(&repo, "veri"), "bronz");
    let byol = py::join(&bdir, "hareket-olay.jsonl");
    let mut mevcut: HashSet<String> = HashSet::new();
    if Path::new(&byol).exists() {
        let t = py::oku_kati(Path::new(&byol)).map_err(|_| format!("{byol}: okunamadı ya da UTF-8 değil"))?;
        for l in t.split('\n') {
            if l.starts_with('{')
                && let Ok(Value::Object(m)) = serde_json::from_str::<Value>(l)
                && let Some(Value::String(id)) = m.get("hareket_id")
            {
                mevcut.insert(id.clone());
            }
        }
    }
    let yeni: Vec<&Olay> = olaylar.iter().filter(|o| !mevcut.contains(&o.hareket_id)).collect();
    if !kuru {
        dizin_yap(&bdir)?;
        if !Path::new(&byol).exists() {
            yaz(&byol, BRONZ_BASLIK)?;
        }
        let mut tampon = String::new();
        for o in &yeni {
            tampon.push_str(&o.bronz_satir(&head));
            tampon.push('\n');
        }
        let mut f = std::fs::OpenOptions::new().append(true).open(&byol).map_err(|e| format!("{byol}: {e}"))?;
        f.write_all(tampon.as_bytes()).map_err(|e| format!("{byol}: {e}"))?;
    }

    // --- SİLVER ---
    let mut hepsi: Vec<Olay> = vec![];
    let mut g: HashSet<String> = HashSet::new();
    if Path::new(&byol).exists() {
        let t = py::oku_kati(Path::new(&byol)).map_err(|_| format!("{byol}: okunamadı ya da UTF-8 değil"))?;
        for l in t.split('\n') {
            if l.starts_with('{') {
                let v: Value = serde_json::from_str(l).map_err(|e| format!("{byol}: JSONDecodeError: {e}"))?;
                let id = match &v {
                    Value::Object(m) => match m.get("hareket_id") {
                        Some(Value::String(s)) => s.clone(),
                        Some(x) => return Err(format!("bronz hareket_id metin değil: {}", py_repr_v(x))),
                        None => return Err("bronz hareket_id: KeyError".into()),
                    },
                    _ => return Err("bronz satırı sözlük değil".into()),
                };
                if g.insert(id) {
                    hepsi.push(Olay::bronzdan(&v)?);
                }
            }
        }
    }
    if kuru {
        for o in &yeni {
            if g.insert(o.hareket_id.clone()) {
                hepsi.push((*o).clone());
            }
        }
    }
    hepsi.sort_by(|x, y| (x.ts.as_deref().unwrap_or(""), &x.oturum).cmp(&(y.ts.as_deref().unwrap_or(""), &y.oturum)));
    let satirlar = satir_uret(&hepsi, &head);
    let mut testler: Vec<(String, i64, &str)> = vec![];
    let gunler: Vec<String> = {
        let mut k: Vec<String> = satirlar.iter().filter_map(|s| s.tarih_tr.clone()).collect::<HashSet<_>>().into_iter().collect();
        k.sort();
        k
    };
    if !kuru {
        let db = py::join(&py::join(&repo, "veri"), "baglam.sqlite");
        let mut con = Connection::open(&db).map_err(sq)?;
        con.execute_batch(SILVER_BETIK).map_err(sq)?;
        let kol: HashSet<String> = {
            let mut st = con.prepare("PRAGMA table_info(hareket)").map_err(sq)?;
            let r: HashSet<String> = st.query_map([], |r| r.get::<_, String>(1)).map_err(sq)?.collect::<Result<HashSet<String>, _>>().map_err(sq)?;
            r
        };
        if !kol.contains("okuma_tipi") {
            con.execute("ALTER TABLE hareket ADD COLUMN okuma_tipi TEXT", []).map_err(sq)?; // additive (eski DB'de)
        }
        {
            let tx = con.transaction().map_err(sq)?;
            {
                let mut st = tx.prepare("INSERT INTO hareket VALUES (?1,?2,?3,?4,?5,?6,?7,?8,?9,?10,?11,?12,?13,?14,?15,?16,?17,?18)").map_err(sq)?;
                for s in &satirlar {
                    st.execute(rusqlite::params![
                        s.hareket_id, s.ts_utc, s.ts_tr, s.tarih_tr, s.saat_tr, s.oturum_id, s.oturum_kisa, s.sira, s.arac, s.fiil, s.hedef, s.dosya, s.repo_ici, s.sonuc, s.model, s.kaynak_dosya,
                        s.yuklendi_head, s.okuma_tipi
                    ])
                    .map_err(sq)?;
                }
            }
            tx.commit().map_err(sq)?;
        }
        let sdir = py::join(&py::join(&repo, "veri"), "sozlesme");
        dizin_yap(&sdir)?;
        let syol = py::join(&sdir, "hareket.json");
        if !Path::new(&syol).exists() {
            let mut st = con.prepare("PRAGMA table_info(hareket)").map_err(sq)?;
            let cols: Vec<Value> = st
                .query_map([], |r| Ok((r.get::<_, String>(1)?, r.get::<_, Option<String>>(2)?, r.get::<_, i64>(3)?, r.get::<_, i64>(5)?)))
                .map_err(sq)?
                .collect::<Result<Vec<_>, _>>()
                .map_err(sq)?
                .into_iter()
                .map(|(ad, tip, nn, pk)| json!({"ad": ad, "tip": tip.filter(|t| !t.is_empty()).unwrap_or_else(|| "ANY".into()), "not_null": nn != 0, "pk": pk != 0}))
                .collect();
            let sozlesme = json!({"tablo": "hareket", "surum": "1.0.0-deneysel-m29", "katman": "silver", "grain": "1 satır = 1 Jarvis araç çağrısı (jarvis ana-oturum transkriptleri)",
                "kolonlar": cols, "kural": "additive-only; kırıcı = silme/tip/kısıt/yeniden-ad"});
            yaz(&syol, &py::json_girintili(&sozlesme))?;
        }
        let enum_ = fiil_enum();
        let ph = vec!["?"; enum_.len()].join(",");
        let sorgular: Vec<(&str, String, Vec<String>)> = vec![
            ("hareket.hareket_id unique", "SELECT COUNT(*) FROM (SELECT hareket_id FROM hareket GROUP BY hareket_id HAVING COUNT(*)>1)".into(), vec![]),
            ("hareket.arac not_null", "SELECT COUNT(*) FROM hareket WHERE arac IS NULL OR arac=''".into(), vec![]),
            ("hareket.fiil accepted_values", format!("SELECT COUNT(*) FROM hareket WHERE fiil NOT IN ({ph})"), enum_),
        ];
        for (ad, sql, prm) in sorgular {
            let n: i64 = con.query_row(&sql, params_from_iter(prm.iter()), |r| r.get(0)).map_err(sq)?;
            testler.push((ad.to_string(), n, if n == 0 { "PASS" } else { "ERROR" }));
        }
        // --- GOLD ---
        let gdir = py::join(&py::join(&repo, "veri"), "gorunum");
        dizin_yap(&gdir)?;
        for v in ["v_hareket_gunluk", "v_son_hareketler", "v_okuma_orani"] {
            let csv = csv_yaz(&con, v)?;
            yaz(&py::join(&gdir, &format!("{v}.csv")), &csv)?;
        }
        drop(con);
        // --- İNSAN-YÜZÜ günlük ---
        let hedef_gunler: Vec<String> = if tum { gunler.clone() } else { vec![bugun.clone()] };
        let rdir = py::join(&py::join(&repo, "raporlar"), "hareket");
        dizin_yap(&rdir)?;
        for gun in &hedef_gunler {
            yaz(&py::join(&rdir, &format!("hareket-gunlugu-{gun}.md")), &gunluk_metin(gun, &satirlar, &head))?;
        }
    }
    if !a.bayrak("sessiz") {
        let son = if kuru { " (kuru)".to_string() } else { format!(" → gold CSV + raporlar/hareket/hareket-gunlugu-{}.md", if tum { "*" } else { bugun.as_str() }) };
        py::print(&format!("bronz: {} çağrı tarandı ({} yeni, {} mevcut) · silver: {} satır · gün: {}{son}", olaylar.len(), yeni.len(), mevcut.len(), satirlar.len(), gunler.len()));
        for t in &testler {
            py::print(&format!("  [{}] {} ihlal {}", t.2, t.0, t.1));
        }
    }
    Ok(0)
}

pub fn kos(argv: &[String]) -> i32 {
    match calis(argv) {
        Ok(k) => k,
        Err(e) => py::coker(&e),
    }
}
