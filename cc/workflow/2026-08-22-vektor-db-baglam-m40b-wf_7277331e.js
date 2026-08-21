export const meta = {
  name: 'vektor-db-baglam-m40b',
  description: 'm.40b ekonomi: 3 aile × (tez → CoVe-Factored antitez → V26 kural-tabanlı örneklem → maskeli hakem) — bağlam verisinin HANGİ sınıflarında ve NASIL vektör DB; determinizm-önceliği (Karar 65); araştırma-sonu DUR (gorev-2026-08-22-1)',
  phases: [
    { title: 'Tez', detail: 'aile başına bağımsız atlas tez koşumu (Opus, medium)', model: 'opus' },
    { title: 'Antitez', detail: 'yalnız iddia listesi verilir (gerekçesiz) — ¬T ara (Opus, medium)', model: 'opus' },
    { title: 'V26', detail: 'KURAL-TABANLI örneklem: son üçte-birden ≥1 URL li iddia + TÜM sayısal iddialar (Sonnet, low)', model: 'sonnet' },
    { title: 'Hakem', detail: 'taraf-maskeli kıyas → SAĞLAM/DARALDI/DÜŞTÜ/ÇELİŞKİLİ + yapı-taşları + deterministik damgası (üst model, high)' },
  ],
}

// ---------- ortak bloklar (emir: cc/gorev-2026-08-22-1.md) ----------
const BAGLAM = `BAĞLAM: Jarvis = tek-kullanıcılı, TÜRKÇE markdown-kanon + SQLite tabanlı kişisel LLM-operasyon sistemi; Claude Code (terminal/masaüstü) üzerinde çalışır. Hafıza = LLM-wiki + ilişkisel silver tablolar + anahtar-değer kaydı + özet belleği (kapsül) + çalışma belleği (CLAUDE.md) + graf (referans tablosu, [[link]]). Sahibin emri (aynen): "vektörler lineer cebirin ve llm'lerin ortaya çıkış sürecinin atası ve data science'da veriyi bir depolama yöntemi. normalde bağlamı saklamanın yollarından bahsetmiştik (graflar, databaseler, llm wiki gibi), vektörler de bağlam datasını saklamanın yollarından biri; bizim aktif hedefimiz bağlam datasını tüm yöntemlerin toplamı optimize bir şekilde saklamaktı. dolayısıyla araştır: bağlam datasını hangi alanlarda, konularda vektör database olarak tutmamız lazım ve nasıl tutmamız lazım; literatür ve güncel bilgimiz bağlamında". Senin ailen bu sorunun bir boyutuna DIŞ KANIT getirir; kararı sen vermezsin, Jarvis için şema/kod tasarlamazsın (araştırma-sonu DUR).
DETERMİNİZM ÖNCELİĞİ (sahibin Katman-1 kuralı, aynen: "determinizmle çelişkilerde determinizm kazanır"): bir yöntem/ürün/model determinizmle çelişiyorsa (rastgele-başlatmalı ANN indeksi HNSW/IVF · sürümü sabitlenemeyen/değişen API embedding · LLM-rerank/LLM-router · rastgele örnekleme) ve deterministik karşılığı varsa (tam brute-force KNN · yerel sabit-sürümlü model · kural-tabanlı füzyon RRF/eşik · sabit tohum) DETERMİNİZM KAZANIR. Her yöntem/ürün/model iddiasına "deterministik: e / h / — (+ neden, tek cümle)" damgası vur; bilmiyorsan "—" ve neyin bilinmediğini yaz.`

