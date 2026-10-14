//! Uçtan uca CLI testleri (geçici dizinde kütük).

use std::path::PathBuf;
use std::process::Command;
use std::sync::atomic::{AtomicU32, Ordering};

static SAYAC: AtomicU32 = AtomicU32::new(0);

struct Kutuk(PathBuf);

impl Kutuk {
    fn yeni() -> Kutuk {
        let d = std::env::temp_dir().join(format!("durum-test-{}-{}", std::process::id(), SAYAC.fetch_add(1, Ordering::SeqCst)));
        std::fs::create_dir_all(&d).unwrap();
        Kutuk(d.join("durum-olay.jsonl"))
    }
    fn calistir(&self, args: &[&str]) -> (i32, String, String) {
        let mut tam: Vec<&str> = args.to_vec();
        let yol = self.0.to_str().unwrap().to_string();
        tam.extend(["--kutuk", &yol, "--ts", "2026-10-14T09:00:00Z"]);
        let o = Command::new(env!("CARGO_BIN_EXE_durum")).args(&tam).output().unwrap();
        (o.status.code().unwrap(), String::from_utf8(o.stdout).unwrap(), String::from_utf8(o.stderr).unwrap())
    }
    fn ok(&self, args: &[&str]) -> String {
        let (k, o, e) = self.calistir(args);
        assert_eq!(k, 0, "{args:?}: {e}");
        o
    }
}

impl Drop for Kutuk {
    fn drop(&mut self) {
        let _ = std::fs::remove_dir_all(self.0.parent().unwrap());
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
    assert_eq!(o, "DURUM sage (2026-10-14): 1 açık/işlemde\n#1 islemde S4 dersi -> Meditations 4. kitap PROBE\n");
    assert!(o.len() <= 1024);
    assert!(k.ok(&["listele", "--durum", "bayat"]).contains("\teski\t"));
    assert_eq!(k.calistir(&["al", "2"]).0, 1);
    assert_eq!(k.ok(&["oturum-basi", "--alan", "vega"]), "DURUM vega (2026-10-14): açık iş yok\n");
    k.ok(&["bayatla", "1"]);
    assert_eq!(k.ok(&["oturum-basi", "--alan", "sage"]), "DURUM sage (2026-10-14): açık iş yok\n");
}

#[test]
fn oturum_basi_boyut_siniri() {
    let k = Kutuk::yeni();
    for i in 0..60 {
        k.ok(&["ac", "--alan", "sage", "--is", &format!("is numara {i}"), "--sonraki", "uzun bir sonraki eylem metni"]);
    }
    let o = k.ok(&["oturum-basi", "--alan", "sage"]);
    assert!(o.len() <= 1024, "{}", o.len());
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

#[test]
fn bozuk_kutuk_cikis_1() {
    let k = Kutuk::yeni();
    std::fs::write(&k.0, "bozuk\n").unwrap();
    assert_eq!(k.calistir(&["listele"]).0, 1);
}
