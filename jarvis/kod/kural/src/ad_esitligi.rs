//! `tools/ad-esitligi-denetim.py` karşılığı: ad-eşitliği denetimi (Karar 93 EK): "Carvis = Jarvis" bilgisi her bağlam kombinasyonunda bulunmalı.
//! K1 her-seans-yüklenen dosyalar · K2 dizin README/eşdeğeri · K3 canlı bağlamda bağlanmamış "Carvis". Çıkış: 0 PASS · 4 eksik var.
use crate::argparse::{Ayrisan, Secenek};
use crate::{harness_anahtar, py};
use regex::Regex;
use serde_json::{Value, json};
use std::path::Path;

const BELGE: &str = include_str!("belge/ad.txt");

fn ayrisan() -> Ayrisan {
    Ayrisan::yeni("ad-esitligi-denetim.py", Some(BELGE), vec![Secenek::bayrak(&["--json"], "json", None)])
}

/// `oku(p)`: UTF-8 katı okuma, evrensel satır sonu; her hatada boş metin.
fn oku(p: &str) -> String {
    py::oku_kati(Path::new(p)).unwrap_or_default()
}

/// `os.walk` sırası: dizinin kendi dosyaları, sonra alt dizinler (okuma sırasıyla); `atla` adları gezilmez. `ziyaret` true dönerse dur.
fn yuru(dizin: &Path, atla: &[&str], ziyaret: &mut dyn FnMut(&Path, &[String]) -> bool) -> bool {
    let Ok(rd) = std::fs::read_dir(dizin) else { return false };
    let (mut dizinler, mut dosyalar): (Vec<String>, Vec<String>) = (vec![], vec![]);
    for e in rd.flatten() {
        let ad = e.file_name().to_string_lossy().into_owned();
        if e.path().is_dir() { dizinler.push(ad) } else { dosyalar.push(ad) }
    }
    dizinler.retain(|d| !atla.contains(&d.as_str()));
    if ziyaret(dizin, &dosyalar) {
        return true;
    }
    for d in &dizinler {
        let yol = dizin.join(d);
        if yol.is_symlink() {
            continue;
        }
        if yuru(&yol, atla, ziyaret) {
            return true;
        }
    }
    false
}

