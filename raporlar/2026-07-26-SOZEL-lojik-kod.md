# Lojik Dil → Kod Dil Dönüşümü — sözel önerme karşılığı

> Kaynak: `raporlar/2026-07-26-lojik-kod-atlas.md` · Register: düz lojik · Compiler: **KAPALI**
> Okuma kuralı: **öncülü sağlanmayan bir önermenin sonucu geçerli DEĞİLDİR.**

**Numaralandırma:** kaynağın kendi kodları korunur (`L1`–`L32`). Bölüm önermeleri `§1.3-1` gibi adreslenir.

**Kanıt sütunu:** *birincil* = birincil kaynağa/depoya inildi · *ikincil* = birincil metinden doğrulanmadı · *çelişkili* = hüküm yok · *kestirim* = ölçülmemiş · *çıkarım* = kavramsal argüman, ölçüm değil · *aranamadı* = erişim/bütçe engeli, **yokluk kanıtı DEĞİL**.

**Antitez sütunu:** bu ailenin antitezi **araç kullanarak** koştu (21 araç çağrısı: Rust RFC, CBMC, SPARK, pyrsistent, icontract, Hypothesis, LogicBench, RuleTaker, FOLIO, miniF2F, IFEval, zod depoları). Depo-doğrulamalı *"sağ çıktı"* damgaları **aynı-aile şerhinden muaftır**; diğerleri değildir.

---

## 0. Ailenin tek cümlelik bulgusu

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§0.1** | Önerme formundan koda geçerken kaybolan şey **önermenin kendisi değil, önermenin kipidir**.<br>`∀` sonlu bir örnekleme çöker; `→` tek bir dala çöker; `¬` *"bulunamadı"*ya çöker; `[?]` ile `⊨X` tek bir `None`'a çöker.<br>Her çöküş **sessizdir**: kod derlenir, test geçer, hata fırlatmaz. | çıkarım | çürütülemedi |
| **§0.2** | Bir spec'teki belirsizlik etiketlerinin **bir LLM tarafından** koda nasıl taşındığına dair literatürde **hiçbir ölçüm yoktur**.<br>Bu bir erişim engeli değildir — **arandı, alan boştur**. Boşluğun kendisi bir bulgudur ve doldurulabilir bir yerdir.<br>⚠️ **Kapsam dar tutulur:** ölçülmemiş olan **LLM'in davranışıdır**. Belirsizlik ile hata ayrımının **koda taşınması** 40+ yıllık literatürdür — Option/Maybe monadları, Rust'ta `Option` ile `Result`, SQL'in üç değerli mantığı. Geniş okuma **yanlıştır**. | çıkarım | kısmen çürütüldü → K31: dar okumaya sabitlendi |

---

## 1. A31 — İnsan tarafı: biçimsel spec → kod

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **L1** | TLA+ üretim sistemlerinde **fiilen kullanılmıştır**: MongoDB'nin Raft'ının basitleştirilmiş parçası, WeChat/Tencent PaxosStore (VLDB 2017), Azure Cosmos DB tutarlılık modelleri, Voldemort dağıtık key-value store.<br>⚠️ Depo metninde spec ile implementasyon arasındaki boşluk hakkında **hiçbir açık ifade yoktur**; yalnızca *"spesifikasyonların bir derlemesi"* deniyor.<br>Sonuç: **benimseme kanıtı vardır**; *"ne yakaladı, ne yakalamadı"* kanıtı **yoktur**. | birincil | çürütülemedi |
| **L2** | AWS biçimsel yöntemler raporunun (CACM 2015) **birincil metnine erişilemedi**.<br>Ajanın kendi beyanı: hatırladığı iddialar — TLA+'ın testle aylar sürecek ince eşzamanlılık hatalarını bulduğu ve makalenin *"spesifikasyon uygulama değildir"* sınırını **açıkça kabul ettiği** — birincil olarak **sunulmadı** ve **rakam verilmedi**.<br>Sonuç: bu ailenin **en çok atıf beklenen endüstriyel kanıtı doğrulanamadı** ⇒ bu eksene dayanan her iddia en fazla **hatırlama düzeyindedir** ve bağımsız doğrulama gerektirir. | aranamadı | çürütülemedi |
| **L3** | `icontract` önkoşul, sonkoşul ve değişmez sunar; sözleşme kalıtımı Liskov kurallarına uyar (önkoşul zayıflatma, sonkoşul ve değişmez güçlendirme).<br>Kütüphanenin **kendi konumlandırması**: *"Python'a DbC entegre edilene kadar bir geçici çözüm."*<br>Sonuç: garanti **çalışma zamanı kontrolüdür**, dil düzeyinde garanti **değildir** — ve kütüphane bunu **kendisi itiraf ediyor**.<br>⚠️ **Kapsam daraltıldı:** *"DbC kütüphane düzeyindedir"* hükmü yalnız **Python, Java ve JS decorator ekosistemi** için doğrudur. **SPARK** kendini *"bir programlama dili, bir doğrulama araç seti ve bir tasarım yöntemi"* olarak tanımlar; Eiffel de aynı sınıftadır ⇒ **dil düzeyinde DbC gerçekten vardır**. icontract hakkındaki hüküm değişmez; değişen, hükmün **evrensel sanılmasıydı**. | birincil | daraltıldı → K28 |
| **L4** | QuickCheck, özelliklerin *"çok sayıda rastgele üretilmiş durumda geçerli olduğunu **test eder**"*.<br>Sonuç: bu, **sonlu örneklem üzerinde tutarlılıktır**; evrensel `∀` **ispatı değildir**.<br>`fast-check`in kendi konumlandırması: *"neyin bozulmaması gerektiğini değil, her zaman ne doğru kalması gerektiğini tarif edersiniz."* | birincil | sağ çıktı ⭐ — Hypothesis'in kendi tanımıyla doğrulandı; **bu turun en sağlam duran iddiası** |
| **L5** | Hypothesis bir hata bulduğunda **rastgele herhangi bir başarısız durumu değil, en basit olanı raporlar** (shrinking).<br>Somut örnek: `sorted(set(ls))` yanlışlıkla tekrarları sildiğinde en minimal karşı örnek `[0, 0]`'dır.<br>Sonuç: değer yalnız hata bulmak değil, **hatayı okunabilir kılmaktır**. | birincil | çürütülemedi |
| **L6** | npm'deki scope'suz `cucumber` paketi **deprecated**'dır; geliştirme `@cucumber/cucumber` altına taşınmıştır.<br>⚠️ Bu, aracın **terk edildiği anlamına gelmez** — paketleme düzeyinde bir süreklilik izidir. **Zayıf kanıt olarak damgalanır** (tek gösterge, kullanım verisi yok). | birincil | çürütülemedi |

