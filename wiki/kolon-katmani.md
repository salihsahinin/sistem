# kolon-katmani

**Üst blok:** Jarvis'in KOLON KATMANI = "SQLite yazma deposu (silver, OLTP; değişmez) → parquet toplu türev (gitignore'lu, 0,3-1,5 sn'de yeniden üretilir) → DuckDB salt-okur OLAP okuyucu" deseni; Karar 63 (KB-55/56 a, Salih 08-21: "hepsi a, venv") ile KOŞULLU kabul, `duckdb` repo-içi `.venv`'de (stdlib-önce kuralına yazılı istisna). Durum GÜNCEL · son teyit 2026-08-29 (Mac'te ilk koşum; k=3 ölçüm) · kaynaklar `cc/rapor-2026-08-18-2.md` (m.40b atlas, S1-S4), `cc/pipeline-2026-08-18-kolon-katmani.md`, `tools/ambar-parquet.py`, `tools/kolon-olcum.py`, `raporlar/2026-08-29-ib33-kolon-olcum-k3.md` · güven ORTA (mekanizma 2 kaynak + yerel ölçüm 08-18 ve 08-29 tutarlı; soğuk-önbellek ayağı ölçülmedi, ölçek küçük: 53K satır).

**Çekirdek — mekanizma:**
- **Neden kolon:** analitik sorgu (group-by, sayım, join) satırın tamamını değil birkaç kolonu okur; satır deposu (SQLite b-tree) tek kolon istense de bütün satır sayfalarını tarar, kolon deposu yalnız istenen kolonun chunk'larını. Bugünkü ölçüm: dokunulan byte 2,5-64 MB → 6 KB-5 MB (**medyan 371×** az), sıcak süre medyan **10,3×** hızlı, ılık (yeni süreç+bağlantı) 2,3×; 6 sorguda parquet kaybeden 0.
- **Yazma semantiği (A-YT3):** kolon deposunda yazma birimi TOPLU yüktür; tek-satır insert/update anti-desendir (delta yapısı + birleştirici gerekir). Jarvis'te bu yüzden SQLite yazar, parquet periyodik `COPY (SELECT … ORDER BY sort_key) TO x.parquet` ile toplu türetilir; parquet asla elle güncellenmez.
- **Tazelik damgası:** her parquet dosyasının footer KV_METADATA'sında `git_head · kod_sha · uretim_ts · satir · sort_key`; okuyucu `parquet_bayat` (git_head ≠ HEAD) bayrağını kayda düşer. Eşdeğerlik (satır sayısı + sayısal toplamlar iki motorda eşit) her yazımda test edilir → silver `parquet_uretim` + katman-olcum testi (İB-31).
- **Redshift ↔ Jarvis eşlemesi (DEA-C01 D2-motor kalemi; kaynak rapor A2-1/A2-2/A-YT6):**

| Redshift (docs 2026-08-18) | Jarvis karşılığı | Not |
|---|---|---|
| 1 MB kolon blokları + blok-başı min/max (zone map) → predikat dışı blok okunmaz | parquet row group (4096 satır) + footer istatistikleri (min/max) → row-group atlama | atlama SIRALAMAYA bağlı: sırasız veri "possibly all" okur (A-YT6) |
| Sort key (compound/interleaved) | `COPY … ORDER BY sort_key` (tablo başına tek anahtar: `kayit_id`, `wf_id`…) | sort key kolonuna RUNLENGTH önerilmez (A-YT6) |
| ENCODE AUTO (AZ64 sayısal · LZO metin · RAW sort key) | ZSTD tek sıkıştırma (DuckDB varsayılanı; kolon-tipi kodlama seçimi yok) | AZ64 için nicel oran kaynağı yok (kör nokta) |
| Dist key / dist style (düğümler arası dağıtım) | YOK — tek makine, PARTITION_BY yok (<100 MB, C-YT1) | ölçek büyüyünce ilk açılacak boyut |
| COPY toplu yük · tek-satır INSERT anti-desen | ambar-parquet toplu COPY; SQLite yazar | aynı ilke, aynı gerekçe |
| Materialized view | gold `v_*` CSV + parquet martları (`v_amb_kosum_maliyet`, `v_karar_borcu_ozet`, `v_hareket_gunluk`) | Jarvis'te görünüm = türetilmiş dosya |

- **Kanonik örnek (EN KÜÇÜK hal):** `SELECT blok_turu, count(*) FROM kayit GROUP BY 1` — SQLite 53.473 satırlık `kayit` b-tree'sinin tamamını (50,9 MB, `metin` kolonu dahil) tarar: sıcak 14,9 ms; DuckDB `read_parquet('veri/parquet/kayit.parquet')` yalnız `blok_turu` chunk'larını (73 KB) okur: 0,86 ms. Fark kolon atlamasından; sonuç satırları birebir aynı (eşdeğerlik).

**SOP (pazartesi sabahı):** (1) `python3 tools/katman-hatti.py --parquet` — parquet + kolon-olcum adımları `.venv/bin/python` ile, `olcum`'dan ÖNCE koşar; venv yoksa `ATLANDI` (hat düşmez). (2) `sqlite3 veri/baglam.sqlite "select tablo,durum,satir,byte from parquet_uretim"` — ESDEGERLIK-FAIL/HATA var mı (olcum testi de bakar). (3) Analitik sorgu için `.venv/bin/python -c "import duckdb; print(duckdb.sql(\"select ... from 'veri/parquet/kayit.parquet'\"))"`; ölçüm bankasına eklemek için `.venv/bin/python tools/kolon-olcum.py` (`veri/kolon-olcum.jsonl`, append-only). (4) Gerçek soğuk ölçüm istenirse `sudo purge` (Salih) sonra tek koşum. (5) Varsayılan bayrak kararı: `raporlar/2026-08-29-ib33-kolon-olcum-k3.md` §4 (İB-30, Salih).

**Gotchas (fiilen yaşananlar):**
- `duckdb` stdlib dışı: sistem `python3` ile koşunca ambar-parquet çıkış 4 → hat "ATLANDI" yazar, kimse fark etmez; venv yolu hat'a 08-29'da bağlandı (`yorumlayici_sec`).
- İlk koşum `INSTALL sqlite` ile eklentiyi `~/.duckdb/extensions` altına indirir (ağ + ev-dizini yan etkisi); çevrimdışı ilk koşum çıkış 4.
- DuckDB `TOTAL_BYTES_READ` profil sayacı yerel parquet'te kolon-chunk okumalarını SAYMAZ (%1,4 raporladı) — kolon atlaması kanıtı `byte` (parquet_metadata) alanından okunur, sayaçtan değil (08-18).
- Native (bellek-içi tablo) ılık süresi ~40 ms (tablo yükleme) — tek sorgu senaryosunda parquet'ten kötü; native yalnız çok-sorgulu sıcak oturumda kazanır.
- Parquet gitignore'lu türev: commit'lenmez, HEAD değişince `parquet_bayat=true`; ölçümü taze parquet'le koş.
- Testin bayat sabit listesi (test_kolon_katmani `--atla` yankısı) hat'a adım eklenince kırıldı — liste ADIMLAR'dan türetilir oldu (08-29).

**Süpersede zinciri:** "veri katmanı v1 stdlib/SQLite-only" (08-16 kanon §4) → **yerini aldı: 2026-08-21 Karar 63 — opsiyonel DuckDB okuyucu istisnası, ölçüm tetikli (Q1 8,1→1,2 ms · byte 41 MB→60 KB)**. "Q6 geniş-kolon sorgusunda parquet kaybeder" (08-18 sondajı, 17,5↔13,6 ms) → **yerini aldı: 2026-08-29 k=3 ölçümü — 21,6↔6,1 ms, parquet kazanıyor (korpus 42K→53K satır; m.29)**.

**Bağlantılar:** [[baglam-veri-ambari]] (ambar tabloları, bitemporal) · [[tarama-yontemleri]] (SQLite EQP ↔ DuckDB plan sınıfı; İB-38 açık) · [[silver-saglik]] (silver = yazma deposu; parquet ondan türer) · [[olcum-banki]] (kolon-olcum kütüğü) · [[pointer-sistemi]] (kayit_id sort key) · kaynaklar: `cc/rapor-2026-08-18-2.md` · `raporlar/2026-08-29-ib33-kolon-olcum-k3.md` · `veri/README.md` §Kolon katmanı · `veri/yetkinlik-haritasi.jsonl` D2-motor.
