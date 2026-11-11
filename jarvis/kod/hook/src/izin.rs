//! A3 (Karar 130): kökten açılan oturumda ajan `permissions.deny` ve `ask` kurallarını dağıtıcıda eşler.
//! Neden: harness yalnız oturum dizininin ayarını yükler; kökten açılan oturumda `<ajan>/.claude/settings.json`
//! izin kuralları uygulanmaz. Dağıtıcı PreToolUse olayında hedef yolun ve cwd'nin ajanını bulur, o ajanın kurallarını eşler.
//! Anahtar: `JARVIS_DISPATCH_DENY=1` (varsayılan kapalı; Salih şartı: debug denetimi geçmeden devreye girmez).
//! Kuru koşum: `hook-dispatch deny-denetle <ajan> <girdi.json | satır içi JSON>`.
//! Kural dili (Claude Code alt kümesi): `Araç` (aracın tamamı) · `Bash(önek:*)` (sözcük sınırlı önek) · `Bash(a * b)` (`*` joker,
//! tam eşleşme) · `Bash(komut)` (tam eşleşme) · `Read|Edit|Write(desen)` yol glob'u: `//c/...` mutlak, `~/...` ev dizini,
//! `/...` ve göreli desen ajan dizinine göre, `**` her derinlik, `*` tek parça. Read kuralı Read/Grep/Glob/NotebookRead'e,
//! Edit ve Write kuralı Edit/MultiEdit/Write/NotebookEdit'e uygulanır. Desteklenmeyen biçim sessiz geçmez: uyarı listesine düşer.
use regex::Regex;
use serde_json::Value;
use std::path::{Path, PathBuf};

#[derive(Debug, Clone, PartialEq)]
pub enum Tur {
    Deny,
    Ask,
}

#[derive(Debug, Clone)]
pub struct Eslesme {
    pub tur: Tur,
    pub kural: String,
    pub ajan: String,
}

#[derive(Debug, Default)]
pub struct Karar {
    pub eslesme: Option<Eslesme>,
    pub uyarilar: Vec<String>,
}

const OKUMA: &[&str] = &["Read", "Grep", "Glob", "NotebookRead"];
const YAZMA: &[&str] = &["Edit", "MultiEdit", "Write", "NotebookEdit"];

/// Karşılaştırma biçimi: `C:\a\B` ve `//c/a/B` → `/c/a/b` (Windows'ta küçük harf), `.` ve `..` sadeleşir.
pub fn yol_normal(s: &str) -> String {
    let mut t = s.replace('\\', "/");
    if t.starts_with("//") {
        t.remove(0);
    }
    let b = t.as_bytes();
    if b.len() >= 2 && b[1] == b':' && b[0].is_ascii_alphabetic() {
        t = format!("/{}{}", (b[0] as char).to_ascii_lowercase(), &t[2..]);
    }
    let mut parca: Vec<&str> = vec![];
    for p in t.split('/') {
        match p {
            "" | "." => {}
            ".." => {
                parca.pop();
            }
            x => parca.push(x),
        }
    }
    let r = format!("/{}", parca.join("/"));
    if cfg!(windows) { r.to_lowercase() } else { r }
}

/// Glob → regex: sondaki `/**` dizinin kendisini de kapsar, `**/` sıfır ya da çok dizin, `**` her şey, `*` ve `?` tek parça içinde.
fn glob_regex(g: &str) -> Option<Regex> {
    let (govde, son) = match g.strip_suffix("/**") {
        Some(b) => (b, "(?:/.*)?"),
        None => (g, ""),
    };
    let ch: Vec<char> = govde.chars().collect();
    let mut r = String::from("^");
    let mut i = 0;
    while i < ch.len() {
        match ch[i] {
            '*' if ch.get(i + 1) == Some(&'*') => {
                if ch.get(i + 2) == Some(&'/') {
                    r.push_str("(?:.*/)?");
                    i += 3;
                } else {
                    r.push_str(".*");
                    i += 2;
                }
                continue;
            }
            '*' => r.push_str("[^/]*"),
            '?' => r.push_str("[^/]"),
            c => r.push_str(&regex::escape(&c.to_string())),
        }
        i += 1;
    }
    r.push_str(son);
    r.push('$');
    Regex::new(&r).ok()
}

