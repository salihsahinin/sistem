# Quant öğrenme sırası — Aile B: klasik kaynak sırası (stokastik hesap · türev fiyatlama · portföy/risk) — Atlas Raporu (2026-09-22)
> **Mod:** ana-sıra, tez ajanı (Sonnet) · şerit: tez (¬tez aşaması ayrı ajanda) · aile sayısı: 1 (B)
> **Kanıt kısıtı (dürüstlük):** QuantNet forum ana konusu 403 döndü (bot/oturum engeli) — **flag: erişilemedi**. Mark Joshi'nin özgün "On Becoming a Quant" PDF'i (tbs-education.fr) WebFetch'te metin çıkaramadı, model genel bilgiden "olası yapı" üretti — bu çıktı **kullanılmadı** (halüsinasyon riski, kaynağa dayanmıyordu). Studocu ve Yumpu kopyaları içerik döndürmedi/boştu.

## Açılan URL'ler (WebFetch, gerçekten indirilen)
1. https://www.quantstart.com/articles/Quantitative-Finance-Reading-List/ — açıldı, içerik alındı.
2. http://magmasystems.blogspot.com/2006/03/on-becoming-quant-by-mark-joshi.html — açıldı, Joshi makalesinden doğrudan alıntı içeriyor (ikincil-birincil karışık; Joshi'nin kendi cümleleri alıntılanmış).
3. https://quantnet.com/threads/master-reading-list-for-quants-mfe-financial-engineering-students.535/ — **403 Forbidden**, flag.
4. https://publication.tbs-education.fr/projets/pole-finance/job/doc/Becoming%20a%20Quant%20by%20Mark%20Joshi.pdf — açıldı ama metin taranamadı (sıkıştırılmış PDF), **kullanılmadı**.
5. https://www.studocu.com/en-gb/document/.../becoming-a-quant-by-mark-joshi/115748627 — açıldı, içerik yok (bozuk sayfa).
6. https://www.yumpu.com/en/document/view/8059811/on-becoming-a-quant-mark-joshis-home-page — açıldı, yalnız başlık/sayfa no listesi döndü, düşük bilgi.

## Aile B başına bulgular

