//! Skill-üretim kapı ağacı (K0 → K1 → [inşa] → K2 → K3 → yaprak).
//!
//! Spec ve kanıtlar: `jarvis/lean/Kanon/SkillKapi.lean`. Bu crate o spec'in çalışan uygulamasıdır; ikisinin aynı
//! hükmü verdiği `tests/fark.rs` fark testiyle denetlenir. Kaynak metin: `jarvis/core/skill-uretim-semasi.md` §1-§2.

pub mod denetim;

/// Adayın kapı girdileri. Her alan tek bir ölçüm; varsayılanlar Lean `Aday` yapısıyla aynı.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Aday {
    pub kapsanmis_tam: bool,
    pub kapsanmis_kismi: bool,
    pub y1: bool,
    pub y2: bool,
    pub y3: bool,
    pub k_w: u64,
    pub k_tau: u64,
    pub delta_bilinmiyor: bool,
    pub deger_yeter: bool,
    pub salih_emri: bool,
    pub r: bool,
    pub i: bool,
    pub p: bool,
    pub rituel: bool,
    pub orkestrator: bool,
    pub yan_etkili: bool,
    pub f1: bool,
    pub f2: bool,
    pub f3: bool,
    pub f4: bool,
    pub f5: bool,
    pub tur_ozel: bool,
}

