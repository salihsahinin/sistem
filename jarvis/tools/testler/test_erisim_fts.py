#!/usr/bin/env python3
"""erisim-fts.py --sorgu AXI testleri (İB-58/3; AXI-STANDARDI.md A1/A2/A4/A6/A7 uyumu; stdlib unittest).
Koş: python3 -m unittest tools/testler/test_erisim_fts.py
Davranış DEĞİŞMEDİ testi (--json'suz insan çıktısı diff'i eski↔yeni) ayrı yapılır (koşum raporunda); burada arayüz
sözleşmesi doğrulanır: --json şema + cikis alanı ↔ süreç çıkış kodu / --json'un --sorgu'suz kullanımı → 2 /
bilinmeyen bayrak → 2 / DB yok → 2 + stderr tek satır + traceback yok / bit-eşit determinizm (A4) / geri uyum.
Yan-etki: SALT-OKUR — testler --sorgu yolunu çağırır, silver'a yazmaz (--insa/--eval koşulmaz, PK-5)."""
import json, os, subprocess, sys, tempfile, unittest

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARAC = os.path.join(KOK, "tools", "erisim-fts.py")
SORGU = "çelişki kapısı"  # korpusta kesin geçen terim; isabet sayısı değil arayüz sözleşmesi test edilir


def kos(*args):
    return subprocess.run([sys.executable, ARAC] + list(args), cwd=KOK, capture_output=True, text=True)


class ErisimFtsAxiTest(unittest.TestCase):
    def test_help_cikis_0_ve_json_bayragi(self):
        r = kos("--help")
        self.assertEqual(r.returncode, 0)
        self.assertIn("--json", r.stdout)

    def test_json_sema_ve_cikis_alani(self):
        r = kos("--sorgu", SORGU, "--json")
        self.assertEqual(r.returncode, 0, r.stderr[:300])
        d = json.loads(r.stdout)  # tek json.loads — stdout'ta fazladan satır olsaydı hata verirdi (A1)
        for alan in ("arac", "surum", "git_head", "cikis", "sorgu", "k", "meta", "n_sonuc", "sonuclar"):
            self.assertIn(alan, d, "eksik alan: %s" % alan)
        self.assertEqual(d["arac"], "erisim-fts")
        self.assertEqual(d["cikis"], r.returncode)
        self.assertEqual(d["n_sonuc"], len(d["sonuclar"]))
        if d["sonuclar"]:
            for alan in ("kayit_id", "dosya_id", "katman", "zaman", "skor", "metin_kisa"):
                self.assertIn(alan, d["sonuclar"][0], "sonuç satırında eksik alan: %s" % alan)

    def test_json_sorgusuz_cikis_2(self):
        r = kos("--json")
        self.assertEqual(r.returncode, 2)
        self.assertTrue(r.stderr.strip(), "stderr'de teşhis satırı bekleniyordu")

    def test_bilinmeyen_bayrak_cikis_2(self):
        r = kos("--yok")
        self.assertEqual(r.returncode, 2)

    def test_db_yok_cikis_2_traceback_yok(self):
        with tempfile.TemporaryDirectory() as bos:
            r = kos("--repo", bos, "--sorgu", SORGU, "--json")
        self.assertEqual(r.returncode, 2)
        self.assertNotIn("Traceback", r.stderr)
        self.assertTrue(r.stderr.strip(), "stderr'de teşhis satırı bekleniyordu")
        self.assertEqual(r.stdout, "", "hata yolunda stdout boş kalmalı (A1)")

    def test_determinizm_bit_esit(self):  # A4: aynı silver + aynı sorgu → bit-eşit stdout (zaman alanı yok)
        r1 = kos("--sorgu", SORGU, "--json")
        r2 = kos("--sorgu", SORGU, "--json")
        self.assertEqual(r1.stdout, r2.stdout)

    def test_geri_uyum_insan_cikti_stdout(self):
        r = kos("--sorgu", SORGU)
        self.assertEqual(r.returncode, 0)
        self.assertTrue(r.stdout.startswith("sorgu:"), r.stdout[:120])


if __name__ == "__main__":
    unittest.main()
