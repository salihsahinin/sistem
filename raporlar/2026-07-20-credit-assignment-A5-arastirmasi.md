# A5 — Credit-Assignment (Kalite Atfı) — Atlas Raporu (2026-07-20)

> **Mod:** yan-oturum (m.41 · CC = yan oturum, kanon KİLİTLENMEDİ, karar ALINMADI) · şerit: çift-atlas (tez ∧ ¬tez) · aile sayısı: **5** (RL · oyun-teorisi/deney · process-supervision · ünlü-isimler · küçük-N) → 10 literatür şeridi + 1 karar-envanteri.
> **Kanıt kısıtı (dürüstlük — ÖNEMLİ):** Bu koşumda proxy egress politikası neredeyse **tüm akademik birincil kaynakları 403'ledi** — arxiv, openai.com, NIST, statmodeling(Gelman), .edu PDF'leri, hatta Wikipedia ve github web sayfaları. WebFetch ile birinci-elden açılabilen çok az kaynak oldu (github API'den PRM800K [D] gibi). Dolayısıyla bulguların **çoğunluğu WebSearch-özeti düzeyinde [K]**, birincil-metin doğrulaması YAPILAMADI. Bu, uydurma değil erişim engelidir; her şerit bunu açıkça bayrakladı. Güven: kavramsal iskelet YÜKSEK (çok-kaynak örtüşmesi), tekil rakamlar ORTA.
> **Okuma sırası (Fable):** §0 Carvis sentezi + §4 dürüst bayraklar → yeterli. Detay: §1 aile bulguları · §2 ünlü isimler · §3 kararların kategori+kontrolü · §5 V26 · §6 açık sorular.

---

## §0 — Carvis sentezi (önce oku)

**Soru (A5):** JARVIS'in karar-modeli (m.37/V39) her karar-noktası için 4'lü tutmak istiyor: (model, token, zaman, **KALİTE**). Token+zaman anında ölçülür; KALİTE proje düzeyinde bir evaluator'la ölçülür ama tek tek karar-noktalarına **dağıtılması** gerekir = **credit-assignment**. Bu, m.37/V39'un adı-konmuş açık bilinmeyeni (senaryo-defteri ŞERH 4: "kalite kolonu credit-assignment olgunlaşana dek boş/tahmini").

**Kesişim (tez∧antitez'in ORTAK dediği — en sağlam katman):**

1. **Formel kredi-atama yöntemleri iki counterfactual kalıba iner:** (a) *"bu karar/adım/ajan OLMASAYDI sonuç ne olurdu"* (Shapley, COMA, Pearl-PN, influence functions, ablation, OFAT) ∨ (b) *"krediyi zaman/adım boyunca geriye DAĞIT"* (TD/eligibility traces, RUDDER, process-supervision). İkisi de JARVIS'in "kaliteyi karar-noktalarına dağıt" cümlesinin doğrudan akrabası. [D-yapısal]

2. **Yöntemler KAVRAMSAL olarak JARVIS'e birebir oturuyor ama MEKANİZMALARI oturmuyor.** RL yöntemleri (A1) üç sütuna dayanır: gradyan · tekrarlı-episode/öğrenilen-critic · büyük-N varyans-indirimi. JARVIS dördünü de ihlal eder (gradyansız · tek-seferlik · küçük-N · non-stationary). ⇒ **Kavramları al, algoritmaları alma; gradyanlı critic/LSTM yerine LLM-tahmini + insan-yargısı koy.** (K-016 "kurulum değil ilham" kuralının birebir teyidi.)

3. **Her şey TEKRARLI KOŞUM'a bağlı.** Shapley/faktöriyel/ablation'ın hepsi çok-sayıda *karşı-olgusal yeniden-koşum* ister. Saf tek-seferlikte per-karar *sayısal* kredi **tanımsız** (Holland "fundamental problem of causal inference": tek realizasyonda bireysel nedensel etki gözlenemez). **AMA V39'un loop-rerun tasarımı (aynı projeyi farklı seçim-dizileriyle yeniden-inşa) tam da bu etkinleştirici koşuldur** — JARVIS'in kendi tasarımı kapıyı açıyor. Küçük-N burada ENGEL değil AVANTAJ: n=5-15'te tam Shapley (2^n) hesaplanabilir; büyük-veri MC-yaklaşımları gereksiz.

4. **Sahadaki ünlü pratisyenler ince per-karar krediden KAÇINIR.** Karpathy, Ng, Chip Huyen, Eugene Yan, Hamel Husain, Jeremy Howard — hepsi (i) tek-sayılı uçtan-uca *sonuç* metriği + (ii) "birer birer değiştir" kaba OFAT-ablation + (iii) başarısızlıklara ELLE bak ("look at your data") üçlüsünde birleşiyor. **Hiçbiri karar-dizisine formel nicel kredi dağıtmıyor.** (Kanıt dolaylı: açık ret değil, yöntem-yokluğu.)

5. **Gerçekten küçük-N/tek-seferlik için tasarlanmış NİTEL/Bayesçi bir aile VAR** (A5-tez): partial-pooling (iş-sınıfları arası güç ödünç al), Bayesçi süreç-izleme (tek-vaka içi kanıt: hoop/smoking-gun testleri), **QCA** (çıktısı doğrudan `X∧Y→Z` Boole kuralı), AHP (insan-yargısını yapısal ağırlığa çevir), Shapley (küçük-N'de fizibil). Bunlar *sayısal kesinlik taklidi yapmadan* atıf üretir.

**JARVIS'e ne demek (gözlem, KARAR DEĞİL — m.41):**
- **JARVIS'in kendi duruşu birden çok cepheden doğrulandı:** "kalite kolonunu olgunlaşana dek boş/tahmini bırak" (ŞERH 4) = A5-antitez + pratisyen konsensüsünün tam söylediği (yok olan sayısal kesinliği imal etme). Bu, m.7 "çıplak veri" ilkesiyle de örtüşür.
- **JARVIS'in mevcut yapıları hazır iskele:** V39 loop-rerun = etkinleştirici koşul · V28 iş-sınıfları / V37 kategorileri = partial-pooling'in "grupları" · `X∧Y→Z` transfer hedefi = QCA'nın birebir çıktı formatı · "yargıç ayrı rol" ihtiyacı = m.7/V8/V53 hattı.
- **Olgun yol (literatürün önerdiği, JARVIS'e eşlenmiş — sadece bir harita, öneri değil):** (a) şimdi → kaba OFAT tek-nokta-değişimi (zaten V39) + **AYRI-rollü** LLM-as-judge ile *nitel* per-karar kredi; (b) V28/V37 sınıflarından partial-pooling ile güç ödünç al; (c) V39 loop-rerun'ları biriktikçe Shapley/fractional-factorial *sayısal* krediye açılır; (d) QCA-tipi `X∧Y→Z` Boole kuralına damıt (transfer hedefi).

---

## §1 — Aile başına bulgular (çift-atlas)

### Aile 1 — RL / temporal credit assignment
- **Tez:** Yöntemler olgun ve kavramsal olarak birebir: return-decomposition (RUDDER), counterfactual baseline (COMA), advantage-vs-taban (GAE), attention-atıf. MC-uniform atıf = JARVIS'in naif varsayılanı (eşit kredi). "advantage = o karar-tipi için beklenen/ortalama kaliteye göre sapma" tek-seferlikte bile uygulanabilir (taban = geçmiş ortalama). [K]
- **Antitez (¬):** Üç sütun (gradyan · tekrarlı-episode/critic · büyük-N) JARVIS'te çöker; non-stationary "aynı durum tekrar gelmez"; uzun-ufuk+seyrek-ödülde atıf üstel-zor, hâlâ açık araştırma. **Çarpıcı:** RL bile "başarısız dizide tek tek doğru olan adımı koruma"yı garanti edemiyor (dizi çökünce tüm adımlar negatif advantage). [K/D]
- **Kesişim:** Kavram transfer edilir, mekanizma edilmez; gradyanlı critic/LSTM → LLM-tahmini. En temiz kavramsal cevap = COMA counterfactual ("bu adımda varsayılanı seçseydik sonuç?"), LLM ile gradyansız üretilebilir.

### Aile 2 — Oyun-teorisi / deney-tasarımı (Shapley, faktöriyel, ablation)
- **Tez:** Shapley'nin *efficiency* aksiyomu = "kaliteyi karar-noktalarına artıksız dağıt"ın birebir matematiği (efficiency+symmetry+dummy+additivity → benzersiz). Küçük-N Shapley için AVANTAJ (2^n fizibil). Fractional factorial (Res III/IV) = az-koşum bütçesinin hazır cevabı (~15 karar → ~16 koşum, bedel: etkileşimler aliased). Data Shapley (Ghorbani-Zou) doğrudan emsal. [D-venue/K]
- **Antitez (¬):** Shapley #P-hard + MC binlerce örnek; tam faktöriyel 2^k patlar; etkileşim tahmini 4-16× örneklem; <10 gözlem/parametre → tanımsız; OFAT etkileşim-körü; çatallanan-yollar + confounding küçük-N'de sahte kredi. Hepsi **çoklu karşı-olgusal koşum** ister. [D-nicel]
- **Kesişim:** Yöntemler titiz ve küçük-N'de hesaplanabilir; **bağlayıcı kısıt hesap değil, tekrarlı koşum ihtiyacı.** Tekrar varsa (V39 loop) → fizibil; saf tek-seferlikte tanımsız.

### Aile 3 — Process supervision / PRM (LLM-native)
- **Tez:** PRM vs ORM = A5'in iskeleti. ORM tek skaler (atıf çözünürlüğü=1); PRM her adıma skor = aradığımız per-karar kredi. Math-Shepherd = insan-etiketsiz MC-atıf (karar-sonrası yörünge iyi-sonuca varma oranı). LLM-as-judge = pratik gövde (>%80 insan-uyumu). [D/K]
- **Antitez (¬):** JARVIS'in yaşadığı yerde (açık-uçlu, altın-cevapsız, öznel) EN güvenilmez. **DeepSeek-R1 process'i DENEDİ+TERK ETTİ** (reward-hacking), en kolay alanda bile → outcome-only'ye döndü. PRM800K = **800.000 insan etiketi [D-doğrulandı]** (fahiş). LLM-judge coin-flip (κ≈0.51, kararlı verdikt 11-15 tekrar), pozisyon/uzunluk/**kendini-kayırma (+%10-25)** yanlılıkları, zayıf adım↔sonuç nedenselliği (Claude 3.7 gerçek gerekçeyi %25 dile getiriyor), Goodhart/step-inflation. [D-PRM800K / K-diğer]
- **Kesişim:** En yakın LLM-native analog AMA en zayıf rejimde; kullanılırsa **yargıç AYRI rol** olmalı (kendini-kayırma; m.7). Nedensellik zayıf → adım-metnini puanlamak kararın gerçek nedenselliğini puanlamak değildir.

### Aile 4 — Ünlü isimler (pratisyenler)
- **Tez:** Alanın ünlüleri kredi-atamayı FORMEL yapıyor: Sutton (TD/eligibility traces + Bitter Lesson), Hochreiter (RUDDER return-decomposition), OpenAI/Lightman (process supervision), Foerster (COMA counterfactual), Zou (Data Shapley), Pearl (probabilities of causation PN/PS), Anthropic/Grosse (influence functions). İki kalıp: counterfactual katkı + geriye-dağıtım. [D-Aile4tez / K]
- **Antitez (¬):** Sahada ÜRETEN pratisyenler ince per-karar krediden KAÇINIR: **Karpathy** ("kahraman olma, ResNet-50 kopyala" · "teker teker karmaşıklaştır" · eval vibe-check'in yerine · doğrulama yeni darboğaz), **Ng** (tek-sayılı metrik + error analysis + ablative analysis), **Hamel Husain / Eugene Yan / Chip Huyen** (uçtan-uca eval + "look at your data" + örnek-etiketle), **Howard** (güçlü baseline + küçük-başla). [D-erişilebilir mirror / K]
- **Kesişim (KRİTİK):** Akademi formel yöntemleri ÜRETİR; ürün-sahibi pratisyenler onları KULLANMAZ — uçtan-uca metrik + kaba ablation + veriye-bakma yeter. JARVIS'in ölçeğinde **pratisyen tarafı daha bağlayıcı** (formel-kredi tavşan deliğine girme; ölç + kaba ablation + bak).

### Aile 5 — Küçük-N / tek-seferlik / offline
- **Tez:** JARVIS'in tam kısıtına tasarlanmış olgun aile VAR: Bayesçi posterior (önselle az-veride kör kalmazsın), **partial-pooling** (V28/V37 sınıflarından güç ödünç al), Pearl "but-for" (tek-vaka, istatistik gerekmez), **Bayesçi süreç-izleme** (tek-vaka içi kanıt: straw/hoop/smoking-gun/doubly-decisive), **QCA** (küçük-N Boole nedenselliği → çıktı doğrudan `X∧Y→Z`), Shapley, OPE, AHP (insan-yargısı → yapısal ağırlık). [K]
- **Antitez (¬):** N<15 tek-seferlikte güvenilir *sayısal* per-karar kredi ELDE EDİLEMEZ: Holland tek-realizasyon + güç yetersizliği/geniş güven aralığı + confounding + overfit. En fazlası kaba OFAT + [tahmin]-etiketli nitel gerekçe — ki bu JARVIS'in "kolonu boş/tahmini bırak"ını doğrular. Toplu (ATE) çalışır ama N+tekrar ister (JARVIS'te ikisi de yok). [K]
- **Kesişim:** *Sayısal* kredi imkânsız (antitez haklı); *nitel/Bayesçi* kredi MÜMKÜN (tez haklı) — partial-pooling + süreç-izleme + QCA + AHP, sayısal kesinlik taklidi yapmadan. Çelişki değil, çözünürlük ayrımı: sayısal HAYIR, nitel/ordinal/Boole EVET.

---

## §2 — Ünlü isimler haritası (iki kamp)

| İsim | Yöntem | Kamp | Kaynak (çoğu 403; mirror/snippet) |
|---|---|---|---|
| Richard Sutton | TD-learning + eligibility traces; "Bitter Lesson" | FORMEL (geriye-dağıtım) | Sutton 1988; incompleteideas.net/BitterLesson |
| Sepp Hochreiter | RUDDER return-decomposition (regresyona çevir) | FORMEL (geriye-dağıtım) | arXiv:1806.07857 |
| OpenAI (Lightman ea.) | Process supervision / PRM (adım-düzeyi ödül) | FORMEL (geriye-dağıtım) | arXiv:2305.20050; PRM800K [D] |
| Foerster (COMA) | Counterfactual baseline (bireysel katkı izole) | FORMEL (counterfactual) | arXiv:1705.08926 |
| James Zou | Data Shapley (marjinal katkı, aksiyomatik) | FORMEL (counterfactual) | Ghorbani & Zou, ICML 2019 |
| Judea Pearl | Probabilities of causation (PN/PS, but-for) | FORMEL (counterfactual) | UCLA R260 |
| Anthropic (Grosse ea.) | Influence functions (yeniden-eğitmeden atıf) | FORMEL (counterfactual) | arXiv:2308.03296 |
| **Andrej Karpathy** | Eval-driven; "kahraman olma"; teker-teker; vibe→eval | **KAÇINAN** (uçtan-uca+ablation) | karpathy.github.io/recipe (mirror) |
| Andrew Ng | Tek-sayılı metrik + error analysis + ablative | **KAÇINAN** | ML Yearning |
| Hamel Husain | "Look at your data"; hata-taksonomisi | **KAÇINAN** | hamel.dev/evals-faq |
| Eugene Yan | "Look at The Data™"; süreç>judge; örnek-etiketle | **KAÇINAN** | eugeneyan.com/eval-process |
| Chip Huyen | Evaluation-Driven Dev; manuel inceleme en yüksek ROI | **KAÇINAN** | huyenchip.com |
| Jeremy Howard | Güçlü baseline + "her ML satırı yanlış varsay" | **KAÇINAN** | course.fast.ai |

**Ders (Karpathy dahil):** Kredi-atama literatürünü *yazan* isimler (RL/nedensellik/veri-değerleme) ile ürün *çıkaran* isimler (LLM-eng) iki ayrı kamp. JARVIS bir ürün-sistemi olduğundan pratisyen-kamp daha bağlayıcı; formel-kamp yalnız V39 loop-rerun verisi biriktiğinde devreye girer.

---

## §3 — Kararlarımızın credit-assignment merceğiyle KATEGORİ + KONTROL

Karar-envanteri (senaryo-defteri 20 kayıt D1-D20 + tüzük m.1-m.43) bu mercekle 4 kategoriye ayrılıyor. Mercek sorusu: *"bu kararın kalitesini bir sonuca atfedebilir miyiz?"*

**Kategori A — Ölçülebilir-sonuçlu + KOŞUMLA doğrulanmış (kredi-atfedilebilir):**
- **D11** (V39 dar koşum): $7,16 · 19,5 dk · 12/12 satır · örneklem D2/K1/X0 — /usage'dan GERÇEK, ilk tam maliyet-çifti + kalite gözlemi. **Kredi-atfının tek olgun örneği.**
- **D4** (K-017): 70 bulgu 58/12/0, ~2,4M token · ~8,5 dk · 78 ajan — koşum-gerçeği.
- **D19** (çelişki-kapısı): süreç fiilen koştu (kalem 1-6 karşılaştırıldı).

**Kategori B — Ölçülebilir-sonuçlu ama hâlâ HİPOTEZ (kredi-bekliyor):** D1, D5, D9, D12, D13, D14, D15, D17, D20 — evaluator tanımlı, koşum yok. Bunların kredisi V23 kuralınca "doğrulandı" sayılamaz.

**Kategori C — Ölçülemez-sonuçlu (tasarım gereği kredi-atfı DIŞI):** D3, D6, D16, D18 + tüzük yönetişim maddelerinin çoğu (m.1-8, m.14-28, m.32-34, m.41). Bunlar değer/yön kararları (m.31 Katman-1); "sonuç-kalitesi atfı" onlara uygulanmaz — kategori hatası olur. (Bu SAĞLIKLI: her karar credit-assignable değildir.)

**Kategori D — Sayı/eşik içeren ama TÜRETİLMEMİŞ (m.39/A7 risk-bölgesi):** D1 (5/3/%5/15), D5 (Brier 0.80/0.65/0.60), D7 (400-700K…, kalite 6/8/8,5), D8 (15-30K…), D10 (8×, TTL 1sa), D13 (5-10K/gece), D14 (×2/×1,6, "16'dan 3"), D15 (N=3), D20 (WER %25, ≥10) + tüzük m.12 (6 ay), m.19 (≤30 dk), m.31 (N=5), m.36 (~3 ay), m.42(e) (RİSK formülü), m.43 (N=3). Hepsi deneysel-damgalı, kalibre-bekliyor.

**Mercek bulgusu:** Envanterin kendisi credit-assignment problemini literatürün öngördüğü gibi yaşıyor — **maliyet-çifti (token↔zaman) D11'e kadar hiçbir blokta tam değil** (D7 token boş, D8 token+süre boş: bulut-Routine'de yapısal boş); **kalite kolonu TÜM bloklarda "[türetilmiş]" damgalı.** Yani "token+zaman anında ölçülür, kalite zor" varsayımı bile pratikte kırılmış: maliyet çifti de çoğu blokta eksik kalmış (ölçüm-tetiği unutulduğunda). Credit-assignment'ın ÖN-KOŞULU (tam maliyet gözlemi) henüz yalnız D11'de sağlanmış.

---

## §4 — Yanlış / zayıf gördüklerim (dürüst bayraklar — KARAR ALMADIM, DEĞİŞTİRMEDİM)

Salih'in talebi gereği: yalnız işaret ediyorum, karar/değişiklik yok.

1. **"kalite 1-10 skalası" (A7 sezgisel-aday) kategori-hatası riski taşıyor.** Literatür (A5-antitez + pratisyenler) diyor ki N<15 tek-seferlikte 1-10'luk *ince sayısal* per-karar skalası kalibre edilemez → gürültüyü sinyal sanma (overfit). Bu rejimde dürüst çözünürlük **nitel** (süreç-izleme: hoop/smoking-gun) veya **ordinal/Boole** (QCA), 1-10 değil. Bayrak: 1-10 skalası verinin taşıyabileceğinden ince olabilir. *(Gözlem; A7/credit-metrik tasarımına girdi — karar değil.)*

2. **Kalite kolonunun "olgunlaşana dek boş" varsayımı, TEKRARLI KOŞUM olmadan asla tetiklenmeyebilir.** A5 tez+antitez ikisi de: sayısal kredi *tekrarlı karşı-olgusal koşum* ister. JARVIS'in tek tekrar-kaynağı V39 loop-rerun'ları — ve onlar tetikli (K-009/K-010). Bayrak: kalite kolonu "olgunlaşma" değil, **loop-rerun'lar fiilen koşana dek TANIMSIZLIK** meselesi. Loop-rerun gelmezse kolon "henüz olgun değil" değil, "ilkesel olarak doldurulamaz" kalır. *(Dürüst ayrım.)*

3. **Karar-modeli (m.37) "kim karar verir" ile "kim kaliteyi puanlar"ı yapısal AYIRMIYOR.** LLM kendini-kayırma bulgusu (+%10-25 kendi çıktısına) diyor ki kaliteyi puanlayan, kararı verenden AYRI rol/ajan/model olmalı. m.37'ye bir kalite-puanlama adımı eklenirse, Carvis kendi kararını puanlarsa yanlılık krediye sızar. Bayrak: kalite-atfı adımı eklenecekse ayrı-yargıç şartı gerekir (m.7/V8/V53 hattı bunu destekler ama m.37 metni henüz zorlamıyor). *(Gözlem.)*

4. **V39 transfer hipotezi (`X∧Y→Z`) sağlam ve HAZIR bir üretim yöntemi var (QCA) — ama bağlı olduğu "kalite atfı" YÖNTEMİ adlandırılmamış.** JARVIS "credit-assignment olgunlaşınca" diyor ama HANGİ yöntemle olgunlaşacağını boş bırakıyor. Literatür somut bir aile veriyor (partial-pooling + süreç-izleme → QCA). Bayrak: yöntem adlandırılmazsa transfer hipotezi test-edilebilir bir kredi mekanizmasına hiç kavuşmayabilir. *(Fırsat-bayrağı, hata değil.)*

5. **Maliyet-çifti ölçümü kredi'nin ÜST-AKIŞI ve henüz güvenilmez (D7/D8).** Kaliteyi maliyete oranla atfetmek istiyorsan önce maliyeti tam ölçmelisin; D7 (token boş), D8 (token+süre boş) gösteriyor ki maliyet çifti çoğu blokta yapısal/unutkanlıkla eksik. JARVIS bunu zaten işaretlemiş (D8 "maliyet-gözlem mekanizması K-009 tasarım girdisi"). Bayrak: credit-assignment tartışmasından ÖNCE, tam-maliyet-gözlemini standart tetiğe bağlamak gelir (ilk-önce ölçülebilir olan). *(Gözlem; D11 bunu /usage-emriyle çözmüş — o desen standartlaşmalı görünüyor.)*

6. **"Küçük-veri itirazı düştü" (V39 ŞERH 2) kısmen fazla-iyimser.** V39, loop-rerun'ların küçük-N'i çözdüğünü varsayıyor. Doğru — AMA A2/A5 antitez şunu ekliyor: loop-rerun'lar *aynı* projeyi yeniden koşsa bile, projeler-ARASI transfer için karar-noktası HİZALAMASI (V28 sınıfları/V37 kategorileri) gerekir ve non-stationary "aynı durum tekrar gelmez" riski sürer. Bayrak: loop-rerun'lar *bir proje içi* krediyi çözer; *projeler-arası* transferi otomatik çözmez — hizalama ayrı bir açık iş. *(Nüans; V39 ŞERH 5/6 bunu kısmen görmüş ama "düştü" ifadesi bunu gölgeliyor.)*

**Genel not:** JARVIS'in çekirdek sezgisi (kalite zor, boş/tahmini bırak, m.39 damga) literatürce GÜÇLÜ biçimde doğru. Bayraklar "yanlış yapıyorsunuz" değil, "şu noktada fazla-iyimserlik / adlandırılmamış yöntem / kategori-inceliği var" uyarılarıdır.

---

## §5 — V26 örneklem-denetimi

| Şerit | Denetlenen iddia | Sonuç | Etki |
|---|---|---|---|
| Aile3 (both) | PRM800K = ~800K adım-düzeyi insan etiketi (MATH) | **[D] DOĞRULANDI** (github.com/openai/prm800k: "800,000 step-level correctness labels... MATH") | Antitezin "fahiş etiket" ayağı sağlam |
| Aile4-antitez | Karpathy recipe: "don't be a hero" / teker-teker | **[K] erişim-engeli** (Cornell PDF mirror 403) | Çürütülmedi; 3 mirror'da çapraz, ama birinci-el YOK |
| Aile5-tez | Process-tracing = tek-vaka Bayesçi (hoop/smoking-gun) | **[K] erişim-engeli** (Wikipedia 403!) | Çürütülmedi; çok-kaynak snippet |
| Metadata | Tüm akademik primary erişimi | **SİSTEMATİK 403** (arxiv/openai/NIST/.edu/Wikipedia) | Raporun baş kısıtı; bulguların çoğu [K] |

**Sonuç:** Denetlenebilen 1 iddia birincil kaynaktan doğrulandı (PRM800K [D]); 2'si erişim-engelli (çürütülmedi). **Baskın epistemik kısıt = egress-403:** bu koşum büyük ölçüde WebSearch-snippet üzerine kurulu. Kavramsal iskelet çok-kaynak örtüşmesiyle güvenilir; tekil rakamlar (κ≈0.51, %78, +%10-25) teyide muhtaç [K]. Karar alınacaksa birincil-kaynak teyidi borç olarak kalır.

---

## §6 — Cevaplanmamış sorular (karar biriktirilmedi — m.41)

1. **Kalite-atfı YÖNTEMİ ne olacak?** Literatür bir aile öneriyor (partial-pooling + süreç-izleme + QCA + ayrı-yargıç LLM-judge); ama seçim m.37/A7 kapsamında Salih+ana-sıra kararı (Katman-1 kanon dokunuşu). Bu rapor yalnız haritayı sunar.
2. **Kalite çözünürlüğü sayısal mı, ordinal/Boole mu?** 1-10 skala mı (mevcut A7 adayı) yoksa nitel/QCA-Boole mu — verinin taşıyabileceği çözünürlük açık soru (§4-1).
3. **V39 loop-rerun'lar ne zaman koşacak?** Kredi kolonunun tanımlılığı buna bağlı (§4-2); K-009/K-010 tetikli.
4. **Ayrı-yargıç rolü m.37'ye girecek mi?** Kendini-kayırma bulgusu bunu gerektiriyor ama kanon dokunuşu (§4-3).
5. **Birincil-kaynak teyit borcu:** egress-403 nedeniyle κ/yüzde rakamları [K]; benimseme/tasarım gündeme gelirse arxiv/OpenAI birincil teyidi gerekir.

---

*Koşum: atlas-kosum (m.40b) · 5 aile × 2 şerit = 10 bağımsız Atlas ajanı + 1 karar-envanteri (Explore) + Carvis V26 denetimi. NOT: ilk koşumda 6 şerit ~8 saat container-suspend'de dondu; taze yeniden koşuldu (07-20). Ham şerit çıktıları bu oturumun task-transcript'lerinde; bulgular yukarıda etiket+URL ile gömülü. Egress-403 baş kısıt.*
