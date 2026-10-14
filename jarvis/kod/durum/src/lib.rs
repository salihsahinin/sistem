//! Ortak durum tablosu: ekle-yalnız olay kütüğü ve katlanmış güncel durum.
//!
//! Doğruluk kaynağı `ortak/durum-olay.jsonl` (satır = bir olay). Durum bellek içinde olayların sırayla
//! uygulanmasıyla hesaplanır; geçersiz geçiş hatadır. `son_gecerlilik` (YYYY-MM-DD) bugünden küçükse
//! kayıt okuma anında `bayat` sayılır (kütüğe yazılmaz).

use serde::{Deserialize, Serialize};
use std::collections::BTreeMap;

pub const ALANLAR: [&str; 9] = ["jarvis", "friday", "tart", "gard", "span", "calc", "deci", "vega", "sage"];
pub const OTURUM_BASI_BAYT: usize = 1024;

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "lowercase")]
pub enum Durum {
    Acik,
    Islemde,
    Tamam,
    Tuketildi,
    Bayat,
}

impl Durum {
    pub fn ad(self) -> &'static str {
        match self {
            Durum::Acik => "acik",
            Durum::Islemde => "islemde",
            Durum::Tamam => "tamam",
            Durum::Tuketildi => "tuketildi",
            Durum::Bayat => "bayat",
        }
    }
    pub fn coz(s: &str) -> Option<Durum> {
        Some(match s {
            "acik" => Durum::Acik,
            "islemde" => Durum::Islemde,
            "tamam" => Durum::Tamam,
            "tuketildi" => Durum::Tuketildi,
            "bayat" => Durum::Bayat,
            _ => return None,
        })
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "lowercase")]
pub enum OlayTuru {
    Ac,
    Al,
    Bitir,
    Tuket,
    Bayatla,
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct Olay {
    pub olay: OlayTuru,
    pub id: u64,
    pub ts: String,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub alan: Option<String>,
    #[serde(default, rename = "is", skip_serializing_if = "Option::is_none")]
    pub is_ad: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub sonraki_eylem: Option<String>,
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    pub kanit: Vec<String>,
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    pub girdi: Vec<u64>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub son_gecerlilik: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub oturum: Option<String>,
}

impl Olay {
    pub fn yalin(olay: OlayTuru, id: u64, ts: &str) -> Olay {
        Olay {
            olay,
            id,
            ts: ts.to_string(),
            alan: None,
            is_ad: None,
            sonraki_eylem: None,
            kanit: vec![],
            girdi: vec![],
            son_gecerlilik: None,
            oturum: None,
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize)]
pub struct Kayit {
    pub id: u64,
    pub alan: String,
    pub durum: Durum,
    #[serde(rename = "is")]
    pub is_ad: String,
    pub sonraki_eylem: String,
    pub kanit: Vec<String>,
    pub girdi: Vec<u64>,
    pub son_gecerlilik: Option<String>,
    pub ts: String,
    pub oturum: Option<String>,
}

impl Kayit {
    /// Bugünün tarihine (YYYY-MM-DD...) göre geçerli durum: süresi geçen, tüketilmemiş kayıt `bayat` sayılır.
    pub fn efektif(&self, bugun: &str) -> Durum {
        match (&self.son_gecerlilik, self.durum) {
            (Some(s), d) if d != Durum::Tuketildi && d != Durum::Bayat && s.as_str() < tarih_kismi(bugun) => Durum::Bayat,
            (_, d) => d,
        }
    }
}

#[derive(Debug, PartialEq, Eq)]
pub enum Hata {
    /// Geçersiz geçiş, bulunamadı, bozuk kütük (çıkış 1).
    Gecersiz(String),
    /// Kullanım hatası (çıkış 2).
    Kullanim(String),
}

impl Hata {
    pub fn kod(&self) -> i32 {
        match self {
            Hata::Gecersiz(_) => 1,
            Hata::Kullanim(_) => 2,
        }
    }
    pub fn mesaj(&self) -> &str {
        match self {
            Hata::Gecersiz(m) | Hata::Kullanim(m) => m,
        }
    }
}

fn gecersiz<T>(m: String) -> Result<T, Hata> {
    Err(Hata::Gecersiz(m))
}

pub fn tarih_kismi(ts: &str) -> &str {
    ts.get(..10).unwrap_or(ts)
}

/// Katlanmış defter: kayıtlar id sırasıyla.
#[derive(Debug, Default, Clone)]
pub struct Defter {
    pub kayitlar: BTreeMap<u64, Kayit>,
}

impl Defter {
    pub fn sonraki_id(&self) -> u64 {
        self.kayitlar.keys().next_back().map_or(1, |m| m + 1)
    }

