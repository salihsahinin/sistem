#!/usr/bin/env python3
"""erisim-vektor.py — VEKTÖR ÖLÇÜM KOLU (İB-47; KB-59 a / Karar 66; Karar 74 M-2 a tetik). İB-43 FTS5 eval'ine vektör + RRF kolu ekler.
Yorumlayıcı: repo-içi `.venv/bin/python` (sentence-transformers · torch · sqlite-vec; Karar 63 venv deseni). Stdlib python ile koşarsa çıkış 4.

Şartname (İB-47 icra metni, birebir):
  (1) yerel gömücü multilingual-e5-large (1024d; "passage:"/"query:" önekleri) + bge-m3 YAN YANA (1024d, öneksiz) — API gömücü YASAK.
  (2) sqlite-vec v0.1.9 vec0 tam brute-force KNN (ANN/alpha KAPALI; vec0 MATCH = tam tarama, 0.1.x'te ANN yok) — indeks dosyası veri/erisim-vektor.sqlite (gitignore, türev).
  (3) RRF sabit k=60 (Cormack 2009 varsayılanı; ağırlık uydurma YOK): fts5+gen ilk 50 ⊕ vektör ilk 50 → sıra füzyonu; kural-tabanlı anahtar zenginleştirme = FTS tarafının `genisletme` kolonu (zaten kural-tabanlı).
  (4) aynı altın-soru kümesi (veri/sozlesme/erisim-eval-sorular.jsonl, n=100; 5 yetenek) ile FTS5-tek · vektör · RRF kıyası — nDCG@10 / recall@5 / MRR dosya grain'inde;
      etki büyüklüğü = ortalama fark + bootstrap %95 GA (n=2000, sabit tohum 0 — deterministik). ranx KURULMADI (numba bağımlılığı; formüller burada, stdlib).
  (5) DETERMİNİZM testi: aynı korpus iki gömme koşumu → vektör byte'larının sha256'sı EŞİT ∧ 100 sorunun sıralaması EŞİT; cihaz (cpu/mps) kayda düşer.
  (6) maliyet: ms/sorgu (gömme + KNN ayrı), sorgu token sayısı; int8 retention = int8'e nicemlenmiş vektörle recall@5 / float32 recall@5.
  (7) YASAK: API gömücü · ANN indeksi · LLM-rerank/router (Karar 65).
Grain: veri/erisim-eval.jsonl'e erisim-fts ile AYNI şemada satır (yontem ∈ {vektor-e5, vektor-bge, vektor-e5-i8, rrf-e5, rrf-bge}); özet veri/gorunum/v_erisim_vektor.csv;
gömme üretim kaydı veri/gorunum/v_erisim_vektor_gomme.csv (model · sürüm · dim · n · cihaz · sha256 · sn · determinizm).
Kullanım: .venv/bin/python tools/erisim-vektor.py --gom [--model e5,bge] [--cihaz auto|cpu|mps] [--sinir N]   (korpus gömme; idempotent üstüne-yazma)
          .venv/bin/python tools/erisim-vektor.py --eval [--model e5,bge]                                       (100 soru × yöntem)
          .venv/bin/python tools/erisim-vektor.py --determinizm [--model e5] [--sinir 1000]                     (iki koşum bit-eşitliği + sıra eşitliği)
          .venv/bin/python tools/erisim-vektor.py --probe 256                                                     (hız + cihaz bit-eşitliği ön-ölçümü; yazmaz)
Çıkış: 0 · 2 girdi yok · 4 bağımlılık yok. Deneysel m.29 (2026-08-29, Jarvis, yan icra oturumu P2). Kayıt: tools/SCRIPTLER.md.
"""
import argparse, csv, hashlib, importlib.util, json, math, os, random, sqlite3, subprocess, sys, time
from datetime import datetime, timezone, timedelta

