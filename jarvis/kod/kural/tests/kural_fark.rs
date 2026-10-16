//! Fark testleri (Karar 115: araç başına en çok ~40 durum; gerçek kullanım biçimleri ve eşik sınırları): eski Python betiği ile yeni ikili aynı girdide
//! stdout · stderr · çıkış kodu · yazılan dosyalar bakımından eşit olmalı. Python'un yakalanmamış istisna verdiği durumlar `.atla()` ile işaretlidir
//! (stdout ve çıkış kodu eşit, stderr metni bilinçli farklı). Lean ile üç yönlü karşılaştırma: `lean_fark.rs`.
mod ortak;
use chrono::{Duration, Utc};
use ortak::*;
use serde_json::{Value, json};

fn say(ad: &str, n: usize) {
    println!("[fark] {ad}: {n} durum");
}

// ------------------------------------------------------------------ derece
#[test]
fn derece() {
    let bayraklar = ["v1", "v2", "v3a", "v3b", "v3c", "v3d", "v4", "v5", "v6", "v7a", "v7b", "v7c", "v8", "v9", "v10"];
    let mut adimlar: Vec<Adim> = vec![adim(&[]), adim(&["--help"]), adim(&["--json"]), adim(&["--help", "--v1"]), adim(&["--bilinmeyen"]), adim(&["--pahali-geri-alma"])];
    // tek bayraklar (her biri tek başına eşik altı, v3a override)
    for b in bayraklar {
        adimlar.push(adim(&[&format!("--{b}")]));
    }
    // eşik sınırları: H=3 (gerekmez) · 4 (F1+F2) · 6 · 7 (tetik); pahalı sınıfta 3 / 4
    adimlar.push(adim(&["--v2"])); // 3
    adimlar.push(adim(&["--v1", "--v5"])); // 4
    adimlar.push(adim(&["--v1", "--v5", "--v6"])); // 6
    adimlar.push(adim(&["--v1", "--v2", "--v5"])); // 7
    adimlar.push(adim(&["--v2", "--pahali-geri-alma"])); // 3, eşik 4
    adimlar.push(adim(&["--v1", "--v5", "--pahali-geri-alma"])); // 4, eşik 4
    adimlar.push(adim(&["--v1", "--v5", "--v6", "--v8", "--v7c"])); // indirimli: 3
    adimlar.push(adim(&["--v8"])); // -2
    adimlar.push(adim(&["--v3a", "--v8", "--v7c"])); // override, H düşük
    adimlar.push(adim(&["--v3a", "--json"]));
    adimlar.push(adim(&["--v1", "--v2", "--v5", "--json", "--pahali-geri-alma"]));
    adimlar.push(adim(&["--v3d", "--v4", "--v9", "--v10", "--json"]));
    adimlar.push(adim(&["--v1", "--v1", "--json", "--json"]));
    adimlar.push(adim(&bayraklar.iter().map(|b| format!("--{b}")).collect::<Vec<_>>().iter().map(String::as_str).collect::<Vec<_>>()));
    adimlar.push(adim(&["--v1", "--v2", "--v3b", "--v3c", "--v6", "--v7a", "--pahali-geri-alma", "--json"]));
    let n = fark(Arac::Derece, "derece", adimlar);
    say("derece", n);
}

// ------------------------------------------------------------------ tetik-denetim
const SKILL_IYI: &str = "---\nname: ornek-uretici\ndescription: örnek\n---\n# Gövde\n";
const SKILL_YAN: &str = "---\nname: ornek-yan\ndisable-model-invocation: true\n---\n# Gövde\n";

struct C {
    skill: &'static str,
    tetik: &'static str,
    kip: &'static str,
    baglam: &'static str,
    damga: &'static str,
    done: &'static str,
    hata: &'static str,
    sira: &'static str,
}

fn iyi() -> C {
    C {
        skill: "ornek-uretici",
        tetik: "görev tipi=kod ise çağır; kod değilse ÇAĞIRMA",
        kip: "literal",
        baglam: "ana-sıra bağlamı",
        damga: "salt-okur",
        done: "çıktı dosyası var ∧ şema uyuyor",
        hata: "retry ≤3, sonra FAIL-LOUD",
        sira: "1. çağrı 2. kayıt",
    }
}

fn blok(c: &[C]) -> String {
    c.iter()
        .map(|c| {
            format!(
                "- skill: {}\n  tetik_kosulu: {}\n  cagri_kipi: {}\n  girdi: dosya yolu\n  baglam: {}\n  yan_etki_damgasi: {}\n  done_yuklemi: {}\n  hata_yolu: {}\n  sira: {}\n  kayit: kuyruk/kayit.md\n",
                c.skill, c.tetik, c.kip, c.baglam, c.damga, c.done, c.hata, c.sira
            )
        })
        .collect()
}

