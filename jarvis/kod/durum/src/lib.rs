//! Ortak durum tablosu + akış grafı: ekle-yalnız olay kütüğü, katlanmış güncel durum ve seans kayıtları.
//!
//! Doğruluk kaynağı `ortak/durum-olay.jsonl` (satır = bir olay). Durum bellek içinde olayların sırayla
//! uygulanmasıyla hesaplanır; geçersiz geçiş hatadır. `son_gecerlilik` (YYYY-MM-DD) bugünden küçükse
//! kayıt okuma anında `bayat` sayılır (kütüğe yazılmaz).
//!
//! Karar 122 (2026-10-25): kütük aynı zamanda **akış grafının** kaynağıdır. Düğüm = iş kaydı (`#id`), hedef
//! kaydı (`tur: hedef`) ya da seans (`seans_ac`/`seans_kapat` olayları); kenar = `girdi` (bağımlılık),
//! `hedef` (iş → hedef), seans → dokunduğu iş, seans → sonraki seans (aynı alan, zaman sırası).
//! Graf türetilmiş görünümdür (`graf_modeli`, `d2`); kütük elle düzenlenmez.

use serde::{Deserialize, Serialize};
use std::collections::{BTreeMap, BTreeSet};

pub const ALANLAR: [&str; 9] = ["jarvis", "friday", "tart", "gard", "span", "calc", "deci", "vega", "sage"];
/// Oturum-başı brifinin bayt tavanı (Karar 113 M2 1 KB idi; Karar 122 ile konum + sıradaki + graf satırları eklendi).
pub const OTURUM_BASI_BAYT: usize = 2048;
pub const GRAF_SEMA: &str = "akis-graf v1 (Karar 122)";
pub const TESLIM_SEMA: &str = "seans-teslim v1 (Karar 121/122)";

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "lowercase")]
pub enum Durum {
    Acik,
    Islemde,
    Tamam,
    Tuketildi,
    Bayat,
}

impl Durum {
    pub fn ad(self) -> &'static str {
        match self {
            Durum::Acik => "acik",
            Durum::Islemde => "islemde",
            Durum::Tamam => "tamam",
            Durum::Tuketildi => "tuketildi",
            Durum::Bayat => "bayat",
        }
    }
    pub fn coz(s: &str) -> Option<Durum> {
        Some(match s {
            "acik" => Durum::Acik,
            "islemde" => Durum::Islemde,
            "tamam" => Durum::Tamam,
            "tuketildi" => Durum::Tuketildi,
            "bayat" => Durum::Bayat,
            _ => return None,
        })
    }
    /// Bir girdi bu durumdaysa bağımlı işi **bloklamaz** (tamam, tüketildi ya da bayat/terk).
    pub fn blok_acar(self) -> bool {
        !matches!(self, Durum::Acik | Durum::Islemde)
    }
}

