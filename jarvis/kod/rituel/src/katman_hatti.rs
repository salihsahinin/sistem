//! `tools/katman-hatti.py` karşılığı: silver/gold katmanını BRONZ'dan uçtan uca yeniden üreten sabit sıralı hat.
//! Kira (`veri/.kira-katman-hatti.json`, O_EXCL, TTL 600 sn, bekleme 60 sn/2 sn, çıkış 5), hijyen (ANALYZE + PRAGMA optimize),
//! `[durum  ] ad  süre  komut` satırları, `--json` tek nesne. Çıkış: ilk FAIL-LOUD adımın kodu · 5 kira alınamadı · 2 bilinmeyen --atla adı.
//! Taşınmış adımlar (hareket, seyir, saglik) yanındaki ikiliyle koşar (yoksa `<repo>/../target/release/`, o da yoksa Python betiği);
//! diğer adımlar Python betiği olarak çağrılmaya devam eder.
use crate::argparse::{Ayrisan, Secenek};
use crate::{harness_anahtar, py};
use jarvis_hook::ortak::py_dumps;
use serde_json::{Value, json};
use std::io::Write;
use std::path::{Path, PathBuf};
use std::process::{Command, Stdio};
use std::time::{Duration, Instant, SystemTime, UNIX_EPOCH};

type Adim = (&'static str, Vec<&'static str>);

fn adimlar() -> Vec<Adim> {
    vec![
        ("baglam", vec!["tools/baglam-tablo.py", "--sessiz"]),
        ("karar", vec!["tools/karar-borcu-tablo.py", "--sessiz"]),
        ("prompt", vec!["tools/prompt-tablo.py", "--sessiz"]),
        ("ambar", vec!["tools/ambar-tablo.py", "--sessiz"]),
        ("deneyim", vec!["tools/deneyim-tablo.py", "--sessiz"]),
        ("hareket", vec!["tools/hareket-tablo.py", "--sessiz"]),
        ("seyir", vec!["tools/baglam-seyir.py", "--sessiz"]),
        ("tarama", vec!["tools/tarama-plan.py", "--sessiz"]),
        ("saglik", vec!["tools/silver-saglik.py", "--sessiz"]),
        ("bag", vec!["tools/bag-tablo.py", "--sessiz"]),
        ("erisim", vec!["tools/erisim-fts.py", "--insa", "--eval", "--sessiz"]),
        (
            "graf",
            vec![
                "tools/pointer-graf.py", "--sessiz", "--d2-dizin", "graf/", "--kirik", "--render", "2", "--d2", "graf/pointer-sistemi-v0-tam.d2", "--kenar-listesi",
                "graf/pointer-sistemi-v0-kenarlar.txt",
            ],
        ),
        ("obsidian-harita", vec!["tools/obsidian-harita.py", "--sessiz"]),
        ("loop", vec!["tools/loop-dedektor.py", "--sessiz"]),
        ("anakronizm", vec!["tools/anakronizm-denetim.py", "--sessiz"]),
        ("devir-ani", vec!["tools/devir-ani.py", "--sessiz"]),
        ("olcum", vec!["tools/katman-olcum.py"]),
    ]
}

fn parquet_adimlar() -> Vec<Adim> {
    vec![
        ("parquet", vec!["tools/ambar-parquet.py", "--sessiz"]),
        ("kolon-olcum", vec!["tools/kolon-olcum.py", "--sessiz"]),
        ("tarama-duckdb", vec!["tools/tarama-plan-duckdb.py", "--sessiz"]),
    ]
}

/// Çıkış 0'da bile stderr'i uyarı kanalı olan adımlar.
const UYARI_KANALI_ADIMLAR: &[&str] = &["tarama", "saglik", "seyir", "anakronizm", "graf", "tarama-duckdb", "devir-ani"];
const KIRA_YOLU: &str = "veri/.kira-katman-hatti.json";
const KIRA_TTL_S: f64 = 600.0;

