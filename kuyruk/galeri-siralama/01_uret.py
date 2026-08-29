"""
SENTETİK İHALE + GALERİ VERİ SETİ ÜRETİCİSİ  (Otonet galeri-sıralama problemi)
==============================================================================
Amaç: gerçek "galeri scoring" sisteminin YAPISINI taklit eden, ama 290 kolon
yerine ~45 temel kolon taşıyan bir sentetik evren üretmek. Model: her satılan
araç (lot) için galerileri sıralayan CatBoost YetiRank.

GERÇEK SİSTEMLE EŞLEŞME (kaynak: galeri_scoring_veri_sozlugu_1.xlsx)
  Dataset A · dealer        (grain: galeri)          -> galeriler.csv + galeri_snapshot.csv
  Dataset B · trim_dealer   (grain: trim x galeri)   -> etkilesim.csv icindeki kademe kolonlari
  Rapor CSV (top50/trim)    (grain: trim x galeri)   -> modelin yerini alacagi mevcut skor

İHALE TAKVİMİ (Salih'in tarifi)
  Haftada 3 gun (Pzt/Car/Cum), bazen ayni gun 2. oturum, her oturumda 20 arac
  SIRAYLA satilir. Sira onemli: bir galeri oturumun basinda arac alirsa
  butcesi/istahi azalir -> sonraki lotlarda sansi duser. Bu dinamik veriye
  BILEREK gomulmustur (oturumda_onceki_alim kolonu).

ETİKET (Salih'in 5 kademesi) -- ic ice gecmis huni:
  4 kazandi  c  3 ikinci  c  2 teklif verdi  c  1 detaya bakti  c  0 hicbir sey
  Yani 4 olan mutlaka teklif de vermistir, bakmistir. Huni tutarli uretilir.

GERÇEK KURAL (veriye gomuldu -- CatBoost'un bunu kesfetmesini bekliyoruz):
  gercek_skor =
    + 2.0*ln(1+trim_alim_arac)          <- kademe 1: EN GUCLU sinyal (trim)
    + 0.8*ln(1+seri_alim_arac)          <- kademe 2: orta (seri)
    + 0.3*ln(1+marka_alim_arac)         <- kademe 3: zayif (marka)
    + 1.6*gizli_marka_uyumu             <- GOZLENEMEZ; sayaclardan dolayli okunur
    - 1.5*|ln(lot_fiyat/tercih_fiyat)|  <- U SEKLI: ne cok ucuz ne cok pahali
    + 1.0*ayni_sehir + 0.4*ayni_bolge
    + 1.5*(butce_yeterli VE taze)       <- ETKILESIM: agirlikli toplam yakalayamaz
    + 0.9*raf_bos_sinyali               <- stok bosluğu (had_trim_listing_no_active_now)
    - 0.02*son_teklif_gun               <- tazelik / aclik
    - 1.2*oturumda_onceki_alim          <- SIRALI IHALE DINAMIGI
    + 0.6*aktiflik
    + 0.0*gurultu_1, gurultu_2          <- SAF GURULTU (importance dibe dusmeli)

BU KURALIN OGRETICI 5 OZELLIGI
  1) Kademe hiyerarsisi (2.0>0.8>0.3): elle-ayar k_seri/k_marka tartismasinin karsiligi
  2) Etkilesim (butce VE tazelik): lineer skor yapisal olarak yakalayamaz
  3) U sekilli fiyat uyumu: monoton degil -> agac lazim
  4) Sirali dinamik: ayni oturum icinde bagimlilik (i.i.d. degil)
  5) Gurultu kolonlari: modelin ezberlemedigi bunlarla kanitlanir

ZAMAN SADAKATI (en onemli tasarim karari)
  Bir lotun satirindaki TUM gecmis-sayaclari, o lot ACILMADAN ONCEKI durumdur.
  Simulasyon lot lot kronolojik ilerler; sayac once yazilir, sonra guncellenir.
  Bu yuzden veri setinde zaman sizintisi YOKTUR -- tek istisna, bilerek konan
  TUZAK_donem_sonu_toplam_alim kolonudur (asagida).

ISINMA (burn-in)
  Takvim 2026-01-05'te baslar ama egitim setine 2026-03-16'dan itibaren yazilir.
  Ilk ~10 hafta sadece gecmis biriktirir (soguk baslangic sayaclari 0 olmasin).

NULL TASARIMI (sozlugun 1 numarali kurali: 0 != NULL)
  Galerilerin ~%25'inin sahibinden eslesmesi yok (listing_match_found=FALSE).
  Bu galerilerin GERCEK butcesi vardir ve gercek kuralda KULLANILIR; ama biz
  onu GOZLEYEMEYIZ -> ilan_* ve butce kolonlari NULL gelir, 0 degil.

TUZAK KOLON
  TUZAK_donem_sonu_toplam_alim: galerinin TUM donem boyunca aldigi arac sayisi
  (gelecek dahil). Egitime sokulursa feature importance patlar ve test skoru
  sahte yukselir. Bilerek birakildi -- disari atmayi ogrenmek icin.

DETERMINIZM (Katman-1 ilkesi): sabit tohum 42. Ayni girdi -> ayni veri.
Cikti: veri/{galeriler,galeri_snapshot,ihaleler,lotlar,etkilesim,_gizli_tercihler}.csv
"""