const KANON = `KANONDA ZATEN BİLİNENLER (verili; yeniden keşfetme, ÜSTÜNE KOY):
- Jarvis sondajı (deterministik, 08-22; sqlite3 3.51.0 / Python 3.9.6): ham bağlam = bronz (git-izlenen 570 md/json/jsonl, 15,8 MB; wiki 17 sayfa; kanon TÜRKÇE) → silver veri/baglam.sqlite 63,9 MB: kayit 48.957 markdown bloğu (PK = yol#satir_bas-satir_son#sha8 = dosya+satır ADRESİ; metin ort. 232 B, maks 19,2 KB, toplam 11,4 MB) · referans 63.062 ([[link]]/pointer ilişkileri) · dosya 571 · json_kayit 18.795 · hareket 2.356 (araç çağrısı kütüğü) · ambar olgu tabloları. FTS/vektör/embedding tablosu YOK; vektör paketi kurulu DEĞİL (kurulmayacak, yerel sınama yapma). Erişim bugün: Read/Grep/sed (dosya-satır) + sqlite3 (görünüm/CSV); grep -rn tüm bronz ≈0,25 s. Silver bronz'dan sıfırdan yeniden üretilir (functional DE).
- Beyan 9 (08-17, Katman-1): hafıza mimarisi = LLM-wiki + veri teknikleri birlikte; "Vektör DB YOK — bilinçli erteleme: grep+SQLite'ı geçmeyen katman eklenmez; ölçüm tetikli". Karar 60 / KB-43 (08-21): (a) FTS5-önce — BM25 + olgu-zenginleştirilmiş anahtar genişletme + zaman-farkındalı sorgu, embedding'siz; ölçüm: yerel 5-yetenekli eval recall@5 + as-of; hibrit/vektör kararı bu ölçümden SONRA (alternatifler masada: (b) doğrudan hibrit FTS5+yerel embedding+RRF+LLM-rerank (qmd deseni) · (c) hiçbiri). İcra henüz koşmadı. Bu araştırma o "SONRA" adımının girdisidir; karar sırası değişmez.
- rapor-2026-08-17-2 (hafıza teknikleri, m.40b, VERİLİ): Letta dosya-tabanlı LoCoMo %74,0 vs Mem0 graf %68,5 (kurulum semantik-arama+grep bütünü; embedding-kapalı ablasyon YOK) · Karpathy llm-wiki index-önce eşiği ~100 kaynak/yüzlerce sayfa (K) · qmd hibrit (BM25 + yerel vektör → RRF → LLM rerank, cihazda; README bench yalnız fixture bm25 ~0,50 / vector ~0,70 / hybrid ~1,00) · kişisel markdown korpusunda hibrit kazancı GERÇEK korpusta ölçülmemiş; 10⁴-10⁵ parçalık tek-kullanıcı korpusunda BM25↔embedding kıyası literatürde yok (kör nokta) · LongMemEval: anahtar genişletme recall@5 +%9,4 / QA +%5,4; zaman-farkındalı sorgu +%6,8-11,3 (embedding'siz, hakemli) · Generative Agents skor = recency(0,995^saat)·importance·relevance(kosinüs) · Zep/Graphiti çift-zamanlı graf (satıcı rakamları K) · Mem0 vektör+graf+SQLite history (satıcı %26 K) · Anthropic context-engineering yazısı gömme-tabanlı ön-indekslemeye karşı dosya-yolu/grep/glob just-in-time erişimi savunur (D); Anthropic memory tool dosya-tabanlı, vektörsüz (D) · BEIR/MTEB BM25-vs-dense tablosu o koşumda OKUNMADI (kör nokta).
- rapor-2026-08-21-ab4 (D): Anthropic Contextual Retrieval (2024-09-19): chunk'a 50-100 token LLM bağlam-özeti → yalnız contextual embedding retrieval-hatası %35 azalma (5,7→3,7), +BM25 %49 (→2,9), +rerank %67 (→1,9); maliyet $1,02/M token (prompt cache). Anthropic embedding önerisi Voyage.
- rapor-2026-08-18-1/2/3 (VERİLİ): noktasal/anahtarlı erişim = SQLite SEARCH USING INDEX (0,004 ms; adresli-erişim kuralı) · kolon/OLAP = parquet + DuckDB salt-okur (koşullu) · tarama-yöntemi seçim kuralı. Yapısal + anahtarlı + tam-metin hatları kararlı; bu koşum yalnız VEKTÖR hattının yerini/nasılını arar.
- Eski kayıtlar (VERİLİ, pointer'lı): wiki/baglam-veri-ambari: vektör ertelendi (ölçüm tetikli) · core/world-model-tasarimi: "ham blok gerçek kaynak; matris/küp/GÖMME türetilmiş ve KAYIPLI görünümlerdir; design-matrix ancak açık vektörleştirme adımıyla türetilir" · 2026-07 dondurulmuş blueprint: saf RAG hedef DEĞİL, tek meşru yükseltme HİBRİT; hibrite geçiş MEKANİK tetikleri: vault ~15-20k dosyayı aşarsa · 10 erişim görevinden >2'si >5 dosya açtırıyorsa · alias'ların çözemediği diller-arası ıskalar tekrarlıyorsa; tasarım adayı: tek SQLite (FTS5 + sqlite-vec + tipli kenar tablosu) · RRF × decay × importance · 1-sıçrama komşu genişletme · "çok-dilli embedding şart: bge-m3 / multilingual-e5" (K, ölçümsüz) · 07-10 araştırması: yerel RAG vektör deposu = "sessizce çürüyen ikinci gerçek kaynağı" riski; Türkçe EK yapısı sözcüksel yöntemleri kırar (iki-dillilik); FTS5 + vektör → RRF (Cormack 2009) k=24→top 5-8 · 07-24: 146 md'nin %92,5'i graf-yetim; insan-kürasyonlu ↔ oto-inşa graf getiri farkı ÖLÇÜLMEMİŞ · 07-18: A-MEM (embedding k-NN + LLM link), GraphRAG/Leiden, HybridRAG (vektör-bul → 1-hop graf genişlet) · 08-01 (K): kosinüs benzerliği düzenlileştirilmiş embedding'lerde keyfi olabilir (arXiv 2403.05440; anizotropi/hubness); bir hafıza sisteminin RAG'e üstünlüğü embedding modeli değişince TERSİNE döndü.
- Kanon ilkeleri: pointer ilkesi (özet + ADRES; vektör tek başına kaynak değil) · deterministik tasarım + ÖNCELİK KURALI (çelişkide determinizm kazanır) · HAZIRI TEMEL AL · açık kaynak/okunabilirlik (bağımlılık/ağırlık görünür) · üçüncü-şahıs verisi dışarı çıkmaz (API embedding'e metin gönderme SINIRI — soru) · Türkçe kanon (~1,5× token; Türkçe embedding kalitesi SORU) · her sayısal eşik YEREL ölçümle kalibre edilir, ithal edilmez.
- Bilinmeyen (çekirdek): hangi SORGU/VERİ sınıfında yoğun gösterim sözcüksel/yapısal/graf erişime ÖLÇÜLMÜŞ üstünlük sağlar, hangisinde sağlamaz (özellikle tek-kullanıcı, Türkçe, 10⁴-10⁵ parça) · Jarvis veri sınıflarının (karar blokları · wiki kavramları · kütükler · transkriptler · referans grafı · kod · deneyim yörüngeleri) sektör/literatür karşılığı ve depo eşlemesi · NASIL: SQLite-yanı gömülü depo + Türkçe-yeterli yerel/API model + parçalama/zenginleştirme + hibrit füzyon + yeniden-gömme/sürüm işletimi (olgunluk/bakım/lisans/DETERMİNİZM) · eval tarifi · "ne zaman değer" eşiği.
- Kural: ÜRÜN + SÜRÜM + TARİH damgası zorunlu (sqlite-vec v0.1.x · DuckDB VSS sürüm · LanceDB x.y · model adı+sürüm+boyut; benchmark → veri kümesi + metrik + tarih); "hibrit daha iyi" gibi iddialar korpus+ölçüm olmadan K; satıcı beyanı D sayılmaz.`

