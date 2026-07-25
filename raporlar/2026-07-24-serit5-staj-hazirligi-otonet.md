# Şerit 5 — Staj Hazırlığı (Otonet/Otoplus, başlangıç 11 Ağustos 2026)

> **Mod:** yan-oturum (m.41) — hazırlık malzemesi. **Nihai planlama PC ana oturumunda** (Salih beyanı 07-24).
> **Tarih:** 2026-07-24 · **Kalan süre: 18 gün**
> **Şerit durumu:** 6 aile açıldı, **3'ü rapor yazdı**, 3'ü oturum limitinde öldü.
> **Kaynak:** `scratchpad/S5-A{1,4,5}-seritA.md`

## 0. Önce eksikler (bu rapor yarım — hangi yarısı eksik, açıkça)

| Aile | Konu | Durum |
|---|---|---|
| S5-A1 | Amazon kurumsal mekanizmaları | ✅ tam rapor |
| S5-A2 | **AWS platformunda veri mühendisliği** | ❌ öldü |
| S5-A3 | **SQL okuma + ajanla kullanma** | ❌ öldü |
| S5-A4 | Python kod okuma okuryazarlığı | ✅ tam rapor |
| S5-A5 | Öğrenme yöntemi + kronolojik partisyon | ✅ tam rapor |
| S5-A6 | AWS'in inşa felsefesi | ❌ öldü (kuyrukta bile koşamadı) |

**Kritik boşluk:** Üç görevden **ikisinin içerik araştırması yok.** SQL hiç araştırılmadı. AWS tarafında yalnız *kurumsal kültür* okuması survived — oysa Salih'in şerhine göre (*"çalışma sürecimiz AWS'in inşası gibi olacak"*) asıl hedef platform/inşa okumasıydı, yani **hayatta kalan aile en az ilgili olanı.**

**Ama plan iskeleti ayakta:** S5-A5 yöntem ailesi üç konunun da partisyonunu kurdu. Yani *ne zaman ne çalışılacağı* belli; *SQL tarafında neyin çalışılacağı* eksik. Limit sıfırlanınca ilk koşacak üç ajan: **S5-A3, S5-A2, S5-A6.**

## 1. Kanıt kısıtı (dürüstlük — S5-A5'in kendi beyanı)

