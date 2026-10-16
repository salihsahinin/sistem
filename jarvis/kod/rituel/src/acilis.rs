//! `tools/acilis-kapilari.py` karşılığı: seans-acilis §1.4 / §1.5 / §2.3b deterministik açılış kapıları (İB-91, Karar 96 M2 A4).
//! K1 canlı-oturum · K2 manifest · K3 silver. TESPİT eder, koşmaz. Çıkış: 0 temiz · 1 uyarı (ŞÜPHE ∨ KOŞMUŞ-ADAY ∨ BAYAT) · 2 repo okunamadı.
use crate::argparse::{Ayrisan, Secenek};
use crate::{harness_anahtar, py};
use chrono::{DateTime, Local, NaiveDateTime};
use jarvis_hook::ortak::{py_dumps, realpath};
use regex::Regex;
use serde_json::{Map, Value, json};
use std::path::{Path, PathBuf};
use std::process::Command;
use std::time::UNIX_EPOCH;

fn ayrisan() -> Ayrisan {
    Ayrisan::yeni(
        "acilis-kapilari.py",
        None,
        vec![
            Secenek::deger(&["--repo"], "repo", None),
            Secenek::deger(&["--is"], "anahtar", None),
            Secenek::tam(&["--dk"], "dk", None),
            Secenek::bayrak(&["--json"], "json", None),
        ],
    )
}

fn git(args: &[&str], repo: &Path) -> String {
    py::sh(args, repo)
}

/// Dakika cinsinden yaş: `int((simdi - t).total_seconds() // 60)`; ayrıştırılamazsa `None`.
fn yas_dk(ts: &str, simdi: &DateTime<Local>) -> Option<i128> {
    let t = DateTime::parse_from_rfc3339(py::strip(ts)).ok()?;
    let fark = simdi.timestamp_micros() as i128 - t.timestamp_micros() as i128;
    Some(fark.div_euclid(60_000_000))
}

fn ad_basi(ad: &str, onek: &str) -> bool {
    if cfg!(windows) { ad.to_lowercase().starts_with(&onek.to_lowercase()) } else { ad.starts_with(onek) }
}
fn ad_sonu(ad: &str, sonek: &str) -> bool {
    if cfg!(windows) { ad.to_lowercase().ends_with(&sonek.to_lowercase()) } else { ad.ends_with(sonek) }
}

/// Ek sinyal: `~/.claude/projects/<slug>*/*.jsonl` içinde son `dk` dakikada yazılmış dosya sayısı.
fn canli_transkript(repo: &str, dk: i128, simdi: &DateTime<Local>) -> i64 {
    let kok = PathBuf::from(harness_anahtar::projeler());
    let slug = harness_anahtar::anahtar(repo);
    let Ok(rd) = std::fs::read_dir(&kok) else { return 0 };
    let simdi_s = simdi.timestamp_micros() as f64 / 1e6;
    let esik = dk as f64 * 60.0;
    let mut n = 0;
    for d in rd.flatten() {
        if !ad_basi(&d.file_name().to_string_lossy(), &slug) {
            continue;
        }
        let Ok(alt) = std::fs::read_dir(d.path()) else { continue };
        for f in alt.flatten() {
            if !ad_sonu(&f.file_name().to_string_lossy(), ".jsonl") {
                continue;
            }
            if let Ok(m) = f.metadata().and_then(|m| m.modified())
                && let Ok(s) = m.duration_since(UNIX_EPOCH)
                && simdi_s - s.as_secs_f64() <= esik
            {
                n += 1;
            }
        }
    }
    n
}

fn kapsul_zamani(repo: &Path) -> String {
    let Ok(t) = std::fs::read_to_string(repo.join("core").join("durum-kapsulu.md")) else { return String::new() };
    let t = py::evrensel_satir(&t);
    let re = Regex::new(r"\*\*Güncelleme:\*\*\s*([0-9]{4}-[0-9]{2}-[0-9]{2})\s*~?([0-9]{1,2}):([0-9]{2})").unwrap();
    match re.captures(&t) {
        Some(m) => format!("{}T{:02}:{}", &m[1], m[2].parse::<u32>().unwrap_or(0), &m[3]),
        None => String::new(),
    }
}

