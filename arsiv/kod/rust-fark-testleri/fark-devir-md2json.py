#!/usr/bin/env python3
"""devir-md2json: Python özgün ile Rust portunun fark testi.

Her durum aynı sandbox'ın iki taze kopyasında (Python / Rust) çalışır; çıkış kodu, stdout, stderr ve
sandbox'taki her dosya (CRLF→LF) karşılaştırılır. Yakalanmamış Python istisnası (çıkış 1 + traceback) olan
durumlarda yalnız çıkış kodu + stdout eşitliği aranır (stderr metni bilinçli ayrışır).
Kullanım: python fark-devir-md2json.py   (RUST_EXE ile exe yolu verilebilir)
"""
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

KOK = Path(__file__).resolve().parents[3]
PY = KOK / "jarvis" / "tools" / "devir-md2json.py"
if not PY.exists():
    PY = KOK / "arsiv" / "kod" / "python" / "tools" / "devir-md2json.py"
RUST = os.environ.get("RUST_EXE", r"C:/tmp/tgt/release/devir-md2json.exe")

# TAM örnek bloğu birim testinden alınır
_t = KOK / "jarvis" / "tools" / "testler" / "test_devir_md2json.py"
if not _t.exists():
    _t = KOK / "arsiv" / "kod" / "python" / "tools" / "testler" / "test_devir_md2json.py"
_ozel = importlib.util.spec_from_file_location("tdm", _t)
_m = importlib.util.module_from_spec(_ozel)
_ozel.loader.exec_module(_m)
TAM = _m.TAM

ORTAM = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
ORTAM.pop("COLUMNS", None)

DURUMLAR = []  # (ad, dosyalar{ad: str|bytes}, argüman listesi, çökme_beklenir)


def durum(ad, md=None, args=("gorev.md",), dosyalar=None, cokme=False, once=None):
    d = dict(dosyalar or {})
    if md is not None:
        d["gorev.md"] = md
    DURUMLAR.append((ad, d, list(args), cokme, once))


def degis(a, b):
    assert a in TAM, a
    return TAM.replace(a, b)


# ---- normal yollar
durum("tam-varsayilan")
durum("tam-kuru", TAM, ["gorev.md", "--kuru"])
durum("tam-cikti-alt", TAM, ["gorev.md", "--cikti", "alt/x.json"], {"alt/.keep": ""})
durum("tam-cikti-bos-dizge", TAM, ["gorev.md", "--cikti", ""])
durum("tam-altdizin-emir", TAM, ["d1/d2/gorev.md"], {"d1/d2/x": ""}, once=lambda d: (d / "d1/d2/gorev.md").write_text(TAM, encoding="utf-8"))
durum("tam-nokta-yol", TAM, ["./gorev.md"])
durum("tam-kuru-ve-dogrula", TAM, ["gorev.md", "--kuru", "--dogrula", "x.json"], {"x.json": "{}"})
durum("cikti-eksik-dizin-cokme", TAM, ["gorev.md", "--cikti", "yok/x.json"], cokme=True)
durum("yardim", TAM, ["-h"])
durum("arguman-yok", None, [])
durum("bilinmeyen-bayrak", TAM, ["gorev.md", "--bilinmeyen"])
durum("iki-konumsal", TAM, ["gorev.md", "b.md"])
durum("cikti-degersiz", TAM, ["gorev.md", "--cikti"])
durum("onek-kisaltma", TAM, ["gorev.md", "--ku"])
durum("emir-yok", None, ["yok.md"])
durum("cit-yok", "# başlık\nmetin\n", ["gorev.md"])
durum("cit-sonu-yok", "```lojik\nA: b\n", ["gorev.md"])
durum("emir-dizin-cokme", None, ["dizin"], {"dizin/x": ""}, cokme=True)
durum("emir-utf8-degil-cokme", None, ["gorev.md"], {"gorev.md": b"\xff\xfe```lojik\nA: b\n```\n"}, cokme=True)
durum("crlf-emir", TAM.replace("\n", "\r\n"))
durum("cit-bosluklu", TAM.replace("```lojik\n", "```lojik \t\n"))
durum("cit-oncesi-metin-iki-cit", "```lojik\nX: 1\n```\n\n" + TAM)

