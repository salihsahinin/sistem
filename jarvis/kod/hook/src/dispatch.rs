//! `bin/hook-dispatch.sh` karşılığı: kök tek hook girişi. Oturum cwd'sinden ajanı bulur, ajanın KENDİ
//! `.claude/settings.json` içindeki `hooks[<olay>]` komutlarını sırayla koşturur (mini hook-koşucu).
//! Çıkış: bir komut 2 dönerse 2 (stderr aynen), aksi hâlde ilk sıfır olmayan kod, yoksa 0; stdout'lar birleştirilir.
//! Karar 130: D22 (b) ajan dışı cwd'de çocuksuz erken çıkış, D22 (c) çocuk zaman aşımı, A3 ajan deny/ask eşleme (`izin`, anahtarlı).
use crate::izin;
use crate::ortak::{Ortam, Sonuc, ev_dizini, json_oku, realpath, sep, sondaki_nl_sil};
use regex::Regex;
use serde_json::Value;
use std::io::{Read, Write};
use std::path::{Path, PathBuf};
use std::process::{Child, Command, Stdio};
use std::sync::mpsc;
use std::time::{Duration, Instant};

fn rp(s: &str) -> PathBuf {
    if s.is_empty() {
        realpath(&std::env::current_dir().unwrap_or_default())
    } else {
        realpath(Path::new(s))
    }
}

/// Claude Code matcher kuralı: boş ya da `*` = hepsi; aksi hâlde tam eşleşen regex.
fn matcher_uyar(m: &str, arac: &str) -> bool {
    if m.is_empty() || m == "*" || arac.is_empty() {
        return true;
    }
    Regex::new(&format!("^(?:{m})$")).map(|r| r.is_match(arac)).unwrap_or(false)
}

/// Kilit olayı: çocuk zaman aşımı işlemi keser (PreToolUse); diğer olaylarda uyarıp geçer.
fn kilit_olayi(olay: &str) -> bool {
    olay == "PreToolUse"
}

/// Çocuk zaman aşımı (sn): hook kaydının `timeout` alanı > `JARVIS_DISPATCH_ZAMAN_ASIMI` > 10.
fn zaman_asimi(h: &Value, o: &Ortam) -> Duration {
    let sn = h
        .get("timeout")
        .and_then(Value::as_f64)
        .or_else(|| o.env("JARVIS_DISPATCH_ZAMAN_ASIMI").and_then(|x| x.parse::<f64>().ok()))
        .filter(|x| *x > 0.0)
        .unwrap_or(10.0);
    Duration::from_secs_f64(sn)
}

/// Çocuğu sınırlı süre bekle; aşımda öldür. Dönüş: (çıkış kodu, aşım oldu mu, stdout, stderr).
/// Boru okuyucuları ayrı iş parçacığında; aşımda torun süreç boruyu tutabileceği için okuyucu en çok 200 ms beklenir.
fn sinirli_bekle(mut c: Child, sure: Duration) -> (i32, bool, Vec<u8>, Vec<u8>) {
    fn okuyucu<R: Read + Send + 'static>(r: Option<R>) -> mpsc::Receiver<Vec<u8>> {
        let (tx, rx) = mpsc::channel();
        std::thread::spawn(move || {
            let mut b = Vec::new();
            if let Some(mut r) = r {
                let _ = r.read_to_end(&mut b);
            }
            let _ = tx.send(b);
        });
        rx
    }
    let out = okuyucu(c.stdout.take());
    let err = okuyucu(c.stderr.take());
    let son = Instant::now() + sure;
    let (kod, asim) = loop {
        match c.try_wait() {
            Ok(Some(st)) => break (st.code().unwrap_or(1), false),
            Ok(None) if Instant::now() >= son => {
                let _ = c.kill();
                let _ = c.wait();
                break (124, true);
            }
            Ok(None) => std::thread::sleep(Duration::from_millis(5)),
            Err(_) => break (1, false),
        }
    };
    let bekle = if asim { Duration::from_millis(200) } else { Duration::from_secs(5) };
    (kod, asim, out.recv_timeout(bekle).unwrap_or_default(), err.recv_timeout(bekle).unwrap_or_default())
}

/// Ask kararı varsa stdout'u harness JSON'u yap (ajan hook stdout'u bastırılır, boyutu stderr'e not düşülür).
fn ask_ile(mut s: Sonuc, ask: Option<String>) -> Sonuc {
    if let Some(j) = ask {
        if !s.cikti.is_empty() {
            s.hata.push_str(&format!("(ajan hook stdout'u ask kararı yüzünden bastırıldı: {} bayt)\n", s.cikti.len()));
        }
        s.cikti = format!("{j}\n").into_bytes();
    }
    s
}

