# 07c. GitHub persona/karakter ajanı repoları: dizin yapısı, araç kombinasyonu, iş akışı

**AS-OF 2026-10-29.** Yıldız, lisans, son push değerleri `gh api` ile aynı gün çekildi. Dosya içerikleri `gh api contents` ve resmî doküman sayfalarından okundu. Hiçbir sayı model hafızasından değildir; doğrulanmayanlar `[?]` ile işaretli.
D/K/X okuma varsayımı (bu dosyada): **D** = dosya/dizin doğrudan okundu · **K** = yalnız README/başlık/arama özeti okundu, iç yapı kısmen · **X** = doğrulanamadı ya da iddia düştü.

## 1. Repo tablosu

| # | Repo | Amaç | Yıldız / lisans / son push | Dizin yapısı (prompt · test · veri) | Prompt sürümleme | Test/eval | Arayüz | Çok-turlu hafıza |
|---|---|---|---|---|---|---|---|---|
| 1 | [Caizhen-x/socrates-agent](https://github.com/Caizhen-x/socrates-agent) | Platon diyaloglarından RAG ile Sokrates gibi akıl yürüten Claude Code ajanı | 0 / lisans yok / 2026-05-15 | `CLAUDE.md` (kimlik+biçim), `.claude/agents/socrates.md` (iş akışı), `.claude/rules/character-guardrails.md` (8 sert kural), `.claude/skills/dialectic.md` · `tests/` (4 dosya + `retrieval_gold.yaml`) · `Books/` 27 diyalog, `data/corpus`, `config/*.yaml` | Yalnız git + `HANDOFF.md` + `socrates-improvement-plan.md`; `prompt_stats.jsonl` token bütçesi (`system_max_tokens: 4800`) | Var: `test_character.py` (5 hileli soru + yasak terim listesi), `eval_retrieval.py` (38 soruluk altın küme), `response_validator.py` (regex anakronizm/register denetimi + yeniden deneme), `drift_audit.py` (her 10 seansta LLM denetimi) | CLI döngüsü `scripts/socrates_loop.py`; `app.py` [?] | Var: YAML seans özeti + `summary.yaml` + diyalektik iz; oturum başında bağlam bloğu |
| 2 | [leamas-ai/agents-historical-figures](https://github.com/leamas-ai/agents-historical-figures) | 50 tarihî figür alt-ajanı + `debate-moderator`, Claude Code'da tartışma | 3 / yok / 2025-08-06 | Yalnız `agents/<ad>-agent.md` (frontmatter `name`, `description`; gövde: Core Identity, Method, Key Beliefs, Speaking Style, Common Phrases) | Yok (git) | Yok (test dizini yok) | Claude Code Task aracı | Yok |
| 3 | [bevibing/socrates-skill](https://github.com/bevibing/socrates-skill) | Doğrudan cevap vermeyen Sokratik öğretim skill'i | 342 / MIT / 2026-04-02 | Tek `SKILL.md` + README + LICENSE | Yok | Yok | Claude Code skill (tetik: "socratic", "Socrates") | Yok |
| 4 | [jordaneunson/holodeck](https://github.com/jordaneunson/holodeck) | Figür adından araştır, vektörle, persona profili çıkar, ajan çalışma alanı üret | 3 / yok / 2026-08-21 | `templates/{SOUL,IDENTITY,AGENTS,MEMORY,USER,TOOLS,HEARTBEAT,SKILL}.md.j2` · `src/test.py` · `data/figures/<id>.json` + LanceDB | Üretim betiği şablondan basar; "flavour" varyantı ayrı id (`donald_trump__leftist`) | Var: `holodeck.py test` 3 modda (conversational/expert/creative) LLM puanlı ses tutarlılığı | CLI + OpenClaw kaydı | `MEMORY.md` şablonu + RAG |
| 5 | [giovannigatti/socratic-llm](https://github.com/giovannigatti/socratic-llm) | Phi-3-mini'yi Sokratik yönteme ince ayar | 36 / MIT / 2025-10-10 | `templates/inference.txt` (prompt) · `src/{train,eval_model,self_eval,human_vs_gpt}.py` · `datasets/{debugging,mathdial,tutorchat}_{train,test}.json` | git; eğitim verisi dosyada | Var: prompt-only ve ince ayarlı model karşılaştırması, GPT-4o yargıç [K: arama özeti + ağaç] | `chatbot/socratic_ui.py` + Ollama demosu | Yok [?] |
| 6 | [ChenChenyaqi/learn-anything](https://github.com/ChenChenyaqi/learn-anything) | 30+ kodlama asistanı için Sokratik/TDD öğrenme komutları üretici | 496 / MIT / 2026-08-29 | `openspec/specs/*` (11 spec) + `openspec/changes/archive` · `packages/cli/test` (vitest) · `AGENTS.md`+`CLAUDE.md` | OpenSpec değişiklik arşivi + `CHANGELOG.md` + commitlint | Var ama CLI/site için (CI `ci.yml`); persona kalitesi ölçülmüyor | Slash komutlar + `packages/gui` panosu | Aralıklı tekrar için kayıtlı soru destesi [K] |
| 7 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | Karakter sohbeti için LLM ön yüzü (ekosistem merkezi) | 35088 / AGPL-3.0 / 2026-10-02 | Karakter = "Character Card V2" (`description, personality, scenario, first_mes, mes_example, system_prompt, post_history_instructions, character_book`); `default/content`, `tests/` uygulama içindir | Kartta sürüm alanı [?: spec'te `character_version` bekleniyor, bu oturumda satır doğrulanmadı] | Persona eval yok; yalnız uygulama testleri | Web UI | Sohbet dosyası + lorebook (`world-info.js`); uzantı [muyoou/st-memory-enhancement](https://github.com/muyoou/st-memory-enhancement) 1531 yıldız |
| 8 | [malfoyslastname/character-card-spec-v2](https://github.com/malfoyslastname/character-card-spec-v2) | Kart şeması (de-facto standart) | 199 / yok / 2023-06-22 | `spec_v2.md` (alan listesi, `{{original}}` yer tutucu) | Şema sürümü v2 | Doğrulayıcı kütüphane `character-card-utils` | n/a | n/a |
| 9 | [letta-ai/letta](https://github.com/letta-ai/letta) | Durumlu ajan platformu | 25288 / Apache-2.0 / 2026-10-18 | Persona = **memory block** (`label`, `description`, `value`, `limit`, `read_only`); `persona` + `human` blokları bağlamda daima görünür, arşiv belleği ayrı ([doküman](https://docs.letta.com/guides/agents/memory-blocks)) | Blok değeri API ile; sürüm sistemi dokümanda görülmedi | Persona eval yok [?] | API + Letta Code | Çekirdek özellik: ajan bloğu kendisi düzenleyebilir (`read_only` ile kilitlenir) |
| 10 | [choosewhatulike/trainable-agents](https://github.com/choosewhatulike/trainable-agents) (Character-LLM) | Rol oynama için eğitilmiş karakter modelleri | 654 / Apache-2.0 / 2024-10-29 | `data/seed_data/{profiles,prompts,questions}` (Sokrates dahil 9 karakter), `data/gen_results/interview_*` | git + HF veri seti | Var: tek ve çok turlu "interview"; "Protective Scene" ile karakter halüsinasyonunu azaltma | FastChat CLI/Web | Yok (eğitimle içselleştirme) |
| 11 | [morecry/CharacterEval](https://github.com/morecry/CharacterEval) | Rol-oynama ajanı benchmark'ı | 309 / MIT / 2025-05-27 | 1785 çok turlu diyalog, 77 karakter, 13 metrik, 4 boyut, CharacterRM | Veri sürümü README haberlerinde | Evet, başlı başına eval | betik | Diyalog verisi |
| 12 | [vsamuel2003/PersonaGym](https://github.com/vsamuel2003/PersonaGym) | Persona ajanı değerlendirme çerçevesi (EMNLP Findings 2025) | 44 / MIT / 2025-08-21 | `code/personas.py`, `code/eval_tasks.py` (statik ortamlar), `run.py --persona_list --model` | git | Evet, OpenAI/Anthropic/Together modelleri | CLI | Yok |

Dürüstlük notu: tablodaki "Sokrates" odaklı ajan repolarının hepsi 0-3 yıldız (en yüksek: #3 bevibing, 342). Yüksek yıldızlı repolar (#7, #9) persona **kalitesi** değil platform sunar. Kanıtlı olgun bir "persona ajanı + eval" referansı bu aramada bulunmadı; en yakını #1 (yıldız 0, lisanssız).

## 2. Ortak desenler

1. **Tek markdown dosya = persona** en yaygın biçim (#2, #3, kart #7). Başarısızlığı: eval yok, sürüm yok. Kimlik alanları (Core Identity, Speaking Style, Common Phrases) tekrar eder.
2. **Kimlik + sert kurallar ayrı dosya:** yalnız #1 ayırıyor (`CLAUDE.md` kimlik, `.claude/rules/character-guardrails.md` yasaklar). Kart spec'inde de `system_prompt` ile `post_history_instructions` ayrıdır.
3. **Örnek diyalog banka:** #7 `mes_example`, #1 5 few-shot + planlanan 30-40'lık dönen banka (`config/exemplars.yaml`, gerekçe: aynı 5 örneğe yakınsama). Desen: sabit az örnek yerine mod x tema süzgeçli dönen örnek.
4. **Ucuz deterministik denetim + pahalı LLM denetimi katmanı:** #1 regex doğrulayıcı (anakronizm terimleri, modern register, meta yorum) her yanıtta; LLM `drift_audit` her 10 seansta. #4 ve #5 LLM yargıç. #11, #12 çok boyutlu LLM yargıç.
5. **Hileli soru ile karakter kırma testi:** #1 `TRICK_QUESTIONS` (Aristoteles'i sor, "As an AI" sor, "Platon senin hakkında ne yazdı" sor) + `forbidden` alt dizgi listesi. #10 "Protective Scene" aynı fikrin eğitim tarafı.
6. **Kaynağa bağlama (grounding) ile halüsinasyon azaltma:** #1 her felsefi iddia bulunan pasaja izlenmeli, yoksa soruya çevir. #4 kaynak toplama + vektör. #10 profil metinleri (Wikipedia).
7. **Hafıza üç kademe:** daima bağlamda küçük blok (#9 persona/human, #1 özet bloğu) · oturum günlüğü (#1 YAML, #7 jsonl) · arama tabanlı arşiv (#4 LanceDB, #9 archival, #7 lorebook).
8. **Üretici betik + şablon:** #4 (Jinja), #6 (CLI), kart yardımcı kütüphaneleri. Kimlik elle yazılmaz, şablondan basılır; tutarsızlık azalır, ama ses düzleşir [?].
9. **El devri dosyası:** #1 `HANDOFF.md` + iyileştirme planı; #6 `openspec/changes/archive`. Çok seanslı geliştirmede karar izi repoda durur.
10. **Eval ayrı repo/benchmark:** #11, #12 karakterden bağımsız; ölçüt boyutları (tutarlılık, bilgi sınırı, kişilik) yeniden kullanılabilir.

**Kaçınılan hatalar (kanıtlı):**
- Aynı 5 örneğe yakınsama, aynı hitap kalıbı: #1 `CLAUDE.md` "Vocative variety, aynı hitap art arda iki yanıt olmaz".
- Sonuçları tekrar özetleme döngüsü: #1 ANTI-REPETITION kuralı, HANDOFF "synthesis loop" düzeltmesi.
- Sahne talimatını modelin kendi uydurması: #1 "kendi `*pauses*` ekleme, sistem tek sahne notu verir".
- Fazla hızlı zincirleme argüman: #1 AGREEMENT CHECKPOINTS (her adımda onay, yanıt başına en çok 1-2 adım).
- Doğrudan cevap sızması: #3 "ABSOLUTE" kural, ama aynı kural kullanıcının gerçekten takıldığı durumu (#3 "I don't know" dalı: basitleştir) ele almak zorunda kalıyor; #1 ise "her zaman soru sormaz" diyerek 4 yöntemle (elenktik, yapıcı, ironik, tavizli öğretim) esnek.
- Model kimliğini sızdırma: #1 kural 3 "As an AI yok", test ve doğrulayıcı ile üç kat.

## 3. Claude Code'a özgü karşılıklar

Kaynak: [Output styles](https://code.claude.com/docs/en/output-styles) (AS-OF 2026-10-29, canlı okundu).

| Persona ihtiyacı | Claude Code yüzeyi | Not (doküman) |
|---|---|---|
| Ana konuşmada her yanıtın sesi | **output style**: `.claude/output-styles/<ad>.md`, frontmatter `name`, `description`, `keep-coding-instructions` (varsayılan false = yazılım mühendisliği talimatını bırakır) | Alt-ajanlar kendi sistem istemini koşar, stil onları değiştirmez; `fork` hariç. Talimattır, garanti değildir. |
| Ayrı bağlamda koşan persona | **agent**: `.claude/agents/<ad>.md` (kendi model, araç, istem) | #1 ve #2 bu biçimi kullanıyor |
| Koşula bağlı usul (elenktik hamle seçimi) | **skill** (`SKILL.md`) | #1 `dialectic.md`, #3 `SKILL.md` |
| Proje bilgisi, kimlik ve yasak listesi | `CLAUDE.md` + `.claude/rules/*.md` | #1 desen: kimlik CLAUDE.md, yasaklar rules |
| Her seferinde garanti gereken denetim | **hook** | Doküman: "must happen every time" için hook; yanıt metnini doğrulayan hook olayı bu oturumda doğrulanmadı [?] |
| Dağıtım | **plugin** (`output-styles/` dizini dahil, `force-for-plugin: true` ile zorunlu) | doküman |
| Hafıza | `memory/` dosyaları + oturum başı okuma, ya da Letta tarzı sabit blok | Claude Code'da yerleşik persona hafıza bloğu yok [?] |

Çıkarım: **output style ana yüzey, agent ikincil yüzey**; ikisi aynı kimlik metnini paylaşıyorsa çoğaltma yerine tek kaynak dosya + iki yüzey gerekir (aksi hâlde sürüm kayar). Hiçbir incelenen repo bunu yapmıyor; #1 `CLAUDE.md`'ye işaret eden ince agent dosyası yazıyor ("See CLAUDE.md for full identity"), bu tek-kaynak desenine yakın.

## 4. Önerilen referans yapı (Sokrates için)

```
C:\sistem\sokrates\
  README.md
  CLAUDE.md                      # kimlik özeti + hafıza protokolü (kısa)
  sokrates.bat
  .claude\
    settings.local.json
    output-styles\sokrates.md    # ana yüzey (tek kaynak kimlik)
    agents\sokrates.md           # ince; kimliğe işaret eder
    rules\karakter-yasaklari.md  # sert kurallar (anakronizm, meta yorum, uydurma alıntı)
    skills\elenktik\SKILL.md     # hamle seçimi: elenktik/yapıcı/ironik/tavizli
  kaynak\                        # Platon diyalogları (Apology, Euthyphro, Meno...) + künye
  ornekler\                      # dönen örnek diyalog bankası (mod x tema), YAML
  diyaloglar\                    # simülasyon kayıtları (mevcut)
  hafiza\                        # oturum özeti YAML + summary
  test\
    hileli-sorular.yaml          # soru + yasak terim listesi + beklenen davranış
    altin-diyaloglar\            # altın transkriptler
    rubrik.md                    # 5 ölçüt, maskeli hakem girdisi
    kosucu.py                    # senaryoları koşar, ucuz regex denetimi, sonuç JSONL
  surum\                         # prompt sürümü: kimlik metni v0.x + değişiklik notu
  HANDOFF.md
```

## 5. Sokrates klasörüyle fark

Mevcut: `README`, `CLAUDE.md`, `.claude/{settings.local.json, output-styles, agents, skills}`, `sokrates.bat`, `diyaloglar/`.

| Eksik/fark | Emsal | Etki |
|---|---|---|
| `.claude/rules/` ayrımı yok (yasaklar kimlikle karışık olabilir) | #1 | Yasaklar ayrı, test edilebilir liste olur |
| Otomatik hileli soru testi + yasak terim listesi yok (diyaloglar/ elle kayıt) | #1 `test_character.py` | Yeniden üretilebilir karakter kırma ölçümü |
| Ucuz deterministik yanıt denetimi yok | #1 `response_validator.py` | Anakronizm/meta yorum ucuz yakalanır |
| Dönen örnek diyalog bankası yok | #1 plan A1, #7 `mes_example` | Aynı kalıba yakınsama azalır |
| Kaynak korpus + künye yok | #1 `Books/`, #10 `profiles` | Uydurma alıntı kapısı |
| Hafıza dizini yok | #1 `memory/`, #9 bloklar | Dönen kullanıcı süreklilik |
| Sürüm dizini/`HANDOFF` yok | #1, #6 | Prompt sürüm izi |
| Eval çerçevesi (rubrik) mevcut bağlamda var (rapor tarafında), repoda yok | #11, #12 | Ölçüt boyutları ödünç alınabilir |
| Güçlü yön | Çoğu repo eval içermiyor; mevcut yapıda 18 simülasyon ve maskeli hakem turu zaten emsallerin çoğundan ileride (Sokrates klasörü dışı kaynaktan: commit `d79269a`) | |

## 6. D/K/X

- **D:** #1 yapısı, `CLAUDE.md`, guardrails, agent, test, validator, HANDOFF, ayarlar · #2 ağaç + `socrates-agent.md` + README · #3 `SKILL.md` · #4 README, SOUL şablonu, `test.py` · #5 ağaç · #6 ağaç + README · #7 ağaç · #8 spec alan listesi (kısmi satırlar) · #9 Letta bloğu (doküman) · #10 ağaç + README · #11, #12 README · output style doküman sayfası.
- **K:** #5 GPT-4o yargıç ve sonuçları (yalnız arama özeti ve dosya adları); #6 aralıklı tekrar ayrıntısı; #7 `default/content` alt ağacı ve kart sürüm alanı; #9 repo ağacı (yalnız kök, persona/prompt dosyaları aranırken boş döndü); #1 `app.py` arayüz türü.
- **X (doğrulanamadı):** (a) "persona + Claude Code output style" odaklı bir GitHub koleksiyonu aramada çıkmadı; (b) Anthropic cookbook/quickstarts ve OpenAI Agents SDK örneklerinde persona repoları taranmadı (bu koşumda arama gelmedi); (c) hook ile yanıt metni doğrulaması; (d) Letta'da persona sürümleme.
- **Kanıt sınırı:** yıldız sayıları anlık görüntüdür; birçok emsal 0-3 yıldızlıdır, bu yüzden "topluluk uzlaşısı" değil "tasarım örneği" sayılmalı (kanıt hiyerarşisi 4-5).