/// Kayıt türü: iş (varsayılan) ya da hedef (işlerin hizmet ettiği üst düğüm; bitirilmez, altındaki işler bitince kapanır).
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize, Default)]
#[serde(rename_all = "lowercase")]
pub enum Tur {
    #[default]
    Is,
    Hedef,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum OlayTuru {
    Ac,
    Al,
    Bitir,
    Tuket,
    Bayatla,
    SeansAc,
    SeansKapat,
}

fn sifir(v: &u64) -> bool {
    *v == 0
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct Olay {
    pub olay: OlayTuru,
    /// İş/hedef kayıt kimliği; seans olaylarında 0 (yazılmaz).
    #[serde(default, skip_serializing_if = "sifir")]
    pub id: u64,
    pub ts: String,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub alan: Option<String>,
    #[serde(default, rename = "is", skip_serializing_if = "Option::is_none")]
    pub is_ad: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub sonraki_eylem: Option<String>,
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    pub kanit: Vec<String>,
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    pub girdi: Vec<u64>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub son_gecerlilik: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub oturum: Option<String>,
    // --- Karar 122 alanları ---
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub tur: Option<Tur>,
    /// İşin hizmet ettiği hedef kaydı (`ac` olayında).
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub hedef: Option<u64>,
    /// Seansın tek cümlelik hedefi (`seans_ac`) ya da yoklama sonucu (`seans_kapat`: hedef_tutuldu).
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub hedef_cumle: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub hedef_tutuldu: Option<bool>,
    /// Seans kapanış kaydının yolu (repo köküne göre) ve etiketi (`seans_kapat`).
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub kayit: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub etiket: Option<String>,
}

impl Olay {
    pub fn yalin(olay: OlayTuru, id: u64, ts: &str) -> Olay {
        Olay {
            olay,
            id,
            ts: ts.to_string(),
            alan: None,
            is_ad: None,
            sonraki_eylem: None,
            kanit: vec![],
            girdi: vec![],
            son_gecerlilik: None,
            oturum: None,
            tur: None,
            hedef: None,
            hedef_cumle: None,
            hedef_tutuldu: None,
            kayit: None,
            etiket: None,
        }
    }
    pub fn seans(olay: OlayTuru, oturum: &str, alan: &str, ts: &str) -> Olay {
        let mut o = Olay::yalin(olay, 0, ts);
        o.oturum = Some(oturum.to_string());
        o.alan = Some(alan.to_string());
        o
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize)]
pub struct Kayit {
    pub id: u64,
    pub alan: String,
    pub durum: Durum,
    #[serde(rename = "is")]
    pub is_ad: String,
    pub sonraki_eylem: String,
    pub kanit: Vec<String>,
    pub girdi: Vec<u64>,
    pub son_gecerlilik: Option<String>,
    pub ts: String,
    pub oturum: Option<String>,
    #[serde(default)]
    pub tur: Tur,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub hedef: Option<u64>,
    /// Zaman çizgisi: açılış · alınış · bitiş damgaları.
    pub acilis_ts: String,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub al_ts: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub bitir_ts: Option<String>,
    /// Kayda dokunan seanslar (olay sırasıyla, tekrarsız).
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    pub oturumlar: Vec<String>,
}

impl Kayit {
    /// Bugünün tarihine (YYYY-MM-DD...) göre geçerli durum: süresi geçen, tüketilmemiş kayıt `bayat` sayılır.
    pub fn efektif(&self, bugun: &str) -> Durum {
        match (&self.son_gecerlilik, self.durum) {
            (Some(s), d) if d != Durum::Tuketildi && d != Durum::Bayat && s.as_str() < tarih_kismi(bugun) => Durum::Bayat,
            (_, d) => d,
        }
    }
}

/// Seans düğümü: bir sohbetin kütükteki izi. Açılış olayı olmayan eski oturumlar (`oturum` alanı taşıyan olaylardan)
/// örtük seans olarak kurulur (`ortuk = true`).
#[derive(Debug, Clone, PartialEq, Eq, Serialize)]
pub struct Seans {
    pub oturum: String,
    pub alan: String,
    pub ac_ts: String,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub kapat_ts: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub hedef: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub hedef_tutuldu: Option<bool>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub kayit: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub etiket: Option<String>,
    /// Bu seansta açılan / alınan / bitirilen kayıtlar (olay sırası, tekrarsız).
    pub acilan: Vec<u64>,
    pub alinan: Vec<u64>,
    pub bitirilen: Vec<u64>,
    pub ortuk: bool,
}

impl Seans {
    pub fn dokunulan(&self) -> Vec<u64> {
        let mut v: Vec<u64> = self.acilan.iter().chain(&self.alinan).chain(&self.bitirilen).copied().collect();
        v.sort_unstable();
        v.dedup();
        v
    }
    /// Açık seans = `seans_ac` ile açılmış ve henüz kapanmamış; örtük (eski kütük) seanslar hiç açık sayılmaz.
    pub fn acik(&self) -> bool {
        self.kapat_ts.is_none() && !self.ortuk
    }
}

#[derive(Debug, PartialEq, Eq)]
pub enum Hata {
    /// Geçersiz geçiş, bulunamadı, bozuk kütük (çıkış 1).
    Gecersiz(String),
    /// Kullanım hatası (çıkış 2).
    Kullanim(String),
}

impl Hata {
    pub fn kod(&self) -> i32 {
        match self {
            Hata::Gecersiz(_) => 1,
            Hata::Kullanim(_) => 2,
        }
    }
    pub fn mesaj(&self) -> &str {
        match self {
            Hata::Gecersiz(m) | Hata::Kullanim(m) => m,
        }
    }
}

fn gecersiz<T>(m: String) -> Result<T, Hata> {
    Err(Hata::Gecersiz(m))
}

pub fn tarih_kismi(ts: &str) -> &str {
    ts.get(..10).unwrap_or(ts)
}

/// Katlanmış defter: kayıtlar id sırasıyla, seanslar oturum adıyla.
#[derive(Debug, Default, Clone)]
pub struct Defter {
    pub kayitlar: BTreeMap<u64, Kayit>,
    pub seanslar: BTreeMap<String, Seans>,
}

impl Defter {
    pub fn sonraki_id(&self) -> u64 {
        self.kayitlar.keys().next_back().map_or(1, |m| m + 1)
    }

    /// Olayları sırayla uygular (yeniden oynatma; son_gecerlilik denetimi yok).
    pub fn katla(olaylar: &[Olay]) -> Result<Defter, Hata> {
        let mut d = Defter::default();
        for o in olaylar {
            d.uygula(o, "0000-00-00")?;
        }
        Ok(d)
    }

    /// Olayın `oturum` alanı varsa seans düğümünü (gerekirse örtük) bulur ve dokunuşu işler.
    fn seans_dokun(&mut self, o: &Olay, alan: &str) {
        let Some(ad) = &o.oturum else { return };
        let s = self.seanslar.entry(ad.clone()).or_insert_with(|| Seans {
            oturum: ad.clone(),
            alan: alan.to_string(),
            ac_ts: o.ts.clone(),
            kapat_ts: None,
            hedef: None,
            hedef_tutuldu: None,
            kayit: None,
            etiket: None,
            acilan: vec![],
            alinan: vec![],
            bitirilen: vec![],
            ortuk: true,
        });
        let liste = match o.olay {
            OlayTuru::Ac => &mut s.acilan,
            OlayTuru::Al => &mut s.alinan,
            OlayTuru::Bitir => &mut s.bitirilen,
            _ => return,
        };
        if !liste.contains(&o.id) {
            liste.push(o.id);
        }
    }

    /// Tek olayı doğrular ve uygular. `bugun`: süresi geçmiş kayıtta al/bitir/tuket reddi için.
    pub fn uygula(&mut self, o: &Olay, bugun: &str) -> Result<(), Hata> {
        match o.olay {
            OlayTuru::SeansAc => {
                let (Some(ad), Some(alan)) = (o.oturum.clone(), o.alan.clone()) else {
                    return gecersiz("seans_ac: oturum ve alan zorunlu".into());
                };
                if !ALANLAR.contains(&alan.as_str()) {
                    return gecersiz(format!("bilinmeyen alan: {alan}"));
                }
                if self.seanslar.get(&ad).is_some_and(|s| !s.ortuk) {
                    return gecersiz(format!("seans {ad} zaten açılmış"));
                }
                let s = self.seanslar.entry(ad.clone()).or_insert_with(|| Seans {
                    oturum: ad.clone(),
                    alan: alan.clone(),
                    ac_ts: o.ts.clone(),
                    kapat_ts: None,
                    hedef: None,
                    hedef_tutuldu: None,
                    kayit: None,
                    etiket: None,
                    acilan: vec![],
                    alinan: vec![],
                    bitirilen: vec![],
                    ortuk: true,
                });
                s.ortuk = false;
                s.alan = alan;
                s.ac_ts = o.ts.clone();
                s.hedef = o.hedef_cumle.clone();
                return Ok(());
            }
            OlayTuru::SeansKapat => {
                let Some(ad) = o.oturum.clone() else {
                    return gecersiz("seans_kapat: oturum zorunlu".into());
                };
                let s = self.seanslar.get_mut(&ad).ok_or_else(|| Hata::Gecersiz(format!("seans {ad} açılmamış")))?;
                if s.kapat_ts.is_some() {
                    return gecersiz(format!("seans {ad} zaten kapanmış"));
                }
                s.kapat_ts = Some(o.ts.clone());
                s.hedef_tutuldu = o.hedef_tutuldu;
                if o.hedef_cumle.is_some() {
                    s.hedef = o.hedef_cumle.clone();
                }
                s.kayit = o.kayit.clone();
                s.etiket = o.etiket.clone();
                return Ok(());
            }
            _ => {}
        }
        if o.olay == OlayTuru::Ac {
            let alan = o.alan.clone().ok_or_else(|| Hata::Gecersiz(format!("ac #{}: alan yok", o.id)))?;
            if !ALANLAR.contains(&alan.as_str()) {
                return gecersiz(format!("bilinmeyen alan: {alan}"));
            }
            // Karar 123 (durum #27): id tekdüze artar ama boşluk serbesttir — worktree kopyaları arasında çakışmasın diye
            // CLI, diğer worktree kütüklerinin en büyük id'sini de aşan bir id seçer.
            if o.id == 0 || o.id < self.sonraki_id() {
                return gecersiz(format!("ac: id {} en az {} olmalı", o.id, self.sonraki_id()));
            }
            for g in &o.girdi {
                if !self.kayitlar.contains_key(g) {
                    return gecersiz(format!("girdi #{g} bulunamadı"));
                }
            }
            if let Some(h) = o.hedef {
                match self.kayitlar.get(&h) {
                    None => return gecersiz(format!("hedef #{h} bulunamadı")),
                    Some(k) if k.tur != Tur::Hedef => return gecersiz(format!("#{h} hedef türünde değil")),
                    _ => {}
                }
            }
            let is_ad = o.is_ad.clone().filter(|s| !s.is_empty());
            let sonraki = o.sonraki_eylem.clone().filter(|s| !s.is_empty());
            let (Some(is_ad), Some(sonraki_eylem)) = (is_ad, sonraki) else {
                return gecersiz(format!("ac #{}: is ve sonraki_eylem zorunlu", o.id));
            };
            self.kayitlar.insert(
                o.id,
                Kayit {
                    id: o.id,
                    alan: alan.clone(),
                    durum: Durum::Acik,
                    is_ad,
                    sonraki_eylem,
                    kanit: o.kanit.clone(),
                    girdi: o.girdi.clone(),
                    son_gecerlilik: o.son_gecerlilik.clone(),
                    ts: o.ts.clone(),
                    oturum: o.oturum.clone(),
                    tur: o.tur.unwrap_or_default(),
                    hedef: o.hedef,
                    acilis_ts: o.ts.clone(),
                    al_ts: None,
                    bitir_ts: None,
                    oturumlar: o.oturum.iter().cloned().collect(),
                },
            );
            self.seans_dokun(o, &alan);
            return Ok(());
        }
        let k = self.kayitlar.get_mut(&o.id).ok_or_else(|| Hata::Gecersiz(format!("#{} bulunamadı", o.id)))?;
        let efektif = k.efektif(bugun);
        let hedef = match o.olay {
            OlayTuru::Al => {
                if efektif != Durum::Acik {
                    return gecersiz(format!("#{} al: durum {} (acik beklenir)", o.id, efektif.ad()));
                }
                k.al_ts = Some(o.ts.clone());
                Durum::Islemde
            }
            OlayTuru::Bitir => {
                if efektif != Durum::Islemde {
                    return gecersiz(format!("#{} bitir: durum {} (islemde beklenir)", o.id, efektif.ad()));
                }
                k.bitir_ts = Some(o.ts.clone());
                Durum::Tamam
            }
            OlayTuru::Tuket => {
                if efektif != Durum::Tamam {
                    return gecersiz(format!("#{} tuket: durum {} (tamam beklenir)", o.id, efektif.ad()));
                }
                Durum::Tuketildi
            }
            OlayTuru::Bayatla => {
                if k.durum == Durum::Bayat {
                    return gecersiz(format!("#{} zaten bayat", o.id));
                }
                Durum::Bayat
            }
            OlayTuru::Ac | OlayTuru::SeansAc | OlayTuru::SeansKapat => unreachable!(),
        };
        k.durum = hedef;
        k.ts = o.ts.clone();
        k.kanit.extend(o.kanit.iter().cloned());
        if let Some(ot) = &o.oturum {
            k.oturum = Some(ot.clone());
            if !k.oturumlar.contains(ot) {
                k.oturumlar.push(ot.clone());
            }
        }
        let alan = k.alan.clone();
        self.seans_dokun(o, &alan);
        Ok(())
    }

    pub fn listele(&self, alan: Option<&str>, durum: Option<Durum>, bugun: &str) -> Vec<(&Kayit, Durum)> {
        self.kayitlar
            .values()
            .map(|k| (k, k.efektif(bugun)))
            .filter(|(k, e)| alan.is_none_or(|a| k.alan == a) && durum.is_none_or(|d| *e == d))
            .collect()
    }

    /// Bir kaydın girdilerinden hâlâ açık/işlemde olanlar (bloklayanlar).
    pub fn bloklayanlar(&self, k: &Kayit, bugun: &str) -> Vec<u64> {
        k.girdi.iter().copied().filter(|g| self.kayitlar.get(g).is_some_and(|x| !x.efektif(bugun).blok_acar())).collect()
    }

    /// Sıradaki işler (graf ucu): açık ∧ iş türünde ∧ hiçbir girdisi bloklamıyor. İd sırası.
    pub fn sirada(&self, alan: &str, bugun: &str) -> Vec<&Kayit> {
        self.listele(Some(alan), Some(Durum::Acik), bugun)
            .into_iter()
            .map(|(k, _)| k)
            .filter(|k| k.tur == Tur::Is && self.bloklayanlar(k, bugun).is_empty())
            .collect()
    }

    /// Alanın seansları zaman sırasıyla (açılış damgası, sonra ad).
    pub fn alan_seanslari(&self, alan: &str) -> Vec<&Seans> {
        let mut v: Vec<&Seans> = self.seanslar.values().filter(|s| s.alan == alan).collect();
        v.sort_by(|a, b| a.ac_ts.cmp(&b.ac_ts).then(a.oturum.cmp(&b.oturum)));
        v
    }

    /// Alanın konumu: açık seans varsa o, yoksa son kapanan seans.
    pub fn konum(&self, alan: &str) -> Option<&Seans> {
        let v = self.alan_seanslari(alan);
        v.iter().rev().find(|s| s.acik()).or(v.last()).copied()
    }

    /// Bağlama konacak kısa metin (≤ `OTURUM_BASI_BAYT`): konum (seans) · açık/işlemde kayıtlar · sıradakiler ·
    /// bloklu bekleyenler · graf pointer'ı. Karar 113 M2 biçimi + Karar 122 graf satırları.
    pub fn oturum_basi(&self, alan: &str, bugun: &str) -> String {
        let tarih = tarih_kismi(bugun);
        let mut cikti = String::new();
        if let Some(s) = self.konum(alan) {
            let hal = match (&s.kapat_ts, s.ortuk) {
                (Some(t), _) => format!("kapandı {}", tarih_kismi(t)),
                (None, true) => format!("örtük, son olay {}", tarih_kismi(&s.ac_ts)),
                (None, false) => "AÇIK".to_string(),
            };
            cikti.push_str(&format!("KONUM {alan}: seans {} ({hal}", s.oturum));
            if let Some(h) = &s.hedef {
                cikti.push_str(&format!("; hedef: {h}"));
            }
            if let Some(t) = s.hedef_tutuldu {
                cikti.push_str(if t { "; tutuldu" } else { "; TUTMADI" });
            }
            cikti.push_str(")\n");
        }
        let acik: Vec<&Kayit> = self
            .listele(Some(alan), None, bugun)
            .into_iter()
            .filter(|(_, e)| *e == Durum::Acik || *e == Durum::Islemde)
            .map(|(k, _)| k)
            .collect();
        if acik.is_empty() {
            cikti.push_str(&format!("DURUM {alan} ({tarih}): açık iş yok\n"));
            cikti.push_str("GRAF: ortak/akis-graf.json · durum graf --alan ");
            cikti.push_str(alan);
            cikti.push('\n');
            return cikti;
        }
        let sirada: BTreeSet<u64> = self.sirada(alan, bugun).iter().map(|k| k.id).collect();
        let mut satirlar: Vec<String> = vec![];
        for k in &acik {
            let e = k.efektif(bugun);
            let isaret = if k.tur == Tur::Hedef {
                "HEDEF".to_string()
            } else if sirada.contains(&k.id) {
                "SIRADA".to_string()
            } else if e == Durum::Islemde {
                "islemde".to_string()
            } else {
                let b = self.bloklayanlar(k, bugun);
                format!("bekler<-{}", b.iter().map(|x| format!("#{x}")).collect::<Vec<_>>().join(","))
            };
            satirlar.push(format!("#{} {isaret} {} -> {}", k.id, k.is_ad, k.sonraki_eylem));
        }
        let toplam = satirlar.len();
        cikti.push_str(&format!("DURUM {alan} ({tarih}): {toplam} açık/işlemde · sırada {}\n", sirada.len()));
        let kuyruk = format!("GRAF: ortak/akis-graf.json · d2 ortak/graf/akis-{alan}.d2\n");
        let mut yazilan = 0;
        for s in &satirlar {
            let ek = if yazilan + 1 < toplam { 32 } else { 0 };
            if cikti.len() + s.len() + 1 + ek + kuyruk.len() > OTURUM_BASI_BAYT {
                break;
            }
            cikti.push_str(s);
            cikti.push('\n');
            yazilan += 1;
        }
        if yazilan < toplam {
            cikti.push_str(&format!("... +{} daha\n", toplam - yazilan));
        }
        cikti.push_str(&kuyruk);
        cikti
    }

    // ---------------- Akış grafı (Karar 122) ----------------

    /// Graf modeli: düğüm + kenar listesi, deterministik sıra (alan → id; seanslar zaman sırası). `alan` verilirse yalnız o alan.
    pub fn graf_modeli(&self, alan: Option<&str>, bugun: &str) -> serde_json::Value {
        use serde_json::{Value, json};
        let mut dugumler: Vec<Value> = vec![];
        let mut kenarlar: Vec<Value> = vec![];
        let alanlar: Vec<&str> = ALANLAR.iter().copied().filter(|a| alan.is_none_or(|x| x == *a)).collect();
        for a in &alanlar {
            let seanslar = self.alan_seanslari(a);
            for (i, s) in seanslar.iter().enumerate() {
                dugumler.push(json!({
                    "id": format!("seans:{}", s.oturum), "tur": "seans", "alan": a, "etiket": s.oturum,
                    "ac_ts": s.ac_ts, "kapat_ts": s.kapat_ts, "hedef": s.hedef, "hedef_tutuldu": s.hedef_tutuldu,
                    "kayit": s.kayit, "ortuk": s.ortuk, "dokunulan": s.dokunulan(),
                }));
                if i + 1 < seanslar.len() {
                    kenarlar.push(json!({"k": format!("seans:{}", s.oturum), "h": format!("seans:{}", seanslar[i + 1].oturum), "tur": "sonra"}));
                }
                for id in &s.acilan {
                    kenarlar.push(json!({"k": format!("seans:{}", s.oturum), "h": format!("is:{id}"), "tur": "acti"}));
                }
                for id in &s.bitirilen {
                    kenarlar.push(json!({"k": format!("seans:{}", s.oturum), "h": format!("is:{id}"), "tur": "bitirdi"}));
                }
                for id in s.alinan.iter().filter(|x| !s.bitirilen.contains(x)) {
                    kenarlar.push(json!({"k": format!("seans:{}", s.oturum), "h": format!("is:{id}"), "tur": "aldi"}));
                }
            }
            for (k, e) in self.listele(Some(a), None, bugun) {
                dugumler.push(json!({
                    "id": format!("is:{}", k.id), "tur": if k.tur == Tur::Hedef { "hedef" } else { "is" }, "alan": a,
                    "durum": e.ad(), "etiket": k.is_ad, "sonraki_eylem": k.sonraki_eylem,
                    "acilis_ts": k.acilis_ts, "al_ts": k.al_ts, "bitir_ts": k.bitir_ts, "oturumlar": k.oturumlar,
                    "sirada": k.tur == Tur::Is && e == Durum::Acik && self.bloklayanlar(k, bugun).is_empty(),
                }));
                for g in &k.girdi {
                    kenarlar.push(json!({"k": format!("is:{g}"), "h": format!("is:{}", k.id), "tur": "girdi"}));
                }
                if let Some(h) = k.hedef {
                    kenarlar.push(json!({"k": format!("is:{}", k.id), "h": format!("is:{h}"), "tur": "hizmet"}));
                }
            }
        }
        json!({
            "meta": {"sema": GRAF_SEMA, "uretici": "durum graf", "tarih": tarih_kismi(bugun), "alan": alan,
                     "dugum_sayisi": dugumler.len(), "kenar_sayisi": kenarlar.len(),
                     "not": "türetilmiş görünüm; kaynak ortak/durum-olay.jsonl; gövde deterministik"},
            "dugumler": dugumler, "kenarlar": kenarlar,
        })
    }

    /// LLM'e verilen kenar-listesi metni (graf dili): her satır bir düğüm ya da kenar; D2 kaynağı LLM'e verilmez.
    pub fn graf_metni(&self, alan: &str, bugun: &str) -> String {
        let mut s = format!("# akış grafı {alan} ({}) — düğüm: tür id durum etiket · kenar: k -tür-> h\n", tarih_kismi(bugun));
        for se in self.alan_seanslari(alan) {
            let hal = se.kapat_ts.as_deref().map_or(if se.ortuk { "örtük" } else { "AÇIK" }.to_string(), |t| tarih_kismi(t).to_string());
            s.push_str(&format!("seans {} {} hedef=\"{}\" dokunulan={:?}\n", se.oturum, hal, se.hedef.as_deref().unwrap_or("-"), se.dokunulan()));
        }
        for (k, e) in self.listele(Some(alan), None, bugun) {
            let tur = if k.tur == Tur::Hedef { "hedef" } else { "is" };
            s.push_str(&format!("{tur} #{} {} \"{}\" -> \"{}\"\n", k.id, e.ad(), k.is_ad, k.sonraki_eylem));
        }
        for (k, _) in self.listele(Some(alan), None, bugun) {
            for g in &k.girdi {
                s.push_str(&format!("#{g} -girdi-> #{}\n", k.id));
            }
            if let Some(h) = k.hedef {
                s.push_str(&format!("#{} -hizmet-> #{h}\n", k.id));
            }
        }
        s
    }

    /// Salih için D2 kaynağı (render: `d2 --layout=elk x.d2 x.svg`). Alan verilmezse tüm alanlar birer küme.
    pub fn d2(&self, alan: Option<&str>, bugun: &str) -> String {
        let alanlar: Vec<&str> = ALANLAR.iter().copied().filter(|a| alan.is_none_or(|x| x == *a)).collect();
        let mut s = String::new();
        s.push_str(&format!(
            "# akış grafı · üretici: durum graf · tarih {} · kaynak ortak/durum-olay.jsonl · render: d2 --layout=elk <bu dosya> <çıktı.svg>\n",
            tarih_kismi(bugun)
        ));
        s.push_str("direction: right\n");
        s.push_str("classes: {\n");
        s.push_str("  acik: {style.fill: \"#fff3bf\"; style.stroke: \"#f08c00\"}\n");
        s.push_str("  islemde: {style.fill: \"#ffd8a8\"; style.stroke: \"#e8590c\"; style.bold: true}\n");
        s.push_str("  tamam: {style.fill: \"#d3f9d8\"; style.stroke: \"#2f9e44\"}\n");
        s.push_str("  tuketildi: {style.fill: \"#e9ecef\"; style.stroke: \"#868e96\"}\n");
        s.push_str("  bayat: {style.fill: \"#f8f9fa\"; style.stroke: \"#adb5bd\"; style.stroke-dash: 3}\n");
        s.push_str("  hedef: {shape: hexagon; style.fill: \"#e7f5ff\"; style.stroke: \"#1971c2\"}\n");
        s.push_str("  seans: {shape: page; style.fill: \"#f3f0ff\"; style.stroke: \"#7048e8\"}\n");
        s.push_str("  seans_acik: {shape: page; style.fill: \"#f3f0ff\"; style.stroke: \"#7048e8\"; style.stroke-width: 3}\n");
        s.push_str("  sirada: {style.stroke-width: 3; style.stroke: \"#e03131\"}\n");
        s.push_str("}\n");
        let mut capraz: Vec<String> = vec![];
        s.push_str("aciklama: |md\n  Kutu = iş · altıgen = hedef · sayfa = seans (sohbet) · kırmızı kalın çerçeve = sırada (girdileri tamam)\\\n  Renk: sarı açık · turuncu işlemde · yeşil tamam · gri tüketildi · soluk bayat\\\n  Ok: girdi (bağımlılık) · hizmet (iş→hedef) · açtı/bitirdi (seans→iş) · sonra (seans→seans)\n|\n");
        for a in alanlar {
            let seanslar = self.alan_seanslari(a);
            if seanslar.is_empty() && !self.kayitlar.values().any(|k| k.alan == a) {
                continue;
            }
            s.push_str(&format!("{a}: {{\n  label: \"{a}\"\n"));
            for se in &seanslar {
                let anahtar = d2_anahtar(&format!("seans_{}", se.oturum));
                let hal = se.kapat_ts.as_deref().map_or(
                    if se.ortuk { format!("örtük · {}", tarih_kismi(&se.ac_ts)) } else { "AÇIK".to_string() },
                    |t| tarih_kismi(t).to_string(),
                );
                let mut etiket = format!("seans {}\\n{}", se.oturum, hal);
                if let Some(h) = &se.hedef {
                    etiket.push_str(&format!("\\nhedef: {}", kisalt(h, 60)));
                }
                if let Some(t) = se.hedef_tutuldu {
                    etiket.push_str(if t { " ✓" } else { " ✗" });
                }
                let sinif = if se.acik() { "seans_acik" } else { "seans" };
                s.push_str(&format!("  {anahtar}: {{label: \"{}\"; class: {sinif}}}\n", d2_kacis(&etiket)));
            }
            for (k, e) in self.listele(Some(a), None, bugun) {
                let anahtar = format!("is{}", k.id);
                let etiket = format!("#{} {}\\n{}", k.id, kisalt(&k.is_ad, 48), if e.blok_acar() { String::new() } else { kisalt(&k.sonraki_eylem, 56) });
                let mut siniflar = vec![if k.tur == Tur::Hedef { "hedef" } else { e.ad() }];
                if k.tur == Tur::Is && e == Durum::Acik && self.bloklayanlar(k, bugun).is_empty() {
                    siniflar.push("sirada");
                }
                s.push_str(&format!("  {anahtar}: {{label: \"{}\"; class: [{}]}}\n", d2_kacis(etiket.trim_end_matches("\\n")), siniflar.join("; ")));
            }
            for (k, _) in self.listele(Some(a), None, bugun) {
                for g in &k.girdi {
                    if self.kayitlar.get(g).is_some_and(|x| x.alan == a) {
                        s.push_str(&format!("  is{g} -> is{}: girdi\n", k.id));
                    }
                }
                if let Some(h) = k.hedef {
                    s.push_str(&format!("  is{} -> is{h}: hizmet {{style.stroke-dash: 3}}\n", k.id));
                }
            }
            for (i, se) in seanslar.iter().enumerate() {
                let anahtar = d2_anahtar(&format!("seans_{}", se.oturum));
                if i + 1 < seanslar.len() {
                    s.push_str(&format!("  {anahtar} -> {}: sonra {{style.stroke: \"#7048e8\"; style.bold: true}}\n", d2_anahtar(&format!("seans_{}", seanslar[i + 1].oturum))));
                }
                // Seans → iş kenarları: aynı alanda küme içinde; başka alanın kaydına dokunduysa küme dışına (yalnız tüm-sistem görünümünde).
                for (liste, etiket, renk) in [(&se.acilan, "açtı", "#7048e8"), (&se.bitirilen, "bitirdi", "#2f9e44")] {
                    for id in liste {
                        match self.kayitlar.get(id) {
                            Some(k) if k.alan == a => s.push_str(&format!("  {anahtar} -> is{id}: {etiket} {{style.stroke: \"{renk}\"; style.stroke-dash: 2}}\n")),
                            Some(k) if alan.is_none() => capraz.push(format!("{a}.{anahtar} -> {}.is{id}: {etiket} {{style.stroke: \"{renk}\"; style.stroke-dash: 2}}\n", k.alan)),
                            _ => {}
                        }
                    }
                }
            }
            s.push_str("}\n");
        }
        for c in &capraz {
            s.push_str(c);
        }
        // alanlar arası girdi kenarları
        if alan.is_none() {
            for k in self.kayitlar.values() {
                for g in &k.girdi {
                    if let Some(x) = self.kayitlar.get(g)
                        && x.alan != k.alan
                    {
                        s.push_str(&format!("{}.is{g} -> {}.is{}: girdi\n", x.alan, k.alan, k.id));
                    }
                }
            }
        }
        s
    }
}

fn d2_anahtar(s: &str) -> String {
    s.chars().map(|c| if c.is_ascii_alphanumeric() { c } else { '_' }).collect()
}

fn d2_kacis(s: &str) -> String {
    s.replace('"', "'")
}

fn kisalt(s: &str, n: usize) -> String {
    let t: String = s.chars().take(n).collect();
    if s.chars().count() > n { format!("{t}…") } else { t }
}

/// Kütük satırlarını (JSONL) olaylara çevirir; boş satırlar atlanır.
pub fn olaylari_oku(metin: &str) -> Result<Vec<Olay>, Hata> {
    let mut v = vec![];
    for (i, s) in metin.lines().enumerate() {
        if s.trim().is_empty() {
            continue;
        }
        v.push(serde_json::from_str(s).map_err(|e| Hata::Gecersiz(format!("kütük satır {}: {e}", i + 1)))?);
    }
    Ok(v)
}

pub fn olay_satiri(o: &Olay) -> String {
    serde_json::to_string(o).expect("olay serileştirilir")
}

/// Sistem saatinden `YYYY-MM-DDTHH:MM:SSZ` (UTC).
pub fn simdi_iso() -> String {
    let s = std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).map_or(0, |d| d.as_secs()) as i64;
    let (gun, sn) = (s.div_euclid(86400), s.rem_euclid(86400));
    // Howard Hinnant civil_from_days.
    let z = gun + 719_468;
    let era = z.div_euclid(146_097);
    let doe = z.rem_euclid(146_097);
    let yoe = (doe - doe / 1460 + doe / 36_524 - doe / 146_096) / 365;
    let y = yoe + era * 400;
    let doy = doe - (365 * yoe + yoe / 4 - yoe / 100);
    let mp = (5 * doy + 2) / 153;
    let d = doy - (153 * mp + 2) / 5 + 1;
    let m = if mp < 10 { mp + 3 } else { mp - 9 };
    let y = if m <= 2 { y + 1 } else { y };
    format!("{y:04}-{m:02}-{d:02}T{:02}:{:02}:{:02}Z", sn / 3600, sn % 3600 / 60, sn % 60)
}

/// Sistem saatinin yerel takvim günü `YYYY-MM-DD` (durum #7, Karar 68). Windows: `GetLocalTime`; diğerleri: `date +%F`;
/// ikisi de olmazsa UTC günü (sessiz değil: davranış `simdi_iso` ile aynı kalır).
pub fn yerel_tarih() -> String {
    #[cfg(windows)]
    {
        #[repr(C)]
        #[derive(Default)]
        struct SistemSaati {
            yil: u16,
            ay: u16,
            hafta_gunu: u16,
            gun: u16,
            saat: u16,
            dakika: u16,
            saniye: u16,
            ms: u16,
        }
        unsafe extern "system" {
            fn GetLocalTime(s: *mut SistemSaati);
        }
        let mut s = SistemSaati::default();
        // SAFETY: GetLocalTime yalnız verilen SYSTEMTIME yapısını (8 × u16) doldurur.
        unsafe { GetLocalTime(&mut s) };
        format!("{:04}-{:02}-{:02}", s.yil, s.ay, s.gun)
    }
    #[cfg(not(windows))]
    {
        std::process::Command::new("date")
            .arg("+%F")
            .output()
            .ok()
            .and_then(|o| String::from_utf8(o.stdout).ok())
            .map(|s| s.trim().to_string())
            .filter(|s| s.len() == 10)
            .unwrap_or_else(|| tarih_kismi(&simdi_iso()).to_string())
    }
}

#[cfg(test)]
mod testler {
    use super::*;

