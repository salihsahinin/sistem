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
        """Eski↔yeni fark yalnız İKİ YAPISAL SINIFTA kalır (sabit yol listesi değil — 08-29 dersi: liste her yeni cc/ alt-klasöründe bayatladı):
        (A) eski SOĞUK → silver ILIK: yalnız kuyruk/gelen-* ve kök snapshot kapsülleri (CEP-/CHAT-KAPSULU-*, secim-turu-*, PARALEL-VARDIYA-ILK-DENEME) — açık liste, küçük, durağan.
        (B) eski ILIK → silver SOĞUK: eski tanımın VARSAYILAN dalı ılık, silver'ın varsayılanı soğuk (README/SKILL/tools/veri/sozlesme/cc/<alt-klasör>/Clippings…) — yapısal, listelenmez.
        Değişmez: SICAK küme iki tanımda BİREBİR; soğuk→ılık terfisi yalnız (A)'da."""
        sinif_a = ("kuyruk/gelen-", "CEP-KAPSULU-", "CHAT-KAPSULU-", "secim-turu-", "PARALEL-VARDIYA-ILK-DENEME")
        fark = [(y, self.ad._katman_yerel(y), self.bt.katman_bul(y)) for y in self.yollar if self.ad._katman_yerel(y) != self.bt.katman_bul(y)]
        sicak_fark = [f for f in fark if "sicak" in f[1:]]
        self.assertEqual(sicak_fark, [], "SICAK küme ayrıştı: %s" % sicak_fark[:5])
        beklenmeyen = [f for f in fark if not ((f[1], f[2]) == ("soguk", "ilik") and f[0].startswith(sinif_a)) and not (f[1], f[2]) == ("ilik", "soguk")]
        self.assertEqual(beklenmeyen, [], "eski↔yeni tanım farkı bilinmeyen sınıfta: %s" % beklenmeyen[:5])
        self.assertTrue(fark, "fark 0 — eski yerel tanım silinmiş/eşitlenmiş olabilir; docstring'i güncelle (FAIL-LOUD)")

if __name__ == "__main__":
    unittest.main()
