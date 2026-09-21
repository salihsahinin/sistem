# V26 Örneklem-Denetimi — Bitirme Tezi Atlas Koşumları (Aile C + Aile D)

**Denetleyen:** Atlas (V26 örneklem-denetim rolü, kural-tabanlı) · **Çekim tarihi (AS-OF):** 2026-09-21
**Yöntem notu:** (b) sondajında "sayısal iddia" birimi = aynı cümle/aynı kaynak-atfı içinde geçen rakam kümesi (ör. "5/6 problem, 35/42 puan, 4.5 saat" tek birim sayıldı; farklı kaynağa/cümleye geçince yeni birim başladı). WEF PDF (>10 MB, WebFetch sınırını aştı) `curl -sL` + `pdftotext -layout` ile indirilip birincil metinden doğrudan okundu. arXiv "abs" sayfaları özet düzeyinde doğrulama sağlar; tam metin iddiaları ("makalenin içeriği X'ten bahsetmiyor" türü) için ayrıca işaretlendi.

---

## Rapor 1/4: `rapor-2026-09-21-bitirme-tez-C-ai-matematik-durum.md` (Atlas TEZ, Aile C — 108 satır, son 1/3: satır 73-108)

| Ajan/rapor | Sondaj türü | Denetlenen iddia | URL | Kaynak kanıtı (≤15 kelime, bölüm) | Sonuç | Not |
|---|---|---|---|---|---|---|
| Tez-C | a | (satır 73, tablo) "LeanCopilot (MIT, GPU isteğe bağlı)" | https://github.com/lean-dojo/LeanCopilot | "MIT license"; "Optional (recommended if CUDA-enabled GPU)" (README) | TUTTU | CPU'da çalıştığı iddiası da doğrulandı |
| Tez-C | b1 | (satır13) DeepMind: 6'dan 5/6 çözüldü, 35/42, 2025-07-21, 4.5 saat | https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/ | "solved five out of six...earning 35...4.5-hour" (blog gövdesi) | TUTTU | — |
| Tez-C | b2 | (satır14) 2024 AlphaProof+AlphaGeometry2: 2-3 gün, 28/42, gümüş, 4 problem | (aynı DeepMind blog) | "four out of six...28 points...silver...2-3 days" | TUTTU | Rapor "aynı kaynak" demişti, doğru |
| Tez-C | b3 | (satır15) OpenAI aynı gün (2025-07-21) 35/42 | URL verilmemiş (yalnız "TechCrunch/Zvi Substack" adı anılmış) | — | URL YOK | Çapraz kaynak (bkz. Rapor2/b2): gerçek tarih 2025-07-19, rapor 07-21 yazmış — olası tarih hatası ama bu URL'siz sondaj için doğrulama yapılamadı |
| Tez-C | b4 | (satır16) Aristotle 5/6 problem çözüp altın-eşdeğer | https://arxiv.org/abs/2510.01346 | özet yalnız "gold-medal-equivalent performance" diyor, "5/6" sayısı yok | TUTMADI | Fark: problem sayısı (5/6) kaynağın özetinde belirtilmiyor |
| Tez-C | b5 | (satır17) IMO2026 Şangay, dots-note-3.0 6/6=42/42 | URL verilmemiş (SCMP/Rohan Paul/Zamin.uz adı anılmış, link yok) | — | URL YOK | Rapor kendi de "X, ek doğrulama gerekir" diye işaretlemiş |
| Tez-C | b6 | (satır18) Erdős 2026-08-03: 565 çözüldü, 652 açık | https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/ | "565 solved problems and 652 open ones" | TUTTU | — |
| Tez-C | b7 | (satır18) OpenAI 2026-05-20 unit-distance çürütme; 2026-08-01 10 ek ilerleme | (aynı Quanta) | "On May 20, 2026...unit distance"; "August 1...10 additional...advances" | TUTTU | — |
| Tez-C | b8 | (satır18) DeepMind 13 problem (4 yeni + 9 yeniden keşif) | (aynı Quanta) | "solving four problems and finding...solutions to nine more" | TUTTU | — |
| Tez-C | b9 | (satır19) Erdős #1196, 2026-05, Tao dahil | URL verilmemiş (yalnız WebSearch özeti) | — | URL YOK | Rapor kendi de "K, ayrı doğrulanmadı" diyor |
| Tez-C | b10 | (satır21) FrontierMath Tiers1-3 v2: 2026-06-12, 295+43=338, Tier1-3'te 123 düzeltme/5 çıkarma, Tier4'te 12 düzeltme/7 çıkarma | https://epoch.ai/benchmarks/frontiermath-tiers-1-3-v2 | "2026-06-12"; "123 problems corrected"/"5 removed"; "12 corrected"/"7 removed" | TUTTU | — |
| Tez-C | b11 | (satır22) GPT-5 ~%25, o4-mini ~%20 FrontierMath skoru | URL verilmemiş (yalnız arama özeti; rapor da doğrulanmadığını söylüyor) | — | URL YOK | Rapor kendi tutarlı: "sayfada görülmedi" |
| Tez-C | b12 | (satır23) FrontierMath Erdős: 2026-09-01, 68 problem (~%10 of 652), 300$/72sa | https://epoch.ai/latest/announcing-frontiermath-erdos | "Sep 1, 2026"; "68...problems"; "~10%"; "$300 per problem"; "72 hours" | TUTTU | — |
| Tez-C | b13 | (satır23) GPT-6 Astra resmi 2/68 (%3), diğerleri %0, gayri-resmi toplam 5 | (aynı Epoch) | "2 problemi çözdü (%3)"; diğerleri "%0"; gayri-resmi "toplam 5" | TUTTU | — |
| Tez-C | b14 | (satır25) DeepSeek-Prover-V2-671B: MiniF2F %88.9, PutnamBench 49/658 | https://arxiv.org/abs/2504.21801 | "88.9% pass ratio"; "solving 49 out of 658" | TUTTU | — |
| Tez-C | b15 | (satır26) Goedel-Prover-V2 32B: pass@32 %88.1, 2-tur %90.4, "80× daha küçük" | https://arxiv.org/abs/2508.03613 | "88.1%...pass@32"; "90.4%...self-correction"; "80X smaller" | TUTMADI | Fark: "80× daha küçük" iddiası kaynakta 8B modele (671B'ye karşı) ait, 32B'ye değil; rapor bu ayrımı yapmadan 32B satırına bağlamış |
| Tez-C | c | (satır100) IMO2026'da "dört AI mükemmel skor aldı" başlığı (digitalapplied.com) | URL verilmemiş (yalnız domain adı, tıklanabilir link yok) | — | URL YOK | Rapor zaten "X, çözülmedi" diye işaretlemiş; çapraz not: Rapor2/EK-SORU-1 bu domaini gerçekten açmış ve gayri-resmi/sertifikasız olarak 4'ten fazla model iddiasını bulmuş |

