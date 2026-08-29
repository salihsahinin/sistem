# İB-43 kalanı — Erişim katmanı kalibrasyonu: genişletme ağırlığı · güncel-yüzey yönlendirmesi · çekimserlik eşiği

**AS-OF 2026-08-29 (ölçüm 19:02) · yan icra oturumu (Fable), P8 · KB-43 (a) / Karar 60 sırası · araç [tools/erisim-kalibrasyon.py](../tools/erisim-kalibrasyon.py) (stdlib, **LLM YOK** — Salih 08-29 model-düşümü önlemi: sonuçlar yalnız SQLite/kütükten; ayrıca `switchModelsOnFlag: false` teyit) · gold `v_erisim_kalibrasyon.csv`, `v_erisim_cekimserlik.csv` · kütük `veri/erisim-kalibrasyon.jsonl` · deneysel m.29**

*Ne bu (2026-08-29):* İB-43'ün üç kalan ölçümü. "gen" = `fts5+gen` = kural-tabanlı anahtar GENİŞLETME kolonu (referans değerleri + tarih; bm25 ikinci kolon), model/üretim terimi değil. 100 altın soru (İB-43; 84 cevaplı), ilk 50 aday dosya düzeyinde, aynı metrik kodu (erisim-vektor `metrik`).

## 1. Genişletme ağırlığı (w) × yüzey — grid 7 × 3 (ölçüm 2026-08-29; TÜMÜ recall@5 / nDCG@10)

| w | yüzeysiz | +güncel (sabit) | +auto (soruya bağlı) |
|---|---|---|---|
| 0 | 0,605 / 0,419 | 0,630 / 0,457 | — |
| **0,5** | **0,630 / 0,452** | 0,630 / 0,467 | **0,654 / 0,468** |
| 1 | 0,642 / 0,441 | 0,617 / 0,459 | 0,667 / 0,456 |
| 1,5 | 0,630 / 0,436 | 0,630 / 0,450 | — |
| **2 (eski varsayılan)** | **0,630 / 0,433** | 0,617 / 0,447 | 0,642 / 0,448 |
| 3 | 0,630 / 0,429 | 0,593 / 0,445 | — |
| 4 | 0,605 / 0,424 | 0,593 / 0,446 | — |

Yetenek kırılımı (2026-08-29; recall@5 / nDCG@10):

| Ayar | bilgi-cikarma | cok-oturum | zamansal | bilgi-guncelleme |
|---|---|---|---|---|
| gen=2 (eski) | 0,739 / 0,500 | 0,684 / 0,403 | 0,684 / 0,552 | 0,400 / 0,272 |
| gen=0,5 | ≈ | ≈ | ≈ | 0,450 / — |
| gen=2+güncel (sabit) | 0,739 / 0,552 | **0,421** / 0,290 | 0,579 / 0,453 | **0,700** / 0,470 |
| **gen=0,5+auto** | 0,696 / 0,519 | 0,684 / 0,416 | **0,789 / 0,633** | 0,450 / 0,301 |

Okuma (2026-08-29): (1) genişletme ağırlığı 2,0 fazla — 0,5 nDCG'yi 0,433→0,452 yükseltiyor, `bilgi-guncelleme`'yi 0,40→0,45; (2) **sabit güncel-yüzey ödünleşmeli**: güncelleme sorularını 0,70'e çıkarıyor ama çok-oturum'u 0,68→0,42, zamansal'ı 0,68→0,58 düşürüyor (arşiv/soğuk kayıtları dışlıyor); (3) **auto yönlendirme** (yüzey yalnız soruda "güncel/son/şu an…" varsa) her ikisini korur: TÜMÜ 0,654/0,468, zamansal 0,789/0,633 (en yüksek).

**Uygulanan (Katman-2, ölçüm kuralıyla):** `GEN_AGIRLIK 2,0 → 0,5` (`erisim-fts.py`; kural: nDCG ∧ bilgi-guncelleme ≥ mevcut, ikisi de sağlandı). `fts5+auto` erisim-fts eval'ine 4. yöntem olarak eklendi (additive; varsayılan yöntem semantiği değişmedi — auto'yu ana yol yapmak Karar 60 masasının konusu, RRF ile birlikte).

## 2. Çekimserlik eşiği (2026-08-29; top-1 skor; kural "skor ≥ eşik → çekimser"; dengeli doğruluk = ½(cevapsız yakalama + isabet koruma); n küçük → öneri [?])

| Yöntem | cevapsız medyan | isabet medyan | eşik | dengeli doğruluk | yakalama / koruma | n |
|---|---|---|---|---|---|---|
| vektor-e5 (kosinüs uzaklığı) | 0,531 | 0,486 | **0,522** | **0,837** | 0,79 / 0,88 | 19 / 43 |
| vektor-bge | 0,897 | 0,801 | 0,821 | 0,810 | 0,95 / 0,67 | 19 / 49 |
| vektor-e5-int8 | 68,7 | 63,4 | 67,9 | 0,813 | 0,74 / 0,89 | 19 / 45 |
| vektor-bge-int8 | 114,9 | 102,6 | 105,6 | 0,814 | 0,95 / 0,68 | 19 / 50 |
| fts5+gen (bm25, negatif) | −14,99 | −31,53 | −19,86 | 0,788 | 0,68 / 0,89 | 19 / 46 |

Okuma (2026-08-29): vektör uzaklığı çekimserliği bm25'ten iyi ayırıyor (0,84 ↔ 0,79); e5 en dengeli. Eşikler ÖNERİ (n=19 cevapsız); "cevap yok" davranışı için RRF katmanında e5 uzaklığı ≥0,52 ∧ bm25 ≥ −19,9 birleşik kuralı masa adayı.

## 3. Gözlem (2026-08-29, kayda değer): eval sürüklenmesi
`erisim-fts --eval` fts5+gen TÜMÜ recall@5 sabah 0,593 → akşam 0,568 (aynı 100 soru, silver 53.983 kayıt sabit): FTS indeksi son hat koşumunda `gecerlilik/katman` bayraklarıyla yeniden kuruldu → güncel-yüzey ve katman-sıralaması değişti. Ağırlık parametresi sıralamayı değiştirmedi (grid'de gen=2 = 0,630, sabahki erisim-vektor ölçümüyle aynı). Ders: eval satırları indeks kimliği (uretim git_head) taşıyor — kıyas aynı indekste yapılmalı; hasat adayı.

## 4. Ne değişti / ne değişmedi / kalan
- Değişen: GEN_AGIRLIK 0,5 · `fts5+auto` yöntemi · kalibrasyon aracı + 2 gold görünüm + kütük · çekimserlik eşik önerileri.
- Değişmeyen: erişim ana yolu (fts5+gen semantiği) · vektör/RRF benimseme kararı (Karar 60, Salih) · 75 sorunun KESTİRİM statüsü (Salih teyidi).
- İB-43 KAPANDI: kalan yalnız Salih-tarafı (soru teyidi) ve karar-sonrası işler (artımlı gömme, RRF ana yol).