    /// Olayları sırayla uygular (yeniden oynatma; son_gecerlilik denetimi yok).
    pub fn katla(olaylar: &[Olay]) -> Result<Defter, Hata> {
        let mut d = Defter::default();
        for o in olaylar {
            d.uygula(o, "0000-00-00")?;
        }
        Ok(d)
    }

    /// Tek olayı doğrular ve uygular. `bugun`: süresi geçmiş kayıtta al/bitir/tuket reddi için.
    pub fn uygula(&mut self, o: &Olay, bugun: &str) -> Result<(), Hata> {
        if o.olay == OlayTuru::Ac {
            let alan = o.alan.clone().ok_or_else(|| Hata::Gecersiz(format!("ac #{}: alan yok", o.id)))?;
            if !ALANLAR.contains(&alan.as_str()) {
                return gecersiz(format!("bilinmeyen alan: {alan}"));
            }
            if o.id != self.sonraki_id() {
                return gecersiz(format!("ac: id {} beklenen {} değil", o.id, self.sonraki_id()));
            }
            for g in &o.girdi {
                if !self.kayitlar.contains_key(g) {
                    return gecersiz(format!("girdi #{g} bulunamadı"));
                }
            }
            let is_ad = o.is_ad.clone().filter(|s| !s.is_empty());
            let sonraki = o.sonraki_eylem.clone().filter(|s| !s.is_empty());
            let (Some(is_ad), Some(sonraki_eylem)) = (is_ad, sonraki) else {
                return gecersiz(format!("ac #{}: is ve sonraki_eylem zorunlu", o.id));
            };
            self.kayitlar.insert(
                o.id,
                Kayit {
                    id: o.id,
                    alan,
                    durum: Durum::Acik,
                    is_ad,
                    sonraki_eylem,
                    kanit: o.kanit.clone(),
                    girdi: o.girdi.clone(),
                    son_gecerlilik: o.son_gecerlilik.clone(),
                    ts: o.ts.clone(),
                    oturum: o.oturum.clone(),
                },
            );
            return Ok(());
        }
        let k = self.kayitlar.get_mut(&o.id).ok_or_else(|| Hata::Gecersiz(format!("#{} bulunamadı", o.id)))?;
        let efektif = k.efektif(bugun);
        let hedef = match o.olay {
            OlayTuru::Al => {
                if efektif != Durum::Acik {
                    return gecersiz(format!("#{} al: durum {} (acik beklenir)", o.id, efektif.ad()));
                }
                Durum::Islemde
            }
            OlayTuru::Bitir => {
                if efektif != Durum::Islemde {
                    return gecersiz(format!("#{} bitir: durum {} (islemde beklenir)", o.id, efektif.ad()));
                }
                Durum::Tamam
            }
            OlayTuru::Tuket => {
                if efektif != Durum::Tamam {
                    return gecersiz(format!("#{} tuket: durum {} (tamam beklenir)", o.id, efektif.ad()));
                }
                Durum::Tuketildi
            }
            OlayTuru::Bayatla => {
                if k.durum == Durum::Bayat {
                    return gecersiz(format!("#{} zaten bayat", o.id));
                }
                Durum::Bayat
            }
            OlayTuru::Ac => unreachable!(),
        };
        k.durum = hedef;
        k.ts = o.ts.clone();
        k.kanit.extend(o.kanit.iter().cloned());
        if o.oturum.is_some() {
            k.oturum = o.oturum.clone();
        }
        Ok(())
    }

