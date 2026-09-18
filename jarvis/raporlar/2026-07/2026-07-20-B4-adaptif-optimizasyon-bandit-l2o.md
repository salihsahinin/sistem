# B4 — Adaptif-Optimizasyon (Non-Stationary Bandit O6 + Meta-Learning/L2O O11) — Atlas Raporu (2026-07-20)

> **Mod:** yan-oturum (m.41 · CC = yan oturum, kanon KİLİTLENMEDİ, karar ALINMADI) · şerit: çift-atlas (tez ∧ ¬tez) · aile sayısı: **5** (bandit-nedir/O6 · meta-learning-nedir/O11 · küçük-N fizibilite · JARVIS-uyum/V39-K-020 · ünlü-isimler) → 10 literatür/pratisyen şeridi + 1 adaptif-optimizasyon karar envanteri.
> **Kanıt kısıtı (dürüstlük):** Bu turda birincil PDF'lerin çoğu (arXiv, Optuna docs, distill.pub) egress-403 → bulgular WebSearch-özeti **[K]**; kanon dosyaları doğrudan okundu **[D-kanon]**; Sutton & Barto kitabı yerleşik künye **[D]**. Garivier-Moulines kaynağı kanon-içinde zaten "doğrulanmadı" damgalı.
> **"Nedir" notu:** Terimler teknik — §0 kutusunda ve §1 Aile A/B'de sade tanım var.
> **Okuma sırası (Fable):** §0 Carvis sentezi (+ "nedir" kutusu) + §4 dürüst bayraklar → yeterli. Detay: §1 aile bulguları · §2 ünlü isimler · §3 optimizasyon-kararlarımızın kategori+kontrolü · §5 V26 · §6 açık sorular.

---

## §0 — Carvis sentezi (önce oku)

**"NEDİR" (sade tanım):** **Multi-armed bandit** = k kol (seçenek), çek=dene, ödül gözlemle, keşif↔sömürü dengesi. **Non-stationary** = ödül dağılımı zamanla KAYAR (model güncellenir, fiyat düşer) → durağan optimizer geç fark eder; çözüm eski gözlemi iskonto/pencerele (discounted/sliding-window UCB). **Meta-learning** = "öğrenmeyi öğrenme" (MAML: iyi başlangıç öğren). **L2O (Learning-to-Optimize)** = optimizer'ın KENDİSİNİ öğren. **Warm-starting** = geçmiş sonucu başlangıç yap (öğrenme yok). Veri-açlığı sırası: warm-start < meta-learning < L2O. O6 = non-stationary bandit; O11 = meta-learning/L2O.

**En sağlam kesişim (beş ailenin İKİ şeridinin de + envanterin ortak dediği):**

1. **FORMEL uç uygulanamaz, HAFİF uç uygulanabilir — keskin bölünme.** Formel bandit-regret-makinesi + tam-L2O JARVIS'in küçük-N (~5-15 karar) + non-stationary + gürültülü-evaluator + tek-seferlik rejiminde çöker (A/B/C/E-antitez + D-antitez YAKINSIYOR). Hafif uç (warm-start + **pilot-korumalı** successive-halving-budama + son-gözlem-iskonto + m.42-zorunlu-keşif) MÜMKÜN ve JARVIS'in V39/K-020/m.37/m.42/m.35'i ZATEN orada (A/B/C/D-tez). [D/K]

2. **O6/O11 egzotik sıçrama DEĞİL — JARVIS'in zaten OLDUĞU şeyin prensipli ADI.** Optuna-Hyperband (K-020) bir multi-fidelity bandit; V39'un evrimsel dizi-araması garantisiz-PBT; DEHB/PB2 prensipli melez; m.42(f) çeşitlilik-bütçesi = keşif-terimi (ε_n=1/n → O(log n) teoremi, 07-18 raporu); m.35 = bandit gövdesi (kombinasyon=kol, beklenti-vektörü=posterior, kalan-zaman=bütçe). **JARVIS bandit iskeletine bağımsızca vardı.** Ve 07-18 raporu O5=Contextual-TS/BOHB, O6="NEXT WAVE #1", O11="ERKEN" diye ZATEN sınıflamış. [D-kanon]

