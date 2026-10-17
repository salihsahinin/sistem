//! baglam-tablo: JARVIS bağlamını (git-izlenen .md/.json/.jsonl) veri tablosuna çevirir (`tools/baglam-tablo.py` karşılığı).
//! Çıktılar: `veri/baglam.sqlite` (tmp → replace) · `veri/baglam.jsonl` · `veri/gorunum/*.csv`.
//! Python `re` ileri/geri-bakışlı kalıpları kod noktası dizisi (`Vec<char>`) üzerinde elle yazılmış tarayıcılardır
//! (ofsetler Python gibi kod noktası; geri-izleme sırası kalıbın öncelik sırasına bağlı kalır).
//! `json.loads` hata iletileri/konumları CPython C-tarayıcısına göre taklit edilir (`uretim.notlar` içine yazıldığı için).
use crate::argparse::{Ayrisan, Secenek};
use crate::py::{self, Sha1, float_repr, sha1_hex};
use jarvis_hook::ortak::py_dumps;
use regex::Regex;
use rusqlite::{Connection, ToSql, types::ValueRef};
use serde_json::{Map, Value};
use std::collections::{BTreeMap, BTreeSet, HashMap, HashSet};
use std::path::Path;
use std::process::{Command, Stdio};
use std::sync::LazyLock;

const SEMA_SURUMU: &str = "v1";
const CSV_SATIR_TAVANI: usize = 5000;
const JSON_HARIC: [&str; 2] = [".claude/settings.json", ".mcp.json"];
const MODEL_KLASOR_ONEK: &str = "arsiv/chat-model-degisikligi";

type Sn<T> = Result<T, String>;

// ---------------------------------------------------------------- Yardımcılar
fn fail_loud(msg: &str) -> i32 {
    py::err(&format!("HATA (FAIL-LOUD): {msg}\n"));
    2
}

struct GitCikti {
    out: Vec<u8>,
}

/// `git(repo, *args)` (check=True): sıfır olmayan çıkış → `RuntimeError` iletisi; başlatılamama → OSError iletisi.
fn git(repo: &str, args: &[&str], kontrol: bool) -> Sn<GitCikti> {
    let mut c = Command::new("git");
    c.args(["-c", "core.quotepath=off"]).args(args).current_dir(repo);
    c.stdin(Stdio::null()).stdout(Stdio::piped()).stderr(Stdio::piped());
    let o = c.output().map_err(|e| {
        if cfg!(windows) {
            let s = e.to_string();
            let govde = s.split(" (os error").next().unwrap_or(&s).trim_end_matches(['.', ' ']).to_string();
            format!("[WinError {}] {govde}", e.raw_os_error().unwrap_or(0))
        } else {
            e.to_string()
        }
    })?;
    if kontrol && !o.status.success() {
        return Err(format!("git {} başarısız: {}", args.join(" "), String::from_utf8_lossy(&o.stderr)));
    }
    Ok(GitCikti { out: o.stdout })
}

/// `git hash-object` ile birebir aynı değer.
fn git_blob_sha(data: &[u8]) -> String {
    let mut s = Sha1::yeni();
    s.ekle(format!("blob {}\0", data.len()).as_bytes());
    s.ekle(data);
    s.bitir()
}

fn token_kestirim(metin: &str) -> i64 {
    ((metin.len() + 3) / 4) as i64
}

// ---------------------------------------------------------------- Python karakter sınıfları
static ND: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"^\p{Nd}$").unwrap());
static WNONASCII: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"^[\p{L}\p{N}]$").unwrap());

/// Python `\d` (Unicode Nd).
fn nd(c: char) -> bool {
    c.is_ascii_digit() || (!c.is_ascii() && ND.is_match(c.encode_utf8(&mut [0; 4])))
}
/// Python `\w` (str.isalnum ya da `_`).
fn w(c: char) -> bool {
    if c.is_ascii() { c.is_ascii_alphanumeric() || c == '_' } else { WNONASCII.is_match(c.encode_utf8(&mut [0; 4])) }
}
/// Python `\s`.
fn ws(c: char) -> bool {
    py::bosluk_mu(c)
}

/// Python tek karakter küçültme (`sre_lower_unicode`: basit eşleme).
fn alt1(c: char) -> char {
    if c == '\u{130}' {
        return 'i';
    }
    let mut it = c.to_lowercase();
    let f = it.next().unwrap_or(c);
    if it.next().is_none() { f } else { c }
}

/// Python `os.path.basename`.
fn basename(p: &str) -> &str {
    let i = if cfg!(windows) { p.rfind(['/', '\\']) } else { p.rfind('/') };
    match i {
        Some(i) => &p[i + 1..],
        None => p,
    }
}

/// Python `os.path.dirname` (göreli yollar için).
fn dirname(p: &str) -> String {
    let i = if cfg!(windows) { p.rfind(['/', '\\']) } else { p.rfind('/') };
    let Some(i) = i else { return String::new() };
    let head = &p[..=i];
    if head.chars().all(|c| c == '/' || (cfg!(windows) && c == '\\')) {
        return head.to_string();
    }
    head.trim_end_matches(|c| c == '/' || (cfg!(windows) && c == '\\')).to_string()
}

/// Python `os.path.splitext(p)[1]`.
fn uzanti_bul(p: &str) -> String {
    let c: Vec<char> = p.chars().collect();
    let sep = c.iter().rposition(|&x| x == '/' || (cfg!(windows) && x == '\\')).map(|i| i as isize).unwrap_or(-1);
    let nokta = c.iter().rposition(|&x| x == '.').map(|i| i as isize).unwrap_or(-1);
    if nokta > sep {
        let mut k = sep + 1;
        while k < nokta {
            if c[k as usize] != '.' {
                return c[nokta as usize..].iter().collect();
            }
            k += 1;
        }
    }
    String::new()
}

/// Python `os.path.splitext(p)[0]`.
fn govde_bul(p: &str) -> String {
    let u = uzanti_bul(p);
    p[..p.len() - u.len()].to_string()
}

// ---------------------------------------------------------------- Türkçe-ASCII katlama (uzunluk korunur)
fn fold(metin: &[char]) -> Vec<char> {
    metin
        .iter()
        .map(|&ch| match ch {
            'ç' | 'Ç' => 'c',
            'ğ' | 'Ğ' => 'g',
            'ı' | 'I' | 'İ' | 'i' => 'i',
            'ö' | 'Ö' => 'o',
            'ş' | 'Ş' => 's',
            'ü' | 'Ü' => 'u',
            'â' | 'Â' => 'a',
            'î' | 'Î' => 'i',
            'û' | 'Û' => 'u',
            _ => {
                let mut it = ch.to_lowercase();
                let f = it.next().unwrap_or(ch);
                if it.next().is_none() { f } else { ch }
            }
        })
        .collect()
}

fn fold_str(s: &str) -> String {
    fold(&s.chars().collect::<Vec<_>>()).into_iter().collect()
}

// ---------------------------------------------------------------- Katman / tür kuralları
fn katman_bul(yol: &str) -> &'static str {
    let ad = basename(yol);
    if [".json", ".jsonl", ".yaml", ".yml"].iter().any(|e| yol.ends_with(e)) {
        return "yapisal";
    }
    if yol == "CLAUDE.md" || yol.starts_with("core/") {
        return "sicak";
    }
    if yol.starts_with(".claude/skills/") && ad == "SKILL.md" {
        return "sicak";
    }
    if yol.starts_with("raporlar/")
        || yol.starts_with("cc/rapor/")
        || yol.starts_with("cc/gorev/")
        || yol.starts_with("ogrenme/")
        || yol.starts_with(MODEL_KLASOR_ONEK)
        || format!("/{yol}").contains("/arsiv/")
        || ad.starts_with("arsiv-")
        || ad.contains("-arsiv")
    {
        return "soguk";
    }
    if yol.starts_with("kuyruk/")
        || yol.starts_with("wiki/")
        || yol == "fikir-kutusu.md"
        || yol.starts_with("cc/pipeline/")
        || yol == "cc/defter.md"
        || (!yol.contains('/') && yol.ends_with(".md"))
        || yol.starts_with(".claude/")
        || yol == "cc/README.md"
    {
        return "ilik";
    }
    "soguk"
}

fn tur_bul(yol: &str) -> &'static str {
    let ad = basename(yol);
    let adl = ad.to_lowercase();
    if JSON_HARIC.contains(&yol) {
        return "diger";
    }
    if yol == "CLAUDE.md" {
        return "kanon";
    }
    if yol == "core/durum-kapsulu.md" || adl.contains("kapsulu") || adl.contains("kapsul") {
        return "kapsul";
    }
    if yol == "core/pano.md" {
        return "pano";
    }
    if yol.starts_with("core/tuzuk") {
        return "tuzuk";
    }
    if yol.starts_with("core/") {
        return "kanon";
    }
    if yol.starts_with(".claude/skills/") {
        if yol.contains("/evals/") && yol.ends_with(".json") {
            return "eval";
        }
        return "skill";
    }
    if yol == "wiki/sozluk.md" {
        return "sozluk";
    }
    if yol.starts_with("wiki/") {
        return "wiki";
    }
    if yol.starts_with("kuyruk/") {
        if adl.starts_with("gelen-") {
            return "gelen";
        }
        if adl.contains("fikir-kutusu") {
            return "kutu";
        }
        if adl.contains("defter") && !adl.contains("sema") {
            return "defter";
        }
        return "kuyruk";
    }
    if yol == "cc/defter.md" {
        return "defter";
    }
    if yol.starts_with("cc/gorev/") {
        return "emir";
    }
    if yol.starts_with("cc/rapor/") {
        return "rapor";
    }
    if yol.starts_with("cc/pipeline/") {
        return "pipeline";
    }
    if yol.starts_with("raporlar/") {
        if adl.starts_with("vardiya-teslim-") {
            return "teslim";
        }
        if yol.ends_with(".jsonl") {
            return "log";
        }
        return "rapor";
    }
    if yol.starts_with("ogrenme/dersler/") {
        return "ders";
    }
    if yol.starts_with(MODEL_KLASOR_ONEK) {
        return "log";
    }
    if yol == "fikir-kutusu.md" || adl.contains("fikir-kutusu") {
        return "kutu";
    }
    if adl.contains("rapor") {
        return "rapor";
    }
    if yol.ends_with(".jsonl") {
        return "log";
    }
    "diger"
}

// ---------------------------------------------------------------- Git meta
type Zaman = (i64, String);

fn git_meta(repo: &str, yollar: &[String]) -> Sn<HashMap<String, (String, String)>> {
    let p = git(repo, &["log", "--format=%x01%H %ct %cI", "--name-status", "-M", "-c", "--no-color"], true)?;
    let metin = String::from_utf8_lossy(&p.out).into_owned();
    let mut ilk_ct: HashMap<String, Zaman> = HashMap::new();
    let mut son_ct: HashMap<String, Zaman> = HashMap::new();
    let mut rename_eski: HashMap<String, Vec<(i64, String)>> = HashMap::new();
    let mut cur: Option<Zaman> = None;
    for satir in metin.split('\n') {
        if let Some(r) = satir.strip_prefix('\u{1}') {
            let parca: Vec<&str> = r.splitn(3, ' ').collect();
            if parca.len() == 3 {
                let ct: i64 = parca[1].parse().map_err(|_| "ValueError: invalid literal for int()".to_string())?;
                cur = Some((ct, parca[2].to_string()));
            }
            continue;
        }
        let Some(cur) = cur.as_ref() else { continue };
        if py::strip(satir).is_empty() {
            continue;
        }
        let alan: Vec<&str> = satir.split('\t').collect();
        let durum = alan[0];
        let hedefler: Vec<String> = if durum.starts_with('R') && alan.len() >= 3 {
            rename_eski.entry(alan[2].to_string()).or_default().push((cur.0, alan[1].to_string()));
            vec![alan[2].to_string()]
        } else if alan.len() >= 2 {
            vec![alan[alan.len() - 1].to_string()]
        } else {
            continue;
        };
        for y in hedefler {
            if ilk_ct.get(&y).is_none_or(|e| cur.0 < e.0) {
                ilk_ct.insert(y.clone(), cur.clone());
            }
            if son_ct.get(&y).is_none_or(|e| cur.0 > e.0) {
                son_ct.insert(y, cur.clone());
            }
        }
    }
    fn ilk_zincir(y: &str, gorulen: &mut HashSet<String>, ilk_ct: &HashMap<String, Zaman>, rename_eski: &HashMap<String, Vec<(i64, String)>>) -> Option<Zaman> {
        let mut best = ilk_ct.get(y).cloned();
        if let Some(l) = rename_eski.get(y) {
            for (_ct, eski) in l {
                if gorulen.contains(eski) {
                    continue;
                }
                gorulen.insert(eski.clone());
                let b2 = ilk_zincir(eski, gorulen, ilk_ct, rename_eski);
                if let Some(b2) = b2
                    && best.as_ref().is_none_or(|b| b2.0 < b.0)
                {
                    best = Some(b2);
                }
            }
        }
        best
    }
    let mut sonuc = HashMap::new();
    for y in yollar {
        let mut g = HashSet::new();
        g.insert(y.clone());
        let ilk = ilk_zincir(y, &mut g, &ilk_ct, &rename_eski);
        let son = son_ct.get(y);
        sonuc.insert(y.clone(), (ilk.map(|i| i.1).unwrap_or_else(|| "-".into()), son.map(|s| s.1.clone()).unwrap_or_else(|| "-".into())));
    }
    Ok(sonuc)
}