    pub fn listele(&self, alan: Option<&str>, durum: Option<Durum>, bugun: &str) -> Vec<(&Kayit, Durum)> {
        self.kayitlar
            .values()
            .map(|k| (k, k.efektif(bugun)))
            .filter(|(k, e)| alan.is_none_or(|a| k.alan == a) && durum.is_none_or(|d| *e == d))
            .collect()
    }

    /// Bağlama konacak kısa metin: alanın açık + işlemde kayıtları (süresi geçmiş olanlar hariç), ≤ 1 KB.
    pub fn oturum_basi(&self, alan: &str, bugun: &str) -> String {
        let mut satirlar: Vec<String> = vec![];
        for (k, e) in self.listele(Some(alan), None, bugun) {
            if e == Durum::Acik || e == Durum::Islemde {
                satirlar.push(format!("#{} {} {} -> {}", k.id, e.ad(), k.is_ad, k.sonraki_eylem));
            }
        }
        if satirlar.is_empty() {
            return format!("DURUM {alan} ({}): açık iş yok\n", tarih_kismi(bugun));
        }
        let toplam = satirlar.len();
        let mut cikti = format!("DURUM {alan} ({}): {toplam} açık/işlemde\n", tarih_kismi(bugun));
        let mut yazilan = 0;
        for s in &satirlar {
            // Sığmayan satırlar için "... +N daha" satırına yer ayır (en çok 32 bayt).
            let ek = if yazilan + 1 < toplam { 32 } else { 0 };
            if cikti.len() + s.len() + 1 + ek > OTURUM_BASI_BAYT {
                break;
            }
            cikti.push_str(s);
            cikti.push('\n');
            yazilan += 1;
        }
        if yazilan < toplam {
            cikti.push_str(&format!("... +{} daha\n", toplam - yazilan));
        }
        cikti
    }
}

/// Kütük satırlarını (JSONL) olaylara çevirir; boş satırlar atlanır.
pub fn olaylari_oku(metin: &str) -> Result<Vec<Olay>, Hata> {
    let mut v = vec![];
    for (i, s) in metin.lines().enumerate() {
        if s.trim().is_empty() {
            continue;
        }
        v.push(serde_json::from_str(s).map_err(|e| Hata::Gecersiz(format!("kütük satır {}: {e}", i + 1)))?);
    }
    Ok(v)
}

pub fn olay_satiri(o: &Olay) -> String {
    serde_json::to_string(o).expect("olay serileştirilir")
}

/// Sistem saatinden `YYYY-MM-DDTHH:MM:SSZ` (UTC).
pub fn simdi_iso() -> String {
    let s = std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).map_or(0, |d| d.as_secs()) as i64;
    let (gun, sn) = (s.div_euclid(86400), s.rem_euclid(86400));
    // Howard Hinnant civil_from_days.
    let z = gun + 719_468;
    let era = z.div_euclid(146_097);
    let doe = z.rem_euclid(146_097);
    let yoe = (doe - doe / 1460 + doe / 36_524 - doe / 146_096) / 365;
    let y = yoe + era * 400;
    let doy = doe - (365 * yoe + yoe / 4 - yoe / 100);
    let mp = (5 * doy + 2) / 153;
    let d = doy - (153 * mp + 2) / 5 + 1;
    let m = if mp < 10 { mp + 3 } else { mp - 9 };
    let y = if m <= 2 { y + 1 } else { y };
    format!("{y:04}-{m:02}-{d:02}T{:02}:{:02}:{:02}Z", sn / 3600, sn % 3600 / 60, sn % 60)
}

#[cfg(test)]
mod testler {
    use super::*;

    const T: &str = "2026-10-14T09:00:00Z";

