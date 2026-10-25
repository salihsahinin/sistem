# Durum Kapsülü — Span (bağlam)

*Her oturumun ilk okuduğu dosya. Sıcak katman: üzerine yazılır, arşiv değildir. Bütçe ≤4 KB / ≤20 satır (birincil, Karar 104 M1); "Şu an" ≤8 madde sigorta; aşımda en eski madde `arsiv/kapsul-YYYY-MM-DD.md`'ye iner ve buraya `kesildi: <madde> → arsiv/…` satırı düşer (silme yok, m.8). Tarihçe `raporlar/` + git log.*

**Güncelleme:** 2026-10-25 (seans 1; 10'da `desenler.md` yeniden-oluşum tetiği). Rapor `raporlar/seans-teslim-2026-10-25-claude-mods.md`.

## Şu an
- Şerit `claude-mods` (emir `ortak/durum-olay.jsonl` id 16): M0 + M1 kavramsal `DONE`, pratik `DONE` Salih beyanıyla (10-19, 10-25); M2-M5 sırada. Jarvis iskeleti yok `[sapma]`, README taslağı izleniyor.
- AS-OF plugin-authoring build 2.1.308 (2026-10-25). Tip dosyası her skill yüklemesinde yeni klasöre yazılır; `okuma-izin.sh` Temp yolunu kapatır, Salih eliyle okur.
- Doğrulanan API: `tool.call` için `e.tool`, `e.command` (Bash), `e.file_path` (Edit); `deny: string`; `$.ui.toast`.
- Zayıf: M0 Kutu 6-7 (spread, `hooks.json`/`plugin.json`); M1 Kutu 3 (`===`), Kutu 5 (`includes` alt-dize).
- Branch `oturum/2026-10-16-span-mods` (04d8c83, ddf14e6 + kapanış commit'i), PR istendi. `veri/` commit dışı.
- Öteki şeritler: `baglam-modelleme` (B0 sırada) · `dersler-2026-07` (arşiv-okuma).

## Sonraki ilk iş
1. M2 (status line, toast, prompt üstü band): `ogrenme/claude-mods/README.md` tablosu; önce `plugin-authoring` yükle, build teyit et.
2. `cc/gelen/` içinde Jarvis iskeleti varsa onu kullan.