// ---------------------------------------------------------------- Markdown blok ayrıştırıcı
struct Blok {
    tur: &'static str,
    bas: usize,
    son: usize,
    metin: String,
    derinlik: usize,
    seviye: usize,
    baslik: String,
}

fn blok(tur: &'static str, bas: usize, son: usize, satirlar: &[&str], derinlik: usize) -> Blok {
    Blok { tur, bas, son, metin: satirlar.join("\n"), derinlik, seviye: 0, baslik: String::new() }
}

/// `RE_BASLIK`: (seviye, grup2) — grup2 ham (strip edilmemiş).
fn re_baslik(s: &str) -> Option<(usize, Vec<char>)> {
    let c: Vec<char> = s.chars().collect();
    let k = c.iter().take_while(|&&x| x == '#').count();
    if k == 0 || k > 6 {
        return None;
    }
    let mut p = k;
    while p < c.len() && (c[p] == ' ' || c[p] == '\t') {
        p += 1;
    }
    if p == k {
        return None;
    }
    // (.*?)\s*#*\s*$ — tembel grup: en uzun `\s*#*\s*` kuyruğu atılır
    let mut e = c.len();
    while e > p && ws(c[e - 1]) {
        e -= 1;
    }
    while e > p && c[e - 1] == '#' {
        e -= 1;
    }
    while e > p && ws(c[e - 1]) {
        e -= 1;
    }
    Some((k, c[p..e].to_vec()))
}

/// `RE_FENCE`: (çit karakteri, çit uzunluğu, kalan metin).
fn re_fence(s: &str) -> Option<(char, usize, String)> {
    let c: Vec<char> = s.chars().collect();
    let b = c.iter().take_while(|&&x| x == ' ').count();
    if b > 3 || b >= c.len() {
        return None;
    }
    let f = c[b];
    if f != '`' && f != '~' {
        return None;
    }
    let k = c[b..].iter().take_while(|&&x| x == f).count();
    if k < 3 {
        return None;
    }
    Some((f, k, c[b + k..].iter().collect()))
}

/// `^\s{0,3}` sonrası ilk boşluk-olmayan karakterin indeksi (en çok 3 boşluk).
fn girinti_en_cok3(c: &[char]) -> Option<usize> {
    let mut k = 0;
    for (i, &x) in c.iter().enumerate() {
        if ws(x) {
            k += 1;
            if k > 3 {
                return None;
            }
        } else {
            return Some(i);
        }
    }
    None
}

fn re_yatay(s: &str) -> bool {
    let c: Vec<char> = s.chars().collect();
    let Some(i) = girinti_en_cok3(&c) else { return false };
    let m = c[i];
    if m != '-' && m != '*' && m != '_' {
        return false;
    }
    let mut adet = 0;
    for &x in &c[i..] {
        if x == m {
            adet += 1;
        } else if !ws(x) {
            return false;
        }
    }
    adet >= 3
}

fn re_tablo(s: &str) -> bool {
    s.chars().find(|&c| !ws(c)) == Some('|')
}

fn re_alinti(s: &str) -> bool {
    let c: Vec<char> = s.chars().collect();
    girinti_en_cok3(&c).is_some_and(|i| c[i] == '>')
}

/// `RE_MADDE`: eşleşirse `expandtabs(4)` sonrası girinti genişliği.
fn re_madde(s: &str) -> Option<usize> {
    let c: Vec<char> = s.chars().collect();
    let g = c.iter().take_while(|&&x| ws(x)).count();
    let mut p = g;
    if p >= c.len() {
        return None;
    }
    if matches!(c[p], '-' | '*' | '+') {
        p += 1;
    } else {
        let d = c[p..].iter().take_while(|&&x| nd(x)).count();
        if d == 0 || d > 3 {
            return None;
        }
        p += d;
        if p >= c.len() || !matches!(c[p], '.' | ')') {
            return None;
        }
        p += 1;
    }
    if p >= c.len() || !ws(c[p]) {
        return None;
    }
    // girinti: group(1).expandtabs(4) uzunluğu
    let mut kol = 0usize;
    for &x in &c[..g] {
        match x {
            '\t' => kol += 4 - (kol % 4),
            '\n' | '\r' => kol = 0,
            _ => kol += 1,
        }
    }
    Some(kol)
}

fn ayrac_satiri(s: &str) -> bool {
    // re.match(r"^\s*\|?\s*:?-{2,}", s)
    let c: Vec<char> = s.chars().collect();
    let mut p = c.iter().take_while(|&&x| ws(x)).count();
    if p < c.len() && c[p] == '|' {
        p += 1;
    }
    while p < c.len() && ws(c[p]) {
        p += 1;
    }
    if p < c.len() && c[p] == ':' {
        p += 1;
    }
    c[p.min(c.len())..].iter().take_while(|&&x| x == '-').count() >= 2
}

fn md_bloklar(metin: &str) -> Vec<Blok> {
    let satirlar: Vec<&str> = metin.split('\n').collect();
    let n = satirlar.len();
    let mut bloklar: Vec<Blok> = vec![];
    let mut i = 0usize;
    if n > 0 && py::strip(satirlar[0]) == "---" {
        for j in 1..n.min(200) {
            let t = py::strip(satirlar[j]);
            if t == "---" || t == "..." {
                bloklar.push(blok("frontmatter", 1, j + 1, &satirlar[0..=j], 0));
                i = j + 1;
                break;
            }
        }
    }
    let mut para: Vec<&str> = vec![];
    let mut para_bas = 0usize;
    fn para_kapat<'a>(para: &mut Vec<&'a str>, para_bas: &mut usize, bloklar: &mut Vec<Blok>) {
        if !para.is_empty() {
            bloklar.push(blok("paragraf", *para_bas, *para_bas + para.len() - 1, para, 0));
            para.clear();
            *para_bas = 0;
        }
    }
    while i < n {
        let s = satirlar[i];
        let no = i + 1;
        if py::strip(s).is_empty() {
            para_kapat(&mut para, &mut para_bas, &mut bloklar);
            i += 1;
            continue;
        }
        if let Some((fc, fk, _)) = re_fence(s) {
            para_kapat(&mut para, &mut para_bas, &mut bloklar);
            let mut j = i + 1;
            let mut kapandi = false;
            while j < n {
                if let Some((c2, k2, r2)) = re_fence(satirlar[j])
                    && c2 == fc
                    && k2 >= fk
                    && py::strip(&r2).is_empty()
                {
                    kapandi = true;
                    break;
                }
                j += 1;
            }
            let son = if kapandi { j } else { n - 1 };
            bloklar.push(blok("kod", no, son + 1, &satirlar[i..=son], 0));
            i = son + 1;
            continue;
        }
        if let Some((sev, g)) = re_baslik(s) {
            para_kapat(&mut para, &mut para_bas, &mut bloklar);
            let mut b = blok("baslik", no, no, &[s], 0);
            b.seviye = sev;
            let gs: String = g.into_iter().collect();
            b.baslik = py::strip(&gs).to_string();
            bloklar.push(b);
            i += 1;
            continue;
        }
        if re_yatay(s) {
            para_kapat(&mut para, &mut para_bas, &mut bloklar);
            bloklar.push(blok("yatay_cizgi", no, no, &[s], 0));
            i += 1;
            continue;
        }
        if re_tablo(s) {
            para_kapat(&mut para, &mut para_bas, &mut bloklar);
            let mut j = i;
            let mut ilk = true;
            while j < n && re_tablo(satirlar[j]) {
                if ilk {
                    let mut son = j;
                    if j + 1 < n && ayrac_satiri(satirlar[j + 1]) && re_tablo(satirlar[j + 1]) {
                        son = j + 1;
                    }
                    bloklar.push(blok("tablo_baslik", j + 1, son + 1, &satirlar[j..=son], 0));
                    j = son + 1;
                    ilk = false;
                    continue;
                }
                bloklar.push(blok("tablo_satiri", j + 1, j + 1, &[satirlar[j]], 0));
                j += 1;
            }
            i = j;
            continue;
        }
        if re_alinti(s) {
            para_kapat(&mut para, &mut para_bas, &mut bloklar);
            let mut j = i;
            while j < n && re_alinti(satirlar[j]) {
                j += 1;
            }
            bloklar.push(blok("alinti", no, j, &satirlar[i..j], 0));
            i = j;
            continue;
        }
        if let Some(girinti) = re_madde(s) {
            para_kapat(&mut para, &mut para_bas, &mut bloklar);
            let mut j = i + 1;
            while j < n {
                let t = satirlar[j];
                if py::strip(t).is_empty() {
                    break;
                }
                if re_madde(t).is_some() || re_baslik(t).is_some() || re_fence(t).is_some() || re_tablo(t) || re_alinti(t) || re_yatay(t) {
                    break;
                }
                let lead = t.chars().count() - t.trim_start_matches(ws).chars().count();
                if lead <= girinti {
                    break;
                }
                j += 1;
            }
            bloklar.push(blok("madde", no, j, &satirlar[i..j], girinti / 2));
            i = j;
            continue;
        }
        if para.is_empty() {
            para_bas = no;
        }
        para.push(s);
        i += 1;
    }
    para_kapat(&mut para, &mut para_bas, &mut bloklar);
    bloklar
}

// ---------------------------------------------------------------- Zarf (ingest v2)
const ZARF_ZORUNLU: [&str; 5] = ["tip", "kaynak", "tarih", "hedef", "sema"];

struct Zarf {
    alanlar: BTreeMap<String, String>,
    tam: bool,
}

fn zarf_ayristir(c: &[char]) -> Option<Zarf> {
    let hedef: Vec<char> = "[tip:".chars().collect();
    let idx = (0..c.len()).find(|&i| c[i..].starts_with(&hedef))?;
    let mut derinlik = 0i32;
    let mut son: Option<usize> = None;
    for (j, &ch) in c.iter().enumerate().skip(idx) {
        if ch == '[' {
            derinlik += 1;
        } else if ch == ']' {
            derinlik -= 1;
            if derinlik == 0 {
                son = Some(j);
                break;
            }
        }
    }
    let son = son?;
    let ic: String = c[idx + 1..son].iter().collect();
    let mut alanlar: BTreeMap<String, String> = BTreeMap::new();
    for parca in ic.split('|') {
        let Some((k, v)) = parca.split_once(':') else { continue };
        let k = fold_str(py::strip(k)).replace('_', "-").replace(' ', "-");
        if k.is_empty() || k.contains(' ') {
            continue;
        }
        alanlar.insert(k, py::strip(v).to_string());
    }
    let tam = ZARF_ZORUNLU.iter().all(|k| alanlar.contains_key(*k));
    Some(Zarf { alanlar, tam })
}

fn zarf_json(al: &BTreeMap<String, String>, kismi: bool) -> String {
    let mut m: BTreeMap<String, Value> = al.iter().map(|(k, v)| (k.clone(), Value::String(v.clone()))).collect();
    if kismi {
        m.insert("kismi".into(), Value::Bool(true));
    }
    let mut o = Map::new();
    for (k, v) in m {
        o.insert(k, v);
    }
    py_dumps(&Value::Object(o))
}

