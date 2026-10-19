# Claude Code Modları (claude-mods): status line, pane, slash komutu, hook, toast

> **Kaynak emir:** `ortak/durum-olay.jsonl` id 16 (2026-10-16): "ogren ile şerit aç: Claude Code modları (status line, pane, slash komutu, hook, toast); sistemde mod fikir yapısı; uygulanacak mod → Jarvis devri".
> **[sapma]** Jarvis'ten `cc/gelen/ders-<hafta>.md` iskeleti yok; müfredat aşağıda **taslaktır**, `PROBE` sonucuna göre Salih onayıyla kesinleşir. Jarvis'e "iskelet gerekli" notu `cc/giden/`'e yazılır.
> **Alan notu:** bağlam alanının dışı (araç öğrenimi). Bağ: mod = bağlama giren/çıkan her şeye kanca (`prompt.compose`, `tool.call`), dolayısıyla bağlam bütçesi modellemesine ürün adayı üretir.

**Yüzey:** `seans başı, claude-mods`. Terminalde görsel = Artifact sayfası (Salih 2026-10-16, A).

## Sınırlar
- **Kod yazımı bu şeritte değil, ders:** mod yazma alıştırması Salih'in eli (pratik = Salih'in eli). Uygulanacak mod Jarvis'e `cc/giden/` ile devredilir, Span yazmaz (kök md.14 tek-yazar).
- **Karar 73:** her derste ≥1 formül ya da somut ölçülebilir ilişki (örn. hook zinciri bileşimi `f₁∘f₂∘…∘motor`).
- **Karar 68:** API yüzeyi AS-OF damgalı; kaynak = bu yapıdaki `plugin-authoring` skill'i (build 2.1.301, 2026-10-16; M0 dersinde canlı yüklenen sürüm 2.1.299, 2026-10-19; M1'de yeniden teyit) + resmi docs; tahmin değil, canlı tipler (`claude-code.d.ts`).
- **md.49:** işyeri verisi girmez.

## Müfredat taslağı (kutu = 1 oturum; sektör başlığı EN; AS-OF 2026-10-16)
| M | Konu | Sektör başlığı | Tek-satır `DONE` (Salih yapar) |
|---|---|---|---|
| M0 | Mod = hook zinciri: `on(event, matcher, ($, e, next))`, `next` ile bileşim, `$` arayüzü, mod klasör yapısı | *Claude Code Plugins* · *Hooks (middleware chain)* | boş mod klasörü + `claude plugin validate` yeşil |
| M1 | Araç çağrısı kancası: `tool.call` ile engelle / yeniden yaz / sonucu gözle | *Hooks: PreToolUse / PostToolUse* | bir Bash çağrısını reddeden mod |
| M2 | Yüzeyler: status line (`$.ui.status`), toast (`$.ui.toast`), prompt üstü band (`AbovePrompt`) | *Status Line* · *UI Surfaces* | status line'da canlı sayaç |
| M3 | Pane: `$.ui.open`, `ui.render`, durum atomları (`atom`/`read`/`update`), `$.state` sözleşmesi | *Reactive State* · *Panes* | oturum doluluğunu gösteren pane |
| M4 | Slash komutu (`$.command.register` + `command.run`), `prompt.submit`, `prompt.compose` (sistem istemi bölümü) | *Custom Slash Commands* · *System Prompt Sections* | `/komut` yanıt veren mod |
| M5 | Sınama ve paylaşım: `claude plugin test`, tsc, marketplace; sistemde mod fikir yapısı (fikir kutusu → Jarvis devri) | *Plugin Testing & Distribution* | 1 fikir kaydı + devir dosyası |

Kaynaklar: [plugins reference](https://docs.claude.com/en/docs/claude-code/plugins-reference) · [statusline](https://docs.anthropic.com/en/docs/claude-code/statusline) · bu build'in `plugin-authoring` skill'i ve `claude-code.d.ts`.