const DISIPLIN = `ÇIKTI DİSİPLİNİ (zorunlu):
- Her iddiaya URL (birincil kaynak: resmî docs / kaynak kodu README-releases / standart metni / arXiv-ACL / model kartı / benchmark liderlik tablosu). Rakamlar kaynaklı; kestirimse "[?]". Örneklem/kapsam/sürüm/veri-kümesi yaz (çıplak yüzde yasak). Her sayısal iddiada figure alanını doldur — sonradan KAYNAĞA İNİLEREK denetlenecek.
- UYDURMA YASAK. "bulunamadı" meşru sonuçtur. "[ARANAMADI]" = arama hiç yapılamadı (bütçe/erişim). Erişim engeli (403/paywall) açıkça bayraklanır.
- Etiket: D = birincil kaynaktan doğrulandı · K = ikincil/özet, teyide muhtaç · X = doğrulanamadı/çelişkili. SATICI PAZARLAMA iddiası D sayılmaz (benchmark tablosu/metodoloji görülmedikçe K).
- Niceleyici ayrımı: "her" (∀) ↔ "bazı" (∃) karıştırma. Ürün+sürüm+tarih ∨ veri-kümesi damgası her iddiada. Her yöntem/ürün/model iddiasında determinism alanı dolu (e / h / — + neden).
- Bütçe İDARELİ: ~10-15 dış erişim; bilinen birincil kaynağa DOĞRUDAN git; arama yalnız var/yok negatifi için. Bütçe biterse belirt.
- Repoya/diske HİÇBİR DOSYA YAZMA. Paket KURMA, yerel sınama YAPMA. Alt-ajan AÇMA. Tek çıktın yapısal cevaptır. Karar ALMA, Jarvis şeması TASARLAMA — sen kanıt getir.`