// ---------------------------------------------------------------- Referans çıkarımı
const ANAHTAR_TERIMLER: [(&str, &str); 27] = [
    ("gunaydin", "gunaydin"),
    ("seans basi", "seans basi"),
    ("seans bitimi", "seans bitimi"),
    ("uyucam", "uyucam"),
    ("vardiya", "vardiya"),
    ("kapsul", "kapsul"),
    ("pano", "pano"),
    ("tuzuk", "tuzuk"),
    ("damitma", "damitma"),
    ("ingest", "ingest"),
    ("zarf", "zarf"),
    ("atlas", "atlas"),
    ("antitez", "antitez"),
    ("hakem", "hakem"),
    ("workflow", "workflow"),
    ("pipeline", "pipeline"),
    ("skill", "skill"),
    ("halusinasyon", "halusinasyon"),
    ("sema", "sema"),
    ("staj", "staj"),
    ("cowork", "cowork"),
    ("terminal", "terminal"),
    ("ana-sira", "ana[- ]sira"),
    ("yan-oturum", "yan[- ]oturum"),
    ("katman-1", "katman[- ]1"),
    ("katman-2", "katman[- ]2"),
    ("celiski", "celiski"),
];

/// Anahtar terim gövdesi: `Some(c)` sabit karakter, `None` = `[- ]` sınıfı.
fn terim_belirtec(govde: &str) -> Vec<Option<char>> {
    let mut v = vec![];
    let mut it = govde.chars().peekable();
    while let Some(c) = it.next() {
        if c == '[' {
            // yalnız `[- ]`
            it.next();
            it.next();
            it.next();
            v.push(None);
        } else {
            v.push(Some(c));
        }
    }
    v
}

/// `_EK` kuyruğunun tam eşleşme dili.
static EK_TAM: LazyLock<Regex> = LazyLock::new(|| {
    Regex::new(
        r"^(?:s|(?:y|n|s)?(?:[aeiou]|[dt][ae]n?|l[ae]r|[iu]n|dir|dur|tir|tur|ki|ken|le|la|yle|yla|ce|ca|l[iu]k?|s[iu]z|c[iu]|lik|luk|lig|lug|siz|suz|cik|cuk|mis|mus))*$",
    )
    .unwrap()
});

fn ak(c: char) -> bool {
    c.is_ascii_lowercase() || c.is_ascii_digit()
}

/// Terimden sonra `_EK` + `(?![a-z0-9])` için eşleşme sonu (öncelik sırası: kesme işaretini tüketmek, sonra tüketmemek).
fn ek_son(f: &[char], t: usize) -> Option<usize> {
    let n = f.len();
    let kos_son = |b: usize| {
        let mut q = b;
        while q < n && ak(f[q]) {
            q += 1;
        }
        q
    };
    if t < n && f[t] == '\'' {
        let q = kos_son(t + 1);
        if q == t + 1 {
            return Some(t + 1);
        }
        let s: String = f[t + 1..q].iter().collect();
        if EK_TAM.is_match(&s) {
            return Some(q);
        }
        return Some(t);
    }
    let q = kos_son(t);
    if q == t {
        return Some(t);
    }
    let s: String = f[t..q].iter().collect();
    if EK_TAM.is_match(&s) { Some(q) } else { None }
}

fn terim_tara(f: &[char], terim: &[Option<char>]) -> Vec<(usize, usize)> {
    let n = f.len();
    let mut out = vec![];
    let mut i = 0usize;
    while i < n {
        // geri-bakış (?<![a-z0-9])
        if (i == 0 || !ak(f[i - 1])) && i + terim.len() <= n {
            let esles = terim.iter().enumerate().all(|(k, t)| match t {
                Some(c) => f[i + k] == *c,
                None => f[i + k] == '-' || f[i + k] == ' ',
            });
            if esles && let Some(son) = ek_son(f, i + terim.len()) {
                out.push((i, son));
                i = son;
                continue;
            }
        }
        i += 1;
    }
    out
}

fn gecerli_tarih(a: i64, g: i64) -> bool {
    (1..=12).contains(&a) && (1..=31).contains(&g)
}

/// Unicode Nd basamağının değeri (Nd karakterleri 10'luk bitişik bloklardır; Python `int()` hepsini çözer).
fn basamak(c: char) -> i64 {
    if c.is_ascii_digit() {
        return c as i64 - '0' as i64;
    }
    let mut k = 0u32;
    while let Some(o) = char::from_u32(c as u32 - k - 1) {
        if !nd(o) {
            break;
        }
        k += 1;
    }
    (k % 10) as i64
}

fn ik(c: &[char]) -> i64 {
    c.iter().fold(0i64, |a, d| a * 10 + basamak(*d))
}

fn ascii_rakam(c: &[char]) -> bool {
    c.iter().all(|x| nd(*x))
}

/// `(?<![\d-])(20\d{2})-(\d{2})-(\d{2})(?![\d-])` → (ay, gün) metin indeksleri; eşleşirse son = i+10.
fn tarih_tam_at(c: &[char], i: usize) -> bool {
    let n = c.len();
    if i + 10 > n {
        return false;
    }
    if i > 0 && (nd(c[i - 1]) || c[i - 1] == '-') {
        return false;
    }
    let t = &c[i..i + 10];
    if !(t[0] == '2' && t[1] == '0' && ascii_rakam(&t[2..4]) && t[4] == '-' && ascii_rakam(&t[5..7]) && t[7] == '-' && ascii_rakam(&t[8..10])) {
        return false;
    }
    i + 10 == n || !(nd(c[i + 10]) || c[i + 10] == '-')
}

fn tarih_kisa_at(c: &[char], i: usize) -> bool {
    let n = c.len();
    if i + 5 > n {
        return false;
    }
    if i > 0 && (nd(c[i - 1]) || c[i - 1] == '-') {
        return false;
    }
    let t = &c[i..i + 5];
    if !(ascii_rakam(&t[0..2]) && t[2] == '-' && ascii_rakam(&t[3..5])) {
        return false;
    }
    i + 5 == n || !(nd(c[i + 5]) || c[i + 5] == '-')
}

fn tarih_ipucu_bul(c: &[char]) -> (Option<String>, Option<String>) {
    let n = c.len();
    let mut en: Option<(usize, String, Option<String>)> = None;
    let mut i = 0;
    while i < n {
        if tarih_tam_at(c, i) {
            if gecerli_tarih(ik(&c[i + 5..i + 7]), ik(&c[i + 8..i + 10])) {
                let s: String = c[i..i + 10].iter().collect();
                en = Some((i, s.clone(), Some(s)));
                break;
            }
            i += 10;
            continue;
        }
        i += 1;
    }
    let mut i = 0;
    while i < n {
        if tarih_kisa_at(c, i) {
            let (a, b) = (ik(&c[i..i + 2]), ik(&c[i + 3..i + 5]));
            if !(gecerli_tarih(a, b) || gecerli_tarih(b, a)) {
                i += 5;
                continue;
            }
            if en.as_ref().is_none_or(|e| i < e.0) {
                en = Some((i, c[i..i + 5].iter().collect(), None));
            }
            break;
        }
        i += 1;
    }
    match en {
        None => (None, None),
        Some((_, a, b)) => (Some(a), b),
    }
}

fn url_izin(c: char) -> bool {
    !ws(c) && !matches!(c, '<' | '>' | '(' | ')' | '[' | ']' | '"' | '\'' | '`')
}

fn basla(c: &[char], i: usize, s: &str) -> bool {
    let k: Vec<char> = s.chars().collect();
    c.len() >= i + k.len() && c[i..i + k.len()] == k[..]
}

/// `https?://[^...]+` eşleşme sonu.
fn url_at(c: &[char], i: usize) -> Option<usize> {
    if !basla(c, i, "http") {
        return None;
    }
    let p = if basla(c, i + 4, "s://") {
        i + 8
    } else if basla(c, i + 4, "://") {
        i + 7
    } else {
        return None;
    };
    let mut q = p;
    while q < c.len() && url_izin(c[q]) {
        q += 1;
    }
    if q > p { Some(q) } else { None }
}

fn url_bul(c: &[char]) -> Vec<(usize, usize)> {
    let mut out = vec![];
    let mut i = 0;
    while i < c.len() {
        if c[i] == 'h'
            && let Some(e) = url_at(c, i)
        {
            out.push((i, e));
            i = e;
            continue;
        }
        i += 1;
    }
    out
}

fn yol_kar(c: char) -> bool {
    c == '-' || c == '.' || w(c)
}

const YOL_UZANTI: [&str; 8] = ["md", "py", "d2", "svg", "json", "jsonl", "sh", "ps1"];

/// `RE_YOL` bir başlangıçta eşleşme sonu (geri-izleme önceliği: en çok bölüm, en uzun gövde, uzantı sırası).
fn yol_at(c: &[char], s: usize) -> Option<usize> {
    let n = c.len();
    if s > 0 && (w(c[s - 1]) || matches!(c[s - 1], '/' | '\\' | '.' | '@' | '-')) {
        return None;
    }
    let p = if c[s] == '/' { s + 1 } else { s };
    // (YK+/)* bölüm başlangıçları
    let mut baslar = vec![p];
    let mut q = p;
    loop {
        let mut r = q;
        while r < n && yol_kar(c[r]) {
            r += 1;
        }
        if r > q && r < n && c[r] == '/' {
            q = r + 1;
            baslar.push(q);
        } else {
            break;
        }
    }
    for fs in baslar.iter().rev() {
        let fs = *fs;
        let mut l = 0;
        while fs + l < n && yol_kar(c[fs + l]) {
            l += 1;
        }
        let mut m = l;
        while m >= 1 {
            if fs + m < n && c[fs + m] == '.' && fs + m < fs + l {
                for e in YOL_UZANTI {
                    if basla(c, fs + m + 1, e) {
                        let son = fs + m + 1 + e.chars().count();
                        if son == n || !(w(c[son]) || c[son] == '/') {
                            return Some(son);
                        }
                    }
                }
            }
            m -= 1;
        }
    }
    None
}

fn yol_bul(c: &[char]) -> Vec<(usize, usize)> {
    let mut out = vec![];
    let mut i = 0;
    while i < c.len() {
        if let Some(e) = yol_at(c, i) {
            out.push((i, e));
            i = e;
            continue;
        }
        i += 1;
    }
    out
}

fn yol_normalize(ham: &str) -> String {
    let mut y: Vec<char> = ham.chars().collect();
    let low: Vec<char> = ham.to_lowercase().chars().collect();
    for isaret in ["/jarvis/", "c:/jarvis/"] {
        let k: Vec<char> = isaret.chars().collect();
        if let Some(i) = (0..low.len()).find(|&i| low[i..].starts_with(&k)) {
            let from = (i + k.len()).min(y.len());
            return y[from..].iter().collect();
        }
    }
    let mut s: String = y.drain(..).collect();
    for onek in ["~/sistem/jarvis/", "jarvis/", "./"] {
        if let Some(r) = s.strip_prefix(onek) {
            s = r.to_string();
        }
    }
    while let Some(r) = s.strip_prefix("../") {
        s = r.to_string();
    }
    s.trim_start_matches('/').to_string()
}

static SHA_KOMSU: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"(?i)(?:comm[iıİ]t|sha|g[iıİ]t|head|revert|`|hash|blob|push|merge)").unwrap());

struct Ref {
    tur: &'static str,
    deger: String,
    ham: String,
    konum: i64,
    hedef_var: Option<i64>,
    hedef_yol: Option<String>,
}

struct SkillEs {
    adlar: Vec<Vec<char>>,
    kume: HashSet<String>,
}

fn skill_harf_esit(p: char, t: char) -> bool {
    let (lp, lt) = (alt1(p), alt1(t));
    lp == lt || (lp == 'i' && t == 'ı') || (lp == 's' && t == 'ſ')
}

fn skill_at(c: &[char], i: usize, sk: &SkillEs) -> Option<usize> {
    if i > 0 && (w(c[i - 1]) || c[i - 1] == '-') {
        return None;
    }
    for ad in &sk.adlar {
        if i + ad.len() <= c.len() && ad.iter().enumerate().all(|(k, &p)| skill_harf_esit(p, c[i + k])) {
            let e = i + ad.len();
            if e == c.len() || !(w(c[e]) || c[e] == '-') {
                return Some(e);
            }
        }
    }
    None
}

struct Baglam<'a> {
    skill: &'a SkillEs,
    repo_yollar: &'a HashSet<String>,
    repo_adlar: &'a HashMap<String, String>,
    repo_kok: &'a str,
    terimler: &'a [(String, Vec<Option<char>>)],
}

fn sub(c: &[char], a: usize, b: usize) -> String {
    c[a..b].iter().collect()
}

