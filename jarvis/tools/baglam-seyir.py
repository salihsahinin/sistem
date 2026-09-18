#!/usr/bin/env python3
"""baglam-seyir.py — BAĞLAM KOMPOZİSYONU ölçüm hattı (KB-50 (a), Salih imzası 08-21 Karar 61 — bağlam bütçesi kural setinin KALİBRASYON VERİSİ;
KB-52 (a) 128K uzun-koşum uyarısı; icra İB-22, 2026-08-22 seans-14). STDLIB ONLY, Python ≥3.9; deterministik (yalnız transkript + disk).

BRONZ (kaynak-konform, ham + provenans): oturum transkriptleri (`~/.claude/projects/<proje>/*.jsonl`, repo dışı, md.49: yalnız jarvis) taranır; her
  ASİSTAN TURU (API çağrısı) için `message.usage` alanları OLDUĞU GİBİ `veri/bronz/baglam-olay.jsonl`'a APPEND edilir (tekilleştirme anahtarı =
  mesaj uuid; ham sayı DEĞİŞTİRİLMEZ; provenans: kaynak dosya + uuid + ts + requestId). Statusline JSON YOK (ayar boş) → tek kaynak transkript.
  Alanlar: input_tokens · cache_creation_input_tokens · cache_read_input_tokens · output_tokens · thinking_tokens · model · is_sidechain · effort.
SİLVER (1:1, tipli, türetilmiş): `baglam_olay` (1 satır = 1 asistan turu): baglam = input + cache_creation + cache_read (= o turda pencerede duran
  token — bağlam doluluğu kestirimi; Anthropic usage semantiği: üçü ayrık, toplamı istek girdisi) · ts_tr/tarih_tr · oturum_kisa · sira · 128k bayrağı.
GOLD (iş-konform, tek tanım): `v_baglam_seyri` (oturum başına: tur sayısı · ilk-tur bağlamı [STATİK ÖNEK kestirimi: sistem + CLAUDE.md + hook +
  skill açıklamaları + araç şemaları + ilk mesaj] · max/son bağlam · 128K üstü tur sayısı · toplam çıktı/thinking) · `v_baglam_gunluk` (gün × model)
  → `veri/gorunum/*.csv`. KB-50 (a) eşikleri (m.29, bu veriyle kalibre): statik önek ≤~60k ∧ Jarvis-özel ≤~25k · 128K uyarısı (KB-52).
Uyarı kanalı (stderr; çıkış 0): oturum max bağlam > 128.000 → "UYARI 128K" · ilk-tur bağlamı > 60.000 → "UYARI statik-önek". Testler: unique(olay_id) ·
  not_null(oturum) · baglam ≥ 0. Sözleşme `veri/sozlesme/baglam_olay.json` (additive-only).
Kullanım: python3 tools/baglam-seyir.py [--proje-dizin <yol>] [--repo <yol>] [--kuru] [--sessiz]
Çıkış: 0 tamam · 2 transkript dizini yok · 3 veri-testi ERROR. Deneysel m.29.
"""
import argparse, csv, glob, json, os, sqlite3, sys
from datetime import datetime, timezone, timedelta

TR = timezone(timedelta(hours=3))
ESIK_128K = 128_000
ESIK_STATIK = 60_000


def parse_ts(ts):
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except Exception:
        return None


