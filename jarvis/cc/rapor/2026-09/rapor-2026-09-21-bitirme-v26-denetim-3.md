# V26 Örneklem-Denetimi (3) — Aile E + Aile F (tez/antitez)

**Denetleyen:** Atlas (V26 örneklem-denetim ajanı, kural-tabanlı) · **AS-OF:** 2026-09-21 · **Yöntem:** WebFetch (bütçe sınırı nedeniyle WebSearch kullanılmadı) · **Kural:** atlas-kosum adım 5, sabit sondaj seçimi (a) son üçte birden ≥1 URL'li iddia · (b) tüm sayısal iddialar (≤15, aşarsa "kesildi: N/M") · (c) son üçlükten ≥1 URL'siz iddia

**Etiket anahtarı:** TUTTU = kaynakta birebir/aynı anlamda doğrulandı · TUTMADI = kaynakta bulunamadı/çelişiyor (fark açıklanır) · URL YOK = iddiaya bağlı URL yok · ERİŞİLEMEDİ = URL'ye ulaşılamadı (403/404/429/binary vb.)

---

## 1. Ajan/rapor: tez-E (kuresel-universite)

| Ajan/rapor | Sondaj türü | Denetlenen iddia | URL | Kaynak kanıtı (≤15 kelime, bölüm) | Sonuç | Not |
|---|---|---|---|---|---|---|
| tez-E | a | "Açılan kaynaklar" #7: arXiv 2602.12891 journal-ref alanında "ISTA Ph.D. Thesis (2026)" yazıyor, PhD tezi | https://arxiv.org/abs/2602.12891 | "ISTA Ph.D. Thesis (2026); ISSN: 2663-337X" — journal reference alanı | TUTTU | Yazar Martin Dvorak, 2026 de teyit |
| tez-E | b1 | Princeton Math senior thesis: tipik 20-40 sayfa | math.princeton.edu/undergraduate/majors/independent-work | "About 20-40 pages when single-spaced seems typical" | TUTTU | |
| tez-E | b2 | Princeton: bazı tezler <10, bazıları 100+ sayfa | aynı URL | "some... under 10 pages, while others have been over 100 pages" | TUTTU | |
| tez-E | b3 | Cambridge Part III: 5.000-8.000 kelime "mükemmel" için | maths.cam.ac.uk/postgrad/part-iii/current/examinations-and-essays | "excellent essay requires about 5000 words... more than about 8000 words" | TUTTU | |
| tez-E | b4 | Cambridge: 20-30 sayfa, istisnaen 35'e kadar | aynı URL | "between 20 and 30 pages... only exceptionally more than 35 pages" | TUTTU | |
| tez-E | b5 | Oxford Part C, matematik programının 4. yılı | maths.ox.ac.uk/.../dissertations | Sayfada "fourth year" ifadesi yok, yıl belirtilmemiş | TUTMADI | Fark: sayfa Part C'yi hangi yıla denk geldiğini söylemiyor |
| tez-E | b6 | Oxford: 7.500 kelime sınırı | aynı URL | "a written dissertation with a word limit of 7,500 words" | TUTTU | |
| tez-E | b7 | Oxford: tipik 25-35 sayfa | aynı URL | "which usually equates to 25-35 pages" | TUTTU | |
| tez-E | b8 | Stanford Honors Thesis başvurusu 1 Mayıs son tarih | cs.stanford.edu/bs-requirements-senior-project | "Applications for the honors program are due by May 1st" | TUTTU | |
| tez-E | b9 | Stanford Senior Project: 5 farklı yol | aynı URL | 5 seçenek listelendi: CS194/W, CS210B, CS191/W, Honors Thesis, CS294 | TUTTU | |
| tez-E | b10 | Stanford GPA ≥2.0 şartı | aynı URL | "2.0 minimum grade point average... is required" | TUTTU | |
| tez-E | b11 | CMU Honors Thesis: 2 dönem, 36 kredi birimi | cs.cmu.edu/research/undergraduate-research/honors-thesis-history | Sayfada bu rakamlar yok, yalnız Undergraduate Catalog'a yönlendirme var | TUTMADI | Fark: verilen URL'de rakamlar bulunamadı |
| tez-E | b12 | CMU: prospectus ≤3 sayfa | aynı URL | Sayfada bu bilgi yok | TUTMADI | Aynı URL, aynı eksiklik |
| tez-E | b13 | Harvard: Leonard Tang 2024 Bachelor's Thesis | dash.harvard.edu/items/1639db4a-... | "Bachelors Thesis, Harvard University... " (2024) | TUTTU | |
| tez-E | b14 | Imperial "Formalising Mathematics" 2024, son-sınıf lisans hedefli | ma.imperial.ac.uk/~buzzard/xena/formalising-mathematics-2024 | "final year of an undergraduate mathematics degree" | TUTTU | "MSc" kelimesi sayfada yok (raporun kendi K notuyla tutarlı) |
| tez-E | b15 | arXiv 2602.12891: 2026 PhD tezi (bkz. b/a) | arxiv.org/abs/2602.12891 | (a) ile aynı kanıt | TUTTU | Sondaj (a) ile aynı kaynak, ayrı madde olarak zorunlu |
| tez-E | c | Sentez: Princeton "orijinal bakış açısı" + Cambridge β- "final-year project quality" küçük-kapsam normunu gösteriyor | math.princeton.edu (Princeton) + maths.cam.ac.uk (Cambridge) | Princeton: "original point of view or individual mathematical style"; Cambridge β-: "quality expected of an upper-second-class final-year project" | TUTTU | İki ayrı kaynağın sentezi, ikisi de doğrulandı |

