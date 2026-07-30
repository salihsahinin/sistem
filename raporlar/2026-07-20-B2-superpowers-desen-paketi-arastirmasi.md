# B2 — "Superpowers" Desen Paketi (TDD · systematic-debugging · subagent-driven-development) — Atlas Raporu (2026-07-20)

> **Mod:** yan-oturum (m.41 · CC = yan oturum, kanon KİLİTLENMEDİ, karar ALINMADI) · şerit: çift-atlas (tez ∧ ¬tez) · aile sayısı: **5** (Superpowers-nedir/meta · TDD · systematic-debugging · subagent-driven-development · ünlü-isimler) → 10 literatür/pratisyen şeridi + 1 skill/disiplin karar envanteri.
> **Salih notu (ne olduğu açıklaması):** Bu rapor, paketin "tam olarak ne olduğunu" §0 ve §1'de SADE anlatır — Salih notu gereği. Kısa cevap §0'ın ilk kutusunda.
> **Kanıt kısıtı (dürüstlük):** Birincil `SKILL.md` dosyaları (obra/superpowers repo) çoğunlukla DOĞRUDAN çekildi **[D]**. Egress-403 verenler: `blog.fsck.com` (obra duyurusu), `anthropic.com/engineering/*`, `simonwillison.net`, `cognition.ai`, `jvns.ca`, birkaç arXiv → o bulgular WebSearch-özeti **[K]** veya GitHub-aynası **[D-ayna]**. Doğrulanamayan sayılar ("174-180k yıldız", "%95 fix", benimseyen-şirket listesi) §5'te işaretli, raporlanmadı.
> **Okuma sırası (Fable):** §0 Carvis sentezi (+ "nedir" kutusu) + §4 dürüst bayraklar → yeterli. Detay: §1 aile bulguları · §2 ünlü isimler · §3 skill-kararlarımızın kategori+kontrolü · §5 V26 · §6 açık sorular.

---

## §0 — Carvis sentezi (önce oku)

**"Superpowers TAM OLARAK NEDİR" (Salih için sade tanım):** Superpowers = Jesse Vincent'ın (takma-ad "obra") yaptığı bir **Claude Code eklentisi (plugin)** — kodlama-ajanına "önce düşün/planla, sonra kod yaz" disiplinini bir **markdown *skill* koleksiyonu** olarak yükleyen paket. Bir *skill* = ajanın belirli bir durumda izlemek ZORUNDA olduğu, markdown'a kodlanmış prosedür (öneri değil, **zorunlu iş-akışı**). Marketplace'ten `/plugin install` ile kurulur; session-start hook oturum başında bir bootstrap enjekte eder; ajan işi algılayınca ilgili skill'i **otomatik tetikler**. İçinde ~13 skill var: brainstorming · writing-plans · **subagent-driven-development** · **test-driven-development** · **systematic-debugging** · verification-before-completion · code-review · git-worktrees · dispatching-parallel-agents · writing-skills (meta). Felsefesi dört ilke: **süreç > tahmin**, **kanıt > iddia**, TDD test-önce, sadelik. Kısaca: *"disiplini kağıda değil, ajanın davranışına gömen; ajan kuralın etrafından dolaşmaya kalkınca kapıyı kapatan"* bir sistem.

**En sağlam kesişim (beş ailenin İKİ şeridinin de + envanterin ortak dediği):**

1. **MANŞET: JARVIS bu yığının neredeyse TAMAMINI bağımsız olarak zaten KANON halinde yeniden-icat etmiş.** Envanter birebir eşliyor: TDD ≈ **m.9** (proof-of-work=push) + DONE-kuralı ("pytest yeşil + push") + **V39** (makine-ölçülebilir evaluator); systematic-debugging ≈ **m.5** (sorun-güdümlü iterasyon) + senaryo-defteri vaka-kaydı; subagent-driven ≈ **m.37/m.40** (çift-atlas) + **m.42** (düşük-temp icra ajanları) + KILAVUZ Kompozisyon kuralı (`context:fork` orkestratör + çocuk skill + sabit-handoff + fail-loud) + **m.20 pointer** (= görev-brifini DOSYAYA yaz, metin yapıştırma); skill-authoring ≈ **m.43** (skill ≥3 tekrarda doğar) + KILAVUZ Skill Standardı (SKILL.md<500 satır, description=NE+NE ZAMAN, Gotchas, eval-önce) + **V25** (kurulum yok, yeniden yaz). Hatta **S-A/S-B skill'leri ÜRETİLDİ** (eval 3/3). ⇒ **Superpowers, JARVIS mimarisinin YAKINSAK DOĞRULAMASIDIR — benimsenecek yeni araç değil.** [D + envanter]

