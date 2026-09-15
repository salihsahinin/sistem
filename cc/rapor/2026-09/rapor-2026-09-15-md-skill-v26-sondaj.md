# V26 örneklem-denetimi — md→skill atlas koşumu (2026-09-15, Fable ana-sıra; kural-tabanlı sondaj)
Sondaj: her tez raporunun son üçlüğünden ≥1 URL'li iddia + tüm sayısal iddialar + ≥1 URL'siz iddia; kaynağa inildi (WebFetch, çekim 2026-09-15).

| Tez | İddia | Birincil kaynak | Sonuç |
|---|---|---|---|
| A2 | CLAUDE.md 200 satır altı hedef; 4 MiB üstü atlanır | code.claude.com/docs/en/memory | **D** — "target under 200 lines per CLAUDE.md file"; "skips a file over 4 MiB" |
| A2 | @import ≤4 hop; import launch'ta yüklenir, tasarruf yok | aynı | **D** — "maximum depth of four hops"; "imported files still load … at launch" |
| A2 | MEMORY.md ilk 200 satır ∨ 25 KB | aynı | **D** |
| A2 | Yükleme sırası managed → user → project → local; en yakın en son | aynı | **D** — tablo "in load order, from broadest scope to most specific" |
| A2 | Alt-dizin CLAUDE.md lazy | aynı | **D** — "included when Claude reads files in those subdirectories" |
| A2 | "aynı hatayı ikinci kez yapınca ekle" | aynı | **D** — "When to add to CLAUDE.md" 4 madde; **EK BULGU:** "If an entry is a multi-step procedure or only matters for one part of the codebase, move it to a skill or a path-scoped rule" — resmî md→skill kuralı (tez A1 iddia 6 "kesin kural yok" → DARALDI) |
| A1 | Metadata ~100 token/skill; gövde <5k token; name ≤64, description ≤1024 | platform.claude.com …/agent-skills/overview | **D** — tablo aynen |
| A1 | Script kodu bağlama girmez, yalnız çıktı | aynı | **D** |
| A1 | SkillsBench: 84 görev, +16,2 pp, 16 görevde negatif, self-generated −1,3, 2-3 modül optimum | arxiv.org/abs/2602.12670 (abstract) | **DARALDI** — abstract: **87 görev, 8 alan, 18 konfig, 33,9→50,5 (+16,6 pp), "en fazla 3 modül"**; "16 negatif" ve "self-generated −1,3" abstract'ta YOK (ikincil emergentmind özeti) → K |
| A1 | Kun Chen "Program Bench" ölçümü | video transkripti (Downloads, 2026-06-20, 19:06-19:40) | **K** — birincil kaynak videonun kendisi; yayınlanmış benchmark bulunamadı; Kun Chen'in kendi ölçümü, yayınsız |
| A3 | "Prefer scripts for deterministic operations" + low/medium/high freedom | platform.claude.com …/best-practices | **D** — aynen |
| A3 | SKILL.md gövde 500 satır altı | aynı | **D** |
| A3 | ≥3 eval, Haiku/Sonnet/Opus testi checklist | aynı | **D** |
| A3 | "There is not currently a built-in way to run these evaluations" | aynı | **D** — aynen |
| A3 | plan-validate-execute deseni | aynı | **D** — "Create verifiable intermediate outputs" |

Ek birincil bulgular (hakeme ham kanıt): (1) `.claude/rules/*.md` + `paths:` frontmatter = üçüncü mekanizma (dosya-kapsamlı koşullu yükleme; skill'den farkı: tetik = dosya okuma, açıklama eşleşmesi değil). (2) "CLAUDE.md content is delivered as a user message after the system prompt" — kural değil bağlam; zorlama = hook. (3) `/doctor` CLAUDE.md kırpma önerir (koddan türetilebilen içeriği keser). (4) `InstructionsLoaded` hook: hangi talimat dosyasının ne zaman yüklendiğini kütükler — bağlam-izleme için hazır araç (İB-81 ön-koşulu!). (5) Auto-memory tüm worktree'lerde paylaşılır; CLAUDE.local.md paylaşılmaz.
