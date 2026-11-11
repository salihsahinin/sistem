//! Python 3.11 `argparse` davranışının bu araçlarda kullanılan alt kümesi: yalnız isteğe bağlı (`--x`) bayraklar,
//! önek kısaltması (`--rep` → `--repo`), `--x=değer`, `nargs="*"`, `append`, `type=int`, `choices` (`secimli`), karşılıklı dışlayan grup (`dislayan`),
//! `-h` yardımı, usage sarması ve hata iletileri.
//! Konumsal argüman yoktur; tanınmayan her dize `unrecognized arguments` olur. Yardım genişliği `COLUMNS` (yoksa 80) - 2.
use crate::py;
use std::collections::HashMap;

#[derive(Clone, Copy, PartialEq, Eq)]
pub enum Tur {
    /// `store_true`
    Bayrak,
    /// `store` (nargs=None)
    Deger,
    /// `append`
    Ekle,
    /// `nargs="*"`
    Liste,
    /// `-h/--help`
    Yardim,
}

pub struct Secenek {
    pub adlar: &'static [&'static str],
    pub dest: &'static str,
    pub tur: Tur,
    pub tamsayi: bool,
    pub yardim: Option<&'static str>,
    /// `choices=[...]` (`None`: serbest değer)
    pub secimler: Option<&'static [&'static str]>,
}

impl Secenek {
    pub const fn bayrak(adlar: &'static [&'static str], dest: &'static str, yardim: Option<&'static str>) -> Self {
        Secenek { adlar, dest, tur: Tur::Bayrak, tamsayi: false, yardim, secimler: None }
    }
    pub const fn deger(adlar: &'static [&'static str], dest: &'static str, yardim: Option<&'static str>) -> Self {
        Secenek { adlar, dest, tur: Tur::Deger, tamsayi: false, yardim, secimler: None }
    }
    pub const fn tam(adlar: &'static [&'static str], dest: &'static str, yardim: Option<&'static str>) -> Self {
        Secenek { adlar, dest, tur: Tur::Deger, tamsayi: true, yardim, secimler: None }
    }
    pub const fn ekle(adlar: &'static [&'static str], dest: &'static str, yardim: Option<&'static str>) -> Self {
        Secenek { adlar, dest, tur: Tur::Ekle, tamsayi: false, yardim, secimler: None }
    }
    pub const fn liste(adlar: &'static [&'static str], dest: &'static str, yardim: Option<&'static str>) -> Self {
        Secenek { adlar, dest, tur: Tur::Liste, tamsayi: false, yardim, secimler: None }
    }
    /// `choices=[...]`: usage/yardımda metavar `{a,b}`; geçersiz değer `invalid choice` hatası verir.
    pub fn secimli(mut self, secimler: &'static [&'static str]) -> Self {
        self.secimler = Some(secimler);
        self
    }
    fn metavar(&self) -> String {
        match self.secimler {
            Some(s) => format!("{{{}}}", s.join(",")),
            None => self.dest.to_uppercase(),
        }
    }
    fn arguman_metni(&self) -> String {
        match self.tur {
            Tur::Deger | Tur::Ekle => self.metavar(),
            Tur::Liste => format!("[{} ...]", self.metavar()),
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
    /// tek konumsal argüman (`add_argument("spec")`, nargs=None, zorunlu); yok ise `None`
    konumsal: Option<&'static str>,
    /// karşılıklı dışlayan gruplar: (üye `dest` adları, zorunlu mu); üyeler seçenek listesinde ardışık olmalıdır
    dislayanlar: Vec<(&'static [&'static str], bool)>,
}

#[derive(Default, Debug)]
pub struct Sonuc {
    bayrak: HashMap<&'static str, bool>,
    metin: HashMap<&'static str, String>,
    tam: HashMap<&'static str, i128>,
    liste: HashMap<&'static str, Vec<String>>,
    konumsal: Option<String>,
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
    /// `nargs="*"` ya da `append` değerleri (verilmediyse `None`).
    pub fn liste(&self, d: &str) -> Option<&Vec<String>> {
        self.liste.get(d)
    }
    /// konumsal argümanın değeri (ayrıştırma başarılıysa her zaman dolu)
    pub fn konumsal(&self) -> Option<&str> {
        self.konumsal.as_deref()
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
        secenekler.insert(0, Secenek { adlar: &["-h", "--help"], dest: "help", tur: Tur::Yardim, tamsayi: false, yardim: Some("show this help message and exit"), secimler: None });
        Ayrisan { prog, aciklama, secenekler, konumsal: None, dislayanlar: vec![] }
    }

    /// Tek zorunlu konumsal argüman ekler (`ap.add_argument(ad)`); usage'da seçeneklerden sonra gelir.
    pub fn konumsal(mut self, ad: &'static str) -> Self {
        self.konumsal = Some(ad);
        self
    }

