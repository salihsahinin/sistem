# Optimize Compiler Formülü — "AI→AI" raporundan "AI→insan" raporuna

> **Mod:** yan-oturum (m.41) · Kaynak: A13 ailesi (tez koşumu; **Aşama 2 antitez KOŞULMADI** — protokol eksiği, bölüm 8) + A8 (etiket granülerliği) + A15/K8 (yapı-aynalama) · Tetikleyen: Salih 07-26, "lojik bizim compiler kapımız olacak" + "optimize compiler oluşturma formülü"
> **Bu belge bir tasarım önerisidir, kanon değildir.** Kanon değişikliği Katman 1 (m.31).

---

## 0. Problem tanımı

Carvis lojik-yoğun raporlar üretiyor: her iddiaya URL, kanıt etiketi, çelişki bayrağı, daraltma kaydı. Salih okuyor ama yorucu. İstenen: aynı raporu günlük dile çeviren ikinci bir katman — her "AI→AI" rapor için bir "AI→insan" muadili.

**Bu belgenin tezi:** çeviri katmanı kurulabilir, ama **naif kurulursa tam olarak en değerli sinyali yok eder.** Aşağıdaki formül, ölçülmüş kayıp modlarının her birine bir karşı-tedbir bağlar.

---

## 1. Neyin bozulduğu — ölçüm

Formülün her maddesi bir bulguya bağlı. Önce bulgular:

| # | Ölçüm | Sayı | Etiket |
|---|---|---|---|
| B1 | **Kayıp, uydurma değil muğlaklaşmadır.** 104 LLM-sadeleştirilmiş özet, 1.000 dilbilimci-küratörlü kayıp örneği | Özet başına **9,62 kayıp**; **%74,1 kavram-muğlaklaşması**, %25,9 düz silme | D (ham veri sayıldı) |
| B2 | **Silme, insan referanslarında bile baskın** | İnsan eliyle yazılmış sadeleştirmelerde silme hatası **%84,1**; silme hataları ekleme/değiştirmenin **3-18 katı** | D (ham anotasyon) |
| B3 | **Epistemik güç değişiyor.** 563 basın-bülteni ↔ makale-özeti çifti | Güç korunmuş %61,3 · **şişirilmiş %21,7** · zayıflatılmış %17,1 → **%38,7'sinde değişiyor.** Korelasyon→nedensellik: **%38,7** | D (ham veri hesaplandı) |
| B4 | **Yanlılık ortalamada küçük, varyansta büyük** | Ortalama işaretli kayma **+0,085** | D |
| B5 | **"Sadık kal" talimatı işi KÖTÜLEŞTİRİYOR** | 10 LLM, 4.900 özet: aşırı-genelleme insan özetlerine göre **OR 4,85**; doğruluk-promptu bazı modellerde genellemeyi **~2 kat artırdı**; yeni modeller eskilerden **daha kötü** | K |
| B6 | **Negatif kutup ~7 kat daha oynak** | Varyasyon katsayısı: negatif terimler **0,97** ↔ pozitif **0,14**; uçlarda **~30 kat**. Okurların **%9'u** en az bir negatif terimi >%50 okuyor (kutup tersine dönüyor) | D (ham CSV hesaplandı) |
| B7 | **Standart terimler bile kaçıyor** | 9 standart terim × 46 okur = 414 okuma; **%27,1'i standardın kendi bandının dışında**. "Probable" ile "Likely" ayırt edilemiyor | D (hesaplandı) |
| B8 | **Soyutlama derecesi ↔ sadakat: doz-yanıt** | Çıkarımcıya yakın yeniden yazımda kaynakta-olmayan içerik **%16,6**; agresif soyutlamada **%52,9 → 3,2 kat**. Tamamen temiz özet oranı %58,6 → **%7,8** | D (ham anotasyon) |
| B9 | **Olgun bir iki-sürüm rejiminde bile güven bilgisi geçmiyor** | 1.738 laik özet denetlendi: **hiçbiri tam uyumlu değil**; kanıt kesinliğini belirtme maddesinde uyum **%0,7** | K |
| B10 | **Sürüm↔sürüm tutarlılık doğrulaması çözülmüş değil** | İkili "tutarlı mı" sorusunda tavan **~%74 dengeli doğruluk**; en iyi metrik insan yargısıyla **Spearman ~0,59** | D |
| B11 | **Sadeleştirme kavramayı çoğu zaman artırmıyor** | 9 sınıf düzeyi sadeleştirme: tercih %62↔%38, "kolay" %97↔%75, ama **kavrama %58↔%56 (fark yok)** | K |
| B12 | **Uzmanlık tersine dönmesi** | Düşük ve yüksek ön-bilgi grupları arasındaki fark **d = 0,971** [0,631–1,312]; basitleştirilmiş sunum uzmanda **kayıp** | K |
| B13 | **Okunabilirlik skoru oynanabilir** | FKGL "dramatik biçimde iyileştirilmek üzere kolayca manipüle edilebilir"; 8 metrik insan yargısıyla zayıf korele, en iyi yargıç **r = 0,56** | D |
| B14 | **Geri-bağlama, tam da soyutlamada çöküyor** | Atıf metrikleri "atfedilebilir soyutlayıcı yanıtları atfedilemez olanlardan güvenilir ayırt edemiyor"; kaynak uzadıkça kötüleşiyor | D |
| B15 | **Akıcılık tuzağı — ve tersi** | Akıcı sunulan ifade daha "doğru" değerlendiriliyor; **AMA** kolay sindirilir açıklamalar aşırı-güveni **azaltıyor** (5 çalışma, N=731) çünkü doğrulama maliyetini düşürüyor | K [X] |

