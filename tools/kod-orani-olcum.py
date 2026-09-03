#!/usr/bin/env python3
"""kod-orani-olcum.py — İB-71 baseline ölçümü: repo-genel içerik oranı ↔ bağlam-penceresi (Salih'in son 3 gün
okuduğu dosyalar) oranı arasındaki fark, DÖRT kovaya ayrılarak (md · kod · yapisal · diger).

Ne bu: iki ayrı ölçüm üretir —
  (i) REPO ENVANTERİ: ~/jarvis altındaki (`.git`, `veri/bronz`, `veri/gorunum` HARİÇ) her dosyayı uzantısına göre
      kovaya koyar (md=.md · kod=.py/.sh/.sql · yapisal=.json/.jsonl/.csv · diger=geri kalan), kova başına
      dosya sayısı + toplam satır (\\n bayt sayımı — ikili dosyada da güvenli, exception atmaz) + toplam bayt.
  (ii) BAĞLAM-PENCERESİ PROXY'Sİ: `veri/bronz/hareket-olay.jsonl` (şema: hareket_id/ts/oturum/arac/girdi_ozet/
      dosya/repo_ici/sonuc/model/kaynak_dosya/yuklendi_head/okuma_tipi — gerçek veriden çıkarıldı, tahmin
      edilmedi) son N=3 gün penceresindeki dosya-okuma olaylarını tarar: `arac=="Read"` ∧ `dosya` doluysa o
      yol doğrudan sayılır; `arac=="Bash"` içinde cat/head/tail/sed/less/more/nl/awk komutlarının ARDINDAN
      geçen uzantılı path-benzeri token'lar HEURİSTİK regex'le çıkarılır (docstring'te işaretli — bu bir
      kesin ayrıştırıcı değildir, AXI A6 salt-okur sınıfı). Kütükte satır-bazlı okuma miktarı alanı YOK
      (okuma_tipi yalnız aralik/bütün bilgisi taşır, satır sayısı değil) → ağırlık dosya-sayımı (1 olay = 1
      sayım), görev metninin "yoksa dosya-sayımı olarak say" dalı.

Grain: 1 koşum = 1 çıktı satırı (`veri/kod-orani.jsonl`, append-only).

Modlar: `--json` (AXI A1: stdout tek JSON nesnesi, insan satırları stderr) · `--pencere-gun N` (varsayılan 3) ·
`--bugun YYYY-MM-DD` (A3 determinizm için zaman enjeksiyonu — yoksa sistem bugünü) · `--kuru` (kütüğe yazmaz).

Kullanım: `python3 tools/kod-orani-olcum.py [--pencere-gun 3] [--bugun 2026-09-03] [--kuru] [--json] [--sessiz]`

Çıkış: 0 tamam · 2 girdi/kullanım hatası (A2 sözlüğü; hareket-olay.jsonl yoksa ya da bilinmeyen bayrak).

Yan-etki (A6): EKLEMELİ — yalnız `veri/kod-orani.jsonl`e append-only tek satır yazar (--kuru ile yazmaz);
başka hiçbir dosyaya dokunmaz, salt-okur tarama.

Kayıt: İB-71 (Salih 09-03), Carvis yan-oturum işçi-ajanı.
"""
import argparse
import json
import os
import re
import subprocess
import sys
from datetime import date, timedelta

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KUTUK = os.path.join(KOK, "veri", "kod-orani.jsonl")
HAREKET_KUTUK = os.path.join(KOK, "veri", "bronz", "hareket-olay.jsonl")

DISLA_DIZIN = {".git", os.path.join("veri", "bronz"), os.path.join("veri", "gorunum"),
               os.path.join("kuyruk", "arsiv", "karantina")}  # İB-72: karantina dizini tarama-dışı (m.8 arşiv, tekrar-sayılmaz)

UZANTI_KOVA = {
    ".md": "md",
    ".py": "kod",
    ".sh": "kod",
    ".sql": "kod",
    ".json": "yapisal",
    ".jsonl": "yapisal",
    ".csv": "yapisal",
}

