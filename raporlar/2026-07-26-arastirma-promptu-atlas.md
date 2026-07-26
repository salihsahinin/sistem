# Araştırma Promptu Verimi — önerme formu

*Kayıt: 2026-07-26 · Carvis (CC, yan-oturum m.41) · Talep: "ana oturuma geçince araştırma promptlarımın verimini arttırmaya yönelik çalışmalıyız … araştır atlasları koş rapor oluştur"*

**REGISTER:** Salih'in 07-26 hükmü gereği **tam önerme formunda** (P144). Gerekçe: okuma modu = Salih ⊕ JARVIS. Compiler KAPALI; insan-yüzü muadil ayrı oturuma ertelendi ve bu **eksiklik sayılmaz**.

**Aileler:** A28 (brifing tasarımı) · A29 (bağlam ekonomisi) · A30 (verim ölçümü)
**Notasyon:** `2026-07-26-LOJIK-onerme-formu.md` §Notasyon ile aynı. `⊨D` birincil · `⊨K` ikincil · `⊨X` çelişkili · `⊨¬2` antitez koşulmadı · `[?]` kestirim.
**Okuma kuralı:** öncülü sağlanmayan önermenin sonucu geçerli DEĞİLDİR.

> **DURUM:** A28, A29 ∧ A30 **kapandı**.

> ## ⛔ DÜZELTME KAYDI — 2026-07-26 antitez turu *(teslim SONRASI eklendi)*
> Antitez **araçsız** koştu (`tool_uses = 0`) ⇒ **mantıksal** saldırılar tam güçtedir; **olgusal karşı-örnekler `[K-hatırlama]`**dır ∧ borç açar. Hakemlik: `raporlar/2026-07-26-antitez-hakemlik.md` §6.
>
> | Düzeltme | Nerede | Ne oldu |
> |---|---|---|
> | **K19** ⭐ | §2.5 ⑧ · §2.4 | *"Özetleme kaybını ölçen HİÇBİR çalışma yok"* ⇒ **`[ARANAMADI]`** — koca bir alt-alan var ∧ taranmadı |
> | **K20** ⭐ | §3.6 · §3.7 ⑥ | *"Negatif talimat için HİÇBİR kanıt yok"* ⇒ **`[ARANAMADI]`** — doğrudan ölçen çalışma var |
> | **K21** ⭐ | §3.7 ③ | *"Sistematik olarak daha kötü"* → **"ölçülen bazı kurulumlarda belirgin daha kötü"** |
> | K22 | §4.6 ④ · Q30 | *"Korelasyon raporlanmamalı"* → **güven aralığıyla birlikte raporlanır**; çifte standart kaydı |
> | K23 | §4.6 ⑦ | *"Sıfır kanıt"* → **nedensel kanıt yok, korelasyonel kanıt var** |
> | K24 | §2.5 ③ (Q13) | Kanıt-türü şerhi **iddia listesine taşındı**; ③'ün ④'ten **çıkmadığı** kaydı |
> | K25 | §4.6 ② | Tekrar örnekleme **rassal varyansı** azaltır, **sistematik yanlılığı azaltmaz** |
> | K26 | §4.6 ⑧ | *"n=1 ASLA meşru değil"* → **ikili/felaket türü farkta meşrudur** |
>
> ⚠️ **K19 + K20 aynı hata sınıfıdır ∧ tam olarak V73'ün uyardığı hatadır:** arama bütçesi tükendiği için **aranamamış** olan şeyi **"bulunamadı"** diye yazdık. Bu, `⊨A` etiketinin gerekçesini **dördüncü kez** üretiyor.
> ⚠️ **Üç iç tutarsızlık kabul edildi** (§4.6 giriş notu): çifte standart, aynı eşiğin iki yerde farklı uygulanması, ve kanıt türü karışması.

---

## 0. ÖNCE: BU KOŞUMUN KENDİ HATASI

**Q1** — CARVIS'İN BRİFİNG HATASI
`brifing(A28, A29, A30) → "arxiv.org/html AÇIK, önce onu dene"`
`ölçüm(A30 ∧ A29) → arxiv.org ∧ export.arxiv.org ∧ ar5iv.labs.arxiv.org = 403 (gate seviyesi)`
⇒ `brifing_iddiası = YANLIŞ` ∧ `maliyet = en az bir ajanın ilk hamlesi`

**Kaynağı:** önceki ailelerde arXiv **PDF**'i kapalıydı ∧ **HTML sürümü hiç denenmemişti** ⇒ *"denenmedi"* → *"açık olabilir"* → brifingte *"açık"*.
⇒ **`denenmemiş ≢ açık`.** Bu, tam olarak ailenin kendi konusudur: **brifingteki doğrulanmamış öncül, ajanın bütçesini yakar.**

**Q2** — DÜZELTMENİN AJANDAN GELMESİ İSTENEN DAVRANIŞTIR
`A30 → proxy_durumunu_ölçtü ∧ brifingi_düzeltti ∧ ara_metin_olarak_bildirdi`
⇒ Düzeltme dört ajana ∧ sonraki ailelere yayıldı.
⇒ **KURAL:** brifing bir hipotezdir, veri karşısında düzeltilir. Ajana *"brifingi sorgula"* yetkisi verilmelidir — **maliyeti sıfır, getirisi ölçülmüş.**

---

## 1. ERİŞİM HARİTASI (bu koşumda ölçüldü — kalıcı değer)

**Q3** ⊨D
`KAPALI(403) = {arxiv.org ∧ tüm_alt_alanları, ScienceDirect, Springer, SAGE, Wiley, ACM_DL, IEEE, *.edu, *.github.io, TÜM_PDF, api.github.com, github.com(web), semanticscholar.org, aclanthology.org, openreview.net, paperswithcode.com, huggingface.co, wikipedia, anthropic.com/engineering}`
`AÇIK = {raw.githubusercontent.com, pypi.org, registry.npmjs.org, code.claude.com/docs/en/<sayfa>.md}`

**Q4** — ⭐ ASİMETRİ VE TAKTİK
`github.com(web) = 403` ∧ `raw.githubusercontent.com = 200`
⇒ **Bu asimetri boyunca replikasyon depolarına yönelmek, kapalı yayıncının etrafından dolaşmanın YOLUDUR.**
`kaynak_kapalı` ⇒ `hedef := replikasyon_deposu ∨ upstream_git ∨ kaynak(.md/.rst/.txt)`
⇒ Bu koşumda **dört kez** karşılığını verdi (A22 ×4 [D] ölçüm · A27 PostgreSQL/Kafka · A29 RULER/NoLiMa · A25 cli.js).
⇒ `kanıt_kalitesi(taktik) > kanıt_kalitesi(makale_özeti)` — engel kaliteyi **düşürmedi, YÜKSELTTİ**.

**Q5** ⊨D — ⭐ SESSİZ TÜKENİŞİN İKİNCİ YÜZÜ
`WebSearch_bütçesi = 200 / OTURUM` ∧ `sayaç = ana_konuşma ⊕ tüm_alt_ajanlar`
`plan_yükseltmesi` ⇒ `kota_sıfırlanır` ∧ **`WebSearch_oturum_sayacı SIFIRLANMAZ`**
`sayaç_dolu` ⇒ `arama → boş_döner ∧ ¬hata`
⇒ **`boş_arama ≢ sonuç_yok`** ∧ **`boş_arama ≡ sayaç_dolu`**
⇒ Ajan bunu bilmezse `aranamadı` durumunu `bulunamadı` diye raporlar ⇒ **negatif bulgu UYDURULUR.**

---

## 2. A29 — BAĞLAM EKONOMİSİ ⊨¬2

### 2.1 Etkin uzunluk ≠ iddia edilen uzunluk

**Q6** ⊨D — RULER (17 açık model)
`iddia_edilen_pencere ≫ etkin_pencere` (etkin = kalite eşiğini koruduğu uzunluk)

