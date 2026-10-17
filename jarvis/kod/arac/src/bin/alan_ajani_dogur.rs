//! `alan-ajani-dogur`: ince sarmalayıcı (bkz. `jarvis_arac::alan_ajani`).
fn main() {
    let argv: Vec<String> = std::env::args_os().skip(1).map(|a| a.to_string_lossy().into_owned()).collect();
    std::process::exit(jarvis_arac::alan_ajani::kos(&argv));
}
