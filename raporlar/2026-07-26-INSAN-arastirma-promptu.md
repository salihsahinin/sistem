# Araştırma Promptu Verimi — insan yüzü

> Kaynak: `raporlar/2026-07-26-arastirma-promptu-atlas.md` · Register: kavrayış · Compiler: **AÇIK** (F1-F9)
> **UYARI: Bu dosya karar kaynağı DEĞİLDİR.** Katman-1 kararı teknik kayıttan alınır. Her maddenin sonunda kaynak bölüm var.

---

## 1. Tek cümlede

Prompt veriminin en yüksek getirili kolu ölçüm eklemek değil, **ajanın ne bilmediğini söyleyebilmesini yapısal olarak mümkün kılmaktır** — ve bu raporun kendisi, tam olarak bu kuralı **iki yerde ihlal ettiği** için antitezde düştü.

---

## 2. Ne bulduk

### ① ⭐ Bağlam penceresi iddia edildiği kadar değil

- **İddia:** Modellerin **ölçülmüş etkin uzunluğu**, iddia ettikleri pencereden çok daha küçük. Kelime örtüşmesinden arındırılmış bir testte GPT-4o'nun etkin uzunluğu **8K**, Claude 3.5 Sonnet'in **4K**, Gemini 1.5 Pro'nun **2K** çıktı.
- **Neye dayanıyor:** İki bağımsız benchmark deposuna inildi (RULER 17 model, NoLiMa 12 güncel model).
- **Ne kadar güveniyoruz:** Yüksek. NoLiMa'nın tasarımı kritik: literal kelime örtüşmesi **yok** ⇒ ölçtüğü şey konum etkisi değil, **anlamsal seyrelme**. 32K'da 12 modelin **10'u** kısa bağlam tabanının yarısının altına düşüyor.
- **Ne yapmamız gerekiyor:** Bağlam bütçesini **nominal pencereye göre değil, ölçülmüş etkin uzunluğa göre** ayarla. Dikkat gerektiren işte **2K–16K** varsay.
- → `arastirma-promptu §2.1`

**Analoji:** Bir kamyonun ruhsatında yazan azami yük ile virajda devrilmeden taşıyabileceği yük aynı sayı değildir.

### ② ⭐⭐ Çok-ajan başarısızlıklarının en büyük kaynağı brifing

- **İddia:** Çok-ajan sistemlerin başarısızlıklarının **%37,17'si** *"Poor Specification"* — yani görev ve sistem tasarımının **en baştan kötü kurulması**. Koordinasyon sorunları %31,41, kalite kontrol %31,41.
- **Neye dayanıyor:** Yazarların yayımladığı taksonomi figürüne **doğrudan inildi ve okundu** — ikincil aktarım değil.
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** *"Araştırma promptunun verimi"* sorusu **ikincil bir iyileştirme değil, birinci kaynaktır**. Salih'in bu konuyu açma sezgisi bağımsız bir ölçümle doğrulandı.
- → `arastirma-promptu §2.6 Q9b`

> **Ve alt kırılımda bir şey daha var:** *"yanlış doğrulama"* (%13,61) *"eksik doğrulama"*dan (%9,16) **daha büyük**. Yani **kötü hakem, hakemsizlikten daha zararlı.** Bu, m.40b'nin maskeli hakemlik tasarımını dışarıdan doğruluyor.

### ③ ⭐ Aramalar sessizce boşa dönüyor — ve bu negatif bulgu uydurtuyor

- **İddia:** WebSearch bütçesi oturum başına 200'dür, ana konuşma ve tüm alt-ajanlar **aynı sayaçtan** yer, ve tükendiğinde **hata vermez** — arama yapılmış gibi görünüp boş döner.
- **Ek bulgu:** Plan yükseltmesi kotayı sıfırlar ama **bu sayacı sıfırlamaz**.
- **Neye dayanıyor:** Birincil kaynak.
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** Ajan bunu bilmezse **`aranamadı` durumunu `bulunamadı` diye raporlar** ⇒ negatif bulgu **uydurulur**. Brifinge zorunlu madde.
- → `arastirma-promptu §1 Q5`

### ④ ⛔ Ve tam olarak bu hatayı biz yaptık — iki kez

- **İddia (düzeltildi):** Bu rapor iki yerde *"hiçbir çalışma yok"* yazdı ve **ikisi de yanlıştı**.
  - *"Özetlemenin bilgi kaybını ölçen hiçbir çalışma yok"* → **koca bir alt-alan var**: QAGS, SummaC, FactCC (özet sadakati metrikleri), LLMLingua (sıkıştırmanın downstream kaybı).
  - *"Negatif talimat için hiçbir ölçülmüş kanıt yok"* → modellerin olumsuzlamaya duyarsızlığını **doğrudan ölçen** çalışma var (Kassner & Schütze, ACL 2020).
