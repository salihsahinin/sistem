//! devir-md2json: A1 md emrindeki ```lojik bloğundan devir birimi json'u türetir (`tools/devir-md2json.py` karşılığı).
//! Çıkış: 0 türetildi · 2 şema ihlali · 3 --dogrula farkı · 4 dosya/çit yok. Python'da yakalanmamış istisna olan
//! durumlar (`py::coker`) çıkış 1 ile biter (traceback metni taklit edilmez).
use crate::buyuk_harf::pathlib_metni;
use jarvis_rituel::argparse::{Ayrisan, Secenek};
use jarvis_rituel::py::{self, OkuHata};
use regex::Regex;
use serde_json::{Map, Value};
use std::collections::HashMap;
use std::path::Path;

const ACIKLAMA: &str = "devir-md2json.py — A1 md emrindeki ```lojik bloğundan devir birimi json'u (v0.1) türetir.";
const SEMA: &str = "devir-birimi v0.2 (A1 türev; tools/devir-md2json.py; md kazanır; v0.2 09-16: OTURUM · KAPANIŞ · KAYNAKLAR · AÇILIŞ_ADIMLARI, olcen→gorev, kapali_goz_ozeti liste, .aktif-devir yazımı)";
const ZORUNLU: [&str; 23] = [
    "DEVİR_ID", "KAYNAK_YÜZEY", "HEDEF_KATMAN", "TARİH", "EMİR_YOLU",
    "AMAÇ", "ÇIKTI", "DONE", "DALLAR", "NİÇİN_ŞİMDİ", "BAĞLI_DEVİR", "KAPALI_GÖZ_ÖZETİ", "ÖLÇEN",
    "EAGER", "LAZY", "KARAR_ÖZETİ", "YASAK", "YAZMA_İZNİ", "BÜTÇE", "YENİDEN_DENEME", "GİT_İZNİ",
    "OTURUM", "KAPANIŞ",
];
const DAL_TAVANI: usize = 5;

/// Ayrıştırılmış blok değeri: Python'daki `None` · `str` · `list[str]` · `dict[str, str]` (sözlük ekleme sırasını korur).
#[derive(Clone)]
enum V {
    Yok,
    S(String),
    L(Vec<String>),
    D(Vec<(String, String)>),
}

type Veri = HashMap<String, V>;

fn bos_mu(v: &V) -> bool {
    match v {
        V::Yok => true,
        V::S(_) => false,
        V::L(l) => l.is_empty(),
        V::D(d) => d.is_empty(),
    }
}

fn blok_cikar(metin: &str) -> Option<String> {
    let re = Regex::new(r"(?s)```lojik[ \t]*\n(.*?)\n```").unwrap();
    re.captures(metin).map(|c| c[1].to_string())
}

fn blok_ayristir(blok: &str) -> Result<Veri, String> {
    let mut veri: Veri = HashMap::new();
    let mut anahtar: Option<String> = None;
    for ham in py::splitlines(blok) {
        let ciplak = py::strip(&ham);
        if ciplak.is_empty() || ciplak.starts_with('#') {
            continue;
        }
        if !(ham.starts_with(' ') || ham.starts_with('\t')) {
            let (k, v) = match ham.split_once(':') {
                Some((k, v)) => (k, v),
                None => (ham.as_str(), ""),
            };
            let k = py::strip(k).to_string();
            let v = py::strip(v);
            veri.insert(k.clone(), if v.is_empty() { V::Yok } else { V::S(v.to_string()) });
            anahtar = Some(k);
            continue;
        }
        let Some(ak) = anahtar.clone() else {
            return Err(format!("girintili satır anahtarsız: {}", py::repr(&ham)));
        };
        let satir = ciplak;
        let girdi = veri.get_mut(&ak).unwrap();
        if let Some(madde) = satir.strip_prefix("- ") {
            if matches!(girdi, V::Yok) {
                *girdi = V::L(vec![]);
            }
            match girdi {
                V::L(l) => l.push(py::strip(madde).to_string()),
                _ => return Err(format!("{ak}: liste ile skaler/sözlük karışık")),
            }
        } else {
            let Some((k, v)) = satir.split_once(':') else {
                return Err(format!("{ak}: alt satır ne liste ne sözlük: {}", py::repr(satir)));
            };
            if matches!(girdi, V::Yok) {
                *girdi = V::D(vec![]);
            }
            match girdi {
                V::D(d) => {
                    let k = py::strip(k).to_string();
                    let v = py::strip(v).to_string();
                    match d.iter_mut().find(|(a, _)| *a == k) {
                        Some(e) => e.1 = v,
                        None => d.push((k, v)),
                    }
                }
                _ => return Err(format!("{ak}: sözlük ile liste karışık")),
            }
        }
    }
    Ok(veri)
}

