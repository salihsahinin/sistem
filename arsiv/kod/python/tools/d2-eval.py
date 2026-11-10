#!/usr/bin/env python3
"""d2-eval.py — D2 MİNİ-EVAL harness'i (İB-49; KB-60 a / Karar 67 G3): LLM'in .d2 ÜRETME ve GRAF OKUMA doğruluğunu DETERMİNİSTİK ölçer.
STDLIB ONLY + `d2` ikilisi (derleme). LLM çağırmaz; işçi çıktıları dosya olarak verilir (cc/d2-eval/*). Literatürde D2 benchmark yok → Jarvis'e özgü.

(a) ÜRETİM: `--uretim <dosya.d2>` — d2 derleme çıkış kodu (`d2 --layout=elk`), D2 metninden kenar kümesi ({(kaynak,hedef)}; `a -> b` ve `a -> b: etiket`)
    ve düğüm kümesi ayrıştırılır; model JSON'undaki (veri/graf/pointer-sistemi-model.json) kenar kümesiyle SİMETRİK FARK: eksik / fazla / precision / recall.
    Düğüm kimliği eşlemesi: model id `tablo:kayit` ↔ D2 kimliği `tablo_kayit` (':' → '_', '-'/'.' → '_'); işçiye aynı kural yazılır.
(b) OKUMA: `--sorular` yapısal soruların DOĞRU cevaplarını üretir (b1: kenar-listesi/model JSON'dan · b2: silver SQL'den); `--okuma <cevap.json> --kol b1|b2`
    işçi cevabını doğru cevapla kıyaslar (normalize: küçük harf, boşluk, sayı). `--sql <sql.json>` işçinin yazdığı SQL'i silver'da (salt-okur) YÜRÜTÜR, sonucu
    b2 doğru cevabıyla kıyaslar (LLM SQL yazar / motor yürütür kolu).
(c) HAKEM: harness A/B hakemliği yapmaz (LLM işi; yalnız tercih, mutlak puan yok — Karar 67); `--kaydet` ile tercih satırı kütüğe girer.
Kütük: veri/d2-eval.jsonl (append-only; 1 satır = 1 ölçüm olgusu {kol, kosum, deger…}) · gold veri/gorunum/v_d2_eval.csv (özet).
Kullanım: python3 tools/d2-eval.py --uretim cc/d2-eval/uretim-1.d2 [--kosum u1] · --sorular · --okuma cc/d2-eval/okuma-1.json --kol b1 · --sql cc/d2-eval/sql-1.json
          · --kaydet '{"kol":"c","a":"uretim-1","b":"uretim-2","tercih":"A","hakem":"sonnet"}' · --ozet
Çıkış: 0 · 2 girdi yok · 3 d2 derleme hatası (uretim kolunda; kütüğe yine yazılır). Deneysel m.29 (2026-08-29, Jarvis, yan icra P4).
"""
import argparse, csv, json, os, re, sqlite3, subprocess, sys, tempfile
from datetime import datetime, timezone, timedelta

RX_KENAR = re.compile(r"^\s*([A-Za-z0-9_.\-]+)\s*(?:->|<-|<->)\s*([A-Za-z0-9_.\-]+)\s*(?::\s*([^{]*?))?\s*\{?\s*$")
RX_DUGUM = re.compile(r"^\s*([A-Za-z0-9_.\-]+)\s*(?::[^{]*)?\{?\s*$")


def repo_kok():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def d2id(model_id):
    return re.sub(r"[^A-Za-z0-9_]", "_", model_id)


def model_kume(repo):
    m = json.load(open(os.path.join(repo, "veri", "graf", "pointer-sistemi-model.json"), encoding="utf-8"))
    nodes = {n["id"] for n in m["nodes"]}; edges = {(e["from"], e["to"], e["type"]) for e in m["edges"]}
    # kenar kümesi ÜÇLÜ (kaynak, hedef, tip): aynı çift iki tipte olabilir (tablo:kayit→tablo:dosya fk ∧ wasRevisionOf) — çift-grain 58→57 çökertiyordu (08-29)
    return m, {d2id(n) for n in nodes}, {(d2id(a), d2id(b), t) for a, b, t in edges}


def d2_ayristir(metin):
    kenar, dugum = set(), set()
    for s in metin.split("\n"):
        t = s.strip()
        if not t or t.startswith("#") or t.startswith("//"):
            continue
        m = RX_KENAR.match(t)
        if m:
            a, b = m.group(1), m.group(2); tip = (m.group(3) or "").strip().strip('"').strip()
            kenar.add((a, b, tip)); dugum.update((a, b)); continue
        m = RX_DUGUM.match(t)
        if m and m.group(1) not in ("direction", "vars", "classes", "style", "shape", "label", "tooltip", "link"):
            dugum.add(m.group(1))
    return dugum, kenar


