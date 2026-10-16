//! Sabit güncellik denetimi (durum #15, Karar 116): `lean/Kanon/Sabitler.lean` kaydını okur, `veri/model-kesim.jsonl` ile
//! bugünü karşılaştırır, "yeniden bak" listesini üretir. Kural Lean'deki `yenidenBak`ın aynısıdır:
//! yeni kuşak devrede ∨ AS-OF'tan bu yana gün ≥ `gozdenGecirmeGun`; yeni kuşak önce sayılır.
//! Yeni kuşak = tabloda, devreye giriş tarihi sabitin AS-OF'undan sonra olan bir model. Devreye giriş tarihi: modelin
//! `yayim` satırı varsa o, yoksa en geç kesim tarihi (kesim ≤ yayım olduğundan bu ölçüt eksik sayabilir, fazla saymaz).
//! Çıktı iki yüzeye gider: seans açılış brifine tek satır (`brif_satiri`), tam liste (`jarvis-hook sabit-guncellik`).
use crate::ortak::{Ortam, Sonuc, bugun_yerel, ilk_n, oku_py};
use chrono::NaiveDate;
use regex::Regex;
use serde_json::Value;
use std::path::Path;

const LEAN: &str = "lean/Kanon/Sabitler.lean";
const KESIM: &str = "veri/model-kesim.jsonl";

#[derive(Debug, Clone, PartialEq)]
pub struct Sabit {
    pub ad: String,
    pub deger: String,
    pub modul: String,
    pub as_of: NaiveDate,
    pub kusak: String,
    pub kaynak: String,
}

#[derive(Debug, Clone, PartialEq)]
pub enum Neden {
    /// AS-OF'tan sonra devreye giren modeller (kısa adlar).
    YeniKusak(Vec<String>),
    /// AS-OF'tan bu yana geçen gün.
    SureDoldu(i64),
}

#[derive(Debug, Clone, PartialEq)]
pub struct Model {
    pub ad: String,
    pub devreye: NaiveDate,
}

