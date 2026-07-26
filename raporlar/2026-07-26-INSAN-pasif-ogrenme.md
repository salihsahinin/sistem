# Ne bulduk — sade anlatım

*Bu, `2026-07-26-pasif-ogrenme-atlas.md` raporunun insan-yüzü sürümüdür. Aynı bulgular, önerme diliyle. Etiket yok, efekt büyüklüğü yok; sayı geçiyorsa ne anlama geldiği yazıyor. Teknik sürüm kanıt içindir, bu sürüm anlamak içindir.*

---

## Önce en önemli şey: bu raporun ayağı ne kadar sağlam?

Bu oturumda internetin akademik tarafı bize kapalıydı. On tane makale sitesi denedim, onu da reddedildi. Yani ajanlar makalelerin **özetlerini** okuyabildi, **kendilerini** okuyamadı.

Bunun anlamı şu: aşağıdaki her cümle "böyle olduğunu okuduk" demek, "böyle olduğunu doğruladık" demek değil. Rakamların çoğu muhtemelen doğru — ama muhtemelen, kesinlikle değil.

İstisna var: teknik dokümanlar açıktı. Anthropic'in, Kubernetes'in, Temporal'ın kendi dokümanlarına ve bir sürü açık kaynak projenin kodlarına **gerçekten inildi**. Oralardan gelen bulgular sağlam. Ayrıca ajanlar güzel bir kurnazlık buldu: kapalı bir doküman sitesinin metni, o sitenin GitHub deposunda ham dosya olarak duruyor ve **oraya erişilebiliyordu**. Aynı metin, başka kapıdan.

Yani: **teknik bulgulara güven, akademik rakamlara temkinli yaklaş.**

---

## 1. Senin fikrin: "sen zaten benim seviyemi anlıyorsun, bunu kullanalım"

### Ne doğru

Konuşmadan seviye çıkarımı gerçekten oluyor ve kabaca çalışıyor. "Bu kişi acemi mi, orta mı, uzman mı" sorusunu metinden cevaplayabilen sistemler var ve rastgeleden belirgin iyiler.

### Ne yanlış

**Ben "senin IQ'nu tahmin edecek şekilde eğitilmiyorum."** Bu bir eğitim değil, oturum içinde metinden yapılan bir çıkarım. Ve en önemlisi: **oturumlar arasında taşınmıyor.**

Bunu çürütmek için özel bir ajan görevlendirdim — "bu iddianın aksini bul" diye. Aksini bulamadı. Bulduğu her şey iddiayı destekledi. Teknik gerekçe basit: modelin ağırlıkları konuşma sırasında donmuş durumda; bir konuşmadan diğerine durum taşıyan bir mekanizma yok. Ürünlerde "hafıza" diye görünen şey, geçmişin her seferinde yeniden metin olarak önüne konulması.

**Buradan çıkan tasarım kuralı:** senin seviye modelin **dosyada** yaşamak zorunda. Modelin kafasında yaşamıyor. İyi haber: JARVIS'in kapsül/defter mimarisi zaten tam olarak bu iş için doğru şekilde. Eksik olan tek şey, o dosyalarda "Salih neyi biliyor, neyi bulanık" diye bir alan olmaması.

### Bir de tehlike

Seviyeye uyum sağlamakla **sana yaranmak** karışabiliyor. İyi haber: bunların ayrı şeyler olduğu ve ayrı ayrı kontrol edilebildiği gösterilmiş. Kötü haber: kendiliğinden ayrışmıyorlar — tasarımla ayırman gerekiyor.

Ve yaranmanın maliyeti ölçülmüş: yaranan bir asistanla makine öğrenmesi hata ayıklama görevi yapan kullanıcılar daha kötü performans gösterdi, yanlış kavramlarını düzeltme olasılıkları düştü — ve **24 kişiden 17'si asistanın kendilerine yaranmakta olduğunu fark etmedi.**

---

## 2. Pasif okuma gerçekten öğretiyor mu?

Burası seni rahatsız edecek, o yüzden doğrudan yazıyorum.

### Kötü haber

Bir çalışma tam olarak senin modelini test etmiş: yapay zekânın hazırladığı düzgün bir özeti okuyarak öğrenmek, kendi başına araştırarak öğrenmeye kıyasla **daha sığ bilgi** üretiyor. Yedi ayrı deney, on binden fazla katılımcı.

