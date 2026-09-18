# Atlas Antitez Raporu — Aile B (pratisyen sistemler ve açık-kaynak orkestratörler)

**Tarih:** 2026-09-18
**Rol:** ANTİTEZ (Devil's Advocate) — yalnız iddia listesi verildi, gerekçe/kaynak çıpalanmadı
**Disiplin:** her karşı-kanıt URL'li + AS-OF (yayın·çekim) + model/kuşak sürümü; hüküm ÇÜRÜDÜ / DARALDI / ÇÜRÜTÜLEMEDİ

---

## İddia 1 — Anthropic: Opus lider / Sonnet paralel, gerekçe paralellik+bağlam-sıkıştırma
**¬T arama:** Anthropic'in resmî mühendislik yazısı gerekçeyi doğrudan doğruluyor.
> "Subagents facilitate compression by operating in parallel with their own context windows, exploring different aspects of the question simultaneously before condensing the most important tokens for the lead research agent."
**Kaynak:** [Anthropic — How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) — AS-OF: yayın 2025-06-13 (Simon Willison arşivi teyidiyle), çekim 2026-09-18. Kuşak: Opus 4 (lider) + Sonnet 4 (alt-ajan).
**Not:** Opus'un neden Sonnet yerine lider seçildiğine dair ayrı bir gerekçe metinde yok; yalnız genel performans/verimlilik argümanı var (ör. "upgrading to Claude Sonnet 4 is a larger performance gain than doubling the token budget").
**Hüküm: ÇÜRÜTÜLEMEDİ** — ¬T bulunamadı, birincil kaynak T'yi doğruluyor.

## İddia 2 — Cognition (Devin): paralel çok-ajan terk, tek-ajan + sıralı dar soru-cevap alt-ajan
**¬T arama:** Cognition'ın kendi blog yazısı iddiayı neredeyse birebir dille doğruluyor.
> "Claude Code is an example of an agent that spawns subtasks. However, it never does work in parallel with the subtask agent, and the subtask agent is usually only tasked with answering a question, not writing any code."
**Kaynak:** [Cognition — Don't Build Multi-Agents](https://cognition.com/blog/dont-build-multi-agents) — AS-OF: yayın 2025-06-12, çekim 2026-09-18.
**Hüküm: ÇÜRÜTÜLEMEDİ** — birincil kaynak T'yi teyit ediyor, ¬T yok.

## İddia 3 — Claude Code alt-ajanları varsayılan hafızasız, `memory` alanı etkin değilse kimlik taşımaz
**¬T arama:** Resmî dokümantasyon aynı sınırı tanımlıyor; `memory` alanı 2026-02'de (v2.1.33) eklendi, öncesinde her çağrı sıfırdan başlıyordu.
> "Every subagent has its own memory directory — your code-reviewer subagent's MEMORY.md is invisible to your security-auditor subagent."
**Kaynak:** [Claude Code Docs — Create custom subagents](https://code.claude.com/docs/en/sub-agents) — AS-OF: çekim 2026-09-18, özellik girişi v2.1.33 (2026-02).
**Hüküm: ÇÜRÜTÜLEMEDİ** — T doğrulandı, ¬T bulunamadı.

## İddia 4 — model katmanlaması elle atanır, perspektife göre otomatik atama yok
**¬T arama:** `model` alanının varsayılanı `inherit` — ebeveyn oturumun modelini **otomatik** devralır; bu "yalnız elle atanır" çerçevesini daraltıyor (perspektife göre değil ama otomatik-inherit var).
> "The model field on a subagent accepts an alias (sonnet, opus, haiku), a full model ID such as claude-opus-4-8, or inherit, and defaults to inherit."
**Kaynak:** [Claude Code Docs — Create custom subagents](https://code.claude.com/docs/en/sub-agents) — AS-OF: çekim 2026-09-18.
**Hüküm: DARALDI** — "perspektife göre otomatik atama yok" kısmı ayakta; "yalnız elle atanır" kısmı yanlış (varsayılan otomatik-inherit var).

## İddia 5 — MetaGPT: PM/Mimar/Proje Yöneticisi/Mühendis/QA ayrı ajan
**¬T arama:** Resmî README doğruluyor.
> "MetaGPT includes product managers / architects / project managers / engineers."
**Kaynak:** [GitHub — FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) — AS-OF: en son haber girdisi 2025-03-10, çekim 2026-09-18. (QA rolü README alıntısında açıkça geçmedi, ikincil kaynaklarla [IBM](https://www.ibm.com/think/topics/metagpt) teyit edildi.)
**Hüküm: ÇÜRÜTÜLEMEDİ.**

## İddia 6 — AG2: critic/verifier üreticiden ayrı kurulur (hatalı çıktının yayılmasını önleme gerekçesi)
**¬T arama:** Doğrudan AG2 resmî sayfasında net "critic ayrı kurulur, gerekçe X" cümlesi bulunamadı; deseni açıklayan ikincil kaynaklar (Producer-Critic Pattern, Verifier Pattern) desteği veriyor ama AG2'ye özgü birincil alıntı zayıf.
> "The multi-step approach tends to be more reliable because it separates the 'creator' and 'critic' mindsets, reducing the tendency for models to rubber-stamp their own work."
**Kaynak:** [Agentic Design — Producer-Critic Pattern](https://agentic-design.ai/patterns/reflection/producer-critic) — AS-OF: çekim 2026-09-18 (sayfada yayın tarihi yok). AG2 GitHub'ı ([ag2ai/ag2](https://github.com/ag2ai/ag2)) çekildi, "Critic" örnek deseni geçiyor ama gerekçe cümlesi doğrulanamadı.
**Hüküm: ÇÜRÜTÜLEMEDİ** — ama kanıt AG2'ye özgü birincil kaynaktan değil, genel desen literatüründen; zayıf teyit olarak işaretlenir.

## İddia 7 — supervisor-worker "en yaygın kanıtlanmış" topoloji
**¬T arama:** 2026 üretim verisi tam tersini değil, T'yi güçlendiriyor.
> "Supervisor/Star topology accounts for 70% of production scenarios."
**Kaynak:** ikincil sentez [FutureAGI — Multi-Agent AI Systems in 2026](https://futureagi.com/blog/multi-agent-systems-2025/) ve ilişkili 2026 üretim retrospektifleri — AS-OF: çekim 2026-09-18, veri damgası [?] (birincil anket bulunamadı, toplulaştırılmış blog rakamı).
**Hüküm: ÇÜRÜTÜLEMEDİ** — rakam [?] işaretli (birincil anket yok) ama yön T'yi destekliyor, ¬T bulunamadı.

## İddia 8 — OpenHands 2025-11 SDK varsayılan tek-ajan, çok-ajan orkestrasyon öntanımlı değil
**¬T arama:** Birincil arXiv metninde (2511.03690) açık "varsayılan tek-ajan" cümlesi bulunamadı (soyut erişimle sınırlı). Repo yapısı dolaylı destek veriyor: alt-ajan devri ayrı bir alt-modülde (`openhands/sdk/subagent/`) belgeleniyor, çekirdek `Conversation`/`Agent` akışından ayrık.
**Kaynak:** [OpenHands/agent-sdk — AGENTS.md](https://github.com/OpenHands/agent-sdk/blob/main/AGENTS.md) — AS-OF: çekim 2026-09-18. [arXiv 2511.03690](https://arxiv.org/abs/2511.03690) — yayın 2025-11, çekim 2026-09-18 (yalnız özet erişildi, 403/kilit yok ama tam metin taranamadı).
**Hüküm: ÇÜRÜTÜLEMEDİ (zayıf/dolaylı kanıt)** — doğrudan "varsayılan tek-ajan" cümlesi bulunamadı; ¬T de bulunamadı.

## İddia 9 — pratisyenler arasında kişisel tutor ajanını ayrı kanonla kuran vaka yok
**¬T arama:** [amosblomqvist/learn](https://github.com/amosblomqvist/learn) incelendi — öğretim mantığı ayrı bir tutor-ajanı değil, `skills/teach/` altında bir **beceri (skill)** olarak kodlanmış; alt-ajanlar (researcher, svg-maker, mermaid-maker) öğretimden ayrı görevler. Microsoft ATLAS ([techcommunity.microsoft.com](https://techcommunity.microsoft.com/blog/educatordeveloperblog/atlas-your-ai-tutoring-agent-for-personalised-learning/4450466)) kurumsal bir ürün, "pratisyen" (bireysel/açık-kaynak) vakası değil.
**AS-OF:** çekim 2026-09-18, repo tarihleri README'de belirtilmemiş.
**Hüküm: ÇÜRÜTÜLEMEDİ** — arananlar arasında ayrı-kanonlu kişisel tutor ajanı vakası bulunamadı.

## İddia 10 — Microsoft Ekim 2025'te AutoGen'i bakım moduna aldı; AG2 + Microsoft Agent Framework'e ikiye ayrıldı
**¬T arama:** Kronoloji hatalı — AG2 çatallanması Ekim 2025'in **öncesinde**, Kasım 2024'te bağımsız yönetişimle kuruldu; Ekim 2025'teki olay AutoGen'i bakım moduna almak + Semantic Kernel ile birleştirip Microsoft Agent Framework'ü duyurmaktı (GA 2026-04-03, önizleme 2025-10-01), AG2'yi o an "doğurmadı".
> "AG2 is a separate community fork at ag2ai/ag2... governance structure established when the fork was created in November 2024."
> "Microsoft folded AutoGen ... into Semantic Kernel ... and shipped the result as a single Microsoft Agent Framework in October 2025."
**Kaynak:** [docs.ag2.ai — DefaultPattern](https://docs.ag2.ai/latest/docs/api-reference/autogen/agentchat/group/patterns/pattern/DefaultPattern/) ve ilişkili arama kaydı; [Alex Bevilacqua — Two Lineages, One Framework](https://alexbevi.com/blog/2026/06/18/two-lineages-one-framework-how-autogen-and-semantic-kernel-became-the-microsoft-agent-framework/) — AS-OF: yayın 2026-06-18, çekim 2026-09-18.
**Hüküm: DARALDI** — "bakım moduna alma, Ekim 2025" doğru; ama "AG2'ye ikiye ayrıldı" o tarihte olmadı, AG2 zaten 11 ay önceden vardı — iddianın nedensellik/zamanlama kısmı yanlış çerçevelenmiş.

## İddia 11 — Claude Code'da yalnız `context: fork` dışında alt-ajanlar ebeveynin konuşma geçmişini devralmaz
**¬T arama:** v2.1.232 (2026-08-13) itibarıyla etkileşimli oturumlarda fork **varsayılan** davranış oldu; yani "yalnız açık `context: fork` istisnası" çerçevesi artık güncel değil.
> "Claude Code fork subagents went from an opt-in experiment to the default behavior in interactive sessions with version 2.1.232, released on August 13, 2026... off by default in non-interactive mode and the Agent SDK."
**Kaynak:** ikincil sentez, birincil doğrulama gerekli — [daniliants.com — Claude Code forked subagents inherit the parent session context](https://daniliants.com/insights/claude-code-released-forked-subagents/) — AS-OF: çekim 2026-09-18 (birincil changelog doğrudan açılamadı, 403/erişim kısıtı bayrağı).
**Hüküm: DARALDI** — etkileşimli-oturum bağlamında varsayılan artık devralma yönünde kaydı; kural yalnız non-interactive/SDK modunda hâlâ geçerli. Kaynak birincil değişiklik güncesi ile teyit edilemedi (bayrak: ikincil kaynağa dayalı).

## İddia 12 — pratisyen kaynakların hiçbiri antitez/red-team rolünü ayrı kalıcı ajan sınıfı olarak tanımlamaz
**¬T arama:** En az bir kaynak doğrudan tanımlıyor ve critic/değerlendirme fonksiyonundan açıkça ayırıyor (güvenlik/MDR alanında).
> "A red team agent in agentic AI–based MDR is an autonomous or semi-autonomous AI agent designed to continuously emulate adversary behavior within an enterprise environment" — critic/değerlendirme fonksiyonlarından ayrı, kalıcı bir "adversarial simulator" sınıfı olarak konumlandırılıyor.
**Kaynak:** [Deepwatch — What Is a Red Team Agent in Agentic AI MDR?](https://www.deepwatch.com/glossary/red-team-agent-in-agentic-ai-mdr/) — AS-OF: çekim 2026-09-18 (sayfada yayın tarihi yok). Destekleyici ikincil: [Rapid7 — Formalizing Red Teaming Offensive Methodology as a Multi-Agent AI Architecture](https://www.rapid7.com/blog/post/so-red-teaming-offensive-methodology-multi-agent-ai-architecture/).
**Hüküm: ÇÜRÜDÜ** — "hiçbiri" evrensel-olumsuz iddiası tek karşı-örnekle düşer; kapsam notu: bulunan kaynak genel-amaçlı ajan orkestrasyonu değil, güvenlik/MDR alanına özgü — iddianın "genel pratisyen literatürü" kastıysa alan-dışı sayılabilir, ama "hiçbiri" ifadesi tam olarak yanlışlanıyor.

---

## Açılan Kaynak Sayısı
WebFetch ile fiilen açılan URL sayısı: **9** (Cognition blog, Anthropic engineering, Deepwatch glossary, amosblomqvist/learn README, MetaGPT README, arXiv 2511.03690 özeti, docs.openhands.dev/sdk, OpenHands agent-sdk AGENTS.md, docs.openhands.dev/sdk/guides/agent-delegation [404]) + çok sayıda WebSearch sentez sonucu (ikincil, birincil doğrulama zayıf yerlerde bayraklandı).

## Özet Tablo

| # | Hüküm | Tek cümle |
|---|---|---|
| 1 | ÇÜRÜTÜLEMEDİ | Anthropic'in kendi mühendislik yazısı paralellik+bağlam-sıkıştırma gerekçesini doğruluyor. |
| 2 | ÇÜRÜTÜLEMEDİ | Cognition'ın kendi blogu Devin'in sıralı, kod-yazmayan dar alt-ajan modelini teyit ediyor. |
| 3 | ÇÜRÜTÜLEMEDİ | Resmî doküman `memory` alanı olmadan alt-ajanların sıfırdan başladığını doğruluyor. |
| 4 | DARALDI | Varsayılan "inherit" otomatik atama var; yalnız "perspektife göre" otomatik atama yok. |
| 5 | ÇÜRÜTÜLEMEDİ | MetaGPT README'si PM/mimar/proje-yöneticisi/mühendis rollerini ayrı ajan olarak doğruluyor. |
| 6 | ÇÜRÜTÜLEMEDİ (zayıf) | Genel desen literatürü critic/üretici ayrımını destekliyor, AG2'ye özgü birincil alıntı zayıf. |
| 7 | ÇÜRÜTÜLEMEDİ | 2026 üretim verisi supervisor/star topolojisinin baskın olduğunu gösteriyor ([?] rakam). |
| 8 | ÇÜRÜTÜLEMEDİ (zayıf/dolaylı) | Alt-ajan devri ayrı belgelenmiş modül, ama "varsayılan tek-ajan" doğrudan alıntılanamadı. |
| 9 | ÇÜRÜTÜLEMEDİ | İncelenen pratisyen repo'da öğretim ayrı ajan değil skill olarak kurulmuş, karşı-vaka yok. |
| 10 | DARALDI | AG2 çatallanması Ekim 2025'ten önce (Kasım 2024) oldu; Ekim 2025 olayı bakım-modu + Agent Framework birleşimiydi. |
| 11 | DARALDI | v2.1.232'den (2026-08-13) beri etkileşimli oturumlarda fork varsayılan; istisna artık kural. |
| 12 | ÇÜRÜDÜ | Deepwatch red-team ajanını critic'ten ayrı kalıcı sınıf olarak tanımlıyor; kapsam güvenlik/MDR'a özgü. |

**Epistemolojik not:** Bu rapor 2026-09-18 itibarıyla erişilebilir web kanıtına dayanır; bazı birincil kaynaklar (OpenHands arXiv tam metni, AG2 resmî critic-pattern sayfası, Claude Code v2.1.232 changelog'u) doğrudan açılamadı — bu satırlar "zayıf/dolaylı kanıt" olarak bayraklandı.
