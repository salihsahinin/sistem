//! `durum` CLI: ortak durum tablosu (kütük `ortak/durum-olay.jsonl`).
//! Çıkış kodları: 0 başarı · 1 geçersiz geçiş/bulunamadı · 2 kullanım hatası.

use durum::*;
use std::io::Write;
use std::path::PathBuf;

const KULLANIM: &str = "kullanım: durum <ac|al|bitir|tuket|bayatla|listele|oturum-basi> ... [--kutuk <yol>] [--ts <ISO>]\n  \
ac --alan A --is \"..\" --sonraki \"..\" [--kanit a,b] [--girdi 1,2] [--son-gecerlilik YYYY-MM-DD] [--oturum X]\n  \
al <id> · bitir <id> [--kanit ..] [--kalan \"is|sonraki_eylem\"] · tuket <id> · bayatla <id>\n  \
listele [--alan A] [--durum D] [--json] · oturum-basi --alan A";

struct Arg {
    konumsal: Vec<String>,
    bayrak: Vec<(String, Option<String>)>,
}

impl Arg {
    fn coz(args: &[String]) -> Result<Arg, Hata> {
        let (mut konumsal, mut bayrak) = (vec![], vec![]);
        let mut i = 0;
        while i < args.len() {
            if let Some(ad) = args[i].strip_prefix("--") {
                if ad == "json" {
                    bayrak.push((ad.to_string(), None));
                } else {
                    i += 1;
                    let v = args.get(i).ok_or_else(|| Hata::Kullanim(format!("--{ad} değer ister")))?;
                    bayrak.push((ad.to_string(), Some(v.clone())));
                }
            } else {
                konumsal.push(args[i].clone());
            }
            i += 1;
        }
        Ok(Arg { konumsal, bayrak })
    }
    fn al(&self, ad: &str) -> Option<&str> {
        self.bayrak.iter().rev().find(|(a, _)| a == ad).and_then(|(_, v)| v.as_deref())
    }
    fn var(&self, ad: &str) -> bool {
        self.bayrak.iter().any(|(a, _)| a == ad)
    }
    fn liste(&self, ad: &str) -> Vec<String> {
        self.al(ad).map(|v| v.split(',').map(|s| s.trim().to_string()).filter(|s| !s.is_empty()).collect()).unwrap_or_default()
    }
    fn id(&self) -> Result<u64, Hata> {
        self.konumsal.get(1).and_then(|s| s.trim_start_matches('#').parse().ok()).ok_or_else(|| Hata::Kullanim("<id> gerekli".into()))
    }
}

/// Varsayılan kütük: cwd'den yukarı doğru `ortak/` dizinini ara; yoksa cwd altında `ortak/durum-olay.jsonl`.
fn varsayilan_kutuk() -> PathBuf {
    if let Ok(mut d) = std::env::current_dir() {
        let ilk = d.clone();
        loop {
            if d.join("ortak").is_dir() {
                return d.join("ortak").join("durum-olay.jsonl");
            }
            if !d.pop() {
                break;
            }
        }
        return ilk.join("ortak").join("durum-olay.jsonl");
    }
    PathBuf::from("ortak/durum-olay.jsonl")
}

fn yukle(yol: &PathBuf) -> Result<Defter, Hata> {
    match std::fs::read_to_string(yol) {
        Ok(m) => Defter::katla(&olaylari_oku(&m)?),
        Err(e) if e.kind() == std::io::ErrorKind::NotFound => Ok(Defter::default()),
        Err(e) => Err(Hata::Gecersiz(format!("kütük okunamadı: {e}"))),
    }
}

fn ekle(yol: &PathBuf, olaylar: &[Olay]) -> Result<(), Hata> {
    if let Some(p) = yol.parent() {
        std::fs::create_dir_all(p).map_err(|e| Hata::Gecersiz(format!("dizin: {e}")))?;
    }
    let mut metin = String::new();
    for o in olaylar {
        metin.push_str(&olay_satiri(o));
        metin.push('\n');
    }
    let mut f = std::fs::OpenOptions::new().create(true).append(true).open(yol).map_err(|e| Hata::Gecersiz(format!("kütük açılamadı: {e}")))?;
    f.write_all(metin.as_bytes()).map_err(|e| Hata::Gecersiz(format!("kütük yazılamadı: {e}")))
}