**kesildi: 15/23** (8 ek sayısal iddia doğrulanmadı: Kimina-Prover %92.2 satır27; Mathlib 288.718/136.941/772 satır33; WebSearch alt-rakamlar 210.000+/100.000+ satır33; miniF2F 488 satır36; PutnamBench-arXiv 1.692/640 satır38; PutnamBench-GitHub 1.724/672/640/412 satır39; LeanCopilot 939 commit satır42; arXiv 2607.07779 tarihi satır48)

**Rapor 1 özet:** TUTTU 10 (a dahil) · TUTMADI 2 · URL YOK 5 · ERİŞİLEMEDİ 0

---

## Rapor 2/4: `rapor-2026-09-21-bitirme-antitez-C.md` (Atlas ANTİTEZ, ¬C — 114 satır, son 1/3: satır 77-114)

| Ajan/rapor | Sondaj türü | Denetlenen iddia | URL | Kaynak kanıtı (≤15 kelime, bölüm) | Sonuç | Not |
|---|---|---|---|---|---|---|
| Antitez-C | a | (satır100, EK-SORU-1) Huawei Celia + RedNote dots-note-3.0, ikisi de 42/42 "officially graded" | https://tech-insider.org/ai-imo-2026-perfect-score-odds-hit-96-percent/ | "officially graded 42 out of 42"; "IMO's own formal grading process" | TUTTU | "İnsan müdahalesi olmadan" kısmı açık alıntı değil, bağlamdan çıkarım |
| Antitez-C | b1 | (satır15) DeepMind 35/42, 2025-07-21 | DeepMind blog (yk.) | "35 total points"; "21 Temmuz 2025" | TUTTU | — |
| Antitez-C | b2 | (satır16) OpenAI 35/42, 2025-07-19 (Alexander Wei/X) | https://simonwillison.net/2025/Jul/19/openai-gold-medal-math-olympiad/ | "19th July 2025"; "35/42 points...enough for gold" | TUTTU | — |
| Antitez-C | b3 | (satır17) "3 eski IMO madalyalısı" değerlendirdi, IMO zamanlama eleştirisi | https://www.lesswrong.com/posts/ZkgaPopsBkQgeA2k8/google-and-openai-get-2025-imo-gold | "üç eski IMO madalyalısı...bağımsız"; "dolaylı eleştiriler" | TUTTU | Eleştiri "dolaylı" nitelendirilmiş, rapor "eleştirdi" diyor — ton farkı küçük |
| Antitez-C | b4 | (satır24) dots-note-3.0 42/42 "ilk kez", kaynağı modelin kendi sitesi | https://www.scmp.com/tech/article/3361482/worlds-first-ai-model-earn-perfect-score-maths-olympiad-comes-chinas-rednote | "all six puzzles...42"; "For the first time"; kaynak "a post on the model's website" | TUTTU | — |
| Antitez-C | b5 | (satır32) 565 çözüldü/652 açık, 2026-08-03 | Quanta Magazine (yk.) | "565 solved problems and 652 open ones" | TUTTU | — |
| Antitez-C | b6 | (satır33) İkincil kaynak "%41 çözülmüş" diyor (çelişki notu) | URL verilmemiş | — | URL YOK | Rapor zaten bunun Quanta'nın rakamı olmadığını söylüyor |
| Antitez-C | b7 | (satır39) 68 problem, 2026-09-01, GPT-6 Astra 2/68, diğerleri %0 | Epoch AI Erdős (yk.) | "Sep 1, 2026"; "2 problemi çözdü (%3)"; diğerleri "%0" | TUTTU | — |
| Antitez-C | b8 | (satır40) Ek gayri-resmi denemelerde 5/68 (resmi sayılmıyor) | Epoch AI Erdős (yk.) | "toplam 5 of the 68"; "not a FrontierMath Erdős score" | TUTTU | — |
| Antitez-C | b9 | (satır41) $218/15sa vs $222/10sa ikincil kaynak çelişkisi | URL verilmemiş | — | URL YOK | Rapor "önemsiz" diye zaten düşük öncelikli işaretlemiş |
| Antitez-C | b10 | (satır47) Mathlib 288.718 teorem, 136.941 tanım | https://leanprover-community.github.io/mathlib_stats.html | "Theorems: 288,718"; "Definitions: 136,941" | TUTTU | — |
| Antitez-C | b11 | (satır48) arXiv 2604.24797: "308.129 declarations" | https://arxiv.org/abs/2604.24797 | "a multilayer graph of 308,129 declarations" | TUTTU | — |
| Antitez-C | b12 | (satır54) PutnamBench 1.724 (672/640/412), Apache2.0/MIT | https://github.com/trishullab/PutnamBench | "1,724...672/640/412"; "Apache 2.0...MIT for Coq" | TUTTU | — |
| Antitez-C | b13 | (satır66) DeepSeek-Prover-V2 %88.9 MiniF2F, PutnamBench 47/658 | https://arxiv.org/abs/2504.21801 | "88.9% pass ratio"; gerçek rakam "solving 49 out of 658" | TUTMADI | Fark: kaynak 49/658 diyor, rapor 47/658 yazmış (rapor1'in aynı iddiası — b14 — doğru "49" vermişti) |
| Antitez-C | b14 | (satır72) Goedel-Prover-V2 %88.1/%90.4 | https://arxiv.org/abs/2508.03613 | "88.1%...pass@32"; "90.4%...self-correction" | TUTTU | — |
| Antitez-C | b15 | (satır78) arXiv 2607.07779, 2026-07-08, 19 yazar | https://arxiv.org/abs/2607.07779 | "19 yazarı"; "8 Temmuz 2026'da gönderilmiş"; Tao yazarlar arasında | TUTTU | Ayrıca: makale özeti gerçekten "proof explanation/interpretability" konusuna değinmiyor (rapor1'in §3 atfı bağımsız olarak da yanlış çıkıyor) |
| Antitez-C | c | (satır106, EK-SORU-3) Goedel-Prover-V2 32B "24-48GB VRAM sınıfı GPU gerektirir" | URL verilmemiş, rapor kendi `[?]` işaretlemiş | — | URL YOK | Kendi kendine dürüst: "kesin VRAM rakamı doğrulanmadı" |