fn kapi_canli(repo: &Path, repo_s: &str, dk: i128, simdi: &DateTime<Local>) -> Result<Map<String, Value>, String> {
    let mut r = Map::new();
    r.insert("kapi".into(), json!("K1-canli-oturum"));
    let log = git(&["log", "-5", "--format=%h|%cI|%s"], repo);
    if log.is_empty() {
        r.insert("durum".into(), json!("HATA"));
        r.insert("not".into(), json!("git log okunamadı"));
        return Ok(r);
    }
    // (sha, yaş, konu, alan)
    let mut commitler: Vec<(String, Option<i128>, String, String)> = vec![];
    for l in py::splitlines(&log) {
        let l = py::strip_kume(&l, "'");
        let mut p = l.splitn(3, '|');
        let (Some(h), Some(ci), Some(s)) = (p.next(), p.next(), p.next()) else { return Err("git log satırı `|` ile 3 alana bölünemedi".into()) };
        let dosyalar = git(&["show", "--name-only", "--format=", h], repo);
        let mut alan: Vec<String> = py::splitlines(&dosyalar)
            .iter()
            .filter(|y| !py::strip(y).is_empty())
            .map(|y| if let Some((a, _)) = y.split_once('/') { a.to_string() } else { "kök".to_string() })
            .collect();
        alan.sort();
        alan.dedup();
        let alan = if alan.is_empty() { "?".to_string() } else { alan.join("+") };
        commitler.push((h.to_string(), yas_dk(ci, simdi), py::ilk(s, 70), alan));
    }
    let son5: Vec<Value> = commitler.iter().map(|(h, y, k, a)| json!({"sha": h, "yas_dk": y.map(|v| json!(v as i64)).unwrap_or(Value::Null), "konu": k, "alan": a})).collect();
    r.insert("son5".into(), Value::Array(son5));
    let son_yas = commitler[0].1;
    // kapsül güncelleme zamanı
    let kap = kapsul_zamani(repo);
    r.insert("kapsul_guncelleme".into(), json!(if kap.is_empty() { "?" } else { &kap }));
    let mut kapsul_eski = false;
    if !kap.is_empty() {
        let ci = git(&["log", "-1", "--format=%cI"], repo);
        kapsul_eski = match (NaiveDateTime::parse_from_str(&kap, "%Y-%m-%dT%H:%M"), DateTime::parse_from_rfc3339(&ci)) {
            (Ok(k), Ok(c)) => k < c.naive_local(),
            _ => false,
        };
    }
    r.insert("kapsul_son_committen_eski".into(), json!(kapsul_eski));
    // ek sinyaller
    let canli_tr = canli_transkript(repo_s, dk, simdi);
    r.insert("canli_transkript".into(), json!(canli_tr));
    let wt: Vec<String> = py::splitlines(&git(&["worktree", "list"], repo)).into_iter().filter(|l| !py::strip(l).is_empty()).collect();
    let worktree = if wt.is_empty() { 0 } else { wt.len() - 1 };
    r.insert("worktree".into(), json!(worktree));
    // 09-17: yan oturum worktree'si main'in gerisindeyse eski kanon + eski hook yolları yüklenir (guvenlik-2 vakası) → kanıt kapısı.
    let mut geride_liste: Vec<(String, String, Option<bool>)> = vec![];
    for l in wt.iter().skip(1) {
        let yol = l.split(py::bosluk_mu).find(|s| !s.is_empty()).unwrap_or("");
        let dal = if l.contains('[') { py::rstrip_kume(l.rsplit('[').next().unwrap_or(""), "]").to_string() } else { "HEAD".to_string() };
        let g = git(&["rev-list", "--count", &format!("{dal}..main")], repo);
        let geride = if g.is_empty() { "?".to_string() } else { g };
        let hook_eski = std::fs::read_to_string(Path::new(yol).join(".claude").join("settings.json")).ok().map(|t| !t.contains("CLAUDE_PROJECT_DIR"));
        geride_liste.push((yol.rsplit('/').next().unwrap_or("").to_string(), geride, hook_eski));
    }
    r.insert(
        "worktree_geride".into(),
        Value::Array(geride_liste.iter().map(|(a, g, h)| json!([a, g, h.map(Value::Bool).unwrap_or(Value::Null)])).collect()),
    );
    let dallar = git(&["for-each-ref", "--format=%(refname:short)|%(committerdate:iso-strict)", "refs/heads", "refs/remotes/origin"], repo);
    let mut taze_dal: Vec<String> = vec![];
    for l in py::splitlines(&dallar) {
        let l = py::strip_kume(&l, "'");
        let Some((ad, ci)) = l.split_once('|') else { return Err("git for-each-ref satırı `|` ile bölünemedi".into()) };
        if ad == "origin" || ad == "main" || ad.ends_with("/main") || ad.ends_with("HEAD") {
            continue;
        }
        if let Some(y) = yas_dk(ci, simdi)
            && y <= 24 * 60
        {
            taze_dal.push(format!("{ad}({}s)", y.div_euclid(60)));
        }
    }
    taze_dal.truncate(6);
    r.insert("taze_dal_24s".into(), json!(taze_dal));
    let suphe = son_yas.is_some_and(|y| y <= dk) && kapsul_eski || canli_tr >= 2;
    r.insert("durum".into(), json!(if suphe { "ŞÜPHE" } else { "TEMİZ" }));
    let son_yas_s = son_yas.map(|v| v.to_string()).unwrap_or_else(|| "None".into());
    let mut not = if suphe {
        format!(
            "son commit {son_yas_s} dk önce, kapsül kapanışı {}; canlı transkript {canli_tr} (bu oturum dahil); worktree {worktree} — başka oturum açık mı? TEK soru; git add <yol> (H4)",
            if kapsul_eski { "eski" } else { "güncel" }
        )
    } else {
        format!("son commit {son_yas_s} dk önce; canlı transkript {canli_tr}")
    };
    for (ad, geride, hook_eski) in &geride_liste {
        if geride != "0" && geride != "?" || *hook_eski == Some(true) {
            not.push_str(&format!(
                " · worktree {ad} main'in {geride} commit gerisinde{} → yan oturumu kapat, dalı merge et, main'den yeni worktree (Karar 95 EK)",
                if *hook_eski == Some(true) { " + hook yolları eski (CLAUDE_PROJECT_DIR yok)" } else { "" }
            ));
        }
    }
    r.insert("not".into(), json!(not));
    Ok(r)
}

