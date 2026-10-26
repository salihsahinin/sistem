#!/usr/bin/env python3
"""devir-md2json.py — A1 md emrindeki ```lojik bloğundan devir birimi json'u (v0.1) türetir.

İB-84 (Karar 92 M3 EK, Salih 2026-09-10) · İB-93 (Karar 96 M2 A6, 2026-09-16). Tek kaynak = md emir +
lojik blok; json elle yazılmaz, buradan türetilir; çelişkide md kazanır (Friday tur-2 B2 bulgusu).

Lojik blok sözdizimi (md içinde ```lojik … ``` çiti; anahtar büyük harf = kod jetonu):
  ANAHTAR: değer                 → skaler
  ANAHTAR:                       → altında "  - madde" (liste) ya da "  K1: değer" (sözlük)
Zorunlu alanlar: ZORUNLU listesinde. Her ÇIKTI için DONE satırı zorunlu (çıktı-başına done) ve
her çıktı yolu YAZMA_İZNİ kalıplarından biriyle eşleşmeli (kilit görsün — Friday tur-2 2. aşama notu).

Kullanım:
  python3 tools/devir-md2json.py <emir.md> [--cikti <devir.json>] [--dogrula <mevcut.json>] [--kuru]
Çıkış: 0 türetildi · 2 şema ihlali (eksik alan / çıktı-izin çelişkisi / dal tavanı) · 3 --dogrula farkı ·
       4 dosya/çit yok. Yalnız stdlib; kanona yazmaz.

Ad eşitliği (Karar 93): Jarvis = Salih'le konuşan ana-sıra ajan; tarihli metinlerdeki 'Carvis' = Jarvis.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import re
import sys
from pathlib import Path

SEMA = "devir-birimi v0.2 (A1 türev; tools/devir-md2json.py; md kazanır; v0.2 09-16: OTURUM · KAPANIŞ · KAYNAKLAR · AÇILIŞ_ADIMLARI, olcen→gorev, kapali_goz_ozeti liste, .aktif-devir yazımı)"
ZORUNLU = [
    "DEVİR_ID", "KAYNAK_YÜZEY", "HEDEF_KATMAN", "TARİH", "EMİR_YOLU",
    "AMAÇ", "ÇIKTI", "DONE", "DALLAR", "NİÇİN_ŞİMDİ", "BAĞLI_DEVİR", "KAPALI_GÖZ_ÖZETİ", "ÖLÇEN",
    "EAGER", "LAZY", "KARAR_ÖZETİ", "YASAK", "YAZMA_İZNİ", "BÜTÇE", "YENİDEN_DENEME", "GİT_İZNİ",
    "OTURUM", "KAPANIŞ",  # v0.2 (Friday tur-3 a2, a3)
]
ISTEGE_BAGLI = ["KAYNAKLAR", "AÇILIŞ_ADIMLARI", "PUSH", "KARAR_YETKİSİ"]  # v0.2 a1; URL geçen görevde KAYNAKLAR zorunlu
DAL_TAVANI = 5  # ajan-metodolojisi: dal+koşul ≤5, aşarsa böl
CIT = re.compile(r"```lojik[ \t]*\n(.*?)\n```", re.S)


def blok_cikar(metin: str) -> str | None:
    m = CIT.search(metin)
    return m.group(1) if m else None


def blok_ayristir(blok: str) -> dict:
    """Satır-tabanlı ayrıştırıcı: skaler · liste ('  - ') · sözlük ('  K: v')."""
    veri: dict = {}
    anahtar = None
    for ham in blok.splitlines():
        if not ham.strip() or ham.lstrip().startswith("#"):
            continue
        if not ham.startswith((" ", "\t")):
            k, _, v = ham.partition(":")
            anahtar = k.strip()
            v = v.strip()
            veri[anahtar] = v if v else None
            continue
        if anahtar is None:
            raise ValueError(f"girintili satır anahtarsız: {ham!r}")
        satir = ham.strip()
        if satir.startswith("- "):
            if veri[anahtar] is None:
                veri[anahtar] = []
            if not isinstance(veri[anahtar], list):
                raise ValueError(f"{anahtar}: liste ile skaler/sözlük karışık")
            veri[anahtar].append(satir[2:].strip())
        else:
            k, sep, v = satir.partition(":")
            if not sep:
                raise ValueError(f"{anahtar}: alt satır ne liste ne sözlük: {satir!r}")
            if veri[anahtar] is None:
                veri[anahtar] = {}
            if not isinstance(veri[anahtar], dict):
                raise ValueError(f"{anahtar}: sözlük ile liste karışık")
            veri[anahtar][k.strip()] = v.strip()
    return veri


def butce_ayristir(s: str) -> dict:
    out = {}
    for parca in s.split():
        k, _, v = parca.partition("=")
        out[k] = int(v) if v.isdigit() else v
    return out


def dogrula(v: dict) -> list[str]:
    hatalar = []
    for k in ZORUNLU:
        if k not in v or v[k] in (None, [], {}):
            hatalar.append(f"eksik alan: {k}")
    if hatalar:
        return hatalar
    if not isinstance(v["ÇIKTI"], dict) or not isinstance(v["DONE"], dict):
        return ["ÇIKTI ve DONE 'Cn: …' sözlük biçiminde olmalı (çıktı-başına done)"]
    for c in v["ÇIKTI"]:
        if c not in v["DONE"]:
            hatalar.append(f"DONE eksik: {c} ({v['ÇIKTI'][c]})")
    for c in v["DONE"]:
        if c not in v["ÇIKTI"]:
            hatalar.append(f"DONE var, ÇIKTI yok: {c}")
    izin = v["YAZMA_İZNİ"] if isinstance(v["YAZMA_İZNİ"], list) else [v["YAZMA_İZNİ"]]
    for c, yol in v["ÇIKTI"].items():
        if not any(fnmatch.fnmatch(yol, kalip) or yol.startswith(kalip.rstrip("*")) for kalip in izin):
            hatalar.append(f"çıktı yazma-izni dışında: {c} {yol} ∉ YAZMA_İZNİ")
    dallar = v["DALLAR"] if isinstance(v["DALLAR"], list) else [v["DALLAR"]]
    if len(dallar) > DAL_TAVANI:
        hatalar.append(f"dal sayısı {len(dallar)} > {DAL_TAVANI} — görevi böl")
    for d in dallar:
        if "→" not in d:
            hatalar.append(f"dal '→' içermiyor (koşul → eylem): {d[:60]}")
    if not str(v["YENİDEN_DENEME"]).isdigit():
        hatalar.append("YENİDEN_DENEME tam sayı değil")
    if v["OTURUM"] not in ("devam", "yeni"):
        hatalar.append("OTURUM 'devam' ya da 'yeni' olmalı")
    metin_butun = " ".join(str(x) for x in (v["AMAÇ"], v["NİÇİN_ŞİMDİ"], *liste(v["DALLAR"]), *v["DONE"].values()))
    if re.search(r"https?://|/docs/", metin_butun) and not v.get("KAYNAKLAR"):
        hatalar.append("blokta URL/doküman anılıyor ama KAYNAKLAR yok (Friday tur-3 a1: kaynak bağlayıcı metinde olmalı)")
    return hatalar


def liste(x) -> list:
    return x if isinstance(x, list) else [x]


def json_uret(v: dict, emir_yolu: str) -> dict:
    done_birlesik = " ∧ ".join(f"[{c}] {v['DONE'][c]}" for c in v["ÇIKTI"])
    return {
        "_sema": SEMA,
        "_kaynak_md": emir_yolu,
        "devir": {
            "kimlik": {
                "devir_id": v["DEVİR_ID"], "kaynak_yuzey": v["KAYNAK_YÜZEY"], "hedef_katman": v["HEDEF_KATMAN"],
                "tarih": v["TARİH"], "emir_yolu": v["EMİR_YOLU"], "bagli_devir": v["BAĞLI_DEVİR"],
            },
            "gorev": {
                "amac": v["AMAÇ"], "nicin_simdi": v["NİÇİN_ŞİMDİ"],
                "ciktilar": dict(v["ÇIKTI"]), "done_cikti_basina": dict(v["DONE"]),
                "done_yuklemi": done_birlesik, "dallar": liste(v["DALLAR"]),
                "yeniden_deneme": int(v["YENİDEN_DENEME"]), "olcen": v["ÖLÇEN"],
                "kapanis": liste(v["KAPANIŞ"]),
            },
            "oturum": {"durum": v["OTURUM"], "acilis_adimlari": liste(v.get("AÇILIŞ_ADIMLARI") or [])},
            "kaynaklar": dict(v["KAYNAKLAR"]) if isinstance(v.get("KAYNAKLAR"), dict) else liste(v.get("KAYNAKLAR") or []),
            "baglam": {
                "eager": liste(v["EAGER"]), "lazy": liste(v["LAZY"]), "karar_ozeti": liste(v["KARAR_ÖZETİ"]),
                "yasak": liste(v["YASAK"]), "kapali_goz_ozeti": liste(v["KAPALI_GÖZ_ÖZETİ"]),
            },
            "butce": butce_ayristir(v["BÜTÇE"]),
            "yetki": {
                "karar_yetkisi": str(v.get("KARAR_YETKİSİ", "false")).lower() == "true",
                "yazma_izni": liste(v["YAZMA_İZNİ"]), "git_izni": v["GİT_İZNİ"],
                "push": str(v.get("PUSH", "false")).lower() == "true",
            },
        },
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("emir")
    ap.add_argument("--cikti", help="json yolu (varsayılan: emirle aynı dizin, <DEVİR_ID>.json)")
    ap.add_argument("--dogrula", help="mevcut json ile karşılaştır; fark → çıkış 3 (md kazanır)")
    ap.add_argument("--kuru", action="store_true", help="yazma, json'u stdout'a bas")
    a = ap.parse_args(argv)

    yol = Path(a.emir)
    if not yol.exists():
        print(f"HATA: emir yok: {yol}", file=sys.stderr); return 4
    blok = blok_cikar(yol.read_text(encoding="utf-8"))
    if blok is None:
        print("HATA: ```lojik çiti bulunamadı (A1 formatı değil)", file=sys.stderr); return 4
    try:
        v = blok_ayristir(blok)
    except ValueError as e:
        print(f"ŞEMA: {e}", file=sys.stderr); return 2
    hatalar = dogrula(v)
    if hatalar:
        print("ŞEMA İHLALİ (" + str(len(hatalar)) + "):\n  " + "\n  ".join(hatalar), file=sys.stderr); return 2
    j = json_uret(v, str(yol))
    metin = json.dumps(j, ensure_ascii=False, indent=2, sort_keys=True) + "\n"

    if a.dogrula:
        eski = json.loads(Path(a.dogrula).read_text(encoding="utf-8"))
        if eski != j:
            farklar = [k for k in set(eski.get("devir", {})) | set(j["devir"]) if eski.get("devir", {}).get(k) != j["devir"].get(k)]
            print(f"FARK: json ≠ md türevi; farklı bloklar: {sorted(farklar)} — md kazanır, json'u yeniden türet", file=sys.stderr)
            return 3
        print("EŞ: json = md türevi"); return 0
    if a.kuru:
        sys.stdout.write(metin); return 0
    hedef = Path(a.cikti) if a.cikti else yol.parent / f"{v['DEVİR_ID']}.json"
    hedef.write_text(metin, encoding="utf-8")
    # b1 (Friday tur-3): kütük v0.3 devir_id'yi cc/gelen/.aktif-devir'den okur; "oturum devam" hâlinde seans-acilis koşmaz →
    # dosyayı emri yazan taraf (bu script) bırakır; Friday geri-dönüşte siler.
    (yol.parent / ".aktif-devir").write_text(v["DEVİR_ID"] + "\n", encoding="utf-8")
    print(f"TÜRETİLDİ: {hedef} ({len(metin)} B; çıktı {len(v['ÇIKTI'])} · dal {len(liste(v['DALLAR']))})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
