# Problem Çözme Eğitim Serisi — Tasarım v1 (2026-09-09; v0 → v1, Salih kararı "v1'i şimdi yaz")

> **Ne bu:** Salih'in problem çözme yeteneğini lisans düzeyinden ileri seviyeye taşıyan, **AI çağında kariyer yatırımı** bağlamına oturtulmuş 9 başlıklı (A-I), seviyeli (L0→L3) eğitim serisi. v0 (`seri-tasarimi-v0.md`, 09-08) arşiv/pointer olarak durur (m.8). Revizyon gerekçesi: Atlas koşumu `raporlar/2026-09-09-problem-cozme-ai-cagi-atlas.md` §3 (hayatta-kalan çekirdek ⑥⑦⑨: kapalı-uçlu yarışma problemleri AI'ya geçti · uzun-ufuklu/işbirlikli iş ölçülmemiş · korumasız AI ile öğrenme −%17).
> **Varsayımlar:** Salih üniversite öğrencisi (matematik mühendisliği); veri/ML işi yapıyor; MIT 6.006 + 6.042J şeritleri açık; bu seri onları içine yerleştirir (hazırı temel al).
> **Kaynak damgası (Karar 68):** kitap/kurs adları model hafızasından AS-OF ≤ 2026-01 canlı doğrulanmadı; Atlas'tan gelen kaynaklar [D]/[K] etiketli, URL'ler raporda. Ders açılırken kaynağın erişilebilirliği o gün doğrulanır.

## 0. v0 → v1 değişiklik özeti
| # | Değişiklik | Gerekçe (Atlas §3) |
|---|---|---|
| 1 | **Yeni başlık I:** AI-çıktısı doğrulama + sınır bilgisi + benchmark okuryazarlığı (öncelik 1) | Bastani −%17 [D] · otomasyon yanlılığı [D] · doğrulama literatürü var, pedagojide işlenmemiş [K] |
| 2 | **A-L2/L3:** Putnam hedefleri "teknik repertuar" düzeyine iner; L3 = özgün problem/model üretimi | IMO altın sertifikalı [D]; kapalı-uçlu olimpiyat ikame edildi |
| 3 | **B-L2:** Codeforces rating hedefi KALKAR; yerine AI-üretimi kodu okuma-doğrulama + karmaşıklık analizi | METR: self-contained kısa görevler AI'nın en güçlü alanı [D] |
| 4 | **C:** nedensel çıkarım L2'ye iner; C-L2/L3 fazda öne çekilir | "pazarlık dışı" [K] · nedensel/A-B talep sinyali [K] · BLS [D] |
| 5 | **D/F-L3 proje çıktıları erken faza;** portföy-ürün hedefi | junior AI-maruz istihdam açığı %15→%19 [D]; uzun-ufuklu iş ölçülmemiş [D] |
| 6 | **G-L1:** A/B testi + nedensel çerçeveleme eklendi | tekrarlayan talep sinyali [K] |
| 7 | **F-L1 ↔ müfredat P19** birleşti (tek kalibrasyon kalemi) | m.8 pointer, aynı iş iki yerde durmaz |
| 8 | **H'ye "paydaşa anlatma"** formatı | Lightcast çapraz-fonksiyonel talep [K] |
| 9 | **Öğrenme protokolü kuralı** (§5): çözüm aşamasında AI KAPALI; AI yalnız tutor/doğrulama modunda | Bastani: cevap-gizleyen tutor nötr, korumasız kullanım zararlı [D] |

## 1. Seviye tanımları (ortak)
| Seviye | Anlamı | Çıkış ölçütü biçimi |
|---|---|---|
| **L0 Lisans-giriş** | Kavram tabanı + standart teknikler | N alıştırma, çözüm kaydı var |
| **L1 Lisans-ileri** | Tekniği SEÇMEYİ öğrenmek | Karışık set, yardımsız oran ≥ eşik |
| **L2 Lisans-üstü** | Standart olmayan problem; tekniklerin birleşimi; gerçek vaka | Yarışma arşivi (araç) ya da gerçek proje formülasyonu |
| **L3 İleri** | Problem/model ÜRETME + öğretme + portföy-ürün | Özgün ürün + yazılı editorial/rapor |

