import sqlite3, itertools
c=sqlite3.connect(':memory:')
def q(b,sql):
    cur=c.execute(sql); k=[d[0] for d in cur.description]; s=cur.fetchall()
    print('\n'+b); print('   '+' | '.join(k))
    print('   (satir yok)') if not s else [print('   '+' | '.join(str(x) for x in r)) for r in s]

c.executescript("""
CREATE TABLE ogrenci (ogrenci_no INT PRIMARY KEY, ad TEXT, bolum TEXT, bolum_baskani TEXT);
INSERT INTO ogrenci VALUES
 (101,'Ahmet','Bilgisayar','Prof. Demir'),(102,'Zeynep','Bilgisayar','Prof. Demir'),
 (103,'Mert','Makine','Prof. Kaya'),(104,'Elif','Makine','Prof. Kaya'),
 (105,'Can','Bilgisayar','Prof. Demir');
""")
q('Tablo (anahtar TEK sutun: ogrenci_no -> 2NF otomatik saglaniyor)','SELECT * FROM ogrenci')
q('Ama tekrar hala var:',
  "SELECT bolum, bolum_baskani, COUNT(*) AS kac_satirda_yazili FROM ogrenci GROUP BY 1,2")

print('\n--- OTOMATIK BAGIMLILIK TARAYICI: hangi sutun hangi sutunu belirliyor? ---')
kol=[r[1] for r in c.execute("PRAGMA table_info(ogrenci)")]
n=c.execute("SELECT COUNT(*) FROM ogrenci").fetchone()[0]
print(f'   ({n} satir; "X -> Y" = ayni X icin hep ayni Y)')
for x,y in itertools.permutations(kol,2):
    ihlal=c.execute(f'SELECT COUNT(*) FROM (SELECT "{x}" FROM ogrenci GROUP BY "{x}" HAVING COUNT(DISTINCT "{y}")>1)').fetchone()[0]
    if ihlal==0:
        anahtar_mi=c.execute(f'SELECT COUNT(DISTINCT "{x}")=COUNT(*) FROM ogrenci').fetchone()[0]
        print(f'   {x:14s} -> {y:14s}   (sol taraf anahtar mi? {"EVET" if anahtar_mi else "HAYIR  <-- tekrar kaynagi"})')

print('\n--- GUNCELLEME MALIYETI (bolunmeden once) ---')
cur=c.execute("UPDATE ogrenci SET bolum_baskani='Prof. Yildiz' WHERE bolum='Bilgisayar'")
print(f'   Bilgisayar bolumune yeni baskan -> {cur.rowcount} satir guncellendi')

print('\n'+'='*58+'\n3NF AYRISTIRMASI\n'+'='*58)
c.executescript("""
CREATE TABLE bolum (ad TEXT PRIMARY KEY, baskan TEXT NOT NULL);
CREATE TABLE ogrenci2 (ogrenci_no INT PRIMARY KEY, ad TEXT NOT NULL, bolum TEXT REFERENCES bolum(ad));
INSERT INTO bolum VALUES ('Bilgisayar','Prof. Demir'),('Makine','Prof. Kaya'),('Elektrik','Prof. Ates');
INSERT INTO ogrenci2 VALUES (101,'Ahmet','Bilgisayar'),(102,'Zeynep','Bilgisayar'),
 (103,'Mert','Makine'),(104,'Elif','Makine'),(105,'Can','Bilgisayar');
""")
cur=c.execute("UPDATE bolum SET baskan='Prof. Yildiz' WHERE ad='Bilgisayar'")
print(f'   Ayni degisiklik bolunmus halde -> {cur.rowcount} satir guncellendi')
q('Ogrencisi olmayan bolum de yasiyor (Elektrik):','SELECT * FROM bolum')
q('JOIN ile eski gorunum:',
  "SELECT o.ogrenci_no, o.ad, o.bolum, b.baskan FROM ogrenci2 o JOIN bolum b ON b.ad=o.bolum ORDER BY 1")
