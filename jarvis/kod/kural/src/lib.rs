//! Jarvis kural/denetim araçlarının Rust karşılığı: `.claude/skills/gorev-emri-derleme/scripts/tetik-denetim.py`,
//! `.claude/skills/halusinasyon-engelleyici/scripts/derece.py`, `tools/{skill-esik,paralel-kapi,ad-esitligi-denetim}.py`.
//! Her modül `kos(argv) -> i32` verir; `src/bin/*.rs` ince sarmalayıcılardır. Fark testi: `tests/` (Python = Rust; `tetik` ve `derece` için
//! ayrıca Lean `jarvis/lean` ikilileriyle üç yönlü). `py`/`argparse`/`harness_anahtar` yardımcıları `jarvis-ortak` crate'indedir
//! (Karar 130 K46; eski kopya `arsiv/kod/rust/ortak-oncesi-kopyalar-2026-11-11/kural/`).
pub mod ad_esitligi;
pub mod derece;
pub mod paralel;
pub mod pyjson;
pub mod skill_esik;
pub mod tetik;
/// Ortak Python-taklit yardımcıları `jarvis-ortak` crate'inde durur (Karar 130 K46); eski `crate::py` yolları bu yeniden dışa aktarımla çalışır.
pub use jarvis_ortak::{argparse, harness_anahtar, py};
