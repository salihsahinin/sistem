#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Obsidian bağlantı haritası üretici (Karar 72 EK, Salih seçimi A — 2026-08-27).

Ne yapar: silver'daki HAZIR pointer ayıklamasını okur (referans.ref_turu =
'dosya_pointer' ∧ hedef_var=1) → küme (üst dizin) başına graf/obsidian-harita-
<kume>.md harita notu + graf/obsidian-harita.md indeksi yazar. Harita
notlarındaki md-linkler Obsidian graf görünümünde kenar sayılır; böylece
backtick yol-pointer'larının görünmez kütlesi grafiğe girer ve kanon dosya
GÖVDELERİNE DOKUNULMAZ (m.8 / İB-53 "araç bize uyar").

Neden silver'dan: tek-kaynak determinizm — dosya gövdesi yeniden regexlenmez
(pointer-graf.py ile aynı desen); aynı silver → aynı çıktı, damga uretim
tablosundan (zaman fonksiyonu yok).

Kapsam kuralları (deterministik, gerekçeleriyle):
- kaynak da hedef de .md olmalı (Obsidian düğümü = not; .py/.jsonl hedefleri
  varsayılan ayarda düğüm değildir).
- Obsidian'ın indekslemediği dizinler (.obsidian/app.json userIgnoreFilters;
  dosya okunamazsa gömülü VARSAYILAN liste) kaynak ve hedef olarak DIŞARIDA.
- nokta-dizin altındaki dosyalar (.claude/ vb.) DIŞARIDA — Obsidian gizli
  klasörleri hiç indekslemez, linkleri vault'ta ölü olur (kapı: kaynak-kodu/).
- yolunda 'arsiv' bölütü geçen dosya KAYNAK olamaz (bayat kaydın kenarları
  canlı topolojiyi bulandırır); HEDEF olabilir (canlı dosyadan arşive işaret
  gerçek bir kenardır).
- graf/obsidian-harita* üretim dışı ve kaynak dışıdır (kendine besleme yok;
  gitignore'lu türev oldukları için git-izli tarayan silver'a zaten girmezler).
- öz-döngü atılır; (kaynak, hedef) çifti tekilleştirilir.

Çıktı gitignore'lu TÜREVDİR (veri/baglam.sqlite emsali): her katman-hatti
koşumunda yeniden üretilir, elle düzenlenmez, commit'lenmez.

Kullanım: python3 tools/obsidian-harita.py [--db veri/baglam.sqlite]
          [--cikti-dizin graf] [--sessiz]
