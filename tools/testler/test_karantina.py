#!/usr/bin/env python3
"""karantina.py testleri (İB-72; AXI-STANDARDI.md A1/A2/A7; stdlib unittest).
Koş: python3 -m unittest tools/testler/test_karantina.py
Kapsam: (a) --ekle sahte bir git-fixture repo'da dosyayı arsiv/karantina/ altına git mv ile taşıyor +
veri/karantina.jsonl'e 5-alanlı satır ekliyor · (b) --denetle gerçek repodaki kod-orani-olcum.py karantina
dizinini TARAMIYORKEN PASS (kod 0) veriyor · (c) --liste boş/dolu durumlarda doğru çalışıyor.
Gerçek ~/jarvis dosyalarına DOKUNULMAZ — her --ekle testi izole tempdir'de kendi git repo fixture'ını kurar.
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARAC = os.path.join(KOK, "tools", "karantina.py")


def kos(*args, cwd=None):
    return subprocess.run([sys.executable, ARAC] + list(args), cwd=cwd or KOK, capture_output=True, text=True)


def fixture_repo(tmp):
    """İzole tmp dizininde küçük bir git repo kurar; tools/kod-orani-olcum.py'yi de kopyalar
    ki --denetle bu fixture üzerinde de çalışabilsin (yalnız gerçek repoya dokunmadan)."""
    subprocess.run(["git", "init", "-q"], cwd=tmp, check=True)
    subprocess.run(["git", "config", "user.email", "test@test"], cwd=tmp, check=True)
    subprocess.run(["git", "config", "user.name", "test"], cwd=tmp, check=True)
    os.makedirs(os.path.join(tmp, "veri"), exist_ok=True)
    os.makedirs(os.path.join(tmp, "sahte", "alt"), exist_ok=True)
    with open(os.path.join(tmp, "sahte", "alt", "bayat.md"), "w", encoding="utf-8") as fh:
        fh.write("# bayat test dosyası\n")
    open(os.path.join(tmp, "veri", "karantina.jsonl"), "w").close()
    subprocess.run(["git", "add", "."], cwd=tmp, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "fixture"], cwd=tmp, check=True)
    return tmp


def kutuk_oku(tmp):
    yol = os.path.join(tmp, "veri", "karantina.jsonl")
    if not os.path.exists(yol):
        return []
    with open(yol, encoding="utf-8") as fh:
        return [json.loads(s) for s in fh if s.strip()]


class TestEkle(unittest.TestCase):
    def test_ekle_tasir_ve_jsonl_yazar(self):
        with tempfile.TemporaryDirectory() as tmp:
            fixture_repo(tmp)
            kaynak = os.path.join("sahte", "alt", "bayat.md")
            r = kos("--repo", tmp, "--ekle", kaynak, "--beyan", "Salih: bu dosya bayat, karantinaya al")
            self.assertEqual(r.returncode, 0, r.stderr)
            eski = os.path.join(tmp, kaynak)
            yeni = os.path.join(tmp, "arsiv", "karantina", kaynak)
            self.assertFalse(os.path.exists(eski), "kaynak hâlâ eski yerde duruyor")
            self.assertTrue(os.path.exists(yeni), "hedefte dosya yok")
            kayitlar = kutuk_oku(tmp)
            self.assertEqual(len(kayitlar), 1)
            k = kayitlar[0]
            for alan in ("yol", "tescil_tarihi", "salih_beyani", "neden", "git_head"):
                self.assertIn(alan, k)
            self.assertEqual(k["yol"], kaynak)

    def test_ekle_beyansiz_reddedilir(self):
        with tempfile.TemporaryDirectory() as tmp:
            fixture_repo(tmp)
            r = kos("--repo", tmp, "--ekle", os.path.join("sahte", "alt", "bayat.md"))
            self.assertEqual(r.returncode, 2)

    def test_ekle_olmayan_dosya_hata(self):
        with tempfile.TemporaryDirectory() as tmp:
            fixture_repo(tmp)
            r = kos("--repo", tmp, "--ekle", "yok-boyle-dosya.md", "--beyan", "x")
            self.assertEqual(r.returncode, 2)


class TestDenetle(unittest.TestCase):
    def test_denetle_gercek_repoda_pass(self):
        # gerçek ~/jarvis repo, salt-okur: kod-orani-olcum.py karantina dizinini tarıyor mu diye bakar
        r = kos("--repo", KOK, "--denetle")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_denetle_bozuk_jsonl_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            fixture_repo(tmp)
            with open(os.path.join(tmp, "veri", "karantina.jsonl"), "w", encoding="utf-8") as fh:
                fh.write('{"yol": "a.md", "tescil_tarihi": "2026-09-03"}\n')  # eksik alan
            r = kos("--repo", tmp, "--denetle")
            self.assertEqual(r.returncode, 1)


class TestListe(unittest.TestCase):
    def test_liste_bos(self):
        with tempfile.TemporaryDirectory() as tmp:
            fixture_repo(tmp)
            r = kos("--repo", tmp, "--liste")
            self.assertEqual(r.returncode, 0)
            self.assertIn("BOŞ", r.stdout)

    def test_liste_dolu(self):
        with tempfile.TemporaryDirectory() as tmp:
            fixture_repo(tmp)
            kaynak = os.path.join("sahte", "alt", "bayat.md")
            kos("--repo", tmp, "--ekle", kaynak, "--beyan", "Salih: karantina")
            r = kos("--repo", tmp, "--liste")
            self.assertEqual(r.returncode, 0)
            self.assertIn(kaynak, r.stdout)


if __name__ == "__main__":
    unittest.main()