**kesildi: 15/20** (5 ek: EK-SORU-1 42/42 bundle + "96 percent" başlığı; EK-SORU-2 %86; EK-SORU-3 671B/32B bundle; Kaynak Sayımı 12+~12; Genel özet 12/8-9/2/1 bundle)

**Rapor 2 özet:** TUTTU 13 (a dahil) · TUTMADI 1 · URL YOK 3 · ERİŞİLEMEDİ 0

---

## Rapor 3/4: `rapor-2026-09-21-bitirme-tez-D-meslek-format.md` (Atlas TEZ, Aile D — 132 satır, son 1/3: satır 89-132)

| Ajan/rapor | Sondaj türü | Denetlenen iddia | URL | Kaynak kanıtı (≤15 kelime, bölüm) | Sonuç | Not |
|---|---|---|---|---|---|---|
| Tez-D | a | (satır95, taksonomi tablosu i) "Mathlib Initiative / Buzzard örneği gerçek emsal" | https://lims.ac.uk/event/ai-and-the-formalisation-of-mathematics/ | Sayfa yalnız 9 Mart 2026 seminer duyurusu; Buzzard/Mathlib Initiative/satır-sayısı hiç geçmiyor | TUTMADI | Verilen URL iddiayı desteklemiyor (bkz. b6 için ikinci kaynakla kısmi düzelme) |
| Tez-D | b1 | (satır13-14) BLS: %10 genel/%1 mathematicians/%11 statisticians, ~2000/yıl, 2025-2035 | https://www.bls.gov/ooh/math/mathematicians-and-statisticians.htm | "grow 10 percent"; "Mathematicians %1"; "Statisticians %11"; "2,000 openings" | TUTTU | Sayfa güncelleme tarihi 2026-08-27 teyit edildi |
| Tez-D | b2 | (satır17) WEF: 1000+ işveren/14M+ çalışan/22 sektör/55 ekonomi, %39 beceri değişimi | https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf | "1,000 employers...14 million workers...22 industry clusters and 55 economies"; "(39%)...transformed" | TUTTU | curl+pdftotext ile birincil metinden doğrulandı (WebFetch 10MB sınırını aştı) |
| Tez-D | b3 | (satır20-21) FrontierMath: 338 soru (Tier1-4), 70+ matematikçi | https://epoch.ai/frontiermath | Sayfa 4-tier yapısını doğruluyor ama "338" ve "70+" bu sayfada geçmiyor ("several hundred" diyor) | TUTMADI | Kısmi: 338 rakamı yalnız kardeş sayfada (frontiermath-tiers-1-3-v2) doğrulanabiliyor, verilen bu URL'de yok |
| Tez-D | b4 | (satır21-22) FrontierMath Tier4: 48 özel sorudan 17'si (2026 Ocak) | https://ourworldindata.org/grapher/ai-frontiermath-over-time | Sayfa açıkça "Tier 4 contains 43...problems and is **not included here**" diyor | TUTMADI | Verilen URL Tier4'ü kapsam dışı bırakıyor; 17/48 rakamı bu sayfada yok |
| Tez-D | b5 | (satır25-26) Anthropic: ~%4 işgücü, ~%30 anket payı, %57/%43 | https://www.anthropic.com/economic-index | Sayfa JS-yüklemeli gösterge panosu, statik metinde rakam yok ("Loading data") | ERİŞİLEMEDİ | Aynı veri anthropic.com/news üzerinden (Rapor4/b7) ayrıca doğrulandı — orada TUTTU |
| Tez-D | b6 | (satır32-34) Buzzard 2025 Oxford Strachey Lecture; Mathlib ~2 milyon satır | lims.ac.uk + renaissancephilanthropy.org | 2. URL: "nearly two million lines"; Strachey Lecture HİÇBİR verilen URL'de yok | TUTMADI | Fark: "~2M satır" TUTTU (2. kaynakta) ama "Strachey Lecture" iddiası iki kaynakta da bulunamadı |
| Tez-D | b7 | (satır36-37) de Bruijn faktörü ~20 (2023-24), 1-altı engel yok | https://teorth.github.io/tao-web/ai-views.html | "'de Bruijn factor' at ~20 (2023–24)"; "'no fundamental obstacle' to falling below 1" | TUTTU | — |
| Tez-D | b8 | (satır43) Harmonic 9-10 açık pozisyon | https://www.harmonic.fun/careers/ | "9 full-time engineering roles" | TUTTU | — |
| Tez-D | b9 | (satır56-57) İTÜ MAT4901/4902, 4 şablon | https://matmuh.itu.edu.tr/egitim/lisans/bitirme-staj | "4 ders şablonu"; MAT4901/4901E/4902/4902E | TUTTU | — |
| Tez-D | b10 | (satır68-69) YTÜ EEE kılavuzu, 2024-05 tarihli, bölüme göre ad ayrımı | https://elm.yildiz.edu.tr/.../bitirme-calismasi-yazim-kilavuzu.pdf | Bölüm ayrımı TUTTU; PDF meta-tarihi "D:20240105" (5 Ocak 2024) | TUTMADI | Fark: rapor "2024-05" diyor, PDF'in kendi meta-tarihi 2024-01; muhtemelen dizin-yolu damgası karıştırılmış |
| Tez-D | b11 | (satır78, tablo) Cambridge MPhil PINN tezi, 2024-01 | https://arxiv.org/abs/2401.03534 | Başlık+tarih ("7 Jan 2024") TUTTU; "Cambridge"/"MPhil" özet sayfasında yok | TUTMADI | Kısmi — rapor bunu zaten K diye işaretlemişti, tutarlı |
| Tez-D | b12 | (satır80, tablo) LeanMarathon, arXiv 2026-06 | https://arxiv.org/abs/2606.05400 | Başlık birebir; "Submitted on 3 Jun 2026" | TUTTU | — |
| Tez-D | b13 | (satır81, tablo) Beyond the Library, arXiv 2026-06 | https://arxiv.org/abs/2606.31134 | Başlık birebir; "submitted...June 30, 2026" | TUTTU | — |
| Tez-D | b14 | (satır82, tablo) U-MATH/UGMathBench, arXiv/ICLR 2025 | https://arxiv.org/abs/2412.03205 | Konu doğru ama "Submission history"nde ICLR 2025 referansı yok | TUTMADI | Fark: ICLR 2025 bağlantısı kaynakta doğrulanamadı, yalnız arXiv ön-baskı görünüyor |
| Tez-D | b15 | (satır83, tablo) Berkeley EECS TR, Yue/Klein, 2025 | https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-121.pdf | "Jonathan Yue, Daniel Klein...UC Berkeley...May 16, 2025...'thesis submitted'" | TUTTU | curl+pdftotext ile okundu |
| Tez-D | c | (satır99, taksonomi tablosu v) "AI'nin ispatı üretmesi ile öğrencinin anlaması arasındaki fark jüride tartışma konusu olabilir" | URL verilmemiş, rapor kendi "kestirim `[?]`" diyor | — | URL YOK | Dürüstçe işaretlenmiş kestirim |

