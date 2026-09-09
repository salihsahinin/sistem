#!/usr/bin/env bash
# userprompt-dosya.sh — İB-79 UserPromptSubmit hook (Karar 88 M12 a, Salih 2026-09-09).
# stdin: Claude Code UserPromptSubmit JSON ({prompt, session_id, ...}) → tools/prompt-dosya.py → stdout bağlama eklenir.
# Prompt'u ASLA engellemez (çıkış 0); tablo core/prompt-dosya-tablosu.tsv; kütük veri/bronz/prompt-dosya-olay.jsonl.
KOK="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
python3 "$KOK/tools/prompt-dosya.py" --repo "$KOK" 2>/dev/null
exit 0