3. **BAĞLAYICI KISIT hiçbir zaman algoritma değil — ÖDÜL/EVALUATOR SİNYALİ.** A-tez "asıl darboğaz ödül-metriği tanımı"; C-antitez κ≈0.5 + regresyonel-Goodhart (gürültüyü optimize etmek); B1/B3/A5 ile YAKINSAK (LLM-judge güvenilmez, credit-assignment küçük-N'de tanımsız). Güvenilir ucuz kalite-sinyali OLMADAN her adaptif optimizer gürültüyü optimize eder. Envanter bunu her yerde işaretlemiş (V39 "evaluator ŞART", A5 credit-assignment, senaryo-defteri "kalite boş/tahmini"). [D/K]

4. **Non-stationary GERÇEK — ve JARVIS zaten KURUMSAL düzeyde iskonto ediyor.** m.29 "eşikler zamanla kalibre" = kayma-kabulü; Sutton §2.5 sabit-α "eski veriyi unut" = JARVIS'in "kapsül üzerine yazılır, bayat kural arşive iner" (m.22). Yani non-stationary "iskonto/pencere" ilkesi ZATEN kurumsal hafızada uygulanıyor; O6 onu (gelecekteki) formül için biçimselleştirir. [D-kanon]

5. **Zamanlama: ŞİMDİ DEĞİL — ve mevcut erteleme DOĞRU.** V39 koşulmadı, K-020 bekleyen, m.5/m.13/m.36 donmuş-kapsam, ödül-sinyali yok; doğru tetik (POP + m.30b'de zaten kanon) = veri-muslukları dolup (PortRisk hasadı + senaryo-defteri) varyant held-out'ta varsayılanı YENİNCE. O6/O11 doğru şekilde deferred/C_carry≈0. Dürüst konum, ŞİMDİ kurmayı DEĞİL, mevcut ertelemeyi ONAYLAR. [D-kanon]

**JARVIS'e ne demek (gözlem, KARAR DEĞİL — m.41):**

- **Dürüst manşet:** B4 büyük ölçüde JARVIS'in mevcut 07-18 yakınsayan-formül analizini DOĞRULUYOR — bandit iskeleti (m.35/m.42/V39/K-020) zaten kanon-ya-da-kuyrukta, O6/O11 zaten doğru şerhlerle ertelenmiş ("NEXT WAVE #1", "ERKEN"). Net-yeni: (a) FORMEL/HAFİF bölünmesi açıkça (formel-uygulanamaz / hafif-uygulanabilir-ama-sinyal-kapılı); (b) ödül-sinyali TÜM B-serisinde (B1/B3/A5/B4) bağlayıcı-kısıt olarak teyitli; (c) Sutton-unutma ≈ kapsül-üzerine-yazma yakınsaması; (d) küçük-N-GÜVENLİ varyant şerhi (pilot-korumalı budama, agresif eleme DEĞİL).
- **En yüksek-kaldıraçlı üç gözlem (harita, öneri değil):** (1) O6/O11'i ŞİMDİ KURMA — mevcut erteleme (C_carry≈0, tetik=veri+held-out-galibiyet) doğru; (2) V39/K-020'nin ZATEN hafif adaptif-optimizer iskeleti olduğunu tanı, tetiklenince küçük-N-GÜVENLİ biçimi kullan (median-pruner+startup-trials / racing-eşiği + non-stationarity için iskonto), agresif SH DEĞİL; (3) ÖNCE kurulacak tek şey **güvenilir ödül/evaluator sinyali** — o olmadan her optimizer gürültüyü optimize eder; bu gerçek kapı-ön-koşulu (O5→O6→O11 hepsi ona bağlı) ve B1/B3/A5'in bulduğu AYNI darboğaz.
- **En keskin dürüst gerilim:** non-stationary + küçük-N ÇİFTE bağ — O6'yı GEREKLİ kılan kayma, küçük-N tahmini İMKÂNSIZ kılan kaymayla aynı; yani O6 "ilkece gerekli ama onu gerektiren rejimde kullanılamaz" N büyüyene dek.

---

## §1 — Aile başına bulgular (çift-atlas)

### Aile A — Non-stationary bandit (O6)
- **Tez:** (Tanım §0.) Kollar=model/kombinasyon (m.37/V39), ödül=kalite÷(token×zaman); non-stationary uygun (ortam gerçekten kayıyor); en uygun aile muhtemelen D-UCB/iskontolu-Thompson. [K]
- **Antitez (¬):** Regret-sınırları çok-çekim asimptotiği (Lai-Robbins log T/KL); non-stationary İSPATLI daha zor (Ω(√KMT) > Ω(√KT)); çifte-bağ (pencere hem-uzun-hem-kısa olamaz); kayma-tespiti min-SNR ister; minimax T^{2/3}≈4.6 (T~10) → koşum bitmeden öğrenme yok; A5 (ödül-sinyali zaten tanımsız); m.5. [K]
- **Kesişim:** Çerçeve GERÇEK ve JARVIS-uyumlu AMA asıl darboğaz **ödül-metriği tanımı**, algoritma değil; formel-makine küçük-N'de anlamsız, kurumsal-iskonto (kapsül-üzerine-yazma) zaten çalışıyor.

### Aile B — Meta-learning / L2O (O11)
- **Tez:** (Tanım §0.) Warm-start bugün uygulanabilir (Optuna `source_trials`, düşük-risk); V39=hiperparametre-uzayı, m.37=politika, evaluator-skorları=warm-start kaynağı. Kademeli reçete: warm-start → meta-öğrenilmiş m.37 politikası → tam-L2O ancak bol koşum+dürüst-evaluator. [K]
- **Antitez (¬):** L2O binlerce görev+ağır hesap ister (VeLO ~4000 TPU-ay); meta-overfitting 200 görevle bile şiddetli; dağılım-kayması çöküşü (O6 ile çifte-zorluk); learned-optimizer kararsız (baseline'ları geçmiyor); NFL — alan-bilgisi (m.37/m.25) küçük-N'de yener; m.5/V25. [K]
- **Kesişim:** Tam-L2O fena halde ERKEN + OOD-kırılgan; tek uygun meta-form = **hafif-meta (warm-start + Brier-kalibrasyon)**, Brier tek-ödül OLMADAN. Dürüst karşı: dağılım-İÇİ kazanç var (Metz) → "L2O değersiz" fazla güçlü.

### Aile C — Küçük-N fizibilite
- **Tez:** Küçük-N adaptif-optimizasyon MÜMKÜN (basit biçimde): successive-halving/Hyperband/ASHA, Optuna MedianPruner (`n_startup_trials=5`=küçük-N koruması), irace/F-race (Friedman-testi), TPE/BO, basit bandit. **V39'un pilot-5→3'erli-parti→>%5-kapı→tavan-15'i ZATEN insan-döngülü successive-halving; K-020 Optuna küçük-N-GÜVENLİ somutlar.** [K]
- **Antitez (¬):** SH güvenilir erken-sinyal İSTER yoksa yanlış-eleme; çok-fidelity ucuz↔gerçek korelasyonu çok-yüksek ister (JARVIS'te ÖLÇÜLMEMİŞ); küçük-N yüksek varyans ("iyileşme"=gürültü, 30-40 örnek→2.5-3.3pt sapma); evaluator güvenilmez (κ≈0.51-0.56); güvenilirlik≠geçerlilik; gürültülü-metrik = regresyonel-Goodhart; >%5-kapı güç-analizinden geçmez. [K]
- **Kesişim:** Pruning/racing MEKANİK mümkün AMA **güvenilir ucuz-sinyale KOŞULLU**; JARVIS'te o sinyal (öznel-çıktı + κ≈0.5 evaluator) yok → fizibilite ÖNCE evaluator-sorununu çözmeye bağlı. Açık [?]: JARVIS ucuz-proxy↔gerçek-kalite korelasyonu ölçülürse antitez doğrudan test edilir.

### Aile D — JARVIS-uyum (V39/K-020)
- **Tez:** K-020 Optuna-Hyperband ZATEN multi-fidelity bandit; V39 evrimsel-arama = garantisiz-PBT, PB2/DEHB prensipli sürüm (DEHB "V39 mı K-020 mı" çözer); O6 non-stationary GERÇEK (m.29 = kayma-kabulü; standart Optuna sabit-ödül varsayar → O6 eksik-parça); model-seçimi = contextual-bandit; m.42 = keşif-terimi; **KRİTİK: LLM'ler kendi başına greedy'ye kaçar → dış bandit-kontrolör + m.42 gerek**. [K]
- **Antitez (¬):** Optimize edilecek süreç YOK (V39 ham, K-020 bekleyen, ödül-sinyali üretilmemiş); m.5 erken-optimizasyon; Knuth 97/3; **m.37'nin KENDİSİ "optimizasyon hamlelerini minimize et" der**; m.25/m.31 elle-ölçek "yeterince iyi" (YAGNI); m.13/m.36 donmuş-kapsam; doğru yön DAHA AZ katman. [D-kanon]
- **Kesişim:** İki şerit HEMFİKİR — bandit iskeleti zaten kanon/kuyruk, O6/O11 zaten doğru ertelenmiş. Ayrışma: D-tez "prensipli sürüm hazır (DEHB/PB2)", D-antitez "ama ŞİMDİ DEĞİL"; uzlaşı = mevcut erteleme (tetik=veri+held-out) DOĞRU, meşru çekirdek (m.35) korunur.

### Aile E — Ünlü isimler / pratisyen
- **Tez:** Sutton (RL Böl.2 bandit + §2.5 non-stationary sabit-α unutma = **kapsül-üzerine-yazma kurumsal karşılığı**; Bitter Lesson), Lattimore-Szepesvári (Böl.31 discounted/sliding-UCB), Finn (MAML), Andrychowicz/Li-Malik (L2O), Akiba (Optuna), Li (Hyperband), Balandat (BoTorch) — tanınmış isimler geliştirdi/savunuyor. [D/K]
- **Antitez (¬):** Karpathy "Don't be a hero" (basit-baseline-önce); Knuth "premature optimization root of all evil"; learned-optimizer Adam'ı güvenilir geçemiyor (Celo/VeLO); Bergstra-Bengio "random search çoğu zaman yeterli"; Meta-Baseline; küçük-veri meta-overfitting. "Önce basit, önce ölç; L2O son çare." [D/K]
- **Kesişim:** Gerilim ekseni Sutton-Bitter-Lesson (öğrenmeyi ölçekle) ↔ Karpathy (önce ölç). Sağlıklı sentez zaman-sıralı: önce ölç/sinyal (Karpathy) → non-stationary unutan-adaptasyon (Sutton/Lattimore) → gerekirse budamalı AutoML (Hyperband/Optuna) — küçük-N-şimdi → öğrenme-sonra.

---

## §2 — Ünlü isimler / kaynak tablosu

| İsim | Yöntem | Özü | JARVIS bağı | Kaynak | Etiket |
|---|---|---|---|---|---|
| Sutton & Barto | Bandit + non-stationary sabit-α | Eski veriyi unut (üstel-yakınlık-ağırlık) | **Kapsül-üzerine-yazma + bayat-kural-arşiv (m.22) = kurumsal iskonto** | [incompleteideas.net/book](http://incompleteideas.net/book/the-book-2nd.html) | [D] |
| Sutton | Bitter Lesson | Ölçeklenen öğrenme > el-yapımı bilgi | m.35 farklılaşma (uzun-vade); Karpathy ile gerilim | [incompleteideas.net](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) | [K] |
| Lattimore & Szepesvári | Bandit Algorithms Böl.31 | Non-stationary'de iskonto/pencere zorunlu | O6 = model-seçim bandit'inin non-stationary düzeltmesi | [banditalgs.com](https://banditalgs.com/) | [D]/[K] |
| Chelsea Finn | MAML | İyi başlangıç öğren, az-atışla uyum | Kapsülden-devralma / few-shot onboarding analoğu | [arXiv 1703.03400](https://arxiv.org/abs/1703.03400) | [K] |
| Andrychowicz / Li-Malik | L2O | Optimizer'ın kendisini öğren | O11 = Carvis köprü-ayarlamasının otomasyon ufku | [1606.04474](https://arxiv.org/abs/1606.04474) · [1606.01885](https://arxiv.org/abs/1606.01885) | [K] |
| Akiba (Optuna) | Successive-halving + TPE | Budamalı, programlanabilir HPO | K-020 = V39 pruner'ı; küçük-N-güvenli MedianPruner | [KDD 2019](https://dl.acm.org/doi/10.1145/3292500.3330701) | [K] |
| Lisha Li (Hyperband) | Bandit-tabanlı HPO | Kaybedenleri erken öldür | V39 pilot-parti-tavan = insan-döngülü Hyperband | [arXiv 1603.06560](https://arxiv.org/abs/1603.06560) | [K] |
| Balandat (BoTorch/Ax) | MC Bayes-optimizasyon | Pahalı kara-kutuda min-deneme | Her koşum pahalıysa örneklem-verimli arama | [arXiv 1910.06403](https://arxiv.org/abs/1910.06403) | [K] |
| Karpathy | "A Recipe" | Önce ölç, kahraman olma | Erken-meta-tuning'e pragmatik FREN (V1/m.5) | [karpathy.github.io/recipe](http://karpathy.github.io/2019/04/25/recipe/) | [K] |
| Knuth | Premature optimization | Efor ölçülmüş kritik %3'e | m.5 erken-optimizasyon yasağının atası | [ACM 1974](https://dl.acm.org/doi/10.1145/356635.356640) | [D] |
| Bergstra & Bengio | Random search | Rastgele ≥ grid, çoğu zaman yeter | Karmaşık HPO'dan önce basit-baseline | [JMLR 2012](https://jmlr.org/papers/v13/bergstra12a.html) | [D] |
| VeLO / Metz (karşı) | Learned optimizer | 4000 TPU-ay, genellemiyor / dağılım-içi kazanır | L2O erken+OOD-kırılgan; ama değersiz değil | [2310.18191](https://arxiv.org/html/2310.18191v2) · [1703.04813](https://arxiv.org/pdf/1703.04813) | [K] |

---

## §3 — Optimizasyon kararlarımızın kategori + kontrolü

| Karar/kimlik | Adaptif-optimizasyon denkliği | Statü | Kontrol (bu araştırmanın verdiği) |
|---|---|---|---|
| **O5 yakınsayan formül** | Contextual-TS + BOHB + warm-start | deferred (07-18 raporu) | ✅ V39'un prensipli bandit-sürümü; O6/O11'in ebeveyni; ödül-sinyaline bağlı. |
| **O6 non-stationary düzeltme** | iskontolu/kayan-UCB | **deferred, "NEXT WAVE #1", C_carry≈0** | ⚠️ GERÇEK eksik-parça (m.29 kayma-kabulü) AMA küçük-N'de çifte-bağ; kurumsal-iskonto (kapsül) zaten var. |
| **O11 meta-learning/L2O** | L2O "formül=politika" | **deferred, "ERKEN", C_carry≈0** | ⚠️ Tam-L2O fena halde erken; hafif-meta (warm-start+Brier) tek uygun form; Brier tek-ödül değil. |
| **O10 desirability + regret** | evaluator/ödül-sinyali + regret | deferred | ✅ Doğru sıra: ödül-sinyali+regret-ölçümü ÖNCE (bağlayıcı kısıt). |
| **V39 kombinasyon-dizisi** | genetik-arama + successive-halving | ham fikir | ✅ ZATEN insan-döngülü SH; ⚠️ eşikler (pilot5/parti3/%5/tavan15) tümü sezgisel (A7); küçük-N-güvenli varyant seçilmemiş. |
| **m.35 farklılaşma** | bandit gövdesi (kol/posterior/bütçe) | imzalı kanon | ✅ Bandit iskeleti kanonda; ölçüm-öncelikli (~10-görev ön-koşul). |
| **m.42(f) çeşitlilik-bütçesi** | keşif↔sömürü (azalan-ε/daralan-UCB) | imzalı kanon | ✅ "ε_n=1/n → O(log n) TEOREM" (07-18); LLM greedy-kaçışına karşı zorunlu-keşif = doğru. |
| **m.37 karar-modeli + karşıt-temel** | evaluator + keşif↔sömürü + yakınsama-durdurma | imzalı kanon | ✅ "keşif↔sömürü" karşıt-eksende açıkça; ⚠️ ama m.37 "hamleyi minimize et" der → O6/O11 ile gerilim. |
| **m.29 deneysel-damga** | kalibrasyon (veriye eğri) | imzalı kanon | ✅ Non-stationary kabulü ("eşikler zamanla kalibre"). |
| **K-020 Optuna/promptfoo/Brier** | SH + evaluator + kalibrasyon | BEKLEYEN | ✅ Küçük-N-güvenli araç; ⚠️ promptfoo evaluator-güvenilirliği (κ≈0.5) açık. |
| **V31 tahmin ajanı / Brier** | warm-start + kalibrasyon | TETİKLİ | ✅ Brier proper-scoring; ⚠️ tek-skaler değil (çözünürlük/kalibrasyon ayrışımı). |
| **V56 Kimi işçi-model** | bandit-kol (model-routing) | **ERTELENDİ (Fable-only)** | ⚠️ Model-çeşitliliği kolu bütçeyle kapalı; "ucuz≠ucuz-iş" ölçülmüş ders. |

**Özel vurgu:** O6+O11 aynı 07-18 raporunun §5 bandit-ailesinden türedi; ikisi de O5'in çocuğu (O6=non-stationary düzeltme, O11=meta-katman). Envanter, ödül-sinyali darboğazını 8 ayrı yerde işaretledi (V39 "evaluator ŞART" · A5 credit-assignment · senaryo-defteri "kalite boş/tahmini" · K-020 promptfoo · m.42f "judge düşük-temp" · K-009 G1) — bu B4'ün "bağlayıcı kısıt = sinyal" sentezinin kanon-içi teyidi.

---

## §4 — Yanlış/zayıf gördüklerim (dürüst bayraklar — KARAR ALMADAN, m.41)

1. **B4 büyük ölçüde 07-18 yakınsayan-formül raporunu yeniden-türetiyor** — O6/O11 orada zaten deferred/next-wave, doğru şerhlerle ("NEXT WAVE #1", "ERKEN"). Net-yeni küçük (FORMEL/HAFİF bölünmesi + sinyal-bağlayıcı-kısıt + Sutton/kapsül yakınsaması + küçük-N-güvenli varyant). Yeni-keşif kılığına sokmuyorum.
2. **Ödül/evaluator sinyali BAĞLAYICI kısıt (B1/B3/A5 ile yakınsak).** Güvenilir kalite-sinyali ÖNCE gelmeden kurulan her O5/O6/O11 gürültüyü optimize eder (regresyonel Goodhart). Sıra bulanıklaştırılmamalı: sinyal-ÖNCE, optimizer-SONRA.
3. **Non-stationary + küçük-N ÇİFTE bağ.** O6'yı gerekli kılan kayma, küçük-N tahmini imkânsız kılan kaymayla AYNI — "ilkece gerekli, o rejimde kullanılamaz" N büyüyene dek. Dürüst gerilim, gizlenmemeli.
4. **Sayılar JARVIS-N'de lisanssız (m.39).** Regret-sınırları O(log T), minimax T^{2/3}, "2-çeşitli≈16-homojen" asimptotik; JARVIS-garantisi gibi ithal etmek yanlış (A5/A4/B3 aynı tuzak). 07-18'in "ε_n=1/n → O(log n) TEOREM"i gerçek teorem ama N~10'daki SONLU-örneklem davranışı açık soru, asimptot değil.
5. **V39 eşikleri (pilot5/parti3/%5/tavan15) tümü deneysel/sezgisel (A7-işaretli)** — sezgisel-eşikli successive-halving küçük-N'de tam C-antitez'in "agresif eleme sağlamlığını yitirir" bölgesi; küçük-N-güvenli varyant (istatistiksel-kapı) henüz seçilmemiş.
6. **Öz-referans (maliyet notu):** B4, zaten ertelenmiş kalemler için "mevcut erteleme doğru + önce sinyali kur" sonucuna 11 çift-atlas ajanı harcadı — çift-atlas ×2 maruziyetinin bir örneği daha (A2/B1/B2/B3).
7. **L2O dürüst karşı (E-tez/B-antitez):** dağılım-İÇİ kazanç var (Metz) → "L2O değersiz" fazla güçlü; savunulabilir iddia = "JARVIS ölçeğinde erken + OOD-kırılgan". Sutton Bitter Lesson (öğrenmeyi ölçekle) ↔ "el-heuristik küçük-N'de yener" gerçek uzun-vade gerilim; ölçek/zaman ile çözülür (küçük-N-şimdi → öğrenme-sonra).

---

## §5 — V26 örneklem-denetimi

| Ajan/şerit | Denetlenen iddia | Sonuç | Etki |
|---|---|---|---|
| A-antitez | "minimax T^{2/3}≈4.6 (T~10)" | **Asimptotik** — sonlu-örneklemde açık | [K]/[?]; JARVIS-garantisi olarak sunulmadı |
| B-antitez | "VeLO ~4000 TPU-ay, genellemiyor" | **Arama-özeti** — çok-kaynak | [K]; L2O-erken argümanının çekirdeği |
| C-antitez | "evaluator κ≈0.51-0.56 öznel-çıktıda" | **Kaynaklı + B1/A5 ile yakınsak** | [K]; sinyal-bağlayıcı-kısıt teyidi |
| D-tez | "Optuna-Hyperband bir multi-fidelity bandit" | **Doğrulandı** — Optuna docs | [K]; "O6/O11 zaten OLDUĞU şey" tezinin çekirdeği |
| Envanter | "O6=NEXT WAVE #1, O11=ERKEN, C_carry≈0" | **Kanon-DOĞRULANDI** — POP + 07-18 raporu | [D-kanon]; mevcut erteleme onayı |
| E-tez | "Sutton §2.5 sabit-α = kapsül-üzerine-yazma" | **Kitap-DOĞRULANDI** + kanon-eşleme | [D]; kurumsal-iskonto yakınsaması |
| Kanon | "Garivier-Moulines kaynağı" | **Kanon-içinde 'doğrulanmadı' damgalı** | [X]; O6 sayısal parametreleri belirlenmemiş |
| Egress | arXiv · Optuna docs · distill.pub | **403** | Bulgular [K]; Sutton kitabı + kanon [D] |

---

## §6 — Cevaplanmamış sorular (karar biriktirilmedi — m.41)

1. **O6/O11'in mevcut ertelemesi (deferred, C_carry≈0, tetik=veri+held-out-galibiyet) korunsun mu?** — kanıt "evet, mevcut erteleme doğru"ya işaret ediyor; ama teyit Salih'te (POP kalemleri).
2. **ÖNCE kurulacak tek şey — güvenilir ödül/evaluator sinyali — nasıl inşa edilir?** JARVIS ucuz-proxy↔gerçek-kalite korelasyonu ölçülmemiş; ölçülene dek O5/O6/O11 gürültü-optimizasyonu riski (B1/B3/A5 aynı darboğaz). PortRisk pytest-yeşil (nesnel) ilk aday.
3. **Tetiklenince küçük-N-GÜVENLİ varyant mı** (median-pruner+startup-trials / racing-eşiği + non-stationarity için iskonto), **yoksa V39'un sezgisel-eşikli agresif SH'si mi?** — C-antitez birincisini işaret ediyor.
4. **Non-stationarity kurumsal-iskonto (kapsül-üzerine-yazma) ile YETERİNCE karşılanıyor mu, yoksa formül-düzeyi O6 gerekli mi?** — çifte-bağ (O6 küçük-N'de kullanılamaz) bunu N-büyümesine erteliyor.
5. **O11 hafif-meta (warm-start + Brier-kalibrasyon) formuna mı sınırlansın** (tam-L2O "ERKEN" kalsın), **ve Brier tek-ödül olmaktan nasıl korunur** (çözünürlük/kalibrasyon ayrışımı)?

---

*Bu rapor B4 kartının çıktısıdır (m.41 yan-oturum): 5 aile × 2 şerit + 1 envanter = 11 Atlas koşumu, çift-atlas (tez ∧ ¬tez). Karar ALINMADI, kanon DEĞİŞMEDİ; yalnız bulgu + "nedir" açıklaması + kategori/kontrol + dürüst bayraklar sunuldu. Ana bulgu: O6/O11 JARVIS'in zaten OLDUĞU bandit-iskeletinin prensipli adı; mevcut erteleme doğru; bağlayıcı kısıt algoritma değil ödül-sinyali (B1/B3/A5 ile yakınsak). Sıradaki kuyruk: B5 (Heartbeat/otomasyon maliyet deseni — "bu tam olarak nedir" tekrar-açıklamalı).*
