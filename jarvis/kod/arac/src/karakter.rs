//! `karakter-turet`: karakter ajanı kanonunun çekirdeğinden ajan ve skill kopyalarını üretir (Karar 130 B12).
//!
//! Kanon `core/<ad>-ajani.md` içinde çekirdek `<!-- cekirdek:bas -->` ile `<!-- cekirdek:son -->` arasındadır;
//! arada tek bir ``` çiti varsa çit satırları atılır. Kelime sınırı (varsayılan 1600) yalnız çekirdeğe uygulanır.
//! Hedef dosyada frontmatter (`---` blokları) ve üretim yorumundan önceki önsöz korunur; gövde çekirdekle değişir.
//! Çıkış: 0 yazıldı ya da uyumlu · 1 `--denetle` kipinde sapma · 2 sınır aşımı · 3 kullanım ya da dosya hatası.

use std::fs;
use std::path::Path;

pub const BAS_ISARETI: &str = "<!-- cekirdek:bas -->";
pub const SON_ISARETI: &str = "<!-- cekirdek:son -->";
pub const VARSAYILAN_SINIR: usize = 1600;
/// Hedefte bu işaretten sonrası hedef-özel sonsözdür; üretimde korunur, sınıra sayılmaz.
pub const SONSOZ_ISARETI: &str = "<!-- karakter-turet:sonsoz -->";

const YARDIM: &str = "\
karakter-turet: karakter kanonunun çekirdeğinden ajan ve skill kopyalarını üretir (Karar 130 B12)

Kullanım:
  karakter-turet --kanon <core/x-ajani.md> --ajan <.claude/agents/x.md> [--skill <SKILL.md>] [--denetle] [--sinir N] [--cikti <dizin>]

Seçenekler:
  --kanon <yol>   çekirdeği taşıyan kanon dosyası (işaretler: <!-- cekirdek:bas --> ve <!-- cekirdek:son -->)
  --ajan <yol>    üretilecek ajan dosyası (frontmatter korunur)
  --skill <yol>   üretilecek skill dosyası (isteğe bağlı; frontmatter ve önsöz korunur)
                  hedefte <!-- karakter-turet:sonsoz --> satırından sonrası hedef-özel ektir, korunur
  --denetle       yazma; yalnız sınır ve sapma denetimi yap
  --sinir N       çekirdek kelime sınırı (varsayılan 1600)
  --cikti <dizin> hedefleri yerine yazma, aynı dosya adıyla bu dizine yaz (Bash teli korumalı dizinler için)
  -h, --help      bu yardım

Çıkış kodları: 0 tamam · 1 sapma (--denetle) · 2 sınır aşımı · 3 kullanım ya da dosya hatası
Hedef dosya henüz yoksa önce en azından frontmatter'ı elle yazılmalıdır.
";

/// Kanon metninden çekirdeği çıkarır; işaretler tek ve sıralı olmalı.
pub fn cekirdek_cikar(kanon: &str) -> Result<String, String> {
    let metin = kanon.replace("\r\n", "\n");
    let bas_sayi = metin.matches(BAS_ISARETI).count();
    let son_sayi = metin.matches(SON_ISARETI).count();
    if bas_sayi != 1 || son_sayi != 1 {
        return Err(format!("işaretler tam bir kez geçmeli: bas {bas_sayi}, son {son_sayi}"));
    }
    let bas = metin.find(BAS_ISARETI).unwrap() + BAS_ISARETI.len();
    let son = metin.find(SON_ISARETI).unwrap();
    if son < bas {
        return Err("cekirdek:son işareti cekirdek:bas işaretinden önce".into());
    }
    let mut satirlar: Vec<&str> = metin[bas..son].trim_matches('\n').lines().collect();
    // Çekirdek tek bir kod çiti içindeyse çit satırlarını at.
    if satirlar.len() >= 2 && satirlar[0].trim_start().starts_with("```") && satirlar.last().unwrap().trim() == "```" {
        satirlar.remove(0);
        satirlar.pop();
    }
    let govde = satirlar.join("\n").trim().to_string();
    if govde.is_empty() {
        return Err("çekirdek boş".into());
    }
    Ok(govde)
}

