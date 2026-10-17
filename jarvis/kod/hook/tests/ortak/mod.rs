//! Fark testi ortak donanımı: eski betik (bash/python) ile yeni ikili aynı girdiyle, ayrı kum havuzlarında koşar;
//! stdout · stderr · çıkış kodu · yazılan kütük/durum dosyaları (ts alanları hariç) eşit olmalı.
#![allow(dead_code)]
use jarvis_hook::ortak::py_dumps;
use serde_json::Value;
use std::collections::BTreeMap;
use std::io::Write;
use std::path::{Path, PathBuf};
use std::process::{Command, Stdio};
use std::sync::atomic::{AtomicUsize, Ordering};

pub static SAYAC: AtomicUsize = AtomicUsize::new(0);
pub static HOOK_SAYAC: std::sync::Mutex<BTreeMap<String, usize>> = std::sync::Mutex::new(BTreeMap::new());

#[derive(Clone, Copy, Debug)]
pub enum H {
    CoreTel,
    AjanFren,
    Altajan,
    Buyuk,
    Talimat,
    Userprompt,
    Session,
    Paket,
    Prompt,
    Dispatch,
}

pub fn gercek_kok() -> PathBuf {
    let p = Path::new(env!("CARGO_MANIFEST_DIR")).join("../../..");
    let c = std::fs::canonicalize(p).unwrap();
    PathBuf::from(c.to_string_lossy().trim_start_matches(r"\\?\"))
}

pub fn ileri(p: &Path) -> String {
    p.to_string_lossy().replace('\\', "/")
}

pub fn ev() -> String {
    let a = if cfg!(windows) { "USERPROFILE" } else { "HOME" };
    std::env::var(a).unwrap_or_default().replace('\\', "/")
}

pub struct Kum {
    pub kok: PathBuf,
    pub jarvis: PathBuf,
}

fn kopya(src: &Path, dst: &Path, rel: &str) {
    let s = src.join(rel);
    if s.is_file() {
        let d = dst.join(rel);
        std::fs::create_dir_all(d.parent().unwrap()).unwrap();
        std::fs::copy(&s, &d).unwrap();
    }
}

/// Geçici "kök" kur: `<kök>/jarvis/...` gerçek kaynaklardan kopya (hook betikleri, araçlar, tablo, manifest, kaynak dosyalar).
pub fn kum(ad: &str, yan: &str) -> Kum {
    let gk = gercek_kok();
    let kok = std::env::temp_dir().join(format!("jhook-{}-{ad}-{yan}", std::process::id()));
    let _ = std::fs::remove_dir_all(&kok);
    let jarvis = kok.join("jarvis");
    std::fs::create_dir_all(jarvis.join("veri").join("bronz")).unwrap();
    std::fs::create_dir_all(jarvis.join(".claude").join("hooks").join("state")).unwrap();
    let gj = gk.join("jarvis");
    for e in std::fs::read_dir(gj.join(".claude").join("hooks")).unwrap().flatten() {
        let n = e.file_name().to_string_lossy().into_owned();
        if n.ends_with(".sh") {
            kopya(&gj, &jarvis, &format!(".claude/hooks/{n}"));
        }
    }
    for r in ["tools/prompt-dosya.py", "tools/baglam_oku.py", "core/tuzuk-v0-m11.md", "core/tuzuk-v0-m17.md", "core/tuzuk-v0-m29.md", "core/tuzuk-v0-m30.md", "core/tuzuk-v0-m31.md", "core/tuzuk-v0-m32.md", "core/tuzuk-v0-m40.md", "core/tuzuk-v0-m41.md", "core/tuzuk-v0-m42.md", "core/tuzuk-v0-m43.md", "core/tuzuk-v0-m44.md", "core/tuzuk-v0-m45.md","core/tuzuk-v0-m46.md", "core/tuzuk-v0-m47.md","tools/paket-yonlendir.py", "core/prompt-dosya-tablosu.tsv", "core/baglam-paketleri.json", "core/tuzuk-v0.md", "core/durum-kapsulu.md", "core/pano.md", "core/ajan-metodolojisi.md", "core/ingest-semasi.md", "kuyruk/senaryo-defteri.md", "veri/karar-borcu.jsonl", "veri/model-kesim.jsonl"] {
        kopya(&gj, &jarvis, r);
    }
    if let Ok(rd) = std::fs::read_dir(gj.join("kuyruk")) {
        for e in rd.flatten() {
            let n = e.file_name().to_string_lossy().into_owned();
            if n.starts_with("masa-gundemi-") {
                kopya(&gj, &jarvis, &format!("kuyruk/{n}"));
            }
        }
    }
    // manifestte anılan adresler
    if let Ok(t) = std::fs::read_to_string(gj.join("core/baglam-paketleri.json")) {
        let m: Value = serde_json::from_str(&t).unwrap();
        for p in m["paketler"].as_array().unwrap() {
            for k in ["cekirdek", "pointer"] {
                for a in p[k].as_array().unwrap() {
                    let a = a.as_str().unwrap();
                    let yol = match a.rsplit_once(':') {
                        Some((y, ar)) if ar.chars().all(|c| c.is_ascii_digit() || c == '-') => y,
                        _ => a,
                    };
                    // `../x` kök düzeyine düşer
                    let hedef = gj.join(yol);
                    if let Ok(rel) = std::fs::canonicalize(&hedef) {
                        let rel = PathBuf::from(rel.to_string_lossy().trim_start_matches(r"\\?\"));
                        if let Ok(r) = rel.strip_prefix(&gk) {
                            kopya(&gk, &kok, &ileri(r));
                        }
                    }
                }
            }
        }
    }
    Kum { kok, jarvis }
}

pub struct Adim {
    pub stdin: String,
    pub env: Vec<(String, String)>,
    pub args: Vec<String>,
    pub dosyalar: Vec<(String, String)>,
    pub stderr_atla: bool,
    pub stdout_atla: bool,
}

pub fn adim(stdin: &str) -> Adim {
    Adim { stdin: stdin.to_string(), env: vec![], args: vec![], dosyalar: vec![], stderr_atla: false, stdout_atla: false }
}
impl Adim {
    pub fn env(mut self, k: &str, v: &str) -> Self {
        self.env.push((k.into(), v.into()));
        self
    }
    pub fn arg(mut self, a: &str) -> Self {
        self.args.push(a.into());
        self
    }
    pub fn dosya(mut self, rel: &str, icerik: &str) -> Self {
        self.dosyalar.push((rel.into(), icerik.into()));
        self
    }
    pub fn tam_atla(mut self) -> Self {
        self.stderr_atla = true;
        self.stdout_atla = true;
        self
    }
    pub fn atla(mut self) -> Self {
        self.stderr_atla = true;
        self
    }
}

pub struct Cikti {
    pub out: String,
    pub err: String,
    pub kod: i32,
}

fn sablon(s: &str, k: &Kum) -> String {
    s.replace("{R}", &ileri(&k.jarvis)).replace("{K}", &ileri(&k.kok)).replace("{EV}", &ev())
}

fn komut(h: H, eski: bool, k: &Kum, args: &[String]) -> Command {
    let j = ileri(&k.jarvis);
    let hook = |ad: &str| format!("{j}/.claude/hooks/{ad}");
    let yeni = |olay: &str| {
        let mut c = Command::new(env!("CARGO_BIN_EXE_jarvis-hook"));
        c.arg(olay);
        c
    };
    let mut c = match (h, eski) {
        (H::CoreTel, true) => bash(hook("pretool-core-tel.sh")),
        (H::AjanFren, true) => bash(hook("pretool-ajan-fren.sh")),
        (H::Altajan, true) => bash(hook("pretool-altajan-okuma.sh")),
        (H::Buyuk, true) => bash(hook("stop-buyuk-harf.sh")),
        (H::Talimat, true) => bash(hook("instructions-loaded.sh")),
        (H::Userprompt, true) => bash(hook("userprompt-dosya.sh")),
        (H::Session, true) => bash(hook("session-start.sh")),
        (H::Paket, true) => py(format!("{j}/tools/paket-yonlendir.py"), &j),
        (H::Dispatch, true) => bash(format!("{}/bin/hook-dispatch.sh", ileri(&k.kok))),
        (H::Prompt, true) => py(format!("{j}/tools/prompt-dosya.py"), &j),
        (H::Dispatch, false) => {
            let mut c = Command::new(env!("CARGO_BIN_EXE_hook-dispatch"));
            c.args(["--kok", &ileri(&k.kok)]);
            c
        }
        (H::CoreTel, false) => yeni("pretool-core-tel"),
        (H::AjanFren, false) => yeni("pretool-ajan-fren"),
        (H::Altajan, false) => yeni("pretool-altajan-okuma"),
        (H::Buyuk, false) => yeni("stop-buyuk-harf"),
        (H::Talimat, false) => yeni("instructions-loaded"),
        (H::Userprompt, false) => yeni("userprompt"),
        (H::Session, false) => yeni("session-start"),
        (H::Paket, false) => {
            let mut c = yeni("paket-yonlendir");
            c.args(["--repo", &j]);
            c
        }
        (H::Prompt, false) => {
            let mut c = yeni("prompt-dosya");
            c.args(["--repo", &j]);
            c
        }
    };
    c.args(args);
    c.current_dir(&k.jarvis);
    c.env("CLAUDE_PROJECT_DIR", &k.jarvis);
    c.env("PYTHONUTF8", "1");
    for v in ["JARVIS_HOOK_TEST", "JARVIS_FREN_UYARI", "JARVIS_FREN_DURDUR", "JARVIS_FREN_KAPALI"] {
        c.env_remove(v);
    }
    c
}

fn bash(yol: String) -> Command {
    let mut c = Command::new("bash");
    c.arg(yol);
    c
}
fn py(yol: String, j: &str) -> Command {
    let mut c = Command::new("python");
    c.arg(yol);
    c.args(["--repo", j]);
    c
}

fn calistir(mut c: Command, girdi: &str) -> Cikti {
    c.stdin(Stdio::piped()).stdout(Stdio::piped()).stderr(Stdio::piped());
    let mut ch = c.spawn().expect("başlatılamadı");
    let mut si = ch.stdin.take().unwrap();
    let b = girdi.as_bytes().to_vec();
    let t = std::thread::spawn(move || {
        let _ = si.write_all(&b);
    });
    let o = ch.wait_with_output().unwrap();
    let _ = t.join();
    Cikti { out: String::from_utf8_lossy(&o.stdout).into_owned(), err: String::from_utf8_lossy(&o.stderr).into_owned(), kod: o.status.code().unwrap_or(-1) }
}

fn norm(s: &str, k: &Kum) -> String {
    let mut s = s.replace('\r', "");
    // Rust-only brif satırı (durum #15, sabit güncellik): Python düşüş yolunda yok
    s = s.split_inclusive('\n').filter(|l| !l.starts_with("SABİT-GÜNCELLİK")).collect();
    for v in [k.kok.to_string_lossy().into_owned(), ileri(&k.kok), k.kok.to_string_lossy().replace('\\', "\\\\")] {
        s = s.replace(&v, "<K>");
    }
    s
}

fn dosyalar(k: &Kum) -> BTreeMap<String, String> {
    let mut m = BTreeMap::new();
    for alt in ["veri", ".claude/hooks/state"] {
        gez(&k.jarvis.join(alt), &k.jarvis, k, &mut m);
    }
    m
}

fn gez(d: &Path, kokj: &Path, k: &Kum, m: &mut BTreeMap<String, String>) {
    let Ok(rd) = std::fs::read_dir(d) else { return };
    for e in rd.flatten() {
        let p = e.path();
        if p.is_dir() {
            gez(&p, kokj, k, m);
            continue;
        }
        let rel = ileri(p.strip_prefix(kokj).unwrap());
        let t = std::fs::read_to_string(&p).unwrap_or_default();
        let ad = rel.rsplit('/').next().unwrap_or("");
        let icerik = if rel.ends_with(".jsonl") {
            t.lines()
                .filter(|l| !l.trim().is_empty())
                .map(|l| match serde_json::from_str::<Value>(l) {
                    Ok(Value::Object(mut o)) => {
                        o.remove("ts");
                        o.remove("ts_utc");
                        py_dumps(&Value::Object(o))
                    }
                    _ => l.to_string(),
                })
                .collect::<Vec<_>>()
                .join("\n")
        } else if rel.ends_with(".json") {
            serde_json::from_str::<Value>(&t).map(|v| py_dumps(&v)).unwrap_or(t.clone())
        } else {
            t
        };
        let _ = ad;
        m.insert(rel, norm(&icerik, k));
    }
}

/// Aynı adımları iki kum havuzunda (eski/yeni) koştur, her adımdan sonra çıktıları ve dosya durumunu karşılaştır.
pub fn fark(h: H, ad: &str, hazirla: &dyn Fn(&Kum), adimlar: Vec<Adim>) {
    let (ke, ky) = (kum(ad, "eski"), kum(ad, "yeni"));
    hazirla(&ke);
    hazirla(&ky);
    for (i, a) in adimlar.iter().enumerate() {
        for k in [&ke, &ky] {
            for (rel, ic) in &a.dosyalar {
                let y = k.jarvis.join(rel);
                std::fs::create_dir_all(y.parent().unwrap()).unwrap();
                std::fs::write(y, sablon(ic, k)).unwrap();
            }
        }
        let mut sonuc = vec![];
        for (eski, k) in [(true, &ke), (false, &ky)] {
            let args: Vec<String> = a.args.iter().map(|x| sablon(x, k)).collect();
            let mut c = komut(h, eski, k, &args);
            for (kk, vv) in &a.env {
                c.env(kk, sablon(vv, k));
            }
            sonuc.push(calistir(c, &sablon(&a.stdin, k)));
        }
        let (e, y) = (&sonuc[0], &sonuc[1]);
        let etiket = format!("{h:?} [{ad}] adım {i}");
        if let (H::Session, true) = (h, norm(&e.out, &ke) != norm(&y.out, &ky)) {
            // eski betik Windows'ta Python satırlarını CRLF yazar; 2000 bayt kapısı CR'leri de sayar -> eski çıktı daha kısa kesilebilir
            let (en, yn) = (norm(&e.out, &ke), norm(&y.out, &ky));
            assert!(yn.starts_with(&en) && e.out.len() >= 1990, "{etiket}: session-start kesim farkı
 eski:{en}
 yeni:{yn}");
        } else if !a.stdout_atla {
            assert_eq!(norm(&e.out, &ke), norm(&y.out, &ky), "{etiket}: stdout");
        }
        assert_eq!(e.kod, y.kod, "{etiket}: çıkış kodu (eski stderr: {})", e.err);
        if !a.stderr_atla {
            assert_eq!(norm(e.err.trim_end(), &ke), norm(y.err.trim_end(), &ky), "{etiket}: stderr");
        }
        assert_eq!(dosyalar(&ke), dosyalar(&ky), "{etiket}: kütük/durum dosyaları");
        SAYAC.fetch_add(1, Ordering::SeqCst);
        *HOOK_SAYAC.lock().unwrap().entry(format!("{h:?}")).or_insert(0) += 1;
    }
    let _ = std::fs::remove_dir_all(&ke.kok);
    let _ = std::fs::remove_dir_all(&ky.kok);
}

pub fn bos(_: &Kum) {}
