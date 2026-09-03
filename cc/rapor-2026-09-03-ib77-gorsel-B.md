# İB-77 Atlas — Aile B: Araç + LLM→Görsel Emsalleri (TEZ)

## 0. KÜNYE
- Ajan: Atlas TEZ, Aile B (m.40b v0.2)
- AS-OF: 2026-09-03 (tüm URL çekimleri bu tarihte)
- Kapsam: deklaratif görsel diller · LLM→görsel benchmark'ları · doğrulama kapıları · Claude Code ortam kısıtları
- Gerçekten açılan (WebFetch) kaynaklar: mermaid.js.org/config/usage.html, vega.github.io/vega-lite, arxiv.org/abs/2303.02927 (LIDA), d2lang.com/tour/install — 4 kaynak, ≥2 şartı karşılanmış (D)
- Yalnız arama-özeti (WebSearch snippet, doğrudan açılmamış) ile alınan bulgular ayrı işaretli (K)

## 1. BULGULAR

**B1 (D).** Mermaid güncel sürümü v11.17.2; tek-HTML gömme `<script type="module"> import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs'` + `<pre class="mermaid">…</pre>` kalıbıyla yapılır, sayfa yüklenince otomatik SVG'ye render eder. Kaynak: https://mermaid.js.org/config/usage.html (2026-09-03 çekim).

**B2 (D).** Mermaid'in desteklediği diyagram sınıfları geniş: flowchart, sequence, class, state, ER, gantt, mindmap, timeline, pie, quadrant, C4, sankey, XY, kanban, architecture, radar, treemap ve daha fazlası — aile B'nin "flow/sequence/class/ER/mindmap/timeline/gantt" listesinin tamamı ve fazlası mevcut. Aynı kaynak.

**B3 (D).** Mermaid CLI (mmdc) Node ≥16 gerektirir, komut satırından SVG/PNG üretir — ama sayfada tam komut sözdizimi verilmemiş [?]. Aynı kaynak.

**B4 (D).** Vega-Lite güncel sürümü 6.4.3; JSON-tabanlı deklaratif "grammar" olarak tanımlanıyor — "specifications describe visualizations as encoding mappings from data to properties of graphical marks." Resmi JSON şema adresi: https://vega.github.io/schema/vega-lite/v6.json (şema-doğrulama kapısı için doğrudan kullanılabilir). Kaynak: https://vega.github.io/vega-lite/ (2026-09-03).

**B5 (K, sayfada yok).** Vega-Lite'ın CLI araçları (vl2svg/vl2png, @vega/cli paketi) ekosistem sayfasında listeleniyor ama bu çekimde içerik görülmedi — doğrulanmadı, ayrı fetch gerekir.

**B6 (D).** LIDA (Microsoft), ACL 2023 Demonstration'da kabul edilmiş, ilk gönderim 2023-03-06, son revizyon 2023-06-06. Mimari 4 modülden oluşuyor: Summarizer (veri→NL özet), Goal Explorer (görselleştirme hedefi üretimi), VisGenerator (kod üretimi/iyileştirme/filtreleme), Infographer (görüntü üretim modelleriyle stilize infografik). Sayfada hedef kütüphane adı (matplotlib/vega-lite) ve sayısal değerlendirme metriği AÇIKÇA YOK — bu iddia bu çekimde doğrulanamadı [?]. Kaynak: https://arxiv.org/abs/2303.02927.

**B7 (K).** VisEval (Microsoft), arXiv 2407.00981, ilk gönderim 2024-07-01, revize 2024-08-07, IEEE TVCG'de yayımlı. 2.524 sorgu, 146 veritabanı kapsıyor; NL2VIS (doğal dilden görselleştirme) için "validity, legality, readability" (geçerlilik, uygunluk, okunabilirlik) üç eksenli otomatik değerlendirme çerçevesi sunuyor, heterojen "checker"larla taranıyor. GitHub: microsoft/VisEval. Bu bulgu WebSearch özetinden alındı, sayfa doğrudan açılmadı — sayısal başarı oranları bu turda ELDE EDİLEMEDİ [?].

