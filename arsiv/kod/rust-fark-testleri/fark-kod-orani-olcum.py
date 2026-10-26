#!/usr/bin/env python3
"""fark-kod-orani-olcum.py — kod-orani-olcum.py (Python) ↔ kod-orani-olcum (Rust) fark testi.
Aynı kum havuzunun iki taze kopyasında iki uygulamayı koşar; çıkış kodu, stdout, stderr ve yazılan dosyalar karşılaştırılır.
Python betiği kum havuzunun jarvis/tools/ altına kopyalanır (KOK = betik konumu); Rust için CLAUDE_PROJECT_DIR = kum/jarvis."""
import os
import re
import shutil
import subprocess
import sys
import tempfile

DEPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
PY_ARAC = os.path.join(DEPO, "jarvis", "tools", "kod-orani-olcum.py")
RUST_EXE = os.environ.get("RUST_EXE", "C:/tmp/tgt/release/kod-orani-olcum.exe")


def git(cwd, *a):
    subprocess.run(["git", *a], cwd=cwd, stdin=subprocess.DEVNULL, capture_output=True, check=True)


def olay(**k):
    import json
    return json.dumps(k, ensure_ascii=False)


HAREKET = "\n".join([
    "# yorum satırı",
    "",
    olay(ts="2026-09-02T10:00:00", arac="Read", dosya="jarvis/a.md"),
    olay(ts="2026-09-03T10:00:00", arac="Read", dosya="x/b.PY"),
    olay(ts="2026-09-03T11:00:00", arac="Read", dosya="x/c.jsonl"),
    olay(ts="2026-09-03T11:00:00", arac="Read", dosya="x/.gizli"),
    olay(ts="2026-09-03T11:00:00", arac="Read", dosya=""),
    olay(ts="2026-08-01T11:00:00", arac="Read", dosya="eski.md"),
    olay(ts="", arac="Read", dosya="tssiz.md"),
    olay(arac="Read", dosya="tssiz2.md"),
    olay(ts="2026-09-03T12:00:00", arac="Bash", girdi_ozet="Bash⟨cat a/b.md | head -n 5 c/d.sql; tail -f z.log⟩ ek"),
    olay(ts="2026-09-03T12:00:00", arac="Bash", girdi_ozet="sed -n 1,5p foo.sh && awk '{print}' bar.csv x.unknown"),
    olay(ts="2026-09-03T12:00:00", arac="Bash", girdi_ozet="ls -la q.md"),
    olay(ts="2026-09-03T12:00:00", arac="Bash", girdi_ozet="⟩cat zz.md⟨ cat yy.json ⟩"),
    olay(ts="2026-09-03T12:00:00", arac="Bash", girdi_ozet="cat --opt-a.md -x.py nl ü.md"),
    olay(ts="2026-09-03T12:00:00", arac="Bash", girdi_ozet=""),
    olay(ts="2026-09-03T12:00:00", arac="Bash"),
    olay(ts="2026-09-03T12:00:00", arac="Write", dosya="w.md"),
    olay(ts="2026-09-04", arac="Read", dosya="a.b.c/d."),
    olay(ts="üüüüüüüüüüüü", arac="Read", dosya="u.md"),
]) + "\n"


