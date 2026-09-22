# Quant müfredat DAG'ı — v1 (Vega; Atlas koşumu 2026-09-22, hakem hükümleriyle; Karar 109)

`[tip: mufredat-dag | kaynak: jarvis atlas 09-22 | tarih: 2026-09-22 | hedef: vega/ogrenme/quant | sema: v1 | koken: jarvis/claude-fable-5-1/2026-09-22]`

**Kural:** kenar = "önce bunu". Etiket = hakemin kenar hükmü (**D** birincil kaynakta açık önkoşul · **K** dönem sırası/çıkarım · **K↓** daraldı, yalnız yazılan koşulda). Hakemin **X** verdiği kenarlar DAG'a **alınmadı** (aşağıda "Alınmayan kenarlar"). Her düğüm İngilizce sektör başlığı taşır (ogren §2); her düğüme 1 kaynak. Kaynak raporlar: `jarvis/cc/rapor/2026-09/rapor-2026-09-22-quant-mufredat-{tez,antitez}-{A..D}.md` · V26 · hakem; sentez `jarvis/raporlar/2026-09/2026-09-22-quant-mufredat-atlas.md`. AS-OF 2026-09-22.

## Girdi düğümleri (öğrencide var; `PROBE` ile ölçülür, DAG'a girmez)
G1 *Calculus & Linear Algebra* · G2 *Probability Theory* (ders düzeyi) · G3 *Python Basics* · G4 PortRisk mini projesi (yfinance getiriler, Fama-French 5F fikri; K-002).

