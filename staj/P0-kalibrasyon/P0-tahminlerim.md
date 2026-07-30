# P0 Tahminlerim — Salih (tarih: 2026-07-29, chat üzerinden, kâtip: Carvis)

*KOŞUM NOTU (m.29 deneysel): P0 soğuk koşulamadı — Salih beyanı "soruları anlamadım, temelden alalım" (07-29). Önce 6 bloklu SQL çekirdek dersi verildi (SELECT/WHERE/NULL · LEFT JOIN · JOIN · GROUP BY/COUNT · alt sorgu/NOT IN · SUM+JOIN şişmesi), ARDINDAN set chat'te tek-satır-cevap formatıyla koşuldu. Skor DERS-SONRASI etiketlidir; soğuk baseline değildir. Format revizyonu Salih emri: dosya/uzun yazım yok, chat ana yüzey, cevaplar kısa, kayıt Carvis'te.*

## SQL (ders-sonrası: 7/10)
- S1: YANLIŞ — "3 satır, tuzak COUNT sütunu" dedi; doğru 2 satır, tuzak WHERE'in LEFT JOIN korumasını öldürmesi. (Blok 4'te işlenmişken 20 dk sonra kaçırdı.)
- S2: DOĞRU — 0 satır, NOT IN + NULL.
- S3: DOĞRU — 6/5/5.
- S4: DOĞRU — 3 satır, Toyota çift sayım (JOIN şişmesi).
- S5: DOĞRU — 5, NULL iki daldan da düşer.
- S6: DOĞRU — tek satır, alıcı 2 (kova mantığı doğru).
- S7: DOĞRU — 2, BETWEEN uçları dahil.
- S8: YANLIŞ — "id'si NULL araç yok" dedi; anti-join desenini tanımadı, dolgu-NULL kavramı yeniydi. Doğru: Can.
- S9: DOĞRU — 4-3.
- S10: YANLIŞ — Mehmet'i (sehir NULL) içeri aldı; doğru 2 satır. Blok1-kapı hatasının tekrarı.

**Hata deseni:** 3 yanlışın 3'ü NULL-WHERE ailesi (dolgu-NULL dahil). Tekrar kuyruğu: S1, S8, S10 → 07-30 soğuk dokunuş.

## Python (2026-07-29, aynı vardiya devamı)
*Koşum notu: 6 bloklu Python çekirdek dersi verildi (etiket/referans · mutable-default · try-except-pass · float · pandas filtre/NaN/groupby/merge · kopya-vs-.loc). Orijinal PY setinin cevapları ders içinde açığa çıktığı için sınav VARYANT setle koşuldu (V1-V10, Carvis üretimi — README kuralı: pratik soruları sınavda tekrar kullanılmaz). Orijinal PY1-PY10 tekrar kuyruğuna soğuk-malzeme olarak kaldı.*

**Varyant set: Paket 1 → 3,5/5** (V1 yarım: desen doğru, liste tam yazılmadı · V2 ✓ · V3 açıklama istedi, NaN-filtre → sayılmadı · V4 ✓ · V5 ✓). **Paket 2 → koşulmadı** — Salih yorgunluk beyanı ("bitirelim"); V6-V10 cevapları motor-okumasıyla ANLATILDI, ölçülmedi.

**Hata/boşluk deseni (Python):** pandas motor-okuması henüz kendi başına akmıyor (V6-V10'da "nasıl okunur bilmiyorum" beyanı); saf Python referans/mutasyon oturdu. Tekrar kuyruğu: orijinal PY1-PY10 soğuk koşum + NaN-filtre (V3) → sonraki staj vardiyası.

## Doğrulama sonrası
- SQL ders-sonrası: 7/10 · Python varyant P1: 3,5/5, P2 ölçülmedi — SOĞUK BASELINE HÂLÂ YOK; ilk soğuk ölçüm sonraki vardiyada tekrar-kuyruğuyla alınacak.

## Python
- PY1:
- PY2:
- PY3:
- PY4:
- PY5:
- PY6:
- PY7:
- PY8:
- PY9:
- PY10:

## Doğrulama sonrası
- SQL baseline: __/10 · Python baseline: __/10
- 2+ yanlış verdiğim hata sınıfları:
- Tekrar kuyruğu (27-28 Tem):
