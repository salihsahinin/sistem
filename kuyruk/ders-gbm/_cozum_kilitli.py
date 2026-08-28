"""
CATBOOST RANKER EĞİTİMİ — sentetik ihale verisi üzerinde
=========================================================
Ders partisyonlarıyla eşleşme:
  P4  : zaman-bazlı bölme (kronolojik, karıştırma YOK)
  P13 : erken durdurma (doğrulama setine bakarak)
  P15 : NDCG@k, Hit Rate@k — elle kurduğumuz formüller
  P16 : QuerySoftMax, group_id = araç (her grupta tam 1 pozitif)

Determinizm (Katman-1): sabit tohum + tek iş parçacığı -> aynı girdi, aynı model.
"""

import numpy as np
import pandas as pd
from catboost import CatBoostRanker, Pool

DIZIN = "/Users/HasanSalihSahin/jarvis/kuyruk/ders-gbm"
df = pd.read_csv(f"{DIZIN}/ihale_verisi.csv")

# ---------------------------------------------------------------------------
# 1. FEATURE TRİYAJI (P16'nın kimlik-ezberi uyarısı)
# ---------------------------------------------------------------------------
# DIŞARI atılanlar ve nedenleri:
#   _gercek_skor -> CEVAP ANAHTARI. Veriyi üretirken kullandığımız gizli skor;
#                   eğitime girerse model hiçbir şey öğrenmeden %100 başarır
#                   (en saf sızıntı örneği).
#   arac_id      -> grup anahtarı, feature değil
#   galeri_id    -> kimlik. Model davranışı değil kimliği ezberler; yeni
#                   galeride çöker (P16).
DISARI = ["_gercek_skor", "arac_id", "galeri_id", "kazandi", "hafta"]

KATEGORIK = ["marka", "seri", "trim", "arac_sehir", "galeri_sehir"]

df["ilan_eslesme"] = df["ilan_eslesme"].astype(int)   # bool -> 0/1
df = df.sort_values(["hafta", "arac_id"]).reset_index(drop=True)

# CatBoost group_id tam sayı ister ve grupların bitişik olmasını bekler
df["grup_no"] = pd.factorize(df["arac_id"])[0]

FEATURELAR = [k for k in df.columns if k not in DISARI + ["grup_no"]]
print("EĞİTİME GİREN FEATURE'LAR:")
for f in FEATURELAR:
    tip = "kategorik" if f in KATEGORIK else "sayısal"
    bos = df[f].isna().sum()
    print(f"   {f:<18} {tip:<10} {'NULL: ' + str(bos) if bos else ''}")
print()

# ---------------------------------------------------------------------------
# 2. ZAMAN-BAZLI BÖLME (P4) — rastgele karıştırma YOK
# ---------------------------------------------------------------------------
egitim = df[df.hafta <= 16]
dogrulama = df[(df.hafta >= 17) & (df.hafta <= 20)]
test = df[df.hafta >= 21]


def havuz(alt):
    """CatBoost Pool nesnesi: veri + etiket + grup anahtarı bir arada."""
    return Pool(
        data=alt[FEATURELAR],
        label=alt["kazandi"],
        group_id=alt["grup_no"],
        cat_features=KATEGORIK,
    )


print(f"BÖLME  eğitim: hafta 1-16 ({egitim.arac_id.nunique()} araç) | "
      f"doğrulama: 17-20 ({dogrulama.arac_id.nunique()}) | "
      f"test: 21-24 ({test.arac_id.nunique()})\n")

# ---------------------------------------------------------------------------
# 3. MODEL (P16) — QuerySoftMax, tek-pozitiflik yapısına özel kayıp
# ---------------------------------------------------------------------------
model = CatBoostRanker(
    loss_function="QuerySoftMax",   # P16: grup içinde TEK doğru cevap
    eval_metric="NDCG:top=5",       # P15: elle kurduğumuz metrik
    iterations=2000,
    learning_rate=0.05,             # P11: küçük adım, çok ağaç
    depth=6,
    l2_leaf_reg=5,
    early_stopping_rounds=200,      # P13: doğrulama iyileşmiyorsa dur
    random_seed=42,                 # determinizm
    thread_count=1,                 # tam tekrarlanabilirlik
    verbose=200,
)

print("EĞİTİM BAŞLIYOR")
print("-" * 70)
model.fit(havuz(egitim), eval_set=havuz(dogrulama), use_best_model=True)
print("-" * 70)
print(f"En iyi iterasyon: {model.get_best_iteration()} "
      f"(erken durdurma {'TETİKLENDİ' if model.get_best_iteration() < 1999 else 'tetiklenmedi'})\n")


# ---------------------------------------------------------------------------
# 4. ÖLÇÜM (P15) — elle kurduğumuz formüller
# ---------------------------------------------------------------------------
def olc(alt, skorlar, ad):
    """Her grup için kazananın sırasını bulup P15 metriklerini hesaplar.

    Tek pozitif olduğu için (P15'te ispatladık) IDCG=1, yani NDCG=DCG.
    """
    t = alt.copy()
    t["skor"] = skorlar
    siralar = []
    for _, grup in t.groupby("arac_id"):
        g = grup.sort_values("skor", ascending=False).reset_index(drop=True)
        sira = g.index[g["kazandi"] == 1][0] + 1   # 1'den başlayan sıra
        siralar.append(sira)
    s = np.array(siralar)

    print(f"{ad}")
    print(f"   kazananın ortalama sırası : {s.mean():.2f} / 10")
    print(f"   Hit Rate@1                : {(s <= 1).mean():.1%}")
    print(f"   Hit Rate@3                : {(s <= 3).mean():.1%}")
    print(f"   Hit Rate@5                : {(s <= 5).mean():.1%}")
    print(f"   NDCG@5                    : {np.where(s <= 5, 1/np.log2(s+1), 0).mean():.4f}")
    print()
    return s


