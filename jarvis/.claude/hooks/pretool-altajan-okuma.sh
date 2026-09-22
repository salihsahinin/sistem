#!/usr/bin/env bash
# ALT-AJAN OKUMA KİLİDİ — PreToolUse hook (Read · Grep · Glob · Bash). İB-83 (Karar 92 M7-1, Salih 2026-09-10: "jarvisin alt ajanı
# çalıştırırken de kendi içerisindeki diğer context windowu okuma kabiliyetini kısıtlarız"). Kaynak: Friday tur-2 S3 — hook girdisinde
# `agent_id` "Present only when the hook fires inside a subagent call" (code.claude.com/docs/en/hooks, AS-OF 2026-09-10).
# Mekanizma: agent_id VARSA (= alt-ajan) → "başka bağlam pencereleri" listesi RED (exit 2): oturum transkriptleri (~/.claude/projects/**),
# Jarvis'in sıcak hafızası (kapsül · pano · defter · fikir kutusu · MEMORY), hareket/bağlam kütükleri (veri/bronz/*olay.jsonl), Friday reposu,
# staj/galeri dış projeler (md.49). Ana-sıra (agent_id yok) etkilenmez. Her RED bronz olaya düşer: veri/bronz/altajan-okuma-olay.jsonl.
# Emrin `baglam` listesi bir gün hook'a ulaşırsa (ortam değişkeni / .aktif-emir dosyası) izin-listesi moduna geçilir; v0 = yasak-listesi.
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
if not g.get("agent_id"):
    sys.exit(0)  # ana-sıra çağrısı
arac = g.get("tool_name", ""); ti = g.get("tool_input", {}) or {}
repo = os.path.realpath(os.environ["REPO"]); home = os.path.expanduser("~")
kok = os.path.dirname(repo)  # monorepo kökü (Karar 101): friday = jarvis'in kardeş dizini; ev yolundan bağımsız (2026-09-22 Windows taşınabilirliği)
YASAK = [os.path.join(home, ".claude", "projects"), os.path.join(kok, "friday"), os.path.join(home, "staj başlangıç"),
         os.path.join(home, "Desktop", "repo"),
         os.path.join(repo, "core", "durum-kapsulu.md"), os.path.join(repo, "core", "pano.md"),
         os.path.join(repo, "kuyruk", "senaryo-defteri.md"), os.path.join(repo, "fikir-kutusu.md"),
         os.path.join(repo, "veri", "bronz", "hareket-olay.jsonl"), os.path.join(repo, "veri", "bronz", "baglam-olay.jsonl"),
         os.path.join(repo, "veri", "bronz", "altajan-okuma-olay.jsonl"),
         # Karar 100 M3 (09-18): başka devirlerin emir/dönüş dosyaları — işçiye gereken parça liderin görev-fonksiyonuyla verilir
         os.path.join(repo, "cc", "gelen"), os.path.join(repo, "cc", "devir")]
# 09-17 ilk canlı koşum bulgusu: harness büyük araç çıktısını ~/.claude/projects/<proje>/<oturum>/tool-results/ altına yazıp
# alt-ajana "oku" der; bu alt-ajanın KENDİ araç çıktısıdır, başka bağlam penceresi değildir → tool-results/ dizini muaf.
def muaf_mi(r):
    return (os.sep + "tool-results" + os.sep) in r and r.startswith(os.path.join(home, ".claude", "projects") + os.sep)
def yasak_mi(yol):
    if not yol: return False
    r = os.path.realpath(yol if os.path.isabs(yol) else os.path.join(repo, yol))
    if muaf_mi(r): return False
    return any(r == y or r.startswith(y + os.sep) for y in YASAK)
adaylar = []
if arac in ("Read", "Grep", "Glob"):
    adaylar = [ti.get("file_path"), ti.get("path")]
elif arac == "Bash":
    cmd = re.sub(r"<<-?\s*['\"]?(\w+)['\"]?.*?\n\1\s*$", "<<HEREDOC>>", ti.get("command", ""), flags=re.S | re.M)
    ev = home.replace(os.sep, "/")  # Windows'ta ters bölü desenle çakışır; realpath karışık ayracı çözer
    cmd = cmd.replace("~", ev).replace("$HOME", ev).replace("${HOME}", ev)
    adaylar = re.findall(r"(?<![\w@:])(?:[A-Za-z]:)?/?[\w.\-]+(?:/[\w.\-]+)+", cmd)  # `C:/…` sürücü öneki (Windows) da yol adayı
kotu = sorted({a for a in adaylar if a and yasak_mi(a)})
if kotu:
    # Karar 100 M2 (09-18, Friday tur-4 tespiti): test bayrağı YALNIZ kütük yazımını kapatır; exit 2 kararı bayraktan bağımsızdır
    # (eski biçimde bayrak export edilmiş kabukta kilit kesmiyordu — test yeşil, kilit işlevsiz).
    if not os.environ.get("JARVIS_HOOK_TEST"):   # test koşumu bronz kütüğe yazmaz (09-17: 09-10 testi 4 yapay satır bırakmıştı)
        d = os.path.join(repo, "veri", "bronz"); os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "altajan-okuma-olay.jsonl"), "a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(timespec="seconds"),
                                "oturum": (g.get("session_id") or "")[:36], "agent_id": g.get("agent_id"), "agent_type": g.get("agent_type"),
                                "arac": arac, "reddedilen": kotu, "kaynak": "pretool-altajan-okuma.sh"}, ensure_ascii=False) + "\n")
    sys.stderr.write("ALT-AJAN OKUMA KİLİDİ (İB-83): alt-ajan başka bağlam penceresini okuyamaz (transkript · kapsül/pano/defter/kutu · kütükler · Friday · dış projeler). Reddedilen: %s\n" % ", ".join(kotu))
    sys.exit(2)
sys.exit(0)
EOF
