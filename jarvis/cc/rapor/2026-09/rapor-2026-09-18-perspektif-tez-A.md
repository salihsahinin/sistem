# Atlas TEZ Raporu — Aile A: Sektör Öncülleri (Perspektif Ayrımı Araştırması)

**Tarih:** 2026-09-18
**Rol:** TEZ araştırmacısı, aile A (Anthropic, Cognition/Devin, OpenAI, Cursor, Claude Agent SDK)
**Soru:** Çok-ajanlı kodlama/ajan sistemlerinde ajan sınırı hangi perspektif ayrımına göre çiziliyor?

---

## 1. Kaynak Listesi

| # | URL | Yayın Tarihi | Açıldı mı (WebFetch) | Model/Kuşak | Kullanım Biçimi |
|---|-----|--------------|----------------------|-------------|------------------|
| K1 | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | **EVET** (birincil) | Claude Opus 4 (lider) + Claude Sonnet 4 (işçi) — 2025-Q2 kuşağı, 4.x sınıfı | Üretim (Claude "Research" özelliği) |
| K2 | https://cognition.com/blog/dont-build-multi-agents | 2025-06-12 | **EVET** (birincil) | Belirtilmemiş (Devin ürün deneyimi, 2025-H1) | Üretim gözlemi + karşı-argüman |
| K3 | https://code.claude.com/docs/en/agent-sdk/subagents | Sürekli güncellenen canlı dokümantasyon, erişim 2026-09-18 | **EVET** (birincil) | Model-agnostik alan (`model` alanı: fable/opus/sonnet/haiku/inherit); ayrı bölüm "Opus 5 ile subagent" — **güncel kuşak** (Opus 5, 2026 sınıfı) | Üretim (Claude Agent SDK / Claude Code canlı ürün belgesi) |
| K4 | https://cognition.com/blog/multi-agents-working | 2026-04-22 | **EVET** (birincil) | SWE-1.5, SWE-1.6, Sonnet 4.5, Opus-class, Mythos-class, GPT (karma, 2025-Q4→2026-Q1 kuşağı) — **güncel kuşak** | Üretim (Devin ürün güncellemesi, K2'nin geri alımı) |
| K5 | https://cursor.com/blog/plan-mode | 2025-10-07 | EVET (açıldı, ama ayrım gerekçesi içermiyor) | Belirtilmemiş, Cursor Agent (2025-Q4) | Üretim (Cursor ürün duyurusu) |
| K6 | https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/ | Bilinmiyor (2025 tahmini, OpenAI "practical guide to building agents") | **HAYIR — 403 Forbidden** (bayraklandı, paywall/bot-engelli) | — | — |
| K7 | https://openai.github.io/openai-agents-python/multi_agent/ | Sürekli güncellenen canlı dok (arama özetinden, açılmadı) | HAYIR (yalnız arama özeti — WebFetch ile doğrulanmadı, düşük güvenle kaydediliyor) | OpenAI Agents SDK, kuşak belirtilmemiş | Üretim/SDK dokümantasyonu |

**Not (dürüstlük):** K7 yalnız arama motoru özetinden alındı, WebFetch ile birincil metin doğrulanmadı; bu yüzden K7'ye dayanan hiçbir iddia hakem aşamasına "doğrulanmış" olarak sunulmuyor, yalnız yönlendirici bağlam olarak (2) bölümünde düşük güvenle işaretlendi.

---

## 2. Bulgu Tablosu: Perspektif × Ayrım × Gerekçe × Kaynak

