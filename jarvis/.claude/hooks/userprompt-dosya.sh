#!/usr/bin/env bash
# userprompt-dosya.sh — İB-79 UserPromptSubmit hook (Karar 88 M12 a, Salih 2026-09-09).
# stdin: Claude Code UserPromptSubmit JSON ({prompt, session_id, ...}) → tools/prompt-dosya.py → stdout bağlama eklenir.
# Prompt'u ASLA engellemez (çıkış 0); tablo core/prompt-dosya-tablosu.tsv; kütük veri/bronz/prompt-dosya-olay.jsonl.
# Karar 112 (Salih 2026-10-05, deneysel): aynı stdin ikinci araca da verilir → tools/paket-yonlendir.py (bağlam paketi yönergesi;
# manifest core/baglam-paketleri.json; durum .claude/hooks/state/paket-<oturum>.json; kütük veri/bronz/paket-olay.jsonl).
. "$(dirname "${BASH_SOURCE[0]}")/rust-yonlendir.sh" userprompt   # Rust varsa exec; yoksa aşağısı (durum #1)
# Karar 118 M2 (Salih 2026-10-17; icra 2026-10-30): Python gövdesi arsiv/kod/python/hooks/userprompt-dosya.sh'a indi (m.8: taşındı, silinmedi).
# Buraya düşüldüyse jarvis-hook ikilisi yok (ya da JARVIS_HOOK_PYTHON=1): uyarı ver, hiçbir şeyi engelleme, sessiz çık.
cat > /dev/null
echo "jarvis-hook yok (userprompt): önce cargo build --release -p jarvis-hook (Karar 118 M2; eski Python gövdesi arsiv/kod/python/hooks/userprompt-dosya.sh)" >&2
exit 0
