#!/usr/bin/env python3
"""deneyim-tablo.py — EPİZODİK DENEYİM KATMANI (KB-44 (a) + model-kuşağı şerhi = Karar 60, 08-21; icra İB-44, 2026-08-22 seans-14). STDLIB ONLY; deterministik
(yalnız silver ambar + kural dosyası). LLM yok.

İki kanal (ExpeL): (i) yapısal DENEYİM tablosu → başarı/başarısızlık ÇİFTLERİ → damıtma turunda KURAL ADAYI (kanonlaşma yalnız dış geri-besleme / Salih imzası);
(ii) yeni görevde BENZER GEÇMİŞ YÖRÜNGE çekme (FTS5 `deneyim_fts`, kuşak iskontolu) → few-shot bağlam.
SİLVER `deneyim` (1 satır = 1 görev-yörüngesi = 1 işçi-ajan koşumu; amb_olgu_kosum ⋈ amb_olgu_kosum_sonuc ⋈ amb_olgu_tahmin): kosum_id · wf_id · agent_type ·
  aile · rol · emir_ozet · model · MODEL_KUSAGI (kural dosyası deseni) · eski_kusak (1 = kuşak < güncel) · agirlik (iskonto) · tarih (valid_time_bas) · sure_sn · token in/out ·
  hukum (PASS/FAIL/NULL = hüküm yok ≠ FAIL; Karar 52 öneri-damgalı) · hukum_kaynak · tahmin_var · oturum · kod_sha. Model/kuşak/tarih ZORUNLU (Salih şerhi).
GOLD: `v_deneyim_ozet` (kuşak × agent_type × hüküm) · `v_deneyim_cift` (aynı wf_id ∨ aile+rol altında PASS∧FAIL çiftleri — kural adayı havuzu) · CSV.
Kuşak-değişim damgası: `guncel_kusak` kural dosyasından; değişince tüm eski yörüngeler otomatik eski_kusak=1 (yeniden üretim; silme yok).
Kullanım: python3 tools/deneyim-tablo.py [--repo <yol>] [--benzer "<yeni emir metni>" [--k 5]] [--sessiz] [--kuru]
Çıkış: 0 · 2 kural dosyası/DB yok · 3 veri-testi ERROR. Deneysel m.29.
"""
import argparse, csv, json, os, re, sqlite3, subprocess, sys

KURAL_YOLU = "veri/sozlesme/deneyim-kurallar.json"


def git_head(repo):
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "?"