/// `str.isdigit()` içindeki ondalık olmayan rakamlar (üst/alt simge, çevrili): `int()` bunları reddeder.
fn ozel_rakam(c: char) -> bool {
    matches!(c as u32,
        0xB2 | 0xB3 | 0xB9 | 0x2070 | 0x2074..=0x2079 | 0x2080..=0x2089 | 0x2460..=0x2468 | 0x2474..=0x247C
        | 0x2488..=0x2490 | 0x24EA | 0x24F5..=0x24FD | 0x24FF | 0x2776..=0x277E | 0x2780..=0x2788
        | 0x278A..=0x2792 | 0x10A40..=0x10A43 | 0x1F100..=0x1F10A)
}

/// `str.isdigit()`.
fn rakam_mi(s: &str) -> bool {
    !s.is_empty() && s.chars().all(|c| c.is_ascii_digit() || ozel_rakam(c) || py::int(&c.to_string()).is_some())
}

/// `int(s)` (s rakam dizisi): ondalık olmayan rakam varsa Python `ValueError` verirdi → `None`.
fn tam_sayi(s: &str) -> Option<Value> {
    let n = py::int(s)?;
    Some(match u64::try_from(n) {
        Ok(u) => Value::from(u),
        Err(_) => Value::from(n as f64), // bilinçli ayrışma: u64 üstü tamsayılar float olur
    })
}

fn butce_ayristir(v: &V) -> Result<Value, String> {
    let V::S(s) = v else {
        return Err("BÜTÇE metin değil (split)".into());
    };
    let mut out = Map::new();
    for parca in s.split(py::bosluk_mu).filter(|p| !p.is_empty()) {
        let (k, v) = parca.split_once('=').unwrap_or((parca, ""));
        let deger = if rakam_mi(v) {
            tam_sayi(v).ok_or_else(|| format!("BÜTÇE: int({}) geçersiz", py::repr(v)))?
        } else {
            Value::String(v.to_string())
        };
        out.insert(k.to_string(), deger);
    }
    Ok(Value::Object(out))
}

/// Python `str(x)` (liste/sözlük repr'i).
fn py_str(v: &V) -> String {
    match v {
        V::Yok => "None".into(),
        V::S(s) => s.clone(),
        V::L(l) => format!("[{}]", l.iter().map(|x| py::repr(x)).collect::<Vec<_>>().join(", ")),
        V::D(d) => format!("{{{}}}", d.iter().map(|(k, v)| format!("{}: {}", py::repr(k), py::repr(v))).collect::<Vec<_>>().join(", ")),
    }
}

// ---------------------------------------------------------------- fnmatch
enum Tok {
    Lit(char),
    Bir,
    Yildiz,
    Sinif(bool, Vec<(char, char)>),
}

