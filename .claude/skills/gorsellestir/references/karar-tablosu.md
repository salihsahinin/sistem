# Karar tablosu v0 — içerik sınıfı → görsel tür → araç (İB-77 sentez §3, 2026-09-03; kaynak `raporlar/2026-09-03-ib77-gorsellestir-atlas.md`)

Damga: **D** = birincil kaynaklı, adversarial'dan sağlam · **DENEYSEL** = literatürde normatif kaynağı yok (hakem T1 = X), Munzner görev-soyutlamasından türetilmiş; 10 koşumluk kütükle kalibre edilir (m.29). `icerik_sinifi` enum'u `tools/gorsellestir.py` ile birebir aynıdır.

| `icerik_sinifi` | Yüklem (ne zaman) | Birincil tür | Araç önceliği | Alternatif | Damga |
|---|---|---|---|---|---|
| `surec` | adımlar sıralı ∧ dallanma olabilir | akış diyagramı (oklu = işlevsel/nedensel — Tversky) | d2 (elk) → Mermaid `flowchart` | swimlane (d2 container) | DENEYSEL |
| `kavram-iliskisi` | ≥3 kavram ∧ ilişkiler etiketlenebilir | concept map: en genel kavram üstte, oklar etiketli (Novak) | d2 → dot | ağ diyagramı | D (Novak) + DENEYSEL eşleme |
| `karsilastirma` | ≥2 şey × ≥2 özellik, nitel | tablo / matris | HTML tablo | küçük-çoklu | DENEYSEL |
| `hiyerarsi` | ağaç ilişkisi; oksuz = yapısal (Tversky) | ağaç | dot (`rankdir=TB`) → Mermaid `mindmap` | girintili özet | DENEYSEL |
| `zaman-akisi` | olaylar sıralı/tarihli, sayısal değil | timeline | Mermaid `timeline` | Gantt (`gantt`) | DENEYSEL |
| `mekanizma` | "nasıl çalışır": parçalar + bağlantı | etiketli şema | d2 | kesit şeması | DENEYSEL |
| `sayisal-dagilim` | tek sayısal değişken | histogram | Vega-Lite `bar` (binned) | kutu grafiği (`boxplot`) | D (data-to-viz) |
| `sayisal-iliski` | iki sayısal değişken | scatter | Vega-Lite `point` | bağlı saçılım | D (data-to-viz; C–M pozisyon) |
| `zaman-serisi` | sayısal × zaman | çizgi | Vega-Lite `line` | alan | D (FT change-over-time) |
| `sayisal-karsilastirma` | kategori × sayı | çubuk (uzunluk/pozisyon) — eksen 0'dan | Vega-Lite `bar` | lollipop | D (C–M, FT ranking/magnitude) |
| `parca-butun` | paylar toplamı = bütün | treemap ∨ yığılmış çubuk (pasta DEĞİL: açı kodlaması zayıf) | Vega-Lite `rect`/`bar` | — | D (C–M) |
| `akis-miktari` | kaynak → hedef miktar | sankey | Mermaid `sankey-beta` | chord | D (data-to-viz, FT flow) |
| belirsiz / karma | — | bölüm başına ayrı görsel (≤3) ∨ tek soru | — | — | m.4 |

**Araç önceliğinin gerekçesi:** d2/dot çevrimdışı + kurulu + deterministik (09-03 ölçümü: aynı girdi → bayt-bayt aynı SVG) + font gömülü SVG → varsayılan. Mermaid/Vega-Lite CDN ile çevrimiçi render; tarayıcısız doğrulama yok → yalnız d2/dot'un vermediği türlerde ve yapısal kapıyla. **Offline kip (Salih hükmü 09-03, kurulum izinli):** `vl-convert` 1.9.0 (`.venv`) + `mmdc` 11.17.0 (+ puppeteer chrome) kuruldu → `--offline` bayrağıyla Vega-Lite ve Mermaid de yerelde SVG'ye çevrilip gömülür; dış URL sıfır; kapı gerçek render'ı doğrular. Varsayılan kip `cdn` (Salih 4. seçenek kabul), offline istendiğinde sunulur.

**Görsel-kalite kuralları (kapı zorlar):** bar/area eksen sıfırdan (lie-factor) · Okabe–Ito renk-körü-güvenli palet · veri satırı = kaynak satırı · 5 zorunlu blok (başlık · kaynak · görsel · açıklama · künye).

**Kalibrasyon kaydı (append):**
- 2026-09-03 · v0 açıldı · koşum 0 · Salih beyanı —
