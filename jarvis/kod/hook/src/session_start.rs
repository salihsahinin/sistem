//! `session-start.sh` karşılığı: SessionStart brifi, çıktı sert kapı `head -c 2000` (bayt).
use crate::ortak::{Ortam, Sonuc, bugun_yerel, ilk_n, oku_py, py_str, py_truthy};
use rusqlite::{Connection, OpenFlags, types::Value as SV};
use serde_json::Value;
use std::path::Path;
use std::process::Command;

const KAPI: usize = 2000;

fn git(repo: &Path, args: &[&str]) -> String {
    Command::new("git")
        .args(args)
        .current_dir(repo)
        .output()
        .map(|o| String::from_utf8_lossy(&o.stdout).trim().to_string())
        .unwrap_or_default()
}

fn sv_str(v: &SV) -> String {
    match v {
        SV::Null => "None".into(),
        SV::Integer(i) => i.to_string(),
        SV::Real(r) => {
            if r.fract() == 0.0 && r.abs() < 1e16 { format!("{r:.1}") } else { r.to_string() }
        }
        SV::Text(t) => t.clone(),
        SV::Blob(b) => format!("b'{}'", String::from_utf8_lossy(b)),
    }
}

fn sv_truthy(v: &SV) -> bool {
    match v {
        SV::Null => false,
        SV::Integer(i) => *i != 0,
        SV::Real(r) => *r != 0.0,
        SV::Text(t) => !t.is_empty(),
        SV::Blob(b) => !b.is_empty(),
    }
}

/// Python sqlite3 hata iletisi karşılığı.
fn hata_iletisi(e: &rusqlite::Error) -> String {
    match e {
        rusqlite::Error::SqliteFailure(f, Some(m)) => {
            if f.code == rusqlite::ErrorCode::CannotOpen {
                "unable to open database file".into()
            } else {
                m.clone()
            }
        }
        rusqlite::Error::SqliteFailure(f, None) => match f.code {
            rusqlite::ErrorCode::CannotOpen => "unable to open database file".into(),
            _ => e.to_string(),
        },
        other => other.to_string(),
    }
}

fn satir_oku(c: &Connection, sql: &str, n: usize) -> Result<Option<Vec<SV>>, rusqlite::Error> {
    let mut st = c.prepare(sql)?;
    let mut rows = st.query([])?;
    match rows.next()? {
        None => Ok(None),
        Some(r) => Ok(Some((0..n).map(|i| r.get::<_, SV>(i)).collect::<Result<Vec<_>, _>>()?)),
    }
}

fn kesim_satiri(repo: &Path) -> String {
    let yol = repo.join("veri").join("model-kesim.jsonl");
    let hata = |m: String| format!("ZAMAN-ZEMİNİ: kesim tablosu okunamadı ({m}) — veri/model-kesim.jsonl");
    let Some(t) = oku_py(&yol) else {
        return hata("[Errno 2] No such file or directory: 'veri/model-kesim.jsonl'".into());
    };
    let mut ks: Vec<(String, String)> = vec![];
    // Python `for l in open()` satırları; boş satır json.loads hatasıdır
    let mut parcalar: Vec<&str> = t.split('\n').collect();
    if parcalar.last() == Some(&"") {
        parcalar.pop();
    }
    for l in parcalar {
        let d: Value = match serde_json::from_str(l) {
            Ok(v) => v,
            Err(e) => {
                return hata(if l.trim().is_empty() {
                    format!("Expecting value: line 2 column 1 (char {})", l.chars().count() + 1)
                } else {
                    e.to_string()
                });
            }
        };
        let Some(tur) = d.get("kesim_turu") else { return hata("'kesim_turu'".into()) };
        if tur.as_str() == Some("reliable") {
            let Some(ad) = d.get("model_ad").and_then(Value::as_str) else { return hata("'model_ad'".into()) };
            let Some(tarih) = d.get("kesim_tarihi") else { return hata("'kesim_tarihi'".into()) };
            let ad = ad.replace("Claude ", "");
            let tarih = py_str(tarih);
            if let Some(e) = ks.iter_mut().find(|(a, _)| *a == ad) {
                e.1 = tarih;
            } else {
                ks.push((ad, tarih));
            }
        }
    }
    let liste: Vec<String> = ks.iter().map(|(a, b)| format!("{a} {b}")).collect();
    format!(
        "ZAMAN-ZEMİNİ (Karar 68): BUGÜN {} · kesim(reliable) {} · zaman-bağımlı iddia AS-OF damgasız ÇIKMAZ; model-hafızası = 'AS-OF ≤ kesim, doğrulanmadı' → canlı çek (../target/release/anakronizm-denetim)",
        bugun_yerel(),
        liste.join(" · ")
    )
}

