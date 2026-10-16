//! `tools/paralel-kapi.py` karşılığı: koşum-önü paralellik kapısı (İB-63 PK-11). `veri/manifest/*.json` birim manifestlerini okur, her çift için
//! Bernstein koşulu + PK-1..12 kurallarıyla hüküm verir (PARALEL-SERBEST · SIRALI · RED · BEKLE), planlı birimleri dalgalara böler.
//! Çıkış: 0 RED yok · 1 manifest bütünlük hatası · 2 kullanım · 3 RED var. Manifest alanları beklenen türde değilse (liste yerine sayı gibi) Python
//! o alana dokunduğunda çöker; Rust alanı okurken çöker (bkz. rapor).
use crate::argparse::{Ayrisan, Secenek};
use crate::{py, pyjson};
use jarvis_hook::ortak::{py_dumps, py_str, py_truthy};
use regex::Regex;
use serde_json::{Map, Value, json};
use std::collections::HashMap;
use std::path::Path;
use std::process::Command;

const BELGE: &str = include_str!("belge/paralel.txt");
const ARAC: &str = "paralel-kapi";
const SURUM: &str = "0.1";
const ZORUNLU: [&str; 10] = ["birim_id", "tur", "pist", "okur", "yazar", "granul", "sira", "silver", "kanon_yuzeyi", "dis_etki"];
const TUR_ENUM: [&str; 5] = ["pipeline", "loop", "hibrit", "matris", "belirsiz"];

type Obj = Map<String, Value>;
type Sonuc<T> = Result<T, String>;

fn ayrisan() -> Ayrisan {
    Ayrisan::yeni(
        "paralel-kapi.py",
        Some(BELGE),
        vec![
            Secenek::deger(&["--repo"], "repo", None),
            Secenek::deger(&["--manifest-dizin"], "manifest_dizin", None),
            Secenek::tam(&["--kademe"], "kademe", Some("dalga genişliği tavanı (0 = sınırsız)")),
            Secenek::bayrak(&["--json"], "json", None),
            Secenek::bayrak(&["--sessiz"], "sessiz", None),
        ],
    )
}

// ---------------------------------------------------------------- yardımcılar
fn id(b: &Obj) -> &str {
    b.get("birim_id").and_then(Value::as_str).unwrap_or("")
}

fn al<'a>(b: &'a Obj, k: &str) -> Option<&'a Value> {
    b.get(k)
}

fn dogru(b: &Obj, k: &str) -> bool {
    b.get(k).is_some_and(py_truthy)
}

fn esit_metin(v: Option<&Value>, s: &str) -> bool {
    v.and_then(Value::as_str) == Some(s)
}

/// `str(b.get(k, ''))`
fn metin(b: &Obj, k: &str) -> String {
    b.get(k).map(py_str).unwrap_or_default()
}

/// Metin listesi alanı (`yazar`/`okur`); liste değilse ya da öğe metin değilse Python öğeye dokunurken çöker.
fn liste(b: &Obj, k: &str) -> Sonuc<Vec<String>> {
    match b.get(k) {
        Some(Value::Array(a)) => a.iter().map(|x| x.as_str().map(String::from).ok_or_else(|| format!("{}: `{k}` öğesi metin değil", id(b)))).collect(),
        _ => Err(format!("{}: `{k}` liste değil", id(b))),
    }
}

fn py_liste(l: &[String]) -> String {
    format!("[{}]", l.iter().map(|s| py::repr(s)).collect::<Vec<_>>().join(", "))
}

fn canli(b: &Obj) -> bool {
    metin(b, "durum").starts_with("canli")
}

fn tamamlandi(b: &Obj) -> bool {
    let d = metin(b, "durum");
    d.starts_with("tamam") || d.starts_with("kapandi")
}

// ---------------------------------------------------------------- fnmatch (Python 3.11 `fnmatch.fnmatch`)
fn normcase(s: &str) -> String {
    if cfg!(windows) { s.replace('/', "\\").to_lowercase() } else { s.to_string() }
}

