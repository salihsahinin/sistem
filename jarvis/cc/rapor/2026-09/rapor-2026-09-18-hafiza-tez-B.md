# Atlas TEZ raporu — aile B: akademik hafıza taksonomileri ve kendini-geliştiren ajan literatürü

**Tarih:** 2026-09-18
**Araştırmacı:** atlas (TEZ rolü)
**Kapsam:** kalıcı ajan hafızası katmanlama, büyüme/damıtma/unutma ölçümleri, kendini-geliştiren hafıza frenleri, çok-ajan izolasyon/paylaşım.
**Yöntem notu:** yalnız web; WebFetch ile 4 kaynak gerçekten açıldı (gövde metninden alıntı alındı); geri kalanı WebSearch özetiyle sınırlı — bu kaynaklar TAKSONOMİ/BAĞLAM için kullanıldı, sayısal iddia YALNIZ açılan kaynaklardan alındı.

## 1. Kaynak listesi

| # | Kaynak | AS-OF (yayın) | Açıldı mı | Model/ölçek (deneyde) |
|---|---|---|---|---|
| K1 | arXiv:2603.07670v1 — "Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers" (Pengfei Du) | 2026-03-08 (çekim 2026-09-18) | KISMEN — abstract HTML'den doğrulandı; PDF gövdesi sıkıştırılmış geldi, sayısal iddia buradan ALINMADI (güvenilmez çıktı, aşağıda not) | belirtilmemiş |
| K2 | arXiv:2605.13941v1 — "EvolveMem: Self-Evolving Memory Architecture via AutoResearch for LLM Agents" | 2026-05-13 (çekim 2026-09-18) | EVET — HTML sürümünden gövde metni alıntılandı | GPT-4o, GPT-5.1 (Azure OpenAI API) |
| K3 | arXiv:2602.19320v1 — "Anatomy of Agentic Memory: Taxonomy and Empirical Analysis of Evaluation and System Limitations" (Jiang, Li, Wei ve ark., UT Dallas/UC Davis/Texas A&M) | 2026-02-22 (çekim 2026-09-18) | EVET — HTML sürümünden gövde metni alıntılandı | gpt-4o-mini (API), Qwen-2.5-3B (açık ağırlık) |
| K4 | arXiv:2606.24535v1 — "Governed Shared Memory for Multi-Agent LLM Systems" (Margalit, Cohen-Inger, Avram, Taig, Margalit) | 2026-06-23 (çekim 2026-09-18) | EVET — HTML sürümünden gövde metni alıntılandı | belirtilmemiş (mimari odaklı, LLM sürümü verilmemiş) |
| K5 | arXiv:2607.01480v1 — "Procedural Memory Distillation: Online Reflection for Self-Evolving Agents" (Liu, Bansal, Pang ve ark.) | 2026-07-03 (çekim 2026-09-18) | KISMEN — yazar/benchmark listesi doğrulandı; sayısal kazanç tabloları PDF sıkıştırmasından ÇIKARILAMADI (güvenilmez, kullanılmadı) | Qwen 3, DeepSeek-R1, SDPO-varyantları (karşılaştırma); değerlendirme: SciKnowEval, LiveCodeBench, DeepSeek-Math |
| K6 | arXiv:2606.20475 — "Marginal Advantage Accumulation for Memory-Driven Agent Self-Evolution" | 2026-06 [?] | HAYIR — yalnız WebSearch özeti | bilinmiyor |
| K7 | arXiv:2606.17628 — "OPD-Evolver: Cultivating Holistic Agent Evolver via On-Policy Distillation" | 2026-06 [?] | HAYIR — yalnız WebSearch özeti | bilinmiyor |
| K8 | arXiv:2603.10062v1 — "Multi-Agent Memory from a Computer Architecture Perspective" | 2026-03-09 | HAYIR — yalnız WebSearch özeti | bilinmiyor |
| K9 | arXiv:2606.19911v1 — "Multi-Agent Transactive Memory" | 2026-06-19 | HAYIR — yalnız WebSearch özeti | bilinmiyor |
| K10 | arXiv:2601.09113 — "The AI Hippocampus: How Far are We From Human Memory?" | 2026-01 [?] | HAYIR — yalnız WebSearch özeti | bilinmiyor |
| K11 | arXiv:2603.11768 — "Governing Evolving Memory in LLM Agents: … Stability and Safety Governed Memory (SSGM)" | 2026-03 [?] | HAYIR — yalnız WebSearch özeti | bilinmiyor |
| K12 | GitHub Shichun-Liu/Agent-Memory-Paper-List (eşlik ettiği survey: "Memory in the Age of AI Agents: A Survey", arXiv:2512.13564) | liste hâlinde, çekim 2026-01 [?] | HAYIR — dizin/pointer amaçlı | — |

