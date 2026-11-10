//! `okuma-izin.sh` (alan ajanları: friday, tart, gard, ...) karşılığı: PreToolUse okuma kilidi (Read · Grep · Glob · Bash).
//! Davranış kaynağı v0.6 Python gövdesi (tart kopyası); bu modül v0.7 (2026-11-10).
//! İzinli kökler: ajan dizini + kök `sablonlar/` + geçici dizinler + harness `~/.claude/projects` + `.claude/okuma-izin-ek` satırları;
//! depo kökünün kendisi ve doğrudan altındaki dosyalar serbest; ev ve depo kökü dışındaki sistem yolları serbest; geri kalanı çıkış 2.
//! v0.6'ya göre üç düzeltme: (a) Git Bash `/c/` ve `/cygdrive/c/` önekleri çözümden önce `C:/` olur (Windows)
//! (b) fail-closed: stdin JSON nesnesi değilse (boş dahil) çıkış 2 (c) `std::env::temp_dir()` izinli geçici dizinlere eklenir.
use crate::ortak::{Ortam, Sonuc, ekle_satir, ev_dizini, ilk_n, oku_py, py_dumps, py_isabs, py_truthy, realpath, sep, ts_yerel};
use regex::Regex;
use serde_json::{Map, Value, json};
use std::path::{Path, PathBuf};

const KAYNAK: &str = "okuma-izin (rust) v0.7";

/// Dosya açan komutlar: argümanları yol sayılır. Liste eksik kalabilir (desen 20); yeni okuma komutu buraya eklenir.
const DOSYA_KOMUT: &[&str] = &[
    "cat", "sed", "head", "tail", "less", "more", "cp", "mv", "ln", "rm", "python3", "python", "bash", "sh", "source", ".", "jq",
    "sqlite3", "wc", "sort", "uniq", "diff", "open", "code", "ls", "find", "awk", "grep", "rg", "egrep", "fgrep", "tee", "touch",
    "mkdir", "stat", "file", "md5", "shasum", "nl", "cut",
];
/// İlk argümanı desen/betik olan komutlar: o argüman yol sayılmaz.
const DESEN_ILK: &[&str] = &["grep", "rg", "egrep", "fgrep", "sed", "awk", "jq", "find"];
const DEGER_ALAN_BAYRAK: &[&str] = &["-e", "-f", "--regexp", "--file", "--include", "--exclude", "-name", "-iname", "-path"];
const SARMALAYICI: &[&str] = &["sudo", "time", "timeout", "nice", "nohup", "stdbuf", "command", "builtin", "xargs", "env"];

// ---------------------------------------------------------------- yol yardımcıları

/// Git Bash / Cygwin sürücü önekini Windows biçimine çevirir: `/c/x` ve `/cygdrive/c/x` -> `C:/x`; önek yoksa yol aynen döner.
/// (`altajan_okuma.rs` içindeki özel fonksiyonun kopyası; ortak yardımcıya taşınması Jarvis'e bırakıldı.)
pub(crate) fn surucu_onek_cevir(yol: &str) -> String {
    let govde = yol.strip_prefix("/cygdrive").filter(|g| g.starts_with('/')).unwrap_or(yol);
    let b = govde.as_bytes();
    if b.len() >= 2 && b[0] == b'/' && b[1].is_ascii_alphabetic() && (b.len() == 2 || b[2] == b'/') {
        let harf = (b[1] as char).to_ascii_uppercase();
        let kalan = if b.len() == 2 { "/" } else { &govde[2..] };
        return format!("{harf}:{kalan}");
    }
    yol.to_string()
}

fn onek(yol: &str) -> String {
    if cfg!(windows) { surucu_onek_cevir(yol) } else { yol.to_string() }
}

/// Python `coz`: mutlaksa kendisi, değilse cwd'ye göre; sonra realpath. Önce MSYS öneki çevrilir (düzeltme a).
fn coz(yol: &str, cwd: &Path) -> PathBuf {
    let y = onek(yol);
    let tam = if py_isabs(&y) { PathBuf::from(&y) } else { cwd.join(&y) };
    realpath(&tam)
}

