# IB-53 · MASKELİ HAKEM RAPORU — Aile C (pipeline / IR emsalleri)

## KÜNYE

| Alan | Değer |
|---|---|
| Rol | Maskeli hakem (aile C) — üretici koşumlardan bağımsız; kıyas kimliğe değil İDDİA+KANIT içeriğine göre |
| Tarih | 2026-08-29 |
| Girdiler | `scratchpad/hakem-c/rapor-1.md` (TEZ, 55 iddia, 37 emsal) · `scratchpad/hakem-c/rapor-2.md` (ANTİTEZ, 22 kırpılmış iddia üzerinde ¬T taraması) |
| Bağımsız denetçi sondajı | rapor-1: SCIP range 3/4-eleman, SCIP "10%-20%", SourcetrailDB 1-tabanlılık, MDN opak-origin → birebir doğru; TEK EKSİLTME: SCIP `range` alanı kaynak protoda `deprecated` işaretli, rapor-1 anmıyor. rapor-2: Pandoc `sourcepos` (satır:sütun taşır), file:// altında `<script src>` yerel veri yükleme izni, Backstage `builder:'local'` varsayılanı → birebir doğru |
| Verdikt ölçeği | SAĞLAM = adversarial taramadan değişmeden çıktı · DARALDI = mekanizma çekirdeği ayakta, kapsam/niceleyici daraltıldı (daraltılmış form AYNEN yazılır) · DÜŞTÜ = iddia yanlışlandı · ÇELİŞKİLİ = iki rapor uzlaştırılamaz karşıt kanıt taşıyor · KARARSIZ = iki tarafta da karar verdirecek kanıt yok |
| Usul notu | rapor-2, çağıran ajanın kırptığı 22 iddia üzerinde çalışmış; en az bir kırpılmış iddia (md.5 "mozsearch tamamen statik") rapor-1'in gerçek metnine uymuyor — rapor-1 zaten "Hibrit" yazıyor (C19, iddia 20). Bu hüküm rapor-1 aleyhine SAYILMADI; ayrıntı Hakem Notları'nda. |

## VERDİKT TABLOSU

