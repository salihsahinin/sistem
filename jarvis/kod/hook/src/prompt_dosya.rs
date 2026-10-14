//! `tools/prompt-dosya.py` karşılığı (İB-79): prompt'u `core/prompt-dosya-tablosu.tsv` ile eşler, kaynak parçalarını basar.
use crate::ortak::{Ortam, Sonuc, ekle_satir, json_oku, oku_py, py_dilim, py_dumps, ts_yerel, yerel_ayrac};
use regex::{Regex, RegexBuilder};
use serde_json::{Value, json};
use std::path::{Path, PathBuf};

pub const PARCA_BAYT: usize = 1500;
pub const TOPLAM_BAYT: usize = 4000;

#[derive(Debug, Clone)]
pub struct Parca {
    pub anahtar: String,
    pub kaynak: String,
    pub etiket: Option<String>,
    pub metin: String,
    pub not: String,
}

/// Python `re.IGNORECASE` yaklaşığı: desendeki i/I/İ/ı (kaçışsız, sınıf dışı ya da sınıf içinde tekil) dört harfli sınıfa açılır.
pub fn ignorecase_desen(d: &str) -> String {
    const IIII: &str = "iIİı";
    let c: Vec<char> = d.chars().collect();
    let mut o = String::new();
    let (mut i, mut sinif) = (0, false);
    while i < c.len() {
        let ch = c[i];
        if ch == '\\' && i + 1 < c.len() {
            o.push(ch);
            o.push(c[i + 1]);
            i += 2;
            continue;
        }
        if !sinif && ch == '(' && c.get(i + 1) == Some(&'?') {
            // (?flags) / (?:...) / (?P<ad>...) başlığını aynen kopyala
            o.push_str("(?");
            i += 2;
            while i < c.len() && (c[i].is_ascii_alphabetic() || c[i] == '-' || c[i] == '<' || c[i] == '=' || c[i] == '!') {
                o.push(c[i]);
                i += 1;
                if o.ends_with("(?P<") {
                    while i < c.len() && c[i] != '>' {
                        o.push(c[i]);
                        i += 1;
                    }
                    break;
                }
            }
            continue;
        }
        if ch == '[' && !sinif {
            sinif = true;
            o.push(ch);
            i += 1;
            if c.get(i) == Some(&'^') {
                o.push('^');
                i += 1;
            }
            if c.get(i) == Some(&']') {
                o.push(']');
                i += 1;
            }
            continue;
        }
        if ch == ']' && sinif {
            sinif = false;
        }
        if IIII.contains(ch) {
            let aralik = sinif && (c.get(i + 1) == Some(&'-') && c.get(i + 2).is_some_and(|x| *x != ']') || (i > 0 && c[i - 1] == '-'));
            if aralik {
                o.push(ch);
            } else if sinif {
                o.push_str(IIII);
            } else {
                o.push('[');
                o.push_str(IIII);
                o.push(']');
            }
        } else {
            o.push(ch);
        }
        i += 1;
    }
    o
}

pub fn tablo_oku(yol: &Path) -> Option<Vec<(String, String, String)>> {
    let t = oku_strict(yol)?;
    let mut v = vec![];
    for ham in t.split('\n') {
        let s = ham;
        if s.is_empty() || s.starts_with('#') {
            continue;
        }
        let p: Vec<&str> = s.split('\t').collect();
        if p.len() < 2 {
            continue;
        }
        v.push((p[0].to_string(), p[1].to_string(), p.get(2).unwrap_or(&"").to_string()));
    }
    Some(v)
}

fn oku_strict(yol: &Path) -> Option<String> {
    let b = std::fs::read(yol).ok()?;
    let s = String::from_utf8_lossy(&b).into_owned();
    Some(s.replace("\r\n", "\n").replace('\r', "\n"))
}

fn satirlar(repo: &Path, yol: &str) -> Option<Vec<String>> {
    let t = oku_py(&repo.join(yol))?;
    Some(t.split('\n').map(String::from).collect())
}

fn fnmatch_regex(p: &str) -> Regex {
    let mut r = String::from("(?is)^");
    let c: Vec<char> = p.chars().collect();
    let mut i = 0;
    while i < c.len() {
        match c[i] {
            '*' => r.push_str(".*"),
            '?' => r.push('.'),
            '[' => {
                if let Some(k) = c[i + 1..].iter().position(|x| *x == ']') {
                    let ic: String = c[i + 1..i + 1 + k].iter().collect();
                    let ic = if let Some(x) = ic.strip_prefix('!') { format!("^{x}") } else { ic };
                    r.push_str(&format!("[{ic}]"));
                    i += k + 1;
                } else {
                    r.push_str("\\[");
                }
            }
            ch => r.push_str(&regex::escape(&ch.to_string())),
        }
        i += 1;
    }
    r.push('$');
    Regex::new(&r).unwrap_or_else(|_| Regex::new("^$").unwrap())
}