/// Karşılaştırma anahtarı: Windows'ta harf duyarsız (NTFS), diğerlerinde aynen.
fn anahtar(s: &str) -> String {
    if cfg!(windows) { s.to_lowercase() } else { s.to_string() }
}

fn metin(p: &Path) -> String {
    p.to_string_lossy().into_owned()
}

/// `r == k or r.startswith(k + os.sep)`.
fn altinda(r: &str, k: &str) -> bool {
    let (r, k) = (anahtar(r), anahtar(k));
    r == k || r.starts_with(&format!("{k}{}", sep()))
}

struct Kilit {
    repo: PathBuf,
    home: PathBuf,
    kok: PathBuf,
    harness: PathBuf,
    izinli: Vec<String>,
}

impl Kilit {
    fn kur(o: &Ortam) -> Kilit {
        let repo = realpath(Path::new(&onek(&metin(&o.repo))));
        let home = realpath(&ev_dizini());
        let kok = repo.parent().map(Path::to_path_buf).unwrap_or_default();
        let harness = home.join(".claude").join("projects");
        let mut izinli: Vec<String> = vec![
            metin(&repo),
            metin(&kok.join("sablonlar")),
            "/tmp".into(),
            "/private/tmp".into(),
            "/private/var/folders".into(),
            metin(&harness),
            metin(&realpath(&std::env::temp_dir())), // düzeltme (c): Windows geçici dizini ev altında
        ];
        // v0.6: ek salt-okur kökler (depo köküne göreli; ör. ogrenme/kaynaklar); dosya yoksa sessiz
        if let Some(govde) = oku_py(&repo.join(".claude").join("okuma-izin-ek")) {
            for satir in govde.lines() {
                let satir = satir.trim();
                if !satir.is_empty() && !satir.starts_with('#') {
                    izinli.push(metin(&coz(satir, &kok)));
                }
            }
        }
        Kilit { repo, home, kok, harness, izinli }
    }

    fn izinli_mi(&self, r: &Path) -> bool {
        let rs = metin(r);
        if self.izinli.iter().any(|k| altinda(&rs, k)) {
            return true;
        }
        let ks = metin(&self.kok);
        // kök kanon: depo kökünün kendisi ve doğrudan altındaki dosyalar serbest; alt dizinler izin listesine tabi
        if anahtar(&rs) == anahtar(&ks) || (r.parent().is_some_and(|u| anahtar(&metin(u)) == anahtar(&ks)) && !r.is_dir()) {
            return true;
        }
        // ev dizini ve depo kökü dışındaki sistem yolları serbest; ev ya da depo kökü altındaki her şey izin listesine tabi
        let hs = metin(&self.home);
        let ust = |k: &str| anahtar(&rs).starts_with(&format!("{}{}", anahtar(k), sep()));
        !(anahtar(&rs) == anahtar(&hs) || ust(&hs) || ust(&ks))
    }

