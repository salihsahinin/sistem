# A3 Antitez Taraması — İB-51 (A67-7) ve İB-66 (A67-8)

**AS-OF:** 2026-08-31 · **Aile:** A3 (antitez) · **Model:** sonnet · **Yöntem:** adversarial literatür taraması (WebSearch/WebFetch), "BU ZATEN VAR" kanıtı arama

---

## A67-7 (İB-51) — Kural bütçesi ölçümü + IFScale kalibrasyonu

**İddia:** LLM-ajan sisteminde yazılı kural bütçesini deterministik ölçmek (taşıyıcı sınıfı T0-T4 × görev sınıfı çapraz tablo) ve IFScale'e (%68 @ 500 talimat) karşı yerel ≤100-birim eşiği kalibre etmek.

### IFScale doğrulama (ZORUNLU)

**DOĞRULANDI — birincil kaynak açıldı.**
- Başlık: "How Many Instructions Can LLMs Follow at Once?"
- Yazarlar: Daniel Jaroslawicz, Brendan Whiting, Parth Shah, Karime Maamari (Distyl AI)
- arXiv: 2507.11538, 15 Temmuz 2025 — https://arxiv.org/abs/2507.11538
- Doğrulanan rakam: "even the best frontier models only achieve 68% accuracy at the max density of 500 instructions" — İDDİA EDİLEN %68 @ 500 RAKAMI DOĞRU, birincil kaynaktan teyitli.
- Metodoloji: N=10'dan 500'e, 10'ar artan; 500 anahtar-kelime-içerme talimatlı iş raporu yazma görevi; 20 model/7 sağlayıcı; üç degradasyon deseni (eşik/doğrusal/üstel).
- Etiket: **DESTEKLİ** (IFScale gerçek, rakam doğru).

### En-yakın-komşu çalışmalar

