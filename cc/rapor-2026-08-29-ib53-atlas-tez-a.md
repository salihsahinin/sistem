# IB-53 · ATLAS TEZ-A — Dış emsaller: yerel Markdown + dış SQLite referans-grafı üstünde tıklanabilir gezinme ve graf görünümü

**Künye**
- **Rol:** tez-A (Aile A, dış emsaller). **Bağımsız koşum** — kardeş tez ajanlarının (B, C…) çıktısı okunmadı; `cc/rapor-2026-08-29-ib53-atlas-tez-c.md` bilinçli olarak AÇILMADI.
- **AS-OF:** 2026-08-29. Damgasız hiçbir zaman-bağımlı iddia yok. Tarih/sürüm verisi ya kaynağın kendi tarihini taşır ya da bugünkü çekimdir.
- **Yöntem:** GitHub REST API (`repos/*`, `releases/latest`, `issues/*`), VS Code Marketplace Gallery API (`extensionquery`, flags=914), resmî doküman sayfaları, ve **depo klonlayıp kaynak koddan okuma** (Foam, Quartz, Cosma, D2, zk, vscode-markdown-mermaid). Model hafızasına dayanan tek iddia yok.
- **Dalga protokolü:** varsayılan tek hat "aday aday web araması" idi; 3 dik hat paralel koşturuldu (A: VS Code md/graf eklentileri · B: türev üreteçler/digital garden · C: kod-zekâsı + graf-DB UI) + kendi birincil-kaynak hattım. Üçü de raporladı ve **örneklem-denetiminden geçti** (§6); hat B kendi alt-hatlarının (Obsidian ekosistemi, diğer SSG'ler) hâlâ koştuğunu bildirdiği için **kısmi**dir — eksik kalan noktalar §5'te işaretli. Cosma ve Quartz iddiaları hem hat B'nin hem benim bağımsız kaynak-kodu okumamla **çift doğrulandı**.
- **Hüküm yok.** Aşağıdaki sıralama öneridir; karar Salih'indir.

---

## 1. Tek ekranda sonuç

**Profilin tamamını (①–⑤) tek pakette veren canlı bir araç BULUNAMADI.** Bu, olumsuz ama sağlam bir bulgudur: üç bağımsız hat (benim birincil kaynak taramam, hat A, hat C) aynı boşluğa yakınsadı.

Boşluğun sebebi tek bir kolonda toplanıyor: **"dış veri alabilir mi"**. Markdown/PKM araçlarının neredeyse tamamı kendi parser'ına mahkûm — graf, aracın kendi ayrıştırdığı wikilink'lerden doğar; dışarıdan kenar listesi enjekte etme yolu ya hiç yok ya belgesiz.

Bu kolonu gerçekten geçen **dört** mekanizma var (İddia numaraları §4'e gider):

| # | Mekanizma | Nasıl | Bedeli |
|---|---|---|---|
| 1 | **Cosma CSV modu** — `nodes_origin` + `links_origin` | Dış SQLite'tan iki CSV üret: düğümler (`title,id,content,…`) ve **açık kenar listesi** (`id,source,target,label,type`); `cosma modelize` tek dosyalık, **CDN'siz, tam çevrimdışı** etkileşimli HTML üretir. CSV modunda markdown parser hiç koşmaz — belgelenmiş, birinci sınıf giriş modu | Markdown dizini modunun *yerine geçer*, VS Code eklentisi yok (çıktı tarayıcıda açılır) — İ-33…İ-37, İ-84…İ-90 |
| 2 | **Foam extension exports** — `exports.foam.workspace.set()` / `registerProvider()` | `activate()` canlı `foam` nesnesini dışarı veriyor; sentetik `Resource` enjekte edersen zincir graf webview'ine kadar akıyor | **Belgesiz iç API** — Foam aktif geliştiriliyor, kırılma riski gerçek — İ-06…İ-11 |
| 3 | **Quartz v5 eklenti mimarisi** — `contentIndex.json` içindeki `links` alanı | Dört giriş noktası: `frontmatterLinks` append (en temiz) · `file.data.links` · özel emitter · derleme-sonrası JSON yaması | Çıktı statik site, VS Code değil; **graf görünümü jsDelivr CDN'ine bağımlı** (⑤ ile çelişir) — İ-38…İ-42, İ-91…İ-95 |
| 4 | **SourcetrailDB** — "keyfi veri" indeksleyicisi | Sourcetrail'in veritabanını dışarıdan yaz; graf + kod paneli + **satır-düzeyi** hazır gelir | Kütüphane **arşiv (2021-11-22)**, VS Code köprüsü **arşiv (2020-02-24)** — İ-58…İ-62 |
| 5 | **MkDocs graf eklentileri** — `graph.json` üzerine yaz | `mkdocs-obsidian-interactive-graph` derleme sonunda `site_dir/assets/javascripts/graph.json` yazar (ECharts `{nodes,links}`); `mkdocs-network-graph` `site_dir/graph/graph.json` (D3). Dosyayı ezmek yeter | Belgelenmemiş sözleşme — sürüm kırılmasına açık — İ-96…İ-98 |
| 6 | **Docusaurus `loadContent()` + `setGlobalData()`** | Resmî eklenti API'si veriyi "filesystem, remote API…" kaynağından çekmeye izin veriyor | Hazır graf bileşeni **yok** — grafı kendin yazarsın — İ-99 |

**Buna karşılık, üçüncü gereksinim (③ satır-adresli pointer) beklenenden ÇOK daha kolay:** VS Code'un kendisi hem editörde/önizlemede `[x](yol/dosya.md#L123)` biçimini hem de `vscode://file/{tam_yol}:{satır}:{sütun}` URI'sini **resmî olarak** destekliyor (İ-01…İ-05). Yani "satıra tıkla" için özel araç aramaya gerek yok; üretilen türevin doğru biçimde link basması yeterli.

**Üç bağımsız doğrulamayla kapanan negatif bulgu:** Mermaid diyagramında düğüme tıklayıp dosya açma **bugün çalışmıyor** (İ-17…İ-21). "Graf verisini mermaid'e yazıp tıklanabilir yaparım" planı geçersiz. Alternatifi D2 ve Graphviz'dir (İ-22…İ-25).

---

## 2. Eşleşme tablosu

Kolonlar: **DışVeri** = dış graf/kenar verisi enjekte edilebilir mi (KRİTİK) · **Satır** = `dosya:satır` düzeyinde gezinme · **VSC** = VS Code ilişkisi · **Canlılık** = son sürüm / son commit (AS-OF 2026-08-29) · **Profil** = ①–⑤'ten karşılananlar.

### 2.1 VS Code yerlisi Markdown/PKM araçları

| Ad | Ne yapar | DışVeri | Satır | VSC | Canlılık | Lisans | Profil | İddia |
|---|---|---|---|---|---|---|---|---|
| **Foam** | Wikilink PKM + tıklanabilir graf webview + backlink + blok çıpası | **KISMEN — belgesiz ama gerçek:** `exports.foam` → `workspace.set()`, `registerProvider()`; ayrıca `foam graph > graph.json` CLI ve MCP sunucusu | `#başlık` ✓, `#^blockid` ✓, `:123` ✗ (VS Code çekirdeğinin `#L123`'ü devrede) | **Yerli eklenti** | mp 0.44.5 · **2026-07-26**; commit 2026-08-13 | MIT | ①(kısmen) ②③④⑤ | İ-06…İ-14 |
| **Dendron** | Hiyerarşik PKM + Note/Schema Graph + pod'lar | JSON pod import/export + engine REST API — ama proje ölü | `#başlık` ✓, blok çıpası ✓ | Yerli eklenti | mp 0.124.0 · **2023-08-12**; son kod commit 2024-04-17 | Apache-2.0 | **ÖLÜ** | İ-26…İ-29 |
| **Markdown Links** (tchayen) | Yalnız graf (d3); düğüme tıkla → dosya aç | **YOK** — remark parser sabit, 8 ayar | ✗ | Yerli eklenti | mp 0.8.5 · 2025-12-30 | MIT | ②④⑤ | İ-30 |
| **tendr / WikiBonsai** | Wikiref + tree graph + web graph (2D/3D/VR) | Belgeli yol yok; graf motoru ayrı paket (`treehouze`) | doğrulanamadı | Yerli eklenti | mp 0.0.9 · **2024-12-25**; depo 2026-03-20 | GPL-3.0 | beta, riskli | İ-32 |
| **Markdown Memo** | `[[link]]` + backlink paneli — **graf YOK** | YOK | ✗ | Yerli eklenti | mp 0.3.19 · **2022-07-30** | MIT | uyuyor | İ-15 |
| **Marksman** (LSP) | Markdown dil sunucusu; **graf YOK** | YOK (LSP sınırı) | `#başlık` ✓ | Sunucu canlı / **istemci 2023-12-09** | sunucu 2026-02-08 | MIT | — | İ-15 |
| **Markdown Oxide** (LSP) | Obsidian-uyumlu PKM LSP; **graf YOK** | YOK | `#başlık`, blok ref | **İstemci bayat:** mp 1.1.0 · **2024-07-02**, 1.813 kurulum | sunucu commit 2026-08-29 | Apache-2.0 | — | İ-16 |
| **IWE** (LSP+CLI+MCP) | Markdown→bilgi grafı LSP; **VS Code'da graf görünümü YOK** | CLI/MCP yazma (markdown'a düşer) | — | mp 0.0.4 · 2025-09-09, 565 kurulum | çekirdek commit 2026-08-28 | Apache-2.0 (çekirdek) / MIT (eklenti) | — | İ-15 |
| **vscode-markdown-notes** (kortina) | Wikilink + backlink explorer; graf YOK | YOK | ✗ | Yerli eklenti | mp 0.0.27 · **2023-04-30** | GPL-3.0 | durgun | İ-15 |
| **CodeGraphy** | Dosya bağlantılarının D3 kuvvet grafı (VS Code panelinde) | YOK (kendi tarayıcısı) | ✗ | **Yerli eklenti** | mp 5.16.4 · **2026-08-05**, 10.935 kurulum ⚠ depo `CodeGraphyV2` 2023-06-10'da durmuş | MIT | ④⑤ | İ-31 |
| **VS Code çekirdeği (eklentisiz)** | `#L123` bağlantıları, `DocumentLinkProvider`, `vscode://` URI, yerleşik Mermaid | Tamamen sende | **✓ EN İYİ** | — | Mermaid 1.121'de çekirdeğe girdi (2026-05-20) | MIT | ②③④⑤ | İ-01…İ-05, İ-21 |

### 2.2 Türev üreteçleri / digital garden / statik yayıncılar

| Ad | Ne yapar | DışVeri | Satır | VSC | Canlılık | Lisans | Profil | İddia |
|---|---|---|---|---|---|---|---|---|
| **Cosma** | md/CSV/JSON → tek dosyalık etkileşimli HTML graf ("cosmoscope") | **EVET — sınıfın en iyisi:** `select_origin: csv` + ayrı `nodes_origin` / `links_origin` CSV'leri = açık dış kenar listesi | `content` kolonu markdown; `:123` doğrulanmadı | Eklenti yok (çıktı tarayıcıda) | 2.6.1 · **2026-03-17** | GPL-3.0 **OR** CeCILL-2.1 | ①②⑤ (④ hayır) | İ-33…İ-37 |
| **Quartz v5** | md → statik site + yerel/global graf | **EVET (eklenti mimarisi):** 4 giriş noktası — `frontmatterLinks` append · `file.data.links` · özel emitter · `contentIndex.json` post-yaması | `[[wikilink]]` ✓; graf kenarında `#başlık` **atılır** | Eklenti yok | package.json **5.0.0**, `v5.0.0` etiketi 2026-03-14; commit 2026-08-18 ⚠ GitHub'daki son *release* v4.0.8 (2023-08-21) — yanıltıcı | MIT | ①② (⑤ **kısmen ihlal**: graf jsDelivr CDN'i çeker) | İ-38…İ-42, İ-91…İ-95 |
| **Logseq** | Outliner PKM + graf | **2.0'da yön değişti:** DB (SQLite) kanonik oldu, md dosyaları artık kaynak-doğru değil | — | Eklenti yok | **2.0.1 beta · 2026-07-13**; commit 2026-08-28 | AGPL-3.0 | ② ihlal riski (kaynak-gövde artık dosya değil) | İ-43…İ-45 |
| **zk** | SQLite indeksli düz-metin not asistanı; `zk graph --format json`, `zk lsp` | Girdi kendi md dizini; **çıktı JSON graf** — türev üreteci olarak güçlü | LSP gezinme | `zk-vscode` **2024-01-04**, 28 yıldız | commit 2026-08-24, 2.777 yıldız | GPL-3.0 | ②③(kısmen)⑤ | İ-46…İ-49 |
| **obsidian-dataview** | Obsidian içi sorgu/türev motoru | Obsidian kasası; kum havuzu dışına çıkamaz | ✗ | ✗ | 0.5.70 · **2025-04-07**; commit 2025-11-17 | MIT | — | İ-50 |
| **Obsidian graf + `resolvedLinks` enjeksiyonu** | Eklenti çalışma-zamanında sentetik kenar enjekte edebiliyor | **EVET ama belgesiz iç API** (`metadataCache.resolvedLinks`) | ✗ | ✗ (Obsidian kapalı kaynak) | Juggl commit **2025-02-27** | Juggl GPL-3.0; Obsidian tescilli | ⑤ ihlal | İ-51…İ-52 |
| **SilverBullet** | Kendi datastore + Lua sorgu motoru olan md wiki | plug sistemi var (bu turda derinlemesine doğrulanmadı) | — | ✗ | 2.10.0 · 2026-07-28; commit 2026-08-29 | MIT | ⑤ | İ-53 |
| **Emanote** | md → statik site (Neuron'un halefi) | kendi parser'ı | — | ✗ | 1.4.0.0 · **2025-08-19** | AGPL-3.0 | ⑤ | İ-54 |
| **MarkdownDB** | md klasörünü **SQLite'a indeksler** (frontmatter, tag, link, backlink) + JS API | Ters yön: md→SQLite. Köprü parçası olarak değerli | — | ✗ | commit 2026-05-21, 520 yıldız | MIT | ② | İ-55 |
| **Flowershow** | md → site yayıncı | kendi parser'ı | — | ✗ | commit 2026-08-21 | AGPL-3.0 | ⑤ | İ-56 |
| **SSG çekirdek sınıfı** (Starlight, VitePress, Sphinx/MyST, Quarto) | md → site; eklenti API'leri var ama **hazır bilgi-grafı bileşeni yok** | teknik olarak evet | — | ✗ | hepsi canlı (2026-08 commit'leri) | MIT/BSD çoğunlukla | ②⑤ | İ-57 |
| **Neuron** | Zettelkasten yayıncı | — | — | — | **Emanote tarafından emekli edildi** (depo açıklaması) | AGPL-3.0 | emekli | İ-54 |

### 2.3 MkDocs / Docusaurus graf eklentileri (hat B, kaynak-kodu doğrulamalı)

Bu sınıfın önemi: **hepsi grafı bir JSON dosyasına yazıp tarayıcıda okuyor.** Yani dış veri enjeksiyonu "o dosyayı üzerine yaz" kadar basit — ama sözleşme belgelenmemiş.

| Ad | Graf verisini nereye yazar (dış enjeksiyon kapısı) | `[[wl]]` · `#başlık` · `:123` | Sürüm / tarih | Lisans | İddia |
|---|---|---|---|---|---|
| **mkdocs-obsidian-interactive-graph** | **`site_dir/assets/javascripts/graph.json`** — ECharts biçimi `{nodes:[{id,name,symbolSize,value}], links:[{source,target}]}` (plugin.py:100) | ✓ · ✓ · ✗ | 0.3.2 · 2026-02-10 | MIT | İ-96 |
| **mkdocs-network-graph** | **`site_dir/graph/graph.json`** — D3; `on_post_build`'da yazılır | ✓ · ✗ · ✗ | 1.0.3 · 2025-09-11 | MIT | İ-97 |
| **mkdocs-graphviz** | DOT kaynağı → **derleme-anında inline SVG, JS yok, tam deterministik** | ✗ · — · ✗ | 2.0.2 · 2026-08-14 | **GPL-3.0-or-later** ⚠ | İ-98 |
| **mkdocs-material** | Tema; **graf YOK** | ✗ · ✓ · kısmen | 9.7.7 · 2026-07-17 | MIT | — |
| **mkdocs-roamlinks** / **obsidian-bridge** / **obsidian-support** | Wikilink dönüşümü; bellekte çalışır, kaynak dosyaya dokunmaz; graf yok | ✓ · kısmen · ✗ | 0.3.2 · 2023-04-19 / 1.3.1 · 2025-08-13 / 1.4.1 · 2024-09-20 | MIT / BSD-3 / MIT | — |
| **Docusaurus** | `loadContent()` *"fetch from data sources (filesystem, remote API…)"* + `setGlobalData()` → **API düzeyinde en temiz enjeksiyon**, ama grafı kendin yazarsın | ✗ · ✓ · ✗ | 3.10.2 · 2026-07-10 | MIT | İ-99 |
| **docusaurus-graph** | `static/docusaurus-graph.json` yamalanabilir ⚠ ama eklenti **yalnız frontmatter `sources:`/`references:` okur** → düz md deposunda graf BOŞ çıkar | ✗ · ✗ · ✗ | 2.0.0 · 2024-11-22 | MIT | İ-100 |

**MkDocs'un belgelenmiş enjeksiyon kapıları:** `on_files` (*"Use this event to add, remove, or alter files in the collection"*), `on_env`, `on_post_build` (*"Use this event to call post-build scripts"*); paketleme bile gerekmez — `hooks:` anahtarı yerel Python betiklerini eklenti örneği olarak yükler (İ-101).

### 2.4 Kod-zekâsı / satır-düzeyi harita (hat C + kendi doğrulamam)

| Ad | Ne yapar | DışVeri | Satır | VSC | Canlılık | Lisans | İddia |
|---|---|---|---|---|---|---|---|
| **Sourcetrail** (petermost forku) | Etkileşimli kaynak gezgini: graf + kod paneli | **EVET, SourcetrailDB ile** | **✓** | `vsce-sourcetrail` **ARŞİV 2020-02-24**; mp 0.0.2 · **2017-06-27** | fork sürüm **2026.6 · 2026-06-11**; README'de 2026-08-01 tarihli "yavaşlıyorum" notu | GPL-3.0 | İ-58…İ-62 |
| **SourcetrailDB** | Sourcetrail DB'sini dışarıdan yazma SDK'sı — *"or other kind of data"* | **EVET — profil için en doğrudan tarihsel emsal** | ✓ | — | **ARŞİV, 2021-11-22** | Apache-2.0 | İ-58…İ-59 |
| **Sourcegraph** | Kod arama/gezinme platformu | SCIP yükleme | ✓ | eklenti | **KAPALI KAYNAK** — `repos/sourcegraph/sourcegraph` bugün 404; public snapshot arşiv, son push 2024-09-02 | Enterprise (kapalı) | İ-63…İ-64 |
| **SCIP** | Dil-bağımsız kod indeksleme protokolü (Protobuf) | **EVET** (kendi indeksini yazarsın) | ✓ (`Occurrence.range`) | — | v0.9.0 · 2026-06-29; commit 2026-08-28; **`scip-code` org'una taşındı, kuruluş 2026-01-09** | Apache-2.0 | İ-70 |
| **Kythe / Glean** | Çapraz-referans olgu depoları | **EVET** (kendi olgularını yazarsın) | ✓ | Glean'de LSP+VS Code | Kythe v0.0.76 · 2026-07-16 · Glean commit 2026-08-29 | Apache-2.0 / BSD | İ-66 |
| **stack-graphs** (GitHub) | Precise code navigation motoru | — | ✓ | — | **ARŞİV**, son push 2025-09-09 | Apache-2.0 | İ-67 |
| **universal-ctags** | Sembol → `dosya:satır` etiket dosyası | Etiket dosyası düz metin | **✓** | 3. parti | v6.2.1 · 2025-10-25; commit 2026-08-26 | GPL-2.0 | İ-68 |
| **tree-sitter** | Artımlı ayrıştırıcı; satır/sütun taşır | Sorgularla her şeyi çıkarırsın | ✓ | — | commit 2026-08-29 | MIT | İ-68 |
| **aider repo-map** | tree-sitter + graf sıralama (PageRank) ile deterministik kod haritası | Girdi kaynak kod | dosya başlıkları (satır no yok) | ✗ | Aider commit 2026-05-22; `RepoMapper` klonu 2025-12-08 | Apache-2.0 / MIT | İ-70 |
| **CodeSee** | Etkileşimli kod haritaları | — | — | — | **ÜRÜN ERİŞİLEMEZ** — GitKraken 2024-05-14'te satın aldı; `www.codesee.io` bugün **HTTP 404**, `app.codesee.io` Cloudflare Access arkasında | Tescilli | İ-71…İ-74 |
| **OpenGrok / CodeCompass / Sourcebot** | Kendi barındırılan kod arama + çapraz referans | kaynak depolar | ✓ | — | üçü de 2026-08 commit'i | CDDL-1.0 / GPL-3.0 / **FSL-1.1 (OSI-açık değil)** | İ-70 |

### 2.5 Graf render / dış veri yüzeyleri

| Ad | Ne yapar | DışVeri | `vscode://` linki basabilir mi | Canlılık | Lisans | İddia |
|---|---|---|---|---|---|---|
| **D2** | Metin→diyagram dili; `link:` ile tıklanabilir şekil | EVET (metni sen üretirsin) | **EVET** — SVG'ye `<a href>` olarak XML-escape ile basıyor, **şema beyaz listesi YOK** (kaynaktan doğrulandı) | v0.8.2 · **2026-08-28**, 25.101 yıldız; VS Code eklentisi 2026-08-03 | MPL-2.0 (eklenti BSD-3) | İ-22…İ-24 |
| **Graphviz** | DOT→SVG; `URL` özniteliği düğüm/kenar/küme/graf üzerinde | EVET | **EVET** (`svg`, `cmap/i*map`, `ps2` biçimlerinde) | — | EPL | İ-25 |
| **Mermaid** | Metin→diyagram; VS Code 1.121'den beri **çekirdekte** | EVET | **HAYIR** — `securityLevel` ayarlanmıyor → varsayılan `strict` → `click` devre dışı; PR #346 merge edilmeden kapandı, issue #332 hâlâ açık | çekirdek 1.121 (2026-05-20); mermaid v11 | MIT | İ-17…İ-21 |
| **Datasette** | SQLite dosyasını salt-okunur web UI + JSON API yapar | **EVET (doğrudan .db)** | Hazır eklentiyle hayır (şema filtresi); ~20 satırlık `render_cell` eklentisiyle evet | 0.65.3 · 2026-08-06 | Apache-2.0 | İ-75…İ-77 |
| **Cytoscape.js / sigma.js / vis-network / force-graph** | Graf çizim kütüphaneleri (JSON düğüm/kenar) | **EVET** | **EVET** (tıklama handler'ı serbest) | cytoscape v3.34.2 · 2026-08-25 · vis-network v10.1.2 · 2026-08-19 · sigma 2026-08-20 | MIT / Apache-2.0 | İ-78 |
| **Kùzu** | Gömülü property-graph VT | EVET | — | **ARŞİV, 2025-10-10**; Apple satın aldı; fork `Kineviz/bighorn` canlı | MIT | İ-79 |
| **Cosmograph** | WebGL + gömülü DuckDB ile devasa graf | EVET (CSV/Parquet) | serbest | 2.5.1 · 2026-08-14 | **CC-BY-NC-4.0 — ticari kullanım YOK** | İ-80 |
| **Gephi / Gephi Lite** | Masaüstü / tarayıcı graf analiz | EVET (CSV/GEXF/GraphML) | ✗ | v0.11.2 · 2026-05-09 | GPL-3.0 | İ-81 |
| **Neo4j Bloom / NeoDash / Memgraph Lab** | Graf-VT üstü keşif UI'ları | **HAYIR — çalışan sunucu gerekir, dosya okumaz** | ✗ | NeoDash commit 2026-08-14 | ticari / Apache-2.0 | İ-82 |

**Toplam taranan aday: 50 satır** (bazı satırlar birden çok aracı topluyor: SSG çekirdek sınıfı 4, wikilink-dönüştürücü MkDocs eklentileri 3, graf kütüphaneleri 4, OpenGrok/CodeCompass/Sourcebot 3, Neo4j/NeoDash/Memgraph 3 → **tekil araç ≈ 70**) (tabloların satır sayısı; SSG sınıfı 6 aracı tek satırda topluyor).

---

## 3. En güçlü 3 aday — derinlik

### 3.1 Foam (`foam.foam-vscode`) — profilin ④'ünü tek başına karşılayan tek canlı aday

Foam, VS Code'un içinde yaşayan wikilink tabanlı bir PKM eklentisidir: `Foam: Show Graph` komutuyla tıklanabilir bir graf webview'i açar, backlink paneli tutar, `[[not#başlık]]` ve `[[not#^blokid]]` çapalarını çözer, blok çapası yeniden adlandırmasında tüm referansları günceller. Profil açısından kritik olan şey ise dokümantasyonda değil, kaynak kodda: `packages/foam-vscode/src/extension.ts` içindeki `activate()` fonksiyonu `return { extendMarkdownIt, foam }` ile canlı `foam` nesnesini VS Code extension exports'una veriyor (satır 212-219, commit `3452c98`, 2026-08-13). O nesnenin tipi `interface Foam { services; workspace: FoamWorkspace; graph: FoamGraph; tags }`; `FoamWorkspace` üzerinde `registerProvider(provider: ResourceProvider)` (workspace.ts:57) ve `set(resource: Resource)` (workspace.ts:127) **public** metotlar, `FoamGraph` ise `fromWorkspace()` ile bu değişimlere abone. `ResourceProvider` arayüzü dört metottan ibaret — `supports`, `readAsMarkdown`, `fetch`, `resolveLink` — yani kendi link çözümleyicini takabilirsin. Pratik sonuç: dış SQLite'tan okuduğun referans grafını sentetik `Resource`'lara çevirip `workspace.set()` ile enjekte edersen, kenarlar Foam'ın graf ekranına kadar akar; `ResourceLink` tipi zaten `range: Range` (satır+sütun) taşıdığı için model satır-farkındadır. **Bedeli:** bu yol Foam'ın hiçbir kullanıcı dokümanında geçmiyor; `docs/user/` altında "extension API / plugin API" başlığı yok. Foam aktif geliştirilen bir proje olduğu için (Ağustos 2026'da commit'ler, marketplace 0.44.5 / 2026-07-26, 272.027 kurulum) iç API'nin kırılma riski gerçek ve sürekli. Daha az kırılgan iki alternatif yol Foam'ın kendi içinde duruyor: `foam-cli`'nin `foam graph > graph.json` komutu (grafı deterministik JSON olarak dışa verir) ve `@foam/mcp` kütüphanesi (`get_connections`, `traverse_graph`, `get_graph_summary`, `get_orphans` araçları). Bunlar "graf enjekte etme" değil, "graf okuma/üretme" kapılarıdır — türev üretip Foam'ın kendi parser'ına parse ettirme desenine hizmet ederler.

### 3.2 Cosma (`graphlab-fr/cosma`) — dış kenar listesini AÇIKÇA kabul eden tek araç

Cosma, EHESS/Graphlab çevresinden çıkan bir "cosmoscope" üreticisidir: girdiyi okur, düğüm-kenar modeli kurar, ve **tek dosyalık, bağımsız, etkileşimli bir HTML** üretir (`cosma modelize`). Profil için belirleyici olan, README'nin ilk cümlesinde duruyor: *"Cosma reads files (.md, .csv and .json) to extract Records"*. CSV modunda mimari tam olarak profilin istediği şeydir: yapılandırmada `select_origin: csv` seçilir, `nodes_origin` düğüm CSV'sini, `links_origin` ise **açık kenar listesini** gösterir. Kenar CSV'sinin kolonları `id, source, target, label, type`; düğüm CSV'sinde `title` zorunlu, `content` kolonu kaydın metinsel gövdesini (markdown) taşır, ayrıca `type:<ad>`, `tag:<ad>`, `meta:<ad>`, `time:begin/end` kolonları var. Yani dış SQLite'ından iki CSV dökersen — biri gövde, biri graf — Cosma bunları LLM'siz, deterministik biçimde tıklanabilir bir graf yüzeyine çevirir ve kaynak md dosyalarına hiç dokunmaz (②). Lisans GPL-3.0 **veya** CeCILL-2.1, tamamen yerel çalışır (⑤). **İki ciddi uyarı:** (a) kullanıcı el kitabı CSV modunu birebir *"This is an alternative to using Markdown files"* diye tanımlıyor — yani md dizini modu ile CSV modu aynı anda koşmuyor; md gövdesini de CSV'ye taşımak zorundasın. (b) VS Code ilişkisi **yok**; cosmoscope tarayıcıda açılır, dolayısıyla ④ karşılanmıyor — `content` alanına gömeceğin `vscode://file/...:123` bağlantılarının HTML'e sağ salim çıkıp çıkmadığını bu turda **doğrulayamadım** (§5'te bayraklı). Canlılık orta: 2.6.1 sürümü 2026-03-17, 190 yıldız — küçük ama akademik olarak sürdürülen bir proje ([Zenodo DOI kaydı var](https://doi.org/10.5281/zenodo.5920616)). **Bağımsız kaynak-kodu doğrulaması dört ek noktayı açığa çıkardı:** (a) `controllers/modelize.js:165-172`'de `csv` dalı yalnız `processNodes` + `processLinks` çağırır — **markdown parser hiç koşmaz**, yani "parser'ına mahkûm olma" riski tanım gereği yok; (b) üretilen `cosmoscope.html` CSS'i, JS bundle'ını ve görselleri (base64) gömer, **hiçbir CDN çağrısı yoktur** — Quartz'ın grafının aksine tam çevrimdışı çalışır; (c) graf verisi HTML'e `const data = {{ graph.data | dump | safe }}` olarak gömülür, yani **derleme sonrası bu değişkeni yamalamak beşinci bir enjeksiyon noktasıdır**; (d) `core/utils/getGraph.js:110`'daki `if (!graph.hasNode(link.target))` koşulu gereği hedefi `nodes.csv`'de bulunmayan kenar `brokenEdges`'e düşer ve çizilmez — hayalet düğüm üretilmez, düğümü de eklemek zorundasın. Ayrıca `--citeproc` + `references_as_nodes: true` ikinci bir deterministik kenar üreteci verir: kaynakça referansları düğüm, atıflar kenar olur.

### 3.3 VS Code çekirdeği + deterministik türev (D2/Graphviz) — "araç seçme, türev üret" yolu

Bu, bir ürün değil bir desen; ama üç bağımsız hattın hepsinde en sağlam seçenek olarak çıktığı için buraya giriyor. Dayanağı üç resmî destek noktası: **(1)** VS Code'un markdown desteği `[metin](./dosya.md#L3)` biçimini yerleşik olarak çözüyor ve dosyayı 3. satırda açıyor (issue #40140, 2017-12-13 kapatıldı); `.md` dışı dosyalar için de çalışıyor (issue #125320, 2021-10-08 düzeltildi, raporlayan tarafından `/verified` edildi); sütun için `#L123,45` biçimi de destekli (vscode-markdown-languageservice#29, bakımcı mjbvz'nin 2022-09-16 tarihli yorumu: *"This is actually already supported using the syntax: `#L123,45`"*). **(2)** Resmî VS Code dokümanı, "Opening VS Code with URLs" bölümünde birebir `vscode://file/{full path to file}:line:column` kalıbını ve `vscode://file/c:/myProject/package.json:5:10` örneğini veriyor — yani profilin istediği **iki nokta üst üste** sözdizimi tam olarak bu URI'de yaşıyor; HTML/SVG'den VS Code'un belirli satırına atlamak resmî bir yol. **(3)** Terminalde de `file:1:2` biçimi belgeli. Grafiksel yüzey için ise Mermaid **kullanılamaz** (aşağıda), buna karşılık **D2** kaynak koddan doğrulandığı üzere `link:` değerini SVG'ye yalnızca XML-escape'leyerek `<a href="…" xlink:href="…">` olarak basıyor — hiçbir şema beyaz listesi yok (`d2renderers/d2svg/d2svg.go:1235,1362,1685`, commit `07cd321`, 2026-08-28) — ve **Graphviz** `URL` özniteliğini `svg`, `cmap/i*map`, `ps2` biçimlerinde düğüm, kenar, graf ve küme üzerinde destekliyor. Bu desenin bir yan faydası, hazır statik-site graflarının gizli bağımlılığından kaçınmaktır: Quartz'ın graf bileşeni `d3` ve `pixi.js`'i **çalışma anında jsDelivr CDN'inden** çeker (`graph.inline.ts:35-36`), yani graf görünümü internet ister — profilin ⑤ (yerel) maddesiyle doğrudan çelişen, dokümantasyonda öne çıkarılmayan bir kısıt. Bu desenin bedeli açıktır: hazır bir ürün almıyorsun, türev üreticisini kendin yazıyorsun; kazancı da açıktır: hiçbir üçüncü parti iç API'sine bağlanmıyorsun, ①–⑤'in tamamı senin kontrolünde, ve ② (deterministik, LLM'siz, kaynağa dokunmayan) tanım gereği sağlanıyor.

---

## 4. İDDİALAR (numaralı, tek cümle, kanıt-URL'li)

> Antitez aşaması bu listeyi kullanacak. Her satır AS-OF 2026-08-29'dur; kaynağın kendi tarihi varsa parantezde.

**A. VS Code'un yerleşik satır-adresli gezinmesi (③)**

1. VS Code markdown'da `[b](./b.md#L3)` biçimi dosyayı 3. satırda açar; talep 2017-12-13'te "completed" olarak kapatıldı — https://github.com/microsoft/vscode/issues/40140
2. Satır-numarası fragment'i `.md` dışı dosyalar için de çalışır; kusur 2021-10-08'de düzeltildi ve raporlayan 2021-10-12'de `/verified` yazdı — https://github.com/microsoft/vscode/issues/125320
3. Sütun için `#L123,45` biçimi desteklidir; bakımcı mjbvz 2022-09-16'da birebir *"This is actually already supported using the syntax: `#L123,45`"* yazıp issue'yu kapattı — https://github.com/microsoft/vscode-markdown-languageservice/issues/29
4. Resmî VS Code dokümanı "Opening VS Code with URLs" bölümünde `vscode://file/{full path to file}:line:column` kalıbını ve `vscode://file/c:/myProject/package.json:5:10` örneğini verir — https://code.visualstudio.com/docs/configure/command-line
5. VS Code terminali `file:1:2` gibi yaygın satır/sütun biçimlerini tıklanabilir yapar (resmî doküman, "Links" bölümü) — https://code.visualstudio.com/docs/terminal/basics

**B. Foam**

6. Foam'ın `activate()` fonksiyonu `return { extendMarkdownIt, foam }` ile canlı Foam nesnesini extension exports olarak dışarı verir (extension.ts:212-219, commit `3452c98`, 2026-08-13) — https://github.com/foambubble/foam/blob/main/packages/foam-vscode/src/extension.ts
7. `Foam` arayüzü `services`, `workspace: FoamWorkspace`, `graph: FoamGraph`, `tags` alanlarını taşır — https://github.com/foambubble/foam/blob/main/packages/foam-core/src/model/foam.ts
8. `FoamWorkspace` sınıfında `registerProvider()` (satır 57) ve `set(resource)` (satır 127) public metotlardır ve `onDidAdd`/`onDidUpdate` olaylarını tetikler — https://github.com/foambubble/foam/blob/main/packages/foam-core/src/model/workspace.ts
9. `ResourceProvider` arayüzü dört metottan oluşur: `supports`, `readAsMarkdown`, `fetch`, `resolveLink` — yani dış çözümleyici takılabilir — https://github.com/foambubble/foam/blob/main/packages/foam-core/src/model/provider.ts
10. `ResourceLink` tipi `range: Range` alanı taşır, yani Foam'ın bağlantı modeli satır/sütun farkındadır — https://github.com/foambubble/foam/blob/main/packages/foam-core/src/model/note.ts
11. Foam'ın `docs/user/` dizininde belgelenmiş bir "extension API / plugin API" sayfası **yoktur**; enjeksiyon yolu yalnız kaynak koddan çıkarılmıştır (bulunamadı) — https://github.com/foambubble/foam/tree/main/docs/user
12. `foam-cli` grafı deterministik JSON olarak dışa verir: `foam graph > graph.json` (graph.ts:17) — https://github.com/foambubble/foam/blob/main/packages/foam-cli/src/commands/graph.ts
13. Foam marketplace'te 0.44.5 sürümüyle 2026-07-26'da güncellendi ve 272.027 kuruluma sahiptir (Gallery API çekimi); GitHub'daki son release etiketi ise `vscode@0.40.4`/2026-05-14 olduğu için release sayfası canlılığı **eksik gösterir** — https://marketplace.visualstudio.com/items?itemName=foam.foam-vscode · https://github.com/foambubble/foam/releases
14. GitHub API'ye göre Foam'ın lisansı `NOASSERTION` görünür ama LICENSE dosyasının ilk satırı *"The MIT Licence (MIT)"*tir, yani gerçek lisans MIT'tir — https://github.com/foambubble/foam/blob/main/LICENSE

**C. Graf görünümü OLMAYAN VS Code Markdown araçları (eleme)**

15. Marksman, Markdown Oxide, IWE, vscode-markdown-notes ve Markdown Memo'nun hiçbirinde graf/harita görünümü yoktur; ayrıca VS Code istemcileri bayattır (marksman-vscode 2023-12-09 · markdown-oxide mp 1.1.0/2024-07-02 · iwe mp 0.0.4/2025-09-09 · kortina mp 0.0.27/2023-04-30 · memo mp 0.3.19/2022-07-30) — Gallery API çekimi; https://github.com/artempyanykh/marksman-vscode · https://github.com/Feel-ix-343/markdown-oxide · https://github.com/iwe-org/vscode-iwe · https://github.com/kortina/vscode-markdown-notes · https://github.com/svsool/memo
16. Markdown Oxide'ın Rust dil sunucusu bugün commit almasına rağmen (pushed 2026-08-29, Apache-2.0, 2.275 yıldız) VS Code istemcisi 2024-07-02'den beri güncellenmemiştir ve yalnızca 1.813 kuruluma sahiptir — https://github.com/Feel-ix-343/markdown-oxide

**D. Mermaid — tıklanabilirlik negatifi (üç bağımsız doğrulama)**

17. Mermaid'in `click nodeId "url"` işlevi resmî dokümanda *"disabled when using `securityLevel='strict'` and enabled when using `securityLevel='loose'`"* olarak tanımlıdır — https://mermaid.js.org/syntax/flowchart.html
18. VS Code'un Mermaid oluşturucusunun kaynak kodunda `securityLevel` **hiçbir yerde geçmez**; `loadMermaidConfig()` yalnızca `startOnLoad` ve `theme` ayarlar (shared-mermaid/index.ts:127-135, commit `9f4d37d`, 2026-05-20) — dolayısıyla varsayılan `strict` geçerlidir ve `click` devre dışıdır — https://github.com/mjbvz/vscode-markdown-mermaid/blob/master/src/shared-mermaid/index.ts
19. Mermaid'e VS Code'da tıklanabilir dosya bağlantısı ekleyen PR #346, 2026-06-25'te **merge edilmeden** kapatıldı — https://github.com/mjbvz/vscode-markdown-mermaid/pull/346
20. Bunu talep eden issue #332 (2025-08-06) bugün hâlâ **açıktır** — https://github.com/mjbvz/vscode-markdown-mermaid/issues/332
21. Mermaid, VS Code 1.121 (2026-05-20) ile `Mermaid Markdown Features` adlı yerleşik eklenti olarak çekirdeğe alındı; sürüm notu *"We've merged Matt Bierner's Markdown Preview Mermaid Support extension into VS Code as a new built-in extension"* diyor — https://code.visualstudio.com/updates/v1_121

**E. Mermaid alternatifleri — tıklanabilir diyagram**

22. D2, şekil `link` değerini SVG'ye `<a href="%s" xlink:href="%[1]s">` olarak yalnızca `svg.EscapeText` ile basar; şema (protokol) beyaz listesi yoktur (d2svg.go:1235, 1362, 1685; commit `07cd321`, 2026-08-28) — https://github.com/terrastruct/d2/blob/master/d2renderers/d2svg/d2svg.go
23. D2 dokümanı "Links" bölümünde *"Links are like tooltips, except you click to go to an external link"* der — https://d2lang.com/tour/interactive/
24. D2 canlıdır: v0.8.2 sürümü 2026-08-28'de yayımlandı, MPL-2.0, 25.101 yıldız; VS Code eklentisi `terrastruct/d2-vscode` (BSD-3) 2026-08-03'te güncellendi — https://github.com/terrastruct/d2/releases · https://github.com/terrastruct/d2-vscode
25. Graphviz'in `URL` özniteliği düğüm, kenar, graf ve küme üzerinde geçerlidir ve *"At present, used in `ps2`, `cmap`, `i*map` and `svg` formats"* — https://graphviz.org/docs/attrs/URL/

**F. Dendron — ölü**

26. Dendron'un README'sinin en üstünde bakımcıların kendi cümlesi bulunur: *"Dendron is currently in maintenace only, active development has ceased."* — https://github.com/dendronhq/dendron
27. Kurucu Kevin Lin Şubat 2023'te Discussion #3890'da *"Dendron the project will be in maintenance mode moving forward"* ve *"as a business, we were ultimately not able to find product market fit"* yazdı — https://github.com/dendronhq/dendron/discussions/3890
28. Dendron'un marketplace sürümü 0.124.0'dır ve **2023-08-12**'den beri güncellenmemiştir (168.625 kurulum); `master` dalındaki son gerçek kod commit'i 2024-04-17'dir (lisans güncellemesi) — https://marketplace.visualstudio.com/items?itemName=dendron.dendron · https://github.com/dendronhq/dendron/commits/master
29. Dendron'un şirket olarak **resmen tasfiye edildiğine** dair birincil kayıt **bulunamadı**; doğrulanan tek şey "bakım modu + pivot" beyanıdır — https://github.com/dendronhq/dendron/discussions/3890

**G. Diğer VS Code graf eklentileri**

30. Markdown Links (tchayen) grafı yalnız kendi remark parser'ından üretir, dış veri girişi yoktur ve başlıksız dosyalar grafta hiç görünmez; mp 0.8.5 / 2025-12-30, MIT — https://github.com/tchayen/markdown-links
31. CodeGraphy marketplace'te 5.16.4 / 2026-08-05 ile canlıdır (10.935 kurulum) ama GitHub deposu `joesobo/CodeGraphyV2` 2023-06-10'dan beri push almamıştır — bu iki tarih arasındaki fark açıklanamadı — https://marketplace.visualstudio.com/items?itemName=codegraphy.codegraphy · https://github.com/joesobo/CodeGraphyV2
32. tendr (WikiBonsai) marketplace'te 0.0.9 / 2024-12-25'te durmuştur ve README kendini beta ilan eder; depo (GPL-3.0) 2026-03-20'de push almıştır — https://github.com/wikibonsai/vscode-tendr

**H. Cosma — dış kenar listesi**

33. Cosma README'si birebir *"Cosma reads files (.md, .csv and .json) to extract Records"* der — https://github.com/graphlab-fr/cosma
34. Cosma yapılandırmasında `select_origin` değeri `csv` olabilir ve `nodes_origin` (düğüm CSV'si) ile `links_origin` (**kenar CSV'si**) ayrı ayrı verilir — https://github.com/graphlab-fr/cosma/blob/main/docs/user-manual.md (satır 132-137)
35. Kenar CSV'sinin kolonları `id` (zorunlu), `source` (zorunlu), `target` (zorunlu), `label`, `type`'tır; düğüm CSV'sinde `title` zorunlu, `content` kolonu kaydın metinsel gövdesini taşır — aynı el kitabı, "Metadata for nodes" ve "Metadata for links" bölümleri
36. El kitabı CSV modunu birebir *"This is an alternative to using Markdown files"* diye tanımlar — yani md dizini modu ile CSV modu birlikte koşmaz — aynı kaynak, "Creating content: tabular data (CSV)" bölümü
37. Cosma'nın lisans dosyası `GPL-3.0 OR CeCILL-2.1` ifadesini taşır; son sürüm 2.6.1, 2026-03-17 — https://github.com/graphlab-fr/cosma/releases

**I. Quartz**

38. Quartz'ın `package.json`'ındaki sürüm bugünkü `main` dalında **5.0.0**'dır (commit `075afd3`, 2026-08-12); GitHub'daki son *release* ise hâlâ v4.0.8 / 2023-08-21'dir, bu yüzden release tarihi canlılık ölçüsü olarak yanıltıcıdır — https://github.com/jackyzha0/quartz/blob/v4/package.json · https://github.com/jackyzha0/quartz/releases
39. Quartz v5'te Graph View artık çekirdek değil bir **topluluk eklentisidir**; doküman birebir *"The Graph View is now a community plugin. This demonstrates how external plugins can extend Quartz functionality while serving as a reference implementation for plugin developers."* der — https://github.com/jackyzha0/quartz/blob/v4/docs/features/graph%20view.md
40. Graf ve arama bileşenlerinin verisi `contentIndex.json` dosyasından gelir: *"The plugin also emits a `contentIndex.json` file which is used by dynamic frontend components like search and graph."* — https://github.com/jackyzha0/quartz/blob/v4/docs/plugins/ContentIndex.md
41. `ContentDetails` tipi `links: SimpleSlug[]` alanı taşır ve emitter bunu `data.links` üzerinden doldurur (emitter.ts:20-24, 149) — yani dış kenar listesi bu alandan enjekte edilebilir — https://github.com/quartz-community/content-index/blob/main/src/emitter.ts
42. Quartz eklentileri `npx quartz plugin add github:<org>/<repo>` ile kurulur ve `quartz.config.yaml` içinde etkinleştirilir — https://github.com/jackyzha0/quartz/blob/v4/docs/features/graph%20view.md

**J. Logseq — yön değişikliği**

43. Logseq 2.0.1 "Beta (DB version)" sürümü 2026-07-13'te yayımlandı — https://github.com/logseq/logseq/releases
44. Resmî Logseq dokümanı DB graf işlevselliğini 28 Nisan 2026 itibarıyla tanımlar ve düğüm/özellik/etiket modelini anlatır — https://github.com/logseq/docs/blob/master/db-version.md
45. DB sürümünde SQLite veritabanının kanonik kaynak hâline geldiği ve markdown dosyalarının artık elle düzenlenen kaynak olmadığı iddiası **ikincil kaynaklıdır**; Logseq'in kendi sürüm notu yalnızca "iki sürüme ayrılıyoruz" der — https://logseq.io/p/e3YDyX5AYr · ikincil: https://kompozy.io/news/logseq-2-0-db-version-beta [ikincil, birincil doğrulama yapılamadı]

**K. zk — SQLite indeksli düz-metin**

46. `zk` not defterinde `.zk/notebook.db` bir SQLite veritabanıdır (resmî doküman) — https://github.com/zk-org/zk/blob/main/docs/notes/notebook.md
47. `zk graph` komutu grafı JSON olarak üretir (`Format` alanı `enum:"json" required`, graph.go:18) — https://github.com/zk-org/zk/blob/main/internal/cli/cmd/graph.go
48. `zk` bir LSP sunucusu içerir (`internal/cli/cmd/lsp.go`) ve VS Code için `zk-org/zk-vscode` eklentisi vardır, ancak eklenti **2024-01-04**'ten beri push almamıştır (28 yıldız) — https://github.com/zk-org/zk-vscode
49. `zk` deposu canlıdır: son push 2026-08-24, GPL-3.0, 2.777 yıldız — https://github.com/zk-org/zk

**L. Obsidian ekosistemi**

50. obsidian-dataview'in son sürümü 0.5.70 / 2025-04-07'dir ve depo 2025-11-17'den beri push almamıştır — https://github.com/blacksmithgu/obsidian-dataview/releases
51. Obsidian eklentileri `metadataCache.resolvedLinks` yapısına çalışma-zamanında sentetik kenar enjekte ederek graf görünümünü dosyalara dokunmadan değiştirebilir; ancak bu **resmî public API değildir** — https://www.obsidianstats.com/tags/graph-view [ikincil aggregator; birincil Obsidian API dokümanıyla doğrulanmadı]
52. Obsidian Juggl (Cytoscape.js tabanlı gelişmiş graf görünümü) 2025-02-27'den beri push almamıştır, GPL-3.0 — https://github.com/HEmile/juggl

**M. Diğer türev üreteçleri**

53. SilverBullet MIT lisanslıdır, 2.10.0 sürümü 2026-07-28'de çıktı ve depo bugün (2026-08-29) push almıştır — https://github.com/silverbulletmd/silverbullet
54. Emanote AGPL-3.0'dır, son sürümü 1.4.0.0 / 2025-08-19'dur; selefi Neuron'un depo açıklaması birebir *"superseded by Emanote"* der — https://github.com/srid/emanote/releases · https://github.com/srid/neuron
55. MarkdownDB bir md klasörünü SQLite'a indeksler (frontmatter, tag, link, backlink) ve JS sorgu API'si verir; MIT, son push 2026-05-21 — https://github.com/flowershow/markdowndb
56. Flowershow AGPL-3.0'dır ve 2026-08-21'de push almıştır — https://github.com/datopian/flowershow
57. SSG sınıfının tamamı (Docusaurus, Starlight, VitePress, MkDocs, Sphinx, Quarto) 2026-08 içinde commit almış canlı projelerdir, ancak hiçbirinde hazır bir bilgi-grafı bileşeni yoktur — https://github.com/facebook/docusaurus · https://github.com/withastro/starlight · https://github.com/vuejs/vitepress · https://github.com/mkdocs/mkdocs · https://github.com/sphinx-doc/sphinx · https://github.com/quarto-dev/quarto-cli

**N. Sourcetrail hattı — profilin en yakın tarihsel emsali**

58. SourcetrailDB README'si birebir *"You can use the SourcetrailDB project to write an indexer for an arbitrary programming language (or other kind of data, e.g. see poetry indexer example)"* der — yani araç, kod olmayan keyfi veriyi de kabul eder — https://github.com/CoatiSoftware/SourcetrailDB
59. SourcetrailDB **arşivlenmiştir**, son push 2021-11-22, Apache-2.0 — https://github.com/CoatiSoftware/SourcetrailDB
60. Orijinal `CoatiSoftware/Sourcetrail` deposu arşivlidir (son push 2021-12-13) ve README'si projenin 2021 sonunda orijinal bakımcılarca arşivlendiğini yazar — https://github.com/CoatiSoftware/Sourcetrail
61. `petermost/Sourcetrail` **canlı bir forktur**: 2026.6 sürümü 2026-06-11'de çıktı, GPL-3.0, 751 yıldız; README'de 2026-08-01 tarihli bakım notu *"development will slow down somewhat"* der ve SourcetrailDB SDK'sına atıf yapar — https://github.com/petermost/Sourcetrail
62. Sourcetrail'in VS Code köprüsü `CoatiSoftware/vsce-sourcetrail` **arşivlidir** (son push 2020-02-24) ve marketplace sürümü 0.0.2 / **2017-06-27**'dir — https://github.com/CoatiSoftware/vsce-sourcetrail · https://marketplace.visualstudio.com/items?itemName=astallinger.sourcetrail

**O. Kod-zekâsı manzarası**

63. `sourcegraph/sourcegraph` deposu bugün GitHub API'de **404** döndürür; `sourcegraph/sourcegraph-public-snapshot` arşivlidir (son push 2024-09-02) ve README'si *"Sourcegraph transitioned to a private monorepo"* der — https://github.com/sourcegraph/sourcegraph-public-snapshot
64. Aynı snapshot'ın LICENSE dosyası *"LICENSE.enterprise (Enterprise License) applies to all files in this repository"* ile başlar — yani Sourcegraph artık açık kaynak değildir — https://github.com/sourcegraph/sourcegraph-public-snapshot/blob/main/LICENSE
65. SCIP bağımsız `scip-code` organizasyonuna taşınmıştır (org kuruluşu 2026-01-09), Apache-2.0'dır ve son push 2026-08-28'dir — https://github.com/scip-code/scip
66. Kythe (Apache-2.0) v0.0.76 sürümünü 2026-07-16'da yayımladı; Glean (BSD) bugün push aldı — ikisi de kendi olgu/indeks verinizi yazmanıza izin verir — https://github.com/kythe/kythe/releases · https://github.com/facebookincubator/glean
67. GitHub'ın `stack-graphs` deposu **arşivlidir**, son push 2025-09-09 — https://github.com/github/stack-graphs
68. universal-ctags v6.2.1'i 2025-10-25'te yayımladı ve 2026-08-26'da push aldı; tree-sitter bugün push aldı — https://github.com/universal-ctags/ctags/releases · https://github.com/tree-sitter/tree-sitter
69. Aider'ın repo-map'i tree-sitter ile AST üretir, dosyaları düğüm/bağımlılıkları kenar yapan bir graf kurar ve üzerine bir graf sıralama algoritması uygular — https://aider.chat/2023/10/22/repomap.html
70. Sourcetrail'in yerini almaya en yakın canlı kendi-barındırmalı seçenekler OpenGrok (CDDL-1.0), CodeCompass (GPL-3.0) ve Sourcebot'tur; Sourcebot'un lisansı **FSL-1.1**'dir, yani OSI onaylı açık kaynak değildir — https://github.com/OpenGrok/OpenGrok · https://github.com/Ericsson/CodeCompass · https://github.com/sourcebot-dev/sourcebot

**P. CodeSee**

71. GitKraken'in resmî basın bülteni *"Scottsdale, AZ — May 14, 2024 — GitKraken … today announced it has acquired code health innovator, CodeSee."* der ve **ürünün sonlandırılacağına dair hiçbir ifade içermez** — https://www.gitkraken.com/press/gitkraken-acquires-codesee-launches-devex-platform
72. `https://www.codesee.io` bugün (kendi çekimim, 2026-08-29) **HTTP 404** döndürür — https://www.codesee.io
73. `https://app.codesee.io` bugün 302 ile Cloudflare Access giriş sayfasına yönlenir, yani herkese açık değildir — https://app.codesee.io
74. CodeSee için resmî bir "sonlandırma tarihi" duyurusu **bulunamadı** — https://www.gitkraken.com/press

**R. Graf render / dış veri yüzeyleri**

75. Datasette bir SQLite dosyasını salt-okunur web arayüzü + JSON API olarak sunar; Apache-2.0, kararlı sürüm 0.65.3 / 2026-08-06 — https://docs.datasette.io/en/stable/getting_started.html · https://github.com/simonw/datasette/releases
76. Datasette'in resmî eklenti dizininde düğüm-kenar graf görselleştirme eklentisi **yoktur** (görselleştirme eklentileri grafik/harita odaklıdır) — https://datasette.io/plugins
77. `datasette-json-html` README'si birebir *"The `href` property must begin with `https://` or `http://` or `/`, to avoid potential XSS injection attacks"* der, yani hazır eklentiyle `vscode://` linki basılamaz — https://github.com/simonw/datasette-json-html
78. Cytoscape.js (v3.34.2 / 2026-08-25, MIT), vis-network (v10.1.2 / 2026-08-19, Apache-2.0) ve sigma.js (2026-08-20, MIT) tamamen dış JSON düğüm/kenar verisiyle çalışır ve tıklama işleyicisi tamamen serbesttir — https://github.com/cytoscape/cytoscape.js/releases · https://github.com/visjs/vis-network/releases · https://github.com/jacomyal/sigma.js
79. Kùzu deposu **arşivlidir**, son sürüm v0.11.3 / 2025-10-10; canlı fork `Kineviz/bighorn`tur — https://github.com/kuzudb/kuzu · https://github.com/Kineviz/bighorn
80. Cosmograph'ın npm paketi `@cosmograph/cosmograph` 2.5.1 sürümünde **CC-BY-NC-4.0** lisanslıdır, yani ticari kullanıma kapalıdır — https://www.npmjs.com/package/@cosmograph/cosmograph
81. Gephi v0.11.2 sürümünü 2026-05-09'da yayımladı, GPL-3.0 — https://github.com/gephi/gephi/releases
82. Neo4j Bloom dosya okumaz, çalışan bir Neo4j örneği gerektirir (*"Neo4j Bloom is powered by the Neo4j graph database"*) — https://neo4j.com/docs/bloom-user-guide/current/
83. Sourcetrail dışında, "dış SQLite → graf UI → tıkla → VS Code'da o satır" üçlüsünü tek pakette veren **canlı bir araç bulunamadı**; bu üç bağımsız araştırma hattının yakınsadığı olumsuz bulgudur — (negatif bulgu; §5'teki arama kapsamıyla sınırlı)

**S. Hat B eki — Cosma, Quartz ve MkDocs/Docusaurus kaynak-kodu bulguları**

84. Cosma'nın `select_origin` yapılandırma anahtarı `directory | csv | online` değerlerini alır; `csv` modunda `nodes_origin`/`links_origin`, `online` modunda `nodes_online`/`links_online` (URL) kullanılır ve CSV uzantısı `/\.csv$/` ile zorunlu tutulur (`core/models/config.js`, satır 40-45 ve 160-162) — https://github.com/graphlab-fr/cosma/blob/develop/core/models/config.js
85. `controllers/modelize.js`'in `csv` dalı yalnızca `processNodes(nodes_origin)` ve `processLinks(links_origin)` çağırır; markdown taraması yalnız `directory` dalındadır, yani **CSV modunda Cosma'nın kendi parser'ı hiç çalışmaz** (satır 165-172, ve satır 77) — https://github.com/graphlab-fr/cosma/blob/develop/controllers/modelize.js
86. Üretilen `cosmoscope.html` CSS'i, JS bundle'ını ve görselleri (base64) gömer; şablonda hiçbir CDN çağrısı yoktur, yani çıktı tam çevrimdışı çalışır (`static/template/cosmoscope.njk`, satır 15-30 ve 600-616) — https://github.com/graphlab-fr/cosma/blob/develop/static/template/cosmoscope.njk
87. Graf verisi HTML'e `const data = {{ graph.data | dump | safe }}` olarak gömülür ve `graph.data` graphology `graph.export()` çıktısıdır — derleme sonrası bu değişkeni yamalamak beşinci bir enjeksiyon noktasıdır (`core/models/template.js`, satır 308-310) — https://github.com/graphlab-fr/cosma/blob/develop/core/models/template.js
88. `core/utils/getGraph.js:110`'daki `if (!graph.hasNode(link.target))` koşulu gereği hedefi `nodes.csv`'de bulunmayan kenarlar `brokenEdges`'e düşer ve çizilmez — https://github.com/graphlab-fr/cosma/blob/develop/core/utils/getGraph.js
89. Cosma'nın `modelize` komutunun tam seçenek listesi `--citeproc`, `--custom-css`, `--sample`, `--fake`, `-p/--project`'tır; `--citations` diye bir seçenek **yoktur** (`app.js`, satır 85-95) — https://github.com/graphlab-fr/cosma/blob/develop/app.js
90. Cosma el kitabı `references_as_nodes: true` için birebir *"bibliographic references become nodes in the graph: each cited reference is treated as a node and each citation is treated as a link"* der — ikinci bir deterministik kenar kaynağı — https://github.com/graphlab-fr/cosma/blob/develop/docs/user-manual.md
91. Quartz'ın graf bileşeni `d3` ve `pixi.js`'i çalışma anında `https://cdn.jsdelivr.net/npm/d3@7/...` ve `https://cdn.jsdelivr.net/npm/pixi.js@8/...` adreslerinden yükler (`graph.inline.ts`, satır 35-36) — yani **graf görünümü internet gerektirir** — https://github.com/quartz-community/graph/blob/main/src/components/scripts/graph.inline.ts
92. Quartz'ın graf zinciri şudur: crawl-links transformer `file.data.links` yazar → ContentIndex emitter `links: data.links ?? []` ile `static/contentIndex.json` üretir → `renderPage.tsx` bu dosyayı `fetch` eder → graf bileşeni kenarları `details.links`'ten kurar — https://github.com/quartz-community/crawl-links/blob/main/src/transformer.ts · https://github.com/quartz-community/content-index/blob/main/src/emitter.ts · https://github.com/jackyzha0/quartz/blob/main/quartz/components/renderPage.tsx
93. Quartz grafında hedef slug `contentIndex`'te anahtar olarak yoksa kenar çizilmez (`validLinks.has(dest)` kapısı, `graph.inline.ts`, satır 132-139) — hayalet düğüm oluşmaz — https://github.com/quartz-community/graph/blob/main/src/components/scripts/graph.inline.ts
94. Quartz'ta kaynak `.md` dosyalarına dokunmadan kenar eklemenin en temiz yolu `file.data.frontmatterLinks` dizisine **append** etmektir; bu desen resmî `note-properties` eklentisinde birebir kullanılır — https://github.com/quartz-community/note-properties/blob/main/src/transformer.ts
95. Quartz'ın `v5.0.0` etiketi 2026-03-14'te (`feat(v5): add plugin system (#2295)`) atılmıştır ve v5 çekirdeği boşaltılıp eklentiler `github.com/quartz-community/*` altında ~60 ayrı MIT depoya taşınmıştır — https://github.com/jackyzha0/quartz/tags · https://github.com/orgs/quartz-community/repositories
96. `mkdocs-obsidian-interactive-graph` eklentisi grafı `site_dir/assets/javascripts/graph.json` yoluna ECharts biçiminde yazar (`obsidian_interactive_graph/plugin.py`, satır 100) — dosyanın üzerine yazmak dış enjeksiyon için yeterlidir — https://github.com/daxcore/mkdocs-obsidian-interactive-graph-plugin/blob/main/obsidian_interactive_graph/plugin.py
97. `mkdocs-network-graph` eklentisi grafı `site_dir/graph/graph.json` yoluna D3 biçiminde `on_post_build` sırasında yazar; MIT, 1.0.3 / 2025-09-11 — https://github.com/develmusa/mkdocs-network-graph-plugin
98. `mkdocs-graphviz` DOT kaynağını derleme anında inline SVG'ye çevirir (JS'siz, tam deterministik) ama lisansı **GPL-3.0-or-later**'dır (PyPI `license_expression` alanı, sürüm 2.0.2, yükleme 2026-08-14) — https://pypi.org/pypi/mkdocs-graphviz/json
99. Docusaurus'un eklenti API'si `loadContent()` ile *"fetch from data sources (filesystem, remote API…)"* ve `setGlobalData()` ile istemciye veri geçirmeye izin verir, ancak hazır bir graf bileşeni yoktur; `@docusaurus/core` 3.10.2 / 2026-07-10, MIT — https://docusaurus.io/docs/api/plugin-methods/lifecycle-apis · https://www.npmjs.com/package/@docusaurus/core
100. `docusaurus-graph` eklentisi grafı yalnız frontmatter'daki `sources:`/`references:` alanlarından kurar, yani düz bir `.md` deposunda graf boş çıkar; 2.0.0 / 2024-11-22, MIT — https://github.com/Arsero/docusaurus-graph
101. MkDocs'un belgelenmiş eklenti kancaları `on_files` (*"Use this event to add, remove, or alter files in the collection"*), `on_env` ve `on_post_build` (*"Use this event to call post-build scripts"*)'tir; ayrıca `hooks:` yapılandırma anahtarı yerel Python betiklerini paketlemeden eklenti örneği olarak yükler — https://www.mkdocs.org/dev-guide/plugins/ · https://www.mkdocs.org/user-guide/configuration/#hooks
102. `@graphlab-fr/cosma`'nın npm kaydındaki `license` alanı `GPL-3.0-or-later`, depo `LICENSE.txt` dosyası ise `GPL-3.0 OR CeCILL-2.1` der — iki kaynak arasında küçük bir tutarsızlık vardır — https://www.npmjs.com/package/@graphlab-fr/cosma · https://github.com/graphlab-fr/cosma/blob/develop/LICENSE.txt


---

## 5. Bayraklar, bulunamayanlar, doğrulanmayanlar

**403 / erişilemeyen:**
- `https://iwe.md/docs/editors/vscode/` → **HTTP 403** (hat A). IWE hakkındaki her şey GitHub README'lerine dayanıyor.
- `https://sourcegraph.com/blog/*` → **HTTP 403** (hat C). SCIP yönetişimi ve Amp ayrılması duyuruları yalnız ikincil kaynakla desteklendi.
- `web.archive.org` → araç kısıtı nedeniyle okunamadı; CodeSee'nin 2024-2025 arşiv görüntüleri incelenemedi.

**Bulunamadı (meşru sonuç):**
- Profilin ①–⑤'ini tek pakette veren canlı araç.
- Foam için belgelenmiş public extension/plugin API sayfası.
- Dendron şirketinin resmî kapanış/tasfiye kaydı (yalnız "bakım modu + pivot" doğrulandı).
- CodeSee için resmî ürün sonlandırma duyurusu ve tarihi.
- Marksman ve IWE'de `#^blockid` desteğine dair doğrulanmış doküman.
- Datasette için düğüm-kenar graf eklentisi.
- Kythe için tarayıcı UI dokümanı.

**Doğrulanmadı / kestirim [?]:**
- Cosma'nın `content` kolonuna gömülen `vscode://file/...:123` bağlantısının üretilen cosmoscope HTML'ine sağ salim çıkıp çıkmadığı — **test edilmedi**, profil için kritik.
- VS Code 1.121'in yerleşik Mermaid eklentisinin kaynağının `mjbvz/vscode-markdown-mermaid@9f4d37d` ile birebir aynı olduğu (merge sonrası çekirdek sürümü ayrıca okunmadı) [?] — ancak PR #346'nın merge edilmemesi ve issue #332'nin açık kalması bu çıkarımı ayrıca destekliyor.
- CodeGraphy'nin marketplace'te canlı (2026-08-05) ama GitHub deposunun durgun (2023-06-10) olmasının sebebi — depo taşınmış olabilir [?].
- Logseq 2.0'da SQLite'ın kanonik kaynak olduğu iddiası — birincil Logseq kaynağıyla doğrulanamadı, ikincil kaynak var.
- Obsidian'ın `resolvedLinks` enjeksiyon deseni — yalnız üçüncü-parti aggregator kaynağı; birincil Obsidian API dokümanıyla doğrulanmadı.
- Tarayıcıların `vscode://` şeması için gösterdiği onay diyaloğu davranışı (OS/tarayıcı bağımlı).
- Sourcetrail `.srctrldb` dosyasının SQLite olduğu (yaygın bilgi, bu turda doğrulanmadı).
- `zk`'nın `content`/graf çıktısının satır numarası taşıyıp taşımadığı.
- Hiçbir aday **kurulup koşturulmadı**; Cosma ve Quartz enjeksiyon iddiaları yalnız kaynak-kodu okumasına dayanır. Fiili doğrulama için tek `cosma modelize` ve tek `npx quartz build` koşumu yeterlidir — **önerilir**.
- Cosma'nın SVG/d3 render'ının büyük graflarda Quartz'ın PixiJS/WebGL'inden yavaş olacağı — bu bir **çıkarımdır, ölçüm değildir**.
- MkDocs'ta `pymdownx.snippets` (`--8<-- "dosya.md:4:6"`) + `anchor_linenums: true` ile üretilen `#__codelineno-<blok>-<satır>` çapalarının gerçek satır-gezinmesi verdiği — hat B'nin çıkarımı, Material bunu belgelemiyor, **sözleşmesiz**.

**Kapsam sınırı:**
- **Hat B kısmi raporladı:** Cosma, Quartz ve MkDocs/Docusaurus ekosistemini kaynak-kodu düzeyinde kapattı, ancak kendi alt-hatları (Obsidian ekosistemi: dataview, webpage-export, digital-garden, obsidian-export, Bases, `resolvedLinks`; ve Emanote/Neuron/SilverBullet/TiddlyWiki/org-roam-ui/Logseq/zk/Foam/Dendron turu) rapor anında **hâlâ koşuyordu**. Bu iki alt-hat bu belgeye girmedi; Cosma/Quartz/Logseq/zk/Emanote/SilverBullet/MarkdownDB satırları benim kendi birincil kaynak okumamla doldurulmuştur. **TiddlyWiki ve org-roam-ui hiç taranmadı.**
- Ticari/SaaS araçlar (InfraNodus, Understand, Neo4j Bloom) yalnız yüzeysel not edildi; profilin ⑤ maddesi (yerel/açık kaynak tercihi) gereği önceliklendirilmedi.

---

## 6. Örneklem-denetimi kaydı (V26/R3)

Kural: her yardımcı hat için çıktının **son üçte birinden ≥1 kaynak iddiası** + **tüm sayısal iddialar** bağımsız doğrulanır.

| Hat | Denetlenen | Sonuç |
|---|---|---|
| A | Marketplace sürüm/tarih/kurulum sayıları (foam, dendron, memo, markdown-links, markdown-notes, marksman, iwe, tendr) | **8/8 birebir tuttu** (Gallery API kendi çekimim) |
| A | Son üçte bir: Mermaid PR #346 merge edilmeden kapandı + issue #332 açık | **Tuttu** (GitHub API: PR merged=false, closed 2026-06-25; issue 332 state=open) |
| A | Foam `exports.foam` / `registerProvider` / `set` iddiası | **Bağımsız olarak kaynak koddan doğrulandı** (kendi klonum, commit `3452c98`) |
| C | scip-code org kuruluş tarihi (2026-01-09), vis-network v10.1.2/2026-08-19, gephi v0.11.2/2026-05-09, cytoscape v3.34.2/2026-08-25, Cosmograph CC-BY-NC-4.0, Datasette 0.65.3/2026-08-06 | **6/6 birebir tuttu** |
| C | Son üçte bir: CodeSee — `www.codesee.io` 404, `app.codesee.io` Cloudflare Access, GitKraken 2024-05-14 satın alma | **Tuttu** (kendi curl çekimim + basın bülteni birinci elden) |
| B | Sayısal: mkdocs-graphviz 2.0.2 / 2026-08-14 / `license_expression: GPL-3.0-or-later` (PyPI), `@docusaurus/core` 3.10.2 / 2026-07-10 / MIT (npm), `@graphlab-fr/cosma` 2.6.1 / 2026-03-17 (npm), Quartz `v5.0.0` etiketinin varlığı, 6 MkDocs/Docusaurus eklenti deposunun lisans+tarihi (GitHub API) | **Hepsi birebir tuttu** |
| B | Son üçte bir + kritik mimari: Quartz grafının jsDelivr CDN bağımlılığı (`graph.inline.ts:35-36`) ve `graph.json` çıktı yolu (`plugin.py:100`) | **İkisi de kaynak koddan bağımsız doğrulandı** |
| B | Cosma CSV modunun markdown parser'ı baypas ettiği | **Bağımsız olarak kendi klonumdan doğrulandı** (`docs/user-manual.md` satır 132-137 + 542-580) |

**Tespit edilen sapmalar (ikisi de küçük, düzeltildi):**
1. Hat A, `iwe-org/vscode-iwe` lisansını Apache-2.0 saydı; GitHub API **MIT** döndürüyor (çekirdek `iwe-org/iwe` Apache-2.0). Tabloya düzeltme işlendi.
2. Cosma'nın lisansı iki kaynakta farklı görünüyor: npm `license` alanı `GPL-3.0-or-later`, depo `LICENSE.txt` ise `GPL-3.0 OR CeCILL-2.1`. İkili lisans olarak raporlandı, tutarsızlık İ-102'de kayıt altına alındı.

**Yakınsama notu:** Cosma ve Quartz'ın enjeksiyon mekanizmaları **iki bağımsız hat tarafından (hat B ve benim kendi kaynak-kodu okumam) ayrı ayrı** bulundu ve aynı dosya/satırlara işaret etti — bu iki iddia raporun en yüksek güvenli kısmıdır. Mermaid'in tıklanamazlığı **üç** bağımsız yoldan (hat A'nın PR/issue izi, benim `securityLevel` grep'im, resmî Mermaid dokümanı) doğrulandı.

---

## 7. Öneri sıralaması (hüküm değil)

1. **Kendi türevini üret + VS Code çekirdeğinin `#L123` / `vscode://…:satır:sütun` desteğine yaslan; graf yüzeyi için D2 ya da Graphviz.** ①–⑤'in tamamı karşılanır, hiçbir belgesiz iç API'ye bağlanılmaz, ② tanım gereği sağlanır. Bedeli: hazır ürün yok, türev üreticisi yazılır.
2. **Cosma CSV modu.** Dış kenar listesini **belgelenmiş, birinci sınıf bir giriş modu** olarak kabul eden tek araç — diğer tüm adaylarda enjeksiyon "belgelenmemiş dosyayı ez" demektir. Çıktı tek dosyalık, **CDN'siz, tam çevrimdışı** HTML. Bedeli: ④ (VS Code) karşılanmaz; md dizini modu ile birlikte koşmaz (gövdeyi de `content` kolonuna taşırsın); `vscode://` linkinin HTML'e sağ salim çıktığı **doğrulanmadı**; topluluk küçük (190 yıldız).
3. **Foam üstüne bindirme.** Graf UI + backlink + blok çıpası + VS Code yerliliği hazır gelir. Bedeli: `exports.foam` belgesiz iç API; Foam aktif geliştirildiği için kırılma riski sürekli. Daha güvenli varyantı: enjeksiyon yerine **türev md üretip** Foam'ın kendi parser'ına okutmak.
4. **Quartz v5 + `frontmatterLinks` append eden özel transformer.** Zengin gezinme, arama ve explorer hazır gelir; kaynak `.md` dosyalarına dokunulmaz. Bedeli: çıktı statik site (VS Code değil) ve **graf görünümü jsDelivr CDN'i ister** — profilin ⑤ maddesiyle çelişir.
4b. **MkDocs graf eklentisi + `graph.json` üzerine yazma.** En düşük eforlu enjeksiyon (`site_dir/assets/javascripts/graph.json` ya da `site_dir/graph/graph.json`); MkDocs'un `hooks:` anahtarı sayesinde eklenti paketlemeye bile gerek yok. Bedeli: sözleşme belgelenmemiş, sürüm kırılmasına açık.
5. **Kullanma:** Dendron (ölü), Markdown Memo / Marksman / Markdown Oxide / IWE / kortina (graf yok), Mermaid (tıklanamaz), Sourcegraph (kapalı kaynak), CodeSee (erişilemez), Kùzu (arşiv), Cosmograph (ticari kullanım yasak), Sourcebot (FSL, OSI-açık değil).

---

**Rapor sonu — tez-A.** Antitez aşaması §4'teki 102 iddiayı hedef alsın; §5'teki "doğrulanmadı" listesi ve §6'daki iki sapma özellikle saldırıya açık noktalardır. En zayıf halkalar: (a) hiçbir aday fiilen kurulup koşturulmadı, (b) Cosma'nın `vscode://` linkini HTML'e taşıyıp taşımadığı test edilmedi, (c) hat B'nin Obsidian ve "diğer SSG" alt-hatları hiç raporlamadı.