"""

import argparse
import json
import os
import sqlite3
import sys

VARSAYILAN_IGNORE = ["veri/bronz/", "veri/gorunum/", "veri/parquet/", "arsiv/claude-izler/"]
HARITA_ONEK = "obsidian-harita"


def ignore_filtreleri(repo_kok):
    """Obsidian'ın indekslemediği dizinler — app.json'dan; okunamazsa gömülü varsayılan."""
    yol = os.path.join(repo_kok, ".obsidian", "app.json")
    try:
        with open(yol, encoding="utf-8") as fh:
            filtreler = json.load(fh).get("userIgnoreFilters", [])
        return [f if f.endswith("/") else f + "/" for f in filtreler] or VARSAYILAN_IGNORE
    except (OSError, json.JSONDecodeError):
        return VARSAYILAN_IGNORE


def kapsamda(yol, filtreler):
    if not yol.endswith(".md") or any(yol.startswith(f) for f in filtreler):
        return False
    return not any(b.startswith(".") for b in yol.split("/")[:-1])  # nokta-dizin: Obsidian indekslemez


def kume_adi(yol):
    return yol.split("/")[0] if "/" in yol else "kok"


def md_link(yol):
    """graf/ içinden depo-köküne göreli md-link; boşluk/parantezli yol açılı ayraçla."""
    hedef = "../" + yol
    if any(c in hedef for c in " ()"):
        hedef = "<%s>" % hedef
    return "[%s](%s)" % (yol, hedef)


def main():
    ap = argparse.ArgumentParser(description="Obsidian bağlantı haritası üretici (silver → graf/obsidian-harita*.md)")
    ap.add_argument("--db", default="veri/baglam.sqlite")
    ap.add_argument("--cikti-dizin", default="graf")
    ap.add_argument("--sessiz", action="store_true")
    a = ap.parse_args()

    repo_kok = os.getcwd()
    filtreler = ignore_filtreleri(repo_kok)

    con = sqlite3.connect(a.db)
    cur = con.cursor()
    damga = cur.execute("SELECT uretim_zamani, substr(git_head_sha,1,7) FROM uretim LIMIT 1").fetchone() or ("-", "-")

    kenarlar = set()
    atilan = {"md_disi": 0, "ignore": 0, "arsiv_kaynak": 0, "oz_dongu": 0, "harita": 0}
    for kaynak, hedef in cur.execute(
        "SELECT DISTINCT k.dosya_id, r.hedef_yol FROM referans r "
        "JOIN kayit k ON k.kayit_id = r.kayit_id "
        "WHERE r.ref_turu='dosya_pointer' AND r.hedef_var=1"
    ):
        if HARITA_ONEK in kaynak or HARITA_ONEK in hedef:
            atilan["harita"] += 1
            continue
        if not (kaynak.endswith(".md") and hedef.endswith(".md")):
            atilan["md_disi"] += 1
            continue
        if not (kapsamda(kaynak, filtreler) and kapsamda(hedef, filtreler)):
            atilan["ignore"] += 1
            continue
        if "arsiv" in kaynak.split("/")[:-1]:
            atilan["arsiv_kaynak"] += 1
            continue
        if kaynak == hedef:
            atilan["oz_dongu"] += 1
            continue
        kenarlar.add((kaynak, hedef))
    con.close()

    kumeler = {}
    for kaynak, hedef in sorted(kenarlar):
        kumeler.setdefault(kume_adi(kaynak), {}).setdefault(kaynak, []).append(hedef)

    os.makedirs(a.cikti_dizin, exist_ok=True)
    baslik_damga = ("*TÜREV — elle düzenlenmez, commit'lenmez (gitignore). Üretici: `tools/obsidian-harita.py` "
                    "(katman-hatti 'obsidian-harita' adımı). Kaynak: silver `%s` (%s), kenar = `referans` "
                    "dosya_pointer (çözülmüş). Amaç: backtick pointer kütlesini Obsidian grafiğine göstermek — "
                    "kanon gövdelerine dokunmadan (Karar 72 EK).*" % (damga[1], damga[0]))

    for kume, kaynaklar in sorted(kumeler.items()):
        satirlar = ["# Obsidian bağlantı haritası — %s" % kume, "", baslik_damga, ""]
        for kaynak, hedefler in sorted(kaynaklar.items()):
            satirlar.append("## %s" % md_link(kaynak))
            satirlar.append(" · ".join(md_link(h) for h in sorted(set(hedefler))))
            satirlar.append("")
        with open(os.path.join(a.cikti_dizin, "%s-%s.md" % (HARITA_ONEK, kume)), "w", encoding="utf-8") as fh:
            fh.write("\n".join(satirlar))

    # eski koşumdan kalan, bu koşumda üretilmeyen küme dosyaları temizlenir (türev — m.8 dışı)
    uretilen = {"%s-%s.md" % (HARITA_ONEK, k) for k in kumeler} | {"%s.md" % HARITA_ONEK}
    for ad in sorted(os.listdir(a.cikti_dizin)):
        if ad.startswith(HARITA_ONEK) and ad.endswith(".md") and ad not in uretilen:
            os.remove(os.path.join(a.cikti_dizin, ad))

    indeks = ["# Obsidian bağlantı haritası — indeks", "", baslik_damga, "",
              "| küme | kaynak dosya | kenar | harita |", "|---|---|---|---|"]
    for kume, kaynaklar in sorted(kumeler.items()):
        kenar_sayisi = sum(len(set(h)) for h in kaynaklar.values())
        indeks.append("| %s | %d | %d | [%s-%s.md](%s-%s.md) |"
                      % (kume, len(kaynaklar), kenar_sayisi, HARITA_ONEK, kume, HARITA_ONEK, kume))
    dugumler = {k for k, _ in kenarlar} | {h for _, h in kenarlar}
    indeks += ["", "Toplam: %d kenar · %d düğüm · %d küme. Atılan: md-dışı %d · indeks-dışı %d · "
               "arşiv-kaynak %d · öz-döngü %d." % (len(kenarlar), len(dugumler), len(kumeler),
               atilan["md_disi"], atilan["ignore"], atilan["arsiv_kaynak"], atilan["oz_dongu"]), ""]
    with open(os.path.join(a.cikti_dizin, "%s.md" % HARITA_ONEK), "w", encoding="utf-8") as fh:
        fh.write("\n".join(indeks))

    if not a.sessiz:
        print("obsidian-harita: %d kenar · %d düğüm · %d küme → %s/%s-*.md (silver %s)"
              % (len(kenarlar), len(dugumler), len(kumeler), a.cikti_dizin, HARITA_ONEK, damga[1]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