MODELLER = {"e5": ("intfloat/multilingual-e5-large", "query: ", "passage: "), "bge": ("BAAI/bge-m3", "", "")}
RRF_K = 60; ADAY = 50; METIN_SINIR = 2000; BOOT_N = 2000; BOOT_TOHUM = 0


def repo_kok():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def yukle_fts(repo):
    yol = os.path.join(repo, "tools", "erisim-fts.py")
    spec = importlib.util.spec_from_file_location("erisim_fts", yol); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def bagimliliklar():
    try:
        import sqlite_vec, sentence_transformers, torch  # noqa
        return sqlite_vec, sentence_transformers, torch
    except ImportError as e:
        print("HATA: bağımlılık yok (%s) — .venv/bin/pip install sentence-transformers sqlite-vec; yorumlayıcı .venv/bin/python (Karar 63)" % e, file=sys.stderr)
        sys.exit(4)


def vec_db(repo, sqlite_vec):
    yol = os.path.join(repo, "veri", "erisim-vektor.sqlite")
    con = sqlite3.connect(yol); con.enable_load_extension(True); sqlite_vec.load(con); con.enable_load_extension(False)
    con.execute("CREATE TABLE IF NOT EXISTS gomme_uretim (model TEXT, model_id TEXT, st_surum TEXT, torch_surum TEXT, dim INTEGER, n INTEGER, cihaz TEXT, "
                "sha256 TEXT, sure_sn REAL, git_head TEXT, uretim_ts TEXT, metin_sinir INTEGER, not_ TEXT)")
    return con


def korpus(repo, sinir=None):
    con = sqlite3.connect(os.path.join(repo, "veri", "baglam.sqlite"))
    sql = "SELECT g.kayit_id, g.dosya_id, g.katman, COALESCE(k.metin,'') FROM erisim_genisletme g JOIN kayit k ON k.kayit_id=g.kayit_id ORDER BY g.kayit_id"
    rows = con.execute(sql + (" LIMIT %d" % sinir if sinir else "")).fetchall(); con.close()
    return [(r[0], r[1], r[2], r[3][:METIN_SINIR]) for r in rows]


def cihaz_sec(torch, istek):
    if istek != "auto":
        return istek
    return "mps" if torch.backends.mps.is_available() else "cpu"


def model_yukle(st, ad, cihaz, torch):
    torch.manual_seed(0)
    m = st.SentenceTransformer(MODELLER[ad][0], device=cihaz); m.max_seq_length = 512
    return m


def gom(model, metinler, onek, toplu=32):
    import numpy as np
    v = model.encode([onek + t for t in metinler], batch_size=toplu, normalize_embeddings=True, convert_to_numpy=True, show_progress_bar=False)
    return np.ascontiguousarray(v.astype("float32"))


def sha(v):
    return hashlib.sha256(v.tobytes()).hexdigest()


def int8_nicemle(v):
    import numpy as np
    return np.clip(np.round(v * 127.0), -127, 127).astype("int8")


