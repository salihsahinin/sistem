# Pipeline Durumu — Erişim katmanı FTS5+BM25 (İB-43 icrası; KB-43 (a) = Karar 60 · Karar 66 ölçüm-kolu şartnamesi) · 2026-08-22 seans-14 (icra oturumu, Carvis/Fable, oturum 11b49d44)

*Künye: karar `veri/karar-borcu.jsonl` KB-43 → Karar 60 (08-21: FTS5-önce, embedding'siz iki iyileştirme, hibrit/vektör kararı İB-20 yerel eval'den SONRA; Beyan 9 baki) + Karar 66 (08-22: vektör ÖLÇÜM KOLU şartnamesi İB-47 — paralel seans-13 kalemi, bu manifestin eval iskeletine EKLENİR). Araştırma `cc/rapor-2026-08-17-2.md` (A-YT6/C-YT1/C-YT3; qmd B4-1). Salih emri 08-22: "kararımın gerekmediği icra borcu varsa tespit et devam et". Koşum-önü kapı: FTS5 mevcut (sqlite 3.51.0 ENABLE_FTS5; bm25 testi PASS) · paralel oturum İB-48/49 graf şeridinde, bu kalemde DEĞİL (transkript 19:07) · manifest/git log'da önceki koşum yok. Paralel oturum canlı → commit'ler yollu `git add`.*

## Kapsam (KB-43 (a) → kod; deterministik, stdlib, LLM/embedding YOK)
| SH | ne | kanıt (done-yüklemi) | durum |
|---|---|---|---|
| SH-0 | Manifest + ledger SAHADA | bu dosya + İB-43 `not` | ✅ |
| SH-1 | `tools/erisim-fts.py`: silver additive `erisim_genisletme` (kayit başına anahtar-genişletme metni = referans değerleri [anahtar_terim/tuzuk_madde/kart/skill/v_no/wiki/etiket] + dosya başlığı + bölüm yolu + zaman) · FTS5 sanal tablo `kayit_fts` (metin + genisletme; unicode61 remove_diacritics 2; bm25 ağırlık genişletme 2×) · sorgu: sözcük-önek eşleme + ZAMAN-FARKINDALI genişletme (sorgudaki açık tarih → zaman filtresi; "güncel/son" → sıcak/ılık + yeni-önce) · `--sorgu` CLI · katman-hatti adımı `erisim` | index kurulur; 2 koşum aynı sonuç; hat OK | ⏳ |
| SH-2 | İB-20 eval iskeleti: `veri/sozlesme/erisim-eval-sorular.jsonl` (5 yetenek: bilgi-çıkarma · çok-oturum · zamansal · bilgi-güncelleme · çekimserlik; beklenen dosya + opsiyonel kayit regex) · yöntemler: `grep` (taban: AND alt-dize, katman-öncelikli) · `fts5` (yalnız metin) · `fts5+gen` (metin+genişletme+zaman) · metrik recall@5 · MRR · süre · COST tabanı (FTS5 ↔ grep) · kütük `veri/erisim-eval.jsonl` append-only (1 satır = soru × yöntem × koşum) + gold `v_erisim_eval` CSV; yöntem sütunu vektör/RRF kollarına AÇIK (İB-47) | eval koşar, sayılar kaynaklı; hibrit kararı bu sayıyla masaya (KARAR DEĞİL) | ⏳ |
| SH-3 | SCRIPTLER · veri/README · ledger İB-43 (kısmen/kapandı + kalan) · manifest T beyanı · kapsül | dosyalar | ⏳ |

## Kapsam DIŞI
Vektör kolu (İB-47, paralel oturum; bu iskelete `yontem='vektor'|'rrf'` satırı olarak eklenir) · LLM-rerank · hibrit KARARI (Karar 60 sırası: ölçümden sonra masa) · altın-soru kümesinin ≥100'e büyütülmesi (Karar 66 şartı; v0 tohum ~25 soru, Carvis-yazımı → Salih teyidi gerekir: gold cevaplar kanıt değil kestirim).

## Kütük
- 19:12 açılış.
