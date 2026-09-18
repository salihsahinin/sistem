#!/usr/bin/env python3
"""kolon-olcum.py — SATIR (SQLite) ↔ KOLON (DuckDB parquet/native) ölçüm aracı: aynı OLAP sorgu seti iki motorda; süre + sorgunun dokunduğu
byte + plan; append-only ölçüm kütüğü veri/kolon-olcum.jsonl (DE-artefakt; K-023 "her ship ≥1 artefakt"; deneysel m.29).
Kanıt/kural kaynağı: cc/rapor/2026-08/rapor-2026-08-18-2.md (S2 ölçüm tablosu, S4 ölçüm yöntemi; C-YT6 ClickBench disiplini: soğuk/ılık 1 + sıcak min(2,3)).

`byte` alanı iki motorda da STATİK "sorgunun dokunduğu depolama" tahminidir (fiziksel okuma değil; m.39 her rakam kaynaklı; tanım her satırda
`byte_tanimi` alanıyla damgalanır — motorlar arası kıyas aynı sınıfta ama aynı tanımda değildir, asimetri kayıtta okunur):
- SQLite (satır): dbstat sayfa tahmini. Sayılan b-tree'ler = sorgu şablonunun kullandığı tablolar ({k}→kayit, {r}→referans; plan metnindeki
  takma ad/alt-dize eşleşmesine güvenilmez) + planda `USING [COVERING] INDEX <ad>` ile geçen indeksler; plan bir tabloyu COVERING INDEX ile
  okuyorsa tablonun sayfaları yerine o indeksin sayfaları sayılır (tabloya inilmez). byte = sayfa × page_size. Satır deposunda tablo b-tree'si
  sorgu tek kolon istese de BÜTÜN kolonlarıyla sayılır — kolon atlaması yoktur, tahmin bunu yansıtır.
- DuckDB parquet (kolon): parquet kolon-chunk byte'ı. SORGULAR'daki her sorgu kaynak başına DOKUNDUĞU kolon listesini taşır ({k}: [...],
  {r}: [...]); byte = o kolonların parquet_metadata(dosya).total_compressed_size toplamı (tüm row group'lar; deterministik, statik) — kolon
  atlamanın diskteki karşılığı: sorgunun istemediği kolon toplama GİRMEZ. Listede olup dosyada olmayan kolon → FAIL-LOUD (ValueError).
- DuckDB native (bellek-içi tablo): byte None, byte_tanimi "bellek-içi tablo; byte sayacı yok".
DuckDB profil sayacı TOTAL_BYTES_READ ayrıca `duck_total_bytes_read` alanında saklanır (cpu_sn ile) — `byte` DEĞİLDİR: DuckDB 1.4.5
varsayılanlarında yerel parquet dosyasında kolon-chunk okumalarını SAYMAZ (yalnız footer/küçük okumalar; sayfa önbelleği dahil), bu yüzden
kolon atlamayı göstermez (ölçüldü: 21 kolonlu tam tarama dosyanın %1,4'ünü rapor eder); yanındaki `duck_total_bytes_read_notu` alanı bunu
satırda söyler. Kolon atlaması kanıtı `byte`tan okunur.

Kolon tarafı `duckdb` paketini ister (stdlib dışı; KB-55). Paket yoksa satır tarafı yine ölçülür, kolon satırları `durum=ATLANDI` yazılır
(FAIL-LOUD değil — ölçüm bankası büyümeye devam eder). Parquet dosyaları yoksa (tools/ambar-parquet.py koşmamışsa) parquet motoru ATLANDI.
Parquet tazeliği: duckdb-parquet/native satırlarına parquet footer KV_METADATA'sından (ambar-parquet yazar) `parquet_git_head`,
`parquet_uretim_ts` ve `parquet_bayat` (parquet git_head ≠ ölçüm anındaki HEAD) damgalanır; metadata yoksa None — satır↔kolon kıyasının
aynı silver hâline ait olup olmadığı kayıttan okunur (m.29/m.39 kendini-açıklayan kayıt).

Kullanım:
  python3 tools/kolon-olcum.py [--repo <yol>] [--db veri/baglam.sqlite] [--parquet veri/parquet] [--cikti veri/kolon-olcum.jsonl]
                               [--tekrar 3] [--sorgu Q1,Q3] [--sessiz] [--kuru]
Çıkış: 0 tamam · 2 girdi yok ya da bilinmeyen --sorgu adı (stderr'de listelenir; FAIL-LOUD). Grain: 1 satır = 1 (sorgu × motor × ölçüm) olgusu;
alanlar: ts, git_head, sorgu, motor, ilik_ms (yeni bağlantı, 1. koşum), sicak_ms (min sonraki tekrar), satir, plan (sqlite), byte, byte_tanimi,
surum, damga, (kolon) duck_total_bytes_read/duck_total_bytes_read_notu/cpu_sn, parquet_git_head/parquet_uretim_ts/parquet_bayat.
"""
import argparse, json, os, re, sqlite3, subprocess, sys, tempfile, time
from datetime import datetime, timezone, timedelta

