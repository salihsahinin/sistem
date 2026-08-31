# İB-66 — MASKELİ HAKEM RAPORU (D/K/X)

**Künye:** HAKEM · model **opus** (lider-ajan Carvis alt-ajanı; ayrı hakem işçisi AÇILAMADI — `.claude/hooks/pretool-ajan-fren.sh` İB-54/Karar-39 DURDUR eşiği 72. Agent çağrısında tetikledi, Salih beyanı olmadan aşılmadı) · AS-OF 2026-08-31 · girdi: 6 rapor · web kullanılmadı.
**Maskeleme beyanı:** İddialar İ-01… kimliğiyle sıralandı; hüküm verilirken kaynak aile AĞIRLIK olarak kullanılmadı. Ölçüt yalnız (a) kanıtın birincilliği (b) kanıtın iddiayı GERÇEKTEN kapsaması (c) ANTİTEZ/V26 sondajından sağ çıkması. Kaynak rapor hükümden SONRA parantezde açıldı.
**Bağlayıcı girdiler:** V26'nın 6 ihlali · ANTİTEZ'in 1 DÜŞTÜ + 2 BELİRSİZ hükmü.

Etiketler: **D** = birincil kaynak iddiayı doğrudan kapsıyor, sondajdan sağ çıktı · **K** = kaynak konuya değiniyor ama iddianın tam halini demiyor ∨ yalnız ikincil kaynak ∨ sondaj belirsiz · **X** = kaynak iddiayı desteklemiyor ∨ kaynak eşleşmesi hatalı ∨ yalnız model-hafızası.

---

## A. ÜRÜN İDDİALARI

