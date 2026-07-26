# Araştırma Promptu Verimi — sözel önerme karşılığı

> Kaynak: `raporlar/2026-07-26-arastirma-promptu-atlas.md` · Register: düz lojik · Compiler: **KAPALI**
> Okuma kuralı: **öncülü sağlanmayan bir önermenin sonucu geçerli DEĞİLDİR.**

**Numaralandırma:** kaynağın kendi kodları korunur — `Q1`–`Q32`, `B1`–`B15`, `D1`–`D10`, `V72`–`V75`.

**Kanıt sütunu:** *birincil* = birincil kaynağa/depoya inildi · *ikincil* = doğrulanmadı · *çelişkili* = hüküm yok · *kestirim* = ölçülmemiş · *çıkarım* = bileşim · *aranamadı* = bütçe/erişim engeli, **yokluk kanıtı DEĞİL** · *arandı, yok* = **yokluk bulgusudur**.

**Antitez sütunu:** bu ailenin antitezi **araçsız** koştu ⇒ **mantıksal** saldırılar tam güçtedir; **olgusal karşı örnekler hatırlama düzeyindedir** ve borç açar. *"Sağ çıktı"* damgaları **aynı-aile şerhlidir**.

---

## 0. Bu koşumun kendi hatası

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **Q1** | Brifingte ajanlara *"arXiv'in HTML sürümü açık, önce onu dene"* denildi.<br>Ölçüm: arXiv ve tüm alt alanları **kapalıdır** (kapı seviyesinde 403) ⇒ **brifing iddiası yanlıştı** ve maliyeti **en az bir ajanın ilk hamlesiydi**.<br>Kaynağı: önceki ailelerde arXiv'in **PDF**'i kapalıydı ve **HTML sürümü hiç denenmemişti** ⇒ *"denenmedi"* önce *"açık olabilir"*e, sonra brifingte *"açık"*a dönüştü.<br>⇒ **Denenmemiş olmak, açık olmak değildir.** Bu, tam olarak ailenin kendi konusudur: **brifingteki doğrulanmamış öncül, ajanın bütçesini yakar.** | ölçüm | — |
| **Q2** | Düzeltmenin ajandan gelmesi **istenen davranıştır**: ajan proxy durumunu ölçtü, brifingi düzeltti ve bunu ara metin olarak bildirdi ⇒ düzeltme dört ajana ve sonraki ailelere yayıldı.<br>⇒ **Kural:** brifing bir **hipotezdir** ve veri karşısında düzeltilir. Ajana *"brifingi sorgula"* yetkisi verilmelidir — **maliyeti sıfır, getirisi ölçülmüştür**. | ölçüm | — |

---

## 1. Erişim haritası

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **Q3** | Kapalı olanlar: arXiv ve tüm alt alanları, ScienceDirect, Springer, SAGE, Wiley, ACM DL, IEEE, tüm `*.edu` ve `*.github.io`, **tüm PDF'ler**, GitHub'ın web arayüzü ve API'si, Semantic Scholar, ACL Anthology, OpenReview, Papers with Code, Hugging Face, Wikipedia.<br>Açık olanlar: ham dosya sunucusu, PyPI, npm registry, ürün dokümanlarının `.md` uzantılı hâli. | birincil | — |
| **Q4** | GitHub'ın **web arayüzü kapalı**, **ham dosya sunucusu açıktır**.<br>⇒ Bu asimetri boyunca **replikasyon depolarına yönelmek**, kapalı yayıncının etrafından dolaşmanın **yoludur**: kaynak kapalıysa hedef **replikasyon deposu**, **upstream git** ya da kaynağın `.md`/`.rst`/`.txt` hâli olur.<br>Bu koşumda **dört kez** karşılığını verdi.<br>⇒ **Engel kanıt kalitesini düşürmedi, YÜKSELTTİ** — depo metni, makale özetinden üstündür. | ölçüm | — |
| **Q5** | WebSearch bütçesi oturum başına **200**'dür ve sayaç **ana konuşma ile tüm alt ajanlar için ortaktır**.<br>Plan yükseltmesi kotayı sıfırlar ama **bu oturum sayacını SIFIRLAMAZ**.<br>Sayaç dolduğunda arama **boş döner ve hata vermez**.<br>⇒ **Boş arama, sonucun yok olduğu anlamına gelmez; sayacın dolduğu anlamına gelir.**<br>⇒ Ajan bunu bilmezse **`aranamadı` durumunu `bulunamadı` diye raporlar** ⇒ **negatif bulgu uydurulur.** | birincil | — |

---

