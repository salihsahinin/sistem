# Sokrates ajanı: modern LLM tasarımlarının güncel durumu

**AS-OF:** 2026-10-29 (sistem saati). Canlı web araması; model hafızası kullanılmadı. **Araştırmacı:** atlas (Sonnet). **Deneysel damga:** bulgular tek koşum, hakem denetimi yok.

**Kanıt işareti:** `[P]` birincil (makale/resmî sayfa açılıp okundu) · `[S]` ikincil (arama özeti/blog/haber, açılmadı ya da açılamadı) · `[?]` doğrulanamadı.

## 0. Önce düzeltmeler (istemdeki varsayımlar)

| İstemdeki iddia | Bulgu |
|---|---|
| "Princeton SocraticAI" | **Bulunamadı.** Aramada Princeton bağlantılı bir Sokratik LLM sistemi çıkmadı. Aynı adlı iki sistem var: Ashoka Üniversitesi (Sunil, Thakkar; arXiv 2512.03501) ve City University of Hong Kong (EDULEARN26). Princeton adı muhtemelen karışıklık `[?]`. https://arxiv.org/html/2512.03501v1 · https://library.iated.org/view/SUVERNEV2026SOC |
| "anthropics/skills içinde grill-me" | **Yok.** Arama anthropics/skills altında böyle bir skill bulmadı. Topluluk skill'i: `mattpocock/skills` (skills/productivity/grill-me) ve `brianlovin/agent-config`. https://www.claudemarket.ai/skills/brianlovin/agent-config/grill-me |
| "sartak gist" | **Bulunamadı.** Tek aramada böyle bir gist çıkmadı; URL elde yok `[?]`. |
| Chang 2303.08769 | Var, doğrulandı (bkz. 1.1). |

## 1. Akademik

### 1.1 Chang 2023: Socratic method prompting `[P]`
"Prompting Large Language Models With the Socratic Method", Edward Y. Chang; arXiv ilk sürüm 17 Şubat 2023, v2 16 Mart 2023; IEEE CCWC 2023. Altı teknik önerir: tanımlama, elenchus, diyalektik, maieutics, genelleme, karşıolgusal akıl yürütme. Bunları tümevarım/tümdengelim/abdüksiyonla eşler. Gözlem: görev hedefi ve kullanıcı niyeti diyalogdan önce verilince model daha iyi çalışıyor. Sayfa her tekniğin uygulama ayrıntısını vermiyor (tam metin okunmadı).
Nitelik: bu çalışma **modelin kendi akıl yürütmesini** Sokratik yapar (prompting tekniği); öğrenciyi sorgulayan öğretmen ajanı değildir. Bizim kullanım (ajan kullanıcıyı sorgular) farklı bir kategori.
URL: https://arxiv.org/abs/2303.08769

### 1.2 SocraticAI (Ashoka), 2025 `[P]`
Sunil ve Thakkar, arXiv 2512.03501. Kısıtlı yardım mimarisi: günde **8 sorgu** hakkı; öğrenci önce yaklaşımını, denemelerini, takıldığı kavramı yazmak zorunda; girdi doğrulama; ders notlarına RAG; her etkileşim yansıtma istemiyle biter; yansıtma işe yaramazsa eğitmene yükseltme. CS-1102 dersinde 3 hafta gözlem: öğrencilerin yaklaşık **%75'i** yanlış anlamayı/sonraki adımı belirten yansıtma yazdı; belirsiz sorulardan ("kodum çalışmıyor") ayrıntılı sorulara geçiş 2-3 hafta. **Sınırlılık:** bazı öğrenciler yansıtma istemini atlatmak için yasak çözüm talebini yeniden ifade etti; bıkkınlık verisi yok; kontrollü prompt injection denemelerinde küçük zafiyetler.
URL: https://arxiv.org/html/2512.03501v1

