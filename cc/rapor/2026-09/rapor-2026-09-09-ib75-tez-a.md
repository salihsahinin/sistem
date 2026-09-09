# IB-75 Tez A — Statik/tanımlı lider (orkestratör/ekip-lideri) desenleri

**Aile:** A (statik/tanımlı lider desenleri) | **Model:** Sonnet 5 (işçi) | **Tarih:** 2026-09-09 | **Açılan birincil kaynak sayısı:** 2 (WebFetch ile fiilen açıldı)

## İddia Listesi

**A1.** Claude Code subagent'ları `.claude/agents/*.md` (proje) ya da `~/.claude/agents/*.md` (kullanıcı) altında YAML frontmatter + Markdown gövde olarak tanımlanır; zorunlu alanlar yalnız `name` ve `description`, opsiyonel alanlar arasında `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`, `skills`, `mcpServers`, `hooks`, `memory`, `background`, `effort`, `isolation`, `color` vardır. — **D** — https://code.claude.com/docs/en/sub-agents — AS-OF 2026-09-09 (çekim tarihi)

**A2.** `description` alanı, ana Claude'un otomatik delegasyon kararı için rota-ipucu olarak kullanılır; birleşik açıklamalar 15.000 token'ı aşarsa uyarı tetiklenir. — **D** — https://code.claude.com/docs/en/sub-agents — AS-OF 2026-09-09