# Sorgu seti (rapor S3 sondajıyla aynı; {k}=kayit {r}=referans yer tutucuları). Üçlü: (ad, şablon, kolonlar); kolonlar = sorgunun kaynak
# başına DOKUNDUĞU kolonlar ({k}: [...], {r}: [...]) — parquet kolon-chunk byte'ı bu listeden hesaplanır; SQL'e yeni kolon girerse liste de
# güncellenir (liste ↔ şablon uyumu testte, tools/testler/test_kolon_katmani.py).
SORGULAR = {
    "Q1": ("dosya×token group-by (2 kolon)", "SELECT dosya_id, count(*) AS n, sum(token_kestirim) AS tok FROM {k} GROUP BY 1 ORDER BY 3 DESC LIMIT 5",
           {"k": ["dosya_id", "token_kestirim"]}),
    "Q2": ("blok_turu dağılımı", "SELECT blok_turu, count(*) AS n, avg(token_kestirim) AS ort FROM {k} GROUP BY 1 ORDER BY 1",
           {"k": ["blok_turu", "token_kestirim"]}),
    "Q3": ("tarih×kayıt (ay)", "SELECT substr(tarih_iso,1,7) AS ay, count(*) AS n FROM {k} WHERE tarih_iso IS NOT NULL AND tarih_iso<>'' GROUP BY 1 ORDER BY 1",
           {"k": ["tarih_iso"]}),
    "Q4": ("referans türü×değer top", "SELECT ref_turu, ref_deger, count(*) AS c FROM {r} GROUP BY 1,2 ORDER BY c DESC, ref_turu, ref_deger LIMIT 10",
           {"r": ["ref_turu", "ref_deger"]}),
    "Q5": ("join kayit⋈referans token by ref_turu", "SELECT r.ref_turu, sum(k.token_kestirim) AS tok, count(distinct k.dosya_id) AS d FROM {r} r JOIN {k} k ON k.kayit_id=r.kayit_id GROUP BY 1 ORDER BY 1",
           {"k": ["kayit_id", "token_kestirim", "dosya_id"], "r": ["kayit_id", "ref_turu"]}),
    "Q6": ("geniş kolon: avg(length(metin))", "SELECT avg(length(metin)) AS ort FROM {k}",
           {"k": ["metin"]}),
}
YER_TUTUCU = {"k": "kayit", "r": "referans"}  # şablon yer tutucusu → silver tablo
PARQUET_BYTE_TANIMI = "parquet kolon-chunk byte (parquet_metadata total_compressed_size; sorgunun dokunduğu kolonlar; statik)"
NATIVE_BYTE_TANIMI = "bellek-içi tablo; byte sayacı yok"
DUCK_TBR_NOTU = ("DuckDB profil sayacı TOTAL_BYTES_READ; 1.4.5 varsayılanlarında yerel parquet kolon-chunk okumalarını SAYMAZ "
                 "(yalnız footer/küçük okumalar; sayfa önbelleği dahil, fiziksel disk değil) — kolon atlama kanıtı değildir, `byte` alanına bak")
