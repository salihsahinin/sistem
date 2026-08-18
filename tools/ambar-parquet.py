#!/usr/bin/env python3
"""ambar-parquet.py — bağlam veri ambarından KOLON-BAZLI YAZIM: silver/ambar tabloları + gold martları → veri/parquet/*.parquet
(deneysel m.29; pipeline cc/pipeline-2026-08-18-kolon-katmani.md SH-2; kanıt cc/rapor-2026-08-18-2.md S4).

Desen (rapor S1/S4 — hazırı temel al, kod = tutkal): SQLite = YAZMA deposu (silver, OLTP; değişmez) → parquet = periyodik TOPLU türev
(kolon dosyası; kolon depolarında yazma birimi topludur, tek-satır yazımı anti-desen: A-YT3) → DuckDB = OLAP okuyucu. Kolon-kolon tablo
bölme YAPILMAZ (A-YT2 anti-desen). Yazıcı = DuckDB `COPY (SELECT … ORDER BY sort_key) TO 'x.parquet'` (B-YT1: hazır 14 seçenek; sıfırdan
yazıcı yok): ZSTD · ROW_GROUP_SIZE küçük-korpus (S-9 CD-YT1) · KV_METADATA {git_head, kod_sha, uretim_ts, satir, kaynak_tablo, sort_key}
(B-YT3/C-YT3: tazelik damgası footer'da) · idempotent üstüne-yazma + temp→rename atomiklik (C-YT2) · PARTITION_BY YOK (C-YT1: <100 MB).
Silver↔parquet EŞDEĞERLİK testi: satır sayısı + sayısal kolon toplamları iki motorda eşit (yazım-anı ölçüm kapısı, KB-01).

Bağımlılık: `duckdb` Python paketi (stdlib DIŞI — kabul kararı KB-55 Salih'te; yoksa FAIL-LOUD çıkış 4 + kurulum yönergesi; venv yolu ile
`<venv>/bin/python tools/ambar-parquet.py` çalışır). Diğer her şey stdlib (Python 3.9).

Kullanım:
  python3 tools/ambar-parquet.py [--repo <yol>] [--db veri/baglam.sqlite] [--cikti veri/parquet] [--tablo kayit,referans,...]
                                 [--row-group 4096] [--sessiz] [--kuru]
Çıkış: 0 tamam · 2 girdi yok · 3 eşdeğerlik testi FAIL · 4 duckdb yok.
Çıktı: veri/parquet/<tablo>.parquet (gitignore — KB-56 hükmüne dek türev sınıfı) + stdout özet (JSON satırı: dosya, satır, byte, ms, kv).
"""
import argparse, hashlib, json, os, sqlite3, subprocess, sys, time
from datetime import datetime, timezone, timedelta

# Tablo → sort key (rapor S4; anahtar/zaman sıralı yazım row-group min/max atlamasını çalıştırır — S-9 CD-YT2, A-YT6)
TABLOLAR = [
    ("kayit",            "dosya_id, sira"),
    ("referans",         "ref_turu, ref_deger"),
    ("dosya",            "dosya_id"),
    ("anahtar",          "anahtar_id"),
    ("json_kayit",       "dosya_id, satir_no, json_yolu"),
    ("karar_borcu",      "borc_id"),
    ("prompt",           "ts_utc"),
    ("hareket",          "ts_utc"),
    ("amb_olgu_kosum",   "valid_time_bas"),
    ("amb_olgu_prompt",  "valid_time"),
    ("amb_olgu_karar_borcu", "borc_id"),
    # gold martları (görünüm; DuckDB sqlite tarayıcısı görünümleri okur — 08-18 yerel teyit)
    ("v_referans_sayim", "ref_turu, ref_deger"),
    ("v_amb_kosum_maliyet", "wf_id"),
    ("v_karar_borcu_ozet", "1"),
    ("v_hareket_gunluk", "1"),
]
SAYISAL_TIPLER = {"INTEGER", "REAL", "NUMERIC", "INT", "BIGINT", "DOUBLE", "FLOAT"}


def sha1_dosya(yol):
    h = hashlib.sha1()
    with open(yol, "rb") as fh:
        h.update(fh.read())
    return h.hexdigest()


def git_head(repo):
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip() or "-"
    except Exception:
        return "-"


def sayisal_kolonlar(sq, tablo):
    """SQLite tablo/görünümün sayısal kolonları (eşdeğerlik toplamı için); görünümde tip boş kalabilir → örnek satırdan çıkarım."""
    kolonlar = []
    for cid, ad, tip, *_ in sq.execute("PRAGMA table_info(%s)" % tablo).fetchall():
        t = (tip or "").upper()
        if t in SAYISAL_TIPLER:
            kolonlar.append(ad)
    if not kolonlar:
        row = sq.execute("SELECT * FROM %s LIMIT 1" % tablo).fetchone()
        if row:
            adlar = [d[0] for d in sq.execute("SELECT * FROM %s LIMIT 1" % tablo).description]
            kolonlar = [a for a, v in zip(adlar, row) if isinstance(v, (int, float)) and not isinstance(v, bool)]
    return kolonlar