def gom_yaz(repo, ad, cihaz, sinir, sessiz):
    sqlite_vec, st, torch = bagimliliklar()
    import numpy as np
    K = korpus(repo, sinir); onek = MODELLER[ad][2]
    onbellek = os.path.join(repo, "veri", "erisim-vektor-%s.npy" % ad)  # gitignore'lu ara ürün: yazım çökerse 1 saatlik gömme yeniden hesaplanmaz (08-29 vakası)
    t0 = time.time(); V = None
    if os.path.exists(onbellek) and sinir is None:
        Vc = np.load(onbellek)
        if Vc.shape[0] == len(K):
            V = np.ascontiguousarray(Vc.astype("float32")); sure = 0.0
            if not sessiz:
                print("[%s] AŞAMA 1/4 gömme: ÖNBELLEKTEN (%s, %d×%d) — yeniden hesaplanmadı" % (ad, os.path.relpath(onbellek, repo), V.shape[0], V.shape[1]), flush=True)
    if V is None:
        model = model_yukle(st, ad, cihaz, torch); parcalar = []
        if not sessiz:
            print("[%s] AŞAMA 1/4 gömme: model %s · cihaz %s · %d kayıt · parça 512 · max_seq 512 · normalize" % (ad, MODELLER[ad][0], cihaz, len(K)), flush=True)
        for i in range(0, len(K), 512):
            parcalar.append(gom(model, [r[3] for r in K[i:i + 512]], onek))
            if not sessiz:
                bitti = min(i + 512, len(K)); gecen = time.time() - t0; hiz = bitti / max(gecen, 1e-6)
                print("  [%s] %6d/%d · %5.1f%% · %.0f sn · %.1f kayıt/sn · kalan ~%.0f sn" % (ad, bitti, len(K), 100.0 * bitti / len(K), gecen, hiz, (len(K) - bitti) / max(hiz, 1e-6)), flush=True)
        V = np.vstack(parcalar); sure = time.time() - t0
        if sinir is None:
            np.save(onbellek, V)
    h = sha(V); V8 = int8_nicemle(V)
    if not sessiz:
        print("[%s] AŞAMA 2/4 sha256 + int8 nicemleme: %s… · %d×%d · önbellek %s" % (ad, h[:12], V.shape[0], V.shape[1], os.path.relpath(onbellek, repo)), flush=True)
        print("[%s] AŞAMA 3/4 sqlite-vec yazımı: vec_%s (float32) · vec_%s_i8 (int8, vec_int8()) · meta_%s" % (ad, ad, ad, ad), flush=True)
    con = vec_db(repo, sqlite_vec)
    for t in ("vec_%s" % ad, "vec_%s_i8" % ad, "meta_%s" % ad):
        con.execute("DROP TABLE IF EXISTS %s" % t)
    con.execute("CREATE VIRTUAL TABLE vec_%s USING vec0(kayit_id TEXT PRIMARY KEY, gomme float[%d])" % (ad, V.shape[1]))
    con.execute("CREATE VIRTUAL TABLE vec_%s_i8 USING vec0(kayit_id TEXT PRIMARY KEY, gomme int8[%d])" % (ad, V.shape[1]))
    con.execute("CREATE TABLE meta_%s (kayit_id TEXT PRIMARY KEY, dosya_id TEXT, katman TEXT)" % ad)
    con.executemany("INSERT INTO vec_%s (kayit_id, gomme) VALUES (?, ?)" % ad, [(K[i][0], V[i].tobytes()) for i in range(len(K))]); con.commit()
    # int8 sütunu ham blob kabul etmez: vec_int8() sarmalayıcısı şart (08-29 ilk koşum bu satırda düştü: "expected int8, float32 provided")
    con.executemany("INSERT INTO vec_%s_i8 (kayit_id, gomme) VALUES (?, vec_int8(?))" % ad, [(K[i][0], V8[i].tobytes()) for i in range(len(K))]); con.commit()
    con.executemany("INSERT INTO meta_%s VALUES (?,?,?)" % ad, [(r[0], r[1], r[2]) for r in K])
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip()
    ts = datetime.now(timezone(timedelta(hours=3))).replace(microsecond=0).isoformat()
    con.execute("INSERT INTO gomme_uretim VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (ad, MODELLER[ad][0], st.__version__, torch.__version__, int(V.shape[1]), len(K), cihaz, h, round(sure, 1), head, ts, METIN_SINIR,
                                                                              "normalize=True · max_seq 512 · batch 32 · sıra kayit_id ASC · torch.manual_seed(0)"))
    con.commit(); con.close()
    if not sessiz:
        print("[%s] AŞAMA 4/4 üretim kaydı (gomme_uretim) yazıldı" % ad, flush=True)
        print("gömme %s: n=%d dim=%d cihaz=%s %.0f sn (%.1f kayıt/sn) sha256=%s… → veri/erisim-vektor.sqlite" % (ad, len(K), V.shape[1], cihaz, sure, len(K) / max(sure, 1e-6), h[:12]), flush=True)
    return h


