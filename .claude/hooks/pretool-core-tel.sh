#!/usr/bin/env bash
# core/-Bash TELİ — PreToolUse hook (deneysel m.29; kurulum 2026-07-23, A2 kapanış eki)
# Amaç: canary'nin kanıtladığı deliği kapatmak — settings-deny yalnız Edit/Write tutar,
# Bash ile core/ + CLAUDE.md + .claude/ yazımı serbestti. Bu bir TÖKEZLEME-TELİ, sınır değil
# (kabuk-taşıyan ajan zaptedilemez — kapsül güvenlik notu 07-22); kaçırdığı desen olabilir,
# yanlış-pozitifte mesajı gör ve komutu yeniden ifade et. Gerekçe: raporlar/vardiya-teslim-2026-07-22-aksam.md
input=$(cat)
cmd=$(printf '%s' "$input" | python -c "import sys,json;print(json.load(sys.stdin).get('tool_input',{}).get('command',''))" 2>/dev/null)
[ -z "$cmd" ] && cmd="$input"
PROT='(core/|CLAUDE\.md|\.claude/)'
block=0
printf '%s' "$cmd" | grep -qE ">{1,2}[[:space:]]*\"?\.?/?(core/|CLAUDE\.md|\.claude/)" && block=1
printf '%s' "$cmd" | grep -qE "\b(mv|cp|rm|touch|truncate|tee|dd|install)\b.*${PROT}" && block=1
printf '%s' "$cmd" | grep -qE "\b(sed|perl)\b.*-i.*${PROT}" && block=1
printf '%s' "$cmd" | grep -qE "\bgit[[:space:]]+(checkout|restore|reset|clean|rm|mv)\b.*${PROT}" && block=1
if [ "$block" = "1" ]; then
  echo "TEL (m.41 kilit): Bash ile core/ · CLAUDE.md · .claude/ yazımı bu yüzeyde engellidir. Bu bir tökezleme-telidir; iş meşruysa ana-sıra(Cowork/Fable) ya da Salih eliyle yapılır. Komut: $cmd" >&2
  exit 2
fi
exit 0
