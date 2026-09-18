#!/usr/bin/env python3
"""kod-orani-olcum.py testleri (İB-71 baseline; AXI-STANDARDI.md A1/A2/A7; stdlib unittest).
Koş: python3 -m unittest tools/testler/test_kod_orani.py
Kapsam: (a) kova sınıflandırması uzantı→kova doğru mu · (b) .git/veri/bronz/veri/gorunum dışlanıyor mu ·
(c) --json çıktısı json.loads ile parse edilebiliyor mu (+ --kuru ile kütük yazılmıyor)."""
import json
import os
import subprocess
import sys
import tempfile
import unittest

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARAC = os.path.join(KOK, "tools", "kod-orani-olcum.py")

sys.path.insert(0, os.path.join(KOK, "tools"))
import importlib.util

_spec = importlib.util.spec_from_file_location("kod_orani_olcum", ARAC)
kod_orani_olcum = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(kod_orani_olcum)


def kos(*args):
    return subprocess.run([sys.executable, ARAC] + list(args), cwd=KOK, capture_output=True, text=True)


class KovaSiniflandirmaTest(unittest.TestCase):
    def test_md_kovasi(self):
        self.assertEqual(kod_orani_olcum.kova_ver("core/durum-kapsulu.md"), "md")

    def test_kod_kovasi_py_sh_sql(self):
        self.assertEqual(kod_orani_olcum.kova_ver("tools/x.py"), "kod")
        self.assertEqual(kod_orani_olcum.kova_ver("bin/y.sh"), "kod")
        self.assertEqual(kod_orani_olcum.kova_ver("z.sql"), "kod")

    def test_yapisal_kovasi(self):
        self.assertEqual(kod_orani_olcum.kova_ver("a.json"), "yapisal")
        self.assertEqual(kod_orani_olcum.kova_ver("b.jsonl"), "yapisal")
        self.assertEqual(kod_orani_olcum.kova_ver("c.csv"), "yapisal")

    def test_diger_kovasi(self):
        self.assertEqual(kod_orani_olcum.kova_ver("gorsel.png"), "diger")
        self.assertEqual(kod_orani_olcum.kova_ver("uzantisiz"), "diger")


class DislamaTest(unittest.TestCase):
    def test_git_ve_veri_alt_dizinleri_dislanir(self):
        with tempfile.TemporaryDirectory() as tmp:
            os.makedirs(os.path.join(tmp, ".git"))
            with open(os.path.join(tmp, ".git", "icinde.md"), "w") as f:
                f.write("gizli\n")
            os.makedirs(os.path.join(tmp, "veri", "bronz"))
            with open(os.path.join(tmp, "veri", "bronz", "olay.jsonl"), "w") as f:
                f.write("{}\n")
            os.makedirs(os.path.join(tmp, "veri", "gorunum"))
            with open(os.path.join(tmp, "veri", "gorunum", "v_x.csv"), "w") as f:
                f.write("a,b\n1,2\n")
            os.makedirs(os.path.join(tmp, "veri", "silver"))
            with open(os.path.join(tmp, "veri", "silver", "kalir.jsonl"), "w") as f:
                f.write("{}\n")
            with open(os.path.join(tmp, "kok.md"), "w") as f:
                f.write("# baslik\nsatir2\n")

            oran, okunamayan = kod_orani_olcum.repo_envanteri(tmp)

            toplam_dosya = sum(oran[k + "_dosya"] for k in ("md", "kod", "yapisal", "diger"))
            self.assertEqual(toplam_dosya, 2)  # kok.md + veri/silver/kalir.jsonl
            self.assertEqual(oran["md_dosya"], 1)
            self.assertEqual(oran["yapisal_dosya"], 1)
            self.assertEqual(okunamayan, 0)


class GitignoreDislamaTest(unittest.TestCase):
    def test_gitignore_dosyasi_envanterden_dislanir(self):
        """M15 (Karar 88): .venv benzeri gitignore'lu içerik repo_envanteri sayımına girmemeli."""
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(["git", "init", "-q"], cwd=tmp, check=True)
            with open(os.path.join(tmp, ".gitignore"), "w") as f:
                f.write("ignored_dir/\nignored_dosya.txt\n")
            os.makedirs(os.path.join(tmp, "ignored_dir"))
            with open(os.path.join(tmp, "ignored_dir", "icinde.py"), "w") as f:
                f.write("x = 1\n")
            with open(os.path.join(tmp, "ignored_dosya.txt"), "w") as f:
                f.write("gizli\n")
            with open(os.path.join(tmp, "kalir.md"), "w") as f:
                f.write("# baslik\n")

            oran, okunamayan = kod_orani_olcum.repo_envanteri(tmp)

            toplam_dosya = sum(oran[k + "_dosya"] for k in ("md", "kod", "yapisal", "diger"))
            # kalir.md + .gitignore'un kendisi (o da git-dışı ama ignore'lu DEĞİL, envantere girmesi doğru);
            # ignored_dir/icinde.py ve ignored_dosya.txt dışlandı → kod kovasına hiçbir dosya girmemeli
            self.assertEqual(toplam_dosya, 2)
            self.assertEqual(oran["md_dosya"], 1)
            self.assertEqual(oran["kod_dosya"], 0)
            self.assertEqual(okunamayan, 0)

    def test_git_yoksa_fallback_none_doner(self):
        with tempfile.TemporaryDirectory() as tmp:  # git init yok → gitignore_disla_kumesi None döner
            self.assertIsNone(kod_orani_olcum.gitignore_disla_kumesi(tmp))


class JsonCiktiTest(unittest.TestCase):
    def test_json_parse_edilir_ve_alanlar_dolu(self):
        r = kos("--json", "--kuru", "--sessiz")
        self.assertEqual(r.returncode, 0, r.stderr[:500])
        d = json.loads(r.stdout)
        for alan in ("arac", "surum", "git_head", "cikis", "kayit"):
            self.assertIn(alan, d)
        self.assertEqual(d["arac"], "kod-orani-olcum")
        self.assertEqual(d["cikis"], r.returncode)
        self.assertFalse(d["kutuk_yazildi"])  # --kuru
        for alan in ("tarih", "git_head", "repo_orani", "baglam_orani"):
            self.assertIn(alan, d["kayit"])
        for k in ("md_satir", "kod_satir", "yapisal_satir", "diger_satir"):
            self.assertIn(k, d["kayit"]["repo_orani"])
            self.assertIn(k, d["kayit"]["baglam_orani"])

    def test_bilinmeyen_bayrak_cikis_2(self):
        r = kos("--yok")
        self.assertEqual(r.returncode, 2)

    def test_kuru_kutuge_yazmaz(self):
        kutuk = os.path.join(KOK, "veri", "kod-orani.jsonl")
        onceki_boyut = os.path.getsize(kutuk) if os.path.isfile(kutuk) else None
        kos("--kuru", "--sessiz")
        sonraki_boyut = os.path.getsize(kutuk) if os.path.isfile(kutuk) else None
        self.assertEqual(onceki_boyut, sonraki_boyut)


if __name__ == "__main__":
    unittest.main()
