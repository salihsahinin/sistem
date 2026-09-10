#!/usr/bin/env bash
# HAREKET KÜTÜĞÜ — PostToolUse hook (tüm araçlar). Her araç çağrısı tek JSONL satırı olarak veri/bronz/hareket-olay.jsonl'e düşer
# (append-only; Jarvis hareket kütüğünün eşleniği). Denetim sorusu: "Friday hangi yolları okudu/yazdı?" → bu dosya + Jarvis kütüğü çapraz okunur.
# Alanlar: ts · oturum · arac · yol · komut (Bash, ilk 160 karakter) · hata.
# v0.2 (2026-09-10, Friday tur-1 A4 düzeltmesi): Bash çağrısında `yol` boş kalmıyordu artık — komut metninden yol-benzeri
#   belirteçler (içinde "/" olan ya da bilinen uzantıyla biten) ";" ile birleşik yazılır; heredoc gövdesi (<<EOF … EOF) TARANMAZ
#   (gövde dosya içeriğidir, okuma değildir). Bu sayede seans-kapanis md.7 denetimi Bash okumalarını da görür.
input=$(cat)
PY=$(command -v python3 || command -v python)
[ -z "$PY" ] && exit 0
REPO="${CLAUDE_PROJECT_DIR:-$PWD}"
INPUT="$input" REPO="$REPO" "$PY" - <<'EOF'
import json, os, re, sys, datetime
try:
    g = json.loads(os.environ.get("INPUT") or "{}")
except Exception:
    sys.exit(0)
ti = g.get("tool_input", {}) or {}
arac = g.get("tool_name", "")
yol = ti.get("file_path") or ti.get("path") or ti.get("pattern") or ""
kom_tam = ti.get("command") or ""
if arac == "Bash" and not yol:
    govde_siz = re.sub(r"<<-?\s*['\"]?(\w+)['\"]?.*?\n\1\s*$", "<<HEREDOC>>", kom_tam, flags=re.S | re.M)
    UZ = r"(?:md|json|jsonl|py|sh|txt|html|csv|sqlite|yaml|yml)"
    adaylar = re.findall(r"(?<![\w@:])(?:~|\$HOME|\.{0,2})?/?[\w.\-~$]+(?:/[\w.\-]+)+/?|\b[\w.\-]+\." + UZ + r"\b", govde_siz)
    temiz = []
    for a in adaylar:
        if a.startswith(("http", "//")) or re.fullmatch(r"[\d./-]+", a):  # URL ya da sayı/tarih
            continue
        if a not in temiz:
            temiz.append(a)
    yol = ";".join(temiz[:20])
tr = g.get("tool_response")
satir = {"ts": datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(timespec="seconds"),
         "oturum": (g.get("session_id") or "")[:36], "arac": arac, "yol": yol, "komut": kom_tam[:160],
         "hata": bool(tr.get("error")) if isinstance(tr, dict) else False}
d = os.path.join(os.environ["REPO"], "veri", "bronz"); os.makedirs(d, exist_ok=True)
with open(os.path.join(d, "hareket-olay.jsonl"), "a", encoding="utf-8") as f:
    f.write(json.dumps(satir, ensure_ascii=False) + "\n")
EOF
exit 0
