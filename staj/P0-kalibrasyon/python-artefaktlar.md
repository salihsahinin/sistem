# P0 — Python Artefaktları (10 hücre, soğuk okuma)

**Kural:** SQL'dekiyle aynı: çalıştırmadan yazılı tahmin (`P0-tahminlerim.md`), sonra çalıştırıp doğrula, en son cevap anahtarı. Ortak veri:

```python
import pandas as pd
import numpy as np

arac = pd.DataFrame({
    "id":      [1, 2, 3, 4, 5, 6],
    "marka":   ["Toyota", "Honda", "Ford", "Renault", "Toyota", "Fiat"],
    "fiyat":   [850000, np.nan, 450000, 600000, 1200000, 380000],
    "sehir":   ["Ankara", "Istanbul", None, "Izmir", "Ankara", "Ankara"],
})
servis = pd.DataFrame({
    "arac_id": [1, 1, 3, 4],
    "maliyet": [5000, 3000, 8000, 2500],
})
```

**PY1** — kaç satır döner?
```python
m = arac.merge(servis, left_on="id", right_on="arac_id")
len(m)
```

**PY2** — çıktı ne, toplamı `len(arac)`'a eşit mi?
```python
arac.groupby("sehir").size()
```

**PY3** — bu hücreden sonra `arac.loc[5, "fiyat"]` kaç?
```python
arac[arac["fiyat"] < 500000]["fiyat"] = 0
```

**PY4** — iki çağrının çıktıları?
```python
def ekle(x, liste=[]):
    liste.append(x)
    return liste
print(ekle(1))
print(ekle(2))
```

**PY5** — `sonuc` ne olur?
```python
sonuc = []
try:
    for _, satir in arac.iterrows():
        if satir["fiyatt"] > 400000:
            sonuc.append(satir["marka"])
except Exception:
    pass
sonuc
```

**PY6** — iki ifadenin değerleri?
```python
print(0.1 + 0.2 == 0.3)
print(round(2.675, 2))
```

**PY7** — kaç satır döner? (fiyat sütununda NaN var)
```python
len(arac[arac["fiyat"] > 400000])
```

**PY8** — `len(a)` kaç?
```python
a = [1, 2]
b = a
b.append(3)
len(a)
```

**PY9** — çıktı ne?
```python
{m: len(m) for m in arac["marka"].unique()}
```

**PY10** — bu hücreden sonra `arac["fiyat"].isna().sum()` kaç?
```python
arac["fiyat"].fillna(0)
```
