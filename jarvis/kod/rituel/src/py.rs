//! Python davranışını taklit eden küçük yardımcılar: `str.strip/splitlines/%r`, `int()`, ntpath yol işlemleri, zaman aşımlı alt süreç.
//! Amaç: araç çıktısının Python ile bayt bayt eşit kalması; her yardımcı ilgili Python işlevinin adını taşır.
use std::io::{Read, Write};
use std::path::Path;
use std::process::{Command, Stdio};
use std::time::{Duration, Instant};

// ---------------------------------------------------------------- Çıktı (kırık boru Python'da da sessiz sayılır)
pub fn out(s: &str) {
    let mut o = std::io::stdout().lock();
    let _ = o.write_all(s.as_bytes());
    let _ = o.flush();
}
pub fn err(s: &str) {
    let mut o = std::io::stderr().lock();
    let _ = o.write_all(s.as_bytes());
    let _ = o.flush();
}
/// Python `print(s)`.
pub fn print(s: &str) {
    out(&format!("{s}\n"));
}

/// Python'da yakalanmamış istisna (traceback, çıkış 1) olan durumlar: gerekçe stderr'e, çıkış kodu 1.
/// Traceback metni taklit edilmez (bilinçli ayrışma; raporda listeli).
pub fn coker(neden: &str) -> i32 {
    err(&format!("[HATA] Python karşılığında yakalanmamış istisna olurdu: {neden}\n"));
    1
}

// ---------------------------------------------------------------- str
/// `str.isspace()` (Unicode boşluk + \x1c-\x1f).
pub fn bosluk_mu(c: char) -> bool {
    c.is_whitespace() || ('\u{1c}'..='\u{1f}').contains(&c)
}
/// `s.strip()`.
pub fn strip(s: &str) -> &str {
    s.trim_matches(bosluk_mu)
}
/// `s.strip(chars)`.
pub fn strip_kume<'a>(s: &'a str, kume: &str) -> &'a str {
    s.trim_matches(|c| kume.contains(c))
}
/// `s.lstrip(chars)`.
pub fn lstrip_kume<'a>(s: &'a str, kume: &str) -> &'a str {
    s.trim_start_matches(|c| kume.contains(c))
}
/// `s.rstrip(chars)`.
pub fn rstrip_kume<'a>(s: &'a str, kume: &str) -> &'a str {
    s.trim_end_matches(|c| kume.contains(c))
}
/// `s[:n]` (kod noktası).
pub fn ilk(s: &str, n: usize) -> String {
    s.chars().take(n).collect()
}
/// `'%-*s' % (n, s)`.
pub fn sola_hizala(s: &str, n: usize) -> String {
    let u = s.chars().count();
    format!("{s}{}", " ".repeat(n.saturating_sub(u)))
}
/// `'%*s' % (n, s)`.
pub fn saga_hizala(s: &str, n: usize) -> String {
    let u = s.chars().count();
    format!("{}{s}", " ".repeat(n.saturating_sub(u)))
}

/// `str.splitlines()` (Unicode satır sınırları: \n \r \r\n \v \f \x1c-\x1e \x85 \u2028 \u2029).
pub fn splitlines(s: &str) -> Vec<String> {
    let mut sonuc = vec![];
    let mut satir = String::new();
    let mut it = s.chars().peekable();
    while let Some(c) = it.next() {
        match c {
            '\r' => {
                if it.peek() == Some(&'\n') {
                    it.next();
                }
                sonuc.push(std::mem::take(&mut satir));
            }
            '\n' | '\u{b}' | '\u{c}' | '\u{1c}' | '\u{1d}' | '\u{1e}' | '\u{85}' | '\u{2028}' | '\u{2029}' => sonuc.push(std::mem::take(&mut satir)),
            _ => satir.push(c),
        }
    }
    if !satir.is_empty() {
        sonuc.push(satir);
    }
    sonuc
}

