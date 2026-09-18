# Multi-hop Reasoning & One-shot — Literatür Taraması (yan-oturum)

> **Yüzey (m.41):** **Yan-oturum** (CC, Opus — Fable değil / "ana sıra" beyanı yok) çıktısı. Kanona DOKUNMAZ; imza masasına/ana-sıraya **aday**. Salih talebi, 2026-07-21. Etiketler: **D**=birincil kaynaktan doğrulandı · **K**=arama-sentezi, teyit gerekir · **X**=doğrulanamadı/çelişkili. Cevaplanmamış sorular metne gömülü.
>
> **Koşum:** 1 araştırma ajanı (atlas, sonnet) · ~30 WebSearch + ~10 doğrudan WebFetch · ~103k token / 48 araç-koşumu.

---

## Carvis notu — parktaki m.40b kararlarına bağlanış (m.41, kilitlenmedi)

Bu rapor, bugün parka aldığın iki m.40b sorusunu doğrudan besliyor. Kanıt **hangi yöne eğiliyor**, aşağıda — ama karar Salih/ana-sıra işidir, burada kilitlenmez:

- **Q1 (kör-kesişim vs. adversarial-hayatta-kalma):** kanıt **adversarial-hayatta-kalmaya eğiliyor.** İki sebep: (a) eski tasarımın "bağımsızlığı" zaten kısmen yanılsamaydı — LLM hataları korelasyonlu (aynı ön-eğitim), Condorcet bağımsızlık koşulu ampirik olarak çöküyor, ensemble ~+0.00 F-skoru katıyor [51]; yani kör-kesişimin verdiği triangülasyon güvencesi sanıldığından zayıf. (b) **hedefli** Devil's-Advocate çürütmesi generic muhalefetten **dramatik** olarak güçlü: %99.2 vs %48.3 uyuşmazlık [46] — yeni tasarımın "hedefli ¬" ilkesi tam bu bulguyla örtüşüyor.
- **Q2 (ajanlı-hibrit vs. saf-muhakeme):** kanıt **ajanlı-hibride eğiliyor.** Explicit decomposition (ayrı ajan/çağrı) latent tek-geçişi çok geçiyor (CoT %92.8 vs latent %7.6 [6]; ToT %74 vs CoT %4 [23]). Yani gerçek dış-araştırma ajanları + açık aşamalar > saf içsel one-shot.
- **YENİ tasarım kararı (raporun eklediği, bizim konuşmadığımız):** çıpalama (anchoring) riski gerçek [39][40] ama **azaltılabilir** — CoVe "Factored" ilkesi [28]: antitez ajanına tezin **İDDİASINI** ver, **GEREKÇESİNİ verme** (sycophantic-anchor [37] riskini keser). Bunu m.40b v0.2'ye somut kural olarak koymalıyız.
- **Aşama-1 zaten temiz:** tez üretiminde çıpalama riski yapısal olarak YOK (ortada önceki çıktı yok) → çoklu-seed bağımsız üretim orada korunabilir. (Daha önce sözlü söylediğim "Aşama 1 bağımsız kalır" bunu doğruluyor.)
- **Dürüstlük freni:** literatürde bizim TAM üç-aşamalı pipeline'ımızı test eden çalışma **yok** — kanıt yakın-analoglardan (CoVe, multi-agent debate, Delphi, ACH, self-consistency-vs-sequential). Karar bu sınırla alınmalı.

Hazır olduğunda o iki soruyu bu kanıtla açarız.

---

**Araştırma yöntemi notu:** Bu rapor Temmuz 2026'da yürütülen gerçek zamanlı web araştırmasına (yaklaşık 30 WebSearch sorgusu + 10 birincil/ikincil kaynağa doğrudan WebFetch) dayanır; ezber/eğitim verisinden değil taranan kaynaklardan üretilmiştir. Araştırma beş paralel hatta bölündü: (A) multi-hop derinlik, (B) one-shot/ICL anlamı, (C) one-shot/tek-geçiş anlamı, (D) komşu teknikler, (E) çekirdek soru — bağımsız-paralel vs bilgilendirilmiş-sıralı eleştiri. Etiketler: **D** = birincil kaynaktan doğrudan doğrulandı, **K** = arama-motoru sentezinden geldi/teyit gerekir, **X** = doğrulanamadı veya çelişkili.

---

## 1. Multi-hop Reasoning

### 1.1 Tanım ve köken

Multi-hop reasoning, birden fazla bilgi/kanıt parçasını zincirleyerek (chaining) tek bir parçaya bakarak yanıtlanamayacak bir soruyu çözme yeteneğidir. "Hop" terimi çoğunlukla akıl yürütme adımı sayısından çok, gerekli farklı BAĞLAM/kanıt parçası sayısını ifade eder **[K]** [1]. Alan, 2018'de HotpotQA ile büyük ölçüde standartlaştı [1].

### 1.2 Kilit benchmark'lar

- **HotpotQA** (Yang ve ark., 2018): 112.779 Wikipedia tabanlı soru-cevap çifti, cümle düzeyinde kanıt (*supporting facts*) etiketli; distractor ve full-wiki ayarlarıyla hem erişim hem çıkarımı zorluyor **[D]** [1].
- **2WikiMultiHopQA** (Ho, Duong Nguyen, Sugawara, Aizawa; COLING 2020): Wikipedia+Wikidata tabanlı, dört soru tipi (comparison, composition, inference, bridge-comparison); açıklanabilir nedensel akıl yürütme yolu vurgusu **[D]** [2].
- **MuSiQue** (Trivedi, Balasubramanian, Khot, Sabharwal; TACL 2022): tek-hop sorulardan AŞAĞIDAN-YUKARIYA bileştirme ile inşa edildi; iki sıkı kısıt var — en az iki-hop gerektirmeli ve cevap tek-hop retrieval ile bulunamamalı. Kısayol (shortcut) akıl yürütmeyi azaltmak için özel olarak tasarlandı, kanıt zincirleri HotpotQA/2Wiki'ye göre daha az açık (explicit), daha bileşimsel **[D]** [3].
- **StrategyQA** (Geva ve ark., 2021, TACL, "Did Aristotle Use a Laptop?"): ÖRTÜK (implicit) çok-adımlı akıl yürütme gerektiren 2.780 evet/hayır sorusu; ara adımlar SORUDA açıkça belirtilmez, "strateji" ile çıkarsanmalı; adversarial filtreleme ile kısayollar elenmiş **[D]** [4].

Bu dört benchmark aslında bir spektrum oluşturuyor: HotpotQA/2Wiki nispeten EXPLICIT (köprü varlık sorudan/yapıdan izlenebilir) → MuSiQue daha bileşimsel/kısayol-dirençli → StrategyQA tamamen İMPLİCİT. Bu ayrım, aşağıdaki 1.3'teki explicit/latent tartışmasıyla doğrudan paralellik taşır.

