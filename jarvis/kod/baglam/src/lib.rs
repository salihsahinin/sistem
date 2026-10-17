//! Bağlam yükleme sırası (Karar 117, durum #18).
//!
//! Model (ölçüm: Claude Code 2.1.302, `raporlar/2026-10-16-baglam-sirasi-import-deneyi.md` B1-B8):
//! `L(f) = metin(f) ++ L(i1) ++ … ++ L(ik)`. İçe aktarma satır içinde açılmaz; `@yol` satırı ebeveyn metninde
//! ham kalır, hedef dosya ebeveynin tamamından sonra ayrı blok olarak gelir (pre-order DFS). Aynı dosya ikinci
//! kez görülürse atlanır (ilk görülen kazanır). Kökten en çok 4 sıçrama; daha derini sessizce düşer.
//! `.md` ve `.txt` yüklenir, `.lean` yüklenmez (`.lean.md` symlink'i yüklenir). Kod aralığı ve çit kod bloğu
//! içindeki `@` içe aktarma değildir.
//!
//! Lean karşılığı: `lean/Kanon/BaglamSirasi.lean` (düzleştirme = parça dizisi değişmezi).

use std::collections::HashSet;
use std::fs;
use std::path::{Component, Path, PathBuf};

pub const AZAMI_SICRAMA: usize = 4;

/// Bir dosyadaki içe aktarma adayı: yazıldığı satır ve ham yol.
#[derive(Debug, Clone, PartialEq)]
pub struct IceAktarma {
    pub satir: usize,
    pub yol: String,
}

/// Metindeki `@yol` jetonlarını yazılış sırasıyla çıkarır (çit blok ve backtick aralıkları hariç).
pub fn ice_aktarmalar(metin: &str) -> Vec<IceAktarma> {
    let mut sonuc = Vec::new();
    let mut citte = false;
    for (i, satir) in metin.lines().enumerate() {
        let kirpik = satir.trim_start();
        if kirpik.starts_with("```") || kirpik.starts_with("~~~") {
            citte = !citte;
            continue;
        }
        if citte {
            continue;
        }
        let mut backtick = false;
        let mut onceki_bosluk = true;
        let karakterler: Vec<char> = satir.chars().collect();
        let mut j = 0;
        while j < karakterler.len() {
            let c = karakterler[j];
            if c == '`' {
                backtick = !backtick;
            } else if c == '@' && !backtick && onceki_bosluk {
                let mut k = j + 1;
                while k < karakterler.len() && !karakterler[k].is_whitespace() {
                    k += 1;
                }
                let yol: String = karakterler[j + 1..k].iter().collect();
                if !yol.is_empty() {
                    sonuc.push(IceAktarma { satir: i + 1, yol });
                }
                j = k;
                onceki_bosluk = false;
                continue;
            }
            onceki_bosluk = c.is_whitespace();
            j += 1;
        }
    }
    sonuc
}

/// `~/`, mutlak ve göreli yolu içe aktaran dosyanın dizinine göre çözer; `.`/`..` sözcüksel olarak sadeleşir.
pub fn coz(ebeveyn: &Path, yol: &str) -> PathBuf {
    let ham = if let Some(kalan) = yol.strip_prefix("~/") {
        let ev = std::env::var_os("USERPROFILE").or_else(|| std::env::var_os("HOME")).unwrap_or_default();
        PathBuf::from(ev).join(kalan)
    } else if Path::new(yol).is_absolute() {
        PathBuf::from(yol)
    } else {
        ebeveyn.parent().unwrap_or(Path::new(".")).join(yol)
    };
    let mut sade = PathBuf::new();
    for parca in ham.components() {
        match parca {
            Component::CurDir => {}
            Component::ParentDir => {
                sade.pop();
            }
            p => sade.push(p),
        }
    }
    sade
}

/// Harness'in yüklediği uzantı mı (ölçülen: `.md`, `.txt`).
pub fn yuklenir(yol: &Path) -> bool {
    matches!(yol.extension().and_then(|e| e.to_str()), Some("md") | Some("txt"))
}

/// Genişletmede bir blok: dosya yolu, kökten derinlik, ham metin.
#[derive(Debug)]
pub struct Blok {
    pub yol: PathBuf,
    pub derinlik: usize,
    pub metin: String,
}