fn referanslar(c: &[char], b: &Baglam, dosya_dizin: &str) -> Vec<Ref> {
    let n = c.len();
    let mut out: Vec<Ref> = vec![];
    let mk = |tur: &'static str, deger: String, ham: String, konum: usize| Ref { tur, deger, ham, konum: konum as i64, hedef_var: None, hedef_yol: None };
    // tuzuk_madde: (?<![\w.])(md|m)\.(\d{1,3})([a-z]?)(?!\w)
    let mut i = 0;
    while i < n {
        if (i == 0 || !(w(c[i - 1]) || c[i - 1] == '.')) && (c[i] == 'm') {
            let (g1, p) = if basla(c, i, "md.") {
                ("md", i + 3)
            } else if basla(c, i, "m.") {
                ("m", i + 2)
            } else {
                i += 1;
                continue;
            };
            let d = c[p.min(n)..].iter().take(3).take_while(|x| nd(**x)).count();
            if d > 0 {
                let mut q = p + d;
                let mut ok = false;
                let mut harf = String::new();
                if q < n && c[q].is_ascii_lowercase() {
                    if !(q + 1 < n && w(c[q + 1])) {
                        harf = c[q].to_string();
                        q += 1;
                        ok = true;
                    }
                } else if !(q < n && w(c[q])) {
                    ok = true;
                }
                if ok {
                    let g2 = ik(&c[p..p + d]);
                    out.push(mk("tuzuk_madde", format!("{g1}.{g2}{harf}"), sub(c, i, q), i));
                    i = q;
                    continue;
                }
            }
        }
        i += 1;
    }
    // v_no: (?<![\w-])V(\d{1,3})(?![\w-])
    let mut i = 0;
    while i < n {
        if c[i] == 'V' && (i == 0 || !(w(c[i - 1]) || c[i - 1] == '-')) {
            let d = c[i + 1..].iter().take(3).take_while(|x| nd(**x)).count();
            let q = i + 1 + d;
            if d > 0 && !(q < n && (w(c[q]) || c[q] == '-')) {
                out.push(mk("v_no", format!("V{}", ik(&c[i + 1..q])), sub(c, i, q), i));
                i = q;
                continue;
            }
        }
        i += 1;
    }
    // kart: (?<![\w-])K-(\d{3})(?![\w-])
    let mut i = 0;
    while i < n {
        if c[i] == 'K' && i + 1 < n && c[i + 1] == '-' && (i == 0 || !(w(c[i - 1]) || c[i - 1] == '-')) {
            let q = i + 5;
            if q <= n && ascii_rakam(&c[i + 2..q]) && !(q < n && (w(c[q]) || c[q] == '-')) {
                out.push(mk("kart", format!("K-{}", sub(c, i + 2, q)), sub(c, i, q), i));
                i = q;
                continue;
            }
        }
        i += 1;
    }
    // wiki_link: \[\[([^\]\|#\n]+?)(?:[#|][^\]\n]*)?\]\]
    let mut i = 0;
    while i + 1 < n {
        if c[i] == '[' && c[i + 1] == '[' {
            let g0 = i + 2;
            let mut son: Option<(usize, usize)> = None;
            if g0 < n && !matches!(c[g0], ']' | '|' | '#' | '\n') {
                let mut p = g0 + 1;
                loop {
                    if p < n && (c[p] == '#' || c[p] == '|') {
                        let mut q = p + 1;
                        while q < n && c[q] != ']' && c[q] != '\n' {
                            q += 1;
                        }
                        if q + 1 < n && c[q] == ']' && c[q + 1] == ']' {
                            son = Some((p, q + 2));
                            break;
                        }
                    }
                    if p + 1 < n && c[p] == ']' && c[p + 1] == ']' {
                        son = Some((p, p + 2));
                        break;
                    }
                    if p < n && !matches!(c[p], ']' | '|' | '#' | '\n') {
                        p += 1;
                    } else {
                        break;
                    }
                }
            }
            if let Some((ge, e)) = son {
                let g = sub(c, g0, ge);
                out.push(mk("wiki_link", py::strip(&g).to_string(), sub(c, i, e), i));
                i = e;
                continue;
            }
        }
        i += 1;
    }
    // url
    let urller = url_bul(c);
    for &(a, e) in &urller {
        let u = sub(c, a, e);
        let u = py::rstrip_kume(&u, ".,;:!?)").to_string();
        out.push(mk("url", u.clone(), u, a));
    }
    // etiket: \[(D|K|X|ARANAMADI|\?)\]
    let mut i = 0;
    while i < n {
        if c[i] == '[' {
            let mut bulundu = None;
            for e in ["D", "K", "X", "ARANAMADI", "?"] {
                if basla(c, i + 1, e) && c.get(i + 1 + e.chars().count()) == Some(&']') {
                    bulundu = Some(e);
                    break;
                }
            }
            if let Some(e) = bulundu {
                let son = i + 2 + e.chars().count();
                out.push(mk("etiket", e.to_string(), sub(c, i, son), i));
                i = son;
                continue;
            }
        }
        i += 1;
    }
    // tarih
    let mut i = 0;
    while i < n {
        if tarih_tam_at(c, i) {
            if gecerli_tarih(ik(&c[i + 5..i + 7]), ik(&c[i + 8..i + 10])) {
                let s = sub(c, i, i + 10);
                out.push(mk("tarih", s.clone(), s, i));
            }
            i += 10;
            continue;
        }
        i += 1;
    }
    // sha: 7-12 hex yalnız git-benzeri komşulukta; ≥13 hex doğrudan
    let mut i = 0;
    let hex = |x: char| x.is_ascii_digit() || ('a'..='f').contains(&x);
    while i < n {
        if hex(c[i]) && (i == 0 || !(c[i - 1].is_ascii_alphanumeric() || c[i - 1] == '_')) {
            let mut l = 0;
            while i + l < n && hex(c[i + l]) {
                l += 1;
            }
            let tum_rakam = c[i..i + l].iter().all(|x| x.is_ascii_digit());
            let nn = l.min(40);
            let e = i + nn;
            if !tum_rakam && nn >= 7 && !(e < n && (c[e].is_ascii_alphanumeric() || c[e] == '_')) {
                let h = sub(c, i, e);
                let mut ok = true;
                if nn < 13 {
                    let (k1, k2) = (i.saturating_sub(40), (e + 40).min(n));
                    let pencere = sub(c, k1, k2);
                    if !SHA_KOMSU.is_match(&pencere) {
                        ok = false;
                    }
                }
                if ok {
                    out.push(mk("sha", h.clone(), h, i));
                }
                i = e;
                continue;
            }
        }
        i += 1;
    }
    // dosya_pointer (URL maskeli metinde)
    let mut maskeli = c.to_vec();
    for &(a, e) in &urller {
        for x in &mut maskeli[a..e] {
            *x = ' ';
        }
    }
    for (a, e) in yol_bul(&maskeli) {
        let ham = sub(&maskeli, a, e);
        if ham.starts_with('.') && !ham.contains('/') {
            continue;
        }
        if ham.starts_with('-') {
            continue;
        }
        if ham.contains('…') || ham.replace("../", "").contains("..") {
            continue;
        }
        let norm = yol_normalize(&ham);
        let mut var = 0i64;
        let mut hedef: Option<String> = None;
        let goreli = if !dosya_dizin.is_empty() { py::normpath(&py::join(dosya_dizin, &norm)) } else { norm.clone() };
        if b.repo_yollar.contains(&norm) || Path::new(&py::join(b.repo_kok, &norm)).exists() {
            var = 1;
            hedef = Some(norm.clone());
        } else if b.repo_yollar.contains(&goreli) || Path::new(&py::join(b.repo_kok, &goreli)).exists() {
            var = 1;
            hedef = Some(goreli);
        } else if !norm.contains('/')
            && let Some(h) = b.repo_adlar.get(&norm)
        {
            var = 1;
            hedef = Some(h.clone());
        }
        out.push(Ref { tur: "dosya_pointer", deger: norm, ham, konum: a as i64, hedef_var: Some(var), hedef_yol: hedef });
    }
    // skill_adi
    if !b.skill.adlar.is_empty() {
        let mut i = 0;
        while i < n {
            if let Some(e) = skill_at(c, i, b.skill) {
                let m = sub(c, i, e);
                let ad = m.to_lowercase();
                if b.skill.kume.contains(&ad) {
                    out.push(mk("skill_adi", ad, m, i));
                }
                i = e;
                continue;
            }
            i += 1;
        }
    }
    // anahtar_terim (katlanmış metin; ofset korunur)
    let f = fold(c);
    for (deger, tok) in b.terimler {
        for (a, e) in terim_tara(&f, tok) {
            out.push(mk("anahtar_terim", deger.clone(), sub(c, a, e), a));
        }
    }
    out
}

// ---------------------------------------------------------------- JSON (CPython json.loads taklidi)
enum J {
    Nul,
    Bool(bool),
    Int(String),
    Flt(f64),
    Str(String),
    Lst(Vec<J>),
    Dct(Vec<(String, J)>),
}

enum JErr {
    Dur(usize),
    Msg(&'static str, usize),
    Ozel(String),
}

struct Jp<'a> {
    s: &'a [char],
    derin: usize,
    vekil: bool,
}

const JSON_DERINLIK: usize = 990;