    const T: &str = "2026-10-14T09:00:00Z";

    fn ac(id: u64, alan: &str) -> Olay {
        let mut o = Olay::yalin(OlayTuru::Ac, id, T);
        o.alan = Some(alan.into());
        o.is_ad = Some(format!("is{id}"));
        o.sonraki_eylem = Some(format!("eylem{id}"));
        o
    }

    fn ol(t: OlayTuru, id: u64) -> Olay {
        Olay::yalin(t, id, T)
    }

    #[test]
    fn gecerli_zincir() {
        let d = Defter::katla(&[ac(1, "sage"), ol(OlayTuru::Al, 1), ol(OlayTuru::Bitir, 1), ol(OlayTuru::Tuket, 1)]).unwrap();
        assert_eq!(d.kayitlar[&1].durum, Durum::Tuketildi);
        assert!(d.kayitlar[&1].al_ts.is_some() && d.kayitlar[&1].bitir_ts.is_some());
    }

    #[test]
    fn gecersiz_gecisler() {
        for t in [OlayTuru::Bitir, OlayTuru::Tuket] {
            assert_eq!(Defter::katla(&[ac(1, "sage"), ol(t, 1)]).unwrap_err().kod(), 1);
        }
        assert!(Defter::katla(&[ac(1, "sage"), ol(OlayTuru::Al, 1), ol(OlayTuru::Al, 1)]).is_err());
        assert!(Defter::katla(&[ac(1, "sage"), ol(OlayTuru::Al, 1), ol(OlayTuru::Bitir, 1), ol(OlayTuru::Al, 1)]).is_err());
        assert!(Defter::katla(&[ol(OlayTuru::Al, 9)]).is_err());
        assert!(Defter::katla(&[ac(1, "sage"), ol(OlayTuru::Bayatla, 1), ol(OlayTuru::Bayatla, 1)]).is_err());
        assert!(Defter::katla(&[ac(1, "yok")]).is_err());
        // boşluk serbest (worktree çakışma koruması), geri/tekrar id yasak
        assert!(Defter::katla(&[ac(5, "sage")]).is_ok());
        assert!(Defter::katla(&[ac(5, "sage"), ac(5, "sage")]).is_err());
        assert!(Defter::katla(&[ac(5, "sage"), ac(3, "sage")]).is_err());
        assert!(Defter::katla(&[ac(0, "sage")]).is_err());
        let mut g = ac(1, "sage");
        g.girdi = vec![7];
        assert!(Defter::katla(&[g]).is_err());
        // hedef olmayan kayda hedef bağı
        let mut h = ac(2, "sage");
        h.hedef = Some(1);
        assert!(Defter::katla(&[ac(1, "sage"), h]).is_err());
    }

