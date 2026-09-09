#!/usr/bin/env python3
"""test_devir_ani.py — İB-75 devir-ani.py: eşik-altı False, eşik-üstü (E2) True, determinizm. TAM 3 test (Karar 90: fazla test yok).
Koşum: python3 -m unittest tools/testler/test_devir_ani.py"""
import csv, importlib.util, json, os, shutil, sys, tempfile, unittest

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARAC = os.path.join(KOK, "tools", "devir-ani.py")


def modul():
    spec = importlib.util.spec_from_file_location("devir_ani", ARAC); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


KOLONLAR = ["oturum_kisa", "tarih", "ilk_saat", "son_saat", "tur", "ilk_tur_baglam", "max_baglam", "son_baglam",
            "tur_128k_ustu", "toplam_cikti", "toplam_thinking", "yan_zincir_tur", "model"]


class DevirAniTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="devir-ani-")
        os.makedirs(os.path.join(self.tmp, "veri", "gorunum"))
        os.makedirs(os.path.join(self.tmp, "veri", "bronz"))
        self.girdi = os.path.join(self.tmp, "veri", "gorunum", "v_baglam_seyri.csv")
        self.cikti = os.path.join(self.tmp, "veri", "bronz", "devir-ani-olay.jsonl")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def yaz(self, satirlar):
        with open(self.girdi, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=KOLONLAR)
            w.writeheader()
            for s in satirlar:
                row = {k: "" for k in KOLONLAR}
                row.update(s)
                w.writerow(row)

    def oku_kayitlar(self):
        with open(self.cikti, encoding="utf-8") as f:
            return [json.loads(l) for l in f if l.strip()]

    def test_esik_alti_false(self):
        m = modul()
        self.yaz([{"oturum_kisa": "s1", "tarih": "2026-09-09", "model": "sonnet-5", "max_baglam": "50000", "tur_128k_ustu": "0"}])
        m.calistir(self.tmp)
        kayitlar = self.oku_kayitlar()
        self.assertEqual(len(kayitlar), 1)
        self.assertEqual(kayitlar[0]["yuklem_sonucu"], False)
        self.assertEqual(kayitlar[0]["tetikleyen_kosul"], "esik-alti")
        self.assertIsNone(kayitlar[0]["gorev_siniri"])
        self.assertFalse(kayitlar[0]["atesleme"])

    def test_esik_ustu_true(self):
        m = modul()
        self.yaz([{"oturum_kisa": "s2", "tarih": "2026-09-09", "model": "opus-5", "max_baglam": "650000", "tur_128k_ustu": "40"}])
        m.calistir(self.tmp)
        kayitlar = self.oku_kayitlar()
        self.assertEqual(len(kayitlar), 1)
        self.assertEqual(kayitlar[0]["yuklem_sonucu"], True)
        self.assertEqual(kayitlar[0]["tetikleyen_kosul"], "E2-son-care")
        self.assertFalse(kayitlar[0]["atesleme"])

    def test_determinizm(self):
        m = modul()
        self.yaz([
            {"oturum_kisa": "s1", "tarih": "2026-09-09", "model": "sonnet-5", "max_baglam": "50000", "tur_128k_ustu": "0"},
            {"oturum_kisa": "s2", "tarih": "2026-09-09", "model": "opus-5", "max_baglam": "300000", "tur_128k_ustu": "10"},
            {"oturum_kisa": "s3", "tarih": "2026-09-09", "model": "opus-5", "max_baglam": "650000", "tur_128k_ustu": "40"},
        ])

        def ts_haric(kayit):
            d = dict(kayit); d.pop("ts", None); return d

        m.calistir(self.tmp)
        birinci = [ts_haric(k) for k in self.oku_kayitlar()]

        # ikinci koşum: yeni oturumlar yok, mükerrer satır eklenmemeli (idempotens); içerik birebir aynı kalır
        m.calistir(self.tmp)
        ikinci = [ts_haric(k) for k in self.oku_kayitlar()]

        self.assertEqual(birinci, ikinci)
        self.assertEqual(len(ikinci), 3)


if __name__ == "__main__":
    unittest.main()