2. **Her ailede tek mesaj: DİSİPLİNİ benimse (zaten büyük ölçüde kanon), PAKETİ reddet.** V25 "kurulum yok yeniden yaz" estetik NIH değil, **tedarik-zinciri savunması** — marketplace aktif güvenlik yüzeyi (Snyk ToxicSkills: skill'lerin %36'sı zafiyetli, 71 kötücül Claude skill'i; skill tam-yetkiyle koşar, prompt-injection savunması baypas). Ve skill-savunan kaynak ile şişmeye-karşı-uyaran kaynak AYNI (Anthropic'in kendi rehberi "az/öz/eval-test-edilmiş/tek-tip skill" diyor) → skill değerli AMA az+kendi-yazılmış+eval-güdümlü disiplin olarak = **tam olarak V25+m.43+K-016**. [D/K]

3. **İki "uyum-eşiği" çizgisi net.** (a) **TDD DETERMİNİSTİK-kabul işine oturur** (PortRisk pytest-yeşil, V39), araştırma/kanon/wiki'ye (öznel, altın-cevapsız) OTURMAZ — B-tez∧B-antitez ekseni = JARVIS'in kendi ölçüm-işi vs araştırma-işi ayrımı. (b) **subagent-driven MELEZ:** JARVIS'in paralelliği Anthropic **araştırma-modeli** (salt-okunur, çakışmasız — bu raporun kendisi), obra'nın **sıralı-yazma modeli DEĞİL** (obra'nın SKILL.md'si paralel-yazmayı YASAKLAR: "çakışma"). Sıkı-bağımlı kanon/yazmada ASLA fan-out. [D]

4. **Skill'lerin GERÇEK değeri: yeti değil, KONTRAT/denetlenebilirlik.** S-A eval sonucu tam bunu söylüyor: with-skill 6/6 assertion, baseline 2/6 → "katma değer zekâ değil KONTRAT (denetlenebilirlik + kanon zinciri)". Ve skill'lerin ÇÖZMEDİĞİ hata modları model-düzeyinde (confirmation-bias, "düzelttim" aşırı-güveni, reward-hacking yeşil-test) — bu oturumun 8-saat-stall yanlış-okuması + A5'in LLM-judge κ≈0.51'i kanıt. Bunlar için gereken **dış falsifikasyon-kapısı** (m.9 ruhu), daha çok skill değil. [D]

**JARVIS'e ne demek (gözlem, KARAR DEĞİL — m.41):**

- **Dürüst manşet:** Superpowers bir AYNA — JARVIS'in doğru disiplinleri, çoğunu önden kurduğunu doğruluyor. Net-yeni küçük: (1) KILAVUZ'a madenlenebilir 2-3 somut desen (≥3-yama→dur-mimariyi-sorgula kuralı · çift-aşamalı spec-önce-sonra-kalite review · dosya-tabanlı görev-brifi = zaten m.20); (2) **kepano/obsidian-skills JARVIS'in Obsidian vault'una (V24 [[wiki-link]]) doğrudan uygulanabilir aday**; (3) eval-güdümlü skill-authoring (Executor/Grader) zaten K-017 ilhamı.
- **JARVIS'in borçlu olduğu uzlaştırma:** obra "spec-first" ("specs matter, code doesn't") ↔ V1 "iterasyon > spec-first". Göründüğü kadar zıt DEĞİL: obra'nın "spec"i bir kodlama-görevi için = plan/test; V1 belirsiz-iş için büyük-tasarım-önden'i reddeder. Çizgi TDD çizgisiyle AYNI: **deterministik-kabul işi → spec/test-önce sorun değil (PortRisk); keşif/araştırma işi → iterasyon-önce (CV araştırması, bu rapor).** V1 ile superpowers-spec-first ÇELİŞMEZ, iş-tipine göre BÖLÜNÜR.
- **En yüksek-kaldıraçlı üç gözlem (harita, öneri değil):** (1) 2-3 somut deseni KILAVUZ'a madenle (paketi kurma); (2) TDD-disiplini ölçüm-işine ait (PortRisk/V39), araştırmaya değil; (3) skill değeri KONTRAT — zaten sahip olunan eval-önce/Grader disiplinini genişlet, skill SAYISINI kovalama.

