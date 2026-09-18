"""
SENTETİK İHALE VERİ SETİ ÜRETİCİSİ
===================================
GBM dersi (P1-P17) pratiği için. Salih'in gerçek problemini taklit eder:
haftalık toplu ihale, her araç TEK bir galeriye satılır, model ihale ÖNCESİ
"bu aracı kim alır" sıralaması üretir.

YAPI (gerçek problemle eşleşme):
  grup (group_id) = bir araç       (P16: her grupta TAM 1 pozitif)
  aday            = o araca teklif verebilecek galeriler
  etiket          = 1 (aracı aldı) / 0 (almadı)
  zaman           = hafta numarası (P4: zaman-bazlı bölme için)

GERÇEK KURAL (veriye BİLEREK gömüldü — CatBoost'un bunu keşfetmesini bekliyoruz):

    gercek_skor =
        2.0 * ln(1 + trim_teklif)                 <- kademe 1: EN GÜÇLÜ sinyal
      + 0.8 * ln(1 + seri_disi_trim)              <- kademe 2: orta
      + 0.3 * ln(1 + marka_disi_seri)             <- kademe 3: zayıf
      + 1.5 * (butce_yeterli VE taze)             <- ETKİLEŞİM (kritik!)
      + 1.0 * (sehir_eslesme)                     <- kategorik etki
      - 0.02 * gun_son_teklif                     <- süreklilik: tazelik
      + 0.0 * gurultu_1, gurultu_2                <- SAF GÜRÜLTÜ (model yok saymalı)

    P(galeri kazanır) = softmax(gercek_skor)  [P16'da ispatladığımız formül]
    kazanan = bu dağılımdan çekilen tek galeri

NEDEN BU KURAL SEÇİLDİ - üç öğretici özellik:
  1. KADEME HİYERARŞİSİ (2.0 > 0.8 > 0.3): Salih'in k_seri=0.35 / k_marka=0.15
     elle-ayar tartışmasının karşılığı. Burada DOĞRU değerleri biliyoruz;
     CatBoost'un bunları veriden bulup bulamayacağını göreceğiz.
  2. ETKİLEŞİM (butce_yeterli VE taze): ağırlıklı toplam bunu YAPISAL OLARAK
     yakalayamaz - "yüksek bütçe" tek başına ödül vermiyor, ancak tazelikle
     BİRLİKTE veriyor. Mevcut SQL skorunun neden düşük performans verdiğinin
     muhtemel sebebi bu sınıf.
  3. GÜRÜLTÜ KOLONLARI: feature importance'ta bunların dibe düşmesi, modelin
     gerçekten öğrendiğinin (ezberlemediğinin) kanıtı olacak.

EKSİK VERİ (NULL) TASARIMI:
  Galerilerin ~%25'inde sahibinden eşleşmesi yok (Salih'in listing_match_found
  = FALSE durumu). Bu galerilerin GERÇEK bütçesi vardır ve gerçek kuralda
  kullanılır - ama biz onu GÖZLEMLEYEMEYİZ (kolon NULL gelir). Yani eksiklik
  bir iş sinyali değil, veri kalitesi sorunudur (Salih'in SQL yorumundaki
  tespitin aynısı). notr_dolgu=0.50 tartışmasının test zemini burasıdır.

DETERMİNİZM (Katman-1 ilkesi): sabit tohum (42). Aynı girdi -> aynı veri.

Çıktı: ihale_verisi.csv
"""

import numpy as np
import pandas as pd

RNG = np.random.default_rng(42)  # determinizm: sabit tohum

# ---------------------------------------------------------------------------
# 1. EVREN: markalar, seriler, trimler, şehirler
# ---------------------------------------------------------------------------
MARKALAR = ["Renault", "Fiat", "Volkswagen", "Ford", "Toyota"]
# her markanın 3 serisi, her serinin 3 trimi -> 45 trim
SERILER = {m: [f"{m}-S{i}" for i in range(1, 4)] for m in MARKALAR}
TRIMLER = {s: [f"{s}-T{i}" for i in range(1, 4)] for m in MARKALAR for s in SERILER[m]}
SEHIRLER = ["Istanbul", "Ankara", "Izmir", "Bursa", "Antalya", "Konya"]

TRIM_LISTESI = [t for trimler in TRIMLER.values() for t in trimler]
TRIM_SERI = {t: s for s, trimler in TRIMLER.items() for t in trimler}
SERI_MARKA = {s: m for m in MARKALAR for s in SERILER[m]}

N_GALERI = 40
N_HAFTA = 24
ARAC_PER_HAFTA = 12
ADAY_PER_ARAC = 10