**A3.** Varsayılan (fork-olmayan) subagent DURUMSUZDUR: her çağrı taze bağlamla başlar (kendi sistem promptu, ortam bilgisi, CLAUDE.md, git durumu, ön-yüklü skill'ler, delege görev mesajı); önceki konuşma geçmişi, daha önce okunmuş dosyalar, çağrılmış skill'ler, ana konuşmanın oto-hafızası dahil DEĞİLDİR. `fork` istisnadır: tüm ebeveyn konuşmasını (mesaj geçmişi dahil) devralır. — **D** — https://code.claude.com/docs/en/sub-agents — AS-OF 2026-09-09

**A4.** Subagent tanımı statik konfigürasyondur: başlangıçta bir kez tanımlanır, değişiklikler yeniden yükleme gerektirir (`.claude/agents/` ve `~/.claude/agents/` dosya değişiklikleri izlenir ama yeni dizinler için yeniden başlatma gerekir). — **D** — https://code.claude.com/docs/en/sub-agents — AS-OF 2026-09-09

**A5.** CrewAI hiyerarşik süreçte iki yapılandırma yolu vardır: `manager_llm` (otomatik yönetici agent oluşturur) ya da `manager_agent` (özel tanımlı, `role`/`goal`/`backstory`/`allow_delegation`/`tools` alanlarına sahip özel agent). — **D** — https://docs.crewai.com/en/learn/hierarchical-process — AS-OF 2026-09-09

**A6.** CrewAI'de delegasyon varsayılan olarak KAPALIDIR; kullanıcı işçi agent'larda `allow_delegation=False` ayarlayarak delegasyon döngülerini önler; bu explicit kontrol amacıyla değiştirilmiştir. — **D** — https://docs.crewai.com/en/learn/hierarchical-process — AS-OF 2026-09-09 [not: kaynak sayfası kesin sürüm/tarih vermiyor, WebFetch özet çıktısında geçiyor]

**A7.** CrewAI dokümantasyonu, yönetici agent'ın görevler arası hafıza/durum taşıyıp taşımadığını ve işçi agent'lara tam olarak neyin aktarıldığını AÇIKÇA belirtmiyor (dokümantasyon boşluğu). — **D** (boşluğun kendisi doğrulandı) — https://docs.crewai.com/en/learn/hierarchical-process — AS-OF 2026-09-09

**A8.** CrewAI'de yönetici agent, işçi agent listesine (`agents=[...]`) DAHİL EDİLMEMELİDİR — işçi havuzunun dışında çalışır. — **K** — arama özeti, GitHub PR #2068 / discussion #1220 bağlamında — AS-OF 2026-09-09 [teyide muhtaç, birincil kaynak fiilen açılmadı]

**A9.** GitHub Issue #4783'e göre CrewAI hiyerarşik süreçte, `allow_delegation=True` ayarlanmış olsa bile yönetici agent'ların işçi agent'lara görev delege edemediği bildirilmiş (bilinen hata/uygulama sorunu). — **K** — https://github.com/crewAIInc/crewAI/issues/4783 — AS-OF 2026-09-09 [issue açık mı kapalı mı, hangi sürümde doğrulanmadı]

**A10.** `langgraph-supervisor` kütüphanesinde supervisor merkezi bir agent olarak tüm iletişim akışını ve görev delegasyonunu kontrol eder; "handoff tool" adlı araçlar üzerinden işçi agent'lara kontrolü (ve mesaj geçmişini) devreder; `create_handoff_tool` fonksiyonu `agent_name`, `name`, `description` parametreleriyle özelleştirilir; varsayılan olarak TÜM mesaj geçmişini işçiye aktarır. — **K** — https://github.com/langchain-ai/langgraph-supervisor-py — AS-OF 2026-09-09 [arama özeti; birincil kaynak fiilen açılmadı]

**A11.** AutoGen Magentic-One'ın Orchestrator agent'ı bir plan oluşturur, görevleri diğer agent'lara (FileSurfer, WebSurfer, Coder, ComputerTerminal) delege eder ve hedefe ilerlemeyi izler, gerektiğinde planı dinamik olarak revize eder; kod tabanında `MagenticOneOrchestrator` sınıfı `BaseGroupChatManager`'ı genişletir ve agent koordinasyonu, mesaj yönlendirme, DURUM YÖNETİMİ yapar (yani orchestrator durum taşır, statik değildir). — **K** — https://microsoft.github.io/autogen/stable//user-guide/agentchat-user-guide/magentic-one.html — AS-OF 2026-09-09 [arama özeti; birincil kaynak fiilen açılmadı]

**A12.** OpenAI Agents SDK'da iki farklı orkestrasyon deseni var: "Manager (agents-as-tools)" — merkezi bir yönetici agent uzman alt-agent'ları ARAÇ olarak çağırır ve konuşma kontrolünü ELİNDE TUTAR; "Handoffs" — eş agent'lar arası kontrol devri, seçilen uzman kalan tur boyunca konuşmayı DEVRALIR. Handoff'lar LLM'e araç olarak sunulur (örn. `transfer_to_refund_agent`); her agent'ın bir `handoffs` parametresi vardır (Agent nesnesi ya da özelleştirilmiş Handoff nesnesi alır). — **K** — https://openai.github.io/openai-agents-python/multi_agent/ ve https://openai.github.io/openai-agents-python/handoffs/ — AS-OF 2026-09-09 [arama özeti; birincil kaynak fiilen açılmadı]

## Açılan Kaynaklar (WebFetch ile fiilen açılan, D etiketli)

1. https://code.claude.com/docs/en/sub-agents — Claude Code resmi dokümantasyon (subagents)
2. https://docs.crewai.com/en/learn/hierarchical-process — CrewAI resmi dokümantasyon (hierarchical process)

## AÇIK SORU:

- AÇIK SORU: LangGraph `create_handoff_tool` ve supervisor'ın durum (state) modeli birincil kaynaktan (langgraph-supervisor-py README/reference.langchain.com) doğrulanmadı — yalnız arama özetine dayanıyor (A10).
- AÇIK SORU: AutoGen Magentic-One Orchestrator'ın "durum taşıma" iddiası (A11) yalnız arama özetinden; `MagenticOneOrchestrator` kaynak kodu (GitHub `_magentic_one_orchestrator.py`) fiilen açılıp hangi state alanlarının tutulduğu (plan, ledger, progress) satır düzeyinde doğrulanmadı.
- AÇIK SORU: OpenAI Agents SDK'da manager/handoff desenlerinin agent tanım ALANLARI (instructions, tools, handoff_description gibi) birincil kaynaktan (openai.github.io/openai-agents-python/agents/) fiilen doğrulanmadı — yalnız arama özetine dayanıyor (A12).
- AÇIK SORU: CrewAI'de yönetici agent'ın işçi havuzuna dahil edilmemesi kuralı (A8) ve delegasyon hatası (A9) birincil kaynaktan değil, GitHub issue/PR arama özetinden geliyor; issue'nun güncel durumu (açık/kapalı/çözüldü mü) doğrulanmadı.
- AÇIK SORU: Hiçbir kaynakta "lider rol metninin DURUM TAŞIMAYIP TAŞIMADIĞI" karşılaştırmalı bir tablo halinde yok; bu sentez tez-B (antitez) ve hakem aşamasında derlenmeli.
