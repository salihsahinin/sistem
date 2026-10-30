#!/usr/bin/env python3
"""Harness oto-hafıza aynası (Karar 104 M3, masa-17, 2026-09-20 — jarvis AGENTS.md §2 açık-kaynak ilkesi).

Ne yapar: Claude Code'un makine-yerel oto-hafıza dizinini (`~/.claude/projects/<anahtar>/memory/`) depoya
**deterministik** kopyalar: `veri/hafiza-ayna/<anahtar>/…` + `MANIFEST.json` (dosya adı · sha256 · bayt · kaynak mtime;
ad sırasına göre). Kaynak dizin **değişmez** (salt-okur). m.8: kaynakta silinen dosya aynada kalır, manifestte
`durum: kaynakta-yok` damgası alır. Seans kapanışında koşar (seans-kapanis §6h), çıktı commit'e girer.

Kullanım: python3 tools/hafiza-ayna.py [--anahtar=<proje-anahtarı>]... [--kuru] [--json] [--repo <yol>]
Varsayılan anahtar: -Users-HasanSalihSahin-sistem (hükümdeki dizin). Ek anahtar: --anahtar=-Users-HasanSalihSahin-sistem-jarvis
(anahtar `-` ile başladığından `=` zorunlu; argparse ayrı argüman sanır).
Çıkış kodu: 0 = ayna güncel/güncellendi · 2 = kaynak dizin yok · 3 = kaynakta-yok dosya var (bilgi; engel değil).
"""
import argparse, datetime, hashlib, json, os, shutil, sys
import harness_anahtar

VARSAYILAN = [harness_anahtar.kok_anahtar()]  # makineye göre kök anahtarı (Mac: -Users-HasanSalihSahin-sistem · Windows: C--sistem-sistem; 2026-09-22)


def sha256(yol):
    h = hashlib.sha256()
    with open(yol, "rb") as fh:
        for p in iter(lambda: fh.read(1 << 16), b""):
            h.update(p)
    return h.hexdigest()


AYNA_ADI = "-Users-HasanSalihSahin-sistem"  # aynanın KANONİK dizin adı (Karar 104 M3 hükmündeki ad); makine anahtarı değişse de (Windows C--sistem-sistem) tek ayna dizini (2026-09-22)


def ayna(anahtar, repo, kuru, hedef_ad=None):
    kaynak = os.path.expanduser(f"~/.claude/projects/{anahtar}/memory")
    hedef = os.path.join(repo, "veri", "hafiza-ayna", hedef_ad or anahtar)
    if not os.path.isdir(kaynak):
        return {"anahtar": anahtar, "durum": "KAYNAK-YOK", "kaynak": kaynak}
    manifest_yolu = os.path.join(hedef, "MANIFEST.json")
    eski = {}
    if os.path.exists(manifest_yolu):
        try:
            eski = {d["ad"]: d for d in json.load(open(manifest_yolu, encoding="utf-8")).get("dosyalar", [])}
        except (OSError, json.JSONDecodeError, KeyError):
            eski = {}
    dosyalar, yeni, degisen, ayni = [], 0, 0, 0
    kaynaktakiler = sorted(f for f in os.listdir(kaynak) if os.path.isfile(os.path.join(kaynak, f)) and not f.startswith("."))
    for ad in kaynaktakiler:
        ky = os.path.join(kaynak, ad); sh = sha256(ky); st = os.stat(ky)
        kayit = {"ad": ad, "sha256": sh, "bayt": st.st_size, "kaynak_mtime": datetime.datetime.fromtimestamp(st.st_mtime).isoformat(timespec="seconds"), "durum": "ayna"}
        onceki = eski.get(ad)
        if onceki is None:
            yeni += 1
        elif onceki.get("sha256") != sh:
            degisen += 1
        else:
            ayni += 1
        if not kuru:
            os.makedirs(hedef, exist_ok=True); shutil.copyfile(ky, os.path.join(hedef, ad))
        dosyalar.append(kayit)
    kaynakta_yok = []
    for ad, onceki in sorted(eski.items()):
        if ad not in set(kaynaktakiler):
            k = dict(onceki); k["durum"] = "kaynakta-yok"; k.setdefault("kaynakta_yok_tespit", datetime.date.today().isoformat())
            dosyalar.append(k); kaynakta_yok.append(ad)
    dosyalar.sort(key=lambda d: d["ad"])
    m = {"anahtar": anahtar, "kaynak": kaynak, "uretim": datetime.date.today().isoformat(), "karar": "Karar 104 M3 (2026-09-20)",
         "dosya_sayisi": len(kaynaktakiler), "kaynakta_yok": kaynakta_yok, "dosyalar": dosyalar}
    if not kuru:
        os.makedirs(hedef, exist_ok=True)
        with open(manifest_yolu, "w", encoding="utf-8") as fh:
            json.dump(m, fh, ensure_ascii=False, indent=1); fh.write("\n")
    return {"anahtar": anahtar, "durum": "GÜNCELLENDİ" if (yeni or degisen) else "GÜNCEL", "kaynak": kaynak, "hedef": os.path.relpath(hedef, repo),
            "dosya": len(kaynaktakiler), "yeni": yeni, "degisen": degisen, "ayni": ayni, "kaynakta_yok": kaynakta_yok}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--anahtar", action="append", help="proje anahtarı (tekrarlanabilir)")
    ap.add_argument("--kuru", action="store_true", help="yazma; yalnız fark raporu")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    a = ap.parse_args()
    # kök anahtarı hangi makinede olursa olsun kanonik ayna dizinine iner; ek anahtarlar kendi adıyla
    sonuc = [ayna(k, a.repo, a.kuru, AYNA_ADI if k == harness_anahtar.kok_anahtar() else None) for k in (a.anahtar or VARSAYILAN)]
    if a.json:
        print(json.dumps(sonuc, ensure_ascii=False, indent=1))
    else:
        print("HAFIZA-AYNA (Karar 104 M3; kaynak salt-okur, m.8 silme yok):")
        for s in sonuc:
            if s["durum"] == "KAYNAK-YOK":
                print(f"  [YOK ] {s['anahtar']} — {s['kaynak']}"); continue
            print(f"  [{s['durum']}] {s['anahtar']} → {s['hedef']} · dosya {s['dosya']} (yeni {s['yeni']} · değişen {s['degisen']} · aynı {s['ayni']})"
                  + (f" · kaynakta-yok {len(s['kaynakta_yok'])}: {', '.join(s['kaynakta_yok'])}" if s["kaynakta_yok"] else "") + (" · KURU" if a.kuru else ""))
    if any(s["durum"] == "KAYNAK-YOK" for s in sonuc):
        sys.exit(2)
    sys.exit(3 if any(s.get("kaynakta_yok") for s in sonuc) else 0)


if __name__ == "__main__":
    main()