    #[test]
    fn bayatla_her_durumdan() {
        let zincir = [vec![], vec![OlayTuru::Al], vec![OlayTuru::Al, OlayTuru::Bitir], vec![OlayTuru::Al, OlayTuru::Bitir, OlayTuru::Tuket]];
        for ara in zincir {
            let mut v = vec![ac(1, "sage")];
            v.extend(ara.into_iter().map(|t| ol(t, 1)));
            v.push(ol(OlayTuru::Bayatla, 1));
            assert_eq!(Defter::katla(&v).unwrap().kayitlar[&1].durum, Durum::Bayat);
        }
    }

    #[test]
    fn son_gecerlilik_bayat_sayilir() {
        let mut a = ac(1, "sage");
        a.son_gecerlilik = Some("2026-10-13".into());
        let d = Defter::katla(&[a]).unwrap();
        assert_eq!(d.kayitlar[&1].efektif("2026-10-13T23:59:59Z"), Durum::Acik);
        assert_eq!(d.kayitlar[&1].efektif("2026-10-14T00:00:00Z"), Durum::Bayat);
        let mut d2 = d.clone();
        assert!(d2.uygula(&ol(OlayTuru::Al, 1), "2026-10-14").is_err());
        assert!(d.oturum_basi("sage", "2026-10-14").contains("açık iş yok"));
    }

