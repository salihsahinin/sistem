//! `gorev-emri-derleme/scripts/tetik-denetim.py` karşılığı: skill-TETİKLENME şemasının (core/skill-tetikleme-semasi.md) deterministik Kapı-Ö denetimi.
//! Emir dosyasındaki `## SKILL TETİKLERİ` bloğunu okur; her çağrı için skill varlığı, 10 alan, kip, derece ifadesi, retry/FAIL-LOUD, done yüklemi denetlenir.
//! Spec (kısmen): `jarvis/lean/Kanon/SkillTetik.lean` `kapiO`; eşleşme ve ayrışmalar rapor 3. bölümde.
//! Kullanım: `tetik-denetim <emir.md> [--repo <kök>] [--json]`. Çıkış: 0 geçti · 1 sert kapı düştü · 2 kullanım · 3 blok yok.
use crate::py;
use regex::Regex;
use serde_json::{Value, json};
use std::path::{Path, PathBuf};

const BELGE: &str = include_str!("belge/tetik.txt");
const ALANLAR: [&str; 10] = ["skill", "tetik_kosulu", "cagri_kipi", "girdi", "baglam", "yan_etki_damgasi", "done_yuklemi", "hata_yolu", "sira", "kayit"];

struct Kapi {
    id: String,
    ok: bool,
    sert: bool,
    ileti: String,
}

struct Cagri {
    skill: String,
    kapilar: Vec<Kapi>,
    gecti: bool,
}

/// `frontmatter(text)`: `---\n...\n---` başlığındaki `anahtar: değer` satırları.
fn frontmatter(metin: &str) -> Vec<(String, String)> {
    let re = Regex::new(r"(?s)^---\n(.*?)\n---").unwrap();
    let satir = Regex::new(r"^([A-Za-z_-]+):\s*(.*)$").unwrap();
    let mut fm: Vec<(String, String)> = vec![];
    if let Some(m) = re.captures(metin) {
        for l in py::splitlines(&m[1]) {
            if let Some(k) = satir.captures(&l) {
                let (a, d) = (k[1].to_string(), py::strip(&k[2]).to_string());
                match fm.iter_mut().find(|(x, _)| *x == a) {
                    Some(e) => e.1 = d,
                    None => fm.push((a, d)),
                }
            }
        }
    }
    fm
}

/// `skills`: `<repo>/.claude/skills/*/SKILL.md` (gizli dizinler hariç; Windows'ta ad eşleşmesi büyük/küçük harfe duyarsız).
fn skill_haritasi(repo: &Path) -> Vec<(String, PathBuf)> {
    let mut r: Vec<(String, PathBuf)> = vec![];
    let Ok(rd) = std::fs::read_dir(repo.join(".claude").join("skills")) else { return r };
    for e in rd.flatten() {
        let ad = e.file_name().to_string_lossy().into_owned();
        if ad.starts_with('.') || !e.path().is_dir() {
            continue;
        }
        let Ok(alt) = std::fs::read_dir(e.path()) else { continue };
        for f in alt.flatten() {
            let fa = f.file_name().to_string_lossy().into_owned();
            let esles = if cfg!(windows) { fa.eq_ignore_ascii_case("SKILL.md") || fa.to_lowercase() == "skill.md" } else { fa == "SKILL.md" };
            if esles {
                match r.iter_mut().find(|(a, _)| *a == ad) {
                    Some(x) => x.1 = f.path(),
                    None => r.push((ad.clone(), f.path())),
                }
            }
        }
    }
    r
}

fn alan<'a>(f: &'a [(String, String)], k: &str) -> &'a str {
    f.iter().find(|(a, _)| a == k).map(|(_, v)| v.as_str()).unwrap_or("")
}

