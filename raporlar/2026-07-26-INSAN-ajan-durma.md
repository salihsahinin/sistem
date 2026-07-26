# Ajanlar Neden Duruyor — insan yüzü

> Kaynak: `raporlar/2026-07-26-ajan-durma-atlas.md` · Register: kavrayış · Compiler: **AÇIK** (F1-F9)
> **UYARI: Bu dosya karar kaynağı DEĞİLDİR.** Katman-1 kararı teknik kayıttan alınır. Burada okuduğun her maddenin sonunda kaynak bölüm numarası var — karar vereceksen oraya git.

---

## 1. Tek cümlede

Ajanların **"stopped" olmadı** — `failed` oldular, `failed` **terminal bir durum değildi**, ve asıl sebep ajanlarda değil **onları nasıl koştuğumdaydı**: 112 ajanlık bir dalga, belgelenmiş kapasitenin dışındaydı.

---

## 2. Ne bulduk

### ① Sorunun kendisi yanlış öncüle dayanıyordu

- **İddia:** Bu oturumda hiçbir ajan "stopped" olmadı. `Stopped` durumuna insan ya da dış müdahale sokar (`Ctrl+X`, `claude stop`, dışarıdan `kill`). Limit, hız limiti, tur sayısı ve asılma — hepsi **`Failed`** üretir.
- **Neye dayanıyor:** Kurulu CLI kaynağı + bu oturumun kendi 35 bildirimi: 22 `completed`, 13 `failed`, **0 `stopped`**.
- **Ne kadar güveniyoruz:** Yüksek — ölçüm kendi makinemizde, birincil kaynaktan. **Bir kenar-durum şerhi var:** makine kapanması da dışarıdan sonlandırmadır ama `Failed` üretir, yani *"yalnız şu üç yol"* çerçevesi orada çatlıyor.
- **Ne yapmamız gerekiyor:** `failed` gördüğünde **"öldü" diye okuma**. Bu kelimenin altında dört farklı şey saklı.
- → `ajan-durma §0`

**Analoji:** `Stopped` = birinin fişi çekmesi. `Failed` = "bir şey oldu" yazan tek bir kırmızı lamba — arkasında kota bitmesi de var, sunucu hatası da, ajanın kendi hatası da. Lamba tek, sebepler dört.

### ② ⭐ `failed` damgası ölüm ilanı değil

- **İddia:** Bir ajan limit yüzünden `failed` damgası aldıktan **sonra** çalışmaya devam edip raporunu bitirebilir.
- **Neye dayanıyor:** Ölçüm. Beş ajan 04:09–04:15 arasında `failed` bildirdi; limit 04:50'de kalktı; beşi de 05:08–05:12 arasında **20.274 ile 34.998 karakter arası** rapor üretip teslim etti.
- **Ne kadar güveniyoruz:** Mekanizmaya yüksek güven — beş bağımsız vakada gözlendi. **Ama sayıya değil:** ilk ölçüm *"3 rapordan 2'si kayıp"* demişti, tam oturum taraması bunu düzeltti. Mekanizma korunur, sayı düşer.
- **Ne yapmamız gerekiyor:** Limit kalktıktan sonra ajanı **yeniden başlatma** — `SendMessage` ile **sürdür**. Tam bağlamıyla kaldığı yerden devam eder.
- → `ajan-durma §2`

> ⚠️ **Bu maddede saklı olan asıl haber:** o beş rapor teslim edildi **çünkü elle müdahale ettim**. Müdahale olmasaydı diskte kalacaklardı. Yani *"bu oturumda veri kaybı yok"* cümlesi bir sistem özelliği değil, **bir müdahalenin sonucudur**.

### ③ ⭐ En pahalı bulgu: aramalar sessizce boşa dönüyor

- **İddia:** Bir oturumda en fazla 200 WebSearch yapılabilir; bu sayaç **ana konuşma ve tüm alt-ajanlar için ortaktır**; ve bittiğinde **hata vermez** — arama yapılır gibi görünür, boş döner.
- **Neye dayanıyor:** Ham dokümandan birebir alıntı. Antitez turu bunu ayrıca **doğruladı** ve *"tam örtüşüyor"* dedi.
- **Ne kadar güveniyoruz:** Çok yüksek — hem birincil kaynaktan, hem bağımsız bir sınamadan geçti. Sınamayı yapan ajanın kanıtı kendi belleği değil, dokümanın kendisiydi.
- **Ne yapmamız gerekiyor:** Görev emrine **URL koy**. URL varsa ajan WebSearch yerine WebFetch kullanır ve bütçeden hiç yemez.
- → `ajan-durma §7`