pub fn kos(argv: &[String]) -> i32 {
    let a = match ayrisan().ayristir(argv) {
        Ok(a) => a,
        Err(k) => return k,
    };
    let j = harness_anahtar::jarvis();
    let ev = py::expanduser("~");
    // Python `re.I`: katlanmış metne katlanmış desen
    let esit = Regex::new(&py::katla(
        r"eski ad[ıi]? Carvis|JARVİS FRIDAY CARVIS|Carvis\s*=\s*\*{0,2}Jarvis|Carvis\s*→\s*\*{0,2}Jarvis|Carvis emekli|Carvis\)|eski ad Carvis",
    ))
    .unwrap();
    let esit_mi = |t: &str| esit.is_match(&py::katla(t));
    let carvis = Regex::new(r"Carvis|CARVİS|CARVIS").unwrap();
    let jp = |alt: &[&str]| alt.iter().fold(j.clone(), |acc, p| py::join(&acc, p));
    let mut k1: Vec<String> = vec![
        jp(&["CLAUDE.md"]),
        jp(&[".claude", "hooks", "session-start.sh"]),
        py::join(&harness_anahtar::memory_dizin(), "MEMORY.md"), // makineye göre anahtar
        py::join(&py::join(&harness_anahtar::dirname(&j), "friday"), "CLAUDE.md"), // monorepo: friday = jarvis'in kardeşi
    ];
    let ajanlar = jp(&[".claude", "agents"]);
    if Path::new(&ajanlar).is_dir() {
        let mut adlar: Vec<String> = std::fs::read_dir(&ajanlar).map(|rd| rd.flatten().map(|e| e.file_name().to_string_lossy().into_owned()).collect()).unwrap_or_default();
        adlar.sort();
        k1.extend(adlar.iter().filter(|f| f.ends_with(".md")).map(|f| py::join(&ajanlar, f)));
    }
    let (mut r1, mut r2, mut r3): (Vec<Value>, Vec<Value>, Vec<Value>) = (vec![], vec![], vec![]);
    for p in &k1 {
        let t = oku(p);
        let durum = if esit_mi(&t) { "PASS" } else if t.is_empty() { "YOK" } else { "EKSİK" };
        r1.push(json!({"yol": p.replace(&ev, "~"), "durum": durum}));
    }
    let mut adlar: Vec<String> = std::fs::read_dir(&j).map(|rd| rd.flatten().map(|e| e.file_name().to_string_lossy().into_owned()).collect()).unwrap_or_default();
    adlar.sort();
    for d in &adlar {
        let dp = py::join(&j, d);
        if !Path::new(&dp).is_dir() || (d.starts_with('.') && d != ".claude") || d == "node_modules" {
            continue;
        }
        let mut var = false;
        yuru(Path::new(&dp), &[".git", "node_modules", "__pycache__", "worktrees"], &mut |dir, dosyalar| {
            for f in dosyalar {
                if [".md", ".py", ".sh", ".json", ".html", ".txt", ".d2"].iter().any(|e| f.ends_with(e)) && carvis.is_match(&oku(&dir.join(f).to_string_lossy())) {
                    var = true;
                    break;
                }
            }
            var
        });
        if var {
            // README'siz dizinlerin gezinme eşleniği: core → CLAUDE.md · .claude → kaynak-kodu/README.md · tools → SCRIPTLER.md
            let rd = match d.as_str() {
                "core" => jp(&["CLAUDE.md"]),
                ".claude" => jp(&["kaynak-kodu", "README.md"]),
                "tools" => jp(&["tools", "SCRIPTLER.md"]),
                _ => py::join(&dp, "README.md"),
            };
            let durum = if esit_mi(&oku(&rd)) { "PASS" } else if !Path::new(&rd).exists() { "README-YOK" } else { "EKSİK" };
            let goreli = match py::relpath(&rd, &j) {
                Ok(r) => r,
                Err(e) => return py::coker(&format!("relpath: {e}")),
            };
            r2.push(json!({"dizin": d, "esdeger": goreli, "durum": durum}));
        }
    }
    let mut hedef: Vec<String> = ["CLAUDE.md", "KILAVUZ.md", "README.md", "fikir-kutusu.md"].iter().map(|f| py::join(&j, f)).collect();
    for d in ["core", ".claude", "wiki", "tools"] {
        yuru(Path::new(&py::join(&j, d)), &["__pycache__", "node_modules", "worktrees"], &mut |dir, dosyalar| {
            hedef.extend(dosyalar.iter().filter(|f| [".md", ".py", ".sh", ".json"].iter().any(|e| f.ends_with(e))).map(|f| dir.join(f).to_string_lossy().into_owned()));
            false
        });
    }
    let kendi = py::abspath(&jp(&["tools", "ad-esitligi-denetim.py"]));
    for p in &hedef {
        if py::abspath(p) == kendi {
            continue; // aracın kendi desen satırları
        }
        for (i, l) in oku(p).split('\n').enumerate() {
            if carvis.is_match(l) && !esit_mi(l) && !["sozluk.md", "baglam-anahtar-kaydi.md"].iter().any(|x| p.contains(x)) {
                let goreli = match py::relpath(p, &j) {
                    Ok(r) => r,
                    Err(e) => return py::coker(&format!("relpath: {e}")),
                };
                r3.push(json!({"yol": goreli, "satir": i + 1, "metin": py::ilk(py::strip(l), 100)}));
            }
        }
    }
    let say = |v: &[Value]| v.iter().filter(|x| x["durum"] != "PASS").count();
    let eksik = say(&r1) + say(&r2) + r3.len();
    if a.bayrak("json") {
        py::print(&py::json_girintili(&json!({"K1": r1, "K2": r2, "K3": r3})));
    } else {
        py::print("AD-EŞİTLİĞİ DENETİMİ (Karar 93 EK): Carvis = Jarvis her bağlam kombinasyonunda");
        let s = |x: &Value, k: &str| x[k].as_str().unwrap_or("").to_string();
        for x in &r1 {
            py::print(&format!("  [K1 {}] {}", py::sola_hizala(&s(x, "durum"), 6), s(x, "yol")));
        }
        for x in &r2 {
            py::print(&format!("  [K2 {}] {}/README.md", py::sola_hizala(&s(x, "durum"), 6), s(x, "dizin")));
        }
        for x in &r3 {
            py::print(&format!("  [K3 İHLAL ] {}:{}  {}", s(x, "yol"), x["satir"], s(x, "metin")));
        }
        py::print(&format!("  → eksik {eksik} ({})", if eksik == 0 { "PASS" } else { "FLAG" }));
    }
    if eksik > 0 { 4 } else { 0 }
}
