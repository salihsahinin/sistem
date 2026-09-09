# IB-75 Tez C — Yetki-sınırlı lider / guardrail deseni (dış kanıt taraması)

**Künye:** İşçi-ajan (tez, aile C, karar yetkisiz) · tarih 2026-09-09 · araç bütçesi 10-15 (kullanılan: 6 WebFetch + 5 WebSearch) · zorunlu kota: ≥2 birincil kaynak fiilen açıldı (4 açıldı).

## İddia Listesi

**C1 — OpenAI Agents SDK guardrail/tripwire mekanizması.** `@input_guardrail` / `@output_guardrail` dekoratörleriyle tanımlanır; guardrail fonksiyonu `GuardrailFunctionOutput` üretir, `tripwire_triggered=True` olursa sistem `InputGuardrailTripwireTriggered` / `OutputGuardrailTripwireTriggered` istisnasını fırlatıp ajan yürütmesini DURDURUR. Girdi guardrail'i `run_in_parallel=False` (bloklayıcı) modda ajan hiç başlamadan tamamlanır — token/araç harcaması önlenir; varsayılan paralel modda ajan kısmen çalışmış olabilir, sonra iptal edilir. Üçüncü tür: tool guardrail (araç çağrısı öncesi/sonrası doğrulama), `ToolInputGuardrailTripwireTriggered` / `ToolOutputGuardrailTripwireTriggered`.
**D** — https://openai.github.io/openai-agents-python/guardrails/ — AS-OF 2026-09-09 (çekim tarihi; sayfa güncelleme tarihi belirtilmemiş)

**C2 — LangGraph `interrupt()` insan-onay mekanizması.** `interrupt()` bir düğüm/middleware'in `after_model` kancasında çağrılır (örn. araç çağrısı tespit edilince `HITLRequest` inşa edilip `interrupt` tetiklenir); graf durumu checkpointer (persistence layer) ile KAYDEDİLİR ve yürütme donar — onay bekleyen araç çağrısı ÇALIŞMAZ. Devam etmek için aynı `thread_id` ile `Command(resume={"decisions":[...]})` gönderilir; her karar bekleyen eyleme sırayla eşlenir (approve/edit/reject/respond). Checkpointer + thread_id ZORUNLU ön koşul; yoksa mekanizma çalışmaz.
**D** — https://docs.langchain.com/oss/python/langchain/human-in-the-loop — AS-OF 2026-09-09 (çekim; sayfanın kendi güncelleme tarihi görünmüyor)

**C3 — CrewAI `human_input` / `allow_delegation=False`.** Task nesnesinde `human_input=True` set edilince ajan nihai cevabı vermeden ÖNCE kullanıcıdan girdi istiyor (bloklayıcı akış); bu, agent'ın `allow_delegation` ayarından BAĞIMSIZ çalışır. `allow_delegation=False` ajanın diğer ajanlara görev DELEGE ETMESİNİ engelliyor (delegasyon derinliği freni). Ancak dokümantasyon reddetme/feedback sonrası akışın nasıl işlediğini (agent muhakemesine nasıl geri beslendiği) AÇIKLAMIYOR — bu bir doküman boşluğu, spekülasyon yapmadım.
**D** (mekanizma var, ayrıntı kısmi) — https://docs.crewai.com/en/learn/human-input-on-execution — AS-OF 2026-09-09 (çekim)

