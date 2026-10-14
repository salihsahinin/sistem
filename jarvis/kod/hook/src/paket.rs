//! `tools/paket-yonlendir.py` karşılığı (Karar 112 + EK-2): bağlam paketi yönlendiricisi.
//! Modlar: hook (stdin JSON -> yönerge) · `--sec` (model niyet->paket) · `--denetle` (manifest bütünlüğü).
use crate::ortak::{Ortam, Sonuc, ekle_satir, ilk_n, json_oku, oku_py, py_dilim, py_dumps, ts_yerel};
use regex::Regex;
use serde_json::{Map, Value, json};
use std::path::{Path, PathBuf};

pub const SURUM: &str = "0.2";
const KOMUTLAR: [(&str, &str); 5] = [("kapat", "kapat"), ("yok", "kapat"), ("sıfırla", "sifirla"), ("sifirla", "sifirla"), ("durum", "durum")];

#[derive(Default, Debug, Clone)]
pub struct Bayrak {
    pub manifest: Option<String>,
    pub durum_dizin: Option<String>,
    pub kuru: bool,
    pub json: bool,
    pub denetle: bool,
    pub sec: bool,
    pub niyet: Vec<String>,
    pub paket: Vec<String>,
    pub oturum: Option<String>,
    pub duzeltme: bool,
}

/// Komut satırından bayrakları ayrıştır (argparse uyumlu: `--bayrak değer` ve `--bayrak=değer`).
pub fn bayrak_oku(args: &[String]) -> Result<Bayrak, String> {
    let mut b = Bayrak::default();
    let mut i = 0;
    while i < args.len() {
        let (ad, satir_ici) = match args[i].split_once('=') {
            Some((a, v)) if a.starts_with("--") => (a.to_string(), Some(v.to_string())),
            _ => (args[i].clone(), None),
        };
        let deger = |i: &mut usize| -> Result<String, String> {
            if let Some(v) = &satir_ici {
                return Ok(v.clone());
            }
            *i += 1;
            args.get(*i).cloned().ok_or_else(|| format!("{ad}: değer gerekli"))
        };
        match ad.as_str() {
            "--repo" => {
                deger(&mut i)?;
            }
            "--manifest" => b.manifest = Some(deger(&mut i)?),
            "--durum-dizin" => b.durum_dizin = Some(deger(&mut i)?),
            "--kuru" => b.kuru = true,
            "--json" => b.json = true,
            "--denetle" => b.denetle = true,
            "--sec" => b.sec = true,
            "--niyet" => b.niyet.push(deger(&mut i)?),
            "--paket" => b.paket.push(deger(&mut i)?),
            "--oturum" => b.oturum = Some(deger(&mut i)?),
            "--duzeltme" => b.duzeltme = true,
            diger => return Err(format!("tanınmayan bayrak: {diger}")),
        }
        i += 1;
    }
    Ok(b)
}

pub fn katla(m: &str) -> String {
    m.replace('İ', "i").replace('I', "ı").to_lowercase()
}

/// `ara(desen, metin, bastan)`: önce Türkçe katlama, sonra düz lower(); eşleşen metni verir. Derlenemeyen desen -> None.
fn ara(desen: &str, metin: &str, bastan: bool) -> Option<Vec<Option<String>>> {
    if desen.is_empty() {
        return None; // (?!) yedeği: asla eşleşmez
    }
    let re = Regex::new(desen).ok()?;
    for k in [katla(metin), metin.to_lowercase()] {
        if let Some(c) = re.captures(&k)
            && (!bastan || c.get(0).unwrap().start() == 0)
        {
            return Some(c.iter().map(|g| g.map(|x| x.as_str().to_string())).collect());
        }
    }
    None
}

fn s_(v: &Value) -> &str {
    v.as_str().unwrap_or("")
}

