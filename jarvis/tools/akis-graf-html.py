#!/usr/bin/env python3
"""Akış grafını (ortak/akis-graf.json) tıklanabilir HTML'e döker.

Zenginleştirme: her düğüme kütük olayları (ortak/durum-olay.jsonl: kanıt, oturum),
oturum kayıt JSON'u (raporlar/seans/*.json: ne_degisti, kararlar, sapma…), canlı
oturum özeti (raporlar/seans/seans-canli-<oturum>.json) ve karar defteri paragrafı
(kuyruk/senaryo-defteri.md, etiketteki "Karar NNN") eklenir. Panel metni ASD-STE100
Türkçe: kısa, etken, tek fikirli cümleler; ayrıntı dosyalarına file:// bağlantı.

Kullanım (jarvis/ kökünden):
  python3 tools/akis-graf-html.py [--merkez seans:<ad>] [--cikti raporlar/.../x.html] [--oda-dizin <dizin>]
B8 (2026-11-03): üst görev şeridi (tıklanır, hedef bağı H<no>), ortak/oda/<odaId>.json varsa
her oda için "Oda" sekmesi (görevler, işçi raporları, tam sohbet akışı); dosya yoksa sekme çıkmaz.
Varsayılan merkez: kütükteki son seans_ac oturumu. Karar 124 / Salih 2026-10-26.
"""
import json, re, sys, datetime, pathlib, argparse

KOK = pathlib.Path(__file__).resolve().parents[1]          # jarvis/
DEPO = KOK.parent                                          # sistem/

def oku_json(p): return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))

def dosya_url(yol):
    """Depo-göreli ya da jarvis-göreli yolu mutlak file:// URL'ye çevirir; yoksa None."""
    for taban in (DEPO, KOK):
        p = (taban / yol).resolve()
        if p.exists(): return p.as_uri()
    return None

KATEGORI_KURALI = [  # (regex etikette, kategori) — sıra önemli, ilk eşleşen kazanır
    (r"Portal Parkur|oyun|oynayıp", "Portal Parkur (oyun demosu)"),
    (r"\bCV\b", "CV"),
    (r"veri bilimi|claude-mods|öğrenme şeridi", "öğrenme şeritleri"),
    (r"md'siz", "Karar 113 md'siz koşum"),
    (r"Rust|Lean|hook|dispatcher|session-start|stop-buyuk|durum ts|test oranı|paket niyet|Herdr|skill revizyonu|ritüel|tetik-denetim|sabit güncellik", "Rust/Lean geçişi (Karar 117)"),
    (r"Karar (\d{2,3})", None),  # None → "Karar NNN" olarak üretilir
    (r"durum kütüğü|SessionStart hook brifi|seans teslim", "durum kütüğü / seans kaydı"),
    (r"push teli|alan ajanı", "alan ajanı altyapısı"),
]

def kategori_bul(n, G):
    """İş düğümünün üst başlığı: hizmet ettiği hedef; yoksa etiket anahtar sözcüğü; yoksa 'genel'."""
    if n["tur"] == "hedef":
        m = re.search(r"Karar (\d{2,3})", n.get("etiket") or ""); return ("Karar %s hedefi" % m.group(1)) if m else "hedef"
    for e in G["kenarlar"]:
        if e["tur"] == "hizmet" and e["k"] == n["id"]:
            h = next((d for d in G["dugumler"] if d["id"] == e["h"]), None)
            if h: return kategori_bul(h, G)
    et = n.get("etiket") or ""
    for rx, kat in KATEGORI_KURALI:
        m = re.search(rx, et)
        if m: return kat if kat else "Karar %s" % m.group(1)
    return "genel"

def defter_paragraf(metin, karar_no):
    m = re.search(r"\*\*Karar %s\b[^\n]*" % re.escape(karar_no), metin)
    if not m: return None
    par = m.group(0)
    return par if len(par) <= 900 else par[:880] + "…"

def js_veri(x):
    """JSON'u <script> içine güvenli gömer: '</' → '<\\/', U+2028/9 kaçışlı."""
    return (json.dumps(x, ensure_ascii=False).replace("</", "<\\/")
            .replace("\u2028", "\\u2028").replace("\u2029", "\\u2029"))

