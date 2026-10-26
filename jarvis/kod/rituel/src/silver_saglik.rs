//! `tools/silver-saglik.py` karşılığı: SİLVER SAĞLIK (bayrak + güncel-görünüm + tespit-damgalı kuyruk; Karar 58 = KB-39/40/41 (a)).
//! Python betiği `tools/anahtar-denetim.py`'yi `importlib` ile yükleyip `norm/compile_patterns/load_registry/integrity` kullanıyordu;
//! burada dört işlev Rust'ta yeniden uygulanır (tek tanım: bu modül). Kural dosyasındaki desenler Python `re` sözdizimi taşıdığından
//! (ileri bakış `(?!...)` vb.) `fancy_regex` ile derlenir. Çıkış: 0 · 6 (`--kapi` + T-Ç error) · 2 girdi/şema hatası · 7 canary FAIL.
use crate::argparse::{Ayrisan, Secenek, Sonuc};
use crate::py::{self, iso_tarih, sha1_hex};
use fancy_regex::Regex as Fr;
use jarvis_hook::ortak::{py_dumps, py_truthy};
use regex::Regex;
use rusqlite::types::Value as V;
use rusqlite::{Connection, params_from_iter};
use serde_json::{Map, Value, json};
use std::collections::{BTreeMap, BTreeSet, HashMap, HashSet};
use std::io::Write;
use std::path::Path;
use std::process::{Command, Stdio};
use std::sync::LazyLock;
use unicode_normalization::UnicodeNormalization;

const KURAL_YOLU: &str = "veri/sozlesme/silver-saglik-kurallar.json";
const KAYIT_YOLU: &str = "core/baglam-anahtar-kaydi.md";
const LOG_YOLU: &str = "veri/silver-saglik.jsonl";
const KUYRUK_YOLU: &str = "veri/silver-kuyruk.jsonl";
const ACIK_DURUM: [&str; 7] = ["İMZASIZ", "BEKLET", "Salih'te", "masaya", "kısmen-kapandı", "belirsiz", "icra-sırada"];
const CSV_GORUNUMLER: [&str; 4] = ["v_silver_saglik_son", "v_silver_kuyruk_ozet", "v_silver_kuyruk", "v_guncel_anahtar"];

// ---------------------------------------------------------------- hata türleri
enum Hata {
    /// `sys.exit(kod)` / `sys.exit("mesaj")`: mesaj stderr'e, çıkış kodu
    Cik(i32, String),
    /// Python'da yakalanmamış istisna (traceback): `py::coker`
    Coker(String),
}
type Sn<T> = Result<T, Hata>;

fn cok<T>(m: impl Into<String>) -> Sn<T> {
    Err(Hata::Coker(m.into()))
}
impl From<rusqlite::Error> for Hata {
    fn from(e: rusqlite::Error) -> Self {
        Hata::Coker(format!("sqlite3: {e}"))
    }
}
impl From<std::io::Error> for Hata {
    fn from(e: std::io::Error) -> Self {
        Hata::Coker(format!("OSError: {e}"))
    }
}
impl From<fancy_regex::Error> for Hata {
    fn from(e: fancy_regex::Error) -> Self {
        Hata::Coker(format!("re: {e}"))
    }
}

// ---------------------------------------------------------------- Python değer yardımcıları
/// Python `float.__repr__`.
fn pyfloat(f: f64) -> String {
    if f.is_nan() {
        return "nan".into();
    }
    if f.is_infinite() {
        return if f > 0.0 { "inf".into() } else { "-inf".into() };
    }
    if f == 0.0 {
        return if f.is_sign_negative() { "-0.0".into() } else { "0.0".into() };
    }
    let a = f.abs();
    if (1e-4..1e16).contains(&a) {
        return format!("{f:?}");
    }
    let e = format!("{f:e}");
    let (m, us) = e.split_once('e').unwrap_or((&e, "0"));
    let us: i32 = us.parse().unwrap_or(0);
    format!("{m}e{}{:02}", if us < 0 { '-' } else { '+' }, us.abs())
}

/// Python `str(v)` (JSON'dan gelen değer).
fn ps(v: &Value) -> String {
    match v {
        Value::Null => "None".into(),
        Value::Bool(true) => "True".into(),
        Value::Bool(false) => "False".into(),
        Value::Number(n) => n.as_f64().filter(|_| n.is_f64()).map(pyfloat).unwrap_or_else(|| n.to_string()),
        Value::String(s) => s.clone(),
        Value::Array(a) => format!("[{}]", a.iter().map(pr).collect::<Vec<_>>().join(", ")),
        Value::Object(o) => format!("{{{}}}", o.iter().map(|(k, v)| format!("{}: {}", py::repr(k), pr(v))).collect::<Vec<_>>().join(", ")),
    }
}
/// Python `repr(v)`.
fn pr(v: &Value) -> String {
    match v {
        Value::String(s) => py::repr(s),
        o => ps(o),
    }
}

fn obj(v: &Value) -> Sn<&Map<String, Value>> {
    match v {
        Value::Object(m) => Ok(m),
        _ => cok("AttributeError: 'dict' beklenirken başka tür"),
    }
}
fn kget<'a>(v: &'a Value, k: &str) -> Sn<&'a Value> {
    match obj(v)?.get(k) {
        Some(x) => Ok(x),
        None => cok(format!("KeyError: {}", py::repr(k))),
    }
}
/// `d.get(k, [])` ile dolaşılan liste (yoksa boş; liste değilse TypeError).
fn liste_al<'a>(m: &'a Map<String, Value>, k: &str) -> Sn<Vec<&'a Value>> {
    match m.get(k) {
        None => Ok(vec![]),
        Some(Value::Array(a)) => Ok(a.iter().collect()),
        Some(_) => cok(format!("TypeError: {k} yinelenemez")),
    }
}
/// `d.get(k) or []` ile dolaşılan liste.
fn liste_veya<'a>(m: &'a Map<String, Value>, k: &str) -> Sn<Vec<&'a Value>> {
    match m.get(k) {
        None => Ok(vec![]),
        Some(v) if !py_truthy(v) => Ok(vec![]),
        Some(Value::Array(a)) => Ok(a.iter().collect()),
        Some(_) => cok(format!("TypeError: {k} yinelenemez")),
    }
}
/// Python `int(v)`.
fn pint(v: &Value) -> Sn<i64> {
    match v {
        Value::Number(n) => n.as_i64().or_else(|| n.as_f64().map(|f| f as i64)).map(Ok).unwrap_or_else(|| cok("OverflowError")),
        Value::Bool(b) => Ok(*b as i64),
        Value::String(s) => py::int(s).map(|x| x as i64).map(Ok).unwrap_or_else(|| cok(format!("ValueError: int({})", py::repr(s)))),
        _ => cok("TypeError: int()"),
    }
}
fn metin_al(v: &Value) -> Sn<&str> {
    match v {
        Value::String(s) => Ok(s),
        _ => cok("TypeError: metin beklenirken başka tür"),
    }
}
/// JSON değerini SQLite parametresine bağla (Python `sqlite3`: list/dict → hata).
fn baglanir(v: &Value) -> Sn<V> {
    Ok(match v {
        Value::Null => V::Null,
        Value::Bool(b) => V::Integer(*b as i64),
        Value::Number(n) => match n.as_i64() {
            Some(i) => V::Integer(i),
            None if n.is_u64() => return cok("OverflowError: Python int too large to convert to SQLite INTEGER"),
            None => V::Real(n.as_f64().unwrap_or(0.0)),
        },
        Value::String(s) => V::Text(s.clone()),
        _ => return cok("sqlite3.InterfaceError: desteklenmeyen tür"),
    })
}

// ---------------------------------------------------------------- SQLite değer yardımcıları
fn vs(v: &V) -> String {
    match v {
        V::Null => "None".into(),
        V::Integer(i) => i.to_string(),
        V::Real(f) => pyfloat(*f),
        V::Text(s) => s.clone(),
        V::Blob(b) => format!("b'{}'", String::from_utf8_lossy(b)),
    }
}
fn v_dogru(v: &V) -> bool {
    match v {
        V::Null => false,
        V::Integer(i) => *i != 0,
        V::Real(f) => *f != 0.0,
        V::Text(s) => !s.is_empty(),
        V::Blob(b) => !b.is_empty(),
    }
}
fn v_text(v: &V) -> Sn<String> {
    match v {
        V::Text(s) => Ok(s.clone()),
        _ => cok("TypeError: metin beklenirken başka tür"),
    }
}
/// `x or ""` sonrası metin işlemi.
fn v_veya_bos(v: &V) -> Sn<String> {
    if v_dogru(v) { v_text(v) } else { Ok(String::new()) }
}
/// Python `a > b` (sqlite türleri).
fn v_buyuk(a: &V, b: &V) -> Sn<bool> {
    let sayi = |v: &V| match v {
        V::Integer(i) => Some(*i as f64),
        V::Real(f) => Some(*f),
        _ => None,
    };
    match (a, b) {
        (V::Text(x), V::Text(y)) => Ok(x > y),
        (V::Integer(x), V::Integer(y)) => Ok(x > y),
        _ => match (sayi(a), sayi(b)) {
            (Some(x), Some(y)) => Ok(x > y),
            _ => cok("TypeError: '>' desteklenmeyen türler"),
        },
    }
}

fn sorgu(con: &Connection, sql: &str, p: &[V]) -> Sn<Vec<Vec<V>>> {
    let mut st = con.prepare_cached(sql)?;
    let n = st.column_count();
    let mut rows = st.query(params_from_iter(p.iter()))?;
    let mut out = vec![];
    while let Some(r) = rows.next()? {
        let mut s = Vec::with_capacity(n);
        for i in 0..n {
            s.push(r.get::<_, V>(i)?);
        }
        out.push(s);
    }
    Ok(out)
}
fn yurut(con: &Connection, sql: &str, p: &[V]) -> Sn<()> {
    con.prepare_cached(sql)?.execute(params_from_iter(p.iter()))?;
    Ok(())
}
fn toplu_ekle(con: &Connection, sql: &str, satirlar: &[Vec<V>]) -> Sn<()> {
    let mut st = con.prepare_cached(sql)?;
    for s in satirlar {
        st.execute(params_from_iter(s.iter()))?;
    }
    Ok(())
}

// ---------------------------------------------------------------- anahtar-denetim.py işlevleri (norm / compile_patterns / load_registry / integrity)
/// `anahtar-denetim.norm`: NFC + Türkçe harf eşlemesi + küçük harf.
fn norm(s: &str) -> String {
    s.nfc()
        .map(|c| match c {
            'ı' | 'İ' => 'i',
            'ğ' | 'Ğ' => 'g',
            'ü' | 'Ü' => 'u',
            'ş' | 'Ş' => 's',
            'ö' | 'Ö' => 'o',
            'ç' | 'Ç' => 'c',
            x => x,
        })
        .collect::<String>()
        .to_lowercase()
}
fn norm_v(v: Option<&Value>) -> Sn<String> {
    match v {
        None => Ok(String::new()),
        Some(Value::String(s)) => Ok(norm(s)),
        Some(_) => cok("TypeError: normalize() metin bekler"),
    }
}