/// Python `re.search(r"(?i)\b(SAHADA|AÇIK|KOŞUYOR|YARIM)\b", t[:1500])`: IGNORECASE'in `i`/`ı`/`İ` denkliği dahil.
fn acik_gorunuyor(t: &str) -> bool {
    fn kat(c: char) -> char {
        let mut l = c.to_lowercase();
        let ilk = l.next().unwrap_or(c);
        if l.next().is_some() {
            return if c == '\u{130}' { 'i' } else { c };
        }
        match ilk {
            'ı' => 'i',
            'ſ' => 's',
            x => x,
        }
    }
    fn kelime(c: char) -> bool {
        c.is_alphanumeric() || c == '_'
    }
    let ham: Vec<char> = t.chars().take(1500).collect();
    let k: Vec<char> = ham.iter().map(|&c| kat(c)).collect();
    let kelimeler: Vec<Vec<char>> = ["SAHADA", "AÇIK", "KOŞUYOR", "YARIM"].iter().map(|s| s.chars().map(kat).collect()).collect();
    for i in 0..ham.len() {
        if !kelime(ham[i]) || (i > 0 && kelime(ham[i - 1])) {
            continue;
        }
        for w in &kelimeler {
            if k[i..].starts_with(w) && (i + w.len() == ham.len() || !kelime(ham[i + w.len()])) {
                return true;
            }
        }
    }
    false
}

