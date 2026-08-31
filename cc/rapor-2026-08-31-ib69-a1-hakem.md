# İB-69 aile-1 — MASKELİ HAKEM (m.40b v0.2)

AS-OF: 2026-08-31 · Hakem: İB-69 aile-1 · Dil: TÜRKÇE
**Maske kuralı uygulandı:** hiçbir iddia "tez dedi / antitez dedi" diye kabul ya da red edilmedi. Hüküm yalnız (i) bu oturumda AÇILDIĞI beyan edilen birincil kaynak, (ii) repo dosya:satır kanıtı, (iii) formal zorunluluk üzerinden verildi. Hakem kendi WebFetch'i yapmadı; dış-kaynak iddialarında dayanak = tez raporunun kendi "açıldı mı" beyanı + V26 bağımsız denetimi (`cc/rapor-2026-08-31-ib69-a1-v26-ornekleme.md`). Bu yüzden dış-kaynak D'leri "raporun açıldı beyanı ∧ V26 çelişkisi yok" tabanlıdır ve bu sınır burada AÇIKÇA beyan edilir.
**Kapsam sınırı:** K-020 kararı VERİLMEDİ; bu belge yalnız şema girdisidir. Prototip inşa/koşum yok, repo değişikliği yok (bu dosya hariç), git yok.

## 1. Hüküm tablosu (26 iddia)

