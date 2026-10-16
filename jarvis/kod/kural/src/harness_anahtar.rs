//! `tools/harness_anahtar.py` karşılığı: Claude Code harness proje anahtarını makineye göre türetir.
//! Python betiğe göreli çözer (`tools/..`); Rust ikilisinin betik konumu yoktur: jarvis dizini `CLAUDE_PROJECT_DIR`, yoksa çalışma dizinidir
//! (hook crate'indeki kök seçimiyle aynı kural).
use crate::py;
use std::path::Path;

/// Jarvis dizini (Python: `JARVIS`).
pub fn jarvis() -> String {
    let ham = std::env::var("CLAUDE_PROJECT_DIR").ok().filter(|v| !v.is_empty()).unwrap_or_else(|| std::env::current_dir().map(|d| d.to_string_lossy().into_owned()).unwrap_or_default());
    py::abspath(&ham)
}

/// `os.path.dirname`.
pub fn dirname(p: &str) -> String {
    let (surucu, geri) = py::splitdrive(p);
    let ayrac = |c: char| c == '/' || (cfg!(windows) && c == '\\');
    let i = geri.char_indices().rev().find(|(_, c)| ayrac(*c)).map(|(i, c)| i + c.len_utf8()).unwrap_or(0);
    let bas = &geri[..i];
    let kes = bas.trim_end_matches(ayrac);
    format!("{surucu}{}", if kes.is_empty() { bas } else { kes })
}

/// Depo kökü (Python: `KOK`).
pub fn kok() -> String {
    dirname(&jarvis())
}

/// `~/.claude/projects` (Python: `PROJELER`).
pub fn projeler() -> String {
    py::join(&py::join(&py::expanduser("~"), ".claude"), "projects")
}

/// Mutlak yol -> harness proje anahtarı: alfanümerik olmayan her karakter `-` olur.
pub fn anahtar(yol: &str) -> String {
    py::abspath(yol).chars().map(|c| if c.is_ascii_alphanumeric() { c } else { '-' }).collect()
}

pub fn jarvis_anahtar() -> String {
    anahtar(&jarvis())
}

pub fn kok_anahtar() -> String {
    anahtar(&kok())
}

/// Oto-hafıza dizini: kök anahtarı; yoksa jarvis anahtarı (eski Mac düzeni).
pub fn memory_dizin() -> String {
    for a in [kok_anahtar(), jarvis_anahtar()] {
        let y = py::join(&py::join(&projeler(), &a), "memory");
        if Path::new(&y).is_dir() {
            return y;
        }
    }
    py::join(&py::join(&projeler(), &kok_anahtar()), "memory")
}