**Çapraz kural:** her çözüm 4 satırlık Pólya kaydıyla yazılır (verili/istenen · plan · icra · geriye bakış). Kayıtsız çözüm sayılmaz. **AI kuralı:** §5.

## 2. Başlık haritası
| # | Başlık | Bileşen | Öncelik (Atlas) | Hazır ray |
|---|---|---|---|---|
| I | **AI-çıktısı doğrulama, sınır bilgisi, benchmark okuryazarlığı** | AI nerede yanılır, nasıl yakalanır | **1** | jarvis halüsinasyon paketi, V26 sondaj deneyimi |
| C | Olasılıksal/istatistiksel akıl yürütme + nedensel çıkarım | Belirsizlikle çıkarım, deney | **2** | — |
| D | Modelleme, kestirim, optimizasyon (proje ölçeği) | Gerçek durumu matematiğe çevirme | **3** | galeri şeridi |
| F | Karar verme, belirsizlik, kalibrasyon | Beklenen değer, Brier, oyun teorisi | 3 | senaryo-defteri tahminleri, P19 |
| A | Matematiksel akıl yürütme, ispat, özgün problem kurma | Dedüksiyon, değişmez, problem yazarlığı | 4 | MIT 6.042J |
| B | Algoritmik düşünme + AI kodunu doğrulama | İndirgeme, karmaşıklık, kod okuma | 5 | MIT 6.006 |
| E | Sistemli teşhis, hata ayıklama, formel spesifikasyon | Hipotez-deney, kök neden | 5 | jarvis kod tabanı |
| G | Veri-güdümlü çerçeveleme + deney tasarımı | İş sorusu → ölçülebilir soru, sızıntı, A/B | 2 | galeri şeridi, SHAP/GBM dersleri |
| H | Üstbiliş, pratik disiplini, paydaşa anlatma (çapraz-kesit) | Kayıt, tekrar, öğreterek öğrenme | hep açık | sinav-grill |

## 3. Başlık başına seviye tabloları

### I — AI-çıktısı doğrulama, sınır bilgisi, benchmark okuryazarlığı (YENİ, öncelik 1)
| Sev. | Kaynak | Pratik | Çıkış ölçütü |
|---|---|---|---|
| L0 | Bergstrom-West, *Calling Bullshit* (veri/iddia okuryazarlığı) + Bastani vd. "Generative AI Can Harm Learning" (PNAS) [D] + Atlas raporu §1 | **Yeniden-türetme egzersizi:** 30 AI cevabı (matematik/kod/istatistik) elle yeniden türetilir; hata bulunanlar sınıflanır (yanlış olgu · yanlış adım · doğru ama gerekçesiz) | 30 kayıt; hata tipi dağılımı tablosu; hata yakalama oranı kayıtlı |
| L1 | Epoch AI FrontierMath "about" sayfası [D] · METR time-horizon + sınır notu [D] · Dell'Acqua "jagged frontier" [K] · Vaccaro meta-analiz (arXiv 2405.06087) [K] | **Benchmark okuryazarlığı:** 5 benchmark için künye (kim finanse etti, kontaminasyon, tier/kapsam, insan taban çizgisi); "hangi görevde AI'ya devret, hangisinde döngüde kal" karar tablosu | 5 benchmark künyesi + 1 devret/döngüde-kal karar tablosu (kendi iş görevleri için) |
| L2 | Otomasyon-yanlılığı deneyleri [D] · "Think First, Verify Always" (arXiv 2508.03714) [K] · Kohavi vd. deney tasarımı (C/G ile ortak) | **Doğrulama deneyi tasarımı:** kendi işinde bir AI-destekli görev için körleme, kontrol, ölçüm; sonucu yazı | 1 deney raporu (N, ölçüm, sonuç); 1 "AI hata atlası" taslağı (alan: veri/ML) |
| L3 | halusinasyon-paketi + V26 sondaj kuralı (jarvis) · literatür taraması | **AI hata atlası v1:** kendi alanında AI'nın sistematik yanılma sınıfları + her sınıf için yakalama testi; başkasına öğretilebilir | Atlas ≥ 20 sınıf × yakalama testi; 1 öğretim yazısı; grill ile sınanmış |

