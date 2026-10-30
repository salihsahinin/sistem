//! Fark testi ortak donanımı: eski araç (`tools/*.py`, Python) ile yeni ikili aynı girdiyle ve aynı başlangıç durumundaki iki ayrı kum havuzunda koşar;
//! stdout · stderr · çıkış kodu · yazılan dosyalar (`veri/`; zaman damgaları hariç) eşit olmalı. Python yoksa test başarısız olur (atlanmaz).
//! Kum havuzu: geçici "kök" (`<kök>/jarvis/...`, `<kök>/friday/...`, `.git` kökte), `<kök>/ev` sahte ev dizini (USERPROFILE/HOME).
#![allow(dead_code)]
use jarvis_hook::ortak::py_dumps;
use serde_json::Value;
use std::collections::BTreeMap;
use std::path::{Path, PathBuf};
use std::process::{Command, Stdio};
use std::sync::atomic::{AtomicUsize, Ordering};
use std::time::{Duration, SystemTime, UNIX_EPOCH};

pub static SAYAC: AtomicUsize = AtomicUsize::new(0);

#[derive(Clone, Copy, Debug)]
pub enum Arac {
    Acilis,
    Fifo,
    Ayna,
    Sayac,
}

impl Arac {
    fn py(self) -> &'static str {
        match self {
            Arac::Acilis => "acilis-kapilari",
            Arac::Fifo => "sicak-katman-fifo",
            Arac::Ayna => "hafiza-ayna",
            Arac::Sayac => "kural-sayaci",
        }
    }
    fn exe(self) -> &'static str {
        match self {
            Arac::Acilis => env!("CARGO_BIN_EXE_acilis-kapilari"),
            Arac::Fifo => env!("CARGO_BIN_EXE_sicak-katman-fifo"),
            Arac::Ayna => env!("CARGO_BIN_EXE_hafiza-ayna"),
            Arac::Sayac => env!("CARGO_BIN_EXE_kural-sayaci"),
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
    /// Python `harness_anahtar.anahtar(kök)` (alfanümerik olmayan -> `-`).
    pub fn kok_anahtar(&self) -> String {
        anahtar(&self.kok)
    }
    pub fn jarvis_anahtar(&self) -> String {
        anahtar(&self.jarvis)
    }
}

pub fn anahtar(p: &Path) -> String {
    let a = std::path::absolute(p).unwrap();
    a.to_string_lossy().chars().map(|c| if c.is_ascii_alphanumeric() { c } else { '-' }).collect()
}

pub fn simdi_epoch() -> i64 {
    SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs() as i64
}

/// Dakika sınırına bağımlı yaş hesaplarının (commit yaşı) iki koşum arasında kaymaması için dakikanın ilk saniyelerine hizalan;
/// dönen değer dakika başı epoch'u.
pub fn dakika_basi() -> i64 {
    loop {
        let s = simdi_epoch();
        if s % 60 <= 8 {
            return s - s % 60;
        }
        std::thread::sleep(Duration::from_millis(500));
    }
}

/// Eski/yeni koşum çifti dakika sınırını aşmasın (commit yaşı dakika cinsinden; temel commit tarihleri 60'ın katı):
/// dakikanın son saniyelerindeyse sonraki dakikanın başına dek bekle.
fn dakika_sinirindan_kac() {
    let s = simdi_epoch() % 60;
    if s >= 55 {
        std::thread::sleep(Duration::from_millis((61 - s) as u64 * 1000));
    }
}

pub fn mtime(p: &Path, epoch: i64) {
    let f = std::fs::OpenOptions::new().write(true).open(p).unwrap();
    f.set_modified(UNIX_EPOCH + Duration::from_secs(epoch as u64)).unwrap();
}

pub fn yaz(p: &Path, icerik: &[u8]) {
    std::fs::create_dir_all(p.parent().unwrap()).unwrap();
    std::fs::write(p, icerik).unwrap();
}

/// Git komutu; `epoch` verilirse yazar/işleyen tarihi sabitlenir (iki kumda aynı sha).
pub fn git(k: &Kum, args: &[&str], epoch: Option<i64>) -> String {
    git_dizin(&k.kok, args, epoch)
}

pub fn git_dizin(d: &Path, args: &[&str], epoch: Option<i64>) -> String {
    git_tarihli(d, args, epoch.map(|e| format!("{e} +0300")).as_deref())
}