| # | İddia | Etiket | Gerekçe (maskeli değerlendirme) | Kaynak |
|---|---|---|---|---|
| İ-01 | LangGraph Studio koşum sürerken canlı stream + aktif düğüm vurgusu gösterir (K1) | **K** | Kanıt WebSearch özetinden, birincil doküman metniyle birebir eşleştirilmedi | A1 §1 |
| İ-02 | LangGraph Studio interrupt'ta state düzenleme + time-travel branching sunar (K4) | **D** | `docs.langchain.com/oss/python/langgraph/interrupts` birincil, mekanizma adlandırılmış (`Command(resume=...)`) | A1 §1 |
| İ-03 | LangGraph Studio subgraph'ları AYRI eşzamanlı panelde göstermez (K3 = HAYIR) | **X** | ANTİTEZ: hedef sayfa 404, ne doğrulandı ne çürütüldü → "HAYIR" hükmü dayanaksız; `[?]`'ye inmeli | A1 §1 (ANTİTEZ A1-1 BELİRSİZ) |
| İ-04 | AgentOps post-hoc "Session Replay" ürünüdür, koşum sürerken canlı akış yok (K1 = HAYIR) | **D** | Birincil doküman dili replay/time-travel; sondajda sarsılmadı | A1 §2 |
| İ-05 | AgentOps alt-ajanı parent altında nested child span olarak gösterir, tek ağaç (K3 KISMİ) | **D** | Resmî README/entegrasyon metni birebir | A1 §2 |
| İ-06 | AutoGen Studio canlı sohbet + tüm ajan mesajlarını gözlem sunar (K1/K2) | **D** | ANTİTEZ 2026 kaynaklarıyla teyit etti (AYAKTA); anakronizm endişesi giderildi | A1 §3 (ANTİTEZ A1-2) |
| İ-07 | AutoGen Studio üretime hazır değildir, araştırma prototipidir (K5 = HAYIR) | **D** | Kaynağın kendi beyanı, ANTİTEZ'de 2026 kaynaklarıyla tekrar doğrulandı | A1 §3 |
| İ-08 | CrewAI AMP'te canlılık/nesting/müdahale birincil dokümanda doğrulanamadı | **K** | Doğru biçimde "bilinmiyor" olarak sunulmuş; "yok" değil | A1 §4 |
| İ-09 | OpenAI Agents SDK tracing `BatchTraceProcessor` kullanır → trace'ler koşum sırasında anında görünmez (K1 = HAYIR) | **D** | V26 sondajı birincil kaynakta birebir doğruladı ("may not appear immediately") | A1 §5 (V26 #1) |
| İ-10 | OpenAI Agents SDK hiyerarşisi "TEK dikey ağaç, ayrı eşzamanlı panel değil" (K3) | **X** | V26 ihlal-2: doküman görsel sunum biçimini hiç söylemiyor → aşırı-belirlilik | A1 §5 (V26 #2) |
| İ-11 | Temporal Web UI "liveness… nested and child workflows as well" — canlı güncelleme (K1 = EVET) | **X** | V26 ihlal-1: alıntı gösterilen birincil sayfada YOK, kaynak eşleşmesi hatalı → `[?]` | A1 §6 (V26 #1) |
| İ-12 | Temporal Web UI'dan koşum sürerken Cancel / Signal / Update / Reset / Terminate yapılabilir (K4 = EVET) | **D** | V26 birebir doğruladı | A1 §6 (V26 #4) |
| İ-13 | Temporal'ın gösterdiği birim workflow event'idir, LLM konuşma turu değildir (K2 = HAYIR) | **D** | Ürünün kapsam tanımı; kriter-yorumu şeffafça beyan edilmiş, ampirik itiraz yok | A1 §6 |
| İ-14 | Claude Agent SDK oturum-seviyesi event stream'i alt-ajanın yalnız başlangıç/bitişini gösterir, tam etkinliğini değil (K1/K3 KISMİ) | **D** | Birincil `platform.claude.com/docs` alıntısı; B raporunun bağımsız `parent_tool_use_id` bulgusuyla YAKINSIYOR | A2 §1 + B §2 |
| İ-15 | Claude Agent SDK'da koşum-SÜRERKEN alt-ajana mesaj enjeksiyonu/duraklatma YOKTUR (K4 = HAYIR) | **D** | ANTİTEZ birincil `subagents` sayfasını okudu: yalnız tamamlanmış/limit-durmuş ajanın SIRALI resume'u var; `pause`/`interrupt` terimi yok | A2 §1 (ANTİTEZ A2-3, "kısmi"→HAYIR sertleştirildi) |
| İ-16 | Devin'de alt-oturumlara koşum sürerken mesaj/düzeltme gönderilebilir (K4 = EVET) | **D** | Birincil blog birebir: "send instructions, context, or corrections to any managed Devin mid-task" | A2 §2 |
| İ-17 | Devin gerçek iç-içe seviye sunar: koordinatör + N managed Devin, her biri ayrı izole oturum (K3 = EVET) | **D** | Birincil kaynak; 12 araç içinde K3'te tek net EVET | A2 §2 |
| İ-18 | Devin'de tüm alt-oturumları TEK ekranda eşzamanlı canlı akıtan konsolide pano YOKTUR (K1 KISMİ) | **D** | ANTİTEZ bağımsız sorguladı, konsolide dashboard hiçbir kaynakta tarif edilmiyor (AYAKTA) | A2 §2 (ANTİTEZ A2-1) |
| İ-19 | Manus tek-ajan canlı izleme + onay/devral/durdur sunar ama iç-içe seviye YOKTUR (K3 = HAYIR) | **D** | Birincil fetch açıkça "focuses on a single agent" | A2 §3 |
| İ-20 | Langfuse'ta koşum-sürerken canlı UI akışı birincil kaynakta doğrulanamadı; K4 müdahale yok | **K** | "Session replay" dili post-hoc; canlılık `[?]`, müdahale kanıtsız (gözlem aracı, kontrol katmanı değil) | A2 §4 |
| İ-21 | Arize Phoenix "root span'den token-düzeyi ayrıntıya zoom" sunar (K2 = EVET) | **X** | V26 ihlal-3: alıntı resmî dokümanda bulunamadı, ikincil/SEO kaynaklı | A2 §5 (V26 #5) |
| İ-22 | Braintrust'ta canlılık doğrulanamadı; "en zayıf kanıtlanan aday" (K1 = `[?]`) | **X** | ANTİTEZ DÜŞÜRDÜ: birincil `braintrust.dev/docs/observe/view-logs` **"Live tail"** — yeni satırlar flash-animasyonla akıyor, sekme gizlenince duraklıyor → **K1 = EVET**. V26 de "view it in real time" alıntısını birincil kaynakta doğruladı | A2 §6 (ANTİTEZ A2-2 DÜŞTÜ, V26 #6) |
| İ-23 | Langfuse/Phoenix/Braintrust sınıfı observability araçlarının hiçbiri canlı değildir (genelleme) | **X** | Braintrust Live tail bu genellemeyi çürütür; genelleme kayıtlı istisna ile kullanılmalı | A2 sonuç (ANTİTEZ uyarı-6) |

## B. MİMARİ/STANDART İDDİALARI

| # | İddia | Etiket | Gerekçe | Kaynak |
|---|---|---|---|---|
| İ-24 | OTel GenAI konvansiyonları ayrı repoya taşındı (`semantic-conventions-genai`); span hiyerarşisi `invoke_workflow → invoke_agent → plan` + kardeş `execute_tool`; `gen_ai.operation.name` enum'u tanımlı | **D** | Ham spec dosyası WebFetch ile okundu, span adlandırma kalıpları birebir | B §1 |
| İ-25 | Tüm `gen_ai.*` kayıtları "Development" statüsünde, Stable yok | **K** | İki kaynak yakınsıyor ama biri ikincil blog; birincil rozet metni doğrudan alıntılanmadı | B §1 |
| İ-26 | OTel GenAI konuşma içeriğini span attribute'undan ayrı "event"e taşır | **X** | B'nin kendi itirafı: model-hafızası kaynaklı; ANTİTEZ B-1 sondajı da doğrulayamadı (BELİRSİZ) → **sentezde kullanılmayacak** | B §1 (ANTİTEZ B-1) |
| İ-27 | Claude Agent SDK'da `parent_tool_use_id` alanı `StreamEvent` (token-delta) mesajlarında HER ZAMAN null; alt-ajan token akışı ana oturuma forward EDİLMEZ; yalnız TAMAMLANMIŞ mesajlar parent atfı taşır | **D** | Birincil doküman birebir alıntı (`code.claude.com/docs/en/agent-sdk/streaming-output`); tasarımın en kritik teknik kısıtı | B §2 |
| İ-28 | Alt-ajan tool adı v2.1.63'te `Task` → `Agent` oldu; `Agent` tool sonucu `agentId: <id>` taşır | **D** | ANTİTEZ birincil sayfayla birebir doğruladı (AYAKTA, güven düşük→yüksek) | B §2 (ANTİTEZ B-2) |
| İ-29 | Temporal her child'ın kendi event history'sini tuttuğunu, parent'ın yalnız `ChildWorkflowExecution*` referans olaylarını logladığını belgeler | **D** | Birincil doküman; "kendi kütüğü + üstte referans satırı" deseni | B §3 |
| İ-30 | Temporal UI'nin child görünümünü nasıl/ne sıklıkla yenilediği (polling mi push mu) HİÇBİR kaynakta doğrulanamadı | **D** | Açık boşluk olarak dürüstçe işaretlenmiş; İ-11 ile tutarlı | B §3 |
| İ-31 | Jaeger UI büyük trace'lerde (2000-5000 span) yavaşlar | **K** | V26 ihlal-6: issue "stale/not planned" kapatılmış — bağlam eksik, "aktif sınırlama" imasıyla sunulmuş | B §4 (V26 #7) |
| İ-32 | Jaeger/Tempo canlı trace gösterimi için SSE/WebSocket mi kullanıyor — doğrulanamadı, spekülasyon | **K** | B kendisi spekülasyon damgası koymuş; sondaj yapılmadı | B §4 (ANTİTEZ B-3) |
| İ-33 | Langfuse Cloud gözlemlerinin ~%60'ı OTel endpoint'inden geliyor; canlı ingestion'da trace metadata'sı ilk observation'dan sonra gelebiliyor (nesting gecikmesi) | **D** | V26 birincil blogda birebir doğruladı | B §4 (V26 #8) |
| İ-34 | OTel SDK aktif span varken log satırına `trace_id`/`span_id`'yi OTOMATİK ekler | **K** | V26 ihlal-4: spec bunu entegrasyon yoluna (appender/auto-instrumentation) bağlıyor; koşul düşürülmüş aşırı-genelleme | B §5 (V26 #9) |
| İ-35 | Hiçbir standartta "token-delta'dan kaba, tam-mesajdan ince" bir ARA konuşma-granülü tanımı yok | **K** | Negatif bulgu, taramanın kapsamıyla sınırlı; ama üç bağımsız aile de bulamadı (yakınsama) | B boşluklar |

## C. İÇ ENVANTER İDDİALARI

| # | İddia | Etiket | Gerekçe | Kaynak |
|---|---|---|---|---|
| İ-36 | `tools/gnhf-izle.py` CANLI tail'dir (`while True` + `sleep(2)`, bayt-ofsetli kısmi-satır güvenli) ve konuşma-granüllü basar (`🗣`/`⚙`/`↳`) | **D** | Kod birebir okundu, satır pointer'lı (`tools/gnhf-izle.py:66-86`, `:30-49`) | C §1 |
| İ-37 | `gnhf-izle.py` `parent_tool_use_id`, `session_id`/`uuid`, `usage`, `thinking`, `system`/`rate_limit_event` satırlarını OKUMAZ → iç-içe seviye ayrımı YOK | **D** | Koddan doğrudan; İB-66'nın hedefiyle doğrudan boşluk | C §1 |
| İ-38 | `gnhf-izle.py` yalnız EN YENİ tek worktree'nin EN SON koşumunu izler → çoklu eşzamanlı koşum görünümü yok | **D** | `:20-22`, `:60-63` | C §1 |
| İ-39 | stream-json şeması `parent_tool_use_id` alanını TAŞIR (nested-ajan atfı şema düzeyinde mümkün) | **D** | Gerçek dosyada alan gözlendi; İ-27 ile YAKINSIYOR (bağımsız iki kaynak, biri kod biri resmî doküman) | C §2 + B §2 |
| İ-40 | Örnek `iteration-N.jsonl`'da tüm `parent_tool_use_id` değerleri `None` | **K** | 8 assistant satırlık TEK küçük dosya; ayrıca dosya gnhf worktree'sinden değil ikame projeden (`~/dev/wf-deneme`) — gnhf worktree'leri boş | C §2 (öz-itiraf) |
| İ-41 | `usage` önbellek-okuma/yazma ayrımını ve `result.usage.modelUsage` per-model dökümünü taşır; izleyici bunları hiç göstermiyor | **D** | Gerçek dosya alanları + kod eksikliği, ikisi de pointer'lı | C §1-2 |
| İ-42 | m.10 commit-dili teli gnhf'nin Türkçe iterasyon özetine çarpıp koşumu durdurdu (a20630) — fren kalıtımı arızası | **D** | `raporlar/2026-08-31-k010-a3-loop-1.md:11` | C §4a |
| İ-43 | gnhf bütçe birimi önbellek-okuma DAHİL; iterasyon tabanı ~300k; e2e715'te 535k/500k tavan doldu (2 iterasyon); tavan 3M + tek-çağrılı uzun uyku ile e600a7'de 3/3 arızasız | **K** | Tek raporun kendi beyanı; C bağımsız `usage` toplamı hesaplamadı (öz-itiraf). Tasarımda kullanılabilir ama "tek kaynak" damgasıyla | C §4b |
| İ-44 | Bu koşum fiilen İÇ-İÇE loop'tur: dış = gnhf iterasyonu (`--stop-when`), iç = tur-içi tempo/kontrol (uyku sayacı); bütçe arızası doğrudan kompozisyon-maliyeti dersidir | **D** | `raporlar/2026-08-31-k010-a3-loop-1.md:19` | C §4c |
| İ-45 | gnhf worktree transkriptleri merkezi hareket kütüğüne (bronz/silver) DÜŞMÜYOR — açık kapsama açığı | **D** | `raporlar/2026-08-31-k010-a3-loop-1.md:22` | C §4c |
| İ-46 | Canlı yüzey envanteri: `CronCreate` fiilen kullanılmış (`veri/gorunum/v_son_hareketler.csv:93`); Monitor dokümante ama gnhf'ye bağlanmamış; `.claude/hooks/` ana-repo teli, gnhf worktree'sini izlemiyor; gnhf'ye özgü başka yüzey yok | **D** | Pointer'lı; §5 tablosu | C §5 |

---

## HÜKÜM

**Soru:** İç-içe LLM loop'ların KONUŞMA akışını CANLI izleten ürün var mı?
**Hüküm: KISMİ — "beş kriteri BİRLİKTE karşılayan ürün YOK; kriterler ayrı ayrı VAR."**

Gerekçe yalnız D+K iddialardan (12 araç, 60 hücre):
- **K3 (iç-içe seviyelerin ayrı yüzeyi) 12 araçta yalnız 1 kez net EVET** — Devin Managed Devins (İ-17, D). Diğerlerinde ya tek-ağaç KISMİ (İ-05, İ-20, İ-22, İ-29 sınıfı) ya HAYIR (Manus İ-19, AutoGen) ya `[?]` (İ-03, İ-08, İ-10).
- **K3 EVET olan tek araçta K1 (canlılık) KISMİ** — Devin'de her alt-oturum ayrı link, konsolide eşzamanlı canlı pano yok (İ-18, D, ANTİTEZ ile ayakta).
- **K1 net EVET olan araçlarda ya K3 ya K4 düşüyor** — Braintrust Live tail (İ-22 düzeltmesi) K1+K2 EVET ama K3 tek-ağaç KISMİ, K4 HAYIR; Manus (İ-19) K1+K4 EVET ama K3 HAYIR; AutoGen (İ-06) K1+K2 EVET ama K5 HAYIR (üretim-dışı) + K3 HAYIR.
- **K2 (konuşma-granülü) 12 araçta 6 EVET ama hiçbiri K3 ile birlikte değil.** Konuşma-granülü + canlı + seviye-ayrımı üçlüsü hiçbir üründe birleşmiyor.
- **K4 (müdahale) 4 EVET / 6 HAYIR / 2 `[?]`.** Gözlem araçları (AgentOps, Langfuse, Phoenix, Braintrust) kategorik olarak kontrol katmanı sunmuyor; Claude Agent SDK'da mid-run müdahale birincil kaynakta YOK (İ-15, D).

**Salih'in negatif bulgusu ÇÜRÜTÜLEMEDİ**, ama "hiçbir ürün yaklaşmıyor" biçimindeki güçlü versiyonu iki noktada zayıfladı: Devin K3+K4'te, Braintrust K1+K2'de gerçek karşılık üretiyor.

## KRİTER-BAZLI SAYIM (12 araç; hakem düzeltmeleri uygulanmış)

| Kriter | EVET | KISMİ | HAYIR | `[?]` |
|---|---|---|---|---|
| K1 canlılık | 4 (LangGraph, AutoGen, Manus, Braintrust) | 2 (Claude SDK, Devin) | 2 (AgentOps, OpenAI) | 4 (CrewAI, Temporal, Langfuse, Phoenix) |
| K2 konuşma-granülü | 6 (AutoGen, OpenAI, Claude SDK, Devin, Langfuse, Braintrust) | 2 (AgentOps, CrewAI) | 1 (Temporal) | 3 (LangGraph, Manus, Phoenix) |
| K3 seviye ayrımı | **1** (Devin) | 6 (AgentOps, Temporal, Claude SDK, Langfuse, Phoenix, Braintrust) | 2 (AutoGen, Manus) | 3 (LangGraph, CrewAI, OpenAI) |
| K4 müdahale | 4 (LangGraph, Temporal, Devin, Manus) | 0 | 6 (AgentOps, OpenAI, Claude SDK, Langfuse, Phoenix, Braintrust) | 2 (AutoGen, CrewAI) |
| K5 olgunluk | 8 | 2 (LangGraph, Claude SDK) | 1 (AutoGen) | 1 (Braintrust) |

**K1∧K2∧K3∧K4 hepsi EVET olan araç sayısı: 0/12.**

## SENTEZE GİRMEMESİ GEREKENLER (X etiketli)

- İ-03 LangGraph K3 "HAYIR" → `[?]` olarak yazılacak
- İ-10 OpenAI Agents SDK K3 "tek dikey ağaç" → `[?]`
- İ-11 Temporal K1 "liveness" alıntısı → kaynak eşleşmesi hatalı, `[?]`
- İ-21 Arize Phoenix K2 "token-level zoom" → `[?]`, ikincil kaynak
- İ-22 Braintrust K1 `[?]` → **EVET'e düzeltildi** (X olan, eski hükümdür)
- İ-23 "hiçbir observability aracı canlı değil" genellemesi → kullanılmayacak
- İ-26 OTel GenAI content-event ayrımı → kullanılmayacak (model-hafızası)

**D: 27 · K: 11 · X: 8** (toplam 46 iddia; İ-22'nin X'i düzeltilen ESKİ hükme aittir, yerine geçen "Braintrust K1 = EVET" D sayılmıştır).