def derle(yol):
    with tempfile.TemporaryDirectory() as td:
        r = subprocess.run(["d2", "--layout=elk", yol, os.path.join(td, "o.svg")], capture_output=True, text=True, timeout=120)
    return r.returncode, (r.stderr or "")[-300:]


def kaydet(repo, satir):
    satir = {"ts": datetime.now(timezone(timedelta(hours=3))).replace(microsecond=0).isoformat(),
             "git_head": subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip(), **satir}
    with open(os.path.join(repo, "veri", "d2-eval.jsonl"), "a", encoding="utf-8") as fh:
        fh.write(json.dumps(satir, ensure_ascii=False) + "\n")
    return satir


def sorular(repo):
    """Yapısal sorular + DOĞRU cevaplar. b1: kenar listesi / model JSON'dan (işçi kenar listesini okur). b2: silver SQL'den (işçi SQL yazar)."""
    m, _, _ = model_kume(repo)
    cik = {}
    for e in m["edges"]:
        cik[e["from"]] = cik.get(e["from"], 0) + 1
    b1 = {
        "B1-1": ("Grafta 'referans_turu' türünde kaç düğüm var?", str(sum(1 for n in m["nodes"] if n["kind"] == "referans_turu"))),
        "B1-2": ("'tablo:kayit' düğümüne GİREN (hedefi tablo:kayit olan) kaç kenar var?", str(sum(1 for e in m["edges"] if e["to"] == "tablo:kayit"))),
        "B1-3": ("En çok ÇIKAN kenara sahip düğümün id'si nedir?", max(cik, key=lambda k: (cik[k], k))),
        "B1-4": ("Tipi 'pointer_hedef' olan kaç kenar var?", str(sum(1 for e in m["edges"] if e["type"] == "pointer_hedef"))),
        "B1-5": ("Tipi 'wasRevisionOf' olan kaç kenar var ve hangi düğümlerden çıkar? (sayı, ardından kaynak id'leri alfabetik, virgülle)",
                 "%d,%s" % (sum(1 for e in m["edges"] if e["type"] == "wasRevisionOf"), ",".join(sorted({e["from"] for e in m["edges"] if e["type"] == "wasRevisionOf"})))),
    }
    con = sqlite3.connect("file:%s?mode=ro" % os.path.join(repo, "veri", "baglam.sqlite"), uri=True)
    q = lambda s: con.execute(s).fetchone()
    b2 = {
        "B2-1": ("silver'da kaç farklı referans türü (referans.ref_turu) var?", str(q("SELECT count(DISTINCT ref_turu) FROM referans")[0])),
        "B2-2": ("ref_turu='dosya_pointer' olup hedefi çözülemeyen (hedef_var=0) kaç referans var?", str(q("SELECT count(*) FROM referans WHERE ref_turu='dosya_pointer' AND hedef_var=0")[0])),
        "B2-3": ("En çok referansı olan ref_turu hangisi?", q("SELECT ref_turu FROM referans GROUP BY 1 ORDER BY count(*) DESC, 1 LIMIT 1")[0]),
        "B2-4": ("bag tablosunda kaç satır var?", str(q("SELECT count(*) FROM bag")[0])),
        "B2-5": ("bag tablosunda kural='R1' olan kaç satır var?", str(q("SELECT count(*) FROM bag WHERE kural='R1'")[0])),
    }
    con.close()
    return b1, b2


def norm(x):
    return re.sub(r"[\s'\"`]+", "", str(x)).lower()