/// 'yol' ya da 'yol:a-b' -> bayt (dosya yoksa None).
pub fn adres_coz(repo: &Path, adres: &str) -> Option<usize> {
    let re = Regex::new(r"^(.+):(\d+)-(\d+)$").unwrap();
    let (yol, aralik) = match re.captures(adres) {
        Some(c) => (c[1].to_string(), Some((c[2].parse::<i64>().unwrap_or(0), c[3].parse::<i64>().unwrap_or(0)))),
        None => (adres.to_string(), None),
    };
    let tam: PathBuf = repo.join(&yol);
    if !tam.is_file() {
        return None;
    }
    match aralik {
        None => std::fs::metadata(&tam).ok().map(|m| m.len() as usize),
        Some((a, b)) => {
            let t = oku_py(&tam)?;
            let l: Vec<String> = t.split('\n').map(String::from).collect();
            Some(py_dilim(&l, a - 1, b).join("\n").len())
        }
    }
}

/// Python `repr(str)`.
pub fn py_repr(s: &str) -> String {
    let tirnak = if s.contains('\'') && !s.contains('"') { '"' } else { '\'' };
    let mut o = String::new();
    o.push(tirnak);
    for c in s.chars() {
        match c {
            '\\' => o.push_str("\\\\"),
            '\n' => o.push_str("\\n"),
            '\r' => o.push_str("\\r"),
            '\t' => o.push_str("\\t"),
            c if c == tirnak => {
                o.push('\\');
                o.push(c);
            }
            c if (c as u32) < 0x20 || c as u32 == 0x7f => o.push_str(&format!("\\x{:02x}", c as u32)),
            c => o.push(c),
        }
    }
    o.push(tirnak);
    o
}

pub fn denetle(man: &Value, repo: &Path) -> Vec<String> {
    let mut ihlal = vec![];
    let mut gorulen: Vec<String> = vec![];
    let kademeler = man.get("kademeler").and_then(Value::as_object).cloned().unwrap_or_default();
    for ad in ["agir_is", "oncelik"] {
        let d = man.get(ad).map(s_).unwrap_or("");
        if let Err(e) = Regex::new(d) {
            ihlal.push(format!("{ad}: regex bozuk ({e})"));
        }
    }
    let id_re = Regex::new(r"^[a-zçğıöşü-]+$").unwrap();
    let butce = man.get("butce_bayt").and_then(Value::as_u64).unwrap_or(0) as usize;
    for p in man.get("paketler").and_then(Value::as_array).cloned().unwrap_or_default() {
        let pid = p.get("id").map(s_).unwrap_or("").to_string();
        if !id_re.is_match(&pid) {
            ihlal.push(format!("{}: id küçük harf/tire olmalı", py_repr(&pid)));
        }
        if gorulen.contains(&pid) || KOMUTLAR.iter().any(|(k, _)| *k == pid) || pid == "paket" {
            ihlal.push(format!("{pid}: id çakışması"));
        }
        gorulen.push(pid.clone());
        let kad = p.get("kademe").map(s_).unwrap_or("");
        if !kademeler.contains_key(kad) {
            ihlal.push(format!("{pid}: kademe tanımsız ({kad})"));
        }
        for t in p.get("tetik").and_then(Value::as_array).cloned().unwrap_or_default() {
            let t = s_(&t).to_string();
            if let Err(e) = Regex::new(&t) {
                ihlal.push(format!("{pid}: tetik regex bozuk {} ({e})", py_repr(&t)));
            }
            if t != katla(&t) {
                ihlal.push(format!("{pid}: tetik küçük harfli olmalı {}", py_repr(&t)));
            }
        }
        let mut toplam = 0;
        for a in p.get("cekirdek").and_then(Value::as_array).cloned().unwrap_or_default() {
            match adres_coz(repo, s_(&a)) {
                None => ihlal.push(format!("{pid}: çekirdek adresi kırık {}", s_(&a))),
                Some(b) => toplam += b,
            }
        }
        if toplam > butce {
            ihlal.push(format!("{pid}: çekirdek {toplam} B > bütçe {butce} B"));
        }
        for a in p.get("pointer").and_then(Value::as_array).cloned().unwrap_or_default() {
            if adres_coz(repo, s_(&a)).is_none() {
                ihlal.push(format!("{pid}: pointer kırık {}", s_(&a)));
            }
        }
    }
    ihlal
}

