//! `jarvis-hook <olay> [bayraklar]`: stdin JSON -> stdout (bağlama eklenir) / stderr (engel gerekçesi) / çıkış kodu (2 = engel).
//! Depo kökü: `--repo` > `CLAUDE_PROJECT_DIR` > cwd. Alt komutlar: pretool-core-tel · pretool-ajan-fren · pretool-altajan-okuma ·
//! stop-buyuk-harf · instructions-loaded · userprompt · session-start · sabit-guncellik · paket-yonlendir · prompt-dosya.
use jarvis_hook::{Ortam, Sonuc, ajan_fren, altajan_okuma, buyuk_harf, core_tel, paket, prompt_dosya, sabit, session_start, talimat};
use std::io::{Read, Write};
use std::path::PathBuf;
use std::process::ExitCode;

fn main() -> ExitCode {
    let argv: Vec<String> = std::env::args().skip(1).collect();
    let Some(olay) = argv.first().cloned() else {
        eprintln!("kullanım: jarvis-hook <olay> [bayraklar]");
        return ExitCode::from(64);
    };
    let bayraklar: Vec<String> = argv[1..].to_vec();
    let mut repo: Option<String> = None;
    let mut i = 0;
    while i < bayraklar.len() {
        if bayraklar[i] == "--repo" {
            repo = bayraklar.get(i + 1).cloned();
        } else if let Some(v) = bayraklar[i].strip_prefix("--repo=") {
            repo = Some(v.to_string());
        }
        i += 1;
    }
    let repo = repo
        .or_else(|| std::env::var("CLAUDE_PROJECT_DIR").ok().filter(|x| !x.is_empty()))
        .map(PathBuf::from)
        .unwrap_or_else(|| std::env::current_dir().unwrap_or_default());
    let mut stdin = Vec::new();
    if olay != "paket-yonlendir" || !bayraklar.iter().any(|b| b == "--sec" || b == "--denetle") {
        let _ = std::io::stdin().read_to_end(&mut stdin);
    }
    let o = Ortam { stdin, repo, env: std::env::vars().collect() };
    let s: Sonuc = match olay.as_str() {
        "pretool-core-tel" => core_tel::kos(&o),
        "pretool-ajan-fren" => ajan_fren::kos(&o),
        "pretool-altajan-okuma" => altajan_okuma::kos(&o),
        "stop-buyuk-harf" => buyuk_harf::kos(&o),
        "instructions-loaded" => talimat::kos(&o),
        "session-start" => session_start::kos(&o),
        "sabit-guncellik" => sabit::kos(&o),
        "prompt-dosya" => {
            let mut b = prompt_dosya::Bayrak::default();
            let mut j = 0;
            while j < bayraklar.len() {
                match bayraklar[j].as_str() {
                    "--tablo" => {
                        j += 1;
                        b.tablo = bayraklar.get(j).cloned();
                    }
                    "--kuru" => b.kuru = true,
                    "--json" => b.json = true,
                    "--repo" => j += 1,
                    _ => {}
                }
                j += 1;
            }
            prompt_dosya::kos(&o, &b)
        }
        "paket-yonlendir" => match paket::bayrak_oku(&bayraklar) {
            Ok(b) => paket::kos(&o, &b),
            Err(e) => Sonuc { cikti: vec![], hata: format!("HATA: {e}\n"), kod: 2 },
        },
        "userprompt" => {
            // userprompt-dosya.sh: aynı stdin iki araca; hata sessiz, çıkış hep 0
            let mut s = prompt_dosya::kos(&o, &prompt_dosya::Bayrak::default());
            let p = paket::kos(&o, &paket::Bayrak::default());
            s.cikti.extend_from_slice(&p.cikti);
            s.hata.clear();
            s.kod = 0;
            s
        }
        diger => {
            eprintln!("bilinmeyen olay: {diger}");
            return ExitCode::from(64);
        }
    };
    let _ = std::io::stdout().write_all(&s.cikti);
    let _ = std::io::stdout().flush();
    if !s.hata.is_empty() {
        let _ = std::io::stderr().write_all(s.hata.as_bytes());
    }
    ExitCode::from(s.kod as u8)
}
