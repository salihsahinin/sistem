# 02 — Yerel Bilgi Index'i: Araştırma Sentezi + Karar + Rollout

**Statü:** öneri dosyası (imzasız). **Ham kanıt:** `raporlar/2026-07-10-arastirma-1-index-mimarisi.md` (3 mimari + stat kartları) ve `raporlar/2026-07-10-arastirma-2-ingest-pipeline.md` (fabrika hattı + eşik tablosu + literatür). Bu dosya karar katmanıdır; detaya inen oraya gider.

## 1. Karar özeti (Katman-2 varsayılanları; veto = revert)

1. **Kişisel erişim ihtiyacı BUGÜN Mimari 1 ile karşılanır** — konvansiyon + ripgrep/FTS5: frontmatter `aliases:` (TR/EN eşanlam katmanı, ~50 önemli entity), klasör başına `_INDEX.md`, kökte `KNOWLEDGE-MAP.md`, erişim tarifi (TR+EN+İ/ı-varyant sorgular → rg → `[[link]]` yürü). Sıfır yeni altyapı; her saat curation'a gider ve gelecek her mimaride bileşik değer taşır. Gerekçe: sorgu karışımı entity-ağır; orkestratör zaten semantik katman; hata profili gürültülü=teşhis edilebilir (rapor 1, tavsiye bölümü).
2. **Saf RAG (Mimari 2) HEDEF DEĞİL — asla.** Domine edilmiş tasarım; sessiz bayatlama = "kendinden emin yanlış bağlam" (ilke #5'in kabusu). Embedding ekleyen BM25'i tutar; tek meşru yükseltme hibrittir.
3. **Hibrite (Mimari 3) yükseltme MEKANİK tetikleyicilerle:** vault ~15-20k dosyayı aşarsa · 10 erişim görevinden >2'si >5 dosya açtırıyorsa · alias'ların çözemediği diller-arası ıskalar tekrarlıyorsa. Kaçış kapısı: qmd + Qwen3-Embedding-0.6B, ya da DIY LanceDB hibrit.
4. **vault-index REPO'su (CV artefaktı) DONDU** — geri-açma tetiği: PortRisk canlı-link DONE (`00_MASTER_PLAN.md` karar 3; red-team: ikinci repo şimdi açılırsa birincisi bitmez). Çözüldüğü gün blueprint hazır: rapor 2'nin fabrika hattı, aşağıdaki fazlarla.

**Net sonuç:** index vizyonundan bugün alınan şey KOD DEĞİL, üç ucuz konvansiyon (alias/MOC/harita — Homebase'de, tarama onayından sonra) + hazır bekleyen tam blueprint. Bu, BUILD-enerjisinin PortRisk'ten çalınmasını engeller.

## 2. Fabrika hattı — 4 istasyon (özet; ham detay rapor 2)

| İstasyon | Mekanizma | Kilit karar | Solo-kırılma noktası |
|---|---|---|---|
| **1. Gümrük kapısı** | hash-diff keşif + kabul skoru `I = 0.4·novelty + 0.4·importance + 0.2·provenance` + 3 tier + append-only defter; ilk hat: hariç-tutma listesi (`.venv/` tuzağı gerçek — keşifte ~40 çöp .md) | kapı VARLIĞA değil DERİNLİĞE karar verir (tier vanası) | yakalama anında insan kararı → 2. haftada ölür; sessiz yanlış-skor → güven ölümü (mitigasyon: görünür defter, Tier-3 bile başlıktan bulunur) |
| **2. İşçiler** | heading-duyarlı chunking 200-500 token + %15 örtüşme + breadcrumb enjeksiyonu (Anthropic contextual retrieval: −%49 hata); transkriptlere ~350-token geri-düşüş; LLM paketleri yalnız Tier-1 + "ilk dokunuşta terfi" | ham dilim vs damıtık paket → ikisi, tier'lı | "tüm backlog'u LLM'le işle" = bitmeyen göç; `[[link]]` söken chunker bağ verisini imha eder |
| **3. Katı QC** | şema kontrolleri + dedup kaskadı: SHA-256 → MinHash char-5gram (Jaccard ≥0.7) → cosine (oto ≥0.95; 0.88-0.95 LLM hükmü) — eşikler Salih'in KENDİ çift-özüt temizlik verisiyle kalibre (max-F1) + ret/yeniden-yap tavan 2 + karantina | hakim kim → kurallar önce, LLM örneklemde; hakim ≠ işçi modeli (Zheng: kendine-onay yanlılığı) | aşırı katılık = sessiz backlog; kural: karantina sayacı erişimde görünür + >25 maddede oto-gevşeme |
| **4. Yaşayan kütüphane** | tek SQLite (FTS5 + sqlite-vec + tipli kenar tablosu) · hibrit RRF erişim · sıralama = RRF × decay(sınıf,yaş; taban 0.2) × importance · 1-sıçrama komşu genişletme · **supersede kenarları** (decay eskiyi bilir, YANLIŞI bilmez — v6"12 enstrüman" tuzağını yalnız supersede çözer) | graf ağırlığı → hafif tipli kenarlar (GraphRAG bilinçli ertelendi) | senkron gecelik otomatik değilse 1 haftada ıraksama; tabansız oto-link = yumak |

**Tasarım değişmezleri (pazarlıksız):** dosyalar kanonik / index atılabilir önbellek (tek komutla yeniden kurulur — tek-kopya riskinin index ayağını sıfırlar) · yakalama sıfır-karar, hüküm batch · her düğmenin yazılı testi (tek altın soru seti, 20→50 gerçek soru) · iki-dillilik birinci sınıf kısıt (çok-dilli embedding şart: bge-m3 / multilingual-e5; Ollama İngilizce-merkezli varsayılanlarına anti-tavsiye).

## 3. Eşik tablosu ve yoğunluk protokolü

- **Tüm düğmeler + varsayılanlar + ayarlayan testler:** rapor 2 §6 (kapı θ 0.6/0.3 + aylık pişmanlık denetimi <%5 · chunk 200-500 · dedup eşikleri etiketli çiftlerle · decay yarı-ömürleri sınıf-başına · link tabanları 0.75/0.88 · RRF k=24→top 5-8).
- **Bağlam-yoğunluğu (#28) diz-noktası deneyi:** rapor 2 §5 — 12 doküman × 4 yoğunluk (1×/3×/6×/12×) × 2 model sınıfı × 6 soru ≈ 576 puanlı cevap; D\* = doğruluk ≥ %90 taban kalan en yüksek yoğunluk. Eğriler sınıfa göre ayrışmazsa sınıf-routing İPTAL — deney kendi özelliğini öldürebilir (bilimsel yapan bu).

## 4. Fazlı rollout (vault-index çözüldüğü gün; her fazda DONE + öldürme kriteri)

- **Faz 0 — Kanıt Dilimi (1-2 oturum):** Homebase dilimi (~60-100 dosya, hariç-liste aktif) → chunker + bge-m3 + SQLite hibrit + 20 soruluk altın set. DONE: hit@5 ≥ %80 + grep'in bulamadığı ≥1 gerçek cevap. KILL: taramadan sonra hit@5 < %60 → model Türkçede başarısız, önce model değiştir.
- **Faz 1 — Kapı + ayna:** gecelik senkron Routine (loop-eng Faz 4'ün doğal ilk routine'i) + tier defteri + exact/MinHash dedup; Benlik'e genişle. DONE: 14 gün gözetimsiz <24s gecikme; kopya <%2.
- **Faz 2 — QC + çift-özüt infazı:** kalibre semantik dedup + evaluator + karantina. DONE: etiketli sette F1 ≥ 0.9; haftalık inceleme <10 dk.
- **Faz 3 — Yoğunluk + sınıf routing:** diz deneyi; Tier-1'e çift yoğunluk. DONE: ölçülmüş tablo; ayrışma yoksa routing atlanır (negatif sonuç kaydedilir).
- **Faz 4 — Tam kütüphane:** tam korpus + supersede + decay + link genişletme. DONE: 50 soruda hit@5 ≥ %85; MIDAS sürüm-tuzağı v7 döndürüyor.

**CV çerçevesi (çözülme günü için):** repo İngilizce; README'de ölçüm tablosu (recall@k, latency, dedup F1) — ölçümsüz "kişisel RAG" 2026 klişesidir, ölçümlü retrieval mühendisliği sinyaldir (red-team §2.2).

## 5. Homebase bağları

Bu plan havuz maddelerinin doğrudan uygulaması: #5 (wiki=ana rol; çift kapı şerhi = istasyon 2+3), #7 (bilimsel ingest → kabul skoru + eşik testleri; 3-model protokolü = rapor 1'in 3 mimarisi), #14/#24 (routing → gümrük + hakim seçimi), #15 (RAG → erişim montajı), #16/#17 (wiki üretim/sınıf → yoğunluk protokolü), #26 (fabrika deseni → istasyon haritası bire bir), #28 (yoğunluk → §3). Tarama onayından sonra havuza tek satır işaretçi düşülür (Katman 1 — Salih).
