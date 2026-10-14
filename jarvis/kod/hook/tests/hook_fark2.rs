//! Fark testleri (2): session-start (git + sqlite kumları) ve kök dispatcher.
mod ortak;
use ortak::*;
use rusqlite::Connection;
use serde_json::json;
use std::path::Path;
use std::process::Command;

fn git(d: &Path, args: &[&str]) -> String {
    let o = Command::new("git")
        .args(args)
        .current_dir(d)
        .env("GIT_AUTHOR_DATE", "2026-10-14T10:00:00+03:00")
        .env("GIT_COMMITTER_DATE", "2026-10-14T10:00:00+03:00")
        .env("GIT_AUTHOR_NAME", "t")
        .env("GIT_AUTHOR_EMAIL", "t@t")
        .env("GIT_COMMITTER_NAME", "t")
        .env("GIT_COMMITTER_EMAIL", "t@t")
        .output()
        .unwrap();
    String::from_utf8_lossy(&o.stdout).trim().to_string()
}

/// Kum içinde deterministik git deposu (iki kumda aynı HEAD sha) kurar; dönen: tam sha.
fn git_kur(k: &Kum) -> String {
    git(&k.jarvis, &["init", "-q", "-b", "main"]);
    std::fs::write(k.jarvis.join("a.txt"), "a").unwrap();
    git(&k.jarvis, &["add", "a.txt"]);
    git(&k.jarvis, &["commit", "-q", "-m", "ilk"]);
    git(&k.jarvis, &["rev-parse", "HEAD"])
}

#[derive(Clone, Copy)]
enum Db {
    Yok,
    Bos,
    Taze,
    Bayat,
    UretimBos,
    GorunumYok,
    Tam,
}

fn db_kur(k: &Kum, sha: &str, tur: Db) {
    let yol = k.jarvis.join("veri").join("baglam.sqlite");
    let _ = std::fs::remove_file(&yol);
    if matches!(tur, Db::Yok) {
        return;
    }
    let c = Connection::open(&yol).unwrap();
    if matches!(tur, Db::Bos) {
        return;
    }
    c.execute_batch("CREATE TABLE uretim(git_head_sha TEXT, uretim_zamani TEXT);").unwrap();
    match tur {
        Db::Taze | Db::GorunumYok | Db::Tam => {
            c.execute("INSERT INTO uretim VALUES (?1, '2026-10-14T09:00:00+03:00')", [sha]).unwrap();
        }
        Db::Bayat => {
            c.execute("INSERT INTO uretim VALUES ('deadbeefdeadbeef', '2026-09-01T09:00:00+03:00')", []).unwrap();
            c.execute("INSERT INTO uretim VALUES ('0123456789abcdef', '2026-08-01T09:00:00+03:00')", []).unwrap();
        }
        _ => {}
    }
    if matches!(tur, Db::Taze | Db::Bayat | Db::Tam) {
        c.execute_batch(
            "CREATE TABLE v_amb_acilis_brifi(acik_salih_karari, acik_icra_borcu, son_teslim, son_kosum);
             INSERT INTO v_amb_acilis_brifi VALUES (3, 7, 'çok uzun bir son teslim adı çok uzun bir son teslim adı çok uzun bir son teslim adı', 'koşum');
             CREATE TABLE silver_saglik_son(test_id, sonuc); INSERT INTO silver_saglik_son VALUES ('T-C3-sicak', 'OK');
             CREATE TABLE silver_kuyruk(x); INSERT INTO silver_kuyruk VALUES (1),(2),(3);",
        )
        .unwrap();
    }
    if matches!(tur, Db::Tam) {
        // alt kılavuz: NULL ve boş değerler
        c.execute_batch("DELETE FROM v_amb_acilis_brifi; INSERT INTO v_amb_acilis_brifi VALUES (NULL, 2.5, '', NULL);").unwrap();
    }
}

fn session_varyant(ad: &str, tur: Db, duzen: impl Fn(&Kum) + 'static) {
    let hazirla = move |k: &Kum| {
        let sha = git_kur(k);
        db_kur(k, &sha, tur);
        duzen(k);
    };
    fark(H::Session, ad, &hazirla, vec![adim(""), adim("").env("CLAUDE_CODE_ENTRYPOINT", "cli")]);
}

