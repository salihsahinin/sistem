#!/usr/bin/env python3
"""pano-akis.py — Kanban 4 akış metriği: WIP · throughput · cycle time · kart yaşı (İB-41 icrası, 2026-08-21).

Kaynak karar: KB-46 A (Salih 08-21, defter Karar 49; pano şablon v3 eki) — akış görünümü `v_pano_akis`,
deterministik sayım. Metrik kaynağı agile atlası `cc/rapor-2026-08-17-3.md`.

Ne yapar (tamamı `core/pano.md`'nin kart satırlarından, deterministik):
  - WIP            = AKTİF bölümündeki kart sayısı
  - kart yaşı      = bugün − Açılış (AKTİF/BEKLEYEN/BLOKE kartlarında, gün)
  - throughput     = SON BİTEN'de kapanış tarihi son 7/30 güne düşen TEKİL kayıtlar
                     ("**K-xxx KAPANDI (MM-DD …)**" satırları; toplu arşiv satırları tarih-tekil
                     olmadığından SAYIM DIŞI bırakılır ve adet olarak beyan edilir — m.39, uydurma yok)
  - cycle time     = Started → kapanış (Karar 49: Started damgası yeni kartlarda zorunlu, mevcutlara
                     geriye dönük UYDURULMAZ → Started'sız kartta cycle HESAPLANMAZ, "—" kalır;
                     görünüm ilk Started'lı kapanışlarla anlam kazanır — ledger İB-41 notu)

Çıktı: gold CSV `veri/gorunum/v_pano_akis.csv` (kart-bazlı) + stdout özet bloğu.
Sınırlar (yazılı): pano tarihleri MM-DD biçimli — yıl 2026 varsayılır (yıl dönümünde betik güncellenmeli);
Started kolonu panoda henüz yoksa tüm satırlarda "—". FAIL-LOUD: pano bölüm/tablo başlığı bulunamazsa çıkış 2.

Koşum: python3 tools/pano-akis.py [--pano core/pano.md] [--csv veri/gorunum/v_pano_akis.csv]
                                  [--bugun YYYY-MM-DD]   (test/tekrar-üretim için tarih enjeksiyonu)
stdlib-only. Çıkış: 0 · 2 pano parse edilemedi.
"""
import argparse, csv, os, re, sys
from datetime import date

YIL = 2026  # pano tarihleri MM-DD; yıl varsayımı (yıl dönümünde güncellenir)

def t2date(mmdd):
    m = re.fullmatch(r"(\d{2})-(\d{2})", mmdd or "")
    if not m:
        return None
    try:
        return date(YIL, int(m.group(1)), int(m.group(2)))
    except ValueError:
        return None

def tablo_ayir(satirlar):
    """Bölüm başlığı → o bölümün tablo satırları (hücre listeleri)."""
    bolum, sonuc = None, {}
    for s in satirlar:
        b = re.match(r"##\s+(.+?)\s*$", s)
        if b:
            bolum = b.group(1).strip()
            sonuc.setdefault(bolum, [])
            continue
        if bolum and s.lstrip().startswith("|"):
            hucre = [h.strip() for h in s.strip().strip("|").split("|")]
            sonuc[bolum].append(hucre)
    return sonuc

def kart_satirlari(tablo, bolum_adi):
    """Header'dan 'Açılış'/'Started' kolon indeksini bulur; kart satırlarını (no, açılış, started) döndürür."""
    satirlar = tablo.get(bolum_adi, [])
    if not satirlar:
        return None
    header = satirlar[0]
    try:
        i_ac = next(i for i, h in enumerate(header) if "Açılış" in h)
    except StopIteration:
        return None
    i_st = next((i for i, h in enumerate(header) if "Started" in h), None)
    kartlar = []
    for h in satirlar[1:]:
        if not h or not re.match(r"K-\d+", h[0]):
            continue
        acilis = h[i_ac] if i_ac < len(h) else ""
        started = h[i_st] if (i_st is not None and i_st < len(h)) else "—"
        kartlar.append((h[0].split()[0], acilis, started))
    return kartlar

