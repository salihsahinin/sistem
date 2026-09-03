# İB-77 Atlas Görselleştirme — HAKEM Raporu (m.40b aşama 3)

## 0. KÜNYE + maskeleme şerhi
Hakem: bu ajan (Karar 86 D3-i, karar vermez, sentez yazmaz). Girdi: tez A/B, antitez A/B, V26 denetimi, iç-envanter C (yalnız pointer). AS-OF 2026-09-03.
**MASKELEME ŞERHİ (K2-k):** dosya adları (`-A`/`-B`/`-antitez-`) tez/antitez kimliğini açıkça sızdırıyor; yine de kıyas aşağıda ETİKET üzerinden değil, iddia+kanıt düzeyinde yapıldı.

## 1. Tablo A (Aile A — Kuram+Öğrenme, 14 iddia)
| # | İddia (kısa) | D/K/X | Hayatta-kalma | Not |
|---|---|---|---|---|
|1|Lie factor=grafik/veri etkisi|D|DARALDI|Formül D (V26 doğruladı); "genel yanıltıcılık göstergesi" iddiası Lo 2023/baseline-paradox ile daralıyor|
|2|Cleveland-McGill sıralaması|D|DARALDI|Heer&Bostock (2010) "kabul edilebilir sapmayla" doğruladı, tüm görevlere genellenmedi|
|3|Munzner 4 katman|D|SAĞLAM|Antitez birincil PDF'i (cs.ubc.ca) fiilen açtı, birebir doğrulandı|
|4|Mayer 5 ilke deneysel destekli|D|DARALDI|İsimler/varlık D; 2025 meta-analiz çok küçük/karışık etki (g≈-0.4) buluyor|
|5|Coherence etkisi ~0.86|K|DARALDI|Rakam Mayer'in KENDİ raporu (bağımsız değil); bağımsız meta-analiz g=-0.37…-0.41|
|6|Spatial contiguity ~1.10|X|DÜŞTÜ|Rakam hiçbir birincil kaynakta yok; en yakın Ginns(2006) d=0.85 (ÜGA 1.02). **İki rakam: 1.10 vs 0.85(≤1.02)**|
|7|Sweller 3 yük türü|D|DARALDI|Klasik doğru; germane-load sonraki yazında tartışmalı|
|8|Worked-example öğrenmeyi iyileştirir|D|DARALDI|Yalnız acemi öğrenicide (expertise-reversal); koşulsuz ifade aşırı-genelleme|
|9|Novak concept-map/Ausubel, hiyerarşik|D|SAĞLAM|Antitez çürütemedi, tarihsel/tanımsal doğru|
|10|Concept map öğrenmeyi/tutulumu artırır|D|DARALDI|Nesbit&Adesope (55 çalışma) yön doğru, büyüklük son derece heterojen|
|11|data-to-viz 5 eksen|X|DÜŞTÜ|Site fiilen 6 dal gösteriyor. **İki rakam: 5 vs 6**|
|12|FT Visual Vocabulary 9 kategori|D|SAĞLAM|Antitez+V26 ikisi de birebir doğruladı|
|13|Düşük data-ink=chartjunk (norm-kural)|X|DÜŞTÜ|Tanım D (V26) ama Bateman 2010 (CHI): süsleme 2-3 hafta sonra hatırlamayı ARTIRIYOR, anlamayı bozmuyor — çelişkili, norm-kural olarak çürüdü|
|14|Metin-türü→diyagram-türü sezgisel eşleme|K|DARALDI|Tek normatif kaynak yok (tez de kendi işaretlemiş); Tversky farklı eksen (ok-varlığı) sunuyor|