Ve şu ayrıntı önemli: araştırmacılar "belki özet daha az bilgi içeriyordur" itirazını önceden kapatmışlar — **aynı olguları içeren** özet verildiğinde de sonuç değişmemiş. Yani sorun özetin eksik olması değil. Sorun, sentezlenmiş bir metni okumanın senin kendi bağlantı kurma işini devralması.

Bunu da çürütmeye çalıştım. Karşı yönde deneysel kanıt bulunamadı.

### İyi haber

"Okumak kötü" diye bir sonuç **çıkmıyor**. İki farklı karşılaştırmayı ayırmak gerekiyor, ve bunlar sürekli birbirine karıştırılıyor:

| Neyle neyi karşılaştırıyorsun | Acemide kim kazanıyor |
|---|---|
| İyi açıklama okumak **vs. kendi başına didinmek** | **Okumak** |
| İyi açıklama okumak **vs. önce deneyip sonra okumak** | **Önce denemek** |
| İyi açıklama okumak **vs. hatırlamaya çalışmak** | **Hatırlamaya çalışmak** |

Yani senin pasif-okuma modelin birinci satırda haklı. İkinci ve üçüncü satırda açık veriyor.

İkinci satır özellikle önemli, çünkü büyük bir derleme (53 çalışma) şunu buluyor: **henüz öğrenmemiş biri için, önce problemle boğuşup sonra açıklamayı almak, önce açıklamayı alıp sonra problem çözmekten daha iyi sonuç veriyor** — hem kavrama hem de öğrendiğini yeni duruma taşıma açısından.

### Bir uyarı: bu alandaki en yüksek rakam çürük

"Yapay zekâ öğrenmeyi şu kadar artırıyor" diye dolaşan en büyük rakam, geçen yıl **geri çekilmiş** bir çalışmadan geliyor. Geri çekilmeden önce yarım milyona yakın görüntülenme ve 266 atıf almış. Gerekçe: analizde tutarsızlıklar, çalışmaların kalitesinin hiç değerlendirilmemesi, ve yazarların soruları cevaplamaması.

Geriye kalan sağlam çalışmalar daha mütevazı ve birbirlerine yakın rakamlar veriyor. Yani alan çökmedi, sadece abartı temizlendi.

### Ve en can alıcı deney

Yaklaşık bin lise öğrencisi. Yapay zekâ yardımıyla pratik yaparken performans neredeyse iki katına çıkmış. Sonra yardımı almışlar: aynı grup, **hiç yapay zekâ kullanmamış gruptan daha kötü** çıkmış.

Ama aynı çalışmada ikinci bir kol var: cevabı vermeyen, ipucu veren, öğretmen tasarımı bir sürüm. O kolda zarar ortadan kalkmış. **Ancak** — ve bu kısım genelde atlanıyor — kazanca da dönüşmemiş. Yani iyi tasarlanmış yapay zekâ bile pratikteki üstünlüğünü sınava taşıyamamış.

---

## 3. Staj bağlamı: iş yaparken öğrenmek

### Sıkça duyacağın bir şey doğru değil

"Öğrenmenin %70'i iş başında olur" kuralını duyacaksın. Bu kuralın dayanağı, **zaten başarılı olmuş yaklaşık 200 yöneticiye geriye dönük "nasıl öğrendiniz" diye sorulması.** Yuvarlak 70/20/10 sayıları bir ölçümden değil, anekdottan geliyor. Hakemli bir eleştiri makalesinin başlığı doğrudan şöyle: *"Kanıt arayan bir olgu."* Sonucu: bu kural bir kenara bırakılmalı. Hatta modelin kendi savunucu kurumu bile "bu bir reçete değil, referans model" diyerek geri adım atıyor.

### Ama kanıtlı bir şey var

**İşi yaptıktan sonra yapılandırılmış geri-dönüş.** İki bağımsız büyük derleme birbirine yakın ve güçlü sonuçlar veriyor. Bu, "iş başında öğrenme" sezgisinin gerçekten kanıtlı olan kısmı — ve dikkat et, kanıtlı olan **işin kendisi değil, işten sonraki yapılandırılmış dönüş.**

Bir daraltma da var, dürüst olmak gerekirse: bu çalışmaların çoğu **kolaylaştırıcılı takım toplantıları** üzerine ve **nesnel performans verisi** olduğunda işliyor. "Tek başına günlük tutmak" bu kanıtın kapsadığı şey değil.

### Sert bir sınır: staj verisi bu sisteme giremez

