#!/usr/bin/env python3
"""erisim-fts.py — ERİŞİM KATMANI: SQLite FTS5 + bm25 sözcüksel arama + embedding'siz iki iyileştirme + İB-20 yerel eval (KB-43 (a) = Karar 60,
08-21; Karar 66 ölçüm-kolu şartnamesi; icra İB-43, 2026-08-22 seans-14). STDLIB ONLY (sqlite3 ENABLE_FTS5 şart; yoksa FAIL-LOUD çıkış 2).
LLM/embedding YOK; hibrit/vektör KARARI bu ölçümden SONRA masada (Beyan 9 baki). Deterministik: aynı silver + aynı soru seti → aynı sıralama/sayılar (süre hariç).

1. İNDEKS (silver additive; her katman-hatti koşumunda yeniden kurulur — baglam-tablo DB'yi sıfırdan yazar):
   - `erisim_genisletme` (1 satır = 1 kayit): `genisletme` = ANAHTAR GENİŞLETME metni — kayıt içindeki referans DEĞERLERİ (anahtar_terim · tuzuk_madde ·
     kart · skill_adi · v_no · wiki_link · etiket) + dosya başlığı + bölüm yolu + zaman (ay) — "indeks anahtarı = ham metin yerine çıkarılmış olgular"
     (LongMemEval A-YT6/C-YT3: recall@5 +%9,4 — transfer ÖLÇÜLMEMİŞ, burada ölçülür). `zaman` = kayit.tarih_iso ∨ dosya.son_commit[:10].
   - `kayit_fts` FTS5 sanal tablosu: (kayit_id UNINDEXED, dosya_id UNINDEXED, katman UNINDEXED, zaman UNINDEXED, gecerlilik UNINDEXED, metin, genisletme);
     tokenize = unicode61 remove_diacritics 2 (Türkçe aksan katlanır; ı/i ayrımı kaybolur — yazılı sınır). bm25 ağırlıkları: metin 1,0 · genisletme 2,0 (deneysel m.29).
2. SORGU (`--sorgu "..."` ∨ eval): sözcük-önek eşleme (≥4 harf → `kelime*`; Türkçe ek kuyruğu), FTS5 MATCH = sözcüklerin AND'i (boş dönerse OR'a düşer — FAIL-LOUD değil,
   "gevşetildi" damgası) · ZAMAN-FARKINDALI genişletme (A-YT6 +%6,8-11,3): sorguda açık tarih (YYYY-MM-DD ∨ MM-DD) → `zaman` filtresi ∨ metinde tarih dizesi;
   "güncel/son/şu an/bugün" → sıcak/ılık katman önce, sonra bm25. Sonuç: top-k (kayit_id · dosya · satır · bm25 · özet).
3. EVAL (İB-20, 5 yetenek — LongMemEval şablonu: bilgi-cikarma · cok-oturum · zamansal · bilgi-guncelleme · cekimserlik): `veri/sozlesme/erisim-eval-sorular.jsonl`
   (1 satır = 1 soru: soru · yetenek · beklenen_dosya[] (boş = çekimserlik) · beklenen_kayit_regex? · not) × yöntem ∈ {grep (taban: tüm sözcükler alt-dize AND,
   sıcak>ılık>soğuk, sonra dosya/sıra), fts5 (yalnız metin), fts5+gen (metin+genişletme+zaman), fts5+guncel (= fts5+gen ∧ v_guncel yüzeyi: sıcak/ılık ∧ gecerlilik=guncel — Karar 58 sinerjisi; boşsa tüm korpus)} → recall@5 (beklenen dosya top-5'te) · MRR · süre(ms) ·
   çekimserlikte top-1 skor (eşik kalibresi borç). Kütük `veri/erisim-eval.jsonl` APPEND-ONLY (1 satır = soru × yöntem × koşum) + gold `v_erisim_eval` CSV
   (yöntem × yetenek özet). COST tabanı = fts5 ↔ grep süre/recall (DE kanonu §1.3: tabanı geçmeyen eklenmez). Yöntem sütunu vektör/RRF kollarına AÇIK (İB-47).
Kullanım: python3 tools/erisim-fts.py [--repo <yol>] [--insa] [--eval [--taban]] [--sorgu "metin" [--k 5]] [--sessiz] [--kuru]  (bayraksız = --insa --eval; --taban = grep taban çizgisi de koşar)
Çıkış: 0 · 2 FTS5 yok/DB yok/soru dosyası yok · 3 eval testi ERROR (soru seti şema hatası). Deneysel m.29.
"""
import argparse, csv, json, os, re, sqlite3, subprocess, sys, time
from datetime import datetime, timezone