fn kelime(c: char) -> bool {
    c.is_alphanumeric() || c == '_'
}
/// `re.compile(r'(?<![\w-])' + re.escape(v) + r'(?![\w])', re.I)`: ileri/geri bakışlı sabit metin (v zaten `norm` edilmiş küçük harf).
struct Kalip(String);
impl Kalip {
    /// `len(p.findall(metin))`: örtüşmeyen eşleşmeler.
    fn say(&self, h: &str) -> usize {
        let (mut n, mut i) = (0, 0);
        while i <= h.len() {
            let Some(k) = h[i..].find(&self.0) else { break };
            let (b, e) = (i + k, i + k + self.0.len());
            let once = h[..b].chars().next_back().is_none_or(|c| !(kelime(c) || c == '-'));
            let sonra = h[e..].chars().next().is_none_or(|c| !kelime(c));
            if once && sonra {
                n += 1;
                i = e;
            } else {
                i = b + h[b..].chars().next().map_or(1, char::len_utf8);
            }
        }
        n
    }
}
fn kaliplari_derle(vals: &[String]) -> Vec<Kalip> {
    vals.iter().filter_map(|v| {
        let v = norm(v);
        let v = py::strip(&v);
        if v.is_empty() { None } else { Some(Kalip(v.to_string())) }
    }).collect()
}

/// Python `re.I` ile Türkçe i/ı/İ/I denkliği: desendeki bu harfler sınıfa çevrilir (sınıf içi/kaçışlı/grup sözdizimi hariç).
fn ci_hazirla(p: &str) -> String {
    let c: Vec<char> = p.chars().collect();
    let (mut o, mut i) = (String::from("(?i)"), 0);
    while i < c.len() {
        match c[i] {
            '\\' => {
                o.push('\\');
                if i + 1 < c.len() {
                    o.push(c[i + 1]);
                }
                i += 2;
            }
            '[' => {
                let mut j = i + 1;
                if j < c.len() && c[j] == '^' {
                    j += 1;
                }
                if j < c.len() && c[j] == ']' {
                    j += 1;
                }
                while j < c.len() && c[j] != ']' {
                    if c[j] == '\\' {
                        j += 1;
                    }
                    j += 1;
                }
                let son = j.min(c.len() - 1);
                o.extend(&c[i..=son]);
                i = son + 1;
            }
            '(' if c.get(i + 1) == Some(&'?') => {
                o.push_str("(?");
                i += 2;
                if c.get(i) == Some(&'P') && c.get(i + 1) == Some(&'<') {
                    while i < c.len() && c[i] != '>' {
                        o.push(c[i]);
                        i += 1;
                    }
                    if i < c.len() {
                        o.push('>');
                        i += 1;
                    }
                } else if c.get(i) == Some(&'<') && matches!(c.get(i + 1), Some('=') | Some('!')) {
                    o.push(c[i]);
                    o.push(c[i + 1]);
                    i += 2;
                } else if matches!(c.get(i), Some('=') | Some('!') | Some(':')) {
                    o.push(c[i]);
                    i += 1;
                } else {
                    while i < c.len() && (c[i].is_alphabetic() || c[i] == '-') {
                        o.push(c[i]);
                        i += 1;
                    }
                    if i < c.len() && matches!(c[i], ':' | ')') {
                        o.push(c[i]);
                        i += 1;
                    }
                }
            }
            'i' | 'I' | 'ı' | 'İ' => {
                o.push_str("[iIıİ]");
                i += 1;
            }
            x => {
                o.push(x);
                i += 1;
            }
        }
    }
    o
}

fn anahtarlar(reg: &Value) -> Sn<Vec<&Value>> {
    liste_al(obj(reg)?, "anahtarlar")
}

/// `anahtar-denetim.load_registry`: ```json bloğunu okur; hata → `sys.exit(2)`.
fn kayit_yukle(yol: &str) -> Sn<Value> {
    let ham = match std::fs::read(yol) {
        Ok(b) => b,
        Err(e) => return Err(Hata::Cik(2, format!("FAIL-LOUD: kayıt dosyası okunamadı: {yol} ({})", os_hata(&e, yol)))),
    };
    let Ok(metin) = String::from_utf8(ham) else { return cok("UnicodeDecodeError: kayıt dosyası") };
    let metin = py::evrensel_satir(&metin);
    static BLOK: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"(?s)```json\s*\n(.*?)\n```").unwrap());
    let Some(m) = BLOK.captures(&metin) else { return Err(Hata::Cik(2, "FAIL-LOUD: kayıtta ```json bloğu yok".into())) };
    match serde_json::from_str::<Value>(&m[1]) {
        Ok(v) => Ok(v),
        Err(e) => Err(Hata::Cik(2, format!("FAIL-LOUD: kayıt JSON hatası: {e}"))),
    }
}

/// `OSError` metni (`[Errno N] açıklama: 'yol'`).
fn os_hata(e: &std::io::Error, yol: &str) -> String {
    use std::io::ErrorKind::*;
    match e.kind() {
        NotFound => format!("[Errno 2] No such file or directory: {}", py::repr(yol)),
        PermissionDenied => format!("[Errno 13] Permission denied: {}", py::repr(yol)),
        _ => format!("{e}: {}", py::repr(yol)),
    }
}

/// `anahtar-denetim.integrity`: kayıt bütünlük hataları.
fn butunluk(reg: &Value) -> Sn<Vec<String>> {
    let mut errs: Vec<String> = vec![];
    let mut guncel_map: HashMap<String, String> = HashMap::new();
    let mut ids: HashSet<String> = HashSet::new();
    let bos = Map::new();
    for a in anahtarlar(reg)? {
        let a = obj(a)?;
        let aid = match a.get("anahtar_id") {
            Some(v) if py_truthy(v) => ps(v),
            _ => {
                errs.push("anahtar_id boş".into());
                continue;
            }
        };
        if ids.contains(&aid) {
            errs.push(format!("{aid}: çift anahtar_id"));
        }
        ids.insert(aid.clone());
        let g = match a.get("guncel") {
            Some(v) if py_truthy(v) => obj(v)?,
            _ => &bos,
        };
        if !g.get("deger").is_some_and(py_truthy) {
            errs.push(format!("{aid}: guncel.deger boş"));
        }
        if !g.get("gecerli_bas").is_some_and(py_truthy) {
            errs.push(format!("{aid}: damgasız güncel (gecerli_bas yok)"));
        }
        let gv = norm_v(g.get("deger"))?;
        if !gv.is_empty() {
            if let Some(onceki) = guncel_map.get(&gv)
                && *onceki != aid
            {
                errs.push(format!("{aid}: tekillik tip-b — aynı güncel değer '{}' {onceki} anahtarında da", ps(&g["deger"])));
            }
            guncel_map.insert(gv.clone(), aid.clone());
        }
        let gd = g.get("deger").map(ps).unwrap_or_else(|| "None".into());
        for e in liste_al(a, "emekli")? {
            let e = obj(e)?;
            let ed = e.get("deger").map(ps).unwrap_or_else(|| "None".into());
            if !e.get("deger").is_some_and(py_truthy) {
                errs.push(format!("{aid}: emekli.deger boş"));
            }
            if !e.get("tarih").is_some_and(py_truthy) {
                errs.push(format!("{aid}: damgasız emekli '{ed}'"));
            }
            let rb = e.get("replaced_by");
            if !rb.is_some_and(py_truthy) || matches!(rb, Some(Value::Array(_))) {
                errs.push(format!("{aid}: halefsiz/çoklu replaced_by '{ed}'"));
            } else {
                let rbs = metin_al(rb.unwrap())?;
                if norm(rbs) == norm_v(e.get("deger"))? {
                    errs.push(format!("{aid}: çevrim — replaced_by kendisi '{rbs}'"));
                } else if norm(rbs) != gv {
                    errs.push(format!("{aid}: replaced_by '{rbs}' ≠ güncel '{gd}' (zincir derinliği >1?)"));
                }
            }
            if norm_v(e.get("deger"))? == gv {
                errs.push(format!("{aid}: emekli değer güncel değerle aynı"));
            }
        }
    }
    Ok(errs)
}

// ---------------------------------------------------------------- yardımcılar
fn git_head(repo: &str) -> String {
    let mut c = Command::new("git");
    c.args(["rev-parse", "--short", "HEAD"]).current_dir(repo).stdin(Stdio::null());
    match c.output() {
        Ok(o) if o.status.success() => match String::from_utf8(o.stdout) {
            Ok(s) => py::strip(&py::evrensel_satir(&s)).to_string(),
            Err(_) => "?".into(),
        },
        _ => "?".into(),
    }
}

/// `tempfile.mkdtemp(prefix=...)`.
fn gecici_dizin(onek: &str) -> Sn<String> {
    static SAYAC: std::sync::atomic::AtomicU32 = std::sync::atomic::AtomicU32::new(0);
    let kok = std::env::temp_dir();
    loop {
        let n = std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).map(|d| d.subsec_nanos()).unwrap_or(0);
        let ad = format!("{onek}{:x}{:x}{}", std::process::id(), n, SAYAC.fetch_add(1, std::sync::atomic::Ordering::Relaxed));
        let yol = kok.join(ad);
        match std::fs::create_dir(&yol) {
            Ok(()) => return Ok(yol.to_string_lossy().into_owned()),
            Err(e) if e.kind() == std::io::ErrorKind::AlreadyExists => continue,
            Err(e) => return Err(e.into()),
        }
    }
}

fn rakam(c: char) -> bool {
    static ND: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"^\p{Nd}$").unwrap());
    c.is_ascii_digit() || (!c.is_ascii() && ND.is_match(&c.to_string()))
}

/// `re.search(r"(?<!\d)(\d{2})-(\d{2})(?!\d)", metin)` → (AA, GG) metinleri.
fn aa_gg_ara(metin: &str) -> Option<(String, String)> {
    let c: Vec<char> = metin.chars().collect();
    if c.len() < 5 {
        return None;
    }
    for i in 0..=c.len() - 5 {
        if rakam(c[i]) && rakam(c[i + 1]) && c[i + 2] == '-' && rakam(c[i + 3]) && rakam(c[i + 4]) && (i == 0 || !rakam(c[i - 1])) && (i + 5 == c.len() || !rakam(c[i + 5])) {
            return Some((c[i..i + 2].iter().collect(), c[i + 3..i + 5].iter().collect()));
        }
    }
    None
}

fn kapanis_tarihi(kapanis_kaniti: &V, kayit_tarihi: &V) -> Sn<Option<String>> {
    let kt = v_veya_bos(kayit_tarihi)?;
    let yil = if kt.is_empty() { "2026".to_string() } else { py::ilk(&kt, 4) };
    let kan = v_veya_bos(kapanis_kaniti)?;
    if let Some((a, g)) = aa_gg_ara(&kan) {
        let (ai, gi) = (py::int(&a).unwrap_or(0), py::int(&g).unwrap_or(0));
        if (1..=12).contains(&ai) && (1..=31).contains(&gi) {
            return Ok(Some(format!("{yil}-{a}-{g}")));
        }
    }
    Ok(if kt.is_empty() { None } else { Some(kt) })
}

/// SEANS sayacı: `raporlar/seans/seans-teslim-*.md` + `raporlar/vardiya/vardiya-teslim-*.md` dosya adlarındaki tarihler; sıralı.
fn seans_tarihleri(repo: &str) -> Vec<String> {
    static TARIH: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"(\d{4}-\d{2}-\d{2})").unwrap());
    let mut out = vec![];
    for (alt, onek) in [("seans", "seans-teslim-"), ("vardiya", "vardiya-teslim-")] {
        let dizin = py::join(&py::join(repo, "raporlar"), alt);
        let Ok(rd) = std::fs::read_dir(&dizin) else { continue };
        for e in rd.flatten() {
            let ad = e.file_name().to_string_lossy().into_owned();
            let kucuk = if cfg!(windows) { ad.to_lowercase() } else { ad.clone() };
            if kucuk.starts_with(onek) && kucuk.ends_with(".md") && let Some(m) = TARIH.captures(&ad) {
                out.push(m[1].to_string());
            }
        }
    }
    out.sort();
    out
}

