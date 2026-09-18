# TEZ — Aile D: Ajan Sınıfları ve Model Katmanlaması

**Rol:** Atlas TEZ araştırmacısı · **AS-OF:** 2026-09-18 · **Kapsam:** subagent vs persistent agent, tutor ajanı, model katmanlaması

## 1. Kaynak Listesi

| # | URL | Yayın tarihi | Çekim tarihi | Açıldı mı | Model/kuşak | Kullanım biçimi |
|---|---|---|---|---|---|---|
| 1 | https://code.claude.com/docs/en/sub-agents | sürekli güncellenen resmi belge, v2.1.257+ referansı | 2026-09-18 | EVET (WebFetch) | Claude Code — Sonnet 5 / Opus 5 / Haiku 4.5 / Fable (alias sistemi) | üretim (resmi ürün belgesi) |
| 2 | https://www.anthropic.com/engineering/multi-agent-research-system | Anthropic mühendislik blogu (orijinal yayın 2025 ortası, içerik Claude Opus 4 / Sonnet 4 dönemine ait — ESKİ KUŞAK) | 2026-09-18 | EVET (WebFetch) | Claude Opus 4 (lead) + Sonnet 4 (subagent) — **eski kuşak, "o zaman böyle" notu** | üretim (Anthropic'in kendi araştırma ürünü) |
| 3 | https://arxiv.org/pdf/2606.30306 (Always-On Agents: A Survey of Persistent Memory, State, and Governance in LLM Agents, Ding ve ark.) | 2026-06-30 | 2026-09-18 | KISMEN (WebFetch yalnız metadata/başlık yapısını döndürdü, gövde metni çekilemedi) | model-agnostik akademik taksonomi | akademik derleme |
| 4 | https://mem0.ai/blog/build-a-personalized-ai-tutor-with-persistent-memory | tarih belirtilmemiş, 2026 içeriği | 2026-09-18 | HAYIR (yalnız WebSearch özeti) | model-agnostik (Mem0 altyapısı) | pratisyen/ürün blogu |
| 5 | https://arxiv.org/html/2604.26962v1 (DeepTutor: Towards Agentic Personalized Tutoring) | 2026-04 | 2026-09-18 | HAYIR (yalnız WebSearch özeti) | model-agnostik, TutorBench ile değerlendirilmiş | akademik/deneysel |
| 6 | https://github.com/HKUDS/DeepTutor | 2026 | 2026-09-18 | HAYIR (yalnız WebSearch özeti) | model-agnostik | açık kaynak deney |
| 7 | https://www.morphllm.com/claude-code-models | 2026-09 (başlıkta "September 2026") | 2026-09-18 | HAYIR (yalnız WebSearch özeti) | Sonnet 5 / Opus 5 / Haiku 4.5 / Fable 5.1 — **güncel kuşak** | pratisyen karşılaştırma yazısı |
| 8 | HN iş parçacığı (30 Temmuz 2026, morphllm üzerinden alıntı) | 2026-07-30 | 2026-09-18 | HAYIR (ikincil alıntı) | Opus (planlama) + Sonnet 5 (kodlama, max effort) — güncel kuşak | pratisyen anekdot |
| 9 | https://www.mindstudio.ai/blog/what-is-claude-agent-sdk-vs-claude-api | 2026 | 2026-09-18 | HAYIR (yalnız WebSearch özeti) | Claude Agent SDK genel | pratisyen rehber |
| 10 | https://academy.claude.com/courses/claude-code-101/subagents | 2026 | 2026-09-18 | HAYIR (yalnız WebSearch özeti) | Claude Code resmi eğitim | üretim/eğitim materyali |

