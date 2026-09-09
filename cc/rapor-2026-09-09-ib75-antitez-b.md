# ATLAS Antitez Raporu — IB-75 Grup B (Bağlam Devri) + Grup C (Yetki Sınırı)

## 1. Künye
- Rol: Antitez işçisi (Devil's Advocate) — karar yetkisi yok
- Tarih (AS-OF): 2026-09-09
- Araç çağrısı sayısı: 12 (WebSearch x8, WebFetch x4 — 4 birincil kaynak fiilen açıldı: arXiv 2505.06120, Chroma context-rot raporu, Trail of Bits blog, arXiv 2606.02875)
- Yazma izni: yalnız bu dosya; git komutu kullanılmadı

## 2. İddia Başına Hüküm

### B1 — "Budayarak/filtreleyerek devir işler, bilgi kaybı yönetilebilir"
**DARALTILDI (yönetilebilirlik iddiası zayıf destekli).**
- D: Handoff/devir sonrası hata taksonomisi (AgentAsk) dört hata tipi çıkarıyor: Data Gap %29.1, Referential Drift %27.3, Signal Corruption %36.8, Capability Gap %6.8 — https://arxiv.org/pdf/2510.07593 — AS-OF 2026-09-09 [arama sonucundan, PDF fiilen açılmadı → K]
- K: "Agent B might receive... instead of a focused summary, miss critical context Agent A discovered but didn't surface" — pratikte devir kayıpları belgeleniyor — https://xtrace.ai/blog/ai-agent-context-handoff — AS-OF 2026-09-09
- Yorum: "yönetilebilir" iddiası mutlak DEĞİL; kayıp oranları görev-bağımlı ve ölçülmüş, sıfır değil. İddia tam çürütülmedi ama "yönetilebilir" niteliği kanıtla desteklenmedi — kaynağın sadece kayıp olduğunu, yönetilebilirlik derecesini ölçmediğini gösteriyor.

### B3 — "Otomatik sıkıştırma/özetleme uzun koşumlarda kaliteyi korur"
**ÇÜRÜTÜLDÜ.**
- D: "LLMs Get Lost In Multi-Turn Conversation" (Laban, Hayashi, Zhou, Neville — Microsoft Research/Salesforce, ICLR 2026 Best Paper) — 200.000+ simüle konuşmada, tüm test edilen açık/kapalı model ailelerinde çok-turlu performans tek-turluya göre ortalama %39 düşüyor; düşüşün asıl kaynağı "aptitude loss" değil "unreliability" artışı — https://arxiv.org/abs/2505.06120 — AS-OF 2026-09-09 (WebFetch ile fiilen açıldı)
- D: Fixed-interval/token-eşikli compaction "trajectory structure"ı göz ardı eder; mid-derivation/mid-search'te ateşlenirse modelin hesapladığı ara sonuçları atar ve yeniden hesaplattırır; "summarization-based compaction"ın 4 bilinen sınırı: kayıplılık öngörülemez (özetleyici LLM'in anlık saliency yargısına bağlı), yapı yok edilir (araç-çağrısı→çıktı→karar nedensel zinciri düzyazıya çöker) — https://arxiv.org/html/2606.23525v2 (Self-Compacting Language Model Agents) — AS-OF 2026-09-09 [arama özetinden → K]
- Sonuç: "kaliteyi korur" iddiası doğrudan ters yönde kanıtlanıyor: özetleme hem genel görev başarısızlığını hem de ara-hesap kaybını artırıyor.

### B6 — "Alt-ajanın ayrı bağlam penceresi ana ajanın bağlamını etkili biçimde küçültür"
**DARALTILDI.**
- K: Orkestratör alt-ajanın kendi penceresini büyütmese de, geri dönen özetleri işlemek zorunda; "every subagent bills tokens independently... orchestrator still incurs token costs from receiving and processing summaries from each sub-agent's work"; koordinasyon 3-4 paralel alt-ajanın ötesinde "clutter" biriktiriyor — https://www.augmentcode.com/guides/ai-agent-loop-token-cost-context-constraints — AS-OF 2026-09-09
- K: Ölçülen dağılım: planlama/orkestrasyon katmanı toplam token'ın ~%9.8'i, işçi ajanlar %70.6'sı — koordinatör bunun üzerine çıkarsa "context'i delege etmesi gerektiği" belirtiliyor (yani küçülme garanti değil, disiplin gerektiriyor) — aynı kaynak — AS-OF 2026-09-09
- Yorum: Ana bağlamın "etkili biçimde" küçüldüğü koşullu — ölçek arttıkça (>3-4 paralel ajan) fayda azalıyor, maliyet çarpanı doğuruyor. Tam çürütme değil; koşulsuzluk iddiası çürütülüyor.

