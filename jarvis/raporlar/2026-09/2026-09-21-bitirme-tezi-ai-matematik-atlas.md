# Bitirme tezi: AI × matematik — Atlas raporu (2026-09-21)

`[tip: rapor | kaynak: jarvis-terminal 09-21 | tarih: 2026-09-21 | hedef: raporlar/2026-09 | sema: v2 | koken: jarvis/claude-fable-5-1/2026-09-21]`

> **Mod:** ana-sıra (`~/sistem/jarvis`, Fable, worktree kapalı) · şerit: çift-atlas (tez ∧ ¬tez) + V26 + hakem · aile sayısı: **6** (A Navier-Stokes iddiası · B Tao Temmuz-Eylül 2026 · C AI×matematik durum ve araçlar · D meslek + Türkiye tez biçimi · E küresel üniversite biçimi ve örnekler · F matematikçi rolünün evrimi). Salih'in iki ara emri (09-21): "küresel en iyi üniversitelerden ilham, İTÜ'ye şartlanma yok" → aile E; "rolün nereye gideceğini doğru analiz et" → aile F; "fazladan token serbest" → hakem Opus'a eskalasyon (tetik a Salih beyanı + b V26 `TUTMADI` ≥3 olan rapor 5/12; emirde 6/12 yazılmıştı, hakem düzeltti).
> **Kanıt kısıtı (dürüstlük):** OpenAI'nin kendi duyuru sayfası 403 (iki ajan, üç deneme) · Princeton DataSpace 401, MIT tez sayfası 404, ETH Research Collection 429, Cambridge CST arşivi OAuth duvarı · oturumun paylaşımlı WebSearch bütçesi antitez aşamasında tükendi, V26 ve hakem yalnız WebFetch ile çalıştı · Tao'nun "üstel/exponential" sözü birincil kaynakta **bulunamadı** · Tao'nun 15 Eylül "Fast math, slow math" yazısı açıldı ama içeriği özetlenmedi · YÖK Tez Merkezi'nde AI×matematik lisans tezi aranmadı (form doldurulmadı).
> **Koşum:** 6 tez + 6 antitez + 3 V26 denetim (Sonnet) + 1 hakem (Opus) = 16 alt-ajan. Üretici raporlar `cc/rapor/2026-09/rapor-2026-09-21-bitirme-*.md` (15 dosya, 278 KB). Alt-ajan token toplamı §7'de.

## 0. Salih'in dört öncülü — kanıt ne diyor

| # | Öncül (Salih, 09-21) | Kanıt sonucu | Tek satır gerekçe |
|---|---|---|---|
| 1 | "AI geçen günlerde Navier-Stokes problemini çözdü" | **DARALDI** | Sağlam olan: Buckmaster (NYU) + Alpöge (Anthropic), Eylül 2026, **zorlamalı** IPM/Boussinesq/3D **Euler** için sonlu-zamanda patlama, Lean'de biçimsel, Tao 09-07 blogunda "remarkable achievement" (D). OpenAI 8 Eylül duyurusu (dahili model, ~10.000 ajan, 88 saat, K): hakemin açtığı belgeye göre kapsam **zorlamalı** 3D Navier-Stokes, düzgün ve kompakt destekli dış kuvvet, başlangıç verisi u=0 (D); **aynı belge zorlamasız (f=0) Millennium sorusunun açık kaldığını yazıyor** (D). Üretici raporların "kaynaklar çelişiyor" satırı hakemde düştü: OpenAI'nin iki ayrı sonucu var (zorlamalı NS + zorlamasız Euler), Buckmaster–Alpöge'ninki zorlamalı Euler; OpenAI'nin kendi metni 403. Clay: ana sayfa "Active", 11 Eylül duyurusu "apparently settled" ama çözen adlandırılmamış, **ödül yok**, değerlendirme kasıtlı yavaş (D). Sonuç: Clay'in zorlamalı (C/D) alternatifi için "teknik zafer" savunulabilir; Millennium'un asıl sorusu (A/B, zorlamasız) açık. |
| 2 | "Tao son 2 ayda AI'ın üstel gelişiminden bahsetti" | **BULUNAMADI** | "Exponential" için birincil kaynak yok (tez ve antitez ayrı ayrı aradı). Tao'nun asıl çerçevesi başka: ICM 2026 Philadelphia (gün yalnız ikincil kronolojide "24 Temmuz", birincil künyede yok; arXiv 2608.16753, tek yazar Tao, gönderim 08-17, D) kanıt sürecini **üretim–doğrulama–sindirim** diye üçe ayırıyor, darboğaz **sindirim** (K). Hız hakkında söylediği: "frenetic competition" eleştirisi (09-07/09-11, K). "Yavaşlamalıyız, hız çılgınca" alıntısı hakemde **düştü** (birincil zincir kapanmadı, AS-OF yok). |
| 3 | "AI'ın yöntemlerini insan düzeyine çevirecek araçlara ihtiyaç olacak" | **KISMEN DOĞRULANDI** | İhtiyaç tanımı güçlü: "100.000 satırlık kanıt… kimse anlamıyor" (konuşmadan iki ikincil aktarım, yazılı makalede yok; K, daraldı); 09-11 Fields bildirisi "problem çözme kavramsal anlayış için araç/vekil", insan "aktarım zinciri" (D, hakem birincilden); 09-12 konuk yazısı mantıksal-kanıt ↔ anlaşılır-kanıt ayrımı (K, yazar Tao değil); 09-15 konuk yazısı (Ben Antieau) "anlayabildiğinden hızlı çalışma" (K). **Somut araç önerisi hiçbir kaynakta yok** (X). Boşluk = tez fırsatı (§4 Ö1). |
| 4 | "Matematik mühendisinin görevi AI'ın yaptığı matematiği yönetmek olabilir" | **DARALDI / PARÇALANDI** | Hiçbir birincil kaynak "yönetici" tek-fonksiyon dilini kullanmıyor. Kanıt rolü **dört fonksiyona** bölüyor: doğrulama (ilanlar) · problem seçimi/küratörlük (Tao) · sindirim/açıklama/anlama (Tao, Fields 25, Buzzard "insana daha iyi anlama kazandırmak") · kavram-tasarımı (Venkatesh). Buzzard'a atfedilen "biçimsel önerme formülasyonu" hakemde düştü (kaynakta yok). Piyasa bugün yalnız **doğrulamayı** ödüyor: Harmonic 9 açık pozisyon, "Formal Verification Engineer", "Proof Engineer" (D); "AI yöneticisi" unvanı yok (D). Anthropic Economic Index Haziran 2026: matematik görevleri **en düşük özerklik** ucunda, yani insan hâlâ adım adım yönlendiriyor (D). |

