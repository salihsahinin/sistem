//! Python 3.11 `json.load` çözücüsünün (C ayrıştırıcı) hata iletileriyle birlikte karşılığı: `Expecting value`, `Expecting ',' delimiter`, `Extra data` ...
//! `paralel-kapi` manifest bütünlük hatalarında Python iletisini (`JSON okunamadı (...)`) aynen basar. `NaN`/`Infinity` sabitleri `null` olarak okunur.
use serde_json::{Map, Number, Value};

pub struct Hata {
    pub ileti: String,
    /// kod noktası indeksi
    pub konum: usize,
}

type S = Result<(Value, usize), Hata>;

fn hata(ileti: &str, konum: usize) -> Hata {
    Hata { ileti: ileti.into(), konum }
}

/// `JSONDecodeError.__str__`: `ileti: line L column C (char P)`.
pub fn hata_metni(belge: &[char], h: &Hata) -> String {
    let once = &belge[..h.konum.min(belge.len())];
    let satir = once.iter().filter(|&&c| c == '\n').count() + 1;
    let sutun = match once.iter().rposition(|&c| c == '\n') {
        Some(i) => h.konum - i,
        None => h.konum + 1,
    };
    format!("{}: line {satir} column {sutun} (char {})", h.ileti, h.konum)
}

struct Cozucu<'a> {
    s: &'a [char],
}

/// `StopIteration(idx)` taşıyıcı: dışarıda `Expecting value` olur.
const DUR: &str = "\u{0}dur";

