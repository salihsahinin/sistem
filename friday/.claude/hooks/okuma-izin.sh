#!/usr/bin/env bash
# OKUMA-İZİN KİLİDİ — PreToolUse hook (Read · Grep · Glob · Bash). Jarvis Karar 91 (2026-09-09): lider reposu Jarvis'ten YALNIZ
# `kanon/` bağını (= ~/sistem/jarvis/core, salt-okur) okur; başka hiçbir Jarvis yolu (kuyruk/, cc/, raporlar/, veri/, hafıza…) bağlama giremez.
# Mekanizma: izinli kökler = bu repo + kanon hedefi + geçici dizinler + harness araç çıktısı; dışı → exit 2 (çağrı engellenir, gerekçe stderr'e).
# Bu bir KİLİTTİR (prompt cümlesi değil); kaçırdığı desen olursa veri/bronz/hareket-olay.jsonl kanıtıyla sonradan görülür.
# v0.2 (2026-09-10, tur-1 A5): heredoc gövdesi taranmaz (yanlış-pozitif); `$HOME/sistem/jarvis`, `${HOME}/jarvis`, `kanon/../x` yakalanır.
# v0.3 (2026-09-18, Karar 99 M2): alt-ajan dalı (`agent_id`) + Bash dalı izin listesine çevrildi (Z1) + `cd` takibi (Z2).
# v0.4 (2026-09-18, Karar 100 M1/M3; tur-4 raporu §4d seçenek (c)):
#   (a) AYRIŞTIRICI — Bash'te yol adayları artık yalnız DOSYA KOMUTLARININ argümanlarından toplanır (aşağıdaki DOSYA_KOMUT kümesi),
#       artı yönlendirme hedefleri (`> < >>`). `grep`/`rg`/`sed`/`awk`/`jq` gibi komutlarda İLK argüman desen/betiktir, yol sayılmaz
#       (tur-4'te bir `grep` deseni çağrıyı durdurmuştu). Tırnak soyulur, yani tırnaklı açık yol yakalanmaya devam eder.
#       Değişken içeren belirteçte `$`'tan ÖNCEKİ sabit önek denetlenir (`~/$J/kuyruk` yakalanır; yolun tamamı değişkense — Z3b —
#       görünmez: metin taramasının bilinen sınırı, Karar 100 M5 ile bu turda açık bırakıldı).
#   (b) ALT-AJAN — yasak listesine `cc/gelen/**` eklendi (Karar 100 M3): işçi başka devirlerin emirlerini okuyamaz.
#       Liderin kendi emrini okuması etkilenmez: dal yalnız `agent_id` varken çalışır.
#   Read/Grep/Glob dalı v0.3'teki gibidir; test bayrağı (FRIDAY_HOOK_TEST | JARVIS_HOOK_TEST) yalnız bronz kütük yazımını kapatır,
#   `exit 2` kararını ETKİLEMEZ.
# v0.5 (2026-09-18, Karar 101 monorepo `sistem`, F3): `kanon/` bağı emekli. İzinli kökler = bu repo + depo kökünün doğrudan
#   altındaki dosyalar (`~/sistem/AGENTS.md`, `CLAUDE.md`, `README.md`…; genelleştirilmiş kanon) + geçici + harness. `jarvis/**`
#   tamamen kapalı (Jarvis `core/` dahil; Friday'in gördüğü kural kökteki kanon). Depo kökü = repo'nun üst dizini.
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
kok = os.path.dirname(repo)  # depo kökü (~/sistem): kök kanon dosyaları buradan okunur (v0.5, Karar 101)
harness = os.path.join(home, ".claude", "projects")
izinli = [repo, os.path.join(kok, "sablonlar"), "/tmp", "/private/tmp", "/private/var/folders", harness]  # kök sablonlar/ ortak (F4)
TEST = bool(os.environ.get("FRIDAY_HOOK_TEST") or os.environ.get("JARVIS_HOOK_TEST"))

# Dosya açan komutlar: argümanları yol sayılır. Liste EKSİK KALABİLİR (desen 20) — yeni bir okuma komutu buraya eklenmeli.
DOSYA_KOMUT = {"cat", "sed", "head", "tail", "less", "more", "cp", "mv", "ln", "rm", "python3", "python", "bash", "sh",
               "source", ".", "jq", "sqlite3", "wc", "sort", "uniq", "diff", "open", "code", "ls", "find", "awk",
               "grep", "rg", "egrep", "fgrep", "tee", "touch", "mkdir", "stat", "file", "md5", "shasum", "nl", "cut"}
# İlk argümanı desen/betik olan komutlar: o argüman yol sayılmaz.
DESEN_ILK = {"grep", "rg", "egrep", "fgrep", "sed", "awk", "jq", "find"}
DEGER_ALAN_BAYRAK = {"-e", "-f", "--regexp", "--file", "--include", "--exclude", "-name", "-iname", "-path"}
SARMALAYICI = {"sudo", "time", "timeout", "nice", "nohup", "stdbuf", "command", "builtin", "xargs", "env"}

