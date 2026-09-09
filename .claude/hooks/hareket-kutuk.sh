#!/usr/bin/env bash
# HAREKET KÜTÜĞÜ — PostToolUse hook (tüm araçlar). Her araç çağrısı tek JSONL satırı olarak veri/bronz/hareket-olay.jsonl'e düşer
# (append-only; Jarvis hareket kütüğünün eşleniği). Denetim sorusu: "Friday hangi yolları okudu/yazdı?" → bu dosya + Jarvis kütüğü çapraz okunur.
# Alanlar: ts · oturum · arac · yol (Read/Edit/Write/Grep/Glob) ya da komut özeti (Bash, ilk 160 karakter) · hata (varsa).
input=$(cat)
PY=$(command -v python3 || command -v python)
[ -z "$PY" ] && exit 0
REPO="${CLAUDE_PROJECT_DIR:-$PWD}"
INPUT="$input" REPO="$REPO" "$PY" - <<'EOF'
import json, os, sys, datetime
try:
    g = json.loads(os.environ.get("INPUT") or "{}")
except Exception:
    sys.exit(0)
ti = g.get("tool_input", {}) or {}
yol = ti.get("file_path") or ti.get("path") or ti.get("pattern") or ""
kom = (ti.get("command") or "")[:160]
tr = g.get("tool_response")
satir = {"ts": datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(timespec="seconds"),
         "oturum": (g.get("session_id") or "")[:36], "arac": g.get("tool_name", ""), "yol": yol, "komut": kom,
         "hata": bool(tr.get("error")) if isinstance(tr, dict) else False}
d = os.path.join(os.environ["REPO"], "veri", "bronz"); os.makedirs(d, exist_ok=True)
with open(os.path.join(d, "hareket-olay.jsonl"), "a", encoding="utf-8") as f:
    f.write(json.dumps(satir, ensure_ascii=False) + "\n")
EOF
exit 0
