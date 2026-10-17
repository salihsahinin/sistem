//! `bayat-cekim`: ince sarmalayıcı (bkz. `jarvis_rituel::bayat_cekim`).
fn main() {
    let argv: Vec<String> = std::env::args_os().skip(1).map(|a| a.to_string_lossy().into_owned()).collect();
    std::process::exit(jarvis_rituel::bayat_cekim::kos(&argv));
}
