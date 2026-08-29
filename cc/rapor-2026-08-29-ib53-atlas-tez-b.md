# ATLAS TEZ RAPORU — Aile B: Görsel-Temsil Kanıtı (3B görselleştirme yatırımı)

## KÜNYE

| Alan | Değer |
|---|---|
| Rapor kodu | IB-53 / Aile B (tez ayağı) |
| Ajan | ATLAS (research-agent), bağımsız koşum |
| Tarih (AS-OF) | **2026-08-29** — aşağıdaki TÜM iddialar bu tarihte canlı kaynaktan çekilmiştir |
| Araştırma sorusu | ~500-600 düğümlük bir bilgi-deposu graf görüntüleme katmanı için 3B görselleştirmeye yatırım kanıtla destekleniyor mu? |
| Alt-sorular | ① 2B↔3B görev-performans deneyleri ② düğüm-sayısı okunabilirlik eşikleri ③ focus+context / odak-panosu ölçülmüş kazancı |
| Yöntem | WebSearch + WebFetch; PDF'ler yerel diske indirilip `pdftotext` ile ham metne çevrildi, sayılar satır düzeyinde okundu (özet modeline güvenilmedi) |
| Bulunan birincil deney | **15** (11'i kaynak-doğrulanmış sayı ile; 4'ü yalnız abstract/aktarım — aşağıda bayraklı) |
| Karar | **YOK** — bu rapor karar vermez, yalnız kanıt serer (görev emri gereği) |

### Erişim bayrakları (dürüstlük kaydı)

| Kaynak | Durum |
|---|---|
| Ware & Franck 1996 (TOG) | ✅ TAM METİN okundu (Kent State kopyası, PDF sayfa görüntüsü) |
| Ware & Mitchell 2008 (TAP) | ⚠️ **PAYWALL** (ACM DL). Yalnız UNH kurum-deposundaki ABSTRACT'a dayanıldı; deneyin n'i, koşul tablosu görülmedi |
| Greffard vd. 2011 (GD) | ⚠️ **PAYWALL** (Springer 303→IdP); ResearchGate PDF **403**. Yalnız yayıncı/arama-motoru abstract düzeyi; sayılar ikinci-el |
| Ghoniem vd. 2005 (Inf.Vis.) | ⚠️ **PAYWALL** (SAGE, £29/24sa). Abstract birebir alındı; n ve graf boyutları GÖRÜLMEDİ |
| Kotlarek vd. 2020 | ✅ TAM METİN (arXiv PDF → pdftotext), sayılar satır düzeyinde doğrulandı |
| McGuffin vd. 2022 | ⚠️ Yarı-doğrulanmış: arXiv PDF 10 MB sınırını aştı; **ar5iv HTML** üzerinden okundu, satır düzeyinde kendi gözümle doğrulamadım |
| Feyer vd. 2023 | ✅ TAM METİN (arXiv PDF → pdftotext); ilk arama-özeti sayıları YANLIŞ eşleştirmişti, ham metinden düzeltildi |
| Yoghourdjian vd. 2018 + 2020 | ✅ TAM METİN (arXiv PDF → pdftotext) |
| Moscovich vd. 2009 (CHI) | ✅ TAM METİN (aviz.fr kopyası). HAL aynaları (hal.inria.fr, inria.hal.science) **Anubis ile 403** |
| Nekrasovski vd. 2006 (CHI) | ✅ TAM METİN (UBC teknik rapor kopyası) |
| Okoe vd. 2018/19 (TVCG) | ✅ TAM METİN (City, Open Access) |
| Cockburn vd. 2008 (CSUR) | ✅ TAM METİN (Georgia Tech kopyası) — İKİNCİL derleme olarak kullanıldı |
| van Ham & Perer 2009 (TVCG) | ✅ TAM METİN — ve **kontrollü deney İÇERMİYOR** (aşağıda ③) |

---

## ① 2B ↔ 3B DÜĞÜM-BAĞ GÖRSELLEŞTİRMESİ: BİRİNCİL DENEYLER

### Kanıt tablosu