/// Boşlukla ayrılmış kelime sayısı (`wc -w` ile aynı ölçü).
pub fn kelime_say(metin: &str) -> usize {
    metin.split_whitespace().count()
}

/// Üretilen gövdenin başına konan yorum satırı.
pub fn uretim_yorumu(kanon_adi: &str) -> String {
    format!("<!-- bu gövde `{kanon_adi}` çekirdeğinden `karakter-turet` ile üretilir; elle düzenleme, kanonu değiştir ve yeniden türet -->")
}

/// Hedefin korunacak başını (frontmatter + üretim yorumundan önceki önsöz) döndürür.
fn korunan_bas(hedef: &str) -> String {
    let metin = hedef.replace("\r\n", "\n");
    let mut bas = String::new();
    let mut kalan = metin.as_str();
    if let Some(sonrasi) = kalan.strip_prefix("---\n") {
        if let Some(i) = sonrasi.find("\n---\n") {
            let uzunluk = 4 + i + 5;
            bas.push_str(&kalan[..uzunluk]);
            kalan = &kalan[uzunluk..];
        }
    }
    // Önsöz: önceki üretim yorumuna (ya da eski elle yazılmış kaynak yorumuna) kadar olan metin.
    let isaret = kalan
        .find("<!-- bu gövde ")
        .or_else(|| kalan.find("<!-- kaynak:"));
    if let Some(i) = isaret {
        bas.push_str(&kalan[..i]);
    } else {
        // Yorum yoksa gövde tamamen değişir; frontmatter ile gövde arasında bir boş satır kalır.
        bas.push('\n');
    }
    bas
}

/// Hedefin korunacak sonu: sonsöz işaretinden dosya sonuna kadar (hedef-özel ekler, ör. skill'in `$ARGUMENTS` satırı).
fn korunan_son(hedef: &str) -> String {
    let metin = hedef.replace("\r\n", "\n");
    match metin.find(SONSOZ_ISARETI) {
        Some(i) => {
            let son = metin[i..].trim_end();
            format!("\n{son}\n")
        }
        None => String::new(),
    }
}

/// Hedef dosyanın beklenen içeriğini (LF satır sonlu) üretir.
pub fn hedef_uret(hedef: &str, cekirdek: &str, kanon_adi: &str) -> String {
    format!("{}{}\n{}\n{}", korunan_bas(hedef), uretim_yorumu(kanon_adi), cekirdek, korunan_son(hedef))
}

/// İki metnin ilk farklı satırını (1 tabanlı) verir; eşitse None.
pub fn ilk_fark(a: &str, b: &str) -> Option<(usize, String, String)> {
    let a = a.replace("\r\n", "\n");
    let b = b.replace("\r\n", "\n");
    if a == b {
        return None;
    }
    let al: Vec<&str> = a.lines().collect();
    let bl: Vec<&str> = b.lines().collect();
    let n = al.len().max(bl.len());
    for i in 0..n {
        let x = al.get(i).copied().unwrap_or("<dosya sonu>");
        let y = bl.get(i).copied().unwrap_or("<dosya sonu>");
        if x != y {
            return Some((i + 1, x.to_string(), y.to_string()));
        }
    }
    Some((n, String::new(), String::new()))
}

fn kisalt(s: &str) -> String {
    let k: String = s.chars().take(100).collect();
    if k.len() < s.len() { format!("{k}…") } else { k }
}

fn kanon_adi(yol: &Path) -> String {
    let dosya = yol.file_name().map(|d| d.to_string_lossy().into_owned()).unwrap_or_default();
    match yol.parent().and_then(|p| p.file_name()) {
        Some(ust) if ust == "core" => format!("core/{dosya}"),
        _ => yol.to_string_lossy().replace('\\', "/"),
    }
}

