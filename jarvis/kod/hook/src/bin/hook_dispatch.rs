//! `hook-dispatch [--kok <dizin>] <olay>`: kök dispatcher (bin/hook-dispatch.sh karşılığı). Kök: `--kok` > `SISTEM_KOK` >
//! `CLAUDE_PROJECT_DIR` > cwd. Neden ayrı ikili: yalnız dispatcher çalıştırılır, tek amaçlı ve `jarvis-hook` alt komutlarından bağımsız
//! kalır (harness/backend değişince yalnız bu dosya değişir, Karar 101 EK); crate ve yardımcılar ortak.
use jarvis_hook::{Ortam, dispatch};
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
    let mut stdin = Vec::new();
    let _ = std::io::stdin().read_to_end(&mut stdin);
    let o = Ortam { stdin, repo: kok, env: std::env::vars().collect() };
    let s = dispatch::kos(&olay, &o);
    let _ = std::io::stdout().write_all(&s.cikti);
    let _ = std::io::stderr().write_all(s.hata.as_bytes());
    ExitCode::from(s.kod as u8)
}