SORU_YOLU = "veri/sozlesme/erisim-eval-sorular.jsonl"
EVAL_LOG = "veri/erisim-eval.jsonl"
YETENEK = ("bilgi-cikarma", "cok-oturum", "zamansal", "bilgi-guncelleme", "cekimserlik")
GEN_REF_TURLERI = ("anahtar_terim", "tuzuk_madde", "kart", "skill_adi", "v_no", "wiki_link", "etiket")
KATMAN_ONCELIK = {"sicak": 0, "ilik": 1, "yapisal": 2, "soguk": 3}
ZAMAN_RX = re.compile(r"(?<!\d)(\d{4}-\d{2}-\d{2}|\d{2}-\d{2})(?!\d)")
GUNCEL_RX = re.compile(r"\b(güncel|guncel|son|şu an|su an|bugün|bugun|en yeni|şimdi|simdi)\b", re.I)
TR_FOLD = str.maketrans({"ı": "i", "İ": "i", "ğ": "g", "Ğ": "g", "ü": "u", "Ü": "u", "ş": "s", "Ş": "s", "ö": "o", "Ö": "o", "ç": "c", "Ç": "c"})


def fts5_var():
    c = sqlite3.connect(":memory:")
    try:
        c.execute("CREATE VIRTUAL TABLE t USING fts5(x)"); return True
    except sqlite3.Error:
        return False


def git_head(repo):
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "?"


def fold(s):
    return (s or "").translate(TR_FOLD).lower()


# ------------------------------------------------------------------ indeks
def insa(con):
    con.executescript("""
    DROP TABLE IF EXISTS erisim_genisletme;
    CREATE TABLE erisim_genisletme (kayit_id TEXT PRIMARY KEY, dosya_id TEXT, katman TEXT, zaman TEXT, genisletme TEXT, ref_sayisi INTEGER);
    INSERT INTO erisim_genisletme
      SELECT k.kayit_id, k.dosya_id, d.katman,
             COALESCE(NULLIF(k.tarih_iso,''), substr(d.son_commit,1,10)) AS zaman,
             TRIM(COALESCE(d.baslik,'') || ' ' || REPLACE(COALESCE(k.bolum_yolu,''), '/', ' ') || ' ' ||
                  COALESCE((SELECT GROUP_CONCAT(DISTINCT r.ref_deger) FROM referans r WHERE r.kayit_id=k.kayit_id
                            AND r.ref_turu IN ('anahtar_terim','tuzuk_madde','kart','skill_adi','v_no','wiki_link','etiket')), '') || ' ' ||
                  COALESCE(substr(NULLIF(k.tarih_iso,''),1,7), substr(d.son_commit,1,7), '')) AS genisletme,
             (SELECT COUNT(*) FROM referans r WHERE r.kayit_id=k.kayit_id) AS ref_sayisi
      FROM kayit k JOIN dosya d ON d.dosya_id=k.dosya_id;
    DROP TABLE IF EXISTS kayit_fts;
    CREATE VIRTUAL TABLE kayit_fts USING fts5(kayit_id UNINDEXED, dosya_id UNINDEXED, katman UNINDEXED, zaman UNINDEXED, gecerlilik UNINDEXED, metin, genisletme,
                                            tokenize = 'unicode61 remove_diacritics 2');
    INSERT INTO kayit_fts (kayit_id, dosya_id, katman, zaman, gecerlilik, metin, genisletme)
      SELECT g.kayit_id, g.dosya_id, g.katman, g.zaman, COALESCE(k.gecerlilik, CASE WHEN g.katman='soguk' THEN 'tarihce' ELSE 'guncel' END), COALESCE(k.metin,''), COALESCE(g.genisletme,'')
      FROM erisim_genisletme g JOIN kayit k ON k.kayit_id=g.kayit_id;
    INSERT INTO kayit_fts(kayit_fts) VALUES('optimize');
    """)
    con.commit()
    n = con.execute("SELECT COUNT(*) FROM kayit_fts").fetchone()[0]
    return n