impl Cozucu<'_> {
    fn bosluk(&self, mut i: usize) -> usize {
        while i < self.s.len() && matches!(self.s[i], ' ' | '\t' | '\n' | '\r') {
            i += 1;
        }
        i
    }

    fn deger(&self, idx: usize) -> S {
        let s = self.s;
        let n = s.len();
        if idx >= n {
            return Err(hata(DUR, idx));
        }
        let basla = |lit: &str| s[idx..].iter().take(lit.chars().count()).copied().eq(lit.chars());
        match s[idx] {
            '"' => self.dize(idx + 1).map(|(t, e)| (Value::String(t), e)),
            '{' => self.nesne(idx + 1),
            '[' => self.dizi(idx + 1),
            'n' if basla("null") => Ok((Value::Null, idx + 4)),
            't' if basla("true") => Ok((Value::Bool(true), idx + 4)),
            'f' if basla("false") => Ok((Value::Bool(false), idx + 5)),
            'N' if basla("NaN") => Ok((Value::Null, idx + 3)),
            'I' if basla("Infinity") => Ok((Value::Null, idx + 8)),
            '-' if basla("-Infinity") => Ok((Value::Null, idx + 9)),
            _ => self.sayi(idx),
        }
    }

    fn sayi(&self, bas: usize) -> S {
        let s = self.s;
        let n = s.len();
        let mut i = bas;
        if i < n && s[i] == '-' {
            i += 1;
        }
        if i >= n {
            return Err(hata(DUR, bas));
        }
        let rakam = |j: usize| j < n && s[j].is_ascii_digit();
        match s[i] {
            '1'..='9' => {
                i += 1;
                while rakam(i) {
                    i += 1;
                }
            }
            '0' => i += 1,
            _ => return Err(hata(DUR, bas)),
        }
        let mut ondalik = false;
        if i < n && s[i] == '.' && rakam(i + 1) {
            ondalik = true;
            i += 2;
            while rakam(i) {
                i += 1;
            }
        }
        if i < n && (s[i] == 'e' || s[i] == 'E') {
            let e0 = i;
            i += 1;
            if i < n && (s[i] == '-' || s[i] == '+') {
                i += 1;
            }
            if rakam(i) {
                while rakam(i) {
                    i += 1;
                }
                ondalik = true;
            } else {
                i = e0;
            }
        }
        let metin: String = s[bas..i].iter().collect();
        let v = if ondalik {
            Number::from_f64(metin.parse::<f64>().unwrap_or(0.0)).map(Value::Number).unwrap_or(Value::Null)
        } else {
            match metin.parse::<i64>() {
                Ok(x) => Value::Number(x.into()),
                Err(_) => match metin.parse::<u64>() {
                    Ok(x) => Value::Number(x.into()),
                    Err(_) => Number::from_f64(metin.parse::<f64>().unwrap_or(0.0)).map(Value::Number).unwrap_or(Value::Null),
                },
            }
        };
        Ok((v, i))
    }

    fn nesne(&self, mut idx: usize) -> S {
        let s = self.s;
        let n = s.len();
        let mut o = Map::new();
        idx = self.bosluk(idx);
        if idx >= n || s[idx] != '}' {
            loop {
                if idx >= n || s[idx] != '"' {
                    return Err(hata("Expecting property name enclosed in double quotes", idx));
                }
                let (anahtar, e) = self.dize(idx + 1)?;
                idx = self.bosluk(e);
                if idx >= n || s[idx] != ':' {
                    return Err(hata("Expecting ':' delimiter", idx));
                }
                idx = self.bosluk(idx + 1);
                let (v, e) = self.deger(idx)?;
                o.insert(anahtar, v);
                idx = self.bosluk(e);
                if idx < n && s[idx] == '}' {
                    break;
                }
                if idx >= n || s[idx] != ',' {
                    return Err(hata("Expecting ',' delimiter", idx));
                }
                idx = self.bosluk(idx + 1);
            }
        }
        Ok((Value::Object(o), idx + 1))
    }

    fn dizi(&self, mut idx: usize) -> S {
        let s = self.s;
        let n = s.len();
        let mut l = vec![];
        idx = self.bosluk(idx);
        if idx >= n || s[idx] != ']' {
            loop {
                let (v, e) = self.deger(idx)?;
                l.push(v);
                idx = self.bosluk(e);
                if idx < n && s[idx] == ']' {
                    break;
                }
                if idx >= n || s[idx] != ',' {
                    return Err(hata("Expecting ',' delimiter", idx));
                }
                idx = self.bosluk(idx + 1);
            }
        }
        Ok((Value::Array(l), idx + 1))
    }

    /// `scanstring_unicode` (strict): `bas` açılış tırnağından sonraki indeks.
    fn dize(&self, bas: usize) -> Result<(String, usize), Hata> {
        let s = self.s;
        let n = s.len();
        let acilis = bas - 1;
        let mut cikti = String::new();
        let mut end = bas;
        loop {
            let mut next = end;
            let mut d = '\0';
            while next < n {
                d = s[next];
                if d == '"' || d == '\\' {
                    break;
                }
                if (d as u32) <= 0x1f {
                    return Err(hata("Invalid control character at", next));
                }
                next += 1;
            }
            if !(d == '"' || d == '\\') || next >= n {
                return Err(hata("Unterminated string starting at", acilis));
            }
            cikti.extend(&s[end..next]);
            next += 1;
            if d == '"' {
                return Ok((cikti, next));
            }
            if next == n {
                return Err(hata("Unterminated string starting at", acilis));
            }
            let c = s[next];
            if c != 'u' {
                end = next + 1;
                let ch = match c {
                    '"' => '"',
                    '\\' => '\\',
                    '/' => '/',
                    'b' => '\u{8}',
                    'f' => '\u{c}',
                    'n' => '\n',
                    'r' => '\r',
                    't' => '\t',
                    _ => return Err(hata("Invalid \\escape", end - 2)),
                };
                cikti.push(ch);
            } else {
                next += 1;
                end = next + 4;
                if end >= n {
                    return Err(hata("Invalid \\uXXXX escape", next - 1));
                }
                let mut kod: u32 = 0;
                for &ch in &s[next..end] {
                    match ch.to_digit(16) {
                        Some(x) if ch.is_ascii() => kod = kod << 4 | x,
                        _ => return Err(hata("Invalid \\uXXXX escape", end - 5)),
                    }
                }
                next = end;
                // vekil çifti
                if (0xD800..0xDC00).contains(&kod) && end + 6 < n && s[next] == '\\' && s[next + 1] == 'u' {
                    let mut kod2: u32 = 0;
                    let e2 = end + 6;
                    let mut gecerli = true;
                    for &ch in &s[next + 2..e2] {
                        match ch.to_digit(16) {
                            Some(x) if ch.is_ascii() => kod2 = kod2 << 4 | x,
                            _ => {
                                gecerli = false;
                                break;
                            }
                        }
                    }
                    if !gecerli {
                        return Err(hata("Invalid \\uXXXX escape", e2 - 5));
                    }
                    if (0xDC00..0xE000).contains(&kod2) {
                        kod = 0x10000 + (((kod - 0xD800) << 10) | (kod2 - 0xDC00));
                        end = e2;
                    }
                }
                cikti.push(char::from_u32(kod).unwrap_or('\u{fffd}'));
            }
        }
    }
}

/// `json.loads(metin)`.
pub fn coz(metin: &str) -> Result<Value, Hata> {
    let s: Vec<char> = metin.chars().collect();
    if s.first() == Some(&'\u{feff}') {
        return Err(hata("Unexpected UTF-8 BOM (decode using utf-8-sig)", 0));
    }
    let c = Cozucu { s: &s };
    let bas = c.bosluk(0);
    let (v, son) = c.deger(bas).map_err(|h| if h.ileti == DUR { hata("Expecting value", h.konum) } else { h })?;
    let son = c.bosluk(son);
    if son != s.len() {
        return Err(hata("Extra data", son));
    }
    Ok(v)
}

/// Hata için gösterim metni (`coz` çağırandan karakter dizisi istemesin diye).
pub fn coz_ileti(metin: &str) -> Result<Value, String> {
    coz(metin).map_err(|h| hata_metni(&metin.chars().collect::<Vec<_>>(), &h))
}
