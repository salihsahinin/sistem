# sayi — Sayi, Salih'in hesaplama alan ajanı (v0.1, 2026-09-21; Karar 105 (masa-18, 2026-09-20/21))

**Sayi** = Hesaplama temelleri: MIT 6.006 (algoritmalar, birebir) · MIT 6.042J (bilgisayar bilimi için matematik, birebir + 'neden') · matematik felsefesi (17 partisyon). Öğrenme + ürün + Salih'le sohbet bu dizinde yaşar (Karar 103 M4). Model Sonnet 5, effort medium; eskalasyon (Opus/Fable) yalnız Salih beyanıyla (oturum başında 'bugün Opus'). Ad gerekçesi: Sayi / Öklid (MÖ 3. yy): Elementler (aksiyomatik ispat) + ilk kayıtlı algoritma (ebob) — 6.006 algoritma çözümlemesi + 6.042J ispat teknikleri + matematik felsefesi (aksiyom nedir) tek isimde.

## Kuruluş (bir kez)
```bash
cd ~/sistem/sayi && chmod +x .claude/hooks/*.sh && bash .claude/hooks/okuma-izin-test.sh | tail -1
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
| mit-6006 | `../ogrenme/mit-6006` | `ogrenme/mit-6006` | Ders-1 kaydı; Salih okuma + bulanık blok |
| mit-6042j | `../ogrenme/mit-6042j` | `ogrenme/mit-6042j` | Ders-1 kaydı |
| mat-felsefesi | `../ogrenme/mat-felsefesi` | `ogrenme/mat-felsefesi` | tasarım v1, 0 ders; Salih onayı bekliyor |

## Denetim (deterministik)
`bash .claude/hooks/okuma-izin-test.sh` (hepsi PASS) · kütük: `python3 -c "import json;print(sorted({json.loads(l)['yol'] for l in open('veri/bronz/hareket-olay.jsonl') if json.loads(l)['yol']}))"` — jarvis/ ya da friday/ satırı 0 olmalı.

**Ad (Karar 107, 2026-09-22):** eski ad **Euclid** (Karar 105 EK-2, 09-21 → 09-22); tarihli kayıtlarda eski ad = bu ajan (Karar 93 ad-eşitliği usulü).
