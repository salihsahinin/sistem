# Claude Code'da konuşulabilir persona mekanizmaları (claude-code-guide ajanı, AS-OF 2026-10-29, docs canlı)

Kaynak: code.claude.com/docs (output-styles, sub-agents, skills, cli-reference, settings-reference, memory, desktop sayfaları).

| Mekanizma | Dosya | Konuşma başlangıcı | Sınır |
|---|---|---|---|
| Output style | `.claude/output-styles/sokrates.md` (proje) ya da `~/.claude/output-styles/` | `/output-style sokrates` ya da `settings.local.json` `{"outputStyle":"sokrates"}` | `keep-coding-instructions: false` ile mühendislik bölümü çıkar; ana sohbete uygulanır, alt-ajanlara uygulanmaz; yeni dosya yeniden başlatma ister; ayar adı büyük-küçük harf duyarlı |
| Custom subagent | `.claude/agents/sokrates.md` (`name`, `description`, `model`, `tools`, `maxTurns`, `memory`…) | `claude --agent sokrates` (tüm oturum bu prompt/model/araçla) ya da `settings.json` `"agent":"sokrates"` | Normal oturumda yalnız ana ajan çağırır; persona için `--agent` gerekir; desktop'ta bayrak davranışı doğrulanmadı |
| Skill / slash | `.claude/skills/sokrates/SKILL.md` (`disable-model-invocation: true`, `argument-hint`) | `/sokrates <konu>` | Talimat oturuma girer, kalır; docs persona mekanizması saymaz; `model` yalnız o tura etki eder |
| Plugin / mod | output style + agent + skill + hook paketi; `force-for-plugin: true` stili otomatik uygular | plugin etkinleşince | Resmi pane API'si yok; jarvis-oda/graf yerel mekanizma |
| CLI bayrakları | `--system-prompt(-file)`, `--append-system-prompt(-file)`, `--agent` | her açılışta verilir | docs: otomasyon için, interaktif için değil |
| CLAUDE.md | dizin bağlamı | otomatik | zorunlu yapılandırma değil, persona için uygun değil |

## Öneri (ajan): Windows 11 desktop
- Ayrı klasör (ör. `C:\sistem\sokrates`) + `.claude/settings.local.json` `{"outputStyle":"sokrates"}` + stil dosyası; klasör desktop'ta açılınca persona gelir. İlk oturumda test şart (talimat zorunlu değil, sistem promptuna eklenir).
- Terminal için `sokrates.bat` → `claude --agent sokrates` (gerçek ayrı prompt + araç kısıtı).

## Jarvis hükmü
İkisi birden kurulur: output style (desktop tek tık) + agent dosyası (terminal `--agent` + alt-ajan testi) + `/sokrates` skill (bu oturumda hızlı deneme). Kaynak tek: `core/sokrates-ajani.md`; üç yüzey ondan türetilir.
