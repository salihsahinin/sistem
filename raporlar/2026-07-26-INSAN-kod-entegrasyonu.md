# Kod Entegrasyonu — insan yüzü

> Kaynak: `raporlar/2026-07-26-kod-entegrasyonu.md` · Register: kavrayış · Compiler: **AÇIK** (F1-F9)
> **UYARI: Bu dosya karar kaynağı DEĞİLDİR.** Katman-1 kararı teknik kayıttan alınır. Her maddenin sonunda kaynak bölüm var.

---

## 1. Tek cümlede

**Kod, metnin yerine geçmez; metnin doğrulanamayan kısmını devralır** — ve metin, yalnızca **dışarıdan denetlenen** bir icra katmanına bağlıysa etki üretir; kâğıt üzerinde zorunlu kılınmak etkiyi **sıfırlar**.

---

## 2. Ne bulduk

### ① Öncülün kendisi doğru — sistem %87 markdown

- **İddia:** İzlenen 172 dosyanın **148-149'u markdown** (%86,6), yaklaşık 11.750 satır.
- **Neye dayanıyor:** İki bağımsız ölçüm, aynı sonuç.
- **Ne kadar güveniyoruz:** Yüksek.
- **Ama iki düzeltme var.** Birincisi: *"sadece md"* tam doğru değil — beceri klasörlerinde değerlendirme verisi dosyaları var, yani **embriyonik bir doğrulama katmanı zaten mevcut** (koşan bir harness değil, elle üretilmiş veri). İkincisi ve asıl bulgu: var olan **4 yürütülebilir dosya rastgele yerlerde değil, tam olarak zorlama gereken yerlerde** — `core/` yazımını engelleyen hook ve push doğrulayıcı.
- **Ne yapmamız gerekiyor:** Sistem *"kural metinle yazıldı, tutmadı, koda taşındı"* yolunu **zaten bir kez yürümüş**. Bu raporun tezi bunun genelleştirilmesidir.
- → `kod-entegrasyonu §0`

### ② ⭐ Markdown'da "hata" kavramı yok — bu kusur değil, tasarım

- **İddia:** Spesifikasyon birebir şöyle diyor: *"Any sequence of characters is a valid CommonMark document."* Ve sonucu da söylüyor: *"Markdown'da hiçbir şey 'sözdizimi hatası' sayılmadığı için, sapma çoğu zaman hemen fark edilmiyor."*
- **Neye dayanıyor:** Birincil kaynak (spec metni).
- **Ne kadar güveniyoruz:** Çok yüksek. **Ve antitez bunu sınadı — çürütemedi**; spec'i birebir doğruladı.
- **Ne yapmamız gerekiyor:** **Sessiz bozulma Markdown'ın kusuru değil, tasarım özelliğidir.** Geçersiz belge yoksa, hata kavramı da yoktur.
- → `kod-entegrasyonu §1.1`

**Ölçek notu:** Orijinal tarifin cevaplamadığı 14 belirsizliği kapatmak **9.811 satır spec + 655 uygunluk testi** gerektirdi. Ve GitHub'ın sürümü hâlâ eski bir spec sürümüne sabitli — *"Markdown"* tek bir dil bile değil.

### ③ Denetlenebilirlik tavanı sandığımızdan yüksek çıktı

- **İddia (düzeltildi):** Markdown'ı **metin olarak** denetleyen araçların tavanı **referans bütünlüğüdür** — en olgun linter 53 kural taşır ve hepsi tipografik/sözdizimseldir.
- **Ne değişti:** Rapor önce *"araçların erişebildiği **azami** katman **yalnız** referans bütünlüğü"* demişti. Antitez karşı örnek gösterdi: **`doctest` ve `nbval`** dokümanın içindeki kod bloklarını **çalıştırıp beklenen çıktıyla karşılaştırır** ⇒ **davranışsal doğruluk** denetlerler.
- **Ne kadar güveniyoruz:** Düzeltmeye yüksek.
- **Ne yapmamız gerekiyor:** Bu **tezi zayıflatmıyor, keskinleştiriyor**: metnin doğrulanabilir kısmı, **içine gömülmüş yürütülebilir parçalar** kadardır. Düzyazı iddiası hâlâ denetlenemez — ama *"şu komut şu çıktıyı verir"* biçiminde yazılmış bir cümle **denetlenebilir hâle gelir**.
- → `kod-entegrasyonu §1.1`

