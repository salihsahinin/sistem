# ANTİTEZ RAPORU — Aile B (2B↔3B graf okunabilirliği)

**Ajan:** ATLAS (antitez rolü — açık devil's advocate)
**Tarih / AS-OF:** 2026-08-29 (tüm bulgular bu tarih itibarıyla; kaynak yayın tarihleri ayrıca verildi)
**Görev:** Verilen iddiaların DEĞİLİNİ (¬T) savunacak birincil kanıt aramak. Kaynak/gerekçe bilerek verilmedi; tüm kanıt bağımsız arandı.

## 0. Kırpma beyanı (hakeme görünür)
Orijinal liste **28 iddia**; görev emrinde karar-taşıyan **14 iddiaya** kırpılmıştır (kırpmayı gönderen taraf yaptı, ATLAS yapmadı). Kırpılan 14 iddia bu raporda İNCELENMEDİ; dolayısıyla bu rapor Aile B'nin tamamı için değil, karar-taşıyan alt küme için geçerlidir.

## 0.1 Erişim engelleri (bayraklar)
- `inria.hal.science` → **403 (Anubis bot duvarı)**, hem curl hem WebFetch. Moscovich 2009 metnine `aviz.fr` aynasından ulaşıldı (tam metin, PDF).
- `researchgate.net` → 403.
- **Yalnız abstract'a dayanan iki kaynak:** Ware & Bobrow 2005 (*Information Visualization*) ve Ware & Mitchell 2008 (*ACM TAP*) — tam metin yayıncı duvarında; abstract'lar UNH kurumsal arşivinden (scholars.unh.edu) birebir alındı. İlgili yerlerde işaretlendi.
- ACM DL tam metinleri paywall; kullanılmadı.

## 0.2 Skor tablosu

| # | Konu | Karar |
|---|------|-------|
| 1 | Statik perspektif 3B ≈ 2B | DARALDI |
| 2 | 3B'nin süre kazancı hiç yok | **ÇÜRÜDÜ** |
| 3 | Uzamsal bellekte 2B > 3B | **ÇÜRÜDÜ** |
| 4 | 2015 sonrası düz-ekran 3B↔2B deneyi yok | **ÇÜRÜDÜ** |
| 5 | Yol görevi ≥50 yoğun / >100 seyrek kırılır | **ÇÜRÜDÜ** (eşikler yanlış, iki yönde) |
| 6 | Medyan ~50 düğüm; >500 çalışmaları parça-çıkarma | ÇÜRÜTEMEDİM (kanıt iddiayı doğruluyor) |
| 7 | 500-600 düğüm tam-graf topoloji deneyi yok | DARALDI |
| 8 | Odak-getirme ~3× hız, hata yarılanması | ÇÜRÜTEMEDİM (doğrulandı; kapsamı daraltıldı) |
| 9 | Geometrik-bozunum F+C pan&zoom'dan yavaş + derlemeler kanıt yok der | **ÇÜRÜDÜ** (her iki yarısı) |
| 10 | Overview'ün süreye ölçülmüş katkısı yok | **ÇÜRÜDÜ** |
| 11 | Yol-bulma tutarlı biçimde düğüm-bağ lehine | DARALDI |
| 12 | PKM/not-grafı kontrollü deney yok | ÇÜRÜTEMEDİM (arandı, bulunamadı) |
| 13 | Tam-graf ↔ odak-alt-graf doğrudan kıyas yok | DARALDI |
| 14 | DOI kanonik makalesi kontrollü deney içermez | DARALDI (hangi makale "kanonik" sayıldığına bağlı) |

Özet: 6 ÇÜRÜDÜ · 5 DARALDI · 3 ÇÜRÜTEMEDİM · 0 ARANMADI.

---

## İDDİA 1 — "Düz ekranda statik perspektif 3B, 2B'den anlamlı ayrışmaz; 3B kazancı yalnız stereo + gerçek-zamanlı hareketten gelir."
**Karar: DARALDI** (AS-OF 2026-08-29)

**Karşı-kanıt (statik perspektif 3B, düz ekran, stereo YOK, hareket YOK, yine de anlamlı üstün):**
Tavanti & Lind, "2D vs 3D, Implications on Spatial Memory", IEEE InfoVis 2001.
URL: https://www.cs.kent.edu/~jmaletic/cs63903/papers/Tavanti01.pdf

Yöntem beyanı (§3, "2D vs 3D: background"), ham alıntı:
> "By '3D' in this paper we specifically refer to 2D perspective projections of 3D environments."

Donanım (§4.2.2): Pentium II, **19 inç 1024×768 düz ekran**; 3B görüntü Cinema 4D ile üretilmiş statik sahne (§4, "the 3D display was a static environment"). Stereo yok, kinetik derinlik yok.

Sonuçlar (§8, Deney II — burada HER İKİ koşul da statik ve kaydırmasız, yani Deney I'deki kaydırma karışıklığı giderilmiş):
- Genel doğru sayısı: 3B **20,03** vs 2B **12,8**; Mann-Whitney **U=21,5, p<.05**
- Derinlik düzeyine doğru yerleştirme: 3B **24,7** vs 2B **17,1**; **U=14,5, p<.01**
- n = 20 (10 kadın / 10 erkek, gruplar arası)
Deney I (§5.1): 3B 10,2 vs 2B 4,2; **U=10,5, p<.01**; derinlik düzeyi 15,3 vs 10,5; **U=20, p<.05**; n=20.

**Karşı-kanıtın sınırı (dürüst bildirim — iddiayı destekleyen taraf):**
1. Uyaran bir **hiyerarşi/ağaç** (27 dikdörtgen, 4 derinlik), genel graf değil; görev uzamsal bellek, topoloji görevi değil.
2. Doğrudan yineleme başarısız: Cockburn & McKenzie, "Revisiting 2D vs 3D Implications on Spatial Memory", AUIC 2004 — URL: https://www.csse.canterbury.ac.nz/andrew.cockburn/papers/revisiting2Dv3D.pdf — sonuç bölümü ham alıntı: *"the presence of perspective effects made no difference to how well participants recalled the location of letters or flags"* ve *"The results disagree with the prior work, and strongly suggest that these 3D effects make no [difference]"*.
3. **İddianın lehine ek kanıt bulundu:** Huang, Pfister & Yang 2023 (bkz. İddia 4) düz ekranda 2B+fare ile **döndürülebilir** 3B+fare arasında üç görevin üçünde de zaman ve doğrulukta anlamlı fark bulamadı — yani iddia graf görevleri için ayakta.

**Daralma:** İddia "graf görevleri" için ayakta; "hiçbir görevde ayrışmaz" biçiminde genellenirse yanlış — statik perspektif 3B, hiyerarşik uzamsal-bellek görevinde 2B'yi anlamlı geçmiştir (tartışmalı, bir yineleme çalışması nötr çıktı).

---

## İDDİA 2 — "3B'nin tamamlanma SÜRESİ üzerinde ölçülmüş kazancı hiçbir kontrollü çalışmada yoktur; VR'da 3B daha doğru olsa bile daha yavaştır."
**Karar: ÇÜRÜDÜ** (AS-OF 2026-08-29)

**Karşı-kanıt:** Kwon, Muelder, Lee & Ma, "A Study of Layout, Rendering, and Interaction Methods for Immersive Graph Visualization", *IEEE TVCG* 22(7):1802-1815, 2016.
URL (yazar kopyası, tam metin): http://kwon.io/resource/papers/kwon_tvcg2016.pdf
DOI: https://doi.org/10.1109/TVCG.2016.2520921

Tasarım: n=**21** (12E/9K), Oculus Rift DK2, tekrarlı ölçüm. Koşullar: **C1 = 2B düzen**, C2 = küresel 3B düzen (derinlik yönlendirmesi yok), C3 = küresel 3B + derinlik yönlendirmesi. Veri: D1 77 düğüm/254 kenar, D2 116/615, D3 297/2359. Görevler: T1 ortak komşu, T2 en yüksek derece, T3 yol, T4 (dördüncü görev).

Ölçülen süre (§4.6.1, ham alıntı):
> "Average task completion times (Fig. 11a) are 75.77s for C1 (SD = 103.19), 56.22s for C2 (SD = 67.02), and 43.20s for C3 (SD = 50.55). Post-hoc tests using the Bonferroni correction indicate that C3 is significantly faster than both C1 (p < .0001) and C2 (p < .05), and that C2 is also significantly faster than C1 (p < .05)."

ANOVA: F(1.38, 27.63) = 16,05, **p<.001** (Greenhouse-Geisser, ε=.691).
3B (C3), 2B'ye göre **%43 daha hızlı** — iddianın "hiçbir kontrollü çalışmada süre kazancı yok" hükmü yanlış.

İddianın ikinci yarısı ("daha doğru ama daha yavaş") da tersine dönüyor: en büyük grafta (D3) doğruluk C1 %80,95 · C2 %88,1 · **C3 %95,24**; F(2,40)=6,92, **p<.01**; C3-C1 farkı p<.05. Yani aynı çalışmada 3B hem **daha hızlı** hem **daha doğru**.

**Sınır (dürüst bildirim):** 2B temel koşul (C1) de HMD içinde gösterilmiştir — masaüstü 2B ekranla kıyas değildir. Yani "3B'nin süre kazancı ölçülmüştür" kesin; "masaüstü 2B'ye karşı ölçülmüştür" değildir.

---

## İDDİA 3 — "Uzamsal-bellek/hatırlama görevlerinde 2B, 3B'den daha doğrudur."
**Karar: ÇÜRÜDÜ** (AS-OF 2026-08-29)

**Karşı-kanıt:** Tavanti & Lind 2001 (yukarıda, İddia 1). İki deneyin ikisinde de **3B anlamlı biçimde DAHA DOĞRU**:
- Deney I: 3B 10,2 vs 2B 4,2 doğru (U=10,5, **p<.01**), n=20
- Deney II: 3B 20,03 vs 2B 12,8 doğru (U=21,5, **p<.05**), n=20
Sonuç bölümü ham alıntı (§9):
> "In conclusion, the results of the experiment showed that subjects performed significantly better using the 3D display."

**Bu aramada iddiayı destekleyen (2B > 3B) BİRİNCİL kanıt bulunamadı.** En yakın karşıt bulgu Cockburn & McKenzie 2004'tür ve o da **fark yok** demektedir, "2B daha doğru" dememektedir. Dolayısıyla iddia, elde edilen iki birincil kaynağın hiçbiriyle desteklenmiyor; biri onu tersine çeviriyor.

**Sınır:** Uyaran hiyerarşi; graf değil. Uzamsal-bellek literatüründe 2B lehine bulgular olduğu bilinir (ör. Cockburn & McKenzie'nin daha eski çalışmaları) — ancak bu koşumda birincil metinleri çekilmedi, dolayısıyla ATLAS bunları kanıt olarak SAYMIYOR.

---

## İDDİA 4 — "2015 sonrası tüm 2B↔3B graf kıyasları VR/HMD içinde koşulmuştur; düz masaüstü ekranda modern 3B-döndürülebilir↔2B kıyası YOKTUR."
**Karar: ÇÜRÜDÜ** (AS-OF 2026-08-29)

**Karşı-kanıt (aranan deney bulundu):** Huang, Pfister & Yang, "Is Embodied Interaction Beneficial? A Study on Navigating Network Visualizations", *Information Visualization* 22(3):169-185, 2023.
URL (tam metin): https://arxiv.org/pdf/2301.11516 · Yayıncı: https://doi.org/10.1177/14738716231157082

Koşullar (Şekil 1 başlığı, ham alıntı):
> "(a) 2D network visualization displayed on a 2D screen with a standard mouse, (b) 3D network visualization on a 2D screen with a standard mouse, (c) 3D network visualization on a 2D screen with a trackball mouse, (d) 3D network visualization in virtual reality with hand-held controllers."

Yani **(a) ve (b) tam olarak aranan kıyastır**: düz masaüstü ekranda 2B ↔ döndürülebilir 3B, aynı ekran ve aynı girdi aygıtı. n=**20**, 4 koşul × 3 görev = 24 deneme/katılımcı. Graf boyutları: Common görevi 60 düğüm (3 küme), Compare görevi 100 düğüm; veriler stochastic block model ile üretilmiş.

Sonuç (ham alıntı):
> "We did not find significant differences between 2D Vis+Mouse and 3D Vis+Mouse in time and accuracy for all three tested tasks."

**Not:** Bu bulgu İddia 4'ü çürütürken İddia 1'i (graf görevleri kısmını) DESTEKLER. Devil's advocate rolüne rağmen bunu gizlemiyorum: iddia 4 "böyle bir deney yok" dediği için yanlıştır; deney vardır ve sonucu iddia 1'in lehinedir.

---

## İDDİA 5 — "En-kısa-yol görevi yoğun grafta ≥50, seyrek grafta >100 düğümde kırılır."
**Karar: ÇÜRÜDÜ** (eşik sayıları iki yönde de yanlış) (AS-OF 2026-08-29)

**Karşı-kanıt A — 50'de kırılmıyor:** Ghoniem, Fekete & Castagliola, "On the Readability of Graphs Using Node-Link and Matrix-Based Representations: A Controlled Experiment and Statistical Analysis", *Information Visualization* 4(2):114-135, 2005.
URL (tam metin): http://www-sop.inria.fr/orion/COGC/teams/INSITUghoniem-fivj05-final.pdf

§3.5.7 "findPath", ham alıntı:
> "On small graphs, 99% of the users answer correctly using node-link diagrams against 70% only using matrices. On medium-sized graphs, node-link diagrams record 93% of correct answers with a lead of 10% over matrices. For large graphs, every other user answers correctly using both representations with a statistically insignificant lead in favor of matrices."

Boyutlar 20 / 50 / 100 düğüm, yoğunluklar 0,2 / 0,4 / 0,6 (yani hepsi "yoğun"). **50 düğümde düğüm-bağ %93 doğru** → iddianın "≥50'de kırılır" eşiği yanlış. Kırılma 100'de gerçekleşiyor (~%50 doğru), seyrek değil YOĞUN grafta.

**Karşı-kanıt B — kırılma çok daha ERKEN de olabilir, çok daha GEÇ de:** Ware & Bobrow, "Supporting visual queries on medium-sized node-link diagrams", *Information Visualization*, 2005.
URL (abstract, kurumsal arşiv — **yalnız abstract'a dayanıldı, tam metin paywall**): https://scholars.unh.edu/ccom/1014/
Ham alıntı:
> "An experimental evaluation was carried out with networks having 32, 100, 320, 1000, and 3200 nodes respectively, and with four highlighting techniques: static highlighting, motion highlighting, static+motion highlighting, and none. The results show that the interactive highlighting methods support rapid visual queries of nodes in close topological proximity to one another, even for the largest diagrams tested. Without highlighting, error rates were high even for the smallest network that was evaluated."

Yani vurgulama YOKKEN **32 düğümde bile** hata oranı yüksek (iddia edilen 50/100 eşiğinin çok altı); vurgulama VARKEN **3200 düğümde bile** sorgular hızlı ve doğru (eşiğin çok üstü).

**Karşı-kanıt C:** Ware & Mitchell, "Visualizing graphs in three dimensions", *ACM TAP* 5(1):1-15, 2008 (abstract, https://scholars.unh.edu/ccom/467/ — **yalnız abstract**):
> "with both motion and stereoscopic depth cues, unskilled observers could see paths between nodes in 333 node graphs with less than a 10% error rate. Skilled observers could see up to a 1000-node graph with less than a 10% error rate. This represented an order of magnitude increase over 2D display."

"2B'ye göre bir büyüklük mertebesi artış" ifadesi, 2B'de <%10 hata sınırının **~33 düğüm** civarında olduğunu ima eder — yine iddianın 50/100 eşiğinin altında.

**Sonuç:** Kırılma noktası düğüm sayısının tek başına fonksiyonu değil; **etkileşim + derinlik ipucu** koşuluna bağlı. İddianın sabit sayıları hem aşağı hem yukarı yönde çürütüldü.

---

## İDDİA 6 — "Medyan graf boyutu ~50 düğüm; >500 düğüm kullanan çalışmaların büyük çoğunluğu parça-çıkarma tekniklerini ölçer."
**Karar: ÇÜRÜTEMEDİM — birincil kaynak iddiayı neredeyse birebir doğruluyor** (AS-OF 2026-08-29)

Yapılan aramalar: `Yoghourdjian "Exploring the limits of complexity" median number of nodes`; ardından birincil PDF indirilip Table 2 ve §4.1 tam metinden okundu.

Kaynak: Yoghourdjian, Archambault, Diehl, Dwyer, Klein, Purchase & Wu, "Exploring the limits of complexity: A survey of empirical studies on graph visualisation", *Visual Informatics* 2(4):264-282, 2018.
URL (tam metin): https://www.cg.tuwien.ac.at/research/publications/2019/YOGHOURDJIAN2019/YOGHOURDJIAN2019-paper.pdf · arXiv: https://arxiv.org/abs/1809.00270

Table 2 (birebir satır): Nodes — Minimum 2 · Maximum 113 M. · Average 457.242 · **Median 49,5** · Alt çeyrek 18,5 · Üst çeyrek 116,5.

İkinci yarı, §4.1 ham alıntı:
> "Among these studies, the majority aim is to evaluate tools that use interactive exploration to extract parts (e.g. neighbourhoods) of the graph (20/24 studies, 83%)."
ve
> "Most of the studies that use a large number of nodes, use abstractions or aggregation to show only parts of the graph at a time, but do not report on the number of nodes seen at a given abstraction."

İddiadaki "~50" = 49,5 (medyan, 152 çalışma); "büyük çoğunluğu" = %83 (20/24). **Çürütecek kanıt bulunamadı; aksine iddia doğrulandı.**

---

## İDDİA 7 — "500-600 düğümlük TAM-graf görünümünde topoloji-görevi performansını ölçen birincil deney YOKTUR."
**Karar: DARALDI** (AS-OF 2026-08-29)

Tam olarak 500-600 bandında, tam-graf görünümlü, topoloji görevli birincil deney **bulunamadı**. Ancak bandın iki yanı da kapatılmıştır — yani "bu ölçekte kanıt yok" genellemesi yanlıştır:

1. **Ware & Bobrow 2005** (abstract — https://scholars.unh.edu/ccom/1014/): 32 / 100 / **320** / **1000** / 3200 düğümlü tam düğüm-bağ diyagramları; görev "nodes in close topological proximity to one another" = topoloji görevi. 320 ve 1000, 500-600 bandını kuşatır.
2. **Ware & Mitchell 2008** (abstract — https://scholars.unh.edu/ccom/467/): **333** ve **1000** düğümlü graflarda yol izleme (topoloji), tam graf görünümü.
3. **Okoe, Jianu & Kobourov 2019**, *IEEE TVCG* 25(10):2940-2952 (tam metin: https://www2.cs.arizona.edu/~kobourov/NL-AM-TVCG18.pdf): **258 düğüm/1090 kenar** ve **332 düğüm/2126 kenar** gerçek-dünya grafları, 864 çevrimiçi katılımcı, 14 görev — bunların 10'u topoloji görevi; tam graf gösterildi (zoom/pan ile).
4. Yoghourdjian ve ark. 2018 §5.1.1'in bildirdiğine göre **Okoe ve ark. 2014**, 900 düğüm / 2500 kenarlı grafla topoloji görevi ölçmüş, >%50 hata oranı raporlamıştır (ikincil aktarım — birincil metin bu koşumda çekilmedi, bu yüzden zayıf kanıt sayılır).

**Daralma:** İddia yalnızca "tam olarak 500-600 düğümde koşulmuş bir deney yok" biçiminde doğrudur; "bu ölçek ölçülmemiştir" biçiminde yanlıştır.

---

## İDDİA 8 — "Odak-getirme (1-sıçrama komşuları getirme) 1000 düğümlük grafta pan&zoom'a göre ~3× hız ve hata yarılanması sağlar."
**Karar: ÇÜRÜTEMEDİM — sayılar birincil kaynakta doğrulandı; kapsam daraltıldı** (AS-OF 2026-08-29)

Aramalar: `Moscovich "Topology-aware navigation in large networks" CHI 2009 results completion time`; HAL 403 verdi, metin **aviz.fr aynasından** alındı.
Kaynak: Moscovich, Chevalier, Henry, Pietriga & Fekete, "Topology-Aware Navigation in Large Networks", *ACM CHI 2009*.
URL (tam metin PDF): https://www.aviz.fr/wiki/uploads/Research/topologyawarenav-CHI2009.pdf · DOI: https://doi.org/10.1145/1518701.1519056

Tasarım: n=**12**; seyrek graf **1000 düğüm / 1485 kenar**, yoğun graf **1000 düğüm / 2488 kenar**; teknikler PZ (pan&zoom), BEV (kuşbakışı), LS (link sliding), B&G (bring & go).

Neighbors (komşuları ziyaret) görevi — ham alıntı:
> "Mean times were: PZ 27.2 sec (SD=0.8), BEV 21 sec (SD=0.7), LS 24 sec (SD=0.8) and B&G 8.5 sec (SD=0.2)."
ANOVA: F(3,33)=69,811, **p<.0001**. → 27,2 / 8,5 = **3,2×**. İddianın "~3×" rakamı doğrulandı.

Hata — ham alıntı:
> "BEV (42% error rate) and LS (33%) were both significantly more error-prone than B&G (10%), while PZ showed a 25% error rate."
25% → 10% = **2,5× azalma** (yarılanmadan daha iyi). İddia doğrulandı.

**Daralma (tek gerçek karşı-bulgu):** 3× çarpanı **göreve özgüdür**. Aynı deneyin "Follow" görevinde:
> "Mean times were: PZ 7 sec (SD=0.4), BEV 5.6 sec (SD=0.2), LS 4.9 sec (SD=0.3) and B&G 4.2 sec (SD=0.2)."
→ 7 / 4,2 = **1,67×**, ve o görevde toplam yalnız 2 hata oluştu (ikisi de PZ) — hata yarılanmasından söz edilemez. Ayrıca kazanç **1-sıçrama komşuluk** görevine bağlıdır; genel navigasyona genellenemez.

---

## İDDİA 9 — "Geometrik-bozunum focus+context (fisheye/rubber-sheet) kontrollü ölçümlerde pan&zoom'dan yavaştır ve alan derlemeleri bu sınıfın performans kanıtı üretemediğini söyler."
**Karar: ÇÜRÜDÜ (her iki yarısı da)** (AS-OF 2026-08-29)

**A) "Daha yavaştır" — çürüten birincil deney:**
Schaffer, Zuo, Greenberg, Bartram, Dill, Dubs & Roseman, "Navigating Hierarchically Clustered Networks through Fisheye and Full-Zoom Methods", *ACM TOCHI* 3(2):162-188, 1996.
URL (tam metin): https://markroseman.com/pubs/fisheyetochi96.pdf

n=**20** denek, hiyerarşik kümelenmiş **telefon ağı** (graf) üzerinde kopuk hat bulma + yeniden yönlendirme görevi, 2×2 (görünüm × sıra) denek-içi tasarım. §4 Results ham alıntı:
> "An analysis of variance revealed that running time was significantly affected by the view factor used in the task (F=9.91, p=.01), with people completing the task much faster when using fisheye views (102 seconds versus 161 seconds)."

Tablo 3: fisheye **101,9 s** (SD 59,5) vs full-zoom **161,2 s** (SD 71,6) → fisheye **%37 daha hızlı**. Zoom sayısı 6,3 vs 10,9 (F=18,29, **p=.00**). Hata: 20 full-zoom yeniden-yönlendirmesi başarısız, yalnız 4 fisheye hatalı.

**Ek karşı-kanıt (aynı sınıf, farklı görev):** Furnas, "Generalized Fisheye Views", *ACM CHI 1986* — URL: https://cspages.ucalgary.ca/~saul/581/exer.eps/4furnas86.pdf — n=20, ham alıntı:
> "We found that people were only 52% correct with two flat views, 64% correct with one fisheye and one flat view, and 75% correct with two fisheye views. That is, as expected, fisheye views are far superior."

**B) "Alan derlemeleri kanıt üretemediğini söyler" — bu yanlış.** Alanın kanonik derlemesi:
Cockburn, Karlson & Bederson, "A Review of Overview+Detail, Zooming, and Focus+Context Interfaces", *ACM Computing Surveys* 41(1), 2009.
URL (tam metin): https://www.microsoft.com/en-us/research/wp-content/uploads/2008/01/cockburn-ComputingSurveys09.pdf

§8 (sonuç) ham alıntı:
> "Schaffer et al. (1996) showed that hierarchical fisheye views outperformed full-zoom techniques, but it remains unclear whether an alternative implementation of zooming (continuous rather than full) would have defeated fisheye views"

§7.2.8 ham alıntı (Baudisch ve ark. 2002 hakkında):
> "The focus+context screen was faster (by up to 56%) in all tasks, and they attributed the difference to the costs of switching between views when using overview+detail or zooming."

§7.2.7 ham alıntı (DateLens, Bederson ve ark. 2004):
> "showed that the fisheye allowed improved performance of complex tasks, but little difference for simple ones"

Derleme "kanıt yok" demiyor; **"kanıt var ama göreve bağlı ve karıştırıcı değişkenlerle yüklü"** diyor. Ham alıntı (§8):
> "The current state of research fails to provide clear guidelines, despite a recent surge in empirical analysis of the techniques' effectiveness."

**İddiayı destekleyen taraf (dürüst bildirim):** Aynı derleme Nekrasovski ve ark. 2006'yı da aktarıyor — *"Contrary to their predictions, pan and zoom was significantly faster than the focus+context technique"* (rubber-sheet, ağaç gezinme) — ve Donskoy & Kaptelinin 1997'de zoom fisheye'ı geçmiş. Yani literatür bölünmüş; iddianın mutlak biçimi ("yavaştır", "kanıt üretemedi") çürük.

---

## İDDİA 10 — "Overview panelinin görev süresine ölçülmüş katkısı yoktur; kullanıcı algısı ile ölçüm ayrışır."
**Karar: ÇÜRÜDÜ** (AS-OF 2026-08-29)

**Karşı-kanıt A:** Beard & Walker, "Navigational Techniques to Improve the Display of Large Two-Dimensional Spaces", *Behaviour & Information Technology* 9(6):451-466, 1990 (UNC TR 89-042).
URL (tam metin): https://techreports.cs.unc.edu/papers/89-042.pdf

Tasarım: 3×2 (gezinme tekniği: roam / zoom / scroll × harita penceresi: var / yok), denek-içi; **bağımlı değişken "error-free response time"**; uyaran 280 kelimelik sözlük ağaçları, ekranda aynı anda ~15 düğüm. n=6.
Ham alıntı (Task Two, Results):
> "Several of the results are significant: the use of a map window was found to be significantly better than without (99.5% confidence); both the roam technique and the roam-and-zoom technique were found to be significantly better than scroll bars (99.5% confidence and 99.5% confidence, respectively)."
ANOVA tablosu: sütun (harita penceresi) F=**31,96**, F₀,₀₀₅=7,88 → aşıyor, yani **p<.005**.

**Karşı-kanıt B:** Ghosh & Shneiderman, "Zoom-Only Vs Overview-Detail Pair: A Study in Browsing Techniques as Applied to Patient Histories", HCIL TR 99-12, 1999 — Cockburn ve ark. 2009 derlemesinin §7.2.2'sinden birebir aktarım:
> "In directly comparing overview+detail and zooming interfaces, Ghosh and Shneiderman (1999) analysed task completion times for tasks that involved extracting medical information from two versions of the Lifelines system (Plaisant et al. 1996). The overview+detail interface allowed tasks to be completed more quickly."
(Bu ikincil aktarımdır — birincil TR bu koşumda çekilmedi; bayraklıdır.)

**İddiayı destekleyen taraf:** Hornbæk, Bederson & Plaisant 2002 (harita gezinme) ve Nekrasovski ve ark. 2006 (ağaç gezinme) overview'ün süreye katkısı olmadığını, ancak öznel puanlarda tercih edildiğini buldu — iddianın "algı/ölçüm ayrışması" kısmı bu iki çalışma için doğrudur. Fakat "ölçülmüş katkısı YOKTUR" mutlak hükmü, Beard & Walker 1990 karşısında çürüktür.

**Sınırlar:** Beard & Walker'da n=6 (çok küçük), uyaran kelime ağacı (graf değil), tarih 1990 (donanım/etkileşim çok farklı).

---

## İDDİA 11 — "Yol-bulma tutarlı biçimde düğüm-bağ lehinedir; büyük-n çalışmada düğüm-bağ topoloji sorularında matrisi geçer."
**Karar: DARALDI** (AS-OF 2026-08-29)

**A) "Tutarlı biçimde düğüm-bağ lehine" — iddianın kaynağı kendi içinde çelişiyor.**
Ghoniem ve ark. 2005 (URL yukarıda). Abstract ham alıntı — iddiayı destekler:
> "Only path finding is consistently in favor of node-link diagrams throughout the evaluation."
Fakat §3.5.7 ham alıntı — iddiayı yalanlar:
> "The matrix-based representation performs very poorly for this task except for very dense graphs where it outperforms the node-link representation... This fact is confirmed by the percentage of correct answers which towers at 95% for the matrix-based representation against 85% for node-links when dealing with large link density."
ve
> "For large graphs, every other user answers correstly using both representations with a statistically insignificant lead in favor of matrices."
(son alıntıda kaynaktaki yazım aynen korundu)

Yani yüksek yoğunlukta matris **%95 vs %85** ile öndedir, 100 düğümde ise matrisin (anlamsız) bir üstünlüğü vardır. "Tutarlı" ifadesi yalnızca küresel istatistiksel modelde geçerlidir, koşul-bazında değil.

**B) "Büyük-n etkileşimli çalışmada düğüm-bağ topolojide matrisi geçer" — 5-3, temiz galibiyet değil.**
Okoe, Jianu & Kobourov 2019, *IEEE TVCG* 25(10):2940-2952 (URL yukarıda), 864 çevrimiçi katılımcı, 258 ve 332 düğümlü graflar. Ham alıntı:
> "NL outperforms AM for questions about graph topology (e.g., 'Select all neighbors of node,' 'Is a highlighted node connected to a named node?'). Of 10 such tasks in two datasets, participants who used the node-link diagram were more accurate in 5 and less accurate in 3. AM outperforms NL in 2 of 4 tasks which tested the ability of the participants to identify and compare node groups or clusters."

Ve yol görevlerinde SÜRE matris lehine — ham alıntı:
> "AM also outperformed NL in terms of time in T 5 and T 10 but we believe that those results are anomalous"
> "The average time of participants performing path tasks (T 10) using AM in our first study is significantly smaller than that for NL. The results are reversed in study 2."

**Daralma:** İddia doğruluk-ağırlıklı ve ortalama-üzerinden doğrudur; "tutarlı" ve "geçer" sözcükleri, yoğunluk yüksekken ve süre ölçütünde yanlıştır. Ayrıca ortak-komşu görevlerinde (T4, T12) matris düğüm-bağı geçmiştir.

---

## İDDİA 12 — "Kişisel bilgi-deposu / not-grafı (Obsidian-Roam sınıfı) bağlamında kontrollü bir graf-görselleştirme deneyi YOKTUR."
**Karar: ÇÜRÜTEMEDİM (arama yapıldı, çürütecek kanıt bulunamadı)** (AS-OF 2026-08-29)

Yapılan sorgular:
1. `Obsidian Roam "graph view" personal knowledge management controlled user study evaluation note-taking network visualization experiment` (WebSearch)
2. `"knowledge graph" OR "linked notes" note-taking app graph visualization empirical study participants CHI evaluation "personal knowledge"` (WebSearch)
3. OpenAlex tam-metin arama API: `personal knowledge management graph view note-taking user study` (81.048 sonuç, hiçbiri konu-ilgili değil)
4. OpenAlex: `Obsidian Roam note graph visualization evaluation experiment` (14 sonuç; en yakın aday **"Atlas: An Interactive Graph-Based File System for Enhanced Document Relationship Visualization", 2025** — kontrollü deney içerip içermediği doğrulanamadı, atıf sayısı 1, tam metin bu koşumda çekilemedi)
5. OpenAlex: `backlinks note-taking network visualization controlled experiment participants` (42 sonuç, ilgisiz)

Dönen sonuçların tamamı ürün incelemesi, blog yazısı veya ilgisiz akademik iş. **Uydurma kaynak vermiyorum.** Adayın (Atlas 2025) doğrulanması sonraki tur için açık kalır.

---

## İDDİA 13 — "Tam-graf görünümü ↔ odak-alt-graf görünümünü DOĞRUDAN karşılaştıran kontrollü deney YOKTUR."
**Karar: DARALDI** (AS-OF 2026-08-29)

**Karşı-kanıt:** Lee, Parr, Plaisant, Bederson, Veksler, Gray & Kotfila, "TreePlus: Interactive Exploration of Networks with Enhanced Tree Layouts", *IEEE TVCG* 12(6):1414-1426 (InfoVis'06).
URL (tam metin, HCIL TR 2006-04): http://www.cs.umd.edu/hcil/trs/2006-04/2006-04.pdf

Tasarım: n=**28**, denek-içi, 6 görev, 2 yoğunluk. Uyaran: **200 düğüm**, 900 kenar (%15 yoğunluk) ve 3.600 kenar (%30 yoğunluk). Koşullar: **TreePlus** (bir kökten başlayıp artımlı genişleyen, ağaç-yerleşimli **odak-alt-graf** görünümü + komşu önizleme paneli) ↔ **GraphPlus** (TouchGraph yerleşimli klasik düğüm-bağ arayüzü).

Abstract ham alıntı:
> "user study with 28 participants comparing TreePlus with a traditional graph interface for six tasks. In general, the advantage of TreePlus over the traditional interface increased as the density of the displayed data increased."

Sonuç ham alıntı:
> "significant advantages for the TreePlus interface for Adjacency, Accessibility, and Connectivity tasks"
ANOVA tablosundan örnek Interface ana etkileri: F(1,27)=38,952 (**), F(1,27)=14,867 (**), F(1,27)=59,565 (**) — (** = p<.01, kaynak notasyonu).

**Daralma nedeni (dürüst bildirim):** GraphPlus'ın yerleşim motoru da artımlı çalışır — ham alıntı:
> "This algorithm was chosen because it was designed for incremental exploration"
Dolayısıyla bu, **saf statik tam-graf** ↔ odak-alt-graf kıyası değil; ağaç-tabanlı odak görünümü ↔ graf-tabanlı (artımlı yeteneği olan) tam görünüm kıyasıdır. İddia "hiçbir doğrudan kıyas yok" biçiminde yanlıştır; "saf tam-graf temel koşullu kıyas yok" biçiminde ayakta kalabilir.

---

## İDDİA 14 — "DOI / odak-alt-graf yaklaşımının kanonik makalesi kontrollü deney içermez, yalnız vaka çalışmasıdır."
**Karar: DARALDI — hangi makalenin 'kanonik' sayıldığına bağlı** (AS-OF 2026-08-29)

**Okuma 1 — kanonik = Furnas 1986 (DOI kavramını icat eden makale): İddia ÇÜRÜK.**
Furnas, "Generalized Fisheye Views", *ACM CHI 1986*, s. 16-23. URL: https://cspages.ucalgary.ca/~saul/581/exer.eps/4furnas86.pdf
§4 ham alıntı — kontrollü deney vardır:
> "To test this we ran an experiment in which 20 subjects were asked to perform a navigation-related task in a large unfamiliar hierarchical structure... Subjects received either two flat views, two fisheye views, or one of each on which to base their decision, and saw a total of 16 pairs in all."
> "We found that people were only 52% correct with two flat views, 64% correct with one fisheye and one flat view, and 75% correct with two fisheye views."
(Not: p-değeri raporlanmamış, süre ölçülmemiş, uyaran botanik taksonomi ağacı.)

**Okuma 2 — kanonik = van Ham & Perer 2009 (DOI'yi graflara taşıyan makale): İddia DOĞRU.**
van Ham & Perer, "'Search, Show Context, Expand on Demand': Supporting Large Graph Exploration with Degree-of-Interest", *IEEE TVCG* 15(6):953-960, 2009. URL (tam metin): https://perer.org/papers/adamPerer-DOIGraphs-InfoVis2009.pdf
§4 başlığı "EVALUATION: LEGAL CITATION NETWORK" — hukuki atıf grafı üzerinde anlatısal vaka çalışması; katılımcı yok, koşul yok, ölçüm yok. §4 sonu ham alıntı:
> "Although this anecdotal evidence should obviously be confirmed through more rigorous evaluation techniques such as long-term field studies (e.g. [16]) with a broad field of actual experts, these initial explorations were encouraging."

**Daralma:** İddia van Ham & Perer 2009 için tamdır; DOI'nin asıl kanonik makalesi olan Furnas 1986 için yanlıştır (n=20'lik kontrollü, fisheye lehine anlamlı fark üreten bir deney içerir).

---

## Yöntem notu (epistemolojik)
- Her karar için **birincil metin** (PDF tam metni ya da yayıncı/kurumsal arşiv abstract'ı) çekildi; ikincil aktarımlar (Ghosh & Shneiderman 1999, Okoe ve ark. 2014) açıkça bayraklandı ve zayıf kanıt sayıldı.
- Rakamların tamamı kaynaktan kopyalandı; **[?] kestirim işareti kullanılmadı çünkü kestirim yapılmadı** — tek türetilmiş sayı oran hesaplarıdır (27,2/8,5=3,2× · 75,77/43,20=%43 · 161,2/101,9=%37) ve türetildiği açıkça yazılmıştır.
- Devil's advocate rolüne rağmen, iddiayı DESTEKLEYEN karşı-bulgular (İddia 4→1 etkisi, İddia 9'da Nekrasovski, İddia 10'da Hornbæk) gizlenmeden raporlandı; antitezin görevi hakikat aramaktır, tarafı kazandırmak değil.
- Bu rapor, aramanın kapsadığı kadarıyla geçerlidir. Bulunamayan kanıt (İddia 12) "yok" anlamına gelmez; "bu sorgularla bulunamadı" anlamına gelir.
