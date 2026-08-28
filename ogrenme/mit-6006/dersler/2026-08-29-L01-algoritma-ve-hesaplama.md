# L1 — Introduction (Algorithms and Computation)

> **Kaynak (BK-1, birebir):** MIT 6.006 S20, Ders 1 — anlatan Jason Ku. Not PDF'i: `static_resources/477c78e0...MIT6_006S20_lec1.pdf` · video transkripti: [Clippings/1. Algorithms and Computation.md](../../../Clippings/1.%20Algorithms%20and%20Computation.md) (YouTube ZA-tUyM_y7s). Lisans: CC BY-NC-SA 4.0, © MIT OCW — bu kayıt atıflı Türkçe uyarlamadır; başlık iskeleti ve örnekler dersin kendisidir, hiçbir konu eklenmemiş/çıkarılmamıştır. Zaman damgaları videoya işaret eder. Salih videoyu izledi (2026-08-29); bu kayıt okunur, bulanık blok numarası bildirilir.

## Kursun hedefi (0:56–2:59)
Dersin ilk cümlesi kursun tanımıdır: bu kurs **hesaplama problemlerini çözmeyi** VE **çözümünün doğru (correct) ve verimli (efficient) olduğunu başkalarına iletmeyi** öğretir. Ku'nun vurgusu: bu derste koddan çok **yazı** yazacaksın — hedef bilgisayarı değil, **insanları** ikna etmek. Kursun üç fiili: çöz (solve) · doğruluğu kanıtla (prove correctness) · verimliliği gerekçele (argue efficiency).

---

## Blok 1 — Problem nedir? (3:04–8:56)

**Tanım (dersin tanımı):** Bir hesaplama problemi, **girdiler kümesi** ile **çıktılar kümesi** arasında bir **ikili bağıntıdır (binary relation)**: her girdi için hangi çıktıların "doğru" sayıldığını söyler.

- Ku bunu tahtada **iki parçalı graf (bipartite graph)** olarak çizer: solda girdiler, sağda çıktılar, kenarlar "bu girdi için bu çıktı doğrudur" der (4:55).
- **Tek doğru çıktı şart değil:** "dizide 5 değerini içeren bir indeks ver" probleminde birden çok 5 olabilir — hepsi doğru (4:26).
- **Problemi kenar listesiyle vermeyiz** (girdi 1→çıktı 0, girdi 2→çıktı 3... diye saymak sonsuza dek sürer). Onun yerine **doğrulanabilir yüklem (predicate)** veririz: (girdi, çıktı) çifti verildiğinde çıktının doğru olup olmadığını KONTROL edebilen bir özellik (5:30). Örn.: "verdiğin indekse git, bak — 5 mi?"

**Matematik köşesi — sembollerle:** problem $P \subseteq I \times O$ bir bağıntıdır ($I$ girdi uzayı, $O$ çıktı uzayı); yüklem $v(i,o) \in \{\text{doğru},\text{yanlış}\}$, $(i,o) \in P$ testinin hesaplanabilir halidir.

**Dersin örneği — doğum günü eşleşmesi:** "Bu sınıfta aynı doğum gününe sahip bir çift var mı?"
- 365'ten fazla öğrenci varsa cevap otomatik EVET — **güvercin yuvası ilkesi (pigeonhole principle)**: $n$ nesne $k$ kutuya konur ve $n > k$ ise en az bir kutuda ≥2 nesne vardır (6:17–6:29).
- Soruyu ilginç tutmak için doğum ANI'na inceltilir (yıl + gün + saat): olası-değerler uzayı büyür (6:39).
- Ku'nun olasılık dipnotu (6:56): değer uzayı öğrenci sayısının **karesinden** büyükse çakışma olasılığı yarının altına düşer (klasik doğum günü problemi) — ama bu kurs olasılıkla uğraşmaz, **deterministik** algoritma ister (7:26).
- **Asıl mesaj (7:45–8:56):** bu kurs SABİT bir sınıf için değil, **keyfî büyüklükte girdi (arbitrarily sized input)** alan GENEL problemler için algoritma kurar: bu derslik, yan derslik, 1 milyar kullanıcılı veritabanı — aynı algoritma.