    /// (gerçek_yol, ham) çiftleri; `cd` izlenir, yalnız dosya komutlarının argümanları ve yönlendirme hedefleri taranır.
    fn bash_adaylari(&self, cmd: &str) -> Vec<(PathBuf, String)> {
        let cmd = heredoc_sil(cmd); // gövde = içerik, okuma değil
        let ev = metin(&self.home).replace('\\', "/");
        let cmd = cmd.replace("${HOME}", &ev).replace("$HOME", &ev).replace('~', &ev);
        let ayrac = Regex::new(r"&&|\|\||;|\||\n").unwrap();
        let belirtec = Regex::new(r#"[^\s'"]+|'[^']*'|"[^"]*""#).unwrap();
        let atama = Regex::new(r"^\w+=\S*$").unwrap();
        let mut cwd = self.repo.clone();
        let mut cikti = vec![];
        for parca in ayrac.split(&cmd) {
            let parcalar: Vec<&str> = belirtec.find_iter(parca).map(|m| m.as_str()).filter(|p| !p.is_empty()).collect();
            if parcalar.is_empty() {
                continue;
            }
            let mut i = 0;
            // ortam ataması ve sarmalayıcıları geç
            while i < parcalar.len() && (atama.is_match(parcalar[i]) || SARMALAYICI.contains(&soy(parcalar[i]))) {
                i += 1;
            }
            if i >= parcalar.len() {
                continue;
            }
            let komut = taban_ad(soy(parcalar[i])).to_string();
            i += 1;
            if komut == "cd" {
                let hedef = parcalar.get(i).map(|t| soy(t)).unwrap_or("");
                if !hedef.is_empty() && !hedef.contains('$') {
                    cwd = coz(hedef, &cwd);
                    cikti.push((cwd.clone(), hedef.to_string()));
                }
                continue;
            }
            let mut desen_atlanacak = DESEN_ILK.contains(&komut.as_str());
            let mut atla_sonraki = false;
            for ham in &parcalar[i..] {
                let t = soy(ham);
                if atla_sonraki {
                    atla_sonraki = false;
                    continue;
                }
                if DEGER_ALAN_BAYRAK.contains(&t) {
                    atla_sonraki = true;
                    continue;
                }
                if t.starts_with('<') || t.starts_with('>') || matches!(t, ">" | ">>" | "<" | "2>") {
                    // yönlendirme: hedef her zaman aday
                    let hedef = t.trim_start_matches(['<', '>', '2']).trim();
                    if !hedef.is_empty() {
                        let p = yol_mu(hedef);
                        if !p.is_empty() {
                            cikti.push((coz(p, &cwd), hedef.to_string()));
                        }
                    }
                    continue;
                }
                if t.starts_with('-') {
                    continue;
                }
                if desen_atlanacak {
                    // ilk sözcük-argüman desen/betiktir
                    desen_atlanacak = false;
                    continue;
                }
                if !DOSYA_KOMUT.contains(&komut.as_str()) {
                    continue;
                }
                let p = yol_mu(t);
                if !p.is_empty() {
                    cikti.push((coz(p, &cwd), t.to_string()));
                }
            }
        }
        cikti
    }
}

/// Python `tok.strip().strip("'\"")`.
fn soy(tok: &str) -> &str {
    tok.trim().trim_matches(['\'', '"'])
}

/// `os.path.basename`: Windows'ta `/` ve `\`, diğerlerinde `/`.
fn taban_ad(s: &str) -> &str {
    let ayraclar: &[char] = if cfg!(windows) { &['/', '\\'] } else { &['/'] };
    s.rsplit(ayraclar).next().unwrap_or(s)
}

/// Belirteç yol adayı mı; değişkenliyse `$`'tan önceki sabit önek döner ('' = görünmez).
/// Windows'ta `\` de yol işareti sayılır (`cat 'C:\x\y'`).
fn yol_mu(tok: &str) -> &str {
    let tok = match tok.find('$') {
        Some(k) => &tok[..k],
        None => tok,
    };
    if tok.is_empty() || tok.starts_with('-') {
        return "";
    }
    if tok.contains('/') || tok.starts_with('.') || (cfg!(windows) && tok.contains('\\')) { tok } else { "" }
}

fn kelime(c: char) -> bool {
    c.is_alphanumeric() || c == '_'
}

/// `<<-?\s*['"]?(\w+)['"]?.*?\n\1\s*$` (S|M) -> `<<HEREDOC>>` (`altajan_okuma.rs` ile aynı el yazımı eşleyici).
fn heredoc_sil(s: &str) -> String {
    let c: Vec<char> = s.chars().collect();
    let n = c.len();
    let mut cikti = String::new();
    let mut i = 0;
    while i < n {
        if c[i] == '<' && i + 1 < n && c[i + 1] == '<' && let Some(son) = heredoc_dene(&c, i + 2) {
            cikti.push_str("<<HEREDOC>>");
            i = son;
            continue;
        }
        cikti.push(c[i]);
        i += 1;
    }
    cikti
}

fn heredoc_dene(c: &[char], mut p: usize) -> Option<usize> {
    let n = c.len();
    if p < n && c[p] == '-' {
        p += 1;
    }
    while p < n && c[p].is_whitespace() {
        p += 1;
    }
    if p < n && (c[p] == '\'' || c[p] == '"') {
        p += 1;
    }
    let bas = p;
    while p < n && kelime(c[p]) {
        p += 1;
    }
    if p == bas {
        return None;
    }
    for uzun in (1..=(p - bas)).rev() {
        let kel = &c[bas..bas + uzun];
        let mut q = bas + uzun;
        if q < n && (c[q] == '\'' || c[q] == '"') {
            q += 1;
        }
        let mut i = q;
        while i < n {
            if c[i] == '\n' && i + 1 + uzun <= n && &c[i + 1..i + 1 + uzun] == kel {
                let a = i + 1 + uzun;
                let mut b = a;
                while b < n && c[b].is_whitespace() {
                    b += 1;
                }
                let mut e = b;
                loop {
                    if e == n || c[e] == '\n' {
                        return Some(e);
                    }
                    if e == a {
                        break;
                    }
                    e -= 1;
                }
            }
            i += 1;
        }
    }
    None
}

fn sirali_tekil(mut v: Vec<String>) -> Vec<String> {
    v.sort();
    v.dedup();
    v
}

pub fn kos(o: &Ortam) -> Sonuc {
    let mut s = Sonuc::bos();
    // düzeltme (b): fail-closed; ayrıştırılamayan ya da nesne olmayan girdi (boş dahil) engellenir
    let g: Map<String, Value> = match serde_json::from_str::<Value>(&o.stdin_metin()) {
        Ok(Value::Object(m)) => m,
        Ok(_) => {
            s.hata = "OKUMA-İZİN KİLİDİ: hook girdisi JSON nesnesi değil; çağrı engellendi (fail-closed).\n".into();
            s.kod = 2;
            return s;
        }
        Err(e) => {
            s.hata = format!("OKUMA-İZİN KİLİDİ: hook girdisi JSON olarak ayrıştırılamadı ({e}); çağrı engellendi (fail-closed).\n");
            s.kod = 2;
            return s;
        }
    };
    let arac = g.get("tool_name").and_then(Value::as_str).unwrap_or("").to_string();
    let ti = match g.get("tool_input") {
        Some(Value::Object(m)) => m.clone(),
        _ => Map::new(),
    };
    let k = Kilit::kur(o);
    let test = ["FRIDAY_HOOK_TEST", "JARVIS_HOOK_TEST", "AJAN_HOOK_TEST"].iter().any(|a| o.env(a).is_some_and(|v| !v.is_empty()));

    let adaylar: Vec<(PathBuf, String)> = match arac.as_str() {
        "Read" | "Grep" | "Glob" => ["file_path", "path"]
            .iter()
            .filter_map(|a| ti.get(*a).and_then(Value::as_str).filter(|y| !y.is_empty()))
            .map(|y| (coz(y, &k.repo), y.to_string()))
            .collect(),
        "Bash" => k.bash_adaylari(ti.get("command").and_then(Value::as_str).unwrap_or("")),
        _ => vec![],
    };

    // ---- 1. katman: izin listesi (ana-sıra ve alt-ajan için aynı) ----
    let kotu = sirali_tekil(adaylar.iter().filter(|(r, _)| !k.izinli_mi(r)).map(|(_, h)| h.clone()).collect());
    if !kotu.is_empty() {
        s.hata = format!(
            "OKUMA-İZİN KİLİDİ (Karar 91/101/105): ajan kendi dizini + depo kökündeki kanon dosyaları + sablonlar/ + okuma-izin-ek kökleri okur; diğer ajan dizinleri (jarvis/**, friday/**, alan ajanları) ve repo dışı kullanıcı yolu kapalıdır. Reddedilen yol: {}\n",
            kotu.join(", ")
        );
        s.kod = 2;
        return s;
    }

    // ---- 2. katman: alt-ajan dalı (Karar 99 M2; cc/gelen Karar 100 M3) ----
    let agent_id = g.get("agent_id").cloned().unwrap_or(Value::Null);
    if py_truthy(&agent_id) {
        let r = |a: &str, b: &str| metin(&k.repo.join(a).join(b));
        let alt_yasak = [
            r("core", "durum-kapsulu.md"),
            r("core", "pano.md"),
            r("kuyruk", "senaryo-defteri.md"),
            r("kuyruk", "fikir-kutusu.md"),
            r("veri", "bronz"),
            r("cc", "gelen"),
            metin(&k.harness),
        ];
        let hs = metin(&k.harness);
        let tr = format!("{0}tool-results{0}", sep());
        let alt_yasak_mi = |p: &Path| -> bool {
            let ps = metin(p);
            let muaf = anahtar(&ps).contains(&anahtar(&tr)) && anahtar(&ps).starts_with(&format!("{}{}", anahtar(&hs), sep()));
            !muaf && alt_yasak.iter().any(|y| altinda(&ps, y))
        };
        let kotu2 = sirali_tekil(adaylar.iter().filter(|(p, _)| alt_yasak_mi(p)).map(|(_, h)| h.clone()).collect());
        if !kotu2.is_empty() {
            if !test {
                // test koşumu bronz kütüğe yazmaz; çıkış kararı bayraktan etkilenmez
                let oturum = ilk_n(g.get("session_id").and_then(Value::as_str).unwrap_or(""), 36);
                let agent_type = match g.get("agent_type") {
                    Some(v) if py_truthy(v) => v.clone(),
                    _ => Value::String(String::new()),
                };
                let satir = json!({"ts": ts_yerel(), "oturum": oturum, "agent_id": agent_id, "agent_type": agent_type,
                    "arac": arac, "reddedilen": kotu2, "kaynak": KAYNAK});
                let _ = ekle_satir(&k.repo.join("veri").join("bronz").join("altajan-okuma-olay.jsonl"), &py_dumps(&satir));
            }
            s.hata = format!(
                "ALT-AJAN OKUMA KİLİDİ (Karar 99 M2 · 100 M3): işçi, liderin bağlam penceresini ve başka devirlerin emirlerini okuyamaz (kapsül · pano · defter · kutu · kütükler · cc/gelen · transkriptler; kendi tool-results'ı muaf). Reddedilen: {}\n",
                kotu2.join(", ")
            );
            s.kod = 2;
        }
    }
    s
}

#[cfg(test)]
mod testler {
    use super::*;
    use std::collections::HashMap;