PLAN_INDEKS = re.compile(r"USING (COVERING )?INDEX (\S+)")


def git_head(repo):
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip() or "-"
    except Exception:
        return "-"


def sql_metin(s):
    """SQL tek-tırnak sabiti için kaçış (yol içindeki ' → '')."""
    return str(s).replace("'", "''")


def sorgu_sec(secim):
    """--sorgu virgüllü listesi → (seçili sorgu adları, bilinmeyen adlar). Boş = hepsi; virgül çevresi boşluk kırpılır;
    SORGULAR'da olmayan ad sessizce düşmez, bilinmeyen listesine gider (çağıran FAIL-LOUD çıkış 2 verir)."""
    adlar = [x.strip() for x in secim.split(",") if x.strip()]
    if not adlar:
        return list(SORGULAR), []
    return [q for q in SORGULAR if q in adlar], [x for x in adlar if x not in SORGULAR]


def sablon_tablolari(sablon):
    """Sorgu şablonunun kullandığı silver tabloları (yer tutucudan; {k}→kayit, {r}→referans)."""
    return [t for yt, t in YER_TUTUCU.items() if "{%s}" % yt in sablon]


def plan_nesneleri(plan, tablolar, indeks_tablo):
    """EXPLAIN QUERY PLAN metni + şablon tabloları → dbstat'ta sayılacak b-tree adları (küme).
    tablolar: şablonun kullandığı tablo adları; indeks_tablo: {indeks adı: tablo adı} (sqlite_master). Kural: her şablon tablosu sayılır,
    planda 'USING [COVERING] INDEX <ad>' geçen indeksler eklenir; COVERING INDEX'in tablosunun kendi sayfaları sayılmaz (tabloya inilmez).
    Takma ad (SCAN k, SEARCH r) ve alt-dize eşleşmesi kullanılmaz."""
    nesneler, kaplayan = set(), set()
    for kaplayici, indeks in PLAN_INDEKS.findall(plan):
        nesneler.add(indeks)
        if kaplayici:
            kaplayan.add(indeks_tablo.get(indeks))
    nesneler.update(t for t in tablolar if t not in kaplayan)
    return nesneler


def zamanla(baglan, sorgula, kapat, tekrar):
    """ılık = YENİ bağlantıda 1. koşum (bağlantı/eklenti/yükleme dahil); sıcak = AYNI bağlantıda sonraki (tekrar-1) koşumun min'i
    (C-YT6 disiplini: 1 soğuk/ılık + min(2.,3.)). Böylece native modda tablo yüklemesi yalnız ılık süreye girer."""
    t0 = time.perf_counter(); con = baglan(); rows = sorgula(con); ilik = (time.perf_counter() - t0) * 1000
    sicak = None
    for _ in range(max(1, tekrar - 1)):
        t0 = time.perf_counter(); sorgula(con); dt = (time.perf_counter() - t0) * 1000
        sicak = dt if sicak is None else min(sicak, dt)
    kapat(con)
    return ilik, sicak, rows


def sqlite_olc(db, sorgu_sql, tekrar, tablolar):
    """Satır motoru ölçümü; tablolar = şablonun kullandığı tablo adları (dbstat tahmini için, bkz. modül docstring kuralı)."""
    ilik, sicak, rows = zamanla(lambda: sqlite3.connect(db), lambda c: c.execute(sorgu_sql).fetchall(), lambda c: c.close(), tekrar)
    con = sqlite3.connect(db)
    try:
        plan = " | ".join(r[3] for r in con.execute("EXPLAIN QUERY PLAN " + sorgu_sql).fetchall())
        indeks_tablo = dict(con.execute("SELECT name, tbl_name FROM sqlite_master WHERE type='index'").fetchall())
        nesneler = plan_nesneleri(plan, tablolar, indeks_tablo)
        page_size = con.execute("PRAGMA page_size").fetchone()[0]
        sayfa = 0
        try:
            for ad in sorted(nesneler):
                sayfa += con.execute("SELECT count(*) FROM dbstat WHERE name=?", (ad,)).fetchone()[0]
        except sqlite3.OperationalError:
            sayfa = -1  # dbstat derlenmemiş
    finally:
        con.close()
    return {"ilik_ms": round(ilik, 3), "sicak_ms": round(sicak, 3), "satir": len(rows), "plan": plan[:300],
            "byte": (sayfa * page_size if sayfa >= 0 else None),
            "byte_tanimi": "dbstat sayfa×page_size (şablon tabloları + plandaki USING INDEX; COVERING → tablo yerine indeks; statik tahmin)"}