Bu şeritte egress politikası akademik yayıncıların tamamını 403'ledi. **S5-A5 raporunun tamamı [K]'dır** — hiçbir birincil kaynağa inilemedi; tüm etki büyüklükleri arama özeti düzeyinde. S5-A4 daha şanslı (GitHub üzerinden bazı [D]'ler). S5-A1 ağırlıklı [K] + belgelenmiş [X]'ler.

**Sonuç:** Aşağıdaki rakamlar (g=0.74, d=0.60 vb.) yön göstergesi olarak kullanılmalı, sayı olarak alıntılanmamalı. Plan bunlara *yaslanmıyor*; plan yön üzerine kurulu.

## 2. ★ Planın temelini belirleyen karar: "okuma" ne demek?

İki görev de "okumayı öğrenme" diyor. S5-A5 bu varsayımı doğrudan sınadı ve **üç parçalı** cevap verdi:

1. **Hedef okumaysa — EVET, risk yok.** Beceri hiyerarşisinde okuma yazmanın *altındadır*; öğretim teorisi "önce oku sonra yaz" der; alıcı bilgi üretici bilgiden hızlı gelişir. **18 günde okuma yeterliliği hedeflemek kanıtla desteklenen bir karar.**
2. **Ama "pasif okuma" kastediliyorsa — HAYIR, çok riskli.** Yeniden okuma düşük faydalı; akıcılık yanılsaması tam burada devreye girer. *"En büyük risk beceriksizlik değil, ölçülmemiş sahte yeterliliktir — 11 Ağustos'ta 'hazırım' hissiyle gidip ilk gerçek sorguda donmak."*
3. **Tamamen sıfır üretim — savunulamaz.** Yazma→okuma transferi kanıtlı; küçük üretim dozu okuma hedefine hizmet eder.

### → Bunun somut sonucu: okuma birimi 5-adımlı çevrimdir

Plan **"200 sorgu oku" OLAMAZ.** Her artefakt şu çevrimle okunur (pazarlıksız):

1. **Tahmin yaz** — çalıştırmadan, cevaba bakmadan, ne yaptığını **yazılı** söyle
2. **Doğrula** — çalıştır / cevabı aç
3. **Farkı açıkla** — neden yanıldığını 1 cümleyle yaz
4. **Yanlışı kuyruğa at** — 2–3 gün sonra tekrar gelsin
5. **Üretim vergisi** — her 5 okunan artefakta 1 küçük değişiklik yaz

*Adım 1 ve 3 olmadan bu plan "düşük fayda" kutusuna düşer.*

## 3. ★ En yüksek getirili bulgu (beklenmedik)

S5-A5'in ilk-gün etkisi analizi, hazırlık önceliklerini **tersine çeviriyor**:

**İşe yarayan:**
1. **Terim/kelime dağarcığı tanıma** → rol netliğini besler; rol netliği en hızlı kazanılan ve performansa aracılık eden boyut.
2. **Hazırlanmış soru repertuarı** → *"Yazılı 5 soru, 5 saatlik ekstra SQL çalışmasından daha yüksek beklenen getiriye sahiptir."*
3. **Öz-yeterlik** → DONE'ları geçtikçe planın kendisi üretir.

**Boşa giden:**
1. **Görev ustalığı avı** — en yavaş kazanılan boyut, 18 günde satın alınamaz.
2. **Kurumun özgül şemasını önceden öğrenmeye çalışmak** — bilinemez.
3. **Yazma (üretim) becerisine yatırım** — iş görevi okumaysa format eşleşmez.
4. **Son 2 günde cramming** — kazanımlar söner.

> **Hedef:** *Advanced Beginner okuma yeterliliği + rol netliği + öz-yeterlik + hazır soru repertuarı.*
> **Hedef değil (18 günde alınamaz):** görev ustalığı.

**Uyarı [X]:** "yeni işe alınanlar 1-3 ayda tam üretkenliğe ulaşır" tipi rakamlar yalnız satıcı bloglarında bulundu, hakemli kaynak yok. Plan bunlara yaslanmıyor.

## 4. KRONOLOJİK PARTİSYONLAR (S5-A5 iskeleti)

**Tasarım ilkeleri:** dikey dilim (her partisyon kullanılabilir yetenekle biter) · 2–4 günlük partisyonlar · gün-içi bloklu, günler-arası aralıklı · destekli → destek-azaltılmış iki rejim · Mager formatında ölçülebilir DONE · açık tampon · son iki gün iniş · günde 1,5–2,5 saat aktif.

| Partisyon | Tarih | Konu | DONE (ölçülebilir) |
|---|---|---|---|
| **P0** | 24 Tem (bugün) ~1 sa | **Kalibrasyon** | 10 SQL + 10 Python soğuk okunur, çalıştırmadan yazılı tahmin → **baseline yüzdesi yazılı** |
| **P1** | 25–28 Tem (4 gün) | **SQL okuma / çekirdek** *(destekli)* | 15 görülmemiş orta sorgu, referanssız, ≤3 dk/sorgu; her biri için tablolar+filtre+granülerlik+satır yönü → **≥12/15** |
| **P2** | 29 Tem–1 Ağu (4 gün) | **Python okuma / çekirdek** *(destekli)* | 12 görülmemiş hücre; girdi tipi/şekli + çıktı + kırılma noktası → **≥10/12**; ayrıca P1 bakım testi ≥4/5 |
| **P3** | 2–3 Ağu (2 gün) | **Kurumsal çalışma yöntemi** *(düşük yük)* | (a) 30 terim kapalı-kitap, kendi cümlenle + "bu bana ne yaptırır" → **≥24/30** · (b) **ilk hafta soracağın 5 soru yazılı ve spesifik** |
| **P4** | 4–6 Ağu (3 gün) | **Entegrasyon** *(iskele sökülüyor)* | 1 gerçek-boyutlu artefakt (100+ satır script **veya** 40+ satır sorgu), referanssız, 10 cümlelik yazılı davranış özeti → **≤2 maddi hata (%90 eşik)** |
| **P5** | 7–8 Ağu (2 gün) | **Tampon** *(yeni içerik YOK)* | P1–P4 DONE'larının **hiçbiri açık değil** |
| **P6** | 9–10 Ağu (2 gün) | **Soğuk prova + iniş** *(cramming YASAK)* | 9 Ağu: 10 SQL + 8 Python + 15 terim tek oturum karma sınav → **≥%80**; 10 Ağu: ≤45 dk hafif geri-çağırma + lojistik |
| — | **11 Ağustos** | **STAJ BAŞLANGICI** | — |

### Pazarlıksız kurallar (tüm partisyonlar boyunca)

1. Her artefakt **5-adımlı çevrimle** okunur
2. Hiçbir konuya **3 günden fazla ara** yok (odak dışı konulara 10 dk/gün)
3. **Yeniden okuma / vurgulama / pasif izleme yok**
4. DONE testleri **soğuk, görülmemiş, referanssız, yazılı**
5. **Eşik düşürülmez, kapsam küçültülür**
6. **Minimum doz:** kötü gün = 15 dk / 5 artefakt. Sıfır gün yok, tam gün de zorunlu değil
7. **Kayma kuralı önceden yazılı:** 1 gün→tampon · 2 gün→kapsam küçülür · 3+ gün→plan P1+P3'e indirgenir
8. **Günlük tavan 2,5 saat**
9. Her partisyon başında **eğer-o zaman planı** yazılır
10. Son 2 gün **iniş**, yeni içerik yok

**Yöntemsel şerh (ayrışan hat):** S5-A5 **harmanlamayı (interleaving) tavsiye ETMİYOR** — genel etki olumlu görünse de kelime-benzeri materyalde tersine dönüyor ve mekanizması (ayırt etme) bu üç konuya uymuyor. Tavsiye edilen **aralıklama**. Bu ayrım plana işlenmiş durumda: gün-içi bloklu, günler-arası aralıklı.

## 5. Python okuma — uygulanabilir çekirdek (S5-A4)

### 5.1 LLM üretimi Python'da aranacak 6 hata sınıfı

| # | Sınıf | Ölçülmüş büyüklük | Kim yakalar |
|---|---|---|---|
| 1 | Uydurma paket/API | **%19,7 paket halüsinasyonu** [D] | Import denemesi, lockfile |
| 2 | Eski/deprecated API | %25–38 [K] | Sürüm-farkındalıklı linter |
| 3 | Güvenlik açığı | %12–40 (çelişkili) [X] | Bandit/ruff-S, SAST |
| 4 | **Sessiz mantık hatası** | %66 "neredeyse doğru" [K] | **Yalnız insan okuması + karşı-test** |
| 5 | Atlanmış hata yolu | nitel [K] | Property testing |
| 6 | **Boş test tiyatrosu** | nitel [K] | **Yalnız insan okuması** (testi oku, kodu değil) |

**Kritik:** 4 ve 6 numaralı sınıfları **hiçbir araç yakalamıyor** — okuma okuryazarlığının varlık sebebi tam olarak bu ikisi. Bu, "neden okumayı öğreniyorum" sorusunun kanıtlı cevabı.

### 5.2 Onay öncesi kontrol listesi — veri işi için en kritik maddeler

**Mekanik (30 sn):** her `import` lockfile'daki sürümde mi · her method çağrısını **tanıma atla, doğrula** · diff >400 satırsa bölmeden inceleme (tespit oranı %65→%28)

**Veri semantiği (veri mühendisliği için ZORUNLU):**
- Her `merge`: `validate=` var mı? Satır sayısı kontrolü var mı?
- Her `groupby`: NA anahtar mümkün mü, `dropna=` bilinçli mi?
- Her filtre: sınır dahil mi hariç mi (`<` vs `<=`) — **tarih aralıklarında off-by-one AI'ın en klasik sessiz hatası**
- Kopyala/görünüm: zincirli atama var mı? null vs NaN?

**Mantık — TEK GERÇEK TEST:** *"Bir gerçek girdiyi elle fonksiyondan geçir. Bu maddeyi atlarsan liste tiyatrodur."* Ayrıca: kod **ne yapmıyor**? (omission hatası — otomasyonun gündeme getirmediği eksik.)

**Yan etki:** `except Exception: pass` var mı · `assert` ile girdi doğrulaması yapılmış mı (`-O` altında silinir) · idempotent mi?

**★ Karşı-kanıt (dürüst kayıt):** S5-A4, "AI yardımı okuma becerisini **aşındırıyor**" yönünde bulgu da getirdi. Yani ajanla çalışmak, okuma becerisini kendiliğinden geliştirmiyor — bilinçli pratik gerekiyor. Bu, stajda ajan kullanırken de geçerli.

## 6. Amazon çalışma yöntemi — küçük ekibe ne taşınır (S5-A1)

**Taşınabilir (ölçek gerektirmez):** PR/FAQ (kısaltılmış — asıl faydası "kendine yalan söylemeyi engellemek") · yazılı karar notu 1–2 sayfa + sessiz okuma · girdi/çıktı metrik ayrımı + haftalık 30 dk mini-inceleme · hafif COE (1 sayfa: ne oldu, etki, zaman çizelgesi, 5 neden, sahipli+tarihli aksiyon) · **tek-yön/çift-yön kapı** (küçük ekipte *daha da* değerli) · "you build it you run it" · **mekanizma testi**: "iyi niyet mi kurdum, mekanizma mı? — denetim adımı yoksa kural yok demektir"

**Kargo-kült olur (taşıma):** zorunlu 6-sayfa + 30 dk sessiz okuma ritüeli · Bar Raiser (ekip dışı havuz gerektirir) · OP1/OP2 yıllık plan · performans kotaları

**Eleştiri literatürü (dürüst bakış):** Amazon'un kendi CEO'su bürokrasiyi hedef aldı (yönetici başına çalışan oranını %15 artırma, "bürokrasi ihbar hattı"). Ve klasik vaka: *Anytime Feedback Tool* — denetim bileşeni olmayan ve teşvikleri yanlış hizalayan bir "mekanizma", niyetin tersini üretti. **Ders bizim m.29/deneysel damga disiplinimizle aynı: mekanizmanın denetim ayağı yoksa mekanizma değildir.**

> Bu bölüm Salih'in şerhine göre **düşük öncelikli** — asıl hedef platform/inşa okumasıydı, o aile koşamadı.

## 7. JARVIS bağlamı — köprü notu (m.16 hattı, karar değil)

Staj hattı panoya üçüncü bir zaman-baskılı şerit olarak giriyor ve iki mevcut kararla temas ediyor:

- **K-015 "ÖNCELİK №1"** (m.36 2. revizyon, hedef ~10 Ekim) — staj 11 Ağustos–? aralığında Salih'in saatlerini alacak.
- **K-002 PortRisk** BEKLEYEN'de, gerekçesi *"birkaç gün odak öğrenme+Jarvis"* idi; o "birkaç gün" artık farklı bir şeye tahsis oluyor.
- **K-004** (İngilizce/CV paketi, Kasım) — staj CV malzemesi üretiyor, yani K-004'ü besliyor.

**Bu bir çelişki raporu değil, bir yük bildirimi.** Karar ana oturumda; ben yalnız görünür kılıyorum.

## 8. Sıradaki iş (limit sıfırlanınca — UTC 03:50 sonrası)

1. **S5-A3 (SQL okuma + ajanla kullanma)** — en büyük boşluk, P1 partisyonunun içeriği buna bağlı
2. **S5-A2 (AWS veri mühendisliği hattı)** — Salih'in şerhine göre asıl hedef
3. **S5-A6 (AWS'in inşa felsefesi)** — "AWS'in inşası gibi" cümlesinin doğrudan karşılığı
4. Sonra: bu üçünün antitezleri + hakemlik

**Ama P0 bugün koşulabilir** — kalibrasyon için araştırma gerekmiyor, yalnız 10 SQL + 10 Python artefaktı ve yazılı tahmin. Araştırma beklenmeden başlanabilecek tek partisyon bu.

## 9. Cevaplanmamış sorular (m.41)

1. Staj hangi teknoloji yığınında? (AWS mi, başka bulut mu, on-prem mi) — S5-A2'nin kapsamı buna bağlı.
2. "AWS'in inşası gibi" cümlesi kim tarafından, hangi bağlamda söylendi? Kurumsal mekanizma mı, servis mimarisi mi kastediliyor?
3. Günlük gerçekçi çalışma penceresi ne kadar? Plan 1,5–2,5 saat varsayıyor ve bu rakamın **hakemli dayanağı yok** [X].
4. Staj JARVIS'e nasıl bağlanacak — ayrı şerit mi, K-004'ün altında mı, yoksa yeni kart mı?
5. Şirkete dair hiçbir bilgi bu repoya yazılmamalı mı (m.14 private ama yine de üçüncü taraf)? Sınırı Salih çizmeli.

---

*Yan-oturum çıktısı. Kanon kilitlenmedi. Nihai planlama PC ana oturumunda (Salih beyanı 07-24).*