---

## §1 — Aile başına bulgular (çift-atlas)

### Aile A — "Superpowers nedir" (meta)
- **Tez:** (Tam tanım §0 kutusunda.) obra/Jesse Vincent'ın CC eklentisi; ~13 zorunlu-oto-tetiklenen markdown skill; "process over vibes"; skill'ler zincir halinde birbirini çağırır (brainstorm→worktree→plan→subagent-dev(TDD)→review→finish). JARVIS referans-değeri: skill=markdown-süreç-paketi = KILAVUZ ontolojisi; session-start hook + oto-tetik = m.41 hook emsali. [D README]
- **Antitez (¬):** Kendini "eksiksiz yazılım-geliştirme metodolojisi" (KOD odaklı) diye tanımlıyor — JARVIS'in araştırma/kanon/wiki işi değil; plugin-kurulumu V25'e aykırı; ~13 oto-yüklenen skill prefix-bütçesini şişirir (K-019); dış-bağımlılık + sürüm-kayması. En fazla ilham. [D]
- **Kesişim:** NET tanım verildi; JARVIS için değer İLHAM düzeyinde (V25), paket düzeyinde değil — çünkü hedef-problem (kod-üretimi) JARVIS'in problemi değil; JARVIS ileride kod-ağırlıklı faza geçse bile "yeniden-yaz, kurma" kapısı kalır.

### Aile B — Test-Driven Development
- **Tez:** TDD = "başarısız test olmadan tek satır kod yok" (Kent Beck RED-GREEN-REFACTOR + Uncle Bob 3 Yasa); Superpowers bunu test-öncesi kodu SİLDİREN skill-kapısı yapar; AI+TDD gücü = spec=test → doğrulanabilir çıktı. JARVIS'te ZATEN örtük: K-002 pytest-yeşil done + m.36c ölçüm-bankı + V39 makine-ölçülebilir evaluator; mount yanlış-yeşil vakası tam TDD'nin "başarısızlığı İZLE" kuralının yakaladığı şey. [D/K]
- **Antitez (¬):** TDD yalnız spec-stabil/altın-cevaplı/test-yazılabilir işe verim; JARVIS'in araştırma/kanon/wiki'si (öznel, iterasyon-güdümlü) uymaz; "yeşil test" gameable vekil → yanlış-güven (ImpossibleBench GPT-5 %76 hile; reward-hacking assertion-silme/`exit(0)`; Goodhart); DHH "test-induced design damage"; meta-analiz net verim kazancı YOK (%15-35 düşüş); spec-first ↔ V1 gerilimi. [D/K]
- **Kesişim:** TDD **deterministik-kabul işine** (PortRisk/V39/ölçüm-bankı) oturur, araştırma/kanon/wiki'ye oturmaz — eksen = JARVIS'in kendi iş-tipi ayrımı. İki şerit ORTAK: yeşil-test tek başına halüsinasyon-kalkanı DEĞİL.