fn kapi_manifest(repo: &Path, anahtar: &str) -> Result<Map<String, Value>, String> {
    let mut r = Map::new();
    r.insert("kapi".into(), json!("K2-manifest"));
    let dizin = repo.join("cc").join("pipeline");
    let mut mans: Vec<String> = std::fs::read_dir(&dizin)
        .map(|rd| rd.flatten().map(|e| e.file_name().to_string_lossy().into_owned()).filter(|n| ad_basi(n, "pipeline-") && ad_sonu(n, ".md")).collect())
        .unwrap_or_default();
    mans.sort();
    let oku = |n: &String| py::oku_yoksay(&dizin.join(n)).map_err(|e| format!("{}: {e}", dizin.join(n).display()));
    if !anahtar.is_empty() {
        let a = anahtar.to_lowercase();
        let mut hits: Vec<String> = vec![];
        for m in &mans {
            if oku(m)?.to_lowercase().contains(&a) {
                hits.push(m.clone());
            }
        }
        let logh: Vec<String> = py::splitlines(&git(&["log", "-15", "--format=%h %s"], repo)).into_iter().filter(|l| l.to_lowercase().contains(&a)).collect();
        r.insert("anahtar".into(), json!(anahtar));
        r.insert("manifest_eslesme".into(), json!(hits.iter().take(5).collect::<Vec<_>>()));
        r.insert("gitlog15_eslesme".into(), json!(logh.iter().take(5).map(|l| py::ilk(py::strip_kume(l, "'"), 80)).collect::<Vec<_>>()));
        r.insert("durum".into(), json!(if !hits.is_empty() || !logh.is_empty() { "KOŞMUŞ-ADAY" } else { "TEMİZ" }));
        r.insert(
            "not".into(),
            json!(format!("manifest {} · git log -15 {} eşleşme → varsa devral, koşma (vaka-3: 518k mükerrer)", hits.len(), logh.len())),
        );
    } else {
        let mut acik: Vec<String> = vec![];
        for m in &mans {
            if acik_gorunuyor(&oku(m)?) {
                acik.push(m.clone());
            }
        }
        r.insert("manifest_sayisi".into(), json!(mans.len()));
        r.insert("acik_gorunen".into(), json!(acik.iter().take(6).collect::<Vec<_>>()));
        r.insert("durum".into(), json!("TEMİZ"));
        r.insert("not".into(), json!("anahtar verilmedi; Workflow/atlas/pipeline açmadan --is \"<konu>\" ile koş"));
    }
    Ok(r)
}

fn kapi_silver(repo: &Path) -> Result<Map<String, Value>, String> {
    let mut r = Map::new();
    r.insert("kapi".into(), json!("K3-silver"));
    let head = git(&["rev-parse", "HEAD"], repo);
    let db = repo.join("veri").join("baglam.sqlite");
    if !db.exists() {
        r.insert("durum".into(), json!("YOK"));
        r.insert("not".into(), json!("veri/baglam.sqlite yok (worktree ya da ilk kurulum) → öğrenme oturumu koşmaz; geliştirme oturumu python3 tools/katman-hatti.py"));
        return Ok(r);
    }
    // Python `u[0][:7]`/`u[1][:16]`: metin olmayan sütun TypeError (çöker); burada `Err(None)` ile işaretlenir
    type Satir = Option<(Option<String>, Option<String>)>;
    let sorgu = || -> Result<Satir, rusqlite::Error> {
        let uri = format!("file:{}?mode=ro", db.display());
        let c = rusqlite::Connection::open_with_flags(uri, rusqlite::OpenFlags::SQLITE_OPEN_READ_ONLY | rusqlite::OpenFlags::SQLITE_OPEN_URI)?;
        let mut s = c.prepare("SELECT git_head_sha, uretim_zamani FROM uretim ORDER BY uretim_zamani DESC LIMIT 1")?;
        let mut rows = s.query([])?;
        match rows.next()? {
            Some(row) => {
                let metin = |i: usize| -> Result<Option<String>, rusqlite::Error> {
                    Ok(match row.get_ref(i)? {
                        rusqlite::types::ValueRef::Text(b) => Some(String::from_utf8_lossy(b).into_owned()),
                        _ => None,
                    })
                };
                Ok(Some((metin(0)?, metin(1)?)))
            }
            None => Ok(None),
        }
    };
    let u = match sorgu() {
        Ok(u) => u,
        Err(e) => {
            r.insert("durum".into(), json!("HATA"));
            // rusqlite açılış hatasına `: <uri>` ekler; Python yalnız SQLite iletisini verir
            let ileti = e.to_string();
            let ileti = ileti.split(": file:").next().unwrap_or("");
            r.insert("not".into(), json!(py::ilk(ileti, 80)));
            return Ok(r);
        }
    };
    let taze = u.as_ref().is_some_and(|(sha, _)| !head.is_empty() && sha.as_deref() == Some(head.as_str()));
    let (silver_sha, uretim) = match &u {
        Some((Some(a), Some(b))) => (py::ilk(a, 7), py::ilk(b, 16)),
        Some(_) => return Err("uretim satırında NULL/metin olmayan sütun (Python: TypeError)".into()),
        None => ("?".into(), "?".into()),
    };
    r.insert("silver_sha".into(), json!(silver_sha));
    r.insert("head".into(), json!(py::ilk(&head, 7)));
    r.insert("uretim".into(), json!(uretim));
    r.insert("durum".into(), json!(if taze { "TAZE" } else { "BAYAT" }));
    r.insert(
        "not".into(),
        json!(if taze { "" } else { "python3 tools/katman-hatti.py (~12 sn, idempotent; Karar 62 İB-27) — atlanırsa adresli erişim yanlış satır getirir" }),
    );
    Ok(r)
}

