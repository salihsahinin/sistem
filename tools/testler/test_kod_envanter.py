#!/usr/bin/env python3
"""kod-envanter.py testi (M14, Karar 88, 2026-09-09; AXI-STANDARDI.md A7; stdlib unittest).
Koş: python3 -m unittest tools/testler/test_kod_envanter.py
Kapsam: kuyruk/arsiv/karantina/ altına düşen git-izlenen bir dosya envanter sayımına girmiyor mu
(disla_uygula, tools/kod-orani-olcum.py::DISLA_DIZIN tek-kaynak sabitine göre süzüyor mu)."""
import importlib.util
import os
import sys
import unittest

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARAC = os.path.join(KOK, "tools", "kod-envanter.py")

_spec = importlib.util.spec_from_file_location("kod_envanter", ARAC)
kod_envanter = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(kod_envanter)


class KarantinaDislamaTest(unittest.TestCase):
    def test_karantina_dosyasi_envanterden_dislanir(self):
        disla_kume = kod_envanter.disla_dizinlerini_yukle(KOK)
        karantina_yolu = os.path.join("kuyruk", "arsiv", "karantina")
        self.assertIn(karantina_yolu, disla_kume)  # tek-kaynak: kod-orani-olcum.py::DISLA_DIZIN'den geldi

        dosyalar = [
            "tools/x.py",
            os.path.join(karantina_yolu, "eski-skill", "SKILL.md"),
            os.path.join(karantina_yolu, "alt", "dosya.py"),
        ]
        sonuc = kod_envanter.disla_uygula(dosyalar, disla_kume)
        self.assertEqual(sonuc, ["tools/x.py"])

    def test_disla_dizinlerini_yukle_gercek_modulden_gelir(self):
        # importlib ile tools/kod-orani-olcum.py'nin DISLA_DIZIN'i ile birebir aynı küme (tekrar tanım yok)
        _kaynak_spec = importlib.util.spec_from_file_location(
            "kod_orani_olcum_kaynak", os.path.join(KOK, "tools", "kod-orani-olcum.py"))
        kaynak = importlib.util.module_from_spec(_kaynak_spec)
        _kaynak_spec.loader.exec_module(kaynak)
        self.assertEqual(kod_envanter.disla_dizinlerini_yukle(KOK), set(kaynak.DISLA_DIZIN))


if __name__ == "__main__":
    unittest.main()
