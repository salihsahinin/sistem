# Claude Code modları (kanon kopyası; Salih 2026-10-27, Karar 126; video "Claude Mods" 3 fikir)

Canlı kopya `~/.claude/dev-mods/<oturum-id>/<mod>/` (motor orayı izler, oturum sonunda yükler); bu dizin **kaynak kanonu** ve proof-of-work'tür (görünür klasör, gizli-klasör-yok ilkesi 08-18). Değişiklik: önce burada, sonra canlı klasöre kopya ya da `CLAUDE_CODE_PLUGIN_DIRS=C:\sistem\sistem\jarvis\mods\<mod>` ile doğrudan buradan yükleme. Doğrulama: `claude plugin validate mods/<mod>`.

| Mod | Ne | Araçlar / komut |
|---|---|---|
| `jarvis-oda` (v0.2) | Lobi eşgörevi, lobi MCP kullanmaz: Jarvis (Fable) planlar, görevler zorluğa göre Haiku/Sonnet/Opus işçilerine; **anlık paralel işçi sayısı değişken** (`maksParalel`, panoda −/+, kuyruk); **ortak sohbet** (panodaki giriş alanı: Salih herkese ya da `#N` ile tek işçiye; mesaj işçi bağlamına ve Jarvis'e düşer, işçi `oda_rapor` ile cevaplar); öneri kararı Salih'in (Kabul/Ret). İşçi bitince Jarvis `[oda]` mesajıyla uyanır. | `oda_ac · oda_plan · oda_gorev_ver · oda_ayar · oda_sohbet · oda_oku · oda_oneri_karar · oda_oneri · oda_rapor` · `/oda` · ayar `otoUyandir`, `maksParalel` |
| `jarvis-graf` | Akış grafı paneli: `ortak/akis-graf.json` pane'de SVG (hedef · iş · seans bantları, x = açılış sırası, renk = durum), filtre, düğüm detayı, `HTML aç` (`tools/akis-graf-html.py`), `durum graf` (Rust). 10 sn'de bir dosya değişimini izler. | `/graf` |