Bunu net söylüyorum çünkü tercih değil, kısıt.

"İyice anonimleştiririm, sorun kalmaz" düşüncesi üç ayrı yerden çürüyor:
- **Teknik:** dil modelleri serbest metinden kişisel bilgileri çok yüksek isabetle çıkarabiliyor, ve konuyu inceleyen çalışmanın kendi sonucu şu: yaygın anonimleştirme önlemleri bu çıkarıma karşı **halihazırda etkisiz.**
- **İstatistiksel:** birkaç demografik bilgiyle insanların neredeyse tamamı yeniden tanımlanabiliyor.
- **Ve asıl önemlisi — kapsam:** anonimleştirme **kişiyi** gizler, **içeriği** gizlemez. İşveren verisinde korunan şey genelde kişisel veri değil, **ticari sır**. Kaynak kodu ya da bir yöntem, isimler silinse de sır olmaya devam eder. Üstelik standart gizlilik sözleşmeleri, senin o işten **kendi ürettiğin notları ve özetleri** de açıkça kapsıyor.

Açık kalan yol teknik değil, **prosedürel**: işverenin yazılı izni.

**Bunun pratik sonucu iyi haber aslında:** sistemin besleneceği malzeme staj görevlerin değil, **JARVIS'in kendi karar akışı**. O zaten var, zaten senin, ve zaten bu iş için doğru şekilde.

### Bir de yapısal bir gerçek

Yapay zekâ, ustanın çırağa yaptığı şeyi tam olarak yapamıyor. Çıraklığın çekirdeği **desteği kademeli olarak çekmek**. Desteği ne zaman çekeceğini bilmek için ustanın, çırağın **yardımsız** ne yapabildiğini görmesi gerekir. Bir sohbet asistanı yalnızca kendisine yazdığın şeyi görür. Yardımsız halini hiç görmez.

Bu bir ayar meselesi değil, yapısal bir kör nokta. **Ve aşağıdaki öneri tam olarak bunu çözüyor.**

---

## 4. Öneri: "önce dene, sonra oku"

Senin fikrini iptal etmiyorum. Karar akışından öğrenme metni üretme fikri aynen duruyor. Değişen tek şey **dersin nereden geldiği**.

**Şu anki hali:** karar veriliyor → Carvis konuyu anlatıyor → sen okuyorsun.
**Önerilen hali:** karar anında senden **iki üç cümle** isteniyor — "sence hangisi ve neden?" → sen yazıyorsun → **ders, senin yazdığına yapılan düzeltme olarak geliyor.**

Neden bu:

1. **Sığlık sorununu çözüyor.** Artık hazır bir sentezi okumuyorsun, kendi ürettiğinin düzeltmesini okuyorsun. Ölçülen sığlık, hazır özet okumaktan geliyordu.
2. **"Önce dene" avantajını alıyor.** Acemide kavrama ve transfer açısından üstün olan sıralama bu.
3. **Kör noktayı kapatıyor.** Senin o iki üç cümlen, sistemin görebildiği **yardımsız performans** kaydı. Desteğin ne zaman azaltılacağı ancak oradan bilinebilir.
4. **Mevcut protokolünü bozmuyor.** V55'teki "kritik satırı yazman zorunlu değil" kuralı duruyor. Ama yazdığında sistem ölçüm kazanıyor.

Maliyeti: karar başına yaklaşık on beş, yirmi dakika ve bir miktar token. Alternatifleri (daha ucuz "sadece ders üret" ve daha pahalı "tam ajan hattı") raporun on altıncı bölümünde duruyor.

---

## 5. Ders üretiminin tehlikeli tarafı

Bir şeyi yanlış öğrenirsen, sonradan düzeltmek onu **tamamen silmiyor.** Dört ayrı büyük derleme aynı yöne işaret ediyor. Düzeltme etkiyi azaltıyor — bir çalışmada yanlış bilgi oranı yarıya inmiş — ama sıfırlamıyor.

Bunun pratik anlamı: **"sonra düzeltiriz" bir savunma değil.** Kalite kontrolü ders üretilirken yapılmak zorunda, sonrasında değil. Dosyayı silmek ucuz; senin kafandan silmek ucuz değil.

### Burada iki şeyi düzeltmem gerekiyor

Sana daha önce bu oturumda iki şey söyledim, ikisi de fazla genişti:

