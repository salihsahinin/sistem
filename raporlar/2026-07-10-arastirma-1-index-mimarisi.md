# Görev Raporu — Yerel Bilgi Index'i: 3 Aday Mimari

**Ajan:** araştırma-1 (index mimarisi) · **Tarih:** 2026-07-10 · **Statü:** rapor — karar içermez · **Tüketen:** `02_KNOWLEDGE_INDEX_PLAN.md`

**Kapsam varsayımları:** tek Windows 11 makine, tek kullanıcı, ~binlerce iki-dilli (TR/EN) markdown, tek güvenlik ağı git, orkestratör Claude Code; kullanıcının belgelenmiş hata modu = bakım rutinlerini terk etmek. Entegrasyon gerçeği: index ya (a) Grep'lenebilir düz dosya, ya (b) çağrılabilir CLI, ya (c) MCP server olmalı — (a) doğal, (b)/(c) birinin kurup yaşatması gereken tutkal.

---

## Mimari 1 — Konvansiyon + Tam-Metin Arama (embedding yok)

**Nasıl çalışır.** Vault'un kendisi index'tir: katı klasör/adlandırma konvansiyonu, her notta YAML frontmatter sözleşmesi (`project`, `status`, `date` ve kritik olarak TR/EN eşanlamlıları taşıyan `aliases:`) ve hub "Map of Content" notları (klasör başına `_INDEX.md`, kökte `KNOWLEDGE-MAP.md`). Erişim ripgrep'tir — Claude Code zaten Grep aracı olarak taşır — istenirse BM25 sıralamalı tek-dosya SQLite FTS5 ile desteklenir. Wiki-linkler `[[...]]` ilişki katmanıdır. Orkestratör LLM "semantiği" kendisi sağlar: sorguyu yeniden yazar, TR+EN+eşanlam varyantları üretir, adayları tarayarak fiili reranker olur.

**Gerçek araçlar (hepsi yerel, hepsi Windows):**
- **ripgrep** — Claude Code içinde geliyor; bağımsız: `winget install BurntSushi.ripgrep.MSVC`.
- **SQLite FTS5** — makinedeki Python 3.11'in stdlib'inde; BM25, prefix sorguları (`portföy*`), `unicode61 remove_diacritics 2` tokenizer. Tek `.db`, ~60 satır Python.
- **git grep / `git log -S`** (pickaxe) — "X'i ilk ne zaman yazdım" tarihçe sorgusu, bedava.
- **Obsidian konvansiyonları** yalnız veri formatı olarak (wiki-link, frontmatter) — sorgu anında Obsidian süreci gerekmez.
- Opsiyonel: **ugrep** (fuzzy `-Z`, boolean), **fd** (dosya adı).
- **Türkçe notu:** Türkçe eklemeli dil (*portföy → portföyümdeki*), prefix/substring eşleme çekimli halleri stemmer'sız yakalar — düz FTS Türkçede beklenmedik ölçüde işler. Bilinen tuzak: Unicode case folding Türkçe İ/ı kuralını uygulamaz; `rg -i ingilizce` "İngilizce"yi kaçırabilir → erişim tarifi iki i-varyantını da üretir + FTS5'te `remove_diacritics 2`. Gerçek vault'ta bir kez test edilecek.

**Stat kartı:**

| Boyut | Puan | Dayanak |
|---|---|---|
| Erişim kalitesi | 6/10 | Tam ad/tarih/proje terimi — kişisel ops vault sorgularının çoğu — güvenilir vuruyor; parafraz ve unutulmuş-kelime sorguları alias/MOC ya da ajan yeniden-yazımı yoksa ıskalıyor. |
| Kurulum maliyeti | 9/10 | ripgrep orkestratörün içinde; "konvansiyon" yazılım değil kural sayfası; opsiyonel FTS5 kurulu yorumlayıcıda ~60 satır stdlib Python. |
| Bakım sürtünmesi | 8/10 | Salt grep'te bakılacak şey yok; tek vergi editoryal disiplin + mevcut git hook'una asılabilen tek komutluk FTS yeniden-inşası. |
| Token verimi | 6/10 | Grep satır döndürür, cevap değil — ajan soru başına 2-4 aday dosya açar; MOC ve disiplinli başlıklar bunu yükseltir. |
| Açıklanabilirlik | 10/10 | Sonucun kendisi açıklamadır: literal eşleşme + dosya yolu. Yorumlanacak bir şey yok. |
| Makine maliyeti | 10/10 | Birkaç bin .md üzerinde milisaniyeler; yerleşik süreç, RAM, model dosyası sıfır. |

