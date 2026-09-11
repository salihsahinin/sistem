#!/usr/bin/env python3
"""İB-81 kuru-koşum aracı: tüzükteki SÜPERSEDE / REVİZE / EK izlerini madde bazında sayar,
çelişki-adayı madde çiftlerini (ortak anahtar-terim ∧ ikisinde de iz) listeler.
Kanona YAZMAZ; yalnız rapor (md) üretir. Karar-modeli M7-2 (2026-09-11) Model A + B kesişimi:
yazım madde-bazlı, çelişki taraması global ve deterministik.

Kullanım: python3 tools/tuzuk-iz-tarama.py [--tuzuk core/tuzuk-v0.md] [--cikti raporlar/...md]
"""
import argparse, re, itertools, datetime, pathlib

IZ = re.compile(r"SÜPERSEDE|REVİZE|\bEK(?:-\d+)?\b|~~")
MADDE = re.compile(r"^(\d+)\.\s+\*\*(.+?)\*\*")
DURAK = set(("ve ile için bir bu da de her yok var olan olarak sonra önce kural karar salih jarvis carvis imzası kaynak "
             "değil değildir beyanı kalır fable ana-sıra hükmü kararı kayıt kuyruk ayrıca yalnız kadar sabit emekli eşiği görev masası "
             "ancak açılır başına başlar canlı gerekçe bloğu claude görünür formunda geri-açma revize ilkesi kuralı seans oturum "
             "günaydın vardiyası katman-1 katman-2 aynen madde defter arşiv pointer tarih").split())

def anahtar(metin: str) -> set:
    kelimeler = re.findall(r"[a-zçğıöşü\-]{5,}", metin.lower())
    return {k for k in kelimeler if k not in DURAK}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tuzuk", default="core/tuzuk-v0.md")
    ap.add_argument("--cikti", default=None)
    a = ap.parse_args()
    satirlar = pathlib.Path(a.tuzuk).read_text(encoding="utf-8").splitlines()
    maddeler = []  # (no, baslik, satir_no, metin)
    for i, s in enumerate(satirlar, 1):
        m = MADDE.match(s)
        if m:
            maddeler.append((int(m.group(1)), m.group(2), i, s))
    izli = []
    for no, baslik, ln, metin in maddeler:
        izler = IZ.findall(metin)
        if izler:
            izli.append((no, baslik, ln, len(izler), len(metin.encode())))
    # çelişki adayı: iki izli madde ≥4 ortak alan-terimi paylaşıyorsa (v0, gürültülü)
    anah = {no: anahtar(metin) for no, _, _, metin in maddeler}
    ciftler = []
    for (n1, *_), (n2, *_) in itertools.combinations(izli, 2):
        ortak = anah[n1] & anah[n2]
        if len(ortak) >= 4:
            ciftler.append((n1, n2, sorted(ortak)[:6]))
    toplam_b = sum(len(s.encode()) for s in satirlar)
    bugun = datetime.date.today().isoformat()
    out = [f"# İB-81 kuru koşum — tüzük iz taraması ({bugun}, deneysel m.29; kanona yazılmadı)",
           "", f"*Kaynak `{a.tuzuk}` · {len(maddeler)} madde · {toplam_b/1024:.1f} KB · üreten `tools/tuzuk-iz-tarama.py` (deterministik). "
           "İz = SÜPERSEDE / REVİZE / EK / üstü-çizili. Çelişki adayı = iki izli madde ≥3 ortak alan-terimi (durak sözcükler dışı) — v0 GÜRÜLTÜLÜ: sözcük örtüşmesi çelişki DEĞİL, yalnız okuma sırası önerir; hüküm Salih'in.*", "",
           "## İzli maddeler (tek hükme inme adayları)", "", "| m. | başlık | satır | iz | bayt | öneri |", "|---|---|---|---|---|---|"]
    for no, baslik, ln, k, b in sorted(izli, key=lambda x: (-x[3], -x[4])):
        oneri = "tek hüküm + arşiv-pointer" if k >= 2 or b > 1500 else "bekle (tek iz, küçük)"
        out.append(f"| m.{no} | {baslik[:60]} | {ln} | {k} | {b} | {oneri} |")
    out += ["", f"Toplam izli madde: {len(izli)} / {len(maddeler)} · iz toplamı: {sum(x[3] for x in izli)}", "",
            "## Çelişki adayı çiftler (deterministik, ortak alan-terimi ≥4)", ""]
    if ciftler:
        out += ["| çift | ortak terimler |", "|---|---|"]
        out += [f"| m.{a1} ↔ m.{a2} | {', '.join(t)} |" for a1, a2, t in ciftler]
    else:
        out.append("aday yok")
    out += ["", "## Usul", "- Uygulama: madde başına tek commit `[damıtma]`; eski metin `arsiv/tuzuk-madde-arsivi-YYYY-MM-DD.md`'ye iner (m.8).",
            "- Şeffaflık (Salih 09-10 şartı): uygulanan maddenin son 5 seansta hangi oturumda yüklendiği `hareket` tablosundan (Read + dosya=tüzük, okuma_tipi) rapora eklenir."]
    metin = "\n".join(out) + "\n"
    if a.cikti:
        pathlib.Path(a.cikti).write_text(metin, encoding="utf-8")
        print(f"yazıldı: {a.cikti} · izli {len(izli)} · çift {len(ciftler)}")
    else:
        print(metin)

if __name__ == "__main__":
    main()
