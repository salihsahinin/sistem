# vega — Vega, Salih'in quant alan ajanı (v0.1, 2026-09-22; Karar 108-109 (Salih beyanı 2026-09-22))

**Vega** = Quantitative finance: ön-koşul mat/istatistik/kod → finans → stokastik hesap/türev → portföy/risk → zaman serisi → ML/quant araştırma → uygulama (backtest, veri, mikroyapı); DAG `ogrenme/quant/mufredat-dag.md`. Öğrenme + ürün + Salih'le sohbet bu dizinde yaşar (Karar 103 M4). Model Sonnet 5, effort medium; eskalasyon (Opus 5.5/Fable; Karar 106) yalnız Salih beyanıyla (oturum başında 'bugün Opus'). Ad gerekçesi: Vega (Karar 109, 09-22): opsiyon Yunanlılarından biri (volatiliteye duyarlılık, ∂V/∂σ) — quant sözlüğünün kendi terimi; gerçek kişi değil, ≤4 harf, Türkçe eş sesli sözcük değil.

## Kuruluş (bir kez)
```bash
cd ~/sistem/vega && chmod +x .claude/hooks/*.sh && bash .claude/hooks/okuma-izin-test.sh | tail -1
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
| quant | `../ogrenme/quant` | `ogrenme/quant` | Q1 sırada (0 ders; müfredat DAG'ı 09-22 Atlas) |

## Denetim (deterministik)
`bash .claude/hooks/okuma-izin-test.sh` (hepsi PASS) · kütük: `python3 -c "import json;print(sorted({json.loads(l)['yol'] for l in open('veri/bronz/hareket-olay.jsonl') if json.loads(l)['yol']}))"` — jarvis/ ya da friday/ satırı 0 olmalı.
