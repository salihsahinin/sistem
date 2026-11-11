//! Aylık bronz kütük düzeni (Karar 130 D23): eklemeli ham kütük `veri/bronz/<ad>.jsonl` yerine
//! `veri/bronz/<ad>/<YYYY-MM>.jsonl` dosyalarına bölünür. Ay, kaydın kendi zaman damgasından alınır.
//! Yazan: `ekle` (satırları ay dosyalarına dağıtır). Okuyan: `oku_kati` / `oku_bayt` (bütün ay dosyaları ad sırasıyla, birleşik).
//! Python karşılığı `jarvis/tools/bronz_ay.py`; ajan hook betiklerinde aynı kural satır içi yazılıdır.
//!
//! Ay kuralı: JSON nesnesinde `ZAMAN_ANAHTARLARI` sırasıyla ilk `YYYY-MM` önekli dize; yoksa üst düzeydeki ilk böyle dize.
//! Ayı okunamayan satır (başlık yorumu, bozuk ya da birleşik kayıt) bir önceki geçerli satırın ayına gider; öncesinde geçerli satır
//! yoksa sonraki ilk geçerli satırın ayına; hiç yoksa yerel saatle bugünün ayına.

use std::io::Write;
use std::path::{Path, PathBuf};

use serde_json::Value;

use crate::py;

/// Ay çıkarılırken bakılan alanlar, öncelik sırasıyla.
pub const ZAMAN_ANAHTARLARI: &[&str] = &["ts", "ts_utc", "ts_bas", "tarih", "yuklendi_ts", "cekim_tarihi"];

/// `<ad>` sonundaki `.jsonl` atılır: `hareket-olay.jsonl` ile `hareket-olay` aynı kütüktür.
fn kok_ad(ad: &str) -> &str {
    ad.strip_suffix(".jsonl").unwrap_or(ad)
}

/// Kütük dizini: `<bronz>/<ad>/`.
pub fn dizin(bronz: &Path, ad: &str) -> PathBuf {
    bronz.join(kok_ad(ad))
}

/// Ay dosyası: `<bronz>/<ad>/<ay>.jsonl`.
pub fn ay_yolu(bronz: &Path, ad: &str, ay: &str) -> PathBuf {
    dizin(bronz, ad).join(format!("{ay}.jsonl"))
}

fn ay_onek(s: &str) -> Option<String> {
    let b = s.as_bytes();
    let rakam = |i: usize| b.get(i).is_some_and(u8::is_ascii_digit);
    if (0..4).all(rakam) && b.get(4) == Some(&b'-') && (5..7).all(rakam) {
        let ay: u32 = s[5..7].parse().ok()?;
        if (1..=12).contains(&ay) {
            return Some(s[..7].to_string());
        }
    }
    None
}

/// Bir satırın ayı (`YYYY-MM`); okunamazsa `None`.
pub fn satir_ayi(satir: &str) -> Option<String> {
    let Ok(Value::Object(m)) = serde_json::from_str::<Value>(satir.trim_end_matches(['\r', '\n'])) else { return None };
    for k in ZAMAN_ANAHTARLARI {
        if let Some(Value::String(s)) = m.get(*k)
            && let Some(ay) = ay_onek(s)
        {
            return Some(ay);
        }
    }
    m.values().find_map(|v| match v {
        Value::String(s) => ay_onek(s),
        _ => None,
    })
}

/// Satırları (satır sonları korunarak) aylara dağıtır; sıra korunur. Dönüş: ardışık (ay, metin) grupları.
pub fn aylara_bol(metin: &str, varsayilan_ay: &str) -> Vec<(String, String)> {
    let parcalar: Vec<&str> = metin.split_inclusive('\n').collect();
    let aylar: Vec<Option<String>> = parcalar.iter().map(|p| satir_ayi(p)).collect();
    let ilk_gecerli = aylar.iter().flatten().next().cloned().unwrap_or_else(|| varsayilan_ay.to_string());
    let mut gruplar: Vec<(String, String)> = Vec::new();
    let mut onceki: Option<String> = None;
    for (p, a) in parcalar.iter().zip(aylar) {
        let ay = a.or_else(|| onceki.clone()).unwrap_or_else(|| ilk_gecerli.clone());
        onceki = Some(ay.clone());
        match gruplar.last_mut() {
            Some((g, m)) if *g == ay => m.push_str(p),
            _ => gruplar.push((ay, (*p).to_string())),
        }
    }
    gruplar
}