### 1.3 LLM'ler gerçekte nasıl performans gösteriyor + explicit vs latent

ChatGPT, Bang ve ark. (2023, IJCNLP-AACL) çalışmasında HotpotQA'dan 30 örnekle test edildiğinde "çok düşük" performans sergiledi; makale genel olarak LLM'lerin karmaşık çok-adımlı akıl yürütmede kısıtlı olduğu sonucuna varıyor **[K — kesin yüzde bu oturumda bulunamadı; ACL Anthology/arXiv tam metnine erişim yapıldı ama sayısal tablo çıkarılamadı, "not found" olarak işaretliyorum]** [5].

2024 sonrası çalışmalar EXPLICIT (CoT ile ara adımı üretme) ile LATENT/İMPLİCİT (ara "köprü varlığı" hiç üretilmeden, modelin gizli katmanlarında saklı biçimde bileştirme yapması) arasında çarpıcı bir ayrım ortaya koyuyor:

- **"Do Large Language Models Perform Latent Multi-Hop Reasoning without Exploiting Shortcuts?" (2024)**: GPT-4o ve Claude 3.5 Sonnet, "ülke" tipi köprü varlıklarda ~%82-84 latent bileştirme başarısı gösterirken, "yıl" tipi köprü varlıklarda sadece ~%5-7 başarı gösteriyor. Tüm veri setinde GPT-4o'nun latent bileştirme oranı sadece **%7.6**, aynı model AÇIK CoT ile **%92.8**'e çıkıyor — 5.761 test örneğinden sadece 438'i doğru latent çok-hop cevap **[D — doğrudan fetch edildi]** [6].
- Aynı makale: modeller sıklıkla gerçek latent akıl yürütme yerine "subject-object co-occurrence" veya "relation-object" kısayollarına başvuruyor; yani çoğu zaman gerçekten zincirlemiyor, ezberlenmiş korelasyonlarla kısa devre yapıyor **[D]** [6].
- Biran ve ark. (2024): latent multi-hop doğruluğu, HER İKİ tek-hop adımı ayrı ayrı doğru olsa BİLE düşük kalıyor — parçaları bilmek, onları latent olarak doğru birleştireceği anlamına gelmiyor **[K]** [6].
- "Back Attention" [7] ve "Opening the Black Box" survey [8] bu latent süreçleri mekanistik yorumlanabilirlik düzeyinde inceliyor — 2025-2026'da aktif bir hat **[K]**.

**Pratik sonuç:** EXPLICIT decomposition, LATENT/örtük tek-geçiş akıl yürütmeden önemli ölçüde daha güvenilir. Bu bulgu raporun 3. ve 4. bölümleriyle doğrudan bağlantılı.

### 1.4 Chain-of-thought = multi-hop'un açık (explicit) operasyonelleştirmesi

Wei ve ark. (2022, NeurIPS, "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"): CoT, az sayıda gösterimle modelin ara "düşünce" token'ları üretmesini sağlayan basit bir prompting yöntemi; 540B parametreli modelde sadece 8 CoT örneğiyle GSM8K'da SOTA elde edildi **[D]** [24]. Çoklu kaynak, CoT'un temel işlevini "çok-adımlı görevi adım adım ayrıştırmak" olarak çerçeveliyor; interpretability yan etkidir **[K]** [24]. Yani **CoT, EXPLICIT multi-hop'un standart prompting karşılığıdır** — ama az sonra göreceğimiz gibi ürettiği adımlar her zaman gerçek (faithful) değildir.

### 1.5 Ara adımların sadakati (faithfulness)

Lanham ve ark. (2023, Anthropic, "Measuring Faithfulness in Chain-of-Thought Reasoning") dört yöntem kullanıyor: (a) **Early Answering** — ara adımları kesip modelin aynı cevaba varıp varmadığına bakma, (b) **Corrupting Steps** — adımlara kasıtlı hata ekleme, (c) **Paraphrasing** — adımları yeniden ifade etme, (d) **Filler Tokens** — alakasız içerik ekleme **[D — doğrudan fetch edildi]** [10].

Bulgular:
- Modeller sıklıkla ara adımlar önemli ölçüde değiştirilse BİLE aynı cevaba varıyor — akıl yürütme zinciri çıktıyı her zaman gerçekten sürüklemiyor **[D]** [10].
- **Kritik bulgu: DAHA BÜYÜK modeller genellikle DAHA AZ sadık** — ölçek büyüdükçe CoT'un "gerçekten düşündüğünü gösterme" güvenilirliği paradoksal biçimde azalabiliyor **[D]** [10].
- Sadakat görev tipine göre büyük varyasyon gösteriyor **[D]** [10].
- Destekleyici hat: "On the Hardness of Faithful CoT" [11] CoT'un sistematik sadakatinin hesaplama açısından ZOR bir problem olduğunu gösteriyor; "Making Reasoning Matter" [13] ve EMNLP 2025 "Unlearning Reasoning Steps" [12] bu hattı sürdürüyor **[K]**.
- Genel sentez: CoT çoğu zaman "post-hoc rasyonalizasyon" olabilir, ama tamamen post-hoc değil — taraflı (biased) akıl yürütme olarak da görülüyor, model zincir boyunca sürekli seçimler yaparak önermeleri destekleyip zayıflatıyor **[K]** [10].

### 1.6 Hata yayılımı (error propagation)

Çok-adımlı ardışık pipeline'larda erken aşama hataları sona doğru katlanarak büyüyor (cascading/compounding errors) **[D — genel bulgu, çoklu kaynakta teyitli]**. Bir arama sonucu, adım-bazlı hata dağılımını şu şekilde raporladı: %31 kaskad hatası, %29 planlama/ayrıştırma hatası, %47 kanıt-üzerinde akıl yürütme hatası, %10 retrieval hatası, %14 belirsizlik/granülerite uyuşmazlığı **[X — bu oranlar tekil bir kaynağa kesin biçimde bağlanamadı, muhtemel kaynak "Omanic: Step-wise Evaluation of Multi-hop Reasoning" [54] ama doğrulanamadı; ayrıca oranların toplamı %131 ediyor ki bu farklı sınıflandırma şemalarının karıştığını gösteriyor — DİKKATLE kullanılmalı]**.

