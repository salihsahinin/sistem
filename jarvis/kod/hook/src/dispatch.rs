//! `bin/hook-dispatch.sh` karşılığı: kök tek hook girişi. Oturum cwd'sinden ajanı bulur, ajanın KENDİ
//! `.claude/settings.json` içindeki `hooks[<olay>]` komutlarını sırayla koşturur (mini hook-koşucu).
//! Çıkış: bir komut 2 dönerse 2 (stderr aynen), aksi hâlde ilk sıfır olmayan kod, yoksa 0; stdout'lar birleştirilir.
use crate::ortak::{Ortam, Sonuc, json_oku, realpath, sep, sondaki_nl_sil};
use regex::Regex;
use serde_json::Value;
use std::io::Write;
use std::path::{Path, PathBuf};
use std::process::{Command, Stdio};

fn rp(s: &str) -> PathBuf {
    if s.is_empty() {
        realpath(&std::env::current_dir().unwrap_or_default())
    } else {
        realpath(Path::new(s))
    }
}

pub fn kos(olay: &str, o: &Ortam) -> Sonuc {
    let mut s = Sonuc::bos();
    let girdi_ham = o.stdin_metin();
    let girdi = sondaki_nl_sil(&girdi_ham).to_string();
    let g: Value = if girdi.trim().is_empty() { Value::Object(Default::default()) } else { json_oku(&girdi).unwrap_or(Value::Object(Default::default())) };
    let cwd_ham = g.get("cwd").and_then(Value::as_str).unwrap_or("").to_string();
    let cwd = rp(&cwd_ham).to_string_lossy().into_owned();
    let kok = realpath(&o.repo).to_string_lossy().into_owned();
    let on = format!("{kok}{}", sep());
    if !cwd.starts_with(&on) {
        return s;
    }
    let ajan = cwd[on.len()..].split(sep()).next().unwrap_or("").to_string();
    let ajan_dir = PathBuf::from(&kok).join(&ajan);
    let proje = o.env("CLAUDE_PROJECT_DIR").unwrap_or("");
    if rp(proje) == realpath(&ajan_dir) {
        return s; // çift-koşum freni: harness ajanın kendi ayarını zaten yükledi
    }
    let ayar = ajan_dir.join(".claude").join("settings.json");
    let Some(ayar_v) = std::fs::read_to_string(&ayar).ok().and_then(|t| json_oku(&t)) else { return s };
    let kayitlar = ayar_v.get("hooks").and_then(|h| h.get(olay)).and_then(Value::as_array).cloned().unwrap_or_default();
    let arac = g.get("tool_name").and_then(Value::as_str).unwrap_or("");
    let mut kod = 0;
    for k in kayitlar {
        let m = k.get("matcher").and_then(Value::as_str).unwrap_or("");
        if !m.is_empty() && !arac.is_empty() {
            let ok = Regex::new(&format!("^(?:{m})$")).map(|r| r.is_match(arac)).unwrap_or(false);
            if !ok {
                continue;
            }
        }
        for h in k.get("hooks").and_then(Value::as_array).cloned().unwrap_or_default() {
            if h.get("type").and_then(Value::as_str) != Some("command") {
                continue;
            }
            let komut = h.get("command").and_then(Value::as_str).unwrap_or("");
            let mut cocuk = match Command::new("bash")
                .arg("-c")
                .arg(komut)
                .current_dir(&ajan_dir)
                .env("CLAUDE_PROJECT_DIR", &ajan_dir)
                .env("SISTEM_KOK", &kok)
                .env("SISTEM_AJAN", &ajan)
                .stdin(Stdio::piped())
                .stdout(Stdio::piped())
                .stderr(Stdio::piped())
                .spawn()
            {
                Ok(c) => c,
                Err(e) => {
                    s.hata.push_str(&format!("bash başlatılamadı: {e}\n"));
                    kod = if kod == 0 { 127 } else { kod };
                    continue;
                }
            };
            if let Some(mut si) = cocuk.stdin.take() {
                let gonder = girdi.clone().into_bytes();
                std::thread::spawn(move || {
                    let _ = si.write_all(&gonder);
                });
            }
            let r = cocuk.wait_with_output();
            let Ok(r) = r else { continue };
            s.cikti.extend_from_slice(&r.stdout);
            s.hata.push_str(&String::from_utf8_lossy(&r.stderr));
            let rc = r.status.code().unwrap_or(1);
            if rc == 2 {
                s.kod = 2;
                return s;
            }
            if kod == 0 {
                kod = rc;
            }
        }
    }
    s.kod = kod;
    s
}
