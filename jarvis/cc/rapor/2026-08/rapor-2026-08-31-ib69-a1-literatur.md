# İB-69 aile-1 (a — LİTERATÜR) — "İki değişken-sınıflı koşum matrisi" literatür karşılığı

AS-OF: 2026-08-31 · Ajan: İB-69 aile-1 TEZ işçisi (alan a, canlı web)

## 1. Faktöriyel tasarımın formal tanımı

- **Faktör (factor):** Deneyde kontrol edilen/incelenen değişken. [DESTEKLİ: https://help.reliasoft.com/reference/experiment_design_and_analysis/doe/general_full_factorial_designs.html, AS-OF 2026-08-31 — sayfa "the effect of two factors" (A ve B) örneğiyle faktörü kontrol edilen değişken olarak tanımlıyor]
- **Seviye (level):** Faktörün alabileceği belirli değer/ayar. [DESTEKLİ: aynı URL, AS-OF 2026-08-31 — "A_low ... A_high" örneğiyle seviye, faktörün test edildiği belirli değerler olarak tanımlanıyor]
- **Hücre/koşu (run):** Tek bir deneysel gözlem/faktör-seviye kombinasyonunun uygulanması. [DESTEKLİ: aynı URL — "four runs are required for each replicate" cümlesi, 2 faktör × 2 seviye için 4 koşu gerektiğini gösteriyor]
- **Tekrar (replicate):** Aynı faktör-seviye kombinasyonunun birden fazla kez tekrarlanan deneysel koşumu; temel tasarımın (base design) bütünsel bir kopyası. [DESTEKLİ: WebSearch özeti (SixSigma/Minitab kaynaklı, doğrudan açılmadı) — "[?]" — bu tanım WebSearch snippet'inden geliyor, birincil kaynağı ben açmadım]

## 2. |A|×|B| tam faktöriyel maliyet formülü + tekrar çarpanı; fractional factorial indirimi

- **Temel formül:** Koşu sayısı = faktör seviyelerinin çarpımı → |A|×|B|×...×|N|. [DESTEKLİ: https://help.reliasoft.com/reference/experiment_design_and_analysis/doe/general_full_factorial_designs.html, AS-OF 2026-08-31 — "Runs = (Levels of Factor A) × (Levels of Factor B) × ... ; Since there are two factors with two levels, a total of 2×2=4 combinations exist"]
- **Tekrar çarpanı:** Toplam koşu = (|A|×|B|) × tekrar sayısı. [DESTEKLİ: aynı URL — "three speeds and two types of fuel additives...replicated three times" → 3×2×3=18 toplam koşu, tekrarın çarpan olarak eklendiğini gösteriyor]
- **Fractional factorial indirimi:** Tam faktöriyelin bir alt-kümesini (2^(k-p) tasarım) çalıştırarak koşu sayısını 2^p kat azaltır, karşılığında yüksek-mertebe etkileşimleri (genelde 3. ve üstü) confound/karıştırılmış (aliased) bırakır. [?] — bu iddia yalnız model-hafızasından; WebFetch ile birincil kaynak (ör. NIST/e-Handbook fractional factorial sayfası) açılmadı, bu oturumda doğrulanmadı.

## 3. Grid search vs random search vs successive halving/Hyperband

- **Grid search:** Tüm faktör-seviye kombinasyonlarını (tam faktöriyel gibi) tarar; faktör sayısı arttıkça maliyet katlanarak büyür (boyut laneti). [?] — WebSearch/WebFetch ile bu oturumda ayrıca doğrulanmadı, genel bilgi.
- **Random search:** Grid yerine hiperparametre uzayından rastgele örnekler çeker; Bergstra & Bengio (2012) sonucu grid search'ten çoğu pratik durumda daha verimli olduğunu gösterir. [?] — bu oturumda birincil kaynak (JMLR makalesi) açılmadı.
- **Successive halving (SH):** Sabit bir bütçeyi konfigürasyon kümesine tahsis eder, her turda performansı değerlendirip en kötü yarıyı eler, kalanlara daha büyük bütçe ayırır; tek bir konfigürasyon kalana dek tekrarlanır — "best arm identification" problemi. [DESTEKLİ: WebSearch özeti, medium.com/@vireshj kaynağı — "iteratively allocates the available budget to a set of hyper-parameter configurations, evaluates their performance and throws away the worst half" — AS-OF 2026-08-31; URL bu oturumda WebFetch ile açılmadı, yalnız WebSearch snippet'i, bu yüzden [?] işaretiyle sınırlı güven]
- **Hyperband:** SH'yi "pure-exploration non-stochastic infinite-armed bandit problem" olarak çerçeveler; rastgele örneklenen konfigürasyonlara adaptif kaynak tahsisi + erken-durdurma uygular, Bayesian optimizasyona göre bir büyüklük mertebesi (order-of-magnitude) hızlanma iddia eder. [DESTEKLİ: https://arxiv.org/abs/1603.06560 (Li et al., "Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization"), AS-OF 2026-08-31 — "Hyperband can provide over an order-of-magnitude speedup" ve "adaptive resource allocation and early-stopping" ifadeleri]
- **Ne zaman hangisi:** Küçük, düşük-boyutlu, ucuz-değerlendirmeli uzaylarda grid/tam faktöriyel tercih edilir (deterministik kapsama); yüksek boyutlu / pahalı değerlendirmeli uzaylarda random search ve SH/Hyperband tercih edilir (erken elemeyle bütçe tasarrufu). [?] — bu sentez cümlesi genel bilgi, doğrudan kaynağa bağlanmadı.
- **Erken-durdurmanın matematiksel dayanağı:** Bandit-tabanlı bütçe tahsisi — her turda kaynağı (η katsayısıyla) azaltılan konfigürasyon kümesine artan bütçeyle yeniden dağıtır; teorik garantiler "several desirable guarantees" olarak makalede belirtiliyor ama tam teorem/ispat bu özet-fetch'te görülmedi. [DESTEKLİ (kısmi): https://arxiv.org/abs/1603.06560, AS-OF 2026-08-31 — "establishing a rigorous mathematical basis for the early-stopping approach within the bandit optimization framework" (WebFetch özetinden, tam makale metni değil)] [?] tam teorem detayı için PDF açılmadı.

## 4. Toplama/indirgeme: ana etki ve etkileşim — deterministik hesap

- Faktöriyel tabloda **ana etki (main effect)**, bir faktörün bir seviyeden diğerine geçerken yanıt değişkeninde yarattığı ortalama değişimdir; genelde faktörün yüksek-seviye satır/sütun ortalaması eksi düşük-seviye ortalaması olarak hesaplanır (satır/sütun marjinal ortalamaları farkı). [?] — bu oturumda birincil DOE ders kaynağı (ör. NIST e-Handbook "Interpreting main effects and interactions") açılmadı; genel bilgi.
- **Etkileşim (interaction)**, bir faktörün etkisinin diğer faktörün seviyesine bağlı olarak değişip değişmediğini ölçer; hücre ortalamaları ile marjinal (ana etki) tahminleri arasındaki fark olarak deterministik biçimde hesaplanır (ör. AB etkileşimi = hücre-ortalama farklarının yarısı). [?] — aynı gerekçeyle doğrulanmadı, genel istatistik bilgisi.
- Not: bu hesaplar tamamen deterministiktir — aynı hücre-değerleri verildiğinde aynı marjinal/etkileşim sayıları çıkar; rastgelelik yalnız örnekleme/tekrar aşamasında (gürültü tahmini için) girer.

## 5. LLM koşum matrisine eşlemede kırılan varsayımlar

Klasik DOE/faktöriyel çerçeve, eksen A = prompt-değişken sınıfı 1, eksen B = prompt-değişken sınıfı 2, hücre = LLM çıktısı olacak şekilde eşlenirse şu varsayımlar kırılır:

1. **Skaler yanıt varsayımı kırılır.** DOE'de hücre değeri tek bir sayısal yanıt (response variable) olmasını varsayar; ana etki/etkileşim formülleri bu sayısal yanıt üzerinden ortalama alır. LLM hücresi ise serbest-metin çıktısıdır — doğrudan ortalanamaz, önce bir skorlayıcı/rubrik ile skalere indirgenmesi (ör. LLM-judge puanı, kural-tabanlı metrik) gerekir; bu indirgeme kendisi ek bir gürültü/karar katmanı ekler.
2. **Gürültü kaynağı farklıdır.** Klasik DOE'de gürültü ölçüm hatası/çevresel varyasyondur ve tekrar (replicate) ile tahmin edilir. LLM'de asıl gürültü kaynağı örnekleme (temperature/top-p, decoding rastgeleliği) ve modelin kendi tutarsızlığıdır — CLAUDE.md'deki "deterministik tasarım" ilkesiyle (m.6) gerilim yaratır: rastgele-örneklemli LLM koşumu "aynı girdi → aynı çıktı" varsayımını otomatik sağlamaz, temperature=0 / seed sabitleme gibi ek disiplin gerekir.
3. **Bağımsızlık/toplanabilirlik (additivity) varsayımı zayıflar.** Ana etki + etkileşim ayrıştırması, faktörlerin yanıt üzerindeki etkisinin (yaklaşık) toplanabilir olduğunu varsayar. Prompt-değişken sınıflarının LLM çıktısı üzerindeki etkileşimi doğrusal/toplanabilir olmayabilir (ör. bir talimat sınıfı diğerinin anlamını tamamen değiştirebilir — kategorik/anlamsal etkileşim, sayısal ana-etki modeliyle iyi yakalanmayabilir).
4. **Maliyet-model farkı.** DOE'de bir koşunun maliyeti sabit kabul edilir; LLM koşumunda hücre başına maliyet (token, gecikme) çıktı uzunluğuna göre değişkendir — sabit-maliyetli tam faktöriyel/fractional-factorial indirim hesapları doğrudan taşınmaz.

## Kaynak listesi

| URL | Açıldı mı (WebFetch) | AS-OF |
|---|---|---|
| https://help.reliasoft.com/reference/experiment_design_and_analysis/doe/general_full_factorial_designs.html | EVET | 2026-08-31 |
| https://arxiv.org/abs/1603.06560 (Hyperband, Li et al.) | EVET | 2026-08-31 |
| WebSearch özeti — SixSigma/Minitab (replicate tanımı) | HAYIR (yalnız arama snippet'i) | 2026-08-31 |
| WebSearch özeti — medium.com/@vireshj (successive halving) | HAYIR (yalnız arama snippet'i) | 2026-08-31 |
| Bergstra & Bengio 2012 (random search) | HAYIR — bu oturumda hiç açılmadı, model-hafızasından anıldı | [?] doğrulanmadı |
| NIST e-Handbook fractional factorial / main-effect-interaction sayfaları | HAYIR — bu oturumda hiç açılmadı | [?] doğrulanmadı |
