# Önerme Formu — anlaşılırlık kaygısı olmadan

> **Bu üçüncü register'dır.** Teknik sürüm kanıt için, insan sürümü anlamak için, bu sürüm **kaybetmemek** için.
> **Gerekçe:** A13 ölçtü — sadeleştirme kaybının %74'ü kavram-muğlaklaşmasıdır ve kayıp DÜZYAZIYA çevirirken oluşur, çünkü düzyazı koşulu cümle akışına gömer. Önerme formunda koşul gömülmez, **öncül olarak açığa çıkar**. Kaybın kaynağı yapısal olarak ortadan kalkar.
> **Kapsam:** A1–A27 aileleri (A23 hariç — koşuyor). **Bölüm XV'ten itibaren Salih'in 07-26 register hükmüyle eklendi:** ai-to-ai raporlar bundan böyle tam önerme formunda yazılır, gerekçe *"jarvisle beraber okuyacağım"*. Bu, compiler formülü F8'in genişletilmiş hâlidir: uzman-alan **∨** makine-eşlikli okuma ⇒ compiler KAPALI.

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

## Düzeltme kaydı — 2026-07-26 antitez turu

`raporlar/2026-07-26-antitez-hakemlik.md` §8'deki K listesi bu dosyaya uygulandı. Düzeltilen önermeler ve gerekçeleri, **eski hâli silinmeden**, önermenin altında `[K…]` etiketli satırla taşınır (m.8 otomatik-silme yasağı).

| Düzeltme | Önerme | Ne değişti |
|---|---|---|
| K9 + H1 | P109 | Sonuç satırı kendi öncülüyle çelişiyordu; `transfer ≈ 0` → `düşük ∧ ≠ 0` |
| K15 | P114 | `Stopped yalnız 3 yol` → makine kapanması istisnası + oturum/task ayrımı |
| K16 | P115 | `claude agents HİÇ göstermez` → belirli koşulda gösterir (fallback) |
| K11 + K17 | P117 | `is_error = FALSE` → **⊨X, çözülmedi**; `result ∉ şema` → dile bağlı |
| K18 | P121 | `tek keskin ayırt edici` → coupling ⊨D, "tek" süperlatifi düşer |
| K12 | P126 | `önbellek isabeti = 0` → yalnız ilk çağrıda; sonra kendi cache'ini ısıtır |
| K13 | P127 | `bağlayıcı sınır = 10` → üç ayrı mekanizma ayrıştırıldı |
| K14 | P134 | **Explore/Plan sürdürülemezliği ASKIDA** — `[?]`, dayanağı bulunamadı |
| H4 | P96 · P98 | `indirme → bakım öngörür` → toplu düzeyde, paket-başına garanti değil |

⚠️ **K14 en ağır olanıdır:** teslim edilmiş bir raporda **listenin başına konmuş bir tavsiyenin** dayanağı bulunamadı. Doğrulanana kadar kural olarak kullanılmaz.

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

## XV. KOD ENTEGRASYONU (A16–A18)

**P74** ⊨D — ÖNCÜL ÖLÇÜMÜ
`izlenen_dosya = 172` ∧ `md = 148..149` ⇒ `md_payı = %86,6` ∧ `md_satırı ≈ 11.750`
"Sadece md" **tam doğru değil**: `yürütülebilir = 4` ∧ konumları rastgele **değil**.
`yürütülebilir_dosya ∈ {core-yazım-kilidi_hook, push_doğrulayıcı}` ⇒ sistem "kural metinle yazıldı ∧ tutmadı ∧ koda taşındı" yolunu **zaten bir kez yürümüş**.

**P75** ⊨D — BİÇİMSEL TABAN
`CommonMark: her_karakter_dizisi = geçerli_belge` ⇒ `markdown → hata_kavramı = ∅`
⇒ Markdown'da "bozuk dosya" **tanımsızdır**; doğrulama ancak dışarıdan dayatılan bir şemayla var olur.

**P76** ⊨D ⊨X — ⭐ METNİN GÜCÜ VE TEK KOŞULU
`saf_metin(19_madde) ∧ dış_denetimli_icra` ⇒ `ölüm: %1,5 → %0,8` (p=0,003) ∧ `komplikasyon: %11,0 → %7,0` (p<0,001)
`saf_metin(aynı) ∧ yönetmelikle_zorunlu ∧ öz-beyanla_uyum` ⇒ `ölüm: %0,71 → %0,65` (p=0,13) — **101 hastanenin hiçbirinde anlamlı iyileşme yok**
`fark ≠ metin` ∧ `fark = metnin_etrafındaki_icra_makinesi`
⇒ **`metin ∧ ¬dış_denetim → etki = 0`.** Kâğıt üzerinde zorunlu kılınmak etkiyi **sıfırlar**.

**P77** ⊨D
`skill_etkisini_yitirdi` ⇒ `içerik_mevcut ∧ model_başka_yolu_seçiyor`
Üreticinin kendi reçetesi: `açıklamayı_güçlendir ∨ hook_ile_deterministik_zorla`
`AGENTS.md_kanonik_örneği → içeriğini_doğrulayıcılara_devrediyor` ⇒ markdown **doğrulayıcı değil, doğrulayıcıya İŞARETÇİ**.

**P78** ⊨D — ⭐ İSTEMCİ HOOK'U SİGORTA DEĞİLDİR
`git commit -n ∨ git push --no-verify` ⇒ `hook = atlanır`
`git clone` ⇒ `istemci_hook ∉ kopya`
`pre-receive ∧ exit ≠ 0` ⇒ `hiçbir ref güncellenmez`
⇒ `zorlayıcılık ⇔ push_edenin_kontrolünde_DEĞİL`
⇒ Mevcut `core/`-teli ∧ push-doğrulayıcı: `danışmanlık_gücü = var` ∧ `zorlama_gücü = yok`.

**P79** ⊨D — TEK KİŞİLİK REPODA KORUMANIN VARSAYILANI
`branch_protection ∧ admin_yetkisi ∧ ¬"Do not allow bypassing"` ⇒ `koruma(kendine) = ∅`
`ruleset ∧ mod = evaluate` ⇒ `bloklamadan_izleme` ⇒ **önce ölç, sonra zorla** mümkün.

**P80** ⊨D — KAÇINILACAK YOL
`OPA/Conftest → markdown_parser = ∅` ∧ `girdi_modeli ≠ uyumlu` ⇒ `yeni_dil + çevirici_bakımı`
⇒ policy-as-code yığını bu işe **YARAMAZ**.