/// `fnmatch.translate` içindeki `[...]` işleme (Python 3.11): tire parçalama + boş aralık eleme; çıktı kaçışlı küme gövdesi.
fn sinif_govde(pat: &[char], i0: usize, j: usize) -> String {
    let stuff: &[char] = &pat[i0..j];
    let kac = |c: &[char], tire: bool| -> String {
        let mut s = String::new();
        for &x in c {
            if x == '\\' || (tire && x == '-') {
                s.push('\\');
            }
            s.push(x);
        }
        s
    };
    if !stuff.contains(&'-') {
        return kac(stuff, false);
    }
    let mut chunks: Vec<Vec<char>> = vec![];
    let mut i = i0;
    let mut k = if pat[i] == '!' { i + 2 } else { i + 1 };
    loop {
        let bulundu = (k..j.max(k)).find(|&x| x < j && pat[x] == '-');
        let Some(kk) = bulundu else { break };
        chunks.push(pat[i..kk].to_vec());
        i = kk + 1;
        k = kk + 3;
    }
    let chunk = pat[i.min(j)..j].to_vec();
    if !chunk.is_empty() {
        chunks.push(chunk);
    } else if let Some(son) = chunks.last_mut() {
        son.push('-');
    }
    let mut k = chunks.len();
    while k > 1 {
        k -= 1;
        if let (Some(&a), Some(&b)) = (chunks[k - 1].last(), chunks[k].first()) {
            if a > b {
                let mut yeni = chunks[k - 1][..chunks[k - 1].len() - 1].to_vec();
                yeni.extend_from_slice(&chunks[k][1..]);
                chunks[k - 1] = yeni;
                chunks.remove(k);
            }
        }
    }
    chunks.iter().map(|c| kac(c, true)).collect::<Vec<_>>().join("-")
}

fn desen_coz(pat: &[char]) -> Vec<Tok> {
    let mut t: Vec<Tok> = vec![];
    let n = pat.len();
    let mut i = 0;
    while i < n {
        let c = pat[i];
        i += 1;
        match c {
            '*' => {
                if !matches!(t.last(), Some(Tok::Yildiz)) {
                    t.push(Tok::Yildiz);
                }
            }
            '?' => t.push(Tok::Bir),
            '[' => {
                let mut j = i;
                if j < n && pat[j] == '!' {
                    j += 1;
                }
                if j < n && pat[j] == ']' {
                    j += 1;
                }
                while j < n && pat[j] != ']' {
                    j += 1;
                }
                if j >= n {
                    t.push(Tok::Lit('['));
                } else {
                    let govde: Vec<char> = sinif_govde(pat, i, j).chars().collect();
                    i = j + 1;
                    let (neg, g) = match govde.first() {
                        Some('!') => (true, &govde[1..]),
                        _ => (false, &govde[..]),
                    };
                    // küme gövdesi: `\x` düz karakter, kaçışsız `a-b` aralık
                    let mut ogeler: Vec<(char, char)> = vec![];
                    let mut p = 0;
                    let oku = |p: &mut usize| -> Option<char> {
                        let c = *g.get(*p)?;
                        *p += 1;
                        if c == '\\' && *p < g.len() {
                            let d = g[*p];
                            *p += 1;
                            return Some(d);
                        }
                        Some(c)
                    };
                    while let Some(a) = oku(&mut p) {
                        if g.get(p) == Some(&'-') && p + 1 < g.len() {
                            p += 1;
                            if let Some(b) = oku(&mut p) {
                                ogeler.push((a, b));
                                continue;
                            }
                        }
                        ogeler.push((a, a));
                    }
                    t.push(Tok::Sinif(neg, ogeler));
                }
            }
            _ => t.push(Tok::Lit(c)),
        }
    }
    t
}

fn tek_uyar(t: &Tok, c: char) -> bool {
    match t {
        Tok::Lit(l) => *l == c,
        Tok::Bir => true,
        Tok::Sinif(neg, o) => o.iter().any(|&(a, b)| a <= c && c <= b) != *neg,
        Tok::Yildiz => false,
    }
}

