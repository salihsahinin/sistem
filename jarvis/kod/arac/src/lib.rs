//! Jarvis genel araçlarının Rust karşılığı: `tools/{alan-ajani-dogur,buyuk-harf-temizle}.py` + `.claude/skills/karar-masasi/scripts/masa-uret.py` (parti 2: `devir-md2json` · `kod-orani-olcum`).
//! Tek seferlik Mac göç aracı `yol-tasi` arşivdedir: `arsiv/kod/rust/yol-tasi-2026-11-11/` (Karar 130 K53).
//! Her modül `kos(argv) -> i32` verir; `src/bin/*.rs` ikilileri ince sarmalayıcıdır. Ortak Python-taklit yardımcıları `jarvis-ortak` crate'indedir (`jarvis_rituel::{py, argparse}` yeniden dışa aktarımıyla erişilir).
pub mod alan_ajani;
pub mod buyuk_harf;
pub mod difflib;
pub mod masa;
pub mod devir_md2json;
pub mod kod_orani;
pub mod karakter;
