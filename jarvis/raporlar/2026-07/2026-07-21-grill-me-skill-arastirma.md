# "Grill Me" Skill — Araştırma Raporu (yan-oturum)

> **Yüzey (m.41):** Bu **yan-oturum** (CC, Opus — Fable değil / "ana sıra" beyanı yok) çıktısıdır. Kanona DOKUNMAZ; imza masasına/ana-sıraya **aday**dır, kilitli karar değildir. Salih talebi, 2026-07-21. Etiketler: **D**=birincil kaynak · **K**=arama/ikincil · **X**=doğrulanamadı. Cevaplanmamış sorular metne gömülüdür (karar biriktirme yok).
>
> **Koşum:** 1 araştırma ajanı (general-purpose, sonnet) · web taraması + JARVIS `ogrenme/` repo okuması · ~110k token / 50 araç-koşumu.

---

## Carvis notu — karar-adayları (m.41, kilitlenmedi)

Rapor iki gerçek karar yüzeyi açıyor; ikisi de **Katman-1/2**, bu oturumda kilitlenmez — Salih/ana-sıra işidir:

1. **V55 pasif-okuma varsayılanı vs. aktif-sorgulama.** Rapora göre öğrenme şeridi 2026-07-15'te bilinçle pasif-okumaya geçmiş (tempo gerekçesi) ve "gerçek anlama ölçümü ileriye ertelendi" borcunu kendi kaydına düşmüş. Grill-me tam bu ertelenmiş boşluğu dolduran hazır mekanizma. Rapor bunu **varsayılan-değişimi olarak değil**, üstüne binen *isteğe bağlı doğrulama geçişi* olarak öneriyor — doğru çerçeve; varsayılanı değiştirmek ayrı bir Salih kararı.
2. **Kur vs. JARVIS-natifi üret.** İki yol: (a) Pocock'un skill'ini olduğu gibi kur (`npx skills add` / plugin) — ama `.claude/` yazımı bu yan-oturumda YAPISAL kilitli, kurulum ana-sıra/Salih işi; (b) K-016 eval-önce akışıyla JARVIS-natif bir `sinav`/`grill` skill'i üret — [S]/[O]/[T] derinlik etiketleri + "bulanık blok" çıktısıyla öğrenme şeridine gömülü (karar-modeli ve atlas-kosum'un üretildiği akışın aynısı).

**Şimdi bedelsiz kullanılabilir:** §3'teki hazır-yapıştır şablon kurulum gerektirmez — bugün bir derste denenebilir.

---

**Özet çerçeve:** "Grill me" hem (a) somut, isimlendirilmiş, GitHub'da yayınlı bir Claude Code skill'i hem de (b) bu skill'in de üstünde durduğu daha genel bir teknik (adversarial Sokratik sorgulama / decision-tree interview). İkisini ayrı ayrı, birincil kaynaklardan doğrulayarak raporluyorum. Etiketler: **D** = birincil kaynaktan doğrulandı, **K** = arama/ikincil özet, teyit gerekir, **X** = doğrulanamadı.

---

## 1) "Grill me" isimli somut bir skill var mı?

**D — Evet, var; ama Anthropic'in resmi/kanonik skill'i DEĞİL.**

