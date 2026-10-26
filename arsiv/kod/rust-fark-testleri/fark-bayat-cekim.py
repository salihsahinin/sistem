#!/usr/bin/env python3
"""fark-bayat-cekim.py — bayat-cekim.py (Python) ile Rust ikilisinin çıktı/dosya farkını sınar.
Her durum için aynı sandbox'ın iki taze kopyası: biri Python, biri Rust ile koşar; çıkış kodu, stdout, stderr
ve yazılan dosyalar (CRLF→LF, zaman damgaları maskeli) karşılaştırılır."""
import os, re, shutil, subprocess, sys, tempfile

KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
PY = os.path.join(KOK, "jarvis", "tools", "bayat-cekim.py")
if not os.path.exists(PY):
    PY = os.path.join(KOK, "arsiv", "kod", "python", "tools", "bayat-cekim.py")
RUST = os.environ.get("RUST_EXE", "C:/tmp/tgt/release/bayat-cekim.exe")

CSV = ('dosya,yas_gun,en_yeni_damga,esik_gun\n'
       'core/b.md,120,2026-01-01,90\n'
       '# yorum.md,500,x,90\n'
       'core/a.md,120,2026-01-02,90\n'
       'core/c.md,300,2025-05-05,90\n'
       '"core/q,uote.md",200,"2025-06-06",90\n'
       '\n'
       'core/kisa.md\n'
       ',50,bos,90\n'
       'core/d.md,,2026-02-02,90,fazla\n')
DENETIM = "\n".join([
    '{"kosum_id":"k1","denetim":"D1","dosya":"core/a.md","satir":1,"kalip":"eski","seviye":"warn"}',
    'bozuk json',
    '',
    '{"kosum_id":"k2","denetim":"D1","dosya":"core/a.md","satir":7,"kalip":"As of 2010","seviye":"error"}',
    '{"kosum_id":"k2","denetim":"D1","dosya":"core/b.md","satir":3,"kalip":"şimdiki","seviye":"warn"}',
    '{"kosum_id":"k2","denetim":"D2","dosya":"core/c.md","satir":3,"kalip":"x","seviye":"warn"}',
    '{"kosum_id":"k2","denetim":"D1","dosya":"core/zz.md","satir":3,"kalip":"y","seviye":"warn"}',
] + ['{"kosum_id":"k2","denetim":"D1","dosya":"core/c.md","satir":%d,"kalip":"p%d","seviye":"info"}' % (i, i) for i in range(10)]) + "\n"


def kur(dizin, kipler):
    os.makedirs(os.path.join(dizin, "veri", "gorunum"))
    os.makedirs(os.path.join(dizin, "veri", "bronz"))
    os.makedirs(os.path.join(dizin, "core"))
    for f in ("a", "b", "c", "d"):
        open(os.path.join(dizin, "core", f + ".md"), "w").write("x\n")
    if "csv" in kipler:
        open(os.path.join(dizin, "veri", "gorunum", "v_bayat_aday.csv"), "w", encoding="utf-8", newline="").write(CSV)
    if "crlf" in kipler:
        open(os.path.join(dizin, "veri", "gorunum", "v_bayat_aday.csv"), "w", encoding="utf-8", newline="").write(CSV.replace("\n", "\r\n"))
    if "bos" in kipler:
        open(os.path.join(dizin, "veri", "gorunum", "v_bayat_aday.csv"), "w").write("")
    if "bozukyas" in kipler:
        open(os.path.join(dizin, "veri", "gorunum", "v_bayat_aday.csv"), "w").write("dosya,yas_gun\na.md,abc\n")
    if "tirnaksatir" in kipler:
        open(os.path.join(dizin, "veri", "gorunum", "v_bayat_aday.csv"), "w", encoding="utf-8").write('dosya,yas_gun,en_yeni_damga\n"a\nb.md",5,"x ""y"" z"\nc.md,7,t\n')
    if "denetim" in kipler:
        open(os.path.join(dizin, "veri", "anakronizm-denetim.jsonl"), "w", encoding="utf-8", newline="").write(DENETIM)
    if "olay" in kipler:
        open(os.path.join(dizin, "veri", "bronz", "cekim-olay.jsonl"), "w", encoding="utf-8", newline="").write(
            '{"cekim_tarihi":"2026-09-01"}\n{"cekim_tarihi":"2026-09-01T10:00"}\nbozuk\n{"cekim_tarihi":null}\n{"cekim_tarihi":"2026-09-02"}\n')
    if "olcum_yok" not in kipler:
        open(os.path.join(dizin, "veri", "katman-olcum.jsonl"), "w", newline="").write('{"eski":1}\n')
    if "git" in kipler:
        env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t",
                   GIT_AUTHOR_DATE="2026-01-01T00:00:00", GIT_COMMITTER_DATE="2026-01-01T00:00:00")
        for c in (["init", "-q"], ["add", "-A"], ["commit", "-q", "-m", "i"]):
            subprocess.run(["git"] + c, cwd=dizin, env=env, stdin=subprocess.DEVNULL, capture_output=True)