## 1. Aile başına bulgular (tez / antitez / kesişim)

Etiketler üretici + antitez sonucudur; hakem düzeltmeleri §2'de. **D** birincil kaynak açıldı · **K** ikincil/tek-kaynak/AS-OF eksik · **X** çelişkili/düştü.

### Aile A — Navier-Stokes iddiası
- **Tez:** DeepMind+Brown+NYU+Stanford Eylül 2025 kararsız tekillik aileleri, Millennium çözülmedi beyanı [D] (arXiv 2509.14185; deepmind.google/blog/discovering-new-solutions-to-century-old-problems-in-fluid-dynamics/) · Buckmaster–Alpöge Eylül 2026 Lean-doğrulamalı patlama [D] (terrytao.wordpress.com/2026/09/07/…) · OpenAI 8 Eylül duyurusu [K] · Clay "Active" + ödül yok [D] (claymath.org/millennium-problems/navier-stokes-equation/ · claymath.org/news/navier-stokes-announcement/, 11 Eylül) · Fefferman: "kahramanlar Córdoba ve Martínez-Zoroa" (2023 makalesi) [D] · Tao "strip-mined" endişesi [D].
- **Antitez (¬):** A1 daraldı (2025 özetinde yeni aile yalnız IPM + sınırlı-alan Euler; Navier-Stokes açık problem olarak anılıyor) · A3 daraldı (Tao Lean kanıtını kendisi doğrulamadı, "hâlâ sindirmem gerekiyor") · A8 daraldı (tehdit/veri iddiası tek taraflı, Bubeck reddediyor) · A2/A4/A5/A7/A9/A10 çürütülemedi. En güçlü savunma: OpenAI'nin sonucu Clay'in **C/D (zorlamalı) alternatiflerini** karşılıyorsa "teknik/kısmi zafer" savunulabilir; **A/B (zorlamasız)** için savunulamaz.
- **Kesişim (hakem sonrası):** "AI-destekli, Lean-doğrulamalı yeni patlama sonuçları" sağlam; "Navier-Stokes çözüldü" düştü; "OpenAI ne kanıtladı" çelişkisi hakemde çözüldü (zorlamalı NS, u=0; f=0 açık), yalnız "kaç ayrı sonuç" sorusu ikincil düzeyde tek tip doğrulanmadı. Hakem notu: stanfordtechreview.com bağımsız yayındır, Stanford'la ilişkisi yok; Lean depo sayımları (1,68 M / 616 k satır) tek yayının kendi tablosu (K, daraldı).