# ------------------------------------------------------------------ sorgu
def fts_sorgu_kur(sorgu):
    """Sözcükler → FTS5 MATCH: ≥4 harf önek (kelime*), kısa sözcük tam; AND. Tarih/sayı dizeleri MATCH'e alınmaz (zaman filtresiyle işlenir)."""
    kelimeler = [w for w in re.findall(r"[0-9A-Za-zÇĞİÖŞÜçğıöşü]+", sorgu)]  # tire/alt-çizgi AYIRICI (FTS5 unicode61 ile aynı): proof-of-work → 3 sözcük
    parcalar = []
    for w in kelimeler:
        if ZAMAN_RX.fullmatch(w) or len(w) < 2 or w.isdigit():
            continue
        parcalar.append('"%s"*' % w if len(w) >= 4 else '"%s"' % w)
    return parcalar


GEN_AGIRLIK = 0.5  # bm25 genişletme kolonu ağırlığı (metin 1,0). 2,0 → 0,5 (08-29, İB-43 kalibrasyonu: 7 ağırlık × 100 soru; nDCG@10 0,433→0,452, bilgi-guncelleme r@5 0,40→0,45; kural: her ikisi ≥ mevcut) — değişiklik yalnız tools/erisim-kalibrasyon.py ölçümüyle


def sorgula(con, sorgu, k=5, genisletme=True, zaman_farkindali=True, guncel_yuzey=False, gen_agirlik=None):
    """Dönüş: (sonuç listesi [kayit_id, dosya_id, katman, zaman, skor, metin_kisa], meta). gen_agirlik: genişletme kolonu bm25 ağırlığı (None = GEN_AGIRLIK)."""
    parcalar = fts_sorgu_kur(sorgu)
    meta = {"parca": len(parcalar), "gevsetildi": False, "zaman_filtre": None, "guncel": False, "guncel_yuzey": guncel_yuzey}
    if not parcalar:
        return [], meta
    tarihler = ZAMAN_RX.findall(sorgu)
    zaman_on = None
    if zaman_farkindali and tarihler:
        t = tarihler[0]; zaman_on = t if len(t) == 10 else None; meta["zaman_filtre"] = t
    guncel = bool(zaman_farkindali and GUNCEL_RX.search(sorgu)); meta["guncel"] = guncel
    ga = GEN_AGIRLIK if gen_agirlik is None else float(gen_agirlik)
    agir = "bm25(kayit_fts, 0, 0, 0, 0, 0, 1.0, %s)" % (repr(ga) if genisletme else "0.0")
    kolonlar = "metin" if not genisletme else None

    def calistir(match):
        sql = "SELECT kayit_id, dosya_id, katman, zaman, %s AS skor, substr(metin,1,120) FROM kayit_fts WHERE kayit_fts MATCH ? " % agir
        prm = [match]
        if zaman_on:
            sql += "AND zaman LIKE ? "; prm.append(zaman_on + "%")
        if guncel_yuzey:  # Karar 58 sinerjisi: sıcak/ılık ∧ gecerlilik=guncel (v_guncel_kayit yüzeyi); boş dönerse tüm korpusa düşer
            sql += "AND katman IN ('sicak','ilik') AND gecerlilik='guncel' "
        sql += "ORDER BY skor LIMIT 200"
        return con.execute(sql, prm).fetchall()

    if genisletme:
        match = " AND ".join(parcalar)
    else:
        match = "metin : (" + " AND ".join(parcalar) + ")"
    match_or = (" OR ".join(parcalar)) if genisletme else ("metin : (" + " OR ".join(parcalar) + ")")
    # sıra: AND@yüzey → OR@yüzey → AND@tüm → OR@tüm (güncel yüzey önce korunur; gevşetme önce terimlerde, sonra yüzeyde)
    rows = calistir(match)
    if not rows and len(parcalar) > 1:
        meta["gevsetildi"] = True; rows = calistir(match_or)
    if not rows and guncel_yuzey:
        meta["guncel_yuzey"] = "düştü"; guncel_yuzey = False; meta["gevsetildi"] = False
        rows = calistir(match)
        if not rows and len(parcalar) > 1:
            meta["gevsetildi"] = True; rows = calistir(match_or)
    if zaman_farkindali and tarihler and not zaman_on:  # MM-DD: metinde tarih dizesi geçenler öne
        t = tarihler[0]
        rows.sort(key=lambda r: (0 if t in (r[5] or "") else 1, r[4]))
    if guncel:
        rows.sort(key=lambda r: (KATMAN_ONCELIK.get(r[2], 9), r[4]))
    return rows[:k], meta


