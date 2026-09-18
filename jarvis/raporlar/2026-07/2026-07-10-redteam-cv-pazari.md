# Görev Raporu — "Bomba CV" Planı: Duvar Taraması (Red-Team)

**Ajan:** red-team (CV pazarı) · **Tarih:** 2026-07-10 · **Statü:** rapor — karar içermez · **Tüketen:** `00_MASTER_PLAN.md` + `03_DUVAR_RAPORU.md`

## 0. Yönetici Özeti — En Sert Üç Bulgu

1. **Plan fazla sistem-inşası, fazla az görünür shipping içeriyor.** Sayısal kanıt yerel diskten: **Homebase (planlama reposu) son 2 günde 53 commit; portrisk (CV artefaktı) son 8 günde 0.** Oran 53:0. Screener'ın göreceği tek taraf, 0 olan taraf.
2. **Belgelenmiş tempoyla 6 ayda 3 repo gerçekçi değil.** 06-18'de yazılan 8-haftalık MVP planında bugün hafta ~3; hafta 2 işi (Sprint 1, yfinance+getiriler) başlamadı. Gerçekleşme/plan oranı ≈ 0. vault-index'in workspace'te spec'i dahi yok (grep: 0 sonuç). Bar'ı geçen minimum portföy 3 repo değil: **1 bitmiş + deploy edilmiş repo + düzgün commit geçmişi + İngilizce CV + 1 yarışma satırı.**
3. **JARVIS repo olarak sinyal değil, gürültü — kötü sunulursa red flag.** 2026'da screener'lar AI-üretimi jenerik repo okyanusunda yüzüyor (The Markup); "kişisel AI orkestrasyon sistemi (markdown planlar)" tam bu şüpheyi tetikleyen kategori. Mülakat anlatısı olarak değerli, repo olarak değil.

## 1. Araştırma Bulguları

### 1.1 Screener'lar 2025-26'da gerçekte neye bakıyor (DS/ML/quant staj)
- **İlk eleme insan değil, hız + ATS.** Recruiter ilk bakışta CV'ye 6-10 saniye; ATS için ilanla ~%70 keyword örtüşmesi + sayısallaştırılmış sonuçlar (%, $, süre) + standart bölüm başlıkları (enhancv, cvcompiler, Medium/Reshtei). GitHub linki header'da beklenir ama **GitHub'a bakış CV'yi geçtikten sonra gelir** — GitHub, CV zayıflığını telafi etmez [çıkarım].
- **DS staj ilanlarının değişmez çekirdeği:** Python + **SQL** + istatistik + ML kütüphaneleri + görselleştirme + "modelleme tercihlerini savunabilme" (Indeed/Coursera taraması). SQL neredeyse her ilanda; planda hiçbir yerde yok.
- **Quant trading firmaları (Optiver/IMC/Jane Street sınıfı) bambaşka eleme:** matematik/olasılık, mental math testi (Optiver "80-in-8"), olimpiyat geçmişi, okul seçiciliği; kişisel GitHub bu firmaların ilk elemesinde neredeyse ağırlıksız (quantt.co.uk, techinterview.org, getsmartresume, northwesternfintech/2026QuantInternships). **"Quant" hedefinin iki ayrı pazarı var — trading firmaları (GitHub'ın az işe yaradığı) ve finans-domenli data/ML rolleri (GitHub'ın gerçekten işe yaradığı). Plan ikincisine hizmet ediyor; bunu bilerek yazmak gerek.**

### 1.2 GitHub vs not/okul/yarışma ağırlığı
- Tech recruiter'ların %60-80'i linklenen GitHub'a göz atıyor, %40-50'si derine iniyor; LLM-tabanlı repo özetleme araçları yaygınlaştı (fonzi.ai). Staj elemesinde ilk kapı GPA + test + okul; GitHub ikinci tur malzemesi [çıkarım].
- **Kaggle:** yüksek sıralama yoksa zayıf sinyal; kendi problemini tanımlayan kişisel proje jenerik Kaggle'dan daha etkili (datascienceweekly).
- **IMC Prosperity:** son turda 18.803 takım, üniversite öğrencilerine dünya çapında açık, remote, ücretsiz (prosperity.imc.com). Yüzdelik dilim CV'ye ölçülebilir tek satır; matematik+trading+Python kesişimine en uygun yarışma. **Planda yarışma kanalı tamamen boş.**

