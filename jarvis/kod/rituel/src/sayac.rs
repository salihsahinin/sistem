//! `tools/kural-sayaci.py` karşılığı: EŞZAMANLI KURAL SAYISI sayacı (KB-50 (a), Karar 61: eşzamanlı kural sayısı ≤100; İB-23).
//! Kural birimi (dar, satır-grain kestirim): madde satırı ∨ kalın-başlı satır ∨ ZORUNLULUK işareti taşıyan satır; başlık/boş/tablo-ayraç sayılmaz.
//! Çıkış: 0 · 1 eşik AŞIMI · 2 dosya yok.
use crate::argparse::{Ayrisan, Secenek};
use crate::py;
use jarvis_hook::ortak::py_dumps;
use regex::Regex;
use serde_json::{Value, json};
use std::io::Write;
use std::path::Path;
use std::process::Command;

fn ayrisan() -> Ayrisan {
    Ayrisan::yeni(
        "kural-sayaci.py",
        None,
        vec![
            Secenek::deger(&["--repo"], "repo", None),
            Secenek::liste(&["--dosya"], "dosya", Some("sayılacak kural dosyaları (varsayılan CLAUDE.md)")),
            Secenek::liste(&["--skill"], "skill", Some("çağrılacak skill adları (.claude/skills/<ad>/SKILL.md eklenir)")),
            Secenek::tam(&["--esik"], "esik", Some("KB-50 (a) eşiği (deneysel m.29)")),
            Secenek::bayrak(&["--json"], "json", None),
            Secenek::bayrak(&["--kutuk"], "kutuk", None),
        ],
    )
}

struct Say {
    dosya: String,
    satir: usize,
    byte: usize,
    birim: usize,
    ornek: Vec<String>,
}

enum SayHata {
    /// `OSError`: Python `None` döndürür (dosya yok sayılır)
    Yok,
    Coker(String),
}

fn say(yol: &str, re: &Regexler) -> Result<Say, SayHata> {
    let t = match py::oku_kati(Path::new(yol)) {
        Ok(t) => t,
        Err(py::OkuHata::Io(_)) => return Err(SayHata::Yok),
        Err(py::OkuHata::Kod) => return Err(SayHata::Coker(format!("{yol}: UnicodeDecodeError"))),
    };
    let satirlar: Vec<&str> = t.split('\n').collect();
    let (mut n, mut ornek) = (0, vec![]);
    for (ln, s) in satirlar.iter().enumerate() {
        let k = py::strip(s);
        if k.is_empty() || re.baslik.is_match(s) || k.starts_with("|---") || k.starts_with("```") {
            continue;
        }
        if re.madde.is_match(s) || re.kalin.is_match(s) || re.isaret.is_match(k) {
            n += 1;
            if ornek.len() < 3 {
                ornek.push(format!("{}: {}", ln + 1, py::ilk(k, 70)));
            }
        }
    }
    let dosya = py::relpath(yol, ".").map_err(|e| SayHata::Coker(format!("relpath: {e}")))?;
    Ok(Say { dosya, satir: satirlar.len(), byte: satirlar.iter().map(|x| x.len() + 1).sum(), birim: n, ornek })
}

struct Regexler {
    isaret: Regex,
    madde: Regex,
    kalin: Regex,
    baslik: Regex,
}