#[test]
fn session_start() {
    session_varyant("s-taze", Db::Taze, |_| {});
    session_varyant("s-bayat", Db::Bayat, |_| {});
    session_varyant("s-dbyok", Db::Yok, |_| {});
    session_varyant("s-dbbos", Db::Bos, |_| {});
    session_varyant("s-uretimbos", Db::UretimBos, |_| {});
    session_varyant("s-gorunumyok", Db::GorunumYok, |_| {});
    session_varyant("s-null", Db::Tam, |_| {});
    session_varyant("s-kesimyok", Db::Taze, |k| {
        std::fs::remove_file(k.jarvis.join("veri").join("model-kesim.jsonl")).unwrap();
    });
    session_varyant("s-kesim-bos-satir", Db::Taze, |k| {
        let y = k.jarvis.join("veri").join("model-kesim.jsonl");
        let t = std::fs::read_to_string(&y).unwrap();
        std::fs::write(&y, format!("{t}\n\n")).unwrap();
    });
    session_varyant("s-kesim-yinelenen", Db::Taze, |k| {
        std::fs::write(
            k.jarvis.join("veri").join("model-kesim.jsonl"),
            "{\"model_ad\": \"Claude A\", \"kesim_turu\": \"reliable\", \"kesim_tarihi\": \"2026-01\"}\n{\"model_ad\": \"Claude B\", \"kesim_turu\": \"x\", \"kesim_tarihi\": \"2026-02\"}\n{\"model_ad\": \"Claude C\", \"kesim_turu\": \"reliable\", \"kesim_tarihi\": 5}\n{\"model_ad\": \"Claude A\", \"kesim_turu\": \"reliable\", \"kesim_tarihi\": \"2026-03\"}\n",
        )
        .unwrap();
    });
    session_varyant("s-kesim-anahtar-eksik", Db::Taze, |k| {
        std::fs::write(k.jarvis.join("veri").join("model-kesim.jsonl"), "{\"model_ad\": \"Claude A\"}\n").unwrap();
    });
    session_varyant("s-kapsul-yok", Db::Taze, |k| {
        std::fs::remove_file(k.jarvis.join("core").join("durum-kapsulu.md")).unwrap();
    });
    session_varyant("s-kapsul-farkli", Db::Taze, |k| {
        std::fs::write(
            k.jarvis.join("core").join("durum-kapsulu.md"),
            format!("# K\n**Güncelleme:**   \n\n  uzun {}\n\n## Sonraki ilk iş\n\n\n  **kalın** `kod` {}\nikinci\n", "ç".repeat(120), "x".repeat(300)),
        )
        .unwrap();
    });
    session_varyant("s-kapsul-basliksiz-sonsuz", Db::Taze, |k| {
        std::fs::write(k.jarvis.join("core").join("durum-kapsulu.md"), "## Sonraki ilk iş   metin satırı").unwrap();
    });
    session_varyant("s-kirli-agac", Db::Taze, |k| {
        std::fs::write(k.jarvis.join("yeni.txt"), "x").unwrap();
    });
}

#[test]
fn session_start_gercek_depo() {
    // Gerçek depo ve gerçek (394 MB) silver: salt-okur çalıştırma, yazma yok.
    let gj = gercek_kok().join("jarvis");
    let calistir = |c: &mut Command| -> String {
        let o = c.current_dir(&gj).env("CLAUDE_PROJECT_DIR", &gj).env("PYTHONUTF8", "1").output().unwrap();
        String::from_utf8_lossy(&o.stdout).replace('\r', "")
    };
    let mut yeni = Command::new(env!("CARGO_BIN_EXE_jarvis-hook"));
    yeni.arg("session-start");
    let mut eski = Command::new("bash");
    eski.arg(ileri(&gj.join(".claude/hooks/session-start.sh")));
    let (y, e) = (calistir(&mut yeni), calistir(&mut eski));
    assert!(!y.is_empty() && y.len() <= 2000, "yeni boş ya da 2000 bayt üstü");
    assert!(y.starts_with(&e) || y == e, "gerçek depo session-start farkı:\n eski:{e}\n yeni:{y}");
    SAYAC.fetch_add(1, std::sync::atomic::Ordering::SeqCst);
}

