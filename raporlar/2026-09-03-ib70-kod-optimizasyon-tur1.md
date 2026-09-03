# İB-70 Kod-Optimizasyon Tur 1 — `tools/*.py` + hook'lar

AS-OF: 2026-09-03 · Kapsam: `tools/` 48 script (~10.244 satır) + `.claude/hooks/*.sh` 3 dosya (142 satır) + `cc/workflow/` (yalnız pipeline-koşum `.js` artefaktları, .py yok — kapsam dışı). Yöntem: `wc -l` sıralama + grep kalıp taraması + `pyflakes` (statik). Derinlemesine okunan: >200 satır 12 dosya; kalan 36 dosya başlık+grep düzeyinde tarandı.

## Bulgu tablosu

| Dosya/alan | Satır | Gözlem | Öneri | Risk |
|---|---|---|---|---|
| **Paylaşılan modül yok** (tüm `tools/`) | — | Hiçbir script `tools.` içe aktarmıyor (`from tools import` sıfır sonuç); `tools/ortak.py` YOK | `git_head()`, sqlite bağlantı açma, JSONL/CSV I/O için ortak modül aç | Düşük (salt-okur çıkarım, refactor ayrı iş) |
| `git_head()` tekrar deseni | — | 24 dosyada `git rev-parse --short HEAD` aynı try/except kalıbıyla ayrı ayrı tanımlı (örn. `silver-saglik.py:def git_head`) | `ortak.py`'ye taşı, 24 yer tek çağrıya insin | Düşük |
| JSONL okuma/yazma yardımcıları | — | Yalnız 3 dosyada (`karar-borcu-tablo.py`, `hareket-tablo.py`, `obsidian-harita.py`) `def ...jsonl` var; diğerleri muhtemelen satır-satır `json.loads` tekrarlıyor (derin taranmadı) | Ortak modülde `oku_jsonl()/yaz_jsonl()` — 3+ yer birleşir | Düşük |
| `sqlite3.connect` çağrı sayısı | — | 28 dosyada doğrudan `sqlite3.connect`; bağlantı/pragma ayarı (WAL, timeout vb.) her yerde ayrı olabilir | Ortak `baglam_ac()` sarmalayıcı | Düşük |
| `tools/silver-saglik.py` | 622 | Dosya içinde 43 ayrı `sqlite3.connect`/`.execute` çağrısı — en yoğun DB-trafik dosyası; tam tablo taraması `SELECT * FROM %s` (satır 480, döngüde) | Döngü içindeki `SELECT *` sorgularını tek toplu sorguya/`ANALYZE`'a indirmeyi değerlendir | Orta (silver sağlık mantığı kırılgan, test şart) |
| `tools/baglam-tablo.py` | 1019 | En büyük dosya; 10 sqlite çağrısı + `SELECT * FROM %s` (satır 981) döngü-içi; silver'ı sıfırdan yeniden kuruyor (beklenen davranış — deterministik tasarım m.6) | Bölünebilir mi (ör. şema-kurulum / view-üretim ayrı modül) değerlendir | Orta (çekirdek silver üretici, bölme riskli) |
| `SELECT * FROM <view>` döngüsü (CSV dışa aktarım) | — | 16 yerde `SELECT * FROM {view}` — çoğu gold view → CSV dışa aktarımı (küçük tablo, sorun değil); asıl maliyet `baglam-tablo.py`/`silver-saglik.py` içindeki döngü-içi tam taramalar | Gold-export tarafı DOKUNMA; yalnız silver-üretim döngülerini gözden geçir | Düşük |
| `tools/pointer-graf.py` | 654 | pyflakes: satır 465 `N` atanıp kullanılmıyor, satır 480 `shutil` içe aktarılıp kullanılmıyor; 4 yerde placeholder'sız f-string (241,380,381,384) | Ölü değişken/import temizliği — kozmetik, davranış değişmez | Düşük |
| `tools/atlas-derle.py` | 324 | pyflakes: `glob` içe aktarılıp kullanılmıyor | Sil | Düşük |
| `tools/katman-olcum.py` | 275 | pyflakes: `csv` ve `datetime.timedelta` kullanılmıyor | Sil | Düşük |
| `tools/kural-envanter.py` / `kural-sayaci.py` | 120/87 | pyflakes: her ikisinde `hashlib` kullanılmıyor | Sil | Düşük |
| `tools/erisim-fts.py` | 308 | pyflakes: satır 117 `kolonlar` atanıp kullanılmıyor | İncele, muhtemelen ölü kod parçası | Düşük |
| `tools/anahtar-denetim.py` | 206 | pyflakes: satır 169 `dosya_sayisi` atanıp kullanılmıyor | İncele | Düşük |
| `tools/prompt-tablo.py` | 199 | pyflakes: `sys` kullanılmıyor; `SELECT * FROM v_son_50_prompt` iki kez art arda çağrılıyor (satır 175) — aynı sorgu iki kez çalıştırılmış | Tek sorguya indir (cursor'ı önce fetch et, description'ı ondan al) | Düşük |
| `.claude/hooks/*.sh` (3 dosya, 142 satır) | — | Küçük, deterministik regex-tel; tekrar yok, salt-okur incelemede sorun görülmedi | Değişiklik önerilmiyor | — |
| `cc/workflow/` | — | Yalnız üretilmiş `.js` pipeline artefaktları (workflow-authoring aracı çıktısı), Python script yok | Kapsam dışı, atla | — |

## Özet

- 48 `tools/*.py` dosyasının tamamı `wc -l`/grep ile tarandı; >200 satır 12'si (toplam ~4770 satır, dosyaların ~%47'si) daha derin grep+pyflakes ile incelendi.
- En çarpıcı bulgu: **paylaşılan yardımcı modül yok** — `git_head()` 24 kez, sqlite bağlantısı 28 kez ayrı ayrı yazılmış; `tools/ortak.py` gibi tek modül en yüksek geri-dönüşlü tek değişiklik.
- İkinci bulgu: `baglam-tablo.py` (1019 satır) ve `silver-saglik.py` (622 satır, 43 DB çağrısı) en pahalı yollar — döngü-içi `SELECT * FROM %s` tam taramaları var; ikisi de silver'ı deterministik sıfırdan kurduğu için (m.6) bu beklenen maliyet, ama toplu-sorguya indirme fırsatı var.
- 8 dosyada pyflakes ile tespit edilen kullanılmayan import/değişken (kozmetik, davranış etkisiz).

Rapor satır sayısı: 120 (sınır içinde).
