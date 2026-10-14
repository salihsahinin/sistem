"""test_paket_yonlendir.py — bağlam paketi yönlendiricisi testleri (Karar 112; EK-2 10-14 niyet düzeyi).
Geçici repoda sahte manifest + dosyalarla koşar: (1) açık önek · (2) EK-2 regresyon: tetik sözcüğü ve bildirim gövdesi sessiz ·
(3) önek yokken aktif pakette yapışma yok · (4) sessiz (çıktı/kütük/durum yok) · (5) geçiş sayacı + kapsül yönergesi + eşik ·
(6) --sec iki paket: birincil + ek yükleme · (7) ağır iş → alt-ajan · (8) öncelik → fable · (9) komutlar · (10) determinizm ·
(11) kütük şeması · (12) --denetle temiz/ihlal · (13) gerçek manifest temiz · (14) --sec tavan/bilinmeyen/yok · (15) son-oturum.
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

    def _sec(self, ciftler, ekstra=(), oturum="t", rc=0):
        arg = []
        for n, pid in ciftler:
            arg += ["--niyet", n, "--paket", pid]
        r = subprocess.run([sys.executable, SCRIPT, "--repo", self.repo, "--durum-dizin", self.durum, "--sec", *arg,
                            *(["--oturum", oturum] if oturum else []), *ekstra],
                           capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, rc, r.stderr)
        return r.stdout + r.stderr

    def _durum(self, oturum="t"):
        with open(os.path.join(self.durum, f"paket-{oturum}.json"), encoding="utf-8") as f:
            return json.load(f)

    def test_acik_onek(self):
        out = self._kos("ajan: emri nasıl yazarız")
        self.assertIn("[paket] ajan", out); self.assertIn("kural a: açık önek", out)
        self.assertIn("Opus 5.5", out); self.assertIn("core/ajan.md:1-2", out); self.assertIn("ilk yükleme", out)
        self.assertEqual(self._durum()["aktif"], "ajan")

    def test_ek2_sozcuk_ve_bildirim_sessiz(self):
        # EK-2 regresyonu (10-14 kütük vakaları): tetik sözcüğü ve alt-ajan bildirim gövdesi paket açmaz
        self.assertEqual(self._kos("SILVER bayat mı, İNGEST koşalım").strip(), "")
        self.assertEqual(self._kos("<task-notification>işçi lider silver ingest</task-notification>").strip(), "")
        self.assertFalse(os.path.exists(self.kutuk))

    def test_yapisma_yok(self):
        self._kos("veri: başlayalım")
        self.assertEqual(self._kos("peki bunu nasıl yaparız").strip(), "")  # paket seçimi modelde (--sec)
        self.assertEqual(self._durum()["aktif"], "veri")

    def test_sessiz(self):
        out = self._kos("merhaba, bugün hava güzel")
        self.assertEqual(out.strip(), "")
        self.assertFalse(os.path.exists(self.kutuk))
        self.assertEqual(os.listdir(self.durum), ["son-oturum.txt"])  # paket durumu yazılmaz, yalnız oturum işareti (EK-2)

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

    def test_sec_birincil_ve_ek(self):
        self._kos("ajan: başla")
        out = self._sec([("silver bayat", "veri"), ("işçi emri", "ajan"), ("hava güzel", "yok")])
        self.assertIn("[paket] veri · Veri (kural m: niyet: silver bayat)", out); self.assertIn("geçiş 1/2", out)
        self.assertIn("[paket] ajan · Ajan (ek yükleme · kural m", out)
        self.assertEqual(out.count("geçiş "), 1)  # ek yükleme geçiş saymaz
        d = self._durum()
        self.assertEqual(d["aktif"], "veri"); self.assertEqual(d["gecis"], 1); self.assertEqual(d["yuklu"], ["ajan", "veri"])
        satirlar = [json.loads(x) for x in open(self.kutuk, encoding="utf-8") if x.strip()]
        sec = [r for r in satirlar if r["kural"] == "m"]
        self.assertEqual([r["paket"] for r in sec], ["veri", "ajan", None])
        self.assertEqual([r.get("ek") for r in sec], [False, True, None]); self.assertEqual(sec[2]["niyet"], "hava güzel")
        self.assertIn("görünür etiket", out); self.assertIn("`[paket] veri ← silver bayat · ajan ← işçi emri`", out)
        self._sec([("silver bayat", "ajan")], ["--duzeltme"])
        son = [json.loads(x) for x in open(self.kutuk, encoding="utf-8") if x.strip()][-1]
        self.assertTrue(son["duzeltme"]); self.assertEqual(son["paket"], "ajan")

    def test_agir_is_alt_ajan(self):
        out = self._kos("veri: silver sağlığını araştır")
        self.assertIn("ayrım: alt-ajan", out); self.assertIn("`model: sonnet`", out)
        out = self._sec([("bunu da araştır", "veri")])
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
        self._kos("veri: bir"); self._kos("veri: devam"); self._kos("hava güzel", oturum="baska")
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

    def test_sec_tavan_bilinmeyen_yok(self):
        out = self._sec([("a", "veri"), ("b", "ajan"), ("c", "kanon")], rc=1)
        self.assertIn("bilinmeyen paket: kanon", out)
        m = json.loads(json.dumps(MANIFEST)); m["tavan_paket"] = 1; self._manifest_yaz(m)
        self.assertIn("en çok 1 farklı paket", self._sec([("a", "veri"), ("b", "ajan")], rc=1))
        self.assertFalse(os.path.exists(self.kutuk))  # hatada kütük yazılmaz
        out = self._sec([("selam", "yok")])
        self.assertIn("[paket] yok", out); self.assertIsNone(self._durum()["aktif"])
        r = subprocess.run([sys.executable, SCRIPT, "--repo", self.repo, "--sec", "--niyet", "x"], capture_output=True,
                           text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 2)  # niyet/paket sayısı eşit değil

    def test_son_oturum(self):
        self._kos("merhaba", oturum="oturumA")  # sessiz mesaj da son-oturum'u yazar
        with open(os.path.join(self.durum, "son-oturum.txt"), encoding="utf-8") as f:
            self.assertEqual(f.read(), "oturumA")
        self._sec([("silver", "veri")], oturum=None)
        self.assertEqual(self._durum("oturumA")["aktif"], "veri")

    def test_gercek_manifest_temiz(self):
        r = subprocess.run([sys.executable, SCRIPT, "--repo", KOK, "--denetle"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()