### ④ Doküman-kod sapması ölçülmüş bir norm

- **İddia:** Kod değişikliklerinin yalnız **%13-20'si** bir yorum değişikliği tetikliyor (1.500 sistem, 1,3 milyar değişiklik). Tutarsız değişiklikler tutarlı olanlara göre **~1,5 kat** fazla bug doğuran commit üretiyor.
- **Ve tam bizim sınıfımız:** AI yapılandırma dosyalarında (CLAUDE.md sınıfı, 82 depo) **230 bayat kod referansı = %23,0**; doküman sorunlarının **%39'u** bayatlık; katılımcıların **üçte ikisinden fazlası** kendi sistem dokümanının bayat olduğuna inanıyor.
- **Neye dayanıyor:** İkincil kaynaklar; ölçek verisi replikasyon deposundan birincil.
- **Ne kadar güveniyoruz:** Orta-yüksek. Rakamlar ikincil, **yön** güvenilir.
- **Ne yapmamız gerekiyor:** **Sapma normdur, istisna değil.** Bunu bir disiplin sorunu sanmayı bırak.
- → `kod-entegrasyonu §1.2`

### ⑤ "Yürütülebilir doküman" geleneklerinin sicili kötü

- **Literate programming ölü:** endüstriyel ölçekte (>10K satır) bununla yazılmış üretim sistemi **bulunamadı** — yokluğun kendisi bulgu. 40 yılda bulunabilen **tek kontrollü deney** (14 denek) zaman ve doğrulukta **anlamlı fark bulamadı**. 2000 sonrası kontrollü karşılaştırma **yok**.
- **Notebook'lar — en sert rakamlar:** 1.450.071 notebook / 265.143 depo taramasında çalıştırma denemelerinin yalnız **%24,11'i hatasız koştu**; yalnız **%4,03'ü orijinaliyle aynı sonucu üretti**. Sırası belirlenebilenlerin **%36,4'ü** sırasız çalıştırılmış — ve **bağımsız bir ekip 10 milyon notebook'ta ~%36 bulmuş**. Farklı ekip, farklı örneklem, **aynı rakam** ⇒ bu hattaki en sağlam sayı.
- **Docs-as-code — ampirik zemini yok:** en bilinen çerçevenin **yazarı kendi metninde** itiraf ediyor: *"bu, Diátaxis'e bir dokümantasyon teorisi olarak güvenmek için yeterli değil."*
- **Ne kadar güveniyoruz:** Notebook rakamlarına yüksek (çapraz doğrulanmış). Literate programming'e orta — **yokluk kanıtı**, ve tek deneyin tasarımı ikincil kaynaklarda çelişkili aktarılıyor.
- → `kod-entegrasyonu §1.3`

### ⑥ ⭐ Metni çalıştırılabilir kılmanın ölçülmüş getirisi

- **İddia:** **3.000+ sayfalık** metinsel bir spesifikasyon 5.000 satırlık çalıştırılabilir modele çevrildi ve implementasyona karşı koşuldu ⇒ **200'den fazla sorun** bildirildi. *Metin yıllarca orada duruyordu; sorunlar ancak metin çalıştırılabilir hâle geldiğinde göründü.*
- **Ve ikinci kanıt:** Bir bulut sağlayıcıda 804 satırlık spec **2 bug**, 645 satır **1 bug**, 939 satır **3 bug** buldu — ve bu bug'lar tasarım incelemesinden, kod incelemesinden **ve testten** geçmişti. Mühendisler aracı **2-3 haftada** öğrendi.
- **Neye dayanıyor:** İkincil (endüstri raporları).
- **Ne kadar güveniyoruz:** Orta-yüksek. Bu, *"kod ekle"* tezinin **en güçlü kanıtıdır**.
- → `kod-entegrasyonu §1.4`

