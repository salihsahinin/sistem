# İB-69 aile-1 · b1 — Araç Emsalleri: promptfoo × Optuna matris/tarama desenleri

AS-OF: 2026-08-31 · Birincil kaynak: promptfoo.dev, optuna.readthedocs.io (resmî doküman)

## 1. promptfoo — matris kurulumu

**Eksen çarpımı** `prompts × providers × tests`: her prompt her provider'da her test-vaka ile çalıştırılır.
[DESTEKLİ: https://www.promptfoo.dev/docs/configuration/guide/, AS-OF 2026-08-31] — birebir: "Bu yapı, her prompt × provider × test kombinasyonunu değerlendirir." Örnek YAML:
```yaml
prompts: [file://prompt1.txt, file://prompt2.txt]
providers: [openai:gpt-5-mini, vertex:gemini-2.0-flash-exp]
tests:
  - vars: {language: French, input: "Hello world"}
  - vars: {language: German, input: "How's it going?"}
```

**Değişken enjeksiyonu:** Nunjucks templating, `{{language}}`, `{{input}}`; nesne erişimi `{{ user_profile.name }}`, filtre `{{ interests | join(', ') }}`, ortam değişkeni `{{ env.TOPIC }}`.
[DESTEKLİ: aynı URL, AS-OF 2026-08-31]

**repeat/tekrar:** Sayfa içeriğinde `repeat` alanı birebir doğrulanamadı — WebFetch özetinde geçmedi. [?]

**defaultTest / assert:** `defaultTest` tüm test vakalarına ortak `vars`/`assert`/`options.provider` uygular; test kendi `disableDefaultAsserts: true` ile geçersiz kılabilir.
[DESTEKLİ: aynı URL, AS-OF 2026-08-31] — assert örneği: `type: contains`, `type: javascript` (value: `output.toLowerCase().includes('bonjour')`), `type: similar` (threshold: 0.6), `type: llm-rubric`.

**Bir hücre ne üretir / çıktı formatı:** Doküman özetinde JSON/CSV çıktı şemasının alan adları (örn. `success`, `score`, `latencyMs`, `provider`, `prompt`, `vars`) birebir listelenmedi — WebFetch bu düzeyde ayrıntı döndürmedi. [?] Doğrulanan tek şema-benzeri unsur: test seviyesinde `transform` ile çıktının işlenmesi (`output.toUpperCase()`, `output.category`).
[DESTEKLİ: aynı URL, AS-OF 2026-08-31]

**Toplama/özet:** "Pass Rate: İddiaları karşılayan testlerin yüzdesi" ve "Per-Provider Summary: Her model için ayrı başarı oranları" — bu ifadeler WebFetch'in ürettiği özetten geliyor, sayfanın ham metninden birebir alıntı değil; alan adı düzeyinde (örn. tam JSON şema anahtarı) DOĞRULANAMADI. [?]

CSV/harici test kaynağı: `tests: file://tests.csv` ya da Google Sheets URL'i; prompt/provider/test dosyadan da alınabilir (`file://prompts/*.txt`, `file://provider_config.yaml`).
[DESTEKLİ: https://www.promptfoo.dev/docs/configuration/guide/, AS-OF 2026-08-31]

## 2. Optuna — adaptif tarama

**GridSampler (tam faktöriyel):** search_space = `Mapping[str, Sequence[GridValueType]]`, örn. `{"x": [-50, 0, 50], "y": [-99, 0, 99]}` — "exhaustive search over the define-and-run user-specified grids". Tüm kombinasyonlar tükenince normal `optimize()` otomatik durur; ask-and-tell arayüzünde `stop()` iç çağrısı yapılır, RuntimeError elle ele alınmalı. Dağıtık koşumda aynı kombinasyon birden fazla işçiye önerilebilir → fiili deneme sayısı grid boyutunu aşabilir.
[DESTEKLİ: https://optuna.readthedocs.io/en/stable/reference/samplers/generated/optuna.samplers.GridSampler.html, AS-OF 2026-08-31]

**SuccessiveHalvingPruner — erken durdurma sinyali:** kullanıcı `trial.report(intermediate_value, step)` ile ara-değer bildirir, `trial.should_prune()` kontrolü tetikleyicidir. Parametreler: `min_resource` (r, varsayılan 'auto' — ilk denemenin adım sayısına göre), `reduction_factor` (η, varsayılan 4 — her rungda tutulan oran 1/η), `min_early_stopping_rate` (s, varsayılan 0). Mekanizma: rung/bracket sistemi — deneme `min_resource × reduction_factor^s` adıma ulaşana dek kesilmez; rungu tamamlayan deneme o rungtaki diğerleriyle kıyaslanır, yalnız en iyi 1/η sonraki rungya yükseltilir, kalan budanır (bandit-tabanlı).
[DESTEKLİ: https://optuna.readthedocs.io/en/stable/reference/generated/optuna.pruners.SuccessiveHalvingPruner.html, AS-OF 2026-08-31]

**Bütçe kurtarma miktarı (sayısal oran):** kaynak sayfada nicel bir "% bütçe tasarrufu" rakamı doğrulanamadı. [?]

**HyperbandPruner / MedianPruner:** genel `optuna.readthedocs.io/en/stable/reference/samplers/index.html` sayfası bu pruner sınıflarını içermiyor ("Bu pruner sınıfları sağlanan metinde hiç geçmez" — WebFetch sonucu); ayrı sayfaları bu koşumda açılmadı. [?]

**Study/Trial veri modeli ve storage (RDB) kütükleme:** bu koşumda ayrı bir sayfa açılmadı, alan adları (trial number, params, value, state) resmî dokümandan birebir DOĞRULANAMADI. [?]

## 3. Ortak soyutlama

| Kavram | promptfoo | Optuna |
|---|---|---|
| Eksen tanımı | `prompts`, `providers`, `tests[].vars` — statik liste | `search_space` (Grid) ya da sampler'ın önerdiği sürekli/kesikli param uzayı |
| Hücre | prompt×provider×test üçlüsünün tek çalıştırması | tek `Trial` (params kombinasyonu) |
| Kütük satırı | test sonucu (assert pass/fail, transform çıktısı) — şema alanları bu koşumda tam doğrulanamadı [?] | `trial.report(value, step)` ile ara-değer + nihai `value`/`state` |
| Toplama | pass rate, per-provider özet [?] alan-adı düzeyinde doğrulanamadı | `study.best_trial`, `study.trials_dataframe()` (bu koşumda doğrulanmadı) [?] |

**Fark:** promptfoo eksenleri **statik çarpım** — tüm hücreler önceden tanımlı, tümü çalıştırılır (grid tam tarama gibi davranır). Optuna **adaptif**: sampler (TPE, Grid, vb.) bir sonraki denemeyi önceki sonuçlara göre önerir, pruner ara-sonuçlara göre denemeyi erken keser — promptfoo'da "erken kesme" karşılığı yok, her hücre sonuna kadar çalışır.
[DESTEKLİ: yukarıdaki iki bölümün kaynaklarından çıkarım, AS-OF 2026-08-31]

## 4. Jarvis'e taşınabilirlik notu (girdi — karar Salih'te)

**promptfoo (hazır araç) — matris-eval için:**
- Artı 1: YAML-first, kod yazmadan prompt×provider×test matrisi kurulur — Jarvis'in "hazırı temel al" ilkesiyle (m.6) örtüşür.
- Artı 2: Nunjucks değişken enjeksiyonu + `defaultTest`/assert hazır; pass-rate/per-provider özet üretimi kurulu.
- Eksi 1: Node.js ekosistemine bağımlı (npm paketi) — Jarvis'in mevcut Python/DuckDB veri hattına yabancı; entegrasyon köprüsü gerekir (m.17).
- Eksi 2: Çıktı şeması bu koşumda tam doğrulanamadı [?] — Jarvis'in bronz/silver/gold katman şemasına eşlemeden önce ayrı bir doğrulama turu gerekir.

**Kendi harness (matrisli prompt-test) için:**
- Artı 1: Jarvis'in mevcut JSONL bronz-katman + DuckDB gold-view desenine (`veri/bronz/*.jsonl`, `veri/gorunum/*.csv`) doğrudan oturur, ek dönüştürücü gerekmez.
- Artı 2: Türkçe kaynak-kodu ilkesiyle (CLAUDE.md §2) uyumlu, dış paket bağımlılığı yok.
- Eksi 1: Assert-tipi kütüphanesi (contains, similar, llm-rubric vb.) sıfırdan yazılmalı — "hazırı temel al" ilkesine ters, geliştirme maliyeti var.
- Eksi 2: Pass-rate/per-provider toplama script'i sıfırdan yazılmalı; promptfoo'da hazır.

**Optuna (hazır araç) — adaptif hiperparam tarama için:**
- Artı 1: GridSampler tam-faktöriyel + SuccessiveHalvingPruner erken-durdurma birlikte kullanılabilir — büyük parametre uzayında bütçe tasarrufu (nicel oran bu koşumda doğrulanamadı [?]).
- Artı 2: RDB storage ile kalıcı, restart-proof study kütüğü (Jarvis'in "silme yasağı"/pointer ilkesiyle m.20 uyumlu potansiyel).
- Eksi 1: Python paket kurulumu gerekir (bu görev emrinde paket kurmak zaten YASAK) — deneme bu koşumda yapılmadı.
- Eksi 2: Optuna'nın deneme birimi "sürekli hiperparam optimizasyonu" için tasarlı; Jarvis'in ayrık "skill/kural denemesi" senaryosuna doğrudan uymayabilir — eşleme çalışması gerekir.

**Kendi harness (adaptif tarama) için:**
- Artı 1: Jarvis'in deterministik-tasarım ilkesiyle (CLAUDE.md §6, "aynı girdi → aynı yol") pruner'ların olasılıksal/bandit doğası zaten gerilimli — kendi harness bu ilkeye tam uyumlu basit sıralı tarama yazabilir.
- Artı 2: Bağımlılık yok, mevcut hareket-kütüğü/silver-health altyapısına doğrudan entegre olur.
- Eksi 1: Erken-durdurma (successive halving/hyperband) mantığı sıfırdan yazılırsa doğrulama yükü büyük — yanlış budama riski.
- Eksi 2: Study/Trial kalıcı kütük şeması (RDB) sıfırdan tasarlanmalı; Optuna'da hazır ve test edilmiş.

## Kaynak listesi

| URL | WebFetch açıldı | AS-OF |
|---|---|---|
| https://www.promptfoo.dev/docs/configuration/guide/ | EVET | 2026-08-31 |
| https://optuna.readthedocs.io/en/stable/reference/samplers/index.html | EVET (pruner detayı yoktu, ayrı sayfaya yönlendirdi) | 2026-08-31 |
| https://optuna.readthedocs.io/en/stable/reference/generated/optuna.pruners.SuccessiveHalvingPruner.html | EVET | 2026-08-31 |
| https://optuna.readthedocs.io/en/stable/reference/generated/optuna.samplers.GridSampler.html | HAYIR (404) | — |
| https://optuna.readthedocs.io/en/stable/reference/samplers/generated/optuna.samplers.GridSampler.html | EVET | 2026-08-31 |
| HyperbandPruner / MedianPruner ayrı sayfaları | HAYIR (bu koşumda açılmadı) | — |
| Optuna Study/Trial veri modeli sayfası | HAYIR (bu koşumda açılmadı) | — |