import datetime as dt
from pathlib import Path

import numpy as np
import pandas as pd

TOHUM = 42
RNG = np.random.default_rng(TOHUM)
CIKTI = Path(__file__).resolve().parent / "veri"
CIKTI.mkdir(exist_ok=True)

# ============================================================================
# 1. EVREN
# ============================================================================
MARKALAR = ["Renault", "Fiat", "Volkswagen", "Ford", "Toyota"]
SERI_PER_MARKA, TRIM_PER_SERI = 4, 3
N_MARKA = len(MARKALAR)
N_SERI = N_MARKA * SERI_PER_MARKA          # 20
N_TRIM = N_SERI * TRIM_PER_SERI            # 60

SEHIRLER = ["Istanbul", "Ankara", "Izmir", "Bursa", "Antalya", "Konya",
            "Adana", "Gaziantep", "Kayseri", "Samsun", "Trabzon", "Denizli"]
BOLGE = {"Istanbul": "Marmara", "Bursa": "Marmara", "Ankara": "Ic Anadolu",
         "Konya": "Ic Anadolu", "Kayseri": "Ic Anadolu", "Izmir": "Ege",
         "Denizli": "Ege", "Antalya": "Akdeniz", "Adana": "Akdeniz",
         "Gaziantep": "Guneydogu", "Samsun": "Karadeniz", "Trabzon": "Karadeniz"}
# sehir populasyonu: Istanbul agir basar (gercek dagilim boyle)
SEHIR_AGIRLIK = np.array([.26, .12, .11, .08, .06, .06, .06, .05, .05, .05, .05, .05])
SEHIR_AGIRLIK = SEHIR_AGIRLIK / SEHIR_AGIRLIK.sum()

# --- trim tablosu ---
trim_marka = np.repeat(np.arange(N_MARKA), SERI_PER_MARKA * TRIM_PER_SERI)
trim_seri = np.repeat(np.arange(N_SERI), TRIM_PER_SERI)
trim_ad, seri_ad = [], []
for m in range(N_MARKA):
    for s in range(SERI_PER_MARKA):
        seri_ad.append(f"{MARKALAR[m]}-S{s+1}")
        for t in range(TRIM_PER_SERI):
            trim_ad.append(f"{MARKALAR[m]}-S{s+1}-T{t+1}")
# her trimin piyasa medyan fiyati (TL) ve tipik model yili
trim_taban_fiyat = np.exp(RNG.normal(np.log(750_000), 0.45, N_TRIM))
trim_taban_yil = RNG.integers(2014, 2024, N_TRIM)

# ============================================================================
# 2. GALERILER (gorunur kimlik) + GIZLI TERCIHLER (uretim anahtari)
# ============================================================================
N_GALERI = 420
gid = np.array([f"G{i:04d}" for i in range(1, N_GALERI + 1)])
g_sehir_ix = RNG.choice(len(SEHIRLER), N_GALERI, p=SEHIR_AGIRLIK)
g_sehir = np.array(SEHIRLER)[g_sehir_ix]
g_bolge = np.array([BOLGE[s] for s in g_sehir])

