# İB-77 Görsel Atlas — Antitez Raporu (Aile B, Devil's-Advocate)

AS-OF: 2026-09-03. CoVe-Factored: yalnız iddia listesi verildi, tez raporu okunmadı.

## 0. KÜNYE
Açılan/işlenen kaynak sayısı: 9 (arXiv 2406.09961 iki kez — abstract sayfası + html tam metin —, ACL Anthology/arXiv 2303.02927, arXiv 2407.00981, npm/mermaid, npm/vega-lite, github vega/vl-convert, github vega/schema, pygraphviz-discuss grubu, + genel WebSearch sonuçları). Fiilen açılan (WebFetch ile içerik çekilen) kaynak: 2 (arXiv 2406.09961 abstract + html tam metin).

## 1. İddia Tablosu

| # | Hüküm | Kanıt + URL + AS-OF | D/K |
|---|---|---|---|
| 1 | DARALDI | npm kaydı 11.17.2'yi "latest" ve "8 gün önce yayınlandı" olarak doğruluyor (npmjs.com/package/mermaid, AS-OF 2026-09-03) — sürüm doğru ama tarihe bu kadar yakın olması iddiayı KIRILGAN yapıyor: birkaç gün içinde patch çıkarsa iddia bayatlar; "geniş diyagram yelpazesi" ölçülebilir bir sayı taşımıyor, doğrulanamaz-genel ifade. | D |
| 2 | DARALTILDI | npm 6.4.3'ü doğruluyor. Resmi şema URL'i gerçekten var: `https://vega.github.io/schema/vega-lite/v6.json` (github.com/vega/schema, vega.github.io/schema). Ancak "JSON şema tabanlı" ifadesi Vega-Lite'ın kendisinin JSON-Schema İLE DOĞRULANDIĞI anlamına gelmiyor sanılmamalı — şema validasyonu ayrı bir adım, spesifikasyonun kendisi JSON-Schema'yı "kullanır" ama araç zinciri (ör. LLM çıktısı) şemaya karşı otomatik doğrulanmadıkça bu güvence sağlamaz. | K |
| 3 | ÇÜRÜTÜLEMEDİ | ACL Anthology (2023.acl-demo.11) ve arXiv 2303.02927 dört modülü (Summarizer, Goal Explorer, VisGenerator, Infographer) ve ACL 2023 System Demonstrations track'ini doğruluyor. ¬T aranan ama karşı-kanıt bulunamadı — iddia sağlam. | D |
| 4 | ÇÜRÜTÜLEMEDİ | arXiv 2407.00981 rakamları birebir doğruluyor: 2.524 sorgu, 146 veritabanı, 748 tablo, 3 eksen (validity/legality/readability — "uygunluk" çevirisi "legality"ye karşılık geliyor, "geçerlilik/uygunluk/okunabilirlik" isimlendirmesi kabul edilebilir). ¬T bulunamadı. | D |
| 5 | DARALTILDI | arXiv 2406.09961 4.800 örneği doğruluyor; GPT-4o skoru İKİ AYRI GÖREVDE farklı: "Direct Mimic" 82.2, "Customized Mimic" yalnız 61.6 — iddia sadece Direct Mimic'i alıp genel "lider" gibi sunmuşsa eksik. Ayrıca "4 düşük-seviye metrik" makalede açıkça dört isimle listelenmemiş (WebFetch özeti: "multi-level evaluation metrics", isimler metnin ayrıntısında). EN ÖNEMLİSİ — ZAMAN BOYUTU: makale 06-2024 tarihli; GPT-4o o dönemki karşılaştırma setinde en iyisiydi. AS-OF 2026-09-03'te ChartCoder (arXiv 2501.06598), Chart Specification (arXiv 2602.10880), CharTide (arXiv 2604.22192), Aligned Multi-View Scripts (arXiv 2604.24559) gibi 2025-2026 çalışmaları ChartMimic üzerinde GPT-4o'yu geçtiğini iddia ediyor (başlıklarından "advancing"/"improved" dili) — güncel bir ChartMimic lider tablosu bulunamadı (arama sonuçsuz) ama bu yayın akışı "GPT-4o hâlâ lider" iddiasını AS-OF'ta destekLEMİyor; iddia muhtemelen 2024 anlık görüntüsünü güncelmiş gibi sunuyor (anakronizm riski, Karar 68). | K |
| 6 | DARALTILDI | arXiv 2406.09961 html tam metin (Bölüm 4.4 Error Analysis) DÖRT ana hata sınıfı listeliyor: Code-related, Text-related, Type-related, Color-related — yalnız ikisi değil dört. "Halüsinasyon" ayrı bir kategori DEĞİL, metinde "hallucinations... lead to... confusion between similar types of charts" şeklinde Type-related hatanın bir AÇIKLAMASI/nedeni olarak geçiyor, eşit ağırlıklı bağımsız bir sınıf olarak değil. İddia dört sınıftan ikisini öne çıkarıp diğer ikisini (Code-related, Color-related) atlıyor. | K |
| 7 | ÇÜRÜDÜ (kapsamla) | arXiv 2404.00971 ("Beyond Functional Correctness: Exploring Hallucinations in LLM-Generated Code") ve DracoGPT/Synchromesh literatürü: LLM'lerin ham kod üretiminde hem "Invalid Generation" (sözdizimsel bozukluk) hem semantik halüsinasyon yaygın; somut sayı — GPT-3.5-Turbo Vega-Lite tamamlamalarında yalnız **%19.10** geçerli, GPT4-Turbo ise **>%90**. Bu, "doğrulama kapısıyla birlikte yeterince güvenilir" iddiasını MODEL SEÇİMİNE ve versiyon farkına aşırı bağımlı kılıyor — zayıf modelde doğrulama-kapısı tek başına yetmez (kapı sürekli reddedip döngüye girebilir, maliyet/gecikme büyür); iddia "yeterince güvenilir" gibi mutlak bir sonucu, model-bağımlı bir aralığı gizleyerek sunuyor. Mermaid tarafında da ayrı topluluk araçları ("mermaid-validator") "LLM çıktısında sık sözdizimi hatası" sorununu çözmek için doğmuş — sorunun VAR OLDUĞUNUN kendisi dolaylı kanıt. | K |