**Not:** Kota gereği ≥2 birincil kaynak WebFetch ile gerçekten açıldı (#1, #2); #3 kısmen açıldı ama gövde metni PDF ayrıştırma sınırı nedeniyle alınamadı — yalnız başlık/tarih/bölüm iskeleti doğrulandı, taksonomi içeriği İDDİA LİSTESİ'ne düşürülmedi, "bulunamadı" olarak işaretlendi.

## 2. Alt-Ajan vs Kalıcı Ajan Ayrım Tablosu (Claude Code temelli, kaynak #1)

| Boyut | Alt-ajan (subagent, `isolation` yok/worktree) | Kalıcı ajan (persistent, `memory` alanlı) | Kaynak |
|---|---|---|---|
| **Hafıza** | Yok varsayılan; her çağrı "fresh, isolated context window" — önceki konuşmayı, zaten çağrılmış skill'leri, okunmuş dosyaları görmez | `memory: user/project/local` alanı → kalıcı dizin (`~/.claude/agent-memory/<ad>/` vb.); `MEMORY.md`'nin ilk 200 satırı/25KB'ı her çağrıda sistem promptuna otomatik enjekte edilir | #1 |
| **Kimlik** | Adlandırılmış tanım dosyası var ama oturumlar arası "instance" sürekliliği yok — her çağrı yeni örnek (resume özelliğiyle konuşma geçmişi tutulabilir, istisna) | Aynı adlandırılmış tanım + kendi kalıcı bilgi deposu; zamanla "codebase patterns, debugging insights, architectural decisions" biriktirir | #1 |
| **Yetki (araç/dosya izni)** | `tools`/`disallowedTools` allowlist-denylist; MCP sunucu düzeyinde desen (`mcp__<server>`); arka planda koşan alt-ajanlar için ayrı, daha dar araç seti | Bellek etkinken ek olarak Read/Write/Edit otomatik açılır (kendi `MEMORY.md`'sini düzenleyebilmesi için) | #1 |
| **Oturum/süreç** | Ana konuşmanın cwd'sinde başlar; `cd` çağrılar arası kalıcı değil; `isolation: worktree` ile tam izole kopya çalışma dizini | Bellek dizini kalıcı olsa da çalışma süreci yine ana konuşmanın açtığı çağrı ömrüyle sınırlı — "persistent" olan dizin, süreç değil | #1 |
| **Maliyet** | "Control costs by routing tasks to faster, cheaper models like Haiku"; yüksek hacimli çıktı (test/log) ana bağlamdan izole edilerek token tasarrufu | Bellek maliyeti: her çağrıda MEMORY.md'nin (≤200 satır/25KB) sistem promptuna eklenmesi → sabit ek token yükü, ama tekrar keşif maliyetini azaltabilir (doğrudan ölçüm kaynakta yok — [?]) | #1 |

## 3. Tutor/Öğretim Ajanı Vakaları

- **DeepTutor** (arXiv 2604.26962, 2026-04): "Tutoring is an inherently longitudinal endeavor that spans weeks or months and benefits from an evolving model of the individual learner, a requirement that existing agentic frameworks do not directly address." Gerekçe: öğrenme haftalar/aylar süren bir süreç, tek-seferlik icra ajanının ephemeral (geçici) bağlamı bunu karşılamıyor; kalıcı öğrenci modeli (learner memory) gerekli. Dinamik öğrenci belleği + TutorBench ile değerlendirme. (WebSearch özeti, birincil açılmadı — [?] işaretli detaylar)
- **Mem0 tutor blogu:** "agent_id separates memory by subject within the same student profile, eliminating cross-contamination between, say, math and CS tutoring" — konuya göre ayrı bellek alt-bölmeleri, tek öğrenci profili içinde. Gerekçe pedagojik izolasyon (konular arası karışmayı önleme), icra ajanından ayrılık gerekçesi doğrudan alıntılanmadı — [?].
- **Prosedürel bellek notu (Mem0 blogu):** "the agent rewrites its own instructions based on what teaching strategies have worked" — öğretim ajanının kendi sistem promptunu zamanla güncellemesi; icra ajanlarında (Claude Code subagent) bu doğrudan karşılığı `MEMORY.md` kürasyonu (#1) ile yapısal olarak benzer ama farklı ürün.
- Claude Code resmi belgesinde (#1) "tutor" veya "öğretim" adlı özel bir ajan sınıfı YOK; bulgu bu spesifik iddiaya destek sağlamıyor — genel `memory` alanı herhangi bir role (tutor dahil) uygulanabilir bir mekanizma, tutor'a özgü tasarım değil.

## 4. Model Katmanlaması Bulguları

| Kim | Gerekçe | AS-OF | Model | Kuşak |
|---|---|---|---|---|
| Anthropic (multi-agent research system) | "a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2%" — kalite; ayrıca "upgrading to Claude Sonnet 4 is a larger performance gain than doubling the token budget on Claude Sonnet 3.7" — model kalitesi token bütçesinden daha verimli | orijinal yayın ~2025-Q3 (Opus 4/Sonnet 4 dönemi) | Opus 4 (lider) + Sonnet 4 (işçi) | **ESKİ KUŞAK** — bugünün (2026-09) Opus 5/Sonnet 5 hattından önce |
| Claude Code resmi belge | "Control costs by routing tasks to faster, cheaper models like Haiku"; Explore ajanı "capped at Opus on the Claude API, so Explore never runs on a more expensive model than the one you already chose" — maliyet tavanı mekanizması | 2026-09-18 (belge v2.1.257+ referanslı) | alias sistemi: sonnet/opus/haiku/fable | **GÜNCEL KUŞAK** |
| morphllm pratisyen yazısı | "Haiku 4.5 is the fast/cheap tier... You almost never want Haiku as your main session model — you want it as the model your subagents run on while your main session stays on something heavier" — gecikme + maliyet; hacimli/mekanik fan-out işlerine uygun | 2026-09 | Haiku 4.5 (işçi) vs ana oturum (ağırlığı belirtilmeyen "heavier") | GÜNCEL KUŞAK |
| HN pratisyen anekdotu | "Claude Opus for planning at high effort and Claude Sonnet 5 for coding at max effort" — planlama/karar için en güçlü model, icra için orta model | 2026-07-30 | Opus (plan) + Sonnet 5 (kod) | GÜNCEL KUŞAK |
| Genel pratik özeti (Google ADK bağlamında, ikincil kaynak) | "use a fast, cheap model... for triage and routing agents, and a more capable model... for complex reasoning agents" | 2026 (tarih belirsiz — [?]) | GPT-5.4-mini/Claude Haiku 4.5 (triyaj) + GPT-5.4/Claude Sonnet 4.6 (karmaşık akıl yürütme) | karışık — Sonnet 4.6 referansı eski/orta kuşak izlenimi veriyor, doğrulanmadı [?] |

**Orta model (Opus sınıfı) kalıcı LİDER ajan olarak seçilmesine kanıt:** #2 kaynağındaki Opus-lider + Sonnet-işçi düzeni doğrudan destekler (kalite: %90.2 iyileşme), ancak bu ESKİ KUŞAK (Opus 4/Sonnet 4) veridir ve "lider = en pahalı/en güçlü model" örüntüsüdür — "orta model" (bugünün Opus 5'i "en güçlü" değil, Fable üstte olabilir; fiyatlandırma tablosunda Fable 5 > Opus 4.8 > Sonnet 5 > Haiku 4.5 sıralaması bulundu, kaynak morphllm) ifadesiyle tam örtüşmüyor — güncel kuşakta hangi modelin "en güçlü" olduğu ayrı doğrulama gerektirir. **Çürüten/sınırlayan kanıt:** doğrudan "Opus sınıfının kalıcı lider olarak seçilmesi yanlıştır" diyen bir kaynak bulunamadı; morphllm pratisyen notu Haiku'nun asla ana oturum modeli olmaması gerektiğini söylüyor (dolaylı destek: lider daha güçlü model olmalı, ama "Opus" adını anmıyor).

## 5. İDDİA LİSTESİ (gerekçesiz, numaralı)

1. Claude Code'da subagent'lar varsayılan olarak oturumlar arası hafızasızdır; her çağrı taze bağlamla başlar.
2. Claude Code'da `memory: user/project/local` alanı subagent'a kalıcı, adına özel bir dizin ve `MEMORY.md` dosyası verir.
3. `MEMORY.md`'nin yalnız ilk 200 satırı veya 25KB'ı (hangisi önce gelirse) sistem promptuna otomatik eklenir.
4. Bellek etkin subagent'larda Read/Write/Edit araçları otomatik açılır.
5. Subagent bellek dizinleri ajan-başınadır; farklı subagent'lar birbirinin `MEMORY.md`'sini görmez.
6. Claude Code'da model seçimi çözümleme sırası: çağrı-parametresi > subagent tanımındaki `model` alanı > `CLAUDE_CODE_SUBAGENT_MODEL` ortam değişkeni > ana konuşmanın modeli.
7. Anthropic'in kendi çok-ajanlı araştırma sisteminde (Opus 4 lider + Sonnet 4 işçi, eski kuşak) tek-ajanlı Opus 4'e göre %90.2 performans artışı ölçüldü.
8. Aynı kaynakta Sonnet 4'e yükseltmenin, Sonnet 3.7 üzerinde token bütçesini iki katına çıkarmaktan daha büyük performans kazancı sağladığı bildirildi.
9. Çok-ajanlı sistemler tek sohbete göre yaklaşık 15 kat, tek-ajanlı sohbete göre bir ajan yaklaşık 4 kat daha fazla token tüketir (Anthropic kaynağı).
10. DeepTutor (2026-04) öğretimi haftalar/aylar süren, kalıcı öğrenci modeli gerektiren bir süreç olarak çerçeveliyor ve mevcut ajan çerçevelerinin bunu doğrudan karşılamadığını iddia ediyor.
11. Claude Code resmi belgesinde tutor/öğretim'e özgü ayrı bir ajan sınıfı tanımlanmamıştır; `memory` mekanizması role-agnostiktir.
12. "Always-On Agents" akademik derlemesinin (2026-06-30) gövde metni bu oturumda çekilemedi; taksonomi içeriği doğrulanamadı, yalnız başlık ve yayın tarihi doğrulandı.

---

**Dönüş özeti için:** kaynak sayısı 10, WebFetch ile gerçekten açılan 2 (kısmi 3.), İDDİA LİSTESİ yukarıda 12 madde.
