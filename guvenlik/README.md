# guvenlik — Kerckhoffs, Salih'in guvenlik alan ajanı (v0.1, 2026-09-21; Karar 105 (masa-18, 2026-09-20/21))

**Kerckhoffs** = Ajan güvenliği (AI Agent Security): prompt injection · lethal trifecta / en-az-yetki · MCP tedarik zinciri · hafıza zehirleme · guardrail · red teaming. Öğrenme + ürün + Salih'le sohbet bu dizinde yaşar (Karar 103 M4). Model Sonnet 5, effort medium; eskalasyon (Opus/Fable) yalnız Salih beyanıyla (oturum başında 'bugün Opus'). Ad gerekçesi: Auguste Kerckhoffs, 'La cryptographie militaire' (1883): sistem gizli olmasa da güvenli kalmalı, sır yalnız anahtarda — depo açık-kaynak ilkesi + `.secrets/` sınırıyla (md.49) birebir aynı tasarım ilkesi.

## Kuruluş (bir kez)
```bash
cd ~/sistem/guvenlik && chmod +x .claude/hooks/*.sh && bash .claude/hooks/okuma-izin-test.sh | tail -1
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
| guvenlik | `../ogrenme/guvenlik` | `ogrenme/guvenlik` | G1 DONE (kavramsal+pratik), G2 kavramsal DONE, G3 DONE; G4 sırada |

## Denetim (deterministik)
`bash .claude/hooks/okuma-izin-test.sh` (hepsi PASS) · kütük: `python3 -c "import json;print(sorted({json.loads(l)['yol'] for l in open('veri/bronz/hareket-olay.jsonl') if json.loads(l)['yol']}))"` — jarvis/ ya da friday/ satırı 0 olmalı.