# gizli: her galerinin marka tercihi (Dirichlet -> bazi galeriler tek markaci)
g_marka_uyum = RNG.dirichlet(np.full(N_MARKA, 0.6), N_GALERI)        # (N,5)
g_tercih_fiyat = np.exp(RNG.normal(np.log(700_000), 0.5, N_GALERI))  # TL
g_fiyat_esneklik = RNG.uniform(0.25, 0.9, N_GALERI)                  # log-olcekte sigma
g_tercih_yil = RNG.integers(2013, 2024, N_GALERI)
g_aktiflik = RNG.normal(0, 1, N_GALERI)                              # z-skor
g_kapasite = np.clip(RNG.lognormal(2.2, 0.65, N_GALERI), 2, 90)      # aylik arac
g_uzak_egilim = RNG.beta(1.4, 3.0, N_GALERI)                         # sehir disi istahi

# uyelik + yetki
g_uyelik_gun = RNG.integers(60, 2600, N_GALERI)
g_alim_yetkisi = RNG.random(N_GALERI) > 0.04
g_askida = RNG.random(N_GALERI) < 0.03
g_uygun = g_alim_yetkisi & (~g_askida)
# sahibinden eslesmesi: galeri bazinda HEP-YA-HIC (sozluk: 556/756 hepsi, 200 hicbiri)
g_ilan_eslesti = RNG.random(N_GALERI) > 0.25

pd.DataFrame({
    "galeri_id": gid,
    "galeri_adi": [f"{s} Oto {i:04d}" for i, s in zip(range(1, N_GALERI + 1), g_sehir)],
    "sehir": g_sehir,
    "bolge": g_bolge,
    "uyelik_yasi_gun": g_uyelik_gun,
    "alim_yetkisi": g_alim_yetkisi,
    "askiya_alinmis": g_askida,
    "alim_yapabilir": g_uygun,
    "ilan_eslesmesi_var": g_ilan_eslesti,
}).to_csv(CIKTI / "galeriler.csv", index=False)

pd.DataFrame({
    "galeri_id": gid,
    "gizli_tercih_marka": np.array(MARKALAR)[g_marka_uyum.argmax(1)],
    "gizli_marka_payi": g_marka_uyum.max(1).round(3),
    "gizli_tercih_fiyat": g_tercih_fiyat.round(0),
    "gizli_fiyat_esneklik": g_fiyat_esneklik.round(3),
    "gizli_tercih_model_yili": g_tercih_yil,
    "gizli_aktiflik": g_aktiflik.round(3),
    "gizli_aylik_kapasite": g_kapasite.round(1),
}).to_csv(CIKTI / "_gizli_tercihler.csv", index=False)

# ============================================================================
# 3. TAKVIM: Pzt/Car/Cum, bazen gunde 2 oturum, 20 lot/oturum
# ============================================================================
BASLANGIC = dt.date(2026, 1, 5)     # Pazartesi -- isinma burada baslar
BITIS = dt.date(2026, 8, 28)
YAZIM_BASI = dt.date(2026, 3, 16)   # egitim setine bu tarihten sonrasi yazilir
LOT_ADEDI = 20

oturumlar = []                       # (tarih, gun_ici_oturum)
gun = BASLANGIC
while gun <= BITIS:
    if gun.weekday() in (0, 2, 4):   # Pzt/Car/Cum
        oturumlar.append((gun, 1))
        if RNG.random() < 0.35:      # ayni gun ikinci oturum
            oturumlar.append((gun, 2))
    gun += dt.timedelta(days=1)

GUN0 = BASLANGIC
def gun_no(d): return (d - GUN0).days

# ============================================================================
# 4. DURUM (as-of sayaclar) -- lot lot guncellenir
# ============================================================================
YOK = -10**6                          # "hic olmadi" gun damgasi
c_trim_teklif = np.zeros((N_GALERI, N_TRIM), np.int32)
c_trim_alim = np.zeros((N_GALERI, N_TRIM), np.int32)
c_trim_ikinci = np.zeros((N_GALERI, N_TRIM), np.int32)
c_trim_son_teklif = np.full((N_GALERI, N_TRIM), YOK, np.int32)
c_seri_teklif = np.zeros((N_GALERI, N_SERI), np.int32)
c_seri_alim = np.zeros((N_GALERI, N_SERI), np.int32)
c_marka_teklif = np.zeros((N_GALERI, N_MARKA), np.int32)
c_marka_alim = np.zeros((N_GALERI, N_MARKA), np.int32)
c_marka_son_alim = np.full((N_GALERI, N_MARKA), YOK, np.int32)