### C — Olasılıksal/istatistiksel akıl yürütme + nedensel çıkarım (öncelik 2)
| Sev. | Kaynak | Pratik | Çıkış ölçütü |
|---|---|---|---|
| L0 | Blitzstein-Hwang, *Introduction to Probability* (Stat 110) böl. 1-7 | Bölüm alıştırmaları; her 5'ten 1'i Python simülasyonuyla doğrulanır | 70 alıştırma; 14 simülasyon eşleşmesi |
| L1 | Mosteller, *Fifty Challenging Problems in Probability* + Bayes uygulamaları | 50 problem: elle + Monte Carlo | 50/50; ≥ 45 uyuşma |
| L2 | Wasserman, *All of Statistics* (böl. 1-12) + Pearl-Glymour-Jewell, *Causal Inference in Statistics: A Primer* + Hernán-Robins, *What If* (ücretsiz) | 5 gerçek veri sorusu: hipotez, test, güç; 3 nedensel soru: DAG → tanımlama → tahmin | 5 analiz planı + 3 DAG'lı nedensel analiz; her biri "yanlış olabilirdi çünkü" bölümüyle |
| L3 | McElreath, *Statistical Rethinking* + Grimmett-Stirzaker (seçme) + Kohavi-Tang-Xu, *Trustworthy Online Controlled Experiments* | Uçtan uca: nedensel soru + deney tasarımı + duyarlılık; iş verisiyle (galeri şeridi) | 1 uçtan uca nedensel/deneysel rapor + 100 seçme alıştırma |

### D — Modelleme, kestirim, optimizasyon, proje ölçeği (öncelik 3)
| Sev. | Kaynak | Pratik | Çıkış ölçütü |
|---|---|---|---|
| L0 | Mahajan, *Street-Fighting Mathematics* (ücretsiz) + Weinstein-Adam, *Guesstimation* | 30 Fermi sorusu, varsayım zinciriyle | ×3 bandı içinde ≥ 21/30 |
| L1 | Mahajan, *The Art of Insight* + Hillier-Lieberman (LP bölümleri) | 10 sözel problem → LP/IP; PuLP/OR-Tools | 10 model + çözüm, kısıt gerekçeli |
| L2 | Boyd-Vandenberghe, *Convex Optimization* (böl. 1-5) + Bertsimas-Tsitsiklis (seçme) + Williams, *Model Building in Mathematical Programming* | 15 modelleme alıştırması + **galeri-sıralama problemi optimizasyon olarak formüle** (ML tahmini + kısıt hibrit) | 15 alıştırma + 1 gerçek-vaka formülasyonu (amaç/kısıt/değişken tablosu) |
| L3 | Stokastik programlama / simülasyon-tabanlı optimizasyon (seçme makale) | **Portföy projesi:** belirsizlik altında karar modeli, senaryo ağacı, duyarlılık; çok-haftalık, başkasıyla paylaşılabilir ürün | 1 proje raporu + kod deposu + duyarlılık tablosu (portföy kalemi) |

