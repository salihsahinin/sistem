#!/usr/bin/env bash
# TALİMAT-YÜKLEME KÜTÜĞÜ — InstructionsLoaded hook (deneysel m.29; kurulum 2026-09-15, Karar 96 M4).
# Amaç: hangi CLAUDE.md / .claude/rules dosyasının hangi seansta, hangi nedenle (session_start ·
# nested_traversal · path_glob_match · include · compact) bağlama yüklendiğini deterministik kütüklemek.
# Kullanım: bağlam-izleme (İB-81 ön-koşulu; Salih 09-10: "bağlama neyin girdiğini yalnız model bilir")
# + S-kaynak madenciliğinin okunma ayağı (tools/baglam-skill-aday.py) + üç-yuva davranış ölçümü.
# Ham girdi olduğu gibi saklanır (alan şeması belgede tam değil; ilk seanslardan sonra şema çıkarılır).
# Hiçbir şeyi engellemez; çıkış 0. Kütük: veri/bronz/talimat-yukleme-olay.jsonl (ekleme-esaslı).
input=$(cat)
PY=$(command -v python3 || command -v python)
GIRDI=$(mktemp); printf '%s' "$input" > "$GIRDI"; trap 'rm -f "$GIRDI"' EXIT
KOK="$(cd "$(dirname "$0")/../.." && pwd)"
"${PY:-python3}" - "$GIRDI" "$KOK" <<'EOF'
import sys, json, pathlib, datetime
girdi, kok = sys.argv[1], sys.argv[2]
try:
    d = json.load(open(girdi))
except Exception:
    d = {"ham": open(girdi, errors="ignore").read()[:2000]}
kayit = {
    "ts_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
    "session_id": d.get("session_id"),
    "olay": d.get("hook_event_name", "InstructionsLoaded"),
    "neden": d.get("load_reason") or d.get("reason") or d.get("matcher"),
    "dosya": d.get("file_path") or d.get("path") or d.get("file"),
    "cwd": d.get("cwd"),
    "ham_alanlar": sorted(k for k in d.keys()),
}
yol = pathlib.Path(kok) / "veri" / "bronz" / "talimat-yukleme-olay.jsonl"
yol.parent.mkdir(parents=True, exist_ok=True)
with open(yol, "a", encoding="utf-8") as f:
    f.write(json.dumps(kayit, ensure_ascii=False) + "\n")
EOF
exit 0
