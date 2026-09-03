#!/usr/bin/env python3
"""skill-butce.py testleri (İB-77 S-C; stdlib unittest, subprocess ile AXI arayüzü sınanır).
Koş: python3 -m unittest tools.testler.test_skill_butce

Kapsam: tek-satır description · çok-satırlı (`>`) description · description'sız SKILL.md ·
proje/kullanıcı hazineleri arası symlink gerçek-yol tekilleştirmesi (aynı dosya iki kez sayılmaz) ·
bütçe AŞIMI çıkış kodu 3 · --aday sığar/sığmaz hesabı (minimal küme, en uzundan).
Yan-etki: SALT-OKUR — geçici dizinlerde çalışır, repo'ya yazmaz."""
import json
import os
import subprocess
import sys
import tempfile
import unittest

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARAC = os.path.join(KOK, "tools", "skill-butce.py")

TEK_SATIR_DESC = "A" * 50  # skill-a
COK_SATIR_PARCA_1 = "B" * 20
COK_SATIR_PARCA_2 = "C" * 15  # skill-b description = 20+1(boşluk)+15 = 36 char (katlamalı >)
PAYLASILAN_DESC = "X" * 30  # ev-dizini skill'i, symlink ile de erişilir


def skill_yaz(skills_kok, ad, icerik):
    d = os.path.join(skills_kok, ad)
    os.makedirs(d, exist_ok=True)
    yol = os.path.join(d, "SKILL.md")
    with open(yol, "w", encoding="utf-8") as fh:
        fh.write(icerik)
    return yol


class SkillButceTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = os.path.join(self.tmp.name, "repo")
        self.home = os.path.join(self.tmp.name, "home")
        os.makedirs(self.repo)
        os.makedirs(self.home)
        self.proje_skills = os.path.join(self.repo, ".claude", "skills")
        self.kullanici_skills = os.path.join(self.home, ".claude", "skills")
        os.makedirs(self.proje_skills)
        os.makedirs(self.kullanici_skills)

        # 1) tek-satır description
        skill_yaz(self.proje_skills, "skill-a", (
            "---\nname: skill-a\ndescription: %s\n---\n# skill-a\niçerik\n" % TEK_SATIR_DESC
        ))
        # 2) çok-satırlı (katlamalı >) description
        skill_yaz(self.proje_skills, "skill-b", (
            "---\nname: skill-b\ndescription: >\n  %s\n  %s\n---\n# skill-b\n"
            % (COK_SATIR_PARCA_1, COK_SATIR_PARCA_2)
        ))
        # 3) description'sız SKILL.md
        skill_yaz(self.proje_skills, "skill-c", (
            "---\nname: skill-c\n---\n# skill-c\ndescription yok\n"
        ))
        # 4) kullanıcı-düzeyi paylaşılan skill (gerçek dosya ev dizininde)
        self.paylasilan_yol = skill_yaz(self.kullanici_skills, "shared", (
            "---\nname: shared\ndescription: %s\n---\n# shared\n" % PAYLASILAN_DESC
        ))
        # symlink: proje tarafında aynı dosyaya işaret eden bir skill dizini (tekilleştirme testi)
        sym_dizin = os.path.join(self.proje_skills, "shared-sym")
        os.makedirs(sym_dizin)
        os.symlink(self.paylasilan_yol, os.path.join(sym_dizin, "SKILL.md"))

        self.env = dict(os.environ)
        self.env["HOME"] = self.home

    def tearDown(self):
        self.tmp.cleanup()

    def kos(self, *args):
        return subprocess.run(
            [sys.executable, ARAC, "--repo", self.repo] + list(args),
            capture_output=True, text=True, env=self.env,
        )

    def test_json_sema_ve_char_sayimi(self):
        r = self.kos("--json", "--butce", "100000")
        self.assertEqual(r.returncode, 0, r.stderr)
        d = json.loads(r.stdout)
        for alan in ("arac", "surum", "git_head", "toplam_char", "butce", "kalan", "skill_n", "satirlar"):
            self.assertIn(alan, d)
        adlar = {s["ad"]: s["char"] for s in d["satirlar"]}
        self.assertEqual(adlar["skill-a"], len(TEK_SATIR_DESC))
        self.assertEqual(adlar["skill-b"], len(COK_SATIR_PARCA_1) + 1 + len(COK_SATIR_PARCA_2))
        self.assertEqual(adlar.get("skill-c"), 0)  # description yok → 0 char (frontmatter var, alan yok)

    def test_symlink_tekillestirme(self):
        r = self.kos("--json", "--butce", "100000")
        d = json.loads(r.stdout)
        adlar = [s["ad"] for s in d["satirlar"]]
        # shared VEYA shared-sym görünür ama İKİSİ BİRDEN değil (aynı gerçek dosya)
        self.assertEqual(len(set(adlar) & {"shared", "shared-sym"}), 1)
        # toplam: skill-a + skill-b + paylaşılan(bir kez) — skill-c hariç
        beklenen = len(TEK_SATIR_DESC) + (len(COK_SATIR_PARCA_1) + 1 + len(COK_SATIR_PARCA_2)) + len(PAYLASILAN_DESC)
        self.assertEqual(d["toplam_char"], beklenen)

    def test_butce_asimi_cikis_3(self):
        r = self.kos("--json", "--butce", "1")
        self.assertEqual(r.returncode, 3)
        self.assertIn("AŞIM", r.stderr)
        d = json.loads(r.stdout)
        self.assertGreater(d["toplam_char"], d["butce"])

    def test_aday_sigar(self):
        r = self.kos("--json", "--butce", "100000", "--aday", "5")
        self.assertEqual(r.returncode, 0)
        d = json.loads(r.stdout)
        self.assertIn("SIĞAR", d["aday_hukmu"])

    def test_aday_sigmaz_minimal_kume(self):
        # bütçeyi tam toplam kadar ayarla, aday olarak fazladan char ekle → sığmaz
        toplam = len(TEK_SATIR_DESC) + (len(COK_SATIR_PARCA_1) + 1 + len(COK_SATIR_PARCA_2)) + len(PAYLASILAN_DESC)
        r = self.kos("--json", "--butce", str(toplam), "--aday", "10")
        d = json.loads(r.stdout)
        self.assertIn("SIĞMAZ", d["aday_hukmu"])
        # minimal küme en uzun description'dan (skill-a, 50 char) başlamalı — 10 char fazlalık tek skille kapanır
        self.assertIn("skill-a", d["aday_hukmu"])

    def test_help_ve_json_bayragi(self):
        r = self.kos("--help")
        self.assertEqual(r.returncode, 0)
        self.assertIn("--json", r.stdout)


if __name__ == "__main__":
    unittest.main()
