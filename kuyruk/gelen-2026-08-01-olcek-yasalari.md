# COWORK DEVİR DOSYASI — ÖLÇEK YASALARI / AJAN UYARLAMASI

> **HAM FİKİR / PC'de ingest edilecek.** Bu dosyayı chat yüzeyindeki Carvis (snapshot oturumu) hazırladı; kanon değildir, `C:\JARVIS` altına ingest edilene kadar hiçbir maddesi kural sayılmaz.
> **Hazırlayan:** Carvis / chat yüzeyi — Claude Opus 5 · **Talep eden:** Salih (Patron) · **Tarih:** 2026-08-01
> **Ek dosya:** `olcek-yasalari-notr-damitma.md` (ayrıntılı damıtma; bu dosya onun devir özetidir ve tek başına yeterlidir).

---

## §0 — Salih'in niyeti (Patron beyanı)

Bir ölçek-yasaları kaynağını (Veritasium / Geoffrey West *Scale*) JARVIS projesinde **metafor olarak** kullanmak istiyorum. Kaynak baştan sona biyoloji-kökenli; ham haliyle kanona sokarsam bağlam hijyeni kararımı (07-13 tam-süpürme) ihlal eder ve model düşümüne yol açar. Bu yüzden önce nötrleştirilmiş bir damıtma çıkarttım, sonra ajanlara uyarlanmış bir formül iskeleti kurdurdum.

Şimdi istediğim şey **araştırmanın kendisi değil, araştırmanın koşulacağı hazırlık.** Cowork bu dosyadaki bilgiyi alacak ve bana **yalnız iki çıktı** verecek: CC'ye gidecek görev raporu ve araştırma promptu. Araştırmayı Cowork koşmayacak.

---

## §1 — Şimdiye kadar ne yapıldı

1. Ham transkript okundu (Veritasium, "Why does every mammal get 1 billion heartbeats in their life?", 2026-07-25 · Geoffrey West, *Scale* temelli).
2. Transkriptin ham ingest'i **reddedildi**: sorun kelimeler değil, iddiaların biyolojik otoriteyle taşınması.
3. Kaynak, kopyalanmadan **yeniden türetildi**: her iddia matematiksel forma indirildi, terimler nötr karşılıklarıyla değiştirildi, çevrilemeyenler karantinaya alındı. Çıktı: `olcek-yasalari-notr-damitma.md` (§1 sözlük, §2 yapısal çekirdek, §3 epistemik durum, §4 P1–P5 önermeleri, §5 Ö1–Ö4 ölçüm askıları, §6 karantina, §7 açık kararlar).
4. Üzerine **ajan uyarlaması** kuruldu: ortak uç-birim adayı belirlendi, debi formülü yazıldı, iki ölçülebilir üs (γ ve θ) tanımlandı, invaryantın koşulu türetildi.
5. Bu dosya, 3 ve 4'ün Cowork'e devri için hazırlandı.

**Kritik uyarı, baştan:** Elde şu an metafor ve türetilmiş form var; **ölçülmüş tek bir sayı yok.** Araştırmanın işi bu formu doldurmak, doğrulamak değil.

---

## §2 — Nötr sözlük (kanon dili adayı)

| Kaynaktaki kavram | Nötr karşılık | Sembol | Ajan karşılığı |
|---|---|---|---|
| kütle | ölçek | S | toplam parametre sayısı |
| metabolizma hızı | kaynak-tüketim debisi | B | karar-noktası başına hesap |
| hücre | uç-birim | — | dikkat başlığı |
| organizma | koşum-sistemi | — | bir model konfigürasyonu |
| dolaşım ağı | dağıtım ağı | — | bağlam taşıma yolu |
| kan | taşınan kaynak | — | token / bağlam |
| uç damar genişliği | uç-birim invaryantı | d_head | başlık boyutu |
| kalp atış hızı | çevrim frekansı | f | birim bütçedeki karar sayısı |
| ömür | kullanım ufku | T | bozulma öncesi etkin bağlam |
| toplam atış | toplam çevrim bütçesi | N = f·T | konfigürasyon başına toplam karar |
| hasar birikimi | birikimli bozulma | — | bağlam kirlenmesi, drift |
| evrimin verimliliğe itmesi | ardışık-deney araması | — | mimari iterasyonu |
| tür | sistem-ailesi | — | model ailesi |

