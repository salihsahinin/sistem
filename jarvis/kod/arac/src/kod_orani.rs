//! `tools/kod-orani-olcum.py` karşılığı: İB-71 baseline ölçümü (repo içerik oranı ↔ bağlam-penceresi oranı, dört kova).
//! Çıkış: 0 tamam · 1 `sys.exit(metin)` (hareket kütüğü yok/bozuk, --bugun/--repo hatası) · 2 argparse hatası.
//! Python'da yakalanmamış istisna olurdu durumlar (beklenmedik JSON türü, yazma hatası, tarih taşması) `py::coker` ile çıkış 1'dir.
//! Bilinçli ayrışmalar: `os.walk` dizin bağlantılarına (symlink/junction) inilmez; git çıktısı yalnız UTF-8 çözülür.
use chrono::{Datelike, Duration, Local, NaiveDate, Weekday};
use jarvis_hook::ortak::{py_dumps, py_truthy};
use jarvis_rituel::argparse::{Ayrisan, Secenek};
use jarvis_rituel::harness_anahtar;
use jarvis_rituel::py;
use regex::Regex;
use serde_json::{Map, Value, json};
use std::collections::HashSet;
use std::io::Write;
use std::path::Path;
use std::process::Command;

/// `--help` açıklaması (Python `__doc__`, `RawDescriptionHelpFormatter`: aynen basılır).
const ACIKLAMA: &str = r#"kod-orani-olcum.py — İB-71 baseline ölçümü: repo-genel içerik oranı ↔ bağlam-penceresi (Salih'in son 3 gün
okuduğu dosyalar) oranı arasındaki fark, DÖRT kovaya ayrılarak (md · kod · yapisal · diger).

Ne bu: iki ayrı ölçüm üretir —
  (i) REPO ENVANTERİ: ~/sistem/jarvis altındaki (`.git`, `veri/bronz`, `veri/gorunum` HARİÇ) her dosyayı uzantısına göre
      kovaya koyar (md=.md · kod=.py/.sh/.sql · yapisal=.json/.jsonl/.csv · diger=geri kalan), kova başına
      dosya sayısı + toplam satır (\n bayt sayımı — ikili dosyada da güvenli, exception atmaz) + toplam bayt.
  (ii) BAĞLAM-PENCERESİ PROXY'Sİ: `veri/bronz/hareket-olay.jsonl` (şema: hareket_id/ts/oturum/arac/girdi_ozet/
      dosya/repo_ici/sonuc/model/kaynak_dosya/yuklendi_head/okuma_tipi — gerçek veriden çıkarıldı, tahmin
      edilmedi) son N=3 gün penceresindeki dosya-okuma olaylarını tarar: `arac=="Read"` ∧ `dosya` doluysa o
      yol doğrudan sayılır; `arac=="Bash"` içinde cat/head/tail/sed/less/more/nl/awk komutlarının ARDINDAN
      geçen uzantılı path-benzeri token'lar HEURİSTİK regex'le çıkarılır (docstring'te işaretli — bu bir
      kesin ayrıştırıcı değildir, AXI A6 salt-okur sınıfı). Kütükte satır-bazlı okuma miktarı alanı YOK
      (okuma_tipi yalnız aralik/bütün bilgisi taşır, satır sayısı değil) → ağırlık dosya-sayımı (1 olay = 1
      sayım), görev metninin "yoksa dosya-sayımı olarak say" dalı.

Grain: 1 koşum = 1 çıktı satırı (`veri/kod-orani.jsonl`, append-only).

Modlar: `--json` (AXI A1: stdout tek JSON nesnesi, insan satırları stderr) · `--pencere-gun N` (varsayılan 3) ·
`--bugun YYYY-MM-DD` (A3 determinizm için zaman enjeksiyonu — yoksa sistem bugünü) · `--kuru` (kütüğe yazmaz).

Kullanım: `python3 tools/kod-orani-olcum.py [--pencere-gun 3] [--bugun 2026-09-03] [--kuru] [--json] [--sessiz]`