### §1.3 — Lojik → kod çeviri tuzakları

*Bu tablo ailenin ana katkısıdır. **Ampirik desteği sıfırdır** (bkz. M3): kavramsal argümandır, ölçüm değildir.*

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§1.3-1** | `P → Q` biçimindeki maddi koşul `if P: assert Q` diye yazılırsa: maddi koşulda `¬P` iken önerme **otomatik doğru** sayılır (vacuous truth) ve kod bunu es geçer ⇒ **`¬P` dalı sessizce doğrulanmamış kalır**.<br>Doğrusu: `¬P` dalı da açıkça test edilir; `P→Q` ile `P⇔Q` farkı yorumda belirtilir. | çıkarım | çürütülemedi |
| **§1.3-2** | `∀x. P(x)` bir döngüyle test edilirse kod yalnız **eldeki örneklem** üzerinde çalışır; sonlu örneklem `∀`'nın **ispatı değildir**.<br>Doğrusu: property-based test ve shrinking **güven artışı** sağlar, tam ispat değil. Model checking sonlu durum uzayını **tüketici** tarar ⇒ epistemik olarak daha güçlüdür — **ama koşulsuz değil** (bkz. §1.5-4). | çıkarım | daraltıldı → K30 |
| **§1.3-3** | `∃x. P(x)` yazılırken kapsam belirsizse — *"bir X vardır ki her Y için"* mi, *"her Y için bir X vardır"* mı — kod **sessizce yanlış sırayı seçer** ve hata fırlatmaz.<br>Doğrusu: niceleyici sırası önerme yazılırken **açıkça numaralandırılır**; `∃x∀y` ile `∀y∃x` **farklı matematiksel nesnelerdir**; kod yorumunda sıra birebir korunur. | çıkarım | çürütülemedi |
| **§1.3-4** | `¬(A ∧ B)` elle yazılırken De Morgan atlanır: doğrusu `¬A ∨ ¬B`'dir, **`¬A ∧ ¬B` değildir**. Bu klasik ve yaygın bir hatadır.<br>Doğrusu: dönüşüm **programatik uygulanır**, elle yeniden türetilmez. | çıkarım | çürütülemedi |
| **§1.3-5** | `[?]` (kestirim) `None` ya da `null` ile temsil edilirse: `None` **üç değerli mantığı gizlice ikiye indirger**, ve *"bilinmiyor"*, *"boş"*, *"hata"* **aynı değerle** temsil edilir ⇒ hangisi olduğu **kaybolur**.<br>Ayrıca diller arasında tutarsızdır: SQL'de `NULL = NULL` sonucu `UNKNOWN`'dır, Python'da `None == None` sonucu `True`'dur.<br>⚠️ **Bu kayıp kaçınılmaz DEĞİLDİR** — bir tasarım tercihinin sonucudur. Rust RFC 0243: `Option<T>` ile `Result<T,E>` yapısal olarak eşdeğerdir ama **farklı semantik amaçlarla** kullanılır ⇒ ayrım **hiç kaybolmadan** taşınabilir.<br>Doğrusu: `Option`/`Maybe` tipi veya açık üç durumlu enum — `Known(x)`, `Unknown`, `Contradictory`. Kayıp kaçınılmaz olmadığı için **kaçınmak bir karardır**. | çıkarım | daraltıldı → K29 (*"geri alınamaz"* düştü) |
| **§1.3-6** | `⊨X` (çelişkili) için genelde **kod karşılığı yazılmaz, atlanır**. Çelişkili durumun kendi tipi ya da dalı yoksa, çelişkili girdi **sessizce ilk eşleşen dala düşer** (genelde `else`) ⇒ çelişki bilgisi kaybolur.<br>Doğrusu: ayrı bir `Contradiction` durumu ya da exception tipi. **`⊨X` asla `[?]` ile aynı koda düşmemelidir.** | çıkarım | çürütülemedi |
| **§1.3-7** | Kapalı dünya `¬`'si (*"X yoksa Y'dir"*) `if not found_in_db(x)` diye yazılırsa: mantıkta `¬P`, **P'nin yanlışlığının kanıtlanmış olmasıdır**; kodda `not found` ise *"arandı, bulunamadı"*dır ⇒ **kanıtlanmamış yokluk ile kanıtlanmış yokluk karışır**.<br>Prolog'un `\+` operatörü de klasik değildir: *"şu an ispatlanamıyor"* der, *"yanlıştır"* demez.<br>Doğrusu: açık dünya varsayımı gerekiyorsa arama uzayının **tam** olduğu ayrıca garanti edilir; değilse *"bulunamadı"* ile *"yoktur"* **kod seviyesinde ayrı durumlar** yapılır. | çıkarım | çürütülemedi |
| **§1.3-8** | `→` ile `⇔` ikisi de `if...then` diye yazılırsa ters yön hiç test edilmez ve `A→B` doğrulanınca `B→A` da doğru **varsayılır** (converse hatası).<br>Doğrusu: her `⇔` **hem ileri hem geri** yön testi ister; `→` tek yöndür ve tersi **test edilmez**. | çıkarım | çürütülemedi |
| **§1.3-9** | `t` ve `t+1` zamansal indeksleri mutasyonla (`state = new_state`) yazılırsa: bu ikisi matematiksel olarak **iki ayrı, değişmez durumdur** ve üzerine yazılınca `t` **kaybolur** ⇒ *"t ile t+1 arasında X değişmemeli"* tipi invariant **kontrol edilemez hâle gelir**.<br>⚠️ **"İmkânsız" DEĞİL.** `pyrsistent`in kendi tanımı: *"normalde onu değiştirecek tüm metotlar bunun yerine yeni bir kopya döndürür… orijinal yapıya dokunulmaz."* Event sourcing de aynı işi görür ⇒ invariant **korunur**.<br>Doğrusu: TLA+ tam bunun için vardır (primed variables — eski ve yeni durumu **aynı ifadede** tutar). Kodda: immutable snapshot artı açık diff/invariant kontrol fonksiyonu.<br>Bu düzeltme *"doğrusu"* sütununu **güçlendirir**: çözüm zaten oradaydı, fazla mutlak olan **iddia metniydi**. | çıkarım | ⛔ çürütüldü → K27 |
| **§1.3-10** | Yumuşatıcısız kesin bir önerme `assert` ya da `raise` ile yazılırsa: spec **bütün uzay** için doğrudur, kod ise **yalnız test edilen uzay** için doğrulanmış olabilir (refinement gap).<br>Doğrusu: kod yorumuna üst not düşülür — *"bu invariant spec'te model-checked, implementasyonda yalnızca test edilmiştir."* | çıkarım | çürütülemedi |
| **§1.3-11** | Salih'in önerme formu için en kritik üç satır `[?]`, `⊨X` ve `t/t+1`'dir.<br>İlk ikisi **onun kendi notasyonunun ayırt ettiği** ama kodun varsayılan olarak **birleştirdiği** ayrımlardır.<br>Üçüncüsü, `durum-kapsulu.md` gibi *"üzerine yazılır"* dosyalarının kod karşılığında **doğrudan bir tuzaktır**. | çıkarım | çürütülemedi |