### Aile C — Systematic-debugging
- **Tez:** 4-fazlı ("DEMİR YASA: kök-neden araştırması bitmeden düzeltme YOK"; yeniden-üret → örüntü-karşılaştır → tek-hipotez-test → failing-test-önce-düzelt; ≥3-yama→dur-mimariyi-sorgula). LLM'in halüsinasyonlu "düzelttim"ini yapısal engeller; m.5 + senaryo-defteri + 8-saat-stall canlı örneğiyle hizalı. [D SKILL.md]
- **Antitez (¬):** Skill = tören, yeti değil (kök-neden zaten iyi-ajan varsayılanı); asıl sorun (confirmation-bias / "düzelttim" aşırı-güveni) MODEL-düzeyinde, metinle düzelmez (Failing-to-Falsify ICLR'26 11 model; Materialize 80+ ajan var-olmayan bug'ı onayladı; bu oturumun stall yanlış-okuması); gerçek kaldıraç = dış falsifikasyon-kapısı (m.9), skill değil. [K/X arXiv 403]
- **Kesişim:** DİSİPLİNİ benimse (yeniden-üret + kök-neden + failing-test-gate + ≥3-yama-dur), skill-paketlemesine ve onun aşırı-güveni çözeceğine şüpheci kal; küçük hataya 4-faz ağır (m.25 ölçek).