**Kontrol sorusu 1:** "Bir dizide 5'in İLK geçtiği indeksi döndür" problemi ile "5 içeren HERHANGİ bir indeksi döndür" problemi bağıntı olarak nasıl farklıdır? (cevap en altta)

---

## Blok 2 — Algoritma nedir? (9:05–15:08) ⭐ Karar 73 dayanağı

**Tanım (dersin tanımı, dk 9:40):** Algoritma, **sabit boyutlu bir makine/prosedürdür**: girdi verilirse bir çıktı üretir — ve ürettiği çıktı, problemin o girdi için doğru saydığı çıktılardan biri OLMALIDIR.

- **Algoritma bir fonksiyondur** (10:14): girdileri çıktılara götürür; her girdiye **tek** çıktı (deterministik). Problem çok-doğru-çıktılı bir bağıntı olabilir; algoritma o bağıntının içinden tek-değerli bir fonksiyon seçer.
- Öğrenci sorusuna netleştirme (14:11): buradaki "fonksiyon", fonksiyonel programlamadaki saf-fonksiyon değil, **matematiksel fonksiyon**: her girdiye tam bir çıktı.
- **Çözmek (solves)** ne demek (10:35): algoritma, tanım kümesindeki HER problem girdisi için doğru bir çıktı döndürüyorsa problemi çözer.
- Sezgi (14:46): algoritma bir **tarif (recipe)** — sırayla yapılacak işler dizisi; sonunda çıktı döner.

**Matematik köşesi:** problem $P \subseteq I \times O$ iken algoritma $f: I \to O$ fonksiyonudur; "çözer" $\iff \forall i \in I: (i, f(i)) \in P$.

**Dersin örneği — doğum günü algoritması** (öğrencinin önerisi, 11:01; dersin kendi sözcükleriyle):
1. Bir **kayıt (record)** tut (başta boş).
2. Öğrencileri bir sıraya koy, tek tek görüş (interview):
   - doğum günü kayıtta VARSA → çifti döndür, dur;
   - yoksa → (ad, doğum günü) kaydına ekle.
3. Son öğrenci de eşleşmeden biterse → `None` döndür.

Bu sözel betimleme düzeyi, problem setlerindeki teori sorularında beklenen düzeydir (13:24): "sınıftaki bir arkadaşın dinleyince gidip kodlayabilmeli" (25:03).

**⌥ Carvis notu (kurs içeriği değil):** dk 9:40–10:21 pasajı Karar 73'ün dayanağıdır — "Jarvis özünde bir makinedir": Jarvis de bu tanımın kapsamında girdi→çıktı dönüşümü yapan sabit boyutlu bir prosedürdür; deterministik tasarım ilkesi (CLAUDE.md §6) bu tanımın işletim halidir. Kanon: [core/varlik-felsefesi.md](../../../core/varlik-felsefesi.md) §1.

**Kontrol sorusu 2:** Doğum günü PROBLEMI ile doğum günü ALGORİTMASI arasındaki fark nedir — hangisi bağıntı, hangisi fonksiyon, "çözer" hükmü hangi niceleyiciyle kurulur?

---

## Blok 3 — Doğruluk: tümevarımla kanıt (15:15–25:26)

**Neden tümevarım (induction)?** Algoritma/program **sabit boyutludur**, girdi **keyfî büyüklükte** (16:27–16:58). Küçük girdi için tüm durumları tek tek denetleyebilirsin (case analysis — Ku ön sıradaki 4 öğrenci için bunu yapabileceğini söyler, 15:50); ama keyfî $n$ için kod **döngü ya da özyineleme (recursion)** içermek zorundadır → kanıt da **tümevarım** ister. Ku: özyinelemenin bilgisayar biliminde bu kadar merkezî olmasının nedeni budur (16:58); ayrık matematik ön-koşulu bundandır (17:06).

