//! `instructions-loaded.sh` karşılığı: InstructionsLoaded olayını `veri/bronz/talimat-yukleme-olay.jsonl`e kütükler (çıkış hep 0).
use crate::ortak::{Ortam, Sonuc, ekle_satir, ilk_n, json_oku, py_dumps, py_or, ts_utc};
use serde_json::{Map, Value, json};

pub fn kos(o: &Ortam) -> Sonuc {
    let s = Sonuc::bos();
    let metin = o.stdin_metin();
    let d: Map<String, Value> = match json_oku(&metin) {
        Some(Value::Object(m)) => m,
        Some(_) => return s, // Python: .get patlar, betik yine 0 çıkar
        None => {
            let mut m = Map::new();
            m.insert("ham".into(), json!(ilk_n(&metin, 2000)));
            m
        }
    };
    let mut anahtarlar: Vec<&String> = d.keys().collect();
    anahtarlar.sort();
    let get = |k: &str| d.get(k).cloned().unwrap_or(Value::Null);
    let mut kayit = Map::new();
    kayit.insert("ts_utc".into(), json!(ts_utc()));
    kayit.insert("session_id".into(), get("session_id"));
    kayit.insert("olay".into(), d.get("hook_event_name").cloned().unwrap_or(json!("InstructionsLoaded")));
    kayit.insert("neden".into(), py_or(&d, &["load_reason", "reason", "matcher"]));
    kayit.insert("dosya".into(), py_or(&d, &["file_path", "path", "file"]));
    kayit.insert("cwd".into(), get("cwd"));
    kayit.insert("ham_alanlar".into(), json!(anahtarlar));
    let yol = o.repo.join("veri").join("bronz").join("talimat-yukleme-olay.jsonl");
    let _ = ekle_satir(&yol, &py_dumps(&Value::Object(kayit)));
    s
}