fn fnmatchcase(ad: &str, kalip: &str) -> bool {
    let a: Vec<char> = ad.chars().collect();
    let k: Vec<char> = kalip.chars().collect();
    let t = desen_coz(&k);
    let (mut i, mut j) = (0usize, 0usize);
    let mut yildiz: Option<(usize, usize)> = None;
    while i < a.len() {
        if j < t.len() && matches!(t[j], Tok::Yildiz) {
            yildiz = Some((j, i));
            j += 1;
        } else if j < t.len() && tek_uyar(&t[j], a[i]) {
            i += 1;
            j += 1;
        } else if let Some((yj, yi)) = yildiz {
            yildiz = Some((yj, yi + 1));
            j = yj + 1;
            i = yi + 1;
        } else {
            return false;
        }
    }
    while j < t.len() && matches!(t[j], Tok::Yildiz) {
        j += 1;
    }
    j == t.len()
}

/// `fnmatch.fnmatch` (Windows'ta `normcase`: küçük harf + `/` → `\`).
fn fnmatch(ad: &str, kalip: &str) -> bool {
    if cfg!(windows) {
        fnmatchcase(&ad.replace('/', "\\").to_lowercase(), &kalip.replace('/', "\\").to_lowercase())
    } else {
        fnmatchcase(ad, kalip)
    }
}

// ---------------------------------------------------------------- doğrulama
fn liste_v(v: &V) -> Vec<V> {
    match v {
        V::L(l) => l.iter().map(|s| V::S(s.clone())).collect(),
        x => vec![x.clone()],
    }
}

/// `Err` = Python'da yakalanmamış istisna.
fn dogrula(v: &Veri) -> Result<Vec<String>, String> {
    let mut hatalar: Vec<String> = vec![];
    for k in ZORUNLU {
        if v.get(k).is_none_or(bos_mu) {
            hatalar.push(format!("eksik alan: {k}"));
        }
    }
    if !hatalar.is_empty() {
        return Ok(hatalar);
    }
    let (V::D(cikti), V::D(done)) = (&v["ÇIKTI"], &v["DONE"]) else {
        return Ok(vec!["ÇIKTI ve DONE 'Cn: …' sözlük biçiminde olmalı (çıktı-başına done)".into()]);
    };
    for (c, yol) in cikti {
        if !done.iter().any(|(d, _)| d == c) {
            hatalar.push(format!("DONE eksik: {c} ({yol})"));
        }
    }
    for (c, _) in done {
        if !cikti.iter().any(|(d, _)| d == c) {
            hatalar.push(format!("DONE var, ÇIKTI yok: {c}"));
        }
    }
    let izin: Vec<String> = match &v["YAZMA_İZNİ"] {
        V::L(l) => l.clone(),
        V::S(s) => vec![s.clone()],
        _ => return Err("fnmatch(yol, sözlük): TypeError".into()),
    };
    for (c, yol) in cikti {
        if !izin.iter().any(|kalip| fnmatch(yol, kalip) || yol.starts_with(kalip.trim_end_matches('*'))) {
            hatalar.push(format!("çıktı yazma-izni dışında: {c} {yol} ∉ YAZMA_İZNİ"));
        }
    }
    let dallar = &v["DALLAR"];
    let dal_sayisi = match dallar {
        V::L(l) => l.len(),
        _ => 1,
    };
    if dal_sayisi > DAL_TAVANI {
        hatalar.push(format!("dal sayısı {dal_sayisi} > {DAL_TAVANI} — görevi böl"));
    }
    match dallar {
        V::L(l) => {
            for d in l {
                if !d.contains('→') {
                    hatalar.push(format!("dal '→' içermiyor (koşul → eylem): {}", py::ilk(d, 60)));
                }
            }
        }
        V::S(d) => {
            if !d.contains('→') {
                hatalar.push(format!("dal '→' içermiyor (koşul → eylem): {}", py::ilk(d, 60)));
            }
        }
        V::D(d) => {
            if !d.iter().any(|(k, _)| k == "→") {
                return Err("d[:60] sözlükte: TypeError".into());
            }
        }
        V::Yok => {}
    }
    if !matches!(&v["YENİDEN_DENEME"], V::S(s) if rakam_mi(s)) {
        hatalar.push("YENİDEN_DENEME tam sayı değil".into());
    }
    if !matches!(&v["OTURUM"], V::S(s) if s == "devam" || s == "yeni") {
        hatalar.push("OTURUM 'devam' ya da 'yeni' olmalı".into());
    }
    let mut parcalar: Vec<String> = vec![py_str(&v["AMAÇ"]), py_str(&v["NİÇİN_ŞİMDİ"])];
    parcalar.extend(liste_v(dallar).iter().map(py_str));
    parcalar.extend(done.iter().map(|(_, x)| x.clone()));
    let butun = parcalar.join(" ");
    let kaynak_var = v.get("KAYNAKLAR").is_some_and(|k| !bos_mu(k));
    if (butun.contains("http://") || butun.contains("https://") || butun.contains("/docs/")) && !kaynak_var {
        hatalar.push("blokta URL/doküman anılıyor ama KAYNAKLAR yok (Friday tur-3 a1: kaynak bağlayıcı metinde olmalı)".into());
    }
    Ok(hatalar)
}

