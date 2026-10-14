//! `kapi-denetim.py`'nin birebir Rust karşılığı: skill-üretim kapı ağacının DETERMİNİSTİK kapıları
//! (K2-R referans-varlığı · K3-F1..F4 biçim · tür-özel bayraklar). Kural kaynağı: `core/skill-uretim-semasi.md`.
//! LLM'e bırakılan kapılar (K0/K1/K2-İ/K3-F5/şekil-FIRST) burada YOK; yalnız yapısal dış sinyal üretilir.
//!
//! Python betiğiyle bilinçli tek ayrım: Python'da `set` yineleme sırası süreç başına rastgeledir (uyarı sırası,
//! eksik `m.NN` sırası); burada bu iki liste sıralı verilir (belirlenimci). Fark testi bu iki listeyi sırasız karşılaştırır.
use regex::Regex;
use serde::Serialize;
use serde_json::Value;
use std::collections::{BTreeSet, HashMap};
use std::path::{Path, PathBuf};
use std::sync::LazyLock;

/// Argümansız çağrıda basılan kullanım metni (Python `__doc__` + `print` sonu).
const KULLANIM: &str = "kapi-denetim.py — Skill-üretim kapı-ağacının DETERMİNİSTİK kapıları (K2-R referans-varlığı · K3-F1..F4 biçim · tür-özel bayraklar).
Kural kaynağı: core/skill-uretim-semasi.md (v1, 2026-08-15). LLM'e bırakılan kapılar (K0/K1/K2-İ/K3-F5/şekil-FIRST) burada YOK — script yalnız
\"yapısal dış sinyal\"i üretir (C-YT3: kapı prompt'la kurulmaz). Kullanım:
    python3 kapi-denetim.py <skill-dizini|SKILL.md> [--json] [--repo <kök>]
Çıkış kodu: 0 = tüm SERT kapılar geçti · 1 = en az bir sert kapı düştü · 2 = kullanım hatası. Uyarılar (K) çıkış kodunu etkilemez.

";

const BUTCE_CHARS: usize = 7380;

fn rx(s: &str) -> Regex {
    Regex::new(s).unwrap_or_else(|e| panic!("regex derlenemedi {s:?}: {e}"))
}

macro_rules! rx_sabit {
    ($ad:ident, $s:expr) => {
        static $ad: LazyLock<Regex> = LazyLock::new(|| rx($s));
    };
}