### ⑦ Metnin doğrulanamazlığı — beş bağımsız araç, aynı tavan

- **İddia:** Gereksinim analizi araçlarının hepsi aynı duvara çarpıyor: kesinlik **%59-68** bandında, ve isabeti %100'e çıkarınca kesinlik düşüyor. **Hiçbiri güvenilir otomatik denetim eşiğine (~%90/%90) ulaşmıyor.** Çelişki tespitinde en iyi araç bile **çelişkilerin %40'ını hiç görmüyor**.
- **Neye dayanıyor:** Beş ayrı araç ailesinin ölçümleri.
- **Ne kadar güveniyoruz:** Yüksek — **örüntü sabit**, tek bir çalışmaya dayanmıyor.
- **Ne yapmamız gerekiyor:** Düzyazı kuralı otomatik denetlenemez. Vekil ölçüt yazarsan **kuralı değil, gölgesini** ölçersin.
- → `kod-entegrasyonu §1.5`

### ⑧ ⭐⭐ Metin ölüm oranını yarıya indirebiliyor — ama tek bir koşulla

Bu, raporun **en önemli bulgusudur** ve görev emrinde olmayan bir hattan geldi.

- **Saf metin çalışıyor:** 19 maddelik bir kontrol listesi, 8 ülke, 8 hastane ⇒ ölüm **%1,5'ten %0,8'e** (p=0,003), komplikasyon **%11,0'dan %7,0'a** (p<0,001).
- **Aynı müdahale başka yerde hiçbir şey yapmadı:** 101 hastane, 215.711 işlem ⇒ ölüm %0,71'den %0,65'e (p=0,13). **101 hastanenin hiçbirinde anlamlı iyileşme yok.**
- **Farkı yaratan ne:** Başarılı vakalarda uyum **ölçüldü**, veri toplandı, ekip eğitildi, geri bildirim döngüsü kuruldu. Başarısız vakada kontrol listesi **yönetmelikle zorunlu kılındı ve uyum öz beyanla raporlandı**.
- **Ne kadar güveniyoruz:** Yüksek — iki yönlü ölçüm var, ve fark mekanizması net.
- **Ne yapmamız gerekiyor:** **Metin, yalnızca dışarıdan denetlenen bir icra katmanına bağlıysa etki üretir. Kâğıt üzerinde zorunlu kılınmak etkiyi sıfırlar.**
- → `kod-entegrasyonu §1.6`

**Analoji:** Bir yasa çıkarmakla o yasanın uygulanması arasındaki fark. Metin aynı metindir; farkı yaratan **denetim makinesidir**.

### ⑨ ⭐ Git hook'ların sigorta değil, hatırlatıcı

- **İddia:** `git commit -n` ve `git push --no-verify` hook'u **atlar**. Hook'lar **klonla gelmez**. Sunucu tarafındaki `pre-receive` ise farklıdır: sıfırdan farklı çıkış kodu döndürürse **hiçbir referans güncellenmez**.
- **Neye dayanıyor:** Git'in kendi dokümanı — birincil.
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** Mevcut `core/` telin ve push doğrulayıcın **danışmanlık gücü taşıyor, zorlama gücü taşımıyor**. Bu bir kusur değil — tek kişilik bir sistemde *"yanlışlıkla"* hatalarının çoğunu yakalayan da budur. Ama **sigorta sanma**.
- → `kod-entegrasyonu §2.3`

**Ve atlanamaz katman şurada:** GitHub ruleset'leri — dosya yolu kısıtı, commit metadata kuralları, ve **üç mod: aktif / evaluate (bloklamadan izleme) / kapalı**.
⚠️ **Kritik varsayılan:** dal koruması **admin yetkisi olan kişiye uygulanmaz** ⇒ tek kişilik bir repoda koruma, *"Do not allow bypassing"* kutusu işaretlenmedikçe **kendi kendine uygulanmaz**.