fn python_kismi(repo: &Path) -> Vec<String> {
    let mut o: Vec<String> = vec![];
    let head = git(repo, &["rev-parse", "--short", "HEAD"]);
    let when = ilk_n(&git(repo, &["log", "-1", "--format=%ci"]), 16);
    let durum = git(repo, &["status", "-sb"]);
    let ilk = durum.lines().next().unwrap_or("").replacen("## ", "", 1);
    o.push(format!("HEAD: {head} ({when}) · {ilk}"));
    o.push(kesim_satiri(repo));
    o.extend(crate::sabit::brif_satiri(repo));
    let db = repo.join("veri").join("baglam.sqlite");
    let baglan = || Connection::open_with_flags(&db, OpenFlags::SQLITE_OPEN_READ_ONLY | OpenFlags::SQLITE_OPEN_URI | OpenFlags::SQLITE_OPEN_NO_MUTEX);
    let mut silver = || -> Result<(), rusqlite::Error> {
        let c = baglan()?;
        let u = satir_oku(&c, "SELECT git_head_sha, uretim_zamani FROM uretim ORDER BY uretim_zamani DESC LIMIT 1", 2)?;
        let taze = u.as_ref().is_some_and(|u| !head.is_empty() && sv_str(&u[0]).starts_with(&head));
        let (sha, zaman) = match &u {
            Some(u) => (ilk_n(&sv_str(&u[0]), 7), ilk_n(&sv_str(&u[1]), 16)),
            None => ("?".into(), "?".into()),
        };
        o.push(format!(
            "SİLVER: {sha} ({zaman}) → {}",
            if taze { "TAZE" } else { "BAYAT → python3 tools/katman-hatti.py (~12 sn; Karar 62 İB-27)" }
        ));
        if let Ok(Some(r)) = satir_oku(&c, "SELECT acik_salih_karari, acik_icra_borcu, son_teslim, son_kosum FROM v_amb_acilis_brifi LIMIT 1", 4) {
            let veya = |v: &SV, n: usize| if sv_truthy(v) { ilk_n(&sv_str(v), n) } else { "-".to_string() };
            o.push(format!("AS-OF: açık Salih kararı {} · açık icra borcu {} · son teslim {} · son koşum {}", sv_str(&r[0]), sv_str(&r[1]), veya(&r[2], 60), veya(&r[3], 50)));
        }
        let sag = (|| -> Result<String, rusqlite::Error> {
            let s = satir_oku(&c, "SELECT sonuc FROM silver_saglik_son WHERE test_id='T-C3-sicak'", 1)?;
            let q = satir_oku(&c, "SELECT COUNT(*) FROM silver_kuyruk", 1)?;
            let q = q.map(|r| sv_str(&r[0])).unwrap_or_default();
            let s = s.map(|r| sv_str(&r[0])).unwrap_or("?".into());
            Ok(format!("SİLVER-SAĞLIK: sıcak kalıntı {s} · kuyruk aday {q} (v_silver_kuyruk_ozet)"))
        })();
        if let Ok(l) = sag {
            o.push(l);
        }
        Ok(())
    };
    if let Err(e) = silver() {
        o.push(format!("SİLVER: okunamadı ({}) → python3 tools/katman-hatti.py", hata_iletisi(&e)));
    }
    // Karar 122 (2026-10-25): kapsül dondu; konum akış grafından (`durum oturum-basi`, ilk 4 satır: KONUM · DURUM · sıradakiler).
    let durum = Command::new(repo.join("..").join("target").join("release").join("durum.exe"))
        .args(["oturum-basi", "--alan", "jarvis"])
        .current_dir(repo)
        .output();
    match durum {
        Ok(c) if c.status.success() => {
            for l in String::from_utf8_lossy(&c.stdout).replace('\r', "").lines().take(3) {
                o.push(ilk_n(l, 160));
            }
        }
        _ => o.push("DURUM: durum.exe yok ya da hata → cargo build --release -p durum; konum ortak/akis-graf.json".into()),
    }
    let _ = oku_py;
    o
}

pub fn kos(o: &Ortam) -> Sonuc {
    let giris = match o.env("CLAUDE_CODE_ENTRYPOINT") {
        Some(x) if !x.is_empty() => x.to_string(),
        _ => "?".into(),
    };
    let mut satirlar: Vec<String> = vec![
        "=== JARVIS SessionStart (brif ≤2 KB; tam durum: durum oturum-basi --alan jarvis · ortak/akis-graf.json) ===".into(),
        "AD (Karar 93): Salih'le konuşan ajan = JARVİS (eski ad Carvis) · repo = 'depo'/'kanon' · denetim tools/ad-esitligi-denetim.py".into(),
        format!("YETKİ (m.41 GK-2): Claude Code (giriş: {giris}) = ANA-SIRA · kanon kararı = (ana-sıra ∧ en güçlü model, bugün Fable) ∨ Salih imzası · Katman-1 (core/, CLAUDE.md, tüzük) yalnız Salih · frenler: push Salih beyanıyla (m.9) · md.49 · PreToolUse teli · canlı paralel oturumda git add <yol> (H4)."),
    ];
    satirlar.extend(python_kismi(&o.repo));
    satirlar.push("OKU (CLAUDE.md §3): durum oturum-basi --alan jarvis → raporlar/seans/*.json → ritüel 'seans başı' (K1-K3; İB-91). Kapsül/pano dondu (Karar 122).".into());
    satirlar.push("=== /SessionStart ===".into());
    let mut tam = satirlar.join("\n");
    tam.push('\n');
    let mut b = tam.into_bytes();
    b.truncate(KAPI);
    let mut s = Sonuc::bos();
    s.cikti = b;
    let _ = py_truthy;
    s
}