rx_sabit!(RX_FM, r"(?s)^---\n(.*?)\n---\n?(.*)$");
rx_sabit!(RX_FM_ANAHTAR, r"^([A-Za-z_-]+):\s*(.*)$");
rx_sabit!(RX_NEG, r#"(?i)KULLANILMAZ|KULLANMA|kullanma[:;]|KULLANMAZ|kullanılmaz[:;]|Use when.*(?:not|don't)|DO NOT"#);
rx_sabit!(RX_BIRINCI, r"\b(ben|beni|bana|I can|I will|I help)\b");
rx_sabit!(RX_NEZAMAN, r"Tetik|tetik|dendiğinde|dediğinde|Kullan[: ]|Use when|ne zaman|WHEN");
rx_sabit!(RX_ADIM, r"(?m)^\s*\d+\.\s");
rx_sabit!(RX_MADDE, r"(?m)^\s*[-*]\s");
rx_sabit!(RX_GOTCHAS, r"(?mi)^#+\s*(Gotchas|Tuzaklar|Frenler|Dikkat)");
rx_sabit!(RX_DOSYA, r"`([^`\s]+?\.(?:md|py|sh|json|yaml|yml|d2|txt|svg))`");
rx_sabit!(RX_ATLA, r"YYYY|MM-DD|<|>|\*|\{|N\.md|-N\b|\.\.\.");
rx_sabit!(RX_TUZUK_MADDE, r"(?m)^(\d+)\.\s+\*\*");
rx_sabit!(RX_M_NN, r"\bm\.(\d+)[a-z]?\b");
rx_sabit!(RX_SKILL_ADI, r"`([a-z]+(?:-[a-z]+)+)`");
rx_sabit!(RX_SKILL_SONEK, r"-(kosum|kapisi|modeli|hatti|derleme|kaydet|ceviri|vardiya|kapanis|yaz|grill|acilis)$");
rx_sabit!(RX_NEG_BOL, r"(?i)KULLANILMAZ|KULLANMA[:;]|KULLANMAZ|kullanma[:;]|kullanılmaz[:;]");
rx_sabit!(RX_TIRELI, r"[a-z]+(?:-[a-z]+)+");
rx_sabit!(RX_R, r"(?i)ritüel|oturum[- ]?sınır|seans başı|seans bitimi|vardiya[- ]?(?:AÇILIŞ|KAPANIŞ|açılış|kapanış)|SessionStart|Stop hook|kadans");
rx_sabit!(RX_O, r"(?i)pipeline|orkestrat|alt-ajan|çocuk skill|zincir(?:le|i)|paralel araştırma|Workflow|uçtan uca");
rx_sabit!(
    RX_YAN_POS,
    r"(?i)commit atar|ayrı commit|commit'ler|commit eder|commit \+ push|git push|push'lar|publish|paylaş(?:ır|ım)|deftere .{0,15}yazar|kanon.{0,25}yazar|kapsül.{0,15}(?:tazele|günceller|yazar)|dosyaya yazar"
);
rx_sabit!(RX_YAN_NEG, r"commit yapmaz|commit atmaz|kanon yazmaz|yan-etki freni|dosya YAZMAZ|kaydetme/commit yapmaz");
rx_sabit!(RX_YAN_ISTISNA, r"commit atar|ayrı commit|git push|commit \+ push");
rx_sabit!(RX_M31, r"m\.31|Katman[- ]1|onay");
rx_sabit!(RX_BEYAN, r"Salih|beyan|m\.31|onay");
rx_sabit!(RX_PARALEL, r"(?i)paralellik|bağımsız .{0,20}mi|ortak (?:çıktı|üretim)");
rx_sabit!(RX_ZAMAN, r"(?i)zaman-?kayması|zaman yalnız sistem|selamlama .{0,30}zaman");
rx_sabit!(RX_COMMIT_YAPMAZ, r"commit yapmaz|commit atmaz|yan-etki freni|kaydetme/commit yapmaz|karar ALMA");

#[derive(Serialize)]
struct Kapi {
    id: String,
    ok: bool,
    hard: bool,
    msg: String,
}

#[derive(Serialize)]
struct Facets {
    hazine_desc_toplam: usize,
    hazine_skill_sayisi: usize,
    sekil_tahmini: String,
    yan_etki_faseti: bool,
    disable_model_invocation: String,
    context: String,
    user_invocable: String,
}

#[derive(Serialize)]
struct Rapor {
    skill: String,
    gates: Vec<Kapi>,
    warns: Vec<String>,
    facets: Facets,
    sonuc: String,
    dusen_sert_kapilar: Vec<String>,
}

/// Python metin-kipi okuma karşılığı: UTF-8 + evrensel satır sonu (`\r\n` ve `\r` → `\n`).
fn yukle(p: &Path) -> std::io::Result<String> {
    let b = std::fs::read(p)?;
    let s = String::from_utf8(b).map_err(|e| std::io::Error::new(std::io::ErrorKind::InvalidData, e))?;
    Ok(s.replace("\r\n", "\n").replace('\r', "\n"))
}

/// Python `str.splitlines()` karşılığı (sondaki boş satır üretmez).
fn py_splitlines(s: &str) -> Vec<&str> {
    let mut out = Vec::new();
    let mut bas = 0;
    let mut it = s.char_indices().peekable();
    while let Some((i, c)) = it.next() {
        if matches!(c, '\n' | '\r' | '\x0b' | '\x0c' | '\x1c' | '\x1d' | '\x1e' | '\u{85}' | '\u{2028}' | '\u{2029}') {
            out.push(&s[bas..i]);
            let mut son = i + c.len_utf8();
            if c == '\r' && matches!(it.peek(), Some((_, '\n'))) {
                it.next();
                son += 1;
            }
            bas = son;
        }
    }
    if bas < s.len() {
        out.push(&s[bas..]);
    }
    out
}

/// Python `str.strip()`: Unicode boşluk + `\x1c-\x1f`.
fn py_strip(s: &str) -> &str {
    s.trim_matches(|c: char| c.is_whitespace() || ('\x1c'..='\x1f').contains(&c))
}

/// Python `repr(str)` (liste yazımı için).
fn py_repr(s: &str) -> String {
    let tirnak = if s.contains('\'') && !s.contains('"') { '"' } else { '\'' };
    let mut o = String::new();
    o.push(tirnak);
    for c in s.chars() {
        match c {
            '\\' => o.push_str("\\\\"),
            '\n' => o.push_str("\\n"),
            '\r' => o.push_str("\\r"),
            '\t' => o.push_str("\\t"),
            c if c == tirnak => {
                o.push('\\');
                o.push(c);
            }
            c if c.is_control() => {
                let k = c as u32;
                if k <= 0xff {
                    o.push_str(&format!("\\x{k:02x}"));
                } else {
                    o.push_str(&format!("\\u{k:04x}"));
                }
            }
            c => o.push(c),
        }
    }
    o.push(tirnak);
    o
}

fn py_liste(l: &[String]) -> String {
    format!("[{}]", l.iter().map(|s| py_repr(s)).collect::<Vec<_>>().join(", "))
}

fn frontmatter(text: &str) -> (HashMap<String, String>, String) {
    let Some(m) = RX_FM.captures(text) else {
        return (HashMap::new(), text.to_string());
    };
    let mut fm: HashMap<String, String> = HashMap::new();
    let mut cur: Option<String> = None;
    for line in py_splitlines(&m[1]) {
        if let Some(km) = RX_FM_ANAHTAR.captures(line) {
            let k = km[1].to_string();
            fm.insert(k.clone(), py_strip(&km[2]).to_string());
            cur = Some(k);
        } else if let Some(k) = &cur
            && (line.starts_with(' ') || line.starts_with('\t'))
        {
            let eski = fm.get(k).cloned().unwrap_or_default();
            fm.insert(k.clone(), py_strip(&format!("{eski} {}", py_strip(line))).to_string());
        }
    }
    (fm, m[2].to_string())
}

/// Hazinedeki skill dizinleri (`<repo>/.claude/skills/*/SKILL.md`; nokta ile başlayanlar glob'da atlanır).
fn hazine_skilleri(repo: &str) -> Vec<(String, PathBuf)> {
    let kok = Path::new(repo).join(".claude").join("skills");
    let mut v = Vec::new();
    if let Ok(rd) = std::fs::read_dir(&kok) {
        for e in rd.flatten() {
            let ad = e.file_name().to_string_lossy().to_string();
            let f = e.path().join("SKILL.md");
            if !ad.starts_with('.') && f.is_file() {
                v.push((ad, f));
            }
        }
    }
    v.sort();
    v
}

/// Python `len()` karşılığı (JSON değeri için); uygunsuz türde hata.
fn py_len(v: &Value) -> Result<usize, String> {
    match v {
        Value::Array(a) => Ok(a.len()),
        Value::Object(o) => Ok(o.len()),
        Value::String(s) => Ok(s.chars().count()),
        _ => Err("object has no len()".into()),
    }
}

fn py_dogru(v: &Value) -> bool {
    match v {
        Value::Null => false,
        Value::Bool(b) => *b,
        Value::Number(n) => n.as_f64().is_some_and(|x| x != 0.0),
        Value::String(s) => !s.is_empty(),
        Value::Array(a) => !a.is_empty(),
        Value::Object(o) => !o.is_empty(),
    }
}

/// `[c for c in E.get('cases', []) if c.get('type') == tur]` uzunluğu
fn vaka_sayisi(e: &serde_json::Map<String, Value>, tur: &str) -> Result<usize, String> {
    match e.get("cases") {
        None => Ok(0),
        Some(Value::Array(a)) => {
            let mut n = 0;
            for c in a {
                let Value::Object(o) = c else { return Err("object has no attribute 'get'".into()) };
                if o.get("type").and_then(Value::as_str) == Some(tur) {
                    n += 1;
                }
            }
            Ok(n)
        }
        Some(v) if !v.is_null() && !py_dogru(v) => Ok(0),
        Some(_) => Err("object has no attribute 'get'".into()),
    }
}

/// `de.get(anahtar, [])` doğruysa onun uzunluğu, değilse `cases` tür sayısı.
fn tetik_sayisi(
    e: &serde_json::Map<String, Value>,
    de: &serde_json::Map<String, Value>,
    anahtar: &str,
    tur: &str,
) -> Result<usize, String> {
    match de.get(anahtar) {
        Some(v) if py_dogru(v) => py_len(v),
        _ => vaka_sayisi(e, tur),
    }
}

fn evals_kapilari(ev: &Path, gate: &mut impl FnMut(&str, bool, String, bool)) {
    let sonuc: Result<(usize, usize, usize), String> = (|| {
        let metin = yukle(ev).map_err(|e| e.to_string())?;
        let e: Value = serde_json::from_str(&metin).map_err(|e| e.to_string())?;
        let Value::Object(e) = e else { return Err("object has no attribute 'get'".into()) };
        let bos_liste = Value::Array(vec![]);
        let tests = match e.get("tests") {
            Some(v) => v,
            None => e.get("cases").unwrap_or(&bos_liste),
        };
        let nt = py_len(tests)?;
        let bos = serde_json::Map::new();
        let de = match e.get("description_eval") {
            None => &bos,
            Some(Value::Object(o)) => o,
            Some(_) => return Err("object has no attribute 'get'".into()),
        };
        let st = tetik_sayisi(&e, de, "should_trigger", "pozitif")?;
        let snt = tetik_sayisi(&e, de, "should_not_trigger", "negatif")?;
        Ok((nt, st, snt))
    })();
    match sonuc {
        Ok((nt, st, snt)) => {
            gate("F3a-eval-sayisi", nt >= 3, format!("evals: {nt} test (≥3)"), true);
            gate("F3b-description-eval", st >= 5 && snt >= 5, format!("should_trigger {st} / should_not {snt} (≥5+5)"), true);
        }
        Err(e) => gate("F3a-eval-sayisi", false, format!("evals.json okunamadı: {e}"), true),
    }
}

/// `references/` altında ikiden derin dizin yolları (os.walk, ad sırasıyla).
fn derin_dizinler(kok: &Path, derinlik: usize, out: &mut Vec<String>) {
    let Ok(rd) = std::fs::read_dir(kok) else { return };
    let mut ds: Vec<PathBuf> = rd.flatten().filter(|e| e.path().is_dir()).map(|e| e.path()).collect();
    ds.sort();
    for d in ds {
        if derinlik >= 1 {
            out.push(d.to_string_lossy().to_string());
        }
        derin_dizinler(&d, derinlik + 1, out);
    }
}

/// Betik mantığı: `argv` = `sys.argv[1:]`. Dönüş: (stdout metni, çıkış kodu).
pub fn denetle(argv: &[String]) -> (String, i32) {
    let args: Vec<&String> = argv.iter().filter(|a| !a.starts_with("--")).collect();
    let as_json = argv.iter().any(|a| a == "--json");
    let mut repo: Option<String> = None;
    if let Some(i) = argv.iter().position(|a| a == "--repo") {
        match argv.get(i + 1) {
            Some(v) => repo = Some(v.clone()),
            None => return ("HATA: --repo değeri eksik\n".into(), 1),
        }
    }
    let Some(target) = args.first() else { return (KULLANIM.to_string(), 2) };
    let skill_md = if target.ends_with("SKILL.md") { PathBuf::from(target) } else { Path::new(target.as_str()).join("SKILL.md") };
    if !skill_md.is_file() {
        return (format!("HATA: {} yok\n", skill_md.display()), 2);
    }
    let mutlak = std::path::absolute(&skill_md).unwrap_or(skill_md.clone());
    let skill_dir = mutlak.parent().map(Path::to_path_buf).unwrap_or_default();
    let skill_name = skill_dir.file_name().map(|s| s.to_string_lossy().to_string()).unwrap_or_default();
    let repo = match repo.filter(|r| !r.is_empty()) {
        Some(r) => r,
        None => {
            // .claude/skills/<n>/ → repo kökü üç üst
            let cand = skill_dir.ancestors().nth(3).map(Path::to_path_buf).unwrap_or_default();
            if cand.join(".claude").is_dir() {
                cand.to_string_lossy().to_string()
            } else {
                std::env::current_dir().map(|p| p.to_string_lossy().to_string()).unwrap_or_default()
            }
        }
    };

    let text = match yukle(&skill_md) {
        Ok(t) => t,
        Err(e) => return (format!("HATA: {} okunamadı: {e}\n", skill_md.display()), 1),
    };
    let (fm, body) = frontmatter(&text);
    let lines = py_splitlines(&text);
    let mut gates: Vec<Kapi> = Vec::new();
    let mut warns: Vec<String> = Vec::new();
    let mut gate = |id: &str, ok: bool, msg: String, hard: bool| gates.push(Kapi { id: id.into(), ok, hard, msg });
    let fm_al = |k: &str, varsayilan: &str| fm.get(k).cloned().unwrap_or_else(|| varsayilan.to_string());

    // ---------- K3-F1 description ----------
    let desc = fm_al("description", "");
    let n = desc.chars().count();
    gate("F1a-len", 0 < n && n <= 1024, format!("description {n} char (≤1024; platform kesme 1536)"), true);
    let neg = RX_NEG.is_match(&desc);
    gate("F1b-negatif-tetik", neg, format!("negatif tetik (KULLANILMAZ/KULLANMA) {}", if neg { "var" } else { "YOK" }), true);
    let third = !RX_BIRINCI.is_match(&desc);
    gate("F1c-3.sahis", third, format!("3. şahıs {}", if third { "✓" } else { "✗ (1. şahıs ifade)" }), true);
    let ne_zaman = RX_NEZAMAN.is_match(&desc);
    gate("F1d-ne-zaman", ne_zaman, format!("NE-ZAMAN (tetik tarifi) {}", if ne_zaman { "var" } else { "YOK" }), false);
    let mut tot = 0usize;
    let mut cnt = 0usize;
    for (_, f) in hazine_skilleri(&repo) {
        let t = std::fs::read(&f).map(|b| String::from_utf8_lossy(&b).replace("\r\n", "\n").replace('\r', "\n")).unwrap_or_default();
        let (fm2, _) = frontmatter(&t);
        tot += fm2.get("description").map_or(0, |d| d.chars().count());
        cnt += 1;
    }
    if tot > BUTCE_CHARS {
        // Karar 96 (Salih 09-15): hazine tavanı KALKTI; bu satır yalnız ölçümdür (engel/uyarı değil)
        gate(
            "F1e-hazine-butcesi",
            true,
            format!("hazine {cnt} skill / {tot} char (eski eşik {BUTCE_CHARS}; tavan kalktı Karar 96 — yalnız ölçüm, /context ile teyit)"),
            false,
        );
    } else {
        gate("F1e-hazine-butcesi", true, format!("hazine {cnt} skill / {tot} char ≤ {BUTCE_CHARS}"), false);
    }

    // ---------- K3-F2 gövde ----------
    let nl = lines.len();
    gate("F2a-satir", nl < 500, format!("gövde {nl} satır (<500)"), true);
    let refdir = skill_dir.join("references");
    let mut deep: Vec<String> = Vec::new();
    if refdir.is_dir() {
        derin_dizinler(&refdir, 0, &mut deep);
    }
    let deep_msg = if deep.is_empty() {
        "references ≤1 seviye".to_string()
    } else {
        format!("iç içe referans: {}", py_liste(&deep[..deep.len().min(2)]))
    };
    gate("F2b-referans-derinlik", deep.is_empty(), deep_msg, true);

    // ---------- K3-F3 evals ----------
    let ev = skill_dir.join("evals").join("evals.json");
    if ev.is_file() {
        evals_kapilari(&ev, &mut gate);
    } else {
        gate("F3a-eval-sayisi", false, "evals/evals.json YOK (eval-önce, K-016)".into(), true);
    }

    // ---------- K3-F4 adımlar + gotchas ----------
    let steps = RX_ADIM.find_iter(&body).count();
    let bullets = RX_MADDE.find_iter(&body).count();
    gate(
        "F4a-numarali-adim",
        steps >= 3 || bullets >= 5,
        format!("numaralı adım {steps} (≥3) ∨ checklist maddesi {bullets} (≥5)"),
        true,
    );
    let got = RX_GOTCHAS.is_match(&body);
    gate("F4b-gotchas", got, format!("Gotchas bölümü {}", if got { "var" } else { "YOK" }), true);

    // ---------- K2-R referans-varlığı ----------
    let mut missing: Vec<String> = Vec::new();
    let mut checked = 0usize;
    for m in RX_DOSYA.captures_iter(&text) {
        let p = &m[1];
        if RX_ATLA.is_match(p) || p.starts_with('~') || p.starts_with('/') || p.starts_with("C:") {
            continue;
        }
        checked += 1;
        if !(Path::new(&repo).join(p).exists() || skill_dir.join(p).exists()) {
            missing.push(p.to_string());
        }
    }
    let tuz = Path::new(&repo).join("core").join("tuzuk-v0.md");
    if tuz.is_file() {
        let arts: BTreeSet<String> =
            RX_TUZUK_MADDE.captures_iter(&yukle(&tuz).unwrap_or_default()).map(|c| c[1].to_string()).collect();
        let kullanilan: BTreeSet<String> = RX_M_NN.captures_iter(&text).map(|c| c[1].to_string()).collect();
        for a in kullanilan {
            checked += 1;
            if !arts.contains(&a) {
                missing.push(format!("m.{a} (tüzükte madde yok)"));
            }
        }
    }
    let skills: BTreeSet<String> = hazine_skilleri(&repo).into_iter().map(|(a, _)| a).collect();
    let tokenlar: BTreeSet<String> = RX_SKILL_ADI.captures_iter(&text).map(|c| c[1].to_string()).collect();
    for tok in tokenlar {
        if skills.contains(&tok) || tok == skill_name {
            continue;
        }
        if RX_SKILL_SONEK.is_match(&tok) {
            warns.push(format!("K2-R? `{tok}` skill adı gibi ama hazinede yok (referans mı, aday mı?)"));
        }
    }
    let eksik = if missing.is_empty() { "yok".to_string() } else { py_liste(&missing) };
    gate("R-referans-varligi", missing.is_empty(), format!("{checked} referans denetlendi; eksik: {eksik}"), true);

    // ---------- şekil tahmini (FIRST: R > O > Y > Ü) + tür-özel bayraklar ----------
    let d_all = format!("{desc} {body}");
    // yalnız pozitif tetik kısmı (negatif-tetik cümlesi şekil belirlemez)
    let d_pos = match RX_NEG_BOL.find(&desc) {
        Some(m) => &desc[..m.start()],
        None => desc.as_str(),
    };
    let d_shape = RX_TIRELI.replace_all(d_pos, " ");
    let is_r = RX_R.is_match(&d_shape);
    let is_o = RX_O.is_match(&d_shape);
    let yan_pos = RX_YAN_POS.is_match(&d_all);
    let yan_neg = RX_YAN_NEG.is_match(&d_all);
    let yan = yan_pos && !(yan_neg && !RX_YAN_ISTISNA.is_match(&d_all));
    let shape = if is_r {
        "T-R"
    } else if is_o {
        "T-O"
    } else if yan {
        "T-Y"
    } else {
        "T-Ü"
    };
    let facets = Facets {
        hazine_desc_toplam: tot,
        hazine_skill_sayisi: cnt,
        sekil_tahmini: shape.to_string(),
        yan_etki_faseti: yan,
        disable_model_invocation: fm_al("disable-model-invocation", "false"),
        context: fm_al("context", "ana"),
        user_invocable: fm_al("user-invocable", "true"),
    };
    if shape == "T-Y" {
        let ok = fm_al("disable-model-invocation", "").to_lowercase() == "true";
        gate(
            "TY-disable-model-invocation",
            ok,
            format!("yan-etkili birincil şekil → disable-model-invocation:true {}", if ok { "✓" } else { "EKSİK" }),
            true,
        );
        let ok31 = RX_M31.is_match(&d_all);
        gate("TY-m31", ok31, format!("m.31 kapısı/onay atfı {}", if ok31 { "var" } else { "YOK" }), false);
    }
    if (shape == "T-R" || shape == "T-O") && yan {
        let okb = RX_BEYAN.is_match(&d_all);
        gate("TRO-yan-etki-beyan", okb, format!("yan-etki adımı Salih-beyanına/m.31'e bağlı {}", if okb { "✓" } else { "YOK" }), true);
    }
    if shape == "T-O" {
        let okp = RX_PARALEL.is_match(&d_all);
        gate("TO-paralellik-uygunluk", okp, format!("paralellik-uygunluk sorusu {}", if okp { "var" } else { "YOK" }), false);
    }
    if shape == "T-R" {
        let okz = RX_ZAMAN.is_match(&d_all);
        gate("TR-zaman-freni", okz, format!("zaman-kayması freni {}", if okz { "var" } else { "YOK" }), false);
    }
    if shape == "T-Ü" {
        let okc = RX_COMMIT_YAPMAZ.is_match(&d_all);
        gate(
            "TU-commit-yapmaz",
            okc,
            format!("\"commit yapmaz / yan-etki freni\" beyanı {}", if okc { "var" } else { "YOK" }),
            false,
        );
    }

    let dusen: Vec<String> = gates.iter().filter(|g| g.hard && !g.ok).map(|g| g.id.clone()).collect();
    let sonuc = if dusen.is_empty() { "GEÇTİ" } else { "DÜŞTÜ" };
    let kod = if dusen.is_empty() { 0 } else { 1 };
    let r = Rapor { skill: skill_name.clone(), gates, warns, facets, sonuc: sonuc.into(), dusen_sert_kapilar: dusen };
    let mut o = String::new();
    if as_json {
        let mut buf = Vec::new();
        let bicim = serde_json::ser::PrettyFormatter::with_indent(b" ");
        let mut ser = serde_json::Serializer::with_formatter(&mut buf, bicim);
        r.serialize(&mut ser).expect("JSON yazımı");
        o.push_str(&String::from_utf8(buf).expect("UTF-8"));
        o.push('\n');
    } else {
        o.push_str(&format!("== {skill_name} — {sonuc} (şekil-tahmini {shape}; yan-etki {})\n", if yan { "var" } else { "yok" }));
        for g in &r.gates {
            let isaret = if g.ok { "✓" } else if g.hard { "✗" } else { "△" };
            o.push_str(&format!("  [{isaret}] {}: {}\n", g.id, g.msg));
        }
        for w in &r.warns {
            o.push_str(&format!("  [K] {w}\n"));
        }
    }
    (o, kod)
}
