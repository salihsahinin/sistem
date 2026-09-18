# 1 Ağustos'un on raporu — sade anlatım

*Bu dosya, 2026-08-01 günü üretilen on teknik raporun insan-yüzü sürümüdür. Aynı hükümler, aynı sayılar, anlatı diliyle. Teknik sürümler kanıt içindir, bu sürüm anlamak içindir; her bölümün sonunda kaynağın adresi var.*

*Bir usul notu: bu derlemenin kendisi emrindeki $8 maliyet tavanını aştı ($12,69 ölçüldü). Aşımın dökümü ve nedeni `cc/rapor-2026-08-01-6.md` dosyasında; okuma dosyası tam teslim edildi.*

---

## 0. Bu on rapor birlikte ne anlatıyor

Bir gün içinde on rapor çıktı ve hepsi ayrı işlere bakıyor: bir ölçekleme çalışması, bir çeviri mekanizması tasarımı, bağlam şişmesi ölçümü, geçmiş kayıtların yedeklenmesi, iki vardiya teslimi, üç ayrı damıtma turu ve bir de bunları kırmaya çalışan denetim. Konular dağınık. Ama aralarından **üç tane tekrar eden desen** geçiyor, ve asıl okunması gereken şey o.

**Birincisi: yazılmış kural kendiliğinden çalışmıyor.** Bu, günün en çok tekrarlanan bulgusu ve her seferinde başka bir yerden çıktı. Çeviri kurallarını içeren formül altı gün önce zaten yazılmıştı — dört ayrı olayda o iş elle yapıldı, kurallar yalnız bir olayda uygulandı, çünkü kurallar çağrılabilir bir yerde durmuyordu (§8). Ölçülmüş bir başka örnek: bir karar-modeli kuralı 28'den fazla kez koştu, o kurala ait yardımcı dosya hiçbirinde çağrılmadı; iki yardımcı dosya 53 oturumda sıfır kez kendiliğinden tetiklendi (§6). Emirde "tüm alt-görevliler ucuz modelde koşsun" yazıyordu — şart, görevlinin kendi içinde çağırdığı katmana ulaşmıyor, denetlenemiyor (§1). Ve bu derlemenin kendisi aynı aileye üçüncü örneği ekledi: maliyet tavanı yalnız emir metnindeydi, aşıldı. Ortak sonuç sertleşerek çıkıyor: **kısıt, denetlenebilen yüzeyde kurulmazsa kısıt değildir.**

**İkincisi: "biliyoruz" sandığımız şeylerin çoğu ölçülmemişti.** Günün ayırt edici hareketi, hükümlerin kendilerine değil, dayanaklarına bakmak oldu. "Bağlam şişti" hükmü yıllardır kullanılıyordu — 57 oturum ölçüldüğünde ortaya çıktı ki bu bir ölçüm değil, bir izlenim; ve ölçüm, sezilen ilişkiyi doğrulamadı (§9). Uç-birim genişliğinin ölçekle sabit kaldığı iddiası ne doğrulandı ne çürütüldü, **daraltıldı** — sabitliğin kaynağı ölçek değil, sistem-ailesi kimliği çıktı (§2). Ve en sert sınav: dışarıdan literatüre dayandırılan 35 iddia kasten çürütülmeye çalışıldı; 16'sı ayakta kaldı, 13'ü daraldı, 5'i düştü (§7). Düşenlerden ikisi bizim lehimize düştü — karşıt sanılan kanıt kendi tarafımızı güçlendirdi.

**Üçüncüsü: bugün eşik koymayı bilerek reddettik.** Hem bağlam sayacında (§9) hem ölçekleme kararında (§2) aynı refleks çalıştı: veri yetersizken sayı seçmek kura çekmektir. Bağlam eşiğinde bu ölçüldü — aday eşik 150 binden 300 bine kaydırıldığında ateşleme oranı %81,5'ten %22,2'ye düşüyor; yani seçilen sayıya göre sonuç baştan aşağı değişiyor. Önerilen yol her ikisinde de aynı: önce **sessiz ölç**, hükmü sonra bağla.

Bir de zaman baskısı var, ve tek satırla önemli: bütün bu ölçümlerin dayandığı ham kayıtlar 30 günde bir siliniyordu; 10-11 Ağustos'ta ilk kayıp başlayacaktı. Yedek alındı (§4), sonra ayarın kendisi değiştirilip sorun sınıfı kökten kapatıldı (§3).

---

## 1. Karantina usulüyle koşulan bir ölçekleme raporunun kanona girişi

Bu bölümün kaynağı, "ölçekleme" (bir sistemin büyüklüğü arttıkça davranışının nasıl değiştiğini ölçen çalışma türü) başlıklı bir koşumun ingest'ini (ham raporun hangi hükmünün kanona geçeceğinin karara bağlanması) anlatıyor. Soru: ham rapor doğrudan ana karar hattına mı girsin, arada süzgeç mi olsun? Cevap "karantina deseni" oldu — ham rapor ana hatta hiç girmedi (ikinci kez uygulanan bir ihtiyat kuralı); bir alt-görevli (Sonnet adlı modelle çalışan yardımcı) raporu okuyup nötr hükümler ve bir sözlük çıkardı, iki koşumda ≈122 bin token (işlem birimi) harcayarak. Hakemlik Carvis'te kaldı, kararlar Salih'e ait. Kimlik tutarlı bulunduğu, güvenlik siperi tetiklenmediği ve iç çelişki saptanmadığı için koşum KABUL damgası aldı.