impl Default for Aday {
    fn default() -> Self {
        Aday {
            kapsanmis_tam: false,
            kapsanmis_kismi: false,
            y1: false,
            y2: false,
            y3: false,
            k_w: 0,
            k_tau: 3,
            delta_bilinmiyor: true,
            deger_yeter: false,
            salih_emri: false,
            r: false,
            i: false,
            p: false,
            rituel: false,
            orkestrator: false,
            yan_etkili: false,
            f1: false,
            f2: false,
            f3: false,
            f4: false,
            f5: false,
            tur_ozel: false,
        }
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Sekil {
    Rituel,
    Orkestrator,
    YanEtkili,
    Uretici,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Yaprak {
    Yeni,
    Evrim,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Hukum {
    Ret0,
    Beklet,
    Onar2,
    Onar3,
    Uret(Sekil, Yaprak),
}

/// K0 := ¬kapsanmış(a,H) ∧ (Y1 ∨ Y2 ∨ Y3)
pub fn k0(a: &Aday) -> bool {
    !a.kapsanmis_tam && (a.y1 || a.y2 || a.y3)
}

/// Z1 := k_W ≥ k_τ ∧ (Δ̂ bilinmiyor ∨ değer yeter)
pub fn z1(a: &Aday) -> bool {
    a.k_w >= a.k_tau && (a.delta_bilinmiyor || a.deger_yeter)
}

/// K1 := Z1 ∨ Z2
pub fn k1(a: &Aday) -> bool {
    z1(a) || a.salih_emri
}

/// K2 := R ∧ İ ∧ ¬P
pub fn k2(a: &Aday) -> bool {
    a.r && a.i && !a.p
}

/// Şekil, first hit-policy: T-R > T-O > T-Y > T-Ü
pub fn sekil(a: &Aday) -> Sekil {
    if a.rituel {
        Sekil::Rituel
    } else if a.orkestrator {
        Sekil::Orkestrator
    } else if a.yan_etkili {
        Sekil::YanEtkili
    } else {
        Sekil::Uretici
    }
}

/// K3 := F1 ∧ F2 ∧ F4 ∧ F5 ∧ tür-özel (F3 Karar 113 M5 ile kapı değil, ölçüm alanı)
pub fn k3(a: &Aday) -> bool {
    a.f1 && a.f2 && a.f4 && a.f5 && a.tur_ozel
}

/// Kapı ağacı: ilk düşen kapı terminali verir; hepsi geçerse yaprak.
pub fn hukum(a: &Aday) -> Hukum {
    if !k0(a) {
        Hukum::Ret0
    } else if !k1(a) {
        Hukum::Beklet
    } else if !k2(a) {
        Hukum::Onar2
    } else if !k3(a) {
        Hukum::Onar3
    } else {
        let y = if a.kapsanmis_kismi { Yaprak::Evrim } else { Yaprak::Yeni };
        Hukum::Uret(sekil(a), y)
    }
}

impl Hukum {
    /// Lean `Hukum.kod` ile aynı sabit sözlük.
    pub fn kod(self) -> String {
        let s = |s: Sekil| match s {
            Sekil::Rituel => "R",
            Sekil::Orkestrator => "O",
            Sekil::YanEtkili => "Y",
            Sekil::Uretici => "Ü",
        };
        match self {
            Hukum::Ret0 => "RET-0".into(),
            Hukum::Beklet => "BEKLET".into(),
            Hukum::Onar2 => "ONAR-2".into(),
            Hukum::Onar3 => "ONAR-3".into(),
            Hukum::Uret(k, Yaprak::Yeni) => format!("ÜRET-{}-yeni", s(k)),
            Hukum::Uret(k, Yaprak::Evrim) => format!("ÜRET-{}-evrim", s(k)),
        }
    }
}

/// `anahtar=değer` satırları (Bool: true/false/1/0, Nat: ondalık; `#` yorum). Lean `oku` ile aynı sözleşme.
pub fn oku(girdi: &str) -> Result<Aday, String> {
    let mut a = Aday::default();
    for ham in girdi.split('\n') {
        let satir = ham.trim();
        if satir.is_empty() || satir.starts_with('#') {
            continue;
        }
        let parca: Vec<&str> = satir.split('=').collect();
        if parca.len() != 2 {
            return Err(format!("satır 'anahtar=değer' değil: {satir}"));
        }
        let (k, v) = (parca[0].trim(), parca[1].trim());
        let b = || match v {
            "true" | "1" => Ok(true),
            "false" | "0" => Ok(false),
            _ => Err(format!("{k}: Bool beklenirken '{v}'")),
        };
        let n = || v.parse::<u64>().map_err(|_| format!("{k}: Nat beklenirken '{v}'"));
        match k {
            "kapsanmisTam" => a.kapsanmis_tam = b()?,
            "kapsanmisKismi" => a.kapsanmis_kismi = b()?,
            "y1" => a.y1 = b()?,
            "y2" => a.y2 = b()?,
            "y3" => a.y3 = b()?,
            "kW" => a.k_w = n()?,
            "kTau" => a.k_tau = n()?,
            "deltaBilinmiyor" => a.delta_bilinmiyor = b()?,
            "degerYeter" => a.deger_yeter = b()?,
            "salihEmri" => a.salih_emri = b()?,
            "r" => a.r = b()?,
            "i" => a.i = b()?,
            "p" => a.p = b()?,
            "rituel" => a.rituel = b()?,
            "orkestrator" => a.orkestrator = b()?,
            "yanEtkili" => a.yan_etkili = b()?,
            "f1" => a.f1 = b()?,
            "f2" => a.f2 = b()?,
            "f3" => a.f3 = b()?,
            "f4" => a.f4 = b()?,
            "f5" => a.f5 = b()?,
            "turOzel" => a.tur_ozel = b()?,
            _ => return Err(format!("bilinmeyen anahtar: {k}")),
        }
    }
    Ok(a)
}

#[cfg(test)]
mod testler {
    use super::*;

    fn gecer() -> Aday {
        Aday {
            y1: true,
            k_w: 3,
            r: true,
            i: true,
            f1: true,
            f2: true,
            f3: true,
            f4: true,
            f5: true,
            tur_ozel: true,
            ..Aday::default()
        }
    }

    #[test]
    fn tam_kapsanan_ret() {
        let a = Aday { kapsanmis_tam: true, ..gecer() };
        assert_eq!(hukum(&a), Hukum::Ret0);
    }

    #[test]
    fn emir_topraklamayi_atlamaz() {
        let a = Aday { salih_emri: true, k_w: 0, r: false, ..gecer() };
        assert_eq!(hukum(&a), Hukum::Onar2);
    }

    #[test]
    fn rituel_once() {
        let a = Aday { rituel: true, orkestrator: true, kapsanmis_kismi: true, ..gecer() };
        assert_eq!(hukum(&a).kod(), "ÜRET-R-evrim");
    }

    #[test]
    fn girdi_hatasi() {
        assert!(oku("bilinmeyen=1").unwrap_err().contains("bilinmeyen anahtar"));
        assert!(oku("kW=üç").unwrap_err().contains("Nat beklenirken"));
    }
}
