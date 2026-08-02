# K2 Masası — Hazırlık Dosyası (Salih için, İNSAN register)

*Bu dosya `cc/gorev-2026-08-02-2.md` emrinin ürünüdür — masaya oturmadan önce tek başına okunup anlaşılabilecek karar rehberi. Karar YOK, öneri işareti DEĞİŞTİRİLMEDİ; bu bir ÇEVİRİ, hakemlik değil.*

## Terimler (bir kere açıklanıyor, aşağıda tekrar edilmiyor)
- **SHA** — bir commit'in (kayıtlı değişikliğin) parmak izi; hangi sürümden bahsettiğimizi kesinleştiren kod.
- **Katman-1** — yalnız Salih'in karar verebileceği karar sınıfı (kanon, para, dışarı çıkacak iş, geri-alınması zor iş).
- **Hakem** — bir tartışmayı taraf bilmeden (maskeli) değerlendiren ayrı bir yapay-zeka koşumu; "SAĞLAM/DARALDI/ÇÜRÜDÜ" gibi hükümler verir.
- **Antitez** — bir raporun iddialarını kasten çürütmeye çalışan, ayrı ve bağımsız ikinci koşum.
- **m.40b** — tez → antitez → hakem üçlü doğrulama protokolümüz.
- **Bant-dışı / bant-içi** — "bant-dışı" = kuralın yaşadığı yer, koşucunun okuduğu dosyanın DIŞINDA (ör. koşum promptunun kendisi); "bant-içi" = kuralın yaşadığı yer, koşucunun bulması gereken dosyanın İÇİNDE. 08-02 arızasında dosya bulunamadığı için bant-içi hiçbir önlem işlemedi.
- **L1/L2/L3** — üç-katmanlı mimarideki üç "dil/register": L1 = Salih'in okuduğu doğal dil, L2 = ara-katman (makine ve insanın ortak okuduğu), L3 = tam makine-diline (şema/kod) form.
- **Register** — "dil" kelimesinin bu rapordaki gevşek kullanımının yerine önerilen, daha dar/doğru terim (bkz. K2-f).

## Okuma kılavuzu (hakemin sentez uyarısı, aynen taşınıyor)
> *"En olası hata paket-kabul / paket-red: kalemler birbirine bağlıymış gibi konuşuluyor, oysa BAĞIMSIZ karar veriyorlar."*

14 kalem + 1 yapısal ayrım kararı = 15 bölüm. Her biri **ayrı** imza/red/beklet kararı ister. Aşağıdaki "önerilen sıra" yalnız okuma-verimliliği içindir, paket değildir.

---

## HAT-A ⊥ HAT-B — kalem-üstü yapısal ayrım (hakem Ç7)

**1. Ne karar veriliyor:** İki ayrı iş akışının BİRBİRİNDEN BAĞIMSIZ ilerlemesi kanonlaşsın mı? **HAT-A** = ölçülmüş arızayı kapatan, sıfır ek geliştirme maliyetli koruma önlemleri (ör. K2-a). **HAT-B** = "compiler hangi sınıfta kurulmalı" gibi mimari tasarım kararları.

**2. Neden şimdi masada:** Rapor bulgusu S7: bugünkü arızanın (08-02) çözümü mimari seçimi beklemek zorunda değil — HAT-A bağımsız yürüyebilir. Ama HAT-B için depo kendi kuralını (bir deseni ancak ≥3 kez tekrarlandıktan sonra kalıcı yapıya dökme) henüz karşılamıyor: mimari-gerektiren kenarlarda (L3, bkz. S8) örnek sayısı 0.

**3. Seçenekler:**
- **A — İki hattı ayır (rapor yönü):** Kazanç — HAT-A bugün bedelsiz ilerler, HAT-B'nin belirsizliği HAT-A'yı geciktirmez. Kabul edilen bedel — iki ayrı karar takibi, "hangi kalem hangi hatta" sınıflandırma yükü.
- **B — Tek paket olarak birlikte karara bağla:** Kazanç — tek oturumda kapanır. Kabul edilen bedel — hakemin doğrudan uyardığı hata: "E0 muhafızı apaçık doğru olduğu için mimari de onun sırtında içeri alınır; ya da mimari doğrulanmamış diye muhafız da reddedilir" — ikisi de hatalı çıkarım.

**4. Raporun önerdiği yön + karşı-taraf:** Rapor: HAT-A ∧ HAT-B ayrı imza ister, HAT-B (compiler sınıfı seçimi) N=0 kenarlarda **BEKLESİN**, sıfır-token muhafızlar (HAT-A) **beklemesin** — bu ikisi ayrı kararlardır, paket alınmaz. Karşı-taraf: rapor içinde ayrı bir karşı-taraf sütunu yok — bu, hakemin doğrudan verdiği hüküm (Ç7: antitez daraldı, iki-iş-ayrı sonucu ayakta kaldı).

**5. Karar verilmezse ne olur:** Bedelsiz beklet DEĞİL — bu ayrımı imzalamadan aşağıdaki 14 kalem tek tek okunursa risk, okuyanın kendiliğinden paket-kabul/paket-red mantığına kayması (hakemin en olası hata öngörüsü tam bu).

