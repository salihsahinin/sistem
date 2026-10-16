//! Fark testleri: her ritüel aracı için eski betik (`tools/*.py`, Python) ile yeni ikili aynı girdide stdout · stderr · çıkış kodu ·
//! yazılan dosyalar (`veri/`, zaman damgaları hariç) bakımından eşit olmalı. Python yoksa test başarısız olur (atlanmaz).
//! Python'un yakalanmamış istisna (traceback) verdiği durumlar `.atla()` ile işaretlidir: stdout ve çıkış kodu eşit, stderr metni bilinçli farklı.
mod ortak;
use ortak::*;

fn say(ad: &str, n: usize) {
    println!("[fark] {ad}: {n} durum");
}

// ------------------------------------------------------------------ ortak: argparse davranışı (4 araç)
const ARACLAR: [Arac; 4] = [Arac::Acilis, Arac::Fifo, Arac::Ayna, Arac::Sayac];

#[test]
fn argparse_ortak() {
    let durumlar: Vec<Vec<&str>> = vec![
        vec!["-h"],
        vec!["--help"],
        vec!["--he"],
        vec!["--h"],
        vec!["-hx"],
        vec!["-h=x"],
        vec!["--help=1"],
        vec!["--dk", "x"],
        vec!["--esik", "x"],
        vec!["--esik", ""],
        vec!["--j2"],
        vec!["--r"],
        vec!["--k"],
        vec!["--kuru=1"],
        vec!["--json=x"],
        vec!["--repo"],
        vec!["--repo", "--json"],
        vec!["--tarih"],
        vec!["--anahtar"],
        vec!["--anahtar", "-x"],
        vec!["--is"],
        vec!["--i", "x"],
        vec!["a", "b"],
        vec!["--"],
        vec!["--", "a"],
        vec!["--repo", "--", "x"],
        vec!["-"],
        vec!["-x"],
        vec!["-5"],
        vec!["--foo", "--bar=1", "baz"],
        vec!["--dk", "1", "--help"],
        vec!["--help", "--dk", "x"],
        vec!["--dk", "x", "--help"],
        vec!["--dosya", "a", "--esik", "1_0", "--foo"],
        vec!["--d", "a"],
        vec!["--s", "a"],
        vec!["--e", "5", "--e"],
        vec!["--esik", "-5", "--dosya"],
        vec!["--json", "--json"],
        vec!["--kutuk=", "x"],
        vec!["--repo=", "--json"],
        vec!["--esik=0x10"],
        vec!["--esik", " 7 "],
        vec!["--esik", "٣"],
    ];
    for arac in ARACLAR {
        let mut adimlar: Vec<Adim> = durumlar.iter().map(|a| adim(a)).collect();
        adimlar.push(adim(&["--repo", "-a b"]).atla());
        let n = fark(arac, &format!("arg-{arac:?}"), adimlar);
        say(&format!("argparse {arac:?}"), n);
    }
}

#[test]
fn yardim_genislikleri() {
    for arac in ARACLAR {
        let mut adimlar = vec![];
        for c in ["20", "30", "40", "50", "60", "70", "79", "80", "100", "200", "0", "-5", "abc", "1_0", "12", ""] {
            adimlar.push(adim(&["-h"]).env("COLUMNS", c));
            adimlar.push(adim(&["--yok"]).env("COLUMNS", c));
        }
        let n = fark(arac, &format!("yg-{arac:?}"), adimlar);
        say(&format!("yardim genislikleri {arac:?}"), n);
    }
}

// ------------------------------------------------------------------ sicak-katman-fifo
fn maddeler(n: usize, uzun: usize) -> String {
    (0..n).map(|i| format!("- **Madde {i} başlığı** {}\n", "ğüşiöçı ".repeat(uzun))).collect()
}

