//! `skill-esik`: Python karşılığı ile aynı bayrak/çıktı/çıkış kodu (bkz. `jarvis_kural::skill_esik`).
fn main() {
    let argv: Vec<String> = std::env::args_os().skip(1).map(|a| a.to_string_lossy().into_owned()).collect();
    std::process::exit(jarvis_kural::skill_esik::kos(&argv));
}