/// `tarih`: git'in kabul ettiği `<epoch> <+HHMM>` metni.
pub fn git_tarihli(d: &Path, args: &[&str], tarih: Option<&str>) -> String {
    let mut c = Command::new("git");
    c.args(["-c", "core.autocrlf=false", "-c", "commit.gpgsign=false", "-c", "user.name=T", "-c", "user.email=t@t"]).args(args).current_dir(d);
    for v in ["GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE"] {
        c.env_remove(v);
    }
    if let Some(t) = tarih {
        c.env("GIT_AUTHOR_DATE", t).env("GIT_COMMITTER_DATE", t);
    }
    let o = c.output().expect("git başlatılamadı");
    assert!(o.status.success(), "git {args:?} başarısız: {}", String::from_utf8_lossy(&o.stderr));
    String::from_utf8_lossy(&o.stdout).into_owned()
}

/// Dosyayı yaz, ekle, işle.
pub fn isle(k: &Kum, rel: &str, icerik: &str, mesaj: &str, epoch: i64) {
    let y = k.yol(rel);
    yaz(&y, icerik.as_bytes());
    git(k, &["add", &ileri(&y)], None);
    git(k, &["commit", "-q", "-m", mesaj], Some(epoch));
}

pub const KAPSUL: &str = "# Durum kapsülü\n**Güncelleme:** 2026-10-16 ~9:05\n\n## Şu an\n- **Birinci iş** sürüyor: ayrıntı\n- **İkinci iş** bitti\n- düz madde başı\n\n## Sonraki\n- x\n";
pub const PANO: &str = "# Pano\n\n## AKTİF\n| K-1 | **Karar bir** | açık |\n| K-2 | iş iki | açık |\n\n## KAPALI\n| K-9 | eski | kapalı |\n";
pub const AGENTS: &str = "# Ajan\n1. **Kural bir**\n- yalnız bir kural\n\n| a | b |\n|---|---|\nDüz anlatı satırı.\n";
pub const HOOK: &str = "#!/bin/bash\necho \"merhaba dünya\"\n";

/// Geçici "kök" kur ve ortak başlangıç durumunu yaz (git deposu dahil; sha'lar iki kumda aynı).
pub fn kum(ad: &str, yan: &str) -> Kum {
    let kok = std::env::temp_dir().join(format!("jrit-{}-{ad}-{yan}", std::process::id()));
    let _ = std::fs::remove_dir_all(&kok);
    let (jarvis, ev) = (kok.join("jarvis"), kok.join("ev"));
    std::fs::create_dir_all(jarvis.join("veri")).unwrap();
    std::fs::create_dir_all(&ev).unwrap();
    let k = Kum { kok, jarvis, ev };
    // Eski betik kaynağı: canlı `jarvis/tools/` yoksa Python arşivi `arsiv/kod/python/tools/` (Karar 118 M2, 2026-10-30).
    let gj = gercek_kok().join("jarvis").join("tools");
    let arsiv = gercek_kok().join("arsiv").join("kod").join("python").join("tools");
    for t in ["harness_anahtar", "acilis-kapilari", "sicak-katman-fifo", "hafiza-ayna", "kural-sayaci"] {
        let hedef = k.jarvis.join("tools").join(format!("{t}.py"));
        let canli = gj.join(format!("{t}.py"));
        let kaynak = if canli.is_file() { canli } else { arsiv.join(format!("{t}.py")) };
        yaz(&hedef, &std::fs::read(&kaynak).unwrap_or_else(|e| panic!("{}: {e}", kaynak.display())));
    }
    git(&k, &["init", "-q", "-b", "main"], None);
    yaz(&k.yol("@kok/friday/notlar.md"), "friday\n".as_bytes());
    yaz(&k.yol("@kok/KOK.md"), "kök\n".as_bytes());
    git(&k, &["add", "friday/notlar.md", "KOK.md"], None);
    git(&k, &["commit", "-q", "-m", "ilk: friday + kök"], Some(1788000000));
    for (rel, ic) in [
        ("core/durum-kapsulu.md", KAPSUL),
        ("core/pano.md", PANO),
        ("AGENTS.md", AGENTS),
        ("CLAUDE.md", AGENTS),
        (".claude/settings.json", "{\"env\": \"CLAUDE_PROJECT_DIR\"}\n"),
        (".claude/hooks/session-start.sh", HOOK),
        ("cc/pipeline/pipeline-a.md", "# a\nDurum: SAHADA\n"),
        ("cc/pipeline/pipeline-b.md", "# b\nDurum: bitti\nkonu: araştırma\n"),
    ] {
        yaz(&k.yol(rel), ic.as_bytes());
    }
    git(&k, &["add", "jarvis/core", "jarvis/AGENTS.md", "jarvis/CLAUDE.md", "jarvis/.claude", "jarvis/cc"], None);
    git(&k, &["commit", "-q", "-m", "ikinci: jarvis dosyaları"], Some(1788003600));
    k
}

type Hazir = Box<dyn Fn(&Kum)>;

pub struct Adim {
    pub args: Vec<String>,
    pub env: Vec<(String, String)>,
    pub dosyalar: Vec<(String, Vec<u8>)>,
    pub silinecek: Vec<String>,
    pub mtimeler: Vec<(String, i64)>,
    pub hazir: Vec<Hazir>,
    pub kokte: bool,
    pub stderr_atla: bool,
}

