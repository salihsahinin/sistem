# V26 Örneklem-Denetimi — ps-antitez A1/A2/A3 (2026-09-09)

Bağımsız denetçi raporu. Yazar/beklenti bilgisi verilmedi. Kural: (a) son 1/3'ten ≥1 URL'li iddia, (b) tüm sayısal iddialar, (c) son 1/3'ten ≥1 URL'siz/model-hafızası iddia. Araç çağrısı kullanımı: 10/14 (9 WebFetch/WebSearch + 1 curl indirme, BLS engellendi → yedek WebSearch).

## Tablo

| Dosya | İddia | Kural | Kaynak | Sonuç | Not |
|---|---|---|---|---|---|
| A1 | T1: WEF beceri-bozulma oranı 2016 %35, 2020 %57, 2023 %44 | b | WebSearch (WEF raporları) | **TUTTU** | Bağımsız arama 35%(2016)/57%(2020)/44%(2023) rakamlarını doğrudan doğruladı; 2025 raporunun 39% (44'ten düşüş) bilgisiyle de tutarlı — büyük sürüm-sürüm sıçrama teması ayakta |
| A1 | T1: 2018 rakamı %56 | b | WebSearch (WEF raporları) | **ERİŞİLEMEDİ** | Arama sonucu 2018 için özel olarak "56%" rakamını doğrulayamadı ("didn't find a specific reference to a 56% figure for 2018"); yanlış değil, teyit edilemedi |
| A1 | T3: Anthropic — enterprise API automation %75/%77, consumer %50 | b | anthropic.com/research/economic-index-primitives (WebFetch, birebir) | **TUTMADI** | Aynı URL'yi bağımsız açtım: sayfada yalnızca consumer (Claude.ai) için "augmentation (52%) has overtaken automation (45%)" var; enterprise API'ye dair %75/%77/%50 rakamı sayfada BULUNAMADI. A1'in "birebir açıldı" dediği alıntı bu sayfada doğrulanamadı — ya yanlış sayfa/sürüm alıntılanmış ya da özetleme aracı bir bölümü atlamış olabilir; ayrım net değil ama mevcut ham metinde rakamlar yok |
| A1 | T4: Stanford 22-25 yaş istihdam açığı %19 (2026-06), önceki %15 (2025-07) | a+b (son 1/3'e yakın referans, T4 satırı) | digitaleconomy.stanford.edu/news/canariesaug26/ (WebFetch) | **TUTTU** | Ham metin birebir: "shortfall was 15% at the July 2025 data vintage and is 19% as of June 2026" — tam eşleşme |
| A1 | (c) son 1/3 (Yöntem notu, satır 16-22): "hiçbir iddia tam çürüdü seviyesine ulaşmadı" | c | — (meta-değerlendirme, olgu iddiası değil) | **N/A** | Son üçte birde (satır 15-22) ayrı bir URL'li/URL'siz olgusal iddia yok, yalnız özet/meta metin; kurala tam uyan aday bulunamadı — en yakın olgusal iddia (T4, satır 12) yukarıda test edildi |

| A2 | T3: automation bias — doğruluk %66.67 (AI'sız) → %57.14 (AI aktif) | b | WebSearch (Pediatric Autism ADIS çalışması) | **TUTTU** | Arama sonucu birebir: "57.14% when ADIS active versus 66.67% without ADIS" — ancak arama sonucu ayrıca "nonsignificant difference" notu ekliyor; A2 raporu bu istatistiksel anlamsızlık uyarısını atlamış — rakam doğru, güç/anlamlılık bağlamı eksik aktarılmış |
| A2 | T4: Epoch AI — MIT öğrenci takım ortalaması %19, Tier 4 için veri yok | a+b | epoch.ai/frontiermath/tiers-1-4/about (WebFetch, birincil) | **TUTTU** | Ham metin: "the average team scored 19%, while 35% of the problems were solved collectively"; Tier 4 için performans verisi sayfada yok — A2'nin iki iddiası da doğrulandı |
| A2 | T4 (son 1/3, satır 23): "GPT-6 Astra FrontierMath Tier 4 %97.6" (BenchLM, 2026-09-03) | a (son 1/3) + b | WebSearch (BenchLM + üçüncül basın) | **TUTTU (var, ama üçüncül)** | BenchLM.ai leaderboard'da (Eylül 2026) gerçekten "97.600%" rakamı var, cryptobriefing.com da aynı sayıyı bağımsız aktarıyor. A2'nin bayrağı (Epoch AI'nin RESMİ sayfasında bu sonuç yok, doğrulanmamış üçüncül-kaynak) doğru ve kanıtla teyit edildi — anakronizm riski değil ama kaynak-güvenilirliği riski gerçek |
| A2 | T5: METR hata payı "~2 kat her yönde", "3.5h mi 6.5h mi bilmiyoruz", görevler self-contained | a+b | metr.org/notes/2026-01-22-time-horizon-limitations/ (WebFetch, birincil) | **TUTTU** | Üç alıntı da ham metinde birebir bulundu: "factor of ~2 in each direction", "whether Claude's 'true' time horizon is 3.5h or 6.5h", "all of the tasks in METR-HRS are self-contained" |

| A3 | T1: Stanford istihdam açığı %19/%15 (aynı olgu, A1-T4 ile ortak) | a+b | digitaleconomy.stanford.edu/news/canariesaug26/ (WebFetch) | **TUTTU** | Bkz. A1-T4 satırı — aynı doğrulama geçerli |
| A3 | T3: BLS OR analisti istihdamı 2024-2034 ~%21-22 büyüme | b | WebSearch (BLS OOH, doğrudan sayfa 403 ile engellendi → arama özeti) | **TUTTU** | Bağımsız arama BLS'in resmî rakamının **%21,5** olduğunu buldu — T3'ün "~%21" iddiasına neredeyse birebir; A3'ün kendi bulduğu "22%" de aynı rakamın yuvarlanmışı, çelişki yok |
| A3 | T4: matematik meslekleri "ulusal ortalamanın çok üstünde" büyüyecek, ortalama %3 | b | WebSearch (BLS OOH özeti) | **TUTTU** | "significantly higher than the average for all occupations, which is 3 percent" — ortalama %3 rakamı ve "çok üstünde büyüme" ifadesi doğrudan doğrulandı |
| A3 | T6 (son 1/3, satır 20): PMC/Bastani — GPT Base pratikte +%48, sınavda −%17; GPT Tutor −0.004; ~1000 öğrenci | a+b | pmc.ncbi.nlm.nih.gov/articles/PMC12232635/ (WebFetch, birincil) | **TUTTU (tam)** | Ham metin birebir: "GPT Base and GPT Tutor would increase performance... by 48% and 127%"; "17% reduction in grades for GPT Base"; "smaller by an order of magnitude (−0.004)"; "nearly a thousand high school math students" — dört rakam da tam eşleşti |

## Dosya Başına Özet

**A1** — sondaj 4 (T1×2, T3, T4); tuttu/tutmadı/erişilemedi = 2/1/1. **Tutmadı > 0 → A1'in tüm bulguları K'ya düşer.** En kritik sorun: T3'ün "Anthropic sayfası birebir açıldı, %75/%77/%50 doğrulandı" iddiası, aynı URL'nin bağımsız yeniden-açılışında bu rakamları içermiyor. Bu, T3 satırındaki "hızlanma rakamları doğrulandı, çürütülemedi" hükmünün güvenilirliğini de gölgeler — kaynak sayfa doğru olsa da alıntılanan rakamlar o sayfada yok.

**A2** — sondaj 4 (T3, T4, T4-BenchLM, T5); tuttu/tutmadı/erişilemedi = 4/0/0. Tüm sondajlar tuttu; tek nüans T3'te istatistiksel anlamsızlık uyarısının A2 raporunda eksik aktarılmış olması (rakam doğru, yorum eksik). BenchLM %97.6 iddiası GERÇEKTEN var (üçüncül kaynak, Epoch resmî değil) — A2'nin bayrağı doğru.

**A3** — sondaj 4 (T1, T3, T4, T6); tuttu/tutmadı/erişilemedi = 4/0/0. Tüm sondajlar tam eşleşti, özellikle T6/PMC dört rakamın tamamı birebir doğrulandı.

## Genel Not
BLS.gov doğrudan erişimi bot-engeline takıldı (Access Denied, curl); WebSearch özetiyle ikame edildi — birincil kaynağa tam erişim değil, ikincil doğrulama. WEF 2018/%56 rakamı bağımsız aramada çıkmadı (yanlışlanmadı, teyit edilemedi). En önemli bulgu: **A1** dosyasındaki Anthropic %75/%77/%50 alıntısı bağımsız yeniden-erişimde doğrulanamadı → kural gereği A1'in tüm bulguları güven sınıfı K'ya düşürülmeli.
