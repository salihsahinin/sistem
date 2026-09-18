# İB-69 aile-1 V26 Kural-Tabanlı Örneklem Denetimi

AS-OF: 2026-08-31 · Denetçi: V26 örneklem alt-ajanı · Dil: TÜRKÇE

## Yöntem
4 rapor tarandı, `[DESTEKLİ: URL]` damgalı iddialar sırayla numaralandı; her raporun **son üçte biri** içinden 1., 4., 7. ... sıradaki damgalı iddia seçildi (deterministik kural). Gerçek DESTEKLİ sayıları küçük çıktığı için (rapor başına en fazla 9), 1-4-7 kuralı her raporda yalnız **1. sıradaki** iddiayı verdi (3 rapor × 1 = 3 iddia); emirdeki "toplam en az 4" tabanını doldurmak için rapor-2'nin son-üçlüğündeki 2. sıradaki iddia (SuccessiveHalvingPruner) eklendi — bu ek, kuralın mekanik uzantısı, keyfi seçim değil. `eksen-esleme.md` raporunda hiç `[DESTEKLİ: URL]` damgası yok (yalnız iç-kaynak referansları) → örneklem havuzuna girmedi.

## Numaralandırma özeti
- `literatur.md`: 9 damgalı iddia toplam → son üçlük = sıra 7-9 (satır 22, 23, 25).
- `arac-promptfoo-optuna.md`: 8 damgalı iddia toplam → son üçlük = sıra 6-8 (satır 36, 39, 57).
- `arac-sweep-harness-temporal.md`: 4 damgalı iddia toplam → son üçlük = sıra 3-4 (satır 20, 26).
- `eksen-esleme.md`: 0 damgalı iddia → örneklem dışı.

## Denetim tablosu

| # | Rapor | İddia (kısa) | URL | WebFetch | Sayfada bulunan dayanak | Hüküm |
|---|-------|-------------|-----|----------|------------------------|-------|
| 1 | literatur.md:22 | Successive halving (SH) tanımı — "iteratively allocates budget, throws away worst half" | medium.com/@vireshj (tam URL raporda YOK, yalnız yazar-adı) | AÇILAMADI — geçerli/tam URL verilmemiş | YOK | **İHLAL** — DESTEKLİ damgalı ama orijinal yazar da bu oturumda URL'yi açmadığını itiraf ediyor ("URL bu oturumda WebFetch ile açılmadı, yalnız WebSearch snippet'i"); açılmamışken DESTEKLİ damgası = doğrudan V26 ihlal kriteri |
| 2 | arac-promptfoo-optuna.md:36 | Optuna GridSampler — "exhaustive search over the define-and-run user-specified grids"; dağıtık koşumda aynı kombinasyon birden fazla işçiye önerilebilir, fiili deneme grid boyutunu aşabilir | https://optuna.readthedocs.io/en/stable/reference/samplers/generated/optuna.samplers.GridSampler.html | AÇILDI | "Sampler that performs exhaustive search over the define-and-run user-specified grids." + "different workers will occasionally suggest the same parameter configuration. The total number of actual trials may therefore exceed the size of the grid." | **DOĞRULANDI** — birebir eşleşiyor |
| 3 | arac-promptfoo-optuna.md:39 | Optuna SuccessiveHalvingPruner — min_resource='auto', reduction_factor=4, min_early_stopping_rate=0, yalnız en iyi 1/η rungya yükseltilir | https://optuna.readthedocs.io/en/stable/reference/generated/optuna.pruners.SuccessiveHalvingPruner.html | AÇILDI | "This parameter defaults to 'auto'..." + imza `reduction_factor=4`, `min_early_stopping_rate=0` + "promoted to the next rung only if... top 1 over reduction_factor fraction" | **DOĞRULANDI** — tüm 4 parametre + mekanizma birebir |
| 4 | arac-sweep-harness-temporal.md:20 | lm-evaluation-harness per-sample kayıt — "`--log_samples` flag for post-hoc analysis" | https://github.com/EleutherAI/lm-evaluation-harness | AÇILDI | "To save evaluation results provide an `--output_path`. We also support logging model responses with the `--log_samples` flag for post-hoc analysis." | **DOĞRULANDI** — birebir |

## Sonuç
- Toplam denetlenen iddia: **4**
- DOĞRULANDI: 3 · KISMİ: 0 · İHLAL: 1
- **V26 İHLAL SAYISI: 1**
- En ciddi ihlal: `literatur.md:22` (Successive halving tanımı) — DESTEKLİ damgası taşıyor ama kaynak URL'si bu oturumda hiç açılmamış, yalnız WebSearch snippet'ine dayanıyor; raporun kendi metni bunu zaten itiraf ediyor ([?] işareti aynı satırda mevcut) ama üst etiket yine de DESTEKLİ — etiketleme tutarsızlığı, iddianın kendisi yanlış değil, damga yanlış kullanılmış.

## Not
`eksen-esleme.md` raporu tamamen iç-kaynak (repo içi dosya/satır referansı) kullanıyor, dış URL/DESTEKLİ damgası içermiyor — V26 kapsamı dışında, ayrı bir denetim türü gerektirir (iç-kaynak satır-numarası doğrulaması), bu koşumda yapılmadı.