// ---------------------------------------------------------------- json türetme
fn deger(v: &V) -> Value {
    match v {
        V::Yok => Value::Null,
        V::S(s) => Value::String(s.clone()),
        V::L(l) => Value::Array(l.iter().map(|s| Value::String(s.clone())).collect()),
        V::D(d) => sozluk(d),
    }
}

fn sozluk(d: &[(String, String)]) -> Value {
    let mut m = Map::new();
    for (k, v) in d {
        m.insert(k.clone(), Value::String(v.clone()));
    }
    Value::Object(m)
}

/// Python `liste(x)`: liste değilse tek elemanlı liste.
fn liste(v: &V) -> Value {
    match v {
        V::L(_) => deger(v),
        x => Value::Array(vec![deger(x)]),
    }
}

/// `liste(v.get(k) or [])`.
fn liste_veya_bos(v: Option<&V>) -> Value {
    match v {
        Some(x) if !bos_mu(x) => liste(x),
        _ => Value::Array(vec![]),
    }
}

fn dogru_mu(v: Option<&V>) -> bool {
    match v {
        None => false,
        Some(x) => py_str(x).to_lowercase() == "true",
    }
}

fn nesne(girdiler: Vec<(&str, Value)>) -> Value {
    let mut m = Map::new();
    for (k, v) in girdiler {
        m.insert(k.to_string(), v);
    }
    Value::Object(m)
}

