//! `tools/alan-ajani-dogur.py` karşılığı: alan ajanı doğurucu (Karar 105, masa-18; Karar 103 M4 · Karar 104 M5).
//! Spec dosyasındaki her ajan için `<kök>/<dizin>/` iskeletini `sablonlar/ajan-iskelet/` şablonlarından üretir; hook'lar Friday'den v0.6 yamasıyla türetilir.
//! Çıkış: 0 üretildi/aynı · 2 argparse hatası · 1 `sys.exit(metin)` durumları.
//! KÖK çözümü (Python betik konumundan türetir): env `SISTEM_KOK`, yoksa ikilinin dizininden yukarı `Cargo.toml` + `sablonlar/` olan ilk ata, en sonda cwd'den yukarı.
use jarvis_rituel::argparse::{Ayrisan, Secenek};
use jarvis_rituel::py;
use regex::{NoExpand, Regex};
use serde_json::Value;
use std::collections::HashMap;
use std::fs;
use std::path::Path;

const BELGE: &str = r#"Alan ajanı doğurucu (Karar 105, masa-18, 2026-09-21; Karar 103 M4 alan ajanı = kalıcı dizin · Karar 104 M5 doğum belgesi).

Ne yapar: spec dosyasındaki her ajan için `~/sistem/<dizin>/` iskeletini `sablonlar/ajan-iskelet/` şablonlarından
deterministik üretir: AGENTS.md (charter, §0b doğum belgesi) + CLAUDE.md symlink · README · core/ (kapsül · pano · desenler)
· kuyruk/ (defter · kutu) · cc/gelen|giden · raporlar · arsiv · veri/bronz · .claude/ (settings · okuma-izin-ek · hooks
v0.6 · skills seans-acilis/kapanis · skills/ogren → ../../../sablonlar/skills/ogren symlink · agents/hakem alan perspektifli).
Hook'lar Friday'in v0.5 kopyasından v0.6 yamasıyla türetilir (tek kaynak `friday/.claude/hooks/`; yama = okuma-izin-ek).
Ortak `sablonlar/skills/ogren/` yoksa `jarvis/.claude/skills/ogren/`'den v0.3 (alan sürümü) olarak türetilir.

İdempotens: var olan dosyanın üstüne YAZMAZ (`--uzerine-yaz` verilmedikçe); rapor "yeni/atlandı/aynı" sayar. Şerit taşıma (T3,
`git mv ../ogrenme/<şerit> <dizin>/ogrenme/`) Salih elidir: komut listesi basılır, koşulmaz (m.8 taşıma Salih beyanı).

Kullanım: python3 tools/alan-ajani-dogur.py kuyruk/alan-ajanlari-YYYY-MM-DD.json [--kuru] [--uzerine-yaz] [--tarih YYYY-MM-DD]
Çıkış: 0 = üretildi/aynı · 2 = spec/şablon hatası.
"#;

const CLAUDE_AYAR: &str = "claude-ayar"; // şablonda bu ad; hedefte ".claude"

#[derive(Default)]
struct Sayac {
    yeni: usize,
    atlandi: usize,
    ayni: usize,
}

struct Yollar {
    kok: String,
    iskelet: String,
    friday_hooks: String,
    ogren_kaynak: String,
    ogren_ortak: String,
}

/// Sistem kökü (bkz. modül başlığı).
pub fn kok_coz() -> String {
    if let Ok(v) = std::env::var("SISTEM_KOK")
        && !v.is_empty()
    {
        return py::abspath(&v);
    }
    let uygun = |d: &Path| d.join("Cargo.toml").is_file() && d.join("sablonlar").is_dir();
    if let Ok(exe) = std::env::current_exe() {
        for d in exe.ancestors().skip(1) {
            if uygun(d) {
                return py::abspath(&d.to_string_lossy());
            }
        }
    }
    if let Ok(cwd) = std::env::current_dir() {
        for d in cwd.ancestors() {
            if uygun(d) {
                return py::abspath(&d.to_string_lossy());
            }
        }
        return py::abspath(&cwd.to_string_lossy());
    }
    py::abspath(".")
}

fn yollar() -> Yollar {
    let kok = kok_coz();
    let jarvis = py::join(&kok, "jarvis");
    let sablonlar = py::join(&kok, "sablonlar");
    Yollar {
        iskelet: py::join(&sablonlar, "ajan-iskelet"),
        friday_hooks: py::join(&py::join(&py::join(&kok, "friday"), ".claude"), "hooks"),
        ogren_kaynak: py::join(&py::join(&py::join(&jarvis, ".claude"), "skills"), "ogren"),
        ogren_ortak: py::join(&py::join(&sablonlar, "skills"), "ogren"),
        kok,
    }
}

