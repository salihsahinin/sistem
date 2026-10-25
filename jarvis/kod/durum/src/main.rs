//! `durum` CLI: ortak durum tablosu + akış grafı (kütük `ortak/durum-olay.jsonl`).
//! Çıkış kodları: 0 başarı · 1 geçersiz geçiş/bulunamadı · 2 kullanım hatası · 3 dosya/alt süreç hatası.
//!
//! Karar 113 M2 komutları: ac · al · bitir · tuket · bayatla · listele · oturum-basi.
//! Karar 122 komutları: seans-ac · seans-kapat · graf · ozet (akış grafı JSON/D2/SVG + Salih özeti).

use durum::*;
use std::io::Write;
use std::path::{Path, PathBuf};

const KULLANIM: &str = "kullanım: durum <komut> ... [--kutuk <yol>] [--ts <ISO>]\n  \
ac --alan A --is \"..\" --sonraki \"..\" [--kanit a,b] [--girdi 1,2] [--hedef N] [--tur is|hedef] [--son-gecerlilik YYYY-MM-DD] [--oturum X]\n  \
al <id> · bitir <id> [--kanit ..] [--kalan \"is|sonraki_eylem\"] · tuket <id> · bayatla <id>\n  \
listele [--alan A] [--durum D] [--json] · oturum-basi --alan A [--json]\n  \
seans-ac --alan A [--oturum X] [--hedef \"tek cümle\"]        (X yoksa <tarih>-<alan>)\n  \
seans-kapat --alan A --oturum X --girdi <teslim-girdi.json> [--etiket E] [--render]\n  \
graf [--alan A] [--json <yol>] [--d2 <yol>] [--metin] [--render]  (varsayılan: ortak/akis-graf.json + ortak/graf/akis-<alan>.d2)\n  \
ozet [--cikti ortak/SALIH-OZET.md]";

struct Arg {
    konumsal: Vec<String>,
    bayrak: Vec<(String, Option<String>)>,
}

const BAYRAKSIZ: [&str; 3] = ["json", "metin", "render"];