### F — Karar verme, belirsizlik, kalibrasyon (öncelik 3)
| Sev. | Kaynak | Pratik | Çıkış ölçütü |
|---|---|---|---|
| L0 | Hammond-Keeney-Raiffa, *Smart Choices* + beklenen değer / karar ağacı | 10 gerçek karar (jarvis masası kalemleri) ağaçla | 10 karar ağacı, olasılık/fayda gerekçeli |
| L1 | Tetlock-Gardner, *Superforecasting* + Brier skoru — **müfredat P19 ile TEK kalem** | 100 tahmin senaryo-defteri formatında, skorlanır | 100 tahmin + Brier grafiği |
| L2 | Osborne, *An Introduction to Game Theory* (böl. 1-5) + Raiffa, *Decision Analysis* | 20 oyun problemi + 3 çok-ölçütlü karar | 20 problem + 3 karar matrisi |
| L3 | Lattimore-Szepesvári, *Bandit Algorithms* (ücretsiz, böl. 1-8) + Berger (seçme) | Bandit deneyi: tasarım, simülasyon, pişmanlık | 1 deney raporu: 3 algoritma × pişmanlık eğrisi (portföy kalemi) |

### A — Matematiksel akıl yürütme, ispat, özgün problem kurma (öncelik 4; yarışma = araç)
| Sev. | Kaynak | Pratik | Çıkış ölçütü |
|---|---|---|---|
| L0 | Velleman, *How to Prove It* (böl. 1-6) + MIT 6.042J (mevcut) | 6.042J psetleri; Velleman bölüm başına 10 | 6.042J pset 1-6 + 60 alıştırma |
| L1 | Pólya, *How to Solve It* + Zeitz, *Art and Craft* (böl. 1-4) | 40 problem, Pólya kaydıyla | yardımsız ≥ 25/40 |
| L2 | Engel, *Problem-Solving Strategies* (değişmez, uç ilkesi, güvercin yuvası) — **teknik repertuar olarak, 25 problem** (v0: 40+20 Putnam) | Her tekniğe 5 problem + tekniğin gerçek-vaka karşılığı (ör. değişmez → veri hattı tutarlılık kontrolü) | 25 problem + 5 "teknik → gerçek vaka" eşlemesi |
| L3 | Andreescu-Gelca (seçme) + Schoenfeld problem-yazarlığı | **Özgün problem/model üretimi:** iş/veri bağlamından 10 problem kurma (tanım, çözüm, zorluk, neden ilginç); Putnam tam-set simülasyonu İSTEĞE BAĞLI | 10 özgün problem + çözüm + editorial |

### B — Algoritmik düşünme + AI kodunu doğrulama (öncelik 5)
| Sev. | Kaynak | Pratik | Çıkış ölçütü |
|---|---|---|---|
| L0 | MIT 6.006 (mevcut) + Skiena, *Algorithm Design Manual* (böl. 1-5) | 6.006 psetleri; LeetCode Easy | 6.006 psetler + 60 Easy, karmaşıklık notuyla |
| L1 | Halim, *Competitive Programming 4* (böl. 1-3) + CLRS (DP, çizge) | Codeforces Div2 A-C, **60 problem** (v0: 100) | 60 problem, her biri karmaşıklık + alternatif yaklaşım notuyla |
| L2 | Kleinberg-Tardos, *Algorithm Design* (ispat-odaklı) + Skiena "war stories" — **rating hedefi KALKTI** | **AI-üretimi kod doğrulama:** 20 AI-yazımı çözüm/fonksiyon için doğruluk ispatı ya da karşı-örnek + karmaşıklık analizi; 15 K-T ispatlı tasarım | 20 doğrulama kaydı (kaç hata yakalandı) + 15 ispatlı tasarım |
| L3 | Erickson, *Algorithms* (ücretsiz) + AtCoder ARC (seçme) | 10 özgün problem + test verisi + editorial; 1 algoritmik bileşen portföy projesine (D-L3) | 10 problem + editorial |