const FAMILIES = [
  { key: 'A', title: 'LİTERATÜR — HANGİ SORGU/VERİ SINIFI HANGİ YÖNTEMDE KAZANIR (yoğun ↔ sözcüksel ↔ hibrit ↔ graf ↔ yapısal)',
    questions: `A1. Yoğun (embedding) ↔ sözcüksel (BM25) ↔ hibrit ↔ öğrenilmiş-seyrek (SPLADE/ColBERT): BEIR (Thakur 2021: BM25 sıfır-atış tabanı, yoğun modellerin alan-dışı düşüşü — nDCG@10 sayıları) · MTEB retrieval (güncel liderlik; hangi modeller, hangi veri kümeleri) · hibrit füzyon (RRF / konveks birleşim; Bruch ve ark. 2023; ölçülmüş kazanç + ne zaman ZARAR) — hangi SORGU sınıfı nerede kazanır: tam-eşleşme/anahtar/numara/özel-ad/kod-tanımlayıcı ↔ parafraz/kavram/eşanlam/çok-dilli. Sayı + veri kümesi + tarih.
A2. Ajan-hafıza/uzun-bağlam eval'lerinde GETİRME bileşeninin kazancı: LongMemEval (getirme grain'i oturum↔tur; sorgu tipi: tek-oturum · çok-oturum · zamansal · bilgi-güncelleme · çekimser) · LoCoMo · MemoryAgentBench/MemBench · "RAG or long-context?" (Li ve ark. 2024; Self-Route) · lost-in-the-middle — yoğun getirmenin hangi SORU tipinde işe yaradığı/yaramadığı (tek-atlamalı ↔ çok-atlamalı ↔ zamansal ↔ toplama).
A3. Yoğun gösterimin BAŞARISIZ olduğu sınıflar (kanıt): olumsuzlama · kesin sayılar/tarihler/ID'ler · nadir varlıklar/uzun-kuyruk · parça-sınırı kaybı · uzun belge · çok-dilli/az-kaynaklı dil (TÜRKÇE: MTEB/çok-dilli benchmark'larda sayı var mı) · kod (CodeSearchNet; sembol-indeksi↔embedding) — ve buna karşılık graf (GraphRAG Edge 2024 global sensemaking · HippoRAG çok-atlamalı · Graphiti zamansal) ile yapısal/SQL (text-to-SQL, anahtarlı erişim) erişimin ÖLÇÜLMÜŞ kazandığı sınıflar.
A4. Embedding'in DEPOLAMA olarak doğası: determinizm (aynı model+girdi → aynı vektör mü; API/donanım/sürüm/batch kaynaklı sapmalar — ölçülmüş örnek; bu Jarvis için ÖNCELİKLİ soru) · model değişince korpusun yeniden gömülmesi zorunluluğu (embedding drift / model versioning — kaynak) · vektörün geri-çözülebilirliği (Vec2Text inversion — gizlilik) · vektör tek başına kaynak DEĞİL (metin/pointer eşlik) · depolama/maliyet ölçeği (n×d×bayt; int8/binary kuantizasyon kalite kaybı sayıları; Matryoshka boyut kırpma).`,
    antitezHint: 'BM25 tek başına çoğu sınıfta yeter · yoğun her yerde kazanır · hibrit kazancı korpus-bağımlı, bazen zarar · eval kümeleri tek-kullanıcı Türkçe korpusu temsil etmez · embedding determinizmi pratikte sorun değil / ya da pratikte asla sağlanamaz.' },
  { key: 'B', title: 'NASIL — TEK-KULLANICI ~49k PARÇA TÜRKÇE MARKDOWN+SQLite KORPUSU İÇİN DEPO · MODEL · PARÇALAMA · HİBRİT · İŞLETİM (hazır ürünler)',
    questions: `B1. Gömülü vektör depoları (her biri: ne yapar · kurulum/bağımlılık · indeks türü (brute-force/HNSW/IVF) ve DETERMİNİZMİ (sabit tohum? aynı sorgu aynı sıra?) · metadata filtre · hibrit/FTS desteği · ölçek sınırı · sürüm · bakım/sahip/lisans · SQLite ile birlikte yaşama): sqlite-vec (vec0 sanal tablo, KNN, kuantizasyon; sürüm/olgunluk) · sqlite-vss (emekli mi?) · vectorlite · DuckDB VSS (HNSW, deneysel; kalıcılık sınırı) · LanceDB (gömülü; FTS+vektör hibrit) · Chroma (gömülü) · FAISS (kütüphane) · pgvector/pgvectorscale · Qdrant/Milvus-lite. Küçük ölçekte (10⁴-10⁵ vektör) brute-force tam KNN yeter mi: gecikme/bellek sayıları (kaynak); ANN ne zaman gerekir.
B2. Embedding modelleri (her biri: boyut · bağlam uzunluğu · çok-dilli/TÜRKÇE ölçümü (MTEB Türkçe alt-görevleri var mı, sayı) · yerel koşum yolu (sentence-transformers/ONNX/llama.cpp/ollama, Apple Silicon) · maliyet $/M token (API) · lisans · determinizm/sürüm sabitleme (API modeli sessizce değişir mi; yerel ağırlık dosyası sabit mi)): bge-m3 · bge-small/base · nomic-embed-text v1.5 · multilingual-e5 · gte · all-MiniLM-L6 · Voyage (Anthropic önerisi: voyage-3/3.5, multilingual) · OpenAI text-embedding-3 (small/large) · Cohere embed v4 (multilingual) · Gemini embedding. Türkçe için hangi modeller ÖLÇÜLMÜŞ; yerel↔API ödünleşimi (gizlilik · maliyet · determinizm).
B3. Parçalama + zenginleştirme + sıralama: chunk boyutu/örtüşme, Markdown başlık-temelli ↔ sabit-token (ölçüm: Chroma chunking tech report, LlamaIndex, diğer) · contextual retrieval (VERİLİ; nasıl uygulanır, maliyet, LLM-üretimli özet deterministik mi) · late chunking (Jina) · parent-child/hierarchical (RAPTOR) · reranker'lar (bge-reranker, Cohere rerank, ColBERT/jina-colbert; kazanç sayıları; deterministik mi) · RRF/konveks füzyon parametreleri · metadata filtresi (yol/tarih/tür) · SQLite FTS5 + sqlite-vec hibrit uygulama örnekleri (Garcia'nın hybrid-search örneği; qmd) — kod-seviyesinde desen + sayı.
B4. İşletim: değişen blok → yeniden gömme (içerik-hash ile idempotent senkron; kayıt PK'sı zaten sha8 içeriyor) · model sürüm kolonu + toplu yeniden gömme maliyeti (49k × ort. 232 B ≈ 11,4 MB metin ≈ [?] token → $/yerel süre) · depolama boyutu (49k × 768/1024 boyut × 4 B ≈ 150-200 MB; int8/binary ile) · Claude Code/MCP entegrasyonu (vektör-depo MCP sunucuları; olgunluk/güvenlik) · gizlilik (API'ya metin gitmesi ↔ yerel) · Türkçe token maliyeti. Hazırı temel al: sıfırdan embedding boru hattı yazmak yerine hangi ürün kurulu-çalışır.`,
    antitezHint: 'sqlite-vec/DuckDB VSS olgunlaşmamış (pre-1.0, kalıcılık/bakım riski) · yerel modeller Türkçe\'de zayıf · API embedding gizlilik/maliyet/determinizmi kırar · küçük korpusta grep/FTS5 yeter · chunking/rerank kazançları satıcı beyanı · brute-force KNN 10⁵ vektörde bile yavaş değil — ANN gereksiz.' },
  { key: 'C', title: 'KOMPOZİSYON — "TÜM YÖNTEMLERİN OPTİMİZE TOPLAMI": çok-depolu mimarilerin veri→depo ayrımı · yönlendirme · EVAL TARİFİ · Jarvis veri-sınıfı haritası · eşik',
    questions: `C1. Çok-depolu ajan-hafıza mimarilerinde HANGİ VERİ HANGİ DEPODA (resmî doküman/kaynak kodu): Letta (core blok · archival=pgvector · recall=SQL/konuşma) · Mem0 (vektör + graf (Mem0g) + SQLite history) · Zep/Graphiti (KG düğüm/kenar + embedding + BM25 + RRF) · LangGraph Store/LangMem (semantic index) · LlamaIndex/LangChain (router/ensemble retriever) · Cognee · qmd + Karpathy llm-wiki (index-önce + hibrit arama) · Anthropic memory tool (dosya) — tasarım kuralı + varsa ölçüm; yönlendirme: sorgu-tipi→depo (KURAL-tabanlı ↔ LLM sınıflandırıcı; Adaptive-RAG, Self-RAG, Self-Route; ölçülmüş kazanç/maliyet; deterministik olanı hangisi).
C2. EVAL TARİFİ (hazır): BEIR-stili nDCG@10/recall@k/MRR · RAGAS · LongMemEval 5-yetenek kırılımı · "altın soru kümesi" nasıl kurulur (LLM-üretilmiş soru + insan doğrulama; Anthropic contextual-retrieval eval tarifi; kaç soru yeter — istatistiksel güç) · as-of/zaman doğruluğu · maliyet ölçümü (ms, token, $) · hazır araçlar (ir_measures, ranx, BEIR, ragas, MTEB özel görev) · vektör↔FTS5↔hibrit kıyasının AYNI korpusta adil ölçümü (aynı parça, aynı sorular, deterministik tekrar).
C3. JARVIS VERİ SINIFLARI → literatür/sektör karşılığı (kanıt; KARAR değil): (i) numaralı karar/kural blokları (KB-n, Karar n, İB-n, m.NN) → anahtarlı/SQL erişim · (ii) wiki kavram sayfaları + ders notları (düzyazı, kavramsal, Türkçe) → yoğun getirme ADAYI (kanıt: kavram/parafraz sorgusu) · (iii) araç-çağrısı kütükleri + ambar (yapısal, zaman damgalı) → SQL/kolon · (iv) transkript/prompt olayları (konuşma, uzun) → FTS5 + zaman; yoğun aday (LongMemEval oturum↔tur grain) · (v) referans grafı ([[link]], pointer) → graf/çok-atlamalı · (vi) kod/script → sembol indeksi ↔ embedding (ölçüm) · (vii) deneyim yörüngeleri (few-shot) → benzer-vaka getirme (KATE/EPR örnek-seçimi: embedding-tabanlı seçim kazancı sayıları; BM25 ile kıyas) · (viii) kapsül/CLAUDE.md (her zaman bağlamda) → depo dışı. Her sınıf için: ölçülmüş kanıt ∨ "yok".
C4. EŞİK + REJİM: "ne zaman vektör katmanı eklemeye değer" için yayımlanmış eşik/kural (Karpathy ~100 kaynak K; qmd; "RAG ne zaman gerekmez"; uzun-bağlam maliyeti) · 10⁴-10⁵ parça tek-kullanıcı ölçeğinde brute-force gecikme/bellek (sqlite-vec/numpy ölçümleri) · determinizm/tekrar-üretim (model+sürüm sabitleme; aynı sorgu → aynı sıra; hangi bileşen bozar) · açık kaynak/okunabilirlik (ağırlıklar repo dışı; venv; bağımlılık sayısı) · çok-depolu mimarinin karmaşıklık borcu (bakım, tutarlılık, senkron, "ikinci gerçek kaynak" riski) — sayı + kaynak.`,
    antitezHint: 'çok-depolu mimari karmaşıklık borcu · router\'lar ölçümsüz · Jarvis ölçeğinde FTS5+SQL+pointer yeter · few-shot seçimi için embedding şart değil (BM25 benzer) · eval kümesi küçükken fark istatistiksel anlamsız · deterministik yönlendirme (kural) LLM router\'dan kötü değil.' },
]

