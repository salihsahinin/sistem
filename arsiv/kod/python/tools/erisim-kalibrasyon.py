#!/usr/bin/env python3
"""erisim-kalibrasyon.py — ERİŞİM KATMANI KALİBRASYONU (İB-43 kalanı; KB-43 a / Karar 60 sırası). STDLIB ONLY, LLM YOK, deterministik.

(a) GENİŞLETME AĞIRLIĞI: `erisim-fts.sorgula` bm25 ağırlığı (metin 1,0 · genişletme w) için w ∈ GRID × güncel-yüzey ∈ {kapalı, açık} taranır;
    100 altın soru (veri/sozlesme/erisim-eval-sorular.jsonl), ilk 50 aday dosya düzeyinde tekilleştirilir; recall@5 / MRR / nDCG@10 (erisim-vektor
    ile AYNI metrik kodu, importlib) yetenek başına + TÜMÜ. Seçim kuralı (deterministik): TÜMÜ nDCG@10 max → eşitlikte recall@5 → eşitlikte küçük w.
    Sonuç ÖNERİDİR: GEN_AGIRLIK sabiti yalnız seçilen w, mevcut varsayılana göre HEM TÜMÜ nDCG@10 HEM bilgi-guncelleme recall@5'te ≥ ise değiştirilir (m.29).
(b) ÇEKİMSERLİK EŞİĞİ: veri/erisim-eval.jsonl'daki son koşum satırlarından (yontem ∈ {vektor-e5, vektor-bge, vektor-e5-i8, vektor-bge-i8, fts5+gen})
    cevapsız (yetenek=cekimserlik) ↔ isabetli (recall5=1) sorguların top1 skor dağılımı; eşik t = dengeli doğruluğu (½·(cevapsız yakalama + isabetli koruma))
    maksimize eden değer (tekil skorlar üzerinde tarama; vektörde uzaklık büyük = uzak, bm25 negatif küçük = iyi). n küçük → öneri, damga [?].
Çıktı: veri/gorunum/v_erisim_kalibrasyon.csv (grid) · v_erisim_cekimserlik.csv (eşikler) · veri/erisim-kalibrasyon.jsonl (append-only koşum özeti).
Kullanım: python3 tools/erisim-kalibrasyon.py [--repo <yol>] [--grid 0,0.5,1,1.5,2,3,4] [--sessiz]   Çıkış: 0 · 2 girdi yok.
Model-düşümü önlemi (Salih 08-29): bu araç LLM çağırmaz; sonuçlar yalnız SQLite/kütükten türetilir — model değişimi sonucu etkileyemez.
Deneysel m.29 (2026-08-29, Jarvis, yan icra oturumu). Kayıt: tools/SCRIPTLER.md.
"""
import argparse, csv, importlib.util, json, os, sqlite3, subprocess, sys, time
from datetime import datetime, timezone, timedelta