**P81** — ÖNERİLEN KATMAN AYRIMI
`alan ∈ {id, type, status, date, supersedes, pointers, owner}` ⇒ **şemaya** (sonlu ∧ enum'lanabilir)
`alan ∈ {madde_metni, gerekçe, tartışma}` ⇒ **metinde kalır**
`alan ∈ {pano_tablosu, indeks, geçersizlik_grafı}` ⇒ **türetilir** ∧ `¬elle_yazılır`

**P82** ⊨D — ⭐ TDD'NİN ÜNLÜ RAKAMI ÖLÇÜM DEĞİL
`"%15–35 geliştirme_süresi_artışı"` → kaynak etiketi = **`[Management estimates]`** ⇒ öznel hatırlama
`aynı_makalenin_nesnel_adam-ay_tablosu` ⇒ `normalize_hız ∈ [0,68× , 3,65×]` — **"%15–35" ile bağdaşmıyor**
`N = 4` ∧ `anlamlılık_testi = ∅` ∧ makalenin kendi itirafı: *"iki proje arasında asla doğru bir eşit karşılaştırma olamaz"*
⇒ Bu rakamı alıntılayan **bir ölçümü değil, bir yöneticinin görüşünü** alıntılıyor.

**P83** ⊨K — ⭐ AJAN ÇAĞININ YENİ BAŞARISIZLIK MODU
`başarılı_yamalar → %32,67 çözüm_sızıntısı` ∧ `%31,08 zayıf_test`
`filtreleme_sonrası → çözüm_oranı = %0,55`
`aynı_aktör(test) ∧ aynı_aktör(kod)` ⇒ `test: spesifikasyon → optimizasyon_hedefi`
⇒ **`kabul_testi ⊥ optimize_eden_taraf`** (başkası yazar ∨ held-out saklanır).

**P84** — SENTEZ
> **`kod ≠ metnin_yerine` ∧ `kod = metnin_DOĞRULANAMAYAN_kısmını_devralır`**

| Katman | Zorlayıcılık |
|---|---|
| Metin | **yok** — tavsiye |
| Kod (yerel): `core/` teli, lychee, Vale, cog --check | **hatırlatıcı** — `--no-verify` ile atlanır |
| Kod (dışsal): GitHub ruleset, Actions | **atlanamaz** |

`öncelik_sırası = [lychee, obsidiantools, ruleset(evaluate), front_matter_şeması, cog --check, Vale]`

---

## XVI. ARAÇ VE MODEL ÇEŞİTLİLİĞİ (A19–A21)

**P85** — CARVIS'İN AJANININ HATASI (V26 sınıfı yakalama)
`dizin_adı = /root/.ccr/` → ajan çıkarımı: `router_kurulu ∧ maliyet ≈ 0`
`gerçek: /root/.ccr = agent_proxy` ∧ `içerik = yalnız_CA_sertifikaları` ∧ `ccr_komutu = ∅`
⇒ `dizin_adından_çıkarım → yanlış`. Öneri geçerliliğini korur, **maliyet iddiası düşer**.

**P86** ⊨K — DENETÇİ SEÇİMİ
`çapraz_aile > aynı_aile > öz_doğrulama`
`benzerlik(çözücü, doğrulayıcı) ↑` ⇒ `fayda ↓`
⇒ `başka_model` **yetmez**; `başka_AİLE` gerekir.
*Mekanizma:* `öz_tercih_sapması → aile_düzeyine_yayılır` ∧ `sapma ∈ [−%38, +%90]` ∧ kaynak = kendi çıktısının düşük perplexity'si ⇒ **mimari tercih, düzeltilebilir prompt hatası DEĞİL**.
⇒ `Opus_denetleyen_Sonnet → sapmayı_kısmen_taşır`.

**P87** ⊨K — BAĞIMSIZLIK SATIN ALINAMAZ
`iki_model_birlikte_hata_yaptı` ⇒ `%60 → aynı_yanlış_cevap`
`model_büyük ∧ isabetli ∧ mimari≠ ∧ sağlayıcı≠` ⇒ hata korelasyonu **yine yüksek**
⇒ Bu, A10'un **"9 hakem ≈ 2 bağımsız oy"** ölçümüyle bağımsız olarak **yakınsıyor**.
⇒ `çapraz_sağlayıcı_denetçi = ikinci_süzgeç` ∧ `≠ kalkan`

**P88** ⊨K
`2_heterojen_ajan > 16_homojen_ajan` ⇒ **jüriyi büyütme, çeşitlendir** (8× ajan azalması).

**P89** ⊨D — MALİYET GEREKÇESİ ZAYIF
`$/MTok (2026-07-26): Opus 5 = 5/25 · Sonnet 5 = 2/10 · Haiku 4.5 = 1/5`
`önbellek_okuma = 0,1 × taban_girdi` ∧ `batch = %50`
⇒ `Opus→Haiku = 5×` ∧ `Opus→Sonnet = 2,5×` — **sağlayıcı değiştirmeden**
⇒ **`çapraz_sağlayıcının_gerekçesi ≠ tasarruf` ∧ `= hata_bağımsızlığı`**

**P90** ⊨D — ÇAPRAZ-SAĞLAYICININ GİZLİ MALİYETİ
Üreticinin kendi beyanı: OpenAI-uyumlu katman *"üretime hazır bir çözüm olarak değerlendirilmiyor"*
`strict → yok_sayılır` ∧ `response_format → yok_sayılır` ∧ **`prompt_caching → desteklenmiyor`** ∧ `desteklenmeyen_alanlar → SESSİZCE düşer`
`uzun_kanon_bağlamı ∧ ¬önbellek` ⇒ `girdi_maliyeti → 10×`
⇒ Her sağlayıcıya **kendi API'siyle** gidilir; çeviri bir geçit katmanının işidir.

**P91** ⊨D ⊨K — ⭐ HIZ TEZİNİN ÖLDÜRÜCÜ ÖLÇÜMÜ
`gerçek_oturum_izi: 357.161 LLM_turu ∧ 432.510 araç_kaydı ∧ 43 geliştirici`
`duvar_saati = insan_düşünme %92,3 ⊕ araç_yürütme %4,8 ⊕ LLM_üretimi %3,3`
⇒ **hızlı çıkarımın dokunabileceği dilim = toplamın otuzda biri**
`medyan_önek ≈ 120k` ∧ `medyan_çıktı ≈ 200` ⇒ `girdi = 294 × çıktı`
`decode_farkı(2000 t/s vs 500 t/s) ≈ 0,3 sn` ∧ `ölçülen_ilk_token_gecikmesi = 1,54 sn`
⇒ `1,54 > 5 × 0,3` ⇒ **4× decode üstünlüğü bu iş sınıfında ölçülemez hâle gelir.**

**P92** — GÖRÜNÜRDEKİ ÇELİŞKİNİN ÇÖZÜMÜ (payda farkı, çelişki DEĞİL)
`insansız_benchmark → LLM_süresi = %71..98`
`insan_döngüde_gerçek_oturum → LLM_süresi = %3,3`
⇒ **`insan_devrede → hız ≈ önemsiz`** ∧ **`ajan_otonom → model_süresi baskın`**

**P93** ⊨D ⊨K — ÜÇ EK ENGEL
① `Claude_Code → rastgele_OpenAI_uyumlu_sağlayıcı = KABUL_ETMEZ` ⇒ Cerebras/Groq yalnız **araç seviyesinde taşeron**, sürücü değil.
② `turların %95,7'si → önbellek_isabeti` ∧ `sağlayıcı_değişimi → 120k_soğuk_prefill` ⇒ **hızlı çıkarım konuşmanın ortasına serpiştirilmez**, kendi başına duran işlere verilir.
③ `SWE-bench Pro: Sonnet 4 = 42,70 ±3,59` vs `gpt-oss-120b = 16,20 ±2,67` (≈2,6×) ⇒ hızlı sağlayıcıya geçmek *"aynı işi daha hızlı"* değil, **"farklı bir zekâ sınıfıyla daha hızlı"**.

**P94** ⊨D — ⭐ ENTEGRASYON KATMANI HÜKMÜ
`okunan_katman → tek_markdown_besleyebilir = KANITLANDI` (üç bağımsız üreticiden [D]: `@AGENTS.md` içe-aktarımı ∨ symlink · ters yönde yerleşik geri-düşüş · `context.fileName` dizi kabulü)
`yürütülebilir_katman → HAYIR`

| Taşınan | Taşınmayan |
|---|---|
| CLAUDE.md · 4 beceri | `.claude/agents/` · `.claude/hooks/` · **`settings.json` izin bloğu** |

⇒ **`paylaşılabilir_yüzey = %100` ∧ `yürütülebilir_yüzey = %0`**
⇒ Ve taşınmayan şey **Dilim-1 izin kilidinin ta kendisidir**.

**P95** — HÜKÜM: ŞU AN ALINMAZ
`Continue = ölü` · `Orca ADE → çekirdek_değeri ∈ Claude_Code(yerleşik)` · `OpenHands ≡ Orca` (ikisi birden anlamsız) · `Aider → MCP = ∅` ⇒ ekosisteme bağlanamaz · `Cline ∧ Codex CLI = doğrudan ikiz` · `Cerebras/Groq(ana_döngü) → P91` · `LiteLLM self-host → tedarik_zinciri_emsali`
⇒ `gerçek_kazanç ≠ araç_sayısı` ∧ `gerçek_kazanç = model_rolünün_ayrışması ⊕ doğrulamanın_dışsallaşması`

---

## XVII. TEKNOLOJİ SEÇİMİ (A22)

**P96** — AİLENİN ÇEKİRDEK ASİMETRİSİ
`ölçülmüş(teknoloji_seçimi) ≈ ekosistem_sağlığı` — *seçtiğin şey yaşayacak mı*
`ölçülmemiş(teknoloji_seçimi) ≈ karar_yöntemi` — *nasıl seçmelisin*
`herkesin_baktığı_sinyal(yıldız) → ölçülmüş_şekilde BOZUK`
`kimsenin_bakmadığı_sinyal(indirme) → ölçülmüş_şekilde GÜÇLÜ` *(toplu düzeyde; paket-başına garanti değil — K4, bkz. P98)*

**P97** ⊨D — TERK TABANI (kendi ölçümümüz, n=478, ±4,5pp)
`paket ~ Uniform(PyPI)` ⇒ `P(son_sürüm > 2_yıl) = %54,2` ∧ `medyan_durgunluk = 856 gün`
⇒ `"PyPI'da paket var" → bilgi ≈ 0`

**P98** ⊨D — GRADYAN (4 katman × 500)
`indirme_sırası ∈ [1,500]` ⇒ `terk(>2yıl) = %8,6`
`indirme_sırası = rastgele` ⇒ `terk(>2yıl) = %54,2`
`gradyan = monotonik` ∧ `oran = 6,3×`
⇒ **`top_500'de_kalmak → terk_riski ÷ 6,3`** — ölçülmüş bir eşik, retorik değil.
> **[H4/K4 · antitez daraltması]** Bu ölçüm bir **katman agregasıdır**, paket-başına garanti **değildir**. `indirme → bakım_aktifliği` ilişkisi **toplu düzeyde** güçlüdür ∧ tek pakete uygulanamaz. Karşı-örnek sınıfı: `moment.js` bakım moduna geçti ∧ indirmeleri devasa kaldı; `request` deprecated ilan edildikten sonra yıllarca yüksek kaldı ⇒ **ekosistem ataleti**. Bu örnekler `[K-hatırlama]`dır (doğrulanmadı) ama mekanizma kendi M7 bulgumuzla uyumlu (*"çoğu alt-proje terk edilmiş bağımlılığı hiç değiştirmiyor"*) ⇒ kayıt kabul edildi. Agregayı **çürütmez**, `paket_başına_öngörü` okumasını **yasaklar**.

**P99** ⊨D — YAYIN YETKİSİ YOĞUNLAŞMASI (220.469 paket)
`en_çok_bağımlısı_olan_1000` ⇒ `tek_bakımcı = %41,3` ∧ `tek_bakımcı ∧ >2yıl_durgun = %17,8`
*Kaveat (ajanın kendi dürüstlük notu):* `maintainers = yayın_hesabı ≠ insan_sayısı`
⇒ Bu metrik **tedarik_zinciri_riski** için doğru, **bus_factor** için DEĞİL.

**P100** ⊨D — YILDIZ BOZUK
`lockstep_ile_işaretlenen_depo` ⇒ `%81,4'ünde sahte_oran ≥ %90`
`zirve(2024-07)` ⇒ `yıldız_aktivitesi_olan_depoların %16'sı → kampanyayla_ilişkili`
`düşük_aktivite_işaretlisi ∧ yıldız ≥ 1000` ⇒ `3.672 depo` (küçük spam değil, **"başarılı görünen"** projeler)
⇒ **`yıldız ∉ seçim_kriteri`**

**P101** ⊨K ⊨X — ⭐ AMİRAL GEMİSİ ÇÖKTÜ
`Ray_ve_ark(729_proje): 11_dil ↔ hata_yoğunluğu = anlamlı`
`bağımsız_yeniden_analiz ∧ çoklu_hipotez_düzeltmesi` ⇒ `anlamlı_dil = 4` ∧ `etki = "son derece küçük"`
`çürütme ∧ karşı_çürütme → tartışma_kapanmadı` ⇒ ⊨X
⇒ *"Hangi teknolojiyi seçtiğin ölçülebilir şekilde kaliteyi etkiler"* iddiasının **en çok atıf alan kanıtı buharlaştı**.

**P102** — YANLIŞLANABİLİRLİK KUSURU
`"boring" tanımı = ekibin_beceri_setine_göre_değişir` (tezin kendi savunucularından)
`tanım = sonuca_göre_ayarlanabilir` ⇒ `hipotez = test_edilemez`
⇒ F2 **"kanıt bulunamadı" diye değil, YANLIŞLANAMAZ olduğu için** folklordur. *(Bu ayrım epistemolojik olarak kritiktir.)*

**P103** — FOLKLOR SINIFI: KULLANILMAYACAK
`iddia ∈ {CNCF %42 monolite_dönüş, Gartner %60 pişmanlık, mikroservis_göçü %73 başarısız, teknik_borç %23/%31/%287/4,7ay, COBOL %67}`
∧ `birincil_kaynak = ∅` ∧ `dolaşım_yeri = içerik_çiftliği`
⇒ **`kullanma`**
`iddia ∈ {innovation_token = 3, boring→iyi_sonuç, Radar_isabeti, ATAM_faydası, ADR→daha_iyi_karar, lock-in_pahalı, YAGNI_maliyet_modeli, rakip_sayısı_heuristiği}` ∧ `ölçüm = ∅` ⇒ **folklor, ama uydurma değil** — ayrı sınıf.

**P104** — EN BÜYÜK KANIT BOŞLUĞU
`tüm_ampirik_literatür ∈ {ekosistem_ölçeği, kurumsal_takım_ölçeği}`
`solo_geliştirici ∨ kişisel_sistem` ⇒ `ölçüm = ∅`
⇒ **Salih'in tam bulunduğu yer ölçülmemiş.** Kapatılamaz — ama **üretilebilir** (V65).

---

## XVIII. KARAR ÖĞRENME ORTAMI (A24)

**P105** ⊨K — GEÇERLİ ORTAM ÖLÇÜTÜ
`güvenilir_sezgi ⇔ ortam_düzenli ∧ geri_bildirim(hızlı ∧ belirsizlik_içermeyen)`
`¬(biri)` ⇒ `kendinden_emin_sezgi → sistematik_hata`
`yüksek_geçerlilik = gerek_şart` ∧ `≠ yeter_şart`

**P106** ⊨K [ÇIKARIM, ölçüm DEĞİL] — ⭐ SINIR BEYANI
`mimari_kararlar → Kahneman-Klein_ölçütünü_karşılıyor_mu?` ⇒ **doğrudan ölçen çalışma = ∅**
Dolaylı: `ATD_tezahürü = gecikmeli` ∧ `gecikme ≈ sistem_ömrü_mertebesi`
Dolaylı: `sonuç_yanlılığı_replikasyonu: d = .77 [.62,.93] → 1.1 [.94,1.26]` — **orijinalden GÜÇLÜ**, üstelik katılımcılar *"sonuca bakmamalıyım"* dedikleri hâlde
⇒ `mimari = kötü_öğrenme_ortamı` hükmü **bileşimdir, literatür bulgusu DEĞİLDİR**.
⚠️ **Bu raporun en çok yaslandığı önerme, aynı zamanda en az doğrudan desteklenen önermesidir.**

**P107** ⊨K — DENEYİM ≠ UZMANLIK
`62_değerlendirme` ⇒ `32 (%52) → yıl↑ ise performans↓` ∧ `13 (%21) → ilişkisiz` ∧ `1 (%2) → tüm_çıktılarda_artış`
Yazılım paraleli: `sanayi_deneyimi → kalite ∧ üretkenlik etkisi ≈ 0`
⇒ `geri_bildirim_zayıf → yıl_sayısı ≠ uzmanlık`

**P108** ⊨X — DELIBERATE PRACTICE
`açıklanan_varyans: oyun %26 · müzik %21 · spor %18 · eğitim %4 · MESLEKLER <%1`
`yazılım ∈ meslekler` ⇒ **en düşük dilim**
`çift_kör_replikasyon → çekirdek_bulgu tekrarlanmadı` ∧ `karşı_yanıt yayımlandı` ⇒ tartışma kapanmadı
`DP_payı(yazılım_mühendisliği)` ⇒ **ölçüm = ∅**

**P109** ⊨K — VAKA SAYISI EŞİĞİ
`kaynak_analog = ∅` ⇒ `çözüm ≈ %10`
`kaynak_analog = 1` ⇒ `çözüm ≈ %30`
`kaynak_analog = 1 ∧ ipucu` ⇒ `çözüm ≈ %80`
`şema_tümevarımı ⇔ İKİ_vakanın_karşılaştırılması`
⇒ **`tek_vaka_okuma → transfer DÜŞÜK ∧ transfer ≠ 0`**
> **[K9 + H1 · antitez düzeltmesi]** Eski sonuç satırı `tek_vaka_okuma → transfer ≈ 0` idi ∧ **kendi öncülüyle çelişiyordu** (öncül zaten `%30` diyor). Doğrusu: `∅ analog → ~%10` ∧ `1 analog → ~%30` ∧ `1 analog + ipucu → ~%80`. Şema tümevarımı için **iki** vaka gerekir; ama tek vaka **sıfır getiri değildir**.

**P110** ⊨K — BAŞARISIZLIK > BAŞARI
`öğrenme(başarısızlık) > öğrenme(başarı)` ∧ `değer_kaybı(başarısızlık_bilgisi) < değer_kaybı(başarı_bilgisi)`
*"Başarıdan gelen bilgi uçucu, başarısızlıktan gelen yıllarca kalıyor."*
**Ama:** `postmortem_pratiği → sahada tutarlı_uygulanmıyor` ∧ `çoklu_postmortem_birlikte_analizi ≈ ∅`

**P111** ⊨K — ⭐ AİLENİN EN OPERASYONEL BULGUSU
`belirsizlik_değerlendirmesi_iyileşir ⇔ AÇIKÇA_FORMÜLE_EDİLMİŞ_strateji_kullanıldı`
`sezgi_temelli_yansıtma` ⇒ `öğrenme ≈ 0`
`kötü_formüle_edilmiş_geçmiş_tavsiye` ⇒ **zararlı olabilir**
⇒ **`yapılandırılmış_yansıtma ∧ ¬yazılı_kural → yetersiz`**

**P112** ⊨K ⊨X — KALİBRASYON KOŞULSUZ ÇALIŞMAZ
`GJP_eğitimi` ⇒ `3.yıl +%6` ∧ `4.yıl +%7` — **gerçek ama mütevazı**
`tek_pratik_turu` ⇒ `%98_GA_ıskalama: %41 → %23`
**Karşı:** `ticari_kalibrasyon_kursu(n=70)` ⇒ `iyileşme var ∧ etki göreve_bağlı`; ayrı çalışma: *"pratik skorlama kuralıyla kalibrasyon geri bildirimi güveni kalibre ETMİYOR"*
⇒ `"tahmin ⊕ kayıt ⊕ skorlama → otomatik_işler"` iddiası **⊨X**

**P113** — MÜFREDATIN KENDİ ZAYIFLIĞI (ajanın beyanı, korunuyor)
`L10 ∧ L11 → mimari_karar_kalitesini_artırır` ⇒ **ölçülmüş kanıt = ∅**
`mekanizma_gerekçesi = sağlam` ∧ `sonuç_kanıtı = ∅`
⇒ DONE tanımları bu yüzden `kavrayış` değil **`artefakt_sayısı`** olarak kuruldu.
`L12_rubriği` ⇒ **kendi imalatımız** (valide edilmiş mimari karar rubriği = ∅) ⇒ `[?]`

---

## XIX. AJAN SONLANMA (A25)

**P114** ⊨D — ÖNCÜL DÜZELTMESİ
`Stopped ⇔ Ctrl+X ∨ claude_stop ∨ dış_kill`
`oturum_limiti ∨ hız_limiti ∨ max_turns ∨ stall` ⇒ **`Failed`** ∧ `¬Stopped`
Ampirik (bu oturum): `35 bildirim = 22 completed ⊕ 13 failed ⊕ 0 stopped`
⇒ **`Stopped` en NET tanımlı durumdur**; belirsiz olan **`Failed`**'dır.
> **[K15 · antitez daraltması]** `Stopped ⇔ (üç yol)` çerçevesi bir kenar-durumda çatlıyor: `makine_kapanması` da dışarıdan süreç sonlandırmadır ∧ `agent-view.md`'ye göre **`Failed`** üretir, `Stopped` değil. Ayrıca `oturum_durumu(agent-view) ≠ alt_ajan_task_durumu`; bu önerme ikisini birleştiriyor olabilir. `⇔` (ancak ve ancak) **`→`'ye zayıflar**.

**P115** ⊨D — KATEGORİ HATASI
`claude agents → arka_plan_oturumları` ∧ `claude agents ∩ alt_ajanlar = ∅`
`~/.claude/jobs/ → bu_makinede YOK` ∧ `alt_ajan_transkripti = 115`
⇒ İki ayrı dünya; alt-ajanı `claude agents`'ta aramak **sonuçsuz**.
> **[K16 · antitez daraltması]** `∩ = ∅` (hiç göstermez) fazla güçlü. `sub-agents.md` bir geri-düşüş yolu tanımlıyor: *"`claude agents` bir sayı ∧ ardından yapılandırılmış alt-ajanların listesini basıp çıkıyorsa, agent view kullanılamıyor demektir."* ⇒ `agent_view_kapalı → claude agents, yapılandırılmış alt-ajanları LİSTELER`. Ana tablo iddiası (*alt-ajanlar ayrı satır olarak listelenmez*) **doğru kalır**; "hiç" **düşer**.

**P116** ⊨D — İKİ ORTOGONAL EKSEN
`eksen_1(görev) ∈ {Working, Needs_input, Idle, Completed, Failed, Stopped}`
`eksen_2(süreç) ∈ {✻ canlı, ∙ çıkmış, ✢ loop_uykusu}`
`∙ ⇏ sonlanma` ∧ `boşta ≈ 1_saat → süpervizör_süreci_kapatır` ∧ `transkript ∧ durum → diskte kalır`

**P117** ⊨X — TUZAK *(etiket ⊨D'den ⊨X'e düşürüldü, K11)*
`subtype ∈ {error_max_turns, error_max_budget_usd}` ⇒ `is_error = ?` — **ÇÖZÜLMEDİ**
⇒ Pratik hüküm KORUNUR: ayırt etme **`subtype` ile yapılır**; `is_error`'a dayanan filtre yazılmaz.
`subtype = hata` ⇒ `errors: string[] ∈ şema` ∧ `result_alanı → dile bağlı`
> **[K11 · antitez ÇÜRÜTMESİ — ⭐ yüksek]** Bu önermenin eski hâli `is_error = FALSE` diyordu ∧ dayanağı kurulu `cli.js` v2.1.42'de `is_error:!1` idi. Antitez `agent-sdk/python.md`'yi birebir okudu: *"`is_error`: `True` when the conversation ended in an error state. **Always `True` on the `error_*` subtypes.**"* ⇒ **doğrudan çelişki, çözülmedi ⇒ `⊨X`**. Uzlaştırma adayları (hiçbiri doğrulanmadı): ① minifiye kod okuması yanlış · ② CLI'nin iç üretim yolu ≠ SDK'nın belgelenmiş sözleşmesi · ③ sürüm kayması (`v2.1.42 ↔ ~v2.1.217`). **Tavsiye ayakta, gerekçesi düştü:** `subtype`'a bakmak her iki senaryoda da doğrudur.
> **[K17 · antitez daraltması]** `result_alanı ∉ şema` **dil belirtmiyor** ∧ yarısı yanlış: `TypeScript → result alanı YOK` ∧ `Python_dataclass → tüm varyantları tek şekle düzleştirir ⇒ result alanı VAR ∧ değeri None`. Kod yazarken **alanın yokluğuna değil, `subtype`'a** bakılır.

**P118** ⊨D — ⭐ `failed` TERMİNAL DEĞİLDİR
`ajan → failed(t₀)` ∧ `limit_sıfırlandı(t₁ > t₀)` ⇒ `ajan devam edebilir ∧ raporunu bitirebilir`
Ölçüm: `5 ajan → hata_damgasından_sonra 20.274..34.998 karakter rapor üretti`

**P119** — ▲ A25'İN SAYISINI DÜZELTİYORUM
A25 hükmü: `3_rapordan_2'si teslim_edilmedi`
Carvis tam-oturum taraması: `5/5 → completed bildirimi gönderildi` ⇒ **bu oturumda veri kaybı = 0**
`teslim ⇐ elle_SendMessage_ile_sürdürme` ∧ `¬müdahale → A25_hükmü doğru olurdu`
⇒ **`mekanizma ⊨D korunur` ∧ `sayı ⊨X düşer`**

**P120** ⊨D ⊨X — "PARTIAL WORK ISN'T LOST" YANILTICI
`last_output ≡ son_assistant_metin_bloğu`
Ölçülen `<result>` uzunlukları: `{0, 71, 137, 147, 160}` karakter — içerik = ara-not gürültüsü
⇒ **`iddia(dosya_seviyesi) = doğru` ∧ `iddia(bağlam_seviyesi) = yanlış`**
`output_file → transkripte SYMLINK` ⇒ kurtarma mümkün, ama **varsayılan akışta yapılmaz**.

**P121** ⊨D — SON-KAYIT İMZA TABLOSU (115 transkript)
`isApiErrorMessage: true ∧ stop_reason: "stop_sequence"` ⇒ **API ölümü** (n=17) — *sentetik işaretçi, gerçek API stop_reason'ı değil*
`stop_reason: "tool_use" ∧ metin = ∅` ⇒ **araç ortasında öldü** (n=6)
`son_kayıt.type = "user"` ⇒ araç sonrası öldü (n=3)
`normal_metin ∧ bildirim = failed` ⇒ **P118 vakası — transkripti oku**
`isMeta ∧ "was stopped by the user"` ⇒ kullanıcı iptali; ayırt edici: bu mesajda *"TaskOutput ile kontrol et"* cümlesi **HİÇ geçmez**
> **[K18 · antitez daraltması]** `isApiErrorMessage` için kullanılan **"tek keskin ayırt edici"** süperlatifi doğrulanamadı. Doğrulanan kısım: eşleşmenin kendisi kaynak kodda **⊨D** — `kjq()` sabit-kodlu `stop_reason:"stop_sequence"` ∧ `CY()` `isApiErrorMessage:!0`. Alan **başka bağlamlarda da** kullanılıyor ⇒ `tek` **düşer**, `imza geçerli` **kalır**.

**P122** ⊨D — KATMANLAR ARASI KAYIP
`SDK → 5 ayırt_edilebilir_terminal_durum`
`task_notification → 3 değer {completed, failed, stopped}`
⇒ `(bütçe) ⊕ (altyapı_hatası) ayrımı → SİLİNİR`
Kıyas: `Temporal → CANCELED ≠ TERMINATED` ∧ `LangGraph → GraphRecursionError ≠ NodeCancelledError ≠ NodeTimeoutError`
⇒ **Zaaf taksonomide değil, KATMANLAR ARASI KAYIPTA.**

---

## XX. KOTA MİMARİSİ (A26)

**P123** ⊨D — LİMİT SAYISI
`ayrı_limit_sayısı = 16` ∧ çoğu birbirinden bağımsız
`oturum_limiti ∧ haftalık_limit → tüm_modeller_ORTAK` ⇒ `/model → erişimi geri getirmez`
`Opus_limiti → model_özel` ⇒ `/model → çalışma DURMAZ`
`tek_yoğun_patlama` ⇒ `haftalık_kota, oturum_penceresi_sıfırlanmadan tükenebilir`

**P124** ⊨D — PENCERE MEKANİĞİ YANLIŞ ANLAŞILIYOR
`API → token_bucket` ⇒ *"capacity is continuously replenished… rather than being reset at fixed intervals"*
⇒ `"resets at X" ≡ TAM_DOLUM_anı` ∧ `≠ sıfırlanma_anı`
⇒ **`reset_beklemek → gereksiz`**; kısmi kapasite daha önce açılır.
`abonelik → yuvarlanan_pencere ⊕ ilan_edilmiş_reset`
⇒ **İki farklı mekanizma; birinden çıkarılan sezgi diğerinde YANLIŞ.**

**P125** ⊨D — ⭐ SESSİZ BOZULMA
`WebSearch_bütçesi = 200 / oturum` ∧ `sayaç = ana_konuşma ⊕ TÜM_alt_ajanlar`
`bütçe_doldu` ⇒ `¬hata` ∧ `arama = boş_döner` ∧ *"You don't see the notice"*
`112_ajan × 2_arama = 224 > 200` ⇒ **zarf zaten aşılmıştı**
⇒ `A8 ∧ A12 ∧ A18 → "bulunamadı"` iken doğru cevap muhtemelen **"aranamadı"**
⇒ Panzehir: `brifingte_URL_verilir → ajan WebFetch_kullanır → bütçeden YEMEZ` *(A26 ajanı bu araştırmayı **2 WebSearch** ile bitirdi)*

**P126** ⊨D — ⭐ PARALELİN GİZLİ MALİYETİ
`alt_ajan → kendi_konuşması ∧ kendi_sistem_promptu` ⇒ `ilk_çağrıda önbellek_isabeti = 0`
`alt_ajan ∧ tur > 1` ⇒ **`KENDİ önbelleğini ısıtır`** (isabet > 0)
`alt_ajan → 5_dakikalık_TTL` **abonelikte bile** (1 saatlik otomatik TTL yalnız ana konuşmaya)
`önbellek_OKUMA ∉ ITPM` ∧ `önbellek_OLUŞTURMA ∈ ITPM`
⇒ **`10_paralel_KISA_ÖMÜRLÜ_ajan → ITPM_baskısı > 10 × tek_ajan`**
⇒ **`az_sayıda_uzun_ömürlü > çok_sayıda_kısa_ömürlü`**; 30 yerine 10 ajan ⇒ 20 cache-oluşturma turu tasarrufu.
> **[K12 · antitez ÇÜRÜTMESİ — ⭐ yüksek]** Eski hâli *"alt-ajanlar prompt cache'ten yararlanamaz"* diyordu ⇒ **fazla güçlü, yanlış**. `prompt-caching.md` birebir: *"It builds its own cache, **starting with no cache hits on its first call and warming up across its own turns.**"* ⇒ isabet sıfırı **yalnız ilk çağrıdadır**. `10 ajan = 10× ITPM` çıkarımı **yalnız kısa ömürlü ajanlar için** ayakta. Düzeltme **tavsiyeyi zayıflatmıyor, GÜÇLENDİRİYOR**: uzun ömürlü ajan kendi önbelleğini ısıttığı için *"az sayıda uzun ömürlü"* tercihinin mekanizması artık nettir.

**P127** ⊨D — EŞZAMANLILIK: ÜÇ AYRI MEKANİZMA
`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS = 20` ⇒ **belgelenmiş alt-ajan eşzamanlılık sınırı**
`MAX_TOOL_USE_CONCURRENCY = 10` ⇒ **paralel araç + alt-ajan YÜRÜTME kapısı** (ayrı mekanizma)
`10_oturum ≈ 10× kota` ⇒ **tüketim kuralı, sınır DEĞİL** (üçüncü ve tamamen farklı şey)
⇒ `pratik_dalga_zarfı = 10` **korunur**; gerekçesi `sert_sınır` **değil**, `yürütme_kapısı ⊕ kota_tüketimi`

**P128** ⊨D — DİĞER TAVANLAR
`MAX_SUBAGENTS_PER_SESSION = 200` (nested ⊕ fork ⊕ background ⊕ /subtask; **bitenler de sayılır**) ∧ `/clear → sıfırlar`
`MAX_SUBAGENT_SPAWN_DEPTH = 1` ⇒ varsayılanda **alt-ajan alt-ajan doğuramaz**
`529 → kotaya SAYILMAZ`
`batch → senkron_kotayı ETKİLEMEZ` ∧ `%50 indirim`

**P129** ⊨D — WATCHDOG TAKASI
`RETRY_WATCHDOG = 1` ∧ `cevap → reset_zamanı_taşıyor` ⇒ `kör_backoff YERİNE pencerenin_bitişini_bekler`
⇒ `5_saatlik_limite_çarpan_ajan → saatlerce asılı kalabilir`
⇒ **`watchdog ≠ başarı_garantisi` ∧ `watchdog = başarısızlığı_duvar_saatine_çeviren_TAKAS`**
Kural: `gözetimsiz_koşum → aç` ∧ `interaktif_dalga → kapat` (orada hızlı başarısızlık + yeniden dalga daha ucuz)

**P130** ⊨D — MODEL KOVASI KALDIRACI
`Opus 5 → ayrı_ITPM_kovası` ∧ `Sonnet 5 → ayrı`
`işçiler := Sonnet` ⇒ `işçi_trafiği ∩ Opus_kovası = ∅`
⇒ **Aynı kotayla iki paralel havuz.** V59'un ("ucuz model") **mekanizması budur** — tavsiye tasarruf değil, **kova ayırma** hamlesiymiş.

**P131** ⊨D — EFFORT KALEMİ
`varsayılan_effort = high` ∧ `düşünme_token'ları → ÇIKTI olarak faturalanır`
⇒ `getirme_ajanı := effort(low ∨ medium)` ∧ `sentez_ajanı := effort(high)`
⇒ 112 ajanlık koşumda **tek başına en büyük token kalemi**.

**P132** — ⭐ DALGA ZARFI (V70 adayı)
`dalga := 10_ajan ⊕ Sonnet ⊕ effort(medium) ⊕ 2-3sn_aralı_başlatma ⊕ ≤2_WebSearch/ajan ⊕ oturum_toplamı ≤ 60..80 ⊕ sert_bütçe_tavanı ⊕ watchdog(yalnız_gözetimsiz)`
`gözlenen_koşum = 112_ajan` ⇒ **zarfın DIŞINDA**
⇒ **`%22_limit_sonlanması = BEKLENEN_SONUÇ` ∧ `≠ anomali`**

---

## XXI. DAYANIKLILIK VE SÜRDÜRME (A27)

**P133** ⊨D — KURTARMA MÜMKÜN
`alt_ajan_transkripti → ana_konuşmadan BAĞIMSIZ dosya`
`ana_konuşma → compact` ⇒ `alt_ajan_transkripti etkilenmez`
`cleanupPeriodDays = 30` (varsayılan)
`SendMessage` ⇒ `tam_konuşma_geçmişi korunur` (tüm araç çağrıları ⊕ sonuçlar ⊕ akıl yürütme)
`sürdürme → eşzamanlılık_limitini KONTROL ETMEZ` ⇒ kurtarma yolu kapasite kapısından **muaf**.

**P134** — İKİ İSTİSNA: BİRİ ASKIDA, BİRİ ⊨D
① `[?]` **ASKIDA — kural olarak KULLANILMAZ:** `ajan ∈ {Explore, Plan} ⇒ agent_ID = ∅ ⇒ SÜRDÜRÜLEMEZ`
② ⊨D `kullanıcı_durdurdu` ⇒ `SendMessage → "ajan iptal edildi" reddi`; çözüm: panel transkriptine yazmak bayrağı temizler.
> **[K14 · antitez — ⭐⭐ KRİTİK, dayanak bulunamadı]** ①'in dayanağı **dokümanda bulunamadı**. Antitez `sub-agents.md`'yi okudu: Explore/Plan için sürdürülemezlik istisnasına dair **hiçbir kayıt yok**; bu ajanlar için tutulan tek istisna CLAUDE.md/git-status **yüklememeleridir**. Bu iddia bir alt-ajanın aktarımıydı ∧ **doğrulanmadan** tavsiye listesinin başına konmuştu (U1). ⇒ **`ajan_ID` boşluğu doğrulanana dek *"Explore/Plan kullanma"* diye bir kural ÇIKARILMAZ.** ②'nin durumu değişmedi.
> **[M5 · türetilen kural adayı]** `tavsiye_sırası = 1 → dayanağı BAĞIMSIZ doğrulanmış olmalı`. Listenin başı, en az doğrulanmış maddenin yeri değildir.

**P135** ⊨D — ⭐ KAYIP MEKANİZMASI VE PANZEHİRİ
`ajan → metin_üretti ∧ kesildi` ⇒ `kısmi_çıktı + "kesildi" notu DÖNER`
`ajan → (hiçbir_şey ∨ yalnız_araç_çağrısı) ∧ kesildi` ⇒ `Agent terminated early` ∧ **her şey kaybolur**
`araştırma_ajanı_profili ≡ (20_WebFetch ⊕ tek_rapor)` ⇒ ikinci sınıfa düşer
⇒ **PANZEHİR (U2/V69): `ilk_bulgu_bulunur_bulunmaz → KISA_ARA_METİN üret`** — kayıp modunu *"her şey gitti"*den *"kısmi döndü"*ye çevirir, **maliyet = 0**.
⚠️ `[?]` Ölçülen pay: `tool_use ile ölüm = 6/115 = %5` ⇒ mekanizma teyitli, **ağırlığı hipotezin öngördüğünden düşük**.

**P136** ⊨D — CHECKPOINTING İŞ DAYANIKLILIĞI İÇİN DEĞİL
`/rewind → bash_ile_değiştirilen_dosyaları İZLEMEZ` ∧ `alt_ajan_düzenlemelerini GERİ ALMAZ`
Dokümanın kendi ifadesi: *"checkpoint = yerel geri al · Git = kalıcı tarihçe"*
⇒ **`git_commit = tek_gerçek_checkpoint`**
⇒ JARVIS'in m.10 kuralı bu boşluğu **zaten kapatıyor** — kanon bu noktada dokümandan önce doğruydu.

**P137** ⊨D — ÜRETİCİNİN KENDİ TAVSİYESİ
*"Oturum sürdürmeye güvenme. İhtiyacın olan sonuçları uygulama durumu olarak yakala… transkript dosyalarını ortalıkta taşımaktan çoğu zaman daha sağlamdır."*
⇒ **`artımlı_dosya > transkript_kurtarma`**
⇒ Bu, *"veri kaybı istemiyorum"* talimatının **teknik karşılığıdır** ∧ raporları koşum bitmeden diske yazıp commit'lemenin gerekçesidir.

**P138** ⊨D ⊨X — ÖNCÜL DÜZELTMESİ: DETERMİNİZM
`"Date.now() ∧ random() → durable_execution'da YASAK"` ⇒ **YANLIŞ**
`TypeScript_SDK → deterministik_sürümleriyle DEĞİŞTİRİLİR` ⇒ doğrudan kullanılabilir
`Go_SDK → API_ikamesi gerekir` (`workflow.Now()`)
`Side_Effect` ⇒ non-determinizm **yasaklanmıyor, KAYDEDİLİYOR**
⇒ **`yasak(random) = ∅` ∧ `yasak = KAYIT_DIŞI_non_determinizm`**

**P139** ⊨D — AJAN MİMARİSİNİN AYRIM ÇİZGİSİ
`LLM_çağrısı ∨ API_çağrısı ∨ DB_sorgusu` ⇒ **Activity** (kaydedilir, replay edilmez, otomatik retry)
`akış_kontrolü` ⇒ **Workflow** (deterministik, replay edilir)
⇒ Bu tek ayrım, ajan iş akışı tasarımının **omurgasıdır**.

**P140** ⊨K — TESLİM GARANTİSİ ÜÇLEMESİ
`oku → pozisyon_kaydet → işle` ∧ `çökme` ⇒ **at-most-once** (iş kaybolur)
`oku → işle → pozisyon_kaydet` ∧ `çökme` ⇒ **at-least-once** (iş tekrarlanır)
`exactly_once ⇔ çıktı ∧ ilerleme_işareti ATOMİK_yazılabilir`
`ajan_iş_akışı → atomiklik = imkânsız`
⇒ **`hedef := her_adımı_tekrar_güvenli_yap` ∧ `¬tekrarı_engellemeye_çalış`**
Kaynağın kendi uyarısı: *"Birçok sistem exactly-once iddia eder, ancak ince yazıyı okumak önemlidir."*

**P141** — ⭐ AŞIRI-MÜHENDİSLİK HÜKMÜ
`Temporal_kurulumu → Service ⊕ persistence_store ⊕ Worker_filosu` ∧ `determinizm_kısıtları → tüm_iş_akışı_kodunu_yeniden_yazdırır`
`Temporal'ın_çözdüğü_problem = binlerce_eşzamanlı_workflow ⊕ çoklu_makine ⊕ çoklu_takım`
`JARVIS = tek_kişilik`
⇒ **`kavramları_al ∧ ¬çalışan_sistemi_al`** — *bu araştırmanın en net yargısı.*
Aynı sınıf: `kendi_WAL'ını_yazmak` (git zaten append-only log'un) · `Saga_altyapısı` (geri alma = `git revert`) · `/loop ile limit_sonrası_retry` (kaçırılan tetikleme telafi edilmez ∧ kontrolsüz retry = zararın kendisi)

---

## XXII. KOŞUMUN KENDİ ÖNERMELERİ — EK

**P142** — ÇÖZÜLEN ÇELİŞKİ: `api_retries_exhausted`
`A25: olay = ∅` (kurulu cli.js grep boş ∧ WebFetch özeti "yok")
`A26: olay = VAR` ∧ `nitelikler ∈ {total_attempts, total_retry_duration_ms}` (ham markdown)
Hüküm: **A26 haklı.** İki gerekçe: ① `WebFetch_özeti → alanları SESSİZCE DÜŞÜRÜR` (A26 bunu kendi yöntem notunda yakaladı) ② `kurulu_ikili = v2.1.42` ∧ `dokümanlar ≈ v2.1.217` ⇒ sürüm farkı grep'in boşluğunu açıklar
⇒ `A25'in_ölçümü(kendi_bağlamında) = doğru` ∧ `genellemesi = yanlış`
⇒ **KURAL (V68):** `code.claude.com ∨ platform.claude.com` ⇒ **daima `.md` son ekiyle ham çekim**.

**P143** — SÜRÜM ÇATALI BORCU
`kurulu_ikili = v2.1.42` ∧ `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS ∉ cli.js(grep)`
⇒ Ana atlastaki **stall-watchdog analizi bu makinede geçerli olmayabilir** — yeniden okunmalı.

**P144** — REGISTER HÜKMÜ (Salih, 07-26)
`rapor.tür = ai_to_ai` ⇒ `form := tam_önerme`
Gerekçe: `okuma_modu = Salih ⊕ JARVIS` ⇒ makine-eşlikli
⇒ `compiler := KAPALI` ∧ `insan_yüzü := ayrı_oturuma_ertelendi`
⇒ `¬insan_yüzü ⇏ eksiklik` — bu, F8'in (*uzman-alanda compiler kapalı*) genişletilmiş hâlidir: **uzman_alan ∨ makine_eşlikli_okuma ⇒ compiler kapalı.**

---

## Kullanım notu

Bir önermeyi kullanmadan önce:
1. **Öncülleri kontrol et.** Öncül sağlanmıyorsa sonuç geçmiyor. P49 bunun en net örneği — mimari hükmü var ama JARVIS'te üç öncül birden farklı.
2. **Etikete bak.** `⊨K` olan hiçbir önerme tüzük anlamında hüküm taşımaz (P70).
3. **`⊨¬2` olanı sınanmış sayma.** A5–A27 arası **tüm** aileler bu durumda (P71 + XV–XXI blokları).
4. **`⊨X` olanı kullanma.** Çelişki çözülmedi demektir, ortalama alınmaz. **İstisna:** P142 — çelişki gerekçeli olarak ÇÖZÜLDÜ, hüküm A26 lehine. **Yeni ⊨X:** P117 (`is_error`) — 07-26 antitezinde düştü.
6. **`[?]` olanı tavsiyeye çevirme.** P134① bunun canlı vakasıdır: doğrulanmamış bir öncül, tavsiye listesinin **başına** konmuştu. `tavsiye_sırası = 1 → dayanak BAĞIMSIZ doğrulanmış olmalı`.
7. **`⊨S` = "sağ kaldı" DEĞİL.** Doğru okunuşu: **"aynı-aile hakemi karşısında sağ kaldı."** Antitez ajanları tez ajanlarıyla aynı model ailesindendi ∧ öz-tercih sapması aile düzeyine yayılır (P86). **İstisna:** A25–A27 ∧ A31–A32'nin doküman-doğrulamalı `⊨S`'leri bu şerhten muaftır — kanıt modelden değil kaynaktan geldi.
5. **Ölçüm ile çıkarımı ayır.** P106 ve P119 bu ayrımın iki örneğidir: biri bileşim olduğunu beyan eder, diğeri bir alt-ajanın sayısını tam-oturum verisiyle düzeltir. **Beyan edilmiş sınır, sınırı olmayan önermeden güçlüdür.**