# ---------------------------------------------------------------------------
# 2. GALERİ PROFİLLERİ: her galerinin uzmanlığı, bütçesi, şehri
# ---------------------------------------------------------------------------
# Gerçek hayatta galeriler rastgele değil; belli markalarda uzmanlaşırlar.
# Bu yapı, kademeli teklif sayaçlarının anlamlı olmasını sağlar.
galeriler = []
for gid in range(1, N_GALERI + 1):
    uzman_marka = RNG.choice(MARKALAR)
    uzman_seri = RNG.choice(SERILER[uzman_marka])
    galeriler.append({
        "galeri_id": f"G{gid:03d}",
        "sehir": RNG.choice(SEHIRLER),
        "uzman_marka": uzman_marka,
        "uzman_seri": uzman_seri,
        # bütçe seviyesi: küçük / orta / büyük galeri
        "gercek_butce": float(RNG.choice([250_000, 600_000, 1_400_000], p=[0.4, 0.4, 0.2])),
        # sahibinden eşleşmesi var mı? (~%25 yok -> NULL kolonlar)
        "ilan_eslesme": bool(RNG.random() > 0.25),
        # bu galerinin genel aktiflik eğilimi (teklif sıklığı)
        "aktiflik": float(RNG.uniform(0.3, 1.0)),
    })
galeri_df = pd.DataFrame(galeriler)

# ---------------------------------------------------------------------------
# 3. GEÇMİŞ TEKLİF SAYAÇLARI: (galeri, trim) bazında kademeli geçmiş
# ---------------------------------------------------------------------------
# Uzman olduğu seride yüksek, aynı markanın diğer serilerinde orta,
# yabancı markalarda düşük sayaçlar üretilir. Kademe yapısı (trim <= seri
# <= marka) korunur - Salih'in gerçek tablosundaki iç-içelik kuralı.
def gecmis_sayaclar(galeri, trim):
    seri = TRIM_SERI[trim]
    marka = SERI_MARKA[seri]
    a = galeri["aktiflik"]

    if seri == galeri["uzman_seri"]:
        taban = RNG.poisson(8 * a) + 1
    elif marka == galeri["uzman_marka"]:
        taban = RNG.poisson(3 * a)
    else:
        taban = RNG.poisson(0.4 * a)

    trim_teklif = int(taban)
    # seri sayacı trim'i kapsar (üstüne aynı serinin diğer trimleri)
    seri_teklif = trim_teklif + int(RNG.poisson(max(0.5, taban * 0.6)))
    # marka sayacı seriyi kapsar
    marka_teklif = seri_teklif + int(RNG.poisson(max(0.5, taban * 0.4)))
    return trim_teklif, seri_teklif, marka_teklif


# ---------------------------------------------------------------------------
# 4. HAFTALIK İHALELER
# ---------------------------------------------------------------------------
satirlar = []
arac_sayaci = 0

for hafta in range(1, N_HAFTA + 1):
    for _ in range(ARAC_PER_HAFTA):
        arac_sayaci += 1
        arac_id = f"A{arac_sayaci:04d}"
        trim = RNG.choice(TRIM_LISTESI)
        seri = TRIM_SERI[trim]
        marka = SERI_MARKA[seri]
        arac_fiyat = float(RNG.choice([300_000, 550_000, 900_000], p=[0.4, 0.4, 0.2]))
        arac_sehir = RNG.choice(SEHIRLER)

        # Adaylar: markaya ilgisi olanlara ağırlık verilerek seçilir
        # (gerçekte de rastgele 10 galeri değil, ilgili galeriler teklif verir)
        agirlik = np.array([
            3.0 if g["uzman_marka"] == marka else 1.0
            for g in galeriler
        ])
        agirlik = agirlik / agirlik.sum()
        aday_idx = RNG.choice(len(galeriler), size=ADAY_PER_ARAC, replace=False, p=agirlik)

        grup = []
        for gi in aday_idx:
            g = galeriler[gi]
            trim_t, seri_t, marka_t = gecmis_sayaclar(g, trim)
            gun_son_teklif = int(RNG.exponential(30 / max(g["aktiflik"], 0.2)))
            gun_son_teklif = min(gun_son_teklif, 180)

            # --- GERÇEK KURAL (gizli; model bunu keşfetmeye çalışacak) ---
            butce_yeterli = g["gercek_butce"] >= arac_fiyat
            taze = gun_son_teklif <= 30
            gercek_skor = (
                2.0 * np.log1p(trim_t)
                + 0.8 * np.log1p(max(0, seri_t - trim_t))
                + 0.3 * np.log1p(max(0, marka_t - seri_t))
                + 1.5 * (1.0 if (butce_yeterli and taze) else 0.0)   # ETKİLEŞİM
                + 1.0 * (1.0 if g["sehir"] == arac_sehir else 0.0)
                - 0.02 * gun_son_teklif
            )

            grup.append({
                "hafta": hafta,
                "arac_id": arac_id,
                "galeri_id": g["galeri_id"],
                # --- araç tarafı ---
                "marka": marka,
                "seri": seri,
                "trim": trim,
                "arac_fiyat": arac_fiyat,
                "arac_sehir": arac_sehir,
                # --- galeri tarafı: GÖZLEMLENEBİLİR feature'lar ---
                "galeri_sehir": g["sehir"],
                "trim_teklif": trim_t,
                "seri_teklif": seri_t,
                "marka_teklif": marka_t,
                "gun_son_teklif": gun_son_teklif,
                # bütçe ve ilan kolonları: eşleşme yoksa NULL
                "butce": g["gercek_butce"] if g["ilan_eslesme"] else np.nan,
                "aktif_ilan": (
                    int(RNG.poisson(12 * g["aktiflik"])) if g["ilan_eslesme"] else np.nan
                ),
                "ilan_eslesme": g["ilan_eslesme"],
                # --- SAF GÜRÜLTÜ (gerçek kuralda katsayısı 0) ---
                "gurultu_1": float(RNG.normal(0, 1)),
                "gurultu_2": float(RNG.uniform(0, 100)),
                # --- gizli sütun: doğrulama için tutuluyor, EĞİTİMDE KULLANILMAZ ---
                "_gercek_skor": gercek_skor,
            })

        # --- KAZANANI SEÇ: softmax dağılımından tek çekiliş (P16 formülü) ---
        skorlar = np.array([r["_gercek_skor"] for r in grup])
        p = np.exp(skorlar - skorlar.max())   # sayısal kararlılık için max çıkarma
        p = p / p.sum()
        kazanan_idx = RNG.choice(len(grup), p=p)

        for i, r in enumerate(grup):
            r["kazandi"] = 1 if i == kazanan_idx else 0
            satirlar.append(r)

