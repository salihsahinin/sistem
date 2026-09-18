# AB-1 TEZ Raporu — Skill/Prompt Bakım Sistemleri Dışarıda Nasıl Çözülmüş?

**Rol:** S-1a (skill-bakim-tez) · **Ajan:** ATLAS · **Rejim:** maliyet-öncelikli · **Model:** sonnet
**Tarih:** 2026-08-21 · **Araştırma sorusu:** LLM-ajan skill/prompt varlıklarının PERİYODİK BAKIMI dışarıda nasıl çözülmüş? (eval yenileme · description/tetik isabeti ölçümü · kullanım+drift ölçümü · emeklilik/onarım kriteri · bakım aralığı/tetiği: takvim ∨ koşum-sayısı ∨ sapma-sinyali)

**Kapsam dışı olan (bu raporda YOK):** bakım sisteminin tasarım kararı, antitez (S-1b), iç repo taraması, skill yazımı — bunlar başka masaların işi.

---

## 1. Bulgular (D/K/X + URL)

### D-1 — Anthropic skill-creator: eval/benchmark güncellemesi, bakım tetiği "model güncellemesi sonrası"
**Kaynak:** https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills (AÇILDI/OKUNDU)
Skill-creator artık eval yazma, benchmark modu (başarı oranı + süre + token izleme), çoklu-ajan paralel test, A/B karşılaştırma (comparator ajanı, "hangisi olduğunu bilmeden" yargılıyor) ve description optimizasyonunu (false positive/negative azaltma) destekliyor. **Bakım tetiği açıkça takvimli DEĞİL** — belge "model güncellemeleri sonrasında" çalıştırılmasını öneriyor; bir capability skill'in artık gereksiz olduğunu evaller ortaya çıkarıyor.
**Üstüne-oturma:** `skill-uretim-semasi` BAKIM düğümünün "ne zaman tetiklenir" sorusuna doğrudan emsal — bizim m.43 pencereli sayacımız (koşum-sayısı tetikli) bu emsalle aynı ailede (olay-tetikli), takvim değil.

### D-2 — skill-creator SKILL.md: İB-07'nin kaynağı olan mekanizmanın ta kendisi
**Kaynak:** https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md (AÇILDI/OKUNDU)
Somut komutlar: `evals/evals.json` formatı, `scripts.aggregate_benchmark` → `benchmark.json`/`benchmark.md`, description/tetik optimizasyon döngüsü `scripts.run_loop`: **20 tetik sorgusu (8-10 should-trigger + 8-10 should-not-trigger), her sorgu 3x çalıştırılır, %60/%40 train/test bölünmesi, max 5 iterasyon, overfit'ten kaçınmak için test-skoruyla seçim.**
**Üstüne-oturma:** Bizim İB-07 planı ("20 sorgu×3×14 skill") bu mekanizmanın **birebir aynısı** — yani İB-07 zaten Anthropic'in kendi run_loop tasarımının üstüne oturuyor, ayrı bir icat değil. Kalan iş yalnız betiği bizim 14 skill'e uygulamak (hazırı-temel-al doğrulandı).

### D-3 — promptfoo pratiği (scrolltest.com): katmanlı takvim + "sahipsiz eval çürür" uyarısı
**Kaynak:** https://scrolltest.com/llm-regression-testing-promptfoo/ (AÇILDI/OKUNDU)
Önerilen üç katmanlı test sıklığı: **PR düzeyinde 10 kritik test (olay-tetikli) · gece çalışması 100 geniş test (takvimli) · büyük değişiklik öncesi tam set (olay-tetikli).** Açık uyarı: "sahibi olmayan bir eval suite zamanla eskir." Drift tespiti için özel bir cron mekanizması bu yazıda AÇIKÇA ELE ALINMIYOR (aranan ama bulunamayan nokta — meşru "yok" cevabı).
**Üstüne-oturma:** Bizim `v_skill_kosum` + Karar 51 eşiği (n≥10 → medyan-band) olay-tetikli katmana denk düşüyor; bu bulgu, üstüne bir **takvimli "gece/haftalık" katman** eklemenin dış emsali olabilir — ki bu şu an bizim sistemde YOK (bkz. §3 boşluk).