def duckdb_olc(duckdb, kaynak_sql_uret, sorgu_sql_sablon, tekrar):
    """kaynak_sql_uret(con) → {k},{r} için FROM ifadeleri döner (parquet ya da native). Tutamaç = (bağlantı, sql) çifti.
    Profil JSON'u geçici dizine yazılır (repo'ya dokunulmaz), koşum sonunda silinir. Döner: süreler + satır + duck_total_bytes_read (+ notu)
    + cpu_sn; `byte`/`byte_tanimi` çağıranda motor türüne göre eklenir (parquet → parquet_kolon_byte, native → None)."""
    def yeni():
        con = duckdb.connect()
        k, r = kaynak_sql_uret(con)
        return (con, sorgu_sql_sablon.format(k=k, r=r))
    ilik, sicak, rows = zamanla(yeni, lambda h: h[0].execute(h[1]).fetchall(), lambda h: h[0].close(), tekrar)
    # profil (TOTAL_BYTES_READ + CPU): ayrı bağlantı, tek koşum; TOTAL_BYTES_READ `byte` değildir (bkz. modül docstring / DUCK_TBR_NOTU)
    con, sql = yeni()
    tbr = cpu = None
    try:
        with tempfile.TemporaryDirectory(prefix="kolon-olcum-") as tmpdir:
            prof = os.path.join(tmpdir, "prof.json")
            con.execute("PRAGMA enable_profiling='json'"); con.execute("PRAGMA profiling_output='%s'" % sql_metin(prof))
            con.execute("PRAGMA custom_profiling_settings='{\"TOTAL_BYTES_READ\":\"true\",\"CPU_TIME\":\"true\",\"OPERATOR_ROWS_SCANNED\":\"true\"}'")
            con.execute(sql).fetchall(); con.execute("PRAGMA disable_profiling")
            with open(prof, encoding="utf-8") as fh:
                j = json.load(fh)
            tbr = j.get("total_bytes_read"); cpu = j.get("cpu_time")
    except Exception:  # profil desteklenmiyorsa ölçüm yine kaydedilir (sayaç/cpu None)
        tbr = None; cpu = None
    finally:
        con.close()
    return {"ilik_ms": round(ilik, 3), "sicak_ms": round(sicak, 3), "satir": len(rows),
            "duck_total_bytes_read": tbr, "duck_total_bytes_read_notu": DUCK_TBR_NOTU, "cpu_sn": cpu}


def parquet_kolon_byte(duckdb, yollar, kolonlar):
    """Sorgunun dokunduğu kolonların parquet kolon-chunk byte toplamı (kolon tarafı `byte`): kaynak başına ({k}/{r} → dosya)
    parquet_metadata(dosya).total_compressed_size, path_in_schema ∈ kolon listesi, TÜM row group'lar toplanır. Statik ve deterministik
    (dosya değişmedikçe aynı) — DuckDB'nin fiilen okuduğu değil, kolon atlamanın DİSKTEKİ karşılığı; SQLite dbstat tahminiyle aynı sınıf.
    yollar: {"k": kayit.parquet, "r": referans.parquet}; kolonlar: {"k": [...], "r": [...]} (SORGULAR üçlüsünün 3. öğesi).
    Listede olup dosyada bulunmayan kolon → ValueError (FAIL-LOUD; sessiz 0 sayılıp toplam düşmez)."""
    toplam = 0
    con = duckdb.connect()
    try:
        for yt, kols in kolonlar.items():
            if not kols:
                continue
            yol = yollar[yt]
            # dosyadaki her kolonun chunk toplamı (row group'lar üstünden); süzme Python'da (uzun IN (?,…) listesi DuckDB parametre
            # tip çıkarımını şaşırtıyor)
            dosyadaki = dict(con.execute(
                "SELECT path_in_schema, sum(total_compressed_size) FROM parquet_metadata(?) GROUP BY 1", [yol]).fetchall())
            eksik = [k for k in kols if k not in dosyadaki]
            if eksik:
                raise ValueError("parquet_kolon_byte: %s dosyasında olmayan kolon: %s" % (os.path.basename(yol), ", ".join(map(str, eksik))))
            toplam += int(sum(dosyadaki[k] for k in set(kols)))
    finally:
        con.close()
    return toplam


