#!/usr/bin/env python3
"""test_katman_tek_tanim.py — katman() TEK TANIM testi (İB-42 kalanı, 08-29): anahtar-denetim.katman(yol) ≡ baglam-tablo.katman_bul(yol) silver'daki
her .md dosyası için; ayrıca eski yerel tanımla farkların KAYITLI sınıflarda kaldığı (kuyruk/gelen-*, kök *-KAPSULU-*) doğrulanır.
Koşum: python3 -m unittest tools/testler/test_katman_tek_tanim.py"""
import importlib.util, os, sqlite3, unittest

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def modul(ad):
    yol = os.path.join(KOK, "tools", ad); spec = importlib.util.spec_from_file_location(ad.replace("-", "_").replace(".py", ""), yol)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


class KatmanTekTanimTest(unittest.TestCase):
    def setUp(self):
        self.bt = modul("baglam-tablo.py"); self.ad = modul("anahtar-denetim.py")
        db = os.path.join(KOK, "veri", "baglam.sqlite")
        self.yollar = [r[0] for r in sqlite3.connect(db).execute("SELECT dosya_id FROM dosya WHERE uzanti='md'")] if os.path.exists(db) else []

    def test_delegasyon_yuklendi(self):
        self.assertIsNotNone(self.ad._KATMAN_BUL, "anahtar-denetim baglam-tablo.katman_bul'u yükleyemedi")

    def test_silverdaki_her_md_icin_esit(self):
        self.assertTrue(self.yollar, "silver yok — test atlanamaz (FAIL-LOUD)")
        fark = [(y, self.ad.katman(y), self.bt.katman_bul(y)) for y in self.yollar if self.ad.katman(y) != self.bt.katman_bul(y)]
        self.assertEqual(fark, [], "tek-tanım kırıldı: %s" % fark[:5])

    def test_eski_tanimla_farklar_bilinen_siniflarda(self):
        bilinen = ("kuyruk/gelen-", "CEP-KAPSULU-", "CHAT-KAPSULU-", "secim-turu-", "PARALEL-VARDIYA-ILK-DENEME", "Clippings/")  # Clippings/: eski tanım ılık, silver soğuk (08-29 bulgusu)
        fark = [y for y in self.yollar if self.ad._katman_yerel(y) != self.bt.katman_bul(y)]
        beklenmeyen = [y for y in fark if not y.startswith(bilinen)]
        self.assertEqual(beklenmeyen, [], "eski↔yeni tanım farkı bilinmeyen sınıfta: %s" % beklenmeyen[:5])


if __name__ == "__main__":
    unittest.main()
