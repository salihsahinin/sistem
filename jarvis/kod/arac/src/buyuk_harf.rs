//! `tools/buyuk-harf-temizle.py` karşılığı: "büyük harf = kod" kuralı temizliği (≥3 harfli büyük harf sözcükler → durum jetonu ya da kalın küçük harf).
//! Python'daki `(?<!…)`/`(?!…)` bakışlı `tok` deseni `regex` ile yazılamaz: `sonraki_eslesme` aynı eşleşmeyi elle üretir
//! (sözcük zinciri açgözlü; bitiş bakışı geçmezse zincirin son sözcüğü bırakılır, çünkü kısaltmanın başka hiçbir biçimi bakışı geçemez).
//! Çıkış: 0 (kuru: değişiklik listelendi / uygula: yazıldı) · 2 hata.
use crate::difflib;
use jarvis_hook::ortak::py_dumps;
use jarvis_rituel::argparse::{Ayrisan, Secenek};
use jarvis_rituel::{harness_anahtar, py};
use regex::Regex;
use serde_json::json;
use std::collections::HashSet;
use std::path::{Path, PathBuf};
use std::sync::LazyLock;

/// Değişmeyen kısaltmalar (beyaz liste).
const IZ: &str = r"AS-OF DAG MCP OWASP YAML JSON JSONL YML CSV HTML HTTP HTTPS PDF SVG PNG CI CD API SQL URL URI CLI GUI IDE SDK LLM RAG AXI GNHF OCR USD EUR TRY CV
HITL ASR NDCG MAP MRR GSM8K SWE UK AISI AWS DEA GCP MIT OCW README HEAD MEMORY CLAUDE JARVIS JARVİS FRIDAY CARVIS ATLAS OPUS SONNET HAIKU FABLE GPT KB MB GB
FIFO LIFO SHA UTC TR EN ID UID DNS TLS SSH OAUTH NEMO NLP ML AI ETL ELT DBT SPARK MLOPS LTR PR PRS CTR ROC AUC F1 REGEX BPE ROPE KV SFT RLHF CVE CVSS CWE UTF
İB EK SKILL SCRIPTLER KILAVUZ IAM DRFR NOOP CEO PC MAC VS UTF-8 SCD LUD OWL OBO SKOS SEMVER PEP RIPPLE DDQ DAMA NL GA ASCII OCR NLI RRF BM25 FTS SQLITE
COVE DAG CI/CD OKR KPI ROI SLA SLO SRE QA UX UI CSS JS TS PY SH MD TXT HTML5 LAVISH DAISYUI";
/// Durum jetonları: `JETON` olarak sarılır (başlıkta küçültülür).
const DURUM: &str = r"DONE PASS FAIL WARN ERROR TODO RED YOK RET KAPANDI AKTİF BEKLEYEN BLOKE BAYAT TAZE SÜPERSEDE EMEKLİ DÜŞTÜ SAĞLAM DARALDI FLAG SNAPSHOT DONDU KISMİ TUTTU İMZALANDI
DAYANAKSIZ DESTEKLİ ÇELİŞİR TEMİZ İHLAL RET ŞÜPHE YOK HATA ANALYZE KALAN BEKLET ONAR GEÇTİ YARIM PROBE PLAN TEACH CLOSE TODO DOĞRU
YANLIŞ ERTELENDİ SÜPERSEDE-EDİLDİ KAPALI DEVAM DURDU ONAYLI ONAYSIZ EKSİK PASİF HAZIR TAMAM YARIM-DONE";
/// İngilizce sözcükler: `I`→`i` (Türkçede `I`→`ı`).
const EN: &str = r"INDEX MEDIUM UNIQUE REGISTER LIKE AUTOMATIC JOIN FIRST DESCRIPTION IDK ORIGIN LIMIT INLINE IMPORT INPUT OUTPUT INSERT UPDATE
DELETE SELECT WHERE DISTINCT PRIMARY STRING INTEGER NULL TRUE FALSE PARTITION FILTER SPLIT HIGH LOW WIP LINK LIST LINE PIPELINE
SKILL SKILLS BUILD SHIP SCOUT SYNTHESIS REVIEW VERIFY COMMIT PUSH PULL MERGE BRANCH MAIN DIFF PATCH WORKTREE HOOK HOOKS SETTINGS
ENGINEERING MINING DRIFT RIPPLE EDIT EDITS WRITE READ LOSSLESS LOSSY ENCODING CODEC PRIORITY SURVIVORSHIP RESTRICT CASCADE
NOTIFICATION ISSUE ISSUES ARTIFACT CONTEXT WINDOW PROMPT PROMPTS SYSTEM ASSISTANT USER TOOL TOOLS AGENT AGENTS TRIGGER
WORKFLOW GUARDRAIL GUARDRAILS SANDBOX PERMISSION MEMORY THINKING FIRST-CLASS FAIL LOUD INDEXED IMC RUNTIME POINTER ESI
MISLEADING SUPERSEDED LICENSE DEFAULT PUBLIC PRIVATE ACTIVE DIRTY CLEAN";
/// Özel adlar: büyük harf sözcük → doğru yazım.
const OZEL: &[(&str, &str)] = &[
    ("SALİH", "Salih"),
    ("TÜRKÇE", "Türkçe"),
    ("İNGİLİZCE", "İngilizce"),
    ("FİNDER", "Finder"),
    ("GİTHUB", "GitHub"),
    ("ANTHROPİC", "Anthropic"),
    ("OBSİDİAN", "Obsidian"),
    ("COWORK", "Cowork"),
    ("KUN", "Kun"),
    ("CHEN", "Chen"),
    ("PORTRİSK", "PortRisk"),
    ("WİNDOWS", "Windows"),
    ("DOCKER", "Docker"),
];
/// `--help` açıklaması (Python `__doc__`, `RawDescriptionHelpFormatter`: aynen basılır).
const ACIKLAMA: &str = r#"buyuk-harf-temizle.py — "büyük harf = kod" kuralı temizliği (Salih 09-15 yan-görevi 2, onay "onay, önce kuru diff koş").
Kural: kanonda tamamı büyük harfli sözcük ya KISALTMADIR (beyaz liste, dokunulmaz) ya da backtick içinde makine-jetonudur
(`DONE`, `BAYAT`); vurgu yalnız kalın harftir. Kök neden: yüklenen bağlamda 1.590 caps sözcük (19-35‰), model çoğunluk üslubunu
taklit ediyor (rapor raporlar/2026-09/buyuk-harf-vurgu-analizi-2026-09-15.md + defter 09-15 hook arızası).