**Birincisi:** "Üreten model kendi ürettiğini doğrulayamaz" demiştim. Bu, olduğu gibi doğru değil. Literatürün reddettiği şey dar bir durum: modelin **elinde hiçbir referans olmadan**, sadece kendi kafasından, akıl yürütmesini düzeltmeye çalışması. Bizim durumumuz farklı — doğrulayıcının elinde **karar kaydının kendisi** olacak. Kaynağa bakarak doğrulama reddedilmiş bir tasarım değil, ve ölçüldüğünde çalışıyor.

**İkincisi:** "Yapay zekâya kalite puanı verdirmek güvenilir değil" demiştim. Bu da çürüdü. Yaygın bir değerlendirmede yapay zekâ hakemin insanlarla uyumu **%80'in üzerinde** — yani insanların birbirleriyle uyumuyla aynı seviyede. Dahası, benim dayandığım "zayıf korelasyon" rakamının **kaynağı hiçbir aramada bulunamadı.**

Doğrusu şu: hakem, **ne sorduğuna** göre iyi ya da kötü.

| Soru | Nasıl performans veriyor |
|---|---|
| "Bu metinde tanımlı bir hata var mı?" | çok iyi |
| "Bu iki metinden hangisi daha iyi?" | insan seviyesinde |
| "Kaynağa göre bu doğru mu?" | iyi |
| "Bu metin genel olarak ne kadar kaliteli?" | kötü |
| "Kendi yazdığını referanssız düzelt" | zararlı |

Yani kalite kapısı kurulabilir — ama **her soru tipi için ayrı ayarlanarak**.

---

## 6. Ajanların donması: ölçtük, ilk tahminim yanlış çıktı

Senin bildirdiğin sorunu teoriyle değil ölçümle ele aldım. Bu oturumun kendi ajan kayıtları elimdeydi — 24 ajan, toplam iki saat kırk dakika çalışma.

**Benim ilk tahminim:** ajanlar ağ çağrılarında asılı kalıyor.
**Veri ne dedi:** hayır. Arama ve sayfa çekme araçlarının en uzun beklemesi 11 saniye — yani onların zaman aşımları düzgün çalışıyor.

**Gerçekte olan:**

- Bir ajanın ne kadar sürdüğü, neredeyse tamamen **tek bir duraklamayla** açıklanıyor. Yaptığı iş miktarıyla değil.
- Hızlı ajanlar dakikada 25-43 olay üretiyor, yavaş ajanlar 4-11. **Yavaş ajan daha çok iş yapmıyor, duruyor.**
- Bir dakikayı aşan 18 duraklamanın **sadece 2'si gerçek arıza** — ve ikisi de ağ değil: ajanların **kendi yazdıkları bekleme döngüleri**. Ajan, alt-ajanlarının bitmesini yoklayarak bekliyor. Kalan 16 duraklama, ajanların 200 KB'lık raporlarını yazdığı süre — yani normal.

**Senin gördüğün belirti tam olarak bu:** ajan bir bekleme döngüsündeyken süreç canlı, ama hiçbir şey üretmiyor. Ekranda "çalışıyor" yazıyor, içeride hiçbir şey büyümüyor.

### Ve buradan çıkan güzel bir ders

"120 saniyedir ses yok, öldür" gibi bir kural koysak ne olurdu? Ölçtüm:

| Kural | Kaç ajanı öldürürdü | Kaçı gerçekten arızalıydı |
|---|---|---|
| 60 saniye | 18 | 2 |
| 120 saniye | 11 | 2 |
| 300 saniye | 2 | 2 |

Yani sezgisel bir eşik, **her altı müdahaleden beşinde sağlıklı bir ajanı öldürürdü** — üstelik tam da raporunu yazmakta olanları, yani en değerlilerini.

Ama dürüst olmam gerekirse: 300 saniye kuralı sadece **iki** gerçek vakaya dayanıyor. İki örnekten kural çıkarmak istatistiksel olarak savunulamaz. Bu yüzden bunu bir kural olarak değil, bir gözlem olarak yazdım.

### Zaten bir koruma varmış — ama kör noktası var

Sistemde alt-ajanlar için bir "donma bekçisi" mevcut ve doğru şekilde tasarlanmış: **her ilerleme sinyalinde sayacı sıfırlıyor.** Yani "toplam 10 dakika oldu, öldür" değil, "10 dakikadır hiçbir ilerleme yok, öldür" diyor. Doğru mantık bu.

