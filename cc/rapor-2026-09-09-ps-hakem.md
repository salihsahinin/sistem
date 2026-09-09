# Hakem Raporu — P/Q Kıyası, 3 Aile (2026-09-09)

Bağımsız hakem koşumu. Girdi: 6 aile-dosyası (tez/antitez × 3) + 2 v26 örneklem-denetimi. Emrin yazarı/beklentisi bilinmiyor; yalnız ölçüm.

## Bağlayıcı dosya-kapağı (V26 kuralı: tutmadı>0 → dosya TÜMÜ ≤K)

| Dosya | v26 sonucu (tuttu/tutmadı/erişilemedi) | Kapak |
|---|---|---|
| P1 (tez-A1) | 2/1/1 | **≤K** — "WEF 2026 raporu yok" beyanı yanlış çıktı (rapor var, %44) |
| Q1 (antitez-A1) | 2/1/1 | **≤K** — Anthropic "enterprise %75/77/50" alıntısı bağımsız yeniden-açılışta sayfada bulunamadı |
| P2 (tez-A2) | 4/0/2 | kapak yok — bulgu bazlı D/K/X |
| Q2 (antitez-A2) | 4/0/0 | kapak yok — bulgu bazlı D/K/X |
| P3 (tez-A3) | 1/1/0 | **≤K** — BLS OR-analisti rakamı (%21/$91.290) güncel BLS döngüsüyle uyuşmuyor (vintage kayması) |
| Q3 (antitez-A3) | 4/0/0 | kapak yok — bulgu bazlı D/K/X |

---

## Aile 1 — İşgücü piyasası raporları (P1 ↔ Q1, ikisi de ≤K)

| Çift | Hüküm | Etiket | Kanıt / doğrulama |
|---|---|---|---|
| WEF çekirdek beceri sırası + "%39 2030'a dek eskir" | DARALDI — sıra listesi tutarlı ama yüzde tek-sürüm; WEF 2026 raporu aynı temayı %44 ile güncelliyor (P1 bunu kaçırmış) | K | blog.lewagon.com (özet metni doğrulandı); WEF 2026 raporu v26-tez tarafından bağımsız bulundu, P1'de yok |
| "Problem solving" ölçülebilir alt-beceri → müfredat girdisi | DARALDI — terim İK literatüründe "vague" olarak eleştiriliyor, standart ayrıştırma yok | K | kickresume.com (yalnız arama özeti, ham açılmadı) |
| Augmentation(%52)>automation(%45); 12x/9x hızlanma | SAĞLAM — çürütme denendi (kurumsal-API karşı-örneği), ama karşı-örneğin kendi alıntısı (%75/77/50) bağımsız yeniden-erişimde sayfada YOK | K (dosya kapağı) — içerik D-kalite | anthropic.com/research/economic-index-primitives; v26-tez VE v26-antitez ikisi de "augmentation 52/45" ve "12x/9x" ibarelerini birebir buldu; enterprise-split rakamı v26-antitez'in bağımsız yeniden-açılışında YOK |
| Junior/yüksek-AI-maruziyet istihdam düşüşü + "işveren rasyonel karar" | DARALDI — gözlemsel çekirdek (istihdam açığı %15→%19) iki ayrı bağımsız denetimde birebir doğrulandı; "rasyonel beceri-boşluğu" nedensel iddiası HBR ile çelişiyor | K (dosya kapağı) — içerik D-kalite | digitaleconomy.stanford.edu/news/canariesaug26/ — v26-tez VE v26-antitez ikisi de "15% Temmuz 2025 → 19% Haziran 2026" ibaresini birebir buldu |
| Karmaşık problem çözme üst-performansçı ayırır + çapraz-fonksiyon talebi ↑ | SAĞLAM — çürütme denenmiş, karşıt kanıt bulunamamış | K (dosya kapağı) — kaynak hiç ham açılmadı | lightcast.io (yalnız arama özeti, hiç WebFetch yok) |
| WEF/OECD/LinkedIn/Lightcast sıralamaları "temsilî, kariyer-kararına uygun" | DARALDI — WEF'in kendi sürüm-sürüm oranı (%35→%56→%57→%44) büyük varyans gösteriyor; bağımsız arama bu tarihsel rakamları doğruladı | K | WebSearch (WEF geçmiş raporları) — v26-antitez "35%/57%/44%" rakamlarını bağımsız doğruladı; %56/2018 teyit edilemedi |