### B9 — "Sabit sayısal eşikte (~100K token) otomatik devir tetiklemek doğru tasarım"
**ÇÜRÜTÜLDÜ.**
- D: "Existing scaffolds mitigate context growth with fixed-interval compaction triggered at a token threshold. Such triggers pay no heed to trajectory structure, risking discard of partial results mid-derivation or mid-search... Firing mid-derivation or mid-search is the worst case." Önerilen alternatif (SelfCompact): eşik yerine görev-durumuna duyarlı tetik (alt-görev bitti mi / trajectory yakınsıyor mu) — https://arxiv.org/html/2606.23525v2 — AS-OF 2026-09-09
- K: "Context Compaction Is a Decision, Not a Threshold" başlığı, aynı tezi doğrudan savunuyor (başlıktan çıkarım, içerik fiilen açılmadı) — https://blakecrosley.com/blog/agent-context-compaction — AS-OF 2026-09-09
- Sonuç: sabit eşik tasarımı literatürde açıkça "en kötü durum" olarak işaretleniyor; görev-sınırı kesme riski isim verilerek belgelenmiş.

### B17 — "Alt-ajanın serbest-metin özet döndürmesi yeterlidir"
**ÇÜRÜTÜLDÜ (koşullu).**
- D: "Handoff Debt: The Rediscovery Cost When Coding Agents Take Over Interrupted Tasks" — raw trace / summary notes / structured notes karşılaştırması; structured notes daha düşük hata oranı veriyor, "context-bearing handoffs consistently reduce rediscovery effort across successor models" — https://arxiv.org/pdf/2606.02875 — AS-OF 2026-09-09 (WebFetch ile fiilen açıldı; PDF sıkıştırılmış geldiği için sayısal oranlar net çıkarılamadı → D ama sayısal detay [?])
- K: "If the handoff format isn't designed deliberately, the orchestrator has to guess at the structure — and guessing introduces errors" — https://www.mindstudio.ai/blog/what-is-agent-handoff-pattern — AS-OF 2026-09-09
- K: Yapılandırılmış çıktı bile mükemmel değil — şema uyumu neredeyse tam ama değer-doğruluğu metinde %83.0, görselde %67.2, seste %23.7'ye düşüyor, uzun bağlamda çıkarım zorlaşıyor — https://arxiv.org/html/2604.25359v1 — AS-OF 2026-09-09 [arama özetinden → K]
- Sonuç: serbest-metin özet, yapılandırılmış nota göre ölçülebilir biçimde daha yüksek hata/rediscovery maliyeti taşıyor; "yeterlidir" iddiası çürütülüyor, ama "yapılandırılmış" da mutlak çözüm değil (uzun bağlamda kendi doğruluk kaybı var).

### C1/C2/C3 — "Guardrail/tripwire, interrupt (insan-onay), allow_delegation=False lider ajanın yetkisini etkili sınırlar"
**ÇÜRÜTÜLDÜ (interrupt/guardrail için somut vaka); C3 (allow_delegation) için ÇÜRÜTÜLEMEDİ.**
- D: Trail of Bits — "argument injection" ile pre-approved (allowlisted) komutlara (go test, git, ripgrep) kötü amaçlı bayrak enjekte edilerek insan-onay adımı hiç tetiklenmeden RCE elde edildi: "Because `go test` is considered a safe command, the exploit runs without requiring human approval." Üç ayrı ajan platformunda "one-shot" RCE. İlgili önceki vakalar: Amazon Q RCE (2025-08), Claude Code CVE-2025-54795, Cursor GHSA-534m-3w6r-8pqr — https://blog.trailofbits.com/2025/10/22/prompt-injection-to-rce-in-ai-agents/ — AS-OF 2025-10-22 (yayın), erişim 2026-09-09 (WebFetch ile fiilen açıldı)
- D: OpenAI Guardrails Framework (2025-10-06 yayın) — saldırgan hem üretici modeli hem "safety judge"ı aynı anda manipüle edebiliyor; judge'a düşük güven skoru raporlatan şablon enjekte edilerek zararlı çıktı uyarısız geçiyor — https://cybersecuritynews.com/openai-guardrails-bypassed/ — AS-OF 2026-09-09
- K: "Adversarial testing consistently finds bypasses within weeks of new guardrails being deployed... one study evaded six commercial systems... 100 percent evasion in certain cases" — aynı arama sonucu — AS-OF 2026-09-09
- C3 için: CrewAI `allow_delegation=False` özelinde bir "bypass" tekniği/vakası bulunamadı; bulunan sorunlar tersine — hiyerarşik delegasyonun `allow_delegation=True` iken bile ÇALIŞMAMASI (fonksiyonel bug, güvenlik açığı değil) — https://github.com/crewAIInc/crewAI/issues/4783 — AS-OF 2026-09-09. Bu, C3'ü YANLIŞLAMIYOR; kısıtın atlatıldığına dair kanıt YOK.

