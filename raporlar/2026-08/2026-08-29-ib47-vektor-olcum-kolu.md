# İB-47 — Vektör ölçüm kolu: FTS5 ↔ vektör (e5 · bge-m3) ↔ RRF, aynı 100 altın soru

**AS-OF 2026-08-29 · yan icra oturumu (Fable), partisyon P2 · KB-59 (a) → Karar 66 şartnamesi · Karar 74 M-2 (a) tetik · Karar 60 sırası (hibrit/vektör HÜKMÜ bu ölçümle masaya döner; bu rapor karar VERMEZ) · üretici [tools/erisim-vektor.py](../tools/erisim-vektor.py) (repo `.venv`: sentence-transformers 6.0.0 · torch 2.13.0 · sqlite-vec 0.1.9) · kütük `veri/erisim-eval.jsonl` (+`ndcg10`, `gomme_ms`, `knn_ms`, `sorgu_token`) · gold `veri/gorunum/v_erisim_vektor{,_etki,_gomme}.csv` · deneysel m.29, her rakam kaynaklı**

*Ne bu (ölçüm 2026-08-29):* Şartnamenin 7 maddesi birebir koşuldu: (1) yerel multilingual-e5-large + bge-m3 yan yana (1024d) · (2) sqlite-vec 0.1.9 `vec0` tam brute-force KNN (ANN yok) · (3) RRF sabit k=60, aday 50 · (4) aynı 100 soru (İB-43 seti; 84 cevaplı + 16 çekimserlik), recall@5 / MRR / nDCG@10 dosya düzeyinde + bootstrap %95 GA (n=2.000, tohum 0) · (5) determinizm · (6) maliyet + int8 retention · (7) API gömücü / ANN / LLM-rerank YOK. Korpus: silver `erisim_genisletme ⋈ kayit.metin` (ilk 2.000 karakter), 53.983 kayıt, `kayit_id` sırası, Apple M4 / MPS.

## 1. Sonuç tablosu (n=100, 84 cevaplı; taban = fts5+gen)

| Yöntem (2026-08-29) | recall@5 | MRR | nDCG@10 | ms/sorgu | Δrecall@5 [GA] | ΔnDCG@10 [GA] |
|---|---|---|---|---|---|---|
| fts5 (yalnız metin) | 0,617 | 0,465 | 0,411 | 7,5 | −0,012 [−0,099, +0,086] | −0,022 [−0,095, +0,052] |
| **fts5+gen (taban)** | 0,630 | 0,506 | 0,433 | 7,2 | — | — |
| vektor-e5 | 0,531 | 0,390 | 0,369 | 74 | −0,099 [−0,222, +0,037] | −0,063 [−0,147, +0,020] |
| vektor-bge | 0,605 | 0,429 | 0,396 | 66 | −0,025 [−0,148, +0,099] | −0,037 [−0,119, +0,042] |
| vektor-e5-int8 | 0,556 | 0,396 | 0,367 | 53 | −0,074 [−0,198, +0,062] | −0,066 [−0,149, +0,015] |
| vektor-bge-int8 | 0,617 | 0,423 | 0,397 | 45 | −0,012 [−0,136, +0,111] | −0,036 [−0,117, +0,041] |
| **rrf-e5** | 0,704 | **0,537** | **0,503** | 80 | +0,074 [−0,012, +0,173] | **+0,070 [+0,022, +0,124] ANLAMLI** |
| **rrf-bge** | **0,716** | 0,532 | 0,490 | 76 | +0,086 [+0,000, +0,185] | **+0,057 [+0,006, +0,109] ANLAMLI** |

