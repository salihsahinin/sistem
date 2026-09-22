# tart — Tart, Salih'in evals alan ajanı (v0.1, 2026-09-21; Karar 105 (masa-18, 2026-09-20/21))

**Tart** = LLM / ajan değerlendirme mühendisliği (evals): eval seti · deterministik kontroller · LLM-as-judge kalibrasyonu · trajektori · CI regresyon. Öğrenme + ürün + Salih'le sohbet bu dizinde yaşar (Karar 103 M4). Model Sonnet 5, effort medium; eskalasyon (Opus/Fable) yalnız Salih beyanıyla (oturum başında 'bugün Opus'). Ad gerekçesi: Tart (MÖ 6. yy Atina): yasa koyucu ve yargıç — değerlendirme mühendisliği = ölçüt yazmak + yargılamak (rubrik, yargıç kalibrasyonu).

## Kuruluş (bir kez)
```bash
cd ~/sistem/tart && chmod +x .claude/hooks/*.sh && bash .claude/hooks/okuma-izin-test.sh | tail -1
```
Salih bu klasörde Claude Code oturumu açar (worktree kapalı, main): "seans başı" → ritüel; "seans başı, <şerit>" → ders. Ders iskeleti Jarvis'ten `cc/gelen/ders-<hafta>.md` ile gelir.

## Klasör haritası
| Yol | Ne |
|---|---|
| `AGENTS.md` (`CLAUDE.md` symlink) | sözleşme + doğum belgesi (§0b) |
| `core/` | kapsül · pano · desenler |
| `kuyruk/` | senaryo-defteri (gelen hükümler, `[oneri]`/`[sapma]`) · fikir-kutusu |
| `ogrenme/<şerit>/` | README · ilerleme · dersler (Salih eli `git mv` ile `../ogrenme/`'den taşındı) |
| `cc/gelen/` · `cc/giden/` | Jarvis'ten ders iskeleti / devir birimi · Jarvis'e geri-dönüş |
| `raporlar/` | seans teslim raporları · görsel HTML'ler |
| `veri/bronz/hareket-olay.jsonl` | PostToolUse kütük (append-only) |
| `arsiv/` | silme yok (m.8) |
| `.claude/` | settings (deny) · hooks (okuma-izin v0.6 · hareket-kutuk) · skills (seans-acilis · seans-kapanis · `ogren` → `../sablonlar/skills/ogren`) · agents/hakem (alan perspektifli) |

## Şeritler
| Şerit | Kaynak (T3 öncesi) | Hedef | Durum |
|---|---|---|---|
| evals | `../ogrenme/evals` | `ogrenme/evals` | H1-H3 DONE (09-11→14, κ=1,0), H4 açık |

## Denetim (deterministik)
`bash .claude/hooks/okuma-izin-test.sh` (hepsi PASS) · kütük: `python3 -c "import json;print(sorted({json.loads(l)['yol'] for l in open('veri/bronz/hareket-olay.jsonl') if json.loads(l)['yol']}))"` — jarvis/ ya da friday/ satırı 0 olmalı.

**Ad (Karar 107, 2026-09-22):** eski ad **Solon** (Karar 105 EK-2, 09-21 → 09-22); tarihli kayıtlarda eski ad = bu ajan (Karar 93 ad-eşitliği usulü).