    fn ac(id: u64, alan: &str) -> Olay {
        let mut o = Olay::yalin(OlayTuru::Ac, id, T);
        o.alan = Some(alan.into());
        o.is_ad = Some(format!("is{id}"));
        o.sonraki_eylem = Some(format!("eylem{id}"));
        o
    }

    fn ol(t: OlayTuru, id: u64) -> Olay {
        Olay::yalin(t, id, T)
    }

    #[test]
    fn gecerli_zincir() {
        let d = Defter::katla(&[ac(1, "sage"), ol(OlayTuru::Al, 1), ol(OlayTuru::Bitir, 1), ol(OlayTuru::Tuket, 1)]).unwrap();
        assert_eq!(d.kayitlar[&1].durum, Durum::Tuketildi);
    }

    #[test]
    fn gecersiz_gecisler() {
        for t in [OlayTuru::Bitir, OlayTuru::Tuket] {
            assert_eq!(Defter::katla(&[ac(1, "sage"), ol(t, 1)]).unwrap_err().kod(), 1);
        }
        // iki oturum aynı işe girmez
        assert!(Defter::katla(&[ac(1, "sage"), ol(OlayTuru::Al, 1), ol(OlayTuru::Al, 1)]).is_err());
        // tamam -> al yok
        assert!(Defter::katla(&[ac(1, "sage"), ol(OlayTuru::Al, 1), ol(OlayTuru::Bitir, 1), ol(OlayTuru::Al, 1)]).is_err());
        // bulunamadı
        assert!(Defter::katla(&[ol(OlayTuru::Al, 9)]).is_err());
        // bayat -> bayatla
        assert!(Defter::katla(&[ac(1, "sage"), ol(OlayTuru::Bayatla, 1), ol(OlayTuru::Bayatla, 1)]).is_err());
        // kötü alan, kötü id, olmayan girdi
        assert!(Defter::katla(&[ac(1, "yok")]).is_err());
        assert!(Defter::katla(&[ac(5, "sage")]).is_err());
        let mut g = ac(1, "sage");
        g.girdi = vec![7];
        assert!(Defter::katla(&[g]).is_err());
    }

    #[test]
    fn bayatla_her_durumdan() {
        let zincir = [vec![], vec![OlayTuru::Al], vec![OlayTuru::Al, OlayTuru::Bitir], vec![OlayTuru::Al, OlayTuru::Bitir, OlayTuru::Tuket]];
        for ara in zincir {
            let mut v = vec![ac(1, "sage")];
            v.extend(ara.into_iter().map(|t| ol(t, 1)));
            v.push(ol(OlayTuru::Bayatla, 1));
            assert_eq!(Defter::katla(&v).unwrap().kayitlar[&1].durum, Durum::Bayat);
        }
    }

    #[test]
    fn son_gecerlilik_bayat_sayilir() {
        let mut a = ac(1, "sage");
        a.son_gecerlilik = Some("2026-10-13".into());
        let d = Defter::katla(&[a]).unwrap();
        assert_eq!(d.kayitlar[&1].efektif("2026-10-13T23:59:59Z"), Durum::Acik);
        assert_eq!(d.kayitlar[&1].efektif("2026-10-14T00:00:00Z"), Durum::Bayat);
        let mut d2 = d.clone();
        assert!(d2.uygula(&ol(OlayTuru::Al, 1), "2026-10-14").is_err());
        assert!(d.oturum_basi("sage", "2026-10-14").contains("açık iş yok"));
    }

    #[test]
    fn oturum_basi_sinirli() {
        let v: Vec<Olay> = (1..=80).map(|i| ac(i, "sage")).collect();
        let d = Defter::katla(&v).unwrap();
        let s = d.oturum_basi("sage", T);
        assert!(s.len() <= OTURUM_BASI_BAYT, "{}", s.len());
        assert!(s.contains("... +"));
    }

    #[test]
    fn tarih_bicimi() {
        let s = simdi_iso();
        assert_eq!(s.len(), 20);
        assert!(s.starts_with("20") && s.ends_with('Z'));
    }
}
