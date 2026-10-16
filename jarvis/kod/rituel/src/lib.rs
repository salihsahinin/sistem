//! Jarvis ritüel araçlarının Rust karşılığı: `tools/{acilis-kapilari,sicak-katman-fifo,hafiza-ayna,kural-sayaci}.py` + `tools/harness_anahtar.py`.
//! Her modül `kos(argv) -> i32` verir; `src/bin/*.rs` ikilileri ince sarmalayıcıdır. Bayraklar, stdout/stderr metni ve çıkış kodları Python ile eşittir
//! (fark testi: `tests/rituel_fark.rs`; bilinçli ayrışmalar `jarvis/raporlar/2026-10-16-rust-parti-2-omp.md` içinde).
pub mod acilis;
pub mod argparse;
pub mod ayna;
pub mod fifo;
pub mod harness_anahtar;
pub mod py;
pub mod sayac;
