# Şerit 5 — Staj Hazırlığı (Otonet/Otoplus, başlangıç 11 Ağustos 2026)

> **Mod:** yan-oturum (m.41) — hazırlık malzemesi. **Nihai planlama PC ana oturumunda** (Salih beyanı 07-24).
> **Bugün:** 2026-07-24 · **Kalan: 18 gün**
> **Belirleyici bağlam (Salih, 07-24):** işyerinde **agentic coding** yapılıyor — ekip kendisi kod yazmıyor, ajanlara yazdırıyor. Görevlerin "okumayı öğrenme" biçiminde verilmesinin sebebi bu.
> **Şerit:** 7 aile açıldı, **6'sı rapor yazdı** (eksik: S5-A6, AWS'in inşa felsefesi).
> **Kaynak:** `scratchpad/S5-A{1,2,3,4,5,7}-seritA.md`

## 0. Kanıt kısıtı (önce oku)

Egress politikası akademik yayıncıların ve çoğu blogun tamamını 403'ledi; oturum ortasında WebSearch bütçesi de tükendi. Açık kalan verimli kanal `raw.githubusercontent.com` oldu.

Bunun somut sonucu: **S5-A5 (öğrenme yöntemi) raporunun tamamı [K]** — hiçbir birincil kaynağa inilemedi, tüm etki büyüklükleri arama özeti düzeyinde. S5-A3 (SQL) en sağlam olanı: PostgreSQL semantiği birincil dokümandan alınmış **ve** SQLite üzerinde fiilen koşulmuş. S5-A2 (AWS) fiyat rakamlarının hepsi ikincil — doğrulanmalı.

**Rakamlar yön göstergesi olarak kullanılmalı, sayı olarak alıntılanmamalı.** Plan yöne dayanıyor, rakama değil.

---

## 1. ★ İşin gerçek tanımı: sen doğrulama katmanısın

Agentic coding yapan bir ekipte kıt olan beceri kod yazmak değil. S5-A4'ün ölçtüğü altı LLM hata sınıfından **ikisini hiçbir araç yakalamıyor**:

| Hata sınıfı | Büyüklük | Kim yakalar |
|---|---|---|
| Uydurma paket/API | **%19,7** paket halüsinasyonu [D] | Import denemesi, lockfile |
| Eski/deprecated API | %25–38 [K] | Sürüm-farkındalıklı linter |
| Güvenlik açığı | %12–40 (çelişkili) [X] | Bandit/ruff-S, SAST |
| **Sessiz mantık hatası** | %66 "neredeyse doğru" [K] | **Yalnız insan okuması** |
| Atlanmış hata yolu | nitel [K] | Property testing |
| **Boş test tiyatrosu** | nitel [K] | **Yalnız insan okuması** (testi oku, kodu değil) |

Ve S5-A7'nin bulduğu resmi cümle bu rolü tam olarak adlandırıyor:

> *"Claude iş bitmiş göründüğünde durur. Çalıştırabileceği bir kontrol yoksa 'bitmiş görünüyor' elindeki tek sinyaldir ve **doğrulama döngüsü sen olursun: her hata senin fark etmeni bekler**."* [D]

**İşin bu.** Ve karşı-bulgu bunu daha da keskinleştiriyor: **AI yardımı okuma becerisini aşındırıyor** [S5-A4]. Yani ajanla çalışmak seni kendiliğinden iyi okuyucu yapmıyor — tersine, bilinçli pratik olmazsa kötüleştiriyor.

---

## 2. Planın temeli: "okuma" ne demek (S5-A5'in üç parçalı cevabı)

1. **Hedef okumaysa — EVET, risk yok.** Beceri hiyerarşisinde okuma yazmanın altındadır; öğretim teorisi "önce oku sonra yaz" der. 18 günde okuma yeterliliği hedeflemek kanıtla desteklenen bir karar.
2. **"Pasif okuma" kastediliyorsa — HAYIR, çok riskli.** *"En büyük risk beceriksizlik değil, ölçülmemiş sahte yeterliliktir — 11 Ağustos'ta 'hazırım' hissiyle gidip ilk gerçek sorguda donmak."*
3. **Sıfır üretim savunulamaz.** Yazma→okuma transferi kanıtlı; küçük üretim dozu okuma hedefine hizmet eder.