/// Rust'a taşınmış adım -> ikili adı.
fn ikili_adi(ad: &str) -> Option<&'static str> {
    match ad {
        "hareket" => Some("hareket-tablo"),
        "seyir" => Some("baglam-seyir"),
        "saglik" => Some("silver-saglik"),
        _ => None,
    }
}

fn tum_adlar() -> Vec<&'static str> {
    adimlar().into_iter().chain(parquet_adimlar()).map(|(a, _)| a).collect()
}

/// `atla_sec`: (bilinen, bilinmeyen).
fn atla_sec(secim: &str) -> (Vec<String>, Vec<String>) {
    let adlar: Vec<String> = secim.split(',').map(|x| py::strip(x).to_string()).filter(|x| !x.is_empty()).collect();
    let mut bilinen = tum_adlar();
    bilinen.push("hijyen");
    (adlar.iter().filter(|x| bilinen.contains(&x.as_str())).cloned().collect(), adlar.iter().filter(|x| !bilinen.contains(&x.as_str())).cloned().collect())
}

fn simdi() -> f64 {
    SystemTime::now().duration_since(UNIX_EPOCH).map(|d| d.as_secs_f64()).unwrap_or(0.0)
}

/// Python `round(x, 2)` (JSON çıktısı için ondalık-doğru yuvarlama).
fn yuvarla2(x: f64) -> f64 {
    format!("{x:.2}").parse().unwrap_or(x)
}

fn json_sayi(x: f64) -> Value {
    serde_json::Number::from_f64(x).map(Value::Number).unwrap_or(Value::Null)
}

/// Kira dosyasındaki `ts` değeri: Python `float(k.get("ts", 0) or 0)`; dönüştürülemezse `Err` (Python'da ValueError/TypeError).
fn ts_oku(k: &serde_json::Map<String, Value>) -> Result<f64, String> {
    match k.get("ts") {
        None | Some(Value::Null) | Some(Value::Bool(false)) => Ok(0.0),
        Some(Value::Bool(true)) => Ok(1.0),
        Some(Value::Number(n)) => Ok(n.as_f64().unwrap_or(0.0)),
        Some(Value::String(s)) if s.is_empty() => Ok(0.0),
        Some(Value::String(s)) => py::strip(s).parse::<f64>().map_err(|_| format!("float(): geçersiz ts {}", py::repr(s))),
        Some(Value::Array(a)) if a.is_empty() => Ok(0.0),
        Some(Value::Object(o)) if o.is_empty() => Ok(0.0),
        Some(_) => Err("float(): desteklenmeyen ts türü".into()),
    }
}

enum KiraSonuc {
    Alindi(PathBuf),
    /// çıkış kodu (5 ya da çöküş 1)
    Cik(i32),
}

fn kira_al(repo: &str) -> KiraSonuc {
    let yol = PathBuf::from(py::join(repo, KIRA_YOLU));
    let t0 = simdi();
    if let Some(ust) = yol.parent()
        && let Err(e) = std::fs::create_dir_all(ust)
    {
        return KiraSonuc::Cik(py::coker(&format!("{}: {e}", ust.display())));
    }
    loop {
        match std::fs::OpenOptions::new().write(true).create_new(true).open(&yol) {
            Ok(mut f) => {
                let icerik = py_dumps(&json!({"sahip": "katman-hatti", "pid": std::process::id(), "ts": simdi()}));
                if let Err(e) = f.write_all(icerik.as_bytes()) {
                    return KiraSonuc::Cik(py::coker(&format!("{}: {e}", yol.display())));
                }
                return KiraSonuc::Alindi(yol);
            }
            Err(e) if e.kind() == std::io::ErrorKind::AlreadyExists => {
                let k: serde_json::Map<String, Value> = match std::fs::read(&yol).ok().and_then(|b| serde_json::from_slice::<Value>(&b).ok()) {
                    Some(Value::Object(o)) => o,
                    Some(_) => return KiraSonuc::Cik(py::coker("kira dosyası JSON nesnesi değil (AttributeError)")),
                    None => Default::default(),
                };
                let ts = match ts_oku(&k) {
                    Ok(t) => t,
                    Err(e) => return KiraSonuc::Cik(py::coker(&e)),
                };
                if k.get("sahip").and_then(Value::as_str) != Some("salih") && simdi() - ts > KIRA_TTL_S {
                    match std::fs::remove_file(&yol) {
                        Ok(()) => {}
                        Err(e) if e.kind() == std::io::ErrorKind::NotFound => {}
                        Err(e) => return KiraSonuc::Cik(py::coker(&format!("{}: {e}", yol.display()))),
                    }
                    continue;
                }
                if simdi() - t0 > 60.0 {
                    let g = |a: &str| k.get(a).map(jarvis_hook::ortak::py_str).unwrap_or_else(|| "None".into());
                    py::err(&format!("[KIRA] {} dolu (sahip={} pid={}) — eşzamanlı katman-hatti koşulmaz (PK-5); sonra yeniden dene\n", py::join("veri", ".kira-katman-hatti.json"), g("sahip"), g("pid")));
                    return KiraSonuc::Cik(5);
                }
                std::thread::sleep(Duration::from_secs(2));
            }
            Err(e) => return KiraSonuc::Cik(py::coker(&format!("{}: {e}", yol.display()))),
        }
    }
}

