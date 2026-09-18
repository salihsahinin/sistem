# Atlas TEZ — Aile B: Pratisyen Sistemler (Kun Chen / firstmate sınıfı çok-ajan orkestratörleri)

**Tarih:** 2026-09-18 (AS-OF tüm çekimler bu tarih)
**Rol:** TEZ araştırmacısı, perspektif-ajan-sınırı sorusu
**Kapsam notu:** Firstmate/secondmate/crewmate'in kendi AGENTS.md gerekçeleri yeniden taranmadı; yalnız DIŞ pratisyen kaynaklar.

---

## 1. Kaynak Listesi

| # | URL | Yayın tarihi | Çekim (AS-OF) | Açıldı mı | Model/kuşak | Kullanım biçimi |
|---|-----|--------------|----------------|-----------|--------------|-------------------|
| K1 | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | 2026-09-18 | **Evet (WebFetch)** | Claude Opus 4 (lider) + Claude Sonnet 4 (işçi) — 2025-Q2 kuşağı, eski kuşak (4.x, güncel-kuşak eşiğinin altında ama yakın) | Üretim (Claude'un araştırma özelliği) |
| K2 | https://cognition.com/blog/dont-build-multi-agents | 2025-06-12 | 2026-09-18 | **Evet (WebFetch)** | Devin'in kendi modeli belirtilmemiş; anlatı model-bağımsız mimari dersi | Üretim (Devin, gerçek müşteri kullanımı) |
| K3 | https://code.claude.com/docs/en/sub-agents | Sürekli güncellenen resmî doküman, tarih damgasız | 2026-09-18 | **Evet (WebFetch)** | Model alias listesinde `claude-opus-5`, `claude-sonnet-5`, `fable` görülüyor → **güncel kuşak** (2026-09 dönemi doküman) | Üretim (Claude Code CLI, canlı ürün özelliği) |
| K4 | https://arxiv.org/html/2308.00352v6 (MetaGPT) | İlk 2023-08, v6 revizyonu tarihsiz görüldü | 2026-09-18 | Hayır — yalnız WebSearch sentezi | Orijinal makale eski kuşak (GPT-4 çağı, 2023); pratikteki güncel kullanımı doğrulanmadı | Akademik + açık kaynak proje (pypi `metagpt`) — **kuşak damgası belirsiz, [?]** |
| K5 | AG2 (AutoGen fork) blog/dokümanları — docs.ag2.ai, ag2.ai/blog/beyond-autogen | Blog 2025 içinde (tam gün belirsiz) | 2026-09-18 | Hayır — yalnız WebSearch sentezi | Model-bağımsız çerçeve dokümanı | Açık kaynak framework, pratisyen kullanımı yaygın |
| K6 | Supervisor-Worker desen yazısı — akmalkhaniub.github.io/blog/supervisor-worker-agent-patterns-langgraph.html | Tarihsiz blog | 2026-09-18 | Hayır — yalnız WebSearch sentezi | Belirtilmemiş | Pratisyen blog, üretim iddiası var ama doğrulanmadı |
| K7 | OpenHands Software Agent SDK — arxiv.org/pdf/2511.03690 | 2025-11 | 2026-09-18 | Hayır — yalnız WebSearch sentezi | Güncel kuşak (2025-Q4 SDK) | Üretim SDK dokümantasyonu (akademik makale biçiminde yayımlanmış) |
| K8 | Microsoft AutoGen bakım moduna alınması — Spheron/dev.to karşılaştırma yazıları (2026 tarihli) | 2026 (Ekim 2025 olayını anlatıyor) | 2026-09-18 | Hayır — yalnız WebSearch sentezi | Kurumsal duyuru, model bağımsız | İkincil kaynak (haber/blog özeti), birincil Microsoft duyurusu açılmadı |
| K9 | Eğitim/tutor çok-ajan anketleri — techrxiv.org/doi/pdf/10.36227/techrxiv.176704820.01980102 ve ilişkili arXiv makaleleri (2508.19611, 2605.14266 vb.) | 2025-08 ile 2026-06 arası çeşitli | 2026-09-18 | Hayır — yalnız WebSearch sentezi | Akademik, üretim değil | **Not: bunlar akademik makale, "pratisyen" tanımına tam uymuyor — İDDİA 9'da işaretlendi** |

**403/paywall:** Yok — erişilemeyen kaynak rastlanmadı, ancak K4-K9 zaman kısıtı nedeniyle WebFetch ile açılmadı, yalnız arama motoru sentezine dayanıyor (düşük güven).

---

## 2. Bulgu Tablosu: Perspektif × Ayrı mı × Gerekçe × Kaynak × AS-OF × Kuşak

| Perspektif | Ayrı ajan/bağlam mı? | Gerekçe (verilen) | Kaynak | AS-OF | Kuşak |
|---|---|---|---|---|---|
| **İcra (worker/subagent)** | Evet, paralel ayrı bağlam pencereleri | "Subagents facilitate compression by operating in parallel with their own context windows" — sıkıştırma + paralellik | K1 | 2026-09-18 | Eski kuşak (Sonnet 4, 2025-06) |
| **Planlama/orkestrasyon (lead agent)** | Evet, tek lider ayrı rol | Lider "coordinates the process while delegating to specialized subagents"; plan hafızaya yazılır çünkü 200K token'ı aşınca bağlam kırpılır | K1 | 2026-09-18 | Eski kuşak |
| **Hakem/reviewer (QA)** | Evet, ayrı ajan | MetaGPT: QA mühendisi rolü kod yazan mühendisten ayrı; "generates unit test code and reviews code to identify and fix any bugs" | K4 (açılmadı, WebSearch sentezi) | 2026-09-18 | Belirsiz [?] |
| **Antitez/red-team (critic/verifier)** | Kısmen evet ("critic" adıyla) | AG2 deseni: "Critics or Verifiers are agents that review, challenge, and quality-check what producers output... prevent bad work from propagating" | K5 (açılmadı) | 2026-09-18 | Belirsiz [?] |
| **Alıntı/citation (özel doğrulama rolü)** | Evet, ayrı ajan | "Citation Agent" belgeleri işleyip alıntı konumlarını belirliyor — özel, dar iş | K1 | 2026-09-18 | Eski kuşak |
| **İcra vs planlama (Claude Code)** | Kısıtlı ayrım — bilinçli olarak sınırlı | Cognition: Claude Code'un alt-ajanları "operate only sequentially, never in parallel, and handle narrow question-answering rather than code-writing to avoid lacking critical context" | K2 | 2026-09-18 | Model-bağımsız anlatı, 2025-06 |
| **Gözetim/supervisor** | Evet, en yaygın kanıtlanmış desen | "Supervisor-Worker pattern is the most production-proven orchestration topology" (LangGraph/CrewAI) | K6 (açılmadı) | 2026-09-18 | Belirsiz [?] |
| **Öğretim/tutor** | Evet ama akademik alanda, "pratisyen" değil | Tutor, peer, evaluator, mediator gibi ayrı ajan rolleri; "Pedagogical Agents" alt-sınıfları (Teaching-Assistance, Student-Support, Knowledge-Tracing, Error-Correction) | K9 (açılmadı) | 2026-09-18 | Karışık, çoğu 2025-08→2026-06 |
| **Kod inceleme (code-reviewer)** | Evet, resmî örnek olarak sunulmuş | Claude Code dokümanı: "code-reviewer" alt-ajanı `tools: Read, Grep, Glob` (yazma yetkisi yok), `memory: project` ile kalıcı öğrenme | K3 | 2026-09-18 | Güncel kuşak (Sonnet 5/Opus 5 alias'ları görülüyor) |

---

## 3. Denenip Geri Alınan Ayrımlar

1. **Küçük-model "apply edit" ayrımı (Cognition/Devin):** Büyük model açıklama yazıyor (markdown), küçük model dosyayı yeniden yazıyor — ayrı model katmanı denendi. Terk edildi: "the small model frequently misinterpreted instructions due to subtle ambiguities, causing incorrect edits." Karar/icra tek model aksiyonuna birleştirildi. (K2, 2025-06-12)
2. **Kod-yazan çok-ajan paralellik (Cognition/Devin, Flappy Bird örneği):** Paralel alt-ajanlara farklı görsel varlıklar (Süper Mario tarzı arka plan vs. Flappy Bird varlığı) yazdırıldığında çıktılar çelişti, ana ajan uzlaştıramadı. Sonuç: "share full agent traces, not just individual messages" ilkesine dönüldü, kod yazımı için çok-ajan paralelliği kod tabanında terk edildi. (K2)
3. **AutoGen'in kurumsal kaderi (Microsoft):** Ekim 2025'te bakım moduna alındı; proje AG2 (topluluk) ve Microsoft Agent Framework'e bölündü — orijinal tek-çerçeve mimarisi geri alındı, iki ayrı yola ayrıştırıldı. Bu bir perspektif ayrımı değil kurumsal/proje ayrımı ama ilgili çünkü çok-ajan tasarım felsefesi değişti. (K8, açılmadı — ikincil kaynak, düşük güven)
4. Anthropic'in kendi metninde (K1) genel bir "geri alma" ifadesi bulunamadı; yalnız "early failures" (basit sorgular için 50 alt-ajan doğurma, tekrar/duplication sorunları) düzeltme yoluyla çözülmüş, tam terk edilmiş bir ayrım örneği net biçimde metinde yok — **bu madde düşük güven, spekülasyon işaretli.**

---

## 4. Alt-Ajan vs Kalıcı Ajan (hafıza · kimlik · yetki · oturum)

**Claude Code alt-ajanları (K3, birincil, açık kaynak — resmî doküman, güncel kuşak):**
- **Hafıza:** Varsayılan yok. `memory: project|user|local` alanı açıkça eklenmedikçe alt-ajan oturumlar arası hiçbir şey taşımaz. Etkinleştirilirse `MEMORY.md` ilk 200 satır/25KB sistem promptuna eklenir.
- **Kimlik:** Her çağrı taze bir örnek (`fresh instance with an isolated context window`); adı ve YAML tanımı sabit ama "kendisi" oturumlar arası devam etmez.
- **Bağlam devralma:** Sistem promptu (kendi md gövdesi), görev mesajı, CLAUDE.md hiyerarşisi, git durumu (ebeveyn oturum başlangıcından anlık görüntü), önceden yüklenmiş skill'ler, kardeş ajan listesi (SendMessage için) — ama konuşma geçmişi, önceki skill çağrıları, önceden okunmuş dosyalar, çıktı stili tercihleri, ana konuşmanın otomatik hafızası **aktarılmaz**.
- **İstisna — Fork:** `context: fork` ile oluşturulan alt-görev ebeveynin TAM konuşma geçmişini ve araç setini devralır — yani "kalıcı ajan"a en yakın istisna budur; geri kalan her şey ayrı/hafızasız.
- **Yetki:** Model, araç erişimi, izin modu (`permissionMode`) ajan tanımında elle atanır; öntanımlı perspektif-otomatik atama yok.

**MetaGPT (K4, açılmadı, düşük güven):** Her rol (PM, mimar, proje yöneticisi, mühendis, QA) kendi sistem promptu ve mesaj havuzu aboneliğiyle ayrı ajan; roller arası iletişim paylaşılan mesaj havuzu üzerinden, rol-bazlı filtreleme ile — bu "kalıcı kimlik + dar abonelik" modeline örnek, ama makale doğrudan açılmadığı için ayrıntı teyit edilmedi.

**Anthropic çok-ajan sistemi (K1):** Alt-ajanlar (subagents) görev başına doğar, kendi bağlam penceresiyle paralel çalışır, sonuçları lidere döner — açık biçimde "alt-ajan = geçici" modeli; lider ajan ise plan durumunu hafızaya yazarak (200K token kırpılma riskine karşı) kendi süreklilik sorununu çözüyor, ama bu "kalıcı kimlik" değil "tek oturum içi devamlılık" — oturumlar arası kalıcı hafızadan bahsedilmiyor.

---

## 5. Model Katmanlaması

- **Anthropic (K1, birincil, açık):** Lider = Claude Opus 4, işçi = Claude Sonnet 4. Ölçülen sonuç: "a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2%" — rakam kaynaklı, K1'den, AS-OF 2025-06-13 yayın / 2026-09-18 çekim. **Bu eski kuşak (4.x) verisidir, güncel kuşağa (5.x) genellenmemeli.**
- **Claude Code (K3, birincil, güncel kuşak):** Ajan başına `model:` alanı elle seçilir (`haiku` ucuz-keşif, `sonnet` orta, `opus` ağır muhakeme); çözünürlük sırası: çağrı-anı parametre → ajan tanımı → ortam değişkeni (`CLAUDE_CODE_SUBAGENT_MODEL`) → ana konuşma modeli. Zorla tek model: `CLAUDE_CODE_SUBAGENT_MODEL_FORCE`. **Perspektife göre otomatik model ataması yok** — katmanlama tamamen tasarımcı kararı.
- **AG2/LangGraph örneği (K6, açılmadı, düşük güven):** "32B supervisor + 7B workers" gibi somut boyut örneği aramada geçti (40+ GB VRAM gereksinimi) ama kaynak açılmadığı için doğrudan alıntı doğrulanmadı — **[?] işaretli.**
- **Cognition/Devin (K2):** Model boyut-katmanlaması (büyük model karar, küçük model uygulama) açıkça **denenmiş ve terk edilmiş** (bkz. §3 madde 1) — bu aile B'de nadir bir "negatif" model-tiering kanıtı.

---

## 6. Öğretim/Tutor Ajanı Vakaları

Aile B'nin tipik pratisyen kaynaklarında (Anthropic, Cognition, Claude Code, AG2) **doğrudan bir tutor/öğretim ajanı vakasına rastlanmadı.** Bulunan tek küme akademik eğitim-teknolojisi literatürü (K9, açılmadı, düşük güven):
- Tutor rolü, "peer", "evaluator", "mediator" rollerinden ayrı ajan olarak kuruluyor.
- Alt-sınıflandırma: Teaching-Assistance Agents, Student-Support Agents, Knowledge-Tracing Agents, Error-Correction/Detection Agents.
- Bir kaynak (arXiv 2508.19611) öğretim kadrosunun iş yükünü azaltmak için "Instructional Agents" adıyla çok-ajan öğretim tasarımı öneriyor.

**Uyarı:** Bu kaynaklar akademik makale/anket biçiminde, gerçek üretimde çalışan kişisel orkestratör (Kun Chen/firstmate sınıfı) değil — soru aile B'nin "pratisyen" tanımına tam uymuyor. Tutor ajanı için **pratisyen (üretim, açık-kaynak harness) örneği bulunamadı**; bu meşru bir "bulunamadı" sonucudur, uydurma yapılmadı.

---

## 7. İDDİA LİSTESİ

1. Anthropic'in üretim çok-ajanlı araştırma sisteminde lider (Opus 4) ile paralel alt-ajanlar (Sonnet 4) arasındaki ayrım, paralellik ve bağlam-sıkıştırma gerekçesine dayanır.
2. Cognition (Devin), kod yazma görevlerinde paralel çok-ajan mimarisini terk edip tek-ajan + sıralı, dar soru-cevap alt-ajan modeline geçmiştir.
3. Claude Code alt-ajanları varsayılan olarak hafızasızdır; `memory` alanı açıkça etkinleştirilmedikçe oturumlar arası kimlik/hafıza taşımazlar.
4. Claude Code'da model katmanlaması ajan tanımında elle atanır (`model: haiku/sonnet/opus`); perspektife göre otomatik atama yoktur.
5. MetaGPT yazılım-şirketi rollerini (PM, mimar, proje yöneticisi, mühendis, QA mühendisi) ayrı ajan olarak kurar; bu bulgu birincil kaynaktan doğrulanmadı, yalnız arama sentezine dayanır.
6. AG2 (AutoGen fork) deseninde "critic/verifier" ajanı üretici (coder) ajandan ayrı kurulur; gerekçe hatalı çıktının yayılmasını önlemektir.
7. Supervisor-worker deseni, incelenen ikincil kaynaklarda "en yaygın kanıtlanmış" orkestrasyon topolojisi olarak tanımlanıyor; bu iddia birincil kaynaktan doğrulanmadı.
8. OpenHands'in 2025-11 SDK'sı varsayılan olarak tek-ajan konuşmasına odaklanır, çok-ajan orkestrasyonu destekler ama öntanımlı değildir.
9. Öğretim/tutor ajanı ayrımına dair bulunan tüm kanıtlar akademik anket/makale kaynaklıdır; aile B'nin pratisyen tanımına uyan bir tutor-ajanı vakası bulunamadı.
10. Microsoft, Ekim 2025'te AutoGen'i bakım moduna aldı; proje AG2 (topluluk fork'u) ve Microsoft Agent Framework olarak ikiye ayrıldı.
11. Claude Code'da `context: fork` istisnası dışında alt-ajanlar ebeveynin konuşma geçmişini devralmaz; bu mekanizma "alt-ajan vs kalıcı ajan" ayrımını araç düzeyinde somutlaştıran tek örnektir.
12. İncelenen kaynakların hiçbiri "antitez/red-team" rolünü bu adla ayrı kalıcı bir ajan sınıfı olarak tanımlamadı; en yakın karşılıklar "critic/verifier" (AG2) ve "QA/reviewer" (MetaGPT, Claude Code code-reviewer) etiketleridir.

---

**Epistemolojik not:** K4-K9 zaman kısıtı nedeniyle WebFetch ile açılmadı; yalnız arama motoru sentezine dayanır, düşük güven olarak işaretlendi. K1-K3 birincil kaynak olarak açıldı ve alıntılar doğrudan bu sayfalardan alındı.