# ---- ayrıştırıcı
durum("girintili-anahtarsiz", "```lojik\n  - x\nA: b\n```\n")
durum("liste-skaler-karisik", degis("EAGER:\n  - core/rol.md", "EAGER: skaler\n  - core/rol.md"))
durum("liste-sozluk-karisik", degis("EAGER:\n  - core/rol.md", "EAGER:\n  - core/rol.md\n  K: v"))
durum("sozluk-liste-karisik", degis("ÇIKTI:\n  C1:", "ÇIKTI:\n  - x\n  C1:"))
durum("sozluk-skaler-karisik", degis("ÇIKTI:\n  C1:", "ÇIKTI: x\n  C1:"))
durum("alt-satir-ne-liste-ne-sozluk", degis("EAGER:\n  - core/rol.md", "EAGER:\n  - core/rol.md\n  düz metin"))
durum("alt-satir-tire-yalniz", degis("EAGER:\n  - core/rol.md", "EAGER:\n  - core/rol.md\n  -"))
durum("alt-satir-repr-ozel", degis("EAGER:\n  - core/rol.md", "EAGER:\n  - core/rol.md\n  'çift\"tırnak\\ \x01"))
durum("yorum-bos-satir", degis("EAGER:\n", "# yorum\n\n   \n  # girintili yorum\nEAGER:\n"))
durum("tekrar-anahtar-ustune-yaz", degis("AMAÇ: tek cümle amaç", "AMAÇ: ilk\nAMAÇ: ikinci"))
durum("tekrar-sozluk-anahtari", degis("  C1: cc/giden/devir-2026-09-16-test/cevap.md", "  C1: cc/giden/x/a.md\n  C1: cc/giden/devir-2026-09-16-test/cevap.md"))
durum("sekme-girinti", degis("EAGER:\n  - core/rol.md", "EAGER:\n\t- core/rol.md"))
durum("anahtar-iki-nokta-yok", degis("AMAÇ: tek cümle amaç", "AMAÇ tek cümle amaç"))
durum("deger-iki-nokta", degis("AMAÇ: tek cümle amaç", "AMAÇ: a: b: c"))
durum("nbsp-baslayan-satir", degis("AMAÇ: tek cümle amaç", "\u00a0AMAÇ: x"))
durum("u2028-satir", degis("AMAÇ: tek cümle amaç", "AMAÇ: a\u2028B: c"))
durum("liste-maddesi-bos-tire-bosluk", degis("EAGER:\n  - core/rol.md", "EAGER:\n  - core/rol.md\n  - "))

