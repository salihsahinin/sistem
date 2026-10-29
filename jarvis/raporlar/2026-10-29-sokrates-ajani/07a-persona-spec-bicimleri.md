# 07a Persona spec biçimleri (Atlas V1, AS-OF 2026-10-29, canlı; Jarvis kaydetti, ajan dosya yazmadı)

## Standartlar tablosu
| Ad | Kaynak | Alanlar | Biçim | Yaygınlık |
|---|---|---|---|---|
| Character Card V2 | https://github.com/malfoyslastname/character-card-spec-v2/blob/main/spec_v2.md | name, description, personality, scenario, first_mes, mes_example, system_prompt, post_history_instructions, alternate_greetings, character_book, creator_notes, tags, extensions | Tek JSON (`spec`, `spec_version`, `data`) | 199 yıldız, son push 2023-06; fiili standart |
| Character Card V3 | https://github.com/kwaroran/character-card-spec-v3/blob/main/SPEC_V3.md | V2 + assets, nickname, group_only_greetings, source, creation_date; lorebook `use_regex`, `@@` dekoratör | JSON, PNG `ccv3` chunk, CHARX zip | 114 yıldız, 2024-07 |
| SillyTavern | https://docs.sillytavern.app/usage/core-concepts/characterdesign/ · worldinfo/ | V2 + Character's Note (depth prompt), talkativeness | V2/V3 kartı + ayrı lorebook | 35.088 yıldız, 2026-10-02 |
| Claude Code subagent | https://code.claude.com/docs/en/sub-agents | name, description zorunlu; tools, disallowedTools, model, memory, skills, hooks, effort, omitClaudeMd, initialPrompt | YAML frontmatter + md gövde (= system prompt) | yerleşik |
| CrewAI | https://docs.crewai.com/en/concepts/agents | role, goal, backstory; system/prompt/response_template | Python ya da `agents/*.jsonc` | 60.248 yıldız |
| Letta/MemGPT | https://docs.letta.com/guides/agents/memory-blocks | memory block: label, description, value, limit, read_only; `persona` + `human` | yapısal blok, prompta XML | 25.288 yıldız |
| OpenAI Agents SDK | https://openai.github.io/openai-agents-python/agents/ | name, instructions (statik/fonksiyon), handoff_description, handoffs, tools, guardrails | Python; "persona" kavramı yok | 30.375 yıldız |
| AutoGen | https://microsoft.github.io/autogen/stable/reference/python/autogen_agentchat.agents.html | name, system_message, description, memory | Python | 61.620 yıldız |
| Semantic Kernel | https://learn.microsoft.com/en-us/semantic-kernel/concepts/prompts/yaml-schema | name, description, template, input_variables, execution_settings | YAML; persona `template` içinde | 28.716 yıldız |
| RoleLLM | https://arxiv.org/abs/2310.00746 | 100 rol profili; RoleBench 168.093 örnek | veri + ince ayar | 535 yıldız |
| Character-LLM | https://arxiv.org/html/2310.10158v2 | profil, sahne, deneyim, **koruyucu sahne** (bilgi sınırı) | ince ayar, karakter başına model | yıldız X |

Anthropic: rol promptu (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices); karakter koruma "Keep Claude in character" (https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency): kişilik + geçmiş + huylar ayrıntılı, olası senaryolar ve beklenen cevaplar listesi; prefill Claude 4.6+ desteklenmiyor.

## Ortak alan kümesi
- Her yerde: kimlik (ad, rol, geçmiş) + davranış/ton.
- Çoğunda: örnek diyalog (mes_example), açılış mesajı (first_mes), araç/izin listesi.
- Yalnız kart ekosisteminde: lorebook (anahtarla tetiklenen bilgi), post-history instructions, depth prompt.
- Hiçbir şemada birinci sınıf alan değil: **bilgi sınırı, yasaklar, çıkış kuralı** (serbest metin). Tek istisna Character-LLM koruyucu sahne (dönem dışı soruda şaşkınlık; Beethoven'a Python sorulunca ret).
- Drift: ContextEcho (https://arxiv.org/pdf/2605.24279) periyodik kimlik yeniden beyanı; Assistant Axis (https://arxiv.org/abs/2601.10387) meta-yansıma ve duygusal konuşmalarda drift [K].

## Sokrates için öneri (ajan çıkarımı)
Mevcut yapı zaten subagent biçimi. Üstüne V2 alan adlarını gövde bölümü olarak koymak en ucuz yol: kimlik (description) · konuşma stili + yöntem (personality) · senaryo · **örnek diyaloglar (mes_example)** · kısa hatırlatma (post-history karşılığı) · yasaklar + çıkış. Eksikler: bilgi sınırı için koruyucu örnekler (modern konuya şaşkınlık örnekleri), örnek diyalog bölümü, dışa aktarım için V2 `data` eşlemesi (gerekirse).

## D/K/X
D: V2/V3, SillyTavern, subagent, CrewAI, Letta, SDK, AutoGen alanları, Character-LLM mekanizması, yıldızlar. K: RoleLLM profil biçimi; ContextEcho ve Assistant Axis özetten. X: CharacterGLM alanları, LangGraph persona belgesi, Character-LLM/CharacterEval yıldızları (404).
