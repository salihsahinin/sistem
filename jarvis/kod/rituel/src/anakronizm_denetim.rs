//! `tools/anakronizm-denetim.py` karşılığı: ANAKRONİZM FRENİ deterministik denetimi (Karar 68; "sistemde anakronizm YASAK").
//! Üç denetim: D1 zaman-çivi (paragraf kapsamı) · D2 damga-varlığı (ilk 12 satır) · D3 bayatlık (en yeni damga yaşı > eşik).
//! Çıkış: 0 temiz · 3 D1 İHLAL ∨ D2 var (D3 yalnız kuyruk) · 2 git repo yok · 1 Python'da yakalanmamış istisna olacak durumlar.
//!
//! Python `re` (Unicode + IGNORECASE) anlamı `fancy_regex` ile birebir kurulur (bkz. `py_desen`): `\b` ve `\w` Python'da
//! `isalnum() ∨ _`'dir (Rust `\w` birleştirici işaretleri de sayar) → `\b` açık bakış-ilişkileriyle yazılır; `\s` Python'da
//! `\x1c-\x1f` da içerir; IGNORECASE'de `i`/`I`/`ı`/`İ` denktir (Rust tek-karakter katlamasında değil) ve `[a-z]` sınıfı
//! `ı İ ſ K` karakterlerini de yakalar.
use crate::argparse::{Ayrisan, Secenek};
use crate::harness_anahtar;
use crate::py::{self, iso_tarih};
use chrono::{Datelike, Days, FixedOffset, NaiveDate, Utc};
use fancy_regex::Regex;
use jarvis_hook::ortak::{py_dumps, py_truthy};
use serde_json::{Map, Value, json};
use std::io::Write;
use std::path::Path;
use std::process::{Command, Stdio};
use std::sync::LazyLock;

const ZAMAN_CIVI: [&str; 18] = [
    r"\bşu an(da)?\b", r"\bşimdilik\b", r"\bhâlâ\b", r"\bhala\b", r"\bartık\b", r"\bhenüz\b", r"\byakında\b", r"\bson zamanlarda\b",
    r"\ben güncel\b", r"\ben güçlü\b", r"\ben son sürüm\b", r"\ben yeni\b", r"\bbugün itibar[ıi]yla\b", r"\bbu yazının yazıldığı\b",
    r"\byeni sürüm\b", r"\bdesteklenmiyor\b", r"\bresmî sdk'?s[ıi] yok\b", r"\bhenüz yok\b",
];
const SURUM_SKOR: [&str; 4] = [
    r"\bv\d+\.\d+(\.\d+)?\b",
    r"\bsürüm\s*\d",
    r"\bpass@\d+\b",
    r"\b(?:skor|doğruluk|recall|nDCG|F1|başarı)\S*\s*[:=]?\s*%?\s?\d{1,3}(?:,\d+)?\s?%?",
];
const TARIH: [&str; 11] = [
    r"\b\d{4}-\d{2}(-\d{2})?\b",
    r"\bAS-?OF\b",
    r"\bas of\b",
    r"\bçekim(?:i)?\s*(?:tarihi)?\s*\d{4}",
    r"\bson[- ]teyit\b",
    r"\bKayıt:\s*\d{4}",
    r"\b\d{2}-\d{2}\b(?=[^\d])",
    r"\b(?:0?[1-9]|1[0-2])[-/]\d{4}\b",
    r"\b(?:Ocak|Şubat|Mart|Nisan|Mayıs|Haziran|Temmuz|Ağustos|Eylül|Ekim|Kasım|Aralık)\s+\d{4}\b",
    r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+'?\d{2,4}\b",
    r"\b20\d{2}\b",
];
const DAMGA: &str = r"\b(\d{4}-\d{2}-\d{2})\b";

const KELVIN: char = '\u{212a}';
/// Python `\w` = `str.isalnum() ∨ _`
const KELIME: &str = r"[\p{L}\p{N}_]";

