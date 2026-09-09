# Rapor: IB-75 Tez İşçisi B — Bağlam-Devri Mekanizmaları

## 1. Künye
- Görev: aile B (bağlam-devri mekanizmaları) — devir birimi / devir anı / geri-dönüş
- Rol: İŞÇİ (karar yetkisi yok, yalnız kanıt)
- Tarih: 2026-09-09
- Araç bütçesi kullanımı: 4 WebSearch + 4 WebFetch (2 saved as persisted-output nedeniyle Bash grep ile okundu) = 8 çağrı

## 2. İddia Listesi

### (i) DEVİR BİRİMİ

- **B1 — D** — OpenAI Agents SDK: `HandoffInputData` yapılandırılmış-state şeması taşır — alanlar: `input_history` (Runner.run öncesi girdi geçmişi), `pre_handoff_items` (devir tetiklenen tur öncesi üretilen öğeler), `new_items` (mevcut turda üretilenler, devir çağrısı dahil), `input_items` (opsiyonel, `new_items` yerine sonraki ajana iletilecek filtrelenmiş girdi), `run_context` (RunContextWrapper). https://openai.github.io/openai-agents-python/handoffs/ — AS-OF 2026-09-09 (çekim tarihi)
- **B2 — D** — Aynı SDK'da `input_filter`: `HandoffInputData` alıp yeni bir `HandoffInputData` döndüren fonksiyon; örnek `remove_all_tools` filtresi tüm araç-ilişkili öğeleri geçmişten temizliyor — devir birimi "tam transkript" değil, filtrelenmiş/budanmış transkript olabiliyor. https://openai.github.io/openai-agents-python/handoffs/ — AS-OF 2026-09-09
- **B3 — D** — Anthropic Context Editing API: iki ayrı mekanizma var — (a) context editing (beta, `clear_tool_uses_20250919`): eski araç-sonuçlarını seçici temizler, yer-tutucu metinle değiştirir; (b) compaction: konuşmayı özetleyip özetle yeniden başlatır (yapılandırılmış state değil, özet-metin birimi). https://platform.claude.com/docs/en/build-with-claude/context-editing — AS-OF 2026-09-09
- **B4 — D** — Anthropic "agentic memory" (structured note-taking): ajan bağlam-dışı kalıcı notlar yazar, bu notlar sonraki turlarda bağlama geri çekilir — devir birimi burada "dosya-pointer/not" (context'ten düşürülüp harici depoya yazılan state). https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools — AS-OF 2026-09-09 [ikincil arama-özeti; birincil sayfa açılmadı]
- **B5 — D** — LangGraph: `Command(goto=<agent>)` düğüm-dönüşü hem state güncellemesini hem sonraki düğümü tek nesnede taşır; alt-graf içinden devirde `graph=Command.PARENT` gerekir — devir birimi = graph state (şema tanımlı, reducer'larla birleşen) + hedef düğüm adı. https://www.langchain.com/blog/command-a-new-tool-for-multi-agent-architectures-in-langgraph — AS-OF 2026-09-09 [arama-özeti; birincil sayfa açılmadı, K olarak işaretli]
- **B6 — D** — Claude Code subagent: kendi ayrı bağlam penceresinde çalışır, kendi CLAUDE.md/skill/MCP kopyasını yükler, ana oturuma yalnız NİHAİ ÖZETİNİ döndürür — devir birimi = tek özet metni (yapılandırılmamış, serbest metin). https://code.claude.com/docs/en/context-window — AS-OF 2026-09-09 (WebFetch ile birincil kaynak açıldı)
- **B7 — D** — Claude Code `/compact`: konuşmayı "yapılandırılmış özet"le değiştirir (`Replaces the conversation with a structured summary`); `/compact` sonrası yalnız fiilen çağrılan skill'lerin gövdesi (skill başına 5000 token tavanla) ve path-scoped kurallar yeniden enjekte edilir — devir birimi kısmen "yapılandırılmış özet + seçici yeniden-yükleme" karışımı. https://code.claude.com/docs/en/context-window — AS-OF 2026-09-09 (birincil, WebFetch)
- **B8 — D** — MemGPT/Letta: üç katmanlı bellek — Core Memory (bağlam penceresinde her zaman kalan küçük blok: persona, kullanıcı bilgisi), Recall Memory (konuşma geçmişi, harici), Archival Memory (bağlama sığmayan uzun-vadeli bellek, harici) — devir birimi işlev-çağrısıyla ajanın kendi seçtiği parça (self-edit). Taşma anında eski özet + tahliye edilen mesajlardan yeni özet üretiliyor (özyinelemeli özetleme). https://docs.letta.com/concepts/memory-management/ — AS-OF 2026-09-09 [arama-özeti; birincil sayfa açılmadı, K]

### (ii) DEVİR ANI

- **B9 — D** — Anthropic context editing varsayılan eşiği: `trigger` parametresi varsayılan **100.000 input token**; alternatif `type: "tool_uses"` (araç-kullanım sayısı) ile de tanımlanabilir. Örnek override: `{"type": "input_tokens", "value": 30000}`. `keep` parametresi varsayılan **3** araç-kullanım/sonuç çiftini korur. https://platform.claude.com/docs/en/build-with-claude/context-editing — AS-OF 2026-09-09 (birincil, WebFetch)
- **B10 — D** — Aynı API: `clear_at_least` parametresiyle her temizlemede en az kaç token'ın silineceği ayarlanabilir (önbellek geçersizleşmesini karşılamaya değer kılmak için) — sayısal varsayılan dokümanda belirtilmemiş (`None`). https://platform.claude.com/docs/en/build-with-claude/context-editing — AS-OF 2026-09-09
- **B11 — X** — OpenAI Agents SDK dokümantasyonu devir (handoff) için SAYISAL bir eşik tanımlamıyor; devir modelin kendi kararıyla (tool-call olarak handoff çağırması) tetikleniyor — token doluluğu/tur sayısı gibi otomatik bir eşik YOK. https://openai.github.io/openai-agents-python/handoffs/ — AS-OF 2026-09-09
- **B12 — D** — Claude Code: `/autocompact <token_sayısı>` komutuyla (örn. `/autocompact 500k`) bağlam penceresinin ne kadar dolduğunda otomatik compaction çalışacağı elle ayarlanabiliyor; modele göre varsayılan eşikler ayrı bir sayfada (`model-config#default-auto-compact-thresholds`) — bu sayfa bu koşumda açılmadı, sayısal varsayılan (örn. %XX) doğrulanamadı. https://code.claude.com/docs/en/context-window — AS-OF 2026-09-09 (birincil, WebFetch) — **AÇIK SORU**
- **B13 — K** — LangGraph'ta devir anı SAYISAL bir eşikle değil, ajan/router düğümünün state'i okuyup karar vermesiyle (`Command(goto=...)`) tetikleniyor gibi görünüyor — arama-özetinde eşik sayısı yok; birincil sayfa (`docs.langchain.com/oss/python/langchain/multi-agent/handoffs`) açılmadı, doğrulanmadı. AS-OF 2026-09-09
- **B14 — K** — MemGPT: bağlam taşması ("context overflow") anında özyinelemeli özetleme tetikleniyor; taşma sayısal bir token eşiğiyle tanımlı olmalı ama arama-özetinde somut sayı geçmedi. AS-OF 2026-09-09

### (iii) GERİ-DÖNÜŞ

- **B15 — D** — OpenAI SDK: `input_filter` devirde YALNIZ ileri yönü (yeni ajana ne gidiyor) filtreliyor; dokümantasyonda ayrı bir "geri-dönüş notu" şeması bulunamadı — geri-dönüş ayrı bir yapı değil, aynı `HandoffInputData` mekanizmasının simetriği olarak ima ediliyor (doğrulanmadı). https://openai.github.io/openai-agents-python/handoffs/ — AS-OF 2026-09-09
- **B16 — D** — Anthropic context editing: API yanıtında `context_management.applied_edits` alanı yapılandırılmış geri-bildirim döndürüyor — `type: "clear_tool_uses_20250919"`, `cleared_tool_uses` (temizlenen çift sayısı), `cleared_input_tokens` (serbest kalan token). Bu, devir sonrası "ne yapıldığının" yapılandırılmış dönüş-notu örneği. https://platform.claude.com/docs/en/build-with-claude/context-editing — AS-OF 2026-09-09 (birincil, WebFetch)
- **B17 — D** — Claude Code subagent: ana oturuma dönen şey "yalnız nihai özet" (`returns only its final summary`) — yapılandırılmış şema değil, serbest metin. Alt-ajan transkripti kendi bağlamında kalıcı kalır, ana pencere compact olduğunda etkilenmez. https://code.claude.com/docs/en/context-window — AS-OF 2026-09-09 (birincil, WebFetch)
- **B18 — X** — LangGraph `Command` geri-dönüş şeması için birincil sayfa açılmadı; arama-özetinde geri-dönüş formatına dair somut şema bulunamadı. AS-OF 2026-09-09
- **B19 — X** — MemGPT/Letta'da devredilen alt-ajan/alt-süreçten ana sürece "dönüş notu" formatına dair arama-özetinde bilgi bulunamadı; kaynak sayfa açılmadı. AS-OF 2026-09-09

## 3. Açılan Kaynaklar (WebFetch ile fiilen açılan birincil kaynaklar)
1. https://openai.github.io/openai-agents-python/handoffs/ (OpenAI Agents SDK resmi doküman)
2. https://platform.claude.com/docs/en/build-with-claude/context-editing (Anthropic resmi doküman)
3. https://code.claude.com/docs/en/context-window (Claude Code resmi doküman)

## 4. AÇIK SORULAR
- AÇIK SORU: Claude Code model-başına varsayılan auto-compact eşiği (örn. "%XX doluluk") sayısal değeri — `model-config#default-auto-compact-thresholds` sayfası bu koşumda açılmadı.
- AÇIK SORU: LangGraph handoff'larının birincil sayfası (`docs.langchain.com/oss/python/langchain/multi-agent/handoffs`) açılmadı — Command(goto) geri-dönüş şeması ve devir-anı eşiği doğrulanmadı.
- AÇIK SORU: Letta/MemGPT birincil sayfası (`docs.letta.com/concepts/memory-management/`) açılmadı — özyinelemeli özetleme tetikleyen sayısal token eşiği doğrulanmadı.
- AÇIK SORU: Anthropic "agentic memory" (structured note-taking) birincil cookbook sayfası açılmadı — dosya-pointer devir biriminin tam mekanizması (hangi tool, hangi format) doğrulanmadı.