### Aile D — Subagent-driven-development
- **Tez:** "Her alt-görevi taze-bağlamlı işçiye ver, sadece özet dönsün, orkestratör bağlamı temiz kalsın"; işçiler session-context MİRAS ALMAZ; görev-brifleri DOSYAYA yazılıp yol geçilir (= m.20 pointer!); çift-aşamalı review (spec→kalite) + fix-subagent + progress.md ledger. JARVIS bağı: Carvis=orkestratör = m.17; progress.md = kapsül/pano; capable-model-final-review = m.21. **Kritik:** obra paralel-yazmayı YASAKLAR; paralel-fayda BAŞKA desende (Anthropic çoklu-araştırma). [D SKILL.md]
- **Antitez (¬):** orkestratör-işçi ~15× token (varyansın %80'i); taze-bağlam = cache-miss tam-fiyat (A2); Cognition: subagent'lar birbirini görmez → çelişen karar → kırılgan (Flappy Bird→Super Mario örneği); özet-dönüş = kayıplı sıkıştırma; çok-ajan sıkı-bağımlı işte (kod/kanon = JARVIS çekirdeği) zayıf; B1+A2 ile üçlü yakınsama. [D/K]
- **Kesişim:** Bağlam-mühendisliği çekirdeğini (taze-bağlam + brief-dosyaya + özet-dönüş = zaten m.20/m.22/m.17) benimse; **JARVIS iki desenin melezi** — paralel-koşumu yalnız salt-okunur/araştırmaya (Anthropic modeli) tut, sıkı-bağımlı kanon/yazmada ASLA fan-out; her göreve değil ölçek-eşiği üstüne (m.25).

### Aile E — Ünlü isimler / pratisyen
- **Tez:** obra (process>vibes, skills-that-write-skills); Anthropic Agent Skills (eval-driven: dokümanı yazmadan ÖNCE eval; progressive-disclosure SKILL.md<500 satır); Agent Skills açık standart (agentskills.io, Ara 2025); **kepano/obsidian-skills (açık-format köprüsü — JARVIS vault'una doğrudan aday)**; Skill Creator 2.0 (Executor/Grader = TDD-for-skills). JARVIS bağı: m.43/K-016 doğrudan model; progressive-disclosure = m.22/m.21. [D-ayna/K]
- **Antitez (¬):** skill-şişmesi ölçülü (Vercel %56 hiç çağrılmadı; context-rot limit-içinde bile kaliteyi bozar; description-çakışması→yanlış-tetikleme); "process over vibes" aşırısı → cargo-cult/tören; marketplace = güvenlik yüzeyi (Snyk ToxicSkills %36 zafiyetli, tedarik-zinciri); Anthropic'in KENDİ rehberi "az/öz" diyor. V25+m.43 zaten sigorta. [D/K]
- **Kesişim:** E-tez ve E-antitez YAKINSIYOR — skill-savunan ve şişmeye-karşı-uyaran AYNI kaynak → skill değerli AMA az/kendi-yazılmış/eval-test-edilmiş disiplin olarak, kurulu paket olarak değil = V25+m.43+K-016. Gerilim: obra spec-first ↔ V1 iterasyon>spec (iş-tipine göre bölünür, §0).

---

## §2 — Ünlü isimler / kaynak tablosu

| İsim | Alan/yöntem | Özü | JARVIS bağı | Kaynak | Etiket |
|---|---|---|---|---|---|
| Jesse Vincent (obra) | Superpowers yaratıcısı | "process>vibes"; skills-that-write-skills; brainstorm→spec→TDD | m.43/K-016 doğrudan model; spec-first ↔ V1 gerilimi | [github.com/obra/superpowers](https://github.com/obra/superpowers) · [blog.fsck.com](https://blog.fsck.com/2025/10/09/superpowers/) [X 403] | [D]/[K] |
| Kent Beck | TDD | "Başarısız otomatik test olmadan tek satır kod yazma" | K-002 pytest-yeşil done | [Fowler bliki](https://martinfowler.com/bliki/TestDrivenDevelopment.html) | [D] |
| "Uncle Bob" Martin | TDD 3 Yasa | Döngüyü mekanik kapıya çevirir | V39 evaluator disiplini | [cleancoder](https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html) | [D] |
| DHH | "TDD is dead" | Test-induced design damage; test-first dogma | V1 iterasyon>spec dayanağı | [Fowler: Is TDD Dead?](https://martinfowler.com/articles/is-tdd-dead/) | [K] |
| Julia Evans | Debugging | Yeniden-üret + böl + çıktı-bas | systematic-debugging pratisyen temeli | [jvns.ca](https://jvns.ca/) [X 403] | [K] |
| Anthropic | Agent Skills | Eval-driven + progressive-disclosure + açık standart | m.22/m.21/m.9; K-016 eval-önce | [platform.claude.com Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) | [K] |
| Steph Ango (kepano) | obsidian-skills | Ajanı Obsidian açık-formatına disiplinle bağlar | **JARVIS vault'una doğrudan aday (V24)** | [github.com/kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | [K] |
| Skill Creator 2.0 | Executor/Grader/Comparator/Analyzer | TDD-for-skills; kör A/B (onay-yanlılığı freni) | K-017 ilhamı; m.9 kanıt-mantığı | [github.com/anthropics/skills](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | [K] |
| Cognition (Walden Yan) | "Don't Build Multi-Agents" | Tek-yazar; subagent'lar çelişir→kırılgan | subagent-driven fan-out ihtiyatı | [cognition.ai](https://cognition.ai/blog/dont-build-multi-agents) [X 403] | [K] |
| Snyk | ToxicSkills | Skill'lerin %36'sı zafiyetli; tedarik-zinciri | V25 "kurulum yok" = güvenlik savunması | [snyk.io ToxicSkills](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/) | [D] |

---

## §3 — Skill/disiplin kararlarımızın kategori + kontrolü (superpowers merceğiyle)

Envanter, her superpowers desenine bir JARVIS-kanon karşılığı buldu. Özet + kontrol:

| Superpowers deseni | JARVIS kanon karşılığı | Statü | Kontrol (bu araştırmanın verdiği) |
|---|---|---|---|
| **TDD** | m.9 (push-kanıtı) · DONE-kuralı "pytest yeşil+push" · V39 makine-evaluator · K-002 | imzalı + üretiliyor | ✅ Ölçüm-işine oturur (PortRisk/V39); ⚠️ yeşil≠doğru (mount vakası); araştırmaya taşınmamalı. |
| **systematic-debugging** | m.5 (sorun-güdümlü) · senaryo-defteri vaka-kaydı · loop-eng "hatayı yakalayan kuralı skill'e göm" | imzalı | ✅ Disiplin hizalı; ⚠️ skill-tören aşırı-güveni çözmez (dış falsifikasyon gerek). |
| **subagent-driven-dev** | m.37/m.40 çift-atlas · m.42 (düşük-temp) · KILAVUZ Kompozisyon (`context:fork`) · m.20 pointer · m.17 | imzalı + S-B üretildi | ✅ Bağlam-mühendisliği zaten kanon; ⚠️ paralel yalnız salt-okunur/araştırma; ölçek-eşiği (m.25). |
| **skill-authoring** | m.43 (≥3 tekrar) · KILAVUZ Skill Standardı (<500 satır, Gotchas, eval-önce) · V25 | imzalı + üretiliyor | ✅ Birebir; description=trigger (Anthropic rehberi) zaten KILAVUZ'da. |
| **eval-driven / verification** | K-016 (eval-önce) · K-017 (Executor/Grader ilhamı) · K-020 · V26 · m.16 | aktif | ✅ S-A/S-B eval 3/3 üretildi; "değer=KONTRAT" bulgusu. |
| **brainstorming→plan→spec** | V36/m.40b (araştırma-önce) · m.37 (3-model) | imzalı | ⚠️ obra spec-first ↔ V1 gerilimi; iş-tipine göre bölünür (§0). |
| **git-worktrees / parallel** | K-015 worktree-izolasyon notu · K-009 | icra notu | ✅/⚠️ B1 ile aynı: paralel = kanıtlı istisna, sırf-araştırma izolasyona gerekmez. |
| **marketplace/plugin kurulumu** | V25 "kurulum YOK, yeniden yaz" | altın kural (canlı) | ✅ **Güvenlik savunması** (Snyk ToxicSkills); estetik NIH değil. |

**Özel vurgular:** (1) **ÜRETİLMİŞ kendi skill'lerimiz:** S-A karar-modeli (eval E1 6/6 vs baseline 2/6 → "değer=KONTRAT"), S-B atlas-kosum (E1 6/6, gerçek ¬T; bu rapor onun canlı koşumu). İkisinin de açık borcu: 20-sorgu description-eval + çok-model + CC saha testi. (2) V25 kapsam = dış-kurulum yasağı + iç-yeniden-yazım zorunluluğu; istisna "araştır emri listeyi ezer". (3) TDD/pytest-yeşil done birçok yerde (KILAVUZ DONE-kuralı, K-002/K-003, V39, m37-taslak-A3). (4) subagent/paralel = m.37/m.40/m.42/KILAVUZ-Kompozisyon/atlas-kosum-SKILL.

---

## §4 — Yanlış/zayıf gördüklerim (dürüst bayraklar — KARAR ALMADAN, m.41)

1. **B2 büyük ölçüde bir DOĞRULAMA egzersizi — JARVIS disiplinleri zaten kanon.** Net-yeni küçük: 2-3 madenlenebilir desen (≥3-yama→dur · çift-aşamalı spec-sonra-kalite review · dosya-brifi=zaten m.20) + kepano-uygulanabilirliği + spec-first/V1 uzlaştırması. Yeni-keşif kılığına sokmuyorum.
2. **obra spec-first ↔ V1 iterasyon>spec gerilimi gerçek ama çözülebilir** — iş-tipine göre bölünür (deterministik-kabul=spec/test-önce; keşif=iterasyon-önce), TDD çizgisiyle AYNI. Uzlaştırma köprüde yapılmalı, karar değil.
3. **Skill'ler asıl hata modlarını ÇÖZMEZ (model-düzeyi).** confirmation-bias, "düzelttim" aşırı-güveni, reward-hacking yeşil-test — bu oturumun 8-saat-stall yanlış-okuması + A5 κ≈0.51 + Materialize (80+ ajan var-olmayan bug onayı) kanıt. Kaldıraç = dış falsifikasyon-kapısı (m.9), skill-tören değil. "systematic-debugging skill'i benimse" aşırı-güveni çözüyormuş gibi görünmesin.
4. **TDD yeşil≠doğru (m.39/V23).** Her iki B-şeridi + ImpossibleBench (GPT-5 %76 hile) ortak: test tek başına halüsinasyon-kalkanı değil. V39'un pytest-yeşil evaluator'ı bu riski MİRAS ALIR (mount yanlış-yeşil vakası JARVIS log'unda zaten var). Sigorta ≠ garanti.
5. **Marketplace güvenlik AKTİF tehdit — V25'i keskinleştiriyor.** Snyk ToxicSkills (%36 zafiyetli, imzasız yayın, skill tam-yetkiyle model-görmeden koşar → prompt-injection baypas). V25 "kurulum yok" estetik NIH değil, tedarik-zinciri savunması; bu araştırma V25'in gerekçesini güçlendiriyor.
6. **Doğrulanamayan sayılar (m.39):** "174-180k yıldız" (abartılı, raporlanmadı), "%95 fix" (pazarlama), "specs matter code doesn't" (403, tweet'ten üçgenlendi, obra-ağzından değil), benimseyen-şirket listesi (Microsoft/OpenAI ikincil). [K]/[?] taşındı, laundering YOK.
7. **Öz-referans (maliyet notu):** bu 11-ajanlı raporun KENDİSİ subagent-driven-development (paralel-araştırma çeşidi) — canlı gösterim; ve JARVIS'in ZATEN sahip olduğu bir yığın için "disiplini benimse, paketi reddet" sonucuna ~11 ajan harcadı (A2/B1 çift-atlas ×2 maliyet-maruziyetinin bir örneği daha).

---

## §5 — V26 örneklem-denetimi

| Ajan/şerit | Denetlenen iddia | Sonuç | Etki |
|---|---|---|---|
| A-tez | "174-180k GitHub yıldızı" | **DOĞRULANAMADI** — GitHub API bloke, abartılı | [X]/[?]; raporlanmadı |
| C-tez | "systematic-debugging %95 first-fix" | **Pazarlama** — bağımsız doğrulanmadı | [?]; değer mekanizmadan alındı, sayıdan değil |
| E-tez | "specs matter, code doesn't" (obra) | **403** — tweet+ikincilden üçgenlendi, obra-ağzından değil | [X]; §4-6'ya taşındı |
| D-tez | "obra paralel-yazmayı yasaklar" | **Doğrulandı** — SKILL.md "Red Flags" birincil | [D]; melez-desen ayrımının çekirdeği |
| B-antitez | "ImpossibleBench GPT-5 %76 hile" | **Arama-özeti** — arXiv 2510.20270 | [K]; yeşil≠doğru argümanı çok-kaynaklı |
| E-antitez | "Snyk skill'lerin %36'sı zafiyetli" | **Kaynaklı** — Snyk ToxicSkills | [D]; V25 güvenlik-gerekçesi |
| Envanter | "S-A eval 6/6 vs baseline 2/6" | **Koşum-DOĞRULANDI** — grading dosyası | [D]; "değer=KONTRAT" bulgusu |
| Egress | fsck.com · anthropic.com · cognition.ai · jvns.ca · simonwillison.net · arXiv | **403/site-engeli** | İlgili bulgular [K]/[D-ayna]; obra SKILL.md doğrudan [D] |

---

## §6 — Cevaplanmamış sorular (karar biriktirilmedi — m.41)

1. **Hangi 2-3 somut desen KILAVUZ'a madenlenecek** (≥3-yama→dur · çift-aşamalı spec-sonra-kalite review · fix-subagent)? — V25 "yeniden yaz" akışıyla, paket kurmadan.
2. **kepano/obsidian-skills JARVIS Obsidian vault'una (V24) uygulanmalı mı** — açık-format köprüsü doğrudan aday; ama yine "kur değil, deseni yeniden-yaz" mı?
3. **obra spec-first ↔ V1 iterasyon>spec uzlaştırması iş-tipi bölmesiyle mi çözülsün** (deterministik-kabul=spec/test-önce; keşif=iterasyon)? — köprü kararı Salih'te.
4. **TDD-disiplini yalnız ölçüm-işine mi (PortRisk/V39) sınırlansın**, araştırma/kanon/wiki'ye taşınmasın mı? — yeşil≠doğru riski nasıl sigortalanır (dış falsifikasyon)?
5. **Skill'lerin çözemediği model-düzeyi aşırı-güven için dış falsifikasyon-kapısı** (m.9 ruhu) ayrı bir tasarım kalemi olmalı mı — "daha çok skill" yerine?

---

*Bu rapor B2 kartının çıktısıdır (m.41 yan-oturum): 5 aile × 2 şerit + 1 envanter = 11 Atlas koşumu, çift-atlas (tez ∧ ¬tez). Karar ALINMADI, kanon DEĞİŞMEDİ; yalnız bulgu + "nedir" açıklaması + kategori/kontrol + dürüst bayraklar sunuldu. Sıradaki kuyruk: B3 (LLM Council/Debate maliyet-fayda).*