Sınıflar:  durum-jetonu (DURUM kümesi: KAPANDI, BAYAT, DONE, PROBE …) → `JETON`  ·  vurgu (geri kalan ≥4 harfli caps) → **küçük harf**
           (ardışık vurgu sözcükleri tek kalın span: "TEK SORU" → **tek soru**); YAML ön-blok satırlarında (description …) kalın işareti
           konmaz, yalnız küçültülür (kapi-denetim regex'leri `kullanma[:;]` biçimini arar).
Korunur:  kod blokları, satır-içi kod, URL, `aynen: "…"` Salih alıntıları, tire/alt-çizgi/nokta bitişik tanımlayıcılar, beyaz liste.
Kapsam:   --katman sicak (CLAUDE.md · core/*.md · .claude/skills/*/SKILL.md · .claude/rules/*.md · ~/.claude/CLAUDE.md · hafıza *.md)
          · ilik (+ KILAVUZ.md · wiki/*.md · .claude/skills/*/references/*.md · .claude/skills/README.md)
          · ogrenme (09-17: ogrenme/README+mufredat · <şerit>/README · ilerleme · dersler/*.md · *-seti/*.md — yan oturumun canlı bağlamı) · hepsi. Soğuk katman (raporlar/cc/arşiv) yazılmaz (tarihçe).
Kullanım: python3 tools/buyuk-harf-temizle.py [--katman sicak|ilik|hepsi] [--kuru] [--uygula] [--diff <yol>] [--goster N] [--json]
Çıkış:    0 (kuru: değişiklik listelendi / uygula: yazıldı) · 2 hata. Türkçe küçültme: İ→i, I→ı (Python lower() 'İ'yi bozar).
"#;

struct Desenler {
    kod_blok: Regex,
    satir_ici: Regex,
    url: Regex,
    aynen: Regex,
    pano: Regex,
    kart: Regex,
    baslik_onek: Regex,
    kelime: Regex,
}

/// Python `\s` `\x1c-\x1f` denetim karakterlerini de boşluk sayar (`str.isspace`); Rust `\s` saymaz: sınıfa elle eklendi.
static DESENLER: LazyLock<Desenler> = LazyLock::new(|| Desenler {
    kod_blok: Regex::new(r"(?s)```.*?```").unwrap(),
    satir_ici: Regex::new(r"`[^`\n]*`").unwrap(),
    url: Regex::new(r"https?://[^\s\x1c-\x1f]+").unwrap(),
    aynen: Regex::new(r#"aynen:?[\s\x1c-\x1f]*["“][^"”]*["”]"#).unwrap(),
    pano: Regex::new(r"(?m)^## (AKTİF|BEKLEYEN|BLOKE)[\s\x1c-\x1f]*$").unwrap(),
    kart: Regex::new(r"\*\*K-\d+[\s\x1c-\x1f]+KAPANDI[\s\x1c-\x1f]+\(").unwrap(),
    baslik_onek: Regex::new(r"\A#+[\s\x1c-\x1f]*(?:\d+\.[\s\x1c-\x1f]*)?\z").unwrap(),
    kelime: Regex::new(r"[\p{L}\p{N}]").unwrap(),
});
static IZ_KUMESI: LazyLock<HashSet<&'static str>> = LazyLock::new(|| IZ.split_whitespace().collect());
static DURUM_KUMESI: LazyLock<HashSet<&'static str>> = LazyLock::new(|| DURUM.split_whitespace().collect());
static EN_KUMESI: LazyLock<HashSet<&'static str>> = LazyLock::new(|| EN.split_whitespace().collect());

/// Python `re` `\w` (str): `str.isalnum()` ya da `_`.
fn kelime_mi(c: char) -> bool {
    if c.is_ascii() {
        return c.is_ascii_alphanumeric() || c == '_';
    }
    let mut tampon = [0u8; 4];
    DESENLER.kelime.is_match(c.encode_utf8(&mut tampon))
}

/// `TRLOW` çevirisi (İ→i, I→ı) ardından `str.lower()`.
fn tr_lower(s: &str) -> String {
    s.chars().map(|c| match c { 'İ' => 'i', 'I' => 'ı', c => c }).collect::<String>().to_lowercase()
}

/// `s[:1].upper() + s[1:]`.
fn ust_ilk(s: &str) -> String {
    let mut it = s.chars();
    match it.next() {
        Some(c) => c.to_uppercase().collect::<String>() + it.as_str(),
        None => String::new(),
    }
}

/// (bas, bit) bayt aralıkları: kod blokları, satır-içi kod, URL'ler, aynen alıntıları, pano başlıkları, kart kapanış satırı.
fn korunan_araliklar(metin: &str) -> Vec<(usize, usize)> {
    let d = &*DESENLER;
    let mut ar = vec![];
    for re in [&d.kod_blok, &d.satir_ici, &d.url, &d.aynen, &d.pano, &d.kart] {
        ar.extend(re.find_iter(metin).map(|m| (m.start(), m.end())));
    }
    ar
}

/// `yaml_satirlari`: YAML ön bloğundaki satır numaraları `0..sinir` (küme boşsa 0).
fn yaml_sinir(metin: &str) -> usize {
    if !metin.starts_with("---\n") {
        return 0;
    }
    match metin[4..].find("\n---") {
        Some(i) => metin[..4 + i].matches('\n').count() + 2,
        None => 0,
    }
}

fn sozcuk_cevir(w: &str) -> String {
    let (kok, ek) = match w.split_once('\'') {
        Some((k, e)) => (k, e),
        None => (w, ""),
    };
    let ek_metni = if ek.is_empty() { String::new() } else { format!("'{}", tr_lower(ek)) };
    if let Some((_, ozel)) = OZEL.iter().find(|(k, _)| *k == kok) {
        return format!("{ozel}{ek_metni}");
    }
    let parcalar: Vec<String> = kok
        .split('-')
        .map(|p| if EN_KUMESI.contains(p) && !p.chars().any(|c| "ÇĞİÖŞÜ".contains(c)) { p.to_lowercase() } else { tr_lower(p) })
        .collect();
    format!("{}{ek_metni}", parcalar.join("-"))
}

fn buyuk_mu(c: char) -> bool {
    matches!(c, 'A'..='Z' | 'Ç' | 'Ğ' | 'İ' | 'Ö' | 'Ş' | 'Ü')
}

/// `p`'den başlayarak ardışık büyük harf sayısı en çok `en_cok` olacak biçimde sayar: (bitiş, adet).
fn buyuk_say(m: &str, p: usize, en_cok: usize) -> (usize, usize) {
    let (mut q, mut n) = (p, 0);
    for c in m[p..].chars() {
        if n >= en_cok || !buyuk_mu(c) {
            break;
        }
        q += c.len_utf8();
        n += 1;
    }
    (q, n)
}

/// `W = [A-ZÇĞİÖŞÜ]{3,}(?:-[A-ZÇĞİÖŞÜ]{2,})*(?:'[A-ZÇĞİÖŞÜ]{1,4})?`: `bas`'tan açgözlü eşleşme, bitiş konumu.
fn sozcuk_bitis(m: &str, bas: usize) -> Option<usize> {
    let (mut p, n) = buyuk_say(m, bas, usize::MAX);
    if n < 3 {
        return None;
    }
    while m[p..].starts_with('-') {
        let (q, k) = buyuk_say(m, p + 1, usize::MAX);
        if k < 2 {
            break;
        }
        p = q;
    }
    if m[p..].starts_with('\'') {
        let (q, k) = buyuk_say(m, p + 1, 4);
        if k >= 1 {
            p = q;
        }
    }
    Some(p)
}

/// `(?!\w|[/\-_']|\.\w)` bitiş bakışı: `e` konumunda geçerse `true`.
fn bitis_gecer(m: &str, e: usize) -> bool {
    let mut it = m[e..].chars();
    match it.next() {
        None => true,
        Some(c) => !(kelime_mi(c) || matches!(c, '/' | '-' | '_' | '\'') || (c == '.' && it.next().is_some_and(kelime_mi))),
    }
}

/// `tok.finditer` bir sonraki eşleşmesi (`(?<![\w./\-*_'])W(?:[ ]W)*(?!\w|[/\-_']|\.\w)`), `ara`'dan başlayarak: (bas, bit).
fn sonraki_eslesme(m: &str, ara: usize) -> Option<(usize, usize)> {
    for (goreli, c) in m[ara..].char_indices() {
        if !buyuk_mu(c) {
            continue;
        }
        let a = ara + goreli;
        if let Some(onceki) = m[..a].chars().next_back()
            && (kelime_mi(onceki) || matches!(onceki, '.' | '/' | '-' | '*' | '_' | '\''))
        {
            continue;
        }
        let Some(ilk) = sozcuk_bitis(m, a) else { continue };
        let mut bitisler = vec![ilk];
        while m[*bitisler.last().unwrap()..].starts_with(' ') {
            match sozcuk_bitis(m, *bitisler.last().unwrap() + 1) {
                Some(e) => bitisler.push(e),
                None => break,
            }
        }
        let son = bitisler.len() - 1;
        if bitis_gecer(m, bitisler[son]) {
            return Some((a, bitisler[son]));
        }
        if son > 0 {
            return Some((a, bitisler[son - 1]));
        }
    }
    None
}

#[derive(Default)]
struct Say {
    vurgu: usize,
    durum: usize,
}

fn grup_bosalt(grup: &mut Vec<&str>, parcalar: &mut Vec<String>, say: &mut Say, baslik_basi: bool, duz: bool) {
    if grup.is_empty() {
        return;
    }
    let mut s = grup.iter().map(|w| sozcuk_cevir(w)).collect::<Vec<_>>().join(" ");
    if baslik_basi {
        s = ust_ilk(&s);
    }
    parcalar.push(if duz { s } else { format!("**{s}**") });
    say.vurgu += grup.len();
    grup.clear();
}

fn donustur(metin: &str, say: &mut Say) -> String {
    let d = &*DESENLER;
    let ar = korunan_araliklar(metin);
    let yaml_son = yaml_sinir(metin);
    let satir_bas: Vec<usize> = std::iter::once(0).chain(metin.match_indices('\n').map(|(i, _)| i + 1)).collect();
    let satir_no = |pos: usize| satir_bas.partition_point(|&x| x <= pos) - 1;
    let korunur = |a: usize, b: usize| ar.iter().any(|&(x, y)| x <= a && b <= y);
    let mut out = String::with_capacity(metin.len());
    let mut i = 0;
    let mut ara = 0;
    while let Some((a, b)) = sonraki_eslesme(metin, ara) {
        ara = b;
        if korunur(a, b) {
            continue;
        }
        let kelimeler: Vec<&str> = metin[a..b].split(' ').collect();
        let sb = metin[..a].rfind('\n').map_or(0, |x| x + 1);
        let satir_son = metin[a..].find('\n').map_or(metin.len(), |x| a + x);
        let satir = &metin[sb..satir_son];
        let kalin_ic = metin[sb..a].matches("**").count() % 2 == 1;
        let baslik = satir.trim_start_matches(py::bosluk_mu).starts_with('#');
        let duz = kalin_ic || baslik || satir_no(a) < yaml_son;
        let baslik_basi = baslik && d.baslik_onek.is_match(&metin[sb..a]);
        let mut parcalar: Vec<String> = vec![];
        let mut grup: Vec<&str> = vec![];
        let mut degisti = false;
        for w in kelimeler {
            let kok = w.split('\'').next().unwrap_or("");
            if IZ_KUMESI.contains(kok) {
                grup_bosalt(&mut grup, &mut parcalar, say, baslik_basi, duz);
                parcalar.push(w.to_string());
            } else if DURUM_KUMESI.contains(kok) && !baslik {
                grup_bosalt(&mut grup, &mut parcalar, say, baslik_basi, duz);
                parcalar.push(format!("`{w}`"));
                say.durum += 1;
                degisti = true;
            } else if DURUM_KUMESI.contains(kok) && baslik {
                grup_bosalt(&mut grup, &mut parcalar, say, baslik_basi, duz);
                let mut s = tr_lower(w);
                if baslik_basi {
                    s = ust_ilk(&s);
                }
                parcalar.push(s);
                say.durum += 1;
                degisti = true;
            } else {
                grup.push(w);
                degisti = true;
            }
        }
        grup_bosalt(&mut grup, &mut parcalar, say, baslik_basi, duz);
        if !degisti {
            continue;
        }
        out.push_str(&metin[i..a]);
        out.push_str(&parcalar.join(" "));
        i = b;
    }
    out.push_str(&metin[i..]);
    out
}

// ---------------------------------------------------------------- yol/glob (pathlib)

/// `str(pathlib.PurePath(p))`: Windows'ta `/` → `\`; kopya/`.` parçaları ve sondaki ayraç atılır (kök korunur); boş yol `.` olur.
pub(crate) fn pathlib_metni(p: &str) -> String {
    let t = if cfg!(windows) { p.replace('/', "\\") } else { p.to_string() };
    let (surucu, geri) = py::splitdrive(&t);
    let kokte = geri.starts_with(py::SEP);
    let govde: Vec<&str> = geri.split(py::SEP).filter(|x| !x.is_empty() && *x != ".").collect();
    let r = format!("{surucu}{}{}", if kokte { py::SEP.to_string() } else { String::new() }, govde.join(&py::SEP.to_string()));
    if r.is_empty() { ".".to_string() } else { r }
}

/// `Path.home()`: `~` genişletilemezse Python `RuntimeError` verir.
fn ev_dizini() -> Option<String> {
    let e = py::expanduser("~");
    if e.starts_with('~') { None } else { Some(pathlib_metni(&e)) }
}

/// `Path.resolve()`: gerçek yol (Windows'ta `\\?\` öneki atılır); olmayan yol mutlak+normal biçime düşer.
pub(crate) fn cozumle(p: &Path) -> PathBuf {
    match std::fs::canonicalize(p) {
        Ok(c) => {
            let s = c.to_string_lossy().into_owned();
            if let Some(r) = s.strip_prefix(r"\\?\UNC\") {
                PathBuf::from(format!(r"\\{r}"))
            } else if let Some(r) = s.strip_prefix(r"\\?\") {
                PathBuf::from(r.to_string())
            } else {
                c
            }
        }
        Err(_) => PathBuf::from(py::abspath(&p.to_string_lossy())),
    }
}

/// `fnmatch.translate` (yalnız `*` jokeri); Windows'ta büyük/küçük harf duyarsız.
fn joker_uyar(desen: &str, ad: &str) -> bool {
    let (desen, ad) = if cfg!(windows) { (desen.to_lowercase(), ad.to_lowercase()) } else { (desen.to_string(), ad.to_string()) };
    let parcalar: Vec<&str> = desen.split('*').collect();
    if parcalar.len() == 1 {
        return ad == desen;
    }
    let Some(mut kalan) = ad.strip_prefix(parcalar[0]) else { return false };
    let son = parcalar[parcalar.len() - 1];
    for orta in &parcalar[1..parcalar.len() - 1] {
        match kalan.find(orta) {
            Some(i) => kalan = &kalan[i + orta.len()..],
            None => return false,
        }
    }
    kalan.ends_with(son)
}

/// `pathlib.Path.glob` (3.11) için desen parçaları: ara parçalar dizin olmalı; `*` içeren parça dizin taranır, aksi hâlde adla aranır.
fn glob_dizin(dizin: &Path, parcalar: &[&str], sonuc: &mut Vec<PathBuf>) {
    let Some((ilk, kalan)) = parcalar.split_first() else { return };
    if !dizin.is_dir() {
        return;
    }
    let son = kalan.is_empty();
    if !ilk.contains('*') {
        let yol = dizin.join(ilk);
        if son {
            if yol.exists() {
                sonuc.push(yol);
            }
        } else if yol.is_dir() {
            glob_dizin(&yol, kalan, sonuc);
        }
        return;
    }
    let Ok(rd) = std::fs::read_dir(dizin) else { return };
    for e in rd.flatten() {
        let ad = e.file_name().to_string_lossy().into_owned();
        let yol = dizin.join(&ad);
        if !son && !yol.is_dir() {
            continue;
        }
        if joker_uyar(ilk, &ad) {
            if son {
                sonuc.push(yol);
            } else {
                glob_dizin(&yol, kalan, sonuc);
            }
        }
    }
}

/// `sorted(yollar)`: `Path` karşılaştırması parça parça yapılır (Windows'ta küçük harfe katlanır).
pub(crate) fn pathlib_sirala(yollar: &mut [PathBuf]) {
    yollar.sort_by_cached_key(|p| {
        p.components()
            .map(|c| {
                let s = c.as_os_str().to_string_lossy().into_owned();
                if cfg!(windows) { s.to_lowercase() } else { s }
            })
            .collect::<Vec<String>>()
    });
}

/// `sorted(kok.glob(desen))`.
fn glob_sirali(kok: &Path, desen: &str) -> Vec<PathBuf> {
    let mut sonuc = vec![];
    let parcalar: Vec<&str> = desen.split('/').collect();
    glob_dizin(kok, &parcalar, &mut sonuc);
    pathlib_sirala(&mut sonuc);
    sonuc
}

fn dosyalar(repo: &Path, katman: &str, ev: &str) -> Vec<PathBuf> {
    let yol = |taban: &Path, parcalar: &[&str]| parcalar.iter().fold(taban.to_path_buf(), |y, p| y.join(p));
    let skills = yol(repo, &[".claude", "skills"]);
    let sicak = || -> Vec<PathBuf> {
        let mut v = vec![repo.join("CLAUDE.md"), yol(Path::new(ev), &[".claude", "CLAUDE.md"])];
        v.extend(glob_sirali(&repo.join("core"), "*.md"));
        v.extend(glob_sirali(&skills, "*/SKILL.md"));
        v.extend(glob_sirali(&yol(repo, &[".claude", "rules"]), "*.md"));
        v.extend(glob_sirali(Path::new(&harness_anahtar::memory_dizin()), "*.md"));
        v
    };
    let ilik = || -> Vec<PathBuf> {
        let mut v = vec![repo.join("KILAVUZ.md"), yol(&skills, &["README.md"])];
        v.extend(glob_sirali(&repo.join("wiki"), "*.md"));
        v.extend(glob_sirali(&skills, "*/references/*.md"));
        v.extend(glob_sirali(&skills, "*/*.md"));
        v
    };
    let ogrenme = || -> Vec<PathBuf> {
        let og = repo.join("ogrenme");
        let mut v = vec![og.join("README.md"), og.join("mufredat.md")];
        for desen in ["*/README.md", "*/ilerleme.md", "*/dersler/*.md", "*/*-eval-seti/*.md", "*/*-seti/*.md"] {
            v.extend(glob_sirali(&og, desen));
        }
        v
    };
    let sec = match katman {
        "sicak" => sicak(),
        "ilik" => ilik(),
        "ogrenme" => ogrenme(),
        _ => [sicak(), ilik(), ogrenme()].concat(),
    };
    let mut gorulen: HashSet<String> = HashSet::new();
    let mut res = vec![];
    for p in sec {
        if !p.exists() {
            continue;
        }
        let anahtar = cozumle(&p).to_string_lossy().into_owned();
        let anahtar = if cfg!(windows) { anahtar.to_lowercase() } else { anahtar };
        if gorulen.insert(anahtar) {
            res.push(p);
        }
    }
    res
}