**Dersin kanıtı — doğum günü algoritmasının doğruluğu** (17:16–24:45), dersin kendi kurgusuyla:
- **Tümevarım değişkeni:** $k$ = görüşülmüş öğrenci sayısı (kayıttaki öğrenci sayısı).
- **Hipotez (19:16):** "İlk $k$ öğrenci bir eşleşme içeriyorsa, algoritma $k+1$. öğrenciyle görüşmeden ÖNCE bir eşleşme döndürmüştür."
- **Taban durumu (21:13):** $k = 0$ — öğrencinin bulduğu gibi 1 ya da 2 değil, **0**: ilk 0 öğrenci eşleşme içeremez; öncül yanlış olduğu için hipotez boş yere (vacuously) doğrudur (21:30).
- **Tümevarım adımı (21:56):** hipotez $k = k'$ için doğru olsun; $k = k'+1$'e bak. İki durum:
  1. İlk $k'$ zaten eşleşme içeriyordu → hipotez gereği algoritma ZATEN döndürmüş (22:35).
  2. İlk $k'$ eşleşme içermiyor → ilk $k'+1$ içinde eşleşme varsa, eşleşme $k'+1$. öğrenciyi İÇERMEK ZORUNDA (yoksa öncekilerde olurdu, 23:01). Algoritma tam da bunu doğrudan kontrol eder: $k'+1$. öğrencinin doğum günü kayıtta mı? Varsa döndürür; yoksa hipotez $k'+1$ için yeniden kurulmuş olur (24:26). ∎
- **Kapanış bağlantısı (20:10):** $k = n$ koy: eşleşme varsa son öğrenciden önce dönmüş; yoksa algoritma `None` döndürür — olması gerektiği gibi.
- Ku'nun tümevarım övgüsü (22:17): tümevarım problemi "her şeyi bir anda düşünmekten" kurtarır, her adımda küçük bir arayüze indirger.

**Matematik köşesi — kanıt iskeleti sembollerle:** $H(k)$: "ilk $k$'de eşleşme varsa algoritma $k+1$'den önce döndürür". Kanıt: $H(0)$ ∧ $\big(H(k') \Rightarrow H(k'+1)\big)$ $\Rightarrow \forall k \le n: H(k)$; doğruluk $H(n)$'den çıkar.

**Kontrol sorusu 3:** Taban durumu $k=0$'da hipotez neden "bedavaya" doğru? ("vacuous truth" kavramıyla söyle.)

---

## Blok 4 — Verimlilik: zamanı değil, işlemi say (25:34–36:48)

**Verimlilik nedir (25:59):** yalnız "ne kadar hızlı" değil — **başka yaklaşımlara GÖRE ne kadar hızlı**.

**Neden kronometre tutmayız (26:29–27:32):** ölçülen süre makineye bağlıdır (hesap makinesi vs IBM araştırma bilgisayarı — aynı kod, farklı süre). İstenen makineden bağımsız ölçü. **Fikir:** her temel işlemin sabit süre aldığını varsay; algoritmanın kaç **temel işlem (fundamental operation)** yaptığını **say**.

**Performans girdi boyutuna bağlıdır (29:10):** boyut genelde $n$ ile gösterilir ama dikkat (30:08): $n \times n$ dizi verdiysem girdinin boyutu $n^2$'dir; graf verdiysem boyut = düğüm sayısı + kenar sayısı (30:28).

**Asimptotik gösterim (30:50):** sabit çarpanları ve düşük dereceli terimleri at:
| Sembol | Anlam |
|---|---|
| $O(f)$ | üst sınır (upper bound) |
| $\Omega(f)$ | alt sınır (lower bound) |
| $\Theta(f)$ | sıkı sınır (iki yönden, tight) |

