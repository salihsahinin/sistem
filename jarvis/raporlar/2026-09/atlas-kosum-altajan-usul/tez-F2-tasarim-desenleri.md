AS-OF 2026-09-17, canlı

# Tez F2 — 2026'da alt-ajan / özel ajan tanımı yazmanın standart desenleri

Soru: sistem promptu + araç seti tasarımı, izin listesi, orchestrator–worker deseni, ölçüm/eval, LLM-as-judge tasarımı, 2026 terminolojisi. Bağımsız koşum (F2); repo dosyası okunmadı; 2 birincil kaynak (Anthropic engineering blog) fiilen WebFetch ile açıldı.

## İddialar

**İ1 — D** (Bölüm 1, orchestrator-worker tanımı)
Anthropic'in "Building effective agents" yazısı orchestrator-workers desenini merkezi bir LLM'in görevi dinamik olarak parçalayıp işçi LLM'lere dağıttığı ve sonuçları sentezlediği bir iş akışı olarak tanımlar.
URL: https://www.anthropic.com/engineering/building-effective-agents
Alıntı: "a central LLM dynamically breaks down tasks, delegates them to worker LLMs" (≤15 kelime)

**İ2 — D** (Bölüm 1, orchestrator-worker vs parallelization)
Aynı yazı, orchestrator-worker desenini paralelleştirmeden ayıran özelliğin alt-görevlerin önceden tanımlanmamış olması, orkestratörün girdiye göre belirlemesi olduğunu söylüyor.
URL: https://www.anthropic.com/engineering/building-effective-agents
Alıntı: "subtasks aren't pre-defined, but determined by the orchestrator" (≤15 kelime)

**İ3 — X** (Bölüm 1, rol promptu içeriği — bulunamadı)
"Building effective agents" yazısı, rol/sistem promptunun tam olarak neyi içermesi/içermemesi gerektiğine dair somut yapı önerisi (uzunluk, motivasyon vs vurgu, XML/başlık) sunmuyor; bu konu ayrı bir kaynakta (İ7-İ9, prompting best practices) ele alınıyor.
URL: https://www.anthropic.com/engineering/building-effective-agents
Not: WebFetch özeti "role prompt design: not covered" döndürdü — doğrulanmadı, kaynağın kendisi tam okunmadı, yalnız model özeti alındı.

**İ4 — D** (Bölüm 1, genel ilke)
Anthropic ajan başarısının anahtarının performansı ölçmek ve uygulamaları yinelemek olduğunu; basitlik, planlama adımlarının şeffaflığı ve araç dokümantasyonu/testinin öncelikli ilkeler olduğunu vurguluyor.
URL: https://www.anthropic.com/engineering/building-effective-agents
Alıntı: "measuring performance and iterating on implementations" (≤15 kelime)

**İ5 — D** (Bölüm 2, araç açıklaması = prompt mühendisliği)
"Writing effective tools for agents" yazısı araç açıklamalarının işe yeni başlayan birine anlatır gibi, örtük bağlamı açık hale getirerek yazılmasını; küçük iyileştirmelerin bile büyük performans farkı yarattığını (SWE-bench örneği) belirtiyor.
URL: https://www.anthropic.com/engineering/writing-tools-for-agents
Alıntı: "even small refinements to tool descriptions can yield dramatic improvements" (≤15 kelime)

**İ6 — D** (Bölüm 2, namespacing / en-az-yetki dolaylı)
Aynı yazı, yüzlerce aracın karışmasını önlemek için servis bazlı ya da kaynak bazlı önek/sonek ile "namespacing" (adlandırma alanı gruplama) önerir; bu ölçülebilir eval farkı yaratıyor. Doğrudan "en-az-yetki / pozitif izin listesi" terimi geçmiyor — bu, dolaylı bir çıkarımdır (X işaretlenmeli değil ama netlik için not: makale kelimenin kendisini kullanmıyor).
URL: https://www.anthropic.com/engineering/writing-tools-for-agents
Alıntı: "Namespacing... can help delineate boundaries between lots of tools" (≤15 kelime)