fn yas_seans(seanslar: &[String], tarih_iso: Option<&str>) -> Option<i64> {
    let t = tarih_iso.filter(|t| !t.is_empty())?;
    let t = py::ilk(t, 10);
    Some(seanslar.iter().filter(|s| s.as_str() > t.as_str()).count() as i64)
}

fn muaf_mi(dosya_id: &str, muaf: &Map<String, Value>, oto: &HashSet<String>) -> Sn<bool> {
    if oto.contains(dosya_id) {
        return Ok(true);
    }
    for on in liste_al(muaf, "dosya_onek")? {
        if dosya_id.starts_with(metin_al(on)?) {
            return Ok(true);
        }
    }
    for ic in liste_al(muaf, "dosya_icerir")? {
        if dosya_id.contains(metin_al(ic)?) {
            return Ok(true);
        }
    }
    Ok(false)
}

// ---------------------------------------------------------------- şema (additive)
const DDL: &str = r#"
CREATE TABLE IF NOT EXISTS anahtar_kaydi (
  kaydi_id TEXT PRIMARY KEY, anahtar_id TEXT, tur TEXT, rol TEXT, deger TEXT, deger_norm TEXT,
  gecerli_bas TEXT, gecerli_bitis TEXT, replaced_by TEXT, gerekce TEXT, varyantlar TEXT, izinli_kaliplar TEXT,
  kaldirma_en_erken TEXT, kaynak TEXT, kayit_dosyasi TEXT
);
CREATE TABLE IF NOT EXISTS silver_kuyruk (
  kuyruk_id TEXT PRIMARY KEY, tip TEXT, hedef_tur TEXT, hedef_id TEXT, dosya_id TEXT, neden TEXT, eylem TEXT,
  tespit_tarihi TEXT, yas_gun INTEGER, yas_seans INTEGER, siddet TEXT, snapshot_tarih TEXT, kosum_id TEXT
);
CREATE TABLE IF NOT EXISTS silver_karantina_aday (
  cift_id TEXT PRIMARY KEY, anahtar_terim TEXT, kayit_id_a TEXT, kayit_id_b TEXT, dosya_a TEXT, dosya_b TEXT,
  blok_turu TEXT, uzunluk_a INTEGER, uzunluk_b INTEGER, kosum_id TEXT
);
CREATE TABLE IF NOT EXISTS silver_saglik_son (
  test_id TEXT PRIMARY KEY, ad TEXT, sinif TEXT, siddet TEXT, ihlal INTEGER, sonuc TEXT, ornek TEXT, not_ TEXT,
  kosum_id TEXT, snapshot_tarih TEXT, head TEXT
);
"#;
const GORUNUMLER: [&str; 6] = [
    r#"CREATE VIEW IF NOT EXISTS v_guncel_kayit AS
SELECT k.kayit_id, k.dosya_id, d.katman, k.sira, k.bolum_yolu, k.blok_turu, k.satir_bas, k.satir_son, k.metin, k.metin_kisa,
       k.token_kestirim, k.tarih_iso, k.gecerlilik, k.gecerlilik_neden, k.tespit_tarihi
FROM kayit k JOIN dosya d ON d.dosya_id=k.dosya_id
WHERE k.gecerlilik='guncel' AND d.katman IN ('sicak','ilik')
ORDER BY k.dosya_id, k.sira"#,
    r#"CREATE VIEW IF NOT EXISTS v_guncel_anahtar AS
SELECT a.anahtar_id, a.tur, a.deger AS guncel_deger, a.gecerli_bas, a.kaynak,
       (SELECT COUNT(*) FROM anahtar_kaydi e WHERE e.anahtar_id=a.anahtar_id AND e.rol='emekli') AS emekli_sayisi,
       (SELECT GROUP_CONCAT(e.deger, ' | ') FROM anahtar_kaydi e WHERE e.anahtar_id=a.anahtar_id AND e.rol='emekli') AS emekli_degerler,
       s.referans_sayisi AS gozlenen_referans, s.sicak_referans_sayisi AS gozlenen_sicak_referans
FROM anahtar_kaydi a LEFT JOIN anahtar s ON s.tur='anahtar_terim' AND s.deger=a.deger_norm
WHERE a.rol='guncel'
ORDER BY a.anahtar_id"#,
    r#"CREATE VIEW IF NOT EXISTS v_guncel_karar AS
SELECT b.borc_id, b.baslik, b.kume, b.tur, b.katman, b.karar_sahibi, b.durum, b.kayit_tarihi, b.yas_gun, b.bagimlilik, b.oneri
FROM karar_borcu b
WHERE b.durum IN ('İMZASIZ','BEKLET','Salih''te','masaya','kısmen-kapandı','belirsiz','icra-sırada')
  AND NOT EXISTS (SELECT 1 FROM silver_kuyruk q WHERE q.hedef_tur='karar_borcu' AND q.hedef_id=b.borc_id AND q.tip LIKE 'T-C4%')
ORDER BY b.katman, b.borc_id"#,
    r#"CREATE VIEW IF NOT EXISTS v_silver_kuyruk AS
SELECT tip, hedef_tur, hedef_id, dosya_id, neden, eylem, tespit_tarihi, yas_gun, yas_seans, siddet
FROM silver_kuyruk ORDER BY tip, tespit_tarihi, hedef_id"#,
    r#"CREATE VIEW IF NOT EXISTS v_silver_kuyruk_ozet AS
SELECT tip, siddet, COUNT(*) AS n, MIN(tespit_tarihi) AS en_eski_tespit, MAX(yas_gun) AS en_yasli_gun,
       ROUND(AVG(yas_gun),1) AS ort_yas_gun, SUM(CASE WHEN yas_gun>30 THEN 1 ELSE 0 END) AS n_30gun_ustu
FROM silver_kuyruk GROUP BY tip, siddet ORDER BY tip"#,
    r#"CREATE VIEW IF NOT EXISTS v_silver_saglik_son AS
SELECT test_id, sinif, siddet, ihlal, sonuc, ornek, not_, kosum_id, snapshot_tarih, head FROM silver_saglik_son
ORDER BY CASE sinif WHEN 'celiski' THEN 0 WHEN 'bayatlik' THEN 1 ELSE 2 END, test_id"#,
];

fn sema_hazirla(con: &Connection) -> Sn<()> {
    con.execute_batch(DDL)?;
    let kolonlar: HashSet<String> = sorgu(con, "PRAGMA table_info(kayit)", &[])?.iter().map(|r| vs(&r[1])).collect();
    for (ad, tip) in [("gecerlilik", "TEXT"), ("gecerlilik_neden", "TEXT"), ("tespit_tarihi", "TEXT")] {
        if !kolonlar.contains(ad) {
            con.execute_batch(&format!("ALTER TABLE kayit ADD COLUMN {ad} {tip}"))?;
        }
    }
    for sql in GORUNUMLER {
        con.execute_batch(sql)?;
    }
    // Python sqlite3: DML ile örtük işlem başlar; DDL işlem dışıdır. Aynı sınır burada açıkça kurulur.
    con.execute_batch("BEGIN")?;
    // her koşumda yeniden türetilir (idempotent; kaynak bronz + kural dosyası)
    for sql in ["DELETE FROM anahtar_kaydi", "DELETE FROM silver_kuyruk", "DELETE FROM silver_karantina_aday", "DELETE FROM silver_saglik_son", "UPDATE kayit SET gecerlilik=NULL, gecerlilik_neden=NULL, tespit_tarihi=NULL"] {
        yurut(con, sql, &[])?;
    }
    Ok(())
}

// ---------------------------------------------------------------- Adım 0: anahtar kaydı → silver
fn anahtar_kaydini_yukle(con: &Connection, reg: &Value, kayit_dosyasi: &str) -> Sn<usize> {
    let bos = Map::new();
    let mut rows: Vec<Vec<V>> = vec![];
    let t = |s: &str| V::Text(s.to_string());
    for a in anahtarlar(reg)? {
        let a = obj(a)?;
        let aid = match a.get("anahtar_id") {
            Some(v) if py_truthy(v) => ps(v),
            _ => "?".to_string(),
        };
        let g = match a.get("guncel") {
            Some(v) if py_truthy(v) => obj(v)?,
            _ => &bos,
        };
        let gdeger = g.get("deger").map(ps).unwrap_or_default();
        let tur = baglanir(a.get("tur").unwrap_or(&Value::Null))?;
        rows.push(vec![
            t(&format!("{aid}|guncel|{gdeger}")),
            t(&aid),
            tur.clone(),
            t("guncel"),
            t(&gdeger),
            t(&norm_v(Some(g.get("deger").unwrap_or(&Value::String(String::new()))))?),
            baglanir(g.get("gecerli_bas").unwrap_or(&Value::Null))?,
            V::Null,
            V::Null,
            V::Null,
            t("[]"),
            t("[]"),
            V::Null,
            baglanir(g.get("kaynak").unwrap_or(&Value::Null))?,
            t(kayit_dosyasi),
        ]);
        for rol in ["emekli", "aday"] {
            for e in liste_veya(a, rol)? {
                let e = obj(e)?;
                let edeger = e.get("deger").map(ps).unwrap_or_default();
                let rb = e.get("replaced_by").unwrap_or(&Value::Null);
                let rb_v = match rb {
                    Value::String(s) => V::Text(s.clone()),
                    x if py_truthy(x) => V::Text(py_dumps(x)),
                    _ => V::Null,
                };
                let dmp = |k: &str| V::Text(py_dumps(e.get(k).unwrap_or(&json!([]))));
                rows.push(vec![
                    t(&format!("{aid}|{rol}|{edeger}")),
                    t(&aid),
                    tur.clone(),
                    t(rol),
                    t(&edeger),
                    t(&norm_v(Some(e.get("deger").unwrap_or(&Value::String(String::new()))))?),
                    V::Null,
                    baglanir(e.get("tarih").unwrap_or(&Value::Null))?,
                    rb_v,
                    baglanir(e.get("gerekce").unwrap_or(&Value::Null))?,
                    dmp("varyantlar"),
                    dmp("izinli_kaliplar"),
                    baglanir(e.get("kaldirma_en_erken").unwrap_or(&Value::Null))?,
                    V::Null,
                    t(kayit_dosyasi),
                ]);
            }
        }
    }
    toplu_ekle(con, "INSERT OR REPLACE INTO anahtar_kaydi VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", &rows)?;
    Ok(rows.len())
}

// ---------------------------------------------------------------- testler
struct KuyrukSatiri {
    tip: String,
    hedef_tur: String,
    hedef_id: String,
    dosya_id: Option<String>,
    neden: String,
    eylem: String,
    yas_seans: Option<i64>,
}
impl KuyrukSatiri {
    fn anahtar(&self) -> String {
        format!("{}|{}|{}", self.tip, self.hedef_tur, self.hedef_id)
    }
}

#[derive(Default)]
struct Sonuclar {
    /// (test_id, ihlal, ornek, not)
    liste: Vec<(String, i64, Vec<String>, String)>,
    kuyruk: Vec<KuyrukSatiri>,
    /// kayit_id -> (gecerlilik, neden)
    bayrak: BTreeMap<String, (String, String)>,
}

