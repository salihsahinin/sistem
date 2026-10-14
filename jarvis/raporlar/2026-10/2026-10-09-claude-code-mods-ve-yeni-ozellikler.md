# Claude Code: mods + son 2 ayın özellikleri (AS-OF 2026-10-09)

*Üreten: Sonnet işçi ajanı (`claude-code-guide`), 12 araç çağrısı · 75.884 token · 94 sn (harness kütüğü). Ajanın Write aracı olmadığı için dosyayı Jarvis dönüş metninden yazdı. Kaynaklar canlı okundu; okunmayanlar `[?]` ile işaretli.*

## A) Mods

- **Yayın:** blog yazısı 2026-10-01, yazar Addy Osmani. Aynı gün v2.1.287 ile çıktı. Kaynak: https://claude.dev/blog/getting-started-with-claude-code-mods/
- **Tanım:** mod, plugin içinde JS/TS olarak yazılmış bir olay işleyicisidir ("function hook"). Claude Code sürecinin içinde, oturumla birlikte çalışır. Settings hook'undan (`settings.json` komutu) farkı üç tane: bir kez yüklenir, durum tutar ve ekrana UI çizer. Kaynak: https://code.claude.com/docs/en/plugins/mods/overview.md
- **Dosya yapısı:** `.claude-plugin/plugin.json` · `hooks/hooks.json` (`{"modules":["./x.mjs"]}`) · `hooks/x.mjs` içinde `register(on)`.
- **Mekanizma (middleware zinciri):** `on("tool.call", {tool:"Bash"}, async ($, e, next) => ...)`
  - **gözle:** `next(e)` çağrılır, sonuç incelenir.
  - **yeniden yaz:** `next({...e, ...})` ile olay değiştirilir.
  - **yanıtla:** `next` hiç çağrılmaz, `{deny:"..."}` döner.
- **Olaylar:** `tool.call` · prompt gönderimi · turn başı ve sonu · session başı ve sonu · `command.run` · `ui.render`.
- **UI parçaları:** `AbovePrompt` (prompt üstü band) · `Pane` · `Spinner` · `$.ui.status` · `$.ui.toast`. Kaynak: https://code.claude.com/docs/en/plugins/mods/interface.md
- **Kısıtlar:**
  - DOM ve Node erişimi yok; her şey `$` API'sinden geçer.
  - Hook başına 10 sn sınırı var; `$` içinde geçen süre bu sınıra sayılmaz.
- **Hot reload:** mod klasörü izlenir ve her kayıtta yeniden yüklenir. `register` her yüklemede tekrar koştuğu için kalıcı veri `$.state`'te tutulmalı.
- **Kurulum:**
  - `claude --plugin-dir ./mod`
  - `claude plugin marketplace add ./m` + `claude plugin install ad@m --scope user`
  - oturum içinde `/plugin install` + `/reload-plugins`
- **Doğrulama:** `claude plugin validate` · `claude plugin test` · `claude --debug`.
- **Yüzeye göre davranış:**

  | Yüzey | Hook'lar | UI çizimi |
  |---|---|---|
  | Terminal | çalışır | var |
  | Desktop Code tab (v2.1.286+) | çalışır | var; bazı elemanlar yalnız terminalde |
  | VS Code paneli · `claude -p` · SDK | çalışır | yok |
  | WSL oturumu | yok (plugin yok) | yok |

- **Güvenlik:**
  - Mod senin izinlerinle çalışır ve sandbox'a alınmaz: dosya, süreç, ağ ve ortamdaki sırlara erişebilir.
  - Bir `ask` kuralını atlayıp çağrıyı kendisi onaylayabilir; izin isteminin kendisini ise değiştiremez.
  - Kapatma yolları: `--safe-mode` · `"disableAllHooks": true` · kurumda `allowManagedModsOnly`.
- **Yerleşik modlar:** `cc-plugin-agents-md` · `cc-plugin-diff` · `cc-plugin-you-should-know` (varsayılan kapalı). Kaynak: https://github.com/anthropics/claude-code/tree/main/mods
- **Örnekler** (https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods):
  - `token-weather`: bağlam doluluğunu band olarak gösterir.
  - `blast-radius`: riskli Bash komutunu yakalar, pane'de Proceed/Cancel sorar.
  - `replay-theater`: `/replay` ile son turdaki edit'leri adım adım oynatır.