/// Kural yol desenini mutlak, normal biçime çevir.
fn kural_yolu(desen: &str, ajan_dir: &Path, ev: &Path) -> String {
    let ajan = yol_normal(&ajan_dir.to_string_lossy());
    let ham = if desen.starts_with("//") {
        return yol_normal_desen(desen);
    } else if let Some(r) = desen.strip_prefix("~/") {
        format!("{}/{r}", yol_normal(&ev.to_string_lossy()))
    } else if let Some(r) = desen.strip_prefix('/') {
        format!("{ajan}/{r}")
    } else if !desen.contains('/') {
        format!("{ajan}/**/{desen}") // gitignore kuralı: eğiksiz desen her derinlikte
    } else {
        format!("{ajan}/{}", desen.trim_start_matches("./"))
    };
    yol_normal_desen(&ham)
}

/// Desende `**` parçalarını koruyarak normal biçim (yol_normal `..` sadeleştirir, joker dokunulmaz).
fn yol_normal_desen(d: &str) -> String {
    let son_eg = d.ends_with('/');
    let n = yol_normal(d);
    if son_eg { format!("{n}/") } else { n }
}

/// Bash komutunu alt komutlara böl (`&&`, `||`, `;`, `|`, satır sonu); her parça ayrı eşlenir.
fn alt_komutlar(k: &str) -> Vec<String> {
    let ayir = Regex::new(r"&&|\|\||;|\||\n").unwrap();
    ayir.split(k).map(|p| p.split_whitespace().collect::<Vec<_>>().join(" ")).filter(|p| !p.is_empty()).collect()
}

fn bash_uyar(icerik: &str, komut: &str) -> bool {
    let icerik = icerik.trim();
    if let Some(onek) = icerik.strip_suffix(":*") {
        let onek = onek.trim();
        return alt_komutlar(komut).iter().any(|a| a == onek || a.strip_prefix(onek).is_some_and(|k| k.starts_with(' ')));
    }
    if icerik.contains('*') {
        let desen = format!("^{}$", icerik.split('*').map(regex::escape).collect::<Vec<_>>().join(".*"));
        let Ok(r) = Regex::new(&desen) else { return false };
        return alt_komutlar(komut).iter().any(|a| r.is_match(a));
    }
    alt_komutlar(komut).iter().any(|a| a == icerik)
}

/// Aracın hedef yolu (mutlak, normal); Grep/Glob yolsuzsa cwd.
fn hedef_yol(g: &Value, cwd: &Path) -> Option<String> {
    let ti = g.get("tool_input")?;
    let arac = g.get("tool_name").and_then(Value::as_str).unwrap_or("");
    let ham = ["file_path", "notebook_path", "path"].iter().find_map(|a| ti.get(*a).and_then(Value::as_str)).map(str::to_string);
    let ham = match ham {
        Some(h) if !h.is_empty() => h,
        _ if arac == "Grep" || arac == "Glob" => cwd.to_string_lossy().into_owned(),
        _ => return None,
    };
    let p = PathBuf::from(&ham);
    let mutlak = ham.starts_with('/') || ham.starts_with('\\') || p.is_absolute();
    Some(if mutlak { yol_normal(&ham) } else { yol_normal(&cwd.join(&ham).to_string_lossy()) })
}

