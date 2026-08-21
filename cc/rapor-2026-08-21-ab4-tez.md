# Rapor — AB-4 TEZ: V59 Token-Verim Okuyucu Ön-Katmanı (S-4a)

**Rol:** S-4a (v59-okuyucu-onkatman-tez) · **Tarih:** 2026-08-21 · **Model:** sonnet · **Rejim:** maliyet-öncelikli
**Görev emri:** cc/gorev-2026-08-21-arastirma-borclari.md (S-4a bloğu) · **Devraldığı:** cc/gorev-2026-07-22-1.md §3 (ATLAS-V59)

## Pointer notu (m.20, kendi üstüne uygulanmış)
Bu koşum **cc/rapor-2026-07-22-1.md**'deki V59 bölümünün (satır 111-146) ÜSTÜNE kurulur. O rapor zaten D-doğrulanmış şu bulguları içeriyor: FrugalGPT (%98'e kadar), LLMLingua (20×/~1.5pt), LLMLingua-2 (2-5×), RouteLLM (85%→45%→35% MT Bench→MMLU→GSM8K altında daralma), RAGAS/SummHay/NIAH, RAPTOR (+20% QuALITY), DocumentSummaryIndex, "Verbatim Chunks Beat Extracted Artifacts" (2601.00821). **Burada TEKRARLANMADI** — yalnız referans verildi (KANONDA-BİLİNENLER kuralı + hazırı-temel-al). Bu raporun katkısı: (a) 4 desen ailesine YENİ/ek D-bulgu, (b) her desene **bileşme satırı** (istenen ama July raporunda gevşek dağılmış format), (c) ayrı kalite-kaybı-ölçüm bölümü.

---

## 1. Ucuz-model ön-özetleyici / cascade

**[D] Jina ReaderLM-v2** — 1.5B parametre, 512K bağlam (girdi+çıktı), HTML→Markdown/JSON dönüşümü; format-dönüşümü, ÖZETLEME DEĞİL (bilgi kaybı amaçlanmıyor, yalnız yeniden-yapılanma). Benchmark'ta Qwen2.5-32B, Gemini 2.0 Flash, GPT-4o'yu HTML-temizleme görevinde geçiyor (32B→1.5B, ~20× küçük). Yayın: 2025-01-15.
https://jina.ai/news/readerlm-v2-frontier-small-language-model-for-html-to-markdown-and-json/

**Bileşme noktası:** ReaderLM-v2, "script toplar/temizler, LLM akıl yürütür" (heartbeat dersi) ilkesinin cisimleşmiş hâli — ama DİKKAT: bu bir **özetleyici değil temizleyici**; bilgi kaybı riski taşımadığı için bizim m.20 pointer sistemine tehdit oluşturmaz (AUGMENT/REPLACE ayrımı burada geçersiz, çünkü kayıp yok). Jarvis'te `core/ingest-semasi.md` HTML/PDF ingest ön-adımı için doğrudan aday: pahalı modele ham HTML değil, temiz markdown vermek — token tasarrufu kalite riski OLMADAN.

**[K, pointer]** FrugalGPT / DistilBERT-cascade / matrix-factorization %14 çağrı — cc/rapor-2026-07-22-1.md:115,119-121.

---

## 2. Prompt/bağlam sıkıştırma (LLMLingua sınıfı)

**[D] arXiv 2604.02985 — "Prompt Compression in the Wild"** (Kummer, Jurkschat, Färber, Vahdati; ECIR 2026, kabul edildi). 30.000 sorgu, birden çok açık-kaynak LLM, 3 GPU sınıfı üzerinde LLMLingua ölçümü: **uçtan-uca hızlanma yalnız ~%18** (manşet 20× sıkıştırma-oranından ÇOK küçük), kalite "istatistiksel olarak değişmeden" kalıyor SADECE uzunluk/oran/donanım "iyi eşleştiğinde"; eşleşmezse ön-işleme adımı kazancı YER. Yazarlar "gecikme baş-a-baş noktası" tahmin eden açık-kaynak profil aracı sunuyor.
https://arxiv.org/abs/2604.02985

**[D] arXiv 2503.19114 — "Understanding and Improving Information Preservation in Prompt Compression for LLMs"** (Łajewska ve ark., EMNLP 2025 Findings). Bulgu: soft/hard sıkıştırma yöntemleri "orijinal prompttaki kilit ayrıntıları" tutarlı biçimde KORUYAMIYOR, bu karmaşık görevlerde performans düşüşüne yol açıyor. Önerilen düzeltme (granülarite-kontrollü soft-prompting + sequence-level training): downstream performansta %23'e kadar iyileşme, BERTScore grounding'de +8 puan, korunan varlıkta 2.7×.
https://arxiv.org/abs/2503.19114