(Formal tanımlar yarınki recitation'da — R1; notta da işaret var: "∈, =, is, order" — $O(f)$ aslında bir fonksiyon KÜMESİdir, "=" alışkanlıkla yazılır.)

**Yaygın büyüme sınıfları** (dersin sırasıyla, 32:53–34:23): sabit $\Theta(1)$ · logaritmik $\Theta(\log n)$ · doğrusal $\Theta(n)$ · log-doğrusal $\Theta(n \log n)$ · karesel $\Theta(n^2)$ · polinom $\Theta(n^c)$ ($c$ sabit) · üstel $2^{\Theta(n^c)}$.
- **"Verimli" bu kursta = polinom zaman** (33:48). Büyük-veri derslerinde çıta daha sıkı olabilir; burada polinom yeter.
- Grafik sezgisi (34:35–36:48): $n$ eksenine çizersen log neredeyse sabit gibi yatar; üstel neredeyse dik duvar — "bunlar iyi, o kötü".

**Notların ölçek tablosu** (1 GHz, saniyede $10^9$ işlem varsayımıyla; $n = 1000$):
| sınıf | $\Theta(1)$ | $\Theta(\log n)$ | $\Theta(n)$ | $\Theta(n \log n)$ | $\Theta(n^2)$ | $\Theta(n^c)$ | $2^{\Theta(n)}$ |
|---|---|---|---|---|---|---|---|
| işlem | 1 | ≈10 | 1000 | ≈10.000 | 1.000.000 | $1000^c$ | $2^{1000} \approx 10^{301}$ |
| süre | 1 ns | 10 ns | 1 µs | 10 µs | 1 ms | $10^{3c-9}$ s | $10^{281}$ **binyıl** |

Elle doğrulama (formülün işletimi): $\log_2 1000 \approx 9{,}97 \approx 10$ ✓ · $n \log_2 n \approx 1000 \times 10 = 10.000$ ✓ · $10^{301}$ işlem ÷ $10^9$ işlem/s $= 10^{292}$ s ≈ $10^{281}$ binyıl ✓ (evrendeki parçacık sayısı tahmini $< 10^{100}$ — notların kendi kıyası).

**Kontrol sorusu 4:** $n$-düğümlü, $m$-kenarlı bir graf girdisinde "doğrusal zaman" ne demektir?

---

## Blok 5 — Hesaplama modeli: Word-RAM (36:50–42:26)

**Tanım:** hesaplama modeli (model of computation) = makinede hangi işlemlerin $O(1)$ (sabit) sürede yapılabildiğinin sözleşmesi. Bu kursun modeli: **Word-RAM**.

- **RAM** = random access memory: bellekte herhangi bir adrese **sabit sürede** erişilir (37:44). Bellek = bit dizisi; adresleme bit değil **bayt** (8 bit) üzerindendir (38:57).
- **Kelime (machine word):** $w$ bitlik blok — CPU'nun bellekten tek seferde alıp işleyebildiği parça (39:23). Bugünkü makinelerde $w = 64$.
- **CPU sabit sürede** şunları yapar ($O(1)$ adet kelime üstünde): tamsayı aritmetiği (`+ - * // %`) · mantıksal karşılaştırmalar (`&& || ! == < > <= >=`) · (bitsel işlemler — bu kursta az kullanılır) · adresi verilen kelimeyi **oku/yaz**.
- **Adres sığmalıdır:** $w \ge \log_2 n$ (en büyük bellek adresini tutacak kadar bit). Dersin tarihçesi: 32 bit → $2^{32}$ adres ≈ **4 GB** sınırı (Ku'nun gençliğindeki disk-bölümleme derdi, 39:59); 64 bit → ~16-20 **exabyte** (notta ~16 EB; videoda "~20 EB — Google'ın dünyadaki tüm verisi ~10 EB" kıyası, 41:18).
- **Python bu model değildir** (42:32'deki veri yapısı geçişinde + notta): Python, Word-RAM üzerine kurulmuş daha karmaşık bir modeldir — `list`, `dict`, `set` ile makine arasında maliyeti görünmez kod katmanı vardır (44:04). Kurs bu maliyeti görünür kılacak.

**Elle işletme (adres hesabı):** $w=32$: $2^{32}$ bayt $= 4 \times 2^{30}$ bayt $= 4$ GiB ✓ · $w=64$: $2^{64}$ bayt $= 16 \times 2^{60}$ bayt $= 16$ EiB ✓.

**Kontrol sorusu 5:** Word-RAM'de $n$ kelimelik bir bloğun TAMAMINI okumak neden $\Theta(n)$'dir, $O(1)$ değil?

---

## Blok 6 — Veri yapısı + ilk örnek: StaticArray (42:32–44:24)

**Tanım:** veri yapısı (data structure) = sabit-olmayan miktarda veriyi saklayıp üzerinde bir **işlem kümesi** sunan düzen. İşlemler topluluğuna **arayüz (interface)** denir. Kursun iki ana arayüz ailesi:
- **Dizi/Sequence:** öğelere DIŞSAL sıra (birinci, sonuncu, $n$'inci) — sıra benim dayattığım.
- **Küme/Set:** öğelere İÇSEL sıra (anahtar/keye göre sorgu) — sıra verinin kendinden.

Aynı arayüz farklı veri yapılarıyla FARKLI performansta gerçeklenebilir — kursun ana teması bu.

**İlk veri yapısı — Static Array** (sabit genişlikte hücreler, sabit uzunluk):
| İşlem | Maliyet |
|---|---|
| `StaticArray(n)` — $n$ hücre ayır, 0'la | $\Theta(n)$ |
| `get_at(i)` — $i$. hücredeki kelimeyi oku | $\Theta(1)$ |
| `set_at(i, x)` — $i$. hücreye $x$ yaz | $\Theta(1)$ |

$\Theta(1)$ erişimin sebebi Word-RAM sözleşmesidir: adres = taban + $i$ (aritmetik $O(1)$) + adresli okuma ($O(1)$). Hücredeki kelime daha büyük bir nesnenin ADRESİNİ tutabilir. Python karşılığı: `tuple` + `set_at` ≈ statik dizi; `list` **dinamik dizidir** (L2'nin konusu).

---

## Blok 7 — birthday_match kodu ve koşum analizi (notların 4. sayfası + 12:01)

Dersin kendi kodu (satır satır maliyetiyle):

```python
def birthday_match(students):
    '''
    Find a pair of students with the same birthday
    Input:  tuple of student (name, bday) tuples
    Output: tuple of student names or None
    '''
    n = len(students)                      # O(1)
    record = StaticArray(n)                # O(n)
    for k in range(n):                     # n kez
        (name1, bday1) = students[k]       # O(1)
        # bday1 kayıtta mı?
        for i in range(k):                 # k kez
            (name2, bday2) = record.get_at(i)  # O(1)
            if bday1 == bday2:             # O(1)
                return (name1, name2)      # O(1)
        record.set_at(k, (name1, bday1))   # O(1)
    return None                            # O(1)
```

**Koşum süresi (running time) — dersin formülü, elle işletilmiş:**
$$T(n) = O(n) + \sum_{k=0}^{n-1}\big(O(1) + k \cdot O(1)\big)$$
Toplamı aç: $\sum_{k=0}^{n-1} 1 = n$ ve $\sum_{k=0}^{n-1} k = \frac{n(n-1)}{2}$ (aritmetik seri: ilk terim 0, son terim $n-1$, terim sayısı $n$ → toplam $= n \cdot \frac{0+(n-1)}{2}$). Yani
$$T(n) = O(n) + O(n) + O\!\left(\tfrac{n(n-1)}{2}\right) = O(n^2).$$
Sayısal doğrulama ($n=4$, en kötü durum — hiç eşleşme yok): iç döngü karşılaştırmaları $0+1+2+3 = 6 = \frac{4 \cdot 3}{2}$ ✓.

**Dersin kapanış sorusu:** karesel = polinom = bu kursa göre "verimli". Ama daha iyisi olur mu? **Evet — kayıt için farklı bir veri yapısı kullanarak** (notların son cümlesi; hash table L4'te bunu $O(n)$ beklenen zamana indirecek — bu ileri-bakış notta "Efficient? Use different data structure for record!" satırıdır).

**Kontrol sorusu 6:** Bu algoritmada $\Theta(n^2)$'yi üreten mekanizma tam olarak hangi satırda ve neden?

---

## Blok 8 — Kurs haritası: bir algoritma problemi nasıl çözülür (44:35–45:28)

Dersin verdiği iki strateji (notların son bölümü — bu tablo kursun omurga haritasıdır):

1. **Bildiğin bir probleme indirge (reduce)** — hazır veri yapısı/algoritma kullan:

| Arama problemi (veri yapıları) | Sıralama algoritmaları | En kısa yol algoritmaları |
|---|---|---|
| Static Array (L01) | Insertion Sort (L03) | Breadth-First Search (L09) |
| Linked List (L02) | Selection Sort (L03) | DAG Relaxation (L11) |
| Dynamic Array (L02) | Merge Sort (L03) | · Depth-First Search (L10) |
| Sorted Array (L03) | Counting Sort (L05) | · Topological Sort (L10) |
| Direct-Access Array (L04) | Radix Sort (L05) | Bellman-Ford (L12) |
| Hash Table (L04) | AVL Sort (L07) | Dijkstra (L13) |
| Balanced Binary Tree (L06-07) | Heap Sort (L08) | Johnson (L14) |
| Binary Heap (L08) | | Floyd-Warshall (L18) |

2. **Kendi (özyinelemeli) algoritmanı tasarla** — paradigmalar: Brute Force · Decrease and Conquer · Divide and Conquer · **Dynamic Programming (L15-L19)** · Greedy/Incremental.

**Kursun sınav yapısı (45:15):** Quiz 1 = ilk 8 ders (veri yapıları + sıralama) · Quiz 2 = en kısa yollar/graflar · Quiz 3 = dinamik programlama.

**⌥ Carvis notu:** "önce indirge, yoksa tasarla" stratejisi kanondaki "hazırı temel al" ilkesinin (CLAUDE.md §6) kursun içindeki karşılığıdır.

---

## Kontrol sorularının cevapları
1. "İLK indeks" bağıntısında her girdinin TEK doğru çıktısı vardır (bağıntı zaten fonksiyondur); "herhangi bir indeks"te bir girdiye birden çok doğru çıktı düşebilir — algoritma yine tek çıktı seçmek zorundadır.
2. Problem = $P \subseteq I \times O$ bağıntısı (çok-doğru-çıktı serbest); algoritma = $f: I \to O$ fonksiyonu; çözer $\iff \forall i: (i, f(i)) \in P$ — niceleyici HER girdi üzerinde evrensel.
3. Hipotez koşullu önermedir: "ilk $k$'de eşleşme VARSA...". $k=0$'da öncül yanlıştır (0 kişide eşleşme olamaz); öncülü yanlış koşullu önerme mantıkça doğrudur (vacuous truth).
4. Girdi boyutu $n + m$ olduğundan doğrusal zaman $\Theta(n+m)$ demektir — yalnız $\Theta(n)$ değil.
5. CPU tek adımda yalnız $O(1)$ kelimeye dokunabilir; $n$ kelimeye dokunmak en az $n$ ayrı adım ister.
6. İç döngü (`for i in range(k)`): $k$. öğrenci için kayıttaki $k$ girişin HEPSİYLE karşılaştırma yapılır; toplam $\sum k = n(n-1)/2$ karşılaştırma → $\Theta(n^2)$. Yapıyı değiştirmeden (lineer taramalı kayıt) bundan kaçış yok.

## Durum
- Bulanık blok bildirimi bekleniyor (numarayla). Sonraki adım: R1 (asimptotik gösterimin formal tanımları — dersin kendisi yarınki recitation'a devretti) ∨ L2 (Data Structures, Salih video izleyince).
- İlerleme tablosu: [ilerleme.md](../ilerleme.md)
