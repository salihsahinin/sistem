#!/usr/bin/env bash
# İB-83 alt-ajan okuma kilidi testi (Jarvis 2026-09-10). Beklenen exit: 0 = geçer, 2 = RED. Koşum: bash .claude/hooks/pretool-altajan-okuma-test.sh
cd "$(dirname "$0")/../.." || exit 1
export JARVIS_HOOK_TEST=1   # bronz kütüğe yazma
export CLAUDE_PROJECT_DIR=$PWD
HOOK=.claude/hooks/pretool-altajan-okuma.sh
t(){ printf '%s\n' "$2" | bash "$HOOK" >/dev/null 2>&1; r=$?; [ "$r" = "$3" ] && s=PASS || s=FAIL; echo "$s  $1 → exit $r (beklenen $3)"; }
t "ana-sıra (agent_id yok) kapsül okur"          '{"tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/jarvis/core/durum-kapsulu.md"}}' 0
t "alt-ajan kapsül okur"                          '{"agent_id":"a1","agent_type":"Explore","tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/jarvis/core/durum-kapsulu.md"}}' 2
t "alt-ajan tüzük okur (serbest)"                 '{"agent_id":"a1","agent_type":"Explore","tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/jarvis/core/tuzuk-v0.md"}}' 0
t "alt-ajan transkript okur"                      '{"agent_id":"a1","agent_type":"atlas","tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/.claude/projects/x/y.jsonl"}}' 2
t "alt-ajan Bash cat defter"                      '{"agent_id":"a1","agent_type":"atlas","tool_name":"Bash","tool_input":{"command":"cat kuyruk/senaryo-defteri.md | head"}}' 2
t "alt-ajan Bash ~/friday"                        '{"agent_id":"a1","tool_name":"Bash","tool_input":{"command":"ls ~/friday/cc"}}' 2
t "alt-ajan Bash cc/rapor (serbest)"              '{"agent_id":"a1","tool_name":"Bash","tool_input":{"command":"ls cc/rapor/2026-09"}}' 0
t "alt-ajan Grep wiki (serbest)"                  '{"agent_id":"a1","tool_name":"Grep","tool_input":{"pattern":"m.8","path":"/Users/HasanSalihSahin/jarvis/wiki"}}' 0
t "alt-ajan heredoc gövdesinde kapsül adı"       '{"agent_id":"a1","tool_name":"Bash","tool_input":{"command":"cat > cc/rapor/x.md <<'"'"'EOF'"'"'\nbkz core/durum-kapsulu.md\nEOF"}}' 0
t "alt-ajan kendi tool-results dosyasını okur (09-17 muafiyet)" '{"agent_id":"a1","agent_type":"atlas","tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/.claude/projects/-Users-HasanSalihSahin-jarvis/58141fb3/tool-results/toolu_x.txt"}}' 0
t "bayrak açıkken kilit keser (Karar 100 M2; bayrak yalnız kütüğü kapatır)" '{"agent_id":"a1","agent_type":"atlas","tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/jarvis/core/pano.md"}}' 2
t "alt-ajan cc/devir devir dosyası okur → RED (Karar 100 M3)" '{"agent_id":"a1","agent_type":"atlas","tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/jarvis/cc/devir/friday-2026-09-18-tur4/gorev-2026-09-18-tur4.md"}}' 2
t "alt-ajan Bash cc/gelen listeler → RED (Karar 100 M3)" '{"agent_id":"a1","tool_name":"Bash","tool_input":{"command":"ls cc/gelen/"}}' 2
t "alt-ajan başka oturum transkriptini okur → RED (muafiyet dar)" '{"agent_id":"a1","agent_type":"atlas","tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/.claude/projects/-Users-HasanSalihSahin-jarvis/58141fb3.jsonl"}}' 2