    #[test]
    fn oturum_basi_sinirli() {
        let v: Vec<Olay> = (1..=160).map(|i| ac(i, "sage")).collect();
        let d = Defter::katla(&v).unwrap();
        let s = d.oturum_basi("sage", T);
        assert!(s.len() <= OTURUM_BASI_BAYT, "{}", s.len());
        assert!(s.contains("... +"));
        assert!(s.ends_with("akis-sage.d2\n"));
    }

    #[test]
    fn sirada_ve_bloklu() {
        // #1 açık, #2 girdisi #1 → bekler; #1 bitince #2 sırada; #3 hedef; #4 hedefe hizmet eder
        let mut b = ac(2, "sage");
        b.girdi = vec![1];
        let mut h = ac(3, "sage");
        h.tur = Some(Tur::Hedef);
        let mut i4 = ac(4, "sage");
        i4.hedef = Some(3);
        let mut v = vec![ac(1, "sage"), b, h, i4];
        let d = Defter::katla(&v).unwrap();
        let ids: Vec<u64> = d.sirada("sage", T).iter().map(|k| k.id).collect();
        assert_eq!(ids, vec![1, 4]);
        let brif = d.oturum_basi("sage", T);
        assert!(brif.contains("#2 bekler<-#1") && brif.contains("#3 HEDEF") && brif.contains("#1 SIRADA"));
        v.push(ol(OlayTuru::Al, 1));
        v.push(ol(OlayTuru::Bitir, 1));
        let d = Defter::katla(&v).unwrap();
        let ids: Vec<u64> = d.sirada("sage", T).iter().map(|k| k.id).collect();
        assert_eq!(ids, vec![2, 4]);
    }

