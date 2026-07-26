# Tech Stack — insan yüzü

> Kaynak: `raporlar/2026-07-26-tech-stack-atlas.md` · Register: kavrayış · Compiler: **AÇIK** (F1-F9)
> **UYARI: Bu dosya karar kaynağı DEĞİLDİR.** Katman-1 kararı teknik kayıttan alınır — özellikle §7'deki Model C imzası. Her maddenin sonunda kaynak bölüm var.
> *Not: teknik kayıt başında "insan-yüzü üretilmeyecek" yazar; o beyan 07-26 emriyle aşıldı ve orada üstü çizildi.*

---

## 1. Tek cümlede

Teknoloji seçimi hakkında **ölçülmüş** olan neredeyse her şey *seçtiğin şeyin yaşayıp yaşamayacağıdır*; **ölçülmemiş** olan neredeyse her şey *nasıl seçmen gerektiğidir* — ve herkesin baktığı sinyal (yıldız) ölçülmüş şekilde **bozuk**, kimsenin bakmadığı sinyal (indirme) ölçülmüş şekilde **güçlüdür**.

---

## 2. Ne bulduk

### ① ⭐ Rastgele bir paket zaten terk edilmiş

- **İddia:** Rastgele seçilmiş bir PyPI paketi **medyan 2,3 yıldır** güncellenmemiştir. %54,2'sinin son sürümü 2 yıldan eskidir.
- **Neye dayanıyor:** **Kendi ölçümümüz** — 857.893 projelik tam indeksten seed'li rastgele örneklem, n = 478 geçerli, ±4,5 puan.
- **Ne kadar güveniyoruz:** Yüksek. Bu, oturumun en güçlü birincil verilerinden biri; kapalı yayıncıların etrafından dolaşıp ham registry'den hesaplandı.
- **Ne yapmamız gerekiyor:** *"PyPI'da paket var"* cümlesini bilgi saymayı bırak. **Neredeyse sıfır bilgi taşıyor.**
- → `tech-stack §2.1`

### ② ⭐ İndirme sayısı gerçekten öngörüyor — ama toplu düzeyde

- **İddia:** İlk 500 indirmedeki paketlerde 2 yıldan uzun terk oranı **%8,6**; rastgelede **%54,2**. Gradyan monotonik, oran **6,3 kat**.
- **Neye dayanıyor:** Kendi ölçümümüz, 4 katman × 500 paket.
- **Ne kadar güveniyoruz:** Agregaya yüksek. **Paket başına düşük:** bu bir **dağılım** iddiasıdır, garanti değil. Antitez haklı karşı örnekler verdi — `moment.js` bakım moduna geçtiği hâlde indirmeleri devasa kaldı; `request` deprecated ilan edildikten sonra yıllarca yüksek kaldı (**ekosistem ataleti**). Bu örnekler doğrulanmadı ama mekanizma bizim kendi bulgumuzla uyumlu.
- **Ne yapmamız gerekiyor:** *"Top-500'de kal"* kuralını kullan — ama tek bir paket için *"indirmesi yüksek, demek ki bakımlı"* deme.
- → `tech-stack §2.2` · `§3.4 ④`

### ③ Yıldız ölçülmüş şekilde bozuk

- **İddia:** Manipülasyonla işaretlenen depoların **%81,4'ünde yıldızların en az %90'ı sahtedir**. 2024 Temmuz zirvesinde yıldız aktivitesi olan **tüm depoların %16'sı** bir kampanyayla ilişkiliydi.
- **Neye dayanıyor:** Ham replikasyon CSV'lerinden **kendi hesabımız**, artı yayımlanmış çalışma.
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** Yıldızı seçim kriteri olarak **hiç anma**. Bir AI/LLM deposunun yıldızının üçte ikisi satın alınmış olabilir.
- → `tech-stack §2.4`

**Analoji:** Yıldız, restoranın vitrinindeki "TripAdvisor 2019 Ödülü" plaketi gibi. İçeride kimsenin yemek yiyip yemediğini söylemiyor. İndirme sayısı ise mutfaktan çıkan tabak sayısı.

### ④ Kritik paketlerin yayın yetkisi tek hesapta