fn emir(b: &str) -> String {
    format!("# Görev emri\n\nmetin\n\n## SKILL TETİKLERİ\n{b}\n## SONRAKİ BÖLÜM\nx\n")
}

#[test]
fn tetik() {
    let e = |ad: &str, c: Vec<C>| (ad.to_string(), emir(&blok(&c)));
    let mut adimlar: Vec<Adim> = vec![];
    let ilk = adim(&[])
        .dosya(".claude/skills/ornek-uretici/SKILL.md", SKILL_IYI)
        .dosya(".claude/skills/ornek-yan/SKILL.md", SKILL_YAN)
        .dosya(".claude/skills/ornek-yan2/SKILL.md", "---\nname: x\ndisable-model-invocation: TRUE\n---\n")
        .dosya(".claude/skills/ornek-yan3/SKILL.md", "---\nname: x\ndisable-model-invocation: false\n---\n")
        .dosya(".claude/skills/.gizli/SKILL.md", SKILL_YAN)
        .dosya(".claude/skills/bozuk/SKILL.md", "---\nname: x\ndisable-model-invocation: true\n")
        .dosya(".claude/skills/dizin-ama-skill-yok/README.md", "x\n")
        .ikili(".claude/skills/ikili/SKILL.md", &[0x2d, 0x2d, 0x2d, 0xff, 0x0a]);
    adimlar.push(ilk);
    let mut dosyali = |ad: &str, govde: String, args: &[&str]| {
        let mut a: Vec<&str> = vec![ad];
        a.extend(args);
        adimlar.push(adim(&a).dosya(ad, &govde));
    };
    // yok / blok yok
    dosyali("e1.md", "# Görev\nmetin\n".into(), &[]);
    dosyali("e2.md", emir("yok\n").to_string(), &[]);
    dosyali("e3.md", emir("- yok\n"), &["--json"]);
    dosyali("e4.md", emir("  YOK  \n"), &[]);
    dosyali("e5.md", emir("Yok.\n"), &[]);
    dosyali("e6.md", emir("açıklama metni\n"), &["--json"]);
    // iyi çağrı
    dosyali("g1.md", emir(&blok(&[iyi()])), &[]);
    dosyali("g2.md", emir(&blok(&[iyi()])), &["--json"]);
    dosyali("g3.md", emir(&blok(&[iyi(), C { skill: "ornek-yan", kip: "literal", ..iyi() }, C { skill: "yok-skill", ..iyi() }])), &[]);
    // sert kapılar
    dosyali("s1.md", emir(&blok(&[C { skill: "yok-skill", ..iyi() }])), &[]);
    dosyali("s2.md", emir(&blok(&[iyi()]).replace("  sira: 1. çağrı 2. kayıt\n", "")), &["--json"]);
    dosyali("s3.md", emir(&blok(&[C { kip: "belki", ..iyi() }])), &[]);
    dosyali("s4.md", emir(&blok(&[C { kip: "yasak", ..iyi() }, C { kip: "Örtük", ..iyi() }, C { kip: "ÖRTÜK", ..iyi() }, C { kip: "LİTERAL", ..iyi() }])), &[]);
    dosyali("s5.md", emir(&blok(&[C { skill: "ornek-yan", kip: "ortuk", ..iyi() }])), &[]);
    dosyali("s6.md", emir(&blok(&[C { skill: "ornek-yan", baglam: "alt-ajan içinden", ..iyi() }])), &[]);
    dosyali("s7.md", emir(&blok(&[C { skill: "ornek-yan2", sira: "İŞÇİ üzerinde", ..iyi() }, C { skill: "ornek-yan3", kip: "ortuk", ..iyi() }])), &["--json"]);
    dosyali("s8.md", emir(&blok(&[C { tetik: "gerekirse çağır", ..iyi() }])), &[]);
    dosyali("s9.md", emir(&blok(&[C { tetik: "GEREKİRSE çağır ÇAĞIRMA", ..iyi() }, C { tetik: "isteğe bağlı çağır", ..iyi() }, C { tetik: "İSTEĞE BAĞLI", ..iyi() }])), &[]);
    dosyali("s10.md", emir(&blok(&[C { hata: "retry ≤4, FAIL-LOUD", ..iyi() }, C { hata: "FAIL-LOUD", ..iyi() }, C { hata: "retry<=3 fail loud", ..iyi() }])), &[]);
    dosyali("s11.md", emir(&blok(&[C { hata: "retry 3, sessiz düşüş yasak", ..iyi() }, C { hata: "retry ≤ 2 FAIL-LOUD", ..iyi() }, C { hata: "retry ≤٣ FAIL-LOUD", ..iyi() }])), &["--json"]);
    dosyali("s12.md", emir(&blok(&[C { done: "yeterince iyi", ..iyi() }, C { done: "başarılı olur", ..iyi() }, C { done: "MÜMKÜN OLDUĞUNCA", ..iyi() }])), &[]);
    // yumuşak kapılar
    dosyali("y1.md", emir(&blok(&[C { tetik: "((( a ))) ise ÇAĞIRMA", ..iyi() }])), &[]);
    dosyali("y2.md", emir(&blok(&[C { tetik: "eğer a ise eğer b ise eğer c ise → d ÇAĞIRMA", ..iyi() }])), &["--json"]);
    dosyali("y1b.md", emir(&blok(&[C { tetik: "(( a )) ise ÇAĞIRMA", ..iyi() }, C { tetik: "eğer a ise eğer b ÇAĞIRMA", ..iyi() }, C { tetik: "eğer a ise eğer b ise ÇAĞIRMA", ..iyi() }])), &[]);
    dosyali("y3.md", emir(&blok(&[C { tetik: "a ise çağır", damga: "YIKICI", ..iyi() }, C { damga: "Yıkıcı", ..iyi() }, C { damga: "", ..iyi() }])), &[]);
    // başlık biçimleri
    dosyali("b1.md", "##SKILL TETİKLERİ\n".to_string() + &blok(&[iyi()]), &[]);
    dosyali("b2.md", "## SKILL TETİKLERİ (açıklama)\n".to_string() + &blok(&[iyi()]) + "### alt başlık\n- skill: ornek-uretici\n", &[]);
    dosyali("b3.md", "## Skill Tetikleri\n".to_string() + &blok(&[iyi()]), &[]);
    dosyali("b4.md", "##\n\nSKILL TETİKLERİ\n".to_string() + &blok(&[iyi()]), &[]);
    dosyali("b5.md", emir(&blok(&[iyi()])).replace('\n', "\r\n"), &["--json"]);
    dosyali("b6.md", "\u{feff}".to_string() + &emir(&blok(&[iyi()])), &[]);
    dosyali("b7.md", emir(&blok(&[C { skill: "`ornek-uretici` (tip)", ..iyi() }, C { skill: "ornek-uretici#not", ..iyi() }])), &[]);
    dosyali("b8.md", emir(&(blok(&[iyi()]) + "  cagri_kipi: ortuk\n  tetik_kosulu:\n")), &[]);
    dosyali("b9.md", emir(&blok(&[C { skill: "gizli", ..iyi() }, C { skill: "bozuk", kip: "ortuk", ..iyi() }, C { skill: "dizin-ama-skill-yok", ..iyi() }])), &[]);
    // bayrak / yol biçimleri
    adimlar.push(adim(&[]));
    adimlar.push(adim(&["--json"]));
    adimlar.push(adim(&["yok-dosya.md"]).atla());
    adimlar.push(adim(&["g1.md", "--repo"]).atla());
    adimlar.push(adim(&["g1.md", "--repo", "{R}"]));
    adimlar.push(adim(&["--repo", "{R}", "g1.md"]).atla());
    adimlar.push(adim(&["g1.md", "--repo", "{K}"]));
    adimlar.push(adim(&["{R}/g1.md", "--json"]).kokte());
    adimlar.push(adim(&["ikili.md"]).ikili("ikili.md", &[0x23, 0x23, 0xff, 0xfe]).atla());
    adimlar.push(adim(&["ikili-skill.md"]).dosya("ikili-skill.md", &emir(&blok(&[C { skill: "ikili", ..iyi() }]))).atla());
    let _ = e;
    let n = fark(Arac::Tetik, "tetik", adimlar);
    say("tetik-denetim", n);
}