pub fn kos(argv: &[String]) -> i32 {
    let a = match ayrisan().ayristir(argv) {
        Ok(a) => a,
        Err(k) => return k,
    };
    let re = Regexler {
        // Python re.I: `ı`/`İ` ile `i`/`I` denk sayılır; Rust (?i) bunu yapmadığından sınıf açık yazıldı
        isaret: Regex::new(r"(?i)(YASAK|ZORUNLU|yaln[ıiIİ]z|asla|\bher\b|≤|≥|\bm\.\d+|\bmd\.\d+|Katman-[12]|KURAL|kural)").unwrap(),
        madde: Regex::new(r"^\s*(?:[-*•]|\d+[.)])\s+\S").unwrap(),
        kalin: Regex::new(r"^\s*\*\*[^*]+\*\*").unwrap(),
        baslik: Regex::new(r"^\s*#{1,6}\s").unwrap(),
    };
    let cwd = std::env::current_dir().map(|d| d.to_string_lossy().into_owned()).unwrap_or_default();
    let repo = py::abspath(a.metin("repo").unwrap_or(&cwd));
    let esik = a.tam("esik").unwrap_or(100);
    let mut dosyalar: Vec<String> = a.liste("dosya").cloned().unwrap_or_else(|| vec!["CLAUDE.md".into()]);
    dosyalar.extend(a.liste("skill").into_iter().flatten().map(|s| format!(".claude/skills/{s}/SKILL.md")));
    let (mut sonuc, mut eksik): (Vec<Say>, Vec<String>) = (vec![], vec![]);
    for d in &dosyalar {
        match say(&py::join(&repo, d), &re) {
            Ok(r) => sonuc.push(r),
            Err(SayHata::Yok) => eksik.push(d.clone()),
            Err(SayHata::Coker(e)) => return py::coker(&e),
        }
    }
    if !eksik.is_empty() {
        py::err(&format!("[HATA] dosya yok: {}\n", eksik.join(", ")));
        return 2;
    }
    let hook = py::join(&py::join(&py::join(&repo, ".claude"), "hooks"), "session-start.sh");
    let mut hook_byte: Option<usize> = None;
    if Path::new(&hook).exists() {
        let mut c = Command::new("bash");
        c.arg(&hook).current_dir(&repo);
        hook_byte = py::calistir_zamanli(c, 20).map(|r| r.out.len());
    }
    let toplam: usize = sonuc.iter().map(|r| r.birim).sum();
    let hukum = if toplam as i128 > esik { "AŞIM" } else { "OK" };
    let ts = chrono::Local::now().format("%Y-%m-%dT%H:%M:%S%:z").to_string();
    let head = {
        let mut c = Command::new("git");
        c.args(["rev-parse", "--short", "HEAD"]).current_dir(&repo);
        match c.output() {
            Ok(o) => match String::from_utf8(o.stdout) {
                Ok(s) => py::strip(&py::evrensel_satir(&s)).to_string(),
                Err(_) => "?".to_string(),
            },
            Err(_) => "?".to_string(),
        }
    };
    let hook_json = hook_byte.map(|b| json!(b)).unwrap_or(Value::Null);
    if a.bayrak("json") {
        let dos: Vec<Value> = sonuc.iter().map(|r| json!({"dosya": r.dosya, "satir": r.satir, "byte": r.byte, "kural_birimi": r.birim, "ornek": r.ornek})).collect();
        py::print(&py::json_girintili(&json!({"ts": ts, "head": head, "dosyalar": dos, "hook_cikti_byte": hook_json, "toplam": toplam, "esik": esik as i64, "hukum": hukum})));
    } else {
        py::print(&format!(
            "kural-sayacı @ {head} · eşik {esik} (KB-50 a, m.29) · hook çıktısı {} byte",
            hook_byte.map(|b| b.to_string()).unwrap_or_else(|| "None".into())
        ));
        for r in &sonuc {
            py::print(&format!("  {} {} birim / {} satır / {} byte", py::sola_hizala(&r.dosya, 45), py::saga_hizala(&r.birim.to_string(), 4), py::saga_hizala(&r.satir.to_string(), 4), py::saga_hizala(&r.byte.to_string(), 6)));
        }
        let ek = if hukum == "OK" { String::new() } else { format!(" — KB-50 (a): kural sayısı ≤{esik}; damıtma/birleştirme gerekir") };
        py::print(&format!("  TOPLAM {toplam} → {hukum}{ek}"));
    }
    if a.bayrak("kutuk") {
        let yol = py::join(&py::join(&repo, "veri"), "kural-sayim.jsonl");
        let mut f = match std::fs::OpenOptions::new().append(true).create(true).open(&yol) {
            Ok(f) => f,
            Err(e) => return py::coker(&format!("{yol}: {e}")),
        };
        for r in &sonuc {
            let satir = json!({"ts": ts, "head": head, "dosya": r.dosya, "kural_birimi": r.birim, "satir": r.satir, "byte": r.byte,
                "esik": esik as i64, "toplam": toplam, "hukum": hukum, "hook_cikti_byte": hook_json});
            if let Err(e) = writeln!(f, "{}", py_dumps(&satir)) {
                return py::coker(&format!("{yol}: {e}"));
            }
        }
    }
    if hukum == "AŞIM" { 1 } else { 0 }
}
