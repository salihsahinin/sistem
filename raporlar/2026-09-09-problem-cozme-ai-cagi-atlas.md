# AI çağında kariyer-yatırımı olarak "problem solving": hangi konular? — Atlas Raporu (2026-09-09)
> **Mod:** ana-sıra (Claude Code masaüstü, Fable 5.1) · şerit: çift-atlas (tez ∧ ¬tez) + V26 kural-tabanlı sondaj + bağımsız hakem · aile sayısı: 3 · koşucu: Sonnet (Karar 85) · 9 ajan, ≈548k ajan-token (usage sayaçları toplamı; Carvis'in kendi koşumu hariç — Salih 08-29).
> **Soru (Salih 09-09, aynen):** "ai çağında ilerleyen yıllarda ön plana çıkacak olan skillin problem solving olduğu söyleniyor. matematik mühendisliği öğrencisi olarak yatırım amaçlı gelişen ai çağına uygun, gelecek yıllarda işime yarayacak bağlamda problem solving skillimi geliştirmek istiyorum eğitim serileri de bu bağlamda oluşturulacak. bu bağlamda hangi konulara çalışılması gerektiğini araştır."
> **Kanıt kısıtı (dürüstlük):** WEF skills-outlook sayfası + PDF (403/bozuk), SSRN Dell'Acqua (403), Nature Vaccaro (kimlik duvarı), Science Noy-Zhang/Eloundou (paywall), pnas.org (403, PMC yansıması açıldı), bls.gov (bot engeli). V26 kuralı gereği **tez-A1, tez-A3 ve antitez-A1 dosyalarının TÜM bulguları K'ya düştü** (her birinde ≥1 sondaj tutmadı). Ham dosyalar: `cc/rapor-2026-09-09-ps-{tez,antitez}-A{1,2,3}.md`, `…-v26-{tez,antitez}.md`, `…-hakem.md`.

## 0. Tek paragraf cevap
Hayatta kalan kanıt "problem solving" etiketini değil, üç somut şeyi işaret ediyor: (1) **AI çıktısını doğrulama ve AI'nın sınırını bilme** — korumasız AI kullanımı öğrenmeyi ve doğruluğu ölçülebilir biçimde düşürüyor [D], bu beceri için literatür var ama pedagojide işlenmemiş [K]; (2) **kantitatif temel (olasılık/istatistik/optimizasyon/nedensel çıkarım) azaltılmaz, AI ile kaldıraçlanır** — insanın iyi olduğu alana AI eklemek kazandırıyor, AI'nın iyi olduğu alanda insan müdahalesi zarar veriyor [K, yön sağlam]; (3) **kapalı-uçlu, kısa, kendi-içinde-tamam problemler (IMO tarzı, tek-dosya kod) AI'ya geçti** [D]; **uzun-ufuklu, işbirlikli, açık-uçlu modelleme/karar işleri ölçülmemiş ya da hâlâ insan alanı** [D+K]. Mevcut seri tasarımı (v0) bu yüzden 2 yerde yön değiştirmeli: yarışma-matematiği/rating hedefleri araç düzeyine iner; "AI-çıktısı doğrulama + sınır bilgisi" ayrı başlık olur.

## 1. Aile başına bulgular
### Aile 1 — İşgücü raporları / işveren anketleri (tez K'ya düştü, antitez K'ya düştü)
- **Tez:** WEF FoJ 2025 "analytical thinking" %69 ilk sırada; becerilerin %39'u 2030'a dek eskir [K — WEF sayfası 403; V26: tez WEF 2026 raporunu (2026-01-07, %44) kaçırmış] (https://www.weforum.org/publications/the-future-of-jobs-report-2025/). Anthropic Economic Index: tüketici tarafında augmentation %52 > automation %45 (Kasım 2025); lisans-düzeyi görevde ~12x, lise-düzeyi ~9x hızlanma [D — iki bağımsız denetimde ham metinde tuttu] (https://www.anthropic.com/research/economic-index-primitives, AS-OF 2026-01-15).
- **Antitez (¬):** WEF'in eskime-oranı tahmini sürümden sürüme %35→%56→%57→%44→%39→%44 oynuyor; "problem solving" terimi İK literatüründe "vague" [K]. Augmentation üstünlüğü yalnız tüketici segmenti; kurumsal API için %75/77 automation iddiası **aynı URL'de bağımsız yeniden-açılışta bulunamadı → ÇELİŞKİLİ**. Stanford Digital Economy Lab: 22-25 yaş, yüksek-AI-maruziyetli mesleklerde istihdam açığı %15 (2025-07) → %19 (2026-06) [D] (https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/). Lightcast: çapraz-fonksiyonel işbirliği talebi 2025 Q2→Q4 katlanarak arttı [K].
- **Kesişim/çatışma:** Rapor sıralamaları kariyer kararı için tek başına güvenilmez (K); güvenilir çekirdek = Anthropic hızlanma verisi + junior istihdam açığı (D).

### Aile 2 — Akademik/deneysel ikame-tamamlayıcılık kanıtı (tez ayakta, antitez ayakta)
- **Tez:** Vaccaro-Almaatouq-Malone meta-analizi: insan+AI ortalamada en iyi tekilden düşük; **insan AI'dan iyiyse kombinasyon kazandırır, AI iyiyse insan eklemek zarar verir** [K — yön arXiv'de doğrulandı, g-değerleri ham metinde bulunamadı] (https://arxiv.org/abs/2405.06087). FrontierMath 2024-11: tüm modeller <%2 [D] (https://arxiv.org/pdf/2411.04872); Gemini 3 Pro Tier1-3 %38, Tier4 %19 [D, Epoch açıklaması]; IMO 2025 altın: DeepMind resmî sertifikalı, OpenAI sertifikasız [D]. METR: %50-başarı görev ufku ~7 ayda ikileniyor [D] (https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/). Dell'Acqua "jagged frontier": sınır-dışı görevde AI kullananlar %19 daha az doğru [K — SSRN 403].
- **Antitez (¬):** "Doğrulama literatürü yok" iddiası **DÜŞTÜ**: PNAS Nexus etiketleme deneyi (AI-etiketli sert notlarda düzeltme %22 daha az), arXiv 2508.03714, PLOS One ayırt-etme deneyi [K]. METR kendi notu: ±2x hata payı, tüm görevler "self-contained", aylar-süren işbirlikli görev veri setinde yok [D] (https://metr.org/notes/2026-01-22-time-horizon-limitations/). Epoch resmî sayfasında Tier 4 için model verisi yok [D]; BenchLM "GPT-6 Astra Tier4 %97.6" üçüncül, resmî değil → ÇELİŞKİLİ. Otomasyon yanlılığı: AI desteğiyle doğruluk %66.7→%57.1 (anlamsız), 16 geliştirici AI ile %19 yavaş ama kendini %20 hızlı sanıyor [D].
- **Kesişim:** Aşırı-güvenme/otomasyon yanlılığı her iki şeritte de kanıtlı (SAĞLAM). Tamamlayıcılığın kaynağı "kim daha iyi"den ibaret değil, "farklı bilgi türü" de olabilir (antitez, K) → T2 daraldı ama yön ayakta.

### Aile 3 — Kantitatif meslek + eğitim yaklaşımı (tez K'ya düştü, antitez ayakta)
- **Tez:** Quant pratisyen: "AI işe alımı ikame etmez, çıtayı yükseltir; olasılık/istatistik/stokastik süreçler pazarlık dışı; üretim-kalitesinde kod eklendi" [K, tam metin açıldı ama dosya K-kapaklı] (https://abouttrading.substack.com/p/the-future-of-recruiting-in-quant, 2026-06-11). "500 ilan" analizi: stat/ML %92, A/B testi +14pp, nedensel çıkarım +17pp [K — 403, hiçbir bağımsız taramada yeniden üretilemedi]. MIT AI+Eğitim raporu (2026-08-13): sınavı AI-proof yapmak yerine "ne bilinmeli"yi yeniden sor; proje/sözlü/portföy [D-kalite ama dosya K-kapaklı]. Frontiers sistematik derleme (2026-03-25): AI-destekli öğrenme genelde olumlu; eleştirel-değerlendirme becerisi "boşluk" [K].
- **Antitez (¬):** Bastani vd. (PNAS, ~1000 lise öğrencisi, Türkiye): korumasız GPT ile pratikte +%48, **AI kaldırılınca sınavda −%17**; öğretmen-tasarımlı cevap-gizleyen tutor nötr (−0,004) [D, PMC üzerinden] (https://pmc.ncbi.nlm.nih.gov/ — makale: "Generative AI Can Harm Learning"). BLS: matematik meslekleri ortalamanın (%3) çok üstünde büyüyecek [D]; OR analisti rakamı iki denetimde farklı vintage (%12 vs %21,5) → ÇELİŞKİLİ. Stanford 2025-10 sözlü sınav önerisi [K]. PhD-seviye kantitatif yeteneğe talep/ücret artıyor [K].
- **Kesişim:** Kantitatif temel değer kaybetmiyor (D+K); korumasız AI ile öğrenme zarar veriyor (D); doğrulama becerisi öğretilmemiş boşluk (K, iki bağımsız işaret).

## 2. V26 örneklem-denetimi (özet; tam tablo `cc/…-v26-tez.md`, `…-v26-antitez.md`)
| Dosya | Sondaj | Tuttu / Tutmadı / Erişilemedi | Etki |
|---|---|---|---|
| tez-A1 | 6 | 5 / 1 / 0 (WEF 2026 "bulunamadı" beyanı yanlış) | tümü K |
| tez-A2 | 6 | 4 / 0 / 2 | ayakta |
| tez-A3 | 5 | 4 / 1 / 0 (BLS vintage) | tümü K |
| antitez-A1 | 5 | 4 / 1 / 0 (enterprise %75/77 kaynakta yok) | tümü K |
| antitez-A2 | 6 | 6 / 0 / 0 | ayakta |
| antitez-A3 | 5 | 5 / 0 / 0 | ayakta |

## 3. Sentez — hayatta-kalan çekirdek ve seri tasarımına çeviri
**Hayatta-kalan çekirdek (hakem, hepsi D):** ① tüketici augmentation %52>%45, kurumsala genellenemez · ② lisans-düzeyi görevde ~12x hızlanma · ③ FrontierMath 2024-11 <%2 · ④ Tier 4 resmî veri yok · ⑤ Gemini 3 Pro Tier1-3 %38 / Tier4 %19 · ⑥ IMO 2025 altın (DeepMind sertifikalı) · ⑦ METR 7-ay ikileme + ±2x + self-contained sınırı · ⑧ junior AI-maruz istihdam açığı %15→%19 · ⑨ korumasız AI ile öğrenme −%17 · ⑩ matematik meslekleri ortalama-üstü büyüme.
**Sayım:** SAĞLAM 8 · DARALDI 12 · DÜŞTÜ 1 · ÇELİŞKİLİ 1 (+3 alıntı-çelişkisi) · test edilmedi 4. Hayatta-kalma oranı 8/22 ≈ %36 (deneysel damga, m.40b v0.2).

### Konu listesi + öncelik (seri v0 → v1 önerisi; karar Salih'in)
| Öncelik | Konu | Seri başlığı (v0) | Ne değişir | Kanıt |
|---|---|---|---|---|
| **1** | **AI-çıktısı doğrulama + sınır bilgisi + otomasyon-yanlılığı** (hipotez→sınama, benchmark okuryazarlığı, "AI nerede yanılır" kataloğu) | YENİ başlık **I** (E ve H'den ayrılır) | L0: AI çıktısını elle yeniden-türetme egzersizleri; L1: benchmark/finansör okuma; L2: doğrulama deneyi tasarımı; L3: kendi alanında "AI hata atlası" | ⑨ D · otomasyon yanlılığı D · Dell'Acqua K · literatür var (T6 düştü) K |
| **2** | **Olasılık/istatistik + nedensel çıkarım + deney tasarımı** | C (L2-L3 öne çekilir), G-L3 | C-L2/L3 Faz 4-6'dan Faz 3-4'e; A/B + nedensel çıkarım G-L1'e iner | "pazarlık dışı" K · ⑩ D · A/B/nedensel büyüme K (rakam düştü, sinyal tekrarlıyor) |
| **3** | **Modelleme ve optimizasyon, uzun-ufuklu proje ölçeğinde** (LP/MILP+ML hibrit, belirsizlik altında karar) | D (L2-L3), F | D-L3 ve F-L3 proje çıktıları erken; portföy-ürün hedefi (junior açığına karşı kanıtlanabilir iş) | ⑦ D (self-contained görevler AI'da, işbirlikli/uzun görev ölçülmemiş) · ⑧ D |
| **4** | **Matematiksel akıl yürütme: ispat + ÖZGÜN problem kurma** | A | A-L2/L3 Putnam hedefleri "araç" düzeyine iner (teknik repertuar), L3 hedefi özgün problem/model üretimi olur | ⑥ D (kapalı-uçlu olimpiyat ikame) · ④⑤ D (araştırma-düzeyi belirsiz) |
| **5** | **Algoritmik düşünme + sistemli teşhis** | B, E | B-L2 rating hedefi kaldırılır; B'nin değeri karmaşıklık/indirgeme + AI kodunu okuma-doğrulama; E-L3 formel spesifikasyon korunur | ⑦ D · Bastani D (araç kapalıyken yapabilme) |
| **6** | **Karar verme + kalibrasyon** | F | F-L1 (100 tahmin, Brier) müfredat P19 ile birleşir | K (Tetlock geleneği; bu koşumda ölçülmedi) |
| **7** | **Paydaşa anlatma / çapraz-fonksiyonel iletişim** | H'ye ek | H-L2 öğretim yazıları "iş birimine anlatım" formatı alır | Lightcast K |
| kural | **Öğrenme protokolü:** çözüm aşamasında AI KAPALI; AI yalnız doğrulama/ipucu (tutor modu, cevap vermeyen) | H, ogrenme/README | seri kuralı olarak yazılır | ⑨ D |

### Düşen / daralan (seriye GİRMEYENLER)
- WEF/LinkedIn beceri sıralamaları tek başına gerekçe olmaz (K, sürüm oynaklığı). · "Problem solving" etiketi muğlak → seri kendi operasyonel tanımını korur (Pólya 4-satır + sayılabilir çıkış). · "AI-destekli öğrenme genelde olumlu" → korumasızsa zarar (D). · Prompt-mühendisliği ayrı başlık olmaz (LinkedIn tek-kaynak K).

## 4. Cevaplanmamış sorular (karar biriktirilmedi)
1. Anthropic kurumsal-API automation oranı (%75/77) gerçek mi, hangi sayfada? → ayrı canlı çekim.
2. FrontierMath Tier 4 güncel resmî sonuç (Epoch) — BenchLM %97.6 iddiası çapraz-doğrulanmadı.
3. Vaccaro g-değerleri PDF gövdesinden okunmadı; Dell'Acqua hiç açılamadı.
4. Nedensel çıkarım/A-B talep artışı için birincil ilan-verisi (Lightcast/Indeed ham) yok.
5. Salih kararı: v0 → v1 revizyonu (yeni başlık I, A/B hedef daraltma, faz sırası) uygulanacak mı?