/// `repr(str)` (hata iletilerindeki `%r`).
pub fn repr(s: &str) -> String {
    let tek = s.contains('\'');
    let cift = s.contains('"');
    let tirnak = if tek && !cift { '"' } else { '\'' };
    let mut r = String::new();
    r.push(tirnak);
    for c in s.chars() {
        match c {
            '\\' => r.push_str("\\\\"),
            '\n' => r.push_str("\\n"),
            '\r' => r.push_str("\\r"),
            '\t' => r.push_str("\\t"),
            c if c == tirnak => {
                r.push('\\');
                r.push(c);
            }
            c if c != ' ' && (c.is_control() || c.is_whitespace() || matches!(c as u32, 0xAD | 0x200B..=0x200F | 0x202A..=0x202E | 0x2060..=0x2064 | 0xFEFF)) => {
                let n = c as u32;
                if n < 0x100 {
                    r.push_str(&format!("\\x{n:02x}"));
                } else if n < 0x10000 {
                    r.push_str(&format!("\\u{n:04x}"));
                } else {
                    r.push_str(&format!("\\U{n:08x}"));
                }
            }
            c => r.push(c),
        }
    }
    r.push(tirnak);
    r
}

/// Unicode ondalık rakam (Nd) değeri; Python `int()` hepsini kabul eder.
fn ondalik_rakam(c: char) -> Option<u32> {
    const SIFIRLAR: [u32; 64] = [
        0x30, 0x660, 0x6F0, 0x7C0, 0x966, 0x9E6, 0xA66, 0xAE6, 0xB66, 0xBE6, 0xC66, 0xCE6, 0xD66, 0xDE6, 0xE50, 0xED0, 0xF20, 0x1040, 0x1090, 0x17E0, 0x1810, 0x1946,
        0x19D0, 0x1A80, 0x1A90, 0x1B50, 0x1BB0, 0x1C40, 0x1C50, 0xA620, 0xA8D0, 0xA900, 0xA9D0, 0xA9F0, 0xAA50, 0xABF0, 0xFF10, 0x104A0, 0x10D30, 0x11066, 0x110F0,
        0x11136, 0x111D0, 0x112F0, 0x11450, 0x114D0, 0x11650, 0x116C0, 0x11730, 0x118E0, 0x11950, 0x11C50, 0x11D50, 0x11DA0, 0x16A60, 0x16AC0, 0x16B50, 0x1D7CE,
        0x1D7D8, 0x1D7E2, 0x1D7EC, 0x1D7F6, 0x1E140, 0x1E2F0,
    ];
    let n = c as u32;
    SIFIRLAR.iter().find(|&&z| (z..z + 10).contains(&n)).map(|z| n - z)
}

/// `int(s)` (taban 10): kenar boşlukları, işaret, rakamlar arası tek alt çizgi.
pub fn int(s: &str) -> Option<i128> {
    let t = strip(s);
    let (neg, g) = match t.as_bytes().first()? {
        b'-' => (true, &t[1..]),
        b'+' => (false, &t[1..]),
        _ => (false, t),
    };
    if g.is_empty() || g.starts_with('_') || g.ends_with('_') || g.contains("__") {
        return None;
    }
    let mut n: i128 = 0;
    for c in g.chars() {
        if c == '_' {
            continue;
        }
        let d = ondalik_rakam(c)? as i128;
        n = n.checked_mul(10)?.checked_add(d)?;
    }
    Some(if neg { -n } else { n })
}

/// `open(yol, encoding="utf-8", errors="ignore")`/`read_text(errors="ignore")`: geçersiz baytlar atılır, CRLF/CR -> LF.
pub fn oku_yoksay(yol: &Path) -> std::io::Result<String> {
    let b = std::fs::read(yol)?;
    let mut s = String::new();
    for p in b.utf8_chunks() {
        s.push_str(p.valid());
    }
    Ok(evrensel_satir(&s))
}

/// Evrensel satır sonu: `\r\n` ve `\r` -> `\n`.
pub fn evrensel_satir(s: &str) -> String {
    if !s.contains('\r') { s.to_string() } else { s.replace("\r\n", "\n").replace('\r', "\n") }
}

pub enum OkuHata {
    /// `OSError` (Python'da çoğu yerde yakalanır).
    Io(std::io::Error),
    /// `UnicodeDecodeError` (Python'da yakalanmaz → çöker).
    Kod,
}
/// `open(yol, encoding="utf-8").read()` (katı çözme, evrensel satır sonu).
pub fn oku_kati(yol: &Path) -> Result<String, OkuHata> {
    let b = std::fs::read(yol).map_err(OkuHata::Io)?;
    let s = String::from_utf8(b).map_err(|_| OkuHata::Kod)?;
    Ok(evrensel_satir(&s))
}

// ---------------------------------------------------------------- Yol (ntpath/posixpath)
fn ayrac(c: char) -> bool {
    if cfg!(windows) { c == '/' || c == '\\' } else { c == '/' }
}
pub const SEP: char = if cfg!(windows) { '\\' } else { '/' };