- **Neye dayanıyor:** Antitezin karşı örnekleri. ⚠️ Bunlar **hatırlama düzeyindedir** (antitez araç kullanmadı) — ama alan adları spesifik ve tutarlı olduğu için kabul edildi.
- **Ne kadar güveniyoruz:** Düzeltmeye yüksek. İkisinin de sebebi aynı: **arama bütçesi tükenmişti**.
- **Ne yapmamız gerekiyor:** Bu iki madde artık *"aranamadı"* olarak duruyor. Ve bu, `⊨A` etiketinin **dördüncü** bağımsız gerekçesidir.
- → `arastirma-promptu §2.5 ⑧` · `§3.7 ⑥`

> **Bunun ironisi maddenin kendisinden değerli:** raporun **en güçlü tavsiyesi** *"ajanın ne bilmediğini söyleyebilmesini mümkün kıl"*tı. Kural doğruydu; **uygulamayan biz olduk.**

### ⑤ Katı format zorunluluğu ölçülmüş bir maliyet taşıyor

- **İddia:** Katı format zorunluluğu zayıf bir modelde her şeyi çökertiyor: MMLU 43,13'ten **13,27**'ye, GSM8K 70,40'tan **5,47**'ye düştü.
- **Neye dayanıyor:** Birincil sayısal örnek (bir çalışma) + bir ikincil özet.
- **Ne kadar güveniyoruz:** ⚠️ **Orta ve önemli bir sınırla:** bu etki **zayıf bir model** üzerinde ölçüldü (Llama3.1-8b). Bizim ajanlarımız Sonnet 5 ve Opus 5. **Frontier modelde aynı büyüklükte mi, bilinmiyor.**
- **Ne yapmamız gerekiyor:** Bizim dayattığımız katı çıktı şeması (numaralı bulgu, kanıt etiketi, iddia listesi, erişim engelleri) **bu maliyeti taşıyor olabilir**. Şemayı bırakmıyoruz (izlenebilirlik için gerekli), ama **maliyetini ölçmek borç olarak açıldı**.
- → `arastirma-promptu §3.2`

### ⑥ Persona kullanımı tek yönlü kazanç değil

- **İddia (düzeltildi):** Çok-ajanlı persona rol-oynama, tek-ajan zincir-düşünceden **ölçülen bazı kurulumlarda belirgin biçimde** daha kötü sonuç veriyor.
- **Ne değişti:** Rapor önce *"**sistematik olarak** daha kötü"* demişti. Antitez karşı örnek gösterdi: multiagent debate, GSM8K ve MMLU'da tek-ajan zincir-düşünce tabanını **artırıyor**.
- **Ne kadar güveniyoruz:** Ölçüme (GSM8K 47,60 karşısında CoT 80,13) yüksek — **ama bu bir kurulumdur, bir yasa değil**.
- **Ne yapmamız gerekiyor:** Persona/rol atamayı **gerekçesiz kullanma**. Ve bir ayrımı koru: ajanlarımıza *"sen tez ajanısın"* demek **rol değil, görev tanımıdır**.
- → `arastirma-promptu §3.7 ③`

### ⑦ `[D/K/X]` etiketlemesinin gerekçesi yanlıştı

- **İddia:** Atıf/kaynak etiketleme zorunluluğunun **halüsinasyonu azalttığına dair doğrudan kontrollü kanıt yoktur**. Bulunan tek yakın çalışma, zaten atıf üreten sistemlerin **atıf kalitesini** ölçüyor — *"zorunluluk koyarsan azalır mı"* sorusunu **test etmiyor**.
- **Neye dayanıyor:** Birincil kaynak.
- **Ne kadar güveniyoruz:** Yüksek. **Ve antitez bunu güçlendirdi:** salt prompt seviyesinde *"kaynak göster"* talimatı, retrieval olmadan, **yeni bir halüsinasyon alt-türü** üretebiliyor — **uydurma atıf**.
- **Ne yapmamız gerekiyor:** Etiketleme **korunur**, ama gerekçesi düzelir: *"halüsinasyonu azaltır"* değil, **"iddianın kanıt seviyesini okuyucuya açık kılar"**.
- → `arastirma-promptu §3.4`

### ⑧ Tekrar örnekleme sandığımız kadar koruyucu değil

- **İddia (düzeltildi):** Yargıcı üç kez örneklemek **rassal varyansı** azaltır — ama **sistematik yanlılığı azaltmaz**.
- **Neye dayanıyor:** Antitezin mantıksal saldırısı; kabul edildi.
- **Ne kadar güveniyoruz:** Yüksek — bu kavramsal bir düzeltme, olgusal değil.
- **Ne yapmamız gerekiyor:** Üç oy aynı yanlılığı paylaşıyorsa ortaya çıkan şey **sahte çoğulluktur**. Bu yüzden *"farklı model ailesi"* ve *"kanarya maddesi"* tekrar örneklemenin **ikamesi değil, tamamlayıcısıdır**.
- → `arastirma-promptu §4.6 ②`

