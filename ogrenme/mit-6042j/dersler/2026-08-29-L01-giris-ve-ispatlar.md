# L1 — Introduction and Proofs (Giriş ve İspatlar)

> **Kaynak (BK-2, birebir):** MIT 6.042J F10, Ders 1 — anlatan Tom Leighton (video YouTube L3LMbpZIKhQ, ~44 dk; transkript arşivde: `static_resources/85c80331...L3LMbpZIKhQ.vtt`) + eşlik bölümü **Ch.1 Propositions** (`static_resources/7853d585...MIT6_042JF10_chap01.pdf`, Lehman-Leighton-Meyer). Lisans CC BY-NC-SA 4.0, © MIT OCW — atıflı Türkçe uyarlama; konular ve örnekler dersin/bölümün kendisi. Zaman damgaları videoya, §-numaraları bölüme işaret eder. Ritim: **ders-kaydı-önce** — bu kayıt sıfırdan anlatır, video destek.
> **Yapı:** Kısım A = dersin (video) birebir akışı · Kısım B = Ch.1'in derste anlatılmayan bölümleri. "NEDEN" blokları Salih emrinin icrasıdır: her iddianın gerekçesi.

---

# KISIM A — Dersin akışı (Leighton, 0:00–44:01)

## Blok 1 — İspat nedir? (0:00–8:22)

Leighton dersi bir soruyla açar: **ispat (proof) nedir?** Bir öğrencinin cevabı ("varsayımlardan sonuçlara götüren, her biri öncekilere mantıkça dayanan ifade zinciri") matematiksel ispatın ta kendisidir; ama Leighton önce ÜST kavramı kurar: her alanda ispat = **doğruluğu tespit etme yöntemi (method for ascertaining truth)**. Toplumun yöntem listesi (dersin kendi örnekleriyle):

| Yöntem | Alan | Dersin örneği |
|---|---|---|
| Gözlem/deney | fizik | tebeşir yere düşer → yerçekimi "doğru" |
| Örnekleme/karşı-örnek | istatistik vb. | 10 deneyde hep aynı sonuç → "doğru sayılır" |
| Jüri/yargıç kararı | hukuk | Clemens/Blagojevich/OJ davaları |
| Tanrı sözü (din) | inanç | yorumcuya bağımlı, çelişen "doğrular" |
| Otorite sözü | iş/okul | patron/müşteri/hoca haklıdır — **"burada geçmez"** |
| İç kanaat | yazılım(!) | "benim programımda bug yok" · "yanlış olduğunu görmüyorum" (ispat yükünü karşıya atar) |

Leighton'ın vurgusu (6:00): matematiğin güzelliği — **en genç öğrenci en kıdemli profesöre karşı argüman kazanabilir**; otorite değil, ispat kazanır.

**Matematiksel ispatın tanımı (dersin tahtaya yazdığı, 6:00 sonu):**
> **Matematiksel ispat**, bir **önermenin (proposition)**, bir **aksiyom (axiom)** kümesinden başlayan bir **mantıksal çıkarım (logical deduction)** zinciriyle doğrulanmasıdır.

Üç bileşen: önermeler · mantıksal çıkarımlar · aksiyomlar. Dersin kalanı bu üçünü sırayla işler.