Çıkış: 0 tamam · 2 girdi/kullanım hatası (A2 sözlüğü; hareket-olay.jsonl yoksa ya da bilinmeyen bayrak).

Yan-etki (A6): EKLEMELİ — yalnız `veri/kod-orani.jsonl`e append-only tek satır yazar (--kuru ile yazmaz);
başka hiçbir dosyaya dokunmaz, salt-okur tarama.

Kayıt: İB-71 (Salih 09-03), Jarvis yan-oturum işçi-ajanı.
"#;

type Oran = Map<String, Value>;

fn bos_oran() -> Oran {
    let mut m = Map::new();
    for k in ["md", "kod", "yapisal", "diger"] {
        m.insert(format!("{k}_satir"), json!(0));
        m.insert(format!("{k}_dosya"), json!(0));
    }
    m
}

fn al(m: &Oran, k: &str) -> i64 {
    m.get(k).and_then(Value::as_i64).unwrap_or(0)
}

/// `oran[k] = oran.get(k, 0) + n` (yeni anahtar sona eklenir, var olanın sırası korunur).
fn arttir(m: &mut Oran, k: &str, n: i64) {
    let v = al(m, k) + n;
    m.insert(k.to_string(), json!(v));
}

/// `genericpath._splitext` (ntpath/posixpath): uzantı (nokta dahil) ya da boş.
fn uzanti(p: &str) -> &str {
    let sep = if cfg!(windows) { p.rfind(['/', '\\']) } else { p.rfind('/') };
    let Some(nokta) = p.rfind('.') else { return "" };
    if sep.is_some_and(|s| nokta < s) {
        return "";
    }
    let baslangic = sep.map(|s| s + 1).unwrap_or(0);
    if p[baslangic..nokta].chars().any(|c| c != '.') { &p[nokta..] } else { "" }
}

fn kova_ver(yol: &str) -> &'static str {
    match uzanti(yol).to_lowercase().as_str() {
        ".md" => "md",
        ".py" | ".sh" | ".sql" => "kod",
        ".json" | ".jsonl" | ".csv" => "yapisal",
        _ => "diger",
    }
}

/// `\n` bayt sayımı; okunamayan dosya 0.
fn satir_say(yol: &Path) -> i64 {
    match std::fs::read(yol) {
        Ok(v) => {
            let mut n = v.iter().filter(|&&b| b == b'\n').count() as i64;
            if !v.is_empty() && *v.last().unwrap() != b'\n' {
                n += 1;
            }
            n
        }
        Err(_) => 0,
    }
}

/// `git ls-files --others --ignored --exclude-standard --directory -z`; başarısızlıkta `None`.
fn gitignore_disla_kumesi(kok: &str) -> Option<HashSet<String>> {
    let mut c = Command::new("git");
    c.args(["ls-files", "--others", "--ignored", "--exclude-standard", "--directory", "-z"]).current_dir(kok);
    let r = py::calistir_zamanli(c, 30)?;
    if r.kod != Some(0) {
        return None;
    }
    let s = String::from_utf8(r.out).ok()?;
    Some(py::evrensel_satir(&s).split('\0').filter(|p| !p.is_empty()).map(String::from).collect())
}

fn gitignore_disli_mi(goreli: &str, kume: &Option<HashSet<String>>, dizin_mi: bool) -> bool {
    let Some(kume) = kume else { return false };
    let g = goreli.replace(py::SEP, "/");
    let dizin = format!("{g}/");
    if dizin_mi { kume.contains(&dizin) } else { kume.contains(&g) || kume.contains(&dizin) }
}

struct Yuruyus<'a> {
    kume: &'a Option<HashSet<String>>,
    oran: Oran,
    okunamayan: i64,
    disla: [String; 3],
}