#[test]
fn fifo() {
    let kap = |govde: &str| format!("# Kapsül\n**Güncelleme:** 2026-10-16 ~9:05\n\n## Şu an\n{govde}\n## Sonraki\n- x\n");
    let uzun_satir = format!("- **Uzun madde** {}\n", "ç".repeat(200));
    let pano = |satirlar: &str| format!("# Pano\n\n## AKTİF\n{satirlar}\n## KAPALI\n| K-9 | eski |\n");
    let mem_satir = |i: usize| format!("- [Hafıza {i}](dosya-{i}.md) — özet {i}\n");
    let mem_user = "- [Kullanıcı](user-salih.md) — kimlik\n";
    let mem20: String = (0..20).map(mem_satir).collect::<String>() + mem_user;
    let mem_buyuk: String = (0..16).map(|i| format!("- [Hafıza {i}](dosya-{i}.md) — {}\n", "x".repeat(400))).collect();
    let adimlar = vec![
        adim(&[]),
        adim(&["--json"]),
        adim(&["--tarih", "2026-10-16"]),
        adim(&["--json", "--tarih", "a{t}b{x}"]),
        // kapsül: madde sigortası (K=8) aşımı
        adim(&[]).dosya("core/durum-kapsulu.md", &kap(&maddeler(12, 3))),
        adim(&["--json", "--tarih", "2026-01-02"]),
        // kapsül: bayt tavanı (8 KB)
        adim(&["--tarih", "2026-01-02"]).dosya("core/durum-kapsulu.md", &kap(&maddeler(6, 120))),
        adim(&["--json"]),
        // kapsül: satır tavanı (40)
        adim(&[]).dosya("core/durum-kapsulu.md", &kap(&"- kısa madde\n".repeat(3)).replace("\n\n## Sonraki", &format!("\n{}\n## Sonraki", "açıklama satırı\n".repeat(50)))),
        // NFD başlık
        adim(&[]).dosya("core/durum-kapsulu.md", "# K\n## S\u{327}u an\n- **a b c** d\n- e\n"),
        adim(&["--json"]).dosya("core/durum-kapsulu.md", "# K\n## S\u{327}u an\n"),
        // başlık yok / dosya sonunda / iki bölüm / CRLF
        adim(&[]).dosya("core/durum-kapsulu.md", "# K\n- x\n"),
        adim(&[]).dosya("core/durum-kapsulu.md", "## Şu an\n- a\n- b"),
        adim(&[]).dosya("core/durum-kapsulu.md", "## Şu an"),
        adim(&[]).dosya("core/durum-kapsulu.md", "## Şu an \n- a\n"),
        adim(&[]).dosya("core/durum-kapsulu.md", "## Şu an\n- a\n## Şu an\n- b\n- c\n"),
        adim(&["--json"]).dosya("core/durum-kapsulu.md", "## Şu an\r\n- a\r\n- b\r\n## X\r\n"),
        adim(&[]).dosya("core/durum-kapsulu.md", "## Şu an\n- a\r- b\n- c\u{2028}- d\n- e\u{b}- f\u{85}- g\u{1c}- h\n"),
        adim(&["--json"]).dosya("core/durum-kapsulu.md", "## Şu an\n- **\u{2028}uzun başlık** x\n- ****\n- **ab**\n- **abc**\n- ** x **\n- **a**b**c**\n"),
        adim(&[]).dosya("core/durum-kapsulu.md", &kap(&uzun_satir.repeat(10))),
        adim(&["--json"]).dosya("core/durum-kapsulu.md", &kap(&"- düz madde başı çok uzun sadece başlıksız\n".repeat(9))),
        adim(&[]).dosya("core/durum-kapsulu.md", &kap("- | - : başı\n- :: iki nokta ::\n- --- tire\n")),
        adim(&[]).dosya("core/durum-kapsulu.md", &kap(&(maddeler(8, 1) + "- **Eski:başlık:** x\n- düz metin sonu iki nokta:\n- -| ::: boş başlık\n"))),
        adim(&["--json"]),
        // pano
        adim(&[]).dosya("core/pano.md", &pano(&"| K-1 | **Karar** | açık |\n".repeat(7))),
        adim(&["--json"]).dosya("core/pano.md", &pano(&format!("| K-1 | {} |\n| K-2 | iş |\n", "z".repeat(13000)))),
        adim(&[]).dosya("core/pano.md", "# P\n## AKTI\u{307}F\n| K-1 | a |\n| K-2 | b |\n| K-3 | c |\n| K-4 | d |\n| K-5 | e |\n| K-6 | f |\n"),
        adim(&[]).dosya("core/pano.md", "## AKTİF\n| X-1 | a |\n| K-1 | b |\n"),
        // MEMORY: kök anahtarı
        adim(&[]).dosya("@ev/.claude/projects/{KA}/memory/MEMORY.md", &mem20),
        adim(&["--json"]),
        adim(&[]).dosya("@ev/.claude/projects/{KA}/memory/MEMORY.md", &mem_buyuk),
        // MEMORY: yalnız jarvis anahtarı (kök anahtarı yoksa ikincisine düşer)
        adim(&[])
            .sil("@ev/.claude/projects/{KA}")
            .dosya("@ev/.claude/projects/{JA}/memory/MEMORY.md", &mem20),
        adim(&["--json"]).sil("@ev/.claude/projects/{JA}"),
        adim(&[]).dosya("@ev/.claude/projects/{KA}/memory/MEMORY.md", "- [a](user-x.md) k\n- [b](c.md) d\n"),
        // AGENTS.md
        adim(&[]).dosya("AGENTS.md", &"- kural satırı\n".repeat(90)),
        adim(&["--json"]).dosya("AGENTS.md", &format!("{}\n", "ü".repeat(8000))),
        adim(&[]).dosya("AGENTS.md", ""),
        adim(&[]).dosya("AGENTS.md", "tek satır, sonu yok"),
        adim(&[]).ikili("AGENTS.md", &[0x66, 0xff, 0xfe, 0x0a]).atla(),
        adim(&[]).dosya("AGENTS.md", "temiz\n"),
        // --repo biçimleri
        adim(&["--repo", "."]),
        adim(&["--repo", "..", "--json"]),
        adim(&["--repo", "{R}/"]),
        adim(&["--repo", "{R}/../jarvis", "--json"]),
        adim(&["--repo", "{K}/yok"]),
        adim(&["--repo", "core"]),
        adim(&["--repo", "{R}\\core\\.."]),
        adim(&["--repo", ""]),
        adim(&["--repo", "{R}", "--repo", "."]),
        adim(&["--repo={R}", "--tarih=2026-02-03"]),
        adim(&["--rep", "{R}", "--tar", "2027-01-01", "--js"]),
        // dosya dizin olduğunda
        adim(&[]).sil("core/pano.md").hazir(|k| std::fs::create_dir_all(k.jarvis.join("core").join("pano.md")).unwrap()).atla(),
    ];
    let n = fark(Arac::Fifo, "fifo", adimlar);
    say("sicak-katman-fifo", n);
}

// ------------------------------------------------------------------ hafiza-ayna
const E0: i64 = 1788100000;

