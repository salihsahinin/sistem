//! `hook-dispatch [--kok <dizin>] <olay>`: kök dispatcher (bin/hook-dispatch.sh karşılığı). Kök: `--kok` > `SISTEM_KOK` >
//! `CLAUDE_PROJECT_DIR` > cwd. Neden ayrı ikili: yalnız dispatcher çalıştırılır, tek amaçlı ve `jarvis-hook` alt komutlarından bağımsız
//! kalır (harness/backend değişince yalnız bu dosya değişir, Karar 101 EK); crate ve yardımcılar ortak.
use jarvis_hook::ortak::ev_dizini;
use jarvis_hook::{Ortam, dispatch, izin};
use std::io::{Read, Write};
use std::path::PathBuf;
use std::process::ExitCode;

fn main() -> ExitCode {
    let mut argv: Vec<String> = std::env::args().skip(1).collect();
    let mut kok: Option<String> = None;
    if argv.first().map(String::as_str) == Some("--kok") && argv.len() >= 2 {
        kok = Some(argv[1].clone());
        argv.drain(0..2);
    }
    let Some(olay) = argv.first().cloned() else {
        eprintln!("olay adı gerekli");
        return ExitCode::from(1);
    };
    let kok = kok
        .or_else(|| std::env::var("SISTEM_KOK").ok().filter(|x| !x.is_empty()))
        .or_else(|| std::env::var("CLAUDE_PROJECT_DIR").ok().filter(|x| !x.is_empty()))
        .map(PathBuf::from)
        .unwrap_or_else(|| std::env::current_dir().unwrap_or_default());
    if olay == "deny-denetle" {
        return deny_denetle(&argv[1..], &kok);
    }
    let mut stdin = Vec::new();
    let _ = std::io::stdin().read_to_end(&mut stdin);
    let o = Ortam { stdin, repo: kok, env: std::env::vars().collect() };
    let s = dispatch::kos(&olay, &o);
    let _ = std::io::stdout().write_all(&s.cikti);
    let _ = std::io::stderr().write_all(s.hata.as_bytes());
    ExitCode::from(s.kod as u8)
}

/// A3 kuru koşum: `hook-dispatch deny-denetle <ajan> <girdi.json | satır içi JSON | ->`. Anahtardan bağımsız koşar,
/// hiçbir hook başlatmaz; yalnız `<ajan>` kurallarını eşler. Girdide cwd yoksa ajan dizini. Çıkış: 2 deny, 0 ask/geç.
fn deny_denetle(args: &[String], kok: &std::path::Path) -> ExitCode {
    let (Some(ajan), Some(kaynak)) = (args.first(), args.get(1)) else {
        eprintln!("kullanım: hook-dispatch deny-denetle <ajan> <girdi.json | '{{...}}' | ->");
        return ExitCode::from(64);
    };
    let metin = if kaynak == "-" {
        let mut b = String::new();
        let _ = std::io::stdin().read_to_string(&mut b);
        b
    } else if kaynak.trim_start().starts_with('{') {
        kaynak.clone()
    } else {
        std::fs::read_to_string(kaynak).unwrap_or_default()
    };
    let Ok(g) = serde_json::from_str::<serde_json::Value>(&metin) else {
        eprintln!("girdi JSON okunamadı: {kaynak}");
        return ExitCode::from(64);
    };
    let ajan_dir = kok.join(ajan);
    if !ajan_dir.join(".claude").join("settings.json").is_file() {
        eprintln!("ajan ayarı yok: {}", ajan_dir.join(".claude").join("settings.json").display());
        return ExitCode::from(64);
    }
    let cwd = g.get("cwd").and_then(serde_json::Value::as_str).map(PathBuf::from).unwrap_or_else(|| ajan_dir.clone());
    let k = izin::denetle(std::slice::from_ref(ajan), &g, &cwd, kok, &ev_dizini());
    for u in &k.uyarilar {
        eprintln!("uyarı: {u}");
    }
    let arac = g.get("tool_name").and_then(serde_json::Value::as_str).unwrap_or("");
    match k.eslesme {
        Some(e) => {
            let karar = if e.tur == izin::Tur::Deny { "deny" } else { "ask" };
            println!("ajan={ajan}\tarac={arac}\tkarar={karar}\tkural={}", e.kural);
            ExitCode::from(if e.tur == izin::Tur::Deny { 2 } else { 0 })
        }
        None => {
            println!("ajan={ajan}\tarac={arac}\tkarar=gec\tkural=-");
            ExitCode::from(0)
        }
    }
}
