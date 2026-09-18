#!/usr/bin/env python3
"""Kolon katmanı testleri (pipeline cc/pipeline-2026-08-18-kolon-katmani.md SH-1/SH-2; stdlib unittest, Python 3.9).
Koş: python3 -m unittest discover -s tools/testler -p 'test_*.py' -v
Davranış testleri: araçlar KÜÇÜK geçici bir silver DB üzerinde çalıştırılır (repo verisine dokunulmaz); çıkış kodu, üretilen dosya ve
kütük satırları (public çıktı sözleşmesi) doğrulanır. DuckDB gerektiren testler paket yoksa ATLANIR (skip) — stdlib tarafı her yerde koşar.
"""
import contextlib, hashlib, io, json, os, shutil, sqlite3, subprocess, sys, tempfile, types, unittest, importlib.util
from unittest import mock

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


def modul(script):
    """tools/<script> dosyasını (tire içeren ad) modül olarak yükler — public fonksiyonları doğrudan çağırmak için."""
    sp = importlib.util.spec_from_file_location(script.replace("-", "_").replace(".py", ""), os.path.join(TOOLS, script))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    return m


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
        # --repo geçici dizin: koşum sonunda dizinde YENİ hiçbir şey olmamalı (kütük yok, çalışma dizini yok — yalnız bu koşumun davranışı)
        once = sorted(os.listdir(self.tmp))
        r = kos("kolon-olcum.py", "--repo", self.tmp, "--db", self.db, "--parquet", self.tmp, "--cikti", self.kutuk, "--kuru", "--sessiz")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertFalse(os.path.exists(self.kutuk))
        self.assertEqual(sorted(os.listdir(self.tmp)), once)

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
        r = kos("kolon-olcum.py", "--db", self.db, "--parquet", self.tmp, "--cikti", self.kutuk, "--sessiz", "--sorgu", "Q1, Q6")
        self.assertEqual(r.returncode, 0, r.stderr)
        satirlar = oku_jsonl(self.kutuk)
        self.assertEqual(sorted({s["sorgu"] for s in satirlar}), ["Q1", "Q6"])

    def test_bilinmeyen_sorgu_adi_cikis_2(self):
        # FAIL-LOUD: yazım hatalı --sorgu sessiz no-op DEĞİL → çıkış 2 + stderr'de ad; kütüğe satır yazılmaz
        r = kos("kolon-olcum.py", "--db", self.db, "--parquet", self.tmp, "--cikti", self.kutuk, "--sessiz", "--sorgu", "Q1,Q9")
        self.assertEqual(r.returncode, 2, r.stdout)
        self.assertIn("Q9", r.stderr)
        self.assertFalse(os.path.exists(self.kutuk))

    def test_dbstat_tahmini_sablon_tablolari_ve_plan_indeksleri(self):
        # dbstat sayfa tahmini: şablon tabloları + plandaki USING INDEX; takma ad/alt-dize eşleşmesi yok; COVERING → tablo yerine indeks
        m = modul("kolon-olcum.py")
        it = {"ix_kayit_dosya": "kayit", "ix_ref_tur_deger": "referans", "sqlite_autoindex_kayit_1": "kayit"}
        # Q1 planı: 'dosya' alt-dizesi tablo adı olarak sayılmaz; kayit + indeksi sayılır
        self.assertEqual(m.plan_nesneleri("SCAN kayit USING INDEX ix_kayit_dosya", ["kayit"], it), {"kayit", "ix_kayit_dosya"})
        # Q5 planı takma adlı (r/k): referans planda geçmese de şablondan sayılır; iki indeks eklenir
        self.assertEqual(m.plan_nesneleri("SCAN r USING INDEX ix_ref_tur_deger | SEARCH k USING INDEX sqlite_autoindex_kayit_1",
                                          ["referans", "kayit"], it),
                         {"referans", "kayit", "ix_ref_tur_deger", "sqlite_autoindex_kayit_1"})
        # COVERING INDEX: tablonun sayfaları yerine indeksinki
        self.assertEqual(m.plan_nesneleri("SCAN kayit USING COVERING INDEX ix_kayit_dosya", ["kayit"], it), {"ix_kayit_dosya"})
        # AUTOMATIC/PRIMARY KEY erişimi indeks adı üretmez → yalnız tablo
        self.assertEqual(m.plan_nesneleri("SCAN kayit | SEARCH referans USING AUTOMATIC COVERING INDEX (kayit_id=?)", ["kayit", "referans"], it),
                         {"kayit", "referans"})
        self.assertEqual(m.sablon_tablolari(m.SORGULAR["Q5"][1]), ["kayit", "referans"])
        self.assertEqual(m.sablon_tablolari(m.SORGULAR["Q4"][1]), ["referans"])
        # uçtan uca: küçük DB'de Q1 satır motoru byte tahmini (dbstat varsa) kayit + ix_kayit_dosya sayfaları = 2 sayfa × page_size
        r = m.sqlite_olc(self.db, m.SORGULAR["Q1"][1].format(k="kayit", r="referans"), 2, ["kayit"])
        con = sqlite3.connect(self.db)
        try:
            page_size = con.execute("PRAGMA page_size").fetchone()[0]
            try:
                beklenen = sum(con.execute("SELECT count(*) FROM dbstat WHERE name=?", (ad,)).fetchone()[0] for ad in ("kayit", "ix_kayit_dosya"))
            except sqlite3.OperationalError:
                beklenen = None
        finally:
            con.close()
        if beklenen is None:
            self.assertIsNone(r["byte"])
        else:
            self.assertIn("ix_kayit_dosya", r["plan"])
            self.assertEqual(r["byte"], beklenen * page_size)

    def test_sorgu_kolon_listesi_sorgunun_dokundugu_kolonlarla_birebir(self):
        # SORGULAR üçlüsünün kolon listesi (parquet kolon-chunk byte'ının girdisi) sorgunun DOKUNDUĞU kolon kümesiyle birebir olmalı;
        # tüketici olarak SQLite'ın kendisi koşturulur: (1) her kaynağı YALNIZ listedeki kolonları açan görünümle değiştirince sorgu koşar
        # (liste eksiksiz → byte eksik sayılmaz); (2) listeden herhangi bir (kaynak, kolon) düşülünce sorgu 'no such column' ile düşer
        # (listede fazlalık yok → byte fazla sayılmaz). Ayrıca liste anahtarları = şablonun kullandığı yer tutucular.
        m = modul("kolon-olcum.py")
        con = sqlite3.connect(self.db)
        try:
            for q, (ad, sablon, kolonlar) in m.SORGULAR.items():
                self.assertEqual(sorted(kolonlar), sorted(yt for yt in m.YER_TUTUCU if "{%s}" % yt in sablon), q)
                self.assertTrue(all(kols for kols in kolonlar.values()), q)

                def gorunumlu(cikar=None):
                    adlar = {}
                    for yt, kols in kolonlar.items():
                        secim = [k for k in kols if (yt, k) != cikar]
                        con.execute("DROP VIEW IF EXISTS temp.g_%s" % yt)
                        con.execute("CREATE TEMP VIEW g_%s AS SELECT %s FROM %s" % (yt, ", ".join(secim) if secim else "1 AS bos", m.YER_TUTUCU[yt]))
                        adlar[yt] = "g_%s" % yt
                    return sablon.format(**{yt: adlar.get(yt, m.YER_TUTUCU[yt]) for yt in m.YER_TUTUCU})
                con.execute(gorunumlu()).fetchall()
                for yt, kols in kolonlar.items():
                    for k in kols:
                        with self.assertRaises(sqlite3.OperationalError, msg="%s: %s.%s listede fazla" % (q, yt, k)):
                            con.execute(gorunumlu(cikar=(yt, k))).fetchall()
        finally:
            con.close()