/// `fnmatch.translate` karşılığı bir Rust düzenli ifadesi (tam eşleşme).
fn fn_cevir(pat: &str) -> String {
    let p: Vec<char> = pat.chars().collect();
    let n = p.len();
    let mut res = String::new();
    let mut yildiz_son = false;
    let mut i = 0;
    while i < n {
        let c = p[i];
        i += 1;
        match c {
            '*' => {
                if !yildiz_son {
                    res.push_str(".*");
                }
                yildiz_son = true;
                continue;
            }
            '?' => res.push('.'),
            '[' => {
                let mut j = i;
                if j < n && p[j] == '!' {
                    j += 1;
                }
                if j < n && p[j] == ']' {
                    j += 1;
                }
                while j < n && p[j] != ']' {
                    j += 1;
                }
                if j >= n {
                    res.push_str("\\[");
                } else {
                    let ham: String = p[i..j].iter().collect();
                    let mut stuff = if !ham.contains('-') {
                        ham.replace('\\', "\\\\")
                    } else {
                        let mut parcalar: Vec<String> = vec![];
                        let mut bas = i;
                        let mut k = if p[i] == '!' { i + 2 } else { i + 1 };
                        while let Some(q) = (k..j).find(|&q| p[q] == '-') {
                            parcalar.push(p[bas..q].iter().collect());
                            bas = q + 1;
                            k = q + 3;
                        }
                        let son: String = p[bas..j].iter().collect();
                        if !son.is_empty() {
                            parcalar.push(son);
                        } else if let Some(l) = parcalar.last_mut() {
                            l.push('-');
                        }
                        let mut k = parcalar.len();
                        while k > 1 {
                            k -= 1;
                            let onceki_son = parcalar[k - 1].chars().last().unwrap_or('\0');
                            let sonraki_ilk = parcalar[k].chars().next().unwrap_or('\0');
                            if onceki_son > sonraki_ilk {
                                let mut o: String = parcalar[k - 1].chars().collect::<Vec<_>>().split_last().map(|(_, r)| r.iter().collect()).unwrap_or_default();
                                o.push_str(&parcalar[k].chars().skip(1).collect::<String>());
                                parcalar[k - 1] = o;
                                parcalar.remove(k);
                            }
                        }
                        parcalar.iter().map(|s| s.replace('\\', "\\\\").replace('-', "\\-")).collect::<Vec<_>>().join("-")
                    };
                    stuff = stuff.chars().map(|c| if matches!(c, '&' | '~' | '|') { format!("\\{c}") } else { c.to_string() }).collect();
                    i = j + 1;
                    if stuff.is_empty() {
                        res.push_str("(?:[^\\s\\S])");
                    } else {
                        if let Some(rest) = stuff.strip_prefix('!') {
                            stuff = format!("^{rest}");
                        } else if stuff.starts_with('^') || stuff.starts_with('[') {
                            stuff = format!("\\{stuff}");
                        }
                        res.push_str(&format!("[{stuff}]"));
                    }
                }
            }
            c => res.push_str(&regex::escape(&c.to_string())),
        }
        yildiz_son = false;
    }
    format!("(?s)\\A(?:{res})\\z")
}

fn fnmatch(ad: &str, desen: &str) -> bool {
    let (a, d) = (normcase(ad), normcase(desen));
    Regex::new(&fn_cevir(&d)).map(|r| r.is_match(&a)).unwrap_or(false)
}

// ---------------------------------------------------------------- yükleme
/// Python `json.load(open(yol, encoding='utf-8'))` hatasının `str(e)` metni; başarıda değer.
fn json_yukle(yol: &str) -> Result<Value, String> {
    let bayt = match std::fs::read(yol) {
        Ok(b) => b,
        Err(e) => {
            return Err(if Path::new(yol).is_dir() {
                if cfg!(windows) { format!("[Errno 13] Permission denied: {}", py::repr(yol)) } else { format!("[Errno 21] Is a directory: {}", py::repr(yol)) }
            } else {
                e.to_string()
            });
        }
    };
    if let Some(m) = py::utf8_hata_iletisi(&bayt) {
        return Err(m);
    }
    let t = py::evrensel_satir(&String::from_utf8_lossy(&bayt));
    pyjson::coz_ileti(&t)
}