**B15'in çelişkisi çözülmeden formül kurulamaz.** Ayrım şu olmalı (Carvis yorumu, ölçülmemiş `[?]`): **akıcı İDDİA** inandırıcılığı haksız yere artırır; **akıcı GEREKÇE** doğrulamayı ucuzlatır ve aşırı-güveni azaltır. Formül bu ikisini ters yönde ele alır (F6).

---

## 2. FORMÜL — dokuz kural

### F1. Niteleyici, yeniden yazılan metnin DIŞINDA taşınır

**Gerekçe:** B1 (kaybın %74'ü muğlaklaşma), B9 (%0,7 uyum).

Akışa gömülen niteleyici sadeleştirme geçişinde erir — silinmez, **muğlaklaşır**, ve bu fark edilmez. Çözüm: niteleyiciyi **yapısal yuvaya** koymak.

**Yanlış (niteleyici cümle içinde):**
> Kalite kontrolü üretim anında yapılmalı, çünkü artık etki tamamen silinemiyor — gerçi azaltılabiliyor, o yüzden bu mutlak bir kural değil, maliyet argümanı.

**Doğru (niteleyici ayrı yuvada):**
> **İddia:** Kalite kontrolü ders üretilirken yapılmalı, sonrasında değil.
> **Kanıt ne diyor:** Yanlış öğrenilen bilgi düzeltmeyle azalıyor, sıfırlanmıyor.
> **Bu yüzden:** maliyet argümanı, mutlak kural değil.
> **Güven:** orta — dört derleme aynı yönde, birincil metne inilemedi.

**Kanonik dayanak:** ABD istihbarat topluluğunun zorunlu standardı aynı ilkeyi koyar — *"bir ürün, bir güven seviyesi ile bir olasılık derecesini AYNI CÜMLEDE birleştirmemelidir."* İki eksen ayrı yuvalarda taşınır (A8 §11.2).

**Uygulama:** "Güven" ve "Bu yüzden" alanları compiler'a **salt-okunur** verilir; sadeleştirici bu alanları yeniden yazmaz, **aynen taşır**. Alan boşsa çıktı üretilmez (sert kapı).

### F2. "Sadık kal" DEME — kısıtla

**Gerekçe:** B5.

"Orijinale sadık ol" talimatı aşırı-genellemeyi azaltmıyor, bazı modellerde **iki katına çıkarıyor**. Sadakat bir talimatla değil, **yapısal kısıtla** sağlanır:
- niteleyici alanları salt-okunur (F1),
- iddia sayısı sabit (teknik sürümde N iddia varsa insan sürümünde de N),
- yeni iddia ekleme yasağı makine tarafından denetlenir (F7).

**Ek tedbir (kaynağın önerisi):** düşük sıcaklık + **dolaylı, geçmiş zaman kipiyle** raporlama ("ölçüldü", "bulundu") — çünkü şimdiki zaman genelleme davetiyesidir.

### F3. Negatif kutup ve düşük güven, SAYIYLA çapalanır

**Gerekçe:** B6 (negatif kutup ~7 kat oynak, okurların %9'u kutbu ters okuyor), B7 (%27,1 banttan kaçıyor).

Bu, formülün en yüksek getirili maddesi: **en çok korumak istediğin sinyal, çeviride en çok bozulan sinyal.**

Kural: negatif/düşük-güven ifadesi **asla yalnız kelimeyle** verilmez. Kelime + sayısal çapa, **aynı cümlede, parantezle**.

> ❌ "Bu bulgu şüpheli."
> ✅ "Bu bulgu şüpheli (üç kaynaktan ikisi çelişiyor, birincil metne inilemedi)."

**Neden parantez:** ölçülmüş — terimi cümle içinde parantezle sayısıyla vermek, tıklanabilir tablo veya tooltip'ten belirgin üstün. Okur tabloya gitmiyor.

**Pozitif kutupta bu zorunlu değil** (CV 0,14) — bütçe oraya harcanmaz. Asimetrik uygula.

### F4. Yeniden yazım derinliği SINIRLIDIR

**Gerekçe:** B8 (doz-yanıt: %16,6 → %52,9, 3,2 kat).

Sadakat kaybı, soyutlama agresifliğiyle **doz-yanıt** ilişkisinde. Yani "ne kadar sadeleştireyim" bir üslup tercihi değil, **doğrudan hata oranı ayarı**.

Kural: compiler **cümle-seviyesinde yeniden ifade** eder, **paragraf-seviyesinde yeniden yapılandırmaz**. Bir teknik paragraf → bir insan paragrafı. Birden çok bulguyu tek cümlede birleştirmek yasak (birleştirme, muğlaklaşmanın ana üretim yolu).

### F5. Kaynağın YAPISINI aynalama — ama iddia sırasını KORU

Burada iki kural çakışıyor ve ayrım netleştirilmeli:

- **A15/K8 (hukuki):** kaynağın yapısını cümle cümle aynalamak ihlal riski üretir — bu **dış kaynaklar** için geçerlidir.
- **Bu compiler için:** kaynak **kendi teknik raporumuz**. Orada tersi doğru: iddia sırası korunmalı, çünkü geri-bağlama (F7) buna dayanıyor.

Kural: **dış kaynaktan alıntıda yapı aynalanmaz; kendi teknik raporumuzdan çeviride iddia sırası birebir korunur.**

### F6. Akıcılığı GEREKÇEYE ver, İDDİAYA verme

**Gerekçe:** B15'in iki yüzü.

- **İddia cümlesi:** akıcılaştırılmaz, güçlendirilmez, kesinleştirilmez. Teknik sürümdeki kesinlik seviyesi neyse o.
- **Gerekçe ve örnek:** olabildiğince akıcı, somut, günlük dilde. Doğrulama maliyetini düşürmek buradan gelir.

Pratik test: insan sürümündeki bir iddia, teknik sürümdekinden **daha kesin geliyorsa** hata var.

### F7. Geri-bağlama zorunlu, ve tek yönlü değil

**Gerekçe:** B14 (atıf doğrulaması tam da soyutlamada çöküyor), B10 (tutarlılık doğrulaması tavanı ~%74).

Her insan-sürümü iddiası, teknik sürümdeki **kaynak bölüme çapa** taşır (`→ §7.2`). Bu üç işi birden yapar:
1. Okur derinleşmek istediğinde yol bulur.
2. Otomatik tutarlılık denetimi mümkün olur (iddia sayısı, sıra, çapa bütünlüğü — bunlar **deterministik**, LLM yargısı gerektirmez).
3. F2'nin "yeni iddia ekleme yasağı" denetlenebilir hale gelir: çapasız cümle = yeni iddia = hata.

**Katman-1 kuralı:** karar Katman-1 sınıfındaysa (kanon, para, dışarı çıkacak iş), insan sürümü okuru teknik sürümdeki şerhe **açıkça yönlendirir**. Tek yönlü çeviri değil, **geri-bağlantılı** çeviri.

### F8. Compiler, uzmanlaştığın konuda KAPANIR

**Gerekçe:** B12 (d = 0,971), B11 (kavrama farkı yok).

Sadeleştirmenin kazancı **acemi okura** özeldir ve okur seviyesine göre **işaret değiştirir**. Salih P1/P3/P5/P6'yı tamamladığı konularda (token ekonomisi, RoPE, context engineering) insan sürümü **net zarardır** — hem vakit hem hassasiyet kaybı.

Kural: compiler, öğrenen-durumu dosyasındaki seviye kaydına bakar; konu `[T]` işaretliyse ve o partisyon DONE'sa **çalışmaz**. Bu, F1'in niteleyici alanlarının aynı dosyadan beslenmesiyle birleşir.

### F9. Başarı ölçütü okunabilirlik skoru DEĞİLDİR

**Gerekçe:** B13 (FKGL oynanabilir, insan yargısıyla zayıf korele), B11 (skor iyileşti, kavrama sabit).

Okunabilirlik metriğini optimize etmek **metrik oyunlamadır**. Ölçülecek şey:

| Ölçüt | Nasıl |
|---|---|
| **Kavrama deltası** | Salih insan sürümünü okuduktan sonra 3 soru: iddia neydi, niteleyici neydi, karar ne gerektiriyor |
| **Niteleyici korunma oranı** | Teknik sürümdeki niteleyici sayısı ÷ insan sürümüne geçen (deterministik sayım, F1 sayesinde mümkün) |
| **Kesinlik kayması** | İnsan sürümündeki iddia, teknik sürümdekinden daha mı kesin? (F6 testi) |
| **Çapa bütünlüğü** | Çapasız cümle sayısı (0 olmalı) |

**Doğrulayıcının kendi tavanı beyan edilir:** sürüm↔sürüm otomatik tutarlılık denetiminin tavanı ~%74; bu, çıktının altına yazılır (A15/K33 deseni).

---

## 3. Formülün özeti — tek tablo

| Kural | Neye karşı | Sert/Yumuşak |
|---|---|---|
| F1 Niteleyici ayrı yuvada, salt-okunur | muğlaklaşma (%74 kayıp) | **Sert** — alan boşsa üretim yok |
| F2 "Sadık kal" deme, yapısal kısıtla | doğruluk-promptunun ters tepmesi (~2×) | **Sert** |
| F3 Negatif/düşük güven sayıyla çapalanır, aynı cümlede | negatif kutup 7× oynaklık | **Sert** |
| F4 Cümle-seviyesi yeniden ifade, paragraf birleştirme yasak | doz-yanıt (3,2×) | **Sert** |
| F5 Dış kaynakta yapı aynalanmaz; kendi raporumuzda sıra korunur | hukuki risk ∧ geri-bağlama | **Sert** |
| F6 Akıcılık gerekçeye, iddiaya değil | akıcılık tuzağı | Yumuşak (insan testi) |
| F7 Çapa zorunlu; Katman-1'de şerhe yönlendir | atıf çöküşü, tutarlılık tavanı | **Sert** |
| F8 Uzmanlaştığın konuda kapan | uzmanlık tersine dönmesi (d≈0,97) | Yumuşak (Salih iptal edebilir) |
| F9 Skoru değil kavramayı ölç | metrik oyunlama | **Sert** |

---

## 4. Mimari — kim üretir, kim doğrular

> **Damga düzeltmesi (K2-g, Salih imzası 2026-08-03; kaynak: rapor 08-02-1 S4 + hakem Ç3):** bu bölümün hibrit deseni (üretici LLM ≠ deterministik doğrulayıcı) **"tasarım kıyasında kazanmış AMA bu depoda koşulmamış hipotez"** statüsündedir. Genellemesi koşullu: deterministik denetçi ancak hedef dil formal/karar-verilebilir sözdizim taşıdığında bedava gelir — bugünkü depoda formal-hedefli kenar BOŞ. Önceki metnin "kanıtlanmış desen" tınısı iç-çelişkiydi, bu şerhle düzeltildi.

**Üretici ≠ doğrulayıcı** (A4 §7.2, A7 §10.6: modeller kendi işlerini notlandırırken sistematik iyimser sapıyor).

```
teknik rapor (kaynak, değişmez)
      │
      ├──► [compiler ajanı]  — farklı model (A10 §13.4: heterojenlik kalite kazandırıyor)
      │        F1-F8 kısıtları altında üretir
      │
      └──► [denetleyici]     — LLM DEĞİL, deterministik betik
               · çapa bütünlüğü (çapasız cümle var mı)
               · iddia sayısı eşleşmesi
               · niteleyici alanı doluluk
               · negatif terim → sayısal çapa var mı
               · yeni iddia tespiti
                     │
                     └──► ihlal varsa üretim REDDEDİLİR
```

**Kritik tasarım tercihi:** denetleyici katmanının çoğu **LLM gerektirmiyor**. Çapa sayma, alan doluluk kontrolü, terim taraması — hepsi düz betik. LLM yargısı yalnız "kesinlik kayması" testinde gerekir, ve orada da tavanı (~%74) beyan edilir. Bu, A15/K32'nin "politika kod olarak" ilkesiyle aynı.

---

## 5. Şablon — insan sürümü blok yapısı

```markdown
## <Başlık — soru formunda, günlük dilde>

<Bağlam: 1-2 cümle, neden bu konuşuluyor>

**Ne bulduk.** <İddia. Teknik sürümdeki kesinlik seviyesiyle. Akıcılaştırma YOK.>  → §<çapa>

**Neye dayanıyor.** <Gerekçe. Burada akıcı ol, somut ol, örnek ver.>

**Ne kadar güveniyoruz.** <Niteleyici. SALT-OKUNUR ALAN — compiler bunu yeniden yazmaz.
Negatifse sayısal çapa zorunlu.>

**Ne yapmamız gerekiyor.** <Karar/eylem. Katman-1 ise: "detay ve şerhler §<çapa>">
```

---

## 6. Bu formülün kendi sınırı

1. **A13'ün antitezi koşulmadı.** Yukarıdaki bulguların hiçbiri adversaryal sınamadan geçmedi. En kırılgan üç yer: B5 ("sadık kal" ters tepiyor — tek çalışma), B15'in çelişkisi (çözülmedi, Carvis yorumuyla ayrıştırıldı), B6'nın örneklemi (n=46, kendi-seçilimli, hakemli değil — **gösterge, popülasyon tahmini değil**).
2. **B8'in mutlak oranları eski model dönemine ait** (2020-21). Taşınabilir olan **doz-yanıt ilişkisinin yönü**, mutlak oran değil.
3. **Sürüm↔sürüm doğrulaması literatürde boş.** Bulunan her şey her sürümü ayrı ayrı *kaynağa* karşı denetliyor; sürüm↔sürüm tutarlılık doğrulaması **mimari boşluk** — F7'nin deterministik kısmı bu boşluğu kapatmak için tasarlandı ve **özgün katkı alanıdır**.
4. **Formül test edilmedi.** F9'un ölçütleriyle ilk koşum yapılmadan bu bir hipotezdir.

---

## 7. İlk koşum önerisi (eval)

A7 §10.7 deseni: kapsamlı dokümantasyondan ÖNCE değerlendirme.

1. **Baseline:** `2026-07-26-INSAN-pasif-ogrenme.md` — F1-F9 **uygulanmadan** yazıldı. Bilinen ihlalleri: F1 (niteleyici akışa gömülü, en az 1 kayıp tespit edildi), F7 (çapa yok).
2. **V2:** aynı içerik, formülle yeniden üretilir.
3. **Ölçüm:** F9'un dört ölçütü + Salih'in kavrama deltası.
4. **Karar:** eşleştirilmiş kıyas; **tek koşumdan sonuç çıkarılmaz** (A7 §10.7: küçük-N'de gerçek standart hata naif olanın 3 katından fazla olabiliyor).

---

## 8. Açık borçlar

1. **A13 antitez koşumu** — protokol borcu (m.40b üç aşama zorunlu).
2. **B6'nın hakemli muadili** — n=46 Reddit örneklemi yerine hakemli bir belirsizlik-terimi çalışması.
3. **GRADE etiketlerinin okur tarafından yanlış yorumlanma oranı** — arandı, bulunamadı, arama bütçesi bitti. Bizim D/K/X'in muadili olurdu.
4. **Sürüm↔sürüm tutarlılık doğrulayıcısı** — literatürde yok; kurulacaksa kendi işimiz.
5. **F8'in tetiği:** öğrenen-durumu dosyası henüz yok (Model B'nin çıktısı olacak, §16 ana rapor).