/// Tek kural tek araç çağrısıyla eşleşiyor mu; `Err` = desteklenmeyen kural biçimi.
pub fn kural_uyar(kural: &str, g: &Value, cwd: &Path, ajan_dir: &Path, ev: &Path) -> Result<bool, String> {
    let arac = g.get("tool_name").and_then(Value::as_str).unwrap_or("");
    let (ad, icerik) = match kural.find('(') {
        Some(i) if kural.ends_with(')') => (&kural[..i], Some(&kural[i + 1..kural.len() - 1])),
        Some(_) => return Err(format!("kapanmamış parantez: {kural}")),
        None => (kural, None),
    };
    let kapsam: Vec<&str> = match ad {
        "Read" => OKUMA.to_vec(),
        "Edit" | "Write" => YAZMA.to_vec(),
        x => vec![x],
    };
    let Some(icerik) = icerik else { return Ok(kapsam.contains(&arac)) };
    match ad {
        "Bash" => {
            if arac != "Bash" {
                return Ok(false);
            }
            let komut = g.pointer("/tool_input/command").and_then(Value::as_str).unwrap_or("");
            Ok(bash_uyar(icerik, komut))
        }
        "Read" | "Edit" | "Write" => {
            if !kapsam.contains(&arac) {
                return Ok(false);
            }
            let Some(hedef) = hedef_yol(g, cwd) else { return Ok(false) };
            let desen = kural_yolu(icerik, ajan_dir, ev);
            let r = glob_regex(&desen).ok_or_else(|| format!("glob derlenemedi: {kural}"))?;
            Ok(r.is_match(&hedef))
        }
        _ => Err(format!("desteklenmeyen kural biçimi: {kural}")),
    }
}

/// `<kök>/<ad>/.claude/settings.json` olan ilk yol parçası ajan sayılır.
pub fn ajan_bul(yol_norm: &str, kok: &Path) -> Option<String> {
    let k = yol_normal(&kok.to_string_lossy());
    let kalan = yol_norm.strip_prefix(&format!("{k}/"))?;
    let ad = kalan.split('/').next()?;
    let gercek = std::fs::read_dir(kok).ok()?.flatten().map(|e| e.file_name().to_string_lossy().into_owned()).find(|n| n.eq_ignore_ascii_case(ad))?;
    kok.join(&gercek).join(".claude").join("settings.json").is_file().then_some(gercek)
}

fn kurallar(ajan_dir: &Path) -> (Vec<String>, Vec<String>) {
    let v: Value = std::fs::read_to_string(ajan_dir.join(".claude").join("settings.json")).ok().and_then(|t| serde_json::from_str(&t).ok()).unwrap_or(Value::Null);
    let al = |a: &str| -> Vec<String> {
        v.pointer(&format!("/permissions/{a}")).and_then(Value::as_array).map(|x| x.iter().filter_map(Value::as_str).map(str::to_string).collect()).unwrap_or_default()
    };
    (al("deny"), al("ask"))
}

/// Verilen ajanların kurallarını eşle: önce bütün deny'lar, sonra ask'lar (deny kazanır).
pub fn denetle(ajanlar: &[String], g: &Value, cwd: &Path, kok: &Path, ev: &Path) -> Karar {
    let mut k = Karar::default();
    let mut adaylar: Vec<(Tur, String, String)> = vec![];
    for a in ajanlar {
        let (deny, ask) = kurallar(&kok.join(a));
        adaylar.extend(deny.into_iter().map(|r| (Tur::Deny, r, a.clone())));
        adaylar.extend(ask.into_iter().map(|r| (Tur::Ask, r, a.clone())));
    }
    adaylar.sort_by_key(|(t, _, _)| if *t == Tur::Deny { 0 } else { 1 });
    for (tur, kural, ajan) in adaylar {
        match kural_uyar(&kural, g, cwd, &kok.join(&ajan), ev) {
            Ok(true) if k.eslesme.is_none() => k.eslesme = Some(Eslesme { tur, kural, ajan }),
            Ok(_) => {}
            Err(e) => {
                let u = format!("izin denetimi ({ajan}): {e}");
                if !k.uyarilar.contains(&u) {
                    k.uyarilar.push(u);
                }
            }
        }
    }
    k
}