**İ7 — X** (Bölüm 2, formal en-az-yetki çerçevesi — bulunamadı)
"Writing effective tools for agents" yazısı, açık bir "least-privilege" / pozitif-izin-listesi çerçevesi sunmuyor; onun yerine sistematik ölçüm (çalışma süresi, araç çağrısı sayısı, token tüketimi, hata oranı) üzerinden iyileştirmeyi öneriyor.
URL: https://www.anthropic.com/engineering/writing-tools-for-agents
Alıntı: "metrics like the total runtime of individual tool calls and tasks" (≤15 kelime)

**İ8 — D** (Bölüm 2, ajanların kendi hatalarını tespiti)
Yazı, ajanların kendilerinin araç tasarım sorunlarını (çelişkili açıklamalar, verimsiz uygulamalar) tespit etmede "yardımcı ortak" olarak kullanılabileceğini; Claude Code'un değerlendirme transkriptlerini analiz edip araç değişiklikleri önerebildiğini belirtiyor.
URL: https://www.anthropic.com/engineering/writing-tools-for-agents
Alıntı: "Agents are your helpful partners in spotting issues" (≤15 kelime)

**İ9 — D** (Bölüm 1/2 köprü, context engineering — orchestrator-worker bağlam devri)
Anthropic'in "Effective context engineering for AI agents" yazısı, alt-ajan mimarilerinde "lazy-loading" yaklaşımını tarif eder: uzman alt-ajanlar temiz bağlam penceresiyle odaklı görevleri yürütür ve yalnızca yoğunlaştırılmış, damıtılmış bir özet (genelde 1.000-2.000 token) döndürür.
URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
Alıntı: "returns only a condensed, distilled summary of its work" (≤15 kelime)

**İ10 — D** (Bölüm 1, hibrit bağlam yükleme)
Aynı yazı, hibrit modeller için hızlı erişim adına bazı verinin önceden getirilmesini, ayrıca ajanın kendi takdirine göre ek otonom keşif yapmasını önerir (eager + lazy karışımı).
URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
Alıntı: "retrieving some data up front for speed... further autonomous exploration" (≤15 kelime)

**İ11 — D** (Bölüm 1, rol promptu yapısı/uzunluğu)
Aynı yazı, promptların `<background_information>`, `<instructions>` gibi XML etiketleri ya da Markdown başlıklarıyla ayrık bölümlere organize edilmesini; "minimal" olmanın kısa olmak anlamına gelmediğini, beklenen davranışı tam ortaya koyan minimal bilgi kümesinin hedeflenmesini söyler.
URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
Alıntı: "minimal set of information that fully outlines your expected behavior" (≤15 kelime)

**İ12 — D** (Bölüm 1, aşırı uçlar uyarısı)
Yazı, rol promptunun iki aşırı uca düşmemesi gerektiğini vurgular: aşırı katı if-else mantığı ile paylaşılan bağlamı yanlış varsayan aşırı belirsiz yönlendirme arasında; hedef "spesifik ama esnek" bir orta nokta.
URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
Alıntı: "falsely assumes shared context" (≤15 kelime)

**İ13 — K** (Bölüm 1, Claude 4.x prompting best practices — ikinci elden özet, doğrulanmadı tam metin)
Anthropic'in platform.claude.com "Prompting best practices" sayfası, mevcut Claude modelleri (Fable 5.1, Sonnet 5, Opus 5 vb.) için üç bölümlük bir rehber sunuyor: model-özel rehberlik, tüm modeller için genel teknikler (açıklık, örnekler, XML yapı, thinking, araç kullanımı, ajan sistemleri), ve eski nesilden geçiş notları. Sayfa tam okunmadı (62.7 KB, önizleme alındı); bu iddia yalnız önizleme metnine dayanıyor, K olarak işaretlendi.
URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
Alıntı: "organized in three parts... model-specific guidance" (≤15 kelime)