impl Yuruyus<'_> {
    /// `os.walk(kok)` (yukarıdan aşağı, `scandir` sırası): önce bu dizinin dosyaları, sonra budanmış alt dizinler.
    fn yuru(&mut self, dizin: &Path, goreli_dizin: &str) {
        let Ok(rd) = std::fs::read_dir(dizin) else { return };
        let mut girdiler = vec![];
        for e in rd {
            match e {
                Ok(e) => girdiler.push(e),
                Err(_) => return,
            }
        }
        let mut dizinler: Vec<(String, bool)> = vec![];
        let mut dosyalar: Vec<String> = vec![];
        for e in &girdiler {
            let ad = e.file_name().to_string_lossy().into_owned();
            let ft = e.file_type();
            let baglanti = ft.as_ref().is_ok_and(|f| f.is_symlink());
            let dizin_mi = match &ft {
                Ok(f) if f.is_dir() => true,
                Ok(f) if f.is_symlink() => std::fs::metadata(e.path()).is_ok_and(|m| m.is_dir()),
                _ => false,
            };
            if dizin_mi { dizinler.push((ad, baglanti)) } else { dosyalar.push(ad) }
        }
        let birlestir = |ad: &str| if goreli_dizin.is_empty() { ad.to_string() } else { format!("{goreli_dizin}{}{ad}", py::SEP) };
        for ad in &dosyalar {
            let goreli_dosya = birlestir(ad);
            if gitignore_disli_mi(&goreli_dosya, self.kume, false) {
                continue;
            }
            let tam = dizin.join(ad);
            let k = kova_ver(ad);
            arttir(&mut self.oran, &format!("{k}_dosya"), 1);
            match std::fs::metadata(&tam) {
                Ok(m) => {
                    arttir(&mut self.oran, &format!("{k}_bayt"), m.len() as i64);
                    let n = satir_say(&tam);
                    arttir(&mut self.oran, &format!("{k}_satir"), n);
                }
                Err(_) => self.okunamayan += 1,
            }
        }
        for (ad, baglanti) in &dizinler {
            let aday = birlestir(ad);
            if ad == ".git" || self.disla.contains(&aday) || gitignore_disli_mi(&aday, self.kume, true) {
                continue;
            }
            if *baglanti {
                continue;
            }
            self.yuru(&dizin.join(ad), &aday);
        }
    }
}

fn repo_envanteri(kok: &str, kume: &Option<HashSet<String>>) -> (Oran, i64) {
    let sep = py::SEP;
    let mut y = Yuruyus {
        kume,
        oran: bos_oran(),
        okunamayan: 0,
        disla: [format!("veri{sep}bronz"), format!("veri{sep}gorunum"), format!("arsiv{sep}karantina")],
    };
    y.yuru(Path::new(kok), "");
    (y.oran, y.okunamayan)
}

/// Python `sys.exit(metin)`: stderr + çıkış 1.
fn cik(metin: &str) -> i32 {
    py::err(&format!("{metin}\n"));
    1
}

/// Hareket kütüğü okuması; `Err(çıkış kodu)`.
fn hareket_olaylarini_oku(yol: &str) -> Result<Vec<Value>, i32> {
    if !Path::new(yol).is_file() {
        return Err(cik(&format!("HATA: hareket kütüğü bulunamadı: {yol} (kod 2)")));
    }
    let metin = match py::oku_kati(Path::new(yol)) {
        Ok(m) => m,
        Err(py::OkuHata::Io(e)) => return Err(py::coker(&format!("{yol}: {e}"))),
        Err(py::OkuHata::Kod) => return Err(py::coker(&format!("{yol}: UnicodeDecodeError"))),
    };
    let mut satirlar: Vec<&str> = metin.split('\n').collect();
    if satirlar.last() == Some(&"") {
        satirlar.pop();
    }
    let mut olaylar = vec![];
    for (i, satir) in satirlar.iter().enumerate() {
        let satir = py::strip(satir);
        if satir.is_empty() || satir.starts_with('#') {
            continue;
        }
        match serde_json::from_str::<Value>(satir) {
            Ok(v) => olaylar.push(v),
            Err(_) => return Err(cik(&format!("HATA: hareket-olay.jsonl satır {} bozuk JSON (kod 2)", i + 1))),
        }
    }
    Ok(olaylar)
}

