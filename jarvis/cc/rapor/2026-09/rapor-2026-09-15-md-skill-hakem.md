# Hakem raporu — md→skill atlas koşumu (2026-09-15, Opus 5 medium, maskeli; yapan ≠ ölçen)

## Hakem raporu — üç aile, maskeli kıyas (AS-OF 2026-09-15)

Kullanılan araç: 6 WebFetch (arxiv abs, arxiv html v1, platform overview, platform best-practices, code.claude.com/memory, code.claude.com/skills).

### Aile A1 — hafıza md → skill taşıma

| No | Hüküm | Etiket | Gerekçe + URL |
|---|---|---|---|
| 1 (~100 token/skill) | sağlam | **D** | Overview'un seviye tablosunda birebir "~100 tokens per Skill" yazıyor; karşı-taraf yanlış sayfaya (best-practices) bakmış. platform.claude.com/docs/en/agents-and-tools/agent-skills/overview |
| 2 (gövde bash ile okunur) | sağlam | **D** | "Claude reads SKILL.md from the filesystem using bash. Only then does this content enter the context window." aynı URL |
| 3 (gövde <5k token) | sağlam | **D** | Aynı tabloda Level 2 için "Under 5k tokens"; best-practices'teki "under 500 lines" ayrı sayfanın ayrı birimi, çelişki değil |
| 4 (script kodu bağlama girmez) | sağlam | **D** | "the script code itself never enters context" aynı URL |
| 5 (CLAUDE.md statik / skill koşullu) | sağlam | **D** | "Unlike CLAUDE.md content, a skill's body loads only when it's used" code.claude.com/docs/en/skills |
| 6 ("kesin kural yok") | **düştü** | **D** | Resmî kural var: "If an entry is a multi-step procedure or only matters for one part of the codebase, move it to a skill or a path-scoped rule instead." code.claude.com/docs/en/memory |
| 7 (84 görev, +16,2 pp, 16 negatif) | sağlam (sürüm-koşullu) | **D** | arxiv.org/html/2602.12670v1: 84 görev / 11 alan / 7 konfig / +16,2 pp / 84'ün 16'sında düşüş |
| 8 (self-generated −1,3 pp) | sağlam | **D** | v1: kendi üretimi rehberlik ortalamada −1,3 pp |
| 9 (2-3 modül +18,6; kapsamlı −2,9) | sağlam | **D** | v1 birebir bu rakamlar |
| 10-11 (Kun Chen / "Program Bench") | **düştü** | **X** | Yayınlanmış benchmark hiçbir tarafça bulunamadı; bir taraf blog yazısının programlama-dili konulu olduğunu, diğeri kaynağın yayınsız video olduğunu söylüyor — atıf çürük |
| 12 (skill-creator'da md→skill akışı yok) | daraldı | **K** | Birincil GitHub dosyası açılmadı; ama resmî md→skill kuralı memory belgesinde var (md.6) |
| Ek: SkillsBench context-confound | sağlam | **D** | v1 Limitations: "observed gains could partly reflect increased context rather than procedural structure" |

**84/87 çelişkisinin çözümü:** ikisi de birincil, farklı sürüm. arXiv **html v1** = 84 görev, 11 alan, 7 konfig, +16,2 pp. arXiv **abs (güncel sürüm)** = 87 görev, 8 alan, 18 konfig, 33,9→50,5 (+16,6 pp), "at most 3 modules". Güncel sürüm 87'dir; 84 eskimiş rakamdır. Abstract'ta "16 negatif" ve "−1,3" yok — bunlar v1 gövdesinde var, uydurma değil.

### Aile A2 — çok-proje md hiyerarşisi

| No | Hüküm | Etiket | Gerekçe (hepsi code.claude.com/docs/en/memory) |
|---|---|---|---|
| 1 sıra managed→user→project→local | sağlam | **D** | "in load order, from broadest scope to most specific"; "instructions closer to where you launched Claude are read last" |
| 1b "en son = en etkili" | **düştü** | **X** | Ölçüm yok; belge tersini kabul ediyor: "if two rules contradict each other, Claude may pick one arbitrarily" |
| 2 alt-dizin lazy | sağlam | **D** | "Instead of loading them at launch, they are included when Claude reads files in those subdirectories" |
| 3 ≤4 hop, import tasarruf etmez | sağlam | **D** | "maximum depth of four hops"; "imported files load at launch" |
| 4 200 satır hedef / 4 MiB atlanır | sağlam | **D** | "target under 200 lines per CLAUDE.md file"; "skips a file over 4 MiB" |
| 5 MEMORY.md 200 satır ∨ 25 KB | sağlam | **D** | "first 200 lines of MEMORY.md, or the first 25KB, whichever comes first" |
| 6 AGENTS.md import/symlink | sağlam | **D** | "Claude Code reads CLAUDE.md, not AGENTS.md" |
| 7 AAIF / 30+ araç | daraldı | **K** | İki taraf farklı rakam veriyor (20+ vs 30+ araç); birincil açılmadı |
| 8 Gemini CLI önceliği | daraldı | **K** | Yalnız ikincil |
| 9 `--worktree`, "en az 1 commit şart" | daraldı | **K** | memory belgesinde yok; worktrees sayfası açılmadı |
| 10 CLAUDE.local.md worktree-yerel, auto-memory paylaşılır | sağlam | **D** | "a gitignored CLAUDE.local.md only exists in the worktree where you created it"; "all worktrees … share one auto memory directory" |
| 11 "ikinci kez hata → ekle" | sağlam | **D** | "When to add to CLAUDE.md: Claude makes the same mistake a second time" |
| 11b Kun Chen haftalık-toplu + 5k bütçe | daraldı | **K** | Yalnız blog; Anthropic böyle bir ritim önermiyor |
| 12 Codex 32 KiB | daraldı | **K** | İkincil |

Ek: "tek global md'nin çok-proje zararı" hiçbir birincil kaynakta ölçülmemiş — **X**, A2'nin en savunmasız varsayımı.

### Aile A3 — skill = kalıp-prompt, deterministik icra

| No | Hüküm | Etiket | Gerekçe |
|---|---|---|---|
| 1 script tavsiyesi / low freedom | sağlam | **D** | "Prefer scripts for deterministic operations: Write `validate_form.py` rather than asking Claude to generate validation code"; "Low freedom … Operations are fragile and error-prone" (best-practices) |
| 2 zorunlu alan yalnız name+description | **daraldı** | **D+çelişki** | platform: "The SKILL.md frontmatter requires two fields"; code.claude.com/docs/en/skills: tüm frontmatter alanları isteğe bağlı, yalnız `description` tavsiye. İki ürün yüzeyi farklı |
| 3 disable-model-invocation | sağlam | **D** | Artık birincil: otomatik yüklemeyi engeller, `/ad` ile elle çağrılır (code.claude.com/docs/en/skills) |
| 4 allowed-tools ön-onay, bloklamaz | sağlam | **D** | "Does NOT block other tools"; blokaj ayrı alan `disallowed-tools` |
| 5 plan-validate-execute | sağlam | **D** | "The 'plan-validate-execute' pattern catches errors early…" (best-practices) |
| 6 yerleşik eval yok | sağlam | **D** | "There is not currently a built-in way to run these evaluations." Yan-not doğru: skill-creator eklentisi ayrı bir hat sunuyor, platform-native değil |
| 7 Executor/Grader/Comparator/Analyzer | daraldı | **K** | Birincil GitHub dosyası hiçbir tarafça açılmadı |
| 8 varyans-analizi var, tutarlılık rakamı yok | sağlam | **K** | Pass-rate rakamı var (+16,6), run-to-run varyans rakamı hâlâ yok |
| 9 determinizm hook/script'te | sağlam | **D** | memory: "CLAUDE.md content is delivered as a user message"; "use a PreToolUse hook instead" |
| 10-11 (Warp, Vercel, SkillsBench doğrulanmadı) | 11 sağlamlaştı | **D** | SkillsBench artık birincil doğrulandı (görev sayısı 87, v1'de 84); Warp/Vercel hâlâ **K** |
| 12 `context: fork`, `agent:`, `paths:` | sağlam | **D** | Hepsi code.claude.com/docs/en/skills'te tanımlı |

### Hayatta-kalan çekirdek
**A1:** ~100 token metadata; 5k token gövde bütçesi; script kodu bağlama girmez; skill koşullu / CLAUDE.md statik; SkillsBench 2-3 modül optimumu; SkillsBench'in kendi context-confound itirafı.
**A2:** yükleme sırası; alt-dizin lazy; import ≤4 hop ve tasarruf etmez; 200 satır / 4 MiB / MEMORY.md 200-25KB sınırları; AGENTS.md köprüsü; worktree ayrımı.
**A3:** deterministik iş için script; plan-validate-execute; yerleşik eval yok; allowed vs disallowed ayrımı; determinizm hook'ta; Claude Code'a özgü frontmatter alanları.

### Düşen / daralan
- "Resmî kaynak md→skill kuralı vermiyor" — **düştü** (memory belgesinde açık kural var).
- "En son okunan = en etkili" — **düştü** (ölçüm yok, belge rastgele seçimi kabul ediyor).
- Kun Chen "Program Bench" atfı — **düştü**.
- "Zorunlu alan yalnız iki" — **daraldı** (yalnız platform yüzeyi).
- SkillsBench 84/+16,2 — **daraldı** (eski sürüm; güncel 87/+16,6).
- Warp skill-doctor, Vercel `npx skills`, Codex 32 KiB, Gemini önceliği, worktree "1 commit şartı", skill-creator dört-ajan hattı — hepsi **K**, ikincil.

### Çelişkili (çözülmemiş)
1. platform "iki zorunlu alan" ↔ Claude Code "tüm alanlar isteğe bağlı" — aynı sağlayıcı, iki yüzey; hangi yüzeyde çalışıldığı belirtilmeden iddia kurulamaz.
2. AGENTS.md ekosistem rakamı 20+ ↔ 30+ araç; her ikisi de ikincil.
3. CLAUDE.md güncelleme ritmi: olay-tetikli (birincil) ↔ haftalık toplu (blog, ikincil) — birincil kaynak ikinciyi desteklemiyor.
4. Çok-proje tek-global-md zararı: iddia edilmiş, hiçbir kaynakta ölçülmemiş.