g_teklif_arac = np.zeros(N_GALERI, np.int32)
g_alim_arac = np.zeros(N_GALERI, np.int32)
g_ikincilik = np.zeros(N_GALERI, np.int32)
g_sira_toplam = np.zeros(N_GALERI, np.float64)
g_son_teklif = np.full(N_GALERI, YOK, np.int32)
g_son_alim = np.full(N_GALERI, YOK, np.int32)
g_uzak_teklif = np.zeros(N_GALERI, np.int32)
g_ihale_sayisi = np.zeros(N_GALERI, np.int32)
g_alim_fiyat_top = np.zeros(N_GALERI, np.float64)
g_alim_yil_top = np.zeros(N_GALERI, np.float64)

# perakende (sahibinden) tarafi -- aylik snapshot ile guncellenir
r_ilan_var = np.zeros((N_GALERI, N_TRIM), bool)
r_kaybolma_gun = np.full((N_GALERI, N_TRIM), YOK, np.int32)
r_aktif_ilan = np.zeros(N_GALERI, np.float64)
r_ort_fiyat = np.zeros(N_GALERI, np.float64)
r_ort_km = np.zeros(N_GALERI, np.float64)
r_ort_yil = np.zeros(N_GALERI, np.float64)
r_ort_omur = np.zeros(N_GALERI, np.float64)
r_devir = np.zeros(N_GALERI, np.float64)
r_aylik_satis = np.zeros(N_GALERI, np.float64)
r_butce = np.zeros(N_GALERI, np.float64)      # GERCEK butce (her zaman var)
r_seri_cesidi = np.zeros(N_GALERI, np.float64)

snapshot_satir = []

def snapshot_al(d):
    """Aylik perakende (sahibinden) fotografi. Gercek ETL'in lookback pencereli
    snapshot'inin sadelestirilmisi. r_* dizilerini yerinde gunceller."""
    global r_ilan_var
    gn = gun_no(d)
    adet = RNG.poisson(np.clip(g_kapasite * 1.4, 1, None)).astype(float)
    yeni = np.zeros((N_GALERI, N_TRIM), bool)
    # ilanlar tercih edilen markanin trimlerine yigilir
    trim_olasilik = g_marka_uyum[:, trim_marka]              # (N, T)
    trim_olasilik = trim_olasilik / trim_olasilik.sum(1, keepdims=True)
    for i in range(N_GALERI):
        k = int(min(adet[i], N_TRIM))
        if k > 0:
            sec = RNG.choice(N_TRIM, size=k, replace=False, p=trim_olasilik[i])
            yeni[i, sec] = True
    kayboldu = r_ilan_var & (~yeni)                            # raf bosaldi
    r_kaybolma_gun[kayboldu] = gn
    r_ilan_var = yeni
    r_aktif_ilan[:] = yeni.sum(1)
    r_ort_fiyat[:] = g_tercih_fiyat * RNG.uniform(0.95, 1.18, N_GALERI)
    r_ort_km[:] = np.clip(RNG.normal(120_000, 45_000, N_GALERI), 5_000, None)
    r_ort_yil[:] = g_tercih_yil + RNG.normal(0, 0.8, N_GALERI)
    r_devir[:] = np.clip(RNG.normal(0.55, 0.2, N_GALERI), 0.05, 2.0)
    r_ort_omur[:] = np.clip(45 / np.maximum(r_devir, 0.05) * RNG.uniform(.7, 1.3, N_GALERI), 5, 400)
    r_aylik_satis[:] = r_aktif_ilan * r_ort_fiyat * r_devir
    r_butce[:] = r_aylik_satis - r_aktif_ilan * r_ort_fiyat * RNG.uniform(0.25, 0.75, N_GALERI)
    r_seri_cesidi[:] = np.array([len(set(trim_seri[yeni[i]])) for i in range(N_GALERI)])
    nn = np.where(g_ilan_eslesti, 1.0, np.nan)                # NULL maskesi
    snapshot_satir.append(pd.DataFrame({
        "galeri_id": gid, "snapshot_tarihi": d,
        "aktif_ilan_adedi": r_aktif_ilan * nn,
        "ortalama_ilan_fiyati": (r_ort_fiyat * nn).round(0),
        "ortalama_ilan_km": (r_ort_km * nn).round(0),
        "ortalama_ilan_model_yili": (r_ort_yil * nn).round(2),
        "ortalama_ilan_omru_gun": (r_ort_omur * nn).round(1),
        "stok_devir_hizi": (r_devir * nn).round(3),
        "aylik_satis_tutari": (r_aylik_satis * nn).round(0),
        "alim_butcesi": (r_butce * nn).round(0),
        "ilan_seri_cesidi": r_seri_cesidi * nn,
    }))