**Artılar:** sıfır yeni altyapı; ajan-doğal; gürültülü ve görünür bozulur (ıskalama tek bakışta teşhis edilir); iki-dilli substring kutudan çıkar; yatırılan her saat *curation'a* gider ve her gelecek mimaride bileşik değer taşır; türetilmiş yedeklenecek durum yok — git'teki .md'ler tek gerçek kalır.

**Eksiler:** kelime-uyuşmazlığında sert recall tavanı ("risk hesabı", yalnız "VaR" yazan notu alias köprüsü yoksa bulamaz); kalite, yokluğu geçmiş rutinleri öldüren disipline biner; çıplak rg'de gerçek sıralama yok (FTS5 BM25 ekler ama Türkçe stemmer'sız); ajan-güdümlü aramanın token maliyeti korpus gürültüsüyle büyür.

---

## Mimari 2 — Yerel RAG (embedding + vektör deposu)

**Nasıl çalışır.** Markdown heading-duyarlı parçalara bölünür (kısa kişisel notlarda parça = notun tamamı çoğu kez doğru ve daha basit), her parça yerel çok-dilli modelle embed edilir, vektörler diskte gömülü depoda yaşar. Sorgu embed edilir, k-en-yakın-komşu benzerliğiyle cevaplanır; top-k parça küçük bir CLI ya da MCP üzerinden orkestratöre döner. Index vault ile senkron tutulmalıdır — kayıtta izleyici, zamanlanmış iş ya da elle yeniden-index.

**Gerçek araçlar:**
- **Embedding modelleri (TR+EN için çok-dilli ŞART):** **bge-m3** (BAAI, 568M, 100+ dil, 8k bağlam — güvenli varsayılan), **Qwen3-Embedding-0.6B** (639MB, ~64.3 MTEB multilingual — 1GB-altı en güçlü, 2026 ortası), **EmbeddingGemma-300m** (Google, 622MB, cihaz-içi için). **Anti-tavsiye:** Ollama blog varsayılanları `nomic-embed-text` ve `mxbai-embed-large` İngilizce-merkezli — vault'un Türkçe yarısını sessizce katleder.
- **Çalışma zamanı:** **Ollama for Windows** (`ollama pull bge-m3`), **LM Studio** (`/v1/embeddings`), ya da Python 3.11'de **sentence-transformers** / **fastembed** (ONNX, PyTorch'suz).
- **Vektör depoları:** **LanceDB** (`pip install lancedb`, gömülü, dosya-tabanlı, server'sız — ilk tercih), **sqlite-vec** (SQLite eklentisi, kaba-kuvvet exact KNN — bu ölçekte yeterli; dikkat: hâlâ v1-öncesi alpha 0.1.10, kırıcı değişiklik beklenir; SQLite ekibinin kendi `vec1` eklentisi resmi alternatif olarak doğuyor), **Chroma** (gömülü, popüler, ağır bağımlılık ağacı). **Qdrant/Weaviate/pgvector:** gerçek ama server — tek kullanıcıya aşırı, elendi.
- **Orkestratör tutkalı:** ~100 satır FastMCP server (`search(query,k)`) ya da — daha az sürtünme, daha şeffaf — Bash'ten çağrılan düz CLI (`vaultsearch "sorgu"`).
- **Var olan ama arayüzü yanlış hazır uygulamalar:** Khoj, AnythingLLM Desktop, GPT4All LocalDocs, Obsidian Smart Connections — hepsi not üstü yerel RAG, hepsi chat UI için; hiçbiri CLI orkestratörce temiz sorgulanamaz. Elensin diye isimlendirildi.

**Stat kartı:**

| Boyut | Puan | Dayanak |
|---|---|---|
| Erişim kalitesi | 7/10 | Parafraz ve TR↔EN geçişte gerçek, benzersiz kazanç ("drawdown", "düşüş" notlarını bulur); ama exact tanımlayıcıda (MİDAS, `ee16d2d`, "06-11") grep'in altında — ki bu kullanıcının fiili sorgu karışımını domine eder. |
| Kurulum maliyeti | 4/10 | Ollama + model seçimi + chunker + indexer + depo + MCP/CLI tutkalı: her adım kolay, toplamı bir hafta sonu; Windows kâğıt kesikleri (watcher, long-path, GPU sürücüsü) cabası. |
| Bakım sürtünmesi | 3/10 | Sessizce çürüyen ikinci gerçek kaynağı: her edit yeniden-embedding ister, model değişimi tüm vektörleri geçersizler, senkron işi reboot'lardan sağ çıkmalı — tam da kayıtların "ölür" dediği rutin türü. |
| Token verimi | 8/10 | Top-k parçalar kompakt ve çoğu kez konu-üstü; ajan çok daha az okur. Şerh: sessiz ıskalar aşağı akışta token yakar çünkü ajan kendisine gösterilmeyeni bilemez. |
| Açıklanabilirlik | 3/10 | "cosine 0.83" hiçbir şey açıklamaz; bir hatıranın NEDEN gelmediği görülemez — erişim hatası ayıklama = his. |
| Makine maliyeti | 6/10 | İlk embed birkaç dakika (CPU), sorgu ~100ms; ama yerleşik embedding runtime kalıcı 0.5-1.5 GB RAM tutar. |

**Artılar:** kelime ve dil boşluğunu doğal köprüleyen tek mimari; sorgu başına kompakt hedefli bağlam; ajanın uygun maliyetle grep'leyip okuyabileceği ölçeğin ötesine taşır.

**Eksiler:** türetilmiş durumun kalıcı bebek bakıcılığı; sessiz bayatlama ilke #5 altında en kötü olası hata — *kendinden emin şekilde getirilen yanlış bağlam*; kullanıcının fiilen sorduğu exact-entity sorgularında zayıf; opak; ve saf-semantik erişim zaten domine edilmiş tasarım (aşağıda).

---

## Mimari 3 — Hibrit (BM25 + embedding + wiki-link grafiği + reranker)

**Nasıl çalışır.** Aynı parçalar üstünde iki index — exact terimler için SQLite FTS5/BM25, semantik için vektör — paralel sorgulanır, Reciprocal Rank Fusion ile birleştirilir; yerel cross-encoder top-20'yi hassasiyet için yeniden sıralar. Wiki-link graf katmanı (`[[link]]`'lerden ayrıştırılmış düz SQLite kenar tablosu) sonuçları bir sıçrama genişletir — bir kararın komşuları aday kümesine girer. Sonuçlar isabet başına kaynak-kanıtla döner: eşleşen terimler, benzerlik, link yolu.

