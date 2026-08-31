# İB-69 aile-1 b2 — Araç emsalleri 2: W&B Sweeps · eval-harness grid · Temporal fan-out

AS-OF: 2026-08-31 · Rejim: maliyet-öncelikli · WebFetch: 3/3 gerçek açıldı (kota 2 karşılandı)

## 1. W&B Sweeps

[DESTEKLİ: https://docs.wandb.ai/guides/sweeps/define-sweep-configuration/, AS-OF 2026-08-31]
- `method`: üç arama stratejisi — `grid`, `random`, `bayes`. Birebir alıntı: "The strategy can be as simple as trying every option or as complex as Bayesian Optimization and Hyperband."
- `parameters`: eksen tanımı deklaratif YAML alanlarıyla yapılır — tekil `value: 0.01`, ayrık liste `values: [16, 32, 64]`, ya da dağılım (`distribution: uniform` + `min`/`max`; `q_log_uniform_values` vb.).
- `metric`: `name` (izlenecek log alanı, örn. `validation_loss`) + `goal` (`minimize`/`maximize`).
- `early_terminate`: hyperband tipi — `type: hyperband`, `min_iter`/`max_iter` (durdurma dilimleri), `eta` (bracket geometrisini belirleyen küçültme çarpanı, tipik 3), `s` (bracket sayısını etkileyen parametre). Amaç birebir alıntı: "stop underperforming runs early and preserve resources for more promising configurations."

Run/hücre karşılığı ve agent/controller fan-out modeli: [?] — açılan sayfa parçasında agent-controller mimarisi (her run'ın bir "agent" process'i tarafından çekilip çalıştırılması) doğrudan alıntılanmadı; bu W&B Sweeps'in bilinen genel mimarisi ama bu sayfadan DESTEKLİ değil, ayrı sayfa (`guides/sweeps/quickstart` veya `guides/sweeps/parallelize-agents`) gerekir.

## 2. Eval-harness grid'i (lm-evaluation-harness, GitHub README)

[DESTEKLİ: https://github.com/EleutherAI/lm-evaluation-harness, AS-OF 2026-08-31]
- Görev listesi: "List available tasks with: `lm-eval ls tasks`"; model ve görev seçimi CLI bayraklarıyla (`--model`, `--tasks`).
- Few-shot(k) ekseni: `--num_fewshot` bayrağı; örnek README satırı: "write_out.py ... --num_fewshot 5 --num_examples 10".
- Per-sample kayıt: DESTEKLİ — "we also support logging model responses with the `--log_samples` flag for post-hoc analysis"; çıktı `--output_path` altında, dosya adı deseni `<task_name>_eval_samples.json` (README parçasında JSON gösteriliyor; JSONL formatı bu alıntıda teyit edilmedi → [?]).
- Tekrar/bootstrap (repeats, `--num_fewshot` dışı çoğullama, bootstrap CI hesaplama) ve metric aggregation'ın deterministik olup olmadığı: [?] — README'nin fetch edilen kesitinde detay yok, "interface documentation"a pointer veriliyor (muhtemelen `docs/interface.md`); bu oturumda ikinci bir sayfa açılmadı.
- Modeller × görevler × few-shot(k) × tekrar çarpımının nasıl ifade edildiği (tek komut mu, grid-runner script mi): [?] — CLI tek çalıştırma başına tek (model, task-seti, k) hücresi gibi görünüyor; çoklu-hücre matrisi harness'ın kendisinde değil dış bir sarmalayıcıda (shell loop / sweep aracı) kurulur — bu çıkarım, DESTEKLİ değil.

## 3. Temporal fan-out (child workflow)

[DESTEKLİ: https://docs.temporal.io/develop/typescript/child-workflows, AS-OF 2026-08-31]
- Fan-out deseni: `names.map((name) => executeChild(childWorkflow, { args: [name], ... }))` ile N paralel child workflow başlatma; toplama (gather) `Promise.all(...)` ile — alıntı: "const responseArray = await Promise.all(...); return responseArray.join('\n');"
- Determinism: SDK örtük sağlıyor; `startChild()`/`executeChild()` await edildiğinde framework "internally waits for this Event before returning, so the Child Workflow is guaranteed to have started once the call resolves" — event-sourcing üzerinden deterministik replay.
- Idempotency: `workflowId` seçeneği ("add business-meaningful workflow id here") — iş-anlamlı sabit ID vererek retry'da aynı workflow'un tekrar yaratılmasını engelleme (idempotency mekanizması budur).
- Retry mekaniği detayı (activity-level retry policy, backoff): [?] — açılan kesitte yok; "regular workflow options apply here" ifadesiyle başka bir bölüme pointer veriliyor, bu oturumda açılmadı.
- Eşzamanlılık sınırı (concurrency cap, worker task-queue tuning): [?] — bu sayfada değinilmedi.

## 4. Üç aracın ortak dersi + Jarvis'e taşınabilir 3 kural

Ortak iskelet: **deklaratif eksen tanımı** (sweep.yaml parameters / CLI --model --tasks --num_fewshot / executeChild argümanları) → **hücre kimliği** (W&B run id / lm-eval output dosya adı+task_name / Temporal workflowId) → **kütük** (W&B run log / eval_samples.json / Temporal event history) → **erken durdurma ya da hata izolasyonu** (hyperband early_terminate / lm-eval hata başına task devam eder [?] / Temporal per-child retry+idempotent id).

Somut 3 kural (Jarvis'e taşınabilir, DESTEKLİ kaynaklardan çıkarım — kuralların kendisi [?], dayandığı mekanizmalar DESTEKLİ):
1. **Her matris hücresine sabit, iş-anlamlı bir kimlik ver** (Temporal workflowId deseni) — Jarvis'teki paralel-kapı/pipeline koşumlarında (örn. atlas-kosum aile ajanları) her koşuma tekrar-çalıştırılabilir sabit id (görev+parametre hash'i) atanmalı; aynı id ile tekrar tetiklenirse eski sonuç yeniden kullanılsın/çakışma önlensin.
2. **Eksen tanımı kod/config'te deklaratif dursun, çalıştırma script'i onu okusun** (sweep.yaml / lm-eval CLI bayrakları deseni) — Jarvis'in "hazırı temel al" ilkesiyle örtüşüyor: yeni bir grid/matris ihtiyacında YAML/JSON eksen dosyası + onu okuyan tek koşum script'i, elle yazılmış tekrar-tekrar komut zinciri değil.
3. **Per-hücre ham kayıt (per-sample jsonl benzeri) + toplama ayrı adım** (lm-eval log_samples + ayrı aggregation deseni) — Jarvis'in bronz→silver→gold katman modeliyle zaten uyumlu; yeni bir matris-koşum aracı kurulacaksa ham hücre çıktısı bronz'a, toplanmış metrik gold'a yazılmalı, ikisi aynı adımda karıştırılmamalı.

## Kaynak listesi

| URL | WebFetch açıldı | AS-OF |
|---|---|---|
| https://docs.wandb.ai/guides/sweeps/define-sweep-configuration/ | EVET | 2026-08-31 |
| https://github.com/EleutherAI/lm-evaluation-harness | EVET | 2026-08-31 |
| https://docs.temporal.io/develop/typescript/child-workflows | EVET | 2026-08-31 |
