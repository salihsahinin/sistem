# İB-51 atlas — TEZ aile A (Claude Code yerli mekanizmaları) — ham işçi çıktısı (Sonnet, effort düşük; 9 WebFetch + 3 WebSearch + 2 gh; 2026-08-29)

Künye: emir `cc/gorev-2026-08-29-ib51-atlas.md` (untracked, sha256 edfa194f…) · HEAD 6a975f5.

## İddialar
A-1. `.claude/rules/` resmî ve canlı; her `.md` bir kural konusu; alt-dizinler rekürsif taranır. D · https://code.claude.com/docs/en/memory · AS-OF 2026-08-29.
A-2. `paths:` olmayan kurallar açılışta `.claude/CLAUDE.md` ile aynı öncelikte yüklenir (koşulsuz). D · aynı.
A-3. `paths:` alanlı kurallar deterministik dosya-eşleşmesiyle tetiklenir: "Path-scoped rules trigger when Claude reads files matching the pattern, not on every tool use." D · aynı.
A-4. Glob: `**/*.ts`, `src/**/*`, `*.md`, brace-expansion `src/**/*.{ts,tsx}`; tüm `paths` listesi 1.000 genişletilmiş desen + 4 MiB bütçesi; aşan desen literal. D · aynı.
A-5. v2.1.217 öncesi çok brace-gruplu desen CLI açılışını donduruyordu (düzeltildi). D · aynı.
A-6. v2.1.207 öncesi geçersiz `[` deseni Read'i her dosyada düşürüyordu (düzeltildi). D · aynı.
A-7. `.claude/rules/` symlink destekler; dairesel symlink zararsız. D · aynı.
A-8. `~/.claude/rules/` proje kurallarından ÖNCE yüklenir (proje önceliği yüksek). D · aynı.
A-9. `--setting-sources` `project` hariçse proje kuralları atlanır; v2.1.211 öncesi path-scoped kurallar yine yükleniyordu (bug, düzeltildi). D · aynı.
A-10. Alt-dizin CLAUDE.md/CLAUDE.local.md AÇILIŞTA yüklenmez; o dizindeki dosya okununca dahil edilir (birebir alıntı). D · aynı.
A-11. Çalışma dizini ve üst dizinlerin CLAUDE.md'leri açılışta kök→çalışma sırasıyla concatenate (üzerine yazma yok); CLAUDE.local.md sonra. D · aynı.
A-12. Resmî çerçeve: "Rules load into context every session or when matching files are opened. For task-specific instructions that don't need to be in context all the time, use skills instead, which only load when you invoke them or when Claude determines they're relevant." D · aynı.
A-13. `InstructionsLoaded` hook'u path-specific kural/lazy dosya yüklemesini loglar (debug). D · aynı.
A-14. PreToolUse `additionalContext` başlangıçta yoktu; issue #15664 (2025-12-29): "PreToolUse additionalContext is silently ignored… PostToolUse, SessionStart, and UserPromptSubmit additionalContext all work"; v2.1.9'da eklendi (kapanış 2026-01-16). D · https://github.com/anthropics/claude-code/issues/15664.
A-15. UserPromptSubmit `additionalContext` `hookSpecificOutput` içine konmalı; üst seviyede sessizce yok sayılır. K (arama alıntısı, hooks-guide).
A-16. v2.1.4'te UserPromptSubmit `hookSpecificOutput` yeni oturumun ilk mesajında sahte "hook error" gösterdi; issue #17550 (2026-01-11 → 2026-02-25 kapandı; düzeltme commit'i [?]). D.
A-17. Hook'lar araç-olayında DETERMİNİSTİK tetiklenir; enjekte içerik script mantığına bağlı; "Output reaches Claude via additionalContext JSON." D · https://code.claude.com/docs/en/context-window.
A-18. Skill `description`+`when_to_use` listede 1.536 karakterde kesilir (`skillListingMaxDescChars`). D · https://code.claude.com/docs/en/skills.
A-19. Skill listesi bütçesi bağlam penceresinin %1'i; `skillListingBudgetFraction` / `SLASH_COMMAND_TOOL_CHAR_BUDGET`; taşınca en az kullanılan skill açıklaması önce düşer. D · aynı.
A-20. `/context` Skills satırı bütçe sonrası boyutu raporlar; v2.1.196 öncesi tam metni sayıyordu (bug). D · aynı.
A-21. Skill tetiklenmesi MODEL-SEÇİMLİ ("description helps Claude decide when to load"). D · aynı.
A-22. Frontmatter: varsayılan açıklama bağlamda + iki taraf çağırır; `disable-model-invocation: true` açıklama bağlamda değil, yalnız kullanıcı; `user-invocable: false` yalnız Claude. D · aynı.
A-23. `/context` kategori dağılımı + hangi CLAUDE.md/auto-memory yüklendi. D · context-window.
A-24. Statusline JSON: `context_window.used_percentage/remaining_percentage/context_window_size (200000|1000000)/total_input_tokens/total_output_tokens`, `exceeds_200k_tokens`; used_percentage yalnız input+cache. D · https://code.claude.com/docs/en/statusline.
A-25. Statusline yerel, API token tüketmez. D · aynı.
A-26 (son üçte bir). `/init` Cursor (`.cursor/rules/`, `.cursorrules`) ve Copilot (`.github/copilot-instructions.md`) kurallarını CLAUDE.md'ye katar; `CLAUDE_CODE_NEW_INIT=1` ile AGENTS.md, `.devin/rules/`, `.windsurf/rules/`, `.clinerules` da okunur. D · memory.

## Kanıt kısıtı
hooks.md üç WebFetch'te tutarsız özetlendi → alan tablosu X, çapraz doğrulama GitHub issue + context-window ham dökümü; `/docs/en/hooks-reference` 404; WebFetch özetleyici ara-katman: yalnız "output too large" ham dökümleri D; #17550 düzeltme commit'i [?]; dış erişim 9+3 (+2 gh).