def parquet_damga(duckdb, yollar, head):
    """Parquet footer KV_METADATA'sından tazelik damgası (dosya başına BİR okuma; ambar-parquet git_head/uretim_ts yazar).
    yollar: {tablo: parquet yolu}. Döner: parquet_git_head, parquet_uretim_ts (dosyalar aynıysa tek değer, değilse 'tablo=değer|…'),
    parquet_bayat (herhangi bir dosyanın git_head'i ölçüm HEAD'inden farklıysa True; metadata eksikse None)."""
    okunan = {}
    con = duckdb.connect()
    try:
        for tablo, yol in yollar.items():
            kv = {}
            try:
                for k, v in con.execute("SELECT key, value FROM parquet_kv_metadata(?)", [yol]).fetchall():
                    k = k.decode() if isinstance(k, (bytes, bytearray)) else k
                    v = v.decode() if isinstance(v, (bytes, bytearray)) else v
                    kv[k] = v
            except duckdb.Error:
                kv = {}
            okunan[tablo] = (kv.get("git_head"), kv.get("uretim_ts"))
    finally:
        con.close()

    def tek(i):
        degerler = {d[i] for d in okunan.values()}
        if len(degerler) == 1:
            return next(iter(degerler))
        return "|".join("%s=%s" % (t, d[i]) for t, d in sorted(okunan.items()))
    heads = [d[0] for d in okunan.values()]
    bayat = None if any(h is None for h in heads) else any(h != head for h in heads)
    return {"parquet_git_head": tek(0), "parquet_uretim_ts": tek(1), "parquet_bayat": bayat}


