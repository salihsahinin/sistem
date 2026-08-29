"""
EGITIM: CatBoost YetiRank ile "bu araci hangi galeri alir" siralamasi
======================================================================
Grup (query)  = BIR LOT (ihaledeki tek arac).  Grup icinde ~54 aday galeri.
Etiket        = relevans 0-4 (Salih'in kademesi).
Kayip         = YetiRank (dereceli alakayi kullanan siralama kaybi).
Metrik        = NDCG@5 + is metrikleri (Hit Rate@k, kazananin ortalama sirasi).

BOLME: ZAMAN BAZLI (P4). Rastgele bolme burada YANLIStir -- ayni ihalenin
satirlari egitim ve teste dagilirsa model gelecegi gormus olur.

  egitim    2026-03-16 .. 2026-07-05
  dogrulama 2026-07-06 .. 2026-07-31   (early stopping burada karar verir)
  test      2026-08-01 .. 2026-08-28   (tek sefer bakilir)

Kullanim:
  python 03_egit.py            # temiz kosum
  python 03_egit.py --tuzak    # TUZAK_ kolonunu da sokar (sizinti gosterimi)
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from catboost import CatBoostRanker, Pool

V = Path(__file__).resolve().parent / "veri"
TUZAK = "--tuzak" in sys.argv
SIZINTI = "--sizinti" in sys.argv   # pencere kaymasi: sayaclar TAHMIN EDILEN ihaleyi de iceriyor

df = pd.read_csv(V / "egitim_seti.csv", parse_dates=["tarih"])
print(f"veri: {df.shape[0]:,} satir x {df.shape[1]} kolon, {df['lot_id'].nunique():,} lot")

if SIZINTI:
    # GERCEK HAYATTAKI EN SIK SIZINTI: lookback penceresi tahmin edilen ihaleden
    # SONRA bitiyorsa, galerinin o ihaledeki alimi kendi sayacina dahil olur.
    # Asagidaki dort satir tam olarak bunu taklit ediyor.
    print("  !! SIZINTI MODU: kademe sayaclari bu lotun sonucunu da iceriyor")
    ted = (df["relevans"] >= 2).astype(int)
    df["trim_alim_arac"]   = df["trim_alim_arac"]   + df["kazandi"]
    df["seri_alim_arac"]   = df["seri_alim_arac"]   + df["kazandi"]
    df["marka_alim_arac"]  = df["marka_alim_arac"]  + df["kazandi"]
    df["trim_teklif_arac"] = df["trim_teklif_arac"] + ted
    df["alinan_arac"]      = df["alinan_arac"]      + df["kazandi"]

# ---------------------------------------------------------------- 1. BOLME
egitim = df[df["tarih"] <= "2026-07-05"]
dogrulama = df[(df["tarih"] > "2026-07-05") & (df["tarih"] <= "2026-07-31")]
test = df[df["tarih"] > "2026-07-31"].copy()
for ad, alt in [("egitim", egitim), ("dogrulama", dogrulama), ("test", test)]:
    print(f"  {ad:<10} {len(alt):>7,} satir  {alt['lot_id'].nunique():>5,} lot")

# ------------------------------------------------------- 2. KOLON TRIYAJI
# Kural: kimlik, etiket, tarih ve alt cizgiyle baslayan her kolon DISARIDA.
DISARI = ["lot_id", "ihale_id", "galeri_id", "tarih", "hafta_no",
          "relevans", "kazandi", "_gercek_skor", "_kazanan_galeri_id"]
if not TUZAK:
    DISARI.append("TUZAK_donem_sonu_toplam_alim")

KATEGORIK = ["marka", "seri", "trim", "arac_sehri", "galeri_sehri", "galeri_bolgesi"]
FEATURE = [k for k in df.columns if k not in DISARI and not k.startswith("_")]
print(f"\nfeature sayisi: {len(FEATURE)}  (kategorik {len(KATEGORIK)}, sayisal {len(FEATURE)-len(KATEGORIK)})")
if TUZAK:
    print("  !! TUZAK kolonu ICERIDE -- sonuclar sahte yuksek cikacak")

# kategorik kolonlarda NaN olamaz; sayisal NaN'lari CatBoost kendi isler (BIRAKILIYOR)
for alt in (df, egitim, dogrulama, test):
    for k in KATEGORIK:
        alt[k] = alt[k].fillna("YOK").astype(str)
for k in ["ilan_eslesmesi_var"]:
    if k in FEATURE:
        for alt in (egitim, dogrulama, test):
            alt[k] = alt[k].astype(int)

def havuz(alt):
    """Satirlar lot_id'ye gore ARDISIK olmali (02_birlestir.py boyle siraliyor)."""
    return Pool(data=alt[FEATURE], label=alt["relevans"],
                group_id=pd.factorize(alt["lot_id"])[0], cat_features=KATEGORIK)