fn yukle(dizin: &str) -> Sonuc<(Vec<Obj>, Vec<String>)> {
    let mut birimler: Vec<Obj> = vec![];
    let mut hatalar: Vec<String> = vec![];
    let mut adlar: Vec<String> = std::fs::read_dir(dizin)
        .map(|rd| {
            rd.flatten()
                .map(|e| e.file_name().to_string_lossy().into_owned())
                .filter(|n| !n.starts_with('.') && if cfg!(windows) { n.to_lowercase().ends_with(".json") } else { n.ends_with(".json") })
                .collect()
        })
        .unwrap_or_default();
    adlar.sort();
    for ad in &adlar {
        let yol = py::join(dizin, ad);
        let b = match json_yukle(&yol) {
            Ok(b) => b,
            Err(e) => {
                hatalar.push(format!("{ad}: JSON okunamadı ({e})"));
                continue;
            }
        };
        let eksik: Vec<String> = match &b {
            Value::Object(o) => ZORUNLU.iter().filter(|k| !o.contains_key(**k)).map(|s| s.to_string()).collect(),
            Value::Array(a) => ZORUNLU.iter().filter(|k| !a.iter().any(|x| x.as_str() == Some(k))).map(|s| s.to_string()).collect(),
            Value::String(s) => ZORUNLU.iter().filter(|k| !s.contains(**k)).map(|s| s.to_string()).collect(),
            _ => return Err(format!("{ad}: JSON üst düzey değeri sayı/bool/null (Python: TypeError)")),
        };
        if !eksik.is_empty() {
            hatalar.push(format!("{ad}: eksik alan {}", py_liste(&eksik)));
            continue;
        }
        let Value::Object(o) = b else { return Err(format!("{ad}: nesne olmayan manifest tüm alanları içeriyor (Python: TypeError)")) };
        let Some(bid) = o.get("birim_id").and_then(Value::as_str).map(String::from) else { return Err(format!("{ad}: birim_id metin değil")) };
        if birimler.iter().any(|x| id(x) == bid) {
            hatalar.push(format!("{bid}: çift tanım"));
            continue;
        }
        birimler.push(o);
    }
    let var = |s: &Value, birimler: &[Obj]| s.as_str().is_some_and(|x| birimler.iter().any(|b| id(b) == x));
    for b in &birimler {
        for s in sira_oku(b)? {
            if !var(&s, &birimler) {
                hatalar.push(format!("{}: sira → bilinmeyen birim {}", id(b), py_str(&s)));
            }
        }
    }
    // döngü taraması (özyinelemeli DFS; `durum` sözlüğü 1 = yolda, 2 = bitti)
    let mut durum: HashMap<String, u8> = HashMap::new();
    fn dfs(u: &str, yol: &mut Vec<String>, birimler: &[Obj], durum: &mut HashMap<String, u8>, hatalar: &mut Vec<String>) -> Sonuc<()> {
        durum.insert(u.to_string(), 1);
        let b = birimler.iter().find(|b| id(b) == u).unwrap();
        for v in sira_oku(b)? {
            let Some(v) = v.as_str().filter(|x| birimler.iter().any(|b| id(b) == *x)) else { continue };
            if durum.get(v) == Some(&1) {
                let mut y = yol.clone();
                y.push(v.to_string());
                hatalar.push(format!("sira çevrimi: {}", y.join(" → ")));
                return Ok(());
            }
            if !durum.contains_key(v) {
                yol.push(v.to_string());
                dfs(v, yol, birimler, durum, hatalar)?;
                yol.pop();
            }
        }
        durum.insert(u.to_string(), 2);
        Ok(())
    }
    for b in &birimler {
        if !durum.contains_key(id(b)) {
            dfs(id(b), &mut vec![id(b).to_string()], &birimler, &mut durum, &mut hatalar)?;
        }
    }
    Ok((birimler, hatalar))
}