/// Python desenini (`re.U`, isteğe bağlı `re.I`) Rust (fancy-regex) karşılığına çevirir; kaçış dizileri (`\b \s \S`) ve sınıflar ayrıştırılır.
fn py_desen(desen: &str, ci: bool) -> String {
    let sinir = format!("(?:(?<={KELIME})(?!{KELIME})|(?<!{KELIME})(?={KELIME}))");
    let bosluk = r"\s\x1c-\x1f";
    let mut o = String::new();
    if ci {
        o.push_str("(?i)");
    }
    let c: Vec<char> = desen.chars().collect();
    let (mut i, mut sinifta) = (0, false);
    while i < c.len() {
        let k = c[i];
        match k {
            '\\' if i + 1 < c.len() => {
                match c[i + 1] {
                    'b' => o.push_str(&sinir),
                    's' => o.push_str(&format!("[{bosluk}]")),
                    'S' => o.push_str(&format!("[^{bosluk}]")),
                    d => {
                        o.push('\\');
                        o.push(d);
                    }
                }
                i += 2;
                continue;
            }
            '[' if !sinifta => {
                sinifta = true;
                o.push(k);
            }
            ']' if sinifta => {
                sinifta = false;
                o.push(k);
            }
            'i' | 'I' | 'ı' | 'İ' if ci => {
                if sinifta {
                    o.push_str("iIİı");
                } else {
                    o.push_str("[iIİı]");
                }
            }
            'a' if ci && sinifta && c[i..].starts_with(&['a', '-', 'z']) => {
                o.push_str("a-z");
                o.push_str(&format!("ıİſ{KELVIN}"));
                i += 3;
                continue;
            }
            _ => o.push(k),
        }
        i += 1;
    }
    o
}

fn derle(liste: &[&str], ci: bool) -> Regex {
    Regex::new(&py_desen(&liste.join("|"), ci)).expect("desen")
}

static RX_CIVI: LazyLock<Regex> = LazyLock::new(|| derle(&ZAMAN_CIVI, true));
static RX_SURUM: LazyLock<Regex> = LazyLock::new(|| derle(&SURUM_SKOR, true));
static RX_TARIH: LazyLock<Regex> = LazyLock::new(|| derle(&TARIH, true));
static RX_DAMGA: LazyLock<Regex> = LazyLock::new(|| derle(&[DAMGA], false));

/// Python'da yakalanmamış istisna → `py::coker`
type Sn<T> = Result<T, String>;

fn rx_hata(e: fancy_regex::Error) -> String {
    format!("re: {e}")
}

fn ara<'a>(rx: &Regex, m: &'a str) -> Sn<Option<&'a str>> {
    Ok(rx.find(m).map_err(rx_hata)?.map(|x| x.as_str()))
}

// ---------------------------------------------------------------- tarih (Python `datetime.date`)
fn iso(t: NaiveDate) -> String {
    t.format("%Y-%m-%d").to_string()
}

// ---------------------------------------------------------------- bulgu
struct Bulgu {
    denetim: &'static str,
    /// D1'de açık (`İHLAL`/`UYARI`); D2/D3'te `None` → sonradan `setdefault` (D2: İHLAL, D3: KUYRUK)
    seviye: Option<&'static str>,
    dosya: String,
    satir: i64,
    kalip: String,
    ornek: String,
    yas_gun: Option<i64>,
    not: &'static str,
}

impl Bulgu {
    fn seviye(&self) -> &'static str {
        self.seviye.unwrap_or(if self.denetim == "D2" { "İHLAL" } else { "KUYRUK" })
    }

    /// Python sözlük sırası: D1 `seviye` baştan; D2/D3 `seviye` en sonda (`setdefault`).
    fn harita(&self, ts: &str, head: &str, kosum_id: &str) -> Value {
        let mut m = Map::new();
        m.insert("denetim".into(), json!(self.denetim));
        if let Some(s) = self.seviye {
            m.insert("seviye".into(), json!(s));
        }
        m.insert("dosya".into(), json!(self.dosya));
        m.insert("satir".into(), json!(self.satir));
        m.insert("kalip".into(), json!(self.kalip));
        m.insert("ornek".into(), json!(self.ornek));
        m.insert("yas_gun".into(), json!(self.yas_gun));
        m.insert("not".into(), json!(self.not));
        m.insert("ts".into(), json!(ts));
        m.insert("kod_sha".into(), json!(head));
        m.insert("kosum_id".into(), json!(kosum_id));
        if self.seviye.is_none() {
            m.insert("seviye".into(), json!(self.seviye()));
        }
        Value::Object(m)
    }
}