/// Lean kaydından (sabit listesi, gözden geçirme günü).
pub fn lean_oku(metin: &str) -> Result<(Vec<Sabit>, i64), String> {
    let gun = Regex::new(r"def\s+gozdenGecirmeGun\s*:\s*Nat\s*:=\s*(\d+)").unwrap();
    let gun: i64 = gun
        .captures(metin)
        .and_then(|c| c[1].parse().ok())
        .ok_or("gozdenGecirmeGun bulunamadı")?;
    let bas = metin.find("def kayit").ok_or("`def kayit` bulunamadı")?;
    let govde = &metin[bas..];
    let son = govde.find("\n]").ok_or("kayıt listesi `]` ile kapanmıyor")?;
    let satir_re = Regex::new(r#"^\s*⟨"([^"]*)",\s*"([^"]*)",\s*"([^"]*)",\s*"([^"]*)",\s*"([^"]*)",\s*\.(\w+)⟩,?\s*$"#).unwrap();
    let mut kayit = vec![];
    for l in govde[..son].lines().skip(1) {
        if !l.contains('⟨') {
            continue;
        }
        let c = satir_re.captures(l).ok_or_else(|| format!("kayıt satırı çözülemedi: {}", l.trim()))?;
        let as_of = NaiveDate::parse_from_str(&c[4], "%Y-%m-%d").map_err(|e| format!("{}: AS-OF `{}` ({e})", &c[1], &c[4]))?;
        kayit.push(Sabit { ad: c[1].into(), deger: c[2].into(), modul: c[3].into(), as_of, kusak: c[5].into(), kaynak: c[6].into() });
    }
    if kayit.is_empty() {
        return Err("kayıtta sabit yok".into());
    }
    Ok((kayit, gun))
}

fn tarih(s: &str) -> Option<NaiveDate> {
    let tam = if s.len() == 7 { format!("{s}-01") } else { s.to_string() };
    NaiveDate::parse_from_str(&tam, "%Y-%m-%d").ok()
}

/// Kesim tablosundan model başına devreye giriş tarihi (tablo sırası korunur).
pub fn kesim_oku(metin: &str) -> Result<Vec<Model>, String> {
    struct Ham {
        ad: String,
        yayim: Option<NaiveDate>,
        kesim: Option<NaiveDate>,
    }
    let mut ham: Vec<Ham> = vec![];
    for (n, l) in metin.lines().enumerate().filter(|(_, l)| !l.trim().is_empty()) {
        let d: Value = serde_json::from_str(l).map_err(|e| format!("satır {}: {e}", n + 1))?;
        let alan = |k: &str| d.get(k).and_then(Value::as_str).ok_or(format!("satır {}: `{k}` yok", n + 1));
        let ad = alan("model_ad")?.replace("Claude ", "");
        let t = tarih(alan("kesim_tarihi")?).ok_or(format!("satır {}: kesim_tarihi çözülemedi", n + 1))?;
        let yayim = alan("kesim_turu")? == "yayim";
        let i = match ham.iter().position(|h| h.ad == ad) {
            Some(i) => i,
            None => {
                ham.push(Ham { ad, yayim: None, kesim: None });
                ham.len() - 1
            }
        };
        let h = &mut ham[i];
        if yayim {
            h.yayim = Some(h.yayim.map_or(t, |x| x.max(t)));
        } else {
            h.kesim = Some(h.kesim.map_or(t, |x| x.max(t)));
        }
    }
    Ok(ham.into_iter().filter_map(|h| Some(Model { devreye: h.yayim.or(h.kesim)?, ad: h.ad })).collect())
}

/// Lean `yenidenBak`ın karşılığı.
pub fn yeniden_bak(s: &Sabit, modeller: &[Model], bugun: NaiveDate, esik_gun: i64) -> Option<Neden> {
    let yeni: Vec<String> = modeller.iter().filter(|m| m.devreye > s.as_of).map(|m| m.ad.clone()).collect();
    if !yeni.is_empty() {
        return Some(Neden::YeniKusak(yeni));
    }
    let gecen = (bugun - s.as_of).num_days();
    (gecen >= esik_gun).then_some(Neden::SureDoldu(gecen))
}

pub fn denetle(repo: &Path, bugun: NaiveDate) -> Result<(Vec<(Sabit, Neden)>, usize), String> {
    let lean = oku_py(&repo.join(LEAN)).ok_or(format!("{LEAN} okunamadı"))?;
    let kesim = oku_py(&repo.join(KESIM)).ok_or(format!("{KESIM} okunamadı"))?;
    let (kayit, esik) = lean_oku(&lean).map_err(|e| format!("{LEAN}: {e}"))?;
    let modeller = kesim_oku(&kesim).map_err(|e| format!("{KESIM}: {e}"))?;
    let toplam = kayit.len();
    Ok((kayit.into_iter().filter_map(|s| yeniden_bak(&s, &modeller, bugun, esik).map(|n| (s, n))).collect(), toplam))
}

fn bugun() -> NaiveDate {
    NaiveDate::parse_from_str(&bugun_yerel(), "%Y-%m-%d").unwrap()
}

/// Açılış brifi için tek satır; yeniden bakılacak sabit yoksa `None`.
pub fn brif_satiri(repo: &Path) -> Option<String> {
    match denetle(repo, bugun()) {
        Err(e) => Some(format!("SABİT-GÜNCELLİK: denetlenemedi ({}) — jarvis-hook sabit-guncellik", ilk_n(&e, 120))),
        Ok((l, _)) if l.is_empty() => None,
        Ok((l, _)) => {
            let yeni = l.iter().filter(|(_, n)| matches!(n, Neden::YeniKusak(_))).count();
            let mut modeller: Vec<&str> = vec![];
            for (_, n) in &l {
                if let Neden::YeniKusak(m) = n {
                    for a in m {
                        if !modeller.contains(&a.as_str()) {
                            modeller.push(a);
                        }
                    }
                }
            }
            let kus = if modeller.is_empty() { String::new() } else { format!("; yeni kuşak: {}", modeller.join(", ")) };
            Some(format!(
                "SABİT-GÜNCELLİK (Karar 116): yeniden bak: {} sabit (yeni kuşak {yeni} · süre {}{kus}) → jarvis-hook sabit-guncellik",
                l.len(),
                l.len() - yeni
            ))
        }
    }
}

/// `jarvis-hook sabit-guncellik`: tam liste.
pub fn kos(o: &Ortam) -> Sonuc {
    let mut s = Sonuc::bos();
    let mut cikti = String::new();
    match denetle(&o.repo, bugun()) {
        Err(e) => {
            s.hata = format!("HATA: {e}\n");
            s.kod = 1;
        }
        Ok((l, toplam)) => {
            cikti.push_str(&format!("yeniden bak: {} sabit / {toplam} kayıt (BUGÜN {})\n", l.len(), bugun_yerel()));
            for (sb, n) in &l {
                let neden = match n {
                    Neden::YeniKusak(m) => format!("yeni kuşak: {}", m.join(", ")),
                    Neden::SureDoldu(g) => format!("{g} gün geçti"),
                };
                cikti.push_str(&format!("- {} = {} [{}] AS-OF {} · {} · {} → {neden}\n", sb.ad, sb.deger, sb.modul, sb.as_of, sb.kusak, sb.kaynak));
            }
        }
    }
    s.cikti = cikti.into_bytes();
    s
}
