# Lojik Dil → Kod Dil Dönüşümü — önerme formu

*Kayıt: 2026-07-26 · Carvis (CC, yan-oturum m.41) · Talep: "ilerde lojik temelli raporları okuyup kod yazacağımız zaman (lojik dili-kod dili) dönüşümü yapacağız. Bunun için dikkat etmemiz gereken şeyleri öğrenmemiz gereken şeyleri araştır atlasları koş rapor oluştur"*

**REGISTER:** Tam önerme formu (P144). Compiler KAPALI; insan-yüzü ayrı oturuma ertelendi.
**Aileler:** A31 (insan tarafı — biçimsel spec → kod) · A32 (LLM tarafı — model aracılı çeviri)
**Notasyon:** `2026-07-26-LOJIK-onerme-formu.md` §Notasyon. `⊨D` birincil · `⊨K` ikincil · `⊨X` çelişkili · `⊨¬2` antitez koşulmadı · `[?]` kestirim · `[ARANAMADI]` bütçe/erişim engeli — **yokluk kanıtı DEĞİL**.

---

## 0. BU AİLENİN TEK CÜMLELİK BULGUSU

> **`önerme_formu → kod` dönüşümünde kaybolan şey ÖNERMENİN KENDİSİ DEĞİL, ÖNERMENİN KİPİDİR.**
> `∀` sonlu örnekleme · `→` tek dala · `¬` "bulunamadı"ya · `[?]` ile `⊨X` tek bir `None`'a çöker.
> Her çöküş **sessizdir** — kod derlenir, test geçer, hata fırlatmaz.

Ve ikinci sırada:

> **Salih'in `[?]` ∧ `⊨X` etiketlerinin koda nasıl taşınacağına dair LİTERATÜRDE HİÇBİR ÖLÇÜM YOKTUR.** (L21)
> Bu bir erişim engeli değil — **arandı, alan boş.** Boşluğun kendisi bulgudur ∧ Salih'in doldurabileceği bir yerdir.

---

## 1. A31 — İNSAN TARAFI: BİÇİMSEL SPEC → KOD ⊨¬2

### 1.1 Sanayi sicili — var, ama "ne yakaladı" kaydı yok

**L1** ⊨D
`TLA+ → üretim_sistemlerinde fiilen kullanıldı`: MongoDB'nin Raft'ının basitleştirilmiş parçası · WeChat/Tencent PaxosStore (VLDB 2017) · Azure Cosmos DB tutarlılık modelleri · Voldemort dağıtık key-value store.
⚠️ `depo_metni → spec–implementasyon boşluğu hakkında açık ifade = ∅`; yalnız *"spesifikasyonların bir derlemesi"*.
⇒ **`benimseme_kanıtı = VAR` ∧ `"ne yakaladı / ne yakalamadı" kanıtı = YOK`.**