### 1.3 Türkiye + remote-uluslararası gerçeklik
- **Asıl hacim banka genç-yetenek programları:** Garanti BBVA Talent Week **Data MT** — 2026 başvuruları 27 Ocak–19 Şubat'tı; 2027 döngüsü benzer pencerede beklenir, Kas-Şub CV penceresiyle çakışır. İş Bankası MasterClass (20-30 iş günü hibrit yaz stajı) ve Akbank Gençlik Akademisi aktif. Eleme tipik: transkript + sayısal/kişilik testleri + mülakat; GitHub ilk kapıda görünmez [çıkarım].
- **Midas:** aktif veri/AI ekibi var (Coderspace podcast) ama görünür ilanlar deneyimli seviye; yapılandırılmış veri-staj programı bulunamadı — giriş muhtemelen network/spontane başvuru [çıkarım].
- **TR quant ekosistemi küçük ama sıfır değil:** ALGOCOR (HFT), Liquidity Trading, TradeWise; LinkedIn'de ~59-72 "quantitative finance" ilanı.
- **Remote-uluslararası:** stajda vize sponsorluğu nadir; gerçek yollar (a) Optiver/IMC Amsterdam yaz stajları (dünya çapında açık, eleme elit), (b) UNDP-tarzı remote araştırma stajı, (c) Erasmus+ Digital Opportunity. **Ana senaryo Türkiye içi; uluslararası remote düşük-olasılıklı yan bahis** [çıkarım].

### 1.4 "AI-destekli portföy" algı problemi — slop'tan ayrışan ne?
2026 konsensüsü: AI kullanmak red flag değil; **savunamamak** red flag.
- "Çalışan bir şey inşa edebilmek artık ilginç değil — AI 20 dakikada üretiyor." Ayrıştırıcı, kodun *üstündeki* katman: problem kapsamlama, elle doğrulama, mimari gerekçe (Medium/Shipping Engineer).
- **"Defend your diff" testi:** rastgele 3 satır + "neden bu, alternatifi neydi?" — cevapsızsa elenirsin (abbacustechnologies).
- **Commit geçmişi şekli sinyal:** tek dev commit = "kopyaladın" algısı; düzenli, kendi cümlelerinle mesajlanmış commit'ler = gerçek iteratif iş (DeployHQ, dev.to). **portrisk şu an tam ters örnek: tek commit'lik iskelet.**
- **Deploy edilmiş canlı link en az kullanılan, en çok ayrıştıran öğe;** 2-3 cilalı+deploy proje 10 yarımı ezer; README = hook + demo GIF/canlı link + mimari diyagram; "2 dakikada anlamazsam sonraki adaya geçerim" (careery.pro, Medium/Vourakis).
- **Rekabet setinin fotoğrafı:** GitHub `value-at-risk` topic'i dolu; örnek öğrenci reposu Sribaru45/quant-finance-dashboard — 6 modül (Monte Carlo VaR/CVaR, Black-Scholes, Markowitz, pairs-trading, screener), Streamlit, canlı deploy. **PortRisk'in planladığı her şeyi içeren repolar şablonlaşmış.** Jenerik VaR/backtest reposu görünmezdir; ayrıştırıcı yalnız "gerçek 15-enstrümanlı kendi portföyüm + gerçek karar sürecim" anlatısı + savunulabilir metodoloji [çıkarım + kaynak].

## 2. Adversarial Değerlendirme