impl Sonuclar {
    fn ekle(&mut self, test_id: &str, ihlal: i64, mut ornek: Vec<String>, not_: &str) {
        ornek.truncate(10);
        self.liste.push((test_id.to_string(), ihlal, ornek, not_.to_string()));
    }
    fn kuyruga(&mut self, tip: &str, hedef_tur: &str, hedef_id: &str, dosya_id: Option<&str>, neden: String, eylem: &str, yas_seans: Option<i64>) {
        self.kuyruk.push(KuyrukSatiri { tip: tip.into(), hedef_tur: hedef_tur.into(), hedef_id: hedef_id.into(), dosya_id: dosya_id.map(String::from), neden, eylem: eylem.into(), yas_seans });
    }
    fn bayrakla(&mut self, kayit_id: &str, gecerlilik: &str, neden: &str) {
        // öncelik: emekli-kalinti > celiski-kaybeden > karantina
        let oncelik = |g: &str| match g {
            "emekli-kalinti" => 3,
            "celiski-kaybeden" => 2,
            _ => 1,
        };
        let yaz = match self.bayrak.get(kayit_id) {
            None => true,
            Some((eski, _)) => oncelik(gecerlilik) > oncelik(eski),
        };
        if yaz {
            self.bayrak.insert(kayit_id.to_string(), (gecerlilik.to_string(), neden.to_string()));
        }
    }
}

/// T-C1 tam-bir güncel + damgasız yok · T-C2 emekli.tarih ≤ güncel.gecerli_bas (örtüşme yok).
fn t_c1_c2(con: &Connection, s: &mut Sonuclar) -> Sn<()> {
    let (mut c1, mut c2, mut o1, mut o2) = (0i64, 0i64, vec![], vec![]);
    for r in sorgu(con, "SELECT DISTINCT anahtar_id FROM anahtar_kaydi ORDER BY anahtar_id", &[])? {
        let aid = &r[0];
        let guncel = sorgu(con, "SELECT deger, gecerli_bas FROM anahtar_kaydi WHERE anahtar_id=? AND rol='guncel' AND (gecerli_bitis IS NULL OR gecerli_bitis='')", std::slice::from_ref(aid))?;
        if guncel.len() != 1 {
            c1 += 1;
            o1.push(format!("{}:güncel={}", vs(aid), guncel.len()));
        } else if !v_dogru(&guncel[0][1]) {
            c1 += 1;
            o1.push(format!("{}:damgasız", vs(aid)));
        }
        let bas = if guncel.len() == 1 { Some(&guncel[0][1]) } else { None };
        for e in sorgu(con, "SELECT deger, gecerli_bitis FROM anahtar_kaydi WHERE anahtar_id=? AND rol='emekli' ORDER BY deger", std::slice::from_ref(aid))? {
            let (deger, bitis) = (&e[0], &e[1]);
            if !v_dogru(bitis) {
                c2 += 1;
                o2.push(format!("{}/{}:bitişsiz-emekli", vs(aid), vs(deger)));
            } else if let Some(b) = bas
                && v_dogru(b)
                && v_buyuk(bitis, b)?
            {
                c2 += 1;
                o2.push(format!("{}/{}:{}>{}", vs(aid), vs(deger), vs(bitis), vs(b)));
            }
        }
    }
    s.ekle("T-C1", c1, o1, "");
    s.ekle("T-C2", c2, o2, "");
    Ok(())
}

/// Emekli değer KALINTISI sıcak/ılık kayit'ta (izinli kalıp hariç) — anahtar-denetim ile aynı norm/kalıp; kayit-grain.
fn t_c3(con: &Connection, s: &mut Sonuclar, reg: &Value) -> Sn<()> {
    let satirlar = sorgu(
        con,
        "SELECT k.kayit_id, k.dosya_id, d.katman, k.metin FROM kayit k JOIN dosya d ON d.dosya_id=k.dosya_id
                              WHERE d.katman IN ('sicak','ilik') AND k.metin IS NOT NULL AND k.dosya_id<>? ORDER BY k.dosya_id, k.sira",
        &[V::Text(KAYIT_YOLU.into())],
    )?;
    let mut metin_norm: Vec<(String, String, String, String)> = vec![];
    for r in &satirlar {
        metin_norm.push((vs(&r[0]), vs(&r[1]), vs(&r[2]), norm(&v_text(&r[3])?)));
    }
    let (mut sicak, mut ilik, mut os_, mut oi) = (0i64, 0i64, vec![], vec![]);
    for a in anahtarlar(reg)? {
        let a = obj(a)?;
        let aid = a.get("anahtar_id").map(ps).unwrap_or_else(|| "None".into());
        for e in liste_veya(a, "emekli")? {
            let e = obj(e)?;
            let mut vals: Vec<String> = vec![e.get("deger").map(|v| metin_al(v).map(String::from)).transpose()?.unwrap_or_default()];
            for v in liste_al(e, "varyantlar")? {
                vals.push(metin_al(v)?.to_string());
            }
            let pats = kaliplari_derle(&vals);
            let mut izin = vec![];
            for p in liste_al(e, "izinli_kaliplar")? {
                izin.push(Fr::new(&format!("(?i){}", norm(metin_al(p)?)))?);
            }
            let deger = e.get("deger").map(ps).unwrap_or_else(|| "None".into());
            let rb = e.get("replaced_by").map(ps).unwrap_or_else(|| "None".into());
            for (kid, did, kat, nl) in &metin_norm {
                let n: usize = pats.iter().map(|p| p.say(nl)).sum();
                if n == 0 {
                    continue;
                }
                let mut izinli = false;
                for al in &izin {
                    if al.is_match(nl)? {
                        izinli = true;
                        break;
                    }
                }
                if izinli {
                    continue;
                }
                let neden = format!("T-C3:{aid}/{deger}");
                if kat == "sicak" {
                    sicak += 1;
                    os_.push(kid.clone());
                    s.bayrakla(kid, "emekli-kalinti", &neden);
                    s.kuyruga("T-B-MISLEADING", "kayit", kid, Some(did), neden, &format!("yeniden yaz → '{rb}' (replaced_by) ya da izinli-kalıp damgası"), None);
                } else {
                    ilik += 1;
                    oi.push(kid.clone());
                    s.bayrakla(kid, "emekli-kalinti", &neden);
                }
            }
        }
    }
    s.ekle("T-C3-sicak", sicak, os_, "");
    s.ekle("T-C3-ilik", ilik, oi, "");
    Ok(())
}

fn ayni_baslik_anahtari(b: &str) -> String {
    let b = py::strip(b).to_lowercase();
    let mut o = String::new();
    let mut onceki_bosluk = false;
    for c in b.chars() {
        if py::bosluk_mu(c) {
            if !onceki_bosluk {
                o.push(' ');
            }
            onceki_bosluk = true;
        } else {
            o.push(c);
            onceki_bosluk = false;
        }
    }
    py::ilk(&o, 120)
}

fn t_c4(con: &Connection, s: &mut Sonuclar) -> Sn<()> {
    let rows = sorgu(con, "SELECT borc_id, baslik, durum, bagimlilik, kapanis_kaniti FROM karar_borcu ORDER BY borc_id", &[])?;
    let ids: HashSet<&str> = rows.iter().filter_map(|r| if let V::Text(t) = &r[0] { Some(t.as_str()) } else { None }).collect();
    let durum_acik = |r: &Vec<V>| matches!(&r[2], V::Text(d) if ACIK_DURUM.contains(&d.as_str()));
    let acik: Vec<&Vec<V>> = rows.iter().filter(|r| durum_acik(r)).collect();
    // (a) aynı normalize başlık
    let mut sira: Vec<String> = vec![];
    let mut grup: HashMap<String, Vec<String>> = HashMap::new();
    for r in &acik {
        let anahtar = ayni_baslik_anahtari(&v_veya_bos(&r[1])?);
        if !grup.contains_key(&anahtar) {
            sira.push(anahtar.clone());
        }
        grup.entry(anahtar).or_default().push(vs(&r[0]));
    }
    let cift: Vec<&Vec<String>> = sira.iter().map(|k| &grup[k]).filter(|v| v.len() > 1).collect();
    let a_ornek: Vec<String> = cift.iter().map(|v| v.join("|")).collect();
    for v in &cift {
        for b in v.iter() {
            s.kuyruga("T-C4a", "karar_borcu", b, None, format!("aynı başlık: {}", v.join("|")), "birleştir ya da başlığı ayrıştır", None);
        }
    }
    s.ekle("T-C4a", cift.iter().map(|v| v.len() as i64).sum(), a_ornek, "");
    // (b) kırık bağımlılık
    static BAG: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"^(?:KB|İB|IB|K)-?\d").unwrap());
    let mut kirik = vec![];
    for r in &acik {
        let bag = v_veya_bos(&r[3])?;
        for h in bag.split(|c: char| py::bosluk_mu(c) || matches!(c, ',' | ';' | '|')).filter(|h| !h.is_empty() && BAG.is_match(h)) {
            if !ids.contains(h) {
                kirik.push(format!("{}→{}", vs(&r[0]), h));
                s.kuyruga("T-C4b", "karar_borcu", &vs(&r[0]), None, format!("bağımlılık yok: {h}"), "bağımlılığı düzelt", None);
            }
        }
    }
    s.ekle("T-C4b", kirik.len() as i64, kirik, "");
    // (c) kapanış kanıtı 'Karar NN' ama açık
    static KARAR: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"Karar \d+").unwrap());
    static KISMI: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"(?i)BEKLET|k[ıiIİ]sm[iîIİÎ]|tet[iIİı]k|bekler|koşullu|[iIİı]cra [iIİı]B").unwrap());
    let mut c = vec![];
    for r in &acik {
        let kan = v_veya_bos(&r[4])?;
        let durum_kisi = matches!(&r[2], V::Text(d) if d == "kısmen-kapandı" || d == "BEKLET");
        if KARAR.is_match(&kan) && !durum_kisi && !KISMI.is_match(&kan) {
            c.push(vs(&r[0]));
            s.kuyruga("T-C4c", "karar_borcu", &vs(&r[0]), None, format!("kanıtta hüküm var, durum açık: {}", py::ilk(&kan, 80)), "durumu eşitle ya da kanıtı ayır", None);
        }
    }
    s.ekle("T-C4c", c.len() as i64, c, "");
    Ok(())
}

fn t_c5(con: &Connection, s: &mut Sonuclar) -> Sn<()> {
    let rows = sorgu(con, "SELECT anahtar_terim, dosya_id, bitisli, bitissiz FROM v_celiski_adayi", &[])?;
    let ornek: Vec<String> = rows.iter().map(|r| format!("{}@{}", vs(&r[0]), vs(&r[1]))).collect();
    for r in &rows {
        let (at, did) = (&r[0], &r[1]);
        for k in sorgu(
            con,
            "SELECT k.kayit_id FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id
                                     WHERE r.ref_turu='anahtar_terim' AND r.ref_deger=? AND k.dosya_id=? AND k.zarf_json IS NOT NULL
                                       AND k.zarf_gecerli_bitis IS NOT NULL AND k.zarf_gecerli_bitis<>'' AND k.zarf_gecerli_bitis<>'-'",
            &[at.clone(), did.clone()],
        )? {
            let kid = vs(&k[0]);
            s.bayrakla(&kid, "celiski-kaybeden", &format!("T-C5:{}", vs(at)));
            s.kuyruga("T-B-MISLEADING", "kayit", &kid, Some(&vs(did)), format!("T-C5 bitişli taraf ({})", vs(at)), "emekli damgası / zarfı eşitle", None);
        }
    }
    s.ekle("T-C5", rows.len() as i64, ornek, "");
    Ok(())
}