# ---- doğrulama
durum("eksik-alan", degis("NİÇİN_ŞİMDİ: S2 K etiketi açık\n", ""))
durum("eksik-cok-alan", "```lojik\nA: b\n```\n")
durum("cikti-izin-celiskisi", degis("  C2: cc/giden/devir-2026-09-16-test-geri-donus.md", "  C2: kanon/tuzuk.md"))
durum("cikti-basina-done", degis("  C2: geri-donus 10+2 alanla VAR\n", ""))
durum("done-var-cikti-yok", degis("  C2: geri-donus 10+2 alanla VAR\n", "  C2: geri-donus 10+2 alanla VAR\n  C9: fazla\n"))
durum("dal-tavani", degis("  - D-KATMAN1: kural değişikliği → DUR\n", "".join(f"  - D{i}: eğer x{i} → y{i}\n" for i in range(2, 8))))
durum("dal-oku-yok", degis("  - D1: eğer URL açılamıyorsa → X etiketi\n", "  - D1: ok yok\n  - " + "u" * 70 + "\n"))
durum("dal-skaler", degis("DALLAR:\n  - D1: eğer URL açılamıyorsa → X etiketi\n  - D-KATMAN1: kural değişikliği → DUR\n", "DALLAR: a → b\n"))
durum("dal-skaler-oksuz", degis("DALLAR:\n  - D1: eğer URL açılamıyorsa → X etiketi\n  - D-KATMAN1: kural değişikliği → DUR\n", "DALLAR: ok yok\n"))
durum("dal-sozluk-oksuz-cokme", degis("DALLAR:\n  - D1: eğer URL açılamıyorsa → X etiketi\n  - D-KATMAN1: kural değişikliği → DUR\n", "DALLAR:\n  D1: x\n"), cokme=True)
durum("dal-sozluk-ok-anahtari", degis("DALLAR:\n  - D1: eğer URL açılamıyorsa → X etiketi\n  - D-KATMAN1: kural değişikliği → DUR\n", "DALLAR:\n  →: x\n"))
durum("deneme-sayi-degil", degis("YENİDEN_DENEME: 2", "YENİDEN_DENEME: iki"))
durum("deneme-ust-simge-cokme", degis("YENİDEN_DENEME: 2", "YENİDEN_DENEME: ²"), cokme=True)
durum("deneme-arap-rakam", degis("YENİDEN_DENEME: 2", "YENİDEN_DENEME: ٣"))
durum("deneme-baslangic-sifir", degis("YENİDEN_DENEME: 2", "YENİDEN_DENEME: 007"))
durum("deneme-liste", degis("YENİDEN_DENEME: 2", "YENİDEN_DENEME:\n  - 2"))
durum("deneme-buyuk", degis("YENİDEN_DENEME: 2", "YENİDEN_DENEME: 12345678901234567890"))
durum("oturum-belki", degis("OTURUM: devam", "OTURUM: belki"))
durum("oturum-yeni", degis("OTURUM: devam", "OTURUM: yeni"))
durum("oturum-liste", degis("OTURUM: devam", "OTURUM:\n  - devam"))
durum("url-kaynaksiz", degis("AMAÇ: tek cümle amaç", "AMAÇ: https://x.y/a sayfasını aç"))
durum("docs-kaynaksiz", degis("NİÇİN_ŞİMDİ: S2 K etiketi açık", "NİÇİN_ŞİMDİ: bkz /docs/ yolu"))
durum("url-done-icinde", degis("  C1: cevap.md VAR ∧ her iddia D/K/X", "  C1: http://a.b ok"))
durum("url-kaynakli-sozluk", degis("AMAÇ: tek cümle amaç", "AMAÇ: https://x.y/a\nKAYNAKLAR:\n  R1: https://x.y/a"))
durum("url-kaynakli-liste", degis("AMAÇ: tek cümle amaç", "AMAÇ: https://x.y/a\nKAYNAKLAR:\n  - https://x.y/a\n  - b"))
durum("url-kaynakli-skaler", degis("AMAÇ: tek cümle amaç", "AMAÇ: https://x.y/a\nKAYNAKLAR: tek"))
durum("url-dallarda-liste-repr", degis("  - D1: eğer URL açılamıyorsa → X etiketi", "  - D1: https://x → y"))
durum("cikti-done-skaler", degis("ÇIKTI:\n  C1: cc/giden/devir-2026-09-16-test/cevap.md\n  C2: cc/giden/devir-2026-09-16-test-geri-donus.md\n", "ÇIKTI: cc/giden/x.md\n"))
durum("izin-skaler", degis("YAZMA_İZNİ:\n  - cc/giden/devir-2026-09-16-test/**\n  - cc/giden/devir-2026-09-16-test-geri-donus.md\n", "YAZMA_İZNİ: cc/giden/*\n"))
durum("izin-sozluk-cokme", degis("YAZMA_İZNİ:\n  - cc/giden/devir-2026-09-16-test/**\n  - cc/giden/devir-2026-09-16-test-geri-donus.md\n", "YAZMA_İZNİ:\n  K: cc/giden/*\n"), cokme=True)
durum("izin-onek-yildiz", degis("YAZMA_İZNİ:\n  - cc/giden/devir-2026-09-16-test/**\n  - cc/giden/devir-2026-09-16-test-geri-donus.md\n", "YAZMA_İZNİ:\n  - cc/giden/devir-2026-09-16-test\n"))
durum("izin-buyuk-kucuk", degis("  - cc/giden/devir-2026-09-16-test/**\n", "  - CC/GİDEN/DEVİR-2026-09-16-TEST/**\n"))
durum("izin-soru-isareti", degis("  - cc/giden/devir-2026-09-16-test/**\n  - cc/giden/devir-2026-09-16-test-geri-donus.md\n", "  - cc/giden/devir-2026-09-16-test/c?vap.md\n  - cc/giden/*geri-donus.m?\n"))
durum("izin-kume", degis("  - cc/giden/devir-2026-09-16-test/**\n  - cc/giden/devir-2026-09-16-test-geri-donus.md\n", "  - cc/giden/devir-2026-09-16-test/[a-d]evap.md\n  - cc/giden/devir-2026-09-16-test-geri-donus.m[!x]\n"))
durum("izin-kume-red", degis("  - cc/giden/devir-2026-09-16-test/**\n  - cc/giden/devir-2026-09-16-test-geri-donus.md\n", "  - cc/giden/devir-2026-09-16-test/[!c]evap.md\n  - zzz[\n"))
durum("izin-kume-ters-aralik", degis("  - cc/giden/devir-2026-09-16-test/**\n  - cc/giden/devir-2026-09-16-test-geri-donus.md\n", "  - cc/giden/devir-2026-09-16-test/[z-a]evap.md\n  - cc/giden/devir-2026-09-16-test-geri-donus.m[d-]\n"))
durum("izin-kume-ozel", degis("  - cc/giden/devir-2026-09-16-test/**\n  - cc/giden/devir-2026-09-16-test-geri-donus.md\n", "  - cc/giden/devir-2026-09-16-test/[]c]evap.md\n  - x[^a]\n  - [!]\n"))
durum("izin-ters-egik", degis("  - cc/giden/devir-2026-09-16-test/**\n  - cc/giden/devir-2026-09-16-test-geri-donus.md\n", "  - cc\\giden\\devir-2026-09-16-test\\**\n  - cc/giden/devir-2026-09-16-test-geri-donus.md\n"))