fn calistir(args: &[String]) -> Result<String, Hata> {
    let a = Arg::coz(args)?;
    let komut = a.konumsal.first().ok_or_else(|| Hata::Kullanim("komut yok".into()))?.as_str();
    let yol = a.al("kutuk").map(PathBuf::from).unwrap_or_else(varsayilan_kutuk);
    let ts = a.al("ts").map(String::from).unwrap_or_else(simdi_iso);
    // Geçerlilik ve özet tarihi yerel takvim günüdür (Karar 68: tarih sistem saatinden); --ts verilirse onun tarih kısmı (testler).
    let bugun = a.al("ts").map(|t| tarih_kismi(t).to_string()).unwrap_or_else(yerel_tarih);
    let mut defter = yukle(&yol)?;
    let oturum = a.al("oturum").map(String::from);

    let tur = match komut {
        "ac" => Some(OlayTuru::Ac),
        "al" => Some(OlayTuru::Al),
        "bitir" => Some(OlayTuru::Bitir),
        "tuket" => Some(OlayTuru::Tuket),
        "bayatla" => Some(OlayTuru::Bayatla),
        _ => None,
    };
    if let Some(tur) = tur {
        let mut yeni = vec![];
        let mut o = if tur == OlayTuru::Ac {
            let mut o = Olay::yalin(tur, defter.sonraki_id(), &ts);
            let gerekli = |ad: &str| a.al(ad).map(String::from).ok_or_else(|| Hata::Kullanim(format!("--{ad} gerekli")));
            o.alan = Some(gerekli("alan")?);
            o.is_ad = Some(gerekli("is")?);
            o.sonraki_eylem = Some(gerekli("sonraki")?);
            o.girdi = a
                .liste("girdi")
                .iter()
                .map(|s| s.trim_start_matches('#').parse().map_err(|_| Hata::Kullanim(format!("girdi sayı değil: {s}"))))
                .collect::<Result<_, _>>()?;
            o.son_gecerlilik = a.al("son-gecerlilik").map(String::from);
            o
        } else {
            Olay::yalin(tur, a.id()?, &ts)
        };
        o.kanit = a.liste("kanit");
        o.oturum = oturum.clone();
        defter.uygula(&o, &bugun)?;
        let id = o.id;
        let alan = o.alan.clone();
        yeni.push(o);
        let mut cikti = match tur {
            OlayTuru::Ac => format!("#{id} acik {}\n", alan.unwrap_or_default()),
            OlayTuru::Al => format!("#{id} islemde\n"),
            OlayTuru::Bitir => format!("#{id} tamam\n"),
            OlayTuru::Tuket => format!("#{id} tuketildi\n"),
            OlayTuru::Bayatla => format!("#{id} bayat\n"),
        };
        if let (OlayTuru::Bitir, Some(kalan)) = (tur, a.al("kalan")) {
            let (is_ad, sonraki) = kalan.split_once('|').ok_or_else(|| Hata::Kullanim("--kalan \"is|sonraki_eylem\" biçiminde olmalı".into()))?;
            let alan = defter.kayitlar[&id].alan.clone();
            let mut k = Olay::yalin(OlayTuru::Ac, defter.sonraki_id(), &ts);
            k.alan = Some(alan.clone());
            k.is_ad = Some(is_ad.trim().to_string());
            k.sonraki_eylem = Some(sonraki.trim().to_string());
            k.girdi = vec![id];
            k.oturum = oturum;
            defter.uygula(&k, &bugun)?;
            cikti.push_str(&format!("#{} acik {alan}\n", k.id));
            yeni.push(k);
        }
        ekle(&yol, &yeni)?;
        return Ok(cikti);
    }

    match komut {
        "listele" => {
            let durum = match a.al("durum") {
                Some(s) => Some(Durum::coz(s).ok_or_else(|| Hata::Kullanim(format!("bilinmeyen durum: {s}")))?),
                None => None,
            };
            let l = defter.listele(a.al("alan"), durum, &bugun);
            if a.var("json") {
                let v: Vec<serde_json::Value> = l
                    .iter()
                    .map(|(k, e)| {
                        let mut j = serde_json::to_value(k).expect("kayıt serileşir");
                        j["durum"] = serde_json::Value::String(e.ad().to_string());
                        j
                    })
                    .collect();
                Ok(serde_json::to_string(&v).expect("json") + "\n")
            } else {
                Ok(l.iter().map(|(k, e)| format!("#{}\t{}\t{}\t{}\t{}\n", k.id, k.alan, e.ad(), k.is_ad, k.sonraki_eylem)).collect())
            }
        }
        "oturum-basi" => {
            let alan = a.al("alan").ok_or_else(|| Hata::Kullanim("--alan gerekli".into()))?;
            if !ALANLAR.contains(&alan) {
                return Err(Hata::Kullanim(format!("bilinmeyen alan: {alan}")));
            }
            Ok(defter.oturum_basi(alan, &bugun))
        }
        _ => Err(Hata::Kullanim(format!("bilinmeyen komut: {komut}"))),
    }
}

fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();
    match calistir(&args) {
        Ok(c) => print!("{c}"),
        Err(h) => {
            eprintln!("durum: {}", h.mesaj());
            if h.kod() == 2 {
                eprintln!("{KULLANIM}");
            }
            std::process::exit(h.kod());
        }
    }
}
