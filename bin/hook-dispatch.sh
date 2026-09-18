#!/usr/bin/env bash
# hook-dispatch.sh — sistem kökü tek hook girişi (Karar 101; F1 taslağı 09-18, F4'te ~/sistem/bin/ altına alındı + çift-koşum freni).
# Mekanizma: harness hangi ayar dosyasını yüklerse yüklesin, bu script oturum cwd'sinden (stdin JSON "cwd", yoksa $PWD)
# ajanı bulur (~/sistem/<ajan>/…) ve o ajanın KENDİ .claude/settings.json'ındaki hooks[<olay>] kayıtlarını, matcher'ı
# tool_name'e uygulayarak, CLAUDE_PROJECT_DIR=<ajan dizini> ile sırayla koşturur (mini hook-koşucu). Ajan hook'ları
# değişmeden çalışır; ajanın kaydı yoksa exit 0. Harness-nötr (yalnız dosya + stdin), backend-nötr.
# Çıkış: herhangi bir ajan hook'u 2 dönerse 2 (stderr aynen), aksi hâlde 0; stdout'lar birleştirilir.
set -u
OLAY="${1:?olay adı gerekli}"
KOK="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
GIRDI="$(cat)"
exec python3 - "$OLAY" "$KOK" "$GIRDI" <<'PY'
import json, os, re, subprocess, sys
olay, kok, girdi = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    g = json.loads(girdi) if girdi.strip() else {}
except json.JSONDecodeError:
    g = {}
cwd = os.path.realpath(g.get("cwd") or os.getcwd())
kok = os.path.realpath(kok)
if not cwd.startswith(kok + os.sep):
    sys.exit(0)
ajan = cwd[len(kok) + 1:].split(os.sep)[0]
ajan_dir = os.path.join(kok, ajan)
# Çift-koşum freni (F4): harness ajanın KENDİ settings.json'ını yüklediyse CLAUDE_PROJECT_DIR = ajan dizinidir ve ajan
# hook'ları zaten doğrudan koşar → dispatcher susar. Kök ayar yüklendiyse CLAUDE_PROJECT_DIR = kök → dispatcher koşturur.
if os.path.realpath(os.environ.get("CLAUDE_PROJECT_DIR", "")) == os.path.realpath(ajan_dir):
    sys.exit(0)
ayar = os.path.join(ajan_dir, ".claude", "settings.json")
if not os.path.isfile(ayar):
    sys.exit(0)
try:
    kayitlar = json.load(open(ayar, encoding="utf-8")).get("hooks", {}).get(olay, [])
except (json.JSONDecodeError, OSError):
    sys.exit(0)
arac = g.get("tool_name", "")
env = dict(os.environ, CLAUDE_PROJECT_DIR=ajan_dir, SISTEM_KOK=kok, SISTEM_AJAN=ajan)
kod = 0
for k in kayitlar:
    m = k.get("matcher", "") or ""
    if m and arac and not re.fullmatch(m, arac):
        continue
    for h in k.get("hooks", []):
        if h.get("type") != "command":
            continue
        r = subprocess.run(["bash", "-c", h["command"]], input=girdi, text=True, capture_output=True, env=env, cwd=ajan_dir)
        sys.stdout.write(r.stdout); sys.stderr.write(r.stderr)
        if r.returncode == 2:
            sys.exit(2)
        kod = kod or r.returncode
sys.exit(kod)
PY
