# 24 Temmuz Koşumu — Telefon Özeti

*Beş raporun okunur hâli. Geniş tablo yok, kaydırarak okunur. Her bölümün sonunda tam rapor adresi var.*

---

## Önce: bugün ne oldu

Beş şeritte çift-atlas koşumu yapıldı. Toplam **96 ajan** çalıştı (91'i bitti, 5'i hâlâ açık), kabaca **9–10 milyon token**.

Bunun büyük kısmı gereksizdi ve sebebi bende: her ajan en pahalı kademede (`xhigh`) koştu, çünkü bu ayar önceki oturumdan mirastı ve atlas tanımında onu ezecek alan yok. Ayrıca ajanlar kendi çocuklarını açtı — 25 ajan açtım, 96 koştu. Delegasyon kotası yok.

**Beş rapor yazıldı ve push'landı.** Bundan sonrası ajan istemiyor.

---

## 1. Opus 5 — sistemimizde ne değişiyor

**En önemli sonuç: doğrulama protokolümüz tehdit altında değil.**

Anthropic "doğrulama talimatlarını kaldırın" diyor ve bu ilk bakışta bizim tez→antitez→hakemlik zincirimizi söktürüyor gibi görünüyordu. İki bağımsız antitez ajanı aynı ayrımı buldu: kaldırılması istenen şey modelin **kendi işini** tekrar kontrol etmesi. Bağımsız çapraz denetim aynı sayfada **öneriliyor**. m.40b duruyor.

**İkinci sonuç: kanon dosyalarını kısaltma baskısı yok.** Resmî 200-satır eşiği bize uygulanmıyor; bizim KB+token rejimimiz zaten daha iyi bir ölçü. CLAUDE.md 27 satır.

**Üçüncü sonuç: yapısal kilit tercihimiz doğrulandı.** CLAUDE.md resmî olarak "bağlam, zorlanan konfigürasyon değil" sayılıyor; kesin yaptırım için hook/izin gerekiyor — bizim Dilim-1 paketinin tam olarak yaptığı şey.

**Güncellenmesi gerekenler:** `cc/README.md` envanteri bayat (2.1.209 yazıyor, gerçek 2.1.220 — üstelik oturum ortasında güncellendi). Görev emri ritüeline iki satır eklenmeli: modeli ve eforu oturum başında sabitle, ortada değiştirme; koşum öncesi efor seviyesini teyit et.

**Dikkat:** Opus 5 varsayılanı her planda değil — Pro ve Team Standard'da Sonnet 5 geliyor. Hangi plandayız, kanona yazılmalı.

→ `raporlar/2026-07-24-serit1-opus5-sistem-etkisi.md`

---

## 2. Graph engineering — girer mi

**Kısa cevap: etiketi alma, pratiği al.**

Terim 4–18 Temmuz arasında X'te doğmuş. Kurumsal duyuru yok, makale yok, konferans yok. Anthropic'in 6,36 MB'lık tüm doküman korpusunda "graph engineering" **sıfır kez** geçiyor. En yetkin teknik aktör (LangChain) terimi reddetmedi ama sahiplendi — "yeni değil" diyerek.

**Asıl bulgu terimde değil, kendi depomuzda.** Ajan dış kaynaklara erişemeyince kendi repomuzu ölçtü:

146 markdown dosyanın **%92,5'i graf olarak yetim**. Sadece 15 çözülen bağlantı var. Ve daha sert olanı: 19 Temmuz'da elle tutulan wiki index'i 6 sayfadan **2'sini** listeliyormuş — %67 kayıp, üç gün sonra elle düzeltilmiş. Bunu ben git tarihinden doğruladım, doğru çıktı.

Yani "elle tutulan index bayatlar" bizde teorik risk değil, **yaşanmış vaka**.

**Öneri:** graf veritabanı değil, **türetilmiş index**. Bir saatlik iş, sıfır yeni bağımlılık, tek `git revert` ile geri alınır. Vault dosyalarına dokunmaz.

**Girmeyecekler:** graf veritabanı (bakım riski canlı), GraphRAG (maliyet ölçüldü, faydası bizim ölçekte ölçülmedi), orkestrasyon grafı çerçevesi (bizim iş profilimizde ölçülen etki **negatif**).

→ `raporlar/2026-07-24-serit2-graph-engineering.md`

---

## 3. Ekip liderleri — ayrı klasör mü, gömülü mü

**Cevap: gömülü. Ama doğru yere gömülü.**

