//! Python `difflib.unified_diff` (3.11) birebir portu: `SequenceMatcher` (`find_longest_match`, autojunk, `get_matching_blocks`,
//! `get_opcodes`, `get_grouped_opcodes`) + `unified_diff` (isjunk yok, `lineterm='\n'`, tarih alanları boş).
//! Satırlar dizgi olarak karşılaştırılır; hızlı olsun diye her ayrı satır bir tamsayı kimliğine çevrilir (eşitlik anlamı aynı).
use std::collections::HashMap;

/// `str.splitlines(keepends=True)`: Unicode satır sınırları (\n \r \r\n \v \f \x1c-\x1e \x85 \u2028 \u2029), sınırlayıcı satırda kalır.
pub fn splitlines_keepends(s: &str) -> Vec<String> {
    let mut sonuc = vec![];
    let mut satir = String::new();
    let mut it = s.chars().peekable();
    while let Some(c) = it.next() {
        satir.push(c);
        match c {
            '\r' => {
                if it.peek() == Some(&'\n') {
                    satir.push('\n');
                    it.next();
                }
                sonuc.push(std::mem::take(&mut satir));
            }
            '\n' | '\u{b}' | '\u{c}' | '\u{1c}' | '\u{1d}' | '\u{1e}' | '\u{85}' | '\u{2028}' | '\u{2029}' => sonuc.push(std::mem::take(&mut satir)),
            _ => {}
        }
    }
    if !satir.is_empty() {
        sonuc.push(satir);
    }
    sonuc
}

#[derive(Clone, Copy, PartialEq, Eq, Debug)]
enum Etiket {
    Esit,
    Degis,
    Sil,
    Ekle,
}

type Op = (Etiket, usize, usize, usize, usize);

struct Eslestirici {
    a: Vec<usize>,
    b: Vec<usize>,
    /// b'deki her kimliğin konumları (popüler öğeler boşaltılır: Python'da `b2j`'den silinir)
    b2j: Vec<Vec<usize>>,
    // `find_longest_match` çalışma belleği (çağrılar arası yeniden kullanılır; her çağrı sonunda sıfırlanır)
    onceki: Vec<usize>,
    yeni: Vec<usize>,
}

impl Eslestirici {
    fn yeni(a: &[String], b: &[String]) -> Self {
        let mut kimlik: HashMap<&str, usize> = HashMap::new();
        let mut a_k = Vec::with_capacity(a.len());
        let mut b_k = Vec::with_capacity(b.len());
        for s in b {
            let n = kimlik.len();
            b_k.push(*kimlik.entry(s.as_str()).or_insert(n));
        }
        for s in a {
            let n = kimlik.len();
            a_k.push(*kimlik.entry(s.as_str()).or_insert(n));
        }
        let mut b2j: Vec<Vec<usize>> = vec![vec![]; kimlik.len()];
        for (j, &k) in b_k.iter().enumerate() {
            b2j[k].push(j);
        }
        // autojunk: b'de >= 200 öğe varsa, (n/100 + 1)'den çok geçen öğeler "popüler" sayılıp b2j'den silinir
        let n = b_k.len();
        if n >= 200 {
            let ntest = n / 100 + 1;
            for idx in b2j.iter_mut() {
                if idx.len() > ntest {
                    idx.clear();
                }
            }
        }
        let lb = b_k.len();
        Eslestirici { a: a_k, b: b_k, b2j, onceki: vec![0; lb + 1], yeni: vec![0; lb + 1] }
    }

    /// `find_longest_match(alo, ahi, blo, bhi)`: (besti, bestj, bestsize). Popüler öğeler b2j'de olmadığından önce çekirdek bulunur,
    /// sonra iki uca eşit öğelerle (junk yok) genişletilir.
    fn en_uzun(&mut self, alo: usize, ahi: usize, blo: usize, bhi: usize) -> (usize, usize, usize) {
        let (mut besti, mut bestj, mut bestsize) = (alo, blo, 0usize);
        // j2len: j konumu `j + 1` dizinindedir (j - 1 sorgusu `j` dizinine düşer; dizin 0 hiç yazılmaz)
        let mut onceki = std::mem::take(&mut self.onceki);
        let mut yeni = std::mem::take(&mut self.yeni);
        let mut onceki_dok: Vec<usize> = vec![];
        let mut yeni_dok: Vec<usize> = vec![];
        for i in alo..ahi {
            for &j in &self.b2j[self.a[i]] {
                if j < blo {
                    continue;
                }
                if j >= bhi {
                    break;
                }
                let k = onceki[j] + 1;
                yeni[j + 1] = k;
                yeni_dok.push(j + 1);
                if k > bestsize {
                    besti = i + 1 - k;
                    bestj = j + 1 - k;
                    bestsize = k;
                }
            }
            for &x in &onceki_dok {
                onceki[x] = 0;
            }
            onceki_dok.clear();
            std::mem::swap(&mut onceki, &mut yeni);
            std::mem::swap(&mut onceki_dok, &mut yeni_dok);
        }
        for &x in &onceki_dok {
            onceki[x] = 0;
        }
        self.onceki = onceki;
        self.yeni = yeni;
        while besti > alo && bestj > blo && self.a[besti - 1] == self.b[bestj - 1] {
            besti -= 1;
            bestj -= 1;
            bestsize += 1;
        }
        while besti + bestsize < ahi && bestj + bestsize < bhi && self.a[besti + bestsize] == self.b[bestj + bestsize] {
            bestsize += 1;
        }
        (besti, bestj, bestsize)
    }

