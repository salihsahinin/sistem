# Önerme Formu — anlaşılırlık kaygısı olmadan

> **Bu üçüncü register'dır.** Teknik sürüm kanıt için, insan sürümü anlamak için, bu sürüm **kaybetmemek** için.
> **Gerekçe:** A13 ölçtü — sadeleştirme kaybının %74'ü kavram-muğlaklaşmasıdır ve kayıp DÜZYAZIYA çevirirken oluşur, çünkü düzyazı koşulu cümle akışına gömer. Önerme formunda koşul gömülmez, **öncül olarak açığa çıkar**. Kaybın kaynağı yapısal olarak ortadan kalkar.
> **Kapsam:** A1–A15 aileleri. A16–A18 koşuyor, indiğinde eklenecek.

---

## Notasyon

| İşaret | Okunuşu |
|---|---|
| `∧` | ve |
| `∨` | veya |
| `¬` | değil |
| `→` | ise |
| `⇒` | eşittir / sonuç verir |
| `⊨D` | birincil kaynağa inildi |
| `⊨K` | ikincil kaynak, birincil metinden doğrulanmadı |
| `⊨X` | kaynaklar çelişkili — hüküm YOK |
| `⊨S` | adversaryal saldırıdan sağ çıktı (antitez çürütemedi) |
| `⊨¬2` | **antitez koşulmadı** — sınanmamış |
| `[?]` | kestirim, ölçülmemiş |

**Okuma kuralı:** öncülü sağlanmayan bir önermenin sonucu geçerli DEĞİLDİR. Öncül listesi eksiksizdir; "genelde", "çoğunlukla" gibi yumuşatıcı yoktur.

---

## I. ÖĞRENEN MODELİ

**P1** ⊨S ⊨K
Kalıcı bellek altyapısı yok **olursa** ∧ oturum değişmiş **olursa** ⇒ öğrenen-modeli taşınmaz.
`¬bellek_altyapısı ∧ oturum(t+1) ≠ oturum(t) → öğrenen_modeli(t+1) = ∅`
*Ek:* Kalıcılık modelin değil **uygulama katmanının** özelliğidir. Ağırlıklar çıkarım anında donmuştur.

**P2** ⊨K
Kestirim kaba-sıralı **ise** ⇒ metinden yapılabilir.
Kestirim kalibre-nokta **ise** ⇒ metinden yapılamaz.
`granülerlik(3_sınıf) → şans_üstü` ∧ `granülerlik(0-100) → MAE ≈ 21`

**P3** ⊨D (çürütüldü)
"Seviye çıkarımı ancak konuşma-dışı davranışsal sinyalle olur" ⇒ YANLIŞ.
Davranışsal sinyal **gerekli değildir**; yalnız **düzelticidir** (uzmanı eksik / acemiyi fazla tahmin yanlılığını giderir).

**P4** ⊨K (çürütüldü)
"Seviyeye uyarlama ile yaranma ayrıştırılamaz" ⇒ YANLIŞ.
Yaranma temsil uzayında ayrı eksende kodludur ∧ bağımsız yönlendirilebilir.
**AMA:** ayrışma kendiliğinden olmaz. `¬tasarım → uyarlama ≡ yaranma`

**P5** ⊨X
Yaranmanın acemi kullanıcıya zararı ⇒ ÇÖZÜLMEDİ.
Lehte: ML hata-ayıklama görevinde performans düştü ∧ 24 kişiden 17'si yaranmayı fark etmedi.
Aleyhte: sunulan karşı-kanıt **konstrükt kayması** taşıyor (düşük puanlı EĞİTMEN ≠ acemi ÖĞRENCİ).