### ⑨ n=1'de ne meşru, ne değil

- **İddia (düzeltildi):** `n=1`'den çıkan *"bu prompt öncekinden iyi"* hükmü **derece farkı için** meşru değildir. **Ama ikili ya da felaket türü farkta n=1 yeterlidir** — *"her seferinde çöküyor, bu düzeltme çözüyor"* bir mühendislik standardıdır.
- **Ne değişti:** Rapor önce *"asla meşru değildir"* demişti.
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** Ayrım **derece farkı ile ikili fark** arasındadır. Kanarya maddesi (cevabını bildiğin 1-2 soru) tam olarak bu istisnadan yararlanır ⇒ **n=1'de bile geçerli tek testtir**.
- → `arastirma-promptu §4.6 ⑧`

### ⑩ Bir düzeltmemin düzeltmesi — hüküm açık kalıyor

- **Durum:** Oturumun başında *"LLM-as-judge r≈0,31 iddiası çürütüldü, %80+ uyum geçerli"* demiştim. Bu aile bunu **yeniden açtı**.
- **Ne bulundu:** `r≈0,31`'in kaynağı **hiçbir kanalda bulunamadı** — ama varlığı da **reddedilmiyor**. Ve MT-Bench'in bilinen `~%85` rakamı da **bu oturumda teyit edilemedi**.
- **Mekanik açıklama (sentez):** *"%80 uyum"* ile *"r≈0,31"* **çelişmiyor olabilir** — muhtemelen farklı istatistikleri ölçüyorlar: biri örnek düzeyinde bir **oran**, diğeri az sayıda model üzerinden bir **korelasyon katsayısı**. Görev tipi de değiştiriyor.
- **Ne kadar güveniyoruz:** ⚠️ **Bu bir sentezdir, çözüm değil.** Hüküm **açık kalıyor**, kapanmış sayılmıyor.
- → `arastirma-promptu §4.2`

### ⑪ ⭐ Kapalı kaynağın etrafından dolaşmak kaliteyi düşürmedi, yükseltti

- **İddia:** Web arayüzü kapalıyken ham dosya sunucusu açıktı. Bu asimetri boyunca **replikasyon depolarına** yönelmek, kapalı yayıncının etrafından dolaşmanın yoludur.
- **Neye dayanıyor:** Bu koşumda **dört kez** karşılığını verdi.
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** Bunu brifinge standart madde yap: kaynak kapalıysa → replikasyon deposu → upstream git → kaynağın `.md`/`.rst` hâli.
- → `arastirma-promptu §1 Q4`

### ⑫ Ve bir davranış kaydı: ajan üç kez rakam uydurabilirdi, uydurmadı

Üç çalışmanın deposuna **inildi**, metodolojisi **doğrulandı**, ve **rakamı olmadığı için rakam verilmedi**. Bu, brifingteki *"doğrulayamadığın rakamı verme"* maddesinin **canlı karşılığıdır** — maliyeti iki cümle, getirisi üç uydurulmuş rakamın önlenmesi. → `arastirma-promptu §2.2`

---

## 3. Ne bulamadık

### Aradık, bulamadık — bu bir yokluk bulgusudur

| Ne | Not |
|---|---|
| *"More Agents Is All You Need"* ölçek eğrisi | Depoya **fiilen erişildi**, metodoloji doğrulandı (ajan sayısı doğrudan kontrollü değişken), **ama içinde sayı yok**. Statü *"aranamadı"*dan **"bulunamadı"**ya yükseldi. |
| U-şekilli konum eğrisinin kesin sayıları | Depoya inildi, metodoloji doğrulandı, README'de **sonuç tablosu yok**. |
| MT-Bench'in `~%85` insan uyumu | Resmî değerlendirme kodunda konum yanlılığına karşı rastgeleleştirme **standart pratik olarak kodlanmış**, ama README'de uyum yüzdesi **yok**. |
| Format kısıtlamasının kesin yüzdesi | Rakam birincil kaynaktan doğrulanamadı. |
| Persona `~30 puan` düşüş rakamı | Yalnız arama özeti; birincil erişim yok. |
| *"Az kısıtlı vs çok kısıtlı brief"* ekseni | **Hiçbir doğrudan kanıt bulunamadı.** |

### **Arayamadık** — bunlar yokluk hükmü DEĞİL

