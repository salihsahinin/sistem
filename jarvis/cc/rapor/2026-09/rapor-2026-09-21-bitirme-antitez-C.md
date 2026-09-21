# Antitez Raporu (¬C) — AI × Matematik Güncel Durum

**Ajan:** Atlas (Antitez rolü, ¬C) · **Çekim tarihi (sistem):** 2026-09-21 · **Yöntem:** CoVe-Factored, bağımsız (tez raporu görülmedi) · **Disiplin:** URL zorunlu, AS-OF, rakam kaynaklı, kestirim `[?]`

**Not (model-hafızası ayrımı):** Bu rapordaki iddialar 2025-07 ile 2026-09 arası tarihli; asistanın eğitim kesim tarihi (2026-01) sonrasını kapsıyor. Aşağıdaki tüm veriler canlı WebSearch/WebFetch ile doğrulandı, model-hafızasından **değil**.

---

## İddia Değerlendirmeleri

### C1 — "Google DeepMind ve OpenAI, 2025-07-21'de IMO 2025'te 35/42 ile altın madalya eşiğine ulaştı"

**Sonuç: DARALDI: koşul**

- Google DeepMind: Gemini Deep Think 35/42, 6 problemden 5'ini tam çözdü, **2025-07-21**'de duyuruldu, IMO Başkanı Prof. Gregor Dolinar tarafından resmî sertifikalandı ("We can confirm that Google DeepMind has reached... gold medal"). Kaynak: [DeepMind blog](https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/) (WebFetch, AS-OF 2026-09-21).
- OpenAI: 35/42 iddiası **2025-07-19**'da Alexander Wei tarafından X'te duyuruldu — DeepMind'den 2 gün önce, iddia listesindeki "2025-07-21" tarihi yalnız DeepMind için doğru. Kaynak: [Simon Willison](https://simonwillison.net/2025/Jul/19/openai-gold-medal-math-olympiad/), [Alexander Wei'nin X gönderisi](https://x.com/alexwei_/status/1946477742855532918).
- Daha önemlisi: OpenAI'nin puanı IMO koordinatörlerinin resmî (gizli) rubriğiyle değil, şirketin kendi tuttuğu **3 eski IMO madalyalısı** tarafından değerlendirildi; IMO'nun resmî skor rehberine dışarıdan erişim yok, dolayısıyla DeepMind'in Başkan onaylı sertifikasyonuyla aynı statüde değil. IMO organizasyonu, kapanış töreninden önce sonuç duyurulmasını eleştirdi. Kaynak: [36kr — "IMO Rebukes OpenAI for Self-Claimed Victory"](https://eu.36kr.com/en/p/3388372845035907), [LessWrong](https://www.lesswrong.com/posts/ZkgaPopsBkQgeA2k8/google-and-openai-get-2025-imo-gold).
- **Daralma koşulu:** "35/42 ile altın eşiği" iki taraf için de sayısal olarak doğru, ancak (a) tarih yalnız DeepMind için 07-21 doğru (OpenAI 07-19), (b) yalnız DeepMind'in sonucu IMO-koordinatör-sertifikalı; OpenAI'ninki şirket-içi değerlendirme.

### C2 — "RedNote'un dots-note-3.0 modeli 2026 IMO'da (Şangay) 6 sorunun tümünü çözerek 42/42 puan aldığını iddia etti"

**Sonuç: ÇÜRÜTÜLEMEDİ**

- SCMP (birincil teknoloji basını): "dots-note-3.0... solved all six puzzles and secured a perfect score of 42... For the first time in the competition's history." Ancak bu bilginin kaynağı "a post on the model's website" — SCMP makalesi bağımsız IMO onayı sunmuyor. Kaynak: [SCMP](https://www.scmp.com/tech/article/3361482/worlds-first-ai-model-earn-perfect-score-maths-olympiad-comes-chinas-rednote) (WebFetch, AS-OF 2026-09-21).
- Diğer kaynaklar (digitalapplied.com, tech-insider.org, France24, techxplore) 2026 IMO'da hem Huawei Celia hem RedNote dots-note-3.0'ın "officially graded" 42/42 aldığını, insan müdahalesi olmadan resmî IMO süreciyle değerlendirildiğini raporluyor.
- İddia zaten "iddia etti" diyerek hedge'lenmiş (kesinlik iddia etmiyor) — bu ifade doğru ve kanıtla uyumlu; çürütme girişimi başarısız oldu.

### C3 — "Erdős problemleri veritabanında 2026-08-03 itibarıyla 565 problem çözülmüş, 652 problem açık"

**Sonuç: ÇÜRÜTÜLEMEDİ**

- Quanta Magazine (2026-08-03 tarihli, doğrudan konuyla ilgili makale), erdosproblems.com'dan **birebir aynı rakamları** veriyor: "565 solved problems and 652 open ones." Kaynak: [Quanta Magazine](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/) (WebFetch, AS-OF 2026-09-21).
- Not: Bir ikincil kaynak "%41 çözülmüş" diyor — 565/(565+652)=%46,4 ile uyuşmuyor, ama bu Quanta'nın kendi rakamı değil, farklı bir ikincil özetleyicinin (muhtemelen erken 2026 anlık görüntüsü) hatası/eskimişliği; C3'ü çürütmüyor.

### C4 — "Epoch AI'nin 2026-09-01 FrontierMath Erdős testinde (68 problem) yalnız GPT-6 Astra 2/68, diğerleri %0"

**Sonuç: DARALDI: koşul**

- Epoch AI'nin resmî duyurusu (WebFetch): 68 çözülmemiş Erdős problemi, Lean'de biçimlendirilmiş, **2026-09-01** duyuruldu. Resmî benchmark sonucu: GPT-6 Astra 2/68 (%3), test edilen diğer dört model (GPT-5.6 Sol, GPT-5.5, Claude Fable 5.1, Claude Fable 5) %0. Kaynak: [Epoch AI](https://epoch.ai/latest/announcing-frontiermath-erdos) (WebFetch, AS-OF 2026-09-21).
- **Daralma koşulu:** GPT-6 Astra, resmî benchmark bütçesi dışında daha büyük hesaplama bütçesiyle yapılan **ek (gayri-resmî) denemelerde 5/68** problem çözdü — bu sayı resmî skor sayılmıyor. İddiadaki "2/68" resmî test için doğru, ama "yalnız GPT-6 Astra" ifadesi teknik olarak doğru (diğerleri gerçekten %0) — daralma yalnız "resmî vs. gayri-resmî 5/68" ayrımından kaynaklanıyor, çürütme değil.
- İki farklı ikincil kaynakta dolar/saat rakamları çelişkili ($218/15sa vs $222/10sa) — bu C4'ün iddiasında yer almıyor, önemsiz.

### C5 — "Mathlib 288.718 teorem ve 136.941 tanım"

**Sonuç: ÇÜRÜTÜLEMEDİ**

- Resmî Mathlib istatistik sayfası birebir aynı rakamları veriyor: Definitions 136,941; Theorems 288,718. Kaynak: [Mathlib stats](https://leanprover-community.github.io/mathlib_stats.html) (WebFetch, AS-OF 2026-09-21).
- Not: arXiv 2604.24797 (Şubat 2026 ağ-yapısı analizi) "308,129 declarations" diyor — farklı metrik (tüm declaration'lar: teorem+tanım+lemma+yapı vb. toplamı), C5'in spesifik "teorem" ve "tanım" sayılarıyla çelişmiyor.

### C6 — "PutnamBench 1.724 el-yapımı biçimlendirme, Lean 4/Isabelle Apache 2.0, Coq MIT"

**Sonuç: ÇÜRÜTÜLEMEDİ**

- GitHub README (WebFetch, birincil kaynak): 1724 formalizasyon (Lean 4: 672, Isabelle: 640, Coq: 412); "permissive licenses (Apache 2.0 for Lean 4 and Isabelle, MIT for Coq)." Kaynak: [PutnamBench README](https://github.com/trishullab/PutnamBench/blob/main/README.md) (AS-OF 2026-09-21). Birebir eşleşiyor.

### C7 — "LeanCopilot MIT lisanslı, GPU isteğe bağlı, CPU'da çalışabiliyor"

**Sonuç: ÇÜRÜTÜLEMEDİ**

- GitHub repo (WebFetch): MIT lisans; "Optional (recommended if you have a CUDA-enabled GPU)"; "run either locally (w/ or w/o GPUs) or on the cloud." Kaynak: [LeanCopilot](https://github.com/lean-dojo/LeanCopilot) (AS-OF 2026-09-21). Birebir eşleşiyor.

### C8 — "DeepSeek-Prover-V2-671B, MiniF2F-test'te %88,9"

**Sonuç: ÇÜRÜTÜLEMEDİ**

- arXiv 2504.21801 ve HuggingFace model kartı: "88.9% pass ratio on the MiniF2F-test"; ayrıca PutnamBench'te 658 problemden 47'sini çözdüğü de raporlanıyor (C8 dışı ek veri). Kaynaklar: [arXiv 2504.21801](https://arxiv.org/abs/2504.21801), [HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-Prover-V2-671B).

### C9 — "Goedel-Prover-V2 32B, MiniF2F pass@32 %88,1, iki-tur hata düzeltmeyle %90,4"

**Sonuç: ÇÜRÜTÜLEMEDİ**

- arXiv 2508.03613 (WebFetch, birincil kaynak): standart modda "88.1% on MiniF2F at pass@32", self-correction modunda "90.4%." Kaynak: [arXiv 2508.03613](https://arxiv.org/abs/2508.03613) (AS-OF 2026-09-21). Birebir eşleşiyor.

### C10 — "arXiv 2607.07779, AI-üretimi biçimsel kanıtları insan-okunur hale getirmeyi açık bir araştırma sorunu olarak tanımlıyor"

**Sonuç: ÇÜRÜDÜ**

- Makale gerçekten var: "From Solvers to Research: Large Language Model-Driven Formal Mathematics at the Research Frontier" (2026-07-08 gönderildi, Terence Tao dahil 19 yazar). Kaynak: [arXiv 2607.07779](https://arxiv.org/abs/2607.07779).
- Ancak makalenin **tam metni** (WebFetch ile doğrudan tarandı) "proof explanation", "interpretability", "human-readable proofs", "natural language translation" konularından **hiç bahsetmiyor**. Makalenin ele aldığı açık sorunlar: veri kıtlığı, spesifikasyon boşluğu (informal→formal anlam kaybı), izole kanıtlardan bilgi-grafiklerine geçiş, otomatik keşif, araç entegrasyonu, insan-AI işbirliği (§5.1-5.5) — hiçbiri kanıt açıklama/okunabilirlik değil. Kaynak: [arXiv 2607.07779 tam metin](https://arxiv.org/html/2607.07779) (WebFetch, AS-OF 2026-09-21).
- **Bu bir yanlış atıf** — belirtilen makale, iddia edilen konuyu ele almıyor. Bitirme tezi için bu atıf **düzeltilmeli**; doğru atıf için bkz. EK-SORU-2 cevabı.

### C11 — "PySR, Julia tabanlı SymbolicRegression.jl motoruyla çalışan açık kaynaklı bir sembolik regresyon kütüphanesi"

**Sonuç: ÇÜRÜTÜLEMEDİ**

- GitHub repo (WebFetch): "PySR is developed alongside the Julia library SymbolicRegression.jl, which forms the powerful search engine of PySR"; lisans **Apache-2.0** (iddia yalnız "açık kaynaklı" diyor, bu daha güçlü/kesin — çelişki değil, teyit). Kaynak: [PySR GitHub](https://github.com/MilesCranmer/PySR) (AS-OF 2026-09-21).

### C12 — "Thomas Bloom, AI-üretimi bazı Erdős çözüm makalelerinin hiçbir insan tarafından okunmadığı konusunda uyardı"

**Sonuç: ÇÜRÜTÜLEMEDİ**

- ScienceNews doğrudan alıntı: "These people have used AI to generate hundreds of pages of math that they can't understand or even read. 'It could be right. It could be nonsense. Who's going to be able to check this?'" Kaynak: [ScienceNews](https://www.sciencenews.org/article/ai-guardrails-erdos-math-problem) (WebFetch, AS-OF 2026-09-21).
- **Karıştırılmaması gereken ayrı olay:** 2025-10'da OpenAI'nin GPT-5'in "10 Erdős problemi çözdüğü" iddiasında Bloom'un asıl eleştirisi farklıydı — model orijinal ispat üretmemiş, eski (insan yazımı, AI'nin ürettiği değil) makalelerde zaten var olan ama Erdős listesine bağlanmamış çözümleri **bulmuştu**. Bu, C12'nin bahsettiği "AI-üretimi makale okunmadı" uyarısından farklı, ayrı bir olay — iki olayı karıştırmamak gerekir, ama C12'nin kendisi doğru olayı (yeni AI-üretimi, doğrulanamayan makaleler) doğru tarif ediyor.

---

## EK-SORU Cevapları

**EK-SORU-1 — IMO 2026'da AI sonuçları gerçekte ne?**
2026 IMO Şangay'da yapıldı; **resmî/bağımsız-doğrulanmış** olarak raporlanan iki sonuç: Huawei'nin Celia'sı ve RedNote'un dots-note-3.0'ı, ikisi de 42/42 ("officially graded", insan müdahalesi olmadan, IMO'nun resmî sürecine benzer koşullarda). Kaynak: [tech-insider.org](https://tech-insider.org/ai-imo-2026-perfect-score-odds-hit-96-percent/), [France24](https://www.france24.com/en/live-news/20260723-ai-catches-up-with-humans-to-score-100-at-top-maths-contest). Ayrıca **gayri-resmî**, bir yatırımcının kendi test koşumunda (IMO'nun resmî sürecinin dışında) OpenAI, Anthropic, Axiom Math ve Moonshot AI'nin "Kimi K3" modellerinin de 42/42 aldığı iddia edildi; bu IMO tarafından sertifikalanmadı. Kaynak: [digitalapplied.com](https://www.digitalapplied.com/blog/imo-2026-perfect-scores-ai-benchmark-saturation), [GitHub deedy/imo-2026](https://github.com/deedy/imo-2026). Google DeepMind'in 2026 IMO'ya resmî katılımına dair kanıt bulunamadı `[?]`.

**EK-SORU-2 — "AI kanıtını insana çevirme" boşluğunu kapatan çalışma var mı?**
Kısmen evet, ama tam kapatılmamış. arXiv 2509.09726, "Natural Language Translation of Formal Proofs through Informalization of Proof Steps and Recursive Summarization along Proof Structure" başlığıyla, tam olarak bu yöne (Lean → doğal dil) çalışıyor ve üniversite-düzeyi ispatların anahtar noktalarının **%86'sını** yakalayan okunabilir çıktı üretiyor — yani bitirme tezinin "açık sorun" iddiası abartılı, kısmen çözülmüş bir alan olarak yeniden çerçevelenmeli. Kaynak: [arXiv 2509.09726](https://arxiv.org/pdf/2509.09726). Buna karşılık, 2026'daki asıl araştırma yoğunluğu **ters yönde**: ProofBridge, LeanMarathon, Lean Atlas, Goedel-Architect gibi araçların hepsi doğal dil → Lean biçimlendirmesine (auto-formalization) odaklanıyor, tersi değil. Kaynak: [ProofBridge (ICLR 2026)](https://mlanthology.org/iclr/2026/jana2026iclr-proofbridge/), [Lean Atlas](https://arxiv.org/pdf/2604.16347). arXiv 2607.07779 (C10'da iddia edilen kaynak) bu konuyu **ele almıyor** — yanlış atıf, tez için düzeltilmeli.

**EK-SORU-3 — Tek laptopla çalışma iddialarına karşı gerçek donanım gereksinimi?**
Araçlar arasında uçurum var: LeanCopilot (MIT, GPU isteğe bağlı, CPU'da çalışır) ve PySR/SymbolicRegression.jl gerçekten laptop-dostu — küçük modeller, yerel çalıştırma tasarlanmış. Kaynak: [LeanCopilot](https://github.com/lean-dojo/LeanCopilot), [PySR](https://github.com/MilesCranmer/PySR). Ama DeepSeek-Prover-V2-**671B** (C8) gibi frontier modeller 671 milyar parametreli — tek tüketici laptopunda (hatta tek yüksek-uç GPU'da) yerel çalıştırma pratik değil `[?]`, gerçekçi kullanım bulut API/çok-GPU sunucu üzerinden; Goedel-Prover-V2 32B (C9) daha küçük ama yine de 24-48GB VRAM sınıfı GPU gerektirir `[?]` (kesin VRAM rakamı birincil kaynaklarda doğrulanmadı, teknik tahmin işaretlendi). Tez, "tek laptopla" iddiasını hangi araç için (LeanCopilot/PySR: evet; 671B modeller: hayır) net ayırmalı.

---

## Kaynak Sayımı

WebFetch ile gerçekten açılan birincil kaynak sayısı: **12** (PutnamBench README, Mathlib stats, Epoch AI duyurusu, Quanta Magazine, LeanCopilot GitHub, arXiv 2607.07779 özet, arXiv 2607.07779 tam metin, PySR GitHub, ScienceNews, DeepMind blog, SCMP, arXiv 2508.03613). Ek olarak çok sayıda WebSearch sorgusu (≈12) çapraz-referans için kullanıldı.

**Genel özet:** 12 iddiadan 8'i **ÇÜRÜTÜLEMEDİ** (C2, C3, C5, C6, C7, C8, C9, C11, C12 — aslında 9), 2'si **DARALDI: koşul** (C1, C4), 1'i **ÇÜRÜDÜ** (C10). Düzeltme: ÇÜRÜTÜLEMEDİ = C2, C3, C5, C6, C7, C8, C9, C11, C12 (9 adet); DARALDI = C1, C4 (2 adet); ÇÜRÜDÜ = C10 (1 adet). Toplam 12.