fn kira_birak(yol: &Path) {
    let _ = std::fs::remove_file(yol);
}

fn yorumlayici_sec(repo: &str, ad: &str) -> String {
    if parquet_adimlar().iter().any(|(x, _)| *x == ad) {
        let mut adaylar = vec![py::join(&py::join(&py::join(repo, ".venv"), "bin"), "python")];
        if cfg!(windows) {
            adaylar.push(py::join(&py::join(&py::join(repo, ".venv"), "Scripts"), "python.exe"));
        }
        if let Some(y) = adaylar.into_iter().find(|y| Path::new(y).exists()) {
            return y;
        }
    }
    match std::env::var("PYTHON") {
        Ok(p) if !p.is_empty() => p,
        _ => (if cfg!(windows) { "python" } else { "python3" }).to_string(),
    }
}

/// (durum etiketi, hat düşer mi)
fn adim_durumu(ad: &str, kod: i32) -> (String, bool) {
    if kod == 0 {
        return ("OK".into(), false);
    }
    if (ad == "parquet" || ad == "tarama-duckdb") && kod == 4 {
        return ("ATLANDI".into(), false);
    }
    if ad == "anakronizm" && kod == 3 {
        return ("UYARI".into(), false);
    }
    (format!("KOD {kod}"), true)
}

/// Taşınmış adımın ikilisi: yanındaki dizin, sonra `<repo>/../target/release/`.
fn ikili_bul(repo: &str, ikili: &str) -> Option<PathBuf> {
    let dosya = if cfg!(windows) { format!("{ikili}.exe") } else { ikili.to_string() };
    let mut adaylar = vec![];
    if let Ok(exe) = std::env::current_exe()
        && let Some(d) = exe.parent()
    {
        adaylar.push(d.join(&dosya));
    }
    adaylar.push(PathBuf::from(repo).join("..").join("target").join("release").join(&dosya));
    adaylar.into_iter().find(|p| p.is_file())
}

fn yaz(insan_err: bool, s: &str) {
    if insan_err { py::err(&format!("{s}\n")) } else { py::print(s) }
}

/// Python `s[-n:]`.
fn son(s: &str, n: usize) -> String {
    let c: Vec<char> = s.chars().collect();
    c[c.len().saturating_sub(n)..].iter().collect()
}

