//! `pretool-core-tel.sh` karşılığı: Bash ile core/ · CLAUDE.md · .claude/ yazımı tökezleme-teli (çıkış 2 = engel).
//! grep -E satır başına çalışır ve bu makinede C yerelinde (ASCII `\b`, `[[:alpha:]]`, bayt `.`) davranır; bu yüzden
//! bayt düzeyinde ASCII regex kullanılır.
use crate::ortak::{Ortam, Sonuc, py_str, sondaki_nl_sil};
use regex::bytes::Regex;
use serde_json::Value;

const PROT: &str = r"(core/|CLAUDE\.md|\.claude/)";

fn desenler() -> Vec<Regex> {
    let r = |s: String| Regex::new(&format!("(?-u){s}")).expect("regex");
    vec![
        r(r#">{1,2}[[:space:]]*"?\.?/?(core/|CLAUDE\.md|\.claude/)"#.to_string()),
        r(format!(r"\b(mv|cp|rm|touch|truncate|tee|dd|install)\b.*{PROT}")),
        r(format!(r"\b(sed|perl)\b[^|;&]*[[:space:]]-[[:alpha:]]*i[^|;&]*{PROT}")),
        r(format!(r"\bgit[[:space:]]+(checkout|restore|reset|clean|rm|mv)\b.*{PROT}")),
    ]
}

fn komut_cikar(girdi: &str) -> String {
    let v: Option<Value> = serde_json::from_str(girdi).ok();
    let cmd = v
        .as_ref()
        .and_then(|v| v.as_object())
        .and_then(|d| match d.get("tool_input") {
            None => Some(None),
            Some(Value::Object(ti)) => Some(ti.get("command")),
            Some(_) => None, // .get çağrısı patlar -> boş
        })
        .map(|c| match c {
            None => String::new(),
            Some(c) => py_str(c),
        })
        .unwrap_or_default();
    sondaki_nl_sil(&cmd).to_string()
}

pub fn kos(o: &Ortam) -> Sonuc {
    let girdi = o.stdin_metin();
    let girdi = sondaki_nl_sil(&girdi).to_string();
    let mut cmd = komut_cikar(&girdi);
    if cmd.is_empty() {
        cmd = girdi;
    }
    let desen = desenler();
    let engel = cmd.split('\n').any(|satir| desen.iter().any(|d| d.is_match(satir.as_bytes())));
    let mut s = Sonuc::bos();
    if engel {
        s.hata = format!(
            "TEL (m.41 kilit): Bash ile core/ · CLAUDE.md · .claude/ yazımı bu yüzeyde engellidir. Bu bir tökezleme-telidir; iş meşruysa ana-sıra(Cowork/Fable) ya da Salih eliyle yapılır. Komut: {cmd}\n"
        );
        s.kod = 2;
    }
    s
}