def coz(yol, cwd):
    return os.path.realpath(yol if os.path.isabs(yol) else os.path.join(cwd, yol))

def izinli_mi(r):
    if any(r == k or r.startswith(k + os.sep) for k in izinli):
        return True
    # kök kanon: depo kökünün kendisi ve doğrudan altındaki dosyalar serbest; alt dizinler (jarvis/**) izin listesine tabi
    if r == kok or (os.path.dirname(r) == kok and not os.path.isdir(r)):
        return True
    # ev dizini dışındaki sistem yolları serbest (kilidin konusu kullanıcı verisi); ev altındaki her şey izin listesine tabi
    return not (r == home or r.startswith(home + os.sep))

def soy(tok):
    return tok.strip().strip("'\"")

def yol_mu(tok):
    """Belirteç bir yol adayı mı; değişkenliyse sabit öneki döndürür ('' = görünmez)."""
    if "$" in tok:
        tok = tok.split("$", 1)[0]
    if not tok or tok.startswith("-"):
        return ""
    return tok if ("/" in tok or tok.startswith(".")) else ""

def bash_adaylari(cmd):
    """(gerçek_yol, ham) çiftleri; komut içindeki cd izlenir (Z2), yalnız dosya komutlarının argümanları taranır (v0.4)."""
    cmd = re.sub(r"<<-?\s*['\"]?(\w+)['\"]?.*?\n\1\s*$", "<<HEREDOC>>", cmd, flags=re.S | re.M)  # gövde = içerik, okuma değil
    cmd = cmd.replace("${HOME}", home).replace("$HOME", home).replace("~", home)
    cwd = repo; cikti = []
    for parca in re.split(r"&&|\|\||;|\||\n", cmd):
        parcalar = [p for p in re.findall(r"""[^\s'"]+|'[^']*'|"[^"]*\"""", parca) if p]
        if not parcalar:
            continue
        i = 0
        # ortam ataması ve sarmalayıcıları geç
        while i < len(parcalar) and (re.fullmatch(r"\w+=[^\s]*", parcalar[i]) or soy(parcalar[i]) in SARMALAYICI):
            i += 1
        if i >= len(parcalar):
            continue
        komut = os.path.basename(soy(parcalar[i])); i += 1
        if komut == "cd":
            hedef = soy(parcalar[i]) if i < len(parcalar) else ""
            if hedef and "$" not in hedef:
                cwd = coz(hedef, cwd)
                cikti.append((cwd, hedef))
            continue
        desen_atlanacak = komut in DESEN_ILK
        atla_sonraki = False
        for ham in parcalar[i:]:
            t = soy(ham)
            if atla_sonraki:
                atla_sonraki = False
                continue
            if t in DEGER_ALAN_BAYRAK:
                atla_sonraki = True
                continue
            if t.startswith(("<", ">")) or t in (">", ">>", "<", "2>"):   # yönlendirme: hedef her zaman aday
                hedef = t.lstrip("<>2").strip()
                if hedef:
                    p = yol_mu(hedef)
                    if p:
                        cikti.append((coz(p, cwd), hedef))
                else:
                    atla_sonraki = False
                continue
            if t.startswith("-"):
                continue
            if desen_atlanacak:          # ilk sözcük-argüman desen/betiktir
                desen_atlanacak = False
                continue
            if komut not in DOSYA_KOMUT:
                continue
            p = yol_mu(t)
            if p:
                cikti.append((coz(p, cwd), t))
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
    sys.stderr.write("OKUMA-İZİN KİLİDİ (Karar 91/101): lider reposu kendi dizini + depo kökündeki kanon dosyalarını okur; jarvis/** ve repo dışı kullanıcı yolu kapalıdır. Reddedilen yol: %s\n" % ", ".join(sorted(set(kotu))))
    sys.exit(2)

# ---- 2. katman: alt-ajan dalı (Karar 99 M2; cc/gelen Karar 100 M3) ----
agent_id = g.get("agent_id") or ""
if agent_id:
    ALT_YASAK = [os.path.join(repo, "core", "durum-kapsulu.md"), os.path.join(repo, "core", "pano.md"),
                 os.path.join(repo, "kuyruk", "senaryo-defteri.md"), os.path.join(repo, "kuyruk", "fikir-kutusu.md"),
                 os.path.join(repo, "veri", "bronz"), os.path.join(repo, "cc", "gelen"), harness]
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
                                    "kaynak": "okuma-izin.sh v0.4"}, ensure_ascii=False) + "\n")
        sys.stderr.write("ALT-AJAN OKUMA KİLİDİ (Karar 99 M2 · 100 M3): işçi, liderin bağlam penceresini ve başka devirlerin emirlerini okuyamaz (kapsül · pano · defter · kutu · kütükler · cc/gelen · transkriptler; kendi tool-results'ı muaf). Reddedilen: %s\n" % ", ".join(kotu2))
        sys.exit(2)
sys.exit(0)
EOF