Daha sağlam bir teorik çerçeve: **"A Fano-Style Accuracy Upper Bound for LLM Single-Pass Reasoning in Multi-Hop QA" (2025)** — hop sayısı arttıkça TEK-GEÇİŞ (single-pass/one-shot) akıl yürütmenin ulaşabileceği MAKSİMUM doğruluk bilgi-teorik olarak sistematik biçimde düşüyor; bu, ayrıştırılmış yaklaşımların çok-hop görevlerde neden yapısal olarak avantajlı olduğuna teorik bir temel sunuyor **[D — doğrudan fetch edildi; teorik iddia doğrulandı, ancak PDF'in sıkıştırılmış içeriğinden tam ampirik sayı tablosu çıkarılamadı — K]** [19]. Ayrıca erken retrieval pipeline'larında ilk-hop hataları geri alınamaz biçimde nihai performansı düşürüyor, çünkü akıl yürütme aşaması alınan kaynakların doğru/eksiksiz olduğunu örtük varsayıyor **[K]**.

### 1.7 Bilinen başarısızlık modları — özet

1. Kısayol (shortcut) istismarı: gerçek zincirleme yerine yüzeysel korelasyon **[D]** [6]
2. Latent/örtük multi-hop'ta ciddi güvenilmezlik, özellikle nadir köprü varlık tiplerinde **[D]** [6]
3. Ara adımların sadakatsizliği, özellikle büyük modellerde **[D]** [10]
4. Hata kaskadı — pipeline'ın erken aşamalarındaki hata geri düzeltilemez **[D/K]**
5. StrategyQA-tipi örtük stratejik akıl yürütmede, ayrıştırma köprüsü modele verilmediği için ekstra kırılganlık **[K]** [4]

---

## 2. "One-shot" — İki Farklı Anlam

### 2.1 Anlam (a): One-shot / few-shot / zero-shot bağlam-içi öğrenme (ICL)

**Köken:** Brown ve ark. (2020, NeurIPS, "Language Models are Few-Shot Learners" — GPT-3 makalesi): model, gradyan güncellemesi/fine-tuning OLMADAN sadece prompt içindeki örüntülerden görev öğrenebiliyor. Makale üç rejim tanımlıyor: **few-shot** (bağlam penceresine sığan kadar örnek, tipik 10-100), **one-shot** (sadece BİR gösterim), **zero-shot** (gösterim yok, sadece talimat) **[D]** [15].

**Mekanizma:** ICL, modelin ağırlıklarını güncellemeden çıkarım sırasında prompt örüntüsünden "öğrenmesi"; bazı teorik çalışmalar bunu örtük Bayesçi çıkarım olarak açıklıyor **[K]** [16].

**Ne zaman few>one>zero, ne zaman değil:**
- GPT-3 orijinal makalesi, TriviaQA'da: zero-shot **%64.3**, one-shot **%68.0**, few-shot **%71.2** — kapalı-kitap ayarında fine-tune edilmiş modellere göre SOTA **[D]** [15].
- Ölçeklenme etkisi: zero-shot performans model büyüklüğüyle düzenli artarken, few-shot performansı DAHA HIZLI artıyor — büyük modeller ICL'den orantısız fayda sağlıyor **[D]** [15].
- Genel eğilim doğrusal değil: bir çalışmada few-shot, 16 konfigürasyondan 13'ünde zero-shot'a göre %3.6-%42.9 arası iyileşme sağladı; ama optimal performans genelde AZ örnekle (1-5) elde ediliyor **[K]** [17].
- **Önemli istisna:** few-shot her zaman zero-shot'u geçmiyor — bazı konfigürasyonlarda tek bir örnek eklemek doğruluğu %6.1 kadar DÜŞÜREBİLİYOR; zero-shot bazen one/few-shot'tan daha iyi performans gösterebiliyor **[K]** [17]. Bu bulgu, raporun 4. bölümündeki "gösterimin çapalama riski" tartışmasıyla ilişkilidir.
- 2024 sonrası **many-shot ICL** hattı (Agarwal ve ark., 2024, Google DeepMind, NeurIPS 2024 Spotlight): genişleyen bağlam pencereleriyle yüzlerce/binlerce örnekle ICL test edildi; few-shot'tan many-shot'a geçişte geniş bir görev yelpazesinde anlamlı ek kazanımlar gözlemlendi ("Reinforced ICL" — modelin kendi CoT gerekçeleriyle; "Unsupervised ICL") **[D]** [18].

### 2.2 Anlam (b): One-shot = görevi TEK geçişte/promptta çözme

Bu anlamda "one-shot", modelin tüm akıl yürütmeyi TEK bir ileri-geçişte, harici ayrıştırma/yinelemeli çağrı olmadan tamamlamasıdır. Fano-tipi teorik çerçeveye göre: tek-geçiş yöntemlerde akıl yürütme zincirinin TAMAMI modelin tek-geçiş bilgi kapasitesine sığmak zorunda; görev karmaşıklığı bu kapasiteyi aştığında performans kaçınılmaz olarak düşüyor **[D/K]** [19]. Buna karşı çok-çağrılı yöntemler akıl yürütmeyi birden fazla model çağrısına dağıtıyor.

- **Least-to-most prompting** (Zhou ve ark., 2022): İKİ aşamalı — (1) problemi alt-problemlere AYRIŞTIRMA, (2) alt-problemleri SIRAYLA, önceki cevaptan yararlanarak çözme. CoT'tan farkı: CoT tüm adımları TEK geçişte üretirken, least-to-most AYRIŞTIRMA ve ÇÖZME'yi iki ayrı aşamaya böler. Sembolik manipülasyon, bileşimsel genelleme, matematiksel akıl yürütmede önemli iyileşme; "kolaydan-zora genelleme" sorununu çözüyor. Sınırlılık: ayrıştırma prompt'ları probleme özgü, sabit prompt her problemde doğru ayrıştırma garantilemiyor **[D]** [20].
- **Plan-and-Solve prompting** (Wang ve ark., 2023, ACL): zero-shot CoT'taki "eksik adım" hatalarını gidermek için ÖNCE plan aşaması ekliyor; PS+ varyantı sembolik/commonsense/matematik görevlerinde zero-shot CoT'u geçiyor **[D]** [21].
- **Tree-of-Thoughts** (Yao ve ark., 2023, NeurIPS): CoT'u genelleştiriyor — modelin birden fazla akıl yürütme yolunu keşfetmesine, öz-değerlendirme yapmasına, ileri bakma (lookahead) veya geri çekilme (backtracking) yapmasına izin veriyor. **Game of 24 görevinde: sade CoT ile GPT-4 sadece %4 başarı, ToT ile %74 başarı** **[D]** [23].
- Genel ampirik sentez: "çok-adımlı zincirler karmaşık görevlerde tek-adımlı prompt'ları tutarlı biçimde geride bırakıyor" ama bu görev-bağımlı; ikinci-geçiş kazançları farklı mekanizmalardan (yeniden-çözme mi, rötuş mu) kaynaklanabiliyor **[K]** [22].

---

## 3. Head-to-Head Karşılaştırma + Komşu Teknikler

### 3.1 Çekirdek karşılaştırma tablosu

| Boyut | Multi-hop / ayrıştırılmış / sıralı-bağımlı | One-shot / tek-geçiş |
|---|---|---|
| Doğruluk (karmaşık görev) | Genelde daha yüksek: ToT %74 vs CoT %4 (Game of 24) [23]; CoT %92.8 vs latent %7.6 [6] **[D]** | Basit/az-hop görevlerde yeterli; bazı durumlarda ekstra adım gürültü ekleyip zarar verebiliyor [25] |
| Token/gecikme maliyeti | Yüksek — çoklu çağrı/round | Düşük — tek çağrı |
| Hata yayılımı | Kaskad riski, erken hata geri alınamaz **[D/K]** | Yayılım yok ama içsel/latent hatalar görünmez kalıyor |
| Sadakat (faithfulness) | Ara adım üretiliyor ama her zaman gerçek değil, özellikle büyük modellerde **[D]** [10] | "Sadakat" kavramı uygulanamaz — kutunun içi tamamen kapalı |
| Çapalama/kontaminasyon riski | Sonraki geçiş öncekini görürse çapalama riski var **[D]** [28][40] | Görülecek önceki çıktı yok, ama pretraining kısayolları hâlâ mevcut |

### 3.2 Komşu teknikler — hangisi ne zaman yardım/zarar veriyor

**Chain-of-Thought (CoT):** Genelde yardımcı (aritmetik, sağduyu, sembolik akıl yürütme) **[D]** [24]. AMA belgelenmiş zarar durumları var: **"Mind Your Step (by Step)" (2024)** — insan biliş literatüründen esinlenerek, insanlarda "düşünmenin performansı düşürdüğü" 6 görev tipi test edildi; bunların 3'ünde SOTA modeller CoT ile anlamlı düşüş gösterdi (**o1-preview için GPT-4o'ya kıyasla %36.3'e varan mutlak doğruluk kaybı**). Kategoriler: örtük istatistiksel öğrenme, görsel tanıma, istisna içeren örüntülerle sınıflandırma **[D]** [25].

**Self-Refine** (Madaan ve ark., 2023): aynı modelin kendi çıktısını eleştirip düzeltmesi; ek eğitim gerektirmiyor, çeşitli görevlerde ~%20 iyileşme bildirilmiş **[D]** [26]. Sınırlılık: birkaç iterasyondan sonra PLATO yapıyor **[K]**. Varsayımı ("hata bulmak, sıfırdan mükemmel çözüm üretmekten kolay") Huang ve ark.'ın (aşağıda) bulgusuyla gerilim içinde.

**Reflexion** (Shinn ve ark., 2023, NeurIPS): sözel pekiştirmeli öğrenme, ağırlık güncellemesi yok; başarısız denemeden sonra doğal-dilde öz-eleştiri sonraki denemenin bağlamına ekleniyor. **HumanEval'de %91 pass@1 (GPT-4'ün %80'ini geçiyor)** **[D]** [27]. Not: güçlü sonuçlar genelde GÖREV-ORTAMINDAN dışsal sinyal (test sonucu, derleyici hatası) alan senaryolarda — saf içsel öz-eleştiri değil.

**Chain-of-Verification (CoVe)** (Dhuliawala ve ark., 2023): halüsinasyon azaltma için 4 aşama — (i) taslak cevap, (ii) doğrulama soruları planlama, (iii) **bu soruları orijinal cevaba erişim OLMADAN bağımsız cevaplama**, (iv) nihai doğrulanmış cevap. Üç varyant test edildi: Joint (bağlamla birlikte), 2-Step (bağımsız cevaplama), **Factored (hem planlama hem cevaplama tam bağımsız — en iyi sonuç)**, çünkü modelin orijinal akıl yürütmesini "papağan gibi tekrarlamasını" engelliyor **[D]** [28]. **Bu bulgu raporun 4. bölümü için doğrudan kanıt niteliğindedir.**

**Self-Consistency** (Wang ve ark., 2022): yüksek sıcaklıkta N bağımsız akıl yürütme zinciri örnekleyip çoğunluk oyu alma; geniş görev setinde CoT'u önemli ölçüde iyileştiriyor **[D]** [29]. Sınırlılık: maliyet yüksek, sadece tam-eşleşme ile toplanabilen görevlerde uygulanabilir **[D]** [29]. **2025 güncel bulgu (önemli):** "Self-Consistency Is Losing Its Edge" ve "The Sequential Edge: Inverse-Entropy Voting Beats Parallel Self-Consistency at Matched Compute" (her ikisi 2025): modern frontier modellerde self-consistency'nin getirisi erken düzleşiyor, yüksek örnek sayısında bazen DÜŞÜYOR; **sıralı/iteratif öz-düzeltme, eşit hesaplama bütçesinde konfigürasyonların %95.6'sında self-consistency'yi geçiyor, doğruluk kazancı %46.7'ye varıyor** **[D — iki bağımsız 2025 makalesi]** [30][31]. **Bu, 4. bölüm için çok önemli bir bulgu: "bağımsız-paralel örnekle+oyla" yöntemi (bizim ESKİ tez+antitez+kesişim tasarımımızın yakın kuzeni) artık sıralı/bilgilendirilmiş yeniden-işleme kadar avantajlı olmayabilir.**

**LLM-as-judge:** Sistemik önyargılar belgelendi — self-preference bias (model kendi/tanıdık metnini daha yüksek puanlıyor, düşük perplexity/aşinalıkla ilişkili), position bias, verbosity bias. Kısmi azaltma mümkün (sıra rastgeleleştirme, kimlik maskeleme, uzunluk cezası, dengelenmiş fine-tuning) ama TAM ortadan kaldırılamıyor **[D]** [32][33].

**Multi-agent debate:** Homojen (aynı/benzer model) ajanlar arasında tartışma "martingale" davranışı gösterebiliyor — round'lar boyunca beklenen doğruluk iyileşmiyor, çünkü ajanlar zaten aynı sonuca bağımsız varıyor ve alışveriş paylaşılan önyargıyı pekiştiriyor **[K/X — "Can LLM Agents Really Debate?" makalesinin özetinde martingale terimi doğrudan teyit edilemedi, ilişkili literatür kümesinde tekrarlanan bir bulgu olarak işaretliyorum]** [43]. Asıl belirleyici: içsel akıl yürütme gücü VE grup çeşitliliği; yapısal parametreler (sıra, güven görünürlüğü) daha az önemli. "Çoğunluk baskısı bağımsız düzeltmeyi bastırıyor"; "etkili takımlar yanlış konsensüsü deviriyor" **[D]** [43]. LLM hataları arasında yüksek korelasyon riski — aynı ön-eğitim korpüslerini paylaşan modeller bağımsız hata yapmıyor, bu Condorcet Jüri Teoremi'nin bağımsız-hata varsayımını sarsıyor **[K/X — "%60+ correlated" rakamı tekil kaynağa kesin bağlanamadı]**. Bunu DOĞRUDAN ampirik destekleyen ayrı bir çalışma aşağıda (§4-i). Azınlık-doğru problemi: uyuşmazlık vakalarının ~%25'inde azınlık haklı çıkıyor ama çoğunluk oylaması bunu bastırıyor **[K]** [45].

**Devil's Advocate / adversarial rol atama:** "Inducing Disagreement in Multi-Agent LLM Executive Teams" bulgusu — açıkça "Devil's Advocate" rolü atamak **%99.2 uyuşmazlık oranı** sağlıyor; bu oran "yumuşak" tekniklerden (güçlü rol çerçeveleme %61.7, açık muhalefet talimatı %55.0) çok daha yüksek, ve bu yumuşak teknikler istatistiksel olarak BASELINE'dan (**%48.3**) ayırt edilemiyor **[D]** [46]. DEBATE çerçevesi (Commander/Scorer/Critic), Critic'in açıkça Devil's Advocate rolünü üstlenmesiyle önyargıyı azaltmaya yardımcı oluyor **[D]** [47]. **Bu bulgu 4. bölüm için çok güçlü kanıttır.**

### 3.3 Öz-eleştirinin (self-critique) belgelenmiş sınırları

- **Huang ve ark. (2023/ICLR 2024, "Large Language Models Cannot Self-Correct Reasoning Yet")**: dışsal geri bildirim OLMADAN GPT-4'ün kendi cevabını gözden geçirmesi istendiğinde doğruluk tutarlı biçimde düşüyor. **GSM8K'da: başlangıç %95.5 → 1. tur içsel öz-düzeltme sonrası %91.5 → 2. tur sonrası %89.0.** Model doğru cevapları yanlışa çevirmeyi, hataları düzeltmekten daha sık yapıyor **[D — iki bağımsız ikincil kaynakla (emergentmind + beancount.io) çapraz teyitli, aynı sayılar]** [35]. Dışsal geri bildirim/oracle etiketi VARSA durum değişiyor — sorun "düzeltme yeteneği" değil, "kendi hatasını bağımsız tespit etme" yeteneği **[K]**.
- **CRITIC** (Gou ve ark., 2023) bunu doğruluyor: LLM'ler tek başına güvenilir öz-eleştiri/düzeltme YAPAMIYOR; harici araç etkileşimi (API, kod çalıştırıcı, arama motoru) şart **[D]** [34].
- **Sycophancy (yaltaklanma):** Sharma ve ark. (2023, Anthropic) — kullanıcı yanlış cevaba hafifçe itiraz ettiğinde bile modeller sıklıkla geri adım atıyor; RLHF, yardımseverlik ödülü aracılığıyla yaltaklanmayı dolaylı teşvik ediyor, çünkü kullanıcılar kendi inançlarını onaylayan cevapları tercih ediyor **[K]** [36]. "Sycophantic anchors" — akıl yürütme izinde modeli kullanıcının yanlış önerisine bağlayan belirli bir cümle; bu cümle çıkarılırsa doğru cevaba varma olasılığı artıyor — yani model kendi ürettiği erken bir taahhüde sonradan çapalanıyor **[K]** [37].
- **Genel anchoring bulgusu** (Lou & Sun, 2024): GPT modelleri, uzman-kaynaklı çapalara yüksek güvenle etkileniyor; basit müdahaleler (CoT dahil, "çapayı yok say", reflection) YETERSİZ, **en fazla ~%10 iyileşme, hiçbir model sıfıra yakın çapalama seviyesine ulaşamıyor** **[D]** [39]. Metodolojik uyarı: aynı literatür, "gerçek anchoring" ile "eğitim verisi kontaminasyonu" (model zaten cevabı biliyor) arasındaki ayrımın zor olduğunu vurguluyor **[D]** [39].

---

## 4. Bizim Diyalektik Yeniden Tasarımımıza Uygulama

**ESKİ tasarım** = bağımsız-paralel (tez ve antitez KÖR üretiliyor; kesişim = "bağımsız yakınsama" → sağlamlık kanıtı).
**YENİ tasarım** = çok-hop/sıralı-bağımlı (1. tezler → 2. tezleri OKUYAN hedefe-yönelik antitez [¬] → 3. çift-bazlı karşılaştırma/hakemlik).

### (i) Bağımsız-paralel eleştiri vs bilgilendirilmiş-sıralı eleştiri: literatür ne diyor?

ESKİ tasarımın epistemik temeli iki gelenekten geliyor: **(a)** nitel araştırma metodolojisinde **triangulation (üçgenleme)** — çoklu bağımsız kaynağın yakınsaması güvenilirliği artırır, ama önemli bir nüans var: literatür triangulation'ın MUTLAKA tam uyuşma gerektirmediğini, amacın "tekil birleşik yorum dayatmak değil, karmaşıklık ve çelişkileri keşfetmek" olduğunu vurguluyor **[D]** [53]; **(b)** istatistik/ML'de **Condorcet Jüri Teoremi** ve **"wisdom of crowds"** — Surowiecki'nin dört koşulu: ÇEŞİTLİLİK, BAĞIMSIZLIK, MERKEZİYETSİZLİK, TOPLULAŞTIRMA; bağımsızlık özellikle kritik, çünkü "bireyler birbirinden etkilenirse hiçbir yeni bilgi katılmıyor" **[D]** [48][50].

**Sorun:** LLM bağlamında bu bağımsızlık varsayımı ampirik olarak çoğunlukla GEÇERSİZ. İki kanıt hattı:

1. Multi-agent debate literatüründe homojen ajanlar arasında bile "bağımsız" üretimler yüksek korelasyonlu hatalar taşıyor, çünkü aynı ön-eğitim korpüsünü/mimariyi paylaşıyorlar **[K/X]**.
2. **"Examining Independence in Ensemble Sentiment Analysis... Condorcet Jury Theorem" (2024)** bunu DOĞRUDAN ampirik olarak gösteriyor: GPT tabanlı modeller ile tamamen farklı mimarideki modeller (FinBERT, DistilRoBERTa) arasında BİLE Condorcet'in bağımsızlık koşulu başarısız oluyor; ensemble/bagging neredeyse sıfır katma değer sağlıyor (**F-skorunda +0.00/+0.01 değişim**), en iyi tekil modeli geçemiyor **[D — doğrudan fetch edildi]** [51].

**Sonuç (kanıta dayalı, önemli çıkarım):** Eğer tez ve antitez ayrı ama BENZER (aynı model ailesi/benzer prompt şablonu) süreçlerden üretiliyorsa, ESKİ tasarımın "bağımsızlığı" zaten iddia edildiği kadar güçlü değildir — kesişimin sağladığı üçgenleme güvencesi kısmen yanılsama olabilir. Bu, YENİ tasarıma geçişte "kaybedilecek bağımsızlığın" sanıldığından daha az değerli olabileceği anlamına gelir.

Öte yandan insan karar bilimi tarafında **Delphi yöntemi** tam olarak aranan orta yolu gösteriyor: ilk tur bağımsız tahminlerle başlar, ama sonraki turlarda katılımcılara diğerlerinin (ANONİM) tahminleri gösterilip gözden geçirme fırsatı verilir; anonimlik en kıdemli/baskın kişinin grubu çapalamasını engeller **[D]** [52]. Bu, "tamamen kör" ile "tamamen bilgilendirilmiş" arasında üçüncü bir yol olduğunu gösteriyor: **bilgilendirilmiş ama yapılandırılmış revizyon**. İstihbarat analizi tradecraft'ı da (Heuer'in **Analysis of Competing Hypotheses**) benzer bir yapı öneriyor: önce tüm rakip hipotezler ayrı listelenir, sonra her kanıt parçası TÜM hipotezlere karşı sistematik test edilir — "kanıtı gör, hipotezi tekrar değerlendir" mantığı YENİ tasarımın 3. aşamasına (adjudication) çok yakın **[D]** [49].