**403/paywall bayrağı:** yok, tüm arXiv kaynaklarına erişildi; ancak K1 ve K5'in PDF gövdesi WebFetch aracında "compressed PDF stream" hatasıyla döndü — bu kaynaklardan sayısal iddia ÇIKARILMADI, yalnız doğrulanabilir üst-veri (başlık/tarih/yazar/abstract) kullanıldı. Bu ihtiyat, aracın önceki denemede MemGPT/Voyager/RETRO gibi popüler isimleri "referans" diye üretmesi (K1 ilk denemede) — bu çıktı DOĞRULANAMADI ve rapora ALINMADI; olası halüsinasyon olarak işaretlenir.

## 2. Taksonomi tablosu

| Kaynak | Katmanlar | Not |
|---|---|---|
| K1 (WebSearch özeti + Nuanced Perspective blogu, birincil değil) | çalışma (working) · epizodik · prosedürel · semantik — 4 katman "tam yığın" iddiası, ancak "çoğu sistem yalnız 2 katmanı iyi uyguluyor, geçişleri kaba sezgiyle yönetiyor" | Bu satırdaki iddia BLOG kaynaklı (thenuancedperspective.substack.com), K1'in kendisi değil — kanıt hiyerarşisinde düşük, ayrı işaretlendi |
| K2 (EvolveMem) | epizodik · semantik · prosedürel (3 katman; "çalışma hafızası" ayrı ele alınmamış) | AutoResearch bileşeni memory açıklarını kendi tespit edip deney kurup iyileştiriyor iddiası (bkz. §4) |
| K3 (Anatomy of Agentic Memory) | 4 yapısal kategori: (1) hafif-semantik (append-only + vektör benzerliği) (2) varlık-merkezli/kişiselleştirilmiş (3) epizodik-yansıtıcı (temporal soyutlama + konsolidasyon) (4) yapılandırılmış/hiyerarşik (graf-tabanlı) | Bu, çalışma/epizodik/semantik/prosedürel yerine SİSTEM MİMARİSİ eksenli bir taksonomi — soru kalıbıyla birebir örtüşmüyor, çapraz-referans için değerli |
| K4 (Governed Shared Memory) | katman değil, YÖNETİŞİM ekseni: kapsam (scope), zamansal doğruluk (temporal correctness), köken (provenance), eşzamanlama (synchronization) | Çok-ajan bağlamında "hafıza katmanı" yerine "hafıza kontrolü" sorusuna cevap veriyor |

**Çelişki notu (m.16 türü):** soru metnindeki "çalışma/epizodik/semantik/prosedürel" dörtlemesi K2'de doğrulanıyor (epizodik+semantik+prosedürel, çalışma hafıza ayrı tartışılmamış), ama K3 bunu tümüyle farklı bir eksende (append-only vs. graf-tabanlı) yeniden çerçeveliyor. Yani "standart" bir taksonomi YOK — literatür bölünmüş; K1'in "4 katman aspirasyon, 2 katman gerçeklik" iddiası da ikinci elden (blog), doğrulanamadı.

## 3. Büyüme/damıtma/unutma ölçümleri (yalnız gerçekten açılan kaynaklardan)

