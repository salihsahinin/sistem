#!/usr/bin/env bash
# AJAN FAN-OUT FRENİ — PreToolUse hook, matcher: Agent (İB-54 adım 2; Karar 74 M-4 (d) paket A "sınıf-bazlı deterministik çağrı-freni";
# Karar 39 Salih: "fren tetiklenme koşulu zor olsun, aşırı uç senaryolar için çalışsın; kaliteyi kısmayalım").
# Kök neden (raporlar/2026-08-29-ib54-delinme-kok-neden.md KN-1/KN-2/KN-4): fren metindeydi, ölçüm harcamadan SONRAYDI, fan-out atomikti.
# Bu hook freni KOŞUM KATMANINA taşır: her Agent çağrısı TAAHHÜT ANINDA sayılır (oturum başına sayaç); UYARI eşiğinde bronz olay,
# DURDUR eşiğinde çağrı engellenir (exit 2 + gerekçe). Workflow ajanları bu hook'tan GEÇMEZ — onlar için cc/workflow/fren-sablonu.js.
# Eşikler (m.29 deneysel; taban silver amb_olgu_kosum @b16b1a9, 29 wf: ajan/wf p50 12 · max 23; hareket: Agent/oturum max 11):
#   UYARI  = 36  (p50 × 3 — Öneri A "medyan × ~3")      DURDUR = 72  (UYARI × 2 ≈ max × 3 — aşırı uç)  [tek-katman tabanı, AS-OF 2026-08-29]
# REVİZYON (Salih B-hükmü 2026-08-31, devir cc/devir-2026-08-31-opus-icra.md soru-1): sayaç oturum-geneli ve alt-ajan çağrılarını da
# sayıyor → lider→işçi (firstmate) iki-katmanlı koşum tek-katman tabanını yapısal aşıyor (ölçüm: 78 çağrı / 4 birim ≈ 20/birim).
# Yeni varsayılan: UYARI 72 · DURDUR 144 (2× katman çarpanı). Katman-başına ayrı sayaç (seçenek A) masa kalemi olarak kuyrukta.
# REJİM ETİKETİ (tüzük m.46(d), Karar 39 C): [rejim: manuel-tempo · kota-bol · ekonomi −%30 (Salih 08-15) · AS-OF 2026-08-29] — rejim
# değişince (K-009/K-010 otomasyon) eşikler OTOMATİK yeniden açılır, taşınmaz. Salih beyanıyla geçici kapatma: JARVIS_FREN_KAPALI=1 (olay yazılır).
# Kayıt: bronz veri/bronz/fren-olay.jsonl (append-only; 1 satır = 1 fren olayı) · sayaç durumu .claude/hooks/state/ (gitignore, oturum başına).
input=$(cat)
PY=$(command -v python3 || command -v python)
[ -z "$PY" ] && exit 0   # python yoksa tel bozuk-modda sessiz geçer (tökezleme-teli, sınır değil)
REPO="${CLAUDE_PROJECT_DIR:-$PWD}"
# JSON girdisi ORTAM DEĞİŞKENİYLE geçer: `python -` script'i stdin'den okur, ikinci stdin (pipe) olamaz (ilk test 08-29: 3/3 düştü, düzeltildi).
INPUT="$input" REPO="$REPO" UYARI="${JARVIS_FREN_UYARI:-72}" DURDUR="${JARVIS_FREN_DURDUR:-144}" KAPALI="${JARVIS_FREN_KAPALI:-0}" "$PY" - <<'EOF'
import json, os, sys
from datetime import datetime, timezone, timedelta
try:
    g = json.loads(os.environ.get("INPUT") or "{}")
except Exception:
    sys.exit(0)
if g.get("tool_name") not in ("Agent", "Task"):
    sys.exit(0)
repo = os.environ["REPO"]; uyari = int(os.environ["UYARI"]); durdur = int(os.environ["DURDUR"]); kapali = os.environ["KAPALI"] == "1"
sid = (g.get("session_id") or "oturum")[:36]
sd = os.path.join(repo, ".claude", "hooks", "state"); os.makedirs(sd, exist_ok=True)
syol = os.path.join(sd, "ajan-fren-%s.json" % sid)
try:
    st = json.load(open(syol, encoding="utf-8"))
except Exception:
    st = {"sayac": 0, "uyari_yazildi": False}
st["sayac"] += 1; n = st["sayac"]
ti = g.get("tool_input") or {}
aciklama = (ti.get("description") or "")[:80]
ts = datetime.now(timezone(timedelta(hours=3))).replace(microsecond=0).isoformat()
rejim = "manuel-tempo · kota-bol · ekonomi -%30 (08-15) · AS-OF 2026-08-29"
def olay(tur, mesaj):
    with open(os.path.join(repo, "veri", "bronz", "fren-olay.jsonl"), "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"ts": ts, "session_id": sid, "arac": g.get("tool_name"), "sayac": n, "esik_uyari": uyari, "esik_durdur": durdur,
                             "olay": tur, "aciklama": aciklama, "rejim": rejim, "mesaj": mesaj, "kaynak": "pretool-ajan-fren.sh"}, ensure_ascii=False) + "\n")
if n >= durdur:
    if kapali:
        olay("ASILDI-KAPALI", "JARVIS_FREN_KAPALI=1 (Salih beyanı) — engel kaldırıldı, kayıt düşüldü")
    else:
        olay("DURDUR", "Agent çağrısı engellendi")
        json.dump(st, open(syol, "w", encoding="utf-8"))
        print("AJAN FRENİ (İB-54, Karar 39 uç-eşik): bu oturumda %d. Agent çağrısı — DURDUR eşiği %d (UYARI %d; taban ajan/wf p50 12, max 23). "
              "Fan-out aşırı uç sınıfta: önce ölç (veri/bronz/fren-olay.jsonl), gerekçeli devam için Salih beyanı → JARVIS_FREN_KAPALI=1 ya da eşik revizyonu. "
              "Rejim: %s" % (n, durdur, uyari, rejim), file=sys.stderr)
        sys.exit(2)
elif n >= uyari and not st["uyari_yazildi"]:
    st["uyari_yazildi"] = True
    olay("UYARI", "uyarı eşiği geçildi (engel yok)")
json.dump(st, open(syol, "w", encoding="utf-8"))
sys.exit(0)
EOF
exit $?