**❓NEDEN bu tanım?** Diğer yöntemlerin hepsi ya gözleme (sonlu örneklem), ya yetkiye, ya kanaate dayanır — üçü de aşağıda görüleceği gibi keyfî büyüklükteki iddialarda ÇÖKER (Blok 2'nin p(n) örneği bunun kanıtı). Zincir+aksiyom modeli ise doğruluğu, aksiyomları kabul eden HERKESİN takip edebileceği nesnel adımlara indirger — otoriteyi denklemden çıkarır.

**Kontrol 1:** "İç kanaat" yönteminin dersin verdiği tehlikesi neydi? (ispat yükü kavramıyla)

## Blok 2 — Önerme; "40 örnek yetmez" (8:22–20:01)

**Tanım (ders + §1 aynı):** **Önerme** = doğru YA DA yanlış olan bir ifade. (İkisinden biri; hangisi olduğunu bilmiyor olabilirsin.) Örnek: $2+3=5$ (doğru).

**Dersin baş örneği:**
$$\forall n \in \mathbb{N}.\;\; n^2 + n + 41 \text{ asaldır}$$
- $\forall$ = "her ... için" (**evrensel niceleyici**, for all); $\mathbb{N} = \{0,1,2,3,\dots\}$ doğal sayılar = **evren (universe of discourse)**; "$n^2+n+41$ asaldır" kısmı = **yüklem (predicate)** — doğruluğu $n$ değişkenine bağlı önerme.
- **Asal (prime):** yalnız kendisine ve 1'e bölünen, 1'den büyük tamsayı. ⌥ *Carvis notu: videoda Leighton "1, 3, 5, 7 asal" der (10:00) — sürç-ü lisan: kursun kendi tanımı (Ch.1 §1.3.1) "1'den büyük" der, 1 asal DEĞİLDİR; 2 de asaldır. Kayda bölümün tanımı esas alındı.*

**Elle kontrol (dersin tablosu):** $p(n) ::= n^2+n+41$ ("$::=$" = tanım gereği eşit, §1.3.1 dipnotu):
| $n$ | 0 | 1 | 2 | 3 | ... | 20 | ... | 39 |
|---|---|---|---|---|---|---|---|---|
| $p(n)$ | 41 | 43 | 47 | 53 | ... | 461 | ... | 1601 |
| asal? | ✓ | ✓ | ✓ | ✓ | ... | ✓ | ... | ✓ |

**İlk 40 değer asal.** Fizikte/istatistikte 40 örnek "fazlasıyla yeter" — ya burada? **HAYIR:** $n=40$'ta
$$p(40) = 1600 + 40 + 41 = 1681 = 41^2 \quad \text{— asal değil.}$$
**❓NEDEN tam 40'ta kırılıyor?** Cebir gerekçeyi gösterir: $n^2+n+41 = n(n+1)+41$. $n=40$'ta $40 \cdot 41 + 41 = 41 \cdot (40+1) = 41^2$ — 41 çarpanı iki terimde de belirir. $n=41$ "bariz" durumdur (dersin sorusu): $41^2+41+41 = 41(41+1+1) = 41 \cdot 43$. **Dersin mesajı: sonsuz küme hakkındaki iddia, SONLU örneklemle kanıtlanamaz — örneklem ne kadar büyük olursa olsun** (bu, Blok 1'deki "gözlem yöntemi neden matematikte geçersiz" iddiasının ispatıdır).

**Aynı mesajın ağırlaştırılmış dozları (dersin sırasıyla):**
1. **Euler sanısı (1769):** "$a^4+b^4+c^4=d^4$'ün pozitif tamsayı çözümü yoktur." 218 yıl açık kaldı; **1987'de Noam Elkies** çürüttü: $a{=}95800,\; b{=}217519,\; c{=}414560,\; d{=}422481$. Doğru önerme: $\exists\, a,b,c,d \in \mathbb{Z}^+.\; a^4+b^4+c^4=d^4$ ($\exists$ = "vardır", **varlıksal niceleyici**).
2. **$313(x^3+y^3)=z^3$ pozitif tamsayı çözümsüzdür** → YANLIŞ, ama en küçük karşı-örnek **1000+ basamaklı** — kaba kuvvet/bilgisayar taramasıyla asla bulunamazdı. **❓NEDEN umursayalım (dersin kendi cevabı, 18:02):** bu bir **eliptik eğri** örneği; eliptik eğriler büyük tamsayı **çarpanlama**nın anahtarı, çarpanlama **RSA** kripto-sistemini kırmanın yolu — bu yüzden RSA modülleri 100 basamaktan 1000 basamağa çıktı (kursun Ch.4/L4-5'te işleyeceği hat).
3. **Dört Renk Teoremi:** "Her harita, komşu bölgeler farklı renkte olacak şekilde 4 renkle boyanır." Tarihçe: Guthrie sanısı 1853 → **Kempe'nin resimli 'ispatı' 1879, 10+ yıl inanıldı** → Heawood ölümcül hatayı buldu → Appel-Haken 1977, **bilgisayarla binlerce durum** (matematikçileri rahatsız etti: makine doğru yaptı mı?) → 12 sayfalık insan-ispatı iddiası hâlâ şüpheli ("ana lemmanın detayı okura bırakılmıştır, bkz. şekil 7"). Dersin uyarısı: **resimle ispat ikna edici ve genellikle YANLIŞTIR** (beyin "böyle görünmek zorunda" diye kilitlenir; L2 açılışında kasıtlı sahte PowerPoint-ispatı gelecek).
4. **Goldbach sanısı (1742):** "2'den büyük her çift tamsayı iki asalın toplamıdır" ($24 = 11+13$). Doğru mu? **KİMSE BİLMİYOR** — 283 yıldır açık. Gazete köşesi (Boston Globe) örneği: "20 = 9+11" yazmış — 9 asal değil; **"okuduğun her şeye inanma"** dersin tekrar edeceği tema. Riemann hipotezi (1,5 milyar sıfır doğrulanmış — sonsuz için yine yetmez) ve Poincaré sanısı/Perelman hikâyesi (2003 ispat; Fields + 1M$ Millennium ödülü, ikisini de reddetti) aynı parantezde anlatılır.

**Kontrol 2:** $p(n)=n(n+1)+41$ çarpanlamasından yola çıkarak $p(41k-1)$ ya da $p(41k)$ biçimindeki HER değerin 41'e bölündüğünü göster. (cevapta)

## Blok 3 — İmplikasyon ve ancak-ve-ancak (28:06–34:00)

**Basit doğru örnek:** $\forall n \in \mathbb{Z}.\; (n \ge 2 \;\text{IMPLIES}\; n^2 \ge 4)$ — $\mathbb{Z}$ = tamsayılar $\{0, \pm1, \pm2, \dots\}$.

**Tanım (dersin tahtası):** "$p$ IMPLIES $q$" önermesi, **$p$ yanlışsa YA DA $q$ doğruysa** doğrudur. Doğruluk tablosu (truth table):
| $p$ | $q$ | $p \Rightarrow q$ |
|---|---|---|
| D | D | **D** |
| D | Y | **Y** |
| Y | D | **D** |
| Y | Y | **D** |

Dersin ünlü örneği: *"Domuzlar uçarsa kralım" — domuzlar uçmadığı için önerme DOĞRU* (kral olup olmamamdan bağımsız).
**❓NEDEN "yanlış her şeyi gerektirir" (F ⇒ her şey = D)?** (1) Tanımın tek cümlelik özü (bölümün kendi cümlesi, §1.1.2): *implikasyon, tam olarak "eğer-kısmı yanlış VEYA o-halde-kısmı doğru" iken doğrudur* — evrensel iddiaların çalışması için bu şart: "$n \ge 2 \Rightarrow n^2 \ge 4$" HER tamsayıda doğru olmalı; $n=0$'da öncül yanlış, iddia o örnek hakkında hiçbir şey söylemiyor — cezalandırılmamalı. (2) Aksi tanımlar tutarlılığı bozar: (Y,D) satırını Y yapsaydın, "$n \ge 2 \Rightarrow n^2 \ge 4$" $n=-3$'te ($n^2{=}9{\ge}4$ ama $n{<}2$) yanlış olurdu — oysa iddianın matematik içeriği sağlam. 6.006 L1'deki "vacuous truth" (boş yere doğruluk) taban durumu da tam bu satırdır — iki kurs aynı mekanizmada buluşur.

**IFF (ancak ve ancak):** $\forall n \in \mathbb{Z}.\; (n \ge 2 \iff n^2 \ge 4)$ — **YANLIŞ**; karşı-örnek $n=-3$: $(-3)^2 = 9 \ge 4$ ✓ ama $-3 \ge 2$ ✗. **❓NEDEN iki yön ayrı ayrı denetlenir:** $p \iff q$ tanımca $(p \Rightarrow q) \wedge (q \Rightarrow p)$; ders tabloyu elle genişletir:
| $p$ | $q$ | $p{\Rightarrow}q$ | $q{\Rightarrow}p$ | $p \iff q$ |
|---|---|---|---|---|
| D | D | D | D | **D** |
| D | Y | Y | D | **Y** |
| Y | D | D | Y | **Y** |
| Y | Y | D | D | **D** |

Yani IFF = "ikisi de doğru VEYA ikisi de yanlış". *(⌥ tarih notu: Leighton tahtada bir hücreyi yanlış doldurup sınıf önünde düzeltir, 32:00 — Blok 1'deki "hoca da yanılır, ispat kazanır" ilkesinin canlı örneği.)*

**Her cümle önerme midir? (34:00)** Hayır: "Bu cümle yanlıştır" (doğruysa yanlış, yanlışsa doğru — çelişki; ne doğru ne yanlış) · "Merhaba" (soru/ünlem — doğruluk değeri yok). Bu kursta uğraşılacak her şey pratikte önermedir.

**Kontrol 3:** "$n \ge 2 \Rightarrow n^2 \ge 4$" önermesi $n=0$, $n=3$, $n=-3$ için tablonun hangi satırına düşer?

## Blok 4 — Aksiyomlar, tutarlılık, tamlık, Gödel (34:00–44:01)

**Tanım:** **Aksiyom** = doğru olduğu VARSAYILAN önerme. (Yunanca kökü: "kayda değer bulmak" — ispatı yok, makul bulduğun için kabul edersin.)
- "Matematikte varsayım yapma" öğüdü YANLIŞTIR (dersin kendi ifadesi): varsayım yapmadan hiçbir şey kanıtlayamazsın; marifet **varsayımlarını AÇIKÇA beyan etmektir** — aksiyomlarını kabul eden herkes ispatını izleyip sonucuna KATILMAK ZORUNDA kalır; itiraz edecekse aksiyoma eder.
- Örnek aksiyom: $a=b \wedge b=c \Rightarrow a=c$ (ispatı yok; makul, kabul).
- **Aksiyomlar bağlama göre çelişebilir ve bu MEŞRUDUR** (dersin üç geometrisi): $L$ doğrusu ve üzerinde olmayan $p$ noktası için — Öklid: $p$'den $L$'ye paralel **tam bir** doğru geçer · küresel: **hiç** geçmez · hiperbolik: **sonsuz tane** geçer. Üçü de kendi zemininde (düzlem/küre/hiperbolik yüzey) tutarlıdır; şart, hangi zeminde olduğunu BEYAN etmek. *(⌥ MF-P3 bağlantısı: mat-felsefesi serisinin Kant dersindeki Öklid-dışı geometri sarsıntısı tam bu tablo.)*

**İki yol gösterici ölçüt:**
- **Tutarlılık (consistency):** hiçbir önerme hem doğru hem yanlış KANITLANAMAZ. ❓NEDEN şart: aynı önerme iki yönde de kanıtlanabiliyorsa sistemdeki her "ispat" değersizleşir.
- **Tamlık (completeness):** her önermenin doğruluğu YA DA yanlışlığı kanıtlanabilir. ❓NEDEN istenir: hiçbir soru cevapsız kalmaz.

**Gödel (1930'lar, dersin kapanış bombası):** ikisi birden OLMAZ — (aritmetiği içerecek güçte) hiçbir aksiyom kümesi hem tutarlı hem tam olamaz. Russell ve Whitehead kariyerlerini bu "kutsal kâseye" verdi; Gödel "kâse yok" dedi. Sonuç: **tutarlılık vazgeçilmez olduğuna göre, doğru olup ASLA kanıtlanamayacak olgular vardır** — belki Goldbach onlardan biri. (Dersin şakası: "ödevlerde bunlardan sormamaya çalışacağız." — ve: "Ailen 'yeterince çalışırsan her şeyi yapabilirsin' dediyse... yanılmışlar.") *(⌥ Bu teoremin şartlı-kesin ifadesi ve kötüye-kullanım freni mat-felsefesi MF-P8'in konusu; ders burada bilinçli olarak kabaca anlatıyor, kurs da "logic dersinde kanıtlanır" diye işaretliyor.)*

**Kontrol 4:** "Aksiyom seçimi serbestse matematik keyfî olmaz mı?" — dersin buna cevabı hangi mekanizma?

---

# KISIM B — Ch.1'in derste anlatılmayan bölümleri (birebir, bölüm sırasıyla)

## B1 — Bileşik önermeler: NOT/AND/OR/XOR (§1.1, §1.1.1)
Gündelik dilin belirsizliği matematikte taşınamaz (bölümün 4 örnek cümlesi: "pasta YA DA dondurma alabilirsin" — ikisi birden olur mu?; "her Amerikalının bir hayali var" — aynı hayal mi?). Çözüm: bağlaçları **doğruluk tablosuyla** kesin tanımla. $P, Q$ **Boole değişkenleri** (D/Y):
| $P$ | $Q$ | NOT($P$) | $P$ AND $Q$ | $P$ OR $Q$ | $P$ XOR $Q$ |
|---|---|---|---|---|---|
| D | D | Y | D | D | Y |
| D | Y | Y | Y | D | D |
| Y | D | D | Y | D | D |
| Y | Y | D | Y | Y | Y |

❓NEDEN "OR" ikisi-birden'i içerir (satır 1): matematik yazımının STANDART tanımı kapsayıcıdır — "pasta veya dondurma" diyen matematikçi ikisini birden de kastediyor OLABİLİR der; dışlamak istiyorsan **XOR** (exclusive-or) kullanırsın. Gündelik dil-matematik dil ayrımının ilk resmî noktası.

## B2 — Sembolik gösterim (§1.1.4)
| Türkçe/İngilizce | Sembol |
|---|---|
| NOT($P$) | $\neg P$ (ya da $\overline{P}$) |
| $P$ AND $Q$ | $P \wedge Q$ |
| $P$ OR $Q$ | $P \vee Q$ |
| $P$ IMPLIES $Q$ / if $P$ then $Q$ | $P \longrightarrow Q$ |
| $P$ IFF $Q$ | $P \longleftrightarrow Q$ |

Örnek (bölümün kendisi): "If $P$ AND NOT($Q$), then $R$" $\;=\;(P \wedge \overline{Q}) \longrightarrow R$. *(⌥ m.38 lojik-çeviri bağlacı setimizle aynı aile — Jarvis kural yazımı bu dili kullanıyor.)*

## B3 — Karşıt-ters, ters, IFF bağı (§1.1.5)
- **Karşıt-ters (contrapositive):** "$P \Rightarrow Q$" $\;\equiv\;$ "$\neg Q \Rightarrow \neg P$" — tabloda sütunlar birebir aynı (bölüm "açsam huysuzum" ≡ "huysuz değilsem aç değilim" örneğiyle elle doğrular). ❓NEDEN eşdeğer: $P \Rightarrow Q$ yalnız (D,Y) satırında yanlış; $\neg Q \Rightarrow \neg P$ de yalnız $\neg Q{=}$D,$\neg P{=}$Y yani aynı (D,Y) satırında yanlış.
- **Ters (converse):** "$Q \Rightarrow P$" — EŞDEĞER DEĞİL (tablo farklı; "huysuzsam açımdır" başka bir iddia).
- İmplikasyon + tersi birlikte $=$ IFF (bölüm bunu 4 sütunlu tabloyla doğrular; Kısım A Blok 3'teki tablo).

## B4 — Programlarda önerme mantığı (§1.2)
Bölümün kod örneği: `if ( x > 0 || (x <= 0 && y > 100) )`. $A ::= (x>0)$, $B ::= (y>100)$ koy → koşul $= A \vee (\neg A \wedge B)$. Doğruluk tablosu bunun $A \vee B$'ye **mantıkça eşdeğer** olduğunu gösterir → kod `if ( x > 0 || y > 100 )` diye sadeleşir, davranış DEĞİŞMEZ. ❓NEDEN önemli (bölümün kendi gerekçesi): yazılımda sadeleştirme hız; çip tasarımında aynı problem "kapı sayısını azalt" olarak görülür — daha az eleman = küçük, ucuz, az arızalı çip.

## B5 — Yüklemler ve niceleyiciler, tam gösterim (§1.3.2–§1.3.4)
- **Yüklem:** değişkene bağlı önerme; $P(n) ::= $ "$n$ tam karedir" → $P(4)$ doğru, $P(5)$ yanlış. **Uyarı (bölümün vurgusu):** $P(n)$ doğruluk değeri döndürür; sıradan fonksiyon $p(n)=n^2+n$ SAYI döndürür — ikisini karıştırma.
- "Her zaman doğru" / "bazen doğru" kalıpları: $\forall x \in D.\; P(x)$ (evrensel) · $\exists x \in D.\; P(x)$ (varlıksal). Örnekler (bölümün): $\forall x \in \mathbb{R}.\; x^2 \ge 0$ · $\exists x \in \mathbb{R}.\; 5x^2 - 7 = 0$ (doğru: $x = \pm\sqrt{7/5}$).
- Karışık kullanım meşru: niceleyicili ifadeler de önermedir, $\wedge, \vee, \Rightarrow$ ile birleşir ("her problemi çözersen A alırsın" cümlesinin iki okuması: $(\forall x.\,\text{Solves}(x)) \Rightarrow G$ vs $(\exists x.\,\text{Solves}(x)) \Rightarrow G$ — belirsizliğin formülle çözülüşü).

## B6 — Niceleyici SIRASI ve değilleme (§1.3.5–§1.3.8) — bölümün en kritik tekniği
- **Goldbach'ın tam formül hali** (bölümün kendisi; Evens = 2'den büyük çiftler, Primes = asallar):
$$\forall n \in \text{Evens}.\;\; \exists p \in \text{Primes}\; \exists q \in \text{Primes}.\;\; n = p+q$$
- **Sıra değişirse anlam değişir:** $\exists p,q.\, \forall n.\; n = p+q$ = "AYNI iki asal her çifti toplar" — bariz yanlış. Bölümün ikinci örneği: "Her Amerikalının bir hayali var": $\exists d\, \forall a.\, H(a,d)$ (ortak tek hayal) $\neq$ $\forall a\, \exists d.\, H(a,d)$ (herkesin kendi hayali).
- **Geçerli yön ve ispatı (§1.4'ten, elle):** $\exists x \forall y.\, P(x,y) \Rightarrow \forall y \exists x.\, P(x,y)$ **geçerlidir**: $\exists$ tanımıyla bir $d_0$ var, her $y$ için $P(d_0,y)$; o halde her $y$ için tanık olarak $d_0$ göster. **Ters yön geçersiz** — **karşı-model (counter model)**: evren $=\mathbb{Z}$, $P(x,y) ::= x > y$: her $y$ için $x=y+1$ var (öncül D) ama tüm tamsayılardan büyük tek $x$ yok (sonuç Y). ❓NEDEN "karşı-model" kavramı: geçerlilik HER yorumda doğruluk ister; tek bir yorumda düşürmek yıkmaya yeter.
- **Değilleme kuralı:** $\neg(\forall x. P(x)) \equiv \exists x. \neg P(x)$ ve $\neg(\exists x. P(x)) \equiv \forall x. \neg P(x)$ — **"değil, niceleyicinin üzerinden geçerken türünü değiştirir"** (bölümün cümlesi; örnek: "herkes snowboard sevmez" ≡ "sevmeyen biri var").

## B7 — Geçerlilik ve sağlanabilirlik (§1.4–§1.5)
- **Geçerli (valid) formül:** değişkenlerin HER atamasında D — örnek: dağılma yasası $P \wedge (Q \vee R) \iff (P \wedge Q) \vee (P \wedge R)$; bölüm 8 satırlık tabloyla elle doğrular ($2^3$ atama, iki sütun birebir aynı).
- **Sağlanabilir (satisfiable):** EN AZ BİR atamada D — $P \wedge \overline{Q}$ sağlanabilir; $P \wedge \overline{P}$ sağlanamaz.
- **SAT problemi:** verilen önermenin sağlanabilirliğine karar ver. Tablo yöntemi $2^n$ satır (30 değişken > 1 milyar satır — bölümün kendi hesabı). Polinom-zamanlı çözüm var mı? **KİMSE BİLMİYOR = P vs NP** — teorik bilgisayar biliminin bir numaralı açık sorusu, Clay Millennium 1M$ ödüllerinden biri. ❓NEDEN dünya-değiştirir (bölümün gerekçesi): SAT'a verimli çözüm paketleme/çizelgeleme/devre-doğrulamaya verimli çözüm demek — VE şifreli mesajların çoğunun kırılması, çevrimiçi finansın çöküşü demek. *(⌥ 6.006 bağlantısı: "verimli = polinom" tanımı ve L19-L20 karmaşıklık dersleri bu ipin ucu; iki kurs aynı soruya iki uçtan geliyor.)*

---

## Kontrol cevapları
1. "Yanlış olduğunu görmüyorum" ispat YÜKÜNÜ karşı tarafa devreder: sen kanıt sunmazsın, itiraz edenin çürütmesi beklenir — yöntem değil, yöntemsizliktir.
2. $p(n) = n(n+1)+41$. $n=41k$ için: $41k(41k+1)+41 = 41[k(41k+1)+1]$ — 41 böler. $n=41k-1$ için: $(41k-1)(41k)+41 = 41[k(41k-1)+1]$ — 41 böler. Her iki ailede $p(n) > 41$ olduğundan asal olamaz (41 gerçek bölen).
3. $n=0$: (Y,Y) satırı → D (boş yere) · $n=3$: (D,D) → D · $n=-3$: (Y,D) → D. Üçü de doğru; implikasyonu yanlışlayacak tek satır (D,Y) hiçbir tamsayıda gerçekleşmez — önerme bu yüzden $\forall$ ile doğru.
4. Beyan mekanizması: aksiyom seçimi serbesttir ama AÇIK beyan zorunludur; ispat "aksiyomları kabul edeni sonuca mecbur bırakır." Keyfîlik aksiyom katmanında kalır, çıkarım katmanına sızamaz; ayrıca tutarlılık ölçütü seçimi disipline eder (üç geometri örneği: her küme kendi zemininde tutarlı).

## Durum
- Bulanık blok bildirimi bekleniyor (Kısım+numara ile, ör. "A2, B6"). Sonraki ders: **L2 Induction** (Ch.2 Patterns of proof + Ch.3 Induction; L2 açılışında Leighton'ın söz verdiği sahte "PowerPoint ispatı" var). İlerleme: [ilerleme.md](../ilerleme.md)