### §1.5 — A31 iddia listesi (antitez koştu, hükümler işlendi)

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§1.5-1** | `[?]` ile `⊨X` tek bir `None`'a indirgenirse epistemik olarak farklı iki durum birleşir.<br>⚠️ *"Geri alınamaz biçimde"* ifadesi **düşer**: kayıp bir doğa yasası değil, **bir tasarım tercihinin sonucudur**.<br>Ve bu, iddianın **pratik değerini artırır**: kayıp kaçınılmaz değilse, kaçınmak bir **karardır**. | çıkarım | daraltıldı → K29 |
| **§1.5-2** | `P→Q` yalnız `P` doğruyken test edilirse, `¬P` durumu **hiç doğrulanmamış** gizli bir kör nokta yaratır. | çıkarım | çürütülemedi |
| **§1.5-3** | Property-based testing `∀`'nın **ispatını değil, güven artışını** sağlar; bu epistemik zayıflama belirtilmezse *"test edildi"* ile *"ispatlandı"* karışır. | birincil | sağ çıktı ⭐ (depo-doğrulamalı, şerhten muaf) |
| **§1.5-4** | Model checking, property-based testing'den epistemik olarak daha güçlüdür ama **yalnız spec üzerinde çalışır** — kodun spec'e uyduğu ayrı ve genelde doğrulanmamış bir iddiadır.<br>⛔ **Kısmen çürütüldü.** **CBMC**, *"C ve C++ **programları** için bir Bounded Model Checker'dır"* ⇒ soyut spec değil, **doğrudan kodu** doğrular.<br>Ve ikinci nokta daha derindir: CBMC **bounded**'dır (döngüleri sınırlı açar) ⇒ *"epistemik olarak daha güçlü"* **koşulsuz değildir**; property-based testing ile **aynı sınıf açık uçluluğu** paylaşır. Fark **niceliktir** (tüketici tarama ile rastgele tarama), **nitelik değildir**. | birincil | ⛔ kısmen çürütüldü → K30 |
| **§1.5-5** | DbC kütüphaneleri dil seviyesinde değil kütüphane seviyesinde konumlanır; bu, *"spec'i kodda garantiledik"* **yanılsamasına** yol açabilir.<br>⚠️ Kapsam **Python/Java/JS decorator ekosistemine** daraltılır; SPARK ve Eiffel dil düzeyinde DbC sunar. | birincil | daraltıldı → K28 |
| **§1.5-6** | Negation-as-failure klasik olumsuzlamadan **ontolojik olarak farklıdır**; önerme formunda `¬` kullanılan her yerin açık dünya mı kapalı dünya mı olduğu **belirsiz kalabilir**. | çıkarım | çürütülemedi |
| **§1.5-7** | Zamansal indeksli önermeler mutasyonla ifade edilirse invariant kontrolü **naif mutasyon temelli stilde kaybolur**; kalıcı/immutable veri yapıları ya da event sourcing ile **korunur**.<br>⚠️ Eski hâli *"imkânsız hâle gelir"* diyordu ⇒ **çürütüldü**. | çıkarım | ⛔ çürütüldü → K27 |
| **§1.5-8** | Bu araştırmada en sık atıf yapılan endüstriyel kanıta **erişilemedi**; bu eksene dayanan her iddia en fazla **hatırlama düzeyindedir**. | aranamadı | çürütülemedi |
| **§1.5-9** | Doğal dil→mantık tuzaklarının **ölçülmüş hata oranlarına hiç erişilemedi**; bu eksenin ampirik desteği **şu an sıfırdır**.<br>⚠️ Bu bir **"aranamadı"** kaydıdır, yokluk hükmü **değildir**. | aranamadı | çürütülemedi |

