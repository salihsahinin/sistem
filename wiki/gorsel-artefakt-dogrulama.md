# Görsel Artefakt Doğrulama

**Tanım:** Üretilen görsel artefakt (SVG/HTML/diyagram) "hata vermedi" diye doğrulanmış sayılmaz; okunabilirliği, artefaktı üreten aracın kendi gözüyle değil **bağımsız bir ölçümle** sınanır — tarayıcıda bbox ölçüp taşma / metin-çakışması / kırık referans taranır.
**Durum:** GÜNCEL · **Son teyit:** 2026-08-12 · **Kaynaklar:** staj oturumu 08-12 canlı vaka (7 şekilli öğrenme HTML'i; Salih yazılı izniyle metot olarak ingest — staj verisi taşınmadı, md.49) · **Güven:** ORTA (tek vaka; mekanizma doğrudan ölçüldü, genelleme henüz sınanmadı)

## Çekirdek

Görsel artefaktın kendine özgü bir sessiz hata sınıfı vardır: **dosya üretilir, sözdizimi geçerlidir, tarayıcı hata vermez — ama şekil okunamaz.** Metin kutunun dışına taşmıştır, iki etiket üst üste binmiştir, ok başı görünmez kalmıştır. Derleyici yoktur, test yoktur, uyarı yoktur. Kod tarafındaki *sessiz mantık hatası*nın artefakt tarafındaki tam karşılığıdır.

Göz kontrolü bu sınıfı güvenilir biçimde yakalamaz: ekran görüntüsü sayfanın yalnız bir bölümünü gösterir, uzun sayfada her şekli tek tek gezmek pahalıdır, panel/render katmanı bazen hiç görüntü vermez (ölü döngü riski: doğrulanamayan artefakt "doğrulandı" sanılır).

Çözüm ölçmektir: tarayıcıda DOM'dan her metnin `getBBox()` değeri alınır ve üç şey taranır — (1) metin `viewBox` sınırlarını aşıyor mu, (2) iki metnin kutusu kesişiyor mu, (3) `marker-end`/`url(#id)` referansları aynı belgede çözülüyor mu. Üçü de sayıya iner, üçü de göz gerektirmez.

**Kanonik örnek (damıtılmış):** 7 şekilli bir anlatım dosyası üretildi; tarayıcı paneli görüntü vermiyordu, göz kontrolü imkânsızdı. Bbox taraması tek koşumda iki gerçek arıza çıkardı: bir şekilde iki etiket 96 piksel üst üste biniyordu, ve 10 ok başı `fill="context-stroke"` kullanıyordu (bazı tarayıcılarda görünmez kalır). İkisi de düzeltildi, ikinci tur `{badMarkers:[], overlaps:[], overflow:[]}` döndü. Panel hiç açılmadan artefakt doğrulandı.

## SOP — görsel artefakt ürettikten sonra

1. Artefaktı tarayıcıya yükle (dosya ya da data URL fark etmez).
2. Denetimi **koştur, gözle bakma** — her `<svg>` için: metin bbox'ları `viewBox` içinde mi · metin-metin kesişimi var mı (birkaç piksel tolerans) · her `marker-end` referansı aynı `<svg>` içinde çözülüyor mu.
3. Çıktı boş liste değilse düzelt ve **yeniden koş** — tek turluk doğrulama yoktur.
4. **Tazelik kapısı:** denetim, diskteki son sürümü okuyan bir sayfada koşmalı. Bayat sekme "temiz" der; sayfayı yenilemeden verilen temiz sonuç kanıt değildir (aşağıdaki gotcha).
5. Sonucu kayda geç: neyin ölçüldüğü + kaç arıza çıktığı. "Doğrulandı" tek başına bilgi taşımaz.

## Gotchas

- **Bayat sekme yanılgısı (08-12 canlı vaka):** denetim, dosyanın diske yazılmasından önce yüklenmiş bir sayfada koştu ve düzeltilmiş referansları "kırık" gösterdi. Ters yönü daha tehlikeli: eski temiz sürüm üzerinde koşan denetim, yeni arızayı hiç görmez. **Denetimden önce sayfanın diskteki sürümü yansıttığını doğrula.**
- **Ekran görüntüsü ≠ doğrulama:** görüntü sayfanın tek ekranını kapsar; 7 şekilli bir dosyada 1 şekle bakıp "iyi görünüyor" demek örneklem hatasıdır.
- **Render katmanı kaybolabilir:** panel gizlenir, kaydırma zaman aşımına düşer, görüntü boş döner. Göz kontrolüne bağımlı bir doğrulama planı bu durumda çöker; ölçüm tabanlı olan çalışmaya devam eder.
- **`context-stroke` / `context-fill`:** ok başını çizginin rengine bağlamanın kısa yolu, ama tarayıcı desteği tekdüze değil — ok başları sessizce kaybolabilir. Güvenli yol: marker'ı sınıfla renklendir, renk sayısı kadar ayrı marker tanımla.
- **Kesişim toleransı:** 1-2 piksellik örtüşme tipografik olarak zararsızdır; eşik konmazsa denetim gürültü üretir ve okunmaz hale gelir.
- **Yalnız metin ölçmek eksik:** bu tur metin-metin kesişimini taradı; metin-çizgi ve kutu-kutu örtüşmesi hâlâ ölçülmüyor. Kapsam sınırı açıkça yazılmazsa "temiz" fazla söz vermiş olur.

## Süpersede zinciri

— (ilk sürüm)

## Bağlantılar

[[adversarial-hayatta-kalma]] (aynı damar: iddia kendi üreticisinin gözüyle değil bağımsız sınamayla ayakta kalır) · [[olcum-banki]] (denetim çıktısı sayıya iner — arıza sayısı kaydedilebilir bir ölçüm) · [[pointer-sistemi]] (kanonik örnek damıtıldı; ham vaka staj günlüğünde `gunluk/2026-08-12.md`) · ingest kaydı: `kuyruk/gelen-2026-08-12-staj-hasadi.md`