fn json_uret(v: &Veri, emir_yolu: &str) -> Result<Value, String> {
    let V::D(cikti) = &v["ÇIKTI"] else { unreachable!() };
    let V::D(done) = &v["DONE"] else { unreachable!() };
    let done_birlesik = cikti
        .iter()
        .map(|(c, _)| format!("[{c}] {}", done.iter().find(|(d, _)| d == c).map(|(_, x)| x.as_str()).unwrap_or("")))
        .collect::<Vec<_>>()
        .join(" ∧ ");
    let V::S(deneme) = &v["YENİDEN_DENEME"] else { unreachable!() };
    let deneme = tam_sayi(deneme).ok_or("int(YENİDEN_DENEME): ValueError")?;
    let butce = butce_ayristir(&v["BÜTÇE"])?;
    let kaynaklar = match v.get("KAYNAKLAR") {
        Some(V::D(d)) => sozluk(d),
        k => liste_veya_bos(k),
    };
    let g = |k: &str| &v[k];
    Ok(nesne(vec![
        ("_sema", Value::String(SEMA.into())),
        ("_kaynak_md", Value::String(emir_yolu.into())),
        ("devir", nesne(vec![
            ("kimlik", nesne(vec![
                ("devir_id", deger(g("DEVİR_ID"))), ("kaynak_yuzey", deger(g("KAYNAK_YÜZEY"))), ("hedef_katman", deger(g("HEDEF_KATMAN"))),
                ("tarih", deger(g("TARİH"))), ("emir_yolu", deger(g("EMİR_YOLU"))), ("bagli_devir", deger(g("BAĞLI_DEVİR"))),
            ])),
            ("gorev", nesne(vec![
                ("amac", deger(g("AMAÇ"))), ("nicin_simdi", deger(g("NİÇİN_ŞİMDİ"))),
                ("ciktilar", sozluk(cikti)), ("done_cikti_basina", sozluk(done)),
                ("done_yuklemi", Value::String(done_birlesik)), ("dallar", liste(g("DALLAR"))),
                ("yeniden_deneme", deneme), ("olcen", deger(g("ÖLÇEN"))),
                ("kapanis", liste(g("KAPANIŞ"))),
            ])),
            ("oturum", nesne(vec![("durum", deger(g("OTURUM"))), ("acilis_adimlari", liste_veya_bos(v.get("AÇILIŞ_ADIMLARI")))])),
            ("kaynaklar", kaynaklar),
            ("baglam", nesne(vec![
                ("eager", liste(g("EAGER"))), ("lazy", liste(g("LAZY"))), ("karar_ozeti", liste(g("KARAR_ÖZETİ"))),
                ("yasak", liste(g("YASAK"))), ("kapali_goz_ozeti", liste(g("KAPALI_GÖZ_ÖZETİ"))),
            ])),
            ("butce", butce),
            ("yetki", nesne(vec![
                ("karar_yetkisi", Value::Bool(match v.get("KARAR_YETKİSİ") { None => false, k => dogru_mu(k) })),
                ("yazma_izni", liste(g("YAZMA_İZNİ"))), ("git_izni", deger(g("GİT_İZNİ"))),
                ("push", Value::Bool(match v.get("PUSH") { None => false, k => dogru_mu(k) })),
            ])),
        ])),
    ]))
}

// ---------------------------------------------------------------- json yazımı (`json.dumps(ensure_ascii=False, indent=2, sort_keys=True)`)
fn dize_yaz(s: &str, o: &mut String) {
    o.push('"');
    for c in s.chars() {
        match c {
            '"' => o.push_str("\\\""),
            '\\' => o.push_str("\\\\"),
            '\n' => o.push_str("\\n"),
            '\r' => o.push_str("\\r"),
            '\t' => o.push_str("\\t"),
            '\u{8}' => o.push_str("\\b"),
            '\u{c}' => o.push_str("\\f"),
            c if (c as u32) < 0x20 => o.push_str(&format!("\\u{:04x}", c as u32)),
            c => o.push(c),
        }
    }
    o.push('"');
}

fn yaz(v: &Value, girinti: usize, o: &mut String) {
    let bosluk = |n: usize| " ".repeat(n * 2);
    match v {
        Value::Null => o.push_str("null"),
        Value::Bool(b) => o.push_str(if *b { "true" } else { "false" }),
        Value::Number(n) => o.push_str(&n.to_string()),
        Value::String(s) => dize_yaz(s, o),
        Value::Array(a) => {
            if a.is_empty() {
                o.push_str("[]");
                return;
            }
            o.push_str("[\n");
            for (i, x) in a.iter().enumerate() {
                o.push_str(&bosluk(girinti + 1));
                yaz(x, girinti + 1, o);
                o.push_str(if i + 1 < a.len() { ",\n" } else { "\n" });
            }
            o.push_str(&bosluk(girinti));
            o.push(']');
        }
        Value::Object(m) => {
            if m.is_empty() {
                o.push_str("{}");
                return;
            }
            let mut anahtarlar: Vec<&String> = m.keys().collect();
            anahtarlar.sort();
            o.push_str("{\n");
            for (i, k) in anahtarlar.iter().enumerate() {
                o.push_str(&bosluk(girinti + 1));
                dize_yaz(k, o);
                o.push_str(": ");
                yaz(&m[k.as_str()], girinti + 1, o);
                o.push_str(if i + 1 < anahtarlar.len() { ",\n" } else { "\n" });
            }
            o.push_str(&bosluk(girinti));
            o.push('}');
        }
    }
}

