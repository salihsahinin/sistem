import pandas as pd

df = pd.read_csv("ihale_verisi.csv")

print(df.shape)
print(df.head())

egitim = df[df["hafta"] <= 16]
dogrulama = df[(df["hafta"] >= 17) & (df["hafta"] <= 20)]
test = df[df["hafta"] >= 21]

#print("eğitim:", egitim.shape)
#print("doğrulama:", dogrulama.shape)
#print("test:", test.shape)

DISARI = ["hafta", "arac_id", "galeri_id", "kazandi", "relevans", "_gercek_skor"]
KATEGORIK = ["marka", "seri", "trim", "arac_sehir", "galeri_sehir"]

FEATURELAR = [kolon for kolon in df.columns if kolon not in DISARI]

print(FEATURELAR)
#print(len(FEATURELAR))

df["ilan_eslesme"] = df["ilan_eslesme"].astype(int)

from catboost import CatBoostRanker, Pool


def havuz(alt):
    grup_no = pd.factorize(alt["arac_id"])[0]
    return Pool(
        data=alt[FEATURELAR],
        label=alt["relevans"],
        group_id=grup_no,
        cat_features=KATEGORIK,
    )


model = CatBoostRanker(
    loss_function="YetiRank",
    eval_metric="NDCG:top=5",
    iterations=2000,
    learning_rate=0.05,
    depth=6,
    early_stopping_rounds=200,
    random_seed=42,
    verbose=200,
)

model.fit(havuz(egitim), eval_set=havuz(dogrulama), use_best_model=True)

tahminler = model.predict(havuz(test))
test = test.copy()
test["skor"] = tahminler

siralar = []
for arac, grup in test.groupby("arac_id"):
    g = grup.sort_values("skor", ascending=False).reset_index(drop=True)
    sira = g.index[g["kazandi"] == 1][0] + 1
    siralar.append(sira)

siralar = pd.Series(siralar)
print("ortalama sıra:", siralar.mean())
print("Hit Rate@1:", (siralar <= 1).mean())
print("Hit Rate@3:", (siralar <= 3).mean())
print("Hit Rate@5:", (siralar <= 5).mean())