fn t_c6(repo: &str, s: &mut Sonuclar, kural: &Value) -> Sn<()> {
    let (mut ihlal, mut ornek, mut kalibresiz) = (0i64, vec![], 0i64);
    let katsayilar = liste_al(obj(kural)?, "katsayilar")?;
    for k in &katsayilar {
        let k = obj(k)?;
        let id = k.get("id").map(ps).unwrap_or_else(|| "None".into());
        let yol = py::join(repo, k.get("kanon_dosya").map(metin_al).transpose()?.unwrap_or(""));
        let metin = match py::oku_kati(Path::new(&yol)) {
            Ok(m) => m,
            Err(py::OkuHata::Io(_)) => {
                ihlal += 1;
                ornek.push(format!("{id}:dosya-yok"));
                continue;
            }
            Err(py::OkuHata::Kod) => return cok("UnicodeDecodeError: kanon dosyası"),
        };
        let bulundu = match k.get("kanon_regex") {
            None => false,
            Some(r) => Fr::new(metin_al(r)?)?.is_match(&metin)?,
        };
        if !bulundu {
            ihlal += 1;
            ornek.push(format!("{id}:ifade-bulunamadı(drift)"));
            continue;
        }
        let durum = k.get("durum");
        if !matches!(durum, Some(Value::String(d)) if matches!(d.as_str(), "kalibre" | "kalibre-edilmemis" | "tasinmaz")) {
            ihlal += 1;
            ornek.push(format!("{id}:damgasız"));
            continue;
        }
        if matches!(durum, Some(Value::String(d)) if d == "kalibre-edilmemis") {
            kalibresiz += 1;
        }
    }
    s.ekle("T-C6", ihlal, ornek, &format!("kalibre-edilmemiş damgalı sabit: {kalibresiz}/{}", katsayilar.len()));
    Ok(())
}

fn t_b(con: &Connection, s: &mut Sonuclar, kural: &Value, seanslar: &[String]) -> Sn<()> {
    let pencere = pint(kget(kget(kural, "pencere")?, "deger")?)?;
    let muaf = obj(kget(kural, "muafiyet")?)?;
    // otomatik muafiyet: aktif anahtar kaynak dosyası + anahtar_kaydi kayıt dosyası
    let mut oto: HashSet<String> = sorgu(con, "SELECT DISTINCT kaynak_dosya FROM anahtar WHERE kaynak_dosya IS NOT NULL AND kaynak_dosya<>'-'", &[])?
        .into_iter()
        .filter_map(|r| if let V::Text(t) = &r[0] { Some(t.clone()) } else { None })
        .collect();
    oto.insert(KAYIT_YOLU.to_string());
    // SUPERSEDED — dosya grain: sıcak/ılık başlık/ilk N blok damgalı
    let sd = obj(kget(kural, "supersede_damga")?)?;
    let rx = Fr::new(metin_al(sd.get("baslik_regex").ok_or_else(|| Hata::Coker("KeyError: 'baslik_regex'".into()))?)?)?;
    let n_ilk = sd.get("ilk_blok_sayisi").map(pint).transpose()?.unwrap_or(3);
    let mut sup = vec![];
    for r in sorgu(con, "SELECT dosya_id, katman, baslik FROM dosya WHERE katman IN ('sicak','ilik') ORDER BY dosya_id", &[])? {
        let did = &r[0];
        let mut metinler = vec![v_veya_bos(&r[2])?];
        for m in sorgu(con, "SELECT metin FROM kayit WHERE dosya_id=? AND sira<=? ORDER BY sira", &[did.clone(), V::Integer(n_ilk)])? {
            metinler.push(v_veya_bos(&m[0])?);
        }
        let mut var = false;
        for m in &metinler {
            if rx.is_match(m)? {
                var = true;
                break;
            }
        }
        if var {
            let d = vs(did);
            s.kuyruga("T-B-SUPERSEDED", "dosya", &d, Some(&d), format!("süpersede damgası başlık/ilk {n_ilk} blok"), "arşive indir + pointer bırak (m.8)", None);
            sup.push(d);
        }
    }
    s.ekle("T-B-SUPERSEDED", sup.len() as i64, sup, "");
    // MISLEADING — T-C3 sıcak + T-C5 kuyruğa zaten yazıldı; burada sayılır
    let mis: Vec<String> = s.kuyruk.iter().filter(|q| q.tip == "T-B-MISLEADING").map(|q| q.hedef_id.clone()).collect();
    s.ekle("T-B-MISLEADING", mis.len() as i64, mis, "");
    // YETİM — soğuk dosya, 0 gelen bağ, yaş > pencere, muaf değil
    let kols: Vec<String> = sorgu(con, "PRAGMA table_info(karar_borcu_kaynak)", &[])?.iter().map(|r| vs(&r[1])).collect();
    let kb_kol = ["dosya", "dosya_yolu", "kaynak_dosya"].into_iter().find(|ad| kols.iter().any(|k| k == ad));
    let kb_dosyalar: HashSet<String> = match kb_kol {
        Some(kol) => sorgu(con, &format!("SELECT DISTINCT {kol} FROM karar_borcu_kaynak"), &[])?.into_iter().filter_map(|r| if let V::Text(t) = &r[0] { Some(t.clone()) } else { None }).collect(),
        None => HashSet::new(),
    };
    let mut gelen: HashMap<String, i64> = HashMap::new();
    for r in sorgu(
        con,
        "SELECT r.hedef_yol, COUNT(*) FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id
                                                JOIN dosya d ON d.dosya_id=k.dosya_id WHERE r.ref_turu='dosya_pointer' AND r.hedef_var=1
                                                AND d.katman IN ('sicak','ilik') GROUP BY r.hedef_yol",
        &[],
    )? {
        if let (V::Text(y), V::Integer(n)) = (&r[0], &r[1]) {
            gelen.insert(y.clone(), *n);
        }
    }
    let yetim = obj(kget(kural, "yetim")?)?;
    let esik = yetim.get("esik_gelen_bag").map(pint).transpose()?.unwrap_or(0);
    let min_yas = yetim.get("min_yas_seans").map(pint).transpose()?.unwrap_or(pencere);
    let (mut yet, mut yas_bilinmeyen) = (vec![], 0i64);
    for r in sorgu(con, "SELECT dosya_id, son_commit, token_kestirim FROM dosya WHERE katman='soguk' ORDER BY dosya_id", &[])? {
        let did = vs(&r[0]);
        if muaf_mi(&did, muaf, &oto)? || kb_dosyalar.contains(&did) || gelen.get(&did).copied().unwrap_or(0) > esik {
            continue;
        }
        let son = if v_dogru(&r[1]) { Some(v_text(&r[1])?) } else { None };
        let Some(y) = yas_seans(seanslar, son.as_deref()) else {
            yas_bilinmeyen += 1;
            continue;
        };
        if y > min_yas {
            let g = gelen.get(&did).copied().unwrap_or(0);
            s.kuyruga("T-B-YETIM", "dosya", &did, Some(&did), format!("gelen bağ {g} ≤ {esik} ∧ yaş {y} seans > {min_yas} (≈{} token)", vs(&r[2])), "bağlantılandır (pointer) ya da pointer'a indir — SİLME DEĞİL", Some(y));
            yet.push(did);
        }
    }
    s.ekle("T-B-YETIM", yet.len() as i64, yet.clone(), &format!("yaşı bilinmeyen (son_commit boş): {yas_bilinmeyen}"));
    // Karar 83 B1: aday sayısı > uyarı eşiği → WARN kanalı; hattı düşürmez, pencere birimi KOŞUM
    let uyari_esigi = yetim.get("uyari_esigi").map(pint).transpose()?.unwrap_or(0);
    if uyari_esigi != 0 {
        let asim = if yet.len() as i64 > uyari_esigi { yet.len() as i64 } else { 0 };
        let ornek = if asim != 0 { yet.iter().take(5).cloned().collect() } else { vec![] };
        s.ekle("T-B-YETIM-UYARI", asim, ornek, &format!("aday {} / eşik {uyari_esigi} (medyan 234 × 1,5; Karar 83 B1, m.29)", yet.len()));
    }
    // KAPANDI — karar_borcu kapandı ∧ kapanış > pencere
    let mut kap = vec![];
    for r in sorgu(con, "SELECT borc_id, kayit_tarihi, kapanis_kaniti FROM karar_borcu WHERE durum='kapandı' ORDER BY borc_id", &[])? {
        let kt = kapanis_tarihi(&r[2], &r[1])?;
        let y = yas_seans(seanslar, kt.as_deref());
        if let Some(y) = y
            && y > pencere
        {
            let bid = vs(&r[0]);
            s.kuyruga("T-B-KAPANDI", "karar_borcu", &bid, None, format!("kapanış {}, {y} seans önce", kt.unwrap_or_default()), "tarihçe etiketi (ledger'da kalır, m.8)", Some(y));
            kap.push(bid);
        }
    }
    s.ekle("T-B-KAPANDI", kap.len() as i64, kap, "");
    Ok(())
}

fn t_a(con: &Connection, s: &mut Sonuclar, kural: &Value, kosum_id: &str) -> Sn<()> {
    let oe = obj(kget(kural, "on_eleme")?)?;
    let katmanlar: Vec<V> = match oe.get("katman") {
        None => vec![V::Text("sicak".into())],
        Some(Value::Array(a)) => a.iter().map(baglanir).collect::<Sn<_>>()?,
        Some(_) => return cok("TypeError: katman yinelenemez"),
    };
    let rx = Fr::new(&ci_hazirla(oe.get("sinyal_regex").map(metin_al).transpose()?.unwrap_or(r"\d")))?;
    let min_uz = oe.get("min_uzunluk").map(pint).transpose()?.unwrap_or(80);
    let maxk = oe.get("max_cift_kayit").map(pint).transpose()?.unwrap_or(500);
    if maxk < 0 {
        return cok("max_cift_kayit negatif (Python dilimi: sondan kırpma) desteklenmiyor");
    }
    let ayni_blok = oe.get("ayni_blok_turu").is_none_or(py_truthy);
    let q = format!(
        "SELECT r.ref_deger, k.kayit_id, k.dosya_id, k.blok_turu, k.metin FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id
           JOIN dosya d ON d.dosya_id=k.dosya_id WHERE r.ref_turu='anahtar_terim' AND d.katman IN ({}) AND LENGTH(k.metin)>=?
           ORDER BY r.ref_deger, k.kayit_id",
        vec!["?"; katmanlar.len()].join(",")
    );
    let mut p = katmanlar.clone();
    p.push(V::Integer(min_uz));
    let mut grup: BTreeMap<String, BTreeMap<String, (V, V, usize)>> = BTreeMap::new();
    for r in sorgu(con, &q, &p)? {
        let metin = v_veya_bos(&r[4])?;
        if !rx.is_match(&metin)? {
            continue;
        }
        grup.entry(vs(&r[0])).or_default().entry(vs(&r[1])).or_insert((r[2].clone(), r[3].clone(), metin.chars().count()));
    }
    let (mut toplam, mut rows, mut ornek): (i64, Vec<Vec<V>>, Vec<String>) = (0, vec![], vec![]);
    for (at, kayitlar) in &grup {
        let kayitlar: Vec<(&String, &(V, V, usize))> = kayitlar.iter().collect();
        for i in 0..kayitlar.len() {
            for j in i + 1..kayitlar.len() {
                let ((ka, (da, ba, la)), (kb, (db, bb, lb))) = (kayitlar[i], kayitlar[j]);
                if da == db || (ayni_blok && ba != bb) {
                    continue;
                }
                toplam += 1;
                let id = format!("{at}|{ka}|{kb}");
                if ornek.len() < 10 {
                    ornek.push(id.clone());
                }
                if (rows.len() as i64) < maxk {
                    rows.push(vec![V::Text(id), V::Text(at.clone()), V::Text(ka.clone()), V::Text(kb.clone()), da.clone(), db.clone(), ba.clone(), V::Integer(*la as i64), V::Integer(*lb as i64), V::Text(kosum_id.into())]);
                }
            }
        }
    }
    let yazilan = rows.len();
    toplu_ekle(con, "INSERT OR REPLACE INTO silver_karantina_aday VALUES (?,?,?,?,?,?,?,?,?,?)", &rows)?;
    s.ekle("T-A-ONELEME", toplam, ornek, &format!("yazılan çift {yazilan}/{toplam} (max_cift_kayit); LLM koşumu ayrı tetik"));
    Ok(())
}