**Ve bunun bize maliyeti:** 112 ajan × ajan başına 2 arama = **224 arama**, tavan 200. Zarf zaten aşılmıştı. Yani **A8, A12 ve A18 ailelerinin "bulunamadı" dediği yerde doğru cevap büyük olasılıkla "aranamadı"ydı.** Bu ayrım bu raporun en önemli tek cümlesi olabilir.

### ④ 112 ajanlık koşum zaten kapasitenin dışındaydı

- **İddia:** Sağlıklı dalga zarfı şudur: 10 ajan, Sonnet, orta effort, 2-3 saniye aralıklı başlatma, ajan başına en fazla 2 arama, oturum toplamı 60-80 ajan.
- **Neye dayanıyor:** Belgelenmiş limitler + gözlenen koşumun kendi verisi.
- **Ne kadar güveniyoruz:** Zarfın **sayısına** orta-yüksek güven; **gerekçesi düzeltildi.** Önce *"sert sınır 10'dur"* denmişti — antitez bunu çürüttü: aslında üç ayrı mekanizma var (alt-ajan eşzamanlılığı 20, yürütme kapısı 10, "10 oturum ≈ 10× kota" ise sınır değil tüketim kuralı). **Sayı ayakta, sebebi değişti.**
- **Ne yapmamız gerekiyor:** Dalgayı 10'da tut. 112'lik koşum 200'lük oturum tavanının yarısını tek seferde yedi.
- → `ajan-durma §8` · `§9`

**Yani:** %22'lik limit-sonlanması bir anomali değil, **beklenen sonuçtu**. Sorun ajanlarda değildi.

### ⑤ Effort ayarı en büyük tek token kalemi

- **İddia:** Varsayılan effort `high`'tır ve düşünme token'ları **çıktı olarak** faturalanır. Getirme ajanlarına düşük, sentez ajanına yüksek verilmelidir.
- **Neye dayanıyor:** Birincil kaynak + 112 ajanlık koşumun kendi maliyet dağılımı.
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** Ajan açarken effort'u **bilinçli seç**. Varsayılana bırakmak, en pahalı seçeneği seçmektir.
- → `ajan-durma §9`

### ⑥ "Ucuz model" tavsiyesi aslında bir kova ayırma hamlesiymiş

- **İddia:** Opus'un ve Sonnet'in **ayrı token kovaları** var. İşçiler Sonnet'e alınırsa işçi trafiği Opus kovasından hiç yemez.
- **Neye dayanıyor:** Birincil kaynak.
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** V59 tavsiyesinin gerekçesini güncelle — bu bir **tasarruf** değil, aynı kotayla **iki paralel havuz** açma hamlesidir.
- → `ajan-durma §9`

### ⑦ Ajan hiç metin yazmadan ölürse her şey kaybolur

- **İddia:** Kesilen ajan **metin üretmişse** kısmi çıktı geri döner. **Yalnız araç çağrısı yapmışsa** her şey kaybolur.
- **Neye dayanıyor:** Birincil kaynak (mekanizma) + 115 transkriptin taraması (ağırlık).
- **Ne kadar güveniyoruz:** Mekanizmaya yüksek. **Ağırlığına düşük:** bu şekilde ölüm 115 vakanın 6'sında görüldü, yani **%5** — hipotezin öngördüğünden az. Yani gerçek bir tuzak, ama en büyük tuzak değil.
- **Ne yapmamız gerekiyor:** Ajan promptuna *"ilk bulguyu bulur bulmaz kısa bir ara metin yaz"* koy. Maliyeti sıfır, kayıp modunu *"her şey gitti"*den *"kısmi döndü"*ye çevirir.
- → `ajan-durma §5` · `§11 U2`

### ⑧ Git zaten tek gerçek kontrol noktası

