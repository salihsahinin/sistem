//! Jarvis hook'ları: `.claude/hooks/*.sh` + `tools/prompt-dosya.py` + `tools/paket-yonlendir.py` + kök `bin/hook-dispatch.sh`
//! davranışının Rust karşılığı. Her modül `kos(...) -> Sonuc` verir; `jarvis-hook <olay>` ikilisi bunları çağırır.
//! Fark testi: `tests/hook_fark.rs` (eski betik ile yeni ikili aynı girdide stdout/stderr/çıkış/kütük satırı eşit).
pub mod altajan_okuma;
pub mod ajan_fren;
pub mod buyuk_harf;
pub mod core_tel;
pub mod dispatch;
pub mod ortak;
pub mod paket;
pub mod prompt_dosya;
pub mod sabit;
pub mod session_start;
pub mod talimat;

pub use ortak::{Ortam, Sonuc};
