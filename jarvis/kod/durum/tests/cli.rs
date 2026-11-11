//! Uçtan uca CLI testleri (geçici dizinde kütük).

use std::path::PathBuf;
use std::process::Command;
use std::sync::atomic::{AtomicU32, Ordering};

static SAYAC: AtomicU32 = AtomicU32::new(0);

struct Kutuk(PathBuf);

impl Kutuk {
    /// Kütük `<geçici>/durum-test-N/ortak/durum-olay.jsonl`: repo kökü (teslim kaydı, graf, özet) test dizini olur.
    fn yeni() -> Kutuk {
        let d = std::env::temp_dir().join(format!("durum-test-{}-{}", std::process::id(), SAYAC.fetch_add(1, Ordering::SeqCst)));
        std::fs::create_dir_all(d.join("ortak")).unwrap();
        Kutuk(d.join("ortak").join("durum-olay.jsonl"))
    }
    fn kok(&self) -> PathBuf {
        self.0.parent().unwrap().parent().unwrap().to_path_buf()
    }
    fn komut(&self, args: &[&str]) -> Command {
        let mut c = Command::new(env!("CARGO_BIN_EXE_durum"));
        c.args(args).args(["--kutuk", self.0.to_str().unwrap(), "--ts", "2026-10-14T09:00:00Z"]);
        c
    }
    fn calistir(&self, args: &[&str]) -> (i32, String, String) {
        let o = self.komut(args).output().unwrap();
        (o.status.code().unwrap(), String::from_utf8(o.stdout).unwrap(), String::from_utf8(o.stderr).unwrap())
    }
    fn kilit(&self) -> PathBuf {
        self.0.with_file_name("durum-olay.jsonl.kilit")
    }
    /// Seans teslim girdisi (zorunlu alanlar tam) yazar, yolunu döner.
    fn girdi(&self, ad: &str, hedef: &str) -> String {
        let yol = self.kok().join(ad);
        let v = serde_json::json!({"hedef": hedef, "hedef_tutuldu": true, "ne_degisti": [], "kararlar": [], "adaylar": [],
            "sonraki_ilk_is": ["devam"], "yeniden_acma": "yok"});
        std::fs::write(&yol, v.to_string()).unwrap();
        yol.to_str().unwrap().to_string()
    }
    fn teslimler(&self, alan: &str) -> Vec<String> {
        let d = self.kok().join(alan).join("raporlar").join("seans");
        let mut v: Vec<String> = std::fs::read_dir(d).map(|r| r.map(|e| e.unwrap().file_name().to_string_lossy().into_owned()).collect()).unwrap_or_default();
        v.sort();
        v
    }
    fn ok(&self, args: &[&str]) -> String {
        let (k, o, e) = self.calistir(args);
        assert_eq!(k, 0, "{args:?}: {e}");
        o
    }
}

impl Drop for Kutuk {
    fn drop(&mut self) {
        let _ = std::fs::remove_dir_all(self.kok());
    }
}

fn sage_ac(k: &Kutuk) {
    k.ok(&["ac", "--alan", "sage", "--is", "S4 dersi", "--sonraki", "Meditations 4. kitap PROBE"]);
}

#[test]
fn tam_zincir_ve_kalan() {
    let k = Kutuk::yeni();
    sage_ac(&k);
    assert_eq!(k.ok(&["al", "1"]), "#1 islemde\n");
    let c = k.ok(&["bitir", "1", "--kanit", "abc123", "--kalan", "S5 dersi|Meditations 5. kitap PROBE"]);
    assert_eq!(c, "#1 tamam\n#2 acik sage\n");
    assert_eq!(k.ok(&["tuket", "1"]), "#1 tuketildi\n");
    let l = k.ok(&["listele", "--alan", "sage"]);
    assert_eq!(l, "#1\tsage\ttuketildi\tS4 dersi\tMeditations 4. kitap PROBE\n#2\tsage\tacik\tS5 dersi\tMeditations 5. kitap PROBE\n");
    let j = k.ok(&["listele", "--json", "--durum", "acik"]);
    let v: serde_json::Value = serde_json::from_str(&j).unwrap();
    assert_eq!(v[0]["id"], 2);
    assert_eq!(v[0]["girdi"][0], 1);
    // satır sayısı: ac, al, bitir, ac(kalan), tuket
    assert_eq!(std::fs::read_to_string(&k.0).unwrap().lines().count(), 5);
}