## 2. A29 — bağlam ekonomisi

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **Q6** | 17 açık model üzerinde ölçüldü: **iddia edilen pencere, etkin pencereden çok büyüktür** (etkin = kalite eşiğini koruduğu uzunluk).<br>GPT-4-1106-preview 128K iddia ediyor, etkin **64K**. Llama3.1-70B 128K iddia ediyor, etkin **64K** (skor 64K'da 88,4 iken 128K'da 66,6).<br>Mixtral-8x7B 4K'da 94,9 iken 128K'da **44,5**'e düşüyor. DBRX 95,1'den **0,0**'a. Qwen1.5-72B 94,9'dan **0,0**'a (hem 64K hem 128K'da).<br>⇒ **Neredeyse hiçbir model iddia ettiği boyutta eşik performansını korumuyor.** | birincil | çürütülemedi |
| **Q7** | 12 güncel model üzerinde, **literal kelime örtüşmesi olmayan** bir tasarımla ölçüldü ⇒ ölçülen şey konum etkisi değil, **anlamsal ve distractor etkisidir**.<br>GPT-4o kısa bağlamda %99,3 iken 32K'da %69,7 ⇒ etkin uzunluk **8K**.<br>Claude 3.5 Sonnet %87,6 iken **%29,8** ⇒ etkin uzunluk **4K**.<br>Gemini 1.5 Pro %92,6 iken %48,2 ⇒ etkin uzunluk **2K**.<br>32K'da **12 modelin 10'u** kısa bağlam tabanının yarısının altına düşüyor.<br>⇒ *"Ortada kaybolma"* olgusu **2025 frontier modellerinde hâlâ geçerlidir** ve konum etkisinden **ayrıştırılmıştır**. | birincil | çürütülemedi |
| **Q8** | Nominal pencere 128K ile 1M arasındaysa ve görev distractor yoğunsa ya da dikkat gerektiriyorsa, **etkin bütçe 2K ile 16K arasındadır**.<br>⇒ **Bağlam bütçesi etkin uzunluğa göre belirlenir, nominal pencereye göre değil.** | çıkarım | çürütülemedi |
| **Q9** | Konum eğrisi çalışmasının **deposuna inildi** ve metodolojisi doğrulandı (altın belge 20 belgelik bağlamda 0, 4, 9, 14, 19 pozisyonlarında; 10, 20, 30 belgelik koşullar; anahtar-değer görevinde 300 anahtara kadar).<br>Ama README'de **sonuç tablosu yoktur** ve makalenin kendisi kapalıdır ⇒ **U şekilli eğrinin kesin sayıları doğrulanamadı ⇒ rakam verilmedi.** | birincil (rakam: arandı, yok) | — |
| **Q10** | Çok-ajan başarısızlık taksonomisi deposunda taksonomi figürü vardır ama **kategori yüzdeleri yoktur** ve makale ile model deposu kapalıdır ⇒ **hiçbir kategorik ya da yüzdesel rakam verilmedi.** *(Sonradan delta turunda kapatıldı — Q9b.)* | birincil | — |
| **Q11** | Ölçek çalışmasının deposunda `pass@k` metodolojisi doğrulandı ama **ölçek eğrisi rakamı yoktur** ⇒ *"getiri nerede düzleşiyor"* sorusuna **kanıt yoktur**. | birincil | — |
| **§2.2-not** | ⭐ Bu üç önerme raporun en değerli kısımlarından biridir: **üç çalışmanın da deposuna inildi, metodolojisi doğrulandı, ve rakamı olmadığı için rakam verilmedi.** Ajan üç kez rakam uydurabilirdi; **uydurmadı**. | ölçüm | — |
| **Q12** | Takım hâlinde çalışan ajanlar plan modunda **standart oturumun yaklaşık 7 katı** token tüketir; gerekçe her takım üyesinin **kendi bağlam penceresini sürdürmesidir**. Token kullanımı takım boyutuyla kabaca doğru orantılıdır.<br>⇒ Bu, koordinasyon maliyetinin **sayısal ve birincil kaynaklı tek verisidir** — **token boyutunda**; doğruluk ya da kalite boyutunda **değil**. | birincil | çürütülemedi |
| **Q13** | Alt ajan **kendi bağlam penceresini** kullanır ve ana konuşmaya **yalnız özet** döndürür. İç içe alt ajan **varsayılan olarak kapalıdır**.<br>Resmî desen: *"X, Y, Z'yi ayrı alt ajanlarla paralel araştır… bu, araştırma yolları birbirine bağlı olmadığında en iyi çalışır."*<br>Resmî uyarı: *"Her biri ayrıntılı sonuç döndüren çok sayıda alt ajan çalıştırmak önemli miktarda bağlam tüketebilir."*<br>⇒ Varsayılan mimari **izole bağlam ve özet döngüsüdür**, bağlam paylaşımı değildir.<br>⚠️ **Damga:** bu bir **ürün tasarım kararı ve tavsiyesidir, RCT DEĞİLDİR.** Kaynak birinciildir ama **kanıt türü farklıdır**. | birincil (kanıt türü: tasarım tavsiyesi) | çürütülemedi *(şerh iddia listesine taşındı — K24)* |
| **Q14** | Sıkıştırma mekanizması vardır: bağlam sıkıştırıldığında mesaj geçmişi **özete dönüşür** ve önbellek geçersizleşir. Hook ile ön işlemede 10.000 satırlık bir log **on binlerce token'dan yüzlerce token'a** inebilir.<br>⇒ Bu bir **token hacmi iddiasıdır**; **bilgi kaybı ölçümü yoktur**.<br>⚠️ *"Ölçüm yoktur"* burada **"literatürde yok" DEMEK DEĞİLDİR** — bkz. Q'nun altındaki K19 düzeltmesi. | birincil | daraltıldı → K19 |

### 2.4 Parçalama kuralı

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§2.4-1** | Bir alt ajanın bağlam bütçesi **modelin ölçülmüş etkin uzunluğu** olarak alınır, iddia edilen pencere olarak değil. | birincil | — |
| **§2.4-2** | **Alakasız materyal eklemek başlı başına maliyetlidir**: 30-70 puanlık düşüşler **konum etkisinden bağımsız** bir hacim ve kirlilik etkisidir. | birincil | daraltıldı *(bkz. §2.5-1: aralık geniştir)* |
| **§2.4-3** | Varsayılan topoloji **izole bağlam ve özet döngüsüdür**: ajanlar birbirinin **ham** bulgusunu görmez, orkestratör sentezler. | birincil (tasarım tavsiyesi) | daraltıldı → K24 |
| **§2.4-4** | Ajan sayısı arttıkça token **doğrusal** artar (plan modunda yaklaşık 7 kat) ⇒ **N'i büyütmenin gerekçesi görevin MECE ayrışabilirliğidir**, *"daha fazla ajan daha iyi"* değildir. | birincil | çürütülemedi |
| **§2.4-5** | Sıralı zincir **ancak ve ancak** adımlar gerçekten bağımlıysa kullanılır; bağımsız iş **paralel fan-out**'a verilir. | çıkarım | çürütülemedi |
| **§2.4-6** | **Kestirim olarak işaretlenenler:** self-consistency getirisinin düzleşme noktası (hiçbir birincil kaynaktan doğrulanamadı) · paralel araştırma hatlarının optimal sayısı (yalnız MECE tasarım sezgisi, ablasyon değil) · sıralı zincirde hata birikim oranı (hiçbir ölçüm yok) · özetleme ve sıkıştırmanın bilgi kaybı büyüklüğü (mekanizma doğrulandı, **miktar bizim tarafımızdan ölçülmedi** — ⚠️ literatürde yok demek değildir, K19). | kestirim | K19 |