// ------------------------------------------------------------------ ad-esitligi-denetim
#[test]
fn ad_esitligi() {
    let hafiza = "@ev/.claude/projects/{KA}/memory/MEMORY.md";
    let adimlar = vec![
        adim(&[]),
        adim(&["--json"]),
        adim(&[]).dosya("CLAUDE.md", "# J\neski ad Carvis, şimdi Jarvis\n"),
        adim(&[]).dosya(".claude/hooks/session-start.sh", "#!/bin/bash\necho 'Carvis = Jarvis'\n").dosya(hafiza, "- Carvis → Jarvis\n"),
        adim(&["--json"]).dosya("@kok/friday/CLAUDE.md", "Carvis emekli\n").dosya(".claude/agents/a.md", "Carvis) eski ad\n").dosya(".claude/agents/b.md", "ajan b\n").dosya(".claude/agents/not.txt", "x\n"),
        // ESIT çeşitleri (re.I + ı/İ denkliği)
        adim(&[]).dosya("CLAUDE.md", "ESKİ ADI CARVİS\n"),
        adim(&[]).dosya("CLAUDE.md", "eski adı Carvis\n"),
        adim(&[]).dosya("CLAUDE.md", "JARVİS FRIDAY CARVIS\n"),
        adim(&[]).dosya("CLAUDE.md", "carvis  =  **jarvis\n"),
        adim(&[]).dosya("CLAUDE.md", "Carvis ≠ Jarvis\n"),
        adim(&[]).dosya("CLAUDE.md", "carvıs emekli\n"),
        adim(&[]).dosya("CLAUDE.md", "eski ad Carvis\n"),
        // K2: Carvis geçen dizinler ve README eşdeğerleri
        adim(&[]).dosya("wiki/a.md", "Carvis ile ilgili\n"),
        adim(&["--json"]).dosya("wiki/README.md", "Carvis = Jarvis\n"),
        adim(&[]).dosya("kuyruk/k.md", "Carvis eski\n").dosya("arsiv/z.txt", "CARVİS\n"),
        adim(&[]).dosya("core/c.md", "Carvis = Jarvis tamam\n"),
        adim(&[]).dosya("tools/t.py", "# Carvis\n").dosya("tools/SCRIPTLER.md", "Carvis emekli\n"),
        adim(&["--json"]).dosya("kaynak-kodu/README.md", "Carvis emekli\n").dosya(".claude/skills/x/SKILL.md", "Carvis\n"),
        adim(&[]).dosya("node_modules/p/i.md", "Carvis\n").dosya(".git/c.md", "Carvis\n").dosya(".gizli/d.md", "Carvis\n").dosya("veri/v.json", "{\"a\": \"Carvis\"}\n"),
        adim(&[]).dosya("__pycache__/x.md", "Carvis\n").dosya("ucuncu/alt/derin/x.html", "<p>CARVIS</p>\n"),
        adim(&[]).dosya("diger/x.bin", "Carvis\n"),
        // K3: canlı bağlamda bağlanmamış Carvis
        adim(&["--json"]).dosya("core/c.md", "Carvis kaldı burada\nnormal\nCarvis = Jarvis\n"),
        adim(&[]).dosya("core/alt/d.md", &format!("{}\nCARVİS büyük\n", "uzun ".repeat(40) + "Carvis")),
        adim(&[]).dosya("core/sozluk.md", "Carvis sözlük muaf\n").dosya("core/baglam-anahtar-kaydi.md", "Carvis muaf\n"),
        adim(&[]).dosya("tools/a.sh", "echo Carvis\n").dosya("wiki/w.json", "{\"x\": \"Carvis\"}\n").dosya("wiki/not.txt", "Carvis\n"),
        adim(&[]).dosya("KILAVUZ.md", "Carvis\n").dosya("README.md", "Carvis\n").dosya("fikir-kutusu.md", "Carvis = Jarvis\nCarvis\n"),
        adim(&[]).dosya(".claude/hooks/x.sh", "Carvis\n"),
        adim(&["--json"]).ikili("core/ikili.md", &[0x43, 0x61, 0xff, 0xfe, 0x0a]),
        adim(&[]).dosya("core/crlf.md", "Carvis satırı\r\nbaşka\r\nCarvis\r\n"),
        adim(&[]).dosya("core/crlf.md", "Carvis\u{2028}ikinci\u{85}Carvis\n"),
        adim(&[]).sil("core").sil("wiki").sil("tools/t.py").sil("tools/a.sh").sil("tools/SCRIPTLER.md").sil("kuyruk").sil("arsiv"),
        adim(&["--json"]),
    ];
    let n = fark(Arac::Ad, "ad", adimlar);
    say("ad-esitligi-denetim", n);
}

