#!/usr/bin/env python3
"""anakronizm-denetim.py testleri (Karar 88 M4, Salih hükmü 2026-09-09: tarihli-dosya D1/D2 muafiyeti; stdlib unittest).
Koş: python3 -m unittest tools/testler/test_anakronizm_denetim.py
Kapsam: tarihli_muaf() yüklemi — raporlar/ ∨ cc/ ön-eki ∧ dosya adında YYYY-MM-DD ⇒ muaf; core/ ve wiki/ muaf DEĞİL."""
import os, sys, unittest

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(KOK, "tools"))

import importlib.util
_spec = importlib.util.spec_from_file_location("anakronizm_denetim", os.path.join(KOK, "tools", "anakronizm-denetim.py"))
ad = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ad)


class TarihliMuafTest(unittest.TestCase):
    def test_raporlar_tarihli_muaf(self):
        self.assertTrue(ad.tarihli_muaf("raporlar/2026-09-03-x.md"))

    def test_cc_tarihli_muaf(self):
        self.assertTrue(ad.tarihli_muaf("cc/rapor-2026-09-03.md"))

    def test_core_tarihli_muaf_degil(self):
        self.assertFalse(ad.tarihli_muaf("core/2026-09-03-x.md"))

    def test_wiki_tarihli_muaf_degil(self):
        self.assertFalse(ad.tarihli_muaf("wiki/2026-09-03-x.md"))

    def test_raporlar_tarihsiz_muaf_degil(self):
        self.assertFalse(ad.tarihli_muaf("raporlar/tarihsiz.md"))


if __name__ == "__main__":
    unittest.main()