// ---------- şemalar ----------
const PLACEMENTS = ['veri-sınıfı-kuralı','yöntem-kıyası','hazır-ürün','model-seçimi','parçalama-zenginleştirme','işletim-kuralı','ölçüm-yöntemi','girmez']
const JARVIS = ['kullanıyoruz-eş','kısmi','eksik-aday','girmez']
const CLAIM = { type: 'object', additionalProperties: false, required: ['id','claim','label','source_url','figure','scope','determinism','placement_suggestion'],
  properties: {
    id: { type: 'string', description: 'A1-1 gibi: soru-no + sıra' },
    claim: { type: 'string', description: 'tek cümle iddia (Türkçe)' },
    label: { type: 'string', enum: ['D','K','X'] },
    source_url: { type: 'string', description: 'URL ya da "bulunamadı" ya da "[ARANAMADI]"' },
    figure: { type: 'string', description: 'rakam/eşik/sayı/tarih/sürüm (kaynaklı; kestirimse [?]); yoksa "-"' },
    scope: { type: 'string', description: 'ürün+sürüm+tarih ∨ veri-kümesi+metrik + örneklem/kapsam; yoksa "-"' },
    determinism: { type: 'string', description: 'yöntem/ürün/model iddiasıysa "e" / "h" / "—" + tek-cümle neden (aynı girdi → aynı çıktı mı; hangi bileşen bozar); iddia yöntem değilse "-"' },
    placement_suggestion: { type: 'string', description: 'yerleşim (' + PLACEMENTS.join(' / ') + ') + Jarvis eşlemesi (' + JARVIS.join(' / ') + ') + damga' },
  } }
