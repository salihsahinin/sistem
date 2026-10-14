//! Fark testi: aynı rastgele adaylar Lean spec ikilisine (`jarvis/lean/.lake/build/bin/skillkapi`) ve Rust uygulamasına
//! verilir; her hüküm birebir aynı olmalı. Tohumlu üreteç (deterministik). Lean ikilisi derlenmemişse test atlanır
//! (önce: `cd jarvis/lean && lake build`).
use std::io::Write;
use std::path::PathBuf;
use std::process::{Command, Stdio};

const N: usize = 20_000;

/// xorshift64*: tohumlu, bağımlılıksız.
struct Uretec(u64);
impl Uretec {
    fn sonraki(&mut self) -> u64 {
        self.0 ^= self.0 >> 12;
        self.0 ^= self.0 << 25;
        self.0 ^= self.0 >> 27;
        self.0.wrapping_mul(0x2545_F491_4F6C_DD1D)
    }
    fn bit(&mut self) -> bool {
        self.sonraki() & 1 == 1
    }
}

const BOOL_ANAHTAR: [&str; 20] = [
    "kapsanmisTam", "kapsanmisKismi", "y1", "y2", "y3", "deltaBilinmiyor", "degerYeter", "salihEmri", "r", "i", "p",
    "rituel", "orkestrator", "yanEtkili", "f1", "f2", "f3", "f4", "f5", "turOzel",
];

fn lean_ikili() -> PathBuf {
    let kok = PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../../lean/.lake/build/bin");
    kok.join(if cfg!(windows) { "skillkapi.exe" } else { "skillkapi" })
}

#[test]
fn lean_ve_rust_ayni_hukmu_verir() {
    let ikili = lean_ikili();
    if !ikili.exists() {
        eprintln!("atlandı: Lean ikilisi yok ({})", ikili.display());
        return;
    }
    let mut u = Uretec(0x5EED_2026_1014);
    let mut kayitlar = Vec::with_capacity(N);
    for _ in 0..N {
        let mut s = String::new();
        for k in BOOL_ANAHTAR {
            // Geçen yolları da örneklemek için çoğu bayrak yüksek olasılıkla açık
            let acik = if k == "kapsanmisTam" || k == "p" { u.sonraki().is_multiple_of(8) } else { !u.sonraki().is_multiple_of(8) };
            if acik || u.bit() {
                s.push_str(&format!("{k}={}\n", if acik { 1 } else { 0 }));
            }
        }
        s.push_str(&format!("kW={}\nkTau={}\n", u.sonraki() % 6, u.sonraki() % 5));
        kayitlar.push(s);
    }
    let girdi = kayitlar.join("---\n");

    let mut cocuk = Command::new(&ikili).stdin(Stdio::piped()).stdout(Stdio::piped()).spawn().expect("Lean ikilisi");
    cocuk.stdin.take().unwrap().write_all(girdi.as_bytes()).unwrap();
    let cikti = cocuk.wait_with_output().unwrap();
    assert!(cikti.status.success(), "Lean ikilisi hata verdi");
    let lean: Vec<String> = String::from_utf8(cikti.stdout).unwrap().lines().map(str::to_owned).collect();
    assert_eq!(lean.len(), N, "Lean kayıt sayısı");

    let mut dagilim = std::collections::BTreeMap::new();
    for (k, (kayit, beklenen)) in kayitlar.iter().zip(&lean).enumerate() {
        let rust = skill_kapi::hukum(&skill_kapi::oku(kayit).unwrap()).kod();
        assert_eq!(&rust, beklenen, "kayıt {k} ayrıştı:\n{kayit}");
        *dagilim.entry(rust).or_insert(0usize) += 1;
    }
    // Örneklem her terminali kapsamalı; kapsamazsa fark testi o dalı denetlememiş olur
    for h in ["RET-0", "BEKLET", "ONAR-2", "ONAR-3"] {
        assert!(dagilim.contains_key(h), "{h} hiç örneklenmedi: {dagilim:?}");
    }
    assert!(dagilim.keys().any(|h| h.starts_with("ÜRET-")), "ÜRET hiç örneklenmedi: {dagilim:?}");
    eprintln!("{N} kayıt birebir aynı · dağılım {dagilim:?}");
}
