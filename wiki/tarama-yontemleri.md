# tarama-yontemleri

**Üst blok:** Bir sorgunun veriye NASIL dokunduğunun (tarama yöntemi: Seq/Index/Index-Only/Bitmap/TID/Skip/Parallel/Sample) Postgres ↔ SQLite (Jarvis motoru) ↔ DuckDB/parquet ↔ metin (rg) karşılık tablosu + "hangi soruda hangi tarama" seçim kuralı + Jarvis'teki plan-regresyon testi. Durum: **GÜNCEL**; son teyit 2026-08-22 (hat adımı `tarama` her koşumda). Kaynaklar: araştırma `cc/rapor-2026-08-18-3.md` (m.40b; SENTEZ S1-S3), karar KB-57/58 → Karar 64 (08-21 seans-11: seçim kuralı KILAVUZ'a, plan-regresyon testi uyarı modunda KANON), kural satırı `KILAVUZ.md` §tasarım-ilkeleri, araç `tools/tarama-plan.py` (+ `tools/katman-olcum.py` T1-T3, `katman-hatti` hijyen adımı İB-26). Güven: **orta-yüksek** — PG18/SQLite resmî doküman + yerel EQP ölçümü (sqlite 3.51, HEAD 08-18/08-22); sayısal eşikler bilerek YOK (karar değişkeni ölçülür), DuckDB kısmı kurulu olmadığından (duckdb modülü yok) doğrudan ölçülmedi [K].

