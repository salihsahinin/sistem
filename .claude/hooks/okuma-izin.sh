#!/usr/bin/env bash
# OKUMA-İZİN KİLİDİ — PreToolUse hook (Read · Grep · Glob · Bash). Jarvis Karar 91 (2026-09-09): lider reposu Jarvis'ten YALNIZ
# `kanon/` bağını (= ~/jarvis/core, salt-okur) okur; başka hiçbir Jarvis yolu (kuyruk/, cc/, raporlar/, veri/, hafıza…) bağlama giremez.
# Mekanizma: izinli kökler = bu repo + kanon hedefi + geçici dizinler + harness araç çıktısı; dışı → exit 2 (çağrı engellenir, gerekçe stderr'e).
# Bu bir KİLİTTİR (prompt cümlesi değil); kaçırdığı desen olursa veri/bronz/hareket-olay.jsonl kanıtıyla sonradan görülür.
# v0.2 (2026-09-10, Friday tur-1 A5 düzeltmesi):
#   GENİŞ (yanlış-pozitif) onarımı — heredoc gövdesi (<<EOF … EOF) taranmaz: dosya METNİNDE geçen "~/jarvis" dizesi okuma değildir.
#   DAR (yanlış-negatif) onarımı — `$HOME/jarvis`, `${HOME}/jarvis` biçimleri de taranır; göreli yollar repo köküne göre
#   gerçek yola çözülür (`kanon/../kuyruk` gibi bağ-üstü çıkış yakalanır); `cd` ile dizin değiştirme Jarvis köküne yasak.
# v0.3 (2026-09-18, Karar 99 M2/M3; Friday tur-3 C2 bulguları Z1-Z2 + alt-ajan dalı):
#   (a) ALT-AJAN DALI — girdide `agent_id` varsa (hooks belgesi: "Present only when the hook fires inside a subagent call")
#       liderin bağlam penceresi RED: kapsül · pano · defter · fikir kutusu · veri/bronz/*.jsonl · ~/.claude/projects transkriptleri.
#       Muafiyet: ~/.claude/projects/**/tool-results/** — bu, alt-ajanın KENDİ araç çıktısıdır, başka bağlam penceresi değildir.
#       Her RED veri/bronz/altajan-okuma-olay.jsonl'a düşer. Ana-sıra çağrısı (agent_id yok) bu daldan etkilenmez.
#   (b) Z1 onarımı — Bash dalı artık izin listesi: ev dizini altındaki her yol belirteci izinli köklere göre denetlenir
#       (eskiden yalnız Jarvis yazılışları bakılıyordu; `~/staj başlangıç` gibi repo dışı yollar Bash'ten geçiyordu).
#       Ev dizini dışındaki sistem yolları (/usr, /bin, /opt …) serbest bırakılır: kilidin konusu kullanıcı verisidir.
#   (c) Z2 onarımı — aynı komuttaki `cd` izlenir; göreli yollar repo köküne değil, o anki dizine göre çözülür.
#   (d) Z3 (dize kurgusu: yol çalışma anında değişkenle kurulursa metinde görünmez) KAPANMADI — metin tabanlı taramanın
#       belgelenmiş sınırı (permissions belgesi aynı sınırı `Bash(...)` kuralları için "isn't a security boundary" diye anlatır).
#   Test koşumu bronz kütük YAZMAZ (FRIDAY_HOOK_TEST ya da JARVIS_HOOK_TEST bayrağı) — ama exit 2 kararı bayraktan ETKİLENMEZ.
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
arac = g.get("tool_name", ""); ti = g.get("tool_input", {}) or {}
repo = os.path.realpath(os.environ["REPO"])
home = os.path.realpath(os.path.expanduser("~"))
kanon_hedef = os.path.realpath(os.path.join(repo, "kanon")) if os.path.exists(os.path.join(repo, "kanon")) else None
harness = os.path.join(home, ".claude", "projects")
izinli = [repo] + ([kanon_hedef] if kanon_hedef else []) + ["/tmp", "/private/tmp", "/private/var/folders", harness]
JARVIS = os.path.realpath(os.path.expanduser("~/jarvis"))
TEST = bool(os.environ.get("FRIDAY_HOOK_TEST") or os.environ.get("JARVIS_HOOK_TEST"))

