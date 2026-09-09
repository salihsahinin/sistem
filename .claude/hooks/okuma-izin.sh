#!/usr/bin/env bash
# OKUMA-İZİN KİLİDİ — PreToolUse hook (Read · Grep · Glob · Bash). Jarvis Karar 91 (2026-09-09): lider reposu Jarvis'ten YALNIZ
# `kanon/` bağını (= ~/jarvis/core, salt-okur) okur; başka hiçbir Jarvis yolu (kuyruk/, cc/, raporlar/, veri/, hafıza…) bağlama giremez.
# Mekanizma: izinli kökler = bu repo + kanon hedefi + geçici dizinler; dışı → exit 2 (çağrı engellenir, gerekçe stderr'e).
# Bu bir KİLİTTİR (prompt cümlesi değil); kaçırdığı desen olursa hareket/olay.jsonl kanıtıyla sonradan görülür.
input=$(cat)
PY=$(command -v python3 || command -v python)
[ -z "$PY" ] && exit 0
REPO="${CLAUDE_PROJECT_DIR:-$PWD}"
INPUT="$input" REPO="$REPO" "$PY" - <<'EOF'
import json, os, re, sys
try:
    g = json.loads(os.environ.get("INPUT") or "{}")
except Exception:
    sys.exit(0)
arac = g.get("tool_name", ""); ti = g.get("tool_input", {}) or {}
repo = os.path.realpath(os.environ["REPO"])
kanon_hedef = os.path.realpath(os.path.join(repo, "kanon")) if os.path.exists(os.path.join(repo, "kanon")) else None
izinli = [repo] + ([kanon_hedef] if kanon_hedef else []) + ["/tmp", "/private/tmp", "/private/var/folders"]
JARVIS = "/Users/HasanSalihSahin/jarvis"
def izinli_mi(yol):
    if not yol or not os.path.isabs(yol):
        return True  # göreli yol = repo içi
    r = os.path.realpath(yol)
    return any(r == k or r.startswith(k + os.sep) for k in izinli)
adaylar = []
if arac in ("Read", "Grep", "Glob"):
    adaylar = [ti.get("file_path"), ti.get("path")]
elif arac == "Bash":
    cmd = ti.get("command", "")
    # Jarvis kökünü anan her yol: yalnız /core altı serbest
    for m in re.finditer(re.escape(JARVIS) + r"(/[^\s'\"`;|&)]*)?", cmd):
        adaylar.append(JARVIS + (m.group(1) or ""))
    for m in re.finditer(r"~/jarvis(/[^\s'\"`;|&)]*)?", cmd):
        adaylar.append(JARVIS + (m.group(1) or ""))
kotu = [a for a in adaylar if a and not izinli_mi(a)]
if kotu:
    sys.stderr.write("OKUMA-İZİN KİLİDİ (Karar 91): lider reposu Jarvis'ten yalnız kanon/ (core) okur. Reddedilen yol: %s\n" % ", ".join(kotu))
    sys.exit(2)
sys.exit(0)
EOF