/// `b['sira']` öğeleri; liste değilse ya da öğe liste/nesne ise (hashlenemez) Python çöker.
fn sira_oku(b: &Obj) -> Sonuc<Vec<Value>> {
    match b.get("sira") {
        Some(Value::Array(a)) if a.iter().all(|x| !x.is_array() && !x.is_object()) => Ok(a.clone()),
        _ => Err(format!("{}: `sira` liste değil ya da öğesi hashlenemez", id(b))),
    }
}

// ---------------------------------------------------------------- çakışma / hüküm
/// Kaynak adı türü: dosya, snapshot ya da dış.
fn kaynak_ayir(k: &str) -> (String, Option<String>, &'static str) {
    if k.starts_with("git@") {
        return (k.to_string(), None, "snapshot");
    }
    if k == "web" || k == "stdin" {
        return (k.to_string(), None, "dis");
    }
    match k.split_once('#') {
        Some((d, b)) => (d.to_string(), Some(b.to_string()), "dosya"),
        None => (k.to_string(), None, "dosya"),
    }
}

/// İki kaynak adı aynı öğeye dokunuyor mu (glob iki yönlü; snapshot/dış asla).
fn kesisir(a: &str, b: &str) -> bool {
    let (da, ba, ta) = kaynak_ayir(a);
    let (db, bb, tb) = kaynak_ayir(b);
    if ta != "dosya" || tb != "dosya" {
        return false;
    }
    let pa = if da.ends_with('/') { format!("{da}*") } else { da };
    let pb = if db.ends_with('/') { format!("{db}*") } else { db };
    if !(pa == pb || fnmatch(&pa, &pb) || fnmatch(&pb, &pa)) {
        return false;
    }
    if let (Some(x), Some(y)) = (&ba, &bb)
        && !x.is_empty()
        && !y.is_empty()
        && x != y
    {
        return false;
    }
    true
}

/// Bernstein ihlal listesi: (tür, öğe_x, öğe_y).
fn cakisma(x: &Obj, y: &Obj) -> Sonuc<Vec<(&'static str, String, String)>> {
    let mut out = vec![];
    let (xy, yy, xo, yo) = (liste(x, "yazar")?, liste(y, "yazar")?, liste(x, "okur")?, liste(y, "okur")?);
    for ax in &xy {
        for ay in &yy {
            if kesisir(ax, ay) {
                out.push(("yazar∩yazar", ax.clone(), ay.clone()));
            }
        }
        for oy in &yo {
            if kesisir(ax, oy) {
                out.push(("yazar∩okur", ax.clone(), oy.clone()));
            }
        }
    }
    for ox in &xo {
        for ay in &yy {
            if kesisir(ox, ay) {
                out.push(("okur∩yazar", ox.clone(), ay.clone()));
            }
        }
    }
    Ok(out)
}

fn tuple_listesi(c: &[(&str, String, String)], en_cok: usize) -> String {
    format!("[{}]", c.iter().take(en_cok).map(|(t, a, _)| format!("({}, {})", py::repr(t), py::repr(a))).collect::<Vec<_>>().join(", "))
}

fn sira_var(x: &Obj, y: &Obj) -> Sonuc<bool> {
    let icerir = |a: &Obj, hedef: &str| -> Sonuc<bool> { Ok(sira_oku(a)?.iter().any(|s| s.as_str() == Some(hedef))) };
    Ok(icerir(x, id(y))? || icerir(y, id(x))?)
}