**Aile 1 sayım:** SAĞLAM 2 · DARALDI 4 · DÜŞTÜ 0 · ÇELİŞKİLİ 0 (ayrı bayrak: Anthropic enterprise-split alıntısı aşağıda)

---

## Aile 2 — Akademik/deneysel kanıt (P2 ↔ Q2, kapak YOK — bulgu bazlı)

| Çift | Hüküm | Etiket | Kanıt / doğrulama |
|---|---|---|---|
| FrontierMath ilk yayında (2024-11) tüm modeller <%2 | SAĞLAM — çürütme denenmedi bile, bağımsız iki kez doğrulandı | **D** | arxiv.org/abs/2411.04872 — P2 PDF'i doğrudan okudu; v26-tez özet metninden "solve under 2% of problems" ibaresini bağımsız doğruladı |
| FrontierMath Tier 4 "hâlâ insan alanı" | DARALDI — Epoch'un resmî sayfasında Tier 4 performans verisi YOK (ne doğrular ne çürütür); yalnız Tier1-3 ekip ortalaması %19 var | D (veri-yokluğu için), K (genel iddia için) | epoch.ai/frontiermath/tiers-1-4/about — Q2 açtı, v26-antitez birebir doğruladı ("average team scored 19%... Tier 4 veri yok") |
| Gemini 3 Pro: Tier1-3 %37.6-38, Tier4 %18.8-19 | SAĞLAM — Epoch'un kendi hesabından birebir doğrulandı, "anakronizm riski" bayrağı asılsız çıktı (tarih tutarsızlığı bulunamadı) | **D** | Epoch AI X gönderisi — v26-tez "38% on Tiers 1-3 and 19% on Tier 4" ibaresini bağımsız doğruladı |
| GPT-6 Astra FrontierMath Tier4 %97.6 (BenchLM, üçüncül) | ÇELİŞKİLİ — üçüncül kaynakta rakam gerçekten var (bağımsız doğrulandı), ama Epoch'un resmî sayfasında bu sonuç yok; Tier1-3'ten (~%19, Kasım) Tier4'e (%97.6) sıçrama açıklanamıyor | X | benchlm.ai/... — v26-antitez "97.600%" rakamını bağımsız doğruladı (TUTTU, ama üçüncül); Epoch resmî sayfası bu sonucu içermiyor |
| IMO 2025: OpenAI kendi-değerlendirmesi (sertifikasız) vs DeepMind resmî IMO-onaylı altın | SAĞLAM — ayrım bağımsız aramada doğrulandı | **D** | WebSearch (OpenAI "not certified by IMO coordinators"; DeepMind "officially graded and certified") — v26-tez bağımsız doğruladı |
| METR: görev-ufku ~7 ayda ikileniyor | DARALDI — trend D-kalite doğrulandı, ama METR'in kendi notu ±2x hata payı ve "tüm görevler self-contained" sınırını KABUL ediyor (aylar-süren gerçek işbirliği görevleri veri setinde yok) | **D** (her iki taraf da) | metr.org/blog/2025-03-19 ("7 months") + metr.org/notes/2026-01-22-time-horizon-limitations ("factor of ~2", "self-contained") — ikisi de v26 tarafından birebir doğrulandı |
| Vaccaro meta-analiz: insan+AI ortalama < tek-başına-en-iyi (g=-0.23 vb.) | DARALDI — yön (karar-verme görevinde kayıp, içerik-üretiminde kazanç) arXiv özetinde teyitli; SAYISAL g-değerleri (-0.23/-0.27/+0.46/-0.54) özet metninde YOK, doğrulanamadı | K (yön) / X (sayı) | arxiv.org/abs/2405.06087 — v26-tez: "yönsel bulgu var... sayısal g-değerleri YOK" |
| Dell'Acqua (BCG 758 danışman): kapsam-içi +%12.2/+%25.1, kapsam-dışı -%19 doğruluk (aşırı-güvenme) | belirsiz — hiçbir tarafça ham metne erişilemedi | **X** | papers.ssrn.com — hem P2 hem sonraki denetim 403 aldı; hiç ham doğrulama yok |
| Automation-bias (tanı desteği, doğruluk %66.67→%57.14) — Dell'Acqua'yı dolaylı destekleyen kanıt | SAĞLAM (yön) ama zayıf — rakam doğrulandı, ancak "istatistiksel olarak anlamsız" uyarısı Q2 raporunda ATLANMIŞ | K | WebSearch — v26-antitez rakamı birebir doğruladı, "nonsignificant difference" notunu ekledi |
| AI-çıktısı doğrulama becerisi üzerine literatür "yok/az" | DÜŞTÜ — literatür var (PNAS Nexus, arXiv, PLOS One); ama bu karşı-kanıtın kendisi de tam-metin doğrulanamadı (reCAPTCHA/binari engelleri) | K | pmc.ncbi.nlm.nih.gov/PMC13248211 (kapalı), arxiv.org/2508.03714 (açıldı ama metin okunamadı), PLOS One (kapalı) — hiçbiri bağımsız v26 denetiminden geçmedi |
| Kariyer-değeri AI'nın zayıf olduğu alanlarda yoğunlaşmalı (T7) | açık/test edilmedi — bütçe tükendi, ne taraf da kanıt üretmedi | X | — |

