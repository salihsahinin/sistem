# Görev Emri — İB-53 atlas koşumu: görüntüleme-katmanı inşası (3 aile, m.40b v0.2)

*Derleyen: Carvis ana-sıra (Fable), 2026-08-29 seans-21. Tetik: Salih "atlası koştur" (İB-53 inşa-vizyonu soruları: dış emsal · 3B/2B görüntü · kombinasyon). Koşum-önü kontrol: dış tarama daha önce KOŞMADI (yalnız iç envanter `raporlar/2026-08-29-ib53-kapsama-haritasi.md` + Karar 72 md-editör pazar sayımı). Karar-öncesi kullanım: sonuç İB-53 (2) a-d seçenekleriyle BİRLEŞİK tek masada Salih'e.*

**Gereksinim profili (ailelere gömülü sabit blok):** ① kaynak = yerel md deposu + silver SQLite referans grafı (tek-kaynak) ② türev DETERMİNİSTİK derlenir (LLM'siz; Karar 65), gövdeye dokunmaz (m.8) ③ pointer türleri: `yol` · `yol:satır` · `[[wikilink]]` (9.793 referans, 544 dosya) ④ insan yüzeyi: tıklanabilir gezinme + graf/odak panosu ⑤ birincil editör VS Code (Karar 80) ⑥ yerel/açık-kaynak tercih.

## Aileler (dik)
- **A — dış emsaller:** md/kod deposundan bilgi-grafiği-UI türeten araçlar (Foam, Dendron, Quartz sınıfı; Sourcegraph/SCIP, CodeSee-sınıfı code-map; tree-sitter/ctags harita araçları) — hangisi DIŞ graf verisi alabilir, satır-düzeyi gezinme, VS Code entegrasyonu, canlılık, lisans; profil-eşleşme tablosu.
- **B — görsel-temsil kanıtı:** 2B↔3B düğüm-bağ görselleştirmesi görev-performans ölçümleri (birincil deneyler; masaüstü ↔ stereo/VR ayrımı), düğüm-sayısı okunabilirlik eşikleri, focus+context kanıtı → "3B'ye yatırım?" sorusunun kanıt cevabı.
- **C — pipeline emsalleri:** "DB → typed IR → deterministik derleme → statik HTML/SVG" desenli sistemler (archify-benzeri IR derleyiciler, D2/Graphviz doc-pipeline'ları, Quartz graf-json, Backstage TechDocs, SCIP); IR formatlarının satır-adresliliği; statik-türev ↔ canlı-sunucu; VS Code webview paneli desenleri.

## Kurallar (her ajana aynen)
URL zorunlu · rakam kaynaklı, kestirim `[?]` · uydurma YASAK, "bulunamadı" meşru · 403/paywall açık bayrak · her iddia AS-OF damgalı (Karar 68) · ham-metin kuralı (tırnak-içi alıntı = ham kaynaktan + bölüm beyanı; Karar 79 D5) · işçi bütçesi 10-15k sınıfı · çıktı dosyaya, dönüş ≤5 satır.

## Akış + çıktılar
Tez ×3 (paralel, bağımsız) → `cc/rapor-2026-08-29-ib53-atlas-tez-{a,b,c}.md` → iddia listeleri (gerekçesiz, CoVe-Factored) → antitez ×3 → `...-antitez-{a,b,c}.md` → V26 kural-tabanlı örneklem-denetimi → maskeli hakem (web'siz) → sentez raporu `raporlar/2026-08-29-ib53-atlas.md` (D/K/X + hayatta-kalan çekirdek). Hayatta-kalma oranı deftere tek satır.
