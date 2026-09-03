# İB-77 — Atlas Görselleştirme Araştırması — Aile A (KURAM + ÖĞRENME) — TEZ

## 0. KÜNYE
- Ajan: Atlas Aile-A (TEZ, karar vermez)
- AS-OF: 2026-09-03
- Açılan kaynak sayısı (fiilen WebFetch ile açılan, D-etiketli): 4 — (1) Wikipedia "Misleading Graph" (lie factor formülü), (2) educationaltechnology.net "Mayer's Principles of Multimedia Learning", (3) data-to-viz.com (karar ağacı), (4) cmap.ihmc.us "Theory of Concept Maps" (Novak/Ausubel)
- Başarısız/engellenen açma denemeleri: Munzner'ın orijinal makalesi (cs.ubc.ca PDF — içerik boş/şifreli döndü; ikinci URL 404), Semantic Scholar sayfası (boş içerik döndü), Juniata "Graphical Integrity" sayfası (403 Forbidden) — bu üçü yalnız arama-özetiyle (K) desteklenmiştir.

## 1. BULGULAR
1. Tufte'nin "lie factor" formülü = (grafikte gösterilen etkinin büyüklüğü) / (veride gerçekte olan etkinin büyüklüğü); |1.0'den sapma| arttıkça grafik yanıltıcı sayılır. Kanıt: fiilen açılan Wikipedia sayfası. https://en.wikipedia.org/wiki/Misleading_graph — D — AS-OF 2026-09-03
2. Cleveland & McGill (1984) algısal doğruluk sıralaması: pozisyon (ortak eksen) > pozisyon (ayrı eksen) > uzunluk > yön > açı > eğim > alan > hacim > renk-tonu(shading) > doygunluk(saturation). Kanıt: arama özeti, birincil kaynağa (orijinal 1984 makalesi) erişilmedi. https://www.researchgate.net/publication/6062457 — K — AS-OF 2026-09-03
3. Munzner'ın "nested model"i dört katmandan oluşur: domain (alan durumu) → abstraction (veri/görev soyutlaması) → idiom (görsel kodlama/etkileşim tasarımı) → algorithm (uygulama); her katmanda ayrı bir geçerlilik tehdidi vardır (yanlış ihtiyaç anlama / yanlış şey gösterme / kodlama işe yaramıyor / kod yavaş). Kanıt: iki ayrı arama-özeti örtüşüyor, ancak orijinal makale (Munzner, InfoVis 2009) fiilen açılamadı (PDF boş/şifreli, ikinci link 404). https://www.semanticscholar.org/paper/e8cfef98279aabd43f65d465b304345aec15d9bb — K — AS-OF 2026-09-03
4. Mayer'in çoklu-ortam öğrenme ilkeleri (12 ilke) fiilen açılan sayfada listelendi: coherence, signaling, redundancy, spatial contiguity, temporal contiguity, segmenting, pre-training, modality, multimedia, personalization, voice, image. Kanıt: https://educationaltechnology.net/mayers-principles-of-multimedia-learning/ — D — AS-OF 2026-09-03
5. Coherence ilkesi 23/23 deneyde, spatial contiguity 22/22 deneyde, redundancy 16/16 deneyde desteklenmiş; medyan etki büyüklükleri sırasıyla ~0.86, ~1.10, ~0.86 olarak raporlanmış. Kanıt: yalnız arama-özeti (Cambridge Handbook of Multimedia Learning bölüm özeti), birincil tabloya erişilmedi. https://www.cambridge.org/core/books/... — K — AS-OF 2026-09-03
6. Sweller'in bilişsel yük kuramı üç yük türü tanımlar: intrinsic (görev zorluğu × ön-bilgi etkileşimi), extraneous (sunum tasarımından kaynaklanan, azaltılabilir), germane (yeni bilginin uzun-vadeli belleğe bağlanması için harcanan kapasite). Kanıt: arama-özeti, birincil makaleye girilmedi. https://link.springer.com/article/10.1007/s10648-010-9128-5 — K — AS-OF 2026-09-03
7. "Worked example effect" — çözülmüş örnek üzerinden çalışmanın, problemi sıfırdan çözmeye göre eleman-etkileşimini (element interactivity) azaltarak extraneous yükü düşürdüğü ve bunun bilişsel yük kuramının en güçlü etkilerinden biri sayıldığı raporlanıyor. Kanıt: arama-özeti. https://thedecisionlab.com/reference-guide/psychology/cognitive-load-theory — K — AS-OF 2026-09-03
8. Novak'ın kavram haritası (concept map) teorisi Ausubel'in "anlamlı öğrenme" (meaningful learning) kuramına dayanır: öğrenme, yeni kavramların var olan kavram/önerme çerçevelerine asimile edilmesiyle gerçekleşir; haritalar en genel kavram üstte olacak şekilde hiyerarşik kurulur; kaynak sayfa concept mapping'in öğrenme kazanımını ve uzun-vadeli bilgi tutulumunu artırdığını raporluyor (spesifik efekt büyüklüğü sayfada verilmedi). Kanıt: fiilen açılan sayfa. https://cmap.ihmc.us/docs/theory-of-concept-maps — D — AS-OF 2026-09-03
9. Data-to-viz.com karar ağacı içerik sınıfını dört ana eksene ayırıyor — sayısal (numeric: histogram/scatter/bubble), kategorik (bar/treemap/sunburst), kategorik+sayısal (violin/line/sankey), coğrafi (choropleth/hexbin/connection map) ve ağ (network/chord/edge-bundling) — ve her eksen için değişken sayısına göre alt-öneri veriyor. Kanıt: fiilen açılan sayfa. https://www.data-to-viz.com/ — D — AS-OF 2026-09-03
10. FT (Financial Times) Visual Vocabulary posteri grafik türlerini 9 kategoriye ayırır: deviation, correlation, ranking, distribution, change-over-time, magnitude, part-to-whole, spatial, flow; her kategori "ne anlatmak istiyorsun" sorusuna göre seçilir. Kanıt: arama-özeti (GitHub reposu ve poster PDF'i doğrudan açılmadı). https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary — K — AS-OF 2026-09-03

## 2. İÇERİK-SINIFI → GÖRSEL-TÜR KARAR TABLOSU TASLAĞI

| İçerik sınıfı | Birincil görsel tür | Alternatif | Gerekçe kaynağı |
|---|---|---|---|
| Sayısal dağılım (tek değişken) | Histogram | Kutu grafiği, yoğunluk grafiği | data-to-viz.com (D) |
| Sayısal ilişki (2 değişken) | Scatter plot | Bağlı saçılım, alan grafiği | data-to-viz.com (D); Cleveland-McGill pozisyon-üstünlüğü (K) |
| Kategori karşılaştırma (magnitude/ranking) | Çubuk grafik (bar) | Lollipop, waffle | FT Visual Vocabulary "ranking/magnitude" (K); Cleveland-McGill: uzunluk üstün, açı/hacim zayıf |
| Zaman serisi | Çizgi grafik | Alan grafik, streamgraph | FT "change over time" (K); data-to-viz.com (D) |
| Parça-bütün / hiyerarşi (sayısal) | Treemap / sunburst | Dairesel paketleme (circle packing) | data-to-viz.com (D); FT "part-to-whole" (K) |
| Sapma / referans noktasından fark | Diverging bar | Slope chart | FT "deviation" kategorisi (K) |
| Coğrafi/bölgesel değer | Choropleth harita | Hexbin, kartogram | data-to-viz.com (D) |
| Akış / bağlantı miktarı | Sankey diyagramı | Chord diyagramı | data-to-viz.com (D); FT "flow" (K) |
| **Süreç / prosedür (metin, sayısal değil)** | Akış (flow) diyagramı | Swimlane diyagramı | Munzner "idiom" seçimi görev-tipine göre (K); genel görselleştirme pratiği |
| **Kavramlar-arası ilişki (metin)** | Concept map / knowledge graph | Ağ diyagramı | Novak concept-map teorisi (D) |
| **Karşılaştırma (metin, nitel)** | Tablo / matris | Küçük-çoklu (small multiples) | Munzner "what" abstraction — karşılaştırma görevi tablo/matrisle en dolaysız kodlanır (K) |
| **Hiyerarşi (metin, kavramsal)** | Ağaç diyagramı (tree) | Dendrogram, indented outline | Genel pratik; Novak hiyerarşik kavram haritası ilkesiyle örtüşür (D) |
| **Zaman akışı (metin, olaylar)** | Timeline | Gantt-benzeri şerit | FT "change over time" ailesiyle örtüşen mantık (K) |
| **Mekanizma / nasıl-çalışır (metin)** | Şema (labeled diagram) | Kesit/patlatılmış şema | Mayer çoklu-ortam + dual-coding mantığı: metin+görsel birlikte (D/K karışık, bkz. m.3) |

Not: (3)-(6) satırları "metin açıklaması için görsel tür" sorusuna (görev tarifi madde 3) doğrudan literatür-kanıtlı bir sınıflandırma bulunamadı — bunlar Munzner'ın görev-soyutlaması mantığından ve genel enformasyon-tasarım pratiğinden TÜRETİLMİŞTİR, birebir kaynak-doğrulanmış bir tablo değildir; açık soru olarak madde 6'da işaretlendi.

## 3. ÖĞRENME-ÖZEL KURALLAR (≤8)
1. Coherence: alakasız görsel/metin/ses öğeleri çıkar. Kaynak: educationaltechnology.net (D).
2. Signaling: ana öğeleri ok/vurgu ile işaretle. Kaynak: educationaltechnology.net (D).
3. Redundancy: aynı bilgiyi hem sesli anlatım hem ekran metniyle aynı anda verme. Kaynak: educationaltechnology.net (D).
4. Spatial contiguity: ilgili metin ve görseli birbirine yakın yerleştir. Kaynak: educationaltechnology.net (D).
5. Temporal contiguity: anlatım ve ilgili animasyonu eşzamanlı sun. Kaynak: educationaltechnology.net (D).
6. Segmenting/pre-training: karmaşık görseli öğrenci-kontrollü küçük parçalara böl, temel kavramı önden ver. Kaynak: educationaltechnology.net (D).
7. Worked-example etkisi: yeni/karmaşık bir mekanizma için önce çözülmüş örnek göster, sonra genelleştir — extraneous yükü azaltır. Kaynak: thedecisionlab.com (K).
8. Concept-map / hiyerarşik yapı: en genel kavram üstte, ilişkiler etiketli okla — kavramlar-arası ilişki anlatımında metne ek olarak bu yapı kullanılmalı. Kaynak: cmap.ihmc.us (D).

## 4. METRİK ADAYLARI
- **Lie factor** (Tufte): |grafik-etkisi / veri-etkisi|; 0.95–1.05 dışı = çarpıtma sinyali. Kaynak: Wikipedia (D).
- **Data-ink ratio** (Tufte): veri-taşıyan mürekkep / toplam mürekkep — düşükse gereksiz süsleme var. Kaynak: arama-özeti (K, birincil kaynağa 403 nedeniyle girilemedi).
- **Algısal doğruluk sıralaması** (Cleveland-McGill): kodlama türünün (pozisyon/uzunluk/açı/alan/renk) doğru-okunabilirlik sırasındaki yeri — görsel türü bu sıraya göre seçilir/denetlenir. Kaynak: arama-özeti (K).
- **Efekt büyüklüğü (Cohen's d benzeri)**: Mayer ilkelerinin öğrenme kazanımına etkisi ~0.86–1.10 medyan olarak raporlanıyor — görsel tasarım kararının öğrenmeye etkisini ölçmek için kullanılabilir. Kaynak: arama-özeti (K).
- **Bilişsel yük ölçümü**: NASA-TLX benzeri öz-bildirim ölçekleri veya göz-izleme (eye-tracking) fizyolojik ölçümleri — arama sonucunda başlık düzeyinde geçti (PMC makalesi), içerik açılmadı. Kaynak: arama-özeti (K), doğrulanmadı [?].

## 5. İDDİA LİSTESİ (gerekçesiz, antitez için)
1. Lie factor = grafik-etkisi/veri-etkisi; 1'den sapma yanıltıcılık göstergesidir.
2. Cleveland-McGill sıralamasında pozisyon en doğru, alan/hacim/renk-doygunluğu en az doğru kodlama biçimleridir.
3. Munzner'ın nested modeli dört katmanlıdır (domain/abstraction/idiom/algorithm) ve her katmanda ayrı bir geçerlilik tehdidi vardır.
4. Mayer'in coherence, signaling, redundancy, spatial contiguity, temporal contiguity ilkeleri deneysel olarak desteklenmiştir.
5. Coherence ilkesinin medyan etki büyüklüğü ~0.86'dır.
6. Spatial contiguity ilkesinin medyan etki büyüklüğü ~1.10'dur.
7. Sweller'in bilişsel yük kuramı üç yük türü ayırır: intrinsic, extraneous, germane.
8. Worked-example etkisi extraneous yükü azaltarak öğrenmeyi iyileştirir.
9. Novak'ın kavram haritaları Ausubel'in anlamlı öğrenme kuramına dayanır ve hiyerarşik (en genel kavram üstte) kurulur.
10. Concept mapping'in öğrenme kazanımını ve uzun-vadeli bilgi tutulumunu artırdığı raporlanmıştır.
11. Data-to-viz.com karar ağacı içerik tipini sayısal/kategorik/kategorik+sayısal/coğrafi/ağ olarak beş eksende sınıflar.
12. FT Visual Vocabulary grafik türlerini 9 kategoriye ayırır: deviation, correlation, ranking, distribution, change-over-time, magnitude, part-to-whole, spatial, flow.
13. Data-ink ratio'nun düşük olması gereksiz görsel süslemeyi (chartjunk) işaret eder.
14. Metin-tabanlı (sayısal olmayan) süreç anlatımı için akış diyagramı, kavram-ilişkisi için concept map, karşılaştırma için tablo/matris, hiyerarşi için ağaç diyagramı, zaman için timeline uygun görsel türlerdir.

## 6. AÇIK SORULAR / bulunamayanlar
- Munzner'ın orijinal "A Nested Model for Visualization Design and Validation" (InfoVis 2009) makalesine bu oturumda erişilemedi (PDF içerik boş döndü, ikinci URL 404, Semantic Scholar sayfası boş) — dört katmanın tam terminolojisi ve doğrulama yöntemleri yalnız ikincil kaynaklarla (K) doğrulandı, birincil metinle teyit edilmedi.
- Tufte'nin "Graphical Integrity" ilkelerinin tam listesine (Juniata sayfası 403 verdi) bu oturumda erişilemedi.
- Cleveland-McGill'in 1984 orijinal makalesine (Science dergisi) erişilmedi; sıralama yalnız ikincil kaynaklarla doğrulandı.
- Wilkinson'ın "Grammar of Graphics"i, Bertin'in görsel değişkenleri (retinal variables) ve Chart Chooser tabloları (örn. Andrew Abela / Extreme Presentation) bu oturumda HİÇ ARANMADI — bütçe (20 çağrı) yetmedi; bu üçü sonraki tur için AÇIK bırakılmalı.
- Madde 3'teki (metin açıklaması → görsel tür) satırların çoğu literatürden doğrudan bir kaynakla değil, Munzner'ın görev-soyutlama mantığından türetildi — bu sınıf için özel, adı konmuş bir akademik kaynak bulunamadı; "bulunamadı" olarak kayda geçirilir.
- Bilişsel yük ve öğrenme-kazanımı ölçüm araçlarının (NASA-TLX, göz-izleme metrikleri) görselleştirme bağlamındaki spesifik kullanımı doğrulanmadı [?].
