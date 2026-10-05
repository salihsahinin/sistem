"""test_paket_yonlendir.py — bağlam paketi yönlendiricisi testleri (Karar 112).
Geçici repoda sahte manifest + dosyalarla koşar: (1) açık önek · (2) tetik · (3) yapışkan · (4) sessiz (çıktı/kütük/durum yok) ·
(5) geçiş sayacı + kapsül yönergesi + eşik · (6) eşitlikte aktif kalır · (7) ağır iş → alt-ajan · (8) öncelik → fable ·
(9) komutlar · (10) determinizm · (11) kütük şeması · (12) --denetle temiz/ihlal · (13) gerçek manifest temiz.
Koşum: python3 -m unittest tools/testler/test_paket_yonlendir.py"""
import json, os, subprocess, sys, tempfile, unittest

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT = os.path.join(KOK, "tools", "paket-yonlendir.py")

MANIFEST = {
    "esik_gecis": 2, "butce_bayt": 500, "kapsul_dizin": "core/paket-kapsul",
    "kademeler": {"sonnet": "Sonnet 5.5", "opus": "Opus 5.5", "fable": "Fable 5.1"},
    "agir_is": "\\b(araştır\\w*)", "oncelik": "\\b(yüksek öncelik\\w*|acil)\\b",
    "paketler": [
        {"id": "veri", "ad": "Veri", "kademe": "sonnet", "tetik": ["\\bsilver\\b", "\\bingest\\w*"],
         "cekirdek": ["core/veri.md"], "pointer": ["core/uzun.md"], "skill": ["damitma"]},
        {"id": "ajan", "ad": "Ajan", "kademe": "opus", "tetik": ["\\bişçi\\w*", "\\blider\\w*"],
         "cekirdek": ["core/ajan.md:1-2"], "pointer": [], "skill": []},
    ],
}


