"""devir-md2json.py birim testleri (İB-93, 2026-09-16): tam blok türetimi · eksik alan · çıktı-izin çelişkisi ·
çıktı-başına done · dal tavanı · --dogrula farkı · çit yok."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

KOK = Path(__file__).resolve().parents[2]
SCRIPT = KOK / "tools" / "devir-md2json.py"

TAM = """# GÖREV — test
```lojik
DEVİR_ID: devir-2026-09-16-test
KAYNAK_YÜZEY: fable-ana-sira
HEDEF_KATMAN: lider
TARİH: 2026-09-16
EMİR_YOLU: cc/gelen/gorev-test.md
BAĞLI_DEVİR: devir-2026-09-10-tur2
NİÇİN_ŞİMDİ: S2 K etiketi açık
AMAÇ: tek cümle amaç
ÇIKTI:
  C1: cc/giden/devir-2026-09-16-test/cevap.md
  C2: cc/giden/devir-2026-09-16-test-geri-donus.md
DONE:
  C1: cevap.md VAR ∧ her iddia D/K/X
  C2: geri-donus 10+2 alanla VAR
DALLAR:
  - D1: eğer URL açılamıyorsa → X etiketi
  - D-KATMAN1: kural değişikliği → DUR
YAZMA_İZNİ:
  - cc/giden/devir-2026-09-16-test/**
  - cc/giden/devir-2026-09-16-test-geri-donus.md
YASAK:
  - kanon/ yazımı
EAGER:
  - core/rol.md
LAZY:
  - core/sablonlar/geri-donus-v0.md — geri-dönüş yazarken
KARAR_ÖZETİ:
  - Karar 89: Opus 5 effort medium sabit
KAPALI_GÖZ_ÖZETİ: cc/gelen/devir-2026-09-09-parti5-envanter.md
ÖLÇEN: Jarvis ana-sıra (yapan ≠ ölçen)
BÜTÇE: model=opus effort=medium arac_cagri_tavani=40 beklenen_ajan_cagrisi=0
YENİDEN_DENEME: 2
GİT_İZNİ: pathspec-only
PUSH: false
KARAR_YETKİSİ: false
OTURUM: devam
KAPANIŞ:
  - geri-dönüş 10+2 alan
  - git add <yol> + commit; push yok
```
"""


def kos(md: str, *ek):
    d = tempfile.mkdtemp()
    p = Path(d) / "gorev.md"
    p.write_text(md, encoding="utf-8")
    r = subprocess.run([sys.executable, str(SCRIPT), str(p), *ek], capture_output=True, text=True)
    return r, Path(d)


class Test(unittest.TestCase):
    def test_tam_turetim(self):
        r, d = kos(TAM)
        self.assertEqual(r.returncode, 0, r.stderr)
        j = json.loads((d / "devir-2026-09-16-test.json").read_text())
        self.assertEqual(j["devir"]["kimlik"]["bagli_devir"], "devir-2026-09-10-tur2")
        self.assertEqual(len(j["devir"]["gorev"]["ciktilar"]), 2)
        self.assertIn("[C1]", j["devir"]["gorev"]["done_yuklemi"])
        self.assertEqual(j["devir"]["butce"]["arac_cagri_tavani"], 40)
        self.assertEqual(j["devir"]["gorev"]["olcen"], "Jarvis ana-sıra (yapan ≠ ölçen)")
        self.assertEqual(j["devir"]["oturum"]["durum"], "devam")
        self.assertEqual((d / ".aktif-devir").read_text().strip(), "devir-2026-09-16-test")
        self.assertFalse(j["devir"]["yetki"]["push"])

    def test_eksik_alan(self):
        r, _ = kos(TAM.replace("NİÇİN_ŞİMDİ: S2 K etiketi açık\n", ""))
        self.assertEqual(r.returncode, 2)
        self.assertIn("NİÇİN_ŞİMDİ", r.stderr)

    def test_cikti_izin_celiskisi(self):
        r, _ = kos(TAM.replace("  C2: cc/giden/devir-2026-09-16-test-geri-donus.md", "  C2: kanon/tuzuk.md"))
        self.assertEqual(r.returncode, 2)
        self.assertIn("yazma-izni dışında", r.stderr)

    def test_cikti_basina_done(self):
        r, _ = kos(TAM.replace("  C2: geri-donus 10+2 alanla VAR\n", ""))
        self.assertEqual(r.returncode, 2)
        self.assertIn("DONE eksik: C2", r.stderr)

    def test_dal_tavani(self):
        fazla = "".join(f"  - D{i}: eğer x{i} → y{i}\n" for i in range(2, 8))
        r, _ = kos(TAM.replace("  - D-KATMAN1: kural değişikliği → DUR\n", fazla))
        self.assertEqual(r.returncode, 2)
        self.assertIn("görevi böl", r.stderr)

    def test_dogrula_fark_ve_es(self):
        r, d = kos(TAM)
        j = d / "devir-2026-09-16-test.json"
        r2 = subprocess.run([sys.executable, str(SCRIPT), str(d / "gorev.md"), "--dogrula", str(j)], capture_output=True, text=True)
        self.assertEqual(r2.returncode, 0)
        (d / "gorev.md").write_text(TAM.replace("tek cümle amaç", "değişti"), encoding="utf-8")
        r3 = subprocess.run([sys.executable, str(SCRIPT), str(d / "gorev.md"), "--dogrula", str(j)], capture_output=True, text=True)
        self.assertEqual(r3.returncode, 3)
        self.assertIn("md kazanır", r3.stderr)

    def test_kaynaklar_zorunlu_url_varsa(self):
        r, _ = kos(TAM.replace("AMAÇ: tek cümle amaç", "AMAÇ: https://code.claude.com/docs/en/permissions sayfasını aç"))
        self.assertEqual(r.returncode, 2)
        self.assertIn("KAYNAKLAR", r.stderr)
        r2, _ = kos(TAM.replace("AMAÇ: tek cümle amaç", "AMAÇ: https://code.claude.com/docs/en/permissions sayfasını aç\nKAYNAKLAR:\n  R1: https://code.claude.com/docs/en/permissions"))
        self.assertEqual(r2.returncode, 0, r2.stderr)

    def test_oturum_degeri(self):
        r, _ = kos(TAM.replace("OTURUM: devam", "OTURUM: belki"))
        self.assertEqual(r.returncode, 2)

    def test_cit_yok(self):
        r, _ = kos("# md ama lojik çiti yok\n")
        self.assertEqual(r.returncode, 4)


if __name__ == "__main__":
    unittest.main()
