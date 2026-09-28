import sqlite3
c=sqlite3.connect(':memory:'); c.execute("PRAGMA foreign_keys=ON")
# SQLite tuhafligi: PRIMARY KEY sutunlari NOT NULL degilse NULL kabul eder (eski uyumluluk hatasi).
c.executescript("""
CREATE TABLE siparis_duz (
  siparis_no INT NOT NULL, urun_kod TEXT NOT NULL, adet INT,
  musteri_no INT, musteri_ad TEXT, musteri_sehir TEXT, sehir_plaka INT,
  urun_ad TEXT, urun_fiyat REAL,
  PRIMARY KEY (siparis_no, urun_kod));
INSERT INTO siparis_duz VALUES
 (1,'K-10',2,100,'Ahmet Yilmaz','Ankara',6,'Klavye',450.0),
 (1,'M-20',1,100,'Ahmet Yilmaz','Ankara',6,'Mouse',250.0),
 (2,'K-10',1,100,'Ahmet Yilmaz','Ankara',6,'Klavye',450.0),
 (3,'M-20',3,200,'Zeynep Kaya','Izmir',35,'Mouse',250.0);
""")
try:
    c.execute("INSERT INTO siparis_duz(musteri_no,musteri_ad,musteri_sehir,sehir_plaka) VALUES (300,'Yeni Musteri','Bursa',16)")
    print('[4] Ekleme anomalisi: GECTI (beklenmedik)')
except sqlite3.IntegrityError as e:
    print('[4] Ekleme anomalisi -> siparis vermemis musteri YAZILAMAZ:', e)

# --- 3NF ayristirmasi ---
c.executescript("""
CREATE TABLE sehir   (sehir TEXT PRIMARY KEY, plaka INT NOT NULL);
CREATE TABLE musteri (musteri_no INT PRIMARY KEY, ad TEXT NOT NULL, sehir TEXT REFERENCES sehir(sehir));
CREATE TABLE urun    (urun_kod TEXT PRIMARY KEY, ad TEXT NOT NULL, fiyat REAL NOT NULL);
CREATE TABLE siparis (siparis_no INT PRIMARY KEY, musteri_no INT NOT NULL REFERENCES musteri(musteri_no));
CREATE TABLE siparis_kalem (
  siparis_no INT NOT NULL REFERENCES siparis(siparis_no),
  urun_kod TEXT NOT NULL REFERENCES urun(urun_kod),
  adet INT NOT NULL,
  PRIMARY KEY (siparis_no, urun_kod));
INSERT INTO sehir VALUES ('Ankara',6),('Izmir',35),('Bursa',16);
INSERT INTO musteri VALUES (100,'Ahmet Yilmaz','Ankara'),(200,'Zeynep Kaya','Izmir'),(300,'Yeni Musteri','Bursa');
INSERT INTO urun VALUES ('K-10','Klavye',450.0),('M-20','Mouse',250.0);
INSERT INTO siparis VALUES (1,100),(2,100),(3,200);
INSERT INTO siparis_kalem VALUES (1,'K-10',2),(1,'M-20',1),(2,'K-10',1),(3,'M-20',3);
""")
# Fiyat guncellemesi: TEK satir
c.execute("UPDATE urun SET fiyat=500 WHERE urun_kod='K-10'")
cur=c.execute("""
SELECT sk.siparis_no, sk.urun_kod, sk.adet, m.musteri_no, m.ad, m.sehir, s.plaka, u.ad, u.fiyat
FROM siparis_kalem sk
JOIN siparis  si ON si.siparis_no=sk.siparis_no
JOIN musteri  m  ON m.musteri_no=si.musteri_no
JOIN sehir    s  ON s.sehir=m.sehir
JOIN urun     u  ON u.urun_kod=sk.urun_kod
ORDER BY 1,2""")
print('\n[5] 5 tabloya bolundukten sonra JOIN ile ayni gorunum (fiyat TEK yerde guncellendi):')
for r in cur.fetchall(): print('   ',' | '.join(str(x) for x in r))
print('\n[6] Silinen musteri artik kaybolmuyor:',
      c.execute("SELECT COUNT(*) FROM musteri WHERE musteri_no=300").fetchone()[0], 'satir (siparissiz musteri yasiyor)')
print('[7] Kaynaksiz kalem yazilamaz ->', end=' ')
try:
    c.execute("INSERT INTO siparis_kalem VALUES (9,'X-99',1)"); print('GECTI (beklenmedik)')
except sqlite3.IntegrityError as e: print('FK freni:', e)