/// Python `glob.glob(join(repo, g))` yaklaşığı (`*`, `?`, `[..]`; gizli dosyalar `*` ile eşleşmez; Windows'ta büyük/küçük harf duyarsız).
fn glob(repo: &Path, g: &str) -> Vec<PathBuf> {
    let mut adaylar = vec![repo.to_path_buf()];
    for parca in g.split(['/', '\\']).filter(|x| !x.is_empty()) {
        let mut yeni = vec![];
        for a in &adaylar {
            if parca.contains(['*', '?', '[']) {
                let re = fnmatch_regex(parca);
                if let Ok(rd) = std::fs::read_dir(a) {
                    for e in rd.flatten() {
                        let ad = e.file_name().to_string_lossy().into_owned();
                        if ad.starts_with('.') && !parca.starts_with('.') {
                            continue;
                        }
                        if re.is_match(&ad) {
                            yeni.push(a.join(ad));
                        }
                    }
                }
            } else {
                let p = a.join(parca);
                if p.exists() {
                    yeni.push(p);
                }
            }
        }
        adaylar = yeni;
    }
    adaylar
}

fn kaynak_getir(repo: &Path, kaynak: &str) -> Option<(String, String)> {
    if let Some(m) = kaynak.strip_prefix("uyari:") {
        return Some(("UYARI".into(), m.into()));
    }
    if let Some(n) = kaynak.strip_prefix("tuzuk:") {
        let l = satirlar(repo, "core/tuzuk-v0.md").unwrap_or_default();
        let on = format!("{n}. **");
        return l.iter().find(|s| s.starts_with(&on)).map(|s| (format!("core/tuzuk-v0.md m.{n}"), s.clone()));
    }
    if let Some(n) = kaynak.strip_prefix("defter:") {
        let l = satirlar(repo, "kuyruk/senaryo-defteri.md").unwrap_or_default();
        let on = format!("**Karar {n} (");
        let i = l.iter().position(|s| s.starts_with(&on))?;
        let son = (i + 4).min(l.len());
        return Some((format!("kuyruk/senaryo-defteri.md Karar {n}"), l[i..son].join("\n")));
    }
    if let Some(n) = kaynak.strip_prefix("ledger:") {
        let t = oku_strict(&repo.join("veri").join("karar-borcu.jsonl"))?;
        for ham in t.split('\n') {
            let Ok(Value::Object(r)) = serde_json::from_str::<Value>(ham) else { continue };
            if r.get("borc_id").and_then(Value::as_str) == Some(n) {
                let g = |k: &str| crate::ortak::py_str(r.get(k).unwrap_or(&json!("")));
                return Some((format!("ledger {n}"), format!("{} · durum={} · not={}", g("baslik"), g("durum"), g("not"))));
            }
        }
        return None;
    }
    if let Some(n) = kaynak.strip_prefix("pano:") {
        let l = satirlar(repo, "core/pano.md").unwrap_or_default();
        let on = format!("| {n} |");
        return l.iter().find(|s| s.starts_with(&on)).map(|s| (format!("core/pano.md {n}"), s.clone()));
    }
    if let Some(r) = kaynak.strip_prefix("son:") {
        let (g, n) = r.rsplit_once(':')?;
        let n: i64 = n.parse().ok()?;
        let adaylar = glob(repo, g);
        if adaylar.is_empty() {
            return None;
        }
        let tarih_re = Regex::new(r"(\d{4}-\d{2}-\d{2})").unwrap();
        let anahtar = |y: &PathBuf| {
            let ad = y.file_name().map(|x| x.to_string_lossy().into_owned()).unwrap_or_default();
            (tarih_re.captures(&ad).map(|c| c[1].to_string()).unwrap_or_default(), ad)
        };
        let son = adaylar.iter().max_by(|a, b| anahtar(a).cmp(&anahtar(b)))?;
        let rel = son.strip_prefix(repo).ok()?.to_string_lossy().into_owned();
        let yol = yerel_ayrac(&rel);
        let l = satirlar(repo, &yol).unwrap_or_default();
        return Some((format!("{yol}:1-{n}"), py_dilim(&l, 0, n).join("\n")));
    }
    if let Some(r) = kaynak.strip_prefix("bolum:") {
        let mut p = r.splitn(3, ':');
        let (yol, baslik, n) = (p.next()?, p.next()?, p.next()?);
        let n: usize = n.parse().ok()?;
        let l = satirlar(repo, yol).unwrap_or_default();
        for (i, s) in l.iter().enumerate() {
            if s.starts_with(baslik) {
                let son = (i + n).min(l.len());
                return Some((format!("{yol} '{baslik}'"), l[i..son].join("\n")));
            }
        }
        return None;
    }
    let m = Regex::new(r"^(.+):(\d+)-(\d+)$").unwrap().captures(kaynak)?;
    let (yol, a, b) = (m[1].to_string(), m[2].parse::<i64>().ok()?, m[3].parse::<i64>().ok()?);
    let l = satirlar(repo, &yol)?;
    Some((format!("{yol}:{a}-{b}"), py_dilim(&l, a - 1, b).join("\n")))
}