df = pd.DataFrame(satirlar)

# ---------------------------------------------------------------------------
# 5. KAYDET + ÖZET
# ---------------------------------------------------------------------------
cikti = "/Users/HasanSalihSahin/jarvis/kuyruk/ders-gbm/ihale_verisi.csv"
df.to_csv(cikti, index=False)

print("=" * 70)
print("SENTETİK İHALE VERİ SETİ ÜRETİLDİ")
print("=" * 70)
print(f"dosya          : {cikti}")
print(f"toplam satır   : {len(df):,}")
print(f"araç (grup)    : {df['arac_id'].nunique():,}")
print(f"galeri         : {df['galeri_id'].nunique()}")
print(f"hafta          : {df['hafta'].min()} - {df['hafta'].max()}")
print(f"aday/araç      : {len(df) // df['arac_id'].nunique()}")
print()
print("ETİKET DENGESİ (her grupta tam 1 pozitif olmalı):")
grup_pozitif = df.groupby("arac_id")["kazandi"].sum()
print(f"  her grupta pozitif sayısı: min={grup_pozitif.min()}, max={grup_pozitif.max()}")
print(f"  toplam pozitif           : {df['kazandi'].sum():,} ({df['kazandi'].mean():.1%})")
print()
print("EKSİK VERİ (NULL):")
print(f"  butce NULL      : {df['butce'].isna().sum():,} satır ({df['butce'].isna().mean():.1%})")
print(f"  aktif_ilan NULL : {df['aktif_ilan'].isna().sum():,} satır")
print()
print("ZAMAN BÖLMESİ ÖNERİSİ (P4: kronolojik, karıştırma YOK):")
for ad, (h1, h2) in [("EĞİTİM", (1, 16)), ("DOĞRULAMA", (17, 20)), ("TEST", (21, 24))]:
    alt = df[(df.hafta >= h1) & (df.hafta <= h2)]
    print(f"  {ad:10s} hafta {h1:2d}-{h2:2d} : {len(alt):5,} satır, {alt['arac_id'].nunique():3d} araç")
print()
print("KAZANANLARIN PROFİLİ (gerçek kural işliyor mu — hızlı kontrol):")
kaz = df[df.kazandi == 1]
kyb = df[df.kazandi == 0]
print(f"  {'kolon':<18} {'kazanan ort.':>14} {'kaybeden ort.':>14}")
for kol in ["trim_teklif", "seri_teklif", "marka_teklif", "gun_son_teklif", "gurultu_1", "gurultu_2"]:
    print(f"  {kol:<18} {kaz[kol].mean():>14.2f} {kyb[kol].mean():>14.2f}")
print()
print("  ^ trim_teklif farkı BÜYÜK olmalı (gerçek kuralda katsayı 2.0)")
print("  ^ gurultu_1 / gurultu_2 farkı ~SIFIR olmalı (katsayı 0.0)")
