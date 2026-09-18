# Rapor — AB-3: usage-otomasyon yol seçimi (S-3, kısa atlas)

**Görev:** İB-08 m.40 araştırma-önce şartı · **Soru:** JSONL-parse / OTLP-telemetri / ccusage-sınıfı — hangisi Jarvis'in usage-otomasyonu için temel alınmalı?
**Model:** sonnet · **Rejim:** maliyet-öncelikli · **Tarih:** 2026-08-21

## Bulgular (D/K/X + URL)

### Yol (i) — Transkript-JSONL parse (mevcut yaklaşım: `tools/kosum-maliyeti.py`)

- **D-1:** Transkript formatı **resmî olarak "internal" ilan edilmiş** ve versiyonlar arası değişebilir: *"The entry format is internal to Claude Code and changes between versions, so scripts that parse these files directly can break on any release. To build on session data, use /export or the script interfaces instead."* — kaynak: https://code.claude.com/docs/en/sessions (doğrudan açıldı/okundu)
- **D-2:** Bu kırılganlık teorik değil, somut örneği var: Claude Code 2.1.169'da (WSL2 + macOS) interaktif oturumlarda JSONL'e yalnız `ai-title` stub kaydı yazılmış, hiç `user`/`assistant` kaydı düşmemiş → `--resume` ve JSONL'i takip eden araçlar kırılmış (2.1.168'de sorun yok, regresyon). Kaynak: https://github.com/anthropics/claude-code/issues/66486 (doğrudan açıldı/okundu)
- **D-3:** Anthropic'in kendi önerdiği alternatif "script interface"ler var: `claude -p --output-format json/stream-json` (yapılandırılmış sonuç: session ID, usage, cost) ve hook'lardaki `transcript_path` alanı — bunlar JSONL'i doğrudan parse etmekten daha stabil arayüzler. Kaynak: aynı sessions sayfası (D-1 ile aynı kaynak).

### Yol (ii) — OTLP/OpenTelemetry telemetri

- **D-4:** Claude Code CLI'da OTLP instrümantasyonu YERLEŞİK: `OTEL_METRICS_EXPORTER` ile token/cost/session/LOC/tool-decision sayaçları, `OTEL_LOGS_EXPORTER` ile prompt/API/tool-result olay kayıtları, `OTEL_TRACES_EXPORTER` (+ `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`, beta) ile her etkileşim/model-çağrısı/tool-çağrısı span'i. `claude_code.llm_request` span'i **model adı, gecikme, token sayıları**nı attribute olarak taşıyor — model-düşümü tespiti için doğrudan kullanılabilir alan. Kaynak: https://code.claude.com/docs/en/agent-sdk/observability (doğrudan açıldı/okundu)
- **D-5:** Kurulum: yalnız env değişkeni (`CLAUDE_CODE_ENABLE_TELEMETRY=1` + exporter seçimi) ama **veriyi almak için bir OTLP-uyumlu backend/collector gerekir** (Honeycomb, Datadog, Grafana, self-hosted collector); `console` exporter SDK üzerinden kullanılamıyor (mesaj kanalıyla çakışıyor). Traces hâlâ BETA — span adı/attribute'lar sürümler arası değişebilir uyarısı resmî dokümanda açıkça var. v2.1.179+ gerekli. Aynı kaynak.

### Yol (iii) — ccusage-sınıfı hazır araç