class AmbarParquetGirdiTest(unittest.TestCase):
    """duckdb gerektirmeyen girdi sözleşmesi (bağımlılık denetiminden ÖNCE): DB yok → 2, bilinmeyen tablo adı → 2 (FAIL-LOUD)."""
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="parquet-girdi-")
        self.db = os.path.join(self.tmp, "silver.sqlite"); kucuk_silver(self.db)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_db_yoksa_cikis_2(self):
        r = kos("ambar-parquet.py", "--db", os.path.join(self.tmp, "yok.sqlite"), "--cikti", self.tmp, "--kuru")
        self.assertEqual(r.returncode, 2, r.stderr)

    def test_bilinmeyen_tablo_adi_cikis_2(self):
        r = kos("ambar-parquet.py", "--db", self.db, "--cikti", os.path.join(self.tmp, "pq"), "--tablo", "kayit, olmayan_tablo", "--kuru")
        self.assertEqual(r.returncode, 2, r.stdout)
        self.assertIn("olmayan_tablo", r.stderr)
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "pq")))

    def test_bozuk_db_cikis_2(self):
        bozuk = os.path.join(self.tmp, "bozuk.sqlite")
        with open(bozuk, "w") as fh:
            fh.write("bu bir sqlite dosyası değil")
        r = kos("ambar-parquet.py", "--db", bozuk, "--cikti", os.path.join(self.tmp, "pq"), "--tablo", "kayit", "--sessiz")
        self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
        self.assertNotIn("Traceback", r.stderr)

    def test_tablo_sec_bosluk_kirpar_ve_bilinmeyeni_ayirir(self):
        m = modul("ambar-parquet.py")
        secili, bilinmeyen = m.tablo_sec(" kayit , referans,kayıt")
        self.assertEqual([t for t, _ in secili], ["kayit", "referans"]); self.assertEqual(bilinmeyen, ["kayıt"])
        self.assertEqual(m.tablo_sec("")[0], m.TABLOLAR); self.assertEqual(m.tablo_sec("")[1], [])

    def test_hata_metni_bos_mesajda_dusmez(self):
        m = modul("ambar-parquet.py")
        self.assertEqual(m.hata_metni(ValueError("")), "ValueError: ")
        self.assertEqual(m.hata_metni(ValueError("ilk satır\nikinci")), "ValueError: ilk satır")

    def test_sqlite_eklentisi_yuklenemezse_cikis_4(self):
        # duckdb var ama INSTALL/LOAD/ATTACH düşüyor (çevrimdışı eklenti indirimi vb.) → çıkış 4 + stderr yönergesi, traceback yok,
        # dosya üretilmez. Sahte duckdb modülüyle sürülür: paket kurulu olmasa da güvence yolu her yerde test edilir.
        m = modul("ambar-parquet.py")

        class SahteHata(Exception):
            pass

        class SahteBaglanti:
            def execute(self, sql):
                raise SahteHata("IO Error: Failed to download extension \"sqlite_scanner\" (sahte)")

            def close(self):
                pass

        sahte = types.ModuleType("duckdb"); sahte.Error = SahteHata; sahte.__version__ = "0-sahte"; sahte.connect = lambda: SahteBaglanti()
        argv = ["ambar-parquet.py", "--db", self.db, "--cikti", os.path.join(self.tmp, "pq"), "--tablo", "kayit"]
        err = io.StringIO()
        with mock.patch.dict(sys.modules, {"duckdb": sahte}), mock.patch.object(sys, "argv", argv), contextlib.redirect_stderr(err):
            kod = m.main()
        self.assertEqual(kod, 4, err.getvalue())
        self.assertIn("eklenti", err.getvalue()); self.assertIn("sahte", err.getvalue())
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "pq", "kayit.parquet")))


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
        # TABLOLAR'da olan ama bu silver'da bulunmayan tablo (prompt) özette ATLANDI olarak görünür, koşum düşmez, dosya üretilmez
        r2 = kos("ambar-parquet.py", "--db", self.db, "--cikti", self.pq, "--tablo", "kayit,prompt")
        self.assertEqual(r2.returncode, 0, r2.stderr)
        ozet = {o["tablo"]: o for o in (json.loads(l) for l in r2.stdout.splitlines() if l.startswith("{"))}
        self.assertEqual(ozet["prompt"]["durum"], "ATLANDI"); self.assertEqual(ozet["kayit"]["durum"], "OK")
        self.assertFalse(os.path.exists(os.path.join(self.pq, "prompt.parquet")))

    def test_tablo_hatasi_tmp_silinir_kalanlar_surer_cikis_3_stderr(self):
        # şema kayması: 'dosya' tablosu var ama sort key kolonu (dosya_id) yok → DuckDB COPY o tabloda HATA verir; --sessiz olsa da
        # neden stderr'e düşer, .tmp kalmaz, çıkış 3. Devam kanıtı: ihraç sırası TABLOLAR sırasıdır (dosya=2 < karar_borcu=5) →
        # HATA'dan SONRA gelen karar_borcu yine ihraç edilir (döngü kırılsaydı dosya oluşmazdı)
        con = sqlite3.connect(self.db)
        con.execute("CREATE TABLE dosya (id TEXT)"); con.execute("INSERT INTO dosya VALUES ('x')")
        con.commit(); con.close()
        m = modul("ambar-parquet.py"); sira = [t for t, _ in m.TABLOLAR]
        self.assertLess(sira.index("dosya"), sira.index("karar_borcu"))
        r = kos("ambar-parquet.py", "--db", self.db, "--cikti", self.pq, "--tablo", "dosya,karar_borcu", "--sessiz")
        self.assertEqual(r.returncode, 3, r.stdout + r.stderr)
        self.assertEqual(r.stdout, "")
        hata = [json.loads(l) for l in r.stderr.splitlines() if l.startswith("{")]
        self.assertEqual([(h["tablo"], h["durum"]) for h in hata], [("dosya", "HATA")])  # OK satırı stderr'e düşmez
        self.assertIn("dosya_id", hata[0]["neden"])
        self.assertIn("ambar-parquet: 1 OK", r.stderr)
        self.assertFalse(os.path.exists(os.path.join(self.pq, "dosya.parquet.tmp")))
        self.assertFalse(os.path.exists(os.path.join(self.pq, "dosya.parquet")))
        self.assertTrue(os.path.exists(os.path.join(self.pq, "karar_borcu.parquet")))

    def test_sorgu_aninda_dusen_gorunum_hata_satiri_kalanlar_surer(self):
        # sqlite_master'da var ama sorgu anında düşen görünüm (yarım kurulmuş silver: dayandığı tablo yok) → sayım (count) aşamasında
        # sqlite hatası; traceback DEĞİL, HATA satırı + çıkış 3; sonraki görünüm (v_hareket_gunluk, TABLOLAR'da daha sonra) yine ihraç edilir
        con = sqlite3.connect(self.db)
        con.execute("CREATE VIEW v_referans_sayim AS SELECT ref_turu FROM olmayan_tablo")
        con.execute("CREATE VIEW v_hareket_gunluk AS SELECT count(*) AS n FROM kayit")
        con.commit(); con.close()
        m = modul("ambar-parquet.py"); sira = [t for t, _ in m.TABLOLAR]
        self.assertLess(sira.index("v_referans_sayim"), sira.index("v_hareket_gunluk"))
        r = kos("ambar-parquet.py", "--db", self.db, "--cikti", self.pq, "--tablo", "v_referans_sayim,v_hareket_gunluk", "--sessiz")
        self.assertEqual(r.returncode, 3, r.stdout + r.stderr)
        self.assertNotIn("Traceback", r.stderr)
        hata = [json.loads(l) for l in r.stderr.splitlines() if l.startswith("{")]
        self.assertEqual([(h["tablo"], h["durum"]) for h in hata], [("v_referans_sayim", "HATA")])
        self.assertIn("olmayan_tablo", hata[0]["neden"])
        self.assertFalse(os.path.exists(os.path.join(self.pq, "v_referans_sayim.parquet")))
        self.assertFalse(os.path.exists(os.path.join(self.pq, "v_referans_sayim.parquet.tmp")))
        self.assertTrue(os.path.exists(os.path.join(self.pq, "v_hareket_gunluk.parquet")))
        # --kuru da aynı sözleşme: bozuk görünüm HATA satırı, çıkış 3, dosya yazılmaz
        r2 = kos("ambar-parquet.py", "--db", self.db, "--cikti", os.path.join(self.tmp, "pq2"), "--tablo", "v_referans_sayim", "--kuru")
        self.assertEqual(r2.returncode, 3, r2.stdout + r2.stderr)
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "pq2", "v_referans_sayim.parquet")))

    def test_kolon_olcum_parquet_ile(self):
        # her iki araç --repo geçici dizinle: profil çalışma dizini vb. repo altına açılmaz — koşum sonrası dizine yalnız kütük eklenir
        kos("ambar-parquet.py", "--repo", self.tmp, "--db", self.db, "--cikti", self.pq, "--tablo", "kayit,referans", "--sessiz")
        kutuk = os.path.join(self.tmp, "k.jsonl")
        once = sorted(os.listdir(self.tmp))
        r = kos("kolon-olcum.py", "--repo", self.tmp, "--db", self.db, "--parquet", self.pq, "--cikti", kutuk, "--sessiz", "--sorgu", "Q1,Q5")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(sorted(os.listdir(self.tmp)), sorted(once + ["k.jsonl"]))
        satirlar = oku_jsonl(kutuk)
        self.assertEqual(len(satirlar), 2 * 3)
        for s in satirlar:
            self.assertEqual(s["durum"], "OK", s)
        # aynı sorgu iki motorda aynı satır sayısı (eşdeğerlik)
        for q in ("Q1", "Q5"):
            n = {s["motor"]: s["satir"] for s in satirlar if s["sorgu"] == q}
            self.assertEqual(len(set(n.values())), 1, n)
        # parquet tazelik damgası: aynı HEAD'de üretildi → parquet_git_head = git_head, bayat değil, üretim zamanı dolu
        for s in (s for s in satirlar if s["motor"].startswith("duckdb")):
            self.assertEqual(s["parquet_git_head"], s["git_head"], s)
            self.assertIs(s["parquet_bayat"], False)
            self.assertTrue(s["parquet_uretim_ts"])

    def test_parquet_kolon_byte_kolon_listesinden_ve_kutuk_alanlari(self):
        # kolon tarafı `byte` = sorgunun dokunduğu kolonların parquet kolon-chunk byte toplamı (statik). Küçük DB'de metin deterministik
        # olarak genişletilir (satır başına 2 KB sözde-rastgele hex — sha256 zinciri, tekrar-üretilir), sonra: Q1 (2 dar kolon) > 0;
        # Q6 (geniş metin) ≥ Q1; tüm kolonlar ≤ dosya boyutu ve Q1 < tüm kolonlar (kolon atlama diskte görünür); Q5 kaynak başına toplanır;
        # dosyada olmayan kolon FAIL-LOUD. Uçtan uca CLI: parquet satırı byte/byte_tanimi bu hesapla aynı, TOTAL_BYTES_READ ayrı alanda
        # notuyla; native satırı byte None + 'bellek-içi' tanımı; sqlite satırı dbstat tanımı.
        import duckdb
        m = modul("kolon-olcum.py")
        con = sqlite3.connect(self.db)
        for (kid,) in con.execute("SELECT kayit_id FROM kayit").fetchall():
            ek = "".join(hashlib.sha256(("%s:%d" % (kid, i)).encode()).hexdigest() for i in range(32))  # 2048 hex karakter
            con.execute("UPDATE kayit SET metin = metin || ? WHERE kayit_id = ?", (ek, kid))
        con.commit(); con.close()
        r = kos("ambar-parquet.py", "--repo", self.tmp, "--db", self.db, "--cikti", self.pq, "--tablo", "kayit,referans", "--sessiz")
        self.assertEqual(r.returncode, 0, r.stderr)
        kp, rp = os.path.join(self.pq, "kayit.parquet"), os.path.join(self.pq, "referans.parquet")
        yollar = {"k": kp, "r": rp}
        b = {q: m.parquet_kolon_byte(duckdb, yollar, m.SORGULAR[q][2]) for q in m.SORGULAR}
        self.assertGreater(b["Q1"], 0)
        self.assertGreaterEqual(b["Q6"], b["Q1"], b)
        tum_kolonlar = [c[1] for c in sqlite3.connect(self.db).execute("PRAGMA table_info(kayit)").fetchall()]
        hepsi = m.parquet_kolon_byte(duckdb, yollar, {"k": tum_kolonlar})
        self.assertLess(b["Q1"], hepsi); self.assertLessEqual(hepsi, os.path.getsize(kp))
        self.assertEqual(b["Q5"], m.parquet_kolon_byte(duckdb, yollar, {"k": m.SORGULAR["Q5"][2]["k"]})
                         + m.parquet_kolon_byte(duckdb, yollar, {"r": m.SORGULAR["Q5"][2]["r"]}))
        with self.assertRaises(ValueError):
            m.parquet_kolon_byte(duckdb, yollar, {"k": ["dosya_id", "olmayan_kolon"]})
        kutuk = os.path.join(self.tmp, "k.jsonl")
        r = kos("kolon-olcum.py", "--repo", self.tmp, "--db", self.db, "--parquet", self.pq, "--cikti", kutuk, "--sessiz", "--sorgu", "Q1,Q6")
        self.assertEqual(r.returncode, 0, r.stderr)
        satirlar = oku_jsonl(kutuk)
        self.assertEqual(len(satirlar), 2 * 3)
        for s in satirlar:
            self.assertEqual(s["durum"], "OK", s)
            if s["motor"] == "duckdb-parquet":
                self.assertEqual(s["byte"], b[s["sorgu"]], s)
                self.assertEqual(s["byte_tanimi"], m.PARQUET_BYTE_TANIMI)
                self.assertIn("duck_total_bytes_read", s); self.assertTrue(s["duck_total_bytes_read_notu"])
            elif s["motor"] == "duckdb-native":
                self.assertIsNone(s["byte"]); self.assertEqual(s["byte_tanimi"], m.NATIVE_BYTE_TANIMI)
                self.assertIn("duck_total_bytes_read", s)
            else:
                self.assertTrue(s["byte_tanimi"].startswith("dbstat"), s)
                self.assertNotIn("duck_total_bytes_read", s)

    def test_parquet_damga_metadata_yoksa_none_bayat_ise_true(self):
        import duckdb
        m = modul("kolon-olcum.py")
        duz = os.path.join(self.tmp, "duz.parquet")
        duckdb.connect().execute("COPY (SELECT 1 AS a) TO '%s' (FORMAT PARQUET)" % duz)
        d = m.parquet_damga(duckdb, {"kayit": duz, "referans": duz}, "abc1234")
        self.assertEqual(d, {"parquet_git_head": None, "parquet_uretim_ts": None, "parquet_bayat": None})
        kos("ambar-parquet.py", "--db", self.db, "--cikti", self.pq, "--tablo", "kayit", "--sessiz")
        d2 = m.parquet_damga(duckdb, {"kayit": os.path.join(self.pq, "kayit.parquet")}, "olmayan-head")
        self.assertIs(d2["parquet_bayat"], True); self.assertTrue(d2["parquet_git_head"])