#[derive(Debug, Clone)]
pub struct Karar {
    pub kural: &'static str,
    pub komut: Option<&'static str>,
    pub paket: Option<String>,
    pub onceki: Option<String>,
    pub tutan: Vec<String>,
}

fn aktif_paket(durum: &Value, man: &Value) -> Option<String> {
    let a = durum.get("aktif").and_then(Value::as_str)?;
    man.get("paketler")?.as_array()?.iter().any(|p| s_(&p["id"]) == a).then(|| a.to_string())
}

pub fn yonlendir(prompt: &str, man: &Value, durum: &Value) -> Karar {
    let aktif = aktif_paket(durum, man);
    if let Some(g) = ara(r"^\s*paket\s*:\s*([a-zçğıöşü]+)", prompt, true) {
        let k = g[1].clone().unwrap_or_default();
        if let Some((_, v)) = KOMUTLAR.iter().find(|(a, _)| *a == k) {
            return Karar { kural: "k", komut: Some(v), paket: aktif.clone(), onceki: aktif, tutan: vec![] };
        }
    }
    if let Some(g) = ara(r"^\s*([a-zçğıöşü-]+)\s*:", prompt, true) {
        let k = g[1].clone().unwrap_or_default();
        let var = man.get("paketler").and_then(Value::as_array).is_some_and(|ps| ps.iter().any(|p| s_(&p["id"]) == k));
        if var {
            return Karar { kural: "a", komut: None, paket: Some(k.clone()), onceki: aktif, tutan: vec![format!("{k}:")] };
        }
    }
    Karar { kural: "d", komut: None, paket: None, onceki: aktif, tutan: vec![] }
}

#[derive(Debug, Clone, PartialEq)]
pub struct Durum {
    pub aktif: Option<String>,
    pub yuklu: Vec<String>,
    pub gecis: i64,
}

impl Durum {
    pub fn json(&self) -> Value {
        json!({"aktif": self.aktif, "yuklu": self.yuklu, "gecis": self.gecis})
    }
    fn oku(v: &Value) -> Durum {
        Durum {
            aktif: v.get("aktif").and_then(Value::as_str).map(String::from),
            yuklu: v.get("yuklu").and_then(Value::as_array).map(|a| a.iter().map(|x| s_(x).to_string()).collect()).unwrap_or_default(),
            gecis: v.get("gecis").and_then(Value::as_i64).unwrap_or(0),
        }
    }
}

type Olay = Map<String, Value>;

fn kademe_ad(man: &Value, k: &str) -> String {
    man["kademeler"].get(k).and_then(Value::as_str).unwrap_or(k).to_string()
}