    fn ortam(repo: &Path, girdi: &str) -> Ortam {
        let mut env = HashMap::new();
        env.insert("AJAN_HOOK_TEST".to_string(), "1".to_string());
        Ortam { stdin: girdi.as_bytes().to_vec(), repo: repo.to_path_buf(), env }
    }

    /// Depo kökü (`jarvis/kod/hook` -> üç üst).
    fn depo_koku() -> PathBuf {
        realpath(&PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("..").join("..").join(".."))
    }

    fn bash(cmd: &str) -> String {
        json!({"tool_name": "Bash", "tool_input": {"command": cmd}}).to_string()
    }
    fn oku(yol: &str) -> String {
        json!({"tool_name": "Read", "tool_input": {"file_path": yol}}).to_string()
    }

    /// `C:\a\b` -> `/c/a/b`.
    fn msys(p: &Path) -> String {
        let s = metin(p).replace('\\', "/");
        let b = s.as_bytes();
        if b.len() >= 2 && b[1] == b':' { format!("/{}{}", (b[0] as char).to_ascii_lowercase(), &s[2..]) } else { s }
    }

    #[test]
    fn onek_cevrimi() {
        assert_eq!(surucu_onek_cevir("/c/sistem/sistem/jarvis/CLAUDE.md"), "C:/sistem/sistem/jarvis/CLAUDE.md");
        assert_eq!(surucu_onek_cevir("/cygdrive/c/x"), "C:/x");
        assert_eq!(surucu_onek_cevir("/tmp/x"), "/tmp/x");
    }