---

## 2. A32 — LLM tarafı: model aracılı çeviri

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **L7** | Clover sistemi kod, docstring ve biçimsel ek açıklama üçlüsü arasında tutarlılık kontrolü yapar.<br>Doğru kodda kabul oranı yaklaşık **%87**'dir. Yanlış kodda **ölçülen yanlış pozitif sayısı sıfırdır**.<br>Ölçüm ortamı: CloverBench, Dafny, **ders kitabı seviyesi** problemler.<br>Sonuç: *"ikinci bir **biçimsel** doğrulayıcıyla kontrol"* güvencesinin doğrudan ölçülmüş örneğidir ve **bu ailenin en güçlü tek kanıtıdır**. | birincil | çürütülemedi |
| **L8** | Tip kısıtlı decoding derleme hatalarını **yarıdan fazla** düşürür, işlevsel doğruluğu göreceli olarak **%3,5 ile %5,5** artırır ve derlenmeyen kodun onarımını göreceli ortalama **%37** artırır.<br>⚠️ Birincil kaynağa **erişilemedi** ⇒ rakamlar doğrulanana kadar temkinli kullanılır. | ikincil | çürütülemedi |
| **L9** | Linter ile iteratif prompting (10 iterasyon) sonucunda güvenlik uyarıları %40'ın üzerinden **%13'e**, okunabilirlik %80'in üzerinden **%11'e**, güvenilirlik %50'nin üzerinden **%11'e** iner.<br>⚠️ Birincil kaynağa erişilemedi. | ikincil | çürütülemedi |
| **L10** | HumanEval sonuçları `passed`, `timed_out` ve `failed` olarak etiketler ⇒ **derlenen ama yanlış** kod kategorik olarak *"failed"*tır.<br>*"Sözdizimsel geçerli ama yanlış"* için **ayrı bir etiket yoktur**.<br>SWE-bench de *"spec/issue uyumu"* ile *"test geçme"* arasında README düzeyinde **açık ayrım yapmaz**.<br>Sonuç: aynı boşluk hem kod üretiminde hem kod onarımındadır. | birincil | çürütülemedi |
| **L11** | EvalPlus boşluğu ölçer: HumanEval+ **80 kat**, MBPP+ **35 kat** daha fazla test içerir.<br>Kendi ifadesi: *"daha büyük düşüş, üretilen kodun kırılgan olma eğiliminde olduğu anlamına gelir."*<br>Sonuç: test geçme oranı ile gerçek semantik doğruluk arasında **ölçülmüş bir boşluk vardır**.<br>⚠️ Tam `pass@1` fark rakamı leaderboard'dadır ve **erişilemedi** ⇒ kestirim. | birincil (rakam: kestirim) | çürütülemedi |
| **L12** | DeepSeek-Prover-V1.5 miniF2F-test'te %63,5, ProofNet'te %25,3 alır.<br>⚠️ Bunlar **zaten biçimselleştirilmiş** problemler üzerinde **kanıt üretme** başarısıdır; **autoformalization (doğal dilden biçimsel dile çeviri) doğruluğunu ÖLÇMEZ** — farklı bir aşamayı ölçer.<br>Sonuç: literatürün büyük kısmı *"formalize edilmiş problemi kanıtlama"* başarısını ölçüyor, *"doğal dili doğru formalize etme"* başarısını **değil**.<br>Sonuç: bizim sorumuz (önerme → kod) **tam olarak ölçülmeyen aşamadır**. | birincil | çürütülemedi |
| **L13** | MiniF2F 244 problem tanımlar (olimpiyat seviyesi; Lean, Isabelle, HOL Light, Metamath) ve README'sinde doğruluk/hata oranı **yoktur**.<br>LogicBench 25 akıl yürütme paterni tanımlar (önermeler, birinci derece, monoton olmayan; **olumsuzlama, De Morgan ve koşullu dahil**) ve kategori bazlı sayısal tablosu **yoktur**.<br>FOLIO'nun premises / premises-FOL / conclusion / conclusion-FOL yapısı doğrulandı; olumsuzlama, niceleyici ve De Morgan hata kırılımı **yoktur**.<br>Sonuç: üç benchmark da **kapsamı tanımlar, rakamı vermez**. | birincil | sağ çıktı ⭐ — üç depo yeniden tarandı, karşı örnek çıkmadı ⇒ **en dirençli yokluk iddiası** |
| **L14** | ReFACT ölçümünde GPT-4'ün olumsuzlama yerelleştirmesi **%66 doğruluk / 0,57 IoU**'dur ve entity localization'dan **belirgin biçimde yüksektir** ⇒ *"olumsuzluk sözdizimsel olarak yakalanması daha kolay; derin anlamsal ikame daha zor."*<br>⚠️ Bu, **olumsuzluğun varlığını tespit** etmektir; **niceleyici kapsamı**, **De Morgan** ya da **koşul ters çevirme** değildir.<br>*"Probing Quantifier Comprehension… Another Example of Inverse Scaling"* başlıklı çalışma, **daha büyük modellerin niceleyici anlamada daha kötü olabileceğini** iddia eder.<br>⚠️ **İçeriğe erişilemedi** ⇒ yalnız başlık düzeyinde bilgidir. | ikincil ∧ çelişkili | çürütülemedi |
| **L15** | Üç eksende **hiçbir ölçüm yoktur**.<br>Birincisi: bir LLM'in `[?]` ve `⊨X` etiketlerini koda taşıma **davranışı** — hiçbir çalışma bulunamadı, arandı ve alan boş.<br>İkincisi: autoformalization'da *"sessizce yanlış ama derlenen"* çeviri **oranı** — hiçbir kaynakta rakam yok, yalnız riskin var olduğu **varsayımı** (benchmark tasarımlarının kendisi bunu ima ediyor).<br>Üçüncüsü: maddi koşul ile gündelik *"eğer"* karışıklığının **kod bağlamında** ölçümü — hiç bulunamadı. De Morgan hatası özelinde ayrı ölçüm de **hiç bulunamadı**.<br>⚠️ Birincinin kapsamı **dar okumaya sabitlenmiştir** (bkz. §0.2). | çıkarım | kısmen çürütüldü → K31 |
| **L16** | IFEval'in strict/loose accuracy **metodolojisi vardır**; sayısal tablosu **çekilemedi** (404 ve kapalı kanallar).<br>BigCodeBench *"karmaşık talimatlar"* ölçer; kısıt bazlı atlama tablosu README'de **yoktur**.<br>Sonuç: çok maddeli bir spec'te kaç maddenin sessizce atlandığı — **metodoloji mevcuttur, rakam yoktur**. | birincil | sağ çıktı — IFEval bunu **birebir doğruladı** |
| **L17** | *"Spec ne kadar biçimselleşirse başarı o kadar artar"* ile *"biçimsel diller LLM için daha zordur çünkü eğitim verisi azdır"* önermelerinin **ikisi de bu oturumda birincil doğrulanamadı**.<br>⚠️ **Bunlar çelişki DEĞİLDİR.** Muhtemelen **ters-U şeklinde, tekdüze olmayan** bir ilişkidir: az biçimsellik belirsizlik kaybettirir; çok biçimsellik dağılım dışı sözdizimi kaybettirir; **ortada bir optimum vardır**.<br>Sonuç: soru **cevaplanmadı ama değişti** — *"hangisi doğru"* cevaplanamaz bir soruydu; **"optimum nerede"** ölçülebilir bir sorudur.<br>Bu gerilim, önerme formunun ne kadar biçimselleşmesi gerektiği sorusunun **tam merkezindedir** ve **hâlâ cevapsızdır**. | kestirim | çerçeve değişti → K32 (`⊨X` → `[?]`) |

