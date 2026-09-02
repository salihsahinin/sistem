#!/usr/bin/env python3
"""paralel-kapi.py testleri (Karar 86, Salih hükümleri D5(a)+D6(5), 2026-09-02; stdlib unittest).
Koş: python3 -m unittest discover -s tools/testler -p 'test_paralel_kapi*.py' -v
Kapsam: tur_turet() saf fonksiyonu (pipeline/loop/hibrit/matris/belirsiz ≥4 vaka) + kapı v0.2
tamam-birim düşürme (dalga planı + çakışma taramasından çıkarma) davranışı; gerçek repo manifestlerine
DOKUNMAZ, geçici manifest dizini kullanır."""
import importlib.util, json, os, shutil, tempfile, unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARAC = os.path.join(REPO, "tools", "paralel-kapi.py")


def modul():
    sp = importlib.util.spec_from_file_location("pk", ARAC)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


TEMEL = {
    "birim_id": "x", "tur": "pipeline", "pist": "K-1", "okur": [], "yazar": [],
    "granul": "dosya", "sira": [], "silver": "hayir", "kanon_yuzeyi": False, "dis_etki": [],
}


def birim(**ek):
    b = dict(TEMEL); b.update(ek); return b


class TurTuretTestleri(unittest.TestCase):
    def setUp(self):
        self.pk = modul()

    def test_pipeline(self):
        # Y1 SÜREKLİ=H (tetik_turu='seans') ∧ Y3 iç-sıra sabit=E (iterasyon_ayak_izi='sabit') → pipeline
        b = birim(tetik_turu="seans", iterasyon_ayak_izi="sabit")
        self.assertEqual(self.pk.tur_turet(b), "pipeline")

    def test_loop(self):
        # Y1=E (tetik_turu='surekli') ∧ Y2=H (dis_tavan yok) ∧ Y3=H (iterasyon_ayak_izi='buyuyen') → loop
        b = birim(tetik_turu="surekli", iterasyon_ayak_izi="buyuyen")
        self.assertEqual(self.pk.tur_turet(b), "loop")

    def test_hibrit(self):
        # Y1=E ∧ Y3=E (dış tetik sürekli ama iç-sıra sabit) → hibrit (Y2 fark etmez)
        b = birim(tetik_turu="surekli", iterasyon_ayak_izi="sabit")
        self.assertEqual(self.pk.tur_turet(b), "hibrit")

    def test_belirsiz(self):
        # ¬Y1 ∧ ¬Y3 (tek-turlu ama iç-sıra sabit değil) → hiçbir dala girmez → belirsiz
        b = birim(tetik_turu="seans", iterasyon_ayak_izi="buyuyen")
        self.assertEqual(self.pk.tur_turet(b), "belirsiz")

    def test_matris_eksen_alani(self):
        # 'eksen' ile başlayan üst alan varsa Y1/Y2/Y3'ten ÖNCE matris kazanır (İB-69 a1 şeması)
        b = birim(tetik_turu="seans", iterasyon_ayak_izi="sabit", eksenler=[{"ad": "e1"}])
        self.assertEqual(self.pk.tur_turet(b), "matris")

    def test_matris_matris_blogu(self):
        b = birim(tetik_turu="seans", iterasyon_ayak_izi="sabit", matris={"hucre_tipi": "tek_cagri"})
        self.assertEqual(self.pk.tur_turet(b), "matris")


class TamamBirimDusurmeTestleri(unittest.TestCase):
    """Kapı v0.2: durum='tamam*'|'kapandi*' birim dalga planından ve çakışma taramasından düşer."""

    def setUp(self):
        self.pk = modul()
        self.dizin = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.dizin, ignore_errors=True)

    def _yaz(self, ad, **ek):
        d = birim(birim_id=ad, **ek)
        with open(os.path.join(self.dizin, ad + ".json"), "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)

    def test_tamam_birim_dalgadan_ve_cakismadan_duser(self):
        # a: canlı, aynı dosyaya yazıyor; b: tamam, AYNI dosyaya yazıyor (b düşmeseydi RED/SIRALI üretirdi)
        self._yaz("a", durum="calisiyor", yazar=["ortak.md"])
        self._yaz("b", durum="tamam-2026-09-01", yazar=["ortak.md"])
        birimler, hatalar = self.pk.yukle(self.dizin)
        self.assertEqual(hatalar, [])
        canli = {bid: b for bid, b in birimler.items() if not self.pk.tamamlandi(b)}
        self.assertEqual(set(canli), {"a"})
        plan, bekleyen = self.pk.dalgalar(canli, [], 0)
        tum_planli = [bid for d in plan for bid in d["birimler"]]
        self.assertIn("a", tum_planli)
        self.assertNotIn("b", tum_planli)

    def test_kapandi_da_duser(self):
        self._yaz("c", durum="kapandi-2026-08-31")
        birimler, _ = self.pk.yukle(self.dizin)
        self.assertTrue(self.pk.tamamlandi(birimler["c"]))


if __name__ == "__main__":
    unittest.main()
