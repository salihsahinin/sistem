//! `stop-buyuk-harf.sh` karşılığı: büyük-harf vurgu freni (Stop hook; `decision=block` JSON'u basar).
use crate::ortak::{Ortam, Sonuc, json_oku, py_dumps, py_truthy};
use regex::Regex;
use serde_json::{Value, json};
use std::collections::BTreeSet;

const IZ: &str = "AS-OF DAG MCP OWASP YAML JSON JSONL YML CSV HTML HTTP HTTPS PDF SVG PNG AXI GNHF OCR USD EUR IAM ASCII FTS BM25 RRF NLI XML
CI CD API SQL URL URI CLI GUI IDE SDK LLM RAG HITL ASR NDCG MAP MRR GSM8K SWE UK AISI AWS DEA GCP MIT OCW README HEAD MEMORY CLAUDE
JARVIS JARVİS FRIDAY CARVIS ATLAS OPUS SONNET HAIKU FABLE GPT KB MB GB TODO FIFO LIFO SHA UTC TR EN ID UID DNS TLS SSH OAUTH
NEMO NLP ML AI ETL ELT DBT SPARK MLOPS RAG LTR NDCG PR PRS CTR ROC AUC F1 REGEX BPE ROPE KV SFT MDL CRLF LF RLHF CVE CVSS CWE OWASP UTF
İB KB-08 EK SKILL SCRIPTLER KILAVUZ MECE WSL CTE PATH OMP LSP NYC";

fn kelime(c: char) -> bool {
    c.is_alphanumeric() || c == '_'
}
fn yasak_komsu(c: char) -> bool {
    kelime(c) || c == '.' || c == '/' || c == '-'
}
fn buyuk(c: char) -> bool {
    c.is_ascii_uppercase() || "ÇĞİÖŞÜ".contains(c)
}

/// `(?<![\w./-])[A-ZÇĞİÖŞÜ]{3,}(?![\w./-])`
fn adaylar(metin: &str) -> Vec<String> {
    let c: Vec<char> = metin.chars().collect();
    let n = c.len();
    let mut cikti = vec![];
    let mut i = 0;
    while i < n {
        if buyuk(c[i]) && (i == 0 || !yasak_komsu(c[i - 1])) {
            let mut j = i;
            while j < n && buyuk(c[j]) {
                j += 1;
            }
            if j - i >= 3 && (j == n || !yasak_komsu(c[j])) {
                cikti.push(c[i..j].iter().collect());
            }
            i = j.max(i + 1);
        } else {
            i += 1;
        }
    }
    cikti
}

fn arac_metni(v: &str) -> String {
    let stil = Regex::new(r"(?s)<style.*?</style>").unwrap();
    let etiket = Regex::new(r"<[^>]+>").unwrap();
    let ent = Regex::new(r"&[a-z]+;|&#\d+;").unwrap();
    let v = stil.replace_all(v, " ");
    let v = etiket.replace_all(&v, " ");
    ent.replace_all(&v, " ").into_owned()
}

pub fn kos(o: &Ortam) -> Sonuc {
    let mut s = Sonuc::bos();
    let Some(Value::Object(d)) = json_oku(&o.stdin_metin()) else {
        s.hata = "JSONDecodeError: girdi okunamadı\n".into();
        s.kod = 1;
        return s;
    };
    if d.get("stop_hook_active").is_some_and(py_truthy) {
        return s;
    }
    let mut son: Option<String> = match d.get("last_assistant_message") {
        Some(Value::String(x)) if !x.is_empty() => Some(x.clone()),
        _ => None,
    };
    let tp = d.get("transcript_path").and_then(Value::as_str).filter(|x| !x.is_empty()).map(std::path::PathBuf::from);
    let tp_var = tp.as_ref().is_some_and(|p| p.exists());
    if son.is_none() && !tp_var {
        return s;
    }
    let mut arac_metin: Vec<String> = vec![];
    if let (Some(tp), true) = (&tp, tp_var) {
        let ham = std::fs::read(tp).unwrap_or_default();
        let ham = String::from_utf8_lossy(&ham).into_owned();
        let mut tur: Vec<Value> = vec![];
        for satir in ham.lines() {
            let Ok(Value::Object(r)) = serde_json::from_str::<Value>(satir) else { continue };
            match r.get("type").and_then(Value::as_str) {
                Some("user") => tur.clear(),
                Some("assistant") => tur.push(r.get("message").cloned().unwrap_or(json!({}))),
                _ => {}
            }
        }
        for m in &tur {
            let Some(icerik) = m.get("content").and_then(Value::as_array) else { continue };
            for c in icerik {
                let tip = c.get("type").and_then(Value::as_str);
                if tip == Some("text") {
                    let t = c.get("text").and_then(Value::as_str).unwrap_or("");
                    if !t.trim().is_empty() && son.is_none() {
                        son = Some(t.to_string());
                    }
                }
                if tip == Some("tool_use") {
                    let alan = match c.get("name").and_then(Value::as_str) {
                        Some("mcp__visualize__show_widget") => "widget_code",
                        Some("Write") => "content",
                        Some("Edit") => "new_string",
                        _ => continue,
                    };
                    if let Some(Value::String(v)) = c.get("input").and_then(|i| i.get(alan))
                        && !v.trim().is_empty()
                    {
                        arac_metin.push(arac_metni(v));
                    }
                }
            }
        }
    }
    if son.as_deref().is_none_or(str::is_empty) && arac_metin.is_empty() {
        return s;
    }
    let iz: BTreeSet<&str> = IZ.split_whitespace().collect();
    let kod_blok = Regex::new(r"(?s)```.*?```").unwrap();
    let metin = kod_blok.replace_all(son.as_deref().unwrap_or(""), " ").into_owned();
    let metin = format!("{metin} {}", arac_metin.join(" "));
    let satir_ici = Regex::new(r"`[^`\n]*`").unwrap();
    let metin = satir_ici.replace_all(&metin, " ").into_owned();
    let aynen = Regex::new("aynen:\\s*[\"\u{201c}][^\"\u{201d}]*[\"\u{201d}]").unwrap();
    let metin = aynen.replace_all(&metin, " ").into_owned();
    let url = Regex::new(r"https?://\S+").unwrap();
    let metin = url.replace_all(&metin, " ").into_owned();
    let ihlal: BTreeSet<String> = adaylar(&metin).into_iter().filter(|w| !iz.contains(w.as_str())).collect();
    if ihlal.is_empty() {
        return s;
    }
    let liste: Vec<&String> = ihlal.iter().collect();
    let kisa: Vec<&str> = liste.iter().take(12).map(|x| x.as_str()).collect();
    let neden = format!(
        "Büyük-harf vurgu freni (Salih 09-15; v0.3 09-17 araç girdileri dahil): son turda (cevap ya da widget/dosya içeriği) tamamı büyük harfle yazılmış sözcük var: {}{}. Vurguyu kalın harfle (**sözcük**) ya da cümle yapısıyla ver; büyük harf yalnız kısaltma/durum-sözcüğü. Cevabı YENİDEN YAZMA (09-15 arızası: tam yeniden yazım Salih'e aynı soruyu iki kez gösterdi); yalnız tek satır ekle: 'Düzeltme: <SÖZCÜK> → **sözcük**' ve dur.",
        kisa.join(", "),
        if liste.len() > 12 { " …" } else { "" }
    );
    s.satir(&py_dumps(&json!({"decision": "block", "reason": neden})));
    s
}