fn hukum(x: &Obj, y: &Obj) -> Sonuc<(&'static str, String)> {
    let sira = sira_var(x, y)?;
    if dogru(x, "kanon_yuzeyi") || dogru(y, "kanon_yuzeyi") {
        let kim: Vec<String> = [x, y].iter().filter(|b| dogru(b, "kanon_yuzeyi")).map(|b| id(b).to_string()).collect();
        if canli(x) || canli(y) {
            let c = cakisma(x, y)?;
            if !c.is_empty() {
                return Ok(("BEKLE", format!("PK-12 + PK-6: canlı kanon-yüzeyli birim {} ile çakışma {}", py_liste(&kim), tuple_listesi(&c, 3))));
            }
            return Ok(("PARALEL-SERBEST", format!("PK-6 kanon-yüzeyli {} canlı ama ayak-izi ayrık (yalnız snapshot okuma)", py_liste(&kim))));
        }
        return Ok(("SIRALI", format!("PK-6 kanon yüzeyi {} her şeyle sıralı + Salih imza hattı", py_liste(&kim))));
    }
    if esit_metin(al(x, "silver"), "yazar") && esit_metin(al(y, "silver"), "yazar") {
        return Ok(if sira {
            ("SIRALI", "PK-5 silver tek-yazar (sira kenarı var)".to_string())
        } else {
            ("RED", "PK-5 silver tek-yazar: iki silver-yazar paralel olamaz, sira kenarı yok".to_string())
        });
    }
    if dogru(x, "dislama_grubu") && al(x, "dislama_grubu") == al(y, "dislama_grubu") {
        return Ok(("SIRALI", format!("PK-7 kira: aynı dışlama grubu '{}'", metin(x, "dislama_grubu"))));
    }
    let c = cakisma(x, y)?;
    if !c.is_empty() {
        let ozet = c.iter().take(3).map(|(t, a, b)| format!("{t}: {a} ~ {b}")).collect::<Vec<_>>().join("; ") + if c.len() > 3 { " …" } else { "" };
        if sira {
            return Ok(("SIRALI", format!("PK-1 sira kenarı; çakışma {ozet}")));
        }
        if canli(x) || canli(y) {
            return Ok(("BEKLE", format!("PK-12 diğer oturumun ayak-izi: {ozet}")));
        }
        return Ok(("RED", format!("PK-1 çakışma, sira kenarı yok: {ozet} → seri koş ya da sira ekle")));
    }
    if esit_metin(al(x, "tur"), "loop") && esit_metin(al(y, "tur"), "loop") && (esit_metin(al(x, "iterasyon_ayak_izi"), "buyuyen") || esit_metin(al(y, "iterasyon_ayak_izi"), "buyuyen")) {
        return Ok(("SIRALI", "PK-10 büyüyen iterasyon ayak-izi (v0: seri)".to_string()));
    }
    if sira {
        return Ok(("SIRALI", "sira kenarı (ayak-izi ayrık olsa da beyan edilmiş sıra)".to_string()));
    }
    Ok(("PARALEL-SERBEST", "Bernstein 3/3 ∅".to_string()))
}

/// Manifestin `tur` alanını mevcut alanlardan türetir (saf; `main` çağırmaz, Python'da da çağrılmaz).
pub fn tur_turet(b: &Obj) -> String {
    let turetilen = if b.contains_key("matris") || b.keys().any(|k| k.starts_with("eksen") || k.starts_with("hucre")) {
        "matris"
    } else {
        let y1 = !matches!(b.get("tetik_turu"), None | Some(Value::Null)) && !esit_metin(b.get("tetik_turu"), "seans");
        let y3 = esit_metin(b.get("iterasyon_ayak_izi"), "sabit");
        let y2 = !matches!(b.get("dis_tavan"), None | Some(Value::Null));
        if !y1 && y3 {
            "pipeline"
        } else if y1 && !y2 && !y3 {
            "loop"
        } else if y1 && y3 {
            "hibrit"
        } else {
            "belirsiz"
        }
    };
    if dogru(b, "tur_ustyazim") && dogru(b, "tur_ustyazim_gerekce") {
        return py_str(&b["tur_ustyazim"]);
    }
    turetilen.to_string()
}

