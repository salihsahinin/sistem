#!/usr/bin/env python3
"""harness_anahtar.py — Claude Code harness proje anahtarını makineye göre türetir (2026-09-22, Windows devri; KURULUM §4).

Claude Code `~/.claude/projects/<anahtar>/` dizin adını çalışma dizininin MUTLAK yolundaki alfanümerik olmayan her karakteri `-` yaparak üretir:
  /Users/HasanSalihSahin/sistem/jarvis → -Users-HasanSalihSahin-sistem-jarvis   (Mac)
  C:\\sistem\\sistem\\jarvis              → C--sistem-sistem-jarvis                (Windows)
Sabit Mac anahtarı yerine tools/*.py bu modülü kullanır; Mac'e dönüşte değişiklik gerekmez.

Kural (Karar 104 M3): oto-hafıza `memory/` depo KÖKÜ anahtarındadır (Mac'te -Users-HasanSalihSahin-sistem); oturum transkriptleri (*.jsonl)
oturumun açıldığı dizinin (jarvis/) anahtarındadır. `python3 tools/harness_anahtar.py` iki anahtarı ve dizinlerin varlığını basar.
Deterministik: yalnız yol dizesi; ağ/git yok. Modül adı alt çizgili: `import harness_anahtar` (tools/ dizini script'in sys.path[0]'ıdır).
"""
import os, re

JARVIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KOK = os.path.dirname(JARVIS)
PROJELER = os.path.join(os.path.expanduser("~"), ".claude", "projects")


def anahtar(yol):
    """Mutlak yol → harness proje anahtarı."""
    return re.sub(r"[^A-Za-z0-9]", "-", os.path.abspath(yol))


def jarvis_anahtar():
    return anahtar(JARVIS)


def kok_anahtar():
    return anahtar(KOK)


def proje_dizin(a=None):
    """~/.claude/projects/<anahtar>; varsayılan jarvis anahtarı (transkriptler)."""
    return os.path.join(PROJELER, a or jarvis_anahtar())


def memory_dizin():
    """Oto-hafıza dizini: kök anahtarı; yoksa jarvis anahtarı (eski Mac düzeni)."""
    for a in (kok_anahtar(), jarvis_anahtar()):
        y = os.path.join(PROJELER, a, "memory")
        if os.path.isdir(y):
            return y
    return os.path.join(PROJELER, kok_anahtar(), "memory")


if __name__ == "__main__":
    for ad, a in (("kök", kok_anahtar()), ("jarvis", jarvis_anahtar())):
        d = proje_dizin(a)
        print(f"{ad:7s} {a}  dizin={'VAR' if os.path.isdir(d) else 'YOK'}  memory={'VAR' if os.path.isdir(os.path.join(d, 'memory')) else 'YOK'}")