**B8 (K).** ChartMimic, arXiv 2406.09961, ICLR 2025 kabul, chart-görüntüden-koda (chart-to-code) üretimi ölçüyor. 4.800 insan-küratörlü (görsel, talimat, kod) üçlüsü, 18 temel + 4 gelişmiş tip, 201 alt kategori. Dört düşük-seviye metrik: metin, yerleşim (layout), tip, renk — bir "code tracer" hem referans hem üretilen kodu çalıştırıp bu dört boyutu karşılaştırıyor; yüksek seviye benzerlik GPT-4o hakemliğiyle puanlanıyor. Ölçülen hata sınıfları: halüsinasyon (var olmayan metin ekleme) ve tip karışıklığı (benzer grafik tiplerini birbirine karıştırma). GPT-4o skoru %82.2 olarak bildiriliyor. Kaynak WebSearch özeti, doğrudan sayfa açılmadı [?].

**B9 (D, kısmi).** D2 dili resmi kurulum sayfası açıldı ancak CLI komut detayları, determinizm beyanı ve HTML gömme yöntemi bu sayfada YOKTU — sayfa GitHub INSTALL.md ve play.d2lang.com'a yönlendiriyor. Bu üç alt-iddia bu çekimde DOĞRULANAMADI [?]. Kaynak: https://d2lang.com/tour/install (2026-09-03).

**B10 (bilgi tabanı, K/genel bilgi — doğrudan kaynak açılmadı).** Graphviz DOT ve PlantUML klasik metin→görsel araçları olarak literatürde yaygın kabul görür (dot CLI ile SVG/PNG); bu turda ayrı kaynak açılıp doğrulanmadı — sonraki tur borcu.

## 2. ARAÇ KARŞILAŞTIRMA TABLOSU

| Araç | İçerik sınıfı uyumu | Gömme yolu | CLI | Belirlenimcilik | Bağımlılık maliyeti | Kaynak |
|---|---|---|---|---|---|---|
| Mermaid | flow/sequence/class/ER/mindmap/timeline/gantt/kanban/vb. | CDN ESM script + `<pre class="mermaid">` | mmdc (Node≥16) | Aynı girdi→aynı SVG yapısı (deklaratif); layout motoru sürüm-bağımlı [?] | Düşük (tek CDN script) | B1-B3 (D) |
| Vega-Lite | istatistiksel/veri grafikleri (bar/line/scatter/…) | CDN + vega-embed | @vega/cli (varlığı doğrulanmadı, B5 K) | JSON şema deterministik render (spec sabitse çıktı sabit) [?] | Orta (vega+vega-lite+vega-embed 3 script) | B4 (D) |
| D2 | mimari/kutu-ok diyagramları | SVG dosyası gömme (yöntem bu turda doğrulanmadı) | `d2` CLI (kurulu, ortamda mevcut — emirde belirtilmiş) | Bilinmiyor bu turda [?] | Bilinmiyor [?] | B9 (D, eksik) |
| Graphviz DOT | graf/ağaç yapıları | dot→SVG, sonra gömme | `dot` CLI (kurulu) | Genel bilgi: deterministik layout algoritmaları (dot/neato) — doğrudan kaynakla doğrulanmadı [?] | Düşük | doğrulanmadı |
| PlantUML | UML diyagramları | Java gerektirir tipik olarak — bu turda doğrulanmadı | plantuml.jar | [?] | Orta-yüksek (JVM) [?] | doğrulanmadı |
| Excalidraw JSON | el-çizimi görünümlü şema | Excalidraw render kütüphanesi gerektirir | sınırlı | [?] | Orta-yüksek | doğrulanmadı |
| Markmap | mindmap (Markdown tabanlı) | CDN script | markmap-cli | [?] | Düşük | doğrulanmadı |

## 3. LLM→GÖRSEL BENCHMARK BULGULARI
- **VisEval** (B7, K): NL2VIS için 3 eksen — geçerlilik/uygunluk/okunabilirlik; 2.524 sorgu × 146 DB; sayısal model başarı oranları bu turda elde edilemedi, GitHub'da mevcut olabilir [?].
- **ChartMimic** (B8, K): chart-to-code, 4 düşük-seviye metrik (metin/yerleşim/tip/renk) + GPT-4o hakemi; ölçülen hata sınıfları = halüsinasyon (yok-olan metin ekleme) ve tip-karışıklığı; GPT-4o %82.2, açık modeller belirgin geride (sayı verilmedi).
- **LIDA** (B6, D): mimari doğrulandı, sayısal benchmark/hata-oranı bu makalenin özetinde YOK; ayrı bir LIDA-değerlendirme makalesi olabilir, bu turda aranmadı.
- **nvBench, ChartGPT/VizGPT, Text2Vis, Data Formulator**: bu turda hiç açılmadı/aranmadı — AÇIK SORU.

