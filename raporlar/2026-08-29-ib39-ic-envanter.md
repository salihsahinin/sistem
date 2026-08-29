# İB-39 (C ailesi) — İç idempotens/determinizm desen envanteri (deterministik grep, atlas girdisi)

**AS-OF 2026-08-29 · üretim: bu dosyanın altındaki grep desenleri `tools/*.py` üzerinde (LLM yok) · sayılar = desen eşleşme sayısı (kanıt değil, İŞARET; ajan doğrular).** Kavram ayrımı (ledger İB-39 notu): determinizm = aynı girdi→aynı çıktı; idempotens = f(f(x))=f(x), yeniden-koşum sonucu değiştirmez.

| script | append-only kütük | tekil anahtar (PRIMARY KEY/UNIQUE) | INSERT OR IGNORE/REPLACE | temp→rename (atomik yazım) | sha/özet anahtarı | tekilleştirme (uuid/kayit_id/… in mevcut) | kuru koşum (--kuru) | sıfırdan yeniden yazım (DROP TABLE/ w yazım) |
|---|---|---|---|---|---|---|---|---|
| `ambar-parquet.py` | · | · | · | 13 | 1 | 2 | 1 | · |
| `ambar-tablo.py` | 1 | 4 | · | · | · | 6 | 1 | 6 |
| `anahtar-denetim.py` | · | · | · | · | · | 1 | · | · |
| `anakronizm-denetim.py` | · | · | · | · | · | 1 | 1 | · |
| `atlas-derle.py` | · | · | · | · | · | 3 | · | 1 |
| `bag-tablo.py` | 1 | 1 | · | · | 1 | 3 | 1 | 1 |
| `baglam-seyir.py` | 1 | 1 | · | · | · | 8 | 1 | 1 |
| `baglam-tablo.py` | · | 3 | · | 8 | 2 | 8 | · | 1 |
| `bayat-cekim.py` | 1 | · | · | · | 1 | · | · | · |
| `deneyim-tablo.py` | · | 1 | · | · | · | 2 | 1 | 2 |
| `erisim-fts.py` | · | 1 | · | · | · | 1 | 1 | 2 |
| `erisim-kalibrasyon.py` | · | · | · | · | · | 13 | · | · |
| `erisim-vektor.py` | · | 3 | · | · | 1 | 1 | · | 1 |
| `hareket-tablo.py` | 1 | 1 | · | · | · | 8 | 1 | 2 |
| `karar-borcu-tablo.py` | · | 1 | · | · | · | · | 1 | · |
| `katman-hatti.py` | · | · | · | 1 | · | · | · | · |
| `katman-olcum.py` | · | · | · | · | · | 1 | 1 | 1 |
| `kod-envanter.py` | · | · | · | · | · | · | 1 | · |
| `kolon-olcum.py` | 1 | · | · | 2 | · | · | 1 | · |
| `kosum-maliyeti.py` | · | · | · | · | · | · | · | 1 |
| `kural-envanter.py` | · | · | · | · | · | · | 1 | · |
| `loop-dedektor.py` | · | · | · | · | 1 | 1 | · | 1 |
| `obsidian-harita.py` | · | · | · | · | · | 1 | · | · |
| `olcum-dortlu.py` | 1 | · | · | · | · | · | · | · |
| `pano-akis.py` | · | · | · | · | · | 5 | · | 1 |
| `pointer-graf.py` | · | · | · | · | 1 | 3 | · | 11 |
| `prompt-tablo.py` | 1 | 1 | · | · | · | 15 | 1 | 3 |
| `silver-saglik.py` | · | 8 | 4 | 8 | 1 | 2 | 1 | · |
| `sunum-proof-of-work.py` | · | · | · | 1 | · | · | · | 1 |
| `sunum-son50.py` | · | · | · | · | · | 3 | · | 1 |
| `tarama-plan-duckdb.py` | · | · | · | · | · | · | 1 | · |
| `tarama-plan.py` | 1 | 2 | · | 5 | · | 2 | 1 | · |
| `yuzey-parmak-izi.py` | · | · | · | 1 | 1 | 2 | · | 1 |

**Toplam:** append-only kütük: 9 · tekil anahtar (PRIMARY KEY/UNIQUE): 27 · INSERT OR IGNORE/REPLACE: 4 · temp→rename (atomik yazım): 39 · sha/özet anahtarı: 10 · tekilleştirme (uuid/kayit_id/… in mevcut): 92 · kuru koşum (--kuru): 17 · sıfırdan yeniden yazım (DROP TABLE/ w yazım): 38 · script 33/43.

**Okuma (ajan için sorular):** (1) `"w"` ile sıfırdan yazan + `"a"` ile ekleyen scriptler aynı dosyaya mı dokunuyor (çift-kayıt riski: hareket-kütüğü)? (2) append-only kütüklerde tekil anahtar var mı, yoksa yeniden koşum satırı çoğaltıyor mu (asof-eval/erisim-kalibrasyon/loop-dedektor jsonl'leri: koşum-özeti satırı bilinçli çoğalıyor — 'koşum kütüğü' ≠ 'olgu kütüğü')? (3) temp→rename yalnız ambar-parquet'te mi? (4) katman-hatti 'saf/idempotent yükleme' iddiası (docstring :5) DROP TABLE + yeniden yazım = idempotent-by-rebuild — retry güvenliği var, kısmi-yazım atomikliği yok.

Desenler: `append-only kütük` = `open\([^)]*\"a\"` · `tekil anahtar (PRIMARY KEY/UNIQUE)` = `PRIMARY KEY|UNIQUE` · `INSERT OR IGNORE/REPLACE` = `INSERT OR (IGNORE|REPLACE)` · `temp→rename (atomik yazım)` = `os\.replace\(|\.rename\(|tmp` · `sha/özet anahtarı` = `hashlib\.(sha1|sha256|md5)` · `tekilleştirme (uuid/kayit_id/… in mevcut)` = `tekil|dedup|mevcut|görüldü|gorulen|seen` · `kuru koşum (--kuru)` = `\"--kuru\"` · `sıfırdan yeniden yazım (DROP TABLE/ w yazım)` = `DROP TABLE|open\([^)]*\"w\"`