// ------------------------------------------------------------------ skill-esik
fn ago(saat: f64) -> String {
    let t = Utc::now() - Duration::microseconds((saat * 3.6e9) as i64);
    t.format("%Y-%m-%dT%H:%M:%S%.6f+00:00").to_string()
}

type Kosum = (String, String, Option<String>, Value, Value, Option<String>);

fn db(k: &Kum, satirlar: &[Kosum], tablo: bool) {
    let y = k.jarvis.join("veri").join("baglam.sqlite");
    let _ = std::fs::remove_file(&y);
    std::fs::create_dir_all(y.parent().unwrap()).unwrap();
    let c = rusqlite::Connection::open(&y).unwrap();
    if !tablo {
        c.execute("CREATE TABLE baska (x TEXT)", []).unwrap();
        return;
    }
    c.execute("CREATE TABLE amb_olgu_kosum (kosum_id, agent_type TEXT, modeller, output_tokens, sure_sn, valid_time_bas)", []).unwrap();
    for (kid, agent, model, tok, sure, ts) in satirlar {
        let v = |x: &Value| -> rusqlite::types::Value {
            match x {
                Value::Null => rusqlite::types::Value::Null,
                Value::Number(n) if n.is_i64() => rusqlite::types::Value::Integer(n.as_i64().unwrap()),
                Value::Number(n) => rusqlite::types::Value::Real(n.as_f64().unwrap()),
                Value::String(s) => rusqlite::types::Value::Text(s.clone()),
                _ => unreachable!(),
            }
        };
        c.execute(
            "INSERT INTO amb_olgu_kosum VALUES (?1, ?2, ?3, ?4, ?5, ?6)",
            rusqlite::params![kid, agent, model, v(tok), v(sure), ts],
        )
        .unwrap();
    }
}

