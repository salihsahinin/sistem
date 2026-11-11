"""Aylık bronz kütük düzeni (Karar 130 D23): `veri/bronz/<ad>/<YYYY-MM>.jsonl`.

Rust karşılığı `kod/ortak/src/bronz.rs` (jarvis-ortak); kural ikisinde aynıdır:
ay = JSON nesnesinde ZAMAN_ANAHTARLARI sırasıyla ilk `YYYY-MM` önekli dize, yoksa üst düzeydeki ilk böyle dize.
Ayı okunamayan satır bir önceki geçerli satırın ayına gider; öncesi yoksa sonraki ilk geçerli satırın ayına; hiç yoksa bugünün ayına.
Okuyan bütün ay dosyalarını ad sırasıyla okur.
"""
import datetime
import json
import os
import re

ZAMAN_ANAHTARLARI = ("ts", "ts_utc", "ts_bas", "tarih", "yuklendi_ts", "cekim_tarihi")
_AY = re.compile(r"^(\d{4})-(0[1-9]|1[0-2])")


def _ay_onek(s):
    m = _AY.match(s) if isinstance(s, str) else None
    return m.group(0) if m else None


def satir_ayi(satir):
    try:
        d = json.loads(satir)
    except Exception:
        return None
    if not isinstance(d, dict):
        return None
    for k in ZAMAN_ANAHTARLARI:
        ay = _ay_onek(d.get(k))
        if ay:
            return ay
    for v in d.values():
        ay = _ay_onek(v)
        if ay:
            return ay
    return None


def kok_ad(ad):
    return ad[:-6] if ad.endswith(".jsonl") else ad


def dizin(bronz, ad):
    return os.path.join(bronz, kok_ad(ad))


def ay_dosyalari(bronz, ad):
    d = dizin(bronz, ad)
    if not os.path.isdir(d):
        return []
    return [os.path.join(d, n) for n in sorted(os.listdir(d)) if n.endswith(".jsonl") and _ay_onek(n)]


def var_mi(bronz, ad):
    return bool(ay_dosyalari(bronz, ad))


def aylara_bol(metin, varsayilan_ay):
    parcalar = metin.splitlines(keepends=True)
    aylar = [satir_ayi(p) for p in parcalar]
    ilk = next((a for a in aylar if a), varsayilan_ay)
    gruplar, onceki = [], None
    for p, a in zip(parcalar, aylar):
        ay = a or onceki or ilk
        onceki = ay
        if gruplar and gruplar[-1][0] == ay:
            gruplar[-1][1].append(p)
        else:
            gruplar.append((ay, [p]))
    return [(ay, "".join(ps)) for ay, ps in gruplar]


def ekle(bronz, ad, metin):
    """metin (satır sonları dahil) ay dosyalarına eklenir; her ay grubu tek yazımla gider."""
    if not metin:
        return
    os.makedirs(dizin(bronz, ad), exist_ok=True)
    for ay, parca in aylara_bol(metin, datetime.datetime.now().strftime("%Y-%m")):
        with open(os.path.join(dizin(bronz, ad), ay + ".jsonl"), "a", encoding="utf-8", newline="") as f:
            f.write(parca)


def satirlar(bronz, ad):
    """Bütün ay dosyalarının satırları, ad sırasıyla (open(...) satır yinelemesi gibi, satır sonu dahil)."""
    for yol in ay_dosyalari(bronz, ad):
        with open(yol, encoding="utf-8") as f:
            for l in f:
                yield l if l.endswith("\n") else l + "\n"