/// `os.path.splitdrive` (yalnız Windows'ta sürücü/UNC ayırır).
pub fn splitdrive(p: &str) -> (String, String) {
    if !cfg!(windows) {
        return (String::new(), p.to_string());
    }
    let n: Vec<char> = p.chars().collect();
    let norm: String = p.replace('/', "\\");
    let nn: Vec<char> = norm.chars().collect();
    if n.len() >= 2 && nn[0] == '\\' && nn[1] == '\\' && (nn.len() < 3 || nn[2] != '\\') {
        let Some(i) = nn[2..].iter().position(|&c| c == '\\').map(|i| i + 2) else { return (String::new(), p.to_string()) };
        let j = nn[i + 1..].iter().position(|&c| c == '\\').map(|j| j + i + 1).unwrap_or(n.len());
        return (n[..j].iter().collect(), n[j..].iter().collect());
    }
    if n.len() >= 2 && n[1] == ':' {
        return (n[..2].iter().collect(), n[2..].iter().collect());
    }
    (String::new(), p.to_string())
}

/// `os.path.normpath`.
pub fn normpath(p: &str) -> String {
    if cfg!(windows) && (p.starts_with(r"\\?\") || p.starts_with(r"\\.\")) {
        return p.to_string();
    }
    let p = if cfg!(windows) { p.replace('/', "\\") } else { p.to_string() };
    let (surucu, geri) = splitdrive(&p);
    let kokte = geri.starts_with(SEP);
    let mut parcalar: Vec<&str> = vec![];
    for c in geri.split(SEP) {
        if c.is_empty() || c == "." {
            continue;
        }
        if c == ".." {
            if parcalar.last().is_some_and(|l| *l != "..") {
                parcalar.pop();
            } else if !kokte {
                parcalar.push("..");
            }
        } else {
            parcalar.push(c);
        }
    }
    let ayr = SEP.to_string();
    let r = format!("{surucu}{}{}", if kokte { SEP.to_string() } else { String::new() }, parcalar.join(&ayr));
    if r.is_empty() { ".".to_string() } else { r }
}

/// `os.path.abspath`.
pub fn abspath(p: &str) -> String {
    if p.is_empty() {
        return normpath(&std::env::current_dir().map(|d| d.to_string_lossy().into_owned()).unwrap_or_default());
    }
    let a = std::path::absolute(Path::new(p)).map(|d| d.to_string_lossy().into_owned()).unwrap_or_else(|_| p.to_string());
    normpath(&a)
}

/// `os.path.join(a, b)` (iki parça).
pub fn join(a: &str, b: &str) -> String {
    if !cfg!(windows) {
        if b.starts_with('/') {
            return b.to_string();
        }
        return if a.is_empty() || a.ends_with('/') { format!("{a}{b}") } else { format!("{a}/{b}") };
    }
    // ntpath.join (3.11)
    let (mut s_surucu, mut s_yol) = splitdrive(a);
    let (p_surucu, p_yol) = splitdrive(b);
    if p_yol.starts_with(ayrac) {
        if !p_surucu.is_empty() || s_surucu.is_empty() {
            s_surucu = p_surucu;
        }
        return format!("{s_surucu}{p_yol}");
    } else if !p_surucu.is_empty() && p_surucu != s_surucu {
        if p_surucu.to_lowercase() != s_surucu.to_lowercase() {
            return format!("{p_surucu}{p_yol}");
        }
        s_surucu = p_surucu;
    }
    if !s_yol.is_empty() && !s_yol.ends_with(ayrac) {
        s_yol.push(SEP);
    }
    s_yol.push_str(&p_yol);
    if !s_yol.is_empty() && !s_yol.starts_with(ayrac) && !s_surucu.is_empty() && !s_surucu.ends_with(':') {
        return format!("{s_surucu}{SEP}{s_yol}");
    }
    format!("{s_surucu}{s_yol}")
}

fn normcase(s: &str) -> String {
    if cfg!(windows) { s.replace('/', "\\").to_lowercase() } else { s.to_string() }
}

/// `os.path.relpath(path, start)`; Windows'ta farklı sürücü `ValueError` → `Err`.
pub fn relpath(yol: &str, baslangic: &str) -> Result<String, String> {
    let (b_abs, y_abs) = (abspath(baslangic), abspath(yol));
    let (bs, br) = splitdrive(&b_abs);
    let (ys, yr) = splitdrive(&y_abs);
    if normcase(&bs) != normcase(&ys) {
        return Err(format!("path is on mount {}, start on mount {}", repr(&ys), repr(&bs)));
    }
    let bl: Vec<&str> = br.split(SEP).filter(|x| !x.is_empty()).collect();
    let yl: Vec<&str> = yr.split(SEP).filter(|x| !x.is_empty()).collect();
    let i = bl.iter().zip(yl.iter()).take_while(|(a, b)| normcase(a) == normcase(b)).count();
    let mut rel: Vec<&str> = vec![".."; bl.len() - i];
    rel.extend(&yl[i..]);
    if rel.is_empty() { Ok(".".to_string()) } else { Ok(rel.join(&SEP.to_string())) }
}

/// `os.path.expanduser("~...")` (yalnız `~` ve `~/...`; Windows: USERPROFILE, yoksa HOMEDRIVE+HOMEPATH).
pub fn expanduser(p: &str) -> String {
    if !p.starts_with('~') {
        return p.to_string();
    }
    let rest = &p[1..];
    if !rest.is_empty() && !rest.starts_with(ayrac) {
        return p.to_string(); // ~kullanici: desteklenmez (Python da yerelde çözmez)
    }
    let ev = if cfg!(windows) {
        if let Ok(u) = std::env::var("USERPROFILE") {
            u
        } else if let Ok(hp) = std::env::var("HOMEPATH") {
            format!("{}{hp}", std::env::var("HOMEDRIVE").unwrap_or_default())
        } else {
            return p.to_string();
        }
    } else if let Ok(h) = std::env::var("HOME") {
        h
    } else {
        return p.to_string();
    };
    format!("{ev}{rest}")
}

// ---------------------------------------------------------------- Alt süreç
pub struct AltCikti {
    pub out: Vec<u8>,
    pub kod: Option<i32>,
}

/// `subprocess.run(..., capture_output=True, timeout=sn)`; başlatılamaz ya da zaman aşımı → `None`.
/// stdin boş cihazdır (açık stdin borusu alt süreci kilitleyebilir; 2026-10-17 kural-sayaci dersi).
pub fn calistir_zamanli(mut c: Command, sn: u64) -> Option<AltCikti> {
    c.stdin(Stdio::null()).stdout(Stdio::piped()).stderr(Stdio::piped());
    let mut ch = c.spawn().ok()?;
    let mut so = ch.stdout.take()?;
    let mut se = ch.stderr.take()?;
    let t1 = std::thread::spawn(move || {
        let mut b = vec![];
        let _ = so.read_to_end(&mut b);
        b
    });
    let t2 = std::thread::spawn(move || {
        let mut b = vec![];
        let _ = se.read_to_end(&mut b);
        b
    });
    let bitis = Instant::now() + Duration::from_secs(sn);
    let durum = loop {
        match ch.try_wait() {
            Ok(Some(d)) => break Some(d),
            Ok(None) if Instant::now() >= bitis => {
                let _ = ch.kill();
                let _ = ch.wait();
                break None;
            }
            Ok(None) => std::thread::sleep(Duration::from_millis(5)),
            Err(_) => break None,
        }
    };
    let b = t1.join().unwrap_or_default();
    let _ = t2.join();
    durum.map(|d| AltCikti { out: b, kod: d.code() })
}

/// Araçlardaki `sh(cmd, cwd)`: komut çıktısı (UTF-8 katı, evrensel satır sonu, `strip`), her hatada boş metin.
/// Python kabuk (`shell=True`) kullanır; burada git doğrudan çağrılır (bilinçli ayrışma: kabuk tırnak/metakarakter yorumu yok).
pub fn sh(args: &[&str], cwd: &Path) -> String {
    let mut c = Command::new("git");
    c.args(args).current_dir(cwd);
    let Some(r) = calistir_zamanli(c, 20) else { return String::new() };
    match String::from_utf8(r.out) {
        Ok(s) => strip(&evrensel_satir(&s)).to_string(),
        Err(_) => String::new(),
    }
}

// ---------------------------------------------------------------- JSON
/// `json.dumps(v, ensure_ascii=False, indent=1)`.
pub fn json_girintili(v: &serde_json::Value) -> String {
    use serde::Serialize;
    let mut buf = Vec::new();
    let bicim = serde_json::ser::PrettyFormatter::with_indent(b" ");
    let mut ser = serde_json::Serializer::with_formatter(&mut buf, bicim);
    v.serialize(&mut ser).expect("json");
    String::from_utf8(buf).expect("utf8")
}