#[test]
fn ayna() {
    let m = |ad: &str| format!("@ev/.claude/projects/{{KA}}/memory/{ad}");
    let mj = |ad: &str| format!("@ev/.claude/projects/{{JA}}/memory/{ad}");
    let ayna_m = "veri/hafiza-ayna/-Users-HasanSalihSahin-sistem/MANIFEST.json";
    let buyuk = "b".repeat(200_000);
    let adimlar = vec![
        adim(&[]),
        adim(&["--json"]),
        adim(&["--kuru"]),
        // ilk kopya
        adim(&[])
            .dosya(&m("a.md"), "birinci\n")
            .dosya(&m("b.md"), "ikinci ğüş\n")
            .dosya(&m("ünicode ç.md"), "u\n")
            .dosya(&m(".gizli"), "g\n")
            .dosya(&m("alt/x.md"), "alt\n")
            .dosya(&m("bos.md"), "")
            .dosya(&m("buyuk.bin"), &buyuk)
            .ikili(&m("ikili.dat"), &[0, 1, 2, 255, 254, 0])
            .mtime(&m("a.md"), E0)
            .mtime(&m("b.md"), E0 + 1)
            .mtime(&m("ünicode ç.md"), E0 + 2)
            .mtime(&m("bos.md"), E0 + 3)
            .mtime(&m("buyuk.bin"), E0 + 4)
            .mtime(&m("ikili.dat"), E0 + 5),
        adim(&[]),
        adim(&["--json"]),
        adim(&["--kuru"]),
        // değişen dosya
        adim(&[]).dosya(&m("a.md"), "birinci değişti\n").mtime(&m("a.md"), E0 + 100),
        adim(&["--kuru", "--json"]).dosya(&m("a.md"), "yine\n").mtime(&m("a.md"), E0 + 101),
        adim(&[]).mtime(&m("a.md"), E0 + 101),
        // kaynakta silinen
        adim(&[]).sil(&m("b.md")),
        adim(&["--json"]),
        adim(&[]),
        adim(&["--kuru"]),
        // geri gelen
        adim(&[]).dosya(&m("b.md"), "geri\n").mtime(&m("b.md"), E0 + 200),
        adim(&[]).sil(&m("a.md")).sil(&m("bos.md")),
        adim(&["--json"]),
        // ek anahtarlar
        adim(&["--anahtar={JA}"]),
        adim(&["--anahtar={JA}", "--json"]).dosya(&mj("j1.md"), "jarvis\n").mtime(&mj("j1.md"), E0 + 300),
        adim(&["--anahtar={JA}"]),
        adim(&["--anahtar={KA}"]),
        adim(&["--anahtar={KA}", "--anahtar={JA}", "--kuru"]),
        adim(&["--anahtar={JA}", "--anahtar={KA}"]),
        adim(&["--anahtar", "{JA}"]),
        adim(&["--anahtar", "-x"]),
        adim(&["--anahtar=-x"]),
        adim(&["--anahtar=-x", "--anahtar={KA}"]),
        adim(&["--anahtar="]),
        adim(&["--anahtar=a/b"]),
        adim(&["--anahtar=çğ", "--json"]),
        adim(&["--anah", "{KA}", "--ku"]),
        // bozuk / alışılmadık manifest
        adim(&[]).dosya(ayna_m, "{bozuk json"),
        adim(&[]).dosya(ayna_m, "{\"dosyalar\": [{\"sha256\": \"x\"}]}"),
        adim(&["--json"]).dosya(ayna_m, "{\"dosyalar\": []}"),
        adim(&[]).dosya(ayna_m, "{\"dosyalar\": [{\"ad\": \"eski.md\", \"sha256\": \"zz\", \"bayt\": 3, \"kaynak_mtime\": \"t\", \"durum\": \"ayna\", \"ekstra\": [1, {\"a\": null}]}]}"),
        adim(&["--json"]),
        adim(&[]).dosya(ayna_m, "{\"dosyalar\": [{\"ad\": \"eski.md\", \"kaynakta_yok_tespit\": \"2020-01-01\", \"z\": 1}, {\"ad\": \"b.md\", \"sha256\": \"yanlış\"}]}"),
        adim(&[]).dosya(ayna_m, "{\"baska\": 1}"),
        adim(&[]).dosya(ayna_m, "\u{feff}{\"dosyalar\": []}"),
        adim(&[]).dosya(ayna_m, "[]").atla(),
        adim(&[]).dosya(ayna_m, "{\"dosyalar\": 5}").atla(),
        adim(&[]).dosya(ayna_m, "{\"dosyalar\": [5]}").atla(),
        adim(&[]).dosya(ayna_m, "{\"dosyalar\": []}"),
        // --repo biçimleri
        adim(&["--repo", "."]),
        adim(&["--repo", "{R}/"]),
        adim(&["--repo", "{R}/veri/.."]),
        adim(&["--repo", "--json"]),
        // kaynak dizini yoksa
        adim(&[]).sil("@ev/.claude/projects/{KA}"),
        adim(&["--json"]),
    ];
    let n = fark(Arac::Ayna, "ayna", adimlar);
    say("hafiza-ayna", n);
}