// ---------------------------------------------------------------- denetimler
/// Paragraf = boş satırla ayrılan blok; kod blokları (```) atlanır. (başlangıç satır no, metin).
fn paragraflar(metin: &str) -> Vec<(i64, String)> {
    let (mut out, mut buf, mut bas, mut kod): (Vec<(i64, String)>, Vec<&str>, i64, bool) = (vec![], vec![], 1, false);
    for (i, satir) in metin.split('\n').enumerate() {
        let i = i as i64 + 1;
        if py::strip(satir).starts_with("```") {
            kod = !kod;
            continue;
        }
        if kod {
            continue;
        }
        if py::strip(satir).is_empty() {
            if !buf.is_empty() {
                out.push((bas, buf.join("\n")));
                buf.clear();
            }
            bas = i + 1;
        } else {
            if buf.is_empty() {
                bas = i;
            }
            buf.push(satir);
        }
    }
    if !buf.is_empty() {
        out.push((bas, buf.join("\n")));
    }
    out
}

fn d1_zaman_civi(yol: &str, metin: &str) -> Sn<Vec<Bulgu>> {
    let mut bulgular = vec![];
    for (bas, p) in paragraflar(metin) {
        if p.trim_start_matches(py::bosluk_mu).starts_with("|---") {
            continue;
        }
        let civi = ara(&RX_CIVI, &p)?;
        let surum = ara(&RX_SURUM, &p)?;
        if civi.is_none() && surum.is_none() {
            continue;
        }
        if RX_TARIH.is_match(&p).map_err(rx_hata)? {
            continue;
        }
        let m = surum.or(civi).unwrap_or("");
        bulgular.push(Bulgu {
            denetim: "D1",
            seviye: Some(if surum.is_some() { "İHLAL" } else { "UYARI" }),
            dosya: yol.to_string(),
            satir: bas,
            kalip: m.to_string(),
            ornek: py::ilk(&py::strip(&p).replace('\n', " "), 160),
            yas_gun: None,
            not: if surum.is_some() { "sürüm/skor iddiası, paragrafta tarih/AS-OF yok" } else { "zaman-çivi sözcüğü, paragrafta tarih yok (uyarı)" },
        });
    }
    Ok(bulgular)
}

fn d2_damga_varligi(yol: &str, metin: &str) -> Sn<Vec<Bulgu>> {
    let bas = metin.split('\n').take(12).collect::<Vec<_>>().join("\n");
    if RX_TARIH.is_match(&bas).map_err(rx_hata)? {
        return Ok(vec![]);
    }
    Ok(vec![Bulgu {
        denetim: "D2",
        seviye: None,
        dosya: yol.to_string(),
        satir: 1,
        kalip: "-".into(),
        ornek: py::ilk(&py::strip(&bas).replace('\n', " "), 120),
        yas_gun: None,
        not: "ilk 12 satırda tarih damgası yok",
    }])
}

/// Bronz `veri/bronz/cekim-olay.jsonl` → {dosya_id: en yeni cekim_tarihi}; dosya yoksa boş.
fn cekim_olaylari(repo: &str) -> Sn<std::collections::HashMap<String, NaiveDate>> {
    let mut out = std::collections::HashMap::new();
    let yol = py::join(&py::join(&py::join(repo, "veri"), "bronz"), "cekim-olay.jsonl");
    if !Path::new(&yol).exists() {
        return Ok(out);
    }
    let metin = match py::oku_kati(Path::new(&yol)) {
        Ok(m) => m,
        Err(py::OkuHata::Io(e)) => return Err(format!("OSError: {yol}: {e}")),
        Err(py::OkuHata::Kod) => return Err(format!("UnicodeDecodeError: {yol}")),
    };
    for line in metin.split('\n') {
        let line = py::strip(line);
        if line.is_empty() || line.starts_with('#') {
            continue;
        }
        let Ok(o) = serde_json::from_str::<Value>(line) else { continue };
        let Value::Object(o) = o else { return Err("AttributeError: JSON satırı nesne değil (.get yok)".into()) };
        let ham = o.get("cekim_tarihi").filter(|v| py_truthy(v));
        let t = match ham {
            None => None,
            Some(Value::String(s)) => iso_tarih(&py::ilk(s, 10)),
            Some(_) => return Err("TypeError: cekim_tarihi dize değil".into()),
        };
        let Some(t) = t else { continue };
        let Some(d) = o.get("dosya_id").filter(|v| py_truthy(v)) else { continue };
        match d {
            Value::String(d) => {
                if out.get(d).is_none_or(|e| t > *e) {
                    out.insert(d.clone(), t);
                }
            }
            Value::Array(_) | Value::Object(_) => return Err("TypeError: unhashable type".into()),
            _ => {}
        }
    }
    Ok(out)
}