## Düğümler
| # | Düğüm (sektör başlığı) | Ön-koşul | Kaynak (1) | Blok |
|---|---|---|---|---|
| Q1 | **Financial Markets & Instruments** (hisse, tahvil, forward/futures, opsiyon; no-arbitrage sezgisi) | G1 | Hull, *Options, Futures, and Other Derivatives* ch.1-5 (11. baskı 2021 `[K]`) | Temel |
| Q2 | **Python for Quant Finance** (pandas/NumPy, getiri hesabı, veri: yfinance prototip → WRDS/CRSP akademik → Polygon/massive üretim) | G3 | tidy-finance.org/python (D5-D7 hakem) | Temel |
| Q3 | **Statistics & Financial Data Analysis** (getiri dağılımı, stylized facts, tahmin, hipotez testi) | G2, Q2 | Tsay, *Analysis of Financial Time Series* 3e (2010) ch.1 (C2 D) | Temel |
| Q4 | **Discrete-Time Pricing: Binomial Model** (risk-nötr ölçü, replikasyon, martingale sezgisi) | Q1, G2 | Shreve, *Stochastic Calculus for Finance* **I** (kesikli) — hakem: binom, stokastik hesaptan **önce** | Çekirdek-1 |
| Q5 | **Portfolio Theory & Factor Models** (Markowitz, CAPM, Fama-French, Grinold-Kahn aktif yönetim) | Q3 | Grinold & Kahn, *Active Portfolio Management* 2e (4 kısım; B7 hakem) — stokastik hesap **istemez** | Çekirdek-1 |
| Q6 | **Stochastic Calculus** (Brownian hareket, Itô, martingale; ölçü teorisi **isteğe bağlı titiz yol**) | Q4, G2 (+ ölçü teorisi K↓) | Shreve **II**; titiz yol: Chung / Oksendal (B2 K) | Çekirdek-1 |
| Q7 | **Continuous-Time Derivative Pricing** (Black-Scholes; martingale ve PDE yaklaşımları **alternatif**, sıra değil; Greeks: delta, gamma, **vega**) | Q6 | Joshi, *Concepts and Practice of Mathematical Finance* (martingale) · Wilmott (PDE) (B3 K) | Çekirdek-2 |
| Q8 | **Numerical Methods** (Monte Carlo, sonlu farklar, kalibrasyon) | Q7, Q2 | Oxford MCF Michaelmas çekirdeği (A8 D) — hakem: Computing ile **paralel** | Çekirdek-2 |
| Q9 | **Fixed Income & Interest-Rate Models** (getiri eğrisi, durasyon, kısa-oran modelleri) | Q4, Q6 | Princeton FIN521 / CMU 46956 (A10 K) — hakem: türev-önce yönü şüpheli, bu yüzden Q4+Q6'ya bağlı, Q7'ye değil | Çekirdek-2 |
| Q10 | **Risk Management: VaR / ES / QRM** | Q5, Q3 | Jorion, *Value at Risk* 3e; NYU Core L1 Risk & Portfolio (A5 K) — hakem: stokastik hesapla **paralel** | Çekirdek-2 |
| Q11 | **Time Series & Financial Econometrics** (ARMA/GARCH → piyasa etkinliği testleri) | Q3 | Hamilton (1994) → Tsay → Campbell-Lo-MacKinlay (C1 D; Tsay şart değil, K↓) | Veri |
| Q12 | **Machine Learning for Quant Research** (etiketleme, backtest aşırı-uyumu, CPCV, deflated Sharpe) | Q11, Q2 | López de Prado, *AFML* (2018) + ORIE 5256 modül sırası (C4 K↓ / kenar D) | Veri |
| Q13 | **Backtesting & Strategy Lifecycle** (vectorbt ∥ zipline-reloaded ∥ QuantConnect **alternatif** araçlar; kurulum → icra → post-trade) | Q12, Q5 | Paleologo, *Elements of Quantitative Investing* (2025) · Isichenko (2021) (C9 K) | Uygulama |
| Q14 | **Market Microstructure** (emir defteri, spread, fiyat oluşumu; O'Hara / Harris / Hasbrouck — resmî sıra **yok**, D9) | Q1, Q3 | O'Hara, *Market Microstructure Theory* | Uygulama |
| Q15 | **Stochastic Control & Advanced Topics** (isteğe bağlı) | Q6 | Oxford MCF Hilary (A8 D) | Seçmeli |
| Q16 | **Quant Interview Prep & Job Market** (Green Book · Heard on the Street · 150 MFAQ **3e 2024**; researcher/trader/dev ayrımı; TR + küresel ilan) | Q4, Q6, G2 | quantvault listesi (D10 K) + Kadoa (D12 K↓) + Jane Street ilanı (D14 D) | Kariyer |
| Q17 | **Capstone: PortRisk v2** (faktör analizi + backtest + risk raporu; CV çıktısı m.15) | Q10, Q13 | kendi ürün (`vega/urun/`) | Kapanış |

## Kenarlar (özet; etiket hakem)
G1→Q1 K · G3→Q2 K · G2→Q3 K · Q2→Q3 K · Q1→Q4 K · G2→Q4 K · Q3→Q5 K · Q4→Q6 **K** (Shreve I→II, ters yön X'ten çevrildi) · [ölçü teorisi→Q6 K↓ isteğe bağlı] · Q6→Q7 K · Q7→Q8 K · Q2→Q8 K · Q4→Q9 K · Q6→Q9 K · Q5→Q10 K · Q3→Q10 K · Q3→Q11 K · Q11→Q12 K · Q2→Q12 K · Q12→Q13 **D** · Q5→Q13 K · Q1→Q14 K · Q3→Q14 K · Q6→Q15 K · Q4→Q16 K · Q6→Q16 K · Q10→Q17 K · Q13→Q17 K.

## Alınmayan kenarlar (hakem X)
Computing→Numerical (paralel) · Derivatives→Fixed Income (yön şüpheli) · Derivatives+Numerical→Risk&Portfolio (NYU'da paralel) · Stochastic Calculus→Binomial (ters yön) · PDE→Björk (dayanaksız) · Portfolio→VaR→Meucci sırası (dayanaksız).

## Topolojik sıra (varsayılan öğrenme sırası; paralel dallar ∥)
Q1 ∥ Q2 → Q3 → Q4 ∥ Q5 → Q6 ∥ Q11 ∥ Q10 → Q7 ∥ Q9 ∥ Q12 → Q8 ∥ Q13 ∥ Q14 → Q16 (Q6'dan itibaren paralel) → Q15 (seçmeli) → Q17.

## Program iskeleti kanıtı (A14 K↓)
Hazırlık bloğu → çekirdek-1 → çekirdek-2 → seçmeli → tez deseni CMU (3 hafta prep, A2 düzeltmesi), NYU (3 hafta bootcamp), Oxford (2 hafta 5 giriş dersi, D) programlarında var; Princeton'da belirtilmemiş, ETH-UZH sessiz. Bu DAG'ın "Temel" bloğu o hazırlık bloğunun karşılığıdır.
