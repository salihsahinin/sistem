# Quantitative Finance — Sıfırdan Seri (Karar 109, 2026-09-22; DAG `mufredat-dag.md`)

> **Salih beyanı (09-22, aynen):** "quant alanına girmek ve öğrenmeye başlamak istiyorum … mevcut müfredattan sıfırdan ilerleyebilmek için her bir konu başlığına dag oluşturacak şekilde quant öğrendiğim bir ajan oluştur". Müfredat Atlas koşumundan (4 aile tez → antitez → V26 → hakem; sentez `jarvis/raporlar/2026-09/2026-09-22-quant-mufredat-atlas.md`).

**Yüzey:** bu dizin (`~/sistem/vega`), ajan Vega (Sonnet 5 medium + eskalasyon), açılış tetiği **"seans başı, quant"**. Ders iskeleti Jarvis'ten `cc/gelen/ders-Q<N>.md`; ajan `TEACH`/`CLOSE` koşar (Karar 105 M4); iskelet yoksa önceki dersin `## Kalan`'ı ile devam, yeni düğüm açılmaz. **Pratik = Salih'in eli**; `DONE` yalnız Salih beyanıyla. Her derste ≥1 formül elle işletilir (Karar 73). Sektör başlıkları AS-OF 2026-09-22, ders başında canlı teyit (Karar 68). Görsel yalnız istekle, mekanizma simülasyonu.

**Sıra:** `mufredat-dag.md` topolojik sırası. Her düğüm = 1-2 oturum ("hafta" = düğüm). Paralel dallar (∥) Salih tercihiyle sıralanır; varsayılan aşağıdaki satır sırası. Ön-koşul girdileri (kalkülüs · lineer cebir · olasılık · Python temel · PortRisk) `PROBE` ile Q1'de ölçülür.

## Müfredat — 17 düğüm (oturum 1,5-2 sa; `DONE` yazılı)
| Q | Düğüm · Sektör başlığı (EN) | Ön-koşul | Tek-satır `DONE` (Salih yapar) | Formül (Karar 73) | Kaynak |
|---|---|---|---|---|---|
| Q1 | Financial Markets & Instruments | — | 5 enstrümanın kâr/zarar diyagramı elle + no-arbitrage örneği | forward fiyatı F = S·e^{rT}; put-call paritesi C − P = S − K·e^{−rT} | Hull ch.1-5 |
| Q2 | Python for Quant Finance | Python temel | yfinance'ten 3 hisse, günlük log-getiri, kovaryans matrisi (kendi koşumu) | r_t = ln(P_t/P_{t−1}); yıllık σ = σ_g·√252 | tidy-finance.org/python |
| Q3 | Statistics & Financial Data Analysis | Q2, olasılık | stylized facts tablosu (kalın kuyruk, kümelenen oynaklık) kendi verisinde | basıklık κ = m₄/σ⁴ − 3; Jarque-Bera | Tsay 3e ch.1 |
| Q4 | Discrete-Time Pricing: Binomial Model | Q1, olasılık | 3-adımlı binom ağacında Avrupa call elle + kodla | q = (e^{rΔt} − d)/(u − d); V₀ = e^{−rT}·E_q[payoff] | Shreve I |
| Q5 | Portfolio Theory & Factor Models | Q3 | PortRisk verisinde min-varyans portföy + Fama-French 3F regresyonu | w* = Σ⁻¹μ / 1ᵀΣ⁻¹μ; IR = α/ω (Grinold-Kahn) | Grinold & Kahn 2e |
| Q6 | Stochastic Calculus | Q4 (+ ölçü teorisi isteğe bağlı) | Itô lemması ile d(ln S) türetimi elle; Brownian simülasyonu | dS = μS dt + σS dW → d ln S = (μ − σ²/2)dt + σ dW | Shreve II |
| Q7 | Continuous-Time Derivative Pricing | Q6 | Black-Scholes fiyatı elle + kod; Greeks tablosu (delta · gamma · vega) | C = S·N(d₁) − K·e^{−rT}·N(d₂); vega = S·φ(d₁)·√T | Joshi (martingale) · Wilmott (PDE) |
| Q8 | Numerical Methods | Q7, Q2 | Monte Carlo (10⁴ yol) ↔ kapalı form hata tablosu | SE = σ̂/√N; Euler-Maruyama | Oxford MCF çekirdeği |
| Q9 | Fixed Income & Interest-Rate Models | Q4, Q6 | getiri eğrisi bootstrap + durasyon/konveksite elle | D = −(1/P)·dP/dy; Vasicek dr = a(b − r)dt + σ dW | Princeton FIN521 / CMU 46956 |
| Q10 | Risk Management: VaR / ES / QRM | Q5, Q3 | PortRisk portföyünde tarihsel + parametrik VaR ve ES, backtest (Kupiec) | VaR_α = −q_α; ES_α = E[L \| L ≥ VaR_α] | Jorion 3e |
| Q11 | Time Series & Financial Econometrics | Q3 | GARCH(1,1) kendi verisinde; piyasa etkinliği testi | σ²_t = ω + α ε²_{t−1} + β σ²_{t−1} | Hamilton → Tsay → Campbell-Lo-MacKinlay |
| Q12 | Machine Learning for Quant Research | Q11, Q2 | CPCV ile bir sinyal; deflated Sharpe hesabı | DSR; PBO (backtest overfitting olasılığı) | López de Prado, AFML + ORIE 5256 |
| Q13 | Backtesting & Strategy Lifecycle | Q12, Q5 | aynı stratejiyi vectorbt ∥ QuantConnect'te koşup fark tablosu | Sharpe = (μ − r_f)/σ·√252; turnover; işlem maliyeti | Paleologo 2025 · Isichenko 2021 |
| Q14 | Market Microstructure | Q1, Q3 | emir defteri simülasyonu; spread bileşenleri | Roll spread s = 2√(−Cov(Δp_t, Δp_{t−1})) | O'Hara · Harris · Hasbrouck |
| Q15 | Stochastic Control & Advanced (seçmeli) | Q6 | Merton portföy problemi türetimi | HJB denklemi | Oxford MCF Hilary |
| Q16 | Quant Interview Prep & Job Market | Q4, Q6 | 20 Green Book sorusu çözülmüş; TR + küresel 10 ilan tablosu | — | Green Book · Heard on the Street · 150 MFAQ 3e (2024) |
| Q17 | Capstone: PortRisk v2 | Q10, Q13 | faktör + backtest + risk raporu; CV satırı (m.15) | — | `vega/urun/` |

## Sınırlar
- md.49: şirket/staj verisi yok; kamu verisi (yfinance, Fama-French kütüphanesi, WRDS akademik erişim varsa).
- Her rakam kaynaklı; satıcı/blog rakamı `[K]`; kendi koşumu `D`. Look-ahead/veri sızıntısı hakem ölçütü.
- Hazırı temel al: pandas · statsmodels · arch · PyPortfolioOpt · vectorbt; benzeri sıfırdan yazılmaz.

## Ders kaydı biçimi
`dersler/YYYY-MM-DD-QN-konu.md`, şema `ogren` §5. Kutu başlığı yanında sektör başlığı. İlerleme `ilerleme.md`.