Okuma (2026-08-29 ölçümü): **vektör tek başına tabanı geçmiyor** (iki modelde de fark negatif, GA 0'ı içeriyor). **RRF (FTS ⊕ vektör) nDCG@10'da anlamlı kazanç** (+0,057…+0,070; GA 0'ı dışlıyor), recall@5'te +0,07…+0,09 (GA sınırda). Modeller arası: bge-m3 tek başına e5'ten iyi (0,605 ↔ 0,531), RRF içinde eşdeğer.

## 2. Yetenek kırılımı (2026-08-29; recall@5 / nDCG@10; n: bilgi-cikarma 23 · cok-oturum 19 · zamansal 19 · bilgi-guncelleme 20)

| Yöntem (2026-08-29) | bilgi-cikarma | cok-oturum | zamansal | bilgi-guncelleme |
|---|---|---|---|---|
| fts5+gen | 0,739 / 0,500 | 0,684 / 0,403 | 0,684 / 0,552 | **0,400** / 0,272 |
| vektor-e5 | 0,826 / 0,529 | 0,526 / 0,364 | 0,526 / 0,419 | 0,200 / 0,144 |
| vektor-bge | 0,783 / 0,521 | 0,632 / 0,351 | 0,579 / 0,499 | 0,400 / 0,196 |
| rrf-e5 | **0,913 / 0,673** | 0,789 / 0,442 | 0,737 / 0,586 | 0,350 / 0,287 |
| rrf-bge | 0,870 / 0,634 | **0,842** / 0,433 | **0,737 / 0,606** | 0,400 / 0,269 |

Okuma: vektörün kazandığı yer **anlam-eşleşmeli tek-olgu soruları** (bilgi-cikarma: 0,83 ↔ 0,74); kaybettiği yer **güncelleme soruları** ("X yerine ne kullanılıyor": eski ve yeni değer aynı anlam uzayında → eski kayıt öne çıkıyor; e5 0,20) ve tarih/oturum bağlı sorular. RRF üç yetenekte en iyi; `bilgi-guncelleme`'de kimse 0,45'i (fts5) geçmiyor — bu sınıf erişim değil **süpersede** problemi (silver `bag`/`v_guncel` yüzeyiyle çözülür, gömmeyle değil).

## 3. Determinizm (şartname 5)
- e5 tam korpus iki BAĞIMSIZ süreçte (ilki sqlite yazımında çöktü, ikincisi tamam) aynı sha256: `21b71148531d…` — 53.983×1024 float32 bit-eşit (MPS).
- `--determinizm` (1.000 kayıt × 2 koşum + 100 sorgu): e5 ve bge bit-eşit, top-10 sıra eşit, maks |Δ| = 0.
- Ön-ölçüm: CPU ve MPS her biri kendi içinde bit-eşit; CPU↔MPS eşitliği ÖLÇÜLMEDİ (farklı makine/sürümde eşitlik beklenmez — taşınabilirlik şerhi; sha256 `gomme_uretim`'de).

## 4. Maliyet (şartname 6; M4, MPS)
- Gömme (indeks kurma): e5 3.530 sn (15,3 kayıt/sn) · bge 3.152 sn (17,1) — ~1 saat/model; disk: sqlite-vec 604 MB + `.npy` önbellek 2×221 MB (hepsi gitignore'lu türev).
- Sorgu: gömme ~50-150 ms (model çağrısı; ilk ölçümde 149 ms, ısınmış 50-60) + KNN float32 ~50 ms / int8 ~16 ms (brute-force 54K×1024) ↔ FTS 7-8 ms. RRF toplam ~80 ms. Sorgu token ort. 19.
- int8 retention: recall@5 e5 1,05× · bge 1,02× (kayıp yok, bu ölçekte küçük kazanç = gürültü); KNN 3× hızlı.
- Çekimserlik ayrımı (cevapsız 16 soru): top-1 kosinüs uzaklığı medyanı e5 0,532 ↔ isabetli cevaplı 0,486; bge 0,901 ↔ 0,801 — eşik kalibresi için ölçüm var, eşik ÖNERİLMİYOR (n küçük).

## 5. Şerhler (m.39)
- 100 sorunun 75'i Carvis-yazımı KESTİRİM (İB-43), Salih teyidi bekler; GA'lar geniş (n=84). Sonuç "RRF anlamlı" hükmü nDCG'de sağlam, recall'da sınırda.
- Bu aracın fts5+gen tabanı 0,630, `erisim-fts.py`'nin kendi eval'inde 0,593: burada ilk 50 aday dosya düzeyinde tekilleştirilip ölçülüyor (aynı metrik kodu tüm yöntemlere; kıyas adil, mutlak değer araçlar arası farklı).
- Korpus metni 2.000 karakterle kesildi (uzun bloklarda kuyruk gömülmedi; max_seq 512 token ayrıca keser).
- Artımlı gömme YOK: HEAD değişince indeks bayatlar (parquet'teki gibi); benimsenirse tazelik bayrağı + değişen-blok gömmesi gerekir.
- Ortam: stdlib-önce ilkesine ikinci istisna (torch ~2 GB + modeller 4,4 GB, `.venv`/HF cache).

## 6. Masaya dönüş (karar Salih'in; Karar 60 sırası)
Sorular: (a) RRF'yi `erisim-fts` yüzeyine ikinci kol olarak almak mı (FTS ana yol; vektör yalnız füzyonda; 80 ms/sorgu) — ölçülü şart önerisi: "nDCG GA 0'ı dışlasın ∧ ≤100 ms" → bugün ikisi de sağlanıyor; (b) hangi model: bge-m3 (öneksiz, tek başına daha iyi) ↔ e5 (RRF içinde eşdeğer); (c) int8'i varsayılan yapmak (kayıp yok, 3× hızlı); (d) `bilgi-guncelleme` sınıfını erişimden değil süpersede yüzeyinden çözmek (bag/v_guncel). Kalan icra: artımlı gömme + tazelik bayrağı (benimsenirse), çekimserlik eşiği (n büyüyünce).
