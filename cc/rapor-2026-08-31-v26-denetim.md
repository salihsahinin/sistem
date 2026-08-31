# V26 Denetim Raporu — 6 İşçi Raporu Birincil-Kaynak Sondajı

Künye: AS-OF 2026-08-31 · rejim maliyet-öncelikli · yöntem: örneklem (son-üçlük 1/3) + WebFetch birincil-kaynak açma + 3 özel zorunlu denetim (a/b/c).
Denetlenen dosyalar: `cc/rapor-2026-08-31-ib67-a1-literatur.md`, `-a2-`, `-a3-`, `cc/rapor-2026-08-31-ib68-b1-pazar.md`, `-b2-`, `-b3-pazar-dagitim.md`.

## Örneklem tablosu

| # | İddia (kısa) | Kaynak dosya | URL | AÇILDI mı | Destekliyor mu |
|---|---|---|---|---|---|
| 1 | CoAgent = Bernstein-türü eşzamanlılık kontrolünü LLM-ajanlara uyarlıyor, MTPO protokolü, LLM conflict-yargısına dahil | a1 (A67-3, son bölüm) | arxiv.org/abs/2606.15376 | EVET | TAM — başlık/yazar/özet eşleşti; MTPO gerçek, "LLM planı onarır" karakterizasyonu doğrulandı |
| 2 | ATM = "CID-Brokered Pre-Write Admission for Multi-Agent Code Co-Synthesis", pre-write admission kavramı | a1 (A67-3, son bölüm) | arxiv.org/abs/2607.00041 | EVET | TAM — başlık ve konu birebir eşleşti |
| 3 | "Don't Break the Cache" = long-horizon agentic tasks için prompt-caching değerlendirmesi | a2 (A67-4) | arxiv.org/abs/2601.06007 | EVET | TAM |
| 4 | BAGEN = "Are LLM Agents Budget-Aware?" | a2 (A67-4) | arxiv.org/abs/2606.00198 | EVET | TAM |
| 5 | HiL-Bench = ajanların ne zaman yardım isteyeceğini bilip bilmediği | a2 (A67-5) | arxiv.org/abs/2604.09408 | EVET | TAM |
| 6 | Falsifiable Release Gates = kendini-geliştiren sistemler, capability-token, kontrol halkası | a2 (A67-6) | arxiv.org/abs/2607.13070 | EVET | TAM |
| 7 | Langfuse self-host: Hobby ücretsiz / Core $29 / Pro $199 / Enterprise $2.499 | b3-dagitim (dağıtım emsalleri tablosu) | langfuse.com/pricing-self-host | EVET | KISMİ — ücretli plan VAR doğrulandı ama sayfada yalnız "Self-Hosted Enterprise (Custom Pricing)" katmanı görüldü; $29/$199/$2.499 rakamları bu sayfada teyit EDİLEMEDİ (muhtemelen farklı bir sayfadan/cloud-pricing'den alınmış) |
| 8 | HumanLayer: ajan hassas araç çağrısı öncesi insana onay sorar, ücretli plan var, rakam yazılmadı | b2 (B68-3) | humanlayer.systems/index-en.html | EVET | KISMİ — ürün+ücretli-plan doğrulandı; Slack/Email/Discord bildirim detayı sayfada bulunamadı; rapor rakam yazmadığı için (gerçek rakamlar $15/$80/$200-karar) bu disiplin doğru |
| 9 | Invariant Labs, Snyk tarafından satın alındı (M&A çıkışı) | b2 (B68-6) | invariantlabs.ai/guardrails | EVET | TAM — sayfa başlığında "Snyk Acquires Invariant Labs..." doğrudan doğrulandı |

**Zorunlu (a) sonucu:** CoAgent (2606.15376) ve ATM (2607.00041) — İKİSİ DE GERÇEK, iddia edilen konuyu işliyor. **UYDURMA-ID YOK.**
**Zorunlu (b) sonucu:** Don't Break the Cache (2601.06007), BAGEN (2606.00198), HiL-Bench (2604.09408), Falsifiable Release Gates (2607.13070) — DÖRDÜ DE GERÇEK ve konu eşleşiyor. **UYDURMA-ID YOK.**
**Zorunlu (c) sonucu:** aşağıda İHLAL LİSTESİ #1.

## İHLAL LİSTESİ

1. **[sayısal-iddia-kaynaksız]** — `cc/rapor-2026-08-31-ib68-b3-pazar-dagitim.md`, satır ~32-35 (emsal tablosu) ve satır ~64-66 ("Emsal tablosu" B68-4/dağıtım bölümü): Langfuse ($29/$199/$2.499/ay), LangSmith ($39/koltuk), Braintrust ($249/ay), Galileo ($100/ay), Continue.dev ($3/milyon token, $20/koltuk) dolar tutarları GÖVDE METNİNDE yazılmış. Dosyanın kendi üst-künyesi ("Aşağıdaki hiçbir satırda tahmini fiyat/gelir rakamı YOK. Ücretli plan yalnız VAR/YOK olarak işaretli") ve alt-notu ("Tüm rakamlar arama-sonucu özetinden alınmıştır, birincil kaynak sayfası açılıp doğrulanmamıştır") bu tutarlarla DOĞRUDAN ÇELİŞİYOR — açılmamış kaynaktan sayısal iddia yazılmış, kendi disiplin beyanını ihlal ediyor. WebFetch sondajı (örneklem #7) Langfuse'un kendi sayfasında bu üç rakamı DOĞRULAYAMADI.
2. **[açılmamış-kaynağa-birincil-damgası]** — `cc/rapor-2026-08-31-ib68-b1-pazar.md`, satır 31-32: "AgentOps ~5.6k yıldız ... **DESTEKLİ** (tek arama-sonucu kaynağı)" ve "Langfuse'un Clickhouse tarafından satın alınması ... **DESTEKLİ** (arama-sonucu, birincil kaynak açılmadı)" — kaynak URL açılmadığı halde etiket "DESTEKLİ"; bu, "birincil kaynaktan doğrulandı" izlenimi verir, oysa yalnız arama-özeti var.
3. **[açılmamış-kaynağa-birincil-damgası]** — `cc/rapor-2026-08-31-ib68-b2-pazar.md`, satır 83: "'HumanLayer doğrudan rakip' **DESTEKLİ** (isim+ürün+fiyat üçlü eşleşme, ikinci-el kaynaklardan)" — kendi metni "ikinci-el kaynak" dediği halde etiket DESTEKLİ; WebFetch sondajı (örneklem #8) ürün+ücretli-plan varlığını doğruladı ama raporun "fiyat üçlü eşleşme" iddiasındaki spesifik rakamlar ($15/$80/$200-karar) rapor gövdesinde hiç geçmiyor — yani "fiyat eşleşti" ibaresi de teyitsiz.
4. **[SEO-gürültü]** — `cc/rapor-2026-08-31-ib68-b3-pazar-dagitim.md` ve `-b1-pazar.md`: agentmodeai.com (2 kez, B68-4 rakip listesi), futureagi.com/blog (rollout-strategies-2026), feeds.trussed.ai (2 kez, AI-TRiSM listesi) — hiçbiri birincil ürün/akademik kaynak değil, karşılaştırma-blog/içerik-agregasyon sitesi; b2 dosyası kendi içinde benzer bir riski bir kez işaretlemiş ("blog-SEO şişkinliği olabilir [?]", satır 54) ama bu dört kaynak işaretlenmemiş.

## Toplam

- **Toplam ihlal sayısı: 4** (1× sayısal-iddia-kaynaksız, 2× açılmamış-kaynağa-birincil-damgası, 1× SEO-gürültü grubu)
- **Uydurma-ID: 0/6 zorunlu kimlik** — hepsi gerçek ve konu-uyumlu.
- **Doğrulama oranı (örneklem):** 7/9 TAM, 2/9 KISMİ, 0/9 DESTEKLEMİYOR → tam-doğrulama oranı **%78** (7/9), kısmi dahil **%100** (9/9) hiçbiri çürütülmedi.