def probe(repo, n):
    sqlite_vec, st, torch = bagimliliklar()
    K = korpus(repo, n)
    for ad in ("e5", "bge"):
        for cihaz in (["mps", "cpu"] if torch.backends.mps.is_available() else ["cpu"]):
            model = model_yukle(st, ad, cihaz, torch); onek = MODELLER[ad][2]
            t0 = time.time(); a = gom(model, [r[3] for r in K], onek); s1 = time.time() - t0
            b = gom(model, [r[3] for r in K], onek)
            print("probe %s %-3s n=%d: %.1f sn (%.1f kayıt/sn) · iki koşum bit-eşit: %s · maks |Δ| %.2e" % (ad, cihaz, n, s1, n / s1, sha(a) == sha(b), float(abs(a - b).max())))


def knn(con, ad, q, k, i8=False):
    t = "vec_%s%s" % (ad, "_i8" if i8 else "")
    vec = int8_nicemle(q).tobytes() if i8 else q.astype("float32").tobytes()
    sarmal = "vec_int8(?)" if i8 else "?"
    rows = con.execute("SELECT v.kayit_id, v.distance, m.dosya_id FROM %s v JOIN meta_%s m ON m.kayit_id=v.kayit_id WHERE v.gomme MATCH %s AND k = ? ORDER BY v.distance" % (t, ad, sarmal), (vec, k)).fetchall()
    return [(r[0], r[2], r[1]) for r in rows]


def rrf(listeler, k=RRF_K):
    puan = {}
    for L in listeler:
        for i, kid in enumerate(L, 1):
            puan[kid] = puan.get(kid, 0.0) + 1.0 / (k + i)
    return sorted(puan, key=lambda x: (-puan[x], x))


def dosya_sirasi(kayit_dosya):
    """kayit listesi → tekil dosya listesi (ilk görülme sırası)."""
    out = []
    for _, d in kayit_dosya:
        if d not in out:
            out.append(d)
    return out


def metrik(dosyalar, bek):
    if not bek:
        return None, None, None
    isabet = next((i + 1 for i, d in enumerate(dosyalar) if d in bek), None)
    r5 = 1 if (isabet and isabet <= 5) else 0; mrr = 1.0 / isabet if isabet else 0.0
    dcg = sum(1.0 / math.log2(i + 2) for i, d in enumerate(dosyalar[:10]) if d in bek)
    idcg = sum(1.0 / math.log2(i + 2) for i in range(min(len(bek), 10)))
    return r5, mrr, (dcg / idcg if idcg else 0.0)


def bootstrap_fark(a, b):
    """a, b: soru-bazlı aynı sırada metrik listeleri → (ortalama fark a-b, %95 GA alt, üst); sabit tohum → deterministik."""
    rnd = random.Random(BOOT_TOHUM); n = len(a); farklar = [x - y for x, y in zip(a, b)]
    orta = sum(farklar) / n; ornek = []
    for _ in range(BOOT_N):
        s = sum(farklar[rnd.randrange(n)] for _ in range(n)) / n; ornek.append(s)
    ornek.sort(); return orta, ornek[int(0.025 * BOOT_N)], ornek[int(0.975 * BOOT_N) - 1]


