#!/usr/bin/env python3
"""wiki-baglanti.py — WIKI NOT EVRİMİ: [[link]] grafı + deterministik KARŞI-LİNK geri-güncellemesi (KB-45 (a) = Karar 60, 08-21: A-MEM 'not evrimi'
— yeni kayıt eski sayfaların bağlantı/süpersede/etiket satırını deterministik günceller; anahtar-kaydı §1.6 cascade ilkesinin wiki karşılığı; icra İB-45,
2026-08-22 seans-14). STDLIB ONLY; LLM yok; silme yok (m.8): yalnız EKLEME (karşı-link satıra eklenir ya da satır yoksa sayfa sonuna bir
`**Bağlantılar:**` satırı açılır).

Ne yapar: wiki/*.md tarar → her sayfadaki [[ad]] bağları (kendine bağ hariç; sozluk.md DONDU — ne okunur ne yazılır) → A→B bağı varsa B'de [[A]]
karşı-linki bekler; yoksa ADAY. Varsayılan KURU (rapor); `--uygula` yazar. Kırık [[link]] (hedef sayfa yok) listelenir (yazılmaz). YETİM ölçümü:
silver `silver_kuyruk` T-B-YETIM hedef dosyalarından wiki sayfalarının doğrudan yol verdiği (`wiki/…`, `kuyruk/…` vb.) dosyalar = "pointer kazandı" adayı
(silver-saglik sonraki koşumda kapatır) — güncellenen sayfa / kapanan yetim sayacı (KB-45 ölçüm). Kütük: `veri/wiki-baglanti.jsonl` APPEND (1 satır = 1 koşum özeti).
Kullanım: python3 tools/wiki-baglanti.py [--repo <yol>] [--uygula] [--sessiz] [--json]
Çıkış: 0 · 2 wiki dizini yok. Deneysel m.29.
"""
import argparse, glob, json, os, re, sqlite3, subprocess, sys
from datetime import datetime, timezone

LINK_RX = re.compile(r"\[\[([^\]\|#]+?)(?:[\|#][^\]]*)?\]\]")
BAG_SATIR_RX = re.compile(r"^\*\*(Bağlantılar|\[\[link\]\]'ler|Bağlantı)[^:]*:\*\*", re.M)
DONMUS = {"sozluk", "README"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.getcwd()); ap.add_argument("--uygula", action="store_true")
    ap.add_argument("--sessiz", action="store_true"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args(); repo = os.path.abspath(a.repo); wdir = os.path.join(repo, "wiki")
    if not os.path.isdir(wdir):
        sys.exit("[HATA] wiki dizini yok")
    sayfalar = {}
    for p in sorted(glob.glob(os.path.join(wdir, "*.md"))):
        ad = os.path.splitext(os.path.basename(p))[0]
        with open(p, encoding="utf-8") as fh:
            sayfalar[ad] = fh.read()
    adlar = set(sayfalar)
    ETIKET = ("link", "ad", "wiki-link")  # "**[[link]]'ler:**" gibi ŞABLON etiketleri bağ değildir
    giden = {ad: sorted({m.group(1).strip() for m in LINK_RX.finditer(t) if m.group(1).strip() != ad and m.group(1).strip() not in ETIKET}) for ad, t in sayfalar.items()}
    kirik, aday = [], []
    for kaynak, hedefler in giden.items():
        if kaynak in DONMUS:
            continue
        for h in hedefler:
            if h not in adlar:
                kirik.append((kaynak, h)); continue
            if h in DONMUS:
                continue
            if kaynak not in giden.get(h, []):
                aday.append((h, kaynak))  # h sayfasına [[kaynak]] karşı-linki
    yazilan = []
    if a.uygula:
        grup = {}
        for hedef, kaynak in aday:
            grup.setdefault(hedef, []).append(kaynak)
        for hedef, kaynaklar in sorted(grup.items()):
            t = sayfalar[hedef]
            ek = " · " + " · ".join("[[%s]] (karşı-link %s)" % (k, datetime.now().strftime("%m-%d")) for k in sorted(kaynaklar))
            m = BAG_SATIR_RX.search(t)
            if m:
                satir_son = t.find("\n", m.start()); satir_son = len(t) if satir_son == -1 else satir_son
                t2 = t[:satir_son] + ek + t[satir_son:]
            else:
                t2 = t.rstrip("\n") + "\n\n**Bağlantılar:**" + ek + "\n"
            with open(os.path.join(wdir, hedef + ".md"), "w", encoding="utf-8") as fh:
                fh.write(t2)
            yazilan.append(hedef)
    # YETİM ölçümü
    yetim_pointer = []
    db = os.path.join(repo, "veri", "baglam.sqlite")
    if os.path.exists(db):
        try:
            con = sqlite3.connect("file:%s?mode=ro" % db, uri=True)
            yetimler = [r[0] for r in con.execute("SELECT hedef_id FROM silver_kuyruk WHERE tip='T-B-YETIM'")]
            con.close()
            tum_metin = "\n".join(sayfalar.values())
            yetim_pointer = [y for y in yetimler if y in tum_metin]
        except sqlite3.Error:
            pass
    try:
        head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip()
    except Exception:
        head = "?"
    ozet = {"ts": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"), "head": head, "sayfa": len(sayfalar), "bag": sum(len(v) for v in giden.values()),
            "karsi_link_aday": len(aday), "yazilan_sayfa": len(yazilan), "kirik_link": len(kirik), "yetim_pointer_kazanan": len(yetim_pointer), "uygula": a.uygula}
    if a.uygula:
        with open(os.path.join(repo, "veri", "wiki-baglanti.jsonl"), "a", encoding="utf-8") as fh:
            fh.write(json.dumps({**ozet, "yazilan": yazilan, "kirik": kirik}, ensure_ascii=False) + "\n")
    if a.json:
        print(json.dumps({**ozet, "aday": aday, "kirik": kirik, "yazilan": yazilan, "yetim_pointer": yetim_pointer}, ensure_ascii=False, indent=1))
    else:
        print("wiki-baglanti @ %s: %d sayfa · %d bağ · karşı-link adayı %d · yazılan %d · kırık [[link]] %d · yetim→pointer %d%s" % (
            head, ozet["sayfa"], ozet["bag"], ozet["karsi_link_aday"], ozet["yazilan_sayfa"], ozet["kirik_link"], ozet["yetim_pointer_kazanan"], "" if a.uygula else " · KURU (--uygula yazar)"))
        if not a.sessiz:
            for h, k in aday[:30]: print("  karşı-link: %s ← [[%s]]" % (h, k))
            for k, h in kirik[:20]: print("  kırık: %s → [[%s]] (sayfa yok)" % (k, h))
    sys.exit(0)


if __name__ == "__main__":
    main()