// ---------------------------------------------------------------- dosya sistemi (Python taklidi)
fn oku(yol: &str) -> Result<String, String> {
    match py::oku_kati(Path::new(yol)) {
        Ok(t) => Ok(t),
        Err(py::OkuHata::Io(e)) => Err(format!("{yol}: {e}")),
        Err(py::OkuHata::Kod) => Err(format!("{yol}: UnicodeDecodeError")),
    }
}

/// Metin kipinde yazım: Windows'ta Python `\n` -> `\r\n` çevirir.
pub fn metin_yaz(yol: &str, icerik: &str) -> Result<(), String> {
    let b = if cfg!(windows) { icerik.replace('\n', "\r\n") } else { icerik.to_string() };
    fs::write(yol, b).map_err(|e| format!("{yol}: {e}"))
}

fn ust_dizin_yap(yol: &str) -> Result<(), String> {
    if let Some(p) = Path::new(yol).parent() {
        fs::create_dir_all(p).map_err(|e| format!("{}: {e}", p.display()))?;
    }
    Ok(())
}

fn yaz(yol: &str, icerik: &str, uzerine: bool, kuru: bool, calistir: bool, s: &mut Sayac) -> Result<(), String> {
    if Path::new(yol).exists() {
        if oku(yol)? == icerik {
            s.ayni += 1;
            return Ok(());
        }
        if !uzerine {
            s.atlandi += 1;
            return Ok(());
        }
    }
    s.yeni += 1;
    if kuru {
        return Ok(());
    }
    ust_dizin_yap(yol)?;
    metin_yaz(yol, icerik)?;
    if calistir {
        #[cfg(unix)]
        {
            use std::os::unix::fs::PermissionsExt;
            let m = fs::metadata(yol).map_err(|e| format!("{yol}: {e}"))?.permissions().mode();
            fs::set_permissions(yol, fs::Permissions::from_mode(m | 0o110)).map_err(|e| format!("{yol}: {e}"))?;
        }
    }
    Ok(())
}

fn symlink_mi(p: &Path) -> bool {
    p.symlink_metadata().map(|m| m.file_type().is_symlink()).unwrap_or(false)
}

