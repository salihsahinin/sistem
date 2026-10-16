//! Python 3.11 `argparse` davranışının bu araçlarda kullanılan alt kümesi: yalnız isteğe bağlı (`--x`) bayraklar,
//! önek kısaltması (`--rep` → `--repo`), `--x=değer`, `nargs="*"`, `append`, `type=int`, `-h` yardımı, usage sarması ve hata iletileri.
//! Konumsal argüman yoktur; tanınmayan her dize `unrecognized arguments` olur. Yardım genişliği `COLUMNS` (yoksa 80) - 2.
use crate::py;
use std::collections::HashMap;

#[derive(Clone, Copy, PartialEq, Eq)]
pub enum Tip {
    Metin,
    Tam,
    Ondalik,
}

#[derive(Clone, Copy, PartialEq, Eq)]
pub enum Tur {
    /// `store_true`
    Bayrak,
    /// `store` (nargs=None)
    Deger,
    /// `-h/--help`
    Yardim,
}

pub struct Secenek {
    pub adlar: &'static [&'static str],
    pub dest: &'static str,
    pub tur: Tur,
    pub tip: Tip,
    pub yardim: Option<&'static str>,
}

impl Secenek {
    pub const fn bayrak(adlar: &'static [&'static str], dest: &'static str, yardim: Option<&'static str>) -> Self {
        Secenek { adlar, dest, tur: Tur::Bayrak, tip: Tip::Metin, yardim }
    }
    pub const fn deger(adlar: &'static [&'static str], dest: &'static str, yardim: Option<&'static str>) -> Self {
        Secenek { adlar, dest, tur: Tur::Deger, tip: Tip::Metin, yardim }
    }
    pub const fn tam(adlar: &'static [&'static str], dest: &'static str, yardim: Option<&'static str>) -> Self {
        Secenek { adlar, dest, tur: Tur::Deger, tip: Tip::Tam, yardim }
    }
    pub const fn ondalik(adlar: &'static [&'static str], dest: &'static str, yardim: Option<&'static str>) -> Self {
        Secenek { adlar, dest, tur: Tur::Deger, tip: Tip::Ondalik, yardim }
    }
    fn metavar(&self) -> String {
        self.dest.to_uppercase()
    }
    fn arguman_metni(&self) -> String {
        match self.tur {
            Tur::Deger => self.metavar(),
            _ => String::new(),
        }
    }
    fn ad(&self) -> String {
        self.adlar.join("/")
    }
}

pub struct Ayrisan {
    pub prog: &'static str,
    pub aciklama: Option<&'static str>,
    secenekler: Vec<Secenek>,
}

#[derive(Default, Debug)]
pub struct Sonuc {
    bayrak: HashMap<&'static str, bool>,
    metin: HashMap<&'static str, String>,
    tam: HashMap<&'static str, i128>,
    ondalik: HashMap<&'static str, f64>,
}

impl Sonuc {
    pub fn bayrak(&self, d: &str) -> bool {
        self.bayrak.get(d).copied().unwrap_or(false)
    }
    pub fn metin(&self, d: &str) -> Option<&str> {
        self.metin.get(d).map(String::as_str)
    }
    pub fn tam(&self, d: &str) -> Option<i128> {
        self.tam.get(d).copied()
    }
    pub fn ondalik(&self, d: &str) -> Option<f64> {
        self.ondalik.get(d).copied()
    }
}

#[derive(Clone)]
enum Sinif {
    /// argüman
    A,
    /// `--` işaretçisi
    Cizgi,
    /// seçenek: (eylem dizini ya da tanınmayan, seçenek metni, açık argüman)
    O(Option<usize>, String, Option<String>),
}

/// (eylem dizini ya da `None` = tanınmayan, seçenek metni, açık argüman)
type SecenekCozum = (Option<usize>, String, Option<String>);