fn bash_dosyalarini_cikar(girdi_ozet: &str, komut_rx: &Regex, yol_rx: &Regex) -> Vec<String> {
    if girdi_ozet.is_empty() {
        return vec![];
    }
    let mut komut_bolumu = girdi_ozet;
    if girdi_ozet.contains('⟨') && girdi_ozet.contains('⟩') {
        let kuyruk = girdi_ozet.split_once('⟨').unwrap().1;
        komut_bolumu = kuyruk.rsplit_once('⟩').map(|(a, _)| a).unwrap_or(kuyruk);
    }
    let mut yollar = vec![];
    for c in komut_rx.captures_iter(komut_bolumu) {
        let kuyruk = c.get(2).map(|m| m.as_str()).unwrap_or("");
        for t in yol_rx.find_iter(kuyruk) {
            if t.as_str().starts_with('-') {
                continue;
            }
            yollar.push(t.as_str().to_string());
        }
    }
    yollar
}

fn iso(d: NaiveDate) -> String {
    format!("{:04}-{:02}-{:02}", d.year(), d.month(), d.day())
}

/// Python 3.11 `date.fromisoformat`: `YYYY-MM-DD`, `YYYYMMDD`, ISO hafta biçimleri (`YYYY-Www[-D]`, `YYYYWww[D]`).
fn tarih_ayristir(s: &str) -> Option<NaiveDate> {
    if !s.is_ascii() {
        return None;
    }
    let b = s.as_bytes();
    let say = |a: usize, z: usize| -> Option<u32> {
        let p = s.get(a..z)?;
        if p.bytes().all(|c| c.is_ascii_digit()) { p.parse().ok() } else { None }
    };
    if b.len() < 7 {
        return None;
    }
    let yil = say(0, 4)? as i32;
    let ayrac = b[4] == b'-';
    let kalan = &s[if ayrac { 5 } else { 4 }..];
    let kb = kalan.as_bytes();
    if kb.first() == Some(&b'W') {
        let (hafta_s, gun_s) = if ayrac {
            match kb.len() {
                3 => (&kalan[1..3], None),
                5 if kb[3] == b'-' => (&kalan[1..3], Some(&kalan[4..5])),
                _ => return None,
            }
        } else {
            match kb.len() {
                3 => (&kalan[1..3], None),
                4 => (&kalan[1..3], Some(&kalan[3..4])),
                _ => return None,
            }
        };
        if !hafta_s.bytes().all(|c| c.is_ascii_digit()) || gun_s.is_some_and(|g| !g.bytes().all(|c| c.is_ascii_digit())) {
            return None;
        }
        let hafta: u32 = hafta_s.parse().ok()?;
        let gun: u32 = gun_s.map(|g| g.parse().unwrap()).unwrap_or(1);
        let hg = match gun {
            1 => Weekday::Mon,
            2 => Weekday::Tue,
            3 => Weekday::Wed,
            4 => Weekday::Thu,
            5 => Weekday::Fri,
            6 => Weekday::Sat,
            7 => Weekday::Sun,
            _ => return None,
        };
        if yil < 1 {
            return None;
        }
        let d = NaiveDate::from_isoywd_opt(yil, hafta, hg)?;
        return if (1..=9999).contains(&d.year()) { Some(d) } else { None };
    }
    let (ay, gun) = if ayrac {
        if kb.len() != 5 || kb[2] != b'-' {
            return None;
        }
        (say(5, 7)?, say(8, 10)?)
    } else {
        if kb.len() != 4 {
            return None;
        }
        (say(4, 6)?, say(6, 8)?)
    };
    if yil < 1 {
        return None;
    }
    NaiveDate::from_ymd_opt(yil, ay, gun)
}