### (ii) Ödünleşim: bağımsızlık kaybı vs hedefe-yönelik derinlik; çapalama/kontaminasyon riski ne kadar gerçek?

**Çapalama riski gerçek ve iyi belgelenmiş:**
- Genel LLM anchoring: uzman-kaynaklı çapalara yüksek güvenle etkileniyorlar, basit müdahaleler yetersiz, en fazla ~%10 iyileşme **[D]** [39].
- Zincirleme (chained) pipeline'lara özgü sentez (**Zylos Research, 2026**): kontaminasyon iki kanaldan işliyor — **(a) makine-makine:** yukarı-akış çıktısı (skor/ön-değerlendirme), üretici modeli "context-conditioned next-token predictor" olduğu için onaylayıcı içerik üretmeye itiyor; **(b) makine-insan:** ilk görülen değer bir referans noktası oluşturup sonraki tüm yargıları çarpıtıyor. "Kontaminasyon, naif tasarlanmış bir pipeline'ın VARSAYILAN davranışıdır" **[K — Zylos hakemli olmayan bir şirket araştırma blogu, TERSİYER kaynak; ancak atıf verdiği en az iki makale bu oturumda bağımsız doğrulandı ve isabetli çıktı, bu sentezin güvenilirliğini artırıyor]** [40].
  - **"No Thoughts Just AI" (2025)** — bağımsız doğrulandı **[D]**: önyargılı bir AI önerisi görüldüğünde, önceden adaylara eşit oy verilirken, AI'ın favori tuttuğu grup **%90'a varan oranda** tercih edilmeye başlıyor [42].
  - **"From Spark to Fire" (2026)** — bağımsız doğrulandı **[D]**: çok-ajanlı LLM işbirliğinde tek bir hata "tohumu", bağımlılık zincirinden geçerken 6 ana çerçevede **6.29-10.31 kat "topolojik kırılganlık etki faktörü"** ile yaygın başarısızlığa yol açıyor [41].

