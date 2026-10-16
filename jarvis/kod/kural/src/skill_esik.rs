//! `tools/skill-esik.py` karşılığı: SKILL EŞİK KURALI koşucusu (Karar 51). skill×model çifti n>=eşik koşuma ulaşınca medyan token/süre bandı hesaplanır;
//! son pencerede bandın `carpan`× üstüne çıkan koşumlar SAPMA-YENİ olarak raporlanır. Otomatik kural değişikliği yok.
//! Çıkış: 0 koşum tamam (sapma varlığı hata değildir) · 2 DB yok.
use crate::argparse::{Ayrisan, Secenek};
use crate::{harness_anahtar, py};
use chrono::{Datelike, Duration, Utc};
use rusqlite::types::ValueRef;
use std::cmp::Ordering;
use std::path::Path;

/// Yalnız KESİN eşleme (v_skill_kosum vekil kanalı kuralı): agent_type -> skill.
const ESLEME: [(&str, &str); 1] = [("atlas", "atlas-kosum")];

fn ayrisan() -> Ayrisan {
    Ayrisan::yeni(
        "skill-esik.py",
        None,
        vec![
            Secenek::deger(&["--repo"], "repo", None),
            Secenek::tam(&["--esik-n"], "esik_n", None),
            Secenek::ondalik(&["--carpan"], "carpan", None),
            Secenek::ondalik(&["--saat"], "saat", None),
        ],
    )
}

/// SQLite değeri, Python türleriyle (None/int/float/str).
#[derive(Clone, Debug, PartialEq)]
enum Dyn {
    Yok,
    Int(i64),
    Real(f64),
    Metin(String),
}

impl Dyn {
    fn sayi(&self) -> Option<f64> {
        match self {
            Dyn::Int(i) => Some(*i as f64),
            Dyn::Real(r) => Some(*r),
            _ => None,
        }
    }
    /// f-string gösterimi.
    fn goster(&self) -> String {
        match self {
            Dyn::Yok => "None".into(),
            Dyn::Int(i) => i.to_string(),
            Dyn::Real(r) => py::float_repr(*r),
            Dyn::Metin(s) => s.clone(),
        }
    }
}

fn dyn_oku(v: ValueRef) -> Result<Dyn, String> {
    Ok(match v {
        ValueRef::Null => Dyn::Yok,
        ValueRef::Integer(i) => Dyn::Int(i),
        ValueRef::Real(r) => Dyn::Real(r),
        ValueRef::Text(t) => Dyn::Metin(String::from_utf8_lossy(t).into_owned()),
        ValueRef::Blob(_) => return Err("BLOB sütun (Python: bytes ile karşılaştırma TypeError)".into()),
    })
}

/// (token, süre, zaman, koşum_id)
type Satir = (Dyn, Dyn, Dyn, Dyn);

/// ((skill, model), satır)
type GrupSatir = ((String, Dyn), Satir);

/// `statistics.median`: boş liste StatisticsError (çöker).
fn medyan(mut v: Vec<f64>) -> Option<f64> {
    if v.is_empty() {
        return None;
    }
    v.sort_by(|a, b| a.partial_cmp(b).unwrap_or(Ordering::Equal));
    let n = v.len();
    Some(if n % 2 == 1 { v[n / 2] } else { (v[n / 2 - 1] + v[n / 2]) / 2.0 })
}

/// `now(UTC) - timedelta(hours=saat)` `.isoformat()` (mikrosaniye 0 ise kesir yok).
fn esik_zamani(saat: f64) -> Result<String, String> {
    let mikro = (saat * 3_600_000_000.0).round_ties_even();
    if !mikro.is_finite() || mikro.abs() > 9.0e18 {
        return Err("timedelta taşması (OverflowError)".into());
    }
    let t = Utc::now().checked_sub_signed(Duration::microseconds(mikro as i64)).ok_or("tarih taşması (OverflowError)")?;
    if !(1..=9999).contains(&t.year()) {
        return Err("tarih aralık dışı (OverflowError)".into());
    }
    let frac = t.timestamp_subsec_micros();
    Ok(format!("{}{}+00:00", t.format("%Y-%m-%dT%H:%M:%S"), if frac == 0 { String::new() } else { format!(".{frac:06}") }))
}