/// `(oran, olay_n, esik)`; `Err` = Python'da yakalanmamış istisna.
fn baglam_penceresi_orani(olaylar: &[Value], pencere_gun: i128, bugun: NaiveDate) -> Result<(Oran, i64, String), String> {
    let esik_tarih = i64::try_from(pencere_gun)
        .ok()
        .filter(|g| g.abs() <= 999_999_999)
        .and_then(|g| Duration::try_days(g))
        .and_then(|d| bugun.checked_sub_signed(d))
        .filter(|d| (1..=9999).contains(&d.year()))
        .ok_or_else(|| "OverflowError: date value out of range".to_string())?;
    let esik = iso(esik_tarih);
    let komut_rx = Regex::new(r"\b(cat|head|tail|sed|less|more|nl|awk)\b([^|;&\n]*)").unwrap();
    let yol_rx = Regex::new(r"[A-Za-z0-9_./\-]+\.[A-Za-z0-9]+").unwrap();
    let mut oran = bos_oran();
    let mut olay_n = 0i64;
    for o in olaylar {
        let Value::Object(m) = o else { return Err("AttributeError: olay nesne değil (.get)".into()) };
        let ts = match m.get("ts") {
            Some(v) if py_truthy(v) => match v {
                Value::String(s) => s.as_str(),
                _ => return Err("TypeError: ts dize değil".into()),
            },
            _ => "",
        };
        let ilk10: String = ts.chars().take(10).collect();
        if ilk10.as_str() < esik.as_str() {
            continue;
        }
        let arac = m.get("arac");
        let mut yollar: Vec<String> = vec![];
        if arac == Some(&Value::String("Read".into())) && m.get("dosya").is_some_and(py_truthy) {
            match m.get("dosya") {
                Some(Value::String(s)) => yollar.push(s.clone()),
                _ => return Err("TypeError: dosya dize değil".into()),
            }
        } else if arac == Some(&Value::String("Bash".into())) {
            match m.get("girdi_ozet") {
                Some(v) if py_truthy(v) => match v {
                    Value::String(s) => yollar = bash_dosyalarini_cikar(s, &komut_rx, &yol_rx),
                    _ => return Err("TypeError: girdi_ozet dize değil".into()),
                },
                _ => {}
            }
        }
        for yol in yollar {
            let k = kova_ver(&yol);
            arttir(&mut oran, &format!("{k}_dosya"), 1);
            olay_n += 1;
        }
    }
    Ok((oran, olay_n, esik))
}

fn git_head(kok: &str) -> String {
    let mut c = Command::new("git");
    c.args(["rev-parse", "--short", "HEAD"]).current_dir(kok);
    if let Some(r) = py::calistir_zamanli(c, 10)
        && r.kod == Some(0)
        && let Ok(s) = String::from_utf8(r.out)
    {
        return py::strip(&py::evrensel_satir(&s)).to_string();
    }
    "bilinmiyor".to_string()
}