**Aile 2 sayım:** SAĞLAM 4 (FrontierMath-launch, Gemini3, IMO, automation-bias-yön) · DARALDI 3 (Tier4-veri-yok, METR, Vaccaro) · DÜŞTÜ 1 (verification-literatürü-yok iddiası) · ÇELİŞKİLİ 1 (BenchLM %97.6) · açık 2 (Dell'Acqua, T7)

---

## Aile 3 — Matematik/kantitatif kariyer (P3 ↔ Q3, P3 ≤K kapaklı)

| Çift | Hüküm | Etiket | Kanıt / doğrulama |
|---|---|---|---|
| AI ikame değil çıta-yükseltici; kantitatif temel "pazarlık dışı" | DARALDI — Stanford verisi genel-meslek düzeyinde (yazılım/müşteri desteği), kantitatif rollere özgü kırılım YOK; PhD-quant talebi/ücreti arttığı yönünde dolaylı destek var | K | digitaleconomy.stanford.edu — v26-antitez doğruladı ama makale kantitatif rolleri adlandırmıyor |
| Stat/ML ilan talebi ~%92 sabit; A/B+nedensel-çıkarım en hızlı büyüyen | DARALDI — orijinal %92 rakamı hiçbir taramada yeniden bulunamadı (farklı ölçüm seti: ML %69-77, NLP %5→%19) | X | 365datascience.com (yalnız arama özeti) — orijinal Medium kaynağı 403, hiç doğrulanamadı |
| OR analisti istihdamı 2024-2034 ~%21 büyüme, medyan $91.290 | DARALDI — eski BLS döngüsüne ait, gerçek ama güncelliğini yitirmiş; v26-tez canlı sayfada %12/$88.940 buldu, v26-antitez WebSearch'te %21,5 buldu (**iki denetim arasında uyuşmazlık**, muhtemelen farklı BLS sayfası/vintage'i vurdular) | K | bls.gov/ooh/math/operations-research-analysts.htm — ÇELİŞKİLİ iki bağımsız denetim sonucu |
| Matematik meslekleri ulusal ortalamanın (%3) çok üstünde büyüyecek | SAĞLAM — çürütme denenmedi, bağımsız doğrulandı | K (dosya kapağı) — içerik D-kalite | bls.gov/ooh/math — v26-antitez "significantly higher than... 3 percent" ibaresini birebir doğruladı |
| MIT/CMU/Stanford proje/sözlü/portföy değerlendirmeye kayıyor, matematiğe özgü rehberlik YOK | SAĞLAM — çürütme denendi (matematik bölümlerinin ispat/temel-beceriyi güçlendirdiği karşıt kanıtı arandı, bulunamadı); ek destekleyici kanıt bulundu (Stanford Academic Integrity WG sözlü sınav önerisi) | K (dosya kapağı) — içerik D-kalite | aiandeducation.mit.edu/report/ — v26-tez tam metinden birebir doğruladı |
| AI-kişiselleştirilmiş öğrenme "genelde olumlu"; eleştirel-değerlendirme becerisi ihmal ediliyor | DARALDI (blanket-olumlu kısmı) / SAĞLAM (ihmal-kısmı) — Bastani vd. (PNAS, ~1000 lise öğrencisi): korumasız AI (GPT Base) pratikte +%48 ama SINAVDA -%17 (net ZARAR); yalnız öğretmen-tasarımlı GPT Tutor nötr (-0.004) | **D** | pmc.ncbi.nlm.nih.gov/PMC12232635 — v26-antitez dört rakamın (48%, -17%, -0.004, ~1000 öğrenci) tamamını birebir doğruladı |
| En yüksek kariyer-getirisi: matematik temeli+kod+nedensel-çıkarım+AI-doğrulama (T7) | açık/test edilmedi — bütçe tükendi | X | — |