#[test]
fn gecersiz_gecis_cikis_1_ve_kutuk_degismez() {
    let k = Kutuk::yeni();
    sage_ac(&k);
    k.ok(&["al", "1"]);
    let once = std::fs::read_to_string(&k.0).unwrap();
    for args in [&["al", "1"][..], &["tuket", "1"], &["al", "99"], &["bitir", "2"]] {
        assert_eq!(k.calistir(args).0, 1, "{args:?}");
    }
    // geçersiz --kalan zinciri: bitir de yazılmamalı
    assert_eq!(k.calistir(&["bitir", "1", "--kalan", "ayraçsız"]).0, 2);
    assert_eq!(std::fs::read_to_string(&k.0).unwrap(), once);
}

#[test]
fn kullanim_hatasi_cikis_2() {
    let k = Kutuk::yeni();
    assert_eq!(k.calistir(&[]).0, 2);
    assert_eq!(k.calistir(&["yok"]).0, 2);
    assert_eq!(k.calistir(&["ac", "--alan", "sage"]).0, 2);
    assert_eq!(k.calistir(&["al"]).0, 2);
    assert_eq!(k.calistir(&["listele", "--durum", "x"]).0, 2);
    assert_eq!(k.calistir(&["oturum-basi"]).0, 2);
}

#[test]
fn bilinmeyen_alan_cikis_1() {
    let k = Kutuk::yeni();
    assert_eq!(k.calistir(&["ac", "--alan", "yok", "--is", "x", "--sonraki", "y"]).0, 1);
}

#[test]
fn bayat_hesabi_ve_oturum_basi() {
    let k = Kutuk::yeni();
    sage_ac(&k);
    k.ok(&["ac", "--alan", "sage", "--is", "eski", "--sonraki", "yap", "--son-gecerlilik", "2026-10-13"]);
    k.ok(&["ac", "--alan", "gard", "--is", "baska", "--sonraki", "x"]);
    k.ok(&["al", "1"]);
    let o = k.ok(&["oturum-basi", "--alan", "sage"]);
    // Karar 122 biçimi: başlıkta sıradaki sayısı, sonda graf pointer satırı.
    assert_eq!(
        o,
        "DURUM sage (2026-10-14): 1 açık/işlemde · sırada 0\n#1 islemde S4 dersi -> Meditations 4. kitap PROBE\nGRAF: ortak/akis-graf.json · d2 ortak/graf/akis-sage.d2\n"
    );
    assert!(o.len() <= 2048);
    assert!(k.ok(&["listele", "--durum", "bayat"]).contains("\teski\t"));
    assert_eq!(k.calistir(&["al", "2"]).0, 1);
    assert!(k.ok(&["oturum-basi", "--alan", "vega"]).starts_with("DURUM vega (2026-10-14): açık iş yok\n"));
    k.ok(&["bayatla", "1"]);
    assert!(k.ok(&["oturum-basi", "--alan", "sage"]).starts_with("DURUM sage (2026-10-14): açık iş yok\n"));
}

#[test]
fn oturum_basi_boyut_siniri() {
    let k = Kutuk::yeni();
    for i in 0..120 {
        k.ok(&["ac", "--alan", "sage", "--is", &format!("is numara {i}"), "--sonraki", "uzun bir sonraki eylem metni"]);
    }
    let o = k.ok(&["oturum-basi", "--alan", "sage"]);
    assert!(o.len() <= 2048, "{}", o.len());
    assert!(o.contains("... +"));
}

#[test]
fn determinizm() {
    let a = Kutuk::yeni();
    let b = Kutuk::yeni();
    for k in [&a, &b] {
        sage_ac(k);
        k.ok(&["ac", "--alan", "tart", "--is", "e", "--sonraki", "f", "--girdi", "1"]);
        k.ok(&["al", "2"]);
        k.ok(&["bitir", "2", "--kalan", "g|h"]);
    }
    assert_eq!(std::fs::read(&a.0).unwrap(), std::fs::read(&b.0).unwrap());
    for args in [&["listele"][..], &["listele", "--json"], &["oturum-basi", "--alan", "tart"]] {
        assert_eq!(a.ok(args), b.ok(args));
        assert_eq!(a.ok(args), a.ok(args));
    }
}