def main():
    p = argparse.ArgumentParser(description="v_pano_akis — Kanban akış metrikleri (İB-41)")
    p.add_argument("--pano", default="core/pano.md")
    p.add_argument("--csv", default="veri/gorunum/v_pano_akis.csv")
    p.add_argument("--bugun", default=None, help="YYYY-MM-DD (varsayılan: sistem tarihi)")
    a = p.parse_args()

    bugun = date.fromisoformat(a.bugun) if a.bugun else date.today()
    try:
        satirlar = open(a.pano, encoding="utf-8").read().splitlines()
    except OSError as e:
        print(f"FAIL-LOUD: pano okunamadı: {e}", file=sys.stderr)
        return 2
    tablo = tablo_ayir(satirlar)

    kayitlar, eksik = [], []
    for bolum in ("AKTİF", "BEKLEYEN", "BLOKE"):
        kartlar = kart_satirlari(tablo, bolum)
        if kartlar is None:
            eksik.append(bolum)
            continue
        for no, acilis, started in kartlar:
            d = t2date(acilis)
            kayitlar.append({
                "kart": no, "bolum": bolum, "acilis": acilis, "started": started or "—",
                "kapanis": "", "yas_gun": (bugun - d).days if d else "",
                "cycle_gun": "",  # Started'sız hesaplanmaz (Karar 49: geriye dönük uydurma yok)
            })
    if eksik:
        print(f"FAIL-LOUD: pano bölümleri parse edilemedi: {', '.join(eksik)} — şablon değişmiş olabilir", file=sys.stderr)
        return 2

    # SON BİTEN: tekil kapanışlar + toplu arşiv beyanı
    metin = "\n".join(satirlar)
    kapanislar = re.findall(r"\*\*(K-\d+)\s+KAPANDI\s+\((\d{2}-\d{2})", metin)
    toplu = re.findall(r"Eski kapanışlar\s*\(([^)]*)\)", metin)
    toplu_kart = sum(len(re.findall(r"K-\d+", t)) for t in toplu)
    for no, mmdd in kapanislar:
        d = t2date(mmdd)
        kayitlar.append({"kart": no, "bolum": "SON BİTEN", "acilis": "", "started": "—",
                         "kapanis": mmdd, "yas_gun": "", "cycle_gun": ""})
    t7 = sum(1 for _, mmdd in kapanislar if (d := t2date(mmdd)) and (bugun - d).days <= 7)
    t30 = sum(1 for _, mmdd in kapanislar if (d := t2date(mmdd)) and (bugun - d).days <= 30)

    os.makedirs(os.path.dirname(a.csv), exist_ok=True)
    with open(a.csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["kart", "bolum", "acilis", "started", "kapanis", "yas_gun", "cycle_gun"])
        w.writeheader()
        w.writerows(kayitlar)

    wip = sum(1 for k in kayitlar if k["bolum"] == "AKTİF")
    yaslar = sorted(k["yas_gun"] for k in kayitlar if isinstance(k["yas_gun"], int))
    medyan = yaslar[len(yaslar) // 2] if yaslar else "—"
    cycle_var = [k for k in kayitlar if k["cycle_gun"] != ""]
    print(f"# v_pano_akis · {bugun} · kaynak {a.pano} (deterministik sayım; İB-41)")
    print(f"WIP (AKTİF)          : {wip}")
    print(f"BEKLEYEN / BLOKE     : {sum(1 for k in kayitlar if k['bolum']=='BEKLEYEN')} / {sum(1 for k in kayitlar if k['bolum']=='BLOKE')}")
    print(f"throughput 7g / 30g  : {t7} / {t30}  (yalnız tekil-tarihli kapanışlar: {len(kapanislar)}; arşiv-toplu {toplu_kart} kart tarih-tekil değil → sayım dışı)")
    print(f"kart yaşı medyan     : {medyan} gün  (n={len(yaslar)}; en yaşlı {yaslar[-1] if yaslar else '—'})")
    print(f"cycle time           : {'n='+str(len(cycle_var)) if cycle_var else 'veri yok — Started damgası (Karar 49) yeni kartlarda birikince hesaplanır'}")
    print(f"CSV yazıldı          : {a.csv} ({len(kayitlar)} satır)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
