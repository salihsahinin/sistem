# Quant müfredat — antitez (Aile D), CoVe-Factored, AS-OF 2026-09-22

Açılan birincil kaynaklar (≥2, gerçekten WebFetch ile açıldı):
- https://github.com/mementum/backtrader (repo sayfası)
- https://github.com/polakowo/vectorbt (repo/README)
- https://www.janestreet.com/join-jane-street/position/6302325002/ (canlı ilan)
- https://blog.tidy-finance.org/posts/crsp-v2-update/ (CRSP format tarihçesi, 2024-03-13 yayın)
- https://www.fepress.org/150iqs-third-edition/ (yayıncı, birincil)
- https://massive.com/pricing (Polygon.io'nun yönlendiği güncel fiyat sayfası)

Engellenen/paywall (403, bayraklı): glassdoor.com/Job/istanbul-quantitative-jobs..., kariyer.net/is-ilanlari/kantitatif-analist, crsp.org/important-notice-... (404).

| # | ¬T kanıtı | URL | AS-OF | Sonuç |
|---|---|---|---|---|
| 1 | Karşı kanıt yok; vectorbt README'si açık-kaynağın bakım-modunda kaldığını, PRO'nun haftalık yeni özellik aldığını doğrudan doğruluyor. | github.com/polakowo/vectorbt | 2026-09-22 | DAYANDI |
| 2 | Backtrader 23,3k yıldızla popülerlik iddiasını destekliyor; ancak "bakımı durmuş" iddiasına karşı **kısmi** kanıt: PyPI'deki son sürüm 2023-04-19 ama master dalında 2026-03-27'ye kadar PR aktivitesi var — "tam durmuş" değil, "solo-bakımcı, yavaşlamış" daha doğru. | github.com/mementum/backtrader | 2026-09-22 | DARALDI |
| 3-5 | Sıralama/öneri iddiaları için doğrudan ¬T kanıtı bulunamadı; taranan üçüncül blog kaynakları (quantengines.com, bullalert.ai, pickuma.com) SEO-tipi düşük yetkeli sitelerdi, kanıt sayılmadı. | — | 2026-09-22 | DAYANDI (zayıf temelli — kaynaklar düşük yetkeli) |
| 6 | Karşı kanıt yok; yfinance'in kendi belgesi ve Yahoo API ToS ("kişisel kullanım", "AS IS", ticari kullanımda risk) iddiayı doğruluyor. | ranaroussi.github.io/yfinance, legal.yahoo.com | 2026-09-22 | DAYANDI |
| 7 | Kısmi çürütme: Polygon.io artık **massive.com**'a yönleniyor (marka değişikliği, iddiada geçmiyor) ve "Stocks Basic" **ücretsiz** katman + "Stocks Starter" **$29/ay** sunuyor — "göreceli pahalı" genellemesi giriş seviyesinde geçerli değil; üst katmanlar ($79-199+/ay, gerçek-zamanlı/WebSocket) için pahalılık iddiası hâlâ makul. | massive.com/pricing | 2026-09-22 | DARALDI |
| 8 | Karşı kanıt yok; Morningstar-CRSP satın alımı 2026-02-02'de tamamlandı, iddiayla uyumlu (tutar $365M, iddiada geçmiyor ama çelişmiyor). | investing.com, newsroom.morningstar.com | 2026-09-22 | DAYANDI |
| 9 | **Çürütüldü (tarih hatası):** CIZ formatı 2026'da değil, **2022 yazında** devreye girmiştir; eski SIZ formatı "2026'da kaldırılmakta" değil, WRDS/tidy-finance'e göre **2024 sonu itibarıyla** (Aralık 2024 verisi, Ocak 2025 yayını) zaten son sürümünü almış, fiilen emekliye ayrılmıştır. İddianın zamanlaması CRSP'nin 2026 Morningstar satın alımıyla karışmış görünüyor. | blog.tidy-finance.org/posts/crsp-v2-update/ | 2026-09-22 | ÇÜRÜDÜ |
| 10-11 | İddia 11 zaten kendi kendini sınırlıyor ("resmî kaynak bulunamadı"); aramalarım da tersini kanıtlayan resmî bir sıralama bulamadı — okuma sırasına alternatif olarak Cont/Bouchaud gibi başka açılışlar öne çıkan bloglar var ama "resmî" iddiayı çürütecek güçte değil. | — | 2026-09-22 | DAYANDI |
| 12 | Karşı kanıt aranmadı (bütçe); üç kitabın mülakat çevresinde yaygın atıf aldığı önceki bilgiyle çelişmiyor. | — | 2026-09-22 | DAYANDI (araştırılmadı) |
| 13 | **Daraldı:** 2. baskının ISBN'i (9780979757693) doğru, ancak aynı yazarlar **3. baskıyı** 2024'te (ISBN 978-1734531244) yayıncının kendi sitesinden çıkardı — 200+ soru, ilk kez istatistik/ML soruları eklendi. İddia "çekirdek kitap" olarak güncelliğini kaybetmiş bir baskıyı öne çıkarıyor. | fepress.org/150iqs-third-edition/ | 2026-09-22 | DARALDI |
| 14 | Karşı kanıt aranmadı (bütçe). | — | 2026-09-22 | DAYANDI (araştırılmadı) |
| 15-16 | Kadoa'nın kendi sayfasına erişilemedi (bütçe/API kısıtı); rakamlar doğrulanamadı, çürütülemedi de — kaynak tekilliği (tek agregatör) başlı başına bir risk. | — | 2026-09-22 | DAYANDI (doğrulanamadı, tek-kaynak riski işaretli) |
| 17-18 | **Zayıf çürütme adayı, doğrulanamadı:** LinkedIn üzerinden yapılan bir aramada Ata Portföy Yönetimi için "Quantitative Trader" (İstanbul) başlıklı bir sonuç göründü, ancak takip WebSearch'ü bu ilanı bağımsız olarak doğrulayamadı ve LinkedIn/Glassdoor sayfaları 403 ile engellendi. Bu nedenle "Algocor tek somut örnektir" iddiasını çürütecek güvenilirlikte bir ikinci örnek **teyit edilemedi**; bulgu bayraklanıyor, iddiaya karşı kanıt sayılmıyor. | linkedin.com/jobs (erişilemedi doğrudan), glassdoor.com (403) | 2026-09-22 | DAYANDI (teyitsiz aday var, çürütme yetersiz) |
| 19 | Karşı kanıt aranmadı (bütçe); rol sınırlarının bulanıklaştığı iddiası sektör-genel bir gözlem, spesifik çürütme hedefi değil. | — | 2026-09-22 | DAYANDI (araştırılmadı) |
| 20 | Karşı kanıt yok; Jane Street'in canlı ilanı $300.000 taban maaşı + takdiri bonusu birebir doğruluyor. | janestreet.com/join-jane-street/position/6302325002/ | 2026-09-22 | DAYANDI |

## Özet
20 iddiadan **1 ÇÜRÜDÜ** (#9, CRSP CIZ/SIZ tarihi yanlış), **3 DARALDI** (#2 backtrader "durmuş" abartılı, #7 Polygon.io giriş seviyesi ücretsiz/ucuz, #13 2. baskı güncelliğini yitirmiş), geri kalanı **DAYANDI** (bir kısmı bütçe nedeniyle araştırılmadı, iki kalemde tek-kaynak/teyitsizlik riski işaretlendi: #15-16 Kadoa, #17-18 Türkiye ikinci örnek adayı).

**Epistemolojik not:** Çürütme aranan, bulunmayan iddialer otomatik doğru sayılmaz; yalnız bu turda ¬T kanıtı bulunamadığı anlamına gelir.