/// T-SA sessiz-arıza sayacı (Karar 104 M2): zarf format hatası · köken eksik · çelişki-tespit oranı (bilgi).
fn t_sa(con: &Connection, s: &mut Sonuclar) -> Sn<()> {
    let zorunlu = ["tip", "kaynak", "tarih", "hedef", "sema"];
    let (mut fmt, mut kok, mut of, mut ok_) = (0i64, 0i64, vec![], vec![]);
    let bos = Map::new();
    for r in sorgu(con, "SELECT kayit_id, metin, zarf_json, zarf_tarih FROM kayit WHERE metin LIKE '%[tip:%' ORDER BY dosya_id, sira", &[])? {
        let kid = vs(&r[0]);
        let z: Option<Value> = if v_dogru(&r[2]) { serde_json::from_str(&v_text(&r[2])?).ok().filter(|v: &Value| !v.is_null()) } else { None };
        let alan: &Map<String, Value> = match &z {
            None => &bos,
            Some(v) if !py_truthy(v) => &bos,
            Some(v) => {
                let o = obj(v)?;
                match o.get("alanlar") {
                    None => o,
                    Some(a) if !py_truthy(a) => &bos,
                    Some(a) => obj(a)?,
                }
            }
        };
        let doluluk = |k: &str| !py::strip(&alan.get(k).map(ps).unwrap_or_default()).is_empty();
        if z.is_none() || zorunlu.iter().any(|k| !doluluk(k)) {
            fmt += 1;
            of.push(kid);
            continue;
        }
        let zt = v_veya_bos(&r[3])?;
        if zt.as_str() >= "2026-09-20" && !doluluk("koken") {
            kok += 1;
            ok_.push(kid);
        }
    }
    s.ekle("T-SA-FORMAT", fmt, of, "");
    s.ekle("T-SA-KOKEN", kok, ok_, "");
    let sicak = match &sorgu(con, "SELECT COUNT(*) FROM kayit k JOIN dosya d ON d.dosya_id=k.dosya_id WHERE d.katman='sicak'", &[])?[0][0] {
        V::Integer(n) => *n,
        _ => 0,
    };
    let tespit: i64 = s.liste.iter().filter(|(t, ..)| t.starts_with("T-C") || t.starts_with("T-A")).map(|(_, n, ..)| *n).sum();
    let oran = if sicak != 0 { 1000.0 * tespit as f64 / sicak as f64 } else { 0.0 };
    s.ekle("T-SA-TESPIT", 0, vec![], &format!("tespit {tespit} / sıcak kayıt {sicak} = {oran:.1}‰ (bilgi; taban yok, m.29)"));
    Ok(())
}

// ---------------------------------------------------------------- kuyruk olay kütüğü + yazım
/// Olay kütüğünü yeniden oynat → açık kuyruk {anahtar: tespit_tarihi}.
fn kuyruk_kutugu_oku(yol: &str) -> Sn<HashMap<String, String>> {
    let mut acik = HashMap::new();
    if !Path::new(yol).exists() {
        return Ok(acik);
    }
    let metin = match py::oku_kati(Path::new(yol)) {
        Ok(m) => m,
        Err(py::OkuHata::Io(e)) => return Err(e.into()),
        Err(py::OkuHata::Kod) => return cok("UnicodeDecodeError: kuyruk kütüğü"),
    };
    for line in metin.split_inclusive('\n') {
        let line = py::strip(line);
        if line.is_empty() || line.starts_with('#') {
            continue;
        }
        let Ok(o) = serde_json::from_str::<Value>(line) else { continue };
        let o = obj(&o)?;
        let g = |k: &str| o.get(k).map(ps).unwrap_or_else(|| "None".into());
        let anahtar = format!("{}|{}|{}", g("tip"), g("hedef_tur"), g("hedef_id"));
        match o.get("olay") {
            Some(Value::String(x)) if x == "ACILDI" => {
                if !acik.contains_key(&anahtar) {
                    let t = match o.get("tespit_tarihi") {
                        Some(v) if py_truthy(v) => metin_al(v)?.to_string(),
                        _ => match o.get("ts") {
                            Some(v) if py_truthy(v) => py::ilk(metin_al(v)?, 10),
                            _ => String::new(),
                        },
                    };
                    acik.insert(anahtar, t);
                }
            }
            Some(Value::String(x)) if x == "KAPANDI" => {
                acik.remove(&anahtar);
            }
            _ => {}
        }
    }
    Ok(acik)
}

struct SonSatir {
    test_id: String,
    ad: String,
    sinif: String,
    siddet: String,
    ihlal: i64,
    sonuc: &'static str,
    ornek: String,
    not_: String,
}

fn csv_alan(s: &str) -> String {
    if s.contains([',', '"', '\r', '\n']) { format!("\"{}\"", s.replace('"', "\"\"")) } else { s.to_string() }
}

/// Python metin kipinde dosya sonu: Windows'ta `\n` -> `\r\n`.
const SATIR_SONU: &str = if cfg!(windows) { "\r\n" } else { "\n" };

fn satirlari_ekle(yol: &str, satirlar: &[String]) -> Sn<()> {
    let mut f = std::fs::OpenOptions::new().append(true).create(true).open(yol)?;
    let mut tampon = String::new();
    for s in satirlar {
        tampon.push_str(s);
        tampon.push_str(SATIR_SONU);
    }
    f.write_all(tampon.as_bytes())?;
    Ok(())
}

#[allow(clippy::too_many_arguments)]
fn yaz(con: &Connection, repo: &str, s: &Sonuclar, kurallar: &Value, kosum_id: &str, snapshot: &str, head: &str, ts: &str, kuru: bool) -> Sn<(Vec<SonSatir>, bool, usize, usize)> {
    let testler = liste_al(obj(kurallar)?, "testler")?;
    let (mut siddet, mut ad, mut sinif): (HashMap<String, String>, HashMap<String, String>, HashMap<String, String>) = Default::default();
    for t in testler {
        let t = obj(t)?;
        let id = ps(t.get("id").ok_or_else(|| Hata::Coker("KeyError: 'id'".into()))?);
        let al = |k: &str, d: &str| t.get(k).map(ps).unwrap_or_else(|| d.to_string());
        siddet.insert(id.clone(), al("siddet", "warn"));
        ad.insert(id.clone(), al("ad", ""));
        sinif.insert(id, al("sinif", ""));
    }
    // bayraklar → kayit.gecerlilik
    let onceki = kuyruk_kutugu_oku(&py::join(repo, KUYRUK_YOLU))?;
    yurut(
        con,
        "UPDATE kayit SET gecerlilik = CASE WHEN (SELECT katman FROM dosya d WHERE d.dosya_id=kayit.dosya_id)='soguk' THEN 'tarihce' ELSE 'guncel' END,
                   gecerlilik_neden = NULL, tespit_tarihi = NULL",
        &[],
    )?;
    for (kid, (g, neden)) in &s.bayrak {
        let tespit = [format!("T-B-MISLEADING|kayit|{kid}"), format!("T-C3|kayit|{kid}")].iter().filter_map(|k| onceki.get(k)).find(|t| !t.is_empty()).cloned().unwrap_or_else(|| snapshot.to_string());
        yurut(con, "UPDATE kayit SET gecerlilik=?, gecerlilik_neden=?, tespit_tarihi=? WHERE kayit_id=?", &[V::Text(g.clone()), V::Text(neden.clone()), V::Text(tespit), V::Text(kid.clone())])?;
    }
    // kuyruk tablosu + olaylar
    let mut simdi: BTreeMap<String, String> = BTreeMap::new();
    let mut rows: Vec<Vec<V>> = vec![];
    let snap_tarih = iso_tarih(snapshot);
    for q in &s.kuyruk {
        let anahtar = q.anahtar();
        if simdi.contains_key(&anahtar) {
            continue;
        }
        let tespit = onceki.get(&anahtar).cloned().unwrap_or_else(|| snapshot.to_string());
        let yas_gun = match (snap_tarih, iso_tarih(&tespit)) {
            (Some(a), Some(b)) => V::Integer((a - b).num_days()),
            _ => V::Null,
        };
        simdi.insert(anahtar.clone(), tespit.clone());
        rows.push(vec![
            V::Text(anahtar),
            V::Text(q.tip.clone()),
            V::Text(q.hedef_tur.clone()),
            V::Text(q.hedef_id.clone()),
            q.dosya_id.clone().map(V::Text).unwrap_or(V::Null),
            V::Text(q.neden.clone()),
            V::Text(q.eylem.clone()),
            V::Text(tespit),
            yas_gun,
            q.yas_seans.map(V::Integer).unwrap_or(V::Null),
            V::Text(siddet.get(&q.tip).cloned().unwrap_or_else(|| "aday".into())),
            V::Text(snapshot.into()),
            V::Text(kosum_id.into()),
        ]);
    }
    toplu_ekle(con, "INSERT OR REPLACE INTO silver_kuyruk VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", &rows)?;
    let acilan: BTreeSet<&String> = simdi.keys().filter(|k| !onceki.contains_key(*k)).collect();
    let kapanan: BTreeSet<&String> = onceki.keys().filter(|k| !simdi.contains_key(*k)).collect();
    // test sonuçları
    let (mut son_rows, mut log_rows, mut hata_var) = (vec![], vec![], false);
    let mut son_db: Vec<Vec<V>> = vec![];
    for (test_id, ihlal, ornek, not_) in &s.liste {
        let sv = siddet.get(test_id).cloned().unwrap_or_else(|| "warn".into());
        let sonuc = if *ihlal == 0 {
            "PASS"
        } else if sv == "error" {
            "ERROR"
        } else if sv == "warn" {
            "WARN"
        } else {
            "ADAY"
        };
        if sonuc == "ERROR" {
            hata_var = true;
        }
        let a = ad.get(test_id).cloned().unwrap_or_default();
        let sn = sinif.get(test_id).cloned().unwrap_or_default();
        let ornek_json = py_dumps(&json!(ornek));
        son_db.push(vec![
            V::Text(test_id.clone()),
            V::Text(a.clone()),
            V::Text(sn.clone()),
            V::Text(sv.clone()),
            V::Integer(*ihlal),
            V::Text(sonuc.into()),
            V::Text(ornek_json.clone()),
            V::Text(not_.clone()),
            V::Text(kosum_id.into()),
            V::Text(snapshot.into()),
            V::Text(head.into()),
        ]);
        log_rows.push(py_dumps(&json!({"ts": ts, "kosum_id": kosum_id, "head": head, "snapshot": snapshot, "test_id": test_id, "sinif": sn, "siddet": sv, "ihlal": ihlal, "ornek": ornek, "sonuc": sonuc, "not": not_})));
        son_rows.push(SonSatir { test_id: test_id.clone(), ad: a, sinif: sn, siddet: sv, ihlal: *ihlal, sonuc, ornek: ornek_json, not_: not_.clone() });
    }
    toplu_ekle(con, "INSERT OR REPLACE INTO silver_saglik_son VALUES (?,?,?,?,?,?,?,?,?,?,?)", &son_db)?;
    if !kuru {
        con.execute_batch("COMMIT")?;
        satirlari_ekle(&py::join(repo, LOG_YOLU), &log_rows)?;
        if !acilan.is_empty() || !kapanan.is_empty() {
            let mut olaylar = vec![];
            for a in &acilan {
                let q = s.kuyruk.iter().find(|x| x.anahtar() == **a).expect("acilan kuyrukta");
                olaylar.push(py_dumps(&json!({"ts": ts, "kosum_id": kosum_id, "olay": "ACILDI", "tip": q.tip, "hedef_tur": q.hedef_tur, "hedef_id": q.hedef_id, "neden": q.neden, "tespit_tarihi": snapshot})));
            }
            for k in &kapanan {
                let mut p = k.splitn(3, '|');
                let (tip, ht, hid) = (p.next().unwrap_or(""), p.next().unwrap_or(""), p.next().unwrap_or(""));
                olaylar.push(py_dumps(&json!({"ts": ts, "kosum_id": kosum_id, "olay": "KAPANDI", "tip": tip, "hedef_tur": ht, "hedef_id": hid, "neden": "bu koşumda aday değil (kaynak düzeldi ya da kural değişti)", "tespit_tarihi": onceki.get(*k)})));
            }
            satirlari_ekle(&py::join(repo, KUYRUK_YOLU), &olaylar)?;
        }
        // CSV (gold; küçük görünümler)
        let gdir = py::join(&py::join(repo, "veri"), "gorunum");
        std::fs::create_dir_all(&gdir)?;
        for g in CSV_GORUNUMLER {
            let mut st = con.prepare(&format!("SELECT * FROM {g}"))?;
            let adlar: Vec<String> = st.column_names().iter().map(|x| x.to_string()).collect();
            let n = adlar.len();
            let mut cikti = adlar.iter().map(|x| csv_alan(x)).collect::<Vec<_>>().join(",");
            cikti.push_str("\r\n");
            let mut it = st.query([])?;
            while let Some(r) = it.next()? {
                let mut alanlar = vec![];
                for i in 0..n {
                    alanlar.push(match r.get::<_, V>(i)? {
                        V::Null => String::new(),
                        V::Integer(x) => x.to_string(),
                        V::Real(f) => pyfloat(f),
                        V::Text(t) => csv_alan(&t),
                        V::Blob(_) => return cok("csv: bayt dizisi alanı desteklenmiyor"),
                    });
                }
                cikti.push_str(&alanlar.join(","));
                cikti.push_str("\r\n");
            }
            std::fs::write(py::join(&gdir, &format!("{g}.csv")), cikti)?;
        }
    }
    Ok((son_rows, hata_var, acilan.len(), kapanan.len()))
}