- **İddia:** `/rewind` checkpoint'leri bash ile değiştirilen dosyaları izlemez ve alt-ajan düzenlemelerini geri almaz. Dokümanın kendi ifadesi: *"checkpoint = yerel geri al, Git = kalıcı tarihçe."*
- **Neye dayanıyor:** Birincil kaynak; antitez turu bunu **doğruladı**.
- **Ne kadar güveniyoruz:** Çok yüksek.
- **Ne yapmamız gerekiyor:** Hiçbir şey — **m.10 bu boşluğu zaten kapatıyor.** Kanon bu noktada dokümandan önce doğruydu.
- → `ajan-durma §10`

### ⑨ ⛔ Bir tavsiyeyi geri çekiyorum

- **İddia (geri çekildi):** *"Explore ve Plan ajanları sürdürülemez, uzun işlerde kullanma."*
- **Neye dayanıyor:** **Hiçbir şeye.** Bu, bir alt-ajanın aktardığı bir iddiaydı; ben doğrulamadan *"çok yüksek değer, sıfır maliyet"* etiketiyle **tavsiye listesinin başına** koydum. Antitez dokümanı okudu ve bu istisnaya dair **hiçbir kayıt bulamadı**.
- **Ne kadar güveniyoruz:** **Güvenmiyoruz — askıda.** Yanlış olduğu için değil, **dayanağı gösterilemediği için**. Doğru da çıkabilir.
- **Ne yapmamız gerekiyor:** Doğrulama ucuz: bir `Explore` ajanı aç, dönen nesnede agent ID var mı bak. **Doğrulanana kadar bu bir kural değildir.**
- → `ajan-durma §10` · `§11 U1`

> **Bu maddenin dersi maddenin kendisinden değerli:** listenin başı, **en az doğrulanmış** maddenin yeri değildir. Bir tavsiye ne kadar yukarıdaysa, dayanağı o kadar sağlam olmalı.

### ⑩ ⭐ Taksonomide olmayan bir ölüm biçimi ölçüldü

- **İddia:** Bir ajan işini bitirip durabiliyor ve **hiçbir bildirim göndermeden** ölü kalabiliyor — ne `completed`, ne `failed`, ne `stopped`.
- **Neye dayanıyor:** Canlı ölçüm. Üç ajan 15:10–15:11 arasında son satırını yazdı; **45 dakika** boyunca dosya boyutu, satır sayısı ve değişiklik zamanı **birebir sabit** kaldı. Dürtülünce üçü de **29-34 saniyede tam raporla** döndü.
- **Ne kadar güveniyoruz:** Yüksek — üç bağımsız vaka, ölçülmüş dosya verisiyle.
- **Ne yapmamız gerekiyor:** Uzun koşumlarda **bildirim bekleme**. Transkriptin değişiklik zamanına iki kez bak; büyüme yoksa dürt.
- → `ajan-durma §3.1`

> **Ve teşhis dürtme sonrası değişti — asıl haber bu.** Ajanlar asılmamıştı; **işlerini bitirmişlerdi ama teslim edememişlerdi.** Biri aynen şöyle dedi: *"Donmuş değilim — önceki turda tam sonucu ürettim ve döndürdüm."*
>
> Fark pratik: asılmış bir ajanı sürdürmek işi **yaptırır** (tam maliyet). Teslim edememiş bir ajanı sürdürmek işi yalnız **taşır** (30 saniye). **Kural: beklenenden uzun sürdüyse önce dürt, sonra endişelen.**

### ⑪ Beklediğimiz otomatik koruma yok

- **İddia:** Asılma nöbetçisi (`stall watchdog`) kurulu sürümde **yok**.
- **Neye dayanıyor:** İki bağımsız ölçüm. Birincisi: kurulu `cli.js` içinde `watchdog`, `idleAgent`, `stuckDetection`, `hungTask`, `healthCheck` terimlerinin **hiçbiri** bulunamadı. İkincisi: yukarıdaki üç ajan **45 dakika** sessiz kaldı ve belgelenmiş **10 dakikalık** eşiğe rağmen durdurulmadılar.
- **Ne kadar güveniyoruz:** Yüksek. Rapor önce *"bu makinede geçerli olmayabilir"* demişti; **artık ölçüldü — geçerli değil.**
- **Ne yapmamız gerekiyor:** Asılma tespitini **kendimiz** yapacağız. Bu bir borcun kapanmasıdır, ama **olumsuz yönde**: beklenen koruma yok.
- → `ajan-durma §14 C2`