pub fn uygula(karar: &Karar, prompt: &str, man: &Value, durum: &Durum, repo: &Path, ek: bool) -> (Durum, String, Option<Olay>) {
    let mut yeni = durum.clone();
    let kapsul_dizin = man.get("kapsul_dizin").and_then(Value::as_str).unwrap_or("core/paket-kapsul").to_string();
    let esik = man.get("esik_gecis").and_then(Value::as_i64).unwrap_or(3);
    if karar.kural == "d" {
        return (yeni, String::new(), None);
    }
    if karar.kural == "k" {
        let komut = karar.komut.unwrap_or("");
        let onceki = karar.onceki.clone();
        let metin;
        if komut == "durum" {
            let y = if yeni.yuklu.is_empty() { "yok".to_string() } else { yeni.yuklu.join(", ") };
            metin = format!("### [paket] durum: aktif {} · yüklü {y} · geçiş {}/{esik}", onceki.clone().unwrap_or("yok".into()), yeni.gecis);
        } else if komut == "kapat" {
            yeni.aktif = None;
            let mut m = "### [paket] kapatıldı: genel sohbet (yalnız çekirdek).".to_string();
            if let Some(o) = &onceki {
                m += &format!(" Önce çıkan paketin kapsülünü yaz → {kapsul_dizin}/{o}.md");
            }
            metin = m;
        } else {
            yeni = Durum { aktif: None, yuklu: vec![], gecis: 0 };
            metin = "### [paket] sıfırlandı: aktif yok, yüklü yok, geçiş 0 (pencere temizliği ya da sıkıştırma sonrası).".into();
        }
        let mut o = Olay::new();
        o.insert("kural".into(), json!("k"));
        o.insert("paket".into(), Value::Null);
        o.insert("onceki".into(), json!(onceki));
        o.insert("komut".into(), json!(komut));
        return (yeni, metin, Some(o));
    }
    let pid = karar.paket.clone().unwrap_or_default();
    let onceki = karar.onceki.clone();
    let p = man["paketler"].as_array().unwrap().iter().find(|x| s_(&x["id"]) == pid).unwrap().clone();
    let agir = ara(man.get("agir_is").map(s_).unwrap_or(""), prompt, false).and_then(|g| g[0].clone());
    let oncelik = ara(man.get("oncelik").map(s_).unwrap_or(""), prompt, false).and_then(|g| g[0].clone());
    let kademe = if oncelik.is_some() { "fable".to_string() } else { s_(&p["kademe"]).to_string() };
    let kad_ad = kademe_ad(man, &kademe);
    let ayrim = if agir.is_some() { "alt-ajan" } else { "ayni-pencere" };
    let degisti = ek || Some(&pid) != onceki.as_ref();
    let ilk = !yeni.yuklu.contains(&pid);
    if !ek {
        if degisti && onceki.is_some() {
            yeni.gecis += 1;
        }
        yeni.aktif = Some(pid.clone());
    }
    let mut cekirdek_bayt = 0usize;
    let metin = if !degisti {
        let mut m = format!("### [paket] {pid} (aktif; kural {}) · alt-ajan kademesi {kad_ad}", karar.kural);
        if let Some(o) = &oncelik {
            m += &format!(" (öncelik beyanı: \"{o}\")");
        }
        if let Some(a) = &agir {
            m += &format!(" · ağır iş (\"{a}\"): alt-ajana ver, `model: {kademe}`, paket adreslerini emre koy, ana pencereye ≤2k özet");
        }
        m
    } else {
        let neden = match karar.kural {
            "a" => "açık önek".to_string(),
            "m" => format!("niyet: {}", karar.tutan.join(" | ")),
            k => k.to_string(),
        };
        let mut s = vec![format!("### [paket] {pid} · {} ({}kural {}: {neden})", p.get("ad").map(s_).unwrap_or(""), if ek { "ek yükleme · " } else { "" }, karar.kural)];
        let mut km = format!("- alt-ajan kademesi: {kad_ad}");
        if let Some(o) = &oncelik {
            km += &format!(" (öncelik beyanı: \"{o}\"; paket varsayılanı {})", kademe_ad(man, s_(&p["kademe"])));
        }
        km += &format!(": yalnız alt-ajana giden işte `model: {kademe}`. Oturum modelini Salih seçer, hatırlatma yapılmaz.");
        s.push(km);
        if let Some(a) = &agir {
            s.push(format!("- ayrım: alt-ajan (ağır iş sözcüğü \"{a}\"): paket adreslerini alt-ajan emrine koy, ana pencereye ≤2k özet dönsün."));
        } else {
            s.push("- ayrım: aynı pencere.".into());
        }
        let mut adresler = vec![];
        let cek: Vec<String> = p.get("cekirdek").and_then(Value::as_array).map(|a| a.iter().map(|x| s_(x).to_string()).collect()).unwrap_or_default();
        for a in &cek {
            let bayt = adres_coz(repo, a);
            cekirdek_bayt += bayt.unwrap_or(0);
            adresler.push(if bayt.is_some() { a.clone() } else { format!("{a} [kırık]") });
        }
        if adresler.is_empty() {
            s.push("- oku: çekirdek dosya yok; pointer'dan adresle ilerle.".into());
        } else if ilk {
            s.push(format!("- oku (ilk yükleme, {cekirdek_bayt} B, cevaptan önce Read ile): {}", adresler.join(" · ")));
        } else {
            s.push(format!("- oku: çekirdek bu oturumda yüklendi ({}); pencerede yoksa yeniden oku.", adresler.join(" · ")));
        }
        let liste = |k: &str| -> Vec<String> { p.get(k).and_then(Value::as_array).map(|a| a.iter().map(|x| s_(x).to_string()).collect()).unwrap_or_default() };
        if !liste("pointer").is_empty() {
            s.push(format!("- pointer (gerekince): {}", liste("pointer").join(" · ")));
        }
        if !liste("skill").is_empty() {
            s.push(format!("- ilgili skill: {}", liste("skill").join(" · ")));
        }
        let kapsul = format!("{kapsul_dizin}/{pid}.md");
        if repo.join(&kapsul).is_file() {
            s.push(format!("- konu kapsülü var, oku: {kapsul}"));
        }
        if let (Some(o), false) = (&onceki, ek) {
            s.push(format!("- geçiş {}/{esik}: önce çıkan paketin kapsülünü yaz (nerede kaldık · sıradaki adım) → {kapsul_dizin}/{o}.md", yeni.gecis));
        }
        if yeni.gecis >= esik && !ek {
            s.push(format!("- [eşik] {} geçiş: açık kapsülleri yaz, Salih'e pencere temizliği (/clear) öner; temizlikten sonra 'paket: sıfırla'.", yeni.gecis));
        }
        if ilk {
            yeni.yuklu.push(pid.clone());
        }
        s.join("\n")
    };
    let mut o = Olay::new();
    o.insert("kural".into(), json!(karar.kural));
    o.insert("paket".into(), json!(pid));
    o.insert("onceki".into(), json!(onceki));
    o.insert("gecis".into(), json!(yeni.gecis));
    o.insert("ilk_yukleme".into(), json!(degisti && ilk));
    o.insert("cekirdek_bayt".into(), json!(cekirdek_bayt));
    o.insert("kademe".into(), json!(kademe));
    o.insert("ayrim".into(), json!(ayrim));
    o.insert("tutan".into(), json!(karar.tutan));
    (yeni, metin, Some(o))
}

