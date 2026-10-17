//! `tools/bayat-cekim.py` karşılığı: D3 BAYATLIK KUYRUĞU BOŞALTMA (anakronizm M6; KB-68 (a) Karar 69 EK; İB-52).
//! `veri/gorunum/v_bayat_aday.csv` kuyruğunu okur; `--kaydet` bronz `veri/bronz/cekim-olay.jsonl`'a olay ekler,
//! `--olcum` `veri/katman-olcum.jsonl`'a ölçüm satırı ekler. Çıkış: 0 tamam · 2 girdi hatası.
//! Not: Python `csv.DictReader(raw.splitlines())` davranışı (tırnaklı alanda satır sonu kaybolur) aşağıda birebir taklit edilir.
use crate::argparse::{Ayrisan, Secenek};
use crate::py::{self, iso_tarih, sha1_hex};
use jarvis_hook::ortak::{py_dilim, py_dumps, py_isabs, py_str, ts_istanbul};
use serde_json::{Map, Value};
use std::collections::HashMap;
use std::io::Write;
use std::path::Path;

/// Python'da yakalanmamış istisna → `py::coker` (çıkış 1).
type Sn<T> = Result<T, String>;

type Satir = HashMap<String, Option<String>>;

// ---------------------------------------------------------------- yardımcılar
/// Python `csv.reader(satırlar)` (varsayılan lehçe, katı olmayan) — satırlar `splitlines()` ile gelir, sonlandırıcı yoktur:
/// tırnaklı alan satır sonunu aşarsa satır sonu eklenmez (Python da eklemez).
fn csv_kayitlari(satirlar: &[String]) -> Vec<Vec<String>> {
    #[derive(PartialEq)]
    enum D {
        KayitBasi,
        AlanBasi,
        Alanda,
        Tirnakta,
        TirnakSonrasi,
    }
    let mut kayitlar: Vec<Vec<String>> = Vec::new();
    let mut alanlar: Vec<String> = Vec::new();
    let mut alan = String::new();
    let mut d = D::KayitBasi;
    for s in satirlar {
        for c in s.chars() {
            match d {
                D::KayitBasi | D::AlanBasi => match c {
                    '"' => d = D::Tirnakta,
                    ',' => {
                        alanlar.push(std::mem::take(&mut alan));
                        d = D::AlanBasi;
                    }
                    _ => {
                        alan.push(c);
                        d = D::Alanda;
                    }
                },
                D::Alanda => {
                    if c == ',' {
                        alanlar.push(std::mem::take(&mut alan));
                        d = D::AlanBasi;
                    } else {
                        alan.push(c);
                    }
                }
                D::Tirnakta => {
                    if c == '"' {
                        d = D::TirnakSonrasi;
                    } else {
                        alan.push(c);
                    }
                }
                D::TirnakSonrasi => match c {
                    '"' => {
                        alan.push('"');
                        d = D::Tirnakta;
                    }
                    ',' => {
                        alanlar.push(std::mem::take(&mut alan));
                        d = D::AlanBasi;
                    }
                    _ => {
                        alan.push(c);
                        d = D::Alanda;
                    }
                },
            }
        }
        // satır sonu işareti
        match d {
            D::Tirnakta => continue,
            D::KayitBasi => kayitlar.push(Vec::new()),
            _ => {
                alanlar.push(std::mem::take(&mut alan));
                kayitlar.push(std::mem::take(&mut alanlar));
            }
        }
        d = D::KayitBasi;
    }
    if d == D::Tirnakta {
        alanlar.push(alan);
        kayitlar.push(alanlar);
    }
    kayitlar
}

/// Python `csv.DictReader` (restkey=None, restval=None): boş kayıtlar atlanır, ilk kayıt başlıktır.
fn dict_okuyucu(kayitlar: Vec<Vec<String>>) -> Vec<Satir> {
    let mut it = kayitlar.into_iter();
    let Some(baslik) = it.next() else { return Vec::new() };
    let mut out = Vec::new();
    for k in it {
        if k.is_empty() {
            continue;
        }
        let mut d: Satir = HashMap::new();
        for (ad, v) in baslik.iter().zip(k.iter()) {
            d.insert(ad.clone(), Some(v.clone()));
        }
        for ad in baslik.iter().skip(k.len()) {
            d.insert(ad.clone(), None);
        }
        out.push(d);
    }
    out
}