MASKE = [(re.compile(r'"ts": "[^"]*"'), '"ts": "TS"'), (re.compile(r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d[0-9.:+]*'), 'TS')]


def norm(s):
    s = s.replace("\r\n", "\n")
    for r, t in MASKE:
        s = r.sub(t, s)
    return s


def calistir(komut, dizin, args):
    a = [x.replace("{R}", dizin) for x in args]
    p = subprocess.run(komut + a, cwd=dizin, capture_output=True, stdin=subprocess.DEVNULL, env=dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1"))
    d = {}
    for kd, _, fs in os.walk(dizin):
        if ".git" in kd.split(os.sep):
            continue
        for f in fs:
            y = os.path.join(kd, f)
            d[os.path.relpath(y, dizin)] = norm(open(y, "rb").read().decode("utf-8", "replace"))
    return p.returncode, norm(p.stdout.decode("utf-8", "replace")).replace(dizin.replace("\\", "/"), "R").replace(dizin, "R"), \
        norm(p.stderr.decode("utf-8", "replace")).replace(dizin, "R"), d


DURUMLAR = [
    ("liste varsayılan", {"csv", "git", "denetim"}, ["--repo", "{R}"]),
    ("liste --liste --n 5", {"csv", "git", "denetim"}, ["--repo", "{R}", "--liste", "--n", "5", "--bugun", "2026-09-01"]),
    ("liste n=0", {"csv", "git", "denetim"}, ["--repo", "{R}", "--n", "0", "--bugun", "2026-09-01"]),
    ("liste n=-1", {"csv", "git", "denetim"}, ["--repo", "{R}", "--n", "-1", "--bugun", "2026-09-01"]),
    ("liste n=100 crlf", {"crlf", "git", "denetim"}, ["--repo", "{R}", "--n", "100", "--bugun", "2026-09-01"]),
    ("liste git yok csv yok", {"olcum_yok"}, ["--repo", "{R}", "--bugun", "2026-09-01"]),
    ("liste boş csv", {"bos", "git"}, ["--repo", "{R}", "--bugun", "2026-09-01"]),
    ("liste bozuk yas", {"bozukyas", "git"}, ["--repo", "{R}", "--bugun", "2026-09-01"]),
    ("liste tırnaklı satır", {"tirnaksatir", "git"}, ["--repo", "{R}", "--n", "9", "--bugun", "2026-09-01"]),
    ("olcum", {"csv", "git", "olay"}, ["--repo", "{R}", "--olcum", "--bugun", "2026-09-01"]),
    ("olcum WARN", {"csv", "git", "olay"}, ["--repo", "{R}", "--olcum", "--bugun", "2026-09-05", "--n", "2"]),
    ("olcum + liste", {"csv", "git", "olay", "denetim"}, ["--repo", "{R}", "--olcum", "--liste", "--bugun", "2026-09-02"]),
    ("olcum kuyruk boş", {"git"}, ["--repo", "{R}", "--olcum", "--bugun", "2026-09-02"]),
    ("olcum katman-olcum dizini yok", {"csv", "git", "olcum_yok"}, ["--repo", "{R}", "--olcum"]),
    ("kaydet teyit", {"csv", "git"}, ["--repo", "{R}", "--kaydet", "core/a.md", "--sonuc", "teyit", "--bugun", "2026-09-01"]),
    ("kaydet not+kaynak", {"csv", "git"}, ["--repo", "{R}", "--kaydet", "core/a.md", "--sonuc", "guncellendi", "--kaynak-tarihi", "2026-08-30", "--not", "ğüş \"tırnak\" \\ ü", "--bugun", "2026-09-01"]),
    ("kaydet kaynak boş", {"csv", "git"}, ["--repo", "{R}", "--kaydet", "core/a.md", "--sonuc", "sonlandi", "--kaynak-tarihi", "", "--bugun", "2026-09-01"]),
    ("kaydet mutlak yol", {"csv", "git"}, ["--repo", "{R}", "--kaydet", "{R}/core/b.md", "--sonuc", "teyit", "--bugun", "2026-09-01"]),
    ("kaydet sonuç yok", {"csv", "git"}, ["--repo", "{R}", "--kaydet", "core/a.md"]),
    ("kaydet dosya yok", {"csv", "git"}, ["--repo", "{R}", "--kaydet", "core/yok.md", "--sonuc", "teyit"]),
    ("kaydet kötü kaynak tarihi", {"csv", "git"}, ["--repo", "{R}", "--kaydet", "core/a.md", "--sonuc", "teyit", "--kaynak-tarihi", "31.12.2026"]),
    ("kaydet hafta tarihi", {"csv", "git"}, ["--repo", "{R}", "--kaydet", "core/a.md", "--sonuc", "teyit", "--kaynak-tarihi", "2026-W10-3", "--bugun", "20260901"]),
    ("kaydet git yok", {"csv"}, ["--repo", "{R}", "--kaydet", "core/a.md", "--sonuc", "teyit", "--bugun", "2026-09-01"]),
    ("kaydet olay ekleme", {"csv", "git", "olay"}, ["--repo", "{R}", "--kaydet", "core/c.md", "--sonuc", "teyit", "--bugun", "2026-09-01"]),
    ("kaydet hatalı sonuc", {"csv", "git"}, ["--repo", "{R}", "--kaydet", "core/a.md", "--sonuc", "foo"]),
    ("bugun hatalı", {"csv", "git"}, ["--repo", "{R}", "--bugun", "dün"]),
    ("n hatalı", {"csv", "git"}, ["--repo", "{R}", "--n", "x"]),
    ("bilinmeyen arg", {"csv", "git"}, ["--repo", "{R}", "--foo"]),
    ("yardım", {"csv"}, ["-h"]),
    ("önek kısaltma", {"csv", "git"}, ["--repo", "{R}", "--ol", "--bu", "2026-09-01"]),
    ("not kısaltma kaydet", {"csv", "git"}, ["--repo", "{R}", "--kaydet", "core/a.md", "--sonuc", "teyit", "--no", "kısa", "--bugun", "2026-09-01"]),
]


def main():
    fark = 0
    for ad, kipler, args in DURUMLAR:
        sonuc = []
        for komut in (["python", PY], [RUST]):
            d = tempfile.mkdtemp(prefix="bc-")
            d = os.path.join(d, "r")
            os.makedirs(d)
            kur(d, kipler)
            sonuc.append(calistir(komut, d, args))
            shutil.rmtree(os.path.dirname(d), ignore_errors=True)
        p, r = sonuc
        # git yok durumunda aynı dizin adı farkı doğmaz (maske R)
        if p != r:
            fark += 1
            print("FARK:", ad)
            for i, ne in enumerate(("kod", "stdout", "stderr", "dosyalar")):
                if p[i] != r[i]:
                    print("  ", ne, "\n   py :", repr(p[i])[:600], "\n   rs :", repr(r[i])[:600])
    print("bayat-cekim: %d durum, %d fark" % (len(DURUMLAR), fark))
    return 1 if fark else 0


if __name__ == "__main__":
    sys.exit(main())