def grep_taban(con, sorgu, k=5):
    """Taban çizgisi: tüm sözcükler (katlanmış) alt-dize olarak geçen kayıtlar; sıra: katman önceliği → dosya → sıra. (Deterministik 'grep'.)"""
    kelimeler = [fold(w) for w in re.findall(r"[0-9A-Za-zÇĞİÖŞÜçğıöşü_-]+", sorgu) if len(w) >= 2 and not ZAMAN_RX.fullmatch(w)]
    if not kelimeler:
        return []
    rows = []
    for kid, did, kat, sira, metin in con.execute("SELECT k.kayit_id, k.dosya_id, d.katman, k.sira, k.metin FROM kayit k JOIN dosya d ON d.dosya_id=k.dosya_id"):
        m = fold(metin)
        if all(w in m for w in kelimeler):
            rows.append((kid, did, kat, sira, (metin or "")[:120]))
    rows.sort(key=lambda r: (KATMAN_ONCELIK.get(r[2], 9), r[1], r[3]))
    return [(r[0], r[1], r[2], None, None, r[4]) for r in rows[:k]]


# ------------------------------------------------------------------ eval
def sorulari_oku(repo):
    yol = os.path.join(repo, SORU_YOLU)
    if not os.path.exists(yol):
        sys.exit("[HATA] soru seti yok: %s" % SORU_YOLU)
    out, hata = [], []
    with open(yol, encoding="utf-8") as fh:
        for i, l in enumerate(fh, 1):
            l = l.strip()
            if not l or l.startswith("#"):
                continue
            try:
                s = json.loads(l)
            except json.JSONDecodeError as e:
                hata.append("%d: JSON %s" % (i, e)); continue
            if not s.get("id") or not s.get("soru") or s.get("yetenek") not in YETENEK or not isinstance(s.get("beklenen_dosya"), list):
                hata.append("%d: şema (id/soru/yetenek∈%s/beklenen_dosya[])" % (i, "|".join(YETENEK)))
            out.append(s)
    return out, hata


