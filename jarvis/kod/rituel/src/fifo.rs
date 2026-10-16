//! `tools/sicak-katman-fifo.py` karşılığı: sıcak-katman FIFO sayacı (İB-80; Karar 104 M1: bayt/satır birincil, madde sigorta).
//! Sıcak dosyaların bayt/satır boyutunu ölçer, tavanı aşan için FLAG basar, arşive inecek en eski maddeleri listeler; TAŞIMAZ.
//! Çıkış kodu: 0 aşım yok · 3 en az bir FLAG (bilgi; engel değil).
use crate::argparse::{Ayrisan, Secenek};
use crate::{harness_anahtar, py};
use regex::Regex;
use serde_json::{Value, json};
use std::path::Path;
use unicode_normalization::UnicodeNormalization;

const BELGE: &str = include_str!("belge/sicak.txt");

/// (ad, bayt tavanı B, satır tavanı S, madde sigortası K)
const TAVAN: [(&str, usize, Option<usize>, Option<usize>); 4] =
    [("kapsul", 8 * 1024, Some(40), Some(8)), ("pano", 12 * 1024, None, Some(5)), ("memory", 4 * 1024, None, Some(16)), ("claude", 7 * 1024, Some(80), None)];

fn arsiv_sablonu(ad: &str) -> &'static str {
    match ad {
        "kapsul" => "arsiv/kapsul-{t}.md",
        "pano" => "arsiv/kuyruk-arsiv/pano-arsivi-{t}.md",
        "memory" => "arsiv/memory-arsivi-{t}.md",
        _ => "",
    }
}

fn ayrisan() -> Ayrisan {
    Ayrisan::yeni(
        "sicak-katman-fifo.py",
        Some(BELGE),
        vec![
            Secenek::bayrak(&["--json"], "json", Some("makine çıktısı")),
            Secenek::deger(&["--repo"], "repo", None),
            Secenek::deger(&["--tarih"], "tarih", Some("arşiv dosya adı tarihi (deterministik koşum için sabitle)")),
        ],
    )
}

/// `## <başlık>\n` bölümünün gövdesi (sonraki `^## ` ya da dosya sonuna dek) satırlarına bölünmüş.
fn bolum(t: &str, baslik: &str) -> Vec<String> {
    let aranan = format!("{baslik}\n");
    let mut pos = 0;
    let bas = loop {
        if t[pos..].starts_with(&aranan) {
            break pos + aranan.len();
        }
        match t[pos..].find('\n') {
            Some(i) => pos += i + 1,
            None => return vec![],
        }
    };
    let mut p = bas;
    let son = loop {
        if t[p..].starts_with("## ") {
            break p;
        }
        match t[p..].find('\n') {
            Some(i) => p += i + 1,
            None => break t.len(),
        }
    };
    py::splitlines(&t[bas..son])
}

fn maddeler(ad: &str, t: &str) -> Vec<String> {
    match ad {
        "kapsul" => bolum(t, "## Şu an").into_iter().filter(|l| l.starts_with("- ")).collect(),
        "pano" => bolum(t, "## AKTİF").into_iter().filter(|l| l.starts_with("| K-")).collect(),
        // kullanıcı-olgusu satırları (user-*.md) FIFO'dan MUAF: gündem değil, kimlik bilgisi (Karar 92 M1 uygulaması 09-10)
        "memory" => py::splitlines(t).into_iter().filter(|l| l.starts_with("- [") && !l.contains("](user-")).collect(),
        _ => py::splitlines(t),
    }
}

/// Bildirim satırı için maddenin tanınır başı: kalın başlık varsa o, yoksa ilk 60 karakter.
fn madde_basi(m: &str) -> String {
    let re = Regex::new(r"\*\*(.{3,80}?)\*\*").unwrap();
    let ham = match re.captures(m) {
        Some(k) => py::strip(&k[1]).to_string(),
        None => py::ilk(py::strip(py::lstrip_kume(m, "-| ")), 60),
    };
    py::rstrip_kume(&ham, " :").to_string()
}

fn memory_yolu() -> String {
    let anahtarlar = [harness_anahtar::kok_anahtar(), harness_anahtar::jarvis_anahtar()];
    for a in &anahtarlar {
        let y = py::expanduser(&format!("~/.claude/projects/{a}/memory/MEMORY.md"));
        if Path::new(&y).exists() {
            return y;
        }
    }
    py::expanduser(&format!("~/.claude/projects/{}/memory/MEMORY.md", anahtarlar[0]))
}

