#!/usr/bin/env python3
"""asof-eval.py — AS-OF EVAL (İB-42 kalanı: "v_guncel ↔ ham, n≈20-30"; Karar 58 güncel-yüzey). STDLIB ONLY, LLM YOK, deterministik.

Soru: silver'ın güncel yüzeyi (`gecerlilik=guncel ∧ sıcak/ılık`; erisim-fts `guncel_yuzey=True`) HAM korpusa göre bayat bilgiyi
gerçekten dışarıda bırakıyor mu? İki kol, toplam n=30:
  (1) EMEKLİ TERİM sorguları (n=10; anahtar_kaydi rol=emekli, ör. "günaydın", "CEO", "vardiya"): sorgu = emekli değer; ham ↔ yüzey top-5'te
      (a) gecerlilik='emekli-kalinti' kayıt sayısı, (b) metni GÜNCEL değeri (replaced_by) içeren kayıt var mı. Beklenti: yüzeyde (a)=0, (b) artar.
  (2) BİLGİ-GÜNCELLEME soruları (n=20; altın sette yetenek=bilgi-guncelleme): recall@5 ham ↔ yüzey ↔ auto (erisim-kalibrasyon ile aynı metrik).
Çıktı: veri/gorunum/v_asof_eval.csv (kol × sorgu satırları + özet) · veri/asof-eval.jsonl (append-only koşum özeti).
Kullanım: python3 tools/asof-eval.py [--repo <yol>] [--sessiz]   Çıkış: 0 · 2 girdi yok. Deneysel m.29 (2026-08-29, Jarvis, yan icra P9).
"""
import argparse, csv, importlib.util, json, os, sqlite3, subprocess, sys
from datetime import datetime, timezone, timedelta


def yukle(repo, ad):
    yol = os.path.join(repo, "tools", ad); spec = importlib.util.spec_from_file_location(ad.replace("-", "_").replace(".py", ""), yol)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def main():
    ap = argparse.ArgumentParser(description="as-of eval (İB-42)")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); ap.add_argument("--sessiz", action="store_true")
    a = ap.parse_args(); repo = os.path.abspath(a.repo)
    db = os.path.join(repo, "veri", "baglam.sqlite")
    if not os.path.exists(db):
        print("HATA: silver yok", file=sys.stderr); return 2
    fts = yukle(repo, "erisim-fts.py"); vek = yukle(repo, "erisim-vektor.py")
    con = sqlite3.connect(db)
    if not con.execute("SELECT COUNT(*) FROM sqlite_master WHERE name='kayit_fts'").fetchone()[0]:
        print("HATA: kayit_fts yok — erisim-fts.py --insa", file=sys.stderr); return 2
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip()
    ts = datetime.now(timezone(timedelta(hours=3))).replace(microsecond=0).isoformat()
    gec = dict(con.execute("SELECT kayit_id, COALESCE(gecerlilik,'') FROM kayit").fetchall())
    satirlar = []
    # ---- (1) emekli terim kolu ----
    emekli = con.execute("SELECT anahtar_id, deger, replaced_by FROM anahtar_kaydi WHERE rol='emekli' AND replaced_by IS NOT NULL AND replaced_by<>'' ORDER BY anahtar_id").fetchall()
    for aid, eski, yeni in emekli:
        for kol, gy in (("ham", False), ("yuzey", True)):
            rows = fts.sorgula(con, eski, 5, genisletme=True, zaman_farkindali=False, guncel_yuzey=gy)[0]
            kalinti = sum(1 for r in rows if gec.get(r[0]) == "emekli-kalinti")
            metinler = [con.execute("SELECT metin FROM kayit WHERE kayit_id=?", (r[0],)).fetchone()[0] or "" for r in rows]
            yeni_var = any(yeni.lower() in m.lower() for m in metinler); eski_var = sum(1 for m in metinler if eski.lower() in m.lower())
            satirlar.append({"kol": "emekli-terim", "sorgu": "%s (%s)" % (eski, aid), "yuzey": kol, "n_sonuc": len(rows), "emekli_kalinti_top5": kalinti, "eski_deger_gecen": eski_var, "guncel_deger_var": int(yeni_var), "recall5": ""})
    # ---- (2) bilgi-guncelleme kolu ----
    sorular, _ = fts.sorulari_oku(repo)
    bg = [s for s in sorular if s["yetenek"] == "bilgi-guncelleme" and s.get("beklenen_dosya")]
    for s in bg:
        for kol, gy in (("ham", False), ("yuzey", True), ("auto", bool(fts.GUNCEL_RX.search(s["soru"])))):
            rows = fts.sorgula(con, s["soru"], 50, genisletme=True, zaman_farkindali=True, guncel_yuzey=gy)[0]
            r5, mrr, nd = vek.metrik(vek.dosya_sirasi([(r[0], r[1]) for r in rows]), s["beklenen_dosya"])
            satirlar.append({"kol": "bilgi-guncelleme", "sorgu": s["id"], "yuzey": kol, "n_sonuc": len(rows), "emekli_kalinti_top5": sum(1 for r in rows[:5] if gec.get(r[0]) == "emekli-kalinti"), "eski_deger_gecen": "", "guncel_deger_var": "", "recall5": r5})
    # ---- özet ----
    oz = {}
    for kol in ("ham", "yuzey"):
        e = [x for x in satirlar if x["kol"] == "emekli-terim" and x["yuzey"] == kol]
        oz["emekli-terim/" + kol] = {"n": len(e), "kalinti_top5_toplam": sum(x["emekli_kalinti_top5"] for x in e), "guncel_deger_var": sum(x["guncel_deger_var"] for x in e), "eski_deger_gecen_toplam": sum(x["eski_deger_gecen"] for x in e)}
    for kol in ("ham", "yuzey", "auto"):
        b = [x for x in satirlar if x["kol"] == "bilgi-guncelleme" and x["yuzey"] == kol]
        oz["bilgi-guncelleme/" + kol] = {"n": len(b), "recall5": round(sum(x["recall5"] for x in b) / len(b), 3) if b else None, "kalinti_top5_toplam": sum(x["emekli_kalinti_top5"] for x in b)}
    gd = os.path.join(repo, "veri", "gorunum")
    with open(os.path.join(gd, "v_asof_eval.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["kol", "sorgu", "yuzey", "n_sonuc", "emekli_kalinti_top5", "eski_deger_gecen", "guncel_deger_var", "recall5"], lineterminator="\n"); w.writeheader(); w.writerows(satirlar)
    with open(os.path.join(repo, "veri", "asof-eval.jsonl"), "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"ts": ts, "git_head": head, "n": len(emekli) + len(bg), "ozet": oz, "llm": "yok"}, ensure_ascii=False) + "\n")
    if not a.sessiz:
        print("asof-eval @ %s · emekli terim %d · bilgi-guncelleme %d · LLM yok" % (head, len(emekli), len(bg)))
        for k, v in oz.items():
            print("  %-26s %s" % (k, json.dumps(v, ensure_ascii=False)))
    con.close(); return 0


if __name__ == "__main__":
    sys.exit(main())