# ============================================================================
# 5. SIMULASYON
# ============================================================================
ihale_satir, lot_satir, etk_parca = [], [], []
sonraki_snapshot = BASLANGIC

for ihale_no, (tarih, ic_oturum) in enumerate(oturumlar, start=1):
    if tarih >= sonraki_snapshot:
        snapshot_al(tarih)
        y, m = tarih.year, tarih.month + 1
        sonraki_snapshot = dt.date(y + (m > 12), 1 if m > 12 else m, 1)
    gn = gun_no(tarih)
    hafta = gn // 7 + 1
    ihale_id = f"IH{ihale_no:04d}"
    yaz = tarih >= YAZIM_BASI

    # --- oturum katilimcilari: aktiflik agirlikli, uygun galeriler ---
    p = np.exp(0.9 * g_aktiflik) * g_uygun
    p = p / p.sum()
    n_aday = int(RNG.integers(45, 66))
    aday = RNG.choice(N_GALERI, size=n_aday, replace=False, p=p)
    oturum_alim = np.zeros(n_aday, np.int32)     # SIRALI DINAMIGIN hafizasi
    oturum_teklif = np.zeros(n_aday, np.int32)
    g_ihale_sayisi[aday] += 1

    ihale_satir.append((ihale_id, tarih, ["Pzt", "Sal", "Car", "Per", "Cum"][tarih.weekday()],
                        ic_oturum, hafta, LOT_ADEDI, n_aday))

    for sira in range(1, LOT_ADEDI + 1):
        lot_id = f"{ihale_id}-L{sira:02d}"
        t = int(RNG.integers(0, N_TRIM))
        s, mk = int(trim_seri[t]), int(trim_marka[t])
        model_yili = int(np.clip(trim_taban_yil[t] + RNG.integers(-3, 4), 2010, 2025))
        km = float(np.clip(RNG.normal((2026 - model_yili) * 18_000, 35_000), 1_000, 500_000))
        hasar = float(np.clip(RNG.normal(2.0, 1.1), 0, 6))
        piyasa = float(trim_taban_fiyat[t] * (1 + 0.045 * (model_yili - trim_taban_yil[t]))
                       * (1 - 0.00000035 * km) * (1 - 0.035 * hasar))
        piyasa = max(piyasa, 90_000)
        muhammen = float(piyasa * RNG.uniform(0.80, 0.97))
        arac_sehir_ix = int(RNG.choice(len(SEHIRLER), p=SEHIR_AGIRLIK))
        arac_sehir = SEHIRLER[arac_sehir_ix]

        # ---------- as-of GOZLENEBILIR ozellikler (lot acilmadan onceki durum) ----------
        f_trim_teklif = c_trim_teklif[aday, t].astype(float)
        f_trim_alim = c_trim_alim[aday, t].astype(float)
        f_trim_ikinci = c_trim_ikinci[aday, t].astype(float)
        f_seri_teklif = c_seri_teklif[aday, s].astype(float)
        f_seri_alim = c_seri_alim[aday, s].astype(float)
        f_marka_teklif = c_marka_teklif[aday, mk].astype(float)
        f_marka_alim = c_marka_alim[aday, mk].astype(float)

        def gecen_gun(damga):
            d = gn - damga
            return np.where(damga == YOK, np.nan, d.astype(float))

        f_trim_son_teklif_gun = gecen_gun(c_trim_son_teklif[aday, t])
        f_marka_son_alim_gun = gecen_gun(c_marka_son_alim[aday, mk])
        f_son_teklif_gun = gecen_gun(g_son_teklif[aday])
        f_son_alim_gun = gecen_gun(g_son_alim[aday])
        f_teklif_arac = g_teklif_arac[aday].astype(float)
        f_alim_arac = g_alim_arac[aday].astype(float)
        with np.errstate(invalid="ignore", divide="ignore"):
            f_alim_orani = np.where(f_teklif_arac > 0, f_alim_arac / np.maximum(f_teklif_arac, 1), np.nan)
            f_ikincilik_orani = np.where(f_teklif_arac > 0, g_ikincilik[aday] / np.maximum(f_teklif_arac, 1), np.nan)
            f_ort_sira = np.where(f_teklif_arac > 0, g_sira_toplam[aday] / np.maximum(f_teklif_arac, 1), np.nan)
            f_uzak_oran = np.where(f_teklif_arac > 0, g_uzak_teklif[aday] / np.maximum(f_teklif_arac, 1), np.nan)
            f_alim_fiyat_ort = np.where(f_alim_arac > 0, g_alim_fiyat_top[aday] / np.maximum(f_alim_arac, 1), np.nan)
            f_alim_yil_ort = np.where(f_alim_arac > 0, g_alim_yil_top[aday] / np.maximum(f_alim_arac, 1), np.nan)
        f_aclik_farki = f_son_alim_gun - f_son_teklif_gun
        f_farkli_seri = (c_seri_teklif[aday] > 0).sum(1).astype(float)
        tsum = c_seri_teklif[aday].sum(1)
        f_en_buyuk_seri_payi = np.where(tsum > 0, c_seri_teklif[aday].max(1) / np.maximum(tsum, 1), np.nan)

        # ---------- uyum (cift) ozellikleri ----------
        f_ayni_sehir = (g_sehir_ix[aday] == arac_sehir_ix).astype(int)
        f_ayni_bolge = np.array([BOLGE[g_sehir[i]] == BOLGE[arac_sehir] for i in aday], int)
        with np.errstate(invalid="ignore", divide="ignore"):
            f_fiyat_orani = muhammen / f_alim_fiyat_ort
        f_model_yili_farki = model_yili - f_alim_yil_ort

        nn = np.where(g_ilan_eslesti[aday], 1.0, np.nan)      # NULL maskesi (gozlem)
        f_bu_trimde_ilan = r_ilan_var[aday, t].astype(float) * nn
        raf = gn - r_kaybolma_gun[aday, t]
        f_raf_bos_gun = np.where(r_kaybolma_gun[aday, t] == YOK, np.nan,
                                 np.where(r_ilan_var[aday, t], np.nan, raf.astype(float))) * nn
        f_butce = r_butce[aday] * nn
        f_butce_yeterli = (r_butce[aday] >= muhammen).astype(float) * nn
        f_aktif_ilan = r_aktif_ilan[aday] * nn
        f_ilan_fiyat = r_ort_fiyat[aday] * nn
        f_devir = r_devir[aday] * nn

        # ---------- GERCEK KURAL ----------
        gercek_butce_yeterli = (r_butce[aday] >= muhammen).astype(float)   # gozlenemese de gercek
        taze = np.where(np.isnan(f_son_teklif_gun), 0.0, (np.nan_to_num(f_son_teklif_gun, nan=999) <= 14).astype(float))
        raf_bos_sinyali = ((~r_ilan_var[aday, t]) & (r_kaybolma_gun[aday, t] != YOK)
                           & (gn - r_kaybolma_gun[aday, t] <= 90)).astype(float)
        fiyat_uyumsuz = np.abs(np.log(muhammen / g_tercih_fiyat[aday])) / g_fiyat_esneklik[aday]
        skor = (
            2.0 * np.log1p(f_trim_alim)
            + 0.8 * np.log1p(f_seri_alim)
            + 0.3 * np.log1p(f_marka_alim)
            + 1.6 * (g_marka_uyum[aday, mk] * N_MARKA - 1.0)
            - 1.5 * fiyat_uyumsuz
            + 1.0 * f_ayni_sehir + 0.4 * f_ayni_bolge
            + 1.5 * (gercek_butce_yeterli * taze)
            + 0.9 * raf_bos_sinyali
            - 0.02 * np.nan_to_num(f_son_teklif_gun, nan=60.0)
            - 1.2 * oturum_alim
            + 0.6 * g_aktiflik[aday]
            + 0.8 * g_uzak_egilim[aday] * (1 - f_ayni_sehir)
        )
        skor = skor + RNG.gumbel(0, 0.9, n_aday)     # bireysel gurultu

        # ---------- ETIKET HUNISI: 1 -> 2 -> 3 -> 4 ----------
        z = skor - skor.mean()
        bakti = RNG.random(n_aday) < 1 / (1 + np.exp(-(0.55 * z - 0.65)))
        teklif = bakti & (RNG.random(n_aday) < 1 / (1 + np.exp(-(0.85 * z - 2.05))))
        if teklif.sum() < 3:                          # satilan arac -> en az 3 teklifci
            teklif = np.zeros(n_aday, bool)
            teklif[np.argsort(-skor)[:3]] = True
            bakti = bakti | teklif
        tix = np.flatnonzero(teklif)
        ts = skor[tix]
        pr = np.exp(ts - ts.max()); pr /= pr.sum()
        kazanan = tix[RNG.choice(len(tix), p=pr)]
        kalan = tix[tix != kazanan]
        ks = skor[kalan]
        pr2 = np.exp(ks - ks.max()); pr2 /= pr2.sum()
        ikinci = kalan[RNG.choice(len(kalan), p=pr2)]

        relevans = np.zeros(n_aday, np.int8)
        relevans[bakti] = 1
        relevans[teklif] = 2
        relevans[ikinci] = 3
        relevans[kazanan] = 4

        # teklif sirasi (gercek sistemde: galerinin en iyi teklifinin sirasi)
        sira_dizi = np.empty(len(tix), np.int32)
        digerleri = [i for i in tix if i not in (kazanan, ikinci)]
        digerleri = sorted(digerleri, key=lambda i: -skor[i])
        sira_haritasi = {kazanan: 1, ikinci: 2}
        for r, i in enumerate(digerleri, start=3):
            sira_haritasi[i] = r

        # ---------- SATIRLARI YAZ ----------
        if yaz:
            etk_parca.append(pd.DataFrame({
                "lot_id": lot_id, "ihale_id": ihale_id, "lot_sira": sira,
                "tarih": tarih, "hafta_no": hafta,
                "galeri_id": gid[aday],
                # --- Dataset B: kademeli gecmis (trim / seri / marka) ---
                "trim_teklif_arac": f_trim_teklif, "trim_alim_arac": f_trim_alim,
                "trim_ikincilik": f_trim_ikinci, "trim_son_teklif_gun": f_trim_son_teklif_gun,
                "seri_teklif_arac": f_seri_teklif, "seri_alim_arac": f_seri_alim,
                "marka_teklif_arac": f_marka_teklif, "marka_alim_arac": f_marka_alim,
                "marka_son_alim_gun": f_marka_son_alim_gun,
                # --- Dataset A: galeri geneli gecmis ---
                "teklif_verilen_arac": f_teklif_arac, "alinan_arac": f_alim_arac,
                "alim_donusum_orani": f_alim_orani, "ikincilik_orani": f_ikincilik_orani,
                "ortalama_teklif_sirasi": f_ort_sira, "sehir_disi_teklif_orani": f_uzak_oran,
                "son_teklif_gun": f_son_teklif_gun, "son_alim_gun": f_son_alim_gun,
                "aclik_farki_gun": f_aclik_farki,
                "alinan_fiyat_ort": f_alim_fiyat_ort, "alinan_model_yili_ort": f_alim_yil_ort,
                "farkli_seri_sayisi": f_farkli_seri, "en_buyuk_seri_payi": f_en_buyuk_seri_payi,
                "katildigi_ihale_sayisi": g_ihale_sayisi[aday].astype(float),
                # --- sahibinden, (trim x galeri) grain'inde olanlar (NULL'lu) ---
                # galeri-grain olanlar (aktif_ilan_adedi, alim_butcesi ...) BURADA YOK:
                # onlar galeri_snapshot.csv'den 02_birlestir.py'nin as-of join'iyle gelir.
                "bu_trimde_ilani_var": f_bu_trimde_ilan, "raf_bos_gun": f_raf_bos_gun,
                # --- uyum (cift) ---
                "ayni_sehir": f_ayni_sehir, "ayni_bolge": f_ayni_bolge,
                "fiyat_orani": f_fiyat_orani, "model_yili_farki": f_model_yili_farki,
                # --- sirali ihale dinamigi ---
                "oturumda_onceki_alim": oturum_alim.astype(float),
                "oturumda_onceki_teklif": oturum_teklif.astype(float),
                "oturumda_kalan_lot": float(LOT_ADEDI - sira),
                # --- gurultu ---
                "gurultu_1": RNG.normal(0, 1, n_aday),
                "gurultu_2": RNG.uniform(0, 100, n_aday),
                # --- etiket + teshis ---
                "relevans": relevans, "kazandi": (relevans == 4).astype(np.int8),
                "_gercek_skor": skor.round(4),
            }))
            lot_satir.append((lot_id, ihale_id, sira, tarih, hafta, MARKALAR[mk],
                              seri_ad[s], trim_ad[t], model_yili, round(km),
                              round(hasar, 2), round(muhammen), round(piyasa),
                              arac_sehir, n_aday, int(teklif.sum()), gid[aday[kazanan]]))

        # ---------- DURUMU GUNCELLE (satirlar yazildiktan SONRA) ----------
        for i in tix:
            gi = aday[i]
            c_trim_teklif[gi, t] += 1; c_seri_teklif[gi, s] += 1; c_marka_teklif[gi, mk] += 1
            c_trim_son_teklif[gi, t] = gn
            g_teklif_arac[gi] += 1; g_son_teklif[gi] = gn
            g_sira_toplam[gi] += sira_haritasi[i]
            if g_sehir_ix[gi] != arac_sehir_ix:
                g_uzak_teklif[gi] += 1
        oturum_teklif[tix] += 1
        gi = aday[ikinci]; g_ikincilik[gi] += 1; c_trim_ikinci[gi, t] += 1
        gk = aday[kazanan]
        c_trim_alim[gk, t] += 1; c_seri_alim[gk, s] += 1; c_marka_alim[gk, mk] += 1
        c_marka_son_alim[gk, mk] = gn
        g_alim_arac[gk] += 1; g_son_alim[gk] = gn
        g_alim_fiyat_top[gk] += muhammen; g_alim_yil_top[gk] += model_yili
        oturum_alim[kazanan] += 1