fn al<'a>(r: &'a Satir, k: &str) -> Option<&'a str> {
    r.get(k).and_then(|v| v.as_deref())
}

/// Python `%s` ile `None` → "None".
fn pn(v: Option<&str>) -> String {
    v.map(String::from).unwrap_or_else(|| "None".into())
}

fn kuyruk_oku(repo: &str) -> Sn<(Vec<Satir>, String)> {
    let yol = Path::new(repo).join("veri").join("gorunum").join("v_bayat_aday.csv");
    if !yol.exists() {
        return Ok((Vec::new(), String::new()));
    }
    let raw = match py::oku_kati(&yol) {
        Ok(s) => s,
        Err(py::OkuHata::Io(e)) => return Err(format!("OSError: {e}")),
        Err(py::OkuHata::Kod) => return Err("UnicodeDecodeError: v_bayat_aday.csv".into()),
    };
    let mut satirlar: Vec<(i128, String, Satir)> = Vec::new();
    for r in dict_okuyucu(csv_kayitlari(&py::splitlines(&raw))) {
        let dosya = match al(&r, "dosya") {
            Some(d) if !d.is_empty() && !d.starts_with('#') => d.to_string(),
            _ => continue,
        };
        satirlar.push((0, dosya, r));
    }
    for s in satirlar.iter_mut() {
        let y = al(&s.2, "yas_gun").unwrap_or("");
        let n = if y.is_empty() { 0 } else { py::int(y).ok_or_else(|| format!("ValueError: invalid literal for int() with base 10: {}", py::repr(y)))? };
        s.0 = -n;
    }
    satirlar.sort_by(|a, b| (a.0, &a.1).cmp(&(b.0, &b.1)));
    Ok((satirlar.into_iter().map(|s| s.2).collect(), sha1_hex(raw.as_bytes())))
}

/// JSONL dosyasını Python gibi satır satır oku (bozuk satır atlanır; nesne olmayan değer → AttributeError).
fn jsonl_nesneleri(yol: &Path) -> Sn<Vec<Map<String, Value>>> {
    let metin = match py::oku_kati(yol) {
        Ok(s) => s,
        Err(py::OkuHata::Io(e)) => return Err(format!("OSError: {e}")),
        Err(py::OkuHata::Kod) => return Err(format!("UnicodeDecodeError: {}", yol.display())),
    };
    let mut out = Vec::new();
    for satir in metin.split('\n') {
        let Ok(v) = serde_json::from_str::<Value>(satir) else { continue };
        match v {
            Value::Object(m) => out.push(m),
            _ => return Err("AttributeError: JSON değeri nesne değil ('.get' yok)".into()),
        }
    }
    Ok(out)
}

/// anakronizm-denetim.jsonl son kosum_id'sinin D1 bulguları, dosya → [satır: kalıp].
fn son_d1_bulgular(repo: &str, dosyalar: &[String]) -> Sn<HashMap<String, Vec<String>>> {
    let mut out: HashMap<String, Vec<String>> = dosyalar.iter().map(|d| (d.clone(), Vec::new())).collect();
    let yol = Path::new(repo).join("veri").join("anakronizm-denetim.jsonl");
    if !yol.exists() {
        return Ok(out);
    }
    let kayitlar = jsonl_nesneleri(&yol)?;
    let mut son = Value::Null;
    for o in &kayitlar {
        if let Some(k) = o.get("kosum_id") {
            son = k.clone();
        }
    }
    for o in &kayitlar {
        if o.get("kosum_id").unwrap_or(&Value::Null) != &son || o.get("denetim").and_then(Value::as_str) != Some("D1") {
            continue;
        }
        let Some(d) = o.get("dosya").and_then(Value::as_str) else { continue };
        let Some(liste) = out.get_mut(d) else { continue };
        let g = |k: &str| o.get(k).map(py_str).unwrap_or_else(|| "None".into());
        liste.push(format!("{}: {} [{}]", g("satir"), g("kalip"), g("seviye")));
    }
    Ok(out)
}

