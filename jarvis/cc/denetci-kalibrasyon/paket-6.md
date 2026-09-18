# Denetim paketi P6

KOD: tools/erisim-vektor.py → v_erisim_vektor_etki.csv (taban fts5+gen; bootstrap %95 GA)
ÖLÇÜT: İDDİA'daki her sayı, ad, işaret/yön, tarih ve dayanak HAM VERİ'de birebir destekleniyorsa PASS; tek bir uyuşmazlık, ham veride olmayan bir dayanak ya da ham verideki tarihle çelişen bir tarih varsa FAIL. Yalnız verilen ham veriye bak; dış bilgi kullanma.

## HAM VERİ
```
yontem,taban,metrik,n,fark,ga_alt,ga_ust,anlamli,boot_n,tohum
fts5,fts5+gen,recall5,81,-0.012,-0.099,0.086,hayır,2000,0
fts5,fts5+gen,ndcg10,81,-0.022,-0.095,0.052,hayır,2000,0
rrf-bge,fts5+gen,recall5,81,0.086,0.0,0.185,hayır,2000,0
rrf-bge,fts5+gen,ndcg10,81,0.057,0.006,0.109,evet,2000,0
rrf-e5,fts5+gen,recall5,81,0.074,-0.012,0.173,hayır,2000,0
rrf-e5,fts5+gen,ndcg10,81,0.07,0.022,0.124,evet,2000,0
vektor-bge,fts5+gen,recall5,81,-0.025,-0.148,0.099,hayır,2000,0
vektor-bge,fts5+gen,ndcg10,81,-0.037,-0.119,0.042,hayır,2000,0
vektor-bge-i8,fts5+gen,recall5,81,-0.012,-0.136,0.111,hayır,2000,0
vektor-bge-i8,fts5+gen,ndcg10,81,-0.036,-0.117,0.041,hayır,2000,0
vektor-e5,fts5+gen,recall5,81,-0.099,-0.222,0.037,hayır,2000,0
vektor-e5,fts5+gen,ndcg10,81,-0.063,-0.147,0.02,hayır,2000,0
vektor-e5-i8,fts5+gen,recall5,81,-0.074,-0.198,0.062,hayır,2000,0
vektor-e5-i8,fts5+gen,ndcg10,81,-0.066,-0.149,0.015,hayır,2000,0
```

## İDDİA: rrf-e5 yönteminin nDCG@10 farkı +0,070, GA [+0,022, +0,124], anlamlı; vektor-e5 tek başına recall@5'te tabana göre +0,099 kazanç sağlıyor (GA [-0,222, +0,037]).
