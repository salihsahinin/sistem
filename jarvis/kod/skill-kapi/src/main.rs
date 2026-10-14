//! `skill-kapi`: stdin `anahtar=değer` → stdout hüküm. Kayıtlar `---` satırıyla ayrılırsa her kayıt için bir satır.
//! Çıkış: 0 hüküm üretildi · 2 girdi hatası (stderr). Sözleşme Lean `skillkapi` ikilisiyle aynıdır.
//!
//! Alt komut: `skill-kapi denetle <skill-dizini|SKILL.md> [--json] [--repo <kök>]` (`kapi-denetim.py` karşılığı;
//! çıkış 0 geçti · 1 sert kapı düştü · 2 kullanım hatası).
use std::io::{Read, Write};
use std::process::ExitCode;

fn main() -> ExitCode {
    let argv: Vec<String> = std::env::args().skip(1).collect();
    if argv.first().map(String::as_str) == Some("denetle") {
        let (cikti, kod) = skill_kapi::denetim::denetle(&argv[1..]);
        let mut out = std::io::stdout().lock();
        let _ = out.write_all(cikti.as_bytes());
        let _ = out.flush();
        return ExitCode::from(kod as u8);
    }
    let mut girdi = String::new();
    if let Err(e) = std::io::stdin().read_to_string(&mut girdi) {
        eprintln!("HATA: stdin okunamadı: {e}");
        return ExitCode::from(2);
    }
    let girdi = girdi.replace("\r\n", "\n");
    for kayit in girdi.split("\n---\n") {
        match skill_kapi::oku(kayit) {
            Ok(a) => println!("{}", skill_kapi::hukum(&a).kod()),
            Err(e) => {
                eprintln!("HATA: {e}");
                return ExitCode::from(2);
            }
        }
    }
    ExitCode::SUCCESS
}
