import sqlite3, time, random, statistics
random.seed(42)
c=sqlite3.connect(':memory:')
N_URUN, N_MUSTERI, N_KALEM = 500, 20_000, 300_000

c.executescript("""
CREATE TABLE urun(urun_kod INT PRIMARY KEY, ad TEXT, kategori TEXT, fiyat REAL);
CREATE TABLE musteri(musteri_no INT PRIMARY KEY, ad TEXT, sehir TEXT);
CREATE TABLE kalem(id INTEGER PRIMARY KEY, musteri_no INT, urun_kod INT, adet INT);
""")
sehirler=['Ankara','Izmir','Istanbul','Bursa','Antalya']
kategoriler=['Elektronik','Kirtasiye','Gida','Giyim']
c.executemany("INSERT INTO urun VALUES (?,?,?,?)",
    [(i,f'Urun{i}',random.choice(kategoriler),round(random.uniform(10,2000),2)) for i in range(N_URUN)])
c.executemany("INSERT INTO musteri VALUES (?,?,?)",
    [(i,f'Musteri{i}',random.choice(sehirler)) for i in range(N_MUSTERI)])
c.executemany("INSERT INTO kalem(musteri_no,urun_kod,adet) VALUES (?,?,?)",
    [(random.randrange(N_MUSTERI),random.randrange(N_URUN),random.randint(1,5)) for _ in range(N_KALEM)])
c.executescript("CREATE INDEX ix_k_urun ON kalem(urun_kod); CREATE INDEX ix_k_mus ON kalem(musteri_no);")

# denormalize kopya (ayni veri, tek genis tablo)
c.executescript("""
CREATE TABLE genis AS
SELECT k.id, k.adet, m.musteri_no, m.ad AS musteri_ad, m.sehir,
       u.urun_kod, u.ad AS urun_ad, u.kategori, u.fiyat
FROM kalem k JOIN musteri m USING(musteri_no) JOIN urun u USING(urun_kod);
CREATE INDEX ix_g_urun ON genis(urun_kod);
""")
def olc(sql, tekrar=5):
    sureler=[]
    for _ in range(tekrar):
        t=time.perf_counter(); c.execute(sql).fetchall(); sureler.append((time.perf_counter()-t)*1000)
    return statistics.median(sureler)

print(f"Veri: {N_KALEM:,} kalem · {N_MUSTERI:,} musteri · {N_URUN} urun")
print(f"Tablo boyutlari (sqlite sayfa tahmini):")
for t in ('kalem','musteri','urun','genis'):
    n=c.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0]; print(f'   {t:9s} {n:>8,} satir')

NORM_AGG = """SELECT u.kategori, m.sehir, SUM(k.adet*u.fiyat) AS ciro
              FROM kalem k JOIN urun u USING(urun_kod) JOIN musteri m USING(musteri_no)
              GROUP BY 1,2"""
GENIS_AGG = """SELECT kategori, sehir, SUM(adet*fiyat) AS ciro FROM genis GROUP BY 1,2"""
NORM_TEK = "SELECT k.*, u.ad, m.ad FROM kalem k JOIN urun u USING(urun_kod) JOIN musteri m USING(musteri_no) WHERE k.id=150000"
GENIS_TEK = "SELECT * FROM genis WHERE id=150000"

print("\n--- OKUMA: kategori x sehir ciro raporu (tum tabloyu tarayan analitik sorgu) ---")
a,b=olc(NORM_AGG),olc(GENIS_AGG)
print(f"   3 tablo JOIN (3NF)   : {a:7.1f} ms")
print(f"   tek genis tablo      : {b:7.1f} ms   -> {a/b:.1f}x hizli")

print("\n--- OKUMA: tek satir sorgusu (OLTP tipi) ---")
a,b=olc(NORM_TEK,20),olc(GENIS_TEK,20)
print(f"   3 tablo JOIN (3NF)   : {a:7.3f} ms")
print(f"   tek genis tablo      : {b:7.3f} ms")

print("\n--- YAZMA: bir urunun fiyati degisti ---")
t=time.perf_counter(); cur=c.execute("UPDATE urun SET fiyat=fiyat*1.1 WHERE urun_kod=7"); s1=(time.perf_counter()-t)*1000
n1=cur.rowcount
t=time.perf_counter(); cur=c.execute("UPDATE genis SET fiyat=fiyat*1.1 WHERE urun_kod=7"); s2=(time.perf_counter()-t)*1000
n2=cur.rowcount
print(f"   3NF   : {n1:>6,} satir, {s1:7.3f} ms")
print(f"   genis : {n2:>6,} satir, {s2:7.3f} ms   -> {s2/s1:.0f}x yavas, ve yarida kalirsa tutarsiz")

print("\n--- SORGU PLANLARI ---")
for ad,sql in (('3NF agregasyon',NORM_AGG),('genis agregasyon',GENIS_AGG)):
    print(f'   [{ad}]')
    for r in c.execute('EXPLAIN QUERY PLAN '+sql): print('      ',r[-1])

print("\n--- DUZELTME: genis tablosunda id indekssizdi, adil olsun diye indeks ekliyorum ---")
c.execute("CREATE INDEX ix_g_id ON genis(id)")
a,b=olc(NORM_TEK,20),olc(GENIS_TEK,20)
print(f"   3 tablo JOIN (3NF)   : {a:7.3f} ms")
print(f"   tek genis tablo      : {b:7.3f} ms")
for ad,sql in (('3NF tek satir',NORM_TEK),('genis tek satir',GENIS_TEK)):
    print(f'   [{ad}]')
    for r in c.execute('EXPLAIN QUERY PLAN '+sql): print('      ',r[-1])