// ------------------------------------------------------------------ kural-sayaci
fn zengin() -> String {
    [
        "# Başlık",
        "Düz anlatı satırı.",
        "- madde bir",
        "* yıldız madde",
        "1. numaralı madde",
        "2) paren madde",
        "• nokta madde",
        "\t- sekmeli madde",
        "   - girintili madde",
        "**Kalın başlı satır** devam",
        "  **girintili kalın** x",
        "**",
        "****",
        "*italik* satır",
        "YASAK bir şey",
        "Zorunlu olan",
        "ZORUNLU",
        "yalnız küçük",
        "YALNIZ BÜYÜK",
        "Yalnız baş",
        "yalnİz noktalı",
        "yalnız",
        "asla bunu yapma",
        "ASLA",
        "her şey için",
        "Her biri",
        "herkes değil",
        "her_x değil",
        "≤ 5 ve ≥ 3",
        "m.12 ve md.3",
        "M.5 büyük",
        "m.٣ arap rakamı",
        "Katman-1 ve Katman-2",
        "Katman-3 değil",
        "KURAL ve Kural ve kural",
        "| tablo | satır |",
        "|---|---|",
        "```kod",
        "düz kod satırı yasak",
        "```",
        "## alt başlık her",
        "####### yedi diyez her şey",
        "###### altı diyez her",
        "#etiket her",
        "",
        "   ",
    ]
    .join("\n")
        + &format!("\nuzun asla {}\n", "ç".repeat(100))
}

#[test]
fn sayac() {
    let iki_hook = "#!/bin/bash\necho x\nexit 3\n";
    let adimlar = vec![
        adim(&[]),
        adim(&["--json"]),
        adim(&[]).dosya("CLAUDE.md", &zengin()),
        adim(&["--json"]),
        adim(&["--esik", "5"]),
        adim(&["--esik", "0", "--json"]),
        adim(&["--esik", "-3"]),
        adim(&["--esik", "1_00"]),
        adim(&["--esik", "+7"]),
        adim(&["--esik=26"]),
        adim(&["--esik", "27"]),
        // dosya seçimi
        adim(&["--dosya", "A.md", "B.md"]).dosya("A.md", "- a\n- b\n").dosya("B.md", "düz\nher\n"),
        adim(&["--dosya"]),
        adim(&["--dosya", "CLAUDE.md", "--dosya", "A.md", "--json"]),
        adim(&["--dosya", "CLAUDE.md", "A.md", "B.md", "--esik", "3"]),
        adim(&["--dosya", "yok.md"]),
        adim(&["--dosya", "A.md", "yok.md", "yok2.md"]),
        adim(&["--dosya", "core"]),
        adim(&["--skill", "s1"]).dosya(".claude/skills/s1/SKILL.md", "- skill kuralı\nYASAK\n"),
        adim(&["--skill", "s1", "s2", "--json"]).dosya(".claude/skills/s2/SKILL.md", "**kalın**\n"),
        adim(&["--skill", "yok"]),
        adim(&["--skill"]),
        adim(&["--dosya", "A.md", "--skill", "s1", "s2"]),
        // kütük
        adim(&["--kutuk"]),
        adim(&["--kutuk", "--json"]),
        adim(&["--kutuk", "--dosya", "CLAUDE.md", "A.md", "--skill", "s1", "--esik", "2"]),
        adim(&["--kutuk", "--dosya"]),
        adim(&["--dosya", "yok.md", "--kutuk"]),
        adim(&["--kutuk"]).sil("veri").atla(),
        adim(&["--kutuk"]).hazir(|k| std::fs::create_dir_all(k.jarvis.join("veri")).unwrap()),
        // hook
        adim(&[]).dosya(".claude/hooks/session-start.sh", iki_hook),
        adim(&["--json"]).dosya(".claude/hooks/session-start.sh", &format!("#!/bin/bash\necho {}\n", "ç".repeat(5000))),
        adim(&[]).dosya(".claude/hooks/session-start.sh", "#!/bin/bash\n"),
        adim(&[]).dosya(".claude/hooks/session-start.sh", "#!/bin/bash\necho hata >&2\nexit 1\n"),
        adim(&[]).sil(".claude/hooks/session-start.sh"),
        adim(&["--json"]),
        adim(&[]).hazir(|k| std::fs::create_dir_all(k.jarvis.join(".claude").join("hooks").join("session-start.sh")).unwrap()),
        adim(&[]).sil(".claude/hooks/session-start.sh").dosya(".claude/hooks/session-start.sh", "#!/bin/bash\npwd\n"),
        // dosya biçimleri
        adim(&["--dosya", "crlf.md", "--json"]).dosya("crlf.md", "- a\r\n- b\r\nher\r\n"),
        adim(&["--dosya", "cr.md"]).dosya("cr.md", "- a\r- b\rher"),
        adim(&["--dosya", "bos.md", "--json"]).dosya("bos.md", ""),
        adim(&["--dosya", "sonsuz.md"]).dosya("sonsuz.md", "- sonu yok"),
        adim(&["--dosya", "ikili.md"]).ikili("ikili.md", &[0x2d, 0x20, 0xff, 0xfe, 0x0a]).atla(),
        adim(&["--dosya", "bom.md"]).ikili("bom.md", "\u{feff}- madde\n".as_bytes()),
        adim(&["--dosya", "çok uzun dosya adı kırk beş karakteri kesinlikle aşacak şekilde yazılmış.md"])
            .dosya("çok uzun dosya adı kırk beş karakteri kesinlikle aşacak şekilde yazılmış.md", "- a\n"),
        adim(&["--dosya", "alt/dizin/x.md", "--json"]).dosya("alt/dizin/x.md", "her\n"),
        // yol biçimleri
        adim(&["--repo", "..", "--dosya", "jarvis/CLAUDE.md"]),
        adim(&["--repo", "{K}", "--dosya", "jarvis/CLAUDE.md", "KOK.md", "--json"]),
        adim(&["--repo", ".", "--dosya", "../KOK.md"]),
        adim(&["--dosya", "{K}/KOK.md"]),
        adim(&["--repo", "{R}/", "--dosya", "./CLAUDE.md"]),
        adim(&["--repo", "{K}/friday", "--dosya", "notlar.md"]),
        adim(&["--repo", "{K}/dis", "--dosya", "x.md"]).hazir(|k| {
            ortak::yaz(&k.kok.join("dis").join("x.md"), "- dış\n".as_bytes());
        }),
        adim(&["--repo", "{K}/yok", "--dosya", "x.md"]),
        adim(&["--repo", "{R}", "--dosya", "CLAUDE.md"]).kokte(),
        adim(&[]).kokte(),
    ];
    let n = fark(Arac::Sayac, "sayac", adimlar);
    say("kural-sayaci", n);
}

