# Görev Raporu — Ingest + Indexleme Fabrika Hattı

**Ajan:** araştırma-2 (ingest pipeline) · **Tarih:** 2026-07-10 · **Statü:** rapor — karar içermez · **Tüketen:** `02_KNOWLEDGE_INDEX_PLAN.md`

**Makine gerçekliği (2026-07-10 doğrulandı):** Python 3.11.5 PATH'te; gömülü SQLite 3.42.0 **FTS5 etkin** (BM25 yerleşik, ek kurulum sıfır). Minimal yığın — `sqlite3` + FTS5 + `sqlite-vec` + `sentence-transformers` — tek `pip install` uzaklıkta, server'sız, tek .db. Korpus keşfi: gerçek dokümanlar heading-zengin (tipik 5-26 başlık; korpus dökümlerinde 120'ye dek) → heading-duyarlı chunking'in tutunacağı yapı var; ve workspace hâlihazırda bir tuzak içeriyor — `portrisk/.venv` düzinelerce çöp .md katkılıyor (numpy LICENSE'ları, vendored dokümanlar); naif `**/*.md` glob'u bunları yutar. Gümrük Kapısı hipotetik değil.

## 0. Tasarım değişmezleri (pazarlıksız; geri kalan her şey ayarlanabilir)

1. **Dosyalar kanonik, index atılabilir önbellek.** Bilgi yalnız .md'de yaşar (mümkünse git'li). Index (SQLite) silinip tek komutla dosyalardan deterministik yeniden kurulabilir. Bulutsuz/tek-kopya kabul edilmiş riskin yedek hikâyesi budur: index bozulması saat kaybettirir, bilgi asla.
2. **Yakalama sıfır-karar; kararlar batch ve asenkron koşar.** Yakalama anında Salih'ten madde-başına hüküm isteyen her istasyon 2. haftada ölür. Tüm insan hükmü örneklenmiş, zamanlanmış, sınırlı ("Pazar 10 karantina maddesi gözden geçir"), asla satır-içi değil.
3. **Her düğmenin yazılı testi var** (#7 bilimsel ingest). Ölçüm aleti tek **altın soru seti**: Salih'in gerçekten soracağı 20→50 soru ("MIDAS v7 kaç enstrüman?", "negatif ağırlık kontrolü hangi satırdı?"), her biri kaynak dosya/başlığına eşlenmiş. Kapı eşiği, chunk boyutu, dedup kesimi, yoğunluk dizi, decay yarı-ömrü — hepsi bu tek sete karşı ayarlanır. /goal B-koşulu mantığının aynısı: done-kontrolünü yazamıyorsan loop kuramazsın.
4. **İki-dillilik birinci sınıf kısıt.** Aynı fikir vault'larda bir TR bir EN var. Sözcüksel yöntemler (BM25, MinHash) burada ya dil-körü ya dil-kırık (Türkçe eklemelilik stemming'i bozar; diller-arası eşleşme sözcüksel olarak imkânsız). Her istasyona semantik (embedding) bacak gerekir; model çok-dilli olmalı (BGE-M3 ya da multilingual-e5 sınıfı).

## 1. İstasyon 1 — GÜMRÜK KAPISI (yakalama + filtre)

**Somut yöntem.** Manifest/hash diff'i yeni-veya-değişmiş dosyaları keşfeder; **ingest skorlayıcı** her adaya kabul skoru ve **tier** atar; her hüküm append-only **kapı defterine** yazılır (dosya başına satır: yol, skor, tier, gerekçe). Hiçbir şey sessizce düşmez — ret bir defter satırıdır, silme değil. İlk savunma hattı aptal **hariç-tutma listesi** (`.venv/`, `node_modules/`, `.git/`, `LICENSE*`, vendored) — keşif bunun tek başına Homebase'de ~40 çöp dosyayı temizlediğini gösteriyor.

**Kabul skoru (matematik, #7):** Generative-agents bellek modeli (Park et al. 2023: erişim = recency + importance + relevance; importance LLM 1-10) + marjinal-bilgi düşüncesinden uyarlama:

```
I = 0.4·novelty + 0.4·importance + 0.2·provenance      (her terim ∈ [0,1])

novelty     = 1 − max_cosine(doküman özü embedding'i, mevcut index)
importance  = LLM 1-10 / 10, sınıf-başına rubrik (proje kararı=9, kırpılmış
              jenerik makale=3), ucuz model, batch
provenance  = kaynak önseli: Salih'in kendi sözü 1.0 > Salih'li chat 0.7 >
              derlenmiş makale 0.5 > ham oto-transkript 0.3
```

**İstasyonun kilit kararı: kapı VARLIĞA mı DERİNLİĞE mi karar verir?** Tavsiye: **derinlik** — kapı fedai değil derece vanası; solo operatör gelecekteki alaka ihtiyacını öngöremez:
- **Tier 1 (I ≥ 0.6):** tam işlem — extract, chunk, embed, QC, link.
- **Tier 2 (0.3 ≤ I < 0.6):** sığ index — başlık + 2 satır öz + yol embed edilir; gövde chunk'lanmaz. Bulunur, ucuz, sonradan yükseltilebilir.
- **Tier 3 (I < 0.3):** yalnız defter satırı (yol + başlık). Maliyeti bir satır.

**Test edilebilir eşik protokolü:** aylık, 30 Tier-2/3 maddesi örnekle: "bu ay herhangi bir altın-set (ya da gerçek) soru buna ihtiyaç duydu mu?" = **pişmanlık oranı**; hedef < %5. Pişmanlık > %5 → θ_hi düşür. Tier-1 hacmi QC'nin boşaltabildiğinden hızlı büyüyor → yükselt. İki hata yönü de ölçülebilir → θ ampirik, his değil.

**Seçenekler:**

| Seçenek | Mekanizma | Artı | Eksi |
|---|---|---|---|
| A. Her şeyi indexle, erişimde filtrele | Kapı yok; sıralamaya güven | Sıfır karar, sıfır pişmanlık | Distractor kirliliği gerçek: top-k'daki yakın-alakalı çöp cevabı ölçülebilir bozar (Cuconasu et al. 2024, "The Power of Noise"); embedding maliyeti çöple ölçeklenir; .venv vakası taban gerektiğini gösterdi |
| B. Skor-kapılı tiering (tavsiye) | Yukarıdaki formül, batch LLM skorlama | Geri-alınabilir, ucuz, ölçülebilir pişmanlık | LLM importance 1-puan seviyesinde gürültülü/kayar; dürüst kalmak için aylık denetim şart |
| C. Yakalamada insan etiketi | Salih madde başına önem işaretler | Teoride en yüksek hassasiyet | **2. haftada ölür.** Bu workspace'te bilinen desen: her elle madde-başı ritüel (retype, elle reindex) ya reddedildi ya çürüdü; yalnız batch/zamanlanmış ritüeller yaşıyor |

**Gerçekten kırıldığı yer (refutation).** (1) Satır-içi karar → C'nin ölümü, kapsandı. (2) İncesi: sessizce yanlış-skorlayan kapı *güveni* öldürür — Salih kaydettiğini hatırladığı şeyi arayıp index "yok" dediği ilk an erişime güveni biter, grep'e döner. Mitigasyonlar yapısal: Tier-3 maddeler başlık/dosya-adından hep bulunur (asla sıfır-index), ve kapı defterinin kendisi aranabilir ("X dosyası görüldü mü? hangi tier? neden?"). Görünür defteri olmayan kapı, ilk yanlış-negatifinden sonra terk edilen kapıdır.

## 2. İstasyon 2 — İŞÇİLER (extract + chunk)

**Somut yöntem.** İki işçi tipi, kapı tier'ına eşli:
- **Mekanik chunker (tüm Tier-1, sıfır LLM maliyeti):** markdown-yapı-duyarlı bölme (aşağıda).
- **LLM extractor (yalnız Tier-1, batch):** "bilgi paketleri" üretir — yoğun/karar-ağır dokümanlarda atomik özütler (Chen et al. 2024, "Dense X Retrieval": önerme-düzeyi erişim birimleri QA'de cümle/pasajı yener); her paket = iddia + kaynak çapası + tarih + sınıf.

**Chunking tavsiyesi: heading-duyarlı, token-sınırlı, breadcrumb enjeksiyonlu.**
1. Başlıklardan böl (korpus heading-zengin — yazarlar anlam sınırlarını zaten çizmiş).
2. Küçük kardeş bölümleri 200-500 token'a dek yukarı birleştir; aşırı büyük bölümleri paragraf/cümle sınırında ~%15 örtüşmeyle sert-böl.
3. **Embedding'ten önce her chunk'a breadcrumb öne-ekle:** `dosya başlığı > H1 > H2 + tek satır dosya özü`. Anthropic contextual retrieval'ın (2024: bağlam-önekli chunk'lar top-20 erişim hatasını ~%49, reranking'le ~%67 azaltır) ucuz versiyonu; chunk-başına LLM-yazımı tam bağlam cümlesi Tier-1-özel yükseltme, varsayılan değil.
4. **Yapısız dosyalar için geri-düşüş** (ham YouTube/chat transkriptleri): ~350 token'da özyinelemeli paragraf/cümle bölmesi. Bu geri-düşüş olmadan heading-duyarlı chunking transkriptlerde 8.000 token'lık tek "chunk" döndürür ve hat sessizce bozulur.

**Adlandırılmış tradeoff:** heading-duyarlı, yazar-çizimi anlam sınırlarını korur ve *atıflanabilir çapa* verir (`dosya#başlık` — wiki-linklerin tam ihtiyacı), ama chunk boyu varyansı yüksek (2 satırlık güdük bölümler; duvar-metinler) ve yapısız girdide düpedüz başarısız — bu yüzden birleştirme kuralları + geri-düşüş. Varsayılan olarak reddedilen alternatifler: **sabit-boy** (tekdüze ve basit, ama düşünce ortasından böler ve insana-anlamlı hiçbir şeye atıf vermez) ve **semantik/embedding-sınırlı chunking** (Chroma 2024 değerlendirmesi: kazançları iyi özyinelemeli bölmeye göre maliyetine değmeyecek kadar mütevazı; yalnız altın set transkript sorularının düştüğünü gösterirse yeniden değerlendir).

**İstasyonun kilit kararı: chunk temsili — ham dilimler mi LLM-damıtık paketler mi?**

| Seçenek | Artı | Eksi |
|---|---|---|
| A. Yalnız ham chunk | Bedava, hızlı, inşaen sadık | Ayrıntılı erişim; bağlam penceresi dolgu ile şişer (#28 ihlali) |
| B. Yalnız LLM paket | Maksimum yoğunluk, atomik atıf | Maliyet × binlerce dosya; ölçekte halüsinasyon riski; tam-korpus LLM geçişi bitmeyen çok-günlük iş |
| C. İkisi, tier'lı (tavsiye) | Ham chunk Tier-1'in tamamına; paket yalnız yüksek skorlulara; paket→ham chunk linki saklanır | Senkron tutulacak iki temsil (supersede kuralları gerek) |

**Gerçekten kırıldığı yer (refutation).** Backlog maliyeti. Baştan çıkarıcı plan "tüm backlog'u LLM-extract et" — binlerce dosya × extraction + QC = günlerce runtime ve gerçek para; solo operatör bitiş çizgisi görünmeyen göçü terk eder. Kırılmayı kır: mekanik chunking ~bedava ve %100'ü hemen kapsar (erişim 1. günden çalışır); LLM paket çıkarımı **talep-üzerine ve ileri-yönlü** — yeni Tier-1 ingest paket alır, backlog o dokümandan bir ham chunk fiilen erişildiği İLK anda tembelce yükseltilir ("ilk dokunuşta terfi"). İkinci kırılma: Obsidian sözdizimi — `[[wiki-link]]`, frontmatter, callout — ayrıştırılmalı, gürültü sayılmamalı; `[[...]]`'ü söken chunker, İstasyon 4'ün ihtiyaç duyduğu bağ verisinin ta kendisini imha eder.

## 3. İstasyon 3 — KATI KALİTE KONTROL (dedup + kalite kapısı + ret/yeniden-yap)

**Somut yöntem.** Her paket/chunk kütüphaneye girmeden iki-parçalı muayene: **mekanik kontroller** (şema: kaynak çapası var, tarih var, sınıf var; uzunluk sınırları; dil etiketi) ve **model kontrolleri** (sadakat + kopya). Hükümler: KABUL / **RET + gerekçe → İşçiye geri** (en çok 2 yeniden-yapım turu) / KARANTİNA (Pazar 10-dakikalık insan geçişi için dead-letter kuyruğu). Evaluator yalnız işçi *teslim ettiğinde* bakar — 07-07 dersinin düzeltilmiş /goal semantiği (evaluator her turda değil, done iddiasında kontrol eder); yeniden-yapım tavanı = "veya 15 turdan sonra dur" dersi: sınırdaki pakette tavansız ret döngüsü sonsuza dek token yakar.

**Dedup — çift-özüt problemi.** Çift-çıkarım problemi bu workspace'te belgeli (07-04 "günlük çift-özüt temizliği") → **etiketli kalibrasyon verisi zaten var**: elle birleştirilen çiftler = pozitif örnekler; birleştirilmeyen komşuları = negatifler. Kullan. Yerel tespit kaskadı, ucuz→pahalı:
1. **Normalize et:** Unicode NFC, boşluk/noktalama sıkıştır, küçük harf. Türkçe aksanları SOYMA (ş/s, ı/i anlam taşır).
2. **Exact dup:** normalize metnin SHA-256'sı. Bedava.
3. **Sözcüksel yakın-dup:** **karakter 5-gram** shingle üstünde MinHash + LSH (Broder 1997; ölçekte Manku et al. 2007 deseni). Kelime değil karakter shingle — Türkçe eklemelilikte "aynı" kelime nadiren aynen tekrarlar (`portföyümdeki` vs `portföyün`); char n-gram bunu emer. Jaccard ≥ 0.7 → aday çift. `datasketch` bunu yerelde milisaniyelerde koşar.
4. **Semantik yakın-dup:** embedding cosine — *aynı fikir farklı kelimeler* ve *aynı fikir farklı dil* (TR özüt vs EN özüt) yakalayan tek katman. MinHash ikisine de yapısal kör.
5. **Çözüm:** cosine ≥ 0.95 VE aynı kaynak sınıfı → oto-birleştir (yenisi supersede eder, link kalır); 0.88-0.95 → LLM hüküm kuyruğu (birleştir / tut-ve-ilişkili-linkle / ayrı); hükümler loglanır.

**Kalibrasyon protokolü (test edilebilir, kendi verisiyle):** temizlik tarihçesinden ~50 bilinen-birleşik çift + 50 yakın-komşu non-dup → cosine eşiğini tara → max-F1 seç. Dedup kesimi blog-varsayılanı değil, *onun* korpusunun ve *onun* embedding modelinin ölçülmüş özelliği olur.

**İstasyonun kilit kararı: hakim kim?**

| Seçenek | Artı | Eksi |
|---|---|---|
| A. Yalnız kurallar (şema+hash+MinHash) | Deterministik, bedava, asla halüsinasyon | Parafraz kopyaları ve sadakat hatalarını tamamen kaçırır |
| B. Her şeyde LLM-hakim | Semantiği yakalar; RAGAS-stili sadakat skoru (Es et al. 2023) | Maliyet; bilinen hakim yanlılıkları — laf kalabalığı tercihi, hakim=işçi modelse kendi-kendine-onay (Zheng et al. 2023) → hakim, extract edenden FARKLI model sınıfı olmalı |
| C. Önce kurallar, LLM yalnız işaretli/örneklenmişte (tavsiye) | QC'nin %90'ı bedava; LLM bütçesi sinyalin olduğu yere | Bayrakların altında bir ıskalama oranı var; altın setle izle, kabul et |

**Gerçekten kırıldığı yer (refutation).** QC katılığı sessiz-backlog makinesidir: sadakat çıtasını fazla yükselt, reddedilen paketler kimsenin bakmadığı karantinada yığılır — fabrika "çalışır", kütüphane açlıktan ölür, Salih son bilginin hiç gelmediğini haftalar sonra fark eder. İki sert kural: karantinanın **erişim anında görünen sayacı** ("bu konuda 7 madde QC bekliyor"), ve karantina > 25 madde → yeniden-yapım politikası **oto-gevşer**: blokla değil, uyarı-etiketiyle-kabul et (etiketli vasat paket, görünmez paketten iyidir — insan geçişi hâlâ düzeltebilir). İkinci kırılma: solo = ikinci insan yok — tüm insan QC'si haftalık 10 dakikalık *örneklem*, asla kuyruk-boşaltma görevi; yoksa yine 2.-hafta ölüm ritüeli.

## 4. İstasyon 4 — YAŞAYAN KÜTÜPHANE (depo, linkler, erişim, tazelik)

**Somut yöntem.** Tek SQLite dosyası: `chunks` tablosu (metin, breadcrumb, sınıf, tarihler, tier, importance) + FTS5 sanal tablo (BM25 — mevcut olduğu doğrulandı) + `sqlite-vec` tablo (embeddingler) + `links` tablosu (tipli kenarlar: `related`, `supersedes`, `extracted-from`). Markdown kanonik kalır; .db türetilmiş ve yeniden-kurulabilir (değişmez 1).

**Raf değil bağ.** Wiki-linkler üç kaynaktan hasat edilir: (a) markdown'daki açık `[[link]]`'ler (otoriter), (b) oto-önerilen kenarlar = benzerlik tabanının üstündeki top-3 en yakın komşu — yüksek tabanın üstünde oto-kabul, aksi halde `suggested` olarak yazılır (erişimde görünür, terfi edilebilir), (c) QC dedup çözümünden `supersedes` kenarları. Erişim **1-sıçrama komşu genişletmesi** yapar: isabet, en güçlü bağlarını aday kümesine sürükler. Graf erişiminin pratik değerinin çoğunu, makinesinin ~%1'iyle verir.

**Erişim montajı (#15 somut):** sorgu → FTS5 BM25 bacağı + vektör bacağı paralel → **Reciprocal Rank Fusion** (Cormack et al. 2009 — gürbüz, parametre-hafif, skor normalizasyonu derdi yok) → ~24 aday → final sıralama = `RRF × decay(sınıf, yaş) × (0.5 + 0.5·importance)` → breadcrumb'lı + `as_of` tarihli top 5-8 chunk. Diller-arası not: BM25 bacağı TR sorgu → EN dokümanı eşleyemez; çok-dilli dense bacak kapatır. Altın-set diller-arası sorular düşük kalırsa ucuz güçlendirici: BM25 sorgusunu iki dilde de üret (tek LLM çeviri çağrısı). Opsiyonel Faz-4 yükseltmesi: cross-encoder reranker (bge-reranker-v2-m3) — yalnız ölçülmüş isabet oranı gerektirirse.

**Tazelik/decay — üç ayrı mekanizma, çünkü "bayat" üç farklı şey demek:**
1. **Senkron bayatlığı (index ≠ dosyalar):** içerik-hash manifest diff'i, her gece. Düzenlenen → yeniden chunk/embed; silinen → mezar taşı. Bu, doğal **ilk Routine** (loop-eng Faz 4: "ben yokken çalış") — gecelik ingest koşusu, yol haritasının aradığı zamanlanmış-loop kullanım vakasının TA KENDİSİ. Elle "reindex" komutları tüm elle ritüeller gibi ölür; zamanlanmış değilse yok demektir.
2. **Sıralama bayatlığı (eski ≠ yanlış ama eski fazla yüksek sıralanıyor):** *son-erişim* zamanında üstel decay, generative-agents stili (Park et al. 2023 tick-başına recency decay; üstel form Ebbinghaus 1885; erişimin saati tazelemesi Bjork & Bjork 1992'nin retrieval-strength/storage-strength ayrımının aynası — dokunulan hatıra yeniden güçlenir). Sınıf-başına yarı-ömür: piyasa/haber 14g, proje-durumu 45g, kavram/matematik ∞ (λ=0). **Taban 0.2: decay yeniden sıralar, asla gömmez.** Hiçbir şey salt yaşla bulunmaz olmaz.
3. **Semantik bayatlık (bilgi supersede edildi):** decay, v6'nın "12 enstrüman"ının *yanlış* olduğunu bilemez, yalnız eski olduğunu bilir — bayat-ama-alakalı paket sıralamayı yine kazanır. Doğruluğu yalnız **supersede kenarları** düzeltir: erişim `superseded` chunk'ları varsayılan filtreler ve işaretçi döndürür ("v7, v6'yı supersede eder"). Tespit neredeyse bedava: kapının novelty kontrolü ingest'te en yakın komşuları zaten hesaplıyor → "yeni paket komşuyu çelişiyor/güncelliyor → supersede kenarı öner" zaten yapılmış hesaba biner. MIDAS v5→v6→v7 zinciri canlı test vakası: "kaç enstrüman?" altın sorusuna v6 sayısıyla cevap = otomatik test hatası.

**İstasyonun kilit kararı: graf ne kadar ağır?**

| Seçenek | Artı | Eksi |
|---|---|---|
| A. Düz index, link yok | En basit | "Ölü raflar" — vizyonu açıkça ihlal; ilişkili bilgi asla birlikte gelmez |
| B. Hafif tipli kenarlar + 1-sıçrama genişletme (tavsiye) | Graf değerinin %80'i; kenarlar supersede/doğruluk makinesi olarak çift görev | Oto-önerilen kenarlara eşik şart, yoksa her şeyin her şeye bağlandığı yumak (yumak, bilgisel olarak link-yokluğuyla özdeş) |
| C. Tam GraphRAG (entity çıkarımı, topluluk özetleri — Edge et al. 2024) | Korpus-küresel "temaları özetle" sorularında gerçekten iyi | Ağır LLM index maliyeti, QC'lenecek koca ek hat; solo kişisel index'te bakım öldürür. Yalnız altın set düz erişimin düştüğü küresel sorular biriktirirse yeniden aç |

**Gerçekten kırıldığı yer (refutation).** İhmalle-ıraksama: Salih markdown'ı her gün düzenler; senkron gözetimsiz gecelik iş değilse index ile gerçeklik bir haftada ayrışır, erişim edit-öncesi metin döndürmeye başlar, güven ölür (İstasyon 1'deki güven-ölümünün aynısı, farklı kapıdan). İkinci kırılma: tek-kopya riski — bulut yok demek, index-bozulması olayı (ani kapanmada SQLite, disk hıçkırığı) yalnız yeniden-kurulum zamanına mal olmalı; değişmez 1'in bilgiyi yalnız index'te saklamayı yasaklaması tam bu yüzden. Üçüncü: tabansız oto-link yumak üretir; link-önerme eşiği ayarlanan düğme (başlangıç: öner ≥ 0.75, oto-kabul ≥ 0.88), sabit değil.

## 5. Bağlam-yoğunluğu protokolü (#28) — dizi ölçmek

Yoğunluk tüketici sınıfı başına ayarlanabilir, sabit değil. Somut, tek-öğleden-sonralık deney:
1. **Malzeme:** 12 temsilî doküman — {kendi notları, chat logları, makaleler, transkriptler}ten 3'er.
2. **Yer gerçeği:** her ORİJİNALDEN 6 soru (2 olgusal, 2 ilişkisel, 2 "neden"), cevaplar orijinale anahtarlı.
3. **Yoğunluk merdiveni:** doküman başına 4 sürüm — ham (D=1×), hafif özet (~3×), yoğun özet (~6×), telgrafik önermeler (~12×). D = kaynak_token / sürüm_token; istenirse yoğunluk metriği olarak 100-token-başına-önerme de (LLM çıkarımıyla sayılabilir → his değil ölçüm).
4. **Anlama testi:** her (sürüm × model-sınıfı) 6 soruyu YALNIZ o sürüm bağlamdayken cevaplar. En az iki sınıf: zayıf/yerel (Haiku-sınıfı) ve güçlü (Opus-sınıfı). Yer gerçeğine karşı puanla (rubrikli LLM-puanlama; %20 elle nokta-kontrol).
5. **Diz:** sınıf başına doğruluk-D eğrisi; **D\* = doğruluğun D=1 taban çizgisinin ≥ %90'ında kaldığı en yüksek yoğunluk.** Sınıf-bağımlılık hipotezine göre beklenen şekil: güçlü modeller doğruluğu çok daha yüksek D'ye taşır (LLMLingua, Jiang et al. 2023: küçük kayıpla çok-katlı prompt sıkıştırma — tolerans model/görev-bağımlı); zayıf modeller erken uçurumdan düşer. Eğriler sınıfa göre AYRIŞMAZSA bu da bulgudur: tek yoğunluk yeter ve sınıf-routing makinesi gereksiz — deney kendi özelliğini öldürebilir; bilimsel yapan da bu.
6. **Devreye alma:** yoğunluk bütçe tablosu {tüketici sınıfı → D\*} İşçi özetleyici prompt'unu besler ("~D\*× sıkıştır"). Tier-1 dokümanlar **iki yoğunluk** saklar (ham chunk + yoğun paket); erişim tüketici sınıfına göre servis eder. Maliyet: 12 × 4 × 6 × 2 ≈ 576 puanlı cevap — batch iş, proje değil.

**Refutation:** protokol, 12 doküman temsilî değilse kırılır (gym logunun yoğunluk dizi ≠ MIDAS tezinin — bu yüzden sınıfa göre katmanla) ve elle "aklıma gelince" yeniden koşulursa (koşulmaz) — yeniden-koşuyu takvime değil tetikleyiciye bağla: yalnız tüketici model sınıfı değişince.

## 6. Eşik tablosu (tüm düğmeler, varsayılanlar, testleri)

| Düğme | Başlangıç | Dayanak | Ayarlayan test |
|---|---|---|---|
| Kapı θ_hi / θ_lo | 0.6 / 0.3 | Park et al. 2023 kabul deseni | Aylık pişmanlık denetimi < %5 (30 örnek) |
| Novelty terimi | 1 − max cosine | Marjinal bilgi | Tier-3 hariçken altın-set recall değişmiyor |
| Chunk boyutu | 200-500 tok, %15 örtüşme | Chroma 2024 aralığı; Dense-X granülerlik | 250/350/500'de altın-set hit@5 taraması |
| Breadcrumb | Hep açık | Anthropic contextual retrieval (−%49 hata) | Altın sette A/B, 1 akşam |
| Dedup: exact | SHA-256 normalize | — | Gerekmez |
| Dedup: MinHash | char 5-gram, Jaccard ≥ 0.7 bayrak | Broder 1997; TR morfolojisi için char-gram | Etiketli çift-özüt çiftlerinde precision |
| Dedup: cosine | oto ≥ 0.95, inceleme 0.88-0.95 | — | ~100 etiketli çiftte max-F1 taraması |
| QC yeniden-yapım tavanı | 2, sonra karantina | /goal tur-limiti dersi | Karantina giriş hızı |
| Karantina supabı | > 25 madde → etiketle-kabul | Solo backlog ölümü | Haftalık sayım |
| Decay yarı-ömürleri | piyasa 14g / proje 45g / kavram ∞; taban 0.2 | Ebbinghaus formu; Bjork tazeleme | Tarihli cevaplı altın sorular (v6 vs v7) |
| Link öner / oto-kabul | ≥ 0.75 / ≥ 0.88 | Anti-yumak tabanı | Düğüm-başına kenar dağılımı (medyan 2-4, 20 değil) |
| Yoğunluk D\* sınıf-başına | ölç; beklenti ~3× zayıf / ~6× güçlü | LLMLingua sınıf-bağımlılığı | §5 diz protokolü |
| Erişim | Hibrit BM25+vektör, RRF, k=24→top 5-8 | Cormack 2009; hibrit > tek bacak | Tek-bacak ablasyona karşı altın-set hit@5 |

## 7. Fazlı rollout — önce en küçük yaşayabilir index

Her faz yazılı DONE + öldürme-kriterli tek kanıtlanabilir loop; önceki DONE yeşil olmadan sonraki başlamaz.

**Faz 0 — Kanıt Dilimi.** Kapsam: yalnız Homebase — `01 Daily Logs` + kök `[C]` wiki sayfaları (~60-100 dosya), hariç-tutma listesi aktif (.venv!). İnşa: heading-chunker + çok-dilli embedding (bge-m3; CPU zorlanırsa multilingual-e5-small) + SQLite (FTS5 + sqlite-vec) + hibrit RRF + **20 soruluk altın set**. Kapı yok (hepsini indexle — korpus küçük), QC yok, yoğunluk işi yok. **DONE:** altın sette hit@5 ≥ %80 VE bellek/grep'in bulamadığı ≥ 1 gerçek soru erişimden cevaplandı. **Öldürme kriteri:** chunk-boyu taramasından sonra hit@5 < %60 → embedding modeli Türkçede başarısız; üstüne bir şey kurmadan model değiştir. Efor: 1-2 oturum.

**Faz 1 — Kapı + ayna.** Ekle: hash-manifest artımlı senkron **gecelik Routine** olarak (= loop-eng Faz 4'ün ilk gerçek routine'i), kapı skorlama + 3-tier defter, ingest'te exact + MinHash dedup. Kapsamı Benlik'e genişlet. **DONE:** 14 ardışık gün gözetimsiz edit→index gecikmesi < 24s; yeni ingest'te kopya oranı < %2; kapı defteri herhangi bir dosya için "görüldü mü, hangi tier, neden" cevaplıyor.

**Faz 2 — QC + çift-özüt infazı.** Ekle: etiketli temizlik çiftleriyle kalibre semantik dedup; QC evaluator (mekanik + örneklenmiş LLM sadakati); ret/yeniden-yap (tavan 2) + karantina + supap. **DONE:** etiketli sette dedup F1 ≥ 0.9; karantina incelemesinin < 10 dakika sürdüğü bir tam hafta.

**Faz 3 — Yoğunluk + sınıf routing (#28).** §5 diz deneyini koş; Tier-1'e çift yoğunluk; sınıfa göre servis. **DONE:** ölçülmüş yoğunluk tablosu var; yoğun paketler D\*'da ≥ %90 anlama tutuyor; eğriler ayrışmazsa bulguyu kaydet ve routing'i ATLA (negatif sonuç = ucuza öldürülmüş özellik).

**Faz 4 — Tam yaşayan kütüphane.** Tam korpus (Yasam-Arsivi, Demirtas-Finans, ham exportlar); supersede kenarları + decay sıralaması canlı; link önerileri + 1-sıçrama genişletme; reranker yalnız altın-set sayıları gerektirirse. **DONE:** altın set 50 soruya büyümüş, hit@5 ≥ %85; MIDAS sürüm-tuzağı sorusu v7 döndürüyor, v6 değil; aylık kapı-pişmanlığı < %5.

## 8. Literatür indeksi (tek satırlık; hepsi yukarıda yük taşıyor)

- **Park et al. 2023, Generative Agents** — bellek erişimi = recency × importance × relevance; LLM 1-10 importance; üstel recency decay. Kapı skoru + erişim sıralamasının temeli.
- **Ebbinghaus 1885** (üstel unutma) + **Bjork & Bjork 1992** (retrieval vs storage strength; erişim yeniden güçlendirir) — tabanlı son-erişim decay'i.
- **Anthropic, Contextual Retrieval (2024)** — bağlam-önekli chunk: top-20 erişim hatası ~−%49, reranking'le ~−%67. Breadcrumb enjeksiyonunun temeli.
- **Chen et al. 2024, Dense X Retrieval** — erişim birimi olarak önermeler cümle/pasajı yener. Tier-1 paketlerin temeli.
- **Liu et al. 2023/24, Lost in the Middle** — uzun tıkış bağlam bozar; 30 değil 5-8 yoğun chunk döndür.
- **Cuconasu et al. 2024, The Power of Noise** — yakın-alakalı distraktörler QA'yi bozar; kapı + dedup'un gerekçesi.
- **Chroma Research 2024, chunking değerlendirmesi** — semantik chunking kazancı iyi yapısal bölmeye göre mütevazı; heading-duyarlı varsayılanın gerekçesi.
- **Broder 1997 (MinHash)**, **Manku et al. 2007** — sözcüksel yakın-dup katmanı.
- **Cormack et al. 2009, Reciprocal Rank Fusion** — skor normalizasyonsuz hibrit füzyon.
- **Es et al. 2023, RAGAS** — QC hakimi için sadakat/alaka metrikleri; **Zheng et al. 2023** — LLM-hakim yanlılıkları (laf kalabalığı, kendine-onay) → hakim ≠ işçi modeli.
- **Jiang et al. 2023, LLMLingua** — küçük kayıpla çok-katlı sıkıştırma, tolerans model-bağımlı → sınıf-bağımlı yoğunluğun (#28) ampirik temeli.
- **Packer et al. 2023, MemGPT** — katmanlı bellek (sıcak bağlam vs dış depo) → Tier-1/2/3 derinlik tasarımının aynası.
- **Edge et al. 2024, GraphRAG** — ağır graf seçeneği; adlandırıldı ve bilinçli ertelendi.
- **BGE-M3 (BAAI 2024) / multilingual-e5 (Wang et al. 2024)** — TR↔EN erişimi ve diller-arası dedup'u yerelde mümkün kılan çok-dilli embedding modelleri.
