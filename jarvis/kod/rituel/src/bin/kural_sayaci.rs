//! `kural-sayaci`: `tools/kural-sayaci.py` karşılığı (bkz. `jarvis_rituel::sayac`).
fn main() {
    let argv: Vec<String> = std::env::args_os().skip(1).map(|a| a.to_string_lossy().into_owned()).collect();
    std::process::exit(jarvis_rituel::sayac::kos(&argv));
}