/// n adet atlas koşumu: token `tok(i)`, süre `sure(i)`, zaman `ts(i)`.
fn atlas(n: usize, model: &str, tok: impl Fn(usize) -> Value, sure: impl Fn(usize) -> Value, ts: impl Fn(usize) -> Option<String>) -> Vec<Kosum> {
    (0..n).map(|i| (format!("k{i}"), "atlas".to_string(), Some(model.to_string()), tok(i), sure(i), ts(i))).collect()
}

#[test]
fn skill_esik() {
    let (t1, t23, t25, t47, t100) = (ago(1.0), ago(23.0), ago(25.0), ago(47.0), ago(100.0));
    let sabit = |n: usize, m: &str| atlas(n, m, |_| json!(1000), |_| json!(60), |_| Some(ago(200.0)));
    // 10 koşum: ilk 9 normal (1000 tok / 60 sn), sonuncu `x` tok
    let tepe = {
        let (t23, t25) = (t23.clone(), t25.clone());
        move |x: i64, ts_son: String| {
            let _ = (&t23, &t25);
            atlas(10, "m1", move |i| if i == 9 { json!(x) } else { json!(1000) }, |_| json!(60), {
                let ts_son = ts_son.clone();
                move |i| Some(if i == 9 { ts_son.clone() } else { ago(200.0) })
            })
        }
    };
    let ts_a = t23.clone();
    let ts_b = t25.clone();
    let adimlar = vec![
        adim(&[]).sil("veri"),
        adim(&["--json"]).atla(),
        adim(&[]).hazir(|k| db(k, &[], true)),
        adim(&[]).hazir(|k| db(k, &[], false)).atla(),
        adim(&[]).hazir(move |k| db(k, &atlas(3, "m1", |_| json!(10), |_| json!(1), |_| None), true)),
        adim(&["--esik-n", "3"]),
        adim(&["--esik-n", "4"]),
        adim(&["--esik-n", "0"]),
        adim(&["--esik-n", "-1"]),
        adim(&["--esik-n", "x"]),
        // n=10 sınırı: 9 koşum atlanır, 10 hesaplanır
        adim(&[]).hazir(move |k| db(k, &atlas(9, "m1", |_| json!(1000), |_| json!(60), |_| Some(ago(200.0))), true)),
        adim(&[]).hazir(move |k| db(k, &atlas(10, "m1", |_| json!(1000), |_| json!(60), |_| Some(ago(200.0))), true)),
        // tam 2x sınırı: > 2x değil → sapma yok; 2001 → sapma
        adim(&[]).hazir({
            let (tepe, ts) = (tepe.clone(), ts_a.clone());
            move |k| db(k, &tepe(2000, ts.clone()), true)
        }),
        adim(&[]).hazir({
            let (tepe, ts) = (tepe.clone(), ts_a.clone());
            move |k| db(k, &tepe(2001, ts.clone()), true)
        }),
        // pencere: 23 saat önce (içeride) · 25 saat önce (dışarıda)
        adim(&[]).hazir({
            let (tepe, ts) = (tepe.clone(), ts_b.clone());
            move |k| db(k, &tepe(5000, ts.clone()), true)
        }),
        adim(&["--saat", "48"]),
        adim(&["--saat", "1"]),
        adim(&["--saat", "0.5"]),
        adim(&["--saat", "0"]),
        adim(&["--saat", "-5"]),
        adim(&["--carpan", "1.5"]),
        adim(&["--carpan", "5"]),
        adim(&["--carpan", "5.0"]),
        adim(&["--carpan", "0"]),
        adim(&["--carpan", "1e1"]),
        adim(&["--saat", "nan"]).atla(),
        adim(&["--saat", "inf"]).atla(),
        adim(&["--saat", "1e12"]).atla(),
        adim(&["--carpan", "abc"]),
        // medyan: çift sayıda (ortalama), float token, süre yok
        adim(&[]).hazir(move |k| db(k, &atlas(10, "m1", |i| json!(1000 + i as i64), |i| json!(10 + i as i64), |_| Some(ago(200.0))), true)),
        adim(&[]).hazir(move |k| db(k, &atlas(10, "m1", |i| json!(1000.5 + i as f64), |i| json!(10.25 + i as f64), |_| Some(ago(200.0))), true)),
        adim(&[]).hazir({
            let t = t1.clone();
            move |k| db(k, &atlas(10, "m1", |i| if i == 0 { json!(99999.5) } else { json!(100) }, |_| json!(5), |i| Some(if i == 0 { t.clone() } else { ago(200.0) })), true)
        }),
        adim(&[]).hazir(move |k| db(k, &atlas(10, "m1", |_| json!(1000), |_| Value::Null, |_| None), true)).atla(),
        adim(&[]).hazir(move |k| db(k, &atlas(10, "m1", |_| Value::Null, |_| json!(5), |_| None), true)).atla(),
        adim(&[]).hazir(move |k| db(k, &atlas(10, "m1", |_| json!(0), |_| json!(0), |_| None), true)),
        // birden çok model + başka agent_type satırları
        adim(&[]).hazir({
            let t = t47.clone();
            move |k| {
                let mut s = sabit(10, "model-b");
                s.extend(sabit(10, "model-a"));
                s.extend(sabit(4, "model-c"));
                s.push(("x1".into(), "baska".into(), Some("model-a".into()), json!(1), json!(1), Some(t.clone())));
                db(k, &s, true)
            }
        }),
        adim(&[]).hazir(move |k| db(k, &atlas(10, "m", |_| json!(1), |_| json!(1), |_| Some(ago(200.0))).into_iter().map(|mut s| { s.2 = None; s }).collect::<Vec<_>>(), true)),
        adim(&[]).hazir(move |k| {
            let mut s = atlas(10, "m", |_| json!(1), |_| json!(1), |_| None);
            s.extend(atlas(10, "m", |_| json!(1), |_| json!(1), |_| None).into_iter().map(|mut x| { x.2 = None; x }));
            db(k, &s, true)
        }).atla(),
        adim(&["--repo", "{R}"]).hazir(move |k| db(k, &atlas(10, "m1", |_| json!(1000), |_| json!(60), |_| Some(ago(200.0))), true)),
        adim(&["--repo", ".."]),
        adim(&["--repo", "{K}/yok"]),
        adim(&["--repo"]),
        adim(&[]).ikili("veri/baglam.sqlite", b"bu sqlite degil ama yeterince uzun bir metin dosyasi, sayfa basligi okunabilsin diye ........................").atla(),
    ];
    let _ = (t100, t25);
    let n = fark(Arac::SkillEsik, "esik", adimlar);
    say("skill-esik", n);
}

