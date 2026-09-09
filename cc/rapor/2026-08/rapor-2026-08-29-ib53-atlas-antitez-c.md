# ATLAS — ANTİTEZ RAPORU (Aile C: pipeline emsalleri)

**Tarih / AS-OF:** 2026-08-29 (aksi belirtilmedikçe her bulgu bu tarihte çekildi)
**Rol:** açık devil's advocate — her iddianın DEĞİLİNİ (¬T) savunacak kanıt arandı; "alternatif bakış" değil, lojiksel ters.
**Yöntem:** WebSearch + WebFetch + ham kaynak (raw.githubusercontent) çekimi. Uydurma yok; bulunamayan yerde "ÇÜRÜTEMEDİM (arama yapıldı)" yazıldı.

## KIRPMA BEYANI
Çağıran ajan 55 iddialık listeyi karar-taşıyan 22 iddiaya kırparak gönderdi. Kırpmayı ATLAS yapmadı; kırpılan 33 iddia bu raporda TARANMADI ve bu raporun "çürüdü/daraldı/dayandı" sayıları yalnız bu 22 üzerinden geçerlidir. Gerekçeleri ve kaynakları bilerek verilmedi (kör antitez); tüm karşı-kanıt sıfırdan bulundu.

## ARAÇ/ERİŞİM ARIZALARI (şeffaflık)
- `api.github.com` → **HTTP 403, rate limit** ("API rate limit exceeded for 161.9.13.23"). Arşiv/son-commit durumları bu yüzden API yerine depo sayfası + sürüm sayfası + arama üzerinden doğrulandı.
- `foambubble/foam` ham dosya yolları ve `docs.foam.md` → 404 (dosya düzeni değişmiş); Foam bulgusu PR/ikincil kaynağa dayanıyor, aşağıda işaretli.
- Paywall'a çarpılmadı (ScienceDirect/ResearchGate bağlantıları kullanılmadı; açık PDF'ler tercih edildi).
- Etiket ayrımı: **ÇÜRÜTEMEDİM** = arandı, karşı-kanıt yok. **ARANMADI** = hiç aranmadı → bu raporda ARANMADI etiketli iddia YOK (22/22 arandı).

## SKOR
| Karar | Sayı | İddia no |
|---|---|---|
| ÇÜRÜDÜ | 2 | 5, 21 |
| DARALDI | 14 | 1, 2, 3, 4, 6, 7, 8, 9, 14, 15, 16, 18, 20, 22 |
| ÇÜRÜTEMEDİM (iddia dayandı) | 6 | 10, 11, 12, 13, 17, 19 |
| ARANMADI | 0 | — |

---

## 1. "Satır-adresli tipli IR'ler olgun ve yaygındır" → **DARALDI**
**Karşı-kanıt (olgunluk ekseni):** Alanın amiral formatı 4 yılda değişti. Sourcegraph LSIF'i emekliye ayırdı: "Support for reading LSIF-encoded data has been removed as of Sourcegraph 4.6" (Sourcegraph docs, LSIF→SCIP göç sayfası). Kythe tarafında Wikipedia (üçüncül kaynak, ihtiyatla): ABD'deki Kythe geliştirme ekibi Nisan 2024'te işten çıkarıldı, yerine Hindistan merkezli bakım ekibi geldi. SCIP deposu `sourcegraph/scip` → `scip-code/scip` organizasyonuna taşındı (README'deki bağlantılar ikili org kullanıyor) — yönetişim değişimi, kararlılık işareti değil.
**Ayakta kalan kısım:** "Yaygın" doğru — SCIP README'de 10 üretici indeksleyici listeli (scip-java, scip-typescript, rust-analyzer, scip-clang, scip-ruby, scip-python, scip-dotnet, scip-dart, scip-php, debian-lsp).
**Daralma:** "Olgun" yerine "çalışır ama format-çalkantılı ve tek-satıcı ağırlıklı" okunmalı.
- https://sourcegraph.com/docs/admin/how-to/lsif-scip-migration
- https://github.com/sourcegraph/scip (README, "Tools using SCIP" bölümü)
- https://en.wikipedia.org/wiki/Google_Kythe [üçüncül kaynak bayrağı]

