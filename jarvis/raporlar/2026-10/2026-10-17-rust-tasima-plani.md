# Python → Rust taşıma planı, revizyon 6a (Karar 119; 2026-10-17)

Kaynak: `raporlar/2026-10-17-hazir-karsilik-denetimi.md` (hazır karşılık denetimi). Karar 119: hazır karşılığı olan araç Rust'a taşınmaz. Salih 2026-10-17: "6a".
Kural (Karar 117 EK-3 + Karar 118 M2): Rust sürümü aynı CLI ve aynı çıktı; fark testi araç başına bir kez; geçince Python sürümü ve Python'a bağlı fark testi `arsiv/kod/python/`'a iner; skill'lerde "yedek python3" yazılmaz; yeni birim testi yok.

Durum: parti 1 (8 araç) PR #23. Kalan 51 araç: tut 26 · üstüne kur 10 · ? 11 · kullan 4.

## Parti 2 — tut (2201 satır)
| olay | satır | araç |
|---|---|---|
| 4 | 203 | `tools/devir-md2json.py` |
| 4 | 294 | `tools/kod-orani-olcum.py` |
| 4 | 309 | `tools/ambar-tablo.py` |
| 3 | 234 | `tools/anakronizm-denetim.py` |
| 2 | 142 | `tools/bayat-cekim.py` |
| 2 | 1019 | `tools/baglam-tablo.py` |

## Parti 3 — tut (1994 satır)
| olay | satır | araç |
|---|---|---|
| 1 | 141 | `tools/deneyim-tablo.py` |
| 0 | 60 | `tools/silver-saglik-kalibrasyon.py` |
| 0 | 69 | `tools/headless-esleme.py` |
| 0 | 72 | `tools/tuzuk-iz-tarama.py` |
| 0 | 74 | `tools/asof-eval.py` |
| 0 | 86 | `tools/baglam-skill-aday.py` |
| 0 | 99 | `tools/denetci-kalibrasyon.py` |
| 0 | 113 | `tools/erisim-kalibrasyon.py` |
| 0 | 115 | `tools/pointer-kayma.py` |
| 0 | 120 | `tools/kural-envanter.py` |
| 0 | 135 | `tools/ta-triyaj.py` |
| 0 | 137 | `tools/pano-akis.py` |
| 0 | 172 | `tools/d2-eval.py` |
| 0 | 198 | `tools/devir-ani.py` |
| 0 | 200 | `tools/bag-tablo.py` |
| 0 | 203 | `tools/olcum-dortlu.py` |

## Parti 4 — tut (1290 satır)
| olay | satır | araç |
|---|---|---|
| 0 | 206 | `tools/loop-dedektor.py` |
| 0 | 208 | `tools/karantina.py` |
| 0 | 222 | `tools/karar-borcu-tablo.py` |
| 0 | 654 | `tools/pointer-graf.py` |

## Kullan — arşive (çıktı eşitliği kontrolünden sonra) (4 araç, 763 satır)
Hazır karşılık işi tam yapıyor; Jarvis eşitliği bir kez ölçer, sonra Python arşive iner.

| olay | satır | araç | hazır karşılık |
|---|---|---|---|
| 6 | 269 | `tools/kod-envanter.py` | tokei / scc (kod satır sayacı) |
| 2 | 180 | `tools/kosum-maliyeti.py` | `/usage`, statusline `cost`, OTel `claude_code.cost.usage` + `api_request` |
| 0 | 74 | `tools/verify-push.py` | `git fetch` + `git diff origin/main` |
| 0 | 240 | `tools/ambar-parquet.py` | DuckDB `COPY ... TO parquet` |

## Üstüne kur — yeniden tasarım (sırası gelince) (10 araç, 2061 satır)
Hazır olan temel olur; yerel kısım ince katman olarak tasarlanır, mekanik taşıma yapılmaz.

