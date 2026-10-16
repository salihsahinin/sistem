//! `tools/hafiza-ayna.py` karşılığı: harness oto-hafıza aynası (Karar 104 M3). `~/.claude/projects/<anahtar>/memory/` dizinini
//! `veri/hafiza-ayna/<anahtar>/` altına deterministik kopyalar + `MANIFEST.json`; kaynak salt-okur, kaynakta silinen dosya aynada kalır (m.8).
//! Çıkış: 0 ayna güncel/güncellendi · 2 kaynak dizin yok · 3 kaynakta-yok dosya var (bilgi; engel değil).
use crate::argparse::{Ayrisan, Secenek};
use crate::{harness_anahtar, py};
use chrono::{Local, TimeZone};
use serde_json::{Map, Value, json};
use sha2::{Digest, Sha256};
use std::path::Path;
use std::time::UNIX_EPOCH;

const BELGE: &str = include_str!("belge/ayna.txt");

/// Aynanın KANONİK dizin adı (Karar 104 M3 hükmündeki ad); makine anahtarı değişse de (Windows `C--sistem-sistem`) tek ayna dizini.
const AYNA_ADI: &str = "-Users-HasanSalihSahin-sistem";

fn ayrisan() -> Ayrisan {
    Ayrisan::yeni(
        "hafiza-ayna.py",
        Some(BELGE),
        vec![
            Secenek::ekle(&["--anahtar"], "anahtar", Some("proje anahtarı (tekrarlanabilir)")),
            Secenek::bayrak(&["--kuru"], "kuru", Some("yazma; yalnız fark raporu")),
            Secenek::bayrak(&["--json"], "json", None),
            Secenek::deger(&["--repo"], "repo", None),
        ],
    )
}

fn sha256(yol: &Path) -> std::io::Result<String> {
    let mut h = Sha256::new();
    std::io::copy(&mut std::fs::File::open(yol)?, &mut h)?;
    Ok(h.finalize().iter().map(|b| format!("{b:02x}")).collect())
}

/// `datetime.fromtimestamp(st_mtime).isoformat(timespec="seconds")` (yerel saat; mikrosaniye yarı-çifte yuvarlanır, saniyeye kırpılır).
fn mtime_metni(m: std::time::SystemTime) -> String {
    let d = m.duration_since(UNIX_EPOCH).unwrap_or_default();
    let f = d.as_secs() as f64 + f64::from(d.subsec_nanos()) * 1e-9;
    let (tam, kesir) = (f.trunc(), f.fract());
    let ms = kesir * 1e6;
    let (alt, kalan) = (ms.floor(), ms - ms.floor());
    let us = if kalan > 0.5 || (kalan == 0.5 && (alt as i64) % 2 == 1) { alt as i64 + 1 } else { alt as i64 };
    let sn = tam as i64 + i64::from(us >= 1_000_000);
    match Local.timestamp_opt(sn, 0).single() {
        Some(t) => t.format("%Y-%m-%dT%H:%M:%S").to_string(),
        None => String::new(),
    }
}

type Hata = String;

/// `eski` manifest: ad -> kayıt (Python sözlüğü gibi: yinelenen ad son değeri alır, ilk konumu korur).
fn eski_oku(yol: &str) -> Result<Map<String, Value>, Hata> {
    let eski = Map::new();
    let Ok(t) = std::fs::read_to_string(yol) else { return Ok(eski) };
    let Ok(v) = serde_json::from_str::<Value>(&t) else { return Ok(eski) };
    let Some(o) = v.as_object() else { return Err("MANIFEST.json kökü nesne değil (Python: AttributeError)".into()) };
    let liste = match o.get("dosyalar") {
        None => return Ok(eski),
        Some(Value::Array(l)) => l,
        Some(_) => return Err("MANIFEST.json `dosyalar` liste değil (Python: TypeError)".into()),
    };
    let mut yeni = Map::new();
    for d in liste {
        let Some(d) = d.as_object() else { return Err("MANIFEST.json `dosyalar` öğesi nesne değil (Python: TypeError)".into()) };
        let Some(ad) = d.get("ad") else { return Ok(eski) }; // KeyError yakalanır
        let Some(ad) = ad.as_str() else { return Err("MANIFEST.json `ad` metin değil".into()) };
        yeni.insert(ad.to_string(), Value::Object(d.clone()));
    }
    Ok(yeni)
}