/// Canlı yol: hedef yolun ve cwd'nin ajanları; harness'in zaten yüklediği ajan (CLAUDE_PROJECT_DIR) atlanır.
pub fn canli(g: &Value, cwd: &Path, kok: &Path, proje: &str, ev: &Path) -> Karar {
    let mut ajanlar: Vec<String> = vec![];
    if let Some(h) = hedef_yol(g, cwd) {
        ajanlar.extend(ajan_bul(&h, kok));
    }
    ajanlar.extend(ajan_bul(&yol_normal(&cwd.to_string_lossy()), kok));
    ajanlar.dedup();
    let proje_n = yol_normal(proje);
    ajanlar.retain(|a| proje.is_empty() || yol_normal(&kok.join(a).to_string_lossy()) != proje_n);
    if ajanlar.is_empty() {
        return Karar::default();
    }
    denetle(&ajanlar, g, cwd, kok, ev)
}

/// PreToolUse "ask" kararı (harness JSON çıktısı).
pub fn ask_json(e: &Eslesme) -> String {
    serde_json::json!({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": format!("{} ajan kuralı (ask): {}", e.ajan, e.kural),
        }
    })
    .to_string()
}

#[cfg(test)]
mod testler {
    use super::*;
    use serde_json::json;

    fn kok() -> PathBuf {
        PathBuf::from(if cfg!(windows) { r"C:\sistem\sistem" } else { "/c/sistem/sistem" })
    }
    fn uy(kural: &str, g: Value) -> bool {
        let k = kok();
        kural_uyar(kural, &g, &k.join("tart"), &k.join("tart"), Path::new("/ev")).unwrap()
    }

    #[test]
    fn bash_onek_sozcuk_sinirli() {
        let g = |c: &str| json!({"tool_name":"Bash","tool_input":{"command":c}});
        assert!(uy("Bash(git push origin main:*)", g("git push origin main")));
        assert!(uy("Bash(git add -A:*)", g("cd x && git add -A")));
        assert!(!uy("Bash(git add -A:*)", g("git add -Am")));
        assert!(!uy("Bash(git add .:*)", g("git add tart/a.md")));
        assert!(uy("Bash(git push:*)", g("git   push origin x")));
        assert!(uy("Bash(git * main)", g("git push origin main")));
    }

    #[test]
    fn yol_glob_mutlak_ve_goreli() {
        let r = |p: &str| json!({"tool_name":"Read","tool_input":{"file_path":p}});
        assert!(uy("Read(//c/sistem/sistem/jarvis/**)", r(r"C:\sistem\sistem\jarvis\CLAUDE.md")));
        assert!(uy("Read(//c/sistem/sistem/jarvis/**)", r("/c/sistem/sistem/jarvis")));
        assert!(!uy("Read(//c/sistem/sistem/jarvis/**)", r(r"C:\sistem\sistem\jarvisx\a")));
        assert!(!uy("Read(//c/sistem/sistem/jarvis/**)", r("core/a.md")));
        assert!(uy("Edit(core/*.md)", json!({"tool_name":"Write","tool_input":{"file_path":"core/a.md"}})));
        assert!(!uy("Edit(core/*.md)", json!({"tool_name":"Write","tool_input":{"file_path":"core/x/a.md"}})));
        assert!(uy("Read(~/.ssh/**)", r("/ev/.ssh/id")));
        assert!(uy("Read(//c/sistem/sistem/jarvis/**)", json!({"tool_name":"Grep","tool_input":{"path":"../jarvis/core"}})));
    }

    #[test]
    fn desteklenmeyen_bicim_hata() {
        let k = kok();
        let g = json!({"tool_name":"WebFetch","tool_input":{"url":"x"}});
        assert!(kural_uyar("WebFetch(domain:x.com)", &g, &k, &k, Path::new("/ev")).is_err());
        assert!(kural_uyar("WebFetch", &g, &k, &k, Path::new("/ev")).unwrap());
    }
}