def coz(yol, cwd):
    return os.path.realpath(yol if os.path.isabs(yol) else os.path.join(cwd, yol))

def izinli_mi(r):
    if any(r == k or r.startswith(k + os.sep) for k in izinli):
        return True
    # ev dizini dışındaki sistem yolları serbest (kilidin konusu kullanıcı verisi); ev altındaki her şey izin listesine tabi
    return not (r == home or r.startswith(home + os.sep))

# ---- yol belirteçlerini çıkar (araç başına) ----
def bash_adaylari(cmd):
    """(gerçek_yol, ham) çiftleri; komut içindeki cd'yi izler (Z2)."""
    cmd = re.sub(r"<<-?\s*['\"]?(\w+)['\"]?.*?\n\1\s*$", "<<HEREDOC>>", cmd, flags=re.S | re.M)  # gövde = içerik, okuma değil
    cmd = cmd.replace("${HOME}", home).replace("$HOME", home).replace("~", home)
    cwd = repo; cikti = []
    for parca in re.split(r"&&|\|\||;|\||\n", cmd):
        m = re.match(r"\s*cd\s+(['\"]?)([^'\"\s]+)\1", parca)
        if m:
            cwd = coz(m.group(2), cwd)
            cikti.append((cwd, m.group(2)))
            continue
        for tok in re.findall(r"(?<![\w@:.])(/?[\w.\-]+(?:/[\w.\-]+)+/?)", parca):
            if tok.startswith("//") or re.fullmatch(r"[\d./\-]+", tok):
                continue  # URL kalıntısı ya da sayı/tarih
            cikti.append((coz(tok, cwd), tok))
    return cikti

if arac in ("Read", "Grep", "Glob"):
    adaylar = [(coz(y, repo), y) for y in (ti.get("file_path"), ti.get("path")) if y]
elif arac == "Bash":
    adaylar = bash_adaylari(ti.get("command", ""))
else:
    adaylar = []

# ---- 1. katman: izin listesi (ana-sıra ve alt-ajan için aynı) ----
kotu = [ham for (r, ham) in adaylar if not izinli_mi(r)]
if kotu:
    sys.stderr.write("OKUMA-İZİN KİLİDİ (Karar 91): lider reposu Jarvis'ten yalnız kanon/ (core) okur; repo dışı kullanıcı yolu da kapalıdır. Reddedilen yol: %s\n" % ", ".join(sorted(set(kotu))))
    sys.exit(2)

# ---- 2. katman: alt-ajan dalı (Karar 99 M2; İB-83 eşleniği) ----
agent_id = g.get("agent_id") or ""
if agent_id:
    ALT_YASAK = [os.path.join(repo, "core", "durum-kapsulu.md"), os.path.join(repo, "core", "pano.md"),
                 os.path.join(repo, "kuyruk", "senaryo-defteri.md"), os.path.join(repo, "kuyruk", "fikir-kutusu.md"),
                 os.path.join(repo, "veri", "bronz"), harness]
    def muaf_mi(r):
        return (os.sep + "tool-results" + os.sep) in r and r.startswith(harness + os.sep)
    def alt_yasak_mi(r):
        if muaf_mi(r):
            return False
        return any(r == y or r.startswith(y + os.sep) for y in ALT_YASAK)
    kotu2 = sorted({ham for (r, ham) in adaylar if alt_yasak_mi(r)})
    if kotu2:
        if not TEST:   # test koşumu bronz kütüğe yazmaz; exit kararı bayraktan etkilenmez
            d = os.path.join(repo, "veri", "bronz"); os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, "altajan-okuma-olay.jsonl"), "a", encoding="utf-8") as f:
                f.write(json.dumps({"ts": datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(timespec="seconds"),
                                    "oturum": (g.get("session_id") or "")[:36], "agent_id": agent_id,
                                    "agent_type": g.get("agent_type") or "", "arac": arac, "reddedilen": kotu2,
                                    "kaynak": "okuma-izin.sh v0.3"}, ensure_ascii=False) + "\n")
        sys.stderr.write("ALT-AJAN OKUMA KİLİDİ (Karar 99 M2): işçi, liderin bağlam penceresini okuyamaz (kapsül · pano · defter · kutu · kütükler · transkriptler; kendi tool-results'ı muaf). Reddedilen: %s\n" % ", ".join(kotu2))
        sys.exit(2)
sys.exit(0)
EOF