| olay | satır | araç | hazır karşılık |
|---|---|---|---|
| 3 | 200 | `tools/prompt-tablo.py` | OTel `user_prompt` olayı, UserPromptSubmit hook, `/insights` |
| 0 | 91 | `tools/masa-html.py` | Artifact aracı + `lavish` skill |
| 0 | 126 | `tools/sunum-son50.py` | Artifact aracı, `artifact-design` skill |
| 0 | 160 | `tools/tarama-plan-duckdb.py` | DuckDB `EXPLAIN` |
| 0 | 206 | `tools/anahtar-denetim.py` | ripgrep + anahtar kaydı regex'leri |
| 0 | 211 | `tools/anahtar-cascade.py` | sed / rg + kayıt |
| 0 | 217 | `tools/sunum-proof-of-work.py` | Artifact aracı |
| 0 | 229 | `tools/tarama-plan.py` | SQLite `EXPLAIN QUERY PLAN` (yerleşik) |
| 0 | 308 | `tools/erisim-fts.py` | SQLite FTS5 (zaten temel); ripgrep alternatif |
| 0 | 313 | `tools/erisim-vektor.py` | sentence-transformers, DuckDB vss |

## ? — inceleme (11 araç, 1833 satır)
Denetim hüküm veremedi; Jarvis araç başına hazır karşılığı yeniden tarar.

| olay | satır | araç | hazır karşılık |
|---|---|---|---|
| 7 | 72 | `.claude/skills/karar-masasi/scripts/masa-uret-test.py` |  |
| 5 | 182 | `.claude/skills/skill-kapisi/scripts/kapi-denetim.py` |  |
| 4 | 217 | `tools/skill-butce.py` | `/context` skill payını gösterebilir |
| 1 | 63 | `.claude/skills/karar-masasi/scripts/masa-spec-cikar.py` |  |
| 0 | 57 | `tools/yuzey-parmak-izi.py` | `/status`, SessionStart hook girdisi |
| 0 | 92 | `tools/gnhf-izle.py` | `/workflows` ve görev paneli yalnız Claude Code işleri için |
| 0 | 98 | `tools/wiki-baglanti.py` | Obsidian backlinks (kullanımda) |
| 0 | 160 | `tools/obsidian-harita.py` | Obsidian graph view |
| 0 | 275 | `tools/katman-olcum.py` | dbt tests / source freshness |
| 0 | 293 | `tools/kolon-olcum.py` | DuckDB `EXPLAIN ANALYZE`, hyperfine |
| 0 | 324 | `tools/atlas-derle.py` | `/workflows` görünümü + script dosyası `~/.claude/projects/` altında |

---

## Süpersede: ilk plan (2026-10-17, 59 araç × 7 parti; parti 1 dışı süpersede)