# ============================================================================
# 6. YAZ
# ============================================================================
pd.DataFrame(ihale_satir, columns=["ihale_id", "tarih", "gun_adi", "gun_ici_oturum",
                                   "hafta_no", "lot_adedi", "katilimci_galeri_sayisi"]
             ).to_csv(CIKTI / "ihaleler.csv", index=False)

lotlar = pd.DataFrame(lot_satir, columns=[
    "lot_id", "ihale_id", "lot_sira", "tarih", "hafta_no", "marka", "seri", "trim",
    "model_yili", "km", "hasar_skoru", "muhammen_fiyat", "piyasa_medyan_fiyat",
    "arac_sehri", "aday_galeri_sayisi", "teklif_veren_sayisi", "_kazanan_galeri_id"])
lotlar.to_csv(CIKTI / "lotlar.csv", index=False)

etk = pd.concat(etk_parca, ignore_index=True)
# TUZAK: donem sonu (gelecek dahil) toplam alim -- bilerek sizintili kolon
donem_sonu = pd.Series(g_alim_arac, index=gid)
etk["TUZAK_donem_sonu_toplam_alim"] = etk["galeri_id"].map(donem_sonu).astype(float)
etk.to_csv(CIKTI / "etkilesim.csv", index=False)

pd.concat(snapshot_satir, ignore_index=True).to_csv(CIKTI / "galeri_snapshot.csv", index=False)

print(f"ihale      : {len(ihale_satir):>7,}  ({BASLANGIC} -> {BITIS}, yazim >= {YAZIM_BASI})")
print(f"lot        : {len(lotlar):>7,}")
print(f"etkilesim  : {len(etk):>7,} satir x {etk.shape[1]} kolon")
print(f"galeri     : {N_GALERI:>7,}   trim: {N_TRIM}   sehir: {len(SEHIRLER)}")
print("\nrelevans dagilimi:")
print((etk["relevans"].value_counts(normalize=True).sort_index() * 100).round(2).to_string())
print("\ngrup basi ortalama aday:", round(len(etk) / len(lotlar), 1))
