import sqlite3
c=sqlite3.connect(':memory:')
def q(b,sql):
    cur=c.execute(sql); k=[d[0] for d in cur.description]; s=cur.fetchall()
    print('\n'+b); print('   '+' | '.join(k))
    print('   (satir yok)') if not s else [print('   '+' | '.join(str(x) for x in r)) for r in s]
c.executescript("""
CREATE TABLE ders_kaydi (
  ogrenci_no INT NOT NULL, ders_kodu TEXT NOT NULL, notu INT,
  ogrenci_ad TEXT, ders_ad TEXT, kredi INT,
  PRIMARY KEY (ogrenci_no, ders_kodu));
INSERT INTO ders_kaydi VALUES
 (101,'MAT1',75,'Ahmet','Matematik I',6),
 (101,'FIZ2',60,'Ahmet','Fizik II',5),
 (102,'MAT1',90,'Zeynep','Matematik I',6),
 (103,'MAT1',55,'Mert','Matematik I',6),
 (103,'FIZ2',80,'Mert','Fizik II',5);
""")
q('Tablo (anahtar = ogrenci_no + ders_kodu)','SELECT * FROM ders_kaydi')

print('\n--- KISMI BAGIMLILIK TESTI: anahtarin PARCASI tek basina bir sutunu belirliyor mu? ---')
q('Parca 1: ogrenci_no -> ogrenci_ad ?  (hepsi 1 ise: EVET, kismi bagimlilik VAR)',
  "SELECT ogrenci_no, COUNT(DISTINCT ogrenci_ad) AS farkli_ad FROM ders_kaydi GROUP BY 1")
q('Parca 2: ders_kodu -> ders_ad, kredi ?',
  "SELECT ders_kodu, COUNT(DISTINCT ders_ad) AS farkli_ders_ad, COUNT(DISTINCT kredi) AS farkli_kredi FROM ders_kaydi GROUP BY 1")
q('Tam bagimlilik: notu icin anahtarin TAMAMI gerekiyor mu? (parca tek basina yetiyor mu?)',
  "SELECT ogrenci_no, COUNT(DISTINCT notu) AS farkli_not FROM ders_kaydi GROUP BY 1")

q('TEKRAR SAYIMI: ayni bilgi kac satirda yazili?',
  """SELECT 'MAT1 dersinin adi+kredisi' AS bilgi, COUNT(*) AS kac_satirda FROM ders_kaydi WHERE ders_kodu='MAT1'
     UNION ALL SELECT 'Ahmet adi', COUNT(*) FROM ders_kaydi WHERE ogrenci_no=101""")

print("\n--- ANOMALI: MAT1'in kredisi 6 -> 7 oldu ---")
c.execute("UPDATE ders_kaydi SET kredi=7 WHERE ders_kodu='MAT1' AND ogrenci_no=101")
q('Tek satir guncellendi -> tablo simdi ne diyor?',
  "SELECT ders_kodu, GROUP_CONCAT(DISTINCT kredi) AS kredi_degerleri FROM ders_kaydi GROUP BY 1")

print('\n'+'='*60+'\n2NF AYRISTIRMASI: uc tablo\n'+'='*60)
c.executescript("""
CREATE TABLE ogrenci (ogrenci_no INT PRIMARY KEY, ad TEXT NOT NULL);
CREATE TABLE ders (ders_kodu TEXT PRIMARY KEY, ad TEXT NOT NULL, kredi INT NOT NULL);
CREATE TABLE kayit (
  ogrenci_no INT NOT NULL REFERENCES ogrenci(ogrenci_no),
  ders_kodu TEXT NOT NULL REFERENCES ders(ders_kodu),
  notu INT, PRIMARY KEY (ogrenci_no, ders_kodu));
INSERT INTO ogrenci VALUES (101,'Ahmet'),(102,'Zeynep'),(103,'Mert');
INSERT INTO ders VALUES ('MAT1','Matematik I',6),('FIZ2','Fizik II',5);
INSERT INTO kayit VALUES (101,'MAT1',75),(101,'FIZ2',60),(102,'MAT1',90),(103,'MAT1',55),(103,'FIZ2',80);
""")
c.execute("UPDATE ders SET kredi=7 WHERE ders_kodu='MAT1'")
print('   UPDATE ders SET kredi=7 WHERE ders_kodu=\'MAT1\'  -> etkilenen satir:', c.total_changes and 1)
q('Ayni gorunum JOIN ile geri geliyor, kredi TEK ve tutarli',
  """SELECT k.ogrenci_no, k.ders_kodu, k.notu, o.ad AS ogrenci_ad, d.ad AS ders_ad, d.kredi
     FROM kayit k JOIN ogrenci o USING(ogrenci_no) JOIN ders d USING(ders_kodu) ORDER BY 1,2""")
q('Ogrenci hic ders almasa da yasiyor mu? (104 Elif ekliyorum)',
  "SELECT 1")
c.execute("INSERT INTO ogrenci VALUES (104,'Elif')")
q('ogrenci tablosu', "SELECT * FROM ogrenci")
