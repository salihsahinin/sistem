# Atlas ANTİTEZ Raporu — Aile D (ajan sınıfları, hafıza, model katmanlaması)

**Tarih:** 2026-09-18 · **Rol:** Devil's-Advocate (¬T savunması) · **Dil:** Türkçe

Yöntem notu: her iddia için lojiksel TERS (¬T) için birincil kanıt arandı. Bulunan kanıt çoğu iddiada ¬T'yi değil, orijinal T'yi doğruladı — bu da meşru bir antitez sonucudur (ÇÜRÜDÜ = ¬T çürüdü, T sağlam durdu). Süs-antitez üretilmedi; gerçekten çürütülemeyen/daraltılan maddeler de var.

---

## 1. "Subagent'lar varsayılan hafızasız, her çağrı taze bağlam"
**¬T kanıtı aranan:** subagent'lar varsayılan olarak kalıcı hafızalıdır.
**Bulgu:** Resmî dok: "Each Claude Code session begins with a fresh context window" ve "The main conversation's auto memory isn't loaded into subagents; the exception is a fork." ¬T'yi destekleyen kanıt yok.
**Kaynak:** [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) · AS-OF: çekim 2026-09-18, doküman güncel sürüm (v2.1.2xx serisi referanslı) · **Hüküm: ÇÜRÜDÜ**

## 2. "`memory: user/project/local` alanı kalıcı dizin + MEMORY.md verir"
**Bulgu:** Dok. doğrudan doğruluyor: `memory` alanı `~/.claude/agent-memory/<ad>/` (user), `.claude/agent-memory/<ad>/` (project), `.claude/agent-memory-local/<ad>/` (local) verir; her dizinde kendi MEMORY.md indeksi. ¬T kanıtı yok — bilakis GitHub Issue #31294 özelliğin **var olduğunu** ama bazı sürümlerde bozuk çalıştığını gösteriyor (uygulama hatası, tasarım iddiasını çürütmüyor).
**Kaynak:** [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) (Enable persistent memory bölümü) · AS-OF: çekim 2026-09-18 · **Hüküm: ÇÜRÜDÜ**

## 3. "MEMORY.md'nin ilk 200 satırı/25 KB'ı sistem promptuna enjekte edilir"
**Bulgu:** Birebir alıntı: "The subagent's system prompt also includes the first 200 lines or 25KB of MEMORY.md in the memory directory, whichever comes first." Not: ana-konuşma auto-memory'si CLAUDE.md gibi "user message" olarak yüklenir (sistem promptu değil) — ama **subagent MEMORY.md'si** açıkça "system prompt"a eklendiği belirtiliyor; iddia mekanizma bakımından isabetli.
**Kaynak:** [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) · AS-OF: çekim 2026-09-18 · **Hüküm: ÇÜRÜDÜ**

## 4. "Bellek etkin subagent'larda Read/Write/Edit otomatik açılır"
**Bulgu:** Birebir alıntı: "Read, Write, and Edit tools are automatically enabled so the subagent can manage its memory files." ¬T (elle açılması gerekir) için kanıt yok.
**Kaynak:** [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) · AS-OF: çekim 2026-09-18 · **Hüküm: ÇÜRÜDÜ**