Ne bulundu: Maliyet karşı-okuması ölçüldü — 16 dolarlık tavana karşı 12 dolar harcanmış (tavanın %75'i), aşım yok; panel rakamıyla birebir örtüştü. İki ölçek-katsayısı ölçülüp kabul edildi: biri +0,0957 (76 örneklem, sapma ±0,018) — önceden sabit sanılan bir taşınan-kaynak değerinin aslında sistem-ailesi içi tasarım sabiti olduğu çıktı; ikincisi 0,7569 (31 örneklem, sapma ±0,0588) — "bu katsayı 1'dir" varsayımı reddedildi. İkisi ölçüm-bankı dosyasına yazıldı.

Bir usul sorunu da çıktı: emirde "tüm alt-görevliler Sonnet çalışsın" şartı vardı, ama bu yalnız görevlinin başlatılma modelini kapsıyor — içinde çağırdığı araçların modeli (Haiku adlı modelle 1,11 dolara 34 arama) dışarıdan görülemiyor, denetlenemiyor. Sapma kapsam dışı sayıldı ama her raporda bildirilmesi karara bağlandı — "yazılmış ama uygulanmayan şart" ailesinin üçüncü örneği; sonuç: kısıt denetlenebilen yüzeyde (panel/işlem kaydı) kurulmalı, yalnız talimatta yazmak yetmiyor. Belgede iki kez "bağlantı yarıda kesildi" uyarısı var — aktarım sorunu; veri kesintiden önce tamamdı.

Ne değişti: nötr sözlük küçük düzeltmeyle kanona girdi; bir devir maddesi girdi gelmediği için kapandı; ölçüm-bankı dosyası açılıp iki katsayı işlendi; üçüncü ölçüm bugün koşulmadı, sıraya alındı (maliyet sınıfı henüz doğrulanmadı).

→ kaynak: `raporlar/2026-08-01-ingest-0801-5.md`

---

## 2. Büyüklük arttıkça neyin sabit kaldığı, neyin değiştiği: iki ölçüm, bir açık soru

Kuyruğa düşen bir ham fikir, büyüyen sistemlerde bazı iç oranların ölçek büyüse de sabit kalıp kalmadığını iddia ediyordu. Koşum üç ölçütü test etmek için açıldı: bir sistemin en küçük tekrar eden işlem biriminin ("uç-birim") iç kapasitesi ölçekle sabit mi; sistemin ölçeğine karşı iş-görme payının üstel ilişkisi ("debi") ne kadar; sistemin tek seferde işleyebildiği taşınan-kaynak üst sınırı ("kullanım ufku") ölçekle ne hızda büyüyor. Soru pratikti: bu büyüme hızları birbirine eşitse büyütmek nötr çıkar, biri diğerini geçerse büyütmek ya kârlı ya da zararlı hale gelir.

### Uç-birim genişliği: iddia ne doğrulandı ne çürütüldü, daraltıldı

76 sistem, 26 sistem-ailesi ve ölçekte ~9000 kat aralık üzerinde sayıldı (ölçüldü). Sonuç: uç-birim genişliği tam sabit DEĞİL — zayıf ama gerçek bir yukarı sürüklenme ölçüldü (üs +0,096, sıfırdan istatistiksel olarak ayrışıyor) — ama bu, aynı aralıkta uç-birim *sayısının* (üs +0,287) ve katman sayısının (üs +0,251) büyüme hızının yaklaşık üçte biri kadar zayıf. Genişliğin değişkenliğinin yalnız %28'i ölçekle açıklanıyor (dört birimlik değişkenlikten üçü ölçek-dışı bir nedenden geliyor); katman sayısında bu oran %86'ya çıkıyor — derinlik gerçekten ölçek-güdümlü, genişlik değil.

Ayrıştırma turunda daha önemli bir bulgu çıktı: bant dışına düşen 12 satırın 9'u yalnız iki komşu sistem-ailesine ait. Bu iki aile çıkarılınca sürüklenme küçülüyor ama sıfırlanmıyor (ölçüldü). Aile-içi bakış çok daha net: bir sistem-ailesi ölçeğini 392 kat büyütürken uç-birim genişliğini hiç değiştirmiyor; başka bir aile 3240 kat ölçek aralığını yalnız iki değerle geçiyor. Sonuç: bu bir ölçek yasası değil, ailenin ölçekten bağımsız tuttuğu bir tasarım sabiti — sapmanın ekseni ölçek değil, aile kimliği (çıkarım). İki sistemde de uç-birim genişliği tek sayıya hiç indirgenemiyor; bunlar ölçüm dışında ayrı işaretlendi (çıkarım).

### Debi: ölçüldü, ekonomi var ama zayıf

Debinin öz-pay bileşeni (γ_öz) — üreticinin açıkça yayımladığı 31 veri noktasından — 0,757 ölçüldü, %95 güven aralığı [0,637, 0,877]. "Debi ölçekle tam orantılı büyür" varsayımı istatistiksel olarak reddedildi: gerçek bir ölçek-ekonomisi var ama zayıf. Daha önce yasaklanmış, yalnız iki uç noktadan çizilen kestirim de çürütüldü — o yöntem 0,395 verirdi, ölçülen aralığın tamamen dışında; yasağın haklılığı olgusal olarak da doğrulandı.

Üç çekince eşlik ediyor: yıla göre kayma belirsiz kaldı (erken/geç dönem aralıkları örtüşüyor — yetersiz veri); aile payı ayrıştırılamadığından raporlanan aralığın gerçek belirsizliğin alt sınırı olduğu düşünülüyor (çıkarım); ve en önemlisi, ölçüm yalnız "az kaynak kullanmayı seçen" sistemlerde koşuldu — seçmeyenlerde oran tanım gereği zaten tam orantılı, dolayısıyla 0,757 "alanın genel kuralı" değil "azaltmayı seçenler arasındaki eğilim" (çıkarım, kanıt değil). Debinin taşınan-kaynak-payı bileşeni bu koşumda hiç ölçülmedi.

### Kullanım ufku: bu turda hiç ölçülmedi

Üçüncü ölçüt bilinçli olarak kapalı tutuldu, sıfır veri toplandı. Üç ölçüm tasarımı seçeneği hazırlandı: en ucuzu yanıltıcı çıkma riski taşıdığı için önerilmedi, orta-maliyetli seçenek önerildi, en pahalısı en doğru ama farklı bir soruyu cevapladığı için ayrı külfet getiriyor (çıkarım). Kırılma noktası sayısal biliniyor: bu üssün 0,76'nın altında çıkması "çok sayıda küçük birim", üstünde çıkması "büyütmek kârlı" kararını doğruluyor; debi aralığının içinde (0,637–0,877) çıkarsa karar verilemiyor.

### Ne değişti

Karar Salih'e ait ve kapanmadı, ama iki şey netleşti. Geriye kalan tek bilinmeyen kullanım ufku olduğu için soru "bilinmiyor"dan "tek ölçüme indirgendi" durumuna taşındı. Ayrıca ufuk beklenmeden kullanılabilir bir sonuç çıktı: debiyi ölçekle tam orantılı sayan bir tahsis kuralı, 100 kat ölçek farkında yaklaşık 3 kat fazla kaynak ayırır (ölçüldü, bant 1,76–5,33 kat); tersi de geçerli — ölçek 100 kat büyüdüğünde çevrim frekansı 100 kat değil, yalnız ~3 kat düşer. Üç açık soru Salih'e bırakıldı: nötr sözlüğün kanona girip girmeyeceği (sözlük fiilen sınandı, iki terimde revizyon ihtiyacı çıktı), iki ölçülen üssün bir ölçüm-bankına yazılıp yazılmayacağı, ve kullanım-ufku ölçümünün ikinci bir tura açılıp açılmayacağı.

*(Tutarlılık notu: bu üç sorudan ilk ikisi §1'deki ingest turunda kapandı — sözlük kanona girdi, iki üs ölçüm-bankına işlendi. Açık kalan tek kalem kullanım-ufku ölçümüdür.)*

→ kaynak: `cc/rapor-2026-08-01-5.md`

---

## 3. Gece vardiyasının teslim raporu — bir günlük bekleyen işlerin nasıl kapandığı

Bu rapor, 2026-08-01 günü öğleden geceye uzanan vardiyanın teslim belgesi; soru: bugün gerçekten ne değişti, hangi kararlar alındı, hangi işler karar bekliyor?

Ne değişti: Önceki günden (07-30) kalan 26 raporun ingest (ham raporun hangi hükmünün kanona geçeceğinin karara bağlanması) borcu tamamen kapandı — kalan 12 rapor bir alt-görevli tarafından damıtılarak işlendi, 10'u KABUL şerhli, 2'si KISMEN, sıfırı reddedildi; sayım da düzeltildi: önceki "12/26" kaydı sayım hatasıymış, gerçek durum 14/26'ymış. Bir yüzey testinde, Cowork'teki bir arama-aracının döndürdüğü nesnede görev-kimliği alanı YOK, mesajlaşma aracı da çalışmıyor bulundu — önceden saptanmış bir bulgu doğrulandı.

İki rapor daha ingest edildi: ana bulgu, "bağlam şişti" hükmünün bugüne kadar bir ÖLÇÜM değil bir İHTİYAT bildirimi olduğuydu — doğrulanmamış bir izlenimdi; Cowork'te makine-okunur kayıt olmadığı için, ortam geçişinin kendisinin ölçüm aracı haline geldiği belirlendi. Ayrıca bir modelin sabitlenmesi kararının Salih imzalı olduğu ortaya çıktı — bu kararın önem sınıfını yükseltti.

İki görev emri daha derlenip koşuldu ve ingest edildi: biri iz-hasadı (kanıt yedekleme) — 231 MB'lık 5 yedek + 74 oturumun damıtılmış hasadı, doğrulama 3/3 tutarlı, KABUL damgalı. Öbürü bir karşı-tez turu — 35 iddia değerlendirildi (16 doğrulandı, 13 daraltıldı, 5 çürüdü, 1 açık kaldı); öne çıkan bulgu, iki dış iddianın LEHTE çürümesiydi — karşıt sanılan kanıt kendi tarafımızı güçlendirdi.

Üçüncü emir (ölçekleme işi) yeni bir yöntemle derlendi: ana karar hattı devir dosyasının ham içeriğini hiç görmedi, bir alt-görevli okuyup aktardı — Salih'in kısa bir gözleminin doğurduğu ihtiyat kararıydı.

Kararlar: "Temizlik periyodu" adlı bir sistem ayarı 365 (gün) olarak sabitlendi — bir silme sorunları sınıfının kökten kapatılması demek, bedeli gizlilik penceresinin 12 aya çıkması (Salih kabul etti). Kişisel projeler şirket deposuna girmeyecek — riskleri Salih kendi yedeğiyle aynı gece kapattı. Masa toplantısı bilinçli olarak SONRAKİ oturuma ertelendi — gerekçe, taze bağlamın daha verimli olduğu bulgusu.

Dersler: "[K] etiketi fren değil" — çıkarım şerhi düşmek bulgunun kullanılmasını durdurmuyor; gerçek fren ancak yapı/kural düzeyinde kurulursa işliyor (bugün 2 örnek daha eklendi). Sorunu tek tek kovalamak yerine kök ayarı değiştirmek tüm borç sınıfını birden kapattı. Bugün 9 ayrı iş alt-görevlilere verildi (≈680 bin token), hepsi çalıştı; hakemlik ana hatta kaldı. Kapanışta bir dosyanın boyut sınırının ≈2,1 katına ulaştığı ölçüldü — düzenli sıkıştırma zaten planlanmış bir madde.

→ kaynak: `raporlar/vardiya-teslim-2026-08-01-anasira-2.md`

---

## 4. İz hasadı: silinmeden önce ne kurtarıldı, ne öğrenildi

Bu rapor, JARVIS'in geçmiş oturumlarının teknik izlerinin (Claude Code'un her oturumda arka planda tuttuğu ham kayıt dosyaları — konuşmanın turunu turuna dökümü) 30 günde bir otomatik silinme riski taşıdığının fark edilmesi üzerine yazıldı. Soru basitti: bu izler kaybolmadan önce ne kurtarılabilir, ve kurtarılanlardan ne öğrenilir?

Önce tam bir envanter çıkarıldı: bilgisayardaki tüm proje klasörleri tarandı (ölçüldü). Bunların arasında JARVIS'le ilgili olmayan kişisel klasörler de vardı; Salih'e soruldu ve onayı alınarak kapsam JARVIS'le ilişkili 5 klasörle sınırlandı — diğerleri "kapsam dışı" işaretlendi ama silinme riskleri hâlâ geçerli, bu koşumda dokunulmadı. JARVIS kapsamındaki izler 409 dosya, yaklaşık 231 megabayt tuttu (ölçüldü); kapsam dışındakiler 562 dosya, yaklaşık 34,6 megabayt — bunlar yedeklenmeden bırakıldı. En eski JARVIS dosyasının tarihine bakılarak, mevcut silme kuralıyla ilk kaybın yaklaşık 10-11 Ağustos'ta başlayabileceği önceki bir kayıttan aktarıldı, bu koşumda yeniden ölçülmedi.

Sonra bu 5 klasör tek tek sıkıştırılıp yedeklendi; kaynak ile yedekteki dosya sayıları birebir eşleşti (ölçüldü). Ayrıca 26 dosya rastgele seçilip bayt bayt karşılaştırıldı: 25'i birebir tuttu, 1'i tutmadı — nedeni araştırıldı ve bir bozulma değil, yedek alınırken başka bir açık oturumun o dosyaya hâlâ yazıyor olması olarak açıklandı (tek vakalık bir ölçüm, hüküm verilmedi). Buradan çıkan somut öneri: 9-10 Ağustos civarında, tüm açık oturumlar kapandıktan sonra bir yedek daha alınsın.

Son adımda bir betik (küçük program) yazılarak bu 5 klasördeki 74 oturumdan özet sayılar çıkarıldı (iz-hasadı = ham kayıttan ölçüm damıtma işi): kaç oturumda hangi model kullanıldı, kaç hata çıktı, hangi yardımcı araçlar çağrıldı gibi. Bir maliyet alanı da hesaplandı (yaklaşık 1.160 dolar, 70 oturum üzerinden) ama bu rakama çıplak güven verilmedi — önceki bir ölçüm bu hesaplama motorunun benzer örneklemlerde rakamı yaklaşık 2,3 kat şişirdiğini göstermişti; burada aynı düzeltme yeniden uygulanmadı, o yüzden sayı yalnızca "muhtemelen şişik" yönü taşıyor, düzeltilmiş bir sonuç değil. Doğrulama için 3 oturum önceden belirlenmiş rastgele seçimle elle yeniden sayıldı ve üçü de birebir tuttu.

Ortaya çıkan karar sorusu Salih'e bırakıldı: otomatik silme süresi büyütülsün mü (örneğin 30 günden 90 güne, ya da sınırsıza) yoksa mevcut 30 gün kalıp bu tür hasat koşumları periyodik mi tekrarlansın? İki seçenek de artı-eksileriyle sunuldu, üçüncü yol istenmedi; henüz karar verilmedi.

*(Tutarlılık notu: bu soru aynı gece kapandı — §3'te temizlik periyodu 365 güne sabitlendi. Açık kalan tek kalem, 9-10 Ağustos'taki ikinci yedek önerisidir.)*

→ kaynak: `cc/rapor-2026-08-01-3.md`

---

## 5. İki CC raporu ana sıradan geçti: formül doğrulandı, şişme kanıtlanamadı

Bu bölüm, 08-01 tarihli iki CC (yan-oturumda öneri üreten, kanonu kilitleyemeyen çalışma hattı) raporunun üst karar hattınca (ana-sıra) değerlendirilip damgalanmasının kaydı. Kural şu: CC'nin kendi kullanım verisini yorumlaması tek başına kanıt sayılmaz, YORUM statüsünde kalır — yön kararını üst model verir.

Birinci rapor "semantik compiler" (teknik raporları sade dile çeviren formül/süreç) üstüneydi. Raporun ön-tespiti hatalıydı: "bu daha önce araştırılmamış" dedi, oysa formül önceki bir raporda zaten vardı. Ölçüldü ki formül çalışıyor: 6 dosyadaki 70 iddianın hiçbiri boş niteleyici (iddiaya eklenen güven-etiketi) bırakmamış, 145 kaynak-bağlantısı sağlam, iddiaların %88,6'sı kanıt-temelli. Asıl sorun uygulanabilirlik: 4 üretim olayından yalnız 1'inde kural seti fiilen uygulanmış. "İki-kip" kuralı kaynağın 1,26 katı hacimde çıktı üretiyor — önceki bir hacim kuralıyla çelişiyor. Ana-sıra hükmü: KISMEN KABUL. Şerhler: ön-tespit hatası emri veren tarafın kendi hatası sayıldı; bir bulgu ailesi birincil kaynağa hiç inmeden yalnız çıkarım (kanıt değil akıl yürütme) kaldı; bazı kullanım-verisi hükümleri YORUM sayıldı; raporun kendisi de kendi hacim kuralını ihlal etti (71,2 KB, gece ortalamasının 1,32 katı).

İkinci rapor, "bağlam şişmesi" (oturumun model belleğini ne kadar doldurduğu) için otomatik uyarı eşiği kurulabilir mi sorusunu ele aldı. Bağlam doluluğu diskten gerçekten ölçülebiliyor (57 oturum ölçüldü), ama önerilen eşik-tetik DOĞRULANAMADI: doluluk ile araç-hatası arasında orantılı ilişki çıkmadı, istatistiksel test eşiği geçmedi, model otomatik düşürme 57 oturumun hiçbirinde tetiklenmedi (800 bin token'a, 41,7 saate varan oturumlarda bile). Rapor bu yüzden eşik ÖNERMEDİ; önce sessiz sayaç kurulup veriyle kalibre edilsin, hüküm SONRA bağlansın dedi. Yan bulgu: Cowork yüzeyinde makine-okunur kayıt olmadığından orada sayaç kurulamıyor — CC'ye geçiş kendi başına bir ölçüm gerekçesi taşıyor. Ana-sıra hükmü: KABUL, şerhli — ölçümler yerel/tekrarlanabilir sayıldı, dış literatür karşılaştırması henüz koşulmadı, bazı öz-maliyet rakamları YORUM kaldı.

Aynı gece koşulan karşı-tez turu 35 dış iddiayı sınadı: 16'sı doğrulandı, 13'ü daraltıldı, 5'i çürüdü, 7'si "çıkarım"dan "ölçüldü/belgede" statüsüne yükseldi. Dikkat çekici düzeltme: bir kaynak atfı yanlış makaleyi göstermiş — taşıdığı hükümler başka dayanaklarla ayakta kaldı; ders kayda geçti: "çıkarım damgası fren değil etikettir" — şerhli bulgu kullanımdan alıkonmuyor, yalnız etiketleniyor. Model-sabitleme gerekçesi de zayıfladı, ayrı ölçüm gerekli görüldü. Karar: iki raporun ortak deseni (dış-tetikleyici + varsayılan kapalı/sessiz tasarım) bağımsız iki emirde aynı sonuca varması, yakınsama noktası olarak kaydedildi; eşik konusunda henüz imzalı kural yok.

→ kaynak: `raporlar/2026-08-01-ingest-0801-raporlari.md`

---

## 6. Bekleyen on iki raporun büyük temizliği: kurallar neden kendiliğinden çalışmıyor

Bu rapor, 30 Temmuz'da açılan ③ turunun elde kalan 12 raporunu kapatmak için yazıldı. Soru şuydu: bu 12 ham rapordan hangi hükümler kanona (şirketin resmî karar defterine) girmeye layık, hangileri askıda kalmalı? Yöntem üç alt-ajanın toplam yaklaşık 498 bin token'lık malzemeyi damıtması (ham rapordan yalnız kanona girecek hükmün süzülmesi) ve ardından Carvis'in ana-sıra olarak hakemlik yapmasıydı. Yol boyunca bir sayım hatası da düzeltildi: kapsülde tur öncesi durum "12/26" yazıyordu, gerçekte 14/26 imiş (iki eski damga zaten defterde kayıtlıydı ama sayılmamıştı); bu turla birlikte 26 raporun tamamı işlenmiş oldu.

On iki raporun onu "KABUL, şerhli" (hüküm kabul edildi ama yanına uyarı notu eklendi) damgası aldı, ikisi — "konuşma üslubu" ve "sistem = çağrılabilir yardımcı dosya" — yalnızca "KISMEN" kabul gördü. Ortak bir örüntü tekrar tekrar çıktı: kural yazılı olsa bile kendiliğinden çalışmıyor. Örneğin bir raporda ölçüldü: m.37 kuralı 28 kereden fazla koşmuş ama karar-modeli adlı yardımcı dosya hiçbirinde çağrılmamış; celiski-kapisi ve karar-hatti dosyaları 53 oturumda sıfır kere kendiliğinden tetiklenmiş — yardımcı dosya yalnız emirde adıyla anılınca çalışıyor, durumun kendisi onu tetiklemiyor. Aynı ailenin başka bir üyesinde ölçüldü: atlas-kosum dosyası devreye girmeden önce dört hedefe birden ulaşma oranı sıfırmış, kurulduktan sonra 125 koşumda bu oran %88'e çıkmış — ama %12,3'lük bir sapma da var, disiplin bloğu her koşumda tam uygulanmamış (bu ölçüm kendi karşı-denemesinden geçmedi, üç ayrı karşı-ajanın denetimi koşulmadı; bu yüzden çıkarım damgasında bırakıldı).

Bir başka raporda 734 kalın yazılmış ifade sayıldı; bunların yaklaşık dörtte biri gerçek vurgu, geri kalanı yapı taşı ya da etiket işlevi görüyormuş — ama raporun kendi ilk ölçümleri en az iki yerde yanlış çıkmış, kendi karşı-tezi bunu düzeltmiş (KABUL, sert şerhli). Ölçüm disiplini teması başka raporlarda da sürdü: birinde ölçüldü, çağrı oranı hedef haline getirilince (bir ölçütü hedef yapınca ölçütün kendisinin bozulması) iş değişmeden maliyet 3,67 kat artmış. Bir diğerinde somut bir güvenlik bulgusu çıktı: erişim anahtarı (PAT) `.git/config` dosyasında düz metin duruyormuş — bu, klasörün kopyalanmasının neden yasak olduğunun gerekçesi olarak kayda geçti. Son raporda doğrulanan 7 hatanın 7'si de sayım ya da kaynak-atfı hatasıymış, uydurma kaynak ya da kırık pointer sıfır çıkmış; bu onarım aynı gün zaten uygulanmış.

Katman-1'e (yalnız Salih'in karar vereceği kalemler) düşen adaylar tek tek uygulanmadı, hepsi `kuyruk/masa-gundemi-2026-07-30.md` dosyasının EK-3 bölümünde toplu bekliyor — aralarında yardımcı-dosya çağırma dilinin tek tip imzası, atlas-kosum'un `tools/` klasörüne taşınması, md.44'ün 19 gündür uygulanmamış olması gibi kalemler var. Katman-2 (Carvis'in doğrudan yapıp kaydedebileceği) kalemler ise doğrudan işlendi. Ayrıca bir sayı zinciri düzeltmesi zincirleme yaşandı: bir raporun "oturum başına 0,05 yardımcı-dosya çağrısı" rakamı bayat çıktı, sonraki rapor bunu 0,38 olarak güncelledi. Nihaî kayıt `kuyruk/senaryo-defteri.md` dosyasının son bloğuna işlendi.

→ kaynak: `raporlar/2026-08-01-ingest-3-damitma.md`

---

## 7. İddiaları kırmaya çalıştık, çoğu ayakta kaldı — ama en önemli beşi düştü

Bu bölümün kaynağı bir "antitez turu" — yani daha önce yazılmış iki raporun (08-01-1 ve 08-01-2) dışarıdan literatüre dayandırdığı iddiaları, onları kasten çürütmeye çalışan ayrı bir denetim koşumu. Neden gerekti: 08-01-2 kendi içinde bir itiraf bırakmıştı — "bu iddialar künye kontrolünden geçti ama kasıtlı çürütme sınavından geçmedi." Bu koşum tam o eksik sınavı verdi, aynı anda rapor-1'in de hiç dokunulmamış bir köşesini (hiç birincil kaynağa inilmemiş 12 iddia) kapsama aldı. Dört alt-ajan (ucuz model, Sonnet) paralel çalıştı, sonra ana döngüde beş hüküm dört ayrı yöntemle çapraz denetlendi.

Sonuç: 35 dışarıdan-literatür iddiası sınandı; 16'sı birincil kaynaktan doğrulandı (kaynağı bulundu, metin birebir okundu), 13'ü daraltıldı (iddia genel hatlarıyla doğru ama rakamı ya da kapsamı kaynakta yazandan dar), 5'i çürütüldü, 1'i "aranamadı"ya düştü (yani ne doğrulanabildi ne çürütülebildi, belirsiz kaldı).

Beş çürüyenin ikisi önemliydi. Birincisi: rapor-1'in bir hükmü ("üretici ile doğrulayıcı arasındaki yetenek farkı, öznel-üslup gibi alanlarda geçerli değil") bir arXiv makalesine dayandırılmıştı — makale gerçekten var ama içeriği başka bir konu (matematik/bilgi görevlerinde doğrulayıcı davranışı); "üslup", "yaratıcı" gibi kelimeler o makalenin tam metninde hiç geçmiyor. Yani künye gerçekti ama içerik uyuşmuyordu — belgeden doğrudan okunarak tespit edildi. Bu, rapor-1'in "ayrı bir denetleyici mekanizma yapay zekâ olmamalı" mimarisinin dış dayanağını düşürdü; hüküm iç ölçümle hâlâ ayakta ama artık tek ayak eksik.

İkincisi ters yönde çalıştı, ve daha değerliydi: rapor-1 "yapılandırılmış şablon ile serbest yeniden-yazımı karşılaştıran çalışma literatürde yok" demişti. Bu iddia da çürüdü — ama çürümesi rapor-1'in lehine: iki doğrudan karşılaştırma bulundu ve ikisi de şablon/kontrol-listesi lehine çıktı (6,90'a karşı 6,70; 7,50'ye karşı 5,67; ikisi de belgeden okundu). Yani "yol A" dediğimiz yaklaşımın (yardımcı dosyaların kural taşıyıcısı olması) daha önce hiç sahip olmadığı bir dış kanıt ortaya çıktı.

Üçüncü önemli çürüme rapor-2'ye ait: "N=50-200 gibi küçük örneklem aralığında literatür sessiz kalır" demişti — sessiz değilmiş. "Kısa-koşum istatistiksel süreç kontrolü" adında, tam bu ölçek aralığını hedefleyen köklü bir alt-literatür var; dört ayrı akademik künye bağımsız doğrulandı. Bunun anlamı: kalibrasyon tasarımı artık "hiçbir emsal yok, sıfırdan mühendislik gerek" değil, "okunmamış bir literatür rafı var" haline geldi.

Ayrıca bir düzeltme: rapor-2 bir ortam değişkenini (`CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`) "üçüncü-parti kaynaklı" diye işaretlemişti — yanlış sayfaya bakmış; değişken aslında resmî belgede yazıyor. Ama rapor-2'nin öne sürdüğü "%83" eşik rakamı altı resmî sayfanın hiçbirinde geçmiyor; resmî rakam Sonnet-5/1M için yaklaşık 967 bin token. Sonuç ilginç bir tersine dönüş: %83 rakamı yanlış yerdeydi ama yanlış olan eşik değil, bizim doluluk oranımızmış — gerçek eşikle yeniden hesaplanınca en dolu oturum bile eşiğin %82,7'sinde kalmış, yani "kapasite tetiği hiç ateşlenmedi" hükmü daha da güçlenmiş oldu.

Denetimin kendisi de bir kez hata yaptı ve bunu kayda geçirdi: ana döngü ilk turda altı resmî sayfadan birini taramadan "%83 hiçbir yerde yok" diye yazmış; sonraki bağımsız kontrol bunu düzeltti. Bu, "aranamadı"yı "yoktur" gibi okumanın yedinci kaydedilmiş örneği — bu kez hatayı yapan denetimin kendisiydi.

Kararı doğrudan etkileyen üç kalem — 08-01-2'nin öne sürdüğü Yol-1 tercihi ve iki gerekçe maddesi — bu denetimden etkilenmedi, çünkü üçü de dışarıdan literatüre değil kendi iç ölçümümüze dayanıyor. Ayrı bir bulgu: bütçe hedefini aştık ($30,94, referans $16,34'tü) — nedeni bir referans belgesinin bağlama yüklenip her turda tekrar faturalanması ve iki alt-ajanın koyduğumuz çağrı tavanını (30) aşması (46 ve 60); tavan yalnız talimat metnindeydi, uygulayan bir mekanizma yoktu.

→ kaynak: `cc/rapor-2026-08-01-4.md`

---

## 8. Çeviri kuralları zaten yazılmıştı, kimse çağırmıyordu

Bu rapor, teknik JARVIS raporlarını (yapay zekâdan yapay zekâya yazılan yoğun, damgalı metin) senin okuyabileceğin sade Türkçeye çeviren bir mekanizma — "semantik derleyici" (kaynak metni sabit kurallara göre başka bir forma dönüştüren sistem) — kurulsun mu, nasıl kurulsun sorusuna cevap arıyordu. Emrin kendi ön-kontrolü "bu konuda önceki araştırma yok" diyordu.

İlk bulgu tam da bu ön-kontrolü çürüttü: 26 Temmuz tarihli `compiler-formulu.md` dosyası birincil kaynaktan okunarak doğrulandı ve zaten 15 ölçülmüş bulgu ile 9 kural içeren tam bir formül taşıyordu. Arama yalnız "semantik compiler" kelimesini taramıştı, dosyanın başlığında bu ifade hiç geçmiyordu. Bu yüzden soru değişti: yeniden tasarım değil, "formül zaten var, neden bir kereden fazla çalışmadı" sorusu.

Cevap ölçüldü: aynı çeviri işi dört ayrı olayda dört farklı kuralla elle yapılmış; kurallar yalnız BİR olayda (kuralların doğrudan emir metnine yapıştırıldığı olayda) tam uygulanmış. O tek olayda sonuç iyiydi — sayıldı: 145 çapraz-referansın (kaynağa "→ dosya §bölüm" biçiminde geri işaret eden bağlantı) 145'i sağlam çıktı, kırık sıfırdı. Ama kuralsız üç olayda hiç niteleyici (bir iddiaya ne kadar güvenildiğini gösteren etiket) yoktu. Demek ki arıza kuralların kalitesinde değil, kuralların hatırlanabilir olmamasında — kurallar tek bir yerde yaşamıyor, her seferinde emir metnine yeniden kopyalanması gerekiyordu.

Dış araştırma (kaynak dışı literatürden 40 iddialık bir tez + bu iddiaları çürütmeye çalışan karşı-tur) bir varsayımı da çürüttü: çok-aşamalı/çok-ajanlı mimarinin (işi art arda birden çok yapay-zekâ adımına bölen sistem) tek-geçişli üretimden (bir kerede, ek kontrol adımı olmadan üretim) üstün olduğu iddiasının en güçlü dayanağı, tam metinden okunduğunda kendi kendini çürüttü: orada karşılaştırılan "tek-geçiş" değildi, o da başka bir çok-ajanlı sistemdi (belgeden, tam metinden okundu). Kanıtın fiilen desteklediği tasarım: tek geçişte üret, sonra ayrı ve kurala-bağlı (yapay zekâya değil sabit bir betiğe dayanan) bir denetleyiciden geçir — yani zaten var olan formülün önerdiği şey.

Bir gerilim de ölçüldü: geçen ayki karar her rapor için iki farklı çeviri biçimi üretmeyi öngörüyordu, ama bu ölçüldüğünde kaynağın 1,26 katı yeni metin üretiyor — oysa ayrı bir ölçüm zaten "bekleyen-okunacak rapor hacmini küçültmek gerekir, büyütmek değil" hükmünü vermişti. Bu yüzden "her rapora otomatik iki çeviri" kuralının seçici bir tetiğe (hangi durumda çeviri otomatik yapılsın sorusuna kurala-bağlı verilen cevap) dönüştürülmesi öneriliyor.

Ayrıca, önceden konan bir eşik — aynı sınıf iş üç kez tekrarlanırsa otomatikleştirme adayı doğar — bu koşumda iki ayrı sınıfta doldu (ölçüldü): hem "teknik rapordan insan-yüzü metin üretme" işinde (4 olay sayıldı), hem "ölçüm aracının kendisinin yanılması" sınıfında (denetleyici betiği emoji işaretli bir başlığı tanıyamayıp 3 sahte hata bildirdi, düzeltilince hata sıfıra indi).

Sonuçta önerilen yön: kuralları emir metninden çıkarıp çağrılabilir tek bir yere (bir "skill" — belirli bir iş için tekrar tekrar çağrılabilen, kayıtlı talimat paketi) taşımak, yanına kurala-bağlı bir denetleyici koymak. Önerilen sıra: önce denetleyici betiği, sonra kısa/yalın üçüncü bir çeviri biçimi, en son skill dosyası — çünkü skill dosyası yazmak `core/` dizini gibi Salih imzası isteyen bir kilide giriyor, betik istemiyor. Ayrıca çeviri çıktısının hiç kanona işlenmemesi öneriliyor (yalnız kaynak teknik rapor kanona girer); gerekçe, çevirinin ölçülmüş bir hata kanalı olması ve kanona girerse o hatayı yayabilecek olması. Kalıcı, kendi başına çalışan bir "ajan" rolü kurma fikri bugün için reddedildi — kanıt buna gerekçe vermiyor. Nihaî karar Salih'in.

Raporda ayrıca şunlar var: "ekip lideri" vizyonu için dört kapılı bir kanıt-eşiği tasarımı (kurulmadı, Salih kararı bekliyor), üç çeviri biçiminin tam şablonları ve tek bir bölüm üzerinde elle yapılan bilgi-kaybı ölçümü, ucuz/pahalı model seçiminin hâlâ hipotez düzeyinde kaldığı bulgusu, ve raporun kendi belirlediği hacim kuralını ihlal ettiğinin itirafı.

→ kaynak: `cc/rapor-2026-08-01-1.md`

---

## 9. Bağlam gerçekten mi şişiyor, yoksa bu ölçülmemiş bir izlenim mi

Bu bölümün kaynağı, Salih'in doğrudan sorduğu bir soruya cevap arayan bir CC koşumu: "bağlamın şiştiğini anladığın noktanın matematiksel bir temeli var mı." Carvis'in "oturum ağırlaştı, bağlam şişti" hükmü şu ana kadar bir sayıya değil bir izlenime dayanıyordu. Rapor bunu sınamak için 57 CC oturumunun ham kayıt dosyalarını taradı — her asistan mesajının arkasında, o turda modele fiilen verilen bağlamın (bir oturumun o anda önünde tuttuğu metin miktarı) tam boyutu zaten kayıtlıymış; bu 57 oturumun tamamı için ölçüldü.

Ölçümün getirdiği ilk bulgu beklenmedik yönde çıktı: bağlam boyutu büyüdükçe araç kullanım hatalarının (bir dosya okuma/yazma gibi bir işlemi çağırırken başarısız olma) düzenli biçimde arttığı yönünde temiz bir ilişki yok (ölçüldü). Oturum-içi eşleştirilmiş test — aynı oturumun ilk yarısıyla ikinci yarısını karşılaştırıp tesadüfi dalgalanmayı ayıklayan istatistik yöntemi — fark anlamlı çıkmadı (p değeri 0,185; bu değer 0,05'in altında olsaydı "tesadüf değil" denebilirdi, olmadığı için denemiyoruz). Kaba bir toplu karşılaştırmada anlamlı görünen sonuç bile (p=0,00024) tek bir oturum çıkarılınca dağıldı (p=0,159) — yani o "güçlü" görünüm aslında tek bir vakanın omuzlarında duruyormuş (ölçüldü).

İkinci ve daha çarpıcı bulgu: Salih'in fiilen şikâyet ettiği olgu — model düşümü, yani oturum ortasında modelin daha zayıf bir sürüme geçmesi — 57 oturumun HİÇBİRİNDE görülmedi; en uzun oturum 800 bin birimlik bağlama ve 41,7 saate ulaşmasına rağmen (ölçüldü). Bu, "bağlam şişince düşüm olur" sezgisinin aleyhine bir bulgu, ama zayıf bir kanıt (CC ile Salih'in asıl şikâyet ettiği Cowork ana-arayüzü farklı model ve muhtemelen farklı bağlam penceresi kullanıyor, dolayısıyla ikisi doğrudan kıyaslanamıyor — doğrulanmadı).

Üçüncü bulgu, bir eşik ("şu sayıda uyar") seçmenin bugün neden riskli olduğunu gösteriyor: aday eşik 150 bin ile 300 bin birim arasında değiştirildiğinde, o eşiğin oturumlarda kaç kez ateşleyeceği oranı yüzde 81,5'ten yüzde 22,2'ye düşüyor (ölçüldü). Yani kalibrasyon verisi olmadan bugün bir sayı seçmek kura çekmeye eşdeğer — seçilen sayıya göre sonuç baştan aşağı değişiyor. Buna ek bir çıkarım: 1 milyon birimlik bağlam penceresinde otomatik sıkıştırma (oturum uzayınca eski kısımların özetlenmesi) hiçbir oturumda tetiklenmemiş, ama aynı oturumlar 200 bin birimlik bir pencerede çalışsaydı yarısından fazlası sıkışırdı — bu ikinci kısım koşullu bir çıkarım, çünkü Cowork'ün gerçek pencere boyutu bu yüzeyden görülemedi (doğrulanmadı).

Bu bulgular birlikte kararı değiştirdi: rapor bugün bir eşik sayısı önermiyor, bilerek. Önerilen yol ("Yol 1"), bugün yalnızca sessiz bir sayaç kurmak — bağlam boyutunu ve hata oranını arka planda kaydeden ama eşik altında hiçbir uyarı üretmeyen bir mekanizma — ve gerçek eşiği ancak yeterli veri birikince, ölçerek belirlemek. Asıl ayırt edici deney zaten planlanan bir adım: Salih'in önceliği olan ana-sıranın Cowork'ten Claude Code'a taşınması. Taşındığında model düşümleri ile o anki bağlam boyutu aynı kayıtta yan yana düşecek — yani göç, eşiğin ön-koşulu değil, eşiği kalibre edecek deneyin ta kendisi. Tek zamana bağlı uyarı: bu kalibrasyonun ham malzemesi olan kayıtlar 11 Ağustos'tan itibaren silinmeye başlıyor.

Raporda ayrıca şunlar var ve buraya taşınmadı: CUSUM/EWMA/ADWIN gibi istatistiksel bozulma-tespit yöntemlerinin teknik karşılaştırması (çıkarım/ikincil kaynak ağırlıklı), dış literatür taraması, Cowork ana-arayüzünün kaydına hiç erişilemediğinin tespiti, dokuz adet numaralı karar girdisi ve koşumun kendi maliyet dökümü.

→ kaynak: `cc/rapor-2026-08-01-2.md`

---

## 10. Gündüz vardiyasının teslimi — kayıt onarımı ve iki yeni CC emri

Bu rapor 2026-08-01 gündüz vardiyasının teslim belgesi; önceki günden kalan bir kayıt hatasının nasıl onarıldığını ve günün ilk emirlerinin nasıl derlendiğini anlatıyor.

Ne değişti: Bir önceki gün (07-30) Salih'in emrettiği kayıt onarımı KAPANDI — durum özetindeki (kapsül) 4 sayım hatası düzeltildi, birkaç dosyaya şerh düşüldü. Ana bulgu: bulunan 7 hatanın hepsi sayım ya da kaynak-gösterme sınıfındaydı — hiçbiri uydurma alıntı ya da kırık bağlantı değildi (7/7). Onarım bir commit'e (değişikliğin kayda geçtiği an) bağlandı.

07-30'dan kalan 26 raporun ingest'inin ilk iki dilimi kapandı — 8 rapor işlendi, toplam 12/26'ya ulaşıldı; iki alt-görevli damıtarak yaptı, ≈287 bin token harcayarak. Ayrı bir yüzey testinde, depodaki dört yardımcı dosyanın Cowork ana ortamında YÜKLENMEDİĞİ doğrulandı — önceden şüphelenilen bir erişim arızasının gerçek olduğu teyit edildi.

Salih'in emriyle iki yeni görev emri derlendi: biri "anlam çevirici" (semantik-compiler) kurulumu, öbürü bağlam-şişmesi denen sorunun matematiksel modelini kurma görevi. İkisi de önceden araştırılmadığı kontrol edildikten sonra derlendi; koşumları Salih'e bırakıldı. Fikir kutusuna anlam-çevirici fikri not düşüldü, beceri-kutusuna görev-emri-derleme adında yeni aday eklendi — bu deseni ilk kez Salih işaret etmişti.

Kararlar: Onarımın kapsamı bilinçli dar tutuldu — gerekçe, hatanın sayım/kaynak sınıfında yoğunlaştığının ölçülmüş olması; geniş tarama isteği gelirse ucuza yeniden açılabilir. İngest sırası (önce 1-2. dilim, 3. dilim ertelendi) Salih'in CC-öncelik kararına bağlandı. Daha önce "2,45 dolar" diye doğrulanmaya çalışılan maliyet çapası, yeni ölçümle ÇÜRÜDÜ — gerçek aralık 0,56-302 dolar, ortanca 14 dolar çıktı; bu bir teyit değil düzeltme oldu. Küçük bir kural ihlali de kendiliğinden bildirildi: bir dosya yanlışlıkla üzerine yazılmış (kısaltılmış listeye bakıp dosya yok sanılmış), hemen geri yüklendi, kayıp sıfır; ders: varlık kontrolü kısaltılmış listeyle değil doğrudan komutla yapılmalı.

Sonraki iş: Salih'e göre öncelik, ana çalışma ortamının CC'ye taşınması — gerekçe, mevcut ortamda bağlam şişmesinin oturumları kısalttığı gözlemi. Ayrıca iz-hasadı işinin 08-11'e kadar vadeli bir borç olduğu hatırlatıldı.

Dersler: kirli bir oturumdaki hataların kaynağı çıkarım değil MUHASEBE hatasıydı — en verimli denetim, her rakamı yeniden saymaktı. Ayrıca "bağlam şişti" hükmünün kendisinin de ölçülmemiş bir öz-beyan olduğu, bunun sonraki emirle modele bağlanacağı not edildi.

→ kaynak: `raporlar/vardiya-teslim-2026-08-01-anasira.md`

---

## Salih'in masasına düşenler

Okuduktan sonra hâlâ açık olan kararlar — her biri tek satır, yanında hangi bölümden geldiği:

1. **Kullanım-ufku ölçümü ikinci bir tura açılsın mı** — bugün sıfır veri toplandı, üç tasarım seçeneği hazır, maliyet sınıfı henüz doğrulanmadı. (§2, §1)
2. **Ölçekleme ham raporunun "karantina deseni" kalıcı usul olsun mu** — iki kez uygulandı, henüz imzalı kural değil. (§1, §3)
3. **Bağlam sayacı: Yol-1 (sessiz sayaç) kurulsun mu, ne zaman kalibre edilsin** — eşik sayısı bilerek önerilmedi; ham kayıtlar 11 Ağustos'tan itibaren silinmeye başlıyor. (§9, §5)
4. **Çeviri mekanizmasının kurulum sırası** — önce denetleyici betik, sonra yalın üçüncü kip, en son skill dosyası; skill dosyası Salih imzası isteyen bir kilide giriyor. (§8)
5. **"Çeviri çıktısı kanona işlenmesin" kuralı onaylansın mı** — gerekçe: çeviri ölçülmüş bir hata kanalı. (§8)
6. **"Her rapora otomatik iki kip" kuralı seçici tetiğe dönüşsün mü** — mevcut hali kaynağın 1,26 katı hacim üretiyor, hacim-küçültme hükmüyle çelişiyor. (§8, §5)
7. **EK-3'te biriken Katman-1 adayları** — yardımcı-dosya çağırma dilinin tek tip imzası, atlas-kosum'un taşınması, md.44'ün 19 gündür uygulanmaması. (§6)
8. **"Kısa-koşum istatistiksel süreç kontrolü" literatürü okunsun mu** — kalibrasyon tasarımının artık emsalsiz olmadığı ortaya çıktı. (§7)
9. **Deterministik maliyet/çağrı kapısı kurulsun mu** — bugün üç bağımsız kanıt birikti: bir koşumda tavan aşıldı ($30,94 / $16,34), model-katmanı şartı denetlenemedi, ve bu derlemenin kendisi $8 tavanını $12,69 ile aştı. Üçünde de kısıt yalnız emir metnindeydi. (§7, §1, koşum raporu)
10. **9-10 Ağustos'ta ikinci yedek alınsın mı** — ilk yedekte 26 dosyadan 1'i açık oturum nedeniyle tutmamıştı. (§4)

Kapanan iki kalem, bir daha sorulmasın diye: nötr sözlük kanona girdi ve iki ölçek-üssü ölçüm-bankına yazıldı (§1); iz saklama süresi 365 güne sabitlendi (§3).