fn negatif_sayi(s: &str) -> bool {
    let Some(r) = s.strip_prefix('-') else { return false };
    if !r.is_empty() && r.chars().all(|c| c.is_ascii_digit()) {
        return true;
    }
    // -\d*\.\d+
    match r.split_once('.') {
        Some((a, b)) => a.chars().all(|c| c.is_ascii_digit()) && !b.is_empty() && b.chars().all(|c| c.is_ascii_digit()),
        None => false,
    }
}

impl Ayrisan {
    pub fn yeni(prog: &'static str, aciklama: Option<&'static str>, mut secenekler: Vec<Secenek>) -> Self {
        secenekler.insert(0, Secenek { adlar: &["-h", "--help"], dest: "help", tur: Tur::Yardim, tip: Tip::Metin, yardim: Some("show this help message and exit") });
        Ayrisan { prog, aciklama, secenekler }
    }

    // ------------------------------------------------------------ biçimleme
    fn genislik() -> usize {
        let c = std::env::var("COLUMNS").ok().and_then(|v| py::int(&v)).filter(|&v| v > 0).unwrap_or(80);
        (c as usize).saturating_sub(2)
    }

    fn usage_parcalari(&self) -> Vec<String> {
        self.secenekler
            .iter()
            .map(|s| {
                let a = s.adlar[0];
                match s.tur {
                    Tur::Bayrak | Tur::Yardim => format!("[{a}]"),
                    _ => format!("[{a} {}]", s.arguman_metni()),
                }
            })
            .collect()
    }

    pub fn usage(&self) -> String {
        let genislik = Self::genislik();
        let onek = "usage: ";
        let parcalar = self.usage_parcalari();
        let kullanim = format!("{} {}", self.prog, parcalar.join(" "));
        let metin = if onek.chars().count() + kullanim.chars().count() > genislik {
            let mk = |parts: &[String], indent: &str, onek: Option<&str>| -> Vec<String> {
                let mut satirlar: Vec<String> = vec![];
                let mut satir: Vec<&str> = vec![];
                let mut uz = onek.map(|o| o.chars().count() as i64 - 1).unwrap_or(indent.chars().count() as i64 - 1);
                for p in parts {
                    let pl = p.chars().count() as i64;
                    if uz + 1 + pl > genislik as i64 && !satir.is_empty() {
                        satirlar.push(format!("{indent}{}", satir.join(" ")));
                        satir.clear();
                        uz = indent.chars().count() as i64 - 1;
                    }
                    satir.push(p);
                    uz += pl + 1;
                }
                if !satir.is_empty() {
                    satirlar.push(format!("{indent}{}", satir.join(" ")));
                }
                if onek.is_some() && !satirlar.is_empty() {
                    let ic = indent.chars().count();
                    satirlar[0] = satirlar[0].chars().skip(ic).collect();
                }
                satirlar
            };
            let satirlar = if (onek.chars().count() + self.prog.chars().count()) as f64 <= 0.75 * genislik as f64 {
                let indent = " ".repeat(onek.chars().count() + self.prog.chars().count() + 1);
                let mut parts = vec![self.prog.to_string()];
                parts.extend(parcalar.iter().cloned());
                mk(&parts, &indent, Some(onek))
            } else {
                let indent = " ".repeat(onek.chars().count());
                let mut l = vec![self.prog.to_string()];
                l.extend(mk(&parcalar, &indent, None));
                l
            };
            satirlar.join("\n")
        } else {
            kullanim
        };
        format!("{onek}{metin}\n")
    }

