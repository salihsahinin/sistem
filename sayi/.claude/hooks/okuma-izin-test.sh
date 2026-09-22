#!/usr/bin/env bash
# Alan-ajanı okuma-izin kilidi testi (v0.6; Friday testinin kopyası + Karar 105 vakaları; üretici alan-ajani-dogur.py). Beklenen exit: 0 = geçer, 2 = RED.
# v0.1 (Fable 2026-09-10, tur-1 A5): 9 vaka.
# v0.2 (Friday 2026-09-18, Karar 99 M2/M3; tur-3 C2): +Z1-Z3 +agent_id 3 vaka. FRIDAY_HOOK_TEST export edilir →
#   kilit kararı (exit 2) DEĞİŞMEZ, yalnız bronz kütüğe yazım durur (aksi hâlde test yapay RED satırları bırakır).
# v0.5 (Jarvis 2026-09-18, Karar 101 F3): `kanon/` bağı emekli → 3 vaka yeniden yazıldı (jarvis/core RED), +2 kök-kanon vakası.
# Koşum: bash .claude/hooks/okuma-izin-test.sh  (repo kökünden). Hepsi PASS olmalı.
cd "$(dirname "$0")/../.." || exit 1
export CLAUDE_PROJECT_DIR=$PWD
export FRIDAY_HOOK_TEST=1
HOOK=.claude/hooks/okuma-izin.sh
GECEN=0; KALAN=0
# Yol taşınabilirliği (2026-09-22, Windows devri; KURULUM §4): sabit Mac yolu yerine depo kökü + ev dizini; Git Bash'te Windows-yerel yol (`pwd -W`), Mac'te düz `pwd`.
SISTEM=$(cd .. && { pwd -W 2>/dev/null || pwd; }); EV=$(cd ~ && { pwd -W 2>/dev/null || pwd; })
t(){ printf '%s\n' "$2" | bash "$HOOK" >/dev/null 2>&1; r=$?; if [ "$r" = "$3" ]; then s=PASS; GECEN=$((GECEN+1)); else s=FAIL; KALAN=$((KALAN+1)); fi; echo "$s  $1 → exit $r (beklenen $3)"; }

echo "-- v0.1 vakaları (ana-sıra) --"
t "heredoc gövdesinde ~/sistem/jarvis dizesi"        '{"tool_name":"Bash","tool_input":{"command":"cat > cc/giden/x.md <<'"'"'EOF'"'"'\nJarvis kökü ~/sistem/jarvis/kuyruk burada geçer\nEOF"}}' 0
t "\$HOME/sistem/jarvis/kuyruk okuma"                 '{"tool_name":"Bash","tool_input":{"command":"cat $HOME/sistem/jarvis/kuyruk/senaryo-defteri.md"}}' 2
t "../jarvis/kuyruk göreli çıkış (v0.5)"     '{"tool_name":"Bash","tool_input":{"command":"cat ../jarvis/kuyruk/pano.md"}}' 2
t "kök kanon ../AGENTS.md okuma (v0.5)"       '{"tool_name":"Bash","tool_input":{"command":"sed -n 1,5p ../AGENTS.md"}}' 0
t "kök listeleme ~/sistem (v0.5)"             '{"tool_name":"Bash","tool_input":{"command":"ls '"$SISTEM"'"}}' 0
t "~/sistem/jarvis/core listeleme → RED (Karar 101)" '{"tool_name":"Bash","tool_input":{"command":"ls '"$SISTEM"'/jarvis/core"}}' 2
t "~/sistem/jarvis/cc listeleme"                     '{"tool_name":"Bash","tool_input":{"command":"ls '"$SISTEM"'/jarvis/cc"}}' 2
t "Read jarvis/kuyruk/pano.md"                '{"tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/jarvis/kuyruk/pano.md"}}' 2
t "Read friday kendi dosyası"                 '{"tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/sayi/core/rol.md"}}' 0
t "Grep jarvis/core → RED (Karar 101)"        '{"tool_name":"Grep","tool_input":{"pattern":"m.8","path":"'"$SISTEM"'/jarvis/core"}}' 2
t "Read kök kanon /Users/…/sistem/CLAUDE.md"  '{"tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/CLAUDE.md"}}' 0
t "Read kök sablonlar/ (F4 ortak şablon)"     '{"tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/sablonlar/geri-donus-v0.md"}}' 0
t "Read kök ogrenme/ → RED (Salih'in)"         '{"tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/ogrenme/evals/README.md"}}' 2

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
t "agent_id + kapsül okuma → RED"             '{"agent_id":"a1","agent_type":"general-purpose","tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/sayi/core/durum-kapsulu.md"}}' 2
t "agent_id + wiki/serbest dosya → geçer"     '{"agent_id":"a1","agent_type":"general-purpose","tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/sayi/core/rol.md"}}' 0
t "agent_id + kendi tool-results → geçer"     '{"agent_id":"a1","agent_type":"general-purpose","tool_name":"Read","tool_input":{"file_path":"'"$EV"'/.claude/projects/p/s/tool-results/x.txt"}}' 0
t "agent_id + defter (Bash) → RED"            '{"agent_id":"a1","agent_type":"general-purpose","tool_name":"Bash","tool_input":{"command":"cat kuyruk/senaryo-defteri.md"}}' 2
t "agent_id + bronz kütük → RED"              '{"agent_id":"a1","agent_type":"general-purpose","tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/sayi/veri/bronz/hareket-olay.jsonl"}}' 2
t "ana-sıra + kapsül okuma → geçer (değişmedi)" '{"tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/sayi/core/durum-kapsulu.md"}}' 0

