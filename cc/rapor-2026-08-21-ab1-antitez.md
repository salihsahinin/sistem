# AB-1 Antitez Raporu — "Periyodik/Takvimli Skill-Bakımı Gereksizdir" İddiası

**Rol:** S-1b (skill-bakım-antitez, m.40b hedefli refütasyon kolu) · **Tarih:** 2026-08-21 · **Model:** sonnet · **Bağımsızlık notu:** Bu koşum tez raporunu (ab1-tez) OKUMADAN yürütüldü.

**İncelenen iddia (gerekçesiz verildi, m.40b):** "Periyodik/takvimli skill-bakım turu GEREKSİZDİR: kullanım-anı sinyalleri (koşum sapması, eval FAIL, tetik ıskası) yeterlidir; takvimli bakım ölü-ağırlık (bakım tiyatrosu) üretir ve bakım maliyeti kazancı yer."

## Yöntem notu (dürüstlük beyanı)
LLM-ajan skill/prompt varlıklarının bakımına ÖZGÜ olarak "periyodik vs olay-tetikli" karşılaştırmasını doğrudan konu alan bir çalışma bulunamadı. Aşağıdaki tüm bulgular ANALOJİKTİR — komşu alanlardan (endüstriyel güvenilirlik-merkezli bakım/RCM, MLOps model yeniden-eğitimi, yazılım dokümantasyon bakımı, güvenlik/izleme alarm sistemleri, CI/regresyon testi) devşirilmiştir. Doğrudan aktarılabilirlik SINIRLIDIR, her bulguda ayrıca belirtildi.

## Bulgular — iddia LEHİNE

1. **D** — Gereksiz/erken planlı bakım müdahalesinin arıza oranını GEÇİCİ yükselttiği ("maintenance-induced failures") — https://accendoreliability.com/no-89-percent-of-failures-are-not-random/ (WebFetch ile doğrudan açıldı, okundu). Aynı kaynak, RCM literatüründe sık atıfta bulunulan "%89 rastgele arıza" rakamının veri-kalitesi sorunları yüzünden ABARTILMIŞ olabileceğini savunuyor — bu spesifik rakamı ayrıca **X** işaretliyorum (iç-tartışmalı).
   Değerlendirme: iddiayı KISMEN destekler (gereksiz bakım net zarar verebilir); rakamsal büyüklük belirsiz.

2. **K** — Nowlan & Heap Reliability-Centered Maintenance (1978) bulgusu: karmaşık uçak bileşenlerinin çoğunluğu (ikincil kaynaklara göre ~%77-89) yaşa-bağlı aşınma paterni GÖSTERMEZ; bu nedenle yaş/takvim-bazlı planlı yeniden-yapım bu bileşenlerin arıza oranını iyileştirmiyor. Bu bulgu havacılıkta takvimli bakımdan durum-izlemeye (condition monitoring) geçişi tetikledi. Birincil rapor iki ayrı WebFetch denemesinde de OKUNAMADI (PDF metin çıkarımı başarısız): https://www.omdec.com/wikifiles/nowlanHeap.pdf, https://www.nasa.gov/wp-content/uploads/2023/06/nasa-rcmguide.pdf — bulgu yalnız ikincil/çapraz kaynaklarla (worktrek.com, accendoreliability.com, researchgate figür sayfası) doğrulandı, bu yüzden D değil K.
   Değerlendirme: iddiayı GÜÇLÜ destekler; ancak fiziksel ekipmana özgü, LLM-skill alanına aktarımı tartışmalı.

3. **K** — Condition-based (olay/durum-tabanlı) bakımın time-based (takvimli) bakıma göre maliyet üstünlüğü: sektör kaynakları (spartakustech.com, tractian.com, rasmech.com) ve bir ScienceDirect karşılaştırmalı çalışma özeti, olay-tabanlı yaklaşımların maliyeti azalttığını bildiriyor — ancak kaynaklar arası rakam ÇOK TUTARSIZ (%8 ile %10× arası farklı iddialar), bu yüzden büyüklük **X**.
   Değerlendirme: YÖN destekler, BÜYÜKLÜK güvenilmez.