**Bileşme noktası:** İki bulgu birlikte July'nin "ön-katmanın kendi compute'u hesaba katılmamış" antitez-çekirdeğini GÜÇLENDİRİYOR ve somutluyor: manşet-oran (20×) ile gerçek uçtan-uca kazanç (%18) arasındaki fark büyük. Bizim mimarimizde m.20 pointer ilkesi zaten **yapısal** sıkıştırma yapıyor (özet+adres, gerekmeyen detayı hiç taşımıyor); LLMLingua sınıfı **token-seviyesi** sıkıştırma farklı bir katman. Pointer zaten "ne taşınacağını" seçtiği için, üstüne token-seviyesi sıkıştırma eklemek çoğu Jarvis kullanım-durumunda (küçük-orta bağlam) **gereksiz karmaşıklık + break-even riski**; yalnız pencereyi gerçekten aşan tek-seferlik dev-doküman ingest'inde (m.21 ölçek üstü) değerlendirilmeli, ve o zaman da break-even-hesaplayıcı profil aracı (2604.02985) örnek alınabilir.

---

## 3. Retrieval-damıtma boru hatları

**[D] Anthropic — "Contextual Retrieval"** (2024-09-19, doğrudan anthropic.com'dan doğrulandı). Yöntem: her chunk'a gömme öncesi 50-100 token'lık LLM-üretilmiş bağlam-özeti prepend edilir ("bu bölüm X dokümanının Y bağlamında Z'yi anlatıyor"). Sonuç: yalnız-contextual-embedding %35 retrieval-hata azalması (5.7%→3.7%), +BM25 %49 (→2.9%), +reranking %67 (→1.9%). **Maliyet modeli: prompt caching ile $1.02/milyon doküman-token'ı** (tek-seferlik bağlamlama maliyeti) — büyük bilgi tabanlarında (200K+ token) pratik.
https://www.anthropic.com/news/contextual-retrieval

**Bileşme noktası:** Bu, m.21 "bağlam-detay ölçekleme" ilkesinin RAG-tarafındaki isim-akrabası — "chunk'a bağlam-özeti ekle, aramayı iyileştir" ile bizim "özet+pointer, detayı karar-anında yükle" ilkesi AYNI aileden ama TERS yönde çalışıyor (biri arama-öncesi zenginleştirme, diğeri yükleme-öncesi seyreltme). Doğrudan uygulanabilir parça: **maliyet-tahmin şablonu** ($/milyon token, prompt-caching'e bağlı) — kendi damıtma/ingest maliyetimizi tahmin ederken (m.39 rakam damgası için) referans-noktası olarak kullanılabilir. RAPTOR/DocumentSummaryIndex zaten July'de D-doğrulandı (pointer, tekrar açılmadı).

---

## 4. Model-yönlendirme (RouteLLM sınıfı)

**[D] arXiv 2603.04445 — "Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey"** (Moslem & Kelleher; gönderim 2026-02-23, son revizyon 2026-04-21 — July koşumundan SONRAKİ/bağımsız yeni kaynak). Taksonomi 3 eksende: **ne zaman** karar verilir (istek-öncesi/inference-sırası/ilk-yanıt-sonrası) · **hangi bilgiyle** (sorgu-özellikleri/model-metadata/geçmiş-performans) · **nasıl hesaplanır** (kurallar/sınıflandırıcılar/RL/cascade). Bulgu: iyi tasarlanmış routing en güçlü tekil modeli bile GEÇEBİLİR (uzmanlaşmış yeteneklerin stratejik kullanımıyla), ama "en uygun strateji deployment/hesaplama kısıtına bağlı" — ve açık sorun: **mimari/modalite/uygulama arası genelleme** hâlâ çözülmemiş.
https://arxiv.org/abs/2603.04445

**Bileşme noktası:** Bizim mevcut "modele-göre-görev-atama" (kosum_profili alanında elle: sonnet/haiku/opus, rejim-etiketi m.46c) survey'in taksonomisinde **istek-öncesi + kural-tabanlı** (en basit, en öngörülebilir) uca denk düşüyor — deterministik-tasarım ilkemizle (Salih 08-17) doğrudan uyumlu. Öğrenilmiş/otomatik router'a (RouteLLM sınıfı) geçişin survey'in kendi itirafıyla "genelleme sorunu" var; Jarvis ölçeğinde (görev-emri başına birkaç-onlarca ajan) elle-atama muhtemelen yeterli — otomatik routing yatırımı ancak ajan-sayısı/çeşitliliği büyük ölçüde artarsa gerekçelenir.

---

## 5. Kalite-kaybı ölçüm yöntemleri (ayrı bölüm)

Yukarıdaki 2503.19114 ve 2604.02985 zaten bu başlığa birincil kaynak; ek olarak:

**[K] "Displacement Is Not Direction: Evaluating Fidelity Metrics for Quantized LLM Deployment"** (arXiv 2606.19558) ve **"Beyond Perplexity: Multi-dimensional Safety Evaluation of LLM Compression"** (arXiv 2407.04965) — WebSearch snippet'inden görüldü, URL açılmadı (F3/F5 gereği künye YAZILMADI, yalnız işaret ediliyor — kendi başına doğrulanmamış [X]/aday olarak not düşülüyor, gerekirse ayrı koşumda açılabilir).

**Sentez (July + bugünün bulgusu birlikte):** İki katman kayıp var — (a) **sadakat** (faithfulness: üretilen özet kaynağa sadık mı — RAGAS/SummHay, July'de D) ve (b) **bilgi-koruma/downstream-yeterlilik** (özet kaynağa sadık OLSA bile downstream görevin ihtiyaç duyduğu ayrıntıyı taşıyor mu — 2503.19114'ün ana noktası: "faithfulness metrikleri downstream-görev ihtiyacını GARANTİ ETMEZ"). Bu ikinci katman July raporunda zayıf işlenmişti (RAGAS/NIAH ağırlıklı); bugünün katkısı bu ayrımı netleştirmek. **Ölçüm reçetesi (güncellenmiş):** yalnız faithfulness/RAGAS değil, ablation-tabanlı downstream-doğruluk (with/without ön-katman) + bilgi-koruma oranı (2503.19114'ün "korunan varlık" metriği tarzı) birlikte bakılmalı.

---

## Jarvis'e uygulanabilirlik (özet)
1. **Format-temizleme ≠ özetleme** ayrımı netleşti: ReaderLM-v2 tarzı "temizleyici" ön-katman kayıpsız, m.20 riskine girmez — ingest-şeması için düşük-riskli aday.
2. **Token-seviyesi sıkıştırma (LLMLingua sınıfı) bizim yapısal-pointer sıkıştırmamızın ÜSTÜNE gereksiz katman** çoğu ölçekte; break-even ancak gerçek pencere-aşımı dev-doküman işinde.
3. **Contextual Retrieval'ın maliyet-modeli ($/M token, prompt-caching) doğrudan ödünç alınabilir** — kendi damıtma maliyet-tahminlerimizde şablon.
4. **Model-atama zaten doğru uçta (kural-tabanlı, elle)** — otomatik-router yatırımı şu ölçekte gerekçesiz; survey bunu destekliyor (genelleme sorunu itirafı).
5. **Kalite-ölçüm reçetesi genişledi:** faithfulness YETMEZ, downstream-ablation + bilgi-koruma-oranı birlikte gerekli.

## Cevaplanamayanlar
- Jarvis'in KENDİ ingest/damıtma hatlarında gerçek bilgi-koruma oranı ÖLÇÜLMEDİ (bu araştırma dış-literatür taraması; içeride ablation testi ayrı bir icra işi — kapsam dışı).
- 2606.19558 ve 2407.04965 açılmadı (zaman/bütçe); istenirse ayrı tekil-doğrulama koşumu (S-5 deseni) gerekir.

## F2 destek-kontrolü tablosu
| İddia | Kaynak | Etiket |
|---|---|---|
| ReaderLM-v2 1.5B, format-dönüşümü (özetleme değil), 32B modelleri geçiyor | jina.ai duyuru sayfası (doğrudan WebFetch) | D |
| LLMLingua uçtan-uca hızlanma yalnız ~%18, break-even donanım/orana bağlı | arXiv 2604.02985 (doğrudan WebFetch) | D |
| Sıkıştırma yöntemleri kilit-ayrıntı korumada başarısız; düzeltmeyle %23 downstream iyileşme | arXiv 2503.19114 (doğrudan WebFetch) | D |
| Contextual Retrieval: %35/%49/%67 hata-azalması, $1.02/M token maliyet | anthropic.com/news/contextual-retrieval (doğrudan WebFetch) | D |
| Routing taksonomisi (ne zaman/hangi bilgi/nasıl), genelleme açık-sorun | arXiv 2603.04445 (doğrudan WebFetch) | D |
| FrugalGPT/LLMLingua-2/RouteLLM temel rakamları, RAGAS/SummHay/NIAH, RAPTOR | cc/rapor-2026-07-22-1.md (iç pointer, orada D) | K (pointer) |
| Displacement/Beyond-Perplexity fidelity çalışmaları | WebSearch snippet, URL açılmadı | X (aday, doğrulanmadı) |

---
**Koşum notu:** ~10 dış tool-çağrısı (6 WebFetch + 3 WebSearch) + 4 iç Read/Bash (görev dosyası + pointer-kaynak okuma), sonnet/medium, tahmini profil (15-30 araç) içinde alt-sınırda kaldı — cost-priority rejimine ve "hazırı temel al" pointer-disiplinine uygun.
