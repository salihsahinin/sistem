//! `py::float_repr` fark testi: Python `repr(float)` ile bayt eşitliği (Karar 130 K46 birleşim kararının kanıtı).
//! Değerler deterministik üretilir (sabit tohumlu LCG + bilinen uç değerler); Python yoksa test atlanır.
use jarvis_ortak::py::float_repr;
use std::io::Write;
use std::process::{Command, Stdio};

fn degerler() -> Vec<f64> {
    let mut v = vec![0.0, -0.0, 1.0, 0.1, 0.5, 2.5, 1e16, 1e15, 9999999999999998.0, 1e-4, 1e-5, 0.0001234, 5e-324, f64::MAX, f64::MIN_POSITIVE, 123456789012345678.0, 1.5e300, -3.25];
    let mut s: u64 = 0x2026_1111;
    for _ in 0..20000 {
        s = s.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);
        let x = f64::from_bits(s);
        if x.is_finite() {
            v.push(x);
        }
        // kısa ondalıklı değerler (oran, yüzde gibi araç çıktıları)
        v.push(((s >> 20) % 1_000_000) as f64 / 1000.0);
        v.push(2f64.powi(((s >> 40) % 120) as i32 - 20) * (((s >> 8) % 1000) as f64));
    }
    v
}

#[test]
fn float_repr_python_ile_esit() {
    let v = degerler();
    let girdi: String = v.iter().map(|x| format!("{}\n", x.to_bits())).collect();
    let betik = "import sys,struct\nfor s in sys.stdin.read().split():\n print(repr(struct.unpack('<d', struct.pack('<Q', int(s)))[0]))";
    let Ok(mut c) = Command::new("python").args(["-I", "-c", betik]).stdin(Stdio::piped()).stdout(Stdio::piped()).spawn() else {
        eprintln!("python yok, test atlandı");
        return;
    };
    c.stdin.take().unwrap().write_all(girdi.as_bytes()).unwrap();
    let cikti = String::from_utf8(c.wait_with_output().unwrap().stdout).unwrap();
    let beklenen: Vec<&str> = cikti.lines().collect();
    assert_eq!(beklenen.len(), v.len());
    let farklar: Vec<String> = v.iter().zip(&beklenen).filter(|(x, b)| float_repr(**x) != **b).map(|(x, b)| format!("{:e}: rust={} python={b}", x, float_repr(*x))).collect();
    assert!(farklar.is_empty(), "{} fark: {:?}", farklar.len(), &farklar[..farklar.len().min(10)]);
}