### Alt-küme 1: Stokastik hesap
- **Shreve, *Stochastic Calculus for Finance* I-II (2004):** MFE müfredatlarında ve pratikte "omurga" kabul edilir; Vol I kesikli-zaman (binom) modeller, Vol II sürekli-zaman modelleri kapsar [K] (WebSearch özeti, quantstart.com/quantnet içerik taraması; kaynak: https://www.quantstart.com/articles/Quantitative-Finance-Reading-List/, AS-OF 2026-09-22). Yayım yılı 2004 [?] (bu koşumda birincil kaynaktan doğrulanmadı).
- **Joshi'nin kendi tavsiyesi (magmasystems alıntısı):** "Stochastic calculus is useful but not as important as it at first appears" der; önerdiği metinler **Oksendal** ve **Karatzas and Shreve**; temel olasılık için **Chung** [D] (http://magmasystems.blogspot.com/2006/03/on-becoming-quant-by-mark-joshi.html, AS-OF 2026-09-22 — makale kendisi ~2006 tarihli, orijinal yayım tarihi doğrulanamadı [?]).
- **Björk, *Arbitrage Theory in Continuous Time*:** martingale yaklaşımıyla stokastik hesabı türev fiyatlamaya bağlayan alternatif/tamamlayıcı metin; en güncel baskı (Oxford, ISBN 9780198851615) ölçü teorisi ve olasılık teorisi bölümlerini ayrı ve tam işler [K] (WebSearch, Amazon/OUP ürün sayfası özetinden; AS-OF 2026-09-22, WebFetch ile açılmadı — yalnız arama özeti).

### Alt-küme 2: Türev fiyatlama
- **Hull, *Options, Futures, and Other Derivatives*:** "kapsamlı ama matematiksel olarak düşük seviyeli", saf matematikçiler için bazen sıkıcı bulunur; QuantStart önerisinde ilk okuma turunda kurumsal-detay bölümleri atlanıp forward/future/binom/Black-Scholes/Greeks bölümlerine odaklanılması önerilir [K] (WebSearch özeti, https://www.quantstart.com/articles/Quantitative-Finance-Reading-List/, AS-OF 2026-09-22).
- **Joshi'nin kendi değerlendirmesi (magmasystems alıntısı, D):** Hull "comprehensive but low level mathematically and can be frustrating for pure mathematicians"; Baxter & Rennie "accessible introduction to martingale approach but oriented towards theory rather than practicalities"; Wilmott (Derivatives) PDE yaklaşımında güçlü. Joshi kendi kitabını (2003, *The Concepts and Practice of Mathematical Finance*) da önerir [D] (http://magmasystems.blogspot.com/2006/03/on-becoming-quant-by-mark-joshi.html, AS-OF 2026-09-22).
- **QuantNet "Good Books Before Starting MFE" listesi (K, WebSearch özeti, birincil kaynak açılamadı — 403):** Neftci *An Introduction to the Mathematics of Financial Derivatives*, Neftci *Principles of Financial Engineering*, Mikosch *Elementary Stochastic Calculus With Finance in View*, Joshi *The Concepts and Practice of Mathematical Finance*, Baxter & Rennie *Financial Calculus*, Etheridge *A Course in Financial Calculus*, Wilmott *The Mathematics of Financial Derivatives*, Wilmott *FAQ in Quantitative Finance*, McDonald *Derivatives Markets*, Buchanan *An Undergraduate Introduction to Financial Mathematics* — bu liste "MFE'ye başlamadan önce" kategorisinde, yani stokastik hesap ve türev fiyatlama arasında bir köprü/hazırlık katmanı olarak konumlanıyor [K]. **Bu maddenin kaynağı yalnız arama-özetidir, WebFetch ile doğrudan açılamadı (403) — güven düşürülür.**

### Alt-küme 3: Portföy/risk
- **Grinold & Kahn, *Active Portfolio Management*:** aktif portföy yönetiminin temel metni; Kısım I "Foundations" (CAPM, risk, information ratio, fundamental law of active management), Kısım II beklenen getiri/değerleme, Kısım III bilgi işleme [K] (WebSearch özeti, Google Books/Amazon ürün açıklaması; AS-OF 2026-09-22, WebFetch ile açılmadı).
- **Meucci, *Risk and Asset Allocation*; Jorion, *Value at Risk*:** bu koşumda ikisi de yalnız arama başlıklarında geçti; sıralama/önkoşul ilişkisi doğrulayan bir birincil kaynak **bulunamadı** [X → bulunamadı, meşru]. Genel sektör uzlaşısı (eğitim geçmişimden, doğrulanmamış [?]): Jorion daha giriş-seviyeli VaR mekaniği, Meucci daha ileri/Bayesçi portföy inşası — **bu koşumda kanıtla desteklenmedi, düşük güven**.

## V26 örneklem-denetimi

| Ajan | Denetlenen iddia | Sonuç | Etki |
|---|---|---|---|
| tez-B | "Shreve I-II MFE'de omurga kabul edilir" | K, çapraz-referans yalnız arama-özeti seviyesinde; WebFetch doğrudan doğrulamadı | Güven ORTA'ya düşürüldü |
| tez-B | Joshi'nin Hull/Baxter-Rennie/Wilmott değerlendirmesi (doğrudan alıntı) | D, birincil yazarın kendi cümleleri ikincil barındırıcıda (magmasystems) doğrulandı | Güven YÜKSEK |
| tez-B | QuantNet "Good Books Before MFE" listesi | K, kaynak 403 nedeniyle yalnız arama-özeti; birincil sayfa açılamadı | Güven DÜŞÜK, işaretlendi |
| tez-B | Meucci/Jorion sıralama ilişkisi | X, bulunamadı | Rapora "cevaplanmamış" olarak taşındı |

## Sentez
- **Kesişim (en sağlam):** Shreve I-II stokastik hesabın omurgası; Hull türev fiyatlamada yaygın giriş metni ama matematiksel derinliği düşük bulunuyor; Joshi'nin kendi kitabı ve Baxter-Rennie martingale yaklaşımı için tamamlayıcı — bu üç nokta hem WebSearch hem WebFetch (magmasystems) ile örtüşüyor.
- **Yalnız-arama-özeti (WebFetch doğrulamasız) ayakta kalanlar:** QuantNet'in tam kitap listesi (403 nedeniyle), Björk'ün konumu, Grinold-Kahn içerik yapısı — bunlar K düzeyinde kalıyor, D'ye yükseltilemedi bu koşumda.
- **Çelişkili (X):** yok; ama **bulunamayan** madde var (Meucci/Jorion sıralaması).

## Cevaplanmamış sorular (karar biriktirilmedi — m.41)
1. Meucci (*Risk and Asset Allocation*) ile Jorion (*Value at Risk*) arasında sektörce kabul gören bir önkoşul sırası var mı — bu koşumda birincil kaynakla doğrulanamadı.
2. QuantNet forum konusunun güncel (2024-2026) sürümü ne diyor — 403 nedeniyle bu koşumda erişilemedi; kimlik doğrulamalı bir araçla (gh benzeri, forum hesabı) tekrar denenebilir.
3. Björk'ün Shreve'e göre "önce mi sonra mı okunmalı" sorusu — hiçbir kaynak doğrudan bu ikiliyi karşılaştırmadı.

## DAG önerisi

Düğümler (İngilizce sektör başlığı) — önkoşul → konu:

| Düğüm | Önkoşul(lar) | Kaynak (1) |
|---|---|---|
| Probability & Measure Theory Foundations | — | Chung (temel olasılık); Joshi'nin önerisi — http://magmasystems.blogspot.com/2006/03/on-becoming-quant-by-mark-joshi.html |
| Stochastic Calculus (Itô, martingales) | Probability & Measure Theory Foundations | Shreve, *Stochastic Calculus for Finance* I-II — https://www.quantstart.com/articles/Quantitative-Finance-Reading-List/ |
| Derivative Pricing — Discrete/Binomial | Stochastic Calculus | Hull, *Options, Futures, and Other Derivatives* — https://www.quantstart.com/articles/Quantitative-Finance-Reading-List/ |
| Derivative Pricing — Continuous-Time / Martingale Approach | Derivative Pricing — Discrete/Binomial | Joshi, *The Concepts and Practice of Mathematical Finance* (2003) — http://magmasystems.blogspot.com/2006/03/on-becoming-quant-by-mark-joshi.html |
| PDE Approach to Derivatives | Derivative Pricing — Continuous-Time / Martingale Approach | Wilmott (Derivatives) — http://magmasystems.blogspot.com/2006/03/on-becoming-quant-by-mark-joshi.html |
| Arbitrage-Free Pricing Framework | PDE Approach to Derivatives | Björk, *Arbitrage Theory in Continuous Time* — (yalnız arama-özeti, WebFetch doğrulanmadı) [?] |
| Portfolio Theory & Active Management | Derivative Pricing — Continuous-Time / Martingale Approach | Grinold & Kahn, *Active Portfolio Management* — (yalnız arama-özeti) [?] |
| Risk Management & VaR | Portfolio Theory & Active Management | Jorion, *Value at Risk* — bulunamadı, sıra ilişkisi doğrulanamadı [?] |
| Advanced Risk & Bayesian Allocation | Risk Management & VaR | Meucci, *Risk and Asset Allocation* — bulunamadı, sıra ilişkisi doğrulanamadı [?] |

**Not (dürüstlük):** son üç düğümün (Björk, Grinold-Kahn, Jorion/Meucci) kenar ilişkisi bu koşumda birincil kaynakla doğrulanamadı; sentez aşamasında diğer aile ajanlarının (A/C/D) bulgularıyla çapraz kontrol önerilir.
