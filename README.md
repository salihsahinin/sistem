# friday — Jarvis'in icra ekip-lideri (v0.2, 2026-09-09; Jarvis Karar 91 + EK)

**Friday** = Jarvis'in (`~/jarvis`, Fable ana-oturum) devrettiği proje-ölçekli icra işlerini (çift-atlas araştırma · refactor/taşıma · doküman üretimi · ölçüm koşumları) Sonnet işçi filosuyla yürüten **Opus 5 (effort medium) lider-ajan**. Hafıza mimarisi Jarvis'inkiyle aynı; kuralları Jarvis'te (`kanon/` salt-okur bağ). Jarvis bu repoyu ingest etmez; Friday Jarvis'ten yalnız `kanon/` okur.

## Kuruluş (bir kez)
```bash
cd ~/friday && ln -sfn /Users/HasanSalihSahin/jarvis/core kanon && chmod +x .claude/hooks/*.sh
```
`kanon/` submodule değil sembolik bağ (Jarvis `core/` alt klasör; bağ canlı `core/`yi gösterir, kural değişimi anında yansır; yazma settings deny + hook ile kesilir).

## Koşum döngüsü
1. Jarvis (Fable) `cc/gelen/<devir_id>.json` yazar (şema `core/sablonlar/devir-birimi-v0.json`) + gerekirse envanter dosyası (Friday'in Jarvis'e bakan gözü).
2. Salih bu klasörde Opus 5 medium oturumu açar: "seans başı" → ritüel → devir birimi.
3. Friday koşar (CLAUDE.md · `core/rol.md` · kapsül · desenler); işçiler Sonnet, hakem ayrı çağrı.
4. Çıktı `cc/giden/<devir_id>-geri-donus.md` (+ teslim dosyaları); Jarvis tarafı `cc/devir/`e kopyalar, yerleştirir.
5. Tasarım diyaloğu: Friday `cc/giden/tasarim-*.md` yazar → Salih Fable'a taşır → cevap `cc/gelen/tasarim-*-cevap.md`. İki bağlam birbirini okumaz.

## Hafıza katmanları (Jarvis eşleniği)
| Friday | Jarvis | Kural |
|---|---|---|
| `core/durum-kapsulu.md` | kapsül | sıcak, üzerine yazılır, ≤4 KB/20 satır, FIFO 8 madde → `arsiv/` |
| `core/pano.md` | pano | kartlar = devir birimleri |
| `kuyruk/senaryo-defteri.md` | defter | gelen hükümler + `[oneri]`/`[sapma]`, ≤24 KB |
| `kuyruk/fikir-kutusu.md` | kutu | adaylar, ≤10 KB |
| `core/desenler.md` | wiki/desen tabanı | çekirdek; 10 koşumda yeniden-oluşum; ekleme Salih kabulüyle |
| `veri/bronz/hareket-olay.jsonl` | hareket kütüğü | PostToolUse hook, append-only |
| `arsiv/` | arsiv | silme yok (m.8) |

## Denetim (deterministik)
- Okuma kilidi: `echo '{"tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/jarvis/kuyruk/senaryo-defteri.md"}}' | CLAUDE_PROJECT_DIR=$PWD bash .claude/hooks/okuma-izin.sh; echo exit=$?` → 2 (RED); `kanon/tuzuk-v0.md` → 0.
- Friday neyi okudu: `python3 -c "import json;print(sorted({json.loads(l)['yol'] for l in open('veri/bronz/hareket-olay.jsonl') if json.loads(l)['yol']}))"`.
- Kapsül: `wc -c core/durum-kapsulu.md` ≤ 4096 · `grep -c '^- ' core/durum-kapsulu.md` ≤ 8.
