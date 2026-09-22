#!/usr/bin/env python3
"""10-olap-duckdb-olcum.py — YILDIZ ↔ OBT şema kararı, KOLONSAL motorda (DuckDB + Parquet).

09-olap-sema-karar.py aynı karşılaştırmayı SQLite'ta (satır-deposu) yapar. Bu betik, satır-deposunda
ÖLÇÜLEMEYEN üç ekseni ekler:
  (1) sıkıştırılmış depolama  — sözlük/RLE kodlama tekrarlı boyut sütunlarını ne kadar eritiyor
  (2) taranan byte            — kolon budama; sorgunun dokunduğu kolon-chunk toplamı (parquet_metadata)
  (3) düzeltme maliyeti       — kolonsalda "satır güncelleme" yoktur, dosya YENİDEN YAZILIR

Bağımlılık: duckdb (stdlib dışı). Koşum:  <venv>/bin/python 10-olap-duckdb-olcum.py
Deneysel ölçüm (m.29): tek makine, yerel disk, eşzamanlılık yok, sıcak sayfa önbelleği.
"""
import os, time, statistics, tempfile, shutil
import duckdb

F, D_URUN, D_MUS = 500_000, 2_000, 50_000
DIZIN = tempfile.mkdtemp(prefix='olap-olcum-')
con = duckdb.connect()
con.execute("SET preserve_insertion_order=false")

def yol(ad): return os.path.join(DIZIN, ad)
def mb(p): return os.path.getsize(p)/1e6

# ---------------------------------------------------------------- veri üretimi
con.execute(f"""
CREATE TABLE d_urun AS
SELECT i AS urun_kod, 'Urun'||i AS ad, 'Kat'||(i%12) AS kategori,
       'Marka'||(i%150) AS marka, round(10+random()*2990,2) AS fiyat
FROM range({D_URUN}) t(i);
CREATE TABLE d_musteri AS
SELECT i AS musteri_no, 'Musteri'||i AS ad, 'Sehir'||(i%81) AS sehir, 'Segment'||(i%5) AS segment
FROM range({D_MUS}) t(i);
CREATE TABLE f_satis AS
SELECT i AS id, (random()*{D_MUS})::INT % {D_MUS} AS musteri_no,
       (random()*{D_URUN})::INT % {D_URUN} AS urun_kod,
       1+(random()*4)::INT AS adet, 20260101+(random()*199)::INT AS tarih
FROM range({F}) t(i);
CREATE TABLE obt AS
SELECT f.id, f.musteri_no, m.ad AS musteri_ad, m.sehir, m.segment,
       f.urun_kod, u.ad AS urun_ad, u.kategori, u.marka, u.fiyat, f.adet, f.tarih
FROM f_satis f JOIN d_musteri m USING(musteri_no) JOIN d_urun u USING(urun_kod);
""")

def yaz(tablo, dosya, sirala=''):
    con.execute(f"COPY (SELECT * FROM {tablo} {sirala}) TO '{yol(dosya)}' "
                f"(FORMAT PARQUET, COMPRESSION ZSTD)")

for t,d,s in (('f_satis','f_satis.parquet','ORDER BY tarih, urun_kod'),
              ('d_urun','d_urun.parquet',''), ('d_musteri','d_musteri.parquet',''),
              ('obt','obt.parquet','ORDER BY tarih, urun_kod')):
    yaz(t,d,s)

YILDIZ = [yol('f_satis.parquet'), yol('d_urun.parquet'), yol('d_musteri.parquet')]
OBT = yol('obt.parquet')

print(f"Ölçek: fact {F:,} · d_urun {D_URUN:,} ({100*D_URUN/F:.2f}%) · d_musteri {D_MUS:,} ({100*D_MUS/F:.1f}%)")
print(f"DuckDB {duckdb.__version__} · parquet ZSTD · dizin {DIZIN}\n")

# ---------------------------------------------------------------- 1) DEPOLAMA
print("="*74); print("1) DEPOLAMA (sıkıştırılmış parquet)"); print("="*74)
y_top = sum(mb(p) for p in YILDIZ)
print(f"   yıldız  : {y_top:7.2f} MB  (f_satis {mb(YILDIZ[0]):.2f} + d_urun {mb(YILDIZ[1]):.2f} + d_musteri {mb(YILDIZ[2]):.2f})")
print(f"   OBT     : {mb(OBT):7.2f} MB")
fark = mb(OBT)-y_top
print(f"   fark    : {fark:+7.2f} MB  ({100*fark/y_top:+.0f}%) · fact satırı başına {fark*1e6/F:+.1f} byte")

print("\n   OBT'ye gömülen boyut sütunlarının kolonsal maliyeti:")
q = f"""SELECT path_in_schema AS kolon, SUM(total_compressed_size) AS sikistirilmis,
        SUM(total_uncompressed_size) AS ham
        FROM parquet_metadata('{OBT}')
        WHERE path_in_schema IN ('musteri_ad','sehir','segment','urun_ad','kategori','marka','fiyat')
        GROUP BY 1 ORDER BY 2 DESC"""
for kolon, sik, ham in con.execute(q).fetchall():
    print(f"      {kolon:<12} {sik/1e6:6.2f} MB sıkıştırılmış  ← {ham/1e6:6.2f} MB ham "
          f"({ham/max(sik,1):.1f}x) · {sik/F:6.2f} byte/satır")