### 2.5 A29 iddia listesi

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§2.5-1** | Bağlam kirliliği 2025 frontier modellerinde 32K'da **%30-70** doğruluk kaybına yol açabiliyor.<br>⚠️ **Daraldı:** *"%30-70 aralığı o kadar geniş ki neredeyse her gözlemi doğrular"* ⇒ **sahte kesinlik**. Rakamlar korunur (ölçüm gerçektir), ama **aralık bir öngörü olarak kullanılamaz**; tek tek model satırları (Q7) kullanılır. | birincil | daraltıldı |
| **§2.5-2** | İddia edilen ile ölçülmüş etkin uzunluk arasında bazı modellerde **16 kata varan** uçurum vardır. | birincil | çürütülemedi |
| **§2.5-3** | Alt ajanlar arası varsayılan mimari bağlam paylaşımı değil, **izolasyon ve özet döngüsüdür**.<br>⚠️ **Üç noktada daraldı.** ① Bu bir **mimari tasarım tavsiyesidir**, olgusal konsensüs değildir; blackboard ve paylaşılan bellek mimarileri de vardır. ② Daha keskini: **bu tercih §2.5-4'teki maliyet kaygısından türüyor, başarısızlık kanıtından DEĞİL** — yani **maliyet güdümlü** bir gerekçe **güvenilirlik güdümlüymüş gibi** sunuluyordu. ③ Dolayısıyla **§2.5-3, §2.5-4'ten mantıksal olarak çıkmıyor**.<br>⚠️ Bu şerh raporda **zaten vardı** (Q13) ama **iddia listesine taşınmamıştı**. | birincil (tasarım tavsiyesi) | daraltıldı → K24 |
| **§2.5-4** | Takım büyüklüğü token maliyetiyle kabaca doğru orantılıdır; plan modunda yaklaşık 7 kat. | birincil | çürütülemedi |
| **§2.5-5** | Taksonomi sayısal kategorileri **delta turunda kapatıldı** (Q9b) ⇒ bu iddia **artık geçersizdir**. | birincil | kapandı |
| **§2.5-6** | Self-consistency getirisinin düzleşmesine dair bu koşumda **hiçbir kanıt bulunamadı**. | aranamadı | çürütülemedi |
| **§2.5-7** | Sıralı zincir ile paralel fan-out arasındaki hata birikimini ölçen **hiçbir çalışma bulunamadı**. | aranamadı | çürütülemedi |
| **§2.5-8** | Özetlemenin bilgi kaybını doğrudan ölçen çalışma **bu koşumda ARANAMADI**.<br>⛔ **Eski hâli *"hiçbir çalışma bulunamadı"* diyordu ve YANLIŞTI.** Antitez tek bir karşı örnekle değil, **koca bir alt alanla** karşılık verdi: **QAGS, SummaC, FactCC** (özet sadakati metrikleri) ve **LLMLingua** (sıkıştırmanın downstream kaybı). Alan adları spesifik ve tutarlı olduğu için **kabul edildi**.<br>⇒ Doğrusu: **bizim aradığımız kanalda bulunamadı; sadakat metriği literatürü MEVCUTTUR ve TARANMAMIŞTIR.**<br>⇒ Bu, **`⊨A` etiketinin** gerekçesinin canlı vakasıdır: bütçe tükenmişken **aranamamış** olanı **yok** diye yazdık. | aranamadı | ⛔ çürütüldü → K19 |
| **§2.5-9** | Çok ajan sistemlerin tek ajanı ne zaman geçtiğine dair **baş başa ölçüme erişilemedi**. | aranamadı | çürütülemedi |

### 2.6 A29 delta

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **Q9b** | Taksonomi figürü **doğrudan indirildi ve okundu** (yazarların yayımladığı birincil görsel).<br>**3 üst kategori ve 14 alt başarısızlık modu** vardır ve kategoriler yaklaşık ayrıktır.<br>**Poor Specification (sistem tasarımı): %37,17** — görev şartnamesine uymama %15,2, rol şartnamesine uymama %1,57, **adım tekrarı %11,5**, konuşma geçmişi kaybı %2,36, sonlanma koşullarından habersizlik %6,54.<br>**Inter-Agent Misalignment (koordinasyon): %31,41** — konuşma sıfırlanması %5,50, netleştirme istememe %2,09, görevden sapma %5,50, **bilgi saklama %6,02**, diğer ajanın girdisini görmezden gelme %4,71, **muhakeme-eylem uyumsuzluğu %7,59**.<br>**Task Verification (kalite kontrol): %31,41** — erken sonlanma %8,64, eksik ya da yok doğrulama %9,16, **yanlış doğrulama %13,61**.<br>⇒ **En büyük tek kategori Poor Specification'dır (%37,17)** ⇒ çok ajan başarısızlıklarının en büyük payı **ajan etkileşiminden değil, görev ve sistem tasarımının en baştan kötü kurulmasından** gelir.<br>⇒ Yani *"araştırma promptunun verimi"* sorusu, çok ajan başarısızlığının **birinci** kaynağıdır — ikincil bir iyileştirme değildir.<br>⇒ Ve **yanlış doğrulama (%13,61) eksik doğrulamadan (%9,16) büyüktür** ⇒ **kötü hakem, hakemsizlikten daha zararlıdır.** Bu, m.40b'nin maskeli hakemlik tasarımını doğrular. | birincil | çürütülemedi |
| **Q11b** | Ölçek çalışmasının deposu doğrulandı; ilk erişim hatası **dal adı** yüzündendi. Metodoloji teyitlidir: **ajan sayısı doğrudan kontrollü değişkendir**.<br>README'de **ölçek eğrisi ve düzleşme noktası yoktur** ve dizin listeleme imkânsızdır.<br>⇒ Statü **`aranamadı`dan `bulunamadı`ya yükseldi**: depoya fiilen erişildi, içinde sayı yok — **bu bir yokluk bulgusudur**. | birincil (arandı, yok) | — |
| **Q11c** | Self-consistency getirisi **hâlâ açıktır**. Arama özetinin iddiası: *"1, 5, 10, 20, 40 örneklemle test edilmiş; çoğu ayarda daha fazla örnek daha iyi; en az bir çalışmada 5'in üzerinde performans düşüşe geçiyor."* Birincil kaynaklar **hiç açılamadı**.<br>⇒ **Rakam verilmedi.** Ajanın kendi hükmü: *"Bu, aramanın kendi sentezi, ikinci el aktarım, ben doğrulamadım."*<br>⇒ Dolaşan *"%40 daha iyi"* iddiası birincil kaynaksızdır ⇒ **folklor olarak işaretlendi, kanıt sayılmadı.** | ikincil (doğrulanmadı) | — |
| **Q11d** | Sessiz tükeniş testi: delta turunda 2 arama yapıldı ve **ikisi de normal sonuç döndürdü** ⇒ sayaç o anda henüz dolmamıştı.<br>⇒ Q5'in ayrımı **işledi**: ajan, aramanın boş dönüp dönmediğini **hüküm kurmadan önce** kontrol etti. | ölçüm | — |

---