OKUMA_KOMUT_RX = re.compile(r"\b(cat|head|tail|sed|less|more|nl|awk)\b([^|;&\n]*)")
PATH_TOKEN_RX = re.compile(r"[A-Za-z0-9_./\-]+\.[A-Za-z0-9]+")


def kova_ver(yol):
    _, uzanti = os.path.splitext(yol)
    return UZANTI_KOVA.get(uzanti.lower(), "diger")


def bos_oran():
    return {
        "md_satir": 0, "md_dosya": 0,
        "kod_satir": 0, "kod_dosya": 0,
        "yapisal_satir": 0, "yapisal_dosya": 0,
        "diger_satir": 0, "diger_dosya": 0,
    }


def satir_say(tam_yol):
    """İkili/metin ayrımı yapmadan \\n bayt sayımı — exception atmaz (A7: dosya okunamazsa 0 döner, HATA
    olarak sayılmaz çünkü envanter amaçlı yaklaşık ölçüm; okunamayan dosya sayısı ayrı raporlanır)."""
    try:
        with open(tam_yol, "rb") as f:
            veri = f.read()
        n = veri.count(b"\n")
        if veri and not veri.endswith(b"\n"):
            n += 1
        return n
    except OSError:
        return 0


def repo_envanteri(kok):
    oran = bos_oran()
    okunamayan = 0
    for kok_dizin, alt_dizinler, dosyalar in os.walk(kok):
        goreli_dizin = os.path.relpath(kok_dizin, kok)
        if goreli_dizin == ".":
            goreli_dizin = ""
        # dışlanan dizinleri budama (os.walk alt_dizinler listesi yerinde değiştirilirse iner)
        yeni_alt = []
        for d in alt_dizinler:
            aday = os.path.join(goreli_dizin, d) if goreli_dizin else d
            if d == ".git" or aday in DISLA_DIZIN:
                continue
            yeni_alt.append(d)
        alt_dizinler[:] = yeni_alt
        for ad in dosyalar:
            tam_yol = os.path.join(kok_dizin, ad)
            k = kova_ver(ad)
            oran[k + "_dosya"] += 1
            try:
                bayt = os.path.getsize(tam_yol)
            except OSError:
                okunamayan += 1
                continue
            oran[k + "_bayt"] = oran.get(k + "_bayt", 0) + bayt
            oran[k + "_satir"] += satir_say(tam_yol)
    return oran, okunamayan


def hareket_olaylarini_oku(yol):
    if not os.path.isfile(yol):
        sys.exit("HATA: hareket kütüğü bulunamadı: %s (kod 2)" % yol)
    olaylar = []
    with open(yol, "r", encoding="utf-8") as f:
        for satir_no, satir in enumerate(f, 1):
            satir = satir.strip()
            if not satir or satir.startswith("#"):
                continue
            try:
                olaylar.append(json.loads(satir))
            except json.JSONDecodeError:
                sys.exit("HATA: hareket-olay.jsonl satır %d bozuk JSON (kod 2)" % satir_no)
    return olaylar


def bash_dosyalarini_cikar(girdi_ozet):
    if not girdi_ozet:
        return []
    komut_bolumu = girdi_ozet
    if "⟨" in girdi_ozet and "⟩" in girdi_ozet:
        komut_bolumu = girdi_ozet.split("⟨", 1)[1].rsplit("⟩", 1)[0]
    yollar = []
    for _komut, kuyruk in OKUMA_KOMUT_RX.findall(komut_bolumu):
        for token in PATH_TOKEN_RX.findall(kuyruk):
            if token.startswith("-"):
                continue
            yollar.append(token)
    return yollar


def baglam_penceresi_orani(olaylar, pencere_gun, bugun):
    esik = (bugun - timedelta(days=pencere_gun)).isoformat()
    oran = bos_oran()
    olay_n = 0
    for o in olaylar:
        ts = o.get("ts") or ""
        if ts[:10] < esik:
            continue
        arac = o.get("arac")
        yollar = []
        if arac == "Read" and o.get("dosya"):
            yollar = [o["dosya"]]
        elif arac == "Bash":
            yollar = bash_dosyalarini_cikar(o.get("girdi_ozet"))
        for yol in yollar:
            k = kova_ver(yol)
            oran[k + "_dosya"] += 1
            olay_n += 1
    return oran, olay_n, esik


