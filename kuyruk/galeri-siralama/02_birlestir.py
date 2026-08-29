"""
BIRLESTIRME: 4 ham tablo -> tek egitim tablosu (egitim_seti.csv)
=================================================================
Gercek sistemde de is boyle akar: ETL ayri grain'lerde tablo uretir, model
tarafi bunlari TEK bir (lot x galeri) satirinda birlestirir.

  etkilesim.csv       (lot x galeri)   <- omurga; etiket burada
  + lotlar.csv        (lot)            <- arac ozellikleri, her satira kopyalanir
  + galeriler.csv     (galeri)         <- kimlik/sehir/yetki
  + galeri_snapshot.csv (galeri x ay)  <- AS-OF JOIN: lot tarihinden ONCEKI son foto

AS-OF JOIN NEDEN ONEMLI
  Snapshot aylik cekilir. 12 Nisan'daki bir lot icin 1 Nisan fotografi
  kullanilir; 1 Mayis fotografi KULLANILAMAZ -- o gun henuz yoktu.
  pd.merge_asof(direction="backward") tam olarak bunu yapar. Duz merge
  yapmak (ya da en guncel snapshot'i herkese vermek) klasik zaman sizintisidir.

TURETILEN KOLONLAR (birlestirme adiminda hesaplanir, ham tabloda yok)
  butce_yeterli_mi      = alim_butcesi >= muhammen_fiyat   (NULL yayilir)
  butce_arac_karsiligi  = alim_butcesi / muhammen_fiyat
  muhammen_piyasa_orani = muhammen_fiyat / piyasa_medyan_fiyat
  arac_yasi             = 2026 - model_yili
  ilan_fiyat_orani      = muhammen_fiyat / ortalama_ilan_fiyati

Cikti: veri/egitim_seti.csv
"""

from pathlib import Path
import pandas as pd

V = Path(__file__).resolve().parent / "veri"

etk = pd.read_csv(V / "etkilesim.csv", parse_dates=["tarih"])
lot = pd.read_csv(V / "lotlar.csv", parse_dates=["tarih"]).drop(columns=["tarih", "hafta_no"])
gal = pd.read_csv(V / "galeriler.csv")
snp = pd.read_csv(V / "galeri_snapshot.csv", parse_dates=["snapshot_tarihi"])

print(f"etkilesim {etk.shape}  lot {lot.shape}  galeri {gal.shape}  snapshot {snp.shape}")

# --- 1) lot ozellikleri (lot_id ile duz join) ---
df = etk.merge(lot.drop(columns=["_kazanan_galeri_id"]), on=["lot_id", "ihale_id", "lot_sira"], how="left")

# --- 2) galeri kimligi (galeri_id ile duz join) ---
df = df.merge(gal[["galeri_id", "sehir", "bolge", "uyelik_yasi_gun", "ilan_eslesmesi_var"]],
              on="galeri_id", how="left").rename(columns={"sehir": "galeri_sehri", "bolge": "galeri_bolgesi"})

# --- 3) snapshot (AS-OF: lot tarihinden onceki son foto) ---
df = df.sort_values("tarih", kind="stable")
snp = snp.sort_values("snapshot_tarihi", kind="stable")
df = pd.merge_asof(df, snp, left_on="tarih", right_on="snapshot_tarihi",
                   by="galeri_id", direction="backward")
gecikme = (df["tarih"] - df["snapshot_tarihi"]).dt.days
print(f"snapshot gecikmesi (gun): min {gecikme.min()}  medyan {gecikme.median()}  max {gecikme.max()}")

# --- 4) turetilen kolonlar ---
df["butce_yeterli_mi"] = (df["alim_butcesi"] >= df["muhammen_fiyat"]).astype("float64")
df.loc[df["alim_butcesi"].isna(), "butce_yeterli_mi"] = float("nan")   # NULL yayilir, 0 olmaz
df["butce_arac_karsiligi"] = df["alim_butcesi"] / df["muhammen_fiyat"]
df["muhammen_piyasa_orani"] = df["muhammen_fiyat"] / df["piyasa_medyan_fiyat"]
df["arac_yasi"] = 2026 - df["model_yili"]
df["ilan_fiyat_orani"] = df["muhammen_fiyat"] / df["ortalama_ilan_fiyati"]

df = df.drop(columns=["snapshot_tarihi"]).sort_values(["tarih", "ihale_id", "lot_sira", "galeri_id"],
                                                      kind="stable").reset_index(drop=True)
df.to_csv(V / "egitim_seti.csv", index=False)

print(f"\negitim_seti: {df.shape[0]:,} satir x {df.shape[1]} kolon -> {V/'egitim_seti.csv'}")
print("\nNULL orani (%) -- yalnizca NULL'u olan kolonlar:")
nulls = (df.isna().mean() * 100).round(1)
print(nulls[nulls > 0].sort_values(ascending=False).to_string())
