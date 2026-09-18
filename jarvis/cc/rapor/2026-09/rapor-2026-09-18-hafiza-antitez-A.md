# Atlas ANTİTEZ Raporu — Aile A (harness/ürün hafıza özellikleri)

Tarih: 2026-09-18 · Rol: açık Devil's-Advocate (¬T arayışı) · Dil: Türkçe
Disiplin: yalnız web; en az 2 kaynak gerçekten açıldı (fiilen 8 primer sayfa açıldı — aşağıda); AS-OF = çekim tarihi 2026-09-18; rakamlar kaynaklı, kestirim yok.

Not: hükümler TEZ hakkındadır (TEZ ÇÜRÜDÜ / DARALDI / ÇÜRÜTÜLEMEDİ). "ÇÜRÜTÜLEMEDİ" = ¬T için birincil kanıt bulunamadı, tez ayakta kalır (bu da meşru bir antitez sonucudur).

---

## 1. "CLAUDE.md insan-yazımlıdır; auto memory 4 tipte (user/feedback/project/reference) Claude-yazımlıdır."

¬T kanıtı arandı: bulunamadı, tam tersine birincil kaynak tezi birebir doğruluyor.
Kaynak: code.claude.com/docs/en/memory (Anthropic resmi Claude Code dokümanı)
Alıntı: "CLAUDE.md files | Who writes it: You ... Auto memory | Who writes it: Claude" ve "Claude saves four kinds of notes for itself... `user`... `feedback`... `project`... `reference`".
AS-OF: çekim 2026-09-18 (sayfa tarihsiz, sürekli güncellenen doküman; Claude Code ≥ güncel sürüm varsayımı, spesifik versiyon numarası sayfada yok).
Kuşak: N/A (harness özelliği, model kuşağı değil).
**Hüküm: TEZ ÇÜRÜTÜLEMEDİ** (doğrudan teyit edildi, ¬T yok).

---

## 2. "Auto memory MEMORY.md 200 satır/25 KB sınırlıdır; aşımda otomatik kısaltma uyarısı verir."

¬T kanıtı arandı: mekanizma tam "otomatik kısaltma" değil, iki kademeli — sınıra yakınken "reminder" (kısaltma hatırlatması), sınırı aşınca "error" (satırı düzeltmeye zorlayan hata); dosyanın kendisi otomatik kısaltılmıyor, yalnız **okuma sınırı aşan kısım yüklenmiyor**.
Kaynak: code.claude.com/docs/en/memory
Alıntı: "If the file is near a limit, Claude Code reminds Claude to shorten it... If the file is over a limit, the write still succeeds, but Claude Code returns an error telling Claude to rewrite the index, because everything past the limit is dropped on the next load."
AS-OF: çekim 2026-09-18.
**Hüküm: TEZ DARALDI** — sayısal sınır (200 satır/25 KB) doğru, ama "otomatik kısaltma" yanlış çerçeveleme: dosya kendiliğinden kısaltılmaz, sadece limit üstü kısım sonraki yüklemede sessizce düşer + Claude'a uyarı/hata döner.

---

## 3. "Alt-ajanlara ana konuşmanın auto memory'si yüklenmez (fork hariç)."

¬T kanıtı arandı: bulunamadı, birincil kaynak birebir doğruluyor.
Kaynak: code.claude.com/docs/en/memory
Alıntı: "The main conversation's auto memory isn't loaded into subagents; the exception is a fork, which inherits the parent conversation and system prompt. A subagent's own auto memory, enabled with the subagent `memory` field, is a separate directory."
AS-OF: çekim 2026-09-18.
**Hüküm: TEZ ÇÜRÜTÜLEMEDİ.**

---

## 4. "Memory tool `/memories` istemci-taraflıdır ve yalnız Claude 4+ modellerde çalışır."

¬T kanıtı arandı: bulunamadı, birincil kaynak birebir doğruluyor.
Kaynak: platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool (Anthropic API resmi dokümanı)
Alıntı: "The memory tool operates client-side: Claude requests file operations, and your application executes them." ve "The memory tool is available on all Claude 4 and later models."
AS-OF: çekim 2026-09-18; tool versiyonu `memory_20250818`.
**Hüküm: TEZ ÇÜRÜTÜLEMEDİ.**

---