**K2 — EvolveMem (LoCoMo benchmark, GPT-4o backbone):**
> "EvolveMem achieves an overall F1 of 0.543, outperforming SimpleMem (0.432) by 25.7% relative"
> "The largest gains appear in temporal (+63.4%) and single-hop (+68.7%) categories"
> minimal baseline'a göre genel iyileşme: "78.0% relative"

**K2 — LoCoMo, GPT-5.1 backbone:**
> "EvolveMem leads on all columns with an overall relative gain of 36.8% over SimpleMem"
> Temporal kategoride "98.9% relative improvement"

**K2 — MemBench:**
> "EvolveMem attains the best overall accuracy on both backbones (67.9% on GPT-4o, 71.4% on GPT-5.1), exceeding the strongest baseline by 18.9% relative"
> Recall "+40.0%", Reasoning "+33.4%"

Yorum: bunlar EvolveMem'in KENDİ makalesindeki sonuçlar (yazar-taraflı kıyas), bağımsız doğrulama yok — kanıt hiyerarşisinde "birincil dokümantasyon" ama tek-kaynaklı, çapraz-referans YOK.

**K3 — Anatomy of Agentic Memory (backbone bağımlılığı, model ölçeği etkisi):**
> Nemori sisteminde "30.38% format error" (Qwen-2.5-3B, küçük model) vs. "17.91%" (gpt-4o-mini, güçlü backbone) — "Silent Failure" adı verilen olgu: yapılandırılmış hafıza işlemleri zayıf backbone'da sessizce bozuluyor.
> Değerlendirme metriği uyumsuzluğu: "AMem achieves solid semantic performance (Rank 4)" ama F1 skoru 0.116 — "optimizing solely for F1 may favor surface-level memorization over genuine reasoning."
> Token ekonomisi: hafıza inşa maliyeti 1.3M–7.04M token arası (sistem başına değişken).
> Gecikme: MemoryOS "32+ saniye/tur" — hiyerarşik sayfalama nedeniyle.

Yorum: bu ÖLÇÜM, "hafıza büyümesi kalite/hata oranını nasıl etkiler" sorusuna dolaylı cevap veriyor — büyüme değil, MODEL GÜCÜ × hafıza-yapısı etkileşimi hata oranını belirliyor (küçük model + karmaşık yapılandırılmış hafıza = sessiz bozulma).

**Damıtma/sıkıştırma/unutma mekanizmalarının getirisi:** K5 (Procedural Memory Distillation) bu soruyu doğrudan hedefliyor ama sayısal tablo PDF sıkıştırmasından çıkarılamadı — RAPORA SAYI ALINMADI. K1'de de aynı sorun. Bu, "damıtma getirisi ne kadar" sorusunun bu taramada NİCEL olarak YANITSIZ kaldığı anlamına gelir; yalnız K2'nin (EvolveMem, kendi iddiası) genel iyileşme rakamları var, onlar da "damıtma" değil "genel mimari" karşılaştırması.

## 4. Kendini-geliştiren hafıza ve frenler

**K2 (EvolveMem/AutoResearch):** "autonomously identifies memory deficiencies, conducts targeted experiments, and improves memory quality without manual intervention" — yani AÇIKÇA insan-onayı OLMADAN çalışan bir döngü iddia ediliyor. Rapor kaynağında (WebFetch çıktısı) "guardrail implementation details" konusunda "obscured in the compressed content" notu var — yani insan-onay/fren mekanizmasının VAR olup olmadığı bu taramada DOĞRULANAMADI.

**K5 (Procedural Memory Distillation):** "online reflection" ile prosedürel hafıza damıtımı; insan-onay mekanizması makalede "Appendix C — Backbone and infrastructure" başlığı altında olabilir ama içerik bu taramada okunamadı. **BİLİNMİYOR** olarak işaretlenir.