| Model | İddia | Etkin | Bozulma |
|---|---|---|---|
| GPT-4-1106-preview | 128K | **64K** | — |
| Llama3.1-70B | 128K | **64K** | 88,4 (@64K) → 66,6 (@128K) |
| Mixtral-8x7B | — | — | 94,9 (@4K) → **44,5** (@128K) |
| DBRX | — | — | 95,1 (@4K) → **0,0** (@128K) |
| Qwen1.5-72B | — | — | 94,9 (@4K) → **0,0** (@64K ∧ @128K) |

⇒ `neredeyse_hiçbir_model → iddia_ettiği_boyutta eşik_performansını KORUMUYOR`

**Q7** ⊨D — ⭐ NoLiMa (12 güncel model, ICML 2025)
*Tasarım farkı kritik:* `literal_kelime_örtüşmesi = ∅` ⇒ **"lost in the middle" konfüzyonlarından ARINDIRILMIŞ** ⇒ ölçülen şey saf konum etkisi değil, **anlamsal/distractor etkisi**.

| Model | Kısa-bağlam tabanı | @32K | Etkin uzunluk |
|---|---|---|---|
| GPT-4o | 99,3% | 69,7% | **8K** |
| Claude 3.5 Sonnet | 87,6% | **29,8%** | **4K** |
| Gemini 1.5 Pro | 92,6% | 48,2% | **2K** |

`@32K → 12_modelden 10'u < 0,5 × kısa_bağlam_tabanı`
⇒ **`lost_in_the_middle(2025, frontier) = HÂLÂ GEÇERLİ`** ∧ konum etkisinden ayrıştırılmış.
⇒ Axis-1 sorusunun cevabı: **evet, güncel modellerde de geçerli.**

**Q8** — ÇIKARIM
`nominal_pencere ∈ [128K, 1M]` ∧ `görev = distractor_yoğun ∨ dikkat_gerektiren`
⇒ `etkin_bütçe ∈ [2K, 16K]`
⇒ **`bağlam_bütçesi := etkin_uzunluk` ∧ `≠ nominal_pencere`**

### 2.2 Ölçülemeyenler — dürüstlük kaydı

**Q9** — REPO'YA İNİLDİ, RAKAM YOKTU (`⊨D` erişim ∧ rakam = ∅)
`lost-in-the-middle(repo) → metodoloji doğrulandı` (altın belge 20-belgelik bağlamda pozisyon 0/4/9/14/19; 10/20/30-belge koşulları; key-value görevinde 300 anahtara kadar)
∧ `README → sonuç_tablosu = ∅` ∧ `arXiv = 403`
⇒ **U-şekilli eğrinin kesin sayıları DOĞRULANAMADI ⇒ rakam VERİLMEDİ.**

**Q10** — AYNI DURUM: MAST
`MAST(repo) → "ilk kapsamlı MAS başarısızlık taksonomisi" ∧ taksonomi_figürü = var`
∧ `kategori_yüzdeleri = ∅` ∧ `arXiv ∧ HuggingFace = 403`
⇒ **hiçbir kategorik/yüzdesel rakam verilmedi.** *(Alt dizin taraması istendi — delta bekleniyor.)*

**Q11** — AYNI DURUM: Large Language Monkeys
`repo → pass@k metodolojisi doğrulandı (GSM8K, MATH, CodeContests, MiniF2F-MATH)`
∧ `ölçek_eğrisi_rakamı = ∅`
⇒ **"getiri nerede düzleşiyor" sorusuna kanıt YOK.**

> **▲ Bu üç önerme raporun en değerli kısımlarından biridir.** Üç çalışmanın da deposuna İNİLDİ, metodolojisi DOĞRULANDI, ve **rakamı olmadığı için rakam verilmedi.** Ajan üç kez rakam uydurabilirdi; uydurmadı.

### 2.3 Koordinasyon maliyeti — ölçülmüş

**Q12** ⊨D
`agent_teams ∧ teammate ∈ plan_modu` ⇒ `token ≈ 7 × standart_oturum`
Gerekçe: `her_teammate → kendi_bağlam_penceresini_sürdürür`
`token_kullanımı ∝ takım_boyutu` (kabaca doğru orantılı)
⇒ Bu, koordinasyon maliyetinin **sayısal ve birincil-kaynaklı** tek verisidir — *token boyutunda; **doğruluk/kalite boyutunda DEĞİL***.

**Q13** ⊨D — VARSAYILAN TOPOLOJİ
`alt_ajan → kendi_bağlam_penceresi` ∧ `ana_konuşmaya → yalnız_ÖZET döner`
`nesting = varsayılan KAPALI` (`MAX_SUBAGENT_SPAWN_DEPTH = 1`)
Resmî desen: *"Research the X, Y, Z in parallel using separate subagents… this works best when the research paths don't depend on each other."*
Resmî uyarı: *"Running many subagents that each return detailed results can consume significant context."*
⇒ `varsayılan_mimari = izole_bağlam ⊕ özet_döngüsü` ∧ `≠ bağlam_paylaşımı`
⚠️ **Damga:** bu bir **ürün-tasarım kararı/tavsiyesidir**, RCT DEĞİLDİR. Birincil kaynak ⊨D, ama *kanıt türü* farklı.

**Q14** ⊨D — SIKIŞTIRMA: MEKANİZMA VAR, KAYIP ÖLÇÜMÜ YOK
`/compact` ⇒ `mesaj_geçmişi := özet` ∧ `cache → geçersiz`
`hook_ile_önişleme` ⇒ `10.000_satırlık_log: on_binlerce_token → yüzlerce_token`
⇒ Bu bir **token-hacim iddiasıdır**; `bilgi_kaybı_ölçümü = ∅`.

### 2.4 A29 — PARÇALAMA KURALI

**ÖLÇÜLMÜŞ (Q6, Q7, Q12, Q13 dayanaklı):**
1. `bağlam_bütçesi(alt_ajan) := modelin_ÖLÇÜLMÜŞ_etkin_uzunluğu` ∧ `≠ iddia_edilen_pencere`
2. `alakasız_materyal_eklemek → başlı_başına_maliyetli` — NoLiMa'nın 30-70 puanlık düşüşleri **konum etkisinden bağımsız** bir hacim/kirlilik etkisidir
3. `varsayılan_topoloji := izole_bağlam ⊕ özet_döngüsü` — alt-ajanlar birbirinin **ham** bulgusunu görmez; orkestratör sentezler
4. `N_ajan ↑` ⇒ `token ↑ (doğrusal, plan_modunda ≈7×)` ⇒ `N_büyütmenin_gerekçesi := görevin_MECE_ayrışabilirliği` ∧ `≠ "daha fazla ajan daha iyi"`
5. `sıralı_zincir ⇔ adımlar_gerçekten_bağımlı` ∧ `bağımsız_iş → paralel_fan_out`

**KESTİRİM `[?]` (ölçülemedi — açıkça işaretli):**
- `[?]` self-consistency/ensemble N'inin getiri-düzleşme noktası — **hiçbir birincil kaynaktan doğrulanamadı**
- `[?]` paralel araştırma hatlarının optimal sayısı — yalnız MECE tasarım sezgisi, **ablasyon değil**
- `[?]` sıralı zincirde hata birikim oranı — **hiçbir ölçüm yok**, yalnız mekanizma/tavsiye
- `[?]` özetleme/sıkıştırmanın bilgi-kaybı büyüklüğü — mekanizma doğrulandı, **miktar bizim tarafımızdan ölçülmedi**
  > **[K19]** ⚠️ *"Ölçülmedi"* burada **"literatürde yok"* demek DEĞİLDİR. Sadakat metriği literatürü (QAGS, SummaC, FactCC) ∧ sıkıştırma kaybı literatürü (LLMLingua) **mevcuttur ∧ bu koşumda taranmamıştır**.

### 2.5 A29 — İDDİA LİSTESİ · **ANTİTEZ KOŞTU, hükümler işlendi**

