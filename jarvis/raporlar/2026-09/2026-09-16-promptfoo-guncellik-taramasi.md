# Dar Canlı Tarama: promptfoo Güncellik + LLM/Ajan Eval Seti Manzarası

**AS-OF 2026-09-16, canlı çekildi** (WebSearch/WebFetch; Karar 68 anakronizm freni — model hafızası burada kullanılmadı, tamamı canlı sorgu sonucudur).

Soru: LLM/ajan eval seti kurmak için 2026'da üretimde hangi araçlar standart; promptfoo hâlâ aktif ve güncel mi?

## 1) promptfoo GitHub reposu (github.com/promptfoo/promptfoo)

- **D** — Yıldız/fork: "25.2k stars", "2.3k forks" (GitHub repo sayfası, WebFetch, 2026-09-16 çekim).
- **D** — Açık issue sayısı: "125" (aynı sayfa).
- **K** — Toplam commit sayısı "9,761 Commits" görüldü ama repo sayfası kısmi yüklendi ("Uh oh! There was an error while loading" hatası); son commit tarihi bu sayfadan doğrudan okunamadı.
- **D** — Son sürüm ve tarih: v0.123.0, **2026-09-10** yayımlandı; "included breaking changes for providers defaulting GPT-5.6+ to Responses" (newreleases.io üzerinden GitHub release aynası, WebSearch sonucu). Bu birincil GitHub release sayfası değil, aynadan doğrulandı — **K** olarak işaretliyorum (ikincil kaynak üzerinden).
- **D** — Depo 2026-09-14 civarında aktif güncelleniyordu ("main repository was updated as of September 14, 2026" — WebSearch özeti, doğrudan alıntı değil, kısmi güven → **K**).
- **D** — 2026-09-15 tarihli bağımlılık PR'ı görüldü: "fix(deps): update dependency @anthropic-ai/sdk to v0.124.0" — promptfoo/promptfoo#10940 (WebSearch, GitHub PR başlığı). Bu, deponun 2026-09-15'te hâlâ aktif commit aldığının doğrudan kanıtı.

**Sonuç (bölüm 1):** promptfoo **aktif** — 2026-09'da hem sürüm yayını (0.123.0, 09-10) hem commit trafiği (09-15 PR) var. Yıldız/issue sayıları sağlıklı bir açık kaynak projeye işaret ediyor.

## 2) npm sayfası