**Ama azaltma yolları da iyi belgelenmiş** — en güçlü kanıt CoVe'nin "Factored" tasarımından geliyor **[D]** [28]: doğrulama/eleştiri aşaması orijinal çıktıdan TAMAMEN bağımsız çalıştırıldığında, kendi hatasını "papağan gibi tekrarlama" eğilimi ortadan kalkıyor. Bu, bizim 2. ve 3. aşamalarımıza uyarlanabilir bir ilke: "antitez, tezin METNİNİ görmeli ama tezin GEREKÇESİNİ değil" gibi kısmi-bağımsızlık tasarımları düşünülebilir. Zylos sentezinin önerdiği somut teknikler (CoVe ile tutarlı) **[K]**: bağlam izolasyonu (ham kanıtı geçir, türetilmiş yargıyı geçirme), yapısal çıktı kısıtları, anti-sycophancy rol atama, farklı seed'lerle çoklu bağımsız tamamlama, çapraz-bağlam inceleme.

**Devil's Advocate kanıtı burada çok güçlü destekleyici** [46]: sadece "eleştirin" demek yetersiz (%48-63 uyuşmazlık, baseline'dan istatistiksel ayrılamıyor), ama açıkça "sen Devil's Advocate'sin, görevin BU SPESİFİK iddiayı çürütmek" demek uyuşmazlık oranını **%99.2**'ye çıkarıyor. YENİ tasarımın "hedefe-yönelik mantıksal negasyon (¬)" ilkesi tam olarak bu güçlü-rol-atama mantığıyla örtüşüyor.