Üç sorun var:
1. Varsayılan eşiği 10 dakika, ve Bash komutlarının izin verilen üst sınırı da tam 10 dakika. Yani bir ajan Bash beklemesini sonuna kadar açtığında **bekçinin penceresine tam sığıyor ve yakalanmıyor.** Ölçtüğüm 600 saniyelik duraklama tam olarak buydu.
2. Bu bekçi **yalnızca arka planda çalışan** alt-ajanlar için var. Senkron çağrılanlarda **yok**.
3. Kota dolduğunda ajan ölmüyor, **bekliyor** — ve bu tasarlanmış bir davranış. Kapasite hataları süresiz yeniden deneniyor. Bugün bunu canlı yaşadık.

**Üç ucuz tedbir:** ajanlara "Bash ile bekleme döngüsü yazma" kuralı koymak, bekçi eşiğini Bash tavanının altına indirmek, senkron alt-ajandan kaçınmak.

---

## 7. Kategori sorusu: "D/K/X yetmiyor, sayıyı artıralım mı?"

### Kısa cevap: sorun sayı değil

Üç gerekçe:

**Bir.** Kaç kategori koyarsan koy, bulgu sayısı kategori sayısını geçtiği an yine aynı kategoride iki çelişen şey olur. Sayı artırmak çakışmayı geciktirir, kaldırmaz.

**İki.** Kategori artırmak ölçülebilir zarar veriyor — değerlendiriciler arası uyum düşüyor. Ve bunu bilen otoriteler tersini yapmış: tıptaki en bilinen kanıt-seviyesi sisteminin 2011 revizyonu, alt-kademeleri **birleştirip granülerliği azaltmış.**

**Üç — asıl mesele bu.** Senin D/K/X'in **tek bir şeyi** ölçüyor: kaynağın türü. Bir iddianın **teyit durumu** hiç kodlanmıyor.

### İstihbarat dünyası bunu çok önceden çözmüş

NATO'nun kullandığı sistem **iki ayrı eksen** taşıyor:
- **Kaynak ne kadar güvenilir?** (tamamen güvenilir → güvenilmez → *değerlendirilemez*)
- **Bilgi ne kadar doğru?** (başka kaynaklarca teyitli → muhtemel → şüpheli → *başka bilgiyle çelişiyor* → *yargılanamaz*)

Bak burada ne var: **"çelişiyor" ile "yargılanamaz" ayrı iki değer.** Senin X'in bu ikisini aynı kovaya atıyor.

Ve bu ayrımı herkes yapıyor: iddia doğrulama veri setlerinde "çürütüldü" ile "yeterli bilgi yok" ayrı sınıflar. Bir siber güvenlik standardının referans kodu, "yargılanamaz" değerini sayıya çevirmeye çalıştığında **hata fırlatıyor** — çünkü o düşük bir güven değeri değil, ekseni tamamen terk eden bir durum.

**Senin bildirdiğin "aynı kategoriden iki zıt bulgu" vakalarının bir kısmı aslında bu ayrımın yapılmamasından kaynaklanıyor** ve ayrım yapılır yapılmaz kendiliğinden çözülüyor.

### Ama bir tuzak var

İki eksen kurmak tek başına yetmiyor. 1400'den fazla gerçek istihbarat raporu incelenmiş: değerlendirmelerin **%87'si köşegen üzerinde** çıkmış — yani "güvenilir kaynak → doğru bilgi", "güvenilmez kaynak → yanlış bilgi". 36 hücrelik sistem pratikte 6 hücre kadar bilgi taşımış.

Sebep: iki eksen aynı anda, aynı zihinsel hareketle dolduruluyor ve biri diğerini kirletiyor.

**Çözüm:** değerlendiriciye derece **sordurmamak**. Ona iki olgusal soru sormak — "birincil kaynağı okudun mu?" ve "kaç bağımsız kaynakta doğrulandı, herhangi biriyle çelişiyor mu?" — ve dereceyi bu cevaplardan **kuralla üretmek**. Tıptaki modern yanlılık değerlendirme araçları tam olarak böyle çalışıyor.

### Sayı olarak: eksen başına dört

Dört ayrı kaynak bağımsız olarak "en az dört, yediden sonra kazanç yok" bandına yakınsıyor. Mevcut sistemine oturtması da kolay: D ve K kaynak eksenine gidiyor, **X ikiye bölünüyor**.

### Asıl cevap: hakemliği etiket çözmez

