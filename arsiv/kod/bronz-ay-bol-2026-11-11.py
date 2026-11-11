"""Tek seferlik bölme betiği (Karar 130 D23, 2026-11-11): jarvis/veri/bronz/<ad>.jsonl -> veri/bronz/<ad>/<YYYY-MM>.jsonl.

Kural jarvis/tools/bronz_ay.py ile aynı (onu içe aktarır). Ay dosyası bölmeden önce yeni hook yazımıyla oluşmuşsa
eski içerik onun önüne konur (sıra: eski kayıtlar, sonra yeni kayıtlar). Satır sayısı toplamı denetlenir; eski dosya
C:/sistem/sistem/arsiv/bronz-tek-dosya-2026-11-11/ altına taşınır (silinmez, m.8).
Koşum: python arsiv/kod/bronz-ay-bol-2026-11-11.py <bronz dizini> [<arşiv dizini>] [--kuru]
"""
import os
import shutil
import sys

sys.path.insert(0, "C:/sistem/sistem/jarvis/tools")
import bronz_ay  # noqa: E402


def say(yol):
    with open(yol, "rb") as f:
        return f.read().count(b"\n")


def main():
    bronz = sys.argv[1]
    arsiv = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("--") else "C:/sistem/sistem/arsiv/bronz-tek-dosya-2026-11-11"
    kuru = "--kuru" in sys.argv
    for ad in sorted(os.listdir(bronz)):
        yol = os.path.join(bronz, ad)
        if not (ad.endswith(".jsonl") and os.path.isfile(yol)):
            continue
        kok = ad[:-6]
        with open(yol, "rb") as f:
            metin = f.read().decode("utf-8")
        if metin and not metin.endswith("\n"):
            metin += "\n"
        once = metin.count("\n")
        gruplar = bronz_ay.aylara_bol(metin, "2026-11")
        aylik = {}
        for ay, parca in gruplar:
            aylik[ay] = aylik.get(ay, "") + parca
        d = os.path.join(bronz, kok)
        yeni_var = {}
        if os.path.isdir(d):
            for n in os.listdir(d):
                yeni_var[n[:-6]] = say(os.path.join(d, n))
        if kuru:
            print(f"{ad}: {once} satır -> " + ", ".join(f"{a}:{p.count(chr(10))}" for a, p in sorted(aylik.items())) + (f" (mevcut yeni: {yeni_var})" if yeni_var else ""))
            continue
        os.makedirs(d, exist_ok=True)
        for ay, parca in sorted(aylik.items()):
            hedef = os.path.join(d, ay + ".jsonl")
            mevcut = b""
            if os.path.exists(hedef):
                with open(hedef, "rb") as f:
                    mevcut = f.read()
            with open(hedef + ".tmp", "wb") as f:
                f.write(parca.encode("utf-8") + mevcut)
            os.replace(hedef + ".tmp", hedef)
        sonra = sum(say(os.path.join(d, n)) for n in os.listdir(d))
        beklenen = once + sum(yeni_var.values())
        if sonra != beklenen:
            sys.exit(f"HATA {ad}: önce {once} + yeni {sum(yeni_var.values())} != sonra {sonra}; eski dosya yerinde bırakıldı")
        os.makedirs(arsiv, exist_ok=True)
        shutil.move(yol, os.path.join(arsiv, ad))
        print(f"{ad}: {once} satır (+{sum(yeni_var.values())} yeni) -> " + ", ".join(f"{n}:{say(os.path.join(d, n))}" for n in sorted(os.listdir(d))))


if __name__ == "__main__":
    main()
