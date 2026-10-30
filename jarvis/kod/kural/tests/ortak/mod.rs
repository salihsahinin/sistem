//! Fark testi ortak donanımı: eski araç (Python) ile yeni ikili aynı girdiyle ve aynı başlangıç durumundaki iki ayrı kum havuzunda koşar;
//! stdout · stderr · çıkış kodu · yazılan dosyalar (`veri/`) eşit olmalı. Python yoksa test başarısız olur (atlanmaz).
//! Kum havuzu: geçici "kök" (`<kök>/jarvis/...`, kökte `.git`), `<kök>/ev` sahte ev dizini (USERPROFILE/HOME).
#![allow(dead_code)]
use jarvis_hook::ortak::py_dumps;
use serde_json::Value;
use std::collections::BTreeMap;
use std::path::{Path, PathBuf};
use std::process::{Command, Stdio};

#[derive(Clone, Copy, Debug)]
pub enum Arac {
    Tetik,
    Derece,
    SkillEsik,
    Paralel,
    Ad,
}

impl Arac {
    /// Python betiğinin jarvis'e göre yolu.
    pub fn py(self) -> &'static str {
        match self {
            Arac::Tetik => ".claude/skills/gorev-emri-derleme/scripts/tetik-denetim.py",
            Arac::Derece => ".claude/skills/halusinasyon-engelleyici/scripts/derece.py",
            Arac::SkillEsik => "tools/skill-esik.py",
            Arac::Paralel => "tools/paralel-kapi.py",
            Arac::Ad => "tools/ad-esitligi-denetim.py",
        }
    }
    pub fn exe(self) -> &'static str {
        match self {
            Arac::Tetik => env!("CARGO_BIN_EXE_tetik-denetim"),
            Arac::Derece => env!("CARGO_BIN_EXE_derece"),
            Arac::SkillEsik => env!("CARGO_BIN_EXE_skill-esik"),
            Arac::Paralel => env!("CARGO_BIN_EXE_paralel-kapi"),
            Arac::Ad => env!("CARGO_BIN_EXE_ad-esitligi-denetim"),
        }
    }
}