### §2.5 — LLM çeviri başarısızlık modları

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§2.5-1** | **Sessizce yanlış ama sözdizimsel geçerli çeviri:** Lean ya da FOL çıktısı parse olur, **anlam kayar**. Fenomen kabul görüyor, **kesin oran bulunamadı**.<br>Panzehir: round-trip (biçimselden doğal dile geri çeviri ve karşılaştırma); SMT ya da tip kontrolcüsü. | ikincil (dolaylı) | çürütülemedi |
| **§2.5-2** | **Test geçiyor, spec'i karşılamıyor:** `pass@1` yüksektir, edge-case'lerde çöker. **Ölçülmüştür** (L11).<br>Panzehir: property-based test üretimi; **zayıf test setine güvenme**. | birincil | çürütülemedi |
| **§2.5-3** | **`A→B`'yi `B→A` diye ters çevirme:** spesifikasyonun **tersini** uygulayan kod. Kategori tanımlıdır, sayısal tablo **yoktur**.<br>Panzehir: ikinci modelle çapraz denetim; spec'i doğal dile geri çevirip **insana onaylatma**. | birincil (kategori) | çürütülemedi |
| **§2.5-4** | **Niceleyici sırası karışması:** *"her x için bir y"* ile *"öyle bir y ki her x"* karışır. Yalnız **başlık düzeyinde** iddia vardır (L14).<br>Panzehir: SMT ya da model checker ile **karşı örnek arama**. | ikincil | çürütülemedi |
| **§2.5-5** | **Maddi koşul ile gündelik "eğer" karışması:** boş öncüllü durumlar yanlış işlenir. **Bulunamadı**.<br>Panzehir: vacuous-truth durumlarını **ayrıca test etme**. | — (bulunamadı) | çürütülemedi |
| **§2.5-6** | **Madde atlama:** N maddeden bazıları **sessizce** uygulanmaz. Metodoloji vardır, rakam yoktur (L16).<br>Panzehir: maddeleri **numaralandır**, LLM'e checklist olarak **geri doğrulat**, her maddeyi **ayrı test case'e** bağla. | birincil (metodoloji) | çürütülemedi |
| **§2.5-7** | **Belirsizlik etiketinin sessizce kesinliğe dönüşmesi:** spec'te `[?]` yazar, kodda **hardcoded kesinlik** olur. **Hiç ölçüm yoktur** (L15).<br>Panzehir: etiketleri **tip sistemine taşı** (`Option`/`Result`); sonradan **spec-kod diff'i** al. | çıkarım | kapsam daraltıldı → K31 |
| **§2.5-8** | **Aynı aktörün hem testi hem kodu yazması:** testler *"spec'i doğrulamak"* yerine **"üretilen kodu geçirmek"** için yazılır. **Ölçülmüştür: %32,67 çözüm sızıntısı.**<br>Panzehir: test yazımını **ayrı ajana ya da ayrı tura** ver; spec'ten bağımsız **üçüncü taraf** test üretimi. | ölçüm | çürütülemedi |