/// Python `==` (sayılar değer olarak, `True == 1`).
fn py_esit(a: &Value, b: &Value) -> bool {
    fn sayi(v: &Value) -> Option<f64> {
        match v {
            Value::Number(n) => n.as_f64(),
            Value::Bool(b) => Some(*b as u8 as f64),
            _ => None,
        }
    }
    if let (Some(x), Some(y)) = (sayi(a), sayi(b)) {
        if let (Value::Number(p), Value::Number(q)) = (a, b) {
            if p.is_i64() && q.is_i64() || p.is_u64() && q.is_u64() {
                return p == q;
            }
        }
        return x == y;
    }
    match (a, b) {
        (Value::Array(x), Value::Array(y)) => x.len() == y.len() && x.iter().zip(y).all(|(p, q)| py_esit(p, q)),
        (Value::Object(x), Value::Object(y)) => x.len() == y.len() && x.iter().all(|(k, p)| y.get(k).is_some_and(|q| py_esit(p, q))),
        _ => a == b,
    }
}

fn ebeveyn_birlestir(yol: &str, ad: &str) -> String {
    let (surucu, r) = py::splitdrive(yol);
    let kokte = r.starts_with(py::SEP);
    let mut parcalar: Vec<&str> = r.split(py::SEP).filter(|x| !x.is_empty()).collect();
    parcalar.pop();
    let mut ebeveyn = format!("{surucu}{}{}", if kokte { py::SEP.to_string() } else { String::new() }, parcalar.join(&py::SEP.to_string()));
    if ebeveyn.is_empty() {
        ebeveyn = ".".into();
    }
    let birlesik = if ebeveyn == "." {
        ad.to_string()
    } else if ebeveyn.ends_with(py::SEP) || ebeveyn.ends_with(':') {
        format!("{ebeveyn}{ad}")
    } else {
        format!("{ebeveyn}{}{ad}", py::SEP)
    };
    pathlib_metni(&birlesik)
}

/// Açıklama `Ayrisan` içinde sarılmadığından burada hazırlanır (`argparse::aciklama_sar`).
static ACIKLAMA_SARILI: std::sync::LazyLock<String> = std::sync::LazyLock::new(|| jarvis_rituel::argparse::aciklama_sar(ACIKLAMA));

