#!/usr/bin/env python3
"""test_fren_hook.py — Ajan fan-out freni PreToolUse hook'unun deterministik testi (İB-54 adım 2; .claude/hooks/pretool-ajan-fren.sh).
Geçici repoda (veri/bronz + .claude/hooks/state) sahte PreToolUse JSON'larıyla koşar: eşik altı 0 · UYARI eşiğinde tek olay · DURDUR eşiğinde
exit 2 + stderr gerekçe · JARVIS_FREN_KAPALI=1 ile geçiş + ASILDI-KAPALI olayı · Agent dışı araç dokunulmaz · oturumlar ayrı sayılır.
Koşum: python3 -m unittest tools/testler/test_fren_hook.py"""
import json, os, shutil, subprocess, tempfile, unittest

HOOK = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ".claude", "hooks", "pretool-ajan-fren.sh")


def kos(repo, tool="Agent", sid="s1", env=None):
    e = dict(os.environ, CLAUDE_PROJECT_DIR=repo, JARVIS_FREN_UYARI="3", JARVIS_FREN_DURDUR="5"); e.update(env or {})
    e.pop("JARVIS_FREN_KAPALI", None) if not (env and "JARVIS_FREN_KAPALI" in env) else None
    return subprocess.run(["bash", HOOK], input=json.dumps({"session_id": sid, "tool_name": tool, "tool_input": {"description": "test ajanı"}}),
                          capture_output=True, text=True, env=e, cwd=repo)


def olaylar(repo):
    p = os.path.join(repo, "veri", "bronz", "fren-olay.jsonl")
    return [json.loads(l) for l in open(p, encoding="utf-8")] if os.path.exists(p) else []


class FrenHookTest(unittest.TestCase):
    def setUp(self):
        self.repo = tempfile.mkdtemp(prefix="fren-"); os.makedirs(os.path.join(self.repo, "veri", "bronz"))

    def tearDown(self):
        shutil.rmtree(self.repo, ignore_errors=True)

    def test_esik_alti_sessiz_uyari_tek_olay_durdur_exit2(self):
        for i in range(1, 3):
            r = kos(self.repo); self.assertEqual(r.returncode, 0, r.stderr); self.assertEqual(olaylar(self.repo), [])
        r = kos(self.repo); self.assertEqual(r.returncode, 0)                       # 3 = UYARI
        self.assertEqual([o["olay"] for o in olaylar(self.repo)], ["UYARI"])
        r = kos(self.repo); self.assertEqual(r.returncode, 0)                       # 4: uyarı tekrar yazılmaz
        self.assertEqual(len(olaylar(self.repo)), 1)
        r = kos(self.repo); self.assertEqual(r.returncode, 2)                       # 5 = DURDUR
        self.assertIn("AJAN FRENİ", r.stderr); self.assertIn("DURDUR eşiği 5", r.stderr); self.assertIn("rejim", r.stderr.lower())
        o = olaylar(self.repo)[-1]; self.assertEqual((o["olay"], o["sayac"], o["esik_durdur"]), ("DURDUR", 5, 5)); self.assertIn("rejim", o)

    def test_kapali_bayragi_gecirir_ve_kaydeder(self):
        for _ in range(4): kos(self.repo)
        r = kos(self.repo, env={"JARVIS_FREN_KAPALI": "1"}); self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(olaylar(self.repo)[-1]["olay"], "ASILDI-KAPALI")

    def test_agent_disi_arac_ve_ayri_oturum(self):
        for _ in range(6): self.assertEqual(kos(self.repo, tool="Bash").returncode, 0)
        self.assertEqual(olaylar(self.repo), [])
        for _ in range(4): kos(self.repo, sid="a")
        self.assertEqual(kos(self.repo, sid="b").returncode, 0)                    # b oturumu 1'de
        self.assertEqual(kos(self.repo, sid="a").returncode, 2)                    # a oturumu 5'te


if __name__ == "__main__":
    unittest.main()