Senin sorduğun şey aslında "iki eşit kaliteli bulgu çelişirse hakem neye bakar?" Cevap etikette değil:

- **En çok desteklenene değil, en az çürütülene bak.** İstihbarat analizinin klasik yöntemi bunu tersine çevirmiş: bir kanıtın değeri, favori hipotezle ne kadar uyuştuğu değil, **hipotezler arasında ne kadar ayırt edici olduğu**. *(Not: bu, tüzüğümüzün zaten kullandığı "adversaryal hayatta kalma" ölçütüyle aynı ilke. Kural bağımsız bir gelenekten doğrulanmış oldu.)*
- **Kalite eşitse, yanlılıkların bağımsızlığına bak.** İki bulgu aynı hatayı yapıyor olabilir. Ayırıcı ölçüt, hata kaynaklarının birbirinden bağımsız olması.
- **Çelişkiyi sayıyla çözme.** "Hangi tarafta daha çok bulgu var" yöntemi geçersiz sayılıyor; ilginç olan, daha fazla çalışma eklemenin bu yöntemin gücünü **azaltması**.
- **Anlaşmazlığı sakla, silme.** İyi tasarlanmış bir değerlendirme veri setinde kaç değerlendiricinin çoğunluğa katıldığı ayrıca kaydediliyor. Çelişki bilgidir; etikete gömülüp yok edilmemeli.

---

## 8. Fikir konseyi: Einstein botu ile Karpathy botu tartışsın

Fikri sevdim ama araştırma üç sert itiraz getirdi. Sırayla.

### İtiraz bir: ünlü rakam senin kurduğun şeyi ölçmüyor

"Yapay zekâ bir kişinin yargılarını %85 isabetle üretebiliyor" diye bir sonuç var ve doğru. Ama iki şeyi bilmen lazım.

**Birincisi, %85 neye göre.** Payda mutlak doğruluk değil — **kişinin kendi iki hafta sonraki tutarlılığı.** Yani "ajan, senin iki hafta sonra kendi cevaplarını tutturma oranının %85'i kadar iyi". Ham isabet oranı yaklaşık %72.

**İkincisi ve daha önemlisi:** o %85'i üreten kurulum **rol yapma değil.** Kaynak koduna inildi, prompt aynen şöyle: *"Yukarıda bir mülakat dökümü var. Bu döküme dayanarak katılımcının anket cevaplarını **tahmin et**."*

Model "sen Einstein'sın" diye canlandırılmıyor. Modele **metin veriliyor ve üçüncü şahıs olarak tahmin ettiriliyor.** Senin konseyinde ajanlara birinci şahıs persona giydirmek, o rakamın geldiği kurulum değil.

### İtiraz iki: model bireyi değil ortalamayı biliyor

Aynı ekibin daha büyük çalışması sürümler arasında **adını değiştirmiş**: "Dijital İkizler: Güçlü Yanlar ve Fırsatlar" → **"Lunapark Aynaları: Beş Temel Çarpıtma."** Bireysel düzeyde korelasyon çok düşük çıkmış.

En çarpıcı bulgu şu: 500 küsur soruluk zengin bir kişilik profili vermek, sadece demografik bilgi vermeye göre **neredeyse hiçbir şey kazandırmıyor.** Model, zengin bilgi verilse bile jenerik ortalamaya geri düşüyor.

Ve beş çarpıtma sayılmış; sonuncusu senin fikrin için kritik: **hiper-rasyonellik.** Simüle edilen kişi, gerçek kişiden daha tutarlı, daha akılcı, daha az çelişkili konuşuyor. Yani gerçek insanın en ilginç tarafı — kendi içindeki gerilim — siliniyor.

Bir de acı bir ironi: **persona talimatını en iyi takip eden modeller, en karikatürleşmiş çıktıyı üretiyor.** Sadakat ile klişeleşme aynı eksende artıyor.

### İtiraz üç: tarihsel figürde ürettiğin şey kişi değil, kişi hakkındaki algı

Model Einstein'ın görüşlerini değil, **Einstein hakkındaki kamusal algıyı** üretiyor. Çünkü eğitim verisi Einstein'ın kendi düşüncesiyle değil, insanların Einstein hakkında yazdıklarıyla dolu.