### §2.6 — Güvence sıralaması

*Maliyet artan sırayla.*

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§2.6-1** | **Tip sistemi / biçimsel kısıt** (SMT, model checker, Dafny tarzı) **en güçlü ölçülmüş kanıta** sahiptir: Clover'ın %87 kabulü ve sıfır yanlış pozitifi. Maliyeti **yüksektir** (biçimsel dil ve araç kurulumu).<br>⚠️ Model checking **kodu da** doğrulayabilir (CBMC) ⇒ *"yalnız spec üzerinde çalışır"* yanlıştı. Ama CBMC **bounded**'dır ⇒ üstünlük **koşulsuz değildir**; property-based testing ile aynı açık uçluluk sınıfını paylaşır ve fark **niceliksel**dir. | birincil | daraltıldı → K30 |
| **§2.6-2** | **Genişletilmiş / property-based test seti:** zayıf testte yüksek skor, zengin testte düşüş **ölçülmüştür** (L11). Maliyeti **ortadır** — ve **üreten taraf ayrı olmalıdır**. | birincil (kısmi) | çürütülemedi |
| **§2.6-3** | **İkinci modelle denetim / ayrı aktör test üretimi:** kanıt **dolaylıdır**. Aynı aktör sızıntısı (%32,67) **tam tersini** destekliyor ⇒ ayrıştırmanın değeri **negatif kanıtla** gösteriliyor. Doğrudan *"ayrı model test yazınca X azaldı"* ölçümü **bulunamadı**. Maliyeti orta-yüksektir. | dolaylı | çürütülemedi |
| **§2.6-4** | **Statik analiz geri besleme döngüsü:** ikincil kaynaktan gelir, birincil doğrulanamadı (L9). Maliyeti **düşük-ortadır** — mevcut linter'lar yeterlidir. | ikincil | çürütülemedi |
| **§2.6-5** | **LLM'e testleri de yazdırmak (aynı aktör):** **kısmen tiyatrodur** — %32,67 sızıntı güvence değerini sınırlar. Maliyeti düşüktür ama **güvenilirliği de düşüktür**. | ölçüm | çürütülemedi |
| **§2.6-6** | **Round-trip / back-translation:** kavramsal olarak mantıklıdır ve **doğrudan ölçülmüş etkinlik kanıtı bulunamadı**. Maliyeti ortadır. | kestirim | çürütülemedi |
| **§2.6-7** | **"Prompt'a daha fazla biçimsellik ekle" (araç yok): en zayıf halkadır.** Hiçbir kaynak bunun tek başına yeterli olduğunu göstermiyor. MiniF2F ve FOLIO gibi tasarımların **tümü**, salt metin disiplininin yetmediğini **varsayarak** üzerine biçimsel araç katmanı ekliyor. Maliyeti en düşüktür, **kanıtı da en zayıftır**. | çıkarım | çürütülemedi |
| **§2.6-8** | Yedinci satır **doğrudan bize bakar**: Salih'in önerme formu **salt metin disiplinidir**.<br>Sonuç: **önerme formu gereklidir ama yeterli değildir.** Değeri, kodun *yerine geçmesi* değil, **birinci ya da ikinci sıradaki bir doğrulayıcıya bağlanabilir olmasıdır**. | çıkarım | çürütülemedi |

---

## 3. Öğrenme sırası

