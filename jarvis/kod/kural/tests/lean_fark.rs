//! Üç yönlü fark testi: Python = Rust = Lean hükmü. `derece`: 15 bayrak + pahalı sınıfı = 65.536 bileşimin tamamı (Lean ikilisi `derece`, Rust
//! `jarvis_kural::derece::hukum`, Python `derece.py` tek süreçte döngüyle). `tetik`: Python `tetik-denetim.py` ile Rust ikilisinin sert-kapı
//! hükmü (çıkış kodu) Lean `Kanon.SkillTetik.kapiO` ile 64 bileşimde karşılaştırılır; ayrıca Lean Kapı-S ikilisi bağlantı denetimi.
//! Lean ikilileri derlenmemişse test atlanır (önce: `cd jarvis/lean && lake build`).
mod ortak;
use jarvis_kural::derece;
use ortak::*;
use serde_json::Value;
use std::io::Write;
use std::path::PathBuf;
use std::process::{Command, Stdio};

fn lean_ikili(ad: &str) -> Option<PathBuf> {
    let y = gercek_kok().join("jarvis/lean/.lake/build/bin").join(if cfg!(windows) { format!("{ad}.exe") } else { ad.to_string() });
    if y.exists() {
        Some(y)
    } else {
        eprintln!("atlandı: Lean ikilisi yok ({}); önce `cd jarvis/lean && lake build`", y.display());
        None
    }
}

fn lean_calistir(ikili: &PathBuf, kayitlar: &[String]) -> Vec<String> {
    let mut c = Command::new(ikili).stdin(Stdio::piped()).stdout(Stdio::piped()).stderr(Stdio::piped()).spawn().expect("Lean ikilisi başlatılamadı");
    let mut si = c.stdin.take().unwrap();
    let girdi = kayitlar.join("---\n");
    let t = std::thread::spawn(move || si.write_all(girdi.as_bytes()).unwrap());
    let o = c.wait_with_output().unwrap();
    t.join().unwrap();
    assert!(o.status.success(), "Lean ikilisi hata verdi: {}", String::from_utf8_lossy(&o.stderr));
    let cikti: Vec<String> = String::from_utf8(o.stdout).unwrap().lines().map(str::to_owned).collect();
    assert_eq!(cikti.len(), kayitlar.len(), "Lean kayıt sayısı");
    cikti
}

const BAYRAKLAR: [&str; 15] = ["v1", "v2", "v3a", "v3b", "v3c", "v3d", "v4", "v5", "v6", "v7a", "v7b", "v7c", "v8", "v9", "v10"];

#[test]
fn derece_python_rust_lean() {
    let Some(lean) = lean_ikili("derece") else { return };
    let toplam = 1usize << 16;
    // Lean girdisi: her bileşim için tüm bayrak satırları açık/kapalı yazılır
    let kayitlar: Vec<String> = (0..toplam)
        .map(|m| {
            let mut s = String::new();
            for (i, b) in BAYRAKLAR.iter().enumerate() {
                s.push_str(&format!("{b}={}\n", (m >> i) & 1));
            }
            s.push_str(&format!("pahali={}\n", (m >> 15) & 1));
            s
        })
        .collect();
    let lean_c = lean_calistir(&lean, &kayitlar);
    // Python: modülü bir kez yükle, her bileşim için main() koştur (çıkış kodu SystemExit'ten)
    let k = kum("derece3", "eski");
    let betik = ileri(&k.jarvis.join(Arac::Derece.py()));
    let surucu = format!(
        r#"
import importlib.util, io, sys, contextlib
spec = importlib.util.spec_from_file_location("derece_mod", r"{betik}")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
B = {BAYRAKLAR:?}
for mask in range(1 << 16):
    sys.argv = ["derece.py", "--json"] + ["--" + b for i, b in enumerate(B) if (mask >> i) & 1] + (["--pahali-geri-alma"] if (mask >> 15) & 1 else [])
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            m.main()
        kod = 0
    except SystemExit as e:
        kod = e.code
    print(kod)
"#
    );
    let o = Command::new("python").args(["-c", &surucu]).env("PYTHONUTF8", "1").output().expect("python");
    assert!(o.status.success(), "python: {}", String::from_utf8_lossy(&o.stderr));
    let py_c: Vec<String> = String::from_utf8(o.stdout).unwrap().lines().map(str::to_owned).collect();
    assert_eq!(py_c.len(), toplam);
    let mut dagilim = std::collections::BTreeMap::new();
    for m in 0..toplam {
        let mut f = [false; 15];
        for (i, x) in f.iter_mut().enumerate() {
            *x = (m >> i) & 1 == 1;
        }
        let (_, _, rust) = derece::hukum(&f, (m >> 15) & 1 == 1);
        assert_eq!(py_c[m], rust.to_string(), "bileşim {m:#x}: Python ≠ Rust");
        assert_eq!(lean_c[m], rust.to_string(), "bileşim {m:#x}: Lean ≠ Rust");
        *dagilim.entry(rust).or_insert(0usize) += 1;
    }
    for kod in [0, 5, 10] {
        assert!(dagilim.contains_key(&kod), "çıkış kodu {kod} hiç örneklenmedi: {dagilim:?}");
    }
    println!("[fark] derece Python=Rust=Lean: {toplam} bileşim birebir aynı · dağılım {dagilim:?}");
    let _ = std::fs::remove_dir_all(&k.kok);
}

