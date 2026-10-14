//! Ortak yardımcılar: Python uyumlu JSON yazımı, yerel zaman, realpath, metin okuma.
use serde_json::{Map, Value};
use std::io::Write;
use std::path::{Path, PathBuf};

/// Hook sonucu: stdout baytları, stderr metni, çıkış kodu.
#[derive(Debug, Default, Clone)]
pub struct Sonuc {
    pub cikti: Vec<u8>,
    pub hata: String,
    pub kod: i32,
}

impl Sonuc {
    pub fn bos() -> Self {
        Sonuc::default()
    }
    pub fn yaz(&mut self, s: &str) {
        self.cikti.extend_from_slice(s.as_bytes());
    }
    pub fn satir(&mut self, s: &str) {
        self.yaz(s);
        self.cikti.push(b'\n');
    }
}

/// Çalışma ortamı: stdin metni, depo kökü, ortam değişkenleri (test için enjekte edilebilir).
#[derive(Debug, Clone)]
pub struct Ortam {
    pub stdin: Vec<u8>,
    pub repo: PathBuf,
    pub env: std::collections::HashMap<String, String>,
}

impl Ortam {
    pub fn env(&self, ad: &str) -> Option<&str> {
        self.env.get(ad).map(String::as_str)
    }
    pub fn stdin_metin(&self) -> String {
        String::from_utf8_lossy(&self.stdin).into_owned()
    }
}

// ---------------------------------------------------------------- JSON (Python json.dumps, ensure_ascii=False)
struct PyBicim;
impl serde_json::ser::Formatter for PyBicim {
    fn begin_array_value<W: ?Sized + Write>(&mut self, w: &mut W, first: bool) -> std::io::Result<()> {
        if first { Ok(()) } else { w.write_all(b", ") }
    }
    fn begin_object_key<W: ?Sized + Write>(&mut self, w: &mut W, first: bool) -> std::io::Result<()> {
        if first { Ok(()) } else { w.write_all(b", ") }
    }
    fn begin_object_value<W: ?Sized + Write>(&mut self, w: &mut W) -> std::io::Result<()> {
        w.write_all(b": ")
    }
}

/// `json.dumps(v, ensure_ascii=False)` ile aynı metin (ayraçlar `, ` ve `: `).
pub fn py_dumps(v: &Value) -> String {
    use serde::Serialize;
    let mut buf = Vec::new();
    let mut ser = serde_json::Serializer::with_formatter(&mut buf, PyBicim);
    v.serialize(&mut ser).expect("json");
    String::from_utf8(buf).expect("utf8")
}

pub fn py_truthy(v: &Value) -> bool {
    match v {
        Value::Null => false,
        Value::Bool(b) => *b,
        Value::Number(n) => n.as_f64().map(|f| f != 0.0).unwrap_or(true),
        Value::String(s) => !s.is_empty(),
        Value::Array(a) => !a.is_empty(),
        Value::Object(o) => !o.is_empty(),
    }
}

/// Python `str(v)` (skaler değerler için; bileşikler yaklaşık).
pub fn py_str(v: &Value) -> String {
    match v {
        Value::Null => "None".into(),
        Value::Bool(true) => "True".into(),
        Value::Bool(false) => "False".into(),
        Value::Number(n) => n.to_string(),
        Value::String(s) => s.clone(),
        other => py_dumps(other),
    }
}

/// `d.get(a) or d.get(b) or ...` (Python `or` zinciri; hepsi yoksa Null).
pub fn py_or(d: &Map<String, Value>, anahtarlar: &[&str]) -> Value {
    for a in anahtarlar {
        if let Some(v) = d.get(*a)
            && py_truthy(v)
        {
            return v.clone();
        }
    }
    Value::Null
}

// ---------------------------------------------------------------- Zaman
pub fn ts_yerel() -> String {
    chrono::Local::now().format("%Y-%m-%dT%H:%M:%S%:z").to_string()
}
pub fn ts_utc() -> String {
    chrono::Utc::now().format("%Y-%m-%dT%H:%M:%S%:z").to_string()
}
pub fn ts_istanbul() -> String {
    let off = chrono::FixedOffset::east_opt(3 * 3600).unwrap();
    chrono::Utc::now().with_timezone(&off).format("%Y-%m-%dT%H:%M:%S%:z").to_string()
}
pub fn bugun_yerel() -> String {
    chrono::Local::now().format("%Y-%m-%d").to_string()
}