fn birim_uyarilari(b: &Obj) -> Sonuc<Vec<String>> {
    let mut u = vec![];
    if dogru(b, "tur_ustyazim") && !dogru(b, "tur_ustyazim_gerekce") {
        u.push("Karar 88 M3: tur_ustyazim var ama tur_ustyazim_gerekce boş — üstyazım yok sayıldı, türetilen tur kullanıldı".to_string());
    }
    if !b.get("tur").and_then(Value::as_str).is_some_and(|t| TUR_ENUM.contains(&t)) {
        u.push(format!("tur enum dışı: {}", b.get("tur").map(py_str).unwrap_or_else(|| "None".into())));
    }
    if dogru(b, "belirlenimsiz_girdi") && !dogru(b, "dogrulama_kapisi") {
        u.push("PK-2: belirlenimsiz girdi var, dogrulama_kapisi yok".to_string());
    }
    if dogru(b, "dis_etki") && !dogru(b, "idempotency_anahtari") {
        u.push("PK-9: dış etki var, idempotency_anahtari yok → seri-sınıf".to_string());
    }
    if esit_metin(al(b, "tur"), "loop") && !dogru(b, "durma_kosulu") {
        u.push("durma_kosulu eksik (loop için zorunlu)".to_string());
    }
    let girdi = if dogru(b, "belirlenimsiz_girdi") { b.get("belirlenimsiz_girdi").cloned().unwrap_or(Value::Null) } else { Value::Array(vec![]) };
    let icinde = match &girdi {
        Value::Array(a) => a.iter().any(|x| x.as_str() == Some("model-çıktısı")),
        Value::String(s) => s.contains("model-çıktısı"),
        Value::Object(o) => o.contains_key("model-çıktısı"),
        _ => return Err(format!("{}: belirlenimsiz_girdi sayı/bool (Python: TypeError)", id(b))),
    };
    if icinde && !dogru(b, "kapsam_beyani") {
        u.push("kapsam_beyani eksik (ajan-birim için zorunlu)".to_string());
    }
    let zorlama = b.get("zorlama_modu").cloned().unwrap_or(json!("yok"));
    if zorlama.as_str() == Some("yok") && !canli(b) {
        u.push("PK-4: zorlama_modu yok — hermetiklik varsayılıyor".to_string());
    }
    Ok(u)
}

struct Cift {
    a: String,
    b: String,
    hukum: &'static str,
    neden: String,
}

/// `(oncelik, id)` sıralama anahtarı: sayılar sayılarla, metinler metinlerle karşılaştırılır; karışık tür Python'da TypeError.
fn oncelik(b: &Obj) -> Sonuc<Result<f64, String>> {
    match b.get("oncelik") {
        None => Ok(Ok(5.0)),
        Some(Value::Number(n)) => Ok(Ok(n.as_f64().unwrap_or(5.0))),
        Some(Value::Bool(x)) => Ok(Ok(if *x { 1.0 } else { 0.0 })),
        Some(Value::String(s)) => Ok(Err(s.clone())),
        _ => Err(format!("{}: oncelik sıralanamaz (TypeError)", id(b))),
    }
}

