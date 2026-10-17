//! `posttool-read-genislet`: PostToolUse(Read) hook'u (Karar 117 mekanizma 1a, okuma rejimi).
//! `Read` `@yol` satırlarını açmaz; bu hook okunan md dosyası içe aktarma taşıyorsa içe aktarılan blokları
//! otomatik yükleme sırasıyla (`jarvis_baglam::genislet`, ebeveyn → çocuklar pre-order) `additionalContext`
//! olarak araç sonucunun hemen ardına ekler. Ölçüm 2026-10-17: ek bağlam modele Read sonucundan sonra ulaşır.
//! Kısmi okumada (offset/limit dosya sonuna varmıyorsa) eklemez. Büyük çıktıda (> `SINIR`) yalnız sıralı dosya
//! listesini verir. Hiçbir şeyi engellemez; çıkış 0.
use crate::{Ortam, Sonuc};
use serde_json::{Value, json};
use std::path::Path;

const SINIR: usize = 9000;

pub fn kos(o: &Ortam) -> Sonuc {
    let bos = Sonuc { cikti: vec![], hata: String::new(), kod: 0 };
    let Ok(d) = serde_json::from_slice::<Value>(&o.stdin) else { return bos };
    if d.get("tool_name").and_then(Value::as_str) != Some("Read") {
        return bos;
    }
    let girdi = d.get("tool_input").cloned().unwrap_or(Value::Null);
    let Some(yol) = girdi.get("file_path").and_then(Value::as_str) else { return bos };
    let dosya = Path::new(yol);
    if dosya.extension().and_then(|e| e.to_str()) != Some("md") {
        return bos;
    }
    let Ok(metin) = std::fs::read_to_string(dosya) else { return bos };
    if jarvis_baglam::ice_aktarmalar(&metin).is_empty() {
        return bos;
    }
    if let Some(limit) = girdi.get("limit").and_then(Value::as_u64) {
        let bas = girdi.get("offset").and_then(Value::as_u64).unwrap_or(1).max(1);
        if bas + limit <= metin.lines().count() as u64 {
            return bos;
        }
    }
    let Ok((bloklar, _)) = jarvis_baglam::genislet(dosya) else { return bos };
    if bloklar.len() < 2 {
        return bos;
    }
    let kok = jarvis_baglam::coz(Path::new("."), &o.repo.to_string_lossy());
    let goreli = |p: &Path| p.strip_prefix(&kok).unwrap_or(p).to_string_lossy().replace('\\', "/");
    let mut ek = format!("[baglam-genislet] {} içe aktarmaları, yükleme sırasıyla (Karar 117):\n\n", goreli(dosya));
    let govde: String = bloklar[1..]
        .iter()
        .map(|b| format!("Contents of {}:\n\n{}\n\n", goreli(&b.yol), b.metin.trim_end()))
        .collect();
    if govde.chars().count() <= SINIR {
        ek.push_str(&govde);
    } else {
        ek.push_str("Ek bağlam sınırı aşıldı; bu dosyaları bu sırayla Read ile oku:\n");
        for (i, b) in bloklar[1..].iter().enumerate() {
            ek.push_str(&format!("{}. {}\n", i + 1, goreli(&b.yol)));
        }
    }
    let cikti = json!({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": ek}});
    Sonuc { cikti: cikti.to_string().into_bytes(), hata: String::new(), kod: 0 }
}