def main():
    ap = argparse.ArgumentParser(description="D2 mini-eval harness (İB-49)")
    ap.add_argument("--repo", default=repo_kok()); ap.add_argument("--uretim"); ap.add_argument("--kosum", default=None)
    ap.add_argument("--sorular", action="store_true"); ap.add_argument("--okuma"); ap.add_argument("--kol", default="b1"); ap.add_argument("--sql")
    ap.add_argument("--kaydet"); ap.add_argument("--ozet", action="store_true"); ap.add_argument("--sessiz", action="store_true")
    a = ap.parse_args(); repo = os.path.abspath(a.repo)
    if a.sorular:
        b1, b2 = sorular(repo)
        print(json.dumps({"b1": {k: {"soru": s, "cevap": c} for k, (s, c) in b1.items()}, "b2": {k: {"soru": s, "cevap": c} for k, (s, c) in b2.items()}}, ensure_ascii=False, indent=1)); return 0
    if a.uretim:
        yol = os.path.join(repo, a.uretim)
        if not os.path.exists(yol):
            print("HATA: yok: %s" % a.uretim, file=sys.stderr); return 2
        _, mdugum, mkenar = model_kume(repo)
        metin = open(yol, encoding="utf-8").read()
        kod, err = derle(yol); dugum, kenar = d2_ayristir(metin)
        eksik = mkenar - kenar; fazla = kenar - mkenar; ortak = kenar & mkenar
        prec = len(ortak) / len(kenar) if kenar else 0.0; rec = len(ortak) / len(mkenar) if mkenar else 0.0
        s = kaydet(repo, {"kol": "a-uretim", "kosum": a.kosum or os.path.basename(a.uretim), "dosya": a.uretim, "derleme_kodu": kod, "derleme_hata": err if kod else "",
                          "dugum_llm": len(dugum), "dugum_model": len(mdugum), "kenar_llm": len(kenar), "kenar_model": len(mkenar), "ortak": len(ortak), "eksik": len(eksik), "fazla": len(fazla),
                          "precision": round(prec, 3), "recall": round(rec, 3), "simetrik_fark": len(eksik) + len(fazla), "byte": len(metin.encode("utf-8"))})
        if not a.sessiz:
            print("üretim %s: derleme %s · kenar llm %d / model %d · ortak %d · eksik %d · fazla %d · P %.3f R %.3f · sim.fark %d" % (s["kosum"], "OK" if kod == 0 else "HATA(%d)" % kod, len(kenar), len(mkenar), len(ortak), len(eksik), len(fazla), prec, rec, len(eksik) + len(fazla)))
        return 3 if kod else 0
    if a.okuma or a.sql:
        b1, b2 = sorular(repo); dogru = b1 if a.kol == "b1" else b2
        yol = os.path.join(repo, a.okuma or a.sql)
        cev = json.load(open(yol, encoding="utf-8"))
        if a.sql:
            con = sqlite3.connect("file:%s?mode=ro" % os.path.join(repo, "veri", "baglam.sqlite"), uri=True); dogru = b2; sonuc = {}
            for k in dogru:
                sqltxt = cev.get(k, "")
                try:
                    r = con.execute(sqltxt).fetchone(); sonuc[k] = str(r[0]) if r else ""
                except Exception as e:
                    sonuc[k] = "HATA:" + str(e)[:60]
            con.close(); cev = sonuc; kol = "b2-sql"
        else:
            kol = a.kol + "-okuma"
        dogru_n = sum(1 for k, (_, c) in dogru.items() if norm(cev.get(k, "")) == norm(c))
        s = kaydet(repo, {"kol": kol, "kosum": a.kosum or os.path.basename(yol), "dosya": a.okuma or a.sql, "dogru": dogru_n, "toplam": len(dogru), "dogruluk": round(dogru_n / len(dogru), 3),
                          "ayrinti": {k: {"beklenen": c, "verilen": str(cev.get(k, ""))[:80], "ok": norm(cev.get(k, "")) == norm(c)} for k, (_, c) in dogru.items()}})
        if not a.sessiz:
            print("%s %s: %d/%d doğru" % (kol, s["kosum"], dogru_n, len(dogru)))
            for k, v in s["ayrinti"].items():
                if not v["ok"]:
                    print("   ✗ %s beklenen=%s verilen=%s" % (k, v["beklenen"], v["verilen"]))
        return 0
    if a.kaydet:
        s = kaydet(repo, json.loads(a.kaydet)); print("kaydedildi:", s.get("kol"), s.get("kosum") or s.get("a")); return 0
    if a.ozet:
        rows = [json.loads(l) for l in open(os.path.join(repo, "veri", "d2-eval.jsonl"), encoding="utf-8") if l.strip()]
        oz = {}
        for r in rows:
            o = oz.setdefault(r["kol"], {"n": 0, "derleme_ok": 0, "prec": 0.0, "rec": 0.0, "dogruluk": 0.0, "tercih_A": 0})
            o["n"] += 1
            if r["kol"] == "a-uretim":
                o["derleme_ok"] += 1 if r["derleme_kodu"] == 0 else 0; o["prec"] += r["precision"]; o["rec"] += r["recall"]
            elif r["kol"].endswith("okuma") or r["kol"] == "b2-sql":
                o["dogruluk"] += r["dogruluk"]
            elif r["kol"] == "c-hakem":
                o["tercih_A"] += 1 if r.get("tercih") == "A" else 0
        gd = os.path.join(repo, "veri", "gorunum")
        with open(os.path.join(gd, "v_d2_eval.csv"), "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh, lineterminator="\n"); w.writerow(["kol", "n", "derleme_ok", "ort_precision", "ort_recall", "ort_dogruluk", "tercih_A"])
            for k, o in sorted(oz.items()):
                n = o["n"]; w.writerow([k, n, o["derleme_ok"], round(o["prec"] / n, 3) if k == "a-uretim" else "", round(o["rec"] / n, 3) if k == "a-uretim" else "", round(o["dogruluk"] / n, 3) if (k.endswith("okuma") or k == "b2-sql") else "", o["tercih_A"] if k == "c-hakem" else ""])
        print(open(os.path.join(gd, "v_d2_eval.csv"), encoding="utf-8").read()); return 0
    ap.print_help(); return 2


if __name__ == "__main__":
    sys.exit(main())