fn symlink(hedef: &str, yol: &str, kuru: bool, s: &mut Sayac) -> Result<(), String> {
    let p = Path::new(yol);
    let link = symlink_mi(p);
    if link || p.exists() {
        let ayni = link
            && fs::read_link(p).map(|h| {
                let h = h.to_string_lossy().into_owned();
                h.strip_prefix(r"\\?\").unwrap_or(&h) == hedef
            }).unwrap_or(false);
        if ayni { s.ayni += 1 } else { s.atlandi += 1 }
        return Ok(());
    }
    s.yeni += 1;
    if !kuru {
        ust_dizin_yap(yol)?;
        #[cfg(unix)]
        std::os::unix::fs::symlink(hedef, p).map_err(|e| format!("{yol}: {e}"))?;
        #[cfg(windows)]
        {
            let dizin = p.parent().map(|u| u.join(hedef).is_dir()).unwrap_or(false);
            let r = if dizin { std::os::windows::fs::symlink_dir(hedef, p) } else { std::os::windows::fs::symlink_file(hedef, p) };
            r.map_err(|e| format!("{yol}: {e}"))?;
        }
    }
    Ok(())
}

/// `os.walk(taban)` dosyaları (üst dizinin dosyaları, sonra alt dizinler; ad sıralı; symlink dizinlerine inilmez): (tam yol, `relpath`).
fn dosyalar(taban: &str) -> Vec<(String, String)> {
    fn gez(tam: &str, rel: &str, cikti: &mut Vec<(String, String)>) {
        let Ok(rd) = fs::read_dir(tam) else { return };
        let mut girdiler: Vec<_> = rd.filter_map(Result::ok).collect();
        girdiler.sort_by_key(|e| e.file_name());
        let (mut dizinler, mut dosya) = (vec![], vec![]);
        for e in girdiler {
            let ad = e.file_name().to_string_lossy().into_owned();
            if e.path().is_dir() {
                let link = e.file_type().map(|t| t.is_symlink()).unwrap_or(false);
                if !link {
                    dizinler.push(ad);
                }
            } else {
                dosya.push(ad);
            }
        }
        for ad in dosya {
            let r = if rel.is_empty() { ad.clone() } else { py::join(rel, &ad) };
            cikti.push((py::join(tam, &ad), r));
        }
        for ad in dizinler {
            let r = if rel.is_empty() { ad.clone() } else { py::join(rel, &ad) };
            gez(&py::join(tam, &ad), &r, cikti);
        }
    }
    let mut c = vec![];
    gez(taban, "", &mut c);
    c
}

fn basename(p: &str) -> String {
    let (_, kuyruk) = py::splitdrive(p);
    let ayirac = |c: char| if cfg!(windows) { c == '/' || c == '\\' } else { c == '/' };
    match kuyruk.rfind(ayirac) {
        Some(i) => kuyruk[i + 1..].to_string(),
        None => kuyruk,
    }
}

// ---------------------------------------------------------------- hook yaması
fn degistir(t: &str, a: &str, b: &str) -> String {
    t.replace(a, b)
}

fn hook_v06(y: &Yollar, ad: &str) -> Result<String, String> {
    let mut t = oku(&py::join(&y.friday_hooks, ad))?;
    if ad == "okuma-izin.sh" {
        t = t.replacen(
            "input=$(cat)\n",
            concat!(
                "# v0.6 (2026-09-21, Karar 105 M6 alan ajanları): `.claude/okuma-izin-ek` dosyası (satır başına depo köküne göreli yol, ör.\n",
                "#   `ogrenme/kaynaklar`) izinli köklere eklenir — salt-okur ortak kaynaklar; yazma yasağı settings deny'de. Dosya yoksa v0.5 ile aynı.\n",
                "#   Tek kaynak `friday/.claude/hooks/okuma-izin.sh`; bu kopya `jarvis/tools/alan-ajani-dogur.py` yamasıyla üretilir, elle düzenlenmez.\n",
                "input=$(cat)\n"
            ),
            1,
        );
        let a = concat!(
            r#"izinli = [repo, os.path.join(kok, "sablonlar"), "/tmp", "/private/tmp", "/private/var/folders", harness]  # kök sablonlar/ ortak (F4)"#,
            "\n"
        );
        let b = concat!(
            r#"izinli = [repo, os.path.join(kok, "sablonlar"), "/tmp", "/private/tmp", "/private/var/folders", harness]  # kök sablonlar/ ortak (F4)"#,
            "\n",
            "try:  # v0.6: ek salt-okur kökler (depo köküne göreli; ör. ogrenme/kaynaklar)\n",
            r#"    for satir in open(os.path.join(repo, ".claude", "okuma-izin-ek"), encoding="utf-8"):"#,
            "\n",
            "        satir = satir.strip()\n",
            r##"        if satir and not satir.startswith("#"):"##,
            "\n",
            "            izinli.append(os.path.realpath(os.path.join(kok, satir)))\n",
            "except OSError:\n",
            "    pass\n"
        );
        t = t.replacen(a, b, 1);
        t = degistir(
            &t,
            r#"os.environ.get("FRIDAY_HOOK_TEST") or os.environ.get("JARVIS_HOOK_TEST")"#,
            r#"os.environ.get("FRIDAY_HOOK_TEST") or os.environ.get("JARVIS_HOOK_TEST") or os.environ.get("AJAN_HOOK_TEST")"#,
        );
        t = degistir(&t, r#""kaynak": "okuma-izin.sh v0.4""#, r#""kaynak": "okuma-izin.sh v0.6""#);
        t = degistir(
            &t,
            "OKUMA-İZİN KİLİDİ (Karar 91/101): lider reposu kendi dizini + depo kökündeki kanon dosyalarını okur; jarvis/** ve repo dışı kullanıcı yolu kapalıdır.",
            "OKUMA-İZİN KİLİDİ (Karar 91/101/105): ajan kendi dizini + depo kökündeki kanon dosyaları + sablonlar/ + okuma-izin-ek kökleri okur; diğer ajan dizinleri (jarvis/**, friday/**, alan ajanları) ve repo dışı kullanıcı yolu kapalıdır.",
        );
        if !t.contains("okuma-izin-ek") {
            return Err("AssertionError: v0.6 yaması tutmadı (Friday hook'u değişmiş olabilir)".into());
        }
    } else if ad == "okuma-izin-test.sh" {
        t = degistir(
            &t,
            "# Friday okuma-izin kilidi testi.",
            "# Alan-ajanı okuma-izin kilidi testi (v0.6; Friday testinin kopyası + Karar 105 vakaları; üretici alan-ajani-dogur.py).",
        );
        t = degistir(&t, r#"'"$SISTEM"'/friday/"#, r#"'"$SISTEM"'/__ajan__/"#);
        let ek = concat!(
            "echo \"-- v0.6 alan ajanı (Karar 105) --\"\n",
            r##"t "Read ../friday/core → RED (başka ajan)"        '{"tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/friday/core/rol.md"}}' 2"##,
            "\n",
            r##"t "Read başka alan ajanı core → RED"              '{"tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/__baska_ajan__/core/durum-kapsulu.md"}}' 2"##,
            "\n",
            r##"t "Read ogrenme/kaynaklar (okuma-izin-ek) → geçer" '{"tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/ogrenme/kaynaklar/README.md"}}' 0"##,
            "\n",
            r##"t "Bash cat ../ogrenme/kaynaklar/x → geçer"       '{"tool_name":"Bash","tool_input":{"command":"cat ../ogrenme/kaynaklar/README.md"}}' 0"##,
            "\n",
            r##"t "Read ../ogrenme/evals (kaynaklar dışı) → RED"   '{"tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/ogrenme/mufredat.md"}}' 2"##,
            "\n",
            "echo \"--------\""
        );
        t = t.replacen("echo \"--------\"", ek, 1);
    }
    Ok(t)
}

fn ogren_ortak_hazirla(y: &Yollar, uzerine: bool, kuru: bool, s: &mut Sayac) -> Result<(), String> {
    let pointer = Regex::new(r"(?s)\n> \*\*Karar 105 \(2026-09-21\):\*\* dersi koşan kopya artık alan ajanlarında:.*?\n").expect("regex");
    for (kaynak, rel) in dosyalar(&y.ogren_kaynak) {
        let mut t = oku(&kaynak)?;
        if rel == "SKILL.md" {
            t = pointer.replacen(&t, 1, NoExpand("\n")).into_owned();
            t = degistir(
                &t,
                "# ogren — dört fazlı ders akışı + öğrenme oturum protokolü (v0.2, 2026-09-15; deneme v0.1 09-09 → hazine)",
                concat!(
                    "# ogren — dört fazlı ders akışı + öğrenme oturum protokolü (v0.3 ALAN SÜRÜMÜ, 2026-09-21, Karar 105; v0.2 09-15 Jarvis kopyası `jarvis/.claude/skills/ogren/` öğretim-tasarımı için kalır)\n\n",
                    r##"**Alan-ajanı farkı (Karar 103 EK 1 · Karar 105 M4):** bu skill alan ajanının dizininde (`~/sistem/<alan>/`) koşar; şerit yolları `ogrenme/<şerit>/` **bu dizine** görelidir; ders iskeleti (`PROBE` soruları · `PLAN` DAG · kutu başlıkları) Jarvis'ten `cc/gelen/ders-<hafta>.md` ile gelir — varsa aynen kullanılır, `PROBE`/`PLAN` üretilmez; yoksa önceki dersin `## Kalan` listesiyle devam edilir, **yeni hafta açılmaz** (Jarvis'e `cc/giden/` ile "iskelet gerekli: <hafta>" notu). Oturum: cwd alan dizini, worktree kapalı, main, pathspec-only; PR yok, push yalnız Salih beyanıyla (protokol §5 EK-4 Karar 105 satırı). `mcp__visualize` yoksa DAG `raporlar/gorsel-*.html` olarak elle yazılır."##
                ),
            );
            t = degistir(
                &t,
                "Yan oturum worktree + kendi branch'i; ilk iş `git fetch origin && git rebase origin/main` (protokol §5 EK).",
                "Alan ajanında worktree yok: cwd `~/sistem/<alan>`, main; ilk iş `git log -3 -- .` canlı-oturum kapısı (seans-acilis).",
            );
            t = degistir(
                &t,
                r##"Sonra `git add ogrenme/<şerit>/…` + commit (İngilizce mesaj, m.10) + push + PR (`gh-axi pr create`, açıklamada "yalnız bu oturumun commit'leri"); merge ana-sıra Fable'da (Karar 95). Kapsül/pano/defter'e yazılmaz; `seans-kapanis` koşulmaz."##,
                "Sonra `git add ogrenme/<şerit>/…` + commit (İngilizce mesaj, m.10); push yalnız Salih beyanıyla, PR yok. Kapsül/pano/defter alan ajanının kendi `seans-kapanis` ritüelinde yazılır.",
            );
        }
        yaz(&py::join(&y.ogren_ortak, &rel), &t, uzerine, kuru, false, s)?;
    }
    Ok(())
}

/// `{{ANAHTAR}}` doldurma; anahtar yoksa `sys.exit` metni `\0` önekli hata olarak döner (çağıran stderr + çıkış 1 yapar).
fn doldur(sablon: &str, d: &HashMap<&str, String>) -> Result<String, String> {
    let re = Regex::new(r"\{\{(\w+)\}\}").expect("regex");
    let mut cikti = String::with_capacity(sablon.len());
    let mut son = 0;
    for m in re.captures_iter(sablon) {
        let tam = m.get(0).expect("eşleşme");
        let k = &m[1];
        cikti.push_str(&sablon[son..tam.start()]);
        match d.get(k) {
            Some(v) => cikti.push_str(v),
            None => return Err(format!("\u{0}[HATA] şablon anahtarı yok: {{{{{k}}}}}")),
        }
        son = tam.end();
    }
    cikti.push_str(&sablon[son..]);
    Ok(cikti)
}

// ---------------------------------------------------------------- JSON değerleri
/// Python `str(v)` / `%s` (yalnız skaler değerler; kapsayıcılar desteklenmez).
fn py_str(v: &Value) -> Result<String, String> {
    match v {
        Value::String(s) => Ok(s.clone()),
        Value::Number(n) => Ok(n.to_string()),
        Value::Bool(true) => Ok("True".into()),
        Value::Bool(false) => Ok("False".into()),
        Value::Null => Ok("None".into()),
        _ => Err("kapsayıcı değer metne çevrilemedi".into()),
    }
}

fn al<'a>(v: &'a Value, k: &str) -> Result<&'a Value, String> {
    v.get(k).ok_or_else(|| format!("KeyError: {}", py::repr(k)))
}

fn al_metin(v: &Value, k: &str) -> Result<String, String> {
    py_str(al(v, k)?)
}

fn dizi<'a>(v: &'a Value, k: &str) -> Result<&'a Vec<Value>, String> {
    al(v, k)?.as_array().ok_or_else(|| format!("{k}: liste değil"))
}