pub fn kos(argv: &[String]) -> i32 {
    let ayrisan = Ayrisan::yeni(
        "devir-md2json.py",
        Some(ACIKLAMA_SARILI.as_str()),
        vec![
            Secenek::deger(&["--cikti"], "cikti", Some("json yolu (varsayılan: emirle aynı dizin, <DEVİR_ID>.json)")),
            Secenek::deger(&["--dogrula"], "dogrula", Some("mevcut json ile karşılaştır; fark → çıkış 3 (md kazanır)")),
            Secenek::bayrak(&["--kuru"], "kuru", Some("yazma, json'u stdout'a bas")),
        ],
    )
    .konumsal("emir");
    let a = match ayrisan.ayristir(argv) {
        Ok(a) => a,
        Err(k) => return k,
    };

    let yol = pathlib_metni(a.konumsal().unwrap_or(""));
    if !Path::new(&yol).exists() {
        py::err(&format!("HATA: emir yok: {yol}\n"));
        return 4;
    }
    let metin_md = match py::oku_kati(Path::new(&yol)) {
        Ok(m) => m,
        Err(OkuHata::Io(e)) => return py::coker(&format!("emir okunamadı: {e}")),
        Err(OkuHata::Kod) => return py::coker("emir UTF-8 değil (UnicodeDecodeError)"),
    };
    let Some(blok) = blok_cikar(&metin_md) else {
        py::err("HATA: ```lojik çiti bulunamadı (A1 formatı değil)\n");
        return 4;
    };
    let v = match blok_ayristir(&blok) {
        Ok(v) => v,
        Err(e) => {
            py::err(&format!("ŞEMA: {e}\n"));
            return 2;
        }
    };
    let hatalar = match dogrula(&v) {
        Ok(h) => h,
        Err(n) => return py::coker(&n),
    };
    if !hatalar.is_empty() {
        py::err(&format!("ŞEMA İHLALİ ({}):\n  {}\n", hatalar.len(), hatalar.join("\n  ")));
        return 2;
    }
    let j = match json_uret(&v, &yol) {
        Ok(j) => j,
        Err(n) => return py::coker(&n),
    };
    let mut metin = String::new();
    yaz(&j, 0, &mut metin);
    metin.push('\n');

    if let Some(dg) = a.metin("dogrula").filter(|s| !s.is_empty()) {
        let ham = match py::oku_kati(Path::new(&pathlib_metni(dg))) {
            Ok(m) => m,
            Err(OkuHata::Io(e)) => return py::coker(&format!("--dogrula okunamadı: {e}")),
            Err(OkuHata::Kod) => return py::coker("--dogrula UTF-8 değil (UnicodeDecodeError)"),
        };
        let Ok(eski) = serde_json::from_str::<Value>(&ham) else {
            return py::coker("--dogrula json değil (JSONDecodeError)");
        };
        if !py_esit(&eski, &j) {
            let Value::Object(eski_o) = &eski else {
                return py::coker("eski.get: json kökü sözlük değil");
            };
            let bos = Map::new();
            let eski_devir = match eski_o.get("devir") {
                None => &bos,
                Some(Value::Object(m)) => m,
                Some(_) => return py::coker("eski['devir'] sözlük değil"),
            };
            let yeni_devir = j["devir"].as_object().unwrap();
            let mut anahtarlar: Vec<&String> = eski_devir.keys().chain(yeni_devir.keys()).collect();
            anahtarlar.sort();
            anahtarlar.dedup();
            let bos_deger = Value::Null;
            let farklar: Vec<String> = anahtarlar
                .into_iter()
                .filter(|k| !py_esit(eski_devir.get(*k).unwrap_or(&bos_deger), yeni_devir.get(*k).unwrap_or(&bos_deger)))
                .map(|k| py::repr(k))
                .collect();
            py::err(&format!("FARK: json ≠ md türevi; farklı bloklar: [{}] — md kazanır, json'u yeniden türet\n", farklar.join(", ")));
            return 3;
        }
        py::print("EŞ: json = md türevi");
        return 0;
    }
    if a.bayrak("kuru") {
        py::out(&metin);
        return 0;
    }
    let devir_id = py_str(&v["DEVİR_ID"]);
    let hedef = match a.metin("cikti").filter(|s| !s.is_empty()) {
        Some(c) => pathlib_metni(c),
        None => ebeveyn_birlestir(&yol, &format!("{devir_id}.json")),
    };
    if let Err(e) = std::fs::write(&hedef, metin.as_bytes()) {
        return py::coker(&format!("{hedef} yazılamadı: {e}"));
    }
    // DEVİR_ID liste/sözlük ise Python `v["DEVİR_ID"] + "\n"` TypeError verirdi (json yazıldıktan sonra)
    let V::S(kimlik) = &v["DEVİR_ID"] else {
        return py::coker("DEVİR_ID + '\\n': TypeError");
    };
    let aktif = ebeveyn_birlestir(&yol, ".aktif-devir");
    if let Err(e) = std::fs::write(&aktif, format!("{kimlik}\n").as_bytes()) {
        return py::coker(&format!("{aktif} yazılamadı: {e}"));
    }
    py::print(&format!("TÜRETİLDİ: {hedef} ({} B; çıktı {} · dal {})", metin.chars().count(), cikti_sayisi(&v), dal_sayisi(&v)));
    0
}

fn cikti_sayisi(v: &Veri) -> usize {
    match &v["ÇIKTI"] {
        V::D(d) => d.len(),
        _ => 0,
    }
}

fn dal_sayisi(v: &Veri) -> usize {
    match &v["DALLAR"] {
        V::L(l) => l.len(),
        _ => 1,
    }
}
