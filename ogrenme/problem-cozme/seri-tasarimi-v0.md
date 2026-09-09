# Problem Çözme Eğitim Serisi — Tasarım v0 (2026-09-08)

> **v1'e GEÇİLDİ (2026-09-09, Salih kararı):** güncel tasarım `seri-tasarimi-v1.md`; bu dosya arşiv-pointer (m.8). Revizyon gerekçesi `raporlar/2026-09-09-problem-cozme-ai-cagi-atlas.md` §3.

> **Ne bu:** Salih'in problem çözme yeteneğini lisans düzeyinden ileri seviyeye taşımak için 8 temel başlıkta, seviyeli (L0→L3) eğitim serisi listesi. Her seviyenin **kaynağı, pratik biçimi ve ölçülebilir çıkış ölçütü** yazılıdır; "bitti" hissi değil, sayılabilir çıktı ölçülür (m.29/m.39). Bu dosya LİSTE + HARİTA'dır; dersler `ogrenme/problem-cozme/dersler/` altına, ilerleme `ilerleme.md`'ye düşer (mit-6006 deseniyle aynı).
> **Varsayımlar:** Salih üniversite öğrencisi; veri/ML işi yapıyor (galeri şeridi, SHAP, GBM dersleri); MIT 6.006 + 6.042J kursları zaten açık (`ogrenme/mit-6006`, `ogrenme/mit-6042j`) — bu seri onları YENİDEN başlatmaz, içine yerleştirir (hazırı temel al, Salih 08-17).
> **Kaynak damgası (Karar 68):** kitap/kurs adları model hafızasından, AS-OF ≤ 2026-01, canlı doğrulanmadı; baskı/yıl iddiası yok. Ders başlarken ilgili kaynağın erişilebilirliği o gün doğrulanır.

## 0. Seviye tanımları (tüm başlıklarda ortak)
| Seviye | Anlamı | Tipik çıkış ölçütü biçimi |
|---|---|---|
| **L0 Lisans-giriş** | Kavram tabanı + standart teknikler; ders kitabı alıştırmaları | N alıştırma çözülmüş, çözüm kaydı var |
| **L1 Lisans-ileri** | Teknikleri SEÇMEYİ öğrenmek; "hangi araç bu probleme?" | Karışık problem seti, yardımsız oran ≥ eşik |
| **L2 Lisans-üstü / yarışma** | Standart olmayan problemler; birden çok tekniği birleştirme | Yarışma arşivi ya da gerçek proje formülasyonu |
| **L3 İleri** | Problem ÜRETME + başkasına öğretme + araştırma-sınırı | Özgün problem/proje + yazılı editorial |