def bronz_topla(proje_dizin):
    """Transkriptte aynı asistan mesajı birden çok satırda (içerik bloğu başına) yinelenir, uuid aynı, usage özdeş → uuid başına İLK satır alınır."""
    olaylar, gorulen = [], set()
    for f in sorted(glob.glob(os.path.join(proje_dizin, "*.jsonl"))):
        kaynak = os.path.basename(f)
        for l in open(f, encoding="utf-8", errors="replace"):
            try:
                r = json.loads(l)
            except Exception:
                continue
            if r.get("type") != "assistant":
                continue
            m = r.get("message") or {}
            u = m.get("usage") if isinstance(m, dict) else None
            if not isinstance(u, dict) or not r.get("uuid") or r["uuid"] in gorulen:
                continue
            gorulen.add(r["uuid"])
            olaylar.append({
                "olay_id": r["uuid"], "ts": r.get("timestamp"), "oturum": r.get("sessionId") or kaynak[:-6], "request_id": r.get("requestId"),
                "model": m.get("model"), "effort": r.get("effort"), "is_sidechain": bool(r.get("isSidechain")),
                "input_tokens": u.get("input_tokens"), "cache_creation_input_tokens": u.get("cache_creation_input_tokens"),
                "cache_read_input_tokens": u.get("cache_read_input_tokens"), "output_tokens": u.get("output_tokens"),
                "thinking_tokens": ((u.get("output_tokens_details") or {}).get("thinking_tokens") if isinstance(u.get("output_tokens_details"), dict) else None),
                "kaynak_dosya": kaynak})
    return olaylar


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proje-dizin", default=os.path.expanduser("~/.claude/projects/-Users-HasanSalihSahin-jarvis"))
    ap.add_argument("--repo", default=os.getcwd())
    ap.add_argument("--kuru", action="store_true"); ap.add_argument("--sessiz", action="store_true")
    a = ap.parse_args(); repo = os.path.abspath(a.repo)
    if not os.path.isdir(a.proje_dizin):
        sys.exit("[HATA] transkript dizini yok: %s" % a.proje_dizin)
    bronz_yol = os.path.join(repo, "veri", "bronz", "baglam-olay.jsonl")
    mevcut = {}
    if os.path.exists(bronz_yol):
        for l in open(bronz_yol, encoding="utf-8"):
            try:
                o = json.loads(l); mevcut[o["olay_id"]] = o
            except Exception:
                pass
    yeni = [o for o in bronz_topla(a.proje_dizin) if o["olay_id"] not in mevcut]
    if not a.kuru and yeni:
        os.makedirs(os.path.dirname(bronz_yol), exist_ok=True)
        with open(bronz_yol, "a", encoding="utf-8") as fh:
            for o in yeni:
                fh.write(json.dumps(o, ensure_ascii=False) + "\n")
    tum = list(mevcut.values()) + yeni
    tum.sort(key=lambda o: (o.get("ts") or "", o["olay_id"]))
    # --- SİLVER ---
    sira = {}; satirlar = []
    for o in tum:
        t = parse_ts(o.get("ts") or ""); ttr = t.astimezone(TR) if t else None
        sira[o["oturum"]] = sira.get(o["oturum"], 0) + 1
        inp = o.get("input_tokens") or 0; cc = o.get("cache_creation_input_tokens") or 0; cr = o.get("cache_read_input_tokens") or 0
        baglam = inp + cc + cr
        satirlar.append({"olay_id": o["olay_id"], "ts_utc": o.get("ts"), "ts_tr": ttr.isoformat() if ttr else None,
                         "tarih_tr": ttr.strftime("%Y-%m-%d") if ttr else None, "saat_tr": ttr.strftime("%H:%M:%S") if ttr else None,
                         "oturum_id": o["oturum"], "oturum_kisa": (o["oturum"] or "")[:8], "sira": sira[o["oturum"]], "model": (o.get("model") or "").replace("claude-", "") or None,
                         "effort": o.get("effort"), "is_sidechain": 1 if o.get("is_sidechain") else 0, "input_tokens": inp, "cache_creation_input_tokens": cc,
                         "cache_read_input_tokens": cr, "baglam": baglam, "output_tokens": o.get("output_tokens") or 0, "thinking_tokens": o.get("thinking_tokens"),
                         "ustu_128k": 1 if baglam > ESIK_128K else 0, "request_id": o.get("request_id"), "kaynak_dosya": o.get("kaynak_dosya")})
    testler, uyarilar = [], []
    if not a.kuru:
        db = os.path.join(repo, "veri", "baglam.sqlite"); con = sqlite3.connect(db)
        con.executescript("""
        CREATE TABLE IF NOT EXISTS baglam_olay (
          olay_id TEXT PRIMARY KEY, ts_utc TEXT, ts_tr TEXT, tarih_tr TEXT, saat_tr TEXT, oturum_id TEXT NOT NULL, oturum_kisa TEXT, sira INTEGER,
          model TEXT, effort TEXT, is_sidechain INTEGER, input_tokens INTEGER, cache_creation_input_tokens INTEGER, cache_read_input_tokens INTEGER,
          baglam INTEGER, output_tokens INTEGER, thinking_tokens INTEGER, ustu_128k INTEGER, request_id TEXT, kaynak_dosya TEXT
        );
        DELETE FROM baglam_olay;
        CREATE VIEW IF NOT EXISTS v_baglam_seyri AS
          SELECT oturum_kisa, MIN(tarih_tr) AS tarih, MIN(saat_tr) AS ilk_saat, MAX(saat_tr) AS son_saat, COUNT(*) AS tur,
                 (SELECT b2.baglam FROM baglam_olay b2 WHERE b2.oturum_id=b.oturum_id AND b2.is_sidechain=0 ORDER BY b2.sira LIMIT 1) AS ilk_tur_baglam,
                 MAX(baglam) AS max_baglam, (SELECT b3.baglam FROM baglam_olay b3 WHERE b3.oturum_id=b.oturum_id ORDER BY b3.sira DESC LIMIT 1) AS son_baglam,
                 SUM(ustu_128k) AS tur_128k_ustu, SUM(output_tokens) AS toplam_cikti, SUM(COALESCE(thinking_tokens,0)) AS toplam_thinking,
                 SUM(is_sidechain) AS yan_zincir_tur, MAX(model) AS model
          FROM baglam_olay b GROUP BY oturum_id ORDER BY tarih DESC, ilk_saat DESC;
        CREATE VIEW IF NOT EXISTS v_baglam_gunluk AS
          SELECT tarih_tr, model, COUNT(*) AS tur, COUNT(DISTINCT oturum_id) AS oturum, MAX(baglam) AS max_baglam, ROUND(AVG(baglam)) AS ort_baglam,
                 SUM(ustu_128k) AS tur_128k_ustu, SUM(output_tokens) AS toplam_cikti, SUM(cache_read_input_tokens) AS toplam_cache_read,
                 SUM(cache_creation_input_tokens) AS toplam_cache_create
          FROM baglam_olay GROUP BY tarih_tr, model ORDER BY tarih_tr DESC, model;
        """)
        con.executemany("INSERT INTO baglam_olay VALUES (:olay_id,:ts_utc,:ts_tr,:tarih_tr,:saat_tr,:oturum_id,:oturum_kisa,:sira,:model,:effort,:is_sidechain,"
                        ":input_tokens,:cache_creation_input_tokens,:cache_read_input_tokens,:baglam,:output_tokens,:thinking_tokens,:ustu_128k,:request_id,:kaynak_dosya)", satirlar)
        con.commit()
        for ad, sql in [("baglam_olay.olay_id unique", "SELECT COUNT(*) FROM (SELECT olay_id FROM baglam_olay GROUP BY olay_id HAVING COUNT(*)>1)"),
                        ("baglam_olay.oturum_id not_null", "SELECT COUNT(*) FROM baglam_olay WHERE oturum_id IS NULL OR oturum_id=''"),
                        ("baglam_olay.baglam ≥ 0", "SELECT COUNT(*) FROM baglam_olay WHERE baglam < 0")]:
            n = con.execute(sql).fetchone()[0]; testler.append((ad, n, "PASS" if n == 0 else "ERROR"))
        sdir = os.path.join(repo, "veri", "sozlesme"); os.makedirs(sdir, exist_ok=True); syol = os.path.join(sdir, "baglam_olay.json")
        if not os.path.exists(syol):
            cols = [{"ad": r[1], "tip": r[2] or "ANY", "not_null": bool(r[3]), "pk": bool(r[5])} for r in con.execute("PRAGMA table_info(baglam_olay)")]
            json.dump({"tablo": "baglam_olay", "surum": "1.0.0-deneysel-m29", "katman": "silver", "grain": "1 satır = 1 asistan turu (API çağrısı) usage kaydı; baglam = input+cache_creation+cache_read",
                       "kolonlar": cols, "kural": "additive-only; kırıcı = silme/tip/kısıt/yeniden-ad", "kaynak": "tools/baglam-seyir.py (KB-50/52 a, İB-22, 2026-08-22)"},
                      open(syol, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        gdir = os.path.join(repo, "veri", "gorunum"); os.makedirs(gdir, exist_ok=True)
        for v in ("v_baglam_seyri", "v_baglam_gunluk"):
            cur = con.execute("SELECT * FROM %s" % v); cols = [d[0] for d in cur.description]
            with open(os.path.join(gdir, v + ".csv"), "w", newline="", encoding="utf-8") as fh:
                w = csv.writer(fh); w.writerow(cols); w.writerows(cur.fetchall())
        for ok, tarih, max_b, ilk_b, n128 in con.execute("SELECT oturum_kisa, tarih, max_baglam, ilk_tur_baglam, tur_128k_ustu FROM v_baglam_seyri"):
            if (max_b or 0) > ESIK_128K:
                uyarilar.append("UYARI 128K: oturum %s (%s) max bağlam %d · %d tur üstte (KB-52 uzun-koşum politikası)" % (ok, tarih, max_b, n128))
            if (ilk_b or 0) > ESIK_STATIK:
                uyarilar.append("UYARI statik-önek: oturum %s (%s) ilk-tur bağlamı %d > %d (KB-50 a ≤~60k; kestirim = ilk mesaj dahil)" % (ok, tarih, ilk_b, ESIK_STATIK))
        con.close()
    # --- çıktı ---
    oturumlar = len({o["oturum"] for o in tum})
    print("baglam-seyir: bronz +%d yeni / %d toplam tur · %d oturum · silver baglam_olay %d · gold v_baglam_seyri/v_baglam_gunluk%s"
          % (len(yeni), len(tum), oturumlar, len(satirlar) if not a.kuru else 0, " · KURU" if a.kuru else ""))
    if not a.sessiz:
        for ad, n, s in testler: print("  [%s] test %s → ihlal %d" % (s, ad, n))
        if not a.kuru:
            con = sqlite3.connect(os.path.join(repo, "veri", "baglam.sqlite"))
            for r in con.execute("SELECT oturum_kisa, tarih, tur, ilk_tur_baglam, max_baglam, son_baglam, tur_128k_ustu, toplam_cikti FROM v_baglam_seyri LIMIT 8"):
                print("  %s %s tur %4d · ilk %7s · max %7s · son %7s · 128k+ %3d · çıktı %s" % r)
            con.close()
    n128 = sum(1 for u in uyarilar if u.startswith("UYARI 128K")); nst = sum(1 for u in uyarilar if u.startswith("UYARI statik"))
    if uyarilar:  # uyarı kanalı: özet + en fazla 3 örnek (hat çıktısı taşmasın; tam liste v_baglam_seyri)
        print("UYARI baglam-seyir: %d oturum 128K üstü · %d oturum statik-önek >60k (KB-50/52 a; tam liste veri/gorunum/v_baglam_seyri.csv)" % (n128, nst), file=sys.stderr)
        for u in uyarilar[:3]:
            print("  " + u, file=sys.stderr)
    sys.exit(3 if any(s == "ERROR" for _a, _n, s in testler) else 0)


if __name__ == "__main__":
    main()