// ------------------------------------------------------------------ acilis-kapilari
// Commit yaşları dakika cinsinden olduğundan her grup dakikanın ilk saniyelerine hizalanır; commit tarihleri 60'ın katıdır
// (yaş yalnız bir sonraki dakika başında değişir).
const KAPSUL_ESKI: &str = "# K\n**Güncelleme:** 2026-01-01 ~1:00\n\n## Şu an\n- x\n";

fn kapsul(satir: &str) -> String {
    format!("# K\n{satir}\n\n## Şu an\n- x\n")
}

/// Epoch'u `+hh` ofsetli yerel saat olarak `**Güncelleme:** YYYY-MM-DD ~H:MM` metnine çevirir.
fn damga(epoch: i64, ofset_saat: i64) -> String {
    let t = chrono::DateTime::from_timestamp(epoch + ofset_saat * 3600, 0).unwrap();
    format!("**Güncelleme:** {} ~{}", t.format("%Y-%m-%d"), t.format("%-H:%M"))
}

#[test]
fn acilis_commit_yasi_ve_kapsul() {
    let m = dakika_basi();
    let adimlar = vec![
        adim(&[]),
        adim(&["--json"]),
        adim(&[]).hazir(move |k| {
            isle(k, "x1.txt", "a\n", "feat: x1", m - 180);
            isle(k, "core/durum-kapsulu.md", KAPSUL_ESKI, "kapsül", m - 120);
        }),
        adim(&["--json"]),
        adim(&["--dk", "1"]),
        adim(&["--dk", "2"]),
        adim(&["--dk", "3"]),
        adim(&["--dk", "0"]),
        adim(&["--dk", "-1"]),
        adim(&["--dk", "1_5"]),
        adim(&["--dk", " 5 "]),
        adim(&["--dk", "99999999999999999999"]),
        adim(&["--dk", "3", "--json"]),
        // kapsül bildirimi çeşitleri (çalışma ağacı değişikliği)
        adim(&[]).dosya("core/durum-kapsulu.md", &kapsul("**Güncelleme:** 2099-12-31 ~23:59")),
        adim(&["--json"]),
        adim(&[]).dosya("core/durum-kapsulu.md", &kapsul("**Güncelleme:** 2026-10-16 ~25:61")),
        adim(&[]).dosya("core/durum-kapsulu.md", &kapsul("**Güncelleme:** 2026-10-16 ~9:5")),
        adim(&[]).dosya("core/durum-kapsulu.md", &kapsul("**Güncelleme:** 2026-02-30 10:00")),
        adim(&["--json"]).dosya("core/durum-kapsulu.md", &kapsul("**Güncelleme:**2026-01-01~09:05")),
        adim(&[]).dosya("core/durum-kapsulu.md", &kapsul("**Güncelleme:** 2026-01-01 9:05 sonra **Güncelleme:** 2099-01-01 1:00")),
        adim(&[]).dosya("core/durum-kapsulu.md", &kapsul("**Güncelleme:** 2026-01-01   ~ 9:05")),
        adim(&[]).dosya("core/durum-kapsulu.md", &kapsul("**Güncelleme:** 2026-01-01 009:05")),
        adim(&[]).dosya("core/durum-kapsulu.md", &kapsul("**Güncelleme:** 2026-01-01 10:055")),
        adim(&[]).dosya("core/durum-kapsulu.md", "# K\r\n**Güncelleme:** 2026-01-01 ~1:00\r\n"),
        adim(&[]).ikili("core/durum-kapsulu.md", &[0x2a, 0x2a, 0xff, 0x0a]),
        adim(&["--json"]).sil("core/durum-kapsulu.md"),
        // kapsül, commit'ten saat dilimi farkıyla: yerel (kendi ofsetli) duvar saati karşılaştırılır
        adim(&[]).dosya("core/durum-kapsulu.md", &kapsul(&damga(m - 7200, 3))).hazir(move |k| {
            git(k, &["add", "jarvis/core/durum-kapsulu.md"], None);
            let y = k.jarvis.join("tz.txt");
            yaz(&y, b"tz\n");
            git(k, &["add", "jarvis/tz.txt"], None);
            git_tarihli(&k.kok, &["commit", "-q", "-m", "ofset eksi beş"], Some(&format!("{} -0500", m - 60)));
        }),
        adim(&["--json"]),
        adim(&[]).dosya("core/durum-kapsulu.md", &kapsul(&damga(m - 60, 3))),
        adim(&[]).dosya("core/durum-kapsulu.md", &kapsul(&damga(m - 60, -5))),
        adim(&[]).dosya("core/durum-kapsulu.md", &kapsul(&damga(m + 3600, -5))),
    ];
    let n = fark(Arac::Acilis, "ac-a", adimlar);
    say("acilis-kapilari commit yasi/kapsul", n);
}