pub fn kos(olay: &str, o: &Ortam) -> Sonuc {
    let mut s = Sonuc::bos();
    let girdi_ham = o.stdin_metin();
    let girdi = sondaki_nl_sil(&girdi_ham).to_string();
    let g: Value = if girdi.trim().is_empty() { Value::Object(Default::default()) } else { json_oku(&girdi).unwrap_or(Value::Object(Default::default())) };
    let cwd_ham = g.get("cwd").and_then(Value::as_str).unwrap_or("").to_string();
    let cwd = rp(&cwd_ham).to_string_lossy().into_owned();
    let kok = realpath(&o.repo).to_string_lossy().into_owned();
    let proje = o.env("CLAUDE_PROJECT_DIR").unwrap_or("");
    // A3 (Karar 130): ajan deny/ask kuralları; anahtar JARVIS_DISPATCH_DENY=1, varsayılan kapalı.
    let mut ask: Option<String> = None;
    if olay == "PreToolUse" && o.env("JARVIS_DISPATCH_DENY") == Some("1") {
        let k = izin::canli(&g, Path::new(&cwd), Path::new(&kok), proje, &ev_dizini());
        for u in &k.uyarilar {
            s.hata.push_str(&format!("{u}\n"));
        }
        match k.eslesme {
            Some(e) if e.tur == izin::Tur::Deny => {
                s.hata.push_str(&format!("{} ajan kuralı engelledi (deny): {}\n", e.ajan, e.kural));
                s.kod = 2;
                return s;
            }
            Some(e) => ask = Some(izin::ask_json(&e)),
            None => {}
        }
    }
    // D22 (b): cwd bir ajan dizini değilse hiçbir çocuk süreç başlatmadan çık.
    let on = format!("{kok}{}", sep());
    if !cwd.starts_with(&on) {
        return ask_ile(s, ask);
    }
    let ajan = cwd[on.len()..].split(sep()).next().unwrap_or("").to_string();
    let ajan_dir = PathBuf::from(&kok).join(&ajan);
    if rp(proje) == realpath(&ajan_dir) {
        return ask_ile(s, ask); // çift-koşum freni: harness ajanın kendi ayarını zaten yükledi
    }
    let ayar = ajan_dir.join(".claude").join("settings.json");
    let Some(ayar_v) = std::fs::read_to_string(&ayar).ok().and_then(|t| json_oku(&t)) else { return ask_ile(s, ask) };
    let kayitlar = ayar_v.get("hooks").and_then(|h| h.get(olay)).and_then(Value::as_array).cloned().unwrap_or_default();
    let arac = g.get("tool_name").and_then(Value::as_str).unwrap_or("");
    let mut kod = 0;
    for k in kayitlar {
        let m = k.get("matcher").and_then(Value::as_str).unwrap_or("");
        if !matcher_uyar(m, arac) {
            continue;
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
            // D22 (c): çocuk zaman aşımı; kilit olayında aşım = kes, diğerlerinde = uyar ve geç.
            let sure = zaman_asimi(&h, o);
            let (rc, asim, out, err) = sinirli_bekle(cocuk, sure);
            s.cikti.extend_from_slice(&out);
            s.hata.push_str(&String::from_utf8_lossy(&err));
            if asim {
                let sn = sure.as_secs_f64();
                if kilit_olayi(olay) {
                    s.hata.push_str(&format!("hook-dispatch: {ajan} {olay} hook'u {sn:.1} sn'de bitmedi, öldürüldü; kilit olayı, işlem kesildi: {komut}\n"));
                    s.kod = 2;
                    return s;
                }
                s.hata.push_str(&format!("hook-dispatch: {ajan} {olay} hook'u {sn:.1} sn'de bitmedi, öldürüldü; geçildi: {komut}\n"));
                continue;
            }
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
    ask_ile(s, ask)
}

#[cfg(test)]
mod testler {
    use super::matcher_uyar;

    #[test]
    fn yildiz_hepsi_demek() {
        assert!(matcher_uyar("*", "Bash"));
        assert!(matcher_uyar("*", "Read"));
        assert!(matcher_uyar("", "Bash"));
    }

    #[test]
    fn regex_matcher_korunur() {
        assert!(matcher_uyar("Bash", "Bash"));
        assert!(!matcher_uyar("Bash", "Read"));
        assert!(matcher_uyar("Read|Grep|Glob", "Grep"));
        assert!(matcher_uyar("Bash", ""));
    }
}