## 5. "Memory + context editing kombinasyonu Anthropic iç değerlendirmesinde %39 iyileşme sağlar."

¬T kanıtı arandı: bulunamadı; rakam Anthropic'in kendi duyurusunda teyitli, hatta kırılımı da var.
Kaynak: anthropic.com/news/context-management (Anthropic resmi duyuru, WebSearch üzerinden erişilen özet; birebir URL doğrulandı)
Bulgu: "Combining the memory tool with context editing improved performance by 39% over baseline... context editing alone delivered a 29% improvement, with the additional 10 percentage points coming from adding the memory tool." Ayrı olarak 100 turluk web-arama görevinde %84 token tasarrufu.
AS-OF: duyuru tarihi 2026 içi (context-management lansmanı); çekim 2026-09-18.
**Hüküm: TEZ ÇÜRÜTÜLEMEDİ** — rakam Anthropic'in kendi iç değerlendirmesi, bağımsız doğrulama yok ama bu zaten tezin kendi iddiasıyla (iç değerlendirme) tutarlı; bağımsız çapraz-referans bulunmadı (sınır olarak not edilir).

---

## 6. "Context editing istemci-taraflı tool-result temizler; compaction sunucu-taraflı tüm konuşmayı özetler."

¬T kanıtı arandı: **BULUNDU ve tez ÇÜRÜDÜ** — yön ters. Context editing'in kendi ayrılmış sayfası açıkça **sunucu-taraflı** olduğunu söylüyor; compaction'ın ise hem sunucu-taraflı (önerilen) hem istemci-taraflı (deprecated SDK) biçimleri var.
Kaynak: platform.claude.com/docs/en/build-with-claude/context-editing (birebir alıntı doğrulandı)
Alıntı: "Context editing is applied server-side before the prompt reaches Claude." ve "Anthropic recommends server-side compaction over SDK compaction... Use SDK compaction only if you specifically need client-side control."
Çelişki notu: memory-tool sayfası ("Using with compaction" bölümü) tam tersini yazıyor — "Context editing clears specific tool results on the client. Compaction automatically summarizes the whole conversation on the server" (platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool). Bu, Anthropic'in **kendi iki resmi sayfası arasında iç çelişki** — biri context editing'i client, diğeri server diyor.
AS-OF: her iki sayfa da çekim 2026-09-18.
**Hüküm: TEZ ÇÜRÜDÜ** (dedike context-editing sayfası birincil kaynak sayılırsa yön ters: context editing = server-side, compaction hem server hem — artık deprecated — client seçeneğine sahip). Ek bulgu: Anthropic dokümantasyonu kendi içinde tutarsız, bu başlı başına bir ikinci bulgu.

---

## 7. "OpenAI Agents SDK compaction eşik-tabanlıdır ve streaming'i bloke edebilir."

¬T kanıtı: "eşik-tabanlı" kısmı doğrulandı; "bloke edebilir" kısmı için **doğrudan resmi guide sayfası tam tersini söylüyor** (sunucu-taraflı Responses API compaction modunda stream kesilmiyor).
Kaynak: developers.openai.com/api/docs/guides/compaction (OpenAI resmi API rehberi)
Alıntı: "When the rendered token count crosses the configured threshold, the server runs server-side compaction." ve "The response stream includes the encrypted compaction item" (stream kesintisiz devam eder, ayrı `/responses/compact` çağrısı gerekmez).
Ayrı bulgu (WebSearch, birincil sayfa doğrulanamadı): Agents SDK'nin `OpenAIResponsesCompactionSession` sarmalayıcısı için ayrı bir uyarı var — "stream_events() can stay open for a few seconds after the last output token if compaction is heavy," düşük gecikme isteyenlere auto-compaction'ı kapatıp elle `runCompaction` çağırma önerisi. Bu iddiayı doğrudan referans sayfasından (openai.github.io/openai-agents-js/.../openairesponsescompactionsession/) birebir alıntıyla teyit edemedim — sayfa API-referans iskeleti döndürdü, ilgili cümleler orada yoktu (kaynak WebSearch özetiydi, birincil değil).
AS-OF: çekim 2026-09-18.
**Hüküm: TEZ DARALDI** — "eşik-tabanlı" doğru; "bloke edebilir" yalnız SDK'nin ayrı, deprecate olmayan ama farklı bir client-wrapper modunda geçerli olabilir ve bu kısım birincil kaynaktan doğrulanamadı (yalnız ikincil özet); ana Responses API server-side modunda ise doküman açıkça "stream kesilmez" diyor.