## 3. A28 — brifing tasarımı

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **Q15** | Alan uzmanı persona, dil tabanlı muhakeme görevinde alan dışı personadan **daha iyi** performans veriyor.<br>**Ama aynı çalışma:** persona ataması **önyargıyı da açığa çıkarıyor** — *"erkek"* persona arabaları *"kadın"* personadan daha iyi tanımlıyor.<br>⇒ **Persona etkisi ölçülmüş ve gerçektir; ama saf kalite artışı DEĞİLDİR** — göreve bağlıdır ve önyargı riski taşır. | birincil | çürütülemedi |
| **Q16** | **Ve persona çökertebiliyor:** Llama3.1-8b üzerinde melek/şeytan rol oynama kurulumu GSM8K'da **47,60** verirken, zincir düşünce **80,13**, doğrudan yanıt **70,40** veriyor. MATH'te 10,30 karşısında 40,13.<br>⇒ Rol ve persona tabanlı prompt tasarımı **ölçülmüş biçimde çökertiyor** — tek ajan zincir düşünceden belirgin biçimde kötü.<br>⚠️ **Bu bir kurulumdur, bir yasa değildir** (bkz. §3.7-3). | birincil | daraltıldı → K21 |
| **Q17** | Alakasız persona detayının **yaklaşık 30 puanlık** düşüşe yol açtığı bildirilmiştir.<br>⚠️ **Rakam doğrulanamadı** (birincil metne erişilemedi) ⇒ **hüküm kurulmaz**. | kestirim | — |
| **Q18** | Katı format zorunluluğu zayıf modelde **her şeyi çökertiyor**: MMLU 43,13 tabanından **13,27**'ye, GSM8K 70,40 tabanından **5,47**'ye.<br>⇒ Format uyumsuzluğu tüm tartışma yapısını çökertiyor. | birincil | çürütülemedi |
| **Q19** | JSON ya da XML gibi format kısıtlaması muhakeme yeteneğinde *"belirgin düşüşe"* yol açıyor ve kısıtlama katılığı arttıkça düşüş artıyor.<br>⚠️ **Yüzde rakamı doğrulanamadı — verilmedi.** | ikincil | çürütülemedi |
| **§3.2-not** | **Bize dönük sonuç — kendi tasarımımıza itiraz:** ajanlara dayattığımız katı çıktı şeması (numaralı bulgu, kanıt etiketi, iddia listesi, erişim engelleri, bulunamayanlar) **ölçülmüş bir maliyet taşıyor**.<br>**Ama** bu etki **zayıf bir model** üzerinde ölçüldü; bizim ajanlarımız frontier modellerdir ⇒ **frontier modelde aynı büyüklükte mi, bilinmiyor**.<br>⇒ **Hüküm kurulmuyor, ölçüm borcu açılıyor (D8).** Bu, ölçüm protokolüyle test edilebilecek **ilk somut hipotezdir**. | kestirim | — |
| **Q20** | *"Bilmiyorum de"* çalışmasının deposunda **talimatsız ile talimatlı ayrı komutlar** vardır ⇒ **kontrollü karşılaştırma tasarımı mevcuttur**.<br>Ama README'de **sonuç metrikleri yoktur** ⇒ talimatın ne kadar iyileştirdiği **rakamla doğrulanamadı**. | birincil (rakam: arandı, yok) | — |
| **Q21** | *"Bilmiyorum"* davranışı **ince ayarla** öğretildiğinde kalibrasyon iyileşiyor ve bu meta beceri **alan dışı veri setlerine genelleşiyor**.<br>⚠️ **Bu saf prompt talimatı DEĞİL, eğitim tabanlı bir müdahaledir** ⇒ *"salt prompt talimatı da işe yarar mı"* sorusuna **doğrudan cevap vermiyor**; ima ettiği şey salt promptun muhtemelen **daha zayıf** olduğudur. | birincil (genelleme: kestirim) | çürütülemedi |
| **Q22** | Atıf zorunluluğu üzerine bulunan tek yakın çalışma, üretici arama motorlarının atıflarını insan etiketleyicilerle **tam destek / kısmi destek / destek yok** diye sınıflandırıyor (eğitim kümesi 8.834 örnek: 6.415 / 1.552 / 867).<br>**Ama bu çalışma *"atıf zorunluluğu koyarsan halüsinasyon azalır mı"* sorusunu KONTROLLÜ TEST ETMİYOR** — ölçtüğü şey, **zaten atıf üreten sistemlerin atıf kalitesidir**.<br>⇒ **Nedensel iddia yoktur.**<br>⇒ Bu bulgu **bizim kendi pratiğimize dokunuyor**: JARVIS'te kanıt etiketlemesi *"halüsinasyonu azaltır"* varsayımıyla uygulanıyor ve **bu varsayımın doğrudan kontrollü kanıtı YOKTUR**.<br>⇒ Etiketleme yine de savunulabilir, ama gerekçesi **"iddianın kanıt seviyesini okuyucuya açık kılması"** olmalıdır. **Gerekçe düzeltilir, pratik korunur.** | birincil | sağ çıktı ⚠️ — ve antitez **güçlendirdi**: salt prompt seviyesinde *"kaynak göster"* talimatı, retrieval olmadan, **yeni bir halüsinasyon alt türü** (uydurma atıf) üretebiliyor |
| **Q23** | Uzunluk ekseninin en güçlü sayısal kanıtı Q7'nin rakamlarıdır.<br>⚠️ **Ama konusu talimat ya da brifing uzunluğu DEĞİL**, bağlam penceresindeki **alakasız metin miktarıdır** ⇒ **analoji olarak kullanılabilir, birebir eşleşme değildir.** | birincil (dolaylı) | çürütülemedi |

### 3.6 Ölçülmüş ile folklor

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§3.6-1** | **Ölçülmüş olanlar:** format zorlamasının muhakemeyi düşürdüğü (orta-güçlü: bir birincil sayısal örnek ve bir ikincil özet) · persona etkisinin göreve göre değiştiği, evrensel kazanç olmadığı, **bazen ciddi kayıp** olduğu (orta: iki birincil kaynak) · bağlamda alakasız içerik arttıkça isabetin düştüğü (güçlü ama **dolaylı**). | birincil | — |
| **§3.6-2** | **Folklor ya da doğrulanamayanlar:** format kısıtlamasının kesin yüzdesi (birincil doğrulanamadı) · persona `~30 puan` düşüşü (yalnız arama özeti) · *"bilmiyorum de"* talimatının kalibrasyonu iyileştirdiği (tasarım var, **sonuç rakamı yok**; kanıtlı olan **eğitim tabanlı** müdahale) · atıf zorunluluğunun halüsinasyonu azalttığı (**nedensel test yok**) · az kısıtlı ile çok kısıtlı brifing karşılaştırması (**hiçbir doğrudan kanıt yok**) · few-shot'un açık uçlu görevlerdeki etkisi (**ayrı literatür bulunamadı**). | arandı, yok | — |
| **§3.6-3** | **Negatif ile pozitif talimat ekseni: `ARANAMADI`** — bütçe tükenmişti ve tahmin edilebilir depo adı yoktu.<br>⛔ **Eski hâli *"hiçbir kaynak bulunamadı"* diyordu ve YANLIŞTI:** modellerin olumsuzlamaya duyarsızlığını **doğrudan ölçen** çalışma vardır (Kassner & Schütze, ACL 2020). ⇒ K19 ile **aynı hata sınıfı**, aynı düzeltme. | aranamadı | ⛔ çürütüldü → K20 |