pub fn sec(niyetler: &[(String, String)], man: &Value, durum: &Durum, repo: &Path) -> Result<(Durum, String, Vec<Olay>), String> {
    let paketler: Vec<String> = man.get("paketler").and_then(Value::as_array).map(|a| a.iter().map(|p| s_(&p["id"]).to_string()).collect()).unwrap_or_default();
    for (_, pid) in niyetler {
        if pid != "yok" && !paketler.contains(pid) {
            return Err(format!("bilinmeyen paket: {pid} (geçerli: {} · yok)", paketler.join(", ")));
        }
    }
    let mut sira: Vec<String> = vec![];
    for (_, pid) in niyetler {
        if pid != "yok" && !sira.contains(pid) {
            sira.push(pid.clone());
        }
    }
    let tavan = man.get("tavan_paket").and_then(Value::as_i64).unwrap_or(2);
    if sira.len() as i64 > tavan {
        return Err(format!("mesaj başına en çok {tavan} farklı paket; seçilen {}: {}", sira.len(), sira.join(", ")));
    }
    let aktif = aktif_paket(&durum.json(), man);
    let mut yeni = Durum { aktif: aktif.clone(), yuklu: durum.yuklu.clone(), gecis: durum.gecis };
    let (mut metinler, mut satirlar): (Vec<String>, Vec<Olay>) = (vec![], vec![]);
    for (k, pid) in sira.iter().enumerate() {
        let parca: Vec<&String> = niyetler.iter().filter(|(_, q)| q == pid).map(|(n, _)| n).collect();
        let karar = Karar { kural: "m", komut: None, paket: Some(pid.clone()), onceki: yeni.aktif.clone(), tutan: parca.iter().map(|n| ilk_n(n, 60)).collect() };
        let birlesik = parca.iter().map(|s| s.as_str()).collect::<Vec<_>>().join(" ");
        let (y, metin, olay) = uygula(&karar, &birlesik, man, &yeni, repo, k > 0);
        yeni = y;
        if !metin.is_empty() {
            metinler.push(metin);
        }
        if let Some(olay) = olay {
            for n in &parca {
                let mut r = olay.clone();
                r.insert("niyet".into(), json!(ilk_n(n, 160)));
                r.insert("ek".into(), json!(k > 0));
                satirlar.push(r);
            }
        }
    }
    for (n, q) in niyetler {
        if q == "yok" {
            let mut r = Olay::new();
            r.insert("kural".into(), json!("m"));
            r.insert("paket".into(), Value::Null);
            r.insert("onceki".into(), json!(aktif));
            r.insert("niyet".into(), json!(ilk_n(n, 160)));
            satirlar.push(r);
        }
    }
    if sira.is_empty() {
        metinler.push("### [paket] yok: genel sohbet (yalnız çekirdek); aktif paket değişmedi.".into());
    } else {
        let etiket: Vec<String> = sira
            .iter()
            .map(|pid| {
                let n: Vec<String> = niyetler.iter().filter(|(_, q)| q == pid).map(|(n, _)| ilk_n(n, 40)).collect();
                format!("{pid} ← {}", n.join(" | "))
            })
            .collect();
        metinler.push(format!("- Salih'e görünür etiket: cevabın son satırına aynen yaz → `[paket] {}`", etiket.join(" · ")));
    }
    Ok((yeni, metinler.join("\n"), satirlar))
}