### ⑩ Hazır policy-as-code yığını bizim işimize yaramıyor

- **İddia:** Conftest'in **21 parser'ı arasında markdown yok** (kaynak kodundan okundu) ve **stdin desteği de yok**. `check-jsonschema` markdown okuyamaz — desteklediği formatlar yalnız JSON, TOML, YAML. OPA'nın girdisi JSON'dur.
- **Neye dayanıyor:** Kaynak kodundan birincil.
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** **Bu yolu kullanma.** Yeni bir dil öğrenmek ve bir çevirici katmanı bakmak gerekir. Yerine markdown-yerli araçlar: lychee (referans bütünlüğü), obsidiantools (graf), Vale (terminoloji), markdownlint (yapı), gitleaks (sır sızıntısı).
- → `kod-entegrasyonu §2.1` · `§2.5`

### ⑪ Veri modelin araçlardan uzun yaşamalı

- **İddia:** Bu alandaki araçlar hızla ölüyor. Bir bilgi tabanı aracı **öldü** (*"yalnız bakım, aktif geliştirme durdu"*) ve tam bizim aradığımız hiyerarşi şemalarını sunuyordu. Bir sorgu eklentisi el değiştirdi. Bir başkası 1.9.2'de **format kırdı**.
- **Neye dayanıyor:** Birincil (depo ve sürüm kayıtları).
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** **Bilgi tabanının veri modeli, hiçbir aracın ömründen kısa olmamalı.** Veri modelin düz YAML front matter'da yaşarsa, araçların hepsi ölse bile **verin sağ kalır**.
- → `kod-entegrasyonu §2.6`

**Ve bir karşı örnek dersi:** bir ADR aracı metaveriyi front matter'a koymuyor, bir başlığın altına **düz metin** olarak yazıyor ⇒ *durum bilgisini prozaya gömersen, sonsuza dek regex yazarsın.*

### ⑫ TDD'nin en ünlü rakamı bir ölçüm değil

- **İddia:** En çok alıntılanan endüstriyel TDD çalışmasındaki *"%15-35 geliştirme süresi artışı"* rakamı, makalede açıkça **`[Management estimates]`** etiketlidir — yani **öznel hatırlama**.
- **Ve daha fazlası:** Aynı makalenin nesnel adam-ay tablosundan hesaplanan normalize hız **0,68 kat (daha hızlı) ile 3,65 kat (daha yavaş)** arasında saçılıyor — *"%15-35"* ile **bağdaşmıyor**. Örneklem 4 proje, anlamlılık testi yok, ve makalenin kendi itirafı: *"iki proje arasında asla doğru bir eşit karşılaştırma olamaz."*
- **Neye dayanıyor:** **Birincil PDF okundu.**
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** *"TDD %15-35 verim kaybettirir"* diye alıntı yapan herkes **bir yöneticinin görüşünü** alıntılıyor, bir ölçümü değil.
- → `kod-entegrasyonu §3.1`

**Ve mekanizma olarak ayakta kalan şey "test-first" değil:** bir ayrıştırma çalışması TDD'yi dört boyuta böldü ve iyileşmelerin **granülerlik** (döngü süresi) ve **düzgünlük** (döngü varyansı) ile ilişkili olduğunu, **sıralamanın önemli bir etkisi olmadığını** buldu. ⇒ Ajan çağına aktarılabilir hâli: **küçük, düzgün, doğrulanmış artışlar zorunlu kıl — ritüel sıralama değil.**

### ⑬ ⭐ Ajan çağının yeni başarısızlık modu

- **İddia:** Başarılı sayılan yamaların **%32,67'sinde çözüm sızıntısı** (düzeltme zaten sorunun içinde yazılı) ve **%31,08'i zayıf testler yüzünden şüpheli**. Filtrelemeden sonra bir ajanın çözüm oranı **%0,55'e** düştü.
- **Neye dayanıyor:** İkincil (benchmark çalışması).
- **Ne kadar güveniyoruz:** Orta-yüksek.
- **Ne yapmamız gerekiyor:** **Aynı aktör hem testi hem kodu yazarsa, test spesifikasyon olmaktan çıkıp optimizasyon hedefi olur.** Ajan çağının *"test-first"* karşılığı: **kabul testi, optimize eden taraftan başkası tarafından yazılmalı ya da saklanmalı.**
- → `kod-entegrasyonu §3.3`

