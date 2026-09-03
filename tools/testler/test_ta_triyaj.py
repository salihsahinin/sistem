#!/usr/bin/env python3
"""test_ta_triyaj.py — tools/ta-triyaj.py birim testleri (Karar 83 B3 (a) icrası). STDLIB ONLY."""
import importlib.util, json, os, sqlite3, subprocess, sys, tempfile, unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT = os.path.join(REPO, "tools", "ta-triyaj.py")

spec = importlib.util.spec_from_file_location("ta_triyaj", SCRIPT)
ta_triyaj = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ta_triyaj)


def _gecici_db(rows, kosum_id="k1"):
    fd, yol = tempfile.mkstemp(suffix=".sqlite")
    os.close(fd)
    con = sqlite3.connect(yol)
    con.execute("""CREATE TABLE silver_karantina_aday (
        cift_id TEXT PRIMARY KEY, anahtar_terim TEXT, kayit_id_a TEXT, kayit_id_b TEXT, dosya_a TEXT, dosya_b TEXT,
        blok_turu TEXT, uzunluk_a INTEGER, uzunluk_b INTEGER, kosum_id TEXT)""")
    for i, (at, da, db_, la, lb) in enumerate(rows):
        con.execute("INSERT INTO silver_karantina_aday VALUES (?,?,?,?,?,?,?,?,?,?)",
                     ("cift-%d" % i, at, "ka%d" % i, "kb%d" % i, da, db_, "madde", la, lb, kosum_id))
    con.commit(); con.close()
    return yol


class TestSiniflandirmaVeSiddet(unittest.TestCase):
    def setUp(self):
        # 3 çift: 2'si "ort" anahtar-terimini paylaşır (tekrar_sayisi=2), biri "tek" (tekrar_sayisi=1)
        self.rows = [
            ("ort", ".claude/skills/a/SKILL.md", ".claude/skills/b/SKILL.md", 100, 100),   # ayni-ust-klasor, uzunluk_toplam=200
            ("ort", "core/x.md", ".claude/skills/c/SKILL.md", 10, 10),                      # capraz-ust-klasor, uzunluk_toplam=20
            ("tek", "core/y.md", "core/z.md", 5000, 5000),                                  # ayni-ust-klasor, uzunluk_toplam=10000, tekrar=1
        ]
        self.db = _gecici_db(self.rows)

    def tearDown(self):
        os.remove(self.db)

    def test_ust_klasor_siniflandirma(self):
        _, rows = ta_triyaj.cift_oku(self.db)
        ciftler, toplam = ta_triyaj.triyaj(rows, 20)
        self.assertEqual(toplam, 3)
        by_terim_dosya = {(c["anahtar_terim"], c["dosya_a"]): c["sinif"] for c in ciftler}
        self.assertEqual(by_terim_dosya[("ort", ".claude/skills/a/SKILL.md")], "ayni-ust-klasor")
        self.assertEqual(by_terim_dosya[("ort", "core/x.md")], "capraz-ust-klasor")
        self.assertEqual(by_terim_dosya[("tek", "core/y.md")], "ayni-ust-klasor")

    def test_siddet_formulu_ve_siralama(self):
        _, rows = ta_triyaj.cift_oku(self.db)
        ciftler, _ = ta_triyaj.triyaj(rows, 20)
        # "tek": uzunluk_toplam=10000 × tekrar_sayisi=1 = 10000 (en yüksek şiddet, sıra 1)
        # "ort"/.claude...: uzunluk_toplam=200 × tekrar_sayisi=2 = 400 (sıra 2)
        # "ort"/core...: uzunluk_toplam=20 × tekrar_sayisi=2 = 40 (sıra 3, en düşük)
        self.assertEqual(ciftler[0]["anahtar_terim"], "tek")
        self.assertEqual(ciftler[0]["siddet"], 10000)
        self.assertEqual(ciftler[1]["siddet"], 400)
        self.assertEqual(ciftler[1]["tekrar_sayisi"], 2)
        self.assertEqual(ciftler[2]["siddet"], 40)
        # şiddet azalan sırada olmalı
        siddetler = [c["siddet"] for c in ciftler]
        self.assertEqual(siddetler, sorted(siddetler, reverse=True))

    def test_ilk_n_kirpma(self):
        _, rows = ta_triyaj.cift_oku(self.db)
        ciftler, toplam = ta_triyaj.triyaj(rows, 2)
        self.assertEqual(toplam, 3)
        self.assertEqual(len(ciftler), 2)


class TestJsonCiktisi(unittest.TestCase):
    def setUp(self):
        self.rows = [("ort", "a/X.md", "b/Y.md", 50, 50), ("tek", "core/y.md", "core/z.md", 300, 100)]
        self.db = _gecici_db(self.rows, kosum_id="k2")
        fd, self.saglik = tempfile.mkstemp(suffix=".jsonl")
        os.close(fd)
        with open(self.saglik, "w", encoding="utf-8") as fh:
            fh.write(json.dumps({"ts": "2026-09-03T10:00:00+03:00", "kosum_id": "k2", "head": "abc123",
                                  "snapshot": "2026-09-03", "test_id": "T-A-ONELEME", "ihlal": 2, "ornek": []}) + "\n")

    def tearDown(self):
        os.remove(self.db); os.remove(self.saglik)

    def test_json_cikti_parse_edilebilir_ve_alanlari_dogru(self):
        p = subprocess.run([sys.executable, SCRIPT, "--db", self.db, "--saglik", self.saglik, "--json", "--n", "5"],
                            capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        d = json.loads(p.stdout)
        self.assertTrue(d["ok"])
        self.assertEqual(d["kosum_id"], "k2")
        self.assertEqual(d["snapshot"], "2026-09-03")
        self.assertEqual(d["toplam_cift"], 2)
        self.assertEqual(d["ilk_n"], 2)
        self.assertEqual(len(d["ilk_20"]), 2)
        for c in d["ilk_20"]:
            for alan in ("sira", "sinif", "siddet", "anahtar_terim", "dosya_a", "dosya_b", "tekrar_sayisi"):
                self.assertIn(alan, c)

    def test_bos_tablo_hata_kodu_2(self):
        bos_db = _gecici_db([])
        try:
            p = subprocess.run([sys.executable, SCRIPT, "--db", bos_db, "--saglik", self.saglik, "--json"],
                                capture_output=True, text=True)
            self.assertEqual(p.returncode, 2)
        finally:
            os.remove(bos_db)


if __name__ == "__main__":
    unittest.main()
