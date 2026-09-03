#!/usr/bin/env python3
"""gorsellestir.py testleri (İB-77 S; stdlib unittest, subprocess ile AXI arayüzü sınanır).
Koş: python3 -m unittest tools.testler.test_gorsellestir

Kapsam: d2 örneği → HTML + --dogrula 0 · bozuk d2 → 3 · vegalite bar scale.zero:false → 3 ·
vegalite geçerli → 0 + palet enjekte · tablo satır-uzunluğu uyumsuz → 3 · determinizm (iki
üretim bayt-bayt eşit) · jarvis-dışı dizinde kütük yazılmadı.

AÇIK SORU: mermaid ve vega-lite için gerçek tarayıcı-render doğrulaması bu ortamda YAPILAMAZ
(mmdc yok, headless tarayıcı yok); doğrulama yalnız YAPISAL kontrol seviyesindedir (spec şeması,
mark/encoding/data varlığı, ilk-satır diyagram türü). Bu, script'in --dogrula çıktısının "HTML
üretildi ve şema geçerli" dediği, "tarayıcıda doğru render olur" DEMEDİĞİ anlamına gelir.

Yan-etki: SALT-OKUR — geçici dizinlerde çalışır, repo'ya yazmaz (jarvis kütüğü testi HARİÇ; o
da ayrı geçici bir 'jarvis' adlı git deposu içinde çalışır, gerçek repo'ya dokunmaz)."""
import json
import os
import subprocess
import sys
import tempfile
import unittest

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARAC = os.path.join(KOK, "tools", "gorsellestir.py")


def kosum(*args, **kwargs):
    return subprocess.run(
        [sys.executable, ARAC] + list(args),
        capture_output=True, text=True, timeout=30, **kwargs
    )


def spec_yaz(dizin, ad, spec_obj):
    yol = os.path.join(dizin, ad)
    with open(yol, "w", encoding="utf-8") as fh:
        json.dump(spec_obj, fh, ensure_ascii=False)
    return yol


TEMEL_SPEC = {
    "baslik": "Test Süreci",
    "kaynak_ozet": "Birim test amaçlı spec.",
    "kaynak_pointer": "oturum: 2026-09-02 test",
    "icerik_sinifi": "surec",
    "gorsel_turu": "akis-semasi",
    "aciklama": ["Madde bir.", "Madde iki."],
    "tarih": "2026-09-02",
}


class GorsellestirTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dizin = self.tmp.name

    def tearDown(self):
        self.tmp.cleanup()

    def test_d2_geçerli_html_ve_dogrula_0(self):
        spec = dict(TEMEL_SPEC, arac="d2", spec="a -> b -> c")
        spec_yol = spec_yaz(self.dizin, "spec.json", spec)
        cikti = os.path.join(self.dizin, "cikti.html")
        r = kosum(spec_yol, "--cikti", cikti, "--dogrula", "--json")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue(os.path.isfile(cikti))
        veri = json.loads(r.stdout)
        self.assertTrue(veri["gecti"])
        with open(cikti, encoding="utf-8") as fh:
            html_metin = fh.read()
        for parca in ('id="baslik"', 'id="kaynak"', 'id="gorsel"', 'id="aciklama"', 'id="kunye"'):
            self.assertIn(parca, html_metin)

    def test_bozuk_d2_exit_3(self):
        spec = dict(TEMEL_SPEC, arac="d2", spec="a -> ; ; ; { bozuk sözdizimi [[[")
        spec_yol = spec_yaz(self.dizin, "spec.json", spec)
        cikti = os.path.join(self.dizin, "cikti.html")
        r = kosum(spec_yol, "--cikti", cikti, "--dogrula")
        self.assertEqual(r.returncode, 3, r.stdout + r.stderr)

    def test_vegalite_bar_scale_zero_false_exit_3(self):
        vega_spec = {
            "mark": "bar",
            "encoding": {
                "x": {"field": "kategori", "type": "nominal"},
                "y": {"field": "deger", "type": "quantitative", "scale": {"zero": False}},
            },
            "data": {"values": [{"kategori": "a", "deger": 5}, {"kategori": "b", "deger": 7}]},
        }
        spec = dict(TEMEL_SPEC, arac="vegalite", spec=vega_spec, icerik_sinifi="sayisal-karsilastirma")
        spec_yol = spec_yaz(self.dizin, "spec.json", spec)
        cikti = os.path.join(self.dizin, "cikti.html")
        r = kosum(spec_yol, "--cikti", cikti, "--dogrula")
        self.assertEqual(r.returncode, 3, r.stdout + r.stderr)

    def test_vegalite_gecerli_0_ve_palet_enjekte(self):
        vega_spec = {
            "mark": "bar",
            "encoding": {
                "x": {"field": "kategori", "type": "nominal"},
                "y": {"field": "deger", "type": "quantitative"},
            },
            "data": {"values": [{"kategori": "a", "deger": 5}, {"kategori": "b", "deger": 7}]},
        }
        spec = dict(TEMEL_SPEC, arac="vegalite", spec=vega_spec, icerik_sinifi="sayisal-karsilastirma")
        spec_yol = spec_yaz(self.dizin, "spec.json", spec)
        cikti = os.path.join(self.dizin, "cikti.html")
        r = kosum(spec_yol, "--cikti", cikti, "--dogrula")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        with open(cikti, encoding="utf-8") as fh:
            html_metin = fh.read()
        self.assertIn("#E69F00", html_metin)
        self.assertIn("#56B4E9", html_metin)

    def test_tablo_satir_uzunlugu_uyumsuz_exit_3(self):
        tablo_spec = {"basliklar": ["a", "b"], "satirlar": [["1", "2"], ["3"]]}
        spec = dict(TEMEL_SPEC, arac="tablo", spec=tablo_spec, icerik_sinifi="karsilastirma")
        spec_yol = spec_yaz(self.dizin, "spec.json", spec)
        cikti = os.path.join(self.dizin, "cikti.html")
        r = kosum(spec_yol, "--cikti", cikti, "--dogrula")
        self.assertEqual(r.returncode, 3, r.stdout + r.stderr)

    def test_determinizm_iki_uretim_esit(self):
        spec = dict(TEMEL_SPEC, arac="d2", spec="x -> y")
        spec_yol = spec_yaz(self.dizin, "spec.json", spec)
        cikti1 = os.path.join(self.dizin, "cikti1.html")
        cikti2 = os.path.join(self.dizin, "cikti2.html")
        r1 = kosum(spec_yol, "--cikti", cikti1, "--dogrula")
        r2 = kosum(spec_yol, "--cikti", cikti2, "--dogrula")
        self.assertEqual(r1.returncode, 0, r1.stderr)
        self.assertEqual(r2.returncode, 0, r2.stderr)
        with open(cikti1, "rb") as fh1, open(cikti2, "rb") as fh2:
            self.assertEqual(fh1.read(), fh2.read())

    def test_offline_vegalite_gercek_svg_ve_cdn_yok(self):
        vega_spec = {
            "mark": "bar",
            "encoding": {
                "x": {"field": "kategori", "type": "nominal"},
                "y": {"field": "deger", "type": "quantitative"},
            },
            "data": {"values": [{"kategori": "a", "deger": 5}, {"kategori": "b", "deger": 7}]},
        }
        spec = dict(TEMEL_SPEC, arac="vegalite", spec=vega_spec, icerik_sinifi="sayisal-karsilastirma")
        spec_yol = spec_yaz(self.dizin, "spec.json", spec)
        cikti = os.path.join(self.dizin, "cikti.html")
        r = kosum(spec_yol, "--cikti", cikti, "--offline", "--dogrula", "--json", "--repo", KOK)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        with open(cikti, encoding="utf-8") as fh:
            html_metin = fh.read()
        self.assertNotIn("cdn.jsdelivr.net", html_metin)
        self.assertIn("<svg", html_metin)
        self.assertIn("kip: offline", html_metin)

    def test_offline_mermaid_gercek_svg_veya_atlanir(self):
        # mmdc/chromium bu ortamda kurulu olmayabilir; kuruluysa 0, değilse test kendini atlar
        # (uydurma sonuç yok — case gereği "çalışmıyorsa exit≠0 → FAIL mesajı").
        mmdc_var = subprocess.run(["which", "mmdc"], capture_output=True, text=True).returncode == 0
        if not mmdc_var:
            self.skipTest("mmdc/chromium yok")
        spec = dict(TEMEL_SPEC, arac="mermaid", spec="flowchart LR\na-->b", gorsel_turu="akis-semasi")
        spec_yol = spec_yaz(self.dizin, "spec.json", spec)
        cikti = os.path.join(self.dizin, "cikti.html")
        r = kosum(spec_yol, "--cikti", cikti, "--offline", "--dogrula", "--json")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        with open(cikti, encoding="utf-8") as fh:
            html_metin = fh.read()
        self.assertNotIn("cdn.jsdelivr.net", html_metin)
        self.assertIn("<svg", html_metin)

    def test_offline_determinizm_iki_uretim_esit(self):
        spec = dict(TEMEL_SPEC, arac="d2", spec="x -> y")
        spec_yol = spec_yaz(self.dizin, "spec.json", spec)
        cikti1 = os.path.join(self.dizin, "cikti1.html")
        cikti2 = os.path.join(self.dizin, "cikti2.html")
        r1 = kosum(spec_yol, "--cikti", cikti1, "--offline", "--dogrula")
        r2 = kosum(spec_yol, "--cikti", cikti2, "--offline", "--dogrula")
        self.assertEqual(r1.returncode, 0, r1.stderr)
        self.assertEqual(r2.returncode, 0, r2.stderr)
        with open(cikti1, "rb") as fh1, open(cikti2, "rb") as fh2:
            self.assertEqual(fh1.read(), fh2.read())

    def _ogrenme_spec(self, **override):
        ogrenme = {
            "hedef": "Bu görselden sonra tümevarım kanıtının adımlarını açıklayabilmelisin.",
            "on_bilgi": ["Doğal sayılar", "Önerme mantığı"],
            "cozulmus_ornek": [
                "Taban adımı: n=1 için önerme doğrulanır — başlangıç noktası kurulur.",
                "Tümevarım hipotezi: n=k için önerme doğru varsayılır — adım için zemin.",
                "Tümevarım adımı: n=k+1 için önerme kanıtlanır — hipotez kullanılır.",
                "Sonuç: tüm doğal sayılar için önerme doğrudur — adımlar birleştirilir.",
            ],
            "kendini_sina": [
                {"soru": "Taban adımı neden gereklidir?", "cevap": "Zincirin başlangıç noktasını kurar."},
                {"soru": "Tümevarım hipotezi ne işe yarar?", "cevap": "n=k+1 adımında kullanılacak varsayımı verir."},
            ],
            "tuzaklar": ["Taban adımını atlamak", "Hipotezi kanıtlamadan sonuç çıkarmak"],
            "sonraki_adim": "Güçlü tümevarımı dene.",
        }
        ogrenme.update(override)
        spec = dict(TEMEL_SPEC, arac="d2", spec="taban -> hipotez -> adim -> sonuc", ogrenme=ogrenme)
        return spec

    def test_ogrenme_tam_spec_0_ve_bloklar_ve_details(self):
        spec = self._ogrenme_spec()
        spec_yol = spec_yaz(self.dizin, "spec.json", spec)
        cikti = os.path.join(self.dizin, "cikti.html")
        r = kosum(spec_yol, "--cikti", cikti, "--dogrula", "--json")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        veri = json.loads(r.stdout)
        self.assertTrue(veri["gecti"])
        self.assertIn("ogrenme", veri["kip"])
        with open(cikti, encoding="utf-8") as fh:
            html_metin = fh.read()
        for parca in ('id="ogrenme-hedef"', 'id="cozulmus-ornek"', 'id="kendini-sina"', 'id="tuzaklar"'):
            self.assertIn(parca, html_metin)
        self.assertIn("<details>", html_metin)

    def test_ogrenme_hedefte_yetenek_fiili_yok_exit_3(self):
        spec = self._ogrenme_spec(hedef="Bu görsel tümevarım hakkındadır.")
        spec_yol = spec_yaz(self.dizin, "spec.json", spec)
        cikti = os.path.join(self.dizin, "cikti.html")
        r = kosum(spec_yol, "--cikti", cikti, "--dogrula")
        self.assertEqual(r.returncode, 3, r.stdout + r.stderr)

    def test_ogrenme_bayragi_ama_alan_yok_exit_3(self):
        spec = dict(TEMEL_SPEC, arac="d2", spec="a -> b")
        spec_yol = spec_yaz(self.dizin, "spec.json", spec)
        cikti = os.path.join(self.dizin, "cikti.html")
        r = kosum(spec_yol, "--cikti", cikti, "--ogrenme", "--dogrula")
        self.assertEqual(r.returncode, 3, r.stdout + r.stderr)

    def test_ogrenme_kendini_sina_tek_soru_exit_3(self):
        spec = self._ogrenme_spec(kendini_sina=[{"soru": "Tek soru?", "cevap": "Tek cevap."}])
        spec_yol = spec_yaz(self.dizin, "spec.json", spec)
        cikti = os.path.join(self.dizin, "cikti.html")
        r = kosum(spec_yol, "--cikti", cikti, "--dogrula")
        self.assertEqual(r.returncode, 3, r.stdout + r.stderr)

    def test_jarvis_disi_dizinde_kutuk_yazilmadi(self):
        # jarvis-dışı bir git deposu simüle edilir: kök adı 'jarvis' DEĞİL.
        disi_repo = os.path.join(self.dizin, "baska-proje")
        os.makedirs(disi_repo)
        subprocess.run(["git", "init", "-q"], cwd=disi_repo, check=True)
        spec = dict(TEMEL_SPEC, arac="d2", spec="p -> q")
        spec_yol = spec_yaz(disi_repo, "spec.json", spec)
        r = kosum(spec_yol, "--repo", disi_repo, "--dogrula")
        self.assertEqual(r.returncode, 0, r.stderr)
        beklenen_cikti = os.path.join(disi_repo, "gorsel")
        self.assertTrue(os.path.isdir(beklenen_cikti))
        kutuk_yol = os.path.join(disi_repo, "veri", "bronz", "gorsel-olay.jsonl")
        self.assertFalse(os.path.exists(kutuk_yol))


if __name__ == "__main__":
    unittest.main()