Bu şerit koşum sırasında fikir değiştirdi. Üç ajan da "ayrı klasör üstündür" tezini savunmakla görevlendirildi; ikisi kendi tezini kısmen yıktı, antitez kalanı yıktı.

Düşen argümanlar: "gömülü liderler görünmez" (yanlış — `.claude/agents/` özyinelemeli taranıyor) · "ayrı klasör bağlam izolasyonu verir" (yanlış — izolasyon çalışma-zamanı özelliği) · "çok kök arama kaybı yaratır" (ölçüldü, yanlış) · "boyut ayrışmayı gerektirir" (depo 1,3 MB, eşik 10 GB).

**Kritik ayrım:** liderler `.claude/agents/<lider>/` altına gömülmeli, `liderler/<ad>/` gibi sıradan bir klasöre **değil**. Birincisi kökten görünüyor, ikincisi görünmüyor.

**Ayrı repo yalnız bir durumda haklı:** bir lider dışarı açılacaksa. Görünürlük repo-atomik; alt-dizin görünürlüğü diye bir şey yok.

**Ve karar ucuz:** gömülüden ayrıya geçiş gerçek repomuzda ölçüldü — yarım saniye, tarihçe korunuyor, çift yönlü. Yanlış çıkarsa dönülür.

→ `raporlar/2026-07-24-serit3-ekip-lideri-klasor-duzeni.md`

---

## 4. Araştırma ajanı — nasıl optimize edilir

**Önerilen yapı tek bir "atlas" değil, üç rol:**

**Toplayıcı** — ham indirme, grep, ölçüm. Ucuz model, düşük efor.
**Tez/antitez** — okuma, iddia çıkarma, çürütme. Orta-yüksek. *Burada ucuza kaçılmaz*: düşük efor yalnız düşünmeyi değil araç çağrı sayısını da kısıyor, yani kayıp önce **kapsamda** görünür — araştırmada en kötü kayıp türü.
**Hakem** — maskeli kıyas. **Farklı model ailesi.**

Son madde bugünün en rahatsız edici bulgusu: öz-tercih yanlılığı ölçülmüş ve bizim zincirde tez, antitez, hakem **hepsi Claude**. Yani hakem kendi ailesinin çıktısını kayırıyor olabilir. Ayrıca uzunluk yanlılığı sert — şişirilmiş uzun metin hakemi yanıltıyor, bizim raporlarımız uzun.

**Atlas tanımından silinecekler** (~300 satır, %64 kısalma): akademik makale modu · ölü context7 ayağı · bayat çıktı adresi (`docs/research/` diye bir klasör yok) · skill'le çakışan ikinci ayrıştırma protokolü.

**Eklenecekler:** `effort:` (bugünkü faturanın tek satırlık ilacı) · `maxTurns:` · kapsam kilidi · rapor uzunluk kalibrasyonu.

**Ve zarif olan:** delegasyon kotası atlas'a değil **bana** yazılmalı — atlas zaten çocuk açamıyor, kotayı ihlal eden orkestratör.

**En büyük bulgu:** araştırma kapasitemizin tavanı ajan tasarımı değil, **ortamın ağ politikası**. Anthropic dokümanlarına erişebilen şerit 36 [D] üretti; dış web'e bakan şerit tek bir [D] üretemedi. Fark ajanda değil, izin listesinde.

→ `raporlar/2026-07-24-serit4-arastirma-ajani-optimizasyonu.md`

---

## 5. Staj hazırlığı — 18 gün

**İşin gerçek tanımı: sen doğrulama katmanısın.**

Ajan üretimi kodun ölçülen altı hata sınıfından ikisini **hiçbir araç yakalamıyor**: sessiz mantık hatası ve boş test tiyatrosu. Sadece insan okuması yakalıyor. Resmî cümle şu: *"Çalıştırabileceği bir kontrol yoksa doğrulama döngüsü sen olursun."*

Ve karşı-bulgu: **AI yardımı okuma becerisini aşındırıyor.** Yani ajanla çalışmak seni kendiliğinden iyi okuyucu yapmıyor.

**Okuma birimi = 5 adımlı çevrim.** Plan "200 sorgu oku" olamaz. Her artefakt için: çalıştırmadan **yazılı tahmin** → doğrula → farkı 1 cümleyle açıkla → yanlışı 2-3 gün sonraya kuyruğa at → her 5 artefakta 1 küçük değişiklik yaz. İlk ve üçüncü adım olmadan plan işe yaramaz.

**En yüksek getirili hazırlık kalemi beklenmedik:** *yazılı 5 soru, 5 saatlik ekstra SQL çalışmasından daha değerli.* Hedef görev ustalığı değil — 18 günde alınamaz. Hedef: okuma yeterliliği + rol netliği + öz-yeterlik + hazır soru repertuarı.