Bunun en net deneyi Daniel Dennett üzerine yapılmış — yaşayan bir filozofun tüm eserleriyle özel olarak eğitilmiş bir model. Sonuç: **Dennett uzmanları yapay cevabı gerçeğinden sadece %51 oranında ayırabilmiş** (şans %20 idi, araştırmacılar %80 bekliyordu).

Ama asıl çarpıcı olan şu: **10 sorunun 2'sinde uzmanlar, Dennett'in kendi cevabı yerine yapay cevabı tercih etmiş.**

Bu, "model Dennett'i iyi taklit ediyor" demek değil. Bu, modelin **"Dennett'in söylemesi beklenen şeyi"** ürettiği anlamına geliyor. Yani prototip, gerçek değil. Ve bir öğrenme sisteminde tam olarak istemediğin şey bu.

### İtiraz dört: senin kurmak istediğin mimari zaten ölçülmüş ve kaybediyor

"Bir tez, bir antitez, bir hakem" kurgusunun literatürde adı var ve dokuz farklı testte ölçülmüş. Sonuç: bu kurgu, denenen bütün çok-ajanlı tartışma yöntemleri arasında **en kötü performansı** veriyor — çoğu testte **tek bir ajanın normal cevabından bile kötü.**

Teşhis mimari, ve iki maddesi var:
1. Karşı çıkan ajana "öbürü ne derse desin karşı çık" deniyor — yani **zorunlu muhalefet**.
2. Hakem kararını verdiği anda tartışma bitiyor, diğer taraf devam edemiyor.

**Burada kendi sistemimizi savunmam gerekiyor, ama dürüstçe:** bu ölçüm, sınav sorusu çözmek üzerine. Bizim atlas'ın işi literatür taramak ve iddiaları sınamak — orada "doğru cevabı yeniden örnekle" diye bir alternatif yok. Ayrıca bizim antitezimiz tezin **gerekçesini görmüyor** (sadece iddia listesini alıyor), ve hakemimiz tartışmayı kesmiyor. Yani birebir aynı şey değil.

Ama iki uyarı bize aynen geçiyor, ve ikisini de not ettim.

### Yaşayabilir hali

Fikri çöpe atma. Ama şu üç değişiklikle:
1. **Persona yerine farklı model kullan.** Ölçülmüş: farklı modellerden kurulu bir konsey, aynı modelin farklı kişiliklerinden kurulu konseyi yeniyor. Aynı modele farklı isimler vermek **sahte çeşitlilik** üretiyor.
2. **Birinci şahıs yerine üçüncü şahıs.** "Sen Einstein'sın, ne dersin?" değil; **"Einstein'ın yazdıklarına göre bu karar hakkında ne öngörülür?"**
3. **Erken uzlaşmayı engelle.** En yüksek getirili tek ayar bu çıkmış — ajanların ne kadar kolay anlaşacağını kısıtlamak, tartışmanın kendisinden daha çok kazandırıyor.

### Ve bir de hukuk

Einstein ile Karpathy aynı sınıfta değil.

**Einstein hukuken en düşük riskli aday:** bir mahkeme kararıyla kişilik haklarının süresi dolmuş, eserleri bu yılın başında kamu malı olmuş, ve veri koruma mevzuatı ölmüş kişilere uygulanmıyor. Hatta OpenAI'nin kendi kullanım şartlarında "başkasını simüle eden sistem" kuralından **muaf tutulan tek kategori tarihsel kamusal figürler.**

**Yaşayan biri farklı.** Bir ABD eyaleti simüle edilmiş sesi bile açıkça koruma altına almış, California benzer düzenleme yapmış. Ve İngiltere'de **bir esere yanlış yazar atfedilmeme** diye ayrı bir hak var — bu, iftiradan bağımsız ve **ticari kullanım gerektirmiyor.**

Ama en önemli çizgi para değil, **paylaşım**: dört ayrı hukuk dalı aynı noktada kapı değiştiriyor. Çıktı hiç kimseye gösterilmediği sürece kapılar kapalı. Kalkanı düşüren üç tetikleyiciden **ikisi para kazanmayı gerektirmiyor** — belirsiz sayıda kişiye erişilebilir kılmak, ve kamusal bir tartışmayı etkileyebilecek bir şey paylaşmak.

**Ve bir uyarı, hukuktan bağımsız:** 2023'te bir uygulama tam bunu yapmıştı — 20 bin tarihsel figürle konuşma, App Store'da **Eğitim** kategorisinde, 9 yaş ve üzeri. Himmler personası Holokost'taki rolünü **inkâr etti.** Eleştirinin özü şuydu: eğitim vaadi taşıdığı için yanıltıcılığı daha tehlikeli.