pub fn kos(argv: &[String]) -> i32 {
    let a = match ayrisan().ayristir(argv) {
        Ok(a) => a,
        Err(k) => return k,
    };
    let repo = a.metin("repo").map(String::from).unwrap_or_else(harness_anahtar::jarvis);
    let tarih = a.metin("tarih").map(String::from).unwrap_or_else(jarvis_hook::ortak::bugun_yerel);
    let yollar = [
        ("kapsul", py::join(&py::join(&repo, "core"), "durum-kapsulu.md")),
        ("pano", py::join(&py::join(&repo, "core"), "pano.md")),
        ("memory", memory_yolu()),
        ("claude", py::join(&repo, "AGENTS.md")),
    ];
    let mut sonuc: Vec<Value> = vec![];
    let mut flag = false;
    for (ad, yol) in &yollar {
        if !Path::new(yol).exists() {
            sonuc.push(json!({"ad": ad, "yol": yol, "durum": "YOK"}));
            continue;
        }
        let ham = match py::oku_kati(Path::new(yol)) {
            Ok(h) => h,
            Err(py::OkuHata::Io(e)) => return py::coker(&format!("{yol}: {e}")),
            Err(py::OkuHata::Kod) => return py::coker(&format!("{yol}: UnicodeDecodeError")),
        };
        // macOS dosyaları NFD gelebilir ("Şu an" başlığı eşleşmez); bayt ham metinden
        let t: String = ham.nfc().collect();
        let md = maddeler(ad, &t);
        let (n, b, s) = (md.len(), ham.len(), py::splitlines(&ham).len());
        let (_, tb, ts, tk) = *TAVAN.iter().find(|x| x.0 == *ad).unwrap();
        let mut tetik: Vec<&str> = vec![];
        if b > tb {
            tetik.push("bayt");
        }
        if ts.is_some_and(|ts| s > ts) {
            tetik.push("satır");
        }
        if tk.is_some_and(|tk| n > tk) {
            tetik.push("madde-sigorta");
        }
        let durum = if tetik.is_empty() { "OK" } else { "FLAG" };
        flag |= !tetik.is_empty();
        // FIFO yönü: kapsül/pano yeni maddeyi ÜSTE yazar → en eski = SON; MEMORY.md indeksi sona EKLER → en eski = BAŞ
        let mut arsive: Vec<&String> = vec![];
        if !tetik.is_empty() && *ad != "claude" {
            let sira: Vec<&String> = if *ad == "memory" { md.iter().collect() } else { md.iter().rev().collect() };
            let (mut kalan_b, mut kalan_n) = (b as i64, n as i64);
            for m in sira {
                if kalan_b <= tb as i64 && tk.is_none_or(|k| kalan_n <= k as i64) {
                    break;
                }
                arsive.push(m);
                kalan_b -= m.len() as i64 + 1;
                kalan_n -= 1;
            }
        }
        let arsiv_yolu = arsiv_sablonu(ad).replace("{t}", &tarih);
        let bildirim: Vec<String> = arsive.iter().map(|m| format!("kesildi: {} → {arsiv_yolu}", madde_basi(m))).collect();
        let goreli = if yol.starts_with(&repo) {
            match py::relpath(yol, &repo) {
                Ok(r) => r,
                Err(e) => return py::coker(&format!("relpath: {e}")),
            }
        } else {
            yol.clone()
        };
        sonuc.push(json!({
            "ad": ad, "yol": goreli, "bayt": b, "B": tb, "satir": s, "S": ts, "madde": n, "K": tk, "durum": durum, "tetik": tetik.join("+"),
            "arsive_inecek": arsive.iter().map(|m| py::ilk(m, 90)).collect::<Vec<_>>(), "bildirim": bildirim, "arsiv": arsiv_yolu,
        }));
    }
    let kod = if flag { 3 } else { 0 };
    if a.bayrak("json") {
        py::print(&py::json_girintili(&Value::Array(sonuc)));
        return kod;
    }
    py::print("SICAK-KATMAN FIFO (İB-80 · Karar 104 M1: bayt/satır birincil, madde sigorta):");
    for x in &sonuc {
        let ad = x["ad"].as_str().unwrap_or("");
        if x["durum"] == "YOK" {
            py::print(&format!("  [YOK ] {ad} {}", x["yol"].as_str().unwrap_or("")));
            continue;
        }
        let satir = if x["S"].is_null() { String::new() } else { format!(" · satır {}/{}", x["satir"], x["S"]) };
        let madde = if x["K"].is_null() { String::new() } else { format!(" · madde {}/{}", x["madde"], x["K"]) };
        let tetik = x["tetik"].as_str().unwrap_or("");
        py::print(&format!(
            "  [{}] {} bayt {}/{}{satir}{madde} {}",
            py::sola_hizala(x["durum"].as_str().unwrap_or(""), 4),
            py::sola_hizala(ad, 7),
            x["bayt"],
            x["B"],
            if tetik.is_empty() { String::new() } else { format!("← {tetik}") }
        ));
        for m in x["arsive_inecek"].as_array().into_iter().flatten() {
            py::print(&format!("          ↓ arşive: {}", m.as_str().unwrap_or("")));
        }
        for bl in x["bildirim"].as_array().into_iter().flatten() {
            py::print(&format!("          ✎ kapsüle: {}", bl.as_str().unwrap_or("")));
        }
    }
    kod
}