### D-4 — Braintrust: baseline-karşı-güncel karşılaştırma + üç tetik seviyesi
**Kaynak:** https://www.braintrust.dev/articles/what-is-llm-monitoring (AÇILDI/OKUNDU)
Drift = "current behavior against historical baselines" karşılaştırması. Üç tetik: (1) her PR'da otomatik eval, (2) değişiklik öncesi baseline kurulumu, (3) production'da sürekli örneklem-skorlama.
**Üstüne-oturma:** Bizim m.43 pencereli sayaç (N=5, W=90 gün) + `v_skill_kosum` (n·token·süre·sonuc/fail) tam olarak "baseline'a karşı güncel karşılaştırma" desenine denk düşüyor — bu mimarinin dışarıda tanınan bir desen olduğunu doğruluyor (hazırı-temel-al zaten doğru yoldaydı, yeniden icat gerekmiyor).

### D-5 — LangSmith: offline/online ayrımı + dataset otomatik versiyonlama
**Kaynak:** https://docs.langchain.com/langsmith/evaluation-concepts (AÇILDI/OKUNDU)
Offline eval (küratörlü test setinde regresyon/backtest, deployment ÖNCESİ) vs online eval (canlı trafikte gerçek-zamanlı drift tespiti). Dataset her düzenlemede otomatik yeni versiyon alıyor; CI'da belirli versiyona sabitlenebiliyor. **Tetikleme periyodikliği (ne sıklıkla) dokümanda AÇIKÇA belirtilmiyor** — bu bir boşluk olarak not edildi.
**Üstüne-oturma:** Offline/online ayrımı, bizim "ilk pencerede Δ̂ ölçülür" (offline/kuruluş-anı) ile "koşum-sırasında v_skill_kosum'a düşen veri" (online/sürekli) ayrımıyla zaten örtüşüyor — kavramsal doğrulama, yeni mekanizma değil.

### D-6 — Agenta prompt-drift: somut sayısal örnek + "haftalık en az" önerisi
**Kaynak:** https://agenta.ai/blog/prompt-drift (AÇILDI/OKUNDU)
Prompt drift'in somut örneği: GPT-4'ün asal-sayı-tanıma doğruluğu Mart 2023'te %84 iken Haziran 2023'te %51'e düşmüş (Agenta bu rakamı aktarıyor; **birincil kaynak — muhtemelen Chen ve ark. 2023 "How is ChatGPT's behavior changing over time" çalışması — bu koşumda AÇILMADI, dolayısıyla bu spesifik rakam için Agenta ikincil aktarım sayılır, K-derece dikkat**). Üç adımlı tespit: gözlemlenebilirlik (tüm etkileşim izlenir) → otomatik değerlendirme (örneklenen trafik puanlanır) → zaman-serisi analizi (skor düşüşü, varyans artışı, uzunluk/gecikme değişimi). Önerilen bakım aralığı: **"sürekli izleme ideal; minimumda haftalık regresyon testi + her prompt/model değişiminde kontrol."**
**Üstüne-oturma:** Bu rapor sorusundaki "bakım aralığı: takvim ∨ koşum-sayısı ∨ sapma-sinyali" ayrımına EN DOĞRUDAN cevap — dış pratik bir **taban (floor) takvim + olay-tetik hibridi** öneriyor. Bizim m.43'te şu an yalnız koşum-sayısı (N=5) var, takvim tabanlı bir alt sınır (ör. "90 gün içinde en az 1 kontrol") yok — bu D-6 + D-9'un işaret ettiği somut boşluk.