// ---------------------------------------------------------------- Dosya
/// Python `open(yol, encoding="utf-8", errors="replace").read()` (evrensel satır sonu: CRLF/CR -> LF).
pub fn oku_py(yol: &Path) -> Option<String> {
    let b = std::fs::read(yol).ok()?;
    let s = String::from_utf8_lossy(&b).into_owned();
    Some(s.replace("\r\n", "\n").replace('\r', "\n"))
}

/// Kütüğe tek satır ekle (LF; Python Windows'ta CRLF yazar, bilinçli ayrışma).
pub fn ekle_satir(yol: &Path, satir: &str) -> std::io::Result<()> {
    if let Some(d) = yol.parent() {
        std::fs::create_dir_all(d)?;
    }
    let mut f = std::fs::OpenOptions::new().create(true).append(true).open(yol)?;
    f.write_all(satir.as_bytes())?;
    f.write_all(b"\n")
}

/// Python `s[:n]` (kod noktası).
pub fn ilk_n(s: &str, n: usize) -> String {
    s.chars().take(n).collect()
}

/// Python dilimi `v[a:b]` (negatif indeks dahil).
pub fn py_dilim<T: Clone>(v: &[T], a: i64, b: i64) -> Vec<T> {
    let n = v.len() as i64;
    let duz = |x: i64| if x < 0 { (x + n).max(0) } else { x.min(n) };
    let (a, b) = (duz(a), duz(b));
    if a >= b { vec![] } else { v[a as usize..b as usize].to_vec() }
}

// ---------------------------------------------------------------- Yol
pub fn ev_dizini() -> PathBuf {
    let anahtar = if cfg!(windows) { "USERPROFILE" } else { "HOME" };
    std::env::var_os(anahtar).map(PathBuf::from).unwrap_or_default()
}

#[cfg(windows)]
fn onek_sil(p: PathBuf) -> PathBuf {
    let s = p.to_string_lossy().into_owned();
    if let Some(r) = s.strip_prefix(r"\\?\UNC\") {
        PathBuf::from(format!(r"\\{r}"))
    } else if let Some(r) = s.strip_prefix(r"\\?\") {
        PathBuf::from(r)
    } else {
        p
    }
}
#[cfg(not(windows))]
fn onek_sil(p: PathBuf) -> PathBuf {
    p
}

/// Python `os.path.realpath`: mutlaklaştır, var olan en uzun öneki çöz, kalanı ekle.
pub fn realpath(p: &Path) -> PathBuf {
    let abs = std::path::absolute(p).unwrap_or_else(|_| p.to_path_buf());
    let mut onek = abs.clone();
    let mut kalan: Vec<std::ffi::OsString> = vec![];
    loop {
        if let Ok(c) = std::fs::canonicalize(&onek) {
            let mut r = onek_sil(c);
            for k in kalan.iter().rev() {
                r.push(k);
            }
            return r;
        }
        match (onek.file_name().map(|s| s.to_os_string()), onek.parent().map(Path::to_path_buf)) {
            (Some(ad), Some(ust)) => {
                kalan.push(ad);
                onek = ust;
            }
            _ => return abs,
        }
    }
}

/// Python `ntpath.isabs` (3.11): sürücü sonrası `/` ya da `\` ile başlar.
pub fn py_isabs(s: &str) -> bool {
    let r = if cfg!(windows) {
        let b = s.as_bytes();
        if b.len() >= 2 && b[1] == b':' { &s[2..] } else { s }
    } else {
        s
    };
    if cfg!(windows) { r.starts_with('/') || r.starts_with('\\') } else { r.starts_with('/') }
}

pub fn sep() -> char {
    std::path::MAIN_SEPARATOR
}

/// Yol ayraçlarını işletim sistemine çevir (Python relpath/glob çıktısı Windows'ta `\`).
pub fn yerel_ayrac(s: &str) -> String {
    if cfg!(windows) { s.replace('/', "\\") } else { s.to_string() }
}

/// `$(cat)`: sondaki satır sonlarını sil.
pub fn sondaki_nl_sil(s: &str) -> &str {
    s.trim_end_matches('\n')
}

pub fn json_oku(metin: &str) -> Option<Value> {
    serde_json::from_str(metin).ok()
}