# ---- üretim biçimleri
durum("bütçe-metin-ve-sayi", degis("BÜTÇE: model=opus effort=medium arac_cagri_tavani=40 beklenen_ajan_cagrisi=0", "BÜTÇE:   a=1 b c= =3 d=x=y e=٣ a=2  f=007"))
durum("butce-liste-cokme", degis("BÜTÇE: model=opus effort=medium arac_cagri_tavani=40 beklenen_ajan_cagrisi=0", "BÜTÇE:\n  - a=1"), cokme=True)
durum("butce-ust-simge-cokme", degis("BÜTÇE: model=opus effort=medium arac_cagri_tavani=40 beklenen_ajan_cagrisi=0", "BÜTÇE: a=²"), cokme=True)
durum("butce-yari-kesir", degis("BÜTÇE: model=opus effort=medium arac_cagri_tavani=40 beklenen_ajan_cagrisi=0", "BÜTÇE: a=½"))
durum("butce-sirali-anahtarlar", degis("BÜTÇE: model=opus effort=medium arac_cagri_tavani=40 beklenen_ajan_cagrisi=0", "BÜTÇE: z=1 ç=2 a=3 é=4 Z=5"))
durum("yetki-dogru", degis("PUSH: false\nKARAR_YETKİSİ: false", "PUSH: TRUE\nKARAR_YETKİSİ: True"))
durum("yetki-bos-ve-eksik", degis("PUSH: false\nKARAR_YETKİSİ: false\n", "PUSH:\n"))
durum("yetki-liste", degis("PUSH: false\nKARAR_YETKİSİ: false", "PUSH:\n  - true\nKARAR_YETKİSİ:\n  K: true"))
durum("acilis-adimlari-liste", degis("OTURUM: devam", "OTURUM: devam\nAÇILIŞ_ADIMLARI:\n  - a\n  - b"))
durum("acilis-adimlari-skaler", degis("OTURUM: devam", "OTURUM: devam\nAÇILIŞ_ADIMLARI: tek"))
durum("acilis-adimlari-sozluk", degis("OTURUM: devam", "OTURUM: devam\nAÇILIŞ_ADIMLARI:\n  A: b"))
durum("alanlar-liste-ve-sozluk", degis("AMAÇ: tek cümle amaç", "AMAÇ:\n  - madde1\n  - madde2").replace("ÖLÇEN: Jarvis ana-sıra (yapan ≠ ölçen)", "ÖLÇEN:\n  K: v\n  K2: v2").replace("TARİH: 2026-09-16", "TARİH:\n  - a"))
durum("alanlar-liste-amac-url", degis("AMAÇ: tek cümle amaç", "AMAÇ:\n  - https://a.b\n  - 'x'"))
durum("json-kacislar", degis("AMAÇ: tek cümle amaç", "AMAÇ: tırnak \" ters \\ sekme \t kontrol \x01\x1f \x7f emoji 😀 ş"))
durum("kapanis-skaler", degis("KAPANIŞ:\n  - geri-dönüş 10+2 alan\n  - git add <yol> + commit; push yok\n", "KAPANIŞ: tek\n"))
durum("devir-id-liste-cokme", degis("DEVİR_ID: devir-2026-09-16-test", "DEVİR_ID:\n  - a\n  - b"), ["gorev.md", "--cikti", "c.json"], cokme=True)
durum("devir-id-liste-varsayilan-cokme", degis("DEVİR_ID: devir-2026-09-16-test", "DEVİR_ID:\n  - a"), cokme=True)
durum("devir-id-yol-ayiracli", degis("DEVİR_ID: devir-2026-09-16-test", "DEVİR_ID: alt/kimlik"), ["gorev.md"], {"alt/x": ""})
durum("devir-id-turkce", degis("DEVİR_ID: devir-2026-09-16-test", "DEVİR_ID: devir-ğüşiöç-ÇŞ"))