pub fn kos(argv: &[String]) -> i32 {
    let mut kanon: Option<String> = None;
    let mut hedefler: Vec<String> = Vec::new();
    let mut denetle = false;
    let mut sinir = VARSAYILAN_SINIR;
    let mut cikti: Option<String> = None;
    let mut i = 0;
    while i < argv.len() {
        let a = argv[i].as_str();
        let deger = |i: usize| argv.get(i + 1).cloned();
        match a {
            "-h" | "--help" => {
                print!("{YARDIM}");
                return 0;
            }
            "--kanon" | "--ajan" | "--skill" | "--sinir" | "--cikti" => {
                let Some(d) = deger(i) else {
                    eprintln!("hata: {a} bir değer ister\n\n{YARDIM}");
                    return 3;
                };
                match a {
                    "--kanon" => kanon = Some(d),
                    "--sinir" => match d.parse() {
                        Ok(n) => sinir = n,
                        Err(_) => {
                            eprintln!("hata: --sinir sayı ister: {d}");
                            return 3;
                        }
                    },
                    "--cikti" => cikti = Some(d),
                    _ => hedefler.push(d),
                }
                i += 2;
                continue;
            }
            "--denetle" => denetle = true,
            _ => {
                eprintln!("hata: bilinmeyen argüman: {a}\n\n{YARDIM}");
                return 3;
            }
        }
        i += 1;
    }
    let Some(kanon) = kanon else {
        eprintln!("hata: --kanon gerekli\n\n{YARDIM}");
        return 3;
    };
    if hedefler.is_empty() {
        eprintln!("hata: en az --ajan gerekli\n\n{YARDIM}");
        return 3;
    }
    let kanon_metni = match fs::read_to_string(&kanon) {
        Ok(m) => m,
        Err(e) => {
            eprintln!("hata: kanon okunamadı {kanon}: {e}");
            return 3;
        }
    };
    let cekirdek = match cekirdek_cikar(&kanon_metni) {
        Ok(c) => c,
        Err(e) => {
            eprintln!("hata: {kanon}: {e}");
            return 3;
        }
    };
    let sayi = kelime_say(&cekirdek);
    if sayi > sinir {
        eprintln!("sınır aşıldı: çekirdek {sayi} kelime > {sinir}");
        return 2;
    }
    println!("çekirdek: {sayi} kelime (sınır {sinir})");
    let ad = kanon_adi(Path::new(&kanon));
    let mut sapma = false;
    for hedef in &hedefler {
        let mevcut = match fs::read_to_string(hedef) {
            Ok(m) => m,
            Err(e) => {
                eprintln!("hata: hedef okunamadı {hedef}: {e} (önce frontmatter'ı elle yaz)");
                return 3;
            }
        };
        let beklenen = hedef_uret(&mevcut, &cekirdek, &ad);
        let fark = ilk_fark(&mevcut, &beklenen);
        if denetle {
            match fark {
                None => println!("uyumlu: {hedef}"),
                Some((n, eski, yeni)) => {
                    sapma = true;
                    println!("sapma: {hedef} satır {n}\n  dosyada : {}\n  kanonda : {}", kisalt(&eski), kisalt(&yeni));
                }
            }
            continue;
        }
        // Hedefin satır sonu biçimi korunur.
        let icerik = if mevcut.contains("\r\n") { beklenen.replace('\n', "\r\n") } else { beklenen };
        let yazilacak = match &cikti {
            Some(d) => Path::new(d).join(Path::new(hedef).file_name().unwrap_or_default()),
            None => Path::new(hedef).to_path_buf(),
        };
        if let Err(e) = fs::write(&yazilacak, icerik) {
            eprintln!("hata: yazılamadı {}: {e}", yazilacak.display());
            return 3;
        }
        let durum = if fark.is_none() { "değişmedi" } else { "yazıldı" };
        println!("{durum}: {}", yazilacak.display());
    }
    if sapma { 1 } else { 0 }
}

