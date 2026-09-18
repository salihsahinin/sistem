#!/usr/bin/env python3
"""test_loop_dedektor.py — İB-60 loop dedektörü: imza normalizasyonu + sentetik silver'da k_W/N eşiği + skill penceresi + determinizm.
Koşum: python3 -m unittest tools/testler/test_loop_dedektor.py"""
import hashlib, importlib.util, os, shutil, sqlite3, subprocess, sys, tempfile, unittest

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARAC = os.path.join(KOK, "tools", "loop-dedektor.py")


def modul():
    spec = importlib.util.spec_from_file_location("loop_dedektor", ARAC); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


class ImzaTest(unittest.TestCase):
    def test_bash_zinciri(self):
        m = modul()
        self.assertEqual(m.bash_imza("hat koş ⟨cd ~/sistem/jarvis && python3 tools/katman-hatti.py > x.log; git add a b && git commit -q -F -⟩"), "Bash:py:katman-hatti+git:add+git:commit")
        self.assertEqual(m.bash_imza("inline ⟨python3 - <<'EOF'\nprint(1)\nEOF\ngit status⟩"), "Bash:py:inline+git:status")
        self.assertEqual(m.bash_imza("⟨sqlite3 veri/baglam.sqlite \"select 1\"⟩"), "Bash:sqlite3")

    def test_yol_sinifi(self):
        m = modul()
        self.assertEqual(m.imza("Read", "core/durum-kapsulu.md [bütün]", "core/durum-kapsulu.md"), "Read:core/durum-kapsulu.md")
        self.assertEqual(m.imza("Edit", None, ".claude/skills/x/SKILL.md"), "Edit:.claude/skills")
        self.assertEqual(m.imza("Read", "/private/tmp/a.out", None), "Read:dış")
        self.assertEqual(m.imza("Agent", "[general-purpose] iş", None), "Agent:general-purpose")
        self.assertEqual(m.imza("Skill", "seans-acilis", None), "Skill:seans-acilis")


class SentetikTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="loop-ded-"); os.makedirs(os.path.join(self.tmp, "veri", "gorunum")); os.makedirs(os.path.join(self.tmp, "kuyruk"))
        self.db = os.path.join(self.tmp, "veri", "baglam.sqlite"); con = sqlite3.connect(self.db)
        con.execute("CREATE TABLE hareket (hareket_id TEXT PRIMARY KEY, oturum_id TEXT, sira INTEGER, arac TEXT, hedef TEXT, dosya TEXT, tarih_tr TEXT)")
        rows = []
        def ekle(oid, dizi, tarih="2026-08-20"):
            for i, (arac, hedef, dosya) in enumerate(dizi):
                rows.append(("%s-%d" % (oid, i), oid, i, arac, hedef, dosya, tarih))
        A = [("Read", "tools/a.py", "tools/a.py"), ("Edit", "tools/a.py", "tools/a.py"), ("Bash", "t ⟨python3 -m unittest x⟩", None)]  # 3-gram, 3 oturum → ADAY
        for oid in ("o1", "o2"):
            ekle(oid, A + [("Write", "raporlar/r.md", "raporlar/r.md")])
        ekle("o3", A + [("Bash", "⟨ls⟩", None)])  # 4-gram yalnız 2 oturumda → 3-gram A en uzun ADAY (kapsanan=0)
        B = [("Bash", "⟨sqlite3 db⟩", None), ("Write", "cc/x/y.md", "cc/x/y.md")]  # 2 oturum → ESIK-ALTI
        ekle("o4", B); ekle("o5", B)
        R = [("Skill", "seans-acilis", None), ("Read", "core/durum-kapsulu.md", "core/durum-kapsulu.md"), ("Read", "core/pano.md", "core/pano.md")]  # skill penceresi
        for oid in ("o6", "o7", "o8"):
            ekle(oid, R)
        ekle("o9", A, tarih="2026-01-01")  # pencere dışı (90 gün)
        con.executemany("INSERT INTO hareket VALUES (?,?,?,?,?,?,?)", rows); con.commit(); con.close()
        open(os.path.join(self.tmp, "kuyruk", "skill-fikir-kutusu.md"), "w", encoding="utf-8").write("# kutu\n\n## m.43 sayaçları\n- eski satır\n")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def kos(self, *ek):
        return subprocess.run([sys.executable, ARAC, "--repo", self.tmp, "--bugun", "2026-08-29", "--sessiz", *ek], capture_output=True, text=True)

    def oku(self):
        import csv
        return list(csv.DictReader(open(os.path.join(self.tmp, "veri", "gorunum", "v_loop_aday.csv"), encoding="utf-8")))

    def test_esik_ve_pencere(self):
        r = self.kos(); self.assertEqual(r.returncode, 0, r.stderr)
        rows = self.oku(); byimza = {x["imza"]: x for x in rows}
        a3 = byimza["Read:tools → Edit:tools → Bash:py:inline"]
        self.assertEqual((a3["durum"], a3["k_W"], a3["skill_ici"], a3["kapsanan"]), ("ADAY", "3", "0", "0"))  # o9 pencere dışı → k_W 3, 4 değil
        b = byimza["Bash:sqlite3 → Write:cc/x"]; self.assertEqual((b["durum"], b["k_W"]), ("ESIK-ALTI", "2"))
        r2 = byimza["Read:core/durum-kapsulu.md → Read:core/pano.md"]; self.assertEqual((r2["durum"], r2["skill_ici"]), ("ADAY", "1"))
        a2 = byimza["Read:tools → Edit:tools"]; self.assertEqual(a2["kapsanan"], "1")  # 3-gram ADAY'ın alt-dizisi, aynı k_W

    def test_kutu_idempotent_ve_yalniz_n3(self):
        self.kos("--kutu"); self.kos("--kutu")
        s = open(os.path.join(self.tmp, "kuyruk", "skill-fikir-kutusu.md"), encoding="utf-8").read()
        self.assertEqual(s.count("loop-aday"), 1, s)  # 3-gram bir kez; 2-gram'lar ve skill-içi girmez
        self.assertIn("Read:tools → Edit:tools → Bash:py:inline", s); self.assertNotIn("durum-kapsulu", s)

    def test_determinizm(self):
        self.kos(); p = os.path.join(self.tmp, "veri", "gorunum", "v_loop_aday.csv"); s1 = hashlib.sha1(open(p, "rb").read()).hexdigest()
        self.kos(); s2 = hashlib.sha1(open(p, "rb").read()).hexdigest(); self.assertEqual(s1, s2)


if __name__ == "__main__":
    unittest.main()
