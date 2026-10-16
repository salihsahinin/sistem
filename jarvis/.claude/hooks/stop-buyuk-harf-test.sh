#!/usr/bin/env bash
# stop-buyuk-harf.sh birim testi (5 vaka). Kullanım: bash .claude/hooks/stop-buyuk-harf-test.sh
set -u
H="$(dirname "$0")/stop-buyuk-harf.sh"
T=$(mktemp -d)
T=$(cygpath -m "$T" 2>/dev/null || echo "$T")   # Windows: /tmp/... yolunu yerel programlar (Python, Rust) açamaz → C:/... biçimi
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
vaka "durum #6 kısaltmaları → geç"         gec   "WSL yok, OMP worktree'de, PATH düzeldi; CTE, LSP, NYC."
vaka "3 harfli vurgu (VAR/SANA) → block"    block "Bu SANA yazıldı, kanal VAR."
vaka "durum sözcüğü çıplak (DONE) → block"  block "İş DONE, pratik KALAN."
vaka "kod bloğu içinde caps → geç"         gec   $'Şöyle:\n```\nEXPORT ALL CAPS HERE\n```\nve `INLINE_CAPS` normal.'
vaka "stop_hook_active ikinci tur → geç"   gec   "TEMELDE yine caps var ama ikinci tur." true
vaka "Türkçe karakterli caps → block"      block "Bu adım ZORUNLU ve İLGİSİ yok."
vaka_arac() { # ad · beklenen · araç adı · alan · içerik  (v0.3: araç girdisi taraması)
  n=$((n+1)); local ad="$1" bek="$2" arac="$3" alan="$4" icerik="$5"
  local tp="$T/$n.jsonl"
  printf '%s\n' "$(python3 -c 'import json;print(json.dumps({"type":"user","message":{"content":"soru"}}))')" > "$tp"
  python3 -c 'import json,sys;print(json.dumps({"type":"assistant","message":{"content":[{"type":"tool_use","name":sys.argv[1],"input":{sys.argv[2]:sys.argv[3]}},{"type":"text","text":"Görsel yukarıda."}]}},ensure_ascii=False))' "$arac" "$alan" "$icerik" >> "$tp"
  out=$(printf '{"transcript_path":"%s","stop_hook_active":false,"hook_event_name":"Stop"}' "$tp" | bash "$H")
  if [ "$bek" = block ]; then res=$([ -n "$out" ] && echo block || echo gec); else res=$([ -z "$out" ] && echo gec || echo block); fi
  if [ "$res" = "$bek" ]; then ok=$((ok+1)); echo "  [PASS] $ad"; else echo "  [FAIL] $ad → çıktı: ${out:-<boş>}"; fi
}
vaka_arac "widget JS dizesinde caps → block"  block mcp__visualize__show_widget widget_code '<div class="x"><style>.A{color:red}</style><script>addLog("iki AYRI sunucudan geliyor ama BİRLİKTE bağlı");</script></div>'
vaka_arac "widget yalnız etiket/kısaltma → geç" gec   mcp__visualize__show_widget widget_code '<svg viewBox="0 0 10 10"><text>MCP sunucusu · DAG</text></svg>'
vaka_arac "Write içeriğinde caps → block"      block Write content 'Bu ders TEMELDE şunu anlatır.'
echo "sonuç: $ok/$n"
rm -rf "$T"
[ "$ok" = "$n" ]