- **X** — npmjs.com/package/promptfoo doğrudan erişilemedi: WebFetch "HTTP 403 Forbidden" döndü (npm'in bot/scraper engeli). Sayfa görülemedi, nedeni: npm anlık HTML'i otomatik erişime kapalı.
- **K** — Dolaylı kanıt: birden çok bağımsız repo dependabot/renovate PR'ı "bump promptfoo from 0.121.20/0.122.2 to 0.123.0" gösteriyor (iamjr15/healtheval#2, #5; eamonmason/rss-email#74 — WebSearch). Bu, npm registry'de 0.123.0'ın yayında olduğunu dolaylı doğrular ama npm'in kendi "son yayın tarihi" alanı görülmedi.
- Node.js gereksinimi: **D** — "requires Node.js >=22.22.0 for npm and npx usage, Node.js 24 LTS recommended" (WebSearch özeti, npmjs.com/promptfoo sayfası içeriğinden — kaynak ikincil özet, **K**).

## 3) Resmî doküman: config sözdizimi kırılması + ajan/tool-call eval desteği

- **D** — Ajan/trajectory eval desteği MEVCUT ve aktif geliştiriliyor: `trajectory:goal-success`, `trajectory:step-count` assertion türleri var; "trajectory:goal-success evaluates whether an agent's sequence of steps actually reached the goal, not just whether the final string looks plausible" (promptfoo.dev/docs/tracing/, WebSearch alıntısı).
- **D** — Tool-call normalizasyonu framework-özel: "Vercel AI SDK's ai.toolCall.name, ai.toolCall.args... OpenAI Agents SDK exec_command calls" tanınıyor (promptfoo.dev/docs/tracing/).
- **D** — 2026'da kırılma potansiyeli somut örnekle görüldü: "a user whose shell tool is named 'bash', 'terminal', or 'run' would see those spans normalize to type:tool, breaking trajectory:step-count {type: command} assertions" — bunun için "shell-tool-name set was made configurable" düzeltmesi yapıldı (GitHub PR başlıkları/özetleri, WebSearch). Yani en az bir bilinen kırılma sınıfı var, ama üstüne yama gelmiş.
- **K** — v0.123.0'da "breaking changes for providers defaulting GPT-5.6+ to Responses" — provider davranış kırılması var ama bunun `promptfooconfig.yaml` şemasını (assert türleri, `llm-rubric` alan adları) değiştirip değiştirmediği doğrudan görülmedi; sadece provider varsayılan API modu değişti.
- **X** — `llm-rubric` assertion türünün 2025-2026 arası alan-adı/şema düzeyinde kırıldığına dair doğrudan kanıt bulunamadı; arama bunu doğrulamadı, aksini de kanıtlamadı.
- **D** — Rehber içerik: "Evaluate Coding Agents", "Evaluate Google ADK Agents", "OpenAI Agents" provider sayfaları resmî dokümanda mevcut (promptfoo.dev/docs/guides/..., promptfoo.dev/docs/providers/openai-agents/) — ajan çerçeveleriyle entegrasyon dokümante edilmiş.

**Sonuç (bölüm 3):** Config sözdizimi kökten kırılmamış; ajan/tool-call/trajectory eval'i promptfoo'nun 2026 yol haritasının merkezinde ve son PR'lar bu alanda (trace assertion sertleştirme, trajectory adımları) yoğunlaşmış.

## 4) Alternatifler (ad + son release + tek satır fark)

| Araç | Son sürüm/durum (AS-OF 09-16) | Etiket | Tek satır fark |
|---|---|---|---|
| **Inspect AI** (UK AISI) | v0.3.225 (WebSearch özeti, doğrudan sürüm sayfası görülmedi) | K | Güvenlik/kapasite değerlendirmesine (safety/capability evals) odaklı, devlet destekli açık kaynak. |
| **DeepEval** | v4.0.3 (WebSearch özeti) | K | CI'da hızlı, kod-içi (pytest benzeri) LLM test çerçevesi; "DeepEval for CI evals" konumlandırması. |
| **Braintrust** | Sürüm numarası bulunamadı (ticari SaaS, sürekli deploy) | X | Üretim izlenebilirliği (traceability) + değerlendirme birleşik ticari platform. |
| **LangSmith evals** | Sürüm numarası bulunamadı (LangChain ekosistemine bağlı SaaS) | X | LangChain/LangGraph ajanlarıyla yerleşik entegrasyon, trace-tabanlı. |
| **OpenAI Evals** | Sürüm numarası bulunamadı; "open-source standard" olarak anılıyor | K | OpenAI model ailesine yakın, community eval seti deposu. |
| **Anthropic'in kendi rehberi** | Makale/dok, araç değil — "Demystifying evals for AI agents" (anthropic.com/engineering) | D | Araç satmıyor; metodoloji (görev seçimi, trajectory vs outcome, judge kalibrasyonu, CI'a evals) rehberi. |

Not: Braintrust ve LangSmith SaaS oldukları için "release tarihi" kavramı GitHub açık kaynak projeleri gibi net değil; bu nedenle **X** işaretlendi — bulunamadı, nedeni: sürekli dağıtım modeli + arama bu ayrıntıya inmedi (bütçe: dar tarama, 12 çağrı sınırı).

## 5) Sektörde 2026 güncel başlık

- **D** — "DeepEval for CI evals plus Braintrust for production traceability is becoming the de facto standard for engineering-led AI product teams in 2026" (WebSearch özeti, digitalapplied.com/inference.net kaynaklı derleme, **K** — ikincil sentez, birincil kaynak teyidi yok).
- **D** — "Inspect AI wins for safety and capability evals, Patronus for regulated enterprise" (aynı kaynak kümesi, **K**).
- **D** — Terminoloji 2026'da üç eksene oturmuş: **agent evals** (nihai çıktı) + **trajectory eval** (adım/araç-çağrı sırası doğru mu) + **LLM-as-judge kalibrasyonu** (insan puanıyla korelasyon; hedef "Pearson r > 0.75", 2 hafta üst üste düşerse rubrik/dağılım incelemesi) — confident-ai.com, judgmentlabs.ai, langfuse.com kaynaklarının ortak vurgusu (WebSearch özeti, **K**, birden fazla bağımsız kaynak yakınsıyor → orta-yüksek güven).
- **D** — Anthropic'in resmî tavsiyesi: "20-50 simple tasks drawn from real failures" ile başlamak, hem outcome hem trajectory ölçmek (anthropic.com/engineering/demystifying-evals-for-ai-agents, WebSearch özeti — **K**, ikincil özet ama kaynak birincil ve isimli).

