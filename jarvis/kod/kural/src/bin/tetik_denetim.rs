//! `tetik-denetim`: Python karşılığı ile aynı bayrak/çıktı/çıkış kodu (bkz. `jarvis_kural::tetik`).
fn main() {
    let argv: Vec<String> = std::env::args_os().skip(1).map(|a| a.to_string_lossy().into_owned()).collect();
    std::process::exit(jarvis_kural::tetik::kos(&argv));
}