| Ne | Neden |
|---|---|
| **Özetleme sadakati literatürü** | Arama bütçesi tükenmişti. ⚠️ **Bunu önce "yok" diye yazmıştık — yanlıştı** (QAGS, SummaC, FactCC, LLMLingua **var**). |
| **Olumsuzlama duyarsızlığı literatürü** | Aynı sebep. ⚠️ **Bunu da "yok" diye yazmıştık — yanlıştı** (Kassner & Schütze **var**). |
| Self-consistency getiri düzleşmesi | Birincil kaynaklar (arXiv, openreview) **hiç açılamadı**. Dolaşan *"%40 daha iyi"* iddiası birincil kaynaksız ⇒ **folklor olarak işaretlendi**. |
| Anthropic'in çok-ajan mühendislik yazısı | 403. Muhtemelen paylaşılan-ile-izole bağlam karşılaştırmasını içeriyordu ⇒ **ailenin en hedefli kayıp kaynağı**. |
| Few-shot'un açık uçlu görevlerdeki etkisi | Ayrı bir literatür kümesi bulunamadı — ya da varsa erişilemedi. |

### Ölçtük ama yanlış modelde

Katı format zorunluluğunun maliyeti **zayıf bir modelde** ölçüldü. **Frontier modelde ölçülmedi** — ve bu, raporun kendi ölçüm protokolüyle test edilebilecek **ilk somut hipotezdir**. Yani bu rapor, uygulanmasını önerdiği ölçümü **kendine uygulamamıştır**.

---

## 4. Ne değişiyor

**Brifing kontrol listesi — bugün uygulanabilir:**

1. **Erişim haritasını brifinge yaz, ama HİPOTEZ olarak işaretle.** Ajana onu ölçüp düzeltme yetkisi ver. Bu koşumda benim brifingim yanlıştı (*"arXiv HTML açık"* dedim, denenmemişti) ve **ajan ölçüp düzeltti**. → `§5 B1`
2. **Kapalı kaynak taktiğini brifinge koy:** replikasyon deposu → upstream git → kaynak `.md`. → `B2`
3. **WebSearch'ü tayınla ve sessiz tükenişi ajana SÖYLE.** Boş arama, sonucun yok olduğu anlamına gelmez; **sayacın dolduğu** anlamına gelir. → `B3`
4. **Bağlam bütçesi = etkin uzunluk.** Distractor yoğun işte 2K–16K varsay. → `B4`
5. **"Bulunamadı" ile "aranamadı"yı ayırmak ZORUNLU madde.** → `B7`
6. **"Doğrulayamadığın rakamı verme" ZORUNLU madde.** → `B8`
7. **İskelet önce:** ilk bulguda kısa ara metin. → `B9`
8. **Persona/rol atamayı gerekçesiz kullanma.** → `B10`
9. **Katı format zorunluluğunun maliyetini kabul et ve ölç.** → `B11`
10. **`[D/K/X]` etiketlemesinin gerekçesini düzelt** — *"halüsinasyonu azaltır"* değil, *"kanıt seviyesini açık kılar"*. → `B12`
11. **Yargıç, üreticiyle aynı aileden olmasın**; mümkün değilse confound'u raporda yaz. → `B13`
12. **Kanarya maddesi koy** — cevabını bildiğin 1-2 soru. → `B14`
13. **Süreç metriklerini logla, hüküm kurma.** → `B15`

**KARAR GEREKİYOR (S2) — V73 `⊨A` "aranamadı" etiketi.** Bu, oturumun **en çok bağımsız gerekçe biriktiren** önerisidir: dört ayrı yerden geldi — üç ajanın elle yaptığı ayrım, K19, K20, ve lojik-kod ailesinin kendi dürüstlük kaydı. → `§7 V73`

**Diğer kutu adayları:** brifing = hipotez (V72) · etkin uzunluk tablosu kanona (V74) · MAST'ın 14 başarısızlık modu brifing kontrol listesi olarak (V75). → `§7`

---

## 5. Kontrol

*Bu raporu okuduktan sonra şu üç soruyu cevaplayabiliyor musun?*

1. **Bir ajan "bu konuda kaynak bulunamadı" dedi. Bu cümlenin iki farklı anlamı var — hangileri, ve hangisinin doğru olduğunu nasıl anlarsın?**

2. **Çok-ajanlı bir koşum başarısız oldu. Ölçülmüş veriye göre en olası sebep koordinasyon mu, kalite kontrol mü, yoksa başka bir şey mi — ve bu, brifing yazmaya ne kadar zaman ayırman gerektiği hakkında ne söylüyor?**

3. **Bir prompt karşılaştırmasında yargıcı 3 kez örnekledin ve 3/3 aynı sonuç çıktı. Bu seni hangi hata türüne karşı korur, hangisine karşı korumaz?**