---

## §3 — Yapısal çekirdek (kaynaktan türetilen, nötr)

**Üs yasası:** Y = c·S^α. log-log düzleminde düz çizgi, eğim = α. α<1 alt-doğrusal, α>1 üstü-doğrusal.

**Doğrusallık hatası:** yanlış üsle yapılan tahsisin hata çarpanı = (ölçek oranı)^(α_varsayılan − α_gerçek). Ölçek farkı büyüdükçe hata katlanır. *Örnek: oran 1000, varsayım α=1, gerçek α=0.75 → 5.6× aşırı tahsis.*

**Çeyrek-üs ailesi ve invaryant:** B ∝ S^(3/4) ise f = B/S ∝ S^(−1/4), T ∝ S/B ∝ S^(1/4), dolayısıyla N = f·T = sabit. Frekans ve ufuk aynı bütçenin iki ucudur; üsler birbirini götürür.

**Türetimin dayandığı üç öncül:** (1) dağıtım ağı boşluk-doldurucudur; (2) **uç-birim genişliği ölçekten bağımsız sabittir**; (3) ağ maliyet-minimuma yakınsamıştır. Öz-benzer dallanma etkin yüzeyi L³ gibi davrandırır → L ∝ S^(1/4) → B ∝ S^(3/4).

**Üs / sabit ayrımı:** hijyen iyileştirmesi (pointer, kapsül, damıtma) **sabiti** büyütür; mimari değişimi **üssü** değiştirir. Karıştırmak, hijyen çalışmasını mimari atılım sanmaya yol açar.

**Ölçek-kârlılık eşitsizliği:** (α_çıktı > α_maliyet) → büyüt · (α_çıktı ≤ α_maliyet) → durdur ∧ mevcut ölçekte damıt.

**Epistemik durum:** kaynak alanında üssün 2/3 mü 3/4 mü olduğu bir asırdır tartışmalı; ölçüm zor, hata çubukları iki değeri de kapsıyor; üs rejim-bağımlı olabilir. 1960'larda bir sempozyumda üs **29-0 oyla** sabitlenmiş. **Uzlaşıyla sabitlenmiş üs, ölçülmüş üs değildir.** Bu dosyanın en aktarılabilir uyarısı budur.

---

## §4 — Ajan uyarlaması (araştırılacak asıl iskele)

### 4.1 Ortak uç-birim adayı

WBE'yi çalıştıran öncül "hücre" değil, **uç-birim invaryantı**. Ajanlarda token bu rolü taşıyamaz: bilgi birimi olarak ortak, iş birimi olarak değil (bir Haiku token'ı ile bir Opus token'ı arasında mertebe farkı var).

**Aday: d_head (bir dikkat başlığının vektör genişliği).** Modeller 100M'den 700B'ye çıkarken d_head 64–128 bandında kalıyor; büyüyen şey başlık *sayısı* ve katman sayısı. Yani mimari ölçeklenirken en ince uç birimini sabit tutup sayısını artırıyor — öncül (2)'nin birebir karşılığı.

> Bu bir benzetme değil, model kartlarından doğrulanabilir bir olgu iddiasıdır. **Araştırmanın ilk sağlaması budur.**

### 4.2 Debi formülü

```
B  ≈  A  +  κ·C
```
A = token başına aktif parametre · C = bağlam uzunluğu · κ = katman×başlık geometrisinden gelen sabit.