/// Denetim bulgusu.
#[derive(Debug, PartialEq)]
pub enum Bulgu {
    /// `@` satırından sonra içe aktarma olmayan metin var: satır içi okuma ile otomatik yükleme sırası ayrışır.
    SonrakiMetin { dosya: PathBuf, satir: usize },
    /// Hedef yok.
    HedefYok { dosya: PathBuf, satir: usize, hedef: PathBuf },
    /// Harness bu uzantıyı yüklemez (`.lean` → `.lean.md` symlink'i kullan).
    Uzanti { dosya: PathBuf, satir: usize, hedef: PathBuf },
    /// 4 sıçramadan derin: harness sessizce düşürür.
    Derin { dosya: PathBuf, satir: usize, hedef: PathBuf },
    /// Aynı hedef ikinci kez içe aktarıldı: ikincisi yok sayılır (yalnız uyarı).
    Tekrar { dosya: PathBuf, satir: usize, hedef: PathBuf },
}

impl Bulgu {
    /// `Tekrar` uyarıdır, diğerleri ihlal.
    pub fn ihlal_mi(&self) -> bool {
        !matches!(self, Bulgu::Tekrar { .. })
    }
}

/// Kökten başlayıp harness sırasıyla blokları üretir; yol boyunca bulguları toplar.
pub fn genislet(kok: &Path) -> std::io::Result<(Vec<Blok>, Vec<Bulgu>)> {
    let mut bloklar = Vec::new();
    let mut bulgular = Vec::new();
    let mut gorulen = HashSet::new();
    let kok = coz(Path::new("."), &kok.to_string_lossy());
    gorulen.insert(kok.clone());
    gez(&kok, 0, &mut gorulen, &mut bloklar, &mut bulgular)?;
    Ok((bloklar, bulgular))
}

fn gez(
    dosya: &Path,
    derinlik: usize,
    gorulen: &mut HashSet<PathBuf>,
    bloklar: &mut Vec<Blok>,
    bulgular: &mut Vec<Bulgu>,
) -> std::io::Result<()> {
    let metin = fs::read_to_string(dosya)?;
    // Düz yazıdaki `@200k` gibi yol olmayan jetonlar içe aktarma sayılmaz (harness var olmayan hedefi yok sayar).
    let aktarmalar: Vec<IceAktarma> =
        ice_aktarmalar(&metin).into_iter().filter(|a| a.yol.contains(['/', '\\', '.']) || coz(dosya, &a.yol).is_file()).collect();
    if let Some(ilk) = aktarmalar.iter().find(|a| coz(dosya, &a.yol).is_file()) {
        let aktarma_satirlari: HashSet<usize> = aktarmalar.iter().map(|a| a.satir).collect();
        for (i, satir) in metin.lines().enumerate().skip(ilk.satir) {
            let no = i + 1;
            if !satir.trim().is_empty() && !aktarma_satirlari.contains(&no) {
                bulgular.push(Bulgu::SonrakiMetin { dosya: dosya.to_path_buf(), satir: no });
                break;
            }
        }
    }
    bloklar.push(Blok { yol: dosya.to_path_buf(), derinlik, metin });
    for a in aktarmalar {
        let hedef = coz(dosya, &a.yol);
        let d = dosya.to_path_buf();
        if !hedef.is_file() {
            bulgular.push(Bulgu::HedefYok { dosya: d, satir: a.satir, hedef });
        } else if !yuklenir(&hedef) {
            bulgular.push(Bulgu::Uzanti { dosya: d, satir: a.satir, hedef });
        } else if derinlik + 1 > AZAMI_SICRAMA {
            bulgular.push(Bulgu::Derin { dosya: d, satir: a.satir, hedef });
        } else if !gorulen.insert(hedef.clone()) {
            bulgular.push(Bulgu::Tekrar { dosya: d, satir: a.satir, hedef });
        } else {
            gez(&hedef, derinlik + 1, gorulen, bloklar, bulgular)?;
        }
    }
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn cit_ve_backtick_atlanir() {
        let m = "a @x.md\n`@y.md`\n```\n@z.md\n```\ne-posta a@b.md\n@son.md\n";
        let yollar: Vec<String> = ice_aktarmalar(m).into_iter().map(|a| a.yol).collect();
        assert_eq!(yollar, ["x.md", "son.md"]);
    }
}
