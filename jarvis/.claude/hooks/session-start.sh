#!/usr/bin/env bash
# JARVIS SessionStart hook — BRİF ≤2 KB (KB-51 (a), Salih imzası 08-21 Karar 61; icra İB-24 2026-08-22 seans-14).
# Tarihçe: kurulum 2026-07-19 (Dilim 1: kapsül ilk 40 satır + yetki bandı, 11 KB); rev 08-16/08-17 yetki bandı GK-2.
# Neden indi: harness yalnız ~2 KB önizlemeyi bağlama koyar (25,8 KB → 2 KB; KB-51) → tam kapsül BURADA DEĞİL, elle okunur (CLAUDE.md §3).
# İB-27 (KB-54 (a) Karar 62): silver tazelik — uretim.git_head_sha ≠ HEAD → "BAYAT" + katman-hatti tarifi (otomasyon: tespit; koşum ritüelde).
# Karar 68 (08-26): ZAMAN-ZEMİNİ satırı — bugün (sistem saati) + model kesim tablosu; anakronizm freni.
# Çıktı sert-kapılı: head -c 2000. Her satır tek bakışta; deterministik (yalnız disk + git).
. "$(dirname "${BASH_SOURCE[0]}")/rust-yonlendir.sh" session-start   # Rust varsa exec; yoksa aşağısı (durum #1)
cd "$(dirname "$0")/../.." 2>/dev/null || true
{
echo "=== JARVIS SessionStart (brif ≤2 KB; tam durum: core/durum-kapsulu.md) ==="
echo "AD (Karar 93): Salih'le konuşan ajan = JARVİS (eski ad Carvis) · repo = 'depo'/'kanon' · denetim tools/ad-esitligi-denetim.py"
echo "PAKET (Karar 112 EK-2): Salih mesajını niyetlere böl, anlamdan paket|yok seç (kanon·ajan·skill·veri·baglam·dogrulama, ≤2); değişince tools/paket-yonlendir.py --sec --niyet … --paket …; bildirim niyet değil."
echo "YETKİ (m.41 GK-2): Claude Code (giriş: ${CLAUDE_CODE_ENTRYPOINT:-?}) = ANA-SIRA · kanon kararı = (ana-sıra ∧ en güçlü model, bugün Fable) ∨ Salih imzası · Katman-1 (core/, CLAUDE.md, tüzük) yalnız Salih · frenler: push Salih beyanıyla (m.9) · md.49 · PreToolUse teli · canlı paralel oturumda git add <yol> (H4)."
python3 - <<'PY' 2>/dev/null || echo "BRİF: silver okunamadı (python3 ya da veri/baglam.sqlite yok) → python3 tools/katman-hatti.py"
import sqlite3, subprocess, re
def sh(c):
    try: return subprocess.run(c, shell=True, capture_output=True, text=True).stdout.strip()
    except Exception: return "?"
head = sh("git rev-parse --short HEAD"); when = sh("git log -1 --format=%ci")[:16]
print("HEAD: %s (%s) · %s" % (head, when, sh("git status -sb | head -1 | sed 's/## //'")))
try:  # Karar 68 (08-26) anakronizm freni: BUGÜN sistem saatinden + model kesim tablosu (veri/model-kesim.jsonl, satıcı tablosu V26'lı) — model hafızası ≠ bugün
    import json, datetime
    ks = {}
    for l in open("veri/model-kesim.jsonl", encoding="utf-8"):
        d = json.loads(l)
        if d["kesim_turu"] == "reliable": ks[d["model_ad"].replace("Claude ", "")] = d["kesim_tarihi"]
    print("ZAMAN-ZEMİNİ (Karar 68): BUGÜN %s · kesim(reliable) %s · zaman-bağımlı iddia AS-OF damgasız ÇIKMAZ; model-hafızası = 'AS-OF ≤ kesim, doğrulanmadı' → canlı çek (tools/anakronizm-denetim.py)" % (datetime.date.today().isoformat(), " · ".join("%s %s" % kv for kv in ks.items())))
except Exception as e:
    print("ZAMAN-ZEMİNİ: kesim tablosu okunamadı (%s) — veri/model-kesim.jsonl" % e)
try:
    c = sqlite3.connect("file:veri/baglam.sqlite?mode=ro", uri=True)
    u = c.execute("SELECT git_head_sha, uretim_zamani FROM uretim ORDER BY uretim_zamani DESC LIMIT 1").fetchone()
    taze = bool(u and head and u[0].startswith(head))
    print("SİLVER: %s (%s) → %s" % ((u[0][:7] if u else "?"), (u[1][:16] if u else "?"), "TAZE" if taze else "BAYAT → python3 tools/katman-hatti.py (~12 sn; Karar 62 İB-27)"))
    try:
        r = c.execute("SELECT acik_salih_karari, acik_icra_borcu, son_teslim, son_kosum FROM v_amb_acilis_brifi LIMIT 1").fetchone()
        if r: print("AS-OF: açık Salih kararı %s · açık icra borcu %s · son teslim %s · son koşum %s" % (r[0], r[1], (r[2] or "-")[:60], (r[3] or "-")[:50]))
    except Exception: pass
    try:
        s = c.execute("SELECT sonuc FROM silver_saglik_son WHERE test_id='T-C3-sicak'").fetchone()
        q = c.execute("SELECT COUNT(*) FROM silver_kuyruk").fetchone()[0]
        print("SİLVER-SAĞLIK: sıcak kalıntı %s · kuyruk aday %s (v_silver_kuyruk_ozet)" % ((s[0] if s else "?"), q))
    except Exception: pass
except Exception as e:
    print("SİLVER: okunamadı (%s) → python3 tools/katman-hatti.py" % e)
try:
    t = open("core/durum-kapsulu.md", encoding="utf-8").read()
    m = re.search(r"## Sonraki ilk iş\s*\n(.*?)\n", t, re.S)
    if m: print("SONRAKİ İLK İŞ: " + re.sub(r"[*`]", "", m.group(1))[:190])
    g = re.search(r"\*\*Güncelleme:\*\*\s*(.{0,90})", t)
    if g: print("KAPSÜL: " + re.sub(r"[*`]", "", g.group(1)))
except Exception: pass
PY
echo "OKU (CLAUDE.md §3): core/durum-kapsulu.md (tamamı) → core/pano.md → ritüel 'seans başı' (kapılar: python3 tools/acilis-kapilari.py K1-K3; İB-91)."
echo "=== /SessionStart ==="
} | head -c 2000