// ------------------------------------------------------------------ paralel-kapi
fn man(id: &str, ek: Value) -> (String, String) {
    let mut m = json!({"birim_id": id, "tur": "pipeline", "pist": "a", "okur": [], "yazar": [], "granul": "dosya", "sira": [], "silver": "yok",
        "kanon_yuzeyi": false, "dis_etki": false, "zorlama_modu": "dosya"});
    for (k, v) in ek.as_object().unwrap() {
        m[k] = v.clone();
    }
    (format!("veri/manifest/{id}.json"), serde_json::to_string_pretty(&m).unwrap())
}

fn adim_man(args: &[&str], birimler: Vec<(String, String)>) -> Adim {
    let mut a = adim(args).sil("veri/manifest");
    for (yol, ic) in birimler {
        a = a.dosya(&yol, &ic);
    }
    a
}

#[test]
fn paralel() {
    let m = man;
    let temel = || vec![m("a", json!({"yazar": ["x/a.md"]})), m("b", json!({"yazar": ["x/b.md"]}))];
    let adimlar = vec![
        adim(&[]).sil("veri/manifest"),
        adim(&[]).sil("veri/manifest").atla(),
        adim_man(&[], vec![]),
        adim_man(&["--json"], vec![]),
        adim_man(&[], vec![m("tek", json!({"yazar": ["x.md"]}))]),
        adim_man(&[], temel()),
        adim_man(&["--json"], temel()),
        adim_man(&["--sessiz"], temel()),
        // Bernstein
        adim_man(&[], vec![m("a", json!({"yazar": ["x/a.md"]})), m("b", json!({"yazar": ["x/a.md"]}))]),
        adim_man(&["--json"], vec![m("a", json!({"yazar": ["x/a.md"]})), m("b", json!({"okur": ["x/a.md"]}))]),
        adim_man(&[], vec![m("a", json!({"okur": ["x/a.md"]})), m("b", json!({"okur": ["x/a.md"]}))]),
        adim_man(&[], vec![m("a", json!({"yazar": ["x/a.md"]})), m("b", json!({"yazar": ["x/a.md"], "sira": ["a"]}))]),
        adim_man(&[], vec![m("a", json!({"okur": ["x/a.md"]})), m("b", json!({"yazar": ["x/a.md"]}))]),
        adim_man(&[], vec![m("a", json!({"yazar": ["p1", "p2", "p3"]})), m("b", json!({"yazar": ["p1", "p2", "p3"]}))]),
        adim_man(&[], vec![m("a", json!({"yazar": ["p1", "p2", "p3", "p4"]})), m("b", json!({"yazar": ["p1", "p2", "p3", "p4"]}))]),
        // glob / snapshot / dış / bölüm
        adim_man(&[], vec![m("a", json!({"yazar": ["cc/rapor/*/r.md"]})), m("b", json!({"yazar": ["cc/rapor/z/r.md"]})), m("c", json!({"yazar": ["cc/baska/r.md"]}))]),
        adim_man(&[], vec![m("a", json!({"yazar": ["veri/"]})), m("b", json!({"okur": ["veri/x.json"]}))]),
        adim_man(&[], vec![m("a", json!({"yazar": ["x.md#b1"]})), m("b", json!({"yazar": ["x.md#b2"]})), m("c", json!({"yazar": ["x.md"]}))]),
        adim_man(&[], vec![m("a", json!({"yazar": ["x.md"]})), m("b", json!({"okur": ["git@abc123:x.md", "web", "stdin"]}))]),
        adim_man(&[], vec![m("a", json!({"yazar": ["Dizin/A.md"]})), m("b", json!({"yazar": ["dizin/a.md"]}))]),
        adim_man(&[], vec![m("a", json!({"yazar": ["f[ab].md"]})), m("b", json!({"yazar": ["fa.md"]})), m("c", json!({"yazar": ["f?.md"]}))]),
        // silver / kanon / dışlama / loop
        adim_man(&[], vec![m("a", json!({"silver": "yazar"})), m("b", json!({"silver": "yazar"}))]),
        adim_man(&[], vec![m("a", json!({"silver": "yazar"})), m("b", json!({"silver": "yazar", "sira": ["a"]}))]),
        adim_man(&[], vec![m("a", json!({"kanon_yuzeyi": true, "yazar": ["core/k.md"]})), m("b", json!({"yazar": ["y.md"]}))]),
        adim_man(&["--json"], vec![m("a", json!({"kanon_yuzeyi": true, "yazar": ["core/k.md"], "durum": "canli-diger-oturum"})), m("b", json!({"okur": ["core/k.md"]})), m("c", json!({"okur": ["z.md"]}))]),
        adim_man(&[], vec![m("a", json!({"dislama_grubu": "g1"})), m("b", json!({"dislama_grubu": "g1"})), m("c", json!({"dislama_grubu": "g2"}))]),
        adim_man(&[], vec![m("a", json!({"tur": "loop", "iterasyon_ayak_izi": "buyuyen", "durma_kosulu": "x"})), m("b", json!({"tur": "loop", "durma_kosulu": "y"}))]),
        // canlı / tamam
        adim_man(&[], vec![m("a", json!({"yazar": ["x.md"], "durum": "canli-diger-oturum"})), m("b", json!({"yazar": ["x.md"]})), m("c", json!({"yazar": ["w.md"]}))]),
        adim_man(&["--json"], vec![m("a", json!({"yazar": ["x.md"], "durum": "tamam"})), m("b", json!({"yazar": ["x.md"]})), m("c", json!({"yazar": ["x.md"], "durum": "kapandi-2"}))]),
        // dalgalar: sira zinciri, kademe, öncelik
        adim_man(&[], vec![m("a", json!({})), m("b", json!({"sira": ["a"]})), m("c", json!({"sira": ["b"]})), m("d", json!({}))]),
        adim_man(&["--kademe", "1"], vec![m("a", json!({})), m("b", json!({})), m("c", json!({})), m("d", json!({}))]),
        adim_man(&["--kademe", "2", "--json"], vec![m("a", json!({})), m("b", json!({})), m("c", json!({})), m("d", json!({}))]),
        adim_man(&["--kademe", "-1"], vec![m("a", json!({})), m("b", json!({}))]),
        adim_man(&[], vec![m("a", json!({"oncelik": 3})), m("b", json!({"oncelik": 1})), m("c", json!({"oncelik": 2.5})), m("d", json!({}))]),
        // uyarılar
        adim_man(&[], vec![m("a", json!({"tur": "bilinmez", "belirlenimsiz_girdi": ["model-çıktısı"], "dis_etki": true})), m("b", json!({"tur": "loop", "tur_ustyazim": "matris"}))]),
        // bütünlük hataları
        adim_man(&[], vec![m("a", json!({"sira": ["yok"]})), m("b", json!({"sira": ["c"]})), m("c", json!({"sira": ["b"]}))]),
        adim_man(&["--json"], vec![m("a", json!({"sira": ["b"]})), m("b", json!({"sira": ["c"]})), m("c", json!({"sira": ["a"]})), m("d", json!({"sira": ["d"]}))]),
        adim_man(&[], temel()).dosya("veri/manifest/kopya.json", &man("a", json!({})).1),
        adim_man(&[], temel())
            .dosya("veri/manifest/eksik.json", "{\"birim_id\": \"e\", \"tur\": \"pipeline\"}")
            .dosya("veri/manifest/bos.json", "")
            .dosya("veri/manifest/yarim.json", "{\"birim_id\": \"y\", ")
            .dosya("veri/manifest/virgul.json", "{\"a\": 1,}")
            .dosya("veri/manifest/tirnak.json", "{'a': 1}")
            .dosya("veri/manifest/ekstra.json", "{\"a\": 1} {\"b\": 2}")
            .dosya("veri/manifest/ctrl.json", "{\"a\": \"satir\nbolundu\"}")
            .dosya("veri/manifest/kacis.json", "{\"a\": \"\\q\"}")
            .dosya("veri/manifest/uni.json", "{\"a\": \"\\u12G4\"}")
            .dosya("veri/manifest/ikidot.json", "{\"a\" 1}")
            .dosya("veri/manifest/dizi.json", "[1, 2")
            .dosya("veri/manifest/sayi.json", "[01]")
            .dosya("veri/manifest/bom.json", "\u{feff}{}")
            .dosya("veri/manifest/liste.json", "[\"x\"]")
            .ikili("veri/manifest/ikili.json", &[0x7b, 0xff, 0x7d]),
        adim_man(&["--json"], temel()).dosya("veri/manifest/bos.json", "  \n").dosya("veri/manifest/coklu.json", "{\n  \"a\": 1,\n  \"b\": tru\n}").dosya("veri/manifest/gizli.json", "{}").dosya("veri/manifest/.nokta.json", "{bozuk").dosya("veri/manifest/x.txt", "{bozuk"),
        adim_man(&[], temel()).hazir(|k| std::fs::create_dir_all(k.jarvis.join("veri/manifest/dizin.json")).unwrap()),
        adim_man(&["--manifest-dizin", "baska"], vec![]).dosya("baska/a.json", &man("a", json!({})).1),
        adim_man(&["--manifest-dizin", "baska"], vec![]).sil("baska").atla(),
        adim_man(&["--repo", "{R}", "--json"], temel()),
        adim_man(&["--repo", "{K}"], temel()),
        adim_man(&["--repo", "{R}"], temel()).kokte(),
    ];
    let n = fark(Arac::Paralel, "paralel", adimlar);
    say("paralel-kapi", n);
}

