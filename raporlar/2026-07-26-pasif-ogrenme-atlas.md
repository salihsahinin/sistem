# Pasif Öğrenme Modeli · Ajan Donması · Kaynak Kategorizasyonu — Atlas Raporu (2026-07-26)

> **Mod:** yan-oturum (m.41 — CC bulut) · şerit: çift-atlas (tez ∧ ¬tez) · aile sayısı: 8 (A1–A8)
> **Koşum:** 8 tez atlası + 8 antitez atlası (CoVe-Factored: antiteze yalnız çıplak iddia listesi verildi, gerekçe/kaynak VERİLMEDİ) + hakemlik (Carvis) + 1 yerel ölçüm (bu oturumun kendi telemetrisi)
> **Tetikleyen:** Salih 07-26 — (1) pasif öğrenme modeliyle karar-akışından öğrenme metni üretimi, staj bağlamı · (2) araştırma ajanlarının donması, DS bakışıyla çözüm + oturumlaştırma · (3) şirkete ajan ataması · (4) kaynak-kategori sayısının optimumu

---

## 0. KANIT KISITI — bu raporun en önemli satırı (dürüstlük beyanı)

**Bu oturumda hiçbir akademik kaynağa inilemedi.** Kurumsal egress politikası, denenen akademik hostların tamamını CONNECT düzeyinde reddetti (403 / bağlantı kurulamadı). Carvis 10 hostla ayrıca ölçtü: **10/10 ret**.

```
export.arxiv.org · ncbi.nlm.nih.gov · doi.org · scholar.google.com · researchgate.net
core.ac.uk · api.crossref.org · biorxiv.org · psycnet.apa.org · link.springer.com   → hepsi ret
```

Bunun üç sert sonucu var ve raporun her satırı bu kısıtın altında okunmalıdır:

1. **A1, A2, A3 ailelerinde D etiketi hak eden TEK BİR bulgu yoktur.** m.40b'de D = "birincil kaynağa inildi"; bu oturumda mümkün değildi. Tavan **K**'dir.
2. **A4, A5, A7 ailelerinde D vardır** — çünkü bu ailelerin kaynakları akademik değil teknik: `platform.claude.com`, `code.claude.com`, `github.com`, ve özellikle **`raw.githubusercontent.com` üzerinden dokümantasyonun upstream depoları** (kubernetes/website, temporalio/documentation, celery/celery, github/docs, circleci/circleci-docs, buildkite/docs, mdn/content, torvalds/linux, envoyproxy/envoy, nginx/nginx.org, open-telemetry/semantic-conventions-genai, anthropics/anthropic-sdk-python). Bu, kapalı hostun etrafından dolaşmak DEĞİL — aynı metnin kaynağına inmektir ve [D] etiketini hak eder.
3. **V26 örneklem-denetimi klasik haliyle koşulamadı.** "Rastgele iddia seç, kaynağa in, doğrula" adımı fiziksel olarak kapalıydı. Yerine **çapraz-sorgu denetimi** koşuldu (aynı rakam bağımsız sorgularda tekrar ediyor mu) ve V26 yerine geçtiği İDDİA EDİLMİYOR. Bölüm 10'a bakınız.

