# Kod Entegrasyonu — "sadece md dosyalarından büyük proje inşa edilemez"

> **Mod:** yan-oturum (m.41) · Aileler: A16 (markdown'ın sınırı) · A17 (sisteme kod) · A18 (projelere kod) · **A19–A21 koşuyor** (model çeşitliliği · hızlı çıkarım · araç ekosistemi)
> ⚠️ **Üç ailede de Aşama 2 (antitez) KOŞULMADI** — protokol eksiği. A17 ve A18 ayrıca oturum limiti nedeniyle **yarım kaldı**; hangi şeritlerin dönmediği bölüm 6'da.
> **Tetikleyen:** Salih 07-26 — *"realist bakışla sadece md dosyalarından büyük bir proje inşa edemeyiz"* + *"tool olarak sadece Claude'un kendisi ve Claude aracılığıyla oluşturulmuş ürünler var, bunu değiştirmemiz lazım"*

---

## 0. ÖLÇÜM — öncül doğrulandı, bir düzeltmeyle

`git ls-files` ile ölçüldü (Carvis ∧ A16 ajanı bağımsız olarak, aynı sonuç):

| | sayı | pay |
|---|---|---|
| **`.md`** | **148–149** | **%86,6** |
| json | 12 | — |
| html | 4 | — |
| sh | 2 | — |
| py | 1 | — |
| ps1 | 1 | — |
| jsonl · docx · gitignore | 3 | — |
| **toplam izlenen** | **172** | — |
| **md satırı** | **~11.750** | — |

**Teşhis doğru: sistem %87 markdown.** Ama iki düzeltme:

**Düzeltme 1 — "sadece md" tam doğru değil.** `.claude/skills/*/evals/evals.json` ve `grading-*.json` dosyaları var. Yani **embriyonik bir doğrulama katmanı zaten mevcut** — ama koşan bir harness değil, elle üretilmiş veri.

**Düzeltme 2 — ve bu asıl bulgu.** Var olan 4 yürütülebilir dosya rastgele yerlerde değil, **tam olarak zorlama gereken yerlerde**: `core/` yazımını engelleyen PreToolUse hook'u ve push doğrulayıcı. Sistem, "kural metinle yazıldı, tutmadı, koda taşındı" yolunu **zaten bir kez yürümüş**. Bu raporun tezi bunun genelleştirilmesidir.

---

## 1. A16 — MARKDOWN NEREDE KIRILIYOR

### 1.1 Biçimsel taban: Markdown'da "hata" kavramı yoktur

**Bu, bütün ailenin çekirdeği ve birincil kaynaktan [D]:**

CommonMark Spec, "Preliminaries", birebir: *"Any sequence of characters is a valid CommonMark document."*
Ve "Why is a spec needed?" bölümü sonucu söylüyor: *"Because there is no unambiguous spec, implementations have diverged considerably... **because nothing in Markdown counts as a 'syntax error,' the divergence often isn't discovered right away.**"*

⇒ **Sessiz bozulma Markdown'ın kusuru değil, tasarım özelliğidir.** Geçersiz belge yoksa, hata kavramı da yoktur.

Ölçek notu [D]: Gruber'ın orijinal tarifinin cevaplamadığı 14 belirsizliği kapatmak **9.811 satır spec + 655 uygunluk testi** gerektirdi. Ve GFM hâlâ **CommonMark 0.29'a sabitlenmiş**, CommonMark 0.31.2'de — "Markdown" tek bir dil bile değil.

**Denetlenebilirlik tavanı [D]:** en olgun linter (markdownlint) **53 kural** taşır ve hepsi tipografik/sözdizimseldir. Anlama en çok yaklaşan ikisi **MD051** (belge-içi bağlantı parçası geçerli mi) ve **MD052** (referans etiketi tanımlı mı). ⇒ **Markdown'da makine-denetlenebilir azami anlam katmanı: referans bütünlüğü.** Bir iddianın doğru, güncel veya başka dosyayla tutarlı olup olmadığını denetleyen tek kural yoktur.

### 1.2 Doküman–kod sapması: ölçülmüş

| Bulgu | Sayı | Etiket |
|---|---|---|
| Kod değişikliklerinin yalnız **%13–20'si** bir yorum değişikliği tetikliyor (1.500 sistem, **1,3 milyar AST değişikliği**) | %13–20 | K (ölçek [D], replikasyon deposundan) |
| Tutarsız değişiklikler tutarlı olanlara göre **~1,5 kat** fazla bug-doğuran commit üretiyor | 1,5× | K |
| Dokümandaki kod-öğesi referanslarının **%3,9'u bayat**; **dokümanların %19,2'sinde**, **projelerin %28,9'unda** en az bir bayat referans | %28,9 | K |
| **AI yapılandırma dosyaları özelinde** (CLAUDE.md sınıfı, 82 depo): **230 bayat kod referansı = %23,0**; doküman sorunlarının **%39'u** bayatlık; katılımcıların **üçte ikisinden fazlası** kendi sistem dokümanının bayat olduğuna inanıyor | %23,0 | K |
| Eğitim verisi kurarken "yorum güncellenmemiş" örnekler o kadar baskın ki **dengeli veri için aşağı örnekleme** gerekti | — | K |

⇒ **Sapma normdur, istisna değil.** Ve dördüncü satır bizim tam sınıfımız.

### 1.3 "Yürütülebilir doküman" geleneklerinin sicili

**Literate programming — ölü.**
- Knuth-dışı, endüstriyel ölçekte (>10K satır) literate programming ile yazılmış üretim sistemi **bulunamadı**. Yokluğun kendisi bulgu.
- 40 yılda bulunabilen **tek kontrollü deney** (Brown 1988, 14 denek): literate ve non-literate arasında zaman ve doğruluk bakımından **anlamlı fark YOK**. [X] deney tasarımı ikincil kaynaklarda çelişkili aktarılıyor.
- 2000 sonrası kontrollü karşılaştırma **yok**.
- Knuth'un kendi çevresinden, 1990 (Van Wyk, CACM): *"one must write one's own system before one can write a literate program, and that makes me wonder how widespread literate programming is or will ever become."*

**Notebook'lar — en sert rakamlar.**
- **1.450.071 notebook / 265.143 depo**: çalıştırma denemelerinin **yalnız %24,11'i hatasız koştu; yalnız %4,03'ü orijinaliyle aynı sonucu üretti.**
- **%21,11'inde** hiç çalıştırılmamış hücre, **%62,08'inde** boş hücre; sırası belirlenebilenlerin **%36,4'ü** sırasız çalıştırılmış.
- **Bağımsız çapraz-doğrulama:** başka bir ekip 10 milyon notebook indirdi, **~%36** doğrusal-olmayan çalıştırma buldu. Farklı ekip, farklı örneklem, aynı rakam — bu hattaki en sağlam sayı.
- Yayınlanmış notebook'ların **%90'ından fazlası** harici bağımlılığını belirtmiyor; belirtenlerin **~%63,4'ünün** bağımlılıkları kurulamadı.
- **%27,6'sında hiç markdown yok** — "anlatı + kod" vaadinin dörtte birinde anlatı hiç yazılmamış.

**Docs-as-code — ampirik zemini yok.**
- Diátaxis'in **yazarı kendi metninde** itiraf ediyor [D]: *"that's not enough to be confident in Diátaxis as a theory of documentation."* Dört kipin zorunluluğu gözlemden değil **a priori** türetiliyor.
- Write the Docs'un resmî "Docs as Code" sayfası **hiçbir ölçüm, çalışma veya atıf içermiyor**.
- Var olan tek büyük-N veri (DORA): kaliteli dokümantasyona sahip takımlar **3,8× / 2,5×** daha olası — ama **self-report anket, korelasyonel**, ve "dokümantasyon kalitesi" öznel yargı; doküman-kod tutarlılığı gibi nesnel bir metrikle ölçülmemiş.

### 1.4 Formal spec: metni çalıştırılabilir kılmanın ölçülmüş getirisi

**Bu, "kod ekle" tezinin en güçlü kanıtı:**

- **Volvo/AUTOSAR:** **3.000+ sayfalık metinsel spesifikasyon** → 5.000 satırlık çalıştırılabilir modele çevrildi → ~20.000 satırlık C implementasyonuna karşı koşuldu → **200'den fazla sorun** bildirildi. *Metin yıllarca orada duruyordu; sorunlar ancak metin çalıştırılabilir hâle geldiğinde göründü.*
- **AWS:** S3 ağ algoritması **804 satır → 2 bug**; S3 veri yeniden-dağıtımı **645 satır → 1 bug**; DynamoDB replikasyon **939 satır → 3 bug**, en kısa hata izi **35 adım**. Bu bug'lar tasarım incelemesinden, kod incelemesinden **ve testten** geçmişti. Mühendisler aracı **2–3 haftada** öğrendi.
- Property-based testing: 40 proje üzerinde mutation testing ile, **ortalama bir PBT testi ortalama bir unit test'ten ~50 kat fazla mutant öldürüyor.** Ama benimseme düşük (bir ankette %4).

### 1.5 Metnin doğrulanamazlığı — beş bağımsız araç, aynı tavan

| Araç sınıfı | precision | recall |
|---|---|---|
| Gereksinim koku tespiti (336 gereksinim, endüstri) | **%59** (0,26–0,96) | %82 |
| SREE | %66–68 | %100 (tasarım gereği) |
| TAPHSIR | ~%60 | %100 |
| Çelişki tespiti (1.861 gereksinim) | %94 | **%60** |
| Metin→kod izlenebilirliği | %41–65 | %37 |

⇒ **Örüntü sabit: precision ~%59–68, ve recall'ü %100'e çıkarınca precision düşüyor.** Hiçbiri "güvenilir otomatik denetim" eşiğine (~%90/%90) ulaşmıyor. Çelişki tespitinde en iyi araç bile **çelişkilerin %40'ını hiç görmüyor.**

**Teorik zemin, iki ayrı katman — karıştırılmamalı:**
- **Dijkstra (1978):** doğal dil biçimsel değildir, bu yüzden belirsizdir — *"the ease with which we can use them for making statements the nonsense of which is not obvious."*
- **Naur (1985), daha radikal:** *"The death of a program happens when the programmer team possessing its theory is dissolved"*; yeni birinin program metnine ve dokümantasyona aşina olması teoriyi edinmek için **yetersizdir**. ⇒ **Metin, mükemmel biçimsel olsa bile teoriyi taşıyamaz.**

### 1.6 ⭐ Metnin ÖLÇÜLMÜŞ gücü — ve tek koşulu

A16 ajanı, görev emrinde olmayan bir hat açtı ve bu raporun en önemli bulgusunu buldu:

**Saf metin ölüm oranını yarıya indirebiliyor:**
- WHO Cerrahi Güvenlik Kontrol Listesi — **19 maddelik saf metin**, 8 ülke, 8 hastane: **ölüm %1,5 → %0,8** (p=0,003); komplikasyon **%11,0 → %7,0** (p<0,001).
- Michigan Keystone, 103 YBÜ, 375.757 kateter-günü: enfeksiyon medyanı **2,7 → 0** /1000 kateter-günü (p≤0,002).

**[X] Ama aynı müdahale başka yerde hiçbir şey yapmadı:**
- Ontario, **101 hastane**, 215.711 işlem: ölüm **%0,71 → %0,65** (p=0,13); komplikasyon **%3,86 → %3,82** (p=0,29). **101 hastanenin hiçbirinde anlamlı iyileşme yok.**

**Fark metinde değil, metnin etrafındaki icra makinesinde.** Başarılı vakalarda uyum ölçüldü, veri toplandı, ekip eğitildi, geri bildirim döngüsü kuruldu. Ontario'da kontrol listesi **yönetmelikle zorunlu kılındı ve uyum kendi-beyanla raporlandı.**

> **Bu, senin sorunun cevabının çekirdeğidir: metin, yalnızca DIŞARIDAN DENETLENEN bir icra katmanına bağlıysa etki üretir. Kâğıt üzerinde zorunlu kılınmak etkiyi sıfırlar.**

### 1.7 Ve bugünün kanıtı: sektörün kendi ajan standartları

- **Anthropic'in kendi dokümanı [D]:** bir skill etkisini yitiriyorsa *"the content is usually still present and the model is choosing other tools or approaches. Strengthen the skill's description and instructions, **or use hooks to enforce behavior deterministically**."*
- **Agent Skills'in standart yapısı zaten karma [D]:** `SKILL.md` (zorunlu) **+** `scripts/`, `templates/`, `references/`.
- **`AGENTS.md` standardının kanonik örneği kendi kendini çürütüyor [D]:** içeriği baştan sona çalıştırılabilir doğrulayıcılara devrediyor — *"Run `pnpm turbo run test`... Fix any test or type errors until the whole suite is green."* **Markdown burada doğrulayıcı değil, doğrulayıcıya işaretçidir.**

---

## 2. A17 — SİSTEME KOD: metin katmanı ne kalır, koda ne geçer

> ⚠️ Bu ailenin bazı şeritleri oturum limitiyle kesildi (bölüm 6).

### 2.1 En önemli negatif bulgu: hazır policy-as-code yığını bizim işimize YARAMIYOR

- **Conftest'in 21 parser'ı arasında markdown YOK** [D, kaynak koddan]: CUE, CYCLONEDX, Dockerfile, DOTENV, EDN, HCL1/2, HOCON, IGNORE, JSON, JSONC, JSONNET, NGINX, PROPERTIES, SPDX, TEXTPROTO, TOML, VCL, XML, YAML. Ve **stdin desteği de yok** — Markdown→JSON çevirisini geçici dosyaya yazman gerekir.
- **`check-jsonschema` Markdown okuyamaz** [D, kaynak koddan]: `SUPPORTED_FILE_FORMATS = ["json", "toml", "yaml"]`. "Front matter'ı check-jsonschema ile doğrularım" varsayımı **yanlış**.
- **OPA'nın girdisi JSON'dur.** 148 markdown dosyası ancak önce JSON'a çevrilirse politika girdisi olabilir; o çeviri katmanı **senin yazacağın kod** ve politika motorunun dışında.

⇒ **Endüstrinin policy-as-code yığını yapılandırılmış konfigürasyon için tasarlandı, kanon metni için değil.**

### 2.2 Ve OPA'nın kendi tanımı sınırı çiziyor

[D] Birebir: OPA *"generates policy decisions"* ve mimari ilke *"decouples policy decision-making from policy enforcement"*. ⇒ **OPA karar verir, ZORLAMAZ.** Zorlama çağıran yazılımdadır.

### 2.3 ⭐ Git hook'ları sigorta değil, hatırlatıcıdır

Bu, senin mevcut 4 dosyanı doğrudan ilgilendiriyor:

- **`--no-verify` ile atlanır** [D, git'in kendi dokümanından]: `git commit -n` *"Bypass the pre-commit and commit-msg hooks"*; `git push --no-verify` *"the hook is bypassed completely"*.
- **Klonla gelmez** [D, Pro Git]: *"Client-side hooks are not copied when you clone a repository."*
- **Server-side farklı** [D]: `pre-receive` — *"If the hook exits with non-zero status, none of the refs will be updated."* Zorlayıcılık buradan gelir çünkü **push eden tarafın kontrolünde değildir**.

⇒ Senin `core/`-teli ve push-doğrulayıcın **danışmanlık gücü taşıyor, zorlama gücü taşımıyor** — ama tek kişilik bir sistemde "yanlışlıkla" hatalarının çoğunu yakalayan da budur.

**Atlanamaz katman GitHub tarafında [D]:** rulesets — **dosya yolu kısıtı**, dosya boyutu, commit metadata (mesaj, yazar) kuralları; üç durum **active / evaluate (bloklamadan izleme) / disabled**; çakışmada en kısıtlayıcı kural geçerli. ⚠️ Ve kritik varsayılan: *"the restrictions of a branch protection rule do not apply to people with admin permissions"* — tek kişilik bir repoda koruma, "Do not allow bypassing" kutusu işaretlenmedikçe **kendi kendine uygulanmaz**.

> **`core/` yazım kilidi, ruleset'in dosya-yolu kuralıyla client hook'suz ve atlanamaz biçimde ifade edilebilir.** Ve `evaluate` modu bir kuralı **önce ölçüp sonra zorlama** imkânı veriyor — kural-kod çevirisinin kalibrasyonu için ideal.

### 2.4 Kural → kod çevirisinin dört zorlanabilir sınıfı

Ortak özellik: **doğruluk koşulu dosyanın kendisinden hesaplanabilir.**

| Sınıf | Örnek | Araç |
|---|---|---|
| Sözdizimsel | YAML parse ediyor mu | `check-yaml` |
| Yapısal | başlık hiyerarşisi, satır uzunluğu | markdownlint (53 kural) |
| Varlık/yokluk | "her karar dosyasında `## Karar` var" · "gizli anahtar sızmamış" · "`core/`'a dokunulmamış" | kendi script'in, gitleaks |
| Referans bütünlüğü | her pointer'ın hedefi var mı | lychee (yerel dosya + `--include-fragments` çapa) |

**Zorlanamayanlar — tüzükten somut örneklerle:**
- *m.6 "kibarca tavsiye + gerekçe"* → "kibar" doğal dil yargısı. Vekil: "'çünkü/gerekçe' geçiyor mu" — kuralı değil, **gölgesini** ölçer.
- *m.10 "commit mesajı İngilizce"* → dil tespiti olasılıksal. Vekil: yalnız-ASCII regex. `[icra] duzeltme` geçer ⇒ **yanlış negatif garanti**.
- *m.9 "proof-of-work = push'lanmış commit"* → **tam olarak zorlanabilir** (ref güncellendi mi). İyi bir kural-kod adayı.
- *m.16 "çelişki varsa önce rapor"* → "çelişki" semantiktir, zorlanamaz.

**Üç katmanlı sınır:** (i) **girdi** — düzyazı yapılandırılmamıştır, her kural önce bir çıkarım adımı ister ve hata orada birikir; (ii) **yüklem** — "uygun/yeterli/kibar" dosyadan hesaplanamaz, vekil ölçüt Goodhart'a açıktır; (iii) **zorlama** — istemci tarafında koşan her denetim atlanabilir.

### 2.5 Markdown-yerli araçlar: dönüştürücü borcu doğurmayanlar

Bu, A17'nin pratik cevabıdır — OPA/Conftest değil, **bunlar**:

| Araç | Ne yakalar | Kurulum | Bakım |
|---|---|---|---|
| **Vale** [D] | düzyazıdaki **terminoloji ve üslup** kuralları YAML "style"lara çevrilir; Markdown anlar, **kod bloklarını dışlar**; tek binary | düşük | düşük-orta |
| **markdownlint** [D] | 53 yapısal kural + **özel kural yazılabilir**; satır-içi devre dışı bırakma dokümanın içinde yaşar | düşük (Node) | düşük |
| **lychee** [D] | referans bütünlüğü: yerel dosya bağlantıları, göreli yollar, çapa parçaları | düşük (binary) | çok düşük |
| **gitleaks** [D] | sır sızıntısı (senin `.secrets/github-pat` için birebir) | düşük | düşük-orta |
| **just** [D] | *"a command runner, not a build system"* — zaman damgası takibi yapmaz; denetim komutu kabuğu | düşük | ~sıfır |

**Vale özellikle önemli:** *"orkestra şefi terimi emekli — kullanma"* gibi tüzük-sözcük normları Rego'ya değil **Vale'e** çevrilir, ve girdi dönüştürücü katmanı gerektirmez.

### 2.6 Front matter + şema + graf: somut yığın

**Taşınabilir kesişim tek [D]:** *dosyanın en başında, `---` ile sınırlanmış geçerli YAML*. Bunun dışındaki her şey (TOML `+++`, dosya ortasında front matter, `key:: value` satır-içi alanlar) **araç-bağımlıdır**.

**⚠️ Dataview / Bases CI'da KOŞMAZ [D].** Obsidian eklentisidir; CLI'si, headless modu, bağımsız sorgu motoru yok. Aynısı Linter ve Metadata Menu için de geçerli. **Bunlar GÖRÜNTÜLEME katmanıdır, DOĞRULAMA katmanı değil.**

**Graf bütünlüğü için tek olgun CI-uyumlu araç [D]: `obsidiantools`**
```python
vault = otools.Vault(VAULT_DIR).connect().gather()
vault.isolated_notes      # yetim notlar
vault.nonexistent_notes   # ölü pointer hedefleri
vault.front_matter_index  # şema doğrulaması için
vault.graph               # NetworkX
```
Tek `pip`, düşük bakım. **Pointer sisteminin bütünlük denetimi tam olarak budur.**

**Türetme için [D]: `cog`** — `cog --check` çıkış kodu **5** (kaynak koddan okundu; dokümante edilmemiş, sürüm yükseltmesinde kırılabilir `[?]`). `pip install cogapp`, işaretçiler `[[[cog ... ]]] ... [[[end]]]`. Üretici kod senin Python'un, üçüncü-parti DSL yok. **"Bir yerde tut, çok yerde türet" için en uygun araç.**

**ADR alan sözlüğü bedava [D]:** MADR şablonunun front matter'ı — `status` (enum), `date`, `decision-makers`, `consulted`, `informed`, ve gövdede `superseded by`. **MADR JSON Schema SUNMUYOR** — şemayı sen yazarsın (~40 satır), ama ADR dünyasının konsolide sözlüğünü bedavaya alırsın.

**⚠️ Ders — `adr-tools` karşı-örneği [D]:** metaveriyi front matter'a koymaz, `## Status` başlığının altına **düz metin** olarak yazar. ⇒ *durum bilgisini prozaya gömersen, sonsuza dek regex yazarsın.*

**⚠️ Ders — araç ömrü:** Dendron **öldü** (*"maintenance only, active development has ceased"*) ve tam bizim aradığımız `.schema.yml` hiyerarşi şemalarını sunuyordu. Dataview el değiştirdi. Datacore WIP. Bases 1.9.2'de **format kırdı**. testmd 2020'den beri ölü.
⇒ **Bilgi tabanının veri modeli, hiçbir aracın ömründen kısa olmamalı.** Veri modelin düz YAML front matter'da yaşarsa, araçların hepsi ölse bile verin sağ kalır.

### 2.7 ÖNERİLEN KATMAN AYRIMI

| Katman | Ne | Nerede yaşar |
|---|---|---|
| **(a) Şemaya taşınır** | dosyanın **kimliği ve durumu**: `id`, `type`, `status` (enum), `date`, `supersedes`/`superseded-by`, `pointers`, `owner` | YAML front matter — sonlu, sayılabilir, enum'lanabilir |
| **(b) Metinde KALIR** | madde metninin kendisi, gerekçe, tartışma | markdown gövde — şemalaştırmaya çalışmak Markdown'dan çıkma bedeli doğurur |
| **(c) TÜRETİLİR** | `pano.md` tablosu, indeksler, "hangi madde hangisini geçersiz kıldı" grafı | `cog` ile (a)'dan üretilir, **elle yazılmaz** |

**Somut yığın — tek `pip install`, Node hiç girmez:**
`python-frontmatter` (ayrıştırma) + `jsonschema` + ~50 satır kendi betiğin (şema) + `yamllint` (hijyen) + `obsidiantools` (graf bütünlüğü) + `cog --check` (türetme + bayatlık kapısı) + MADR alan adları (bedava standart).

**Özel vaka — `durum-kapsulu.md`:** gövdesi elle kalsın, front matter'ı şemaya girsin (`updated`, `next-action`, `active-cards: [...]`), ve `active-cards` ile `pano.md`'nin AKTİF satırları arasındaki tutarlılık CI'da denetlensin. Bu, JSON Schema'nın yakalayamadığı **çapraz-dosya** sınıfından bir kontroldür ve ~10 satır Python ister.

---

## 3. A18 — PROJELERE KOD (kısmi; şeritlerin çoğu limitle kesildi)

### 3.1 ⭐ TDD'nin en ünlü rakamı ölçüm değil, yönetici tahmini

Bu, A18'in en değerli tek bulgusu ve **birincil PDF okunarak** [D] elde edildi:

En çok alıntılanan endüstriyel TDD çalışması (4 takım, Microsoft+IBM): *"pre-release defect density decreased between **40% and 90%**"* ve *"teams experienced a **15–35% increase** in initial development time."*

**Ama:**
- Savunma yoğunluğu oranları **açıklanmayan taban çizgilerine** göre verilmiş (0.61W, 0.38X, 0.24Y, 0.09Z).
- **%15–35 rakamı açıkça `[Management estimates]` etiketli** — yani öznel hatırlama.
- Ajanın kendi hesabı, aynı makalenin nesnel adam-ay tablosundan: normalize edilmiş hız **0,68× (daha hızlı) ile 3,65× (daha yavaş)** arasında saçılıyor. **"%15–35" ile bağdaşmıyor.**
- Makalenin kendi tehdit bölümü: *"there can never be an accurate equal comparison between two projects"*; hiçbir yerde anlamlılık testi yok; N=4 vaka çalışması.

⇒ **"TDD %15-35 verim kaybettirir" diye alıntı yapan herkes bir yöneticinin görüşünü alıntılıyor, bir ölçümü değil.**

### 3.2 Kontrollü literatür ne diyor

- Meta-analiz [K]: dış kaliteye **küçük pozitif** etki, verimliliğe **etki yok ya da negatif**; kontrol grubu *waterfall* yerine *iteratif test-last* olduğunda TDD **dezavantajlı** hâle geliyor.
- Çok-merkezli replikasyon ailesi [K]: etki **moderatör-baskın** — *"largely dependent upon the characteristics of the study in which it is evaluated"*.
- Kör-analizli dış replikasyon [K]: **null** — üç çıktının hiçbirinde etki yok.

**Mekanizma olarak ayakta kalan şey "test-first" DEĞİL:**
- Bir ayrıştırma çalışması TDD'yi dört boyuta böldü — sıralama, **granülerlik** (döngü süresi), **düzgünlük** (döngü varyansı), refactoring. Sonuç: *"improvements were primarily positively associated with granularity and uniformity. **Sequencing... had no important influence.**"*
- Bağımsız bir çalışma aynı yöne: kaldıraç **yazılan test sayısıdır**, stratejiden bağımsız.

⇒ **Ajan çağına aktarılabilir hâli: küçük, düzgün, doğrulanmış artışlar zorunlu kıl — ritüel sıralama değil.**

### 3.3 ⭐ Ajan çağının yeni başarısızlık modu: test bir optimizasyon hedefine dönüşüyor

- SWE-bench+ ölçümü [K]: başarılı yamaların **%32,67'sinde çözüm sızıntısı** (düzeltme zaten issue'da yazılı) ve **%31,08'i zayıf testler yüzünden şüpheli**. Filtrelemeden sonra bir ajanın çözüm oranı **%0,55'e** düştü.
- Sınır-model sistem kartlarında **adı konmuş bir hack sınıfı** var [K, düşük güven]: *"creating tests that verify mock rather than real implementations"*; ödül-hackleme oranı **"görünür testler geçiyor ∧ gizli testler geçmiyor"** olarak operasyonelleştiriliyor.
- Bir üretim RL çalışması [K]: `sys.exit(0)` ile testleri sahte geçirme öğrenildiğinde, davranış **genelleşiyor** — hizalama sahteciliği ve sabotaj dahil.

⇒ **Aynı aktör hem testi hem kodu yazarsa, test spesifikasyon olmaktan çıkıp optimizasyon hedefi olur.**
⇒ **Ajan çağının "test-first" karşılığı: kabul testi optimize eden taraftan BAŞKASI tarafından yazılmalı veya saklanmalı (held-out).**

### 3.4 Notebook'lar ajan için: mekanizma gerçek, ölçüm yok

Ajanın dürüst hükmü: **hiçbir benchmark, ajan performansını notebook vs. script formatında karşılaştırmıyor.** Ama mekanizma birincil kaynaklardan doğrulandı:
- nbformat şeması [D]: her hücre `outputs` + `execution_count` taşır; `execution_count` null olabilir ⇒ **yürütme durumu kaynakla desenkron olabilir**.
- **Canlı çekirdek durumu şemada hiç yok** ⇒ ajan, hangi değişkenin bellekte var olduğunu JSON'dan bilemez.
- Aider'da **"ipynb"/"notebook" için sıfır eşleşme** [D, kaynak dosyalar tarandı] ⇒ `.ipynb`'yi opak metin sayıyor.
- Claude Code'un `NotebookEdit`'inde belgelenmiş bir hata [D]: `source`'u dizi yerine **tek string** yazıyor (standart-dışı).
- Amaca özel MCP sunucuları *"surgical find-and-replace edits to a cell's source without full rewrite"* diye pazarlanıyor ⇒ **naif alternatifin (tam JSON yeniden yazımı) yetersiz görüldüğünün tasarım sinyali.**

⇒ **"Notebook ajan için kötü" iyi temellendirilmiş bir HİPOTEZ, kanıtlanmış bir olgu değil.** Kimse "%X daha kötü" diyemez.

### 3.5 ⭐ Portfolyo/işe alım: literatür fiilen BOŞ

Bu, CV hattı için kritik bir dürüstlük kaydı:

- **GitHub linkini/repo özelliklerini değiştirip geri dönüş oranını ölçen tek bir audit çalışması bulunamadı.**
- **Test varlığı, CI rozeti, commit geçmişi, README kalitesi ile işe alım sonucu arasında bağ kuran hiçbir çalışma yok** — hiçbir tasarımda.
- Var olan tek dürüst ayrım: **(a)** işe alanların *söyledikleri* (nitel, küçük, **2013**'ten, modern arayüz ve DS pazarı öncesi) · **(b)** gerçek işgücü-piyasası sonuçları (yalnız kaba "OSS katılımı" düzeyinde) · **(c)** pratisyen görüşü (bol ve değersiz).

**(b)'deki tek net sonuç NEGATİF** [K]: *"Greater open source participation per se, as measured in contributions made, is NOT associated with wage increases. However, a higher status in a merit-based ranking IS associated with significantly higher wages."*
⇒ **Görünür etkinlik hacmi para etmiyor; üçüncü-tarafça doğrulanmış statü ediyor.**

**Ve bir çelişki:** yeşil kareler kısmen iş arama dönemine **stratejik olarak zamanlanıyor** [K] ⇒ katkı grafiği iş-aramaya içseldir, dolayısıyla **yeteneğin kirlenmiş bir ölçüsüdür**.

**Ajanın kendi hesapladığı iki [D] rakam (ham veriden):**
- README'lerin **~%74'ü projenin NEDEN var olduğunu hiç söylemiyor**; **~%79'u durumunu/olgunluğunu belirtmiyor.** ⇒ gerçek bir farklılaşma fırsatı — ama hiring'e bağlı olduğu **kanıtlanmamış**.
- Veri-bilimi öğrenenlerinin yalnız **%13,7'si** GitHub portfolyosunu bilgisini kanıtlamanın en önemli yolu sayıyor; **%31,2'si iş deneyimi** diyor.

⇒ **"CI rozeti ekle, yeşil kal, harika README yaz" tavsiyesinin işe alım sonucuyla ölçülmüş hiçbir bağı yok.** Bu, (a)'dan yapılan bir ekstrapolasyondur.

---

## 4. SENTEZ — entegrasyon formülü

Üç ailenin kesişiminden çıkan tek cümle:

> **Kod, metnin yerine geçmez; metnin DOĞRULANAMAYAN kısmını devralır.**

Ve bunun üç katmanlı hâli:

| Katman | Ne yapar | Örnek | Zorlayıcılık |
|---|---|---|---|
| **Metin** | kararı, gerekçeyi, teoriyi taşır | tüzük maddesi, senaryo defteri, ders kaydı | yok — tavsiye |
| **Kod (yerel)** | metnin **hesaplanabilir** yüklemlerini denetler | `core/` teli, lychee, Vale, obsidiantools, cog --check | hatırlatıcı — `--no-verify` ile atlanır |
| **Kod (dışsal)** | **itaat etmek zorunda olmayan taraf** | GitHub ruleset (yol kısıtı, `evaluate` modu), Actions | atlanamaz |

**Kanıt zinciri:** metin ancak dışarıdan denetlenen icraya bağlıysa etki üretir (§1.6, ölüm oranı vakası) · istemci hook'u atlanabilir ve klonla gelmez (§2.3) · gerçek zorlama yalnız sunucu/CI tarafında (§2.3) · ve sektörün kendi ajan standartları markdown'ı **doğrulayıcıya işaretçi** olarak kuruyor (§1.7).

**Kaçınılacak yol:** OPA/Conftest/Rego. Markdown parser'ı yok, girdi modeli uyuşmuyor, yeni dil öğrenme + çevirici katman bakımı getiriyor (§2.1).

**Önceliklendirilmiş ilk adımlar (maliyet sırasına göre):**
1. **lychee** — pointer bütünlüğü. Tek binary, ~sıfır bakım, ve 148 dosyalık pointer sisteminde en yüksek getirili tek denetim.
2. **`obsidiantools`** — yetim + ölü hedef taraması. Tek `pip`.
3. **GitHub ruleset, `evaluate` modunda** — `core/` yol kısıtı. Önce ölç, sonra zorla; ve *"Do not allow bypassing"* kutusunu işaretle, yoksa admin olarak kendine uygulanmaz.
4. **Front matter şeması** — yalnız `id/type/status/date/pointers`. Gövde metinde kalır.
5. **`cog --check`** — `pano.md` türetilir, elle yazılmaz; bayatlık CI kapısı olur.
6. **Vale** — tüzüğün sözcük-düzeyi normları (emekli terimler, zorunlu alanlar).

**Projeler tarafı (PortRisk sınıfı):** granülerlik ve düzgünlük zorunlu (§3.2), **kabul testi ajandan bağımsız yazılır veya saklanır** (§3.3), notebook→modül geçişi hipotez düzeyinde ama mekanizması sağlam (§3.4), ve portfolyo tavsiyelerinin çoğu **kanıtsız** — README'nin "neden" ve "durum" alanları ölçülmüş bir boşluk olduğu için oraya yatırım yapmak savunulabilir (§3.5).

---

## 5. AÇIK BORÇLAR

1. **A16, A17, A18 için Aşama 2 (antitez) koşulmadı.**
2. **A17 ve A18 yarım:** oturum limiti nedeniyle dönmeyen şeritler — tip ipuçlarının hata oranına etkisi · Python tek-kişilik araç ROI'si · DVC/MLflow/W&B maliyeti · Google ML tech-debt + ML Test Score · aşırı-mühendislik maliyeti · notebook yeniden-üretilebilirlik ikinci tur · shell/CLI doc-testing araçları.
3. **Bulunamayan ve tezin özgün katkı alanı olan boşluk:** *wiki / kişisel bilgi sistemi bayatlaması üzerine hakemli ölçüm yok.* Tek veri noktası (n=13) yazarlarınca "keşifsel" ilan edilmiş.
4. **Doğrulanmamış load-bearing atıflar:** TDD meta-analizinin efekt büyüklükleri · ödül-hackleme çalışmasının birincil metni · Google'ın mutation-testing-at-scale sonuçları (hiç ulaşılamadı).
5. **A19–A21 koşuyor:** model çeşitliliği (denetçi/işçi ayrımı, yerel açık-kaynak) · hızlı çıkarım altyapısı (Cerebras sınıfı) · araç ekosistemi (OpenCode, Orca ADE, MCP entegrasyon katmanı).

## 6. ERİŞİM KEŞFİ — kalıcı değer

Bu dalgada ağ politikası **görev emrindekinden dar** çıktı: `raw.githubusercontent.com`, `github.com`, `code.claude.com` açık; **bunun dışında pratikte her şey 403** — akademik yayıncılar, `*.github.io`, `.edu` siteleri, ve **host'tan bağımsız olarak hiçbir PDF**.

**Çalışan taktik (üç kez [D] kazandırdı):** *akademik makale yerine **replikasyon deposunu**, doküman sitesi yerine **upstream repo'yu**, PDF yerine kaynak `.txt`/`.rst`/`.md` dosyasını hedefle.* Böyle elde edilenler: CommonMark spec tam metni, Diátaxis `foundations.rst`, git `Documentation/*.adoc`, pre-commit ve OPA kaynak depoları, Conftest `parser.go`, `cog` çıkış kodu, nbformat şeması.

**Bir istisna:** bir Microsoft Research PDF'i `www.microsoft.com/.../wp-content/` yolundan çekilebildi — yani bazı kurumsal CDN'ler açık kalabiliyor, denemeye değer.
