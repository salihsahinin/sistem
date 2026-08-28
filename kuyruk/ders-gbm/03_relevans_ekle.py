"""
DERECELİ ALAKA (relevans) EKLEME — YetiRank için
==================================================
Mevcut ihale_verisi.csv'ye ("kazandi" 0/1) ek olarak, ekibin önerdiği
5-seviyeli skalayı üretir:

    4: kazandı
    3: ikinci oldu (kıl payı kaçırdı)
    2: teklif verdi ama ikinci de olmadı
    1: detaya baktı (log var)
    0: hiçbir etkileşim yok

DAVRANIŞ MODELİ (gercek_skor'dan türetiliyor — CatBoost bunu keşfetmeye
çalışacak, biz zaten P16'daki gerçek kuralı kullanıyoruz, sadece bu sefer
TEK bir kazanan değil, KADEMELİ bir ilgi zinciri üretiyoruz):

    1. Kazanan: softmax(gercek_skor) ile 1 çekiliş (öncekiyle AYNI mekanizma)
    2. İkinci: kalan 9 aday arasından, yine softmax ile 1 çekiliş
       (kazanana YAKIN skorlu adaylar ikinci olmaya daha meyilli — gerçekçi)
    3. Teklif verenler (ama ilk 2'de değil): olasılık = sigmoid(skor - grup_ortalaması)
       Yüksek skorlu (güçlü aday) kaybetse bile teklif vermiş olma ihtimali yüksek.
    4. Teklif vermeyenler arasında "detaya baktı": daha zayıf, DAHA GÜRÜLTÜLÜ bir
       korelasyon (0.3 katsayı) — rastgele göz atma, ciddi niyetten daha az bağlı.
    5. Geri kalan: hiç etkileşim yok.

NOT (ekiple konuştuğumuz risk): bu script'te "detaya baktı" (relevans=1)
log'u HERKESE eşit kapsamla veriliyor — yani şimdilik MNAR (kapsam-bağımlı
eksiklik) sorunu YOK, temiz bir taban. İstersen bir sonraki turda
"log_kapsami_var_mi" bayrağıyla bu sorunu bilerek veriye enjekte edip
YetiRank'in ne kadar etkilendiğini ölçebiliriz.

Determinizm: aynı tohum (42) ile df.groupby sırası korunuyor.
"""

import numpy as np
import pandas as pd

df = pd.read_csv("/Users/HasanSalihSahin/jarvis/kuyruk/ders-gbm/ihale_verisi.csv")
RNG = np.random.default_rng(43)  # veri üretiminden farklı, bağımsız bir tohum


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


relevans_sutunu = np.zeros(len(df), dtype=int)

for arac_id, grup in df.groupby("arac_id", sort=False):
    idx = grup.index.to_numpy()
    skor = grup["_gercek_skor"].to_numpy()
    n = len(idx)

    kalan = list(range(n))  # grup İÇİNDEKİ pozisyonlar (0..9)

    # --- 1) Kazanan (relevans=4) — YENİDEN ÇEKMİYORUZ, zaten "kazandi"
    #     kolonunda belirlenmiş; onu birebir kullanıyoruz (tutarlılık şart) ---
    kazandi_dizisi = grup["kazandi"].to_numpy()
    kazanan_poz = int(np.where(kazandi_dizisi == 1)[0][0])
    relevans_sutunu[idx[kazanan_poz]] = 4
    kalan.remove(kazanan_poz)

    # --- 2) İkinci (relevans=3) — kalanlar arasında yine softmax ---
    kalan_skor = skor[kalan]
    p2 = np.exp(kalan_skor - kalan_skor.max())
    p2 = p2 / p2.sum()
    ikinci_poz = kalan[RNG.choice(len(kalan), p=p2)]
    relevans_sutunu[idx[ikinci_poz]] = 3
    kalan.remove(ikinci_poz)

    # --- 3) Teklif verenler (relevans=2) — skora bağlı olasılık ---
    ort = skor.mean()
    for poz in list(kalan):
        p_teklif = sigmoid(skor[poz] - ort)
        if RNG.random() < p_teklif:
            relevans_sutunu[idx[poz]] = 2
            kalan.remove(poz)

    # --- 4) Detaya bakanlar (relevans=1) — daha zayıf korelasyon ---
    for poz in list(kalan):
        p_bakti = sigmoid(0.3 * (skor[poz] - ort))
        if RNG.random() < p_bakti:
            relevans_sutunu[idx[poz]] = 1
            kalan.remove(poz)

    # --- 5) Kalanlar: relevans=0 (zaten öyle başlatıldı) ---

df["relevans"] = relevans_sutunu

cikti = "/Users/HasanSalihSahin/jarvis/kuyruk/ders-gbm/ihale_verisi.csv"
df.to_csv(cikti, index=False)

print("RELEVANS KOLONU EKLENDİ")
print("=" * 60)
print(df["relevans"].value_counts().sort_index())
print()
print("Kontrol — her grupta TAM 1 tane relevans=4 olmalı:")
kontrol = df.groupby("arac_id")["relevans"].apply(lambda s: (s == 4).sum())
print(f"  min={kontrol.min()}, max={kontrol.max()}  (ikisi de 1 olmalı)")
print()
print("Kontrol — relevans=4 satırları, eski 'kazandi' ile birebir aynı mı:")
tutarli = ((df["relevans"] == 4) == (df["kazandi"] == 1)).all()
print(f"  tutarlı: {tutarli}")
print()
print("Örnek bir grup (A0007):")
print(df[df.arac_id == "A0007"][["galeri_id", "trim_teklif", "kazandi", "relevans"]]
      .sort_values("relevans", ascending=False).to_string(index=False))
