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

---

# SOĞUK BASELINE — 2026-07-30 (staj şeridi, chat-ana-yüzey, kâtip: Carvis)

*İlk gerçek soğuk koşum. Referanssız, çalıştırmadan, ders ÖNCESİ. Salih "A" seçti (hatırlatma talebi reddedilmedi, ölçüm sonrasına ertelendi — m.16 kapısı işletildi).*

## Blok 1 — SQL tekrar kuyruğu (S1·S8·S10 = bilerek en zayıf aile) → 0,5/3
| # | Tahmin | Gerçek | Sonuç |
|---|---|---|---|
| S1 | 2 satır: Zeynep 3, Ayse 4 | Ayse 1, Zeynep 1 | **yarım** — LEFT JOIN+WHERE tuzağı YAKALANDI (satır sayısı+isimler doğru); `COUNT(s.id)` sayı değil id sanıldı |
| S8 | hiçbir şey dönmez | Can | **yanlış** — anti-join deseni (`WHERE a.id IS NULL`) S1 dersinin TERS uygulanması |
| S10 | Ayse, Mehmet, Zeynep | Ayse, Zeynep | **yanlış** — `NOT (sehir='Ankara')` NULL'da "bilinmiyor" üretir, satır düşer (üç değerli mantık) |

Geri-anlatım kapısı: "LEFT JOIN + WHERE olduğu için" → **REDDEDİLDİ** (S1'i açıklamıyor). Doğru ayırt edici: OPERATÖR. `IS NULL` ölçer · `=` `<>` `>` `IN` NULL'da satır düşürür. Taşınabilir kural: **NULL'ı IS ile sorarsan cevap alırsın, = ile sorarsan satırı kaybedersin.**

## Blok 2 — Python PY1-PY10 (soğuk, orijinal set) → 6,5/10
| # | Tahmin | Gerçek | Sonuç |
|---|---|---|---|
| PY1 | 4 | 4 | ✓ |
| PY2 | len(arac)'a eşit değil; "4 satır, her eşleşme için 1" | Ankara 3·Istanbul 1·Izmir 1 = 5 ≠ 6 | **yarım** — eşitsizlik doğru, gerekçe PY1'den kopyalandı; `groupby(dropna=True)` None anahtarı gruba SOKMAZ |
| PY3 | değişmez, kopyaya yazdık | 380000 | ✓ gerekçe dahil |
| PY4 | [1] sonra [1,2] | [1] / [1,2] | ✓ (mutable default tek nesne) |
| PY5 | unuttum | [] | **0** — KeyError'ı `except: pass` yuttu; sessiz boş sonuç |
| PY6 | False / 2.67 | False / 2.67 | ✓ |
| PY7 | 4 (mekanizma soruldu) | 4 | ✓ — NaN karşılaştırmada False, maskeden düşer |
| PY8 | 3 | 3 | ✓ (b=a aynı nesne) |
| PY9 | "farklı araba sayısı kadar müşteri" | {'Toyota':6,'Honda':5,'Ford':4,'Renault':7,'Fiat':4} | **0** — `len(m)` marka STRING'inin harf sayısı; sayım değil |
| PY10 | 0 | 1 | **0** — `fillna` yeni Seri döndürür, yerinde değiştirmez (PY3'ün AYNI ailesi, orada doğru bilindi) |

## Baseline
- **Tekrar kuyruğu (SQL, en zayıf aile): 0,5/3 = %17 → tamir BAŞARISIZ**
- **Yeni-görülmemiş (Python): 6,5/10 = %65**
- **Toplam: 7/13 = %54 → <%60 ⇒ 07-29 kuralı gereği P0 YENİDEN AÇILIR (statü kararı Salih'te; Carvis önerisi: dar yeniden-açma = yalnız NULL/NaN ailesi)**

## Hata ailesi sınıflaması (2+ yanlış)
1. **NULL/NaN sessiz satır düşürme — HÂKİM AİLE (S1 yarım·S8·S10·PY2):** SQL `=`/`NOT` · pandas `groupby(dropna)`. PY7 (NaN maske) doğru bilindi → kısmi oturma; köprü kuruldu ama tek yönlü.
2. **"Yeni nesne mi, yerinde mi" (PY3 ✓ / PY10 ✗):** aynı mekanizma, tutarsız cevap ⇒ kural değil örnek ezberlenmiş. `fillna`/`dropna`/`sort_values` inplace-değil listesi tekrar kuyruğuna.
3. **Sessiz yakalanan hata (PY5):** `except: pass` → boş sonuç. Staj rolünün çekirdek örneği, ders içinde de geçmişti, soğukta hatırlanmadı.
4. **Gerekçe kopyalama (PY2, S8, geri-anlatım kapısı):** doğru sonuç + yanlış mekanizma deseni. Ölçüm notu: sonuç doğru olduğunda mekanizma SORULMALI, yoksa skor yanıltır.
5. **Kod-okuma yerine anlam-tahmini (PY9):** `len(m)` okunmadan "sayım olmalı" varsayıldı. Ajan çıktısı doğrulamada en tehlikeli refleks.

## Tekrar kuyruğu (2 Ağu'da soğuk, varyant setle)
S1/S8/S10 varyantları · PY2 · PY9 · PY10 · inplace-değil listesi · `except: pass`

*Damga: beyansız. Skor uydurulmadı; ölçülmeyen kalem yok — 13/13 kalem koşuldu.*

## P0 STATÜ KARARI — Salih, 2026-07-30
**Yeniden açma YOK.** Kaldığımız yerden ilerlenir; tekrar, ilerleyen konuların içine gömülü sorularla yapılır. Gerekçe (Salih): AWS/P3 hattı da girecek, ayrı geri-sarma için vakit yok.
- 07-29 kuralı (<%60 → P0 yeniden açılır) Salih kararıyla **geçersiz kılındı**; kural metni arşiv değeri için duruyor (m.8).
- Carvis şerhi: eşik düşürülmedi, ÖLÇÜM ertelendi — NULL/NaN ailesi %17'de kaldı ve sahipsiz kalırsa hiç kapanmaz. Karşı-önlem: **bakım vergisi P2+ sınav setlerinin İÇİNE gömülür** (her sette ≥2 kalem NULL/NaN + ≥1 kalem inplace-değil, varyant değerlerle). Ayrı oturum, ayrı zaman yok — sahiplik Carvis'te, README "3 günden fazla ara yok" kuralı bu yolla karşılanır.
- Yeniden ölçüm: P6 soğuk provası (9-10 Ağu) tek gerçek kapı olur.