pub fn kos(argv: &[String]) -> i32 {
    let ayrisan = Ayrisan::yeni(
        "kod-orani-olcum.py",
        Some(ACIKLAMA),
        vec![
            Secenek::deger(&["--repo"], "repo", Some("repo kökü (varsayılan: bu dosyanın üst-üst dizini)")),
            Secenek::tam(&["--pencere-gun"], "pencere_gun", Some("bağlam-penceresi gün sayısı (varsayılan 3)")),
            Secenek::deger(&["--bugun"], "bugun", Some("YYYY-MM-DD determinizm damgası (yoksa sistem bugünü)")),
            Secenek::bayrak(&["--kuru"], "kuru", Some("kütüğe yazma (prova)")),
            Secenek::bayrak(&["--json"], "json", Some("stdout = tek JSON nesnesi (A1)")),
            Secenek::bayrak(&["--sessiz"], "sessiz", Some("insan çıktısını kıs")),
        ],
    );
    let a = match ayrisan.ayristir(argv) {
        Ok(a) => a,
        Err(k) => return k,
    };
    let varsayilan_kok = harness_anahtar::jarvis();
    let kutuk = py::join(&py::join(&varsayilan_kok, "veri"), "kod-orani.jsonl");
    let pencere_gun = a.tam("pencere_gun").unwrap_or(3);
    let (kuru, json_mod, sessiz) = (a.bayrak("kuru"), a.bayrak("json"), a.bayrak("sessiz"));
    let insan = |s: &str| {
        if json_mod { py::err(&format!("{s}\n")) } else { py::print(s) }
    };

    let bugun = match a.metin("bugun").filter(|s| !s.is_empty()) {
        Some(s) => match tarih_ayristir(s) {
            Some(d) => d,
            None => return cik("HATA: --bugun YYYY-MM-DD biçiminde olmalı (kod 2)"),
        },
        None => Local::now().date_naive(),
    };

    let kok = py::abspath(a.metin("repo").unwrap_or(&varsayilan_kok));
    if !Path::new(&kok).is_dir() {
        return cik(&format!("HATA: --repo dizini yok: {kok} (kod 2)"));
    }

    let kume = gitignore_disla_kumesi(&kok);
    if kume.is_none() && !sessiz {
        insan("  UYARI: git ls-files --ignored çalışmadı (git yok/repo değil) — .gitignore süzgeci UYGULANMADI, eski (süzgeçsiz) davranışa düşüldü.");
    }
    let (repo_oran, okunamayan) = repo_envanteri(&kok, &kume);
    let hareket_yolu = py::join(&py::join(&py::join(&kok, "veri"), "bronz"), "hareket-olay.jsonl");
    let olaylar = match hareket_olaylarini_oku(&hareket_yolu) {
        Ok(o) => o,
        Err(k) => return k,
    };
    let (baglam_oran, olay_n, esik) = match baglam_penceresi_orani(&olaylar, pencere_gun, bugun) {
        Ok(r) => r,
        Err(neden) => return py::coker(&neden),
    };

    let head = git_head(&kok);
    let satir = json!({
        "tarih": iso(bugun),
        "git_head": head,
        "repo_orani": Value::Object(repo_oran.clone()),
        "baglam_orani": Value::Object(baglam_oran.clone()),
    });

    let mut yazildi = false;
    if !kuru {
        let yazma = (|| -> std::io::Result<()> {
            if let Some(ust) = Path::new(&kutuk).parent() {
                std::fs::create_dir_all(ust)?;
            }
            let mut f = std::fs::OpenOptions::new().append(true).create(true).open(&kutuk)?;
            f.write_all(format!("{}\n", py_dumps(&satir)).as_bytes())
        })();
        if let Err(e) = yazma {
            return py::coker(&format!("{kutuk}: {e}"));
        }
        yazildi = true;
    }

    if !sessiz {
        insan(&format!("kod-orani-olcum — AS-OF {} (git_head {head})", iso(bugun)));
        insan(&format!("  repo envanteri ({okunamayan} dosya okunamadı):"));
        for k in ["md", "kod", "yapisal", "diger"] {
            insan(&format!(
                "    {} dosya={:<5} satir={:<8} bayt={}",
                py::sola_hizala(k, 8),
                al(&repo_oran, &format!("{k}_dosya")),
                al(&repo_oran, &format!("{k}_satir")),
                al(&repo_oran, &format!("{k}_bayt"))
            ));
        }
        insan(&format!("  baglam penceresi (son {pencere_gun} gün, esik>={esik}, {olay_n} okuma-olayı):"));
        for k in ["md", "kod", "yapisal", "diger"] {
            insan(&format!("    {} dosya={}", py::sola_hizala(k, 8), al(&baglam_oran, &format!("{k}_dosya"))));
        }
        insan(&format!("  kütük: {}", if yazildi { "yazıldı" } else { "--kuru (yazılmadı)" }));
    }

    if json_mod {
        let cikti = json!({
            "arac": "kod-orani-olcum",
            "surum": "0.1",
            "git_head": head,
            "cikis": 0,
            "kayit": satir,
            "okunamayan_dosya_n": okunamayan,
            "baglam_olay_n": olay_n,
            "kutuk_yazildi": yazildi,
        });
        py::print(&py_dumps(&cikti));
    }
    0
}