def kum_kur(yol, varyant="normal"):
    j = os.path.join(yol, "jarvis")
    for d in ["tools", "veri/bronz", "veri/gorunum", "arsiv/karantina", "node", "src/alt/derin", "bos-dizin", "ik"]:
        os.makedirs(os.path.join(j, d), exist_ok=True)
    shutil.copy(PY_ARAC, os.path.join(j, "tools", "kod-orani-olcum.py"))

    def yaz(rel, veri):
        p = os.path.join(j, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as f:
            f.write(veri if isinstance(veri, bytes) else veri.encode("utf-8"))
    yaz(".gitignore", "node/\n*.log\n/gizli.md\n")
    yaz("README.md", "# başlık\nikinci\nüçüncü")
    yaz("src/a.py", "print(1)\nprint(2)\n")
    yaz("src/alt/b.SH", "echo\n")
    yaz("src/alt/derin/c.sql", "select 1;\r\nselect 2;\r\n")
    yaz("src/alt/derin/d.json", "{}")
    yaz("src/alt/derin/e.jsonl", "{}\n{}\n{}\n")
    yaz("src/f.csv", "a,b\n1,2\n")
    yaz("src/g.bin", bytes(range(256)) * 3)
    yaz("src/bos.txt", b"")
    yaz("src/ğüşiçö.md", "tr\n")
    yaz("src/.gizli", "x\n")
    yaz("src/.md", "nokta-md\n")
    yaz("src/arc.tar.gz", b"\x1f\x8b\n\n")
    yaz("gizli.md", "ignore\n")
    yaz("node/lib.js", "ignored\n")
    yaz("x.log", "log\n")
    yaz("ik/y.log", "log\n")
    yaz("veri/gorunum/v.md", "gorunum\n")
    yaz("arsiv/karantina/k.md", "kar\n")
    yaz("arsiv/baska.md", "arsiv\n")
    yaz("veri/bronz/öteki.txt", "bronz\n")
    if varyant != "hareketsiz":
        yaz("veri/bronz/hareket-olay.jsonl", HAREKET)
    if varyant == "bozuk":
        yaz("veri/bronz/hareket-olay.jsonl", HAREKET + "{bozuk\n")
    if varyant == "crlf":
        yaz("veri/bronz/hareket-olay.jsonl", HAREKET.replace("\n", "\r\n"))
    if varyant == "dizi":
        yaz("veri/bronz/hareket-olay.jsonl", "[1,2]\n")
    if varyant == "ts-sayi":
        yaz("veri/bronz/hareket-olay.jsonl", olay(ts=5, arac="Read", dosya="a.md") + "\n")
    if varyant == "dosya-sayi":
        yaz("veri/bronz/hareket-olay.jsonl", olay(ts="2026-09-03", arac="Read", dosya=5) + "\n")
    if varyant == "ozet-liste":
        yaz("veri/bronz/hareket-olay.jsonl", olay(ts="2026-09-03", arac="Bash", girdi_ozet=["x"]) + "\n")
    if varyant == "bos-hareket":
        yaz("veri/bronz/hareket-olay.jsonl", "")
    if varyant == "hareket-dizin":
        os.remove(os.path.join(j, "veri/bronz/hareket-olay.jsonl"))
        os.makedirs(os.path.join(j, "veri/bronz/hareket-olay.jsonl"))
    if varyant == "onceki-kutuk":
        yaz("veri/kod-orani.jsonl", '{"onceki": 1}\n')
    if varyant != "gitsiz":
        git(j, "init", "-q")
        git(j, "-c", "user.name=t", "-c", "user.email=t@t", "add", "-A")
        git(j, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "ilk")
        if varyant == "kirli":
            yaz("src/yeni.py", "x\n")
            yaz("src/ignored-by-info.md", "x\n")
            with open(os.path.join(j, ".git", "info", "exclude"), "a") as f:
                f.write("ignored-by-info.md\n")
    if varyant == "bos-repo-yok":
        pass


def agac(kok):
    sonuc = {}
    for d, ds, fs in os.walk(kok):
        if ".git" in ds:
            ds.remove(".git")
        for f in fs:
            p = os.path.join(d, f)
            with open(p, "rb") as fh:
                sonuc[os.path.relpath(p, kok).replace("\\", "/")] = fh.read().replace(b"\r\n", b"\n")
    return sonuc


MASKE = [(re.compile(r"\b[0-9a-f]{7,40}\b"), "<HASH>")]


def maske(metin, kum):
    metin = metin.replace(kum, "<KUM>").replace(kum.replace("\\", "/"), "<KUM>")
    return metin.replace("\r\n", "\n")


def kos(kimlik, kum_ana, argv, varyant, env_ek):
    kum = tempfile.mkdtemp(prefix="kofark-")
    try:
        shutil.copytree(kum_ana, os.path.join(kum, "k"), symlinks=True)
        k = os.path.join(kum, "k")
        j = os.path.join(k, "jarvis")
        env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8", GIT_CONFIG_NOSYSTEM="1")
        env.update(env_ek)
        argv = [a.replace("@KUM@", k).replace("@J@", j) for a in argv]
        if kimlik == "py":
            kmt = [sys.executable, os.path.join(j, "tools", "kod-orani-olcum.py"), *argv]
        else:
            kmt = [RUST_EXE, *argv]
            env["CLAUDE_PROJECT_DIR"] = j
        r = subprocess.run(kmt, cwd=j, env=env, stdin=subprocess.DEVNULL, capture_output=True)
        o = r.stdout.decode("utf-8", "replace")
        e = r.stderr.decode("utf-8", "replace")
        if kimlik == "py" and "Traceback (most recent call last)" in e:
            e = "<TRACEBACK>"
        return r.returncode, maske(o, k), maske(e, k), {a: b.decode("utf-8", "replace").replace(k, "<KUM>") .encode() for a, b in agac(k).items()}
    finally:
        shutil.rmtree(kum, ignore_errors=True)


DURUMLAR = [
    ("varsayilan-dry", "normal", ["--bugun", "2026-09-03", "--kuru"], {}),
    ("yaz", "normal", ["--bugun", "2026-09-03"], {}),
    ("yaz-json", "normal", ["--bugun", "2026-09-03", "--json"], {}),
    ("json-sessiz", "normal", ["--bugun", "2026-09-03", "--json", "--sessiz"], {}),
    ("sessiz", "normal", ["--bugun", "2026-09-03", "--sessiz"], {}),
    ("kuru-json", "normal", ["--bugun", "2026-09-03", "--kuru", "--json"], {}),
    ("pencere-1", "normal", ["--bugun", "2026-09-03", "--pencere-gun", "1", "--kuru"], {}),
    ("pencere-0", "normal", ["--bugun", "2026-09-03", "--pencere-gun", "0", "--kuru"], {}),
    ("pencere-negatif", "normal", ["--bugun", "2026-09-03", "--pencere-gun=-2", "--kuru"], {}),
    ("pencere-buyuk", "normal", ["--bugun", "2026-09-03", "--pencere-gun", "100", "--kuru"], {}),
    ("pencere-tasma", "normal", ["--bugun", "2026-09-03", "--pencere-gun", "99999999999", "--kuru"], {}),
    ("pencere-yil1", "normal", ["--bugun", "2026-09-03", "--pencere-gun", "800000", "--kuru"], {}),
    ("onek", "normal", ["--bug", "2026-09-03", "--pen", "5", "--ku", "--js"], {}),
    ("bugun-bosluklu", "normal", ["--bugun", "", "--kuru", "--json", "--sessiz"], {}),
    ("bugun-bitisik", "normal", ["--bugun", "20260903", "--kuru"], {}),
    ("bugun-hafta1", "normal", ["--bugun", "2026-W36-4", "--kuru"], {}),
    ("bugun-hafta2", "normal", ["--bugun", "2026-W53", "--kuru", "--sessiz"], {}),
    ("bugun-hafta3", "normal", ["--bugun", "2026W361", "--kuru", "--sessiz"], {}),
    ("bugun-hafta4", "normal", ["--bugun", "2026W36", "--kuru", "--sessiz"], {}),
    ("bugun-hafta-kotu", "normal", ["--bugun", "2026-W54", "--kuru"], {}),
    ("bugun-kotu", "normal", ["--bugun", "2026-13-01"], {}),
    ("bugun-kotu2", "normal", ["--bugun", "03.09.2026"], {}),
    ("bugun-yil0", "normal", ["--bugun", "0000-01-01"], {}),
    ("bugun-yil1", "normal", ["--bugun", "0001-01-05", "--kuru"], {}),
    ("bugun-9999", "normal", ["--bugun", "9999-12-31", "--kuru"], {}),
    ("bugun-bugun", "normal", ["--kuru", "--sessiz", "--json"], {}),
    ("hareketsiz", "hareketsiz", ["--bugun", "2026-09-03"], {}),
    ("bozuk-json", "bozuk", ["--bugun", "2026-09-03"], {}),
    ("crlf", "crlf", ["--bugun", "2026-09-03", "--kuru"], {}),
    ("olay-dizi", "dizi", ["--bugun", "2026-09-03"], {}),
    ("ts-sayi", "ts-sayi", ["--bugun", "2026-09-03"], {}),
    ("dosya-sayi", "dosya-sayi", ["--bugun", "2026-09-03"], {}),
    ("ozet-liste", "ozet-liste", ["--bugun", "2026-09-03"], {}),
    ("bos-hareket", "bos-hareket", ["--bugun", "2026-09-03", "--json"], {}),
    ("hareket-dizin", "hareket-dizin", ["--bugun", "2026-09-03"], {}),
    ("onceki-kutuk", "onceki-kutuk", ["--bugun", "2026-09-03", "--json"], {}),
    ("gitsiz", "gitsiz", ["--bugun", "2026-09-03", "--kuru"], {}),
    ("gitsiz-json", "gitsiz", ["--bugun", "2026-09-03", "--kuru", "--json"], {}),
    ("gitsiz-sessiz", "gitsiz", ["--bugun", "2026-09-03", "--kuru", "--sessiz"], {}),
    ("kirli", "kirli", ["--bugun", "2026-09-03", "--kuru", "--json"], {}),
    ("repo-yok", "normal", ["--repo", "@KUM@/yok", "--bugun", "2026-09-03"], {}),
    ("repo-dosya", "normal", ["--repo", "@J@/README.md", "--bugun", "2026-09-03"], {}),
    ("repo-bos", "normal", ["--repo", "@J@/bos-dizin", "--bugun", "2026-09-03"], {}),
    ("repo-alt", "normal", ["--repo", "@J@/src", "--bugun", "2026-09-03"], {}),
    ("repo-kok-goreli", "normal", ["--repo", "..", "--bugun", "2026-09-03", "--kuru"], {}),
    ("repo-baska", "normal", ["--repo=@J@", "--bugun", "2026-09-03"], {}),
    ("yardim", "normal", ["-h"], {}),
    ("yardim-uzun", "normal", ["--help"], {"COLUMNS": "120"}),
    ("yardim-dar", "normal", ["--help"], {"COLUMNS": "40"}),
    ("bilinmeyen", "normal", ["--yok"], {}),
    ("konumsal", "normal", ["fazla"], {}),
    ("pencere-metin", "normal", ["--pencere-gun", "abc"], {}),
    ("pencere-eksik", "normal", ["--pencere-gun"], {}),
    ("belirsiz-onek", "normal", ["--b"], {}),
]


def main():
    if not os.path.isfile(RUST_EXE):
        print("Rust exe yok:", RUST_EXE)
        return 2
    ana = tempfile.mkdtemp(prefix="kofark-ana-")
    farklar = 0
    try:
        havuz = {}
        for ad, varyant, argv, env_ek in DURUMLAR:
            if varyant not in havuz:
                p = os.path.join(ana, varyant)
                os.makedirs(p)
                kum_kur(p, varyant)
                havuz[varyant] = p
            py = kos("py", havuz[varyant], argv, varyant, env_ek)
            rs = kos("rs", havuz[varyant], argv, varyant, env_ek)
            if py == rs:
                continue
            farklar += 1
            print("FARK:", ad, argv)
            for i, ad_ in enumerate(["kod", "stdout", "stderr"]):
                if py[i] != rs[i]:
                    print("  %s py=%r\n  %s rs=%r" % (ad_, py[i], ad_, rs[i]))
            for yol in sorted(set(py[3]) | set(rs[3])):
                if py[3].get(yol) != rs[3].get(yol):
                    print("  dosya", yol, "py=%r rs=%r" % (py[3].get(yol), rs[3].get(yol)))
        print("kod-orani-olcum: %d durum, %d fark" % (len(DURUMLAR), farklar))
        return 1 if farklar else 0
    finally:
        shutil.rmtree(ana, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