① Bağlam kirliliği 2025 frontier modellerinde 32K'da %30-70 doğruluk kaybına yol açabiliyor. — **DARALDI:** antitez haklı olarak *"%30-70 aralığı o kadar geniş ki neredeyse her gözlemi doğrular"* dedi ⇒ **sahte kesinlik**. Rakamlar korunur (ölçüm gerçek), ama **aralık bir öngörü olarak kullanılamaz**; tek tek model satırları (Q7) kullanılmalıdır.
② İddia edilen ile ölçülmüş etkin uzunluk arasında bazı modellerde **16 kata varan** uçurum var. — **çürütülemedi**
③ Alt-ajanlar arası varsayılan/önerilen mimari bağlam paylaşımı değil **izolasyon + özet-döngüsü**dür.
   > **[K24 · antitez tam isabet — üç ayrı nokta, üçü de kabul]** ① Bu bir **mimari tasarım tavsiyesidir**, olgusal konsensüs **değildir**; blackboard ve paylaşılan bellek mimarileri de mevcuttur. ② Daha keskini: **bu tercih ④'teki maliyet kaygısından türüyor, MAST'ın başarısızlık kanıtından DEĞİL** — yani **maliyet güdümlü** bir gerekçe, **güvenilirlik güdümlüymüş** gibi sunuluyordu. ③ Dolayısıyla **③, ④'ten mantıksal olarak ÇIKMIYOR**.
   > ⚠️ Bu şerh raporda **zaten vardı** (Q13: *"ürün-tasarım kararıdır, RCT DEĞİLDİR"*) — ama **iddia listesine taşınmamıştı**. Bu, *"iddia listesi raporun kendisinden zayıf çıkıyor"* deseninin bu ailedeki vakasıdır.
④ Takım büyüklüğü token maliyetiyle kabaca doğru orantılı; plan-modunda ≈7×. — **çürütülemedi** *(token boyutunda; **doğruluk/kalite boyutunda ölçüm yok**)*
⑤ MAST taksonomi sunuyor ama sayısal kategoriler **delta turunda kapatıldı** (Q9b) ⇒ iddia **artık geçersiz**, taksonomi rakamlarıyla elimizde.
⑥ Self-consistency getiri-düzleşmesine dair bu oturumda **hiçbir kanıt bulunamadı**. — **çürütülemedi** *(erişim kaydı)*
⑦ Sıralı zincir ile paralel fan-out arasındaki hata birikimini ölçen **hiçbir çalışma bulunamadı**. — **çürütülemedi**
⑧ Özetlemenin bilgi kaybını doğrudan ölçen çalışma **bu koşumda ARANAMADI** — *"hiçbir çalışma yok"* **DEĞİL**.
   > **[K19 · ⭐ antitez ÇÜRÜTMESİ — yokluk iddiası düştü]** Antitez tek bir karşı-örnekle değil, **koca bir alt-alanla** karşılık verdi: **QAGS, SummaC, FactCC** (özet sadakati metrikleri) ∧ **LLMLingua** (sıkıştırmanın downstream kaybı). Alan adları spesifik ∧ tutarlı ⇒ **kabul edildi**.
   > ⇒ Doğrusu: **`bizim aradığımız kanalda bulunamadı; sadakat-metriği literatürü MEVCUT ∧ TARANMADI`**.
   > ⇒ **Bu tam olarak V73'ün uyardığı hatadır:** arama bütçesi tükenmişken **`[ARANAMADI]`** olan şeyi **`bulunamadı`** diye yazdık.
⑨ Çok-ajan sistemlerin tek ajanı ne zaman geçtiğine dair **baş başa ölçüme erişilemedi**. — **çürütülemedi** *(erişim kaydı)*

---

## 2.6 A29 DELTA — kapatılan boşluklar

**Q9b** ⊨D — ⭐ MAST SAYISAL TAKSONOMİSİ KAPANDI
`repo/assets/ taraması` ⇒ taksonomi figürü **doğrudan indirildi ∧ okundu** (yazarların yayımladığı birincil görsel, ikincil aktarım değil).

`3 üst_kategori ∧ 14 alt_başarısızlık_modu` (kategoriler ~ayrık, toplam ≈ %100):

| Üst kategori | Pay | Alt modlar |
|---|---|---|
| **Poor Specification** (sistem tasarımı) | **%37,17** | görev şartnamesine uymama %15,2 · rol şartnamesine uymama %1,57 · **adım tekrarı %11,5** · konuşma geçmişi kaybı %2,36 · sonlanma koşullarından habersizlik %6,54 |
| **Inter-Agent Misalignment** (koordinasyon) | %31,41 | konuşma sıfırlanması %5,50 · netleştirme istememe %2,09 · görevden sapma %5,50 · **bilgi saklama %6,02** · diğer ajanın girdisini görmezden gelme %4,71 · **muhakeme-eylem uyumsuzluğu %7,59** |
| **Task Verification** (kalite kontrol) | %31,41 | erken sonlanma %8,64 · eksik/yok doğrulama %9,16 · **yanlış doğrulama %13,61** |

> **⭐ Bu, bu ailenin en karar-değiştiren tek bulgusudur.**
> `en_büyük_tek_kategori = Poor_Specification (%37,17)`
> ⇒ **Çok-ajan başarısızlıklarının en büyük payı ajan-etkileşiminden DEĞİL, görev/sistem tasarımının en baştan kötü kurulmasından geliyor.**
> ⇒ Yani "araştırma promptunun verimi" sorusu, çok-ajan başarısızlığının **birinci** kaynağıdır — ikincil bir iyileştirme değil.
> ⇒ Ve `yanlış_doğrulama (%13,61) > eksik_doğrulama (%9,16)` ⇒ **kötü hakem, hakemsizlikten daha zararlı.** Bu, m.40b'nin maskeli hakemlik tasarımını doğruluyor.

**Q11b** — "More Agents Is All You Need": KISMEN KAPANDI, statü YÜKSELDİ
`9 repo_adı_tahmini → 404` ∧ `asıl_hata = DAL_ADI (main değil master)`
`repo doğrulandı` ⊨D ∧ `metodoloji teyitli` (`run.sh {AGENT_NUM} {MODEL} {QTYPE}` — **ajan sayısı doğrudan kontrollü değişken**; MATH/GSM8K/MMLU/Chess/HumanEval)
`README → ölçek_eğrisi ∧ düzleşme_noktası = ∅` ∧ `dizin_listeleme = imkânsız` (codeload ∧ jsdelivr kapalı)
⇒ **Statü: `aranamadı` → `bulunamadı`.** *(Repoya fiilen erişildi, içinde sayı yok — bu bir yokluk BULGUSUDUR.)*

**Q11c** ⊨K `[doğrulanmadı]` — self-consistency N-getirisi: HÂLÂ AÇIK
`arama_özeti_iddiası: "1,5,10,20,40 örneklemle test edilmiş; çoğu ayarda daha fazla örnek daha iyi; en az bir çalışmada 5'in üzerinde performans DÜŞÜŞE geçiyor"` ⇒ `[X aday]`
`birincil_kaynak (arXiv ∧ openreview) → hiç açılamadı`
⇒ **Rakam VERİLMEDİ.** Ajanın kendi hükmü: *"WebSearch'ün kendi sentezi, ikinci-el aktarım, ben doğrulamadım."*
⇒ Dolaşan `"%40 daha iyi"` iddiası birincil kaynaksız ⇒ **FOLKLOR olarak işaretlendi, kanıt sayılmadı.**