- **İddia:** En çok bağımlısı olan 1.000 npm paketinin **%41,3'ü tek bakımcılı**; **%17,8'i hem tek bakımcılı hem 2 yıldan durgun**.
- **Neye dayanıyor:** Kendi ölçümümüz, 220.469 paket.
- **Ne kadar güveniyoruz:** Yüksek — **ama ne ölçtüğüne dikkat.** Bu alan *yayın hesabı* sayar, **insan sayısı değil**. Tedarik zinciri riski için doğru metrik; *"kaç kişi bu kodu biliyor"* için **değil**.
- **Ne yapmamız gerekiyor:** Bağımlılık seçerken bakımcı sayısına bak, ama bunu bus factor sanma.
- → `tech-stack §2.3`

### ⑤ ⭐⭐ Alanın amiral gemisi kanıtı buharlaştı

- **İddia:** *"Hangi teknolojiyi seçtiğin ölçülebilir şekilde kaliteyi etkiler"* iddiasının **en çok atıf alan kanıtı**, bağımsız yeniden analizde büyük ölçüde geçersizleşti. 11 dilden yalnız **4'ü** anlamlı kaldı ve etki **"son derece küçük"**.
- **Neye dayanıyor:** İkincil kaynak (abstract katmanı) — orijinal çalışma, yeniden analiz, çürütme ve karşı çürütme.
- **Ne kadar güveniyoruz:** **Tartışma kapanmadı** ⇒ hüküm yok. Ama yön güvenilir.
- **Ne yapmamız gerekiyor:** *"Doğru dili/aracı seçmek kaliteyi belirler"* cümlesini kanıta dayandırma. Dayanacağı kanıt zayıfladı.
- → `tech-stack §3.3 ▲1`

### ⑥ Dolaşan yüzdelerin bir kısmı uydurma

- **İddia:** *"CNCF: %42'si monolite dönüyor"*, *"Gartner: %60'ı pişman"*, *"mikroservis göçlerinin %73'ü başarısız"*, *"teknik borç %287 ROI"*, *"COBOL göçlerinin %67'si başarısız"* — hiçbiri birincil kaynakta doğrulanamadı; hepsi içerik çiftliği sitelerinde dolaşıyor.
- **Neye dayanıyor:** Arama; birincil kaynak bulunamadı.
- **Ne kadar güveniyoruz:** *"Doğrulanamadı"*ya yüksek güven — bu **uydurma oldukları kanıtı değil**, ama kullanılamayacakları anlamına geliyor.
- **Ne yapmamız gerekiyor:** **KULLANMA.** Bunlar bir tartışmada elimize verilirse kaynak sorulur.
- → `tech-stack §3.2`

### ⑦ "Boring technology" folklor — ama sandığın sebepten değil

- **İddia:** *"Sıkıcı teknoloji seç"* tezi **yanlışlanabilir değildir**, çünkü savunucularının kendi itirafıyla *"neyin sıkıcı sayıldığı ekibin beceri setine göre değişir"* — tanım sonuca göre ayarlanabiliyorsa hipotez değildir.
- **Neye dayanıyor:** Tezin savunucularının kendi ifadeleri.
- **Ne kadar güveniyoruz:** Yüksek — **ve bu ayrım epistemolojik olarak kritik.**
- **Ne yapmamız gerekiyor:** Bu tezi *"kanıt bulunamadı"* diye reddetme; **test edilemez olduğu için** reddet. İkisi farklı şey. Aynısı "innovation token = 3" için de geçerli: **11 yıldır dolaşıyor, hiç test edilmemiş.**
- → `tech-stack §3.3 ▲2` · `§4`

### ⑧ Mimari kötü bir öğrenme ortamı — ama bu bizim çıkarımımız

- **İddia:** Güvenilir sezgi iki koşul birlikte sağlanınca oluşur: ortam düzenli olmalı **ve** geri bildirim hızlı ve belirsizlik içermemeli. Mimaride ikisi de yok — teknik borç **sistem ömrü mertebesinde** gecikmeyle tezahür ediyor, geri bildirim geldiğinde de **sonuç yanlılığıyla** kirli.
- **Neye dayanıyor:** İkincil kaynaklar + **bizim bileşimimiz**.
- **Ne kadar güveniyoruz:** ⚠️ **Bu raporun en çok yaslandığı önerme, aynı zamanda en az doğrudan desteklenen önermesidir.** Kahneman-Klein ölçütünü yazılım mimarisine formel uygulayan tek şey blog düzeyinde yorum. **Bu bir literatür bulgusu değil, bir çıkarımdır** — ve rapor bunu kendisi beyan ediyor.
- **Ne yapmamız gerekiyor:** Model C'nin tüm gerekçesi buna dayanıyor. İmzalarken bunu bilerek imzala.
- → `tech-stack §5.1`

