#!/usr/bin/env python3
"""Kolon katmanı testleri (pipeline cc/pipeline-2026-08-18-kolon-katmani.md SH-1/SH-2; stdlib unittest, Python 3.9).
Koş: python3 -m unittest discover -s tools/testler -p 'test_*.py' -v
Davranış testleri: araçlar KÜÇÜK geçici bir silver DB üzerinde çalıştırılır (repo verisine dokunulmaz); çıkış kodu, üretilen dosya ve
kütük satırları (public çıktı sözleşmesi) doğrulanır. DuckDB gerektiren testler paket yoksa ATLANIR (skip) — stdlib tarafı her yerde koşar.
"""
import json, os, shutil, sqlite3, subprocess, sys, tempfile, unittest, importlib.util

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOLS = os.path.join(REPO, "tools")
try:
    import duckdb  # noqa
    DUCKDB = True
except ImportError:
    DUCKDB = False


def kucuk_silver(yol):
    """kayit + referans + karar_borcu şemasının gerekli alt kümesiyle 3 satırlık DB (kolon-olcum Q1-Q6 + ambar-parquet için yeterli)."""
    con = sqlite3.connect(yol)
    con.executescript("""
    CREATE TABLE kayit (kayit_id TEXT PRIMARY KEY, dosya_id TEXT, sira INTEGER, blok_turu TEXT, satir_bas INTEGER, satir_son INTEGER,
                        metin TEXT, token_kestirim INTEGER, tarih_iso TEXT);
    CREATE INDEX ix_kayit_dosya ON kayit(dosya_id, sira);
    INSERT INTO kayit VALUES ('a.md#1-1#x1','a.md',0,'baslik',1,1,'# A',2,'2026-08-18'),
                             ('a.md#3-4#x2','a.md',1,'paragraf',3,4,'metin metin',5,NULL),
                             ('b.md#1-1#x3','b.md',0,'madde',1,1,'- b',3,'2026-08-17');
    CREATE TABLE referans (kayit_id TEXT, ref_turu TEXT, ref_deger TEXT, ham TEXT, konum INTEGER);
    CREATE INDEX ix_ref_kayit ON referans(kayit_id);
    INSERT INTO referans VALUES ('a.md#1-1#x1','kart','K-015','K-015',0), ('b.md#1-1#x3','kart','K-015','K-015',2), ('b.md#1-1#x3','v_no','V26','V26',5);
    CREATE TABLE karar_borcu (borc_id TEXT PRIMARY KEY, baslik TEXT, katman INTEGER);
    INSERT INTO karar_borcu VALUES ('KB-01','a',1), ('KB-02','b',2);
    """)
    con.commit(); con.close()


def oku_jsonl(yol):
    with open(yol, encoding="utf-8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


def kos(script, *args, py=sys.executable):
    return subprocess.run([py, os.path.join(TOOLS, script)] + list(args), cwd=REPO, capture_output=True, text=True)


class KolonOlcumTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="kolon-test-")
        self.db = os.path.join(self.tmp, "silver.sqlite"); kucuk_silver(self.db)
        self.kutuk = os.path.join(self.tmp, "kolon-olcum.jsonl")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_db_yoksa_cikis_2(self):
        r = kos("kolon-olcum.py", "--db", os.path.join(self.tmp, "yok.sqlite"), "--kuru", "--sessiz")
        self.assertEqual(r.returncode, 2, r.stderr)

    def test_kuru_kosum_kutuge_yazmaz(self):
        r = kos("kolon-olcum.py", "--db", self.db, "--parquet", self.tmp, "--cikti", self.kutuk, "--kuru", "--sessiz")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertFalse(os.path.exists(self.kutuk))

    def test_satir_motoru_her_sorguda_olcer_ve_kutuk_grain(self):
        # parquet dosyası verilmedi → kolon satırları ATLANDI; sqlite satırları OK; grain = sorgu × motor
        r = kos("kolon-olcum.py", "--db", self.db, "--parquet", os.path.join(self.tmp, "pq-yok"), "--cikti", self.kutuk, "--sessiz", "--tekrar", "2")
        self.assertEqual(r.returncode, 0, r.stderr)
        satirlar = oku_jsonl(self.kutuk)
        self.assertEqual(len(satirlar), 6 * 3)  # 6 sorgu × 3 motor
        sq = [s for s in satirlar if s["motor"] == "sqlite"]
        self.assertEqual(len(sq), 6)
        for s in sq:
            self.assertEqual(s["durum"], "OK")
            for alan in ("ts", "git_head", "sorgu", "ilik_ms", "sicak_ms", "satir", "plan", "byte_tanimi", "sqlite"):
                self.assertIn(alan, s)
            self.assertGreaterEqual(s["ilik_ms"], 0.0)
        atl = [s for s in satirlar if s["motor"].startswith("duckdb")]
        self.assertTrue(all(s["durum"] == "ATLANDI" and "neden" in s for s in atl))
        # Q1 sonucu küçük DB'de: 2 dosya → satir=2 ; Q4: 2 (kart K-015, v_no V26)
        q1 = [s for s in sq if s["sorgu"] == "Q1"][0]; self.assertEqual(q1["satir"], 2)
        q4 = [s for s in sq if s["sorgu"] == "Q4"][0]; self.assertEqual(q4["satir"], 2)

    def test_sorgu_alt_kumesi(self):
        r = kos("kolon-olcum.py", "--db", self.db, "--parquet", self.tmp, "--cikti", self.kutuk, "--sessiz", "--sorgu", "Q1,Q6")
        self.assertEqual(r.returncode, 0, r.stderr)
        satirlar = oku_jsonl(self.kutuk)
        self.assertEqual(sorted({s["sorgu"] for s in satirlar}), ["Q1", "Q6"])