fn s<'a>(m: &'a Map<String, Value>, k: &str) -> &'a str {
    m.get(k).and_then(Value::as_str).unwrap_or("")
}

pub fn kos(argv: &[String]) -> i32 {
    let a = match ayrisan().ayristir(argv) {
        Ok(a) => a,
        Err(k) => return k,
    };
    let repo_ham = a.metin("repo").map(String::from).unwrap_or_else(harness_anahtar::jarvis);
    let ham = py::expanduser(&repo_ham);
    let repo = realpath(Path::new(if ham.is_empty() { "." } else { &ham }));
    let repo_s = repo.to_string_lossy().into_owned();
    // Karar 101 (F3): jarvis/ monorepo alt-dizini; .git kökte → git rev-parse ile doğrula
    match Command::new("git").args(["rev-parse", "--git-dir"]).current_dir(&repo).output() {
        Ok(o) if o.status.success() => {}
        Ok(_) => {
            py::print(&format!("repo okunamadı: {repo_s}"));
            return 2;
        }
        Err(e) => return py::coker(&format!("git çalıştırılamadı ({repo_s}): {e}")),
    }
    let dk = a.tam("dk").unwrap_or(15);
    let anahtar = a.metin("anahtar").unwrap_or("");
    let simdi = Local::now();
    let k1 = match kapi_canli(&repo, &repo_s, dk, &simdi) {
        Ok(k) => k,
        Err(e) => return py::coker(&e),
    };
    let k2 = match kapi_manifest(&repo, anahtar) {
        Ok(k) => k,
        Err(e) => return py::coker(&e),
    };
    let k3 = match kapi_silver(&repo) {
        Ok(k) => k,
        Err(e) => return py::coker(&e),
    };
    let kapilar = [k1, k2, k3];
    let uyari = kapilar.iter().any(|x| matches!(s(x, "durum"), "ŞÜPHE" | "KOŞMUŞ-ADAY" | "BAYAT"));
    let kod = if uyari { 1 } else { 0 };
    if a.bayrak("json") {
        let v = json!({"zaman": simdi.format("%Y-%m-%dT%H:%M%:z").to_string(), "kapilar": kapilar.iter().map(|m| Value::Object(m.clone())).collect::<Vec<_>>(), "uyari": uyari});
        py::print(&py_dumps(&v));
        return kod;
    }
    py::print(&format!("AÇILIŞ KAPILARI (İB-91) · {} · {repo_s}", simdi.format("%Y-%m-%d %H:%M")));
    let c = &kapilar[0];
    py::print(&format!("  [{}] K1 canlı-oturum — {}", s(c, "durum"), s(c, "not")));
    let Some(son5) = c.get("son5").and_then(Value::as_array) else { return py::coker("K1 sonucunda `son5` yok (KeyError)") };
    for x in son5 {
        let yas = match x["yas_dk"].as_i64() {
            Some(v) => v.to_string(),
            None => "?".into(),
        };
        py::print(&format!("        {}  {} dk  [{}] {}", x["sha"].as_str().unwrap_or(""), py::saga_hizala(&yas, 4), x["alan"].as_str().unwrap_or("?"), x["konu"].as_str().unwrap_or("")));
    }
    if let Some(t) = c.get("taze_dal_24s").and_then(Value::as_array).filter(|t| !t.is_empty()) {
        py::print(&format!("        24 saatte main-dışı dal: {}", t.iter().filter_map(Value::as_str).collect::<Vec<_>>().join(" · ")));
    }
    let m = &kapilar[1];
    py::print(&format!("  [{}] K2 manifest — {}", s(m, "durum"), s(m, "not")));
    for ad in ["manifest_eslesme", "gitlog15_eslesme", "acik_gorunen"] {
        if let Some(l) = m.get(ad).and_then(Value::as_array).filter(|l| !l.is_empty()) {
            py::print(&format!("        {ad}: {}", l.iter().filter_map(Value::as_str).collect::<Vec<_>>().join(" · ")));
        }
    }
    let v = &kapilar[2];
    let al = |k: &str| v.get(k).and_then(Value::as_str).unwrap_or("-").to_string();
    py::print(&format!("  [{}] K3 silver — silver {} / HEAD {} ({}) {}", s(v, "durum"), al("silver_sha"), al("head"), al("uretim"), s(v, "not")));
    kod
}
