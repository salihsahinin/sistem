# İB-33 — Kolon katmanı k=3 ölçümü (SQLite satır ↔ DuckDB parquet/native) ve bayrak-açma eşiği önerisi

**AS-OF 2026-08-29 · yan icra oturumu (Fable) · HEAD bf215c7 · Karar 63 (KB-55 a, Salih: "hepsi a, venv") · KB-55 icra zinciri İB-33 → İB-30/31 · deneysel m.29, her rakam `veri/kolon-olcum.jsonl`'dan (koşum kimliği = ts; 3 koşum × 6 sorgu × 3 motor = 54 OK satır)**

*Ne bu:* Karar 63 "`--parquet` k=3 soğuk-ölçüme dek varsayılan KAPALI" demişti. Bu rapor k=3 ölçümünü ve **bayrak-açma eşiği ÖNERİSİNİ** (karar Salih'in, İB-30) taşır. Ölçüm aracı [tools/kolon-olcum.py](../tools/kolon-olcum.py) (ClickBench disiplini: ılık = yeni süreç+bağlantı 1. koşum · sıcak = min(2.,3.)); parquet [tools/ambar-parquet.py](../tools/ambar-parquet.py) ile aynı HEAD'de yazıldı (15 tablo, 13,18 MB, eşdeğerlik 0 FAIL).

## 1. Ne yapıldı (08-29, bu oturum)
- `duckdb` 1.5.5 repo-içi `.venv`'e kuruldu (gitignore `**/.venv/`; Karar 63 "venv"). Mac'te ilk kez — önceki tek koşum (08-18, 7d97725) Windows'taydı.
- İB-30 (kısmen): `tools/katman-hatti.py` parquet adımlarını `.venv/bin/python` ile koşar (yoksa çıkış 4 → ATLANDI, hat düşmez) ve **`olcum`'un ÖNÜNE** alır (kanon §8 S3: olcum son adım). Varsayılan hâlâ KAPALI — açma kararı §4'teki eşikle Salih'te.
- İB-31 (kapandı): eşdeğerlik özeti silver `parquet_uretim` tablosuna (sözleşme 1.0.0); `katman-olcum` 2 test: ESDEGERLIK-FAIL/HATA = 0 (error) · parquet git_head = silver HEAD (warn). Hat `--parquet` 17 adım exit 0, iki test PASS.
- İB-33: 3 koşum (hat içi 1 + bağımsız 2; her biri yeni süreç). Birim testleri (`tools/testler/test_kolon_katmani.py`) yeni sıra ve venv seçimi için güncellendi.

## 2. Ölçüm (medyan of 3 koşum; ms; byte = sorgunun dokunduğu depolama, tanım script docstring'inde — motorlar arası aynı sınıf, aynı tanım DEĞİL)

| Sorgu | SQLite ılık / sıcak | parquet ılık / sıcak | native ılık / sıcak | byte SQLite → parquet |
|---|---|---|---|---|
| blok_turu dağılımı | 16,0 / 14,9 | 4,6 / 0,86 | 41,4 / 1,14 | 50,9 MB → 73 KB |
| dosya×token group-by (2 kolon) | 12,1 / 10,7 | 5,3 / 1,04 | 44,9 / 1,10 | 53,6 MB → 70 KB |
| geniş kolon: avg(length(metin)) | 22,7 / 21,6 | 9,8 / 6,12 | 41,9 / 2,40 | 50,9 MB → 5,07 MB |
| join kayit⋈referans token by ref_turu | 106,4 / 104,7 | 8,1 / 4,51 | 46,7 / 6,62 | 64,1 MB → 1,39 MB |
| referans türü×değer top | 4,5 / 3,4 | 4,6 / 1,06 | 41,8 / 1,73 | 2,48 MB → 64 KB |
| tarih×kayıt (ay) | 9,7 / 8,5 | 4,5 / 0,82 | 39,5 / 0,47 | 50,9 MB → 6 KB |

**SQLite/parquet oranı (medyan):** sıcak 3,3×–23,2× (medyan **10,3×**) · ılık 1,0×–13,1× (medyan **2,3×**) · byte 10×–7.844× (medyan **371×**) · parquet kaybeden sorgu **0/6** (08-18 sondajında Q6 geniş-kolon kaybetmişti 17,5↔13,6; bugün 21,6↔6,1 kazanıyor — korpus 42K→53K satır). Native: ılık ~40 ms (tablo yükleme) → tek-sorgu ılık senaryoda parquet'ten kötü, sıcakta en iyi.

## 3. Soğuk ayak — ŞERH (m.39)
"Soğuk önbellek" = OS sayfa-önbelleği boşaltılmış disk okuma; macOS'ta `sudo purge` ister → Carvis koşamaz (Salih el işi). Bu üç koşumun "ılık"ı = yeni süreç + yeni bağlantı, sayfa önbelleği DOLU. Rapor 08-18-2 §S4 de aynı sınırı yazmıştı ("önbellek-altı I/O iddiası YOK"). Eşik önerisi bu şerhle okunur; gerçek soğuk ölçüm istenirse: `sudo purge && .venv/bin/python tools/kolon-olcum.py` (tek koşum, ~2 sn) — sonuç aynı kütüğe düşer.

## 4. Bayrak-açma eşiği ÖNERİSİ (İB-30 kararı Salih'in; sayılar bugünkü ölçümden, m.29)
Koşul (hepsi ∧): (1) k ≥ 3 koşum ✓ · (2) medyan sıcak hızlanma ≥ 3× ✓ (10,3×) · (3) kaybeden sorgu = 0 ✓ (0/6) · (4) eşdeğerlik FAIL = 0 ✓ · (5) parquet üretim + ölçüm süresi ≤ hat süresinin %15'i ✓ (1,5 + 1,4 sn / ~28 sn ≈ %10) · (6) soğuk ayak: ŞERHLİ (purge yok).
- **Seçenek A — AÇ (şerhle):** `--parquet` varsayılan AÇIK, `--parquet-yok` ile kapatılır; duckdb/venv yoksa ATLANDI (hat düşmez). *Artı:* 5/6 koşul ölçülü sağlandı; parquet gitignore'lu türev, geri alma tek bayrak. *Eksi:* her hat +3 sn; soğuk ayak ölçülmedi. *Öneri: A* — açma koşulu "soğuk dahil" idi; soğuk yalnız Salih elinde ölçülebiliyor, fren olarak anlamsız kalıyor.
- **Seçenek B — Salih `sudo purge` koşumundan sonra AÇ:** tek el-işi (~10 sn) + 1 koşum; sonra A. *Artı:* Karar 63 lafzına birebir uyar. *Eksi:* açılış Salih takvimine bağlı.
- **Seçenek C — KAPALI kal:** ölçüm bankası dolmaya devam eder (`--parquet` elle). *Artı:* sıfır risk. *Eksi:* kolon katmanı kullanılmaz, İB-38 (DuckDB plan sınıfı) tetiklenmez.

## 5. Kalan zincir
İB-30 karar (bu rapor §4) · İB-34 wiki `kolon-katmani` (Redshift↔Jarvis eşleme; DEA-C01) · İB-38 DuckDB parquet plan sınıfı (tarama-plan) · İB-32 `.gitattributes` textconv (opsiyonel; duckdb CLI yok).