fn hijyen(repo: &str, atla: &str, insan_err: bool) -> i32 {
    if atla.split(',').map(py::strip).any(|x| x == "hijyen") {
        yaz(insan_err, "[atla  ] hijyen");
        return 0;
    }
    let db = py::join(&py::join(repo, "veri"), "baglam.sqlite");
    if !Path::new(&db).exists() {
        yaz(insan_err, "[ATLANDI] hijyen        DB yok");
        return 0;
    }
    let t0 = Instant::now();
    let sonuc = (|| -> rusqlite::Result<i64> {
        let con = rusqlite::Connection::open(&db)?;
        con.execute_batch("ANALYZE")?;
        con.execute_batch("PRAGMA optimize")?;
        con.query_row("SELECT COUNT(*) FROM sqlite_stat1", [], |r| r.get(0))
    })();
    let dt = t0.elapsed().as_secs_f64();
    match sonuc {
        Ok(n) => yaz(insan_err, &format!("[OK     ] hijyen {dt:6.1}s  ANALYZE + PRAGMA optimize (sqlite_stat1 {n} satır)")),
        Err(e) => yaz(insan_err, &format!("[UYARI  ] hijyen {dt:6.1}s  {e}")),
    }
    0
}

fn ayrisan() -> Ayrisan {
    const ATLA_YARDIM: &str = "virgüllü adım adları (baglam,karar,prompt,ambar,deneyim,hareket,seyir,tarama,saglik,bag,erisim,graf,obsidian-harita,loop,anakronizm,devir-ani,olcum,parquet,kolon-olcum,tarama-duckdb)";
    Ayrisan::yeni(
        "katman-hatti.py",
        None,
        vec![
            Secenek::deger(&["--repo"], "repo", None),
            Secenek::deger(&["--atla"], "atla", Some(ATLA_YARDIM)),
            Secenek::deger(&["--snapshot"], "snapshot", Some("karar-borcu-tablo/olcum için tarih (determinizm)")),
            Secenek::bayrak(&["--parquet"], "parquet", Some("(geriye-uyum; Karar 83 B2'den beri varsayılan zaten AÇIK)")),
            Secenek::bayrak(&["--parquet-yok"], "parquet_yok", Some("kolon katmanını kapat (Karar 83 B2: varsayılan AÇIK; duckdb yoksa zaten ATLANDI)")),
            Secenek::bayrak(&["--json"], "json", Some("axi-standardı (İB-58): stdout = TEK makine-okur JSON nesnesi; insan satırları/ilerleme stderr'e")),
        ],
    )
}