fn cagri_denetle(parca: &str, skills: &[(String, PathBuf)], re: &Regexler) -> Result<Cagri, String> {
    let mut f: Vec<(String, String)> = vec![];
    for ln in py::splitlines(&format!("skill: {parca}")) {
        if let Some(k) = re.alan.captures(&ln) {
            let (a, d) = (k[1].to_string(), py::strip(&k[2]).to_string());
            match f.iter_mut().find(|(x, _)| *x == a) {
                Some(e) => e.1 = d,
                None => f.push((a, d)),
            }
        }
    }
    let ham = py::strip_kume(alan(&f, "skill"), "`");
    let ad = re.ad_bol.split(ham).next().unwrap_or("").to_string();
    let mut kapilar: Vec<Kapi> = vec![];
    let mut kapi = |id: &str, ok: bool, ileti: String, sert: bool| kapilar.push(Kapi { id: id.into(), ok, sert, ileti });
    let yol = skills.iter().find(|(a, _)| *a == ad).map(|(_, p)| p);
    let var = yol.is_some();
    kapi("O1-var", var, format!("skill `{ad}` hazinede {}", if var { "VAR" } else { "YOK — çağrı kurulamaz (K1)" }), true);
    let eksik: Vec<&str> = ALANLAR.iter().copied().filter(|k| alan(&f, k).is_empty()).collect();
    kapi(
        "O2-alanlar",
        eksik.is_empty(),
        if eksik.is_empty() { "9 alan dolu".to_string() } else { format!("eksik alan: {} — sözleşme tek seferde tam olmalı", py_liste(&eksik)) },
        true,
    );
    let kip = alan(&f, "cagri_kipi").to_lowercase();
    let kip_gecerli = ["literal", "ortuk", "örtük", "yasak"].iter().any(|p| kip.starts_with(p));
    kapi("O3-kip", kip_gecerli, format!("cagri_kipi={} (literal|ortuk|yasak)", if kip.is_empty() { "-" } else { &kip }), true);
    let alt_ajan = py::katlanmis_ara(&format!("{} {}", alan(&f, "baglam"), alan(&f, "sira")), &re.alt_ajan).is_some();
    let mut yan_etkili = false;
    if let Some(p) = yol {
        let metin = match py::oku_kati(p) {
            Ok(t) => t,
            Err(py::OkuHata::Io(e)) => return Err(format!("{}: {e}", p.display())),
            Err(py::OkuHata::Kod) => return Err(format!("{}: UnicodeDecodeError", p.display())),
        };
        let fm = frontmatter(&metin);
        yan_etkili = fm.iter().find(|(a, _)| a == "disable-model-invocation").is_some_and(|(_, v)| v.to_lowercase() == "true");
    }
    if yan_etkili {
        let lit = kip.starts_with("literal");
        kapi("O4-TY-literal", lit, format!("yan-etkili (T-Y) skill → cagri_kipi literal {}", if lit { "✓" } else { "DEĞİL — YASAK" }), true);
        kapi("O4-TY-anasira", !alt_ajan, format!("T-Y skill alt-ajandan/işçiden çağrılmıyor {}", if !alt_ajan { "✓" } else { "— YASAK (önyüklenemez)" }), true);
    }
    let tk = alan(&f, "tetik_kosulu");
    let derece = py::katlanmis_ara(tk, &re.derece);
    kapi(
        "O5-derece-yok",
        derece.is_none(),
        format!("tetik_kosulu boolean {}", match &derece { None => "✓".to_string(), Some(d) => format!("✗ derece ifadesi: '{d}'") }),
        true,
    );
    let (mut bal, mut derinlik) = (0i64, 0i64);
    for c in tk.chars() {
        derinlik = derinlik.max(bal);
        match c {
            '(' => bal += 1,
            ')' => bal -= 1,
            _ => {}
        }
    }
    let ic_ice = re.ic_ice.find_iter(tk).count();
    kapi("O5-icice", derinlik <= 2 && ic_ice <= 3, format!("iç içe koşul derinliği {derinlik} (≤2) · koşul-işareti {ic_ice} (≤3)"), false);
    let neg = re.negatif.is_match(tk);
    kapi("O5-negatif", neg, format!("negatif tetik yazılı {}", if neg { "✓" } else { "— 'Z ise ÇAĞIRMA' eksik" }), false);
    let hy = alan(&f, "hata_yolu");
    let rm = re.retry.captures(hy);
    let retry_ok = match &rm {
        Some(m) => py::int(&m[1]).is_some_and(|n| n <= 3),
        None => false,
    };
    kapi("O6-retry", retry_ok, format!("retry {} (≤3)", rm.as_ref().map(|m| format!("≤{}", &m[1])).unwrap_or_else(|| "YOK".into())), true);
    let fl_genis = py::katlanmis_ara(hy, &re.failloud_genis).is_some();
    let fl_dar = py::katlanmis_ara(hy, &re.failloud_dar).is_some();
    kapi("O6-failloud", fl_genis, format!("FAIL-LOUD {}", if fl_dar { "✓" } else { "YOK" }), true);
    let dy = alan(&f, "done_yuklemi");
    let derece_yok = py::katlanmis_ara(dy, &re.done_genis).is_none();
    let derece_yok_dar = py::katlanmis_ara(dy, &re.done_dar).is_none();
    kapi("O7-done-boolean", derece_yok, format!("done_yuklemi boolean {}", if derece_yok_dar { "✓" } else { "✗ derece ifadesi" }), true);
    let yd = alan(&f, "yan_etki_damgasi").to_lowercase();
    kapi(
        "O8-damga",
        re.damga.is_match(&yd),
        format!("yan_etki_damgasi={}", if yd.is_empty() { "YOK → yıkıcı varsayılır" } else { &yd }),
        false,
    );
    let gecti = !kapilar.iter().any(|k| k.sert && !k.ok);
    Ok(Cagri { skill: ad, kapilar, gecti })
}