- **D-6:** ccusage, Claude Code (ve benzeri ajan CLI'ları) için yerel JSONL verisini okuyup token/model/maliyet raporu (günlük/haftalık/aylık/oturum) üreten açık-kaynak topluluk aracı; kurulumsuz `npx ccusage@latest` ile çalışıyor; depo aktif bakımlı (1700+ commit, açık issue/PR trafiği, sponsorlu). Kaynak: https://github.com/ryoppippi/ccusage (doğrudan açıldı/okundu)
- **K-7:** ccusage **de aynı iç JSONL dosyalarını okuyor** — yani Yol (i)'in kırılganlığını devralıyor, ortadan kaldırmıyor. Destekleyici kaynak (başlık/açıklama düzeyinde, tam kod incelenmedi): https://github.com/aarora79/claude-code-usage-analyzer ("raw token usage data ... .jsonl files")
- **X-8:** ccusage'de otomatik model-düşümü/degradation ALARM özelliği bulunamadı — model bazlı ayrım var ama "düşüm tespiti" adında bir mekanizmaya dair kanıt yok (fetch edilen içerikte geçmiyor; yokluk kanıtı zayıf, ileri sürülemez sadece "görülmedi" denebilir). Kaynak: aynı D-6.
- **npm sayfası (npmjs.com/package/ccusage) 403 döndü, açılamadı** — bu kaynak KULLANILMADI (F3/F5 gereği URL açılmadan künye yazılmaz).

## Jarvis'e uygulanabilirlik — 3 yol × 4 eksen kıyas tablosu

| Eksen | (i) JSONL-parse | (ii) OTLP-telemetri | (iii) ccusage-sınıfı |
|---|---|---|---|
| **Kurulum maliyeti** | Düşük — dış bağımlılık yok, dosyalar zaten diskte, `tools/kosum-maliyeti.py` zaten YAZILI ve 08-02'de elle koşuldu | Orta-Yüksek — env değişkeni ile açmak kolay ama veriyi görmek için OTLP-uyumlu bir backend/collector kurmak/işletmek gerekir | En düşük — `npx ccusage@latest`, kurulum/hesap yok |
| **Veri zenginliği** | Yüksek — tam konuşma+tool-call geçmişi, model+token her kayıtta (iç format) | Orta-Yüksek — resmî sayaçlar (token/cost/session/LOC/tool-decision) + beta trace'lerde model/gecikme/token per-request | Orta — hazır günlük/haftalık/aylık/oturum raporu, model bazlı ama Jarvis'e özel alan (KB-27 vb.) yok |
| **Kırılganlık** | Yüksek — resmen "internal, sürümler arası değişir" (D-1) + somut regresyon örneği (D-2) | Düşük — resmî desteklenen OTLP arayüzü, sürüm gereksinimi belgeli; ancak Trace'ler BETA (span/attribute değişebilir) | Yüksek (dolaylı) — altta aynı kırılgan JSONL'e bağımlı + üçüncü-parti bakım riski (topluluk projesi) |
| **Model-düşümü yakalar mı** | Evet — her kayıtta model adı var (08-02 koşumunda zaten çıkarıldı) | Evet, açıkça — `llm_request` span'i model adını attribute olarak taşır, resmî belgeli | Kısmen — model bazlı rapor var, otomatik "düşüm" tespiti/alarm görülmedi (X-8) |

## Öneri (hazırı-temel-al süzgeciyle, gerekçeli)

**JSONL-parse yolunu SÜRDÜR (Yol i) — zaten kurulu, KB-13(5)/KB-27 bu karara bağlı, m.6 "hazırı temel al" ilkesi sıfırdan yeni yol açmayı zaten yasaklıyor.** Buna karşı iki hafif sertleştirme eklenmeli:

1. **Şema-kırılganlık freni:** parse eden script (`tools/kosum-maliyeti.py` ve türevleri) her koşumda beklenmeyen kayıt tipi/alan eksikliğinde SESSİZCE yanlış sayı üretmek yerine FAIL-LOUD uyarı versin (D-1 + D-2'nin gösterdiği somut risk: bir sürüm transkripti hiç yazmayabilir).
2. **Resmî çapraz-doğrulama:** ara sıra (ör. haftalık örneklem) Anthropic'in kendi önerdiği "script interface" olan `claude -p --output-format json` çıktısındaki `usage`/`cost` alanlarıyla JSONL-türetilmiş sayıları karşılaştır — bu, format kırıldığında sessiz sapmayı yakalar.

**OTLP (Yol ii)** teknik olarak en sağlam/resmî yol ama kurulum bedeli (bir collector/backend işletmek) tek-kullanıcı yerel senaryoda kazanımı aşıyor; Jarvis çok-oturumlu/gerçek-zamanlı izleme ihtiyacı doğarsa (ör. çoklu paralel-oturum canlı panosu) yeniden ele alınacak **aday** olarak not düşülsün — o zaman zaten mevcut sürüm şartı v2.1.179+ kontrol edilmeli.

**ccusage-sınıfı (Yol iii)** backbone olarak ÖNERİLMİYOR — aynı kırılgan JSONL'e bağımlı olduğu için risk azaltmıyor, üstüne üçüncü-parti bakım yüzeyi ekliyor. Opsiyonel hızlı-bakış/çapraz-kontrol aracı olarak (`npx ccusage@latest` ile ara sıra elle sağlama) kullanılabilir, ama KB-27 tavan-rejimi gibi Jarvis'e özgü mantık üstüne inşa edilecek temel OLMAMALI.

## F2 Destek Tablosu

| İddia | Dayandığı kaynak | Etiket |
|---|---|---|
| JSONL formatı internal, sürümler arası değişir | code.claude.com/docs/en/sessions | D |
| 2.1.169 regresyonu: transkript stub-only yazıldı | github.com/anthropics/claude-code/issues/66486 | D |
| Resmî script-interface alternatifleri var (`claude -p --output-format json`, hook `transcript_path`) | code.claude.com/docs/en/sessions | D |
| OTLP metrics/traces/logs yerleşik, `llm_request` span model+token+gecikme taşır | code.claude.com/docs/en/agent-sdk/observability | D |
| OTLP kurulumu env-var + backend gerektirir, Trace beta | code.claude.com/docs/en/agent-sdk/observability | D |
| ccusage yerel JSONL okur, model/token/maliyet raporu üretir, aktif bakımlı | github.com/ryoppippi/ccusage | D |
| ccusage da aynı JSONL'e bağımlı (kırılganlığı devralır) | github.com/aarora79/claude-code-usage-analyzer (başlık/açıklama düzeyi) | K |
| ccusage'de otomatik model-düşümü alarmı görülmedi | github.com/ryoppippi/ccusage (fetch içeriğinde yok) | X (yokluk kanıtı zayıf) |

## Cevaplanamayanlar

- ccusage'in (ve benzerlerinin) hangi Claude Code sürümlerine kadar test edildiği / format kırılmalarını ne sıklıkla takip ettiği — npm sayfası 403 verdi, GitHub repo içi CHANGELOG/issue geçmişi bu kısa atlasın kapsamı dışında derinlemesine taranmadı.
- OTLP metrics'in tam alan listesi (`/docs/en/monitoring-usage` referans sayfası) bu koşumda AÇILMADI — yalnız `agent-sdk/observability` sayfasındaki özet kullanıldı; tam metrik/attribute listesi gerekirse ayrı bir kısa iz sürülmeli.