#[cfg(test)]
mod testler {
    use super::*;

    fn kanon(govde: &str) -> String {
        format!("# başlık\n\nönce\n\n{BAS_ISARETI}\n```\n{govde}\n```\n{SON_ISARETI}\n\nsonra\n")
    }

    #[test]
    fn cekirdek_cit_icinden_cikar() {
        let c = cekirdek_cikar(&kanon("Sen Sokrates'sin.\nİkinci satır.")).unwrap();
        assert_eq!(c, "Sen Sokrates'sin.\nİkinci satır.");
    }

    #[test]
    fn isaret_eksikse_hata() {
        assert!(cekirdek_cikar("işaretsiz metin").is_err());
    }

    #[test]
    fn sinir_asimi_cikis_2() {
        let dizin = std::env::temp_dir().join(format!("karakter-turet-sinir-{}", std::process::id()));
        fs::create_dir_all(&dizin).unwrap();
        let k = dizin.join("x-ajani.md");
        let a = dizin.join("x.md");
        fs::write(&k, kanon(&"kelime ".repeat(1601))).unwrap();
        fs::write(&a, "---\nname: x\n---\n\neski\n").unwrap();
        let arg = |s: &std::path::PathBuf| s.to_string_lossy().into_owned();
        let argv = vec!["--kanon".into(), arg(&k), "--ajan".into(), arg(&a), "--denetle".into()];
        assert_eq!(kos(&argv), 2);
        // Sınır yükseltilince aşım kalkar, eski gövde yüzünden sapma (1) görülür.
        let mut argv2 = argv.clone();
        argv2.extend(["--sinir".into(), "2000".into()]);
        assert_eq!(kos(&argv2), 1);
        fs::remove_dir_all(&dizin).ok();
    }

    #[test]
    fn sapma_denetimi_ve_uretim() {
        let dizin = std::env::temp_dir().join(format!("karakter-turet-sapma-{}", std::process::id()));
        fs::create_dir_all(&dizin).unwrap();
        let k = dizin.join("x-ajani.md");
        let a = dizin.join("x.md");
        fs::write(&k, kanon("Sen X'sin.")).unwrap();
        fs::write(&a, "---\r\nname: x\r\n---\r\n\r\nÖnsöz kalır.\r\n\r\n<!-- kaynak: eski -->\r\neski gövde\r\n\r\n<!-- karakter-turet:sonsoz -->\r\n$ARGUMENTS ile başla.\r\n").unwrap();
        let arg = |s: &std::path::PathBuf| s.to_string_lossy().into_owned();
        let denet = vec!["--kanon".into(), arg(&k), "--ajan".into(), arg(&a), "--denetle".into()];
        assert_eq!(kos(&denet), 1, "eski gövde sapma sayılmalı");
        let yaz: Vec<String> = denet[..4].to_vec();
        assert_eq!(kos(&yaz), 0);
        let sonuc = fs::read_to_string(&a).unwrap();
        assert!(sonuc.starts_with("---\r\nname: x\r\n---\r\n\r\nÖnsöz kalır.\r\n\r\n<!-- bu gövde "));
        assert!(sonuc.ends_with("-->\r\nSen X'sin.\r\n\r\n<!-- karakter-turet:sonsoz -->\r\n$ARGUMENTS ile başla.\r\n"));
        assert_eq!(kos(&denet), 0, "üretimden sonra uyumlu olmalı");
        // Elle düzenleme sapma olarak yakalanır.
        fs::write(&a, sonuc.replace("Sen X'sin.", "Sen Y'sin.")).unwrap();
        assert_eq!(kos(&denet), 1);
        fs::remove_dir_all(&dizin).ok();
    }
}