    #[test]
    fn bozuk_ve_bos_girdi_engellenir() {
        let kok = depo_koku();
        assert_eq!(kos(&ortam(&kok.join("friday"), "{bozuk")).kod, 2);
        assert_eq!(kos(&ortam(&kok.join("friday"), "")).kod, 2);
        assert_eq!(kos(&ortam(&kok.join("friday"), "[]")).kod, 2);
    }

    #[test]
    fn heredoc_govdesi_ve_desen_atlanir() {
        let kok = depo_koku();
        let o = ortam(&kok.join("friday"), "{}");
        let k = Kilit::kur(&o);
        let a = k.bash_adaylari("cat <<'EOF'\n/x/jarvis/kuyruk\nEOF\ngrep jarvis/core dosya.txt");
        let hamlar: Vec<&str> = a.iter().map(|(_, h)| h.as_str()).collect();
        assert!(!hamlar.iter().any(|h| h.contains("kuyruk") || h.contains("jarvis/core")), "{hamlar:?}");
    }

    #[test]
    fn diger_ajan_reddedilir_kendi_dizini_ve_kok_dosyasi_serbest() {
        let kok = depo_koku();
        let repo = kok.join("friday");
        let jarvis_md = kok.join("jarvis").join("CLAUDE.md");
        assert_eq!(kos(&ortam(&repo, &oku(&metin(&jarvis_md)))).kod, 2);
        assert_eq!(kos(&ortam(&repo, &bash(&format!("cat {}", metin(&jarvis_md).replace('\\', "/"))))).kod, 2);
        assert_eq!(kos(&ortam(&repo, &oku(&metin(&repo.join("AGENTS.md"))))).kod, 0);
        assert_eq!(kos(&ortam(&repo, &bash(&format!("cat {}", metin(&kok.join("AGENTS.md")).replace('\\', "/"))))).kod, 0);
        let gecici = std::env::temp_dir().join("x.txt");
        assert_eq!(kos(&ortam(&repo, &oku(&metin(&gecici)))).kod, 0);
    }