fn uret(y: &Yollar, spec: &Value, tarih: &str, uzerine: bool, kuru: bool, s: &mut Sayac) -> Result<(), String> {
    let ajanlar = dizi(spec, "ajanlar")?;
    for aj in ajanlar {
        let dizin = al_metin(aj, "dizin")?;
        let hedef = py::join(&y.kok, &dizin);
        let seritler_v = dizi(aj, "seritler")?;
        let mut seritler_parca = vec![];
        let mut tablo_satir = vec![];
        let mut pano_satir = vec![];
        for sr in seritler_v {
            let (kaynak, shedef, durum) = (al_metin(sr, "kaynak")?, al_metin(sr, "hedef")?, al_metin(sr, "durum")?);
            seritler_parca.push(format!("`{shedef}` ({durum})"));
            tablo_satir.push(format!("| {} | `../{kaynak}` | `{shedef}` | {durum} |", basename(&kaynak)));
            pano_satir.push(format!(
                "| {} | şerit: {durum} | sıradaki hafta kavramsal `DONE` + pratik Salih beyanı | {tarih} | `{shedef}/ilerleme.md` | her seans |",
                basename(&shedef)
            ));
        }
        let ad = al_metin(aj, "ad")?;
        let alan_kisa = match aj.get("alan_kisa") {
            Some(v) => py_str(v)?,
            None => dizin.clone(),
        };
        let mut d: HashMap<&str, String> = HashMap::new();
        d.insert("AD", ad.clone());
        d.insert("AD_BUYUK", ad.to_uppercase());
        d.insert("ALAN_KISA", alan_kisa);
        d.insert("AD_GEREKCE", al_metin(aj, "ad_gerekce")?);
        d.insert("DIZIN", dizin.clone());
        d.insert("ALAN", al_metin(aj, "alan")?);
        d.insert("MODEL", al_metin(spec, "model")?);
        d.insert("BAKIM", al_metin(spec, "bakim_maliyeti")?);
        d.insert("KARAR", al_metin(spec, "karar")?);
        d.insert("TARIH", tarih.to_string());
        d.insert("SERITLER", seritler_parca.join(" · "));
        d.insert(
            "SERIT_TABLO",
            format!("| Şerit | Kaynak (T3 öncesi) | Hedef | Durum |\n|---|---|---|---|\n{}", tablo_satir.join("\n")),
        );
        d.insert("URUN", al_metin(aj, "urun")?);
        d.insert("HAKEM_PERSPEKTIFI", al_metin(aj, "hakem_perspektifi")?);
        d.insert("PANO_SATIRLARI", pano_satir.join("\n"));
        // şablon dosyaları (.tmpl -> doldur; diğerleri aynen)
        for (kaynak, rel) in dosyalar(&y.iskelet) {
            let mut rel = rel;
            let onek = format!("{CLAUDE_AYAR}{}", py::SEP);
            if let Some(kalan) = rel.strip_prefix(&onek) {
                rel = py::join(".claude", kalan);
            }
            let mut t = oku(&kaynak)?;
            if let Some(r) = rel.strip_suffix(".tmpl") {
                let r = r.to_string();
                t = doldur(&t, &d)?;
                rel = r;
            }
            yaz(&py::join(&hedef, &rel), &t, uzerine, kuru, rel.ends_with(".sh"), s)?;
        }
        // hook'lar (Friday'den yamalı)
        for hook in ["okuma-izin.sh", "okuma-izin-test.sh", "hareket-kutuk.sh"] {
            let mut t = hook_v06(y, hook)?;
            if hook == "okuma-izin-test.sh" {
                let mut baska = "friday".to_string();
                for x in ajanlar {
                    let xd = al_metin(x, "dizin")?;
                    if xd != dizin {
                        baska = xd;
                        break;
                    }
                }
                t = t.replace("__baska_ajan__", &baska).replace("__ajan__", &dizin);
            }
            let yol = py::join(&py::join(&py::join(&hedef, ".claude"), "hooks"), hook);
            yaz(&yol, &t, uzerine, kuru, true, s)?;
        }
        // boş dizinler + symlink'ler
        for bos in ["cc/gelen", "cc/giden", "cc/rapor", "raporlar", "arsiv", "veri/bronz", "ogrenme"] {
            let mut yol = hedef.clone();
            for p in bos.split('/') {
                yol = py::join(&yol, p);
            }
            yaz(&py::join(&yol, ".gitkeep"), "", uzerine, kuru, false, s)?;
        }
        symlink("AGENTS.md", &py::join(&hedef, "CLAUDE.md"), kuru, s)?;
        let ogren_hedef = py::join(&py::join(&py::join(&py::join("..", ".."), ".."), "sablonlar"), "skills");
        symlink(&py::join(&ogren_hedef, "ogren"), &py::join(&py::join(&py::join(&hedef, ".claude"), "skills"), "ogren"), kuru, s)?;
        let hafiza = py::join(&py::join(&py::join(&py::join(&hedef, ".claude"), "agent-memory"), "hakem"), "MEMORY.md");
        yaz(
            &hafiza,
            &format!("# {ad} hakemi hafızası (yalnız usul dersleri; içerik hükmü girmez)\n\n- {tarih}: doğum; ilk koşum sonrası kendi kalıp hataları buraya.\n"),
            uzerine,
            kuru,
            false,
            s,
        )?;
    }
    // T3 komut listesi (Salih eli)
    py::print("\n# T3 — Salih eli (git mv; m.8 taşıma beyanı). Sıra önemli değil; sonra tek commit `[icra] Decision 105 T3: move learning tracks into domain agents`:");
    py::print("cd ~/sistem");
    for aj in ajanlar {
        for sr in dizi(aj, "seritler")? {
            py::print(&format!("git mv {} {}/{}", al_metin(sr, "kaynak")?, al_metin(aj, "dizin")?, al_metin(sr, "hedef")?));
        }
    }
    py::print("git commit -m \"[icra] Decision 105 T3: move learning tracks into domain agent directories\"   # git mv zaten stage'ler; -A yasak");
    Ok(())
}