## 2. Boşluk Doldurma

**(8) Vega-Lite resmi CLI/determinizm:** VAR — `vl-convert` (Rust, github.com/vega/vl-convert) `vl2svg`/`vl2png` komutlarını sağlıyor, Vega-Lite 5.8–6.4 sürümlerini destekliyor. Determinizm iddiası için AÇIK KANIT bulunamadı — repo/README'de "aynı girdi → bit-birebir aynı SVG" garantisi arandı, doğrudan ifade bulunamadı (bulunamadı, meşru boşluk).

**(9) Graphviz `dot` / D2 determinizm:** KARIŞIK. `dot`'un KENDİSİ (statik/hiyerarşik layout) genelde deterministik kabul edilir, ancak **PyGraphviz** tarafında belgelenmiş bir NON-determinizm sorunu var (pygraphviz-discuss grubu: "graph layouts not deterministic... API sabit seed kullanmayı belgelemiyor", iç veri yapısı sıralamasından kaynaklanıyor) — yani "Graphviz determinizmi" iddiası sarmalayıcıya (Python binding) göre değişir, mutlak değil. D2 için determinizm belgesi bulunamadı (bulunamadı).

## 3. Tez İçin Önerilen Daraltmalar
1. "geniş diyagram yelpazesi" yerine somut diyagram tipi sayısı verilsin.
2. "resmi şema URL'i mevcuttur" ifadesine, bunun otomatik doğrulama sağlamadığı notu eklensin.
3. Değişmesin (çürütülemedi).
4. Değişmesin (çürütülemedi).
5. "GPT-4o lider" ifadesi "2024 ChartMimic yayınında test edilen modeller arasında Direct-Mimic görevinde lider (61.6/82.2 görev-ayrımıyla); 2025-26 özelleşmiş modellerle güncel kıyas yok" şeklinde daraltılsın.
6. "ana hata sınıfları halüsinasyon ve tip-karışıklığı" yerine "dört sınıf (kod/metin/tip/renk); halüsinasyon tip-hatasının bir nedeni" denilsin.
7. "yeterince güvenilirdir" hükmü kaldırılıp "model sürümüne göre %19-%90 arası geçerlilik oranı; doğrulama-kapısı zayıf modelde döngü/maliyet riski taşır" şeklinde koşullu yazılsın.