/// Bir emir dosyasında Kapı-Ö girdisinin gözlenebilir özellikleri (Python/Rust'ın görebildiği altı bit).
#[derive(Clone, Copy)]
struct Ozellik {
    skill_var: bool,
    alanlar_tam: bool,
    literal: bool,
    yan_etkili: bool,
    alt_ajan: bool,
    derece_ifadesi: bool,
}

fn emir_dosyasi(o: Ozellik) -> String {
    let skill = if !o.skill_var { "yok-skill" } else if o.yan_etkili { "ornek-yan" } else { "ornek-uretici" };
    let tetik = if o.derece_ifadesi { "gerekirse çağır; a değilse ÇAĞIRMA" } else { "a ise çağır; b ise ÇAĞIRMA" };
    let baglam = if o.alt_ajan { "alt-ajan içinden" } else { "ana-sıra" };
    let kayit = if o.alanlar_tam { "  kayit: kuyruk/kayit.md\n" } else { "" };
    format!(
        "## SKILL TETİKLERİ\n- skill: {skill}\n  tetik_kosulu: {tetik}\n  cagri_kipi: {}\n  girdi: yol\n  baglam: {baglam}\n  yan_etki_damgasi: salt-okur\n  done_yuklemi: dosya var\n  hata_yolu: retry ≤3, FAIL-LOUD\n  sira: 1\n{kayit}",
        if o.literal { "literal" } else { "ortuk" }
    )
}

fn lean_kapi_o(o: Ozellik) -> String {
    // Python'ın göremediği Lean girdileri sabit "temiz" değerde; yan-etki bilgisi skill yoksa bilinmez (Python yan_etkili=false sayar)
    let yan = o.yan_etkili && o.skill_var;
    format!(
        "kapi=O\nskillVar={}\ntetikDogru=1\ndereceIfadesi={}\nicIceDerinlik=0\ndalSayisi=0\nkip={}\nyanEtkili={}\ncagiran={}\ngirdiTam=1\ntetikAracCiktisindan=0\nceliskiTemiz=1\nalanlarTam={}\n",
        o.skill_var as u8,
        o.derece_ifadesi as u8,
        if o.literal { "literal" } else { "ortuk" },
        yan as u8,
        if o.alt_ajan { "altAjan" } else { "anaSira" },
        o.alanlar_tam as u8,
    )
}