// ------------------------------------------------------------------ dispatcher
#[test]
fn dispatcher() {
    let hazirla = |k: &Kum| {
        std::fs::create_dir_all(k.kok.join("bin")).unwrap();
        std::fs::copy(gercek_kok().join("bin").join("hook-dispatch.sh"), k.kok.join("bin").join("hook-dispatch.sh")).unwrap();
        let ayar = |hooks: serde_json::Value| json!({ "hooks": hooks });
        std::fs::write(
            k.jarvis.join(".claude").join("settings.json"),
            ayar(json!({
                "PreToolUse": [
                    {"matcher": "Bash", "hooks": [{"type": "command", "command": "echo bash-hook; echo $SISTEM_AJAN $CLAUDE_PROJECT_DIR | sed 's|[A-Za-z]:.*[/\\\\]||' "}]},
                    {"matcher": "Agent|Task", "hooks": [{"type": "command", "command": "echo agent >&2; exit 2"}]},
                    {"matcher": "Read.*", "hooks": [{"type": "command", "command": "cat"}, {"type": "command", "command": "echo ikinci"}]},
                    {"hooks": [{"type": "command", "command": "echo eslesmesiz-matcher"}, {"type": "other", "command": "echo asla"}]}
                ],
                "Stop": [{"hooks": [{"type": "command", "command": "echo e1 >&2; exit 3"}, {"type": "command", "command": "echo e2; exit 4"}]}],
                "UserPromptSubmit": [{"hooks": [{"type": "command", "command": "exit 2"}, {"type": "command", "command": "echo hic"}]}],
                "SessionStart": [{"hooks": [{"type": "command", "command": "echo \"merhaba çğş\""}]}]
            }))
            .to_string(),
        )
        .unwrap();
        std::fs::create_dir_all(k.kok.join("friday").join(".claude")).unwrap();
        std::fs::write(k.kok.join("friday").join(".claude").join("settings.json"), "{bozuk").unwrap();
        std::fs::create_dir_all(k.kok.join("tart")).unwrap();
        std::fs::create_dir_all(k.kok.join("calc").join(".claude")).unwrap();
        std::fs::write(k.kok.join("calc").join(".claude").join("settings.json"), ayar(json!({"Stop": [{"hooks": [{"type": "command", "command": "echo calc-stop"}]}]})).to_string()).unwrap();
    };
    let g = |cwd: &str, tool: &str| json!({"cwd": cwd, "tool_name": tool, "session_id": "d"}).to_string();
    let koke = |a: Adim| a.env("CLAUDE_PROJECT_DIR", "{K}");
    let mut adimlar = vec![];
    for (olay, cwd, tool) in [
        ("PreToolUse", "{R}", "Bash"), ("PreToolUse", "{R}", "Agent"), ("PreToolUse", "{R}", "Task"), ("PreToolUse", "{R}", "Read"), ("PreToolUse", "{R}", "ReadFile"),
        ("PreToolUse", "{R}", "Edit"), ("PreToolUse", "{R}", ""), ("PreToolUse", "{R}/core", "Bash"), ("Stop", "{R}", ""), ("UserPromptSubmit", "{R}", ""),
        ("SessionStart", "{R}", ""), ("SessionStart", "{K}/friday", ""), ("SessionStart", "{K}/tart", ""), ("SessionStart", "{K}/yok-ajan", ""), ("Stop", "{K}/calc", ""),
        ("Stop", "{K}", ""), ("Stop", "/c/baska/yer", ""), ("YokOlay", "{R}", ""), ("Stop", "{K}/jarvis/.claude/hooks", ""),
    ] {
        adimlar.push(koke(adim(&g(cwd, tool)).arg(olay)));
    }
    // çift-koşum freni: CLAUDE_PROJECT_DIR = ajan dizini -> susar
    adimlar.push(adim(&g("{R}", "Bash")).arg("PreToolUse").env("CLAUDE_PROJECT_DIR", "{R}"));
    adimlar.push(koke(adim("{bozuk json").arg("SessionStart")));
    adimlar.push(koke(adim("").arg("SessionStart")));
    adimlar.push(koke(adim(&json!({"tool_name": "Bash"}).to_string()).arg("PreToolUse")));
    adimlar.push(koke(adim(&format!("{}\n\n", g("{R}", "Read"))).arg("PreToolUse")));
    fark(H::Dispatch, "dispatch", &hazirla, adimlar);
}

#[test]
fn zz_vaka_sayisi() {
    eprintln!("FARK vaka sayacı (bu süreçte): {} {:?}", SAYAC.load(std::sync::atomic::Ordering::SeqCst), HOOK_SAYAC.lock().unwrap());
}