Birinci terim gövde bakım maliyeti, ikinci terim taşınan kaynağın uzunluğuyla artan dağıtım maliyeti. Dikkat maliyeti önbellekli üretimde bağlamla doğrusal, önbelleksiz ön-dolumda karesel. **Sonuç: iki rejim var, tek üs yok** — küçük bağlamda maliyeti model boyutu, büyük bağlamda bağlam uzunluğu belirler.

### 4.3 γ — bu alanın Kleiber üssü

Yoğun modelde A = S, yani B ∝ S¹: ölçek ekonomisi yok. Kazanç ancak seyreklikten gelir:

```
A ∝ S^γ ,  γ < 1   →   B ∝ S^γ
```

γ, yayınlanmış karışım-uzmanlı (MoE) modellerin **toplam/aktif parametre** çiftleri log-log'a basılarak ölçülebilir. Halka açık veri mevcut. İki bilinen nokta: Mixtral 8x7B ≈ 46.7B toplam / 12.9B aktif · DeepSeek-V3 ≈ 671B / 37B. Bu ikisi tek başına γ ≈ 0.4 veriyor — **anlamsız** (iki nokta, farklı laboratuvar, farklı yıl), ama yöntemin koşulabilirliğini gösteriyor. 15–20 nokta gerçek bir eğim verir.

### 4.4 θ ve invaryantın koşulu

Etkin bağlam kapasitesi C_max ∝ S^θ ve ufuk bağlam bozulmasıyla sınırlıysa:

```
f ∝ 1/B ∝ S^(−γ)
T ∝ C_max ∝ S^θ
N = f·T ∝ S^(θ − γ)
```

**Ajan başına toplam karar bütçesi ancak θ = γ ise ölçekten bağımsız sabittir.** "Her memelinin bir milyar atışı"nın ajan karşılığı tam olarak bu eşitliktir — falsifiable, iki ölçülebilir üsle ifade edilmiş.

### 4.5 Beklenti (kayda geçirilmiş, araştırma öncesi)

**θ = γ'yi beklemek için sebep yok.** Biyolojide invaryant tek bir optimize dağıtım ağından zorunlu olarak çıkıyor; üsler aynı ağdan türediği için götürüyor. Modellerde seyreklik ve bağlam uzunluğu **bağımsız tasarım kollarıdır** — farklı ekipler, farklı yıllar, farklı kısıtlar. Ortak bir kısıttan türemiyorlar.

En olası sonuç invaryantın **tutmaması**; bu metaforun başarısızlığı değil, en değerli çıktısıdır. Çünkü θ − γ farkının **işareti** doğrudan bir mühendislik kararı verir:

```
(θ > γ)  →  büyük model başına karar bütçesi ölçekle artar  →  büyütmek kârlı
(θ < γ)  →  büyümek karar bütçesini yakar  →  çok sayıda küçük ajan
(θ = γ)  →  invaryant  →  seçim hız/ufuk tercihine indirgenir
```

Bu beklenti araştırmadan **önce** yazıldı; sonuç ne çıkarsa çıksın senaryo-defterine bu haliyle işlenecek (post-hoc uyarlama yasak).

---

## §5 — Karantina: kanona GİRMEYECEKLER

- Kaynaktaki canlı/organ/tür adları, doz anlatısı, tüm biyolojik örnekler.
- "1 milyar" rakamının bir JARVIS büyüklüğü olarak anılması.
- 3/4, 1/4, 0.85, 1.15 sayılarının JARVIS parametresi olarak kullanımı — başka bir alanın ölçümleridir.
- "Sistem canlıdır / nefes alır / yaşlanır / ölür" türü ifadeler.
- Bozulma-birikimi → ufuk nedenselliğinin doğrudan aktarımı (kaynağında bile yalnız önde gelen bir teori).
- §4.3'teki γ ≈ 0.4 tahmininin sonuç gibi taşınması.

---

## §6 — COWORK'E DEVİR