/// Deterministik açgözlü dalga planı.
fn dalgalar(birimler: &[&Obj], ciftler: &[Cift], kademe: i128) -> Sonuc<(Vec<Value>, Vec<String>)> {
    let mut h: HashMap<(&str, &str), &str> = HashMap::new();
    for c in ciftler {
        h.insert((c.a.as_str(), c.b.as_str()), c.hukum);
        h.insert((c.b.as_str(), c.a.as_str()), c.hukum);
    }
    let planli: Vec<&Obj> = birimler.iter().copied().filter(|b| !canli(b)).collect();
    let mut bekleyen: Vec<String> = planli
        .iter()
        .filter(|b| birimler.iter().filter(|o| canli(o)).any(|o| h.get(&(id(b), id(o))) == Some(&"BEKLE")))
        .map(|b| id(b).to_string())
        .collect();
    bekleyen.sort();
    // (oncelik, id) anahtarlı kararlı sıralama
    let mut aday: Vec<&Obj> = planli.iter().copied().filter(|b| !bekleyen.iter().any(|x| x == id(b))).collect();
    let mut anahtar: Vec<(Result<f64, String>, String)> = vec![];
    for b in &aday {
        anahtar.push((oncelik(b)?, id(b).to_string()));
    }
    let karisik = anahtar.iter().any(|(o, _)| o.is_ok()) && anahtar.iter().any(|(o, _)| o.is_err());
    if karisik {
        return Err("oncelik değerleri sayı ve metin karışık (TypeError)".into());
    }
    let mut sira: Vec<usize> = (0..aday.len()).collect();
    sira.sort_by(|&i, &j| {
        let (a, b) = (&anahtar[i], &anahtar[j]);
        let o = match (&a.0, &b.0) {
            (Ok(x), Ok(y)) => x.partial_cmp(y).unwrap_or(std::cmp::Ordering::Equal),
            (Err(x), Err(y)) => x.cmp(y),
            _ => std::cmp::Ordering::Equal,
        };
        o.then_with(|| a.1.cmp(&b.1))
    });
    aday = sira.iter().map(|&i| aday[i]).collect();
    let mut yerlesti: HashMap<String, usize> = HashMap::new();
    let (mut dalga_no, mut plan) = (0usize, vec![]);
    while yerlesti.len() < aday.len() {
        dalga_no += 1;
        let mut dalga: Vec<String> = vec![];
        for b in &aday {
            let bid = id(b);
            if yerlesti.contains_key(bid) {
                continue;
            }
            let mut bekle = false;
            for s in sira_oku(b)? {
                let Some(s) = s.as_str() else { continue };
                if let Some(sb) = birimler.iter().find(|x| id(x) == s)
                    && !canli(sb)
                    && yerlesti.get(s).is_none_or(|&d| d >= dalga_no)
                {
                    bekle = true;
                }
            }
            if bekle || dalga.iter().any(|d| h.get(&(bid, d.as_str())) != Some(&"PARALEL-SERBEST")) {
                continue;
            }
            if kademe != 0 && dalga.len() as i128 >= kademe {
                continue;
            }
            dalga.push(bid.to_string());
        }
        if dalga.is_empty() {
            plan.push(json!({"dalga": dalga_no, "birimler": [], "not": "ilerleme yok — kalanlar bekleyen/çevrim"}));
            break;
        }
        for bid in &dalga {
            yerlesti.insert(bid.clone(), dalga_no);
        }
        plan.push(json!({"dalga": dalga_no, "birimler": dalga}));
    }
    Ok((plan, bekleyen))
}

fn git_head(repo: &str) -> String {
    match Command::new("git").args(["rev-parse", "--short", "HEAD"]).current_dir(repo).output() {
        Ok(o) => String::from_utf8(o.stdout).map(|s| py::strip(&py::evrensel_satir(&s)).to_string()).unwrap_or_else(|_| "?".into()),
        Err(_) => "?".into(),
    }
}

pub fn kos(argv: &[String]) -> i32 {
    match calis(argv) {
        Ok(k) => k,
        Err(e) => py::coker(&e),
    }
}

