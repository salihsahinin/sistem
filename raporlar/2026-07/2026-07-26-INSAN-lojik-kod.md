# Lojik Dil → Kod Dil Dönüşümü — insan yüzü

> Kaynak: `raporlar/2026-07-26-lojik-kod-atlas.md` · Register: kavrayış · Compiler: **AÇIK** (F1-F9)
> **UYARI: Bu dosya karar kaynağı DEĞİLDİR.** Katman-1 kararı teknik kayıttan alınır. Her maddenin sonunda kaynak bölüm var.

---

## 1. Tek cümlede

Önermelerini koda çevirirken kaybolan şey **önermenin kendisi değil, kipidir** — `∀` sonlu bir örnekleme, `→` tek bir dala, `¬` *"bulunamadı"*ya, `[?]` ile `⊨X` tek bir `None`'a çöker — **ve her çöküş sessizdir**: kod derlenir, test geçer, hata fırlamaz.

---

## 2. Ne bulduk

### ① ⭐ Kaybın kendisi sessiz — asıl tehlike bu

- **İddia:** Yukarıdaki dört çöküşün hiçbiri hata üretmez. Kod çalışır, testler yeşildir, spec ihlal edilmiştir.
- **Neye dayanıyor:** Kavramsal argüman + araçların kendi dokümantasyonu. **Ölçüm değil.**
- **Ne kadar güveniyoruz:** Argümana yüksek, **kanıta düşük**. Bu ailenin en açık zayıflığı: doğal dil→mantık çevirisinde **ölçülmüş hata oranı bulunamadı** — ve bunun sebebi arama bütçesinin tükenmesiydi, alanın boş olması değil. Yani bu tablo **kavramsal argümandır**, ampirik bulgu değil.
- **Ne yapmamız gerekiyor:** Tabloyu kullan, ama *"ölçüldü"* diye sunma.
- → `lojik-kod §1.3` · `§5 M3`

**Analoji:** Bir şiiri başka dile çevirirken kelimeler yerine oturur ama vezin kaybolur. Burada kaybolan vezin, önermenin **ne kadar kesin olduğudur** — ve okuyan kod, kesinlik farkını göremez.

### ② ⭐ Senin notasyonunun ayırt ettiği iki şeyi kod birleştiriyor

- **İddia:** `[?]` (kestirim) ile `⊨X` (çelişkili) naif çeviride **aynı `None`'a** düşer. `None` üç değerli mantığı gizlice ikiye indirger; ayrıca *"bilinmiyor"*, *"boş"* ve *"hata"* aynı değerle temsil edilir.
- **Neye dayanıyor:** Dillerin kendi semantiği — SQL'de `NULL = NULL` sonucu `UNKNOWN`'dır, Python'da `None == None` sonucu `True`'dur.
- **Ne kadar güveniyoruz:** Yüksek. **Ve antitez burada bir şey düzeltti:** bu kayıp **kaçınılmaz değil**. Rust'ın `Option<T>` ve `Result<T,E>` tipleri yapısal olarak eşdeğerdir ama **farklı amaçlarla** kullanılır ⇒ ayrım kaybolmadan taşınabilir.
- **Ne yapmamız gerekiyor:** Kod karşılığını **şimdiden yaz**: `[?] → Unknown`, `⊨X → Contradictory`, ayrı dal ayrı tip.
- → `lojik-kod §1.3` · `§4 L30`

> **Düzeltmenin ilginç yanı: iddia zayıflarken tavsiye güçlendi.** *"Geri alınamaz biçimde kaybolur"* yanlıştı. Ama kayıp kaçınılmaz değilse, **kaçınmak bir karardır** — ve V76 (notasyona kod-karşılığı sütunu eklemek) tam olarak o kararı şimdiden vermektir.

### ③ Üç mutlak ifade fazla güçlüydü — üçü de düştü

Bu rapor üç yerde *"imkânsız"*, *"geri alınamaz"*, *"yalnız"* dedi. Antitez üçünde de karşı örnek buldu.