### 1.3 SocraticLM (NeurIPS 2024) `[S]`
Liu ve ark. SocraTeach: "Dean-Teacher-Student" çoklu ajan hattıyla üretilmiş yaklaşık 35 bin çok turlu Sokratik diyalog (22 bin tek turlu ayrı dosya), altı simüle öğrenci tipi, beş pedagojik değerlendirme boyutu; GPT-4'e göre öğretim performansında %12'den fazla üstünlük bildiriyor (poster sayfası; makale gövdesi açılmadı). Not: dört öğretim yeteneği + beş değerlendirme boyutu ayrımına dikkat; "beş yetenek" ifadesi doğrulanmadı.
URL: https://neurips.cc/virtual/2024/poster/93477 · https://github.com/CMLF-git-dev/SocraticLM
Aynı çalışmanın notu: sorular ne fazla doğrudan ne fazla muğlak olmalı, sorma zamanlaması ve sıklığı ayarlanmalı `[S]` (https://alphaxiv.org/overview/2407.17349v1).

### 1.4 TreeInstruct (2024) `[S]`
arXiv 2406.11709. Teşhis: LLM'ler çözümü doğrudan veriyor, bu yüzden zayıf eğitmen; çare: öğrencinin bilgi durumunu kestirip sonra soru planlamak (planlama ağacı). Yalnız özetten okundu.
URL: https://arxiv.org/pdf/2406.11709v4

### 1.5 Sokratik sorular çok doğrudan olabiliyor `[S]`
umass-ml4ed/socratic-quest-gen verisetine atıf yapan makale: üretilen bazı sorular çözümü erken ele veriyor. Soru biçiminde sızıntı = "Sokratik kılıklı cevap".
URL: https://par.nsf.gov//servlets/purl/10510120

### 1.6 Paul-Elder taksonomisi (6 soru türü) `[S]`
Tutarlı biçimde: (1) açıklama/netleştirme, (2) varsayımlar, (3) neden ve kanıt, (4) bakış açıları, (5) sonuçlar ve çıkarımlar, (6) sorunun kendisi hakkında sorular. Tarih kaynaklar arası çelişiyor (çoğunlukla 2006; bir ikincil kaynak 1995 diyor, o sayfa güvenilmez sayıldı). Birincil Paul-Elder kitabı açılmadı.
Bu taksonomiyi Sokratik öğretmen için protokol olarak kullanan çalışma: "Resurrecting Socrates in the Age of AI" (araştırma sorusu geliştirme için Sokratik tutor değerlendirme protokolü, arXiv 2504.06294). PDF sıkıştırılmış geldi, **içeriği okunamadı** `[?]`.
URL: https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2019.00126/pdf · https://arxiv.org/pdf/2504.06294

### 1.7 Ürünler: Khanmigo, Claude Learning mode, ChatGPT Study mode, Gemini Guided Learning
- **Khanmigo** `[S]`: GPT-4 üstünde; Sokratik tutumu **doğrudan cevabı reddetme** olarak uygular; yardım isteyince "sonraki adım ne olurdu?" gibi sorularla döner. Khan Academy öğrenme başkanı DiCerbo (2025 röportajı): ilk keşif, sistem prompt'unda "Sokratik, cevap verme" demenin çıktıyı değiştirmesiydi; en büyük uyarı **çıktı koşumdan koşuma değişir, tek denemeyle prompt sınanmaz, tekrarlı değerlendirme düzeneği şart**; Kasım'da başlayıp Mart 2023'te çıkış (yaklaşık 7 ay). Eleştiri (düşük otorite, doğrulanmadı `[?]`): ısrarla cevap isteyen öğrenci yönlendirilmeye devam ediyor; öğrenciler oturumu terk ediyor. Kaynak: https://aiweekly.co/alerts/khanmigo-ai-tutor-falls-short-of-khan-academy-hype · https://www.edweek.org/technology/opinion-can-an-ai-powered-tutor-produce-meaningful-results/2025/07
- **Claude for Education Learning mode** `[P]`: 2 Nisan 2025 duyurusu; cevap yerine soru ("How would you approach this problem?", "What evidence supports your conclusion?"), temel kavramları öne çıkarma, araştırma makalesi/çalışma rehberi/ana hat şablonları; Projects içinde çalışır; ortaklar Northeastern, LSE, Champlain. Sistem prompt'u yayımlanmamış; tasarım ayrıntısı yok. https://www.anthropic.com/news/introducing-claude-for-education
- **ChatGPT Study mode** (29 Temmuz 2025) ve **Gemini Guided Learning** (yaklaşık 1 hafta sonra, LearnLM): ikisi de adım adım, rehber soru, öğrenciye anlattırma `[S]`. Prompt metinleri bulunamadı. https://techcrunch.com/2025/08/06/google-takes-on-chatgpts-study-mode-with-new-guided-learning-tool-in-gemini/

**Tasarım kararı önerisi (bölüm 1):**
- **Alınır:** Paul-Elder'in 6 türü soru-tipi sözlüğü olarak (her tur etiketli); SocraticAI'deki "önce kendi denemeni yaz" kapısı ve tur sonu yansıtma; TreeInstruct'tan "önce kullanıcı durumunu kestir, sonra sor"; Chang'ın tekniklerinden tanımlama + elenchus + karşıolgusal (üçü yeterli).
- **Alınmaz:** Khanmigo'nun mutlak "asla cevap verme" refleksi (kanıtı zayıf, bkz. 3.5); SocraticAI'nin günlük sorgu kotası (Salih'in tek kullanıcılı ortamında anlamsız, bıkkınlık yaratır); SocraticLM'in ince-ayarı (model eğitmiyoruz).
- **Atlanan boşluk:** Princeton SocraticAI, sartak gist, ChatGPT/Gemini prompt metinleri bulunamadı; varsayım olarak kullanılmasın.

## 2. Açık kaynak persona ve prompt örnekleri

| Kaynak | Ne | Kanıt | URL |
|---|---|---|---|
| mattpocock/skills, `grill-me` | SKILL.md yalnız 3 satır: açıklama "A relentless interview to sharpen a plan or design", `disable-model-invocation: true`, gövde "Call the Skill tool with 'grilling'" | `[P]` | https://github.com/mattpocock/skills (ham: skills/productivity/grill-me/SKILL.md) |
| mattpocock/skills, `grilling` | Gerçek mantık burada (özetten): karar ağacı, her karar alt kararlara bölünür; **tek turda numaralı birden çok soru**, her soruya **önerilen cevap**; cevaplardan sonra ağaç yeniden hesaplanır, bağımlı sorular sonraki tura kalır; ortam gerçeği alt-ajanla araştırılır (kullanıcıya sorulmaz), **kararlar kullanıcıya aittir**; çıkış: tüm dallar kapanıp açık varsayım kalmayınca ve kullanıcı ortak anlayışı onaylayınca | `[P]` özet (tam metin verilmedi) | https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grilling/SKILL.md |
| brianlovin/agent-config, `grill-me` | "Interview me relentlessly about every aspect of this plan until we reach a shared understanding"; karar ağacının her dalı, bağımlılıklar tek tek; her soru için önerilen cevap; kod tabanı cevaplayabiliyorsa sorma | `[P]` | https://github.com/brianlovin/agent-config |
| martin.vuk/socratic-tutor (üniversite GitLab) | Düz markdown prompt dosyaları (socratic.md, Feynman tutor); sohbet başına yapıştır | `[S]` | https://git.fri.uni-lj.si/martin.vuk/socratic-tutor |
| Nydv01/fossee-python-evaluation | Meta-prompt: çözüm/kod düzeltmesi verme, satır değil kavram, geri bildirim tek cesaret verici soru | `[S]` | https://github.com/Nydv01/fossee-python-evaluation |
| jakemaly/Gemma4-31B-Socratic-LoRA | Model kartı: adapter yine de tamamlanmış çözüm üretebilir, zararsız tutor isteklerini aşırı reddedebilir, başka prompt şablonunda farklı davranır | `[S]` | https://huggingface.co/jakemaly/Gemma4-31B-Socratic-LoRA |
| Newcastle Cogniti kılavuzu | "Sadece cevap" talebi: nazikçe reddet, rolünün düşünmene yardım olduğunu kısaca söyle, en küçük yararlı sonraki soruyu sor; hayal kırıklığı: duyguyu kabul et, ilerlenebilir tek küçük adım bul, açıklama yerine soruyla yeniden bağlan; kafa karışıklığı: adım boyunu küçült, küçük ipucu ya da iki seçenek ver | `[S]` (PDF doğrudan açılamadı, arama özetinden) | https://www.newcastle.edu.au/__data/assets/pdf_file/0020/1134830/PDF_Designing-a-Socratic-Tutor-Agent-in-Cogniti.pdf |
| LaTrobe "Build a GPT as a Socratic Tutor" | Çözümden önce deneme zorunlu; ipucu merdiveni: ipucu, daha özel ipucu, kısmen çözülmüş örnek | `[S]` | https://www.craigbellamy.net/images//Build_a_GPT_as_a_Socratic_Tutor_LaTrobe.docx |
| Mississippi State kılavuzu | Öğrenciler botu cevap vermeye pek ikna edemiyor; yanıt ≈150 kelimeyle sınırlanırsa tek odaklı soru zorlanır; lise örneği: bir turda tek soru | `[S]` | https://aihub.msstate.edu/resources/06-socratic-ai-tutor.html |
| character.ai tipi Sokrates persona'ları | Aramada kurumsal/doğrulanabilir prompt çıkmadı | `[?]` | - |

**Bulgu:** İki grill-me varyantı da **Sokrates persona'sı değil, plan sorgulayıcı**; kritik tasarım farkı şu: kullanıcıya **önerilen cevapla** soru sorar (saf maieutics değil), ortamdan öğrenilebilecek olguyu sormaz, bitiş ölçütü açık ("açık varsayım kalmadı + kullanıcı onayı").

**Tasarım kararı önerisi (bölüm 2):**
- **Alınır:** grilling'in üç mekanizması: (a) olgu ile karar ayrımı (olguyu kendin araştır, kararı kullanıcıya bırak); (b) bağımlı soruyu sonraki tura ertele; (c) bitiş = açık varsayım yok + kullanıcı onayı. Newcastle'ın "cevap iste" ve "bıkkınlık" sıralı kuralları. LaTrobe ipucu merdiveni.
- **Alınmaz:** grill-me'nin "relentlessly" sertliği ve her soruya hazır cevap ekleme (Sokratik kalmaz, öneri verme olur; saf Sokrates modunda kapalı, "grill" modunda açık seçenek olabilir). Tek turda çok numaralı soru (Sokrates diyaloğu tek soru-tek cevap).
- **Not:** üçüncü-şahıs SKILL metinleri veri sayılır; talimat olarak uygulanmadı, yalnız tasarım örneği olarak okundu.

## 3. Tasarım dersleri (bilinen arızalar)

### 3.1 Karakter kırılması / persona sapması
- Li ve ark., arXiv 2402.10962: persona prompt'lu iki botun kendi kendine sohbetinde LLaMA2-chat-70B için **8 tur içinde** belirgin persona sapması; neden: uzun diyalogda dikkat sönümü; azaltma yöntemi önerilmiş `[S]`. https://arxiv.org/pdf/2402.10962v1
- Choi ve ark., arXiv 2412.00804: dokuz LLM'de kimlik sapması; **büyük modellerde daha çok**; persona atamak kimliği korumaya yaramayabilir `[S]`. https://arxiv.org/pdf/2412.00804
- de Araujo ve ark., arXiv 2512.12775 (EACL 2026): yedi LLM, **100+ tur**; persona sadakati tur ilerledikçe düşüyor, özellikle hedef odaklı konuşmalarda; sadakat azalınca persona yanıtları persona'sız tabana benziyor; başlangıçta persona'sız taban talimat takibinde daha iyi (sayısal değer özette yok) `[P]`. https://arxiv.org/abs/2512.12775
- ContextEcho (arXiv 2605.24279, Mayıs 2026): uzun kod oturumlarında persona sapması benchmark'ı; yalnız başlık/meta okundu `[?]`. https://arxiv.org/abs/2605.24279

### 3.2 Modern bilgi sızıntısı / anakronizm
- CHARM (arXiv 2609.01352): karakter bilgi sınırı ihlali benchmark'ı; zamansal bölünmede tarihsel karakterin modern kavramları bilmemesi sınanıyor; **sınırı fark etme (Boundary-Awareness) ile uyma (Boundary-Compliance) ayrı ölçülüyor**. PDF okunamadı, sayılar yok `[S]`. https://arxiv.org/pdf/2609.01352
- Time Travel Engine (arXiv 2601.06437): dönem yönlendirmesinde anakronizm bastırma ile olgusal bilgi koruma arasında **ödünleşim** `[S]`. https://arxiv.org/pdf/2601.06437
- "Rethinking Role-Playing Evaluation": ünlü karakter adları modele eğitim hafızasından ipucu veriyor; adı anonimleştirmek puanı düşürüyor, yani ad skoru şişiriyor `[S]`. https://www.alphaxiv.org/abs/2603.03915
- Tarihsel simülasyonda modeller modern normları geçmişe taşıyor; ince-ayarlı model otomatik hakemi kandırıp insan hakemi kandıramıyor `[S]` (aynı arama sonucu; birincil kaynağı tek tek açılmadı).

### 3.3 Soru-sor-ama-asla-cevap-verme aşırılığı
- GuideEval (arXiv 2508.06583, 5.177 örnek, GPT-4o-mini hakem, insanla uyum %89-97 bildirilmiş): modeller doğru cevabı kolay onaylıyor (P-Affirm tipik >0,8) ama **hatalı cevapta yönlendirme zayıf**: P-Redirect Qwen3-32B 0,6008, DeepSeek-R1 0,5483, SocraticLM **0,1411**. Kafa karışıklığına duyarlılık da düşük: SocraticLM'de 0,043. Tasarlanmış prompt DeepSeek-R1'in P-Redirect'ini 0,5483'ten 0,9149'a çıkardı. Başarısızlık kalıbı: ayrım gözetmeden olumlu geri bildirim; kafa karışıklığı ifade edilince **yeni açıklama sunmama**; öğrenilmiş konuyu yeniden açıklama. Yani **soru-odaklı ince-ayarlı model (SocraticLM) uyarlamada en zayıf çıktı** `[P]`. https://arxiv.org/html/2508.06583v2 (metnin son %22'si okunmadı)
- Bıkkınlık kanıtı: **zayıf.** SocraticAI makalesi bıkkınlık verisi vermiyor; Khanmigo terk iddiası düşük otoriteli blog (`[?]`). EPFL çalışması (3.6) öğrencilerin Sokratik tutor'ı **daha az verimli algıladığını** ölçtü `[P]`.

### 3.4 Sorgu döngüsüne saplanma
Doğrudan döngü ölçümü bulunamadı `[?]`. Dolaylı: GuideEval'de "belirsiz geri bildirimden sonra hedefli düzeltme yapmama" ve "kafa karışıklığında yeni açıklama sunmama" arızaları aynı soruyu yeniden sorma eğilimiyle uyumlu `[S]`; Khanmigo için "ısrar etsen de yönlendirmeye devam eder" `[?]`; lise prompt örneği: öğrenci zorlanınca soruyu **tekrarlama, ipucu ver** `[S]`. Boston Üniv. çalışması: sistem çözümü nadiren sızdırdı, fakat **çok soru soran öğrenciler vize notunda daha kötüydü** (gözlemsel, rastgele değil; sayfa 403, arama özetinden) `[S]`. https://open.bu.edu/bitstreams/2547d4f0-a878-4ebd-830b-ea40643c66f3/download

### 3.5 Çıkış ölçütü (aporia'da ne zaman durmalı), tur bütçesi
Aporia için **kanıtlı bir durdurma kuralı bulunamadı** `[?]`. Bulunan en yakın somut ölçütler:
- grilling: tüm dallar kapandı, açık varsayım kalmadı, kullanıcı onayı `[P]`.
- SocraticAI: yansıtma sorunu çözmezse **insana yükselt** `[P]`; günde 8 sorgu (bütçe bu, tur bütçesi değil).
- Mississippi State: yanıt ≈150 kelime, tek soru `[S]`.
- Persona sadakati 8 tur (Li) ve 100+ tur (de Araujo) bandında düşüyor: **tur bütçesi kısa tutulmalı ya da persona özeti periyodik yeniden enjekte edilmeli** (azaltma yöntemini Li önerdi; ayrıntısı okunmadı) `[S]`.
Bunlar tasarım çıkarımıdır, doğrulanmış eşik değildir.

### 3.6 Kullanıcı "cevabı söyle" dediğinde
- Khanmigo: reddeder, soruyla döner `[S]`. SocraticAI: öğrenciler reddi yeniden ifadeyle atlatıyor; yani **katı ret, atlatma yarışı doğurur** `[P]`.
- Newcastle sırası: kısa ret, rolü açıkla, en küçük yararlı soru; hayal kırıklığında duyguyu kabul et, adım boyunu küçült `[S]`.
- LaTrobe: ipucu merdiveni; **kısmen çözülmüş örnek** son basamak `[S]`.
- EPFL (AIED 2026): Sokratik grup sonraki oturumlarda daha çok öğrenme kazandı ve kısıtsız LLM'de daha çok anlamaya yönelik prompt kullandı; ama tutor'ı daha az verimli buldular `[P]` (3.7).
Çıkarım (kanıt değil): öğrenme amaçlı bağlamda ret + merdiven yararlı; Salih'in bağlamında amaç öğrenme değil, kendi kavramını netleştirme olduğundan ret yerine **bir kez açık beyan + cevabı ver + işaretle** daha uygun görünür. Bu bağlam farkı için kanıt yok `[?]`.

**Tasarım kararı önerisi (bölüm 3):**
- **Alınır:** tur bütçesi kısa (öneri: 6-8 tur [?], Li'nin 8 tur bulgusuna dayalı kestirim) ya da periyodik persona yeniden enjeksiyonu; olgu/karar ayrımı; "cevabı söyle" için **tek kademeli sapma**: bir kez kısa gerekçe, ikincisinde cevabı ver ve `[sokratik-sapma]` işaretle; kafa karışıklığı ifadesinde yeni açıklama zorunlu (GuideEval arızası); modern bilgi için **kelime-listesi ya da çıktı sonrası denetim** (CHARM'ın farkına göre: bilmek ≠ uymak, bu yüzden prompt'a güvenme, denetle).
- **Alınmaz:** mutlak ret (atlatma doğurur, bıkkınlık riski); kota (8 sorgu/gün); "aporia'da dur" için hazır eşik varsayımı (kanıtı yok; kendi eşiğimizi deneyle belirleyip deneysel damgalarız).
- **Kapsam notu:** anakronizm bizde iki yönlü: Sokrates'in modern kavram kullanması, ve model hafızasının zaman-bağımlı iddiaları (kök md.8). Persona yalnız üslup katmanı olmalı, olgu iddiaları canlı doğrulamadan geçmeli.

## 3.7 Etki kanıtı (karar için)
- EPFL, arXiv 2607.03303 (3 Temmuz 2026, AIED 2026 en iyi makale): 66 öğrenci, 6 hafta, Sokratik yönlendirme (SG) ile prompt iyileştirme (PR) tutor'ı; yönlendirmeli kullanımda görev performansı benzer; **SG sonraki oturumlarda daha yüksek öğrenme kazanımı**; ikinci fazda 52 öğrenci kısıtsız LLM: SG öğrencileri anlamaya yönelik prompt stratejisini daha çok benimsedi; **SG daha az verimli algılandı** `[P]`. Kıyas "doğrudan cevap veren sohbet botu" değil, PR tutor'ı. https://arxiv.org/abs/2607.03303
- Doğrulanamayan: bir blogun andığı 2025 PNAS çalışması (kısıtsız chatbot pratikte yardım, sınavda zarar; iskeleli sürüm zarar vermedi) `[?]` birincil kaynak açılmadı. https://www.iatrox.com/blog/socratic-ai-tutors-vs-answer-first-chatbots

## 4. Değerlendirme: Sokratik ajan kalitesi nasıl ölçülür

**Hazır ölçüm çerçeveleri (kullanıma hazır):**
- **GuideEval** `[P]`: üç aşama, altı metrik. Algılama (P-Affirm, P-Redirect; puan 1/0,5/0), düzenleme (O-Advance, O-Reconfigure; 0/1), yönlendirici soru (E-Strategic, E-Heuristic; Bloom esinli 0-3; ESA = E-S − E-H soru derinliği uyumu). Dört öğrenci durumu: doğru, hatalı, kavrama, kafa karışıklığı. LLM hakem ile insan uyumu %89-97 (bildirilen). Ayrıca ESA bazı modellerde **negatif**: hatalı cevaba karşı daha derin soru. https://arxiv.org/html/2508.06583v2
- **SocraticLM / SocraTeach** `[S]`: beş pedagojik boyut; EduDial (arXiv 2510.12899) dört boyut: IARA, CARA, SER, SRR (adların açılımı okunmadı). https://arxiv.org/pdf/2510.12899
- **Mantık hatası/Sokratik soru çalışması** (arXiv 2606.01020): LLM-hakem (QwQ-32B) insan uzmanla doğrulanmış, diyalog başına geçti/kaldı metrikleri; aşırı soru ölçümüne uyarlanabilir ama uyarlandığı **doğrulanmadı** `[S]`. https://arxiv.org/pdf/2606.01020
- **Boundary-Awareness / Boundary-Compliance** (CHARM) anakronizm için `[S]`.

**Sorduğun üç ölçüt için durum:**
| Ölçüt | Hazır karşılık | Durum |
|---|---|---|
| Soru/cevap oranı | Doğrudan metrik bulunamadı | `[?]` Kendimiz sayarız: ajan turlarında soru işaretli cümle oranı + tek turda soru sayısı (grilling çok soru, Sokrates tek soru). Ucuz, deterministik. |
| Tanım-netleşme | Yakın: E-Strategic/E-Heuristic soru derinliği; Paul-Elder "açıklama" türü | Netleşmeyi doğrudan ölçen hazır metrik bulunamadı `[?]`; öneri: oturum başı ve sonu kullanıcı tanımını (Salih ya da hakem) karşılaştır. |
| Kullanıcı kendi çelişkisini fark etti mi | Bulunamadı | `[?]` Elenchus'un tanımsal ürünü; ölçüm için oturumdan sonra "çelişki işaret edilen tur" ile "kullanıcının tanımı revize ettiği tur" eşleştirilir (öneri, doğrulanmamış). |

Gözlemsel göstergeler: yansıtma kalitesi (SocraticAI, %75 eşik, nitel kodlama) `[P]`; sonraki oturum öğrenme kazanımı (EPFL) `[P]`; soru sayısı ile başarı ilişkisi (BU: çok soru ≈ kötü sonuç, nedensellik yok) `[S]`.
Uyarı: LLM-hakem insanla %89-97 uyum bildiriyor ama tek makale (GuideEval); Khanmigo ekibinin dersi: **tek koşum güvenilmez, tekrarlı değerlendirme** `[S]`. Depodaki yapan ≠ ölçen ilkesi (hakem ajanı) bununla uyumlu.

**Tasarım kararı önerisi (bölüm 4):**
- **Alınır:** GuideEval'in dört öğrenci durumu senaryo setini (doğru, hatalı, kavrama, kafa karışıklığı) Sokrates için test girdisi yapmak; P-Redirect ve "kafa karışıklığında yeni açıklama" kontrolleri; sorgu sayısı/tur ve soru-işareti oranı gibi deterministik sayaçlar; aynı senaryoyu N kez koşturup dağılım ölçmek; hakem = ayrı ajan.
- **Alınmaz:** tek kalite skoru; SocraticAI'nin %75 eşiğini hedef olarak devralmak (farklı bağlam); "kullanıcı çelişkisini fark etti" için otomatik ölçüm iddiası (yok, yalnız hakem + Salih beyanı).

## 5. Sentez (bu raporun kendi hükmü, kanıtla birlikte)

**Yakınsayan (birden çok bağımsız kaynak):** (a) saf "asla cevap verme" kırılgan: atlatılıyor (SocraticAI), uyarlamada zayıf (GuideEval), verimsiz algılanıyor (EPFL); (b) persona sadakati tur arttıkça düşüyor (Li, de Araujo, Choi); (c) tek koşumla prompt sınanmaz (Khanmigo, GuideEval ek test).
**Iraksayan:** Sokratik tutor'ın öğrenme etkisi: EPFL olumlu, BU gözlemi karışık; kıyas gruplarının doğası farklı.
**Açık:** aporia durdurma eşiği; tanım-netleşme ve çelişki-fark-etme için hazır metrik; Princeton SocraticAI, sartak gist, ChatGPT/Gemini prompt metinleri.

## Geçerlilik ve sınırlar
- AS-OF 2026-10-29; üç kaynak (Paul-Elder kitabı, 2504.06294, CHARM) tam metin okunamadı; BU PDF 403 verdi; çoğu ürün bilgisi ikincil haber/blog.
- Sayısal değerler yalnız kaynağın verdiği biçimde alındı; "6-8 tur" önerisi **kestirimdir** `[?]`.
- Salih bağlamı (kişisel kavram netleştirme) ile kaynakların bağlamı (sınıf, öğrenci) farklı; aktarım kanıtsız.
- Üst-ajan için sorulması gereken karar: Sokrates ajanı saf Sokratik mi (tek soru, cevap yok) yoksa grill karışımı mı (öneri cevaplı, olgu araştıran)? Kanıt ikinciyi destekliyor ama Salih'in amacına bağlı.

## Kaynaklar (toplu)
1. https://arxiv.org/abs/2303.08769
2. https://arxiv.org/html/2512.03501v1
3. https://library.iated.org/view/SUVERNEV2026SOC
4. https://neurips.cc/virtual/2024/poster/93477 · https://github.com/CMLF-git-dev/SocraticLM
5. https://arxiv.org/pdf/2406.11709v4
6. https://par.nsf.gov//servlets/purl/10510120
7. https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2019.00126/pdf · https://arxiv.org/pdf/2504.06294
8. https://www.anthropic.com/news/introducing-claude-for-education
9. https://techcrunch.com/2025/08/06/google-takes-on-chatgpts-study-mode-with-new-guided-learning-tool-in-gemini/
10. https://aiweekly.co/alerts/khanmigo-ai-tutor-falls-short-of-khan-academy-hype · https://www.edweek.org/technology/opinion-can-an-ai-powered-tutor-produce-meaningful-results/2025/07
11. https://github.com/mattpocock/skills · https://github.com/brianlovin/agent-config
12. https://git.fri.uni-lj.si/martin.vuk/socratic-tutor · https://github.com/Nydv01/fossee-python-evaluation · https://huggingface.co/jakemaly/Gemma4-31B-Socratic-LoRA
13. https://www.newcastle.edu.au/__data/assets/pdf_file/0020/1134830/PDF_Designing-a-Socratic-Tutor-Agent-in-Cogniti.pdf · https://www.craigbellamy.net/images//Build_a_GPT_as_a_Socratic_Tutor_LaTrobe.docx · https://aihub.msstate.edu/resources/06-socratic-ai-tutor.html
14. https://arxiv.org/pdf/2402.10962v1 · https://arxiv.org/pdf/2412.00804 · https://arxiv.org/abs/2512.12775 · https://arxiv.org/abs/2605.24279
15. https://arxiv.org/pdf/2609.01352 · https://arxiv.org/pdf/2601.06437 · https://www.alphaxiv.org/abs/2603.03915
16. https://arxiv.org/html/2508.06583v2 · https://arxiv.org/pdf/2510.12899 · https://arxiv.org/pdf/2606.01020
17. https://arxiv.org/abs/2607.03303 · https://open.bu.edu/bitstreams/2547d4f0-a878-4ebd-830b-ea40643c66f3/download · https://www.iatrox.com/blog/socratic-ai-tutors-vs-answer-first-chatbots

**Epistemolojik not:** bu rapor 2026-10-29 anlık görüntüsüdür; arama özeti kaynaklı `[S]` satırlar birincil metinle doğrulanmadan kanona girmemeli.