    fn yardim_metni(&self) -> String {
        let genislik = Self::genislik();
        let maks_pozisyon = 24.min(genislik.saturating_sub(20).max(4));
        let girinti = 2usize;
        let eylem_maks = self.secenekler.iter().map(|s| Self::cagri(s).chars().count() + girinti).max().unwrap_or(0);
        let yardim_pozisyon = (eylem_maks + 2).min(maks_pozisyon);
        let yardim_genislik = genislik.saturating_sub(yardim_pozisyon).max(11);
        let eylem_genislik = yardim_pozisyon - girinti - 2;
        let mut r = format!("{}\n", self.usage());
        if let Some(a) = self.aciklama {
            r.push_str(a);
            r.push_str("\n\n");
        }
        r.push_str("\noptions:\n");
        for s in &self.secenekler {
            let baslik = Self::cagri(s);
            let mut satir = String::new();
            let mut ilk_girinti = 0;
            match s.yardim.filter(|h| !h.is_empty()) {
                None => satir.push_str(&format!("{}{baslik}\n", " ".repeat(girinti))),
                Some(_) if baslik.chars().count() <= eylem_genislik => {
                    satir.push_str(&format!("{}{}  ", " ".repeat(girinti), py::sola_hizala(&baslik, eylem_genislik)));
                }
                Some(_) => {
                    satir.push_str(&format!("{}{baslik}\n", " ".repeat(girinti)));
                    ilk_girinti = yardim_pozisyon;
                }
            }
            if let Some(h) = s.yardim.filter(|h| !h.is_empty()) {
                let satirlar = sar(h, yardim_genislik);
                satir.push_str(&format!("{}{}\n", " ".repeat(ilk_girinti), satirlar[0]));
                for l in &satirlar[1..] {
                    satir.push_str(&format!("{}{l}\n", " ".repeat(yardim_pozisyon)));
                }
            }
            r.push_str(&satir);
        }
        r.push('\n');
        // _long_break_matcher: \n\n\n+ -> \n\n ; strip('\n') + '\n'
        let mut son = String::new();
        let mut nl = 0;
        for c in r.chars() {
            if c == '\n' {
                nl += 1;
                if nl <= 2 {
                    son.push(c);
                }
            } else {
                nl = 0;
                son.push(c);
            }
        }
        format!("{}\n", son.trim_matches('\n'))
    }

    fn cagri(s: &Secenek) -> String {
        match s.tur {
            Tur::Bayrak | Tur::Yardim => s.adlar.join(", "),
            _ => s.adlar.iter().map(|a| format!("{a} {}", s.arguman_metni())).collect::<Vec<_>>().join(", "),
        }
    }

    fn hata(&self, mesaj: &str) -> i32 {
        py::err(&self.usage());
        py::err(&format!("{}: error: {mesaj}\n", self.prog));
        2
    }

    fn arg_hata(&self, s: &Secenek, mesaj: &str) -> i32 {
        self.hata(&format!("argument {}: {mesaj}", s.ad()))
    }

    // ------------------------------------------------------------ ayrıştırma
    fn eylem_ara(&self, ad: &str) -> Option<usize> {
        self.secenekler.iter().position(|s| s.adlar.contains(&ad))
    }

    fn secenek_adlari(&self) -> Vec<(usize, &'static str)> {
        self.secenekler.iter().enumerate().flat_map(|(i, s)| s.adlar.iter().map(move |a| (i, *a))).collect()
    }

