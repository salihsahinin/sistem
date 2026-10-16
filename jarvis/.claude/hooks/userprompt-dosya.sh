#!/usr/bin/env bash
# userprompt-dosya.sh — İB-79 UserPromptSubmit hook (Karar 88 M12 a, Salih 2026-09-09).
# stdin: Claude Code UserPromptSubmit JSON ({prompt, session_id, ...}) → tools/prompt-dosya.py → stdout bağlama eklenir.
# Prompt'u ASLA engellemez (çıkış 0); tablo core/prompt-dosya-tablosu.tsv; kütük veri/bronz/prompt-dosya-olay.jsonl.
# Karar 112 (Salih 2026-10-05, deneysel): aynı stdin ikinci araca da verilir → tools/paket-yonlendir.py (bağlam paketi yönergesi;
# manifest core/baglam-paketleri.json; durum .claude/hooks/state/paket-<oturum>.json; kütük veri/bronz/paket-olay.jsonl).
. "$(dirname "${BASH_SOURCE[0]}")/rust-yonlendir.sh" userprompt   # Rust varsa exec; yoksa aşağısı (durum #1)
KOK="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
GIRDI="$(cat)"
printf '%s' "$GIRDI" | python3 "$KOK/tools/prompt-dosya.py" --repo "$KOK" 2>/dev/null
printf '%s' "$GIRDI" | python3 "$KOK/tools/paket-yonlendir.py" --repo "$KOK" 2>/dev/null
exit 0