| Ne demiştik | Ne çıktı | Ne kalıyor |
|---|---|---|
| *"`t`/`t+1` mutasyonla yazılırsa invariant kontrolü **imkânsız** hâle gelir"* | `pyrsistent` gibi immutable yapılar ve event sourcing bunu **korur** | *"Naif mutasyon stilinde kaybolur"* — ve çözüm zaten tablomuzun kendi *"doğrusu"* sütunundaydı |
| *"`[?]`/`⊨X` ayrımı **geri alınamaz** biçimde kaybolur"* | Rust'ın `Option`/`Result` ayrımı bunu taşıyor | Kayıp **bir tasarım tercihinin sonucu** |
| *"Model-checking **yalnız** spec üzerinde çalışır"* | **CBMC** doğrudan C/C++ **programlarını** doğruluyor | Ve dahası: CBMC *bounded*'dır ⇒ üstünlüğü **koşulsuz değil** |

- **Ne kadar güveniyoruz:** Düzeltmelerin hepsi birincil kaynaktan (depo metinleri) — yüksek.
- **Ne yapmamız gerekiyor:** Ortak kalıbı görmek: **mutlak niceleyici tek bir karşı örnekle düşer.** Üçünde de karşı örnek vardı ve biz aramamıştık.
- → `lojik-kod §1.5` · `antitez §7.1`

### ④ En güçlü ölçülmüş güvence: biçimsel doğrulayıcı

- **İddia:** Kod, docstring ve biçimsel ek açıklama üçlüsü arasında tutarlılık kontrolü yapan Clover sistemi, doğru kodun **%87'sini kabul etti** ve yanlış kodda **ölçülen yanlış-pozitif sayısı sıfırdı**.
- **Neye dayanıyor:** Birincil kaynak (CloverBench, Dafny, ders kitabı seviyesi problemler).
- **Ne kadar güveniyoruz:** Yüksek — bu ailenin **en güçlü tek kanıtı**. Sınır: ders kitabı seviyesi problemler, üretim kodu değil.
- **Ne yapmamız gerekiyor:** *"İkinci bir doğrulayıcıyla kontrol"* fikrinin **ölçülmüş** karşılığı budur — ve bu, biçimsel bir doğrulayıcıdır, ikinci bir LLM değil.
- → `lojik-kod §2.1 L7`

### ⑤ Literatür bizim sorumuzu ölçmüyor

- **İddia:** Literatürün büyük kısmı *"formalize edilmiş bir problemi kanıtlama"* başarısını ölçüyor; *"doğal dili doğru formalize etme"* başarısını **değil**.
- **Neye dayanıyor:** Birincil kaynak. DeepSeek-Prover-V1.5'in miniF2F'te %63,5 ve ProofNet'te %25,3 alması, **zaten biçimselleştirilmiş** problemler üzerinde kanıt üretme başarısıdır.
- **Ne kadar güveniyoruz:** Yüksek — ve **ayrımın kendisi bir bulgudur**.
- **Ne yapmamız gerekiyor:** Bizim sorumuz (`önerme → kod`) tam olarak **ölçülmeyen aşamadır**. Bu, boşluğu bizim doldurabileceğimiz anlamına gelir.
- → `lojik-kod §2.3 L12`

### ⑥ Üç benchmark kapsamı tanımlıyor, rakamı vermiyor

- **İddia:** MiniF2F 244 problem tanımlıyor, LogicBench 25 akıl yürütme paterni tanımlıyor (olumsuzlama, De Morgan ve koşullu **dahil**), FOLIO yapısını doğruluyor — **üçünde de kategori bazlı sayısal tablo yok**.
- **Neye dayanıyor:** Üç depo da tarandı.
- **Ne kadar güveniyoruz:** Yüksek. **Ve antitez bunu sınadı**: üç depo yeniden tarandı, karşı örnek çıkmadı ⇒ bu, **bu turun en dirençli yokluk iddiası**.
- **Ne yapmamız gerekiyor:** *"Kategori tablosu yok"* demeye devam edebiliriz — bu, aranıp bulunamamış bir şeydir, aranamamış değil.
- → `lojik-kod §2.3 L13`

### ⑦ Aynı aktörün hem testi hem kodu yazması ölçülmüş bir risk