    /// `_parse_optional`: `Ok(None)` argüman, `Ok(Some(..))` seçenek, `Err` belirsiz kısaltma (çıkış kodu).
    fn secenek_coz(&self, s: &str) -> Result<Option<SecenekCozum>, i32> {
        if s.is_empty() || !s.starts_with('-') {
            return Ok(None);
        }
        if let Some(i) = self.eylem_ara(s) {
            return Ok(Some((Some(i), s.to_string(), None)));
        }
        if s.chars().count() == 1 {
            return Ok(None);
        }
        if let Some((o, e)) = s.split_once('=')
            && let Some(i) = self.eylem_ara(o)
        {
            return Ok(Some((Some(i), o.to_string(), Some(e.to_string()))));
        }
        let mut adaylar: Vec<(usize, String, Option<String>)> = vec![];
        let ikinci: Option<char> = s.chars().nth(1);
        if ikinci == Some('-') {
            let (onek, acik) = match s.split_once('=') {
                Some((o, e)) => (o, Some(e.to_string())),
                None => (s, None),
            };
            for (i, a) in self.secenek_adlari() {
                if a.starts_with(onek) {
                    adaylar.push((i, a.to_string(), acik.clone()));
                }
            }
        } else {
            let kisa: String = s.chars().take(2).collect();
            let kisa_acik: String = s.chars().skip(2).collect();
            for (i, a) in self.secenek_adlari() {
                if a == kisa {
                    adaylar.push((i, a.to_string(), Some(kisa_acik.clone())));
                } else if a.starts_with(s) {
                    adaylar.push((i, a.to_string(), None));
                }
            }
        }
        if adaylar.len() > 1 {
            let eslesen = adaylar.iter().map(|(_, a, _)| a.as_str()).collect::<Vec<_>>().join(", ");
            return Err(self.hata(&format!("ambiguous option: {s} could match {eslesen}")));
        }
        if let Some((i, a, e)) = adaylar.into_iter().next() {
            return Ok(Some((Some(i), a, e)));
        }
        if negatif_sayi(s) || s.contains(' ') {
            return Ok(None);
        }
        Ok(Some((None, s.to_string(), None)))
    }

    /// Ayrıştırır. `Err(kod)`: iletiyi basıp çıkılacak durum (yardım 0, hata 2).
    pub fn ayristir(&self, argv: &[String]) -> Result<Sonuc, i32> {
        let mut sinif: Vec<Sinif> = Vec::with_capacity(argv.len());
        let mut cizgi_goruldu = false;
        for a in argv {
            if cizgi_goruldu {
                sinif.push(Sinif::A);
            } else if a == "--" {
                sinif.push(Sinif::Cizgi);
                cizgi_goruldu = true;
            } else {
                match self.secenek_coz(a)? {
                    None => sinif.push(Sinif::A),
                    Some((i, o, e)) => sinif.push(Sinif::O(i, o, e)),
                }
            }
        }
        let mut sonuc = Sonuc::default();
        let mut ekstra: Vec<String> = vec![];
        let mut i = 0;
        while i < argv.len() {
            let Sinif::O(eylem, secenek, acik) = sinif[i].clone() else {
                ekstra.push(argv[i].clone());
                i += 1;
                continue;
            };
            let Some(mut e) = eylem else {
                ekstra.push(argv[i].clone());
                i += 1;
                continue;
            };
            let mut secenek = secenek;
            let mut acik = acik;
            let mut islemler: Vec<(usize, Vec<String>)> = vec![];
            let bitis;
            loop {
                let s = &self.secenekler[e];
                let sifir = matches!(s.tur, Tur::Bayrak | Tur::Yardim);
                if let Some(a) = acik.clone() {
                    let adet = if sifir { 0 } else { 1 };
                    let tek_tire = secenek.chars().nth(1).is_some_and(|c| c != '-');
                    if adet == 0 && tek_tire {
                        islemler.push((e, vec![]));
                        let ilk = a.chars().next();
                        let yeni = format!("-{}", ilk.map(String::from).unwrap_or_default());
                        let kalan: String = a.chars().skip(1).collect();
                        if ilk.is_some()
                            && let Some(j) = self.eylem_ara(&yeni)
                        {
                            e = j;
                            secenek = yeni;
                            acik = if kalan.is_empty() { None } else { Some(kalan) };
                            continue;
                        }
                        return Err(self.arg_hata(s, &format!("ignored explicit argument {}", py::repr(&a))));
                    } else if adet == 1 {
                        islemler.push((e, vec![a]));
                        bitis = i + 1;
                        break;
                    } else {
                        return Err(self.arg_hata(s, &format!("ignored explicit argument {}", py::repr(&a))));
                    }
                }
                let mut adet = 0;
                if !sifir {
                    if i + 1 < argv.len() && matches!(sinif[i + 1], Sinif::A) {
                        adet = 1;
                    } else {
                        return Err(self.arg_hata(s, "expected one argument"));
                    }
                }
                islemler.push((e, argv[i + 1..i + 1 + adet].to_vec()));
                bitis = i + 1 + adet;
                break;
            }
            for (e, mut degerler) in islemler {
                let s = &self.secenekler[e];
                if let Some(p) = degerler.iter().position(|d| d == "--") {
                    degerler.remove(p);
                }
                match s.tur {
                    Tur::Yardim => {
                        py::out(&self.yardim_metni());
                        return Err(0);
                    }
                    Tur::Bayrak => {
                        sonuc.bayrak.insert(s.dest, true);
                    }
                    Tur::Deger => {
                        let v = degerler.into_iter().next().unwrap_or_default();
                        match s.tip {
                            Tip::Tam => match py::int(&v) {
                                Some(n) => {
                                    sonuc.tam.insert(s.dest, n);
                                }
                                None => return Err(self.arg_hata(s, &format!("invalid int value: {}", py::repr(&v)))),
                            },
                            Tip::Ondalik => match py::float(&v) {
                                Some(n) => {
                                    sonuc.ondalik.insert(s.dest, n);
                                }
                                None => return Err(self.arg_hata(s, &format!("invalid float value: {}", py::repr(&v)))),
                            },
                            Tip::Metin => {
                                sonuc.metin.insert(s.dest, v);
                            }
                        }
                    }
                }
            }
            i = bitis;
        }
        if !ekstra.is_empty() {
            return Err(self.hata(&format!("unrecognized arguments: {}", ekstra.join(" "))));
        }
        Ok(sonuc)
    }
}