class PaketYonlendirTest(unittest.TestCase):
    def setUp(self):
        self.repo = tempfile.mkdtemp(prefix="py-")
        os.makedirs(os.path.join(self.repo, "core", "paket-kapsul"))
        for ad, govde in (("veri.md", "# veri\nkural\n"), ("ajan.md", "# ajan\nbir\niki\n"), ("uzun.md", "x" * 900)):
            with open(os.path.join(self.repo, "core", ad), "w", encoding="utf-8") as f:
                f.write(govde)
        self.manifest = os.path.join(self.repo, "core", "baglam-paketleri.json")
        self._manifest_yaz(MANIFEST)
        self.durum = os.path.join(self.repo, "state")
        self.kutuk = os.path.join(self.repo, "veri", "bronz", "paket-olay.jsonl")

    def _manifest_yaz(self, m):
        with open(self.manifest, "w", encoding="utf-8") as f:
            json.dump(m, f, ensure_ascii=False)

    def _kos(self, prompt, ekstra=(), oturum="t"):
        r = subprocess.run([sys.executable, SCRIPT, "--repo", self.repo, "--durum-dizin", self.durum, *ekstra],
                           input=json.dumps({"prompt": prompt, "session_id": oturum}), capture_output=True, text=True,
                           encoding="utf-8")
        self.assertEqual(r.returncode, 0, r.stderr)
        return r.stdout

    def _durum(self, oturum="t"):
        with open(os.path.join(self.durum, f"paket-{oturum}.json"), encoding="utf-8") as f:
            return json.load(f)

    def test_acik_onek(self):
        out = self._kos("ajan: emri nasıl yazarız")
        self.assertIn("[paket] ajan", out); self.assertIn("kural a: açık önek", out)
        self.assertIn("Opus 5.5", out); self.assertIn("core/ajan.md:1-2", out); self.assertIn("ilk yükleme", out)
        self.assertEqual(self._durum()["aktif"], "ajan")

    def test_tetik_ve_turkce_katlama(self):
        out = self._kos("SILVER bayat mı, İNGEST koşalım")
        self.assertIn("[paket] veri", out); self.assertIn("kural b", out); self.assertIn("ingest", out)
        self.assertIn("Sonnet 5.5", out); self.assertIn("ilgili skill: damitma", out)

    def test_yapiskan(self):
        self._kos("veri: başlayalım")
        out = self._kos("peki bunu nasıl yaparız")
        self.assertIn("[paket] veri (aktif; kural c)", out)
        self.assertEqual(len(out.strip().split("\n")), 1)  # aktif pakette tek satır

    def test_sessiz(self):
        out = self._kos("merhaba, bugün hava güzel")
        self.assertEqual(out.strip(), "")
        self.assertFalse(os.path.exists(self.kutuk)); self.assertFalse(os.path.exists(self.durum))

    def test_gecis_kapsul_esik(self):
        self._kos("veri: bir")
        out = self._kos("ajan: iki")
        self.assertIn("geçiş 1/2", out); self.assertIn("core/paket-kapsul/veri.md", out); self.assertNotIn("[eşik]", out)
        with open(os.path.join(self.repo, "core", "paket-kapsul", "veri.md"), "w", encoding="utf-8") as f:
            f.write("kaldığımız yer\n")
        out = self._kos("veri: üç")
        self.assertIn("geçiş 2/2", out); self.assertIn("[eşik]", out)
        self.assertIn("konu kapsülü var, oku: core/paket-kapsul/veri.md", out)
        self.assertIn("bu oturumda yüklendi", out); self.assertNotIn("ilk yükleme", out)
        d = self._durum()
        self.assertEqual(d["gecis"], 2); self.assertEqual(d["yuklu"], ["veri", "ajan"])

    def test_esitlikte_aktif_kalir(self):
        self._kos("ajan: başla")
        out = self._kos("işçi silver okusun")  # veri 1 · ajan 1 → aktif (ajan) kalır
        self.assertIn("[paket] ajan (aktif; kural b)", out)
        out = self._kos("silver ingest koşsun")  # veri 2 · ajan 0 → geçiş
        self.assertIn("[paket] veri", out); self.assertIn("geçiş 1/2", out)

    def test_agir_is_alt_ajan(self):
        out = self._kos("veri: silver sağlığını araştır")
        self.assertIn("ayrım: alt-ajan", out); self.assertIn("`model: sonnet`", out)
        out = self._kos("bunu da araştır")
        self.assertIn("ağır iş", out); self.assertIn("`model: sonnet`", out)

    def test_oncelik_fable(self):
        out = self._kos("veri: yüksek öncelikli, silver bozuk")
        self.assertIn("alt-ajan kademesi: Fable 5.1", out); self.assertIn("Oturum modelini Salih seçer", out); self.assertIn("paket varsayılanı Sonnet 5.5", out)

    def test_komutlar(self):
        self._kos("veri: bir"); self._kos("ajan: iki")
        self.assertIn("aktif ajan", self._kos("paket: durum"))
        out = self._kos("paket: kapat")
        self.assertIn("kapatıldı", out); self.assertIn("core/paket-kapsul/ajan.md", out)
        self.assertIsNone(self._durum()["aktif"]); self.assertEqual(self._durum()["yuklu"], ["veri", "ajan"])
        self._kos("paket: sıfırla")
        self.assertEqual(self._durum(), {"aktif": None, "yuklu": [], "gecis": 0})

    def test_determinizm_ve_kuru(self):
        a = self._kos("veri: silver", ["--kuru"]); b = self._kos("veri: silver", ["--kuru"])
        self.assertEqual(a, b); self.assertIn("ilk yükleme", b)  # --kuru durum yazmadı
        self.assertFalse(os.path.exists(self.kutuk))

    def test_kutuk_semasi(self):
        self._kos("veri: bir"); self._kos("devam"); self._kos("hava güzel", oturum="baska")
        satirlar = [json.loads(s) for s in open(self.kutuk, encoding="utf-8") if s.strip()]
        self.assertEqual(len(satirlar), 2)  # sessiz karar kütüğe düşmez
        for r in satirlar:
            for alan in ("ts", "oturum", "kural", "paket", "onceki", "gecis", "ilk_yukleme", "cekirdek_bayt", "kademe",
                         "ayrim", "prompt_uzunluk"):
                self.assertIn(alan, r)
        self.assertTrue(satirlar[0]["ilk_yukleme"]); self.assertFalse(satirlar[1]["ilk_yukleme"])

    def test_denetle(self):
        r = subprocess.run([sys.executable, SCRIPT, "--repo", self.repo, "--denetle"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 0, r.stdout)
        bozuk = json.loads(json.dumps(MANIFEST))
        bozuk["paketler"][0]["cekirdek"] = ["core/yok.md", "core/uzun.md"]
        bozuk["paketler"][1]["kademe"] = "haiku"
        bozuk["paketler"][1]["tetik"].append("\\bLider")
        self._manifest_yaz(bozuk)
        r = subprocess.run([sys.executable, SCRIPT, "--repo", self.repo, "--denetle"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 1)
        for beklenen in ("kırık core/yok.md", "> bütçe", "kademe tanımsız", "küçük harfli"):
            self.assertIn(beklenen, r.stdout)
        with open(self.manifest, "w", encoding="utf-8") as f:
            f.write("{bozuk")
        r = subprocess.run([sys.executable, SCRIPT, "--repo", self.repo, "--denetle"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 2)
        self.assertEqual(self._kos("veri: bir").strip(), "")  # bozuk manifestte hook susar, prompt engellenmez

    def test_gercek_manifest_temiz(self):
        r = subprocess.run([sys.executable, SCRIPT, "--repo", KOK, "--denetle"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()
