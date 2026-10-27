---
name: project-claude-modlari-oda-graf
description: "2026-10-27 iki Claude Code modu kuruldu — jarvis-oda (lobi eşgörevi, Fable planlar / Haiku-Sonnet-Opus uygular) ve jarvis-graf (akış grafı paneli); kanon kopyası jarvis/mods, canlı ~/.claude/dev-mods; sonraki adım Salih kullanımıyla iterasyon"
metadata:
  node_type: memory
  type: project
  originSessionId: 5fcbb2ab-34fa-448c-8233-031f1fab19f3
  modified: 2026-10-27T12:28:50.430Z
---

2026-10-27: Salih'in video ("Claude Mods", 3 fikir) analizi sonrası iki mod yazıldı, `claude plugin validate` + tsc temiz.
- `jarvis-oda`: araçlar `oda_ac · oda_plan · oda_gorev_ver(zorluk kolay→haiku, orta→sonnet, zor→opus) · oda_oku · oda_oneri_karar · oda_oneri · oda_rapor`, `/oda` paneli, işçi bitince `[oda]` prompt'uyla Jarvis uyanır, öneri kararı panodan Salih'in (Kabul/Ret).
- `jarvis-graf`: `/graf` paneli, `ortak/akis-graf.json` SVG (hedef · iş · seans bantları), HTML aç (`tools/akis-graf-html.py`), `durum graf` yenile.
- Konum: kanon `C:\sistem\sistem\jarvis\mods\<mod>`, canlı `C:\Users\sasah\.claude\dev-mods\5fcbb2ab-34fa-448c-8233-031f1fab19f3\<mod>` (motor bu klasörü izler; başka oturumda `CLAUDE_CODE_PLUGIN_DIRS` ile kanon kopyası yüklenebilir).

**Why:** Salih lobi MCP'sinin yerel, çok-ajanlı karşılığını ve graf arayüzünü Jarvis içinde istiyor; ikisi de itere edilecek.

**How to apply:** Çok-ajanlı iş gelince önce `oda_ac` + `oda_plan`, görevleri paralel `oda_gorev_ver`; graf sorusu gelince `/graf`. Mod değişikliği: önce `mods/`, sonra canlı klasöre kopya; doğrulama `claude plugin validate`. İlgili: [[feedback-siber-guvenlik-yok-otomasyon-odagi]], [[project-graf-icinde-graf-karar-125]].
