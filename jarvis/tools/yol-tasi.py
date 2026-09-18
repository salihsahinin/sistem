#!/usr/bin/env python3
"""yol-tasi.py — Karar 101 monorepo taşınması için yol-değiştirme aracı (F1 kuru koşum · F3 uygulama).

Ne yapar: verilen dizinlerdeki metin dosyalarında eski mutlak/tilde yolları yeni yollarla değiştirir.
  /Users/HasanSalihSahin/jarvis  → /Users/HasanSalihSahin/sistem/jarvis     (~/jarvis, $HOME/jarvis dahil)
  /Users/HasanSalihSahin/friday  → /Users/HasanSalihSahin/sistem/friday     (~/friday, $HOME/friday dahil)
  -Users-HasanSalihSahin-jarvis  → -Users-HasanSalihSahin-sistem-jarvis     (~/.claude/projects anahtarı)
Ne yapmaz: dokümanları (raporlar/ wiki/ kuyruk/ arsiv/ cc/) değiştirmez — tarihli kayıt AS-OF kalır (m.8).
Friday deny listesindeki `Read(~/jarvis/…)` satırları yalnız BAYRAKLANIR (semantik değişiklik: 20 satır → tek `jarvis/**`, F3'te Edit ile).

Kullanım:
  python3 tools/yol-tasi.py --kuru                       # eski düzen (~/jarvis kökü + ~/friday), rapor + diff dosyası
  python3 tools/yol-tasi.py --uygula --kok ~/sistem      # F2 sonrası yeni düzen: ~/sistem/jarvis + ~/sistem/friday
  --tara <dizin> (tekrarlanabilir) varsayılan listeyi ezer.
Deterministik: aynı girdi → aynı diff; idempotent: zaten /sistem/ içeren satır dokunulmaz. Çıktı: rapor stdout + diff raporlar/2026-09/yol-tasi-<kuru|uygula>-<tarih>.diff
"""
import argparse, datetime, difflib, os, pathlib, re, sys

HOME = os.path.expanduser("~")
CIFTLER = [  # uzun önce (alt-dizi çakışması olmasın)
    (HOME + "/jarvis", HOME + "/sistem/jarvis"),
    ("$HOME/jarvis", "$HOME/sistem/jarvis"),
    ("~/jarvis", "~/sistem/jarvis"),
    (HOME + "/friday", HOME + "/sistem/friday"),
    ("$HOME/friday", "$HOME/sistem/friday"),
    ("~/friday", "~/sistem/friday"),
    ("-Users-HasanSalihSahin-jarvis", "-Users-HasanSalihSahin-sistem-jarvis"),
    ("-Users-HasanSalihSahin-friday", "-Users-HasanSalihSahin-sistem-friday"),
]
UZANTI = {".py", ".sh", ".json", ".md", ".yaml", ".yml", ".toml", ".txt", ".d2", ".tsv"}
BAYRAK = re.compile(r'"Read\(~/jarvis/[^"]*\)"')  # Friday deny satırı


def varsayilan_tara(kok: pathlib.Path, duzen: str):
    if duzen == "eski":   # F1: ~/jarvis kökü + ~/friday ayrı
        j = kok; f = pathlib.Path(HOME) / "friday"
    else:                 # F3: ~/sistem/jarvis + ~/sistem/friday
        j = kok / "jarvis"; f = kok / "friday"
    return [j / "tools", j / ".claude" / "hooks", j / ".claude" / "rules", j / ".claude" / "skills",
            j / ".claude" / "settings.json", j / ".mcp.json",
            f / ".claude", f / "CLAUDE.md", f / "AGENTS.md", f / "tools"]


def dosyalar(yollar):
    for y in yollar:
        if y.is_file():
            yield y
        elif y.is_dir():
            for p in sorted(y.rglob("*")):
                if p.is_file() and p.suffix in UZANTI and "worktrees" not in p.parts and ".git" not in p.parts:
                    yield p


def donustur(satir: str):
    if "/sistem/" in satir or "-sistem-" in satir:
        return satir
    for eski, yeni in CIFTLER:
        satir = satir.replace(eski, yeni)
    return satir


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--kuru", action="store_true"); g.add_argument("--uygula", action="store_true")
    ap.add_argument("--kok", default=os.getcwd()); ap.add_argument("--duzen", choices=["eski", "yeni"], default=None)
    ap.add_argument("--tara", action="append", default=[])
    a = ap.parse_args()
    kok = pathlib.Path(a.kok).expanduser().resolve()
    duzen = a.duzen or ("yeni" if (kok / "jarvis").is_dir() and (kok / "friday").is_dir() else "eski")
    hedefler = [pathlib.Path(t).expanduser() for t in a.tara] or varsayilan_tara(kok, duzen)
    mod = "uygula" if a.uygula else "kuru"
    tarih = datetime.date.today().isoformat()
    rapor, diffler, bayraklar = [], [], []
    for p in dosyalar(hedefler):
        try:
            eski = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        satirlar = eski.splitlines(keepends=True)
        yeni_s = [donustur(s) for s in satirlar]
        for i, s in enumerate(satirlar, 1):
            if BAYRAK.search(s):
                bayraklar.append(f"{p}:{i}")
        n = sum(1 for x, y in zip(satirlar, yeni_s) if x != y)
        if n:
            rapor.append((str(p), n))
            diffler.extend(difflib.unified_diff(satirlar, yeni_s, fromfile=str(p), tofile=str(p) + " (yeni)"))
            if a.uygula:
                p.write_text("".join(yeni_s), encoding="utf-8")
    cikti_dir = (kok / ("jarvis" if duzen == "yeni" else ".") / "raporlar" / "2026-09").resolve()
    cikti_dir.mkdir(parents=True, exist_ok=True)
    diff_yolu = cikti_dir / f"yol-tasi-{mod}-{tarih}.diff"
    diff_yolu.write_text("".join(diffler), encoding="utf-8")
    print(f"yol-tasi {mod} · düzen={duzen} · kök={kok} · tarih={tarih}")
    print(f"{'dosya':70} değişen satır")
    for yol, n in rapor:
        print(f"{yol:70} {n}")
    print(f"toplam: {len(rapor)} dosya · {sum(n for _, n in rapor)} satır · diff → {diff_yolu}")
    if bayraklar:
        print("BAYRAK (elle, F3 Edit): Friday deny satırları → tek `jarvis/**`:")
        for b in bayraklar:
            print("  " + b)
    return 0


if __name__ == "__main__":
    sys.exit(main())
