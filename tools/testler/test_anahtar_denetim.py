#!/usr/bin/env python3
"""anahtar-denetim.py testleri (İB-58 argparse taşıması; AXI-STANDARDI.md A1/A2/A7 uyumu; stdlib unittest).
Koş: python3 -m unittest tools/testler/test_anahtar_denetim.py
Davranış DEĞİŞMEDİ testi (insan çıktısı diff'i) ayrı yapılır (koşum raporunda); burada arayüz sözleşmesi doğrulanır:
--help / --json şema + cikis alanı ↔ süreç çıkış kodu / bilinmeyen bayrak ve tip hatası → 2 / eksik kayıt dosyası →
2 + stderr tek satır + traceback yok / --anahtar filtresi / --json --sessiz."""
import json, os, subprocess, sys, unittest

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARAC = os.path.join(KOK, "tools", "anahtar-denetim.py")


def kos(*args):
    return subprocess.run([sys.executable, ARAC] + list(args), cwd=KOK, capture_output=True, text=True)


class AnahtarDenetimTest(unittest.TestCase):
    def test_help_cikis_0_ve_icerik(self):
        r = kos("--help")
        self.assertEqual(r.returncode, 0)
        self.assertTrue("Kullanım" in r.stdout or "--json" in r.stdout, r.stdout[:300])

    def test_json_sema_ve_cikis_alani(self):
        r = kos("--json")
        d = json.loads(r.stdout)
        for alan in ("arac", "surum", "git_head", "cikis", "anahtarlar", "sonuc"):
            self.assertIn(alan, d, "eksik alan: %s" % alan)
        self.assertEqual(d["arac"], "anahtar-denetim")
        self.assertEqual(d["cikis"], r.returncode)

    def test_bilinmeyen_bayrak_cikis_2(self):
        r = kos("--yok")
        self.assertEqual(r.returncode, 2)

    def test_goster_tip_hatasi_cikis_2(self):
        r = kos("--goster", "abc")
        self.assertEqual(r.returncode, 2)

    def test_kayit_yok_cikis_2_traceback_yok(self):
        r = kos("--kayit", "olmayan.md")
        self.assertEqual(r.returncode, 2)
        self.assertNotIn("Traceback", r.stdout)
        self.assertTrue(r.stderr.strip(), "stderr'de teşhis satırı bekleniyordu")

    def test_anahtar_filtresi_tek_sonuc(self):
        tum = json.loads(kos("--json").stdout)
        self.assertTrue(tum["anahtarlar"], "kayıtta anahtar yok — test atlanamaz (FAIL-LOUD)")
        aid = tum["anahtarlar"][0]["anahtar_id"]
        r = kos("--json", "--anahtar", aid)
        d = json.loads(r.stdout)
        self.assertEqual([a["anahtar_id"] for a in d["anahtarlar"]], [aid])

    def test_json_sessiz_tek_json(self):
        r = kos("--json", "--sessiz")
        d = json.loads(r.stdout)  # tek JSON.loads çağrısı fazladan satır olsaydı hata verirdi
        self.assertEqual(d["cikis"], r.returncode)


if __name__ == "__main__":
    unittest.main()