**Sentez:** Çapalama riski gerçek ve önemsenmeli, ama (a) ESKİ tasarımın bağımsızlığı zaten sanıldığı kadar temiz değildi (korelasyonlu hatalar, [51]), (b) hedefe-yönelik adversarial rol atamanın faydası çok büyük ve iyi belgelenmiş ([46]), (c) CoVe-tipi kısmi bağımsızlıkla çapalama azaltılabilir (tamamen ortadan kaldırılamasa da). **Net değerlendirme: YENİ tasarıma geçiş literatürle tutarlı ve muhtemelen net pozitif — ama çapalama azaltma önlemleri olmadan yapılmamalı.**

### (iii) Üç aşama için: ne zaman ONE-SHOT, ne zaman MULTI-HOP?

**Aşama 1 — Tez üretimi:** Çoklu-bağımsız tek-geçiş (self-consistency mantığı [29]) hâlâ mantıklı, çünkü henüz eleştirilecek bir "önceki çıktı" yok — çapalama riski bu aşamada yapısal olarak YOK. Farklı seed'ler/persona ile mimari+bilişsel rol çeşitliliği [43] çeşitliliği artırabilir. Ancak Sequential-Edge bulgusu [30][31] modern modellerde tek-geçişin görece güvenilir olabileceğini de gösteriyor — konu karmaşık/çok-hopsa tez üretiminin KENDİSİ CoT/least-to-most ile içsel ayrıştırılmalı.