    /// `ap.add_mutually_exclusive_group(required=zorunlu)`: usage'da ilk üyenin yerinde `(a | b)` (zorunlu) ya da `[a | b]` olarak görünür.
    pub fn dislayan(mut self, uyeler: &'static [&'static str], zorunlu: bool) -> Self {
        self.dislayanlar.push((uyeler, zorunlu));
        self
    }

    // ------------------------------------------------------------ biçimleme
    fn genislik() -> usize {
        let c = std::env::var("COLUMNS").ok().and_then(|v| py::int(&v)).filter(|&v| v > 0).unwrap_or(80);
        (c as usize).saturating_sub(2)
    }

    fn usage_parcalari(&self) -> Vec<String> {
        let parca = |s: &Secenek, koseli: bool| -> String {
            let a = s.adlar[0];
            let ic = match s.tur {
                Tur::Bayrak | Tur::Yardim => a.to_string(),
                _ => format!("{a} {}", s.arguman_metni()),
            };
            if koseli { format!("[{ic}]") } else { ic }
        };
        let mut parcalar = vec![];
        let mut i = 0;
        while i < self.secenekler.len() {
            let s = &self.secenekler[i];
            let grup = self.dislayanlar.iter().find(|(u, _)| {
                u.len() > 0 && i + u.len() <= self.secenekler.len() && u.iter().zip(&self.secenekler[i..]).all(|(d, x)| *d == x.dest)
            });
            if let Some((uyeler, zorunlu)) = grup {
                let ic: Vec<String> = self.secenekler[i..i + uyeler.len()].iter().map(|x| parca(x, false)).collect();
                let (ac, kapa) = if *zorunlu { ("(", ")") } else { ("[", "]") };
                parcalar.push(format!("{ac}{}{kapa}", ic.join(" | ")));
                i += uyeler.len();
                continue;
            }
            parcalar.push(parca(s, true));
            i += 1;
        }
        parcalar
    }

    /// `take_action`'daki karşılıklı dışlama denetimi: aynı gruptan daha önce görülmüş üye varsa hata; değilse eylemi görülmüş say.
    fn cakisma(&self, gorulen: &mut Vec<usize>, e: usize) -> Result<(), i32> {
        let s = &self.secenekler[e];
        for (uyeler, _) in &self.dislayanlar {
            if !uyeler.contains(&s.dest) {
                continue;
            }
            for u in uyeler.iter().filter(|u| **u != s.dest) {
                if let Some(k) = self.secenekler.iter().position(|x| x.dest == *u)
                    && gorulen.contains(&k)
                {
                    return Err(self.arg_hata(s, &format!("not allowed with argument {}", self.secenekler[k].ad())));
                }
            }
        }
        gorulen.push(e);
        Ok(())
    }

    pub fn usage(&self) -> String {
        let genislik = Self::genislik();
        let onek = "usage: ";
        let parcalar = self.usage_parcalari();
        let konum: Vec<String> = self.konumsal.map(|k| vec![k.to_string()]).unwrap_or_default();
        let mut tum = parcalar.clone();
        tum.extend(konum.iter().cloned());
        let kullanim = format!("{} {}", self.prog, tum.join(" "));
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
                let mut l = mk(&parts, &indent, Some(onek));
                l.extend(mk(&konum, &indent, None));
                l
            } else {
                let indent = " ".repeat(onek.chars().count());
                let mut satirlar = mk(&tum, &indent, None);
                if satirlar.len() > 1 {
                    satirlar = mk(&parcalar, &indent, None);
                    satirlar.extend(mk(&konum, &indent, None));
                }
                let mut l = vec![self.prog.to_string()];
                l.extend(satirlar);
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
        let mut eylem_maks = self.secenekler.iter().map(|s| Self::cagri(s).chars().count() + girinti).max().unwrap_or(0);
        if let Some(k) = self.konumsal {
            eylem_maks = eylem_maks.max(k.chars().count() + girinti);
        }
        let yardim_pozisyon = (eylem_maks + 2).min(maks_pozisyon);
        let yardim_genislik = genislik.saturating_sub(yardim_pozisyon).max(11);
        let eylem_genislik = yardim_pozisyon - girinti - 2;
        let mut r = format!("{}\n", self.usage());
        if let Some(a) = self.aciklama {
            r.push_str(a);
            r.push_str("\n\n");
        }
        if let Some(k) = self.konumsal {
            r.push_str(&format!("\npositional arguments:\n{}{k}\n", " ".repeat(girinti)));
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
        let mut gorulen: Vec<usize> = vec![];
        let mut ekstra: Vec<String> = vec![];
        let mut i = 0;
        while i < argv.len() {
            let Sinif::O(eylem, secenek, acik) = sinif[i].clone() else {
                if self.konumsal.is_some() && sonuc.konumsal.is_none() {
                    // `-*A-*` deseni: konumsal değer bir `--` ile başlayabilir (`--` değerden atılır)
                    let a = if matches!(sinif[i], Sinif::Cizgi) && i + 1 < argv.len() && matches!(sinif[i + 1], Sinif::A) { i + 1 } else { i };
                    if matches!(sinif[a], Sinif::A) {
                        sonuc.konumsal = Some(argv[a].clone());
                        i = a + 1;
                        continue;
                    }
                }
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
                    while i + 1 + adet < argv.len() && matches!(sinif[i + 1 + adet], Sinif::A) {
                        adet += 1;
                        if s.tur != Tur::Liste {
                            break;
                        }
                    }
                    if adet == 0 && s.tur != Tur::Liste {
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
                        self.cakisma(&mut gorulen, e)?;
                        sonuc.bayrak.insert(s.dest, true);
                    }
                    Tur::Deger | Tur::Ekle => {
                        let v = degerler.into_iter().next().unwrap_or_default();
                        if s.tamsayi {
                            match py::int(&v) {
                                Some(n) => {
                                    self.cakisma(&mut gorulen, e)?;
                                    sonuc.tam.insert(s.dest, n);
                                }
                                None => return Err(self.arg_hata(s, &format!("invalid int value: {}", py::repr(&v)))),
                            }
                        } else {
                            if let Some(secimler) = s.secimler
                                && !secimler.contains(&v.as_str())
                            {
                                let liste = secimler.iter().map(|c| py::repr(c)).collect::<Vec<_>>().join(", ");
                                return Err(self.arg_hata(s, &format!("invalid choice: {} (choose from {liste})", py::repr(&v))));
                            }
                            self.cakisma(&mut gorulen, e)?;
                            if s.tur == Tur::Ekle {
                                sonuc.liste.entry(s.dest).or_default().push(v);
                            } else {
                                sonuc.metin.insert(s.dest, v);
                            }
                        }
                    }
                    Tur::Liste => {
                        self.cakisma(&mut gorulen, e)?;
                        sonuc.liste.insert(s.dest, degerler);
                    }
                }
            }
            i = bitis;
        }
        if self.konumsal.is_some() && sonuc.konumsal.is_none() {
            return Err(self.hata(&format!("the following arguments are required: {}", self.konumsal.unwrap_or(""))));
        }
        for (uyeler, zorunlu) in &self.dislayanlar {
            if *zorunlu && !uyeler.iter().any(|u| gorulen.iter().any(|&k| self.secenekler[k].dest == *u)) {
                let adlar: Vec<String> = uyeler.iter().filter_map(|u| self.secenekler.iter().find(|x| x.dest == *u)).map(Secenek::ad).collect();
                return Err(self.hata(&format!("one of the arguments {} is required", adlar.join(" "))));
            }
        }
        if !ekstra.is_empty() {
            return Err(self.hata(&format!("unrecognized arguments: {}", ekstra.join(" "))));
        }
        Ok(sonuc)
    }
}