### ⑫ Antitez turunun kendisi hakkında

Bu ailenin iddiaları bağımsız bir sınamadan geçti ve sınama **araç kullandı** — ham dokümanları çekti, kurulu kodu okudu. Sonuç: **4 gerçek hata** (⑨ ve yukarıdaki ③-④'ün gerekçeleri dahil) ve 5 daraltma.

**Bunun anlamı iki yönlü.** Bir yandan: bu aile oturumun **en güçlü kanıt tabanına** sahipti — ve yine de dört hata çıktı. Öte yandan: sınamanın *"burada çelişki yok"* diyebildiği yerler de oldu, yani sınama evet-adamı değildi.

- → `antitez-hakemlik §5` · `§9`

---

## 3. Ne bulamadık

**Bu bölümde iki farklı şey var ve karıştırılmamalı.** Birincisi *aradık, yoktu*. İkincisi *arayamadık*. İkincisini birincisi gibi okumak, bu raporun üretebileceği en pahalı hatadır.

### Aradık, bulamadık

| Ne | Not |
|---|---|
| Pro/Max abonelikleri için **sayısal kota tahsisatı** | Hiçbir açık dokümanda yok. Dokümanlar bilinçli olarak **pencere yapısını** yayımlıyor, **büyüklüğünü** değil. Yani bu bir eksik değil, bir tercih. |
| **Explore/Plan sürdürülemezliğinin dayanağı** | Antitez `sub-agents.md`'yi okudu ve bulamadı. Tutulan tek istisna, bu ajanların CLAUDE.md ve git-status yüklememesi. |
| `blocking_limit` ve `rapid_refill_breaker` tanımları | SDK enum'unda yalnız **değer olarak** geçiyorlar. Kota koruma mekanizması oldukları bizim **tahminimiz**, doküman değil. |
| Oturum penceresinin **token mi mesaj mı** saydığı | Yüzde veriliyor, paydası tanımsız. Token ağırlıklı olması kuvvetle muhtemel — ama bu da tahmin. |
| Alt-ajan token'ının ana oturumla **aynı katsayıyla** sayılıp sayılmadığı | *"Aynı kotadan yer"* belgeli; katsayı belirtilmemiş. |

### **Arayamadık** — bu bir yokluk hükmü DEĞİLDİR

| Ne | Neden arayamadık |
|---|---|
| API token-bucket'ının iç mekaniği, ITPM kovalarının sayısal tahsisatı, Batch ayrıntıları | `platform.claude.com` **erişim listesinde değildi**. Ne doğrulandı ne çürütüldü. |
| Temporal / durable execution teorisinin bir kısmı | Birincil kaynaklar kapalıydı, kapsam dışı bırakıldı. |
| HTTP `Idempotency-Key` standardının semantiği (anahtar ömrü, çakışma, 409) | IETF taslağına **erişilemedi**. Kavramın kendisi başka kaynaktan karşılandı, ama standart başlık davranışı doğrulanamadı. |
| *Designing Data-Intensive Applications* içeriği | Kitap **ücretli**; bu koşumda içeriği doğrulanamadı. Bölüm eşlemesi verilseydi **tahmin** olurdu. |

### Gözlemedik (üçüncü kategori)

429 hatasının canlı imzası bu oturumda **hiç görülmedi** — 115 transkriptteki 17 terminal API hatasının **17'si de oturum limitiydi**. 429'un aynı imzayı taşıyıp taşımadığı ampirik olarak doğrulanmadı; aynı kod yolundan geçtikleri için aynı olması **beklenir**, ama bu bir beklenti, ölçüm değil.

### Ve bir borç kapandı — olumsuz yönde

Asılma nöbetçisinin bu sürümde olup olmadığı **açık bir soruydu**; artık kapalı: **yok**. Bu, listeden bir madde silmek değil, **bir güvencenin kaybıdır** (⑪).

---

## 4. Ne değişiyor

Salih'in fiilen yapacağı ya da karar vereceği şeyler:

1. **Görev emirlerine URL koy.** Tek satırlık değişiklik, en yüksek getirili madde. Arama bütçesini korur ve *"bulunamadı"* raporlarının sahtesini keser. → `§7`
2. **Dalga 10 ajanla sınırlı.** 112'lik koşum tekrarlanmayacak. → `§9`
3. **Effort'u ajan başına seç.** Getirme ajanı düşük, sentez ajanı yüksek. Varsayılan `high` en pahalı seçenektir. → `§9`
4. **`failed` gören ajanı yeniden başlatma, sürdür.** `SendMessage`, tam bağlamı korur. → `§2` · `§10`
4b. **Bildirim gelmiyorsa bekleme — dürt.** Transkriptin değişiklik zamanına 45 saniye arayla iki kez bak; büyüme yoksa `SendMessage` gönder. 30 saniyelik maliyet, saatlerce boş beklemeyi önler. → `§3.1` · `§4 Adım 0.5`
5. **Ajan şablonuna "önce kısa ara metin" maddesi.** Maliyeti sıfır. → `§11 U2`
6. **KARAR GEREKİYOR — V71 geri çekildi.** *"Explore/Plan yasağı"* fikri kutudan çıkarıldı. Yerine önerilen: bir doğrulama koşumu (5 dakika) ve sonucuna göre yeniden değerlendirme. → `§10` · `§15`
7. **KARAR GEREKİYOR — iki kural adayı.**
   - **V82** (numarayı hakemlik kaydı verdi): *"Uzun koşumlarda bildirim beklenmez; transkript büyümesi periyodik örneklenir."* Maliyeti iki `stat` çağrısı. → `§15`
   - **Numarasız aday** (Salih atar): *"Bir tavsiye listenin başındaysa, dayanağı bağımsız doğrulanmış olmalı."* Bunun artık **üç** vakası var: ⑨ (Explore/Plan), *"eksen başına 4 kategori"*, ve *"ajan yayımlama eşiğini kendi geçemez"*. Üçü de doğrulanmadan öne çıkarıldı, üçü de düştü. → `§15`
7b. **⚠️ AYRI UYARI — bir güvenlik varsayımı düştü.** *"Ajan yayımlama eşiğini kendi başına geçemez"* iddiası `routines.md` ile çürütüldü: **onaysız push ve PR mümkün.** JARVIS'te `git push` zaten settings-deny ile **yapısal olarak** kilitli, yani oradaki koruma ayakta. Ama bu varsayıma dayanıp **korumasız bırakılmış** bir yüzey varsa açıktır. → `antitez §9c.2 K39`
8. **Öğrenme sırası hazır (L16-L22):** teslim garantileri → idempotency → write-ahead log → retry/heartbeat → durable execution → Continue-As-New/Saga. Hepsi ücretsiz birincil kaynaktan, toplam yaklaşık 3 saat. → `§12`

**Ve yapılmayacaklar** (bu da bir karardır): Temporal kurmak, kendi write-ahead log'unu yazmak, Saga altyapısı kurmak, `/loop` ile limit-sonrası otomatik yeniden deneme. Dördü de tek kişilik bir sistemde aşırı mühendisliktir; kavramları alınır, çalışan sistemleri alınmaz. → `§11 U12-U15`

---

## 5. Kontrol

*Bu raporu okuduktan sonra şu üç soruyu cevaplayabiliyor musun?*

1. **Bir ajanın bildiriminde `failed` gördün. İlk yapacağın şey ne, ve neden "yeniden başlat" değil?**

2. **Bir araştırma ajanı "bu konuda kaynak bulunamadı" dedi. Bu cümleye inanmadan önce hangi tek şeyi kontrol etmen gerekir — ve neden hata mesajına bakmak işe yaramaz?**

3. **Bu raporda bir tavsiye geri çekildi. Geri çekilme sebebi "iddia yanlış çıktı" değildi — neydi, ve bu ayrım neden önemli?**

4. *(Ek — ⑩'dan)* **Bir ajan beklediğinden uzun sürdü ve hiç bildirim gelmedi. "Hâlâ çalışıyor" demeden önce hangi iki ölçümü alırsın, ve dürtmenin maliyeti neden endişelenmenin maliyetinden düşük?**
