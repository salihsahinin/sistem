# JARVIS'le YAPILACAK Proje Fikirleri — Kronolojik Zorluk Partisyonları

*2026-07-16 · Carvis sentezi · Kaynak: 4 paralel Atlas koşusu (Quant/Finans · Veri/ML · Yazılım-Web-LLM-ürün · Kişisel/disiplinlerarası/fırsat). Web taraması Ocak–Temmuz 2026.*

> **Amaç:** JARVIS'i *araç* olarak kullanıp Salih'in YAPACAĞI projelerin (PortRisk sınıfı çıktı-eserleri) fikir havuzu — zorluk + inşa sırasına göre partisyonlanmış. Salih'in çerçevesi: **"JARVIS'le aklıma gelen HER projeyi yapabilmeliyim; başta temel yönelimler olur."** → spektrum geniş, çıpa = çekirdek yönelim (quant/finans/veri/ML).
>
> **Partisyon = zorluk katmanı (S0→S4), aynı zamanda kronolojik inşa sırası.** Her partisyonda proje-fikri sınıflandırmaları; her sınıfta **"örneğin"** somut örnek. Çekirdek yönelim her katmanda önce (çıpa), sonra genişleme (yazılım/ürün), sonra kişisel/disiplinlerarası.
>
> **İsim şerhi:** Bu S0-S4 partisyonları ile (a) `2026-07-16-jarvis-gelistirme...` raporundaki G0-G6 (JARVIS'i inşa) ve (b) `partisyon-plani-P0-P6` (CV/PortRisk takvimi) AYRI eksenlerdir.
>
> **Statü:** HAM FİKİR yüzeyi — hiçbir madde karar/build değil (m.20). Tek-flagship disiplini (m.13) sürüyor: bu havuz seçim turuyla işler, PortRisk canlı-demoya dek aktif artefakt tektir. Fikir-kutusuna pointer olur.

## Sinyal etiketi (agentlerin yakınsadığı ölçek)
⚓ çekirdek yönelim (quant/finans/veri) · 🔵 en yüksek CV sinyali · 🟢 kişisel fayda + gizli CV · 🟡 eğlenceli + orta/niş CV · 🔴 CV-nötr (moral/keyif). **S-tier:** S0 hafta-sonu · S1 küçük-tam · S2 orta · S3 flagship · S4 ileri/yarışma.

## 2026 saha gerçeği (her fikre uygulanan ayrıştırıcı)
Dört şeridin ortak tezi: **"X yaptım" jeneriktir; ayrıştırıcı = gerçek veri + ölçülen sonuç (baseline'a karşı) + canlı deploy + dış doğrulama.** Kod ucuzladı (AI herkeste) → değer *doğru problemi kurmada, dürüst değerlendirmede, domain derinliğinde*. **Kalite > nicelik:** 2-3 derinlemesine-anlatılabilir proje > 8 sığ repo. AI-wrapper / tutorial-repo / "Sharpe 3.0!" mezarlıkları sinyal vermiyor.

---

## PARTİSYON S0 — Hafta-sonu ısınma · *ilk commit çapası, tek notebook*
*Momentum + veri musluğunu açmak; düşük risk, hızlı proof-of-work.*

- **Kişisel portföy faktör-analizi** ⚓🟢 — **Örneğin:** kendi MİDAS getirilerini (anonim ağırlık) *Fama-French 5-faktör + momentum*'a regres et (Ken French Data Library, statsmodels) → alfa + faktör beta'ları (market/SMB/HML/RMW/CMA). *Ayrıştırıcı:* kendi gerçek portföyün + negatif alfayı dürüst raporlamak (mülakat-dostu olgunluk); jenerik "AAPL'ı FF'e regres ettim"den ayrılır.
- **Açık-veri görselleştirme / veri-hikâye** 🟢 — **Örneğin:** TÜİK (enflasyon/demografi) ya da İBB/İETT GeoJSON (İstanbul ulaşım) → Streamlit/Observable Plot canlı dashboard, net bir soruya bağlı. *Ayrıştırıcı:* gerçek Türkçe açık veri + karara-bağlanan içgörü + canlı link; "grafik çizdim"den ayrılır. Kaynak: `acikveri.yagiz.dev`.
- **AI-native mini-artefakt (on-brand)** ⚓🟢 — **Örneğin:** tek-araçlı *Agent Skill* (SKILL.md: "backtest-runner" / "KAP-filing özetleyici") ya da basit *finans-MCP tool'u* (Finnhub'ı saran `get_quote`); `agentskills.io`/registry'de keşfedilebilir. *Ayrıştırıcı:* wrapper değil protokol-uyumlu araç; JARVIS'in AI-native avantajını somut artefakta çevirir.
- **Yaratıcı-kod / moral molası** 🔴 — **Örneğin:** Genuary tarzı p5.js generative eskiz; veri-güdümlü görsel. *Not:* quant CV'ye doğrudan katkı ~yok — "keyif + estetik portfolio" olarak sakla, çekirdek zaman-bütçesini yeme.

## PARTİSYON S1 — Küçük tam proje · *test + README + belki deploy, ilk "gerçek" repo*
*Bir beceriyi uçtan uca kapatmak; her biri anlatılabilir tek-cümle taşır.*

- **Portföy optimizasyonu / tahsis** ⚓🔵 — **Örneğin:** PyPortfolioOpt/Riskfolio-Lib ile efficient frontier + *Black-Litterman* (kendi görüşlerin) + *HRP*/risk-parity; out-of-sample "optimize portföy naif 1/N'i yendi mi?" dürüst testi. *Ayrıştırıcı:* çoğu vakada yenmez — bunu göstermek olgunluk; PortRisk'in doğal tamamlayıcısı (risk ölç → risk dağıt).
- **Sinyal → backtest hattı** ⚓🔵 — **Örneğin:** (a) pairs-trading/kointegrasyon (GARAN/AKBNK ya da EREGL/KRDMD, Engle-Granger) + vectorbt; (b) *GARCH vol-tahmini → dinamik VaR* (`arch`), PortRisk'in statik VaR'ını vol-clustering-farkında yükselt + Kupiec/Christoffersen backtest. *Ayrıştırıcı:* look-ahead-bias'sız + işlem-maliyeti; VaR-backtest bankalara (Garanti/İş Bankası) birebir konuşur.
- **Zaman-serisi tahmini (gerçek yerel veri)** ⚓ — **Örneğin:** EPİAŞ Şeffaflık (`eptr2`/`seffaflik`) elektrik fiyat/talep tahmini; Nixtla StatsForecast baseline'a (AutoARIMA/ETS) karşı ML. *Ayrıştırıcı:* naive/mevsimsel baseline'ı yenmek (çoğu ML yenemez → dürüst rapor bile sinyal), MAPE/sMAPE ölçümü, canlı TR verisi.
- **Domain-RAG / Türkçe-NLP başlangıcı** ⚓🔵 (AI-native) — **Örneğin:** (a) tek-doküman KAP-filing QA (LangChain + Chroma + FastAPI, RAGAS eval); (b) BERTurk fine-tune (Türkçe e-ticaret duygu / haber sınıflama) + F1 + deploy. *Ayrıştırıcı:* RAG "en sık aranan 3 beceriden biri"; Türkçe morfoloji + ölçüm + deploy jenerik chatbot/IMDB-sentiment'ten ayırır.
- **Ship-edilebilir küçük ürün** ⚓🔵 (genişleme) — **Örneğin:** full-stack *finans panosu* temel sürümü (Next.js + Finnhub/Twelve Data WebSocket + Supabase auth + Vercel; ref: `DariusLukasukas/stocks`) ya da `pip install`-lenebilir *backtest CLI* / watchlist tarayıcı-eklentisi. *Ayrıştırıcı:* canlı dış-veri akışı + auth + deploy; CRUD-todo'dan ayrılır.
- **Açık-kaynak katkı** ⚓🔵 (en güçlü tekil sinyal, taklit-edilemez) — **Örneğin:** `borsapy`/`RAGAS`/`Instructor`/`Pydantic AI`'ye "good first issue" PR (`goodfirstissue.dev`). *Ayrıştırıcı:* başkasının merge-standardından geçen PR = dış doğrulama; benchmark = 6-10 issue, ≥1 medium/hard. Wrapper tartışmasının tamamen dışı. [S1→S3 büyür]
- **Kişisel-fayda aracı (gizli CV)** 🟢 — **Örneğin:** kişisel finans/net-değer dashboard (CSV import + kategorize + trend) ya da FSRS spaced-repetition öğrenme aracı; ya da 48-saat *hackathon MVP* (MLH / Akbank DisasterTech). *Ayrıştırıcı:* gerçekten kullandığın araç + (hackathon'da) dış-jüri/Devpost görünürlüğü.

## PARTİSYON S2 — Orta proje · *veri katmanı + model + demo/deploy*
*Sistem düşüncesi; "production'da yaşayan" parçalar.*

- **Yerel-piyasa veri platformu (BIST/TEFAS)** ⚓🔵 (yüksek-yerellik / düşük-rekabet) — **Örneğin:** `borsapy` ile TEFAS fon-tarayıcı (600+ fon Sharpe/vol sıralaması) + *enflasyon-hedge çalışması* (TCMB EVDS-v3 reel getiri: "hangi fon/sektör TÜFE'yi reel yendi?"). *Ayrıştırıcı:* İngilizce quant-repo denizinde BIST/TEFAS analitiği ~yok; Türk işverene "senin piyasan, senin verinle" der. **Şerh:** EVDS artık *evds3* (eski paketler bozuk — currency-farkındalık kancası); scraping ToS'a dikkat, cache+fallback kur.
- **Türev & kripto-quant** ⚓ (tematik genişleme) — **Örneğin:** (a) options *IV-surface + Greeks* (QuantLib/`py_vollib`, Deribit kripto-opsiyon ücretsiz) + no-arbitrage kontrolü — Optiver/IMC market-maker diline birebir; (b) kripto *funding-rate arbitraj* backtester (CCXT `fetchFundingRateHistory`) + P&L attribution. *Ayrıştırıcı:* kripto = 7/24 ücretsiz zengin veri (yfinance kırılganlığından kaçış).
- **Uçtan-uca veri pipeline (veri-mühendisliği)** ⚓ — **Örneğin:** açık API (EPİAŞ/CoinGecko) → `dlt` ingest → *dbt* dönüşüm → DuckDB → Streamlit; GitHub Actions/Prefect ile zamanlanmış + artımlı + veri-kalite testleri. *Ayrıştırıcı:* kendi başına zamanında çalışan, artımlı (full-reload değil), dbt-testli pipeline; "CSV'yi pandas'a okudum"dan ayrılır. Çalışan schedule log'u = proof.
- **Production RAG / agentic uygulama** ⚓🔵 (AI-native) — **Örneğin:** (a) çok-doküman finans-RAG + query-rewrite + *reranking* + RAGAS eval (KAP/earnings korpusu, FastAPI+Next.js); (b) *LangGraph finansal-araştırma ajanı* (veri çek → analiz → haber → insan-onaylı tez; guardrail + eval; ref: `saidsurucu/borsaci`). *Ayrıştırıcı:* faithfulness/eval + kaynak-atıf mühendisi ile prompt-yapıştırıcıyı ayırır; "her şeyi yapan ajan"dan kaçın, dar-derin niş.
- **Nedensellik / deney tasarımı** 🔵 (nadir, yüksek analitik-derinlik) — **Örneğin:** uçtan-uca A-B framework (power analysis + SRM check + *CUPED* varyans-azaltma) ya da uplift modelleme (`uber/causalml`). *Ayrıştırıcı:* korelasyon-ötesi düşünce; çoğu portföy tahminle sınırlı, nedensellik olgunluk gösterir, az rakip.
- **Numerai canlı model (süregelen kanıt)** ⚓ — **Örneğin:** Numerai obfuscated dataset'te LightGBM/nöral model + *haftalık submit* + CORR track-record; Signals'a kendi BIST sinyalin. *Ayrıştırıcı:* Kaggle "bitti"den farklı — canlı, tarih-damgalı, devam eden performans. **Şerh:** staking'siz başla (skor yine görünür, para riski yok → m.31 Katman-1'e girmez).
- **Disiplinlerarası simülasyon / kişisel-RAG** 🟢🟡 — **Örneğin:** (a) Mesa 3 ile ajan-tabanlı ekonomi/emir-defteri simülasyonu (piyasa-mikroyapı sezgisi, quant-komşu); (b) kendi notların üzerinde kişisel RAG "ikinci beyin" (Khoj/LlamaIndex + Ollama) — hem kişisel hem JARVIS altyapısına çift-fayda.

## PARTİSYON S3 — Flagship · *uçtan-uca + canlı demo + özgün anlatı + gerçek kullanıcı*
*Derinlemesine anlatılabilir tek-tek eserler; portföyün belkemiği.*

- **PortRisk v2 — uçtan-uca risk platformu** ⚓🔵 (mevcut flagship'in evrimi) — **Örneğin:** PortRisk'e ekle: faktör-risk ayrıştırma (riskin ne kadarı market/sektör/idiyosinkratik) + rejim-tespiti (Markov-switching/HMM → rejime-bağlı VaR) + Monte Carlo VaR + *TL-krizi stres-testi* (2018/2023 senaryoları) + dinamik GARCH-VaR; canlı Streamlit. *Ayrıştırıcı:* kendi 15-enstrümanlık portföyün + Türk-krizi senaryoları taklit-edilemez. **Şerh:** kapsam-şişmesini m.21 ile parçala; gerçek rakamlar repoya girmez, model/ağırlık girer.
- **BIST/TEFAS flagship ürün (yerel kullanıcılı)** ⚓🔵 (çekirdek × yazılım) — **Örneğin:** enflasyon-düzeltmeli TEFAS analiz panosu + KAP AI-özet asistanı; gerçek Türk kullanıcı topla (Türkiye fintech ~40 mlr EUR ekosistem). *Ayrıştırıcı:* yerel boşluk + "kullanıcısı olan ürün" kanıtı. **⚠️ Katman-1:** gerçek-zamanlı BIST verisi *lisanslı* (VERDA) → gecikmeli/EOD veride kal; canlı yayın öncesi lisans durumu Salih onayı gerektirir (publish kapısı).
- **Türkçe LLM eval / benchmark** ⚓🔵 (AI-native, 2026'nın en-yükselen sinyali) — **Örneğin:** mevcut CETVEL (KUIS-AI) / TR-MMLU üstüne *katkı*, ya da dar bir Türkçe finans/hukuk-muhakeme eval kur + HF leaderboard yayınla. *Ayrıştırıcı:* "model çalıştırdım" değil ölçüm-bilimi (kontamine-olmamış set, hata-taksonomisi); Türkçe niş = az rekabet + akademik görünürlük (arXiv/HF).
- **Sağlam backtest kütüphanesi (overfitting-farkında)** ⚓🔵 (kıdemli-quant sinyali) — **Örneğin:** *Deflated Sharpe Ratio* (Bailey & López de Prado) + *PBO* (kombinatoryal CV) + walk-forward + işlem-maliyeti, bir strateji-ailesi üstünde; pip-paketi + testler. *Ayrıştırıcı:* anti-tutorial duruş — "Sharpe 3.0 buldum ama 200 varyant taradım, deflated 0.4, muhtemelen şans, işte kanıtı." Sahanın en saygı duyduğu şey.
- **Mini-SaaS / ship-edilmiş ürün (para akışı)** 🔵 (nadir junior sinyali) — **Örneğin:** niş finans/SME aracı + Stripe (Next.js + Supabase + Stripe + Vercel). *Ayrıştırıcı:* çalışan ödeme akışı = taklit-edilemez teknik olgunluk. **⚠️ Katman-1:** para akışı + kişisel-veri → Salih onayı; hedef "revenue" değil "çalışan ödeme + birkaç gerçek kullanıcı".
- **Production MLOps kanıtı** 🔵 (2026'nın #1 ayrıştırıcısı: production-ready) — **Örneğin:** bir modeli (S1/S2'den) FastAPI + Docker + HF Spaces + *drift monitoring* (Evidently, PSI/KS) + MLflow + GitHub Actions CI/CD. *Ayrıştırıcı:* modelin zamanla-bozulmasını izleyen sistem; "deploy" iddiasını gerçek kılan katman. Kubernetes gerekmez (tek-kişi ölçek aşımı).

## PARTİSYON S4 — İleri / yarışma / araştırma · *özgün/rekabetçi/araştırma-grade, bonus vitrin*
*Dışsal-doğrulanmış yetenek; portföyün son/opsiyonel parçaları.*

- **Quant trading yarışması** ⚓🔵 (hedef-işverenle *aynı dünya*, dış-doğrulama) — **Örneğin:** IMC Prosperity 5 (~bahar 2027 [?]) / Optiver Ready Trader Go (Avellaneda-Stoikov market-making) + *public writeup*; UChicago/Berkeley Trading, Citadel Datathon. *Ayrıştırıcı:* sıralama + writeup ("ne denedim, ne yaradı, neden") — orta-sıra bile iyi-yazılmış writeup ile güçlü. **Şerh:** takvim-kilitli, planlanmalı.
- **Kaggle featured madalya** 🔵 — **Örneğin:** Playground Series (aylık ısınma) → featured yarışmada bronze/silver + süreç-yazısı (leaderboard ilerlemen, CV-şeman, hata-analizin). *Ayrıştırıcı:* skoru değil *muhakemeyi* göster; Titanic/House-Prices'ı ANA repo yapma (sıfır sinyal).
- **Market-microstructure / LOB deep-learning** ⚓ (hardcore-research, HFT-shop'lara) — **Örneğin:** FI-2010 (ücretsiz) / LOBSTER ile limit-order-book mid-price yön-tahmini (CNN/LSTM/transformer); `LOBFrame` (UCL) reprodüksiyonu + eleştirel analiz. *Ayrıştırıcı:* reprodüksiyon + "literatür %X, ben %Y, fark şu" dürüstlüğü. **Şerh:** LOB'da overfitting/look-ahead çok kolay → şüphe = sinyal; en uzun-çaba, portföyün *son* parçası.
- **Entegre quant araştırma platformu** ⚓🔵 (çok-modül flagship+) — **Örneğin:** data ingest → feature store → backtest → kağıt-ticaret botu → dashboard, tek entegre platform (S2/S3 parçalarını birleştirir). *Ayrıştırıcı:* uçtan-uca quant-engineering. **Şerh:** kağıt-ticaretle kal, canlı para yok (m.13/para eşiği).

---

## Önerilen çekirdek-örgü (agentlerin yakınsadığı sıralı hat)
Dağınık 40 fikir değil, **tek tutarlı anlatı** kur — her adım öncekini besler:

**Quant çekirdek hattı (belkemiği):** `S0 faktör-analizi → S1 GARCH-VaR + portföy-opt → S3 sağlam-backtest → S3 PortRisk v2 (flagship)`. PortRisk'i büyütür, her parça bir öncekini besler.

**Yazılım/ürün örgüsü (genişleme):** `S0 finans-MCP → S1 full-stack finans panosu (MCP'yi tüketir) → S1 borsapy'ye OSS katkı (dış-doğrulama) → S3 BIST/TEFAS flagship (kullanıcılı ürün)`. Tek "finans-veri + AI-native" anlatısı.

**Yerel koz (paralel, yüksek ROI/düşük rekabet):** BIST/TEFAS analitiği (S2) + Türkçe LLM-eval (S3) — İngilizce repo denizinde nadir, Türk işverene birebir.

**Kişisel/keyif (moral + gizli CV):** kişisel finans dashboard · kişisel RAG ikinci-beyin (JARVIS'e çift-fayda) · generative art (CV-nötr, keyif).

**6 ayda gerçekçi:** S0→S3 çekirdek; S4'ler bonus. Salih'in *gerçek hızıyla* kalibre edilmeli (süre tahminleri Atlas kalibrasyonu, [?]).

## Fırsat takvimi 2026-27 (dış-doğrulama kanalları)
- **Şimdi/yakında açık:** MLH 2026-27 hackathon sezonu (200+ etkinlik, çoğu online+ücretsiz, Tem 2026 başladı) · Kaggle Getting Started (her zaman) · Girişimcilik Vakfı Fellow/Challenger 2026-27 (başvuru açık) · TÜBİTAK 2209-A (güz çağrısı ~Eyl-Eki) · Trendyol TEKNOFEST E-Ticaret Datathon+Hackathon (final 5-6 Eyl 2026, 380K₺) · BTK Akademi Hackathon 2026 · Numerai (sürekli haftalık).
- **2026 kapandı → 2027 penceresi izle (~Oca-Şub 2027):** IMC Prosperity 5 · Optiver RTG · UChicago/Berkeley Trading · Citadel Datathon · TEKNOFEST yarışma başvuruları · GSoC 2027 · Outreachy (Ara-2026 kohortu başvuru ~geç-Ağu açılır [?]).
- **Staj-alternatifi (uzaktan, ücretli):** MLH Fellowship (12 hafta) · Outreachy ($6.000 stipend) · GSoC.

## Çapraz-kesen uyarılar
1. **Kalite > nicelik:** hedef 2-3 derinlemesine-anlatılabilir eser (her tasarım kararını mülakatta savunabilmek); 40 fikri de yapmak DEĞİL.
2. **Tek-flagship disiplini (m.13) sürüyor:** bu havuz seçim turuyla işler; PortRisk canlı-demoya dek aktif artefakt tek. Yeni proje açmak = Katman-1/Salih kararı.
3. **Katman-1 kapıları:** para akışı (Stripe/S3-SaaS), lisanslı veri (gerçek-zamanlı BIST), kişisel-veri (dashboard'lar) → publish öncesi Salih onayı; gerçek rakamlar repoya girmez (CLAUDE.md).
4. **Ayrıştırıcı pazarlıksız:** gerçek veri + baseline'a-karşı-ölçülen-sonuç + canlı deploy + (mümkünse) dış-doğrulama. Bunsuz her fikir slop'a düşer.
5. **Veri-kırılganlığı fırsattır:** yfinance kırılgan, EVDS→v3 göçtü → cache+fallback kurmak *production düşüncesi* sinyali verir.

---

## Yöntem & kaynak şerhi
- **Kaynak:** 4 paralel Atlas koşusu (2026-07-16), her biri son 6-12 ayı web-taradı; ~195K subagent-token, ~75 araç-çağrısı.
- **Güven:** Araçlar/kütüphaneler/datasetler (borsapy, eptr2, PyPortfolioOpt, Riskfolio, CCXT, QuantLib, CETVEL/TR-MMLU, RAGAS, Nixtla, causalml, LOBFrame, Mesa, Khoj) GitHub/arXiv/PyPI üzerinden doğrulandı. **Yarışma tarihleri + araç-durumu (IMC 14-30 Nis 2026, EVDS-v3, backtrader bakım-modu, yfinance kırılganlığı) 2026-07-16 teyitli** — yıllık döngü, tekrar-teyit önerilir. Kaggle canlı-sayfa bot-korumasıyla açılmadı [?]. Süre/zorluk tahminleri Atlas kalibrasyonu, Salih hızıyla ayarlanmalı.
- Bu bir 2026-07-16 anlık-görüntüsüdür; saha aylık hızda değişir — karar-anında ilgili repo/takvim tekrar okunur.
