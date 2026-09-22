#!/usr/bin/env python3
"""Sıcak-katman FIFO sayacı (İB-80; Karar 92 M1 2026-09-10 → Karar 104 M1 2026-09-20 revizyonu).

Karar 104 M1 (masa-17, Salih): eşik **bayt/satır ölçümüne** çevrildi (birincil); madde sayısı **ikincil sigorta**.
Gerekçe: madde-FIFO indeks limitinde sessiz düşüyordu (hafıza Atlas 2/2 hakem §ii — literatürde ölçülmüş arıza);
bayt bütçesi hook'un yüklediği gerçek bağlamı ölçer. Karar 92 M1 "madde birincil" `gecerli-bitis: 2026-09-20`.

Ne yapar: sıcak dosyaların bayt (ve kapsül/CLAUDE için satır) boyutunu ölçer; tavanı aşan dosya için FLAG basar,
arşive inecek EN ESKİ maddeleri (bayt tavanının altına inene dek) listeler ve her biri için kapsüle yapıştırılacak
**kesilme bildirimi** satırı üretir: `kesildi: <madde başı> → arsiv/kapsul-YYYY-MM-DD.md`. TAŞIMAZ — taşıma seans
kapanışında `[damıtma]` commit'iyle elle yapılır (m.8: silme yok, arşiv dosyası + pointer + kapsülde bildirim satırı).

Madde tanımı (deterministik; arşive inme birimi):
  kapsül  → `## Şu an` bölümündeki `- ` satırları          (sigorta K = 8)
  pano    → `## AKTİF` tablosundaki `| K-` satırları         (sigorta K = 5)
  MEMORY  → `MEMORY.md` `- [` indeks satırları (user-* muaf) (sigorta K = 16)
  CLAUDE  → AGENTS.md satırları (madde = satır; kesim yok, "bir satır girer bir çıkar")
Bayt tavanı (birincil): kapsül 8 KB · pano 12 KB · MEMORY 4 KB[?] · AGENTS.md 7 KB. Satır tavanı: kapsül 40 (hook ilk 40
satırı yükler) · AGENTS.md 80. Değerler KILAVUZ boyut bölümünden; MEMORY 4 KB deneysel m.29 (İB-80 bayt revizyonu 5 kapanış sonra).

Kullanım: python3 tools/sicak-katman-fifo.py [--json] [--repo <yol>] [--tarih YYYY-MM-DD]
Çıkış kodu: 0 = aşım yok · 3 = en az bir FLAG (bilgi; engel değil).
"""
import argparse, datetime, json, os, re, sys, unicodedata
import harness_anahtar

TAVAN = {  # ad: (bayt B, satır S ∨ None, madde sigortası K ∨ None)
    "kapsul": (8 * 1024, 40, 8),
    "pano": (12 * 1024, None, 5),
    "memory": (4 * 1024, None, 16),
    "claude": (7 * 1024, 80, None),
}
ARSIV = {"kapsul": "arsiv/kapsul-{t}.md", "pano": "arsiv/kuyruk-arsiv/pano-arsivi-{t}.md",
         "memory": "arsiv/memory-arsivi-{t}.md", "claude": None}
MEM_ANAHTARLAR = (harness_anahtar.kok_anahtar(), harness_anahtar.jarvis_anahtar())  # Karar 101: iki anahtar; ilki canlı (Karar 104 M3); makineye göre türetilir (2026-09-22)


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


def madde_basi(m):
    """Bildirim satırı için maddenin tanınır başı: kalın başlık varsa o, yoksa ilk 60 karakter."""
    k = re.search(r"\*\*(.{3,80}?)\*\*", m)
    return (k.group(1).strip() if k else m.lstrip("-| ").strip()[:60]).rstrip(" :")


def memory_yolu():
    for a in MEM_ANAHTARLAR:
        y = os.path.expanduser(f"~/.claude/projects/{a}/memory/MEMORY.md")
        if os.path.exists(y):
            return y
    return os.path.expanduser(f"~/.claude/projects/{MEM_ANAHTARLAR[0]}/memory/MEMORY.md")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true", help="makine çıktısı")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--tarih", default=datetime.date.today().isoformat(), help="arşiv dosya adı tarihi (deterministik koşum için sabitle)")
    a = ap.parse_args()
    dosyalar = {
        "kapsul": (os.path.join(a.repo, "core", "durum-kapsulu.md"), kapsul_maddeler),
        "pano": (os.path.join(a.repo, "core", "pano.md"), pano_maddeler),
        "memory": (memory_yolu(), memory_maddeler),
        "claude": (os.path.join(a.repo, "AGENTS.md"), claude_maddeler),
    }
    sonuc, flag = [], False
    for ad, (yol, f) in dosyalar.items():
        if not os.path.exists(yol):
            sonuc.append({"ad": ad, "yol": yol, "durum": "YOK"}); continue
        ham = open(yol, encoding="utf-8").read()
        t = unicodedata.normalize("NFC", ham)  # macOS dosyaları NFD gelebilir ("Şu an" başlığı eşleşmez); bayt ham metinden
        maddeler = f(t); n, b, s = len(maddeler), len(ham.encode("utf-8")), len(ham.splitlines())
        B, S, K = TAVAN[ad]
        tetik = []
        if b > B: tetik.append("bayt")
        if S and s > S: tetik.append("satır")
        if K and n > K: tetik.append("madde-sigorta")
        durum = "FLAG" if tetik else "OK"
        flag |= durum == "FLAG"
        # FIFO yönü: kapsül/pano yeni maddeyi ÜSTE yazar → en eski = SON; MEMORY.md indeksi sona EKLER → en eski = BAŞ
        arsive = []
        if tetik and ad != "claude":
            sira = maddeler if ad == "memory" else list(reversed(maddeler))  # en eskiden yeniye
            kalan_b, kalan_n = b, n
            for m in sira:
                if kalan_b <= B and (not K or kalan_n <= K):
                    break
                arsive.append(m); kalan_b -= len(m.encode("utf-8")) + 1; kalan_n -= 1
        arsiv_yolu = (ARSIV[ad] or "").format(t=a.tarih)
        bildirim = [f"kesildi: {madde_basi(m)} → {arsiv_yolu}" for m in arsive]
        sonuc.append({"ad": ad, "yol": os.path.relpath(yol, a.repo) if yol.startswith(a.repo) else yol,
                      "bayt": b, "B": B, "satir": s, "S": S, "madde": n, "K": K, "durum": durum, "tetik": "+".join(tetik),
                      "arsive_inecek": [m[:90] for m in arsive], "bildirim": bildirim, "arsiv": arsiv_yolu})
    if a.json:
        print(json.dumps(sonuc, ensure_ascii=False, indent=1))
    else:
        print("SICAK-KATMAN FIFO (İB-80 · Karar 104 M1: bayt/satır birincil, madde sigorta):")
        for x in sonuc:
            if x.get("durum") == "YOK":
                print(f"  [YOK ] {x['ad']} {x['yol']}"); continue
            satir = f" · satır {x['satir']}/{x['S']}" if x["S"] else ""
            madde = f" · madde {x['madde']}/{x['K']}" if x["K"] else ""
            print(f"  [{x['durum']:4}] {x['ad']:7} bayt {x['bayt']}/{x['B']}{satir}{madde} {('← ' + x['tetik']) if x['tetik'] else ''}")
            for m in x["arsive_inecek"]:
                print(f"          ↓ arşive: {m}")
            for bl in x["bildirim"]:
                print(f"          ✎ kapsüle: {bl}")
    sys.exit(3 if flag else 0)


if __name__ == "__main__":
    main()