impl Arg {
    fn coz(args: &[String]) -> Result<Arg, Hata> {
        let (mut konumsal, mut bayrak) = (vec![], vec![]);
        let mut i = 0;
        while i < args.len() {
            if let Some(ad) = args[i].strip_prefix("--") {
                if BAYRAKSIZ.contains(&ad) {
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
    fn alan(&self) -> Result<&str, Hata> {
        let a = self.al("alan").ok_or_else(|| Hata::Kullanim("--alan gerekli".into()))?;
        if !ALANLAR.contains(&a) {
            return Err(Hata::Kullanim(format!("bilinmeyen alan: {a}")));
        }
        Ok(a)
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

/// Repo kökü = kütüğün bulunduğu `ortak/` dizininin ebeveyni.
fn kok(kutuk: &Path) -> PathBuf {
    kutuk.parent().and_then(|p| p.parent()).map(Path::to_path_buf).unwrap_or_else(|| PathBuf::from("."))
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

fn dosya_yaz(yol: &Path, icerik: &str) -> Result<(), Hata> {
    if let Some(p) = yol.parent() {
        std::fs::create_dir_all(p).map_err(|e| Hata::Gecersiz(format!("dizin {}: {e}", p.display())))?;
    }
    std::fs::write(yol, icerik).map_err(|e| Hata::Gecersiz(format!("yazılamadı {}: {e}", yol.display())))
}

fn git(kok: &Path, args: &[&str]) -> Option<String> {
    let o = std::process::Command::new("git").arg("-C").arg(kok).args(args).output().ok()?;
    if !o.status.success() {
        return None;
    }
    Some(String::from_utf8_lossy(&o.stdout).trim().to_string())
}

/// Repo ölçümleri (Karar 121: el kopyası yok, araç çıktısından): HEAD · dal · seans açılışından beri commit ve değişen dosya sayısı.
fn git_olcum(kok: &Path, since: &str) -> serde_json::Value {
    let commits: Vec<String> = git(kok, &["log", "--no-merges", &format!("--since={since}"), "--format=%h %s"])
        .map(|s| s.lines().map(str::to_string).filter(|l| !l.is_empty()).collect())
        .unwrap_or_default();
    let dosyalar: std::collections::BTreeSet<String> = git(kok, &["log", "--no-merges", &format!("--since={since}"), "--name-only", "--format="])
        .map(|s| s.lines().map(str::to_string).filter(|l| !l.is_empty()).collect())
        .unwrap_or_default();
    serde_json::json!({
        "head": git(kok, &["rev-parse", "--short", "HEAD"]),
        "dal": git(kok, &["rev-parse", "--abbrev-ref", "HEAD"]),
        "since": since,
        "commit_sayisi": commits.len(),
        "commitler": commits,
        "degisen_dosya_sayisi": dosyalar.len(),
    })
}

/// D2 → SVG (`d2 --layout=elk`); d2 yoksa ya da hata verirse Err(mesaj) — çağıran uyarı basar, akış durmaz.
fn d2_render(d2: &Path) -> Result<PathBuf, String> {
    let svg = d2.with_extension("svg");
    let o = std::process::Command::new("d2").arg("--layout=elk").arg(d2).arg(&svg).output().map_err(|e| format!("d2 çalışmadı: {e}"))?;
    if o.status.success() { Ok(svg) } else { Err(format!("d2 render hatası: {}", String::from_utf8_lossy(&o.stderr).trim())) }
}

/// Graf türevlerini yazar: tüm-sistem JSON + alan başına (ya da verilen alan) D2; `render` ile SVG. Dönüş: yazılan yollar.
fn graf_yaz(defter: &Defter, kok: &Path, alan: Option<&str>, json_yol: Option<&str>, d2_yol: Option<&str>, bugun: &str, render: bool) -> Result<Vec<String>, Hata> {
    let mut yazilan = vec![];
    let goreli = |p: &Path| p.strip_prefix(kok).unwrap_or(p).display().to_string().replace('\\', "/");
    let json = json_yol.map(PathBuf::from).unwrap_or_else(|| kok.join("ortak").join("akis-graf.json"));
    let model = defter.graf_modeli(alan.filter(|_| json_yol.is_some()), bugun);
    dosya_yaz(&json, &(serde_json::to_string_pretty(&model).expect("json") + "\n"))?;
    yazilan.push(goreli(&json));
    let hedefler: Vec<(Option<&str>, PathBuf)> = match (alan, d2_yol) {
        (_, Some(y)) => vec![(alan, PathBuf::from(y))],
        (Some(a), None) => vec![(Some(a), kok.join("ortak").join("graf").join(format!("akis-{a}.d2")))],
        (None, None) => {
            let mut v: Vec<(Option<&str>, PathBuf)> = ALANLAR
                .iter()
                .filter(|a| defter.kayitlar.values().any(|k| k.alan == **a) || defter.seanslar.values().any(|s| s.alan == **a))
                .map(|a| (Some(*a), kok.join("ortak").join("graf").join(format!("akis-{a}.d2"))))
                .collect();
            v.push((None, kok.join("ortak").join("graf").join("akis-tum.d2")));
            v
        }
    };
    for (a, yol) in hedefler {
        dosya_yaz(&yol, &defter.d2(a, bugun))?;
        yazilan.push(goreli(&yol));
        if render {
            match d2_render(&yol) {
                Ok(svg) => yazilan.push(goreli(&svg)),
                Err(m) => eprintln!("durum: uyarı: {m}"),
            }
        }
    }
    Ok(yazilan)
}

/// Salih özeti (ASD-STE100 Türkçe, kısa etken cümleler): alan başına konum · son seans · sırada · bekleyen Salih kararı.
/// Cümleler seans kayıtlarının (`seans_kapat.kayit` JSON) Claude'un yazdığı alanlarından gelir; Rust yalnız derler.
fn ozet_metni(defter: &Defter, kok: &Path, bugun: &str) -> String {
    let mut s = String::new();
    s.push_str(&format!(
        "# Sistem özeti (Salih için) · AS-OF {} · üretici `durum ozet` (Karar 122; kaynak `ortak/durum-olay.jsonl` + seans kayıtları)\n\n",
        tarih_kismi(bugun)
    ));
    s.push_str("Bu dosya her seans kapanışında yeniden üretilir. Elle düzenlenmez. Görsel: `ortak/graf/akis-<alan>.svg`.\n\n");
    for alan in ALANLAR {
        let seanslar = defter.alan_seanslari(alan);
        let acik = defter.listele(Some(alan), None, bugun).into_iter().filter(|(_, e)| !e.blok_acar()).count();
        if seanslar.is_empty() && acik == 0 {
            continue;
        }
        s.push_str(&format!("## {alan}\n"));
        if let Some(se) = seanslar.last() {
            s.push('\n');
            let hal = se.kapat_ts.as_deref().map_or("açık".to_string(), |t| format!("kapandı {}", tarih_kismi(t)));
            s.push_str(&format!("**Konum:** seans `{}` ({hal}).", se.oturum));
            if let Some(h) = &se.hedef {
                s.push_str(&format!(" Hedef: {h}."));
            }
            match se.hedef_tutuldu {
                Some(true) => s.push_str(" Hedef tutuldu."),
                Some(false) => s.push_str(" Hedef tutmadı."),
                None => {}
            }
            s.push('\n');
            if let Some(k) = &se.kayit {
                if let Ok(m) = std::fs::read_to_string(kok.join(k))
                    && let Ok(v) = serde_json::from_str::<serde_json::Value>(&m)
                {
                    let liste = |ad: &str| -> Vec<String> {
                        v[ad].as_array().map(|a| a.iter().filter_map(|x| x.as_str().map(str::to_string)).collect()).unwrap_or_default()
                    };
                    let bolum = |s: &mut String, baslik: &str, satirlar: Vec<String>| {
                        if !satirlar.is_empty() {
                            s.push_str(&format!("\n**{baslik}**\n"));
                            for l in satirlar {
                                s.push_str(&format!("- {l}\n"));
                            }
                        }
                    };
                    bolum(&mut s, "Son seansta ne değişti", liste("ne_degisti"));
                    let kararlar: Vec<String> = v["kararlar"]
                        .as_array()
                        .map(|a| {
                            a.iter()
                                .filter_map(|k| {
                                    let ad = k["ad"].as_str()?;
                                    Some(format!("{ad}: {}", k["ozet"].as_str().or(k["gerekce"].as_str()).unwrap_or("")))
                                })
                                .collect()
                        })
                        .unwrap_or_default();
                    bolum(&mut s, "Hangi karar verildi", kararlar);
                    bolum(&mut s, "Senin kararını bekleyen", liste("salih_karar"));
                    if let Some(sapma) = v["sapma"].as_str().filter(|x| !x.is_empty()) {
                        s.push_str(&format!("\n**Sapma:** {sapma}\n"));
                    }
                    s.push_str(&format!("\nKayıt: `{k}`\n"));
                } else {
                    s.push_str(&format!("\nKayıt okunamadı: `{k}`\n"));
                }
            }
        }
        let sirada = defter.sirada(alan, bugun);
        if !sirada.is_empty() {
            s.push_str("\n**Sırada (girdileri tamam)**\n");
            for k in sirada {
                s.push_str(&format!("- #{} {}. Sonraki adım: {}.\n", k.id, k.is_ad, k.sonraki_eylem.trim_end_matches('.')));
            }
        }
        let bekleyen: Vec<&Kayit> = defter
            .listele(Some(alan), Some(Durum::Acik), bugun)
            .into_iter()
            .map(|(k, _)| k)
            .filter(|k| k.tur == Tur::Is && !defter.bloklayanlar(k, bugun).is_empty())
            .collect();
        if !bekleyen.is_empty() {
            s.push_str("\n**Bekler (girdisi açık)**\n");
            for k in bekleyen {
                let b: Vec<String> = defter.bloklayanlar(k, bugun).iter().map(|x| format!("#{x}")).collect();
                s.push_str(&format!("- #{} {} bekler: {}.\n", k.id, k.is_ad, b.join(", ")));
            }
        }
        s.push_str(&format!("\nGörsel: `ortak/graf/akis-{alan}.svg` · kaynak `ortak/graf/akis-{alan}.d2`\n\n"));
    }
    s
}

/// Seans teslim girdisinin zorunlu alanları (Claude yazar; Karar 121 beş soru + hedef yoklaması).
const TESLIM_ZORUNLU: [&str; 7] = ["hedef", "hedef_tutuldu", "ne_degisti", "kararlar", "adaylar", "sonraki_ilk_is", "yeniden_acma"];

fn calistir(args: &[String]) -> Result<String, Hata> {
    let a = Arg::coz(args)?;
    let komut = a.konumsal.first().ok_or_else(|| Hata::Kullanim("komut yok".into()))?.as_str();
    let yol = a.al("kutuk").map(PathBuf::from).unwrap_or_else(varsayilan_kutuk);
    let kok_dizin = kok(&yol);
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
            o.tur = match a.al("tur") {
                None | Some("is") => None,
                Some("hedef") => Some(Tur::Hedef),
                Some(x) => return Err(Hata::Kullanim(format!("bilinmeyen tür: {x} (is|hedef)"))),
            };
            o.hedef = match a.al("hedef") {
                None => None,
                Some(h) => Some(h.trim_start_matches('#').parse().map_err(|_| Hata::Kullanim(format!("hedef sayı değil: {h}")))?),
            };
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
            _ => unreachable!(),
        };
        if let (OlayTuru::Bitir, Some(kalan)) = (tur, a.al("kalan")) {
            let (is_ad, sonraki) = kalan.split_once('|').ok_or_else(|| Hata::Kullanim("--kalan \"is|sonraki_eylem\" biçiminde olmalı".into()))?;
            let (alan, hedef) = {
                let k = &defter.kayitlar[&id];
                (k.alan.clone(), k.hedef)
            };
            let mut k = Olay::yalin(OlayTuru::Ac, defter.sonraki_id(), &ts);
            k.alan = Some(alan.clone());
            k.is_ad = Some(is_ad.trim().to_string());
            k.sonraki_eylem = Some(sonraki.trim().to_string());
            k.girdi = vec![id];
            k.hedef = hedef;
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
            let alan = a.alan()?;
            if a.var("json") {
                let konum = defter.konum(alan).map(|s| serde_json::to_value(s).expect("seans"));
                let sirada: Vec<u64> = defter.sirada(alan, &bugun).iter().map(|k| k.id).collect();
                let acik: Vec<serde_json::Value> = defter
                    .listele(Some(alan), None, &bugun)
                    .into_iter()
                    .filter(|(_, e)| !e.blok_acar())
                    .map(|(k, e)| {
                        let mut j = serde_json::to_value(k).expect("kayıt");
                        j["durum"] = serde_json::Value::String(e.ad().to_string());
                        j["bloklayan"] = serde_json::json!(defter.bloklayanlar(k, &bugun));
                        j
                    })
                    .collect();
                let v = serde_json::json!({"alan": alan, "tarih": tarih_kismi(&bugun), "konum": konum, "sirada": sirada, "acik": acik,
                    "graf": {"json": "ortak/akis-graf.json", "d2": format!("ortak/graf/akis-{alan}.d2"), "metin": format!("durum graf --alan {alan} --metin")}});
                Ok(serde_json::to_string_pretty(&v).expect("json") + "\n")
            } else {
                Ok(defter.oturum_basi(alan, &bugun))
            }
        }
        "seans-ac" => {
            let alan = a.alan()?;
            let ad = oturum.unwrap_or_else(|| {
                let taban = format!("{}-{alan}", tarih_kismi(&bugun));
                let mut ad = taban.clone();
                let mut n = 2;
                while defter.seanslar.get(&ad).is_some_and(|s| !s.ortuk) {
                    ad = format!("{taban}-{n}");
                    n += 1;
                }
                ad
            });
            let mut o = Olay::seans(OlayTuru::SeansAc, &ad, alan, &ts);
            o.hedef_cumle = a.al("hedef").map(String::from);
            defter.uygula(&o, &bugun)?;
            ekle(&yol, &[o])?;
            Ok(format!("seans {ad} açıldı\n{}", defter.oturum_basi(alan, &bugun)))
        }
        "seans-kapat" => {
            let alan = a.alan()?;
            let ad = oturum.ok_or_else(|| Hata::Kullanim("--oturum gerekli".into()))?;
            let girdi_yol = a.al("girdi").ok_or_else(|| Hata::Kullanim("--girdi <teslim-girdi.json> gerekli".into()))?;
            let metin = std::fs::read_to_string(girdi_yol).map_err(|e| Hata::Gecersiz(format!("girdi okunamadı {girdi_yol}: {e}")))?;
            let mut kayit: serde_json::Value = serde_json::from_str(&metin).map_err(|e| Hata::Gecersiz(format!("girdi JSON değil: {e}")))?;
            let eksik: Vec<&str> = TESLIM_ZORUNLU.iter().copied().filter(|k| kayit.get(k).is_none()).collect();
            if !eksik.is_empty() {
                return Err(Hata::Gecersiz(format!("teslim girdisinde eksik alan: {}", eksik.join(", "))));
            }
            let hedef_tutuldu = kayit["hedef_tutuldu"].as_bool().ok_or_else(|| Hata::Gecersiz("hedef_tutuldu bool olmalı".into()))?;
            if kayit["sonraki_ilk_is"].as_array().is_none_or(|v| v.is_empty()) {
                return Err(Hata::Gecersiz("sonraki_ilk_is boş olamaz".into()));
            }
            let seans = defter.seanslar.get(&ad).ok_or_else(|| Hata::Gecersiz(format!("seans {ad} açılmamış (önce seans-ac)")))?.clone();
            let etiket = a.al("etiket").map(String::from).or_else(|| kayit["etiket"].as_str().map(String::from)).unwrap_or_else(|| "seans".into());
            let etiket_temiz: String = etiket.chars().map(|c| if c.is_ascii_alphanumeric() || c == '-' { c } else { '-' }).collect();
            let kayit_rel = format!("{alan}/raporlar/seans/seans-teslim-{}-{etiket_temiz}.json", tarih_kismi(&bugun));
            // Rust'ın ürettiği alanlar (Karar 121: ölçüm el kopyası değil).
            kayit["sema"] = serde_json::json!(TESLIM_SEMA);
            kayit["alan"] = serde_json::json!(alan);
            kayit["oturum"] = serde_json::json!(ad);
            kayit["tarih"] = serde_json::json!(tarih_kismi(&bugun));
            kayit["etiket"] = serde_json::json!(etiket_temiz);
            let dokunulan = seans.dokunulan();
            kayit["olcum"] = serde_json::json!({
                "ac_ts": seans.ac_ts, "kapat_ts": ts,
                "git": git_olcum(&kok_dizin, &seans.ac_ts),
                "durum": {"acilan": seans.acilan, "alinan": seans.alinan, "bitirilen": seans.bitirilen,
                           "acik_kalan": defter.listele(Some(alan), None, &bugun).into_iter().filter(|(_, e)| !e.blok_acar()).count()},
            });
            kayit["baglar"]["durum"] = serde_json::json!(dokunulan);
            dosya_yaz(&kok_dizin.join(&kayit_rel), &(serde_json::to_string_pretty(&kayit).expect("json") + "\n"))?;
            let mut o = Olay::seans(OlayTuru::SeansKapat, &ad, alan, &ts);
            o.hedef_tutuldu = Some(hedef_tutuldu);
            o.hedef_cumle = kayit["hedef"].as_str().map(String::from);
            o.kayit = Some(kayit_rel.clone());
            o.etiket = Some(etiket_temiz);
            defter.uygula(&o, &bugun)?;
            ekle(&yol, &[o])?;
            let mut yazilan = graf_yaz(&defter, &kok_dizin, None, None, None, &bugun, a.var("render"))?;
            let ozet = kok_dizin.join("ortak").join("SALIH-OZET.md");
            dosya_yaz(&ozet, &ozet_metni(&defter, &kok_dizin, &bugun))?;
            yazilan.push("ortak/SALIH-OZET.md".to_string());
            Ok(format!("seans {ad} kapandı · kayıt {kayit_rel}\nyazılan: {}\n", yazilan.join(" · ")))
        }
        "graf" => {
            let alan = a.al("alan");
            if let Some(x) = alan
                && !ALANLAR.contains(&x)
            {
                return Err(Hata::Kullanim(format!("bilinmeyen alan: {x}")));
            }
            if a.var("metin") {
                return Ok(match alan {
                    Some(x) => defter.graf_metni(x, &bugun),
                    None => ALANLAR.iter().map(|x| defter.graf_metni(x, &bugun)).collect::<Vec<_>>().join("\n"),
                });
            }
            let yazilan = graf_yaz(&defter, &kok_dizin, alan, a.al("json"), a.al("d2"), &bugun, a.var("render"))?;
            Ok(format!("yazılan: {}\n", yazilan.join(" · ")))
        }
        "ozet" => {
            let cikti = a.al("cikti").map(PathBuf::from).unwrap_or_else(|| kok_dizin.join("ortak").join("SALIH-OZET.md"));
            dosya_yaz(&cikti, &ozet_metni(&defter, &kok_dizin, &bugun))?;
            Ok(format!("yazılan: {}\n", cikti.display()))
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