**Çapraz kural (Başlık H'den):** her problemin çözümü 4 satırlık Pólya kaydıyla yazılır — (1) ne isteniyor / ne verili, (2) plan (hangi teknik, neden), (3) icra, (4) geriye bakış (başka yol var mı, hata neredeydi). Kayıtsız çözüm sayılmaz.

## 1. Başlık listesi (özet harita)
| # | Başlık | Problem çözmenin hangi bileşeni | Hazır ray |
|---|---|---|---|
| A | Matematiksel akıl yürütme ve ispat | Kesin tanım, dedüksiyon, değişmez bulma | MIT 6.042J (açık) |
| B | Algoritmik problem çözme | Ayrıştırma, indirgeme, karmaşıklık, veri yapısı seçimi | MIT 6.006 (açık) |
| C | Olasılıksal ve istatistiksel akıl yürütme | Belirsizlikle çıkarım, simülasyonla doğrulama | — |
| D | Modelleme, kestirim ve optimizasyon | Gerçek durumu matematiğe çevirme, büyüklük sezgisi | galeri şeridi (gerçek vaka) |
| E | Sistemli teşhis ve hata ayıklama | Hipotez-deney döngüsü, kök neden | jarvis kod tabanı, silver-sağlık |
| F | Karar verme ve belirsizlik | Beklenen değer, kalibrasyon, oyun teorisi | senaryo-defteri tahminleri (m.37) |
| G | Veri-güdümlü problem çerçeveleme | İş sorusu → ölçülebilir ML sorusu, sızıntı/doğrulama | galeri şeridi, SHAP/GBM dersleri |
| H | Üstbiliş ve pratik disiplini (çapraz-kesit) | Çözüm kaydı, hata günlüğü, tekrar, öğreterek öğrenme | sinav-grill skill'i |

## 2. Başlık başına seviye tabloları

### A — Matematiksel akıl yürütme ve ispat
| Sev. | Kaynak | Pratik | Çıkış ölçütü |
|---|---|---|---|
| L0 | Velleman, *How to Prove It* (böl. 1-6) + MIT 6.042J (mevcut şerit) | 6.042J problem setleri; Velleman'dan her bölümden 10 alıştırma | 6.042J pset 1-6 tamam + 60 Velleman alıştırması kayıtlı |
| L1 | Pólya, *How to Solve It* + Zeitz, *The Art and Craft of Problem Solving* (böl. 1-4: strateji, taktik, araçlar) | Zeitz böl. 1-4 problemleri; her problem Pólya 4-satır kaydıyla | 40 problem; yardımsız çözüm ≥ 25/40 |
| L2 | Engel, *Problem-Solving Strategies* (değişmez, uç ilkesi, güvercin yuvası, boyama, indirgeme) + Gelca-Andreescu, *Putnam and Beyond* (seçme) | Engel'den 5 bölüm × 8 problem; Putnam A1/B1 düzeyi 20 problem | 40 Engel + 20 Putnam-giriş; Putnam-giriş yardımsız ≥ 10/20 |
| L3 | Putnam arşivi (2000-2020) + Andreescu-Gelca, *Mathematical Olympiad Challenges* | Yılda 1 tam Putnam seti simülasyonu (6 saat, 12 soru) | Bir tam sette ≥ 3 tam-puan çözüm; 5 özgün problem + çözüm |

### B — Algoritmik problem çözme
| Sev. | Kaynak | Pratik | Çıkış ölçütü |
|---|---|---|---|
| L0 | MIT 6.006 (mevcut şerit) + Skiena, *The Algorithm Design Manual* (böl. 1-5) | 6.006 psetleri; LeetCode Easy | 6.006 pset'ler tamam + 60 Easy, her biri karmaşıklık notuyla |
| L1 | Halim, *Competitive Programming 4* (böl. 1-3) + CLRS (seçme: DP, çizge) | Codeforces Div2 A-C, haftada 10 problem | 100 problem; rating grafiği kayıtlı (ölçüm: platform verisi) |
| L2 | CP4 böl. 4-8 (çizge, matematik, string, geometri) + Skiena "war stories" | Codeforces Div2 D-E; ICPC bölgesel arşivi | Bir ICPC bölgesel setinde ≥ %50 ya da Codeforces rating ≥ 1600 |
| L3 | Kleinberg-Tardos, *Algorithm Design* (ispat-odaklı tasarım) + Erickson, *Algorithms* (ücretsiz PDF) | AtCoder ARC; kendi problem seti yazıp editorial hazırlamak | 10 özgün problem + test verisi + editorial; K-T'den 15 ispatlı tasarım |

### C — Olasılıksal ve istatistiksel akıl yürütme
| Sev. | Kaynak | Pratik | Çıkış ölçütü |
|---|---|---|---|
| L0 | Blitzstein-Hwang, *Introduction to Probability* (Stat 110 videoları ücretsiz) böl. 1-7 | Bölüm sonu alıştırmaları; her 5 alıştırmadan 1'i Python simülasyonuyla doğrulanır | 70 alıştırma; 14 simülasyon eşleşmesi kayıtlı |
| L1 | Mosteller, *Fifty Challenging Problems in Probability* + Bayes kuralı uygulamaları | 50 problemin tamamı: elle çözüm + Monte Carlo doğrulama | 50/50 çözüm; simülasyon ile analitik sonuç ≥ 45'inde uyuşur |
| L2 | Wasserman, *All of Statistics* (böl. 1-12) + McElreath, *Statistical Rethinking* (seçme) | 5 gerçek veri sorusu: hipotez, test tasarımı, güç hesabı, sonuç yazısı | 5 analiz planı + kod + yazı; her biri "yanlış olabilirdi çünkü" bölümüyle |
| L3 | Grimmett-Stirzaker, *One Thousand Exercises in Probability* (seçme) + Pearl-Glymour-Jewell, *Causal Inference in Statistics: A Primer*; Hernán-Robins, *What If* (ücretsiz) | Bir nedensel soruyu DAG → tanımlama → tahmin → duyarlılık ile uçtan uca | 1 uçtan uca nedensel analiz + 100 seçme alıştırma |

### D — Modelleme, kestirim ve optimizasyon
| Sev. | Kaynak | Pratik | Çıkış ölçütü |
|---|---|---|---|
| L0 | Mahajan, *Street-Fighting Mathematics* (MIT Press, ücretsiz) + Weinstein-Adam, *Guesstimation* | Fermi soruları: 30 soru, her biri varsayım zinciriyle | 30 soru; gerçek değere ×3 bandı içinde ≥ 21/30 |
| L1 | Mahajan, *The Art of Insight in Science and Engineering* + Hillier-Lieberman, *Introduction to Operations Research* (LP bölümleri) | 10 sözel problemi LP/IP olarak modelle, PuLP/OR-Tools ile çöz | 10 model + çözüm; her biri "kısıt neden bu" gerekçesiyle |
| L2 | Boyd-Vandenberghe, *Convex Optimization* (böl. 1-5 + ek alıştırmalar) + Bertsimas-Tsitsiklis, *Introduction to Linear Optimization* (seçme) | 20 modelleme alıştırması; galeri-sıralama problemini optimizasyon olarak formüle et | 20 alıştırma + 1 gerçek-vaka formülasyonu (amaç, kısıt, değişken tablosu) |
| L3 | Williams, *Model Building in Mathematical Programming* + stokastik programlama / simülasyon-tabanlı optimizasyon (seçme makale) | Belirsizlik altında bir karar modeli: senaryo ağacı + duyarlılık analizi | 1 proje raporu; parametre duyarlılığı tablolu |

### E — Sistemli teşhis ve hata ayıklama
| Sev. | Kaynak | Pratik | Çıkış ölçütü |
|---|---|---|---|
| L0 | Agans, *Debugging: The 9 Indispensable Rules* + Zeller, *Why Programs Fail* (böl. 1-6) | Her bug için kayıt: gözlem → hipotez → deney → sonuç (bilimsel yöntem) | 20 bug kaydı (jarvis + iş kod tabanından) |
| L1 | Kernighan-Pike, *The Practice of Programming* (böl. 5 debugging, 7 performance) + Zeller (delta debugging bölümü) | 3 performans teşhisi: ölçüm → darboğaz → düzeltme → yeniden ölçüm; 1 delta-debugging uygulaması | 3 ölçümlü teşhis raporu + 1 en-küçük-hata-girdisi bulgusu |
| L2 | Meadows, *Thinking in Systems* + Google SRE kitabı "Postmortem Culture" bölümü (ücretsiz) + 5-Neden / Ishikawa | 5 postmortem (gerçek olaylar: silver-sağlık uyarıları, galeri sızıntısı vb.) | 5 postmortem; her biri kök neden + tekrar-önleme kuralıyla |
| L3 | Lamport TLA+ notları + Hillel Wayne, *Practical TLA+* | Bir protokolü/iş akışını (ör. ingest v2 ya da paralel-oturum kilidi) spesifiye et, model-checker'la hata ara | 1 TLA+ spesifikasyonu + model-check'te bulunan ≥ 1 gerçek hata ya da "hata yok" ispatı |

### F — Karar verme ve belirsizlik altında akıl yürütme
| Sev. | Kaynak | Pratik | Çıkış ölçütü |
|---|---|---|---|
| L0 | Hammond-Keeney-Raiffa, *Smart Choices* + beklenen değer / karar ağacı temelleri | 10 gerçek karar (jarvis masası kalemlerinden) karar ağacıyla | 10 karar ağacı; olasılık ve fayda değerleri gerekçeli |
| L1 | Tetlock-Gardner, *Superforecasting* + Brier skoru | 100 tahmin, senaryo-defteri formatında, sonuçlanınca skorlanır | 100 tahmin + Brier skoru grafiği (müfredat P19 ile birleşir) |
| L2 | Osborne, *An Introduction to Game Theory* (böl. 1-5) + Raiffa, *Decision Analysis* | 20 oyun-teorisi problemi + 3 çok-ölçütlü karar (ağırlıklandırma, duyarlılık) | 20 problem + 3 karar matrisi |
| L3 | Lattimore-Szepesvári, *Bandit Algorithms* (ücretsiz, böl. 1-8) + Berger, *Statistical Decision Theory* (seçme) | Bir çok-kollu bandit deneyi tasarla, simüle et, pişmanlık ölç | 1 deney raporu: 3 algoritma × pişmanlık eğrisi |

### G — Veri-güdümlü problem çerçeveleme
| Sev. | Kaynak | Pratik | Çıkış ölçütü |
|---|---|---|---|
| L0 | McKinney, *Python for Data Analysis* + Tukey'nin keşifsel veri analizi ilkeleri | 5 veri seti için EDA raporu: soru → grafik → bulgu → sonraki soru | 5 EDA raporu; her grafik bir soruya bağlı |
| L1 | Zinkevich, *Rules of Machine Learning* (Google, ücretsiz) + Huyen, *Designing Machine Learning Systems* (böl. 1-4) | 5 iş sorusunu ML sorusuna çevir: hedef, metrik, sızıntı riski, doğrulama planı | 5 çerçeveleme dokümanı (galeri şeridi bunların 1'i sayılır) |
| L2 | Kuhn-Johnson, *Feature Engineering and Selection* + Ng, *Machine Learning Yearning* (ücretsiz) + Kaggle çözüm yazıları | 3 bitmiş yarışmayı yeniden üret; hata analizi tablosu (hangi dilim, neden) | 3 reprodüksiyon + hata analizi; skor farkı kaynaklı |
| L3 | Kohavi-Tang-Xu, *Trustworthy Online Controlled Experiments* + nedensel çıkarım (C-L3 ile ortak) | Uçtan uca: iş sorusu → deney tasarımı → model → karar → izleme | 1 uçtan uca vaka raporu + karar önerisi |

### H — Üstbiliş ve pratik disiplini (çapraz-kesit; her başlığa paralel)
| Sev. | Kaynak | Pratik | Çıkış ölçütü |
|---|---|---|---|
| L0 | Pólya 4 adım + Schoenfeld, *Mathematical Problem Solving* (kontrol/üstbiliş bölümü) | Çözüm kaydı şablonu + hata günlüğü (her yanlış çözüm: ne düşündüm, nerede kırıldı) | 4 hafta kesintisiz kayıt; hata günlüğünde ≥ 20 giriş |
| L1 | Ericsson-Pool, *Peak* + Brown-Roediger-McDaniel, *Make It Stick* | Aralıklı tekrar: çözülmüş problemler 1-7-30 gün sonra tekrar; Anki ya da düz dosya | 200 kartlık tekrar destesi; tekrar başarı oranı kayıtlı |
| L2 | Feynman tekniği (öğreterek öğrenme) + `sinav-grill` skill'i | Her başlığın her seviyesi için 1 öğretim yazısı; sınav-grill ile bulanık blok listesi | 8 öğretim yazısı; grill sonucu bulanık blok sayısı azalan seride |
| L3 | Problem yazarlığı + akran hakemliği | Zorluk-ölçekli kişisel problem bankası; başkasının çözümünü hakemlik | 50 özgün problem + çözüm + zorluk etiketi |

## 3. Sıra ve paralellik (aynı anda en fazla 3 başlık; H her zaman açık)
| Faz | Aktif başlıklar | Kapı (faz geçiş koşulu) |
|---|---|---|
| **1** | A-L0 (6.042J) · B-L0 (6.006) · H-L0 | 6.042J pset 1-6 + 6.006 pset'ler + 4 hafta kayıt |
| **2** | A-L1 · C-L0 · D-L0 (+ H-L1) | Zeitz 40 problem + Blitzstein 70 alıştırma + Fermi 21/30 |
| **3** | B-L1 · E-L0 · G-L0/L1 | Codeforces 100 + 20 bug kaydı + 5 çerçeveleme |
| **4** | A-L2 · C-L1 · F-L0/L1 (+ H-L2) | Engel 40 + Mosteller 50 + 100 tahmin |
| **5** | B-L2 · D-L1/L2 · E-L1/L2 | ICPC %50 ∨ rating 1600 + 20 optimizasyon + 5 postmortem |
| **6** | C-L2 · G-L2 · F-L2 | 5 analiz planı + 3 reprodüksiyon + 20 oyun problemi |
| **7** | L3 katmanı: A, B, D, E, C/G ortak proje, F, H | Her başlıkta 1 özgün ürün (problem seti / spesifikasyon / vaka raporu) |

**Gerekçe:** Faz 1 mevcut şeritlerin üstüne biner (ek kaynak açmaz). C ve D erken gelir çünkü G (ML çerçeveleme) ve F (karar) ikisine dayanır. E-L0 kod tabanına dokunduğu için B-L1 ile aynı fazda: aynı haftalarda hem problem çözülür hem gerçek hata teşhis edilir. L3 katmanı tek fazda toplanır; proje-odaklıdır, sıra Salih'e bırakılır.

## 4. Hacim tahmini (deneysel, ölçülmedi — ilk 2 fazdan sonra kalibre edilir)
| Kalem | Değer | Kaynak |
|---|---|---|
| Toplam problem/alıştırma (ölçütlerin toplamı) | ≈ 1.100 | §2 çıkış ölçütleri toplamı, elle sayım |
| Faz sayısı | 7 | §3 |
| Haftalık problem tempo varsayımı | 15 | varsayım; ölçülecek |
| Buna göre süre | ≈ 75 hafta | 1.100 / 15; deneysel damga (m.29) — kitap okuma süresi hariç |

## 5. Kayıt yapısı (mit-6006 deseni)
- `ogrenme/problem-cozme/ilerleme.md` — §2 tablolarının Durum sütunu; her ölçüt için "sayım / hedef".
- `ogrenme/problem-cozme/dersler/YYYY-MM-DD-<başlık>-<seviye>-<konu>.md` — ders kaydı (ogrenme/README protokolü: pasif-okuma, [S]/[O]/[T], görsel atıflı, en az 1 matematik içeriği — Karar 73).
- `ogrenme/problem-cozme/cozumler/<başlık>/NNN.md` — Pólya 4-satır kayıtlı çözümler; hata günlüğü `hata-gunlugu.md`.
- Sayımlar dosyadan script'le türetilir (deterministik; elle sayım yok) — script `tools/` altına ilk ders açılınca yazılır.

## 6. Açık kararlar (Salih)
1. **Faz 1 tetiği:** bu seri mevcut 6.042J/6.006 şeritlerinin üstüne biner; "günaydın, öğrenme" oturumlarında hangi başlıkla açılacağı — öneri: H-L0 kayıt şablonunu ilk derste kur, sonra A-L1 (Zeitz böl. 1).
2. **Yarışma platformu:** B başlığında Codeforces varsayıldı; AtCoder/LeetCode tercihi Salih'in.
3. **F-L1 ile müfredat P19 (kalibrasyon/Brier) birleştirilsin mi** — aynı iş iki yerde durmasın (m.8 pointer).