/// Denetim kalem 41: bozuk satır uyarıyla atlanır, sıra dışı id (worktree birleşmesi) hata değildir,
/// yeni id en büyük mevcut id + 1 olur.
#[test]
fn bozuk_satir_ve_sira_disi_id_calisir() {
    let k = Kutuk::yeni();
    let satir = |id: u64| format!(r#"{{"olay":"ac","id":{id},"ts":"2026-11-11T10:00:00Z","alan":"sage","is":"i{id}","sonraki_eylem":"s"}}"#);
    std::fs::write(&k.0, format!("bozuk\n{}\n{}\n", satir(10), satir(7))).unwrap();
    let (kod, cikti, hata) = k.calistir(&["listele"]);
    assert_eq!(kod, 0, "{hata}");
    assert!(hata.contains("satır 1"), "{hata}");
    assert!(cikti.contains("i7") && cikti.contains("i10"), "{cikti}");
    k.ok(&["ac", "--alan", "sage", "--is", "yeni", "--sonraki", "x"]);
    assert!(std::fs::read_to_string(&k.0).unwrap().contains(r#""id":11"#));
}

// --- Denetim 2026-11-10 (görev #17) düzeltmeleri ---

/// Madde 1: zaten kapanmış seansa ikinci `seans-kapat` reddedilir ve ilk teslim dosyası ezilmez.
#[test]
fn seans_kapat_reddedilirse_teslim_ezilmez() {
    let k = Kutuk::yeni();
    k.ok(&["seans-ac", "--alan", "sage", "--oturum", "s1"]);
    let g1 = k.girdi("g1.json", "ilk hedef");
    k.ok(&["seans-kapat", "--alan", "sage", "--oturum", "s1", "--girdi", &g1, "--etiket", "e"]);
    let teslim = k.kok().join("sage/raporlar/seans/seans-teslim-2026-10-14-e.json");
    let once = std::fs::read_to_string(&teslim).unwrap();
    let kutuk_once = std::fs::read_to_string(&k.0).unwrap();
    let g2 = k.girdi("g2.json", "ikinci hedef");
    assert_eq!(k.calistir(&["seans-kapat", "--alan", "sage", "--oturum", "s1", "--girdi", &g2, "--etiket", "e"]).0, 1);
    assert_eq!(std::fs::read_to_string(&teslim).unwrap(), once);
    assert_eq!(k.teslimler("sage"), vec!["seans-teslim-2026-10-14-e.json"]);
    assert_eq!(std::fs::read_to_string(&k.0).unwrap(), kutuk_once);
}

/// Madde 2: aynı gün etiketsiz ikinci kapanış sıra eki alır, birincinin kaydı korunur.
#[test]
fn seans_kapat_ayni_gun_sira_eki() {
    let k = Kutuk::yeni();
    let g = k.girdi("g.json", "hedef");
    for s in ["s1", "s2", "s3"] {
        k.ok(&["seans-ac", "--alan", "sage", "--oturum", s]);
        k.ok(&["seans-kapat", "--alan", "sage", "--oturum", s, "--girdi", &g]);
    }
    assert_eq!(
        k.teslimler("sage"),
        vec!["seans-teslim-2026-10-14-seans-2.json", "seans-teslim-2026-10-14-seans-3.json", "seans-teslim-2026-10-14-seans.json"]
    );
    let oku = |ad: &str| -> serde_json::Value {
        serde_json::from_str(&std::fs::read_to_string(k.kok().join("sage/raporlar/seans").join(ad)).unwrap()).unwrap()
    };
    assert_eq!(oku("seans-teslim-2026-10-14-seans.json")["oturum"], "s1");
    assert_eq!(oku("seans-teslim-2026-10-14-seans-2.json")["oturum"], "s2");
    assert_eq!(oku("seans-teslim-2026-10-14-seans-2.json")["etiket"], "seans-2");
    assert!(std::fs::read_to_string(&k.0).unwrap().contains("seans-teslim-2026-10-14-seans-3.json"));
}

/// Madde 3: `--alan` seansın alanıyla uyuşmazsa kullanım hatası (2); dosya ve kütük değişmez.
#[test]
fn seans_kapat_alan_uyusmazligi_cikis_2() {
    let k = Kutuk::yeni();
    k.ok(&["seans-ac", "--alan", "sage", "--oturum", "s1"]);
    let once = std::fs::read_to_string(&k.0).unwrap();
    let g = k.girdi("g.json", "hedef");
    let (kod, _, e) = k.calistir(&["seans-kapat", "--alan", "gard", "--oturum", "s1", "--girdi", &g]);
    assert_eq!(kod, 2, "{e}");
    assert!(k.teslimler("gard").is_empty() && k.teslimler("sage").is_empty());
    assert_eq!(std::fs::read_to_string(&k.0).unwrap(), once);
}

/// Madde 4: graf/özet yazımı geçici dosya + rename; üstüne yazım çalışır, geçici dosya kalmaz.
#[test]
fn dosya_yaz_atomik_gecici_kalmaz() {
    let k = Kutuk::yeni();
    sage_ac(&k);
    k.ok(&["graf"]);
    k.ok(&["ac", "--alan", "sage", "--is", "ikinci", "--sonraki", "x"]);
    k.ok(&["graf"]);
    k.ok(&["ozet"]);
    k.ok(&["ozet"]);
    let ortak = k.kok().join("ortak");
    let v: serde_json::Value = serde_json::from_str(&std::fs::read_to_string(ortak.join("akis-graf.json")).unwrap()).unwrap();
    assert!(v.to_string().contains("ikinci"));
    for d in [ortak.clone(), ortak.join("graf")] {
        for e in std::fs::read_dir(d).unwrap() {
            let ad = e.unwrap().file_name().to_string_lossy().into_owned();
            assert!(!ad.contains(".gecici-"), "geçici dosya kaldı: {ad}");
        }
    }
}

/// Madde 5a: eşzamanlı `ac` süreçleri aynı id'yi iki kez yazmaz; kütük okunur kalır, kilit silinir.
#[test]
fn eszamanli_ac_id_cakismaz() {
    let k = Kutuk::yeni();
    let cocuklar: Vec<_> = (0..8)
        .map(|i| k.komut(&["ac", "--alan", "sage", "--is", &format!("paralel {i}"), "--sonraki", "x"]).stdout(std::process::Stdio::piped()).stderr(std::process::Stdio::piped()).spawn().unwrap())
        .collect();
    for c in cocuklar {
        assert!(c.wait_with_output().unwrap().status.success());
    }
    let l = k.ok(&["listele", "--json"]);
    let v: serde_json::Value = serde_json::from_str(&l).unwrap();
    let mut idler: Vec<u64> = v.as_array().unwrap().iter().map(|x| x["id"].as_u64().unwrap()).collect();
    idler.sort();
    assert_eq!(idler, (1..=8).collect::<Vec<u64>>());
    assert!(!k.kilit().exists());
}

/// Madde 5b: kilit her çıkış yolunda silinir (başarı, geçersiz geçiş, kullanım hatası).
#[test]
fn kilit_her_cikista_silinir() {
    let k = Kutuk::yeni();
    sage_ac(&k);
    assert!(!k.kilit().exists());
    assert_eq!(k.calistir(&["tuket", "1"]).0, 1);
    assert!(!k.kilit().exists());
    assert_eq!(k.calistir(&["ac", "--alan", "sage"]).0, 2);
    assert!(!k.kilit().exists());
}

/// Madde 5c: taze yabancı kilit varsa ≈5 sn sonra açık hata; kütük yazılmaz, yabancı kilit silinmez.
#[test]
fn taze_kilit_zaman_asimi() {
    let k = Kutuk::yeni();
    std::fs::write(k.kilit(), "baska oturum").unwrap();
    let basla = std::time::Instant::now();
    let (kod, _, e) = k.calistir(&["ac", "--alan", "sage", "--is", "x", "--sonraki", "y"]);
    assert_eq!(kod, 1);
    assert!(e.contains("kilitli"), "{e}");
    assert!(basla.elapsed() >= std::time::Duration::from_secs(4));
    assert!(!k.0.exists());
    assert!(k.kilit().exists());
}

/// Madde 5d: 60 sn'den eski kilit bayat sayılıp devralınır.
#[test]
fn bayat_kilit_devralinir() {
    let k = Kutuk::yeni();
    let f = std::fs::File::create(k.kilit()).unwrap();
    f.set_modified(std::time::SystemTime::now() - std::time::Duration::from_secs(120)).unwrap();
    drop(f);
    assert_eq!(k.ok(&["ac", "--alan", "sage", "--is", "x", "--sonraki", "y"]), "#1 acik sage\n");
    assert!(!k.kilit().exists());
}

/// Madde 6: uzun (çok baytlı) hedef KONUM satırında karakter sınırında kırpılır; brif bayt tavanını aşmaz.
#[test]
fn oturum_basi_uzun_hedef_tavan() {
    let k = Kutuk::yeni();
    let hedef = "ş".repeat(3000);
    k.ok(&["seans-ac", "--alan", "sage", "--oturum", "s1", "--hedef", &hedef]);
    for i in 0..40 {
        k.ok(&["ac", "--alan", "sage", "--is", &format!("is {i}"), "--sonraki", "uzun bir sonraki eylem metni"]);
    }
    let o = k.ok(&["oturum-basi", "--alan", "sage"]);
    assert!(o.len() <= 2048, "{}", o.len());
    let konum = o.lines().next().unwrap();
    assert!(konum.starts_with("KONUM sage: seans s1 (AÇIK; hedef: şş"));
    assert!(konum.contains("…"));
}

/// Madde 7: `--help` ve `-h` kullanım metnini basar, çıkış 0.
#[test]
fn yardim_cikis_0() {
    for b in ["--help", "-h"] {
        let o = Command::new(env!("CARGO_BIN_EXE_durum")).arg(b).output().unwrap();
        assert_eq!(o.status.code(), Some(0), "{b}");
        assert!(String::from_utf8(o.stdout).unwrap().starts_with("kullanım: durum"));
    }
    let (kod, o, _) = Kutuk::yeni().calistir(&["ac", "--help"]);
    assert_eq!(kod, 0);
    assert!(o.starts_with("kullanım: durum"));
}