**K4 (Governed Shared Memory) — negatif bulgu, fren YOKLUĞUNUN sonucu:** frensiz/az-denetimli şema evrimi somut arıza üretti:
> GET-by-id handler'ı "checked only tenant identity and discarded the resolved agent identity" — trust-level-1 bir ajan fleet-çapında izin dışı satırlara erişebildi (yetki-denetimi arızası, çalışırken keşfedilip düzeltildi).
> Eşzamanlı yakın-kopya (dedup) kapısı, asenkron çelişki dedektöründen ÖNCE çalıştığı için çelişkili yazmaları reddediyor: "A synchronous near-duplicate gate can reject contradictory writes before the asynchronous contradiction detector observes them" — genel çelişki tespit oranı bu yüzden %49'a düştü (admission'a giren çelişkilerin 90/90'ı doğru çözüldü, ama çoğu admission'a hiç giremedi).
> Semantik arama fleet-filtresini kısmen uyguladı: kesişim-dışı 100 probun 43.9'u (yaklaşık 44) yine de kısıtlı satırları gösterdi.

Bu üç bulgu, "kendini geliştiren/paylaşılan hafızada FREN eksikliği somut ölçülebilir arızaya yol açar" önermesini DOĞRUDAN ampirik olarak destekliyor — literatürdeki en somut "insan-onayı/denetim etkisi" kanıtı bu taramada burada.

## 5. Çok-ajan izolasyon/paylaşım

**K4 pozitif sonuçlar (denetimli paylaşım çalıştığında):**
> Köken (provenance) zinciri: "All 50 depth-four derivation chains reconstructed perfectly with correct writer identity (p50: 291ms per hop)"
> Fleet-içi görünürlük yayılımı: "97.5% (117/120 probes)"; fleet-dışı SIZINTI "zero … (0/80 probes)" — yani DOĞRU uygulanmış izolasyon sınırında sızıntı sıfır.
> Yazma-görünürlük gecikmesi: "p50: 0.83s" (güçlü mod).

**Kanıt-temelli sonuç:** izolasyon vs. paylaşım kararı bu makalede "ya/ya da" değil, KAPSAM-BAZLI (scope-based) yönetişim: fleet-içi paylaşım + fleet-dışı sıkı izolasyon + köken izleme. Kararı destekleyen kanıt: doğru uygulandığında sızıntı 0/80, yanlış uygulandığında (GET-by-id arızası) sızıntı somut şekilde gerçekleşti.

K8, K9, K10 (Multi-Agent Memory Architecture Perspective, Transactive Memory, AI Hippocampus) yalnız WebSearch özetiyle tarandı; K10'un "bazı yaklaşımlar gerçek-zamanlı paylaşımı, bazıları yalnız gerekli bilgi alışverişini önceliklendiriyor" notu İKİNCİL/doğrulanmamış — sayısal kanıt yok.

## 6. Çelişen bulgular

1. Taksonomi çelişkisi: soru kalıbındaki 4-katman (çalışma/epizodik/semantik/prosedürel) K2'de kısmen doğrulanıyor, K3'te TAMAMEN FARKLI bir eksenle (yapı-tabanlı: append-only/entity/episodic-reflective/hierarchical) değiştiriliyor — literatürde TEK bir kanonik taksonomi YOK.
2. "Kendini geliştiren hafıza insan-onayı gerektirir mi": K2 açıkça "without manual intervention" diyor (frensiz iddia), K4 ise frensiz/az-denetimli şema evriminin somut güvenlik ve çelişki-çözme arızalarına yol açtığını gösteriyor — K2'nin kendi güvenilirliği bu bulgu ışığında SORGULANABİLİR (K2 kendi güvenlik/doğrulama sürecini bu taramada gösteremedi).
3. Model ölçeği etkisi: K3 küçük modelde (Qwen-2.5-3B) yapılandırılmış hafızanın "sessizce" bozulduğunu (%30.38 format hatası) gösteriyor; K2 ise büyük modellerde (GPT-4o→GPT-5.1) hafıza mimarisi değişmeden performansın yükseldiğini gösteriyor (36.8%→98.9% temporal kazanç) — ikisi birlikte, "hafıza mimarisinin getirisi modelin gücüyle ölçekleniyor" yönünde YAKINSIYOR, ama K3 bunu AÇIK ARIZA olarak, K2 zımnen VARSAYIYOR (K2 küçük model denemedi).