**Çekirdek — katalog (özet; tam tablo rapor S1):**
| Yöntem (PG adı) | SQLite EQP karşılığı | Jarvis ölçümü (08-18) |
|---|---|---|
| Seq Scan | `SCAN kayit` (indekssiz filtre); bronz metinde `rg` | blok_turu filtresi 5,4 ms · grep 0,24 s / rg ≈0 |
| Index Scan | `SEARCH … USING INDEX (kolon=?)` | PK 0,004 ms |
| Index Only Scan | `… USING COVERING INDEX` (SQLite'ta görünürlük-haritası koşulu YOK → daima kazanır) | count(*) 0,07 ms |
| Bitmap Index+Heap | en yakın `MULTI-INDEX OR` | OR sorgusu 0,01 ms |
| TID/Range | `SEARCH … USING INTEGER PRIMARY KEY (rowid>? AND rowid<?)` | rowid BETWEEN 0,03 ms |
| Skip Scan (PG18) | `SEARCH … (ANY(ref_turu) AND ref_deger=?)` — **yalnız ANALYZE sonrası (stat1)** | 1,08 → 0,02 ms (54×) |
| Parallel / Sample | SQLite'ta YOK (tek iş parçacığı; `ORDER BY random()` = tam tarama) → DuckDB row-group paralel / `USING SAMPLE` | girmez / keşif için |
| SQLite'a özgü | `AUTOMATIC COVERING INDEX` = **kalıcı indeks ADAYI sinyali** · `USE TEMP B-TREE FOR ORDER BY` = indeks-sıralı erişim fırsatı | join indekssiz kolon 28,3 ms |

**Seçim kuralı (KILAVUZ satırı; Karar 64):** anahtar biliniyorsa **SEARCH** · küçük tabloda tam agregasyon **SCAN meşru** (covering varsa iyi) · çok-kolonlu agregasyon → **parquet/DuckDB** (KB-55) · bronz metin araması → **rg** · örnekleme/keşif → DuckDB SAMPLE · silver yenilemesi sonrası **ANALYZE/PRAGMA optimize** (stat1 yokken skip-scan kapalı, planlayıcı N=1M varsayar) · **AUTOMATIC INDEX görüldü → kalıcı indeks adayı** · **LIKE önek → aralık yüklemi** (`dosya_id >= 'core/' AND dosya_id < 'core0'` ya da NOCASE indeks; LIKE'ın SEARCH olması 6 koşula bağlı) · **yüzde-eşiği kuralı YAZILMAZ** — karar değişkeni DOKUNULAN SAYFA sayısı (page_count/dbstat), "%5-10 seçicilikte seq scan" birincil kaynakta yok · plan sabitliği garanti değil (çare merdiveni: ANALYZE → CROSS JOIN → unlikely() → unary + → INDEXED BY son çare) · DuckDB←sqlite_scanner filtre pushdown YOK → OLTP SQLite'ta, OLAP parquet'te.

**Kanonik örnek (EN KÜÇÜK hal):** `SELECT kayit_id FROM kayit WHERE dosya_id=? AND satir_bas<=? AND satir_son>=?` (adresli erişim, N2) → beklenen sınıf SEARCH (`ix_kayit_dosya_satir` bileşik indeksi, İB-26); EQP'de `SCAN kayit` görülürse plan-regresyon testi UYARI (tarama-plan) + katman-olcum T1 ERROR. `tools/tarama-plan.py --sorgu N2` tek sorguyu iki durumda (DB olduğu gibi · geçici kopyada ANALYZE) ölçer; kaynak DB değişmez.

**SOP (pazartesi sabahı):** (1) yeni bir SQL/görünüm yazdın → `EXPLAIN QUERY PLAN` oku: noktasal soruda SCAN varsa indeks ekle (additive DDL, sözleşme değişmez); AUTOMATIC INDEX görürsen kalıcı indeks adayı olarak not düş; (2) `python3 tools/tarama-plan.py` — sorgu setine yeni sorguyu `SORGULAR`'a ekle (ad · SQL · parametre · beklenen sınıf {stat1 yok/var}); (3) `python3 tools/katman-hatti.py` → `tarama` adımı uyarı kanalında "UYARI/BEKLENTİ DIŞI" satırlarını oku; `hijyen` adımı ANALYZE+optimize'ı yapar, `olcum` T1-T3 sayar; (4) bronz metin araması için `rg` (silver'a inmeden); (5) sayısal eşik yazma isteği gelirse önce `dbstat`/`page_count` ile dokunulan sayfayı ölç.

**Gotchas (fiilen yaşananlar):** ANALYZE hiç koşmamıştı → skip-scan kapalı, 54× fark (08-18 sondajı) — hat hijyeni 08-22'de eklendi · "küçük veri → her şey seq scan" varsayımı YANLIŞ: SQLite ANALYZE'siz küçük veride bile AUTOMATIC INDEX kurar · tarama-plan `hat` sırasında ANALYZE'den ÖNCE koşar ki "stat1 yok" durumu da kaydedilsin (sıra sözleşmedir) · LIKE 'core/%' SEARCH değil (case/ICU koşulu) → aralık yüklemi · Apple derlemesi sqlite sürüm damgası `sqlite_source_id()` ile tam alınır (sürüm farkı kör noktası) · `sqlite3_stmt_status` sayaçlarına stdlib'ten erişim yok (ctypes; İB-36 opsiyonel).

**Süpersede zinciri:** "seçicilik %5-10 üstünde seq scan" folklor kuralı → **yerini aldı: 2026-08-21 Karar 64 — yüzde kuralı yazılmaz, karar değişkeni dokunulan sayfa** · "silver yenilemesi sonrası bakım gerekmez" (örtük) → **yerini aldı: 2026-08-22 İB-26 hat-içi ANALYZE+PRAGMA optimize**.

**Bağlantılar:** [[baglam-veri-ambari]] (OLTP/OLAP ayrımı, parquet KB-55) · [[silver-saglik]] (aynı hatta bayrak/kuyruk) · [[pointer-sistemi]] (adresli erişim) · kaynaklar: `cc/rapor-2026-08-18-3.md` · `cc/pipeline-2026-08-18-tarama-yontemleri.md` · `KILAVUZ.md` · `tools/tarama-plan.py`. · [[dil-secimi]] (karşı-link 08-26) · [[kolon-katmani]] (karşı-link 08-29)