## 2. "IR emsalleri Markdown bilgi-deposuna taşınabilir" → **DARALDI**
**Karşı-kanıt (antitez yönünde):** SCIP'in resmî indeksleyici listesinde **Markdown yok** — 10 kalemin 9'u programlama dili, biri Debian paketleme dosyaları (SCIP README, "Tools using SCIP"). Yani kod IR'lerinin *artefaktları* md dünyasına taşınmıyor; taşınan şey desen.
**Ama iddiayı çürütemedim, çünkü md dünyasının KENDİ satır-adresli tipli IR'i var (bu, iddiayı farklı mekanizmayla ayakta tutuyor):**
- unist/mdast spesifikasyonu, ham alıntı (`readme.md`, "Point" bölümü): "interface Point { line: number >= 1  column: number >= 1  offset: number >= 0? }" ve "**Position** represents the location of a node in a source *file*." → her mdast düğümü tipli (`type` alanı) + satır/sütun konumlu.
- Marksman ve markdown-oxide: Markdown için LSP sunucuları (go-to-definition, find-references, wiki-link) — LSP'nin kendisi satır/sütun adresli.
**Daralma:** "Emsaller taşınabilir" ≠ "SCIP/LSIF/Kythe md'ye taşınır". Doğru ifade: md'de satır-adresli tipli IR *zaten vardır* (mdast/unist), kod IR'lerinden devşirmeye gerek yok.
- https://github.com/syntax-tree/unist (readme, Position/Point)
- https://github.com/sourcegraph/scip
- https://github.com/artempyanykh/marksman · https://oxide.md/LSP

## 3. "file:// yerel JSON çekemez; tek çözüm gömme ya da yerel sunucu" → **DARALDI** ("tek çözüm" kısmı ÇÜRÜDÜ)
**Ayakta kalan kısım:** fetch/XHR gerçekten bloklu. Eric Lawrence (Chrome/Edge, textslashplain), "Restrictions on File Urls" bölümü: tarayıcılar "treat file origins as unique, blocking simple read of other files via `fetch()`".
**Karşı-kanıt ("tek çözüm" ifadesine):** Aynı yazının izin verilenler bölümü, ham alıntı: "Chromium and Firefox allow HTML pages served from `file://` URIs to _load (execute)_ images, regular ([non-Worker](…)) scripts, and frames from any file same path."
→ Yani **ayrı bir `veri.js` dosyası `<script src>` ile yüklenebilir**: veri HTML'e gömülü DEĞİL, ayrı dosyada, sunucu YOK. Bu üçüncü yol, iddianın "tek çözüm" kapanışını yıkar.
**Ek çıkışlar:** Chromium `--allow-file-access-from-files` (Chromium v99+ ile fetch de açılır), Firefox `privacy.file_unique_origin=false` (Bugzilla 1566051 / 1500453). Ayrıca `<input type="file">`/FileReader kullanıcı-seçimli okuma yolu açık kalır.
**Bonus (aynı sorunun VS Code cephesi):** VS Code'un yeni yerleşik tarayıcısı ham alıntı: "The browser supports `http://`, `https://`, and `file://` URLs." (integrated-browser.md, "Navigation" bölümü) — file:// gezinme editör içinde mümkün. [Not: bu tarayıcı içinde fetch kısıtının kalkıp kalkmadığı DOĞRULANMADI.]
- https://textslashplain.com/2019/10/09/navigating-to-file-urls/
- https://bugzilla.mozilla.org/show_bug.cgi?id=1566051 · https://bugzilla.mozilla.org/show_bug.cgi?id=1500453
- https://github.com/microsoft/vscode-docs/blob/main/docs/debugtest/integrated-browser.md