def kusak_bul(modeller, harita):
    """Çoklu model listesinde ('a,b') sentetik hariç EN GÜÇLÜ/son kuşak değil, İLK gerçek model alınır (deterministik: virgül sırası)."""
    for m in (modeller or "").split(","):
        m = m.strip()
        if not m or m == "<synthetic>":
            continue
        for h in harita:
            if h["desen"] != "<synthetic>" and h["desen"] in m:
                return m, h["kusak"], h.get("sinif")
        return m, "?", None
    return (modeller or ""), "-", "synthetic" if "<synthetic>" in (modeller or "") else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.getcwd()); ap.add_argument("--benzer", default=None); ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--sessiz", action="store_true"); ap.add_argument("--kuru", action="store_true")
    a = ap.parse_args(); repo = os.path.abspath(a.repo)
    kyol = os.path.join(repo, KURAL_YOLU)
    if not os.path.exists(kyol):
        sys.exit("[HATA] kural dosyası yok: %s" % KURAL_YOLU)
    kural = json.load(open(kyol, encoding="utf-8")); harita = kural["kusak_haritasi"]; guncel = str(kural["guncel_kusak"]); iskonto = kural["iskonto"]
    db = os.path.join(repo, "veri", "baglam.sqlite")
    if not os.path.exists(db):
        sys.exit("[HATA] silver yok: veri/baglam.sqlite")
    con = sqlite3.connect(db); head = git_head(repo)
    mevcut = {r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    if "amb_olgu_kosum" not in mevcut:
        sys.exit("[HATA] amb_olgu_kosum yok (ambar-tablo.py önce koşmalı)")
    rows = con.execute("""SELECT k.kosum_id, k.wf_id, k.agent_type, k.aile, k.rol, k.ilk_prompt_kisa, k.modeller, k.valid_time_bas, k.sure_sn,
                                 k.input_tokens, k.output_tokens, k.arac_cagrisi, k.oturum, s.sonuc, s.kaynak,
                                 (SELECT COUNT(*) FROM amb_olgu_tahmin t WHERE t.wf_id=k.wf_id) AS tahmin_var
                          FROM amb_olgu_kosum k LEFT JOIN amb_olgu_kosum_sonuc s ON s.kosum_id=k.kosum_id ORDER BY k.valid_time_bas, k.kosum_id""").fetchall()
    satirlar, bilinmeyen = [], set()
    for r in rows:
        model, kusak, sinif = kusak_bul(r[6], harita)
        if kusak == "?":
            bilinmeyen.add(model)
        eski = 1 if (kusak not in ("-", "?") and float(kusak) < float(guncel)) else (0 if kusak == guncel else (1 if kusak == "?" else 0))
        satirlar.append({"kosum_id": r[0], "wf_id": r[1], "agent_type": r[2], "aile": r[3], "rol": r[4], "emir_ozet": (r[5] or "")[:300], "model": model,
                         "model_sinifi": sinif, "model_kusagi": kusak, "eski_kusak": eski, "agirlik": float(iskonto.get(kusak, iskonto.get("?", 0.5))),
                         "tarih": (r[7] or "")[:10], "valid_time_bas": r[7], "sure_sn": r[8], "input_tokens": r[9], "output_tokens": r[10], "arac_cagrisi": r[11],
                         "oturum": r[12], "hukum": r[13], "hukum_kaynak": r[14], "tahmin_var": 1 if r[15] else 0, "guncel_kusak": guncel, "kod_sha": head})
    if not a.kuru:
        con.executescript("""
        CREATE TABLE IF NOT EXISTS deneyim (
          kosum_id TEXT PRIMARY KEY, wf_id TEXT, agent_type TEXT, aile TEXT, rol TEXT, emir_ozet TEXT, model TEXT, model_sinifi TEXT,
          model_kusagi TEXT NOT NULL, eski_kusak INTEGER NOT NULL, agirlik REAL, tarih TEXT NOT NULL, valid_time_bas TEXT, sure_sn REAL,
          input_tokens INTEGER, output_tokens INTEGER, arac_cagrisi INTEGER, oturum TEXT, hukum TEXT, hukum_kaynak TEXT, tahmin_var INTEGER,
          guncel_kusak TEXT, kod_sha TEXT
        );
        DELETE FROM deneyim;
        CREATE VIEW IF NOT EXISTS v_deneyim_ozet AS
          SELECT model_kusagi, eski_kusak, agent_type, COUNT(*) AS n, SUM(CASE WHEN hukum='PASS' THEN 1 ELSE 0 END) AS pass_n,
                 SUM(CASE WHEN hukum='FAIL' THEN 1 ELSE 0 END) AS fail_n, SUM(CASE WHEN hukum IS NULL THEN 1 ELSE 0 END) AS hukumsuz_n,
                 ROUND(AVG(sure_sn)) AS ort_sure_sn, SUM(output_tokens) AS toplam_cikti, MIN(tarih) AS ilk, MAX(tarih) AS son
          FROM deneyim GROUP BY model_kusagi, eski_kusak, agent_type ORDER BY model_kusagi DESC, agent_type;
        CREATE VIEW IF NOT EXISTS v_deneyim_cift AS
          SELECT p.kosum_id AS pass_kosum, f.kosum_id AS fail_kosum, COALESCE(p.wf_id, p.aile||'/'||p.rol) AS grup, p.agent_type,
                 p.model_kusagi AS pass_kusak, f.model_kusagi AS fail_kusak, p.emir_ozet AS pass_emir, f.emir_ozet AS fail_emir, p.tarih AS pass_tarih, f.tarih AS fail_tarih
          FROM deneyim p JOIN deneyim f ON f.hukum='FAIL' AND p.hukum='PASS'
               AND ((p.wf_id IS NOT NULL AND p.wf_id=f.wf_id) OR (p.aile IS NOT NULL AND p.aile=f.aile AND p.rol=f.rol))
          ORDER BY p.tarih DESC;
        """)
        con.executemany("INSERT INTO deneyim VALUES (:kosum_id,:wf_id,:agent_type,:aile,:rol,:emir_ozet,:model,:model_sinifi,:model_kusagi,:eski_kusak,:agirlik,:tarih,"
                        ":valid_time_bas,:sure_sn,:input_tokens,:output_tokens,:arac_cagrisi,:oturum,:hukum,:hukum_kaynak,:tahmin_var,:guncel_kusak,:kod_sha)", satirlar)
        # FTS (ii. kanal): benzer yörünge çekme
        try:
            con.executescript("""DROP TABLE IF EXISTS deneyim_fts;
            CREATE VIRTUAL TABLE deneyim_fts USING fts5(kosum_id UNINDEXED, model_kusagi UNINDEXED, agirlik UNINDEXED, hukum UNINDEXED, tarih UNINDEXED, metin,
                                                      tokenize='unicode61 remove_diacritics 2');
            INSERT INTO deneyim_fts SELECT kosum_id, model_kusagi, agirlik, hukum, tarih, COALESCE(agent_type,'')||' '||COALESCE(aile,'')||' '||COALESCE(rol,'')||' '||COALESCE(emir_ozet,'') FROM deneyim;""")
            fts_ok = True
        except sqlite3.Error:
            fts_ok = False
        con.commit()
        testler = []
        for ad, sql in [("deneyim.kosum_id unique", "SELECT COUNT(*) FROM (SELECT kosum_id FROM deneyim GROUP BY kosum_id HAVING COUNT(*)>1)"),
                        ("deneyim.model_kusagi/tarih not_null (Salih şerhi)", "SELECT COUNT(*) FROM deneyim WHERE model_kusagi IS NULL OR model_kusagi='' OR tarih IS NULL OR tarih=''"),
                        ("deneyim.hukum accepted_values", "SELECT COUNT(*) FROM deneyim WHERE hukum IS NOT NULL AND hukum NOT IN ('PASS','FAIL')")]:
            n = con.execute(sql).fetchone()[0]; testler.append((ad, n, "PASS" if n == 0 else "ERROR"))
        sdir = os.path.join(repo, "veri", "sozlesme"); syol = os.path.join(sdir, "deneyim.json")
        if not os.path.exists(syol):
            cols = [{"ad": r[1], "tip": r[2] or "ANY", "not_null": bool(r[3]), "pk": bool(r[5])} for r in con.execute("PRAGMA table_info(deneyim)")]
            json.dump({"tablo": "deneyim", "surum": "1.0.0-deneysel-m29", "katman": "silver", "grain": "1 satır = 1 görev-yörüngesi (işçi-ajan koşumu) + hüküm + model-kuşağı; KB-44 (a) Karar 60",
                       "kolonlar": cols, "kural": "additive-only; model/model_kusagi/tarih ZORUNLU (Salih şerhi)", "kaynak": "tools/deneyim-tablo.py (İB-44, 2026-08-22)"},
                      open(syol, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        gdir = os.path.join(repo, "veri", "gorunum"); os.makedirs(gdir, exist_ok=True)
        for v in ("v_deneyim_ozet", "v_deneyim_cift"):
            cur = con.execute("SELECT * FROM %s" % v); cols = [d[0] for d in cur.description]
            with open(os.path.join(gdir, v + ".csv"), "w", newline="", encoding="utf-8") as fh:
                w = csv.writer(fh); w.writerow(cols); w.writerows(cur.fetchall())
        n_cift = con.execute("SELECT COUNT(*) FROM v_deneyim_cift").fetchone()[0]
    else:
        testler, fts_ok, n_cift = [], False, 0
    n_h = sum(1 for s in satirlar if s["hukum"]); n_eski = sum(s["eski_kusak"] for s in satirlar)
    print("deneyim: %d yörünge · hükümlü %d (PASS %d / FAIL %d) · eski-kuşak %d · güncel kuşak %s · çift %d · fts %s%s" % (
        len(satirlar), n_h, sum(1 for s in satirlar if s["hukum"] == "PASS"), sum(1 for s in satirlar if s["hukum"] == "FAIL"), n_eski, guncel, n_cift,
        "var" if fts_ok else "yok", " · KURU" if a.kuru else ""))
    if bilinmeyen:
        print("UYARI deneyim: kuşak haritasında olmayan model: %s (kural dosyasına ekle)" % ", ".join(sorted(bilinmeyen)), file=sys.stderr)
    if not a.sessiz:
        for ad, n, s in testler: print("  [%s] test %s → ihlal %d" % (s, ad, n))
    if a.benzer and not a.kuru and fts_ok:
        kel = [w for w in re.findall(r"[0-9A-Za-zÇĞİÖŞÜçğıöşü]+", a.benzer) if len(w) >= 3]
        match = " OR ".join('"%s"*' % w for w in kel)
        print("benzer yörüngeler (bm25 × kuşak ağırlığı):")
        for r in con.execute("SELECT kosum_id, model_kusagi, agirlik, hukum, tarih, bm25(deneyim_fts)*CAST(agirlik AS REAL) AS skor, substr(metin,1,90) FROM deneyim_fts WHERE deneyim_fts MATCH ? ORDER BY skor LIMIT ?", (match, a.k)):
            print("  %-36s kuşak %-3s ağırlık %.1f hüküm %-4s %s  %s" % (r[0], r[1], r[2], r[3] or "-", r[4], r[6]))
    con.close()
    sys.exit(3 if any(s == "ERROR" for _a, _n, s in testler) else 0)


if __name__ == "__main__":
    main()
