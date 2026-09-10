#!/usr/bin/env bash
# Friday okuma-izin kilidi testi (Fable 2026-09-10; tur-1 A5). Beklenen exit: 0 = geçer, 2 = RED.
# Koşum: bash .claude/hooks/okuma-izin-test.sh  (repo kökünden). 9 vaka; hepsi PASS olmalı.
cd "$(dirname "$0")/../.." || exit 1
export CLAUDE_PROJECT_DIR=$PWD
HOOK=.claude/hooks/okuma-izin.sh
t(){ printf '%s\n' "$2" | bash "$HOOK" >/dev/null 2>&1; r=$?; [ "$r" = "$3" ] && s=PASS || s=FAIL; echo "$s  $1 → exit $r (beklenen $3)"; }
t "heredoc gövdesinde ~/jarvis dizesi"        '{"tool_name":"Bash","tool_input":{"command":"cat > cc/giden/x.md <<'"'"'EOF'"'"'\nJarvis kökü ~/jarvis/kuyruk burada geçer\nEOF"}}' 0
t "\$HOME/jarvis/kuyruk okuma"                 '{"tool_name":"Bash","tool_input":{"command":"cat $HOME/jarvis/kuyruk/senaryo-defteri.md"}}' 2
t "kanon/../kuyruk bağ-üstü çıkış"            '{"tool_name":"Bash","tool_input":{"command":"cat kanon/../kuyruk/pano.md"}}' 2
t "kanon/tuzuk-v0.md okuma"                   '{"tool_name":"Bash","tool_input":{"command":"sed -n 1,5p kanon/tuzuk-v0.md"}}' 0
t "~/jarvis/core listeleme"                   '{"tool_name":"Bash","tool_input":{"command":"ls ~/jarvis/core"}}' 0
t "~/jarvis/cc listeleme"                     '{"tool_name":"Bash","tool_input":{"command":"ls ~/jarvis/cc"}}' 2
t "Read jarvis/kuyruk/pano.md"                '{"tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/jarvis/kuyruk/pano.md"}}' 2
t "Read friday kendi dosyası"                 '{"tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/friday/core/rol.md"}}' 0
t "Grep jarvis/core (kanon hedefi)"           '{"tool_name":"Grep","tool_input":{"pattern":"m.8","path":"/Users/HasanSalihSahin/jarvis/core"}}' 0
