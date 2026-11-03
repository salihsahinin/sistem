# Claude Code modları (kanon kopyası; Salih 2026-10-27, Karar 126; video "Claude Mods" 3 fikir)

Canlı kopya `~/.claude/dev-mods/<oturum-id>/<mod>/` (motor orayı izler, oturum sonunda yükler); bu dizin **kaynak kanonu** ve proof-of-work'tür (görünür klasör, gizli-klasör-yok ilkesi 08-18). Değişiklik: önce burada, sonra canlı klasöre kopya ya da `CLAUDE_CODE_PLUGIN_DIRS=C:\sistem\sistem\jarvis\mods\<mod>` ile doğrudan buradan yükleme. Doğrulama: `claude plugin validate mods/<mod>` (manifest + modül taraması) ve `claude plugin test mods/<mod>` (bellek-içi motorda `tests/*.test.tsx`). Her modun kaynağı katmanlıdır: `hooks/register.tsx` yalnız kayıt, mantık `hooks/src/`; mimari tablosu modun README'sinde.

| Mod | Ne | Araçlar / komut |
|---|---|---|
| `jarvis-oda` (v0.6) | Oda modu: Jarvis (Fable) planlar, görevler iş nodu olarak açılır ve zorluğa göre Haiku/Sonnet/Opus işçilerinde koşar. v0.5: işçiye tıkla → işçi transkripti, kaydırılabilir sohbet/akış, katlanır bölümler, `[#N · başlık · sınıf]` etiketleri; iş nodu sınıfı (`izole · dosyali · planli · rol`) + bütçe + yazma kapısı; görev durum kütüğüne iş olarak yazılır, akış grafına köprü; oda `ortak/oda/<id>.json`'a dışa yazılır. v0.6: kalıcı dış oturumlar dosyayla katılır (`ortak/oda/<id>/gelen-<oturum>.jsonl`, `giden.jsonl`). | `oda_ac · oda_plan · oda_gorev_ver · oda_ayar · oda_sohbet · oda_oku · oda_oneri_karar · oda_oneri · oda_rapor · oda_katil · oda_mesaj` · `/oda` · ayar `otoUyandir`, `maksParalel`, `durumKaydi`, `alan` |
| `jarvis-graf` (v0.2) | Akış grafı paneli: `ortak/akis-graf.json` pane'de SVG; satır = seans (üstte hedef şeridi, kaydı olmayan oturumlar sanal satır), x = gün sütunları, numaralı düğümler, renk = durum. Altında tıklanabilir seans ızgarası; detayda kütük olayları, yönlü bağlar, karar paragrafı. `HTML aç` (`py -3`, Start-Process; aç · kopyala · Explorer), `durum graf` (Rust), oda köprüsü (`ortak/graf-secim.json`). 10 sn'de bir dosya değişimini izler. | `/graf [is:<id>]` |

## Kurulum (Salih 2026-10-27, Ö1 kabul)

Her yeni oturumda kanon kopyasından yüklenmesi için `~/.claude/settings.json` içinde (masaüstü uygulaması bayrak almaz; yazıldı 2026-10-27):

```json
"env": { "CLAUDE_CODE_PLUGIN_DIRS": "C:\sistem\sistem\jarvis\mods\jarvis-oda;C:\sistem\sistem\jarvis\mods\jarvis-graf" }
```

Terminalde tek oturumluk: `claude --plugin-dir C:\sistem\sistem\jarvis\mods\jarvis-oda --plugin-dir C:\sistem\sistem\jarvis\mods\jarvis-graf`. Yeni mod eklenince bu değişkene `;` ile yol eklenir. Not: bu oturum (5fcbb2ab) modları `~/.claude/dev-mods` kopyasından yükler; env yolu sonraki oturumlarda devreye girer, aynı ad iki yerden yüklenirse çakışma uyarısı transkriptte görünür.