const TEZ_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','claims','gaps','access_blocks','budget_note'],
  properties: {
    family: { type: 'string' },
    claims: { type: 'array', minItems: 4, maxItems: 10, items: CLAIM },
    gaps: { type: 'array', items: { type: 'string' }, description: 'aranıp bulunamayanlar (kör nokta adayları)' },
    access_blocks: { type: 'array', items: { type: 'string' }, description: '403/paywall/[ARANAMADI]' },
    budget_note: { type: 'string', description: 'kaç arama/fetch yapıldı, bütçe bitti mi' },
  } }
const REBUT = { type: 'object', additionalProperties: false, required: ['target_id','negation','verdict','evidence_url','figure','note'],
  properties: {
    target_id: { type: 'string' },
    negation: { type: 'string', description: '¬T: savunulan ters önerme (tek cümle)' },
    verdict: { type: 'string', enum: ['ÇÜRÜTÜLDÜ','DARALTILDI','ÇÜRÜTÜLEMEDİ'] },
    evidence_url: { type: 'string', description: 'URL ya da "bulunamadı"' },
    figure: { type: 'string', description: 'rakam varsa; yoksa "-"' },
    note: { type: 'string', description: 'DARALTILDI ise daraltılmış hâl; ÇÜRÜTÜLEMEDİ ise ne arandı; determinizm itirazı varsa burada' },
  } }
const ANTI_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','rebuttals','extra_counter_claims','budget_note'],
  properties: {
    family: { type: 'string' },
    rebuttals: { type: 'array', maxItems: 10, items: REBUT },
    extra_counter_claims: { type: 'array', maxItems: 3, items: CLAIM, description: 'tezde olmayan ama mekanizmayı ilgilendiren KARŞI yönlü bulgular' },
    budget_note: { type: 'string' },
  } }
const V26_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','checks'],
  properties: {
    family: { type: 'string' },
    checks: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['claim_id','url','result','note'],
      properties: { claim_id: { type: 'string' }, url: { type: 'string' }, result: { type: 'string', enum: ['TUTUYOR','TUTMUYOR','ERİŞİLEMEDİ'] }, note: { type: 'string' } } } },
  } }
const HAKEM_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','verdicts','building_blocks','blind_spots','survival'],
  properties: {
    family: { type: 'string' },
    verdicts: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['claim_id','verdict','surviving_form','reason'],
      properties: { claim_id: { type: 'string' }, verdict: { type: 'string', enum: ['SAĞLAM','DARALDI','DÜŞTÜ','ÇELİŞKİLİ'] }, surviving_form: { type: 'string', description: 'hayatta kalan (gerekirse daraltılmış) önerme; DÜŞTÜ ise "-"' }, reason: { type: 'string', description: '≤2 cümle: hangi kanıt hangi kanıtı neden yendi' } } } },
    building_blocks: { type: 'array', minItems: 3, maxItems: 8, items: { type: 'object', additionalProperties: false, required: ['block','source_url','placement','jarvis','deterministic','confidence'],
      properties: { block: { type: 'string' }, source_url: { type: 'string' }, placement: { type: 'string', enum: PLACEMENTS, description: 'yerleşim sınıfı' }, jarvis: { type: 'string', enum: JARVIS, description: 'Jarvis eşlemesi (sondajdaki mevcut duruma göre)' }, deterministic: { type: 'string', enum: ['e','h','—'], description: 'Karar 65: h ise yapı-taşı "girmez" ya da deterministik varyantıyla birlikte yazılır' }, confidence: { type: 'string', enum: ['D','K'] } } } },
    blind_spots: { type: 'array', items: { type: 'string' } },
    survival: { type: 'object', additionalProperties: false, required: ['saglam','daraldi','dustu','celiskili'], properties: { saglam: { type: 'integer' }, daraldi: { type: 'integer' }, dustu: { type: 'integer' }, celiskili: { type: 'integer' } } },
  } }

// ---------- V26 KURAL-TABANLI seçim (Salih imzası 08-17; deterministik — rastgele YOK) ----------
const isUrl = s => /^https?:\/\//.test(s || '')
const isNumeric = (fig, txt) => (fig && fig !== '-' && /\d/.test(fig)) || /\d+\s?%|\bn\s?=\s?\d|\d+\s?×|\d+\s?pp\b/.test(txt || '')
function v26Picks(items, idOf, txtOf, urlOf, figOf) {
  const picks = []; const seen = new Set()
  const add = (it, why) => { const id = idOf(it); if (seen.has(id)) return; seen.add(id); picks.push({ claim_id: id, claim: txtOf(it), url: urlOf(it), figure: figOf(it), why }) }
  const n = items.length
  if (!n) return picks
  const start = Math.floor(n * 2 / 3)
  for (let i = start; i < n; i++) { if (isUrl(urlOf(items[i]))) { add(items[i], 'son-üçte-bir'); break } }
  items.forEach(it => { if (isNumeric(figOf(it), txtOf(it)) && isUrl(urlOf(it))) add(it, 'sayısal') })
  return picks
}