// ---------------------------------------------------------------- canary (--test)
fn canary(kurallar: &Value) -> Sn<bool> {
    let tmp = gecici_dizin("silver-saglik-canary-")?;
    let db = py::join(&tmp, "canary.sqlite");
    let sonuc = canary_kos(&db, kurallar);
    let _ = std::fs::remove_dir_all(&tmp);
    sonuc
}

fn canary_kos(db: &str, kurallar: &Value) -> Sn<bool> {
    let con = Connection::open(db)?;
    con.execute_batch(
        r#"
    CREATE TABLE dosya (dosya_id TEXT PRIMARY KEY, dizin TEXT, katman TEXT, tur TEXT, boyut_bytes INTEGER, satir_sayisi INTEGER, blob_sha TEXT,
      ilk_commit TEXT, son_commit TEXT, baslik TEXT, token_kestirim INTEGER, uzanti TEXT, okunabildi INTEGER);
    CREATE TABLE kayit (kayit_id TEXT PRIMARY KEY, dosya_id TEXT, sira INTEGER, bolum_yolu TEXT, blok_turu TEXT, satir_bas INTEGER, satir_son INTEGER,
      metin TEXT, metin_kisa TEXT, token_kestirim INTEGER, tarih_ipucu TEXT, tarih_iso TEXT, zarf_tip TEXT, zarf_kaynak TEXT, zarf_tarih TEXT,
      zarf_hedef TEXT, zarf_sema TEXT, zarf_onem TEXT, zarf_gecerli_bitis TEXT, zarf_json TEXT, madde_derinlik INTEGER);
    CREATE TABLE referans (kayit_id TEXT, ref_turu TEXT, ref_deger TEXT, ham TEXT, konum INTEGER, hedef_var INTEGER, hedef_yol TEXT);
    CREATE TABLE anahtar (anahtar_id TEXT PRIMARY KEY, tur TEXT, deger TEXT, kaynak_dosya TEXT, durum TEXT, replaced_by TEXT, gecerli_bas TEXT,
      gecerli_bitis TEXT, referans_sayisi INTEGER, sicak_referans_sayisi INTEGER, ilk_gorulme TEXT, son_gorulme TEXT);
    CREATE TABLE karar_borcu (borc_id TEXT PRIMARY KEY, baslik TEXT, kume TEXT, tur TEXT, katman INTEGER, karar_sahibi TEXT, durum TEXT, kayit_tarihi TEXT,
      yas_gun INTEGER, secenekler TEXT, oneri TEXT, bagimlilik TEXT, kapanis_kaniti TEXT, masa_sirasi INTEGER, yururluk_aninda TEXT, icra_borcu TEXT,
      not_ TEXT, kaynak_sayisi INTEGER, snapshot_tarih TEXT, snapshot_sha TEXT);
    CREATE TABLE karar_borcu_kaynak (borc_id TEXT, sira INTEGER, dosya TEXT, satir INTEGER, metin TEXT, dosya_var INTEGER, satir_var INTEGER, kayit_id TEXT);
    CREATE VIEW v_celiski_adayi AS
    SELECT r.ref_deger AS anahtar_terim, k.dosya_id,
       SUM(CASE WHEN k.zarf_gecerli_bitis IS NOT NULL AND k.zarf_gecerli_bitis<>'' AND k.zarf_gecerli_bitis<>'-' THEN 1 ELSE 0 END) AS bitisli,
       SUM(CASE WHEN k.zarf_gecerli_bitis IS NULL OR k.zarf_gecerli_bitis='' OR k.zarf_gecerli_bitis='-' THEN 1 ELSE 0 END) AS bitissiz
    FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id WHERE r.ref_turu='anahtar_terim' AND k.zarf_json IS NOT NULL
    GROUP BY r.ref_deger, k.dosya_id HAVING bitisli>0 AND bitissiz>0;
    "#,
    )?;
    for sql in [
        "INSERT INTO dosya VALUES ('core/x.md','core','sicak','md',1,1,'s','2026-08-01','2026-08-01','X',10,'.md',1)",
        "INSERT INTO dosya VALUES ('cc/soguk-eski.md','cc','soguk','md',1,1,'s','2026-07-01','2026-07-01','EskI',10,'.md',1)",
        "INSERT INTO dosya VALUES ('wiki/emekli-sayfa.md','wiki','ilik','md',1,1,'s','2026-07-01','2026-07-01','EMEKLİ AD → yeni',10,'.md',1)",
        "INSERT INTO kayit (kayit_id,dosya_id,sira,blok_turu,metin) VALUES ('k1','core/x.md',1,'paragraf','Bugün günaydın ile açılış yapılır.')", // emekli kalıntı (izinsiz)
        "INSERT INTO kayit (kayit_id,dosya_id,sira,blok_turu,metin,zarf_json,zarf_gecerli_bitis) VALUES ('k2','core/x.md',2,'paragraf','kapsul kuralı 1 = zorunlu','{}','2026-08-01')",
        "INSERT INTO kayit (kayit_id,dosya_id,sira,blok_turu,metin,zarf_json,zarf_gecerli_bitis) VALUES ('k3','core/x.md',3,'paragraf','kapsul kuralı 2 = yasak','{}','')",
        "INSERT INTO referans VALUES ('k2','anahtar_terim','kapsul','kapsul',0,NULL,NULL)",
        "INSERT INTO referans VALUES ('k3','anahtar_terim','kapsul','kapsul',0,NULL,NULL)",
        "INSERT INTO karar_borcu (borc_id,baslik,durum,kayit_tarihi,bagimlilik,kapanis_kaniti) VALUES ('KB-1','Aynı kalem','masaya','2026-08-01','KB-9','')",
        "INSERT INTO karar_borcu (borc_id,baslik,durum,kayit_tarihi,bagimlilik,kapanis_kaniti) VALUES ('KB-2','aynı  kalem','icra-sırada','2026-08-01','','Karar 5: A')",
        "INSERT INTO karar_borcu (borc_id,baslik,durum,kayit_tarihi,bagimlilik,kapanis_kaniti) VALUES ('KB-3','Eski','kapandı','2026-07-01','','07-02 kapandı')",
    ] {
        con.execute_batch(sql)?;
    }
    let reg = json!({"anahtarlar": [
        {"anahtar_id": "oturum-acilis-tetigi", "tur": "tetik", "guncel": {"deger": "seans başı", "gecerli_bas": "2026-08-15"},
         "emekli": [{"deger": "günaydın", "varyantlar": [], "tarih": "2026-08-16", "replaced_by": "seans başı", "izinli_kaliplar": ["günaydın vardiyası"]}]},  // T-C2: 08-16 > 08-15
        {"anahtar_id": "cift-guncel", "tur": "kavram", "guncel": {"deger": "a", "gecerli_bas": ""}, "emekli": []},  // T-C1 damgasız
    ]});
    let mut kurallar = kurallar.clone();
    kget(kget(&kurallar, "pencere")?, "deger")?;
    kget(&kurallar, "yetim")?;
    if let Some(Value::Object(p)) = kurallar.get_mut("pencere") {
        p.insert("deger".into(), json!(1));
    }
    if let Some(Value::Object(y)) = kurallar.get_mut("yetim") {
        y.insert("min_yas_seans".into(), json!(1));
    }
    let mut s = Sonuclar::default();
    sema_hazirla(&con)?;
    anahtar_kaydini_yukle(&con, &reg, "canary")?;
    t_c1_c2(&con, &mut s)?;
    t_c3(&con, &mut s, &reg)?;
    t_c4(&con, &mut s)?;
    t_c5(&con, &mut s)?;
    t_b(&con, &mut s, &kurallar, &["2026-08-10".to_string(), "2026-08-20".to_string()])?;
    t_a(&con, &mut s, &kurallar, "canary")?;
    let got: HashMap<&str, i64> = s.liste.iter().map(|(t, n, ..)| (t.as_str(), *n)).collect();
    let beklenen: [(&str, i64); 11] = [("T-C1", 1), ("T-C2", 1), ("T-C3-sicak", 1), ("T-C4a", 2), ("T-C4b", 1), ("T-C4c", 1), ("T-C5", 1), ("T-B-SUPERSEDED", 1), ("T-B-YETIM", 1), ("T-B-KAPANDI", 1), ("T-B-MISLEADING", 2)];
    let fail: Vec<String> = beklenen
        .iter()
        .filter(|(t, b)| got.get(t) != Some(b))
        .map(|(t, b)| format!("({}, {b}, {})", py::repr(t), got.get(t).map(|x| x.to_string()).unwrap_or_else(|| "None".into())))
        .collect();
    let ok = fail.is_empty();
    py::print("=== silver-saglik CANARY (tohumlu ihlal → test FAIL vermeli) ===");
    let mut sirali = beklenen;
    sirali.sort();
    for (t, b) in sirali {
        py::print(&format!("  [{}] {} beklenen ihlal {b} · bulunan {}", if got.get(t) == Some(&b) { "PASS" } else { "FAIL" }, py::sola_hizala(t, 16), got.get(t).map(|x| x.to_string()).unwrap_or_else(|| "None".into())));
    }
    py::print(&format!("  CANARY {}", if ok { "PASS".to_string() } else { format!("FAIL: [{}]", fail.join(", ")) }));
    drop(con);
    Ok(ok)
}

