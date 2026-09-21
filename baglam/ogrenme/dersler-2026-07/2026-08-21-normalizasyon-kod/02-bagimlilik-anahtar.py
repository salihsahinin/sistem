import sqlite3
c=sqlite3.connect(':memory:')
c.executescript("""
CREATE TABLE ogrenci (
  ogrenci_no INT, ad TEXT, bolum TEXT, bolum_baskani TEXT);
INSERT INTO ogrenci VALUES
 (101,'Ahmet','Bilgisayar','Prof. Demir'),
 (102,'Zeynep','Bilgisayar','Prof. Demir'),
 (103,'Mert','Makine','Prof. Kaya'),
 (104,'Elif','Makine','Prof. Kaya');
""")
def q(baslik,sql):
    cur=c.execute(sql); kol=[d[0] for d in cur.description]; sat=cur.fetchall()
    print('\n'+baslik); print('   '+' | '.join(kol))
    if not sat: print('   (satir yok)')
    for s in sat: print('   '+' | '.join(str(x) for x in s))

q('TABLO','SELECT * FROM ogrenci')

print('\n--- TEST 1: "bolum -> bolum_baskani" bagimliligi CURUTULEBILIYOR mu? ---')
q('Ayni bolum icin KAC FARKLI baskan yaziliyor? (1 den buyuk cikan = ihlal)',
  "SELECT bolum, COUNT(DISTINCT bolum_baskani) AS farkli_baskan FROM ogrenci GROUP BY bolum")
q('IHLAL EDEN satirlar (bos = veri bagimliligi curutmuyor)',
  "SELECT bolum FROM ogrenci GROUP BY bolum HAVING COUNT(DISTINCT bolum_baskani) > 1")

print('\n--- TEST 2: ters yon "bolum_baskani -> bolum" ---')
q('Ayni baskan kac farkli bolumde?',
  "SELECT bolum_baskani, COUNT(DISTINCT bolum) AS farkli_bolum FROM ogrenci GROUP BY bolum_baskani")

print('\n--- TEST 3: "ad -> bolum" ? ---')
q('Ayni ad kac farkli bolumde? (su anda hepsi 1 -- ama bu KANIT degil)',
  "SELECT ad, COUNT(DISTINCT bolum) AS farkli_bolum FROM ogrenci GROUP BY ad")
print('\n   Yeni satir geldi: (105, Ahmet, Makine, Prof. Kaya)')
c.execute("INSERT INTO ogrenci VALUES (105,'Ahmet','Makine','Prof. Kaya')")
q('Ayni sorgu, yeni veriyle',
  "SELECT ad, COUNT(DISTINCT bolum) AS farkli_bolum FROM ogrenci GROUP BY ad")

print('\n--- TEST 4: hangi sutun satiri TEK BASINA ayirt ediyor? ---')
q('Satir sayisi ile o sutunun farkli deger sayisi esit mi?',
  """SELECT COUNT(*) AS satir, COUNT(DISTINCT ogrenci_no) AS farkli_no,
            COUNT(DISTINCT ad) AS farkli_ad, COUNT(DISTINCT bolum) AS farkli_bolum
     FROM ogrenci""")
