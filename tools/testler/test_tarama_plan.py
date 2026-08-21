#!/usr/bin/env python3
"""tarama-plan.py testleri (pipeline cc/pipeline-2026-08-18-tarama-yontemleri.md SH-1; stdlib unittest, Python 3.9).
Koş: python3 -m unittest discover -s tools/testler -p 'test_*.py' -v
Davranış testleri: küçük geçici silver DB (repo verisine dokunulmaz); çıkış kodları, plan sınıflandırması, kaynak DB'nin değişmezliği,
kütük grain'i, --sert davranışı, şema kaymasında HATA satırı, beklenti-dışı uyarısı, katman-hatti içinde koşum (geçici repo) ve hat adım sırası
(tarama olcum'dan ÖNCE; olcum SON adım — kanon §8 S3) doğrulanır."""
import hashlib, json, os, shutil, sqlite3, subprocess, sys, tempfile, unittest, importlib.util

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOLS = os.path.join(REPO, "tools")
ARAC = os.path.join(TOOLS, "tarama-plan.py")
HAT = os.path.join(TOOLS, "katman-hatti.py")


def modul(yol=ARAC, ad="tp"):
    sp = importlib.util.spec_from_file_location(ad, yol); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m


def kucuk_silver(yol, n=200):
    """kayit/referans/dosya/karar_borcu şemasının gerekli alt kümesi; skip-scan için ref_turu düşük kardinaliteli (2 değer × 100 satır)."""
    con = sqlite3.connect(yol)
    con.executescript("""
    CREATE TABLE kayit (kayit_id TEXT PRIMARY KEY, dosya_id TEXT, sira INTEGER, bolum_yolu TEXT, blok_turu TEXT, satir_bas INTEGER, satir_son INTEGER, metin TEXT, token_kestirim INTEGER);
    CREATE INDEX ix_kayit_dosya ON kayit(dosya_id, sira);
    CREATE TABLE referans (kayit_id TEXT, ref_turu TEXT, ref_deger TEXT);
    CREATE INDEX ix_ref_kayit ON referans(kayit_id);
    CREATE INDEX ix_ref_tur_deger ON referans(ref_turu, ref_deger);
    CREATE TABLE dosya (dosya_id TEXT PRIMARY KEY, baslik TEXT);
    CREATE TABLE karar_borcu (borc_id TEXT PRIMARY KEY, baslik TEXT);
    """)
    for i in range(n):
        d = "core/a%d.md" % (i % 5)
        con.execute("INSERT INTO kayit VALUES (?,?,?,?,?,?,?,?,?)", ("%s#%d-%d#x%d" % (d, i, i, i), d, i, "B › " + str(i % 3), "madde" if i % 2 else "paragraf", i, i, "m%d" % i, i % 7))
        con.execute("INSERT INTO referans VALUES (?,?,?)", ("%s#%d-%d#x%d" % (d, i, i, i), "kart" if i % 2 else "v_no", "K-%03d" % (i % 4)))
    for i in range(5):
        con.execute("INSERT INTO dosya VALUES (?,?)", ("core/a%d.md" % i, "B › %d" % i))
    con.execute("INSERT INTO karar_borcu VALUES ('KB-43','x')")
    con.commit(); con.close()


def kos(*args, env=None):
    return subprocess.run([sys.executable, ARAC] + list(args), cwd=REPO, capture_output=True, text=True, env=env)


def gecici_repo(tmp):
    """Geçici repo iskeleti: tools/ → gerçek tools dizinine symlink (araçlar kendi yolundan --repo türetir → kütük geçici repoya yazılır),
    veri/baglam.sqlite = küçük silver. Gerçek repo verisine dokunulmaz."""
    repo = os.path.join(tmp, "repo"); os.makedirs(os.path.join(repo, "veri"))
    os.symlink(TOOLS, os.path.join(repo, "tools"))
    kucuk_silver(os.path.join(repo, "veri", "baglam.sqlite"))
    return repo


