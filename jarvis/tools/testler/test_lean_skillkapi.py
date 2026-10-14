"""test_lean_skillkapi.py — Lean 4 kanon kodunun (lean/Kanon/SkillKapi.lean) uçtan uca testi (Salih 2026-10-14, md → kod pilotu).
Koşar: `lake build` (kanıtlar derlemede denetlenir; biri bozulursa derleme düşer) → `skillkapi` ikilisine stdin vakaları →
beklenen hüküm. Lean (elan) kurulu değilse atlanır.
Koşum: python3 -m unittest tools/testler/test_lean_skillkapi.py"""
import os, shutil, subprocess, unittest

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LEAN = os.path.join(KOK, "lean")
ELAN = os.path.join(os.path.expanduser("~"), ".elan", "bin")
LAKE = shutil.which("lake") or shutil.which("lake", path=ELAN)
GECER = "y1=1\nkW=3\nr=1\ni=1\nf1=1\nf2=1\nf3=1\nf4=1\nf5=1\nturOzel=1\n"

VAKALAR = [
    ("tam kapsama", "kapsanmisTam=1\ny1=1\nsalihEmri=1\n", "RET-0"),
    ("gerek yok", "kW=9\n", "RET-0"),
    ("eşik altı, emir yok", "y2=1\nkW=2\n", "BEKLET"),
    ("emir var ama referans yok", "y1=1\nsalihEmri=1\ni=1\n", "ONAR-2"),
    ("prompt kapısı", GECER + "p=1\n", "ONAR-2"),
    ("tek bir biçim koşulu düşer", GECER.replace("f5=1", "f5=0"), "ONAR-3"),
    ("üretici yeni", GECER, "ÜRET-Ü-yeni"),
    ("ritüel önce, kısmi kapsama", GECER + "rituel=1\norkestrator=1\nkapsanmisKismi=1\n", "ÜRET-R-evrim"),
    ("değer payı: Δ biliniyor ve yetmiyor", GECER + "deltaBilinmiyor=0\ndegerYeter=0\n", "BEKLET"),
]


@unittest.skipUnless(LAKE, "Lean/lake kurulu değil")
class LeanSkillKapiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        env = dict(os.environ, PATH=ELAN + os.pathsep + os.environ.get("PATH", ""))
        r = subprocess.run([LAKE, "build"], cwd=LEAN, capture_output=True, text=True, encoding="utf-8", env=env)
        assert r.returncode == 0, r.stdout + r.stderr
        cls.exe = os.path.join(LEAN, ".lake", "build", "bin", "skillkapi" + (".exe" if os.name == "nt" else ""))

    def _kos(self, girdi):
        return subprocess.run([self.exe], input=girdi, capture_output=True, text=True, encoding="utf-8")

    def test_vakalar(self):
        for ad, girdi, beklenen in VAKALAR:
            with self.subTest(ad):
                r = self._kos(girdi)
                self.assertEqual(r.returncode, 0, r.stderr)
                self.assertEqual(r.stdout.strip(), beklenen)

    def test_girdi_hatasi(self):
        r = self._kos("bilinmeyen=1\n")
        self.assertEqual(r.returncode, 2); self.assertIn("bilinmeyen anahtar", r.stderr)
        r = self._kos("kW=üç\n")
        self.assertEqual(r.returncode, 2); self.assertIn("Nat beklenirken", r.stderr)


if __name__ == "__main__":
    unittest.main()