def git_head(kok):
    try:
        r = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=kok,
                            capture_output=True, text=True, timeout=10)
        if r.returncode == 0:
            return r.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    return "bilinmiyor"


def satir_ozet(oran):
    toplam = oran["md_satir"] + oran["kod_satir"] + oran["yapisal_satir"] + oran["diger_satir"]
    return toplam


def ana():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=KOK, help="repo kökü (varsayılan: bu dosyanın üst-üst dizini)")
    ap.add_argument("--pencere-gun", type=int, default=3, help="bağlam-penceresi gün sayısı (varsayılan 3)")
    ap.add_argument("--bugun", default=None, help="YYYY-MM-DD determinizm damgası (yoksa sistem bugünü)")
    ap.add_argument("--kuru", action="store_true", help="kütüğe yazma (prova)")
    ap.add_argument("--json", action="store_true", help="stdout = tek JSON nesnesi (A1)")
    ap.add_argument("--sessiz", action="store_true", help="insan çıktısını kıs")
    a = ap.parse_args()

    insan = sys.stderr if a.json else sys.stdout

    if a.bugun:
        try:
            bugun = date.fromisoformat(a.bugun)
        except ValueError:
            sys.exit("HATA: --bugun YYYY-MM-DD biçiminde olmalı (kod 2)")
    else:
        bugun = date.today()

    kok = os.path.abspath(a.repo)
    if not os.path.isdir(kok):
        sys.exit("HATA: --repo dizini yok: %s (kod 2)" % kok)

    repo_oran, okunamayan = repo_envanteri(kok)
    olaylar = hareket_olaylarini_oku(os.path.join(kok, "veri", "bronz", "hareket-olay.jsonl"))
    baglam_oran, olay_n, esik = baglam_penceresi_orani(olaylar, a.pencere_gun, bugun)

    head = git_head(kok)
    satir = {
        "tarih": bugun.isoformat(),
        "git_head": head,
        "repo_orani": repo_oran,
        "baglam_orani": baglam_oran,
    }

    yazildi = False
    if not a.kuru:
        os.makedirs(os.path.dirname(KUTUK), exist_ok=True)
        with open(KUTUK, "a", encoding="utf-8") as f:
            f.write(json.dumps(satir, ensure_ascii=False) + "\n")
        yazildi = True

    if not a.sessiz:
        print("kod-orani-olcum — AS-OF %s (git_head %s)" % (bugun.isoformat(), head), file=insan)
        print("  repo envanteri (%s dosya okunamadı):" % okunamayan, file=insan)
        for k in ("md", "kod", "yapisal", "diger"):
            print("    %-8s dosya=%-5d satir=%-8d bayt=%d" % (
                k, repo_oran[k + "_dosya"], repo_oran[k + "_satir"], repo_oran.get(k + "_bayt", 0)), file=insan)
        print("  baglam penceresi (son %d gün, esik>=%s, %d okuma-olayı):" % (a.pencere_gun, esik, olay_n), file=insan)
        for k in ("md", "kod", "yapisal", "diger"):
            print("    %-8s dosya=%d" % (k, baglam_oran[k + "_dosya"]), file=insan)
        print("  kütük: %s" % ("yazıldı" if yazildi else "--kuru (yazılmadı)"), file=insan)

    if a.json:
        cikti = {
            "arac": "kod-orani-olcum",
            "surum": "0.1",
            "git_head": head,
            "cikis": 0,
            "kayit": satir,
            "okunamayan_dosya_n": okunamayan,
            "baglam_olay_n": olay_n,
            "kutuk_yazildi": yazildi,
        }
        print(json.dumps(cikti, ensure_ascii=False))

    return 0


if __name__ == "__main__":
    sys.exit(ana())