fn transkript(k: &Kum, dizin: &str, ad: &str, epoch: i64) {
    let y = k.ev.join(".claude").join("projects").join(dizin).join(ad);
    yaz(&y, b"{}\n");
    mtime(&y, epoch);
}

#[test]
fn acilis_transkript_dal_worktree() {
    let m = dakika_basi();
    let ja = |k: &Kum| k.jarvis_anahtar();
    let adimlar = vec![
        adim(&[]).hazir(move |k| isle(k, "x1.txt", "a\n", "feat: x1", m - 180)),
        // transkriptler
        adim(&[]).hazir(move |k| transkript(k, &ja(k), "a.jsonl", m - 300)),
        adim(&["--json"]),
        adim(&["--dk", "1"]),
        adim(&["--dk", "4"]),
        adim(&["--dk", "10"]),
        adim(&[]).hazir(move |k| transkript(k, &format!("{}-wt", ja(k)), "b.jsonl", m - 200)),
        adim(&["--json"]),
        adim(&["--dk", "1"]),
        adim(&["--dk", "3"]),
        adim(&[]).hazir(move |k| transkript(k, &k.kok_anahtar(), "c.jsonl", m - 100)),
        adim(&[]).hazir(move |k| {
            transkript(k, &ja(k), "eski.jsonl", m - 7200);
            transkript(k, &ja(k), "x.jsonl.bak", m - 100);
            transkript(k, &ja(k), ".gizli.jsonl", m - 100);
            std::fs::create_dir_all(k.ev.join(".claude").join("projects").join(ja(k)).join("dizin.jsonl")).unwrap();
        }),
        adim(&["--json"]).hazir(move |k| {
            let d = ja(k).to_uppercase();
            transkript(k, &d, "BUYUK.JSONL", m - 100);
        }),
        adim(&[]).sil("@ev/.claude"),
        adim(&[]).sil("@ev"),
        // dallar
        adim(&[]).hazir(move |k| {
            for d in ["feat/a", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "feat/main", "fooHEAD"] {
                git(k, &["branch", d], None);
            }
            git(k, &["branch", "eski", "main~2"], None);
        }),
        adim(&["--json"]),
        adim(&[]).hazir(move |k| {
            git(k, &["update-ref", "refs/remotes/origin/uz", "HEAD"], None);
            git(k, &["update-ref", "refs/remotes/origin/main", "HEAD"], None);
            git(k, &["symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/main"], None);
        }),
        adim(&["--json"]).hazir(move |k| {
            for d in ["feat/a", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "feat/main", "fooHEAD"] {
                git(k, &["branch", "-D", d], None);
            }
        }),
        // worktree'ler
        adim(&[]).hazir(move |k| {
            git(k, &["worktree", "add", "-q", "-b", "yan1", &ileri(&k.kok.join("wt1")), "main~1"], None);
        }),
        adim(&["--json"]),
        adim(&[]).dosya("@kok/wt1/.claude/settings.json", "{\"CLAUDE_PROJECT_DIR\": 1}"),
        adim(&[]).dosya("@kok/wt1/.claude/settings.json", "{}"),
        adim(&[]).hazir(move |k| {
            git(k, &["worktree", "add", "-q", "-b", "yan2", &ileri(&k.kok.join("wt2")), "main"], None);
        }),
        adim(&["--json"]).dosya("@kok/wt2/.claude/settings.json", "{}"),
        adim(&[]).hazir(move |k| {
            git(k, &["worktree", "add", "-q", "--detach", &ileri(&k.kok.join("wt3")), "main~2"], None);
        }),
        adim(&[]).ikili("@kok/wt1/.claude/settings.json", &[0xff, 0xfe]),
        adim(&["--json"]).sil("@kok/wt2"),
        adim(&[]).hazir(move |k| {
            isle(k, "y.txt", "y\n", "feat: y", m - 60);
        }),
        adim(&["--json"]),
    ];
    let n = fark(Arac::Acilis, "ac-b", adimlar);
    say("acilis-kapilari transkript/dal/worktree", n);
}

fn sqlite(k: &Kum, satirlar: &[(Option<&str>, Option<&str>)]) {
    let y = k.jarvis.join("veri").join("baglam.sqlite");
    let _ = std::fs::remove_file(&y);
    let c = rusqlite::Connection::open(&y).unwrap();
    c.execute("CREATE TABLE uretim (git_head_sha TEXT, uretim_zamani TEXT)", []).unwrap();
    for (a, b) in satirlar {
        c.execute("INSERT INTO uretim VALUES (?1, ?2)", rusqlite::params![a, b]).unwrap();
    }
}

