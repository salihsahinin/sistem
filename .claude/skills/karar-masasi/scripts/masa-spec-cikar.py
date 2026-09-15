#!/usr/bin/env python3
"""karar-masasi · tersine araç: elle yazılmış eski masa HTML'ini (7.-12. masa biçimi) spec JSON'a döker (İB-88 P2, 09-15).
Amaç: E3 eşdeğerlik testi (elle masa → spec → masa-uret.py → sayım karşılaştırması) ve eski masaların spec arşivi.
Kullanım: python3 masa-spec-cikar.py <masa.html> [--no 12] [--karar "Karar 96"] > spec.json
Çıkış: 0 üretildi · 2 HTML biçimi tanınmadı (başlık/kalem bulunamadı). Kanona yazmaz, stdout'a basar.
Sınır: satır-içi etiketler (<code>, <em>) metin içinde korunur; header giriş cümlesi `giris` alanına düşer.
"""
import argparse, html, json, re, sys

def strip(x):
    return re.sub(r"\s+", " ", x or "").strip()

def cikar(h, no=None, karar=None):
    b = re.search(r'<h1 class="card-title text-2xl">Karar Masası (\S+) — (.*?) <span', h, re.S)
    if not b:
        return None
    no_html, baslik = b.group(1), strip(b.group(2))
    tetik_m = re.search(r"Tetik: <em>(.*?)</em>", h, re.S)
    giris_m = re.search(r'<p class="text-sm opacity-80">(.*?)Tetik: <em>', h, re.S)
    once = re.search(r"fiilen yapıldı[^<]*</strong>\s*(.*?)</p>", h, re.S)
    asof = re.search(r"AS-OF (.*?) ·", h)
    kanit = []
    tb = re.search(r"<tbody>(.*?)</tbody>", h, re.S)
    for tr in re.findall(r"<tr>(.*?)</tr>", tb.group(1) if tb else "", re.S):
        td = re.findall(r"<td>(.*?)</td>", tr, re.S)
        if len(td) < 3:
            continue
        m = re.match(r"(.*?) · <strong>(.*?)</strong>", td[2], re.S)
        kanit.append({"bulgu": strip(td[0]), "deger": strip(td[1]),
                      "kaynak": strip(m.group(1)) if m else strip(td[2]), "etiket": strip(m.group(2)) if m else ""})
    hakem = re.search(r'<section class="card bg-base-100 shadow-md hakem">.*?<p class="text-sm opacity-80">(.*?)</p>', h, re.S)
    kalemler = []
    for kid, body in re.findall(r'<section class="card bg-base-100 shadow-md" data-lavish-question="(\w+)">(.*?)</section>', h, re.S):
        t = re.search(r'<h2 class="card-title">\w+ · (.*?) <span class="badge badge-outline">(.*?)</span>', body, re.S)
        nd = re.search(r"<strong>Ne demek:</strong> (.*?)</p>", body, re.S)
        secs = []
        for cls, val, rest in re.findall(r'<label class="(opt[^"]*)"[^>]*><input type="\w+" name="secim" value="(.*?)">(.*?)</label>', body, re.S):
            et = re.search(r"<strong>(.*?)</strong>", rest, re.S)
            ac = re.search(r"<div[^>]*>(.*?)</div>", rest, re.S)
            secs.append({"etiket": strip(et.group(1)) if et else "", "value": html.unescape(val), "oneri": "oneri" in cls,
                         "aciklama": strip(ac.group(1)) if ac else strip(re.sub(r"<strong>.*?</strong>", "", rest, flags=re.S))})
        kalemler.append({"id": kid, "baslik": strip(t.group(1)) if t else kid, "rozet": strip(t.group(2)) if t else "",
                         "ne_demek": strip(nd.group(1)) if nd else "", "coklu": "kuyruklaCoklu" in body, "secenekler": secs})
    if not kalemler:
        return None
    tarih = re.search(r"\((\d{4}-\d{2}-\d{2})\)</title>", h)
    return {"no": no if no is not None else (int(no_html) if no_html.isdigit() else no_html),
            "tarih": tarih.group(1) if tarih else "", "baslik": baslik,
            "giris": strip(giris_m.group(1)) if giris_m else "", "tetik": strip(tetik_m.group(1)) if tetik_m else "",
            "once_yapildi": strip(once.group(1)) if once else "—", "asof": asof.group(1) if asof else "",
            "kanit": kanit, "hakem": strip(hakem.group(1)) if hakem else "", "kalemler": kalemler,
            "karar_no": karar or "sonraki Karar", "ustune_yaz": True}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("html"); ap.add_argument("--no", type=int); ap.add_argument("--karar")
    a = ap.parse_args()
    spec = cikar(open(a.html, encoding="utf-8").read(), a.no, a.karar)
    if spec is None:
        print("HTML biçimi tanınmadı (başlık ya da kalem yok)", file=sys.stderr); sys.exit(2)
    json.dump(spec, sys.stdout, ensure_ascii=False, indent=1); print()

if __name__ == "__main__":
    main()