    #[cfg(windows)]
    #[test]
    fn git_bash_c_oneki_kilidi_atlatamaz() {
        let kok = depo_koku();
        let repo = kok.join("friday");
        let jarvis_md = msys(&kok.join("jarvis").join("CLAUDE.md"));
        assert!(jarvis_md.starts_with("/c/") || jarvis_md.starts_with('/'));
        assert_eq!(kos(&ortam(&repo, &bash(&format!("cat {jarvis_md}")))).kod, 2);
        assert_eq!(kos(&ortam(&repo, &oku(&jarvis_md))).kod, 2);
        assert_eq!(kos(&ortam(&repo, &bash(&format!("cat /cygdrive{jarvis_md}")))).kod, 2);
        assert_eq!(kos(&ortam(&repo, &oku(&msys(&repo.join("AGENTS.md"))))).kod, 0);
        assert_eq!(kos(&ortam(&repo, &bash(&format!("cat {}", msys(&kok.join("AGENTS.md")))))).kod, 0);
        // ajan dizini de Git Bash biçiminde verilebilir (CLAUDE_PROJECT_DIR=/c/...)
        let repo_msys = PathBuf::from(msys(&repo));
        assert_eq!(kos(&ortam(&repo_msys, &oku(&msys(&repo.join("AGENTS.md"))))).kod, 0);
        assert_eq!(kos(&ortam(&repo_msys, &bash(&format!("cat {jarvis_md}")))).kod, 2);
    }

    #[test]
    fn alt_ajan_kapsul_reddedilir() {
        let kok = depo_koku();
        let repo = kok.join("friday");
        let g = json!({"tool_name": "Read", "agent_id": "a1", "tool_input": {"file_path": metin(&repo.join("core").join("durum-kapsulu.md"))}});
        let s = kos(&ortam(&repo, &g.to_string()));
        assert_eq!(s.kod, 2);
        assert!(s.hata.starts_with("ALT-AJAN OKUMA KİLİDİ"));
    }
}