fn calis(argv: &[String]) -> Sonuc<i32> {
    let a = match ayrisan().ayristir(argv) {
        Ok(a) => a,
        Err(k) => return Ok(k),
    };
    let repo = a.metin("repo").map(String::from).unwrap_or_else(|| std::env::current_dir().map(|d| d.to_string_lossy().into_owned()).unwrap_or_default());
    let kademe = a.tam("kademe").unwrap_or(0);
    let dizin = py::join(&repo, a.metin("manifest_dizin").unwrap_or("veri/manifest"));
    if !Path::new(&dizin).is_dir() {
        py::err(&format!("HATA: manifest dizini yok: {dizin}\n"));
        return Ok(2);
    }
    let (birimler, hatalar) = yukle(&dizin)?;
    // Kapı v0.2: tamamlanan birimler dalga planından ve çakışma taramasından düşer; bütünlük denetimi tüm birimlerde kalır
    let tamam_n = birimler.iter().filter(|b| tamamlandi(b)).count();
    let aktif: Vec<&Obj> = birimler.iter().filter(|b| !tamamlandi(b)).collect();
    let mut sirali = aktif.clone();
    sirali.sort_by(|x, y| id(x).cmp(id(y)));
    let mut ciftler: Vec<Cift> = vec![];
    for i in 0..sirali.len() {
        for j in i + 1..sirali.len() {
            let (h, n) = hukum(sirali[i], sirali[j])?;
            ciftler.push(Cift { a: id(sirali[i]).into(), b: id(sirali[j]).into(), hukum: h, neden: n });
        }
    }
    let mut uyarilar = Map::new();
    let mut idler: Vec<&Obj> = birimler.iter().collect();
    idler.sort_by(|x, y| id(x).cmp(id(y)));
    for b in idler {
        let u = birim_uyarilari(b)?;
        if !u.is_empty() {
            uyarilar.insert(id(b).to_string(), json!(u));
        }
    }
    let (plan, bekleyen) = dalgalar(&aktif, &ciftler, kademe)?;
    let red = ciftler.iter().filter(|c| c.hukum == "RED").count();
    let cikis = if !hatalar.is_empty() {
        1
    } else if red > 0 {
        3
    } else {
        0
    };
    let mut sayim: Vec<(&str, usize)> = vec![];
    for c in &ciftler {
        match sayim.iter_mut().find(|(k, _)| *k == c.hukum) {
            Some(x) => x.1 += 1,
            None => sayim.push((c.hukum, 1)),
        }
    }
    let planli_n = aktif.iter().filter(|b| !canli(b)).count();
    let git = git_head(&repo);
    if a.bayrak("json") {
        let mut sayim_o = Map::new();
        for (k, n) in &sayim {
            sayim_o.insert(k.to_string(), json!(n));
        }
        let cj: Vec<Value> = ciftler.iter().map(|c| json!({"a": c.a, "b": c.b, "hukum": c.hukum, "neden": c.neden})).collect();
        let out = json!({"arac": ARAC, "surum": SURUM, "git_head": git, "cikis": cikis, "birim_n": birimler.len(), "planli_n": planli_n,
            "tamam_birim_n": tamam_n, "kademe": kademe as i64, "hukum_sayim": sayim_o, "butunluk_hatalari": hatalar, "ciftler": cj,
            "uyarilar": uyarilar, "dalgalar": plan, "bekleyen": bekleyen});
        py::print(&py_dumps(&out));
        return Ok(cikis);
    }
    if !a.bayrak("sessiz") {
        let sayim_s = format!("{{{}}}", sayim.iter().map(|(k, n)| format!("{}: {n}", py::repr(k))).collect::<Vec<_>>().join(", "));
        py::print(&format!(
            "=== paralel-kapi v{SURUM} @ {git} — {} birim ({planli_n} planlı) · kademe={} · hüküm sayımı {sayim_s}",
            birimler.len(),
            if kademe != 0 { kademe.to_string() } else { "∞".into() }
        ));
        py::print(&format!("tamam-birim düşüldü: {tamam_n}"));
        if !hatalar.is_empty() {
            py::print("BÜTÜNLÜK HATALARI:");
            for h in &hatalar {
                py::print(&format!("  - {h}"));
            }
        }
        py::print("\n## Çiftler");
        for c in &ciftler {
            py::print(&format!("  {} {} × {} — {}", py::sola_hizala(c.hukum, 16), c.a, c.b, c.neden));
        }
        if !uyarilar.is_empty() {
            py::print("\n## Birim uyarıları");
            for (k, v) in &uyarilar {
                let l: Vec<&str> = v.as_array().into_iter().flatten().filter_map(Value::as_str).collect();
                py::print(&format!("  {k}: {}", l.join(" | ")));
            }
        }
        py::print("\n## Dalga planı");
        for d in &plan {
            let bl: Vec<String> = d["birimler"].as_array().into_iter().flatten().filter_map(Value::as_str).map(String::from).collect();
            let not = d.get("not").and_then(Value::as_str).map(|n| format!(" ({n})")).unwrap_or_default();
            py::print(&format!("  dalga {}: {}{not}", d["dalga"], py_liste(&bl)));
        }
        if !bekleyen.is_empty() {
            py::print(&format!("  BEKLEYEN (PK-12): {}", py_liste(&bekleyen)));
        }
    }
    Ok(cikis)
}
