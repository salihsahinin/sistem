#!/usr/bin/env python3
"""gorsellestir.py — İB-77 "görselleştir" skill'inin deterministik çekirdeği (m.6 deterministik
tasarım): LLM yalnız spec.json yazar, bu script ÜRETİR ve DOĞRULAR. STDLIB ONLY (jsonschema YOK).

Kullanım:
  python3 tools/gorsellestir.py <spec.json> [--cikti <yol>] [--dogrula] [--json] [--repo <yol>]

Spec JSON alanları (bkz. görev emri): baslik, kaynak_ozet, kaynak_pointer, icerik_sinifi,
gorsel_turu, arac (d2|dot|mermaid|vegalite|tablo), spec, aciklama (1-5 madde), tarih (ISO,
künye için — script SAAT OKUMAZ, determinizm buradan gelir), ogrenme_notu (opsiyonel).

Üretim: tek-dosya self-contained HTML. d2/dot → CLI ile SVG üretilip inline gömülür; mermaid →
CDN'den mermaid.esm.min.mjs; vegalite → CDN'den vega+vega-lite+vega-embed; tablo → düz <table>.
Renk: Okabe–Ito renk-körü-güvenli palet (vegalite spec'ine config.range.category olarak yazılır).

Doğrulama --dogrula (LLM'siz, deterministik): şema + araç-özel + HTML yapısı + determinizm
(aynı spec iki kez üretilince bayt-bayt aynı olmalı — bu script çağrı-içi ikinci üretimle sınanır
DEĞİL, iddiası çıktının zaman okumamasıdır; test dosyası ayrıca iki-koşum eşitliğini sınar).

Çıkış kodu: 0 PASS · 3 FAIL (doğrulama kontrollerinden biri düştü) · 2 girdi hatası.
--json: {arac, surum, git_head, cikti, kontroller:[{ad, sonuc, not}], gecti}.

Kütük: jarvis kökünde üretildiyse veri/bronz/gorsel-olay.jsonl'a append-only tek satır eklenir;
jarvis dışında kütük YAZILMAZ.
"""
import argparse
import contextlib
import html
import json
import os
import re
import subprocess
import sys
import tempfile
import unicodedata

SURUM = "1.0.0"
ARAC = "gorsellestir"

OKABE_ITO = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000"]

ZORUNLU_ALANLAR = [
    "baslik", "kaynak_ozet", "kaynak_pointer", "icerik_sinifi", "gorsel_turu",
    "arac", "spec", "aciklama", "tarih",
]
ICERIK_SINIFLARI = {
    "surec", "kavram-iliskisi", "karsilastirma", "hiyerarsi", "zaman-akisi",
    "mekanizma", "sayisal-dagilim", "sayisal-iliski", "zaman-serisi",
    "sayisal-karsilastirma", "parca-butun", "akis-miktari",
}
ARACLAR = {"d2", "dot", "mermaid", "vegalite", "tablo"}
MERMAID_TURLERI = {
    "flowchart", "graph", "sequenceDiagram", "classDiagram", "stateDiagram",
    "erDiagram", "gantt", "mindmap", "timeline", "pie", "sankey-beta",
    "quadrantChart", "xychart-beta",
}
VEGA_MARKLAR = {"bar", "line", "point", "area", "rect", "arc", "text", "tick", "boxplot", "circle", "square"}
IZINLI_CDN = ("cdn.jsdelivr.net",)
MAKS_BOYUT = 2 * 1024 * 1024


class GirdiHatasi(Exception):
    pass


def slugla(metin):
    """Başlığı dosya-adı-uyumlu slug'a çevirir (ascii, küçük harf, tire ayraç)."""
    metin = unicodedata.normalize("NFKD", metin).encode("ascii", "ignore").decode("ascii")
    metin = metin.lower()
    metin = re.sub(r"[^a-z0-9]+", "-", metin).strip("-")
    return metin or "gorsel"