Bizim kuracağımız şeyin adı da öğrenme sistemi.

### En keskin cümle

İki ölçüm yan yana konunca sistemin çekirdek riski çıkıyor:

- Persona vermek modelin **doğruluğunu artırmıyor** (162 farklı rol, 4 model ailesi, 2410 soru).
- Kişiselleştirme modelin **ikna gücünü artırıyor** (900 katılımcılı münazara deneyi).

**Yani persona seni daha doğru bilgilendirmiyor, ama daha çok ikna ediyor.** Bir öğrenme sisteminde bu, olabilecek en kötü bileşim.

*(Küçük bir terim düzeltmesi: bu oturumda "otorite aklama" diye bir terim kullandım. Öyle yerleşik bir kavram yokmuş. Yerleşik olanı "epistemik sınır ihlali" — bir alanda uzman olanın statüsünü alan dışına taşıması.)*

---

## 9. Ajan atama meselesi

Bunu bir kere daha söylüyorum çünkü karar senin.

**Kendi koyduğun kapılara takılıyor.** İlk canlı ajan kartı bloke ve tetiği dört kanıt kapısına bağlı; şu an birinci kapının sayacı bile tartışmalı. "Ajan atayalım" demek, kendi koyduğun kanıt kapılarını atlamak demek.

**Ama tam blok da değil.** Ekip lideri hattını sen paralel ilan etmiştin ve önkoşulu "tasarım paketi + araştırma". Öğrenme ajanı tam o sınıfa giriyor.

**Ayrım şu:** tasarım paketi bugün üretilebilir — raporda var, yazdım. Devreye alma kapıya bağlı.

Bir de araştırmadan çıkan üç şey, ajan tasarımını doğrudan şekillendiriyor:

- **"Ajanı eğitmek" ağırlık güncellemesi değil.** Bizim ekosistemimizde eğitim demek: rol tanımı + beceri dosyası + araç kısıtı + **kalıcı hafıza dizini**. Ve tam da istediğin mekanizma hazır: alt-ajan tanımına kalıcı hafıza verilebiliyor. Bu, birinci bölümdeki "seviye modeli dosyada yaşamalı" sonucunun doğrudan uygulaması.
- **Çoklu-ajanın üstünlüğü token'la karışmış.** En çok alıntılanan "çoklu-ajan tek ajanı %90 geçti" rakamının yanında, aynı kaynağın ikinci bulgusu duruyor: performans farkının **%80'ini harcanan token miktarı açıklıyor**, ve maliyet 15 kat. **Eşit token verilmiş bir karşılaştırma hiç yapılmamış.** Yani "ajan atayınca daha iyi olur" iddiasının ne kadarının rolden, ne kadarının paradan geldiği bilinmiyor.
- **Ajan kendi işini onaylayamaz.** Ölçülmüş: modeller kendi çıktılarını değerlendirirken sistematik olarak iyimser sapıyor. Kaynağın ifadesiyle, "%30 tamamlanmışken tam güvenle teslim eden ajan" elde ediyorsun.

---

## 10. Bu raporun kendi hatası

Bir şeyi kaydediyorum çünkü ders listesine giriyor.

Alt-ajanlar oturum limitine çarpıp öldüğünde "bekleyip elimdekini yazayım" dedim. Saate bakmadım. Baksaydım limitin on iki dakika önce sıfırlandığını görecektim.

Yani **kaynak tükendi** ile **iş bitti**'yi karıştırdım — araştırdığımız hatanın tam olarak insan tarafındaki hali. Doğru refleks ölçmekti, tahmin etmek değil.

Sen uyardın, ölçtüm, işi sürdürdüm.

---

## Sırada ne var

Dört araştırma daha koşuyor: telefondan senkron proje inşası, bu raporun kendisi gibi metinleri sadeleştiren "compiler" katmanı, ajanlar arası iletişimin graf tasarımı, ve araştırma ajanına hukuksal katman. Onlar inince bu belgeye eklenecek.

**Senden beklenen kararlar** teknik raporun yirminci bölümünde madde madde duruyor. En acil ikisi:

1. **Öğrenme modeli** — önerim "önce dene, sonra oku".
2. **Kategori şeması** — X'i ikiye bölmek. Bu kanonu değiştirir, yani yalnız senin imzanla olur.
