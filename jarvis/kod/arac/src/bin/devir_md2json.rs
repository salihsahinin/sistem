//! `devir-md2json`: ince sarmalayıcı (bkz. `jarvis_arac::devir_md2json`).
fn main() {
    let argv: Vec<String> = std::env::args_os().skip(1).map(|a| a.to_string_lossy().into_owned()).collect();
    std::process::exit(jarvis_arac::devir_md2json::kos(&argv));
}
