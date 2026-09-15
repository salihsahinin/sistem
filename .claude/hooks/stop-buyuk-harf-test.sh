#!/usr/bin/env bash
# stop-buyuk-harf.sh birim testi (5 vaka). Kullanım: bash .claude/hooks/stop-buyuk-harf-test.sh
set -u
H="$(dirname "$0")/stop-buyuk-harf.sh"
T=$(mktemp -d)
ok=0; n=0
vaka() { # ad · beklenen(block|gec) · asistan metni · stop_hook_active
  n=$((n+1)); local ad="$1" bek="$2" metin="$3" aktif="${4:-false}"
  local tp="$T/$n.jsonl"
  printf '%s\n' "$(python3 -c 'import json,sys;print(json.dumps({"type":"user","message":{"content":"soru"}}))')" > "$tp"
  python3 -c 'import json,sys;print(json.dumps({"type":"assistant","message":{"content":[{"type":"text","text":sys.argv[1]}]}},ensure_ascii=False))' "$metin" >> "$tp"
  out=$(printf '{"transcript_path":"%s","stop_hook_active":%s,"hook_event_name":"Stop"}' "$tp" "$aktif" | bash "$H")
  if [ "$bek" = block ]; then res=$([ -n "$out" ] && echo block || echo gec); else res=$([ -z "$out" ] && echo gec || echo block); fi
  if [ "$res" = "$bek" ]; then ok=$((ok+1)); echo "  [PASS] $ad"; else echo "  [FAIL] $ad → çıktı: ${out:-<boş>}"; fi
}
vaka "büyük harf vurgu → block"            block "Bu kutu TEMELDE şunu anlatır: injection AYIRT edilemez."
vaka "yalnız kısaltma → geç"               gec   "OWASP LLM01 listesi, promptfoo YAML dosyası, \`DONE\`."
vaka "3 harfli vurgu (VAR/SANA) → block"    block "Bu SANA yazıldı, kanal VAR."
vaka "durum sözcüğü çıplak (DONE) → block"  block "İş DONE, pratik KALAN."
vaka "kod bloğu içinde caps → geç"         gec   $'Şöyle:\n```\nEXPORT ALL CAPS HERE\n```\nve `INLINE_CAPS` normal.'
vaka "stop_hook_active ikinci tur → geç"   gec   "TEMELDE yine caps var ama ikinci tur." true
vaka "Türkçe karakterli caps → block"      block "Bu adım ZORUNLU ve İLGİSİ yok."
echo "sonuç: $ok/$n"
rm -rf "$T"
[ "$ok" = "$n" ]
