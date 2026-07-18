# Skill Nasıl Oluşturulur — Metodoloji Raporu (TARTIŞMA; Fable ile)

> **Mod:** rapor · KARAR YOK. **COMMIT: Salih 07-18 izin verdi** (branch'e, PC'den bulunabilirlik); **merge→main/canon = Fable Cowork süzgeci** (m.41). Amaç: üreteceğimiz skill KOMBİNASYONLARINA (ör. `karar-hatti`) ders. Kaynak: claude-code-guide (Claude Code otoriter mekaniği) + Atlas skill-desenleri (§8 skill-fikri-kutusu raporu) + Atlas skill-metodolojisi (koşuyor — §9'a işlenecek).

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

## 9. Tuzaklar tablosu (Atlas skill-metodoloji şeridi dönünce derinleşir)
| Tuzak | Kaçınma |
|---|---|
| Aşırı-kapsam (1 skill her şeyi yapar) | tek-sorumluluk; bileşeni zincirle (§5) |
| Şişmiş SKILL.md (>500 satır) | progressive disclosure; veriyi referans dosyaya (§3) |
| Yanlış-tetik | description dar/geniş → 20-sorgu eval (§6) |
| Deterministik'i LLM'e bırakma | kayıt/commit → script (§4) |
| Yan-etkiyi auto'ya açık bırakma | `disable-model-invocation: true` (§4) |
| Eval'siz yayın | skill-creator benchmark (§6) |
| Versiyon kayması | `version` alanı + kör A/B |

*[Atlas skill-metodoloji şeridi koşuyor → uçtan-uca üretim akışı + ek tuzaklar + kombinasyon-ilkeleri buraya işlenecek.]*

## 10. `karar-hatti` için somut ders (özet)
Yapı §5'teki gibi: `celiski-kapisi`/`karar-modeli`/`karar-kaydet` ayrı (kayıt `disable-model-invocation:true`), `karar-hatti` = `context:fork` orkestratör. Gövde emir-kipli + m.38 lojik. Her birine skill-creator eval. Yan-etki = elle-fren.

## Kaynaklar + doğrulanmamış bayraklar
- claude-code-guide: code.claude.com/docs/en/skills.md · agent-sdk/skills.md · sub-agents.md · hooks-guide.md · github.com/anthropics/claude-plugins-official skill-creator. (Frontmatter/mekanik OTORİTER — docs.)
- Atlas skill-desenleri: agentskills.io · kepano · skill-creator v2 eval · repolar. **WebFetch 403** (birincil tam-metin yok, arama-özeti) + **GitHub API kapalı** (yıldız/lisans doğrulanmadı). Uygulamadan önce code.claude.com/docs güncel teyit.
