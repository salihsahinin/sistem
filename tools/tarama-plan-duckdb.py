#!/usr/bin/env python3
"""tarama-plan-duckdb.py — DuckDB/PARQUET PLAN-SINIFI denetimi (İB-38; KB-58 a Karar 64 — `tarama-plan.py`'nin kolon-katmanı kardeşi).
Yorumlayıcı: repo-içi `.venv/bin/python` (duckdb; Karar 63). Stdlib python ile çıkış 4 (hat: ATLANDI).

Ne yapar: tarama-plan.py ile AYNI sorgu sınıflarını (noktasal N* · agregasyon A* · LIKE önek L* · join J* · sıralı R*) parquet dosyalarında
`EXPLAIN (FORMAT JSON)` ile çalıştırır, plan ağacını NORMALİZE eder (operatör adı + PARQUET_SCAN Projections/Filters), PLAN SINIFI etiketlerini
çıkarır ve BEKLENTİ ile karşılaştırır. Ek olarak ZONE-MAP SİMÜLASYONU: sorgunun basit predikatı için parquet footer istatistiklerinden
(parquet_metadata: row_group × kolon min/max) predikatla KESİŞEN row-group sayısı deterministik hesaplanır → `rg_aday/rg_toplam` (Redshift blok
min/max atlamasının parquet karşılığı; wiki/kolon-katmani.md). DuckDB'nin kendi `operator_rows_scanned` sayacı satır sayısının ~10 katını rapor
etti (08-29 keşfi, anlamı belgelenmemiş) → atlama kanıtı sayaçtan DEĞİL footer'dan okunur (kolon-olcum'daki TOTAL_BYTES_READ dersiyle aynı).
Sınıf etiketleri: FİLTRE-İTME (Filters PARQUET_SCAN içinde) · FİLTRE-AYRIK (ayrı FILTER operatörü; predikat itilmedi) · KOLON-BUDAMA (projeksiyon <
dosya kolonu) · TAM-TARAMA (filtre yok) · GROUP-HASH · JOIN-HASH · TOP-N/ORDER. İhlal: `noktasal` türde FİLTRE-AYRIK ∨ TAM-TARAMA ∨ ¬KOLON-BUDAMA.
Çıktı: append-only veri/tarama-plan-duckdb.jsonl (grain: 1 satır = sorgu × koşum) + veri/gorunum/v_tarama_plan_duckdb.csv (son koşum) + stdout tablo.
Kullanım: .venv/bin/python tools/tarama-plan-duckdb.py [--repo <yol>] [--parquet veri/parquet] [--sorgu NP1,A2] [--sert] [--sessiz] [--kuru]
Çıkış: 0 tamam (uyarılar stderr) · 2 parquet yok/bilinmeyen sorgu · 3 ihlal YALNIZ --sert · 4 duckdb yok. Deneysel m.29 (2026-08-29, Carvis, yan icra P3).
"""
import argparse, csv, json, os, subprocess, sys, time
from datetime import datetime, timezone, timedelta