def eval_kos(repo, modeller, cihaz, sessiz):
    sqlite_vec, st, torch = bagimliliklar()
    fts = yukle_fts(repo)
    sorular, hata = fts.sorulari_oku(repo)
    if hata:
        print("HATA: soru seti şeması: %s" % hata[:3], file=sys.stderr); return 2
    bcon = sqlite3.connect(os.path.join(repo, "veri", "baglam.sqlite")); vcon = vec_db(repo, sqlite_vec)
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip()
    ts = datetime.now(timezone(timedelta(hours=3))).replace(microsecond=0).isoformat()
    kayit_dosya = dict(bcon.execute("SELECT kayit_id, dosya_id FROM kayit").fetchall())
    sonuc = []; per = {}
    def kaydet(s, ad, dosyalar, sure, ekstra=None):
        bek = s.get("beklenen_dosya") or []; r5, mrr, ndcg = metrik(dosyalar, bek)
        isabet = next((i + 1 for i, d in enumerate(dosyalar) if d in bek), None) if bek else None
        row = {"ts": ts, "head": head, "soru_id": s["id"], "yetenek": s["yetenek"], "yontem": ad, "recall5": r5, "mrr": mrr, "isabet_sira": isabet,
               "sure_ms": round(sure, 2), "top1_dosya": dosyalar[0] if dosyalar else None, "top1_skor": (ekstra or {}).get("top1_skor"), "n_sonuc": len(dosyalar), "top5": dosyalar[:5], "ndcg10": ndcg}
        row.update(ekstra or {}); sonuc.append(row); per.setdefault(ad, {})[s["id"]] = (r5, mrr, ndcg)
    # FTS tarafı (aynı metrik koduyla; nDCG için yeniden koşulur)
    for s in sorular:
        for ad, kw in (("fts5", dict(genisletme=False, zaman_farkindali=False)), ("fts5+gen", dict(genisletme=True, zaman_farkindali=True))):
            t0 = time.perf_counter(); rows = fts.sorgula(bcon, s["soru"], ADAY, **kw)[0]; sure = (time.perf_counter() - t0) * 1000
            kaydet(s, ad, dosya_sirasi([(r[0], r[1]) for r in rows]), sure, {"top1_skor": rows[0][4] if rows else None})
    for ad in modeller:
        if not vcon.execute("SELECT COUNT(*) FROM sqlite_master WHERE name='vec_%s'" % ad).fetchone()[0]:
            print("UYARI: vec_%s yok — önce --gom --model %s" % (ad, ad), file=sys.stderr); continue
        model = model_yukle(st, ad, cihaz, torch); onek = MODELLER[ad][1]; tok = model.tokenizer
        for s in sorular:
            t0 = time.perf_counter(); q = gom(model, [s["soru"]], onek)[0]; t_gom = (time.perf_counter() - t0) * 1000
            n_tok = len(tok(onek + s["soru"])["input_ids"])
            t1 = time.perf_counter(); v = knn(vcon, ad, q, ADAY); t_knn = (time.perf_counter() - t1) * 1000
            kaydet(s, "vektor-%s" % ad, dosya_sirasi([(r[0], r[1]) for r in v]), t_gom + t_knn, {"top1_skor": v[0][2] if v else None, "gomme_ms": round(t_gom, 2), "knn_ms": round(t_knn, 2), "sorgu_token": n_tok})
            t2 = time.perf_counter(); v8 = knn(vcon, ad, q, ADAY, i8=True); t_i8 = (time.perf_counter() - t2) * 1000
            kaydet(s, "vektor-%s-i8" % ad, dosya_sirasi([(r[0], r[1]) for r in v8]), t_gom + t_i8, {"top1_skor": v8[0][2] if v8 else None, "knn_ms": round(t_i8, 2)})
            t3 = time.perf_counter(); f = fts.sorgula(bcon, s["soru"], ADAY, genisletme=True, zaman_farkindali=True)[0]
            fuz = rrf([[r[0] for r in f], [r[0] for r in v]]); t_rrf = (time.perf_counter() - t3) * 1000
            kaydet(s, "rrf-%s" % ad, dosya_sirasi([(kid, kayit_dosya.get(kid, "?")) for kid in fuz]), t_gom + t_knn + t_rrf, {"rrf_k": RRF_K, "aday": ADAY})
    # yaz: eval kütüğü (aynı şema, ek alanlar additive) + özet
    with open(os.path.join(repo, "veri", "erisim-eval.jsonl"), "a", encoding="utf-8") as fh:
        for r in sonuc:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    oz = []
    yont = sorted(per)
    for ad in yont:
        for yet in sorted({s["yetenek"] for s in sorular}) + ["TÜMÜ"]:
            ids = [s["id"] for s in sorular if (yet == "TÜMÜ" or s["yetenek"] == yet) and per[ad].get(s["id"], (None,))[0] is not None]
            if not ids:
                oz.append({"yontem": ad, "yetenek": yet, "n": sum(1 for s in sorular if yet == "TÜMÜ" or s["yetenek"] == yet), "recall5": "", "mrr": "", "ndcg10": "", "ort_sure_ms": round(sum(r["sure_ms"] for r in sonuc if r["yontem"] == ad and (yet == "TÜMÜ" or r["yetenek"] == yet)) / max(1, sum(1 for r in sonuc if r["yontem"] == ad and (yet == "TÜMÜ" or r["yetenek"] == yet))), 2)}); continue
            r5 = sum(per[ad][i][0] for i in ids) / len(ids); mrr = sum(per[ad][i][1] for i in ids) / len(ids); nd = sum(per[ad][i][2] for i in ids) / len(ids)
            sure = [r["sure_ms"] for r in sonuc if r["yontem"] == ad and (yet == "TÜMÜ" or r["yetenek"] == yet)]
            oz.append({"yontem": ad, "yetenek": yet, "n": len(sure), "recall5": round(r5, 3), "mrr": round(mrr, 3), "ndcg10": round(nd, 3), "ort_sure_ms": round(sum(sure) / len(sure), 2)})
    # etki büyüklüğü + GA (recall@5 ve nDCG@10; taban fts5+gen)
    taban = "fts5+gen"; ids = [s["id"] for s in sorular if per[taban].get(s["id"], (None,))[0] is not None]
    etki = []
    for ad in yont:
        if ad == taban or any(per[ad].get(i, (None,))[0] is None for i in ids):
            continue
        for mi, mad in ((0, "recall5"), (2, "ndcg10")):
            o, alt, ust = bootstrap_fark([per[ad][i][mi] for i in ids], [per[taban][i][mi] for i in ids])
            etki.append({"yontem": ad, "taban": taban, "metrik": mad, "n": len(ids), "fark": round(o, 3), "ga_alt": round(alt, 3), "ga_ust": round(ust, 3), "anlamli": "evet" if (alt > 0 or ust < 0) else "hayır", "boot_n": BOOT_N, "tohum": BOOT_TOHUM})
    gd = os.path.join(repo, "veri", "gorunum")
    with open(os.path.join(gd, "v_erisim_vektor.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["yontem", "yetenek", "n", "recall5", "mrr", "ndcg10", "ort_sure_ms"], lineterminator="\n"); w.writeheader(); w.writerows(oz)
    with open(os.path.join(gd, "v_erisim_vektor_etki.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["yontem", "taban", "metrik", "n", "fark", "ga_alt", "ga_ust", "anlamli", "boot_n", "tohum"], lineterminator="\n"); w.writeheader(); w.writerows(etki)
    with open(os.path.join(gd, "v_erisim_vektor_gomme.csv"), "w", encoding="utf-8", newline="") as fh:
        cur = vcon.execute("SELECT * FROM gomme_uretim ORDER BY uretim_ts"); w = csv.writer(fh, lineterminator="\n"); w.writerow([c[0] for c in cur.description]); w.writerows(cur.fetchall())
    if not sessiz:
        print("erisim-vektor eval @ %s · %d soru · yöntemler: %s" % (head, len(sorular), ", ".join(yont)))
        for o in oz:
            if o["yetenek"] == "TÜMÜ":
                print("  %-14s recall@5 %s · MRR %s · nDCG@10 %s · %s ms" % (o["yontem"], o["recall5"], o["mrr"], o["ndcg10"], o["ort_sure_ms"]))
        for e in etki:
            print("  etki %-14s %-8s fark %+.3f GA[%+.3f, %+.3f] %s" % (e["yontem"], e["metrik"], e["fark"], e["ga_alt"], e["ga_ust"], "ANLAMLI" if e["anlamli"] == "evet" else "—"))
    bcon.close(); vcon.close(); return 0


def determinizm(repo, ad, cihaz, sinir, sessiz):
    sqlite_vec, st, torch = bagimliliklar()
    K = korpus(repo, sinir); fts = yukle_fts(repo); sorular, _ = fts.sorulari_oku(repo)
    model = model_yukle(st, ad, cihaz, torch)
    a = gom(model, [r[3] for r in K], MODELLER[ad][2]); b = gom(model, [r[3] for r in K], MODELLER[ad][2])
    qa = gom(model, [s["soru"] for s in sorular], MODELLER[ad][1]); qb = gom(model, [s["soru"] for s in sorular], MODELLER[ad][1])
    import numpy as np
    sira_esit = all(list(np.argsort(-(a @ qa[i]))[:10]) == list(np.argsort(-(b @ qb[i]))[:10]) for i in range(len(sorular)))
    bit = sha(a) == sha(b) and sha(qa) == sha(qb)
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip()
    ts = datetime.now(timezone(timedelta(hours=3))).replace(microsecond=0).isoformat()
    con = vec_db(repo, sqlite_vec)
    con.execute("INSERT INTO gomme_uretim VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (ad + "-determinizm", MODELLER[ad][0], st.__version__, torch.__version__, int(a.shape[1]), len(K), cihaz, sha(a), None, head, ts, METIN_SINIR,
                                                                              "DETERMİNİZM: iki koşum bit-eşit=%s · 100 soru top-10 sıra eşit=%s · maks|Δ|=%.2e" % (bit, sira_esit, float(abs(a - b).max()))))
    con.commit(); con.close()
    if not sessiz:
        print("determinizm %s %s n=%d: bit-eşit %s · sıra eşit (top-10, %d soru) %s · maks|Δ| %.2e" % (ad, cihaz, len(K), bit, len(sorular), sira_esit, float(abs(a - b).max())))
    return 0 if (bit and sira_esit) else 3


def main():
    ap = argparse.ArgumentParser(description="vektör ölçüm kolu (İB-47)")
    ap.add_argument("--repo", default=repo_kok()); ap.add_argument("--model", default="e5,bge"); ap.add_argument("--cihaz", default="auto")
    ap.add_argument("--gom", action="store_true"); ap.add_argument("--eval", action="store_true"); ap.add_argument("--determinizm", action="store_true")
    ap.add_argument("--probe", type=int, default=0); ap.add_argument("--sinir", type=int, default=None); ap.add_argument("--sessiz", action="store_true")
    a = ap.parse_args(); repo = os.path.abspath(a.repo)
    if not os.path.exists(os.path.join(repo, "veri", "baglam.sqlite")):
        print("HATA: silver yok", file=sys.stderr); return 2
    _, _, torch = bagimliliklar(); cihaz = cihaz_sec(torch, a.cihaz); modeller = [m.strip() for m in a.model.split(",") if m.strip() in MODELLER]
    kod = 0
    if a.probe:
        probe(repo, a.probe)
    if a.gom:
        for ad in modeller:
            gom_yaz(repo, ad, cihaz, a.sinir, a.sessiz)
    if a.determinizm:
        for ad in modeller:
            kod = max(kod, determinizm(repo, ad, cihaz, a.sinir or 1000, a.sessiz))
    if a.eval:
        kod = max(kod, eval_kos(repo, modeller, cihaz, a.sessiz))
    return kod


if __name__ == "__main__":
    sys.exit(main())