**Yan bulgu, rahatsız edici:** 62 tıp değerlendirmesinin **%52'sinde** yıl arttıkça performans **düştü**. Yazılım paraleli: sanayide kazanılan deneyimin kaliteye ve üretkenliğe etkisi **yaklaşık sıfır**. Geri bildirim zayıfsa **yıl sayısı uzmanlık değildir**.

### ⑨ Tek vaka okumak işe yaramıyor — hayır, yarıyor

- **İddia (düzeltildi):** Kaynak analog yokken çözüm oranı ~%10; **tek** analogla ~%30; ipucuyla ~%80.
- **Ne değişti:** Rapor önce *"tek vaka okumak neredeyse transfer üretmiyor"* demişti. Bu **kendi rakamıyla çelişiyordu** — %30, %10'un üç katıdır. Antitez yakaladı.
- **Ne kadar güveniyoruz:** Rakamlara ikincil düzeyde güven; **düzeltmeye yüksek** (kendi metnimizden çıktı).
- **Ne yapmamız gerekiyor:** *"En az iki vaka"* kuralı **ayakta** — ama gerekçesi değişti: *"tek vaka işe yaramaz"* değil, **"şema ancak karşılaştırmayla doğar"**.
- → `tech-stack §5.3` · `§5.4 ④`

### ⑩ ⭐⭐ Bir cümlemiz tam tersine anlaşıldı — ve bu bir bulgudur

Yazdığımız cümle şuydu: *"Sonuç kapatılmadan okuma öğretici değildir."* Kastettiğimiz: **sonuç görünürken okumak öğretici değil.** Antitezin anladığı: *"sonuç açıklanmadan okumak öğretici değil"* — ve haklı olarak Harvard vaka yöntemini karşı örnek gösterdi, çünkü o yöntem sonucu **bilerek saklar**.

- **Ne kadar güveniyoruz:** İddia **ayakta**. Ama bu bir zafer değil, **bir arıza kaydıdır**: yetkin bir okuyucu, önerme formunda yazılmış bir cümleyi **tam tersine** anladı.
- **Sebep:** Olumsuzlamanın kapsamı Türkçe yüzeyde ayrışmıyor.
- **Ne yapmamız gerekiyor:** `¬` içeren her cümlede **kapsamı parantezle sabitle**. Yeni hâli: *"(Sonuç görünür durumdayken) okumak öğretici değildir; (sonuç kapatılarak) okumak — tahmin → aç → skorla — öğreticidir."*
- → `tech-stack §5.4 ⑥`

> **Bunun ilginç yanı:** lojik→kod raporu tam bu tuzağı anlatıyor — *"olumsuzlamanın kapsamı belirsiz olduğunda kod sessizce yanlış dalı seçer."* Burada kod değil **bir model** seçti, ve yanlış seçti. Yani o raporun uyardığı tuzak, **o rapor yazılmadan önce bizim kendi metnimizde zaten vardı.**

### ⑪ ⭐ Statik analiz araçları finansal hataları görmüyor