- **Yaratıcı:** Matt Pocock — "Total TypeScript" eğitmeni, şu an **AI Hero** (aihero.dev) adlı, ~60.000 aboneli bir "AI ile gerçek mühendislik" bültenini yürütüyor. [D — [README](https://github.com/mattpocock/skills/blob/main/README.md)]
- **Depo:** [`github.com/mattpocock/skills`](https://github.com/mattpocock/skills) — "Skills for Real Engineers. Straight from my .agents directory." MIT lisanslı (kök `LICENSE` dosyasını doğrudan çektim: *"MIT License, Copyright (c) 2026 Matt Pocock"*). [D]
- **Tam konum:** `skills/productivity/grill-me/SKILL.md`, ve üç kardeşi: `skills/productivity/grilling/`, `skills/engineering/grill-with-docs/`, `skills/in-progress/batch-grill-me/` (detay §2'de). [D — GitHub API ile dosya listesi doğrudan çekildi]
- **Anthropic'in resmi deposunda YOK.** `github.com/anthropics/skills`'i doğrudan kontrol ettim — oradaki kategoriler Creative & Design, Development & Technical, Enterprise & Communication, Document skills (docx/pdf/pptx/xlsx); "grill-me" hiçbir yerde geçmiyor. [D] Yani grill-me, Anthropic'in resmi, taşınabilir **Agent Skills formatını** (SKILL.md + YAML frontmatter — claude.ai / Claude Code / Claude API arasında ortak, açık bir standart) kullanıyor ama Anthropic'in kendisi **yazmamış**; üçüncü-taraf/topluluk kaynaklı. [D — format iddiası için [anthropic.com/engineering](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills), [platform.claude.com/docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)]
- **Viral yayılım (doğrulanmış):** Depo 2026-02-03'te açıldı; bugün itibarıyla (GitHub API, canlı sorgu) **178.821 yıldız / 15.295 fork**. [D — doğrudan `api.github.com/repos/mattpocock/skills`] Pocock'un kendi X paylaşımı: *"My 'grill-me' skill went viral. mattpocock/skills is up to 9K stars... It's the most useful skill I've written, and I use it even outside of coding."* [D — [x.com/mattpocockuk](https://x.com/mattpocockuk/status/2036076132924100760), ama doğası gereği kendi-beyanı] Ara zamanlı üçüncü-taraf rakamlar (Nisan 2026'da ~14K yıldız, "ilk 24 saatte 22K" iddiası) büyüme eğrisiyle tutarlı — çelişki değil, farklı zaman noktalarında alınmış anlık görüntüler. [K]
- **Diğer agent ekosistemlerine taşınmış:** `chaseai-yt/grill-me-codex` (OpenAI Codex portu, MIT, 763 yıldız — API ile doğrulandı), `alirezarezvani/claude-skills`, `vclimenco/claude-code-skills`, `ericgandrade/claude-superskills`, `satya-janghu/agent-skills` — hepsi mattpocock/skills'ten türetilmiş kopyalar. Her skill klasöründe bir `agents/openai.yaml` dosyası var — bu, skill'in Claude Code dışında Codex gibi ajanlara da taşınabilmesi için adaptör konfigürasyonu. [D/K karışık]
- **Reddit/Hacker News:** Doğrudan "grill me"ye adanmış bir tartışma başlığına rastlamadım; aramalar genel Claude Code kapsamına döndü. Asıl viral kanal **X/Twitter + blog/newsletter** ekosistemiydi. **Simon Willison**'ın grill-me'ye özel bir yazısına da rastlamadım (Willison'ın Claude Skills hakkında genel yazıları var, ör. *"Claude Skills are awesome, maybe a bigger deal than MCP"*, ama grill-me'yi konu aldığını gösteren bir kaynak bulamadım). [X — bulunamadı, iddia edilmiyor]

---

## 2) Nasıl çalışıyor (mekanizma) — birincil kaynaktan tam alıntı

Ailenin **4 parçası** var, hepsi tek bir çekirdek "primitive"i paylaşıyor:

| Skill | `disable-model-invocation` | Tetik | Durum-tutma | Ne yapar |
|---|---|---|---|---|
| **`grilling`** | yok → Claude kendi kararıyla da tetikleyebilir | `/grilling` veya "grill" tetik-sözcükleri | Stateless | Çekirdek motor — diğer üçü bunu çağırır |
| **`grill-me`** | `true` → yalnız kullanıcı yazınca çalışır | `/grill-me` | Stateless, dosya yazmaz | Salt görüşme; sohbetten başka artefakt yok |
| **`grill-with-docs`** | `true` | `/grill-with-docs` | Stateful | Aynı görüşme + `CONTEXT.md` sözlüğü ve ADR yazar |
| **`batch-grill-me`** *(in-progress)* | `true` | `/batch-grill-me` | Stateless | Tek-tek yerine "frontier" (o an sorulabilecek tüm sorular) turlar halinde sorar |

**`grilling/SKILL.md`'nin tam, birebir metni** (bu — asıl mekanizma; İngilizce orijinal, kaynak kod olduğu için değiştirmeden aktarıyorum):

```
---
name: grilling
description: Grill the user relentlessly about a plan, decision, or idea. Use when
  the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.
---

Interview me relentlessly about every aspect of this until we reach a shared
understanding. Walk down each branch of the decision tree, resolving dependencies
between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time, waiting for feedback on each question before
continuing. Asking multiple questions at once is bewildering.

If a *fact* can be found by exploring the environment (filesystem, tools, etc.),
look it up rather than asking me. The *decisions*, though, are mine — put each one
to me and wait for my answer.

Do not act on it until I confirm we have reached a shared understanding.
```
[D — `raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grilling/SKILL.md`, doğrudan çekildi]

`grill-me/SKILL.md` kasıtlı olarak ince bir kabuk: `name`, `description: "A relentless interview to sharpen a plan or design."`, `disable-model-invocation: true`, gövde tek satır — *"Run a `/grilling` session."* `grill-with-docs` da aynı desende, tek fark gövdesi: *"Run a `/grilling` session, using the `/domain-modeling` skill."* [D — ikisi de raw dosyadan doğrudan çekildi]

**Mekanik kurallar** (kaynak: [docs/productivity/grilling.md](https://github.com/mattpocock/skills/blob/main/docs/productivity/grilling.md), [docs/productivity/grill-me.md](https://github.com/mattpocock/skills/blob/main/docs/productivity/grill-me.md), CHANGELOG — hepsi D):

1. **Decision tree modeli:** Hedef (plan/karar/fikir) bir karar ağacı olarak modellenir; **derinlik-öncelikli** (depth-first) gezilir — bir dalın sonuna kadar inip öyle yan dala geçilir. Erken bir cevap sonraki soruları yeniden şekillendirdiği için bu sıra önemli.
2. **Tek seferde tek soru**, her zaman kendi **önerilen cevabıyla** birlikte — kullanıcı boş sayfadan yazmak yerine öneriye tepki verir (bu, Pocock'a göre uzun oturumu yorucu olmaktan çıkaran şey).
3. **Gerçek (fact) vs. karar (decision) ayrımı:** Ortamdan (dosya sistemi, araçlar) bulunabilecek her şey ajan tarafından bulunur, kullanıcıya sorulmaz; yalnız gerçek yargı gerektiren kararlar kullanıcıya sorulur. Bu kural PR #464'te sertleştirildi — çünkü `grilling` başka bir skill içinde iç içe çalıştırıldığında **kendi sorularını kendi cevaplamaya** başlamıştı; bu açıkça istenmeyen bir davranış olarak düzeltildi. [D — CHANGELOG.md]
4. **Periyodik özet duraklaması** ve **onay kapısı (confirmation gate):** Kullanıcı paylaşılan anlayışa ulaşıldığını onaylamadan hiçbir şey uygulanmaz/inşa edilmez — bu PR #464'te açık bir "stop-gate" haline getirildi. [D]
5. Ağacın tüm dalları çözülünce veya kullanıcı durunca biter; kapanışta kararlar + ertelenen konuların özeti verilir.

**Yaratıcının kendi tanımı** (aihero.dev, birincil kaynak, D): grill-me'yi **"rubber ducking"**un (kauçuk ördeğe sesli düşünme) etkileşimli haline benzetiyor — *"Before AI came along, devs called this rubber ducking — talking through your idea until you figured out all the permutations."* Kod-dışı kullanımını da doğruluyor: *"It's also great for non-coding use cases. I've used it for figuring out what course to build next."* Tipik oturum ~45 dakika; çıktı kod değil, *"a rich conversation full of context, your actual ideas, and answers to difficult questions."* [D — [aihero.dev/my-grill-me-skill-has-gone-viral](https://www.aihero.dev/my-grill-me-skill-has-gone-viral)]

**Bağımsız yorum** (Medium, Marc Bara) meseleyi iyi çerçeveliyor: skill'in değeri ajanı akıllandırmak değil, **kasıtlı sürtünme** yaratmak — *"They do not make the agent smarter. They make it slower in exactly the places where slowing down matters."* [K — [medium.com/@marc.bara.iniesta](https://medium.com/@marc.bara.iniesta/the-ai-coding-repo-that-went-viral-because-it-adds-friction-e2b5c4d2fcc2)]

**Topluluk baskısıyla genelleşme:** [Issue #527](https://github.com/mattpocock/skills/issues/527)'de bir kullanıcı (behnamazimi) grilling'in yalnız "plan/tasarım"a değil, *"an opinion... an argument I'm making"* gibi konu-bağımsız durumlara da uygulanabilmesini istedi ve `grill-everything` adlı bir fork yazdı. Ayrı olarak, repo'nun CHANGELOG'unda bunu destekleyen bir changeset var: *"Reword grilling for general use... 'this plan' → 'this', 'exploring the codebase' → 'exploring the environment'. The technique is unchanged; it now reads as a stress-test of any plan, decision, or idea."* [D — `.changeset/grilling-general-use.md`] (İki olgu arasında doğrudan bir nedensellik iddia edilen bir kaynak bulamadım — sadece ikisini de doğrulanmış olgular olarak bildiriyorum.) **Sonuç: çekirdek teknik artık resmen konu-bağımsız — sadece yazılım planlarına özgü değil.**

**Flashcard/pasif quizden farkı:** Flashcard/"quiz me" tipik olarak önceden hazırlanmış soru-cevap çiftleriyle **sabit** bir test yapar (active recall — bilgiyi hafızadan çekme, ama dallanma yok). Grill-me'nin ayırt edici özelliği: (a) soru sırası **önceki cevaba göre dinamik** (karar ağacı gezintisi), (b) **takip sorularıyla ısrarcı** derinleşme ("bir dalın sonuna kadar in"), (c) kullanıcının **kendi cümlesiyle açıklamasını zorunlu kılan** bir çerçeve. Ayrı bir öğrenme-odaklı ürün olan **GuruOwl**, tam bu ayrımı pazarlama diliyle yapıyor: *"grills you until it sticks... makes you explain each answer, catches the concept you only half-know."* [K — yalnız arama özetinden; `guruowl.com`'a doğrudan erişim **403 Forbidden** ile engellendi, birincil doğrulama yapılamadı, **erişim bloğu bayrağı**]

---

## 3) Öğrenme şeridinde nasıl kullanılır + hazır şablon

### Mevcut sisteminizle kesişim (repo içi bulgular)

`ogrenme/` şeridinizi okudum ve doğrudan ilgili bir bulgu var:

- 2026-07-15'te (`ogrenme/README.md`, V55) eski bir **aktif-sorgulama** deseninden ("anlama-kapısı": *"(A) Anladın mı — kendi cümlenle yaz... yanlışsa sertçe düzeltirim"*, bkz. `ogrenme/anlama-kapisi.md`) bilinçli olarak **pasif-okuma** modeline geçilmiş — Carvis soru sormuyor, doğru formülasyonu doğrudan yazıp farkı anlatıyor. Gerekçe: tempo/sürtünme.
- Hem `ogrenme/README.md` hem bugüne kadarki en son ders kaydınız (`ogrenme/dersler/2026-07-19-P3-rope-context.md`) **aynı açık maddeyi** taşıyor: *"Ölçüm notu: pasif-okuma modeli → gerçek anlama ölçümü uygulamaya taşınır (hata koşumda çıkarsa oraya gömülür)."* Yani sistem kendi kendine, gerçek anlama doğrulamasının eksik olduğunu ve ileri bir tarihe ertelendiğini şimdiden not etmiş durumda.

**Grill-me tarzı sorgulama, tam olarak bu ertelenmiş boşluğu dolduran hazır bir mekanizma.** Bunu V55'in pasif-okuma varsayılanını değiştirme önerisi olarak değil — üstüne binen, **isteğe bağlı bir doğrulama geçişi** olarak sunuyorum (varsayılanı değiştirmek Katman-1/2 kararı; bu rapor yalnızca aracı ortaya koyuyor).

Ayrıca sisteminizde zaten olan iki kavram, grill-me'nin çıktısıyla doğrudan eşleşiyor:
- **Derinlik etiketi [S]/[O]/[T]** → sorgulamanın zorluk kadranı olarak yeniden kullanılabilir (bir [S] bloğa [T] derinliğinde soru sormamak gibi).
- **"Bulanık blok"** → grilling'in "geçemedi" çıktısı için zaten var olan, sisteminizin tanıdığı bir kategori (`README.md`: *"önceki dersten BULANIK blok kaldıysa önce onların v2 formatıyla yeniden geçişi"*) — yani grilling'in bulguları, elle yeni bir mekanizma icat etmeden, mevcut yeniden-öğretme akışına doğrudan girebilir.

### Somut iş akışı

1. Ders DONE olduktan sonra (örn. `.html` teslimi + `dersler/*.md` kaydı), **ayrı bir oturumda veya aynı oturumun sonunda**, dersin kaynağını (html içeriği veya md'deki blok özetleri) **önce yapıştırın** — grilling bu kaynağa göre çalışmalı, hafızadan değil.
2. Aşağıdaki şablonu tetikleyin.
3. Çıktıdaki "BULANIK" listesini `dersler/*.md`'nin "Açık borç / taşınan" veya "DONE kapısı" bölümüne yapıştırın; bir sonraki oturumun açılışında bu liste zaten var olan "önceki dersten BULANIK blok kaldıysa..." kuralını tetikler.
4. Oturum uzunluğu için mevcut disiplininizi koruyun ("tek teslimde 2-3 kavramlık blok") — grilling geçişini de ders başına sınırlı tutun; Pocock'un kendi bildirdiği ~45 dk, planlama-grilling için tipik ama öğrenme-grilling'i konu başına daha kısa tutmak (her blok birkaç dakika) mantıklı.

### Hazır-yapıştır şablon (Türkçe, kaynak-temelli)

```
ROL: Bu dersin acımasız ama adil SINAYICISISIN — öğretmen değil, sorgulayıcısın.
Amacın onaylamak değil, gerçek anlama ile ezber/yanılsama arasındaki farkı ortaya
çıkarmak.

KAYNAK (önce bunu oku, kendi genel bilginden değil BUNDAN konuş):
[BURAYA ders dosyasının/HTML'in içeriğini yapıştır. Kaynak yapıştırılmadan
sorgulama BAŞLAMAZ — eksikse önce kaynağı iste.]

KURALLAR:
1. Yalnız yukarıdaki kaynakta olan/ondan çıkarılabilen şeyleri sorgula. Kaynakta
   olmayan bir "doğru cevap" uydurma; emin değilsen "kaynakta bu net değil" de.
2. Her kavram bloğunu KENDİ derinlik etiketiyle ([S]/[O]/[T]) ele al — [S]
   etiketli bir kavrama [T] derinliğinde soru sorma.
3. Tek seferde TEK soru sor, cevabı bekle. Soru yığını yok.
4. Her blok için ÖNCE "bunu kendi cümlenle anlat" iste (kendi kelimelerinle
   açıklama zorunlu) — o anlatmadan ipucu verme, kendi cevabını kendin verme.
5. Cevap yanlış/eksikse: (a) kaynaktan BİREBİR alıntıyla düzelt (hangi
   satır/paragraf), (b) aynı kavramı farklı açıdan tekrar sor.
6. Cevap doğruysa ona bağımlı bir sonraki dala geç (önce temel kavram, sonra
   ona dayanan ileri kavram — dallanma sırasını koru).
7. Asla erken onaylama, asla kanıtsız övgü yapma ("harika!" gibi boş geçiş yok);
   yalnız çıplak gözlemle ilerle.
8. Emin olmadığın bir düzeltmeyi kendinden emin bir tonda sunma — kaynak
   yetersizse "bulanık: kaynak yetersiz" diye işaretle, uydurma.

KAPANIŞ (oturum sonunda bu formatta özet ver — doğrudan dersler/*.md'ye
yapıştırılabilir):
## Grilling özeti — [ders adı, tarih]
- GEÇTİ: [kendi cümlesiyle doğru anlattığı bloklar]
- BULANIK: [yanlış/eksik/tereddütlü kalan bloklar + hangi alt-noktada takıldığı]
- Takip: [bulanık kalanlar için önerilen tekrar-geçiş veya ek örnek]
```

Bu şablon, Pocock'un orijinal `grilling` motorunun beş kuralını (decision-tree, tek-soru, fact-vs-decision, onay-kapısı, kapanış özeti) öğrenme bağlamına uyarlıyor; asıl fark, "karar ağacı"nın yerine "kavram ağacı"nı, "kod tabanını keşfet"in yerine "yapıştırılan kaynağı keşfet"i koyması (bkz. §4 — bu, halüsinasyon riskine karşı kasıtlı bir tasarım).

### Gerçek skill'i kurmak isterseniz (Claude Code)

Öğrenme dışı, mühendislik/plan bağlamlarında (örn. Carvis bir build adımını Salih'e sormadan önce grillemek isterse) orijinal skill'i kurmanın yolları [D — README + docs sayfalarından]:

```bash
# Tek skill, düzenlenebilir kopya:
npx skills add mattpocock/skills --skill=grill-me

# veya interaktif seçici (tüm skill setini gösterir):
npx skills@latest add mattpocock/skills

# veya Claude Code plugin (salt-okunur, otomatik güncellenen paket):
/plugin marketplace add mattpocock/skills
/plugin install mattpocock-skills@mattpocock
```
Kurulumdan sonra `/grill-me` (salt görüşme) veya `/grill-with-docs` (görüşme + ADR/sözlük yazımı) ile çağrılır. Not: ham skill metni "plan/tasarım/kod tabanı" diliyle yazılmış — öğrenme içeriğine uygulamadan önce yukarıdaki şablon gibi yeniden ifade etmek (tıpkı bakımcının kendi `grilling-general-use` değişikliğinde yaptığı gibi) daha isabetli olur. **Yüzey notu (m.41):** `.claude/` yazımı bu yan-oturumda yapısal kilitli — kurulum ana-sıra/Salih işidir.

---

## 4) Tuzaklar ve iyi pratikler

- **AI'nin yumuşaması / sycophancy riski (K, dikkatle okunmalı):** [arXiv 2605.14604](https://arxiv.org/abs/2605.14604) *"Sycophancy is an Educational Safety Risk: Why LLM Tutors Need Sycophancy Benchmarks"* (2026, çok yeni bir preprint — akran değerlendirmesi görmemiş, ihtiyatla okunmalı) bir **"Reasoning-Sycophancy Paradox"** tanımlıyor: bazı saldırgan çerçevelemelere direnen modeller bile **otorite baskısı** ("notlarım doğru diyor") veya **yüz-kurtarma baskısı** ("lütfen yanlış olduğumu söyleme") altında geri adım atabiliyor. Bu makalenin özetinde Claude'un test edilen altı disiplinlik kıyaslamada *"substantial context-switch fragility"* gösterdiği belirtiliyor — bu ortamda kullanılan modelle ilgili olduğu için özellikle not edilmeli. Ayrı bir makale ([arXiv 2510.03667](https://arxiv.org/pdf/2510.03667), *"Invisible Saboteurs: Sycophantic LLMs Mislead Novices"*) benzer bulguyu doğruluyor (K, yalnız başlık/özet seviyesinde incelendi). **Pratik sonuç:** şablonda "erken onaylama yok, kanıtsız övgü yok" kuralı bilerek sert tutulmalı; kullanıcı ısrar ederse/kendinden eminse model geri adım atmaya eğilimli olabilir — kaynağa-alıntı-zorunluluğu (kural 5) bu riski azaltan somut bir fren.
- **Halüsine "yanlış cevap" geri bildirimi:** Kaynak-belgesi olmadan (hafızadan) grilleme yapılırsa, model hem yanlış bir "düzeltme" uydurabilir hem de dersin kendine özgü çerçevesini (JARVIS'e özel örnekler, sizin terminolojiniz) genel bilgisiyle karıştırıp doğru cevabı yanlış işaretleyebilir. Bu yüzden şablonda kaynak yapıştırma **zorunlu ilk adım**, ve düzeltmeler kaynaktan birebir alıntıyla gerekçelendirilmeli — bu, Pocock'un orijinal "fact vs. decision" kuralının (ortamdan bulunabilecek şeyi sorma, bul) genelleştirilmiş hali.
- **Zorluk kalibrasyonu:** Mevcut [S]/[O]/[T] etiketlerinizi zorluk kadranı olarak kullanmak pratik bir çözüm. Daha genel olarak, retrieval-practice literatüründe görev zorluğunun öğrenme kazanımını etkilediği gösterilmiş — bkz. [PMC10698739](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10698739/) *"How task difficulty and academic self-efficacy impact retrieval practice guidance."* [K]
- **Bilişsel temel (neden işe yarar):** "Testing effect" / retrieval practice — bilgiyi hafızadan aktif çekmenin yeniden-okumaktan daha kalıcı öğrenme sağladığı, eğitim psikolojisinde iyi belgelenmiş bir bulgu ([Wikipedia: Testing effect](https://en.wikipedia.org/wiki/Testing_effect); [PMC3983480](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3983480/), *"Retrieval practice enhances new learning: the forward effect of testing"*). Kendi cümlenle-açıklama (self-explanation) ile retrieval practice'in **birlikte** kullanımının tek başına ikisinden daha güçlü olduğu bulunmuş ([ResearchGate 237093763](https://www.researchgate.net/publication/237093763_Comparative_effects_of_test-enhanced_learning_and_self-explanation_on_long-term_retention)) — şablondaki "önce kendi cümlenle anlat" kuralı (kural 4) tam bu ikiliyi birleştiriyor. [K]
- **Sokratik yöntem araştırması:** LLM'lerde Sokratik sorgulamanın akıl yürütmeyi güçlendirdiğine dair akademik çalışma var ([arXiv 2303.08769](https://arxiv.org/abs/2303.08769), Edward Y. Chang, *"Prompting Large Language Models With the Socratic Method"*); Princeton NLP'nin [SocraticAI](https://princeton-nlp.github.io/SocraticAI/) projesi benzer bir çoklu-ajan diyalog yaklaşımı sunuyor. Ayrıca genel-amaçlı, öğrenmeye özel bir Sokratik-öğretmen promptu örneği (grill-me'den bağımsız, muhtemelen ondan önce yaygınlaşmış): [sartak'ın gist'i](https://gist.github.com/sartak/80ca7e31d03d7d6ca32ccf0dcba9467d) — "ilerlemeden önce test sorularıyla dur, öğrenci tatmin edici cevap verene kadar devam etme" ilkesini taşıyor; şablonunuzdaki "önce anlat, geçmezse devam etme" mantığıyla aynı aile. [K]
- **Oturum uzunluğu:** Pocock'un bildirdiği tipik grilling oturumu ~45 dk (plan/tasarım bağlamında) — öğrenme bağlamında muhtemelen daha kısa tutulmalı; mevcut "tek teslimde 2-3 kavram" temponuzla hizalı, tüm dersi tek grilling turunda bitirmek yerine blok-blok ilerlemek tutarlı olur.
- **Tek-tek soru vs. toplu tur:** Eğer tek-soru-bekle ritmi yavaş gelirse, `batch-grill-me`'nin "frontier" (o an cevaplanabilir tüm sorular tek turda, numaralı, önerilen cevaplı) yaklaşımı bir alternatif — ama yazarın kendisi bunu hâlâ "in-progress" (deneysel) olarak işaretlemiş, yani en olgun/test edilmiş sürüm değil. [D]
- **"Sınayıcı, yorumcu değil" ilkesi:** Orijinal skill'in en sık vurgulanan tasarım kuralı — kendi sorusunu kendin cevaplama, istenmeden çözüm sunma, erken onaylama, revize taslak üretme. Öğrenme şablonunda bu ilke korunmalı; aksi halde "grilling" sessizce tekrar pasif-okumaya geri kayar.

---

## 5) Kaynaklar

**Birincil (grill-me ekosistemi, GitHub/aihero.dev):**
- [github.com/mattpocock/skills](https://github.com/mattpocock/skills) — depo, README, lisans
- [skills/productivity/grill-me/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md)
- [skills/productivity/grilling/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md)
- [skills/engineering/grill-with-docs/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md)
- [skills/in-progress/batch-grill-me/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/in-progress/batch-grill-me/SKILL.md)
- [docs/productivity/grilling.md](https://github.com/mattpocock/skills/blob/main/docs/productivity/grilling.md) · [docs/productivity/grill-me.md](https://github.com/mattpocock/skills/blob/main/docs/productivity/grill-me.md) · [docs/engineering/grill-with-docs.md](https://github.com/mattpocock/skills/blob/main/docs/engineering/grill-with-docs.md)
- [CHANGELOG.md](https://github.com/mattpocock/skills/blob/main/CHANGELOG.md) · [.changeset/grilling-general-use.md](https://github.com/mattpocock/skills/blob/main/.changeset/grilling-general-use.md)
- [Issue #527 — konu-bağımsız grilling talebi](https://github.com/mattpocock/skills/issues/527)
- [aihero.dev/my-grill-me-skill-has-gone-viral](https://www.aihero.dev/my-grill-me-skill-has-gone-viral) — yaratıcının kendi anlatımı
- [x.com/mattpocockuk/status/2036076132924100760](https://x.com/mattpocockuk/status/2036076132924100760)
- [github.com/anthropics/skills](https://github.com/anthropics/skills) — negatif kontrol (grill-me burada YOK)
- [github.com/chaseai-yt/grill-me-codex](https://github.com/chaseai-yt/grill-me-codex) — Codex portu

**Format/standart (Anthropic resmi):**
- [anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [platform.claude.com/docs/en/agents-and-tools/agent-skills/overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [rajeevpentyala.com — disable-model-invocation açıklaması](https://rajeevpentyala.com/2026/06/29/disable-model-invocation-control-when-your-coding-agent-auto-invokes-a-skill/)

**İkincil (kapsam/inceleme, K-seviyesi):**
- [medium.com/@marc.bara.iniesta — "adds friction" analizi](https://medium.com/@marc.bara.iniesta/the-ai-coding-repo-that-went-viral-because-it-adds-friction-e2b5c4d2fcc2)
- [awesomeskill.ai/skill/mattpocock-skills-grill-me](https://awesomeskill.ai/skill/mattpocock-skills-grill-me) · [claudemarketplaces.com/.../grill-me](https://claudemarketplaces.com/skills/mattpocock/skills/grill-me) · [claudedirectory.org/skills/claude-skills-grill-me](https://www.claudedirectory.org/skills/claude-skills-grill-me)
- [mcp.directory — "the npm moment" büyüme anlatısı](https://mcp.directory/blog/matt-pocock-skills-the-npm-moment-explained-2026)

**Pedagojik/bilişsel temel:**
- [Wikipedia — Testing effect](https://en.wikipedia.org/wiki/Testing_effect) · [PMC3983480](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3983480/) · [PMC10698739](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10698739/) · [ResearchGate 237093763](https://www.researchgate.net/publication/237093763_Comparative_effects_of_test-enhanced_learning_and_self-explanation_on_long-term_retention)
- [arXiv 2303.08769 — Socratic Method prompting](https://arxiv.org/abs/2303.08769) · [Princeton SocraticAI](https://princeton-nlp.github.io/SocraticAI/) · [sartak gist — Sokratik öğrenme promptu](https://gist.github.com/sartak/80ca7e31d03d7d6ca32ccf0dcba9467d)

**Riskler:**
- [arXiv 2605.14604 — Sycophancy educational safety risk](https://arxiv.org/abs/2605.14604) (çok yeni preprint, ihtiyatlı okunmalı) · [arXiv 2510.03667 — Invisible Saboteurs](https://arxiv.org/pdf/2510.03667)

**Erişim engeli:**
- `guruowl.com` — **403 Forbidden**, doğrudan doğrulanamadı; yalnız arama-özeti seviyesinde (K) kullanıldı.

**Repo-içi (bu araştırmanın §3 zeminini oluşturan, JARVIS deposundan okunan dosyalar):**
- `C:\JARVIS\ogrenme\README.md`, `C:\JARVIS\ogrenme\anlama-kapisi.md`, `C:\JARVIS\ogrenme\dersler\2026-07-19-P3-rope-context.md`