/// Python liste gösterimi: `['a', 'b']`.
fn py_liste(l: &[&str]) -> String {
    format!("[{}]", l.iter().map(|s| py::repr(s)).collect::<Vec<_>>().join(", "))
}

struct Regexler {
    alan: Regex,
    ad_bol: Regex,
    alt_ajan: Regex,
    derece: Regex,
    ic_ice: Regex,
    negatif: Regex,
    retry: Regex,
    failloud_genis: Regex,
    failloud_dar: Regex,
    done_genis: Regex,
    done_dar: Regex,
    damga: Regex,
}

impl Regexler {
    fn yeni() -> Self {
        // Python `re.I` desenleri katlanmış metne karşı katlanmış desenle aranır (`py::katla`; `ı`/`İ`/`ſ` denkliği dahil)
        let k = |s: &str| Regex::new(&py::katla(s)).unwrap();
        Regexler {
            alan: Regex::new(r"^\s*([a-z_]+):\s*(.*)$").unwrap(),
            ad_bol: Regex::new(r"[\s#(]").unwrap(),
            alt_ajan: k(r"alt-ajan|subagent|fork|işçi"),
            derece: k(r"gerekirse|uygunsa|mümkünse|icap ederse|isteğe bağlı|if needed|when appropriate"),
            ic_ice: Regex::new(r"\beğer\b|\bise\b|→").unwrap(),
            negatif: Regex::new(r"ÇAĞIRMA|çağırma|KULLANMA|yasak|¬").unwrap(),
            retry: Regex::new(r"retry\s*[≤<=]*\s*(\d+)").unwrap(),
            failloud_genis: k(r"FAIL-?LOUD|fail loud|sessiz düşüş yasak"),
            failloud_dar: k(r"FAIL-?LOUD|fail loud"),
            done_genis: k(r"iyi bir|kaliteli|yeterince|mümkün olduğunca|başarılı olur"),
            done_dar: k(r"iyi bir|kaliteli|yeterince"),
            damga: Regex::new(r"salt-okur|eklemeli|yıkıcı").unwrap(),
        }
    }
}