| # | Çalışma | Yıl | n | Graf boyutu | Koşullar | Ölçülen | Sonuç (rakam) | URL |
|---|---|---|---|---|---|---|---|---|
| 1a | Ware & Franck, ACM TOG 15(2):121-140, Deney 1a | 1996 | 11 denek (8'i benzer donanım deneyimli) | 24 / 51 / 78 / 105 / 132 düğüm (yay = 4/3·n) | 2B ortografik izdüşüm **vs** stereo + kafa-izlemeli perspektif | Hata oranı, süre | Hata 2B ≈ %12,5 (24 düğüm) → ≈ %40,5 (132); 3B ≈ %4 → ≈ %13,5. ANOVA F(1,100)=276,8, p<0,01. **Süre**: görüş kipinin etkisi YOK; yalnız düğüm sayısı F(4,100)=10,14, p<0,01 | [ware96.pdf](https://www.cs.kent.edu/~jmaletic/softvis/papers/ware96.pdf) · [DOI](https://dl.acm.org/doi/10.1145/234972.234975) |
| 1b | Ware & Franck, Deney 1b | 1996 | 11 katılımcı (6'sı deneyimli) | 21→291 düğüm (koşula göre farklı aralık) | 2B · yalnız stereo · yalnız kafa-izleme · stereo+kafa-izleme | Hata = C·N doğrusal uyum (varyansın %95'i) | Katsayılar: 2B 0,369 · stereo 0,232 · kafa-izleme 0,167 · stereo+kafa 0,123 → aynı hata oranında **anlaşılabilir graf 3,0×**; yalnız stereo 1,6×; yalnız kafa-izleme 2,2×. İkili ANOVA'ların hepsi p<0,01 | aynı PDF, s.132-133 |
| 2 | Ware & Franck, Deney 2 | 1996 | 11 denek | **sabit** 75 düğüm / 100 yay, koşul başına 18 deneme | 9 koşul: 2B · **statik perspektif** · stereo · pasif dönüş (20°/sn) · stereo+pasif · el-güdümlü · stereo+el · kafa-izleme · stereo+kafa | Hata, süre | Hata %26 (2B) → %6,1 (stereo+el-güdümlü). **"İki 2B koşulu diğer tüm koşullardan anlamlı ölçüde yüksek hata verdi, ama birbirlerinden anlamlı farklılaşmadılar"** — iki 2B koşulu = 2B ortografik + STATİK PERSPEKTİF. Yalnız-hareket ortalaması %11,4 vs yalnız-stereo %15,4. El ve kafa hareketi koşulları diğer tüm koşullardan YAVAŞ | aynı PDF, s.135-137 |
| 3 | Ware & Mitchell, ACM TAP 5(1) | 2008 | ⚠️ bilinmiyor (paywall) | 333 ve 1000 düğüm | 2B vs hareket+stereo 3B | Hata oranı | Hareket+stereo ile eğitimsiz gözlemciler 333 düğümde <%10 hata; eğitimli gözlemciler 1000 düğümde <%10 hata — 2B'ye göre "bir büyüklük mertebesi" artış | [UNH deposu (abstract)](https://scholars.unh.edu/ccom/467/) · [DOI paywall](https://dl.acm.org/doi/10.1145/1279640.1279642) |
| 4 | Greffard, Picarougne, Kuntz, GD 2011, LNCS 7034:215-225 | 2011 | 35 katılımcı | "çeşitli karmaşıklıkta" graflar (⚠️ tam boyut görülmedi) | **2B · 3B monoskopik perspektif · 3B stereoskopik** | Doğruluk, tepki süresi | Stereoskopi vakaların büyük çoğunluğunda 3B perspektifi geçiyor; **2B'ye karşı tepki süresi 2B lehine anlamlı ölçüde düşük**; stereo yalnız çok-kümeli + yüksek örtüşmeli graflarda 2B'yi geçiyor, basit yapılarda 2B daha verimli | [Springer (paywall)](https://link.springer.com/chapter/10.1007/978-3-642-25878-7_21) |
| 5 | Kotlarek vd., PacificVis 2020 | 2020 | 20 (11K/9E, ort. yaş 24,35) | karate 34/78 (eğitim), lesmis 77/254, netsci **379/914**, power 4.941/6.594 | **2B masaüstü (fare/klavye) vs 3B VR (HTC Vive Pro)** | Doğruluk + süre, 3 görev | **Yol görevi doğruluk: 3B 0,950 (SD 0,185) > 2B 0,806 (SD 0,387), t(59)=2,820, p=0,0065, d=0,478.** Yol görevi SÜRE: 2B 49,26s < 3B 67,81s (anlamlı). Bellek görevi süre: 2B 31,92s < 3B 50,70s, t(59)=5,847, p=2,3·10⁻⁷. Bellek doğruluk: 2B 0,951 > 3B 0,923, t(59)=4,2086, p=8,88·10⁻⁵. Katılımcıların %85'i 3B'yi TERCİH etti | [arXiv 2001.06462](https://arxiv.org/abs/2001.06462) |
| 6 | McGuffin, Servera, Forest — Çalışma 1 | 2022 | 34 (24E/10K, 19-45 yaş) | 70 düğüm / 140 kenar (Watts-Strogatz, %20 yeniden-bağlama) | **Hepsi VR içinde**: VR2D (kenar-yönlendirmeli 2B) · VR2DHilite · VR3D · VR3DHilite | Hata, süre | 3B'de hata 2B'den düşük, eşli t-testi **p<0,0000005**; fare ile kenar-vurgulamanın etkisi zayıf (p<0,09) | [arXiv 2207.11586](https://arxiv.org/abs/2207.11586) |
| 7 | McGuffin vd. — Çalışma 2 | 2022 | 12 | aynı sınıf | VR'da sanal 3B vs 3B-basılmış fiziksel ağ (HoloLens) | Hata | **Fark bulunamadı** | aynı |
| 8 | Feyer vd., IEEE TVCG / VIS 2023 | 2023 | **22** (28 alındı, 6 elendi) | katman başına 30 düğüm + 45 kenar; 3 katman ("küçük", ~90 düğüm) veya 7 katman ("büyük", ~210 düğüm) | **Hepsi VR içinde**: 2B (tek düzlem) · 2.5D (yığılı düzlem) · 3B (yarıküre) | 6 görev × hata + süre + fiziksel hareket | **"Net bir genel kazanan bulamadık."** T1 en-kısa-yol: hata en yüksek 2B'de (0,41 küçük / 0,32 büyük), en düşük 2.5D (0,18) ve büyükte 3B (0,18). T3 örüntü/büyük: hata en düşük **2B 0,18**, en yüksek **3B 0,45**; süre en düşük 2B 120,45s. T2 büyük: hata en düşük 2B 0,18, süre en düşük 2B 64,94s vs 2.5D 138,9s. T5 büyük: hata 2B/2.5D 0,09, **3B 0,36**. Yazarların özeti: 6 görevin 3'ü 2.5D veya 3B'de daha iyi | [arXiv 2307.10674](https://arxiv.org/abs/2307.10674) · [DOI](https://dl.acm.org/doi/abs/10.1109/TVCG.2023.3327402) |
| 9 | Zhang vd., GD 2025 (LIPIcs 357, art.11) | 2025 | 18 | ⚠️ bildirilmemiş (özet düzeyi) | Yalnız stereoskopik 3B VR + göz izleme — **2B karşılaştırma kolu YOK** | Bakış örüntüsü ↔ performans | 2B/3B kıyası vermiyor; alanın 2025 tarihli en yeni işi bile yalnız-VR kurulumda | [Dagstuhl LIPIcs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.GD.2025.11) |

### Ham alıntılar (kaynak + bölüm beyanlı)

> "The two 2D conditions gave significantly higher error rates than all other conditions although they did not differ significantly from each other."
> — Ware & Franck 1996, **gövde**, Bölüm 4.3 "Results from Experiment 2", s.136. (Buradaki iki 2B koşulu: (1) 2B ortografik ve (2) statik perspektif.)

> "Our results suggest that this effort makes sense only if real-time rotation and/or stereo viewing is included in the data presentation. A static perspective image may add little in comparison with a 2D diagram and adding real-time rotation is more important than adding stereo."
> — Ware & Franck 1996, **gövde**, Bölüm 5 "Conclusion", s.138.

> "if the selection of objects is important, then automatic rotation is not desirable because selecting moving objects is difficult."
> — Ware & Franck 1996, **gövde**, Bölüm 5 "Conclusion", s.138.

> "we found no clear overall winner"
> — Feyer vd. 2023, **abstract**.

> "It would be interesting to conduct a similar experiment on a 2D screen to investigate the ..."
> — Feyer vd. 2023, **gövde**, Bölüm 6 (yazarların kendi sınırlılık notu: deney VR'da koşuldu, düz ekran denenmedi).

### Bu alt-sorunun kanıt okuması (yorum değil, kanıtın söylediği)

- **3B'nin ölçülmüş kazancı, koşulsuz "3B" değil, DERİNLİK İPUCUNA bağlı.** Ware & Franck'te kazancı üreten şey stereo (1,6×) ve gerçek-zamanlı hareket/parallaks (2,2×); ikisi birlikte 3,0×. Statik perspektif (yani düz ekranda döndürmesiz 3B çizim) 2B'den istatistiksel olarak AYRIŞMIYOR.
- **Otomatik dönüş (pasif rotasyon) düz masaüstünde donanımsız elde edilebilir** ve Ware & Franck Deney 2'de yalnız-hareket koşullarının ortalama hatası %11,4 (2B %26'ya karşı); yazarlar "hareketin ÜRETİM YÖNTEMİ önemli değil" diyor. Ancak aynı bölümde: nesne seçimi önemliyse otomatik dönüş İSTENMEZ (hareketli nesne tıklamak zor) — tıklanabilir bilgi-deposu arayüzü için doğrudan çatışma.
- **Süre boyutunda 3B'nin ölçülmüş kazancı yok.** Ware & Franck 1a: görüş kipinin süreye etkisi yok. Kotlarek 2020: 3B her üç görevde de daha YAVAŞ. Greffard 2011: tepki süresi 2B lehine anlamlı. Feyer 2023: büyük ağlarda en düşük süre çoğunlukla 2B'de.
- **3B lehine en güçlü modern bulgular VR/stereo içinde ve YOL-İZLEME görevinde toplanıyor** (Kotlarek yol doğruluğu 0,950 vs 0,806; McGuffin p<0,0000005). McGuffin'de 2B kolu da VR içinde gösterildi — yani "masaüstü 2B" ile kıyas DEĞİL.
- **Görev bağımlılığı ölçülmüş bir olgu, retorik değil:** Feyer 2023'te aynı deneyde 3B kimi görevde en düşük (T1 büyük: 0,18), kimi görevde en yüksek (T3 büyük: 0,45; T5 büyük: 0,36) hatayı veriyor.
- **Iraksama bayrağı:** Ware hattı (1996, 2008) 3B'yi güçlü destekliyor; Kotlarek/Feyer hattı (2020, 2023) karışık/negatif. Ortalama ALINMADI. Muhtemel ayrıştırıcı değişkenler: (i) görev türü (2 uzunluklu yol tespiti ↔ karışık analitik görevler), (ii) 2B kolunun düzeni (Ware'de 2B kolu, 3B düzenin Z ekseni SİLİNMİŞ hâliydi — yani 2B'ye özel bir yerleşim algoritması KULLANILMADI; bu, 2B aleyhine yapısal bir dezavantaj), (iii) donanım kuşağı.
- (ii) maddesi doğrudan kaynaktan: "the 3D graph was projected onto a 2D plane using an orthographic (parallel) projection by removing Z axis information" — Ware & Franck 1996, **gövde**, Bölüm 2.2 / 3.1 koşul tanımı. Modern 2B karşılaştırmaları (McGuffin) 2B kolunda kenar-yönlendirme kullanıyor ve yine de 3B lehine sonuç veriyor.

---

## ② DÜĞÜM-SAYISI OKUNABİLİRLİK EŞİKLERİ

### Kanıt tablosu

| # | Çalışma | Yıl | n | Ölçülen | Sonuç (rakam) | URL |
|---|---|---|---|---|---|---|
| 10 | Yoghourdjian, Yang, Dwyer, Marriott, Wybrow vd., IEEE TVCG 27(2):1677-1687 (VIS 2020) | 2020/21 | **22 katılımcı**, 42 uyaran | En-kısa-yol bulma; doğruluk + tepki süresi + **EEG, göz-bebeği, kalp hızı değişkenliği** | Graflar **25-175 düğüm**, 3 yoğunluk düzeyi. **Yoğunluk 6 ve ≥50 düğümde katılımcılar denemelerin yarısından fazlasında doğru cevap VEREMEDİ; yoğunluk 2 ve >100 düğümde de aynı.** Bilişsel yük belirli bir zorluğa kadar artıyor, sonra DÜŞÜYOR (katılımcılar pes ediyor) | [arXiv 2008.07944](https://arxiv.org/abs/2008.07944) |
| 11 | Yoghourdjian, Archambault, Diehl, Dwyer, Klein, Purchase, Wu — Visual Informatics 2(4):264-282 (tarama) | 2018 | **152 deneysel çalışma** taraması | Kullanılan graf boyutlarının dağılımı | Medyan **49,5 düğüm** / 73 kenar (alt çeyrek 18,5; üst çeyrek 116,5). Çalışmaların **121/152'si (%80) ≤100 düğüm**; yalnız 56/152 (%37) >100 düğüm; 15 çalışma >1000, 9 çalışma >500 düğüm. >500 düğümlü 24 çalışmanın **20'si (%83) grafın PARÇASINI çıkaran etkileşimli araçları** değerlendiriyor. Histogram tepe noktaları 20, 50, 100 (50 → 18 çalışma; 20 → 16; 100 → 14) ve yazarlara göre bu yuvarlak sayılar **ampirik olarak belirlenmemiş, keyfî** | [arXiv 1809.00270](https://arxiv.org/abs/1809.00270) · [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2468502X18300585) |
| 12 | Ghoniem, Fekete, Castagliola — Information Visualization 4(2):114-135 | 2005 | ⚠️ paywall (n görülmedi) | 7 genel görevde okunabilirlik: düğüm-bağ ↔ matris | **"20 düğümden büyük graflarda matris temsili çoğu görevde düğüm-bağ diyagramını geçiyor; yalnız yol bulma tutarlı biçimde düğüm-bağ lehine"** | [SAGE (paywall)](https://journals.sagepub.com/doi/10.1057/palgrave.ivs.9500092) |
| 13 | Okoe, Jianu, Kobourov — IEEE TVCG 25(10):2940-2952 | 2018/19 | **864 katılımcı** (kitle-kaynak), 14 görev | Düğüm-bağ ↔ matris, doğruluk | Ağlar: **258 düğüm/1090 kenar** ve **332 düğüm/2126 kenar**. Topoloji sorularında düğüm-bağ üstün: iki veri kümesindeki 10 topoloji görevinin 5'inde düğüm-bağ daha doğru, 3'ünde daha az doğru. Küme/grup görevlerinin 4'ünün 2'sinde matris üstün | [City Open Access PDF](https://openaccess.city.ac.uk/id/eprint/20159/1/node-link-adjacency%20%283%29.pdf) · [kayıt](https://openaccess.city.ac.uk/20159/) |

### Ham alıntılar

> "Our results show that people have significant difficulty finding the shortest path in high density node-link diagrams with more than 50 nodes and even low density graphs with more than 100 nodes."
> — Yoghourdjian vd. 2020, **abstract**.

> "For small-world graphs with 50 or more nodes and a density (ratio of edges to nodes) of 6, participants were unable to correctly answer in more than half of the trials. This was also the case for graphs with a density of 2 and more than 100 nodes."
> — Yoghourdjian vd. 2020, **gövde**, Bölüm 1 "Contributions", madde 1.

> "three quarters of studies use graphs with 100 nodes and 200 edges or less and, the remaining studies test interactive techniques, such that only a small portion of the graph is shown on the screen at a time"
> — Yoghourdjian vd. 2018, **abstract**.

> "the limits of scalability of the node-link network visualisation paradigm are rarely addressed directly. Rather, there seem to be tacit assumptions (or possibly unreported pilot findings) about what size node-link diagrams are usable"
> — Yoghourdjian vd. 2018, **abstract**.

> "biologists reporting on the interactions of particular proteins may be better off showing a focused neighbourhood around those specific proteins rather than providing a hairball."
> — Yoghourdjian vd. 2018, **gövde**, Bölüm VII.B "Discussion".

> "when graphs are bigger than twenty vertices, the matrix-based visualization outperforms node-link diagrams on most tasks. Only path finding is consistently in favor of node-link diagrams throughout the evaluation."
> — Ghoniem vd. 2005, **abstract** (tam metne erişilemedi).

### Bu alt-sorunun kanıt okuması

- **Doğrudan ölçülmüş tek eşik çalışması Yoghourdjian 2020'dir** ve ölçüm aralığı **25-175 düğümde biter**. 500-600 düğüm bu aralığın tamamen DIŞINDA; o boyutta topoloji görevi için yayımlanmış birincil ölçüm bulunamadı (→ "bulunamadı", meşru sonuç).
- Ölçülen kırılma noktaları: yoğun graflarda >50 düğüm, seyrek graflarda >100 düğüm — her ikisinde de başarı oranı %50'nin altına düşüyor.
- **Eşikler mutlak değil, ETKİLEŞİME bağlı.** Ghoniem'in "20 düğüm" eşiği (2005, statik) ile Okoe'nin 258-332 düğümde düğüm-bağ lehine sonucu (2018, seçim/vurgulama/yakınlaştırma/düğüm sürükleme içeren etkileşimli arayüz) IRAKSIYOR. Ortalama alınmadı. Tarama verisi bu ıraksamayı destekliyor: büyük graf kullanan çalışmaların %83'ü zaten grafın parçasını çıkaran etkileşimli araçlar.
- **Alanın kendi itirafı:** 152 çalışmanın literatüründe kullanılan 20/50/100 düğüm değerleri ampirik değil keyfî; tam-graf okunabilirlik eşiği "doğrudan nadiren ele alınıyor".

---

## ③ FOCUS+CONTEXT / ODAK-PANOSU (KÜÇÜK ALT-GRAF, 1-2 SIÇRAMA) ÖLÇÜLMÜŞ KAZANCI

### Kanıt tablosu

| # | Çalışma | Yıl | n | Graf boyutu | Koşullar | Ölçülen | Sonuç (rakam) | URL |
|---|---|---|---|---|---|---|---|---|
| 14 | Moscovich, Chevalier, Henry, Pietriga, Fekete — CHI 2009:2319-2328 | 2009 | **12** yetişkin gönüllü | **1000 düğüm/1485 kenar** (seyrek) ve **1000/2488** (yoğun), Barabási-Albert | Pan&Zoom (PZ) · Bird's Eye View (BEV = genel-bakış+ayrıntı) · Link Sliding (LS) · **Bring&Go (B&G = odak düğümün 1-sıçrama komşularını yanına getirir)** | Süre + hata, 3 alt-görev | **Komşular görevi süre: PZ 27,2s (SD 0,8) · BEV 21s (0,7) · LS 24s (0,8) · B&G 8,5s (0,2)**; F(3,33)=69,811, p<0,0001 → B&G, PZ'den **~3,2× hızlı**. Yoğun grafta hata: BEV %42 · LS %33 · PZ %25 · **B&G %10**. Yeniden-ziyaret görevi: PZ 15,6s · BEV 13,3s · LS 12s · **B&G 7,2s**, F(3,33)=35,453, p<0,0001. Bağ-takip görevi: PZ 7s · BEV 5,6s · LS 4,9s · **B&G 4,2s**, F(3,33)=12,521, p<0,0001 | [aviz.fr PDF](https://www.aviz.fr/wiki/uploads/Research/topologyawarenav-CHI2009.pdf) · [DOI](https://dl.acm.org/doi/10.1145/1518701.1519056) |
| 15 | Nekrasovski, Bodnar, McGrenere, Guimbretière, Munzner — CHI 2006 | 2006 | **40 denek** | **5.918 düğümlü** ikili ağaç (evrimsel veri) | Pan&Zoom (PZN) · Rubber Sheet Navigation (RSN = dikdörtgensel focus+context bozunum) × genel-bakış var/yok | Süre, zihinsel çaba, gezinme eylemi | **PZN, RSN'den anlamlı ölçüde HIZLI ve daha az zihinsel çaba: F(1,36)=13,477, p<0,001, η²=0,272.** Genel-bakışın süreye etkisi YOK: F(1,36)=0,611, p>0,4 (yine de kullanıcılar yararlı ALGILADI) | [UBC PDF](https://www.cs.ubc.ca/labs/imager/tr/2006/Nekrasovski2006CHI/Nekrasovski2006CHI.pdf) · [DOI](https://dl.acm.org/doi/10.1145/1124772.1124775) |
| — | Cockburn, Karlson, Bederson — ACM Computing Surveys 41(1) art.2 (**İKİNCİL derleme**) | 2008 | — | — | O+D / zoom / F+C / işaret-tabanlı | Literatür değerlendirmesi | Bozunum-tabanlı F+C için ampirik destek zayıf (aşağıda birebir alıntı). Schaffer vd. 1996'yı ilk üst-düzey F+C deneyi olarak aktarıyor: hiyerarşik kümelenmiş ağ diyagramlarında fisheye daha hızlı ve daha az gezinme eylemi — **ama çoklu-odak karışıklığı (confound) var** | [Georgia Tech PDF](https://faculty.cc.gatech.edu/~stasko/7450/Papers/cockburn-surveys08.pdf) · [DOI](https://dl.acm.org/doi/10.1145/1456650.1456652) |
| — | van Ham & Perer, IEEE TVCG 15(6) — "Search, Show Context, Expand on Demand" (degree-of-interest alt-graf) | 2009 | **YOK** | 15M+ belge / 3M+ atıf ağı | — | — | **Kontrollü deney YOK.** Değerlendirme yalnız hukuk atıf ağı üzerinde VAKA ÇALIŞMASI ("4 EVALUATION: LEGAL CITATION NETWORK"); katılımcı sayısı, süre veya doğruluk ölçümü bildirilmemiş. Odak-alt-graf yaklaşımının kanonik makalesi için **ölçülmüş kazanç bulunamadı** | [aviz.fr PDF](https://aviz.fr/wiki/uploads/Teaching2014/SearchShowContext.pdf) · [DOI](https://dl.acm.org/doi/10.1109/TVCG.2009.108) |

### Ham alıntılar

> "Post-hoc pairwise mean comparisons showed that B&G was significantly faster than the three other techniques and that BEV performed better than PZ. Mean times were: PZ 27.2 sec (SD=0.8), BEV 21 sec (SD=0.7), LS 24 sec (SD=0.8) and B&G 8.5 sec (SD=0.2)."
> — Moscovich vd. 2009, **gövde**, "Results / Neighbors Task — Performance Time".

> "BEV (42% error rate) and LS (33%) were both significantly more error-prone than B&G (10%), while PZ showed a 25% error rate."
> — Moscovich vd. 2009, **gövde**, "Results / Neighbors Task — Error Rate" (yoğun graf).

> "Our results show that Pan and Zoom Navigation was significantly faster and required less mental effort than Rubber Sheet Navigation, independent of the presence or absence of an overview. Also, overviews did not appear to improve performance, but were still perceived as beneficial by users."
> — Nekrasovski vd. 2006, **abstract**.

> "evaluations of distortion-based techniques have largely failed to provide evidence of performance enhancements, and several studies have shown that fisheye views can damage fundamental components of interaction such as target acquisition."
> — Cockburn vd. 2008, **gövde**, Bölüm 8 "Discussion" (s.2:26).

### Bu alt-sorunun kanıt okuması

- **"Focus+context" tek bir şey değil ve kanıt ikiye ayrılıyor:**
  - **(a) Topoloji-farkında odak (komşuyu yanına getirme / alt-graf çıkarma):** ölçülmüş kazanç GÜÇLÜ. 1000 düğümlük grafta 1-sıçrama komşuluk görevinde 3,2× hız + hata %25→%10 (Moscovich 2009).
  - **(b) Geometrik bozunum tabanlı F+C (rubber sheet, fisheye):** ölçülmüş kazanç YOK ya da NEGATİF. 5.918 düğümlü ağaçta düz pan&zoom, bozunumlu F+C'yi anlamlı ölçüde geçti (Nekrasovski 2006); derleme de bozunum tekniklerinin performans kanıtı üretemediğini söylüyor (Cockburn 2008).
- **Genel-bakış (overview) paneli**: Nekrasovski'de tamamlanma süresine ölçülebilir katkısı yok (F(1,36)=0,611, p>0,4) — ama kullanıcılar faydalı ALGILADI. Algı ↔ ölçüm ayrışması kayda geçirildi.
- **Boşluk:** "Tam graf görünümü **vs** odak-alt-graf görünümü"nü doğrudan karşılaştıran, ~500 düğümlük bilgi-deposu tipi veride koşulmuş kontrollü deney BULUNAMADI. Moscovich'te tüm koşullar aynı 1000 düğümlük grafı gösteriyor; değişen şey GEZİNME tekniği, "kaç düğüm gösterilsin" değil. Bu, kanıt zincirinin en zayıf halkası olarak işaretlenir.
- Dolaylı destek: >500 düğümlü çalışmaların %83'ünün zaten parça-çıkaran etkileşimli araçları değerlendirmesi (Yoghourdjian 2018) — bu bir ölçüm değil, alanın pratiğinin betimlemesi.

---

## İDDİALAR (antitez aşaması bu listeyi kullanacak)

Her madde: tek cümle · kanıt-URL'li · AS-OF 2026-08-29.

1. Ware & Franck'in 1996 deneyinde 3B'nin ölçülmüş üstünlüğü stereo ve gerçek-zamanlı hareketten gelir; aynı deneyde **statik perspektif 2B'den anlamlı ölçüde farklılaşmamıştır** — yani düz, döndürmesiz masaüstü 3B'nin ölçülmüş kazancı sıfırdır. → https://www.cs.kent.edu/~jmaletic/softvis/papers/ware96.pdf (Bölüm 4.3, s.136)
2. Aynı çalışmada aynı hata oranında anlaşılabilir graf boyutu yalnız stereo ile 1,6×, yalnız kafa-izleme ile 2,2×, ikisi birlikte 3,0× büyür (hata=C·N katsayıları 0,369 / 0,232 / 0,167 / 0,123). → https://www.cs.kent.edu/~jmaletic/softvis/papers/ware96.pdf (Bölüm 3.2, s.133)
3. Ware & Franck'te 3B'nin süre üzerinde ölçülmüş etkisi YOKTUR; tamamlanma süresini belirleyen tek anlamlı etken düğüm sayısıdır (F(4,100)=10,14, p<0,01). → https://www.cs.kent.edu/~jmaletic/softvis/papers/ware96.pdf (Bölüm 2.3, s.130)
4. Otomatik (pasif) dönüş düz ekranda donanımsız uygulanabilir ve yalnız-hareket koşullarının ortalama hatası %11,4'tür (2B %26'ya karşı), fakat aynı yazarlar nesne SEÇİMİ önemliyse otomatik dönüşün istenmediğini yazar. → https://www.cs.kent.edu/~jmaletic/softvis/papers/ware96.pdf (Bölüm 4.3 ve 5, s.136-138)
5. Ware & Mitchell 2008'e göre hareket+stereo ile eğitimsiz gözlemciler 333 düğümde, eğitimli gözlemciler 1000 düğümde <%10 hatayla yol izleyebilir — **ancak bu iddia yalnız ABSTRACT düzeyinde doğrulandı, tam metin ACM paywall'ı arkasındadır.** → https://scholars.unh.edu/ccom/467/
6. Kotlarek vd. 2020'de (n=20; 379 ve 4.941 düğümlü gerçek ağlar dâhil) 3B VR yol görevinde 2B masaüstünden daha DOĞRU (0,950 vs 0,806; p=0,0065) ama her üç görevde de daha YAVAŞtır (bellek görevi 50,70s vs 31,92s; p=2,3·10⁻⁷). → https://arxiv.org/abs/2001.06462
7. Kotlarek vd. 2020'de bellek/uzamsal-hatırlama görevinde 2B, 3B'den anlamlı ölçüde daha doğrudur (0,951 vs 0,923; t(59)=4,2086, p=8,88·10⁻⁵), yani 3B'nin avantajı göreve göre işaret değiştirir. → https://arxiv.org/abs/2001.06462
8. McGuffin vd. 2022'de (n=34, 70 düğüm) 3B, kenar-yönlendirmeli 2B'den daha düşük hata verir (p<0,0000005), fakat **2B kolu da VR içinde gösterilmiştir; masaüstü 2B ile kıyas değildir.** → https://arxiv.org/abs/2207.11586
9. Feyer vd. 2023 (n=22, VR, 90 ve 210 düğümlük çok-katmanlı ağlar) altı görevde "net bir genel kazanan" bulamamış; büyük ağlarda 3B kimi görevde en yüksek hatayı üretmiştir (T3 0,45; T5 0,36 — 2B 0,18 ve 0,09'a karşı). → https://arxiv.org/abs/2307.10674
10. Feyer vd. 2023'te büyük ağlarda en düşük tamamlanma süresi çoğunlukla 2B düzenlemesindedir (T2: 64,94s vs 2.5D 138,9s; T3: 120,45s vs 2.5D 186,23s). → https://arxiv.org/abs/2307.10674
11. Greffard vd. 2011'de (n=35) stereoskopi 3B monoskopik perspektifi çoğu durumda geçer, fakat tepki süresi 2B lehine anlamlıdır ve stereo yalnız çok-kümeli/yüksek-örtüşmeli graflarda 2B'yi geçer — **bu iddia paywall nedeniyle yalnız abstract/aktarım düzeyindedir.** → https://link.springer.com/chapter/10.1007/978-3-642-25878-7_21
12. Düğüm-bağ diyagramlarında en-kısa-yol bulma için ölçülmüş kırılma noktası: yoğunluk 6'da ≥50 düğüm, yoğunluk 2'de >100 düğüm; bu noktalarda katılımcılar denemelerin yarısından fazlasında YANLIŞ cevap vermiştir (n=22). → https://arxiv.org/abs/2008.07944
13. Aynı çalışmada bilişsel yük ölçümleri (EEG/göz-bebeği/HRV) zorluk arttıkça yükselip belli bir eşikten sonra DÜŞER — yazarların yorumu: katılımcılar pes eder. → https://arxiv.org/abs/2008.07944
14. 500-600 düğümlük bir grafın tam görünümünde topoloji görevi performansını ölçen birincil deney **bulunamadı**; en yakın ölçüm aralığı 25-175 düğümde (Yoghourdjian 2020) ve 258-332 düğümde (Okoe 2018) sona erer. → https://arxiv.org/abs/2008.07944 · https://openaccess.city.ac.uk/20159/
15. 152 kullanıcı çalışmasının taramasında graf boyutu medyanı 49,5 düğümdür ve çalışmaların %80'i (121/152) ≤100 düğüm kullanır. → https://arxiv.org/abs/1809.00270
16. Aynı taramada >500 düğüm kullanan 24 çalışmanın 20'si (%83) tam grafı değil, grafın PARÇASINI çıkaran etkileşimli teknikleri değerlendirir. → https://arxiv.org/abs/1809.00270
17. Aynı taramanın kendi tespiti: düğüm-bağ paradigmasının ölçeklenme sınırları literatürde "doğrudan nadiren ele alınmakta", 20/50/100 gibi yaygın boyutlar ampirik değil keyfîdir. → https://arxiv.org/abs/1809.00270
18. Ghoniem vd. 2005'e göre 20 düğümden büyük graflarda matris temsili çoğu görevde düğüm-bağı geçer; yalnız YOL BULMA tutarlı biçimde düğüm-bağ lehinedir — **tam metin SAGE paywall'ı arkasında, yalnız abstract'a dayanılmıştır.** → https://journals.sagepub.com/doi/10.1057/palgrave.ivs.9500092
19. Okoe vd. 2018'de (864 katılımcı; 258 ve 332 düğümlü ağlar, etkileşimli arayüz) düğüm-bağ diyagramı topoloji sorularında matrisi geçer (10 görevin 5'inde daha doğru, 3'ünde daha az doğru) — 20-düğüm eşiğiyle ıraksayan bir bulgudur. → https://openaccess.city.ac.uk/id/eprint/20159/1/node-link-adjacency%20%283%29.pdf
20. Odak-panosu tipi teknik (1-sıçrama komşuları odağın yanına getirme) 1000 düğümlük grafta pan&zoom'a göre komşu-inceleme görevinde 27,2s → 8,5s (~3,2× hız) ve yoğun grafta hata %25 → %10 kazanç sağlar (n=12). → https://www.aviz.fr/wiki/uploads/Research/topologyawarenav-CHI2009.pdf
21. Aynı deneyde odak-getirme tekniği yeniden-ziyaret (15,6s → 7,2s) ve bağ-takip (7s → 4,2s) görevlerinde de tüm diğer tekniklerden anlamlı ölçüde hızlıdır (p<0,0001). → https://www.aviz.fr/wiki/uploads/Research/topologyawarenav-CHI2009.pdf
22. Buna karşılık geometrik bozunum tabanlı focus+context (rubber sheet) 5.918 düğümlük ağaçta düz pan&zoom'dan anlamlı ölçüde YAVAŞtır ve daha çok zihinsel çaba ister (n=40; F(1,36)=13,477, p<0,001). → https://www.cs.ubc.ca/labs/imager/tr/2006/Nekrasovski2006CHI/Nekrasovski2006CHI.pdf
23. Genel-bakış (overview) panelinin tamamlanma süresine ölçülmüş katkısı yoktur (F(1,36)=0,611, p>0,4), ama kullanıcılar onu yararlı ALGILAR — algı ile ölçüm ayrışır. → https://www.cs.ubc.ca/labs/imager/tr/2006/Nekrasovski2006CHI/Nekrasovski2006CHI.pdf
24. ACM Computing Surveys derlemesi bozunum-tabanlı tekniklerin değerlendirmelerinin "büyük ölçüde performans iyileşmesi kanıtı üretemediğini" ve fisheye görünümlerin hedef-seçme gibi temel etkileşim bileşenlerine zarar verebildiğini yazar (İKİNCİL kaynak). → https://faculty.cc.gatech.edu/~stasko/7450/Papers/cockburn-surveys08.pdf
25. Odak-alt-graf yaklaşımının kanonik makalesi (van Ham & Perer 2009, degree-of-interest) **kontrollü deney içermez**; değerlendirmesi tek bir hukuk atıf ağı üzerinde vaka çalışmasıdır — bu tekniğin ölçülmüş kazancı bu kaynaktan gösterilemez. → https://aviz.fr/wiki/uploads/Teaching2014/SearchShowContext.pdf
26. "Tam graf görünümü vs odak-alt-graf görünümü"nü doğrudan karşılaştıran kontrollü deney bulunamadı; Moscovich deneyinde tüm koşullar aynı 1000 düğümlük grafı gösterir, değişen yalnız gezinme tekniğidir. → https://www.aviz.fr/wiki/uploads/Research/topologyawarenav-CHI2009.pdf
27. Alandaki 2025 tarihli en yeni graf-algısı çalışması (n=18) yalnız stereoskopik 3B VR koşuluyla koşulmuştur, 2B karşılaştırma kolu içermez — yani 2B/3B kıyas literatürü 2023'ten bu yana yeni bir birincil ölçümle güncellenmemiştir (bu taramanın bulabildiği kadarıyla, AS-OF 2026-08-29). → https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.GD.2025.11
28. Feyer vd. kendi sınırlılık bölümünde deneyin VR'da koşulduğunu ve aynı deneyin "2B ekranda" tekrarlanmasının ilginç olacağını yazar — yani modern 2B/2.5D/3B kıyaslarının masaüstü ekrana aktarılabilirliği yazarlarınca da AÇIK BIRAKILMIŞTIR. → https://arxiv.org/abs/2307.10674

---

## BULUNAMADI (meşru boşluklar — antitez için hedef)

| Boşluk | Ne arandı | Sonuç |
|---|---|---|
| 500-600 düğümde tam-graf topoloji görevi ölçümü | Yoghourdjian 2020 aralığı, tarama histogramı, Okoe veri kümeleri | Ölçüm aralıkları 175 ve 332 düğümde bitiyor; bu aralıkta birincil deney YOK |
| Düz masaüstü ekranda 3B döndürülebilir graf ↔ 2B graf kıyası (modern, ~2015+) | 2B/3B/VR aramaları, GD 2025, GI 2026 | Modern kıyasların tamamı VR/HMD içinde; düz-ekran kolu yalnız Ware & Franck 1996 (statik perspektif) ve Greffard 2011'de (paywall) var |
| Tam-graf ↔ odak-alt-graf doğrudan kıyası | focus+context, degree-of-interest, ego-network aramaları | Bulunamadı; en yakın kanıt gezinme-tekniği kıyası (Moscovich) |
| Bilgi-deposu/kişisel-not grafı bağlamında (Obsidian/Roam sınıfı) kontrollü deney | genel aramalar | Bu taramada bulunamadı; tüm birincil kanıt sentetik veya bilimsel/sosyal ağlardan |
| Greffard 2011'in n=35 deneyinin koşul-başına sayıları | Springer, ResearchGate, Semantic Scholar, kurumsal ayna | Paywall + 403; abstract düzeyinde kaldı |

## ARAŞTIRMANIN KENDİ SINIRLARI (epistemolojik not)

- Ware & Franck'in görevi "iki vurgulu düğüm arasında 2 uzunluklu yol var mı" — dar, algısal bir görevdir; bir bilgi deposunun okunması (arama, hatırlama, ilişki keşfi) bu göreve indirgenemez. Sonuçların aktarılabilirliği YAZARLARCA da sınırlandırılmıştır ("the answer must be task specific to some extent", Bölüm 1.4, gövde).
- 1996 ve 2008 tarihli bulgular o günün donanımıyla (CRT, 120 Hz shutter gözlük, ultrasonik kafa izleme) elde edildi; modern HMD'lerle tekrar-üretim Kotlarek/McGuffin/Feyer'de KISMEN yapıldı ve sonuçlar karıştı.
- 4 çalışmada (Ware & Mitchell 2008, Greffard 2011, Ghoniem 2005, Schaffer 1996) tam metne erişilemedi; bu kalemlerin sayıları abstract veya derleme aktarımı düzeyindedir ve tablo/iddia listesinde ayrıca bayraklanmıştır.
- Bu rapor bir öneri veya karar İÇERMEZ (görev emri: "KARAR VERME").

---

**Rapor sonu — ATLAS, 2026-08-29.**