#[test]
fn tetik_python_rust_lean() {
    let Some(lean) = lean_ikili("tetik") else { return };
    let k = kum("tetik3", "eski");
    yaz(&k.jarvis.join(".claude/skills/ornek-uretici/SKILL.md"), b"---\nname: ornek-uretici\n---\n");
    yaz(&k.jarvis.join(".claude/skills/ornek-yan/SKILL.md"), b"---\nname: ornek-yan\ndisable-model-invocation: true\n---\n");
    let ozellikler: Vec<Ozellik> = (0..64u32)
        .map(|m| Ozellik {
            skill_var: m & 1 == 1,
            alanlar_tam: m & 2 != 0,
            literal: m & 4 != 0,
            yan_etkili: m & 8 != 0,
            alt_ajan: m & 16 != 0,
            derece_ifadesi: m & 32 != 0,
        })
        .collect();
    let lean_c = lean_calistir(&lean, &ozellikler.iter().map(|&o| lean_kapi_o(o)).collect::<Vec<_>>());
    let mut dagilim = std::collections::BTreeMap::new();
    for (i, &o) in ozellikler.iter().enumerate() {
        yaz(&k.jarvis.join("emir.md"), emir_dosyasi(o).as_bytes());
        let e = calistir(Arac::Tetik, true, &k, &adim(&["emir.md", "--json"]));
        let y = calistir(Arac::Tetik, false, &k, &adim(&["emir.md", "--json"]));
        assert_eq!(norm(&e.out, &k), norm(&y.out, &k), "bileşim {i}: Python ≠ Rust (JSON)");
        assert_eq!(e.kod, y.kod, "bileşim {i}: Python ≠ Rust (çıkış kodu)");
        let gecti = e.kod == 0;
        let lean_h = lean_c[i].as_str();
        assert_eq!(gecti, lean_h == "cagir", "bileşim {i}: Python/Rust {} ama Lean {lean_h}", if gecti { "GEÇTİ" } else { "BLOKE" });
        // Lean'in ilk-isabet sınıfı, Python'ın düşen sert kapılarıyla tutarlı olmalı
        let v: Value = serde_json::from_str(&y.out).unwrap();
        let dustu = |id: &str| v["calls"][0]["gates"].as_array().unwrap().iter().any(|g| g["id"] == id && g["ok"] == false);
        match lean_h {
            "iste" => assert!(dustu("O2-alanlar"), "bileşim {i}: Lean iste, Python O2 düşmedi"),
            "anaSiraya" => assert!(!dustu("O2-alanlar") && (dustu("O4-TY-literal") || dustu("O4-TY-anasira")), "bileşim {i}: Lean anaSiraya, Python O4 düşmedi"),
            "atla" => assert!(!dustu("O2-alanlar") && !dustu("O4-TY-literal") && !dustu("O4-TY-anasira") && (dustu("O1-var") || dustu("O5-derece-yok")), "bileşim {i}: Lean atla, Python O1/O5 düşmedi"),
            _ => {}
        }
        *dagilim.entry(lean_h.to_string()).or_insert(0usize) += 1;
    }
    for h in ["iste", "anaSiraya", "atla", "cagir"] {
        assert!(dagilim.contains_key(h), "{h} hiç örneklenmedi: {dagilim:?}");
    }
    println!("[fark] tetik Python=Rust=Lean: 64 bileşim aynı hüküm · Lean dağılımı {dagilim:?}");

    // Bilinen ayrışmalar (iddia yok; rapora yazılır): Python/Rust'ın geçtiği, Lean'in düşürdüğü durumlar
    let temel = Ozellik { skill_var: true, alanlar_tam: true, literal: true, yan_etkili: false, alt_ajan: false, derece_ifadesi: false };
    let yasak = emir_dosyasi(temel).replace("cagri_kipi: literal", "cagri_kipi: yasak");
    let derin = emir_dosyasi(temel).replace("a ise çağır; b ise ÇAĞIRMA", "((( a ))) ise çağır; b ise ÇAĞIRMA");
    for (ad, icerik, lean_girdi) in [
        ("kip=yasak", yasak, lean_kapi_o(temel).replace("kip=literal", "kip=yasak")),
        ("iç içe derinlik 3", derin, lean_kapi_o(temel).replace("icIceDerinlik=0", "icIceDerinlik=3")),
    ] {
        yaz(&k.jarvis.join("emir.md"), icerik.as_bytes());
        let y = calistir(Arac::Tetik, false, &k, &adim(&["emir.md"]));
        let l = lean_calistir(&lean, &[lean_girdi]);
        println!("[ayrisma] tetik {ad}: Rust/Python çıkış {} · Lean {}", y.kod, l[0]);
    }

    // Kapı-S ikilisinin bağlantı denetimi (md §3-§4: düşen çağrı 3. denemede yüksek sesle başarısız olur)
    let mut kayitlar = vec![];
    let mut beklenen = vec![];
    for m in 0..16u32 {
        for deneme in 1..=4u32 {
            let (done, sema_var, sema_uyuyor, hata) = (m & 1 == 1, m & 2 != 0, m & 4 != 0, m & 8 != 0);
            kayitlar.push(format!("kapi=S\ndone={}\nsemaVar={}\nsemaUyuyor={}\nhataKanali={}\ndeneme={deneme}\n", done as u8, sema_var as u8, sema_uyuyor as u8, hata as u8));
            let gecer = done && (!sema_var || sema_uyuyor) && hata;
            beklenen.push(if gecer { "gecti" } else if deneme < 3 { "tekrar" } else { "failLoud" });
        }
    }
    assert_eq!(lean_calistir(&lean, &kayitlar), beklenen, "Lean Kapı-S çıktısı md kuralından saptı");
    let _ = std::fs::remove_dir_all(&k.kok);
}