# ---------------------------------------------------------------- 3. EGITIM
model = CatBoostRanker(
    loss_function="YetiRank",      # dereceli alaka (0-4) kullanir; QuerySoftMax yalniz 0/1 kullanirdi
    eval_metric="NDCG:top=5",
    iterations=2000,
    learning_rate=0.05,
    depth=6,
    early_stopping_rounds=200,     # dogrulama NDCG'si 200 turda iyilesmezse dur
    random_seed=42,
    verbose=200,
)
model.fit(havuz(egitim), eval_set=havuz(dogrulama), use_best_model=True)
print(f"\nsecilen agac sayisi: {model.tree_count_}")

# ------------------------------------------------------- 4. TEST + IS METRIGI
test["skor"] = model.predict(havuz(test))

def ndcg_at_k(alt, skor_kolonu, k=5):
    """P15'te elle kurdugumuz NDCG: DCG = sum (2^rel - 1)/log2(sira+1), IDCG ile normalize."""
    toplam = []
    for _, g in alt.groupby("lot_id", sort=False):
        rel = g["relevans"].to_numpy()
        s = g[skor_kolonu].to_numpy()
        tahmin = rel[np.argsort(-s, kind="stable")][:k]
        ideal = np.sort(rel)[::-1][:k]
        d = 1 / np.log2(np.arange(2, len(tahmin) + 2))
        dcg = ((2.0 ** tahmin - 1) * d).sum()
        idcg = ((2.0 ** ideal - 1) * d[:len(ideal)]).sum()
        toplam.append(dcg / idcg if idcg > 0 else 0.0)
    return float(np.mean(toplam))

def is_metrikleri(alt, skor_kolonu):
    """Kazananin tahmin siralamasindaki yeri -> Hit Rate@k, MRR, ortalama sira."""
    sira = (alt.groupby("lot_id")[skor_kolonu].rank(ascending=False, method="first"))
    kz = sira[alt["kazandi"] == 1]
    return {"lot": len(kz), "ort_sira": kz.mean(), "HR@1": (kz <= 1).mean(),
            "HR@3": (kz <= 3).mean(), "HR@5": (kz <= 5).mean(),
            "HR@10": (kz <= 10).mean(), "MRR": (1 / kz).mean(),
            "NDCG@5": ndcg_at_k(alt, skor_kolonu, 5)}

# taban cizgileri (model bunlari yenmezse is degeri yok)
rng = np.random.default_rng(0)
test["taban_rastgele"] = rng.random(len(test))
test["taban_populerlik"] = test["alinan_arac"].fillna(0)
test["taban_elle_skor"] = (                       # mevcut SQL skorunun sadelestirilmisi
    0.50 * np.log1p(test["trim_alim_arac"].fillna(0))
    + 0.30 * np.log1p(test["seri_alim_arac"].fillna(0))
    + 0.20 * np.log1p(test["marka_alim_arac"].fillna(0))
    + 0.40 * test["ayni_sehir"])

print("\n" + "=" * 72)
print(f"{'yontem':<22}{'ort_sira':>9}{'HR@1':>8}{'HR@3':>8}{'HR@5':>8}{'HR@10':>8}{'MRR':>8}{'NDCG@5':>9}")
print("=" * 81)
for ad, kol in [("rastgele", "taban_rastgele"), ("populerlik", "taban_populerlik"),
                ("elle agirlikli skor", "taban_elle_skor"), ("CatBoost YetiRank", "skor")]:
    m = is_metrikleri(test, kol)
    print(f"{ad:<22}{m['ort_sira']:>9.2f}{m['HR@1']:>8.3f}{m['HR@3']:>8.3f}"
          f"{m['HR@5']:>8.3f}{m['HR@10']:>8.3f}{m['MRR']:>8.3f}{m['NDCG@5']:>9.3f}")
print("=" * 81)
print(f"grup basi ortalama aday: {len(test)/test['lot_id'].nunique():.1f}"
      f"  (rastgele HR@1 beklentisi ~{test['lot_id'].nunique()/len(test):.3f})")

# ------------------------------------------------------------ 5. ONEM SIRASI
onem = pd.Series(model.get_feature_importance(type="PredictionValuesChange"),
                 index=FEATURE).sort_values(ascending=False)
print("\nen onemli 15 feature:")
print(onem.head(15).round(2).to_string())
print(f"  (butun feature onemleri toplami 100)")
print("\ngurultu kolonlarinin yeri (dipte olmali):")
for k in ["gurultu_1", "gurultu_2"]:
    print(f"  {k:<12} onem {onem[k]:.2f}  sira {list(onem.index).index(k)+1}/{len(onem)}")

ad = "model_tuzak.cbm" if TUZAK else ("model_sizinti.cbm" if SIZINTI else "model.cbm")
model.save_model(str(Path(__file__).resolve().parent / ad))
print(f"\nmodel kaydedildi: {ad}")