def oda_kayitlari(dizin):
    """ortak/oda/<odaId>.json (jarvis-oda Oda tipi) dosyalarını okur; dizin yoksa []. Bozuk dosya atlanır, stderr'e not düşer."""
    if not dizin.is_dir(): return []
    L = []
    for p in sorted(dizin.glob("*.json")):
        try:
            o = oku_json(p)
            if not isinstance(o, dict) or not isinstance(o.get("gorevler", []), list) or not isinstance(o.get("turlar", []), list):
                raise ValueError("Oda şeması değil (gorevler/turlar listesi yok)")
            o.setdefault("id", p.stem); o["_dosya"] = str(p)
            L.append(o)
        except Exception as e:
            print("uyarı: oda dosyası atlandı: %s (%s)" % (p, e), file=sys.stderr)
    return L

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--merkez"); ap.add_argument("--cikti")
    ap.add_argument("--oda-dizin", help="oda kayıt dizini (varsayılan ortak/oda; deneme için)")
    a = ap.parse_args()

    G = oku_json(KOK.parent / "ortak" / "akis-graf.json")
    olaylar = [json.loads(l) for l in (DEPO / "ortak" / "durum-olay.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    defter = (KOK / "kuyruk" / "senaryo-defteri.md").read_text(encoding="utf-8")

    merkez = a.merkez or "seans:" + [o for o in olaylar if o["olay"] == "seans_ac"][-1]["oturum"]

    Z = {}
    for n in G["dugumler"]:
        z = {"olaylar": [], "baglantilar": [], "ozet": None, "defter": None, "canli": None, "kategori": None if n["tur"] == "seans" else kategori_bul(n, G)}
        if n["tur"] == "seans":
            ad = n["etiket"]
            for o in olaylar:
                if o.get("oturum") == ad and o["olay"] in ("ac", "al", "bitir", "bayatla"):
                    z["olaylar"].append({"olay": o["olay"], "id": o.get("id"), "is": o.get("is"), "kanit": o.get("kanit", []), "ts": o["ts"]})
            if n.get("kayit"):
                u = dosya_url(n["kayit"])
                if u: z["baglantilar"].append({"ad": "Seans teslim kaydı (JSON)", "url": u})
                try:
                    k = oku_json(DEPO / n["kayit"]) if (DEPO / n["kayit"]).exists() else oku_json(KOK / n["kayit"])
                    z["ozet"] = {"ne_degisti": k.get("ne_degisti", []), "sapma": k.get("sapma"), "kararlar": [d.get("ad") + ": " + d.get("ozet", "") for d in k.get("kararlar", [])],
                                 "sonraki_ilk_is": k.get("sonraki_ilk_is", []), "salih_karar": k.get("salih_karar", []), "ozutler": (k.get("hasat") or {}).get("ozutler", [])}
                except Exception as e: z["ozet"] = {"hata": str(e)}
            canli = KOK / "raporlar" / "seans" / ("seans-canli-%s.json" % ad)
            if canli.exists():
                z["canli"] = oku_json(canli); z["baglantilar"].append({"ad": "Canlı oturum özeti (JSON)", "url": canli.as_uri()})
        else:
            no = int(n["id"].split(":")[1])
            for o in olaylar:
                if o.get("id") == no and o["olay"] in ("ac", "al", "bitir", "bayatla"):
                    z["olaylar"].append({"olay": o["olay"], "ts": o["ts"], "oturum": o.get("oturum"), "kanit": o.get("kanit", []), "is": o.get("is"), "sonraki": o.get("sonraki_eylem")})
                    for k in o.get("kanit", []):
                        yol = k.split(" ")[0]
                        u = dosya_url(yol)
                        if u and all(b["url"] != u for b in z["baglantilar"]): z["baglantilar"].append({"ad": "Kanıt: " + yol, "url": u})
            m = re.search(r"Karar (\d{2,3})", n.get("etiket") or "")
            if m:
                z["defter"] = defter_paragraf(defter, m.group(1))
                z["baglantilar"].append({"ad": "Karar defteri (Karar %s)" % m.group(1), "url": (KOK / "kuyruk" / "senaryo-defteri.md").as_uri()})
            for ot in n.get("oturumlar") or []:
                sn = next((s for s in G["dugumler"] if s["tur"] == "seans" and s["etiket"] == ot), None)
                if sn and sn.get("kayit"):
                    u = dosya_url(sn["kayit"])
                    if u: z["baglantilar"].append({"ad": "Oturum kaydı: " + ot, "url": u})
        Z[n["id"]] = z

    odalar = oda_kayitlari(pathlib.Path(a.oda_dizin) if a.oda_dizin else DEPO / "ortak" / "oda")

    sablon = (KOK / "tools" / "akis-graf-html.sablon.html").read_text(encoding="utf-8")
    yer = {"VERI": G, "ZENGIN": Z, "MERKEZ": merkez, "ODALAR": odalar,
           "ASOF": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}
    # Tek geçişli yerleştirme: veri içindeki "/*VERI*/" gibi metin ikinci kez yerleştirilmez.
    # "</" kaçışı: veri metnindeki "</script>" script bloğunu kapatmaz.
    html = re.sub(r"/\*(VERI|ZENGIN|MERKEZ|ODALAR|ASOF)\*/",
                  lambda m: js_veri(yer[m.group(1)]), sablon)
    cikti = pathlib.Path(a.cikti) if a.cikti else KOK / "raporlar" / datetime.date.today().strftime("%Y-%m") / (datetime.date.today().isoformat() + "-akis-graf-interaktif.html")
    cikti.parent.mkdir(parents=True, exist_ok=True)
    cikti.write_text(html, encoding="utf-8")
    print(cikti)

if __name__ == "__main__": main()
