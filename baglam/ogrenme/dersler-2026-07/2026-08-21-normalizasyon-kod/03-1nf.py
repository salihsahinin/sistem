import sqlite3
c=sqlite3.connect(':memory:')
def q(b,sql):
    cur=c.execute(sql); k=[d[0] for d in cur.description]; s=cur.fetchall()
    print('\n'+b); print('   '+' | '.join(k))
    print('   (satir yok)') if not s else [print('   '+' | '.join(str(x) for x in r)) for r in s]
c.executescript("""
CREATE TABLE ogrenci_duz (ogrenci_no INT PRIMARY KEY, ad TEXT, dersler TEXT);
INSERT INTO ogrenci_duz VALUES
 (101,'Ahmet','MAT1,FIZ2'), (102,'Zeynep','MAT10'), (103,'Mert','FIZ2,MAT1');
""")
q('Tablo (dersler tek hucrede, virgullu)','SELECT * FROM ogrenci_duz')
q("SORU: MAT1 dersini kimler aliyor? -> LIKE '%MAT1%'",
  "SELECT ogrenci_no, ad, dersler FROM ogrenci_duz WHERE dersler LIKE '%MAT1%'")
print("   ^ Zeynep MAT1 ALMIYOR (MAT10 aliyor) ama listeye girdi = YANLIS SONUC")
q("Duzeltme denemesi: virgullerle sarmalayarak ara",
  "SELECT ogrenci_no, ad FROM ogrenci_duz WHERE ','||dersler||',' LIKE '%,MAT1,%'")
print("   ^ dogru cikti ama artik her sorguda string kurmak zorundayim; bosluk/buyuk-kucuk harf her seferinde risk")