pub fn kos(argv: &[String]) -> i32 {
    let a = match ayrisan().ayristir(argv) {
        Ok(a) => a,
        Err(k) => return k,
    };
    let repo = py::abspath(&a.metin("repo").map(String::from).unwrap_or_else(harness_anahtar::jarvis));
    let atla_ham = a.metin("atla").unwrap_or("").to_string();
    let json_mod = a.bayrak("json");
    let snapshot = a.metin("snapshot").filter(|s| !s.is_empty()).map(String::from);
    let t_bas = Instant::now();
    let mut kayitlar: Vec<Value> = vec![];
    let (atla, bilinmeyen) = atla_sec(&atla_ham);
    if !bilinmeyen.is_empty() {
        py::err(&format!("HATA: bilinmeyen --atla adı: {} · geçerli adlar: {}\n", bilinmeyen.join(", "), tum_adlar().join(",")));
        return 2;
    }
    for ad in &atla {
        yaz(json_mod, &format!("[atla ] {ad}"));
        kayitlar.push(json!({"adim": ad, "durum": "atla", "sure_s": json_sayi(0.0), "kod": Value::Null, "uyari": false}));
    }
    let mut kod = 0;
    let kira = match kira_al(&repo) {
        KiraSonuc::Alindi(y) => y,
        KiraSonuc::Cik(k) => return k,
    };
    let cikis = (|| -> i32 {
        let mut secili = adimlar();
        if !a.bayrak("parquet_yok") {
            let i = secili.iter().position(|(ad, _)| *ad == "olcum").unwrap_or(secili.len());
            for (n, p) in parquet_adimlar().into_iter().enumerate() {
                secili.insert(i + n, p);
            }
        }
        for (ad, cmd) in secili.into_iter().filter(|(ad, _)| !atla.iter().any(|x| x == ad)) {
            if ad == "olcum" {
                kod = kod.max(hijyen(&repo, &atla_ham, json_mod));
            }
            let mut args: Vec<String> = cmd.iter().map(|s| s.to_string()).collect();
            if snapshot.is_some() && ad == "karar" {
                args.extend(["--snapshot".into(), snapshot.clone().unwrap()]);
            }
            if snapshot.is_some() && ad == "olcum" {
                args.extend(["--simdi".into(), format!("{}T00:00:00", snapshot.clone().unwrap())]);
            }
            let rust_ikili = ikili_adi(ad).and_then(|i| ikili_bul(&repo, i).map(|y| (i, y)));
            let (mut komut, yanki) = match &rust_ikili {
                Some((adi, yol)) => {
                    let mut c = Command::new(yol);
                    c.args(&args[1..]);
                    (c, format!("{adi} {}", args[1..].join(" ")))
                }
                None => {
                    let mut c = Command::new(yorumlayici_sec(&repo, ad));
                    c.args(&args);
                    (c, args.join(" "))
                }
            };
            komut.current_dir(&repo).stdin(Stdio::null());
            let t0 = Instant::now();
            let r = match komut.output() {
                Ok(r) => r,
                Err(e) => return py::coker(&format!("{ad}: alt süreç başlatılamadı: {e}")),
            };
            let dt = t0.elapsed().as_secs_f64();
            let (so, se) = match (String::from_utf8(r.stdout), String::from_utf8(r.stderr)) {
                (Ok(o), Ok(e)) => (py::evrensel_satir(&o), py::evrensel_satir(&e)),
                _ => return py::coker(&format!("{ad}: çıktı UTF-8 değil (UnicodeDecodeError)")),
            };
            let rc = r.status.code().unwrap_or(-1);
            let (durum, duser) = adim_durumu(ad, rc);
            let uyari = rc != 0 || (UYARI_KANALI_ADIMLAR.contains(&ad) && !py::strip(&se).is_empty());
            let stderr_son = if uyari { son(py::strip(&se), 300) } else { String::new() };
            kayitlar.push(json!({"adim": ad, "durum": durum, "sure_s": json_sayi(yuvarla2(dt)), "kod": rc, "uyari": uyari, "stderr_son": stderr_son}));
            yaz(json_mod, &format!("[{}] {} {dt:5.1}s  {yanki}", py::sola_hizala(&durum, 7), py::sola_hizala(ad, 11)));
            if !py::strip(&so).is_empty() && (rc != 0 || ad == "olcum") {
                let g = py::strip(&so).replace('\n', "\n        ");
                yaz(json_mod, &format!("        {}", py::ilk(&g, 2000)));
            }
            if uyari {
                yaz(json_mod, &format!("        STDERR: {}", son(py::strip(&se), 600)));
            }
            if duser {
                if kod == 0 {
                    kod = rc;
                }
                if ad == "baglam" {
                    break;
                }
            }
        }
        if json_mod {
            let head = {
                let mut c = Command::new("git");
                c.args(["rev-parse", "--short", "HEAD"]).current_dir(&repo).stdin(Stdio::null());
                match c.output() {
                    Ok(o) => match String::from_utf8(o.stdout) {
                        Ok(s) => json!(py::strip(&py::evrensel_satir(&s))),
                        Err(_) => Value::Null,
                    },
                    Err(_) => Value::Null,
                }
            };
            let ok_n = kayitlar.iter().filter(|k| k["durum"] == "OK").count();
            let uyari_n = kayitlar.iter().filter(|k| k["uyari"] == true).count();
            py::print(&py_dumps(&json!({
                "arac": "katman-hatti", "surum": "v1", "git_head": head, "cikis": kod, "sure_s": json_sayi(yuvarla2(t_bas.elapsed().as_secs_f64())),
                "adim_n": kayitlar.len(), "ok_n": ok_n, "uyari_n": uyari_n, "adimlar": kayitlar.clone(),
            })));
        }
        kod
    })();
    kira_birak(&kira);
    cikis
}
