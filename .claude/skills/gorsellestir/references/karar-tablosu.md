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

## Öğrenme-format tablosu (kip = öğrenme; Salih 09-03: "format konuya göre değişken, sabitleştirme")
| Konu türü | Birincil format (`arac`) | Yapı | Özet görsel (`ozet_gorsel`, opsiyonel) | Damga |
|---|---|---|---|---|
| kanıt / türetim (tümevarım, eşitsizlik, limit) | `anlatim` | bölüm başına: iddia → adım \| neden tablosu → tuzak | d2 akış (≤7 düğüm) | DENEYSEL (worked-example, acemi) |
| algoritma / işlem adımı | `anlatim` | izleme (trace) tablosu: adım · durum · neden; küçük girdiyle elle | d2 akış | DENEYSEL |
| kavram / tanım | `anlatim` | tanım düz dil → somut örnek → karşıt örnek (ne DEĞİL) → sınır | concept map | DENEYSEL (Mayer coherence) |
| kavramlar-arası ilişki ağı | d2/dot concept map | Novak: genel üstte, etiketli ok | — (kendisi görsel) | D (Novak) |
| süreç / protokol | `anlatim` | numaralı adımlar + her adımda "neden" | Mermaid/d2 akış | DENEYSEL |
| sayısal örüntü / veri | `tablo` ∨ Vega-Lite | tablo önce, grafik sonra | — | D (data-to-viz) |
| karşılaştırma (nitel) | `tablo` | matris: şey × özellik | — | DENEYSEL |
Kural: diyagram öğrenme kipinde varsayılan değil; anlatım birincil. Her öğrenme çıktısı `ogrenme` bloğunu taşır (hedef · ön bilgi · çözülmüş örnek · kendini sına · tuzaklar). Kalibrasyon: koşum başına Salih "öğrenme hedefli mi / format uygun mu" beyanı.

**Görsel-kalite kuralları (kapı zorlar):** bar/area eksen sıfırdan (lie-factor) · Okabe–Ito renk-körü-güvenli palet · veri satırı = kaynak satırı · 5 zorunlu blok (başlık · kaynak · görsel · açıklama · künye).

**Kalibrasyon kaydı (append):**
- 2026-09-03 · v0 açıldı · koşum 0 · Salih beyanı —
- 2026-09-03 · öğrenme oturumu (6.006 L1 tümevarım kanıtı) · 3 koşum, hepsi `surec` → d2 akış diyagramı, kapı 13/13 · **Salih beyanı: "öğrenme hedefli değil" (0/3)** · teşhis: TÜR seçimi değil YAPI eksik (hedef · çözülmüş örnek · kendini sına · tuzaklar) → skill adım 0 kip tespiti + `ogrenme` bloğu zorunlu + kapı kontrolleri (v0.2). Tür satırı (surec→akış) bu koşumla düşmedi; öğrenme yapısı ayrı boyut.
- 2026-09-03 (2. beyan) · öğrenme sürümleri de d2 akış grafıyla üretildi · **Salih: "öğretme süreci d2 grafı olarak yansıtılmasın; d2 özet olabilir; optimum format konuya göre değişken"** → öğrenme-format tablosu eklendi (anlatım birincil, `ozet_gorsel` ek); v0.3.