| Çalışma | Yıl | Bulgu | İlişki |
|---|---|---|---|
| [IFScale (2507.11538)](https://arxiv.org/abs/2507.11538) | 2025 | Talimat yoğunluğu arttıkça doğruluk düşüşü, N=10-500, tek görev tipi (anahtar-kelime) | Doğrudan referans, doğrulandı |
| [ManyIFEval (arXiv, EMNLP Findings 2025)](https://aclanthology.org/2025.findings-emnlp.896.pdf) | 2025 | IFEval'den türetilmiş, 1-10 talimat aralığında Instruction-level + Prompt-level Accuracy; Prompt-level düşüş eğilimi net | Aynı problem sınıfı (çoklu-talimat uyumu ölçümü), farklı ölçek (1-10 vs 10-500) |
| [AGENTIF (Tsinghua KEG)](https://keg.cs.tsinghua.edu.cn/persons/xubin/papers/AgentIF.pdf) | 2025 | Ajan-bağlamında talimat takibini kıyaslıyor | Ajan-spesifik talimat uyumu ölçütü, T0-T4 taşıyıcı sınıflandırmasına yakın değil ama komşu |
| [Many-Tier Instruction Hierarchy in LLM Agents (2604.09443)](https://arxiv.org/html/2604.09443v3) | 2026 | Çok-katmanlı talimat hiyerarşisi (sistem/geliştirici/kullanıcı gibi) | Katmanlı talimat kaynağı fikri VAR ama "taşıyıcı sınıfı T0-T4 (her-oturum/ritüel/çağrı-skill/kanon/wiki)" tanımına özgü değil |
| Curse of Instructions (OpenReview) | ~2024-25 | Talimat sayısı arttıkça LLM performans düşüşü, farklı çerçeveleme | Genel fenomeni destekliyor |

### Yenilik durumu: **KISMİ**

- **DÜŞEN kısım:** "Çok sayıda talimatla performans düşer" ve "N'e göre eşik kalibre etme" fikri YENİ DEĞİL — IFScale ve ManyIFEval zaten bunu ölçüyor; IFScale'in kendi metodolojisi tam olarak "talimat sayısına karşı doğruluk eğrisi çıkar, eşik/desen sınıflandır" yapıyor.
- **AYAKTA KALAN kısım (bulunamadı → potansiyel gerçek katkı):** Aramalarda, JARVIS'in önerdiği spesifik **taşıyıcı-sınıfı taksonomisi (T0 her-oturum / T1 ritüel / T2 çağrı-skill / T3 kanon / T4 wiki) × görev-sınıfı ÇAPRAZ TABLOSU** ile bağlam-bütçesi ölçümüne rastlanmadı. Bulunan çalışmalar (ManyIFEval, AGENTIF, Many-Tier Hierarchy) talimat kaynağını ya tek boyutlu sayıyor ya da rol-bazlı hiyerarşi (system/user/tool) kullanıyor — JARVIS'in önerdiği "taşıyıcı sınıfı" ekseni (ne zaman bağlama girdiği: her oturum mu, ritüelle mi, çağrıyla mı) farklı bir eksen; literatürde eşleşen bir çalışma bulunamadı `[?]`.
- **"Yerel ≤100-birim eşiği IFScale'e karşı kalibre etmek"** — bu, IFScale'in genel-amaçlı (business-report, keyword-inclusion) sonucunu kendi ajan-sistemine transfer etme fikri; IFScale yazarları bunu kendi sistemlerine özel kalibrasyon olarak sunmuyorlar, genel bir benchmark sunuyorlar. Bu transfer adımı literatürde doğrudan görülmedi.

### Etiket: **KISMİ / DESTEKLİ-temel + DAYANAKSIZ-taksonomi**
- Alt-iddia "çoklu talimatla performans düşer, ölçülebilir" → DESTEKLİ (IFScale/ManyIFEval zaten var).
- Alt-iddia "T0-T4 taşıyıcı-sınıfı × görev-sınıfı çapraz tablo + yerel ≤100-birim eşik kalibrasyonu" → arama sonuçlarında eşleşen çalışma YOK-bulundu; ancak negatif kanıt (bulunamama) mutlak yenilik ispatı DEĞİL, sadece bu taramanın kapsamında rastlanmadığı anlamına gelir `[?]`.

---

## A67-8 (İB-66) — Nested multi-agent gözlem yüzeyi birleşme eksikliği tespiti

**İddia:** Çok-ajanlı LLM sistemlerinde iç-içe döngü yürütmesinin CANLI + konuşma-granülü + seviye-ayrımlı + müdahale-edilebilir TEK gözlem yüzeyinde birleşmediğinin, 5-kriterli 12-araç matrisiyle sistematik tespiti (0/12).

### En-yakın-komşu çalışmalar

| Çalışma | Yıl | Bulgu | İlişki |
|---|---|---|---|
| [MAST — Multi-Agent System failure taxonomy](https://arxiv.org/pdf/2606.04990) (referans zinciri üzerinden) | 2025 | 14 hata modu, 3 kategori (spesifikasyon/uyumsuzluk/doğrulama) | Hata taksonomisi VAR ama araç-matrisi/gözlem-yüzeyi kıyası DEĞİL |
| [From Agent Traces to Trust (2606.04990)](https://arxiv.org/html/2606.04990) | 2026 | 6 boyutlu (kaynak, kanıt/yürütme birimi, provenance ilişkisi, granülerlik/zamanlama, temsil biçimi, güven işlevi) taksonomi | En yakın kavramsal komşu — "trace kaynağı/granülerlik/temsil" boyutları JARVIS'in "canlı/konuşma-granülü/seviye-ayrımlı/müdahale-edilebilir" kriterlerine kısmen örtüşüyor, ama bu bir ARAÇ-MATRİSİ karşılaştırması değil, bir taksonomi/survey |
| [LumiMAS (2508.12412)](https://arxiv.org/pdf/2508.12412) | 2025 | Gerçek-zamanlı izleme + gelişmiş gözlemlenebilirlik çerçevesi, çok-ajan sistemler için | Canlı + çok-ajan gözlem iddiasına en yakın somut sistem; JARVIS'in "birleşmediği" iddiasına karşı POTANSİYEL ÇELİŞKİ adayı — LumiMAS'ın gerçekte kaç kriteri karşıladığı doğrulanmadı `[?]` |
| Ticari araç karşılaştırmaları (Latitude, Galileo, Confident AI, Arize, LangChain "2026 comparison" blog yazıları) | 2026 | AgentOps, Langfuse, LangSmith, Arize Phoenix, Braintrust, Helicone vb. — tracing, replay, thread-level/multi-turn izleme, hiyerarşik orkestratör→worker görselleştirme sunuyorlar | Bu araçların bir kısmı ("thread-level observability", "hierarchical trace visualization mapping orchestrator to worker") JARVIS'in kriterlerinin bazılarını (canlı, seviye-ayrımlı) ayrı ayrı karşılıyor gibi görünüyor; TÜMÜNÜN AYNI ANDA hiçbirini karşılamadığı iddiası (0/12) bu blog-kaynaklı karşılaştırmalarla ne doğrulanabildi ne çürütülebildi |
| Confident AI "thread-level observability" | 2026 | Çok-turlu konuşmaları thread olarak bağlıyor, konuşma-düzeyi desen analizi sunuyor | "Konuşma-granülü" kriterine kısmen aday çelişki — ama "nested/iç-içe ajan" + "müdahale-edilebilir" kriterleriyle BİRLİKTE karşıladığı doğrulanmadı |

### Yenilik durumu: **KISMİ**

- Sorunun VAR OLDUĞU (gözlemlenebilirlik parçalı, araçlar farklı boyutları kapsıyor, birleşik yüzey eksik) literatürde dolaylı olarak destekleniyor — survey'ler (Evidence Tracing/Provenance, 5-katmanlı AI Observability analizi) zaten "farklı araçlar farklı katmanları kapsıyor, tekilleşmiş yüzey yok" temasını işliyor; yani ÜST-SEVİYE SORUN TESPİTİ yeni değil.
- **JARVIS'e özgü kısım** (taramadan-önce-sabitlenmiş 5 kriterli 12-araç matrisi, 0/12 sonucu, sistematik/tekrarlanabilir metodoloji) için literatürde eşleşen bir ÇALIŞMA bulunamadı — ama bu, mevcut ticari araçların (LumiMAS, Confident AI thread-level, AgentOps) bazılarının iddia edilen kriterlerin bir kısmını gerçekten karşılayıp karşılamadığını ÇÜRÜTMEDİ de. LumiMAS özellikle "gerçek-zamanlı izleme + çok-ajan" iddiasıyla doğrudan test edilmeli; bu turda birincil kaynağı açılıp doğrulanmadı `[?]`.

### Etiket: **KISMİ / DAYANAKSIZ→[?]**
- "Sorun var, parçalı gözlemlenebilirlik" üst-tezi → survey'lerle DESTEKLİ (yeni değil, JARVIS'in gerekçe katmanı).
- "12-araç matrisi ile 0/12 sistematik tespiti" spesifik metodoloji ve sonucu → literatürde eşleşen çalışma YOK-bulundu, ancak LumiMAS gibi adaylar TEK TEK doğrulanmadığı için **ÇELİŞEBİLİR** riski `[?]` olarak işaretleniyor — bu turda kapatılamadı (bütçe sınırı).

---

## Özet tablo

| Aday | Yenilik durumu | Etiket | Kritik risk |
|---|---|---|---|
| A67-7 (İB-51) | KISMİ | temel-DESTEKLİ / taksonomi-`[?]` | Kural-bütçesi ölçüm fikri IFScale/ManyIFEval'de zaten var; JARVIS'in eklediği T0-T4×görev-sınıfı çapraz tablo ve yerel kalibrasyon adımı literatürde bulunamadı ama bu negatif kanıt kesin değil |
| A67-8 (İB-66) | KISMİ | üst-tez-DESTEKLİ / matris-metodolojisi-`[?]` | Parçalı gözlemlenebilirlik sorunu bilinen bir tema; 12-araç/5-kriter/0-12 spesifik sonucu doğrulanamadı, LumiMAS gibi adaylar açılıp test edilmedi (bütçe) |

**Not (H-derecesi):** Bu rapor atıf-yoğun; IFScale rakamı birincil kaynaktan doğrulandı, geri kalan çalışmalar arama-özeti üzerinden değerlendirildi (birincil kaynak açılmadı) — bu URL'ler "birincil kaynak doğrulandı" değil, "arama sonucunda görüldü" statüsündedir.