| # | İddia (tek cümle) | Şema alanı | Dayanak | D/K/X | Gerekçe |
|---|---|---|---|---|---|
| 1 | Tam faktöriyel koşu sayısı = eksen seviye kardinalitelerinin çarpımı (\|A\|×\|B\|). | eksen · maliyet | help.reliasoft.com/.../general_full_factorial_designs.html (WebFetch EVET beyanlı), birebir "Runs = (Levels of A)×(Levels of B)" | **D** | Açılmış birincil kaynak + formal olarak zaten trivial-doğru; V26 bu rapor için ihlal bulmadı. |
| 2 | Tekrar (replicate) toplam maliyete çarpan olarak girer: toplam = \|A\|×\|B\|×r. | maliyet | aynı URL, 3 hız × 2 katkı × 3 tekrar = 18 koşu örneği | **D** | Sayısal örnek kaynakta birebir; çarpan yapısı formal zorunlu. |
| 3 | promptfoo matrisi `prompts × providers × tests` üçlü çarpımıdır; her kombinasyon çalıştırılır. | eksen | promptfoo.dev/docs/configuration/guide/ (açıldı), birebir alıntı + YAML örneği | **D** | Deklaratif eksen tanımının çalışan emsali; alıntı doğrudan. |
| 4 | promptfoo hücre çıktısının kütük şeması (alan adları: `success`, `score`, `latencyMs` vb.) bilinmektedir. | kütük | Yok — raporun kendisi "WebFetch bu düzeyde ayrıntı döndürmedi [?]" diyor | **X** | Kaynak açılmış ama alan adları DOĞRULANMAMIŞ; şemaya girdi olarak kullanılamaz. promptfoo'yu kütük şeması emsali diye almak dayanaksız. |
| 5 | Optuna GridSampler tam-faktöriyeli tüketir; dağıtık koşumda aynı kombinasyon iki işçiye önerilebilir, fiili deneme sayısı grid'i AŞABİLİR. | eksen · kütük | optuna.readthedocs.io/.../GridSampler.html; V26 #2 bağımsız açıp birebir doğruladı | **D** | Bağımsız denetimden geçmiş tek-tek eşleşen alıntı. Şemaya doğrudan sonuç: hücre anahtarı olmadan idempotency yok. |
| 6 | Optuna SuccessiveHalvingPruner erken-durdurma sinyali için `trial.report(intermediate_value, step)` ARA-DEĞER'i şart koşar; η=4 varsayılan, yalnız en iyi 1/η rungya yükselir. | maliyet | optuna.readthedocs.io/.../SuccessiveHalvingPruner.html; V26 #3 birebir doğruladı (4 parametre + mekanizma) | **D** | Bağımsız denetimli. (B) hükmünün taşıyıcı kanıtı: ara-değer SH'nin ön-koşuludur, süsü değil. |
| 7 | Successive halving "her turda en kötü yarıyı eler" tanımı DESTEKLİ'dir. | maliyet | Yok — kaynak medium.com/@vireshj, tam URL bile verilmemiş, WebFetch açılmamış | **X** | V26 #1 bunu tek İHLAL olarak damgaladı; damga-metin çelişkisi rapor içinde açık. Tanım muhtemelen doğru ama ŞEMAYA dayanak olamaz. |
| 8 | Hyperband adaptif kaynak tahsisi + erken-durdurmayla mertebe-düzeyi hızlanma sağlar. | maliyet | arxiv.org/abs/1603.06560 (açıldı; V26 dolaylı, antitez de sağlam saydı) | **K** | Alıntı özet düzeyinde doğru, AMA ölçüm ML-hiperparametre rejiminde; LLM tek-atış eval matrisine taşınabilirliği hiçbir kaynakta sınanmadı. Aşırı-genelleme riski → koşullu. |
| 9 | W&B Sweeps eksen tanımını deklaratif YAML'de tutar (`method` grid/random/bayes, `parameters` value/values/distribution, `metric`, `early_terminate`). | eksen tanımı | docs.wandb.ai/guides/sweeps/define-sweep-configuration/ (açıldı, birebir alıntılar) | **D** | Üç bağımsız aracın (promptfoo, W&B, lm-eval) ortak deseni; formal olarak da eksen-manifestini koşum script'inden ayırmayı zorunlu kılıyor. |
| 10 | Per-hücre ham kayıt (`--log_samples`, `--output_path`) toplamadan AYRI bir adım olarak tutulur. | kütük · toplama | github.com/EleutherAI/lm-evaluation-harness (açıldı); V26 #4 birebir doğruladı | **D** | Bağımsız denetimli; Jarvis bronz→gold katman ayrımıyla birebir örtüşüyor. |
| 11 | Hücreye iş-anlamlı sabit kimlik verilmesi (Temporal `workflowId`) idempotency mekanizmasıdır. | kütük | docs.temporal.io/develop/typescript/child-workflows (açıldı) | **D** | Açılmış kaynak + #5 (Optuna duplicate-trial) ile aynı sonuca yakınsıyor: iki bağımsız emsal aynı alanı zorunlu kılıyor. |
| 12 | İB-07 kütük satırı 8 alanlıdır: `kosum_id, ts, sorgu_id, tekrar, altin_etiket, secilen_skill, isabet, isci_model`. | kütük | `veri/description-eval.jsonl:1` (hakem doğrudan okudu) | **D** | Dosya:satır kanıtı; hakem bağımsız teyit etti. |
| 13 | İB-49 d2-eval toplaması LLM'siz deterministiktir. | toplama | `tools/d2-eval.py:1-4` docstring + alan listeleri `:110-113`, `:130-132` | **D** | Repo kanıtı; harness stdlib+`d2` ikilisiyle kıyaslıyor, çağrı yapmıyor. |
| 14 | "Toplama LLM'siz deterministik olabilir" (Karar 65) — matris hücresi için genel olarak. | toplama | İki iç emsalin ikisi de girdiyi tiplendirmiş (#12 `secilen_skill` kapalı küme; #13 dosya+derleme kodu) | **K** | Doğru AMA gizli ön-koşullu: hücre sözleşmesi çıktıyı kapalı-küme etikete ∨ sayıya zorluyorsa geçerli. Serbest-metin hücre için LLM'siz toplama emsali YOK. |
| 15 | Önerilen ortak şema (`kosum_id, ts, git_head, eksen_degerleri, tekrar, sonuc, model, toplama_yontemi, kosum_durumu`) resume'u çözer. | kütük | Formal: şemada TEKİL ANAHTAR alanı yok; `eksen_degerleri` obje, anahtar olarak işaretsiz | **X** | İç çelişki: aynı raporun §4'ü "planlanan küme − mevcut = eksik" sorgusunu şart koşuyor, §3 tablosu bu sorguyu mümkün kılan alanı koymuyor. Reçete kendi teşhisini karşılamıyor. |
| 16 | Şemaya ayrı bir `model_surumu` alanı EKLENMELİ, çünkü mevcut `model` sürüm taşımıyor. | kütük | Karşı-kanıt: `veri/description-eval.jsonl:1` → `"isci_model": "claude-haiku-4-5-20251001"` (tam snapshot id) | **K** | İhtiyaç gerçek (m.6 anakronizm), ama teşhis yanlış: emsal ZATEN sürümlü id yazıyor. Doğru onarım yeni alan değil, alanın SÖZLEŞMESİ: "model = tam API snapshot id, kısa ad YASAK". |
| 17 | ~300k token tabanı gnhf/işçi koşumu birimi içindir, genel hücre birimi değildir. | maliyet | `raporlar/2026-08-31-ib66-...md:132` birebir: "Aşağıdaki tahminler bu tabana göredir ve **işçi/gnhf koşumları içindir**" | **D** | Kaynağın kendi kapsam beyanı; tartışmaya kapalı. |
| 18 | Matris hücresi tek Agent/prompt çağrısıyken T=300k kullanmak kategori hatasıdır. | maliyet | #17 + İB-66:187 (L1 = gnhf iterasyonu, `--stop-when` yüklemli çok-turlu CLI) + #3 (promptfoo hücresi tek istek/yanıt) | **D** | Formal olarak zorunlu: taban L1 için ölçülmüş, hücre L2-altı bir birim. Tabanı taşımak ölçüm kapsamını ihlal eder. |
| 19 | İB-07'nin 45 hücrelik gerçek koşumunun hücre-başı token/süre maliyeti ÖLÇÜLDÜ. | maliyet | Karşı-kanıt: `raporlar/2026-08-30-ib07-description-eval.md:48-53` yalnız ÇAĞRI sayısı veriyor (51 işçi denemesi, ~65 kendi çağrısı); token ∨ süre rakamı YOK | **X** | **T_hücre ÖLÇÜLMEDİ.** Şemaya sayısal taban repo'dan çıkarılamaz; ölçüm borcu olarak yazılmalı. |
| 20 | İB-07 matrisi "14 dış-tur × 60 iç-koşum = 840 hücre"dir. | eksen-eşleme · maliyet | Karşı-kanıt: `…ib07-description-eval.md:7` durma koşulu "kütükte 60 satır"; `veri/description-eval.jsonl` 45 satır, `altin_etiket` bir ALAN (14 skill = etiket uzayı, koşum ekseni değil) | **X** | Gerçek matris 20 sorgu × 3 tekrar = 60 hücre. Hem tez (eksen-eşleme §4) hem antitez (840 hücre → 252M token) aynı hatayı yapıyor; antitez'in aritmetiği çürük, sonucu (#18) başka dayanakla ayakta. |
| 21 | Ajan-freni sayacı OTURUM-genelinde kümülatiftir; eksen sırası bu kesintiyi önleyemezdi. | eksen-eşleme · maliyet | `.claude/hooks/pretool-ajan-fren.sh:36-37` (`st["sayac"] += 1`, oturum durum dosyası) + `:52` mesajı "bu oturumda %d. Agent çağrısı" | **D** | Tez bunu `[?]` bırakmıştı; hakem hook'u okuyup DOĞRULADI → [?]'dan D'ye yükseltildi. Ek bulgu: hook'un GÜNCEL varsayılanları UYARI 72 · **DURDUR 144** (`:11`, `:20`), İB-07 raporunun andığı "DUR 72" eski eşiktir. |
| 22 | PK-10 "büyüyen iterasyon ayak-izi → SIRALI" fiilen koşan koddur ve verimlilik tercihini geçersiz kılar. | eksen-eşleme | `tools/paralel-kapi.py:111-113` (hakem okudu) + `:104-108` PK-1 çakışma dalı | **D** | Kod kanıtı; kural yürürlükte, öneri değil. Ölçüt sıralamasında (iv)'ün en üstte olması bu yüzden doğru. |
| 23 | Toplam maliyet eksen SIRASINDAN bağımsızdır; fark yalnız kurulum (M_dış) teriminde doğar. | maliyet | Formal (çarpma değişme özelliği) + İB-66:205 çarpım kuralı `∏_L (yineleme_L × birim_L)` | **D** | Matematiksel olarak zorunlu; İB-66'nın kendi kuralıyla tutarlı. |
| 24 | "Matris = 2 seviye (nested loop)". | eksen-eşleme | İB-66 §5.1 üç şart: sayaç ∧ durma yüklemi ∧ TAM kapsama | **K** | Tam faktöriyel gridde üçü de sağlanır → 2 seviye. Budamalı/kademeli matriste (iii) kırılır → 2 seviye DEĞİL. Koşullu; koşul şemaya yazılmalı (bkz. B hükmü). |
| 25 | SH indirimi `\|iç\| × η/(η-1)` LLM matrisine uygulanabilir. | maliyet | #6 (ara-değer şart) + iç çelişki: aynı rapor §3'te SH-matrisi "gerçek nested değil, masaya" ilan edip §5'te indirimi hesaplıyor | **X** | Ön-koşul (∃ kısmi_skor) LLM tek-atış hücresi için hiçbir yerde somutlanmadı; formül dayanağı da (Hyperband tam metni) açılmadı. |
| 26 | Ortak iskelet üç araçta aynı: deklaratif eksen → hücre kimliği → per-hücre kütük → toplama/erken-durdurma ayrı adım. | eksen · kütük · toplama | #3, #9, #10, #11 (dördü de açılmış kaynak) | **D** | Dört bağımsız açılmış kaynağın kesişimi; şemanın iskeletini bu kesişim belirlemeli. |

**Sayım: D = 15 · K = 4 · X = 7.**

## 2. (A) MALİYET TABANI — kesin hüküm

**HÜKÜM: Emrin "iterasyon tabanı ~300k" sabiti matris HÜCRESİ için YANLIŞ tabandır. Şema İKİ TABANLI olmalıdır.**

Gerekçe (maskeli, iddia numaralarıyla): İB-66'nın kendi metni tabanı kapsamla sınırlıyor — "işçi/gnhf koşumları içindir" (#17, `raporlar/2026-08-31-ib66-...md:132`), ve o birim İB-66'nın kendi seviye tablosunda **L1 = gnhf iterasyonu** (`:187`), yani kendi `--stop-when` yüklemi ve çok araç-çağrısı olan bir CLI koşumudur. Matris hücresi ise emsallerin üçünde de tek istek/yanıt ya da tek Agent çağrısıdır (#3, #12). Farklı birimlere aynı sabiti koymak ölçümün kapsam beyanını ihlal eder (#18).

**Sayısal dayanak — İB-07'nin gerçek ölçüsü: ÖLÇÜLMEDİ.** `raporlar/2026-08-30-ib07-description-eval.md:48-53` yalnız çağrı sayısı raporluyor (51 işçi denemesi = 45 başarılı + 6 hook-reddi; lider ~65 kendi çağrısı); token ∨ süre ∨ maliyet rakamı hiçbir satırda yok (#19). Ek olarak matrisin boyu da yanlış aktarılmış: gerçek matris 20×3 = 60 hücre, 14 skill koşum ekseni değil etiket uzayıdır (#20) — dolayısıyla antitezin "840 hücre × 300k ≈ 252M" aritmetiği de çürüktür; hükmü ayakta tutan şey bu aritmetik değil, #17'deki kapsam beyanıdır.

**ŞEMAYA GİRECEK FORMÜL (maliyet alanı, v0):**

```
TANIM
  hücre_tipi ∈ {tek_cagri, gnhf_iterasyonu}          [her matris manifestinde ZORUNLU beyan]
  T_hücre    = tek_cagri birim maliyeti (token, önbellek-okuma DAHİL)  → ÖLÇÜLMEDİ (borç M-1)
  T_gnhf     = 300k  [ÖLÇÜLDÜ, önbellek-okuma dahil; İB-66:132 · e2e715, 08-30]
  M_dış      = dış eksen değeri başına kurulum (bağlam/skill yükleme)
  T          = (hücre_tipi = gnhf_iterasyonu) ? T_gnhf : T_hücre

TOKEN BÜTÇESİ
  toplam ≈ |dış| × M_dış  +  |dış| × |iç| × tekrar × T
  Ö1: toplam ≤ 0,8 × B_oturum        → koşuma izin ver   [İB-66 §5.3 Şablon-1 ile aynı biçim]
  ¬Ö1 → koşma; |iç| ∨ tekrar küçült ∨ Salih'e bildir

ÇAĞRI BÜTÇESİ (token'dan BAĞIMSIZ İKİNCİ KAPI — İB-07'yi kesen kapı budur)
  N_cagri = |dış| × |iç| × tekrar
  Ö2: N_cagri + sayac_oturum ≤ DURDUR        [hook güncel varsayılan DURDUR=144, UYARI=72;
                                              sayaç OTURUM-genelinde kümülatif — #21]
  ¬Ö2 → matrisi oturuma böl (kütük append-only + hücre_anahtari ile resume)

ÖLÇÜM BORCU M-1: ilk gerçek matris koşumunda her satır token_giris/token_cikis/
  token_onbellek_okuma/sure_ms alanlarını yazar; T_hücre bu kütükten TÜRETİLİR,
  tahminle DOLDURULMAZ (m.29 deneysel damga).
```

Tek-tabanlı model REDDEDİLİR: tek taban ya gnhf'yi hafife alır ya tek-çağrı hücresini 1-2 mertebe abartır ve — İB-07 kanıtının gösterdiği gibi — asıl bağlayıcı kısıtı (çağrı sayacı) tamamen ıskalar.

## 3. (B) ERKEN-DURDURMA — kesin hüküm

**HÜKÜM 1: Klasik successive halving, tek-atış LLM eval matrisine UYGULANAMAZ.** Optuna'nın kendi dokümanı budamanın tetikleyicisini `trial.report(intermediate_value, step)` + `should_prune()` olarak tanımlar (#6, V26 bağımsız doğruladı). Tek-atış bir tamamlama için "adım" yoktur: yanıt ya bitmiştir ya bitmemiştir, yarım yanıtın kalite skoru tanımsızdır. `∃ kısmi_skor` öncülü yedi raporun hiçbirinde somutlanmadı. Dolayısıyla `η/(η-1)` indirim formülü şemaya GİRMEZ (#25 = X).

**HÜKÜM 2: İndirim yine de mümkündür ama SH'den değil — iki kademeli deterministik eşik-filtresinden gelir.** Kaynağı budama değil, hücre-tipi ayrımıdır: ucuz kademe (kural-tabanlı ∨ küçük model ∨ tek-alan dönen işçi — İB-07 emsali) tüm hücreleri koşar, pahalı kademe yalnız eşiği geçen alt kümeyi koşar:
```
toplam = N × T_ucuz + k × T_pahali ,  k = |{hücre : proxy_skor ≥ eşik}| ,  eşik SABİT ∧ önceden yazılı
```
Bu deterministiktir (aynı girdi → aynı k), bandit değildir, m.6 ile uyumludur. `kademe` şemada ÜÇÜNCÜ bir eksen olarak beyan edilir, dış/iç ikilisine gizlenmez.

**HÜKÜM 3: "Matris = 2 seviye" KOŞULLUDUR — koşul şemaya yazılır.**
```
matris_2_seviye ↔ (her eksenin kendi sayacı var) ∧ (her eksenin kendi durma yüklemi var)
                  ∧ (∀ dış değeri: iç eksen TAM koşulur)        [İB-66 §5.1 (i)∧(ii)∧(iii)]
tam_faktoriyel ∧ ¬erken_durdurma      → matris = 2 seviye              [D]
kademe_filtresi ∨ budama              → (iii) KIRILIR → 2 seviye DEĞİL:
     üçüncü sayaç (kademe) + BÜZÜLEN aday kümesi → İB-66 §5.2'nin
     hiçbir sınıfına girmez → yeni alt-tür, MASAYA (İB-65 S1 md.1.6 emsali)
```
Yani: tam-faktöriyel matris için "2 seviye" DESTEKLİ; kademeli/budamalı matris için ÇÜRÜK. Şema bu ayrımı bir bayrakla (`erken_durdurma: yok | kademe_esigi`) zorunlu kılmalıdır.

## 4. Hakem tavsiyeleri — 5 zorunlu alan

**1) Eksen tanımı.** Eksenler koşum script'inde DEĞİL, ayrı deklaratif manifest dosyasında dursun (`veri/sozlesme/<is>-eksen.json`): eksen adı, değer listesi, kardinalite, `tekrar`, ve eksenin `dis`/`ic` rolü. Üç açılmış araç emsali de bunu böyle yapıyor (#3, #9, #10). Dış/iç seçimi ölçüt sırası (iv) PK-10 > (ii) bağımsızlık > (i) kurulum-maliyeti ile verilsin; (iii) erken-durdurma ölçüt olarak DÜŞÜRÜLSÜN — o bir eksen değil, ayrı `kademe` bayrağıdır. Manifest ayrıca eksen değerlerinin TAM kümesini içerir; resume farkı buradan hesaplanır (İB-07 dersi).

**2) Hücre sözleşmesi.** Hücre = tek koşum birimi; sözleşme ZORUNLU olarak (a) `hucre_tipi` ∈ {tek_cagri, gnhf_iterasyonu}, (b) çıktı tipi — kapalı-küme etiket ∨ sayı ∨ yapılandırılmış obje, **serbest metin YASAK** (bu kısıt olmadan Karar 65'in LLM'siz toplaması imkânsız, #14), (c) `hucre_anahtari` = eksen değerlerinin deterministik serileştirmesinden türetilen sabit id. Anahtar hem idempotency (#11) hem yinelenen-koşum tespiti (#5) hem resume için tek çözümdür.

**3) Toplama / indirgeme (LLM'siz deterministik, Karar 65).** Toplama AYRI bir adımdır ve hücre koşumuyla asla aynı çağrıda yapılmaz (#10). Girdi bronz jsonl, çıktı gold görünüm; hesap yalnız sayım/oran/marjinal ortalama/etkileşim farkı — hepsi aynı kütükten aynı sayıyı üretir. Karar 65 şemaya koşullu yazılsın: "LLM'siz toplama ⟺ hücre sözleşmesi çıktıyı tiplendiriyor". Serbest-metin gerekiyorsa bu bir İSTİSNA dalıdır: LLM-judge ayrı bir hücre-tipi olarak beyan edilir, kendi maliyeti kütüğe yazılır, deterministik sayılmaz.

**4) Maliyet modeli.** §2'deki iki-tabanlı formül aynen alınsın: `T_gnhf = 300k` (ölçülmüş, yalnız gnhf iterasyonu için), `T_hücre` = ÖLÇÜLMEDİ ve ilk koşumda ölçülecek borç (M-1); tahminle doldurulmaz. Token kapısının YANINDA ikinci ve bağımsız bir **çağrı-sayısı kapısı** dursun (`N_cagri + sayac_oturum ≤ 144`, sayaç oturum-kümülatif, #21) — İB-07'yi kesen kapı token değil buydu ve hiçbir tez raporu bunu maliyet modeline koymamıştı.

