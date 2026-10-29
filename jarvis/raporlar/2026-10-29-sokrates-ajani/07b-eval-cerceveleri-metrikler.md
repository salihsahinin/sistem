# 07b: Persona ajanı değerlendirme çerçeveleri ve metrikler

**AS-OF 2026-10-29**, canlı web (WebFetch/WebSearch). Araştıran: ATLAS (Sonnet). Yöntem: her iddia aşağıdaki URL'den çekildi; çekilemeyen ayrıntı "doğrulanmadı" diye işaretli. Sayılar kaynaktan, kestirim `[?]`. Rakamlar deneysel (yazarların kendi raporu), bağımsız yeniden üretilmedi.

## 1. Benchmark tablosu

| Benchmark | Ne ölçer | Boyutlar / metrik | Hesap / judge | Not | URL |
|---|---|---|---|---|---|
| PersonaGym (2024, v5) | Persona ajanı, dinamik, 10 LLM x 200 persona x 10.000 soru | 5 görev: Expected Action, Action Justification, Linguistic Habits, Persona Consistency, Toxicity Control | Her persona için 150 ortamdan seçim; görev başına 10 soru/ortam; her soru için 1-5 puan örnek cevapları rubriğe eklenir; iki judge (GPT-4o + LLaMA-3-70b) 1-5 puan, T=0, ortalama = PersonaScore | İnsanla Spearman %75,1, Kendall-Tau %62,73 (5 anotatör, 1.500 cevap, Fleiss kappa 0,71). Linguistic Habits en zor. Model boyutu tahmin etmiyor (GPT-4.1 = LLaMA-3-8b = 4,49). Claude 3 Haiku persona reddi diğerinden 8,5 kat yüksek | https://arxiv.org/abs/2407.18416 , https://arxiv.org/html/2407.18416v5 |
| CharacterEval (2024) | Çince, çok-turlu, 77 karakter, 1.785 diyalog, 23.020 örnek | 4 boyut, 13 metrik: Konuşma yeteneği (Fluency, Coherency, Consistency); Karakter tutarlılığı (Knowledge-Exposure, Knowledge-Accuracy, Knowledge-Hallucination, Persona-Behavior, Persona-Utterance); Çekicilik (Human-Likeness, Communication Skills, Expression Diversity, Empathy); Kişilik geri-testi (MBTI doğruluğu) | CharacterRM (Baichuan2-13B tabanlı ödül modeli, 12 anotatör, 5'li ölçek) | İnsanla Pearson: CharacterRM 0,631 genel, GPT-4 0,362-0,385. Persona-Behavior'da CharacterRM 0,879 | https://arxiv.org/abs/2401.01275 , https://arxiv.org/html/2401.01275 |
| CharacterBench (AAAI 2025) | EN+ZH, 22.859 insan etiketli örnek, 3.956 karakter | 6 yön, 11 boyut: Memory (Memory Consistency); Knowledge (Fact Accuracy, Boundary Consistency); Persona (Attribute Consistency, Behavior Consistency); Emotion (Self-regulation, Empathetic Responsiveness); Morality (Stability, Robustness); Believability (Human-likeness, Engagement) | Seyrek boyutlar (özellik her cevapta görünmez) hedefli sorgularla, yoğun boyutlar hedefsiz sorgularla. CharacterJudge (Qwen2-7B-Chat ince ayarlı) | İnsanla Pearson ~%68 ZH, ~%64 EN; GLM-4 tabanından yüksek. **Boundary Consistency = bilgi sınırı**, Sokrates için en yakın boyut | https://arxiv.org/abs/2412.11912 , https://arxiv.org/html/2412.11912 |
| InCharacter (2023) | Kişilik aslına uygunluğu: ajana psikolojik ölçek görüşmesi uygulanır | 14 psikolojik ölçek, 32 karakter | Ajanın ölçek cevapları, insanların karaktere atfettiği kişilikle karşılaştırılır | En iyi ajanlar %80,7'ye kadar uyum. Ölçek adları (BFI, 16Personalities) sayfada doğrulanmadı | https://arxiv.org/abs/2310.17976 |
| RoleBench / RoleLLM (2023) | 168.093 örnek, 100 rol; konuşma tarzı + role özgü bilgi | RAW (genel talimat, rolsüz), CUS (rolle genel talimat = üslup taklidi), SPE (rol soruları = rol bilgisi) | ROUGE-L + GPT-4 judge (AlpacaEval tarzı win-rate, RoleGPT referans) + insan (3 yüksek lisans, 500 talimat) | ROUGE-L sözcük örtüşmesi; yaratıcı/felsefi sohbet için zayıf vekil (çıkarım, kaynak sayfada vurgulanmadı) | https://arxiv.org/abs/2310.00746 , https://arxiv.org/html/2310.00746 |
| TimeChara (2024) | Zaman-noktası karakter halüsinasyonu: karakterin o anki kimliği/zaman çizgisiyle çelişen bilgi | 10.895 örnek; ölçüm yöntemi sayfada doğrulanmadı | Otomatik üretim hattı | GPT-4o dahil lider modellerde belirgin halüsinasyon. **Anakronizm sınaması için en yakın akademik kuzen** | https://arxiv.org/abs/2405.18027 |
| Derlemeler (2024-2026) | Alan haritası | RoleEval (300 karakter, 6.000 EN/ZH çoktan seçmeli), RPEval (2025: duygu, karar, ahlak, karakterde tutarlılık), ArcANE (2026: karakter yayı) | | Doğrudan "anakronizm" benchmark'ı bulunamadı; TimeChara ve CharacterBench Boundary Consistency en yakını | https://arxiv.org/pdf/2601.10122 , https://arxiv.org/pdf/2404.18231 , https://arxiv.org/pdf/2606.05553 |

Ortak örüntü: **rol-yapma benchmark'ları tek-cevap veya kısa diyalog ölçer; hepsi bir judge (LLM ya da eğitilmiş ödül modeli) kullanır; insanla korelasyon 0,6-0,75 bandında, yani judge kusurlu.**

## 2. Araç tablosu

| Ad | URL | Çok-turlu? | Simüle kullanıcı? | Rubrik judge? | Yerel / ücretsiz? |
|---|---|---|---|---|---|
| promptfoo | https://www.promptfoo.dev/docs/providers/simulated-user/ | Evet (`promptfoo:simulated-user`, `maxTurns` varsayılan 10, `initialMessages`, `stateful`, `###STOP###`) | **Evet, yerleşik** (`instructions` değişkeni) | Evet: `llm-rubric` (value, threshold, provider, rubricPrompt; JSON reason/score/pass), `g-eval`, `conversation-relevance`, `select-best`, `factuality`, `model-graded-closedqa`, `trajectory:goal-success` | MIT, yerel koşar (README); judge için LLM sağlayıcı gerekir; Ollama sağlayıcı olarak listeli; OpenAI'ın parçası ama açık kaynak kalıyor (README beyanı) |
| DeepEval | https://deepeval.com/docs/metrics-introduction , https://deepeval.com/docs/conversation-simulator | Evet (`ConversationalTestCase` + `Turn`) | **Evet** (`ConversationSimulator`: scenario + persona + expected_outcome, `max_user_simulations` 10, simulation_graph, stopping_controller) | Evet: Conversational GEval, Role Adherence, Knowledge Retention, Conversation Completeness, Turn/Conversation Relevancy, Turn Faithfulness | Apache 2.0; judge herhangi LLM (özel model sınıfı); yerel Ollama sayfada doğrulanmadı |
| `claude plugin eval` | https://code.claude.com/docs/en/plugin-evals.md | **Hayır, vaka = tek prompt**; önceki konuşmayı `context.history_file` (.jsonl) ile devam ettirir, prompt = sonraki kullanıcı turu | **Hayır** (MCP sunucusu için `type: agent` taklit var, kullanıcı için yok) | Evet: `llm` grader (kural: 3 oydan >=2 PASS; PASS/FAIL somut koşullu rubrik), `baseline` grader (referans transkriptten en az iyi mi), `regex`, `tool_used`, `tool_order`, `file_exists`; `--judge-model` | Claude Code abonelik/API kullanımı yer; yerel HTML rapor; CI'de `--threshold`; vaka başına 3 koşum varsayılan, no-plugin baseline Δ |
| skill-creator evals | https://code.claude.com/docs/en/skills.md#run-evals-with-skill-creator | Doğrulanmadı (yalnız "benzer karşılaştırma, `evals/evals.json`, plugin eval ile dosya paylaşmaz" okundu) | Doğrulanmadı | Doğrulanmadı | Claude Code içinde |
| Inspect (UK AISI) | https://inspect.aisi.org.uk/ , https://inspect.aisi.org.uk/scorers.html | Ajan/çoklu-ajan ilkelleri (`react()`) var; **yerleşik kullanıcı simülatörü bulunamadı** | Hayır (arama sonuçsuz; solver olarak yazılabilir) | `model_graded_qa()` (açık uçlu, `target` rehberli), `model_graded_fact()`; çoklu grader modeli + sohbet geçmişi sunumu "Model Grading" sayfasında (ayrıntı okunamadı) | `pip install inspect-ai`; lisans dosyası sayfada yok (doğrulanmadı); yerel model destekli |
| LangSmith + openevals | https://github.com/langchain-ai/openevals | openevals "readymade evaluators"; çok-turlu simülasyon fonksiyonları bu sayfada doğrulanmadı (docs.langchain.com yolu 404 verdi) | Doğrulanmadı | Evet (hazır değerlendirici) | openevals MIT; LangSmith bulut hizmeti (ücretsiz katman doğrulanmadı) |
| Braintrust + autoevals | https://github.com/braintrustdata/autoevals | Eval sayfası çok-turlu/simüle kullanıcı anmıyor | Hayır (doğrulanmadı) | autoevals: Battle (pairwise), Closed QA, Factuality, Humor, Moderation, Security, Summarization, SQL, Translation | autoevals MIT; varsayılan OpenAI anahtarı, `OPENAI_BASE_URL` ile başka uç; Braintrust platformu bulut |
| OpenAI Evals | https://github.com/openai/evals | Çok-turlu açık değil (zincir/ajan için completion-fn protokolü) | Hayır | Model-graded YAML şablonları (`docs/eval-templates.md`) | Açık kaynak ama OpenAI panelindeki evals'e yönlendiriyor; yeni özel kod kabul edilmiyor |
| Anthropic eval rehberi | https://platform.claude.com/docs/en/docs/test-and-evaluate/develop-tests | Araç değil, yöntem | n/a | Öneriler: spesifik+ölçülebilir ölçüt, otomatik notlama, **kaç tane > tek tek kalite**, LLM notlayıcı olarak çıktıyı üretenden **farklı model**, yalnız skor/etiket çıkar, Likert 1-5 örneği | Ücretsiz doküman |

Çok-turlu + simüle kullanıcı için tek doğrulanmış iki aday: **promptfoo** ve **DeepEval**. Claude Code'un kendi aracı (`plugin eval`) tek-prompt + devam transkript düzeyinde kalıyor.

## 3. Metrik kataloğu

| Metrik | Nasıl hesaplanır | Hazır olduğu yer |
|---|---|---|
| Role Adherence | Her asistan turu önceki bağlamla `chatbot_role`'a karşı yes/no; skor = uygun tur / toplam tur. `hybrid`: P(yes)<0,5 ise karakter dışı. `system_one`: ağırlıklı 3 soru (karakter tutarlılığı 2, aykırı davranmama 1, genel tutarlılık 1). Eşik 0,5 | DeepEval `RoleAdherenceMetric` (https://deepeval.com/docs/metrics-role-adherence) |
| Knowledge Retention | Konuşmada verilen olgular sonraki turlarda tutuluyor mu (LLM judge, 0-1) | DeepEval |
| Conversation Completeness / Relevancy / Turn Faithfulness | LLM judge, 0-1 | DeepEval; promptfoo `conversation-relevance` |
| Conversational GEval | Doğal dil ölçütten adım üret, test durumuna uygula | DeepEval; promptfoo `g-eval` (tek-tur) |
| PersonaScore | 5 görev x rubrik (örnek cevaplı 1-5) x 2 judge ortalaması | PersonaGym kodu (paket olarak doğrulanmadı) |
| Persona-Behavior / Persona-Utterance, Knowledge-Exposure/Accuracy/Hallucination | CharacterRM 1-5 | CharacterEval (Çince, ödül modeli yayımlanacak denmiş; erişilebilirlik doğrulanmadı) |
| Boundary Consistency, Fact Accuracy, Memory Consistency | CharacterJudge, hedefli sorgu | CharacterBench |
| Personality back-testing | MBTI/psikolojik ölçek cevabı vs bilinen tip | CharacterEval, InCharacter |
| ROUGE-L, win-rate | Sözcük örtüşmesi; GPT-4 pairwise | RoleBench; promptfoo `rouge-l`, `select-best`; autoevals Battle |
| Karakter dışı kalma oranı, persona reddi oranı | Tur başına yes/no sayımı; ret sayımı (PersonaGym'de Claude 3 Haiku bulgusu) | Role Adherence'ın tümleyeni; elle regex |
| Toxicity Control / güvenlik | 1-5 rubrik; ya da moderation sınıflayıcı | PersonaGym; promptfoo `moderation`, `guardrails`; autoevals Moderation |
| Anakronizm / point-in-time halüsinasyon | Karakterin o anki bilgisiyle çelişen bilgi sayımı | TimeChara (hazır araç yok); pratikte `llm-rubric` + `regex` yasak-sözcük listesi |
| Araç-iz denetimi | `tool_used`, `tool_order`, `trajectory:*` | `claude plugin eval`, promptfoo |
| Judge çoğunluk oyu | 3 oydan >=2 PASS | `claude plugin eval` `llm` grader |

## 4. Judge pratiği (LLM-as-judge)

- **Önyargılar:** konum, ayrıntılılık (verbosity), kendini kayırma; GPT-4 insanla >%80 uyum (insanlar arası düzeyde). Kaynak: Zheng ve ark. https://arxiv.org/abs/2306.05685. Ayrıntı sayıları (AlpacaEval %22,9 -> %64,3; MT-Bench kendini kayırma ~%10 GPT-4, ~%25 Claude-v1) ikincil blog aktarımı, birincil makalede doğrulanmadı (https://grepture.com/blog/llm-as-a-judge-bias).
- **Azaltma:** pairwise'ta sırayı değiştirip iki kez sor, ikisinde de aynı seçimse say; judge'ı farklı model ailesinden seç; çoklu judge. İkincil kaynak (blog), orta güven.
- **Pairwise vs mutlak:** inceli ölçütte pairwise insanla daha iyi, mutlak puan ortaya sıkışır (blog bulgusu). Küçük tam sayı ölçek + gerekçe alanı judge-insan korelasyonunu 0,567'den 0,843'e çıkardı (Hugging Face cookbook'tan blog aktarımı, tek kaynak, düşük-orta güven).
- **Rubrik tasarımı:** Anthropic: spesifik, ölçülebilir; `claude plugin eval`: "somut PASS ve FAIL koşulu"; küçük judge formatı yanlış cezalandırabilir (Δ negatifse önce judge'ı şüphele). PersonaGym: soru başına örnek puanlı cevaplar rubriğe eklenir.
- **Yapan ≠ ölçen:** Anthropic rehberi judge'ı üreticiden farklı model önerir; PersonaGym iki judge ortalaması; CharacterEval/Bench özel eğitilmiş judge. Sokrates'in "ayrı hakem ajanı" tasarımı bu ilkeyle uyumlu.
- **Simüle kullanıcı güvenilirliği:** "act like a user" istemi tek başına tutarsız; profil/persona + hedef izleme gerekir (Strands Evals blog, SimulatorArena EMNLP 2025 profil-koşullu simülatörlerin insana yakın olduğunu bildirir). https://strandsagents.com/blog/simulate-realistic-users-multi-turn-agents-strands-evals/ , https://preview.aclanthology.org/setup/2025.emnlp-main.1786 (ikincil, özet düzeyinde okundu).

## 5. Regresyon: sürümleme ve golden transcript

- `claude plugin eval`: vaka başına varsayılan 3 koşum, vaka skoru = koşumların ortalaması, `--threshold` altında çıkış kodu 1 (CI kapısı), `Δ` no-plugin'e karşı, HTML rapor, `--json`. Golden transcript = `context.history_file` (.jsonl) + `baseline` grader ("referans transkript kadar iyi mi"). Bu, Sokrates için en yerel regresyon mekanizması.
- promptfoo: `initialMessages` dosyadan (JSON/YAML) devam; çıktılar önceki koşumla yan yana karşılaştırılır (karşılaştırma özelliği README'de "side by side" geçti, regresyon diff ayrıntısı doğrulanmadı).
- Prompt sürümleme için aracın kendi özelliği doğrulanmadı; git sürümü (persona dosyası + vaka klasörü aynı commit) yeterli ve depo ilkesiyle (karar başına commit) uyumlu.

## 6. Sokrates testine öneri

Mevcut: elle 5 ölçütlü rubrik + sabit kullanıcı mesajlı tek-çağrı simülasyon + ayrı hakem ajanı.

| Mevcut parça | Boşluk (kanıta göre) | Hazır karşılık | Öneri |
|---|---|---|---|
| Sabit kullanıcı mesajı | Tek tur; Sokrates sorgulama = çok-turlu davranış; sabit mesaj sapma/kayma/kırma baskısını ölçmez | promptfoo simulated-user (talimatlı persona, 10 tura kadar) ya da DeepEval ConversationSimulator | **Değiştir**: 3-4 kullanıcı personası (inatçı, kırıcı, "sen yapay zekâ mısın" sorgucusu, kendine zarar bahsi) simüle kullanıcıyla 6-10 tur |
| Elle 5 ölçüt | Aynı rubrik ama el hesabı; sayısal tekrar yok | promptfoo `llm-rubric` (her ölçüt ayrı assertion, JSON reason/score) ve DeepEval Role Adherence (tur başına karakterde mi) | **Tamamla, elleme**: 5 ölçütü `llm-rubric` olarak yaz; Role Adherence'ı ek tur-düzeyi metrik olarak ekle |
| Anakronizm (Sokrates MÖ 399 sonrasını bilmemeli) | Genel metrik yok; TimeChara/CharacterBench Boundary Consistency kavramsal örnek | Hazır araç yok | **Elle kal**: yasak-sözcük `regex` + `llm-rubric` ("MÖ 399 sonrası olgu var mı"); kendi veri setin, 15-30 tuzak soru |
| Ayrı hakem ajanı | Yapan ≠ ölçen ilkesi korunuyor | Anthropic rehberi + PersonaGym iki-judge | **Koru**; promptfoo'da `provider` ile judge'ı Sokrates'ten farklı model/aile yap; ilk üç koşumda hakem skoru ile `llm-rubric` skoru karşılaştırılıp korelasyon bakılsın |
| Regresyon | Yok | `claude plugin eval` (3 koşum, eşik, Δ, history_file) | **Ekle**: Sokrates agent/skill'ini `plugin.json`'lı bir klasöre koyup `claude plugin eval`'i yalnız tek-tur kapı için kullan (ör. "Claude/Anthropic adı geçmez", "dosya yolu açıklamaz"); çok-turlu değerlendirme promptfoo'da |
| Judge sapması | Tek koşum, tek judge | 3-oy çoğunluğu (`plugin eval`), konum takası (pairwise) | **Ekle**: sürüm karşılaştırmasında (v0.4 vs v0.5) pairwise + sıra takası; mutlak puan yalnız eşik kapısında |

Yeni araç sıfırdan yazılmaz (kök md.12 hazır karşılık kapısı): promptfoo tek başına simüle kullanıcı + rubrik + trajectory + CI + yerel (MIT) sağlar; DeepEval alternatif/ek. Maliyet kaygısı: her judge çağrısı gerçek model çağrısı (plugin eval belgesi bunu açıkça yazar).

## 7. D/K/X

**D (doğrulanmış, birincil kaynak okundu)**
- PersonaGym beş görevi, PersonaScore hesabı, insan korelasyonu (arxiv v5 HTML).
- CharacterEval 4 boyut / 13 metrik ve CharacterRM korelasyonları (arxiv HTML).
- CharacterBench 6 yön / 11 boyut, sparse/dense ayrımı, CharacterJudge tabanı ve korelasyonu (arxiv HTML).
- RoleBench RAW/CUS/SPE ve ROUGE-L + GPT-4 + insan (arxiv HTML).
- promptfoo simulated-user parametreleri; `llm-rubric` çıktı biçimi ve varsayılan grader; assertion listesi (resmî doküman).
- DeepEval RoleAdherence hesabı, ConversationSimulator parametreleri, Apache 2.0 (resmî doküman, GitHub).
- `claude plugin eval` grader türleri, 3 koşum, 3 oydan 2, history_file, no-plugin baseline, eşik (resmî doküman).
- Zheng ve ark. bu önyargıları (konum, ayrıntılılık, kendini kayırma) adlandırıyor ve >%80 uyum bildiriyor (arxiv özeti).

**K (kısmi / ikincil)**
- Judge önyargısı sayıları (AlpacaEval, MT-Bench oranları, 0,567 -> 0,843) blog aktarımı; birincil doğrulanmadı.
- InCharacter ölçek adları ve metrik formülü sayfada yok.
- TimeChara ölçüm yöntemi sayfada yok.
- skill-creator, openevals çok-turlu simülasyon, LangSmith, Braintrust çok-turlu: sayfalar ilgili ayrıntıyı vermedi.
- Simüle kullanıcı güvenilirliği (SimulatorArena, Strands): arama özeti, tam metin okunmadı.
- DeepEval + yerel judge (Ollama) ve Inspect lisansı doğrulanmadı.

**X (çelişki / zayıf nokta)**
- DeepEval Role Adherence sayfası kendi içinde tam örtüşmüyor (hybrid modu: tur-başına mı, tek istekte tüm konuşma mı); parametre sayısı Python/TS tutarsız.
- PersonaGym'de Claude 3 Haiku persona reddi 8,5 kat yüksek bulgusu: Claude ailesi persona ajanında ret eğilimli olabilir; Sokrates için judge ve hedef model seçerken risk (tek çalışma, eski model, güncel Claude'a genellenemez).
- Benchmark'ların hiçbiri Sokrates'in asıl hedefini (elenktik soru kalitesi, aporia, ders verme yerine soru sorma) ölçmüyor; bu ölçütler özel rubrik ister. Tüm benchmark'lar karakter taklidi/tutarlılık ölçer, pedagojik/diyalektik kalite değil [yorum, kanıt yok].
- İnsanla judge korelasyonu 0,36-0,75 bandında; judge skoru gerçek kalite değil, vekil.
- Anakronizm için hazır metrik yok (TimeChara veri seti dışında); bu boşluk gerçek.

## Kaynak listesi

1. https://arxiv.org/abs/2407.18416 , https://arxiv.org/html/2407.18416v5
2. https://arxiv.org/html/2401.01275
3. https://arxiv.org/html/2412.11912
4. https://arxiv.org/abs/2310.17976
5. https://arxiv.org/html/2310.00746
6. https://arxiv.org/abs/2405.18027
7. https://www.promptfoo.dev/docs/providers/simulated-user/
8. https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/llm-rubric/
9. https://www.promptfoo.dev/docs/configuration/expected-outputs/
10. https://github.com/promptfoo/promptfoo
11. https://deepeval.com/docs/metrics-role-adherence , https://deepeval.com/docs/metrics-introduction , https://deepeval.com/docs/conversation-simulator , https://github.com/confident-ai/deepeval
12. https://code.claude.com/docs/en/plugin-evals.md
13. https://platform.claude.com/docs/en/docs/test-and-evaluate/develop-tests
14. https://inspect.aisi.org.uk/ , https://inspect.aisi.org.uk/scorers.html
15. https://github.com/braintrustdata/autoevals , https://github.com/langchain-ai/openevals , https://github.com/openai/evals
16. https://arxiv.org/abs/2306.05685
17. İkincil: https://grepture.com/blog/llm-as-a-judge-bias , https://strandsagents.com/blog/simulate-realistic-users-multi-turn-agents-strands-evals/ , https://preview.aclanthology.org/setup/2025.emnlp-main.1786
