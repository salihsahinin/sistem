# Denetim paketi P4

KOD: tools/tarama-plan-duckdb.py → v_tarama_plan_duckdb.csv (rg_aday = parquet footer min/max simülasyonu)
ÖLÇÜT: İDDİA'daki her sayı, ad, işaret/yön, tarih ve dayanak HAM VERİ'de birebir destekleniyorsa PASS; tek bir uyuşmazlık, ham veride olmayan bir dayanak ya da ham verideki tarihle çelişen bir tarih varsa FAIL. Yalnız verilen ham veriye bak; dış bilgi kullanma.

## HAM VERİ
```
sorgu,tur,siniflar,uyum,ihlal,projeksiyon_n,kolon_n,rg_aday,rg_toplam,n_sonuc,kosum_ms,git_head
NP1,noktasal,FİLTRE-İTME|KOLON-BUDAMA,True,False,1,26,1,14,0,2.07,0d186a3
NP2,noktasal,FİLTRE-İTME|KOLON-BUDAMA,True,False,1,26,1,14,1,1.43,0d186a3
NP3,noktasal,FİLTRE-İTME|KOLON-BUDAMA,True,False,1,7,1,18,154,1.25,0d186a3
NP4,noktasal,FİLTRE-İTME|KOLON-BUDAMA,True,False,1,20,1,1,1,0.37,0d186a3
A1,agregasyon,TAM-TARAMA,True,False,,26,,,1,0.28,0d186a3
A2,agregasyon,GROUP-HASH|KOLON-BUDAMA|TAM-TARAMA,True,False,2,26,,,587,3.45,0d186a3
A3,agregasyon,FİLTRE-İTME|GROUP-HASH|KOLON-BUDAMA,True,False,0,26,14,14,1,0.99,0d186a3
L1,like,FİLTRE-İTME|GROUP-HASH|KOLON-BUDAMA,True,False,0,26,1,14,1,0.37,0d186a3
J1,join,GROUP-HASH|JOIN-HASH|KOLON-BUDAMA|TAM-TARAMA,True,False,2,26,,,11,5.56,0d186a3
R1,sirali,FİLTRE-İTME|KOLON-BUDAMA|TOP-N/ORDER,True,False,1,26,,,5,1.44,0d186a3
```

## İDDİA: DuckDB/parquet plan denetiminde ihlal 0; row-group atlaması DuckDB'nin kendi operator_rows_scanned sayacıyla doğrulandı: NP1 sorgusunda sayaç 4.096 satır gösterdi (1 row group).