**SQL'de yedi sessiz katil** var; en tehlikelisi `NOT IN` + NULL (sonuç **her zaman** boş döner) ve LEFT JOIN + WHERE (dış birleştirme sessizce iç birleştirmeye döner). Sınavın geçme ölçütü iki koşullu: 13/15 **ve** sessiz-hata sorularının hepsi. Çünkü birini kaçırmak, staj ortamında hata vermeden yanlış rakam raporlamak demek.

**AWS'te sorulacak soru var, öğrenilecek cevap değil:** "raw/curated/serving" AWS'in kendi dili değil; ve **"AWS'in inşası gibi" cümlesinin gerçek anlamını şirkete sormalısın**. Bu, ilk hafta sorularının birincisi olmalı. Sertifikaya şimdi girme — ama sınav rehberini ücretsiz müfredat olarak oku (~2 gün). Sertifika Ekim-Kasım'a, o zaman CV'de "öğrendim" değil "kullanıyorum" demek olur.

### Takvim

**P0 — bugün, ~1 saat.** 10 SQL + 10 Python artefaktını soğuk oku, her biri için çalıştırmadan yazılı tahmin. Baseline yüzdesini kaydet. *Bu olmadan diğer partisyonların ölçütü anlamsız.*

**P1 — 25-28 Temmuz.** SQL okuma. Bitiş: 15 sorgu, referanssız, ≤3 dk → 13/15 ve sessiz-hata 6/6.

**P2 — 29 Temmuz-1 Ağustos.** Python okuma. Bitiş: 12 hücre → ≥10/12, artı P1 bakım testi.

**P3 — 2-3 Ağustos.** Kurumsal yöntem + AWS haritası, düşük yük. Bitiş: 30 terim kapalı kitap ≥24/30 **ve ilk hafta soracağın 5 soru yazılı**.

**P4 — 4-6 Ağustos.** Operatör entegrasyonu. Üç tur: ajana yazılı görev tarifi ver → çıktısını soğuk oku → **kabul / reddet-yeniden tarif et / elle düzelt** kararını gerekçesiyle yaz → gerçek davranışla karşılaştır. En az bir turda sessiz hatayı yakalamış olmalısın; ajan hata yapmazsa sen enjekte et.

**P5 — 7-8 Ağustos.** Tampon. Yeni içerik yok.

**P6 — 9-10 Ağustos.** Soğuk prova, sonra iniş. Cramming yasak.

**11 Ağustos — başlangıç.**

**Pazarlıksız kurallar:** hiçbir konuya 3 günden fazla ara yok · yeniden okuma/pasif izleme yok · sınavlar soğuk ve yazılı · **eşik düşürülmez, kapsam küçültülür** · kötü gün minimum 15 dakika, sıfır gün yok · günlük tavan 2,5 saat · son iki gün yeni konu yok.

→ `raporlar/2026-07-24-serit5-staj-hazirligi-otonet.md`

---

## Senin karar vermen gerekenler

**1.** Hangi Claude planındayız? Model varsayılanı buna bağlı.

**2.** Araştırma yüzeyinin ağ politikası genişleyecek mi? Bugün dış kaynağa inilemediği için V26 kaynak-denetimi yapısal olarak imkânsızdı. Ya kural yüzeye koşullanmalı ya politika değişmeli.

**3.** Hakem katmanı farklı model ailesine taşınabilir mi?

**4.** Staj hattı panoya nasıl girecek? K-015 "öncelik №1" ile saat rekabeti var, K-004 (CV, Kasım) ile beslenme ilişkisi var.

**5.** Atlas tanımı revizyonu ve efor kotası — `.claude/` yapısal kilitli olduğu için ana oturumda yapılmalı.

---

## Dürüstlük notları

- Kanıt tavanı yüzey tarafından belirlendi. Şerit 2, 3 ve 5'in çoğu [K] etiketli, çünkü kaynağa inilemedi.
- Maskeli hakemlik ayrı ajanla koşulmadı; sentezleri ben yaptım ve hangisinin tez hangisinin antitez olduğunu bilerek yaptım. Raporlarda şerhli.
- Dört antitez koşamadı. Hangi hükmün tek-şeritli kaldığı raporlarda işaretli.
- İki kez kendi hükmümü düzeltmek zorunda kaldım: iç içe ajan çıkarımım hatalıydı, ve "ajanlar öldü" dediğim şey doğru değildi.