# ad → (açıklama, SQL şablonu ({p}=parquet dizini), tür, beklenen etiketler (⊆ olmalı), zone-map predikatı (dosya, kolon, alt, üst) ∨ None)
SORGULAR = {
    "NP1": ("noktasal PK (kayit_id=?) — sort key", "SELECT metin FROM '{p}/kayit.parquet' WHERE kayit_id = 'core/durum-kapsulu.md#12-12#00000000'", "noktasal",
            {"FİLTRE-İTME", "KOLON-BUDAMA"}, ("kayit.parquet", "kayit_id", "core/durum-kapsulu.md#12-12#00000000", "core/durum-kapsulu.md#12-12#00000000")),
    "NP2": ("noktasal dosya+satır aralığı", "SELECT kayit_id FROM '{p}/kayit.parquet' WHERE dosya_id = 'core/durum-kapsulu.md' AND satir_bas <= 12 AND satir_son >= 12", "noktasal",
            {"FİLTRE-İTME", "KOLON-BUDAMA"}, ("kayit.parquet", "dosya_id", "core/durum-kapsulu.md", "core/durum-kapsulu.md")),
    "NP3": ("noktasal referans (tür,değer)", "SELECT kayit_id FROM '{p}/referans.parquet' WHERE ref_turu = 'kart' AND ref_deger = 'K-015'", "noktasal",
            {"FİLTRE-İTME", "KOLON-BUDAMA"}, ("referans.parquet", "ref_turu", "kart", "kart")),
    "NP4": ("noktasal karar_borcu (borc_id=?)", "SELECT baslik FROM '{p}/karar_borcu.parquet' WHERE borc_id = 'KB-43'", "noktasal",
            {"FİLTRE-İTME", "KOLON-BUDAMA"}, ("karar_borcu.parquet", "borc_id", "KB-43", "KB-43")),
    "A1": ("tam sayım", "SELECT count(*) FROM '{p}/kayit.parquet'", "agregasyon", {"TAM-TARAMA"}, None),
    "A2": ("dosya×token agregasyon (Q1)", "SELECT dosya_id, count(*), sum(token_kestirim) FROM '{p}/kayit.parquet' GROUP BY 1", "agregasyon", {"TAM-TARAMA", "KOLON-BUDAMA", "GROUP-HASH"}, None),
    "A3": ("kolon filtresi + sayım", "SELECT count(*) FROM '{p}/kayit.parquet' WHERE blok_turu = 'tablo_satiri'", "agregasyon", {"FİLTRE-İTME", "KOLON-BUDAMA"},
           ("kayit.parquet", "blok_turu", "tablo_satiri", "tablo_satiri")),
    "L1": ("LIKE önek (dosya_id LIKE 'core/%') → aralık yeniden-yazımı", "SELECT count(*) FROM '{p}/kayit.parquet' WHERE dosya_id LIKE 'core/%'", "like",
           {"FİLTRE-İTME", "KOLON-BUDAMA"}, ("kayit.parquet", "dosya_id", "core/", "core0")),
    "J1": ("join kayit⋈referans (token by ref_turu)", "SELECT r.ref_turu, sum(k.token_kestirim) FROM '{p}/kayit.parquet' k JOIN '{p}/referans.parquet' r ON r.kayit_id = k.kayit_id GROUP BY 1", "join",
           {"JOIN-HASH", "GROUP-HASH", "KOLON-BUDAMA"}, None),
    "R1": ("sıralı erişim (ORDER BY sort key LIMIT 5)", "SELECT kayit_id FROM '{p}/kayit.parquet' ORDER BY kayit_id LIMIT 5", "sirali", {"TOP-N/ORDER", "KOLON-BUDAMA"}, None),
}
IHLAL_TURLERI = {"noktasal"}


def dugumler(n, out, derinlik=0, ust=None):
    ad = str(n.get("name", n.get("operator_name", "?"))).strip().upper()
    out.append((ad, n.get("extra_info") or {}, derinlik, ust))
    for ch in n.get("children", []):
        dugumler(ch, out, derinlik + 1, ad)


def siniflandir(plan_json, kolon_sayisi):
    kok = plan_json[0] if isinstance(plan_json, list) else plan_json
    D = []; dugumler(kok, D)
    etiket = set(); proj_n = None; filtre = None; scan_n = 0
    for ad, ek, _, ust in D:
        if "PARQUET" in ad or ad.endswith("_SCAN") or ad == "READ_PARQUET":
            scan_n += 1
            pr = ek.get("Projections")
            if pr is not None:
                pl = [x for x in str(pr).replace("\n", ",").split(",") if x.strip()]
                proj_n = len(pl) if proj_n is None else min(proj_n, len(pl))
            if ek.get("Filters"):
                etiket.add("FİLTRE-İTME"); filtre = str(ek.get("Filters"))[:120]
        if ad == "FILTER":
            etiket.add("FİLTRE-AYRIK")
        if "GROUP_BY" in ad or ad == "UNGROUPED_AGGREGATE":
            etiket.add("GROUP-HASH")
        if "JOIN" in ad:
            etiket.add("JOIN-HASH")
        if ad in ("TOP_N", "ORDER_BY"):
            etiket.add("TOP-N/ORDER")
    if "FİLTRE-İTME" not in etiket and "FİLTRE-AYRIK" not in etiket:
        etiket.add("TAM-TARAMA")
    if proj_n is not None and kolon_sayisi and proj_n < kolon_sayisi:
        etiket.add("KOLON-BUDAMA")
    return etiket, proj_n, filtre, [d[0] for d in D]