Bu bölüm bir şartname değil, devir notudur. **Kapsamı, soruları, kabul kriterlerini ve sınırları sen belirleyeceksin** — bu dosya sana ne yaptığımızı ve nereye varmak istediğimizi veriyor, nasıl varılacağını değil.

### Hedef

Yukarıdaki iskeleti ölçülebilir bir araştırma görevine dönüştürmek. Nihai olarak öğrenmek istediğim şey tek cümleyle şu: **ajanlarda frekans–ufuk invaryantı tutuyor mu, tutmuyorsa farkın işareti ne** — çünkü o işaret doğrudan bir model-seçimi ve ölçek kararı veriyor (§4.5). Buraya giden yol senin kararın; §4'teki üç açık uç (uç-birim invaryantı, γ, θ) benim adaylarım, zorunlu değil. Daha iyi bir ayrıştırma görüyorsan onu kur ve gerekçesini yaz.

### Senden istediğim iki çıktı

1. **CC görev raporu** — `cc/` köprü kanalına düşecek, koşulabilir hale getirilmiş görev.
2. **Araştırma promptu** — o görevi koşacak ajana verilecek prompt.

Bunların içeriğini, bölümlenmesini ve ne kadar sıkı sınırlanacağını sen seçeceksin. Araştırmayı **koşma**; bu oturumun işi hazırlık.

### Pazarlığa kapalı olanlar

Aşağıdakiler senin takdirine bırakılmıyor; geri kalan her şey serbest.

- **Tanım-of-done push'lanmış commit'tir (m.9).** Plan, taslak ve analiz metni tamamlanma sayılmaz.
- **Rakam disiplini (m.39):** ölçülemeyen yere "ölçülemedi" yazılır, tahmin üretilmez. Her sayı belirsizliğiyle birlikte raporlanır.
- **§5 karantinası:** biyolojik dil ve kaynak alanın sayıları (3/4, 1/4, 0.85, 1.15) ile §4.3'teki γ ≈ 0.4 tahmini hiçbir çıktıya çapa olarak giremez. Çıktılar §2 sözlüğüyle yazılır.
- **§4.5 beklentisi olduğu gibi taşınır.** Araştırma öncesi yazılmış bir kayıttır; sonuç ne çıkarsa çıksın post-hoc uyarlanmayacak. Hipotez gibi değil, tarih kaydı gibi aktarılsın.
- **§7'deki açık kararlar (Katman 1) senin değil.** Kapatma; gerekiyorsa seçenekleri sunup önerileni işaretle (m.37), kararı Salih verir.
- **Kanon dosyalarına yazma.** Bu dosya damgalı ham fikirdir.

### Bana sorman gereken varsa sor

Kapsamı daraltmak için bir cevaba ihtiyacın varsa sorularını topluca sor — ama cevabın çıktıyı değiştirmeyeceği yerde sorma (m.4). Kendi künyeni (hangi model, hangi tarih) her iki çıktının başına yaz; bu, katman karşılaştırması için biriktirdiğim veridir.

---

## §7 — Salih'e açık kararlar (Katman 1, çözülmeden ingest yok)

- **K1** — §2 sözlüğündeki 13 satır kanon nötr sözlüğüne eklenecek mi?
- **K2** — Bu dosya ve eki nereye iner: wiki mi, kapsül mü, senaryo-defteri eki mi?
- **K3** — Ölçümler K-002'ye mi (ölçüm bankı) yoksa prototip vardiyasına mı yazılacak? Prototip ufku ~10 Ekim.
- **K4** — θ (etkin bağlam ölçeklemesi) en pahalı ve ölçütü en tartışmalı uç. Üç uç birden mi koşulacak, yoksa uç-birim sağlaması + γ ile başlanıp θ ikinci tura mı bırakılacak?

---

*Damga: HAM FİKİR / PC'de ingest edilecek. Hazırlayan: Carvis / chat yüzeyi — Claude Opus 5, 2026-08-01. §7 kararları çözülmeden kanon katmanına indirilmez.*
