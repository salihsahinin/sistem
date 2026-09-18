#!/usr/bin/env python3
"""Ad-eşitliği denetimi (Karar 93 EK, Salih 2026-09-10): "Carvis = Jarvis (09-10 öncesi ajan adı)" bilgisi HER bağlam
kombinasyonunda bulunmalı. Üç katmanı sayar:
  K1 her-seans-yüklenen katman: CLAUDE.md · .claude/hooks/session-start.sh · hafıza MEMORY.md · .claude/agents/*.md · ~/sistem/friday/CLAUDE.md
     → her biri "Carvis" adını Jarvis'e bağlayan bir cümle taşımalı (örüntü: 'eski ad Carvis' ∨ 'Carvis = Jarvis' ∨ 'Carvis → Jarvis' ∨ 'Carvis emekli').
  K2 dizin katmanı: içinde "Carvis" geçen dosya barındıran her kök dizinin README.md'si eşitlik bloğu taşımalı ('Carvis = Jarvis').
  K3 canlı-bağlam sızıntısı: canlı dosyalarda (CLAUDE.md, core/, .claude/, KILAVUZ, README, wiki/, tools/, fikir-kutusu) bağlanmamış "Carvis"
     (aynı satırda eşitlik işareti yok) → İHLAL (tarihli dizinler kuyruk/ arsiv/ cc/ raporlar/ muaf, Karar 68 EK).
Kullanım: python3 tools/ad-esitligi-denetim.py [--json]   · çıkış 0 = PASS · 4 = eksik var (kapanış kapısı: FLAG, engel değil).
Deterministik: yalnız dosya içeriği; ağ yok."""
import argparse, json, os, re, sys

J = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = os.path.expanduser("~")
ESIT = re.compile(r"eski ad[ıi]? Carvis|JARVİS FRIDAY CARVIS|Carvis\s*=\s*\*{0,2}Jarvis|Carvis\s*→\s*\*{0,2}Jarvis|Carvis emekli|Carvis\)|eski ad Carvis", re.I)
CARVIS = re.compile(r"Carvis|CARVİS|CARVIS")
K1 = [os.path.join(J, "CLAUDE.md"), os.path.join(J, ".claude", "hooks", "session-start.sh"),
      os.path.join(H, ".claude", "projects", "-Users-HasanSalihSahin-sistem-jarvis", "memory", "MEMORY.md"),
      os.path.join(H, "friday", "CLAUDE.md")]
ad = os.path.join(J, ".claude", "agents")
if os.path.isdir(ad):
    K1 += [os.path.join(ad, f) for f in sorted(os.listdir(ad)) if f.endswith(".md")]
TARIHLI = ("kuyruk", "arsiv", "cc", "raporlar", "ogrenme", "veri", "graf")
CANLI_DIZIN = ("core", ".claude", "wiki", "tools")
CANLI_DOSYA = ("CLAUDE.md", "KILAVUZ.md", "README.md", "fikir-kutusu.md")


def oku(p):
    try:
        return open(p, encoding="utf-8").read()
    except Exception:
        return ""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true"); a = ap.parse_args()
    r = {"K1": [], "K2": [], "K3": []}
    for p in K1:
        t = oku(p); r["K1"].append({"yol": p.replace(H, "~"), "durum": "PASS" if ESIT.search(t) else ("YOK" if not t else "EKSİK")})
    for d in sorted(os.listdir(J)):
        dp = os.path.join(J, d)
        if not os.path.isdir(dp) or d.startswith(".") and d != ".claude" or d in ("node_modules",):
            continue
        var = False
        for dd, ds, fs in os.walk(dp):
            ds[:] = [x for x in ds if x not in (".git", "node_modules", "__pycache__", "worktrees")]
            for f in fs:
                if f.endswith((".md", ".py", ".sh", ".json", ".html", ".txt", ".d2")) and CARVIS.search(oku(os.path.join(dd, f))):
                    var = True; break
            if var: break
        if var:
            # README'siz dizinlerin gezinme eşleniği: core → CLAUDE.md (kanon kapısı) · .claude → kaynak-kodu/README.md · tools → SCRIPTLER.md
            ALT = {"core": os.path.join(J, "CLAUDE.md"), ".claude": os.path.join(J, "kaynak-kodu", "README.md"), "tools": os.path.join(J, "tools", "SCRIPTLER.md")}
            rd = ALT.get(d, os.path.join(dp, "README.md"))
            r["K2"].append({"dizin": d, "esdeger": os.path.relpath(rd, J), "durum": "PASS" if ESIT.search(oku(rd)) else ("README-YOK" if not os.path.exists(rd) else "EKSİK")})
    hedef = [os.path.join(J, f) for f in CANLI_DOSYA]
    for d in CANLI_DIZIN:
        for dd, ds, fs in os.walk(os.path.join(J, d)):
            ds[:] = [x for x in ds if x not in ("__pycache__", "node_modules", "worktrees")]
            hedef += [os.path.join(dd, f) for f in fs if f.endswith((".md", ".py", ".sh", ".json"))]
    kendi = os.path.abspath(__file__)
    for p in hedef:
        if os.path.abspath(p) == kendi:
            continue  # aracın kendi desen satırları
        for i, l in enumerate(oku(p).split("\n"), 1):
            if CARVIS.search(l) and not ESIT.search(l) and not any(x in p for x in ("sozluk.md", "baglam-anahtar-kaydi.md")):
                r["K3"].append({"yol": os.path.relpath(p, J), "satir": i, "metin": l.strip()[:100]})
    eksik = sum(1 for x in r["K1"] if x["durum"] != "PASS") + sum(1 for x in r["K2"] if x["durum"] != "PASS") + len(r["K3"])
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        print("AD-EŞİTLİĞİ DENETİMİ (Karar 93 EK): Carvis = Jarvis her bağlam kombinasyonunda")
        for x in r["K1"]: print(f"  [K1 {x['durum']:6}] {x['yol']}")
        for x in r["K2"]: print(f"  [K2 {x['durum']:6}] {x['dizin']}/README.md")
        for x in r["K3"]: print(f"  [K3 İHLAL ] {x['yol']}:{x['satir']}  {x['metin']}")
        print(f"  → eksik {eksik} ({'PASS' if not eksik else 'FLAG'})")
    sys.exit(4 if eksik else 0)


if __name__ == "__main__":
    main()
