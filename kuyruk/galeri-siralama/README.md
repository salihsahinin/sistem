# Galeri sıralama — sentetik veri + CatBoost YetiRank

**Problem:** ihale oturumunda sırayla satılan 20 aracın her biri için, o oturumdaki
aday galerileri "bu aracı alma ihtimaline göre" sırala.
**Bağlam:** [[../ders-gbm-ilerleme]] P16/P17'nin devamı. Gerçek sistem sözlüğü:
`~/Downloads/galeri_scoring_veri_sozlugu_1.xlsx` (290 kolon → burada 73).

Kolon açıklamaları: **[[veri-sozlugu]]** ← önce bunu oku.

## Koşum sırası

```bash
cd ~/jarvis/kuyruk/galeri-siralama
../ders-gbm/.venv/bin/python 01_uret.py      # ~3 sn  -> veri/*.csv
../ders-gbm/.venv/bin/python 02_birlestir.py # ~5 sn  -> veri/egitim_seti.csv
../ders-gbm/.venv/bin/python 03_egit.py      # ~25 sn -> model.cbm + metrik tablosu
../ders-gbm/.venv/bin/python 03_egit.py --tuzak    # zayıf sızıntı gösterimi
../ders-gbm/.venv/bin/python 03_egit.py --sizinti  # pencere kayması sızıntısı
../ders-gbm/.venv/bin/python 04_agac_bak.py 0      # ağaç 0'ın yapısı
../ders-gbm/.venv/bin/python 04_agac_bak.py --ozet # 552 ağacın bölme istatistiği
```

| dosya | ne yapar |
|---|---|
| `01_uret.py` | sentetik evreni üretir (deterministik, tohum 42). Gerçek kural içinde gömülü. |
| `02_birlestir.py` | 4 ham tabloyu tek eğitim tablosuna birleştirir; snapshot **as-of join** burada. |
| `03_egit.py` | zaman bazlı bölme → CatBoost YetiRank → 3 taban çizgisiyle karşılaştırma |
| `04_agac_bak.py` | eğitilmiş modelin ağaçlarını tek tek okur (bölmeler, yapraklar, satır izi) |
| `veri-sozlugu.md` | 73 kolonun tek tek açıklaması + gerçek sistemdeki karşılığı |

`veri/` gitignore'ludur: türev, tohum 42 ile aynen yeniden üretilir.

## İlk koşumun sonucu (2026-08-28, test = 2026-08 ayı, 340 lot, grup başı 54 aday)

| yöntem | kazananın ort. sırası | HR@1 | HR@3 | HR@5 | MRR | NDCG@5 |
|---|---|---|---|---|---|---|
| rastgele | 28,38 | 0,021 | 0,062 | 0,088 | 0,087 | 0,137 |
| popülerlik (`alinan_arac`) | 6,82 | 0,144 | 0,388 | 0,576 | 0,334 | 0,345 |
| elle ağırlıklı skor | 2,13 | 0,691 | 0,918 | 0,953 | 0,807 | 0,849 |
| **CatBoost YetiRank** | **1,56** | **0,768** | **0,953** | **0,974** | **0,858** | **0,892** |

Bölme: eğitim 69.580 satır / 1.280 lot · doğrulama 16.120 / 300 · test 18.360 / 340.
Doğrulama NDCG@5 = 0,894 · early stopping 552. ağaçta durdu (2000 tavan).

**Okuma:** elle ağırlıklı skor zaten güçlü — çünkü gerçek kuralın en ağır terimi
kademe hiyerarşisi ve elle skor onu kopyalıyor. Modelin kazandığı fark
(0,691 → 0,768) etkileşim + U şekilli fiyat uyumu + sıralı dinamikten geliyor.
Gerçek veride de beklenen tablo budur: ML mevcut skoru ezmez, üstüne çıkar.