- **İddia:** Başarılı sayılan yamaların **%32,67'sinde çözüm sızıntısı** var. Testi yazan ile kodu yazan aynıysa test bir spesifikasyon olmaktan çıkıp **optimizasyon hedefine** dönüşür.
- **Neye dayanıyor:** Ölçüm (oturum içi veri, kod-entegrasyonu raporundan).
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** *"LLM'e testleri de yazdır"* güvencesi **kısmen tiyatrodur**. Test yazımı ayrı bir ajana ya da ayrı bir tura verilir.
- → `lojik-kod §2.5` · `§2.6 satır 5`

### ⑧ ▲ Ve bu doğrudan bize bakıyor: önerme formu tek başına yetmiyor

- **İddia:** Güvence sıralamasının **en zayıf** satırı *"prompt'a daha fazla biçimsellik ekle, araç yok"*tur. Senin önerme formun tam olarak bu — **salt metin disiplini**.
- **Neye dayanıyor:** Bu literatürün **tamamı**, salt metin disiplininin tek başına yetmediğini varsayarak üzerine bir **araç katmanı** ekliyor (MiniF2F, FOLIO, Clover, hepsi).
- **Ne kadar güveniyoruz:** Orta-yüksek. Doğrudan *"salt metin şu kadar kötü"* diye bir ölçüm yok; kanıt, **tüm tasarımların aynı varsayımı paylaşması**.
- **Ne yapmamız gerekiyor:** Önerme formu **gerekli ama yeterli değil**. Değeri kodun yerine geçmesi değil, **bir doğrulayıcıya bağlanabilir olmasıdır**.
- → `lojik-kod §2.6`

### ⑨ En yüksek getirili tek hamle

Önerme formundan doğrudan koda gitme. Aradaki basamakları kur:

**önerme formu → sözleşme (öncül = precondition, sonuç = postcondition) → property-based test ile `∀` taraması → kod**

Bu zincir seni güvence sıralamasının **en zayıf 7. sırasından** çıkarıp **2. sırasına** taşır ve **1. sıraya kapı açar**. → `lojik-kod §4 L32`

### ⑩ Cevaplayamadığımız merkezî soru — ama çerçevesi düzeldi

- **İddia (eski):** *"Spec biçimselleştikçe başarı artar"* ile *"biçimsel diller LLM için daha zor, çünkü eğitim verisi az"* **çelişiyor** ve çözülmedi.
- **Ne değişti:** Antitez daha iyi bir çerçeve önerdi: bunlar çelişmiyor olabilir — muhtemelen **ters-U** ilişkisi var. Az biçimsellik belirsizlik kaybettirir; çok biçimsellik dağılım dışı sözdizimi kaybettirir; **ortada bir optimum vardır**.
- **Ne kadar güveniyoruz:** Çerçeveye orta güven, **rakama sıfır** — optimum nerede, ölçülmedi.
- **Ne yapmamız gerekiyor:** Soru değişti ve bu bir kazanç: *"hangisi doğru"* cevaplanamaz bir soruydu; **"optimum nerede"** ölçülebilir bir sorudur.
- → `lojik-kod §2.6 L17`

---

## 3. Ne bulamadık

### Aradık, bulamadık

| Ne | Not |
|---|---|
| **`[?]`/`⊨X` etiketlerinin bir LLM tarafından koda taşınma davranışı** | *Arandı, alan boş.* ⚠️ **Ama kapsam dar tutulmalı:** ölçülmemiş olan **LLM'in davranışıdır**. Belirsizlik/hata ayrımının **koda taşınması** 40+ yıllık literatürdür (Option/Maybe, Rust `Option`↔`Result`, SQL üç değerli mantık). Geniş okuma yanlıştır. |
| Kategori bazlı hata tabloları (olumsuzlama, niceleyici, De Morgan) | Üç benchmark deposu tarandı, karşı örnek çıkmadı. **En dirençli yokluk iddiamız.** |
| Gherkin/BDD'nin endüstride terk edilme oranı | Hiçbir ölçüm yok. |
| Alloy, Z, B-metodu endüstriyel vaka **ölçümü** | Yalnız teknik README okundu; *"ne yakalar"* içeriği yoktu. |
| *"PBT örnek temelli testten %X daha fazla hata buluyor"* | Araç sayfaları **niteliksel** üstünlük iddia ediyor; **nicel rakam hiçbir birincil kaynakta yok**. |

