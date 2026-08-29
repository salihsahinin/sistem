# Denetim paketi P5

KOD: tools/d2-eval.py → v_d2_eval.csv
ÖLÇÜT: İDDİA'daki her sayı, ad, işaret/yön, tarih ve dayanak HAM VERİ'de birebir destekleniyorsa PASS; tek bir uyuşmazlık, ham veride olmayan bir dayanak ya da ham verideki tarihle çelişen bir tarih varsa FAIL. Yalnız verilen ham veriye bak; dış bilgi kullanma.

## HAM VERİ
```
kol,n,derleme_ok,ort_precision,ort_recall,ort_dogruluk,tercih_A
a-uretim,5,5,1.0,1.0,,
b1-okuma,5,0,,,0.96,
b2-sql,5,0,,,1.0,
c-hakem,3,0,,,,2
```

## İDDİA: D2 mini-eval: a-uretim kolunda n=5, derleme_ok=5, ort_precision 1,0, ort_recall 1,0; b1-okuma kolunda ort_dogruluk 0,96; b2-sql kolunda ort_dogruluk 1,0; c-hakem kolunda n=3, tercih_A=2.
