# spec-kit (github/spec-kit) jarvis bağlamında — Atlas Raporu (2026-08-13)

> **Mod:** ana-sıra (terminal, Katman-1 geçişi sonrası ilk büyük koşum) · şerit: çift-atlas (tez ∧ ¬tez) + maskeli hakem · aile sayısı: 3
> **Soru (Salih, 08-13):** Ekip liderinin otomasyon sistemi için tasarımına aldığı github/spec-kit, tüm jarvis bağlamında hangi sorunlarımıza çözüm bulur; sisteme nasıl entegre ederiz?
> **Kanıt kısıtı (dürüstlük):** Reddit tamamen erişilemedi (403) — saha ailesi Reddit kanıtı içermiyor. ¬A3 koşumunda arama bütçesi tükendi; karşı-felsefe kaleminin (Naur/Gonzalez/Petre/Whittle) antitez taraması EKSİK kaldı — o kalemler "sağlam ama tek-şerit" damgalı. Birkaç kaynak 403/paywall (VS Magazine, EPAM, bazı ACM DL) — raporda tek tek bayraklı.
> **md.49 sınır notu:** spec-kit public bir depo; bu rapor yöntem bilgisidir, staj verisi içermez. Ekip liderinin sistemine dair hiçbir iç bilgi bu koşumda kullanılmadı.

## 0. Koşum sicili (m.40b v0.2)

- 9 ajan koşumu: 3 tez (A1 mekanizma · A2 saha · A3 kıyas/konum) → 3 hedefli antitez (CoVe-Factored: yalnız iddia listesi, kanıt zinciri verilmeden) → 3 maskeli hakem (üretici≠doğrulayıcı; taraflar kimliksiz). Toplam ~1,1M ajan-tokeni `[?]` (kaba toplam), ~9 saatlik ajan-duvar-saati paralelde ~4 saate sıkıştı.
- **V26 örneklem-denetimi: 6 ajanda 18+ iddia, TAMAMI GEÇTİ** (tablo §5). Bir çapraz-alarm çıktı ve çözüldü: ¬A1, kendi alt-koşumunda yeniden üretemediği HN alıntılarını uydurma şüphesiyle atmıştı; aynı kullanıcı adları A2'nin kaynağıydı → altı HN alıntısının altısı Algolia API'den birebir doğrulandı, A2 temiz çıktı.
- Hakem sayımları: **A1: 1 SAĞLAM · 8 DARALDI · 4 DÜŞTÜ** (13 nokta) · **A2: 5 SAĞLAM · 6 DARALDI · 3 DÜŞTÜ** (14) · **A3: 1 SAĞLAM · 9 DARALDI · 4 DÜŞTÜ · 1 ÇELİŞKİLİ** (15). Toplam 42 nokta: **7 sağlam · 23 daraldı · 11 düştü · 1 çelişkili**.

## 1. spec-kit nedir (hayatta-kalan mekanizma çekirdeği — tamamı D)