fn d3_bayatlik(yol: &str, metin: &str, bugun: NaiveDate, esik: i128, cekim: Option<NaiveDate>) -> Sn<Vec<Bulgu>> {
    let mut tarihler = vec![];
    for m in RX_DAMGA.find_iter(metin) {
        let m = m.map_err(rx_hata)?;
        if let Some(t) = iso_tarih(m.as_str())
            && t <= bugun
        {
            tarihler.push(t);
        }
    }
    if let Some(c) = cekim
        && c <= bugun
    {
        tarihler.push(c);
    }
    let Some(en_yeni) = tarihler.into_iter().max() else { return Ok(vec![]) };
    let yas = (bugun - en_yeni).num_days();
    if yas as i128 <= esik {
        return Ok(vec![]);
    }
    Ok(vec![Bulgu {
        denetim: "D3",
        seviye: None,
        dosya: yol.to_string(),
        satir: 0,
        kalip: iso(en_yeni),
        ornek: "-".into(),
        yas_gun: Some(yas),
        not: "en yeni damga eşiği aştı → BAYAT-ADAY (yeniden-çekim kuyruğu; silme yok)",
    }])
}

/// `re.search(r"\d{4}-\d{2}-\d{2}", s)` (Unicode `\d`)
fn tarih_iceriyor(s: &str) -> bool {
    static RX: LazyLock<regex::Regex> = LazyLock::new(|| regex::Regex::new(r"\d{4}-\d{2}-\d{2}").unwrap());
    RX.is_match(s)
}

/// Karar 88 M4: yol `raporlar/` ∨ `cc/` ile başlıyor ∧ dosya adı YYYY-MM-DD taşıyor → D1/D2 muaf.
fn tarihli_muaf(yol: &str) -> bool {
    (yol.starts_with("raporlar/") || yol.starts_with("cc/")) && tarih_iceriyor(&taban_ad(yol))
}

/// `os.path.basename`
fn taban_ad(yol: &str) -> String {
    let (_, geri) = py::splitdrive(yol);
    let ayrac = |c: char| c == '/' || (cfg!(windows) && c == '\\');
    match geri.char_indices().rev().find(|(_, c)| ayrac(*c)) {
        Some((i, c)) => geri[i + c.len_utf8()..].to_string(),
        None => geri,
    }
}

/// `os.path.isabs` (Python 3.11)
fn mutlak_mu(yol: &str) -> bool {
    let (_, geri) = py::splitdrive(yol);
    let ayrac = |c: char| c == '/' || (cfg!(windows) && c == '\\');
    geri.chars().next().is_some_and(ayrac)
}

fn git(args: &[&str], repo: &str) -> Sn<(bool, String)> {
    let r = Command::new("git").args(args).current_dir(repo).stdin(Stdio::null()).output().map_err(|e| format!("OSError: git: {e}"))?;
    let s = String::from_utf8(r.stdout).map_err(|_| "UnicodeDecodeError: git çıktısı".to_string())?;
    Ok((r.status.success(), py::evrensel_satir(&s)))
}

fn varsayilan_kapsam(repo: &str, bugun: NaiveDate) -> Sn<Option<Vec<String>>> {
    let (ok, cikti) = git(&["ls-files", "-z"], repo)?;
    if !ok {
        return Ok(None);
    }
    let sinir = bugun.checked_sub_days(Days::new(30)).filter(|d| d.year() >= 1).ok_or("OverflowError: date value out of range")?;
    let sinir = iso(sinir);
    let mut secim = std::collections::BTreeSet::new();
    for f in cikti.split('\0').filter(|f| f.ends_with(".md")) {
        if f.starts_with("wiki/") || (f.starts_with("core/") && !f.contains("/sablonlar/")) {
            secim.insert(f.to_string());
        } else if f.starts_with("raporlar/") || f.starts_with("cc/rapor/") {
            static RX: LazyLock<regex::Regex> = LazyLock::new(|| regex::Regex::new(r"(\d{4}-\d{2}-\d{2})").unwrap());
            if let Some(m) = RX.find(f)
                && m.as_str() >= sinir.as_str()
            {
                secim.insert(f.to_string());
            }
        }
    }
    Ok(Some(secim.into_iter().collect()))
}

static ACIKLAMA: LazyLock<String> = LazyLock::new(|| crate::argparse::aciklama_sar("Anakronizm freni deterministik denetimi (D1 zaman-çivi · D2 damga-varlığı · D3 bayatlık)"));