### ⑭ Portfolyo tavsiyelerinin ölçülmüş hiçbir dayanağı yok

- **İddia:** GitHub linkini ya da repo özelliklerini değiştirip geri dönüş oranını ölçen **tek bir audit çalışması bulunamadı**. Test varlığı, CI rozeti, commit geçmişi ya da README kalitesi ile işe alım sonucu arasında bağ kuran **hiçbir çalışma yok** — hiçbir tasarımda.
- **Var olan tek net sonuç NEGATİF:** *"Katkı sayısıyla ölçülen açık kaynak katılımının kendisi ücret artışıyla ilişkili DEĞİL. Ancak liyakate dayalı bir sıralamada daha yüksek statü, anlamlı biçimde daha yüksek ücretle ilişkili."*
- **Ne kadar güveniyoruz:** Yokluk bulgusuna orta-yüksek; negatif sonuca orta (ikincil).
- **Ne yapmamız gerekiyor:** *"CI rozeti ekle, yeşil kal, harika README yaz"* tavsiyesinin işe alım sonucuyla **ölçülmüş hiçbir bağı yok**. Bu bir **ekstrapolasyondur**.
- → `kod-entegrasyonu §3.5`

**Ama ölçülmüş bir boşluk var:** README'lerin **~%74'ü** projenin neden var olduğunu hiç söylemiyor; **~%79'u** durumunu belirtmiyor (ham veriden kendi hesabımız). ⇒ Gerçek bir farklılaşma fırsatı — ama işe alıma bağlı olduğu **kanıtlanmamış**.

**Ve bir çelişki:** yeşil kareler kısmen iş arama dönemine **stratejik olarak zamanlanıyor** ⇒ katkı grafiği iş aramaya **içseldir**, dolayısıyla yeteneğin **kirlenmiş bir ölçüsüdür**.

---

## 3. Ne bulamadık

### Aradık, bulamadık — bu bir bulgudur

| Ne | Not |
|---|---|
| **Endüstriyel ölçekte literate programming ile yazılmış üretim sistemi** | 40 yıllık gelenekte bulunamadı. **Yokluğun kendisi bulgu.** |
| **2000 sonrası literate programming kontrollü karşılaştırması** | Yok. |
| **Docs-as-code'un ampirik zemini** | Resmî sayfa **hiçbir ölçüm, çalışma ya da atıf içermiyor**. Var olan tek büyük veri seti self-report anket ve korelasyonel. |
| **Wiki / kişisel bilgi sistemi bayatlaması üzerine hakemli ölçüm** | Yok. Tek veri noktası (n=13) yazarlarınca *"keşifsel"* ilan edilmiş. ⇒ **Tezin özgün katkı alanı.** |
| **Ajan performansını notebook ile script formatında karşılaştıran benchmark** | Yok. Mekanizma birincil kaynaklardan doğrulandı ama **kimse "%X daha kötü" diyemez** ⇒ *"notebook ajan için kötü"* iyi temellendirilmiş bir **hipotezdir**, kanıtlanmış bir olgu değil. |
| **Portfolyo özelliklerinin işe alım sonucuyla bağı** | Hiçbir tasarımda hiçbir çalışma. |

### **Arayamadık** — bunlar yokluk hükmü DEĞİL