// ---------- aşamalar ----------
const tezStage = (fam) => agent(
`ROL: Atlas TEZ araştırmacısı — aile ${fam.key}: ${fam.title}. Bağımsız çalışıyorsun; başka ailenin sorusuna cevap verme.
${BAGLAM}

${KANON}

ARAŞTIRMA SORULARI (yalnız bunlar):
${fam.questions}

${DISIPLIN}
Çıktı: 4-10 iddia (her soruya ≥1), her biri kaynaklı; gaps/access_blocks/budget_note doldur. Sayısal iddialarda figure alanı ZORUNLU dolu; her iddiada ürün-sürüm ∨ veri-kümesi damgası; yöntem/ürün/model iddialarında determinism alanı dolu.`,
  { label: `tez:${fam.key}`, phase: 'Tez', agentType: 'atlas', model: 'opus', effort: 'medium', schema: TEZ_SCHEMA })

const antitezStage = (tez, fam) => {
  if (!tez) return null
  const claimsOnly = tez.claims.map(c => `${c.id}: ${c.claim}`).join('\n')  // gerekçe/kaynak GEÇMEZ (CoVe-Factored)
  return agent(
`ROL: Atlas ANTİTEZ ajanı (açık Devil's-Advocate) — aile ${fam.key}: ${fam.title}.
Sana bir başka araştırmacının İDDİA satırları veriliyor; GEREKÇELERİ ve KAYNAKLARI kasıtlı olarak verilmiyor (çıpalama freni). Görevin: her iddianın DEĞİLİNİ (¬T) savunacak BİRİNCİL kanıt aramak — "alternatif bakış" değil, lojiksel ters. Çürütemediysen "ÇÜRÜTÜLEMEDİ" yaz ve ne aradığını belirt; süs-antitez ÜRETME. Kısmen çürüttüysen DARALTILDI + daraltılmış hâlini yaz. Determinizm-önceliği gereği: iddia bir yöntemi/ürünü "deterministik" sayıyorsa bunun aksini (rastgelelik/sürüm kayması/batch etkisi) da ara.
Ek olarak: tezde OLMAYAN ama mekanizmayı ilgilendiren karşı-yönlü bulgular varsa extra_counter_claims'e ekle (≤3). Yön ipuçları (bağlayıcı değil): ${fam.antitezHint}
${BAGLAM}

${KANON}

İDDİALAR:
${claimsOnly}

${DISIPLIN}`,
    { label: `antitez:${fam.key}`, phase: 'Antitez', agentType: 'atlas', model: 'opus', effort: 'medium', schema: ANTI_SCHEMA }
  ).then(anti => ({ tez, anti }))
}

const v26Stage = (r, fam) => {
  if (!r || !r.tez) return null
  const tezPicks = v26Picks(r.tez.claims, c => c.id, c => c.claim, c => c.source_url, c => c.figure)
  const antiItems = ((r.anti && r.anti.rebuttals) ? r.anti.rebuttals : []).filter(x => x.verdict !== 'ÇÜRÜTÜLEMEDİ')
  const antiPicks = v26Picks(antiItems, x => `¬${x.target_id}`, x => `${x.negation} [${x.verdict}: ${x.note}]`, x => x.evidence_url, x => x.figure)
  const picks = tezPicks.concat(antiPicks)
  const rule = { tez: tezPicks.map(p => `${p.claim_id}(${p.why})`), antitez: antiPicks.map(p => `${p.claim_id}(${p.why})`) }
  if (!picks.length) return Promise.resolve({ ...r, v26: { family: fam.key, checks: [] }, v26_rule: rule })
  return agent(
`ROL: V26 örneklem-denetçisi (aile ${fam.key}). Aşağıdaki iddia→URL çiftleri KURAL-TABANLI seçildi (çıktının son üçte-birinden ≥1 + tüm sayısal iddialar). Her biri için KAYNAĞA İN (WebFetch): iddia ve rakam kaynak metinde GERÇEKTEN var mı? Sonuç: TUTUYOR / TUTMUYOR / ERİŞİLEMEDİ (403-paywall). Not: tek cümle — kaynakta ne gördün (rakamı aynen aktar). Uydurma yok; yorum yok; yalnız doğrula. Repoya dosya yazma, alt-ajan açma.
${picks.map((p,i)=>`${i+1}. [${p.claim_id}] "${p.claim}" — rakam: ${p.figure} — URL: ${p.url}`).join('\n')}`,
    { label: `v26:${fam.key}`, phase: 'V26', model: 'sonnet', effort: 'low', schema: V26_SCHEMA }
  ).then(v26 => ({ ...r, v26, v26_rule: rule }))
}

