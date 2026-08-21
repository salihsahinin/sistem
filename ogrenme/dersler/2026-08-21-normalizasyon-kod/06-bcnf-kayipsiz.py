import sqlite3
c=sqlite3.connect(':memory:')
def q(b,sql):
    cur=c.execute(sql); k=[d[0] for d in cur.description]; s=cur.fetchall()
    print('\n'+b); print('   '+' | '.join(k))
    print('   (satir yok)') if not s else [print('   '+' | '.join(str(x) for x in r)) for r in s]
print('='*58+'\nBCNF ORNEGI\nKurallar: her hoca TEK ders verir | bir derste COK hoca olabilir\n'
      '          bir ogrenci bir dersi TEK hocadan alir\n'+'='*58)
c.executescript("""
CREATE TABLE kayit (ogrenci TEXT, ders TEXT, hoca TEXT);
INSERT INTO kayit VALUES
 ('Ahmet','MAT1','Prof. Demir'),('Zeynep','MAT1','Prof. Demir'),
 ('Mert','MAT1','Prof. Kaya'),('Ahmet','FIZ2','Prof. Ates');
""")
q('Tablo','SELECT * FROM kayit')
q('ADAY ANAHTAR TESTI: hangi kombinasyon satiri ayirt ediyor? (4 satir)',
  """SELECT COUNT(*) AS satir,
     COUNT(DISTINCT ogrenci) AS ogr, COUNT(DISTINCT ders) AS drs, COUNT(DISTINCT hoca) AS hca,
     COUNT(DISTINCT ogrenci||'|'||ders) AS ogr_ders, COUNT(DISTINCT ogrenci||'|'||hoca) AS ogr_hoca,
     COUNT(DISTINCT ders||'|'||hoca) AS ders_hoca FROM kayit""")
q('hoca -> ders bagimliligi (her hoca kac farkli derste?)',
  "SELECT hoca, COUNT(DISTINCT ders) AS farkli_ders, COUNT(*) AS kac_satirda FROM kayit GROUP BY 1")
print('\n   -> "Prof. Demir MAT1 verir" bilgisi 2 satirda tekrar ediyor.')
print('   -> Ama TUM sutunlar bir aday anahtarin parcasi (asal) oldugu icin 3NF IHLALI YOK.')

print('\n'+'='*58+'\nBCNF AYRISTIRMASI: (hoca,ders) + (ogrenci,hoca)\n'+'='*58)
c.executescript("""
CREATE TABLE hoca_ders (hoca TEXT PRIMARY KEY, ders TEXT NOT NULL);
CREATE TABLE ogrenci_hoca (ogrenci TEXT, hoca TEXT REFERENCES hoca_ders(hoca), PRIMARY KEY (ogrenci,hoca));
INSERT INTO hoca_ders VALUES ('Prof. Demir','MAT1'),('Prof. Kaya','MAT1'),('Prof. Ates','FIZ2');
INSERT INTO ogrenci_hoca VALUES ('Ahmet','Prof. Demir'),('Zeynep','Prof. Demir'),('Mert','Prof. Kaya'),('Ahmet','Prof. Ates');
""")
q('hoca_ders (tekrar bitti: her hoca 1 satir)','SELECT * FROM hoca_ders')
q('JOIN ile eski gorunum aynen geri geliyor',
  "SELECT oh.ogrenci, hd.ders, oh.hoca FROM ogrenci_hoca oh JOIN hoca_ders hd USING(hoca) ORDER BY 1,2")

print('\n--- BEDELI: kural artik tek tabloda denetlenemiyor ---')
print("   Kural: bir ogrenci bir dersi TEK hocadan alir  =  (ogrenci,ders) -> hoca")
print("   Ahmet'i MAT1 icin Prof. Kaya'ya DA yaziyorum (zaten Prof. Demir'den aliyor):")
c.execute("INSERT INTO ogrenci_hoca VALUES ('Ahmet','Prof. Kaya')")
print("   -> INSERT KABUL EDILDI (iki tablo da kendi basina kurali ihlal etmiyor)")
q('Ihlal ancak JOIN edince goruluyor:',
  """SELECT oh.ogrenci, hd.ders, COUNT(DISTINCT oh.hoca) AS kac_hoca
     FROM ogrenci_hoca oh JOIN hoca_ders hd USING(hoca)
     GROUP BY 1,2 HAVING COUNT(DISTINCT oh.hoca)>1""")

print('\n'+'='*58+'\nKAYIPSIZ BIRLESIM: yanlis bolme neye benzer\n'+'='*58)
c.executescript("""
CREATE TABLE ogr (no INT, ad TEXT, bolum TEXT);
INSERT INTO ogr VALUES (101,'Ahmet','Bilgisayar'),(102,'Zeynep','Makine');
CREATE TABLE parca_a AS SELECT ad, bolum FROM ogr;      -- ortak sutun: bolum
CREATE TABLE parca_b AS SELECT bolum, no FROM ogr;
INSERT INTO ogr VALUES (103,'Ahmet','Makine');
INSERT INTO parca_a VALUES ('Ahmet','Makine');
INSERT INTO parca_b VALUES ('Makine',103);
""")
q('Orijinal tablo (3 satir)','SELECT * FROM ogr ORDER BY no')
q('YANLIS bolme: parca_a(ad,bolum) + parca_b(bolum,no) -- ortak sutun "bolum" hicbirinde anahtar degil',
  "SELECT a.no AS a_yok, * FROM (SELECT NULL AS no) a LIMIT 0")
q('JOIN sonucu:',
  "SELECT a.ad, a.bolum, b.no FROM parca_a a JOIN parca_b b ON a.bolum=b.bolum ORDER BY 3,1")
print('   -> 3 satir bekliyorduk; UYDURMA satirlar cikti (ornegin Zeynep|Makine|103).')