| Kalem | Verdikt | Tek satır gerekçe |
|---|---|---|
| ① Satır-adresli tipli IR olgunluğu + md-taşınabilirliği | **DARALDI** | 9 emsal ayakta ama "olgun/kararlı" düştü (LSIF emekli, SCIP range deprecated + org taşınması, rustdoc unstable); md'ye taşınan format değil desen — md'nin yerli yolu var (mdast/unist + Pandoc sourcepos) |
| ② file:// kısıtı ve kaçış yolları | **DARALDI** | Kısıtın kendisi sağlam (opak origin, fetch bloklu); rapor-1'in "iki kaçış yolu" sayımı eksik — doğrulanmış üçüncü yol: `<script src>` yerel veri dosyası |
| ③ Statik-önceden-derlenmiş ↔ canlı-sunucu | **DARALDI** | Statiğin kazancı barındırma/dayanıklılıkla sınırlı; arama/xref yükü sunucuya dönüyor; Backstage'in reddi "her istekte yeniden üretim"e özgü, arka-uç üretim varsayılan sevkiyat |
| ④ Diyagram katmanı determinizmi | **DARALDI** | Determinizm koşullu ve konfigürasyonla: Graphviz (sabit sürüm + start'a sayısal-olmayan değer yok), Mermaid (id-düzeyi, deterministicIds:true + #6530 kusuru), D2 (yalnız SVG hattı tarayıcısız) |
| ⑤ VS Code webview desenleri | **DARALDI** | Webview maliyetleri ayakta; "kalıcılık = yüksek bellek" ve "native graf API hiç yok" mutlakları düştü (getState/setState ucuz; SCM Graph native + proposed scmHistoryProvider, üçüncü şahsa kapalı) |
| ⑥a "dosya:satır + layout birleşik IR yok" | **SAĞLAM** | Antitez bilinçli aradı, bulamadı; en yakın aday Sprotty bile satır değil EMF-URI taşıyor — negatif adversarial taramadan güçlenerek çıktı |
| ⑥b "statik↔canlı ampirik çalışma yok" | **DARALDI** | Doğrudan A/B yok (bu kısım ayakta); ama karar değişkeni gecikme üzerinde birinci sınıf kontrollü deneyler var (Liu&Heer 2014, Brutlag 2009) — "hiç çalışma yok" savunulamaz |

**Sayım: SAĞLAM 1 · DARALDI 6 · DÜŞTÜ 0 (kalem düzeyi; alt-iddia düzeyinde 2 düşme, aşağıda) · ÇELİŞKİLİ 0 · KARARSIZ 0 (kalem düzeyi; kalıntılar Hakem Notları'nda)**

---

## KALEM KALEM GEREKÇE

### ① Satır-adresli tipli IR olgunluğu ve md-dünyasına taşınabilirliği — DARALDI

- rapor-1'in çekirdeği (9 bağımsız satır-adresli IR emsali; kod-zekâsı ailesi taşıyor, doc-graph ailesi taşımıyor ayrımı) denetçi sondajından ve antitezden değişmeden çıktı.
- "Olgunluk" cephesinde rapor-2'nin karşı-kanıtı isabetli: Sourcegraph 4.6'da LSIF okuma desteği kaldırılmış; SCIP deposu org değiştirmiş; denetçi eksiltmesi bunu güçlendiriyor — SCIP'in satır adresini taşıyan `range` alanı protoda `deprecated` işaretli ve rapor-1 bunu hiç anmıyor. rustdoc JSON'un unstable olduğunu rapor-1'in kendisi kaydetmişti (iddia 17). Kythe ekip-değişimi kanıtı ise üçüncül (Wikipedia) — tartıya düşük ağırlıkla girdi.
- md-taşınabilirlik cephesinde rapor-2'nin bulgusu kararı değiştiren türden: mdast/unist `Point { line ≥1, column ≥1, offset }` ile md'nin YERLİ satır-adresli tipli IR'i zaten var; Pandoc `sourcepos` denetçi tarafından doğrulandı (satır:sütun taşır). rapor-1 Pandoc hücresini "kanıt bulunamadı, açık" bırakmıştı (N4) — dürüst bırakılmış ama hücre düştü.
- **Daraltılmış form (AYNEN):** "Satır-adresli tipli IR deseni 9 emsalle kanıtlı ve ÇALIŞIR; ama 'olgun/kararlı format' iddia edilemez — LSIF emekli, SCIP'in range alanı deprecated ve yönetişimi çalkantılı, rustdoc JSON unstable, Sourcetrail üst-akımı ölü (çatal canlı). md-dünyasına taşınan şey FORMAT değil DESENDİR; md tarafında yerli üretim yolu zaten vardır: mdast/unist Point (satır/sütun/offset) + Pandoc sourcepos — sourcepos yalnız commonmark/gfm/commonmark_x/djot okuyucularında çalışır, varsayılan markdown okuyucusunda YOK, konumu tip alanında değil data-pos attribute'unda taşır (Div/Span sarmalama maliyeti)."

### ② file:// kısıtı ve GERÇEK kaçış yolları — DARALDI

- Kısıtın kendisi iki raporda ve denetçi sondajında örtüşüyor: modern tarayıcılar yerel dosyaları opak origin sayar, file:// altında fetch/XHR ile yerel JSON/SVG çekimi bloklu (MDN, rapor-1 iddia 29 doğrulandı; rapor-2 md.3 aynı yönde).
- rapor-1'in "belgeli iki kaçış yolu: gömme ya da yerel sunucu" kapanışı eksik çıktı: rapor-2'nin üçüncü yolu denetçi tarafından doğrulandı — Chromium ve Firefox, file:// sayfasının aynı yoldan görsel/normal-script/frame YÜKLEMESİNE (yürütmesine) izin verir; yani veri ayrı bir `veri.js` dosyasında `<script src>` ile sunucusuz yüklenebilir.
- **Daraltılmış form (AYNEN):** "file:// altında fetch/XHR bloklu — bu sert duvar ayakta. Kaçış yolu İKİ değil ÜÇTÜR, koşullarıyla: (a) veriyi HTML'e gömme — her tarayıcıda, tek dosya, veri büyüdükçe dosya şişer; (b) `<script src>` ile ayrı yerel veri-dosyası (veri.js) — Chromium+Firefox varsayılanında, aynı dizin-yolundan, sunucusuz, çok-dosyalı; fetch/WASM/Range gerektirmeyen her yük için geçerli; (c) yerel HTTP sunucusu — fetch, HTTP Range (sql.js-httpvfs) ya da çalışma-anı WASM çeken her şey (Pagefind) YALNIZ burada çalışır. Tarayıcı bayrakları (--allow-file-access-from-files, privacy.file_unique_origin) mimariye temel yapılmaz."

### ③ Statik-önceden-derlenmiş ↔ canlı-sunucu dengesi (yerel tek-kullanıcı) — DARALDI

- rapor-1'in dağılımı (statiğin belgeli kazancı servis maliyeti + dayanıklılık; bedeli bayatlama + yeniden derleme; en zor parça arama) antitezde esasen ayakta kaldı ve rapor-2'nin "en büyük dağıtımlar canlı sunucu" gözlemiyle keskinleşti.
- mozsearch üzerinde iki rapor AYNI sonuçta: statik HTML üretimi + zorunlu canlı arama katmanı = hibrit (rapor-1 C19/iddia-20 bunu baştan yazmış; rapor-2'nin "ÇÜRÜDÜ" hükmü kırpılmış iddia metnine karşı, rapor-1'e karşı değil).
- Backstage cephesinde denetçi-doğrulamalı düzeltme kararı inceltiyor: reddedilen şey HER İSTEKTE yeniden üretim; arka-uçta üretim (`builder:'local'`) kutudan çıkan varsayılan — statik/CI önerisi ölçek gerekçeli, ilkesel değil. Yerel tek-kullanıcı senaryosunda ölçek argümanı uygulanmaz.
- **Daraltılmış form (AYNEN):** "Statik önceden-derleme yerel tek-kullanıcıda savunulabilir (barındırma/dayanıklılık kazancı; ölçek karşı-argümanları bu senaryoda geçersiz), ama 'pratik üstünlük' genellemesi yapılamaz: arama/çapraz-referans yükü ya statikleştirilir (gömülü/parçalı indeks — file:// altında yalnız ②-b yoluyla) ya da küçük bir yerel sunucuya döner; hibrit (mozsearch deseni) meşru ve emsalli bir orta yoldur. Bedel bayatlama + yeniden-derleme zorunluluğudur ve bu bedel yerel senaryoda da kalır."

### ④ Diyagram katmanının determinizmi — DARALDI

- İki raporun Graphviz alıntıları ÇELİŞMİYOR, koşul uzayını bölüşüyor: `start` atanmamışken tohum sabit ve yerleşim tekrar-üretilebilir (rapor-1, resmî attrs/start); `start`'a sayısal-olmayan değer (ör. `random`) verilirse zaman/pid tohumu → her koşum farklı (rapor-2, resmî startType). Sürümler-arası garanti iki turda da bulunamadı; rapor-2 CHANGELOG'da yerleşim/SVG davranış değişimleri kayıtlı diyor — rapor-1'in N3 negatifi güçlendi.
- Mermaid: varsayılanın deterministik olmadığı (tarih-tabanlı id) birincil şemadan doğrulandı ve antitezde dayandı; rapor-2'nin kapsam daraltması değerli — belirsizlik geometride değil SVG eleman kimliklerinde; `deterministicIds:true` ile kapanır ama `deterministicIDSeed`'in tohum değerini değil UZUNLUĞUNU kullandığı hata (#6530) açık.
- D2: "tarayıcısız derler" iddiası dayandı ama yalnız SVG hattı için; PNG dışa aktarımı playwright-go ile gerçek headless tarayıcı çalıştırıyor.
- **Daraltılmış form (AYNEN):** "Diyagram katmanında determinizm VARSAYILAN değil, KOŞULLU ve kurulumla sağlanan bir özelliktir: Graphviz — aynı sürüm + aynı girdi sırası + start'a sayısal-olmayan değer verilmemiş; sürümler-arası çıktı kararlılığı garanti edilmez, sürüm sabitlenmelidir. Mermaid — varsayılan deterministik DEĞİL (tarih-tabanlı id); deterministicIds:true zorunlu, #6530 nedeniyle tohum değerine güvenilmez; belirsizlik geometriyi değil id'leri vurur. D2 — deterministik tarayıcısız hat yalnız SVG; PNG/PDF headless tarayıcı bağımlılığı getirir. Tekrar-üretim sürüm-sabitleme + kayıtla sağlanır."

### ⑤ VS Code webview desenlerinin maliyet/kısıtları — DARALDI

- Çekirdek maliyetler antitezde dayandı (rapor-2 md.13 ÇÜRÜTEMEDİM): webview kaynak-ağır, resmî kılavuz "sparingly", arka plan sekmesinde durum kaybı, dispose sonrası geri dönüşsüzlük, `"type": "webview"` sessiz başarısızlığı.
- İki mutlak daraldı: (a) "kalıcılık = yüksek bellek" yanlış — yüksek bellek yalnız `retainContextWhenHidden`'a ait, `getState`/`setState` ucuz kalıcılık yolu resmî dokümanda; (b) "native graf API yok" — rapor-1'in kendisi bunu doğrulanamadı diye işaretlemişti (iddia 55), rapor-2 somutladı: Source Control Graph görünümü native (v1.93) ve `scmHistoryProvider` proposed API'si var, ama Marketplace eklentilerine KAPALI.
- "Live Preview yerleşik" ifadesi de düştü: yerleşik olan integrated browser (localhost'u varsayılan editörde açar, file:// URL destekler — file:// içinde fetch davranışı DOĞRULANMADI); Live Preview ayrıca kurulan Microsoft eklentisi.
- **Daraltılmış form (AYNEN):** "Genel-amaçlı graf için üçüncü-şahıs eklentiye açık tek yol webview'dır ve maliyetleri belgelidir (kaynak-ağır, arka planda durum kaybı, CSP/asWebviewUri zorunluluğu); ucuz kalıcılık getState/setState ile vardır, retainContextWhenHidden istisnadır. 'Native graf API yok' yalnız 'GENEL-AMAÇLI native graf API yok, SCM-tarihçesine özel proposed API üçüncü şahsa kapalı' olarak doğrudur. Grafiksiz gezinme için SARIF Viewer deseni (tipli IR → squiggle + Problems + panel) webview kısıtlarını atlayan emsaldir; üçüncü yüzey yerleşik integrated browser + yerel sunucudur (Live Preview yerleşik değildir)."

### ⑥a "Satır-adresi + layout birleşik IR yok" (N1) — SAĞLAM

- Negatif, antitezin hedefli aramasından değişmeden çıktı (rapor-2 md.19 ÇÜRÜTEMEDİM) ve adlandırılmış en-yakın-kaçıranlarla güçlendi: Sprotty (layout + trace VAR ama trace EMF-URI, satır değil), SARIF (satır + graf VAR, layout YOK), Joern CPG (satır VAR, layout YOK), Graphviz -Tdot (pos VAR, satır için standart alan YOK), Structurizr (layout dışa aktarımda korunmaz). Structurizr bulgusu (md.12 daraltıcı notu) da aynı yönde.
- Mimari sonuç: böyle bir şema kurulacaksa emsalsiz alandır; en yakın tabanlar SourcetrailDB (SQLite: satır aralığı + graf, layout çalışma-anında) ve SARIF (satır + graf, layout'suz).

### ⑥b "Statik↔canlı ampirik çalışma yok" (N2) — DARALDI

- "Doğrudan statik-yüzey-vs-canlı-sunucu A/B'si yok" kısmı ayakta — rapor-2 de bulamadı.
- Ama mutlak haliyle savunulamaz: karar değişkeni GECİKME üzerinde kontrollü deneyler var — Liu & Heer 2014 (500 ms ek gecikme keşif etkinliğini, gözlem/hipotez üretim hızını ölçülür düşürür; yüksek gecikmeye önce maruz kalmak sonrayı da bozar), Brutlag/Google 2009 (100→400 ms → kullanım düşüşü, kalıcı etki), TVCG 2008 (önceden-render çok-çözünürlüklü görüntü teslimi çalışması).
- **Daraltılmış form (AYNEN):** "'Statik önceden-derlenmiş yüzey ↔ canlı sunucu' başlıklı doğrudan kontrollü A/B çalışması bulunamadı — bu boşluk gerçek; ancak kararı taşıyan değişken (etkileşim gecikmesi) üzerinde birinci sınıf kontrollü kanıt VARDIR ve yönü nettir: eklenen gecikme keşif davranışını ölçülür biçimde bastırır. Mimari çıkarım vekil-kanıtla yapılabilir; 'hiç ampirik dayanak yok' denemez."

---

## HAYATTA KALAN ÇEKİRDEK (mimari karar girdisi)

1. **md-yerli satır-adresli IR kullan, kod-IR formatı taşıma.** Desen 9 emsalle kanıtlı; formatlar çalkantılı (LSIF emekli, SCIP `range` deprecated). md tarafında hazır üretim yolu: mdast/unist `Point` (satır/sütun/offset, tipli düğüm) + gerekirse Pandoc `sourcepos` (yalnız commonmark/gfm/commonmark_x/djot okuyucu, `data-pos` attribute). Depolama emsali: SourcetrailDB — düz SQLite'ta satır-aralığı + graf, çevrimdışı, incelenebilir.
2. **file:// hedefleniyorsa veri `<script src>` yerel dosyayla ya da gömülü gider; fetch'e dayanan hiçbir bileşen (Pagefind, sql.js-httpvfs, harici JSON) file:// altında çalışmaz** — bunlar seçilirse yerel HTTP sunucusu mimariye baştan girer. Üç yol, koşulları ②'de.
3. **Yerel tek-kullanıcıda statik önceden-derleme savunulur; arama/xref ya ②-b ile statikleştirilir ya da küçük yerel sunucuya verilir (hibrit meşru, mozsearch emsali).** Ölçek argümanları bu senaryoda geçersiz; kalan gerçek bedel bayatlama + yeniden-derleme. Gecikme kanıtı (500 ms eşiği) önceden-derlenmiş anlık yüzey lehine vekil destek.
4. **Diyagram determinizmi kurulumla sağlanır ve sürüm sabitlemesiz garanti edilemez:** Graphviz sürüm-sabitli + `start` dokunulmamış; Mermaid `deterministicIds:true` (tohum değerine #6530 yüzünden güvenme); D2 yalnız SVG hattında tarayıcısız. Tekrar-üretim m.29 gereği kayıtla, sürüm damgasıyla.
5. **VS Code yüzeyi için üç emsalli desen:** webview + istemci çizim (maliyetleri belgeli, kalıcılıkta getState/setState), tipli IR → native UI (SARIF Viewer deseni, grafiksiz), yerleşik integrated browser + yerel sunucu (file:// URL açar; içindeki fetch davranışı doğrulanmadı). Genel-amaçlı native graf API'si üçüncü şahsa yok.
6. **"dosya:satır + layout" birleşik şeması emsalsiz alan** — kurulacaksa kendi şemamız gerekir; en yakın tabanlar SourcetrailDB ve SARIF (satır + graf, layout'suz), Sprotty'nin `trace` deseni (görsel öğe → kaynak geri-bağı) tasarım referansı.

## DÜŞEN / DARALAN

**Düşen alt-iddialar:**
- rapor-1 C12 hücresi "Pandoc AST kaynak-konum taşımaz [kanıt bulunamadı]" → DÜŞTÜ: `sourcepos` uzantısı satır:sütun taşır (denetçi doğrulamalı). rapor-1 hücreyi açık bırakmıştı (N4) — epistemik dürüstlük kaydı lehine, hücre yine de düştü.
- rapor-1 ②-özet kapanışı "belgeli İKİ kaçış yolu" → DÜŞTÜ: üçüncü belgeli yol (`<script src>` yerel veri dosyası, denetçi doğrulamalı) var.
- rapor-2 md.5 "mozsearch tamamen statik → ÇÜRÜDÜ" hükmü → hakemce GEÇERSİZ SAYILDI: rapor-1'in gerçek metni zaten "Hibrit" (C19) ve "sistem hibrittir" (iddia 20) diyor; çürütme kırpma sırasında bozulmuş iddia metnine karşı. rapor-2'nin kanıtı rapor-1'i çürütmüyor, TEYİT ediyor.

**Daralan kalemler (daraltılmış formlar yukarıda AYNEN):** ① IR olgunluğu · ② kaçış-yolu sayımı · ③ statik "pratik üstünlük" · ④ determinizm koşulsuzluğu · ⑤ "kalıcılık=bellek" ve "native API hiç yok" · ⑥b "hiç çalışma yok".

## HAKEM NOTLARI (kalıntı belirsizlikler — karar-taşımaz ama izlenir)

- SCIP `range` alanının `deprecated` işareti iki raporda da YOK (denetçi eksiltmesi); SCIP'e yaslanacak her tasarım önce halef alanı doğrulamalı.
- Kythe bakım-durumu kanıtı üçüncül (Wikipedia) — KARARSIZ; karar girdisi yapılmadı.
- Sourcegraph "8x küçük / 3x hızlı" rakamları iki turda da birincil kaynaktan doğrulanamadı (403) — kullanılmamalı.
- VS Code integrated browser İÇİNDE file:// fetch kısıtının durumu doğrulanmadı (rapor-2'nin kendi bayrağı) — ⑤/② kesişiminde denenerek kapatılmalı.
- Pagefind "10.000 sayfa <300kB" üretici beyanı; bağımsız ölçüm yok — sayı tasarım bütçesine damgasız girmez.
- rapor-2'nin Foam kanıtı ikincil (ham yollar 404) — ⑤ kararını etkilemiyor.
