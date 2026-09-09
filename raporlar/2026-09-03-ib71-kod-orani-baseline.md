# İB-71 — Kod/İçerik Oranı Baseline Ölçümü

> **ÜSTÜNE-NOT 2026-09-09 (Karar 88 M15):** bu baseline `.venv` dahil ölçüldü — ESKİ ÖLÇÜM; gitignore-süzgeçli yeni sayım: kod 89 / md 784 / diğer 98 (veri/kod-orani.jsonl 2026-09-09 satırı).

**AS-OF: 2026-09-03 · git_head: 96ed98d** — üretici `tools/kod-orani-olcum.py`, tek kütük satırı `veri/kod-orani.jsonl` (append-only, bu koşumun satırı `tarih=2026-09-03`). Test `tools/testler/test_kod_orani.py`: 8/8 yeşil. Tur önerisi yok — bu rapor yalnız ölçümü taşır, karar/öneri masa/Fable işidir.

## Yöntem (özet)

İki ayrı ölçüm, aynı 4 kova (uzantı bazlı): **md** (.md) · **kod** (.py/.sh/.sql) · **yapisal** (.json/.jsonl/.csv) · **diger** (geri kalan her şey).

1. **Repo envanteri:** `~/jarvis` altında `.git`, `veri/bronz`, `veri/gorunum` HARİÇ tüm dosyalar — dosya sayısı + satır (`\n` bayt sayımı) + bayt, kova başına.
2. **Bağlam-penceresi proxy'si:** `veri/bronz/hareket-olay.jsonl` son 3 gün (eşik ≥2026-08-31) — `arac=="Read"` ∧ `dosya` alanı dolu olan olaylar + `arac=="Bash"` içinde cat/head/tail/sed/less/more/nl/awk sonrası regex'le çıkarılan dosya yolları. Kütükte satır-bazlı okuma miktarı alanı YOK (yalnız `okuma_tipi`: aralik/butun) → ağırlık **dosya-sayımı** (görev metninin "yoksa dosya-sayımı olarak say" dalı).

## Tablo 1 — Repo-genel içerik oranı (dosya sayısı)

| kova | dosya | % | satır | % | bayt |
|---|---:|---:|---:|---:|---:|
| md | 831 | 1,6% | 105.079 | 0,3% | 16.675.463 |
| kod | 18.040 | 33,9% | 8.295.984 | 26,9% | 307.146.253 |
| yapisal | 793 | 1,5% | 7.563.387 | 24,5% | 2.824.340.680 |
| diger | 33.591 | 63,1% | 14.864.482 | 48,2% | 2.799.265.568 |
| **toplam** | **53.255** | 100% | **30.828.932** | 100% | **5.947.427.964** |

## Tablo 2 — Bağlam-penceresi (son 3 gün, 204 okuma-olayı) — dosya sayımı

| kova | dosya-sayımı | % |
|---|---:|---:|
| md | 74 | 36,3% |
| kod | 50 | 24,5% |
| yapisal | 19 | 9,3% |
| diger | 61 | 29,9% |
| **toplam** | **204** | 100% |

## Fark (ilk gözlem, hüküm değil)

Bağlam-penceresinde **md** payı repo-genele göre çok daha yüksek (36,3% ↔ dosya-bazlı 1,6%) — Salih'in okuduğu dosyalar orantısız md-ağırlıklı. **yapisal** payı da tersine düşük (9,3% ↔ satır-bazlı repo 24,5%) — büyük jsonl/csv dosyaları dosya-sayımıyla ölçüldüğünde küçük görünüyor (ağırlıklandırma satır-bazlı olsaydı fark büyür).

## Karşılaşılan belirsizlikler / dikkat

- **`.venv` gizli-klasörü DIŞLANMADI:** görev metni yalnız `.git`/`veri/bronz`/`veri/gorunum` hariç tutulmasını istedi; `.venv` (35.181 dosya, `.gitignore`'da `**/.venv/`, `git ls-files` = 1.114 dosya) hariç tutulmadı. Repo envanterindeki **kod** (18.040 dosya) ve **diger** (33.591 dosya) sayıları büyük ölçüde `.venv` içeriğinden şişmiş olabilir — repo-genel Tablo 1 gerçek "Jarvis kaynak içeriği"nden ziyade disk üzerindeki tüm ağacı yansıtıyor. Git-izlenen dosya sayısı yalnız 1.114; gerçek oran ölçümü isteniyorsa `--repo` yerine `git ls-files` tabanlı bir varyant ya da ek dışlama (`.venv`, `node_modules`, `.obsidian` vb.) masaya konmalı.
- Bağlam-penceresi Bash-kaynaklı dosya çıkarımı **heuristik regex**tir (cat/head/tail/sed… sonrası uzantılı token); komut içinde `echo`/heredoc gibi dosya-okuma OLMAYAN kalıpları yanlışlıkla eşleştirmiş olabilir — kesin sayaç değil, yaklaşık proxy.
- `hareket-olay.jsonl` şemasında satır-bazlı okuma miktarı alanı yok (yalnız `okuma_tipi`: aralik/butun); bu yüzden ağırlıklandırma dosya-sayımına düştü — görev metninin izin verdiği dal.

## Kaynak

Script: `tools/kod-orani-olcum.py` · Test: `tools/testler/test_kod_orani.py` (8/8) · Kütük: `veri/kod-orani.jsonl` (append-only, bu satır dahil).