print("=" * 70)
print("TEST SONUÇLARI (hafta 21-24 — model bu veriyi HİÇ görmedi)")
print("=" * 70)

olc(test, model.predict(havuz(test)), "CATBOOST")

# --- TABAN ÇİZGİLERİ: model gerçekten değer katıyor mu? ---
rng = np.random.default_rng(42)
olc(test, rng.random(len(test)), "TABAN 1 — RASTGELE sıralama")

# popülerlik: eğitimde en çok kazanan galeriler hep üstte
kazanma = egitim.groupby("galeri_id")["kazandi"].sum()
olc(test, test["galeri_id"].map(kazanma).fillna(0).values, "TABAN 2 — POPÜLERLİK (geçmiş kazanan sayısı)")

# ---------------------------------------------------------------------------
# 5. MODEL NE ÖĞRENDİ? (sentetik verinin asıl değeri — gerçek kuralı biliyoruz)
# ---------------------------------------------------------------------------
print("=" * 70)
print("FEATURE ÖNEMİ — gerçek kuralla karşılaştırma")
print("=" * 70)
# Sıralama modellerinde önem hesabı eğitim havuzunu ister (kayıp-değişimi yöntemi)
onem = model.get_feature_importance(data=havuz(egitim), prettified=True)
GERCEK = {
    "trim_teklif": "katsayı 2.0 — EN GÜÇLÜ olmalı",
    "seri_teklif": "katsayı 0.8 — orta",
    "marka_teklif": "katsayı 0.3 — zayıf",
    "butce": "1.5 — ama SADECE tazelikle ETKİLEŞİMDE",
    "gun_son_teklif": "0.02 + etkileşimin diğer yarısı",
    "arac_fiyat": "bütçe karşılaştırmasının diğer yarısı",
    "galeri_sehir": "1.0 — araç şehriyle eşleşirse",
    "arac_sehir": "1.0 — galeri şehriyle eşleşirse",
    "gurultu_1": "*** 0.0 — SAF GÜRÜLTÜ, dipte olmalı ***",
    "gurultu_2": "*** 0.0 — SAF GÜRÜLTÜ, dipte olmalı ***",
}
print(f"{'sıra':<5} {'feature':<18} {'önem':>7}   gerçek kuraldaki yeri")
for i, satir in onem.iterrows():
    ad = satir["Feature Id"]
    print(f"{i+1:<5} {ad:<18} {satir['Importances']:>6.2f}   {GERCEK.get(ad, '-')}")

# ---------------------------------------------------------------------------
# 6. ETKİLEŞİMİ ÖĞRENDİ Mİ? (gerçek kuralın en zor parçası)
# ---------------------------------------------------------------------------
# Gerçek kural: bonus SADECE (bütçe yeterli VE taze) ise veriliyor (+1.5).
# Ağırlıklı toplam bunu yakalayamaz; ağaç yakalayabilir. Test edelim:
# modelin 4 kombinasyona verdiği ortalama skorlara bakıyoruz.
print()
print("=" * 70)
print("ETKİLEŞİM TESTİ — model 'bütçe VE tazelik' kuralını yakaladı mı?")
print("=" * 70)
t = test.copy()
t["model_skoru"] = model.predict(havuz(test))
t["butce_yeterli"] = t["butce"] >= t["arac_fiyat"]
t["taze"] = t["gun_son_teklif"] <= 30
alt = t[t["butce"].notna()]          # NULL bütçeliler bu testin dışında

print(f"{'bütçe yeterli':<15} {'taze':<8} {'n':>5} {'ortalama model skoru':>22}")
hucre = {}
for (b, z), g in alt.groupby(["butce_yeterli", "taze"]):
    hucre[(b, z)] = g["model_skoru"].mean()
    print(f"{str(b):<15} {str(z):<8} {len(g):>5} {g['model_skoru'].mean():>22.3f}")

if len(hucre) == 4:
    # Toplamsal (etkileşimsiz) bir model şunu öngörürdü:
    #   skor(V,V) = skor(Y,Y) + [skor(V,Y)-skor(Y,Y)] + [skor(Y,V)-skor(Y,Y)]
    beklenen = hucre[(True, False)] + hucre[(False, True)] - hucre[(False, False)]
    gercek = hucre[(True, True)]
    print()
    print(f"  Toplamsal modelin öngörüsü (V,V için) : {beklenen:.3f}")
    print(f"  Modelin GERÇEK (V,V) skoru            : {gercek:.3f}")
    print(f"  ETKİLEŞİM ARTISI                      : {gercek - beklenen:+.3f}")
    print()
    if gercek - beklenen > 0.1:
        print("  ==> POZİTİF: model, iki koşulun BİRLİKTE olmasına ekstra değer veriyor.")
        print("      Ağırlıklı toplam bunu yapısal olarak üretemezdi (artış tam 0 olurdu).")
    else:
        print("  ==> Belirgin etkileşim artısı yok; model bu kuralı yakalayamamış olabilir.")