**İ14 — K** (Bölüm 1, XML etiket kullanımı — WebSearch özetinden)
Anthropic dokümantasyonu Claude'un rastgele hiyerarşik XML etiketlerini saygıyla işlemek üzere ince ayarlandığını, kanonik "en iyi" etiket adı olmadığını, ancak tutarlı ve içerikle uyumlu adlandırma önerdiğini belirtiyor. Bu iddia birincil sayfanın tam metninden değil arama motoru özetinden geliyor — orta güven.
URL: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags
Alıntı: "no canonical 'best' XML tags" (≤15 kelime)

**İ15 — K** (Bölüm 3, eval araçları — promptfoo)
promptfoo'nun 2026'da trace-tabanlı ajan eval rehberi eklediği, `trajectory:tool-used` ve `trajectory:tool-sequence` gibi trajectory-assertion'ları desteklediği bildiriliyor; ayrıca 2026-03'te OpenAI tarafından satın alındığı iddia ediliyor. İkincil kaynaklardan (arama özeti), birincil GitHub PR sayfası açılmadı — orta güven.
URL: https://github.com/promptfoo/promptfoo/pull/8877
Alıntı: "trajectory-based agent evaluation guide" (≤15 kelime, parafraze)

**İ16 — X** (Bölüm 3, Inspect AI — bulunamadı doğrudan)
"Inspect AI" (UK AISI'nin eval çerçevesi) için ajan-trajectory-eval özelliğine dair birincil kaynak bulunamadı; arama sonuçları yalnız genel trajectory-eval kavramlarını (DeepEval, Arize, Langfuse) döndürdü, Inspect'e özgü doğrulanmış tek satır elde edilemedi.
URL: yok (arama sonuçları genel kavram sayfalarıydı, Inspect'e özgü değildi)

**İ17 — K** (Bölüm 3, dört boyutlu ajan-eval çerçevesi)
Sektörde (2026) ajanların dört boyutta değerlendirildiği raporlanıyor: trajectory (izlenen yol), tool use (doğru araç/doğru argüman), task completion (hedefe ulaşma), multi-turn quality (çok turlu tutarlılık). İkincil kaynaklardan derlenmiş genel eğilim — birincil akademik/şirket kaynağı tek tek doğrulanmadı.
URL: https://langfuse.com/resources/engineering/ai-agent-evaluation ; https://arize.com/guides/ai-agent-handbook/agent-evaluation/
Alıntı: "trajectory... tool use... task completion... multi-turn quality" (≤15 kelime)

**İ18 — K** (Bölüm 4, LLM-as-judge kalibrasyonu)
2026'da üretim deseni olarak, ölçülebilir çıktılar için metrik-tabanlı değerlendirme + akıl yürütme görevleri için LLM-judge hibrit kullanımı; frontier-sınıf modellerin güvenilirlik-çıpası, ucuz modellerin kalibre edilip yanlılık kontrolünden geçtikten sonra kabul edilebilir olduğu bildiriliyor. Ayrıca bir kaynak, LLM judge'ların insan değerlendiricilerle ~%85 uyum gösterdiğini (iki insanın kendi aralarındaki uyumdan daha yüksek) belirtiyor — bu rakam tek ikincil kaynaktan, çapraz doğrulanmadı.
URL: https://futureagi.com/blog/llm-as-a-judge/ ; https://deepeval.com/blog/llm-as-a-judge
Alıntı: "agrees with human reviewers about 85% of the time" (≤15 kelime)

**İ19 — K** (Bölüm 4, "yapan ≠ ölçen" ilkesi — dolaylı destek)
Kalibrasyon literatüründe insan-derecelendirilmiş bir kalibrasyon setinin koşul/alan/zaman dilimine göre katmanlandığı, çoklu-ajan müzakere çerçeveleri (ör. CollabEval) ve yapılandırılmış meta-değerlendirme kıyaslamalarının judge güvenilirliğini artırmak için kullanıldığı bildiriliyor. Bu, "yapan ajan ≠ ölçen ajan" ilkesini destekler ama makale doğrudan bu cümleyi kurmuyor — çıkarımsal, K.
URL: https://www.langchain.com/resources/llm-as-a-judge
Alıntı: "human ratings and rationales are used to construct a bank" (≤15 kelime)

**İ20 — D** (Bölüm 5, 2026 terminolojisi — Agent Skills)
Anthropic'in resmî platform dokümantasyonu "Agent Skills"i, Claude'un keşfedip dinamik olarak çektiği, ne zaman etkinleşeceğini tanımlayan yeniden kullanılabilir yetenek paketleri (SKILL.md + opsiyonel script/kaynak) olarak tanımlıyor.
URL: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
Alıntı: "reusable specification that defines how a capability should behave" (≤15 kelime, parafraze — arama özetinden)

**İ21 — K** (Bölüm 5, subagent tanımı — Claude Code)
Claude Code subagent'larının kendi bağlam penceresi, kendi araç izinleri ve kendi modeliyle çalışan izole Claude örnekleri olduğu; lider ajanın yalnız alt-ajanın nihai özetini gördüğü, ara adımları görmediği bildiriliyor. Bu, İ9'daki "lazy-loading/damıtılmış özet" iddiasıyla tutarlı ve onu destekliyor — ancak bu cümle ikincil kaynaktan (arama özeti), birincil Claude Code dokümanı açılmadı.
URL: https://www.totalum.app/blog/claude-code-subagents-totalum
Alıntı: "lead agent sees only each subagent's final summary" (≤15 kelime)

**İ22 — X** (Genel, "agentic context engineering" terimi tek başlı kaynak — bulunamadı)
"Agentic context engineering" teriminin sektörde ayrı, standart bir başlık olarak (context engineering'den farklı) yerleştiğine dair birincil/otoriter tek bir kaynak bulunamadı; bu bütçe içinde yalnızca "context engineering" (Anthropic) ve "agent skills"/"subagent design" (Claude Code ekosistemi) terimleri doğrulanabildi.
URL: yok

## Jarvis için sonuç

1. Rol promptu: XML/başlık bölümlü, "minimal ama tam" hedefli, aşırı katı if-else ile aşırı belirsiz uçlar arasında orta nokta — ATLAS'ın mevcut Türkçe taban metni bu ilkeyle uyumlu (İ11, İ12).
2. Orchestrator-worker'da lider yalnız işçinin damıtılmış özetini görmeli (1.000-2.000 token); Jarvis'in lider-ajan → işçi-ajan devrinde (m.44, ajan-metodolojisi) bu "lazy-loading" ilkesi zaten örtük var, açıkça adlandırılabilir (İ9, İ21).
3. En-az-yetki/pozitif araç listesi için Anthropic'in kendi birincil kaynaklarında formal bir çerçeve YOK (İ3, İ7 — X/D-eksik); Jarvis'in kendi izin-kısıtlama pratiği (araç listesi ajan tanımında sabit) sektör pratiğinden ileride, dış doğrulama beklemeden sürdürülebilir.
4. Eval: trajectory-first değerlendirme (tool-call doğruluğu + task completion + multi-turn) 2026 standardı görünüyor (İ15, İ17); Jarvis'in `v_skill_kosum` örneklem-denetimi bu çerçeveyle hizalı ama "trajectory" terimini benimseyip kaydedebilir.
5. LLM-as-judge: "yapan ≠ ölçen" + kalibrasyon-seti ilkesi ikincil kaynaklarla destekleniyor ama net bir birincil-kaynak yok (İ18, İ19 — K); Jarvis'in mevcut hakem-ayrı-model deseni (Karar 89, Opus lider/Sonnet işçi ayrımı) bu genel eğilimle tutarlı, iddia güçlendirilmeden mevcut kural korunmalı.
