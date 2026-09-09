#!/usr/bin/env python3
"""devir-ani.py — DEVİR-ANI YÜKLEMİ ölçüm aygıtı (yalnız LOGLAR, ATEŞLEMEZ). Kaynak spec: `raporlar/2026-09/2026-09-09-ib75-baglam-devri-ekip-lideri.md` §4.

Yüklem (m.38 boolean):
  DEVRET  ↔  ( baglam_token ≥ E1 ∧ gorev_siniri ) ∨ ( baglam_token ≥ E2 )
  gorev_siniri ↔ (acik_isci_cagrisi = 0) ∧ (son_isci_donusu_diskte = doğru) ∧ (yarim_kanon_yazimi = 0)
  E1 = 128000  (kaynaklı: v_baglam_seyri `tur_128k_ustu` kolonunun eşiği)
  E2 = 600000  [?] deneysel — SABİT, DEĞİŞTİRME (Salih'in açık sorusu Q2)

`gorev_siniri`'nin üç bileşeni mevcut girdilerden (v_baglam_seyri.csv, baglam-olay.jsonl) TÜRETİLEMEZ — uydurulmaz. Bu yüzden script
`gorev_siniri = None` yazar (kayıtta `gorev_siniri_not` alanıyla açıklanır) ve ÜÇ-DEĞERLİ (Kleene) mantık uygular:
  True ∧ None = None · False ∧ None = False · True ∨ None = True · False ∨ None = None
Sonuç: max_baglam ≥ E2 → True (E2-son-care) · E1 ≤ max_baglam < E2 → None (E1-asildi-gorev-siniri-bilinmiyor) · max_baglam < E1 → False (esik-alti).

Girdi: `veri/gorunum/v_baglam_seyri.csv` (oturum başına satır; kolon `max_baglam`, `tur_128k_ustu` kullanılır). `veri/bronz/baglam-olay.jsonl`
şu an TETİKLEYİCİ hesaba katılmıyor (v_baglam_seyri zaten bronz'dan türetilmiş silver/gold; ileride tur-bazlı kesinleştirme için tutulan pointer).

Çıktı: `veri/bronz/devir-ani-olay.jsonl` (append-only, 1 satır = 1 oturumun devir-anı ölçümü). İdempotens: (oturum, max_baglam) çifti mevcutsa
tekrar YAZILMAZ; script mevcut dosyayı okuyup yalnız yeni çiftleri ekler.

Script HİÇBİR koşulda düşmez (exception atmaz); veri eksik/bozuksa o satır `"veri_eksik": true` ile yazılır, koşum devam eder.

Kullanım: python3 tools/devir-ani.py [--repo <yol>] [--sessiz] [--kuru]
Çıkış: her zaman 0 (ölçüm aygıtı; ateşlemez, hattı düşürmez). Deneysel, kaynak spec İB-75.
"""
import argparse, csv, json, os, sys
from datetime import datetime, timezone

E1 = 128_000
E2 = 600_000


def uc_degerli_ve(a, b):
    """Kleene ∧: False baskındır, sonra None, sonra True."""
    if a is False or b is False:
        return False
    if a is None or b is None:
        return None
    return True


def uc_degerli_veya(a, b):
    """Kleene ∨: True baskındır, sonra None, sonra False."""
    if a is True or b is True:
        return True
    if a is None or b is None:
        return None
    return False


def yuklem_hesapla(max_baglam):
    """DEVRET yüklemini m.38 formülüyle hesaplar; gorev_siniri hep None (türetilemez veri).
    Döner: (gorev_siniri, gorev_siniri_not, yuklem_sonucu, tetikleyen_kosul)."""
    gorev_siniri = None
    not_metni = "[?] turetilemedi: acik_isci_cagrisi/son_isci_donusu/yarim_kanon_yazimi kaynakta yok"

    if max_baglam >= E2:
        return gorev_siniri, not_metni, True, "E2-son-care"

    if max_baglam < E1:
        # (baglam>=E1 ∧ gorev_siniri) = False (>=E1 kolu False) ; (baglam>=E2) = False → False ∨ False = False
        return gorev_siniri, not_metni, False, "esik-alti"

    # E1 <= max_baglam < E2: (True ∧ None) ∨ False = None ∨ False = None
    sol = uc_degerli_ve(True, gorev_siniri)
    sonuc = uc_degerli_veya(sol, False)
    return gorev_siniri, not_metni, sonuc, "E1-asildi-gorev-siniri-bilinmiyor"