pub fn gercek_kok() -> PathBuf {
    let c = std::fs::canonicalize(Path::new(env!("CARGO_MANIFEST_DIR")).join("../../..")).unwrap();
    PathBuf::from(c.to_string_lossy().trim_start_matches(r"\\?\"))
}

pub fn ileri(p: &Path) -> String {
    p.to_string_lossy().replace('\\', "/")
}

pub struct Kum {
    pub kok: PathBuf,
    pub jarvis: PathBuf,
    pub ev: PathBuf,
}

impl Kum {
    /// `@ev/..` sahte ev, `@kok/..` kök, aksi halde jarvis altı.
    pub fn yol(&self, rel: &str) -> PathBuf {
        if let Some(r) = rel.strip_prefix("@ev/") {
            self.ev.join(r)
        } else if let Some(r) = rel.strip_prefix("@kok/") {
            self.kok.join(r)
        } else {
            self.jarvis.join(rel)
        }
    }
    pub fn kok_anahtar(&self) -> String {
        anahtar(&self.kok)
    }
    pub fn jarvis_anahtar(&self) -> String {
        anahtar(&self.jarvis)
    }
}

pub fn anahtar(p: &Path) -> String {
    std::path::absolute(p).unwrap().to_string_lossy().chars().map(|c| if c.is_ascii_alphanumeric() { c } else { '-' }).collect()
}

pub fn yaz(p: &Path, icerik: &[u8]) {
    std::fs::create_dir_all(p.parent().unwrap()).unwrap();
    std::fs::write(p, icerik).unwrap();
}

pub fn git(d: &Path, args: &[&str]) -> String {
    let mut c = Command::new("git");
    c.args(["-c", "core.autocrlf=false", "-c", "commit.gpgsign=false", "-c", "user.name=T", "-c", "user.email=t@t"]).args(args).current_dir(d);
    c.env("GIT_AUTHOR_DATE", "1788000000 +0300").env("GIT_COMMITTER_DATE", "1788000000 +0300");
    let o = c.output().expect("git başlatılamadı");
    assert!(o.status.success(), "git {args:?}: {}", String::from_utf8_lossy(&o.stderr));
    String::from_utf8_lossy(&o.stdout).into_owned()
}

/// Geçici "kök" kur: Python betikleri gerçek konumlarının aynısına kopyalanır; kökte git deposu (tek commit, sabit tarih).
pub fn kum(ad: &str, yan: &str) -> Kum {
    let kok = std::env::temp_dir().join(format!("jkur-{}-{ad}-{yan}", std::process::id()));
    let _ = std::fs::remove_dir_all(&kok);
    let (jarvis, ev) = (kok.join("jarvis"), kok.join("ev"));
    std::fs::create_dir_all(jarvis.join("veri")).unwrap();
    std::fs::create_dir_all(&ev).unwrap();
    let k = Kum { kok, jarvis, ev };
    let gj = gercek_kok().join("jarvis");
    // Eski betik kaynağı: canlı `jarvis/<yol>` yoksa Python arşivi `arsiv/kod/python/<yol>` (Karar 118 M2, 2026-10-30).
    let arsiv = gercek_kok().join("arsiv").join("kod").join("python");
    for arac in [Arac::Tetik, Arac::Derece, Arac::SkillEsik, Arac::Paralel, Arac::Ad] {
        let canli = gj.join(arac.py());
        let kaynak = if canli.is_file() { canli } else { arsiv.join(arac.py()) };
        yaz(&k.jarvis.join(arac.py()), &std::fs::read(&kaynak).unwrap_or_else(|e| panic!("{}: {e}", kaynak.display())));
    }
    yaz(&k.jarvis.join("tools/harness_anahtar.py"), &std::fs::read(gj.join("tools/harness_anahtar.py")).unwrap());
    git(&k.kok, &["init", "-q", "-b", "main"]);
    yaz(&k.kok.join("KOK.md"), b"kok\n");
    git(&k.kok, &["add", "KOK.md"]);
    git(&k.kok, &["commit", "-q", "-m", "ilk"]);
    k
}

type Hazir = Box<dyn Fn(&Kum)>;

pub struct Adim {
    pub args: Vec<String>,
    pub env: Vec<(String, String)>,
    pub dosyalar: Vec<(String, Vec<u8>)>,
    pub silinecek: Vec<String>,
    pub hazir: Vec<Hazir>,
    pub kokte: bool,
    pub stderr_atla: bool,
}

pub fn adim(args: &[&str]) -> Adim {
    Adim { args: args.iter().map(|s| s.to_string()).collect(), env: vec![], dosyalar: vec![], silinecek: vec![], hazir: vec![], kokte: false, stderr_atla: false }
}

impl Adim {
    pub fn env(mut self, k: &str, v: &str) -> Self {
        self.env.push((k.into(), v.into()));
        self
    }
    pub fn dosya(mut self, rel: &str, icerik: &str) -> Self {
        self.dosyalar.push((rel.into(), icerik.as_bytes().to_vec()));
        self
    }
    pub fn ikili(mut self, rel: &str, b: &[u8]) -> Self {
        self.dosyalar.push((rel.into(), b.to_vec()));
        self
    }
    pub fn sil(mut self, rel: &str) -> Self {
        self.silinecek.push(rel.into());
        self
    }
    pub fn hazir(mut self, f: impl Fn(&Kum) + 'static) -> Self {
        self.hazir.push(Box::new(f));
        self
    }
    /// Çalışma dizini kök (varsayılan jarvis).
    pub fn kokte(mut self) -> Self {
        self.kokte = true;
        self
    }
    /// stderr metni karşılaştırılmaz (Python traceback'i taklit edilmez; çıkış kodu ve stdout yine karşılaştırılır).
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
    s.replace("{R}", &ileri(&k.jarvis)).replace("{K}", &ileri(&k.kok)).replace("{EV}", &ileri(&k.ev)).replace("{JA}", &k.jarvis_anahtar()).replace("{KA}", &k.kok_anahtar())
}

pub fn calistir(arac: Arac, eski: bool, k: &Kum, a: &Adim) -> Cikti {
    let args: Vec<String> = a.args.iter().map(|x| sablon(x, k)).collect();
    let mut c = if eski {
        let mut c = Command::new("python");
        c.arg(ileri(&k.jarvis.join(arac.py())));
        c
    } else {
        Command::new(arac.exe())
    };
    c.args(&args).current_dir(if a.kokte { &k.kok } else { &k.jarvis });
    c.env("CLAUDE_PROJECT_DIR", &k.jarvis).env("PYTHONUTF8", "1").env("USERPROFILE", &k.ev).env("HOME", &k.ev);
    c.env_remove("COLUMNS");
    for (kk, vv) in &a.env {
        c.env(kk, sablon(vv, k));
    }
    c.stdin(Stdio::null()).stdout(Stdio::piped()).stderr(Stdio::piped());
    let o = c.output().expect("başlatılamadı");
    Cikti { out: String::from_utf8_lossy(&o.stdout).into_owned(), err: String::from_utf8_lossy(&o.stderr).into_owned(), kod: o.status.code().unwrap_or(-1) }
}

pub fn norm(s: &str, k: &Kum) -> String {
    let mut s = s.replace('\r', "");
    let (ka, ja) = (k.kok_anahtar(), k.jarvis_anahtar());
    let kok = k.kok.to_string_lossy().into_owned();
    for v in [kok.clone(), ileri(&k.kok), kok.replace('\\', "\\\\")] {
        s = s.replace(&v, "<K>");
    }
    s.replace(&ja, "<JA>").replace(&ka, "<KA>")
}

fn dosyalar(k: &Kum) -> BTreeMap<String, String> {
    let mut m = BTreeMap::new();
    gez(&k.jarvis.join("veri"), &k.jarvis, k, &mut m);
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
        // sqlite dosyaları ikili: yalnız boyut yerine içerik özeti karşılaştırmak anlamsız (yazılmamalı); yok say
        if rel.ends_with(".sqlite") {
            continue;
        }
        let t = String::from_utf8_lossy(&std::fs::read(&p).unwrap()).into_owned();
        let icerik = if rel.ends_with(".json") { serde_json::from_str::<Value>(&t).map(|v| py_dumps(&v)).unwrap_or(t.clone()) } else { t };
        m.insert(norm(&rel, k), norm(&icerik, k));
    }
}

fn hazirla(k: &Kum, a: &Adim) {
    for rel in &a.silinecek {
        let y = k.yol(&sablon(rel, k));
        if y.is_dir() {
            let _ = std::fs::remove_dir_all(&y);
        } else {
            let _ = std::fs::remove_file(&y);
        }
    }
    for (rel, ic) in &a.dosyalar {
        let y = k.yol(&sablon(rel, k));
        match std::str::from_utf8(ic) {
            Ok(t) => yaz(&y, sablon(t, k).as_bytes()),
            Err(_) => yaz(&y, ic),
        }
    }
    for h in &a.hazir {
        h(k);
    }
}

/// Aynı adımları iki kumda (eski/yeni) koştur; her adımdan sonra çıktı ve dosya durumunu karşılaştır. Karşılaştırılan durum sayısını döndürür.
pub fn fark(arac: Arac, ad: &str, adimlar: Vec<Adim>) -> usize {
    let (ke, ky) = (kum(ad, "eski"), kum(ad, "yeni"));
    for (i, a) in adimlar.iter().enumerate() {
        hazirla(&ke, a);
        hazirla(&ky, a);
        let e = calistir(arac, true, &ke, a);
        let y = calistir(arac, false, &ky, a);
        let etiket = format!("{arac:?} adım {i} args={:?}", a.args);
        assert_eq!(norm(&e.out, &ke), norm(&y.out, &ky), "{etiket}: stdout (eski stderr: {})", e.err);
        assert_eq!(e.kod, y.kod, "{etiket}: çıkış kodu (eski stderr: {})", e.err);
        if !a.stderr_atla {
            assert_eq!(norm(e.err.trim_end(), &ke), norm(y.err.trim_end(), &ky), "{etiket}: stderr");
        }
        assert_eq!(dosyalar(&ke), dosyalar(&ky), "{etiket}: yazılan dosyalar");
    }
    let _ = std::fs::remove_dir_all(&ke.kok);
    let _ = std::fs::remove_dir_all(&ky.kok);
    adimlar.len()
}
