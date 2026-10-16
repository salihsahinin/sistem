//! `sicak-katman-fifo`: `tools/sicak-katman-fifo.py` karşılığı (bkz. `jarvis_rituel::fifo`).
fn main() {
    let argv: Vec<String> = std::env::args_os().skip(1).map(|a| a.to_string_lossy().into_owned()).collect();
    std::process::exit(jarvis_rituel::fifo::kos(&argv));
}
