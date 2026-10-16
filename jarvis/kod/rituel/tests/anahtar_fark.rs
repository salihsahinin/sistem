//! Fark testi: `harness_anahtar` kütüphane modülü ile `tools/harness_anahtar.py` aynı ortamda aynı değerleri üretmeli
//! (anahtar türetme, dizin seçimi, `__main__` özeti). Süreç ortamı bu dosyada tek testle ayarlanır (başka iş parçacığı ortamı okumaz).
mod ortak;
use jarvis_rituel::harness_anahtar as h;
use ortak::*;
use std::path::Path;
use std::process::Command;

fn py(k: &Kum, kod: &str, arg: &str) -> String {
    let tools = ileri(&k.jarvis.join("tools"));
    let program = format!("import sys; sys.path.insert(0, r'{tools}'); import harness_anahtar as h\n{kod}");
    let o = Command::new("python")
        .args(["-c", &program, arg])
        .env("PYTHONUTF8", "1")
        .env("USERPROFILE", &k.ev)
        .output()
        .expect("python başlatılamadı");
    assert!(o.status.success(), "python: {}", String::from_utf8_lossy(&o.stderr));
    String::from_utf8_lossy(&o.stdout).replace('\r', "")
}

fn ozet_py(k: &Kum) -> String {
    let o = Command::new("python")
        .arg(k.jarvis.join("tools").join("harness_anahtar.py"))
        .env("PYTHONUTF8", "1")
        .env("USERPROFILE", &k.ev)
        .output()
        .expect("python başlatılamadı");
    String::from_utf8_lossy(&o.stdout).replace('\r', "")
}

#[test]
fn anahtar_ve_dizinler() {
    let k = kum("anahtar", "eski");
    // SAFETY: bu test dosyasında tek test var; ortamı başka iş parçacığı eşzamanlı okumaz.
    unsafe {
        std::env::set_var("CLAUDE_PROJECT_DIR", &k.jarvis);
        std::env::set_var("USERPROFILE", &k.ev);
    }
    let mut durum = 0;
    // anahtar türetme: göreli/mutlak/Unicode/UNC yollar
    for yol in ["x", "..", ".", "a/b/../c", "a//b", "a/", "C:\\Users\\Ünal Ç\\x y", "//sunucu/paylasim/dizin", "\\\\?\\C:\\x", "", "a  b", "çğ", "a.b-c_d", "/mutlak/unix", "C:", "C:x", "C:/", "D:\\", "x\\..\\..\\y"] {
        assert_eq!(py(&k, "print(h.anahtar(sys.argv[1]))", yol).trim_end_matches('\n'), h::anahtar(yol), "anahtar({yol:?})");
        durum += 1;
    }
    // dizin durumları: hiçbiri / kök anahtarı / kök+memory / yalnız jarvis anahtarı+memory / ikisi
    let projeler = k.ev.join(".claude").join("projects");
    let ka = k.kok_anahtar();
    let ja = k.jarvis_anahtar();
    let durumlar: Vec<Box<dyn Fn()>> = vec![
        Box::new(|| {}),
        Box::new({
            let d = projeler.join(&ka);
            move || std::fs::create_dir_all(&d).unwrap()
        }),
        Box::new({
            let d = projeler.join(&ka).join("memory");
            move || std::fs::create_dir_all(&d).unwrap()
        }),
        Box::new({
            let d = projeler.join(&ka);
            move || std::fs::remove_dir_all(&d).unwrap()
        }),
        Box::new({
            let d = projeler.join(&ja).join("memory");
            move || std::fs::create_dir_all(&d).unwrap()
        }),
        Box::new({
            let d = projeler.join(&ka).join("memory");
            move || std::fs::create_dir_all(&d).unwrap()
        }),
        Box::new({
            let d = projeler.join(&ja);
            move || std::fs::remove_dir_all(&d).unwrap()
        }),
    ];
    for hazirla in durumlar {
        hazirla();
        let py_cikti = py(
            &k,
            "print(h.jarvis_anahtar()); print(h.kok_anahtar()); print(h.PROJELER); print(h.proje_dizin()); print(h.proje_dizin('x')); print(h.memory_dizin())",
            "",
        );
        let rs_cikti = [h::jarvis_anahtar(), h::kok_anahtar(), h::projeler(), h::proje_dizin(None), h::proje_dizin(Some("x")), h::memory_dizin()].join("\n") + "\n";
        assert_eq!(py_cikti, rs_cikti, "dizin durumu {durum}");
        assert_eq!(ozet_py(&k), h::ozet(), "ozet {durum}");
        durum += 2;
        let _ = Path::new("");
    }
    println!("[fark] harness_anahtar: {durum} durum");
    let _ = std::fs::remove_dir_all(&k.kok);
}