**C4 — Claude Code / Agent SDK izin değerlendirme sırası (6 adım).** Sıra: (1) Hooks — `PreToolUse` hook deny'i `bypassPermissions` modunda BİLE geçerli; (2) Deny rules (`disallowed_tools`/settings.json) — eşleşirse her modda bloklar; (3) Ask rules — eşleşirse `canUseTool` callback'ine düşer; (4) Permission mode uygulanır (`bypassPermissions` kritik-yol `rm`/`rmdir` hariç her şeyi onaylar; `plan` modu dosya-yazma araçlarını HER ZAMAN callback'e yönlendirir — allow rule olsa bile); (5) Allow rules; (6) `canUseTool` callback (çözülmemişse). `dontAsk` modunda callback ATLANIR, önceden onaylanmamış her şey REDDEDİLİR. Kritik saptama: `allowed_tools` TEK BAŞINA `bypassPermissions` modunu KISITLAMAZ — listelenmeyen araçlar mode adımına düşer ve bypass onaylar; kısıtlama için `disallowed_tools` gerekir.
**D** — https://code.claude.com/docs/en/agent-sdk/permissions — AS-OF 2026-09-09 (çekim; sayfa sürümü v2.1.199+/v2.1.218+/v2.1.259+ referansları içeriyor, yani güncel tutuluyor)

**C5 — LangGraph derinlik/döngü freni: `recursion_limit`.** Varsayılan sıklıkla 25 (kaynak "often set to 25" diyor, kesin varsayılan değeri doğrulayamadım [?]); her düğüm çalışması sayılır, aşılırsa `GraphRecursionError` fırlatılır (crash guard — hüküm değil, sert durdurma). Alt-graf (subgraph) düğümleri üst grafın limitine SAYILIR (delegasyon derinliği freni buradan geliyor — iç içe ajan çağrıları toplam sayaca eklenir). Ayrıca ayrı bir `max_iterations` state alanı önerilir (yumuşak çıkış, kullanıcı router mantığıyla kontrol eder) — ikisinin BİRLİKTE kullanılması öneriliyor.
**K** (ikincil/blog kaynaklı özet, "genelde 25" ifadesi resmi API referansından değil) — https://machinelearningplus.com/gen-ai/langgraph-cycles-recursion-limits-agent-loops/ — AS-OF 2026-09-09 (çekim; makale tarihi belirsiz)

**C6 — "Ajan öner, insan karar ver" desenine dair sayısal vaka/ölçüm.** Taramada NET, sayısal ("approval rate X%", "override rate Y%") bir vaka raporu BULAMADIM. En yakın bulgu: bir survey/rapor türü kaynakta "%74 human-in-the-loop değerlendirmeye dayanıyor" ifadesi geçiyor (hangi popülasyon/metodoloji belirsiz — birincil kaynağı açıp doğrulamadım, sadece arama özetinden). İkinci bulgu: incident-response bağlamında geri-alınamaz/yüksek-etkili eylemler (uç nokta silme, kimlik bilgisi iptali, prod politika değişikliği) için EXPLICIT insan onayı gerektiği ifade ediliyor, ama bu normatif bir öneri, ölçüm değil. arXiv 2510.09801 (insan-ajan etkileşimi değerlendirme makalesi) doğrudan açıldı — bu makalede onay/red oranı YOK; bulduğu tek ilişkili veri: düşük memnuniyet durumunda kullanıcıların ajanla etkileşimi azalttığı (mesaj sayısı %32 az, kod push %16 az) — bu ONAY MEKANİZMASI ölçümü DEĞİL, memnuniyet/kullanım korelasyonu.
**X** (aranan türde sayısal vaka raporu bulunamadı) — arama sonucu özetleri: idalko.com/blog/humans-approve.-agents-investigate, panther.com/blog/ai-incident-response, arxiv.org/pdf/2512.04123 — AS-OF 2026-09-09 — [%74 rakamı URL'siz doğrudan doğrulanmadı, ikincil arama-özeti üzerinden — doğrulanmadı]

## Açılan Kaynaklar (WebFetch ile fiilen açılan, birincil)
1. https://openai.github.io/openai-agents-python/guardrails/
2. https://docs.langchain.com/oss/python/langchain/human-in-the-loop
3. https://docs.crewai.com/en/learn/human-input-on-execution
4. https://code.claude.com/docs/en/agent-sdk/permissions
5. https://arxiv.org/html/2510.09801v1 (açıldı, konuyla ilgili sayısal veri içermiyor — negatif sonuç)

## AÇIK SORULAR
- AÇIK SORU: CrewAI `human_input=True` reddedilirse (feedback negatifse) tam olarak ne oluyor — tekrar mı deniyor, ajan hatasız mı çıkıyor? Doküman bunu açıklamıyor, ayrı bir kaynak/kod incelemesi gerekir.
- AÇIK SORU: LangGraph `recursion_limit` varsayılan değeri (25) resmi API referansından doğrulanmadı — yalnız ikincil blog kaynağında geçti.
- AÇIK SORU: "Ajan öner, insan karar ver" deseninin SAYISAL etkisini (onay/red oranı, hata azaltma oranı) gösteren birincil, hakemli/kurumsal bir vaka raporu bulunamadı; bu C6'da X olarak işaretlendi. Daha derin arama (örn. Anthropic/OpenAI kendi vaka çalışmaları, güvenlik ekibi raporları) ayrı bir hat gerektirir.
- AÇIK SORU: OpenAI Agents SDK'da guardrail ihlali sonrası akışın (istisna yakalanınca kullanıcıya ne gösterileceği, retry politikası) çağıran kod tarafında mı yoksa SDK içinde varsayılan mı olduğu netleşmedi.