// ---------------------------------------------------------------- main
fn ayrisan() -> Ayrisan {
    Ayrisan::yeni(
        "silver-saglik.py",
        Some("silver sağlık: bayrak + güncel görünüm + kuyruk (Karar 58)"),
        vec![
            Secenek::deger(&["--repo"], "repo", None),
            Secenek::bayrak(&["--kapi"], "kapi", Some("T-Ç error ihlalinde çıkış 6 (seans-kapanis/damitma kapısı); yoksa uyarı modu")),
            Secenek::bayrak(&["--sessiz"], "sessiz", Some("yalnız özet satırı (stdout) + ihlaller (stderr, uyarı kanalı)")),
            Secenek::bayrak(&["--kuru"], "kuru", Some("DB/kütük yazma (geçici kopyada hesapla)")),
            Secenek::deger(&["--snapshot"], "snapshot", Some("tespit/snapshot tarihi (deterministik koşum için sabitle)")),
            Secenek::bayrak(&["--test"], "test", Some("canary: tohumlu ihlal DB'sinde testler FAIL vermeli")),
            Secenek::bayrak(&["--json"], "json", Some("sonuçları JSON yaz")),
        ],
    )
}

fn kurallari_oku(repo: &str) -> Sn<Value> {
    let yol = py::join(repo, KURAL_YOLU);
    let ham = match std::fs::read(&yol) {
        Ok(b) => b,
        Err(e) => return Err(Hata::Cik(1, format!("[HATA] kural dosyası okunamadı: {KURAL_YOLU} ({})", os_hata(&e, &yol)))),
    };
    let Ok(metin) = String::from_utf8(ham) else { return cok("UnicodeDecodeError: kural dosyası") };
    let k: Value = match serde_json::from_str(&metin) {
        Ok(v) => v,
        Err(e) => return Err(Hata::Cik(1, format!("[HATA] kural dosyası okunamadı: {KURAL_YOLU} ({e})"))),
    };
    let gerekli = ["testler", "pencere", "muafiyet", "supersede_damga", "yetim", "on_eleme", "katsayilar", "min_n_surum"];
    let eksik: Vec<&str> = match &k {
        Value::Object(m) => gerekli.iter().copied().filter(|g| !m.contains_key(*g)).collect(),
        _ => gerekli.to_vec(),
    };
    if !eksik.is_empty() {
        return Err(Hata::Cik(1, format!("[HATA] kural dosyasında eksik alan: {}", eksik.join(", "))));
    }
    Ok(k)
}

pub fn kos(argv: &[String]) -> i32 {
    let a = match ayrisan().ayristir(argv) {
        Ok(a) => a,
        Err(k) => return k,
    };
    match calis(&a) {
        Ok(k) => k,
        Err(Hata::Cik(k, m)) => {
            py::err(&format!("{m}\n"));
            k
        }
        Err(Hata::Coker(m)) => py::coker(&m),
    }
}

fn calis(a: &Sonuc) -> Sn<i32> {
    let cwd = std::env::current_dir().map(|d| d.to_string_lossy().into_owned()).unwrap_or_default();
    let repo = py::abspath(a.metin("repo").unwrap_or(&cwd));
    let snapshot = a.metin("snapshot").map(String::from).unwrap_or_else(jarvis_hook::ortak::bugun_yerel);
    let (kuru, kapi) = (a.bayrak("kuru"), a.bayrak("kapi"));
    // Python: tools/anahtar-denetim.py içe aktarılır (yoksa FileNotFoundError); işlevleri bu modülde yeniden uygulandı.
    let denetim = py::join(&py::join(&repo, "tools"), "anahtar-denetim.py");
    if !Path::new(&denetim).is_file() {
        return cok(format!("FileNotFoundError: {}", os_hata(&std::io::Error::from(std::io::ErrorKind::NotFound), &denetim)));
    }
    let kurallar = kurallari_oku(&repo)?;
    if a.bayrak("test") {
        return Ok(if canary(&kurallar)? { 0 } else { 7 });
    }
    let db = py::join(&py::join(&repo, "veri"), "baglam.sqlite");
    if !Path::new(&db).exists() {
        return Err(Hata::Cik(1, "[HATA] silver yok: veri/baglam.sqlite (önce tools/katman-hatti.py)".into()));
    }
    let reg = kayit_yukle(&py::join(&repo, KAYIT_YOLU))?;
    let butunluk = butunluk(&reg)?;
    let mut tmp: Option<String> = None;
    let calis_db = if kuru {
        let t = gecici_dizin("silver-saglik-kuru-")?;
        let hedef = py::join(&t, "baglam.sqlite");
        std::fs::copy(&db, &hedef)?;
        tmp = Some(t);
        hedef
    } else {
        db.clone()
    };
    let sonuc = calis_icinde(a, &repo, &snapshot, kuru, kapi, &calis_db, &reg, &butunluk, &kurallar);
    if let Some(t) = tmp {
        let _ = std::fs::remove_dir_all(t);
    }
    sonuc
}

#[allow(clippy::too_many_arguments)]
fn calis_icinde(a: &Sonuc, repo: &str, snapshot: &str, kuru: bool, kapi: bool, calis_db: &str, reg: &Value, butunluk: &[String], kurallar: &Value) -> Sn<i32> {
    let con = Connection::open(calis_db)?;
    let mevcut: HashSet<String> = sorgu(&con, "SELECT name FROM sqlite_master WHERE type IN ('table','view')", &[])?.iter().map(|r| vs(&r[0])).collect();
    let eksik: Vec<&str> = ["dosya", "kayit", "referans", "anahtar", "karar_borcu", "karar_borcu_kaynak", "v_celiski_adayi"].into_iter().filter(|t| !mevcut.contains(*t)).collect();
    if !eksik.is_empty() {
        return Err(Hata::Cik(1, format!("[HATA] silver eksik nesne: {} (önceki hat adımı düşmüş olabilir — tools/katman-hatti.py çıktısına bak)", eksik.join(", "))));
    }
    let head = git_head(repo);
    let girdi_sha = match sorgu(&con, "SELECT kayit_id_kume_sha, git_head_sha FROM uretim ORDER BY uretim_zamani DESC LIMIT 1", &[]) {
        Ok(r) => r.first().map(|x| vs(&x[0])).unwrap_or_else(|| "?".into()),
        Err(_) => "?".into(),
    };
    // Python: kod_sha = betiğin kendi baytlarının sha1'i; Rust ikilisinin betiği yoktur: repo/tools/silver-saglik.py (yedek Python kaynağı) kullanılır.
    let kod_sha = match std::fs::read(py::join(&py::join(repo, "tools"), "silver-saglik.py")) {
        Ok(b) => sha1_hex(&b)[..8].to_string(),
        Err(_) => sha1_hex(b"silver-saglik-rust")[..8].to_string(),
    };
    let kosum_id = sha1_hex(format!("{head}|{girdi_sha}|{snapshot}|{kod_sha}").as_bytes())[..10].to_string();
    let ts = chrono::Local::now().format("%Y-%m-%dT%H:%M:%S%:z").to_string();
    let seanslar = seans_tarihleri(repo);
    let mut s = Sonuclar::default();
    sema_hazirla(&con)?;
    let n_kaydi = anahtar_kaydini_yukle(&con, reg, KAYIT_YOLU)?;
    t_c1_c2(&con, &mut s)?;
    t_c3(&con, &mut s, reg)?;
    t_c4(&con, &mut s)?;
    t_c5(&con, &mut s)?;
    t_c6(repo, &mut s, kurallar)?;
    t_b(&con, &mut s, kurallar, &seanslar)?;
    t_a(&con, &mut s, kurallar, &kosum_id)?;
    t_sa(&con, &mut s)?;
    if !butunluk.is_empty() {
        let (_, n, mut ornek, _) = s.liste.remove(0);
        ornek.extend(butunluk.iter().cloned());
        s.ekle("T-C1", n + butunluk.len() as i64, ornek, "anahtar-denetim bütünlük hataları dahil");
    }
    let (son_rows, hata_var, n_acilan, n_kapanan) = yaz(&con, repo, &s, kurallar, &kosum_id, snapshot, &head, &ts, kuru)?;
    let sayi = |sql: &str| -> Sn<i64> {
        Ok(match &sorgu(&con, sql, &[])?[0][0] {
            V::Integer(n) => *n,
            _ => 0,
        })
    };
    let n_guncel = sayi("SELECT COUNT(*) FROM v_guncel_kayit")?;
    let n_bayrak = sayi("SELECT COUNT(*) FROM kayit WHERE gecerlilik NOT IN ('guncel','tarihce')")?;
    let n_kuyruk = sayi("SELECT COUNT(*) FROM silver_kuyruk")?;
    drop(con);
    let say = |sonuc: &str| son_rows.iter().filter(|r| r.sonuc == sonuc).count();
    let ozet = format!(
        "silver-saglik: koşum {kosum_id} @ {head} · anahtar_kaydi {n_kaydi} satır · v_guncel_kayit {n_guncel} · bayraklı kayit {n_bayrak} · kuyruk {n_kuyruk} (yeni {n_acilan} · kapanan {n_kapanan}) · testler {} (ERROR {} · WARN {} · ADAY {}) · mod {}{}",
        son_rows.len(),
        say("ERROR"),
        say("WARN"),
        say("ADAY"),
        if kapi { "KAPI" } else { "uyarı" },
        if kuru { " · KURU" } else { "" }
    );
    if a.bayrak("json") {
        let testler: Vec<Value> = son_rows
            .iter()
            .map(|r| json!({"test_id": r.test_id, "ad": r.ad, "sinif": r.sinif, "siddet": r.siddet, "ihlal": r.ihlal, "sonuc": r.sonuc, "ornek": r.ornek, "not": r.not_}))
            .collect();
        py::print(&py::json_girintili(&json!({"ozet": ozet, "testler": testler})));
    } else {
        py::print(&ozet);
        if !a.bayrak("sessiz") {
            for r in &son_rows {
                let ek = if r.not_.is_empty() { String::new() } else { format!("· {}", r.not_) };
                py::print(&format!("  [{}] {} {} ihlal {} {} {}", py::sola_hizala(r.sonuc, 5), py::sola_hizala(&r.test_id, 16), py::sola_hizala(&r.siddet, 8), py::sola_hizala(&r.ihlal.to_string(), 5), py::ilk(&r.ad, 70), ek));
            }
        }
    }
    for r in &son_rows {
        if r.sonuc == "ERROR" || r.sonuc == "WARN" {
            py::err(&format!("{} {} ihlal {} örnek {}\n", r.sonuc, r.test_id, r.ihlal, py::ilk(&r.ornek, 200)));
        }
    }
    Ok(if kapi && hata_var { 6 } else { 0 })
}