### Aile B — Tao, 2026-07-21 → 09-21
- **Tez (kronoloji, hepsi D, Tao'nun kendi metinleri):** 07-24 ICM Philadelphia "Mathematics in the Age of AI" (teorth.github.io/tao-web/slides/age-of-ai-icm-2026.pdf; arXiv 2608.16753) · 08-13 Simons Foundation: "kuralları biz koyarız", başarı = kanıt ders kitabına girer · 08-27 Mathstodon: AI yazımı "önemsiz ayrıntıda oyalanıyor, yeni adımı aceleyle geçiyor" [K] · 09-07 blog Alpöge–Buckmaster · 09-10 AI×matematik kaynak listesi (crowdsourcing) · 09-11 **25 Fields madalyalısı "A Severe Misalignment of AI in Mathematics"** · 09-12 De Toffoli–Duede konuk yazısı "after-math" · 09-15 "Fast math, slow math" (açıldı, özetlenmedi) · 09-17 Gowers "Why I didn't sign" (karşı-görüş, Tao'nun blogunda).
- **Antitez:** B4 daraldı ("dikkate değer başarı" literal değil, Tao "remarkable achievement" yazdı) · B5 daraldı ("haftalarca" kaynakta yok) · B6 daraldı (Buckmaster "suçlamıyorum" diyor, "iddia etti" medya çerçevesi) · B13 daraldı ("yavaşlamalıyız" yalnız ikincil) · B3 daraldı (Mathstodon tarih damgası teyitsiz) · B1/B2/B7/B8/B9/B11/B12/B14/B15/B16 çürütülemedi. V26 ek bulgu: tez-B tablosundaki "Tao & Klowden" yazar satırı yanlış, arXiv API tek yazar Tao.
- **Kesişim:** Tao'nun 2 aylık mesajı **hız değil sindirim**: üretim ve doğrulama hızlandı, insan anlayışı geride kaldı; öncelik/atıf normları değişmeli; camia hızı kendisi belirlemeli. Gowers–Tao gerilimi gerçek ve kayıtlı (problem-çözme motivasyonu vs kavramsal anlayış).

### Aile C — AI × matematik durum ve araçlar (AS-OF 2026-09)
- **Tez:** IMO 2025 DeepMind resmî altın 35/42 (07-21) [D]; IMO 2026 Şangay: Huawei Celia + RedNote dots-note-3.0 42/42 iddiası [K], OpenAI/Anthropic/Axiom/Kimi K3 42/42 yalnız gayri-resmî yatırımcı testi [K] · Erdős veritabanı 08-03: 565 çözülmüş / 652 açık [D] (quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/); Bloom: "kimse okumadı" uyarısı [D] · Epoch FrontierMath Erdős 09-01: 68 problem, Lean; GPT-6 Astra resmî 2/68 (gayri-resmî 5/68), diğerleri 0 [D] (epoch.ai/latest/announcing-frontiermath-erdos) · Mathlib 288.718 teorem / 136.941 tanım [D] (leanprover-community.github.io/mathlib_stats.html) · PutnamBench 1.724 problem, Apache/MIT [D] · LeanCopilot MIT, CPU'da çalışır [D] · Goedel-Prover-V2 32B miniF2F %88,1 / %90,4 [D] (arXiv 2508.03613) · DeepSeek-Prover-V2-671B %88,9 [D] · PySR açık kaynak [D].
- **Antitez:** **C10 DÜŞTÜ** — arXiv 2607.07779 "proof explanation"ı ele almıyor, yanlış atıf. Doğru referanslar: **arXiv 2509.09726** (Lean → doğal dil, adım-informalization + özyinelemeli özetleme, anahtar noktaların %86'sı) · Visored 2606.17581 · LeanTutor 2506.08321 · ProofBridge 2510.15681 (ICLR 2026). 2026 literatür yoğunluğu **ters yönde** (doğal dil → Lean: Lean Atlas, ProofBridge, Goedel-Architect). C1 daraldı (OpenAI 07-19 kendi değerlendirmesi, resmî sertifika yalnız DeepMind). C4 daraldı (gayri-resmî 5/68). Donanım: LeanCopilot/PySR laptop; 32B model 24-48 GB VRAM `[?]`; 671B bulut.
- **Kesişim:** Araç ekosistemi açık kaynak ve lisans ölçeğinde erişilebilir; "AI kanıtını insana açıklama" alanı **kısmen çözülmüş, standart yöntem yok** (2509.09726 tek güçlü çalışma, ters yön kalabalık) → boşluk duruyor ama "açık sorun" değil "olgunlaşmamış alan" diye yazılmalı.

### Aile D — meslek öngörüsü + Türkiye tez biçimi
- **Tez:** BLS 2025-35: mathematicians **+%1**, statisticians **+%11** [D] (bls.gov/ooh/math/mathematicians-and-statisticians.htm) · WEF 2025: "Data Analysts and Scientists", "AI/ML Specialists" büyüyen; "mathematician" listede yok [D] · Anthropic Economic Index: "computer & mathematical" kategori kullanım payı %37,2 (Şub 2025) / ~%33 (Oca 2026) vs istihdam %3,4 [D] · Harmonic 9 açık pozisyon [D] (harmonic.fun/careers/) · İTÜ Matematik Müh. bitirme = **MAT4901/MAT4902** + 4 şablon (TR/EN) [D] (matmuh.itu.edu.tr/egitim/lisans/bitirme-staj) · YTÜ Matematik Müh. sayfası "hazırlanıyor" [D] · de Bruijn faktörü ~20, düşüşte [D] (teorth.github.io/tao-web/ai-views.html).
- **Antitez + hakem:** D2 daraldı (WEF'te "Data Scientist" değil "Data Analysts and Scientists"; "Mathematicians, Actuaries and Statisticians" taksonomide var, büyüme listesinde yok) · D7 daraldı (oran rapor sürümüne göre %30-37,2; sürüm yazılmadan kullanılamaz) · de Bruijn ~20 daraldı (Tao'nun sayfası ölçütün autoformalization ilerlemesiyle **eskidiğini** yazıyor; "o zaman böyle" notu) · diğerleri çürütülemedi. EK: AI becerisi ücret primi %25→%56 (2024→2025) ve AI ilanları +%78 [K, ikincil PwC aktarımı] → BLS'in dar "mathematician" kodu talebi eksik yakalıyor, talep komşu unvanlara kayıyor.
- **V26 uyarısı:** tez-D 17 sondajda **7 `TUTMADI`** (FrontierMath 338 soru/70 matematikçi, Tier-4 17/48, Buzzard Strachey Lecture, U-MATH "ICLR 2025", YTÜ kılavuz tarihi, Cambridge MPhil kurum bilgisi, Mathlib Initiative URL'si) → tez-D'nin bulguları **K tavanı**; yukarıda D bırakılanlar antitez-D'nin bağımsız açtıkları (BLS, İTÜ, Harmonic, Tao sayfası, lean-lang.org).
- **Kesişim:** Dar meslek kodu durgun, komşu kodlar (istatistik, veri, AI) büyüyor; İTÜ çerçevesi belgeli (MAT4901/4902), YTÜ belgesiz.

### Aile E — küresel üniversite biçimi + örnekler
- **Tez:** Princeton Math senior thesis: resmî sayfa sınırı yok, tipik 20-40 sayfa; dört ölçüt = alan bilgisi · özgün bakış · titiz mantık · net sunum [D] · Cambridge Part III essay 5.000-8.000 kelime [D] · Oxford Part C dissertation 7.500 kelime, mutlak tavan 50 sayfa [D] · Stanford CS senior project 5 yol [D] · Imperial: Buzzard "Formalising Mathematics" (Lean 4) [D] · CMU 15-311/15-217 "Logic and Mechanized Reasoning" [D] · Duke Math+ 2024 "AlgebraInLean" lisans araştırma projesi [D] · Harvard SEAS 2024 Leonard Tang lisans tezi: LLM stres-testi / matematiksel sağlamlık [D] (dash.harvard.edu/items/1639db4a-…).
- **Antitez:** **E12 ÇÜRÜDÜ** (ETH/EPFL/TUM'da "Bachelor thesis/project" var) · E11 daraldı (dar okuma ayakta, geniş okuma çürüdü) · E6 daraldı ("MSc" ifadesi sayfada yok). **Bulunan lisans tezleri:** TUM SCML Bachelor 2024 "Solving the three-body problem with neural networks" · 2025 "Learning Hamiltonian Functions of Handwritten Digits" · 2026 "Random Feature Hamiltonian Networks for N-Body Problems" [D] (cs.cit.tum.de/en/scml/teaching/student-projects/) · Harvard Tang 2024 [D] · Duke AlgebraInLean 2024 [D] · ETH "Formalizing Automated Market Makers in Lean 4" [429, bayraklı]. Jüri-risk uyarısı (özgünlük/eskime) ders düzeyinde **bulunamadı** (düşük güvenli negatif).
- **Kesişim:** "İyi lisans tezi" ortak ölçütü: **küçük ama tam katkı · titiz mantık + açık sınır beyanı · yoğun sunum (20-40 sayfa)**; kod teslimi matematik bölümlerinde açık kural değil. AI×matematik lisans işi bugün **ders-projesi ekosisteminde** (Lean dersleri) ve **fizik-bilgili ML** (TUM) kalıbında görünüyor; Lean-odaklı bağımsız lisans tezi arşivlerde nadir.

### Aile F — rolün evrimi
- **Tez:** O*NET 15-2021 Mathematicians 12 görev, AI yok [D] (onetonline.org/link/summary/15-2021.00) · Eloundou: işgücünün ~%80'i görevlerinin ≥%10'u LLM-maruz, ~%19'u ≥%50 [D, 2023 verisi] · Anthropic Economic Index Haziran 2026: matematik görevleri düşük özerklik [D] (anthropic.com/research/economic-index-june-2026-report) · Tao ICM: sindirim en az AI-optimize edilebilir aşama [D] · Fields 25 (09-11): insan = "aktarım zincirinin taşıyıcısı", şirket hızı topluluk doğrulama kapasitesini aştı [D] · Buzzard 07-20: AI karşı-örnekte insandan hızlı [D] · Venkatesh "Mathematics and the AI age": kavram-tasarımı / bilişsel ekonomi [D] (math.ias.edu/~akshay/research/HumanMath.pdf) · İlanlar: Formal Verification Engineer, Proof Engineer; "AI yöneticisi" yok [D] · Anthropic iç çalışma 2025-12-02: görev karmaşıklığı 3,2→3,8, insan müdahalesi −%33 [D] · METR 2025: deneyimli geliştirici −%19 hız, +%20 algı [D]; METR 2026-02-24 takip: yön belirsiz, güven aralığı sıfırı kapsıyor [D] · OpenAI 10.000 ajan, milyonlarca dolar [K, MIT Technology Review].
- **Antitez:** F2 daraldı (GPT-4 öncesi veri) · F6 daraldı ("biçimsel önerme formülasyonu" ifadesi kaynakta yok; Buzzard "içgörü/anlama" diyor) · diğerleri çürütülemedi. "Yönetici" tezine **zayıf-orta destek**: Vakil "joy of making sense of it all", Wegner "oversee the whole process" [K]. Daralma senaryosu (doğrulama da otomatikleşince insan halkası kalmaz) yalnız **alarm** olarak dile geliyor, hiçbir birincil kaynak savunmuyor.
- **Kesişim:** Ölçülmüş kayma yalnız yazılımda; matematik-özgü görev verisi yok. Uzman öngörüsü dört fonksiyonda birleşiyor. Analoji (agentic coding → matematik) taşınabilir ama METR bulgusu "hız algısı ≠ gerçek hız" uyarısı taşıyor.

## 2. V26 örneklem-denetimi + hakem

**V26 (kural-tabanlı: son üçlük URL'li + tüm sayısal + URL'siz; 12 rapor × 17 sondaj = 204):**

| Denetim | Raporlar | TUTTU | TUTMADI | URL YOK | ERİŞİLEMEDİ |
|---|---|---|---|---|---|
| 1 | tez-A · ¬A · tez-B · ¬B | 52 | 7 | 6 | 3 |
| 2 | tez-C · ¬C · tez-D · ¬D | 46 | 10 | 11 | 1 |
| 3 | tez-E · ¬E · tez-F · ¬F | 60 | 8 | 0 | 0 |
| **Toplam** | 12 | **158** | **25** | 17 | 4 |

Rapor başına `TUTMADI`: tez-A 1 · ¬A 3 · tez-B 0 (+1 yazar hatası) · ¬B 3 · tez-C 2 · ¬C 1 · **tez-D 7** · ¬D 0 · tez-E 3 · ¬E 1 · tez-F 3 · ¬F 1. Hata deseni: kurumun genel sayfasına atfedilen ayrıntı rakamının o sayfada olmaması (ikincil-özet sızıntısı) + raporların kendi iç sayım tutarsızlıkları. Tablolar: `cc/rapor/2026-09/rapor-2026-09-21-bitirme-v26-denetim-{1,2,3}.md`.

**Hakem (Opus, maskeli, `hakem` ajanı v0.1; rapor `cc/rapor/2026-09/rapor-2026-09-21-bitirme-ai-matematik-hakem.md`, 49 KB, aynen kaydedildi):**
- **Hayatta-kalma:** 113 iddia · **sağlam 56 / daraldı 25 / düştü 32** (· çelişkili 4, üst-küme) · etiket **D 8 / K 73 / X 32**. V26 tavanı 12 raporun 10'una uygulandı (yalnız ¬D muaf); D yalnız hakemin kendi 8 WebFetch'inden: Clay "Active" + ödül yok · Clay 09-11 duyuru metni · Fields bildirisi 25 imzacı + tarih · arXiv 2608.16753 tek yazar Tao · arXiv 2607.07779 içeriği · Tao ai-views.html künyesi · OpenAI belgesinin zorlamalı/u=0 kapsamı · aynı belgenin "f=0 açık" beyanı.
- **Usul bulguları:** maske ihlali 4 yerde (tez-B ve tez-C raporları "Salih'in iddiası" yazmış; hükme sokulmadı) · `teorth.github.io/tao-web/ai-views.html` Tao-onaylı **AI derlemesidir** (Claude derledi, Tao düzeltti; "omission is editorial"), tek başına D taşımaz; B/D/F ailelerinde onlarca iddianın tek dayanağı · Eloundou 2023 ve Anthropic Şubat-2025 rakamları eski kuşak, tasarım girdisi değil · WebFetch özetleyicisinin kesim-sonrası sayfalara "kurgusal" bayrağı gürültüdür, çürütme sayılmadı (hakem hafızasına usul dersi yazıldı).
- **Düşen 32'nin türleri:** yanlış atıf (Klowden yazarlığı · 2607.07779 konusu · Strachey · ICLR · Buzzard rol tanımı · kaynakta olmayan CMU/Oxford rakamları) · dayanaksız rakam ("7.200+ imzacı" iki ailede tekrar · "100 ajan/50 saat" · "26 madalyalı" · "dört AI 42/42") · iç sayım hatası (¬E, ¬F) · model karışması (PutnamBench 47→49 · "80× küçük" 8B'ye ait · Aristotle 5/6) · adversarial turda çürüyen geniş okuma (E12, E13) · çözülebilir sanılan çelişki (A10).
- **Çelişkili 4 (saklanmadı):** OpenAI kaç sonuç duyurdu (403) · talep: BLS %1 vs AI beceri primi %56 (taksonomik) · matematik görevleri "en düşük özerklik" (AEI 06) vs 10.000 özerk ajan (09): ölçüm birimi farkı olasılığı çıkarım `[?]` · IMO 2026 "officially graded" vs "model sitesindeki gönderi".
- **Sonnet-hakem ölçüm borcu (Karar 105 M1):** bu koşum Opus'la yapıldı, Sonnet taban ölçümüne sayılmaz.

## 3. Rol haritası 2036 → tez konusuna köprü

Kanıt kovaları (aile F + D):

| Yetkinlik | Kanıt kovası | Dayanak | Tez konusuna çeviri |
|---|---|---|---|
| Biçimsel doğrulama okuryazarlığı (Lean 4 / Mathlib) | (i) ölçülmüş: gerçek işe alım | Harmonic, Lean FRO ilanları [D]; Mathlib 288 bin teorem [D]; de Bruijn ↓ [D] | Her tez Lean bileşeni taşımalı (Ö1, Ö2, Ö3) |
| AI değerlendirme (eval) tasarımı | (i) ölçülmüş: kurumsal pratik | Epoch FrontierMath/Erdős protokolü [D]; Anthropic Economic Index görev-düzeyi [D]; U-MATH/UGMathBench [K] | Ö2 doğrudan, Ö1 ölçüt bileşeni |
| Sindirim / açıklama / sunum | (ii) uzman öngörüsü, güçlü uzlaşı | Tao ICM sindirim darboğazı [D]; Fields 25 aktarım zinciri [D]; De Toffoli–Duede anlaşılır-kanıt [D] | **Ö1** (önerilen) |
| Problem seçimi / biçimsel formülasyon | (ii) uzman öngörüsü | Tao "hangi sorular insan gelişimini teşvik eder" [D]; Buzzard [D, daraldı] | Ö3 konu seçimi, Ö5 model seçimi |
| Sayısal modelleme + ML (PINN, nöral operatör) | (i) ölçülmüş: araştırma pratiği | DeepMind 2025 tekillik keşfi [D]; TUM lisans tezleri [D] | Ö4, Ö5 |
| Ajan/sistem orkestrasyonu | (iii) spekülasyon | OpenAI 10.000 ajan [K tek kaynak] | Tez konusu **değil**; Ö2'de bütçe deneyi olarak sınırlı |
| Kavram-tasarımı / yeni dil | (ii) tek uzman | Venkatesh [D] | Lisans ölçeği dışı |

Salih'in hipotezi "AI'ın matematiğini yönetmek" bu tabloda tek satıra değil **ilk dört satıra** dağılıyor; bugün para ödenen satır birinci, Tao/Fields'ın "kaybediliyor" dediği satır üçüncü. Tez, ödenen yetkinliği (doğrulama) araç olarak, kaybedilen yetkinliği (sindirim) konu olarak alırsa hem 2026 piyasasına hem 2036 öngörüsüne oturur.

## 4. Tez konu önerileri (kök md.11: ne demek · ne yaparım · artı · eksi · öneri+gerekçe; önerilen ilk sırada)

Ortak çerçeve (aile E kesişimi): **20-40 sayfa yoğun metin + tekrarlanabilir kod deposu + açık sınır beyanı**; tip = araç + ölçme hibriti (tez-D taksonomisi iii+ii), İTÜ'de MAT4901/4902 çatısı [D]. Hesaplama gereksinimi ve süre kestirimleri `[?]` damgalı.

### Ö1 — **AI-üretimi biçimsel kanıtın sindirimi: Lean kanıtını insan-okunur açıklamaya çevirme ve anlaşılırlığı ölçme** (önerilen)
- **Ne demek:** Açık-kaynak bir kanıtlayıcının (Goedel-Prover-V2 / Kimina) miniF2F ya da PutnamBench üzerinde ürettiği Lean 4 kanıtlarını alıp, (a) doğal-dil açıklamaya çeviren bir hat kurmak (taban: arXiv 2509.09726 adım-informalization + özyinelemeli özetleme; kıyas: düz LLM çevirisi, ham Lean), (b) "anlaşılırlık" için ölçülebilir bir ölçüt tanımlamak (insan değerlendirici paneli: matematik mühendisliği öğrencileri n≈10-20 `[?]`; doğruluk-koruma: açıklamanın Lean kanıtına sadakati otomatik kontrol), (c) üç yöntemi ölçütle kıyaslamak. Türkçe çıktı ayrı bir katkı satırı.
- **Ne yaparım:** Ekim-Kasım Lean 4 + Mathlib + LeanCopilot kurulum, Buzzard ders malzemesi, 2509.09726 ve Tao 2608.16753 okuma, korpus (30-50 kanıt `[?]`) seçimi · Aralık-Ocak hat v0 + sadakat kontrolü · Şubat-Mart ölçüt + insan değerlendirme · Nisan-Mayıs yazım · Haziran teslim `[?]`.
- **Artı:** Tao'nun iki ayda en çok tekrarladığı darboğaza (sindirim) doğrudan cevap [D] · literatür boşluğu duruyor (tek güçlü çalışma, ters yön kalabalık) [D] · hesaplama düşük (API + CPU; 32B model gerekmez, hazır kanıt çıktıları kullanılır) · jüri Lean bilmese de çıktı doğal dil, değerlendirilebilir · 2036 yetkinliklerinden üçünü (doğrulama, eval, sindirim) tek tezde kanıtlar · küresel "küçük ama tam katkı" normuna oturur.
- **Eksi:** "İyi açıklama" ölçütünü tanımlamak tezin en zor kısmı, kötü tanımlanırsa tez görüşe düşer · alan hızlı eskir (2027'de daha iyi çeviri araçları çıkabilir) · 2509.09726 ile fark açıkça yazılmazsa özgünlük itirazı · LLM API bütçesi (kestirim `[?]`, ölçülmeli) · Lean öğrenme eğrisi 6-8 hafta `[?]`.
- **Öneri + gerekçe:** **Birincil aday.** Dört öncülün ikisine (3 ve 4) kanıtla bağlanan tek konu; risklerin hepsi tasarımla yönetilebilir (ölçüt = sadakat + okunabilirlik iki eksen, fark = AI-üretimi kanıt + Türkçe + insan paneli).

### Ö2 — **Açık-kaynak kanıtlayıcılarda başarı–maliyet eğrisi: küçük ölçekli FrontierMath-Erdős protokolü**
- **Ne demek:** Epoch AI'nin 09-01 protokolünü (problem başına bütçe, Lean doğrulama) miniF2F/PutnamBench alt kümesine (100-200 problem `[?]`) ve 2-3 açık modele (Goedel-Prover-V2 8B/32B, Kimina 8B, LeanCopilot) uygulayıp pass@k × token/süre bütçesi eğrisi çıkarmak; problem sınıfı (cebir/analiz/sayı teorisi) etkisini ölçmek.
- **Ne yaparım:** Kurulum + veri kümesi bölme (kirlenme kontrolü: yayın tarihi sonrası problemler) · koşum matrisi · istatistik (güven aralıkları) · yazım.
- **Artı:** Tamamen ölçülebilir, tekrarlanabilir; Epoch şablonu hazır [D]; eval yetkinliği doğrudan; Salih'in depo pratiğiyle (eval ajanı Solon, katman-ölçüm) aynı disiplin.
- **Eksi:** miniF2F herkese açık → kirlenme itirazı · 32B model için 24-48 GB VRAM `[?]` ya da bulut maliyeti · sonuçlar aylar içinde eskir · "yeni bilgi" küçük (eğri, teorem değil).
- **Öneri + gerekçe:** İkinci aday ya da **Ö1'in ölçme omurgası** olarak gömülür (Ö1'de kanıt korpusu zaten bu koşumdan çıkar).

### Ö3 — **Müfredattan bir konunun Lean 4'te biçimselleştirilmesi + insan–AI iş bölümü ölçümü**
- **Ne demek:** Matematik mühendisliği müfredatından Mathlib'de eksik ya da zayıf bir konu (örn. sayısal analizde bir yakınsama teoremi, lineer cebirde bir ayrışma) seçip Lean 4'te biçimselleştirmek; süreçte hangi adımı insan, hangisini AI (LeanCopilot/LLM) yazdı kaydını tutup de Bruijn faktörü ve AI-katkı oranını ölçmek. Emsal: Duke AlgebraInLean [D], Imperial dersi [D].
- **Artı:** Çıktı nesnel (derleyici geçer/geçmez) · Mathlib'e katkı ihtimali (dış onay) · doğrulama yetkinliği en doğrudan · Tao'nun "vatandaş matematikçiliği" (lisans öğrencisi modüler görev) çerçevesine oturur.
- **Eksi:** Jüri Lean bilmiyorsa özgünlük değerlendirmesi zor · konu Mathlib'de zaten varsa iş boşa gider (önce `mathlib_stats` + arama) · Tao'nun "derin öğrenme kaybı" uyarısı: AI yazdıysa öğrenci ne öğrendi sorusu jüride gelir.
- **Öneri + gerekçe:** Üçüncü; Ö1'e giriş modülü olarak Lean pratiğini sağlar.

### Ö4 — **PINN / nöral operatör + sembolik regresyon: PDE çözümünden kapalı forma dönüş**
- **Ne demek:** 1D/2D Burgers ya da düşük-Re Navier-Stokes'u PINN/FNO ile çözüp FEM/FD ile adil kıyaslamak; PySR ile çözümden kapalı-form denklem geri çıkarmak; gürültü dayanıklılığı. Emsal: TUM bachelor tezleri (fizik-bilgili ML) [D], Springer 2025 [K].
- **Artı:** Uygulamalı matematik kimliğine en yakın · sentetik veri, dış veri gerekmez · iyi belgelenmiş araçlar · Navier-Stokes ile tematik bağ.
- **Eksi:** "Yenilik" bulmak zor (kalabalık alan) · adil kıyas yapılmazsa jüri itirazı · GPU orta · AI×matematik "yeni çağ" temasına Ö1-Ö3 kadar bağlanmaz (AI burada araç, konu değil).
- **Öneri + gerekçe:** Klasik güvenli seçenek; Salih'in "10 yıl sonraki form" hedefine en az bağlanan.

### Ö5 — **Tekillik avının yeniden üretimi: DeepMind 2025 yönteminin oyuncak modelde tekrarı**
- **Ne demek:** arXiv 2509.14185'in PINN + yüksek-hassasiyet Gauss-Newton yaklaşımını 1D Burgers kendine-benzer patlama ya da basitleştirilmiş IPM üzerinde yeniden üretmek; kararsız profil bulma ve hassasiyet (kaç basamak) raporlamak.
- **Artı:** Navier-Stokes tartışmasına en doğrudan bağ · yeniden-üretilebilirlik (reproducibility) kendisi 2026'da değerli bir katkı türü · doğrulama + sayısal yetkinlik birlikte.
- **Eksi:** Hesaplama ve hassasiyet gereksinimi yüksek `[?]` · orijinal ekip 4 kurum, lisans öğrencisi tek · başarısızlık riski yüksek, "başarısız yeniden üretim" tezi jüriye anlatmak zor.
- **Öneri + gerekçe:** Yüksek risk / yüksek görünürlük; yalnız danışman bu alanda çalışıyorsa.

### Ö6 — **Meta tez: AI çağında matematik mesleğinin görev-düzeyi analizi**
- **Ne demek:** O*NET 12 görev × Anthropic Economic Index otomasyon/artırma × Fields bildirisi / Tao–Gowers gerilimi; Türkiye matematik mühendisliği mezun/öğrenci anketi `[?]`.
- **Artı:** Salih'in "rolü doğru analiz etmek" isteğine birebir · bu raporun kanıt tabanı hazır.
- **Eksi:** Matematik mühendisliği jürisi için "kanıt mı görüş mü" riski yüksek · matematiksel içerik zayıf · anket etik/izin süreci.
- **Öneri + gerekçe:** Bağımsız tez **değil**; Ö1-Ö5'ten hangisi seçilirse onun giriş bölümü (motivasyon) olarak 5-8 sayfa `[?]`.

**Özet hüküm:** Ö1 birincil (Ö2 ölçme omurgası, Ö3 giriş modülü, Ö6 motivasyon bölümü); Ö4 güvenli B planı; Ö5 yalnız danışman-koşullu.

## 5. Salih'in eli — ilk iki hafta
1. Danışman görüşmesi: Ö1 tek sayfa özet (bu rapor §4 Ö1) + "yazılım/araç bileşenli tez MAT4901'de kabul mü" sorusu (İTÜ şablonları matmuh.itu.edu.tr/egitim/lisans/bitirme-staj) · bölümde Lean/biçimsel yöntem bilen öğretim üyesi var mı `[?]`.
2. Kurulum: Lean 4 + Mathlib + LeanCopilot (github.com/lean-dojo/LeanCopilot, CPU yeter) · PutnamBench klonu.
3. Okuma sırası: Tao ICM makalesi arXiv 2608.16753 → Fields bildirisi (terrytao.wordpress.com/2026/09/11/…) + Gowers cevabı (09-17) → arXiv 2509.09726 → Tao'nun 09-10 kaynak listesi.
4. Karar: Ö1 mi Ö4 mü (danışman + donanım cevabına göre); karar Salih'in.

## 6. Cevaplanmamış sorular (karar biriktirilmedi — m.41)
1. OpenAI'nin 8 Eylül kanıtı zorlamasız Navier-Stokes'u kapsıyor mu (birincil metin 403)?
2. Tao'nun 09-15 "Fast math, slow math" yazısı ne diyor (açıldı, özetlenmedi)?
3. İTÜ MAT4901/4902'de araç/yazılım ağırlıklı tez "Bitirme Tezi" mi "Bitirme Projesi" mi sayılıyor; jüri Lean değerlendirebilir mi?
4. YÖK Tez Merkezi'nde AI×matematik lisans/yüksek lisans tezi var mı (aranmadı)?
5. Ö1 için LLM API bütçesi ve insan panel büyüklüğü (ölçülmeli, `[?]`).
6. OpenAI kaç ayrı sonuç duyurdu (zorlamalı NS + zorlamasız Euler okuması ikincil düzeyde tek tip doğrulanmadı; hakem çelişki 1).
7. AEI "en düşük özerklik" ile "10.000 özerk ajan" gerilimi ölçüm birimi farkı mı (hakem çelişki 3; hiçbir kaynak açıklamıyor).

## 7. Koşum kaydı
- Alt-ajan: 6 tez (76-105 bin token, 26-41 araç çağrısı) · 6 antitez (85-112 bin, 29-62 çağrı) · 3 V26 (156-178 bin, 34-50 çağrı) · hakem Opus 238 bin token, 26 çağrı, 12 dk. Toplam 16 koşum ≈ **1,77 M** alt-ajan token (bildirim sayaçları toplamı); duvar saati 14:46 → 15:41 ≈ 55 dk.
- Kısıt: WebSearch paylaşımlı bütçesi (200 çağrı) antitez aşamasında tükendi → V26 ve hakem yalnız WebFetch; Jarvis kendi koşumu için tahmin yazmaz (KB-02).
- Hayatta-kalma satırı senaryo-defterine yazıldı (09-21 gözlem satırı). Hakem ajanı kendi hafızasına 2 usul dersi bıraktı (`jarvis/.claude/agent-memory/hakem/`): özetleyici "kurgusal" bayrağı · doğrulama bütçesi hedefleme.
- md.49 hook uyarısı bu istekte tetiklendi (regex `staj|galeri`); konu bitirme tezi, staj/galeri değil → yanlış pozitif; kanon yazılmadı, karar alınmadı, yalnız rapor + gözlem satırı + harness hafızasına kullanıcı-bağlamı.