pub fn adim(args: &[&str]) -> Adim {
    Adim { args: args.iter().map(|s| s.to_string()).collect(), env: vec![], dosyalar: vec![], silinecek: vec![], mtimeler: vec![], hazir: vec![], kokte: false, stderr_atla: false }
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
    pub fn mtime(mut self, rel: &str, epoch: i64) -> Self {
        self.mtimeler.push((rel.into(), epoch));
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

fn calistir(arac: Arac, eski: bool, k: &Kum, a: &Adim) -> Cikti {
    let args: Vec<String> = a.args.iter().map(|x| sablon(x, k)).collect();
    let mut c = if eski {
        let mut c = Command::new("python");
        c.arg(ileri(&k.jarvis.join("tools").join(format!("{}.py", arac.py()))));
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

/// Zaman damgası alanlarını ve başlık saatini maskele.
fn maskele(s: &str) -> String {
    let mut r = s.to_string();
    for anahtar in ["\"ts\": \"", "\"zaman\": \""] {
        let mut bas = 0;
        while let Some(i) = r[bas..].find(anahtar) {
            let b = bas + i + anahtar.len();
            let Some(j) = r[b..].find('"') else { break };
            r.replace_range(b..b + j, "<T>");
            bas = b + 3;
        }
    }
    if let Some(i) = r.find("(İB-91) · ") {
        let b = i + "(İB-91) · ".len();
        if r.len() >= b + 16 && r.is_char_boundary(b + 16) {
            r.replace_range(b..b + 16, "<T>");
        }
    }
    r
}

fn norm(s: &str, k: &Kum) -> String {
    let mut s = s.replace('\r', "");
    let (ka, ja) = (k.kok_anahtar(), k.jarvis_anahtar());
    let kok = k.kok.to_string_lossy().into_owned();
    for v in [kok.clone(), ileri(&k.kok), kok.replace('\\', "\\\\")] {
        s = s.replace(&v, "<K>");
    }
    s = s.replace(&ja, "<JA>").replace(&ka, "<KA>");
    maskele(&s)
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
        let t = std::fs::read_to_string(&p).unwrap_or_else(|_| String::from_utf8_lossy(&std::fs::read(&p).unwrap()).into_owned());
        let icerik = if rel.ends_with(".jsonl") {
            t.lines()
                .filter(|l| !l.trim().is_empty())
                .map(|l| match serde_json::from_str::<Value>(l) {
                    Ok(Value::Object(mut o)) => {
                        o.remove("ts");
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
        // içerik şablonu yalnız metin ise
        match std::str::from_utf8(ic) {
            Ok(t) => yaz(&y, sablon(t, k).as_bytes()),
            Err(_) => yaz(&y, ic),
        }
    }
    for (rel, e) in &a.mtimeler {
        mtime(&k.yol(&sablon(rel, k)), *e);
    }
    for h in &a.hazir {
        h(k);
    }
}

/// Aynı adımları iki kumda (eski/yeni) koştur; her adımdan sonra çıktı ve dosya durumunu karşılaştır.
/// Karşılaştırılan durum (adım) sayısını döndürür.
pub fn fark(arac: Arac, ad: &str, adimlar: Vec<Adim>) -> usize {
    let (ke, ky) = (kum(ad, "eski"), kum(ad, "yeni"));
    let n = fark_kumlarda(arac, &ke, &ky, adimlar);
    let _ = std::fs::remove_dir_all(&ke.kok);
    let _ = std::fs::remove_dir_all(&ky.kok);
    n
}

pub fn fark_kumlarda(arac: Arac, ke: &Kum, ky: &Kum, adimlar: Vec<Adim>) -> usize {
    let toplam = adimlar.len();
    for (i, a) in adimlar.iter().enumerate() {
        hazirla(ke, a);
        hazirla(ky, a);
        dakika_sinirindan_kac();
        let e = calistir(arac, true, ke, a);
        let y = calistir(arac, false, ky, a);
        let etiket = format!("{arac:?} adım {i} args={:?}", a.args);
        assert_eq!(norm(&e.out, ke), norm(&y.out, ky), "{etiket}: stdout");
        assert_eq!(e.kod, y.kod, "{etiket}: çıkış kodu (eski stderr: {})", e.err);
        if !a.stderr_atla {
            assert_eq!(norm(e.err.trim_end(), ke), norm(y.err.trim_end(), ky), "{etiket}: stderr");
        }
        assert_eq!(dosyalar(ke), dosyalar(ky), "{etiket}: yazılan dosyalar");
        SAYAC.fetch_add(1, Ordering::SeqCst);
    }
    toplam
}