fn ayna(anahtar: &str, repo: &str, kuru: bool, hedef_ad: Option<&str>) -> Result<Value, Hata> {
    let kaynak = py::expanduser(&format!("~/.claude/projects/{anahtar}/memory"));
    let hedef = py::join(&py::join(&py::join(repo, "veri"), "hafiza-ayna"), hedef_ad.unwrap_or(anahtar));
    if !Path::new(&kaynak).is_dir() {
        return Ok(json!({"anahtar": anahtar, "durum": "KAYNAK-YOK", "kaynak": kaynak}));
    }
    let manifest_yolu = py::join(&hedef, "MANIFEST.json");
    let eski = if Path::new(&manifest_yolu).exists() { eski_oku(&manifest_yolu)? } else { Map::new() };
    let (mut yeni, mut degisen, mut ayni) = (0, 0, 0);
    let mut dosyalar: Vec<Map<String, Value>> = vec![];
    let mut kaynaktakiler: Vec<String> = std::fs::read_dir(&kaynak)
        .map_err(|e| format!("{kaynak}: {e}"))?
        .flatten()
        .filter(|e| e.path().is_file())
        .map(|e| e.file_name().to_string_lossy().into_owned())
        .filter(|n| !n.starts_with('.'))
        .collect();
    kaynaktakiler.sort();
    for ad in &kaynaktakiler {
        let ky = py::join(&kaynak, ad);
        let sh = sha256(Path::new(&ky)).map_err(|e| format!("{ky}: {e}"))?;
        let st = std::fs::metadata(&ky).map_err(|e| format!("{ky}: {e}"))?;
        let mut kayit = Map::new();
        kayit.insert("ad".into(), json!(ad));
        kayit.insert("sha256".into(), json!(sh));
        kayit.insert("bayt".into(), json!(st.len()));
        kayit.insert("kaynak_mtime".into(), json!(mtime_metni(st.modified().map_err(|e| e.to_string())?)));
        kayit.insert("durum".into(), json!("ayna"));
        match eski.get(ad) {
            None => yeni += 1,
            Some(o) if o.get("sha256") != Some(&json!(sh)) => degisen += 1,
            Some(_) => ayni += 1,
        }
        if !kuru {
            std::fs::create_dir_all(&hedef).map_err(|e| format!("{hedef}: {e}"))?;
            std::fs::copy(&ky, py::join(&hedef, ad)).map_err(|e| format!("{ky}: {e}"))?;
        }
        dosyalar.push(kayit);
    }
    let mut kaynakta_yok: Vec<String> = vec![];
    let mut sirali: Vec<(&String, &Value)> = eski.iter().collect();
    sirali.sort_by(|a, b| a.0.cmp(b.0));
    for (ad, onceki) in sirali {
        if !kaynaktakiler.contains(ad) {
            let mut k = onceki.as_object().cloned().unwrap_or_default();
            k.insert("durum".into(), json!("kaynakta-yok"));
            if !k.contains_key("kaynakta_yok_tespit") {
                k.insert("kaynakta_yok_tespit".into(), json!(jarvis_hook::ortak::bugun_yerel()));
            }
            dosyalar.push(k);
            kaynakta_yok.push(ad.clone());
        }
    }
    dosyalar.sort_by(|a, b| a["ad"].as_str().cmp(&b["ad"].as_str()));
    if !kuru {
        let m = json!({
            "anahtar": anahtar, "kaynak": kaynak, "uretim": jarvis_hook::ortak::bugun_yerel(), "karar": "Karar 104 M3 (2026-09-20)",
            "dosya_sayisi": kaynaktakiler.len(), "kaynakta_yok": kaynakta_yok, "dosyalar": dosyalar,
        });
        std::fs::create_dir_all(&hedef).map_err(|e| format!("{hedef}: {e}"))?;
        std::fs::write(&manifest_yolu, format!("{}\n", py::json_girintili(&m))).map_err(|e| format!("{manifest_yolu}: {e}"))?;
    }
    let goreli = py::relpath(&hedef, repo).map_err(|e| format!("relpath: {e}"))?;
    Ok(json!({
        "anahtar": anahtar, "durum": if yeni > 0 || degisen > 0 { "GÜNCELLENDİ" } else { "GÜNCEL" }, "kaynak": kaynak, "hedef": goreli,
        "dosya": kaynaktakiler.len(), "yeni": yeni, "degisen": degisen, "ayni": ayni, "kaynakta_yok": kaynakta_yok,
    }))
}

pub fn kos(argv: &[String]) -> i32 {
    let a = match ayrisan().ayristir(argv) {
        Ok(a) => a,
        Err(k) => return k,
    };
    let repo = a.metin("repo").map(String::from).unwrap_or_else(harness_anahtar::jarvis);
    let kuru = a.bayrak("kuru");
    let kok = harness_anahtar::kok_anahtar();
    let anahtarlar: Vec<String> = a.liste("anahtar").filter(|l| !l.is_empty()).cloned().unwrap_or_else(|| vec![kok.clone()]);
    let mut sonuc: Vec<Value> = vec![];
    for k in &anahtarlar {
        match ayna(k, &repo, kuru, if *k == kok { Some(AYNA_ADI) } else { None }) {
            Ok(s) => sonuc.push(s),
            Err(e) => return py::coker(&e),
        }
    }
    if a.bayrak("json") {
        py::print(&py::json_girintili(&Value::Array(sonuc.clone())));
    } else {
        py::print("HAFIZA-AYNA (Karar 104 M3; kaynak salt-okur, m.8 silme yok):");
        for s in &sonuc {
            let t = |k: &str| s[k].as_str().unwrap_or("").to_string();
            if s["durum"] == "KAYNAK-YOK" {
                py::print(&format!("  [YOK ] {} — {}", t("anahtar"), t("kaynak")));
                continue;
            }
            let yok: Vec<&str> = s["kaynakta_yok"].as_array().into_iter().flatten().filter_map(Value::as_str).collect();
            py::print(&format!(
                "  [{}] {} → {} · dosya {} (yeni {} · değişen {} · aynı {}){}{}",
                t("durum"),
                t("anahtar"),
                t("hedef"),
                s["dosya"],
                s["yeni"],
                s["degisen"],
                s["ayni"],
                if yok.is_empty() { String::new() } else { format!(" · kaynakta-yok {}: {}", yok.len(), yok.join(", ")) },
                if kuru { " · KURU" } else { "" }
            ));
        }
    }
    if sonuc.iter().any(|s| s["durum"] == "KAYNAK-YOK") {
        return 2;
    }
    if sonuc.iter().any(|s| s["kaynakta_yok"].as_array().is_some_and(|l| !l.is_empty())) { 3 } else { 0 }
}