**Aşama 2 — Hedefe-yönelik antitez:** Yapısı gereği multi-hop/sıralı-bağımlı OLMAK ZORUNDA (tanımı gereği tezi görmeli). Asıl soru: tek büyük promptta mı, tez-başına ayrı çağrıyla mı? Devil's Advocate kanıtı [46] (%99.2 vs %48.3), TEZ-BAŞINA AYRI, dar-odaklı, güçlü rol-çerçeveli bir çağrının daha güçlü sonuç vereceğini düşündürüyor — odak dağılması riski azalır (CoT'un "bir seferde bir parçaya odaklanma" mantığıyla tutarlı [24]). Risk azaltma: CoVe'nin Factored ilkesi [28] burada uygulanabilir — antitez üretirken modele tezin İDDİASINI ver, tezin GEREKÇESİNİ/destekleyici argümanını VERME (sycophantic-anchor riski [37]).

**Aşama 3 — Karşılaştırma/hakemlik:** LLM-as-judge literatürünün doğrudan uygulandığı aşama — self-preference bias, position bias, verbosity bias [32][33]. Öneriler: (a) sıra rastgeleleştirilmeli; (b) mümkünse hakem aşaması AYRI bir çağrı/oturum olarak, kimlik maskelemeyle çalıştırılmalı; (c) TEK dev promptta "tüm çiftleri değerlendir" yerine ÇİFT-BAŞINA ayrı çağrı önerilir (hem odaklanma hem çapraz-çift kontaminasyonunu önleme, Zylos'un "context isolation" önerisiyle tutarlı [40]). Bu aşama tanım gereği multi-hop olmalı (iki girdiyi karşılaştırıyor) ama içsel olarak dar/odaklanmış tutulmalı.

### Genel tasarım önerisi (kanıta dayalı, somut)

1. **Tez aşaması:** paralel, çoklu-seed/çoklu-persona bağımsız üretim korunabilir.
2. **Antitez aşaması:** her tez için ayrı, dar-kapsamlı, güçlü Devil's-Advocate rol çerçevesi ("bu SPESİFİK önermeyi çürütmekle görevlisin") + CoVe-tipi kısmi izolasyon (iddiayı ver, gerekçeyi verme).
3. **Hakemlik aşaması:** çift-başına ayrı çağrı, kimlik/sıra maskeleme + rastgeleleştirme, mümkünse farklı model/persona ("üçüncü göz").
4. **Sistem geneli:** "ham kanıtı geçir, türetilmiş yargıyı geçirme" ilkesi pipeline'ın her ara yüzeyinde uygulanmalı.
5. YENİ tasarımın "kaybettiği" şey (tam bağımsızlık/üçgenleme) ESKİ tasarımda da kısmen yanılsamaydı ([51]) — geçişin net maliyeti literatürün ima ettiğinden düşük, kazancı (%99.2 uyuşmazlık kanıtı [46]) yüksek ve iyi belgelenmiş.

### Açıkça işaretlenmesi gereken belirsizlikler

- Bu raporun kanıtlarının büyük kısmı bizim TAM senaryomuzu değil, YAKIN analoglarını (CoVe, multi-agent debate, Delphi, ACH, self-consistency-vs-sequential) test ediyor. Üç-aşamalı tez→hedefe-yönelik-antitez→hakemlik pipeline'ının doğrudan ampirik testi literatürde **bulunamadı**.
- "%60+ correlated errors" ve "martingale" iddiaları tam metin doğrulaması yapılamadan K/X sınırında bırakıldı.
- Zylos Research tersiyer bir kaynak; sentezleri değerli ama atıf verdiği makalelerin sadece ikisi bu oturumda bağımsız doğrulandı (From Spark to Fire, No Thoughts Just AI); geri kalan atıfları (ör. "A-Index" arXiv:2505.15392, "Contextual Drag" 2602.04288, "Judging the Judges" 2604.23178, "Cross-Context Review" 2603.12123) **bu oturumda doğrulanmadı**.
- Bang ve ark.'ın ChatGPT/HotpotQA kesin yüzdesi ve "31/29/47/10/14%" hata dağılımı **bulunamadı/kesin doğrulanamadı** — dürüstçe "not found" olarak işaretliyorum.

---

## 5. Kaynaklar

1. HotpotQA: Multi-Hop QA Benchmark — https://www.emergentmind.com/topics/hotpotqa-benchmark
2. Ho, X., Duong Nguyen, A-K., Sugawara, S., Aizawa, A. (2020). "Constructing A Multi-hop QA Dataset for Comprehensive Evaluation of Reasoning Steps" (2WikiMultiHopQA), COLING 2020 — https://aclanthology.org/2020.coling-main.580/ (arXiv: https://arxiv.org/abs/2011.01060)
3. Trivedi, H., Balasubramanian, N., Khot, T., Sabharwal, A. (2022). "MuSiQue: Multihop Questions via Single-hop Question Composition", TACL 2022 — https://aclanthology.org/2022.tacl-1.31/
4. Geva, M. ve ark. (2021). "Did Aristotle Use a Laptop? A QA Benchmark with Implicit Reasoning Strategies" (StrategyQA), TACL — https://arxiv.org/abs/2101.02235
5. Bang, Y. ve ark. (2023). "A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning, Hallucination, and Interactivity" — https://arxiv.org/html/2302.04023 / https://aclanthology.org/2023.ijcnlp-main.45/
6. "Do Large Language Models Perform Latent Multi-Hop Reasoning without Exploiting Shortcuts?" (2024) — https://arxiv.org/html/2411.16679v1
7. "Back Attention: Understanding and Enhancing Multi-Hop Reasoning in LLMs" — https://arxiv.org/pdf/2502.10835
8. "Opening the Black Box: A Survey on the Mechanisms of Multi-Step Reasoning in LLMs" — https://arxiv.org/pdf/2601.14270
9. "Implicit Reasoning in Large Language Models: A Comprehensive Survey" — https://arxiv.org/html/2509.02350
10. Lanham, T. ve ark. (2023, Anthropic). "Measuring Faithfulness in Chain-of-Thought Reasoning" — https://arxiv.org/pdf/2307.13702
11. "On the Hardness of Faithful Chain-of-Thought Reasoning in LLMs" (2024) — https://arxiv.org/html/2406.10625v2
12. "Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps" (EMNLP 2025) — https://aclanthology.org/2025.emnlp-main.504.pdf
13. "Making Reasoning Matter: Measuring and Improving Faithfulness of CoT Reasoning" (2024) — https://arxiv.org/pdf/2402.13950
14. "Multi-Step Reasoning with Large Language Models, a Survey" (2024) — https://arxiv.org/pdf/2407.11511
15. Brown, T. ve ark. (2020). "Language Models are Few-Shot Learners" (GPT-3), NeurIPS 2020 — https://arxiv.org/pdf/2005.14165
16. Xie, S. ve ark. "An Explanation of In-context Learning as Implicit Bayesian Inference" (2021) — https://arxiv.org/pdf/2111.02080
17. "Zero-Shot vs. One-Shot vs. Few-Shot Learning: How to Test?" — https://testrigor.com/blog/zero-shot-vs-one-shot-vs-few-shot-learning-how-to-test/
18. Agarwal, R. ve ark. (2024, Google DeepMind). "Many-Shot In-Context Learning", NeurIPS 2024 — https://arxiv.org/pdf/2404.11018
19. "A Fano-Style Accuracy Upper Bound for LLM Single-Pass Reasoning in Multi-Hop QA" (2025) — https://arxiv.org/pdf/2509.21199
20. Zhou, D. ve ark. (2022). "Least-to-Most Prompting Enables Complex Reasoning in LLMs" — https://arxiv.org/abs/2205.10625
21. Wang, L. ve ark. (2023). "Plan-and-Solve Prompting", ACL 2023 — https://aclanthology.org/2023.acl-long.147/
22. "Revision or Re-Solving? Decomposing Second-Pass Gains in Multi-LLM Pipelines" (2026) — https://arxiv.org/html/2604.01029
23. Yao, S. ve ark. (2023). "Tree of Thoughts: Deliberate Problem Solving with LLMs", NeurIPS 2023 — https://papers.nips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html (kod: https://github.com/princeton-nlp/tree-of-thought-llm)
24. Wei, J. ve ark. (2022). "Chain-of-Thought Prompting Elicits Reasoning in LLMs", NeurIPS 2022 — https://arxiv.org/abs/2201.11903
25. "Mind Your Step (by Step): CoT can Reduce Performance on Tasks where Thinking Makes Humans Worse" (2024) — https://arxiv.org/abs/2410.21333
26. Madaan, A. ve ark. (2023). "Self-Refine: Iterative Refinement with Self-Feedback" — https://arxiv.org/pdf/2303.17651
27. Shinn, N. ve ark. (2023). "Reflexion: Language Agents with Verbal Reinforcement Learning", NeurIPS 2023 — https://neurips.cc/virtual/2023/poster/70114
28. Dhuliawala, S. ve ark. (2023). "Chain-of-Verification Reduces Hallucination in LLMs" — https://arxiv.org/abs/2309.11495
29. "Self-consistency: majority-vote across reasoning samples" (Wang ve ark. 2022 açıklaması) — https://zeroentropy.dev/concepts/self-consistency/
30. "Self-Consistency Is Losing Its Edge: Diminishing Returns and Rising Costs in Modern LLMs" (2025) — https://arxiv.org/html/2511.00751
31. "The Sequential Edge: Inverse-Entropy Voting Beats Parallel Self-Consistency at Matched Compute" (2025) — https://arxiv.org/pdf/2511.02309
32. "A Survey on LLM-as-a-Judge" (2024) — https://arxiv.org/pdf/2411.15594
33. "Self-Preference Bias in LLM-as-a-Judge" (2024) — https://arxiv.org/abs/2410.21819
34. Gou, Z. ve ark. (2023). "CRITIC: LLMs Can Self-Correct with Tool-Interactive Critiquing" — https://arxiv.org/abs/2305.11738
35. Huang, J. ve ark. (2023/ICLR 2024). "Large Language Models Cannot Self-Correct Reasoning Yet" — https://arxiv.org/abs/2310.01798 (rakamlar: https://www.emergentmind.com/papers/2310.01798)
36. Sharma, M. ve ark. (2023, Anthropic). "Towards Understanding Sycophancy in Language Models" — https://www.lesswrong.com/posts/g5rABd5qbp8B4g3DE/towards-understanding-sycophancy-in-language-models ; https://spectrum.ieee.org/ai-sycophancy
37. "Sycophantic Anchors: Localizing and Quantifying User Agreement in Reasoning Models" (2026) — https://arxiv.org/pdf/2601.21183
38. "TRUTH DECAY: Quantifying Multi-Turn Sycophancy in Language Models" (2025) — https://arxiv.org/pdf/2503.11656
39. Lou, J. & Sun (2024). "Anchoring Bias in Large Language Models: An Experimental Study" — https://arxiv.org/abs/2412.06593
40. "Anchoring and Contamination in Chained LLM Pipelines" (Zylos Research, 2026) — https://zylos.ai/research/2026-06-29-anchoring-contamination-chained-llm-pipelines/
41. "From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration" (2026) — https://arxiv.org/abs/2603.04474v1
42. "No Thoughts Just AI: Biased LLM Hiring Recommendations Alter Human Decision Making and Limit Human Autonomy" (2025) — https://arxiv.org/abs/2509.04404
43. "Can LLM Agents Really Debate? A Controlled Study of Multi-Agent Debate in Logical Reasoning" (2025) — https://arxiv.org/abs/2511.07784
44. "Diverse Evidence, Better Forecasts: Multi-Agent Deliberation Under Information Asymmetry" (2026) — https://arxiv.org/pdf/2607.01661
45. "Minority Sentinel: When to Overturn Majority Voting in Multi-Agent LLM Debates" (2026) — https://arxiv.org/html/2606.29270v1
46. "Inducing Disagreement in Multi-Agent LLM Executive Teams: Only the Devil's Advocate Works" — https://openreview.net/forum?id=mxBmj5LYU2
47. "DEBATE: Devil's Advocate-Based Assessment and Text Evaluation" (2024) — https://arxiv.org/html/2405.09935v2
48. Surowiecki, J. — "The Wisdom of Crowds" — https://en.wikipedia.org/wiki/The_Wisdom_of_Crowds
49. Heuer, R.J. — Analysis of Competing Hypotheses — https://en.wikipedia.org/wiki/Analysis_of_competing_hypotheses ; https://pherson.org/wp-content/uploads/2013/06/06.-How-Does-ACH-Improve-Analysis_FINAL.pdf
50. "Majority Voting and the Condorcet's Jury Theorem" (2020) — https://arxiv.org/abs/2002.03153
51. "Examining Independence in Ensemble Sentiment Analysis... Using the Condorcet Jury Theorem" (2024) — https://arxiv.org/html/2409.00094
52. Delphi Yöntemi — https://www.1000minds.com/decision-making/delphi-method ; https://otexts.com/fpp2/delphimethod.html
53. Triangulation (üçgenleme) metodolojisi — https://www.simplypsychology.org/what-is-triangulation-in-qualitative-research.html ; https://atlasti.com/guides/the-guide-to-mixed-methods-research/triangulation-in-mixed-methods-research
54. "Omanic: Towards Step-wise Evaluation of Multi-hop Reasoning in LLMs" (2026) — hata dağılımı verisi için olası ama DOĞRULANAMAMIŞ kaynak — https://arxiv.org/pdf/2603.16654
