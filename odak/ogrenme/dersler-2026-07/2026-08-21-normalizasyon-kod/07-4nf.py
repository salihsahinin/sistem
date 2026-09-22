import sqlite3
c=sqlite3.connect(':memory:')
def q(b,sql):
    cur=c.execute(sql); k=[d[0] for d in cur.description]; s=cur.fetchall()
    print('\n'+b); print('   '+' | '.join(k))
    print('   (satir yok)') if not s else [print('   '+' | '.join(str(x) for x in r)) for r in s]

print('='*58+'\n4NF: birbirinden BAGIMSIZ iki coklu gercek ayni tabloda\n'+'='*58)
c.executescript("""
CREATE TABLE calisan_duz (calisan TEXT, beceri TEXT, dil TEXT, PRIMARY KEY (calisan,beceri,dil));
INSERT INTO calisan_duz VALUES
 ('Ahmet','Python','Ingilizce'),('Ahmet','Python','Almanca'),
 ('Ahmet','SQL','Ingilizce'),   ('Ahmet','SQL','Almanca');
""")
q('Ahmet 2 beceri + 2 dil biliyor -> tablo 4 satir (2x2)','SELECT * FROM calisan_duz')
print("\n   Ahmet 3. beceriyi ogrendi (Docker) -> kac satir eklemem gerekir?")
c.executescript("INSERT INTO calisan_duz VALUES ('Ahmet','Docker','Ingilizce'),('Ahmet','Docker','Almanca');")
q('Simdi:', "SELECT COUNT(*) AS satir_sayisi, COUNT(DISTINCT beceri) AS beceri, COUNT(DISTINCT dil) AS dil FROM calisan_duz")
print("   -> 1 beceri icin 2 satir yazdim. Dil sayisi kadar. (m x n buyumesi)")
print("   -> Ustelik 'Docker' satirlarindan birini unutsam, Ahmet Docker'i sadece Ingilizce mi biliyor gibi gorunur.")

c.executescript("""
CREATE TABLE calisan_beceri (calisan TEXT, beceri TEXT, PRIMARY KEY(calisan,beceri));
CREATE TABLE calisan_dil (calisan TEXT, dil TEXT, PRIMARY KEY(calisan,dil));
INSERT INTO calisan_beceri VALUES ('Ahmet','Python'),('Ahmet','SQL'),('Ahmet','Docker');
INSERT INTO calisan_dil VALUES ('Ahmet','Ingilizce'),('Ahmet','Almanca');
""")
q('4NF hali: iki ayri tablo -> toplam satir',
  """SELECT (SELECT COUNT(*) FROM calisan_beceri) AS beceri_satir,
            (SELECT COUNT(*) FROM calisan_dil) AS dil_satir,
            (SELECT COUNT(*) FROM calisan_beceri)+(SELECT COUNT(*) FROM calisan_dil) AS toplam""")
print("   -> 6 satir yerine 5. Buyume m x n degil, m + n.")
print("   -> 10 beceri + 5 dil olsaydi: duz tablo 50 satir, bolunmus 15 satir.")
q('Yeni dil eklemek: TEK satir (Fransizca)', "SELECT 1 AS ornek")
c.execute("INSERT INTO calisan_dil VALUES ('Ahmet','Fransizca')")
q('calisan_dil','SELECT * FROM calisan_dil')
print("   Duz tabloda ayni islem 3 satir gerektirirdi (her beceri icin bir tane).")