pub fn kos(argv: &[String]) -> i32 {
    let args: Vec<&String> = argv.iter().filter(|a| !a.starts_with("--")).collect();
    let json = argv.iter().any(|a| a == "--json");
    let repo = match argv.iter().position(|a| a == "--repo") {
        Some(i) => match argv.get(i + 1) {
            Some(r) => r.clone(),
            None => return py::coker("`--repo` son argüman (IndexError)"),
        },
        None => std::env::current_dir().map(|d| d.to_string_lossy().into_owned()).unwrap_or_default(),
    };
    let Some(dosya) = args.first() else {
        py::print(BELGE);
        return 2;
    };
    let metin = match py::oku_kati(Path::new(dosya.as_str())) {
        Ok(t) => t,
        Err(py::OkuHata::Io(e)) => return py::coker(&format!("{dosya}: {e}")),
        Err(py::OkuHata::Kod) => return py::coker(&format!("{dosya}: UnicodeDecodeError")),
    };
    let re_baslik = Regex::new(r"(?m)^##\s*SKILL TETİKLERİ").unwrap();
    let Some(m) = re_baslik.find(&metin) else {
        py::print("SKILL TETİKLERİ bloğu YOK (emirde skill çağrılmıyorsa 'yok' yazılmalı)");
        return 3;
    };
    // `.*?$`: başlık satırının sonu; blok bir sonraki `^##\s` satırına ya da dosya sonuna dek
    let bas = metin[m.end()..].find('\n').map(|i| m.end() + i).unwrap_or(metin.len());
    let son = Regex::new(r"(?m)^##\s").unwrap().find_at(&metin, bas).map(|x| x.start()).unwrap_or(metin.len());
    let blok = &metin[bas..son];
    let yok = Regex::new(&py::katla(r"^\s*(-\s*)?yok\s*$")).unwrap();
    if yok.is_match(&py::katla(py::strip(blok))) {
        py::print("SKILL TETİKLERİ: yok — çağrı bloğu gerekmiyor");
        return 0;
    }
    let parcalar: Vec<&str> = Regex::new(r"(?m)^\s*-\s*skill:\s*").unwrap().split(blok).skip(1).collect();
    let skills = skill_haritasi(Path::new(&repo));
    let re = Regexler::yeni();
    let mut cagrilar: Vec<Cagri> = vec![];
    for p in parcalar {
        match cagri_denetle(p, &skills, &re) {
            Ok(c) => cagrilar.push(c),
            Err(e) => return py::coker(&e),
        }
    }
    let sert_dustu = cagrilar.iter().any(|c| !c.gecti);
    let sonuc = if sert_dustu { "BLOKE" } else { "GEÇTİ" };
    let cagri_sonuc = |c: &Cagri| if c.gecti { "GEÇTİ" } else { "BLOKE" };
    if json {
        let calls: Vec<Value> = cagrilar
            .iter()
            .map(|c| {
                let g: Vec<Value> = c.kapilar.iter().map(|k| json!({"id": k.id, "ok": k.ok, "hard": k.sert, "msg": k.ileti})).collect();
                json!({"skill": c.skill, "gates": g, "sonuc": cagri_sonuc(c)})
            })
            .collect();
        py::print(&py::json_girintili(&json!({"calls": calls, "sonuc": sonuc})));
    } else {
        for c in &cagrilar {
            py::print(&format!("== çağrı `{}` — {}", c.skill, cagri_sonuc(c)));
            for g in &c.kapilar {
                let isaret = if g.ok { "✓" } else if g.sert { "✗" } else { "△" };
                py::print(&format!("  [{isaret}] {}: {}", g.id, g.ileti));
            }
        }
        py::print(&format!("=== SONUÇ: {sonuc} ({} çağrı)", cagrilar.len()));
    }
    if sert_dustu { 1 } else { 0 }
}