## 7. İDDİA LİSTESİ (numaralı, tek cümle, gerekçesiz)

1. Literatürde çalışma/epizodik/semantik/prosedürel dört-katmanlı taksonomi evrensel kabul görmüyor; en az bir güncel survey (K3, 2026-02-22) tamamen farklı bir yapı-tabanlı eksen kullanıyor.
2. EvolveMem (K2, arXiv:2605.13941, 2026-05-13), LoCoMo'da GPT-4o backbone ile SimpleMem'e göre %25.7 rölatif F1 iyileşmesi (0.543 vs 0.432) bildiriyor.
3. EvolveMem, LoCoMo'da GPT-5.1 backbone ile SimpleMem'e göre %36.8 genel rölatif kazanç, temporal kategoride %98.9 bildiriyor.
4. EvolveMem, MemBench'te GPT-4o'da %67.9, GPT-5.1'de %71.4 genel doğruluk bildiriyor, en güçlü baseline'ı %18.9 rölatif geçiyor.
5. Anatomy of Agentic Memory (K3, arXiv:2602.19320, 2026-02-22), Nemori sisteminde küçük modelde (Qwen-2.5-3B) %30.38, güçlü modelde (gpt-4o-mini) %17.91 format hatası ölçtü.
6. K3, F1 gibi sözcüksel metriklerin semantik kaliteyle uyuşmadığını gösterdi: AMem semantik sıralamada 4. olmasına rağmen F1 skoru 0.116.
7. K3, hafıza inşa maliyetinin sistemler arası 1.3M–7.04M token aralığında değiştiğini ve MemoryOS'un tur başına 32+ saniye gecikme gösterdiğini ölçtü.
8. Governed Shared Memory (K4, arXiv:2606.24535, 2026-06-23), yetki-denetimi arızasıyla trust-level-1 bir ajanın fleet-dışı satırlara erişebildiğini, çalışırken keşfedilip düzeltildiğini raporladı.
9. K4, eşzamanlı-kopya-tespiti asenkron çelişki-dedektöründen önce çalıştığı için genel çelişki tespit oranının %49'a düştüğünü, admission'a giren çelişkilerin ise 90/90 doğru çözüldüğünü buldu.
10. K4, semantik aramada fleet-filtresi kısmen uygulandığında kesişim-dışı probların %43.9'unun yine de kısıtlı satırları gösterdiğini buldu.
11. K4, doğru uygulanan yönetişimde (kapsam+köken+eşzamanlama) fleet-dışı sızıntının 0/80 prob'da sıfır, fleet-içi görünürlük yayılımının 117/120 (%97.5) olduğunu buldu.
12. "Kendini geliştiren hafızada insan-onayı/fren etkisi" sorusuna dair bu taramada bulunan TEK somut ampirik kanıt K4'ün negatif bulgularıdır (frensiz şema evrimi → güvenlik ve çelişki-çözme arızası); K2 ve K5 kaynaklarında insan-onay mekanizmasının varlığı/etkisi bu taramada DOĞRULANAMADI (PDF sıkıştırma sorunu).

---

**Epistemolojik not:** İlk WebFetch denemesinde (K1 ve K5 PDF'leri) araç, doğrulanamayan popüler isimler (MemGPT, Voyager, RETRO, Self-RAG, ChatDev, MetaGPT) "referans" diye üretti; bu çıktı olası halüsinasyon olarak İŞARETLENDİ ve rapora dahil EDİLMEDİ — yalnız gerçekten doğrulanabilir HTML gövdesinden alıntı alınan K2, K3, K4 sayısal kanıt olarak kullanıldı.
