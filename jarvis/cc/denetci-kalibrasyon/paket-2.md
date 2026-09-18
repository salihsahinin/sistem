# Denetim paketi P2

KOD: tools/bag-tablo.py → v_bag_ozet.csv
ÖLÇÜT: İDDİA'daki her sayı, ad, işaret/yön, tarih ve dayanak HAM VERİ'de birebir destekleniyorsa PASS; tek bir uyuşmazlık, ham veride olmayan bir dayanak ya da ham verideki tarihle çelişen bir tarih varsa FAIL. Yalnız verilen ham veriye bak; dış bilgi kullanma.

## HAM VERİ
```
kural,tip,kaynak_tur,hedef_tur,n,acik,en_eski_olay,en_yeni_olay
R1,wasRevisionOf,anahtar_kaydi,anahtar_kaydi,10,10,2026-08-12,2026-08-17
R3,wasRevisionOf,kayit,dosya,11,10,2026-07-23,2026-08-29
```

## İDDİA: silver `bag` tablosunda 22 tipli bağ var; tip yalnız wasRevisionOf; R1 anahtar_kaydi→anahtar_kaydi 10 bağ, R3 kayit→dosya 12 bağ.