**Q11d** — ⭐ SESSİZ TÜKENİŞ TESTİ (Q5'in canlı doğrulaması)
`delta_turunda 2 arama yapıldı` ∧ `ikisi de NORMAL sonuç döndürdü`
⇒ `sayaç o anda henüz DOLMAMIŞTI`
⇒ Q5'in ayrımı işledi: ajan, aramanın boş dönüp dönmediğini **hüküm kurmadan önce** kontrol etti.

---

## 3. A28 — BRİFİNG TASARIMI ⊨¬2

### 3.1 Persona / rol atama

**Q15** ⊨D — PERSONA ETKİSİ GERÇEK **AMA** TEK YÖNLÜ KAZANÇ DEĞİL
`alan_uzmanı_persona ∧ görev = dil_tabanlı_muhakeme (MMLU)` ⇒ `performans > alan_dışı_persona`
**∧** aynı çalışma: `persona_ataması → ÖNYARGI da açığa çıkarıyor` ("erkek" persona arabaları "kadın" personadan daha iyi tanımlıyor)
⇒ **`persona_etkisi = ölçülmüş ∧ gerçek` ∧ `≠ saf_kalite_artışı`** — görev-bağımlı ∧ önyargı riski taşır.

**Q16** ⊨D — ⭐ VE PERSONA ÇÖKERTEBİLİYOR (sayısal)
`Llama3.1-8b ∧ "Multi-Persona" (angel/devil rol-oynama)`:
`GSM8K: 47,60` vs `CoT: 80,13` vs `direkt: 70,40`
`MATH: 10,30` vs `CoT: 40,13`
⇒ **Rol/persona-tabanlı prompt tasarımı ölçülmüş biçimde ÇÖKERTİYOR** — tek-ajan zincir-düşünceden belirgin biçimde kötü.

**Q17** ⊨K `[?]` — `alakasız_persona_detayı` ⇒ `~30 puanlık düşüş` bildirilmiş.
⚠️ **Rakam doğrulanamadı** (birincil metne erişilemedi) ⇒ `[?]` damgalı, hüküm kurulmaz.

### 3.2 Format kısıtlaması — ⭐ bizi doğrudan ilgilendiren eksen

**Q18** ⊨D — KATI FORMAT ZORUNLULUĞU ZAYIF MODELDE HER ŞEYİ ÇÖKERTİYOR
`AgentVerse_çerçevesi ∧ katı_format_zorunluluğu ∧ Llama3.1-8b`:
`MMLU: 13,27` (baseline **43,13**) · `GSM8K: 5,47` (baseline **70,40**)
⇒ `format_uyumsuzluğu` ⇒ **tüm debate çöküyor**

**Q19** ⊨K — `format_kısıtlaması (JSON ∨ XML)` ⇒ `muhakeme yeteneğinde "significant decline"` ∧ `kısıtlama_katılığı ↑ ⇒ düşüş ↑`
⚠️ **Yüzde rakamı doğrulanamadı — VERİLMEDİ.**

> **▲ BİZE DÖNÜK SONUÇ — kendi tasarımımıza itiraz:**
> Ajanlara dayattığımız katı çıktı şeması (numaralı bulgu ⊕ `[D/K/X]` ⊕ iddia listesi ⊕ erişim engelleri ⊕ bulunamayanlar) **ölçülmüş bir maliyet taşıyor.**
> **Ama:** Q18'in etkisi `zayıf_model (Llama3.1-8b)` üzerinde ölçüldü. Bizim ajanlarımız Sonnet 5 ∧ Opus 5.
> `[?]` **Frontier modelde aynı büyüklükte mi, bilinmiyor.**
> ⇒ **Hüküm kurulmuyor, ölçüm borcu açılıyor (D8).** *Bu, A30'un n=1 protokolüyle test edilebilecek ilk somut hipotezdir.*

### 3.3 Kalibrasyon / "bilmiyorum de"

**Q20** ⊨D `[tasarım var, rakam yok]`
`SelfAware_deposu → "Direct" (talimatsız) vs "Instruction" (talimatlı) ayrı komutlar` ⇒ **kontrollü karşılaştırma TASARIMI mevcut**
`README → F1/Precision/Recall = ∅` ⇒ **"Instruction"ın ne kadar iyileştirdiği rakamla doğrulanamadı.**

**Q21** ⊨D — ⭐ KRİTİK AYRIM
`"bilmiyorum" davranışı ∧ FINE-TUNING ile öğretildi` ⇒ `kalibrasyon ↑` ∧ bu meta-beceri **domain-dışı veri setlerine genelleşiyor**
⚠️ **Bu saf prompt-talimatı DEĞİL, eğitim-tabanlı müdahaledir.**
⇒ `salt_prompt_talimatı ≟ eğitim` sorusuna **doğrudan cevap vermiyor**; ima ediyor ki salt prompt muhtemelen **daha zayıf** ⇒ `[?]`.

### 3.4 Atıf zorunluluğu — ▲ nedensel kanıt YOK

**Q22** ⊨D — ⭐ EN ÖNEMLİ NEGATİF BULGU
Bulunan tek yakın çalışma: üretici arama motorlarının atıflarını insan etiketleyicilerle `complete/partial/no support` diye sınıflandırıyor (`train n=8834: 6415/1552/867`).
**AMA:** `bu_çalışma → "atıf zorunluluğu koyarsan halüsinasyon azalır mı" sorusunu KONTROLLÜ TEST ETMİYOR`
`ölçtüğü = zaten_atıf_üreten_sistemlerin atıf_KALİTESİ`
⇒ **`nedensel_iddia = ∅`**

> **▲ Bu bulgu bizim kendi pratiğimize dokunuyor.** JARVIS'te `[D/K/X]` etiketlemesi **standart** ve *"halüsinasyonu azaltır"* varsayımıyla uygulanıyor.
> **Bu varsayımın doğrudan kontrollü kanıtı YOKTUR.**
> ⇒ Etiketleme yine de savunulabilir — ama gerekçesi *"ölçülmüş halüsinasyon azalması"* değil, **"iddianın kanıt seviyesini okuyucuya açık kılması"** olmalıdır. Gerekçe düzeltilir, pratik korunur.

### 3.5 Uzunluk / dikkat dağıtma

**Q23** ⊨D `[dolaylı]` — NoLiMa rakamları (Q7 ile aynı kaynak) bu eksene **en güçlü sayısal kanıttır**
⚠️ **AMA konusu talimat/brief uzunluğu DEĞİL**, bağlam penceresindeki *alakasız metin (haystack)* miktarıdır.
⇒ **Analoji olarak kullanılabilir, birebir eşleşme DEĞİL.** Damga korunur.

### 3.6 A28 — ÖLÇÜLMÜŞ vs FOLKLOR

**ÖLÇÜLMÜŞ:**

| Eksen | İddia | Kanıt gücü |
|---|---|---|
| Format zorlaması | Katı biçim/şema zorunluluğu muhakemeyi düşürür | **ORTA-GÜÇLÜ** — bir birincil sayısal örnek (Q18) + bir ikincil özet (Q19) |
| Persona | Etkisi göreve göre değişir; evrensel kazanç değil, **bazen ciddi kayıp** | **ORTA** — bir birincil kaynak (Q15) + bir birincil sayısal örnek (Q16) |
| Uzunluk/dikkat | Bağlamda alakasız içerik ↑ ⇒ isabet ↓ | **GÜÇLÜ ama DOLAYLI** (Q23) |

**FOLKLOR ∨ DOĞRULANAMAYAN:**

| Eksen | Neden zayıf |
|---|---|
| Format kısıtlaması **kesin yüzdesi** | Rakam birincil kaynaktan doğrulanamadı (Q19) |
| Persona **~30 puan** düşüş | Yalnız arama özeti, birincil erişim yok (Q17) |
| "Bilmiyorum de" talimatı kalibrasyonu iyileştirir | Tasarım var, **sonuç rakamı yok**; kanıtlı olan **eğitim-tabanlı** müdahale (Q20, Q21) |
| Atıf zorunluluğu → halüsinasyon ↓ | **Nedensel test yok** (Q22) |
| **Az-kısıtlı vs çok-kısıtlı brief** (aşırı kısıtlamanın tersine tepmesi) | **HİÇBİR doğrudan kanıt bulunamadı** |
| **Negatif ("yapma") vs pozitif talimat** | **`[ARANAMADI]`** — bütçe tükenmişti ∧ tahmin edilebilir repo adı yoktu.<br>**[K20 · antitez ÇÜRÜTMESİ]** *"Hiçbir kaynak bulunamadı"* ifadesi **yanlıştı**: modellerin olumsuzlamaya duyarsızlığını **doğrudan ölçen** çalışma vardır (Kassner & Schütze, ACL 2020). ⇒ K19 ile **aynı hata sınıfı**, aynı düzeltme: `aranamadı ≠ yok`. |
| **Few-shot'un açık-uçlu araştırma görevlerindeki etkisi** | Ayrı bir literatür kümesi **bulunamadı** |

### 3.7 A28 — İDDİA LİSTESİ · **ANTİTEZ KOŞTU, hükümler işlendi**

① Persona/rol ataması araştırma çıktısı kalitesini artırmaz, yalnız üslup ∧ derinlik-berraklık dengesini değiştirir. — **çürütülemedi** *(hafif, hedge'li bir iddiadır — bu yüzden sağlam)*
② Format/şema zorunluluğu, model akıl yürütme adımlarını gizli tuttuğunda doğruluğu düşürür. — **çürütülemedi**
③ Çok-ajanlı persona rol-oynama, tek-ajan zincir-düşünceden **ölçülen bazı kurulumlarda belirgin biçimde daha kötü** sonuç verir.
   > **[K21 · ⭐ antitez ÇÜRÜTMESİ]** Eski hâli *"**sistematik olarak** daha kötü"* diyordu ⇒ **çürütüldü**. Karşı-örnek: **multiagent debate** GSM8K ∧ MMLU'da tek-ajan CoT tabanını **artırıyor** (Du, Li, Torralba, Tenenbaum, Mordatch). *"Sistematik iddiası tek karşı-örnekle çöker."*
   > ⚠️ Antitezin **ikinci gözlemi daha keskindir ∧ kabul edildi:** ① hafif bir *"etkisiz"* iddiasıyken, ③ aynı aileden **çok daha güçlü** bir *"sistematik zarar"* iddiasına sıçrıyordu — **bağımsız gerekçe olmadan**.
   > ⇒ Q16'nın ölçümü (Llama3.1-8b'de GSM8K 47,60 ↔ CoT 80,13) **geçerli kalır** — ama o **bir kurulumdur**, bir yasa değil.
④ Atıf/kaynak etiketleme zorunluluğu, halüsinasyonu azalttığını gösteren doğrudan kontrollü kanıt **olmadan** varsayılan "iyi pratik" hâline gelmiştir. — **⊨S**; ve antitez bunu **güçlendirdi**: salt prompt seviyesinde *"kaynak göster"* talimatı, retrieval olmadan, **yeni bir halüsinasyon alt-türü** (**uydurma atıf**) üretebiliyor. ⚠️ *(aynı-aile şerhi)*
⑤ "Bilmiyorum de" talimatının etkisinin prompt seviyesinde mi eğitim seviyesinde mi güçlü olduğu **net değildir**. — **çürütülemedi**
⑥ Negatif talimatların pozitiflerden daha az güvenilir tutulduğu ekseni **bu koşumda ARANAMADI**.
   > **[K20 · ⭐ antitez ÇÜRÜTMESİ]** Eski hâli *"hiçbir ölçülmüş kanıt bulunamamıştır"* diyordu ⇒ **yanlış**. Modellerin olumsuzlamaya duyarsızlığını **doğrudan ölçen** çalışma vardır (Kassner & Schütze, ACL 2020).
   > ⇒ Doğrusu: **`bütçe tükendiği için aranamadı`** — yokluk hükmü **değil**. K19 ile aynı sınıf.
⑦ Few-shot'un açık-uçlu görevlerdeki etkisi ayrı bir literatür oluşturmamaktadır — ya da oluşturuyorsa **erişilememiştir**. — **çürütülemedi** *(zaten kendi içinde `aranamadı` payını taşıyor)*
⑧ Uzun ∧ ayrıntılı brief'ler, alakasız içerik arttıkça isabeti düşürme riski taşır. — **⊨S**; hedge'li olduğu için sağlam ⚠️ *(aynı-aile şerhi)*
⑨ Katı biçim zorunluluğunun zararı, **model zayıfladıkça orantısız büyür**. — **çürütülemedi** *(ama D8 borcu duruyor: frontier modelde ölçülmedi)*

---

## 4. A30 — VERİM ÖLÇÜMÜ (n=1) ⊨¬2

### 4.1 LLM-as-judge: rakamlar ve yanlılıklar

**Q24** ⊨D — ÖRNEK-DÜZEYİ İNSAN UYUMU
`AlpacaEval ∧ değerlendirici = alpaca_eval_gpt4`:
`insan_uyumu = %69,2` · `Spearman(model_düzeyi) = 0,97` · `Pearson = 0,93` · `Bias = 28,4` · `Variance = 14,6` · `P(daha_uzunu_tercih) = 0,68`
Kaynağın kendi uyarısı: *"we only use 9 models and so the correlation is not very reliable."*

**Q25** ⊨D — ⭐ VERBOSITY BIAS RAKAMLA ÖLÇÜLDÜ
`uzunluk_kontrollü_kazanma_oranı` ⇒ `Chatbot_Arena_korelasyonu: 0,93 → 0,98`
⇒ **Ham pairwise skorun ~0,05 korelasyon puanı SALT UZUNLUKTAN geliyordu.**

**Q26** ⊨D — VARYANS TEORİK DEĞİL, ÖLÇÜLÜYOR
`insan_uyumu ≡ 4_etiketleyiciden_1'ini_çıkar ∧ kalan_3'ün_çoğunluğunu_tahmin_et` (leave-one-out); otomatik değerlendiricilere **aynı hesap** uygulanıyor.
`varyans ≡ aynı_örnek ∧ 4_farklı_örnekleme (sıra/seed farklı) ∧ modun_3'e_karşı_1'i_tahmin_başarısı`
⇒ **Bias ∧ variance'ı ayırmanın tek yolu TEKRAR ÖRNEKLEMEDİR.**

**Q27** ⊨D — ⭐ KÜÇÜK n'DE KORELASYON ÇÖZÜM DEĞİL
Arena-Hard'ın açık ifadesi: *"randomness in human and LLM judgments leads to inconsistent predictions… difficult to confidently determine if a model's apparent performance reflects a genuine difference… or merely noisy observations."*
⇒ Önerilen ikame: **bootstrap ile güven aralığı örtüşmesi** ("Separability with Confidence"). Somut örnek: `o3: 85,9% (CI −0,8/+0,9)`.

**Q28** ⊨D `[metodoloji var, rakam yok]` — konum yanlılığına karşı **çıktı sırası rastgeleleştirme** resmi değerlendirme kodunda standart pratik olarak kodlanmış.
⚠️ `README → GPT-4/insan uyum yüzdesi = ∅` ⇒ halk arasında bilinen `~%85` rakamı **bu oturumda TEYİT EDİLEMEDİ.**

### 4.2 ⭐ `r≈0.31` çelişkisinin çözümü

**Q29** ⊨X — MEKANİK AÇIKLAMA (sentez, kaynaklanmamış)
`"r≈0.31" iddiasının kaynağı` ⇒ **hiçbir kanalda bulunamadı** *(varlığı da REDDEDİLMİYOR — bu oturumdaki erişimle doğrulanamadı)*

Ama Q24–Q27'den çıkan mekanik açıklama:
> **"Korelasyon" farklı ÖLÇÜM DÜZEYLERİNDE ölçülüyor ∧ bu düzeyler birbirine İNDİRGENEMEZ.**
> (a) `örnek_düzeyi_ikili_uyum` (ör. %69,2) = bir **ORAN**
> (b) `model_düzeyi_Spearman/Pearson` (ör. 0,97) = az sayıda modelin **SIRALAMASI** üzerinden korelasyon **KATSAYISI** ∧ yazarların kendi ifadesiyle küçük n'de **"güvenilir değil"**
> (c) `görev_tipi` de değiştiriyor — yorumlayıcı/öznel görevlerde daha düşük

⇒ **`"%80 uyum" ∧ "r≈0.31" ÇELİŞMİYOR OLABİLİR** — muhtemelen **farklı istatistikleri** (oran vs korelasyon katsayısı) ∧/∨ **farklı görev tiplerini** (yapılandırılmış tercih vs öznel derecelendirme) ölçüyorlar.
⚠️ **Bu sentez `⊨X` düzeyinde kalıyor** — `r≈0.31`'in kendi kaynağı doğrulanamadığı için **TAM ÇÖZÜM DEĞİL.**

> **▲ Bu, oturumun başında verdiğim düzeltmenin düzeltmesidir.** Daha önce *"r≈0.31 çürütüldü, MT-Bench >%80 geçerli"* demiştim. Doğrusu: **ikisi farklı şeyi ölçüyor olabilir ∧ MT-Bench'in %85'i de bu oturumda birincil kaynaktan teyit edilemedi (Q28).** Hüküm **açık kalıyor**, kapanmış sayılmıyor.

### 4.3 n=1 ÖLÇÜM PROTOKOLÜ

| Adım | Ne yapılır | Ne ölçer | Kaç koşum | Hangi hükmü meşru kılar |
|---|---|---|---|---|
| **1. Eşleştirilmiş tasarım — ZORUNLU** | Aynı görev setini (5-20 gerçek soru) **iki promptla da** koştur | Prompt farkını görev-zorluğu gürültüsünden ayırır | set başına 2× | *"Bu prompt, BU görev listesinde, ötekine göre X kez tercih edildi"* — daha fazlası değil. **Eşleştirilmemiş karşılaştırma n=5-20'de ANLAMSIZA yakındır** |
| **2. Kör, sıra-rastgeleli pairwise** | A/B sırasını rastgele ata (Q28), hangi promptun hangisi olduğunu **yargı anında gizle** | Doğrudan "hangisi daha iyi" | çift başına ≥1, idealde 3 | Mutlak puanlama iki farklı oturum arası **karşılaştırılabilirlikte zayıf** |
| **3. Yargıyı tekrar örnekle** | Her çift için yargıcı **3 kez** (farklı seed/sıra), çoğunluk oyu | Tek-atımlık yargının **kararsızlığını** (Q26) | 3× | `3/3` ⇒ düşük belirsizlik · `2/1` ⇒ **"belirsiz, tek atımlık yargıya güvenilmez"** — bunu AÇIKÇA işaretle |
| **4. Bootstrap/CI ile özetle** | Ham "X/Y kazandı" sayısına indirgeme; kazanma oranı **+ CI** birlikte (Q27) | Gürültüden ayrılabilir sinyal | — | `CI %50'yi net dışlıyorsa` ⇒ **yönsel sinyal** ∧ `≠ kesin kanıt` |
| **5. ⭐ Bilinen-cevap kanarya maddeleri** | Sete 1-2 tane, cevabını **zaten bildiğin**, doğrulanabilir kısa-gerçek sorusu koy | Ajanın gerçeği bulup bulmadığını — **istatistik gerekmez**, ikili sonuç | 1-2 | **TEK başına bile meşru ∧ kesin bir olumsuz bulgudur** — n=1'de bile geçerli, çünkü istatistiksel değil **doğruluk-temelli** |
| **6. Farklı model ailesini yargıç yap** | Üretici ile yargıcı **aynı aileden seçme** | Kendi-çıktısını-kayırma riskini azaltır | — | Mümkün değilse **confound'u raporda AÇIKÇA yaz** |
| **7. Süreç metriklerini LOGLA ama HÜKÜM VERME** | Araç çağrısı ∧ kaynak sayısı kaydet | — | — | **Q31: korelasyonu doğrulayan kaynak YOK.** *"Çok kaynak = iyi rapor"* hükmü **ÜRETME** |

### 4.4 ⭐ NE ÖLÇÜLEMEZ (bu ölçekte) — bu bölüm listenin en değerlisidir

**Q30** — MEŞRU OLMAYAN HÜKÜMLER
- **Stabil korelasyon katsayısı.** `n = 5..20` ⇒ hesaplanan herhangi bir `r` **gürültü ağırlıklıdır** ∧ **tek başına, güven aralığı olmadan raporlanmamalıdır.** *(AlpacaEval yazarları 9 modelle bile "güvenilmez" diyor.)*
  > **[K22 · antitez daraltması]** Eski hâli *"raporlanmamalıdır"* diyordu ⇒ **aşırı**. Küçük örneklemli korelasyon **bastırılmaz, güven aralığıyla birlikte raporlanır** — bu, pilot çalışma pratiğidir. Bastırmak, veriyi yok etmektir; **belirsizliğiyle birlikte yayımlamak** doğrusudur.
- **Genellenebilirlik.** *"Bu prompt öteki görev setinde de daha iyi olur"* ⇒ **TAŞINAMAZ**; geçerlilik yalnız kullanılan spesifik görev listesi + spesifik yargıç için iddia edilebilir.
- **Tek atımlık kesin verdikt.** `%69,2 insan_uyumu` bile **10 karardan ~3'ünde çoğunluk insan görüşünden SAPMA** demektir ⇒ bir kez `A > B` çıkması **hiçbir şey kanıtlamaz.**
- **Uzunluk/üslup etkisinden arındırılmış "gerçek kalite" farkı**, uzunluk kontrolü yapılmadan (Q25) ⇒ küçük n'de ayrıştırmak **mümkün değil**.
- **Süreç-metrik → sonuç-kalite korelasyonu** ⇒ **nedensel kanıt yoktur**; ⚠️ **korelasyonel kanıt VARDIR** (K23) — test zamanı hesaplama ölçekleme çalışmaları (pass@k, araç adım sayısı ↔ başarı) en azından korelasyonel kanıt sunuyor. *"Sıfır kanıt"* ifadesi **abartıydı**. Normatif sonuç (*"karar vermede kullanma"*) **ayakta kalır**, çünkü gerekçesi `korelasyon ≠ nedensellik`tir.
- **Self-enhancement bias'ın payı** ⇒ varlığı biliniyor, **miktarı ölçülmedi**.
- **`r≈0.31` iddiasının doğruluğu** ⇒ ne doğrulanabildi ne çürütülebildi (Q29).

### 4.5 Atıf doğruluğu — kendi işimize dokunan iki rakam

**Q31** ⊨K `[doğrulanamadı]`
`ticari_deep_research_ajanları → atıf_halüsinasyon_oranı ∈ [%11, %57]`
`atıf_doğruluğu → %78 (bir sistem) .. %94 (arama_destekli_Claude)` (n=100 PhD-düzeyi görev)
⚠️ Yazarların kendi uyarısı: mevcut benchmark'lar **atıflı URL'lerin GERÇEKTEN VAR OLUP OLMADIĞINI doğrulamıyor** ⇒ *"atıf doğruluğu" iddiaları bile kendi içinde eksik doğrulanmış.*
⚠️ Ham metin çekilemedi ⇒ rakamlar `[K]`.

**Q32** ⊨K — mevcut benchmark'lar **yalnız nihai çıktıya bakıyor**, araştırma sürecini (araç çağrısı, kaynak sayısı) **göz ardı ediyor**. Bu süreç metriklerinin sonuçla korelasyonuna dair **rakam bulunamadı** ⇒ Adım 7'nin gerekçesi.

### 4.6 A30 — İDDİA LİSTESİ · **ANTİTEZ KOŞTU, hükümler işlendi**

> ⚠️ **Üç iç tutarsızlık kabul edildi.** ① **Çifte standart:** ④ *"n=5-20'de herhangi bir korelasyon anlamsızdır"* derken, aynı rapor `%30-70`, `16×`, `~7×` gibi kesin rakamları **aynı şüphecilikle sorgulamıyordu**. ② **Aynı eşik iki yerde farklı:** ② tekrar örneklemeyi (**bir süreç müdahalesi**) meşruiyet artırıcı sayarken, ⑦ süreç metriklerini **toptan kanıtsız** ilan ediyordu. ③ **Mutlak niceleme:** ①, ③, ⑤, ⑥, ⑧'in hepsi *"her zaman"*, *"hiçbir"*, *"asla"*, *"bağımsız olarak"* içeriyordu ∧ hepsi **koşullu hâle geldi**.

① Pairwise karşılaştırma, `n=5..20`'de mutlak puanlamadan **genellikle** daha güvenilirdir. — **DARALDI:** *"her zaman"* düşer. **Objektif zeminli görevlerde** (birim testi, tam eşleşme) rubrik üstün olabilir; ayrıca pairwise, **ikisi de kötüyken sahte tercih dayatır**.
② Yargıcı 3 kez tekrar örneklemek, tek atımlıktan daha meşru hüküm verdirir — çünkü **rassal varyansı** azaltır.
   > **[K25 · antitez daraltması — önemli]** Tekrar örnekleme **rassal varyansı azaltır**; **sistematik yanlılığı AZALTMAZ**. Üç oy aynı yanlılığı paylaşıyorsa ortaya çıkan şey **sahte çoğulluktur** — üç kez ölçmek, üç kez aynı yöne sapmayı düzeltmez. ⇒ Bu yüzden ⑥ (farklı aile) ve Adım 5 (kanarya) **ikame değil, tamamlayıcıdır**.
③ **Uzunluk kontrolü yapılmadan** hiçbir win-rate farkı "kalite farkı" olarak yorumlanamaz. — **DARALDI** (mutlak niceleme); yönü korunur.
④ `n=5..20`'de hesaplanan korelasyon katsayısı **tek başına, güven aralığı olmadan raporlanmamalıdır**.
   > **[K22 · antitez daraltması]** Eski hâli *"raporlanmamalıdır"* diyordu ⇒ aşırı. Küçük N korelasyonu **bastırılmaz, güven aralığıyla raporlanır** (pilot çalışma pratiği).
   > ⚠️ Ve **çifte standart kabul edildi:** aynı şüphecilik raporun kendi kesin rakamlarına uygulanmıyordu.
⑤ Bilinen-cevap kanaryası tek başına geçerli bir test biçimidir. — **DARALDI** (*"örneklem büyüklüğünden bağımsız olarak"* mutlaklığı düşer); ama özü ayakta: **doğruluk temelli** olduğu için istatistik gerektirmez.
⑥ Aynı model ailesi hem üretici hem yargıçsa, ölçülen iyileşme **kendi kayırma yanlılığıyla kirlenmiş sayılmalıdır**. — **DARALDI** (mutlak niceleme); yönü korunur ∧ K25 ile **birlikte okunur**.
⑦ Süreç metrikleri karar vermede **kullanılmamalıdır** — çünkü **nedensel kanıt yoktur**.
   > **[K23 · antitez kısmi çürütmesi]** Eski hâli *"sıfır kanıt"* diyordu ⇒ **abartı**. Test zamanı hesaplama ölçekleme çalışmaları (pass@k, araç adım sayısı ↔ başarı) **en azından korelasyonel** kanıt sunuyor.
   > ⇒ **Normatif sonuç ayakta kalır**, çünkü gerekçesi `korelasyon ≠ nedensellik`tir — ama *"kanıt yok"* demek **yanlıştı**.
⑧ `n=1`'den çıkan *"bu prompt öncekinden iyi"* hükmü **derece farkı için** meşru değildir — en iyi ihtimalle yönsel izlenimdir.
   > **[K26 · antitez daraltması]** *"Asla meşru değildir"* **fazla güçlü**. **İkili ya da felaket türü farkta n=1 yeterlidir**: *"her seferinde çöküyor, bu düzeltme çözüyor"* mühendislik standardıdır. ⇒ Ayrım **derece farkı ↔ ikili fark**tır; kanarya maddesi (Adım 5) tam olarak bu istisnadan yararlanır.
⑨ Küçük ölçekte **Salih'in kendi yapılandırılmış kör okuması**, LLM yargıcının insan uyum oranından (`%69..85` bandı) **daha az güvenilir sayılamaz** ⇒ LLM yargıç Salih'in **yerine değil, yanına** konmalıdır. — **çürütülemedi**

---

## 5. ARA HÜKÜM — ana sıraya taşınacak

**Q16** — BRİFİNG KONTROL LİSTESİ (Q1–Q5 ∧ A29 dayanaklı, bugün uygulanabilir)

| # | Kural | Dayanak |
|---|---|---|
| **B1** | **Erişim haritasını brifinge YAZ, ama HİPOTEZ olarak işaretle.** Ajana brifingi ölçüp düzeltme yetkisi ver. | Q1, Q2 — *`denenmemiş ≢ açık`* |
| **B2** | **Kapalı kaynak için taktiği brifinge koy:** replikasyon deposu → upstream git → kaynak `.md/.rst`. | Q4 — dört kez karşılığını verdi |
| **B3** | **WebSearch'ü tayınla ∧ sessiz tükenişi ajana SÖYLE.** `boş_arama ≡ sayaç_dolu`, `≢ sonuç_yok`. | Q5 — yoksa negatif bulgu uydurulur |
| **B4** | **Bağlam bütçesi := etkin uzunluk.** Distractor-yoğun işte 2K-16K varsay, nominal pencereye güvenme. | Q6, Q7 |
| **B5** | **İzole bağlam ⊕ özet döngüsü.** Ajanlar birbirinin ham bulgusunu görmez. | Q13 |
| **B6** | **N'i MECE-ayrışabilirlik gerekçelendirsin**, "daha fazla ajan daha iyi" değil. | Q12, Q4-kuralı |
| **B7** | **"Bulunamadı" ile "aranamadı"yı ayırmayı brifinge ZORUNLU madde yap.** | A29 bunu yaptı ⇒ Q9-Q11 kurtarıldı |
| **B8** | **"Doğrulayamadığın rakamı verme" maddesi ZORUNLU.** | Q9-Q11 — ajan üç kez uydurabilirdi, uydurmadı |
| **B9** | **İskelet-önce (V69):** ilk bulguda kısa ara metin. | P135 — yalnız araç çağrısıyla kesilen ajanın işi **tamamen** kaybolur |

**Q17** — ⭐ BU AİLENİN EN GÜÇLÜ TEK BULGUSU
`brifing_maddesi ∈ {B7, B8}` ⇒ `maliyet = 2 cümle` ∧ `getiri = üç uydurulmuş rakamın önlenmesi`
⇒ **Prompt veriminin en yüksek getirili kolu, ajanın NE BİLMEDİĞİNİ söyleyebilmesini yapısal olarak mümkün kılmaktır.**
⇒ Ölçüm eklemek değil, **ölçememeyi raporlanabilir kılmak.**

**Q17b** — ⭐ VE MAST BUNU DIŞARIDAN DOĞRULUYOR (Q9b)
`en_büyük_başarısızlık_kategorisi = Poor_Specification (%37,17)`
⇒ **Brifing tasarımı, çok-ajan başarısızlığının BİRİNCİ kaynağıdır** — marjinal bir iyileştirme değil.
⇒ Salih'in *"araştırma promptlarımın verimini arttırmalıyız"* sezgisi, bağımsız bir ölçümle **doğrulanmıştır.**

**Q17c** — EK KURALLAR (A28 ∧ A30 dayanaklı)

| # | Kural | Dayanak |
|---|---|---|
| **B10** | **Persona/rol atamayı GEREKÇESİZ kullanma.** Etki göreve bağlı ∧ ölçülmüş çökme vakası var (Q16). Bizim ajanlarımıza "sen TEZ ajanısın" demek **rol değil GÖREV tanımıdır** — bu ayrım korunmalı. | Q15, Q16 |
| **B11** | **Katı format zorunluluğunun maliyetini KABUL ET ∧ ÖLÇ.** Şemayı bırakma (izlenebilirlik için gerekli) ama frontier modelde maliyetini D8 ile ölç. | Q18, Q19 |
| **B12** | **`[D/K/X]` etiketlemesinin gerekçesini DÜZELT.** *"Halüsinasyonu azaltır"* değil — **"iddianın kanıt seviyesini okuyucuya açık kılar."** Nedensel kanıt yok (Q22). | Q22 |
| **B13** | **Yargıç ≠ üretici aile.** Prompt karşılaştırmasında farklı model ailesi kullan; mümkün değilse confound'u **raporda yaz**. | Q26, A30-⑥ |
| **B14** | **Kanarya maddesi koy.** Her ölçüm setine cevabını bildiğin 1-2 soru — `n=1`'de bile meşru tek test. | A30 Adım 5 |
| **B15** | **Süreç metriklerini logla, hüküm kurma.** | Q32 |

---

## 6. AÇIK BORÇLAR

| # | Borç | Durum |
|---|---|---|
| D1 | ~~Antitez koşulmadı~~ → **KAPANDI 2026-07-26** | **Araçsız** koştu ⇒ 4 çürütme (K19, K20, K21, K23) · 4 daraltma (K22, K25, K26 + mutlak niceleme sınıfı) · 3 **iç tutarsızlık kabulü** (K24 + çifte standart + aynı eşiğin iki yerde farklı uygulanması) · 3 `⊨S`. Hükümler §2.5 · §3.7 · §4.6'ya işlendi |
| **D9** | ⭐ **Özetleme sadakati literatürü TARANMADI** (K19) | QAGS · SummaC · FactCC · LLMLingua. Bunu *"yok"* diye yazmıştık; **var ∧ taranmadı**. Erişim açık bir oturumda taranacak |
| **D10** | **Olumsuzlama duyarsızlığı literatürü TARANMADI** (K20) | Kassner & Schütze (ACL 2020) doğrudan ölçüyor. Aynı hata sınıfı |
| D2 | `lost-in-the-middle` U-eğrisi sayıları ∧ LLM-Monkeys ölçek eğrisi ∧ self-consistency düzleşmesi (Q11c) | Erişim açık bir oturumda |
| D3 | Anthropic çok-ajan mühendislik yazısı (403) | Muhtemelen shared-vs-isolated bağlam karşılaştırmasını içeriyordu — **bu ailenin en hedefli kayıp kaynağı** |
| D4 | `"Let Me Speak Freely?"` ∧ persona `~30 puan` rakamları (Q17, Q19) | Birincil metne erişilemedi |
| D5 | MT-Bench'in `~%85` insan uyumu (Q28) ∧ `r≈0.31`'in kaynağı (Q29) | **İkisi de doğrulanamadı** ⇒ hüküm AÇIK |
| D6 | `"More Agents Is All You Need"` ölçek eğrisi (Q11b) | Statü `aranamadı → bulunamadı`; repo erişildi, **sayı yok** |
| **D7** | **Negatif vs pozitif talimat ekseni** | `[ARANAMADI]` — bütçe tükendi ∧ tahmin edilebilir repo adı yoktu |
| **D8** | ⭐ **Kendi şemamızın maliyeti frontier modelde ölçülmedi** | Q18 zayıf modelde ölçüldü. **A30 protokolüyle test edilebilecek İLK somut hipotez** |

---

## 7. FİKİR KUTUSU ADAYLARI

- **V72 — Brifing = hipotez.** Ajana verilen erişim haritası doğrulanmamış öncüldür; ajan onu ölçüp düzeltmekle **yükümlü** kılınmalı. Q1'in maliyeti, Q2'nin getirisi. *(Bu koşumda üç kez karşılığını verdi: A30 proxy'yi ölçtü · A29 dal adını buldu · A31 on bir yeni kapalı alan haritaladı.)*
- **V73 — ⭐⭐ "Aranamadı" etiketi — GEREKÇESİ ANTİTEZLE GÜÇLENDİ.** `[D/K/X]` ailesine dördüncü etiket: **`⊨A` = aranamadı** (bütçe/erişim nedeniyle sorgulanamadı). Şu an bu durum `bulunamadı` içinde eriyor ∧ **negatif bulgu enflasyonu** yaratıyor.
  **Artık dört bağımsız gerekçesi var:** ① bu koşumda üç ajan ayrımı **elle** yaptı ∧ üçü de değer üretti · ② **K19** — özetleme kaybı literatürünü *"yok"* yazmıştık, **var** · ③ **K20** — olumsuzlama literatürünü *"yok"* yazmıştık, **var** · ④ A31'in kendi dürüstlük kaydı: *"erişim engeli ile gerçek yokluk ayırt edilemiyor, ve bu ayrımsızlığın kendisi rapor edilmesi gereken bir bulgudur."*
  ⇒ **Bu, oturumun en çok bağımsız gerekçe biriktiren tek önerisidir. Salih kararı (S2).**
- **V74 — Etkin uzunluk tablosu kanona.** Q6/Q7 tabloları KILAVUZ'a girip bağlam bütçelemesinin sayısal dayanağı olmaya aday.
- **V75 — MAST kontrol listesi.** Q9b'nin 14 başarısızlık modu, ajan brifingi yazarken **doğrudan kontrol listesi** olarak kullanılabilir — özellikle `sonlanma_koşullarından_habersizlik (%6,54)` ∧ `adım_tekrarı (%11,5)` ∧ `bilgi_saklama (%6,02)`, hepsi brifingle önlenebilir sınıflar.

---

## 8. KAPANIŞ DAMGASI

**Aile:** A28 · A29 (+delta) · A30 — **antitez KOŞTU** (2026-07-26, **araçsız**, `tool_uses = 0`)
**Antitez sonucu:** 4 çürütme (K19 özetleme · K20 olumsuzlama · K21 sistematik · K23 sıfır kanıt) · 4 daraltma (K22, K25, K26 + mutlak niceleme sınıfı) · **3 iç tutarsızlık kabulü** (K24 + çifte standart + aynı eşiğin iki yerde farklı uygulanması) · 3 `⊨S`
**⚠️ İki şerh:** ① Araçsız tur ⇒ **mantıksal** saldırılar tam güçte, **olgusal karşı-örnekler `[K-hatırlama]`** ∧ borç açar. ② `⊨S` = **"aynı-aile hakemi karşısında sağ kaldı"**.
**Kanıt tabanı:** `[D]` ağırlıklı — RULER ∧ NoLiMa ∧ MAST taksonomi figürü ∧ AlpacaEval ∧ Arena-Hard replikasyon depoları ∧ ürün dokümanlarının ham markdown'ı
**Register:** tam önerme formu (P144); insan-yüzü iki register sonraki emirle **üretildi** ∧ karar kaynağı **değildir**
**⭐ En ağır ders:** bu ailenin **en güçlü tek bulgusu** *"ajanın ne bilmediğini söyleyebilmesini yapısal olarak mümkün kıl"*tı (Q17) — ve antitez, **bu raporun kendisinin iki yerde bunu yapamadığını** gösterdi (K19, K20). Kural doğruydu; **uygulayan biz değildik**.

**▲ Bu raporun kendi zayıflıkları — beyan edilir:**
1. ~~`antitez = ∅`~~ ⇒ **koştu.** Yeni beyan: **iki yokluk iddiamız yanlış çıktı** (K19, K20) ∧ ikisi de *"aranamadı"*yı *"yok"* diye yazmaktan kaynaklandı — yani **raporun kendi B7 kuralının ihlali**.
2. `D8` ⇒ raporun kendi tavsiye ettiği şema, **kendi ölçüm protokolüyle henüz test edilmedi.** Yani bu rapor, uygulanmasını önerdiği ölçümü **kendine uygulamamıştır.**
3. `Q29` ⇒ oturumun başında verdiğim bir düzeltme, **bu ailede yeniden açıldı.** Kapanmış sayılmıyor.
4. `Q23` ⇒ uzunluk ekseninin tek güçlü kanıtı **dolaylıdır** (haystack ≠ brifing uzunluğu). Analoji olarak işaretlendi.