fn kutuge_yaz(repo: &Path, oturum: &str, satirlar: &[Olay], ek_alan: Option<&Olay>) {
    let ts = ts_yerel();
    for olay in satirlar {
        let mut m = Olay::new();
        m.insert("ts".into(), json!(ts));
        m.insert("oturum".into(), json!(oturum));
        for (k, v) in olay {
            m.insert(k.clone(), v.clone());
        }
        if let Some(e) = ek_alan {
            for (k, v) in e {
                m.insert(k.clone(), v.clone());
            }
        }
        let _ = ekle_satir(&repo.join("veri").join("bronz").join("paket-olay.jsonl"), &py_dumps(&Value::Object(m)));
    }
}

fn temiz_oturum(s: &str) -> String {
    let t: String = s.chars().filter(|c| c.is_ascii_alphanumeric() || *c == '_' || *c == '-').collect();
    if t.is_empty() { "oturumsuz".into() } else { t }
}

fn manifest_oku(yol: &Path) -> Result<Value, String> {
    let b = std::fs::read(yol).map_err(|e| {
        if e.kind() == std::io::ErrorKind::NotFound {
            format!("[Errno 2] No such file or directory: '{}'", yol.to_string_lossy())
        } else {
            e.to_string()
        }
    })?;
    serde_json::from_slice(&b).map_err(|e| e.to_string())
}