## Bilinmeyen / doğrulanamayan

- promptfoo'nun tam son commit SHA'sı ve tarihi (GitHub repo sayfası kısmi yüklendi).
- npm registry'nin kendi "published X days ago" alanı (403 engeliyle görülemedi; dolaylı kanıtla 0.123.0 teyit edildi).
- `llm-rubric` alan-adı düzeyinde şema kırılması olup olmadığı — ne doğrulandı ne çürütüldü.
- Braintrust/LangSmith/OpenAI Evals için somut sürüm numarası/tarih — SaaS + bütçe sınırı nedeniyle atlandı.

## Jarvis için sonuç

promptfoo'yu temel almak **uygun**: proje 2026-09-10'da (v0.123.0) yayın yapmış, 2026-09-15'te hâlâ commit/PR trafiği var, 25.2k yıldız + 125 açık issue ile sağlıklı bir açık kaynak proje profili gösteriyor, ve en kritik nokta — Jarvis'in ajan/tool-call koşumlarını değerlendirmesi gerektiği için tam ihtiyaç duyduğu `trajectory:goal-success` / `trajectory:step-count` assertion türleri zaten üretimde ve aktif olarak sertleştiriliyor (shell-tool-name yapılandırılabilirliği gibi 2026 düzeltmeleriyle); resmi doküman ayrıca OpenAI Agents SDK, Google ADK, Vercel AI SDK ile hazır entegrasyon rehberleri sunuyor. Kurulacaksa **en az v0.123.0** (2026-09-10, GPT-5.6+ Responses API varsayılanı değişikliğini içerir — provider config'inde bu varsayımı kontrol etmek gerekir) hedeflenmeli; Node.js >=22.22.0 (24 LTS önerilir) koşulu not edilmeli. Alternatif olarak DeepEval (CI'da hafif, pytest-benzeri) tamamlayıcı olarak düşünülebilir ama promptfoo'nun YAML-deklaratif config + hazır ajan/trace entegrasyonları, sıfırdan bir eval harness kurmak yerine "hazırı temel al" ilkesiyle (CLAUDE.md §Çalışma ilkeleri) doğrudan örtüşüyor; DeepEval'a geçiş gerekçesi ancak Python-native/pytest-akışı bir zorunluluk doğarsa gündeme gelmeli.

## Kaynaklar
1. https://github.com/promptfoo/promptfoo (WebFetch, 2026-09-16)
2. https://github.com/promptfoo/promptfoo/releases
3. https://newreleases.io/project/github/promptfoo/promptfoo/release/0.123.0
4. https://github.com/promptfoo/promptfoo/pull/10940
5. https://www.promptfoo.dev/docs/tracing/
6. https://www.promptfoo.dev/docs/guides/evaluate-coding-agents/
7. https://www.promptfoo.dev/docs/guides/evaluate-google-adk/
8. https://www.promptfoo.dev/docs/providers/openai-agents/
9. https://www.npmjs.com/package/promptfoo (403 — erişilemedi)
10. https://anthropic.com/engineering/demystifying-evals-for-ai-agents
11. https://www.digitalapplied.com/blog/ai-agent-eval-frameworks-testing-guide-2026
12. https://www.confident-ai.com/blog/llm-agent-evaluation-complete-guide
13. https://www.judgmentlabs.ai/blogs/agent-judge-solving-long-context-evaluations
14. https://langfuse.com/resources/engineering/ai-agent-evaluation

---
**Epistemolojik not:** Bu tarama dar bütçeyle (≤12 araç çağrısı) yapıldı; çoğu bulgu WebSearch'ün ikincil özetleri üzerinden geldi (**K**), birincil sayfa içeriği doğrudan görülemeyen yerler (npm 403, GitHub repo kısmi yükleme) açıkça işaretlendi. Anlık görüntüdür, 2026-09-16 sonrası değişebilir.