# ---- --dogrula
_MD2 = TAM.replace("tek cümle amaç", "değişti")


def _uret(d, md=None):
    """Python ile bir kez türet (iki kopyada da aynı json bulunsun diye hazırlık)."""
    (d / "gorev.md").write_text(md or TAM, encoding="utf-8")
    subprocess.run(["python", str(PY), "gorev.md", "--cikti", "tur.json"], cwd=d, env=ORTAM, capture_output=True)
    (d / ".aktif-devir").unlink(missing_ok=True)


def _oncesi_es(d):
    _uret(d)


def _oncesi_fark(d):
    _uret(d, _MD2)
    (d / "gorev.md").write_text(TAM, encoding="utf-8")


def _oncesi_json(degistir):
    def f(d):
        import json
        _uret(d)
        j = json.loads((d / "tur.json").read_text(encoding="utf-8"))
        degistir(j)
        (d / "tur.json").write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding="utf-8")
        (d / ".aktif-devir").unlink(missing_ok=True)
    return f


def _devir_sil(j):
    del j["devir"]


def _devir_liste(j):
    j["devir"] = [1]


def _devir_sayi(j):
    j["devir"] = 3


def _kok_liste(j):
    j.clear()


def _bosluk_degisim(j):
    j["_sema"] = "x"


def _blok_ekle(j):
    j["devir"]["fazla"] = None
    j["devir"]["butce"]["yeni"] = 1


def _sayi_float(j):
    j["devir"]["gorev"]["yeniden_deneme"] = 2.0


def _bool_say(j):
    j["devir"]["yetki"]["push"] = 0


def _cok_blok(j):
    for k in ("kimlik", "gorev", "baglam"):
        j["devir"][k] = {}


durum("dogrula-es", TAM, ["gorev.md", "--dogrula", "tur.json"], once=_oncesi_es)
durum("dogrula-fark", TAM, ["gorev.md", "--dogrula", "tur.json"], once=_oncesi_fark)
durum("dogrula-sema-farki-yalniz", TAM, ["gorev.md", "--dogrula", "tur.json"], once=_oncesi_json(_bosluk_degisim))
durum("dogrula-devir-yok", TAM, ["gorev.md", "--dogrula", "tur.json"], once=_oncesi_json(_devir_sil))
durum("dogrula-devir-liste-cokme", TAM, ["gorev.md", "--dogrula", "tur.json"], once=_oncesi_json(_devir_liste), cokme=True)
durum("dogrula-devir-sayi-cokme", TAM, ["gorev.md", "--dogrula", "tur.json"], once=_oncesi_json(_devir_sayi), cokme=True)
durum("dogrula-kok-bos", TAM, ["gorev.md", "--dogrula", "tur.json"], once=_oncesi_json(_kok_liste))
durum("dogrula-blok-ekle", TAM, ["gorev.md", "--dogrula", "tur.json"], once=_oncesi_json(_blok_ekle))
durum("dogrula-float-esit", TAM, ["gorev.md", "--dogrula", "tur.json"], once=_oncesi_json(_sayi_float))
durum("dogrula-bool-sayi-esit", TAM, ["gorev.md", "--dogrula", "tur.json"], once=_oncesi_json(_bool_say))
durum("dogrula-cok-blok", TAM, ["gorev.md", "--dogrula", "tur.json"], once=_oncesi_json(_cok_blok))
durum("dogrula-dosya-yok-cokme", TAM, ["gorev.md", "--dogrula", "yok.json"], cokme=True)
durum("dogrula-json-degil-cokme", TAM, ["gorev.md", "--dogrula", "k.json"], {"k.json": "{bozuk"}, cokme=True)
durum("dogrula-kok-liste-cokme", TAM, ["gorev.md", "--dogrula", "k.json"], {"k.json": "[1,2]"}, cokme=True)
durum("dogrula-kok-liste-ama-esit-degil", TAM, ["gorev.md", "--dogrula", "k.json"], {"k.json": "[]"}, cokme=True)
durum("dogrula-utf8-degil-cokme", TAM, ["gorev.md", "--dogrula", "k.json"], {"k.json": b"\xff{}"}, cokme=True)
durum("dogrula-bos-dizge", TAM, ["gorev.md", "--dogrula", ""])
durum("dogrula-kok-bos-nesne", TAM, ["gorev.md", "--dogrula", "k.json"], {"k.json": "{}"})
durum("dogrula-sema-hatasi-once", degis("OTURUM: devam", "OTURUM: x"), ["gorev.md", "--dogrula", "k.json"], {"k.json": "{}"})


