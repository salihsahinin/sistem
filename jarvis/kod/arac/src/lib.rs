//! Jarvis genel araçlarının Rust karşılığı: `tools/{alan-ajani-dogur,buyuk-harf-temizle,yol-tasi}.py` + `.claude/skills/karar-masasi/scripts/masa-uret.py`.
//! Her modül `kos(argv) -> i32` verir; `src/bin/*.rs` ikilileri ince sarmalayıcıdır. Ortak Python-taklit yardımcıları `jarvis_rituel::{py, argparse}` içindedir.
pub mod alan_ajani;
pub mod buyuk_harf;
pub mod difflib;
pub mod masa;
pub mod yol_tasi;