def degerlendir(con, sorular, k=5, taban=False):
    yontemler = {"fts5": lambda q: sorgula(con, q, k, genisletme=False, zaman_farkindali=False)[0],
                 "fts5+gen": lambda q: sorgula(con, q, k, genisletme=True, zaman_farkindali=True)[0],
                 "fts5+guncel": lambda q: sorgula(con, q, k, genisletme=True, zaman_farkindali=True, guncel_yuzey=True)[0],
                 # fts5+auto (08-29, İB-43 kalibrasyonu): güncel yüzey yalnız soruda güncellik sözcüğü varsa (GUNCEL_RX) — deterministik yönlendirme;
                 # gerekçe: sabit yüzey bilgi-guncelleme'yi 0,40→0,70 çıkarırken cok-oturum/zamansal'ı düşürüyordu; auto ikisini de korudu (v_erisim_kalibrasyon)
                 "fts5+auto": lambda q: sorgula(con, q, k, genisletme=True, zaman_farkindali=True, guncel_yuzey=bool(GUNCEL_RX.search(q)))[0]}
    if taban:  # COST tabanı (grep): ~370 ms/soru — yalnız --taban ile (hat adımında kapalı; ölçüm turunda açık)
        yontemler = {"grep": lambda q: grep_taban(con, q, k), **yontemler}
    sonuc = []
    for s in sorular:
        for ad, fn in yontemler.items():
            t0 = time.perf_counter(); rows = fn(s["soru"]); sure = (time.perf_counter() - t0) * 1000
            dosyalar = [r[1] for r in rows]
            bek = s.get("beklenen_dosya") or []
            rx = s.get("beklenen_kayit_regex")
            if bek:
                isabet_sira = next((i + 1 for i, d in enumerate(dosyalar) if d in bek), None)
                if rx and isabet_sira:
                    isabet_sira = next((i + 1 for i, r in enumerate(rows) if r[1] in bek and re.search(rx, r[5] or "")), isabet_sira)
                recall5 = 1 if isabet_sira else 0; mrr = (1.0 / isabet_sira) if isabet_sira else 0.0
            else:  # çekimserlik: doğru davranış = ilgili dosya yok; ölçüm: top-1 skor + sonuç sayısı (eşik kalibresi borç)
                isabet_sira, recall5, mrr = None, None, None
            sonuc.append({"soru_id": s["id"], "yetenek": s["yetenek"], "yontem": ad, "recall5": recall5, "mrr": mrr, "isabet_sira": isabet_sira,
                          "sure_ms": round(sure, 2), "top1_dosya": dosyalar[0] if dosyalar else None, "top1_skor": (rows[0][4] if rows and rows[0][4] is not None else None),
                          "n_sonuc": len(rows), "top5": dosyalar})
    return sonuc


