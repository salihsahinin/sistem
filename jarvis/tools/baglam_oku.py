"""Bağlam sırasıyla okuma yardımcısı (Karar 117): `@` ağacına bölünmüş kanon dosyasını yükleme sırasında tek akış
olarak verir. Asıl uygulama Rust `target/release/baglam genislet` (kod/baglam); ikili yoksa aynı kuralın küçük Python
karşılığı koşar: önce dosyanın metni, sonra `@yol` içe aktarmaları yazılış sırasıyla (pre-order), tekrar atlanır,
kökten ≤4 sıçrama, yalnız .md/.txt (Claude Code 2.1.302 ölçümü, raporlar/2026-10-16-baglam-sirasi-import-deneyi.md).
Kullanım: `from baglam_oku import satirlar; satirlar(repo, "core/tuzuk-v0.md")` → [(göreli_yol, satır), ...]."""
import os
import re
import subprocess

_AKTARMA = re.compile(r"(?:^|\s)@(\S+)")


def _ikili(repo):
    kok = os.path.dirname(os.path.abspath(repo))
    for ad in ("baglam.exe", "baglam"):
        p = os.path.join(kok, "target", "release", ad)
        if os.path.isfile(p):
            return p
    return None


def _python_genislet(repo, yol):
    sonuc, gorulen = [], {os.path.normpath(os.path.join(repo, yol))}

    def gez(tam, derinlik):
        try:
            with open(tam, encoding="utf-8", errors="replace") as f:
                metin = f.read().replace("\r\n", "\n")
        except OSError:
            return
        goreli = os.path.relpath(tam, repo).replace("\\", "/")
        sonuc.extend((goreli, s) for s in metin.split("\n"))
        citte = False
        for s in metin.split("\n"):
            if s.lstrip().startswith(("```", "~~~")):
                citte = not citte
                continue
            if citte:
                continue
            for h in _AKTARMA.findall(re.sub(r"`[^`]*`", "", s)):
                hedef = os.path.normpath(os.path.join(os.path.dirname(tam), h))
                if derinlik + 1 > 4 or not hedef.endswith((".md", ".txt")) or not os.path.isfile(hedef) or hedef in gorulen:
                    continue
                gorulen.add(hedef)
                gez(hedef, derinlik + 1)

    gez(os.path.normpath(os.path.join(repo, yol)), 0)
    return sonuc


def satirlar(repo, yol):
    """Genişletilmiş akışın satırları, her biri geldiği dosyanın repo-göreli yoluyla."""
    ikili = _ikili(repo)
    if ikili:
        r = subprocess.run([ikili, "genislet", os.path.join(repo, yol)], capture_output=True, encoding="utf-8", errors="replace")
        if r.returncode in (0, 1) and r.stdout:
            sonuc, kaynak = [], yol
            for s in r.stdout.replace("\r\n", "\n").split("\n"):
                if s.startswith("Contents of ") and s.endswith(":"):
                    kaynak = os.path.relpath(s[len("Contents of "):-1], repo).replace("\\", "/")
                    continue
                sonuc.append((kaynak, s))
            return sonuc
    return _python_genislet(repo, yol)