pub fn kos(o: &Ortam, b: &Bayrak) -> Sonuc {
    let mut s = Sonuc::bos();
    let man_yol = b.manifest.as_ref().map(PathBuf::from).unwrap_or_else(|| o.repo.join("core").join("baglam-paketleri.json"));
    if b.denetle {
        let man = match manifest_oku(&man_yol) {
            Ok(m) => m,
            Err(e) => {
                s.hata = format!("HATA: manifest okunamadı: {} ({e})\n", man_yol.display());
                s.kod = 2;
                return s;
            }
        };
        let ihlal = denetle(&man, &o.repo);
        let n = man.get("paketler").and_then(Value::as_array).map(Vec::len).unwrap_or(0);
        if b.json {
            s.satir(&py_dumps(&json!({"arac": "paket-yonlendir", "surum": SURUM, "cikis": if ihlal.is_empty() {0} else {1}, "paket_n": n, "ihlal": ihlal})));
        } else {
            for i in &ihlal {
                s.satir(&format!("İHLAL {i}"));
            }
            s.satir(&format!("paket {n} · ihlal {}", ihlal.len()));
        }
        s.kod = if ihlal.is_empty() { 0 } else { 1 };
        return s;
    }
    let durum_dizin = b.durum_dizin.as_ref().map(PathBuf::from).unwrap_or_else(|| o.repo.join(".claude").join("hooks").join("state"));
    if b.sec {
        if b.niyet.is_empty() || b.niyet.len() != b.paket.len() {
            s.hata = "HATA: --sec için eşit sayıda --niyet ve --paket gerekli\n".into();
            s.kod = 2;
            return s;
        }
        let man = match manifest_oku(&man_yol) {
            Ok(m) => m,
            Err(e) => {
                s.hata = format!("HATA: manifest okunamadı: {} ({e})\n", man_yol.display());
                s.kod = 2;
                return s;
            }
        };
        let oturum = match &b.oturum {
            Some(x) if !x.is_empty() => x.clone(),
            _ => std::fs::read_to_string(durum_dizin.join("son-oturum.txt")).map(|t| t.trim().to_string()).unwrap_or_default(),
        };
        let oturum = temiz_oturum(&oturum);
        let durum_yol = durum_dizin.join(format!("paket-{oturum}.json"));
        let durum_v = std::fs::read_to_string(&durum_yol).ok().and_then(|t| json_oku(&t)).unwrap_or(json!({}));
        let durum = Durum::oku(&durum_v);
        let ciftler: Vec<(String, String)> = b.niyet.iter().cloned().zip(b.paket.iter().cloned()).collect();
        let (yeni, metin, mut satirlar) = match sec(&ciftler, &man, &durum, &o.repo) {
            Ok(x) => x,
            Err(e) => {
                s.hata = format!("HATA: {e}\n");
                s.kod = 1;
                return s;
            }
        };
        if b.duzeltme {
            for r in satirlar.iter_mut() {
                r.insert("duzeltme".into(), json!(true));
            }
        }
        if b.json {
            let kutuk: Vec<Value> = satirlar.iter().cloned().map(Value::Object).collect();
            s.satir(&py_dumps(&json!({"arac": "paket-yonlendir", "surum": SURUM, "cikis": 0, "durum": yeni.json(), "metin": metin, "kutuk": kutuk})));
        } else {
            s.satir(&metin);
        }
        if !b.kuru {
            let _ = std::fs::create_dir_all(&durum_dizin);
            let _ = std::fs::write(&durum_yol, py_dumps(&yeni.json()));
            kutuge_yaz(&o.repo, &oturum, &satirlar, None);
        }
        return s;
    }
    // hook modu
    let metin_in = o.stdin_metin();
    let Some(girdi) = json_oku(if metin_in.is_empty() { "{}" } else { &metin_in }) else { return s };
    let Ok(man) = manifest_oku(&man_yol) else { return s };
    let prompt = girdi.get("prompt").and_then(Value::as_str).unwrap_or("").to_string();
    let oturum = temiz_oturum(girdi.get("session_id").and_then(Value::as_str).unwrap_or(""));
    if !b.kuru && oturum != "oturumsuz" {
        let _ = std::fs::create_dir_all(&durum_dizin);
        let _ = std::fs::write(durum_dizin.join("son-oturum.txt"), &oturum);
    }
    if prompt.trim().is_empty() {
        return s;
    }
    let durum_yol = durum_dizin.join(format!("paket-{oturum}.json"));
    let durum = Durum::oku(&std::fs::read_to_string(&durum_yol).ok().and_then(|t| json_oku(&t)).unwrap_or(json!({})));
    let karar = yonlendir(&prompt, &man, &durum.json());
    let (yeni, metin, olay) = uygula(&karar, &prompt, &man, &durum, &o.repo, false);
    if b.json {
        let mut kj = Olay::new();
        kj.insert("kural".into(), json!(karar.kural));
        if let Some(c) = karar.komut {
            kj.insert("komut".into(), json!(c));
        }
        kj.insert("paket".into(), json!(karar.paket));
        kj.insert("onceki".into(), json!(karar.onceki));
        kj.insert("tutan".into(), json!(karar.tutan));
        let kj = Value::Object(kj);
        s.satir(&py_dumps(&json!({"arac": "paket-yonlendir", "surum": SURUM, "cikis": 0, "karar": kj, "durum": yeni.json(), "metin": metin})));
    } else if !metin.is_empty() {
        s.satir(&metin);
    }
    if let (Some(olay), false) = (olay, b.kuru) {
        let _ = std::fs::create_dir_all(&durum_dizin);
        let _ = std::fs::write(&durum_yol, py_dumps(&yeni.json()));
        let mut ek = Olay::new();
        ek.insert("prompt_uzunluk".into(), json!(prompt.chars().count()));
        kutuge_yaz(&o.repo, &oturum, &[olay], Some(&ek));
    }
    s
}