**P6** ⊨K
Ölçüt öznel **olursa** ∧ hedef "kullanıcının hoşuna gitmek" **olursa** ⇒ naif kişiselleştirme zarar verir (denemelerin %29'u jenerikten kötü).
Ölçüt nesnel **olursa** ∧ profil görev-ilgili **olursa** ⇒ naif kişiselleştirme kazandırır.
**Kritik ek:** zarar LLM-yargıçla ölçülünce **gizlenir**; yalnız insan yargısıyla görünür.

---

## II. ÖĞRENME — pasif okuma

**P7** ⊨S ⊨K
LLM sentezi okunur **ise** ⇒ bilgi daha sığdır.
Öncül sağlamlığı: çekirdek olgular **özdeş sunulsa bile** sonuç değişmiyor (kontrol koşulu deneysel olarak koşulmuş, 7 deney, n=10.462).
*Kalan zayıflık:* tek araştırma ekibi, bağımsız replikasyon yok.

**P8** ⊨K — ÜÇ EKSEN, KARIŞTIRILMAZ

| Karşılaştırma | Acemide kazanan |
|---|---|
| okumak **vs.** kendi başına didinmek | okumak (d = 0,505) |
| okumak **vs.** önce deneyip sonra okumak | **deneme-önce** (kavrama ∧ transfer) |
| okumak **vs.** geri-çağırmak | geri-çağırmak (g ≈ 0,50–0,61, gecikmede) |

`Salih_modeli ∈ eksen_1 → geçerli`
`Salih_modeli ∈ eksen_2 ∪ eksen_3 → açık`

**P9** ⊨K (çürütüldü)
"Pasif okuma, arzu edilir zorlukların hepsinin sıfır dozudur" ⇒ YANLIŞ.
Aralıklama okumaya uygulanabilir: `okuma_dağıtılmış ∧ gecikmeli_ölçüm → okuma_tek > okuma_yığılmış`
Doğru hâli: `okuma_tek_geçiş ∧ yığılmış ∧ tek_oturum → sıfır_doz`

**P10** ⊨K — GUARDRAIL'İN SINIRI
Yardım varken ⇒ performans +%48 (guardrail'siz), +%127 (guardrail'li).
Yardım çekilince ⇒ −%17 (guardrail'siz), **≈ 0** (guardrail'li).
`guardrail → zarar = 0` ∧ `guardrail ¬→ fayda > 0`
**Yani: guardrail zararı nötrler, faydaya çevirmez.**

**P11** ⊨K
Bir meta-analiz geri çekilmiş **ise** ⇒ o rakam kullanılamaz.
`g = 0,867 → GERİ ÇEKİLDİ (22 Nisan 2026)` ⇒ kullanılmaz.
Kalanlar: `g ∈ {0,499 · 0,573 · 0,61 · 0,670}` — **yakınsak**, aykırı değer geri çekilenin kendisiydi.

---

## III. İŞ BAĞLAMI

**P12** ⊨K (çürütüldü)
"70-20-10 geçerli bir tasarım temelidir" ⇒ YANLIŞ.
Kaynak = ~200 yöneticinin geriye dönük öz-beyanı ⇒ hayatta-kalan yanlılığı ∧ beyan yanlılığı.
Savunucu kurumun kendi konumu: "reçete değil referans model."

**P13** ⊨K (çürütüldü)
"İhtiyaç anında öğrenme kalıcılığı ve transferi artırır" ⇒ YANLIŞ.
`JIT → anlık_performans ↑` ∧ `JIT → kalıcılık ∈ [0, negatif]` ∧ `JIT → transfer ≈ 0`

**P14** ⊨K — KOŞULLU GEÇERLİ
Yapılandırılmış yansıtma etkilidir **ancak ve ancak**:
kolaylaştırıcı var **olursa** ∧ nesnel performans verisi var **olursa** ∧ görev karmaşık ∧ içsel geri-bildirim yok **olursa**.
`d ∈ [0,67 · 0,79]` — iki bağımsız meta-analiz yakınsak.
`tek_kişi ∧ ¬kolaylaştırıcı ∧ ¬nesnel_veri → etki DESTEKSİZ`

**P15** ⊨K (çürütüldü) — STAJ KISITI
"Yeterli anonimleştirmeyle işveren verisi riski yönetilebilir" ⇒ YANLIŞ, üç bağımsız yönden:
- teknik: `LLM(serbest_metin) → öznitelik_çıkarımı = %85 top-1` ∧ kaynağın kendi sonucu: yaygın anonimleştirme **etkisiz**
- istatistiksel: `15_demografik_nitelik → yeniden_kimliklendirme = %99,98`
- **kapsam:** `anonimleştirme → kişi_gizli` ∧ `anonimleştirme ¬→ içerik_gizli`. Ticari sır ≠ kişisel veri.
Ayakta kalan yol: `yazılı_izin ∧ kurumsal_tenant → risk yönetilebilir` (prosedürel, teknik değil).

**P16** ⊨K (çürütüldü) — YAPISAL
"AI asistanı çıraklıktaki koçluk/iskele rolünü üstlenebilir" ⇒ YANLIŞ.
`çıraklık ⊃ soldurma` ∧ `soldurma → gözlem(yardımsız_performans)` ∧ `sohbet_asistanı → görüş_alanı = yapıştırılan_metin` ⇒ `soldurma_kararı = imkânsız`
**Bu ayar meselesi değil, yapısal eksikliktir.**

---

## IV. DERS ÜRETİM HATTI

**P17** ⊨S ⊨K
Halüsinasyonlu içerik öğrenilmiş **olursa** ∧ düzeltme uygulanmış **olursa** ⇒ artık etki > 0.
`düzeltme → etki ↓` ∧ `düzeltme ¬→ etki = 0`
**Hüküm türü:** `artık_etki > 0 ∧ maliyet(düzeltme_sonra) > maliyet(kapı_önce) ⇒ kapı_konumu = üretim_anı`
⚠️ **Bu EKONOMİK bir hükümdür, NORMATİF değil.** Literatür "zorunlu" demiyor; artık etkinin azaltılabilir olduğunu söylüyor. *(Bu şerh insan sürümünde ERİDİ — kayıt: A13/F1'in doğuş vakası.)*

**P18** ⊨K — CARVIS DÜZELTMESİ 1
Reddedilen tasarım = **intrinsic** self-correction:
`aynı_model ∧ aynı_bağlam ∧ ¬dışsal_referans ∧ akıl_yürütme_görevi → doğruluk ↓`
Reddedilmeyen üç tasarım:
`LLM_yargıcı ∧ materyal_filtreleme → çalışıyor` (52k→9k filtrelenmiş veri tam-veriyi geçti)
`ayrı_doğrulayıcı_geçişi → +%20`
`doğrulayıcı ∧ kaynak_metin_elde → referanslı_doğrulama ≠ reddedilen_tasarım`
⇒ **Karar defterinden ders üretiminde doğrulayıcının elinde karar kaydı VARDIR.** Öncül sağlanmıyor, hüküm geçmiyor.

**P19** ⊨D — CARVIS DÜZELTMESİ 2
"LLM-as-judge zayıf korelasyonludur (r≈0,31)" ⇒ YANLIŞ.
`tercih_karşılaştırması → insan_uyumu > %80 ≡ insan_insan_uyumu`
`13_çalışma → medyan_korelasyon = 0,69`
`r ≈ 0,31 → künye BULUNAMADI`

Yargıcın doğru kullanımı — **görev tipine göre**:

| Sorulan soru | Performans | Kullan |
|---|---|---|
| tanımlı kusur var mı | %94+ | ✅ |
| hangisi daha iyi | insan seviyesi | ✅ |
| kaynağa göre doğru mu | iyi | ✅ |
| genel olarak ne kadar kaliteli | r = 0,13–0,48 | ❌ |
| kendi çıktını referanssız düzelt | doğruluk ↓ | ❌ ASLA |

**P20** ⊨D
13 ADR şablonu incelendi **ise** ⇒ hiçbirinde "gözlenmiş sonuç" alanı YOK.
`∀ şablon: alan(gözlenmiş_sonuç) = ∅` ⇒ karar-anı yakalama şeması, öğrenme şeması değil.
**Bu, kurulacak hattın literatürde karşılığı olmayan parçasıdır.**

---

## V. TASARIM — pasif öğrenme sistemi

**P21** — ÖNERİLEN MODEL (Model B)
`deneme_kapısı ∧ düzeltme_formatı ∧ referanslı_kalite_kapısı ∧ dosya_kaydı ⇒ K1..K6 hepsi sağlanır`

Kısıt matrisi:

| | K1 dosya | K2 sığlık | K3 deneme-önce | K4 kapı | K5 soldurma | K6 izin |
|---|---|---|---|---|---|---|
| Model A (hasat) | ✅ | ❌ | ❌ | ⚠️ | ❌ | ✅ |
| **Model B (önce dene)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Model C (tam hat) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

`Model_C → K-010_kapıları` ⇒ şimdi değil.
`Model_B → Salih_formülasyonu(2-3 cümle)` ⇒ **P16'nın yapısal eksikliği kapanır** (yardımsız performans kaydı oluşur).

---

## VI. AJAN ASILMASI — ölçüm

**P22** ⊨D (ölçüldü, N=24)
`korelasyon(süre, en_uzun_duraklama) = 0,95`
⇒ süre ≈ f(tek duraklama), süre ≠ f(iş hacmi).

**P23** ⊨D — VERİM TERSİNE DÖNÜYOR
`hızlı_ajan → 25–43 olay/dk` ∧ `yavaş_ajan → 4–11 olay/dk`
`en_yavaş(1173 s) → 81 olay` ∧ `hızlı(105 s) → 72 olay`
⇒ yavaş ajan daha çok iş yapmıyor, **duruyor**.

**P24** ⊨D — H0 ÇÜRÜTÜLDÜ
Hipotez: ağ asılması. Ölçüm: `max(WebSearch) = 11,0 s` ∧ `max(WebFetch) = 10,4 s` ⇒ zaman aşımları çalışıyor ⇒ **hipotez yanlış**.
Gerçek: `18 duraklama(>60 s) → 2 patoloji ∧ 16 uzun_üretim`
`patoloji = ajanın kendi yazdığı Bash bekleme/yoklama döngüsü`

**P25** ⊨D — EŞİK
| eşik | işaretlenen | gerçek | kesinlik |
|---|---|---|---|
| 60 s | 18 | 2 | %11 |
| 120 s | 11 | 2 | %18 |
| 300 s | 2 | 2 | %100 |

`sezgisel_eşik(120 s) → 5/6 müdahale sağlıklı ajanı öldürür`
⚠️ `pozitif_örneklem = 2` ⇒ **kural DEĞİL, gözlem.**

**P26** ⊨D — KÖR NOKTA
`stall_watchdog_eşiği = 600.000 ms` ∧ `Bash_tavanı = 600.000 ms` ⇒ Bash tavanına ayarlı bekleme **watchdog penceresine tam sığar ve tetiklemez**.
`watchdog_kapsamı = async_alt_ajan` ∧ `senkron_alt_ajan → watchdog = ∅`
`kota_dolu → retry_watchdog → süresiz bekleme` (429/529 sınırsız yeniden denenir)
`en_kötü_hâl = API_TIMEOUT × (MAX_RETRIES+1) ≈ 110 dk` (tek çağrı, sıfır çıktı)

---

## VII. İSTATİSTİK — eşik seçiminin çerçevesi

**P27** ⊨D
`koşan_iş ⇒ sağdan_sansürlü_gözlem`
`yalnız_bitenlerin_ortalaması → yanlı(düşük)` ∧ `sansürlüyü_bitmiş_saymak → yanlı(düşük)`
İki farklı hata, **aynı yöne**.
`gözlem_penceresi = 3 saat → "3 saati geçen görmedik" = bilgi_yok`

**P28** ⊨D — SEZGİNİN TERSİNE DÖNDÜĞÜ YER
Ortalama kalan süre `E[T−t | T>t]`:

| dağılım | t=1 | t=10 | t=50 |
|---|---|---|---|
| Üstel | 1,00 | 1,00 | 1,00 |
| Weibull k=0,5 (azalan hazard) | 4,00 | 8,33 | 16,14 |
| Weibull k=2 (artan hazard) | 0,38 | 0,05 | — |
| Pareto α=1,5 | 2,00 | 20,00 | 100,00 |

`Pareto → MRL = t/(α−1)` ⇒ **yaşla doğrusal ARTAR.**
⇒ `ağır_kuyruk → "bu kadar bekledik, bitmesine az kaldı" YANLIŞ`

**P29** ⊨D ∧ ⊨K
`üstel → restart nötr` ∧ `artan_hazard → restart zararlı` ∧ `azalan_hazard ∨ ağır_kuyruk → restart faydalı`
Ölçüt: `CV > 1 → restart faydalı` (yeterli koşul, gerek değil)
⚠️ `deterministik_hata → restart ¬→ yeni_çekiliş` ⇒ Luby garantisi çöker. **Proxy 403'ü deterministiktir; restart onu çözmez.**

**P30** ⊨D — GERİ-BESLEME TUZAĞI
`işi_öldürürsen → sansür informative olur → KM_tahmini yanlı`
⇒ **timeout politikası kendi verisini kirletir.** Eşik veriyi üretir, veri eşiği belirler.
`şu_an: hiçbir ajan öldürülmedi → tuzağa henüz düşülmedi`
`watchdog_kurulur → tuzağa düşülür` ⇒ kurulumda ölçüm tasarımı beraber düşünülmeli.

**P31** ⊨D — KÜÇÜK-N
`n = 30 → p95 için dağılımdan-bağımsız %95 GA KURULAMAZ`
`örneklem_maksimumu → beklenen_kuantil = n/(n+1) = 0,9677`
`n=30 → P(max > gerçek_p95) = %78,5` ∧ `P(max > gerçek_p99) = %26,0`

Tahmincinin saçılımı (lognormal, gerçek p95 = 5,18):
| n | ampirik p95'in %95 aralığı |
|---|---|
| 30 | [2,46 · 9,22] |
| 100 | [3,39 · 7,51] |
| 300 | [4,01 · 6,52] |

⇒ `N=24 → P25'in 300 s eşiği kanona YAZILAMAZ`

**P32** ⊨K
`nadir_pozitif_sınıf → PR_eğrisi ✅ ∧ ROC ❌`
`N ≫ P → FPR kıpırdamaz ∧ precision boğulur` ⇒ ROC iyimser yanılsama üretir.
`Amazon_p99.9_kuralı ≡ Neyman-Pearson(α = 0,001)` — sektör pratiği ile kuram aynı şey.

---

## VIII. AJAN UZMANLAŞMASI

**P33** ⊨D
`Claude_ekosistemi → fine-tuning ≈ kapalı`
⇒ "ajanı eğitmek" = `rol_tanımı + beceri_dosyası + araç_kısıtı + hafıza_dizini`

**P34** ⊨D — TALİMAT ≠ ZORLAMA
`CLAUDE.md → sistem_promptu_sonrası_kullanıcı_mesajı` ∧ `¬kesin_uyum_garantisi`
`çelişkili_iki_kural → model keyfî seçebilir`
`dosya_uzunluğu ↑ → uyum ↓`
⇒ `mutlaka_çalışmalı(X) → X ∈ {hook, permissions.deny}`
*(JARVIS bunu zaten uygulamış: core/ settings-deny + PreToolUse teli. A7 tercihi bağımsız doğruluyor.)*

**P35** ⊨D ∧ ⊨X — PERSONA
`persona_ata → nesnel_doğruluk ↑` ⇒ **YANLIŞ** (162 rol, 4 model ailesi, 2.410 soru)
`düşük_bilgi_persona → doğruluk ↓`
Satıcının kendi iddiası dar: "davranış ve **ton**" — doğruluk iddiası YOK.
⊨X: karşı yönde rol-oyun promptlaması kazanç bildiriyor (+10,3 · +60,4 puan) — **aynı manipülasyon ölçülmüyor olabilir** (kimlik-atama ≠ sahne kurulumu). Ayrıştıran deney bulunamadı.

**P36** ⊨X — ÇOKLU-AJAN KAZANCI
`çoklu_ajan → +%90,2 (tek ajana karşı)` ∧ `token_kullanımı → varyansın %80'ini açıklıyor` ∧ `maliyet = 15×`
⇒ **token-eşitlenmiş karşılaştırma BULUNAMADI** ⇒ kazancın kaynağı belirsiz.

**P37** ⊨D — İZOLASYONUN İKİ YÜZÜ
`alt_ajan → ana_pencerede tasarruf = 5.680 token`
`alt_ajan → mükerrer başlangıç yükü = 3.790 token`
⇒ `denge ≈ 1,5:1` ⇒ **izolasyon ANA PENCEREYİ korur, TOPLAM token'ı korumaz.**
`kısa_görev → başabaş noktasının altında`

**P38** ⊨K
`ajan → kendi_işini_notlandır → iyimser sapma`
⇒ `¬dışsal_sinyal → "%30 tamamlanmışken tam güvenle teslim eden ajan"`
*(P17 ile birleşir: öğrenme ajanı kendi dersini onaylayamaz — iki bağımsız gerekçe.)*

**P39** ⊨K — KALICI HAFIZA RİSKİ
`hafıza_dosyası > 200 satır ∨ > 25KB → sessizce KIRPILIR`
`zehirleme_oranı < %0,1 → saldırı_başarısı > %80` ∧ `iyi_niyetli_performans_düşüşü < %1` ⇒ **fark edilmez**

---

## IX. KATEGORİ / ETİKET ŞEMASI

**P40** — SORUN SAYI DEĞİL
`|bulgu| > |kategori| → aynı_kategori_çakışması ZORUNLU`
⇒ `kategori_sayısı ↑ → çakışma ertelenir, kaldırılmaz`
`kategori_sayısı ↑ → kappa ↓` ∧ `menzil_kısıtlaması → etkin_kategori < nominal_kategori`
Otorite kanıtı: yerleşik bir sistem 2011'de alt-kademeleri **birleştirip granülerliği AZALTTI**.

**P41** ⊨D — ASIL ARIZA
`D/K/X → tek_eksen(kaynak_türü)` ∧ `teyit_durumu → kodlanmıyor`
Çözüm: `eksen_S(kaynak) × eksen_C(teyit) × durum(yargılanamaz)`
`optimum(eksen_başına) ≈ 4`

**P42** ⊨D — EN YÜKSEK GETİRİLİ TEK DÜZELTME
`X ≡ {çelişkili} ∪ {doğrulanamadı}` ⇒ **iki farklı epistemik durum tek kovada.**
Her yerleşik sistem ayırıyor:
`Admiralty: 5(çelişkili) ≠ 6(yargılanamaz)`
`FEVER: REFUTED ≠ NOTENOUGHINFO`
`STIX: değer(6) → sayıya çevrilemez → ValueError` ⇒ **"bilinmiyor" düşük güven DEĞİL, ekseni terk eden ayrı durum.**

**P43** ⊨K — İKİ EKSEN KENDİLİĞİNDEN ÇALIŞMAZ
`iki_eksen ∧ aynı_zihinsel_hareket → köşegene çöker`
Ölçüm: `1400+ rapor → %87 köşegen` ⇒ `36 hücre ⇒ ~6 hücrelik bilgi`
Çözüm: `¬derece_sor` ∧ `olgusal_sinyal_sorusu_sor` ∧ `derece = kural(cevaplar)`

**P44** ⊨K — HAKEMLİK ETİKETTE DEĞİL
`kazanan ≠ en_çok_desteklenen` ∧ `kazanan = en_az_çürütülen`
*(Bu, m.40b'nin adversaryal-hayatta-kalma ölçütüyle AYNI ilke — tüzük bağımsız gelenekle doğrulandı.)*
`kalite_eşit → ayırıcı_ölçüt = yanlılık_kaynaklarının_bağımsızlığı`
`oy_sayımı(anlamlılık_temelli) → geçersiz` ∧ `çalışma_sayısı ↑ → güç → 0`
`anlaşmazlık → veri` (etikete gömülüp yok edilmez)

**P45** ⊨K
`sözel_kabalaştırma → kestirim_doğruluğu ↓` (888.328 tahmin)
`granülerlik → f(beceri)` ⇒ `¬kalibre → ince_granülerlik = gürültü`
⇒ `etiket = 4_kademe(arayüz)` ∧ `alt_katman = 0-100(makine)` ∧ `karar_ağırlığı(sayı) = 0` **Brier ile kalibre edilene dek**

---

## X. PERSONA VE KONSEY

**P46** ⊨D — %85 RAKAMININ ÜÇ KATMANI
1. `payda = kişinin_kendi_2_hafta_sonraki_tutarlılığı` ⇒ ham isabet ≈ %72
2. `%85_üreten_prompt = üçüncü_şahıs_TAHMİN` ∧ `≠ birinci_şahıs_ROL_YAPMA`
   Birebir: *"Based on the interview transcript, **predict** the participant's survey responses."*
   ⇒ **Salih'in konsey kurgusu ölçülmüş kurulum DEĞİLDİR.**
3. `bireysel_korelasyon = 0,20` ⇒ model ortalamayı bilir, bireyi ayırt etmez.

**P47** ⊨K
`zengin_profil(500+ soru) ≈ yalnız_demografi` ⇒ zenginleştirme bireysel doğruluğu artırmıyor.
`persona_takip_gücü ↑ → karikatürleşme ↑` ⇒ sadakat ve klişeleşme aynı eksende.
`yönlendirilebilirlik ≠ hizalanma`

**P48** ⊨K — TARİHSEL FİGÜR
`tarihsel_persona → çıktı = kamusal_algı` ∧ `çıktı ≠ kişinin_görüşleri`
Kanıt: `uzman_ayırt_etme = %51` (şans %20, beklenti %80) ∧ `10 sorunun 2'sinde uzmanlar YAPAY cevabı gerçeğine TERCİH ETTİ`
⇒ ölçülen = prototipiklik, ≠ gerçeklik.
`adanmış_doğruluk_benchmark'ı = ∅`

**P49** ⊨D — MİMARİ HÜKMÜ
`Salih_kurgusu(1 tez + 1 antitez + 1 hakem) ≡ Multi-Persona`
`Multi-Persona → 9 benchmark'ın 8'inde konseye kaybediyor` ∧ `çoğunda tek-ajan CoT'un altında` (MATH: 51,87 ↔ 75,40 ↔ 72,87)
Teşhis: `zorunlu_karşıtlık ∧ hakem_kararı_geri_dönüşsüz`

⚠️ **JARVIS'e TRANSFER EDİLMEZ**, üç öncül farklı:
`atlas_görevi = literatür_keşfi ∧ ≠ benchmark_çözme` ⇒ self-consistency alternatifi YOK
`m.40b_antitezi = CoVe-Factored` ⇒ tezin gerekçesini görmez ≠ MP'nin devil'i
`m.40b_hakemi ¬→ tartışmayı keser`
**Geçen iki uyarı:** zorunlu karşıtlık zararlı ∧ aynı modele farklı persona = sahte çeşitlilik.

**P50** ⊨D
`farklı_MODEL > aynı_modelin_farklı_persona'sı` (+%6,4 … +%8,2)
`persona_detayı ↑ → çeşitlilik ↓` (manifold collapse)
⇒ **V59'un gerekçesi değişir: maliyet tedbiri ⇒ KALİTE tedbiri.**

**P51** ⊨K
`sabit_bütçe → optimum = 2 ajan × 2-3 tur`
`genişlik 2→3→5 → doğruluk 86,77 → 85,22 → 86,15` (düşüyor)
`tur ↑ → anlaşmazlık ↓ → performans ↓`
`modal_cevabı_sorgusuz_benimseme = %85,5` ∧ `doğru→yanlış geçişleri = %57–77`
`oracle_gap = 32,3 puan` (doğru cevap havuzdaydı, oylama attı)

---

## XI. HUKUK

**P52** ⊨K — EŞİK
`çıktı ¬→ üçüncü_kişi` ⇒ iftira kapısı KAPALI
`kullanım = özel ∧ ticari_değil` ⇒ publicity kapısı KAPALI
`faaliyet = hane_içi` ⇒ GDPR md. 2(2)(c) ∧ AI Act md. 2(10) KAPALI

Kalkanı düşüren üç tetikleyici — **ikisi para gerektirmiyor**:
`belirsiz_sayıda_kişiye_erişim → GDPR istisnası düşer`
`düzenli_ekonomik_fayda → AI Act istisnası düşer ∧ publicity açılır`
`kamusal_tartışmayı_etkileme → md. 50(4) ∧ md. 2(10) kaybı`

Eşikten **bağımsız** iki risk:
`yanlış_atıf(CDPA md.84) ¬→ ticari_kullanım_şartı`
`epistemik_bozulma → özel_kullanımda TAM GÜÇLE mevcut`

**P53** ⊨K
`Einstein: publicity_hakkı → sona_erdi(2005)` ∧ `eserler → kamu_malı(2026, ömür+70 ülkeleri)` ∧ `GDPR ¬→ ölüler`
`yaşayan_kişi: ELVIS_Act ∧ CA_AB1836 ∧ CDPA_md84` ⇒ farklı sınıf.
⚠️ `hukuken_serbest ¬→ etik_güvenli` — emsal: bir uygulamada Himmler personası Holokost'taki rolünü **inkâr etti**, ve uygulama **Eğitim** kategorisindeydi.

**P54** ⊨K — ÇEKİRDEK EPİSTEMİK RİSK
`persona ¬→ doğruluk ↑` ∧ `kişiselleştirme → ikna_gücü ↑ (+%81,2 olasılık)`
⇒ **`persona → daha_çok_ikna ∧ ¬daha_doğru`** — bir öğrenme sisteminde en kötü bileşim.

**P55** ⊨K — ARAŞTIRMA AJANI
`ajan ¬→ kimlik_doğrula` ⇒ tek kural, iki davanın farkını üretir.
`URL_geçerli ¬→ atıf_geçerli`: `link_geçerliliği > %94` ∧ `olgusal_doğruluk ∈ [%39 · %77]`
`deep_research_ajanı → uydurma_URL > basit_arama_ajanı`
`yapışkan_lisans ← uyarlama` ∧ `yapışkan_lisans ¬← alıntı` (istisna kapsamında lisans **uygulanmaz**)
`güvenli_alıntı_uzunluğu = ∅` (hiçbir yargı çevresinde yok)
`yayım = ayrı_açık_geçiş ∧ ≠ varsayılan`

---

## XII. SENKRON VE COMPILER

**P56** ⊨D
`kısa_vade_hedef(telefon↔PC senkron) → ZATEN KARŞILANMIŞ`
Sınırlar:
`terminal_kapanır → oturum biter` ∧ `ağ_kopması > 10 dk → oturum biter`
`devir = tek_yönlü`: `bulut → terminal ✅` ∧ `terminal → web ✗ (CLI'dan)`
`teleport → telefon_bağlantısı KOPAR`
`/voice → yerel_mikrofon_şartı` ⇒ `mobil → sesle_inşa = ∅`
`bulut_oturumu → yalnız commit'lenmiş yapılandırma`

**P57** ⊨D — K-009 İÇİN KAPI MODELİ
`Routines → koşum_içi_izin_istemi = ∅` ∧ `insan_kapısı = koşum_sonrası(PR)` ∧ `yazma_yüzeyi = claude/*_dalları`
⇒ **özerklik içeride, denetim sonrada, yazma dal-kısıtlı.**

**P58** ⊨D — COMPILER KAYIP MODELİ
`sadeleştirme → kayıp` ∧ `kayıp = %74,1 muğlaklaşma + %25,9 silme`
`laik_yeniden_yazım → epistemik_güç_değişimi = %38,7`
`ortalama_kayma = +0,085` ⇒ **ortalamaya bakan denetim göremez.**
`negatif_kutup_CV = 0,97` ∧ `pozitif_kutup_CV = 0,14` ⇒ **~7× oynaklık**
⇒ `en_çok_korunması_gereken_etiket = çeviride_en_çok_bozulan_etiket`

**P59** ⊨K — TERS TEPEN TALİMAT
`prompt("sadık kal") → aşırı_genelleme ↑ (~2×)`
⇒ `sadakat ← yapısal_kısıt` ∧ `sadakat ¬← talimat`

**P60** ⊨D
`soyutlama_agresifliği ↑ → sadakat ↓` (doz-yanıt: %16,6 → %52,9)
⇒ `yeniden_yazım = cümle_seviyesi` ∧ `¬paragraf_birleştirme`

**P61** ⊨K
`olgun_iki_sürüm_rejimi ∧ zorunlu ∧ denetlenen → kanıt_kesinliği_uyumu = %0,7`
⇒ güven bilgisi laik sürüme **pratikte hiç geçmiyor**.

**P62** ⊨K
`okur_uzman → sadeleştirme = ZARAR` (`d = 0,971` düşük↔yüksek ön-bilgi farkı)
⇒ `konu ∈ DONE ∧ derinlik = [T] → compiler KAPALI`

---

## XIII. GRAF TASARIMI

**P63** ⊨D
`düğüm=ajan ∧ kenar=kanal` ⇒ literatürün standart formalizasyonu.
`arama_uzayı ⊆ DAG` ⇒ döngü özellik değil, **dışlanan**.

**P64** ⊨D — YOĞUNLUK YANLIŞ DEĞİŞKEN
`kenar_sayısı sabit(32,76 ↔ 32,80) → sonuç 0,575 ↔ 0,510`
⇒ `belirleyici = hangi_kenarlar` ∧ `≠ kaç_kenar`
`kenar_sayısı = O(n²)`: 2→4 (9 dk) · 6→36 (23 dk) · 10→100 (58 dk) · 14→196 (95 dk)

**P65** ⊨D — TERS-U
`en_yoğun ∧ düşman_var → 0,5751` (çöküyor)
`en_seyrek(zincir) ∧ tek_bozuk_ajan → −%23,7`
`hiyerarşik ∧ tek_bozuk_ajan → −%5,5`
⇒ `kenar_eklemenin_faydası = hata_düzeltme` ∧ `bedeli = bulaşma + token`

**P66** ⊨D — BULAŞMA
`tek_zehirli_ajan → ~%100 bulaşma, 27-31 tur` (1M ajanlı ağ)
`ölçek ↑ ¬→ koruma`: `N=2¹⁴ → %95,03` ∧ `N=2²⁰ → %96,23`
`saldırgan_maliyeti = O(1/N) tohum ∧ O(log N) tur`
`kendini_kopyalamayan_injection → 32 turda yalnız 1/8` (doğrusal)

**P67** ⊨D — ÇARE ROL, KENAR DEĞİL
`tek_bozuk_ajan → çoklu_ajan_primi silinir` (prim +4,76 / +5,29)
`Challenger + Inspector → kaybın %96,4'üne kadarı geri kazanılır`
⇒ kırılganlık **rol ekleyerek** onarılır, kenar ekleyerek değil.

**P68** ⊨K — 80 YILLIK YAKINSAMA
`görev_basit → merkezî ✅` ∧ `görev_karmaşık → merkezsiz ✅`
1940'ların insan deneyleri ∧ modern LLM ölçümleri ⇒ aynı sonuç.
⇒ `evrensel_kazanan_topoloji = ∅` ∧ `görev_topoloji_eşleşmesi mevcut`

**P69** ⊨D — METODOLOJİK UYARI (kendi evallerimize de uygulanır)
`prompt("hata oranı = %20") → gerçekleşen = %1,56 (SD 3,65)`
`prompt("hata oranı = %40") → gerçekleşen = %9,49 (SD 26,70, maks 90,10)`
⇒ **prompt ile hata oranı ayarlayan her çalışma, iddia ettiği şeyi ölçmüyor olabilir.**

---

## XIV. KOŞUMUN KENDİ ÖNERMELERİ

**P70** — KANIT KISITI
`akademik_host_erişimi = 0/10` ⇒ `A1,A2,A3,A11 → D_etiketi = ∅` ⇒ **tavan K**
`teknik_host_erişimi > 0` ⇒ `A4,A5,A7,A12,A13,A14 → D mevcut`
⇒ `rapor ∈ karar_öncesi_tarama` ∧ `rapor ∉ kanıt`

**P71** — PROTOKOL BORCU
`A5..A15 → aşama_2 = ∅` ⇒ 11 aile adversaryal sınamadan geçmedi.
`[D]_bulguları → olgusal_risk düşük` ∧ `yorum_katmanı → sınanmamış`

**P72** — V26 İKAMESİ
`birincil_kaynağa_iniş = imkânsız` ⇒ `V26 koşulamadı`
İkame = çapraz-sorgu denetimi ⇒ **V26 yerine geçtiği İDDİA EDİLMİYOR**
`yakalanan_çelişki = 10` ∧ `denetimsiz_yüzey = büyük` ⇒ **etiket enflasyonu riski YÜKSEK**

**P73** — CARVIS'İN KENDİ HATASI
`alt_ajanlar_limite_çarptı → "bekle" kararı` ∧ `¬saat_kontrolü`
`gerçek: limit 12 dk önce sıfırlanmıştı`
⇒ `kaynak_tükendi ≡ iş_bitti` varsayımı — **araştırılan hatanın insan tarafındaki hâli.**
Düzeltme: `ölç ∧ ¬tahmin_et`

---

## Kullanım notu

Bir önermeyi kullanmadan önce:
1. **Öncülleri kontrol et.** Öncül sağlanmıyorsa sonuç geçmiyor. P49 bunun en net örneği — mimari hükmü var ama JARVIS'te üç öncül birden farklı.
2. **Etikete bak.** `⊨K` olan hiçbir önerme tüzük anlamında hüküm taşımaz (P70).
3. **`⊨¬2` olanı sınanmış sayma.** A5–A15 arası 11 aile bu durumda (P71).
4. **`⊨X` olanı kullanma.** Çelişki çözülmedi demektir, ortalama alınmaz.