def satir_uret(row):
    """Bir v_baglam_seyri.csv satırından devir-ani-olay kaydı üretir; veri eksikse veri_eksik=true ile döner."""
    ts = datetime.now(timezone.utc).isoformat()
    oturum = row.get("oturum_kisa") or ""
    tarih = row.get("tarih") or ""
    model = row.get("model") or ""

    try:
        max_baglam = int(row.get("max_baglam", ""))
        tur_128k = int(row.get("tur_128k_ustu", ""))
    except (TypeError, ValueError):
        return {
            "ts": ts, "oturum": oturum, "tarih": tarih, "model": model,
            "max_baglam": None, "tur_128k_ustu": None, "E1": E1, "E2": E2,
            "gorev_siniri": None, "gorev_siniri_not": "veri eksik/bozuk: max_baglam/tur_128k_ustu okunamadı",
            "yuklem_sonucu": None, "tetikleyen_kosul": "veri-eksik", "atesleme": False,
            "kaynak": "v_baglam_seyri", "veri_eksik": True,
        }

    gorev_siniri, gs_not, sonuc, tetik = yuklem_hesapla(max_baglam)
    return {
        "ts": ts, "oturum": oturum, "tarih": tarih, "model": model,
        "max_baglam": max_baglam, "tur_128k_ustu": tur_128k, "E1": E1, "E2": E2,
        "gorev_siniri": gorev_siniri, "gorev_siniri_not": gs_not,
        "yuklem_sonucu": sonuc, "tetikleyen_kosul": tetik, "atesleme": False,
        "kaynak": "v_baglam_seyri", "veri_eksik": False,
    }


def mevcut_anahtarlari_oku(cikti_yolu):
    """Çıktı dosyasındaki mevcut (oturum, max_baglam) çiftlerini okur (idempotens için)."""
    anahtarlar = set()
    if not os.path.exists(cikti_yolu):
        return anahtarlar
    try:
        with open(cikti_yolu, encoding="utf-8") as f:
            for satir in f:
                satir = satir.strip()
                if not satir:
                    continue
                try:
                    d = json.loads(satir)
                except Exception:
                    continue
                anahtarlar.add((d.get("oturum"), d.get("max_baglam")))
    except Exception:
        pass
    return anahtarlar


def calistir(repo, sessiz=False, kuru=False):
    """Ana koşum: v_baglam_seyri.csv'yi okur, yeni (oturum, max_baglam) çiftlerini devir-ani-olay.jsonl'a ekler.
    Döner: (yeni_sayisi, mevcut_sayisi, dagilim) — dagilim = {"true": n, "false": n, "none": n}."""
    girdi_yolu = os.path.join(repo, "veri", "gorunum", "v_baglam_seyri.csv")
    cikti_yolu = os.path.join(repo, "veri", "bronz", "devir-ani-olay.jsonl")

    dagilim = {"true": 0, "false": 0, "none": 0}
    if not os.path.exists(girdi_yolu):
        if not sessiz:
            print("UYARI: girdi yok: %s" % girdi_yolu, file=sys.stderr)
        return 0, 0, dagilim

    mevcut = mevcut_anahtarlari_oku(cikti_yolu)
    yeni_satirlar = []
    yeni_sayisi = 0
    mevcut_sayisi = 0

    try:
        with open(girdi_yolu, encoding="utf-8") as f:
            okuyucu = csv.DictReader(f)
            for row in okuyucu:
                try:
                    kayit = satir_uret(row)
                except Exception as e:
                    kayit = {
                        "ts": datetime.now(timezone.utc).isoformat(),
                        "oturum": row.get("oturum_kisa"), "tarih": row.get("tarih"), "model": row.get("model"),
                        "max_baglam": None, "tur_128k_ustu": None, "E1": E1, "E2": E2,
                        "gorev_siniri": None, "gorev_siniri_not": "beklenmeyen hata: %r" % e,
                        "yuklem_sonucu": None, "tetikleyen_kosul": "hata", "atesleme": False,
                        "kaynak": "v_baglam_seyri", "veri_eksik": True,
                    }
                anahtar = (kayit.get("oturum"), kayit.get("max_baglam"))
                if anahtar in mevcut:
                    mevcut_sayisi += 1
                    continue
                mevcut.add(anahtar)
                yeni_satirlar.append(kayit)
                yeni_sayisi += 1
                sonuc = kayit.get("yuklem_sonucu")
                if sonuc is True:
                    dagilim["true"] += 1
                elif sonuc is False:
                    dagilim["false"] += 1
                else:
                    dagilim["none"] += 1
    except Exception as e:
        if not sessiz:
            print("UYARI: girdi okunamadı: %r" % e, file=sys.stderr)
        return 0, 0, dagilim

    if not kuru and yeni_satirlar:
        os.makedirs(os.path.dirname(cikti_yolu), exist_ok=True)
        with open(cikti_yolu, "a", encoding="utf-8") as f:
            for kayit in yeni_satirlar:
                f.write(json.dumps(kayit, ensure_ascii=False) + "\n")

    return yeni_sayisi, mevcut_sayisi, dagilim


def main():
    ap = argparse.ArgumentParser(description="devir-ani.py — devir-anı yüklemi ölçüm aygıtı (yalnız loglar, ateşlemez)")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--sessiz", action="store_true", help="özet basma")
    ap.add_argument("--kuru", action="store_true", help="dosyaya yazma, yalnız özet")
    a = ap.parse_args()

    yeni, mevcut, dagilim = calistir(a.repo, sessiz=a.sessiz, kuru=a.kuru)

    if not a.sessiz:
        print("devir-ani: yeni=%d mevcut(atlanan)=%d | dagilim True=%d False=%d None=%d%s" % (
            yeni, mevcut, dagilim["true"], dagilim["false"], dagilim["none"],
            " [KURU: yazilmadi]" if a.kuru else ""))

    return 0


if __name__ == "__main__":
    sys.exit(main())