/// `textwrap.wrap(' '.join(text.split()), genislik)` (Python 3.11 `_wrap_chunks`; yalnız boşluk sınırlı parçalar, tirede bölme yok).
/// Dar genişlikte uzun sözcük bölünürken satır sonunda boşluk kalması (`adı tarihi `) Python'daki gibi korunur.
fn sar(metin: &str, genislik: usize) -> Vec<String> {
    let norm = metin.split_whitespace().collect::<Vec<_>>().join(" ");
    // parçalar: sözcük ve tek boşluk dönüşümlü
    let mut parcalar: Vec<String> = vec![];
    for (i, s) in norm.split(' ').enumerate() {
        if i > 0 {
            parcalar.push(" ".to_string());
        }
        if !s.is_empty() {
            parcalar.push(s.to_string());
        }
    }
    parcalar.reverse();
    let uz = |s: &str| s.chars().count();
    let bos = |s: &str| s.trim().is_empty();
    let mut satirlar: Vec<String> = vec![];
    while !parcalar.is_empty() {
        let mut satir: Vec<String> = vec![];
        let mut sl = 0;
        if parcalar.last().is_some_and(|c| bos(c)) && !satirlar.is_empty() {
            parcalar.pop();
        }
        while let Some(c) = parcalar.last() {
            let l = uz(c);
            if sl + l <= genislik {
                sl += l;
                satir.push(parcalar.pop().unwrap());
            } else {
                break;
            }
        }
        if let Some(c) = parcalar.pop_if(|c| uz(c) > genislik) {
            // _handle_long_word
            let kalan = if genislik < 1 { 1 } else { genislik.saturating_sub(sl) };
            let bas: String = c.chars().take(kalan).collect();
            let son: String = c.chars().skip(kalan).collect();
            satir.push(bas);
            parcalar.push(son);
        }
        if satir.last().is_some_and(|c| bos(c)) {
            satir.pop();
        }
        if !satir.is_empty() {
            satirlar.push(satir.concat());
        }
    }
    if satirlar.is_empty() {
        satirlar.push(String::new());
    }
    satirlar
}