#[test]
fn acilis_manifest_ve_silver() {
    let m = dakika_basi();
    let govde = |s: &str| format!("# Manifest\nDurum: {s}\n");
    let dolgu = |n: usize, s: &str| format!("{}{s}\n", "x".repeat(n));
    let adimlar = vec![
        adim(&[]).hazir(move |k| isle(k, "x1.txt", "a\n", "feat: x1", m - 180)),
        // K2 --is
        adim(&["--is", "a"]),
        adim(&["--is", "araştırma", "--json"]),
        adim(&["--is", "ARAŞTIRMA"]),
        adim(&["--is", "İŞ"]),
        adim(&["--is", "zzzz"]),
        adim(&["--is", ""]),
        adim(&["--is", " "]),
        adim(&["--is", "sahada"]),
        adim(&["--is", "ikinci"]),
        adim(&["--is", "İKİNCİ"]),
        adim(&["--is", "jarvis dosyaları", "--json"]),
        adim(&["--is", "ilk:"]),
        adim(&["--is", "x1"]),
        adim(&["--is", "'"]),
        adim(&[]).hazir(move |k| {
            for i in 0..7 {
                yaz(&k.jarvis.join("cc/pipeline").join(format!("pipeline-o{i}.md")), b"ortak konu\n");
                isle(k, &format!("o{i}.txt"), "o\n", &format!("ortak {i}"), m - 120 + i as i64);
            }
        }),
        adim(&["--is", "ortak"]),
        adim(&["--is", "ortak", "--json"]),
        // K2 açık görünenler
        adim(&[])
            .dosya("cc/pipeline/pipeline-01.md", &govde("açık"))
            .dosya("cc/pipeline/pipeline-02.md", &govde("AÇIK"))
            .dosya("cc/pipeline/pipeline-03.md", &govde("yarım kaldı"))
            .dosya("cc/pipeline/pipeline-04.md", &govde("YARIM"))
            .dosya("cc/pipeline/pipeline-05.md", &govde("koşuyor"))
            .dosya("cc/pipeline/pipeline-06.md", &govde("KOŞUYOR"))
            .dosya("cc/pipeline/pipeline-07.md", &govde("Sahada."))
            .sil("cc/pipeline/pipeline-o0.md")
            .sil("cc/pipeline/pipeline-o1.md")
            .sil("cc/pipeline/pipeline-o2.md")
            .sil("cc/pipeline/pipeline-o3.md")
            .sil("cc/pipeline/pipeline-o4.md")
            .sil("cc/pipeline/pipeline-o5.md")
            .sil("cc/pipeline/pipeline-o6.md"),
        adim(&["--json"]),
        adim(&[])
            .sil("cc/pipeline/pipeline-01.md")
            .sil("cc/pipeline/pipeline-02.md")
            .sil("cc/pipeline/pipeline-03.md")
            .sil("cc/pipeline/pipeline-04.md")
            .sil("cc/pipeline/pipeline-05.md")
            .sil("cc/pipeline/pipeline-06.md")
            .sil("cc/pipeline/pipeline-07.md")
            .dosya("cc/pipeline/pipeline-08.md", &govde("açıklama"))
            .dosya("cc/pipeline/pipeline-09.md", &govde("_SAHADA"))
            .dosya("cc/pipeline/pipeline-10.md", &govde("xSAHADA"))
            .dosya("cc/pipeline/pipeline-11.md", &govde("SAHADA_"))
            .dosya("cc/pipeline/pipeline-12.md", &govde("SAHADAx")),
        adim(&["--json"]),
        adim(&[])
            .dosya("cc/pipeline/pipeline-13.md", &govde("ışık-AÇIK"))
            .dosya("cc/pipeline/pipeline-14.md", &dolgu(1500, "SAHADA"))
            .dosya("cc/pipeline/pipeline-15.md", &dolgu(1495, "SAHADA"))
            .dosya("cc/pipeline/pipeline-16.md", &dolgu(1494, "AÇIK"))
            .dosya("cc/pipeline/pipeline-17.md", &dolgu(1497, "AÇIK"))
            .ikili("cc/pipeline/pipeline-18.md", b"SAH\xffADA")
            .dosya("cc/pipeline/pipeline-19.md", &govde("AÇİK"))
            .dosya("cc/pipeline/pipeline-20.md", &govde("açıK ve yarıM"))
            .dosya("cc/pipeline/PIPELINE-21.md", &govde("SAHADA"))
            .dosya("cc/pipeline/pipeline-x.txt", &govde("SAHADA"))
            .dosya("cc/pipeline/pipeline-.md", &govde("SAHADA"))
            .dosya("cc/pipeline/xpipeline-1.md", &govde("SAHADA")),
        adim(&["--json"]),
        adim(&["--is", "sahada"]),
        adim(&["--is", "ışık"]),
        adim(&["--is", "SAH"]),
        adim(&["--is", "sah\u{fffd}ada"]),
        adim(&["--json"]).dosya("cc/pipeline/pipeline-22.md", "yarım\r\nSAHADA\r\n").sil("cc/pipeline/pipeline-18.md"),
        adim(&[]).hazir(|k| std::fs::create_dir_all(k.jarvis.join("cc").join("pipeline").join("pipeline-dizin.md")).unwrap()).atla(),
        adim(&["--is", "x"]).atla(),
        adim(&[]).sil("cc/pipeline/pipeline-dizin.md"),
        adim(&[]).sil("cc/pipeline"),
        adim(&["--is", "ortak"]).sil("cc"),
        // K3 silver
        adim(&[]),
        adim(&["--json"]).hazir(|k| {
            let h = git(k, &["rev-parse", "HEAD"], None);
            sqlite(k, &[(Some(h.trim()), Some("2026-10-16T10:00:00.123456"))]);
        }),
        adim(&[]),
        adim(&[]).hazir(|k| sqlite(k, &[(Some("deadbeefcafe0123"), Some("2026-10-16T10:00:00"))])),
        adim(&["--json"]),
        adim(&[]).hazir(|k| {
            let h = git(k, &["rev-parse", "HEAD"], None);
            sqlite(k, &[(Some("eski"), Some("2026-01-01")), (Some(h.trim()), Some("2026-10-01")), (Some("daha eski"), Some("2025-01-01"))]);
        }),
        adim(&[]).hazir(|k| sqlite(k, &[])),
        adim(&["--json"]),
        adim(&[]).hazir(|k| sqlite(k, &[(Some("çğüşiöçğüşiöçğ"), Some("ünicode zaman damgası uzun uzun"))])),
        adim(&[]).hazir(|k| {
            let y = k.jarvis.join("veri").join("baglam.sqlite");
            let _ = std::fs::remove_file(&y);
            let c = rusqlite::Connection::open(&y).unwrap();
            c.execute("CREATE TABLE baska (x TEXT)", []).unwrap();
        }),
        adim(&["--json"]),
        adim(&[]).ikili("veri/baglam.sqlite", b"bu bir sqlite dosyasi degil, sadece metin ama yeterince uzun olmali ki sayfa baslik okunabilsin ......................................"),
        adim(&["--json"]),
        adim(&[]).ikili("veri/baglam.sqlite", b""),
        adim(&[]).sil("veri/baglam.sqlite").hazir(|k| std::fs::create_dir_all(k.jarvis.join("veri").join("baglam.sqlite")).unwrap()),
        adim(&["--json"]).sil("veri/baglam.sqlite").hazir(|k| sqlite(k, &[(None, Some("2026-01-01"))])).atla(),
        adim(&["--json"]).hazir(|k| sqlite(k, &[(Some("abc"), None)])).atla(),
        adim(&[]).hazir(|k| {
            let y = k.jarvis.join("veri").join("baglam.sqlite");
            let _ = std::fs::remove_file(&y);
            let c = rusqlite::Connection::open(&y).unwrap();
            c.execute("CREATE TABLE uretim (git_head_sha INTEGER, uretim_zamani TEXT)", []).unwrap();
            c.execute("INSERT INTO uretim VALUES (12345678, 'z')", []).unwrap();
        })
        .atla(),
        adim(&[]).sil("veri/baglam.sqlite"),
    ];
    let n = fark(Arac::Acilis, "ac-c", adimlar);
    say("acilis-kapilari manifest/silver", n);
}

