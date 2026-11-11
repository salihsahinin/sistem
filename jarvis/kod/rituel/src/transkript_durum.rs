//! Transkript artımlı okuma durumu (denetim kalem 42 B).
//!
//! Claude Code transkriptleri (`~/.claude/projects/<anahtar>/*.jsonl`) yalnız sona eklenerek büyür. Adım başına küçük bir
//! durum dosyası (`veri/transkript-durum-<adim>.json`) her dosya için boyut + mtime + okunan bayt konumunu tutar:
//! - boyut ve mtime aynı → dosya atlanır (okunmaz);
//! - boyut ≥ kayıtlı konum → yalnız konumdan sonrası okunur;
//! - boyut < kayıtlı konum (kesilmiş/yeniden yazılmış) → baştan okunur.
//!
//! Konum her zaman son tam satırın (`\n`) sonrasıdır; yarım son satır bir sonraki koşumda yeniden okunur.
//! Güvenlik şartı: önceki koşumda okunan her kayıt bronz kütüğe yazılmış olmalı. Bu yüzden durum yalnız bronz yazımından
//! sonra kaydedilir ve bronz kütüğün o anki boyutu da saklanır; kütük dışarıdan değişmişse (boyut farklı) durum yok sayılır,
//! tam okuma yapılır. Ayrıca proje dizini ya da sürüm farklıysa durum yok sayılır.
use serde_json::{Map, Value, json};
use std::collections::BTreeMap;
use std::io::{Read, Seek, SeekFrom};
use std::path::Path;

const SURUM: i64 = 1;

#[derive(Clone, Copy, PartialEq, Eq)]
struct Girdi {
    boyut: u64,
    mtime_ns: i128,
    konum: u64,
}

pub struct Durum {
    proje_dizin: String,
    eski: BTreeMap<String, Girdi>,
    yeni: BTreeMap<String, Girdi>,
    /// Atlanan dosya sayısı (yalnız bilgi).
    pub atlanan: usize,
}

fn mtime_ns(md: &std::fs::Metadata) -> i128 {
    md.modified()
        .ok()
        .and_then(|t| t.duration_since(std::time::UNIX_EPOCH).ok())
        .map(|d| d.as_nanos() as i128)
        .unwrap_or(-1)
}

fn dosya_boyut(yol: &str) -> Option<u64> {
    std::fs::metadata(yol).ok().map(|m| m.len())
}

/// Durum dosyasının yolu: `<repo>/veri/transkript-durum-<adim>.json`.
pub fn yol(repo: &str, adim: &str) -> String {
    crate::py::join(&crate::py::join(repo, "veri"), &format!("transkript-durum-{adim}.json"))
}

impl Durum {
    /// Durumu yükler; `tam` verilirse, dosya yoksa ya da geçersizse boş durumla (tam okuma) başlar.
    pub fn yukle(durum_yol: &str, proje_dizin: &str, bronz_yol: &str, tam: bool) -> Durum {
        let mut d = Durum { proje_dizin: proje_dizin.to_string(), eski: BTreeMap::new(), yeni: BTreeMap::new(), atlanan: 0 };
        if tam {
            return d;
        }
        let Ok(metin) = std::fs::read_to_string(durum_yol) else { return d };
        let Ok(Value::Object(o)) = serde_json::from_str::<Value>(&metin) else { return d };
        let gecerli = o.get("surum").and_then(Value::as_i64) == Some(SURUM)
            && o.get("proje_dizin").and_then(Value::as_str) == Some(proje_dizin)
            && o.get("bronz_boyut").and_then(Value::as_u64).is_some_and(|b| Some(b) == dosya_boyut(bronz_yol));
        if !gecerli {
            return d;
        }
        if let Some(Value::Object(ds)) = o.get("dosyalar") {
            for (ad, g) in ds {
                let (Some(boyut), Some(mt), Some(konum)) = (
                    g.get("boyut").and_then(Value::as_u64),
                    g.get("mtime_ns").and_then(Value::as_str).and_then(|s| s.parse::<i128>().ok()),
                    g.get("konum").and_then(Value::as_u64),
                ) else {
                    continue;
                };
                d.eski.insert(ad.clone(), Girdi { boyut, mtime_ns: mt, konum });
            }
        }
        d
    }

    /// `ad` (proje dizinindeki dosya adı) için okunacak baytlar: `None` → değişmemiş, atla.
    /// Dönen baytlar ya dosyanın tamamı ya da kayıtlı konumdan sonrasıdır.
    pub fn oku(&mut self, ad: &str, yol: &str) -> std::io::Result<Option<Vec<u8>>> {
        let md = std::fs::metadata(yol)?;
        let (boyut, mt) = (md.len(), mtime_ns(&md));
        let onceki = self.eski.get(ad).copied();
        if let Some(g) = onceki
            && g.boyut == boyut
            && g.mtime_ns == mt
        {
            self.yeni.insert(ad.to_string(), g);
            self.atlanan += 1;
            return Ok(None);
        }
        let bas = match onceki {
            Some(g) if boyut >= g.konum => g.konum,
            _ => 0,
        };
        let mut f = std::fs::File::open(yol)?;
        f.seek(SeekFrom::Start(bas))?;
        let mut bayt = Vec::new();
        f.read_to_end(&mut bayt)?;
        // Konum son tam satırın sonuna ilerler; yarım satır bir dahaki koşumda yeniden okunur.
        let konum = match bayt.iter().rposition(|&b| b == b'\n') {
            Some(i) => bas + i as u64 + 1,
            None => bas,
        };
        let okunan_boyut = bas + bayt.len() as u64;
        self.yeni.insert(ad.to_string(), Girdi { boyut: okunan_boyut, mtime_ns: if okunan_boyut == boyut { mt } else { -1 }, konum });
        Ok(Some(bayt))
    }

    /// Durumu yazar; bronz kütüğün güncel boyutu ile birlikte. Yalnız bronz yazımı başarılıysa çağrılır.
    pub fn kaydet(&self, durum_yol: &str, bronz_yol: &str) -> Result<(), String> {
        let mut ds = Map::new();
        for (ad, g) in &self.yeni {
            ds.insert(ad.clone(), json!({"boyut": g.boyut, "mtime_ns": g.mtime_ns.to_string(), "konum": g.konum}));
        }
        let o = json!({
            "surum": SURUM,
            "not": "transkript artımlı okuma durumu (denetim kalem 42 B); silinirse ya da --tam verilirse tam okuma yapılır",
            "proje_dizin": self.proje_dizin,
            "bronz_boyut": dosya_boyut(bronz_yol).unwrap_or(0),
            "dosyalar": Value::Object(ds),
        });
        if let Some(ust) = Path::new(durum_yol).parent() {
            std::fs::create_dir_all(ust).map_err(|e| format!("{durum_yol}: {e}"))?;
        }
        let gecici = format!("{durum_yol}.gecici");
        std::fs::write(&gecici, format!("{}\n", serde_json::to_string_pretty(&o).unwrap_or_default())).map_err(|e| format!("{gecici}: {e}"))?;
        std::fs::rename(&gecici, durum_yol).map_err(|e| format!("{durum_yol}: {e}"))
    }
}