**kesildi: 15/16** (1 ek: YÖK/dergipark "84 yüksek lisans tezi 2017-2021" satır87, tam URL'li ama sıra dışı kaldı)

**Rapor 3 özet:** TUTTU 8 (a hariç) · TUTMADI 7 (a dahil) · URL YOK 1 · ERİŞİLEMEDİ 1

---

## Rapor 4/4: `rapor-2026-09-21-bitirme-antitez-D.md` (Atlas ANTİTEZ, ¬D — 151 satır, son 1/3: satır 101-151)

| Ajan/rapor | Sondaj türü | Denetlenen iddia | URL | Kaynak kanıtı (≤15 kelime, bölüm) | Sonuç | Not |
|---|---|---|---|---|---|---|
| Antitez-D | a | (satır109, D11) YTÜ Matematik Müh. sayfası "Sayfa Hazırlanıyor...", içerik yok | https://matmuh.yildiz.edu.tr/ | "yalnızca 'Sayfa Hazırlanıyor...' yer tutucu"; "akademik içerik yoktur" | TUTTU | — |
| Antitez-D | b1 | (satır14) BLS %1/%11/%10, ~2000/yıl, 2025-2035 | bls.gov (yk.) | Aynı rakamlar, Rapor3/b1 ile birebir | TUTTU | — |
| Antitez-D | b2 | (satır25-29) WEF: 15'li "fastest-growing jobs" listesi (s.19), Table A3 s.103 "Mathematicians, Actuaries and Statisticians" | WEF PDF (yk.) | Liste 15 kalemle birebir eşleşti (curl+pdftotext); Table A3 satırı bulundu | TUTTU | "Data Scientist" tek başlık değil, "Data Analysts and Scientists" — raporun kendi notuyla tutarlı |
| Antitez-D | b3 | (satır39) FrontierMath Tier4: 50 problem (2 kamuya açık+48 özel) | https://epoch.ai/benchmarks/frontiermath-tier-4-v1 | "2 problems...public...48 problems...private" | TUTTU | — |
| Antitez-D | b4 | (satır39) 17/48 (%35), GPT-5.2 Pro 15/48, önceki rekor 13, +4 yeni | https://epochai.substack.com/p/new-record-on-frontiermath-tier-4 | "17/48 (35%)"; "15/48 (31%)"; "13 problems...had been solved" | TUTTU | Kaynak "13 problem" diyor (payda vermiyor), rapor "13/48" yazmış — sayısal olarak tutarlı |
| Antitez-D | b5 | (satır59) Mathlib "yaklaşık 2 milyon satır" | https://lean-lang.org/use-cases/mathlib/ | "over two million lines of formalized mathematics" | TUTTU | — |
| Antitez-D | b6 | (satır69) Harmonic 9 pozisyon, Formal Verification Engineer Palo Alto/Londra | https://www.harmonic.fun/careers/ | "9 full-time engineering roles"; "Palo Alto, London" | TUTTU | — |
| Antitez-D | b7 | (satır79) Anthropic %37.2 kullanım / %3.4 işgücü (2025-02) | https://www.anthropic.com/news/the-anthropic-economic-index | "37.2%"; "3.4%"; "Feb 10, 2025"; "arXiv:2503.04761" | TUTTU | — |
| Antitez-D | b8 | (satır79) Ocak 2026 raporu: ~%33 Claude.ai, ~%46 API, işgücü payı ayrı verilmiyor | https://www.anthropic.com/research/anthropic-economic-index-january-2026-report | "a third of conversations"; "%46"; "regresyon" (yüzde yerine korelasyon) | TUTTU | — |
| Antitez-D | b9 | (satır89) İTÜ MAT4901/4902, 4 şablon | matmuh.itu.edu.tr (yk.) | "4 ders şablonu" | TUTTU | — |
| Antitez-D | b10 | (satır99) YTÜ EEF kılavuzu s.2, bölüme göre ad ayrımı | elm.yildiz.edu.tr PDF (yk.) | "Bilgisayar...Bitirme Projesi"; "Elektrik...Bitirme Tezi veya...Projesi" | TUTTU | — |
| Antitez-D | b11 | (satır119) de Bruijn ~20 (2023-24), 1-altı engel yok | teorth.github.io (yk.) | "~20 (2023–24)"; "no fundamental obstacle" | TUTTU | Nüans (2025-26'da "essentially emptied queue") de doğrulandı |
| Antitez-D | b12 | (satır131) AI ücret primi 2025'te %56 | https://youngandcalculated.substack.com/p/quant-finance-vs-ai-labs-where-the | "56% wage premium on AI skills" | TUTTU | 2024'ün "%25" rakamı fetch özetinde ayrıca alıntılanmadı, çelişki de yok |
| Antitez-D | b13 | (satır131) İş ilanları %78 artış, aday havuzu %24, 3.4 pozisyon/aday | (aynı substack) | "grew 78%"; "grew 24%"; "roughly 3.4 open roles" | TUTTU | — |
| Antitez-D | b14 | (satır131) Anthropic L5 $700-950k, OpenAI L5 ~$1.15M, Meta 4yıl $300M | (aynı substack) | "$700k-$950k"; "~$1.15M"; "4 yılda $300M" | TUTTU | — |
| Antitez-D | b15 | (satır151) "18 kaynak açıldı, 4 başarısız deneme" | URL verilmemiş (öz-bildirim) | — | URL YOK | Süreç kendi-bildirimi, dış URL yok — doğası gereği doğrulanamaz |
| Antitez-D | c | (satır127, EK-SORU-1) "84 yüksek lisans tezi (2017-2021, dergipark.org.tr)" | URL verilmemiş (yalnız domain adı, tıklanabilir link yok) | — | URL YOK | Rapor3'ün aynı iddiası (satır87) tam URL veriyordu (dergipark.org.tr/tr/pub/okufbed/article/1062622) — bu raporda link eksik bırakılmış |

**kesildi: hayır (toplam 15, ek yok — b15 zaten son sayısal iddia)**

**Rapor 4 özet:** TUTTU 15 (a dahil) · TUTMADI 0 · URL YOK 2 · ERİŞİLEMEDİ 0

---

## Genel Özet (4 rapor toplamı)

| Rapor | TUTTU | TUTMADI | URL YOK | ERİŞİLEMEDİ | Toplam sondaj |
|---|---|---|---|---|---|
| Tez-C | 10 | 2 | 5 | 0 | 17 |
| Antitez-C | 13 | 1 | 3 | 0 | 17 |
| Tez-D | 8 | 7 | 1 | 1 | 17 |
| Antitez-D | 15 | 0 | 2 | 0 | 17 |
| **Toplam** | **46** | **10** | **11** | **1** | **68** |

## TUTMADI ≥1 olan raporlar

- **Tez-C** (2): b4 Aristotle "5/6" sayısı kaynak özetinde yok · b15 "80× daha küçük" iddiası yanlış modele (32B yerine 8B) bağlanmış
- **Antitez-C** (1): b13 DeepSeek-Prover-V2 PutnamBench rakamı 47/658 yazılmış, kaynak 49/658 diyor (Tez-C'nin aynı iddiası — b14 — doğru vermişti)
- **Tez-D** (7, en yüksek oran): a Buzzard/Mathlib Initiative iddiası verilen URL'de yok · b3 FrontierMath "338/70+" verilen URL'de yok · b4 FrontierMath Tier4 "17/48" verilen URL Tier4'ü açıkça kapsam dışı bırakıyor · b6 Strachey Lecture iddiası iki verilen URL'de de yok · b10 YTÜ kılavuz tarihi (2024-05 vs kaynağın 2024-01 meta-tarihi) · b11 Cambridge/MPhil bilgisi arXiv özetinde yok (rapor zaten K işaretlemişti) · b14 ICLR 2025 bağlantısı kaynakta yok
- **Antitez-D** (0): TUTMADI çıkmadı

**Genel gözlem:** Tez-D (Aile D, meslek/format raporu) diğer üç rapora göre belirgin biçimde daha kırılgan (7/17 TUTMADI, %41) — çoğunlukla ikincil/websearch kaynaklı rakamların (FrontierMath Tier4, Buzzard/Strachey Lecture, ICLR bağlantısı) verilen URL'lerde doğrulanamamasından kaynaklanıyor. Antitez-D (kendi çürütme girişimlerinde curl+pdftotext gibi ek doğrulama adımları kullanmış) en sağlam çıktı (0 TUTMADI).