## 5. "Bellek dizinleri ajan-başına ayrıdır, birbirini görmez"
**Bulgu:** Dok: "Agents cannot access each other's memory directories. This isolation is by design." ¬T (paylaşımlı görünürlük) kanıtı yok; aksine Hindsight blog yazısı bu izolasyonu bir **eksiklik** olarak eleştiriyor ("subagents don't share what they learn") — bu eleştiri de izolasyon iddiasını doğruluyor, çürütmüyor.
**Kaynak:** [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) + [hindsight.vectorize.io](https://hindsight.vectorize.io/blog/2026/05/06/claude-code-subagents-shared-memory) (AS-OF yayın 2026-05-06) · çekim 2026-09-18 · **Hüküm: ÇÜRÜDÜ**

## 6. "Model çözümleme sırası: çağrı parametresi > frontmatter model > CLAUDE_CODE_SUBAGENT_MODEL > ana model"
**Bulgu:** Dok. birebir bu sırayı doğruluyor (v2.1.251+): "1. The per-invocation model parameter 2. The subagent definition's model frontmatter... 3. CLAUDE_CODE_SUBAGENT_MODEL... 4. The main conversation's model." Ancak GitHub Issue #10993 (closed as not-planned) eski davranışı farklı tarif ediyor: kullanıcı raporuna göre önceki sürümlerde `CLAUDE_CODE_SUBAGENT_MODEL` **her şeyi override ediyordu** (frontmatter'ı yok sayıyordu) — yani sıralama sürüme bağlı, zamana göre değişmiş. Bu, iddiayı tümüyle çürütmüyor ama "evrensel/değişmez sıra" izlenimini daraltıyor.
**Kaynak:** [code.claude.com/docs/en/model-config](https://code.claude.com/docs/en/model-config) (çekim 2026-09-18, v2.1.251+) + [github.com/anthropics/claude-code/issues/10993](https://github.com/anthropics/claude-code/issues/10993) (eski davranış raporu, kapatıldı) · **Hüküm: DARALDI** (sıra doğru ama sürüm-bağımlı; öncesinde farklıydı)

## 7. "Opus 4 lider + Sonnet 4 işçi, tek-ajan Opus 4'e göre %90,2 iyileşme (eski kuşak)"
**Bulgu:** Anthropic'in orijinal mühendislik yazısı bu rakamı doğruluyor: multi-agent sistem (LeadResearcher: Opus 4, Subagents: Sonnet 4) tek-ajan Opus 4'e göre %90,2 daha iyi performans. İddia zaten "eski kuşak ölçüm" diye etiketlenmiş, bu doğru — Opus 4/Sonnet 4, 2026-09 itibarıyla eski kuşak (Opus 5/Sonnet 5 sonrası).
**Kaynak:** [anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system) · AS-OF: yazı ilk yayın ~2025 ortası, çekim 2026-09-18 · kuşak: Opus 4 / Sonnet 4 · **Hüküm: ÇÜRÜDÜ**

## 8. "Sonnet 4'e geçmek, Sonnet 3.7'de token bütçesini ikiye katlamaktan daha kazançlı"
**Bulgu:** Birebir alıntı: "upgrading to Claude Sonnet 4 is a larger performance gain than doubling the token budget on Claude Sonnet 3.7." ¬T kanıtı yok.
**Kaynak:** [anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system) · AS-OF: çekim 2026-09-18 · kuşak: Sonnet 3.7 → Sonnet 4 · **Hüküm: ÇÜRÜDÜ**

## 9. "Çok-ajanlı sistem sohbete göre ~15×, tek ajan ~4× token tüketir"
**Bulgu:** Birebir alıntı: "agents typically use about 4× more tokens than chat interactions" ve "multi-agent systems use about 15× more tokens than chats." Rakamlar tam eşleşiyor.
**Kaynak:** [anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system) · AS-OF: çekim 2026-09-18 · **Hüküm: ÇÜRÜDÜ**

## 10. "DeepTutor (2026-04) kalıcı öğrenci modeli gerektiğini, mevcut ajan çerçevelerinin bunu karşılamadığını savunur"
**Bulgu:** Makale (v1: 2026-04-10, güncel v3: 2026-07-09) gerçekten kalıcı/dinamik öğrenen hafızası (dynamic learner memory) savunuyor ve genel LLM'lerin "güncel bilgiye ve bireysel öğrenenlere uyum eksikliği"nden, RAG sistemlerinin kişiselleştirilmiş rehberlik sağlayamamasından bahsediyor. Ama metin **spesifik ajan çerçevelerini (Claude Code, LangChain vb.) doğrudan eleştirmiyor** — iddiadaki "mevcut ajan çerçevelerinin bunu karşılamadığını savunur" kısmı orijinal makalede bu netlikte yok; genel LLM/RAG eleştirisi var, çerçeve-düzeyinde karşılaştırma yok.
**Kaynak:** [arxiv.org/abs/2604.26962](https://arxiv.org/abs/2604.26962) "DeepTutor: Towards Agentic Personalized Tutoring" · AS-OF: v1 2026-04-10, v3 2026-07-09, çekim 2026-09-18 · **Hüküm: DARALDI**

## 11. "Claude Code'da tutor'a özgü ayrı ajan sınıfı yok; `memory` özelliği role bağımsız"
**Bulgu:** Dok. `memory` alanını herhangi bir subagent tanımına eklenebilen genel bir frontmatter alanı olarak tarif ediyor (`code-reviewer`, `db-agent` gibi örnekler; tutor'a özgü ayrı sınıf/mekanizma yok). ¬T (tutor-özel sınıf var) kanıtı bulunamadı.
**Kaynak:** [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) · AS-OF: çekim 2026-09-18 · **Hüküm: ÇÜRÜDÜ**

## 12. "arXiv 2606.30306'nın gövdesi erişilebilir değildir"
**Bulgu:** Doğrudan çürütüldü — hem `/abs/2606.30306` hem `/pdf/2606.30306` gerçekten açıldı, 403/paywall yok. Makale: "Always-On Agents: A Survey of Persistent Memory, State, and Governance in LLM Agents" (Ding, Nannapaneni, Liu, Zhang), CC-BY 4.0, 435+ eser taranmış, cs.MA/cs.AI. PDF içeriği tool-results dizinine indi (2.6MB), tam metin okunabilir durumda.
**Kaynak:** [arxiv.org/abs/2606.30306](https://arxiv.org/abs/2606.30306) + [arxiv.org/pdf/2606.30306](https://arxiv.org/pdf/2606.30306) · AS-OF: gönderim 2026-06-29, çekim 2026-09-18 · **Hüküm: ÇÜRÜDÜ**

---

## Açılan kaynak sayısı
WebFetch ile gerçekten açılan sayfa: **8** — code.claude.com/docs/en/memory, code.claude.com/docs/en/model-config, code.claude.com/docs/en/sub-agents, github.com/anthropics/claude-code/issues/10993, anthropic.com/engineering/multi-agent-research-system, arxiv.org/abs/2604.26962, arxiv.org/abs/2606.30306, arxiv.org/pdf/2606.30306.