def zone_map(con, pq_dizin, pred):
    """parquet footer istatistiklerinden predikatla kesişen row group sayısı (deterministik; DuckDB'nin ne yaptığından bağımsız SİMÜLASYON)."""
    if not pred:
        return None, None
    dosya, kolon, alt, ust = pred
    yol = os.path.join(pq_dizin, dosya)
    rows = con.execute("SELECT row_group_id, stats_min_value, stats_max_value FROM parquet_metadata(?) WHERE path_in_schema = ?", (yol, kolon)).fetchall()
    if not rows:
        return None, None
    aday = sum(1 for _, mn, mx in rows if mn is None or mx is None or (str(mn) <= str(ust) and str(mx) >= str(alt)))
    return aday, len(rows)


def main():
    ap = argparse.ArgumentParser(description="DuckDB/parquet plan-sınıfı denetimi (İB-38)")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--parquet", default="veri/parquet"); ap.add_argument("--cikti", default="veri/tarama-plan-duckdb.jsonl")
    ap.add_argument("--sorgu", default=""); ap.add_argument("--sert", action="store_true"); ap.add_argument("--sessiz", action="store_true"); ap.add_argument("--kuru", action="store_true")
    a = ap.parse_args(); repo = os.path.abspath(a.repo); pq = os.path.join(repo, a.parquet)
    try:
        import duckdb
    except ImportError:
        print("HATA: duckdb yok — .venv/bin/python (Karar 63 venv)", file=sys.stderr); return 4
    if not os.path.exists(os.path.join(pq, "kayit.parquet")):
        print("HATA: parquet yok: %s (önce ambar-parquet.py)" % pq, file=sys.stderr); return 2
    secim = [s.strip() for s in a.sorgu.split(",") if s.strip()] or list(SORGULAR)
    bilinmeyen = [s for s in secim if s not in SORGULAR]
    if bilinmeyen:
        print("HATA: bilinmeyen sorgu adı: %s · geçerli: %s" % (", ".join(bilinmeyen), ",".join(SORGULAR)), file=sys.stderr); return 2
    con = duckdb.connect()
    kolon_sayisi = {}
    for f in sorted(os.listdir(pq)):
        if f.endswith(".parquet"):
            kolon_sayisi[f] = con.execute("SELECT count(*) FROM parquet_schema(?) WHERE num_children IS NULL OR num_children = 0", (os.path.join(pq, f),)).fetchone()[0]
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip() or "-"
    ts = datetime.now(timezone(timedelta(hours=3))).replace(microsecond=0).isoformat()
    satirlar, ihlal = [], 0
    for ad in secim:
        acik, sql_s, tur, beklenti, pred = SORGULAR[ad]
        sql = sql_s.format(p=pq)
        try:
            t0 = time.perf_counter(); plan = json.loads(con.execute("EXPLAIN (FORMAT JSON) " + sql).fetchall()[0][1]); t_plan = (time.perf_counter() - t0) * 1000
            ana_dosya = next((x for x in kolon_sayisi if x in sql), None)
            etiket, proj_n, filtre, ops = siniflandir(plan, kolon_sayisi.get(ana_dosya))
            t1 = time.perf_counter(); n_sonuc = len(con.execute(sql).fetchall()); t_kos = (time.perf_counter() - t1) * 1000
            rg_aday, rg_toplam = zone_map(con, pq, pred)
        except Exception as e:
            satirlar.append({"ts": ts, "git_head": head, "sorgu": ad, "aciklama": acik, "tur": tur, "sonuc": "HATA", "neden": str(e)[:200]})
            print("HATA: %s EXPLAIN/koşum düştü: %s" % (ad, str(e)[:120]), file=sys.stderr); continue
        uyum = beklenti <= etiket
        ihl = tur in IHLAL_TURLERI and (("FİLTRE-AYRIK" in etiket) or ("TAM-TARAMA" in etiket) or ("KOLON-BUDAMA" not in etiket))
        ihlal += 1 if ihl else 0
        satirlar.append({"ts": ts, "git_head": head, "duckdb": duckdb.__version__, "sorgu": ad, "aciklama": acik, "tur": tur, "sonuc": "OK",
                         "siniflar": sorted(etiket), "beklenti": sorted(beklenti), "uyum": uyum, "ihlal": ihl, "operatorler": ops,
                         "projeksiyon_n": proj_n, "kolon_n": kolon_sayisi.get(ana_dosya), "filtre": filtre, "rg_aday": rg_aday, "rg_toplam": rg_toplam,
                         "n_sonuc": n_sonuc, "plan_ms": round(t_plan, 2), "kosum_ms": round(t_kos, 2),
                         "damga": "deneysel m.29; sınıf = EXPLAIN JSON normalize; rg_aday = footer min/max simülasyonu (DuckDB sayacı değil)"})
        if ihl:
            print("UYARI: %s (%s) İHLAL — noktasal sorguda %s" % (ad, acik, "/".join(sorted(etiket))), file=sys.stderr)
        elif not uyum:
            print("BEKLENTİ DIŞI: %s %s ⊄ %s" % (ad, sorted(etiket), sorted(beklenti)), file=sys.stderr)
    ok = [s for s in satirlar if s["sonuc"] == "OK"]
    if not ok:
        print("HATA: hiçbir sorgu koşmadı", file=sys.stderr); return 2
    if not a.kuru:
        with open(os.path.join(repo, a.cikti), "a", encoding="utf-8") as fh:
            for s in satirlar:
                fh.write(json.dumps(s, ensure_ascii=False) + "\n")
        gd = os.path.join(repo, "veri", "gorunum"); os.makedirs(gd, exist_ok=True)
        with open(os.path.join(gd, "v_tarama_plan_duckdb.csv"), "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh, lineterminator="\n"); w.writerow(["sorgu", "tur", "siniflar", "uyum", "ihlal", "projeksiyon_n", "kolon_n", "rg_aday", "rg_toplam", "n_sonuc", "kosum_ms", "git_head"])
            for s in ok:
                w.writerow([s["sorgu"], s["tur"], "|".join(s["siniflar"]), s["uyum"], s["ihlal"], s["projeksiyon_n"], s["kolon_n"], s["rg_aday"], s["rg_toplam"], s["n_sonuc"], s["kosum_ms"], s["git_head"]])
    if not a.sessiz:
        print("tarama-plan-duckdb @ %s · duckdb %s · %d sorgu · ihlal %d · beklenti-dışı %d" % (head, duckdb.__version__, len(ok), ihlal, sum(1 for s in ok if not s["uyum"])))
        for s in ok:
            print("  %-4s %-10s %-45s proj %s/%s · rg %s/%s · %5.1f ms · %s%s" % (s["sorgu"], s["tur"], "|".join(s["siniflar"])[:45], s["projeksiyon_n"], s["kolon_n"], s["rg_aday"], s["rg_toplam"], s["kosum_ms"],
                                                                                  "UYUM" if s["uyum"] else "BEKLENTİ-DIŞI", " İHLAL" if s["ihlal"] else ""))
    return 3 if (ihlal and a.sert) else 0


if __name__ == "__main__":
    sys.exit(main())