- **Konum:** GitHub'ın resmî org'unda, MIT lisanslı "Spec-Driven Development (SDD) araç seti". Uygulama değil: `specify` CLI (Python 3.11+/uv, Typer) + ajan-tarafında slash-komut/skill şablonları. 2025-08-21 doğumlu; bugün v0.16.2; ~127k yıldız. Kendi beyanı: "our experiment" (github.blog duyurusu).
- **Çekirdek akış (10 komut):** `/speckit.constitution → specify → clarify → plan → checklist → tasks → analyze → implement → converge` (+`taskstoissues`). Plan öncesi tek zorunlu adım `specify`. Komut semantiği sıkı: `analyze` salt-okunur, `converge` ekleme-only (kod→spec yakınsama), `implement` checklist'i kapı olarak okur (kapı sert değil: işaretsiz maddede durup sorar; işaretleri değiştiremez).
- **Artefakt düzeni:** kök işaretçisi `.specify/`; anayasa `.specify/memory/constitution.md`; özellik başına `specs/NNN-ad/` altında spec/plan/tasks/research/data-model/quickstart/contracts. Aktif özellik git dalından DEĞİL `.specify/feature.json`dan çözülür. Şablonlar 4-katman öncelikle çözülür (overrides>presets>extensions>core).
- **Entegrasyon matrisi:** 38 kayıt (catalog=docs=kaynak birebir; README'deki "30+" bayat pazarlama). **Claude Code entegrasyonu skills-tabanlı** (`.claude/skills/speckit-*`); Copilot varsayılanı da v0.16.0'da skills'e döndü.
- **Otomasyon yüzeyi (v0.16, bizim için kritik):** YAML-tanımlı, **resumable workflow motoru** — 11 adım tipi (gate/if/while/fan-out/fan-in dahil); resmî `speckit` workflow'unda iki insan-onay kapısı (`review-spec`, `review-plan`, `on_reject: abort`); kapılar `verdict_input` ile AÇIK delegasyonla makineye bağlanabilir; koşum çıktısı `--json`. Fan-out `max_concurrency` ile thread-pool'da paralel (dokümandaki "sequential" satırı bayat — CHANGELOG #3224 ile doğrulandı). `shell` adımlarında **sandbox yok** — belgeli tasarım kararı, azaltım reçetesi "gate ile koru".
- **Çok-ajan:** çekirdekte bilinçli olarak YOK (bakımcı beyanı: ajan-bağımsız sözleşme yok → eklenti/preset katmanına). Worktree/paralel-izolasyon çekirdeğe ALINMADI — bakımcı açık sözle eklenti/preset katmanına havale etti (#1476 → topluluk eklentisi PR #2207; hakem hükmü: bu iddia SAĞLAM — antitezin "aslında teslim edildi" okuması yanlış-atıf üzerine kuruluydu ve çöktü).

## 2. Saha kanıtı (A2 — hakem sonrası durum)

**Ayakta kalanlar:**
- **Kullanım tabanı gerçek:** ~10k public repo constitution taşıyor; yerleşim sayımı skills lehine 11:1 (eski `.claude/commands` sayıları ölü yerleşimi ölçüyor). Microsoft org'unda 8 repo; bakımcılık fiilen Microsoft'ta.
- **GitHub kendi ürünlerinde kullanmıyor** (org:github'da tek sonuç spec-kit'in kendisi) ve **hiçbir kontrollü ölçüm yayımlamadı**.
- **Küçük işte süreç yükü gerçek ve üretici tarafından kabul edilmiş:** Scott Logic ölçümü (aynı iş düz iteratif promptlamadan ~10× yavaş; 2.577 satır markdown/689 satır kod — rakamlar birincil metinde birebir; ANCAK 2025-11 sürümüne ait, bugünkü araçla ölçülmedi) · Böckeler (kopya-sınıf üretimi; spec başına 8 dosya ↔ Kiro 3; Eylül 2025 şerhli) · çekirdeğe cevap olarak `lean` preset geldi (5 komut, %93,6 küçük şablon).
- **En yüksek-sinyalli açık: spec'i YERİNDE güncelleme.** Repo rekortmeni issue (105👍) bir eklenti-katalog kaydıyla kapatıldı; `converge` yalnız kod→spec yönlü ve append-only; genel refine/reconcile hâlâ eklenti; #620 açık.
- Token farkı: yön doğru (spec-kit daha ağır), büyüklük ~%30 mertebesinde (viral "2×" ölçümü n=1, sürümsüz, çıkar-çatışmalı — düştü). Şablon gövdeleri büyümeye devam ediyor (~130KB).

**Düşenler:**
- "Her oturumda 18,6k token vergisi" — Nisan 2026 skills geçişiyle mekanizma kalktı (ön-yükleme ~246 token; tam gövde yalnız çağrılınca).
- "SSRN çalışması spec-kit aleyhine ampirik kanıt" — çalışmanın örnekleminde SIFIR spec-kit çıktısı var; muamele "PR'da issue linki"; yazarın kendi cümlesi: *"SDD tool adoption itself remains untested."* +1,4pp manşeti hakem sürecinde geri çekildi (PSM'de null).
- "Illusion-of-work açık yarası" — issue'yu şikâyetçi kendisi `completed` kapattı.

**Kurumsal sinyal:** SNCF Connect&Tech CTO'su 2-4× hız beyanı (SDD *yaklaşımına* — BMad+Spec Kit; 2 kişilik greenfield pilot; kontrollü ölçüm değil) · Microsoft Learn enterprise modülü + Dev Blog birinci-taraf yazısı · 279 gerçek CI workflow'u sahada (ör. OpenELIS: speckit-validate PR kapısı).

**Yönetişim riski (A1 hakem bulgularıyla):** fiilî bakımcı 1 kişi (kurucu 2025-12'de Anthropic'e geçti; 67 gün tam duruş; "Is this project dead?" dönemi; sonra tek-kişilik yoğun diriliş) · açık issue'ların ~%65-69'u bakımcı-yanıtsız; stale-bot kapanışları şişiriyor · **AI-slop PR akını:** açık kuyruğun %27'si tek hesap; aynı saniyede açılmış 10'lu PR yığını; savunma issue'su 92 gün yorumsuz (bu bulgu bağımsız denetimden SAĞLAM çıktı) · CHANGELOG'da "breaking" kaydı sıfır ↔ 550 satırlık uyarılı upgrade rehberi.

## 3. Ekosistem konumu (A3 — hakem: 1 SAĞLAM · 9 DARALDI · 4 DÜŞTÜ · 1 ÇELİŞKİLİ)

- **Kamplar:** spec-first tam-spec (spec-kit) ↔ delta-spec iteratif (OpenSpec, 64,8k★ — "built for brownfield **not just** greenfield") ↔ persona-ordusu (BMAD, 51,9k★, spec-kit'ten 4 ay yaşlı) ↔ kapalı-ürün (AWS Kiro; EARS **varsayılan ama zorunlu değil** [¬A3 düzeltmesi]; Q Developer IDE hattı 2027'de Kiro'ya devrediliyor) ↔ worktree+kanban koşum katmanı (Spec Kitty 1,5k★; KiroCrew 2,8k★ Apache-2.0). Tessl SDD'den skills platformuna pivot etti (pivot tartışmasız; "duyurulu mu sessiz mi" hakem kapatamadı [X]). Böckeler taksonomisi alanın ortak dili: **spec-first / spec-anchored / spec-as-source**; spec-kit bugün fiilen spec-first, spec-anchored'a "özenen".
- **Doktrin ↔ ürün açığı:** "specifications become executable / PRD değişince planlar otomatik güncellenir" retoriği duruyor; fiilî artefakt düz markdown, CLI'da spec-linter yok (#1862 açık; `analyze` ajan-yürütmeli denetim). Dokuz-madde anayasa şablonda "boş" değil — Articles IV-VI bilinçli proje-tanımlı (2026-06-23 doktrin güncellemesi).
- **Karşı-felsefe hattı:** Thoughtworks Radar iki cilttir Assess'te tutuyor ("bitter lesson" uyarısı; instruction bloat — ölçümle bugün de doğru: şablonlar v0.7.1→v0.16.2 arası +%31,7); Naur teori-önceliği ve MDE tarihi (UML 35/50 kullanmıyor; kod-üretimi "red herring") paraleli pratisyen kanadın zemini. ŞERH: bu eleştirilerin çoğu 80-131 sürüm önceki artefaktı ölçtü ve olumlu cümleleri seçici düşürülmüştü (¬A3); antitezin felsefe-kalemi taraması eksik kaldı — tek-şerit damgası.
- **Ampirik durum (koşumun en net düzeltmesi):** "veri yok" İDDİASI DÜŞTÜ. Doğrulanmış külliyat: arXiv **2606.30689** (ön-kayıtlı, 840 uygulama, spec-kit vs OpenSpec vs traceSDD: alıntısız koşullar daha determinist [d≈−0,7], AMA otomatik halüsinasyon tespiti yalnız alıntı-disiplinli koşulda: TDR %86-88 vs %0) · **2605.18461** (kurumsal brownfield: tek kişi + 4 ajan, planlanan sürenin yarısı, %90 ilk-inceleme kabulü) · **2602.02584** (constitution kısıtları → güvenlik defekti −%73) · **2605.01160** (67-kaynaklı MLR; METR'in %19 yavaşlamasını "spec disiplini eksikliği" semptomu olarak okuyor). Beş kimlik V26'da + hakem çift-doğrulamasında gerçek çıktı. Hakem şerhi: altısı da ÖN-BASKI, yalnız ikisi karşılaştırmalı-kontrollü, hiçbiri insan-denekli değil — "veri yok" düştü ama "hakemli zemin var" da denemez. Hâlâ YOK olan: insan-denekli RCT, DORA SDD-özel verisi, standart metrikler.
- **Çok-ajan gerçeği:** spec-kit çekirdeği tek-ajan + insan-döngüde; katalogdaki "çok-ajan" kalemleri cılız (171 depo, yıldız medyanı 4, toplamı spec-kit'in %1,1'i; MAQA 9★/2-günlük). Olgun paralel-ajan uygulaması spec-kit'in DIŞINDA: Spec Kitty ve KiroCrew.

## 4. Sentez — hayatta-kalan çekirdek

1. **Mekanizma güvenilir belgelendi; karar zemini sağlam.** Anatomi iddialarının ~%90'ı birincil kaynakla birebir doğrulandı.
2. **Ölçek-bağımlılık artık kanıtlı desen:** küçük/iteratif işte spec-first net kayıp (10× vakası, "sledgehammer/nut", lean itirafı); yüksek-belirsizlikli, çok-parçalı, denetim-gerektiren işte kazanç sinyali (SNCF, brownfield vakası, constitution-güvenlik çalışması). Hiçbir kamp insan-denekli kontrollü çalışmayla desteklenmiyor.
3. **spec-kit'in gerçek değeri süreç-iskeleti + anayasa kapısı + makine-okur workflow'u;** zayıf karnı yaşayan-spec bakımı ve tek-bakımcı yönetişimi.
4. **"GitHub'ın resmî aracı" statüsü abartılmamalı:** deney konumlaması, dogfooding yok, ölçüm yok — ama ölü/oyuncak da değil: bugün yüksek tempolu, gerçek kurumsal kullanıcılı, hızla evrilen bir proje.

## 5. V26 örneklem-denetimi

| Ajan | Denetlenen | Sonuç |
|---|---|---|
| A1 tez | repo API rakamları · kanonik komut sırası · README slash tablosu | 3/3 GEÇTİ (D hakkı korundu) |
| A2 tez | #1191 105👍 · #1401 gövdesi (18.6k/%93) · commit boşluğu · +hedefli: 6 HN alıntısı (Algolia) | 4+6 GEÇTİ |
| A3 tez | OpenSpec künyesi · workflow README ("resumable", fan-out) · #1476 + bakımcı alıntısı | 3/3 GEÇTİ |
| ¬A1 | GraphQL 157/173 ayrımı · PyPI 52 sürüm · Maintainers-silme commit'i | 3/3 GEÇTİ |
| ¬A2 | lean preset varlığı · (#1191 closed — önceki denetimle çakışık teyit) | GEÇTİ |
| ¬A3 | MAQA istatistiği · v0.16.0 skills-varsayılanı · 5 arXiv kimliği | 5+2 GEÇTİ |

Etiket düşürme gerekmedi; tüm aileler D-uygunluğunu korudu. (K-damgalı kalemler metin içinde tek tek işaretli.)

## 6. JARVIS eşlemesi — hangi sorunumuza ne söylüyor

| # | Bizim sorun/yapı | spec-kit karşılığı | Hüküm |
|---|---|---|---|
| 1 | **Tüzük → işleyen kural** (entegrasyon fazının ana konusu: "kanon md'leri workflow'a") | `constitution.md` + plan-aşaması "Constitution Check" kapısı + `analyze`'da ihlal=CRITICAL. Kapılar doğal-dil metninden türetiliyor — sabit kod değil | **EN GÜÇLÜ EŞLEME.** Tüzüğün makine-yüzü için hazır, sahada koşan desen. arXiv 2602.02584 yönü destekliyor (−%73 güvenlik defekti) [K] |
| 2 | **Görev-emri derleme / masa-hazırlık usulü** (m.17 köprü; cc/gorev-*.md el yapımı) | `specify → clarify → plan → tasks` zinciri: niyet → netleştirme (≤5 soru) → plan → bağımlılık-sıralı, [P]-işaretli görev listesi | Usulümüzün araçlaşmış hâli. `clarify`'ın ≤5-soru disiplini m.4 soru-eşiğimizle akraba |
| 3 | **Done-yüklemi** (pano kuralı: DONE alanı boş kart açılamaz) | Acceptance criteria + `checklist` ("unit tests for English"; reviewer-owned, ajan self-approve edemez) | 08-02 raporundaki EARS önerisiyle birleşir; EARS spec-kit'te hâlâ açık istek (#1356), Kiro'da varsayılan |
| 4 | **K-009/K-010 otomasyon-ajan kapıları** (A2 guardrail, A3 kontrol-devri) | Workflow motoru: insan-onay `gate` + `on_reject: abort` + `verdict_input` (açık, beyan edilmiş delegasyon) + `--json` + resumable state | Kapı tasarımımızla izomorf; A3 kapısının "sabit-promptlu Routine" kanıtları için emsal. DİKKAT: `shell` sandboxsuz — bizim pretool-tel/deny katmanı olmadan koşulmaz |
| 5 | **K-019 boyut sigortası / kararlı-prefix** | Token bulguları: komut gövdeleri şişiyor (+%31,7), çözüm progressive-disclosure (skills) + lean preset | Pointer-sistemimizin (m.20/m.22) üçüncü bağımsız doğrulaması — kanonumuz literatürle yine yakınsadı |
| 6 | **Firstmate/treehouse hattı** | spec-kit tek-ajan intake; çok-ajan bilinçle dışarıda. Spec Kitty deseni (worktree-başına görev + kanban + review→merge döngüsü) bizim treehouse+firstmate yapımızın birebir akrabası | RAKİP DEĞİL TAMAMLAYICI: spec-kit'in `tasks.md`'si firstmate tayfa-görevlerinin intake'i olabilir |
| 7 | **K-022 staj** (ekip liderinin sistemi spec-kit üstüne) | Bu raporun tamamı + özellikle: sürüm hızı (eleştirilerin çoğu bayat), skills-yerleşimi, `--skip ci` benzeri Gotcha'lar, workflow motoru | Salih'in doğrulama-katmanı rolü için yöntem cephanesi. Staj verisi jarvis'e girmedi; raporu staj tarafında kullanmak serbest (md.49: yöntem yönü serbest) |
| 8 | **V1 ilkesi** (iterasyon > spec-first) | Doktrin çatışıyor; saha kanıtı ölçek-eşikli hibrit gösteriyor | m.16 raporu → §7 |

## 7. m.16 çelişki raporu — V1 ↔ spec-first (KARAR SALİH'TE)

**Çelişki:** Tüzük V1 "iterasyon > spec-first" der; spec-kit'in doktrini "önce spec, kod spec'e hizmet eder" der. Entegrasyon bu hâliyle V1'le çatışır.

**Bulgunun çelişkiye etkisi:** Saha kanıtı iki ilkeyi AYNI eksende değil, ölçek ekseninin iki ucunda konumluyor — küçük/belirsiz işte iterasyon kazanıyor (10× vakası, lean itirafı), büyük/çok-parçalı/denetimli işte spec-önce kazanç sinyali veriyor (SNCF, brownfield vakası, halüsinasyon-tespit çalışması). m.25 (görev-ölçek optimizasyonu) zaten bu ayrımı yapıyor; m.21 (bağlam-detay ölçekleme) ile de uyumlu.

**Öneri (karar değil):** V1 korunur + şerh eklenir: *"Ölçek-eşiği üstü, çok-ajan/otomasyon-sınıfı işlerde intake spec-önce olabilir; eşik altında iterasyon esastır."* Artılar: iki dünyanın kanıtlı güçlü yanları; firstmate intake'ine doğal oturur. Eksiler: eşik muğlaklığı yeni karar yükü üretir; spec-bakımı (yaşayan-doküman) bizim damıtma kültürüne ek yük — spec-kit'in kendi çözemediği alan.

## 8. Entegrasyon yolu — ADAYLAR (karar masası Salih'e)

- **Seçenek A — dar deneme (önerilen ilk adım):** `~/dev/wf-deneme`'de tek koşum: `uv tool install specify-cli` → `specify init` (claude entegrasyonu, skills) → constitution'a tüzük-özütü (m.6/m.8/m.9 sınıfı 3-5 madde) → `specify→plan→tasks` zinciri küçük-orta bir işte → çıkan `tasks.md` firstmate'e intake → **P6 dörtlüsüyle ölç** (token·süre·iterasyon·sonuç; kıyas: aynı iş düz firstmate intake'iyle). Maliyet ~1 oturum. Çürütme koşulu baştan: dörtlüde düz-intake'e karşı kazanç yoksa B'ye düşülür.
- **Seçenek B — desen aktarımı (araçsız):** spec-kit alınmaz; üç desen kanonumuza işlenir: (1) constitution-kapısı → görev-emri şablonuna "tüzük-kontrol" bloğu, (2) acceptance-criteria/checklist → done-yüklemi standardı, (3) clarify'ın ≤5-soru intake'i → m.4 usulüne. Maliyet: yazım turu. (HN'deki "araçsız SDD yeter" kanadının yolu — bizim CLAUDE.md/wiki yapımız zaten yarısını kuruyor.)
- **Seçenek C — bekle-izle:** jarvis'e alma; spec-kit akıcılığı staj tarafında kazanılır (ekip lideri zaten kullanıyor), 2-3 ay sonra tek-bakımcı riski + sürüm temposu yeniden değerlendirilir.
- **Riskler (hangisi seçilirse seçilsin):** deneysel konumlanış + bus-factor 1 + breaking-change disiplinsizliği (sürüm SABITLE: `@vX.Y.Z`) · Python/uv bağımlılığı · token ağırlığı (~%30) · `shell` sandboxsuzluğu (bizim deny/pretool katmanı şart) · spec-birikimi ↔ kapsül-üzerine-yazılır kültür çatışması.

## 9. Cevaplanmamış sorular (karar biriktirilmedi — m.41)

1. İnsan-denekli kontrollü SDD çalışması yok — "2-4×" sınıfı beyanlar beyan olarak kalıyor.
2. Ekip liderinin sistemi spec-kit'in hangi sürümünü/modunu kullanıyor (skills mi commands mi; workflow motoru açık mı)? — Salih staj tarafında öğrenecek; jarvis'e yalnız yöntem dersi taşınır.
3. Render-docs "49/50 entegrasyon" ↔ ham kaynak 38 tutarsızlığının açıklaması bulunamadı.
4. EARS entegrasyonu (#1356) açık — bizim done-yüklemi/EARS hattımız (08-02 raporu) için izlenecek.
5. `plansDirectory`/plan-kalıcılığı gibi hızlı değişen yüzeylerde bu raporun raf ömrü kısa: **eleştiri de övgü de sürüm-damgasız taşınmamalı** (bu koşumun ana epistemik dersi).

---
*Koşum-sonrası istatistik (m.40b deneysel damga): 42 hakem-noktası — 7 SAĞLAM · 23 DARALDI · 11 DÜŞTÜ · 1 ÇELİŞKİLİ. Koşumun epistemik dersleri (A3 hakeminin ortak-kör-nokta tespiti, iki yönde de geçerli): (1) kanıt SÜRÜM-DAMGASIZ taşınmamalı — eleştiri de övgü de; (2) artefaktın VARLIĞI canlılığı değildir (katalog kaydı ≠ yetenek, yıldız ≠ olgunluk); (3) alıntı toplamak kanıt tartmak değildir. Ham ajan çıktıları oturum scratchpad'inde; kalıcı kanıt bu rapor + URL'ler.*
