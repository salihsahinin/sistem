# ATLAS ANTİTEZ RAPORU — Aile A (dış emsal araçları)

**Rol:** açık devil's advocate — her iddianın DEĞİLİNİ (¬T) savunacak kanıt arandı.
**Tarih / AS-OF:** 2026-08-29 (aksi belirtilmedikçe tüm sürüm, tarih ve sayım bu güne aittir)
**Yöntem:** kaynak URL'leri bilerek verilmedi; kanıt sıfırdan bulundu. Mümkün olan yerde
birincil kaynak (kaynak kodu, resmî doküman, registry/marketplace API, yerel deney) tercih edildi.
**Dalga protokolü:** 4 paralel hat — VS Code çekirdeği · not-eklentileri · diyagram+SSG+indeksleyici · graf araçları.

## KIRPMA BEYANI
Gönderilen liste **102 iddiadan karar-taşıyan 19'una** kırpıldı. Kırpma bu ajanın işi değildir;
görev emriyle birlikte kırpılmış geldi ve hakeme görünür olsun diye buraya yazıldı.
Kırpılan 83 iddia bu raporda **denetlenmemiştir** — "çürütülemedi" sayılamazlar, **"bakılmadı"** sayılırlar.

## VERDİKT DAĞILIMI
| Verdikt | Sayı | İddialar |
|---|---|---|
| **ÇÜRÜDÜ** | 2 | 10, 13 |
| **DARALDI** | 10 | 1, 3, 5, 6, 7, 8, 9, 17, 18, 19 |
| **ÇÜRÜTEMEDİM** | 5 | 2, 4, 12, 14, 15 |
| **BÖLÜNMÜŞ** (yarısı çürüdü) | 2 | 11 (a çürüdü / b ayakta), 16 (3 SSG çürüdü / 3 ayakta) |
| **ARANMADI** | 0 | — |

**Hiçbir iddia "aranmadı" değil.** Her biri için en az bir hedefli arama + en az bir birincil kaynak denemesi yapıldı.

---

## 1. VS Code markdown'da `dosya.md#L123` ve `#L123,45` sütun biçimi resmî olarak desteklenir
### VERDİKT: **DARALDI** — davranış doğrulandı (hatta iddiadan geniş), ama "resmî" sıfatı yanlış

**Çürütemediğim çekirdek — üstelik iddia EKSİK kalıyor.** Kanonik ayrıştırıcı, yayımlanmış
`vscode-markdown-languageservice` paketinde, `src/util/path.ts` satır 71-72, fonksiyon
`parseLocationInfoFromFragment` (ham alıntı):

```
const match = fragment.match(/^L?(?<startLine>\d+)(?:,(?<startCol>\d+))?(?:-L?(?<endLine>\d+)(?:,(?<endCol>\d+))?)?$/i);
```
https://github.com/microsoft/vscode-markdown-languageservice/blob/main/src/util/path.ts

Regex'in söyledikleri — iddiada geçmeyenler dahil:
- `L` öneki **isteğe bağlı** → `#123` de çalışır
- `#L123,45` (satır,sütun) ✔ — iddia doğru
- **aralık** da destekli: `#L12,5-L20,3` — iddia bunu atlıyor
- satır 1-tabanlı, içeride 0-tabanlıya çevriliyor (`+match.groups['startLine'] - 1`)

Editör tarafında aynı davranış: `extensions/markdown-language-features/src/util/openDocumentLink.ts`,
`getSelectionFromLocationFragment` — aynı regex, `vscode.open` çağrısına `selection` olarak geçiyor.

**ÇÜRÜTEN BULGU 1 — "resmî olarak destekler" belgeleme anlamında YANLIŞ.**
Resmî doküman **kaynak deposunda** (`microsoft/vscode-docs`, `docs/languages/markdown.md`) satır-numarası
fragmenti **hiç geçmiyor**. Grep'te çıkan tek fragment referansları yalnız **başlık** fragmentleri:
- satır 175: "Fragments in links: `[text](./path/to/file.md#my-header)`. Shows all links to `#my-header` in `./path/to/file.md`"
- satır 159-160: `markdown.validate.fragmentLinks.enabled` / `markdown.validate.fileLinks.markdownFragmentLinks` — ikisi de **başlık** doğrulaması

https://github.com/microsoft/vscode-docs/blob/main/docs/languages/markdown.md ·
yayınlanmış hâli: https://code.visualstudio.com/docs/languages/markdown

→ Özellik **uygulanmış ama kullanıcı dokümanında yok**: sözleşme değil, gözlemlenmiş davranış.
Kırılganlık farkı buradan doğar — belgelenmemiş davranış haber verilmeden değişebilir.

**ÇÜRÜTEN BULGU 2 — GitHub ile sütun sözdizimi UYUMSUZ.** GitHub'ın kendi sütun biçimi `#L3C3`'tür;
VS Code regex'i **virgül** ister, `C` kabul etmez. Bunu isteyen issue kapatıldı:
"Support link with column numbers in the markdown editor" — `vscode-markdown-languageservice` issue **#29**,
durum **kapalı**, gövde (ham alıntı): *"Clicking on link `./b.md#L3C3` in the markdown editor should open
`b.md` with the cursor position in line 3, letter B."*
https://github.com/microsoft/vscode-markdown-languageservice/issues/29
→ Pratik sonuç: `yol:satır` GitHub ile VS Code arasında **taşınabilir**, `yol:satır:sütun` **taşınabilir DEĞİL**.

**İddiayı GÜÇLENDİREN yan bulgu (dürüst kayıt).** Satır-fragmenti kaza değil, kasıtlı:
bağlantı doğrulayıcı onu açıkça muaf tutuyor. `src/languageFeatures/diagnostics.ts` satır 233-234 ve 405-406,
ham alıntı (yorum satırı): `// Don't validate line number links` → ardından `parseLocationInfoFromFragment(...)`
ile erken çıkış. Yani `#L123` yazınca "No header found" uyarısı **alınmaz**.
https://github.com/microsoft/vscode-markdown-languageservice/blob/main/src/languageFeatures/diagnostics.ts

**Markdown-dışı hedefler çalışıyor:** "Linking to file with line number from markdown only works for .md files"
— `microsoft/vscode` issue **#125320**, **kapalı**, kilometre taşı **October 2021**.
https://github.com/microsoft/vscode/issues/125320

*Aramalar: VS Code markdown link line number fragment #L123 · vscode-docs markdown.md grep · language service path.ts / diagnostics.ts kaynak okuma · issue #29 / #125320 / #40140 / #142347*

---

## 2. `vscode://file/<tam-yol>:satır:sütun` resmî dokümanda tanımlıdır
### VERDİKT: **ÇÜRÜTEMEDİM** — iddia birebir doğrulandı

Resmî CLI dokümanı, **"Opening VS Code with URLs"** başlığı altında (ham alıntı):

```
vscode://file/{full path to file}:line:column

vscode://file/c:/myProject/package.json:5:10
```
https://code.visualstudio.com/docs/configure/command-line

İddia 1'in tersine burada gerçekten **resmî ve belgeli** bir sözleşme var. Çürütecek kanıt bulunamadı.
**Bu, 1 ile 2 arasındaki asıl asimetridir:** `#L` fragmenti belgesiz davranış, `vscode://` şeması belgeli sözleşme.

**Küçük daraltma (çürütme değil):** dokümandaki tek örnek **Windows** yolu (`c:/myProject/...`);
POSIX mutlak yolu için örnek yok — macOS/Linux'ta `vscode://file/` + baştaki `/` birleşiminin ürettiği
çift eğik çizgi karışıklığı dokümanda ele alınmıyor.

*Aramalar: vscode://file URL scheme line column official documentation · code.visualstudio.com/docs/configure/command-line*

---

## 3. Foam canlıdır; extension-exports ile programatik enjeksiyon fiilen mümkün ama resmî/belgeli API değil
### VERDİKT: **DARALDI** — iki yarısı zıt yönde kırıldı

**(a) "Foam ölü mü?" → HAYIR, fazlasıyla canlı (çürütemedim).**