def ozetle(sonuc):
    oz = {}
    for r in sonuc:
        key = (r["yontem"], r["yetenek"]); o = oz.setdefault(key, {"n": 0, "r5": 0, "mrr": 0.0, "sure": 0.0, "nc": 0})
        o["n"] += 1; o["sure"] += r["sure_ms"]
        if r["recall5"] is not None:
            o["r5"] += r["recall5"]; o["mrr"] += r["mrr"]; o["nc"] += 1
    satirlar = []
    for (y, yt), o in sorted(oz.items()):
        satirlar.append({"yontem": y, "yetenek": yt, "n": o["n"], "recall5": round(o["r5"] / o["nc"], 3) if o["nc"] else None,
                         "mrr": round(o["mrr"] / o["nc"], 3) if o["nc"] else None, "ort_sure_ms": round(o["sure"] / o["n"], 2)})
    top = {}
    for r in sonuc:
        o = top.setdefault(r["yontem"], {"n": 0, "r5": 0, "mrr": 0.0, "sure": 0.0, "nc": 0}); o["n"] += 1; o["sure"] += r["sure_ms"]
        if r["recall5"] is not None:
            o["r5"] += r["recall5"]; o["mrr"] += r["mrr"]; o["nc"] += 1
    for y, o in sorted(top.items()):
        satirlar.append({"yontem": y, "yetenek": "TÜMÜ", "n": o["n"], "recall5": round(o["r5"] / o["nc"], 3) if o["nc"] else None,
                         "mrr": round(o["mrr"] / o["nc"], 3) if o["nc"] else None, "ort_sure_ms": round(o["sure"] / o["n"], 2)})
    return satirlar


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.getcwd())
    ap.add_argument("--insa", action="store_true"); ap.add_argument("--eval", action="store_true")
    ap.add_argument("--sorgu", default=None); ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--sessiz", action="store_true"); ap.add_argument("--kuru", action="store_true")
    ap.add_argument("--taban", action="store_true", help="grep taban çizgisini de koş (COST tabanı; ~370 ms/soru)")
    a = ap.parse_args(); repo = os.path.abspath(a.repo)
    if not fts5_var():
        sys.exit("[HATA] bu Python'un sqlite3'ünde FTS5 yok (compile_options ENABLE_FTS5) — KB-43 (a) ön-koşulu")
    db = os.path.join(repo, "veri", "baglam.sqlite")
    if not os.path.exists(db):
        sys.exit("[HATA] silver yok: veri/baglam.sqlite (önce tools/katman-hatti.py)")
    con = sqlite3.connect(db); head = git_head(repo)
    yap_insa = a.insa or (not a.eval and not a.sorgu)
    yap_eval = a.eval or (not a.insa and not a.sorgu)
    if yap_insa:
        t0 = time.perf_counter(); n = insa(con); print("erisim-fts: indeks kuruldu — kayit_fts %d satır · %.1f sn @ %s" % (n, time.perf_counter() - t0, head))
    else:
        try:
            con.execute("SELECT 1 FROM kayit_fts LIMIT 1")
        except sqlite3.Error:
            print("[uyarı] kayit_fts yok → kuruluyor"); insa(con)
    if a.sorgu:
        rows, meta = sorgula(con, a.sorgu, a.k, True, True)
        print("sorgu: %r · %s" % (a.sorgu, meta))
        for r in rows:
            print("  %-45s %-7s %-10s %8.3f  %s" % (r[1], r[2], (r[3] or "-"), (r[4] or 0), (r[5] or "").replace("\n", " ")[:80]))
    if yap_eval:
        sorular, hata = sorulari_oku(repo)
        if hata:
            for h in hata: print("[ŞEMA HATASI] " + h, file=sys.stderr)
            sys.exit(3)
        sonuc = degerlendir(con, sorular, a.k, a.taban); ozet = ozetle(sonuc)
        ts = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
        if not a.kuru:
            with open(os.path.join(repo, EVAL_LOG), "a", encoding="utf-8") as fh:
                for r in sonuc:
                    fh.write(json.dumps({"ts": ts, "head": head, **r}, ensure_ascii=False) + "\n")
            gdir = os.path.join(repo, "veri", "gorunum"); os.makedirs(gdir, exist_ok=True)
            with open(os.path.join(gdir, "v_erisim_eval.csv"), "w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=["yontem", "yetenek", "n", "recall5", "mrr", "ort_sure_ms"]); w.writeheader(); w.writerows(ozet)
        print("erisim-eval: %d soru × %d yöntem @ %s%s" % (len(sorular), 4 if a.taban else 3, head, " · KURU" if a.kuru else ""))
        if not a.sessiz:
            for o in ozet:
                if o["yetenek"] == "TÜMÜ" or True:
                    print("  %-9s %-17s n=%-3d recall@5 %-6s MRR %-6s süre %s ms" % (o["yontem"], o["yetenek"], o["n"], o["recall5"], o["mrr"], o["ort_sure_ms"]))
            kacirilan = [r for r in sonuc if r["recall5"] == 0 and r["yontem"] == "fts5+guncel"]
            if kacirilan:
                print("  fts5+guncel KAÇIRDI (%d): %s" % (len(kacirilan), ", ".join("%s→%s" % (r["soru_id"], r["top1_dosya"]) for r in kacirilan)))
    con.close()


if __name__ == "__main__":
    main()