// ---------------------------------------------------------------- Python `json.load` hata iletisi taklidi
struct Tarayici {
    c: Vec<char>,
}
type Sonuc<T> = Result<T, (&'static str, usize)>;

impl Tarayici {
    fn bosluk(&self, mut i: usize) -> usize {
        while i < self.c.len() && matches!(self.c[i], ' ' | '\t' | '\n' | '\r') {
            i += 1;
        }
        i
    }
    fn basla(&self, i: usize, s: &str) -> bool {
        s.chars().enumerate().all(|(k, ch)| self.c.get(i + k) == Some(&ch))
    }
    fn rakam(&self, i: usize) -> bool {
        self.c.get(i).is_some_and(|c| c.is_ascii_digit())
    }
    fn sayi(&self, i0: usize) -> Sonuc<usize> {
        let bos = ("Expecting value", i0);
        let mut j = i0;
        if self.c[j] == '-' {
            j += 1;
            if j >= self.c.len() {
                return Err(bos);
            }
        }
        match self.c[j] {
            '1'..='9' => {
                while self.rakam(j) {
                    j += 1;
                }
            }
            '0' => j += 1,
            _ => return Err(bos),
        }
        if self.c.get(j) == Some(&'.') && self.rakam(j + 1) {
            j += 2;
            while self.rakam(j) {
                j += 1;
            }
        }
        if matches!(self.c.get(j), Some('e' | 'E')) {
            let mut k = j + 1;
            if matches!(self.c.get(k), Some('+' | '-')) {
                k += 1;
            }
            if self.rakam(k) {
                while self.rakam(k) {
                    k += 1;
                }
                j = k;
            }
        }
        Ok(j)
    }
    fn dize(&self, bas: usize) -> Sonuc<usize> {
        let acilis = bas - 1;
        let n = self.c.len();
        let mut j = bas;
        loop {
            if j >= n {
                return Err(("Unterminated string starting at", acilis));
            }
            match self.c[j] {
                '"' => return Ok(j + 1),
                '\\' => {
                    if j + 1 >= n {
                        return Err(("Unterminated string starting at", acilis));
                    }
                    if self.c[j + 1] == 'u' {
                        let sonraki = j + 2;
                        let son = sonraki + 4;
                        if son >= n {
                            return Err(("Invalid \\uXXXX escape", sonraki - 1));
                        }
                        if !(sonraki..son).all(|k| self.c[k].is_ascii_hexdigit()) {
                            return Err(("Invalid \\uXXXX escape", son - 5));
                        }
                        j = son;
                    } else if matches!(self.c[j + 1], '"' | '\\' | '/' | 'b' | 'f' | 'n' | 'r' | 't') {
                        j += 2;
                    } else {
                        return Err(("Invalid \\escape", j));
                    }
                }
                ch if ch < ' ' => return Err(("Invalid control character at", j)),
                _ => j += 1,
            }
        }
    }
    fn nesne(&self, mut i: usize) -> Sonuc<usize> {
        let n = self.c.len();
        i = self.bosluk(i);
        if !(i < n && self.c[i] == '}') {
            loop {
                if i >= n || self.c[i] != '"' {
                    return Err(("Expecting property name enclosed in double quotes", i));
                }
                i = self.dize(i + 1)?;
                i = self.bosluk(i);
                if i >= n || self.c[i] != ':' {
                    return Err(("Expecting ':' delimiter", i));
                }
                i = self.bosluk(i + 1);
                i = self.deger(i)?;
                i = self.bosluk(i);
                if i < n && self.c[i] == '}' {
                    break;
                }
                if i >= n || self.c[i] != ',' {
                    return Err(("Expecting ',' delimiter", i));
                }
                i = self.bosluk(i + 1);
            }
        }
        Ok(i + 1)
    }
    fn liste(&self, mut i: usize) -> Sonuc<usize> {
        let n = self.c.len();
        i = self.bosluk(i);
        if !(i < n && self.c[i] == ']') {
            loop {
                i = self.deger(i)?;
                i = self.bosluk(i);
                if i < n && self.c[i] == ']' {
                    break;
                }
                if i >= n || self.c[i] != ',' {
                    return Err(("Expecting ',' delimiter", i));
                }
                i = self.bosluk(i + 1);
            }
        }
        Ok(i + 1)
    }
    fn deger(&self, i: usize) -> Sonuc<usize> {
        if i >= self.c.len() {
            return Err(("Expecting value", i));
        }
        match self.c[i] {
            '"' => self.dize(i + 1),
            '{' => self.nesne(i + 1),
            '[' => self.liste(i + 1),
            'n' if self.basla(i, "null") => Ok(i + 4),
            't' if self.basla(i, "true") => Ok(i + 4),
            'f' if self.basla(i, "false") => Ok(i + 5),
            'N' if self.basla(i, "NaN") => Ok(i + 3),
            'I' if self.basla(i, "Infinity") => Ok(i + 8),
            '-' if self.basla(i, "-Infinity") => Ok(i + 9),
            _ => self.sayi(i),
        }
    }
}

/// `json.load` ayrıştırma hatası iletisi (`JSONDecodeError.__str__`); geçerliyse `None`.
fn json_hata(metin: &str) -> Option<String> {
    let t = Tarayici { c: metin.chars().collect() };
    let sonuc = if t.c.first() == Some(&'\u{feff}') {
        Err(("Unexpected UTF-8 BOM (decode using utf-8-sig)", 0))
    } else {
        t.deger(t.bosluk(0)).and_then(|e| {
            let e = t.bosluk(e);
            if e != t.c.len() { Err(("Extra data", e)) } else { Ok(e) }
        })
    };
    let (ileti, poz) = sonuc.err()?;
    let onceki = &t.c[..poz];
    let satir = onceki.iter().filter(|&&c| c == '\n').count() + 1;
    let sutun = match onceki.iter().rposition(|&c| c == '\n') {
        Some(k) => poz - k,
        None => poz + 1,
    };
    Some(format!("{ileti}: line {satir} column {sutun} (char {poz})"))
}

fn oserror(e: &std::io::Error, yol: &str) -> String {
    use std::io::ErrorKind::{NotFound, PermissionDenied};
    match e.kind() {
        NotFound => format!("[Errno 2] No such file or directory: {}", py::repr(yol)),
        PermissionDenied => format!("[Errno 13] Permission denied: {}", py::repr(yol)),
        _ => e.to_string(),
    }
}

fn bugun() -> String {
    chrono::Local::now().format("%Y-%m-%d").to_string()
}

pub fn kos(argv: &[String]) -> i32 {
    let ap = Ayrisan::yeni(
        "alan-ajani-dogur.py",
        Some(BELGE),
        vec![
            Secenek::bayrak(&["--kuru"], "kuru", None),
            Secenek::bayrak(&["--uzerine-yaz"], "uzerine_yaz", None),
            Secenek::deger(&["--tarih"], "tarih", None),
        ],
    )
    .konumsal("spec");
    let a = match ap.ayristir(argv) {
        Ok(a) => a,
        Err(k) => return k,
    };
    let tarih = a.metin("tarih").map(str::to_string).unwrap_or_else(bugun);
    let (kuru, uzerine) = (a.bayrak("kuru"), a.bayrak("uzerine_yaz"));
    let yol = a.konumsal().unwrap_or_default();
    let metin = match py::oku_kati(Path::new(yol)) {
        Ok(t) => t,
        Err(py::OkuHata::Io(e)) => {
            py::err(&format!("[HATA] spec okunamadı: {}\n", oserror(&e, yol)));
            return 1;
        }
        Err(py::OkuHata::Kod) => return py::coker(&format!("{yol}: UnicodeDecodeError")),
    };
    if let Some(h) = json_hata(&metin) {
        py::err(&format!("[HATA] spec okunamadı: {h}\n"));
        return 1;
    }
    let spec: Value = match serde_json::from_str(&metin) {
        Ok(v) => v,
        Err(e) => return py::coker(&format!("{yol}: JSON değeri işlenemedi: {e}")),
    };
    if !spec.is_object() && !spec.is_array() {
        return py::coker("spec kökü nesne değil");
    }
    for z in ["ajanlar", "model", "bakim_maliyeti", "karar"] {
        if spec.get(z).is_none() {
            py::err(&format!("[HATA] spec alanı eksik: {z}\n"));
            return 1;
        }
    }
    let y = yollar();
    if !Path::new(&y.iskelet).is_dir() {
        py::err(&format!("[HATA] şablon dizini yok: {}\n", y.iskelet));
        return 1;
    }
    let mut sayac = Sayac::default();
    let sonuc = ogren_ortak_hazirla(&y, uzerine, kuru, &mut sayac).and_then(|_| uret(&y, &spec, &tarih, uzerine, kuru, &mut sayac));
    if let Err(m) = sonuc {
        return match m.strip_prefix('\u{0}') {
            Some(cikis) => {
                py::err(&format!("{cikis}\n"));
                1
            }
            None => py::coker(&m),
        };
    }
    let (karar, n) = match (al_metin(&spec, "karar"), spec.get("ajanlar").and_then(Value::as_array)) {
        (Ok(k), Some(l)) => (k, l.len()),
        _ => return py::coker("spec alanları okunamadı"),
    };
    py::print(&format!(
        "\nALAN-AJANI-DOGUR {karar}: ajan {n} · dosya yeni {} · atlandı (var, farklı) {} · aynı {}{}",
        sayac.yeni,
        sayac.atlandi,
        sayac.ayni,
        if kuru { " · KURU" } else { "" }
    ));
    0
}