// ------------------------------------------------------------------ paralel-kapi: tur_turet (main çağırmaz; Python işlevi doğrudan çağrılır)
#[test]
fn paralel_tur_turet() {
    let vakalar: Vec<Value> = vec![
        json!({}),
        json!({"matris": 1}),
        json!({"eksenler": []}),
        json!({"hucre_tipi": "x"}),
        json!({"tetik_turu": "seans", "iterasyon_ayak_izi": "sabit"}),
        json!({"tetik_turu": "cron", "iterasyon_ayak_izi": "sabit"}),
        json!({"tetik_turu": "cron"}),
        json!({"tetik_turu": "cron", "dis_tavan": 5}),
        json!({"tetik_turu": "cron", "dis_tavan": 5, "iterasyon_ayak_izi": "buyuyen"}),
        json!({"tetik_turu": null, "iterasyon_ayak_izi": "sabit"}),
        json!({"tetik_turu": "cron", "tur_ustyazim": "matris", "tur_ustyazim_gerekce": "neden"}),
        json!({"tetik_turu": "cron", "tur_ustyazim": "matris", "tur_ustyazim_gerekce": ""}),
        json!({"matris": 1, "tur_ustyazim": "loop", "tur_ustyazim_gerekce": "g"}),
    ];
    let k = kum("turet", "eski");
    let betik = ileri(&k.jarvis.join(Arac::Paralel.py()));
    let girdi = serde_json::to_string(&vakalar).unwrap();
    let surucu = format!(
        "import importlib.util, json, sys\nspec = importlib.util.spec_from_file_location('pk', r'{betik}')\nm = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)\nprint(json.dumps([m.tur_turet(b) for b in json.loads(sys.argv[1])]))"
    );
    let o = std::process::Command::new("python").args(["-c", &surucu, &girdi]).env("PYTHONUTF8", "1").output().unwrap();
    assert!(o.status.success(), "{}", String::from_utf8_lossy(&o.stderr));
    let py: Vec<String> = serde_json::from_slice(&o.stdout).unwrap();
    let rs: Vec<String> = vakalar.iter().map(|v| jarvis_kural::paralel::tur_turet(v.as_object().unwrap())).collect();
    assert_eq!(py, rs);
    say("paralel-kapi tur_turet", vakalar.len());
    let _ = std::fs::remove_dir_all(&k.kok);
}
