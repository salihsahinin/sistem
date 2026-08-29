#!/usr/bin/env python3
"""silver-saglik-kalibrasyon.py — SİLVER-SAĞLIK SABİT KALİBRASYONU (İB-42 kalanı: "sabit kalibrasyonu ≥10 koşum; pencere 3 seans, YETİM eşiği";
sabitler deneysel m.29). STDLIB ONLY, LLM YOK. Girdi: veri/silver-saglik.jsonl (append-only; 1 satır = 1 test × 1 koşum) — koşum sayısı ≥10 şartı.
Ne yapar: koşum başına T-B (SUPERSEDED · MISLEADING · YETIM · KAPANDI) aday sayılarını ve T-Ç ihlallerini zaman sırasına dizer; son N koşum
penceresinde (varsayılan 10) medyan / p90 / maks hesaplar; YETİM eşiği ÖNERİSİ = son-pencere medyanı × 1,5 (uç değil, uyarı bandı; m.29 — karar Salih).
Çıktı: veri/gorunum/v_silver_saglik_kalibrasyon.csv (koşum × test) + stdout özet + veri/silver-saglik-kalibrasyon.jsonl (append-only özet).
Kullanım: python3 tools/silver-saglik-kalibrasyon.py [--repo <yol>] [--pencere 10]   Çıkış: 0 · 2 kütük yok / koşum <10.
Deneysel m.29 (2026-08-29, Carvis, yan icra P9). Kayıt: tools/SCRIPTLER.md.
"""
import argparse, csv, json, os, subprocess, sys
from datetime import datetime, timezone, timedelta

TESTLER = ["T-B-SUPERSEDED", "T-B-MISLEADING", "T-B-YETIM", "T-B-KAPANDI", "T-C1", "T-C2", "T-C3-sicak", "T-C3-ilik", "T-C4a", "T-C4b", "T-C4c", "T-C5", "T-C6"]


def pct(v, p):
    v = sorted(v); k = (len(v) - 1) * p; f = int(k); c = min(f + 1, len(v) - 1); return v[f] + (v[c] - v[f]) * (k - f)


def main():
    ap = argparse.ArgumentParser(description="silver-sağlık sabit kalibrasyonu")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); ap.add_argument("--pencere", type=int, default=10); ap.add_argument("--sessiz", action="store_true")
    a = ap.parse_args(); repo = os.path.abspath(a.repo)
    yol = os.path.join(repo, "veri", "silver-saglik.jsonl")
    if not os.path.exists(yol):
        print("HATA: kütük yok", file=sys.stderr); return 2
    rows = [json.loads(l) for l in open(yol, encoding="utf-8") if l.strip()]
    kosum = {}
    for r in rows:
        k = kosum.setdefault(r["kosum_id"], {"ts": r["ts"], "head": r.get("head"), "snapshot": r.get("snapshot")})
        k[r["test_id"]] = r.get("ihlal")
    sirali = sorted(kosum.items(), key=lambda kv: kv[1]["ts"])
    if len(sirali) < 10:
        print("HATA: koşum %d < 10 — kalibrasyon şartı dolmadı" % len(sirali), file=sys.stderr); return 2
    gd = os.path.join(repo, "veri", "gorunum")
    with open(os.path.join(gd, "v_silver_saglik_kalibrasyon.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n"); w.writerow(["kosum_id", "ts", "head"] + TESTLER)
        for kid, d in sirali:
            w.writerow([kid, d["ts"], d["head"]] + [d.get(t, "") for t in TESTLER])
    son = sirali[-a.pencere:]
    ozet = {}
    for t in TESTLER:
        v = [d.get(t) for _, d in son if isinstance(d.get(t), (int, float))]
        if v:
            ozet[t] = {"n": len(v), "medyan": pct(v, 0.5), "p90": round(pct(v, 0.9), 1), "maks": max(v), "ilk": v[0], "son": v[-1]}
    yetim = ozet.get("T-B-YETIM", {})
    oneri = {"YETIM_uyari_esigi": round(yetim.get("medyan", 0) * 1.5) if yetim else None, "kural": "son %d koşum medyanı × 1,5 (m.29; karar Salih; pencere 3 seans şartı kütükte seans kimliği olmadığından koşum-penceresiyle temsil edildi [?])" % a.pencere}
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip()
    with open(os.path.join(repo, "veri", "silver-saglik-kalibrasyon.jsonl"), "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"ts": datetime.now(timezone(timedelta(hours=3))).replace(microsecond=0).isoformat(), "git_head": head, "kosum_toplam": len(sirali), "pencere": a.pencere, "ozet": ozet, "oneri": oneri, "llm": "yok"}, ensure_ascii=False) + "\n")
    if not a.sessiz:
        print("silver-saglik-kalibrasyon @ %s · %d koşum (%s → %s) · pencere son %d" % (head, len(sirali), sirali[0][1]["ts"][:10], sirali[-1][1]["ts"][:10], a.pencere))
        for t, o in ozet.items():
            print("  %-16s medyan %5.1f · p90 %5.1f · maks %4d · ilk %4d → son %4d" % (t, o["medyan"], o["p90"], o["maks"], o["ilk"], o["son"]))
        print("  ÖNERİ:", json.dumps(oneri, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