### E — Sistemli teşhis, hata ayıklama, formel spesifikasyon (öncelik 5)
| Sev. | Kaynak | Pratik | Çıkış ölçütü |
|---|---|---|---|
| L0 | Agans, *Debugging* + Zeller, *Why Programs Fail* (böl. 1-6) | 20 bug kaydı (gözlem → hipotez → deney → sonuç); ≥ 5'i AI-yazımı kodda | 20 kayıt |
| L1 | Kernighan-Pike, *Practice of Programming* (böl. 5, 7) + delta debugging | 3 ölçümlü performans teşhisi + 1 delta-debugging | 3 rapor + 1 en-küçük-girdi bulgusu |
| L2 | Meadows, *Thinking in Systems* + Google SRE "Postmortem Culture" (ücretsiz) + 5-Neden/Ishikawa | 5 postmortem (silver-sağlık uyarıları, galeri sızıntısı vb.) | 5 postmortem, kök neden + tekrar-önleme kuralı |
| L3 | Lamport TLA+ + Hillel Wayne, *Practical TLA+* | Bir iş akışını (ingest v2 / paralel-oturum kilidi) spesifiye et, model-check | 1 spesifikasyon + ≥ 1 bulunan hata ya da "hata yok" ispatı |

### G — Veri-güdümlü çerçeveleme + deney tasarımı (öncelik 2)
| Sev. | Kaynak | Pratik | Çıkış ölçütü |
|---|---|---|---|
| L0 | McKinney, *Python for Data Analysis* + Tukey EDA ilkeleri | 5 veri seti EDA: soru → grafik → bulgu → sonraki soru | 5 rapor, her grafik bir soruya bağlı |
| L1 | Zinkevich, *Rules of ML* (ücretsiz) + Huyen, *Designing ML Systems* (böl. 1-4) + **Kohavi A/B temel bölümleri** | 5 iş sorusu → ML/deney sorusu: hedef, metrik, sızıntı, doğrulama planı, **A/B mi gözlemsel mi kararı** | 5 çerçeveleme dokümanı (galeri şeridi 1'i) |
| L2 | Kuhn-Johnson, *Feature Engineering and Selection* + Ng, *ML Yearning* (ücretsiz) + Kaggle çözüm yazıları | 3 bitmiş yarışma reprodüksiyonu + hata analizi | 3 reprodüksiyon + dilimli hata tablosu |
| L3 | C-L3 ile ortak (Kohavi + nedensel) | Uçtan uca: iş sorusu → deney → model → karar → izleme | 1 vaka raporu + karar önerisi (portföy kalemi) |

### H — Üstbiliş, pratik disiplini, paydaşa anlatma (çapraz-kesit)
| Sev. | Kaynak | Pratik | Çıkış ölçütü |
|---|---|---|---|
| L0 | Pólya 4 adım + Schoenfeld (kontrol/üstbiliş) | Çözüm kaydı + hata günlüğü; **AI kuralı §5 uygulanır** | 4 hafta kesintisiz; ≥ 20 hata girişi |
| L1 | Ericsson-Pool, *Peak* + Brown vd., *Make It Stick* | Aralıklı tekrar 1-7-30 gün; deste | 200 kart; tekrar başarı oranı |
| L2 | Feynman tekniği + `sinav-grill` | Her başlık için 1 öğretim yazısı, **"iş birimine anlatım" formatında** (teknik olmayan okuyucu, 1 sayfa, karar önerisiyle) | 9 yazı; grill bulanık-blok sayısı azalan seride |
| L3 | Problem yazarlığı + akran hakemliği | Zorluk-ölçekli problem bankası; başkasının çözümünü hakemlik | 50 özgün problem + zorluk etiketi |

## 4. Sıra ve paralellik (aynı anda ≤ 3 başlık; H hep açık)
| Faz | Aktif | Kapı |
|---|---|---|
| **1** | I-L0 · A-L0 (6.042J) · B-L0 (6.006) · H-L0 | 30 yeniden-türetme + 6.042J pset 1-6 + 6.006 psetler + 4 hafta kayıt |
| **2** | I-L1 · C-L0 · D-L0 (+H-L1) | 5 benchmark künyesi + devret/döngüde-kal tablosu + Blitzstein 70 + Fermi 21/30 |
| **3** | C-L1 · G-L0/L1 · E-L0 | Mosteller 50 + 5 çerçeveleme + 20 bug kaydı |
| **4** | C-L2 · A-L1 · F-L0/L1 (+H-L2 başlar) | 5 analiz + 3 DAG + Zeitz 25/40 + 100 tahmin |
| **5** | D-L1/L2 · I-L2 · B-L1 | 10 LP + galeri formülasyonu + doğrulama deneyi + 60 CF |
| **6** | D-L3 (portföy) · G-L2 · E-L1/L2 | proje raporu + 3 reprodüksiyon + 5 postmortem |
| **7** | C-L3/G-L3 ortak vaka · F-L2 · A-L2 · B-L2 | vaka raporu + 20 oyun + Engel 25 + 20 kod doğrulama |
| **8** | L3 katmanı: I-L3 (hata atlası) · A-L3 · B-L3 · E-L3 · F-L3 · H-L3 | her başlıkta 1 özgün ürün |

**Gerekçe:** I-L0 Faz 1'de çünkü §5 kuralının kası orada kurulur ve sonraki her fazın AI kullanımı bu beceriye dayanır. C ve G öne çekildi (öncelik 2); D-L3 portföy Faz 6'ya alındı (v0: Faz 7). A-L2 ve B-L2 (yarışma repertuarı) Faz 7'ye indi: araçtır, hedef değil.

## 5. Öğrenme protokolü — AI kuralı (Atlas ⑨, Bastani [D])
1. **Çözüm aşamasında AI KAPALI.** Problem okunur, Pólya kaydı 1-3 AI'sız yazılır.
2. **AI yalnız iki modda:** (a) **tutor modu** — cevap vermeyen, ipucu veren (Bastani'nin nötr bulduğu tasarım); (b) **doğrulama modu** — Salih'in bitmiş çözümünü AI sınar, Salih AI'nın itirazını elle yeniden-türetir (I-L0 kası).
3. **Geriye bakış (Pólya 4)** AI ile yapılabilir; fark bulunursa hata günlüğüne "kim haklıydı" sütunuyla girer.
4. Ölçüm: her ders kaydında "AI kullanımı: kapalı / tutor / doğrulama" etiketi; ilerleme dosyasında oran izlenir.

## 6. Hacim (deneysel, ölçülmedi; ilk 2 fazdan sonra kalibre)
| Kalem | Değer | Kaynak |
|---|---|---|
| Toplam problem/alıştırma/kayıt | ≈ 1.050 | §3 çıkış ölçütleri toplamı, elle sayım (v0 ≈ 1.100; yarışma hacmi düştü, I eklendi) |
| Faz | 8 | §4 |
| Haftalık tempo varsayımı | 15 | varsayım; ölçülecek |
| Süre | ≈ 70 hafta | 1.050 / 15; kitap okuma hariç (m.29) |

## 7. Kayıt yapısı
`ilerleme.md` (ölçüt başına sayım/hedef + AI-modu oranı) · `dersler/YYYY-MM-DD-<başlık>-<seviye>-<konu>.md` (ogrenme/README protokolü: pasif-okuma, [S]/[O]/[T], görsel atıflı, ≥ 1 matematik içeriği — Karar 73) · `cozumler/<başlık>/NNN.md` (Pólya 4-satır) · `hata-gunlugu.md` · sayımlar script'le (`tools/`, ilk derste yazılır).

## 8. Açık kalemler
1. I-L1/L2 kaynakları Atlas raporundan; kitap düzeyi kaynak (doğrulama pedagojisi) ayrı küçük tarama ister — Faz 2 öncesi.
2. Atlas'ta çözülmeyen 3 çelişkili rakam (Anthropic kurumsal-API oranı, Epoch Tier 4 güncel, BLS OR) I-L1 benchmark-künyesi egzersizinin İLK üç ödevi olsun (öğrenme + kapanış aynı iş).
3. Faz 1 açılış tetiği: "günaydın, öğrenme" oturumunda I-L0 ilk ders (30 yeniden-türetmenin ilk 5'i).