### → Okuma birimi = 5 adımlı çevrim (pazarlıksız)

1. **Tahmin yaz** — çalıştırmadan, cevaba bakmadan, ne yaptığını **yazılı** söyle
2. **Doğrula** — çalıştır / cevabı aç
3. **Farkı açıkla** — neden yanıldığını 1 cümleyle yaz
4. **Yanlışı kuyruğa at** — 2–3 gün sonra tekrar gelsin
5. **Üretim vergisi** — her 5 okunan artefakta 1 küçük değişiklik yaz

*Adım 1 ve 3 olmadan bu plan "düşük fayda" kutusuna düşer.*

---

## 3. ★ En yüksek getirili hazırlık kalemi (beklenmedik)

**İşe yarayan:** (1) terim/kelime dağarcığı — rol netliğini besler, en hızlı kazanılan boyut · (2) **hazırlanmış soru repertuarı** — *"yazılı 5 soru, 5 saatlik ekstra SQL çalışmasından daha yüksek beklenen getiriye sahiptir"* · (3) öz-yeterlik — planın DONE'ları bunu üretir.

**Boşa giden:** görev ustalığı avı (18 günde alınamaz) · kurumun özgül şemasını önceden öğrenmeye çalışmak (bilinemez) · yazma becerisine yatırım (format eşleşmiyor) · son 2 günde cramming.

> **Hedef:** advanced-beginner okuma yeterliliği + rol netliği + öz-yeterlik + hazır soru repertuarı.
> **Hedef değil:** görev ustalığı.

---

## 4. SQL çekirdeği (S5-A3 — bu şeridin en sağlam raporu)

### 4.1 Yedi sessiz katil

| # | Yapı | Neden sessiz |
|---|---|---|
| 1 | **LEFT JOIN + WHERE** | Sağ tablonun kolonuna `WHERE` koyunca dış birleştirme **sessizce INNER JOIN'e** döner — satırlar kaybolur, hata verilmez |
| 2 | **`NOT IN` + NULL** | Alt sorguda tek bir NULL varsa sonuç **HER ZAMAN boş** — "SQL'in en sessiz katili" |
| 3 | **NULL üç değerli mantık** | `NULL > 100` = *unknown*, ne doğru ne yanlış; filtre sessizce eler |
| 4 | **Fan-out** | Birden-çoğa birleştirme satırları çoğaltır; `SUM` bir anda yanlış rakam verir |
| 5 | **`COUNT(*)` ≠ `COUNT(kolon)`** | İkincisi NULL'ları saymaz |
| 6 | **GROUP BY / HAVING** | Granülerlik değişir, filtre sırası sonucu değiştirir |
| 7 | **Tarih / zaman dilimi** | Sınır dahil mi hariç mi; off-by-one — ajanın en klasik sessiz hatası |

### 4.2 Yazmadan doğrulama — beş teknik
- **`EXPLAIN`** = sorguyu çalıştırmadan bedava satır tahmini
- **"Kaç satır olmalı?" ön-tahmini** — okumadan önce yazılır
- **Granülerlik (grain) kontrolü** — tek en değerli test: *bu sorgunun bir satırı neyi temsil ediyor?*
- **Tekilleştirme/karşılaştırma testleri** — fan-out tespiti
- **Sağlama sorguları** — ajanın sorgusundan bağımsız, kendi yazdığın kontrol

### 4.3 Sınav tasarımı (P1 DONE'u)
15 sorgu · referanssız · ≤3 dk/sorgu. **Geçme ölçütü iki koşul birden:**
1. **13/15 doğru**, VE
2. **Sessiz-hata sınıfındaki 6 sorunun HEPSİ doğru.**

İkinci koşul sert olmalı: *"15'in 13'ünü bilip bu altısından birini kaçırmak, staj ortamında hata vermeden yanlış rakam raporlamak demektir. Toplam puanla telafi edilemez."*

