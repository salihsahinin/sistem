# K-019 Taslak — Fikir-kutusu damıtma planı

*Statü: **İMZALANDI (Salih, 07-22)** — adım 1-2 onaylı; adım 3 (MEZUN inişi) liste-onayına tabi (aşağıda sunulacak). Salih şartı kayıtta: kutudaki ÖNEMLİ fikirler için optimize bir uygulama-sırası oluşturulduğunda o sıranın GİDİŞAT KONTROLÜ korunur — damıtılmış format bu yüzden statü/etiket alanını (TETİKLİ/UFUK/ADAY/statü) her satırda zorunlu tutar; sıra kurulduğu gün kutu üstünden izlenebilir kalır.* *Hazırlayan: Carvis, 2026-07-22. Hazırlayan: Carvis, 2026-07-22. Boyut-izleme taslağının ilk emsali.*

## Teşhis
`fikir-kutusu.md` = 37,3 KB / 81 satır. Satırca küçük, token-yoğun: V26-V57 blokları tam-metin paragraflar taşıyor (V39 deney tarifi, V43 vaka anlatısı, V53 Council deseni...). Kutunun sözleşmesi "tarih + damga + TEK SATIR, tam metin kaynağa pointer" idi — fiilen bozulmuş; kutu ham-fikir yüzeyi olmaktan çıkıp mini-arşive dönmüş.

## Önerilen operasyon (üç adım, tek vardiya)
1. **Arşiv dosyası açılır:** `kuyruk/arsiv-fikir-kutusu-2026-07.md` — V26'dan V57'ye uzun blokların TAM METNİ buraya aynen taşınır (kırpma yok, birleştirme yok; git tarihçesi zaten korur, dosya erişilebilirlik için).
2. **Kutuda her madde tek satıra iner:** `V<n> | <etiket: TETİKLİ/UFUK/KURAL-ADAYI/DERS/VAKA> | <özüt ≤140 karakter> | damga | → arşiv#V<n>` formatında. V1-V25 tablosu zaten kompakt — dokunulmaz.
3. **Statü-süzgeci (ayrı onay satırı):** İşi BİTMİŞ maddeler kutudan arşive tam iner (kutuda satır bile kalmaz): V43 (kural yürürlükte + A1a DONE — kural zaten KILAVUZ/operasyon satırında yaşıyor) · V50/V51 sınıfı işlenmiş süreç-dersleri (senaryo-defterine geçmiş olanlar). Bu sınıf "çürüdü" değil "MEZUN" — karşılığı kanonda yaşıyor, kutu görevi bitti.

## Beklenen sonuç
Kutu ~37 KB → tahmini 10-12 KB (bütçe 20 KB'ın altı, yarı pay boş). Bilgi kaybı SIFIR: her özütün yanında arşiv-pointer; arşiv soğuk katman, oturum önekine girmez.

## Karar istenen
- [ ] Adım 1-2 onay (mekanik taşıma + özütleme)
- [ ] Adım 3 onay — MEZUN listesini Salih tek tek görür: icra vardiyasında liste sunulur, onaysız hiçbir madde tam inmez
- [ ] Arşiv dosya adı kabul