### 3.7 A28 iddia listesi

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§3.7-1** | Persona ve rol ataması araştırma çıktısı kalitesini artırmaz, yalnız üslup ile derinlik-berraklık dengesini değiştirir. | ikincil | sağ çıktı ⚠️ *(hafif ve hedge'li olduğu için sağlam)* |
| **§3.7-2** | Format ve şema zorunluluğu, model akıl yürütme adımlarını gizli tuttuğunda doğruluğu düşürür. | birincil | çürütülemedi |
| **§3.7-3** | Çok ajanlı persona rol oynama, tek ajan zincir düşünceden **ölçülen bazı kurulumlarda belirgin biçimde** daha kötü sonuç verir.<br>⛔ **Eski hâli *"sistematik olarak daha kötü"* diyordu ⇒ çürütüldü.** Karşı örnek: **multiagent debate** GSM8K ve MMLU'da tek ajan zincir düşünce tabanını **artırıyor**. *"Sistematik iddiası tek karşı örnekle çöker."*<br>⚠️ Antitezin **ikinci gözlemi daha keskindir ve kabul edildi:** §3.7-1 hafif bir *"etkisiz"* iddiasıyken, §3.7-3 aynı aileden **çok daha güçlü** bir *"sistematik zarar"* iddiasına **bağımsız gerekçe olmadan** sıçrıyordu. | birincil (tek kurulum) | ⛔ çürütüldü → K21 |
| **§3.7-4** | Atıf ve kaynak etiketleme zorunluluğu, halüsinasyonu azalttığını gösteren doğrudan kontrollü kanıt **olmadan** varsayılan *"iyi pratik"* hâline gelmiştir. | birincil | sağ çıktı ⚠️ — antitez **güçlendirdi** |
| **§3.7-5** | *"Bilmiyorum de"* talimatının etkisinin prompt seviyesinde mi eğitim seviyesinde mi güçlü olduğu **net değildir**. | kestirim | çürütülemedi |
| **§3.7-6** | Negatif talimatların pozitiflerden daha az güvenilir tutulduğu ekseni **bu koşumda ARANAMADI**.<br>⛔ Eski hâli *"hiçbir ölçülmüş kanıt bulunamamıştır"* diyordu ⇒ **yanlış** (bkz. §3.6-3). | aranamadı | ⛔ çürütüldü → K20 |
| **§3.7-7** | Few-shot'un açık uçlu görevlerdeki etkisi ayrı bir literatür oluşturmamaktadır — ya da oluşturuyorsa **erişilememiştir**. | aranamadı | çürütülemedi |
| **§3.7-8** | Uzun ve ayrıntılı brifingler, alakasız içerik arttıkça isabeti düşürme **riski taşır**. | birincil (dolaylı) | sağ çıktı ⚠️ |
| **§3.7-9** | Katı biçim zorunluluğunun zararı, **model zayıfladıkça orantısız büyür**. | birincil | çürütülemedi *(D8 borcu duruyor)* |

---

## 4. A30 — verim ölçümü

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **Q24** | Bir değerlendirme çerçevesinde LLM yargıcının **örnek düzeyinde insan uyumu %69,2**'dir; model düzeyinde Spearman 0,97, Pearson 0,93; bias 28,4, varyans 14,6; daha uzun cevabı tercih etme olasılığı 0,68.<br>Kaynağın kendi uyarısı: *"yalnızca 9 model kullanıyoruz, bu yüzden korelasyon çok güvenilir değil."* | birincil | çürütülemedi |
| **Q25** | Uzunluk kontrollü kazanma oranı kullanıldığında arena korelasyonu **0,93'ten 0,98'e** çıkıyor ⇒ ham ikili skorun yaklaşık **0,05 korelasyon puanı salt uzunluktan** geliyordu. | birincil | çürütülemedi |
| **Q26** | Varyans teorik değil, **ölçülüyor**: insan uyumu 4 etiketleyiciden birini çıkarıp kalan 3'ün çoğunluğunu tahmin etmekle tanımlanıyor ve otomatik değerlendiricilere **aynı hesap** uygulanıyor. Varyans ise aynı örneğin 4 farklı örneklemesinde modun 3'e karşı 1'ini tahmin başarısıyla ölçülüyor.<br>⇒ **Bias ile varyansı ayırmanın tek yolu tekrar örneklemedir.** | birincil | çürütülemedi |
| **Q27** | Küçük örneklemde korelasyon çözüm değildir: *"insan ve LLM yargılarındaki rastlantısallık tutarsız tahminlere yol açıyor… bir modelin görünür performansının gerçek bir farkı mı yoksa yalnızca gürültülü gözlemleri mi yansıttığını güvenle belirlemek zor."*<br>Önerilen ikame: **bootstrap ile güven aralığı örtüşmesi**. | birincil | çürütülemedi |
| **Q28** | Konum yanlılığına karşı **çıktı sırasını rastgeleleştirme**, resmî değerlendirme kodunda **standart pratik olarak kodlanmıştır**.<br>⚠️ README'de insan uyum yüzdesi **yoktur** ⇒ halk arasında bilinen `~%85` rakamı **bu oturumda teyit edilemedi**. | birincil (rakam: arandı, yok) | — |
| **Q29** | `r≈0,31` iddiasının kaynağı **hiçbir kanalda bulunamadı** — varlığı da **reddedilmiyor**.<br>Mekanik açıklama (sentez): *"korelasyon"* farklı **ölçüm düzeylerinde** ölçülüyor ve bu düzeyler birbirine **indirgenemez**. Örnek düzeyinde ikili uyum bir **orandır**; model düzeyinde Spearman/Pearson az sayıda modelin **sıralaması** üzerinden bir **katsayıdır** ve yazarların kendi ifadesiyle küçük N'de *"güvenilir değildir"*; ayrıca **görev tipi** de değiştiriyor.<br>⇒ *"%80 uyum"* ile *"r≈0,31"* **çelişmiyor olabilir** — muhtemelen **farklı istatistikleri** ve/veya **farklı görev tiplerini** ölçüyorlar.<br>⚠️ **Bu sentez çelişkili düzeyinde kalıyor** — `r≈0,31`'in kendi kaynağı doğrulanamadığı için **tam çözüm değildir**.<br>⇒ Ve bu, **oturumun başında verilen bir düzeltmenin düzeltmesidir**: hüküm **açık kalıyor**, kapanmış sayılmıyor. | çelişkili | — |

### 4.3 n=1 ölçüm protokolü

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§4.3-1** | **Eşleştirilmiş tasarım zorunludur:** aynı görev seti (5-20 gerçek soru) **iki promptla da** koşulur. Prompt farkını görev zorluğu gürültüsünden ayırır. Meşru kıldığı hüküm: *"bu prompt, BU görev listesinde, ötekine göre X kez tercih edildi"* — daha fazlası değil. **Eşleştirilmemiş karşılaştırma 5-20'de anlamsıza yakındır.** | birincil | — |
| **§4.3-2** | **Kör ve sıra rastgeleli ikili karşılaştırma:** A/B sırası rastgele atanır ve hangi promptun hangisi olduğu **yargı anında gizlenir**. Mutlak puanlama iki farklı oturum arasında **karşılaştırılabilirlikte zayıftır**. | birincil | — |
| **§4.3-3** | **Yargı tekrar örneklenir:** her çift için yargıç **3 kez** (farklı seed ve sıra), çoğunluk oyu alınır. Üçte üç ⇒ düşük belirsizlik; ikiye bir ⇒ **"belirsiz, tek atımlık yargıya güvenilmez"** ve bu **açıkça işaretlenir**.<br>⚠️ **Tekrar örnekleme rassal varyansı azaltır, sistematik yanlılığı AZALTMAZ** (K25). | birincil | daraltıldı → K25 |
| **§4.3-4** | **Bootstrap ve güven aralığıyla özetlenir:** ham *"X/Y kazandı"* sayısına indirgenmez; kazanma oranı **güven aralığıyla birlikte** verilir. Aralık %50'yi net dışlıyorsa **yönsel sinyaldir**, kesin kanıt değildir. | birincil | — |
| **§4.3-5** | **Bilinen cevap kanaryası:** sete cevabını **zaten bildiğin**, doğrulanabilir 1-2 kısa gerçek sorusu konur. Ajanın gerçeği bulup bulmadığını ölçer — **istatistik gerekmez**, sonuç ikilidir.<br>⇒ **Tek başına bile meşru ve kesin bir olumsuz bulgudur**; n=1'de bile geçerlidir, çünkü istatistiksel değil **doğruluk temellidir**. | çıkarım | daraltıldı *(mutlak niceleme)*; özü ayakta |
| **§4.3-6** | **Yargıç farklı model ailesinden seçilir.** Mümkün değilse confound **raporda açıkça yazılır**. | çıkarım | — |
| **§4.3-7** | **Süreç metrikleri loglanır ama hüküm verilmez:** araç çağrısı ve kaynak sayısı kaydedilir; *"çok kaynak = iyi rapor"* hükmü **üretilmez**. | çıkarım | daraltıldı → K23 |

### 4.4 Ne ölçülemez

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **Q30** | **Meşru olmayan hükümler:**<br>**Stabil korelasyon katsayısı** — 5 ile 20 arası örneklemde hesaplanan `r` **gürültü ağırlıklıdır** ve **tek başına, güven aralığı olmadan raporlanmamalıdır**. ⚠️ *"Raporlanmamalıdır"* mutlak hâli **aşırıydı**: küçük N korelasyonu **bastırılmaz, güven aralığıyla raporlanır** (pilot çalışma pratiği).<br>**Genellenebilirlik** — *"bu prompt öteki görev setinde de daha iyi olur"* **taşınamaz**; geçerlilik yalnız kullanılan spesifik görev listesi ve spesifik yargıç için iddia edilebilir.<br>**Tek atımlık kesin verdikt** — %69,2 insan uyumu bile **10 karardan yaklaşık 3'ünde çoğunluk insan görüşünden sapma** demektir ⇒ bir kez `A > B` çıkması **hiçbir şey kanıtlamaz**.<br>**Uzunluk ve üsluptan arındırılmış gerçek kalite farkı** — uzunluk kontrolü yapılmadan, küçük örneklemde ayrıştırmak **mümkün değildir**.<br>**Süreç metriği ile sonuç kalitesi ilişkisi** — **nedensel kanıt yoktur**; ⚠️ **korelasyonel kanıt VARDIR** (test zamanı hesaplama ölçekleme çalışmaları). *"Sıfır kanıt"* ifadesi **abartıydı**; normatif sonuç `korelasyon ≠ nedensellik` gerekçesiyle **ayakta kalır**.<br>**Kendi kayırma yanlılığının payı** — varlığı biliniyor, **miktarı ölçülmedi**.<br>**`r≈0,31` iddiasının doğruluğu** — ne doğrulanabildi ne çürütülebildi. | çıkarım | daraltıldı → K22, K23 |

### 4.5 Atıf doğruluğu

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **Q31** | Ticari derin araştırma ajanlarının **atıf halüsinasyon oranı %11 ile %57 arasındadır**; atıf doğruluğu bir sistemde **%78**, arama destekli bir başkasında **%94** (n=100 doktora düzeyi görev).<br>⚠️ Yazarların kendi uyarısı: mevcut benchmark'lar **atıflı URL'lerin gerçekten var olup olmadığını doğrulamıyor** ⇒ *"atıf doğruluğu"* iddiaları bile **kendi içinde eksik doğrulanmıştır**.<br>⚠️ Ham metin çekilemedi ⇒ rakamlar ikincildir. | ikincil | çürütülemedi |
| **Q32** | Mevcut benchmark'lar **yalnız nihai çıktıya bakıyor** ve araştırma sürecini (araç çağrısı, kaynak sayısı) **göz ardı ediyor**. Bu süreç metriklerinin sonuçla korelasyonuna dair **rakam bulunamadı**. | arandı, yok | daraltıldı → K23 |

### 4.6 A30 iddia listesi

> ⚠️ **Üç iç tutarsızlık kabul edildi.** ① **Çifte standart:** §4.6-4 *"5-20'de herhangi bir korelasyon anlamsızdır"* derken, aynı rapor `%30-70`, `16×`, `~7×` gibi kesin rakamları **aynı şüphecilikle sorgulamıyordu**. ② **Aynı eşik iki yerde farklı:** §4.6-2 tekrar örneklemeyi (**bir süreç müdahalesi**) meşruiyet artırıcı sayarken, §4.6-7 süreç metriklerini **toptan kanıtsız** ilan ediyordu. ③ **Mutlak niceleme:** §4.6-1, -3, -5, -6, -8'in hepsi *"her zaman"*, *"hiçbir"*, *"asla"*, *"bağımsız olarak"* içeriyordu ve hepsi **koşullu hâle geldi**.

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§4.6-1** | İkili karşılaştırma, 5 ile 20 arası örneklemde mutlak puanlamadan **genellikle** daha güvenilirdir.<br>⚠️ *"Her zaman"* düşer: **objektif zeminli görevlerde** (birim testi, tam eşleşme) rubrik üstün olabilir; ayrıca ikili karşılaştırma **ikisi de kötüyken sahte tercih dayatır**. | çıkarım | daraltıldı |
| **§4.6-2** | Yargıcı 3 kez tekrar örneklemek tek atımlıktan daha meşru hüküm verdirir — çünkü **rassal varyansı** azaltır.<br>⚠️ **Sistematik yanlılığı AZALTMAZ.** Üç oy aynı yanlılığı paylaşıyorsa ortaya çıkan şey **sahte çoğulluktur**. ⇒ Bu yüzden farklı model ailesi (§4.6-6) ve kanarya maddesi (§4.3-5) tekrar örneklemenin **ikamesi değil, tamamlayıcısıdır**. | birincil | daraltıldı → K25 |
| **§4.6-3** | Uzunluk kontrolü yapılmadan hiçbir kazanma oranı farkı *"kalite farkı"* olarak yorumlanamaz. — mutlak niceleme **daraldı**, yönü korunur. | birincil | daraltıldı |
| **§4.6-4** | 5 ile 20 arası örneklemde hesaplanan korelasyon katsayısı **tek başına, güven aralığı olmadan raporlanmamalıdır**.<br>⚠️ Eski hâli *"raporlanmamalıdır"* diyordu ⇒ **aşırı**; küçük N korelasyonu **güven aralığıyla raporlanır**.<br>⚠️ Ve **çifte standart kabul edildi**. | çıkarım | daraltıldı → K22 |
| **§4.6-5** | Bilinen cevap kanaryası tek başına geçerli bir test biçimidir. — *"örneklem büyüklüğünden bağımsız olarak"* mutlaklığı **daraldı**; özü ayakta, çünkü **doğruluk temelli** olduğu için istatistik gerektirmez. | çıkarım | daraltıldı |
| **§4.6-6** | Aynı model ailesi hem üretici hem yargıçsa, ölçülen iyileşme **kendi kayırma yanlılığıyla kirlenmiş sayılmalıdır**. — mutlak niceleme **daraldı**, yönü korunur; K25 ile **birlikte okunur**. | ikincil | daraltıldı |
| **§4.6-7** | Süreç metrikleri karar vermede **kullanılmamalıdır** — çünkü **nedensel kanıt yoktur**.<br>⚠️ Eski hâli *"sıfır doğrulanmış kanıt"* diyordu ⇒ **abartı**: test zamanı hesaplama ölçekleme çalışmaları **en azından korelasyonel** kanıt sunuyor.<br>⇒ **Normatif sonuç ayakta kalır**, çünkü gerekçesi `korelasyon ≠ nedensellik`tir — ama *"kanıt yok"* demek **yanlıştı**. | çıkarım | ⛔ kısmen çürütüldü → K23 |
| **§4.6-8** | Tek koşumdan çıkan *"bu prompt öncekinden iyi"* hükmü **derece farkı için** meşru değildir — en iyi ihtimalle **yönsel izlenimdir**.<br>⚠️ *"Asla meşru değildir"* **fazla güçlüydü**: **ikili ya da felaket türü farkta n=1 yeterlidir** — *"her seferinde çöküyor, bu düzeltme çözüyor"* bir mühendislik standardıdır.<br>⇒ Ayrım **derece farkı ile ikili fark** arasındadır; kanarya maddesi tam olarak bu istisnadan yararlanır. | çıkarım | daraltıldı → K26 |
| **§4.6-9** | Küçük ölçekte **Salih'in kendi yapılandırılmış kör okuması**, LLM yargıcının insan uyum oranından (%69 ile %85 bandı) **daha az güvenilir sayılamaz** ⇒ LLM yargıç Salih'in **yerine değil, yanına** konmalıdır. | çıkarım | çürütülemedi |

---

## 5. Brifing kontrol listesi

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **B1** | **Erişim haritasını brifinge yaz, ama HİPOTEZ olarak işaretle.** Ajana brifingi ölçüp düzeltme yetkisi ver. Dayanak: *denenmemiş olmak, açık olmak değildir*. | ölçüm | — |
| **B2** | **Kapalı kaynak için taktiği brifinge koy:** replikasyon deposu → upstream git → kaynağın `.md`/`.rst` hâli. Bu koşumda **dört kez** karşılığını verdi. | ölçüm | — |
| **B3** | **WebSearch'ü tayınla ve sessiz tükenişi ajana SÖYLE.** Boş arama, sayacın dolduğu anlamına gelir; sonucun yok olduğu anlamına gelmez. Yoksa **negatif bulgu uydurulur**. | birincil | — |
| **B4** | **Bağlam bütçesi etkin uzunluktur.** Distractor yoğun işte 2K ile 16K varsay, nominal pencereye güvenme. | birincil | — |
| **B5** | **İzole bağlam ve özet döngüsü.** Ajanlar birbirinin ham bulgusunu görmez. ⚠️ Bu bir **tasarım tercihidir**, kanıtlanmış üstünlük değil (K24). | birincil (tasarım tavsiyesi) | daraltıldı → K24 |
| **B6** | **Ajan sayısını MECE ayrışabilirlik gerekçelendirsin**, *"daha fazla ajan daha iyi"* değil. | birincil | — |
| **B7** | **"Bulunamadı" ile "aranamadı"yı ayırmak brifinge ZORUNLU madde yapılır.**<br>⚠️ **Bu raporun kendisi bu kuralı iki yerde ihlal etti** (K19, K20). | ölçüm | — |
| **B8** | **"Doğrulayamadığın rakamı verme" ZORUNLU maddedir.** Bu koşumda ajan üç kez rakam uydurabilirdi, **uydurmadı**. | ölçüm | — |
| **B9** | **İskelet önce:** ilk bulguda kısa ara metin üretilir; yalnız araç çağrısıyla kesilen ajanın işi **tamamen** kaybolur. | birincil | — |
| **B10** | **Persona ve rol atamayı gerekçesiz kullanma.** Etki göreve bağlıdır ve ölçülmüş çökme vakası vardır. Bizim ajanlarımıza *"sen tez ajanısın"* demek **rol değil GÖREV tanımıdır** — bu ayrım korunmalıdır. | birincil | — |
| **B11** | **Katı format zorunluluğunun maliyetini KABUL ET ve ÖLÇ.** Şema bırakılmaz (izlenebilirlik için gereklidir) ama maliyeti frontier modelde ölçülür. | birincil | — |
| **B12** | **Kanıt etiketlemesinin gerekçesini DÜZELT:** *"halüsinasyonu azaltır"* değil, **"iddianın kanıt seviyesini okuyucuya açık kılar"**. Nedensel kanıt yoktur. | birincil | — |
| **B13** | **Yargıç, üreticiyle aynı aileden olmasın**; mümkün değilse confound **raporda yazılır**. | çıkarım | — |
| **B14** | **Kanarya maddesi koy** — her ölçüm setine cevabını bildiğin 1-2 soru. n=1'de bile meşru tek testtir. | çıkarım | — |
| **B15** | **Süreç metriklerini logla, hüküm kurma.** ⚠️ Gerekçe düzeltildi: kanıt **sıfır değil**, **nedensel değil** (K23). | arandı, yok | daraltıldı → K23 |
| **§5-1** | ⭐ **Bu ailenin en güçlü tek bulgusu:** B7 ve B8'in maliyeti **iki cümledir** ve getirisi **üç uydurulmuş rakamın önlenmesidir**.<br>⇒ **Prompt veriminin en yüksek getirili kolu, ajanın NE BİLMEDİĞİNİ söyleyebilmesini yapısal olarak mümkün kılmaktır.**<br>⇒ Ölçüm eklemek değil, **ölçememeyi raporlanabilir kılmak**. | ölçüm | — |
| **§5-2** | ⭐ **Ve bunu MAST dışarıdan doğruluyor:** en büyük başarısızlık kategorisi **Poor Specification (%37,17)** ⇒ **brifing tasarımı, çok ajan başarısızlığının BİRİNCİ kaynağıdır**, marjinal bir iyileştirme değildir.<br>⇒ Salih'in *"araştırma promptlarımın verimini artırmalıyız"* sezgisi **bağımsız bir ölçümle doğrulanmıştır**. | birincil | — |

---

## 6. Açık borçlar

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **D1** | ~~Antitez koşulmadı~~ ⇒ **KAPANDI.** Araçsız koştu: **4 çürütme** (K19, K20, K21, K23), **4 daraltma** (K22, K25, K26 ve mutlak niceleme sınıfı), **3 iç tutarsızlık kabulü**, **3 sağ çıkan iddia**. | ölçüm | kapandı |
| **D2** | Konum eğrisi sayıları, ölçek eğrisi ve self-consistency düzleşmesi — **erişim açık bir oturumda**. | aranamadı | — |
| **D3** | Üreticinin çok ajan mühendislik yazısı kapalıydı. Muhtemelen **paylaşılan ile izole bağlam karşılaştırmasını** içeriyordu ⇒ **bu ailenin en hedefli kayıp kaynağı**. | aranamadı | — |
| **D4** | Format kısıtlaması ve persona rakamlarının birincil metinlerine **erişilemedi**. | aranamadı | — |
| **D5** | MT-Bench'in `~%85` insan uyumu ve `r≈0,31`'in kaynağı — **ikisi de doğrulanamadı** ⇒ **hüküm AÇIK**. | aranamadı | — |
| **D6** | Ölçek eğrisi: statü *"aranamadı"*dan **"bulunamadı"**ya yükseldi; depoya erişildi, **sayı yok**. | arandı, yok | — |
| **D7** | Negatif ile pozitif talimat ekseni **aranamadı**. | aranamadı | — |
| **D8** | ⭐ **Kendi şemamızın maliyeti frontier modelde ölçülmedi.** Ölçüm zayıf modelde yapıldı ⇒ **ölçüm protokolüyle test edilebilecek İLK somut hipotez**. | kestirim | — |
| **D9** | ⭐ **Özetleme sadakati literatürü TARANMADI** — QAGS, SummaC, FactCC, LLMLingua. Bunu *"yok"* diye yazmıştık; **var ve taranmadı**. | aranamadı | K19'dan doğdu |
| **D10** | **Olumsuzlama duyarsızlığı literatürü TARANMADI** — Kassner & Schütze (ACL 2020) doğrudan ölçüyor. Aynı hata sınıfı. | aranamadı | K20'den doğdu |

---

## 7. Fikir kutusu adayları

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **V72** | **Brifing bir hipotezdir.** Ajana verilen erişim haritası **doğrulanmamış bir öncüldür**; ajan onu ölçüp düzeltmekle **yükümlü** kılınmalıdır. Bu koşumda **üç kez** karşılığını verdi. | ölçüm | — |
| **V73** | ⭐⭐ **"Aranamadı" etiketi.** Kanıt etiketi ailesine dördüncü etiket: **aranamadı** (bütçe ya da erişim nedeniyle sorgulanamadı). Şu anda bu durum *"bulunamadı"* içinde **eriyor** ve **negatif bulgu enflasyonu** yaratıyor.<br>**Dört bağımsız gerekçesi vardır:** ① bu koşumda üç ajan ayrımı **elle** yaptı ve üçü de değer üretti · ② **K19** — özetleme kaybı literatürünü *"yok"* yazmıştık, **var** · ③ **K20** — olumsuzlama literatürünü *"yok"* yazmıştık, **var** · ④ başka bir ailenin dürüstlük kaydı: *"erişim engeli ile gerçek yokluk ayırt edilemiyor, ve bu ayrımsızlığın kendisi rapor edilmesi gereken bir bulgudur."*<br>⇒ **Oturumun en çok bağımsız gerekçe biriktiren tek önerisidir.** | ölçüm | gerekçesi güçlendi → K19, K20 |
| **V74** | **Etkin uzunluk tablosu kanona.** Q6 ve Q7 tabloları, bağlam bütçelemesinin **sayısal dayanağı** olmaya adaydır. | birincil | — |
| **V75** | **MAST kontrol listesi.** 14 başarısızlık modu, ajan brifingi yazarken **doğrudan kontrol listesi** olarak kullanılabilir — özellikle sonlanma koşullarından habersizlik (%6,54), adım tekrarı (%11,5) ve bilgi saklama (%6,02); **hepsi brifingle önlenebilir sınıflardır**. | birincil | — |

---

## 8. Kapanış

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§8.1** | Aile A28, A29 ve A30'dur; **antitez koştu** (araçsız).<br>Sonuç: 4 çürütme, 4 daraltma, **3 iç tutarsızlık kabulü**, 3 sağ çıkan iddia. | ölçüm | — |
| **§8.2** | **İki şerh birlikte okunur:** ① araçsız tur olduğu için **mantıksal** saldırılar tam güçtedir, **olgusal karşı örnekler hatırlama düzeyindedir**; ② *"sağ çıktı"* damgası **"aynı-aile hakemi karşısında sağ kaldı"** demektir. | çıkarım | — |
| **§8.3** | ⭐ **En ağır ders:** bu ailenin en güçlü tek bulgusu *"ajanın ne bilmediğini söyleyebilmesini yapısal olarak mümkün kıl"* idi — ve antitez, **bu raporun kendisinin iki yerde bunu yapamadığını** gösterdi (K19, K20).<br>**Kural doğruydu; uygulayan biz değildik.** | ölçüm | — |
| **§8.4** | **Raporun beyan edilen diğer zayıflıkları:** ① kendi tavsiye ettiği şema, **kendi ölçüm protokolüyle henüz test edilmedi** — yani bu rapor, uygulanmasını önerdiği ölçümü **kendine uygulamamıştır**; ② oturumun başında verilen bir düzeltme **bu ailede yeniden açıldı** ve kapanmış sayılmıyor; ③ uzunluk ekseninin tek güçlü kanıtı **dolaylıdır** ve analoji olarak işaretlenmiştir. | çıkarım | — |
