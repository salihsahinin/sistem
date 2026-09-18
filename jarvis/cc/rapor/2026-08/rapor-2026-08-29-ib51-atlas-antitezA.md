# İB-51 atlas — ANTİTEZ (¬) aile A — ham işçi çıktısı (Sonnet, effort düşük; CoVe-Factored; 6/15 WebFetch/WebSearch + gh api/CHANGELOG; 2026-08-29)

¬A-1: `.claude/rules/` varlığı ve rekürsif tarama çürütülemedi; symlink alt-durumu 3 açık issue ile çelişiyor: #88405 (2026-08-20 "Symlinked files in .claude/rules/ are not auto-loaded (contradicts docs)"), #90523, #90525 (2026-08-29; 2.1.241/2.1.251). K.
¬A-2: bulunamadı (iddia ayakta). X.
¬A-3: belge aynı cümleyi kullanıyor; pratikte #88565 (2026-08-21, açık) "Auto mode… Bash edits never trigger rule injection", #87217 (2026-08-16, açık) kullanıcı-seviyesi `paths:` kural hiç yüklenmiyor; #19377 (kapalı 2026-03-19) `paths:` YAML listesi CSV ayrıştırıcıdan geçiyordu. K.
¬A-4: bulunamadı (1.000 / 4 MiB birebir); yan not #83299 (açık) gövde-metni parse maliyeti. X.
¬A-8: belge birebir; `paths:`'lı kullanıcı kuralı için #87217/#21858/#22170 "hiç yüklenmiyor". K.
¬A-10: belge birebir; #90449 (2026-08-28, açık) "Subdirectory CLAUDE.md loads only via the Read tool — every other file access path silently skips it"; #90450 Auto Mode. K.
¬A-12: bulunamadı (iddia ayakta). X.
¬A-14: CHANGELOG "2.1.9 — Added support for PreToolUse hooks to return additionalContext" (npm 2026-01-15) — "başlangıçta sessizce yok sayılıyordu" çerçevesi abartılı (yeni özellik); UserPromptSubmit additionalContext v1.0.59'dan beri; "dropped when tool call fails" düzeltmesi 2.1.9 sonrası. K.
¬A-17: deterministik tetik doğru; "additionalContext Claude'a ulaşır" açık issue'larla daralıyor: #90296 (2026-08-28) aralıklı ulaşmıyor, #89125 PreToolUse ephemeral, #85917 SubagentStop, #84011 trailing-newline cache, #88086 SessionStart "succeeded but never injected". K.
¬A-18, ¬A-19, ¬A-24, ¬A-26: bulunamadı (iddia ayakta). X.
¬A-21: skills belgesi frontmatter'da `paths` alanı tanımlıyor ("Glob patterns that limit when this skill is activated… Uses the same format as path-specific rules") → "skill tetiklenmesi deterministik değildir" evrensel önermesi yanlış; en az bir deterministik yol var. K.

SON ÜÇTE BİR: ¬A-21 (K, kaynaklı).
Kanıt kısıtı: canlı reprodüksiyon yok; issue'lar kullanıcı raporu (Anthropic teyidi değil), "open" = en güncel yamada sürdüğünü garanti etmez; CHANGELOG satır→sürüm eşlemesi grep ile.
