//! `skill-kapi`: stdin `anahtar=değer` → stdout hüküm. Kayıtlar `---` satırıyla ayrılırsa her kayıt için bir satır.
//! Çıkış: 0 hüküm üretildi · 2 girdi hatası (stderr). Sözleşme Lean `skillkapi` ikilisiyle aynıdır.
use std::io::Read;
use std::process::ExitCode;

fn main() -> ExitCode {
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