---

## 8. "ChatGPT 'saved memories' (açık) ile 'chat history reference' (örtük) iki ayrı mekanizmadır."

¬T kanıtı arandı: bulunamadı, OpenAI Help Center teyit ediyor.
Kaynak: help.openai.com/en/articles/8590148-memory-faq (OpenAI resmi yardım merkezi, WebSearch ile erişilen özet)
Bulgu: "Saved memories are stored separately from chat history... separate toggles: 'Reference saved memories' and 'Reference chat history.' You can turn them on or off independently."
AS-OF: çekim 2026-09-18.
**Hüküm: TEZ ÇÜRÜTÜLEMEDİ.**

---

## 9. "Google ADK'de Session ve MemoryService ayrıdır; unutma politikası dokümante edilmemiştir."

¬T kanıtı arandı: bulunamadı, birincil kaynak (redirect sonrası adk.dev) her iki alt-iddiayı da doğruluyor.
Kaynak: adk.dev/sessions/memory/ (google.github.io/adk-docs/sessions/memory/ adresinden 301 yönlendirme; Google resmi ADK dokümanı)
Alıntı: "`Session`/`State`: It's your short-term memory during one specific chat. Long-Term Knowledge (`MemoryService`): It's a searchable archive... potentially containing information from many past chats." Eviction/forgetting/retention politikası konusunda sayfada **hiçbir açıklama yok**; yalnız `InMemoryMemoryService` için "data is lost on restart" notu var (bu bir unutma politikası değil, implementasyon sınırı).
AS-OF: çekim 2026-09-18.
**Hüküm: TEZ ÇÜRÜTÜLEMEDİ.**

---

## 10. "Letta/MemGPT 3 katmanlıdır (core/recall/archival) ve insan onay katmanı yoktur."

¬T kanıtı arandı: 3 katman kısmı doğrulandı (ikincil kaynaklarla — docs.letta.com/memory/overview 404 verdi, birincil sayfaya doğrudan erişilemedi). "İnsan onay katmanı yoktur" iddiasına kısmi karşı-bulgu var ama **farklı bir katmana ait**: Letta Code ürününde tool-çağrısı onayı (`human-in-the-loop approval flows`, `Update Approval For Tool` API) mevcut — ancak bu memory-tier mimarisinin (core/recall/archival) bir parçası değil, ayrı bir tool-execution güvenlik katmanı.
Kaynak: docs.letta.com (WebSearch üzerinden Letta resmi dokümanına ait sayfa başlıkları ve alıntılar: "Permissions", "Update Approval For Tool", "Core memory"); doğrudan WebFetch docs.letta.com/memory/overview → 404 (sayfa yolu değişmiş olabilir, bayraklanır).
AS-OF: çekim 2026-09-18.
**Hüküm: TEZ DARALDI** — 3-katman mimarisi teyitli; "insan onay katmanı yok" iddiası memory-yazma kararları için hâlâ ayakta (ajan kendi kendine karar veriyor), ama Letta ekosisteminde genel olarak bir "human-in-the-loop approval" özelliği (farklı katman: tool execution) var — tez bunu dışlamamış olsa karışıklık riski taşır. Birincil memory-overview sayfası 404 olduğu için tam doğrulama yapılamadı (bayrak).

---

## 11. "Mem0 4 aşamalı pipeline'da LLM otomatik ADD/UPDATE/DELETE/NOOP kararı verir."