def hat_kos(repo, *args):
    return subprocess.run([sys.executable, os.path.join(repo, "tools", "katman-hatti.py"), "--repo", repo,
                          "--atla", "baglam,karar,prompt,ambar,hareket,olcum"] + list(args), cwd=repo, capture_output=True, text=True)


def sha(yol):
    with open(yol, "rb") as fh:
        return hashlib.sha1(fh.read()).hexdigest()


def oku(yol):
    with open(yol, encoding="utf-8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


class NormalizeTest(unittest.TestCase):
    def test_siniflar(self):
        m = modul()
        n = m.normalize_plan
        self.assertEqual(n(["SEARCH kayit USING INDEX sqlite_autoindex_kayit_1 (kayit_id=?)"])[1], "SEARCH")
        self.assertEqual(n(["SCAN kayit"])[1], "SCAN")
        self.assertEqual(n(["SCAN kayit USING COVERING INDEX ix_kayit_dosya"])[1], "SCAN-COVERING")
        self.assertEqual(n(["SEARCH kayit USING INTEGER PRIMARY KEY (rowid>? AND rowid<?)"])[1], "SEARCH-ROWID")
        self.assertEqual(n(["SEARCH referans USING COVERING INDEX ix_ref_tur_deger (ANY(ref_turu) AND ref_deger=?)"])[1], "SKIP-SCAN")
        self.assertEqual(n(["SCAN d", "SEARCH k USING AUTOMATIC COVERING INDEX (bolum_yolu=?)"])[1], "AUTOMATIC-INDEX")
        norm, sinif, bayrak = n(["MULTI-INDEX OR", "INDEX 1", "SEARCH referans USING INDEX ix_ref_kayit (kayit_id=?)", "INDEX 2", "SEARCH referans USING INDEX ix_ref_tur_deger (ref_turu=? AND ref_deger=?)"])
        self.assertEqual(sinif, "MULTI-INDEX-OR"); self.assertNotIn("INDEX 1", norm)
        norm, sinif, bayrak = n(["SCAN kayit USING INDEX ix_kayit_dosya", "USE TEMP B-TREE FOR ORDER BY"])
        self.assertEqual(sinif, "SCAN"); self.assertIn("TEMP-BTREE", bayrak)
        # gevşek mod: parantez içi koşul metni normalize satırda yok
        self.assertNotIn("(", n(["SEARCH kayit USING INDEX ix_kayit_dosya (dosya_id=?)"])[0][0])


class KosumTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="tarama-test-"); self.db = os.path.join(self.tmp, "silver.sqlite"); kucuk_silver(self.db)
        self.kutuk = os.path.join(self.tmp, "tarama-plan.jsonl")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_db_yoksa_2_ve_bilinmeyen_ad_2(self):
        self.assertEqual(kos("--db", os.path.join(self.tmp, "yok.sqlite"), "--kuru").returncode, 2)
        r = kos("--db", self.db, "--kuru", "--sorgu", "N1, ZZ")
        self.assertEqual(r.returncode, 2); self.assertIn("ZZ", r.stderr)

    def test_kaynak_db_degismez_ve_iki_durum_kaydi(self):
        once = sha(self.db)
        tmpdir = os.path.join(self.tmp, "gecici"); os.mkdir(tmpdir)
        r = kos("--db", self.db, "--cikti", self.kutuk, "--sessiz", env=dict(os.environ, TMPDIR=tmpdir))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stderr.strip(), "")  # ihlal/beklenti-dışı/hata yok → stderr boş
        self.assertEqual(sha(self.db), once)  # ANALYZE geçici kopyada; kaynak byte-özdeş
        self.assertEqual(os.listdir(tmpdir), [])  # geçici ANALYZE kopyası silindi
        con = sqlite3.connect(self.db)
        self.assertEqual(con.execute("SELECT count(*) FROM sqlite_master WHERE name='sqlite_stat1'").fetchone()[0], 0); con.close()
        satirlar = oku(self.kutuk)
        m = modul()
        self.assertEqual(len(satirlar), 2 * len(m.SORGULAR))  # sorgu × {oldugu-gibi, analiz-kopya}
        durumlar = {s["durum"] for s in satirlar}; self.assertEqual(durumlar, {"oldugu-gibi", "analiz-kopya"})
        for s in satirlar:
            for alan in ("ts", "git_head", "sqlite", "sqlite_source_id", "sorgu", "durum", "stat1", "sonuc"):
                self.assertIn(alan, s)
        # noktasal sorgular her iki durumda SEARCH; ihlal yok
        for s in satirlar:
            if s["sonuc"] == "OK" and s["tur"] == "noktasal":
                self.assertFalse(s["ihlal"], s); self.assertIn(s["sinif"], ("SEARCH", "SEARCH-ROWID"))
        # skip-scan adayı: stat1 yokken SCAN-COVERING, analiz kopyasında SKIP-SCAN (düşük kardinaliteli ref_turu)
        s1 = {s["durum"]: s for s in satirlar if s["sorgu"] == "S1"}
        self.assertEqual(s1["oldugu-gibi"]["sinif"], "SCAN-COVERING")
        self.assertEqual(s1["analiz-kopya"]["sinif"], "SKIP-SCAN"); self.assertIn("skip-scan-aktif(stat1)", s1["analiz-kopya"]["sinyal"])
        # J1: otomatik indeks sinyali
        j1 = [s for s in satirlar if s["sorgu"] == "J1"][0]
        self.assertEqual(j1["sinif"], "AUTOMATIC-INDEX"); self.assertIn("kalici-indeks-adayi", j1["sinyal"])
        # A1: sayım covering; A3: indekssiz kolon SCAN
        self.assertEqual([s for s in satirlar if s["sorgu"] == "A3"][0]["sinif"], "SCAN")

    def test_analizsiz_tek_durum_ve_kuru_yazmaz(self):
        r = kos("--db", self.db, "--cikti", self.kutuk, "--sessiz", "--analizsiz", "--sorgu", "N1,A1")
        self.assertEqual(r.returncode, 0, r.stderr)
        satirlar = oku(self.kutuk); self.assertEqual({s["durum"] for s in satirlar}, {"oldugu-gibi"}); self.assertEqual(len(satirlar), 2)
        r = kos("--db", self.db, "--cikti", self.kutuk + ".2", "--kuru", "--sessiz")
        self.assertEqual(r.returncode, 0); self.assertFalse(os.path.exists(self.kutuk + ".2"))

    def test_ihlal_uyari_ve_sert(self):
        # indeksi düşürülmüş DB: N1 PK indeksi kalır ama ix_kayit_dosya yok → N2 noktasal SCAN'e düşer = ihlal
        con = sqlite3.connect(self.db); con.execute("DROP INDEX ix_kayit_dosya"); con.commit(); con.close()
        r = kos("--db", self.db, "--cikti", self.kutuk, "--sessiz", "--sorgu", "N2", "--analizsiz")
        self.assertEqual(r.returncode, 0); self.assertIn("UYARI", r.stderr)
        self.assertIn("BEKLENTİ DIŞI: N2(oldugu-gibi) SCAN ∉ {SEARCH}", r.stderr)
        self.assertTrue(oku(self.kutuk)[0]["ihlal"])
        r = kos("--db", self.db, "--kuru", "--sessiz", "--sorgu", "N2", "--analizsiz", "--sert")
        self.assertEqual(r.returncode, 3)

    def test_beklenti_disi_uyari_ihlal_degil_sert_dusurmez(self):
        # bileşik indeks yok → S1 analiz kopyasında SKIP-SCAN olamaz (SCAN): beklenti-dışı ama ihlal değil (tür skip) → stderr satırı, çıkış 0, --sert de 0
        con = sqlite3.connect(self.db); con.execute("DROP INDEX ix_ref_tur_deger"); con.commit(); con.close()
        r = kos("--db", self.db, "--cikti", self.kutuk, "--sessiz", "--sorgu", "S1")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("BEKLENTİ DIŞI: S1(analiz-kopya) SCAN ∉ {SKIP-SCAN}", r.stderr); self.assertNotIn("UYARI", r.stderr)
        s1 = {s["durum"]: s for s in oku(self.kutuk)}
        self.assertTrue(s1["oldugu-gibi"]["uyum"]); self.assertFalse(s1["analiz-kopya"]["uyum"]); self.assertFalse(s1["analiz-kopya"]["ihlal"])
        self.assertEqual(kos("--db", self.db, "--kuru", "--sessiz", "--sorgu", "S1", "--sert").returncode, 0)

    def test_eksik_tablo_atlanir(self):
        con = sqlite3.connect(self.db); con.execute("DROP TABLE karar_borcu"); con.commit(); con.close()
        r = kos("--db", self.db, "--cikti", self.kutuk, "--sessiz", "--sorgu", "N4", "--analizsiz")
        self.assertEqual(r.returncode, 0, r.stderr)
        s = oku(self.kutuk)[0]; self.assertEqual(s["sonuc"], "ATLANDI"); self.assertIn("karar_borcu", s["neden"])

    def test_sema_kaymasi_hata_satiri_kalanlar_surer_tumu_duserse_2(self):
        # kolon adı değişmiş (şema kayması): A2 EXPLAIN'de düşer → traceback yok, sonuc=HATA satırı + stderr HATA; N1 sürer, çıkış 0
        con = sqlite3.connect(self.db); con.execute("ALTER TABLE kayit RENAME COLUMN token_kestirim TO tk"); con.commit(); con.close()
        tmpdir = os.path.join(self.tmp, "gecici"); os.mkdir(tmpdir)
        r = kos("--db", self.db, "--cikti", self.kutuk, "--sorgu", "A2,N1", env=dict(os.environ, TMPDIR=tmpdir))
        self.assertEqual(r.returncode, 0, r.stderr); self.assertNotIn("Traceback", r.stderr)
        self.assertIn("HATA", r.stderr); self.assertIn("A2(oldugu-gibi)", r.stderr); self.assertIn("token_kestirim", r.stderr)
        self.assertEqual(os.listdir(tmpdir), [])  # hata yolunda da geçici kopya silindi
        satirlar = oku(self.kutuk); self.assertEqual(len(satirlar), 4)
        a2 = [s for s in satirlar if s["sorgu"] == "A2"]; n1 = [s for s in satirlar if s["sorgu"] == "N1"]
        self.assertEqual({s["sonuc"] for s in a2}, {"HATA"}); self.assertTrue(all("token_kestirim" in s["neden"] for s in a2))
        self.assertEqual({s["sonuc"] for s in n1}, {"OK"})
        self.assertIn("HATA", r.stdout)  # stdout tablosunda satır etiketi HATA (ATLANDI değil)
        # çalışan sorguların tümü düşerse çıkış 2 (kütük yine yazılır)
        r = kos("--db", self.db, "--cikti", self.kutuk + ".2", "--sessiz", "--sorgu", "A2", "--analizsiz")
        self.assertEqual(r.returncode, 2); self.assertIn("HATA", r.stderr); self.assertNotIn("Traceback", r.stderr)
        self.assertEqual([s["sonuc"] for s in oku(self.kutuk + ".2")], ["HATA"])

    def test_db_acilamazsa_2_ve_salt_okur(self):
        # DB olmayan dosya: traceback yok, stderr HATA, çıkış 2
        bozuk = os.path.join(self.tmp, "bozuk.sqlite")
        with open(bozuk, "wb") as fh:
            fh.write(b"bu bir sqlite dosyasi degil" * 100)
        r = kos("--db", bozuk, "--kuru", "--sessiz")
        self.assertEqual(r.returncode, 2, r.stderr); self.assertIn("HATA", r.stderr); self.assertNotIn("Traceback", r.stderr)
        # kaynak bağlantı salt-okur: yazma denemesi hata verir, dosya değişmez
        m = modul(); once = sha(self.db)
        con = m.salt_okur_ac(self.db)
        with self.assertRaises(sqlite3.OperationalError):
            con.execute("ANALYZE"); con.commit()
        con.close(); self.assertEqual(sha(self.db), once)


