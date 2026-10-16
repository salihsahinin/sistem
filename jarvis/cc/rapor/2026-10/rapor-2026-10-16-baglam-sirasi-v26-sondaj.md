# V26 sondaj tablosu: bağlam sırası atlas koşumu (durum #18, 2026-10-16)

Kural: ajan başına son üçlükten ≥1 kaynak iddiası + tüm sayısal iddialar (örneklenen) + son üçlükten ≥1 URL'siz iddia. Sondajı orkestratör (Jarvis ana-sıra) yaptı; sentez ve hakemlik ayrı.

| # | Rapor | İddia | Sondaj yöntemi | Sonuç |
|---|---|---|---|---|
| S1 | A-tez | Lean taslağı (`chain_L`, `Ls_eq_flatten_map`) Mathlib'siz derlenir | yerel `lake env lean` (Lean 4.35.0) | tuttu, hatasız |
| S2 | A-tez, B-tez | "maximum depth of four hops" | iki bağımsız antitez ajanı aynı ham cümleyi alıntıladı | tuttu |
| S3 | B-tez (URL'siz, ölçüm) | `.lean` içe aktarılmaz, `.md`/`.txt` içe aktarılır | yerel deney 2: ham API isteği yakalandı (yerel dinleyici, `ANTHROPIC_BASE_URL`) | tuttu: `.lean.md` symlink'li sırada `bas01, lean02, txt03, son04, ic06, orta05` |
| S4 | B-antitez T1 | belge: `@AGENTS.md` üstteyse "imported file first, then the rest" | yerel deney 3: `CLAUDE.md` = `@ust.md` + gövde; ham API isteği | belge davranışı tutmadı: istek sırası `govde01, ust02` (ebeveyn önce). 2.1.302'de içe aktarma, konumundan bağımsız olarak ebeveynden sonra gelir |
| S5 | C-tez | LiM GPT-3.5 75.8/53.8/63.2, closed-book 56.1 | C-antitez PDF metninden bağımsız okudu | tuttu |
| S6 | C-tez | IFScale claude-3.7-sonnet 100/94.8/72.9/52.7; en iyi 68 | C-antitez HTML'den okudu | tuttu (en iyi 68.9) |
| S7 | C-antitez T7 | claude-code issue #63786 vb. hook aşımı | sayfalar açılmadı (ajan beyanı) | sondaj yapılmadı → K |
| S8 | B-antitez T8 | Cedar FSE 2024 "4 hata kanıtla, 21 DRT+PBT" | makale açılmadı (ajan beyanı) | K |
| S9 | depo | `core.symlinks` | `git config core.symlinks` | `true`; `CLAUDE.md` ve `jarvis/CLAUDE.md` mod 120000 |

Ham istekler: oturum scratchpad'i `istek.jsonl` (geçici; yetki başlıkları kaydedilmedi, yalnız gövde).
