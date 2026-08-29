"""
AGACLARI TEK TEK OKU  (CatBoost simetrik / oblivious agaclar)
==============================================================
CatBoost'un agaci SIMETRIKTIR: her SEVIYEDE tek bir (kolon, esik) cifti vardir
ve o seviyedeki BUTUN dugumlere ayni soru sorulur. Yani derinlik-6 bir agac =
6 bolme + 2^6 = 64 yaprak. Grafik gerekmez, tablo olarak okunur.

YAPRAK NUMARASI
  Her bolme icin bir bit: kosul saglaniyorsa 1, saglanmiyorsa 0.
  seviye 0 -> bit degeri 1, seviye 1 -> 2, seviye 2 -> 4, ... seviye 5 -> 32
  yaprak_no = toplam(bit_k * 2^k)
  (calc_leaf_indexes ile 400 satirda dogrulandi: 400/400 ayni)

TAHMIN = butun agaclarin yaprak degerlerinin TOPLAMI
  (predict ile fark: 0.0 -- scale=1, bias=0)

BOLME TURLERI
  FloatFeature   sayisal kolon > esik ?
                 esik -3.4e38 (-FLT_MAX) ise bu bir NULL TESTIDIR:
                 "deger dolu mu?" NaN olan satirlar 0 tarafina duser.
  OneHotFeature  kategorik kolon == belirli deger ?   (<=10 farkli degerli kolonlar)
  OnlineCtr      hedef-istatistigi(kolon[+kolon...]) > esik ?
                 (>10 farkli degerli kategorikler; CatBoost KOMBINASYON da uretir)

Kullanim:
  python 04_agac_bak.py 0                          agac 0
  python 04_agac_bak.py 0 4                        agac 0..4
  python 04_agac_bak.py --ozet                     552 agacin tamami uzerinden istatistik
  python 04_agac_bak.py --ctr                      uretilen hedef-istatistigi kombinasyonlari
  python 04_agac_bak.py --iz IH0120-L01 G0252 0 3  bir satiri agaclarda adim adim izle
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from catboost import CatBoostRanker, Pool

KOK = Path(__file__).resolve().parent
m = CatBoostRanker(); m.load_model(str(KOK / "model.cbm"))
JS = KOK / "model.json"
if not JS.exists():
    m.save_model(str(JS), format="json")
j = json.load(open(JS))
AGAC = j["oblivious_trees"]
FI = j["features_info"]
FFm = {f["feature_index"]: f["feature_id"] for f in FI["float_features"]}
CFm = {f["feature_index"]: f["feature_id"] for f in FI["categorical_features"]}
FLTMAX = -3.4028234663852886e38


def _el(e):
    if "cat_feature_index" in e: return CFm.get(e["cat_feature_index"], "?")
    if "float_feature_index" in e: return FFm.get(e["float_feature_index"], "?") + "(say)"
    return "?"

# split_index -> (tur, okunur ad, esik, kaynak kolonlar)  -- float bolmelerde 3063/3063 dogrulandi
HARITA, _ix = {}, 0
for f in FI["float_features"]:
    for b in f.get("borders", []):
        HARITA[_ix] = ("float", f["feature_id"], b, [f["feature_id"]]); _ix += 1
for f in FI["categorical_features"]:
    for v in f.get("values", []):
        HARITA[_ix] = ("onehot", f["feature_id"], v, [f["feature_id"]]); _ix += 1
for c in FI["ctrs"]:
    kolonlar = [_el(e) for e in c["elements"]]
    ad = f'{c["ctr_type"]}({"+".join(kolonlar)})'
    for b in c["borders"]:
        HARITA[_ix] = ("ctr", ad, b, kolonlar); _ix += 1


def bolme(s):
    """(okunur kosul, kisa etiket, kaynak kolonlar) dondurur."""
    tur, ad, esik, kol = HARITA[s["split_index"]]
    if tur == "float":
        if esik <= FLTMAX:
            return f"{ad} DOLU MU?", ad, kol
        return f"{ad} > {esik:g}", ad, kol
    if tur == "onehot":
        return f"{ad} == hash:{esik}", ad, kol
    return f"{ad} > {esik:g}", ad.split("(")[1].rstrip(")"), kol


def agac_yaz(i):
    t = AGAC[i]; sp, lv, lw = t["splits"], t["leaf_values"], t["leaf_weights"]
    d = len(sp)
    print("=" * 92)
    print(f"AGAC {i}   derinlik {d}   yaprak {2**d}   bu agaca giren satir {int(sum(lw)):,}")
    print("=" * 92)
    print("BOLMELER (her seviyede TEK soru, butun dugumlere ayni):")
    kisa = []
    for k, s in enumerate(sp):
        kos, et, _ = bolme(s); kisa.append(et[:16])
        print(f"  seviye {k}  bit {2**k:>2}   {kos}")
    print(f"\nYAPRAKLAR  (E = kosul saglandi, h = saglanmadi; bit dizisi seviye 0..{d-1})")
    print(f"  {'no':>3} {'bit':<8}{'agirlik':>9}{'deger':>10}   " + " ".join(f"{x:<16}" for x in kisa))
    for no in sorted(range(2**d), key=lambda x: -lw[x]):
        if lw[no] == 0: continue
        bits = [(no >> k) & 1 for k in range(d)]
        print(f"  {no:>3} {''.join(map(str,bits)):<8}{int(lw[no]):>9,}{lv[no]:>10.5f}   " +
              " ".join(f"{('E' if b else 'h'):<16}" for b in bits))
    print(f"\n  dolu yaprak {sum(1 for w in lw if w>0)}/{2**d}   "
          f"deger araligi {min(lv):+.5f} .. {max(lv):+.5f}   "
          f"katki genisligi {max(lv)-min(lv):.5f}")


def ozet():
    n = sum(len(t["splits"]) for t in AGAC)
    print(f"{len(AGAC)} agac, {n:,} bolme, {len(HARITA):,} olasi ikili ozellik\n")
    say, sev, tur = {}, {}, {}
    for t in AGAC:
        for k, s in enumerate(t["splits"]):
            _, et, _ = bolme(s)
            say[et] = say.get(et, 0) + 1
            sev.setdefault(et, []).append(k)
            tur[s["split_type"]] = tur.get(s["split_type"], 0) + 1
    print("bolme turleri:", tur, "\n")
    tab = pd.DataFrame({"bolme": pd.Series(say),
                        "ort_seviye": pd.Series({k: np.mean(v) for k, v in sev.items()})})
    tab["pay_%"] = (100 * tab.bolme / n).round(2)
    print("EN COK BOLUNEN 25  (ort_seviye kucuk = agacin USTUNDE sorulmus)")
    print(tab.sort_values("bolme", ascending=False).head(25).round(2).to_string())
    hic = [f for f in m.feature_names_ if f not in say]
    print(f"\nHIC BOLUNMEYEN kolon ({len(hic)}): {', '.join(hic) if hic else '— yok'}")


def ctr_listesi():
    print("CatBoost'un URETTIGI hedef-istatistigi ozellikleri (kombinasyonlar dahil):\n")
    for c in FI["ctrs"]:
        kol = "+".join(_el(e) for e in c["elements"])
        print(f"  {c['ctr_type']:<9} {len(c['elements'])} parca   {kol}")


def iz(lot_id, galeri_id, a, b):
    d = pd.read_csv(KOK / "veri/egitim_seti.csv", parse_dates=["tarih"])
    F = m.feature_names_
    K = ["marka", "seri", "trim", "arac_sehri", "galeri_sehri", "galeri_bolgesi"]
    g = d[(d.lot_id == lot_id) & (d.galeri_id == galeri_id)].copy()
    if g.empty: print("satir bulunamadi"); return
    for k in K: g[k] = g[k].fillna("YOK").astype(str)
    g["ilan_eslesmesi_var"] = g["ilan_eslesmesi_var"].astype(int)
    p = Pool(g[F], group_id=[0], cat_features=K)
    yap = m.calc_leaf_indexes(p)[0]
    tam = float(m.predict(p)[0])
    print(f"satir: {lot_id} x {galeri_id}   relevans={int(g.relevans.iloc[0])}   TOPLAM SKOR={tam:.5f}")
    print(f"({len(AGAC)} agacin yaprak degerleri toplami)\n")
    top = 0.0
    for i in range(a, b + 1):
        no = int(yap[i]); t = AGAC[i]; dg = t["leaf_values"][no]; top += dg
        print(f"AGAC {i:>3}  yaprak {no:>3}  katki {dg:+.5f}   kumulatif {top:+.5f}")
        for k, s in enumerate(t["splits"]):
            bit = (no >> k) & 1
            kos, _, kol = bolme(s)
            deg = ", ".join(f"{c}={g[c].iloc[0]}" for c in kol if c in g.columns) or "-"
            print(f"        s{k} {'EVET ' if bit else 'HAYIR'}  {kos:<46} [{deg}]")
        print()
    kalan = tam - top
    print(f"agac {a}..{b} toplami {top:+.5f}   geri kalan {len(AGAC)-(b-a+1)} agac {kalan:+.5f}")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "--ozet": ozet()
    elif a[0] == "--ctr": ctr_listesi()
    elif a[0] == "--iz": iz(a[1], a[2], int(a[3]) if len(a) > 3 else 0, int(a[4]) if len(a) > 4 else 2)
    else:
        for i in range(int(a[0]), (int(a[1]) if len(a) > 1 else int(a[0])) + 1):
            agac_yaz(i); print()