**Aile 3 sayım:** SAĞLAM 2 (BLS-ortalama-üstü, MIT-değerlendirme) · DARALDI 4 (AI-çıta, stat-%92, OR-%21, AI-öğrenme-blanket) · DÜŞTÜ 0 · ÇELİŞKİLİ 1 (OR-analisti BLS rakamı, iki denetim arası) · açık 1 (T7)

---

## Hayatta-kalan çekirdek (aile-bağımsız, D/K etiketli, en fazla 10)

1. **D** — Anthropic Economic Index: Claude.ai (tüketici) trafiğinde augmentation (%52) Kasım 2025'te automation'ı (%45) geçti — iki bağımsız denetimde birebir doğrulandı; kurumsal-API tarafına genellenemez (o rakamlar kaynakta yok).
2. **D** — Anthropic Economic Index: lisans-düzeyi görevlerde ~12x, lise-düzeyi görevlerde ~9x hızlanma faktörü.
3. **D** — FrontierMath ilk yayında (2024-11) tüm modeller problemlerin <%2'sini çözebildi.
4. **D** — Epoch AI'nin resmî sayfasında FrontierMath Tier 4 için HİÇBİR model performans verisi yayımlanmamış (yalnız Tier1-3 ekip ortalaması %19).
5. **D** — Gemini 3 Pro (Epoch'un kendi açıklaması): Tier1-3 %38, Tier4 %19.
6. **D** — IMO 2025: OpenAI'nin 35/42 sonucu IMO koordinatörlerince sertifikalanmadı; Google DeepMind'ın Gemini Deep Think sonucu resmî sertifikalandı.
7. **D** — METR: ölçülen görev-uzunluğu ufku ~7 ayda bir ikileniyor, ANCAK METR'in kendisi ±2x hata payı kabul ediyor ve ölçülen tüm görevler "self-contained" (gerçek aylar-süren işbirlikli görevler veri setinde yok).
8. **D** — Stanford Digital Economy Lab: 22-25 yaş, yüksek-AI-maruziyetli mesleklerde istihdam açığı %15 (Temmuz 2025) → %19 (Haziran 2026) büyüdü.
9. **D** — PNAS/Bastani (~1000 lise öğrencisi): korumasız AI kullanımı (GPT Base) sınav performansını %17 DÜŞÜRDÜ; yalnız öğretmen-tasarımlı, cevap-gizleyen tutor nötr etkiliydi.
10. **D** — BLS: matematik meslekleri 2034'e dek ulusal ortalamanın (%3) çok üstünde büyüyecek.

## Düşen / Daralan iddialar

- WEF "%39 2030'a dek eskir" — DARALDI, WEF 2026 raporu aynı temayı %44 ile güncelliyor, P1 bunu kaçırmış.
- "Augmentation automation'ı geçti" genellemesi — DARALDI, yalnız tüketici segmenti; kurumsal-API %75/77/50 rakamı bağımsız yeniden-erişimde kaynakta YOK (aşağıda ayrıca çelişkili işaretli).
- OR analisti %21/$91.290 — DARALDI, BLS vintage kayması (iki denetim farklı güncel rakam buldu).
- "Problem solving" net ölçülebilir alt-beceri seti → müfredat girdisi — DARALDI, terim İK literatüründe "vague" eleştirisi alıyor.
- Stat/ML ilan talebi ~%92 sabit; A/B+nedensel-çıkarım "en hızlı büyüyen" — DARALDI, orijinal rakam hiçbir bağımsız taramada yeniden üretilemedi.
- "AI-kişiselleştirilmiş öğrenme genelde olumlu" (blanket) — DARALDI/kısmen DÜŞTÜ, korumasız kullanımda net negatif (Bastani -%17).
- "AI çıktısı doğrulama üzerine literatür yok/az" — DÜŞTÜ, literatür var (ama karşıt kanıtın kendisi de tam doğrulanamadı).
- Vaccaro g-değerleri (-0.23/-0.27/+0.46/-0.54) — sayısal olarak DÜŞTÜ (ham metinde yok), yön K kalitesinde ayakta.
- Dell'Acqua (%12.2/%25.1/-%19) — hiç doğrulanamadı, açık kaldı.

## Çelişkili

- **Anthropic enterprise-API automation %75/%77/%50:** İki ayrı antitez ajanı (Q1-T3 bağlamında) bu rakamı `anthropic.com/research/economic-index-primitives` sayfasından "birebir açıldı" diyerek aktardı; v26-antitez AYNI URL'yi bağımsız yeniden açtığında bu rakamlar sayfada YOK. Çözülmedi — ya yanlış sayfa/sürüm alıntılanmış ya da özetleme aracı atlamış.
- **GPT-6 Astra FrontierMath Tier4 %97.6 (BenchLM):** Üçüncül kaynakta gerçekten var (bağımsız doğrulandı) ama Epoch'un resmî sayfası bu sonucu içermiyor; Tier1-3'ten (~%19, birkaç ay önce) Tier4'e böylesi bir sıçrama açıklanamadı. Çözülmedi.
- **BLS OR-analisti güncel rakamı:** v26-tez canlı sayfada %12/$88.940 buldu, v26-antitez WebSearch'te %21,5 buldu (eski rakamla örtüşen). İki bağımsız denetim aynı kurumun aynı meslek sayfası için farklı "güncel" rakam raporladı — hangisinin gerçekten canlı/güncel olduğu bu koşumda çözülmedi.

## Hayatta-kalma sayımı (3 aile toplamı)

| Durum | Sayı |
|---|---|
| SAĞLAM | 8 |
| DARALDI | 12 |
| DÜŞTÜ | 1 (+ birkaç sayısal alt-bileşen düştü) |
| ÇELİŞKİLİ | 1 pair-düzeyinde net (+ 3 ayrı çelişkili-alıntı bayrağı, yukarıda) |
| Açık/test edilmedi | 4 |
