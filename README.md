# ekip-lideri — Jarvis'in lider-ajan reposu (v0.1, 2026-09-09; Jarvis Karar 91)

Ne: Jarvis (`~/jarvis`) Fable ana-oturumunun bağlamı büyüdüğünde görev paketini devralan **Opus 5 (medium) lider-ajanın** kendi reposu. Hafızası burada, kuralları Jarvis'te (`kanon/` salt-okur bağ). Jarvis bu repoyu ingest etmez; bu repo Jarvis'ten yalnız `kanon/` okur.

## Kuruluş (bir kez)
```bash
cd ~/ekip-lideri && ln -s /Users/HasanSalihSahin/jarvis/core kanon && chmod +x .claude/hooks/*.sh
```
`kanon/` submodule DEĞİL, sembolik bağ: Jarvis `core/` bir alt klasör olduğu için submodule tek başına alınamaz; bağ her zaman Jarvis'in canlı `core/`sini gösterir (kural değişimi anında yansır). Yazma `.claude/settings.json` deny + hook ile kesilir.

## Koşum
1. Jarvis (Fable) `gelen/<devir_id>.json` yazar (şema `semalar/devir-birimi-v0.json`).
2. Salih bu klasörde Opus 5 medium oturumu açar: "gelen/<devir_id>.json'u devral".
3. Lider `ROL.md` + `CLAUDE.md` + devir birimi + `hafiza/` ile koşar; işçiler Sonnet.
4. Çıktı `giden/<devir_id>-geri-donus.md` (şema `semalar/geri-donus-v0.md`); Jarvis tarafı bunu `cc/devir/`e kopyalar ve işler.

## Denetim (deterministik)
- Lider neyi okudu? `python3 -c "import json;print(sorted({json.loads(l)['yol'] for l in open('hareket/olay.jsonl') if json.loads(l)['yol']}))"` → hepsi bu repo ya da `kanon/` altında olmalı.
- Okuma kilidi testi: `echo '{"tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/jarvis/kuyruk/senaryo-defteri.md"}}' | bash .claude/hooks/okuma-izin.sh; echo exit=$?` → 2 (RED). `kanon/tuzuk-v0.md` → 0.
- Sıcak hafıza bütçesi: `grep -c '^- ' hafiza/sicak.md` ≤ 20.

## Klasörler
`ROL.md` · `CLAUDE.md` · `kanon/` (bağ) · `gelen/` `giden/` · `hafiza/` (sicak · cekirdek · arsiv/) · `semalar/` · `hareket/` · `.claude/` (hooks + settings)