*Ön koşul zinciridir; her katman bir öncekinin çözemediğini çözer.*

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **L23** | **Üç değerli mantık ve `Option`/`Maybe` tipleri** (ön koşul yok): `[?]` ile `⊨X`'in kod karşılığını çözer. **Bu, Salih'in kendi notasyonunun doğrudan ihtiyacıdır.**<br>En başta gelir, çünkü **her önermesinde bu etiketler vardır** ve naif çeviri onları **birleştirip yok eder**. | çıkarım | çürütülemedi |
| **L24** | **Niceleyici kapsamı, De Morgan ve maddi koşul** (ön koşul L23): `∀∃` sırasını, `¬` dağılımını, `P→Q`'nun `¬P` dalını ve converse hatasını çözer.<br>Salih zaten bu sembolleri kullanıyor ⇒ **kullandığı sembolün kod semantiğini bilmek zorundadır**. | çıkarım | çürütülemedi |
| **L25** | **Kapalı dünya ile açık dünya ve negation-as-failure** (ön koşul L24): `¬P`'nin *"yanlış olduğu kanıtlandı"* mı yoksa *"bulunamadı"* mı olduğunu çözer.<br>L24 olmadan ayrım **görünmezdir**; ve *"aranamadı"* etiketi tam bu ayrımın **kendi notasyonumuzdaki karşılığıdır**. | çıkarım | çürütülemedi |
| **L26** | **Design by Contract** — önkoşul, sonkoşul, değişmez (ön koşul L24): önerme formunun **en doğrudan kod karşılığıdır**. Öncül precondition'a, sonuç postcondition'a gider.<br>Önermeler zaten `öncül → sonuç` yapısındadır ⇒ **çeviri neredeyse birebirdir**. Ama L3 geçerlidir: **çalışma zamanı kontrolü, dil garantisi değil**. | çıkarım | çürütülemedi |
| **L27** | **Property-based testing** (ön koşul L26): `∀` önermelerinin **pratik** kod karşılığı ve shrinking.<br>L26 tek çağrıyı korur, L27 **girdi uzayını** tarar. Ve L4 geçerlidir: **ispat değil, güven artışı**. | çıkarım | çürütülemedi |
| **L28** | **Model checking (TLA+)** (ön koşul L27): `t`/`t+1` zamansal önermelerini ve sonlu durum uzayının **tüketici** taranmasını çözer.<br>En sonda gelir çünkü **en pahalı ve en güçlüdür**. Ve kavramı al, üretim sistemini kurma hükmü burada da geçerlidir. | çıkarım | daraltıldı → K30 (bounded sınırı) |
| **L29** | Sıranın gerekçesi şudur: L23 → L24 → L25 **notasyonun kendi semantiğidir** (Salih'in zaten yazdığı şeyin ne demek olduğu); L26 → L27 → L28 **doğrulama merdivenidir** (artan maliyet, artan epistemik güç).<br>İlk üçü **bugün gereklidir**; son üçü **kod yazımı başlayınca** gereklidir. | çıkarım | çürütülemedi |

---

## 4. Uygulanabilir hüküm

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **L30** | Notasyona üç ayrım eklenir.<br>`[?]` koda çevrilince `None`'a düşer ve `⊨X` ile birleşir ⇒ kod karşılığı **şimdiden yazılır**: `Unknown`.<br>`⊨X`'in kod karşılığı **yoktur** ⇒ `else`'e düşer; kod karşılığı `Contradictory` olur — **ayrı dal, ayrı tip**.<br>`¬`'nin kapalı dünya mı açık dünya mı olduğu **belirsizdir**; *"aranamadı"* etiketi bunu kısmen çözer ve **notasyona alınmalıdır**. | çıkarım | çürütülemedi |
| **L31** | Önerme yazarken bugünden uygulanacak dört kural: `∀`/`∃` kullanınca **sırayı açıkça numaralandır**; `→` yazınca **`⇔` olmadığını** kastediyorsan belirt; `t`/`t+1` içeren önermede **hangi durumun korunması gerektiğini** yaz; `P → Q` yazınca **`¬P` durumunda ne olduğunu** ayrıca yaz.<br>Dördünün de maliyeti **yaklaşık sıfırdır** ve dördü de **çeviri anında geri kazanılamayacak** bilgiyi şimdi korur. | çıkarım | çürütülemedi |
| **L32** | Önerme formu **doğrudan koda gitmez**.<br>Zincir şudur: önerme formu → DbC sözleşmesi (öncül precondition, sonuç postcondition) → property-based test ile `∀` taraması → kod.<br>Bu zincir §2.6'nın **ikinci sırasındaki** güvenceye bağlanır ve **birinci sıraya kapı açar**; ve seni §2.6'nın **yedinci sırasında kalmaktan** (salt metin disiplini, en zayıf) çıkarır. | çıkarım | çürütülemedi |

---

## 5. Açık borçlar

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **M1** | ~~Antitez koşulmadı~~ ⇒ **KAPANDI.** Araçlı koştu (21 araç çağrısı): **3 çürütme** (K27, K30, K31), **3 daraltma** (K28, K29, K32), **4 sağ çıkan iddia**.<br>Ayrıca hakemin **iki öngörü hatası düştü**: işaret ettiği iki iç çelişki adayının **ikisi de tutmadı**, ve antitez bunu dürüstçe raporladı. Bir antitez ajanının *"aradığın çelişki yok"* diyebilmesi, protokolün **evet-adamı üretmediğinin** kanıtıdır. | — | kapandı |
| **M2** | AWS TLA+ raporuna **erişilemedi** (L2). Bu ailenin en çok atıf beklenen endüstriyel kanıtıdır. | aranamadı | — |
| **M3** | Doğal dil→mantık hata oranları literatürüne **erişilemedi**. Ampirik destek **şu an sıfırdır**; yalnız kavramsal argüman vardır.<br>⚠️ Bu bir **"aranamadı"**dır. | aranamadı | — |
| **M4** | `[?]`/`⊨X`'in koda taşınma ölçümü: **arandı, alan boş** — literatür boşluğudur, erişim engeli değildir.<br>⚠️ Kapsam **dar okumaya** sabitlenmiştir (K31). | çıkarım | daraltıldı → K31 |
| **M5** | EvalPlus'ın tam `pass@1` fark rakamı leaderboard'dadır ve **kapalıdır**. | aranamadı | — |
| **M6** | LogicBench ve FOLIO'nun kategori bazlı sayısal tabloları: **kapsam var, rakam yok**. | birincil | sağ çıktı ⭐ |
| **M7** | L17'nin gerilimi: önerme formunun ne kadar biçimselleşmesi gerektiği sorusunun **merkezidir** ve **cevapsızdır**.<br>⚠️ Çerçeve değişti: çelişki değil, **ters-U ilişkisi** (K32). | kestirim | çerçeve değişti |
| **M8** | SQL `NULL`, Prolog `\+`, Eiffel/JML birincil kaynaklarının **hepsi kapalıydı** ⇒ §1.3'ün ilgili satırları **kavramsaldır**, birincil kaynaklı değildir. | aranamadı | — |
| **M9** | *"Sağ çıktı"* damgaları **aynı-aile şerhlidir**: antitez ajanları tez ajanlarıyla aynı model ailesindendi.<br>**İstisna:** bu ailenin depo doğrulamalı damgaları (Hypothesis, IFEval, üç benchmark deposu) **şerhten muaftır** — kanıt modelden değil kaynaktan geldi. | çıkarım | — |

---

## 6. Fikir kutusu adayları

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **V76** | **Notasyona kod karşılığı sütunu.** Notasyon tablosuna **üçüncü sütun** eklenir: her sembolün kod karşılığı — `[?] → Unknown`, `⊨X → Contradictory`, `∀ → PBT`, `→ → precondition/postcondition`.<br>Maliyeti bir tablo sütunudur. Getirisi, **çeviri anında kaybolacak bilginin şimdiden sabitlenmesidir**.<br>⚠️ **Antitez bu önerinin gerekçesini GÜÇLENDİRDİ:** kayıp kaçınılmaz olmadığı için (K29), kaçınmak bir **karardır** — ve V76 o kararı şimdiden vermektir. | çıkarım | gerekçesi güçlendi → K29 |
| **V77** | **Önerme → DbC şablonu.** L32'nin zinciri bir beceriye dönüşebilir: önermeyi al, `icontract` sözleşmesine çevir, `Hypothesis` özelliği üret. **Ölçülmüş güvence merdiveninin ikinci basamağına** doğrudan bağlanır. | çıkarım | — |
| **V78** | **"Aranamadı" etiketi.** Aynı öneri buraya **ikinci kez ve farklı gerekçeyle** geliyor: L25'te açık dünya / kapalı dünya ayrımının notasyondaki karşılığıdır. **İki bağımsız aile aynı eksiği işaret etti** ⇒ güçlenmiş adaydır. | çıkarım | — |
| **V79** | **Kendi boşluğumuzu doldurmak.** M4'e göre `[?]`/`⊨X`'in koda taşınması literatürde ölçülmemiştir. JARVIS'te bu **ölçülebilir**: önerme yaz, koda çevirt, etiketin korunup korunmadığını say.<br>Örneklem 1 olur — ama **ölçülmüş** bir 1'dir, ve alan **boştur**. | çıkarım | — |

---

## 7. Kapanış

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§7.1** | Aile A31 ve A32'dir; **antitez koştu** (araçlı, 21 araç çağrısı).<br>Sonuç: 3 çürütme, 3 daraltma, 4 sağ çıkan iddia, 2 düşen öngörü. | ölçüm | — |
| **§7.2** | En güçlü tek bulgu Clover'dır: biçimsel doğrulayıcı, **%87 kabul ve sıfır yanlış pozitif**. | birincil | — |
| **§7.3** | En değerli boşluk, bir LLM'in `[?]`/`⊨X` etiketlerini koda taşıma davranışının **ölçülmemiş olmasıdır** — doldurulabilir bir alandır. | çıkarım | daraltıldı → K31 |
| **§7.4** | Ana hüküm: **önerme formu gereklidir ve yeterli değildir**; değeri **bir doğrulayıcıya bağlanabilir olmasıdır**. | çıkarım | çürütülemedi |
| **§7.5** | **Bu raporun kendi zayıflığı — beyan edilir:** üç mutlak ifadesi (*"imkânsız"*, *"geri alınamaz"*, *"yalnız spec üzerinde"*) fazla güçlüydü ve **üçü de daraltıldı**.<br>Ortak kalıp: **mutlak niceleyici tek bir karşı örnekle düşer** — ve üçünde de karşı örnek vardı, biz aramamıştık.<br>Ayrıca §1.3'ün **ampirik desteği sıfırdır** (M3): tablo **kavramsal argümandır**, ölçüm değildir. Değerlidir ama **kanıt sınıfı farklıdır**. | çıkarım | — |