### 2.1 PortRisk — **HELPS (tek gerçek aday) — ama yalnız bitirilirse; bugünkü haliyle HURTS'a yakın**
Finans-domenli data/ML stajı için doğru türde artefakt. **Ama** bugünkü hali (1 commit, "Full methodology section to follow" README, yalnız CSV loader) screener için klasik "başlanmış-bırakılmış" sinyali — boş repoyu linklemek linklememekten kötü [çıkarım].
- **Etkileyici yapan:** canlı Streamlit URL'i · MİDAS v7 gerçek-portföy anlatısı ("kendi paramın riskini ölçemiyordum, aracı kurdum") · İngilizce metodoloji · düzenli haftalık commit'ler · pytest coverage · "AI ile nasıl çalıştım, neyi elle doğruladım" bölümü (2026'da artı sinyal — herohunt).
- **Görünmez yapan:** jenerik yfinance+Sharpe+VaR kombinasyonunda kalmak · deploy'suz script olarak bitmek · tek-commit geçmiş · Türkçe/yarım README.

### 2.2 vault-index — **NEUTRAL; yanlış zamanlamada HURTS (PortRisk'i öldürerek)**
Teknik içerik gerçek mühendislik sinyali (FTS5, BM25, RRF, MinHash — ölçülebilir retrieval işi). Üç sorun: (1) mevcudiyeti sıfır — şu an fikir cümlesi; (2) anlatı tutarlılığı — "finans quant×AI" hedefiyle markdown-indeksleyici hikayeyi dağıtır, screener 8 saniyede tek tema okur [çıkarım]; (3) fırsat maliyeti — belgelenmiş tempoda ikinci repo birincinin bitmemesi demek; "2-3 cilalı > 10 yarım" kuralının ön koşulu *cilalı*. Etkileyici olması ancak: PortRisk deploy edildikten SONRA, ölçümlü benchmark'la (recall@k, latency, dedup precision) ve İngilizce yazıyla. Ölçümsüz "kendi not-arama aracım" 2026'da kişisel-RAG klişesi [çıkarım].

### 2.3 JARVIS node — **NOISE; kötü sunumda RED FLAG**
Screener'ın 6-8 saniyesinde "personal AI orchestration system (markdown plans)" kod içermeyen doküman yığını olarak okunur. 2026'da "kendi JARVIS'imi kurdum" cümlesi AI-slop şüphesini tetikler (The Markup, learnist.org). Ek risk: içerik kişisel — public'e açmak gizlilik sorunu. **Ama:** Salih'in gerçek AI-workflow akıcılığı gerçek varlık, 2026'nın aradığı profil tam bu. Doğru taşıyıcı: **mülakat anlatısı + PortRisk README'sinde 5 satırlık "AI-assisted workflow" bölümü + belki tek blog yazısı.** Sistem repo olarak CV'ye girmemeli. İçinden dar, çalışan, ölçülebilir bir araç çıkarsa (vault-index kalıbı) CV'ye giren o araç olur — "sistem" değil.

### 2.4 Timeline — **HAYIR (mevcut tempoda); koşullu EVET (tek repo'ya daralırsa)**

| Kanıt | Değer |
|---|---|
| portrisk toplam commit (07-02'den beri) | 1 (GitHub'dan doğrulandı) |
| Homebase planlama commit'leri (07-09/07-10) | 53 |
| 8-haftalık MVP planında bulunulan nokta | Hafta ~3; Sprint 1 başlamadı (plan: hafta 2) |
| Kayıtlı desen | "3. commit'siz oturum" bizzat CLAUDE.md'de; strateji teşhisi: "niyet ≫ eylem" |

Aritmetik [çıkarım]: Kasım başına ~16 hafta, Şubat sonuna ~33. PortRisk MVP 7 hafta daha ister; gerçekleşme katsayısı 0 olduğundan iyimser 2x çarpanla ~14-16 hafta → **PortRisk tek başına Kasım penceresini yer.** vault-index ancak Şubat'a, o da tempo dönerse. Üç artefakt matematiksel olarak kapanmıyor.

**Bar'ı geçen minimum portföy:** 1 bitmiş+deploy PortRisk (canlı link + testler + İngilizce README + ≥20 anlamlı commit) + GitHub graph'ta düzenli aktivite + İngilizce CV/LinkedIn + 1 ölçülebilir yarışma satırı.

### 2.5 Planda eksikler (screener'ların gerçekten istediği)
1. **SQL** — ilanların değişmezi; planda sıfır. (PortRisk Faz-2 SQLite katmanı öne çekilerek kapanır.)
2. **İngilizce CV + LinkedIn + GitHub profil README'si** — ATS/keyword katmanı tamamen boş.
3. **GPA/transkript gerçeği** — banka programları ilk kapıda not + testle eler; kayıtlarda GPA hiç geçmiyor: açık eleme değişkeni.
4. **Yarışma kanalı** — IMC Prosperity tarzı, Kasım öncesi ölçülebilir satır ekleyebilecek tek hızlı kanal; planda yok.
5. **Deploy edilmiş canlı link** — en ayrıştırıcı öğe; "belki" değil çekirdek teslimat olmalı.
6. **Mülakat/test hazırlığı** — quant yönü ciddiyse eleme repo değil test (mental math, olasılık); data/ML için "modelleme tercihini savun" standardı.
7. **Başvuru lojistiği** — pencereler Oca-Şub'da; hedef program listesi + tarih takvimi şimdiden yoksa CV doğru tarihte yanlış masada kalır. CV'nin gerçek son teslim tarihi Kasım değil, ilk programın başvuru açılışı.

## 3. En Yüksek Kaldıraçlı 5 Aksiyon (öneri; karar Salih'in)

1. **PortRisk'i tek flagship ilan et; canlı demoya kadar başka artefakt açma.** DONE: README'de tıklanabilir canlı Streamlit URL'i; vol/Sharpe/Sortino/MDD/VaR + benchmark backtest çalışır; pytest yeşil; İngilizce README (hook + demo + mimari + metodoloji).
2. **Commit çapası: 8 hafta boyunca haftada ≥3 anlamlı portrisk commit'i.** DONE: GitHub contribution graph'ta 8 ardışık hafta ≥3 kod commit'i; mesajlar kendi cümlelerinle İngilizce.
3. **Bir sonraki IMC Prosperity turuna (veya eşdeğer) kaydol ve bitir.** DONE: leaderboard'da takım adı + CV'de "top X% of ~19k teams" satırı.
4. **İngilizce CV + LinkedIn + GitHub profil paketi (tek hafta sonu işi).** DONE: 1 sayfa İngilizce CV (sayısal maddeler) + canlı LinkedIn + PortRisk'i pinleyen profil README'si.
5. **SQL kanıtını PortRisk'e göm: fiyat verisi SQLite'a yazılsın/sorgulansın.** DONE: veri katmanı SQLite üzerinden; README'de şema + örnek sorgu; ≥1 test SQL katmanını kapsıyor.

Yan öneri: vault-index'i "PortRisk canlı linki DONE olana kadar" dondurulmuş aday olarak kaydet; JARVIS'i repo hedefi listesinden çıkar, mülakat-anlatısı + README-bölümü olarak yeniden sınıflandır. Başvuru takvimi (Garanti Talent Week ~Oca-Şub, İş MasterClass, Akbank, Optiver/IMC Amsterdam) Kasım'dan önce tek sayfaya dökülmeli.

## Kaynaklar
enhancv · cvcompiler · Medium/Reshtei (ATS) · beamjobs · quantt.co.uk (Optiver) · techinterview.org · getsmartresume (Jane Street) · northwesternfintech/2026QuantInternships · Optiver EU campus Q&A · fonzi.ai · DeployHQ · dev.to (GitHub profili) · The Markup (AI slop) · abbacustechnologies · learnist.org · herohunt.ai · Medium/Shipping Engineer · careery.pro · Medium/Vourakis · staragile · datascienceweekly (Kaggle) · prosperity.imc.com · OpenQuant · Garanti BBVA kariyer + machingo · İş Bankası staj · Akbank Youth Academy · TBB staj · Coderspace (Midas podcast) · Boğaziçi Kariyer (HFT ilanı) · LinkedIn TR · erasmusintern.org · impactpool (UNDP) · Sribaru45/quant-finance-dashboard · Coursera (DS Internship 2026). Yerel kanıtlar: github.com/salihsahinin/portrisk (1 commit — WebFetch doğrulaması) · SALIH_IT_STAJ_STRATEJISI_v1.md (8-haftalık MVP + "niyet ≫ eylem") · Homebase git log (53 commit / son 2 gün) · workspace grep: "vault-index/FTS5/MinHash" = 0.

**Rapor sonu.** En kısa özet: duvar, artefakt seçiminde değil — üretim temposunda ve "sistem kurma"nın "gönderme"yi sürekli ikame etmesinde. Plan 3 repo diyor; kanıt tabanı 1 bitmiş repo + yarışma + İngilizce paket diyor.