4. **K** — MLOps model yeniden-eğitim stratejileri meta-analizi (ResearchGate özeti; tam metin WebFetch'te HTTP 403 ile engellendi, yalnız arama motoru sentezi üzerinden görüldü): periyodik yeniden-eğitim ortalama %4.1 doğruluk iyileştirmesi sağlarken tetik-tabanlı %6.7, adaptif %9.3 sağlıyor; ayrıca periyodik yeniden-eğitimin "gereksiz yeniden-eğitim VEYA gecikmiş adaptasyon" ürettiği belirtiliyor.
   Değerlendirme: iddiayı DOĞRUDAN ve NİCEL destekler; alan (ML sisteminin periyodik bakımı) incelenen konuya EN YAKIN analoji. Kaynak tam okunamadığı için K, tekrar-doğrulama önerilir.

5. **K** — Bakım denetimi (maintenance audit) etkinliği: sektör kaynakları (fiixsoftware.com, manwinwin.com türü), önemli arıza/ramak-kala olayıyla TETİKLENEN plansız denetimlerin, planlı/takvimli denetimlerin KAÇIRDIĞI sistemik sorunları ortaya çıkarma eğiliminde olduğunu bildiriyor.
   Değerlendirme: "olay-tetikli > takvimli" yönünü destekler; kaynaklar akademik değil sektör-blog düzeyinde, yetkesi zayıf.

6. **K** — Alarm yorgunluğu (alert fatigue) literatürü (ScienceDirect makale özeti, LogicMonitor, Vectra): sık/düşük-değerli periyodik uyarılar habitüasyon (duyarsızlaşma) yaratıyor, operatörün gerçek sorunu fark etme kapasitesini düşürüyor; olay-tetikli + akıllı filtreleme öneriliyor.
   Değerlendirme: DOLAYLI destek — analoji burada "periyodik bakım turu" değil "periyodik/sık UYARI"; iddianın "bakım tiyatrosu" (rutinleşip işe yaramaz hale gelme) kısmına destek, "maliyet kazancı yer" kısmına doğrudan değil.

## Karşı-yönde / nötr bulgular (dürüstlük için ayrıca not edildi — iddiayı zayıflatıyor)
- **K** — CI/CD regresyon testi araştırması (Elbaum ve ark., FSE 2014 + Google ampirik çalışma sentezi): periyodik test "stabil/legacy sistemlerde" hâlâ DEĞERLİ bulunuyor; sürekli/her-commit yaklaşım yalnız AKTİF geliştirmede üstün gösteriliyor. Bu, iddianın "periyodik HER ZAMAN gereksizdir" (mutlak) kısmını ZAYIFLATIYOR — bağlama-bağlılık bulgusu var.
- **K** — Yazılım dokümantasyonu bakım pratiği (glitter.io, readytoday.co.uk): "dokümantasyon takvime göre değil sistem değiştiğinde güncellenmeli" denirken, aynı kaynaklar HİBRİT model öneriyor (periyodik gözden geçirme + olay-tetikli güncelleme birlikte) — SAF event-driven'ı değil, tamamlayıcılığı savunuyor.
- **X** — Bulgu 1'deki kaynağın kendisi, RCM alanının en çok atıfta bulunulan istatistiğini (%89 rastgele arıza) sorguluyor — iddiayı destekleyen literatürün kendi içinde de anlaşmazlık var.

## Cevaplanamayanlar
- LLM ajan skill/prompt varlıkları için ÖZEL OLARAK "periyodik bakım turu vs olay-tetikli bakım" karşılaştırmasını konu alan bir akademik çalışma veya vaka analizi bulunamadı — bu koşumun kapsamında (S-1b, m.40b) buna dair arama yapılmadı çünkü tez tarafının (S-1a) inceleme alanı; bu antitez yalnız komşu-alan analojileriyle çalıştı.
- "Bakım tiyatrosu" (maintenance theater) yazılım/AI bağlamında yerleşik bir akademik terim olarak bulunamadı; yalnız fiziksel bakım endüstrisi denetim (audit) bağlamında yakın kavramlar bulundu.
- Nowlan & Heap'in birincil 1978 raporu iki WebFetch denemesinde de OKUNAMADI (PDF metin çıkarımı başarısız oldu, ikinci denemede model kendi ön-eğitim bilgisine dayandığını AÇIKÇA belirtti) — bu yüzden D değil K etiketlendi.
- MLOps meta-analiz kaynağı ResearchGate 403 ile erişime kapalı — tam metin doğrulanamadı, yalnız arama motoru sentezi kayıtta.

## F2 Destek-Tablosu (hangi iddia bileşeni hangi kaynağa dayanıyor)
| # | İddia bileşeni | Destekleyen/zayıflatan bulgu | Etiket | Kaynak (URL) |
|---|---|---|---|---|
| 1 | "kullanım-anı sinyalleri yeterlidir" | MLOps: tetik-tabanlı/adaptif > periyodik (doğruluk %) | K | ResearchGate meta-analiz (arama sentezi, tam metin 403) |
| 2 | "takvimli bakım ölü-ağırlık üretir" | RCM: bileşenlerin çoğu yaşa-bağlı değil, takvimli yeniden-yapım işe yaramıyor | K | worktrek.com / accendoreliability.com / researchgate figür |
| 3 | "takvimli bakım ölü-ağırlık üretir" | Gereksiz bakım arıza oranını geçici yükseltir (maintenance-induced failure) | D | accendoreliability.com/no-89-percent-of-failures-are-not-random |
| 4 | "bakım maliyeti kazancı yer" | CBM/olay-tabanlı maliyet tasarrufu (yön var, büyüklük tutarsız) | K/X | spartakustech.com, tractian.com, rasmech.com, ScienceDirect özeti |
| 5 | "bakım tiyatrosu" | Planlı denetimler sistemik sorunu kaçırıyor, olay-tetikli denetim yakalıyor | K | fiixsoftware.com, manwinwin.com |
| 6 | "bakım tiyatrosu" (dolaylı analoji) | Alarm yorgunluğu: sık periyodik sinyal duyarsızlaştırır | K | ScienceDirect / LogicMonitor / Vectra |
| 7 | ZAYIFLATICI karşı-kanıt | Periyodik test, stabil/legacy sistemde hâlâ değerli | K | Elbaum FSE'14 + Google ampirik (sentez) |
| 8 | ZAYIFLATICI karşı-kanıt | Dokümantasyon bakımında HİBRİT (periyodik+olay-tetikli) öneriliyor | K | glitter.io, readytoday.co.uk |

## Genel değerlendirme (S-1b sonucu)
**İddia lehine bulgu sayımı:** D = 1, K = 6 (lehine eğilimli), X = 2 (iç-tartışmalı/belirsiz büyüklük). Ayrıca 2 adet ZAYIFLATICI (karşı-yönde) K-bulgu kayda geçti.

Toplamda literatür iddianın YÖNÜNÜ (olay/sapma-tetikli sinyaller takvimli bakımdan daha isabetli ve daha az israflı) orta-güçte destekliyor — en somut ve nicel destek MLOps yeniden-eğitim meta-analizinden geliyor (bulgu 4), ki bu alan incelenenlere en yakın analoji. Ancak literatür iddianın MUTLAK biçimini ("GEREKSİZDİR", tam ret) TAM DESTEKLEMİYOR: CI/regresyon testi ve dokümantasyon-bakımı kaynakları HİBRİT modeli (düşük-maliyetli periyodik arka-plan + olay-tetikli asıl mekanizma) öneriyor, saf periyodiğin tamamen kaldırılmasını değil. Hiçbir bulgu doğrudan LLM-skill/prompt bakımı alanından değil — hepsi analoji, aktarım riski açık.

## Jarvis'e uygulanabilirlik
- Mevcut kanon mekanizması (m.43 pencereli sayaç N=5/W=90 gün + Karar 51 eşik kuralı: n≥10 → medyan-band, 2× sapma raporu) ZATEN kısmen sapma-tetikli bir yapı — iddia ile ÖRTÜŞÜYOR; saf "takvim" bakımı bunun üstüne binmiyor.
- Bulgu 4 (MLOps) + zayıflatıcı bulgu 7 (CI/regresyon) birlikte okunduğunda: literatür "SAF takvimli" YERİNE "sapma-tetikli birincil + düşük-maliyetli periyodik arka-plan kontrolü" hibridini destekliyor — iddianın "TAMAMEN GEREKSİZ" hükmünden çok "TEK BAŞINA yetersiz, ek maliyet-fayda gerekçesi olmadan eklenmemeli" hükmünü güçlendiriyor.
- Bu bulgular G-1 (Carvis + Salih masası) tasarım kararına HAM MADDE olarak sunulabilir; tasarım kararının kendisi bu raporun kapsamı DIŞINDADIR (m.40b, kapsam_disi: sentez/hakemlik Carvis işi).

---
**Halüsinasyon disiplini notu:** Bu raporda geçen her iddia yukarıdaki F2 tablosuyla eşlenmiştir; hiçbir URL okumadan künye yazılmadı (2 kaynak açık biçimde "okunamadı" diye işaretlendi: NASA/omdec PDF'leri, ResearchGate 403). Etiketsiz iddia yoktur.