## 4. "Statik önceden-derlenmiş yüzeyler canlı-sunucudan pratik olarak üstündür" → **DARALDI**
**Karşı-kanıt:** En büyük üç kod-tarama dağıtımı canlı sunucu kullanıyor.
- Searchfox/mozsearch'ün kendisi: statik HTML üretir AMA arama için canlı sunucu şart (aşağıda md.5).
- Google: cs.chromium.org / source.chromium.org kapalı kaynak, sunucu tabanlı CodeSearch (Kythe issue #1101 ve chromium-discuss başlıklarında "codesearch is not open source" beyanı).
- Sourcegraph: canlı sunucu + arka planda SCIP indeksleri.
**Daralma:** Statik derlemenin gerçek üstünlüğü *barındırma maliyeti ve dayanıklılık*; "pratik üstünlük" arama/çapraz-referans yükü altında kanıtlanmıyor — o iş yükü sürekli sunucuya geri dönüyor.
- https://github.com/kythe/kythe/issues/1101
- https://groups.google.com/a/chromium.org/g/chromium-discuss/c/vgr8gU6gLWw

## 5. "mozsearch tamamen statik bir sistemdir" → **ÇÜRÜDÜ**
**Karşı-kanıt (birincil, depo dokümanı):**
- Mimari doküman: "Mozsearch generates one static HTML file for every source file" — ama aynı dokümanda arama için canlı bileşen: "This step generates a single large index file, `livegrep.idx`… The same `codesearch` tool is used by the web server to search the index."
- Kurulum README'si, "test" bölümü ham alıntı: "Setup the webserver for the test repo." / "Run the webserver for the test repo." / "After that, you can connect to http://localhost:16995/ and see Searchfox at work!"
- Depoda `web-server` (Rust) + `router` bileşenleri var; kurulum belgesine göre Rust web sunucusu 8001, Python sunucusu 8000 portunda koşar.
**Sonuç:** mozsearch = statik HTML üretimi + **zorunlu canlı sunucu katmanı** (arama, sembol sorguları, yönlendirme). "Tamamen statik" yanlış.
- https://github.com/mozsearch/mozsearch (README + docs/)
- https://github.com/Rob--W/searchfox/blob/master/docs/install.md

## 6. "Quartz içerik indeksi satır adresi taşımaz; graf kenarları yalnız link alanından türetilir" → **DARALDI**
**Ayakta kalan kısım (satır adresi):** `contentIndex.tsx` içindeki tip, ham alıntı:
`export type ContentDetails = { slug, filePath, title, links, tags, content, richContent?, date?, description? }` → satır/sütun alanı YOK. Bu yarı doğrulandı.
**Karşı-kanıt (kenar üretimi):** `graph.inline.ts` kenarları etiketlerden de üretiyor, ham alıntı:
```
if (showTags) {
  const localTags = details.tags.filter((tag) => !removeTags.includes(tag)).map((tag) => simplifySlug(("tags/" + tag) as FullSlug))
  …
  for (const tag of localTags) { links.push({ source: source, target: tag }) }
}
```
ve `Graph.tsx` varsayılanları hem localGraph hem globalGraph için `showTags: true`. → **Varsayılan ayarda kenarların bir kısmı etiketlerden gelir**, "yalnız link alanından" yanlış.
- https://github.com/jackyzha0/quartz/blob/v4/quartz/plugins/emitters/contentIndex.tsx
- https://github.com/jackyzha0/quartz/blob/v4/quartz/components/scripts/graph.inline.ts
- https://github.com/jackyzha0/quartz/blob/v4/quartz/components/Graph.tsx

## 7. "Statik SQLite sorgusu tarayıcıdan mümkün ve pratikte kullanışlı" → **DARALDI**
**Ayakta kalan:** Teknik gerçekten çalışıyor (Range istekli lazy VFS).
**Karşı-kanıt ("pratikte kullanışlı" ifadesine), yazarın kendi beyanları:**
- "this library was mainly written for small personal projects of mine and as a demonstration"
- "There's also no cache eviction, so the more data is fetched the more RAM it will use."
- "Note that this whole thing only works well if your database and indexes are structured well."
- "If the browser doesn't support WebAssembly and WebWorkers, this won't work."
Ayrıca DOM sanal tablosu için: "proof-of-concept level implementation".
**Ek kısıt:** Barındırıcının HTTP Range desteği ZORUNLU; maksimum dosya boyutu olan barındırıcılarda veritabanını `create_db.sh` ile parçalamak gerekir. Range HTTP semantiğidir → **file:// senaryosunda uygulanamaz** (mekanizma çıkarımı [?], doğrudan beyan bulunamadı).
- https://github.com/phiresky/sql.js-httpvfs

## 8. "Tarayıcıda tam-metin arama statik parçalı indeksle küçük ağ yüküyle çözülür" → **DARALDI**
**Ayakta kalan (ama satıcı beyanı):** Pagefind ana sayfası ham alıntı: "Pagefind can run a full-text search on a 10,000 page site with a total network payload under 300kB, including the Pagefind library itself. For most sites, this will be closer to 100kB." → Bu **bağımsız ölçüm değil, üreticinin kendi iddiası**; bağımsız benchmark bulunamadı.
**Karşı-kanıt (kullanım kısıtı):** Pagefind çalışma anında `fetch` ile parça indeksleri ve WASM çeker; md.3'teki Chromium/Firefox file:// kuralı gereği **doğrudan diskten (file://) açılan sayfada arama çalışmaz**, HTTP sunucusu gerekir. Depoda "Implement local development mode" (issue #14) ve Hugo/Nextra topluluk başlıklarında aynı 404/fetch sorunu görünüyor. [file:// kısıtı mekanizma çıkarımı [?]: Pagefind dokümanında açık cümle bulunamadı.]
- https://pagefind.app/
- https://github.com/Pagefind/pagefind/issues/14

## 9. "Graphviz yerleşimi deterministiktir" → **DARALDI**
**Karşı-kanıt (birincil, Graphviz doküman çelişkisi):** `startType` sayfası ham alıntı: "If `seed` is a positive number, this is used as the seed. If it is anything else, the current time, and possibly the process id, is used to pick a seed, thereby making the choice more random." → `start=random` gibi sayısal olmayan değerde çıktı **her koşumda değişir**.
`start` attr sayfası ise varsayılan için tersini söyler: "If unset, the nodes are randomly placed in a unit square with the same seed is always used for the random number generator, so the initial placement is repeatable." (yalnız neato/fdp/sfdp).
FAQ ayrıca kuvvet-yönelimli motorlar için: "Neato and all similar virtual physical model algorithms rely on heuristic solutions of optimization problems… it is also possible for these heuristics to get stuck in local minima."
**Daralma:** Determinizm koşullu — *aynı sürüm* + *aynı girdi sırası* + *sayısal olmayan `start` yok*. "Graphviz deterministiktir" koşulsuz haliyle yanlış; sürümler arası yerleşim/SVG çıktısı değişimleri de CHANGELOG'da kayıtlı (ör. viewBox davranışının 2.38.0→geri alınması).
- https://graphviz.org/docs/attr-types/startType/ · https://graphviz.org/docs/attrs/start/ · https://graphviz.org/faq/

## 10. "Mermaid varsayılan ayarlarla deterministik DEĞİL" → **ÇÜRÜTEMEDİM (arama yapıldı) — iddia dayandı**
**Doğrulama (birincil şema):** `config.schema.yaml` ham alıntı: "deterministicIds: … If set to `false`, the IDs are generated based on the current date and thus are not deterministic. This is the default behavior." `default: false`. Ek: "This matters if your files are checked into source control e.g. git and should not change unless content is changed."
**Bulabildiğim tek daraltma (iddia lehine değil, kapsam lehine):** Belirsizlik **geometride değil, SVG eleman kimliklerinde**; `deterministicIds: true` (+ `deterministicIDSeed`) ile kapatılabilir. Yani "deterministik değil" doğru ama tek satırlık bir konfigürasyonla tersine çevrilebilir bir kusur.
- https://github.com/mermaid-js/mermaid/blob/develop/packages/mermaid/src/schemas/config.schema.yaml

## 11. "D2 tipli IR üzerinden tarayıcısız SVG derler" → **ÇÜRÜTEMEDİM (arama yapıldı) — iddia dayandı**
**Doğrulama:** D2 README FAQ ham alıntı: "Does D2 need a browser to run? — No, D2 can run entirely server-side." Yerleşimler Go içinde: dagre ve ELK'in native Go portları gömülü (TALA ayrı ikili).
**Buldğum tek çatlak (SVG'yi değil, diğer hedefleri vuruyor):** PNG dışa aktarımı **gerçek tarayıcı çalıştırıyor** — `lib/png/png.go` doğrudan `github.com/mxschmitt/playwright-go` import ediyor. Yani "tarayıcısız" yalnız SVG için geçerli; PNG/PDF hattında headless tarayıcı bağımlılığı var.
- https://github.com/terrastruct/d2 (README, FAQ bölümü)
- https://github.com/terrastruct/d2/blob/master/lib/png/png.go

## 12. "Tek tipli modelden çok diyagram hedefine dışa aktarım çalışan bir desendir" → **ÇÜRÜTEMEDİM (arama yapıldı) — iddia dayandı**
**Doğrulama:** Structurizr CLI `export` şu hedefleri destekliyor: plantuml, plantuml/c4plantuml, mermaid, websequencediagrams, ilograph, d2, json; tek DSL dosyasından çok diyagram üretilip senkron tutuluyor.
**Daraltıcı not (çürütme değil):** Structurizr'ın kendi dokümanına göre dışa aktarılan diyagramlar statiktir, yalnız otomatik yerleşim kullanır ve görünüm Structurizr görüntüleyicisine göre "basic" kalır — yani **yerleşim bilgisi taşınmaz**, her hedef kendi yerleşimini yeniden hesaplar. (Bu, md.19'daki "satır+yerleşim birleşik şema yok" tezini destekler.)
- https://docs.structurizr.com/cli/export · https://docs.structurizr.com/getting-started/export-diagrams-as-code

## 13. "VS Code webview'ları kaynak-ağırdır; resmî kılavuz 'idareli kullanın' der" → **ÇÜRÜTEMEDİM (arama yapıldı) — iddia dayandı**
**Doğrulama (birincil, resmî doküman, "Should I use a webview?" bölümü), ham alıntı:** "Webviews are pretty amazing, but they should also be used sparingly and only when VS Code's native API is inadequate. Webviews are resource heavy and run in a separate context from normal extensions. A poorly designed webview can also easily feel out of place within VS Code."
Metin bugün de yürürlükte (vscode-docs `main`, 2026-08-29 çekimi). Karşı-kanıt yok.
- https://github.com/microsoft/vscode-docs/blob/main/api/extension-guides/webview.md

## 14. "Webview'da yerel dosya URI dönüşümüyle yüklenir; arka planda durum kaybolur; kalıcılık yüksek bellek maliyetlidir" → **DARALDI**
**Ayakta kalan iki parça (ham alıntılar, aynı doküman):**
- "you must use the `Webview.asWebviewUri` function to convert a local `file:` URI into a special URI that VS Code can use to load a subset of local resources." ("Loading local content" bölümü)
- "The contents of webviews however are created when the webview becomes visible and destroyed when the webview is moved into the background. Any state inside the webview will be lost when the webview is moved to a background tab." ("Persistence" bölümü)
**Karşı-kanıt (üçüncü parçaya):** Yüksek bellek maliyeti **kalıcılığın kendisine değil, yalnız `retainContextWhenHidden` seçeneğine** ait. Doküman ucuz alternatifi öneriyor: `getState`/`setState` düşük maliyetli kalıcılık, önerilen desen ise durumsuz webview + mesajlaşma. Yani "kalıcılık = yüksek bellek" yanlış; "tam bağlam saklama = yüksek bellek" doğru.
- https://github.com/microsoft/vscode-docs/blob/main/api/extension-guides/webview.md ("Persistence", "getState and setState")

## 15. "VS Code'da graf çizimi için native API yok; tüm graf eklentileri webview kullanır" → **DARALDI**
**Karşı-kanıt 1 (native graf, webview değil):** VS Code 1.93 sürüm notları, "Source Control Graph view" bölümü ham alıntı: "Based on user feedback, we have moved the history graph that was enabled last milestone from the Source Control view into a new view called **Source Control Graph**… This also lays the foundation for a full-featured history graph." Bu görünüm workbench'in kendi liste/ağaç bileşeniyle çizilir, eklenti webview'ı değildir.
**Karşı-kanıt 2 (API var, ama proposed):** `vscode.proposed.scmHistoryProvider.d.ts` içinde `SourceControlHistoryProvider` arayüzü — `provideHistoryItems`, `provideHistoryItemRefs`, `SourceControlHistoryItem.parentIds[]` (yani düğüm+kenar). Yerleşik Git eklentisi grafiği **bu sağlayıcı API'siyle** besliyor; graf çizimini VS Code yapıyor.
**Daralma:** "Native graf API yok" → "genel amaçlı native graf API yok; SCM tarihçesi için (henüz proposed olan) bir sağlayıcı API var ve Marketplace eklentilerine kapalı". "Tüm graf eklentileri webview kullanır" ifadesi de ürün düzeyinde yanlış.
- https://github.com/microsoft/vscode-docs/blob/main/release-notes/v1_93.md
- https://github.com/microsoft/vscode/blob/main/src/vscode-dts/vscode.proposed.scmHistoryProvider.d.ts

## 16. "VS Code localhost'u editörde açabilir; Live Preview yerleşik yerel sunucu deseni sunar" → **DARALDI**
**Karşı-kanıt ("yerleşik" sözcüğüne):** Live Preview **yerleşik değil**; Marketplace'ten kurulan bir Microsoft eklentisidir (`ms-vscode.live-server`). Yerleşik olan başka şey: eskiden "Simple Browser: Show" komutu, bugün ise tam bir **Integrated browser** (doküman onay tarihi 8/26/2026).
**Ayakta kalan + genişleyen kısım (ham alıntılar, integrated-browser.md):** "Select a `localhost` link anywhere in VS Code, like the terminal or chat. This behavior is enabled by default." ve "The browser supports `http://`, `https://`, and `file://` URLs."
**Daralma:** Doğru ifade = "localhost'u editörde açma YERLEŞİKTİR (ve artık file:// de açar); yerel sunucu deseni ise ayrıca kurulan bir eklentiden gelir."
- https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server
- https://github.com/microsoft/vscode-docs/blob/main/docs/debugtest/integrated-browser.md

## 17. "Foam'ın graf görünümü webview'da koşar" → **ÇÜRÜTEMEDİM (arama yapıldı) — iddia dayandı**
**Doğrulama (ikincil, birincil dosya yolu 404 verdi — bayrak):** Foam PR #438 "Add custom graph styling support" açıklaması, webview ↔ eklenti mesajlaşmasını tarif ediyor: webview yüklendiğinde VS Code'dan graf stilini ister, cevap gelince graf güncellenir. Graf çizimi `force-graph` (D3 force üstüne HTML canvas) ile yapılır; belge grafı `dagrejs/graphlib` ile tutulur. Komut: `Foam: Show Graph`.
Webview DIŞINDA bir Foam graf yolu bulunamadı.
- https://github.com/foambubble/foam/pull/438 · https://github.com/foambubble/foam/issues/58
- [BAYRAK: `packages/foam-vscode/src/features/**` ham yolları 404 döndü; kanıt ikincil.]

## 18. "Sourcetrail arşivlenmiştir, canlı değildir" → **DARALDI**
**Ayakta kalan:** Orijinal depo (CoatiSoftware/Sourcetrail) 14 Aralık 2021'de arşivlendi; EOL duyurusu issue #1214'te.
**Karşı-kanıt:** Bakımlı çatal **canlı**: `petermost/Sourcetrail` sürümleri — 2026.6 (11 Haziran 2026), 2026.4 (15 Nisan 2026), 2025.12.8, 2025.10.13, 2025.9.9. Yayın notları C/C++ indeksleme, derleyici desteği ve GUI değişiklikleri içeriyor.
**Daralma:** "Emsal ölü" değil; "üst-akım ölü, çatal canlı" — teknik emsal olarak (satır-adresli SQLite indeksi) hâlâ incelenebilir ve derlenebilir durumda.
- https://github.com/CoatiSoftware/Sourcetrail/issues/1214
- https://github.com/petermost/Sourcetrail/releases

## 19. "Satır-adresi + diyagram-yerleşimini BİRLEŞİK taşıyan yaygın şema YOKTUR" → **ÇÜRÜTEMEDİM (arama yapıldı) — iddia dayandı**
Böyle bir şema aradım; bulduklarımın **her biri üç özellikten yalnız ikisini** taşıyor:
- **Sprotty (Eclipse):** SModelElement'lerde yerleşim (position/size) VAR ve `trace` alanıyla kaynağa geri bağ VAR — ama trace bir **EMF URI/fragment**, satır/sütun değil. `UriTraceProvider.trace(traceable, source) → traceable.trace = source.URI.toPath`; satır çözümü sonradan dil sunucusundan yapılıyor.
- **SARIF 2.1.0:** `region.startLine` (satır) + `graph`/`node`/`edge` (graf) VAR, **yerleşim koordinatı YOK**.
- **Code Property Graph (Joern):** satır/sütun ve dosya katmanı VAR, yerleşim YOK.
- **Graphviz `-Tdot` çıktısı:** `pos` koordinatları + `URL`/`href` ile satır çapasına bağ pratikte mümkün, ama satır-adresi için **standartlaşmış alan yok** (serbest attribute).
- **Structurizr:** görünüm yerleşimi taşır, dışa aktarımda yerleşim korunmaz (md.12), satır adresi hiç yok.
**Sonuç:** Karşı-kanıt bulunamadı; iddia ayakta. En yakın aday Sprotty ve o da satır değil nesne-URI taşıyor.
- https://github.com/theia-ide/sprotty/blob/master/server/xtext-diagram/src/main/java/io/typefox/sprotty/server/xtext/tracing/UriTraceProvider.xtend
- https://cpg.joern.io/ · https://docs.joern.io/code-property-graph/

## 20. "Statik↔canlı görüntüleme kıyasını ölçen kontrollü/ampirik çalışma YOKTUR" → **DARALDI**
**Karşı-kanıt:** İki ayrımı ayıran değişken (gecikme) üzerinde kontrollü deneyler VAR.
- Liu & Heer, "The Effects of Interactive Latency on Exploratory Visual Analysis" (IEEE InfoVis/TVCG 2014), özetten ham alıntı: "We present an experiment measuring user behavior and knowledge discovery with interactive visualizations under varying latency conditions. We observe that an additional delay of 500ms incurs significant costs, decreasing user activity and data set coverage… we find that increased latency reduces the rate at which users make observations, draw generalizations and generate hypotheses." Ayrıca: yüksek gecikmeye önce maruz kalmak, sonraki düşük-gecikme koşulunda performansı düşürüyor.
- Brutlag (Google, 2009), "Speed Matters for Google Web Search": sunucu tarafına yapay gecikme enjekte edilen kontrollü deney; 100→400 ms gecikme günlük arama sayısını kullanıcı başına %0.2–%0.6 düşürüyor; 400 ms'ye 6 hafta maruz kalanlar gecikme kaldırıldıktan sonraki 5 haftada da ortalama %0.21 daha az arama yapıyor.
- Ayrıca önceden-render edilmiş (statik) görüntü teslimi ile talep-üzerine render'ı karşılaştıran sistem çalışmaları var (IEEE TVCG 2008, "Interactive, internet delivery of visualization via structured prerendered multiresolution imagery").
**Daralma:** "Statik yüzey vs canlı sunucu yüzeyi" başlıklı doğrudan A/B çalışması bulunamadı; ama kararı taşıyan değişken (gecikme) üzerinde birinci sınıf kontrollü kanıt mevcut → "hiç çalışma yok" savunulamaz.
- https://idl.cs.washington.edu/files/2014-Latency-InfoVis.pdf
- https://services.google.com/fh/files/blogs/google_delayexp.pdf
- https://pubmed.ncbi.nlm.nih.gov/18192711/

## 21. "Pandoc AST'si kaynak satır-konumu taşımaz" → **ÇÜRÜDÜ**
**Karşı-kanıt (birincil, Pandoc MANUAL.txt, "Extension: `sourcepos`" bölümü, satır 6377-6382), ham alıntı:**
"### Extension: `sourcepos` ###
Include source position attributes when parsing `commonmark` or `djot`. For elements that accept attributes, a `data-pos` attribute is added; other elements are placed in a surrounding Div or Span element with a `data-pos` attribute."
Konum değeri `./dosya.md@2:1-3:1` biçiminde satır:sütun aralığı taşır (pandoc 2.11.3 sürüm notlarında tanıtıldı; `commonmark`, `gfm`, `commonmark_x` için).
**Daralma (dürüstlük payı):** Uzantı **varsayılan `markdown` okuyucusunda yoktur** — yalnız commonmark/gfm/commonmark_x ve djot okuyucularında; ayrıca konum, tip alanında değil `data-pos` attribute'unda taşınır (Div/Span sarmalama maliyeti var; başlık düğümlerinde bilinen sorun: jgm/pandoc#7769).
- https://github.com/jgm/pandoc/blob/main/MANUAL.txt (satır 6377)
- https://github.com/jgm/pandoc/releases/tag/2.11.3 · https://github.com/jgm/pandoc/issues/7769

## 22. "Backstage TechDocs anlık üretimi reddedip statik üretimi savunur" → **DARALDI**
**Ayakta kalan (birincil, architecture.md FAQ), ham alıntı:** "**Q: Why aren't docs built on the fly i.e. when users visits a page, generate docs site in real-time?** A: Generating the content from Markdown on the fly is not optimal. Storage solutions act as a cache for the generated static content. TechDocs is also currently built on MkDocs which does not allow us to generate docs per-page, so we would have to build all docs for a entity on every request."
**Karşı-kanıt:** Ürünün **kutudan çıkan varsayılanı** Backstage'in kendi arka ucunda üretimdir. getting-started.md ham alıntı: "Out of the box, TechDocs is configured in `app-config.yaml` as: `builder: 'local'`" ve "**builder = local** — uses the TechDocs backend to generate the docs, publish to storage, and show the generated docs." Ayrıca architecture.md FAQ: "the basic setup would work but there are going to be downsides as you scale with the number of documentation sites and sizes of them."
**Daralma:** Reddedilen şey **her istekte yeniden üretim**; arka uçta üretim reddedilmiyor, varsayılan olarak SEVK EDİLİYOR — statik/CI önerisi ölçek gerekçeli, ilkesel değil.
- https://github.com/backstage/backstage/blob/master/docs/features/techdocs/architecture.md
- https://github.com/backstage/backstage/blob/master/docs/features/techdocs/getting-started.md

---

## ANTİTEZ AJANININ EPİSTEMİK NOTU
- 22 iddianın 6'sını çürütecek kanıt **bulunamadı** — bu iddialar bir antitez turundan geçmiş sayılır ve güvenleri yükselmiştir (özellikle 13, 17, 19).
- 2 iddia doğrudan yanlıştır (5 ve 21); ikisi de pipeline kararını değiştirebilecek türden: mozsearch'ün "statik emsal" olarak sayılması hatalı, ve Pandoc satır-konumu taşıyabildiği için md tarafında satır-adresli IR için hazır bir üretim yolu vardır.
- 14 daralma çoğunlukla **"tek çözüm / tamamen / yalnız / yerleşik"** gibi mutlak niceleyicileri vuruyor. Desen: iddiaların mekanizma çekirdeği sağlam, kapanış cümleleri fazla geniş.
- Zaman damgası: tüm bulgular 2026-08-29 itibarıyladır; VS Code (integrated browser), Mermaid şeması ve Sourcetrail çatalı hızlı değişen kalemlerdir, 3 ay sonra yeniden çekilmelidir.