impl Jp<'_> {
    fn bosluk(&self, mut i: usize) -> usize {
        while i < self.s.len() && matches!(self.s[i], ' ' | '\t' | '\n' | '\r') {
            i += 1;
        }
        i
    }
    fn dizge(&mut self, mut end: usize) -> Result<(String, usize), JErr> {
        let s = self.s;
        let len = s.len();
        let begin = end - 1;
        let mut out = String::new();
        loop {
            let mut next = end;
            let mut c = '\0';
            while next < len {
                c = s[next];
                if c == '"' || c == '\\' {
                    break;
                }
                if (c as u32) <= 0x1f {
                    return Err(JErr::Msg("Invalid control character at", next));
                }
                next += 1;
            }
            if next == len {
                return Err(JErr::Msg("Unterminated string starting at", begin));
            }
            out.extend(&s[end..next]);
            next += 1;
            if c == '"' {
                end = next;
                break;
            }
            if next == len {
                return Err(JErr::Msg("Unterminated string starting at", begin));
            }
            c = s[next];
            if c != 'u' {
                end = next + 1;
                let ch = match c {
                    '"' => '"',
                    '\\' => '\\',
                    '/' => '/',
                    'b' => '\u{8}',
                    'f' => '\u{c}',
                    'n' => '\n',
                    'r' => '\r',
                    't' => '\t',
                    _ => return Err(JErr::Msg("Invalid \\escape", end - 2)),
                };
                out.push(ch);
            } else {
                next += 1;
                end = next + 4;
                if end >= len {
                    return Err(JErr::Msg("Invalid \\uXXXX escape", next - 1));
                }
                let mut cu = 0u32;
                while next < end {
                    let d = s[next].to_digit(16).filter(|_| s[next].is_ascii()).ok_or(JErr::Msg("Invalid \\uXXXX escape", end - 5))?;
                    cu = (cu << 4) | d;
                    next += 1;
                }
                let mut cp = cu;
                if (0xD800..0xDC00).contains(&cu) && end + 6 < len && s[end] == '\\' && s[end + 1] == 'u' {
                    let mut c2 = 0u32;
                    for k in 0..4 {
                        let ch = s[end + 2 + k];
                        let d = ch.to_digit(16).filter(|_| ch.is_ascii()).ok_or(JErr::Msg("Invalid \\uXXXX escape", end + 1))?;
                        c2 = (c2 << 4) | d;
                    }
                    if (0xDC00..0xE000).contains(&c2) {
                        cp = 0x10000 + ((cu - 0xD800) << 10) + (c2 - 0xDC00);
                        end += 6;
                    }
                }
                match char::from_u32(cp) {
                    Some(ch) => out.push(ch),
                    None => {
                        self.vekil = true;
                        out.push('\u{FFFD}');
                    }
                }
            }
        }
        Ok((out, end))
    }
    fn sayi(&self, start: usize) -> Result<(J, usize), JErr> {
        let s = self.s;
        let n = s.len();
        let end_idx = n as isize - 1;
        let mut idx = start as isize;
        let g = |i: isize| s[i as usize];
        let rk = |c: char| c.is_ascii_digit();
        if g(idx) == '-' {
            idx += 1;
            if idx > end_idx {
                return Err(JErr::Dur(start));
            }
        }
        if ('1'..='9').contains(&g(idx)) {
            idx += 1;
            while idx <= end_idx && rk(g(idx)) {
                idx += 1;
            }
        } else if g(idx) == '0' {
            idx += 1;
        } else {
            return Err(JErr::Dur(start));
        }
        let mut is_float = false;
        if idx < end_idx && g(idx) == '.' && rk(g(idx + 1)) {
            is_float = true;
            idx += 2;
            while idx <= end_idx && rk(g(idx)) {
                idx += 1;
            }
        }
        if idx < end_idx && (g(idx) == 'e' || g(idx) == 'E') {
            let e_start = idx;
            idx += 1;
            if idx < end_idx && (g(idx) == '-' || g(idx) == '+') {
                idx += 1;
            }
            while idx <= end_idx && rk(g(idx)) {
                idx += 1;
            }
            if rk(g(idx - 1)) {
                is_float = true;
            } else {
                idx = e_start;
            }
        }
        let metin: String = s[start..idx as usize].iter().collect();
        let j = if is_float {
            J::Flt(metin.parse::<f64>().unwrap_or(f64::NAN))
        } else if metin == "-0" {
            J::Int("0".into())
        } else {
            J::Int(metin)
        };
        Ok((j, idx as usize))
    }
    fn tara(&mut self, idx: usize) -> Result<(J, usize), JErr> {
        let s = self.s;
        let n = s.len();
        if idx >= n {
            return Err(JErr::Dur(idx));
        }
        match s[idx] {
            '"' => {
                let (d, e) = self.dizge(idx + 1)?;
                return Ok((J::Str(d), e));
            }
            '{' => return self.nesne(idx + 1),
            '[' => return self.dizi(idx + 1),
            'n' if idx + 3 < n && basla(s, idx, "null") => return Ok((J::Nul, idx + 4)),
            't' if idx + 3 < n && basla(s, idx, "true") => return Ok((J::Bool(true), idx + 4)),
            'f' if idx + 4 < n && basla(s, idx, "false") => return Ok((J::Bool(false), idx + 5)),
            'N' if idx + 2 < n && basla(s, idx, "NaN") => return Ok((J::Flt(f64::NAN), idx + 3)),
            'I' if idx + 7 < n && basla(s, idx, "Infinity") => return Ok((J::Flt(f64::INFINITY), idx + 8)),
            '-' if idx + 8 < n && basla(s, idx, "-Infinity") => return Ok((J::Flt(f64::NEG_INFINITY), idx + 9)),
            _ => {}
        }
        self.sayi(idx)
    }
    fn nesne(&mut self, mut idx: usize) -> Result<(J, usize), JErr> {
        if self.derin >= JSON_DERINLIK {
            return Err(JErr::Ozel("maximum recursion depth exceeded while decoding a JSON object from a unicode string".into()));
        }
        self.derin += 1;
        let n = self.s.len();
        let mut alanlar: Vec<(String, J)> = vec![];
        let mut dizin: HashMap<String, usize> = HashMap::new();
        idx = self.bosluk(idx);
        if idx >= n || self.s[idx] != '}' {
            loop {
                if idx >= n || self.s[idx] != '"' {
                    return Err(JErr::Msg("Expecting property name enclosed in double quotes", idx));
                }
                let (k, e) = self.dizge(idx + 1)?;
                idx = self.bosluk(e);
                if idx >= n || self.s[idx] != ':' {
                    return Err(JErr::Msg("Expecting ':' delimiter", idx));
                }
                idx = self.bosluk(idx + 1);
                let (v, e) = self.tara(idx)?;
                match dizin.get(&k) {
                    Some(&p) => alanlar[p].1 = v,
                    None => {
                        dizin.insert(k.clone(), alanlar.len());
                        alanlar.push((k, v));
                    }
                }
                idx = self.bosluk(e);
                if idx < n && self.s[idx] == '}' {
                    break;
                }
                if idx >= n || self.s[idx] != ',' {
                    return Err(JErr::Msg("Expecting ',' delimiter", idx));
                }
                idx = self.bosluk(idx + 1);
            }
        }
        self.derin -= 1;
        Ok((J::Dct(alanlar), idx + 1))
    }
    fn dizi(&mut self, mut idx: usize) -> Result<(J, usize), JErr> {
        if self.derin >= JSON_DERINLIK {
            return Err(JErr::Ozel("maximum recursion depth exceeded while decoding a JSON array from a unicode string".into()));
        }
        self.derin += 1;
        let n = self.s.len();
        let mut l: Vec<J> = vec![];
        idx = self.bosluk(idx);
        if idx >= n || self.s[idx] != ']' {
            loop {
                let (v, e) = self.tara(idx)?;
                l.push(v);
                idx = self.bosluk(e);
                if idx < n && self.s[idx] == ']' {
                    break;
                }
                if idx >= n || self.s[idx] != ',' {
                    return Err(JErr::Msg("Expecting ',' delimiter", idx));
                }
                idx = self.bosluk(idx + 1);
            }
        }
        self.derin -= 1;
        Ok((J::Lst(l), idx + 1))
    }
}

fn json_hata_metni(doc: &[char], msg: &str, pos: usize) -> String {
    let pos = pos.min(doc.len());
    let satir = doc[..pos].iter().filter(|&&c| c == '\n').count() + 1;
    let sutun = match doc[..pos].iter().rposition(|&c| c == '\n') {
        Some(i) => pos - i,
        None => pos + 1,
    };
    format!("{msg}: line {satir} column {sutun} (char {pos})")
}

/// `json.loads(metin)`; (değer, kayıp-vekil bayrağı) ya da `str(hata)`.
fn json_yukle(doc: &[char]) -> Result<(J, bool), String> {
    if doc.first() == Some(&'\u{feff}') {
        return Err(json_hata_metni(doc, "Unexpected UTF-8 BOM (decode using utf-8-sig)", 0));
    }
    let mut p = Jp { s: doc, derin: 0, vekil: false };
    let bas = p.bosluk(0);
    let (j, e) = match p.tara(bas) {
        Ok(r) => r,
        Err(JErr::Dur(i)) => return Err(json_hata_metni(doc, "Expecting value", i)),
        Err(JErr::Msg(m, i)) => return Err(json_hata_metni(doc, m, i)),
        Err(JErr::Ozel(m)) => return Err(m),
    };
    let e = p.bosluk(e);
    if e != doc.len() {
        return Err(json_hata_metni(doc, "Extra data", e));
    }
    Ok((j, p.vekil))
}

fn jp(parca: &str) -> String {
    format!("/{}", parca.replace('~', "~0").replace('/', "~1"))
}