**L2** `[?]` — ▲ EN ÇOK ATIF BEKLENEN KAYNAĞA ERİŞİLEMEDİ
`AWS_biçimsel_yöntemler_raporu (CACM 2015)` ⇒ **birincil metne erişilemedi.**
Ajanın kendi beyanı: hatırladığı iddialar (TLA+'ın test ile aylar sürecek ince eşzamanlılık hatalarını bulduğu ∧ makalenin *"spesifikasyon uygulama değildir"* sınırlamasını **açıkça kabul ettiği**) **`[D]` olarak SUNULMADI** ∧ **rakam VERİLMEDİ.**
⇒ Bu ailenin **en çok atıf beklenen endüstriyel kanıtı DOĞRULANAMADI.**
⇒ `bu_eksene_dayanan_her_iddia ≤ [K-hatırlama]` ∧ bağımsız doğrulama gerektirir.

### 1.2 Araçların kendi itirafları — ⭐ epistemik sınırlar

**L3** ⊨D — DbC KÜTÜPHANE DÜZEYİNDEDİR, DİL DÜZEYİNDE DEĞİL
`icontract → {precondition, postcondition, invariant}` ∧ sözleşme kalıtımı (precondition zayıflatma / postcondition-invariant güçlendirme, Liskov).
Kütüphanenin **kendi konumlandırması**: *"Python'a DbC entegre edilene kadar bir geçici çözüm (work-around)"*
⇒ **`garanti = runtime_kontrol` ∧ `≠ dil_düzeyinde_garanti`** — kütüphane bunu **kendisi itiraf ediyor.**

**L4** ⊨D — ⭐ PROPERTY-BASED TESTING ∀'YI İSPATLAMAZ
`QuickCheck → "bu özelliklerin ÇOK SAYIDA rastgele üretilmiş durumda geçerli olduğunu TEST EDER"`
⇒ **`sonlu_örneklem_üzerinde_tutarlılık` ∧ `≠ evrensel_∀_ispatı`**
`fast-check` kendi konumlandırması: *"neyin bozulmaması gerektiğini değil, her zaman ne doğru KALMASI gerektiğini tarif edersiniz"*

**L5** ⊨D — SHRINKING: PBT'NİN ASIL DEĞERİ
`Hypothesis ∧ hata_bulundu` ⇒ **rastgele herhangi bir başarısız durumu değil, EN BASİT olanı raporlar** (shrinking/minimization).
Somut: `sorted(set(ls))` yanlışlıkla tekrarları sildiğinde en minimal karşı-örnek `[0, 0]`.
⇒ Değer yalnız *hata bulmak* değil, **hatayı okunabilir kılmaktır.**

**L6** ⊨D — YÜRÜTÜLEBİLİR DOĞAL-DİL GELENEĞİNİN İZİ
`npm cucumber (scope'suz) → DEPRECATED`, geliştirme `@cucumber/cucumber` altına taşınmış.
⚠️ **Bu, aracın terk edildiği anlamına GELMEZ** — paketleme/organizasyon düzeyinde bir süreklilik izidir. Zayıf kanıt olarak damgalanır.

### 1.3 ⭐⭐ LOJİK → KOD ÇEVİRİ TUZAKLARI

*Bu tablo bu ailenin ana katkısıdır. Salih'in kendi önerme kalıpları üzerinden yazıldı.*

| Önerme kalıbı | Naif kod karşılığı | Neden yanlış | Doğrusu |
|---|---|---|---|
| **`P → Q`** (maddi koşul) | `if P: assert Q` | Maddi koşulda `¬P` iken önerme **otomatik DOĞRU** sayılır (vacuous truth). Kod bunu es geçer ⇒ **`¬P` dalı sessizce doğrulanmamış kalır** | `¬P` dalını da AÇIKÇA test et (PBT'de hem `P` hem `¬P` girdi uzayını üret); `P→Q` ile `P⇔Q` farkını yorumda belirt |
| **`∀x. P(x)`** | `for x in liste: assert P(x)` | Kod yalnız **eldeki örneklem** üzerinde ∀'yı test eder. Sonlu örneklem ∀'nın **İSPATI DEĞİL** (L4) | PBT + shrinking ⇒ güven artışı, **tam ispat değil**. Model-checker (TLA+/Alloy) sonlu durum uzayını **tüketici** tarar ⇒ epistemik olarak **daha güçlü** |
| **`∃x. P(x)`** | `if any(P(x) for x in xs)` | Kapsam belirsizse — *"bir X vardır ki her Y için"* mi, *"her Y için bir X vardır"* mi (`∃∀` vs `∀∃`) — kod **SESSİZCE yanlış sırayı seçer**, hata fırlatmaz | Niceleyici sırasını önerme yazarken **açıkça numaralandır**; `∃x∀y` ile `∀y∃x` **farklı matematiksel nesnelerdir**; kod yorumunda sıra birebir korunur |
| **`¬(A ∧ B)`** | genelde elle `not a and not b` yazılır | De Morgan atlanır: `¬(A∧B) = ¬A ∨ ¬B`, **`¬A ∧ ¬B` DEĞİL** — klasik ∧ yaygın hata | Dönüşümü **programatik uygula**, elle yeniden türetme |
| **⭐ `[?]`** (kestirim) | `None` / `null` | `None` **üç-değerli mantığı gizlice ikiye indirger.** Ve *"bilinmiyor"* ile *"boş"* ile *"hata"* **aynı değerle** temsil edilir ⇒ **hangisi olduğu KAYBOLUR**. Ayrıca diller arası tutarsız: SQL'de `NULL = NULL → UNKNOWN`, Python'da `None == None → True` | `Option`/`Maybe` tipi **veya** açık üç-durumlu enum: `Known(x) \| Unknown \| Contradictory` |
| **⭐ `⊨X`** (çelişkili) | *(genelde kod karşılığı YOKTUR — atlanır)* | Çelişkili durumun kendi tip/dal karşılığı yoksa, çelişkili girdi **sessizce ilk eşleşen dala düşer** (genelde `else`) ⇒ **çelişki bilgisi kaybolur** | Ayrı `Contradiction` durumu/exception tipi. **`⊨X` asla `[?]` ile aynı koda düşmemeli** |
| **Kapalı-dünya `¬`** ("X yoksa Y'dir") | `if not found_in_db(x): return Y` | Mantıkta `¬P` = **P'nin yanlışlığının KANITLANMIŞ olması**; kodda `not found` = *"arandı, bulunamadı"* ⇒ **kanıtlanmamış yokluk** ile **kanıtlanmış yokluk** karışır. Prolog'un `\+` de klasik değil: *"şu an ispatlanamıyor"*, *"yanlıştır"* değil | OWA gerekiyorsa arama uzayının **TAM (complete)** olduğunu ayrıca garanti et; değilse *"bulunamadı"* ile *"yoktur"*u **kod-seviyesinde AYRI durumlar** yap |
| **`→` vs `⇔`** | ikisi de `if...then`, ters yön test edilmez | `A→B` doğrulanınca `B→A` da doğru **VARSAYILIR** (converse hatası) | Her `⇔` **HEM ileri HEM geri** yön testi ister; `→` **tek yön**, tersini test ETME |
| **⭐ `t` / `t+1`** (zamansal indeks) | `state = new_state` (mutasyon) | `t` ∧ `t+1` matematiksel olarak **iki ayrı, değişmez durum**. Mutasyonla üzerine yazılınca `t` **KAYBOLUR** ⇒ *"t ile t+1 arasında X değişmemeli"* tipi invariant artık **kontrol EDİLEMEZ** | TLA+ tam bunun için var (primed variables `X'` — eski ∧ yeni durumu **aynı ifadede** tutar). Kodda: **immutable snapshot + explicit diff/invariant-check** fonksiyonu |
| **Kesin önerme, yumuşatıcı yok** | `assert` / `raise` | Spec **bütün-uzay** için doğru; kod **yalnız test-edilen-uzay** için doğrulanmış olabilir (**refinement gap**) | Kod yorumunda üst-not: *"bu invariant spec'te model-checked, implementasyonda YALNIZCA test-edilmiş"* |

> **⭐ Salih'in önerme formu için en kritik üç satır:** `[?]` · `⊨X` · `t/t+1`.
> İlk ikisi **onun kendi notasyonunun ayırt ettiği** ama kodun varsayılan olarak **birleştirdiği** ayrımlardır.
> Üçüncüsü, `durum-kapsulu.md` gibi *"üzerine yazılır"* dosyalarının kod karşılığında **doğrudan bir tuzaktır.**

### 1.4 A31 — ÖLÇÜLMÜŞ vs FOLKLOR

**ÖLÇÜLMÜŞ (birincil kaynaktan doğrulandı):**

| İddia | Etiket |
|---|---|
| TLA+ endüstride üretim sistemlerinde fiilen kullanıldı/spesifiye edildi (L1) | ⊨D |
| Hypothesis başarısız durumu **otomatik olarak en basit hâline indirger** (L5) | ⊨D |
| QuickCheck sonlu-örneklem üzerinde özellik kontrolü yapar, **evrensel ispat değil** (L4) | ⊨D |
| icontract kendini **kütüphane-düzeyi geçici çözüm** olarak konumluyor (L3) | ⊨D |
| npm `cucumber` deprecated, `@cucumber/cucumber`'a taşındı (L6) | ⊨D |

**FOLKLOR ∨ DOĞRULANAMAYAN — rakam VERİLMEDİ:**

| İddia | Neden |
|---|---|
| *"TLA+ Amazon'da X ay sürecek hatayı Y günde buldu"* · *"%N formal methods hata azaltımı"* | Birincil kaynağa erişilemedi (L2). **İnternette yaygın dolaşıyor ∧ bu oturumda teyit EDİLEMEDİ** |
| *"PBT örnek-temelli testten %X daha fazla hata buluyor"* | Araç sayfaları **NİTELİKSEL** üstünlük iddia ediyor; **NİCEL karşılaştırma rakamı hiçbir birincil kaynakta YOK** |
| Doğal dil→mantık çevirisinde **ölçülmüş hata oranları** (∀/∃ sırası, De Morgan) | `[ARANAMADI]` — tüm akademik kanallar kapalıydı. **Bu eksenin ampirik desteği ŞU AN SIFIR**, yalnız kavramsal argüman var |
| Gherkin/BDD'nin endüstride terk edilme oranı | **Hiçbir ölçüm bulunamadı** |
| Alloy · Z · B-metodu endüstriyel vaka **ölçümü** | **Bulunamadı** (yalnız Alloy'un teknik README'si okundu, *"ne yakalar"* içeriği yoktu) |

### 1.5 A31 — İDDİA LİSTESİ (antitez için, gerekçesiz) ⊨¬2

① `[?]` ile `⊨X` tek bir `None`'a indirgenirse epistemik olarak farklı iki durum **geri alınamaz** biçimde birleşir. ② `P→Q` yalnız `P` doğruyken test edilirse, `¬P` durumu **hiç doğrulanmamış** gizli bir kör nokta yaratır. ③ PBT, ∀'nın **ispatını değil güven artışını** sağlar; bu epistemik zayıflama belirtilmezse *"test edildi"* ile *"ispatlandı"* karışır. ④ Model-checking PBT'den **epistemik olarak daha güçlüdür** ama yalnız **spec** üzerinde çalışır — kodun spec'e uyduğu **ayrı ∧ genelde doğrulanmamış** bir iddiadır. ⑤ DbC kütüphaneleri dil-seviyesinde değil kütüphane-seviyesinde konumlanır; bu, *"spec'i kodda garantiledik"* **yanılsamasına** yol açabilir. ⑥ Negation-as-failure klasik olumsuzlamadan **ontolojik olarak farklıdır**; önerme formunda `¬` kullanılan her yerin açık-dünya mı kapalı-dünya mı olduğu **belirsiz kalabilir**. ⑦ Zamansal indeksli önermeler mutasyonla ifade edilirse invariant kontrolü **imkânsız hâle gelir**. ⑧ Bu araştırmada **en sık atıf yapılan endüstriyel kanıta erişilemedi**; bu eksene dayanan her iddia en fazla `[K-hatırlama]`dır. ⑨ Doğal dil→mantık tuzaklarının **ölçülmüş hata oranlarına hiç erişilemedi**; ampirik destek **sıfırdır**.

---

## 2. A32 — LLM TARAFI: MODEL ARACILI ÇEVİRİ ⊨¬2

### 2.1 ⭐ En güçlü pozitif bulgu: biçimsel doğrulayıcı çalışıyor

**L7** ⊨D — CLOVER (kapalı-döngü doğrulanabilir kod üretimi)
`kod ⊕ docstring ⊕ biçimsel_ek_açıklama` üçlüsü arasında tutarlılık kontrolü:
`doğru_kod → kabul_oranı ≈ %87`
**`yanlış_kod → ölçülen YANLIŞ-POZİTİF = SIFIR`**
*(CloverBench, Dafny, ders kitabı seviyesi)*
⇒ **"İkinci bir BİÇİMSEL doğrulayıcıyla kontrol" güvencesinin doğrudan ölçülmüş örneği ∧ bu ailenin en güçlü tek kanıtı.**

**L8** ⊨K `[birincil doğrulanamadı]` — TİP-KISITLI DECODING
`tip_kısıtlı_decoding` ⇒ `derleme_hataları yarıdan_fazla ↓` ∧ `işlevsel_doğruluk +%3,5..5,5 (görece)` ∧ `derlenmeyen_kodun_onarımı +%37 (görece ortalama)`
⚠️ Birincil kaynağa erişilemedi ⇒ **rakamlar doğrulanana kadar temkinli kullanılır.**

**L9** ⊨K `[birincil doğrulanamadı]` — STATİK ANALİZ GERİ-BESLEME DÖNGÜSÜ
`linter_ile_iteratif_prompting (10 iterasyon)`: güvenlik `%40+ → %13` · okunabilirlik `%80+ → %11` · güvenilirlik `%50+ → %11`

### 2.2 Sözdizim ≠ semantik — ölçülmüş boşluk

**L10** ⊨D — DEĞERLENDİRME ALTYAPISI BU AYRIMI YAPMIYOR
`HumanEval → passed / timed_out / failed` ⇒ derlenen ama yanlış kod **kategorik olarak "failed"**
`"syntactically valid but wrong" → AYRI ETİKET YOK`
`SWE-bench → "spec/issue uyumu" ile "test geçme" arasında README düzeyinde AÇIK AYRIM YAPILMIYOR`
⇒ **Aynı boşluk hem kod üretiminde hem kod onarımında.**

**L11** ⊨D `[kısmi]` — EvalPlus BOŞLUĞU ÖLÇÜYOR
`HumanEval+ → 80×` ∧ `MBPP+ → 35×` daha fazla test
Kendi ifadesi: *"bigger drop means the generated code tends to be fragile"*
⇒ **`test_geçme_oranı ↔ gerçek_semantik_doğruluk` arasında ÖLÇÜLMÜŞ bir boşluk VAR**
⚠️ `tam pass@1 fark rakamı` → leaderboard `github.io`'da ∧ **erişilemedi** ⇒ `[?]`

### 2.3 ▲ Literatürün ölçtüğü şey, aradığımız şey değil

**L12** ⊨D — ⭐ AYRIMIN KENDİSİ BİR BULGUDUR
`DeepSeek-Prover-V1.5 → miniF2F-test %63,5 · ProofNet %25,3`
⚠️ Bunlar **zaten biçimselleştirilmiş problemler üzerinde KANIT ÜRETME** başarısıdır.
**`autoformalization (NL → formal çeviri) doğruluğunu ÖLÇMÜYOR`** — farklı bir aşamayı ölçüyor.
⇒ **Literatürün büyük kısmı *"formalize edilmiş problemi kanıtlama"* başarısını ölçüyor, *"doğal dili doğru formalize etme"* başarısını DEĞİL.**
⇒ Bizim sorumuz (`önerme → kod`) tam olarak **ölçülmeyen aşamadır.**

**L13** ⊨D `[kapsam var, rakam yok]`
`MiniF2F → 244 problem` (olimpiyat seviyesi, Lean/Isabelle/HOL Light/Metamath) ∧ `README → doğruluk/hata oranı = ∅`
`LogicBench → 25 akıl_yürütme_paterni` (önermeler/birinci-derece/monoton-olmayan; negation ∧ De Morgan ∧ koşullu **dahil**) ∧ `kategori_bazlı_sayısal_tablo = ∅`
`FOLIO → premises/premises-FOL/conclusion/conclusion-FOL yapısı doğrulandı` ∧ `negation/quantifier/De Morgan hata kırılımı = ∅`
⇒ **Üç benchmark da kapsamı TANIMLIYOR, rakamı VERMİYOR.**

**L14** `[K]` ∧ `[X]` — NİCELEYİCİ VE OLUMSUZLAMA
`ReFACT: GPT-4 negation_localization → %66 doğruluk / 0,57 IoU` — entity localization'dan **belirgin yüksek**
⇒ *"Olumsuzluk sözdizimsel olarak yakalanması daha kolay; derin anlamsal ikame daha zor."*
⚠️ Bu, **negation-VARLIĞI tespitidir**, `quantifier scope` ∨ `De Morgan` ∨ `conditional inversion` DEĞİL.
`"Probing Quantifier Comprehension… Another Example of Inverse Scaling"` ⇒ başlık **daha büyük modellerin niceleyici anlamada DAHA KÖTÜ olabileceğini** iddia ediyor
⚠️ **İçeriğe erişilemedi** ⇒ `[X]`, başlık düzeyinde.

### 2.4 ⭐⭐ ÖLÇÜLMEMİŞ OLANIN KENDİSİ BULGU

**L15** — HİÇBİR ÖLÇÜM YOK, ÜÇ EKSENDE

| Eksen | Durum |
|---|---|
| **`[?]` ∧ `⊨X` etiketlerinin koda taşınma davranışı** | **HİÇBİR çalışma bulunamadı.** *Arandı, alan boş.* ⇒ **L21** |
| Autoformalization'da *"sessizce yanlış ama derlenen"* çeviri **oranı** | Hiçbir kaynakta rakam yok — yalnız riskin var olduğu **VARSAYIMI** (benchmark tasarımlarının kendisi bunu ima ediyor) |
| Materyal koşullu ↔ gündelik "eğer" karışıklığının **kod bağlamında** ölçümü | **Hiç bulunamadı** |
| De Morgan hatası özelinde ayrı ölçüm | **Hiç bulunamadı** |

**L16** `[metodoloji var, rakam yok]` — MADDE ATLAMA
`IFEval → strict/loose accuracy metodolojisi VAR` ∧ `sayısal tablo → çekilemedi (404 + kapalı kanallar)`
`BigCodeBench → "complex instructions" ölçüyor` ∧ `kısıt-bazlı atlama tablosu README'de yok`
⇒ **Çok maddeli spec'te kaç maddenin sessizce atlandığı — metodoloji mevcut, RAKAM YOK.**

### 2.5 LLM ÇEVİRİ BAŞARISIZLIK MODLARI

| Başarısızlık modu | Nasıl görünür | Ölçülmüş mü | Panzehir |
|---|---|---|---|
| **Sessizce yanlış ama sözdizimsel geçerli çeviri** | Lean/FOL çıktısı parse olur, **anlam kayar** | Fenomen kabul görüyor; **kesin oran bulunamadı** ⇒ `[K]` dolaylı | Round-trip (formal→NL geri çeviri + karşılaştırma); SMT/tip kontrolcüsü |
| **Test geçiyor, spec'i karşılamıyor** | `pass@1` yüksek, edge-case'lerde çöküyor | **ÖLÇÜLMÜŞ ⊨D** (L11) | PBT üretimi; **zayıf test setine güvenme** |
| **`A→B` → `B→A` ters çevirme** | Spesifikasyonun **tersini** uygulayan kod | Kategori **tanımlı** (L13), sayısal tablo **yok** | İkinci modelle çapraz denetim; spec'i doğal dile geri çevirip **insana onaylatma** |
| **Niceleyici sırası `∀∃` / `∃∀`** | *"her x için bir y"* ile *"öyle bir y ki her x"* karışır | Yalnız **başlık düzeyinde** iddia (L14) | SMT/model checker ile **karşı-örnek arama** |
| **Materyal koşullu ↔ gündelik "eğer"** | Boş öncüllü (vacuous) durumlar yanlış işlenir | **Bulunamadı** | Vacuous-truth durumlarını **ayrıca test et** |
| **Madde atlama** | N maddeden bazıları **sessizce** uygulanmıyor | Metodoloji var, rakam yok (L16) | Maddeleri **numaralandır** ∧ LLM'e checklist olarak **geri doğrulat**; her maddeyi **ayrı test case'e** bağla |
| **⭐ Belirsizlik etiketinin sessizce kesinliğe dönüşmesi** | Spec'te `[?]`, kodda **hardcoded kesinlik** | **HİÇ ÖLÇÜM YOK** (L15) | Etiketleri **tip sistemine taşı** (`Option`/`Result`); post-hoc **spec-kod diff'i** |
| **Aynı aktörün test+kod yazması** | Testler *"spec'i doğrulamak"* yerine **"üretilen kodu geçirmek"** için yazılır | **ÖLÇÜLMÜŞ: %32,67 çözüm sızıntısı** *(oturum-içi veri, kod-entegrasyonu raporu §3.3)* | Test yazımını **ayrı ajana/tura** ver; spec'ten bağımsız **üçüncü taraf** test üretimi |

### 2.6 ⭐ GÜVENCE SIRALAMASI — hangisi işe yarıyor, hangisi tiyatro

*Maliyet artan sırayla; "ölçülmüş mü" işaretli.*

| # | Güvence | Ölçülmüş mü | Maliyet |
|---|---|---|---|
| **1** | **Tip sistemi / biçimsel kısıt (SMT, model checker, Dafny-tarzı)** | ⭐ **EN GÜÇLÜ ölçülmüş kanıt** — Clover `%87 kabul + SIFIR yanlış-pozitif` ⊨D (L7); tip-kısıtlı decoding ⊨K (L8) | **Yüksek** (biçimsel dil/araç kurulumu) |
| **2** | **Genişletilmiş / property-based test seti** | ⊨D `[kısmi]` — zayıf testte yüksek skor, zengin testte düşüş (L11) | Orta — **üreten ayrı olmalı** |
| **3** | **İkinci modelle denetim / ayrı aktör test üretimi** | **Dolaylı**: aynı-aktör sızıntısı (%32,67) **tam tersini** destekliyor ⇒ ayrıştırma **negatif kanıtla** gösteriliyor. Doğrudan *"ayrı model test yazınca X azaldı"* ölçümü **bulunamadı** | Orta-yüksek |
| **4** | **Statik analiz geri-besleme döngüsü** | ⊨K, birincil doğrulanamadı (L9) | **Düşük-orta** — mevcut linter'lar yeterli |
| **5** | **LLM'e testleri de yazdırmak (AYNI aktör)** | ⚠️ **KISMEN TİYATRO** — %32,67 sızıntı, güvence değerini sınırlıyor | Düşük ama **güvenilirliği düşük** |
| **6** | **Round-trip / back-translation** | Kavramsal olarak mantıklı ∧ **doğrudan ölçülmüş etkinlik kanıtı bulunamadı** ⇒ `[?]` | Orta |
| **7** | **"Prompt'a daha fazla biçimsellik ekle" (araç yok)** | ⚠️ **EN ZAYIF** — hiçbir kaynak tek başına yeterli olduğunu göstermiyor. MiniF2F/FOLIO gibi tasarımların **TÜMÜ**, salt-metin disiplininin yetmediğini varsayarak **biçimsel araç katmanı ekliyor** | En düşük, **kanıt da en zayıf** |

> **▲ 7. satır doğrudan bize bakıyor.** Salih'in önerme formu **salt-metin disiplinidir.** Bu literatürün tamamı, salt-metin disiplininin **tek başına yetmediğini varsayarak** üzerine araç katmanı ekliyor.
> ⇒ **Önerme formu gerekli ama yeterli değildir.** Değeri, kodun *yerine geçmesi* değil, **1. ∨ 2. sıradaki bir doğrulayıcıya BAĞLANABİLİR olmasıdır.**

**L17** ⊨X — ÇÖZÜLMEMİŞ GERİLİM
`"spec ne kadar biçimselleşirse başarı o kadar artar"` **↔** `"biçimsel DSL'ler LLM için DAHA ZOR çünkü eğitim verisi az"`
⇒ **İkisi de bu oturumda birincil doğrulanamadı** ⇒ `[X]`, çözülmedi.
⚠️ Bu gerilim, önerme formunun ne kadar biçimselleşmesi gerektiği sorusunun **tam merkezindedir** ∧ **cevapsızdır.**

### 2.7 A32 — İDDİA LİSTESİ (antitez için, gerekçesiz) ⊨¬2

① Sözdizimsel geçerlilik ile spec-uyumu arasındaki boşluk **ölçülmüş ∧ büyüktür** — ama tam sayı elde edilemedi. ② Autoformalization'da *"sessizce yanlış ama derlenen"* oranına dair **tek bir birincil rakam bulunamadı**. ③ Negation/quantifier/De Morgan hata oranlarına dair **kategori-bazlı sayısal tablo hiçbir erişilen kaynakta yoktu**. ④ Biçimsel doğrulayıcı katmak **ölçülmüş en güçlü güvencedir**. ⑤ Aynı aktörün test+kod yazması ölçülmüş sızıntı riski taşır ⇒ *"LLM'e testleri de yazdır"* güvencesini **kısmen çürütür**. ⑥ `[?]` ∧ `⊨X` etiketlerinin koda taşınma davranışına dair **HİÇBİR ölçüm yoktur** — literatür boşluğu, satıcı iddiası değil. ⑦ Madde-atlama metodolojisi **vardır** ama sayısal çıktı alınamadı — **metodoloji varlığı ile rakam erişimi ayrı şeylerdir**. ⑧ Tip/şema kısıtının hata oranını düşürdüğü iddiası **ikincil kaynaktan** gelir. ⑨ *"Spec biçimselleştikçe başarı artar"* ile *"biçimsel DSL'ler LLM için daha zor"* **çelişkilidir ∧ çözülmemiştir**.

---

## 3. SENTEZ — ÖĞRENME SIRASI (L23–L28)

*Salih'in "ne öğrenmem lazım" sorusunun cevabı. Ön koşul zinciri; her katman bir öncekinin çözemediğini çözer.*

| # | Katman | Ne çözer | Neden bu sırada |
|---|---|---|---|
| **L23** | **Üç-değerli mantık ∧ `Option`/`Maybe` tipleri** *(ön koşul: yok)* | `[?]` ile `⊨X`'in kod karşılığı. **Bu, Salih'in kendi notasyonunun doğrudan ihtiyacıdır** | En başta, çünkü **her önermesinde bu etiketler var** ∧ naif çeviri onları **birleştirip yok ediyor** (tablo §1.3) |
| **L24** | **Niceleyici kapsamı ∧ De Morgan ∧ maddi koşul** *(ön koşul: L23)* | `∀∃` sırası · `¬` dağılımı · `P→Q`'nun `¬P` dalı · converse hatası | Salih zaten bu sembolleri kullanıyor ⇒ **kullandığı sembolün kod semantiğini bilmek zorunda**. §1.3 tablosu bu katmanın özeti |
| **L25** | **Kapalı-dünya vs açık-dünya ∧ negation-as-failure** *(ön koşul: L24)* | `¬P` = *"yanlış olduğu kanıtlandı"* mı, *"bulunamadı"* mı | L24'süz ayrım **görünmez**; ve `V73` (`⊨A = aranamadı`) etiketi tam bu ayrımın **kendi notasyonumuzdaki karşılığıdır** |
| **L26** | **Design by Contract** — önkoşul/sonkoşul/değişmez *(ön koşul: L24)* | Önerme formunun **en doğrudan kod karşılığı**. Öncül → precondition, sonuç → postcondition | Önermeler zaten `öncül → sonuç` yapısında ⇒ **çeviri neredeyse birebir**. Ama L3: **runtime kontrol, dil garantisi değil** |
| **L27** | **Property-based testing** (Hypothesis) *(ön koşul: L26)* | `∀` önermelerinin **pratik** kod karşılığı + shrinking | L26 tek çağrıyı korur, L27 **girdi uzayını** tarar. Ve L4: **ispat değil, güven artışı** — bu sınır bilinerek kullanılmalı |
| **L28** | **Model checking (TLA+)** *(ön koşul: L27)* | `t / t+1` zamansal önermeleri ∧ sonlu durum uzayının **tüketici** taranması | En sonda çünkü **en pahalı ∧ en güçlü**. Ve U12 hükmü burada da geçerli: **kavramı al, üretim sistemini kurma** |

**L29** — ⭐ SIRANIN GEREKÇESİ
`L23 → L24 → L25` = **notasyonun kendi semantiği** (Salih'in zaten yazdığı şeyin ne demek olduğu)
`L26 → L27 → L28` = **doğrulama merdiveni** (artan maliyet ∧ artan epistemik güç)
⇒ İlk üçü **bugün gerekli**; son üçü **kod yazımı başlayınca** gerekli.

---

## 4. UYGULANABİLİR HÜKÜM — bugün yapılabilir

**L30** — NOTASYONA EKLENECEK ÜÇ AYRIM

| Şu anki | Sorun | Öneri |
|---|---|---|
| `[?]` (kestirim) | Koda çevrilince `None`'a düşer ∧ `⊨X` ile birleşir | Kod karşılığını **şimdiden yaz**: `Unknown` |
| `⊨X` (çelişkili) | Kod karşılığı **yok** ⇒ `else`'e düşer | Kod karşılığı: `Contradictory` — **ayrı dal, ayrı tip** |
| `¬` | Kapalı-dünya mı açık-dünya mı **belirsiz** | `V73`'ün `⊨A` etiketi bunu kısmen çözüyor: *"aranamadı"* ≠ *"yok"*. **Notasyona alınmalı** |

**L31** — ÖNERME YAZARKEN BUGÜNDEN UYGULANACAK
1. `∀`/`∃` kullanınca **sırayı açıkça numaralandır** (`∃x∀y` ≠ `∀y∃x`)
2. `→` yazınca **`⇔` olmadığını** kastediyorsan belirt (converse test edilmeyecek)
3. `t`/`t+1` içeren önermede **hangi durumun korunması gerektiğini** yaz (invariant adayı)
4. `P → Q` yazınca **`¬P` durumunda ne olduğunu** ayrıca yaz (vacuous truth dalı)

⇒ Dördü de **maliyet ≈ 0** ∧ **çeviri anında geri kazanılamaz bilgiyi** şimdi korur.

**L32** — ⭐ EN YÜKSEK GETİRİLİ TEK HAMLE
`önerme_formu` **↛** `kod` **doğrudan**
`önerme_formu` **→** `DbC sözleşmesi (öncül=precondition, sonuç=postcondition)` **→** `PBT ile ∀ taraması` **→** `kod`
⇒ Bu zincir, §2.6'nın **2. sırasındaki** güvenceye bağlanır ∧ **1. sıraya (biçimsel doğrulayıcı) kapı açar.**
⇒ Ve §2.6'nın **7. sırasında kalmaktan** (salt-metin disiplini, en zayıf) çıkarır.

---

## 5. AÇIK BORÇLAR

| # | Borç | Not |
|---|---|---|
| M1 | **Antitez (Aşama 2) koşulmadı** — A5'ten beri | §1.5 ∧ §2.7 iddia listeleri hazır |
| M2 | **AWS TLA+ raporuna erişilemedi** (L2) | Bu ailenin en çok atıf beklenen endüstriyel kanıtı |
| M3 | **Doğal dil→mantık hata oranları literatürü** `[ARANAMADI]` | Ampirik destek **şu an sıfır**; yalnız kavramsal argüman |
| M4 | `[?]`/`⊨X` koda taşınma ölçümü (L15/L21) | **Arandı, alan boş** — literatür boşluğu, erişim engeli değil |
| M5 | EvalPlus tam `pass@1` fark rakamı (L11) | Leaderboard `github.io`'da, kapalı |
| M6 | LogicBench ∧ FOLIO kategori-bazlı sayısal tablolar (L13) | Kapsam var, rakam yok |
| M7 | L17'nin çelişkisi | **Önerme formunun ne kadar biçimselleşmesi gerektiği sorusunun merkezi** ∧ cevapsız |
| M8 | SQL NULL · Prolog `\+` · Eiffel/JML birincil kaynakları | Hepsi kapalıydı ⇒ §1.3'ün ilgili satırları **kavramsal**, birincil-kaynaklı değil |

---

## 6. FİKİR KUTUSU ADAYLARI

- **V76 — ⭐ Notasyona kod-karşılığı sütunu.** `2026-07-26-LOJIK-onerme-formu.md` §Notasyon tablosuna **üçüncü sütun**: her sembolün **kod karşılığı**. `[?] → Unknown` · `⊨X → Contradictory` · `∀ → PBT` · `→ → precondition/postcondition`. Maliyet: bir tablo sütunu. Getiri: **çeviri anında kaybolacak bilginin şimdiden sabitlenmesi.**
- **V77 — Önerme → DbC şablonu.** L32'nin zinciri bir skill'e dönüşebilir: önermeyi al, `icontract` sözleşmesine çevir, `Hypothesis` özelliği üret. **Ölçülmüş güvence merdiveninin 2. basamağına** doğrudan bağlanır.
- **V78 — `⊨A` (aranamadı) etiketi.** V73 ile aynı öneri, buradan **ikinci kez** ve **farklı gerekçeyle** geliyor: L25'te açık-dünya/kapalı-dünya ayrımının notasyondaki karşılığı. **İki bağımsız aile aynı eksiği işaret etti** ⇒ güçlenmiş aday.
- **V79 — Kendi boşluğumuzu doldurmak (V65'in ikizi).** M4: `[?]`/`⊨X`'in koda taşınması **literatürde ölçülmemiş**. JARVIS'te bu **ölçülebilir**: önerme yaz → koda çevirt → etiketin korunup korunmadığını say. `n=1` ama **ölçülmüş** n=1, ve alan **boş**.

---

## 7. KAPANIŞ DAMGASI

**Aile:** A31 ⊨¬2 · A32 ⊨¬2
**Kanıt tabanı:** `[D]` — TLA+ Examples · icontract · Hypothesis · QuickCheck · fast-check · npm registry · Clover · HumanEval · EvalPlus · MiniF2F · LogicBench · FOLIO · DeepSeek-Prover · SWE-bench depoları
**En güçlü tek bulgu:** Clover — biçimsel doğrulayıcı, `%87 kabul + sıfır yanlış-pozitif` (L7)
**En değerli boşluk:** `[?]`/`⊨X` koda taşınma ölçümü **yok** (L15) — Salih'in doldurabileceği alan
**Ana hüküm:** `önerme_formu = gerekli ∧ ¬yeterli`; değeri **doğrulayıcıya BAĞLANABİLİR olmasıdır** (§2.6)

**▲ Bu raporun kendi zayıflıkları — beyan edilir:**
1. `antitez = ∅`
2. §1.3'ün **ampirik desteği sıfırdır** (M3) — tablo **kavramsal argümandır**, ölçüm değil. Değerli ama **kanıt sınıfı farklıdır.**
3. `L2` ⇒ en çok atıf beklenen endüstriyel kanıt **doğrulanamadı**; A31'in sanayi ayağı `[K-hatırlama]` düzeyindedir.
4. `L17` ⇒ **"ne kadar biçimsel"** sorusu, bu raporun cevaplaması beklenen sorulardan biriydi ∧ **cevaplanamadı.**
