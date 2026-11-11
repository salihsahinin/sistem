//! `tools/yol-tasi.py` karşılığı: Karar 101 monorepo taşınması için yol-değiştirme aracı (F1 kuru koşum · F3 uygulama).
//! Verilen dizinlerdeki metin dosyalarında eski mutlak/tilde yolları yenileriyle değiştirir; dokümanlara (raporlar/ wiki/ ...) dokunmaz.
//! Diff `raporlar/2026-09/yol-tasi-<kuru|uygula>-<tarih>.diff` dosyasına yazılır; Friday deny satırları yalnız bayraklanır.
//! Çıkış: 0 · argparse hatası 2. Python'daki yakalanmamış istisnalar (yazma/dizin hataları) `py::coker` ile çıkış 1.
use crate::buyuk_harf::{cozumle, pathlib_metni, pathlib_sirala};
use crate::difflib;
use jarvis_rituel::argparse::{Ayrisan, Secenek};
use jarvis_rituel::py;
use regex::Regex;
use std::path::{Path, PathBuf};
use std::sync::LazyLock;

const UZANTI: [&str; 10] = [".py", ".sh", ".json", ".md", ".yaml", ".yml", ".toml", ".txt", ".d2", ".tsv"];
/// Friday deny satırı.
static BAYRAK: LazyLock<Regex> = LazyLock::new(|| Regex::new(r#""Read\(~/jarvis/[^"]*\)""#).unwrap());

/// `CIFTLER`: uzun önce (alt-dizi çakışması olmasın).
fn ciftler(home: &str) -> Vec<(String, String)> {
    let c = |a: String, b: String| (a, b);
    vec![
        c(format!("{home}/jarvis"), format!("{home}/sistem/jarvis")),
        c("$HOME/jarvis".into(), "$HOME/sistem/jarvis".into()),
        c("~/jarvis".into(), "~/sistem/jarvis".into()),
        c(format!("{home}/friday"), format!("{home}/sistem/friday")),
        c("$HOME/friday".into(), "$HOME/sistem/friday".into()),
        c("~/friday".into(), "~/sistem/friday".into()),
        c("-Users-HasanSalihSahin-jarvis".into(), "-Users-HasanSalihSahin-sistem-jarvis".into()),
        c("-Users-HasanSalihSahin-friday".into(), "-Users-HasanSalihSahin-sistem-friday".into()),
    ]
}

fn alt(taban: &Path, parcalar: &[&str]) -> PathBuf {
    parcalar.iter().fold(taban.to_path_buf(), |y, p| y.join(p))
}

fn varsayilan_tara(kok: &Path, duzen: &str, home: &str) -> Vec<PathBuf> {
    let (j, f) = if duzen == "eski" { (kok.to_path_buf(), PathBuf::from(pathlib_metni(home)).join("friday")) } else { (kok.join("jarvis"), kok.join("friday")) };
    vec![
        j.join("tools"),
        alt(&j, &[".claude", "hooks"]),
        alt(&j, &[".claude", "rules"]),
        alt(&j, &[".claude", "skills"]),
        alt(&j, &[".claude", "settings.json"]),
        j.join(".mcp.json"),
        f.join(".claude"),
        f.join("CLAUDE.md"),
        f.join("AGENTS.md"),
        f.join("tools"),
    ]
}

/// `PurePath.suffix`.
fn uzanti(ad: &str) -> &str {
    match ad.rfind('.') {
        Some(i) if i > 0 && i + 1 < ad.len() => &ad[i..],
        _ => "",
    }
}

fn yasak_parca(p: &Path) -> bool {
    p.components().any(|c| c.as_os_str() == "worktrees" || c.as_os_str() == ".git")
}

/// `sorted(y.rglob("*"))` içinden `is_file` + uzantı + `worktrees`/`.git` süzgecini geçenler (süzgeç sıralamadan bağımsızdır;
/// adı `.git`/`worktrees` olan dizinlerin altında süzgeçten geçen yol olmadığından oralara inilmez; sembolik bağ dizinlerine inilmez).
fn dizin_dosyalari(y: &Path) -> Vec<PathBuf> {
    fn gez(d: &Path, cikti: &mut Vec<PathBuf>) {
        let Ok(rd) = std::fs::read_dir(d) else { return };
        for e in rd.flatten() {
            let ad = e.file_name();
            let yol = d.join(&ad);
            if e.file_type().is_ok_and(|t| t.is_dir()) {
                if ad != ".git" && ad != "worktrees" {
                    gez(&yol, cikti);
                }
                continue;
            }
            cikti.push(yol);
        }
    }
    let mut v = vec![];
    if yasak_parca(y) {
        return v;
    }
    gez(y, &mut v);
    v.retain(|p| {
        p.is_file() && p.file_name().is_some_and(|n| UZANTI.contains(&uzanti(&n.to_string_lossy()))) && !yasak_parca(p)
    });
    pathlib_sirala(&mut v);
    v
}

/// `dosyalar(yollar)` bir yol için: dosyaysa kendisi, dizinse süzülmüş torunları.
fn yol_dosyalari(y: &Path) -> Vec<PathBuf> {
    if y.is_file() {
        vec![y.to_path_buf()]
    } else if y.is_dir() {
        dizin_dosyalari(y)
    } else {
        vec![]
    }
}

fn donustur(satir: &str, cift: &[(String, String)]) -> String {
    if satir.contains("/sistem/") || satir.contains("-sistem-") {
        return satir.to_string();
    }
    let mut s = satir.to_string();
    for (eski, yeni) in cift {
        s = s.replace(eski.as_str(), yeni);
    }
    s
}

pub fn kos(argv: &[String]) -> i32 {
    let home = py::expanduser("~");
    let ayrisan = Ayrisan::yeni(
        "yol-tasi.py",
        None,
        vec![
            Secenek::bayrak(&["--kuru"], "kuru", None),
            Secenek::bayrak(&["--uygula"], "uygula", None),
            Secenek::deger(&["--kok"], "kok", None),
            Secenek::deger(&["--duzen"], "duzen", None).secimli(&["eski", "yeni"]),
            Secenek::ekle(&["--tara"], "tara", None),
        ],
    )
    .dislayan(&["kuru", "uygula"], true);
    let a = match ayrisan.ayristir(argv) {
        Ok(a) => a,
        Err(k) => return k,
    };
    let cwd = std::env::current_dir().map(|d| d.to_string_lossy().into_owned()).unwrap_or_default();
    let kok = cozumle(Path::new(&pathlib_metni(&py::expanduser(a.metin("kok").unwrap_or(&cwd)))));
    let duzen = match a.metin("duzen") {
        Some(d) => d.to_string(),
        None => (if kok.join("jarvis").is_dir() && kok.join("friday").is_dir() { "yeni" } else { "eski" }).to_string(),
    };
    let hedefler: Vec<PathBuf> = match a.liste("tara") {
        Some(l) if !l.is_empty() => l.iter().map(|t| PathBuf::from(pathlib_metni(&py::expanduser(t)))).collect(),
        _ => varsayilan_tara(&kok, &duzen, &home),
    };
    let uygula = a.bayrak("uygula");
    let mod_adi = if uygula { "uygula" } else { "kuru" };
    let tarih = chrono::Local::now().format("%Y-%m-%d").to_string();
    let cift = ciftler(&home);
    let (mut rapor, mut diffler, mut bayraklar): (Vec<(String, usize)>, Vec<String>, Vec<String>) = (vec![], vec![], vec![]);
    for y in &hedefler {
        for p in yol_dosyalari(y) {
            let Ok(eski) = py::oku_kati(&p) else { continue };
            let ps = p.to_string_lossy().into_owned();
            let satirlar = difflib::splitlines_keepends(&eski);
            let yeni_s: Vec<String> = satirlar.iter().map(|s| donustur(s, &cift)).collect();
            for (i, s) in satirlar.iter().enumerate() {
                if BAYRAK.is_match(s) {
                    bayraklar.push(format!("{ps}:{}", i + 1));
                }
            }
            let n = satirlar.iter().zip(&yeni_s).filter(|(x, y)| x != y).count();
            if n > 0 {
                rapor.push((ps.clone(), n));
                diffler.extend(difflib::unified_diff(&satirlar, &yeni_s, &ps, &format!("{ps} (yeni)"), 3));
                if uygula
                    && let Err(e) = std::fs::write(&p, yeni_s.concat())
                {
                    return py::coker(&format!("{ps}: {e}"));
                }
            }
        }
    }
    let cikti_dir = cozumle(&alt(&if duzen == "yeni" { kok.join("jarvis") } else { kok.clone() }, &["raporlar", "2026-09"]));
    if let Err(e) = std::fs::create_dir_all(&cikti_dir) {
        return py::coker(&format!("{}: {e}", cikti_dir.display()));
    }
    let diff_yolu = cikti_dir.join(format!("yol-tasi-{mod_adi}-{tarih}.diff"));
    if let Err(e) = std::fs::write(&diff_yolu, diffler.concat()) {
        return py::coker(&format!("{}: {e}", diff_yolu.display()));
    }
    py::print(&format!("yol-tasi {mod_adi} · düzen={duzen} · kök={} · tarih={tarih}", kok.display()));
    py::print(&format!("{} değişen satır", py::sola_hizala("dosya", 70)));
    for (yol, n) in &rapor {
        py::print(&format!("{} {n}", py::sola_hizala(yol, 70)));
    }
    py::print(&format!("toplam: {} dosya · {} satır · diff → {}", rapor.len(), rapor.iter().map(|(_, n)| n).sum::<usize>(), diff_yolu.display()));
    if !bayraklar.is_empty() {
        py::print("BAYRAK (elle, F3 Edit): Friday deny satırları → tek `jarvis/**`:");
        for b in &bayraklar {
            py::print(&format!("  {b}"));
        }
    }
    0
}