# ---------------------------------------------------------------- koşucu
def dosya_haritasi(kok: Path):
    h = {}
    for p in sorted(kok.rglob("*")):
        if p.is_file():
            b = p.read_bytes().replace(b"\r\n", b"\n")
            h[p.relative_to(kok).as_posix()] = b
    return h


def kos_biri(komut, d: Path):
    r = subprocess.run(komut, cwd=d, env=ORTAM, capture_output=True, stdin=subprocess.DEVNULL)
    norm = lambda b: b.decode("utf-8", "replace").replace("\r\n", "\n").replace(str(d), "<D>").replace(str(d).replace("\\", "/"), "<D>")
    return r.returncode, norm(r.stdout), norm(r.stderr), dosya_haritasi(d)


def calistir(durum_):
    ad, dosyalar, args, cokme, once = durum_
    sonuc = []
    for komut_basi in (["python", str(PY)], [RUST]):
        d = Path(tempfile.mkdtemp(prefix="dmj_"))
        try:
            for yol, ic in dosyalar.items():
                p = d / yol
                p.parent.mkdir(parents=True, exist_ok=True)
                if isinstance(ic, bytes):
                    p.write_bytes(ic)
                else:
                    p.write_bytes(ic.encode("utf-8"))
            if once:
                # hazırlık her iki kopyada da Python ile yapılır → aynı başlangıç
                once(d)
            sonuc.append(kos_biri(komut_basi + args, d))
        finally:
            shutil.rmtree(d, ignore_errors=True)
    return sonuc


def main():
    fark = 0
    cokme_listesi = []
    for dd in DURUMLAR:
        ad, _, args, cokme, _ = dd
        (kp, ko, ke, kf), (rp, ro, re_, rf) = calistir(dd)
        sorunlar = []
        if kp != rp:
            sorunlar.append(f"çıkış kodu py={kp} rust={rp}")
        if ko != ro:
            sorunlar.append(f"stdout farklı:\n  py  ={ko!r}\n  rust={ro!r}")
        if kf != rf:
            for k in sorted(set(kf) | set(rf)):
                if kf.get(k) != rf.get(k):
                    sorunlar.append(f"dosya farklı: {k}\n  py  ={kf.get(k)!r}\n  rust={rf.get(k)!r}")
        trace = "Traceback (most recent call last)" in ke
        if trace:
            cokme_listesi.append(ad)
        elif ke != re_:
            sorunlar.append(f"stderr farklı:\n  py  ={ke!r}\n  rust={re_!r}")
        if cokme and not trace:
            sorunlar.append("çökme beklenmişti ama Python traceback vermedi")
        if trace and not cokme:
            sorunlar.append("beklenmeyen Python traceback: " + ke[-300:])
        if sorunlar:
            fark += 1
            print(f"FARK [{ad}]")
            for s in sorunlar:
                print("  " + s)
    print(f"devir-md2json: {len(DURUMLAR)} durum, {fark} fark")
    print(f"Python traceback (stderr metni bilinçli ayrışır; çıkış kodu+stdout+dosyalar eşit): {len(cokme_listesi)}: {cokme_listesi}")
    return 1 if fark else 0


if __name__ == "__main__":
    sys.exit(main())
