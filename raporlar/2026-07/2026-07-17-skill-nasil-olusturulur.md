# Skill Nasıl Oluşturulur — Metodoloji Raporu (TARTIŞMA; Fable ile)

> **Mod:** rapor · KARAR YOK. **COMMIT: Salih 07-18 izin verdi** (branch'e, PC'den bulunabilirlik); **merge→main/canon = Fable Cowork süzgeci** (m.41). Amaç: üreteceğimiz skill KOMBİNASYONLARINA (ör. `karar-hatti`) ders. Kaynak: claude-code-guide (Claude Code otoriter mekaniği) + Atlas skill-desenleri (§8 skill-fikri-kutusu raporu) + Atlas skill-metodolojisi (§9, DONE).

---

## 1. Skill anatomisi + üretim adımları (claude-code-guide, OTORİTER)
- **Klasör:** `.claude/skills/<name>/SKILL.md` (proje, git'e commit) · `~/.claude/skills/` (kişisel) · plugin. **Öncelik:** Managed > Kişisel > Proje > Plugin > Bundled.
- **SKILL.md** = YAML frontmatter + markdown gövde + ops. `scripts/` `references/` `assets/`.
- **Frontmatter alanları (otoriter):**

| Alan | Zorunlu | Ne | Sınır |
|---|---|---|---|
| `name` | hayır | listede görünen ad = komut adı | klasör adıyla eş |
| `description` | **önerilen** | NEDEN + NE ZAMAN (auto-tetik için) | `when_to_use` ile birlikte **≤1536 char** |
| `when_to_use` | hayır | ek tetik bağlamı (description'a eklenir) | 1536 kapağa dahil |
| `argument-hint` | hayır | autocomplete ipucu | `[issue] [format]` |
| `arguments` | hayır | isimli pozisyonel args (`$name`) | boşluk-ayrık / YAML liste |
| `disable-model-invocation` | hayır | `true` = Claude auto-tetikleyemez (yalnız kullanıcı) | default false |
| `user-invocable` | hayır | `false` = `/` menüsünden gizli (yalnız Claude/arka-plan) | default true |
| `allowed-tools`/`disallowed-tools` | hayır | o TUR için tool ön-onay/çıkar (sonraki mesajda temizlenir) | `Bash(git add *) Read` |
| `model` / `effort` | hayır | skill için model/efor override | sonnet/opus/haiku/fable · low..max |
| `context: fork` | hayır | izole subagent bağlamında koş | gövde = subagent prompt'u |
| `agent` | hayır | fork'ta subagent tipi | Explore/Plan/custom |
| `hooks` · `paths` · `shell` | hayır | skill-scoped hook · glob-koşullu yükleme · shell | `paths: *.ts` |

- **Validasyon:** invalid YAML → skill yine `/name` ile yüklenir ama description-match olmaz. name = klasör adı.

## 2. Description/tetik ZANAATI (tetiklemenin #1 belirleyicisi)
- `description` = **NE yapar + NE ZAMAN** (ana kullanım önce). Hafif "iddialı" yaz (undertrigger'a karşı) AMA sınırı net çiz (negatif tetik: "X ise KULLANMA"). Bizim `dev-run-planner`/`hizalama` bu deseni zaten kullanıyor.
- Yanlış-tetik = description ya dar (tetiklemesi gerekeni kaçırır) ya geniş (yanlış tetikler) → §6 eval ile ölç.

## 3. Gövde + progressive disclosure (= m.20/m.22 birebir)
- 3 kat: **name+desc (~100 tok, hep yüklü)** → **gövde (<5k tok, tetiklenince)** → **referans dosyalar (talep-üzerine)**. Bu, JARVIS'in pointer (m.20) + katmanlı-yerleşim (m.22) ilkesinin AYNISI — JARVIS önden.
- Gövde: emir-kipli adımlar; şablon/arka-plan/veri → ayrı referans dosyaya.

## 4. Script vs LLM + YAN-ETKİ GÜVENLİĞİ (★ "commit atma" hattının koda dökümü)
- **Deterministik** adımlar (kayıt, commit, validasyon) → **script**; **muhakeme/üretim** (3 model, karşıt-fikir) → **LLM talimatı**. İlke: "belirsizliği kaldır."
- **Yan-etkili skill** (commit/deploy/kayıt) → **`disable-model-invocation: true`** → yalnız `/name` ile ELLE; Claude auto-tetikleyemez. + `allowed-tools` o tur için git komutlarını ön-onaylar.
- **Sonuç:** otonom pipeline kanona KAZARA yazamaz = **m.31 Katman-1 freni + m.9 proof-of-work koda gömülü.** (Senin "commit atma" endişenin yapısal karşılığı.)

## 5. KOMPOZİSYON (Salih'in asıl hedefi — `karar-hatti` dersi)
**★ KRİTİK:** skill'ler birbirini DOĞRUDAN çağırmaz. Kompozisyon **subagent aracılığıyla**. Üç desen:
- **A)** subagent Skill tool'la herhangi bir skill'i çağırır (default).
- **B)** `skills:` frontmatter'ıyla subagent'a skill'leri ÖNYÜKLE (startup context).
- **C)** `context: fork` + `agent:` ile skill'i izole subagent'ta koştur (gövde = subagent prompt'u).
- **Önerilen `karar-hatti` yapısı:**
  ```
  .claude/skills/
  ├── celiski-kapisi/SKILL.md   # disable-model-invocation: true
  ├── karar-modeli/SKILL.md     # disable-model-invocation: true
  ├── karar-kaydet/SKILL.md     # disable-model-invocation: true  (yan-etki: commit)
  └── karar-hatti/SKILL.md      # context: fork, agent: general-purpose
  ```
  `karar-hatti` izole subagent'ta koşar; İÇİNDE `/celiski-kapisi → /research → /karar-modeli → /karar-kaydet` sırayla çağrılır (her çocuk talep-üzerine yüklenir).
- **Ders:** bileşiği TEK dev skill yapma → izole-subagent orkestratör + küçük çocuk skill'ler; kayıt AYRI `disable-model-invocation` skill (fren).

## 6. EVAL (skill-creator plugin — K-016 eval kuralının somut hali)
- `/plugin install skill-creator@claude-plugins-official`.
- `evals/evals.json` (test: prompt + assertion) → her test AYRI subagent (temiz bağlam) → `grading.json` (alanlar: `text`/`passed`/`evidence`) → `benchmark.json` (**with-skill vs without-skill**: pass-rate/token/süre) → **kör A/B** version karşılaştırma → **description tuning** (should-trigger/should-not) → HTML viewer.
- **Description eval (Atlas):** 20 sorgu (10 tetiklemeli + 10 tetiklemesiz) × 3 koşum, 60/40 train/val, overfit'ten kaçın. **Yayına girmeden ZORUNLU adım.**

## 7. Skill vs slash vs subagent vs hook (karar ağacı)
- "Claude anmasa da HEP çalışsın mı?" → **Hook** · "Claude karar versin mi?" → **Skill/Subagent** · "İzole çok-adım keşif mi?" → **Subagent** · "Referans bilgi/komut mu?" → **Skill**.
- Custom slash-command'lar skill'e BİRLEŞTİ (`.claude/commands/x.md` ≈ `.claude/skills/x/SKILL.md`).

## 8. Test + dağıtım
- **Test:** proje-scope skill + `skillOverrides: {x: off}` ile with/without baseline; sonra skill-creator eval.
- **Dağıtım:** proje (git commit, takım) · kişisel · plugin (marketplace/agentskills.io) · managed (org, öncelikli).

## 9. Atlas metodoloji bulguları (DONE) — üretim akışı + tuzaklar + kompozisyon
> Kaynak güven: **[D]** doğrudan resmi doküman/GitHub · **[A]** arama-özeti (site 403, teyide muhtaç).

### 9.1 ★ EVAL-ÖNCE üretim akışı (resmi, sezgiye aykırı) [D]
*"Önce eval yaz, SONRA doküman"* — hayali gereksinim yazma. 5 adım: (1) skill'siz koştur, boşluğu bul · (2) 3 senaryo eval'i yaz · (3) baseline ölç · (4) **minimal** gövde (eval'i geçecek kadar) · (5) iterasyon. **description ilk yazılan DEĞİL; eval ilk, description ince-ayarı EN SON.** **Claude A/B deseni:** Claude A yazar → Claude B taze bağlamda kullanır → gözlemle → A'ya geri taşı. *Not [D]: Claude skill formatını doğal bilir — meta-skill şart değil; skill-creator yalnız eval/paketleme iskelesi.* **Carvis dersi:** bizim kalıplar (çelişki, 3-model) zaten gözlenmiş tekrar → adım 1-2 tamam, doğrudan "eval + baseline"la başlarız.

### 9.2 Description zanaatı — kesin kurallar [D]
- **3. ŞAHIS her zaman** ("Extract text..." ✓, "I can help..." ✗) — sistem-prompt'a enjekte edilir.
- **NE + NE ZAMAN:** `[yetenek] + "Use when [gerçek kullanıcı ifadeleri / uzantı / jargon]"`. Kullanıcının GERÇEKTEN yazdığı ifadeler = tetik-anahtarı.
- **≤1024 karakter** (resmi; §1'deki 1536 [A] doğrulanmadı) · **gerund isim** (`processing-pdfs`) · `helper/utils` yasak.
- **"özet DEĞİL, NE ZAMAN tetiklenir'in tarifi"** (Anthropic) — en yaygın hata özet-yazmak (az-tetikleme).
- **Denge:** Claude az-tetikleme eğilimli → hafif "iddialı" yaz, AMA **negatif tetik** ("X'te KULLANMA") ile aşırı-tetiklemeyi kes (React skill'i Vue'yu dışlar).

### 9.3 Gövde [D]
`<500 satır`; *"bağlam penceresi kamu malı"* + *"Claude zaten akıllı — yalnız bilmediğini ekle"*; her cümle "token'ı hak ediyor mu?". **En yüksek-sinyal bölüm = "Gotchas"** (zamanla biriken gerçek hata noktaları). Referanslar **bir seviye derin** (iç içe ✗); >100 satır referansa İçindekiler. Emir-kipli numaralı adım + **checklist deseni** (kritik adım atlanmasın). **Tek skill = tek kategori/sorumluluk** (Anthropic: çok-kategoriye yayılan ajanı şaşırtır).

### 9.4 Script serbestlik-derecesi + yan-etki [D]
Serbestlik = işin kırılganlığı: **yüksek** (metin talimat, çok geçerli yol) · **orta** (parametreli) · **düşük** (kesin script, "komutu değiştirme"). *"Solve don't defer"* · voodoo-constant yok · çalıştır-mı-oku-mu açık · doğrulama script'i ayrıntılı hata döndürür. **plan-validate-execute** (yıkıcı/toplu iş): analiz → **plan dosyası** → **script'le doğrula** → uygula → teyit. → **kayıt/commit adımımız tam bu sınıf**: düşük-serbestlik script + m.31 publish/commit kapısı doğal oturur.

### 9.5 Tuzaklar (15) [D/A]
| # | Tuzak | Kaçınma |
|---|---|---|
|1| Şişmiş SKILL.md / context-rot | <500 satır, referansa böl |
|2| Eval'siz yayın | ≥3 eval + baseline ÖNCE |
|3| Description'ı özet yazmak (az-tetik) | "Use when" + gerçek ifadeler |
|4| Aşırı-tetikleme (dışlamasız pushy) | negatif tetik |
|5| Deterministik'i LLM'e bırakma | düşük-serbestlik script |
|6| Aşırı-kapsam (çok-iş) | tek sorumluluk |
|7| Çok seçenek sunma (karar felci) | bir varsayılan + kaçış |
|8| Derin iç içe referans | bir seviye derin |
|9| Kural yerleşimi (üstte, kullanımdan uzak) | kuralı kullanıldığı adıma koy |
|10| Zaman-duyarlı bilgi | "Old patterns" + `<details>` |
|11| Windows-yol / kurulu-varsayım | ileri-slash, bağımlılık listele |
|12| Voodoo constants | her sabiti gerekçelendir |
|13| Skill sprawl (çoğaltma) | periyodik audit + budama |
|14| Versiyonsuzluk | erken versiyonla, geri-dönebil |
|15| Çok-model test etmeme | Haiku/Sonnet/Opus'ta test |

### 9.6 ★ KOMPOZİSYON GERÇEĞİ + dersler (Salih hedefi) [A/D]
- **Çağrı GERÇEĞİ:** skill'ler birbirini literal çağırmaz — runtime'da `skill.call()` YOK. İki yol: **model-güdümlü** (Claude description'ları okuyup seçer) veya **literal** (`/skill-adı`). Orkestratör zincirlemeyi **gövde-adımlarıyla** yapar ("şu dosyayı oku / şu subagent'ı spawn et / şu script'i sırayla çalıştır"). Dosyalar OTO yüklenmez — gövde açıkça söyler.
- **3 desen:** skill-chain (bağımsız yeniden-kullanılabilir) · sub-agent (delege/paralel; ~20k token/ajan ek-yük [A doğrulanmadı]) · **orchestrator/router** (koşullu alt-skill seçer).
- **OneWave orkestratör dersi [D]:** YAML iş-akışı · topolojik DAG · state handoff · **hata yönetimi = güvenilirliğin kalbi**: her adım çıktıyı şemaya doğrular; başarısızlıkta `error` alanı yaz, **"fail fast and loud"**, retry-backoff; orkestratör bozuk veriyle ilerlemez, hata-skill'ine yönlendirir.
- **Gevşek bağlaşım:** çocuk-skill boru-hattını bilmez; **sabit-format handoff kontratı** (JSON/MD şema) → her skill bağımsız test edilebilir.
- **TEK skill mi ZİNCİR mi:** her-zaman-birlikte + tek-sorumluluk → tek skill (gövde-içi numaralı adım yeterli) · bağımsız-yeniden-kullanım / paralellik / izolasyon → zincir/orkestratör. **Pratik sınır ~3-4 skill** [A doğrulanmadı] — üstü handoff yönetilemez.
- **`karar-hatti` boru-hattına ders (sentez):** orkestratör-skill + gevşek-bağlı alt-skill'ler (tek dev skill DEĞİL) · **çelişki-kapısı = koşullu-yönlendirme** (çelişki→"rapor+Salih onayı"na dallan, deterministik) · **3-model = paralel-fan/sub-agent** (karşıt-gömülü) · **kayıt = yan-etkili terminal → script + plan-validate-execute + m.31 kapısı** · handoff = sabit format + `error` alanı + "fail loud" · description bizim gerçek ifadelerimiz ("çelişki/üç-model/karar üstüne karar") + negatif tetik ("tek-atımlık küçük görevde kullanma", m.25 uyumlu).

### 9.7 Yayın-öncesi checklist [D]
Description spesifik+anahtar-terimli+NE+NE ZAMAN · gövde<500 · detay ayrı dosya · zaman-duyarlı yok · tutarlı terim · referans bir-seviye · ≥3 eval · Haiku+Sonnet+Opus test · gerçek-senaryo test · **+bizim:** negatif tetik var mı · tek-kategori mi · yan-etki script'te+onay-kapısında mı · zincir-mi-tek-skill gerekçeli mi · handoff sabit-format mı.

### 9.8 Güvenilirlik [Atlas]
[D] resmi: name≤64 · desc≤1024 · gövde<500 satır · skill-creator akışı · OneWave orkestratör. [A] doğrulanmadı: subagent ~20k/3-4× token · ~3-4 skill sınırı · 1536 listeleme-kesme · medyan token değerleri. WebFetch 403 (Anthropic blog/Lessons tam-metni [A]).

## 10. `karar-hatti` için somut ders (özet)
Yapı §5'teki gibi: `celiski-kapisi`/`karar-modeli`/`karar-kaydet` ayrı (kayıt `disable-model-invocation:true`), `karar-hatti` = `context:fork` orkestratör. Gövde emir-kipli + m.38 lojik. Her birine skill-creator eval. Yan-etki = elle-fren.

## Kaynaklar + doğrulanmamış bayraklar
- claude-code-guide: code.claude.com/docs/en/skills.md · agent-sdk/skills.md · sub-agents.md · hooks-guide.md · github.com/anthropics/claude-plugins-official skill-creator. (Frontmatter/mekanik OTORİTER — docs.)
- Atlas skill-desenleri: agentskills.io · kepano · skill-creator v2 eval · repolar. **WebFetch 403** (birincil tam-metin yok, arama-özeti) + **GitHub API kapalı** (yıldız/lisans doğrulanmadı). Uygulamadan önce code.claude.com/docs güncel teyit.