**6. Beklenen karar biçimi:** {imza / red} — çerçeve kararı, bağımlı: K2-a/K2-k/K2-n (HAT-A adayları) ↔ K2-f/K2-g (HAT-B'ye yakın, mimari-terminoloji).

*(Bağlı bölüm: masa-gündemi "Yapısal karar" satırı · rapor §7.1 Ç7)*

---

## K2-a ⭐ — Bant-dışı erişim-doğrulama kuralı

**1. Ne karar veriliyor:** Koşum promptunun kendisi emrin kesin adresini (dosya yolu) + SHA'sını taşısın; koşucunun ilk işi bunu doğrulamak olsun — dosya yoksa ya da SHA tutmuyorsa koşucu **DUR** desin, kendi kafasına göre iş üretmesin (doğaçlama yasak). Bu kural kanonlaşsın mı?

**2. Neden şimdi masada:** 08-02 sabahı görev emri yanlış dala push'landı; koşucu emri bulamayınca doğaçlama bir araştırma raporu üretti. Salih her iki çıktıyı da (yanlış-dal emri + doğaçlama rapor) geçersiz saydı — bir günlük iş kayboldu. Bu emrin kendisi (`cc/gorev-2026-08-02-2.md`) kuralı deneme olarak zaten taşıyor; bu raporun künye satırı (aşağıda) ilk saha-verisidir.

**3. Seçenekler:** Tek meşru seçenek — rapor ile hakem aynı yönde, gerçek bir ikinci "eşit değerde" seçenek yok. **YAZ (kanonlaştır):** kazanç — 08-02'de fiilen işleyen tek koruma; kabul edilen bedel — kısıt sayısı bir artar, geçmiş emsal (30-19:335 kaydı) kısıt biriktikçe takibin bozulduğunu gösteriyor. **YAZMA:** kazanç — kısıt sayısı sabit kalır; kabul edilen bedel — kural "deneme" statüsünde kalır, bir sonraki emirde tekrar unutulma riski taşır.

**4. Raporun önerdiği yön + karşı-taraf:** Rapor: **YAZ** — "08-02'de fiilen çalışan tek koruma buydu; şablon-içi alan bant-içidir, kapsamı arızayı örtmez" (hakem Ç6). Karşı-taraf: "kısıt sayısı arttıkça takip bozuluyor" (30-19:335 emsali, çürütülmedi).

**5. Karar verilmezse ne olur:** Bedelsiz beklet değil — kural zaten fiilen kullanımda ama resmi statüsü yok; resmileşmeden bir sonraki emir yazımında atlanma riski sürer.

**6. Beklenen karar biçimi:** {imza / red} — bağımlı: K2-b (b, a olmadan tek başına yetmez).

*(Bağlı bölüm: rapor §4.3 · §7.1 Ç6)*

---

## K2-b — Şablona "emir konumu + erişim doğrulaması" alanı

**1. Ne karar veriliyor:** `core/sablonlar/gorev-emri.md` (emir yazarken kullanılan kalıp dosya) içine, K2-a'daki doğrulama adımı için sabit bir alan eklensin mi?

**2. Neden şimdi masada:** K2-a'nın doğal tamamlayıcısı — kural kanonlaşırsa emir yazarken unutulmaması için şablonda yer tutması gerekir.

**3. Seçenekler:** **EKLE:** kazanç — emir yazarken alan hatırlatıcı olarak durur; kabul edilen bedel — hakemin uyarısı: **bu alan tek başına YETMEZ**, çünkü şablonun kendisi de bant-içi sayılır (koşucu dosyayı hiç bulamazsa şablondaki alanın kapsamı da sıfırdır — aynı tuzak). **EKLEME:** kazanç — şablon sadeliği korunur; kabul edilen bedel — K2-a kanonlaşsa bile emir yazarken unutulma riski taşınmaya devam eder.

**4. Raporun önerdiği yön + karşı-taraf:** Rapor: **EKLE — ama tek başına yetmez**. Karşı-taraf (hakem Ç6 hükmü): "adresi bulunamayan dosyanın İÇİNDEKİ alanın kapsamı, dosyayı hiç görmeyen koşucu için tam olarak SIFIRDIR."

**5. Karar verilmezse ne olur:** K2-a tek başına ayakta kalır (koşum promptu doğrulaması) ama şablon hatırlatıcısı olmadan emir-yazım aşamasında unutulma riski taşınır — düşük ama sıfır olmayan bedel.

**6. Beklenen karar biçimi:** {imza / red / beklet} — K2-a'ya bağımlı (a reddedilirse b anlamsızlaşır).

*(Bağlı bölüm: rapor §1.2 E0 · §7.1 Ç6)*

---

## K2-c — Şablona "done-yüklemi" (makine formunda tamam-koşulu) alanı

**1. Ne karar veriliyor:** Görev emri şablonuna, "iş ne zaman bitmiş sayılır" sorusunun ikili/sayılabilir (evet-hayır ya da sayı ile ölçülebilir) biçimde yazılacağı sabit bir alan eklensin mi?

**2. Neden şimdi masada:** Antitez koşumu (tezi çürütmeye çalışan bağımsız koşum) bu alanı K2-b/d/e'den **bağımsız olarak** ayrıca gerekçelendirdi — kendi başına duran bir dayanağı var (08-01-1 raporunun 434. satırı).

**3. Seçenekler:** **EKLE:** kazanç — antitezin bağımsız doğruladığı tek alan, "iş bitti mi" belirsizliğini azaltır; kabul edilen bedel — dört aday alandan (K2-c/d/e + tetik) sadece biri ayrı ayrı eklenirse şablon parça parça büyür, tek seferde tutarlı revize edilmez. **EKLEME:** kazanç — şablon değişikliği ertelenir, tek toplu revizyon beklenir; kabul edilen bedel — bu koşumun somut bulduğu belirsizlik-kaynağı kapanmaz.

**4. Raporun önerdiği yön + karşı-taraf:** Rapor: **EKLE** — antitez bu alanı bağımsız gerekçelendirdi. Karşı-taraf: dört alanı **birden** eklemeye antitez itiraz ediyor; **tek tek ve ölçerek** eklenmeli — yani K2-c'nin EKLE yönü, K2-d/e'nin de otomatik EKLE anlamına gelmediğinin açık uyarısı.

**5. Karar verilmezse ne olur:** Bedelsiz beklet değil — "iş bitti mi" belirsizliği devam eder, ama acil değil (K2-a/K2-k gibi bir arızaya doğrudan bağlı değil).

**6. Beklenen karar biçimi:** {imza / red / beklet} — K2-d ve K2-e'den bağımsız, ayrı ayrı değerlendirilmeli.

*(Bağlı bölüm: rapor §3.3 · §6.3)*

---

## K2-d — Şablona "tetik" (D8) alanı

**1. Ne karar veriliyor:** Şablona, "bu iş neyle/ne zaman başlatılır" (tetik) sorusunun boş bırakılamayacağı bir alan eklensin mi?

**2. Neden şimdi masada:** Ayrı bir araştırma hattı (g23) hakeminde zaten aynı isteği bağımsız olarak koydu (Ç1: "SAĞLAM" — güçlü kanıt sınıfı); iki hat aynı ihtiyacı ayrı ayrı buldu.

**3. Seçenekler:** **EKLE:** kazanç — g23 hattının zaten SAĞLAM bulduğu bir eksiği kapatır; kabul edilen bedel — bu rapor ile g23 raporu aynı alanı iki kere önerebilir, **birleştirilmeden** eklenirse mükerrer/çelişkili alan tanımı riski var. **EKLEME / g23 ile birleştir sonra karar ver:** kazanç — mükerrer tanım riski sıfırlanır; kabul edilen bedel — karar bu masada kapanmaz, g23 kalemleriyle ayrı bir tur gerekir.

**4. Raporun önerdiği yön + karşı-taraf:** Rapor: **EKLE** — g23 hakem Ç1 zaten bunu istiyor; ama **mükerrer olabilir**, bu yüzden g23 kalemleriyle **birleştirilerek** masaya alınması öneriliyor. Ayrı bir karşı-taraf sütunu bu kalem için yok — riskin kendisi mükerrerlik.

**5. Karar verilmezse ne olur:** Bedelsiz beklet — g23 kalemleriyle birleşik tur zaten önerilen yol; bu masada tek başına kapatmak mükerrerlik riskini taşır.

**6. Beklenen karar biçimi:** {beklet — g23 turuna ertelensin / yine de bu masada karara bağlansın} — bağımlı: g23'ün D8 kalemi (bu rapor kapsamı dışında, ayrı dosya).

*(Bağlı bölüm: rapor §3.3 · g23 D8)*

---

## K2-e — Şablona kısıt-profili / devir-arayüzü / sınır-denetçisi alanları

**1. Ne karar veriliyor:** Şablona üç teknik alan birden eklensin mi: "kısıt-profili" (işin hangi kural setine tabi olduğu), "devir-arayüzü" (bir işin bir sonrakine nasıl devredildiği) ve "sınır-denetçisi" (işin sınırını kimin/neyin denetlediği)?

**2. Neden şimdi masada:** Bu üç alan, henüz koşulmamış bir mimari tasarımın (g20/g23 hattı) parçası; şablona şimdiden girip girmeyeceği K2 masasının gündemine antitez tarafından taşındı.

**3. Seçenekler:** **BEKLET (rapor yönü):** kazanç — kısıt yükü ölçülmeden şablon şişirilmez; kabul edilen bedel — tersi risk de gerçek: alan olmadan g20/g23 tasarımı sadece kağıt üzerinde kalabilir (bu, kendi kuralımızın tanımladığı bir arıza sınıfıdır — kural var ama hiç tetiklenmiyor). **EKLE:** kazanç — g20/g23 tasarımı bugünden şablonda karşılık bulur; kabul edilen bedel — ölçülmemiş kısıt yükü şablonu ağırlaştırabilir, üç alan aynı anda büyük bir değişikliktir (K2-c'nin "tek tek ekle" uyarısına aykırı düşer).

**4. Raporun önerdiği yön + karşı-taraf:** Rapor: **BEKLET** — "kısıt yükü ölçülmeden eklenmez." Karşı-taraf: "alan olmadan g20/g23 tasarımı kâğıtta kalır" — kendi arıza-sınıfımıza (kural var, tetik yok) düşme riski.

**5. Karar verilmezse ne olur:** Rapor zaten BEKLET öneriyor — kararsızlık burada fiilen önerilen yönle örtüşüyor; bedel yalnız g20/g23 tasarımının kağıtta kalma riskinin sürmesi.

**6. Beklenen karar biçimi:** {beklet (rapor yönü) / imza (üç alanı şimdi ekle) / red} — en düşük öncelikli kalem, diğerlerinden bağımsız.

*(Bağlı bölüm: rapor §3.3 · §6.2 H3)*

---

## K2-f — "Üç dil" → "üç register" adlandırma düzeltmesi

**1. Ne karar veriliyor:** Mimarinin "üç dil" (L1/L2/L3) diye anılan yapısı, "üç register + kenar-başına biçim" olarak yeniden adlandırılsın mı? Bu bir mimari değişikliği DEĞİL, yalnız isim değişikliğidir.

**2. Neden şimdi masada:** Antitez koşumunun bulgusu (H2): her kenarda biçim farklı önerildiği anda "ortak dil" fikrinin ekonomik gerekçesi (paylaşılan bir ara-form) zaten düşüyor — yani "dil" kelimesi mimariyi olduğundan daha birleşik gösteriyor. Ayrıca "üç dil" ifadesi **Salih'in kendi kelimesi** — kanonun kendi kuralı gereği (m.20-benzeri açık kayıt ilkesi) bu tür bir değişiklik yalnız Salih'in onayıyla yapılabilir.

**3. Seçenekler:** **DÜZELT:** kazanç — terminoloji, mimarinin bugünkü fiili durumunu ("iki register + bir boşluk", S8) daha doğru yansıtır; kabul edilen bedel — Salih'in kendi kelimesi değiştiriliyor, geçmiş raporlarda "üç dil" geçen yerlerin okunması bu değişimle hafif kayar. **DEĞİŞTİRME:** kazanç — Salih'in orijinal ifadesi korunur, geçmiş metinlerle tutarlılık sürer; kabul edilen bedel — terim, mimarinin şu anki halinden (L3 yok, L2 yarım) daha iddialı bir görüntü vermeye devam eder.

**4. Raporun önerdiği yön + karşı-taraf:** Rapor: **DÜZELT** — "antitezin H2 hamlesi terminolojiyi çürüttü, mimariyi değil." Karşı-taraf: "'Üç dil' Salih'in kendi kelimesi; değişiklik yalnız Salih" (bu zaten kararın Salih'e ait olduğunu doğruluyor, çürütme değil — kapsam hatırlatması).

**5. Karar verilmezse ne olur:** Bedelsiz beklet — isim değişmeden de mimari aynı şekilde çalışır; yalnız terminolojik netlik ertelenir.

**6. Beklenen karar biçimi:** {imza (düzelt) / red (üç dil kalsın)} — bağımsız, diğer kalemlere bağımlılığı yok.

*(Bağlı bölüm: rapor §6.2 H2 · S5 · S8)*

---

## K2-g — Compiler-formülü §4 hibrit maddesinin yeniden damgalanması

**1. Ne karar veriliyor:** `2026-07-26-compiler-formulu.md` belgesindeki "hibrit" önerisi (üretici yapay-zeka + deterministik/kural-tabanlı doğrulayıcı ikilisi), "kazanmış kesin cevap" değil, "tasarım kıyasında kazanmış AMA bu depoda henüz KOŞULMAMIŞ bir hipotez" olarak yeniden etiketlensin mi?

**2. Neden şimdi masada:** Bu koşumun kendi bulgusu (S4): hibrit yaklaşımın dış literatürdeki güçlü sonucu (VeriTrans, %94,46), hedefi FORMAL (SAT/CNF gibi kesin biçimli) olan bir kenarda ölçülmüş; bizim deponuzda böyle bir kenar (E3) şu an BOŞ. Yani hibridin bizim depoda genellenmesi kanıtlanmış değil, tasarım tercihi.

**3. Seçenekler:** Tek meşru seçenek — belgenin kendisi zaten kendi §6.4'ünde bu daha temkinli statüyü kabul ediyor; asıl mesele önceki emrin bu inceliği "kazanmış" diye atlamış olması. **DÜZELT:** kazanç — belge kendi iç-tutarlılığına döner, emrin öncül ilanı (K2-g'nin doğduğu emrin kendisinin "kazanmış" varsayması) düzelir; kabul edilen bedel — "çözülmüş" sayılan bir kenar yeniden maliyetli/tartışmalı hale gelir, ileride tekrar gündeme gelebilir.

**4. Raporun önerdiği yön + karşı-taraf:** Rapor: **DÜZELT** — "belge kendi §6.4'ünde zaten böyle diyor; emrin öncül ilanı bunu örtüyordu." Karşı-taraf: "yeniden açmak, çözülmüş sayılan bir kenarı yeniden maliyetli hale getirir."

**5. Karar verilmezse ne olur:** Bedelsiz beklet değil — belge içinde bir iç-çelişki (bir yerde "kazanmış", başka yerde "koşulmamış hipotez") sessizce durmaya devam eder; ileride biri "kazanmış" satırına güvenip karar alırsa hata miras alınır.

**6. Beklenen karar biçimi:** {imza (düzelt) / red} — bağımsız, K2-f ile aynı "terminoloji temizliği" ailesinden ama ayrı karar.

*(Bağlı bölüm: rapor §6.2 H1 · §2.5)*

---

## K2-h — "Ç-YENİ" çelişkisinin hakemliği (= B1 borcu)

**1. Ne karar veriliyor:** İki eski rapor arasındaki çelişkiye (30-13'ün 60. satırı ↔ 30-16'nın 251. satırı; ikisi de "skill'ler ne zaman tetiklenir" konusunda birbirini tutmuyor) bir hakemlik koşumu yapılsın mı? Bu bir karar değil, ucuz bir çalıştırma onayı (~15 dakikalık yerel iş).

**2. Neden şimdi masada:** S7'nin kanıt tabanı (bugün compiler'ı skill olarak kurmanın, ölçülmüş "durum-tetiği" arızasını miras alacağı hükmü) bu çelişkinin çözümüne bağlı; ayrıca hakemin kendi denetimi (§7.3) bu çelişkinin **hâlâ ayakta** olduğunu doğruladı.

**3. Seçenekler:** Tek meşru seçenek — iş ucuz (~15 dk, karşı-taraf yok), yapmamak için maliyet-gerekçesi zayıf. **ONAY:** kazanç — S7'nin kanıt tabanı netleşir; kabul edilen bedel — 15 dakikalık yerel emek. **ONAYLAMA/ERTELE:** kazanç — hiç; kabul edilen bedel — S7 hükmü kanıtsız kalmaya devam eder.

**4. Raporun önerdiği yön + karşı-taraf:** Rapor: **HAKEMLİK KOŞ** — "ucuz, karşı-taraf yok." Karşı-taraf sütunu boş bırakılmış (rapor bunu açıkça "karşı-taraf yok" diye işaretliyor — bir uydurma-üçlü değil, gerçek tekli durum).

**5. Karar verilmezse ne olur:** Bedelsiz beklet değil — çelişki açık kalır, S7'nin dayanağı zayıf kalmaya devam eder; ama acil değil, herhangi bir boş vardiyada 15 dakikada kapanabilir.

**6. Beklenen karar biçimi:** {onay / beklet} — bu kalem aynı zamanda `build-tartisma-notlari.md`'deki B1 borcuyla özdeş; oradaki öneri zaten "Carvis, ilk boş vardiya" olarak not düşülmüş — masanın burada yapacağı, o rotayı onaylamak.

*(Bağlı bölüm: rapor §6.6)*

---

## K2-i — Dil-sınırı ↔ loop-sınırı çakışma hipotezinin sınanması (= B4 borcu)

**1. Ne karar veriliyor:** Üç-register mimarisinin sınırlarıyla, ayrı bir hattın (g23) "loop" tanımının sınırlarının çakışıp çakışmadığı hipotezi, 3 örnek vaka üzerinden ucuz bir şekilde sınansın mı?

**2. Neden şimdi masada:** Sınama hem üç-register modelini hem g23'ün loop-yükünü aynı anda test eden, tek koşumla iki soruya birden ışık tutan bir fırsat olarak değerlendiriliyor.

**3. Seçenekler:** **SINA (rapor yönü):** kazanç — iki ayrı hat için aynı anda veri üretir; kabul edilen bedel — n=3 örneklem **doğrulamak için yetersiz**, yalnız **çürütme gücü** taşır (bir vaka hipotezle çelişirse hipotez zayıflar, ama üçü de uyuşsa hipotez "kanıtlanmış" sayılamaz — bu açıkça beyan edilmesi gereken bir sınır). **SINAMA:** kazanç — hiç; kabul edilen bedel — hipotez test edilmeden kutuda beklemeye devam eder.

**4. Raporun önerdiği yön + karşı-taraf:** Rapor: **SINA** — "hem üç-dil modelini hem g23 loop-yüklemini aynı anda test eder." Karşı-taraf (raporun kendi uyarısı, dış itiraz değil): "n=3 doğrulamak için yetersiz — yalnız çürütme gücü var, bu açıkça beyan edilmeli."

**5. Karar verilmezse ne olur:** Bedelsiz beklet — hipotez `build-tartisma-notlari.md`'de kutuda ("çürütme gücü var/doğrulama yok" notuyla) beklemeye devam eder, masa sonrasına da ertelenebilir.

**6. Beklenen karar biçimi:** {onay / beklet — masa sonrası} — `build-tartisma-notlari.md`'deki B4 önerisi zaten "masa sonrası" diyor; masanın işi bu rotayı onaylamak ya da öne çekmek.

*(Bağlı bölüm: rapor §4.2)*

---

## K2-j — `[rejim: manuel-tempo]` etiketinin kanonlaşması

**1. Ne karar veriliyor:** Bu raporun önerdiği aşama-1 değişikliklerinin tümü "[rejim: manuel-tempo]" etiketini taşıyor (yani "otomasyon yokken, elle çalışırken geçerli" kaydı) — bu etiket kanonun resmi bir parçası olsun mu?

**2. Neden şimdi masada:** Kanonda zaten "bugünün kısıtları bir REJİM (abundance-regime) ölçümüdür, otomasyon geçişinde yeniden açılmalı" ilkesiyle uyumlu bir kayıt ihtiyacı var; bu etiket o ilkenin somut karşılığı olarak öneriliyor.

**3. Seçenekler:** **MASAYA AL / KANONLAŞTIR:** kazanç — rejim-bağımlı kalibrasyon ilkesiyle uyumlu, hangi kararların otomasyon geçişinde otomatik yeniden açılacağı işaretlenmiş olur; kabul edilen bedel — yeni bir etiket, yeni bir bakım kalemi demektir (kim, ne zaman, hangi kayıtları bu etiketle taramalı — bu iş kendiliğinden olmaz). **KANONLAŞTIRMA:** kazanç — bakım yükü artmaz; kabul edilen bedel — rejim-bağımlı kararlar etiketsiz kalır, otomasyon geçişinde hangilerinin yeniden açılması gerektiği elle hatırlanmak zorunda kalır.

**4. Raporun önerdiği yön + karşı-taraf:** Rapor: **MASAYA** — "rejim-bağımlı kalibrasyon ilkesiyle uyumlu." Karşı-taraf: "yeni etiket = yeni bakım kalemi."

**5. Karar verilmezse ne olur:** Bedelsiz beklet — etiket zaten gayri-resmi olarak bu raporda kullanılıyor; kanonlaşmadan da çalışır, yalnız resmi statüsü yok.

**6. Beklenen karar biçimi:** {imza / red / beklet} — en düşük aciliyetli kalemlerden biri, bağımsız.

*(Bağlı bölüm: rapor §3.1)*

---

## K2-k ⭐ — Maskeli-hakem yapısal açığı

**1. Ne karar veriliyor:** Hakemlik koşumlarında "taraflar maskelenir, hakem hangisinin asıl tez olduğunu bilmez" kuralı (m.40b Aşama 3), üretici çıktısı çalışma ağacına (git deposuna) yazıldığı anda **yapısal olarak sağlanamıyor** — çünkü hakem depoyu okuma yetkisine sahip ve dosya adından/satır numarasından hangi tarafın kim olduğunu çıkarabiliyor. Bu açığa karşı hangi çare kanonlaşsın: (i) hakem depo-okuma yetkisiz mi koşsun, (ii) üretici çıktısı hakem bitene dek depo-dışı bir geçici alanda mı tutulsun, (iii) maskeleme hedefi daraltılıp ("kim tez" yerine "hangi tarafın gerekçesi") sızıntı açıkça mı beyan edilsin?

**2. Neden şimdi masada:** Bu koşumun kendisinde fiilen kırıldı: hakem, bu raporun kendi dosyasından satır numaralı alıntılar yaptı (6 farklı satır, hepsi doğrulandı). Sonuç bu sefer tez lehine bozulmadı — hakem tezin kendi cümlelerini teze karşı kullandı — ama "bir sonraki koşumda bozabilir" uyarısı raporun kendisinde var.

**3. Seçenekler:** **(i) Hakem depo-yetkisiz koşsun:** kazanç — maskeleme tam sağlanır; kabul edilen bedel — hakem bu koşumda tam da o yetkiyle tezin kendi cümlelerini teze karşı kullandı, yetkisiz koşarsa bu kanıt-doğrulama gücü kaybolur. **(ii) Üretici çıktısı hakem bitene dek scratchpad'de (depo-dışı geçici alan) tutulsun:** kazanç — maskeleme korunur, hakem yine de kanıt metnini görür (yalnız depoya henüz yazılmamış hali); kabul edilen bedel — iş akışına bir ekstra aşama girer (depoya yazma hakemden sonraya ertelenir). **(iii) Maskeleme hedefi daraltılsın, sızıntı beyan edilsin (bu koşumun fiilen yaptığı):** kazanç — ek mekanizma gerekmez, bugün uygulanabilir; kabul edilen bedel — "kimlik" maskesi resmi olarak gevşetilmiş olur, hakemin tarafsızlığı yalnız beyan disiplinine dayanır.

**4. Raporun önerdiği yön + karşı-taraf:** Rapor: **MASAYA** (üç çareden hangisi kanon olacak, Salih kararı) — bu koşum (iii)'ü fiilen uyguladı ve beyan etti. Karşı-taraf: "(i) kanıt-doğrulamasını öldürür — hakem bu koşumda tam o yetkiyle tezin kendi cümlelerini teze karşı kullandı; kapatmak kaliteyi düşürebilir."

**5. Karar verilmezse ne olur:** Bedelsiz beklet değil — her yeni hakemlik koşumu (K2-h dahil) aynı yapısal açığı taşımaya devam eder; bu sefer sonucu bozmadı ama garanti yok.

**6. Beklenen karar biçimi:** {(i) imza / (ii) imza / (iii) imza (mevcut fiili durumu kanonlaştır) / red-hepsi} — bağımlı: K2-h (yeni hakemlik koşumu bu kararın gölgesinde çalışacak) ve K2-l/K2-m (hakemlik/ölçüm disiplini ailesinin parçası).

*(Bağlı bölüm: rapor §7.4)*

---

## K2-l — m.40b "hayatta-kalma serisi" hükmü

**1. Ne karar veriliyor:** m.40b protokolü (tez→antitez→hakem) art arda 4. kez çalıştı ve 4. kez de hiçbir tez tam-sağlam çıkmadı (g20: 0/8 iddia sağlam, g23: 0/6, bu koşum: 0/14). Bu seri, "protokol bu haliyle mi kalsın" sorusunu masaya taşıyor mu, taşımalı mı?

**2. Neden şimdi masada:** Dört ardışık koşumda sıfır tam-sağlam iddia, tek koşumluk bir tesadüf olmaktan çıkıp bir örüntü sayılabilecek eşiğe geldi — raporun kendi ifadesiyle "dördüncü üst üste."

**3. Seçenekler:** **MASAYA (rapor yönü — protokolü sorgula):** kazanç — eğer protokolün kendisinde bir sistematik sorun varsa (ör. tezler hep fazla iddialı kuruluyor, ya da hakem hep aşırı sıkı) bu 4 koşumluk veriyle yakalanabilir; kabul edilen bedel — seri, "hafif" (kısa/az kaynaklı) ve "tam" (geniş) formları karıştırıyor, birebir kıyaslanabilir değil — yani sinyal gürültülü. **DOKUNMA (protokol aynen kalsın):** kazanç — değişiklik maliyeti yok; kabul edilen bedel — eğer gerçekten sistematik bir sorun varsa (ör. hakem sistematik olarak çok sıkı), her koşum boşuna "0 sağlam" üretmeye devam eder.

**4. Raporun önerdiği yön + karşı-taraf:** Rapor: **MASAYA** — "'m.40b bu haliyle mi kalsın' sorusu artık 4 koşumluk seriye dayanıyor." Karşı-taraf: "seri HAFİF ∧ TAM formları karıştırıyor ⇒ birebir kıyaslanabilir değil; yön aynı" (yani karşı-taraf veri kalitesini sorguluyor, yönü değil).

**5. Karar verilmezse ne olur:** Bedelsiz beklet değil — g20'nin K1-h kalemiyle birleştirilmesi öneriliyor; birleştirilmezse aynı örüntü iki ayrı yerde parça parça tartışılmaya devam eder.

**6. Beklenen karar biçimi:** {masaya al / beklet} — bağımlı: K2-m (aynı "ölçüm disiplini" ailesinden, ayrı karar) ve g20 K1-h (bu rapor kapsamı dışında, birleştirme önerisi var).

*(Bağlı bölüm: rapor §6.1)*

---

## K2-m — "Ölçüm kültürü arızası" sistemik teşhisi

**1. Ne karar veriliyor:** Hakem, bu koşumdaki 7 anlaşmazlığın 5'inde aynı kalıbı gördü: küçük bir sayı (ör. "0/53" ya da "2/2") kademeli, genel bir hükme ("sınıf bozuk", "genellenebilir") sıçratılıyor — taraf farketmeksizin. Hakemin kök-teşhisi: depoda **sürekli bir sayaç yok**, bu yüzden tek anlık sayımlar hüküm gibi dolaşıyor. Bu teşhis, tek bu rapora özgü bir bulgu değil, sistemik bir kalem olarak mı ele alınsın?

**2. Neden şimdi masada:** Bu, raporun kendi bulgusu değil — hakemin bağımsız, "toplu gözlem" bölümünde ayrıca vurguladığı, 5 farklı anlaşmazlıkta tekrarlanan bir örüntü.

**3. Seçenekler:** **MASAYA (rapor yönü):** kazanç — tek bir rapor bulgusu değil sistemik bir disiplin sorunu olarak ele alınırsa, kalıcı bir sayaç mekanizması kurulabilir; kabul edilen bedel — sürekli sayaç kurulumu maliyetlidir VE kendisi de bizim tanımladığımız bir arıza sınıfına (m.43: araç var, tetik yok) açıktır — yani çözüm kendi başına yeni bir risk taşır. **MASAYA ALMA:** kazanç — ek maliyet yok; kabul edilen bedel — aynı kalıp (küçük örneklemden büyük hükme sıçrama) sonraki koşumlarda da tekrarlanmaya devam eder.

**4. Raporun önerdiği yön + karşı-taraf:** Rapor: **MASAYA** — "bu, tekil bir rapor bulgusu değil sistemik bir ölçüm-disiplini kalemi." Karşı-taraf: "sürekli sayaç kurulumu maliyetlidir ve kendisi de m.43 arıza sınıfına açıktır (araç var, tetik yok)."

**5. Karar verilmezse ne olur:** Bedelsiz beklet değil — hakemin gözlemi doğruysa (5/7 anlaşmazlıkta aynı kalıp), bu örüntü yeni koşumlarda da sessizce tekrarlanmaya devam eder; maliyeti düşük ama birikimli.

**6. Beklenen karar biçimi:** {masaya al / beklet} — bağımlı: K2-l (aynı aile, ayrı karar) ve K2-k (hakemlik/denetim kalitesi ailesi).

*(Bağlı bölüm: rapor §7.6)*

---

## K2-n ⭐ — Damga kuralının sıkılaştırılması

**1. Ne karar veriliyor:** Dış kaynak künyelerinde kullanılan iki damgadan (`[K]` = arama-sonucu özetinden alınmış · `[D-belge]` = birincil metne inilmiş) `[K]` damgasının kullanım şartı sıkılaştırılsın mı: bir künye yalnız arama-özetinden geldiyse `[K]` **zorunlu** olsun, `[D-belge]` yalnız gerçekten birincil metne (WebFetch ile) inilmişse kullanılsın.

**2. Neden şimdi masada:** Gerekçe artık ölçülü hale geldi: arama-özet katmanını üreten model (Haiku) için, zor görevlerde ölçülmüş bir performans kaybı var (−36,2 puan — S6'da geçen aynı ölçüm). Yani "özetten mi geldi, birincil metinden mi" ayrımı artık soyut bir titizlik meselesi değil, ölçülmüş bir güvenilirlik farkının kaydı.

**3. Seçenekler:** **MASAYA (rapor yönü — sıkılaştır):** kazanç — künyelerin güvenilirlik seviyesi artık daha doğru yansıtılır; kabul edilen bedel — kural sıkılaşınca `[D-belge]` sayısı düşer VE **geçmiş raporların damgaları geriye dönük denetime açılır** — bu pahalı bir iştir (kaç rapor, kaç künye, kim tarayacak — bu hesap bu raporda YOK, `[?]`). **MASAYA ALMA:** kazanç — geriye dönük denetim maliyeti hiç doğmaz; kabul edilen bedel — özet-katmanından gelen bilgiler birincil-metin bilgisiyle aynı görsel ağırlıkta kalmaya devam eder.

**4. Raporun önerdiği yön + karşı-taraf:** Rapor: **MASAYA** — "mevcut damga tanımının daraltılması", gerekçe ölçülü (Haiku'nun zor görevdeki −36,2 puanlık kaybı). Karşı-taraf: "kural sıkılaşır ⇒ [D-belge] sayısı düşer ⇒ geçmiş damgalar geriye dönük denetime açılır (pahalı)."

**5. Karar verilmezse ne olur:** Bedelsiz beklet değil — mevcut haliyle bazı `[K]` nitelikli bilgiler `[D-belge]` gibi okunmaya devam ediyor olabilir (bu koşumun kendi B9 borcu: öz-sayım ile panel-arama sayımı arasında fark var, kök bulunamadı) — düşük ama sıfır olmayan bir güven-kayması riski.

**6. Beklenen karar biçimi:** {imza (sıkılaştır) / red / imza + geriye-dönük-denetim-ayrı-borç-olarak-kaydet} — bağımsız, ama geriye dönük denetimin kim/ne zaman yapacağı ayrı bir borç olarak düşünülmeli.

*(Bağlı bölüm: rapor §9.3 Ç1 · §1.3)*

---

## Önerilen karar sırası (bağımlılık haritasıyla)

1. **HAT-A ⊥ HAT-B ayrımı** — önce bu; geri kalan 14 kalemin hangisinin "bugün bedelsiz ilerler" (HAT-A: K2-a, K2-k, K2-n) hangisinin "mimari netleşmeden bekler" (HAT-B: K2-f, K2-g ve dolaylı olarak K2-e) sınıfında olduğunu çerçeveler.
2. **K2-a** — en ucuz, en somut kanıtlı, hiçbir bağımlılığı yok; bugünkü emrin kendisi zaten bu kuralı taşıyor.
3. **K2-b** — a'nın doğal devamı, a'ya bağımlı.
4. **K2-c** — bağımsız, ucuz, antitez tarafından ayrıca gerekçelendirilmiş.
5. **K2-d** — g23 turuyla birleştirme kararı burada verilebilir (bu masada mı kapansın, g23 turuna mı ertelensin).
6. **K2-e** — rapor zaten BEKLET diyor; en son ya da hiç konuşulmadan mevcut öneri onaylanabilir.
7. **K2-f** — Salih'in kendi kelimesi, hızlı karar; K2-g ile aynı "terminoloji temizliği" ailesi ama bağımsız.
8. **K2-g** — bağımsız, ucuz, belge kendi içinde zaten bu yönde.
9. **K2-k ⭐** — sonraki hakemlik koşumlarının (K2-h dahil) çalışma biçimini belirlediği için K2-h'den ÖNCE karara bağlanması mantıklı.
10. **K2-h** — K2-k netleştikten sonra çalıştırılabilir (~15 dk, ucuz onay).
11. **K2-i** — bağımsız, ucuz onay.
12. **K2-l** — K2-m ile aynı aile; ikisi ayrı kararlar ama art arda okunması bağlamı taze tutar.
13. **K2-m** — K2-l'den hemen sonra, aynı gerekçeyle.
14. **K2-n ⭐** — bağımsız ama en pahalı yan-etkisi (geriye dönük denetim) olan kalem; dikkatli okunmalı, son sıraya konması "yorgunlukta hızlı geçilme" riskini artırabilir — bu yüzden K2-k'den hemen sonra da düşünülebilir. Öneri: 9. sıraya (K2-k'nin hemen ardından) alınması, masa sonuna bırakılmaması.
15. **K2-j** — en düşük aciliyet, herhangi bir noktada ya da son sırada kapatılabilir.

*(Not: yukarıdaki numaralandırma okuma-akışı içindir; K2-n'nin fiili önceliği yüksek olduğundan masada K2-k'nin hemen ardından ele alınması önerilir.)*

---

## Yönetici özeti (10 satır)

1. Bu dosya 14 K2 kalemi + 1 yapısal ayrım kararını (HAT-A/HAT-B) Salih'in tek başına karar verebileceği biçime çevirir; hiçbir öneri işareti değiştirilmedi.
2. Kaynak rapor (`cc/rapor-2026-08-02-1.md`) kendi hakemliğinde 7 anlaşmazlığın hiçbirinde bir tarafa "SAĞLAM" almadı, 14 iddiasından 8'i çürüdü — bu yüzden her hüküm KOŞULLU okunmalı.
3. En değerli tek bulgu (S1): 08-02 arızası hiçbir çeviri adımında değil, adı yeni konan bir "taşıma" adımında (E0) oldu — K2-a bu bulgunun doğrudan çaresi.
4. En kritik 3 yıldızlı kalem: K2-a (bant-dışı doğrulama, çalışan tek koruma), K2-k (hakem tarafsızlığında yapısal açık), K2-n (künye güvenilirlik damgası, geriye dönük denetim maliyeti var).
5. Hakemin en güçlü uyarısı: kalemler bağımsızdır, paket-kabul/paket-red ikisi de hatadır — bu dosya kalemleri o yüzden tek tek ayırdı.
6. HAT-A (K2-a/k/n ailesi) bugün mimari beklemeden ilerleyebilir; HAT-B (compiler'ın hangi sınıfta kurulacağı, K2-f/g) örnek sayısı sıfır olduğu için beklemeli — bu ikisi ayrı kararlardır.
7. K2-c/d/e (şablon alanları) TEK TEK ele alınmalı — dördünü birden eklemek antitez tarafından açıkça reddedildi.
8. K2-h/i ucuz, karşı-tarafsız onay kalemleri (~15 dk); K2-l/m aynı "ölçüm disiplini" ailesinden, ayrı kararlar.
9. Bu koşumun maliyeti $16,06 — eski $14 tavanı aşıldı, Salih'in önceden verdiği fren-gevşetme emri yerinde çıktı; bu tür koşumların maliyet kestirimi %24-78 düşük sapıyor (B8 kalibrasyon borcu, ayrı).
10. Hiçbir kalemde rakam uydurulmadı; bilinmeyen yerler `[?]` ile işaretli (yalnız K2-n'nin geriye-dönük-denetim maliyeti tahmini).

---

## Koşum künyesi

- **Emir doğrulama:** `main` dalı · `cc/gorev-2026-08-02-2.md` · ilk başlık birebir: *"# Görev Emri — cc/gorev-2026-08-02-2 (ÇEVİRİ/E5: K2 masası HAZIRLIK DOSYASI — Salih için İNSAN-register karar rehberi)"* · SHA doğrulandı: `a6332f9baa210c42ede469fca1372d96d7292be4` (koşum başında `git rev-parse HEAD` ile teyit edildi, promptta verilen SHA ile birebir eşleşti). Yazılabilir-yüzey kontrolü: hedef dosya koşum başında YOKTU, mükerrer-sevk freni tetiklenmedi.
- **Okunan dosyalar:** `kuyruk/masa-gundemi-K2-2026-08-02.md` (tam) · `cc/rapor-2026-08-02-1.md` §0, §7.1-§7.6, §8 (grep-hedefli, tam dosya okunmadı — 659 satırdan ~180 satır okundu) · `raporlar/vardiya-teslim-2026-08-02-anasira.md` (tam) · `kuyruk/build-tartisma-notlari.md` (tam, D-0802-1/2 + B1-B9 blokları için) · `raporlar/2026-07-26-compiler-formulu.md` (tam, F1-F9 için).
- **Yasaklara uyum:** karar alınmadı, öneri işareti değiştirilmedi, kanon dosyasına yazılmadı, web araması yapılmadı, V-numarası atanmadı, git commit/push yapılmadı, rakam uydurulmadı (bilinmeyenler `[?]`).
- **/usage:** RAPORLANMADI, Salih yapıştıracak.
