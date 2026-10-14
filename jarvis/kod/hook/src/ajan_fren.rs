//! `pretool-ajan-fren.sh` karşılığı: Agent çağrısı sayacı, UYARI/DURDUR eşikleri (çıkış 2 = engel).
use crate::ortak::{Ortam, Sonuc, ilk_n, py_dumps, ts_istanbul, ekle_satir, json_oku};
use serde_json::{Map, Value, json};

const REJIM: &str = "manuel-tempo · kota-bol · ekonomi -%30 (08-15) · AS-OF 2026-08-29";

pub fn kos(o: &Ortam) -> Sonuc {
    let mut s = Sonuc::bos();
    let Some(Value::Object(g)) = json_oku(&o.stdin_metin()) else { return s };
    let arac = g.get("tool_name").and_then(Value::as_str).unwrap_or("");
    if arac != "Agent" && arac != "Task" {
        return s;
    }
    let tamsayi = |ad: &str, vars: i64| -> Result<i64, ()> {
        match o.env(ad) {
            None => Ok(vars),
            Some(v) => v.trim().parse::<i64>().map_err(|_| ()),
        }
    };
    let (Ok(uyari), Ok(durdur)) = (tamsayi("JARVIS_FREN_UYARI", 72), tamsayi("JARVIS_FREN_DURDUR", 144)) else {
        s.hata = "ValueError: invalid literal for int() with base 10\n".into();
        s.kod = 1;
        return s;
    };
    let kapali = o.env("JARVIS_FREN_KAPALI").unwrap_or("0") == "1";
    let sid_ham = match g.get("session_id") {
        Some(Value::String(x)) if !x.is_empty() => x.clone(),
        _ => "oturum".to_string(),
    };
    let sid = ilk_n(&sid_ham, 36);
    let sd = o.repo.join(".claude").join("hooks").join("state");
    let _ = std::fs::create_dir_all(&sd);
    let syol = sd.join(format!("ajan-fren-{sid}.json"));
    let (mut sayac, mut uyari_yazildi) = (0i64, false);
    if let Some(Value::Object(st)) = std::fs::read_to_string(&syol).ok().and_then(|t| json_oku(&t)) {
        sayac = st.get("sayac").and_then(Value::as_i64).unwrap_or(0);
        uyari_yazildi = st.get("uyari_yazildi").and_then(Value::as_bool).unwrap_or(false);
    }
    sayac += 1;
    let n = sayac;
    let aciklama = g
        .get("tool_input")
        .and_then(|t| t.get("description"))
        .and_then(Value::as_str)
        .map(|d| ilk_n(d, 80))
        .unwrap_or_default();
    let ts = ts_istanbul();
    let olay = |tur: &str, mesaj: &str| {
        let mut m = Map::new();
        for (k, v) in [
            ("ts", json!(ts)), ("session_id", json!(sid)), ("arac", g.get("tool_name").cloned().unwrap_or(Value::Null)),
            ("sayac", json!(n)), ("esik_uyari", json!(uyari)), ("esik_durdur", json!(durdur)), ("olay", json!(tur)),
            ("aciklama", json!(aciklama)), ("rejim", json!(REJIM)), ("mesaj", json!(mesaj)),
            ("kaynak", json!("pretool-ajan-fren.sh")),
        ] {
            m.insert(k.into(), v);
        }
        let _ = ekle_satir(&o.repo.join("veri").join("bronz").join("fren-olay.jsonl"), &py_dumps(&Value::Object(m)));
    };
    let durum_yaz = |uy: bool| {
        let v = json!({"sayac": n, "uyari_yazildi": uy});
        let _ = std::fs::write(&syol, py_dumps(&v));
    };
    if n >= durdur {
        if kapali {
            olay("ASILDI-KAPALI", "JARVIS_FREN_KAPALI=1 (Salih beyanı) — engel kaldırıldı, kayıt düşüldü");
        } else {
            olay("DURDUR", "Agent çağrısı engellendi");
            durum_yaz(uyari_yazildi);
            s.hata = format!(
                "AJAN FRENİ (İB-54, Karar 39 uç-eşik): bu oturumda {n}. Agent çağrısı — DURDUR eşiği {durdur} (UYARI {uyari}; taban ajan/wf p50 12, max 23). Fan-out aşırı uç sınıfta: önce ölç (veri/bronz/fren-olay.jsonl), gerekçeli devam için Salih beyanı → JARVIS_FREN_KAPALI=1 ya da eşik revizyonu. Rejim: {REJIM}\n"
            );
            s.kod = 2;
            return s;
        }
    } else if n >= uyari && !uyari_yazildi {
        uyari_yazildi = true;
        olay("UYARI", "uyarı eşiği geçildi (engel yok)");
    }
    durum_yaz(uyari_yazildi);
    s
}