**Kesildi: 15/26** (tam sayısal iddia dökümü ~26; ilk 15 sırayla alındı — geri kalanlar: arXiv 2603.24372 yılı, "üst-13 kurum", 2020 UROP, "8 adet" başlık vs 9 liste maddesi çelişkisi, "9 başarılı fetch", 403/404/231 KB hata kodları, 2023-2026 tarih aralığı).

**Rapor başına özet:** TUTTU 14 / TUTMADI 3 / URL YOK 0 / ERİŞİLEMEDİ 0 (toplam 17 sondaj)

---

## 2. Ajan/rapor: antitez-E

| Ajan/rapor | Sondaj türü | Denetlenen iddia | URL | Kaynak kanıtı (≤15 kelime, bölüm) | Sonuç | Not |
|---|---|---|---|---|---|---|
| antitez-E | a | TUM (SCML) 2024: "Solving the three-body problem with neural networks", Andreas Merrath, "Bachelor thesis" etiketli | cs.cit.tum.de/en/scml/teaching/student-projects/ | "Andreas Merrath: Solving the three-body problem... Bachelor thesis, 2024" | TUTTU | |
| antitez-E | b1 | E1: Princeton 20-40 sayfa | math.princeton.edu/... | (bkz. tez-E b1) | TUTTU | Tekrar doğrulama |
| antitez-E | b2 | E1: <10 / 100+ sayfa uçları | aynı URL | (bkz. tez-E b2) | TUTTU | |
| antitez-E | b3 | E2: Cambridge 20-30, istisnaen 35 sayfa | maths.cam.ac.uk/... | (bkz. tez-E b4) | TUTTU | |
| antitez-E | b4 | E2: 5.000-8.000 kelime | aynı URL | (bkz. tez-E b3) | TUTTU | |
| antitez-E | b5 | E3: Oxford 7.500 kelime, 25-35 sayfa | maths.ox.ac.uk/... | (bkz. tez-E b6/b7) | TUTTU | |
| antitez-E | b6 | E3: 50 sayfa mutlak tavan (tez-E'de yok, antitez'in eklediği yeni bilgi) | aynı URL | "There is also an absolute page limit of 50 pages" | TUTTU | tez-E bu bilgiyi hiç vermemiş, antitez'in katkısı doğru |
| antitez-E | b7 | E5: Stanford tam 5 seçenek | cs.stanford.edu/... | 5 seçenek birebir sayıldı | TUTTU | |
| antitez-E | b8 | E6: Imperial kursu Ocak-Mart 2024'te koştu | github.com/ImperialCollegeLondon/formalising-mathematics-2024 | "The course ran from January to March 2024" | TUTTU | |
| antitez-E | b9 | E8: Harvard/Tang 2024 Bachelor's Thesis | dash.harvard.edu/items/1639db4a-... | (bkz. tez-E b13) | TUTTU | |
| antitez-E | b10 | E11: Harvard DASH "senior thesis"+"autoformalization" araması sıfır sonuç | dash.harvard.edu/search?query=... | "Your search returned no results" | TUTTU | Yalnız bu sorgu test edildi; "physics-informed" sorgusu ayrıca test edilmedi |
| antitez-E | b11 | E11: Princeton DataSpace 401 Unauthorized | dataspace.princeton.edu | HTTP 401 Unauthorized döndü | TUTTU | |
| antitez-E | b12 | E11: MIT DSpace 404 | math.mit.edu/academics/undergrad/uthesis.php | HTTP 404 Not Found döndü | TUTTU | |
| antitez-E | b13 | E11: ETH Research Collection 429 | research-collection.ethz.ch/server/api/core/bitstreams/4deec035-.../content | HTTP 429 Too Many Requests döndü | TUTTU | |
| antitez-E | b14 | E12: ETH Bachelor Math müfredatı 3. yılda "Bachelor's thesis" bileşeni | ethz.ch/en/studies/bachelor/.../mathematics.html | "Seminars, Bachelor's thesis" (3. yıl bölümünde) | TUTTU | |
| antitez-E | b15 | E12: EPFL MATH-397 zorunlu, 14 hafta×12 saat, 12 kredi | edu.epfl.ch/coursebook/en/mathematics-project-bachelor-MATH-397 | "Type: mandatory"; "12 Hour(s) per week x 14 weeks"; "12 credits" | TUTTU | "5. ve 6. dönem" ifadesi ayrıca teyit edilmedi, yalnız "her iki dönemde zorunlu" doğrulandı |
| antitez-E | c | "Diğer sekiz kurumda (MIT, Princeton, Cambridge, Oxford, Stanford, Berkeley, Caltech, CMU, Imperial, EPFL) doğrulanmış örnek bulunamadı" | (URL yok — dahili sayım) | Parantezde 10 kurum adı sayılı, metin "sekiz" diyor | TUTMADI | Dahili tutarsızlık: 10 kurum listelenmiş, "sekiz" değil |