type Duz = (Option<i64>, String, String, &'static str);

fn json_duzlestir(obj: &J, yol: &str, out: &mut Vec<Duz>, satir_no: Option<i64>) {
    match obj {
        J::Dct(d) => {
            for (k, v) in d {
                json_duzlestir(v, &format!("{yol}{}", jp(k)), out, satir_no);
            }
        }
        J::Lst(l) => {
            for (i, v) in l.iter().enumerate() {
                json_duzlestir(v, &format!("{yol}{}", jp(&i.to_string())), out, satir_no);
            }
        }
        _ => {
            let (tip, deger): (&'static str, String) = match obj {
                J::Nul => ("null", String::new()),
                J::Bool(b) => ("boolean", if *b { "true" } else { "false" }.to_string()),
                J::Int(s) => ("number", s.clone()),
                J::Flt(f) => (
                    "number",
                    if f.is_nan() {
                        "NaN".to_string()
                    } else if f.is_infinite() {
                        if *f > 0.0 { "Infinity" } else { "-Infinity" }.to_string()
                    } else {
                        float_repr(*f)
                    },
                ),
                J::Str(s) => ("string", s.clone()),
                _ => unreachable!(),
            };
            out.push((satir_no, if yol.is_empty() { "/".to_string() } else { yol.to_string() }, deger, tip));
        }
    }
}

// ---------------------------------------------------------------- SQLite şema
const DDL: &str = r#"
CREATE TABLE dosya (
  dosya_id TEXT PRIMARY KEY, dizin TEXT, katman TEXT, tur TEXT,
  boyut_bytes INTEGER, satir_sayisi INTEGER, blob_sha TEXT,
  ilk_commit TEXT, son_commit TEXT, baslik TEXT, token_kestirim INTEGER,
  uzanti TEXT, okunabildi INTEGER
);
CREATE TABLE kayit (
  kayit_id TEXT PRIMARY KEY, dosya_id TEXT, sira INTEGER, bolum_yolu TEXT, blok_turu TEXT,
  satir_bas INTEGER, satir_son INTEGER, metin TEXT, metin_kisa TEXT, token_kestirim INTEGER,
  tarih_ipucu TEXT, tarih_iso TEXT,
  zarf_tip TEXT, zarf_kaynak TEXT, zarf_tarih TEXT, zarf_hedef TEXT, zarf_sema TEXT,
  zarf_onem TEXT, zarf_gecerli_bitis TEXT, zarf_json TEXT,
  madde_derinlik INTEGER
);
CREATE TABLE referans (
  kayit_id TEXT, ref_turu TEXT, ref_deger TEXT, ham TEXT, konum INTEGER,
  hedef_var INTEGER, hedef_yol TEXT
);
CREATE TABLE anahtar (
  anahtar_id TEXT PRIMARY KEY, tur TEXT, deger TEXT, kaynak_dosya TEXT,
  durum TEXT, replaced_by TEXT, gecerli_bas TEXT, gecerli_bitis TEXT,
  referans_sayisi INTEGER, sicak_referans_sayisi INTEGER, ilk_gorulme TEXT, son_gorulme TEXT
);
CREATE TABLE json_kayit (
  dosya_id TEXT, satir_no INTEGER, json_yolu TEXT, deger TEXT, deger_tipi TEXT
);
CREATE TABLE uretim (
  uretim_zamani TEXT, git_head_sha TEXT, dosya_sayisi INTEGER, kayit_sayisi INTEGER,
  referans_sayisi INTEGER, sema_surumu TEXT, script_sha TEXT,
  anahtar_sayisi INTEGER, json_kayit_sayisi INTEGER, sure_sn REAL, python_surumu TEXT,
  kayit_id_kume_sha TEXT, notlar TEXT
);
CREATE TABLE parquet_uretim (
  kosum_id TEXT, tablo TEXT, durum TEXT, satir INTEGER, byte INTEGER, ms REAL,
  git_head TEXT, uretim_ts TEXT, duckdb TEXT, neden TEXT
);
CREATE INDEX ix_kayit_dosya ON kayit(dosya_id, sira);
CREATE INDEX ix_kayit_dosya_satir ON kayit(dosya_id, satir_bas, satir_son);  -- KB-53 (a) İB-26: adresli erişim (dosya + satır aralığı) bileşik indeksi, 08-22
CREATE INDEX ix_ref_kayit ON referans(kayit_id);
CREATE INDEX ix_ref_tur_deger ON referans(ref_turu, ref_deger);
CREATE INDEX ix_json_dosya ON json_kayit(dosya_id);
"#;

const GORUNUMLER: [(&str, &str); 10] = [
    (
        "v_referans_sayim",
        r#"
CREATE VIEW v_referans_sayim AS
SELECT r.ref_turu, r.ref_deger, COUNT(*) AS toplam,
       SUM(CASE WHEN d.katman='sicak' THEN 1 ELSE 0 END) AS sicak,
       SUM(CASE WHEN d.katman='ilik'  THEN 1 ELSE 0 END) AS ilik,
       SUM(CASE WHEN d.katman='soguk' THEN 1 ELSE 0 END) AS soguk,
       COUNT(DISTINCT k.dosya_id) AS dosya_sayisi
FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id JOIN dosya d ON d.dosya_id=k.dosya_id
GROUP BY r.ref_turu, r.ref_deger
ORDER BY toplam DESC, r.ref_turu, r.ref_deger"#,
    ),
    (
        "v_anahtar_terim_dosya",
        r#"
CREATE VIEW v_anahtar_terim_dosya AS
SELECT r.ref_deger AS anahtar_terim, k.dosya_id, d.katman, d.tur, COUNT(*) AS sayi
FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id JOIN dosya d ON d.dosya_id=k.dosya_id
WHERE r.ref_turu='anahtar_terim'
GROUP BY r.ref_deger, k.dosya_id
ORDER BY r.ref_deger, sayi DESC, k.dosya_id"#,
    ),
    (
        "v_zarf_kayitlar",
        r#"
CREATE VIEW v_zarf_kayitlar AS
SELECT k.kayit_id, k.dosya_id, d.katman, k.bolum_yolu, k.zarf_tip, k.zarf_kaynak, k.zarf_tarih,
       k.zarf_hedef, k.zarf_sema, k.zarf_onem, k.zarf_gecerli_bitis, k.zarf_json, k.metin_kisa
FROM kayit k JOIN dosya d ON d.dosya_id=k.dosya_id
WHERE k.zarf_json IS NOT NULL
ORDER BY k.dosya_id, k.sira"#,
    ),
    (
        "v_dosya_envanter",
        r#"
CREATE VIEW v_dosya_envanter AS
SELECT dosya_id, dizin, katman, tur, boyut_bytes, satir_sayisi, token_kestirim,
       ilk_commit, son_commit, blob_sha, baslik
FROM dosya
ORDER BY katman, tur, dosya_id"#,
    ),
    (
        "v_bolum_yogunluk",
        r#"
CREATE VIEW v_bolum_yogunluk AS
SELECT dosya_id, bolum_yolu, COUNT(*) AS kayit_sayisi, SUM(token_kestirim) AS token,
       MIN(satir_bas) AS satir_bas, MAX(satir_son) AS satir_son
FROM kayit
GROUP BY dosya_id, bolum_yolu
ORDER BY dosya_id, MIN(sira)"#,
    ),
    (
        "v_kirik_pointer",
        r#"
CREATE VIEW v_kirik_pointer AS
SELECT r.ref_deger AS yol,
       CASE WHEN instr(r.ref_deger,'/')>0 THEN 'yol' ELSE 'ciplak_ad' END AS yol_bicimi,
       COUNT(*) AS sayi, COUNT(DISTINCT k.dosya_id) AS dosya_sayisi,
       MIN(k.dosya_id) AS ilk_dosya, MIN(r.kayit_id) AS ilk_kayit
FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id
WHERE r.ref_turu='dosya_pointer' AND r.hedef_var=0
GROUP BY r.ref_deger
ORDER BY sayi DESC, yol"#,
    ),
    (
        "v_celiski_adayi",
        r#"
CREATE VIEW v_celiski_adayi AS
SELECT r.ref_deger AS anahtar_terim, k.dosya_id,
       SUM(CASE WHEN k.zarf_gecerli_bitis IS NOT NULL AND k.zarf_gecerli_bitis<>'' AND k.zarf_gecerli_bitis<>'-' THEN 1 ELSE 0 END) AS bitisli,
       SUM(CASE WHEN k.zarf_gecerli_bitis IS NULL OR k.zarf_gecerli_bitis='' OR k.zarf_gecerli_bitis='-' THEN 1 ELSE 0 END) AS bitissiz
FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id
WHERE r.ref_turu='anahtar_terim' AND k.zarf_json IS NOT NULL
GROUP BY r.ref_deger, k.dosya_id
HAVING bitisli>0 AND bitissiz>0
ORDER BY anahtar_terim, k.dosya_id"#,
    ),
    (
        "v_boyut_anahtar",
        r#"
CREATE VIEW v_boyut_anahtar AS
SELECT a.anahtar_id, a.tur, a.deger, a.durum, a.replaced_by,
       a.gecerli_bas, a.gecerli_bitis,
       a.referans_sayisi, a.sicak_referans_sayisi, a.ilk_gorulme, a.son_gorulme
FROM anahtar a
ORDER BY a.tur, a.anahtar_id"#,
    ),
    (
        "v_olgu_referans",
        r#"
CREATE VIEW v_olgu_referans AS
SELECT r.kayit_id, r.ref_turu, r.ref_deger, r.hedef_var, r.hedef_yol,
       k.dosya_id, d.katman, d.tur AS dosya_turu, k.bolum_yolu,
       COALESCE(k.tarih_iso, k.zarf_tarih) AS olay_tarihi,
       d.son_commit AS dosya_son_commit,
       CASE WHEN COALESCE(k.tarih_iso, k.zarf_tarih) IS NOT NULL THEN 'zamanli' ELSE 'zamansiz' END AS zaman_grain
FROM referans r
JOIN kayit k ON k.kayit_id = r.kayit_id
JOIN dosya d ON d.dosya_id = k.dosya_id"#,
    ),
    (
        "v_x_olcum",
        r#"
CREATE VIEW v_x_olcum AS
WITH sirali AS (
  SELECT d.katman, k.blok_turu, k.token_kestirim,
         ROW_NUMBER() OVER (PARTITION BY d.katman, k.blok_turu ORDER BY k.token_kestirim) AS rn,
         COUNT(*)     OVER (PARTITION BY d.katman, k.blok_turu) AS n
  FROM kayit k JOIN dosya d ON d.dosya_id = k.dosya_id
  WHERE k.token_kestirim IS NOT NULL
)
SELECT katman, blok_turu, MAX(n) AS birim_sayisi,
       MIN(token_kestirim) AS token_min,
       MAX(CASE WHEN rn = (n + 1) / 2 THEN token_kestirim END) AS token_medyan,
       MAX(token_kestirim) AS token_maks,
       ROUND(AVG(token_kestirim), 1) AS token_ortalama,
       SUM(token_kestirim) AS token_toplam,
       'bytes/4 kestirimi; Türkçe dil-çarpanı ölçülmemiş (rapor-8 C-kör)' AS olcum_serhi
FROM sirali
GROUP BY katman, blok_turu
ORDER BY katman, token_toplam DESC"#,
    ),
];

// ---------------------------------------------------------------- Ana akış
struct Notlar {
    utf8_hatasi: Vec<String>,
    json_hatasi: Vec<String>,
    kayit_id_cakisma: i64,
    csv_kesildi: Vec<String>,
    cekim_olay_dosya: i64,
}

fn notlar_json(n: &Notlar) -> String {
    let dz = |v: &Vec<String>| Value::Array(v.iter().map(|s| Value::String(s.clone())).collect());
    // sort_keys=True sırası
    let mut o = Map::new();
    o.insert("cekim_olay_dosya".into(), Value::from(n.cekim_olay_dosya));
    o.insert("csv_kesildi".into(), dz(&n.csv_kesildi));
    o.insert("json_hatasi".into(), dz(&n.json_hatasi));
    o.insert("kayit_id_cakisma".into(), Value::from(n.kayit_id_cakisma));
    o.insert("utf8_hatasi".into(), dz(&n.utf8_hatasi));
    py_dumps(&Value::Object(o))
}

fn utf8_hata_metni(ham: &[u8], e: &std::str::Utf8Error) -> String {
    let bas = e.valid_up_to();
    let (son, neden) = match e.error_len() {
        Some(n) => {
            let b = ham[bas];
            (bas + n, if (0x80..0xC2).contains(&b) || b > 0xF4 { "invalid start byte" } else { "invalid continuation byte" })
        }
        None => (ham.len(), "unexpected end of data"),
    };
    if son - bas == 1 {
        format!("'utf-8' codec can't decode byte 0x{:02x} in position {}: {}", ham[bas], bas, neden)
    } else {
        format!("'utf-8' codec can't decode bytes in position {}-{}: {}", bas, son - 1, neden)
    }
}

struct Kayit {
    id: String,
    dosya: String,
    sira: i64,
    bolum: String,
    tur: &'static str,
    bas: i64,
    son: i64,
    metin: String,
    kisa: String,
    tok: i64,
    t_ip: Option<String>,
    t_iso: Option<String>,
    z: [Option<String>; 8], // tip kaynak tarih hedef sema onem gecerli-bitis json
    derinlik: i64,
}

struct DosyaSatir {
    id: String,
    dizin: String,
    katman: &'static str,
    tur: &'static str,
    boyut: i64,
    satir: i64,
    blob: String,
    ilk: String,
    son: String,
    baslik: String,
    tok: i64,
    uzanti: String,
    okunabildi: i64,
}

fn csv_alan(s: &str) -> String {
    if s.contains([',', '"', '\n']) { format!("\"{}\"", s.replace('"', "\"\"")) } else { s.to_string() }
}

fn ayrisan() -> Ayrisan {
    Ayrisan::yeni(
        "baglam-tablo.py",
        Some("JARVIS bağlam → veri tablosu (şema v0)"),
        vec![
            Secenek::deger(&["--repo"], "repo", Some("repo kökü (varsayılan: tools/'un üstü)")),
            Secenek::deger(&["--cikti"], "cikti", Some("çıktı dizini (varsayılan: <repo>/veri)")),
            Secenek::bayrak(&["--sessiz"], "sessiz", None),
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

fn sq(e: rusqlite::Error) -> String {
    format!("sqlite3.Error: {e}")
}

fn io(e: std::io::Error) -> String {
    format!("OSError: {e}")
}

fn calis(a: &crate::argparse::Sonuc) -> Sn<i32> {
    let t0 = std::time::Instant::now();
    let cwd = std::env::current_dir().map(|d| d.to_string_lossy().into_owned()).unwrap_or_default();
    // Python varsayılanı betiğin üst-üst dizini; Rust ikilisinde betik yok → çalışma dizini (silver-saglik ile aynı kural).
    let repo = py::abspath(a.metin("repo").filter(|s| !s.is_empty()).unwrap_or(&cwd));
    let cikti = match a.metin("cikti").filter(|s| !s.is_empty()) {
        Some(c) => py::abspath(c),
        None => py::join(&repo, "veri"),
    };

    // D1: git ls-files başarısız → repo değil → DUR
    let p = match git(&repo, &["ls-files", "-z"], true) {
        Ok(p) => p,
        Err(e) => return Ok(fail_loud(&format!("`git ls-files` başarısız (repo değil?): {e}"))),
    };
    let mut tum_yollar: Vec<String> = String::from_utf8_lossy(&p.out).split('\0').filter(|y| !y.is_empty()).map(String::from).collect();
    tum_yollar.sort();
    if tum_yollar.is_empty() {
        return Ok(fail_loud("`git ls-files` boş döndü — izlenen dosya yok"));
    }
    let repo_yollar: HashSet<String> = tum_yollar.iter().cloned().collect();
    let mut repo_adlar: HashMap<String, String> = HashMap::new();
    for y in &tum_yollar {
        repo_adlar.entry(basename(y).to_string()).or_insert_with(|| y.clone());
    }
    let hedef_yollar: Vec<String> = tum_yollar
        .iter()
        .filter(|y| {
            let l = y.to_lowercase();
            l.ends_with(".md") || l.ends_with(".json") || l.ends_with(".jsonl")
        })
        .cloned()
        .collect();

    let head = {
        let o = git(&repo, &["rev-parse", "HEAD"], false)?;
        let s = String::from_utf8(o.out).map_err(|_| "UnicodeDecodeError: git rev-parse HEAD".to_string())?;
        let s = py::strip(&s).to_string();
        if s.is_empty() { "-".to_string() } else { s }
    };
    let meta = git_meta(&repo, &hedef_yollar)?;

    let skill_kok = py::join(&py::join(&repo, ".claude"), "skills");
    let mut skill_adlari: Vec<String> = vec![];
    if Path::new(&skill_kok).is_dir()
        && let Ok(rd) = std::fs::read_dir(&skill_kok)
    {
        for e in rd.flatten() {
            let ad = e.file_name().to_string_lossy().into_owned();
            if Path::new(&py::join(&py::join(&skill_kok, &ad), "SKILL.md")).is_file() {
                skill_adlari.push(ad);
            }
        }
    }
    skill_adlari.sort();
    let skill = SkillEs { adlar: skill_adlari.iter().map(|s| s.chars().collect()).collect(), kume: skill_adlari.iter().cloned().collect() };
    let terimler: Vec<(String, Vec<Option<char>>)> = ANAHTAR_TERIMLER.iter().map(|(d, g)| (d.to_string(), terim_belirtec(g))).collect();
    let baglam = Baglam { skill: &skill, repo_yollar: &repo_yollar, repo_adlar: &repo_adlar, repo_kok: &repo, terimler: &terimler };

    let mut notlar = Notlar { utf8_hatasi: vec![], json_hatasi: vec![], kayit_id_cakisma: 0, csv_kesildi: vec![], cekim_olay_dosya: 0 };
    let mut dosya_rows: Vec<DosyaSatir> = vec![];
    let mut kayit_rows: Vec<Kayit> = vec![];
    let mut ref_rows: Vec<(usize, Ref)> = vec![];
    let mut json_rows: Vec<(String, Option<i64>, String, String, &'static str)> = vec![];
    let mut gorulen_id: HashSet<String> = HashSet::new();

    for yol in &hedef_yollar {
        let tam = py::join(&repo, yol);
        let ham = std::fs::read(&tam).map_err(|e| format!("FileNotFoundError: {tam}: {e}"))?;
        let boyut = ham.len();
        let blob = git_blob_sha(&ham);
        let (ilk_c, son_c) = meta.get(yol).cloned().unwrap_or(("-".into(), "-".into()));
        let uzanti = uzanti_bul(yol).to_lowercase();
        let dizin = if yol.contains('/') { yol.split('/').next().unwrap().to_string() } else { ".".to_string() };
        let mut okunabildi = 1i64;
        let metin: Option<String> = match std::str::from_utf8(&ham) {
            Ok(s) => {
                let s = s.strip_prefix('\u{feff}').unwrap_or(s);
                Some(s.replace("\r\n", "\n").replace('\r', "\n"))
            }
            Err(e) => {
                okunabildi = 0;
                notlar.utf8_hatasi.push(format!("{yol}: {}", py::ilk(&utf8_hata_metni(&ham, &e), 80)));
                None
            }
        };
        let satir_sayisi = match &metin {
            Some(m) => m.matches('\n').count() + if m.ends_with('\n') || m.is_empty() { 0 } else { 1 },
            None => ham.iter().filter(|&&b| b == b'\n').count() + if ham.ends_with(b"\n") || ham.is_empty() { 0 } else { 1 },
        };
        let mut baslik = basename(yol).to_string();
        let tur = if okunabildi == 1 { tur_bul(yol) } else { "diger" };
        let katman = katman_bul(yol);

        if let (Some(metin), ".md") = (&metin, uzanti.as_str()) {
            // re.search(r"^# +(.+?)\s*$", metin, re.M)
            for satir in metin.split('\n') {
                if let Some(r) = satir.strip_prefix('#') {
                    let bosluk = r.chars().take_while(|&c| c == ' ').count();
                    let icerik: String = r.chars().skip(bosluk).collect();
                    if bosluk >= 1 && (!icerik.is_empty() || bosluk >= 2) {
                        baslik = py::strip(&icerik).to_string();
                        break;
                    }
                }
            }
            let bloklar = md_bloklar(metin);
            let mut yol_stack: BTreeMap<usize, String> = BTreeMap::new();
            let dizin_yol = dirname(yol);
            for (sira, b) in bloklar.iter().enumerate() {
                if b.tur == "baslik" {
                    let sev = b.seviye;
                    yol_stack.retain(|s, _| *s < sev);
                    yol_stack.insert(sev, b.baslik.clone());
                }
                let bolum_yolu = yol_stack.iter().filter(|(s, _)| **s <= 3).map(|(_, v)| v.as_str()).collect::<Vec<_>>().join(" › ");
                let mt = &b.metin;
                let mut kid = format!("{yol}#{}-{}#{}", b.bas, b.son, &sha1_hex(mt.as_bytes())[..8]);
                if gorulen_id.contains(&kid) {
                    let mut n = 2;
                    while gorulen_id.contains(&format!("{kid}~{n}")) {
                        n += 1;
                    }
                    kid = format!("{kid}~{n}");
                    notlar.kayit_id_cakisma += 1;
                }
                gorulen_id.insert(kid.clone());
                let mut kisa = String::new();
                let mut onceki_bosluk = false;
                for ch in mt.chars() {
                    if ws(ch) {
                        if !onceki_bosluk {
                            kisa.push(' ');
                        }
                        onceki_bosluk = true;
                    } else {
                        kisa.push(ch);
                        onceki_bosluk = false;
                    }
                }
                let kisa = py::ilk(py::strip(&kisa), 200);
                let mc: Vec<char> = mt.chars().collect();
                let (t_ip, t_iso) = tarih_ipucu_bul(&mc);
                let mut z: [Option<String>; 8] = Default::default();
                if let Some(zr) = zarf_ayristir(&mc) {
                    let al = &zr.alanlar;
                    if zr.tam {
                        for (k, anahtar) in ["tip", "kaynak", "tarih", "hedef", "sema", "onem", "gecerli-bitis"].iter().enumerate() {
                            z[k] = al.get(*anahtar).cloned();
                        }
                        z[7] = Some(zarf_json(al, false));
                    } else {
                        z[7] = Some(zarf_json(al, true));
                    }
                }
                let idx = kayit_rows.len();
                kayit_rows.push(Kayit {
                    id: kid,
                    dosya: yol.clone(),
                    sira: sira as i64,
                    bolum: bolum_yolu,
                    tur: b.tur,
                    bas: b.bas as i64,
                    son: b.son as i64,
                    metin: mt.clone(),
                    kisa,
                    tok: token_kestirim(mt),
                    t_ip,
                    t_iso,
                    z,
                    derinlik: b.derinlik as i64,
                });
                for r in referanslar(&mc, &baglam, &dizin_yol) {
                    ref_rows.push((idx, r));
                }
            }
        } else if let Some(metin) = &metin
            && (uzanti == ".json" || uzanti == ".jsonl")
            && !JSON_HARIC.contains(&yol.as_str())
        {
            let mut duz: Vec<Duz> = vec![];
            let sonuc: Result<(), String> = (|| {
                if uzanti == ".json" {
                    let c: Vec<char> = metin.chars().collect();
                    let (j, vekil) = json_yukle(&c)?;
                    json_duzlestir(&j, "", &mut duz, None);
                    if vekil {
                        return Err("\u{0}VEKIL".into());
                    }
                } else {
                    for (no, satir) in metin.split('\n').enumerate() {
                        if py::strip(satir).is_empty() {
                            continue;
                        }
                        let c: Vec<char> = satir.chars().collect();
                        let (j, vekil) = json_yukle(&c)?;
                        json_duzlestir(&j, "", &mut duz, Some(no as i64 + 1));
                        if vekil {
                            return Err("\u{0}VEKIL".into());
                        }
                    }
                }
                Ok(())
            })();
            if let Err(e) = sonuc {
                if e == "\u{0}VEKIL" {
                    return Err("UnicodeEncodeError: 'utf-8' codec can't encode character (surrogates not allowed)".into());
                }
                notlar.json_hatasi.push(format!("{yol}: {}", py::ilk(&e, 80)));
                duz.clear();
            }
            for (no, jy, dg, tp) in duz {
                json_rows.push((yol.clone(), no, jy, dg, tp));
            }
        }
        dosya_rows.push(DosyaSatir {
            id: yol.clone(),
            dizin,
            katman,
            tur,
            boyut: boyut as i64,
            satir: satir_sayisi as i64,
            blob,
            ilk: ilk_c,
            son: son_c,
            baslik,
            tok: ((boyut + 3) / 4) as i64,
            uzanti: uzanti.trim_start_matches('.').to_string(),
            okunabildi,
        });
    }

    // ---- anahtar tablosu (gözlenen) ----
    let katman_of: HashMap<&str, &str> = dosya_rows.iter().map(|r| (r.id.as_str(), r.katman)).collect();
    let son_commit_of: HashMap<&str, &str> = dosya_rows.iter().map(|r| (r.id.as_str(), r.son.as_str())).collect();
    type Anahtar = (&'static str, String);
    let mut ref_say: HashMap<Anahtar, i64> = HashMap::new();
    let mut ref_sicak: HashMap<Anahtar, i64> = HashMap::new();
    let mut ref_dosyalar: HashMap<Anahtar, HashSet<&str>> = HashMap::new();
    let mut gozlenen: HashMap<&'static str, BTreeSet<String>> = HashMap::new();
    for (ki, r) in &ref_rows {
        let d = kayit_rows[*ki].dosya.as_str();
        let key = (r.tur, r.deger.clone());
        *ref_say.entry(key.clone()).or_default() += 1;
        if katman_of.get(d) == Some(&"sicak") {
            *ref_sicak.entry(key.clone()).or_default() += 1;
        }
        ref_dosyalar.entry(key).or_default().insert(d);
        gozlenen.entry(r.tur).or_default().insert(r.deger.clone());
    }
    struct AnahtarSatir {
        id: String,
        tur: String,
        deger: String,
        kaynak: String,
        say: i64,
        sicak: i64,
        ilk: Option<String>,
        son: Option<String>,
    }
    let mut anahtar_rows: Vec<AnahtarSatir> = vec![];
    let eslesme = |t: &str| -> &'static str {
        match t {
            "skill" => "skill_adi",
            "kart" => "kart",
            "tuzuk_madde" => "tuzuk_madde",
            "v_no" => "v_no",
            "anahtar_terim" => "anahtar_terim",
            _ => "wiki_link",
        }
    };
    let anahtar_ekle = |tur: &str, deger: &str, kaynak: &str, rows: &mut Vec<AnahtarSatir>| {
        let key = (eslesme(tur), deger.to_string());
        let mut tarihler: Vec<&str> = ref_dosyalar.get(&key).map(|s| s.iter().map(|d| *son_commit_of.get(d).unwrap_or(&"-")).filter(|t| *t != "-").collect()).unwrap_or_default();
        tarihler.sort();
        let (ilk, son) = match (tarihler.first(), tarihler.last()) {
            (Some(a), Some(b)) => (Some(a.to_string()), Some(b.to_string())),
            _ => (None, None),
        };
        rows.push(AnahtarSatir {
            id: format!("{tur}:{deger}"),
            tur: tur.to_string(),
            deger: deger.to_string(),
            kaynak: kaynak.to_string(),
            say: ref_say.get(&key).copied().unwrap_or(0),
            sicak: ref_sicak.get(&key).copied().unwrap_or(0),
            ilk,
            son,
        });
    };
    for s in &skill_adlari {
        anahtar_ekle("skill", s, &format!(".claude/skills/{s}/SKILL.md"), &mut anahtar_rows);
    }
    for (deger, _) in &terimler {
        anahtar_ekle("anahtar_terim", deger, "-", &mut anahtar_rows);
    }
    let mut wiki_sayfalar: HashMap<String, String> = HashMap::new();
    for y in &hedef_yollar {
        if y.starts_with("wiki/") && y.ends_with(".md") {
            wiki_sayfalar.insert(govde_bul(basename(y)), y.clone());
        }
    }
    let bos: BTreeSet<String> = BTreeSet::new();
    for k in gozlenen.get("kart").unwrap_or(&bos) {
        anahtar_ekle("kart", k, "core/pano.md", &mut anahtar_rows);
    }
    let mut tuzukler: Vec<&String> = gozlenen.get("tuzuk_madde").unwrap_or(&bos).iter().collect();
    tuzukler.sort_by_key(|s| {
        let mut it = s.split('.');
        let a = it.next().unwrap_or("").to_string();
        let ikinci = it.next().unwrap_or("");
        let sayi: String = ikinci.chars().filter(|c| c.is_ascii_digit()).collect();
        (a, sayi.parse::<i64>().unwrap_or(0), s.to_string())
    });
    for k in tuzukler {
        anahtar_ekle("tuzuk_madde", k, "core/tuzuk-v0.md", &mut anahtar_rows);
    }
    let mut vnolar: Vec<&String> = gozlenen.get("v_no").unwrap_or(&bos).iter().collect();
    vnolar.sort_by_key(|s| s[1..].parse::<i64>().unwrap_or(0));
    for k in vnolar {
        anahtar_ekle("v_no", k, "-", &mut anahtar_rows);
    }
    let mut wikiler: BTreeSet<String> = wiki_sayfalar.keys().cloned().collect();
    wikiler.extend(gozlenen.get("wiki_link").unwrap_or(&bos).iter().cloned());
    for k in &wikiler {
        let kaynak = wiki_sayfalar.get(k).cloned().unwrap_or_else(|| "-".to_string());
        anahtar_ekle("wiki_sayfa", k, &kaynak, &mut anahtar_rows);
    }

    // ---- SQLite yaz (tmp → replace) ----
    std::fs::create_dir_all(py::join(&cikti, "gorunum")).map_err(io)?;
    let db_yolu = py::join(&cikti, "baglam.sqlite");
    let tmp_yolu = format!("{db_yolu}.tmp");
    if Path::new(&tmp_yolu).exists() {
        std::fs::remove_file(&tmp_yolu).map_err(io)?;
    }
    let con = Connection::open(&tmp_yolu).map_err(sq)?;
    con.execute_batch(DDL).map_err(sq)?;
    for (_ad, sql) in &GORUNUMLER {
        con.execute(sql, []).map_err(sq)?;
    }
    con.execute_batch("BEGIN").map_err(sq)?;
    {
        let mut st = con.prepare("INSERT INTO dosya VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)").map_err(sq)?;
        for r in &dosya_rows {
            st.execute(rusqlite::params![r.id, r.dizin, r.katman, r.tur, r.boyut, r.satir, r.blob, r.ilk, r.son, r.baslik, r.tok, r.uzanti, r.okunabildi]).map_err(sq)?;
        }
        let mut st = con.prepare(&format!("INSERT INTO kayit VALUES ({})", ["?"; 21].join(","))).map_err(sq)?;
        for r in &kayit_rows {
            let p: [&dyn ToSql; 21] = [
                &r.id, &r.dosya, &r.sira, &r.bolum, &r.tur, &r.bas, &r.son, &r.metin, &r.kisa, &r.tok, &r.t_ip, &r.t_iso, &r.z[0], &r.z[1], &r.z[2], &r.z[3], &r.z[4], &r.z[5], &r.z[6], &r.z[7], &r.derinlik,
            ];
            st.execute(&p[..]).map_err(sq)?;
        }
        let mut st = con.prepare("INSERT INTO referans VALUES (?,?,?,?,?,?,?)").map_err(sq)?;
        for (ki, r) in &ref_rows {
            st.execute(rusqlite::params![kayit_rows[*ki].id, r.tur, r.deger, r.ham, r.konum, r.hedef_var, r.hedef_yol]).map_err(sq)?;
        }
        let mut st = con.prepare("INSERT INTO anahtar VALUES (?,?,?,?,?,?,?,?,?,?,?,?)").map_err(sq)?;
        for r in &anahtar_rows {
            st.execute(rusqlite::params![r.id, r.tur, r.deger, r.kaynak, "gozlenen", None::<String>, None::<String>, None::<String>, r.say, r.sicak, r.ilk, r.son]).map_err(sq)?;
        }
        let mut st = con.prepare("INSERT INTO json_kayit VALUES (?,?,?,?,?)").map_err(sq)?;
        for (d, no, jy, dg, tp) in &json_rows {
            st.execute(rusqlite::params![d, no, jy, dg, tp]).map_err(sq)?;
        }
    }

    // ---- İB-52: ADDITIVE iki kolon (kaynak_tarihi · cekim_tarihi) ----
    con.execute("ALTER TABLE kayit ADD COLUMN cekim_tarihi TEXT", []).map_err(sq)?;
    con.execute("ALTER TABLE kayit ADD COLUMN kaynak_tarihi TEXT", []).map_err(sq)?;
    let gun = "'[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]*'";
    con.execute(
        &format!("UPDATE kayit SET kaynak_tarihi = CASE WHEN tarih_iso GLOB {gun} THEN substr(tarih_iso,1,10) WHEN zarf_tarih GLOB {gun} THEN substr(zarf_tarih,1,10) END"),
        [],
    )
    .map_err(sq)?;
    con.execute("UPDATE kayit SET cekim_tarihi = (SELECT substr(d.son_commit,1,10) FROM dosya d WHERE d.dosya_id=kayit.dosya_id)", []).map_err(sq)?;
    let mut cekim_son: BTreeMap<String, String> = BTreeMap::new();
    let cekim_yolu = py::join(&py::join(&cikti, "bronz"), "cekim-olay.jsonl");
    if Path::new(&cekim_yolu).exists() {
        let b = std::fs::read(&cekim_yolu).map_err(io)?;
        let s = String::from_utf8(b).map_err(|_| "UnicodeDecodeError: 'utf-8' codec can't decode (cekim-olay.jsonl)".to_string())?;
        let s = s.replace("\r\n", "\n").replace('\r', "\n");
        for line in s.split('\n') {
            let line = py::strip(line);
            if line.is_empty() || line.starts_with('#') {
                continue;
            }
            let c: Vec<char> = line.chars().collect();
            let Ok((o, _vekil)) = json_yukle(&c) else { continue };
            let J::Dct(d) = o else {
                return Err("AttributeError: object has no attribute 'get'".into());
            };
            let al = |k: &str| d.iter().find(|(n, _)| n == k).map(|(_, v)| v);
            let truthy = |v: Option<&J>| match v {
                None | Some(J::Nul) => false,
                Some(J::Bool(b)) => *b,
                Some(J::Int(s)) => s != "0",
                Some(J::Flt(f)) => *f != 0.0,
                Some(J::Str(s)) => !s.is_empty(),
                Some(J::Lst(l)) => !l.is_empty(),
                Some(J::Dct(l)) => !l.is_empty(),
            };
            let dosya = match al("dosya_id") {
                Some(J::Str(s)) if !s.is_empty() => Some(s.clone()),
                v if !truthy(v) => None,
                _ => return Err("TypeError: dosya_id türü desteklenmiyor".into()),
            };
            let t = match al("cekim_tarihi") {
                Some(J::Str(s)) => py::ilk(s, 10),
                v if !truthy(v) => String::new(),
                _ => return Err("TypeError: cekim_tarihi türü desteklenmiyor".into()),
            };
            if let Some(dd) = dosya
                && !t.is_empty()
                && t.as_str() > cekim_son.get(&dd).map(String::as_str).unwrap_or("")
            {
                cekim_son.insert(dd, t);
            }
        }
        for (d, t) in &cekim_son {
            con.execute("UPDATE kayit SET cekim_tarihi=? WHERE dosya_id=? AND (cekim_tarihi IS NULL OR cekim_tarihi<?)", rusqlite::params![t, d, t]).map_err(sq)?;
        }
    }
    notlar.cekim_olay_dosya = cekim_son.len() as i64;

    let mut idler: Vec<&str> = kayit_rows.iter().map(|r| r.id.as_str()).collect();
    idler.sort();
    let kume_sha = sha1_hex(idler.join("\n").as_bytes());
    // Python: betiğin kendi baytlarının sha1'i; Rust ikilisinin betiği yoktur → repo/tools/baglam-tablo.py (yedek Python kaynağı).
    let script_sha = match std::fs::read(py::join(&py::join(&repo, "tools"), "baglam-tablo.py")) {
        Ok(b) => sha1_hex(&b),
        Err(_) => sha1_hex(b"baglam-tablo-rust"),
    };
    let uretim_zamani = chrono::Local::now().format("%Y-%m-%dT%H:%M:%S%:z").to_string();
    let sure: f64 = format!("{:.2}", t0.elapsed().as_secs_f64()).parse().unwrap_or(0.0);
    con.execute(
        "INSERT INTO uretim VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
        rusqlite::params![
            uretim_zamani,
            head,
            dosya_rows.len() as i64,
            kayit_rows.len() as i64,
            ref_rows.len() as i64,
            SEMA_SURUMU,
            script_sha,
            anahtar_rows.len() as i64,
            json_rows.len() as i64,
            sure,
            "rust",
            kume_sha,
            notlar_json(&notlar)
        ],
    )
    .map_err(sq)?;
    con.execute_batch("COMMIT").map_err(sq)?;

    // ---- CSV görünümler ----
    for (ad, _sql) in &GORUNUMLER {
        let mut st = con.prepare(&format!("SELECT * FROM {ad}")).map_err(sq)?;
        let kolonlar: Vec<String> = st.column_names().iter().map(|s| s.to_string()).collect();
        let mut satirlar: Vec<Vec<String>> = vec![];
        {
            let mut rows = st.query([]).map_err(sq)?;
            while let Some(r) = rows.next().map_err(sq)? {
                let mut alanlar = vec![];
                for i in 0..kolonlar.len() {
                    alanlar.push(match r.get_ref(i).map_err(sq)? {
                        ValueRef::Null => String::new(),
                        ValueRef::Integer(n) => n.to_string(),
                        ValueRef::Real(f) => float_repr(f),
                        ValueRef::Text(t) => String::from_utf8_lossy(t).into_owned(),
                        ValueRef::Blob(b) => format!("b{}", py::repr(&String::from_utf8_lossy(b))),
                    });
                }
                satirlar.push(alanlar);
            }
        }
        let mut csv = String::new();
        csv.push_str(&kolonlar.iter().map(|k| csv_alan(k)).collect::<Vec<_>>().join(","));
        csv.push('\n');
        for r in satirlar.iter().take(CSV_SATIR_TAVANI) {
            csv.push_str(&r.iter().map(|v| csv_alan(v)).collect::<Vec<_>>().join(","));
            csv.push('\n');
        }
        if satirlar.len() > CSV_SATIR_TAVANI {
            let mut alanlar = vec![format!("# UYARI: {} satırın ilk {}'i yazıldı; tam küme veri/baglam.sqlite {}", satirlar.len(), CSV_SATIR_TAVANI, ad)];
            alanlar.extend(std::iter::repeat_n(String::new(), kolonlar.len() - 1));
            csv.push_str(&alanlar.iter().map(|v| csv_alan(v)).collect::<Vec<_>>().join(","));
            csv.push('\n');
            notlar.csv_kesildi.push(format!("{ad}:{}", satirlar.len()));
        }
        let csv_yolu = py::join(&py::join(&cikti, "gorunum"), &format!("{ad}.csv"));
        std::fs::write(&csv_yolu, csv.as_bytes()).map_err(io)?;
    }
    if !notlar.csv_kesildi.is_empty() {
        con.execute("UPDATE uretim SET notlar=?", rusqlite::params![notlar_json(&notlar)]).map_err(sq)?;
    }
    let _ = con.close();
    std::fs::rename(&tmp_yolu, &db_yolu).map_err(io)?;

    // ---- JSONL (kayit tablosu; deterministik sıra) ----
    let mut jl = String::new();
    for r in &kayit_rows {
        let ov = |o: &Option<String>| o.as_ref().map(|s| Value::String(s.clone())).unwrap_or(Value::Null);
        let mut m: BTreeMap<&str, Value> = BTreeMap::new();
        m.insert("kayit_id", Value::String(r.id.clone()));
        m.insert("dosya_id", Value::String(r.dosya.clone()));
        m.insert("sira", Value::from(r.sira));
        m.insert("bolum_yolu", Value::String(r.bolum.clone()));
        m.insert("blok_turu", Value::String(r.tur.to_string()));
        m.insert("satir_bas", Value::from(r.bas));
        m.insert("satir_son", Value::from(r.son));
        m.insert("metin", Value::String(r.metin.clone()));
        m.insert("metin_kisa", Value::String(r.kisa.clone()));
        m.insert("token_kestirim", Value::from(r.tok));
        m.insert("tarih_ipucu", ov(&r.t_ip));
        m.insert("tarih_iso", ov(&r.t_iso));
        for (k, ad) in ["zarf_tip", "zarf_kaynak", "zarf_tarih", "zarf_hedef", "zarf_sema", "zarf_onem", "zarf_gecerli_bitis", "zarf_json"].iter().enumerate() {
            m.insert(ad, ov(&r.z[k]));
        }
        m.insert("madde_derinlik", Value::from(r.derinlik));
        let mut o = Map::new();
        for (k, v) in m {
            o.insert(k.to_string(), v);
        }
        jl.push_str(&py_dumps(&Value::Object(o)));
        jl.push('\n');
    }
    std::fs::write(py::join(&cikti, "baglam.jsonl"), jl.as_bytes()).map_err(io)?;

    let sure = format!("{:.2}", t0.elapsed().as_secs_f64()).parse::<f64>().unwrap_or(0.0);
    if !a.bayrak("sessiz") {
        let mut ozet = Map::new();
        ozet.insert("dosya".into(), Value::from(dosya_rows.len()));
        ozet.insert("kayit".into(), Value::from(kayit_rows.len()));
        ozet.insert("referans".into(), Value::from(ref_rows.len()));
        ozet.insert("anahtar".into(), Value::from(anahtar_rows.len()));
        ozet.insert("json_kayit".into(), Value::from(json_rows.len()));
        ozet.insert("sure_sn".into(), serde_json::Number::from_f64(sure).map(Value::Number).unwrap_or(Value::Null));
        ozet.insert("kayit_id_kume_sha".into(), Value::String(kume_sha));
        ozet.insert("git_head".into(), Value::String(py::ilk(&head, 12)));
        ozet.insert("utf8_hatasi".into(), Value::from(notlar.utf8_hatasi.len()));
        ozet.insert("json_hatasi".into(), Value::from(notlar.json_hatasi.len()));
        ozet.insert("kayit_id_cakisma".into(), Value::from(notlar.kayit_id_cakisma));
        ozet.insert("csv_kesildi".into(), Value::Array(notlar.csv_kesildi.iter().map(|s| Value::String(s.clone())).collect()));
        ozet.insert("cikti".into(), Value::String(cikti.clone()));
        py::print(&py::json_girintili(&Value::Object(ozet)));
    }
    Ok(0)
}
