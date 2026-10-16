//! Jarvis kural/denetim araçlarının Rust karşılığı: `.claude/skills/gorev-emri-derleme/scripts/tetik-denetim.py`,
//! `.claude/skills/halusinasyon-engelleyici/scripts/derece.py`, `tools/{skill-esik,paralel-kapi,ad-esitligi-denetim}.py`.
//! Her modül `kos(argv) -> i32` verir; `src/bin/*.rs` ince sarmalayıcılardır. Fark testi: `tests/` (Python = Rust; `tetik` ve `derece` için
//! ayrıca Lean `jarvis/lean` ikilileriyle üç yönlü). Parti 2'nin (`jarvis/kod/rituel`) `py`/`argparse`/`harness_anahtar` yardımcılarının
//! küçültülmüş kopyası burada durur (PR #7 birleşince ortak crate'e taşınabilir).
pub mod ad_esitligi;
pub mod argparse;
pub mod derece;
pub mod harness_anahtar;
pub mod paralel;
pub mod py;
pub mod pyjson;
pub mod skill_esik;
pub mod tetik;