**Kesildi: 15/23** (tam sayısal iddia dökümü ~23; geri kalanlar: TUM 2025/2026 yılları — zaten (a)'da doğrulandı —, "≥8 hedef, 5/8+1 bayraklı", "20+ URL, ~14 başarılı ~8 hata: 401×2/404×3/429×2/302×1").

**Rapor başına özet:** TUTTU 16 / TUTMADI 1 / URL YOK 0 / ERİŞİLEMEDİ 0 (toplam 17 sondaj)

---

## 3. Ajan/rapor: tez-F (rol-evrimi)

| Ajan/rapor | Sondaj türü | Denetlenen iddia | URL | Kaynak kanıtı (≤15 kelime, bölüm) | Sonuç | Not |
|---|---|---|---|---|---|---|
| tez-F | a | "Açılan kaynaklar" #1: O*NET Mathematicians görev listesi | onetonline.org/link/summary/15-2021.00 | 12 görev listelendi, "AI"/"artificial intelligence" ifadesi yok | TUTTU | |
| tez-F | b1 | O*NET: 12 görev listelendi | aynı URL | (a) ile aynı kanıt | TUTTU | |
| tez-F | b2 | Eloundou: ~%80 işgücü, görevlerin en az %10'u etkilenebilir | arxiv.org/abs/2303.10130 | "around 80% of the U.S. workforce could have at least 10%..." | TUTTU | |
| tez-F | b3 | Eloundou: ~%19'u, görevlerin en az %50'si etkilenebilir | aynı URL | "approximately 19% of workers may see at least 50%..." | TUTTU | |
| tez-F | b4 | Anthropic EI: "Computer and Mathematical" ~%30 anket payı | anthropic.com/research/economic-index-june-2026-report | "roughly 30% of survey respondents" | TUTTU | |
| tez-F | b5 | Anthropic EI: ABD istihdamının %4'ü | aynı URL | "far above their 4% share of US employment" | TUTTU | |
| tez-F | b6 | Anthropic EI raporu Haziran 2026 / 2026-06-26 | aynı URL | "Jun 26, 2026"; "date = {2026-06-26}" | TUTTU | |
| tez-F | b7 | Microsoft: 200.000 Bing Copilot konuşması | microsoft.com/en-us/research/publication/working-with-ai-... | "a dataset of 200k anonymized... conversations... Bing Copilot" | TUTTU | |
| tez-F | b8 | Microsoft: konuşmaların %40'ında hedef-eylem uyuşmazlığı | aynı URL | Sayfa içeriğinde bu yüzdeye dair bilgi yok | TUTMADI | Fark: alınan sayfada rakam yok (rapor zaten bunu K/WebSearch-özeti olarak işaretlemişti) |
| tez-F | b9 | Tao ICM 2026 makalesi + 2026-07-24 halka açık konuşma | arxiv.org/abs/2608.16753 | Gönderim 17 Ağustos 2026; "based on a public lecture... ICM 2026" — spesifik tarih yok | TUTMADI | Fark: 2026-07-24 tarihi kaynakta doğrulanamadı |
| tez-F | b10 | Fields deklarasyonu: 2026-09-16 itibarıyla 7.200+ imzacı | terrytao.wordpress.com/.../a-severe-misalignment-of-ai-in-mathematics/ (birincil) + cryptobriefing.com/fields-medal-winners-ai-mathematics-misalignment/ (ikincil, raporun kendi kaynağı) | Birincil: yalnız "25 initial signatories"; ikincil kaynakta da "7.200+" rakamı **yok**, yalnız "Twenty-five Fields Medal winners" | TUTMADI | Rapor bunu zaten K etiketlemişti ama verdiği ikincil kaynakta da rakam doğrulanamadı — kaynak hatalı gösterilmiş olabilir |
| tez-F | b11 | Fields deklarasyonu 2026-09-11 tarihli | terrytao.wordpress.com/2026/09/11/... | URL'nin kendisi ve sayfa tarihi 11 Eylül 2026 | TUTTU | |
| tez-F | b12 | OpenAI duyurusundan "3 gün sonra" deklarasyon yayımlandı | technologyreview.com (2026-09-08) + terrytao.wordpress.com (2026-09-11) | MIT Tech Review 2026-09-08, deklarasyon 2026-09-11 → 3 gün fark | TUTTU | İki tarihin çıkarımı |
| tez-F | b13 | OpenAI Navier-Stokes: 10.000 eşzamanlı ajan, milyonlarca dolar | technologyreview.com/2026/09/08/1143747/... | "running about 10,000 agents concurrently, at a cost of millions of dollars" | TUTTU | |
| tez-F | b14 | Buckmaster/Alpöge ~1 yılda halka açık modellerle | aynı URL | "worked on the problem for almost a year, using publicly available models" | TUTTU | |
| tez-F | b15 | Alignerr Lean 4 Proof Engineer: $170-200/saat | alignerr.com/jobs/d61fdffd-b1a1-4cf7-9eae-6c0e3d39df83 | "$170-200/hr" | TUTTU | |
| tez-F | c | "10.000-ajan koordinasyonu" yetkinliği yalnız MIT Tech Review'in tek ikincil haberinden (K); doğrudan "bu artık matematikçinin işi" beyanı bulunamadı | technologyreview.com/2026/09/08/1143747/... | 10.000 ajan + maliyet teyit edildi; "bu artık matematikçinin işi" tarzı açık beyan bulunamadı | TUTTU | |

**Kesildi: 15/31** (tam sayısal iddia dökümü ~31; geri kalanlar: Math Inc ~200K satır/2022/8-24 boyut, Anthropic Aralık-2025 sayıları (132/53/3.2→3.8/%116/%33), METR 2025 (%19/%20/16 dev), Rol adları tablosundaki tekrarlanan AS-OF tarihleri).

**Rapor başına özet:** TUTTU 14 / TUTMADI 3 / URL YOK 0 / ERİŞİLEMEDİ 0 (toplam 17 sondaj)

---

## 4. Ajan/rapor: antitez-F

| Ajan/rapor | Sondaj türü | Denetlenen iddia | URL | Kaynak kanıtı (≤15 kelime, bölüm) | Sonuç | Not |
|---|---|---|---|---|---|---|
| antitez-F | a | METR 2026-02-24 takip yazısı, orijinal başlık "We are Changing our Developer Productivity Experiment Design" | metr.org/blog/2026-02-24-uplift-update/ | Başlık ve tarih birebir eşleşti; "unreliable signal" ifadesi de var | TUTTU | |
| antitez-F | b1 | Başlık: "20 deneme, 17 başarılı, 3 başarısız" | (URL yok — dahili sayım, Kaynak Listesi 1-20) | Listede 4 madde "BAŞARISIZ" (#6,15,16,20) — 16 başarılı, 4 başarısız | TUTMADI | Dahili tutarsızlık: rapor 17/3 diyor, kendi listesi 16/4 gösteriyor |
| antitez-F | b2 | F1: O*NET 12 görev | onetonline.org/link/summary/15-2021.00 | (bkz. tez-F b1) | TUTTU | |
| antitez-F | b3 | F1: O*NET görev verisi 2025'te güncellendi | onetonline.org/link/updates/15-2021.00 | "Tasks: Occupational Expert (2025)" | TUTTU | |
| antitez-F | b4 | F2: Eloundou ~%80/%10 | arxiv.org/abs/2303.10130 | (bkz. tez-F b2) | TUTTU | |
| antitez-F | b5 | F2: Eloundou ~%19/%50 | aynı URL | (bkz. tez-F b3) | TUTTU | |
| antitez-F | b6 | F2: makale Mart 2023 tarihli | aynı URL | "[Submitted on 17 Mar 2023]" | TUTTU | |
| antitez-F | b7 | F5: 25 Fields Madalyalısı imzacı | terrytao.wordpress.com/2026/09/11/... | "Twenty-five Fields Medal winners" | TUTTU | |
| antitez-F | b8 | F5: deklarasyon 2026-09-11 tarihli | aynı URL | Yayım tarihi 11 Eylül 2026 | TUTTU | |
| antitez-F | b9 | F6: Buzzard, üç karşı-örnek, iki ayda (Erdős 20 Mayıs, Grothendieck 11 Tem, Jacobian 20 Tem) | xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/ | Üç örnek + tarihler teyit edildi, 20 Mayıs–20 Temmuz = tam 2 ay | TUTTU | |
| antitez-F | b10 | F6: Grothendieck sorusu "60 yıllık" | aynı URL | "60 yıllık soru" | TUTTU | |
| antitez-F | b11 | F6: Jacobian konjektürü "100 yıllık" | aynı URL | "100 yıllık" bir problem | TUTTU | |
| antitez-F | b12 | F8: Anthropic raporu 2 Aralık 2025 (Dec 2, 2025) | anthropic.com/research/how-ai-is-transforming-work-at-anthropic | Başlıkta "Dec 2, 2025" | TUTTU | |
| antitez-F | b13 | F8: ölçüm dönemi Şubat-Ağustos 2025 | aynı URL | "200,000 internal transcripts from Claude Code from February and August 2025" | TUTTU | |
| antitez-F | b14 | F8: 132 mühendis/araştırmacı anketi | aynı URL | "we surveyed 132 Anthropic engineers and researchers" | TUTTU | |
| antitez-F | b15 | F8: 200.000 Claude Code transkripti | aynı URL | "analyze 200,000 internal transcripts from Claude Code" | TUTTU | |
| antitez-F | c | "11 iddiadan 9'u ÇÜRÜTÜLEMEDİ, 2'si DARALDI, hiçbiri ÇÜRÜDÜ statüsüne düşmedi" | (URL yok — dahili sayım, F1-F11 sonuç etiketleri) | Sayım: F1,F3,F4,F5,F7,F8,F9,F10,F11 = 9 ÇÜRÜTÜLEMEDİ; F2,F6 = 2 DARALDI | TUTTU | Dahili tutarlılık doğrulandı |

**Kesildi: 15/29** (tam sayısal iddia dökümü ~29; geri kalanlar: Anthropic 3.2→3.8/%116/%33, METR 2025 %19/%20/16 dev/246 görev, OpenAI 10.000 ajan/2.7M mesaj/130B token/88 saat, METR-2026 -18%/-4%/CI aralıkları/%30-50 seçilim yanlılığı).

**Rapor başına özet:** TUTTU 16 / TUTMADI 1 / URL YOK 0 / ERİŞİLEMEDİ 0 (toplam 17 sondaj)

---

## Genel Özet (4 rapor, 68 sondaj)

| Rapor | TUTTU | TUTMADI | URL YOK | ERİŞİLEMEDİ | Toplam |
|---|---|---|---|---|---|
| tez-E | 14 | 3 | 0 | 0 | 17 |
| antitez-E | 16 | 1 | 0 | 0 | 17 |
| tez-F | 14 | 3 | 0 | 0 | 17 |
| antitez-F | 16 | 1 | 0 | 0 | 17 |
| **Toplam** | **60** | **8** | **0** | **0** | **68** |

## TUTMADI ≥1 olan raporlar

Dördü de en az bir TUTMADI içeriyor: **tez-E, antitez-E, tez-F, antitez-F**.

### TUTMADI listesi (8 madde)

1. **tez-E b5** — Oxford Part C "4. yıl" ifadesi verilen URL'de yok.
2. **tez-E b11** — CMU "2 dönem, 36 kredi birimi" verilen URL'de yok.
3. **tez-E b12** — CMU prospectus "≤3 sayfa" verilen URL'de yok.
4. **antitez-E c** — "Diğer sekiz kurumda" derken parantezde 10 kurum adı sayılmış (dahili tutarsızlık).
5. **tez-F b8** — Microsoft "Working with AI" sayfasında %40 rakamı yok.
6. **tez-F b9** — Tao'nun arXiv özetinde "2026-07-24" tarihi doğrulanamadı (yalnız "ICM 2026'da verilen bir konuşmaya dayanıyor" deniyor).
7. **tez-F b10** — Fields deklarasyonu "7.200+ imzacı" rakamı ne birincil (terrytao.wordpress.com) ne de raporun verdiği ikincil kaynakta (cryptobriefing.com) bulundu.
8. **antitez-F b1** — Raporun kendi başlığı "20 deneme, 17 başarılı, 3 başarısız" diyor ama kendi Kaynak Listesi'nde 4 madde "BAŞARISIZ" işaretli (16 başarılı/4 başarısız).

**Not:** TUTMADI oranı 8/68 (%12); hiçbiri "ERİŞİLEMEDİ" ya da "URL YOK" değil — tüm sondajlar tamamlanabildi. En sistematik hata türü: bir kurumun genel sayfasına atıfla verilen ayrıntı rakamının o spesifik sayfada bulunmaması (tez-E CMU, tez-F Microsoft) ve dahili sayım tutarsızlıkları (antitez-E, antitez-F).