def git_head(repo):
    try:
        r = subprocess.run(
            ["git", "-C", repo, "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, timeout=5,
        )
        if r.returncode == 0:
            return r.stdout.strip()
    except OSError:
        pass
    return "bilinmiyor"


def git_kok(baslangic):
    try:
        r = subprocess.run(
            ["git", "-C", baslangic, "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, timeout=5,
        )
        if r.returncode == 0:
            return r.stdout.strip()
    except OSError:
        pass
    return None


def spec_oku(yol):
    try:
        with open(yol, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, json.JSONDecodeError) as e:
        raise GirdiHatasi("spec okunamadı: %s" % e)


# ---------------------------------------------------------------------------
# ŞEMA DOĞRULAMA
# ---------------------------------------------------------------------------

def sema_dogrula(spec):
    """Zorunlu alan + enum kontrolleri. (ad, sonuc, not) üçlü listesi döndürür."""
    sonuclar = []

    eksik = [a for a in ZORUNLU_ALANLAR if a not in spec]
    sonuclar.append(("sema:zorunlu-alanlar", "PASS" if not eksik else "FAIL",
                      "eksik: %s" % ", ".join(eksik) if eksik else "tümü mevcut"))

    sinif = spec.get("icerik_sinifi")
    sonuclar.append(("sema:icerik_sinifi", "PASS" if sinif in ICERIK_SINIFLARI else "FAIL",
                      str(sinif)))

    arac = spec.get("arac")
    sonuclar.append(("sema:arac", "PASS" if arac in ARACLAR else "FAIL", str(arac)))

    aciklama = spec.get("aciklama")
    aciklama_ok = isinstance(aciklama, list) and 1 <= len(aciklama) <= 5
    sonuclar.append(("sema:aciklama", "PASS" if aciklama_ok else "FAIL",
                      "madde sayısı=%s" % (len(aciklama) if isinstance(aciklama, list) else "n/a")))

    for alan in ("baslik", "kaynak_ozet", "kaynak_pointer", "tarih", "gorsel_turu"):
        deger = spec.get(alan)
        ok = isinstance(deger, str) and deger.strip() != ""
        sonuclar.append(("sema:%s" % alan, "PASS" if ok else "FAIL", "boş/str-değil" if not ok else "tamam"))

    return sonuclar


# ---------------------------------------------------------------------------
# ARAÇ-ÖZEL RENDER
# ---------------------------------------------------------------------------

def _cli_render_svg(komut, girdi_metni, hata_baglam):
    """d2/dot CLI ile SVG üretir. (svg_metin_veya_None, kontrol_notu) döndürür."""
    with _gecici_dosya(girdi_metni) as (in_yol, calisma_dizin):
        out_yol = in_yol + ".svg"
        try:
            r = subprocess.run(
                komut(in_yol, out_yol), capture_output=True, text=True, timeout=30,
            )
        except (OSError, subprocess.TimeoutExpired) as e:
            return None, "%s çalıştırılamadı: %s" % (hata_baglam, e)
        if r.returncode != 0:
            return None, "%s exit=%s stderr=%s" % (hata_baglam, r.returncode, r.stderr.strip()[:300])
        try:
            with open(out_yol, encoding="utf-8") as fh:
                svg = fh.read()
        except OSError as e:
            return None, "SVG okunamadı: %s" % e
        if not svg.strip() or "<svg" not in svg:
            return None, "SVG boş/geçersiz"
        return svg, "render OK (%d bayt)" % len(svg.encode("utf-8"))


@contextlib.contextmanager
def _gecici_dosya(icerik):
    d = tempfile.mkdtemp(prefix="gorsellestir-")
    yol = os.path.join(d, "girdi.txt")
    with open(yol, "w", encoding="utf-8") as fh:
        fh.write(icerik)
    try:
        yield yol, d
    finally:
        pass  # geçici dizin bilinçli bırakılır (os temp, kalıcı zarar yok); sadeleştirme


def d2_render(spec_metni):
    return _cli_render_svg(lambda i, o: ["d2", "--layout=elk", i, o], spec_metni, "d2")


def dot_render(spec_metni):
    return _cli_render_svg(lambda i, o: ["dot", "-Tsvg", i, "-o", o], spec_metni, "dot")


def mermaid_kontrol(spec_metni):
    """Mermaid metnini yapısal kontrolden geçirir (tarayıcısız — gerçek render YAPILAMAZ)."""
    satirlar = [s for s in spec_metni.splitlines() if s.strip() != ""]
    if len(satirlar) < 2:
        return False, "en az 2 anlamlı satır gerekli, bulunan=%d" % len(satirlar)
    ilk = satirlar[0].strip()
    ilk_kelime = ilk.split()[0] if ilk.split() else ""
    tur_bulundu = None
    for tur in MERMAID_TURLERI:
        if ilk.startswith(tur):
            tur_bulundu = tur
            break
    if tur_bulundu is None:
        return False, "ilk satırda tanınan diyagram türü yok: %r" % ilk[:60]
    return True, "tür=%s, satır=%d" % (tur_bulundu, len(satirlar))


def vegalite_kontrol(spec_nesne):
    """Vega-Lite spec nesnesini yapısal + lie-factor kurallarına göre denetler."""
    if not isinstance(spec_nesne, dict):
        return False, "spec bir JSON nesnesi değil"
    mark = spec_nesne.get("mark")
    mark_ad = mark.get("type") if isinstance(mark, dict) else mark
    if mark_ad not in VEGA_MARKLAR:
        return False, "mark geçersiz: %r" % mark_ad
    if "encoding" not in spec_nesne or not isinstance(spec_nesne["encoding"], dict):
        return False, "encoding yok/geçersiz"
    veri = spec_nesne.get("data", {})
    degerler = veri.get("values") if isinstance(veri, dict) else None
    if not isinstance(degerler, list) or len(degerler) < 1:
        return False, "data.values eksik/boş"
    if mark_ad in ("bar", "area"):
        for eksen_ad in ("x", "y"):
            enc = spec_nesne["encoding"].get(eksen_ad, {})
            if isinstance(enc, dict) and enc.get("type") == "quantitative":
                scale = enc.get("scale", {})
                if isinstance(scale, dict) and scale.get("zero") is False:
                    return False, "lie-factor: %s ekseninde scale.zero=false (mark=%s)" % (eksen_ad, mark_ad)
    renk_paleti = spec_nesne.get("config", {}).get("range", {}).get("category")
    if renk_paleti != OKABE_ITO:
        return False, "palet Okabe-Ito değil (config.range.category enjekte edilmemiş)"
    return True, "mark=%s, satır=%d, palet OK" % (mark_ad, len(degerler))


def vegalite_palet_enjekte(spec_nesne):
    """spec_nesne'ye Okabe-Ito paletini config.range.category olarak yazar (yoksa ekler)."""
    spec_nesne = json.loads(json.dumps(spec_nesne))  # sığ kopya yeterli değil, derin kopya
    cfg = spec_nesne.setdefault("config", {})
    rng = cfg.setdefault("range", {})
    rng["category"] = list(OKABE_ITO)
    return spec_nesne


def tablo_kontrol(spec_nesne):
    if not isinstance(spec_nesne, dict):
        return False, "spec bir JSON nesnesi değil"
    basliklar = spec_nesne.get("basliklar")
    satirlar = spec_nesne.get("satirlar")
    if not isinstance(basliklar, list) or not isinstance(satirlar, list):
        return False, "basliklar/satirlar eksik"
    n = len(basliklar)
    for i, satir in enumerate(satirlar):
        if not isinstance(satir, list) or len(satir) != n:
            return False, "satır %d uzunluğu %d != başlık sayısı %d" % (i, len(satir) if isinstance(satir, list) else -1, n)
    return True, "başlık=%d, satır=%d" % (n, len(satirlar))


# ---------------------------------------------------------------------------
# HTML ÜRETİM
# ---------------------------------------------------------------------------

CSS = """
:root{--fg:#1a1a1a;--bg:#ffffff;--muted:#555;--border:#ddd;--accent:#0072B2;}
*{box-sizing:border-box;}
body{font-family:-apple-system,"Segoe UI",Helvetica,Arial,sans-serif;color:var(--fg);
background:var(--bg);margin:0;padding:24px;line-height:1.5;}
h1{font-size:1.5rem;margin:0 0 12px;}
#kaynak{font-size:.9rem;color:var(--muted);border-left:3px solid var(--accent);
padding:6px 12px;margin-bottom:20px;background:#f7f7f7;}
#govde{display:grid;grid-template-columns:1fr;gap:20px;}
@media(min-width:900px){#govde{grid-template-columns:2fr 1fr;align-items:start;}}
#gorsel{border:1px solid var(--border);border-radius:6px;padding:12px;overflow:auto;}
#gorsel svg{max-width:100%;height:auto;}
#aciklama{border:1px solid var(--border);border-radius:6px;padding:12px 16px;background:#fafafa;}
#aciklama h2{font-size:1rem;margin:0 0 8px;}
#aciklama ul{margin:0;padding-left:20px;}
#aciklama li{margin:4px 0;}
table{border-collapse:collapse;width:100%;}
th,td{border:1px solid var(--border);padding:6px 10px;text-align:left;font-size:.92rem;}
th{background:#f0f0f0;}
#kunye{margin-top:20px;font-size:.8rem;color:var(--muted);border-top:1px solid var(--border);
padding-top:8px;}
#ogrenme{margin-top:12px;font-size:.85rem;color:var(--muted);font-style:italic;}
"""


def _tablo_html(spec_nesne):
    basliklar = spec_nesne["basliklar"]
    satirlar = spec_nesne["satirlar"]
    tr_baslik = "".join("<th>%s</th>" % html.escape(str(b)) for b in basliklar)
    gov = []
    for satir in satirlar:
        gov.append("<tr>" + "".join("<td>%s</td>" % html.escape(str(h_)) for h_ in satir) + "</tr>")
    return "<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (tr_baslik, "".join(gov))


def gorsel_blogu_uret(spec, arac_kontrolleri):
    """(gorsel_html, kontroller_listesi) döndürür. arac_kontrolleri: bu çağrıya eklenecek liste referansı."""
    arac = spec["arac"]
    ic_spec = spec["spec"]

    if arac == "d2":
        svg, not_ = d2_render(ic_spec)
        arac_kontrolleri.append(("arac:d2-render", "PASS" if svg else "FAIL", not_))
        return svg or "<p>d2 render başarısız</p>"

    if arac == "dot":
        svg, not_ = dot_render(ic_spec)
        arac_kontrolleri.append(("arac:dot-render", "PASS" if svg else "FAIL", not_))
        return svg or "<p>dot render başarısız</p>"

    if arac == "mermaid":
        ok, not_ = mermaid_kontrol(ic_spec)
        arac_kontrolleri.append(("arac:mermaid-yapi", "PASS" if ok else "FAIL", not_))
        return (
            '<script type="module">\n'
            'import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";\n'
            'mermaid.initialize({startOnLoad:true, theme:"neutral"});\n'
            "</script>\n"
            '<pre class="mermaid">\n%s\n</pre>' % html.escape(ic_spec)
        )

    if arac == "vegalite":
        vs = ic_spec if isinstance(ic_spec, dict) else {}
        vs = vegalite_palet_enjekte(vs)
        ok, not_ = vegalite_kontrol(vs)
        arac_kontrolleri.append(("arac:vegalite-yapi", "PASS" if ok else "FAIL", not_))
        vs_json = json.dumps(vs, ensure_ascii=False, sort_keys=True)
        return (
            '<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>\n'
            '<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>\n'
            '<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>\n'
            '<div id="vega-hedef"></div>\n'
            "<script>\nvegaEmbed('#vega-hedef', %s, {actions:false});\n</script>" % vs_json
        )

    if arac == "tablo":
        ts = ic_spec if isinstance(ic_spec, dict) else {}
        ok, not_ = tablo_kontrol(ts)
        arac_kontrolleri.append(("arac:tablo-yapi", "PASS" if ok else "FAIL", not_))
        if ok:
            return _tablo_html(ts)
        return "<p>tablo spec geçersiz</p>"

    arac_kontrolleri.append(("arac:bilinmeyen", "FAIL", "arac=%r" % arac))
    return "<p>bilinmeyen araç</p>"


KUNYE_YER_TUTUCU = "@@DOGRULAMA-OZETI@@"


def html_uret(spec, arac_kontrolleri, dogrulama_ozeti=None):
    """HTML üretir. dogrulama_ozeti None ise künyeye yer-tutucu konur (sonradan tek-geçiş
    string-replace ile doldurulur) — böylece render (d2/dot CLI) yalnız BİR kez çalışır."""
    baslik = html.escape(spec.get("baslik", ""))
    kaynak_ozet = html.escape(spec.get("kaynak_ozet", ""))
    kaynak_pointer = html.escape(spec.get("kaynak_pointer", ""))
    aciklama = spec.get("aciklama", [])
    aciklama_li = "".join("<li>%s</li>" % html.escape(str(a)) for a in aciklama)
    ogrenme = spec.get("ogrenme_notu")
    ogrenme_html = ('<div id="ogrenme">Öğrenme notu: %s</div>' % html.escape(ogrenme)) if ogrenme else ""

    gorsel_html = gorsel_blogu_uret(spec, arac_kontrolleri)

    kunye = "%s · içerik sınıfı: %s · görsel türü: %s · araç: %s · doğrulama: %s" % (
        html.escape(spec.get("tarih", "")),
        html.escape(spec.get("icerik_sinifi", "")),
        html.escape(spec.get("gorsel_turu", "")),
        html.escape(spec.get("arac", "")),
        html.escape(dogrulama_ozeti) if dogrulama_ozeti is not None else KUNYE_YER_TUTUCU,
    )

    return """<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<style>%s</style>
</head>
<body>
<h1 id="baslik">%s</h1>
<div id="kaynak"><strong>Kaynak:</strong> %s — <em>%s</em></div>
<div id="govde">
<div id="gorsel">%s</div>
<div id="aciklama"><h2>Açıklama</h2><ul>%s</ul></div>
</div>
%s
<div id="kunye">%s</div>
</body>
</html>
""" % (baslik, CSS, baslik, kaynak_ozet, kaynak_pointer, gorsel_html, aciklama_li, ogrenme_html, kunye)


# ---------------------------------------------------------------------------
# HTML DOĞRULAMA
# ---------------------------------------------------------------------------

def html_dogrula(html_metin):
    sonuclar = []
    zorunlu_id = ["baslik", "kaynak", "gorsel", "aciklama", "kunye"]
    eksik = [i for i in zorunlu_id if ('id="%s"' % i) not in html_metin]
    sonuclar.append(("html:zorunlu-bloklar", "PASS" if not eksik else "FAIL",
                      "eksik: %s" % ", ".join(eksik) if eksik else "tümü mevcut"))

    boyut = len(html_metin.encode("utf-8"))
    sonuclar.append(("html:boyut", "PASS" if boyut < MAKS_BOYUT else "FAIL",
                      "%d bayt" % boyut))

    dis_url = re.findall(r'(?:src|href)="(https?://[^"]+)"', html_metin)
    kotu = [u for u in dis_url if not any(u.startswith("https://" + izin) or u.startswith("http://" + izin) for izin in IZINLI_CDN)]
    sonuclar.append(("html:cdn-allowlist", "PASS" if not kotu else "FAIL",
                      "izinsiz: %s" % ", ".join(kotu) if kotu else "tümü cdn.jsdelivr.net"))

    return sonuclar


# ---------------------------------------------------------------------------
# ÇIKTI YERİ
# ---------------------------------------------------------------------------

def cikti_yolu_belirle(spec, repo_cwd, verilen_cikti):
    kok = git_kok(repo_cwd)
    if verilen_cikti:
        # --cikti verilse de kütük kararı kökle belirlenir: jarvis kökündeyse gorsel-olay.jsonl yazılır (09-03 vaka bulgusu)
        return os.path.abspath(verilen_cikti), bool(kok and os.path.basename(kok) == "jarvis")
    slug = slugla(spec.get("baslik", ""))
    tarih = spec.get("tarih", "tarihsiz")
    ad = "gorsel-%s-%s.html" % (tarih, slug)
    if kok and os.path.basename(kok) == "jarvis":
        return os.path.join(kok, "raporlar", ad), True
    return os.path.join(repo_cwd, "gorsel", ad), False


def kutuk_yaz(kok, spec, dogrulama_ozeti, cikti_yolu):
    kutuk_dizin = os.path.join(kok, "veri", "bronz")
    os.makedirs(kutuk_dizin, exist_ok=True)
    kutuk_yol = os.path.join(kutuk_dizin, "gorsel-olay.jsonl")
    satir = {
        "tarih": spec.get("tarih"),
        "icerik_sinifi": spec.get("icerik_sinifi"),
        "gorsel_turu": spec.get("gorsel_turu"),
        "arac": spec.get("arac"),
        "dogrulama": dogrulama_ozeti,
        "cikti": cikti_yolu,
    }
    with open(kutuk_yol, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(satir, ensure_ascii=False, sort_keys=True) + "\n")


# ---------------------------------------------------------------------------
# ANA AKIŞ
# ---------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(prog=ARAC, description="Spec'ten deterministik görsel HTML üretir ve doğrular.")
    ap.add_argument("spec_yolu")
    ap.add_argument("--cikti")
    ap.add_argument("--dogrula", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--repo", default=os.getcwd())
    ns = ap.parse_args(argv)

    try:
        spec = spec_oku(ns.spec_yolu)
    except GirdiHatasi as e:
        if ns.json:
            print(json.dumps({"arac": ARAC, "surum": SURUM, "hata": str(e)}, ensure_ascii=False))
        else:
            print("girdi hatası: %s" % e, file=sys.stderr)
        return 2

    sema_kontrolleri = sema_dogrula(spec)
    sema_gecti = all(s == "PASS" for _, s, _ in sema_kontrolleri)
    if not sema_gecti and not ns.dogrula:
        # Şema geçersizse üretim de yapılamaz (zorunlu alanlar HTML'de kullanılıyor).
        for ad, sonuc, not_ in sema_kontrolleri:
            if sonuc == "FAIL":
                print("FAIL %s: %s" % (ad, not_), file=sys.stderr)
        if ns.json:
            print(json.dumps({"arac": ARAC, "surum": SURUM, "hata": "sema gecersiz",
                               "kontroller": [{"ad": a, "sonuc": s, "not": n} for a, s, n in sema_kontrolleri]},
                              ensure_ascii=False))
        return 2

    arac_kontrolleri = []
    html_metin = html_uret(spec, arac_kontrolleri) if sema_gecti else None

    tum_kontroller = list(sema_kontrolleri) + arac_kontrolleri
    if html_metin is not None:
        tum_kontroller += html_dogrula(html_metin)

    gecti = all(s == "PASS" for _, s, _ in tum_kontroller)
    ozet = "%d/%d PASS" % (sum(1 for _, s, _ in tum_kontroller if s == "PASS"), len(tum_kontroller))

    if html_metin is not None:
        # künye satırındaki yer-tutucuyu nihai özetle doldur (render ikinci kez ÇALIŞTIRILMAZ —
        # determinizm ve performans: tek CLI çağrısı yeter).
        html_metin = html_metin.replace(KUNYE_YER_TUTUCU, html.escape(ozet))

    kok = git_kok(ns.repo)
    cikti_yolu, jarvis_kok_mu = cikti_yolu_belirle(spec, ns.repo, ns.cikti)

    yazildi = False
    if html_metin is not None and (gecti or not ns.dogrula):
        os.makedirs(os.path.dirname(cikti_yolu), exist_ok=True)
        with open(cikti_yolu, "w", encoding="utf-8") as fh:
            fh.write(html_metin)
        yazildi = True
        # kütük yalnız jarvis kökü ALTINA yazılan çıktılar için (test/geçici-dizin koşumları kütüğe düşmez — 09-03 bulgusu)
        if jarvis_kok_mu and kok and os.path.abspath(cikti_yolu).startswith(os.path.abspath(kok) + os.sep):
            kutuk_yaz(kok, spec, ozet, cikti_yolu)

    if ns.json:
        cikti_json = {
            "arac": ARAC,
            "surum": SURUM,
            "git_head": git_head(ns.repo),
            "cikti": cikti_yolu if yazildi else None,
            "kontroller": [{"ad": a, "sonuc": s, "not": n} for a, s, n in tum_kontroller],
            "gecti": gecti,
        }
        print(json.dumps(cikti_json, ensure_ascii=False))
    else:
        for ad, sonuc, not_ in tum_kontroller:
            satir = "%s %s: %s" % (sonuc, ad, not_)
            if sonuc == "FAIL":
                print(satir, file=sys.stderr)
            else:
                print(satir)
        if yazildi:
            print("çıktı: %s" % cikti_yolu)
        print("doğrulama: %s" % ozet)

    if ns.dogrula:
        return 0 if gecti else 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