const hakemStage = (r, fam, idx) => {
  if (!r || !r.tez) return null
  const rebutBy = {}
  ;((r.anti && r.anti.rebuttals) || []).forEach(x => { rebutBy[x.target_id] = x })
  const mask = {}
  const pairs = r.tez.claims.map((c, i) => {
    const x = rebutBy[c.id]
    const tezFirst = ((idx + i) % 2 === 0)
    mask[c.id] = tezFirst ? 'Taraf-1=tez' : 'Taraf-1=antitez'
    const P = `Önerme P: ${c.claim}\n  kanıt: ${c.source_url} · rakam: ${c.figure} · kapsam: ${c.scope} · deterministik: ${c.determinism}`
    const N = x ? `Önerme ¬P: ${x.negation}\n  kanıt: ${x.evidence_url} · rakam: ${x.figure} · not: ${x.note} · karşı-tarafın öz-değerlendirmesi: ${x.verdict}` : `Önerme ¬P: (karşı-taraf bu önermeye itiraz getirmedi)`
    return `### ${c.id}\n${tezFirst ? 'Taraf-1 — ' + P + '\nTaraf-2 — ' + N : 'Taraf-1 — ' + N + '\nTaraf-2 — ' + P}`
  }).join('\n\n')
  const extras = ((r.anti && r.anti.extra_counter_claims) || []).map(c => `- [${c.id}] ${c.claim} — ${c.source_url} · ${c.figure} · ${c.scope} · deterministik: ${c.determinism}`).join('\n')
  const v26txt = (r.v26 && r.v26.checks || []).map(c => `- [${c.claim_id}] ${c.url} → ${c.result}: ${c.note}`).join('\n')
  return agent(
`ROL: MASKELİ HAKEM — aile ${fam.key}: ${fam.title}. Sen üretici koşumların devamı DEĞİLSİN; iki tarafın hangisinin "tez" hangisinin "antitez" olduğu sana SÖYLENMİYOR — iddia+kanıt olarak tart.
Ölçüt = adversarial-hayatta-kalma: bilgili karşı-tarafın çürütmeyi deneyip BAŞARAMADIĞI önerme SAĞLAM; kısmen çürüyen DARALDI (hayatta kalan daraltılmış hâlini yaz); çürüyen DÜŞTÜ; iki taraf da güçlü ve uzlaşmazsa ÇELİŞKİLİ (saklama, öyle yaz). Kanıt gücü: birincil > ikincil; rakamlı > rakamsız; sürüm/veri-kümesi damgalı > damgasız. KAYNAK-DENETİMİ kuralı (V26): bir tarafın denetlenen iddiası TUTMUYOR çıktıysa o tarafın o ailedeki TÜM iddiaları K'ya düşer (nota yaz). Şüphede kaynağa kendin inebilirsin (WebFetch), bütçe idareli (≤6).
DETERMİNİZM ÖNCELİĞİ (sahibin kuralı, Karar 65): yapı-taşı deterministik değilse (deterministic=h) ya "girmez" ya da deterministik varyantıyla BİRLİKTE yazılır; çelişkide determinizm kazanır — bunu hükümlerde açıkça uygula.
Sonda: bu aileden JARVIS'e girecek 3-8 yapı-taşı (yalnız SAĞLAM/DARALDI önermelerden; her biri kaynak URL + yerleşim: ${PLACEMENTS.join(' / ')} + Jarvis-eşleme: ${JARVIS.join(' / ')} + deterministic e/h/— + ürün-sürüm ∨ veri-kümesi damgası; 'hazır-ürün' yalnız bakım/güvenlik/lisans durumu bilinen ürünlerde) + kör noktalar (aranıp bulunamayan; özellikle TÜRKÇE ölçüm · 10⁴-10⁵ tek-kullanıcı korpus ölçümü · hibrit kazancının gerçek korpusta ölçümü · embedding determinizm ölçümü yoksa AÇIKÇA) + survival sayımı.
${BAGLAM}

## ÇİFTLER
${pairs}

## KARŞI-TARAFIN EK BULGULARI (teze itiraz dışı)
${extras || '(yok)'}

## KAYNAK-DENETİMİ (bağımsız, kural-tabanlı örneklem)
${v26txt || '(yapılamadı)'}

## Tezin kendi beyan ettiği boşluklar/erişim engelleri
${(r.tez.gaps||[]).map(g=>'- '+g).join('\n') || '(yok)'}
${(r.tez.access_blocks||[]).map(g=>'- ⚠ '+g).join('\n')}`,
    { label: `hakem:${fam.key}`, phase: 'Hakem', effort: 'high', schema: HAKEM_SCHEMA }
  ).then(hakem => ({ ...r, hakem, mask }))
}

log('gorev-2026-08-22-1 sahada: 3 aile × tez(opus)→antitez(opus)→V26 kural-tabanlı(sonnet)→hakem(üst model) — pipeline, barrier yok; determinizm-önceliği (Karar 65) tüm rollerde')
const results = await pipeline(FAMILIES, tezStage, antitezStage, v26Stage, hakemStage)
const out = {}
FAMILIES.forEach((f, i) => { out[f.key] = results[i] || null })
const done = FAMILIES.filter((f,i)=>results[i] && results[i].hakem).map(f=>f.key)
log(`Tamam: hakem çıktısı olan aileler = ${done.join(',') || 'yok'}`)
return { date: args && args.date, emir: (args && args.emir) || 'cc/gorev-2026-08-22-1.md', families: out }