## 4. DOĞRULAMA KAPISI ADAYLARI
- **Şema doğrulama (LLM'siz, deterministik):** Vega-Lite JSON şeması (v6.json) karşı `ajv` gibi bir validator ile — kodsuz/kural-tabanlı. ✅ LLM'siz.
- **Render testi (headless, LLM'siz):** `mmdc`/`d2`/`dot` CLI çıktısının hatasız dönmesi (exit code 0) — ✅ LLM'siz, deterministik.
- **Lint (kısmen LLM'siz):** chart-junk/renk-körlüğü-paleti kontrolleri kural-tabanlı yazılabilir (ör. sabit renk-körü-güvenli palet listesiyle karşılaştırma) — ✅ LLM'siz mümkün, ama bu turda hazır bir araç adı doğrulanmadı [?].
- **"Görsel iddia ↔ kaynak veri" tutarlılığı:** ChartMimic'in "code tracer" yaklaşımı (referans kodu çalıştırıp değerleri karşılaştırma) bu sınıfa örnek — kısmen LLM'siz (tracer deterministik, üst-skor GPT-4o gerektiriyor).

## 5. İDDİA LİSTESİ (numaralı, gerekçesiz — antiteze)
1. Mermaid v11.17.2, CDN-ESM ile tek dosyaya gömülebilir, geniş diyagram yelpazesi sunar (D).
2. Vega-Lite 6.4.3, JSON şema tabanlı, resmi şema URL'i mevcuttur (D).
3. LIDA 4 modüllü mimariye sahiptir, ACL 2023'te sunulmuştur (D).
4. LIDA'nın hedef kütüphaneleri ve sayısal metrikleri bu kaynakta doğrulanmamıştır (K/eksik).
5. VisEval 2.524 sorgu / 146 DB, 3 eksenli (geçerlilik/uygunluk/okunabilirlik) otomatik değerlendirme sunar (K, tek-kaynak arama-özeti).
6. ChartMimic 4.800 örnek, 4 düşük-seviye metrik + GPT-4o hakemliği kullanır; GPT-4o %82.2 skorla lider (K, tek-kaynak arama-özeti).
7. ChartMimic'te ölçülen ana hata sınıfları halüsinasyon ve tip-karışıklığıdır (K).
8. D2'nin CLI/determinizm/gömme detayları bu turda doğrulanamamıştır (eksik — [?]).
9. Vega-Lite CLI (vl2svg/vl2png) varlığı bu turda doğrulanamamıştır (eksik — [?]).
10. Graphviz/PlantUML/Excalidraw/Markmap bu turda hiç doğrudan kaynakla açılmamıştır (eksik).
11. nvBench, ChartGPT/VizGPT, Text2Vis, Data Formulator bu turda araştırılmamıştır (kapsam dışı kaldı).

## 6. AÇIK SORULAR / bulunamayanlar
- VisEval ve ChartMimic'in ham GitHub/arXiv PDF'i açılıp tam sayısal tabloları çekilmedi (bütçe kısıtı, 20 araç çağrısı tavanı).
- D2 CLI komut sözdizimi, determinizm garantisi, SVG gömme pratiği doğrulanmadı — d2lang.com/tour/install sayfası bu detayları içermiyordu, GitHub INSTALL.md'ye gidilmedi.
- nvBench, ChartGPT/VizGPT, Text2Vis, Data Formulator, Claude Code'un CDN allowlist'i (mermaid/d2/dot harici JS için) bu turda hiç ele alınmadı.
- LIDA'nın sayısal doğruluk/geçerli-kod-oranı metrikleri ayrı bir makale/rapor gerektiriyor olabilir — bu arXiv özet sayfasında yoktu.
