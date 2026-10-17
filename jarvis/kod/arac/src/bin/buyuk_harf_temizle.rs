//! `buyuk-harf-temizle`: ince sarmalayıcı (bkz. `jarvis_arac::buyuk_harf`).
fn main() {
    let argv: Vec<String> = std::env::args_os().skip(1).map(|a| a.to_string_lossy().into_owned()).collect();
    std::process::exit(jarvis_arac::buyuk_harf::kos(&argv));
}
