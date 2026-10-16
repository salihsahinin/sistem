//! `baglam <genislet|denetle> <kök.md> [--json]`
//!
//! - `genislet`: kök dosyanın bağlamını Claude Code'un otomatik yükleme sırasıyla tek akış olarak basar
//!   (okuma rejiminde `Read` yerine; Karar 117 mekanizma 1a). Bloklar `Contents of <yol>:` başlığıyla.
//! - `denetle`: sıra değişmezini denetler (`@` satırları dosya sonunda · hedef var · uzantı yüklenir ·
//!   ≤4 sıçrama · tekrar uyarısı). Çıkış: 0 temiz · 1 ihlal · 2 hata (dosya okunamadı, kullanım).
use jarvis_baglam::{genislet, Bulgu};
use std::path::Path;

fn kullanim() -> i32 {
    eprintln!("kullanım: baglam <genislet|denetle> <kök.md> [--json]");
    2
}

fn satir(b: &Bulgu) -> (&'static str, String) {
    match b {
        Bulgu::SonrakiMetin { dosya, satir } => {
            ("sonraki-metin", format!("{}:{}: `@` satırından sonra metin var; içe aktarmalar dosya sonunda durmalı", dosya.display(), satir))
        }
        Bulgu::HedefYok { dosya, satir, hedef } => ("hedef-yok", format!("{}:{}: hedef yok: {}", dosya.display(), satir, hedef.display())),
        Bulgu::Uzanti { dosya, satir, hedef } => {
            ("uzanti", format!("{}:{}: harness bu uzantıyı yüklemez: {} (`.lean` için `.lean.md` symlink'i)", dosya.display(), satir, hedef.display()))
        }
        Bulgu::Derin { dosya, satir, hedef } => {
            ("derin", format!("{}:{}: 4 sıçramadan derin, harness düşürür: {}", dosya.display(), satir, hedef.display()))
        }
        Bulgu::Tekrar { dosya, satir, hedef } => {
            ("tekrar", format!("{}:{}: uyarı: ikinci kez içe aktarıldı, yok sayılır: {}", dosya.display(), satir, hedef.display()))
        }
    }
}

fn json_dize(s: &str) -> String {
    let mut o = String::from("\"");
    for c in s.chars() {
        match c {
            '"' => o.push_str("\\\""),
            '\\' => o.push_str("\\\\"),
            '\n' => o.push_str("\\n"),
            c if (c as u32) < 0x20 => o.push_str(&format!("\\u{:04x}", c as u32)),
            c => o.push(c),
        }
    }
    o.push('"');
    o
}

fn main() {
    let argv: Vec<String> = std::env::args().skip(1).collect();
    let json = argv.iter().any(|a| a == "--json");
    let konum: Vec<&String> = argv.iter().filter(|a| !a.starts_with("--")).collect();
    let (komut, kok) = match konum.as_slice() {
        [k, d] => (k.as_str(), Path::new(d.as_str())),
        _ => std::process::exit(kullanim()),
    };
    let (bloklar, bulgular) = match genislet(kok) {
        Ok(s) => s,
        Err(e) => {
            eprintln!("baglam: {}: {e}", kok.display());
            std::process::exit(2);
        }
    };
    let ihlal = bulgular.iter().filter(|b| b.ihlal_mi()).count();
    let cikis = if ihlal > 0 { 1 } else { 0 };
    match komut {
        "genislet" => {
            for b in &bloklar {
                print!("Contents of {}:\n\n{}\n\n", b.yol.display(), b.metin.trim_end());
            }
            for b in &bulgular {
                eprintln!("{}", satir(b).1);
            }
        }
        "denetle" if json => {
            let bul: Vec<String> = bulgular
                .iter()
                .map(|b| {
                    let (tur, m) = satir(b);
                    format!("{{\"tur\":{},\"mesaj\":{}}}", json_dize(tur), json_dize(&m))
                })
                .collect();
            let sira: Vec<String> = bloklar.iter().map(|b| json_dize(&b.yol.display().to_string())).collect();
            println!(
                "{{\"arac\":\"baglam\",\"surum\":\"0.1\",\"cikis\":{cikis},\"sira\":[{}],\"bulgular\":[{}]}}",
                sira.join(","),
                bul.join(",")
            );
        }
        "denetle" => {
            for b in &bloklar {
                println!("{}{}", "  ".repeat(b.derinlik), b.yol.display());
            }
            for b in &bulgular {
                println!("{}", satir(b).1);
            }
            println!("{} blok · {} ihlal · {} uyarı", bloklar.len(), ihlal, bulgular.len() - ihlal);
        }
        _ => std::process::exit(kullanim()),
    }
    std::process::exit(cikis);
}