**5) Kütük standardı.** Tek jsonl, append-only, satır başına: `hucre_anahtari` (ZORUNLU, tekil) · `kosum_id` · `ts` · `git_head` · `eksen_degerleri` (obje) · `tekrar` · `hucre_tipi` · `model` (tam API snapshot id — kısa ad yasak, #16) · `sonuc` {tip, deger} · `toplama_yontemi` {llm, deterministik} · `token_giris`/`token_cikis`/`token_onbellek_okuma`/`sure_ms` (M-1 ölçümü) · `kosum_durumu`. Resume kuralı kütükten tek sorguyla çıkmalı: `manifest_anahtarlar − kütük_anahtarlar = kalan iş`.

## 5. Hakemin kendi sınırları
- Hakem WebFetch yapmadı; dış-kaynak D'leri "rapor açıldı beyan etti ∧ V26 bağımsız denetimi çelişmedi" tabanlıdır. V26 yalnız 4 iddia örnekledi — açılmamış-URL riski örneklem dışında kalan dış iddialar için sıfırlanmadı.
- `raporlar/2026-08-31-k010-a3-loop-1.md:12-13` (300k'nın asıl ölçüm kaydı) bu koşumda AÇILMADI; #17 İB-66'nın aktarımına dayanıyor. `[?]` — 300k'nın ham ölçüm satırı ayrıca teyit edilmeli.
- K-020 kararı verilmedi; yukarıdakiler girdidir, hüküm masadadır.
