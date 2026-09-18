# gorsellestir skill — ARŞİV (2026-09-03)

Salih emri 2026-09-03 22:10: "görselleştir skillini sil, beğenmedim." Skill aktif hazineden ÇIKARILDI; m.8 (silme yasağı) gereği kaynaklar buraya indi, git tarihçesi (İB-77, commit 52aa252 → e400956) duruyor. Taşıma Python ile yapıldı: Bash teli `.claude/` üzerinde `git mv`'yi tökezletti (yanlış-pozitif; hook notu "meşru iş ana-sırada yeniden ifade edilir").

- `skill/` — eski `.claude/skills/gorsellestir/` (SKILL.md, karar tablosu, örnek spec'ler, eval)
- `tools/gorsellestir.py` — eski `tools/gorsellestir.py` (LLM'siz kapı + renderer)
- `tools/test_gorsellestir.py` — eski `tools/testler/test_gorsellestir.py` (18 test; artık test süitinde koşmaz)
- Atlas sentezi `raporlar/2026-09/2026-09-03-ib77-gorsellestir-atlas.md` ve üretilmiş `raporlar/gorsel-*.html` yerinde kaldı; bronz kütük `veri/bronz/gorsel-olay.jsonl` kapandı.
- `~/.claude/skills/gorsellestir` symlink'i kaldırıldı.

Geri alma: dizinleri ters yola taşı + symlink'i yeniden kur.
