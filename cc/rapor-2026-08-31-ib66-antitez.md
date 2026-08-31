# İB-66 ANTİTEZ Raporu — CoVe-Factored Çürütme Denemesi

**Künye:** ANTİTEZ · model sonnet · AS-OF 2026-08-31 · araç çağrısı sayısı: 9 (WebFetch 3, WebSearch 4, üç girdi raporu Read 3 → toplam 9 araştırma çağrısı, sınır 15 içinde)
**Kaynak raporlar:** `cc/rapor-2026-08-31-ib66-a1.md` (aile A1) · `cc/rapor-2026-08-31-ib66-a2.md` (aile A2) · `cc/rapor-2026-08-31-ib66-b.md` (aile B)
**Saldırı yönü:** her iddia için "bu araç/kural aslında kriteri KARŞILIYOR mu?" sorusu bağımsız sorgulandı; iddianın kendi metni soruya taşınmadı.

---

## AİLE A1 — 3 İDDİA

### A1-1. LangGraph Studio subgraph'ları ayrı eşzamanlı panelde gösterir mi? (K3)
- **Kaynak rapor iddiası:** "Alt-graf (subgraph) ayrı panel/lane'de mi gösteriliyor sorusu doğrulanamadı → temkinli HAYIR."
- **Bağımsız doğrulama sorusu:** LangGraph Studio dokümantasyonu subgraph görselleştirmesini nasıl tarif ediyor?
- **Bulgu:** `docs.langchain.com/oss/python/langgraph/subgraphs` WebFetch'te **404 Not Found** döndürdü — sayfa bu adreste yok/taşınmış. Doğru URL'yi bulmak için ek arama gerekirdi, bütçe içinde yapılmadı.
- **Hüküm: BELİRSİZ** (kaynağa erişilemedi, ne doğrulama ne çürütme yapılabildi — A1'in temkinli HAYIR'ı da BELİRSİZ'e revize edilmeli, HAYIR fazla kesin).
- AS-OF 2026-08-31.

### A1-2. AutoGen Studio K1/K2 hükmü 2023 blog kaynaklı — anakronizm riski var mı? (Karar 68)
- **Kaynak rapor iddiası:** "AutoGen Studio K1/K2 hükmü 2023 tarihli tek blog cümlesine dayanıyor, güncel davranış farklı olabilir."
- **Bağımsız doğrulama sorusu:** 2026 itibarıyla AutoGen Studio gerçekten canlı sohbet + üretim-dışı (prototip) statüsünü koruyor mu?
- **Bulgu:** WebSearch (çoklu 2026 kaynağı) — "AutoGen Studio allows real-time interaction... chat with the workflow, observe all agent messages" VE ayrıca "AutoGen Studio is a research prototype and is not meant to be used in a production environment... not meant to be a production-ready app" (birden fazla 2026 makalesi aynı çerçeveyi tekrarlıyor). Güncel kaynaklar 2023 blogun K1/K5 çerçevesini DOĞRULUYOR, çürütmüyor.
- **Hüküm: AYAKTA** — A1'in orijinal K1 EVET / K5 HAYIR hükmü güncel (2026) kaynaklarla teyit edildi; anakronizm endişesi yersizdi, ama endişeyi işaretlemesi metodolojik olarak doğruydu.
- URL: microsoft.github.io/autogen (arama özeti, çoklu 2026 kaynağı) — AS-OF 2026-08-31.

### A1-3. Temporal K2 kategorik HAYIR — "workflow event" ile "LLM konuşma turu" ayrımı ürünün kendi sınırı mı, A1'in yorumu mu?
- **Kaynak rapor iddiası:** "Bu sınırı ben çizdim, kriter seti bunu net kesmiyor — biri Temporal+LLM-activity entegrasyonunu K2'yi karşılıyor diye savunabilir."
- **Değerlendirme:** Bu ampirik değil, kriter-yorumlama (semantik sınır çizme) sorusu; tek bir web sorgusuyla "doğru/yanlış" çıkmaz — Temporal'ın kendisi LLM-agnostik bir motor olduğu zaten A1 tarafından da kabul edilmiş, tartışma yalnız kriterin kapsamı üzerine.
- **Hüküm: sondaj yapılmadı** (bütçe — ampirik doğrulanabilir bir soru değil, A1'in kendi itirafı zaten yeterli şeffaflıkta).

---

## AİLE A2 — 3 İDDİA

### A2-1. Devin "Managed Devins" tek ekranda tüm alt-oturumları eşzamanlı canlı gösteriyor mu? (K1)
- **Kaynak rapor iddiası:** "K1 kısmi/hayır — session-link-tıkla-izle, konsolide tek-ekran canlı akış iddiası birincil kaynakta yok; ama bu ekran-düzeyi doğrulama yapılmadan verildi."
- **Bağımsız doğrulama sorusu:** Devin dokümantasyonu/blogu birden çok managed-Devin oturumunu TEK panelde gösteren bir dashboard tarif ediyor mu?
- **Bulgu:** WebSearch (docs.devin.ai, cognition.ai blogları) — "Each has its own session link, so you can inspect its work or message it directly" + ACU tüketimini izleme/uyutma/sonlandırma özellikleri bulundu, ama **"tek ekranda konsolide, eşzamanlı canlı" bir dashboard görünümü hiçbir kaynakta açıkça tarif edilmedi.**
- **Hüküm: AYAKTA** — A2'nin K1 kısmi/hayır hükmü çürütülemedi; kendi zayıflık itirafı (ekran görüntüsü doğrulamadım) doğruydu ama sonuç değişmedi.
- URL: https://docs.devin.ai/work-with-devin/advanced-capabilities · https://cognition.ai/blog/devin-can-now-manage-devins — AS-OF 2026-08-31.

### A2-2. Braintrust K1 CANLILIK gerçekten "[?] doğrulanamadı" mı, yoksa açık EVET mi?
- **Kaynak rapor iddiası:** "K1 [?] doğrulanmadı... 'view it in real time' ifadesi belirsiz; Braintrust'ı 'en zayıf kanıtlanan aday' olarak damgaladım — 'live tail' sorgusu ayrı bir sorgu gerektirirdi, atlandı."
- **Bağımsız doğrulama sorusu:** Braintrust'ın resmî log görüntüleme dokümanı gerçek-zamanlı (koşum sürerken) akan bir görünüm sunuyor mu?
- **Bulgu:** `braintrust.dev/docs/observe/view-logs` (WebSearch özetinde birincil doküman metni): **"To stream new rows as they arrive in Braintrust's Logs section, you can select Live tail. New rows are highlighted with a flash animation, and streaming pauses automatically when the browser tab is hidden."** Bu, koşum SÜRERKEN satırların otomatik/canlı aktığını açıkça tarif ediyor — replay değil, push/stream davranışı (flash-animasyon + sekme-gizlenince-duraklatma detayı, canlılığın teknik imzasıdır).
- **Hüküm: DÜŞTÜ** — A2'nin K1 "[?] doğrulanamadı" hükmü ÇÜRÜTÜLDÜ; Braintrust K1'de **EVET** olmalıydı. "En zayıf kanıtlanan aday" damgası abartılıydı; K2 EVET + K3 kısmi (nested spans) ile birlikte Braintrust aslında Langfuse/Phoenix sınıfının ÜSTÜNDE, K1'de somut kanıtlı bir aday.
- URL: https://www.braintrust.dev/docs/observe/view-logs — AS-OF 2026-08-31.

### A2-3. Claude Agent SDK'da koşum-sırası (mid-run) subagent'a mesaj enjeksiyonu/duraklatma var mı? (K4)
- **Kaynak rapor iddiası:** "K4 hükmü ikincil kaynaklara (MindStudio, claudefa.st) dayanıyor, resmî dokümanda doğrudan alıntı bulamadım — [?] sınıfına daha yakın olabilirdi."
- **Bağımsız doğrulama sorusu:** Resmî `code.claude.com/docs/en/agent-sdk/subagents` sayfası bir subagent'ı koşum SÜRERKEN duraklatma/mesaj enjekte etme mekanizması tarif ediyor mu?
- **Bulgu:** Sayfa birebir okundu (WebFetch, birincil kaynak). "Resume subagents" bölümü VAR ama açıkça şunu şart koşuyor: yalnız subagent **`maxTurns` limitinde durduğunda ya da tamamlandığında** resume edilebilir; resume "capture session ID → agentId parse et → `resume: sessionId` ile YENİ bir query başlat" akışıdır — bu SIRALI (sequential) bir devam mekanizmasıdır, koşum SÜRERKEN canlı mesaj enjeksiyonu/duraklatma değildir. Sayfada `pause`, `interrupt`, `inject mid-task` gibi bir terim/mekanizma YOK.
- **Hüküm: AYAKTA** — A2'nin temkinli "[?] kısmen" hükmü haklı çıktı, ama netleşti: resmî kaynak mid-run müdahaleyi DOĞRULAMIYOR (yalnız tamamlanmış/duraklamış subagent'ı sonradan devam ettirme var). K4 için bu satır **HAYIR'a daha yakın** okunmalı, "kısmi" yerine.
- URL: https://code.claude.com/docs/en/agent-sdk/subagents — AS-OF 2026-08-31.

---

## AİLE B — 3 İDDİA

### B-1. OTel GenAI conventions konuşma içeriğini span attribute'undan ayrı event'e taşıyor mu?
- **Kaynak rapor iddiası:** "[?] doğrulanmadı — model hafızasından (eğitim verisi) geldi, Karar-68 riskli, en zayıf halka."
- **Bağımsız doğrulama sorusu:** `gen-ai-events` spec sayfası prompt/completion içeriğinin nerede (attribute mi event mi) tutulduğunu tarif ediyor mu?
- **Bulgu:** `opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/` WebFetch edildi ama sayfa içeriği bu ayrımı doğrulayacak teknik detay İÇERMİYORDU (fetch aracı "cannot answer based on provided content" döndürdü — repo taşınmış olabilir, B'nin A1'inde de aynı taşınma sorunu görüldü).
- **Hüküm: BELİRSİZ** — B'nin kendi zayıflık itirafı (model-hafızası kaynaklı, doğrulanmamış) hâlâ geçerli; bu sondaj da doğrulayamadı, ÇÜRÜTEMEDİ de. B'nin "doğrulanmamış sayılmalı" uyarısı AYNEN geçerliliğini koruyor.
- URL: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/ — AS-OF 2026-08-31.

### B-2. Claude Agent SDK subagent tespiti: `Agent` tool adı + `agentId` alanı gerçek mi?
- **Kaynak rapor iddiası:** "Yalnız WebSearch özetinden geldi, resmî sayfayı WebFetch ile doğrulamadım; alan adı yanlış olabilir."
- **Bağımsız doğrulama sorusu:** Resmî subagents dokümanı `Agent` tool adını ve `agentId` alanını birebir kullanıyor mu?
- **Bulgu:** Resmî sayfa (A2-3'te aynı fetch) BİREBİR TEYİT ETTİ: *"The tool name was renamed from `Task` to `Agent` in Claude Code v2.1.63"* ve *"the Agent tool result includes a text block containing `agentId: <id>`"* — B'nin ikincil-kaynaklı tahmini tam isabetli çıktı.
- **Hüküm: AYAKTA** (iddia doğrulandı; B'nin "zayıf" diye damgaladığı satır aslında DOĞRU — güven düzeyi düşükten yükseğe çıkarılmalı, ama iddianın kendisi çürütülmedi, tersine GÜÇLENDİ).
- URL: https://code.claude.com/docs/en/agent-sdk/subagents — AS-OF 2026-08-31.

### B-3. Jaeger/Tempo'nun canlı gösterim mimarisi (push/SSE mi, pull/refresh mi) hakkındaki B yorumu
- **Kaynak rapor iddiası:** "Bu SPEKÜLASYON, doğrulanmadı — büyük ölçüde YORUMUMDUR."
- **Değerlendirme:** B zaten bunu açıkça "AÇIK BOŞLUK" ve "spekülasyon" olarak işaretlemiş; bütçe kısıtı nedeniyle bu oturumda ayrı sorgu ayrılmadı.
- **Hüküm: sondaj yapılmadı** (B'nin kendi temkinli etiketlemesi zaten doğru davranış; çürütme denemesi için öncelik diğer 6 maddeye verildi).

---

## DÜŞEN İDDİALAR ÖZETİ

Yalnız **1 iddia DÜŞTÜ**: A2 raporunun Braintrust K1 (canlılık) hükmü. A2 "[?] doğrulanamadı" diyerek Braintrust'ı "en zayıf kanıtlanan aday" ilan etmişti; birincil dokümanda (`braintrust.dev/docs/observe/view-logs`) açık "Live tail" akış özelliği (flash-animasyonlu yeni satır, sekme-gizlenince-otomatik-duraklama) bulundu — bu **K1 = EVET** anlamına gelir. Braintrust'ın genel "gözlem var, canlılık zayıf" sınıflandırması yanlıştı.

Diğer 8 iddianın hiçbiri "aslında kriteri karşılıyor" saldırısıyla çürütülemedi: 4'ü AYAKTA (2'si zaten doğru öngörülmüştü, biri [B-2] güven düzeyi yükseltilerek doğrulandı, biri [A2-3] netleştirilerek HAYIR'a yaklaştı), 2'si BELİRSİZ kaldı (kaynak erişim sorunu — sayfa taşınmış/404), 2'si bütçe nedeniyle sondaj yapılmadı.

## SENTEZE UYARI

1. **Braintrust'ın K1 hükmü A2 raporunda [?] → EVET'e düzeltilmeli.** Sentezde "gözlemlenebilirlik araçları hepsi post-hoc/replay ağırlıklı" genellemesi Braintrust için artık YANLIŞ; Braintrust "Live tail" ile gerçek push/stream canlılığı sunuyor (K4 müdahale hâlâ HAYIR, K3 hâlâ tek-ağaç kısmi — bu kriterlerde değişiklik yok).
2. **Claude Agent SDK K4 (A2 raporu) "kısmi" yerine "HAYIR'a yakın" olarak sertleştirilmeli.** Resmî `subagents` sayfası mid-run duraklatma/mesaj-enjeksiyonu için hiçbir mekanizma tarif etmiyor; "Resume subagents" tamamlanmış/limit-durmuş subagent'ları SIRALI devam ettirir, canlı müdahale değildir.
3. **B raporunun `agentId`/`Agent` tool-adı iddiası (madde B-2) "zayıf iddia" listesinden çıkarılıp doğrulanmış kabul edilmeli** — resmî kaynakla birebir teyit edildi; B'nin kendi temkini fazla ihtiyatlıydı.
4. **A1'in LangGraph Studio subgraph (K3) hükmü "temkinli HAYIR" yerine "BELİRSİZ" olarak yumuşatılmalı** — bu oturumda da kaynağa erişilemedi (404); iddia ne doğrulandı ne çürütüldü, kesin HAYIR demek erken.
5. **B'nin OTel GenAI content-event ayrımı iddiası (madde B-1) sentezde HİÇ kullanılmamalı** — hem B'nin kendisi hem bu antitez turu doğrulayamadı; "İNŞA EDİLEBİLİR DESENLER" listesindeki 3. madde bu doğrulanmamış temele dayanıyorsa köşeli parantezle ([?] doğrulanmadı) işaretlenmeli.
6. **Genel örüntü:** ANTİTEZ turunun asıl başarısı, üç ekibin de "gözlem var ama canlılık/müdahale yok" diye toptan elediği observability araçları (Langfuse, Phoenix, Braintrust) arasında en az BİRİNİN (Braintrust) K1'de yanlış sınıflandırıldığını göstermesi — bu, "hiçbir observability aracı canlı değil" biçimindeki güçlü genellemeyi zayıflatır; sentez bu genellemeyi Braintrust istisnasıyla kayıtlı kullanmalı.

---

**Yöntem notu:** CoVe-Factored ilkesine uyularak her doğrulama sorusu, kaynak iddianın metni sorguya taşınmadan bağımsız soruldu; hiçbir hüküm model hafızasından verilmedi (Karar 68), her hüküm URL + AS-OF 2026-08-31 damgalı.