**Sonuç: bu rapor karar-öncesi TARAMA olarak kullanılabilir, KANIT olarak kullanılamaz.** Akademik rakamların tüzük anlamında hüküm taşıması için erişimi açık bir oturumda yeniden doğrulanması gerekir (bölüm 12, açık borç #1). Teknik [D] bulguları bu borcun dışındadır.

---

## 1. YÖNETİCİ ÖZETİ — hayatta kalan çekirdek

Adversaryal saldırıdan sağ çıkan iddialar (bilgili bir antitez ajanı çürütmeyi deneyip **başaramadı**):

| # | Hayatta kalan çekirdek | Aile | Etiket |
|---|---|---|---|
| S1 | Bir LLM, kalıcı bellek altyapısı olmadan önceki oturumlardan öğrenen-modeli **taşımaz**; kalıcılık modelin değil **uygulama katmanının** özelliğidir. | A1 | K |
| S2 | LLM sentezinden öğrenmek, **çekirdek olgular aynı sunulsa bile** web aramasıyla öğrenmeye göre daha sığ bilgi üretir (7 deney, n=10.462). | A2 | K |
| S3 | Halüsinasyonlu bir içerik bir kez öğrenildiğinde, sonraki düzeltme etkiyi **tamamen silmez** (4 bağımsız meta-analiz aynı yöne). | A4 | K |
| S4 | Ajan-belleği satıcı rakamları **kıyaslanamaz**; LoCoMo protokol boşlukları + çözülmemiş satıcı ihtilafı birincil kaynakla doğrulandı. | A4 | D |
| S5 | Doğru asılma-saptama primitifi mutlak zaman aşımı değil, **her ilerleme olayında sıfırlanan** progress deadline'dır. | A5 | D |
| S6 | 13 ADR şablonunun **hiçbirinde** "gözlenmiş sonuç / karar doğru çıktı mı" alanı yoktur; hepsi karar-anı yakalama şemasıdır. | A4 | D |

Çürüyen ya da ciddi daralan iddialar bölüm 3–9'da aile aile verilmiştir. **Bu koşumun en değerli çıktısı çürüyenlerdir** — çünkü üçü doğrudan Salih'in tasarımını değiştirir (bölüm 11).

---

## 2. ÖLÇÜM — ajan donması (Carvis, yerel telemetri, N=24)

Bu bölüm atlas çıktısı değildir. Salih'in "bazı araştırma ajanları donuyor" bildirimi üzerine, **bu oturumun kendi alt-ajan transkriptleri veri seti olarak kullanılarak** ölçülmüştür. m.35 (ölçüm-öncelik) uyarınca teoriden önce koşuldu.

**Veri:** 24 alt-ajan koşumu, toplam 139 dk duvar-saati, olay-zaman damgaları JSONL transkriptlerinden.

### 2.1 Hipotez ve çürütülmesi

**H0 (Carvis'in ilk hipotezi):** Ajanlar ağ çağrılarında asılı kalıyor — proxy 403'lerine takılan `WebFetch`/`curl`.

**H0 ÇÜRÜTÜLDÜ.** Araç başına bekleme dağılımı:

| Araç | n | p50 (s) | p90 (s) | max (s) |
|---|---|---|---|---|
| WebSearch | 359 | 0,7 | 7,0 | **11,0** |
| WebFetch | 281 | 0,2 | 1,2 | **10,4** |
| Bash | 113 | 0,4 | 3,1 | **600,1** |

`WebSearch` ve `WebFetch` maksimumları ~11 saniyede tavana vuruyor — bu araçların zaman aşımı **çalışıyor**. Ağ kaynaklı asılma yok.

### 2.2 Gerçek bulgular

- **Süre ile en uzun tek duraklama arasında r = 0,95 (N=24).** Bir ajanın ne kadar sürdüğü neredeyse tamamen tek bir duraklamayla açıklanıyor — iş hacmiyle değil.
- **Verim tersine dönüyor.** Hızlı ajanlar 25–43 olay/dk üretirken yavaş ajanlar 4–11 olay/dk. En yavaş ajan (1173 s) 81 olay üretti; 105 saniyelik bir ajan 72 olay üretti. **Yavaş ajan daha çok iş yapmıyor — duruyor.**
- **Toplam duvar-saatinin %35'i, ajan başına tek bir duraklamanın içinde geçiyor** (139 dk'nın 48 dk'sı).

### 2.3 Kök neden — 60 saniyeyi aşan 18 duraklamanın ayrıştırılması

| Sınıf | Adet | Ne olduğu |
|---|---|---|
| **Gerçek patoloji** | **2** | Ajanın **kendi yazdığı bekleme döngüsü**: biri `Bash(timeout=600000)`, diğeri `for i in $(seq 1 30); do if [ -f ... ]` — yani alt-ajan çıktısını **yoklayarak (polling)** bekleme |
| Uzun üretim | 16 | Ajanın 200 KB+ raporunu yazdığı üretim süresi — patoloji değil |

**Salih'in gördüğü belirtinin tam açıklaması budur:** ajan `sleep`/yoklama döngüsündeyken süreç canlıdır, CPU'dadır, ama bağlam büyümez — çünkü gerçekten hiçbir şey üretmemektedir.

### 2.4 Eşik seçimi — maliyet-duyarlı, ve neden sezgi yanlış

| Eşik | İşaretlenen | Gerçek patoloji | Kesinlik |
|---|---|---|---|
| 60 s | 18 | 2 | **%11** |
| 120 s | 11 | 2 | %18 |
| 250 s | 5 | 2 | %40 |
| 300 s | 2 | 2 | **%100** |

"120 saniyedir çıktı yok → öldür" gibi sezgisel bir kural, **her 6 müdahaleden 5'inde sağlıklı bir ajanı öldürürdü** — üstelik tam da raporunu yazan, yani en değerli ajanları. Doğru eşik veriden çıkar.

**Ama:** pozitif örneklem **N = 2**. Bu eşiğe güvenmek için çok küçüktür. Bu, başlı başına bir ders konusudur (bölüm 11.2, oturum L4).

### 2.5 Ölçümün kendi sınırı (dürüstlük)

- 18 duraklamanın 16'sı "araç bloğu olmayan asistan olayı"nı takip ediyor. Bunlar uzun üretim OLARAK yorumlandı, çünkü bu ajanlar gerçekten çok büyük raporlar üretti. Ancak **bu veriden "uzun üretim" ile "asılı akış" ayrıştırılamaz** — ikisi de dışarıdan sessizlik olarak görünür. Bu bir **tanımlanabilirlik (identifiability)** sorunudur ve ayrıştırmak için token-düzeyi telemetri gerekir (`gen_ai.client.operation.time_per_output_chunk` — A5/32).
- N=24 tek oturumdan; koşumlar zaman-ayrık değil, aynı ağ/kota koşullarını paylaşıyor. Genellenebilirliği sınırlıdır.

---

## 3. HAKEMLİK YÖNTEMİ

m.40b v0.2 uyarınca hakem, üretici koşumların devamı DEĞİLDİR: tez ve antitez raporları Carvis tarafından **iddia+kanıt olarak** kıyaslandı, "hangisi tezdi" etiketine bakılmadan. Aşamalar arası **ham kanıt** taşındı, türetilmiş yargı taşınmadı. Antitez ajanlarına tezin yalnız **çıplak iddia listesi** verildi; gerekçe ve kaynaklar VERİLMEDİ (CoVe-Factored çıpalama freni).

**Sağlamlık ölçütü = adversaryal hayatta kalma.** Bilgili bir antitezin çürütmeyi deneyip **başaramadığı** iddia sağlam çekirdektir. Çürüyen iddia ayrı yazılır; çatışma saklanmaz.

**Hakemin kendi müdahaleleri ayrıca işaretlenmiştir** (▲ ile) — antitez ajanlarının yaptığı akıl yürütme hataları hakem tarafından yakalandığında, antitezin hükmü otomatik kabul edilmemiştir.

---

## 4. AİLE A1 — LLM kullanıcının seviyesini kestirebilir mi?

**Bu aile Salih'in öncülünü doğrudan sınar:** "sen benimle konuşmalarımdan zaten benim seviyemi tahmin edecek şekilde eğitiliyorsun."

### 4.1 Hayatta kalan çekirdek

**S1 — Kalıcı bellek altyapısı olmadan öğrenen-modeli oturumlar arası TAŞINMAZ.** [K]
Antitez ajanı bu iddianın aksini aramak için özel olarak görevlendirildi ve **bulduğu her şey iddiayı destekledi**. Üç bağımsız yönden:
- Ağırlıklar çıkarım anında donmuştur; transformer mimarisinde çağrılar arası durum saklayan yerel mekanizma yoktur. Ürünlerde "hafıza" görünen şey, her istekte geçmişin token olarak yeniden enjekte edilmesidir. (https://atlan.com/know/are-llms-stateless/ · https://www.letta.com/blog/continual-learning/)
- Öğrenme literatürü bunu açıkça yazıyor: LLM tabanlı tutor "esasen mevcut etkileşim düzeyinde çalışır, öğrenenin evrilen bilgi durumunun **kalıcı bir modelini tutmaz**". (https://arxiv.org/pdf/2512.23036)
- 2025-26 sistemlerinin (LOOM, IntelliCode, DeepTutor) tamamı bu boşluğu **dışarıdan eklenen** bellek grafiği / versiyonlu learner-state ile kapatıyor — yani altyapı gerektiğini kabul ediyorlar. (https://arxiv.org/html/2511.21037)

**Tasarım sonucu:** Seviye modeli **dosyada** yaşamalıdır. JARVIS'in kapsül/defter mimarisi bunun için zaten doğru şekildedir; eksik olan, o dosyalarda *öğrenen-durumu* tutan bir alanın olmaması.

### 4.2 Çürüyenler

| İddia | Hüküm | Gerekçe |
|---|---|---|
| "Seviye çıkarımı ancak konuşma-DIŞI davranışsal sinyalle olur" | **ÇÜRÜTÜLDÜ** | Salt metinden çalışan üç ölçüm var: 27.188 Slack mesajı (tıklama/zamanlama yok), diyalog transkriptleri (zero-shot LLaMA denetimli ModernBERT'i geçiyor), dialogue-KT (AUC ≈ 0,76). Davranışsal sinyal **gerekli değil, faydalı** — sistematik yanlılığı (uzmanı eksik/acemiyi fazla tahmin) düzeltiyor. |
| "Uyarlama ile yaranma (sycophancy) ayrıştırılamaz" | **ÇÜRÜTÜLDÜ** | Yaranmacı onay, samimi onay ve yaranmacı övgü temsil uzayında **ayrı eksenlerde** kodlanıyor ve her biri diğerlerini bozmadan bağımsız yönlendirilebiliyor; örüntü veri kümeleri ve mimariler arası tekrarlanıyor. (https://arxiv.org/html/2509.21305v1) Persona vektörleri sycophancy yönünden büyük ölçüde bağımsız. (https://arxiv.org/html/2605.21006) |

**▲ Hakem müdahalesi (antitez lehine değil):** Antitez, "uyarlama acemiye zarar verir" kısmını da çürüttüğünü iddia etti ve buna Tutor CoPilot RCT'sini dayanak gösterdi ("+9 puan düşük puanlılarda"). **Bu bir konstrükt kaymasıdır:** Tutor CoPilot'taki heterojenlik **düşük puanlı EĞİTMENLER** üzerindedir, **acemi ÖĞRENCİLER** üzerinde değil. İkisi aynı şey değildir. Ayrıca antitezin ikinci dayanağı (`innovativehumancapital.com`, 770 öğrenci) tez şeridinin zaten "hakemli değil, sektör yayını" diye bayrakladığı kaynaktır. **Hüküm: mekanizma-ayrıştırılabilirliği ÇÜRÜTÜLDÜ (sağlam kaynaklı); "acemiye zarar" kısmı ÇÖZÜLMEDİ [X].** Karşı yönde CHI 2026 deneyi duruyor: yüksek-sycophancy koşulunda ML hata ayıklama görevinde performans anlamlı düştü ve katılımcıların 17/24'ü (%71) yaranmayı fark etmedi. (https://arxiv.org/abs/2510.03667)

### 4.3 Daralanlar

- **"Seviye hiç kestirilemez" → "kaba sıralı kestirim olur, kalibre nokta-kestirimi olmaz."** Üç sınıflı (acemi/orta/uzman) ayrım metinden şans üstü çalışıyor; ama 0-100 ölçekte en iyi rapor edilen hata **MAE ≈ 21 puan**. Alanın kendi güncel işi (ExPerT, ACL 2026) metin-tek-başına yetersizliği gerekçesiyle davranışsal sinyal ekliyor.
- **"Ticari bellek yalnız olgu/tercih saklar" → çürüdü.** ChatGPT belleği doğrudan seviye beyanları saklıyor ("I'm not a developer — explain in plain language") ve konuşma geçmişinden otomatik profil sentezliyor. Ama kalıcı bellek VARKEN bile oturumlar-arası kullanıcı modellemesi konuşlandırılmış ticari sistemlerde zayıf: PersonaMem'de sınır modeller genel doğrulukta **~%50**.
- **"Naif kişiselleştirme zarar verir" → rejime bağlı.** Öznel/açık-uçlu ölçütte gerçek (denemelerin %29,0'ı jenerikten kötü; kişiselleştirilmiş yanıtların %54,6'sı insan yargısında jenerikten iyi değil). Nesnel metrikli, profil-temelli görevlerde tersi (LaMP'ta RAG +%14,92; rastgele profil belgesi enjeksiyonu bile iyileştiriyor). **Ek kritik bulgu: bu zarar LLM-yargıçla ölçüldüğünde GİZLENİYOR, yalnız insan yargısıyla görünüyor.**

### 4.4 Salih'in öncülüne hüküm

Öncülün **kısmen doğru, kritik yerde yanlış**:
- ✅ Doğru: seviyeni konuşmadan kestirme yeteneği vardır ve kaba düzeyde çalışır.
- ❌ Yanlış: bu "eğitilme" değildir — oturum içinde bağlamdan yapılan bir çıkarımdır, ve **oturumlar arası taşınmaz**.
- ⚠️ Tehlike: bu çıkarım yaranmayla karışabilir. Ayrıştırılabilir olduğu gösterilmiştir ama **kendiliğinden ayrışmaz** — tasarımla ayrılması gerekir.

---

## 5. AİLE A2 — Pasif okuma öğretir mi?

**Bu aile mevcut öğrenme protokolünü (V55 pasif-okuma modeli) sınar.**

### 5.1 Hayatta kalan çekirdek

**S2 — LLM sentezinden öğrenmek, çekirdek olgular AYNI sunulsa bile daha sığ bilgi üretir.** [K]
Melumad & Yun, *PNAS Nexus* 4(10):pgaf316 — **7 deney, n=10.462**. Antitez ajanı bunu çürütmek için arandı, karşı yönde deneysel çalışma **bulamadı**. Üstelik iddianın en kırılgan noktası deneysel olarak ayrıca test edilmiş: (a) Google ve ChatGPT sonuçlarında **özdeş olgu kümesi** sunulan koşul, (b) platform Google'da sabitlenip yalnız "AI Overview" var/yok değiştirilen koşul — ikisinde de sentezden öğrenme daha sığ. Mekanizma: sonuçların tekil kaynak bağlantıları yerine özet olarak sunulması, kullanıcının kendi keşif ve sentez etkinliğini bastırıyor.
(https://academic.oup.com/pnasnexus/article/4/10/pgaf316/8303888 · https://pmc.ncbi.nlm.nih.gov/articles/PMC12560091/)
*Kalan zayıflık:* tek araştırma ekibi, 2025, bağımsız replikasyon bulunamadı.

**Bu, bu raporun Salih için en rahatsız edici bulgusudur** — çünkü tam olarak "Carvis bana konuyu anlatsın, ben okuyayım" modelinin ölçüldüğü koşuldur.

### 5.2 Çürüyenler

| İddia | Hüküm | Gerekçe |
|---|---|---|
| "Pasif okuma, arzu edilir zorlukların hepsinin SIFIR dozudur" | **ÇÜRÜTÜLDÜ** (mutlak haliyle) | Aralıklama (spacing) okumaya uygulanabilir: **dağıtılmış** yeniden-okuma gecikmeli testte tek okumayı geçiyor, **yığılmış** geçmiyor (Rawson & Kintsch 2005). Yani "pasif okuma" bir etkinlik türü değil, bir **program parametreleri kümesidir**. İddia ancak "tek oturumda, yığılmış, tek geçişli okuma" olarak yeniden yazılırsa ayakta kalır. |
| "GenAI ürün kalitesini yükseltir ama bilgi kazanımını yükseltmez" | **ÇÜRÜTÜLDÜ** (genel haliyle) | Kestin ve ark., *Scientific Reports* 2025: 194 öğrenci, randomize crossover, aynı içerik/çalışma yaprağı/ön-son test; ölçülen **testle ölçülen bilgi**, ürün değil; AI kolu aktif-öğrenme dersini geçiyor (medyan 4,5 vs 3,5; tavana-dayanıklı 0,73–1,3 SD; p<10⁻⁸), üstelik daha kısa sürede. **Transfer ayağı ÇÜRÜTÜLEMEDİ** — orada kanıt hâlâ seyrek. |
| "Kalan meta-analizler birbirinden uzak tahminler veriyor" | **ÇÜRÜTÜLDÜ** | Geri çekilme sonrası ayakta kalanlar dar bantta: **g = 0,499 · 0,573 · 0,61 · 0,670**. Aykırı değer, geri çekilen 0,867'nin kendisiydi. Literatür geri çekilmeden sonra **daha tutarlı**, sadece daha mütevazı. |

**▲ Hakem müdahalesi — ÇÖZÜLMEMİŞ ÇELİŞKİ [X]:** Tez ve antitez şeritleri **aynı URL'ye farklı rakam atfetti**: `nature.com/articles/s41599-026-07019-z` için tez **g = 1,14**, antitez **g = 0,670**. İkisi de birincil metne inemedi. Bu rakam raporda **[X] damgalıdır ve kullanılmamalıdır**. Bu vaka, V26 denetiminin neden var olduğunun canlı örneğidir.

**Geri çekilme uyarısı (kritik):** GenAI-öğrenme literatürünün en yüksek etkili meta-analizi — Wang & Fan (2025), *Humanities and Social Sciences Communications*, 51 çalışma, öğrenme performansı **g = 0,867** — **22 Nisan 2026'da GERİ ÇEKİLDİ**. Geri çekilmeden önce ~486.000 görüntülenme, 266 atıf almıştı. Gerekçe: meta-analizde tutarsızlıklar; 51 çalışmada kalite değerlendirmesi yapılmaması; 33 çalışmada ChatGPT grubunun 35 kişiden az olması; yazarların yazışmalara yanıt vermemesi. **Bu sayı hiçbir yerde kullanılmamalıdır.** (https://www.nature.com/articles/s41599-026-07310-z)

### 5.3 Daralanlar — ve tasarımı değiştiren bulgu

**"Acemide açıklama okumak, kendi başına problem çözmeyi geçer" → CİDDİ DARALDI.** Sinha & Kapur, *Review of Educational Research* (2021) meta-analizi — 53 çalışma, 166 karşılaştırma: **önce-problem-çözme sonra-öğretim (PS-I), önce-öğretim sonra-problem (I-PS)'yi anlamlı ve orta etkiyle geçiyor.** PS-I'in hedef kitlesi tanımı gereği **henüz öğrenmemiş** öğrenendir — yani iddianın "pasif okuma önde" dediği hücrenin ta kendisi. Sınıf çalışmaları PS-I öğrencilerinin kavramsal anlama ve **transferde** doğrudan-öğretimi geçtiğini, işlemsel akıcılıktan ödün vermediğini bildiriyor. (https://eric.ed.gov/?id=EJ1308129)

Okumanın geçerli kaldığı yer daraldı: **işlemsel akıcılık + yakın transfer + zamanlanmamış tek atış.**

**"Guardrail zararı giderir" → DARALDI, ve bu kritik.** Bastani ve ark., *PNAS* 2025, ~1000 öğrenci: pratikte GPT Base kontrolden **+%48**, GPT Tutor **+%127**; yardımsız sınavda GPT Base kontrolden **−%17**, GPT Tutor kontrolle **yaklaşık AYNI**. Yani guardrail **zararı nötrler, fayda üretmez** — pratikteki %127'lik üstünlük sınava sıfır aktarılıyor.

**"Öz-açıklama + soldurma, geri-çağırmayla eş etki verir" → DARALDI.** Parite yalnız **anlık ölçüm ve yakın transfer** için savunulabilir; gecikmeli tutma ve uzak transfer için desteklenmiyor. Ayrıca karşılaştırma **iki ayrı meta-analiz arasında** yapılıyor (farklı materyal, farklı kontrol koşulu, farklı tutma aralığı) — bu bir kafa-kafaya eşitlik kanıtı değildir.

### 5.4 İki ekseni karıştırmama kuralı (hakem sentezi)

Literatürdeki iki karşılaştırma ekseni birbirine karıştırılmamalıdır:

| Eksen | Karşılaştırma | Acemide kazanan |
|---|---|---|
| **Edinim** (worked-example / expertise reversal) | okumak **vs. kendi başına didinmek** | okumak (d = 0,505 düşük ön-bilgide) |
| **Edinim** (productive failure) | okumak **vs. yapılandırılmış deneme sonra okumak** | **deneme-önce** (kavramsal anlama + transfer) |
| **Pekiştirme** (testing effect) | okumak **vs. geri-çağırmak** | geri-çağırmak (g ≈ 0,50–0,61, gecikmede) |

Salih'in pasif-okuma modeli birinci satırda haklı, ikinci ve üçüncü satırda açıktır.

---

## 6. AİLE A3 — İş-akışı içinde öğrenme ve staj bağlamı

### 6.1 Çürüyenler — üç sert hüküm

**"70-20-10 geçerli bir tasarım temelidir" → ÇÜRÜTÜLDÜ.**
Kökeni: ~200 yöneticinin **geriye dönük öz-beyanı** (CCL, *Lessons of Experience* 1988) — hem hayatta-kalan yanlılığı hem geriye-dönük beyan yanlılığı taşıyor; yuvarlak 70/20/10 sayıları ölçümden değil anekdottan geliyor. Hakemli eleştiri kesin: Clardy (2018), *Human Resource Development Review* 17:153-178 — "70-20-10 and the Dominance of Informal Learning: **A Fact in Search of Evidence**"; sonuç: **%70 kuralı bir kenara bırakılmalıdır.** Modelin kendi savunucu kurumu bile onu "reçete/oran değil, referans model" diye savunuyor. (https://journals.sagepub.com/doi/abs/10.1177/1534484318759399 · https://www.702010institute.com/5-myths-702010-reference-model/)

**"İhtiyaç anında öğrenme kalıcılığı ve transferi artırır" → ÇÜRÜTÜLDÜ.**
Fan ve ark. (2025), *BJET* 56(2):489-530, n=117, 4 kollu: ChatGPT grubu **anlık deneme skorunda üstün**, ama **bilgi kazanımı ve TRANSFER'de anlamlı fark YOK**. Bastani: erişim kaldırılınca −%17. Mekanizma: bilişsel boşaltma — bilginin sonradan erişilebilir olacağı **beklentisi** içsel kodlamayı düşürüyor. **Ayakta kalan hali: verimliliği artırır; kalıcılığı ve transferi artırmaz.**

**"Yeterli anonimleştirmeyle işveren verisi riski yönetilebilir" → ÇÜRÜTÜLDÜ — üç yönden birden.**
- *Teknik:* Staab ve ark. (ETH Zürih, **ICLR 2024**): LLM'ler serbest metinden kişisel nitelikleri **%85 top-1 / %95,8 top-3** doğrulukla çıkarsıyor, insanlara göre 100× ucuz ve 240× hızlı. Makalenin açık sonucu: *"metin anonimleştirme ve model hizalama dahil yaygın önlemler kullanıcı gizliliğini LLM çıkarımına karşı korumada halihazırda **ETKİSİZDİR**."* Takip işi (ICLR 2025): mevcut anonimleştirme araçları modern LLM'lerin de-anonimleştirme yeteneğiyle **temelden hizasız**. (https://arxiv.org/abs/2310.07298)
- *İstatistiksel:* Rocher ve ark. (2019), *Nature Communications*: 15 demografik nitelikle Amerikalıların **%99,98'i** yeniden kimliklendirilebilir; anonimleştirilmiş veri kümeleri **GDPR'ın anonimleştirme standardını karşılamıyor**. (https://www.nature.com/articles/s41467-019-10933-3)
- *Kapsam (en önemlisi):* **Anonimleştirme kişiyi gizler, İÇERİĞİ gizlemez.** İşveren verisinde korunan şey çoğu zaman kişisel veri değil **ticari sır / sözleşmesel gizlilik**tir. Kaynak kodu, marj yapısı, müşteri şeması "anonimleştirilse" de sır olmaktan çıkmaz. Standart NDA'ler türev materyalleri (notlar, analizler, özetler — **alan tarafın kendi ürettiği belgeler dahil**) açıkça kapsar.

**Ayakta kalan yol PROSEDÜREL, teknik değil:** işverenin yazılı izni + sıfır-saklama kurumsal tenant + veri sınıflandırması. "Ben iyice sansürlerim" bir kontrol değil, **yanlış güvenlik hissidir.**

**"AI asistanı bilişsel çıraklıktaki koçluk/iskele rolünü üstlenebilir" → ÇÜRÜTÜLDÜ — ve gerekçesi tasarım kısıtı.**
Bilişsel çıraklığın çekirdeği modelleme → koçluk → iskele → **SOLDURMA (fading)** → artikülasyon → keşiftir. Soldurma, koçun öğrenenin **yardımsız** performansını gözlemesini gerektirir. Bir sohbet asistanı yalnızca kendisine yapıştırılanı görür; **yardımsız performansa dair sinyali yoktur** → soldurma kararını verecek temelden yoksundur. Bu yapısal bir eksikliktir, ayar meselesi değil. Ampirik destek: Otis ve ark. (*Management Science*, Kenya saha deneyi) — YZ danışmanlığı **baştan düşük performanslılarda** yüksek performanslılara göre 0,20 SS'den fazla daha kötü etki (~%10 düşüş).

### 6.2 Cepheden saldırıya direnen: yapılandırılmış yansıtma

**AAR / yapılandırılmış debrief, bu ailenin en sağlam niceliksel çapasıdır** ve antitez onu **etkisizlik göstererek çürütemedi** — yalnız koşullarını daraltabildi.
- Tannenbaum & Cerasoli (2013), *Human Factors* 55:231-245, k=46: debrief yapan takımlar ortalama **%25** daha iyi.
- Keiser & Arthur (2021), *Journal of Applied Psychology* 106(7):1007-1032, k=61, 107 efekt, 915 takım / 3.499 birey: genel **d = 0,79**.
- İki bağımsız meta-analiz **0,67 → 0,79** aralığında yakınsıyor.

**Daraltma (antitezin başarısı):** Etki koşulludur — (i) kolaylaştırıcılı, (ii) **nesnel performans verisine** dayalı, (iii) karmaşık/belirsiz, içsel geri-bildirimi olmayan görevlerde. Meta-analitik havuz ağırlıklı olarak **takım debrief'i** (askeri, tıbbi simülasyon). "Tek kişilik, kendi kendine yazılan yansıtma günlüğü" bu havuzun temsil ettiği müdahale DEĞİLDİR; etki büyüklüğünü oraya taşımak kanıtsız bir aktarımdır. Ayrıca tekil yansıtma RCT sicili çelişkilidir (Dobronyi ve ark. 2019, n=1.356: sıfır etki; Schippers grubu 2023, n=1.134: pozitif).

**▲ Hakem notu:** Wipro "%23" rakamı (Di Stefano ve ark., "Learning by Thinking") raporda **kullanılmayacaktır** — iki nedenle: (a) hakemli nihai dergi künyesi doğrulanamadı (HBS working paper ile *Management Science* "in press" arasında çelişki), (b) ikinci yazar hakkında Harvard soruşturması araştırma suistimalinin "kasıtlı, bilerek veya pervasızca" işlendiği sonucuna vardı ve Mayıs 2025'te kadrosu iptal edildi. Bu spesifik makale geri çekilenler arasında **değildir** ve ona yönelik spesifik bir suistimal iddiası bulunamadı — ama tez bu iddiayı Keiser & Arthur üzerine kurmalı, Wipro rakamı yalnız illüstratif kalmalıdır.

### 6.3 Staj bağlamına doğrudan sonuç

Salih'in "stajda ekip liderim task verecek, ben yaparken öğreneceğim" çerçevesi için:
- ✅ **Yapılandırılmış yansıtma** ölçülmüş olarak en güçlü müdahale — ama nesnel performans verisi ve tercihen dışsal bir gözlemci gerektiriyor.
- ❌ **İşveren görevini bu sisteme taşımak prosedürel olarak kapalı** (yazılı izin olmadan). Bu, bir tercih değil bir kısıt.
- ⚠️ **Yalnızca ihtiyaç-anı öğrenme** verimlilik verir, kalıcılık vermez.
- **Dürüst boşluk:** Stajyer veri-bilimci onboarding'inde **ölçülmüş hiçbir öğrenme çıktısı bulunamadı.** Airbnb/Meta/Spotify/Shopify desenlerinin hiçbiri etkisini ölçmemiş. Bu alt-başlık dürüstçe "yalnız pratisyen kaynağı [K]" damgalıdır — ve JARVIS için bu bir zayıflık değil, **kendi katkı alanıdır**.

---

## 7. AİLE A4 — Karar-akışından ders üretimi hattı

Bu ailenin antitezi koşumun en verimlisiydi: birincil kaynaklara inerek **tez şeridinin dört iddiasını çürüttü**.

### 7.1 Hayatta kalan çekirdek

**S3 — Halüsinasyonlu içerik bir kez öğrenildiğinde düzeltme etkiyi TAMAMEN silmez.** [K]
Antitez bunu çürütmeye çalıştı, **çürütemedi**; dört bağımsız kaynak aynı yöne:
- Walter & Tukachinsky (2020) meta-analizi, 32 çalışma, N=6.527: *"correction does not entirely eliminate the effect of misinformation."*
- Chan ve ark. (2017) meta-analizi, 52 çalışma, N=6.878.
- Ecker hattı: nedensel alternatif sunmak azaltıyor ama *"elimination of the CIE appears to be more of an exception than the norm."*
- Butler & Roediger (2008): geri-bildirimle yanlış bilgi %20'den ~%10'a **yarıya iniyor — sıfırlanmıyor.**

**Daraltma (antitezin başarısı):** "Kalite kapısı üretim anında olmak **zorunda**" ifadesi literatürden çıkmıyor; artık etki *azaltılabilir* (nedensel alternatif + geri-bildirim + önceden test). Doğru ifade **normatif değil ekonomiktir**: *artık etki sıfırlanamadığı için üretim-anı kapısı en ucuz noktadır.*

**S4 — Ajan-belleği satıcı rakamları kıyaslanamaz.** [D]
Zep/Mem0 anlaşmazlığı açık ve çözülmemiş: Zep %84 → Mem0'ın düzeltmesi 58,44% ± 0,20 (10 koşum) → Zep'in karşı-iddiası 75,14%. İhtilaf noktaları (adversarial kategori dahil mi, yalnız-Zep sistem promptu, SDK sürüm farkı) protokolce şart koşulmamış. LoCoMo altın anahtarının **%6,4'ü hatalı**. Birincil kaynaktan (açık GitHub issue) doğrulandı. (https://github.com/getzep/zep-papers/issues/5)
**Daraltma:** Kusur büyük ölçüde **LoCoMo'ya özgüdür**; LongMemEval elle küratörlendi ve değerlendirici 3 uzman anotatörle >%97 uyum gösteriyor. Tek harness altında kıyaslanabilirlik geri geliyor.

**S6 — 13 ADR şablonunun HİÇBİRİNDE "gözlenmiş sonuç / karar doğru çıktı mı" alanı yoktur.** [D]
Üç şablon metni (Nygard, Tyree-Akerman, MADR) doğrudan okundu. MADR'ın "Consequences" alanı karar anında **beklenen** sonuçtur; "Confirmation" uyum denetimidir (fitness function/ArchUnit), retrospektif öğrenme değil. **Hepsi karar-ANI yakalama şemasıdır.**
**Bu, Salih'in kuracağı hattın literatürde karşılığı olmayan parçasıdır** — ve öğrenme oturumlarının besleneceği alan tam olarak budur.

### 7.2 Çürüyenler — ikisi Carvis'in önceki ifadesini düzeltir

| İddia | Hüküm | Gerekçe |
|---|---|---|
| "ADR şeması kanoniktir, yakınsama var" | **ÇÜRÜTÜLDÜ** | Tek listede **13 birbirine indirgenemez şablon**; alan sayıları uyumsuz (Nygard 4 bölüm, Tyree-Akerman 14 alan, MADR 7 bölüm + 4 varyant). Ortak kesişim yalnız "Decision/Status". MADR'ın kendi CHANGELOG'unda breaking rename'ler var. `adr-tools`'un MADR desteği PR'ı **merge edilmedi**. MSR çalışması: ADR kullanan repoların ~%50'sinde yalnız 1-5 ADR var — "denendi, benimsenmedi". |
| **"LLM'in ürettiğini LLM'e doğrulatmak reddedilmiştir"** | **DARALTILDI — Carvis düzeltmesi** | Reddedilen şey dar: **intrinsic** self-correction (aynı model, aynı bağlam, **dışsal referans YOK**, akıl yürütme görevi — Huang ve ark., ICLR 2024). Reddedilmeyen ve ölçülmüş olarak işleyen üçü: (a) LLM yargıcıyla materyal **filtreleme** (AlpaGasus: 52k→9k filtrelenmiş veri tam-veriyi geçti), (b) **ayrı doğrulayıcı geçişi** (CriticGPT: insan+model ekibinin eleştirisi yalnız-insana %60+ oranda tercih edildi; generator-verifier ayrımı ~%20 kazanç), (c) **referansa dayalı** doğrulama. **Karar defterinden ders üretiminde doğrulayıcının elinde karar kaydı vardır — bu intrinsic self-correction DEĞİLDİR.** |
| **"LLM-as-judge zayıf korelasyonlu (r≈0,31), kalite güvencesi değildir"** | **ÇÜRÜTÜLDÜ — Carvis düzeltmesi** | MT-Bench resmî deposu [D]: 3.3K insan anotasyonu üzerinde *"humans and GPT-4 judge achieve **over 80% agreement, the same level of agreement between humans**"*. Sağlık alanı derlemesinde 13 çalışmada yargıç-uzman korelasyonu **0,40–0,94, medyan 0,69**. **r≈0,31 rakamının künyesi iki bağımsız aramada hiçbir çalışmaya bağlanamadı.** |
| "LLM üretimi kartların SR döngüsündeki öğrenme çıktısı hiç ölçülmedi" | **ÇÜRÜTÜLDÜ** | En az dört ölçüm var (N=60 Anki+AI mnemonic, 4 tekrar seansı; N=73 randomize, 7 haftalık tutma; ~60 öğrenci quasi-deneysel %89 vs %73; MOOC çalışması). **Ama ikinci yarı ayakta:** kanıt tabanı küçük-N (20-73), ağırlıkla quasi-deneysel, ağırlıkla kelime/EFL, 2-7 hafta ufuklu, ön-kayıtlı büyük RCT yok. Doğru formülasyon: *"ölçülmedi" yanlış; "yeterince güçlü ölçülmedi" doğru.* |
| "Batch VEYA cache — maliyet avantajı garantili değil" | **DARALTILDI** | Anthropic dokümanı birebir [D]: *"The pricing discounts from prompt caching and Message Batches **can stack**."* Batch **%50 indirim garantili taban** (hem giriş hem çıkış). İddianın iki çekirdeği yine de doğrulandı: batch içi cache isabeti **best-effort (%30–98)** ve **stateful ajan oturumu batch indirimini yapısal olarak kaybediyor** (*"Sessions are stateful and interactive. There is no batch mode."*) + saatlik runtime ücreti. |

### 7.3 LLM-yargıcın doğru kullanımı (hakem sentezi)

Çürüme ve daralmalar birleştirildiğinde net bir tasarım kuralı çıkıyor:

| Görev | Yargıç performansı | Kullan? |
|---|---|---|
| "Bu içerik bozuk mu?" — önceden tanımlı kusur tipi tespiti | %94+ doğruluk | ✅ evet |
| Tercih/sıralama karşılaştırması | insan-insan uyumu seviyesinde (>%80) | ✅ evet |
| Referansa karşı olgusal doğrulama (kaynak metin elde) | reddedilen tasarım değil | ✅ evet |
| "Bu içerik ne kadar iyi?" — açık uçlu, çok boyutlu, öznel rubrik | r = 0,13–0,48 | ❌ hayır |
| Kendi ürettiğini, referanssız, akıl yürüterek düzeltmek | doğruluğu **düşürüyor** | ❌ asla |

**Kural: yargıç bir kalite GÜVENCESİ değil, rubrik-bağımlı bir ölçüm aracıdır; her rubrik için ayrı kalibre edilmelidir.**

---

## 8. AİLE A5 — Ajan asılması: kök nedenler ve saptama

> ⚠️ **PROTOKOL EKSİĞİ (dürüstlük):** Bu ailenin **Aşama 2 (antitez) koşumu YAPILMAMIŞTIR** — oturum limiti nedeniyle. m.40b v0.2 üç aşamayı zorunlu kılar. Aşağıdaki bulgular tez şeridinden gelir ve adversaryal sınamadan **geçmemiştir**. Bulguların çoğu resmî dokümantasyondan [D] olduğu için olgusal risk düşüktür; ama **yorum ve öneri katmanı sınanmamıştır.** Antitez borcu bölüm 12'de kayıtlıdır.

### 8.1 Kanonik ayrım: canlılık ≠ ilerleme

Kubernetes dokümanı sorunun adını koyuyor [D]: liveness probe *"could catch a **deadlock, where an application is running, but unable to make progress**."* Ama probe mekanizmalarının tümü (`exec`/`grpc`/`httpGet`/`tcpSocket`) **dışarıdan yapılan sorgulardır** — iş döngüsü asılıyken ayrı bir HTTP dinleyicisi yanıt verdiği sürece BAŞARILI dönerler.

**Doğru primitif: progress deadline.** Kubernetes `progressDeadlineSeconds` (varsayılan **600**) aşıldığında `reason: ProgressDeadlineExceeded` yazar — ve kritik nokta: **öldürmez, görünürlük üretir.**

Temporal'ın tez cümlesi [D]: *"Heartbeating is best thought about **not in terms of time, but in terms of 'How do you know you are making progress?'**"* Ve heartbeat aynı zamanda **iptal kanalıdır**: *"Activities that don't Heartbeat can't receive a Cancellation."* — heartbeat'siz iş yalnız saptanamaz değil, **durdurulamaz** da.

### 8.2 Bizim ortamımızda ne var (hepsi [D])

| Mekanizma | Değer | Not |
|---|---|---|
| `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS` | **600.000 ms (10 dk)** | *"The timer **resets on each streaming progress event**"* → doğru primitif. Aşınca alt-ajan **iptal edilir, görev başarısız işaretlenir, kısmi sonuç ebeveyne verilir.** **SINIR: senkron alt-ajanlara UYGULANMAZ.** |
| `CLAUDE_ENABLE_STREAM_WATCHDOG` | varsayılan **açık** | *"aborts the request when **headers have arrived but the response body stops streaming**"* — 200 sonrası sessizleşen akış vakası. |
| `API_FORCE_IDLE_TIMEOUT` | **5 dk** gövde-idle | Doğrudan Anthropic/AWS'de pasif (orada bayt-düzeyi nöbetçi var). |
| `BASH_DEFAULT_TIMEOUT_MS` / `BASH_MAX_TIMEOUT_MS` | **120.000 / 600.000** | **Ölçtüğümüz 600 s duraklamanın kaynağı:** ajan Bash zaman aşımını izin verilen **tavana** ayarlamış. |
| `MCP_TOOL_TIMEOUT` | **100.000.000 ms ≈ 28 saat** | Mutlak zaman aşımı pratikte YOK. Asılmayı yakalayan ayrı mekanizma: `CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT` (ağ 300 s / stdio 1.800 s) — *"no response and no progress notification"*. |
| `CLAUDE_CODE_RETRY_WATCHDOG=1` | 429/529'u **SÜRESİZ** dener | *"Retries 429 and 529 capacity errors **indefinitely**"*, 5 dk'ya kadar geri çekilir. **Kota tükenince ajan ölmez, bekler.** |
| `CLAUDE_CODE_MAX_RETRIES` | varsayılan **10** | Resmî formül: en kötü hal ≈ `API_TIMEOUT_MS × (MAX_RETRIES+1)` + backoff = **~110 dakika**, tek çağrı, sıfır çıktı. |

**▲ Çelişki [X]:** `CLAUDE_STREAM_IDLE_TIMEOUT_MS` iki resmî sayfada farklı anlatılıyor — Agent SDK sayfası tek değer (300.000, minimuma sabitlenmiş) derken, env-vars sayfası iki-değerli mimari tarif ediyor (event-düzeyi 300 s / bayt-düzeyi 180 s, ikincisi 5-dk sabitlemesine tabi değil). Çözülmedi.

### 8.3 Ekosistemin fiilî çözümleri

- **LangGraph:** döngüyü **saptamaz, sayarak sınırlar** — `DEFAULT_RECURSION_LIMIT = 25`, aşımda `GraphRecursionError` (*"This prevents infinite loops"*). Aynı desen Agent SDK'da `max_turns` + `error_max_turns` / `error_max_budget_usd` başarısızlık sınıfları.
- **Celery:** Redis `visibility_timeout` varsayılanı **3600 s**; dokümanın kendi caveat'i: fencing yoksa *"it will be executed **again, and again in a loop**"* — tek asılı iş sistemik döngüye dönüşüyor.
- **CI dünyası ayrışıyor:** CircleCI'da `no_output_timeout` **var** (varsayılan 10 dk). **Buildkite'ta ve GitHub Actions'ta YOK** — yalnız mutlak sınırlar (GHA hosted job 6 saat). Yani GHA'da sessizce asılı bir iş **6 saat boyunca "çalışıyor" görünür.**
- **OpenTelemetry GenAI:** ajan metrikleri tanımlı (`gen_ai.invoke_agent.tool_calls`, `...inference_calls`, `gen_ai.client.operation.time_to_first_chunk`, `...time_per_output_chunk`) ama hepsi **Recommended**, ve **hazır bir "agent stalled" sinyali TANIMLI DEĞİL** — türetmek zorundasın.

### 8.4 Ölçümle birleştirilmiş kök-neden hükmü

Bölüm 2'nin ölçümü + A5'in dokümantasyonu birleştiğinde, **bizim ajanlarımızın donma nedeni üç katmanlıdır**:

1. **Ajan-yazımı bekleme döngüsü (ölçüldü, 2 vaka).** Ajan alt-ajanlarını `Bash` ile yokluyor; Bash tavanı 600 s olduğu için async stall watchdog'un 600 s'lik penceresine **tam olarak sığıyor ve tetiklenmiyor.** Bu, watchdog'un kör noktasıdır.
2. **Kota tükenişi (bu oturumda canlı yaşandı).** Retry watchdog 429/529'u süresiz denediği için ajan ölmüyor, bekliyor. Beş atlasın "failed" dönmesi bunun sert halidir; yumuşak hali sessiz bekleme.
3. **Senkron alt-ajan boşluğu.** Stall watchdog **yalnız async** alt-ajanlara uygulanıyor. Senkron çağrılan bir alt-ajan asılırsa onu kesen ilerleme-tabanlı bir mekanizma yok.

---

## 9. AİLE A6 — Asılma saptamasının istatistiksel çerçevesi

> ⚠️ **PROTOKOL EKSİĞİ:** Bu ailenin de **Aşama 2 (antitez) koşumu YAPILMAMIŞTIR** (oturum limiti). Tez şeridi kendi en kırılgan üç noktasını işaretlemiştir (A6-17 dağılım ailesi çelişkisi · A6-34 Elkan eşik uyuşmazlığı · A6-6 sansür yanlılığının yönü) — antitez öncelikle oraya bakmalıdır.

Bu aile, Salih'in "DS bakışıyla çöz ve oturumlaştır" isteğinin **müfredat gövdesidir**. Beş bağımsız şerit aynı çekirdeğe indi: **sabit bir zaman-aşımı sayısı, süre dağılımının hazard fonksiyonu hakkındaki örtük bir iddiadır.**

### 9.1 Sansürleme — ve bizim kendi tuzağımız

**Hâlâ koşan iş = sağdan sansürlü gözlem.** lifelines dokümanı [D] hatayı adıyla koyuyor: *"A common mistake data analysts make is choosing to ignore the right-censored individuals."* Ve ikinci cümle daha az bilinir: sansürlüleri **dahil edip mevcut sürelerini gerçek süre saymak da** ortalamayı düşük gösterir. İki farklı yanlış, aynı yöne.

scikit-survival [D]: sansür altında naif tahminci yalnız yanlı değil, **tanımsız** — *"the numerator is not always defined."* Pratik karşılığı: *"şu ana kadar hiç 3 saati geçen iş görmedik"* cümlesi, gözlem pencereniz 3 saatse **hiçbir bilgi taşımaz.**

**▲ En tehlikeli nokta — bizim için:** Bir işi "çok uzun sürdü" diye öldürüyorsan, sansürleme **olayla ilişkilidir (informative censoring)**. O zaman Kaplan-Meier tahminin yanlıdır ve **kendi timeout politikan kendi verini kirletir.** Bu bir geri-besleme döngüsüdür: eşik veriyi üretir, veri eşiği belirler. Bölüm 2'deki ölçümümüz bu tuzağa **henüz düşmedi** çünkü hiçbir ajanı öldürmedik — ama bir watchdog kurar kurmaz düşeriz.

### 9.2 "Yeterince bekledik, artık bitmek üzeredir" — matematiksel olarak TERS

Ortalama kalan süre E[T−t | T>t], atlas'ın kendi sayısal hesabıyla [D-hesap]:

| Dağılım | t=1 | t=5 | t=10 | t=50 |
|---|---|---|---|---|
| Üstel (ort.=1) | 1,00 | 1,00 | 1,00 | 1,00 |
| Weibull k=0,5 (azalan hazard) | 4,00 | 6,47 | 8,33 | 16,14 |
| Weibull k=2 (artan hazard) | 0,38 | 0,10 | 0,05 | — |
| Lognormal σ=1,5 | 4,75 | 9,47 | 14,00 | 40,60 |
| Pareto α=1,5 | 2,00 | 10,00 | 20,00 | 100,00 |

Pareto'da MRL = t/(α−1), yani **yaşla doğrusal artar**: 10 dakikadır koşan işin beklenen kalan süresi 20 dakika; 50 dakikadır koşanınki 100 dakika. Üstelde hiç değişmez (hafızasızlık). Yalnız artan-hazard'da düşer.

**Sonuç: "bu kadar bekledik, bitmesine az kaldı" sezgisi ağır-kuyruklu dağılımlarda yanlıştır — beklemek işi bitmeye yaklaştırmaz, uzaklaştırır.**

### 9.3 Yeniden başlatma ne zaman kazandırır

Atlas'ın sayısal optimizasyonu [D-hesap], sıfır restart maliyetiyle:

| Dağılım | restart'sız ort. | τ* (kesme) | hızlanma | CV |
|---|---|---|---|---|
| Üstel(1) | 1,000 | →∞ | **1,00** (nötr) | 1,00 |
| Weibull k=2 (IFR) | 0,886 | →∞ | **1,00** (zararlı) | 0,52 |
| Lognormal σ=1,5 | 3,080 | 0,349 | **2,42** | 2,91 |
| Pareto α=1,5 | 3,000 | 3,418 | **1,32** | ∞ |

**Reuveni ölçütü [K]: CV > 1 ise restart faydalıdır.** Tablonun CV sütunu bu ölçütle uyumlu — iki bağımsız yol yakınsıyor. *Sınır:* ölçüt Poissonian restart için ifade edilmiştir, tablo deterministik kesme kullanıyor; CV>1 **yeterli** koşuldur, gerek değil.

**Dağılımı hiç bilmiyorsan:** Luby, Sinclair & Zuckerman (1993) evrensel dizisi (1,1,2,1,1,2,4,…) sabit çarpan farkıyla optimaldir. **Ne kırar:** tekrar denemenin **bağımsız bir örneklem** çektiğini varsayar. Deterministik bir işi (aynı girdi, aynı hata) restart etmek yeni çekiliş üretmez — garanti çöker. **Bizim vakamızda bu kritik:** proxy 403'ü deterministiktir, restart onu çözmez.

### 9.4 Ortalama neden yasak, kuyruk neden zor

- **Fan-out yükseltmesi:** N=100 yaprağa dağılan istekte her yaprağın %1 olasılıkla >1 s sürmesi, isteklerin **~%63'ünün** >1 s sürmesi demektir. (Atlas kendi aritmetiğiyle doğruladı: 1 − 0,99¹⁰⁰ = 0,634.) *Varsayım:* bağımsızlık — ortak kaynak varsa gerçek kuyruk daha kötüdür.
- **Coordinated omission [D]:** kapalı-döngü ölçüm (yanıtı bekle-sonra-gönder) yapan ölçerler, **tam da sistem tıkandığı anlarda** ölçüm yapmayı bırakır; p99 yapay olarak iyi görünür. Yani **asılma sinyali ölçüm metodolojisi tarafından silinir.** wrk2/HdrHistogram bunun için ayrı düzeltme sunuyor.
- **Prometheus `histogram_quantile` [D]:** kova içi düzgün dağılım varsayar; kuyrukta bu neredeyse hiç doğru değildir.

### 9.5 Eşik = hangi hatayı sert kısıtladığın sorusu

- **PR eğrisi, ROC değil.** Asılı iş nadirdir; N ≫ P iken mutlak yanlış-pozitif sayısındaki büyük artış FPR'yi kıpırdatmaz ama precision'ı boğar. ROC bu rejimde **sistematik iyimser yanılsama** üretir.
- **Maliyet-duyarlı Bayes eşiği:** p* = C_FP / (C_FP + C_FN). **▲ Çelişki [X]:** scikit-learn'ün kendi örnek dosyası C_FN=5, C_FP=1 için "1/5" diyor; türetme **1/6 = 0,167** veriyor. Elkan'ın PDF'i bloke olduğu için çözülemedi — **bayraklı bırakıldı, sessizce uzlaştırılmadı.** *Formülün şartı:* skorun **kalibre edilmiş posterior olasılık** olması. Birkaç düzine koşumla kalibrasyon eğrisi çizilemez.
- **Neyman-Pearson alternatifi:** bir hata tipini **sert kısıtla** ("sağlıklı ajanı yanlışlıkla öldürme oranı ≤ %1"), diğerini minimize et — hiçbir parasal maliyet bilmene gerek kalmaz. **Amazon Builders' Library'nin p99.9 kuralı fiilen budur** (α = 0,001). Sektör pratiği ile kuram arasındaki köprü burasıdır.

### 9.6 Küçük-N — bizim N=24'ümüzün hükmü

Atlas'ın kendi hesabı [D-hesap]: **n=30 ile p95 için geçerli bir dağılımdan-bağımsız %95 güven aralığı KURULAMAZ** (gerekli sıra-istatistiği aralığı örneklem dışına taşıyor). Örneklem maksimumunun beklenen kuantil düzeyi n/(n+1) = 0,9677; n=30'da maksimumun gerçek p95'i aşma güveni yalnız **%78,5**, p99 için **%26,0**.

Simülasyonla tahmincinin kendi saçılımı (lognormal σ=1, gerçek p95 = 5,18):

| n | ampirik p95'in %95 aralığı | genişlik / gerçek |
|---|---|---|
| 30 | [2,46 · 9,22] | **1,30** |
| 100 | [3,39 · 7,51] | 0,80 |
| 300 | [4,01 · 6,52] | 0,49 |

**Bizim N=24 ölçümümüz için hüküm: bölüm 2.4'teki "300 s eşiği %100 kesin" sonucu bir KURAL DEĞİL, bir GÖZLEMDİR.** Pozitif örneklem N=2; bu eşiği kanona yazmak istatistiksel olarak savunulamaz. Bootstrap da kurtarmaz — scipy'nin kendi dokümanı uç sıra-istatistikleri için dejenerasyon uyarısı veriyor.

**Elde kalan üç meşru seçenek:** (a) daha ılımlı kuantil (p80-p90) + emniyet payı; (b) parametrik kuyruk modeli takıp ekstrapole et (dağılımdan-bağımsızlığı fazladan varsayıma takas edersin — ve dağılım ailesi tartışmalıdır [X]); (c) **Neyman-Pearson çerçevesi + veri toplamaya devam.**

---

## 10. AİLE A7 — Role adanmış ajan kurmak

> ⚠️ **PROTOKOL EKSİĞİ:** Aşama 2 (antitez) koşulmadı — oturum limiti. Bulguların çoğu resmî dokümantasyondan [D]; yorum katmanı sınanmamıştır. Ayrıca bu ailenin kendi 4 alt-şeridinden ikisi (fine-tuning maliyeti · insan-onay kapısının ölçülmüş etkisi) limit nedeniyle kapatılamadı.

### 10.1 "Ajanı eğitmek" ne demek — merdiven ve fiyatı

Claude ekosisteminde **fine-tuning pratikte kapalıdır**: yalnız Amazon Bedrock üzerinden ve yalnız Claude 3 Haiku için genel kullanıma açıldı [K]. Yani "adanmış ajan eğitmek" ağırlık güncellemesi anlamına **gelmiyor**; prompt / beceri / araç-kısıtı / hafıza katmanında kalıyor.

Merdivenin fiyatı [D]:

| Basamak | Bağlam maliyeti | Not |
|---|---|---|
| Beceri metadata (Seviye 1) | **~100 token/beceri**, HER ZAMAN yüklü | tetikleyici burada yaşar |
| Beceri gövdesi (Seviye 2) | **<5k token**, yalnız tetiklenince | SKILL.md <500 satır şartı |
| Kaynak dosya/script (Seviye 3) | okunana dek **sıfır** | script çalışırsa kod değil yalnız çıktı bağlama girer |
| Alt-ajan tanımı | ayrı bağlam penceresi | `tools` / `disallowedTools` / `model` / `permissionMode` / `maxTurns` / `memory` |

**Kalıcı role adanmış ajan için hazır mekanizma var [D]:** alt-ajan tanımında **`memory:`** alanı — konuşmalar arası yaşayan bir dizin (`user`/`project`/`local` kapsamı). Etkinleşince sistem promptuna `MEMORY.md`'nin **ilk 200 satırı veya 25KB'ı** enjekte edilir. Doküman `project` kapsamını öneriyor (versiyon kontrolüyle paylaşılabilir). **Ana oturumun hafızası alt-ajana YÜKLENMEZ** — ayrı dizindir.

**Bu, A1/S1'in doğrudan uygulamasıdır:** öğrenen-modeli modelin hafızasında değil, dosyada yaşamalıydı — mekanizma bu.

### 10.2 Talimat ≠ zorlama [D]

Anthropic açıkça yazıyor: CLAUDE.md içeriği sistem promptunun parçası olarak değil, **sistem promptundan sonra bir kullanıcı mesajı** olarak iletilir; Claude uymaya çalışır ama **"kesin uyum garantisi yoktur"**, özellikle belirsiz veya çelişkili talimatlarda. Çelişkili iki kural varsa "Claude birini keyfî seçebilir." Dosya başına **200 satır hedefi** — "daha uzun dosyalar daha çok bağlam tüketir ve **uyumu düşürür**."

**Mutlaka çalışması gereken şey için doğru katman prompt değil, `PreToolUse` hook'u veya `permissions.deny`'dır** — bunlar "istemci tarafından, Claude ne karar verirse versin" uygulanır.
*(JARVIS'te bu zaten yapılmış: `core/` yazımı settings-deny + `pretool-core-tel.sh` ile yapısal kilitli. A7 bu tercihi bağımsız olarak doğruluyor.)*

### 10.3 Rol/persona atamanın ölçülmüş etkisi — [X] ÇELİŞKİ

**KARŞI kanıt [D], yazar deposundan okundu:** Zheng, Pei, Logeswaran, Lee, Jurgens — **162 rol** (6 kişilerarası ilişki tipi × 8 uzmanlık alanı), **4 LLM ailesi**, **2.410 olgusal soru**. Yazarların kendi ifadesi: *"sistem promptlarına persona eklemek, persona eklenmeyen kontrol koşuluna kıyasla model performansını **artırmıyor**."* Dahası: soru-başına *en iyi* personayı toplulaştırmak doğruluğu artırıyor, ama en iyi personayı **otomatik bulmak** çoğu zaman rastgele seçimden iyi değil — yani **her personanın etkisi büyük ölçüde rastlantısal**.
(https://raw.githubusercontent.com/Jiaxin-Pei/Prompting-with-Social-Roles/main/README.md)

**LEHTE kanıt [K], aynı derecede sert:** Kong ve ark., NAACL 2024, "Better Zero-Shot Reasoning with Role-Play Prompting" — ChatGPT'de AQuA **%53,5 → %63,8** (+10,3 puan), Last Letter **%23,8 → %84,2** (+60,4 puan).

**▲ Hakem yorumu (doğrulanmadı [?]):** İki çalışma aynı manipülasyonu ölçmüyor olabilir. Karşı-kanıttaki müdahale **kimlik-atamadır** ("Sen bir doktorsun") ve **olgusal QA**'da ölçülüyor; lehteki müdahale **çok-cümleli, göreve özgü, akıl yürütmeyi yönlendiren sahne kurulumudur** ve **muhakeme** benchmarklarında ölçülüyor. İkisini aynı protokolle karşılaştıran kontrollü deney **bulunamadı**.

**Anthropic'in kendi iddiası dikkat çekici biçimde dar [D]:** *"Sistem promptunda rol belirlemek Claude'un **davranışını ve tonunu** kullanım durumunuza odaklar."* — *doğruluk* veya *görev başarısı* iddiası YOK. Bu, karşı-kanıtla çelişmiyor; onu destekliyor.

### 10.4 Çoklu-ajan: kazanç var, ama neyin kazancı belirsiz

**[K]** Anthropic'in iç değerlendirmesinde lider-Opus + Sonnet alt-ajanlar kurulumu tek-ajan Opus'u **%90,2** geçmiş. Maliyet: normal sohbetin **~15 katı token**.

**▲ [X] Bu rakam tek başına yanıltıcıdır.** Aynı kaynağın ikinci bulgusu: BrowseComp'ta **token kullanımı tek başına performans varyansının %80'ini** açıklıyor. İkisi birlikte okunduğunda kazancın büyük kısmı rol uzmanlaşmasından değil **15× daha fazla token harcamaktan** geliyor olabilir. **Token-eşitlenmiş tek-ajan karşılaştırması BULUNAMADI.** Bu, A7'nin en kritik boşluğudur ve "şirkete ajan atayalım" kararının ROI'sini doğrudan belirsizleştirir.

**MAST — başarısızlıklar rastgele değil, sistematik [D depo / K taksonomi]:** 7 çerçeve, 1000+ etiketli koşum izi. **14 başarısızlık modu, 3 kategori:** spesifikasyon/tasarım **%41,8** · ajanlar-arası hizasızlık **%36,9** · doğrulama **%21,3**. Etiketleyiciler arası Cohen κ = 0,88.
**Okunuşu: başarısızlıkların çoğunluğu koordinasyon değil, SPESİFİKASYON kaynaklı — yani mimariyi değiştirmek çözmez, görev tanımını düzeltmek çözer.**

**Anthropic'in kendi kapı kuralı [D] — "ana konuşmayı kullan" koşulları:** görev sık gidip-gelme/iteratif iyileştirme gerektiriyorsa · aşamalar önemli bağlam paylaşıyorsa · hızlı hedefli değişiklikse · gecikme önemliyse. Ve: *"Yeniden kullanılabilir prompt/iş akışı istiyorsanız, izole alt-ajan bağlamı yerine ana konuşmada çalışan **Skills**'i düşünün."*

### 10.5 Bağlam izolasyonu — iki yüzü birden

**Kazanç [D]:** yayımlanmış simülasyonda alt-ajan **6.100 token** dosya okudu, ana bağlama **420 token** döndü → ana pencerede ~**5.680 token** tasarruf.

**▲ Genelde alıntılanmayan masraf [D-türev]:** aynı simülasyonda alt-ajanın kendi başlangıç yükü **3.790 token** (sistem promptu 900 + CLAUDE.md 1.800 + araç/beceri 970 + görev promptu 120) — iş başlamadan önce, ve bu ana oturumdakinin **tekrarıdır**. Kaba denge **5.680 / 3.790 ≈ 1,5:1**.
**Sonuç: izolasyon ANA PENCEREYİ korur, TOPLAM token'ı değil — ve kısa görevlerde başabaş noktasının altında kalır.**

**İzolasyonun gerekçesi ampirik [K]:** Chroma "Context Rot" — 18 sınır model, hepsi girdi uzunluğu arttıkça kötüleşiyor; NIAH'ta 10k→100k+ arasında %20-50 doğruluk düşüşü. Çarpıcı ayrıntı: modeller **karıştırılmış haystack'te mantıksal olarak tutarlı belgeye göre daha iyi** performans gösterdi — 18 modelin hepsinde.

**İzolasyonun bedeli açıkça yazılı [D]:** *"Her alt-ajan taze, izole bir bağlam penceresiyle başlar. Konuşma geçmişinizi, çağırdığınız becerileri veya Claude'un okuduğu dosyaları **görmez**."* Yani izolasyon = kirlenmeden korunma **+** devraldığı bilgiden yoksunluk, aynı madalyonun iki yüzü.

### 10.6 Kalıcı ajanın riskleri

**Bellek zehirlenmesi ölçülmüş ve oranlar yüksek [K]:**
- MINJA (NeurIPS 2025): saldırgan hafıza deposuna **doğrudan erişmeden, yalnız sorgu göndererek** zehirliyor — **%98,2 enjeksiyon başarısı, %76,8 saldırı başarısı**.
- AgentPoison (NeurIPS 2024): **%0,1'den az** zehirleme oranıyla ortalama **>%80** saldırı başarısı; iyi-niyetli performansta **%1'den az** düşüş — **yani fark edilmiyor.**

**Hafıza dosyası şişerse SESSİZCE KIRPILIR [D]:** yalnız ilk **200 satır / 25KB** yüklenir; ötesi yüklenmez. Bu, kalıcı ajanın en sinsi hata kaynağıdır — ajan "hatırlıyorum" sanır, hatırlamaz.
*(JARVIS bağlantısı: K-019'un boyut-izleme kuralı ve m.34 damıtma tam olarak bu sorunu hedefliyor. Ajan hafızası kurulursa aynı disiplin oraya da uygulanmalı.)*

**Kendi işini denetleyen ajan iyimserlik yönünde sapıyor [K]:** *"Modeller kendi işlerini notlandırırken güvenilir biçimde pozitife sapar... Bunun meets-the-bar sinyali ayrı bir kaynaktan gelmezse, **%30 tamamlanmışken tam güvenle teslim eden ajan** elde edersiniz."*
**Bu, öğrenme ajanının kendi dersini onaylayamayacağının İKİNCİ bağımsız gerekçesidir** (birincisi A4/S3: yanlış öğrenilen silinmiyor).

### 10.7 "Eğitim"in operasyonel karşılığı: Claude A / Claude B döngüsü [D]

Anthropic'in tarif ettiği somut yöntem — ve bu, Salih'in "bir ajanı böyle eğitiriz" cümlesinin gerçek karşılığıdır:

1. Bir Claude örneğiyle (**A**) beceriyi/rolü tasarla.
2. **Taze** bir örnek (**B**) onu gerçek işte kullanır.
3. B'nin **gözlenen davranışı** A'ya geri taşınır.
4. *"İyileştirmeleri varsayımlara değil, **gözlenen ajan davranışına** dayandırır."*

İzlenecek sinyaller listelenmiş: beklenmedik keşif sırası · takip edilmeyen referanslar · aynı dosyanın tekrar tekrar okunması · hiç erişilmeyen içerik.

**Eval disiplini [D]:** *"Kapsamlı dokümantasyon yazmadan ÖNCE değerlendirmeler oluşturun"* · en az **3 senaryo** + baseline ölçümü · "Haiku, Sonnet ve Opus ile test edildi" şartı · **"Bu değerlendirmeleri koşmanın yerleşik bir yolu şu anda YOK; kullanıcılar kendi sistemlerini kurar."**
Kabul kararı için ölçek ayrı [D]: *"Hacmi kaliteye göre önceliklendirin"* — örnek ölçekler 100–1.000 vaka. Ve: *"genelde **üreten modelden farklı bir modelle** değerlendirmek en iyi pratiktir."*

**Küçük-N tuzağı [K]:** Evan Miller (Anthropic, 2024), "Adding Error Bars to Evals" — eval sorularının kümelenmesi göz ardı edildiğinde gerçek standart hata naif standart hatanın **3 katından fazla** olabiliyor. Küçük N'de görülen "fark" çoğu zaman gürültüdür. Öneri: **eşleştirilmiş fark testi**.

**▲ Hakem sentezi [?]:** Bir kişilik şirket-simülasyonunda 100 vaka gerçekçi değilse, tek meşru yol A/B'yi **eşleştirilmiş** koşmaktır (aynı karar-akışı girdisi, ajanlı ve ajansız) ve **tek koşumdan sonuç çıkarmamaktır**. Bu bir çıkarımdır, ölçülmüş eşik değil.

---

## 11. AİLE A8 — Kaynak kategorizasyonunda optimum sayı

> ⚠️ Aşama 2 (antitez) koşulmadı. Ayrıca bu ailenin bir şeridi (veri-füzyonu / truth discovery / kaynak-kopyalama tespiti) oturum limiti nedeniyle **hiç açılmadı**.

**Salih'in sorusu:** "aynı kategoriden iki zıt karar gelirse hakem hangisine yönelmeli? Kategori sayısını artıralım mı, optimum kaç?"

### 11.1 Kısa cevap: sorun kategori sayısı DEĞİL

**(a) Sayı artırmak problemi mantıken çözemez.** Sonlu bir etiket kümesi, bulgu sayısı kategori sayısını aştığı anda **kesinlikle** aynı-kategori çakışması üretir. 3 yerine 7 kategori çakışmayı geciktirir, kaldırmaz.

**(b) Sayı artırmak ölçülebilir ZARAR verir.**
- Kappa, kategori sayısı arttıkça **düşer** — mekanizma: kappa tüm anlaşmazlıkları eşit ve tam sayar; kategori arttıkça "kıl payı ıskalama" olasılığı artar ve hepsi tam ceza alır.
- **Etkin kategori sayısı nominalin altındadır**: merkezi eğilim yanlılığı + uç kaçınması + menzil kısıtlaması birlikte, 7 kategori vermenin 7 kategorilik bilgi üretmediği anlamına gelir.
- Uzman uyumu zaten düşük: 4 kademeli GRADE'de değerlendiriciler arası ağırlıklı κ = **0,79**, ama standart GRADE değerlendiricisi ile araç kullanıcısı arasında **0,35**. Bilimsel hakemlikte ~**0,17**.
- **Otorite bizzat granülerliği AZALTTI:** Oxford CEBM 2011 revizyonu, eski 1a/1b/1c alt-kademelerini tek bir "1"e indirdi.
- PolitiFact'in 6. kademesi ("Pants on Fire" vs "False") nesnel bir ayrım taşımıyor — kategori enflasyonunun uç örneği. *(Kaynak uyarısı: bu iddianın ayrıntılı hali taraflı bir savunuculuk sitesinden geliyor; tek başına yük taşımamalı.)*

**(c) Asıl arıza iki tane — ve ikisi de sayı değil.**

### 11.2 Arıza 1: tek-eksenlilik

D/K/X **tek bir şeyi** ölçüyor: kaynağın türü. Bir iddianın **teyit durumu** hiç kodlanmıyor.

**Admiralty Code / NATO STANAG** tam bu yüzden iki eksenlidir [D, MISP taksonomisinin makine-okunur metninden]:
- **Kaynak güvenilirliği A–F:** completely reliable → usually → fairly → not usually → unreliable → **reliability cannot be judged**
- **Bilgi doğruluğu 1–6:** confirmed by other sources → probably true → possibly true → doubtful → **improbable (contradicted by other information)** → **truth cannot be judged**

**ICD 203 / ODNI** aynı ayrımı farklı granülerlikte yapıyor [D]: olasılık ekseni **7 kademe + sayısal bant** (01-05% … 95-99%), güven ekseni yalnız **3 kademe** (Low/Moderate/High). Ve güvenin tanımı içine **kaynak çeşitliliği** açıkça yazılmış: *"the credibility and **diversity of sourcing** in the knowledge base."*

**▲ Ama iki eksen kendiliğinden çalışmıyor — bu bulgu kritiktir.** Baker, McKendry & Mace (1968), **1400'den fazla** saha istihbarat raporu: derecelendirmelerin **%87'si köşegen üzerinde** (A1, B2, C3…). Yani **36 hücrelik sistem pratikte ~6 hücrelik bilgi taşıyor.** Değerlendiriciler kaynak yargısının doğruluk yargısını kirletmesine izin veriyor. Aynı çalışma: doğruluk ekseninde referans çözümden sapma **%49**, güvenilirlik ekseninde **%15**.

**Çözüm RoB 2'nin yoludur [K]:** değerlendirici dereceyi **seçmez**; alan başına 3-7 **sinyal sorusuna** olgusal cevap verir, dereceyi **yayımlanmış bir algoritma** üretir.

### 11.3 Arıza 2: X'in iki farklı şeyi birleştirmesi

**Bu, tek değişiklikle en yüksek getiriyi veren düzeltmedir.**

Mevcut X = "doğrulanamadı **veya** çelişkili". Bunlar epistemik olarak farklı durumlardır ve her yerleşik sistem ayırıyor:

| Sistem | "çelişkili" | "yargılanamaz" |
|---|---|---|
| Admiralty | **5** — improbable, *contradicted by other information* | **6** — truth cannot be judged (+ kaynak ekseninde **F**) |
| FEVER (185.445 iddia, Fleiss κ=0,68) | REFUTED | NOTENOUGHINFO |
| Atıf değerlendirmesi (4'lü) | Contradictory | Irrelevant |
| Google AIS [D] | düşük atıf yargısı | ayrı **`Flagged`** alanı |
| STIX 2.1 [D] | Admiralty 5 → sayısal 10 | **6 sayıya çevrilemez — `ValueError` fırlatır** |

STIX'in davranışı bunun **formal kanıtıdır**: "bilinmiyor" düşük bir güven değeri değildir; **ekseni terk eden ayrı bir durumdur.**

**Pratik sonuç:** Salih'in bildirdiği "aynı kategoriden iki çelişen bulgu" vakalarının bir kısmı aslında **X-çelişkili vs X-doğrulanamadı** ayrımıdır ve bu ayrım yapılır yapılmaz kendiliğinden çözülür.

### 11.4 Optimum sayı: eksen başına ≈ 4

| Alt sınırı çeken | Üst sınırı çeken |
|---|---|
| Lozano ve ark. (2008), Monte Carlo: **minimum 4** şart, 7'den sonra kazanç kıt | Kappa kategori sayısıyla düşer |
| Cox (1980): 2-3 yeterli bilgi taşımaz; ideal 7 merkezli 5-9 | Menzil kısıtlaması etkin sayıyı zaten düşürür |
| Mellers ve ark.: **en az dört ayrı kategori** Brier skorunu yükseltiyor | Yerleşik taksonomiler: GRADE **4**, RoB 2 **3**, ICD 203 güven **3**, OCEBM **5** (azaltılarak) |

Preston & Colman (2000) 7-10 diyor, Krosnick & Fabrigar 5-7 — **[X] literatür tek bir sayıda uzlaşmıyor** ve bu dağılımın kendisi bir bulgudur. Sun ve ark. (2025) bunu formalize ediyor: ölçüm hatası kategori sayısından bağımsızsa **gerçek bir optimum YOKTUR**.

**▲ Aktarım uyarısı:** psikometri literatürünün tamamı **katılımcıların gizil bir tutumu derecelendirmesi** üzerinedir. Bizim görevimiz farklı: tek bir uzmanın **kanıt kalitesini sınıflandırması**. Doğrudan aktarıldığına dair kanıt bulunamadı; GRADE/RoB 2/Admiralty daha yakın analoglardır.

### 11.5 Önerilen yapı (Carvis tasarımı, Salih onayına tabi)

**Eksen S (kaynak), 4 kademe:** birincil · kurumsal-ikincil · bağımsız-ikincil · bilinmeyen-veya-taraflı
**Eksen C (teyit), 4 kademe:** bağımsız kaynaklarca teyitli · teyitsiz-ama-tutarlı · teyitsiz-ve-yalnız · **başka kanıtla çelişkili**
**Eksen-dışı durum:** `YARGILANAMAZ` (erişilemedi / kaynak yok / ölçülmemiş)

Mevcut D/K/X ile eşleme: D ≈ S-birincil · K ≈ S-ikincil · X **ikiye ayrılır** → C-çelişkili ve YARGILANAMAZ.

**Uygulama şartı (Admiralty'nin %87 köşegen dersi):** iki eksen aynı zihinsel hareketle doldurulursa tek eksene çöker. Bu yüzden atlas ajanına **derece sordurulmaz**, iki olgusal soru sorulur: (1) "Bu iddiayı birincil kaynaktan okudun mu?" (2) "Bu iddia kaç bağımsız kaynakta doğrulandı / herhangi biriyle çelişiyor mu?" Derece bu cevaplardan **kural** ile üretilir.

### 11.6 Hakemliğin gerçek makinesi etikette değil, etiketin YANINDA

Bu, A8'in en tutarlı yakınsamasıdır ve Salih'in sorusunun asıl cevabıdır:

1. **Diagnostiklik (ACH — Heuer):** Kanıt, favori hipotezle ne kadar *tutarlı* olduğuna göre değil, **rakip hipotezler arasında ne kadar AYIRT EDİCİ** olduğuna göre değerlendirilir. Karar kuralı tersine çevrilmiştir: **en çok destekli olan değil, en az ÇÜRÜTÜLMÜŞ olan** seçilir.
   **▲ Bu, m.40b'nin "adversaryal hayatta kalma" ölçütüyle AYNI ilkedir. Tüzüğün o maddesi bağımsız bir gelenek tarafından doğrulanmış oldu.**
2. **Bağımsızlık / triangülasyon (Munafò & Davey Smith, *Nature* 2018):** iki bulgunun kalitesi eşitse ayırıcı ölçüt **yanlılık kaynaklarının ilişkisizliğidir** — replikasyon tek başına yetmez.
3. **Tiplenmiş saldırı (savunulabilir akıl yürütme):** çelişki öncüle mi (undermining), sonuca mı (rebutting), çıkarımın kendisine mi (undercutting) saldırıyor? Üçü farklı çözüm gerektirir ve tek bir sıralı etiket bunu kodlayamaz.
4. **Anlaşmazlığı VERİ olarak sakla (Google AIS [D]):** 5 değerlendiriciden kaçının çoğunluğa katıldığı ayrıca tutuluyor. **Çelişki bilgidir; etikete gömülüp yok edilmemelidir.**
5. **Oy sayma yasağı (Cochrane):** çelişkiyi "hangi tarafta daha çok bulgu var" diye çözme. İstatistiksel anlamlılığa dayalı oy sayımının **gücü çalışma sayısı arttıkça sıfıra gider**; Cochrane bunu açıkça kabul edilemez sayıyor. Yalnız **yön** temelli sayım meşru.
6. **GRADE'in cevabı bize yetmez:** GRADE çelişkiye "kazanan seçerek" değil **güveni düşürerek** cevap verir (inconsistency bir *düşürücü* alandır). Hakemin ihtiyaç duyduğu ayırt edici bilgi GRADE'de yoktur.

### 11.7 Sayısal katman — kategoriyi değiştirmez, altına girer

Friedman, Baker, Mellers, Tetlock & Zeckhauser (2018), **888.328 jeopolitik tahmin**: sayısal olasılıkları yaygın nitel ifadelere uygun biçimde **kabalaştırmak — istihbarat analistlerine halihazırda ÖNERİLEN ifadeler dahil — kestirim doğruluğunu tutarlı biçimde feda ediyor.**

Ama **granülerlik beceriye bağlıdır**: süper-tahminciler %1'e bölünebilen tahminler yaparken sıradan tahminciler %10'a bölüyor; süper-tahmincilerin kestirimleri yuvarlandığında skorları düşüyor — yani ince granülerlik **kalibre olmayanda gürültüdür**.

**Öneri:** etiket 4 kademe kalsın (insan/hakem arayüzü), altında isteğe bağlı 0-100 saklansın (makine katmanı, STIX deseni), ve **kalibrasyon Brier ile ölçülene kadar sayıya karar ağırlığı verilmesin.** *(Bu, kapsüldeki "Fatebook BEKLEMEDE" kararıyla uyumlu.)*

---

## 12. AİLE A9 — Persona sadakati

> ⚠️ Aşama 2 (antitez) koşulmadı.

### 12.1 %85 rakamı sanıldığı şey değil — üç katmanlı düzeltme

Park ve ark. (2024), "Generative Agent Simulations of 1,000 People": 1.052 kişi, kişi başı ~2 saatlik mülakat; **GSS'te ortalama normalize doğruluk 0,85**, Big Five'ta normalize korelasyon ≈ 0,80.

**Katman 1 — normalizasyonun paydası insanın KENDİ tutarsızlığıdır.** Aynı katılımcılar GSS'i 2 hafta sonra tekrar dolduruyor; ajan, kişinin *kendi* iki-hafta-sonraki tutarlılığının %85'i kadar iyi. Twin-2K veri setinde ölçek açıkça görünüyor: **ham doğruluk ≈ 0,72**, insan test-retest tabanı ≈ 0,817, normalize ≈ 0,88. **Payda düştükçe normalize rakam ŞİŞER.**

**Katman 2 [D] — %85'i üreten prompt ROL YAPMA DEĞİL, ÜÇÜNCÜ ŞAHIS TAHMİN.** Kaynak koddan birebir okundu:
> *"Task: What you see above is an interview transcript. Based on the interview transcript, I want you to **predict the participant's survey responses**."*
…ve *"DON'T over think it. Use your system 1 (fast, intuitive) thinking."*

Model **"sen X'sin" diye canlandırılmıyor**; korpusa bakıp "bu kişi ne cevaplar" diye tahmin ettiriliyor. **Salih'in konseyinde ajanlara birinci-şahıs persona giydirmek, ölçülmüş 0,85'in geldiği kurulum DEĞİLDİR.**
Yöntem de fine-tuning değil: kaynak kodda `memory_stream.retrieve([anchor], 0, n_count=120)` — kişinin kendi korpusu üzerinde **RAG + refleksiyonla çıkarılmış öz-tanım**.

**Katman 3 [X] — aynı makale sürüm arasında adını değiştirdi.** arXiv 2509.19088 (Columbia, 19 ön-kayıtlı çalışma, 164 sonuç değişkeni): v3 = *"A Mega-Study of Digital Twins Reveals **Strengths**, Weaknesses and Opportunities"* → v5 = *"Digital Twins as **Funhouse Mirrors**: Five Key Distortions"*. Bireysel korelasyon **r = 0,20**.
**Uzlaştırma:** yüksek normalize doğruluk ile düşük bireysel korelasyon çelişmez — **model ortalama insanı iyi bilir, bireyi ayırt etmeyi bilmez.** Doğruluk çoğunluk-cevabından geliyor.

### 12.2 Beş sistematik çarpıtma + varyans çöküşü

Mega-çalışmanın kendi listesi: **yetersiz bireyselleşme · stereotipleştirme · temsil yanlılığı · ideolojik yanlılık · hiper-rasyonellik**. Sonuncusu konsey için kritik: simüle kişi, gerçek kişiden **daha tutarlı, daha akılcı, daha az çelişkili** konuşuyor.

Aynı çalışmanın en sert itirafı: **"tam-persona" ikizler, YALNIZCA-DEMOGRAFİ ikizlerden bireysel düzeyde çok az daha doğru.** 500+ soruluk zengin profil modelin cevabını neredeyse hiç değiştirmiyor — model jenerik özelliklere geri düşüyor. Ve: **yönlendirilebilirlik ≠ hizalanma** — prompt'la istediğin yöne çevirebilirsin, bu doğruluk kazandırmaz.

**Varyans çöküşü [K]:** Bisbee ve ark. (*Political Analysis* 2024) — ChatGPT personalarının ortalamaları ANES'e yakın **ama** dağılım belirgin biçimde daha dar; ChatGPT'den kestirilen katsayıların **%48'i** ANES muadilinden anlamlı farklı ve bunların **%32'sinde etkinin İŞARETİ ters dönüyor**.

**Karikatür, yüksek sadakatin MALİYETİ [K]:** "persona prompt'unu EN İYİ takip eden modeller, en karikatürleşmiş popülasyonları üretiyor." Persona uyumu ile stereotipleştirme aynı eksende artıyor.

### 12.3 Tarihsel figür: gerçek görüş değil, kamusal algı

**Adanmış bir doğruluk benchmark'ı YOK [D].** Alanın en geniş küratörlü listesi tarandı: kurgusal karakter sadakati için InCharacter/CharacterEval/RoleLLM/TimeChara var; **gerçek tarihsel ya da yaşayan kişiler için ayrılmış doğruluk benchmark'ı listede yok.**

**Klişe-gerçek karışması belgelenmiş [K]:** LLM'lerin öğrendiği ipuçları figürlerin *gerçek* kişiliğini yansıtmayabilir — eğitim verisi stereotiple şekillenmiş **insan tasvirleriyle** dolu. Yani **"Einstein personası", Einstein'ın görüşlerini değil Einstein hakkındaki kamusal algıyı üretir.** Ölçüm tarafı da aynı sorunu taşıyor: InCharacter'ın referans doğrusu karakterin *insanlarca-algılanan* kişiliğidir.

**En yakın gerçek deney — ve sonucu ayıltıcı [K]:** Schwitzgebel ve ark. (*Mind & Language* 2024), GPT-3 Dennett'in eserleriyle fine-tune edildi:
- **Dennett uzmanları (N=25): %51 doğru ayırt etme** (şans %20; yazarların hipotezi %80 idi → **hipotez çöktü**)
- **10 sorunun 2'sinde uzmanlar, Dennett'in KENDİ cevabı yerine yapay cevabı tercih etti.**

**▲ Hakem uyarısı:** "%51 ayırt edilemezlik" bir **inandırıcılık/Turing** ölçüsüdür, **yargı sadakati** ölçüsü değildir. Uzmanların yapay cevabı tercih etmesi, ölçülen şeyin **prototipiklik** olduğunu güçlendiriyor.

### 12.4 Konseye özel hata: yapay uzlaşma

Çok-ajanlı tartışmada LLM'lerin yalakalığı tartışmayı erken konsensüse çöktürüyor. DEBATE benchmark'ı (107 konu, 697 grupta 2.788 katılımcı): **sıfır-atışlı kurulumda rol-yapan ajan grupları, insan gruplarına kıyasla belirgin şekilde daha güçlü görüş yakınsaması gösteriyor.** Yani "Einstein vs Karpathy tartışsın" kurulumu, **gerçek hayatta sürecek anlaşmazlığı yapay olarak eritme** eğilimindedir — ki bu, Salih'in fikirden beklediği şeyin tam tersidir.

---

## 13. AİLE A10 — Konsey/tartışma mimarisi

> ⚠️ Aşama 2 (antitez) koşulmadı.

### 13.1 En sert bulgu: önerilen mimari literatürde ölçülmüş ve kaybediyor

**Salih'in "1 tez + 1 antitez + 1 hakem" kurgusunun literatürdeki adı: Multi-Persona (MP).** Bütçe-eşleştirilmiş 5 çerçeve × 9 benchmark değerlendirmesinde [D, kaynak markdown'ından tablolar okundu], GPT-4o-mini doğruluk (%):

| | MMLU | CSQA | AGIEval | GSM8K | MATH | HumanEval |
|---|---|---|---|---|---|---|
| CoT (tek ajan) | 80,73 | 82,87 | 66,40 | 93,60 | 72,87 | 78,05 |
| **Self-Consistency** | **82,13** | **83,80** | **67,07** | **95,67** | 73,96 | — |
| MAD (3 ajanlı konsey) | 74,73 | 80,73 | 64,33 | 94,93 | **75,40** | 68,09 |
| **Multi-Persona (tez+antitez+hakem)** | 75,47 | 68,07 | 61,67 | 90,87 | **51,87** | 63,01 |

MP, 9 benchmark'ın 8'inde 3-ajanlı konseye kaybediyor ve çoğunda **tek-ajan CoT'un da altında**. Llama3.1-8b ile çöküyor (MATH **10,30**, CoT 40,13).

**Yazarların teşhisi MİMARİ:** *"Multi-Persona explicitly instructs the devil agent to counter **whatever** the angel agent says. However, once the judge agent determines the devil's side is correct, the angel agent has **no opportunity to continue debating**."* — yani (a) **zorunlu karşıtlık** ve (b) **hakem kararının tek yönlü/geri dönüşsüz olması**.

**▲ HAKEM KAYDI — bunu doğrudan JARVIS'e transfer ETMİYORUM, gerekçesiyle:**
1. Ölçüm **benchmark sorusu çözme** üzerine; atlas'ın işi **literatür keşfi + adversaryal doğrulama**. Orada self-consistency diye bir alternatif yok (yeniden örnekleyeceğin bir "doğru cevap" yok).
2. m.40b'nin antitezi **CoVe-Factored**'dır — tezin gerekçesini görmez. MP'nin devil'i ise tezin her söylediğini görüp karşı çıkar. Farklı mekanizma.
3. m.40b'de hakem tartışmayı **kesmez** — üç aşama sıralı koşar, geri dönüşsüz bir "karar anı" yoktur.

**Ama iki uyarı AYNEN geçiyor:** (a) **zorunlu karşıtlık zararlıdır** — skill'in "süs-antitez kurma" uyarısının tersi de doğruymuş: *her koşulda* itiraz etmeye zorlanan antitez de zararlı. (b) Aynı modele farklı persona vermek gerçek çeşitlilik üretmiyor.

### 13.2 Ölçek: daha çok ajan ≠ daha iyi

**Sabit çağrı bütçesinde (10 çağrı):** 2 ajanla **2-3 tur en iyi** (87,42 / 87,39); 4-5 tur fayda vermiyor. Aynı bütçede genişliği 2→3→5 ajana çıkarmak doğruluğu **düşürüyor**: 86,77 → 85,22 → 86,15. Süreç analizi: *"majority pressure suppresses independent correction."*

**[X] Ama ölçekleme yönü çelişkili:** başka bir çalışma "ajan sayısını artırmak iyileştirdi, tur sayısını artırmak kötüleştirdi" diyor; bütçe-eşleştirilmiş değerlendirme ise **ne ajan ne tur sayısında belirgin eğilim** bulmuyor. Bütçe eşitleme metodolojileri farklı olduğu için üçü uzlaşmıyor.

### 13.3 Konformite — sayısal

- **Modal (çoğunluk) cevabı sorgusuz benimseme %85,5'e kadar.**
- **"Oracle gap" 32,3 puana kadar:** doğru cevap havuzda ÜRETİLMİŞ olmasına rağmen çoğunluk oyu onu çöpe atıyor.
- **Katı konformite %29**, ve ağırlıklı olarak zararlı: **doğru→yanlış geçişleri %57-77**.
- Sycophancy %70'i aştığında ekipler doğru muhakemeyi **erken uzlaşma uğruna** sistematik olarak atıyor.
- Sonuç: yapılandırılmamış akran alışverişi yerine **izole öz-düzeltme daha iyi maliyet-doğruluk dengesi veriyor.**

### 13.4 Çeşitlilik: model ≫ persona

**Farklı MODEL kullanmak, aynı modelin farklı persona'sını yeniyor [D]:**

| | CCC | GGG | LLL | GGL | GLL | GLC |
|---|---|---|---|---|---|---|
| GSM8k | 87,80 | 94,80 | 84,00 | **95,00** | 94,40 | 94,34 |
| HumanEval | 64,02 | 68,29 | 69,51 | **77,44** | 76,83 | **77,44** |
| MMLU | 55,13 | 75,00 | 84,20 | 79,00 | **88,20** | 71,92 |

Her üç görevde de en iyi skor **karma** konseyde; homojen üçlüler hiçbirinde tepe değil. Heter-MAD (her adımda havuzdan rastgele model) tüm çerçeveleri **+%6,4 ila +%8,2** iyileştiriyor.

**Buna karşılık persona çeşitliliği SAHTE çeşitlilik üretiyor:** persona ayrıntısını artırmak çeşitliliği monoton artırmıyor; demografik detay eklemek bazı modellerde çeşitliliği **azaltıyor** ("persona manifold collapse"). Tartışma bağlamında farklı persona ataması **anlaşmaya varma olasılığını düşürüyor ama doğruluğu yükseltmiyor**.

**▲ Bu, kutudaki V59'u (atlas alt-ajanlarına farklı/ucuz model) kanıta bağlar — ve gerekçesini değiştirir: V59 bir MALİYET tedbiri olarak kutuya girmişti; A10 onu bir KALİTE tedbiri yapıyor.**

**[X] Ama heterojenlik evrensel ilaç değil:** başka çalışmalarda heterojen takım **8 koşul-görev çiftinin 6'sında en iyi homojen üyenin altında** kaldı; "model çeşitliliği tipik olarak en iyi ve en kötü üye arasında bir sonuç veriyor".

### 13.5 Hakem çoğullaştırmak da kurtarmıyor [X]

- **PoLL:** 3 küçük modelden panel, tek büyük hakemi geçiyor ve 7 kat ucuz.
- **"Nine Judges, Two Effective Votes" (Apple):** 7 model ailesinden 9 hakem, **yalnızca ~2 bağımsız oy kadar bilgi** taşıyor — nominal bağımsızlığın dörtte üçü kayıp, çünkü modeller **aynı maddelerde aynı hatayı** yapıyor. Panelin gerçek doğruluğu bağımsız-oylama idealinin **8-22 puan altında**; **en iyi tek hakem, tam paneli her koşulda eşliyor ya da geçiyor.**

İkisi doğrudan çelişiyor; ikincisi daha yeni ve daha sıkı ölçülmüş.

### 13.6 En yüksek getirili tek kaldıraç: erken uzlaşmayı engellemek

Anlaşma şiddetini prompt ile modüle etmek **Multi-Persona'da ~%15**, SoM'da ~%5 kazanç veriyor; %90 anlaşma-şiddeti promptu MedQA'da yeni en yüksek skoru veriyor.
**Okunuşu: tartışmanın kazancı, tartışmanın kendisinden çok "erken uzlaşmayı engelleme" ayarından geliyor olabilir.**

### 13.7 Kapı kuralı ve maliyet

*"most test cases in existing benchmarks only require a single knowledge point to be solved, which naturally makes MAD unnecessary. Under this circumstance, **MAD degrades to an inefficient resampling method**"* [D].
İkinci teşhis: ajanlar **tam yanıtlar** üzerinden tartıştığı için muhakeme adımlarına değil nihai cevaba tepki veriyorlar — "öteki farklı cevap verdi" olgusuna, gerekçe farkına değil.

**Maliyet:** çoklu-ajan ~15× sohbet tokeni; MAD izole öz-düzeltmenin **2,1×-3,4×**'i; maliyet ajan ve tur sayısıyla **süper-lineer** büyüyor (her ajan diğerlerinin çıktısını bağlamına alıyor).

**Tartışmanın en güçlü POZİTİF kanıtı farklı bir problemde:** bilgi-asimetrik hakemlik — uzman olmayan hakem iki tartışmacıyı dinlediğinde doğruluk **%76 (model hakem) / %88 (insan hakem)**, naif temeller %48/%60. Ve kritik ayrım: **tartışmacıları daha ikna edici yapmak tartışmada doğruluğu ARTIRIYOR, tek-danışman kurulumunda DÜŞÜRÜYOR.** Bu senaryo "hakem cevabı bilmiyor, tartışmacılar biliyor" durumudur — genel karar kalitesine doğrudan transfer etmez.

---

## 14. AİLE A11 — Persona'nın etik ve hukuki sınırları

> ⚠️ Aşama 2 (antitez) koşulmadı. **Ayrıca bu ailede [D] üretilemedi** — hiçbir birincil mevzuat/karar metnine inilemedi; tamamı [K].

### 14.1 Einstein ile Karpathy aynı hukuki sınıfta DEĞİL

**Einstein — hukuken en düşük riskli persona adayı:**
- **Hebrew University of Jerusalem v. General Motors LLC**, 903 F. Supp. 2d 932 (C.D. Cal. 2012): mahkeme common law post-mortem publicity hakkına ilk kez sınır tanıyarak sürenin **50 yılı aşamayacağına** hükmetti. Einstein 1955'te öldü, ikametgâhı New Jersey → **hakları 2005'te sona erdi**, imgesi kamu malı.
- Eserleri **1 Ocak 2026'da** ömür+70 ülkelerinde kamu malı oldu. *(ABD telif kuralları farklıdır — doğrulanmadı.)*
- **GDPR Resital 27:** *"This Regulation does not apply to the personal data of deceased persons."*
- OpenAI kullanım şartlarında "başka kişiyi simüle eden" sistemler için rıza/etiket şartından **muaf tutulan tek kategori: tarihsel kamusal figürler.**

**Karpathy (yaşayan) — farklı tablo:**
- Tennessee **ELVIS Act** yürürlükte (1 Temmuz 2024): ad, fotoğraf, **ses** (gerçek ya da **simüle edilmiş**) üzerinde icra edilebilir hak; hem hukuki hem cezai yaptırım; insan taklidi üreten üretken-YZ klonlama servislerini hedefliyor.
- California **AB 1836 + AB 2602** yürürlükte (1 Ocak 2025).
- **BK CDPA 1988 md. 84 — yanlış atfedilmeme hakkı:** bir esere yazar olarak yanlış atfedilmeme. **Bu, iftiradan bağımsız ayrı bir dava kapısıdır ve TİCARİ KULLANIM GEREKTİRMEZ.** Einstein için süre dolmuş (ölüm+20 yıl); **yaşayan biri için AÇIK.**
- ⚠️ **NO FAKES Act YASA DEĞİL** — S.1367, 9 Nisan 2025'te sunuldu, hâlâ komitede.

### 14.2 Özel kullanım ↔ yayımlama eşiği — dört hukuk dalı aynı yerde kapı değiştiriyor

**Özel kullanımda KAPALI kapılar:**
| Dal | Kapı |
|---|---|
| İftira | Üçüncü kişiye **yayım** gerekir (Restatement §577). Yalnız mağdura söylenen iftira değildir. |
| Right of publicity | "advertising or trade" / ticari sömürü kapısı |
| GDPR (yaşayan) | md. 2(2)(c) hane-içi istisnası |
| EU AI Act | md. 2(10) "purely personal, non-professional" istisnası → md. 50 ifşa yükümlülüğü doğmaz |

**Kalkanı düşüren ÜÇ tetikleyici — ve ikisi para gerektirmiyor:**
1. **Belirsiz sayıda kişiye erişilebilir kılma** → GDPR hane-içi istisnası düşer (*Lindqvist* C-101/01; *Ryneš* C-212/13 istisnayı dar yorumluyor).
2. **Düzenli ekonomik fayda / mesleki bağlam** → AI Act md. 2(10) düşer + publicity'nin ticari kapısı açılır.
3. **Kamu yararına ilişkin kamusal tartışmayı etkileme** → AI Act md. 50(4) metin-ifşası + md. 2(10) kaybı.

**Eşikten BAĞIMSIZ iki risk:**
- **Yanlış atıf** (BK CDPA md. 84) — ticari kullanım gerektirmez.
- **Epistemik bozulma** — **özel kullanımda TAM GÜÇLE mevcut** ve Salih'in kendi kararlarını doğrudan bozar. Hukuki eşik burada koruma sağlamaz.

### 14.3 Dava manzarası oturmamış [X]

- **Walters v. OpenAI:** OpenAI **kazandı** (19 Mayıs 2025, Gwinnett County). Üç gerekçe: makul okuyucu çıktıyı olgu sanmazdı · OpenAI'nin halüsinasyon azaltma çabası ve kapsamlı uyarıları kusur bulgusunu imkânsız kıldı · zarar yok. **Temyiz durumu doğrulanamadı — "kesinleşti" denemez.**
  **▲ Kritik: bu zafer büyük ölçüde DISCLAIMER ve "makul okuyucu bunu olgu sanmaz" üzerine kuruldu. Persona-ajan tam tersini yapar — inandırıcılığı artırır, disclaimer'ı zayıflatır. Walters savunması persona sistemine TRANSFER OLMAZ.**
- **Starbuck v. Meta:** Ağustos 2025'te **sulh**; Starbuck, Meta'nın Product Policy ekibine danışman oldu.
- **Starbuck v. Google:** derdest, 15M USD üzeri talep, Delaware mahkemesi **iddiaların ilerlemesine izin verdi**.

**Sonuç: LLM iftira hukuku HENÜZ OTURMADI. Tek bir emsale yaslanmak yanlış olur.**

### 14.4 "Hukuken serbest" ≠ "etik olarak güvenli" — somut emsal

**"Historical Figures" uygulaması (Ocak 2023):** ChatGPT üzerine kurulu, App Store'da **Eğitim** kategorisinde ve **9+ yaş** için listelenmiş, ~20.000 tarihsel figür. Somut zarar: **Himmler personası Holokost'taki rolünü inkâr etti.** Eleştirinin özü: **eğitim vaadi taşıdığı için yanıltıcılığı daha tehlikeli.**

Bu, "ölmüş = risksiz" varsayımının etik tarafını çürüten en somut vakadır — ve JARVIS için özellikle yakıcıdır, çünkü kurulacak sistemin **adı öğrenme sistemi**.

### 14.5 Griefbot/deadbot etiği — uygulanabilir tavsiyeler

Hollanek & Nowaczyk-Basińska (*Philosophy & Technology*, 2024), üçlü rol çerçevesi: **data donor** (verisi kullanılan) · **data recipient** (ölümden sonra sahibi) · **service interactant** (etkileşen). Tasarım tavsiyeleri:
(a) deadbot'ları **emekliye ayırmak için hassas prosedürler** · (b) **anlamlı şeffaflık** · (c) yalnız yetişkin erişimi · (d) **karşılıklı rıza** ilkesi.
Yazarların dürüst tavizi: rıza vermemiş bağışçılara dayalı deadbot'ların tümden yasaklanması **uygulanabilir değildir**.

### 14.6 Epistemik risk: ikna ile doğruluğun AYRIŞMASI

**▲ Terim düzeltmesi:** Carvis'in kullandığı **"authority laundering" yerleşik bir akademik terim DEĞİL.** Yerleşik karşılık **"epistemic trespassing"** (Ballantyne): bir alanda uzman olanların statülerini uzmanlık alanları dışına taşıyıp orada otoriteyle konuşmaları; mekanizma **kredibilite fazlası / kredibilite açığı**.

**Ölçülmüş iki bulgu, birlikte okununca sistemin çekirdek riskini veriyor:**
- **Persona doğruluğu ARTIRMIYOR** (Zheng ve ark., EMNLP Findings 2024 — 162 persona, 4 model ailesi, 2.410 soru); düşük-bilgi personalar doğruluğu **düşürüyor**.
- **Kişiselleştirme ikna gücünü ARTIRIYOR** (Salvi ve ark., *Nature Human Behaviour* 2025, 900 katılımcı): kişiselleştirilmiş GPT-4, münazara sonrası mutabakat için insanlara kıyasla **%81,2 daha yüksek olasılık**.

**Yani: persona seni daha doğru bilgilendirmiyor, ama daha çok ikna ediyor.** Bir öğrenme sisteminde bu, olabilecek en kötü bileşimdir.
*(Not: Salvi kişiselleştirme etkisidir, ünlü-isim atfı etkisi değil — doğrudan transfer edilemez. **Aynı argümanın farklı isimlere atfedilmesiyle algılanan kaliteyi ölçen deney BULUNAMADI** — açık boşluk.)*

---

## 15. V26 ÖRNEKLEM-DENETİMİ — koşulamadı, yerine ne yapıldı

**V26 klasik haliyle KOŞULAMADI.** Protokol "ajan başına ≥1 rastgele kaynak iddiası seç, kaynağa in, doğrula" der; bu oturumda birincil kaynağa iniş fiziksel olarak kapalıydı (bölüm 0).

**Yerine koşulan — çapraz-denetim (V26 DEĞİLDİR, yerine geçtiği iddia edilmez):**

| Denetim | Sonuç | Etki |
|---|---|---|
| Aynı rakam bağımsız sorgularda tekrar ediyor mu? | A1/1 (AUC 0,83 / 0,69) ve A1/16 (statelessness) iki bağımsız aramada teyitli | güven artışı, D'ye çıkarmaz |
| Tez ve antitez aynı kaynağa aynı rakamı mı atfediyor? | **HAYIR — 1 vaka** | **[X] damgası** |
| Ajanın kendi bayrakladığı zayıf kaynak, başka ajan tarafından dayanak yapılmış mı? | **EVET — 1 vaka** | hakem müdahalesi (§4.2) |
| Ajanın hükmü kendi kanıtıyla uyumlu mu? | **HAYIR — 1 konstrükt kayması** (eğitmen↔öğrenci) | hüküm daraltıldı (§4.2) |
| İddia edilen rakamın künyesi bulunabiliyor mu? | **HAYIR — r≈0,31** | iddia çürütüldü (§7.2) |

**Yakalanan çelişkiler (hepsi raporda [X] damgalı, sessizce uzlaştırılmadı):**
1. Aynı URL'ye iki farklı efekt büyüklüğü (g=1,14 vs g=0,670) — §5.2
2. `CLAUDE_STREAM_IDLE_TIMEOUT_MS` iki resmî sayfada farklı — §8.2
3. scikit-learn'ün Elkan eşiği (1/5) vs türetme (1/6) — §9.5
4. Persona lehte/aleyhte literatür — §10.3
5. Ajan/tur ölçekleme yönü — §13.2
6. Hakem paneli lehte/aleyhte — §13.5
7. Sansür yanlılığının yönü — §9.1
8. Süre dağılımı ailesi (Pareto vs lognormal vs karışık) — §9.3
9. AI Act md. 50 kılavuzunda çelişkili aktarım — §14.2
10. Mega-çalışmanın sürüm arası ad değişimi — §12.1

**Hüküm: bu koşumun etiket enflasyonu riski YÜKSEK.** 10 çelişki yakalandı ama denetimsiz kalan yüzey büyük. Akademik rakamların hüküm taşıması için bölüm 20/borç-1 kapatılmalıdır.

---

## 16. TASARIM — pasif öğrenme sistemi (m.37, 3 model)

### 16.1 Kanıttan çıkan sert kısıtlar

Tasarım bu altı kısıtın **hepsini** karşılamak zorunda:

| # | Kısıt | Kaynak |
|---|---|---|
| K1 | Öğrenen-modeli **dosyada** yaşamalı; modelin hafızasında yaşamaz | §4.1 (S1) |
| K2 | Yalnız LLM sentezi okumak **sığ bilgi** üretir — çekirdek olgular aynı olsa bile | §5.1 (S2) |
| K3 | Acemide **önce deneme, sonra okuma** kavramsal anlama ve transferde öndedir | §5.3 |
| K4 | Kalite kapısı **üretim anında** olmalı (artık etki sıfırlanamaz); doğrulama **referanslı** ve **ayrı geçiş** olmalı, intrinsic self-correction değil | §7.1 (S3), §7.2 |
| K5 | Sistem, Salih'in **yardımsız** performansını görmeli — yoksa soldurma (fading) kararı veremez | §6.1 |
| K6 | İşveren verisi **prosedürel** kapıdan geçer (yazılı izin), anonimleştirmeden değil | §6.1 |

**K6'nın doğrudan sonucu: staj görevleri bu sistemin substratı OLAMAZ.** Substrat, JARVIS'in kendi karar akışıdır — ki zaten mevcut (senaryo-defteri, m.37 kayıtları) ve Salih'in kendi malıdır.

### 16.2 Üç model

**Model A — "Hasat" (minimal)**
Her m.37 kararından sonra Carvis tek sayfalık bir ders notu üretir; karar kaydına `SONUÇ` alanı eklenir (§7.1/S6: hiçbir ADR şablonunda yok).
· Token: ~3-5k/karar · Zaman: +5 dk/karar · Beklenen kalite: **düşük-orta**
· K1 ✅ K2 ❌ K3 ❌ K4 ⚠️ K5 ❌ K6 ✅
· **Zayıflığı belirleyici:** K2 ve K3'ü hiç karşılamıyor — tam olarak "LLM sentezini pasif oku" deseni, yani ölçülmüş olarak sığ bilgi üreten kurulum.

**Model B — "Önce dene, sonra oku" (ÖNERİLEN ✅)**
Akış, karar başına:
1. **Deneme kapısı (K3, K5):** Karar anında Salih'ten **2-3 cümlelik kendi formülasyonu** istenir — "sence hangi seçenek ve neden?". Bu, productive-failure'ın "önce dene" adımıdır **ve aynı zamanda K5'in çözümüdür**: bu metin, Salih'in *yardımsız* performansının kaydıdır. Soldurma kararı buradan verilir.
2. **Ders üretimi (K2 karşı-tedbiri):** Carvis, Salih'in formülasyonundaki farkı V55 formatıyla düzeltir (*"bunu derken aslında ... demek istedin"*) — yani ders **sentez değil, kendi üretimine yapılan düzeltme**. Melumad & Yun'un ölçtüğü "hazır özet oku" kurulumundan yapısal olarak farklı.
3. **Kalite kapısı (K4):** Ders metni, **ayrı bir doğrulayıcı geçişten** geçer; doğrulayıcının elinde **karar kaydının kendisi** vardır (referanslı doğrulama — reddedilen intrinsic self-correction değil). Rubrik: "tanımlı kusur tespiti" (olgu hatası, uydurma atıf, karar kaydıyla çelişki) — yargıcın güçlü olduğu görev tipi (§7.3).
4. **Kayıt (K1):** ders `ogrenme/dersler/`e; Salih'in formülasyonu + fark, **öğrenen-durumu dosyasına** işlenir.
· Token: ~12-18k/karar `[?]` · Zaman: +15-20 dk/karar · Beklenen kalite: **yüksek**
· K1 ✅ K2 ✅ K3 ✅ K4 ✅ K5 ✅ K6 ✅
· **Ek avantaj:** mevcut V55 pasif-okuma protokolünü **iptal etmiyor, önüne bir adım ekliyor.** Salih'in "kritik satırı yazması zorunlu değil" kuralı korunuyor — ama yazdığında sistem ölçüm kazanıyor.

**Model C — "Tam hat" (ajan + aralıklı tekrar + eval)**
Model B + adanmış öğrenme ajanı + FSRS döngüsü + eval seti.
· Token: ~40-60k/karar `[?]` · Zaman: kurulum 2-3 vardiya · Beklenen kalite: **yüksek, ama kanıtı zayıf**
· **Neden şimdi değil:** (a) K-010 kapıları kapalı (§18); (b) LLM üretimi kartların SR döngüsündeki öğrenme çıktısı ölçülmüş ama **küçük-N, quasi-deneysel, çoğu kelime/EFL** (§7.2); (c) A7: adanmış ajanın getirisi token-eşitlenmiş olarak **hiç ölçülmemiş**.

### 16.3 Önerinin gerekçesi tek cümlede

**Model B, "pasif öğrenme"yi iptal etmiyor — onu ölçülmüş olarak çalışan tek forma sokuyor.** Salih'in fikri (karar akışından ders üretimi) aynen korunuyor; değişen tek şey, dersin **hazır özet** olarak değil **kendi denemesine yapılan düzeltme** olarak gelmesi. Bu tek değişiklik K2, K3 ve K5'i birden çözüyor.

---

## 17. ÖĞRENME OTURUMLARI — donma vakasından çıkan müfredat

Salih'in isteği: "çözüm sürecinin aşamalarını içeren ilimleri, DS bağlamıyla öğrenme oturumlarına çevir." Aşağıdaki müfredat **gerçek vakadan** (bölüm 2) türetilmiştir — her oturumun malzemesi kendi sistemimizin verisidir.

| # | Oturum | Vakadaki karşılığı | DS disiplini | DONE | Derinlik |
|---|---|---|---|---|---|
| **L1** | **Ölç, sonra teorileştir** | H0 (ağ asılması) veriyle çürütüldü; WebSearch/WebFetch 11 s'de tavana vuruyor | hipotez testi, teşhis ölçümü | Salih, kendi bir hipotezini ölçümle çürütür | [O] |
| **L2** | **Sağdan sansürleme** | Hâlâ koşan ajan = sansürlü gözlem; "3 saati geçen görmedik" cümlesinin boşluğu | survival analysis, Kaplan-Meier, survivorship bias | "yalnız bitenlerin ortalaması" hatasını iki yönüyle anlatır | [T] |
| **L3** | **Hazard ve bekleme sezgisinin tersine dönmesi** | MRL tablosu: Pareto'da 10 dk koşanın kalanı 20 dk | hazard fonksiyonu, DFR/IFR, ağır kuyruk, restart (CV>1) | "yeterince bekledik" sezgisinin ne zaman yanlış olduğunu söyler | [T] |
| **L4** | **Maliyet-duyarlı eşik ve küçük-N** | 60 s eşiği %11 kesin; 300 s %100 ama **N=2** | PR vs ROC, Bayes eşiği, Neyman-Pearson, kuantil GA'sı | n=30'da p95 GA'sının neden kurulamadığını gösterir | [T] |
| **L5** | **İlerleme ≠ canlılık** | Async stall watchdog; progress deadline vs mutlak timeout | gözlemlenebilirlik, heartbeat, telemetri tasarımı | JARVIS için ilerleme sinyali tanımlar | [O] |
| **L6** | **Geri-besleme döngüsü: politika kendi verisini kirletir** | Watchdog kurulduğu an sansür *informative* olur | informative censoring, seçim yanlılığı | Kendi eşiğimizin veriyi nasıl bozacağını açıklar | [T] |

**Not:** L2, L3, L4, L6 **doğrudan veri-bilimci işidir** ve stajda karşılığı vardır (A/B test analizi, churn/survival modelleme, eşik seçimi, seçim yanlılığı). L1 ve L5 mühendislik tarafı.

**Format:** `ogrenme/README.md` protokolü aynen (Yarı-1 pasif-okuma + Yarı-2 m.37 3-model), **artı Model B'nin deneme kapısı** — her oturum Salih'in kendi formülasyonuyla açılır.

---

## 18. AJAN TASARIM PAKETİ — iki parça, biri kapı-bağımlı

> **m.16 çelişki bildirimi (Salih'e sunuldu 07-26):** "Şirkete ajan atayalım" isteği K-010 (BLOKE) ile çakışıyor; tetik K-009 ∧ (A1∧A2∧A3∧A4) ve A1 sayacı şu an tartışmalı. Ancak **A5 (ekip-lideri hattı) paralel ilan edilmişti** ve önkoşulu "tasarım paketi + CC derin-araştırma + atlas". Öğrenme ajanı bu sınıfa girer. Aşağıdaki (a) bugün üretilebilir, (b) kapı-bağımlıdır.

### 18.a Bugün üretilebilir — tasarım paketi

**Rol:** Karar-akışından ders üretimi (Model B adım 2-3).
**Yetki bandı:** yalnız `ogrenme/dersler/` ve öğrenen-durumu dosyasına yazar. `core/`, `CLAUDE.md`, `.claude/` **yapısal kilitli** (mevcut settings-deny + tel yeterli). Commit atmaz.
**Araç kısıtı (A7/1.2):** `tools: Read, Grep, Glob, Write` — Bash YOK (bölüm 2'nin bulgusu: ajan-yazımı Bash bekleme döngüsü, ölçülen iki patolojinin ikisi de), WebSearch YOK (ders karar kaydından üretilir, dış aramadan değil).
**Model:** `inherit` değil — **farklı model** (A10/13.4: heterojenlik kalite kazandırıyor; V59 bu bulguyla kanıta bağlandı).
**Hafıza:** `memory: project` (A7/1.3) → öğrenen-durumu dosyası burada yaşar (K1). **Boyut disiplini zorunlu:** 200 satır / 25KB eşiği aşılırsa **sessizce kırpılır** (A7/5.3) — K-019 boyut-izleme kuralı buraya da uygulanır.
**Doğrulayıcı:** **ayrı** ajan, referanslı rubrik (K4). Üreten ajanla **aynı model olmayacak** (A7/6.3: "üreten modelden farklı bir modelle değerlendirmek en iyi pratiktir").
**Defter:** `kuyruk/ajan-defteri-sema-v1.md` mevcut — bu ajan ilk müşterisi.
**Eval (A7/6.1):** ≥3 senaryo + baseline; kabul kararı **eşleştirilmiş** A/B (aynı karar kaydı, ajanlı ve ajansız), **tek koşumdan sonuç çıkarılmaz** (A7/6.5: küçük-N'de gerçek SE naif SE'nin 3 katından fazla olabiliyor).
**Geliştirme döngüsü:** Claude A / Claude B (A7/6.2) — gözlenen davranışa dayalı, varsayıma değil.

### 18.b Kapı-bağımlı — devreye alma

K-010 kapıları (A1∧A2∧A3∧A4) kapanmadan **canlı ajan atanmaz**. Öğrenme ajanı, A5'in "ilk devir iş-sınıfı" açık kararına **somut aday** olarak sunulur.

**Aday olarak lehte:** çıktısı ders metni, kanona yazmıyor, dosya silinerek geri alınır.
**Aday olarak aleyhte — ve bu ciddi:** A4/S3 gösterdi ki yanlış öğrenilen bilgi düzeltmeyle **tamamen silinmiyor**. Yani "geri alınması ucuz" yalnız **dosya** için doğru; **Salih'in kafasında ucuz değil.** Bu, öğrenme ajanını göründüğünden riskli kılar ve K4 kapısını pazarlık dışı yapar.

---

## 19. FİKİR KUTUSU — hazır V-kayıtları (ana sıraya yapıştırılmak üzere)

> m.41 gereği bu yan-oturum `fikir-kutusu.md`'ye YAZMAZ. Aşağıdaki satırlar ana-sırada yapıştırılmak üzere hazırdır; numaralar ana sırada verilecektir.

**V6x — Fikir konseyi (gerçek kişi personaları).** Ünlü kişilerin yazı ve projelerinden persona-ajanları kurup yargıları konseyde tartıştırma. **Statü: ADAY — ama atlas koşumu ciddi itirazlar getirdi (rapor §12-13-14).** Üç sert bulgu: (1) ölçülmüş %85 sadakat **birinci-şahıs rol yapmadan değil, üçüncü-şahıs tahminden** geliyor; (2) tarihsel figür personası kişinin görüşlerini değil **kamusal algıyı** üretiyor, ve adanmış doğruluk benchmark'ı **yok**; (3) önerilen "tez+antitez+hakem" mimarisi literatürde **Multi-Persona** adıyla ölçülmüş ve MAD çerçeveleri arasında **en kötüsü**. Ayrıca persona doğruluğu artırmıyor ama ikna gücünü artırıyor — bir öğrenme sisteminde en kötü bileşim. **Yaşayabilir dar hali:** persona yerine **farklı MODEL** kullan (Heter-MAD +%6,4-8,2), ve "X ne derdi" yerine **"X'in yazdıklarına göre bu karar hakkında ne öngörülür"** üçüncü-şahıs formatı. `TETİKLİ: K-010 açılışı ∧ Salih onayı`

**V6x — Fütüristik: her an proje inşası (giyilebilir + senkron).** Uzun ufuk: Meta gözlük sınıfı cihazlarla gün içinde her işi yaparken paralel proje geliştirme. **Kısa vade hedefi Salih'in kendi koyduğu şekliyle: telefon-PC senkron konuşabilme, telefondan senkron proje inşası.** `UFUK` · **ARAŞTIRILMADI** — atlas koşulmadı (bölüm 20/borç-3).

**V6x — Lojik→günlük dil compiler ajanı.** Carvis lojik-temelli raporlar üretiyor, Salih okuyor; ileride o raporları tekrar okuyup günlük hayat diline çeviren bir compiler ajan gerekebilir. Lojik = compiler kapısı. Türev: her "ai→ai" rapor için bir "ai→insan" muadili. `UFUK` · **ARAŞTIRILMADI** (bölüm 20/borç-4). *Not: bu raporun kendisi bu ihtiyacın kanıtı — 20 bölüm, ağır kanıt yoğunluğu.*

**V6x — Ajanlar arası iletişimin graf tasarımı.** Şirkette ajan-ajan iletişimi bir graf tasarım problemi olarak modellenebilir (topoloji, kenar tipi, mesaj yönü, döngü). `UFUK` · **ARAŞTIRILMADI** (bölüm 20/borç-5). *Kısmi girdi mevcut: A10/13.2 (sabit bütçede 2 ajan × 2-3 tur optimum; genişlik artışı zararlı) ve A7/10.4 (MAST: başarısızlıkların %41,8'i spesifikasyon, %36,9'u ajanlar-arası hizasızlık) bu kartın ilk kanıtlarıdır.*

**V6x — Araştırma ajanına hukuksal katman.** Research agent'a hukuki değerlendirme katmanı eklenmesi. `TETİKLİ: dışarı çıkacak ilk çıktı` · **KISMEN ARAŞTIRILDI** — A11 (§14) hukuki çerçeveyi kurdu: özel kullanım ↔ yayımlama eşiği, üç tetikleyici, eşikten bağımsız iki risk. Tam tasarım için ayrı koşum gerekli (bölüm 20/borç-6).

---

## 20. AÇIK BORÇLAR VE CEVAPLANMAMIŞ SORULAR

### 20.1 Protokol borçları (m.40b)

1. **A5-A11 için Aşama 2 (antitez) KOŞULMADI** — oturum limiti. Yedi ailenin bulguları adversaryal sınamadan geçmemiştir. A5/A7/A11'in [D] bulguları olgusal olarak sağlam ama **yorum katmanı sınanmamıştır**. En kırılgan üç nokta antitez öncelikli: A6-17 (dağılım ailesi), A6-34 (Elkan eşiği), A6-6 (sansür yanlılığı yönü).
2. **V26 örneklem-denetimi klasik haliyle koşulamadı** (§15). Etiket enflasyonu riski yüksek.
3. **Koşum-sonrası hayatta-kalma oranı senaryo-defterine işlenmeli** (m.40b v0.2 deneysel damgası): A1-A4'te 36 iddiadan 3 ÇÜRÜTÜLEMEDİ · 7 ÇÜRÜTÜLDÜ · 26 DARALTILDI.

### 20.2 Kanıt borçları

1. **⭐ Akademik rakamların yeniden doğrulanması.** Bu oturumda hiçbir akademik kaynağa inilemedi; A1/A2/A3'te D etiketi yok. Erişimi açık bir oturumda öncelikli doğrulanacaklar: Bastani %48/%127/−%17 · Kestin 0,73-1,3 SD · Keiser & Arthur d=0,79 · Sinha & Kapur PS-I etkisi · Staab %85/%95,8 · Park normalize 0,85 ve ham 0,72 · Rocher %99,98.
2. **[X] Aynı URL'ye iki farklı efekt büyüklüğü** (g=1,14 vs g=0,670) — kullanılmadan önce çözülmeli.
3. **r≈0,31 künyesi bulunamadı** — tez şeridinin dayanağıydı, çürütüldü, ama kaynağı hâlâ meçhul.

### 20.3 Koşulmamış araştırmalar (Salih'in istekleri, açıkça eksik)

| # | Konu | Durum |
|---|---|---|
| 3 | **Fütüristik: giyilebilir + telefon-PC senkron proje inşası** | **HİÇ KOŞULMADI** — görev emri hazırlanacak |
| 4 | **Lojik→günlük dil compiler ajanı** ("ai→ai" ∥ "ai→insan" rapor çifti) | **HİÇ KOŞULMADI** |
| 5 | **Ajanlar arası iletişimin graf tasarımı** | **HİÇ KOŞULMADI** (kısmi girdi: A10/13.2, A7/10.4) |
| 6 | **Araştırma ajanına hukuksal katman — tam tasarım** | **KISMEN** (A11 çerçeveyi kurdu, tasarım yok) |
| 7 | A8'in veri-füzyonu / truth-discovery şeridi | ailede açılmadı |
| 8 | A7'nin fine-tuning maliyeti + insan-onay kapısı şeritleri | ailede açılmadı |

### 20.4 Salih kararı bekleyenler

1. **Model A / B / C seçimi** (§16) — Carvis önerisi **B**.
2. **Kategori şeması:** iki eksen × 4 kademe + eksen-dışı YARGILANAMAZ (§11.5). Bu bir **kanon değişikliğidir** (m.40b'nin etiket sistemi) → Katman 1, yalnız Salih.
3. **Öğrenme ajanı** — tasarım paketi onayı (§18.a) ayrı, devreye alma (§18.b) ayrı karar.
4. **V59'un gerekçe değişimi:** maliyet tedbiri → **kalite tedbiri** (§13.4). Tetiği öne çekilsin mi?
5. **Fikir konseyi** — atlas ciddi itiraz getirdi (§19); fikir kutuda kalsın mı, dar haliyle mi denensin, düşsün mü?
6. **Ajan donma tedbirleri** (§8.4): (a) atlas ajanlarına "Bash ile bekleme/yoklama döngüsü YAZMA" kuralı — ölçülen iki patolojinin ikisi de bu; (b) `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS` düşürülsün mü (varsayılan 600.000 = Bash tavanıyla aynı, bu yüzden kör nokta üretiyor); (c) senkron alt-ajanlarda stall watchdog **yok** — senkron kullanımdan kaçınılsın mı?

### 20.5 Bu raporun kendi sınırı

Rapor **karar-öncesi tarama**dır, **kanıt değildir** (bölüm 0). Teknik [D] bulguları (Anthropic/Kubernetes/Temporal/FSRS/MISP/STIX/Google-AIS dokümanları ve kaynak kodları) bu kısıtın dışındadır ve doğrudan kullanılabilir. Akademik [K] bulguları borç-1 kapatılana dek **hüküm taşımaz**.