## 2. Tablo B (Aile B — Araç+Emsal, 11 iddia)
| # | İddia (kısa) | D/K/X | Hayatta-kalma | Not |
|---|---|---|---|---|
|1|Mermaid v11.17.2, CDN-ESM, geniş yelpaze|D|DARALDI|Sürüm doğru ama 8 gün önce yayınlanmış (kırılgan); "geniş" ölçülemez|
|2|Vega-Lite şema URL'i doğrulama kapısı sağlar|K|DARALDI|Şema var ama kendiliğinden otomatik doğrulama SAĞLAMIYOR — ayrı adım gerekir|
|3|LIDA 4 modül, ACL2023|D|SAĞLAM|Antitez+V26 birebir doğruladı|
|4|LIDA hedef kütüphane/metrik bu kaynakta yok|K|DARALDI|Kendi kendine işaretli açık boşluk, değişmedi|
|5|VisEval 2.524/146, 3 eksen|D|SAĞLAM|Antitez birincil arXiv'i açıp birebir doğruladı|
|6|ChartMimic 4.800, GPT-4o %82.2 lider|D|DARALDI|Rakam D ama %82.2 yalnız "Direct Mimic"; "Customized Mimic" %61.6 gizli; ayrıca 2025-26 modelleri geçmiş olabilir (anakronizm riski, Karar 68)|
|7|ChartMimic ana hata sınıfı=halüsinasyon+tip-karışıklığı|X|DÜŞTÜ|Makale 4 kategori listeliyor (kod/metin/tip/renk); halüsinasyon bağımsız kategori değil, tip-hatasının nedeni|
|8|D2 CLI/determinizm doğrulanmadı|K|DARALDI|Açık boşluk kaldı, kimse çözemedi|
|9|Vega-Lite CLI varlığı doğrulanmadı|D|SAĞLAM|Antitez `vl-convert` (vl2svg/vl2png) buldu — varlık artık D; determinizm ayrı, hâlâ açık|
|10|Graphviz/PlantUML/vb. hiç doğrulanmadı|K|DARALDI|`dot` V26 ile kısmen D; PyGraphviz'te belgeli non-determinizm; PlantUML/Excalidraw/Markmap tümüyle açık|
|11|nvBench/ChartGPT/Text2Vis/Data Formulator araştırılmadı|K|kapsam-dışı|Hüküm yok, dürüst boşluk beyanı|

## 3. Sayım
Birleşik (25 iddia): **D=14 (%56) · K=7 (%28) · X=4 (%16)**. Hayatta-kalma: **SAĞLAM=6 (%24) · DARALDI=15 (%60) · DÜŞTÜ=4 (%16)**.
A: D9/K2/X3 (64/14/21); B: D5/K5/X1 (45/45/9).

## 4. Tasarım soruları
- **T1** (metin-tür→diyagram-tür normatif kaynak): **X** — böyle bir normatif tablo literatürde bulunamadı (tez de antitez de); Tversky farklı bir eksen (ok-varlığı=işlevsel/nedensel vs oksuz=yapısal) sunuyor, doğrudan eşleme değil.
- **T2** (LLM-spec+LLM'siz kapı yeterli mi): **K, koşullu** — şema-doğrulama + render-testi LLM'siz ve mümkün, ama "yeterlilik" model-versiyonuna aşırı bağımlı: GPT-3.5-Turbo Vega-Lite geçerliliği %19, GPT4-Turbo >%90; zayıf modelde kapı döngü/maliyet riski taşır.
- **T3** (adversarial'dan sağlam Mayer/Sweller kuralları): hiçbiri koşulsuz SAĞLAM değil. Uygulanabilir liste (hepsi koşullu-DARALDI): coherence, signaling, spatial-contiguity — YÖN olarak sağlam, BÜYÜKLÜK tartışmalı; worked-example YALNIZ acemi öğrenicide.
- **T4** (data-ink minimalizmi kural olarak yazılabilir mi): **X** — koşulsuz yazılamaz; Bateman (2010) süslemenin uzun-vadeli hatırlamayı artırdığını gösterdi, ilke göreve bağlı.

## 5. Sentez yazarına — kullanılamaz kanıt (X) listesi
1. Spatial contiguity "~1.10" rakamı — kullan 0.85 (ÜGA 1.02) veya temporal-contiguity 1.30, karıştırma.
2. Data-to-viz "5 eksen" — site fiilen 6 dal gösteriyor, düzelt.
3. "Düşük data-ink=chartjunk" norm-kuralı olarak yazma — Bateman 2010 ile çelişiyor, göreve-bağlı ifade kullan.
4. ChartMimic "ana hata sınıfı halüsinasyon+tip-karışıklığı" — gerçek 4 kategori (kod/metin/tip/renk), halüsinasyon bağımsız değil.
5. "Metin-türü→diyagram-türü" için tek normatif kaynak iddiası — böyle bir kaynak yok, sezgisel/türetilmiş olarak işaretle.
