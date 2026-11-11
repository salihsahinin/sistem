//! Jarvis Rust crate'lerinin ortak Python-taklit yardımcıları: `py` (str/int/float/yol/alt süreç/SHA-1/tarih),
//! `argparse` (Python 3.11 argparse alt kümesi) ve `harness_anahtar` (`tools/harness_anahtar.py` karşılığı).
//! Bu üç modül önce `jarvis-kural` ve `jarvis-rituel` içinde ayrışmış kopyalar olarak duruyordu; Karar 130 K46 ile tek API'de birleştirildi.
//! Davranış farkı olan yerde seçilen kopya ve gerekçesi modül belgelerinde yazılıdır (örn. `py::float_repr`).
pub mod argparse;
pub mod bronz;
pub mod harness_anahtar;
pub mod py;