| Perspektif | Ayrı ajan/bağlam mı? | Gerekçe sınıfı | Kaynak | AS-OF | Kuşak |
|---|---|---|---|---|---|
| **Planlama (lider) vs icra (işçi)** | EVET, ayrı ajan — "lead agent" plan kurar, "subagent"lara devreder | Paralellik + bağlam sıkıştırma ("subagents facilitate compression by operating in parallel with their own context windows") | K1 (Architecture overview) | 2026-09-18 çekim / 2025-06-13 yayın | Opus 4 / Sonnet 4 (2025-Q2, eski kuşak — 09-2026'dan bakınca "o zaman böyle") |
| **Araştırma (çoklu alt-görev)** | EVET, ayrı bağlam — her subagent "distinct tools, prompts, and exploration trajectories" | Bağlam kirlenmesi önleme + path-dependency azaltma | K1 (Benefits section) | 2026-09-18 / 2025-06-13 | eski kuşak |
| **Hakem/değerlendirici (atıf ekleme)** | EVET, ayrı **CitationAgent** — ayrı rol, ayrı geçiş | Yapan≠ölçen: yazan ajanın atıf bulma işi farklı beceri/bağlam ister | K1 (Process diagram section) | 2026-09-18 / 2025-06-13 | eski kuşak |
| **Değerlendirme/skor (LLM judge)** | EVET, ayrı — "an LLM judge that evaluated each output against criteria in a rubric" | Yapan≠ölçen (üretimi yapan ajan kendi çıktısını puanlamıyor) | K1 (Evaluation section) | 2026-09-18 / 2025-06-13 | eski kuşak |
| **İcra (kod yazma, çok-ajanlı)** | HAYIR — Cognition, paralel yazan çoklu ajanı **reddediyor** | Bağlam kirlenmesi + çelişen zımni kararlar ("actions carry implicit decisions, and conflicting decisions carry bad results") | K2 (Flappy Bird örneği) | 2026-09-18 / 2025-06-12 | eski kuşak |
| **Salt-okur alt-görev (arama, kod arama)** | EVET, sınırlı — "most multi-agent setups in the world are limited to 'readonly' subagents, like web search subagents and code search subagents" | Yetki (yazma yetkisi yok → çelişki riski düşük) | K2 | 2026-09-18 / 2025-06-12 | eski kuşak |
| **Sıkıştırma/özetleme (uzun görev)** | EVET, ayrı katman — geçmişi "key details, events, decisions" haline sıkıştıran ayrı LLM katmanı öneriliyor | Bağlam yönetimi (token sınırı), ama tek-iş-parçacıklı karar akışını bozmadan | K2 (Context Management Solutions) | 2026-09-18 / 2025-06-12 | eski kuşak |
| **Kod incelemesi (review) — GÜNCEL KUŞAK REVİZYONU** | EVET, ayrı bağlamlı inceleyici ajan — "Code-Review-Loop": biri yazar, ayrı bir inceleme ajanı paylaşılan bağlam OLMADAN bağımsız kontrol eder | Yapan≠ölçen + temiz bağlam hata tespitini artırıyor (PR başına ~2 hata, %58'i şiddetli olarak işaretleniyor) | K4 (Code-Review-Loop section) | 2026-09-18 / 2026-04-22 | **güncel kuşak** (SWE-1.5/1.6, Sonnet 4.5, Opus-class) |
| **Model kademesi (küçük→büyük eskalasyon) — "Smart Friend"** | EVET, ayrı model/perspektif — küçük/birincil model zorlandığını fark edince büyük modele eskale ediyor | Maliyet + yetenek eşiği ("let the primary/smaller model decide when a situation was tricky enough") | K4 (Smart Friend section) | 2026-09-18 / 2026-04-22 | **güncel kuşak** |
| **Yönetici-çocuk devri (büyük ölçekli orkestrasyon)** | EVET, tek yönetici + çoklu "child agent" — map-reduce deseni | Ölçek + paralellik, ama düzenli hiyerarşi (dağınık eş-ağ değil) | K4 (Looking Ahead: Higher-Level Delegation) | 2026-09-18 / 2026-04-22 | **güncel kuşak** |
| **Planlama modu (Cursor)** | EVET, ayrı mod — Agent önce plan yazıyor, sonra icraya geçiyor | Belirtilmemiş açık gerekçe (yalnız sonuç: "significantly improve the code generated") — **gerekçe K5'te açık değil, bayraklanıyor** | K5 | 2026-09-18 / 2025-10-07 | eski kuşak |
| **Alt-ajan tool kısıtlaması (yetki ayrımı)** | EVET — `tools` alanıyla salt-okur (Read/Grep/Glob) vs yazma yetkili subagent ayrımı yapılandırma düzeyinde birinci sınıf | Yetki (istenmeyen eylem riskini azaltma: "reducing the risk of unintended actions") | K3 (Tool restrictions) | 2026-09-18 (canlı dok) | **güncel kuşak** (Opus 5 referanslı) |
| **Manager (araç olarak ajan) vs Handoff (devir)** | EVET, iki ayrı desen; manager orkestratör konuşmayı elde tutar, handoff'ta tam devir olur | Yetki modeli farkı (kim kullanıcıyla konuşur) | K7 (yalnız arama özeti, **düşük güven**, doğrulanmadı) | 2026-09-18 | belirsiz |

---

## 3. Reddedilen / Geri Alınan Ayrımlar

1. **Cognition'ın kendi geri alımı (K2 → K4):** 2025-06-12'de "Don't Build Multi-Agents" ile paralel-yazan çoklu ajanı toptan reddettiler; 2026-04-22'de (K4) bunu kısmen geri aldılar — "our original observations still hold today for parallel-writer swarms" (paralel-YAZAN swarm'lar hâlâ kötü) ama "a narrower class of patterns that do [work]" bulduklarını açıkladılar: tek-iş-parçacıklı yazma + ayrı-bağlamlı inceleme, model-kademe eskalasyonu, ve düzenli yönetici-çocuk hiyerarşisi. **Reddedilen kaldı:** dağınık/eş-ağ (unstructured agent networks negotiating autonomously).
2. **Anthropic'in kendi sınırlaması (K1):** "Some domains that require all agents to share the same context or involve many dependencies between agents are not a good fit for multi-agent systems today" — kodlama görevleri açıkça bu sınıfa örnek verilmiş (Benefits section). Yani Anthropic da çok-ajanlı mimariyi evrensel çözüm olarak sunmuyor, sıkı bağımlılıklı görevlerde (çoğu kodlama) reddediyor.
3. **Maliyet itirafı (K1):** "Multi-agent systems use about 15× more tokens than chats" — açık ayrım maliyeti itiraf ediliyor, gerekçe koşulsuz değil.

---

## 4. Alt-Ajan vs Kalıcı Ajan Ayrımı (K3, birincil kaynak — canlı Claude Agent SDK dokümantasyonu)

| Boyut | Alt-ajan (subagent) | Kalıcı/ana ajan |
|---|---|---|
| **Hafıza** | Varsayılan: koşumlar arası hafızasız — "if you spawn a new sub-agent to 'continue where the last one left off,' it starts completely fresh" (genel bilgi, K3 dolaylı doğrulaması: fork olmayan subagent "starts fresh, with no parent conversation"). `memory` alanı opsiyonel (`user/project/local`) ile devre dışı bırakılabilir. | Ana konuşma geçmişini tutar, oturum devam eder. |
| **Bağlam** | İzole: yalnız kendi sistem promptu + Agent tool'un verdiği prompt string'i alır; "the subagent doesn't receive: the parent's conversation history or tool results" | Tüm geçmiş tool çağrıları ve sonuçları birikir. |
| **Kimlik** | `AgentDefinition` ile tanımlı (isim, açıklama, prompt, araç listesi); resume edilebilir (`agentId` + `session_id` ile), ama devam ancak açıkça istenirse. | Sabit sistem kimliği, tek oturum akışı. |
| **Yetki** | `tools` alanıyla kısıtlanabilir (örn. yalnız Read/Grep/Glob → yazamaz); `permissionMode` ayrı ayarlanabilir. | Ana izin modunu taşır. |
| **Dönüş** | Yalnız son mesaj ebeveyne döner — "only its final message returns to the parent"; ara adımlar ebeveyne sızmaz (bağlam kirlenmesi önleme mekanizması burada açık). | Doğrudan kullanıcıya/çağırana konuşur. |
| **Model** | Her subagent için ayrı `model` override edilebilir (fable/opus/sonnet/haiku/inherit) — model kademelemesi burada birinci sınıf yapılandırma alanı. | Ana modelin kendisi. |

**Not — Opus 5 özel davranışı (K3, güncel kuşak bölümü):** "Claude Opus 5 delegates to subagents more readily than earlier models" — bu yüzden derinlik/eşzamanlılık/harcama sınırları (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`, `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`, `maxBudgetUsd`) özellikle Opus 5 koşumlarında önemli hale geliyor — yani güçlü modelin kendi delegasyon eğilimi arttıkça açık frenleme mekanizması ürün düzeyinde eklenmiş.

---

## 5. Model Katmanlaması Pratiği

- **K1 (2025-06, eski kuşak):** "A multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2%" — güçlü model = orkestratör/lider, ucuz model = paralel işçi. Bu, sorunun öngördüğü "lider-işçi model katmanlaması" pratiğinin birincil kaynaklı doğrulamasıdır.
- **K4 (2026-04, güncel kuşak, "Smart Friend"):** Ters yönlü kademeleme — küçük/ucuz model VARSAYILAN çalışır, yalnız zorlandığını kendi kendine fark ettiğinde büyük/pahalı modele eskale eder ("let the primary/smaller model decide when a situation was tricky enough"). Bu K1'deki "başta büyük model karar verir" modelinden farklı: **maliyet-güdümlü, talep-üzerine eskalasyon**, sabit hiyerarşi değil.
- **K3 (canlı dok, güncel kuşak):** Model seçimi per-subagent yapılandırma alanı (`model` override), örnek kodda açıkça "use a more capable model for high-stakes reviews" (strict güvenlik incelemesi → opus, dengeli → sonnet) — yani model kademelemesi RİSK/ÖNEM eksenine göre yapılıyor, yalnız orkestratör/işçi eksenine göre değil.

---

## 6. İDDİA LİSTESİ (≤12, gerekçesiz, numaralı — antitez aşamasına)

1. Anthropic'in üretim araştırma sisteminde lider ajan (Opus 4) ile paralel işçi ajanlar (Sonnet 4) arasındaki ayrım, bağlam sıkıştırma ve paralellik gerekçesiyle kurulmuştur (K1).
2. Anthropic, atıf ekleme işini (CitationAgent) ve çıktı değerlendirmesini (LLM judge) üretici ajandan ayrı, "yapan≠ölçen" ilkesiyle kurmuştur (K1).
3. Anthropic, sıkı bağımlılıklı/paylaşılan-bağlam gerektiren görevlerde (kodlamanın çoğu dahil) çok-ajanlı mimariyi kendi belirttiği üzere uygun görmemektedir (K1).
4. Cognition (Devin), 2025 ortasında paralel yazan çoklu ajan mimarisini bağlam kirlenmesi ve çelişen zımni kararlar gerekçesiyle toptan reddetmiştir (K2).
5. Cognition, 2025 ortasında yalnız salt-okur (arama/kod-arama) alt-görevleri ayrı ajana verilebilir bulmuş, yazma yetkili paralel ajanları reddetmiştir (K2).
6. Cognition, 2026 ortasında kendi 2025 pozisyonunu kısmen geri almış; tek-iş-parçacıklı yazma + paylaşılan bağlamı olmayan ayrı inceleme ajanı (Code-Review-Loop) desenini üretimde çalışır bulmuştur (K4).
7. Cognition'ın Code-Review-Loop deseninde, incelemeyi yapan ajanın yazan ajanla bağlam paylaşmaması, hata tespit oranını artırdığı bildirilmektedir (PR başına ~2 hata, %58'i şiddetli) (K4).
8. Cognition, 2026'da model kademelemesini sabit lider-işçi hiyerarşisi değil, küçük modelin kendi kararıyla büyük modele eskalasyon talep ettiği bir düzen ("Smart Friend") olarak tanımlamıştır (K4).
9. Claude Agent SDK'nin canlı dokümantasyonu, alt-ajanı varsayılan olarak hafızasız ve ebeveyn bağlamından izole tanımlar; yalnız son mesaj ebeveyne döner, ara adımlar sızmaz (K3).
10. Claude Agent SDK'de alt-ajan başına model seçimi (fable/opus/sonnet/haiku/inherit) ve araç kısıtlaması birinci sınıf yapılandırma alanlarıdır; model kademelemesi risk/önem eksenine göre yapılabilir (K3).
11. Opus 5 modelinin alt-ajan çağırma eğilimi öncekilerden yüksek olduğu için, Claude Code ürün düzeyinde derinlik/eşzamanlılık/harcama sınırları eklenmiştir (K3).
12. Cursor'ın Plan Mode'u planlamayı icradan ayrı bir aşama olarak sunar, ancak yayımlanan blog yazısı bu ayrımın gerekçesini (bağlam kirlenmesi, yetki vb.) açıkça belirtmez, yalnız sonuç iyileşmesini bildirir (K5).

---

**Kaynak sayısı:** 7 (K1-K7)
**Açılan kaynak sayısı:** 5 birincil metin doğrudan WebFetch ile açıldı (K1, K2, K3, K4, K5); K6 403 ile engellendi (bayraklandı); K7 yalnız arama özeti, doğrulanmadı (düşük güven).
