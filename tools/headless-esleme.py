#!/usr/bin/env python3
"""headless-esleme.py — HEADLESS İŞ-SINIFI → YÜZEY EŞLEME TASLAĞI (İB-57; entegrasyon masası K1-2 yeniden çerçeve: "hangi iş sınıfı headless'a iner").
STDLIB ONLY, LLM YOK, deterministik — hareket kütüğü (silver `hareket`) + ambar (`amb_olgu_kosum`) verisinden; hüküm vermez, MASAYA TABLO üretir.

İş sınıfı iki kaynaktan türetilir:
  (A) SKILL İCRA PROFİLİ: her Skill çağrısını izleyen PENCERE adımda araç dağılımı (AskUserQuestion oranı = Salih-kararı ihtiyacı; Bash/Write/Edit
      = dosya-üreten icra; Agent/Workflow = zaten alt-koşum). Sınıf = skill adı.
  (B) AJAN KOŞUM SINIFI: amb_olgu_kosum rol/agent_type kırılımı (n, ortalama süre, araç çağrısı, çıktı token) — bunlar FİİLEN headless (Agent/Workflow).
YÜZEY ATAMA KURALI (deterministik, deneysel m.29 [?]):
  ask_oran > 0                                  → ANA-SIRA (etkileşimli; karar içerir)
  ask_oran = 0 ∧ oturum ≥ 3 ∧ icra_adim ≥ 5      → HEADLESS-ADAY (`claude -p` / schedule / RC): girdi dosya, çıktı dosya, karar yok
  ask_oran = 0 ∧ (oturum < 3 ∨ icra_adim < 5)   → BELİRSİZ (veri az ya da icra yok)
  ajan sınıfları                                 → ZATEN-HEADLESS (Agent alt-koşum ∨ Workflow), yüzey = fiilî yüzey
ÇIKTI: veri/gorunum/v_headless_esleme.csv (sınıf × kaynak × n × oturum × ask_oran × icra_adim × yüzey-önerisi) + stdout özet.
Kullanım: python3 tools/headless-esleme.py [--repo <yol>] [--pencere 12] [--sessiz]   Çıkış: 0 · 2 girdi yok. Deneysel m.29 (2026-08-29, Jarvis).
"""
import argparse, collections, csv, os, sqlite3, sys

def main():
    ap = argparse.ArgumentParser(description="headless eşleme taslağı (İB-57)")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); ap.add_argument("--pencere", type=int, default=12)
    ap.add_argument("--sessiz", action="store_true"); a = ap.parse_args(); repo = os.path.abspath(a.repo)
    db = os.path.join(repo, "veri", "baglam.sqlite")
    if not os.path.exists(db):
        print("HATA: silver yok", file=sys.stderr); return 2
    con = sqlite3.connect(db); out = []
    # (A) skill icra profili
    rows = con.execute("SELECT oturum_id, sira, arac, hedef FROM hareket ORDER BY oturum_id, sira").fetchall()
    byo = collections.defaultdict(list)
    for o, s, ar, h in rows:
        byo[o].append((ar, h or ""))
    prof = collections.defaultdict(collections.Counter); ot = collections.defaultdict(set)
    for o, d in byo.items():
        for i, (ar, h) in enumerate(d):
            if ar == "Skill":
                sk = h.split()[0] if h else "?"; ot[sk].add(o); prof[sk]["_n"] += 1
                for a2, _ in d[i + 1:i + 1 + a.pencere]:
                    prof[sk][a2] += 1
    for sk, c in prof.items():
        n = c["_n"]; ask = c["AskUserQuestion"] / n; icra = (c["Bash"] + c["Write"] + c["Edit"]) / n; alt = (c["Agent"] + c["Workflow"]) / n
        if ask > 0:
            yuzey = "ANA-SIRA"
        elif len(ot[sk]) >= 3 and icra >= 5:
            yuzey = "HEADLESS-ADAY"
        else:
            yuzey = "BELİRSİZ"
        out.append({"sinif": sk, "kaynak": "skill-profili", "n": n, "oturum": len(ot[sk]), "ask_oran": round(ask, 2), "icra_adim": round(icra, 1),
                    "alt_kosum_adim": round(alt, 1), "sure_ort_sn": "", "out_token": "", "yuzey_onerisi": yuzey})
    # (B) ajan koşum sınıfları
    for rol, tip, n, sure, arac, tok in con.execute("SELECT COALESCE(rol,'-'), agent_type, COUNT(*), ROUND(AVG(sure_sn)), ROUND(AVG(arac_cagrisi),1), SUM(output_tokens) FROM amb_olgu_kosum GROUP BY 1,2 ORDER BY 3 DESC"):
        kisa = (rol.split("(")[0].split(".")[0].strip() or "-")[:40]
        yuzey = "ZATEN-HEADLESS: Workflow" if tip == "workflow-subagent" else "ZATEN-HEADLESS: Agent alt-koşum"
        out.append({"sinif": "%s [%s]" % (kisa, tip), "kaynak": "ajan-kosum", "n": n, "oturum": "", "ask_oran": 0.0, "icra_adim": "", "alt_kosum_adim": "",
                    "sure_ort_sn": sure, "out_token": tok, "yuzey_onerisi": yuzey})
    out.sort(key=lambda r: (r["kaynak"], -int(r["n"]), r["sinif"]))
    gd = os.path.join(repo, "veri", "gorunum"); os.makedirs(gd, exist_ok=True)
    kol = ["sinif", "kaynak", "n", "oturum", "ask_oran", "icra_adim", "alt_kosum_adim", "sure_ort_sn", "out_token", "yuzey_onerisi"]
    with open(os.path.join(gd, "v_headless_esleme.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=kol); w.writeheader(); w.writerows(out)
    if not a.sessiz:
        say = collections.Counter(r["yuzey_onerisi"].split(":")[0] for r in out)
        print("headless-esleme · sınıf %d · %s" % (len(out), " · ".join("%s %d" % kv for kv in sorted(say.items()))))
        for r in out:
            if r["kaynak"] == "skill-profili":
                print("  %-28s n=%3s oturum=%2s ask=%.2f icra=%4s alt=%4s → %s" % (r["sinif"], r["n"], r["oturum"], r["ask_oran"], r["icra_adim"], r["alt_kosum_adim"], r["yuzey_onerisi"]))
    return 0

if __name__ == "__main__":
    sys.exit(main())