#[test]
fn acilis_konu_alan_ve_repo() {
    let m = dakika_basi();
    let ep = move |i: i64| m - 600 + i * 60;
    let adimlar = vec![
        adim(&[]).hazir(move |k| isle(k, "x1.txt", "a\n", "feat: x1", ep(0))),
        adim(&[]).hazir(move |k| isle(k, "x2.txt", "a\n", "bitti 'x'", ep(1))),
        adim(&["--json"]).hazir(move |k| isle(k, "x3.txt", "a\n", "a|b|c ve | daha", ep(2))),
        adim(&[]).hazir(move |k| isle(k, "x4.txt", "a\n", &"çok uzun konu satırı ".repeat(8), ep(3))),
        adim(&[]).hazir(move |k| {
            yaz(&k.yol("a/b/c.txt"), b"1\n");
            yaz(&k.yol("@kok/friday/f.txt"), b"2\n");
            yaz(&k.yol("@kok/KOK2.md"), b"3\n");
            git(k, &["add", "jarvis/a", "friday/f.txt", "KOK2.md"], None);
            git(k, &["commit", "-q", "-m", "üç alan"], Some(ep(4)));
        }),
        adim(&["--json"]).hazir(move |k| {
            git(k, &["commit", "-q", "--allow-empty", "-m", "boş commit"], Some(ep(5)));
        }),
        adim(&[]).hazir(move |k| isle(k, "çğ.txt", "1\n", "unicode yol", ep(6))),
        adim(&[]).hazir(move |k| {
            git(k, &["checkout", "-q", "-b", "yan"], None);
            isle(k, "yan.txt", "1\n", "yan dal", ep(7));
            git(k, &["checkout", "-q", "main"], None);
            git(k, &["merge", "-q", "--no-ff", "-m", "birleştirme", "yan"], Some(ep(8)));
        }),
        adim(&["--json"]),
        adim(&[]).hazir(move |k| isle(k, "x5.txt", "a\n", "sonu tırnak'", ep(9))),
        // --repo biçimleri
        adim(&["--repo", "{R}"]),
        adim(&["--repo", "{K}", "--json"]),
        adim(&["--repo", "{K}/friday"]),
        adim(&["--repo", ".."]),
        adim(&["--repo", "../jarvis"]),
        adim(&["--repo", "{R}/"]),
        adim(&["--repo", "core"]),
        adim(&["--repo", "~"]),
        adim(&["--repo", "~/alt"]).hazir(|k| std::fs::create_dir_all(k.ev.join("alt")).unwrap()),
        adim(&["--repo", "{K}/disk"]).hazir(|k| std::fs::create_dir_all(k.kok.join("disk")).unwrap()).env("GIT_CEILING_DIRECTORIES", "{K}"),
        adim(&["--repo", "{K}/yok"]).atla(),
        adim(&["--repo", "{K}/bos", "--json"]).hazir(|k| {
            std::fs::create_dir_all(k.kok.join("bos")).unwrap();
            git_dizin(&k.kok.join("bos"), &["init", "-q", "-b", "main"], None);
        }).env("GIT_CEILING_DIRECTORIES", "{K}"),
        adim(&["--repo", "{K}/bos"]).env("GIT_CEILING_DIRECTORIES", "{K}").atla(),
        adim(&["--repo", "{K}/bos", "--is", "x"]).env("GIT_CEILING_DIRECTORIES", "{K}").atla(),
        // satır sınırı karakteri içeren konu: Python `splitlines` bölünce satır `|` ile 3 alana ayrılamaz (ValueError)
        adim(&[]).hazir(move |k| isle(k, "x6.txt", "a\n", "bölücü\u{2028}konu", ep(9) + 30)).atla(),
        adim(&["--json"]).atla(),
    ];
    let n = fark(Arac::Acilis, "ac-d", adimlar);
    say("acilis-kapilari konu/alan/repo", n);
}