/// Bugünün ayı (yerel saat).
pub fn bu_ay() -> String {
    chrono::Local::now().format("%Y-%m").to_string()
}

/// `metin`i (bir ya da çok satır, satır sonları dahil) ay dosyalarına ekler. Her ay grubu tek yazımla gider:
/// eşzamanlı hook süreçlerinde kayıtlar iç içe geçmez.
pub fn ekle(bronz: &Path, ad: &str, metin: &str) -> std::io::Result<()> {
    if metin.is_empty() {
        return Ok(());
    }
    std::fs::create_dir_all(dizin(bronz, ad))?;
    for (ay, parca) in aylara_bol(metin, &bu_ay()) {
        let mut f = std::fs::OpenOptions::new().create(true).append(true).open(ay_yolu(bronz, ad, &ay))?;
        f.write_all(parca.as_bytes())?;
    }
    Ok(())
}

/// Ay dosyaları, ad sırasıyla (`YYYY-MM.jsonl` ad sırası = zaman sırası).
pub fn ay_dosyalari(bronz: &Path, ad: &str) -> Vec<PathBuf> {
    let Ok(it) = std::fs::read_dir(dizin(bronz, ad)) else { return Vec::new() };
    let mut v: Vec<PathBuf> = it
        .flatten()
        .map(|e| e.path())
        .filter(|p| p.is_file() && p.file_name().and_then(|n| n.to_str()).is_some_and(|n| n.ends_with(".jsonl") && ay_onek(n).is_some()))
        .collect();
    v.sort();
    v
}

/// Kütükte en az bir ay dosyası var mı.
pub fn var_mi(bronz: &Path, ad: &str) -> bool {
    !ay_dosyalari(bronz, ad).is_empty()
}

/// Bütün ay dosyalarının birleşik baytı; ay dosyası yoksa `None`. Satır sonuyla bitmeyen dosyanın arkasına `\n` konur.
pub fn oku_bayt(bronz: &Path, ad: &str) -> std::io::Result<Option<Vec<u8>>> {
    let dosyalar = ay_dosyalari(bronz, ad);
    if dosyalar.is_empty() {
        return Ok(None);
    }
    let mut b = Vec::new();
    for d in dosyalar {
        let parca = std::fs::read(&d)?;
        let eksik = !parca.is_empty() && !parca.ends_with(b"\n");
        b.extend_from_slice(&parca);
        if eksik {
            b.push(b'\n');
        }
    }
    Ok(Some(b))
}

/// `py::oku_kati` karşılığı (katı UTF-8, evrensel satır sonu); ay dosyası yoksa `None`.
pub fn oku_kati(bronz: &Path, ad: &str) -> Option<Result<String, py::OkuHata>> {
    match oku_bayt(bronz, ad) {
        Ok(None) => None,
        Err(e) => Some(Err(py::OkuHata::Io(e))),
        Ok(Some(b)) => Some(String::from_utf8(b).map(|s| py::evrensel_satir(&s)).map_err(|_| py::OkuHata::Kod)),
    }
}

/// Toplam bayt (artımlı okuma durumunun "kütük dışarıdan değişti mi" denetimi için); ay dosyası yoksa `None`.
pub fn boyut(bronz: &Path, ad: &str) -> Option<u64> {
    let d = ay_dosyalari(bronz, ad);
    if d.is_empty() {
        return None;
    }
    Some(d.iter().filter_map(|p| std::fs::metadata(p).ok()).map(|m| m.len()).sum())
}

#[cfg(test)]
mod testler {
    use super::*;

    #[test]
    fn bolme_kurali() {
        let m = "# baslik\n{\"ts\": \"2026-08-31T23:00:00Z\"}\nbozuk\n{\"ts_utc\": \"2026-09-01T00:00:00Z\"}\n{\"x\": 1}\n";
        let g = aylara_bol(m, "2026-11");
        assert_eq!(g.len(), 2);
        assert_eq!(g[0], ("2026-08".into(), "# baslik\n{\"ts\": \"2026-08-31T23:00:00Z\"}\nbozuk\n".into()));
        assert_eq!(g[1], ("2026-09".into(), "{\"ts_utc\": \"2026-09-01T00:00:00Z\"}\n{\"x\": 1}\n".into()));
        assert_eq!(aylara_bol("{\"a\": 1}\n", "2026-11")[0].0, "2026-11");
        assert_eq!(satir_ayi("{\"oturum\": \"x\", \"cikti\": \"2026-10-05 not\"}"), Some("2026-10".into()));
    }
}