**Gerçek araçlar:**
- **Hazır: `qmd`** (tobi/qmd, Tobias Lütke — güncelliği doğrulandı) — tam bu iş için CLI arama motoru: tek `index.sqlite`'ta FTS5 BM25 + sqlite-vec, varsayılan EmbeddingGemma-300M, **belgelenmiş çok-dilli seçenek Qwen3-Embedding-0.6B** (Türkçe için doğru tercih), Qwen3-Reranker-0.6B, sorgu-genişletme modeli (~2 GB GGUF, node-llama-cpp), **MCP server (`query`, `get`, `multi_get`, `status`) + Claude Code eklentisi**, ve modelsiz `qmd search` = saf anlık BM25. Node 22+/Bun ister. Windows çalışır (dokümanlar Windows CUDA ayarı içerir) ama araç genç ve macOS-öncelikli.
- **DIY konsolide: LanceDB** — yerli BM25 FTS + vektör + `query_type="hybrid"` + yerleşik **RRFReranker** (varsayılan) ya da **CrossEncoderReranker**, tek gömülü kütüphane, server yok.
- **DIY minimal: yalnız SQLite** — tek `.db`'de FTS5 + sqlite-vec + ~20 satır RRF; qmd'nin kendi deseni.
- **Yerel reranker'lar:** **bge-reranker-v2-m3** (çok-dilli, bge-m3 ile eşleşir; CPU top-20'yi ~1-3 sn), **Qwen3-Reranker-0.6B**. Solo-ölçekte dürüst alternatif: **modeli atla — orkestratör 20 başlık+snippet'i kendisi sıralasın**; sıfır altyapı, birkaç yüz token.
- **Graf katmanı:** `[[wiki-link]]`'leri SQLite kenar tablosuna döken ~60 satır Python; link çözümü zorlaşırsa **obsidian-export** (Rust CLI). Açıkça Neo4j değil — tek kullanıcının markdown'ına graf server'ı malpraktis.
- **Meilisearch** (tek Windows binary, yerel ONNX embedder'la hibrit) var ama admin yüzeyli yerleşik servis — elensin diye isimlendirildi.

**Stat kartı:**

| Boyut | Puan | Dayanak |
|---|---|---|
| Erişim kalitesi | 9/10 | BM25 exact entity/tarihi, dense vektör parafraz ve TR↔EN'i yakalar, link grafiği karar-bağlamı komşularını çeker; RRF+rerank yayınlanmış pratik standardı — tavanı yalnız curation kalitesi çizer. |
| Kurulum maliyeti | 3/10 DIY · 6/10 qmd | DIY: LanceDB iki kolu birleştirse bile üç alt sistem + füzyon + reranker + graf parser + MCP tutkalı; qmd kurulumu tek `npm i -g`'ye indirir ama genç, hızlı-değişen, macOS-öncelikli araca bağlar. |
| Bakım sürtünmesi | 3/10 | Mimari 2'nin çürüyen her şeyi, ARTI iki index'in parça-tutarlılığı, ARTI reranker/model güncelliği; qmd bakıcılığı otomatize eder ama kendisi altında güncellenen bir bağımlılıktır. |
| Token verimi | 9/10 | Üçünün en iyi precision-at-k'sı → en az boşa dosya okuma; sorgu genişletme ajanın kendi yeniden-yazım turlarını da tasarruf eder. |
| Açıklanabilirlik | 6/10 | BM25 kolu ("eşleşen: `VaR`") ve link yolu tam okunur; dense kol ve reranker skorları opak — yarım kara kutu. |
| Makine maliyeti | 4/10 | Kaliteli her sorguda embedder + cross-encoder çıkarımı ve ~2 GB yerleşik model (qmd yığını); modern makinede sorunsuz, ama buradaki en ağırı. |

**Artılar:** nesnel olarak en iyi erişim; sektör-konsensüsü tasarım (embedding ekleyen kimse BM25'i sökmez); qmd bunun bilim-projesi değil tek kurulum olabileceğini kanıtlıyor; kısmi kaynak-kanıt, saf RAG'ın hiç'inden iyi.

**Eksiler:** en çok hareketli parça = en çok çürüme yolu; sürtünmeden kaçan solo kullanıcı için DIY-hibrit, *sistem formunda* özenli-ama-asla-bakılmayan rutinin ta kendisi; ajanın hâlâ okuyarak cevaba yürüyebildiği ölçekte overkill; qmd bağımlılık riski gerçek (1.0-öncesi tempo, Windows ana sahası değil).

---

## Yan yana

| Boyut | M1: Konvansiyon+FTS | M2: Yerel RAG | M3: Hibrit |
|---|---|---|---|
| Erişim kalitesi | 6 | 7 | 9 |
| Kurulum | 9 | 4 | 3 (qmd 6) |
| Bakım | 8 | 3 | 3 |
| Token verimi | 6 | 8 | 9 |
| Açıklanabilirlik | 10 | 3 | 6 |
| Makine maliyeti | 10 | 6 | 4 |

---

## Tavsiye: Mimari 1 şimdi, Mimari 3'e adlandırılmış tripwire'larla. Mimari 2'yi asla kurma.

RAG moda cevap ve burada yanlış cevap. Dört neden, hiçbiri diplomatik değil:

1. **Sorgu karışımı entity-ağır.** Kişisel ops vault'una sorulan: "LOBİ için 06-11'de ne karar verdik", "MİDAS v7 kapsam donması nerede", "PortRisk ilk commit" — tam ad ve tarih; grep'in embedding'i düpedüz yendiği yer. Embedding'in parladığı parafraz sorguları azınlık; frontmatter `aliases:` (önemli ~50 entity'ye TR+EN eşanlam) o boşluğun çoğunu elle kapatır.
2. **Orkestratör zaten semantik katman.** Claude Code bilinçli olarak agentic grep üstüne kuruldu — Anthropic kod tabanlarını embed ETMEMEYİ seçti; sorguyu yeniden yazan, varyant deneyen, link izleyen ajan, sorgulayamadığı statik index'ten iyi performans verir. Buraya vektör DB koymak, ajanın dinamik yaptığını statik ve daha kötü kopyalamak. Doğru yatırım **erişim tarifi/skill**: TR+EN+i-varyant sorgular üret, bağlamlı rg, `[[link]]` yürü, top adayları aç, yol göster.
3. **Hata profilleri asimetrik.** Mimari 1 gürültülü ve editoryal bozulur — ıskalama görünür ve teşhis edilir. RAG sessiz bozulur: bayat ya da kötü-parçalanmış index *kendinden emin yanlış bağlam döndürür* — ilke #5'in kabus senaryosu, ilke #5'in üniformasıyla.
4. **İlke #5 bir curation problemi, indexleme problemi değil.** MOC, alias ve adlandırmaya harcanan saatler her gelecek mimaride bileşik değer; embedding pipeline'ına harcanan saatler terk edildiği gün silinir — ve kayıtlar bakım rutinlerinin terk edildiğini söylüyor.

**Somut minimal inşa (Mimari 1'in tamamı, fazlası değil):** (1) tek sayfalık erişim konvansiyonu dokümanı; (2) iki-dilli eşanlam katmanı olarak `aliases:`'lı frontmatter sözleşmesi; (3) klasör başına `_INDEX.md` MOC + orkestratörün her zaman önce okuduğu kök `KNOWLEDGE-MAP.md` — CLAUDE.md'nin klasör haritasının uzantısı; (4) yukarıdaki erişim skill'i; (5) *opsiyonel* tek-dosya FTS5 index'i (BM25, prefix, `remove_diacritics 2`) — **sıfırdan, talep üzerine, tek komutla ya da git hook'uyla — asla watcher daemon'la**. Bu ölçekte tam yeniden-inşa saniyeler; talep-üzerine-yeniden-inşa, senkron-çürümesi hata sınıfının tamamını yok eden tasarım duruşu.

**Mimari 2'yi varış noktası olarak kalıcı atla.** Embedding ekleyen BM25'i tutmalı; saf-semantik RAG domine edilmiş uç nokta — Hibrit yolunda daha kötü bir ara durak, asla hedef. 1'den tek meşru yükseltme 3'tür.

**3'e yükseltmeyi tetikleyen tripwire'lar** (karar mekanik olsun, ruh hali değil): vault ~15-20k dosyayı aşarsa (örn. chat transkriptleri korpusa katılırsa); ya da 10 erişim görevinden 2'den fazlası >5 dosya açtırıyorsa; ya da alias'ların çözemediği diller-arası ıskalar tekrarlıyorsa. Kaçış kapısı: **qmd + Qwen3-Embedding-0.6B** (tek kurulum, markdown gerçek kaynak kalır, MCP doğrudan Claude Code'a) ya da qmd'nin Windows hikâyesi hayal kırıklığıysa DIY LanceDB hibrit. Mimari 1 için kurulan her konvansiyon 3'e %100 taşınır — pişmanlıksız ilk hamle yapan da bu.

**Bu tavsiyenin dürüst hata modları:**

1. **Recall tavanı gerçek ve görünmez.** Grep string bulur, anlam değil. "Sahtekâr gibi hissettiğimi nerede yazmıştım" notta "impostor" yazıyorsa başarısız — ve *başarısız olduğunu bilmeyecek*; hatıra erişilmez olur. Alias bilinen entity'leri kurtarır; kullandığını unuttuğu kelimeleri kurtaramaz. Embedding'in gerçekten çözdüğü, Mimari 1'in gerçekten çözemediği tek şey bu.
2. **Yokluğu belgelenmiş desenin ta kendisi olan disipline bahse girer.** Konvansiyonlar editoryal ve sessiz çürür — yanlış adlandırılan dosya, atlanan frontmatter hata fırlatmaz; erişim yavaşça kötüleşir ve herkes normalleştirir. Mitigasyon (mevcut git hook'una 20 satır frontmatter lint — sapma hata FIRLATSIN) kendisi de onunla temas edip sağ kalması gereken küçük bir rutin.
3. **"Ajan = semantik katman"ın sayaçlı maliyeti var.** Her erişim ücretli token + duvar-saati yakar, her seferinde, sonsuza dek — yerel index'in sorgu başına marjinal maliyeti ~sıfır. ~15k dosya altında toplam sahip olma maliyetinde ajan kazanır; üstünde bu tavsiye sessizce pahalı seçenek olur. Tripwire'ların yazılı olması tam bu yüzden: bu hata modu yavaş gelir, yavaş gelen hatalar karar tetiklemez.

**Kaynaklar:** tobi/qmd (GitHub) · sqlite-vec releases (v1-öncesi alpha statüsü) · LanceDB Hybrid Search docs (RRFReranker, `query_type="hybrid"`) · Ollama embedding model kıyaslamaları (Qwen3-Embedding, bge-m3, EmbeddingGemma MTEB) · sqlite-vec proje sitesi (Alex Garcia)