struct Rapor {
    dosya: String,
    vurgu: usize,
    durum: usize,
}

pub fn kos(argv: &[String]) -> i32 {
    // `default=str(Path.home() / ...)`: ayrıştırıcı kurulurken değerlendirilir, ev dizini yoksa `-h` dahil çöker
    let Some(ev) = ev_dizini() else { return py::coker("Could not determine home directory.") };
    let varsayilan_repo = format!("{ev}{}sistem{}jarvis", py::SEP, py::SEP);
    let ayrisan = Ayrisan::yeni(
        "buyuk-harf-temizle.py",
        Some(ACIKLAMA),
        vec![
            Secenek::deger(&["--repo"], "repo", None),
            Secenek::deger(&["--katman"], "katman", None).secimli(&["sicak", "ilik", "ogrenme", "hepsi"]),
            Secenek::bayrak(&["--kuru"], "kuru", None),
            Secenek::bayrak(&["--uygula"], "uygula", None),
            Secenek::deger(&["--diff"], "diff", None),
            Secenek::tam(&["--goster"], "goster", None),
            Secenek::bayrak(&["--json"], "json", None),
        ],
    );
    let a = match ayrisan.ayristir(argv) {
        Ok(a) => a,
        Err(k) => return k,
    };
    let repo = cozumle(Path::new(&pathlib_metni(&py::expanduser(a.metin("repo").unwrap_or(&varsayilan_repo)))));
    let (kuru, uygula) = (a.bayrak("kuru"), a.bayrak("uygula"));
    if uygula == kuru {
        py::err("--kuru ya da --uygula (tam biri)\n");
        return 2;
    }
    let katman = a.metin("katman").unwrap_or("sicak");
    let diff_yolu = a.metin("diff").unwrap_or("");
    let goster = a.tam("goster").unwrap_or(6);
    let (mut toplam_vurgu, mut toplam_durum) = (0usize, 0usize);
    let mut rapor: Vec<Rapor> = vec![];
    let mut diff_metin = String::new();
    for p in dosyalar(&repo, katman, &ev) {
        let Ok(eski) = py::oku_kati(&p) else { continue };
        let mut say = Say::default();
        let yeni = donustur(&eski, &mut say);
        if yeni == eski {
            continue;
        }
        let rel = p.to_string_lossy().replace(&ev, "~");
        toplam_vurgu += say.vurgu;
        toplam_durum += say.durum;
        rapor.push(Rapor { dosya: rel.clone(), vurgu: say.vurgu, durum: say.durum });
        diff_metin.push_str(&difflib::unified_diff(&difflib::splitlines_keepends(&eski), &difflib::splitlines_keepends(&yeni), &rel, &rel, 0).concat());
        if uygula
            && let Err(e) = std::fs::write(&p, &yeni)
        {
            return py::coker(&format!("{}: {e}", p.display()));
        }
    }
    if !diff_yolu.is_empty() {
        let dp = Path::new(diff_yolu);
        if let Some(ust) = dp.parent()
            && let Err(e) = std::fs::create_dir_all(ust)
        {
            return py::coker(&format!("{}: {e}", ust.display()));
        }
        if let Err(e) = std::fs::write(dp, &diff_metin) {
            return py::coker(&format!("{diff_yolu}: {e}"));
        }
    }
    if a.bayrak("json") {
        let dosyalar: Vec<serde_json::Value> = rapor.iter().map(|r| json!({"dosya": r.dosya, "vurgu": r.vurgu, "durum": r.durum})).collect();
        py::print(&py_dumps(&json!({
            "katman": katman, "mod": if uygula { "uygula" } else { "kuru" }, "dosya": rapor.len(),
            "vurgu": toplam_vurgu, "durum": toplam_durum, "dosyalar": dosyalar, "diff": diff_yolu,
        })));
        return 0;
    }
    let diff_ek = if diff_yolu.is_empty() { String::new() } else { format!(" · diff {diff_yolu}") };
    py::print(&format!(
        "BÜYÜK-HARF TEMİZLİK · {katman} · {} · dosya {} · vurgu→kalın {toplam_vurgu} · durum→`jeton` {toplam_durum}{diff_ek}",
        if uygula { "UYGULANDI" } else { "kuru" },
        rapor.len()
    ));
    let mut sirali: Vec<&Rapor> = rapor.iter().collect();
    sirali.sort_by_key(|r| std::cmp::Reverse(r.vurgu + r.durum));
    for r in sirali.iter().take(40) {
        py::print(&format!("  {:4}  (vurgu {}, durum {})  {}", r.vurgu + r.durum, r.vurgu, r.durum, r.dosya));
    }
    if rapor.len() > 40 {
        py::print(&format!("  … +{} dosya", rapor.len() - 40));
    }
    let adaylar: Vec<String> =
        py::splitlines(&diff_metin).into_iter().filter(|l| (l.starts_with('-') || l.starts_with('+')) && !l.starts_with("---") && !l.starts_with("+++")).collect();
    // `liste[: 2 * goster]`: negatif sınır sondan atar
    let sinir = 2 * goster;
    let adet = if sinir >= 0 { (sinir as usize).min(adaylar.len()) } else { adaylar.len().saturating_sub(sinir.unsigned_abs() as usize) };
    if adet > 0 {
        py::print("  örnek satırlar:");
        for l in &adaylar[..adet] {
            py::print(&format!("    {}", py::ilk(l, 160)));
        }
    }
    0
}