### D-7 — Agent skill versiyonlama + 4-aşamalı emeklilik kriteri
**Kaynak:** https://aiquinta.ai/blog/versioning-agent-skills-semver-compatibility-deprecation/ (AÇILDI/OKUNDU)
SemVer (MAJOR/MINOR/PATCH) skill'lere uyarlanmış. Emeklilik için somut 4 aşama: **(1) `@deprecated` etiketleme → (2) telemetri ile hâlâ kim kullanıyor izleme → (3) yumuşak emeklilik: çıktıya "bu skill 2026-08-01'de kaldırılacak" uyarısı → (4) sert emeklilik: aktif yönlendirmeden kaldırma.** Emeklilik öncesi kontrol listesi: şema değişiklikleri, çıktı bütünlüğü, prompt semantiği, güvenlik yüzeyi.
**Üstüne-oturma:** Sorunun "emeklilik/onarım kriteri" bacağına en somut, doğrudan uygulanabilir cevap — bizim `skill-uretim-semasi` BAKIM düğümünde şu an emeklilik AŞAMALARI tanımlı değil (yalnız Δ̂ ölçümü var); bu 4 aşama neredeyse olduğu gibi devralınabilir bir şablon.

### D-8 — SoK: Agentic Skills (arXiv 2602.20867): 7-aşamalı yaşam döngüsü, ama tetik mekanizması AÇIK PROBLEM
**Kaynak:** https://arxiv.org/html/2602.20867v1 (AÇILDI/OKUNDU)
Akademik tarama, skill yaşam döngüsünü 7 aşamada tanımlıyor (Discovery → Practice/Refinement → Distillation → Storage → Retrieval/Composition → Execution → **Evaluation/Update**). Son aşama: "dağıtım sonrası performans izleme, sapma/başarısızlık tespiti, revizyon/değiştirme/emekli etme." **Önemli:** Makale, tetik mekanizmasının (periyodik mi olay-tetikli mi) ve somut eşik değerlerinin (başarısızlık yüzdesi, karar ağacı) literatürde net tanımlanmadığını AÇIKÇA belirtiyor — "açık problem" olarak bırakıyor.
**Üstüne-oturma:** Bu bulgu, bizim Karar 51 (n≥10 medyan-band) + m.43 (N=5,W=90gün) tasarımlarının **literatürde hazır bir karşılığı olmayan, kendi başımıza doldurduğumuz bir boşluk** olduğunu doğruluyor — yani burada "hazırı temel al" değil, gerçekten kendi eşik tasarımımızı savunmamız gerekiyor (antitez S-1b ile birlikte okunmalı).

### D-9 — Somut hibrit örnek: PR-tetik + haftalık canary
**Kaynak:** https://securelybuilt.substack.com/p/unit-tests-for-llms-catching-model (AÇILDI/OKUNDU)
Gerçek bir uygulamadan alıntı: "The design supports PR triggers and a weekly canary, however, both are currently disabled" (yazar henüz yalnız elle tetikleme kullanıyor). Haftalık canary'nin amacı: "catch drift that lands outside any PR, like a model version bump or a change in your retrieval data" — yani PR'da yakalanamayan (model sağlayıcı tarafında sessiz güncelleme gibi) sapmaları yakalamak için TAKVİMLİ bir yedek katman.
**Üstüne-oturma:** D-6'yı somutlaştırıyor — bizim m.43'e eklenebilecek "haftalık/aylık canary" katmanının nasıl göründüğüne dair birebir kod-seviyesi emsal (PR-tetik ≈ bizim koşum-sayısı/sapma-sinyali, weekly canary ≈ eksik olan takvim katmanı).

---

## 2. Jarvis'e Uygulanabilirlik

- **İB-07 (description-eval, 20 sorgu×3×14 skill)** zaten Anthropic'in kendi `run_loop` mekanizmasının (D-2) doğrudan kopyası — icat değil, uygulama işi. Betik hazır (`scripts.run_loop`), yalnız bizim skill setimize bağlanması gerekiyor.
- **Karar 51 + m.43 (n≥10 medyan-band, N=5/W=90gün)** dışarıda tanınan "baseline-karşı-güncel" desenine (D-4, D-5) uyuyor — mimari doğru; ama SAF olay/koşum-sayısı tetikli, TAKVİM YOK. D-6 ve D-9, bu boşluğa somut bir yama öneriyor: haftalık/aylık bir "canary" alt-katmanı (ör. "90 gün içinde hiç koşum olmadıysa yine de 1 kontrol zorunlu kıl").
- **Emeklilik/onarım kriteri** bizim kanonda YOK (yalnız Δ̂ ölçülüyor, ne olursa emekli edileceği tanımsız). D-7'nin 4 aşaması (`@deprecated` etiket → telemetri → tarihli uyarı → sert kaldırma) doğrudan devralınabilir şablon.
- **D-8 açık-problem tespiti** önemli bir sınır: eşik SAYILARI (n≥10, N=5, W=90gün) konusunda dışarıda "doğru cevap" yok — bunlar Jarvis'in kendi tasarım kararı olarak kalmalı, dış literatürle meşrulaştırılamaz (bu, S-1b antitez tarafının işine malzeme olabilir).