fn ayrisan() -> Ayrisan {
    Ayrisan::yeni(
        "anakronizm-denetim.py",
        Some(ACIKLAMA.as_str()),
        vec![
            Secenek::deger(&["--repo"], "repo", None),
            Secenek::ekle(&["--dosya"], "dosya", Some("tek dosya (tekrarlanabilir); verilirse kapsam yerine bunlar")),
            Secenek::deger(&["--kapsam"], "kapsam", Some("virgüllü ön-ek listesi (wiki,core,raporlar,cc); boşsa varsayılan")),
            Secenek::tam(&["--esik-gun"], "esik_gun", None),
            Secenek::deger(&["--bugun"], "bugun", Some("YYYY-MM-DD (varsayılan sistem tarihi)")),
            Secenek::bayrak(&["--json"], "json", None),
            Secenek::bayrak(&["--kuru"], "kuru", None),
            Secenek::bayrak(&["--sessiz"], "sessiz", None),
            Secenek::bayrak(&["--kalip-listesi"], "kalip_listesi", None),
            Secenek::bayrak(&["--muafiyet-yok"], "muafiyet_yok", Some("Karar 88 M4 tarihli-dosya muafiyetini kapat (eski davranış)")),
        ],
    )
}

pub fn kos(argv: &[String]) -> i32 {
    let a = match ayrisan().ayristir(argv) {
        Ok(a) => a,
        Err(k) => return k,
    };
    match calis(&a) {
        Ok(k) => k,
        Err(e) => py::coker(&e),
    }
}