def yukle(repo, ad):
    yol = os.path.join(repo, "tools", ad); spec = importlib.util.spec_from_file_location(ad.replace("-", "_").replace(".py", ""), yol)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def main():
    ap = argparse.ArgumentParser(description="erişim kalibrasyonu (İB-43)")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--grid", default="0,0.5,1,1.5,2,3,4"); ap.add_argument("--sessiz", action="store_true")
    a = ap.parse_args(); repo = os.path.abspath(a.repo)
    db = os.path.join(repo, "veri", "baglam.sqlite")
    if not os.path.exists(db):
        print("HATA: silver yok", file=sys.stderr); return 2
    fts = yukle(repo, "erisim-fts.py"); vek = yukle(repo, "erisim-vektor.py")  # vektör modülünün stdlib kısımları (metrik, dosya_sirasi, bootstrap)
    sorular, hata = fts.sorulari_oku(repo)
    if hata:
        print("HATA: soru seti: %s" % hata[:2], file=sys.stderr); return 2
    con = sqlite3.connect(db)
    if not con.execute("SELECT COUNT(*) FROM sqlite_master WHERE name='kayit_fts'").fetchone()[0]:
        print("HATA: kayit_fts yok — önce erisim-fts.py --insa", file=sys.stderr); return 2
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip()
    ts = datetime.now(timezone(timedelta(hours=3))).replace(microsecond=0).isoformat()
    grid = [float(x) for x in a.grid.split(",") if x.strip()]
    yetenekler = [y for y in fts.YETENEK if y != "cekimserlik"]
    # ---- (a) ağırlık grid'i ----
    satirlar, ozet = [], {}
    for w in grid:
        for guncel in (False, True, "auto"):  # auto: yüzey yalnız soruda güncellik sözcüğü varsa (GUNCEL_RX) — deterministik yönlendirme (08-29 bulgusu: yüzey yetenek-bağımlı)
            ad = "gen=%g%s" % (w, "+guncel" if guncel is True else ("+auto" if guncel == "auto" else ""))
            per = {}
            t0 = time.perf_counter()
            for s in sorular:
                if not s.get("beklenen_dosya"):
                    continue
                gy = bool(fts.GUNCEL_RX.search(s["soru"])) if guncel == "auto" else guncel
                rows = fts.sorgula(con, s["soru"], 50, genisletme=(w > 0), zaman_farkindali=True, guncel_yuzey=gy, gen_agirlik=w)[0]
                per[s["id"]] = (s["yetenek"],) + vek.metrik(vek.dosya_sirasi([(r[0], r[1]) for r in rows]), s["beklenen_dosya"])
            sure = (time.perf_counter() - t0) * 1000 / max(1, len(per))
            for yet in yetenekler + ["TÜMÜ"]:
                v = [x for x in per.values() if yet == "TÜMÜ" or x[0] == yet]
                if not v:
                    continue
                r5 = sum(x[1] for x in v) / len(v); mrr = sum(x[2] for x in v) / len(v); nd = sum(x[3] for x in v) / len(v)
                satirlar.append({"ayar": ad, "gen_agirlik": w, "guncel_yuzey": guncel, "yetenek": yet, "n": len(v), "recall5": round(r5, 3), "mrr": round(mrr, 3), "ndcg10": round(nd, 3), "ort_sure_ms": round(sure, 2)})
                o = ozet.setdefault(ad, {"w": w, "guncel": guncel})
                if yet == "TÜMÜ":
                    o.update({"recall5": r5, "ndcg10": nd, "mrr": mrr})
                if yet == "bilgi-guncelleme":
                    o["bg_recall5"] = r5  # (ilk sürüm TÜMÜ satırında sözlüğü üzerine yazıyordu → 0,000; düzeltildi 08-29)
    sira = lambda kv: (-round(kv[1]["ndcg10"], 6), -round(kv[1]["recall5"], 6), kv[1]["w"], str(kv[1]["guncel"]))
    en_iyi = sorted(ozet.items(), key=sira)[0]
    en_iyi_sabit = sorted([kv for kv in ozet.items() if kv[1]["guncel"] is False], key=sira)[0]  # GEN_AGIRLIK sabiti yalnız yüzeysiz ayarlardan seçilir
    mevcut = ozet.get("gen=%g" % fts.GEN_AGIRLIK)
    degistir = bool(mevcut and en_iyi_sabit[1]["ndcg10"] >= mevcut["ndcg10"] and en_iyi_sabit[1].get("bg_recall5", 0) >= mevcut.get("bg_recall5", 0) and en_iyi_sabit[1]["w"] != fts.GEN_AGIRLIK)
    # ---- (b) çekimserlik eşiği ----
    ev = [json.loads(l) for l in open(os.path.join(repo, "veri", "erisim-eval.jsonl"), encoding="utf-8") if l.strip()]
    esikler = []
    for m in ("vektor-e5", "vektor-bge", "vektor-e5-i8", "vektor-bge-i8", "fts5+gen"):
        rows = [r for r in ev if r.get("yontem") == m and r.get("top1_skor") is not None]
        if not rows:
            continue
        son_head = rows[-1].get("head"); rows = [r for r in rows if r.get("head") == son_head]
        neg = sorted(r["top1_skor"] for r in rows if r["yetenek"] == "cekimserlik")          # cevapsız: uzak/kötü skor beklenir
        poz = sorted(r["top1_skor"] for r in rows if r["yetenek"] != "cekimserlik" and r.get("recall5") == 1)
        if not neg or not poz:
            continue
        # vektörde uzaklık: cevapsız BÜYÜK; bm25 (negatif): iyi eşleşme daha KÜÇÜK (daha negatif) → cevapsız BÜYÜK. İki halde de kural: skor ≥ t → çekimser.
        adaylar = sorted(set(neg + poz)); best = None
        for t in adaylar:
            yak = sum(1 for x in neg if x >= t) / len(neg); kor = sum(1 for x in poz if x < t) / len(poz); ba = 0.5 * (yak + kor)
            if best is None or ba > best[1] + 1e-12:
                best = (t, ba, yak, kor)
        esikler.append({"yontem": m, "head": son_head, "n_cevapsiz": len(neg), "n_isabet": len(poz), "cevapsiz_medyan": round(neg[len(neg) // 2], 4), "isabet_medyan": round(poz[len(poz) // 2], 4),
                        "esik": round(best[0], 4), "dengeli_dogruluk": round(best[1], 3), "cevapsiz_yakalama": round(best[2], 3), "isabet_koruma": round(best[3], 3), "damga": "öneri [?] n küçük; kural: top1 skor ≥ eşik → çekimser"})
    gd = os.path.join(repo, "veri", "gorunum")
    with open(os.path.join(gd, "v_erisim_kalibrasyon.csv"), "w", encoding="utf-8", newline="") as fh:
        w_ = csv.DictWriter(fh, fieldnames=["ayar", "gen_agirlik", "guncel_yuzey", "yetenek", "n", "recall5", "mrr", "ndcg10", "ort_sure_ms"], lineterminator="\n"); w_.writeheader(); w_.writerows(satirlar)
    with open(os.path.join(gd, "v_erisim_cekimserlik.csv"), "w", encoding="utf-8", newline="") as fh:
        w_ = csv.DictWriter(fh, fieldnames=list(esikler[0].keys()) if esikler else ["yontem"], lineterminator="\n"); w_.writeheader(); w_.writerows(esikler)
    with open(os.path.join(repo, "veri", "erisim-kalibrasyon.jsonl"), "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"ts": ts, "git_head": head, "grid": grid, "mevcut_w": fts.GEN_AGIRLIK, "en_iyi": en_iyi[0], "en_iyi_ndcg10": round(en_iyi[1]["ndcg10"], 3), "en_iyi_recall5": round(en_iyi[1]["recall5"], 3), "en_iyi_sabit": en_iyi_sabit[0],
                             "mevcut_ndcg10": round(mevcut["ndcg10"], 3) if mevcut else None, "degistir_onerisi": degistir, "cekimserlik": esikler, "llm": "yok"}, ensure_ascii=False) + "\n")
    if not a.sessiz:
        print("erisim-kalibrasyon @ %s · %d ayar × %d soru · LLM yok" % (head, len(ozet), len(sorular)))
        for ad, o in sorted(ozet.items(), key=lambda kv: (kv[1]["w"], str(kv[1]["guncel"]))):
            print("  %-14s recall@5 %.3f · MRR %.3f · nDCG@10 %.3f · bilgi-guncelleme r@5 %.3f%s" % (ad, o["recall5"], o["mrr"], o["ndcg10"], o.get("bg_recall5", 0), "   ← mevcut" if ad == "gen=%g" % fts.GEN_AGIRLIK else ""))
        print("  EN İYİ (nDCG→recall→küçük w): %s · yüzeysiz en iyi: %s · GEN_AGIRLIK %g→%g önerisi: %s" % (en_iyi[0], en_iyi_sabit[0], fts.GEN_AGIRLIK, en_iyi_sabit[1]["w"], "EVET (kural: nDCG ∧ bilgi-guncelleme ≥ mevcut)" if degistir else "HAYIR (kural sağlanmadı)"))
        for e in esikler:
            print("  çekimserlik %-13s cevapsız medyan %.3f ↔ isabet %.3f · eşik %.3f · dengeli doğruluk %.3f (yakalama %.2f · koruma %.2f) n=%d/%d" % (e["yontem"], e["cevapsiz_medyan"], e["isabet_medyan"], e["esik"], e["dengeli_dogruluk"], e["cevapsiz_yakalama"], e["isabet_koruma"], e["n_cevapsiz"], e["n_isabet"]))
    con.close(); return 0


if __name__ == "__main__":
    sys.exit(main())