> # Python → Rust taşıma planı (Karar 117 EK-3, seçenek 5b; 2026-10-17)
>
> Kaynak: `tools/*.py` + `.claude/skills/*/scripts/*.py`; Rust karşılığı olanlar ve hook gövdeleri (`jarvis-hook` içinde: prompt-dosya, paket-yonlendir) hariç; `tools/testler/` taşınmaz (Python araçla birlikte emekli olur).
> Sıra: son 30 günde araç adının geçtiği hareket olayı (2026-09-17 → 2026-10-17, `veri/bronz/hareket-olay.jsonl`) azalan, eşitlikte küçük dosya önce. Parti ≈ 1.800 satır Python.
> Toplam: 59 araç, 12010 satır, 7 parti.
>
> Kural: her aracın Rust karşılığı aynı CLI ve aynı çıktıyı verir; fark testi araç başına bir kez (`.claude/rules/tools.md`); yeni birim testi yok; skill/ritüel çağrısı Rust'a çevrilir. **Karar 118 M2 (2026-10-17):** fark testi geçince Python sürümü `arsiv/kod/python/`'a iner (başka bir Python aracı onu kütüphane olarak yüklüyorsa, o araç taşınana dek kalır); Python'a bağlı fark testi de arşive iner; skill'lerde "yedek python3" ifadesi yazılmaz. Parti 1 bu kuraldan önce başladı; onun Python'ları ayrı bir PR'da arşive iner (durum #22).
>
> ## Parti 1 (1868 satır)
> | olay | satır | araç |
> |---|---|---|
> | 32 | 188 | `tools/alan-ajani-dogur.py` |
> | 15 | 220 | `tools/katman-hatti.py` |
> | 14 | 194 | `tools/buyuk-harf-temizle.py` |
> | 13 | 108 | `tools/yol-tasi.py` |
> | 13 | 257 | `tools/hareket-tablo.py` |
> | 12 | 93 | `.claude/skills/karar-masasi/scripts/masa-uret.py` |
> | 12 | 642 | `tools/silver-saglik.py` |
> | 9 | 166 | `tools/baglam-seyir.py` |
>
> ## Parti 2 (1980 satır)
> | olay | satır | araç |
> |---|---|---|
> | 7 | 72 | `.claude/skills/karar-masasi/scripts/masa-uret-test.py` |
> | 6 | 269 | `tools/kod-envanter.py` |
> | 5 | 182 | `.claude/skills/skill-kapisi/scripts/kapi-denetim.py` |
> | 4 | 203 | `tools/devir-md2json.py` |
> | 4 | 217 | `tools/skill-butce.py` |
> | 4 | 294 | `tools/kod-orani-olcum.py` |
> | 4 | 309 | `tools/ambar-tablo.py` |
> | 3 | 200 | `tools/prompt-tablo.py` |
> | 3 | 234 | `tools/anakronizm-denetim.py` |
>
> ## Parti 3 (1803 satır)
> | olay | satır | araç |
> |---|---|---|
> | 2 | 142 | `tools/bayat-cekim.py` |
> | 2 | 180 | `tools/kosum-maliyeti.py` |
> | 2 | 1019 | `tools/baglam-tablo.py` |
> | 1 | 63 | `.claude/skills/karar-masasi/scripts/masa-spec-cikar.py` |
> | 1 | 141 | `tools/deneyim-tablo.py` |
> | 0 | 57 | `tools/yuzey-parmak-izi.py` |
> | 0 | 60 | `tools/silver-saglik-kalibrasyon.py` |
> | 0 | 69 | `tools/headless-esleme.py` |
> | 0 | 72 | `tools/tuzuk-iz-tarama.py` |
>
> ## Parti 4 (1852 satır)
> | olay | satır | araç |
> |---|---|---|
> | 0 | 74 | `tools/asof-eval.py` |
> | 0 | 74 | `tools/verify-push.py` |
> | 0 | 86 | `tools/baglam-skill-aday.py` |
> | 0 | 91 | `tools/masa-html.py` |
> | 0 | 92 | `tools/gnhf-izle.py` |
> | 0 | 98 | `tools/wiki-baglanti.py` |
> | 0 | 99 | `tools/denetci-kalibrasyon.py` |
> | 0 | 113 | `tools/erisim-kalibrasyon.py` |
> | 0 | 115 | `tools/pointer-kayma.py` |
> | 0 | 120 | `tools/kural-envanter.py` |
> | 0 | 126 | `tools/sunum-son50.py` |
> | 0 | 135 | `tools/ta-triyaj.py` |
> | 0 | 137 | `tools/pano-akis.py` |
> | 0 | 160 | `tools/obsidian-harita.py` |
> | 0 | 160 | `tools/tarama-plan-duckdb.py` |
> | 0 | 172 | `tools/d2-eval.py` |
>
> ## Parti 5 (1871 satır)
> | olay | satır | araç |
> |---|---|---|
> | 0 | 198 | `tools/devir-ani.py` |
> | 0 | 200 | `tools/bag-tablo.py` |
> | 0 | 203 | `tools/olcum-dortlu.py` |
> | 0 | 206 | `tools/anahtar-denetim.py` |
> | 0 | 206 | `tools/loop-dedektor.py` |
> | 0 | 208 | `tools/karantina.py` |
> | 0 | 211 | `tools/anahtar-cascade.py` |
> | 0 | 217 | `tools/sunum-proof-of-work.py` |
> | 0 | 222 | `tools/karar-borcu-tablo.py` |
>
> ## Parti 6 (1982 satır)
> | olay | satır | araç |
> |---|---|---|
> | 0 | 229 | `tools/tarama-plan.py` |
> | 0 | 240 | `tools/ambar-parquet.py` |
> | 0 | 275 | `tools/katman-olcum.py` |
> | 0 | 293 | `tools/kolon-olcum.py` |
> | 0 | 308 | `tools/erisim-fts.py` |
> | 0 | 313 | `tools/erisim-vektor.py` |
> | 0 | 324 | `tools/atlas-derle.py` |
>
> ## Parti 7 (654 satır)
> | olay | satır | araç |
> |---|---|---|
> | 0 | 654 | `tools/pointer-graf.py` |