class KatmanHattiSecimTest(unittest.TestCase):
    def test_parquet_adimi_varsayilan_kapali_bayrakla_acik(self):
        m = modul("katman-hatti.py")
        temel = [a for a, _ in m.adimlari_sec()]
        self.assertNotIn("parquet", temel); self.assertNotIn("kolon-olcum", temel)
        acik = [a for a, _ in m.adimlari_sec(parquet=True)]
        # 08-29 (İB-31): kolon katmanı olcum'un ÖNÜNDE koşar — olcum SON ADIM kalır (kanon §8 S3), parquet_uretim satırları olcum testine görünür
        self.assertEqual(acik[-4:], ["parquet", "kolon-olcum", "tarama-duckdb", "olcum"])  # tarama-duckdb: İB-38 (08-29)
        self.assertEqual([a for a, _ in m.adimlari_sec(parquet=True, atla=("kolon-olcum", "tarama-duckdb", "baglam", "olcum"))][-1], "parquet")
        self.assertEqual([a for a, _ in m.adimlari_sec(parquet=True, atla=("olcum",))][-3:], ["parquet", "kolon-olcum", "tarama-duckdb"])
        self.assertEqual(m.adim_durumu("tarama-duckdb", 4), ("ATLANDI", False))

    def test_yorumlayici_parquet_adimlari_venv(self):
        # Karar 63 (venv) / İB-30: parquet adımları repo-içi .venv/bin/python varsa onunla, yoksa sys.executable ile; diğer adımlar hep sys.executable
        m = modul("katman-hatti.py")
        bos = tempfile.mkdtemp(prefix="hat-venv-")
        try:
            self.assertEqual(m.yorumlayici_sec(bos, "parquet"), sys.executable)
            os.makedirs(os.path.join(bos, ".venv", "bin")); open(os.path.join(bos, ".venv", "bin", "python"), "w").close()
            self.assertEqual(m.yorumlayici_sec(bos, "parquet"), os.path.join(bos, ".venv", "bin", "python"))
            self.assertEqual(m.yorumlayici_sec(bos, "kolon-olcum"), os.path.join(bos, ".venv", "bin", "python"))
            self.assertEqual(m.yorumlayici_sec(bos, "baglam"), sys.executable)
        finally:
            shutil.rmtree(bos, ignore_errors=True)

    def test_adim_durumu_parquet_4_atlandi_hat_dusmez(self):
        m = modul("katman-hatti.py")
        self.assertEqual(m.adim_durumu("parquet", 4), ("ATLANDI", False))  # duckdb/eklenti yok → atlandı, hat düşmez
        self.assertEqual(m.adim_durumu("parquet", 1), ("KOD 1", True))
        self.assertEqual(m.adim_durumu("parquet", 3), ("KOD 3", True))    # eşdeğerlik FAIL hattı düşürür
        self.assertEqual(m.adim_durumu("parquet", 0), ("OK", False))
        self.assertEqual(m.adim_durumu("kolon-olcum", 4), ("KOD 4", True))  # atlanma yalnız parquet adımının 4'ü için
        self.assertEqual(m.adim_durumu("baglam", 2), ("KOD 2", True))

    def test_atla_yankisi_ve_yardim_metni(self):
        # --help tüm adım adlarını listeler; --atla verilen adlar döngü öncesi '[atla ] <ad>' ile yankılanır ve koşulmaz
        h = kos("katman-hatti.py", "--help")
        # argparse yardım metnini terminal genişliğine sarar; "kolon-olcum" tire sonrasında satır kırılabilir → boşluk/satır sonu düzleştirilir
        duz = h.stdout.replace("-\n", "-").replace(" ", "").replace("\n", "")
        for ad in ("baglam", "hareket", "olcum", "parquet", "kolon-olcum"):
            self.assertIn(ad, duz)
        bos = tempfile.mkdtemp(prefix="hat-bos-")
        try:
            # Boş repoda hiçbir adım koşmamalı: liste hattın kendi ADIMLAR'ından türetilir (08-29: sabit liste bayatlamıştı — deneyim/bag gibi
            # sonradan eklenen FAIL-LOUD adımlar boş repoda çıkış 2 veriyordu; test yankı + yardım metnini sınar, adım kümesini değil)
            m = modul("katman-hatti.py")
            tum = [a for a, _ in m.adimlari_sec(parquet=True)]  # CLI varsayılanı parquet AÇIK (Karar 83 B2) → kolon adımları da atlanmalı
            r = kos("katman-hatti.py", "--repo", bos, "--atla", "baglam, " + ",".join(tum[1:]))
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertEqual([l for l in r.stdout.splitlines() if l.startswith("[")], ["[atla ] %s" % ad for ad in tum])
            # FAIL-LOUD: yazım hatalı --atla adı 'atlandı' diye yankılanmaz; stderr'de listelenir, çıkış 2, hiçbir adım koşmaz
            r2 = kos("katman-hatti.py", "--repo", bos, "--atla", "olcum,parquett")
            self.assertEqual(r2.returncode, 2, r2.stdout + r2.stderr)
            self.assertIn("parquett", r2.stderr)
            self.assertEqual(r2.stdout, "")
        finally:
            shutil.rmtree(bos, ignore_errors=True)

    def test_atla_sec_bilinen_bilinmeyen_ayrimi(self):
        m = modul("katman-hatti.py")
        self.assertEqual(m.atla_sec(" olcum , parquet,kolon-olcum,parquett,"), (["olcum", "parquet", "kolon-olcum"], ["parquett"]))
        self.assertEqual(m.atla_sec(""), ([], []))
        self.assertEqual(m.atla_sec("baglam,karar,prompt,ambar,hareket,tarama,olcum")[1], [])


if __name__ == "__main__":
    unittest.main()
