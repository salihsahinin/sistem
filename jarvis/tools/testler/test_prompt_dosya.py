"""test_prompt_dosya.py — İB-79 prompt-başı deterministik dosya seçimi testleri (Karar 88 M12 a).
Geçici repoda sahte tüzük/defter/ledger/kapsül + tabloyla koşar: (1) eşleşme → doğru parça · (2) eşleşme yok → boş çıktı, kütük yok ·
(3) bütçe aşımı → gövde kesilir · (4) determinizm: aynı prompt iki koşumda aynı çıktı · (5) kütük satırı şeması.
Koşum: python3 -m unittest tools/testler/test_prompt_dosya.py"""
import importlib.util, json, os, subprocess, sys, tempfile, unittest

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT = os.path.join(KOK, "tools", "prompt-dosya.py")


def _yukle():
    spec = importlib.util.spec_from_file_location("prompt_dosya", SCRIPT)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


class PromptDosyaTest(unittest.TestCase):
    def setUp(self):
        self.m = _yukle()
        self.repo = tempfile.mkdtemp(prefix="pd-")
        os.makedirs(os.path.join(self.repo, "core")); os.makedirs(os.path.join(self.repo, "kuyruk")); os.makedirs(os.path.join(self.repo, "veri", "bronz"))
        with open(os.path.join(self.repo, "core", "tuzuk-v0.md"), "w", encoding="utf-8") as f:
            f.write("# Tüzük\n8. **Silme yasağı** eski kayıt arşive iner.\n9. **Push** yalnız Salih beyanıyla.\n")
        with open(os.path.join(self.repo, "kuyruk", "senaryo-defteri.md"), "w", encoding="utf-8") as f:
            f.write("# Defter\n**Karar 88 (2026-09-08, 9. masa):**\n- M3 (a)\n- M4 (a)\n- M5 (a)\n- M6\n")
        with open(os.path.join(self.repo, "veri", "karar-borcu.jsonl"), "w", encoding="utf-8") as f:
            f.write(json.dumps({"borc_id": "İB-79", "baslik": "hook", "durum": "icra-sırada", "not": "n"}, ensure_ascii=False) + "\n")
        with open(os.path.join(self.repo, "core", "durum-kapsulu.md"), "w", encoding="utf-8") as f:
            f.write("# K\n## Şu an\n- x\n## Sonraki ilk iş\n0. A\n1. B\n")
        with open(os.path.join(self.repo, "core", "buyuk.md"), "w", encoding="utf-8") as f:
            f.write("\n".join("y" * 200 for _ in range(40)))
        self.tablo = os.path.join(self.repo, "core", "prompt-dosya-tablosu.tsv")
        with open(self.tablo, "w", encoding="utf-8") as f:
            f.write("# yorum\n"
                    "\\bm\\.(\\d{1,2})\\b\ttuzuk:{1}\tmadde\n"
                    "\\bkarar (\\d{1,3})\\b\tdefter:{1}\tkarar\n"
                    "\\b(İB-\\d{1,3})\\b\tledger:{1}\tledger\n"
                    "\\bsıradaki\\b\tbolum:core/durum-kapsulu.md:## Sonraki ilk iş:2\tkapsül\n"
                    "\\bbüyük\\b\tcore/buyuk.md:1-40\tbütçe\n"
                    "\\bgaleri\\b\tuyari:md.49 dış-proje\tuyarı\n")

    def _kos(self, prompt, ekstra=()):
        r = subprocess.run([sys.executable, SCRIPT, "--repo", self.repo, "--tablo", self.tablo, *ekstra],
                           input=json.dumps({"prompt": prompt, "session_id": "t"}), capture_output=True, text=True)
        return r

    def test_eslesme_parcalar(self):
        out = self._kos("m.9 gereği push ve karar 88 ile İB-79, sıradaki ne? galeri de var").stdout
        self.assertIn("m.9", out); self.assertIn("**Push** yalnız Salih", out)
        self.assertIn("Karar 88", out); self.assertIn("- M5 (a)", out); self.assertNotIn("- M6", out)  # 4 satır sınırı
        self.assertIn("ledger İB-79", out); self.assertIn("durum=icra-sırada", out)
        self.assertIn("0. A", out); self.assertNotIn("1. B", out)  # 2 satır bölüm (başlık + 1)
        self.assertIn("UYARI", out); self.assertIn("md.49", out)
        self.assertNotIn("Silme yasağı", out)  # m.8 anılmadı

    def test_eslesme_yok_bos_ve_kutuksuz(self):
        r = self._kos("merhaba, bugün hava güzel")
        self.assertEqual(r.stdout.strip(), ""); self.assertEqual(r.returncode, 0)
        self.assertFalse(os.path.exists(os.path.join(self.repo, "veri", "bronz", "prompt-dosya-olay.jsonl")))

    def test_butce_kesme(self):
        out = self._kos("büyük dosya", ["--kuru"]).stdout
        self.assertIn("[kesildi]", out)
        self.assertLessEqual(len(out.encode("utf-8")), self.m.TOPLAM_BAYT + 200)

    def test_determinizm(self):
        a = self._kos("m.9 ve karar 88", ["--kuru"]).stdout; b = self._kos("m.9 ve karar 88", ["--kuru"]).stdout
        self.assertEqual(a, b)

    def test_kutuk_semasi(self):
        self._kos("m.9 push")
        k = os.path.join(self.repo, "veri", "bronz", "prompt-dosya-olay.jsonl")
        satirlar = [json.loads(s) for s in open(k, encoding="utf-8") if s.strip()]
        self.assertEqual(len(satirlar), 1)  # yalnız m.9 satırı (test tablosunda push anahtarı yok)
        for r in satirlar:
            for alan in ("ts", "oturum", "anahtar", "kaynak", "etiket", "bayt", "prompt_uzunluk"):
                self.assertIn(alan, r)


if __name__ == "__main__":
    unittest.main()