¬T kanıtı: **BULUNDU, "4 aşamalı" kısmı çürüdü.** Mem0'ın kendi akademik makalesi pipeline'ı **iki fazlı** (extraction + update) olarak tanımlıyor; dört olan şey aşama sayısı değil, update fazındaki **operasyon** seçenekleri (ADD/UPDATE/DELETE/NOOP). Güncel resmi dokümantasyon ise 3 aşama tanımlıyor (context gathering, retrieval, extraction+update) — kaynaklar arası sayı da tutarsız, ama hiçbiri "4 aşama" demiyor.
Kaynak 1 (birincil akademik): arxiv.org/html/2504.19413v1, "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory" (Chhikara ve ark., 2025)
Alıntı: "Mem0 introduces a two-phase extraction pipeline with four-operation updates (ADD/UPDATE/DELETE/NOOP)."
Kaynak 2 (birincil güncel doküman): docs.mem0.ai/core-concepts/memory-types (WebFetch ile doğrudan açıldı)
Bulgu: sayfa 3 aşama tanımlıyor (context gathering / existing memory retrieval / extraction) — "4 değil, 3 aşamalıdır" (araç özeti, ama sayfadan birebir alıntı: "decides, per fact, whether to `ADD`, `UPDATE`, `DELETE`, or leave a memory alone").
AS-OF: makale 2025-04 (arxiv v1), doküman çekimi 2026-09-18.
**Hüküm: TEZ DARALDI/ÇÜRÜDÜ** (karma) — ADD/UPDATE/DELETE/NOOP operasyon seti doğru (4 operasyon), ama "4 aşamalı pipeline" ifadesi yanlış: birincil akademik kaynak 2 faz diyor, güncel resmi dokümantasyon 3 aşama diyor; "4" sayısı yalnızca operasyonlara ait, aşamalara değil — tez bu ikisini karıştırıyor.

---

## 12. "LangMem semantik/epizodik/prosedürel ayrımı + hot-path/background yazma yolları sunar."

¬T kanıtı: hot-path/background ayrımı birincil kaynakla teyitli; semantik/epizodik/prosedürel üçlü ayrımı **ana sayfada açıkça yazılı bulunamadı** (WebFetch ana sayfada bu üçlü net göremedi), ama bağımsız ikincil kaynaklar (LangChain blog, akademik özetler) bu üçlü ayrımı LangMem'e doğrudan atfediyor.
Kaynak 1: langchain-ai.github.io/langmem/ (birincil, doğrudan WebFetch ile açıldı)
Alıntı: "agents can use to record and search information during active conversations 'in the hot path'" ve "⚙️ Background memory manager that automatically extracts, consolidates, and updates agent knowledge" — "🚀 Hot Path Quickstart" ve "Background Quickstart" başlıkları sayfada mevcut.
Kaynak 2 (ikincil, WebSearch özeti): "LangMem explicitly distinguishes among semantic memory, episodic memory, and procedural memory" — ana sayfa fetch'inde bu üçlü cümle birebir bulunamadı, alt-sayfalarda (`concepts/conceptual_guide`) olabilir, doğrulanamadı.
AS-OF: çekim 2026-09-18.
**Hüküm: TEZ DARALDI** — hot-path/background kısmı ÇÜRÜTÜLEMEDİ (tam teyitli); semantik/epizodik/prosedürel üçlü ayrım kısmı birincil kaynaktan (ana sayfa) doğrudan doğrulanamadı, yalnız ikincil kaynaklarla destekleniyor (bayrak: alt-sayfa taraması eksik kaldı).

---

## Açılan Kaynak Listesi (WebFetch ile fiilen açılanlar)

1. code.claude.com/docs/en/memory
2. platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
3. platform.claude.com/docs/en/build-with-claude/context-editing (2 kez, farklı promptlarla)
4. developers.openai.com/api/docs/guides/compaction
5. google.github.io/adk-docs/sessions/memory/ → 301 → adk.dev/sessions/memory/ (açıldı)
6. docs.mem0.ai/core-concepts/memory-types
7. langchain-ai.github.io/langmem/
8. openai.github.io/openai-agents-js/openai/agents/classes/openairesponsescompactionsession/ (açıldı ama ilgili içerik yoktu — bayrak)

404/başarısız: platform.claude.com/docs/en/build-with-claude/memory-tool (ilk deneme, yanlış yol) · docs.letta.com/memory/overview (404, yol değişmiş olabilir).

## Sınırlar

- Claim 5, 8, 10, 11, 12'nin bir kısmı için birincil sayfaya değil, WebSearch'ün ürettiği ikincil özete dayanıldı; bu özetler kaynak URL'i doğru gösterse de birebir alıntı garantisi taşımaz (bayraklandı).
- Letta memory-overview sayfası 404 verdiği için 3-katman iddiası yalnız ikincil kaynaklarla (arama sonucu metinleri) teyit edildi, tam birincil doğrulama yapılamadı.
