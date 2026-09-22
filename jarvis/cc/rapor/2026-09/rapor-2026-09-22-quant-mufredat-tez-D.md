# Quant öğrenme müfredatı — Aile D (uygulama · veri · mikroyapı · kariyer) — Atlas Tez Raporu (2026-09-22)
> **Mod:** ana-sıra alt-ajan (Sonnet, tez şeridi) · şerit: yalnız tez (¬tez aşama 2'de ayrı ajanda) · aile: D
> **Kanıt kısıtı (dürüstlük):** QuantConnect docs sayfasında açık tarih/versiyon damgası yok (D ama AS-OF zayıf); WRDS erişim koşulları sayfada net değil (kurum başvurusu gerekli, K); Türkiye quant iş ilanı hacmi düşük — tek somut örnek bulundu, genelleme yapılmadı.

## Açılan birincil kaynaklar (WebFetch, bu koşumda gerçekten indirildi)
1. https://kariyermerkezi.bogazici.edu.tr/en/is-ve-staj-ilanlari/hft-quant-trader (Türkiye iş ilanı, birincil)
2. https://www.kadoa.com/quant/quant-researcher-jobs (canlı ilan agregatörü, birincil — sayfa "Sep 2026" başlıklı)
3. https://wrds-www.wharton.upenn.edu/pages/about/data-vendors/center-for-research-in-security-prices-crsp/ (WRDS resmi sayfa, birincil, © 1993-2026)
4. https://www.quantconnect.com/docs/v2/writing-algorithms/key-concepts/getting-started (QuantConnect resmi dokümantasyon, birincil)

## Aile D başına bulgular

### D1: Backtest çerçeveleri (vectorbt · backtrader · zipline-reloaded · QuantConnect Lean)
- **vectorbt:** açık-kaynak sürüm bakım modunda, yeni özellikler kapalı-kaynak PRO'da (~$25/ay, 2026 ortası). [K] (arama-özeti; WebFetch yapılmadı) — https://hasanjaved.me/blog/best-python-backtesting-libraries-2026/, AS-OF 2026
- **backtrader:** GitHub yıldız sayısına göre en popüler Python backtest kütüphanesi ama büyük veri/dakikalık veride yavaş, bakım durmuş durumda. [K] — https://quanttradingtools.com/python-backtesting-frameworks/, AS-OF 2026
- **zipline-reloaded:** Quantopian kapanışı sonrası topluluk forku; Pipeline API'si cross-sectional faktör modelleri (long-short equity) için en temiz arayüz. [K] — https://waylandz.com/quant-book-en/Quant-Framework-Comparison/, AS-OF 2026
- **QuantConnect/Lean:** Python VE C# destekliyor (D, WebFetch ile doğrulandı); `Initialize` yöntemi, evren tanımı, warm-up periyodu, zamanlanmış olaylar temel kavramlar. Sayfada açık tarih damgası yok. [D, AS-OF sayfa-tarihsiz — erişim 2026-09-22] — https://www.quantconnect.com/docs/v2/writing-algorithms/key-concepts/getting-started
- **Kesişim:** Başlangıç için vectorbt (hız/parametre taraması) + zipline-reloaded (faktör araştırması) + QuantConnect (uçtan-uca canlıya geçiş yolu) üçlüsü tekrarlanan öneri; backtrader bakım riski nedeniyle ikinci sırada önerilmiş. [K, çoklu ikincil kaynak çakışması]

### D2: Veri kaynakları (yfinance · Polygon · WRDS/CRSP)
- **yfinance:** resmi olmayan Yahoo Finance uç noktalarını kullanıyor, ticari kullanımda hukuki/operasyonel risk taşıyor; hafif prototipleme için hâlâ uygun. [K] — https://wire.insiderfinance.io/..., AS-OF 2026
- **Polygon.io:** gerçek zamanlı + tarihsel veri (hisse, opsiyon, endeks, döviz, vadeli), REST+WebSocket; geliştirme altyapısı için tasarlanmış, göreceli pahalı. [K] — arama özeti, AS-OF 2026
- **WRDS/CRSP:** CRSP, Şubat 2026'da Morningstar tarafından Chicago Üniversitesi'nden satın alındı (D, WebFetch doğrulandı); 450+ akademik kurum erişimi var; öğrenci erişimi kurum temsilcisi başvurusuyla; 23+ ürün kategorisi (hisse 1923'ten, hazine 1916'dan); Stock & Indexes Flat File Format 2.0 (CIZ) 2026'da devreye girdi, eski SIZ formatı kaldırılıyor. [D] — https://wrds-www.wharton.upenn.edu/pages/about/data-vendors/center-for-research-in-security-prices-crsp/, AS-OF erişim 2026-09-22, sayfa güncelleme Ağu-Eyl 2026
- **Kesişim:** akademik/rigorous araştırma → WRDS/CRSP (üniversite erişimi varsa, İTÜ [?] erişimi bu koşumda doğrulanmadı); hafif prototip → yfinance; üretim/canlı → Polygon. Sıralama önerisi: yfinance ile başla → WRDS erişimi varsa akademik tez için kullan → canlıya geçişte Polygon.

### D3: Piyasa mikroyapısı (O'Hara · Harris · Bouchaud)
- O'Hara "Market Microstructure Theory" (1995, Blackwell) standart teorik referans; Harris "Trading and Exchanges" (2003, Oxford) ampirik/pratik köprü; Hasbrouck "Empirical Market Microstructure" (2007, Oxford) ölçüm odaklı; Bouchaud & Potters (2003, Cambridge) istatistiksel fizik perspektifi, daha ileri düzey. [K, çoklu ikincil kaynak; birincil kitap sayfaları WebFetch ile açılmadı — bütçe kısıtı] — https://en.wikipedia.org/wiki/Market_microstructure, https://www.amazon.com/Market-Microstructure-Theory-Maureen-OHara/dp/0631207619, AS-OF 2026
- Önerilen okuma sırası (ikincil kaynaklardan çıkarım, doğrudan bir kaynakta "resmî sıra" bulunamadı — **bulunamadı, meşru**): O'Hara (teori) → Harris (pratik/kurumsal yapı) → Hasbrouck (ölçüm) → Bouchaud & Potters (istatistiksel fizik, ileri düzey). [K]

### D4: Mülakat hazırlığı (Green Book · Heard on the Street · 150 MFAQ)
- Üç kitap çekirdek set: Green Book (Xinfeng Zhou; stokastik hesap, opsiyon teorisi, zor olasılık — araştırmacı/trader rolüne uygun), Heard on the Street (Timothy Crack; daha geniş kapsam, istatistik, finansal ekonomi, brainteaser), Joshi "Quant Job Interview Questions and Answers" (üst-düzey firmalar için). [K] — https://quantvault.org/best-quant-interview-books.html, https://www.tradermath.org/knowledge-base/best-books-for-trading-quantitative-finance-interviews, AS-OF 2026
- "150 Most Frequently Asked Questions on Quant Interviews" — Stefanica, Radoičić, Wang, 2. baskı; Amazon üzerinden birincil yayıncı bilgisi doğrulandı (ISBN 9780979757693). [D — yayıncı/ISBN sayfası, ancak WebFetch yapılmadı, yalnız arama sonucu metaverisi] — https://www.amazon.com/Frequently-Questions-Interviews-Second-Pocket/dp/097975769X
- 2026'da neredeyse tüm quant rollerinde Python akıcılığı asgari beklenti; birçoğu C++ veya pandas/NumPy aşinalığı istiyor. [K] — https://quantvault.org/best-quant-interview-books.html, AS-OF 2026

### D5: 2026 iş ilanı beklentileri (researcher vs trader vs dev; Türkiye + küresel)
- **Küresel:** Kadoa agregatöründe (erişim 2026-09-22) 521 açık "Quantitative Researcher" pozisyonu, 59 hedge fund/prop shop/market maker'da; açıklanan medyan maaş $210k (127 ilanın maaş verisiyle); en çok ilan veren: Point72 (37), Susquehanna/SIG (34), IMC (29), Citadel Securities (25), Jump Trading (23). Lokasyonlar ağırlıklı New York, Londra, Singapur, Chicago, Amsterdam; Hindistan/Macaristan/Vietnam da var. [D, WebFetch doğrulandı] — https://www.kadoa.com/quant/quant-researcher-jobs, AS-OF 2026-09-22 (sayfa "güncel/updated daily" iddiası, tarafımca yalnız erişim anı doğrulandı)
- **Türkiye:** Kadoa listesinde Türkiye lokasyonu/firması YOK (D, negatif bulgu, meşru). Ayrı arama ile tek somut örnek: Algocor Teknoloji A.Ş., İstanbul (Budotek, hibrit), HFT/Quant Trader pozisyonu — min. 2 yıl prop/systematic/electronic trading deneyimi, Python zorunlu, İngilizce+Türkçe akıcılık, C++/SQL tercih; risk yönetimi bilgisi isteniyor. İlan tarihi sayfada yok. [D, WebFetch doğrulandı] — https://kariyermerkezi.bogazici.edu.tr/en/is-ve-staj-ilanlari/hft-quant-trader, AS-OF erişim 2026-09-22, ilan-tarihi bilinmiyor
- **Rol farkı (2026 kaynağı):** researcher = "ne alım-satılacak ve neden" (sinyal/faktör modeli, backtest); trader = canlı risk/PnL sahibi, sistematik model-güdümlü icra; developer = stratejiyi üretim koduna çeviren mühendis, finans alan bilgisiyle. Sınırlar bulanıklaşıyor: araştırmacı artık üretim Python'u, geliştirici stokastik hesap sezgisi bekleniyor. [K] — https://www.tradermath.org/articles/quant-trader-vs-quant-researcher, https://www.techinterview.org/post/3233474729/day-in-life-quant-researcher-trader-developer-strats/, AS-OF 2026
- **Maaş çapası (K, tek kaynaklı, doğrulanmadı):** Jane Street NY ilanlarında Temmuz 2026 itibarıyla 300.000$ taban maaş (trader ve researcher için), üzerine takdiri bonus — bu rakam ikincil kaynak (arama özeti) üzerinden geldi, birincil ilan sayfası WebFetch ile açılmadı. [K] — arama özeti, AS-OF 2026-07

## Cevaplanmamış sorular (karar biriktirilmedi — m.41)
1. İTÜ'nün (ya da öğrencinin bağlı olduğu kurumun) WRDS/CRSP erişimi var mı — bu koşumda doğrulanmadı, kurum kütüphanesine sorulmalı.
2. Türkiye'de quant researcher/trader ilan hacmi bu koşumda tek örnekle (Algocor) sınırlı kaldı; Kariyer.net, LinkedIn Türkiye filtresi, Borsa İstanbul'a bağlı aracı kurumların kendi kariyer sayfaları ayrı taranmadı — bütçe kısıtı.
3. Piyasa mikroyapısı için "sektörde kabul gören tek bir okuma sırası" iddiasını doğrulayan birincil bir müfredat/sylabus bulunamadı; bu rapordaki sıra ikincil kaynak çıkarımıdır (**bulunamadı, meşru**).
4. Jane Street 300.000$ taban maaş rakamı birincil ilan sayfasından teyit edilmedi (bütçe kısıtı, ≤40 çağrı doldu).

## DAG önerisi (Aile D düğümleri; İngilizce sektör başlığı; önkoşul → konu; düğüm başına 1 kaynak)

| Düğüm (İng. başlık) | Önkoşul | Kaynak (1) |
|---|---|---|
| Python for Quant Finance (pandas/NumPy) | Python temel (verilen) | https://quantvault.org/best-quant-interview-books.html |
| Market Data Handling (yfinance → WRDS/Polygon) | Python for Quant Finance | https://www.tidy-finance.org/python/wrds-crsp-and-compustat.html |
| Vectorized Backtesting (vectorbt) | Market Data Handling | https://hasanjaved.me/blog/best-python-backtesting-libraries-2026/ |
| Event-Driven Backtesting (zipline-reloaded / backtrader) | Vectorized Backtesting | https://waylandz.com/quant-book-en/Quant-Framework-Comparison/ |
| End-to-End Algo Platform (QuantConnect/Lean) | Event-Driven Backtesting | https://www.quantconnect.com/docs/v2/writing-algorithms/key-concepts/getting-started |
| Market Microstructure Theory (O'Hara) | Olasılık + Analiz (verilen) | https://en.wikipedia.org/wiki/Market_microstructure |
| Trading and Exchanges (Harris) | Market Microstructure Theory | https://www.amazon.com/Market-Microstructure-Theory-Maureen-OHara/dp/0631207619 |
| Empirical Microstructure Measurement (Hasbrouck) | Trading and Exchanges | https://www.acsu.buffalo.edu/~keechung/MGF743/Readings/Hasbrouck's%20book.pdf |
| Quant Interview Prep (Green Book + Heard on the Street) | Stokastik hesap + Olasılık (Aile B) | https://quantvault.org/best-quant-interview-books.html |
| Quant Job Market Orientation (researcher/trader/dev + TR+küresel ilan taraması) | Quant Interview Prep | https://www.kadoa.com/quant/quant-researcher-jobs |

**Not:** D ailesi düğümleri Aile A/B/C'deki matematik/istatistik önkoşullarına bağımlı (sentez aşamasında birleştirilecek); bu tabloda yalnız D-içi ve D'nin B'ye bağımlılığı gösterildi.