fn bayt_kes(s: &str, n: usize) -> String {
    let b = s.as_bytes();
    if b.len() <= n {
        return s.to_string();
    }
    let mut k = n;
    while !s.is_char_boundary(k) {
        k -= 1;
    }
    format!("{} …[kesildi]", &s[..k])
}

pub fn eslestir(prompt: &str, tablo: &[(String, String, String)], repo: &Path) -> Vec<Parca> {
    let mut parcalar = vec![];
    for (anahtar, kaynak, not) in tablo {
        let Ok(re) = RegexBuilder::new(&ignorecase_desen(anahtar)).case_insensitive(true).build() else { continue };
        let Some(c) = re.captures(prompt) else { continue };
        let mut kaynak = kaynak.clone();
        if kaynak.contains("{1}") {
            let Some(g1) = c.get(1) else { continue };
            kaynak = kaynak.replace("{1}", g1.as_str());
        }
        match kaynak_getir(repo, &kaynak) {
            None => parcalar.push(Parca { anahtar: anahtar.clone(), kaynak, etiket: None, metin: String::new(), not: not.clone() }),
            Some((etiket, metin)) => {
                let metin = if metin.len() > PARCA_BAYT { bayt_kes(&metin, PARCA_BAYT) } else { metin };
                parcalar.push(Parca { anahtar: anahtar.clone(), kaynak, etiket: Some(etiket), metin, not: not.clone() });
            }
        }
    }
    parcalar
}

pub fn cikti_yaz(parcalar: &[Parca]) -> (String, usize) {
    let (mut out, mut toplam, mut gorulen): (Vec<String>, usize, Vec<String>) = (vec![], 0, vec![]);
    for p in parcalar {
        let Some(et) = &p.etiket else { continue };
        if gorulen.contains(et) {
            continue;
        }
        gorulen.push(et.clone());
        let blok = format!("### [prompt-dosya] {et}\n{}\n", p.metin);
        let b = blok.len();
        if toplam + b > TOPLAM_BAYT {
            out.push(format!("### [prompt-dosya] {et} — bütçe aşımı, adres verildi, gövde basılmadı"));
            continue;
        }
        toplam += b;
        out.push(blok);
    }
    (out.join("\n"), toplam)
}

#[derive(Default, Debug, Clone)]
pub struct Bayrak {
    pub tablo: Option<String>,
    pub kuru: bool,
    pub json: bool,
}

pub fn kos(o: &Ortam, b: &Bayrak) -> Sonuc {
    let mut s = Sonuc::bos();
    let tablo_yol = b.tablo.as_ref().map(PathBuf::from).unwrap_or_else(|| o.repo.join("core").join("prompt-dosya-tablosu.tsv"));
    let girdi = match json_oku(&o.stdin_metin()) {
        Some(Value::Object(m)) => m,
        _ => Default::default(),
    };
    let prompt = girdi.get("prompt").and_then(Value::as_str).unwrap_or("").to_string();
    let oturum = girdi.get("session_id").cloned().unwrap_or(json!(""));
    if !tablo_yol.exists() || prompt.trim().is_empty() {
        return s;
    }
    let Some(tablo) = tablo_oku(&tablo_yol) else { return s };
    let parcalar = eslestir(&prompt, &tablo, &o.repo);
    let (metin, toplam) = cikti_yaz(&parcalar);
    if b.json {
        let pj: Vec<Value> = parcalar
            .iter()
            .map(|p| json!({"anahtar": p.anahtar, "kaynak": p.kaynak, "etiket": p.etiket, "metin": p.metin, "not": p.not}))
            .collect();
        s.satir(&py_dumps(&json!({"parcalar": pj, "toplam_bayt": toplam})));
    } else if !metin.is_empty() {
        s.satir(&metin);
    }
    if !parcalar.is_empty() && !b.kuru {
        let kutuk = o.repo.join("veri").join("bronz").join("prompt-dosya-olay.jsonl");
        let ts = ts_yerel();
        for p in &parcalar {
            let satir = json!({"ts": ts, "oturum": oturum, "anahtar": p.anahtar, "kaynak": p.kaynak, "etiket": p.etiket,
                "bayt": p.metin.len(), "prompt_uzunluk": prompt.chars().count()});
            let _ = ekle_satir(&kutuk, &py_dumps(&satir));
        }
    }
    s
}