def main():
    ap = argparse.ArgumentParser(description="silver/ambar → parquet kolon-bazlı yazım (DuckDB COPY TO)")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--db", default="veri/baglam.sqlite")
    ap.add_argument("--cikti", default="veri/parquet")
    ap.add_argument("--tablo", default="", help="virgüllü alt küme; boş = hepsi")
    ap.add_argument("--row-group", type=int, default=4096, help="ROW_GROUP_SIZE (satır); küçük korpus için 4096 (S-9 CD-YT1)")
    ap.add_argument("--sessiz", action="store_true")
    ap.add_argument("--kuru", action="store_true", help="yalnız plan; yazma")
    a = ap.parse_args()

    repo = os.path.abspath(a.repo)
    db = os.path.join(repo, a.db) if not os.path.isabs(a.db) else a.db
    cikti = os.path.join(repo, a.cikti) if not os.path.isabs(a.cikti) else a.cikti
    if not os.path.exists(db):
        print("HATA: silver DB yok: %s (önce tools/katman-hatti.py)" % db, file=sys.stderr)
        return 2
    try:
        import duckdb  # noqa
    except ImportError:
        print("HATA: `duckdb` Python paketi yok (stdlib dışı bağımlılık — KB-55). Kurulum: python3 -m venv .venv && .venv/bin/pip install duckdb "
              "→ .venv/bin/python tools/ambar-parquet.py ; ya da pip3 install --user duckdb", file=sys.stderr)
        return 4

    secili = [t for t in TABLOLAR if not a.tablo or t[0] in a.tablo.split(",")]
    os.makedirs(cikti, exist_ok=True)
    head = git_head(repo)
    kod_sha = sha1_dosya(os.path.abspath(__file__))[:12]
    tz = timezone(timedelta(hours=3))
    uretim_ts = datetime.now(tz).isoformat(timespec="seconds")

    sq = sqlite3.connect(db)
    mevcut = {r[0] for r in sq.execute("SELECT name FROM sqlite_master WHERE type IN ('table','view')").fetchall()}
    con = duckdb.connect()
    con.execute("INSTALL sqlite; LOAD sqlite;")
    con.execute("ATTACH '%s' AS b (TYPE sqlite, READ_ONLY);" % db.replace("'", "''"))

    ozet, hata = [], 0
    for tablo, sort_key in secili:
        if tablo not in mevcut:
            ozet.append({"tablo": tablo, "durum": "ATLANDI", "neden": "silver'da yok"})
            continue
        hedef = os.path.join(cikti, tablo + ".parquet")
        tmp = hedef + ".tmp"
        n_sq = sq.execute("SELECT count(*) FROM %s" % tablo).fetchone()[0]
        kv = {"git_head": head, "kod_sha": kod_sha, "uretim_ts": uretim_ts, "satir": str(n_sq), "kaynak_tablo": tablo, "sort_key": sort_key,
              "duckdb": duckdb.__version__, "sqlite": sqlite3.sqlite_version}
        kv_sql = ", ".join("%s: '%s'" % (k, str(v).replace("'", "''")) for k, v in kv.items())
        sql = ("COPY (SELECT * FROM b.%s ORDER BY %s) TO '%s' (FORMAT PARQUET, COMPRESSION ZSTD, ROW_GROUP_SIZE %d, KV_METADATA {%s}, OVERWRITE_OR_IGNORE)"
               % (tablo, sort_key, tmp.replace("'", "''"), a.row_group, kv_sql))
        if a.kuru:
            ozet.append({"tablo": tablo, "durum": "KURU", "satir": n_sq, "sql": sql[:160]})
            continue
        t0 = time.perf_counter()
        con.execute(sql)
        ms = (time.perf_counter() - t0) * 1000
        # eşdeğerlik testi (yazım-anı kapısı): satır sayısı + sayısal kolon toplamları
        n_pq = con.execute("SELECT count(*) FROM read_parquet('%s')" % tmp.replace("'", "''")).fetchone()[0]
        farklar = []
        if n_pq != n_sq:
            farklar.append("satir %d != %d" % (n_pq, n_sq))
        for kol in sayisal_kolonlar(sq, tablo)[:6]:
            s1 = sq.execute('SELECT total("%s") FROM %s' % (kol, tablo)).fetchone()[0] or 0.0
            s2 = con.execute('SELECT sum(CAST("%s" AS DOUBLE)) FROM read_parquet(\'%s\')' % (kol, tmp.replace("'", "''"))).fetchone()[0] or 0.0
            if abs(float(s1) - float(s2)) > 1e-6 * max(1.0, abs(float(s1))):
                farklar.append("%s: %s != %s" % (kol, s1, s2))
        if farklar:
            hata += 1
            os.remove(tmp)
            ozet.append({"tablo": tablo, "durum": "ESDEGERLIK-FAIL", "farklar": farklar})
            continue
        os.replace(tmp, hedef)  # atomik takas (temp → rename; C-YT2)
        ozet.append({"tablo": tablo, "durum": "OK", "satir": n_sq, "byte": os.path.getsize(hedef), "ms": round(ms, 1),
                     "sort_key": sort_key, "dosya": os.path.relpath(hedef, repo)})
    con.close(); sq.close()

    if not a.sessiz:
        for o in ozet:
            print(json.dumps(o, ensure_ascii=False))
        ok = [o for o in ozet if o["durum"] == "OK"]
        print("ambar-parquet: %d OK · %d atlandı/kuru · %d FAIL · toplam %.2f MB · HEAD %s · duckdb %s" % (
            len(ok), len(ozet) - len(ok) - hata, hata, sum(o.get("byte", 0) for o in ok) / 1e6, head, duckdb.__version__))
    return 3 if hata else 0


if __name__ == "__main__":
    sys.exit(main())