pub fn kos(argv: &[String]) -> i32 {
    let a = match ayrisan().ayristir(argv) {
        Ok(a) => a,
        Err(k) => return k,
    };
    let repo = a.metin("repo").map(String::from).unwrap_or_else(harness_anahtar::jarvis);
    let esik_n = a.tam("esik_n").unwrap_or(10);
    let carpan = a.ondalik("carpan").unwrap_or(2.0);
    let saat = a.ondalik("saat").unwrap_or(24.0);
    let db = py::join(&py::join(&py::abspath(&repo), "veri"), "baglam.sqlite");
    if !Path::new(&db).exists() {
        py::err(&format!("HATA: {db} yok\n"));
        return 2;
    }
    let esik_ts = match esik_zamani(saat) {
        Ok(t) => t,
        Err(e) => return py::coker(&e),
    };
    // (skill, model) -> satırlar; ekleme sırası korunur
    let mut gruplar: Vec<((String, Dyn), Vec<Satir>)> = vec![];
    let oku = || -> Result<Vec<GrupSatir>, String> {
        let c = rusqlite::Connection::open_with_flags(&db, rusqlite::OpenFlags::SQLITE_OPEN_READ_WRITE).map_err(|e| e.to_string())?;
        let mut cikti = vec![];
        for (agent_type, skill) in ESLEME {
            let mut s = c
                .prepare("SELECT modeller, output_tokens, sure_sn, valid_time_bas, kosum_id FROM amb_olgu_kosum WHERE agent_type=?")
                .map_err(|e| e.to_string())?;
            let mut rows = s.query([agent_type]).map_err(|e| e.to_string())?;
            while let Some(r) = rows.next().map_err(|e| e.to_string())? {
                let g = |i: usize| dyn_oku(r.get_ref(i).map_err(|e| e.to_string())?);
                cikti.push(((skill.to_string(), g(0)?), (g(1)?, g(2)?, g(3)?, g(4)?)));
            }
        }
        Ok(cikti)
    };
    match oku() {
        Ok(satirlar) => {
            for (anahtar, s) in satirlar {
                match gruplar.iter_mut().find(|(k, _)| *k == anahtar) {
                    Some((_, v)) => v.push(s),
                    None => gruplar.push((anahtar, vec![s])),
                }
            }
        }
        Err(e) => return py::coker(&e),
    }
    // sorted(gruplar.items()): anahtarlar karşılaştırılamıyorsa TypeError
    if gruplar.len() > 1 {
        let hepsi_metin = gruplar.iter().all(|((_, m), _)| matches!(m, Dyn::Metin(_)));
        let hepsi_sayi = gruplar.iter().all(|((_, m), _)| m.sayi().is_some());
        if !hepsi_metin && !hepsi_sayi {
            return py::coker("karışık türde model anahtarları sıralanamaz (TypeError)");
        }
        gruplar.sort_by(|((s1, m1), _), ((s2, m2), _)| {
            s1.cmp(s2).then_with(|| match (m1, m2) {
                (Dyn::Metin(x), Dyn::Metin(y)) => x.cmp(y),
                _ => m1.sayi().partial_cmp(&m2.sayi()).unwrap_or(Ordering::Equal),
            })
        });
    }
    let mut sapma_yeni = 0;
    for ((skill, model), satirlar) in &gruplar {
        let n = satirlar.len();
        let model_s = model.goster();
        if (n as i128) < esik_n {
            py::print(&format!("[ATLA ] {skill} × {model_s}: n={n} < eşik {esik_n} — medyan hesaplanmaz (kural gereği)"));
            continue;
        }
        let Some(med_tok) = medyan(satirlar.iter().filter_map(|s| s.0.sayi()).collect()) else { return py::coker("medyan: boş token listesi (StatisticsError)") };
        if satirlar.iter().any(|s| !matches!(s.0, Dyn::Yok | Dyn::Int(_) | Dyn::Real(_))) {
            return py::coker("token sütununda sayı olmayan değer (TypeError)");
        }
        let sureler: Vec<f64> = satirlar.iter().filter_map(|s| s.1.sayi()).collect();
        let med_sure = medyan(sureler);
        let asan = |s: &Satir| {
            s.0.sayi().is_some_and(|t| med_tok != 0.0 && t > carpan * med_tok) || s.1.sayi().is_some_and(|d| med_sure.is_some_and(|m| m != 0.0 && d > carpan * m))
        };
        let asanlar: Vec<&Satir> = satirlar.iter().filter(|s| asan(s)).collect();
        let mut yeniler: Vec<&Satir> = vec![];
        for s in &asanlar {
            match &s.2 {
                Dyn::Metin(t) if *t >= esik_ts => yeniler.push(s),
                Dyn::Metin(_) | Dyn::Yok => {}
                _ => return py::coker("valid_time_bas metin değil (TypeError)"),
            }
        }
        let Some(ms) = med_sure else { return py::coker("medyan süre yok (None biçimlendirme TypeError)") };
        py::print(&format!(
            "[BANT ] {skill} × {model_s}: n={n} · medyan {:.0} tok / {:.0} sn · {}× üstü toplam {} · son {:.0} saatte {}",
            med_tok,
            ms,
            py::float_repr(carpan),
            asanlar.len(),
            saat,
            yeniler.len()
        ));
        for s in yeniler {
            sapma_yeni += 1;
            let Some(tok) = s.0.sayi() else { return py::coker("SAPMA satırında token yok (TypeError)") };
            if med_tok == 0.0 {
                return py::coker("medyan token 0 (ZeroDivisionError)");
            }
            py::print(&format!("[SAPMA-YENİ] {skill} × {model_s} · {} · {} tok (medyan×{:.1}) · {} → teslim raporuna satır", s.3.goster(), s.0.goster(), tok / med_tok, s.2.goster()));
        }
    }
    if gruplar.is_empty() {
        py::print("[BOŞ  ] kesin skill eşlemeli koşum verisi yok (ESLEME kanalları boş)");
    }
    py::print(&format!("skill-esik: {} çift tarandı · yeni-pencere sapması {sapma_yeni} · kural: Karar 51 (otomatik değişiklik YOK)", gruplar.len()));
    0
}