# ---------------------------------------------------------------- 2) İŞ YÜKÜ
print("\n"+"="*74); print("2) İŞ YÜKÜ (ağırlıklı okuma)"); print("="*74)
IS_YUKU = [
 ('Q1 kategori × şehir ciro (2 boyut)', 0.5,
  f"""SELECT u.kategori, m.sehir, SUM(f.adet*u.fiyat) FROM read_parquet('{YILDIZ[0]}') f
      JOIN read_parquet('{YILDIZ[1]}') u USING(urun_kod)
      JOIN read_parquet('{YILDIZ[2]}') m USING(musteri_no) GROUP BY 1,2""",
  f"SELECT kategori, sehir, SUM(adet*fiyat) FROM read_parquet('{OBT}') GROUP BY 1,2",
  ['adet','urun_kod','musteri_no'], ['kategori','sehir','adet','fiyat']),
 ('Q2 marka ciro (1 boyut)', 0.3,
  f"""SELECT u.marka, SUM(f.adet*u.fiyat) FROM read_parquet('{YILDIZ[0]}') f
      JOIN read_parquet('{YILDIZ[1]}') u USING(urun_kod) GROUP BY 1""",
  f"SELECT marka, SUM(adet*fiyat) FROM read_parquet('{OBT}') GROUP BY 1",
  ['adet','urun_kod'], ['marka','adet','fiyat']),
 ('Q3 segment + tarih filtreli sayım', 0.2,
  f"""SELECT COUNT(*), SUM(f.adet) FROM read_parquet('{YILDIZ[0]}') f
      JOIN read_parquet('{YILDIZ[2]}') m USING(musteri_no)
      WHERE m.segment='Segment2' AND f.tarih BETWEEN 20260101 AND 20260131""",
  f"""SELECT COUNT(*), SUM(adet) FROM read_parquet('{OBT}')
      WHERE segment='Segment2' AND tarih BETWEEN 20260101 AND 20260131""",
  ['adet','musteri_no','tarih'], ['segment','tarih','adet']),
]
def olc(sql, tekrar=5):
    s=[]
    for _ in range(tekrar):
        t=time.perf_counter(); con.execute(sql).fetchall(); s.append((time.perf_counter()-t)*1000)
    return statistics.median(s)
def kolon_byte(dosyalar, kolonlar):
    top=0
    for d in dosyalar:
        liste=",".join(f"'{k}'" for k in kolonlar)
        r=con.execute(f"SELECT COALESCE(SUM(total_compressed_size),0) FROM parquet_metadata('{d}') "
                      f"WHERE path_in_schema IN ({liste})").fetchone()[0]
        top+=r
    return top

print(f"{'Sorgu':<36}{'yıldız':>10}{'OBT':>10}{'kazanç':>9}{'ağırlık':>9}")
ty=to=0
byte_y=byte_o=0
for ad,w,sy,so,ky,ko in IS_YUKU:
    a,b = olc(sy), olc(so); ty+=w*a; to+=w*b
    # yıldızda: fact kolonları + boyut dosyalarının TAMAMI (join için okunur)
    by = kolon_byte([YILDIZ[0]], ky) + sum(os.path.getsize(p) for p in YILDIZ[1:] if p.split('/')[-1][:7] in ('d_urun.','d_muste'))
    bo = kolon_byte([OBT], ko)
    byte_y+=w*by; byte_o+=w*bo
    print(f"{ad:<36}{a:>9.1f}m{b:>9.1f}m{a/b:>8.2f}x{w:>9.1f}")
print(f"{'AĞIRLIKLI TOPLAM':<36}{ty:>9.1f}m{to:>9.1f}m{ty/to:>8.2f}x")

print(f"\n   Ağırlıklı TARANAN BYTE (kolon budama sonrası):")
print(f"      yıldız : {byte_y/1e6:7.2f} MB   (fact'in ilgili kolonları + boyut dosyaları)")
print(f"      OBT    : {byte_o/1e6:7.2f} MB   (yalnız adı geçen kolonlar)")
print(f"      oran   : {byte_y/max(byte_o,1):.2f}x")

# ---------------------------------------------------------------- 3) DÜZELTME
print("\n"+"="*74); print("3) DÜZELTME MALİYETİ (kolonsalda = dosyayı yeniden yazmak)"); print("="*74)
con.execute("UPDATE d_urun SET kategori='Kat9' WHERE urun_kod=42")
t=time.perf_counter(); yaz('d_urun','d_urun.parquet'); s_y=(time.perf_counter()-t)*1000
con.execute("UPDATE obt SET kategori='Kat9' WHERE urun_kod=42")
t=time.perf_counter(); yaz('obt','obt.parquet','ORDER BY tarih, urun_kod'); s_o=(time.perf_counter()-t)*1000
etkilenen = con.execute("SELECT COUNT(*) FROM obt WHERE urun_kod=42").fetchone()[0]
print(f"   yıldız : d_urun.parquet yeniden yazıldı  {mb(YILDIZ[1]):6.2f} MB  {s_y:8.1f} ms")
print(f"   OBT    : obt.parquet yeniden yazıldı     {mb(OBT):6.2f} MB  {s_o:8.1f} ms   ({s_o/s_y:.0f}x)")
print(f"   (aynı düzeltme OBT'de {etkilenen:,} fact satırına dokunuyor)")

print(f"\nGeçici dizin siliniyor: {DIZIN}")
shutil.rmtree(DIZIN, ignore_errors=True)