    /// `get_matching_blocks()`: (i, j, boyut) üçlüleri; sonda (len(a), len(b), 0) nöbetçisi.
    fn eslesen_bloklar(&mut self) -> Vec<(usize, usize, usize)> {
        let (la, lb) = (self.a.len(), self.b.len());
        let mut kuyruk = vec![(0usize, la, 0usize, lb)];
        let mut bloklar: Vec<(usize, usize, usize)> = vec![];
        while let Some((alo, ahi, blo, bhi)) = kuyruk.pop() {
            let (i, j, k) = self.en_uzun(alo, ahi, blo, bhi);
            if k > 0 {
                bloklar.push((i, j, k));
                if alo < i && blo < j {
                    kuyruk.push((alo, i, blo, j));
                }
                if i + k < ahi && j + k < bhi {
                    kuyruk.push((i + k, ahi, j + k, bhi));
                }
            }
        }
        bloklar.sort();
        let (mut i1, mut j1, mut k1) = (0usize, 0usize, 0usize);
        let mut bitisik: Vec<(usize, usize, usize)> = vec![];
        for (i2, j2, k2) in bloklar {
            if i1 + k1 == i2 && j1 + k1 == j2 {
                k1 += k2;
            } else {
                if k1 > 0 {
                    bitisik.push((i1, j1, k1));
                }
                i1 = i2;
                j1 = j2;
                k1 = k2;
            }
        }
        if k1 > 0 {
            bitisik.push((i1, j1, k1));
        }
        bitisik.push((la, lb, 0));
        bitisik
    }

    /// `get_opcodes()`.
    fn opkodlar(&mut self) -> Vec<Op> {
        let (mut i, mut j) = (0usize, 0usize);
        let mut cevap: Vec<Op> = vec![];
        for (ai, bj, boyut) in self.eslesen_bloklar() {
            let etiket = if i < ai && j < bj {
                Some(Etiket::Degis)
            } else if i < ai {
                Some(Etiket::Sil)
            } else if j < bj {
                Some(Etiket::Ekle)
            } else {
                None
            };
            if let Some(e) = etiket {
                cevap.push((e, i, ai, j, bj));
            }
            i = ai + boyut;
            j = bj + boyut;
            if boyut > 0 {
                cevap.push((Etiket::Esit, ai, i, bj, j));
            }
        }
        cevap
    }

    /// `get_grouped_opcodes(n)`.
    fn gruplu_opkodlar(&mut self, n: usize) -> Vec<Vec<Op>> {
        let mut kodlar = self.opkodlar();
        if kodlar.is_empty() {
            kodlar = vec![(Etiket::Esit, 0, 1, 0, 1)];
        }
        if kodlar[0].0 == Etiket::Esit {
            let (e, i1, i2, j1, j2) = kodlar[0];
            kodlar[0] = (e, i1.max(i2.saturating_sub(n)), i2, j1.max(j2.saturating_sub(n)), j2);
        }
        let son = kodlar.len() - 1;
        if kodlar[son].0 == Etiket::Esit {
            let (e, i1, i2, j1, j2) = kodlar[son];
            kodlar[son] = (e, i1, i2.min(i1 + n), j1, j2.min(j1 + n));
        }
        let nn = n + n;
        let mut gruplar: Vec<Vec<Op>> = vec![];
        let mut grup: Vec<Op> = vec![];
        for (e, mut i1, i2, mut j1, j2) in kodlar {
            if e == Etiket::Esit && i2 - i1 > nn {
                grup.push((e, i1, i2.min(i1 + n), j1, j2.min(j1 + n)));
                gruplar.push(std::mem::take(&mut grup));
                i1 = i1.max(i2.saturating_sub(n));
                j1 = j1.max(j2.saturating_sub(n));
            }
            grup.push((e, i1, i2, j1, j2));
        }
        if !grup.is_empty() && !(grup.len() == 1 && grup[0].0 == Etiket::Esit) {
            gruplar.push(grup);
        }
        gruplar
    }
}

/// `_format_range_unified(start, stop)`.
fn aralik_biclemi(bas: usize, son: usize) -> String {
    let mut baslangic = bas as i64 + 1;
    let uzunluk = son - bas;
    if uzunluk == 1 {
        return baslangic.to_string();
    }
    if uzunluk == 0 {
        baslangic -= 1;
    }
    format!("{baslangic},{uzunluk}")
}

/// `difflib.unified_diff(a, b, fromfile=…, tofile=…, n=n)` (fromfiledate/tofiledate boş, lineterm `\n`); satırlar `"".join` için dönülür.
pub fn unified_diff(a: &[String], b: &[String], fromfile: &str, tofile: &str, n: usize) -> Vec<String> {
    let mut sonuc: Vec<String> = vec![];
    let mut basladi = false;
    for grup in Eslestirici::yeni(a, b).gruplu_opkodlar(n) {
        if !basladi {
            basladi = true;
            sonuc.push(format!("--- {fromfile}\n"));
            sonuc.push(format!("+++ {tofile}\n"));
        }
        let (ilk, son) = (grup[0], grup[grup.len() - 1]);
        sonuc.push(format!("@@ -{} +{} @@\n", aralik_biclemi(ilk.1, son.2), aralik_biclemi(ilk.3, son.4)));
        for (e, i1, i2, j1, j2) in grup {
            if e == Etiket::Esit {
                for satir in &a[i1..i2] {
                    sonuc.push(format!(" {satir}"));
                }
                continue;
            }
            if matches!(e, Etiket::Degis | Etiket::Sil) {
                for satir in &a[i1..i2] {
                    sonuc.push(format!("-{satir}"));
                }
            }
            if matches!(e, Etiket::Degis | Etiket::Ekle) {
                for satir in &b[j1..j2] {
                    sonuc.push(format!("+{satir}"));
                }
            }
        }
    }
    sonuc
}