| Ölçüt | Değer |
|---|---|
| repo `pushed_at` | **2026-08-13**, `archived: false`, 17.379 yıldız |
| Marketplace son güncelleme | **2026-07-26**, v0.44.5, 271.979 kurulum |
| `engines.vscode` | `^1.110.0` (güncel VS Code'a bağlı) |

Son commit'ler: `2026-08-13 Fix duplicated Foam variables in mirrored tabstops (#1694)`,
`2026-08-04 Moved host-metrics to foam/core`, `2026-07-27 Added internal profiler`.
https://github.com/foambubble/foam/commits/main

**Yol haritası bayat uyarısı:** repo yeniden yapılandırılmış — artık `packages/foam-core`, `foam-cli`,
`foam-graph`, `foam-mcp`, `foam-vscode` ayrı paketler. Eski `packages/foam-vscode/src/core/model/note.ts`
yolu **artık yok**, `packages/foam-core/src/model/note.ts` oldu.

**(b) "Belgeli API değil" → KISMEN ÇÜRÜDÜ.**

Enjeksiyon yolu gerçek: `packages/foam-vscode/src/extension.ts`, `activate()` dönüşü (ham alıntı):
```ts
    return {
      extendMarkdownIt: (md: markdownit) => { ... },
      foam,
    };
```
https://github.com/foambubble/foam/blob/main/packages/foam-vscode/src/extension.ts
→ `extensions.getExtension('foam.foam-vscode').exports.foam` canlı `Foam` nesnesini (workspace + graph) veriyor.
"Fiilen mümkün" yarısı **doğrulandı**.

Ama "belgeli değil" yarısı üç kanıtla daralıyor:
1. **Bakımcı buna "Foam API" diyor.** Issue #308 kapanış yorumu, Riccardo Ferretti (baş bakımcı),
   **2025-09-17**, ham alıntı: *"Closing for inactivity and removal of CLI. The Foam API is now available so
   another extension could access this information."* https://github.com/foambubble/foam/issues/308
2. **"Release API v1" issue'su kapatıldı.** Issue #1291, gövde *"Expose the Foam API so others can build on it"*,
   açılış 2023-10-04, **kapanış 2025-09-17** — yorumsuz, yani sessizce "yapıldı" sayılmış.
   https://github.com/foambubble/foam/issues/1291
3. **Belgeli programatik yol ARTIK VAR — ama exports değil, MCP.** Issue #1521, Ferretti'nin kapanışı
   **2026-06-10**: `"foam mcp is now available in the foam CLI"`. Belge sayfası canlı, açılış cümlesi (ham alıntı):
   > "Run a Model Context Protocol server over stdio so AI agents (Claude Desktop, Cursor, Zed, …) can read and traverse your Foam workspace as a knowledge graph instead of grepping files."
   
   https://docs.foam.md/tools/cli/mcp/ · `packages/foam-mcp/README.md` 30+ belgeli araç sayıyor —
   `traverse_graph`, `get_connections`, `get_placeholders`, `create_resource`, `update_resource`, `run_query`
   — `mode: 'read' | 'read-write'` kapısıyla.
   https://github.com/foambubble/foam/blob/main/packages/foam-mcp/README.md

**İddiayı ayakta tutan pay (dürüstlük):** repo genelinde `getExtension` kod araması **0 sonuç** —
exports şekli hiçbir yerde örneklenmiyor. `docs/` ağacının 79 dosyasında extension-exports/API sayfası **yok**.
`@foam/core` **npm'de yayımlanmamış** (`registry.npmjs.org/@foam/core` → `{"error":"Not found"}`);
`@foam/mcp` ve `foam-vscode` `"private": true` → tip tanımlarını dışarıdan çekemezsiniz.

**YENİ BULGU — enjeksiyonun kırılganlığı (iddiada yok, eklenmeli).**
`FoamGraph.update()` senkron biçimde haritaları temizliyor (ham alıntı, ~satır 107):
```ts
  public update() {
    const start = Date.now();
    this.backlinks.clear();
    this.links.clear();
    this.placeholders.clear();
    for (const resource of this.workspace.resources()) {
      this.connectResource(resource);
    }
```
https://github.com/foambubble/foam/blob/main/packages/foam-core/src/model/graph.ts
Ayrıca `onResourceUpdated` her dosya değişiminde `disconnectResource(old.uri)` + `connectResource(updated)` çağırıyor.
→ **Elle eklenen sentetik kenar, ilk tam yeniden kurulumda ya da o kaynağın ilk düzenlemesinde SİLİNİR.**
Enjeksiyon mümkün ama **kalıcı değil**: `onDidUpdate` olayına abone olup her seferinde yeniden enjekte etmek şart.
(Bu, madde 15'te Obsidian tarafında bulunan desenin birebir aynısı — bkz. aşağıda.)

---

## 4. Foam'ın bağlantı modeli satır/sütun farkındadır (Range taşır)
### VERDİKT: **ÇÜRÜTEMEDİM** — kaynak kodda tam doğrulandı; ama bir gerçek daraltma var

`packages/foam-core/src/model/note.ts` (ham alıntı):
```ts
export interface ResourceLink {
  type: 'wikilink' | 'link' | 'external';
  rawText: string;
  range: Range;          // ← opsiyonel DEĞİL, zorunlu
  isEmbed: boolean;
  definition?: string | NoteLinkDefinition;
}
```
`range.ts` + `position.ts` (ham alıntı):
```ts
export interface Range { start: Position; end: Position; }
export interface Position { line: number; character: number; }
```
`graph.ts` (ham alıntı):
```ts
export type Connection = {
  source: URI;
  target: URI;
  link: ResourceLink;    // ← ve ResourceLink.range zorunlu
};
```
→ **Graf kenarı (Connection) satır/sütun taşır.** Ek olarak `Tag`, `Alias`, `Section` de `range: Range` taşıyor;
`Block` **iki** range taşıyor (`range` + `markerRange`).

https://github.com/foambubble/foam/blob/main/packages/foam-core/src/model/note.ts ·
https://github.com/foambubble/foam/blob/main/packages/foam-core/src/model/graph.ts

**DARALTMA (tek gerçek çürütme payı):** Range **yalnız kaynak tarafında**. `Connection.target` çıplak bir `URI` —
hedef içindeki konumu göstermez. "Satır/sütun farkındalığı" **tek yönlüdür**: bağlantının *nerede yazıldığını*
bilir, *neye çarptığının neresi olduğunu* bilmez. Hedef tarafı konumlandırma ancak blok çıpaları
(`Block.range` / `^id`) ya da `Section.range` üzerinden dolaylı kurulabilir. Placeholder hedefleri hiç dosya
değil (`placeholder:<identifier>`), orada hedef-range kavramı tanımsız.

**Canlılık sinyali:** 2026-07-25 commit'i `"fixed semantics of Range.isBefore"` — Range tipi hâlâ aktif geliştiriliyor.

---

## 5. Marksman / Markdown Oxide / IWE / vscode-markdown-notes / Markdown Memo sınıfında graf yok, VS Code istemcileri bayat
### VERDİKT: **DARALDI** — "graf yok" tamamen doğru, "istemci bayat" doğru; ama "**projeler** bayat" okuması çürük

**Graf görünümü: refütasyon BAŞARISIZ — hiçbirinde yok.** `contributes.commands` üzerinden birebir doğrulandı:

| Eklenti | Komutlar | Graf? |
|---|---|---|
| Markdown Memo | `openDailyNote`, `openRandomNote`, `openReferenceBeside`, `extractRangeToNewNote` … | **Yok** |
| vscode-markdown-notes | `newNote`, `newNoteFromSelection`, `notesForWikiLink` | **Yok** |
| vscode-iwe | `iwe.editor`, `iwe.updateLanguageServer` | **Yok** |
| Marksman | saf LSP, webview yok | **Yok** |
| Markdown Oxide | saf LSP, webview yok | **Yok** |

IWE README'sinde yalnız *"A graph, not a folder tree"* retoriği ve statik bir SVG var; render eden görünüm yok.
https://github.com/iwe-org/iwe

> **⚠ BAYRAK — 403:** `https://iwe.md/docs/` ve `https://iwe.md/docs/concepts/comparison/` iki denemede de
> **HTTP 403 Forbidden** verdi. IWE'nin resmî belge sitesi doğrulanamadı; IWE bulguları GitHub README + release API'sine dayanıyor.

**ASIL DARALMA — iddia İSTEMCİ ile MOTOR ayrımını yapmıyor:**

| Proje | VS Code istemcisi (Marketplace) | Motor / sunucu (GitHub) |
|---|---|---|
| **Markdown Oxide** | v1.1.0 · **2024-07-02** · 1.813 kurulum | `pushed_at` **2026-08-29 (BUGÜN)**; release **v0.25.12 / 2026-06-29** |
| **IWE** | v0.0.4 · **2025-09-09** · 565 kurulum | `pushed_at` **2026-08-28**; release **iwe-v0.20.1 / 2026-08-24 (5 gün önce)** |
| **Marksman** | v0.3.4 · **2023-12-09** · 5.560 kurulum | `pushed_at` **2026-02-08**; son tag 2026-02-08 |
| **vscode-markdown-notes** | v0.0.27 · **2023-04-30** · 100.040 kurulum | son **gerçek** commit 2024-07-15 (kalan push dependabot gürültüsü) |
| **Markdown Memo** | v0.3.19 · **2022-07-30** · 27.758 kurulum | `pushed_at` **2024-07-20** — gerçekten bayat |

https://github.com/Feel-ix-343/markdown-oxide/releases · https://github.com/iwe-org/iwe/releases ·
https://github.com/artempyanykh/marksman/releases · https://github.com/svsool/memo · https://github.com/kortina/vscode-markdown-notes

**Sertleştirici ek kanıt (iddia lehine):** Markdown Oxide'ın VS Code istemcisi repo içinde (`vscode-extension/`),
`package.json` sürümü **1.1.0** — Marketplace'tekiyle **birebir aynı**; o dizindeki son commit 2025-08-17.
Yani yayımlanmamış daha yeni bir istemci de yok. IWE için de aynı: `iwe-org/vscode-iwe` `pushed_at` =
**2025-09-09** = Marketplace tarihi. OpenVSX'te üçünün de kaydı bulunamadı.

**Net:** "VS Code istemcileri bayattır" **ayakta** (en tazesi 11,7 ay, medyan ~2 yıl). Ama **motorlar bayat değil** —
Oxide bugün, IWE 5 gün önce güncellendi. İddia "bu projeler ölü" diye okunursa **çürür**; "bu projelerin VS Code
yüzü ihmal edilmiş" diye okunursa doğrudur ve aslında **daha keskin** bir bulgudur: sınıf toptan
Neovim/Zed/Helix + CLI/MCP'ye kaymış.

---

## 6. VS Code Mermaid önizlemesinde düğümden yerel dosyaya tıklanabilir link YOKTUR; PR reddedilmiş, issue açık
### VERDİKT: **DARALDI** — çekirdeği çürütemedim (aksine mekanizma düzeyinde güçlendirdim), ama iddianın iki olgusu yanlış

**Çürütemedim; üstelik gerekçesi iddiadakinden sağlam.** Üç katmanlı birincil kanıt:

1. **Mermaid `click`'i güvenlik ayarına bağlar ve o ayar direktifle DEĞİŞTİRİLEMEZ.**
   `packages/mermaid/src/schemas/config.schema.yaml`, `secure:` anahtarı, satır 354-367 (ham alıntı):
   > "This option controls which `currentConfig` keys are considered secure and can only be changed via call to `mermaid.initialize`. This prevents malicious graph directives from overriding a site's default security."
   
   varsayılan liste: `['secure', 'securityLevel', 'startOnLoad', 'maxTextSize', 'suppressErrorRendering', 'maxEdges']`.
   Uygulaması `src/config.ts` `sanitize()`, satır 140 (ham alıntı):
   `` log.debug(`Denied attempt to modify a secure key ${key}`, options[key]); `` → ardından `delete options[key]`.
   → Kullanıcı `%%{init: {'securityLevel':'loose'}}%%` yazarak **click'i açamaz.**
   https://github.com/mermaid-js/mermaid/blob/develop/packages/mermaid/src/schemas/config.schema.yaml ·
   https://github.com/mermaid-js/mermaid/blob/develop/packages/mermaid/src/config.ts

2. **VS Code'un yerleşik eklentisi `securityLevel` ayarını hiç açmıyor.**
   `extensions/mermaid-markdown-features/package.json` → sürüm **10.0.0**, bağımlılık `mermaid ^11.16.1`.
   `contributes.configuration.properties` **tam** listesi: `lightModeTheme`, `darkModeTheme`, `languages`,
   `maxTextSize`, `mouseNavigation.enabled`, `controls.show`, `resizable`, `maxHeight`.
   **`securityLevel` YOK** → `mermaid.initialize` yolu (tek izinli yol) kullanıcıya kapalı.
   https://github.com/microsoft/vscode/blob/main/extensions/mermaid-markdown-features/package.json

3. **Resmî sürüm notu interaktivite kapsamını sayıyor, link saymıyor.** VS Code **1.121**, **2026-05-20** (ham alıntı):
   > "We've merged Matt Bierner's Markdown Preview Mermaid Support extension into VS Code as a new built-in extension called `Mermaid Markdown Features`."
   
   İnteraktivite olarak yalnız: *"Rendered Mermaid diagrams also support panning and zooming…"* + kaynak kopyalama.
   https://code.visualstudio.com/updates/v1_121

**DARALTMA 1 — "PR reddedilmiş" YANLIŞ.** `mjbvz/vscode-markdown-mermaid` **PR #346**
("feature to support click link in graph to navigate to source file"; `vscode://bierner.markdown-mermaid/open`
URI handler'ı kaydediyordu) **bakımcı tarafından reddedilmedi** — **gönderen (lilongen) tarafından
2026-06-25'te kapatıldı**. Kayıtta bakımcı reddi yok; aksine bir kullanıcı (marcopedone) 2026-04-09'da
*"any update on this pr?"* diye sormuş, **yanıt yok**.
→ "Reddedildi" bir **karardır**; "sahipsiz kaldı" **karar yokluğudur**. Emsal değeri farklıdır: birincisi
"denendi, olmaz dendi", ikincisi "kimse bakmadı".
https://github.com/mjbvz/vscode-markdown-mermaid/pull/346

**DARALTMA 2 — iddianın hedefi artık referans uygulama değil.** İddia mjbvz'nin üçüncü-parti eklentisine bakıyor;
oysa **2026-05-20'den beri Mermaid VS Code'un içinde yerleşik**. Üçüncü-parti depodaki açık issue'lara dayanmak
karar tabanını bayat bir bileşene bağlar. (Açık issue'lar yine de teyitli: **#130** "Support relatives file links
in diagrams" — **açık**, `feature-request`/`help wanted`, açılış **2022-05-01**; **#126** — **açık**; #345 duplicate kapalı.)
https://github.com/mjbvz/vscode-markdown-mermaid/issues/130

**AÇIK KALAN KARŞI-KANIT YOLU (doğrulanamadı — uydurmuyorum, sınanmamış sayıyorum).**
Markdown Preview Enhanced'ın "Open Mermaid Config" özelliği kullanıcıya `mermaid.initialize` yapılandırmasını
doğrudan düzenletiyor; dolaşımdaki örnek:
`MERMAID_CONFIG = { startOnLoad: false, securityLevel:'loose', flowchart:{ htmlLabels: true } }`.
Yukarıdaki (1) numaralı mekanizmaya göre bu **izinli tek yol** olduğundan MPE'de `click` işleyicilerinin
etkinleşmesi **beklenir**. Ancak tıklamanın **yerel dosyayı editörde açıp açmadığını doğrulayamadım** —
webview'den yerel dosyaya gidiş ayrı bir engel (bkz. `microsoft/vscode` issue **#112459**, "Markdown Preview
links to local files are broken unless they are another markdown file").
https://github.com/shd101wyy/markdown-preview-enhanced/blob/master/docs/usages.md ·
https://github.com/microsoft/vscode/issues/112459

*Aramalar: vscode mermaid preview clickable link local file · markdown-mermaid securityLevel loose click href · mermaid schema/config.ts secure keys kaynak okuma · VS Code 1.121 release notes · mjbvz issue/PR taraması*

---

## 7. D2 canlı; SVG şekil-linkleri tıklanabilir; VS Code eklentisi güncel
### VERDİKT: **DARALDI** — üç bileşenden ikisi ayakta, üçüncüsü çürüdü

**Ayakta 1 — D2 çok canlı.** `v0.8.2` yayın **2026-08-28** (dün); son commit **2026-08-29** (bugün),
`d2sequence: stabilize lifeline endpoint IDs`. Öncesi v0.7.1 (2025-08-19), v0.7.0 (2025-05-02).
https://github.com/terrastruct/d2

**Ayakta 2 — SVG gerçekten `<a>` üretiyor (YEREL DENEY, d2 v0.8.1-HEAD).** Üretilen SVG'den ham çıktı:
```
<a href="https://example.com/a" xlink:href="https://example.com/a">
<a href="detail.svg" xlink:href="detail.svg">
<a href="https://example.com/cluster" xlink:href="https://example.com/cluster">
```
Dış URL ✔, katmanlar-arası board navigasyonu ✔, container/cluster üzerinde ✔.
"Yalnız dahili katman navigasyonu" hipotezi **yanlış**. Ayrıca `href` **ve** `xlink:href` çift yazılıyor.
Doküman: https://d2lang.com/tour/linking/
> **⚠ BAYRAK:** görev emrinde geçen `d2lang.com/tour/links` adresi **404**; doğrusu `/tour/linking/`.

**ÇÜRÜDÜ 3 — VS Code eklentisi BAYAT.** VS Marketplace Gallery API (`extensionquery`):
`terrastruct.d2` → **lastUpdated 2023-09-22**, listelenen tek sürüm **0.8.8**, ilk yayın 2022-10-18, ~77.5k kurulum.
Buna karşılık `terrastruct/d2-vscode` **deposu** canlı: son commit **2026-08-03**, 325 yıldız, 29 açık issue.
→ **Depo çalışıyor ama marketplace'e ~3 yıldır yayın yapılmamış.** Kullanıcının kurduğu artefakt bayat.
https://marketplace.visualstudio.com/items?itemName=terrastruct.d2 · https://github.com/terrastruct/d2-vscode

**Ek daraltma:** interaktivite SVG'ye bağlı; PNG gibi statik export'ta ikonlar numaralandırılıp ek üretiliyor, link yok.
https://d2lang.com/tour/interactive

---

## 8. Graphviz `URL` özniteliği SVG çıktıda tıklanabilir link üretir
### VERDİKT: **DARALDI** — çekirdek doğrulandı (dokümandan da geniş), iki pratik sınır bulundu

**Çürütemedim (YEREL DENEY, Graphviz 15.1.1 / 20260805).** Üretilen SVG'den ham çıktı:
```
<a xlink:href="https://example.com/root">
<a xlink:href="https://example.com/cluster" xlink:title="C">
<a xlink:href="https://example.com/a" xlink:title="a">
<a xlink:href="https://example.com/edge">
```
Düğüm ✔, kenar ✔, cluster ✔.
**Doküman davranışın gerisinde:** `graphviz.org/docs/attrs/URL/` kök grafik URL'i için SVG'yi saymıyor
(`ps2`, `cmap`, `i*map` diyor) ama 15.1.1 kök URL'i SVG'ye yazıyor. https://graphviz.org/docs/attrs/URL/

**DARALTMA 1 — yalnız `xlink:href`, düz `href` YOK.** Çıktıda düz `href="..."` araması **sıfır** sonuç.
D2 ikisini birden yazıyor. SVG2 `xlink`'i emekli ettiğinden, katı SVG2 işleyicileri ve `xlink` şeridini
atan sanitizer'lar altında Graphviz linkleri **sessizce ölebilir**. (İki araç arasındaki somut sağlamlık farkı.)

**DARALTMA 2 — `<img>` ile gömüldüğünde linkler ÖLÜ.** SVG `<img>` içinde işaretçi olayı almaz;
dosya tek başına açılınca çalışır, sayfaya `<img>` ile gömülünce çalışmaz.
Çözüm `<object type="image/svg+xml">` ya da inline SVG.
https://github.com/sphinx-doc/sphinx/issues/2175 · https://github.com/sphinx-doc/sphinx/issues/2232 ·
https://github.com/asciidoctor/asciidoctor-diagram/issues/64

`graphviz.org/docs/outputs/svg/` link konusuna **hiç** değinmiyor (doküman boşluğu).

---

## 9. Dendron bakım modundadır; aktif geliştirme durmuştur
### VERDİKT: **DARALDI** — upstream için doğru, ekosistem için yanlış

**Ayakta kalan yarı:** `dendronhq/dendron` son **gerçek kod** commit'i **2024-01-23**; sonraki iki commit
yalnız README/CI (2025-03-17, 2025-06-01). GitHub **Releases: sıfır**; en yeni tag `v0.116.3`; 800 açık issue.
Depo **arşivlenmemiş**. Kurucu beyanı (Şubat 2023, ham alıntı):
*"Dendron, the extension, will no longer be actively developed"* · *"Dendron the project will be in maintenance mode moving forward."*
https://github.com/dendronhq/dendron/discussions/3890
> **[?] Zayıf halka:** bu alıntı thread'e üçüncü kişi (`jangroth`, 2023-03-26) tarafından aktarılmış;
> Kevin Lin'in doğrudan yanıtı yok, birincil duyuru URL'si bulunamadı.

**ÇÜRÜTEN BULGU — canlı devam çatalı var:** `sxltd/dendron`, `parent: dendronhq/dendron`, **push 2026-07-21**.
Gerçek bakım işi, kendi PR numaralandırmasıyla: `chore!: remove changelog code from engine-server (#46)` 2026-07-21,
`chore(ci): add unit + integration test pipelines (#39)` 2026-01-08,
`enhance(publish): support git refs in nextjs export (#38)` 2026-01-06.
**Dağıtılmış ürün üretiyor:** VSIX `vsix@0.3.2` → **`vsix@0.3.9` (2025-12-27)**;
npm `@sxltd/dendron-cli` 0.4.2 (2025-12-18), `@sxltd/dendron-viz` 0.2.1 (2025-12-08).
README (ham alıntı, "How to Use"): *"This is a fork of Dendron, a local-first, markdown-based knowledge management system."*
https://github.com/sxltd/dendron

---

## 10. Markdown Links / CodeGraphy / tendr sınıfı VS Code graf eklentileri ya dış veri girişi almaz ya bayattır
### VERDİKT: **ÇÜRÜDÜ** — hem taze hem programatik dış-veri girişi olan iki eklenti bulundu

### Çürüten kanıt 1 — CodeGraphy: npm'de yayımlanmış, sürümlenmiş eklenti API'si
**Tazelik:** `codegraphy.codegraphy` **v5.16.4 · 2026-08-05** · 10.944 kurulum (Marketplace API).
Repo `joesobo/CodeGraphyV4` `pushed_at` **2026-08-07**, **MIT** (`Copyright (c) 2026 Joe Soboleski`).

**Dış veri girişi:** `docs/PLUGINS.md` — belgelenmiş iki katmanlı eklenti sistemi. Ham alıntı (§ "Core plugins"):
> "Core plugins add semantic information. They can analyze files, **add Nodes and Relationships**, define semantic Node Types and Edge Types, add filters, and keep plugin-owned data."

`packages/plugin-api/README.md` ham alıntı:
> "- add semantic Nodes, Symbols, and Relationships;
> - add semantic Node Type and Edge Type definitions;
> - store plugin-owned data through the provided data host."

Kayıt CLI ile: `codegraphy plugins register @codegraphy-dev/plugin-vue` → `... enable ...`.

**npm'de gerçekten yayımlanmış ve aktif** (registry'den canlı):

| Paket | Latest | npm `modified` |
|---|---|---|
| `@codegraphy-dev/plugin-api` | **8.0.0** | 2026-07-30 |
| `@codegraphy-dev/extension-plugin-api` | **3.0.0** | 2026-08-05 |
| `@codegraphy-dev/core` | **5.0.4** | 2026-08-05 |

Marketplace açıklaması: *"Markdown analysis ships as a bundled plugin. New workspaces enable it by default."*
ve *"Workspace-local SQLite storage"*.
https://github.com/joesobo/CodeGraphyV4/blob/main/docs/PLUGINS.md ·
https://marketplace.visualstudio.com/items?itemName=codegraphy.codegraphy ·
https://www.npmjs.com/package/@codegraphy-dev/plugin-api

> *Dürüst uyarı:* bu bir **dosya girişi** (JSON/CSV yükle) değil, **kod girişi** (npm paketi yaz, düğüm/kenar döndür).
> Ama "dış veri girişi ALMAZ" iddiasını çürütmeye yeter — eklenti içinden JSON/SQLite okuyup kenar üretebilirsiniz.

### Çürüten kanıt 2 — Yamlink: HTTP yazma API'li markdown graf eklentisi
**Tazelik:** `Yamlink.yamlink` **v0.7.9 · 2026-08-07** · 165 kurulum · **MIT**.
`src/api/router.js` (ham satırlar):
```js
{ method: 'POST',  path: '/api/nodes/bulk', ... nodes.bulkCreate ... },
{ method: 'PATCH', path: '/api/nodes/bulk', ... nodes.bulkUpdate ... },
{ method: 'POST',  path: '/api/nodes',      ... nodes.createNode ... },
{ method: 'ANY',   path: '/api/graph',      ... handleGraph ... },
```
README: `"yamlink serve --port 4000"` (yerel HTTP API), `"yamlink export --format csv"`,
`"41 commands, --json everywhere for scripting"`.
https://github.com/Yamlink-Labs/yamlink/blob/main/src/api/router.js

### Yan bulgu — sınıfta başka taze graf eklentileri de var
| Eklenti | Sürüm | Son güncelleme | Kurulum |
|---|---|---|---|
| `ConstellationGraph.ConstellationGraph` — *"Constellation maps your Markdown notes as an interactive graph — WebGL rendering, worker-side layout, built for large vaults"* | v0.1.0 | **2026-07-31** | 19 |
| `GauravPatidar.obsidian-graph-in-vscode` | v1.1.0 | **2026-08-19** | 14 |
| `visp-code-note.visp-notes` | v0.11.1 | 2026-08-06 | 15 |

### İddiayı doğrulayan kalan pay
- **Markdown Links** (`tchayen.markdown-links` v0.8.5, **2025-12-30**, 65.815 kurulum): taze-sayılır ama
  **dış veri girişi yok** — tüm ayarları yerel-markdown ayrıştırmasıyla sınırlı (`fileIdRegexp`, `graphType`,
  `titleMaxLength`, `wikiLinkAliasDivider`); JSON/CSV/SQLite/import ayarı yok. https://github.com/tchayen/markdown-links
- **tendr** (`manunamz.vscode-tendr` v0.0.9, **2024-12-25**, 258 kurulum): **bayat** (20 ay) — iddiayı doğruluyor.
- **md-graph** (`ianjsikes.md-graph` v0.1.1, **2020-08-14**): ölü.

**Net:** "ya/ya da" ikilemi kırıldı. CodeGraphy ve Yamlink **hem 2026-08'de güncel hem programatik dış-veri girişi
kabul ediyor**. İddia yalnız *markdown-links + tendr + md-graph* üçlüsü için doğru kalıyor; **sınıf genellemesi çürüdü**.

---

## 11. Cosma, dış kenar listesi (CSV: id,source,target,label,type) alan TEK araçtır; CSV ile markdown modu aynı anda çalışmaz
### VERDİKT (a) "TEK araç": **ÇÜRÜDÜ** · VERDİKT (b) "aynı anda çalışmaz": **ÇÜRÜTEMEDİM (doğrulandı)**

**(a) ÇÜRÜDÜ.** Dış kenar listesini birinci-sınıf giriş alan başka canlı araçlar:
- **Gephi** — `docs.gephi.org/desktop/User_Manual/Import/CSV_Format/`: kenar tablosunda **"Source" ve "Target"
  sütunları zorunlu ve seçim dışı bırakılamaz**. Çok canlı: push **2026-08-29**, **v0.11.2 (2026-05-09)**,
  v0.11.1 (2026-05-03). https://docs.gephi.org/desktop/User_Manual/Import/CSV_Format/ · https://github.com/gephi/gephi
- **Cytoscape** — push 2026-08-18, 3.10.4 (2025-09-26). https://github.com/cytoscape/cytoscape
- **graphology** (push 2026-07-21) + **sigma.js** (push 2026-08-20, 12.1k yıldız) — serileştirilmiş graf birinci-sınıf giriş.
- Ayrıca **Cosma'nın kendisi de üç modlu**: `select_origin` = `directory` | `csv` | `online` → dış kenar listesi
  yerel CSV olarak da **URL'den** de alınabiliyor. "Tek araç" değil, "tek mod" bile değil.

**(b) ÇÜRÜTEMEDİM — birincil dokümanla doğrulandı.** Cosma kullanıcı kılavuzu,
**§5 "Creating content: tabular data (CSV)"** (ham alıntı):
> "Cosma can interpret tabular data contained in local or online CSV files. **This is an alternative to using Markdown files.**"

`select_origin` tek değer alır; `files_origin` yalnız `directory`, `nodes_origin`/`links_origin` yalnız `csv` için tanımlı;
kayıt oluşturma komutları (`record`, `autorecord`, `batch`) yalnız `directory` modunda çalışıyor.
**İddiadaki CSV şeması birebir doğru** (§5.2 "Metadata for links"): `id`, `source`, `target` zorunlu; `label`, `type` isteğe bağlı.
https://cosma.arthurperret.fr/user-manual.html
Cosma canlı: **2.6.1 (2026-03-17)**, öncesi 2.6.0 (2025-11-25). https://github.com/graphlab-fr/cosma/releases

**Ek bulgu (iddia 19 için kritik):** Cosma'nın **VS Code eklentisi yok** — marketplace ve depo taramasında
Cosma/Cosmoscope için VS Code istemcisi bulunamadı. Yani ① karşılanıyor, ④ karşılanmıyor.

---

## 12. Quartz v5'te Graph View çekirdekten çıkıp topluluk eklentisine düştü; veri satır-adressiz contentIndex.json'dan gelir
### VERDİKT: **ÇÜRÜTEMEDİM** — üç parçanın üçü de doğru

Bu iddia "tamamen yanlış olabilir" diye işaretlenmişti; **tersi çıktı.**

1. **v5 var ve güncel.** `jackyzha0/quartz` **varsayılan dal = `v5`**, tag **`v5.0.0`** mevcut, push 2026-08-18, 13.130 yıldız.
   Resmî sayfa "What's New in Quartz 5", **2026-05-24** (ham alıntı): *"Plugins are now standalone packages maintained
   in the quartz-community GitHub organization and installed via git."* https://quartz.jzhao.xyz/getting-started/whats-new
   > **⚠ TUZAK BAYRAĞI:** GitHub **Releases** sekmesi **v4.0.8'de (2023-08-21) donmuş** — proje release yayınlamayı
   > bırakıp tag'lemeye geçmiş. Yalnız Releases'e bakan bir denetçi "v5 yok, v4 güncel" **yanlış çürütmesini** üretir;
   > bu hattaki ilk otomatik okuma tam bunu yaptı ve düzeltildi.
2. **Graph View topluluk eklentisi.** Ham alıntı (Graph View sayfası): *"The Graph View is now a community plugin.
   This demonstrates how external plugins can extend Quartz functionality while serving as a reference implementation
   for plugin developers."* Kurulum `npm install github:quartz-community/graph --legacy-peer-deps`.
   https://quartz.jzhao.xyz/features/graph-view · https://github.com/quartz-community/graph (push 2026-07-23)
3. **Satır-adressiz contentIndex.json.** Eklenti README satır 115 (ham alıntı): *"The Graph component fetches
   connection data from `/static/contentIndex.json` (generated by the ContentIndex emitter)"*.
   Emitter'ın `ContentDetails` tipi `slug: FullSlug` ve **`links: SimpleSlug[]`** taşıyor — bağlantılar
   **slug düzeyinde**, satır/karakter offset'i **yok**. Kod düzeyinde doğrulandı.
   https://github.com/quartz-community/graph/blob/main/README.md

---

## 13. Logseq DB sürümünde SQLite'ın kanonik kaynak olduğu iddiası yalnız ikincil kaynaklarla desteklidir
### VERDİKT: **ÇÜRÜDÜ** — Logseq'in kendi depolarında birincil kaynak var

1. **`logseq/logseq` README, master, "🚀 Database Version" (satır 73), ham alıntı:**
   > "The DB version is in beta status while the new mobile app and RTC is in alpha. This means that **data loss is possible** so we recommend automated backups or **regular SQLite DB backups**."
   
   https://github.com/logseq/logseq/blob/master/README.md
2. **`logseq/docs` (resmî doküman deposu, push 2026-08-17), `db-version-changes.md`, "Graph Directories", ham alıntı:**
   > "Inside a graph directory: `db.sqlite` - **Stores all your graph's data including user configs.** … `logseq/` inside a directory no longer exists."
   
   https://github.com/logseq/docs/blob/master/db-version-changes.md
   → "SQLite kanonik kaynak" iddiasının birincil karşılığı: tüm graf verisi tek `db.sqlite`'ta, eski markdown dizin yapısı yok.
3. **`logseq/docs/db-version.md`** (sayfa kendi tarihini veriyor: "as of April 28th, 2026") — "Graph Export":
   *"`Export SQLite DB` - Export graph as a SQLite .db file"*; markdown yalnız içe/dışa aktarım biçimi
   (*"It imports markdown files."*). Geliştirici notu: *"Press `Cmd-S` to persist a graph to `~/logseq/graphs/GRAPH-NAME/db.sqlite`."*
   https://github.com/logseq/docs/blob/master/db-version.md
4. Sürüm zinciri (birincil): release **2.0.1 "Desktop APP 2.0.1 (Beta Testing)" — 2026-07-13**; depo push 2026-08-28.
   https://github.com/logseq/logseq/releases/tag/2.0.1

**Dürüst kayıt — bir alt-iddia birincil kaynakla desteklenmedi:** resmî duyuru sayfası
https://logseq.io/p/e3YDyX5AYr **"SQLite" kelimesini hiç geçirmiyor**; yalnız *"Your database graph runs
exclusively on your local device, just like the file version."* diyor. Duyuru düzeyinde zayıf,
doküman/README düzeyinde birincil ve güçlü.

---

## 14. zk: SQLite + JSON graf + LSP var; VS Code eklentisi 2024'ten beri güncellenmemiş
### VERDİKT: **ÇÜRÜTEMEDİM** — üstelik iddia gerçekten olduğundan DAHA İYİMSER

**Olumlu parçalar doğrulandı:** SQLite → `go.mod`: `github.com/mattn/go-sqlite3 v1.14.22`.
JSON graf → `internal/cli/cmd/graph.go` (ham alıntı):
`` Format string `group:format short:f help:"Format of the graph among: json." enum:"json" required` `` — `--format json` **zorunlu ve tek seçenek**.
LSP → README satır 27 *"Any LSP-compatible editor"*. https://github.com/zk-org/zk/blob/main/go.mod

**VS Code eklentisi iddiadan da kötü.** Marketplace Gallery API (birincil): publisher `mickael-menu`,
**yayınlanan tek sürüm `0.1.0`**, `publishedDate: 2021-04-23`, **`lastUpdated: 2021-04-23`**, 1.232 kurulum.
→ **2024'ten değil, 2021'den beri güncellenmemiş.**
Depoda son commit 2024-01-04 ama içeriği `Remove references to old repo (#4)` — kod değil README temizliği;
son gerçek özellik commit'i **2021-04-23**. Resmî "Editors integration" sayfası hâlâ aynı eklentiyi öneriyor
ve **bakımsızlık uyarısı içermiyor**.
https://marketplace.visualstudio.com/items?itemName=mickael-menu.zk-vscode · https://github.com/zk-org/zk-vscode ·
https://zk-org.github.io/zk/tips/editors-integration.html

**Denge notu (iddiayı çürütmez):** zk çekirdeği çok canlı — **v0.15.6 (2026-07-26)**, push 2026-08-24;
`zk-nvim` push **2026-08-28** (850 yıldız). Durgunluk **yalnız VS Code kanalına** özgü.
Üçüncü-parti canlı graf eklentisi de var: `cyberSapoPerro/zk-graph-view`, push **2026-08-14**, 26 yıldız.
https://github.com/cyberSapoPerro/zk-graph-view

---

## 15. Obsidian eklentileri `resolvedLinks`'e çalışma-zamanında sentetik kenar enjekte edebilir
### VERDİKT: **ÇÜRÜTEMEDİM** — hem tip düzeyinde hem çalışan eklenti kaynağında doğrulandı

**Read-only mü? HAYIR.** Resmî tip tanımı `obsidianmd/obsidian-api/obsidian.d.ts`, satır 4433-4444 (ham alıntı):
```ts
    /**
     * Contains all resolved links. This object maps each source file's path to an object of destination file paths with the link count.
     * ...
     * @public
     */
    resolvedLinks: Record<string, Record<string, number>>;
```
`readonly` **yok**, `Readonly<>` sarmalayıcı **yok**, `@public` **var**. Resmî belge sayfası da readonly işaretlemiyor.
https://github.com/obsidianmd/obsidian-api/blob/master/obsidian.d.ts ·
https://docs.obsidian.md/Reference/TypeScript+API/MetadataCache/resolvedLinks

**Fiilen yapan eklenti: OpenCode Links Graph** (topluluk dizininde yayında). `src/main.ts` ham satırlar:
```ts
private addSyntheticLink(sourcePath: string, targetPath: string): void {
    cache.resolvedLinks[sourcePath] ??= {};
    ...
    cache.resolvedLinks[sourcePath][targetPath] = state.baselineCount + state.syntheticCount;
}
```
README ham alıntıları (§ "What It Does" / § "Why Synthetic Metadata?"):
> "Adds **synthetic entries to Obsidian's resolved-link metadata**."
> "**The native Graph and Local Graph can then render those relationships as if they were ordinary internal links.**"
> "Does **not** rewrite your Markdown files."

https://github.com/wlankasper/obsidian-opencode-plugin/blob/main/src/main.ts ·
https://community.obsidian.md/plugins/opencode-links-graph

**Tek çürütme payı — "resmî public API değil" uyarısı; ama bu iddiayı çürütmüyor, RİSKİNİ adlandırıyor.**
README § "Limitations" ham alıntı:
> "This plugin uses Obsidian's **internal** `metadataCache.resolvedLinks` shape. That shape is **widely used by plugins but is not a formal public API**, so future Obsidian versions may require updates."

Desen kalıcı da değil: sentetik kenarlar `onunload`'da siliniyor ve Obsidian'ın kendi çözümleme turu üzerine
yazabildiği için eklenti `metadataCache` olaylarında (debounce 400 ms) **yeniden enjeksiyon** yapıyor.
**Bu, madde 3'te Foam tarafında bulunan `graph.update()` temizleme davranışının birebir aynısıdır** —
iki ekosistemde de kural aynı: *enjeksiyon mümkün, ama olay-güdümlü yeniden-enjeksiyon şart.*
Resmî ekleme metodu hâlâ yok: https://forum.obsidian.md/t/api-method-to-add-link-and-have-it-parsed-into-metadatacache/72046

**Yan bulgular (aynı sınıf, iç mekanizması AÇILMADI — yalnız varlık teyidi):**
Extended Graph (https://community.obsidian.md/plugins/extended-graph),
Graph Link Types (https://github.com/natefrisch01/Graph-Link-Types), Virtual Linker.

---

## 16. SSG sınıfında (Docusaurus, Starlight, VitePress, MkDocs, Sphinx, Quarto) hazır graf-görünümü YOKTUR
### VERDİKT: **ÇÜRÜDÜ** (Docusaurus, MkDocs, Starlight) · **ÇÜRÜTEMEDİM** (VitePress, Quarto, Sphinx)

Beş canlı, arşivlenmemiş, hazır graph-view eklentisi:

| Eklenti | SSG | Son push | Yıldız |
|---|---|---|---|
| `Fevol/starlight-site-graph` | Starlight | **2026-06-02** | 87 |
| `whoisltd/docusaurus-plugin-graph-view` | Docusaurus | **2026-08-13** | 6 |
| `daxcore/mkdocs-obsidian-interactive-graph-plugin` | MkDocs Material | **2026-02-10** | 36 |
| `develmusa/mkdocs-network-graph-plugin` | MkDocs Material | **2026-02-04** | 8 |
| `Arsero/docusaurus-graph` | Docusaurus | 2024-11-22 | 16 |

- **Starlight Site Graph** — sayfa grafı + backlinks + kenar çubuğuna gömülü; canlı demo sitesi var.
  https://fevol.github.io/starlight-site-graph/ · https://github.com/Fevol/starlight-site-graph
- **docusaurus-plugin-graph-view** — d3-force + Canvas, satır-içi link **ve `[[wikilink]]` otomatik algılama**.
  https://github.com/whoisltd/docusaurus-plugin-graph-view
- **mkdocs-obsidian-interactive-graph-plugin** — ECharts, Obsidian benzeri; PyPI'da 0.3.2.
  https://github.com/daxcore/mkdocs-obsidian-interactive-graph-plugin · https://pypi.org/project/mkdocs-obsidian-interactive-graph-plugin/
- `Arsero/docusaurus-graph` resmî Docusaurus topluluk kaynaklarında listeli: https://docusaurus.io/community/resources

**Çürütemediğim alt-küme (dürüst kayıt):**
- **VitePress** — site-grafı/backlink eklentisi **bulunamadı**; bulunanlar markdown *içi* diyagram çizicileri
  (chartjs, mermaid/markmap, graphviz DOT renderer) — **kategorik olarak farklı**: site yapısını değil, blok içeriğini çiziyorlar.
- **Quarto** — yalnız **açık tartışma**, eklenti yok: Discussion #5901 (Obsidian tarzı graph view talebi;
  öneriler echarts4r/visNetwork gibi elle çözümler). https://github.com/orgs/quarto-dev/discussions/5901
- **Sphinx** — `sphinx.ext.graphviz` (DOT gömme) ve `sphinx-graph` (öğeler arası DAG) var ama **site graf görünümü değil**.
  https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html · https://sphinx-graph.readthedocs.io/en/main/

**Sonuç:** "sınıf genelinde yoktur" biçimi çürüdü; **6 SSG'nin 3'ünde** canlı hazır çözüm var, 3'ünde yok.

---

## 17. SourcetrailDB "keyfî veri için indexer yazılabilir" der ama proje arşivlidir
### VERDİKT: **DARALDI** — uygulama için yanlış, SDK için doğru

**Arşiv kısmı doğrulandı:** `CoatiSoftware/Sourcetrail` **archived: true**, son push **2021-12-13**, 16.5k yıldız;
`CoatiSoftware/SourcetrailDB` **archived: true**, son push **2021-11-22**, 298 yıldız.

**ÇÜRÜTEN BULGU — canlı, düzenli sürüm çıkaran çatal:** `petermost/Sourcetrail`, **archived: false**,
push **2026-08-21**, 751 yıldız. Sürüm takvimi: **2026.6** (2026-06-11), **2026.4** (2026-04-15),
2025.12.8, 2025.10.13, 2025.9.9 — yılda ~4-5 sürüm. Son commit'ler gerçek bakım işi (Qt event anahtar
kelimelerinin `Q_*` makrolarına çevrilmesi, vcpkg güncellemesi, kısayol tooltip düzeltmesi).
Bakımcı README beyanı (2026-08-01): orijinalin 2021 sonunda arşivlendiğini teyit ediyor, kendi konumunu
"çatal, en azından derlenebilir tutmak" diye tanımlıyor ve yeni müşteri projesi nedeniyle geliştirmenin
**yavaşlayacağını** ekliyor. https://github.com/petermost/Sourcetrail

**KRİTİK DARALTMA — asıl mesele SDK'da ve orada iddia AYAKTA.** "Keyfî veri için indexer yazma" yolu
**SourcetrailDB**'dir. Yukarı akış arşivli (2021-11-22); çatal bakımcısının kendi kopyası
`petermost/Sourcetrail-DatabaseAPI` de **2021-11-22'de donmuş** (1 yıldız); petermost README'si hâlâ **arşivli
CoatiSoftware/SourcetrailDB adresine** işaret ediyor.
→ Viewer güncelleniyor, **DB API'si 2021'den beri hiçbir yerde bakılmıyor.**
Uydu ekosistem kısmen canlı: `Sourcetrail-QtCreator` (2026-06-19), `Sourcetrail-VisualStudio` (2026-02-10);
`Sourcetrail-Eclipse` 2019'da donmuş.

---

## 18. MarkdownDB canlıdır ama kendi görselleştirme yüzeyi yoktur
### VERDİKT: **DARALDI** — her iki yarı da düzeltme gerektiriyor

**Yarı A — "canlıdır": doğru, ama npm cephesi yanıltıcı.**
- npm `mddb` **v0.9.5, 2024-03-07**'de donmuş (`dist-tags.latest = 0.9.5`); GitHub Releases de orada bitiyor.
  Eski `@flowershow/markdowndb` 2023-06-12'de terk edilmiş. **Tek pakete bakan canlılık testi yanlış negatif üretir.**
- **Kritik bulgu:** yeniden yazım yeni scoped aile olarak npm'de yayında — **`@mddb/core`, `@mddb/cli`, `@mddb/sdk`,
  hepsi v0.1.1, 2026-03-01**.
- Depo arşivsiz, son push **2026-05-21**, 521 yıldız; 2025-01'den beri **34 commit**, kozmetik değil:
  MySQL/PostgreSQL desteği (2026-03-03), çoklu dizini tek veritabanına indeksleme (2026-01-17),
  `--exec` API script çalıştırma, `processMarkdown` tek-dosya API, Node 20 yükseltmesi.
- **Künye bayat:** `datopian/markdowndb` artık **`flowershow/markdowndb`**'ye yönleniyor.
- Dürüst kayıt: son push 2026-05-21 → bugüne **~3 aylık sessizlik**. Ölü değil, hız kesmiş.
  https://github.com/flowershow/markdowndb · https://www.npmjs.com/package/mddb

**Yarı B — "görselleştirme yüzeyi yoktur": paket sınırında doğru, marka sınırında YANLIŞ.**
Kütüphanenin kendisinde graf UI'ı yok — `markdowndb.com` kendini SQL/JSON'a çeviren JS kütüphanesi olarak
tanımlıyor; ileri-link/backlink **çıkarma ve sorgulama** var, görsel graf yok. Bu kısım ayakta.
**Ama aynı organizasyon birinci-parti yüzey yayınlıyor:** `flowershow/flowershow`, **1102 yıldız**, push **2026-08-21**,
arşivsiz. Ürün sayfasında **Knowledge Graph** (*"notlarınızın ve nasıl bağlandıklarının interaktif haritası"*) ve
**Backlinks** (*"her sayfa kendisine link verenleri gösterir"*) açıkça reklam ediliyor, Obsidian wikilink desteğiyle.
→ markdowndb indeksleyici katman, Flowershow onun üstündeki yayın+graf katmanı, **ikisi aynı ekipten**.
https://flowershow.app/ · https://github.com/flowershow/flowershow

---

## 19. Profilin TAMAMINI karşılayan CANLI araç YOKTUR
> ① yerel md + DIŞ SQLite/CSV graf girişi ② deterministik LLM'siz türev ③ `yol`, `yol:satır`, `[[wikilink]]` pointer ④ VS Code entegrasyonu ⑤ açık kaynak

### VERDİKT: **DARALDI** — çürütemedim, ama iddia artık belirsiz değil: boşluk TEK ölçüte ve tek niteliğe indi

Agresif tarama yapıldı (knowledge-graph, digital-garden, code-map, 2025-2026 yeni çıkanlar dahil).
Beş ölçütün beşini birden karşılayan **tam eşleşme bulunamadı** — ama üç bulgu iddianın gücünü ciddi biçimde düşürüyor.

### BULGU A — CodeGraphy: **en yakın canlı aday**, ①②④⑤ tamam, ③ yarım
`joesobo/CodeGraphyV4` · **MIT** (`Copyright (c) 2026 Joe Soboleski`) · Marketplace **v5.16.4 · 2026-08-05** ·
**10.944 kurulum** · repo push 2026-08-07.

- **① yerel md ✔ + dış graf girişi ✔ (dolaylı):** *"Markdown analysis ships as a bundled plugin. New workspaces
  enable it by default."* + *"Workspace-local SQLite storage"*. Dış veri, **sürümlenmiş ve npm'de yayımlanmış**
  eklenti API'si üzerinden giriyor — `@codegraphy-dev/plugin-api` **v8.0.0** (npm, 2026-07-30). Eklenti
  *"add Nodes and Relationships"* yapabiliyor; yani bir eklenti dışarıdaki SQLite/CSV'yi okuyup düğüm+kenar yayabilir.
- **② deterministik, LLM yok ✔** — analiz tabanlı, plugin API'de LLM yok.
- **③ pointer YARIM:** `yol` ✔ ve `yol:satır(:sütun)` ✔ — tip tanımları birebir (ham alıntı,
  `packages/plugin-api/src/graph.ts` satır 33-38 ve `analysis.ts` satır 3-8):
  ```ts
  export interface IGraphNodeRange {
    startLine: number;
    startColumn?: number;
    endLine: number;
    endColumn?: number;
  }
  ```
  ve kenar tipi (ham alıntı, `analysis.ts` satır 59-69):
  ```ts
  export interface IAnalysisRelation {
    kind: GraphEdgeKind;
    pluginId?: string;
    sourceId: string;
    fromFilePath: string;
    toFilePath?: string | null;
    fromNodeId?: string;
    toNodeId?: string;
    ...
  }
  ```
  **Eksik:** `[[wikilink]]` desteği **doğrulanamadı** — plugin API tiplerinde wikilink kavramı geçmiyor.
- **④ VS Code ✔** · **⑤ MIT ✔**

**Kalan boşluk:** dış graf girişi bir **dosya işaret etme** değil, **npm paketi yazma** işi; ve `[[wikilink]]` yok.
https://github.com/joesobo/CodeGraphyV4/blob/main/docs/PLUGINS.md ·
https://github.com/joesobo/CodeGraphyV4/blob/main/packages/plugin-api/src/graph.ts ·
https://marketplace.visualstudio.com/items?itemName=codegraphy.codegraphy

### BULGU B — Yamlink: ②③④⑤ tamam, yalnız ① eksik (CANLI, çok yeni)
`Yamlink-Labs/yamlink` — **MIT**, **0.7.9**, son commit **2026-08-07**, Marketplace lastUpdated **2026-08-18**,
165 kurulum, 17 yıldız. Release zinciri sıkı: 0.7.7 (2026-08-02) → 0.7.8 → 0.7.9.

- **② LLM yok ✔** · **④ VS Code ✔** (*"Graph Workspace opens a focused explorer centered on the current note"*) · **⑤ MIT ✔**
- **③ pointer ✔ (üçü de, en iyi skor):** `[[wikilink]]` ✔ + frontmatter alanları **tipli kenar** ✔;
  README (ham alıntı): *"Every meaningful body element gets a stable ID… Go-to-definition lands on the exact line
  either way — not just the top of the note."* → satır hassasiyeti var, ama **blok-ID üzerinden**, literal
  `yol:satır` sözdizimiyle değil **[?]**
- **① EKSİK — kaynak kodda doğrulandı:** `src/api/router.js` yalnız **düğüm** CRUD sunuyor
  (`POST /api/nodes`, `POST|PATCH /api/nodes/bulk`, `DELETE /api/nodes/:id`); **kenar/link oluşturma rotası YOK**.
  `/api/nodes/:id/outbound`, `/inbound`, `/neighborhood` salt-okuma gezinme.
  Kenarlar wikilink/frontmatter'dan **türetiliyor** → dış kenar listesini ancak markdown'a **maddîleştirerek**
  enjekte edebilirsiniz. "Import tools" da yalnız **göç** araçları: Obsidian vault + Roam/Notion/Evernote export.
  README özeti: *"…all reading the same local files."*

https://github.com/Yamlink-Labs/yamlink/blob/main/src/api/router.js · https://github.com/Yamlink-Labs/yamlink

### BULGU C — CodeBase Relationship Visualizer: ①③④⑤ tamam ama ÖLÜ (2023-01-08)
**Antitez açısından en önemli bulgu:** profilin en yakın yapısal karşılığı **2023'te inşa edilmiş ve terk edilmiş.**
`jesse-r-s-hines/CodeBaseRelationshipVisualizer` — **GPL-3.0**, 14 yıldız, 449 commit, 2.077 kurulum, arşivsiz.
- **Belgeli public API** ile dış veri enjeksiyonu:
  `vscode.extensions.getExtension('jesse-r-s-hines.codebase-relationship-visualizer').exports`
- `Connection` tipi (ham alıntı, API dokümanı): *"A Connection connects two file:line locations in the workspace"*,
  örnek: `{from: {file: Uri.file("main.py"), line: 10}, to: {file: Uri.file("tutorial.py"), line: 3}}`; `line` isteğe bağlı.
  → **`yol` ve `yol:satır` birinci-sınıf** ✔ · kutudan çıkan **markdown/HTML hyperlink grafı** ✔
- **ÖLDÜRÜCÜ:** son commit **2023-01-08** → "CANLI" koşulu düşüyor. `[[wikilink]]` de yok.
https://github.com/jesse-r-s-hines/CodeBaseRelationshipVisualizer ·
https://jesse-r-s-hines.github.io/CodeBaseRelationshipVisualizer/interfaces/Connection.html

### Elenen adaylar (neden elendiği ile)
| Aday | Durum | Elenme nedeni |
|---|---|---|
| **Event Horizon** (`HeytalePazguato/event-horizon`) | MIT, 12 yıldız, commit **2026-08-15** — CANLI | ① dış graf girişi yok; ③ wikilink/satır pointer belgesiz; md keşfi CLAUDE.md/.cursorrules kalıplarıyla sınırlı. (SQLite grafı var: `<workspace>/.eh/graph.db`, `graph_nodes`/`graph_edges`/`graph_file_state` + FTS5; kenarlar `EXTRACTED (deterministic from AST)`/`INFERRED`/`AMBIGUOUS` provenans etiketi taşıyor; LLM **opsiyonel**.) |
| **Graphify** (`Graphify-Labs/graphify`) | 112.2k yıldız, Apache-2.0/MIT | **② düşüyor:** doküman/PDF/görsel için **LLM çağrısı gerekli**. Graf **`graph.json`**, SQLite değil. Dış kenar listesi almıyor. Ayrı VS Code eklentisi yok. |
| **CodeGraph** (`colbymchenry/codegraph`) | 68.6k yıldız, MIT | **Markdown indekslemiyor**; VS Code'a MCP sunucusu olarak bağlanıyor, eklenti değil; görselleştirme yok. |
| **obra/knowledge-graph** | commit 2026-03-22; *"no LLM inside the tool. The tool is pure data infrastructure"* ✔, SQLite+sqlite-vec ✔, wikilink ✔ | **④ düşüyor:** Obsidian/Claude Code eklentisi, VS Code değil. https://blog.fsck.com/agent-blog/2026/03/20/knowledge-graph/ |
| **Nogic** | VS Code eklentisi, canlı | **⑤ düşüyor:** kapalı kaynak ("will be open source soon" ama kod yayımlanmamış, depo linkleri kırık). https://news.ycombinator.com/item?id=46605675 |
| **vscode-interactive-graphviz** (`tintinweb`) | GPL-3.0, 205 yıldız | Bileşik yol olabilirdi (SQLite→DOT→önizleme) ama **son release v0.3.5, 2022-10-28** → bayat. README'de yerleşik URL/href tıklama navigasyonu belgeli değil; yalnız geliştiriciye `onClick`/`onDblClick` callback'i var. |
| **Cosma** | ①✔ (CSV kenar listesi), canlı 2.6.1 | **④ düşüyor:** VS Code eklentisi yok (bkz. iddia 11). |
| **Gephi / Cytoscape / graphology** | ①✔, canlı | ③④ yok: masaüstü/kütüphane; md yok, VS Code yok. |
| **Markdown Links** (`tchayen`) | 2025-12-30, 65.815 kurulum | ① yok — tüm ayarları yerel markdown ayrıştırmasıyla sınırlı. |
| **Foam** | canlı, ③✔ (Range, bkz. 4), ④⑤✔ | ① yok; exports enjeksiyonu **kalıcı değil** — `graph.update()` haritaları temizliyor (bkz. 3). |
| **SQLite şema görüntüleyiciler** (vscode-database-editor vb.) | VS Code ✔ | Foreign-key/şema grafı çiziyorlar, bilgi grafı değil; md yok, pointer yok. |

### Net hüküm
İddia **ayakta**, ama artık "hiçbir şey yok" değil, **ölçülmüş bir boşluk**:

| | ① dış graf | ② LLM'siz | ③ pointer | ④ VS Code | ⑤ açık kaynak | CANLI |
|---|---|---|---|---|---|---|
| **CodeGraphy** | ✔ (kod yazarak) | ✔ | yarım (satır ✔, wikilink ✘) | ✔ | ✔ MIT | ✔ 2026-08 |
| **Yamlink** | ✘ | ✔ | ✔ (blok-ID ile) | ✔ | ✔ MIT | ✔ 2026-08 |
| **CBRV** | ✔ (belgeli API) | ✔ | yarım (file:line ✔, wikilink ✘) | ✔ | ✔ GPL-3 | ✘ **2023-01** |

Profil **teknik olarak imkânsız değil**: parçaları üç ayrı projede **ayrı ayrı kanıtlanmış**, tek gövdede birleşmemiş.
En yakın canlı adayın (CodeGraphy) eksiği **tek nitelik** (`[[wikilink]]`) ve **bir kullanım maliyeti**
(dış graf için eklenti yazma zorunluluğu).

*Aramalar: knowledge graph tool local markdown SQLite external graph input VS Code extension open source 2026 ·
vscode extension graph view import edges from JSON CSV file · "Codebase Relationship Visualizer" custom connections ·
2026 markdown knowledge graph VS Code extension wikilinks graph view actively maintained ·
zettelkasten digital garden import external edge list CSV JSON graph markdown 2025 2026 ·
"graph view" vscode extension reads sqlite database nodes edges webview ·
tool renders graph from user-supplied nodes edges file with file:line links inside VS Code webview ·
Cosma cosmoscope vscode extension · CodeGraphy/Yamlink/Event Horizon/Graphify/CodeGraph/Nogic kaynak doğrulamaları*

---

## METODOLOJİK UYARILAR (hakeme)

1. **Releases sekmesi tuzağı (iddia 12).** Quartz release yayınlamayı bırakıp tag'lemeye geçmiş; Releases'e bakan
   ilk otomatik okuma *"v5 yok, v4.0.8 güncel"* **yanlış çürütmesini** üretti ve düzeltildi.
   Canlılık testi tek sinyale dayanmamalı (`default_branch` + tags + docs + push birlikte okunmalı).
2. **Depo canlı ≠ artefakt canlı (iddia 5, 7, 14).** D2'nin deposu 2026-08-03'te commit alıyor ama marketplace
   yayını 2023-09-22'de donmuş. zk-vscode deposu 2024, marketplace'i **2021**. Markdown Oxide motoru **bugün**,
   istemcisi 2024-07. **Kullanıcının kurduğu şey marketplace'tekidir** — karar oradan verilmeli.
3. **Paket adı göçü (iddia 18).** `mddb` donuk görünürken `@mddb/*` 2026-03'te canlı; `datopian`→`flowershow`
   sahiplik değişimi. Tek pakete/tek künyeye bakan test yanlış negatif verir.
4. **Kapatan kim? (iddia 6).** PR #346 bakımcıca **reddedilmedi**, **gönderence kapatıldı**.
   "Reddedildi" bir karardır, "sahipsiz kaldı" karar yokluğudur; emsal değeri farklıdır.
5. **SEO-spam yıldız sayıları.** Arama sonuçlarında dolaşan *"85.000+ / 65.000 / 15k+ yıldız"* rakamları ikincil
   blog metinlerinden geliyordu ve **tutarsızdı**; hepsi depo sayfasından yeniden doğrulandı
   (Graphify 112.2k, CodeGraph 68.6k). İkincil kaynaktaki rakamlar **kullanılmadı**.
6. **Sunucu/istemci ayrımı bir sınıf desenidir (iddia 5).** Marksman/Oxide/IWE sınıfının tamamı Neovim/Zed/Helix +
   CLI/MCP'ye kaymış; VS Code yüzü ihmal edilmiş. "Proje ölü" ile "VS Code yüzü ölü" karıştırılmamalı.
7. **Enjeksiyon kalıcı değildir (iddia 3 + 15, bağımsız iki ekosistemde aynı sonuç).** Hem Foam'ın
   `graph.update()`'i hem Obsidian'ın çözümleme turu sentetik kenarları siliyor; her iki tarafta da
   **olay-güdümlü yeniden-enjeksiyon** şart. Bu, "enjeksiyon mümkün" bulgusunun asıl maliyetidir.
8. **403 / erişim engelleri:** `https://iwe.md/docs/` ve `.../concepts/comparison/` iki denemede de **403 Forbidden**
   (IWE belge sitesi doğrulanamadı; bulgular GitHub'a dayanıyor). `api.github.com` WebFetch üzerinden **403** verdi
   ve anonim REST çağrıları rate-limit'e takıldı; veriler `gh api`, atom feed'leri ve HTML sayfaları üzerinden
   yeniden alındı. `d2lang.com/tour/links` **404** (doğrusu `/tour/linking/`). Paywall görülmedi.
9. **Yerel deney kullanılan yerler:** iddia 7 (d2 v0.8.1-HEAD) ve iddia 8 (Graphviz 15.1.1) — SVG çıktıları
   kurulu araçlarla üretilip ayrıştırıldı; bu iki maddede kanıt web iddiası değil, doğrudan gözlemdir.
