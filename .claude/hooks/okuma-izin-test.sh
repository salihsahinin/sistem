#!/usr/bin/env bash
# Friday okuma-izin kilidi testi. Beklenen exit: 0 = geçer, 2 = RED.
# v0.1 (Fable 2026-09-10, tur-1 A5): 9 vaka.
# v0.2 (Friday 2026-09-18, Karar 99 M2/M3; tur-3 C2): +Z1-Z3 +agent_id 3 vaka. FRIDAY_HOOK_TEST export edilir →
#   kilit kararı (exit 2) DEĞİŞMEZ, yalnız bronz kütüğe yazım durur (aksi hâlde test yapay RED satırları bırakır).
# Koşum: bash .claude/hooks/okuma-izin-test.sh  (repo kökünden). Hepsi PASS olmalı.
cd "$(dirname "$0")/../.." || exit 1
export CLAUDE_PROJECT_DIR=$PWD
export FRIDAY_HOOK_TEST=1
HOOK=.claude/hooks/okuma-izin.sh
GECEN=0; KALAN=0
t(){ printf '%s\n' "$2" | bash "$HOOK" >/dev/null 2>&1; r=$?; if [ "$r" = "$3" ]; then s=PASS; GECEN=$((GECEN+1)); else s=FAIL; KALAN=$((KALAN+1)); fi; echo "$s  $1 → exit $r (beklenen $3)"; }

echo "-- v0.1 vakaları (ana-sıra) --"
t "heredoc gövdesinde ~/jarvis dizesi"        '{"tool_name":"Bash","tool_input":{"command":"cat > cc/giden/x.md <<'"'"'EOF'"'"'\nJarvis kökü ~/jarvis/kuyruk burada geçer\nEOF"}}' 0
t "\$HOME/jarvis/kuyruk okuma"                 '{"tool_name":"Bash","tool_input":{"command":"cat $HOME/jarvis/kuyruk/senaryo-defteri.md"}}' 2
t "kanon/../kuyruk bağ-üstü çıkış"            '{"tool_name":"Bash","tool_input":{"command":"cat kanon/../kuyruk/pano.md"}}' 2
t "kanon/tuzuk-v0.md okuma"                   '{"tool_name":"Bash","tool_input":{"command":"sed -n 1,5p kanon/tuzuk-v0.md"}}' 0
t "~/jarvis/core listeleme"                   '{"tool_name":"Bash","tool_input":{"command":"ls ~/jarvis/core"}}' 0
t "~/jarvis/cc listeleme"                     '{"tool_name":"Bash","tool_input":{"command":"ls ~/jarvis/cc"}}' 2
t "Read jarvis/kuyruk/pano.md"                '{"tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/jarvis/kuyruk/pano.md"}}' 2
t "Read friday kendi dosyası"                 '{"tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/friday/core/rol.md"}}' 0
t "Grep jarvis/core (kanon hedefi)"           '{"tool_name":"Grep","tool_input":{"pattern":"m.8","path":"/Users/HasanSalihSahin/jarvis/core"}}' 0

echo "-- v0.3 onarımları (tur-3 C2: Z1-Z2) --"
t "Z1 Bash ile repo dışı ev yolu (staj)"      '{"tool_name":"Bash","tool_input":{"command":"cat ~/staj/rapor.md"}}' 2
t "Z1b Bash ile sistem yolu serbest"          '{"tool_name":"Bash","tool_input":{"command":"wc -l /usr/share/dict/words"}}' 0
t "Z1c Bash ile harness araç çıktısı serbest" '{"tool_name":"Bash","tool_input":{"command":"sed -n 1,5p ~/.claude/projects/p/s/tool-results/x.txt"}}' 0
t "Z2 cd ev + göreli jarvis yolu"             '{"tool_name":"Bash","tool_input":{"command":"cd ~ && cat jarvis/kuyruk/senaryo-defteri.md"}}' 2
t "Z2b cd repo alt dizini + göreli yol"       '{"tool_name":"Bash","tool_input":{"command":"cd core && cat rol.md"}}' 0
echo "   NOT: Z3 iki alt vakaya ayrıldı — ev kökü metinde görünürse kapanıyor, yol tamamen değişkende kurulursa kapanmıyor (K)."
t "Z3a dize kurgusu, ev kökü metinde"         '{"tool_name":"Bash","tool_input":{"command":"J=jarvis; cat ~/$J/kuyruk/x.md"}}' 2
t "Z3b yolun tamamı değişkende (bilinen sınır)" '{"tool_name":"Bash","tool_input":{"command":"D=$(printf %s /Users/x/jarvis/kuyruk); cat \"$D/x.md\""}}' 0

echo "-- v0.3 alt-ajan dalı (Karar 99 M2) --"
t "agent_id + kapsül okuma → RED"             '{"agent_id":"a1","agent_type":"general-purpose","tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/friday/core/durum-kapsulu.md"}}' 2
t "agent_id + wiki/serbest dosya → geçer"     '{"agent_id":"a1","agent_type":"general-purpose","tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/friday/core/rol.md"}}' 0
t "agent_id + kendi tool-results → geçer"     '{"agent_id":"a1","agent_type":"general-purpose","tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/.claude/projects/p/s/tool-results/x.txt"}}' 0
t "agent_id + defter (Bash) → RED"            '{"agent_id":"a1","agent_type":"general-purpose","tool_name":"Bash","tool_input":{"command":"cat kuyruk/senaryo-defteri.md"}}' 2
t "agent_id + bronz kütük → RED"              '{"agent_id":"a1","agent_type":"general-purpose","tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/friday/veri/bronz/hareket-olay.jsonl"}}' 2
t "ana-sıra + kapsül okuma → geçer (değişmedi)" '{"tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/friday/core/durum-kapsulu.md"}}' 0

echo "--------"
echo "PASS $GECEN · FAIL $KALAN"
[ "$KALAN" = 0 ] || exit 1