/// `textwrap.TextWrapper.wordsep_re` tire kuralı: iki harf (ya da `h-h-`) ardından `-`, sonrasında `h` `-`? `h` gelen tireden sonra bölünür.
fn tire_parcala(s: &str, cikti: &mut Vec<String>) {
    let c: Vec<char> = s.chars().collect();
    let harf = |i: usize| c.get(i).is_some_and(|x| x.is_alphabetic() || *x == '_');
    let mut bas = 0;
    for i in 1..c.len() {
        if c[i] != '-' {
            continue;
        }
        let geri = (i >= 2 && harf(i - 2) && harf(i - 1)) || (i >= 3 && harf(i - 3) && c[i - 2] == '-' && harf(i - 1));
        let ileri = (harf(i + 1) && harf(i + 2)) || (harf(i + 1) && c.get(i + 2) == Some(&'-') && harf(i + 3));
        if geri && ileri {
            cikti.push(c[bas..=i].iter().collect());
            bas = i + 1;
        }
    }
    cikti.push(c[bas..].iter().collect());
}

/// `textwrap.wrap(' '.join(text.split()), genislik)` (Python 3.11 `_wrap_chunks`; boşlukta ve `break_on_hyphens` kuralıyla tirede bölünür).
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
            tire_parcala(s, &mut parcalar);
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

/// argparse varsayılan biçimleyicisinin açıklama sarması (`HelpFormatter._fill_text`): genişlik = COLUMNS (yoksa 80) - 2. `Ayrisan` açıklamayı sarmaz; sarılacak açıklamayı çağıran bununla hazırlar.
pub fn aciklama_sar(metin: &str) -> String {
    let kolon = std::env::var("COLUMNS").ok().and_then(|v| crate::py::int(&v)).filter(|&v| v > 0).unwrap_or(80);
    sar(metin, (kolon as usize).saturating_sub(2).max(11)).join("\n")
}