fn bugun_olaylari(repo: &str, bugun: &str) -> Sn<i64> {
    let yol = Path::new(repo).join("veri").join("bronz").join("cekim-olay.jsonl");
    let mut n = 0;
    if yol.exists() {
        for o in jsonl_nesneleri(&yol)? {
            let ilk10 = match o.get("cekim_tarihi") {
                None | Some(Value::Null) => String::new(),
                Some(Value::String(s)) => s.chars().take(10).collect(),
                Some(v) if !jarvis_hook::ortak::py_truthy(v) => String::new(),
                Some(_) => return Err("TypeError: cekim_tarihi dize değil".into()),
            };
            if ilk10 == bugun {
                n += 1;
            }
        }
    }
    Ok(n)
}

fn ts_utc_mikro() -> String {
    chrono::Utc::now().format("%Y-%m-%dT%H:%M:%S%.6f+00:00").to_string()
}

fn ayrisan() -> Ayrisan {
    Ayrisan::yeni(
        "bayat-cekim.py",
        Some("D3 bayatlık kuyruğu boşaltma (İB-52)"),
        vec![
            Secenek::deger(&["--repo"], "repo", None),
            Secenek::bayrak(&["--liste"], "liste", None),
            Secenek::bayrak(&["--olcum"], "olcum", None),
            // metavar="DOSYA": argparse metavar'ı dest.upper() olduğundan dest doğrudan "DOSYA" seçildi
            Secenek::deger(&["--kaydet"], "DOSYA", None),
            Secenek::deger(&["--sonuc"], "sonuc", None).secimli(&["guncellendi", "sonlandi", "teyit"]),
            Secenek::deger(&["--kaynak-tarihi"], "kaynak_tarihi", None),
            Secenek::deger(&["--not"], "not_", None),
            Secenek::tam(&["--n"], "n", None),
            Secenek::deger(&["--bugun"], "bugun", None),
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
        Err(m) => py::coker(&m),
    }
}

fn calis(a: &crate::argparse::Sonuc) -> Sn<i32> {
    let cwd = std::env::current_dir().map(|d| d.to_string_lossy().into_owned()).unwrap_or_default();
    // Python varsayılanı betiğin üst-üst dizini; Rust ikilisinde betik yok → çalışma dizini (silver-saglik ile aynı kural).
    let repo = py::abspath(a.metin("repo").unwrap_or(&cwd));
    let bugun: String = match a.metin("bugun") {
        Some(b) if !b.is_empty() => iso_tarih(b).ok_or_else(|| format!("ValueError: Invalid isoformat string: {}", py::repr(b)))?.format("%Y-%m-%d").to_string(),
        _ => jarvis_hook::ortak::bugun_yerel(),
    };
    let head = {
        let h = py::sh(&["rev-parse", "--short", "HEAD"], Path::new(&repo));
        if h.is_empty() { "-".to_string() } else { h }
    };
    let ts = ts_istanbul();
    let kosum_id = format!("bayat-cekim:{head}:{bugun}");
    let (kuyruk, girdi_sha) = kuyruk_oku(&repo)?;
    let n: i64 = a.tam("n").unwrap_or(3).clamp(i64::MIN as i128, i64::MAX as i128) as i64;

    let kaydet = a.metin("DOSYA").unwrap_or("");
    if !kaydet.is_empty() {
        let Some(sonuc) = a.metin("sonuc") else {
            py::err("HATA: --kaydet için --sonuc zorunlu (teyit|guncellendi|sonlandi)\n");
            return Ok(2);
        };
        let rel = if py_isabs(kaydet) { py::relpath(&py::abspath(kaydet), &repo).map_err(|e| format!("ValueError: {e}"))? } else { kaydet.to_string() };
        if !Path::new(&py::join(&repo, &rel)).exists() {
            py::err(&format!("HATA: dosya yok: {rel}\n"));
            return Ok(2);
        }
        let kaynak = a.metin("kaynak_tarihi");
        if let Some(k) = kaynak
            && !k.is_empty()
            && iso_tarih(k).is_none()
        {
            py::err("HATA: --kaynak-tarihi YYYY-MM-DD olmalı\n");
            return Ok(2);
        }
        let mut olay = Map::new();
        olay.insert("ts".into(), Value::from(ts));
        olay.insert("kod_sha".into(), Value::from(head));
        olay.insert("kosum_id".into(), Value::from(kosum_id));
        olay.insert("dosya_id".into(), Value::from(rel.clone()));
        olay.insert("cekim_tarihi".into(), Value::from(bugun.clone()));
        olay.insert("kaynak_tarihi".into(), kaynak.map(Value::from).unwrap_or(Value::Null));
        olay.insert("sonuc".into(), Value::from(sonuc));
        olay.insert("not".into(), Value::from(a.metin("not_").unwrap_or("")));
        let yol = Path::new(&repo).join("veri").join("bronz").join("cekim-olay.jsonl");
        jarvis_hook::ortak::ekle_satir(&yol, &py_dumps(&Value::Object(olay))).map_err(|e| format!("OSError: {e}"))?;
        let k = match kaynak {
            Some(k) if !k.is_empty() => k,
            _ => "-",
        };
        py::print(&format!("cekim-olay: {rel} → {sonuc} (cekim {bugun}, kaynak {k}) · sonraki: katman-hatti (silver damga) + anakronizm-denetim (kuyruk)"));
        return Ok(0);
    }

    let hedef = py_dilim(&kuyruk, 0, n);
    let (liste, olcum) = (a.bayrak("liste"), a.bayrak("olcum"));
    if liste || !olcum {
        py::print(&format!("bayat-cekim · bugün {bugun} · HEAD {head} · D3 kuyruk {} dosya · hedef N={n} → {}", kuyruk.len(), hedef.len()));
        let adlar: Vec<String> = hedef.iter().map(|h| al(h, "dosya").unwrap_or("").to_string()).collect();
        let d1 = son_d1_bulgular(&repo, &adlar)?;
        for (h, ad) in hedef.iter().zip(&adlar) {
            py::print(&format!("  {ad}  (yaş {} gün, damga {})", pn(al(h, "yas_gun")), pn(al(h, "en_yeni_damga"))));
            let bulgular = &d1[ad];
            for b in bulgular.iter().take(8) {
                py::print(&format!("      D1 {b}"));
            }
            if bulgular.is_empty() {
                py::print("      D1 bulgusu yok (yalnız damga tazeleme adayı)");
            }
        }
        if hedef.is_empty() {
            py::print("  kuyruk boş — yeniden-çekim yok (0 aday; uydurma yok)");
        }
    }
    if olcum {
        let esik = if kuyruk.is_empty() { "90".to_string() } else { pn(al(&kuyruk[0], "esik_gun")) };
        let metrikler: [(&str, i64, String); 3] = [
            ("bayat_kuyruk_n", kuyruk.len() as i64, format!("D3 kuyruğu (eşik {esik} gün)")),
            ("cekim_hedef_n", hedef.len() as i64, format!("N={n} politikası (KB-68 a)")),
            ("cekim_bugun_n", bugun_olaylari(&repo, &bugun)?, "bugün yazılan cekim-olay satırı".to_string()),
        ];
        let mut satirlar = String::new();
        let mut ozet: Vec<String> = Vec::new();
        for (metrik, deger, nt) in metrikler {
            let sonuc = if metrik != "cekim_bugun_n" || deger >= (hedef.len() as i64).min(n) { "PASS" } else { "WARN" };
            let mut o = Map::new();
            o.insert("ts".into(), Value::from(ts_utc_mikro()));
            o.insert("kod_sha".into(), Value::from(head.clone()));
            o.insert("girdi_sha".into(), Value::from(if girdi_sha.is_empty() { "-" } else { girdi_sha.as_str() }));
            o.insert("kosum_id".into(), Value::from(kosum_id.clone()));
            o.insert("katman".into(), Value::from("bronz"));
            o.insert("nesne".into(), Value::from("v_bayat_aday.csv"));
            o.insert("metrik".into(), Value::from(metrik));
            o.insert("deger".into(), Value::from(deger as f64));
            o.insert("birim".into(), Value::from("adet"));
            o.insert("sonuc".into(), Value::from(sonuc));
            o.insert("not".into(), Value::from(nt));
            satirlar.push_str(&py_dumps(&Value::Object(o)));
            satirlar.push('\n');
            ozet.push(format!("{metrik}={deger} [{sonuc}]"));
        }
        let yol = Path::new(&repo).join("veri").join("katman-olcum.jsonl");
        let mut f = std::fs::OpenOptions::new().append(true).create(true).open(&yol).map_err(|e| format!("OSError: {e}"))?;
        f.write_all(satirlar.as_bytes()).map_err(|e| format!("OSError: {e}"))?;
        py::print(&format!("ölçüm: {} → veri/katman-olcum.jsonl", ozet.join(" · ")));
    }
    Ok(0)
}
