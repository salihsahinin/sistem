//! Python davranışını taklit eden küçük yardımcılar: `str.strip/splitlines/%r`, `int()`, ntpath yol işlemleri, zaman aşımlı alt süreç.
//! Amaç: araç çıktısının Python ile bayt bayt eşit kalması; her yardımcı ilgili Python işlevinin adını taşır.
use std::io::Write;
use std::path::Path;

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

// ---------------------------------------------------------------- float / katlama / kodlama hatası
/// `float(s)`: kenar boşlukları, işaret, alt çizgi (rakamlar arası), `inf`/`nan`, üs.
pub fn float(s: &str) -> Option<f64> {
    let t = strip(s);
    if t.is_empty() {
        return None;
    }
    let b = t.as_bytes();
    for (i, &c) in b.iter().enumerate() {
        if c == b'_' && !(i > 0 && i + 1 < b.len() && b[i - 1].is_ascii_digit() && b[i + 1].is_ascii_digit()) {
            return None;
        }
    }
    let temiz = t.replace('_', "");
    // Rust "infinity"/"inf"/"nan" büyük-küçük harfsiz kabul eder; Python da. Ondalık dışı Unicode rakamlar: ASCII'ye çevir
    let temiz: String = temiz.chars().map(|c| ondalik_rakam(c).map(|d| char::from_digit(d, 10).unwrap()).unwrap_or(c)).collect();
    if temiz.contains(|c: char| c.is_ascii_alphabetic() && !matches!(c.to_ascii_lowercase(), 'e' | 'i' | 'n' | 'f' | 'a' | 't' | 'y')) {
        return None;
    }
    temiz.parse::<f64>().ok()
}

/// Python `repr(float)` (`%s` ile aynı): en kısa gidiş-dönüş; üs < -4 ya da >= 16 ise bilimsel gösterim.
pub fn float_repr(x: f64) -> String {
    if x.is_nan() {
        return "nan".into();
    }
    if x.is_infinite() {
        return if x > 0.0 { "inf".into() } else { "-inf".into() };
    }
    let e = format!("{x:e}"); // örn. 1.2345e2
    let (mant, us) = e.split_once('e').unwrap();
    let us: i32 = us.parse().unwrap();
    let neg = mant.starts_with('-');
    let rakamlar: String = mant.chars().filter(|c| c.is_ascii_digit()).collect();
    let isaret = if neg { "-" } else { "" };
    if (-4..16).contains(&us) {
        let n = rakamlar.len() as i32;
        if us >= 0 {
            let tam = (us + 1) as usize;
            if rakamlar.len() <= tam {
                format!("{isaret}{rakamlar}{}.0", "0".repeat(tam - rakamlar.len()))
            } else {
                format!("{isaret}{}.{}", &rakamlar[..tam], &rakamlar[tam..])
            }
        } else {
            let _ = n;
            format!("{isaret}0.{}{rakamlar}", "0".repeat((-us - 1) as usize))
        }
    } else {
        let govde = if rakamlar.len() > 1 { format!("{}.{}", &rakamlar[..1], &rakamlar[1..]) } else { rakamlar };
        format!("{isaret}{govde}e{}{:02}", if us < 0 { '-' } else { '+' }, us.abs())
    }
}

/// `re.IGNORECASE` karşılığı için katlama: her karakter tek karakterli basit küçük harfe, `ı`/`İ` -> `i`, `ſ` -> `s`.
/// Karakter sayısı korunur (eşleşme konumları orijinal metne geri çevrilebilir).
pub fn katla(s: &str) -> String {
    s.chars()
        .map(|c| {
            let mut l = c.to_lowercase();
            let ilk = l.next().unwrap_or(c);
            let c1 = if l.next().is_some() { if c == '\u{130}' { 'i' } else { c } } else { ilk };
            match c1 {
                'ı' => 'i',
                'ſ' => 's',
                x => x,
            }
        })
        .collect()
}

/// Katlanmış metinde `re` ile ara; eşleşen kısmı ORİJİNAL metinden döndür (`m.group(0)`).
pub fn katlanmis_ara(metin: &str, re: &regex::Regex) -> Option<String> {
    let k = katla(metin);
    let m = re.find(&k)?;
    let bas = k[..m.start()].chars().count();
    let uz = k[m.start()..m.end()].chars().count();
    Some(metin.chars().skip(bas).take(uz).collect())
}

/// Python `UnicodeDecodeError` iletisi ('utf-8' codec can't decode ...) ilk geçersiz dizi için; geçerliyse `None`.
pub fn utf8_hata_iletisi(b: &[u8]) -> Option<String> {
    let e = std::str::from_utf8(b).err()?;
    let bas = e.valid_up_to();
    let (son, neden) = match e.error_len() {
        Some(n) => {
            let lead = b[bas];
            let n = n.max(1);
            (bas + n, if n == 1 && (matches!(lead, 0x80..=0xC1 | 0xF5..=0xFF)) { "invalid start byte" } else { "invalid continuation byte" })
        }
        None => (b.len(), "unexpected end of data"),
    };
    Some(if son - bas == 1 {
        format!("'utf-8' codec can't decode byte 0x{:02x} in position {bas}: {neden}", b[bas])
    } else {
        format!("'utf-8' codec can't decode bytes in position {bas}-{}: {neden}", son - 1)
    })
}