class KatmanHattiTest(unittest.TestCase):
    """tarama adımı katman-hatti içinde GERÇEKTEN koşar (geçici repo; tools/ symlink, veri/baglam.sqlite küçük silver)."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="tarama-hat-"); self.repo = gecici_repo(self.tmp)
        self.kutuk = os.path.join(self.repo, "veri", "tarama-plan.jsonl")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_tarama_adimi_hatta_kosar_ve_kutuk_gecici_repoda(self):
        r = hat_kos(self.repo)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        satir = [l for l in r.stdout.splitlines() if l.startswith("[OK") and " tarama " in l]
        self.assertEqual(len(satir), 1, r.stdout)
        self.assertNotIn("STDERR", r.stdout)  # ihlal yok → yankılanacak uyarı yok
        self.assertTrue(os.path.exists(self.kutuk), r.stdout)
        satirlar = oku(self.kutuk); self.assertEqual(len(satirlar), 2 * len(modul().SORGULAR))
        self.assertFalse(any(s.get("ihlal") for s in satirlar))

    def test_atla_tarama_adim_kosmaz_kutuk_yok(self):
        r = hat_kos(self.repo, "--atla", "baglam,karar,prompt,ambar,hareket,tarama,olcum")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("[atla ] tarama", r.stdout); self.assertFalse(os.path.exists(self.kutuk))

    def test_adim_sirasi_tarama_olcumdan_once_olcum_son(self):
        # kanon core/veri-muhendisligi-katmani.md §8 S3 (Salih A 08-17): "katman-hatti son adımı katman-olcum.py" — tarama salt-okur,
        # bu yüzden olcum'un ÖNÜNE konur; sıra hem ADIMLAR listesinde hem hat çıktısında ([atla ] satırları) doğrulanır
        adlar = [ad for ad, _ in modul(HAT, "kh").ADIMLAR]
        self.assertEqual(adlar, ["baglam", "karar", "prompt", "ambar", "hareket", "tarama", "olcum"])
        self.assertLess(adlar.index("tarama"), adlar.index("olcum")); self.assertEqual(adlar[-1], "olcum")
        r = hat_kos(self.repo, "--atla", ",".join(adlar))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        atla = [l.split()[-1] for l in r.stdout.splitlines() if l.startswith("[atla ]")]
        self.assertEqual(atla, adlar)

    def test_ihlal_uyarisi_hatta_gorunur_hat_dusmez(self):
        # uyarı modu: ihlal hattı düşürmez (çıkış 0, [OK ] tarama) ama tarama adımının stderr uyarısı hat çıktısında yankılanır
        db = os.path.join(self.repo, "veri", "baglam.sqlite")
        con = sqlite3.connect(db); con.execute("DROP INDEX ix_kayit_dosya"); con.commit(); con.close()
        r = hat_kos(self.repo)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertTrue(any(l.startswith("[OK") and " tarama " in l for l in r.stdout.splitlines()), r.stdout)
        self.assertIn("STDERR: ", r.stdout); self.assertIn("UYARI", r.stdout); self.assertIn("N2", r.stdout)
        self.assertIn("BEKLENTİ DIŞI: N2(oldugu-gibi) SCAN ∉ {SEARCH}", r.stdout)
        self.assertTrue(any(s.get("ihlal") for s in oku(self.kutuk)))


if __name__ == "__main__":
    unittest.main()