fn calis(a: &crate::argparse::Sonuc) -> Sn<i32> {
    if a.bayrak("kalip_listesi") {
        py::print(&format!("ZAMAN-ÇİVİ: {}", ZAMAN_CIVI.join(" | ")));
        py::print(&format!("SÜRÜM/SKOR: {}", SURUM_SKOR.join(" | ")));
        py::print(&format!("TARİH (muaf kılar): {}", TARIH.join(" | ")));
        return Ok(0);
    }
    let repo = py::abspath(&a.metin("repo").map(String::from).unwrap_or_else(harness_anahtar::jarvis));
    let bugun = match a.metin("bugun").filter(|s| !s.is_empty()) {
        Some(s) => iso_tarih(s).ok_or_else(|| format!("ValueError: Invalid isoformat string: {}", py::repr(s)))?,
        None => chrono::Local::now().date_naive(),
    };
    let esik = a.tam("esik_gun").unwrap_or(90);
    let kuru = a.bayrak("kuru");
    let dosyalar: Vec<String> = if let Some(l) = a.liste("dosya").filter(|l| !l.is_empty()) {
        let mut v = vec![];
        for f in l {
            if mutlak_mu(f) {
                v.push(py::relpath(&py::abspath(f), &repo).map_err(|e| format!("ValueError: {e}"))?);
            } else {
                v.push(f.clone());
            }
        }
        v
    } else {
        let Some(mut d) = varsayilan_kapsam(&repo, bugun)? else {
            py::err(&format!("HATA: git repo değil: {repo}\n"));
            return Ok(2);
        };
        if let Some(k) = a.metin("kapsam").filter(|k| !k.is_empty()) {
            let onek: Vec<String> = k.split(',').map(py::strip).filter(|x| !x.is_empty()).map(|x| format!("{x}/")).collect();
            d.retain(|f| onek.iter().any(|o| f.starts_with(o.as_str()) || f.starts_with(o.trim_end_matches('/'))));
        }
        d
    };
    let head = {
        let (_, c) = git(&["rev-parse", "--short", "HEAD"], &repo)?;
        let h = py::strip(&c);
        if h.is_empty() { "-".to_string() } else { h.to_string() }
    };
    let ts = Utc::now().with_timezone(&FixedOffset::east_opt(3 * 3600).expect("ofset")).format("%Y-%m-%dT%H:%M:%S+03:00").to_string();
    let kosum_id = format!("anakronizm:{head}:{}", iso(bugun));
    let mut bulgular: Vec<Bulgu> = vec![];
    let cekim = cekim_olaylari(&repo)?;
    let mut n_muaf = 0;
    for f in &dosyalar {
        let Ok(ham) = std::fs::read(py::join(&repo, f)) else { continue };
        let metin = py::evrensel_satir(&String::from_utf8_lossy(&ham));
        let muaf = !a.bayrak("muafiyet_yok") && tarihli_muaf(f);
        if muaf {
            n_muaf += 1;
            bulgular.extend(d3_bayatlik(f, &metin, bugun, esik, cekim.get(f).copied())?);
        } else {
            bulgular.extend(d1_zaman_civi(f, &metin)?);
            bulgular.extend(d2_damga_varligi(f, &metin)?);
            bulgular.extend(d3_bayatlik(f, &metin, bugun, esik, cekim.get(f).copied())?);
        }
    }
    let say = |den: &str, sev: Option<&str>| bulgular.iter().filter(|b| b.denetim == den && sev.is_none_or(|s| b.seviye() == s)).count();
    let (n1, n1u, n2, n3) = (say("D1", Some("İHLAL")), say("D1", Some("UYARI")), say("D2", None), say("D3", None));
    if !kuru {
        let jsonl = py::join(&py::join(&repo, "veri"), "anakronizm-denetim.jsonl");
        let mut dok = String::new();
        for b in &bulgular {
            dok.push_str(&py_dumps(&b.harita(&ts, &head, &kosum_id)));
            dok.push('\n');
        }
        let yaz = |e: std::io::Error, y: &str| format!("OSError: {y}: {e}");
        let mut fh = std::fs::OpenOptions::new().append(true).create(true).open(&jsonl).map_err(|e| yaz(e, &jsonl))?;
        fh.write_all(dok.as_bytes()).map_err(|e| yaz(e, &jsonl))?;
        let gd = py::join(&py::join(&repo, "veri"), "gorunum");
        std::fs::create_dir_all(&gd).map_err(|e| yaz(e, &gd))?;
        let csv = py::join(&gd, "v_bayat_aday.csv");
        let mut s = String::from("dosya,en_yeni_damga,yas_gun,esik_gun,bugun,kod_sha\n");
        let mut d3: Vec<&Bulgu> = bulgular.iter().filter(|b| b.denetim == "D3").collect();
        d3.sort_by_key(|b| -b.yas_gun.unwrap_or(0));
        for b in d3 {
            s.push_str(&format!("{},{},{},{},{},{}\n", b.dosya, b.kalip, b.yas_gun.unwrap_or(0), esik, iso(bugun), head));
        }
        std::fs::write(&csv, s.as_bytes()).map_err(|e| yaz(e, &csv))?;
    }
    if a.bayrak("json") {
        let sonuc = json!({
            "ts": ts, "kod_sha": head, "kosum_id": kosum_id, "bugun": iso(bugun), "dosya_sayisi": dosyalar.len(), "tarihli_muaf": n_muaf,
            "D1_ihlal": n1, "D1_uyari": n1u, "D2": n2, "D3": n3,
            "bulgular": bulgular.iter().map(|b| b.harita(&ts, &head, &kosum_id)).collect::<Vec<_>>(), "yazildi": !kuru,
        });
        py::print(&py::json_girintili(&sonuc));
    } else if !a.bayrak("sessiz") {
        py::print(&format!(
            "ANAKRONİZM DENETİMİ · HEAD {head} · bugün {} · {} dosya · tarihli-muaf {n_muaf} · D1 İHLAL (tarihsiz sürüm/skor) {n1} · D1 UYARI (zaman-çivi) {n1u} · D2 damgasız-dosya {n2} · D3 bayat-aday {n3} (eşik {esik} gün)",
            iso(bugun),
            dosyalar.len()
        ));
        let onem = |s: &str| match s {
            "İHLAL" => 0,
            "KUYRUK" => 1,
            _ => 2,
        };
        let mut sirali: Vec<&Bulgu> = bulgular.iter().collect();
        sirali.sort_by_key(|b| onem(b.seviye()));
        for b in sirali.iter().take(60) {
            let kalip = if b.denetim != "D3" { b.kalip.clone() } else { format!("yaş {} gün (damga {})", b.yas_gun.unwrap_or(0), b.kalip) };
            py::print(&format!("  [{} {}] {}:{}  {}  ← {}", b.denetim, b.seviye(), b.dosya, b.satir, kalip, py::ilk(&b.ornek, 100)));
        }
        if bulgular.len() > 60 {
            py::print(&format!("  … +{} bulgu (veri/anakronizm-denetim.jsonl)", bulgular.len() - 60));
        }
    }
    Ok(if n1 > 0 || n2 > 0 { 3 } else { 0 })
}