### **Arayamadık** — bunlar yokluk hükmü DEĞİL

| Ne | Neden |
|---|---|
| **Doğal dil→mantık çevirisinde ölçülmüş hata oranları** | Tüm akademik kanallar kapalıydı. **Bu eksenin ampirik desteği şu an sıfırdır** — ama bu, ölçümün olmadığı anlamına gelmez, bizim ulaşamadığımız anlamına gelir. |
| **AWS biçimsel yöntemler raporu (CACM 2015)** | Birincil metne erişilemedi. Bu, ailenin **en çok atıf beklenen endüstriyel kanıtıydı** ⇒ A31'in sanayi ayağı **hatırlama düzeyindedir**. Dolaşan *"TLA+ Amazon'da şu kadar sürecek hatayı bu kadar günde buldu"* rakamları **bu koşumda teyit edilmedi**. |
| EvalPlus'ın tam `pass@1` fark rakamı | Leaderboard kapalı bir adreste. |
| SQL `NULL`, Prolog `\+`, Eiffel/JML birincil kaynakları | Hepsi kapalıydı ⇒ §1.3'ün ilgili satırları **kavramsaldır**, birincil kaynaklı değil. |

---

## 4. Ne değişiyor

1. **Önerme yazarken dört şey bugünden yapılabilir** — dördünün de maliyeti sıfır, dördü de çeviri anında **geri kazanılamayacak** bilgiyi şimdi korur:
   - `∀`/`∃` kullanınca **sırayı açıkça numaralandır** (`∃x∀y` ile `∀y∃x` **farklı matematiksel nesnelerdir**)
   - `→` yazınca **`⇔` kastetmediğini** belirt (tersi test edilmeyecek)
   - `t`/`t+1` içeren önermede **hangi durumun korunması gerektiğini** yaz
   - `P → Q` yazınca **`¬P` durumunda ne olduğunu** ayrıca yaz
   → `§4 L31`
2. **KARAR GEREKİYOR (S3) — V76:** Notasyon tablosuna **üçüncü sütun**: her sembolün kod karşılığı. `[?] → Unknown`, `⊨X → Contradictory`, `∀ → PBT`, `→ → precondition/postcondition`. Maliyeti bir tablo sütunu. **Antitez bu önerinin gerekçesini güçlendirdi** (② maddesi). → `§6`
3. **KARAR GEREKİYOR (S2) — V78:** *"Aranamadı"* etiketi. Bu öneri buraya **ikinci kez ve farklı gerekçeyle** geliyor: açık dünya / kapalı dünya ayrımının notasyondaki karşılığı. **İki bağımsız aile aynı eksiği işaret etti.** → `§6`
4. **Öğrenme sırası hazır (L23–L28):** üç değerli mantık ve `Option` tipleri → niceleyici kapsamı, De Morgan, maddi koşul → açık/kapalı dünya → Design by Contract → property-based testing → model checking.
   İlk üçü **notasyonun kendi semantiğidir** ve **bugün gereklidir**; son üçü **doğrulama merdivenidir** ve kod yazımı başlayınca gerekir. → `§3`
5. **Bir şeyi YAPMA:** model checking'i üretim sistemi olarak kurmak. Kavramı al, sistemi alma — ajan-durma raporundaki U12 hükmü burada da geçerli. → `§3 L28`

---

## 5. Kontrol

*Bu raporu okuduktan sonra şu üç soruyu cevaplayabiliyor musun?*

1. **Bir önermeyi koda çevirdin, kod derlendi ve testler geçti. Bu, önermenin doğru çevrildiği anlamına neden gelmiyor — ve dört çöküşten hangisi bu durumda en olası?**

2. **`[?]` ile `⊨X` neden aynı `None`'a düşüyor, ve antitez bu maddede iddiayı zayıflattığı hâlde tavsiye neden güçlendi?**

3. **Önerme formun bu literatürün güvence sıralamasında hangi sırada, ve oradan çıkmak için gereken tek hamle ne?**
