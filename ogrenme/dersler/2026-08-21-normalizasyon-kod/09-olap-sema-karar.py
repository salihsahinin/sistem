"""Sema karar olcumu: ayni veri iki semada (yildiz vs tek genis tablo),
is yuku agirlikli maliyet + depolama + tazeleme maliyeti olculur."""
import sqlite3, os, time, random, statistics
random.seed(7)
F, D_URUN, D_MUS = 500_000, 2_000, 50_000
YOL_N, YOL_G = 'olcum_yildiz.db', 'olcum_genis.db'
for y in (YOL_N,YOL_G):
    if os.path.exists(y): os.remove(y)

sehirler=[f'Sehir{i}' for i in range(81)]; kategoriler=[f'Kat{i}' for i in range(12)]
urunler=[(i,f'Urun{i}',random.choice(kategoriler),f'Marka{i%150}',round(random.uniform(10,3000),2)) for i in range(D_URUN)]
musteriler=[(i,f'Musteri{i}',random.choice(sehirler),f'Segment{i%5}') for i in range(D_MUS)]
olaylar=[(random.randrange(D_MUS),random.randrange(D_URUN),random.randint(1,5),20260101+random.randrange(200)) for _ in range(F)]

# --- YILDIZ (fact + 2 boyut) ---
n=sqlite3.connect(YOL_N)
n.executescript("""
CREATE TABLE d_urun(urun_kod INT PRIMARY KEY, ad TEXT, kategori TEXT, marka TEXT, fiyat REAL);
CREATE TABLE d_musteri(musteri_no INT PRIMARY KEY, ad TEXT, sehir TEXT, segment TEXT);
CREATE TABLE f_satis(id INTEGER PRIMARY KEY, musteri_no INT, urun_kod INT, adet INT, tarih INT);
""")
n.executemany("INSERT INTO d_urun VALUES (?,?,?,?,?)",urunler)
n.executemany("INSERT INTO d_musteri VALUES (?,?,?,?)",musteriler)
n.executemany("INSERT INTO f_satis(musteri_no,urun_kod,adet,tarih) VALUES (?,?,?,?)",olaylar)
n.commit()

# --- TEK GENIS TABLO (OBT) ---
g=sqlite3.connect(YOL_G)
g.executescript("CREATE TABLE obt(id INTEGER PRIMARY KEY, musteri_no INT, musteri_ad TEXT, sehir TEXT, segment TEXT, urun_kod INT, urun_ad TEXT, kategori TEXT, marka TEXT, fiyat REAL, adet INT, tarih INT);")
u={r[0]:r for r in urunler}; m={r[0]:r for r in musteriler}
g.executemany("INSERT INTO obt(musteri_no,musteri_ad,sehir,segment,urun_kod,urun_ad,kategori,marka,fiyat,adet,tarih) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
  [(mn,m[mn][1],m[mn][2],m[mn][3],uk,u[uk][1],u[uk][2],u[uk][3],u[uk][4],ad,t) for (mn,uk,ad,t) in olaylar])
g.commit()

def olc(con,sql,tekrar=3):
    s=[]
    for _ in range(tekrar):
        t=time.perf_counter(); con.execute(sql).fetchall(); s.append((time.perf_counter()-t)*1000)
    return statistics.median(s)

IS_YUKU = [
 ('Q1 kategori x sehir ciro (2 boyut)', 0.5,
  "SELECT u.kategori,m.sehir,SUM(f.adet*u.fiyat) FROM f_satis f JOIN d_urun u USING(urun_kod) JOIN d_musteri m USING(musteri_no) GROUP BY 1,2",
  "SELECT kategori,sehir,SUM(adet*fiyat) FROM obt GROUP BY 1,2"),
 ('Q2 tek boyutlu: marka ciro', 0.3,
  "SELECT u.marka,SUM(f.adet*u.fiyat) FROM f_satis f JOIN d_urun u USING(urun_kod) GROUP BY 1",
  "SELECT marka,SUM(adet*fiyat) FROM obt GROUP BY 1"),
 ('Q3 filtreli: tek segment, tarih araligi', 0.2,
  "SELECT COUNT(*),SUM(f.adet) FROM f_satis f JOIN d_musteri m USING(musteri_no) WHERE m.segment='Segment2' AND f.tarih BETWEEN 20260101 AND 20260131",
  "SELECT COUNT(*),SUM(adet) FROM obt WHERE segment='Segment2' AND tarih BETWEEN 20260101 AND 20260131"),
]
print(f"Olcek: fact {F:,} · d_urun {D_URUN:,} · d_musteri {D_MUS:,}")
print(f"Boyut/fact orani: urun %{100*D_URUN/F:.2f} · musteri %{100*D_MUS/F:.1f}\n")
print(f"{'Sorgu':<38}{'yildiz':>10}{'OBT':>10}{'kazanc':>9}{'agirlik':>9}")
tn=tg=0
for ad,w,sn,sg in IS_YUKU:
    a,b=olc(n,sn),olc(g,sg); tn+=w*a; tg+=w*b
    print(f"{ad:<38}{a:>9.1f}m{b:>9.1f}m{a/b:>8.2f}x{w:>9.1f}")
print(f"{'AGIRLIKLI TOPLAM (1 sorgu basi)':<38}{tn:>9.1f}m{tg:>9.1f}m{tn/tg:>8.2f}x")

n.commit(); g.commit()
bn,bg=os.path.getsize(YOL_N),os.path.getsize(YOL_G)
print(f"\nDEPOLAMA: yildiz {bn/1e6:7.1f} MB · OBT {bg/1e6:7.1f} MB · fark {(bg-bn)/1e6:+.1f} MB (%{100*(bg-bn)/bn:+.0f})")
print(f"   fact satiri basina ek: {(bg-bn)/F:.1f} byte")

print("\nTAZELEME / DUZELTME MALIYETI: bir urunun kategorisi yanlis girilmis, duzeltiliyor")
t=time.perf_counter(); c1=n.execute("UPDATE d_urun SET kategori='Kat9' WHERE urun_kod=42").rowcount; s1=(time.perf_counter()-t)*1000
t=time.perf_counter(); c2=g.execute("UPDATE obt SET kategori='Kat9' WHERE urun_kod=42").rowcount; s2=(time.perf_counter()-t)*1000
print(f"   yildiz: {c1:>7,} satir  {s1:8.2f} ms")
print(f"   OBT   : {c2:>7,} satir  {s2:8.2f} ms   ({s2/max(s1,1e-9):.0f}x)")
print("\nBOYUT BUYUMESI (SCD2 senaryosu): musteri segmenti 1 kez degisirse etkilenen fact satiri")
print("   ", n.execute("SELECT COUNT(*) FROM f_satis WHERE musteri_no=7").fetchone()[0], "satir (tek musteri ornegi)")
for y in (YOL_N,YOL_G): os.remove(y)