| Ne | Neden |
|---|---|
| **A18 ailesinin tamamı (TDD, portfolyo blokları)** | Antitez turunda **hiç test edilemedi** — akademik kanallar 403. Antitezin kendi ifadesi: *"Bu bir **kapasite itirafıdır**, iddiaların doğruluğu hakkında hüküm değildir."* ⇒ §3'ün hiçbir iddiası ne doğrulandı ne çürütüldü. |
| TDD meta-analizinin etki büyüklükleri | Birincil metne erişilemedi. |
| Ödül hackleme çalışmasının birincil metni | Erişilemedi. |
| Büyük ölçekli mutation testing sonuçları | **Hiç ulaşılamadı.** |
| A17'nin yarım kalan şeritleri | Oturum limiti kesti: tip ipuçlarının hata oranına etkisi, Python tek kişilik araç getirisi, deney takip maliyeti, ML teknik borç ölçekleri, aşırı mühendislik maliyeti, notebook yeniden üretilebilirlik ikinci turu, kabuk/CLI doküman testi araçları. |

---

## 4. Ne değişiyor

**Öncelik sırasına göre ilk adımlar (maliyet sırasıyla):**

1. **lychee** — pointer bütünlüğü. Tek binary, ~sıfır bakım, ve 148 dosyalık bir pointer sisteminde **en yüksek getirili tek denetim**. → `§4`
2. **`obsidiantools`** — yetim not ve ölü pointer hedefi taraması. Tek `pip`. → `§4`
3. **GitHub ruleset, `evaluate` modunda** — `core/` yol kısıtı. **Önce ölç, sonra zorla.** Ve *"Do not allow bypassing"* kutusunu işaretle, yoksa admin olarak **kendine uygulanmaz**. → `§4`
4. **Front matter şeması** — yalnız `id`, `type`, `status`, `date`, `pointers`. **Gövde metinde kalır.** → `§4`
5. **`cog --check`** — `pano.md` türetilir, elle yazılmaz; bayatlık CI kapısı olur. → `§4`
6. **Vale** — tüzüğün sözcük düzeyi normları (emekli terimler). Rego'ya değil **Vale'e** çevrilir ve dönüştürücü katman gerektirmez. → `§4`
7. **YENİ (K44'ten) — `doctest`/`nbval` sınıfı davranışsal denetim.** Kanon metnindeki *"şu komut şunu döndürür"* cümlelerini **çalıştırıp** doğrular. Denetlenebilirlik tavanının sanılandan yüksek olması buradan geliyor. → `§4`

**Katman ayrımı — ne nereye gider:**
- **Şemaya taşınır:** dosyanın kimliği ve durumu (`id`, `type`, `status`, `date`, `supersedes`, `pointers`, `owner`) — sonlu ve enum'lanabilir.
- **Metinde kalır:** madde metninin kendisi, gerekçe, tartışma.
- **Türetilir:** pano tablosu, indeksler, geçersizlik grafı — **elle yazılmaz**.
→ `§2.7`

**Kaçınılacak yol:** OPA / Conftest / Rego. → `§2.1`

**Projeler tarafı:** granülerlik ve düzgünlük zorunlu kılınır (ritüel sıralama değil); **kabul testi ajandan bağımsız yazılır ya da saklanır**; notebook'tan modüle geçiş hipotez düzeyinde ama mekanizması sağlam; portfolyo tavsiyelerinin çoğu **kanıtsızdır** — README'nin *"neden"* ve *"durum"* alanları ölçülmüş bir boşluk olduğu için oraya yatırım yapmak savunulabilir. → `§4`

---

## 5. Kontrol

*Bu raporu okuduktan sonra şu üç soruyu cevaplayabiliyor musun?*

1. **Bir kuralı CLAUDE.md'ye yazdın ve tutmadı. Bu raporun kanıtına göre kuralı "daha net yazmak" neden çözüm değil — ve çözüm hangi katmanda?**

2. **Mevcut `core/` yazım kilidin bir hook. Bu hook'un yakalayamadığı iki durum ne, ve aynı kuralı atlanamaz hâle getirmek için nereye taşıman gerekir?**

3. **"Markdown denetlenemez" cümlesi bu turda daraldı. Denetlenebilen kısım tam olarak neresi, ve bir kanon cümlesini denetlenebilir hâle getirmek için nasıl yazman gerekir?**
