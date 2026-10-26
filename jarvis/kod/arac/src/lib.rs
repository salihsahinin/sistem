//! Jarvis genel araçlarının Rust karşılığı: `tools/{alan-ajani-dogur,buyuk-harf-temizle,yol-tasi}.py` + `.claude/skills/karar-masasi/scripts/masa-uret.py` (parti 2: `devir-md2json` · `kod-orani-olcum`).
//! Her modül `kos(argv) -> i32` verir; `src/bin/*.rs` ikilileri ince sarmalayıcıdır. Ortak Python-taklit yardımcıları `jarvis_rituel::{py, argparse}` içindedir.
pub mod alan_ajani;
pub mod buyuk_harf;
pub mod difflib;
pub mod masa;
pub mod yol_tasi;
pub mod devir_md2json;
pub mod kod_orani;