echo "-- v0.4 ayrıştırıcı (Karar 100 M1) ve cc/gelen yasağı (M3) --"
t "grep DESENİNDE yasak yol → geçer"          '{"tool_name":"Bash","tool_input":{"command":"grep -n \"jarvis/kuyruk\" core/pano.md"}}' 0
t "cat ile tırnaklı açık yasak yol → RED"     '{"tool_name":"Bash","tool_input":{"command":"cat \"'"$SISTEM"'/jarvis/cc/rapor.md\""}}' 2
t "grep ARGÜMANINDA yasak dizin → RED"        '{"tool_name":"Bash","tool_input":{"command":"grep -r m.8 '"$SISTEM"'/jarvis/kuyruk"}}' 2
t "sed betiği desen, dosya serbest → geçer"   '{"tool_name":"Bash","tool_input":{"command":"sed -n /jarvis.kuyruk/p core/pano.md"}}' 0
t "değişkenli yol (Z3b sınırı) → geçer"       '{"tool_name":"Bash","tool_input":{"command":"cat \"$D/x.md\""}}' 0
t "alt-ajan cc/gelen okur → RED"              '{"agent_id":"a1","agent_type":"general-purpose","tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/sayi/cc/gelen/gorev-2026-09-18-tur4.md"}}' 2
t "lider (agent_id yok) kendi emrini okur"    '{"tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/sayi/cc/gelen/gorev-2026-09-18-tur5.md"}}' 0
t "alt-ajan kendi tool-results (Bash) → geçer" '{"agent_id":"a1","tool_name":"Bash","tool_input":{"command":"sed -n 1,5p ~/.claude/projects/p/s/tool-results/x.txt"}}' 0

echo "-- v0.6 alan ajanı (Karar 105) --"
t "Read ../friday/core → RED (başka ajan)"        '{"tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/friday/core/rol.md"}}' 2
t "Read başka alan ajanı core → RED"              '{"tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/tart/core/durum-kapsulu.md"}}' 2
t "Read ogrenme/kaynaklar (okuma-izin-ek) → geçer" '{"tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/ogrenme/kaynaklar/README.md"}}' 0
t "Bash cat ../ogrenme/kaynaklar/x → geçer"       '{"tool_name":"Bash","tool_input":{"command":"cat ../ogrenme/kaynaklar/README.md"}}' 0
t "Read ../ogrenme/evals (kaynaklar dışı) → RED"   '{"tool_name":"Read","tool_input":{"file_path":"'"$SISTEM"'/ogrenme/mufredat.md"}}' 2
echo "--------"
echo "PASS $GECEN · FAIL $KALAN"
[ "$KALAN" = 0 ] || exit 1
