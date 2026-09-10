#!/usr/bin/env python3
"""Sıcak-katman FIFO sayacı (İB-80, Karar 92 M1 — Salih hükmü 2026-09-10: "konu sayısı asıl öncelik; bayt sonra revize").

Ne yapar: sıcak dosyaların MADDE sayısını (birincil tetik) ve bayt boyutunu (ikincil sigorta) sayar; tavanı aşan
dosya için FLAG basar ve arşive inecek EN ESKİ maddeleri listeler. TAŞIMAZ — taşıma seans kapanışında `[damıtma]`
commit'iyle elle yapılır (m.8: silme yok, arşiv `arsiv/kapsul-YYYY-MM-DD.md` ∨ ilgili arşiv dosyası).

Madde tanımı (deterministik):
  kapsül  → `## Şu an` bölümündeki `- ` satırları                       (K = 8)
  pano    → `## AKTİF` tablosundaki `| K-` satırları                      (K = 5)
  MEMORY  → `MEMORY.md` içindeki `- [` indeks satırları                   (K = 16)
  CLAUDE  → CLAUDE.md satır sayısı                                        (K = 80; "bir satır girer bir çıkar")
Bayt sigortası: KILAVUZ boyut bölümü (kapsül 8 KB · pano 12 KB · CLAUDE.md 7 KB · MEMORY 4 KB[?]) — Salih 09-10: bayt eşikleri
"daha sonra bayta uygun revize edilecek"; bu değerler geçici, m.29.

Kullanım: python3 tools/sicak-katman-fifo.py [--json] [--repo <yol>]
Çıkış kodu: 0 = aşım yok · 3 = en az bir FLAG (bilgi; engel değil).
"""
import argparse, json, os, re, sys, unicodedata

TAVAN = {  # ad: (madde K, bayt)
    "kapsul": (8, 8 * 1024),
    "pano": (5, 12 * 1024),
    "memory": (16, 4 * 1024),
    "claude": (80, 7 * 1024),
}


def kapsul_maddeler(t):
    b = re.search(r"^## Şu an\n(.*?)(?=^## |\Z)", t, flags=re.S | re.M)
    return [l for l in (b.group(1).splitlines() if b else []) if l.startswith("- ")]


def pano_maddeler(t):
    b = re.search(r"^## AKTİF\n(.*?)(?=^## |\Z)", t, flags=re.S | re.M)
    return [l for l in (b.group(1).splitlines() if b else []) if l.startswith("| K-")]


def memory_maddeler(t):
    # kullanıcı-olgusu satırları (user-*.md) FIFO'dan MUAF: gündem değil, kimlik bilgisi (Karar 92 M1 uygulaması 09-10)
    return [l for l in t.splitlines() if l.startswith("- [") and "](user-" not in l]


def claude_maddeler(t):
    return t.splitlines()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true", help="makine çıktısı")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    a = ap.parse_args()
    mem = os.path.expanduser("~/.claude/projects/-Users-HasanSalihSahin-jarvis/memory/MEMORY.md")
    dosyalar = {
        "kapsul": (os.path.join(a.repo, "core", "durum-kapsulu.md"), kapsul_maddeler),
        "pano": (os.path.join(a.repo, "core", "pano.md"), pano_maddeler),
        "memory": (mem, memory_maddeler),
        "claude": (os.path.join(a.repo, "CLAUDE.md"), claude_maddeler),
    }
    sonuc, flag = [], False
    for ad, (yol, f) in dosyalar.items():
        if not os.path.exists(yol):
            sonuc.append({"ad": ad, "yol": yol, "durum": "YOK"}); continue
        ham = open(yol, encoding="utf-8").read()
        t = unicodedata.normalize("NFC", ham)  # macOS dosyaları NFD gelebilir ("Şu an" başlığı eşleşmez); bayt ham metinden
        maddeler = f(t); n, b = len(maddeler), len(ham.encode("utf-8"))
        K, B = TAVAN[ad]
        tasan_madde = max(0, n - K)
        durum = "FLAG" if (tasan_madde > 0 or b > B) else "OK"
        flag |= durum == "FLAG"
        # FIFO yönü: kapsül/pano yeni maddeyi ÜSTE yazar → en eski = SON; MEMORY.md indeksi sona EKLER → en eski = BAŞ
        if not tasan_madde or ad == "claude":
            arsive = []
        elif ad == "memory":
            arsive = maddeler[:tasan_madde]
        else:
            arsive = maddeler[-tasan_madde:]
        sonuc.append({"ad": ad, "yol": os.path.relpath(yol, a.repo) if yol.startswith(a.repo) else yol,
                      "madde": n, "K": K, "bayt": b, "B": B, "durum": durum,
                      "tetik": ("madde" if tasan_madde else "") + ("+bayt" if b > B else ""),
                      "arsive_inecek": [m[:90] for m in arsive]})
    if a.json:
        print(json.dumps(sonuc, ensure_ascii=False, indent=1))
    else:
        print("SICAK-KATMAN FIFO (İB-80; K madde birincil, bayt sigorta):")
        for s in sonuc:
            if s.get("durum") == "YOK":
                print(f"  [YOK ] {s['ad']} {s['yol']}"); continue
            print(f"  [{s['durum']:4}] {s['ad']:7} madde {s['madde']}/{s['K']} · bayt {s['bayt']}/{s['B']} {('← ' + s['tetik']) if s['tetik'] else ''}")
            for m in s["arsive_inecek"]:
                print(f"          ↓ arşive: {m}")
    sys.exit(3 if flag else 0)


if __name__ == "__main__":
    main()