@unittest.skipUnless(DUCKDB, "duckdb paketi yok — kolon tarafı testleri atlandı (KB-55)")
class AmbarParquetTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="parquet-test-")
        self.db = os.path.join(self.tmp, "silver.sqlite"); kucuk_silver(self.db)
        self.pq = os.path.join(self.tmp, "parquet")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_kuru_dosya_yazmaz(self):
        r = kos("ambar-parquet.py", "--db", self.db, "--cikti", self.pq, "--kuru", "--sessiz")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertFalse(os.path.exists(os.path.join(self.pq, "kayit.parquet")))

    def test_ihrac_esdegerlik_ve_kv_metadata(self):
        r = kos("ambar-parquet.py", "--db", self.db, "--cikti", self.pq, "--tablo", "kayit,referans,karar_borcu")
        self.assertEqual(r.returncode, 0, r.stderr + r.stdout)
        import duckdb
        con = duckdb.connect()
        for tablo, n in (("kayit", 3), ("referans", 3), ("karar_borcu", 2)):
            yol = os.path.join(self.pq, tablo + ".parquet")
            self.assertTrue(os.path.exists(yol), tablo)
            self.assertFalse(os.path.exists(yol + ".tmp"))  # atomik takas: tmp kalmaz
            self.assertEqual(con.execute("SELECT count(*) FROM read_parquet(?)", [yol]).fetchone()[0], n)
            kv = dict((k.decode() if isinstance(k, (bytes, bytearray)) else k, v.decode() if isinstance(v, (bytes, bytearray)) else v)
                      for k, v in con.execute("SELECT key, value FROM parquet_kv_metadata(?)", [yol]).fetchall())
            for anahtar in ("git_head", "kod_sha", "uretim_ts", "satir", "kaynak_tablo", "sort_key"):
                self.assertIn(anahtar, kv, tablo)
            self.assertEqual(kv["satir"], str(n)); self.assertEqual(kv["kaynak_tablo"], tablo)
        # sort key uygulanmış mı: kayit dosya_id, sira sırası
        sira = con.execute("SELECT dosya_id, sira FROM read_parquet(?)", [os.path.join(self.pq, "kayit.parquet")]).fetchall()
        self.assertEqual(sira, sorted(sira))
        # atlanan tablo (silver'da yok) çıktı özetinde ATLANDI olarak görünür, koşum düşmez
        r2 = kos("ambar-parquet.py", "--db", self.db, "--cikti", self.pq, "--tablo", "kayit,olmayan_tablo")
        self.assertEqual(r2.returncode, 0, r2.stderr)
        # sadece --tablo ile verilen VE TABLOLAR listesinde olan işlenir; 'olmayan_tablo' listede yok → sessizce dışarıda kalır
        self.assertNotIn("olmayan_tablo", r2.stdout)

    def test_kolon_olcum_parquet_ile(self):
        kos("ambar-parquet.py", "--db", self.db, "--cikti", self.pq, "--tablo", "kayit,referans", "--sessiz")
        kutuk = os.path.join(self.tmp, "k.jsonl")
        r = kos("kolon-olcum.py", "--db", self.db, "--parquet", self.pq, "--cikti", kutuk, "--sessiz", "--sorgu", "Q1,Q5")
        self.assertEqual(r.returncode, 0, r.stderr)
        satirlar = oku_jsonl(kutuk)
        self.assertEqual(len(satirlar), 2 * 3)
        for s in satirlar:
            self.assertEqual(s["durum"], "OK", s)
        # aynı sorgu iki motorda aynı satır sayısı (eşdeğerlik)
        for q in ("Q1", "Q5"):
            n = {s["motor"]: s["satir"] for s in satirlar if s["sorgu"] == q}
            self.assertEqual(len(set(n.values())), 1, n)


class KatmanHattiSecimTest(unittest.TestCase):
    def test_parquet_adimi_varsayilan_kapali_bayrakla_acik(self):
        sp = importlib.util.spec_from_file_location("kh", os.path.join(TOOLS, "katman-hatti.py"))
        m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
        temel = [a for a, _ in m.adimlari_sec()]
        self.assertNotIn("parquet", temel); self.assertNotIn("kolon-olcum", temel)
        acik = [a for a, _ in m.adimlari_sec(parquet=True)]
        self.assertEqual(acik[-2:], ["parquet", "kolon-olcum"])
        self.assertEqual([a for a, _ in m.adimlari_sec(parquet=True, atla=("kolon-olcum", "baglam"))][-1], "parquet")
        self.assertIn(4, m.ATLANDI_KODLARI["parquet"])  # duckdb yoksa hat düşmez


if __name__ == "__main__":
    unittest.main()
