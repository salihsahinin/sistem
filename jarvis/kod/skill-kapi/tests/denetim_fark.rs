//! Fark testi: `kapi-denetim.py --json` ile `skill-kapi denetle --json` her skill için alan alan eşit olmalı
//! (anahtar sırası önemsiz) ve çıkış kodları aynı olmalı. Python yoksa test atlanır.
//! Tek normalleştirme: Python'da `set` sırası süreç başına rastgele olduğundan `warns` ve `R-referans-varligi`
//! mesajındaki eksik listesi sırasız karşılaştırılır.
use serde_json::Value;
use std::path::PathBuf;
use std::process::Command;

fn kok() -> PathBuf {
    PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../..")
}

fn python() -> Option<&'static str> {
    ["python3", "python"].into_iter().find(|p| {
        Command::new(p).arg("-c").arg("import sys; sys.exit(0 if sys.version_info[0] == 3 else 1)").output().is_ok_and(|o| o.status.success())
    })
}

/// "N referans denetlendi; eksik: ['a', 'b']" → eksik öğeleri sıralı (ayrıştırması kaba ama sıra-bağımsız).
fn mesaj_norm(msg: &str) -> String {
    match msg.split_once("; eksik: ") {
        Some((on, ek)) if ek.starts_with('[') => {
            let mut parcalar: Vec<&str> = ek.trim_matches(|c| c == '[' || c == ']').split("', '").collect();
            parcalar.sort();
            format!("{on}; eksik: {parcalar:?}")
        }
        _ => msg.to_string(),
    }
}

fn norm(mut v: Value) -> Value {
    if let Some(w) = v.get_mut("warns").and_then(Value::as_array_mut) {
        w.sort_by_key(|x| x.to_string());
    }
    if let Some(g) = v.get_mut("gates").and_then(Value::as_array_mut) {
        for k in g {
            if k["id"] == "R-referans-varligi" {
                let m = mesaj_norm(k["msg"].as_str().unwrap_or(""));
                k["msg"] = Value::String(m);
            }
        }
    }
    v
}

fn json_al(c: &std::process::Output, kim: &str, skill: &str) -> Value {
    let s = String::from_utf8(c.stdout.clone()).unwrap_or_else(|_| panic!("{kim} {skill}: UTF-8 değil"));
    serde_json::from_str(&s).unwrap_or_else(|e| panic!("{kim} {skill}: JSON ayrıştırılamadı ({e}):\n{s}"))
}

#[test]
fn python_ve_rust_her_skill_icin_ayni_hukmu_verir() {
    let Some(py) = python() else {
        eprintln!("atlandı: Python 3 yok");
        return;
    };
    let betik = kok().join(".claude/skills/skill-kapisi/scripts/kapi-denetim.py");
    let skills = kok().join(".claude/skills");
    if !betik.is_file() || !skills.is_dir() {
        eprintln!("atlandı: betik ya da skill dizini yok ({})", betik.display());
        return;
    }
    let mut dizinler: Vec<PathBuf> =
        std::fs::read_dir(&skills).unwrap().flatten().map(|e| e.path()).filter(|p| p.join("SKILL.md").is_file()).collect();
    dizinler.sort();
    assert!(!dizinler.is_empty(), "hiç skill bulunamadı");
    let ikili = env!("CARGO_BIN_EXE_skill-kapi");
    let mut sayac = 0;
    for d in &dizinler {
        let ad = d.file_name().unwrap().to_string_lossy().to_string();
        let p = Command::new(py)
            .arg(&betik)
            .arg(d)
            .arg("--json")
            .env("PYTHONUTF8", "1")
            .env("PYTHONIOENCODING", "utf-8")
            .output()
            .expect("python koşmadı");
        let r = Command::new(ikili).arg("denetle").arg(d).arg("--json").output().expect("rust koşmadı");
        assert_eq!(p.status.code(), r.status.code(), "{ad}: çıkış kodu ayrıştı");
        let (pj, rj) = (norm(json_al(&p, "python", &ad)), norm(json_al(&r, "rust", &ad)));
        assert_eq!(pj, rj, "{ad}: JSON ayrıştı");
        sayac += 1;
    }
    eprintln!("{sayac}/{} skill birebir aynı", dizinler.len());
}

#[test]
fn metin_ciktisi_ve_hata_kodlari_python_ile_ayni() {
    let Some(py) = python() else {
        eprintln!("atlandı: Python 3 yok");
        return;
    };
    let betik = kok().join(".claude/skills/skill-kapisi/scripts/kapi-denetim.py");
    if !betik.is_file() {
        return;
    }
    let ikili = env!("CARGO_BIN_EXE_skill-kapi");
    let d = kok().join(".claude/skills/skill-kapisi");
    let calistir_py = |a: &[&std::ffi::OsStr]| {
        Command::new(py).arg(&betik).args(a).env("PYTHONUTF8", "1").env("PYTHONIOENCODING", "utf-8").output().unwrap()
    };
    let calistir_rs = |a: &[&std::ffi::OsStr]| Command::new(ikili).arg("denetle").args(a).output().unwrap();
    let dizin = d.as_os_str();
    for a in [vec![dizin], vec![], vec![std::ffi::OsStr::new("yok-boyle-dizin")]] {
        let (p, r) = (calistir_py(&a), calistir_rs(&a));
        assert_eq!(p.status.code(), r.status.code(), "çıkış kodu {a:?}");
        // Windows'ta Python metin kipi \n → \r\n yazar; karşılaştırma satır sonundan bağımsız
        let norm_s = |b: &[u8]| String::from_utf8_lossy(b).replace("\r\n", "\n");
        let (ps, rs) = (norm_s(&p.stdout), norm_s(&r.stdout));
        if a.first().is_some_and(|x| *x == dizin) {
            // metin kipinde yalnız uyarı sırası serbest; satırları sırasız karşılaştır
            let (mut pl, mut rl): (Vec<&str>, Vec<&str>) = (ps.lines().collect(), rs.lines().collect());
            pl.sort();
            rl.sort();
            assert_eq!(pl, rl, "metin çıktısı");
        } else {
            assert_eq!(ps, rs, "stdout {a:?}");
        }
    }
}