    #[test]
    fn seans_dongusu_ve_graf() {
        let mut sa = Olay::seans(OlayTuru::SeansAc, "2026-10-14-sage", "sage", T);
        sa.hedef_cumle = Some("S1 dersi".into());
        let mut a1 = ac(1, "sage");
        a1.oturum = Some("2026-10-14-sage".into());
        let mut al = ol(OlayTuru::Al, 1);
        al.oturum = Some("2026-10-14-sage".into());
        let mut bt = ol(OlayTuru::Bitir, 1);
        bt.oturum = Some("2026-10-14-sage".into());
        let mut sk = Olay::seans(OlayTuru::SeansKapat, "2026-10-14-sage", "sage", "2026-10-14T12:00:00Z");
        sk.hedef_tutuldu = Some(true);
        sk.kayit = Some("sage/raporlar/seans/seans-teslim-2026-10-14-s1.json".into());
        sk.etiket = Some("s1".into());
        let d = Defter::katla(&[sa.clone(), a1, al, bt, sk.clone()]).unwrap();
        let s = &d.seanslar["2026-10-14-sage"];
        assert!(!s.ortuk && !s.acik() && s.hedef_tutuldu == Some(true));
        assert_eq!(s.dokunulan(), vec![1]);
        assert_eq!(d.kayitlar[&1].oturumlar, vec!["2026-10-14-sage".to_string()]);
        // çift açılış / çift kapanış / açılmamış kapanış reddedilir
        assert!(Defter::katla(&[sa.clone(), sa.clone()]).is_err());
        assert!(Defter::katla(&[sa.clone(), sk.clone(), sk.clone()]).is_err());
        assert!(Defter::katla(&[sk.clone()]).is_err());
        // örtük seans (eski kütük biçimi: seans_ac olmadan oturum alanı)
        let mut e = ac(1, "sage");
        e.oturum = Some("eski".into());
        let d2 = Defter::katla(&[e]).unwrap();
        assert!(d2.seanslar["eski"].ortuk);
        // graf modeli deterministik ve tam
        let m1 = d.graf_modeli(Some("sage"), T);
        let m2 = d.graf_modeli(Some("sage"), T);
        assert_eq!(m1, m2);
        assert_eq!(m1["meta"]["dugum_sayisi"], 2);
        let kenar_turleri: Vec<&str> = m1["kenarlar"].as_array().unwrap().iter().map(|k| k["tur"].as_str().unwrap()).collect();
        assert!(kenar_turleri.contains(&"acti") && kenar_turleri.contains(&"bitirdi"));
        let d2m = d.d2(Some("sage"), T);
        assert!(d2m.contains("seans_2026_10_14_sage") && d2m.contains("is1") && d2m.contains("bitirdi"));
        assert!(d.graf_metni("sage", T).contains("seans 2026-10-14-sage 2026-10-14"));
        // olay satırı yuvarlak gidiş-dönüş (seans olayında id yazılmaz)
        let satir = olay_satiri(&sk);
        assert!(!satir.contains("\"id\""));
        let geri: Olay = serde_json::from_str(&satir).unwrap();
        assert_eq!(geri, sk);
    }

    #[test]
    fn tarih_bicimi() {
        let s = simdi_iso();
        assert_eq!(s.len(), 20);
        assert!(s.starts_with("20") && s.ends_with('Z'));
    }
}
