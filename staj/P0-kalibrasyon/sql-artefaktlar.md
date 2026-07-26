# P0 — SQL Artefaktları (10 sorgu, soğuk okuma)

**Kural:** Şemayı ve veriyi (`seed.sql`) oku. Her sorgu için ÇALIŞTIRMADAN yazılı tahmin: **kaç satır döner + değerler ne olur + varsa tuzak nedir.** Tahminleri `P0-tahminlerim.md`'ye yaz, sonra `sqlite3` ile doğrula, EN SON `cevap-anahtari.md`'yi aç. Bazı sorgular temizdir — her soruda tuzak arama refleksi de bir hatadır.

Tahmin şablonu (her sorgu için):
```
S_: satır sayısı = __ · sonuç = __ · tuzak var mı, neyse ne = __
```

---

**S1**
```sql
SELECT m.ad, COUNT(s.id) AS adet
FROM musteri m
LEFT JOIN satis s ON s.alici_id = m.id
WHERE s.tarih >= '2026-07-01'
GROUP BY m.ad;
```

**S2**
```sql
SELECT ad FROM musteri
WHERE id NOT IN (SELECT sahip_id FROM arac);
```

**S3**
```sql
SELECT COUNT(*), COUNT(fiyat), COUNT(DISTINCT marka) FROM arac;
```

**S4**
```sql
SELECT a.marka, SUM(a.fiyat) AS toplam
FROM arac a
JOIN servis sv ON sv.arac_id = a.id
GROUP BY a.marka;
```

**S5**
```sql
SELECT COUNT(*) FROM arac
WHERE fiyat < 700000 OR fiyat >= 700000;
```

**S6**
```sql
SELECT alici_id, SUM(tutar) AS toplam
FROM satis
GROUP BY alici_id
HAVING SUM(tutar) > 500000;
```

**S7**
```sql
SELECT COUNT(*) FROM satis
WHERE tarih BETWEEN '2026-06-01' AND '2026-06-30';
```

**S8**
```sql
SELECT m.ad
FROM musteri m
LEFT JOIN arac a ON a.sahip_id = m.id
WHERE a.id IS NULL;
```

**S9**
```sql
SELECT COUNT(a.id) AS satir, COUNT(DISTINCT a.id) AS tekil
FROM arac a
JOIN servis sv ON sv.arac_id = a.id;
```

**S10**
```sql
SELECT ad FROM musteri
WHERE NOT (sehir = 'Ankara');
```