---

## 3. F2 Destek-Kontrol Tablosu (her iddia → kaynağı)

| # | İddia (özet) | Kaynak | D/K/X |
|---|---|---|---|
| 1 | Skill-creator eval/benchmark/A-B karşılaştırma; tetik = model güncellemesi sonrası | claude.com/blog/improving-skill-creator... | D |
| 2 | run_loop: 20 sorgu (8-10/8-10), 3x çalıştırma, %60/40 split, max 5 iterasyon | github.com/anthropics/skills SKILL.md | D |
| 3 | promptfoo: PR-10/gece-100/büyük-değişiklik-tam-set katmanlaması; "sahipsiz eval çürür" | scrolltest.com/llm-regression-testing-promptfoo | D |
| 4 | Drift = baseline'a karşı güncel karşılaştırma; 3 tetik seviyesi | braintrust.dev/articles/what-is-llm-monitoring | D |
| 5 | Offline/online eval ayrımı; dataset otomatik versiyonlama; periyodiklik belirtilmemiş | docs.langchain.com/langsmith/evaluation-concepts | D |
| 6 | GPT-4 asal-sayı doğruluğu %84→%51 (Mar-Haz 2023) | agenta.ai/blog/prompt-drift (birincil kaynak açılmadı) | K |
| 6b | 3 adımlı tespit + "sürekli ideal, min. haftalık" önerisi | agenta.ai/blog/prompt-drift | D |
| 7 | SemVer + 4 aşamalı emeklilik (@deprecated→telemetri→uyarı→kaldırma) | aiquinta.ai/blog/versioning-agent-skills... | D |
| 8 | 7 aşamalı skill yaşam döngüsü; tetik mekanizması literatürde açık problem | arxiv.org/html/2602.20867v1 (SoK: Agentic Skills) | D |
| 9 | Gerçek örnek: PR-tetik + haftalık canary, ikisi de "henüz devre dışı" | securelybuilt.substack.com/p/unit-tests-for-llms... | D |
| 10 | İB-07 planı (20 sorgu×3×14 skill) = Anthropic run_loop ile birebir aynı desen | iç çıkarım (D-2'ye dayanarak) — kanon-karşılaştırma | D (D-2 üzerinden) |

**Etiketsiz iddia: 0.**

---

## 4. Cevaplanamayanlar

- Somut sayısal eşik ("%X performans düşüşünde emekli et", "kaç başarısız koşumdan sonra onar") — hiçbir kaynakta verilmedi; D-8 bunu açıkça "açık problem" ilan ediyor.
- "Description/tetik yeniden-değerlendirmesi kaç günde/kaç koşumda bir yapılmalı" — Anthropic yalnız "model güncellemesi sonrası" diyor, takvim vermiyor (D-1); dış literatürde bu soruya dolaysız/sayısal cevap bulunamadı.
- Agenta'nın aktardığı %84→%51 rakamının birincil kaynağı (muhtemelen Chen ve ark. 2023 çalışması) bu koşumda AÇILMADI — F3/F5 gereği bu rakam yalnız "Agenta böyle diyor" (K) olarak sayılmalı, birincil doğrulama ayrı bir tekil-kaynak-doğrulama işi gerektirir (S-5 modeline benzer bir borç olarak Carvis'e not düşülebilir).
- Erişim engeli: yok — denenen 9 URL'nin tamamı açıldı/okundu.

---

**Kosum özeti:** ~15 WebSearch/WebFetch çağrısı (tahmini 15-30 araç bandının içinde), 9 D + 1 K bulgu, hepsi üstüne-oturma satırlı.