- **İddia:** Gerçekçi bir risk modülüne kasıtlı hatalar kondu. `ruff` varsayılan ayarla **7 hata** buldu — **hepsi hijyen** (kullanılmayan import, mutable default). `--select ALL` ile 32 hataya çıktı ama **gerçek hata artışı sıfır**. `mypy` varsayılan ayarla 1, strict ile 6 hata verdi — **gerçek hata sayısı sıfır**.
- **Ve asıl olan:** **look-ahead hatası (`df['ret'].shift(-1)`) iki modda da tespit edilmedi.**
- **Neye dayanıyor:** **Bu makinede kendi kontrollü ölçümümüz.**
- **Ne kadar güveniyoruz:** Yüksek — ölçüm kendi kurulumumuzda, adil koşulda (stub'lar kurulu).
- **Ne yapmamız gerekiyor:** `ruff` kullan ama **hata bulmasını bekleme**. Doğruluk kritik hatayı yakalayacak şey **~20 satırlık bir pytest**tir.
- → `tech-stack §6.2`

**Ve mypy'ın iki yüzü var:** tip notlu sınırlarda 4 gerçek hatanın **3'ünü yakaladı** (`DataFrame` yerine `float`, `str` yerine `int`, eksik return). Ama `df["clsoe"]` yazım hatasını **yakalayamadı** — ve veri biliminde hataların çoğu **DataFrame içindedir** ⇒ kapsama **yapısal olarak dar**.

### ⑫ ⭐ En yüksek değerli blok: Sharpe oranı yalan söyleyebilir

- **İddia:** Gerçek beceri **sıfırken** bile, 5 yıllık veriyle **45 varyant** denersen beklenen en yüksek in-sample Sharpe **1,00** çıkar.
- **Neye dayanıyor:** **İki bağımsız yöntem aynı sonucu verdi** — analitik formül (hesaplandı) ve Monte Carlo simülasyonu (saf gürültü, 200 tekrar). İki ondalık basamağa kadar örtüştüler; ve out-of-sample Sharpe **her zaman yaklaşık sıfır** çıktı.
- **Ne kadar güveniyoruz:** Çok yüksek — iki bağımsız yöntem, kendi hesabımız.
- **Ne yapmamız gerekiyor:** Bir backtest'in Sharpe'ı, **kaç varyant denendiği yazılmadan yorumlanamaz**. Bu, bir metin dosyası ve sıfır bağımlılıkla çözülür.
- → `tech-stack §6.6 R31-R32`

### ⑬ Veri sızıntısının ölçülmüş etkisi

- **İddia:** Ekonomik gerekçesi olmayan bir öznitelikle: naif k-fold **R² ≈ +0,85** verdi; purged k-fold aynı veride **R² ≈ −1,2** verdi. Tamamen öngörülemez bir hedefte bile naif yöntem **0,83–0,91** R² üretti — **saf gürültüde**.
- **Neye dayanıyor:** Kendi ölçümümüz (Binance BTC/USDT günlük).
- **Ne kadar güveniyoruz:** Yüksek. **Ama bir dürüstlük notu var:** sızıntı **her zaman felaket değil**. Aynı kaynakta 4.284 haneli bir veri setinde naif ile walk-forward arasındaki zamansal boşluk yalnız **%1,60**'tı; asıl ısıran sızıntı hane bazlıydı (%6,03).
- **Ne yapmamız gerekiyor:** **Kategorik korku değil, ölçüm.** Hangi bölmeye ihtiyacın olduğu ne üzerinde çalıştığına bağlı.
- → `tech-stack §6.6 R35-R36`

### ⑭ Naif look-ahead testi işe yaramıyor

- **İddia:** Klasik *"veriyi kes, sinyal değişiyor mu bak"* testi yazıldı ve **bilinen hatalı fonksiyonu yakalayamadı**. Sebep ölçüldü: kesme noktasında yalnız **1 satır** farklılaşabiliyor, ve eşiklenmiş bir sinyalde bu fark ~%50 olasılıkla tesadüfen aynı değere çöküyor.
- **Çalışan sürüm ölçüldü:** kesme noktasını **süpür**, boolean değil **ham float** karşılaştır, **NaN duyarlı** eşitlik kullan ⇒ **10/10 kesme noktasında yakalıyor**.
- **Ne kadar güveniyoruz:** Yüksek, kendi ölçümümüz.
- **Ne yapmamız gerekiyor:** Bu ~20 satırlık pytest, `ruff` ve `mypy`'ın **tamamen kör olduğu** hata sınıfını yakalıyor. **Yığının 1. sırasındaki madde bu.**
- → `tech-stack §6.6 R37`

### ⑮ MLflow tavsiyelerinin tamamı eskimiş

- **İddia:** MLflow 3.x **dosya deposunu kaldırdı**. `./mlruns` kullanmaya çalışırsan **istisna fırlatıyor**.
- **Neye dayanıyor:** Bu makinede ölçüldü (MLflow 3.14.0).
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** İnternetteki *"pip install mlflow, mlruns'a yaz, bitti"* tavsiyesinin **tamamı MLflow 2.x içindir ve geçersizdir**. Zaten almıyoruz: 90 paket / **611 MB** — bu, tüm bilimsel yığından (472 MB) **büyük**. Yerine **8 satır JSONL**, sıfır bağımlılık, koşum başına 0,006 saniye.
- → `tech-stack §6.4`

### ⑯ En sinsi yeniden üretilebilirlik hatası

- **İddia:** `PYTHONHASHSEED` sabitlenmezse `set` sıralaması **her koşumda değişir** — tüm RNG tohumları doğru olsa bile. İki ardışık koşumda hisse evreni sırası farklı çıktı.
- **Neye dayanıyor:** Kendi ölçümümüz.
- **Ne kadar güveniyoruz:** Yüksek — **ama kapsam daraltıldı**: bu, **hash sırasına duyarlı kod yolu içeren** koşumlar için geçerli. Saf numpy/pandas sayısal hattı bağımsız olabilir. Rapor önce *"hiçbir koşum"* demişti; koşul aslında **`set` kullanımıdır**.
- **Ne yapmamız gerekiyor:** `PYTHONHASHSEED=0` ve `set` yerine `sorted()`. **Dört satır.**
- → `tech-stack §6.5 R27` · `§6.9 ⑦`

---

## 3. Ne bulamadık

### Aradık, bulamadık — ve bu bir bulgudur

| Ne | Not |
|---|---|
| **"Innovation token" kavramının herhangi bir ampirik operasyonelleştirmesi** | Ne token sayısını kalibre eden ne sonuçla ilişkilendiren tek çalışma. **11 yıldır dolaşıyor, hiç test edilmemiş.** |
| **Technology Radar'ın retrospektif isabeti** | *"Adopt'a alınan blip'ler 5 yıl sonra ne oldu"* analizi ne üreticide ne üçüncü tarafta var. |
| **ATAM'ın kontrollü değerlendirmesi** | Uygulayan ile uygulamayan proje karşılaştırması yok. Yalnız uygulama vakaları. |
| **ADR'lerde gözlenmiş-sonuç alanı** | 13 şablonun **hiçbirinde** yok; literatürde de *"kararlar sonradan doğru çıktı mı"* sorulmamış. ⇒ **Özgün katkı alanı.** |
| **"Rakip/alternatif sayısına bak" kriterinin ölçümü** | Bu heuristiği inceleyen **hiçbir** çalışma yok. |
| **Lock-in'in nicel bedeli** | Switching cost'u *fiilen* ölçen (tahmin/anket değil) çalışma yok. Alanın kendi itirafı: çok az kurum ölçüyor. |
| **⭐ Tek kişilik ölçekte teknoloji seçimi** | Tüm ampirik literatür ya ekosistem ya kurumsal takım ölçeğinde. **Bu ailedeki en büyük kanıt boşluğu — ve Salih'in tam bulunduğu yer.** |
| uv deposunda sayısal benchmark | README yalnız bar grafiği görseli içeriyor; *"10-100x"* iddiası **kendi deposunda doğrulanabilir sayıya dayanmıyor**. |
| polars deposunda sayısal iddia | README yalnız *"very fast"*, *"one of the best performing"*. |

### **Arayamadık** — bunlar yokluk hükmü DEĞİL

| Ne | Neden |
|---|---|
| Tip ipuçlarının hata oranına etkisi üzerine ampirik literatür | **Arama bütçesi tükendi** ve akademik yayıncılar kapalıydı. Kendi ölçümümüz (⑪) **literatürün yerine geçmez**. |
| Bağımsız pandas-vs-polars sayıları (db-benchmark) | Barındıran adresler kapalıydı. Hem bağımsız hem satıcı rakamları **aranamadı** ⇒ kendi ölçümümüz bu boşluğu dolduruyor, ama tek ölçek (1,26M satır). |
| Notebook `%4` rakamının birincil doğrulaması | **Teyit edilmedi, üzerine inşa edildi** — bu ayrım kayda geçer. |
| "Kaç deneyden sonra manuel takip kırılır" eşiği | Aranamadı; **kestirim de verilmedi.** |
| Akademik rakamların **hiçbiri** birincil metinden değil | Tüm büyük yayıncılar 403 döndü ⇒ ondalıklar teyit edilmemiş sayılmalı, **yön** güvenilir. |

### Ölçüldü ama tek eksende

**polars** *"şimdi alınmaz"* hükmü **yalnız hız ekseninde** ölçüldü. Antitez ince bir yakalama yaptı: polars'ın asıl argümanı da hız değil **şema katılığı, lazy-evaluation'da erken tip hatası, null semantiği tutarlılığı** olabilir. Bu eksen **ölçülmedi** ⇒ hüküm ayakta ama *"ölçtük ve eledik"* demek yanlış olur.

---

## 4. Ne değişiyor

1. **KARAR GEREKİYOR (S1) — Model C.** Her yığın kararında önce tahmin ve olasılık yazılır, sonra kaynak açılır, Brier skorlanır.
   ⚠️ **İmzalarken bilmen gereken:** bu *"en iyi kanıtlı seçenek"* değil, **"tek uygulanabilir seçenek"**. Kalibrasyon eğitiminin **mimari karara transferi ölçülmemiştir**; GJP'nin %6-7 kazancı tahmin görevlerinde ölçüldü. İyi haber: L7 ve L15'in Brier deltası **tam olarak bu transferi ölçüyor** ⇒ model kendi varsayımını sınayacak biçimde kurulmuş. → `§7`
2. **Sürtünme eşiği zorunlu.** 921 deponun ~%50'sinde 5'ten az ADR kaydı var ⇒ pilot sonrası terk oranı yüksek. Öneri: **yalnız geri alması pahalı kararlar** tam protokole girer (publish / para / kişisel veri / pahalı geri alma / yön değişimi); altı Model B'nin üç sayısıyla geçilir. → `§7`
3. **KARAR GEREKİYOR (S4) — V67 yıldız yasağı.** Hiçbir kararda GitHub yıldızı kriter olarak anılmaz. Yerine: indirme sırası + son sürüm tarihi + bakımcı sayısı. Kural küçük, dayanağı ölçülmüş. → `§9`
4. **DS/ML yığını hazır — toplam 3,3 saniye kurulum, 26 satır yapılandırma:** nedensellik testleri (pytest) → deneme sayacı → uv → pandas/numpy/scipy → parquet → ruff → pytest → tohum disiplini → JSONL deney kaydı → notebook yalnız keşif. **Sırası önemli:** 1. sıradaki ~20 satırlık test, projenin doğruluğunu belirleyen tek katman. → `§6.7`
5. **Alınmayacaklar, gerekçeli:** MLflow/W&B (611 MB > tüm yığın), DVC (98 paket, değeri azalmış ama maliyeti karşılamıyor), poetry (uv aynı işi 0 bağımlılıkla), `mypy --strict` (başlangıçta %100 gürültü), `ruff --select ALL` (gerçek hata artışı 0), polars (şimdilik), papermill/jupytext/nbdev, Docker, backtrader/pyfolio/empyrical (**terk edilmiş**). → `§6.8`
6. **Yeni kural adayı (K10):** önerme formunda `¬` kullanılan her cümlede **kapsam parantezle sabitlenir**. ⑩'daki arızanın doğrudan sonucu. → `§0 düzeltme kaydı`
7. **A24 müfredatı hazır (L7–L15):** taban kalibrasyon → kör kata → zıt vaka çifti → karar arşivi → başarısızlık serisi → süreç-sonuç ayrıştırma → çapa kırma + premortem → dış görüş → yeniden kalibrasyon.
   ⚠️ **Müfredatın kendi zayıflığı beyan edilmiş:** L10 ve L11'in mimari karar kalitesini artırdığına dair **ölçülmüş kanıt yok**; DONE'ları bu yüzden *"kavrayış"* değil **artefakt sayısı** olarak tanımlandı. L12'nin rubriği de **kendi imalatımız** — valide edilmiş bir rubrik bulunamadı. → `§7.1`

---

## 5. Kontrol

*Bu raporu okuduktan sonra şu üç soruyu cevaplayabiliyor musun?*

1. **Bir bağımlılık seçeceksin. Hangi üç sayıya bakarsın, hangi sayıya hiç bakmazsın — ve baktığın üç sayıdan çıkardığın sonuç neden tek bir paket için garanti değil?**

2. **Bir backtest sana Sharpe 1,0 gösterdi. Bu sayıyı yorumlayabilmen için hangi tek bilgiye ihtiyacın var, ve o bilgi olmadan Sharpe 1,0 neden hiçbir şey ifade etmiyor?**

3. **Model C'yi imzalarken kabul ettiğin ölçülmemiş varsayım ne, ve model bu varsayımı nasıl kendi kendine sınayacak biçimde kurulmuş?**