### C4 — "Araç/izin allowlist'i ve PreToolUse denetimi ajan davranışını güvenilir biçimde kısıtlar"
**ÇÜRÜTÜLDÜ.**
- D: Aynı Trail of Bits vakası doğrudan bu iddiayı hedef alıyor — allowlist'teki komutlara argüman enjeksiyonu ("facade pattern weakness": kullanıcı girdisi argüman ayracı olmadan eklenince `-x=python3` gibi enjekte parametreler davranışı değiştiriyor) — https://blog.trailofbits.com/2025/10/22/prompt-injection-to-rce-in-ai-agents/ — AS-OF 2026-09-09
- Not: Makalede PreToolUse'a özgü bir mekanizma tartışılmıyor (Claude Code hook'u spesifik olarak test edilmemiş) — bu bir GENELLEME BOŞLUĞU, işaretleniyor.

### C5 — "Özyineleme/adım tavanı delegasyon derinliği için yeterli fren"
**ÇÜRÜTÜLDÜ.**
- D: "recursion and iteration limits are backstops that fire after the budget is already spent, so they turn a stuck run into a wasted one instead of catching it early"; LangGraph varsayılan recursion_limit=25, LangChain max_iterations=15 yalnız toplam adımı sınırlar, TEKRARI sınırlamaz — https://machinelearningplus.com/gen-ai/langgraph-cycles-recursion-limits-agent-loops/ — AS-OF 2026-09-09 [arama özetinden → K]
- K: "A single runaway agent loop can consume thousands of dollars in API costs within minutes" — tavan devreye girene kadar maliyet birikebiliyor — aynı kaynak — AS-OF 2026-09-09
- K: Önerilen düzeltme "no-progress guard" (tekrarlayan tool/args/error üçlüsünü hash'leyip erken durdurma) — tavanın kendisi bunu YAPMIYOR — GitHub Issue #6731 (langchain-ai/langgraph) canlı bug örneği — AS-OF 2026-09-09

## 3. Açılan Kaynaklar (WebFetch ile fiilen)
1. https://arxiv.org/abs/2505.06120 (LLMs Get Lost in Multi-Turn Conversation) — AS-OF 2026-09-09
2. https://www.trychroma.com/research/context-rot — AS-OF 2026-09-09
3. https://blog.trailofbits.com/2025/10/22/prompt-injection-to-rce-in-ai-agents/ — AS-OF 2026-09-09
4. https://arxiv.org/pdf/2606.02875 (Handoff Debt) — AS-OF 2026-09-09 (PDF sıkışık geldi, sayısal tablo net çıkmadı)

## 4. AÇIK SORULAR
- AÇIK SORU: B1 için "yönetilebilirlik derecesi" ölçen doğrudan bir çalışma bulunamadı; AgentAsk taksonomisi PDF olarak fiilen açılmadı (yalnız arama özeti) — doğrulama eksik.
- AÇIK SORU: C3 (`allow_delegation=False` bypass) için doğrudan yanlışlayan kanıt yok — bu madde ÇÜRÜTÜLEMEDİ olarak kaydedilmeli, C1/C2 ile aynı torbaya konmamalı.
- AÇIK SORU: C4'te PreToolUse'a (Claude Code'a özgü hook mimarisi) özel bir bypass vakası bulunamadı; genel allowlist-argument-injection deseninin PreToolUse'a aktarılabilirliği doğrulanmadı [?].
- AÇIK SORU: Handoff Debt makalesinin (arXiv 2606.02875) tam sayısal tabloları PDF sıkıştırma nedeniyle çıkarılamadı; rakamlar teyit gerektirir.
- AÇIK SORU: B6'daki "%9.8 orkestrasyon / %70.6 işçi" oranı hangi çalışmadan geldiği (birincil kaynak adı) arama özetinde belirtilmedi — kaynak izlenebilirliği zayıf [?].