**Dürüst sınır (ajanın kendi kaydı):** sınav tek bir 20 satırlık şemada ölçüyor; gerçek kurumsal şemadaki şema-bağlama zorluğunu (hataların %29-49'u) **temsil etmiyor**. Staj başladıktan sonra gerçek şemayla tekrarlanmalı.

**Sınav sonrası kalibrasyon:** yanlışları hata *sınıfına* göre grupla; iki soruda aynı sınıf yanlışsa o başlığı yeniden çalış — toplam puana bakma.

---

## 5. Python çekirdeği (S5-A4)

Onay öncesi kontrol listesinin veri işi için kritik maddeleri:

**Mekanik (30 sn):** her `import` lockfile'daki sürümde mi · her method çağrısını **tanıma, doğrula** · diff >400 satırsa bölmeden inceleme (**tespit oranı %65→%28**)

**Veri semantiği (zorunlu):** her `merge`'de `validate=` ve satır sayısı kontrolü · her `groupby`'da NA anahtar ve `dropna=` bilinçli mi · her filtrede sınır dahil/hariç · kopyala-görünüm zincirli atama · null vs NaN

**Mantık — tek gerçek test:** *"Bir gerçek girdiyi elle fonksiyondan geçir. Bu maddeyi atlarsan liste tiyatrodur."* Ve: **kod ne yapmıyor?** (omission hatası — otomasyonun gündeme getirmediği eksik)

**Yan etki:** `except Exception: pass` var mı · `assert` ile girdi doğrulaması (`-O` altında silinir) · idempotent mi

---

## 6. ★ Operatör döngüsü (S5-A7 — plana eklenen yeni katman)

### 6.1 Testler artık kalite aracı değil, **ajanın durma koşulu**

Durdurma sertliği dört kademeli [D]:
1. **Prompt içinde:** "implement ettikten sonra testleri çalıştır"
2. **Oturum boyunca:** `/goal` koşulu — ayrı değerlendirici her turdan sonra kontrol eder
3. **Deterministik kapı:** `Stop` hook — kontrol geçene kadar turu **bloklar**
4. **İkinci görüş:** doğrulama alt-ajanı — *"işi yapan ajan notu veren olmasın"*

Ve kanıt talebi [D]: *"Claude'un başarıyı iddia etmesi yerine **kanıt göstermesini** iste: test çıktısı, çalıştırdığı komut ve dönen sonuç. Kanıtı incelemek, doğrulamayı kendin tekrar çalıştırmaktan hızlıdır."*

### 6.2 Taze-bağlam incelemesi ve kalibrasyonu
Resmi desen [D]: inceleyici alt-ajan **yalnız diff'i ve ölçütleri** görür, *"değişikliği üreten akıl yürütmeyi görmez"* — bu, m.40b'nin CoVe-Factored kuralıyla aynı ilke.

Ama aynı doküman kalibrasyon uyarısı da veriyor [D]: *"Boşluk bulmaya yönlendirilen bir inceleyici, iş sağlam olsa bile genellikle bir şeyler rapor eder… Her bulgunun peşinden koşmak aşırı-mühendisliğe götürür."*

### 6.3 Kabul/ret kararı
- **Anthropic'in "iki düzeltme" kuralı** [D]: iki düzeltmeden sonra düzelmiyorsa yaklaşımı değiştir, düzeltmeye devam etme.
- *"Yeniden promptlamak mı ucuz, elle düzeltmek mi"* için **doğrudan ölçüm bulunamadı** — bu bir boşluk, sahada kendi verini toplayacaksın.

### 6.4 Ajana devredilmeyenler
Salt-okunur rejim ilk basamak (plan modu kaynak dosyaları değiştirmez, onaya kadar düzenlemeler bloklu). Geri-alınamaz eylemler, üretim verisine yazma, kimlik/erişim değişiklikleri devredilmez.

### 6.5 Ölçülen üretkenlik gerçeği — abartma
- **Veracode [K, satıcı]:** güvenli/güvensiz yol arasında seçim sunulduğunda modeller **%45** oranında güvensizi seçmiş. *"AI kodu 2,74x daha çok açık içeriyor"* iddiası ikincil sitelerde dolaşıyor, birincil metinde **doğrulanamadı [X] — kullanma.**
- **MSR 2026 [K]:** merge oranları ve inceleme sonuçları **küçük, yerel ve CI-doğrulanmış** agentic PR'larda daha iyi. → *Küçük dilim + CI, ajan işinin kabul edilebilirliğinin ölçülmüş bileşeni.*

---

## 7. AWS (S5-A2)

### 7.1 Yeni başlayan için ölümcül sınıflar
Açık S3 bucket · kök hesap kullanımı · uzun ömürlü erişim anahtarı. Disiplin: **"her şeye erişim verip sonra kısmak" değil, "hiçbir şeye verip gerekeni açmak."**

### 7.2 Maliyet birinci sınıf tasarım kısıtı
Athena taranan bayt · boşta Redshift kümesi · **NAT Gateway (en sinsi kalem)** · Glue · S3 sınıflarının minimum süre/boyut cezaları. **Uyarı: Free Tier değişti** — öğrenme ortamı kurarken kontrol et. *Tüm fiyat rakamları ikincil kaynaktan [K], doğrulanmalı.*

### 7.3 Terminoloji tuzağı
**"raw/curated/serving" AWS'in kendi dili DEĞİL.** Şirkette hangi adlandırmanın kullanıldığını sor — kendi terimini dayatma.

### 7.4 Sertifika: hayır (şimdi), evet (Ekim-Kasım)
**Şimdi sınava girme.** Ama **DEA-C01 Exam Guide'ı ücretsiz müfredat olarak oku (~2 gün)** — 4 domain + servis listesi, "AWS'te veri mühendisliği nelerden ibaret" haritasını bedavaya veriyor. Sertifika Ekim-Kasım'a: o noktada CV'de "öğrendim" değil **"kullanıyorum"** anlamına gelir. Çoğu işveren sınav ücretini karşılıyor — sormaya değer.

### 7.5 ★ "AWS'in inşası gibi" — cümlenin anlamını SOR
Teknik okuma üç şey önerir: katmanlı ve geri-alınabilir inşa · maliyet birinci sınıf kısıt · least privilege / blast radius.

Ama ajanın kendi uyarısı yerinde: *"cümle mimari bir metafor da olabilir, çalışma disiplini metaforu da. **Gerçek anlamı Salih'in şirkete sorması gereken şeydir** — ve bu iyi bir ilk-hafta sorusudur."*

**→ Bu, P3'teki "5 soru" listesinin birinci maddesi olmalı.**

---

## 8. Amazon kurumsal mekanizmaları (S5-A1 — düşük öncelik)

**Küçük ekibe taşınır:** kısaltılmış PR/FAQ (asıl faydası "kendine yalan söylemeyi engellemek") · 1-2 sayfalık karar notu + sessiz okuma · haftalık 30 dk mini-inceleme · hafif COE · **tek-yön/çift-yön kapı** (küçük ekipte daha da değerli) · **mekanizma testi**: *"iyi niyet mi kurdum, mekanizma mı? — denetim adımı yoksa kural yok demektir."*

**Kargo-kült olur:** zorunlu 6-sayfa ritüeli · Bar Raiser · OP1/OP2 yıllık plan · performans kotaları.

**Dürüst kayıt:** Amazon'un kendi CEO'su bürokrasiyi hedef aldı; ve *Anytime Feedback Tool* vakası — denetim ayağı olmayan bir "mekanizma" niyetin tersini üretti.

---

## 9. KRONOLOJİK PARTİSYONLAR (operatör katmanıyla güncellenmiş)

| Partisyon | Tarih | Konu | DONE |
|---|---|---|---|
| **P0** | 24 Tem · ~1 sa | **Kalibrasyon** | 10 SQL + 10 Python soğuk, çalıştırmadan yazılı tahmin → baseline yüzdesi kayıtlı |
| **P1** | 25–28 Tem | **SQL okuma** *(destekli)* | 15 sorgu, referanssız, ≤3 dk → **13/15 VE sessiz-hata 6/6** |
| **P2** | 29 Tem–1 Ağu | **Python okuma** *(destekli)* | 12 hücre; girdi/çıktı tipi-şekli + kırılma noktası → **≥10/12** · P1 bakım ≥4/5 |
| **P3** | 2–3 Ağu | **Kurumsal yöntem + AWS haritası** *(düşük yük)* | (a) 30 terim kapalı-kitap → **≥24/30** · (b) **ilk hafta soracağın 5 soru yazılı** — birincisi "AWS'in inşası gibi" ne demek |
| **P4** | 4–6 Ağu | **★ OPERATÖR ENTEGRASYONU** *(iskele sökülüyor)* | **Değişti** — aşağıda |
| **P5** | 7–8 Ağu | **Tampon** *(yeni içerik yok)* | P1–P4 DONE'larının hiçbiri açık değil |
| **P6** | 9–10 Ağu | **Soğuk prova + iniş** *(cramming yasak)* | 10 SQL + 8 Python + 15 terim tek oturum → **≥%80** |
| — | **11 Ağustos** | **BAŞLANGIÇ** | — |

### ★ P4 revizyonu (agentic coding bilgisiyle)

Eski DONE "100+ satırlık script'i oku, özet yaz" diyordu. **Format eşleşmiyor** — senin işin script okumak değil, ajan çıktısını yargılamak. Yeni DONE:

> **Üç tur, her biri sıfırdan:** (1) ajana yazılı bir görev tarifi ver — bağlam, kısıt, kabul ölçütü, kapsam sınırı · (2) çıktısını referanssız oku · (3) **kabul / reddet-yeniden-tarif et / elle düzelt** kararını **yazılı gerekçesiyle** ver · (4) sonra gerçek davranışla karşılaştır.
>
> **Geçme:** 3 turun 3'ünde karar doğru **ve** en az bir turda ajanın sessiz hatasını yakalamış olmak. Ajan hata yapmadıysa tur sayılmaz — hatayı sen enjekte et.

Bu, okuma becerisini de operatör kararını da aynı anda ölçer ve gerçek işin biçimindedir.

### Pazarlıksız kurallar
1. Her artefakt **5-adımlı çevrimle** okunur
2. Hiçbir konuya **3 günden fazla ara** yok (10 dk/gün soğuk dokunuş)
3. **Yeniden okuma / pasif izleme yok**
4. DONE testleri **soğuk, görülmemiş, referanssız, yazılı**
5. **Eşik düşürülmez, kapsam küçültülür**
6. **Minimum doz:** kötü gün = 15 dk / 5 artefakt. Sıfır gün yok
7. **Kayma kuralı:** 1 gün→tampon · 2 gün→kapsam · 3+ gün→plan P1+P3'e iner
8. **Günlük tavan 2,5 saat** *(bu rakamın hakemli dayanağı yok [X])*
9. Her partisyon başında **eğer-o zaman planı** yazılır
10. Son 2 gün **iniş**

**Yöntemsel şerh:** S5-A5 **harmanlamayı tavsiye etmiyor** (mekanizması bu üç konuya uymuyor); tavsiye edilen **aralıklama**. Plan buna göre: gün-içi bloklu, günler-arası aralıklı.

---

## 10. JARVIS bağlamı — köprü notu (m.16 hattı, karar değil)

Staj hattı panoya üçüncü zaman-baskılı şerit olarak giriyor: **K-015** "ÖNCELİK №1" (hedef ~10 Ekim) ile saat rekabeti · **K-002 PortRisk** BEKLEYEN'de kalma gerekçesi değişiyor · **K-004** (CV/İngilizce, Kasım) staj malzemesiyle besleniyor — ve S5-A2'nin sertifika zamanlaması (Ekim-Kasım) doğrudan K-004 penceresine düşüyor.

Bu bir çelişki raporu değil, yük bildirimi. Karar ana oturumda.

---

## 11. Cevaplanmamış sorular (m.41)

1. **"AWS'in inşası gibi" ne demek?** — şirkete sorulacak; P3'ün 5 sorusunun birincisi.
2. Staj hangi yığında, hangi katman adlandırmasıyla çalışıyor?
3. Günlük gerçekçi çalışma penceresi? Plan 1,5–2,5 saat varsayıyor, **hakemli dayanağı yok [X]**.
4. Ajan çıktısında "yeniden promptla vs elle düzelt" eşiği — **ölçüm yok**, sahada kendi verini topla.
5. Staj JARVIS'e nasıl bağlanacak — ayrı şerit mi, K-004 altında mı, yeni kart mı?
6. Şirkete dair bilginin bu repoya yazılma sınırı nedir? (m.14 private ama üçüncü taraf)
7. **S5-A6 (AWS'in inşa felsefesi) koşamadı** — "inşa gibi" cümlesinin üçüncü okuması eksik.

---

*Yan-oturum çıktısı. Kanon kilitlenmedi. Nihai planlama PC ana oturumunda.*