## B) Changelog 2026-08-09 → 2026-10-09

Kaynak GitHub releases. Ajan yılı 2026 olarak varsaydı; ayrıntısı yazmayan sürümler listede yok. Liste tam değil `[?]`.

| Sürüm | Tarih | Not |
|---|---|---|
| 2.1.227-229 | 08-10 → 08-12 | plugin marketplace `command` kaynağı · çökme düzeltmeleri |
| 2.1.232 | 08-13 | subagent forking varsayılan · `@` ile başka oturuma mesaj |
| 2.1.234 | 08-17 | limit sıfırlanınca otomatik devam · GitLab MR rozeti |
| 2.1.235-239 | 08-18 → 08-21 | `spellcheck` · `ANTHROPIC_DEFAULT_MODEL` · Concise output style · `keybindingFlavor` |
| 2.1.246-248 | 08-25 → 08-27 | `/permissions` Auto mode sekmesi · `SendFeedback` · `--restricted` |
| 2.1.251 | 08-28 | `PreModelSwitch` / `PostModelSwitch` hook'ları |
| 2.1.257 | 09-01 | Fable 5.1 varsayılan Fable modeli |
| 2.1.259-261 | 09-02 → 09-04 | `--permission-prompts none` · fullscreen `/diff` · `/skill-doctor` |
| 2.1.265-269 | 09-08 → 09-11 | `--plugin-dir` klasör · `maxEffortLevel` · `claude plugin eval` |
| 2.1.275 | 09-17 | send-now tuşu · claude.ai skill/plugin terminal senkronu |
| 2.1.277 | 09-18 | CLAUDE.md yoksa AGENTS.md okunur |
| 2.1.280 / 2.1.284 | 09-22 / 09-28 | Opus 5.5 / Sonnet 5.5 varsayılan |
| 2.1.283 | 09-25 | `deniedModels` · `/doctor prompt-audit` |
| 2.1.285 | 09-29 | `claude --desktop` · `claude plugin configure` |
| 2.1.287 | 10-01 | **Mods** · "You should know" |
| 2.1.288-290 | 10-02 → 10-05 | Ctrl+C sonrası taslak kurtarma · `claude attach` / `claude logs` · WebFetch `offset` |
| 2.1.292-293 | 10-06 → 10-07 | `plugin install --marketplace` · Agent aracına `effort` · Haiku 5.5 |
| 2.1.295 | 10-08 | hook `onFailure:"block"` · OSC 7501 durum protokolü |

## C) Kullanılmayan değerli özellikler

Zaten kullanılanlar: skills · hooks (SessionStart, UserPromptSubmit, PreToolUse) · subagents · Workflow · CLAUDE.md/AGENTS.md · memory · MCP · artifacts/lavish.

| # | Özellik | Ne yapar | Nasıl |
|---|---|---|---|
| 1 | Mods | oturuma pane, band ve komut ekler | `claude --plugin-dir ./mod` |
| 2 | Goal | oturumu hedefe ulaşana dek sürdürür | docs `goal.md` (komut adı doğrulanmadı `[?]`) |
| 3 | attach / logs | arka plan oturumlarına bağlanır | `claude attach <ad>` · `claude logs <ad>` |
| 4 | Checkpoints / rewind | kodu ve konuşmayı geri sarar | docs `checkpointing.md` (tuş doğrulanmadı `[?]`) |
| 5 | Routines / scheduled | cron'lu bulut ajanı, periyodik komut | `/schedule` · `/loop 5m /komut` |
| 6 | Plugin eval | skill/plugin için puanlı test seti | `claude plugin eval` |
| 7 | Remote Control | oturumu telefondan sürer | docs `remote-control.md` (Windows doğrulanmadı `[?]`) |
| 8 | Cross-session messaging | oturumlar arası mesaj | `@oturum` · docs `cross-session-messaging.md` (Windows `[?]`) |

Ek sayfalar (içerikleri okunmadı `[?]`): `statusline.md` · `output-styles.md` · `keybindings.md` · `worktrees.md` · `deep-links.md` · `channels.md` · `sandboxing.md` · `fast-mode.md`.