def main():
    ap = argparse.ArgumentParser(description="satır (SQLite) ↔ kolon (DuckDB parquet/native) ölçüm; append-only kütük")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--db", default="veri/baglam.sqlite")
    ap.add_argument("--parquet", default="veri/parquet")
    ap.add_argument("--cikti", default="veri/kolon-olcum.jsonl")
    ap.add_argument("--tekrar", type=int, default=3)
    ap.add_argument("--sorgu", default="", help="virgüllü alt küme (Q1..Q6); boş = hepsi; bilinmeyen ad → çıkış 2")
    ap.add_argument("--sessiz", action="store_true")
    ap.add_argument("--kuru", action="store_true", help="kütüğe yazma, yalnız ekrana")
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)
    yol = lambda p: p if os.path.isabs(p) else os.path.join(repo, p)
    db, pq, cikti = yol(a.db), yol(a.parquet), yol(a.cikti)
    if not os.path.exists(db):
        print("HATA: silver DB yok: %s" % db, file=sys.stderr); return 2
    secili, bilinmeyen = sorgu_sec(a.sorgu)
    if bilinmeyen:
        print("HATA: bilinmeyen --sorgu adı: %s · geçerli adlar: %s" % (", ".join(bilinmeyen), ", ".join(SORGULAR)), file=sys.stderr)
        return 2
    tz = timezone(timedelta(hours=3)); ts = datetime.now(tz).isoformat(timespec="seconds"); head = git_head(repo)
    ortak = {"ts": ts, "git_head": head, "tekrar": a.tekrar, "sqlite": sqlite3.sqlite_version, "damga": "deneysel m.29; ılık = yeni bağlantı 1. koşum, sıcak = min(sonraki)"}
    try:
        import duckdb
        ortak["duckdb"] = duckdb.__version__
    except ImportError:
        duckdb = None
        ortak["duckdb"] = None
    kp, rp = os.path.join(pq, "kayit.parquet"), os.path.join(pq, "referans.parquet")
    pq_var = duckdb is not None and os.path.exists(kp) and os.path.exists(rp)
    damga = parquet_damga(duckdb, {"kayit": kp, "referans": rp}, head) if pq_var else {}

    satirlar = []
    for q in secili:
        ad, sablon, kolonlar = SORGULAR[q]
        # 1) satır motoru
        r = sqlite_olc(db, sablon.format(k="kayit", r="referans"), a.tekrar, sablon_tablolari(sablon))
        satirlar.append(dict(ortak, sorgu=q, sorgu_adi=ad, motor="sqlite", durum="OK", **r))
        # 2) kolon motoru — parquet
        if pq_var:
            r = duckdb_olc(duckdb, lambda con: ("read_parquet('%s')" % sql_metin(kp), "read_parquet('%s')" % sql_metin(rp)), sablon, a.tekrar)
            r["byte"] = parquet_kolon_byte(duckdb, {"k": kp, "r": rp}, kolonlar); r["byte_tanimi"] = PARQUET_BYTE_TANIMI
            satirlar.append(dict(ortak, sorgu=q, sorgu_adi=ad, motor="duckdb-parquet", durum="OK", **r, **damga))
            # 3) kolon motoru — native (bellek-içi tablo; depolama biçimi arşiv değil, önbellek — B-YT5)
            def native(con, kp=kp, rp=rp):
                con.execute("CREATE TABLE kayit AS SELECT * FROM read_parquet('%s')" % sql_metin(kp))
                con.execute("CREATE TABLE referans AS SELECT * FROM read_parquet('%s')" % sql_metin(rp))
                return "kayit", "referans"
            r = duckdb_olc(duckdb, native, sablon, a.tekrar)
            r["byte"] = None; r["byte_tanimi"] = NATIVE_BYTE_TANIMI
            r["not"] = "ılık süresi tablo yüklemesini (CREATE TABLE AS) içerir; sıcak = yüklü tabloda min tekrar"
            satirlar.append(dict(ortak, sorgu=q, sorgu_adi=ad, motor="duckdb-native", durum="OK", **r, **damga))
        else:
            neden = "duckdb paketi yok" if duckdb is None else "parquet yok (tools/ambar-parquet.py koş)"
            for m in ("duckdb-parquet", "duckdb-native"):
                satirlar.append(dict(ortak, sorgu=q, sorgu_adi=ad, motor=m, durum="ATLANDI", neden=neden))
    if not a.kuru:
        with open(cikti, "a", encoding="utf-8") as fh:
            for s in satirlar:
                fh.write(json.dumps(s, ensure_ascii=False) + "\n")
    if not a.sessiz:
        print("%-4s %-16s %-8s %10s %10s %12s %s" % ("sorgu", "motor", "durum", "ılık ms", "sıcak ms", "byte", "satır"))
        for s in satirlar:
            print("%-4s %-16s %-8s %10s %10s %12s %s" % (s["sorgu"], s["motor"], s["durum"], s.get("ilik_ms", "-"), s.get("sicak_ms", "-"),
                                                          "-" if s.get("byte") is None else s["byte"], s.get("satir", "-")))
        print("kolon-olcum: %d satır → %s (%s) · HEAD %s · sqlite %s · duckdb %s%s" % (
            len(satirlar), os.path.relpath(cikti, repo), "KURU" if a.kuru else "eklendi", head, ortak["sqlite"], ortak["duckdb"],
            (" · parquet HEAD %s%s" % (damga["parquet_git_head"], " (BAYAT)" if damga["parquet_bayat"] else "")) if damga else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
