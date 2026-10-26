#!/usr/bin/env python3
"""fark-baglam-tablo.py — baglam-tablo.py (Python) ile Rust ikilisinin çıktı/dosya farkını sınar.
Her durum için aynı sandbox'ın iki taze kopyası: biri Python, biri Rust ile koşar; çıkış kodu, stdout, stderr
ve yazılan dosyalar (sqlite → tüm tablo/görünüm dökümü, jsonl, csv; CRLF→LF; zaman/süre/betik-sha maskeli) karşılaştırılır.
Durumlar: küçük sınır-durum fixture'ı (her bayrak, hata yolu, çıkış kodu) + gerçek repo içeriğinin kopyası."""
import os, re, shutil, sqlite3, subprocess, sys, tempfile

KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
PY = os.path.join(KOK, "jarvis", "tools", "baglam-tablo.py")
if not os.path.exists(PY):
    PY = os.path.join(KOK, "arsiv", "kod", "python", "tools", "baglam-tablo.py")
RUST = os.environ.get("RUST_EXE", "C:/tmp/tgt/release/baglam-tablo.exe")
ENV = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1",
           GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")

# --------------------------------------------------------------------------- fixture içeriği
PANO = """---
tip: pano
yazar: x
---
# Pano başlık ##
Metin K-001 ve K-1234 ve K-002a V3 V12 V1234 xV5 V7-x m.12a md.3 m.007b m.1234 m.5 x.m.5 md.12ab [D] [K] [X] [ARANAMADI] [?] [Z]
2026-08-16 tarihi, 13-09 kısa, 2026-13-45 geçersiz, 99-99. sürüm 1.2.3-4 (04-05) 31-12 12-31
commit abc1234 revert deadbeefcafe 0123456789abcdef0123 face123 1234567 abcdefg. `a1b2c3d` sha 0a1b2c3 gıt aaaaaaa bbbbbbbbbbbbb ABCDEF0
[[wiki-sayfa]] [[Başka sayfa|takma]] [[x#bolum]] [[a]] [[ ]] [[|x]] [[x
y]] [[a]b]] [[abc#]]
http://example.com/a.md https://x.y/z?q=1). (https://u.v/w) http://a https://
dosyalar: core/pano.md, `tools/baglam-tablo.py`, ./core/tuzuk-v0.md, ~/sistem/jarvis/core/pano.md, /abs/path/jarvis/wiki/a.md, C:/JARVIS/CLAUDE.md, ../CLAUDE.md, README.md, nonexistent.md, dir/yok.py, a..b.md, -12.md, .md, x.json x.jsonl x.jsonlz foo.mdx bar.sh baz.ps1 q.svg r.d2 gorev-…-11.md
yol çeşitleri: /core/pano.md//x.md a/b//c.md ç/ğ.md @x.md _x.md x.md. .x.md ..md sürüm-1.md wiki/a.md/ wiki/a.md/b core/./pano.md
anahtar: Vardiya vardiyayı kapsülden şemasının skill'i panorama semantik seans başı Ana-sıra Ana sıra katman 1 katman-2 pano' pano' x pano'lar pano'abc skills zarfın İNGEST ingest123 Çelişki Staj stajyer workflow'u terminalde atlasa hakemler
Gunaydin SEANS BİTİMİ uyucam tuzuk damıtma damitma halüsinasyon pipeline antitez cowork yan oturum
skill adları: Damitma DAMİTMA damıtma x-y x- x_y xy -x seans-bitimi seans-bitimi's
Unicode: ٣ m.٣ V٣ K-٠٠١ 2026-٠٨-١٦ ² V² m.1² ǅ é́ 😀 m.1é
"""

WIKI_A = """# Wiki A
Bu [[pano]] ve [[wiki-sayfa]] bağlantılı.

## Alt başlık #

### Daha alt ###

#### dördüncü

- madde bir m.1
  - alt madde
\t- sekme girintili
- madde iki
  devam satırı
    daha girintili devam
1. numaralı
12) numaralı iki
1234. bu değil
* yıldızlı
+ artılı

> alıntı bir
> alıntı iki
   > girintili alıntı
    > dört girinti paragraf

| a | b |
|---|---|
| 1 | 2 |
| 3 | 4 |

| yalniz baslik |
sonra paragraf
| x | y |
|:--|--:|

```python
kod [tip: gizli]
```
~~~~
kapanmayan çit
"""

WIKI_B = """---
tip: wiki
---
Dosya başı #hashtag ####### yedi
#nospace
# 
#
#   
## başlık ile ## # 
---
***
___
- - -
 * * *
    ---
Paragraf satırı bir
paragraf iki
[tip: a | kaynak: b | tarih: 2026-08-01 | hedef: c | sema: v1 | önem: yüksek | geçerli_bitis: 2026-09-01]
[tip: a | kaynak: [iç] | tarih: 2026-08-02 | hedef: c | sema: v1 | extra: x]
[tip: kismi | kaynak: z]
[tip: acik
[tip: Ş_ü ğ: 1 | a:b:c | : | x | kaynak:  | tarih: 08-01 | hedef: h | sema: s]
"""

CRLF = "# CRLF Başlık\r\nsatır bir\r\n\r\n- madde\r\n"
CR_ONLY = "# CR\rsatır\r"
BOM = "\ufeff# BOM başlık\nmetin\n"
EVRENSEL_DEFTER = "# Defter\nm.9 K-007 V8\n"
SKILL = "---\nname: damitma\n---\n# Damıtma skill\nbkz references/ref.md ve ref.md ve SKILL.md ve ../x/SKILL.md\n"
SKILL_REF = "# Ref\nİç bağ [[pano]]\n"

JSON_GECERLI = '{"a": 1, "b": [1.0, 1e5, 1E-7, 0.1, 1e16, 123456789012345678901234567890, -0, -0.0, 2.5e+3, 1e999, -1e999, 12345678901234567890123.5], "c": {"d": null, "e": true, "f": false}, "g/h~i": "\\u00e9\\ud83d\\ude00\\n\\t\\"x\\"", "a": 2, "bos": {}, "bosl": [], "": "anahtarsız", "uzun": 10000000000000000, "kucuk": 0.00001}\n'
JSON_NAN = '[NaN, Infinity, -Infinity, 1.5]'
JSON_SKALER = '"yalniz metin"'
JSON_BOZUKLAR = {
    "j-virgul.json": '{"a":1,}',
    "j-dizi-virgul.json": '[1,]',
    "j-iki-nokta.json": '{"a" 1}',
    "j-anahtar.json": '{a:1}',
    "j-acik-dize.json": '{"a": "abc',
    "j-kontrol.json": '{"a": "x\u0001y"}',
    "j-fazla.json": '{"a":1} x',
    "j-bos.json": '',
    "j-bosluk.json": '  \n ',
    "j-nul.json": 'nul',
    "j-virgulsuz.json": '[1 2]',
    "j-kacis.json": '{"a":"\\q"}',
    "j-uxx.json": '{"a":"\\u12"}',
    "j-tru.json": '{"a":tru}',
    "j-cok-satir.json": '{\n  "a": 1,\n  "b": [\n    1,\n    2,\n  ]\n}',
    "j-sayi.json": '[01]',
    "j-eksi.json": '[-]',
    "j-eksi2.json": '-',
    "j-e.json": '[1e]',
    "j-nokta.json": '[1.]',
    "j-derin.json": '[' * 3000,
    "j-derin2.json": '{"a":' * 3000,
    "j-uzun-mesaj-uzun-mesaj-uzun-mesaj-uzun-mesaj-uzun-mesaj-uzun-mesaj-uzun-mesaj-uzun-mesaj.json": '{"a":1,}',
}
JSONL = '{"a": 1}\n\n   \n{"b": [1, 2]}\n"s"\n{"c": null}\n'
JSONL_BOZUK = '{"a": 1}\n{"b": \n'
JSONL_BOM = '{"a": 1}\n\ufeff{"b": 1}\n'
JSONL_CRLF = '{"a": 1}\r\n{"b": 2}\r\n'
CEKIM = ('# yorum\n\n{"dosya_id": "core/pano.md", "cekim_tarihi": "2030-01-01T10:00:00"}\n'
         '{"dosya_id": "wiki/a.md", "cekim_tarihi": "2020-01-01"}\nbozuk json\n'
         '{"dosya_id": "wiki/a.md", "cekim_tarihi": "2031-02-03"}\n{"dosya_id": "", "cekim_tarihi": "2040-01-01"}\n'
         '{"dosya_id": "yok/dosya.md", "cekim_tarihi": "2032-01-01"}\n{"cekim_tarihi": "2033-01-01"}\n'
         '{"dosya_id": "core/pano.md", "cekim_tarihi": null}\n{"dosya_id": "kuyruk/k.md"}\n')


def yaz(yol, icerik, kip="w"):
    os.makedirs(os.path.dirname(yol), exist_ok=True)
    if isinstance(icerik, bytes):
        open(yol, "wb").write(icerik)
    else:
        open(yol, "w", encoding="utf-8", newline="").write(icerik)


def git(d, *a, tarih=None):
    env = dict(ENV)
    if tarih:
        env["GIT_AUTHOR_DATE"] = env["GIT_COMMITTER_DATE"] = tarih
    return subprocess.run(["git", "-c", "core.autocrlf=false", "-c", "core.quotepath=off"] + list(a), cwd=d, env=env,
                          stdin=subprocess.DEVNULL, capture_output=True)


def fixture(d):
    """Küçük sınır-durum deposu (3 commit, bir yeniden adlandırma)."""
    os.makedirs(d)
    git(d, "init", "-q")
    yaz(d + "/CLAUDE.md", "# CLAUDE\nKanon m.1 V1 K-001 damitma\n")
    yaz(d + "/core/pano.md", PANO)
    yaz(d + "/core/tuzuk-v0.md", "# Tüzük\nm.1 m.2 md.3 m.12a\n")
    yaz(d + "/core/durum-kapsulu.md", "# Kapsül\nçok\n")
    yaz(d + "/wiki/a.md", WIKI_A)
    yaz(d + "/wiki/wiki-sayfa.md", "# W\n[[a]]\n")
    yaz(d + "/wiki/sozluk.md", "# Sözlük\n")
    yaz(d + "/wiki/b.md", WIKI_B)
    yaz(d + "/wiki/.md", "gizli\n")
    yaz(d + "/kuyruk/gelen-x.md", "# Gelen\n")
    yaz(d + "/kuyruk/fikir-kutusu-y.md", "# Kutu\n")
    yaz(d + "/kuyruk/defter-z.md", EVRENSEL_DEFTER)
    yaz(d + "/kuyruk/defter-sema.md", "# Defter şema\n")
    yaz(d + "/kuyruk/k.md", "# K\n")
    yaz(d + "/cc/gorev/2026-08/gorev-1.md", "# Görev\n")
    yaz(d + "/cc/rapor/rapor-1.md", "# Rapor\n")
    yaz(d + "/cc/pipeline/p.md", "# Pipeline\n")
    yaz(d + "/cc/defter.md", "# Defter\n")
    yaz(d + "/cc/README.md", "# CC\n")
    yaz(d + "/raporlar/vardiya-teslim-1.md", "# Teslim\n")
    yaz(d + "/raporlar/x.jsonl", JSONL)
    yaz(d + "/raporlar/y.md", "# Y\n")
    yaz(d + "/ogrenme/dersler/d.md", "# Ders\n")
    yaz(d + "/ogrenme/x.md", "# Öğrenme\n")
    yaz(d + "/arsiv/chat-model-degisikligi/c.md", "# Chat\n")
    yaz(d + "/arsiv/a.md", "# Arşiv\n")
    yaz(d + "/diger/arsiv-x.md", "# a\n")
    yaz(d + "/diger/x-arsiv.md", "# a\n")
    yaz(d + "/diger/rapor-q.md", "# Rapor adlı\n")
    yaz(d + "/diger/z.md", "# Diğer\n")
    yaz(d + "/diger/özel çalışma/ünlü.md", "# Ünlü\n")
    yaz(d + "/KÖK.MD", "# Büyük uzantı\n")
    yaz(d + "/README.md", "# Readme\n")
    yaz(d + "/.claude/skills/damitma/SKILL.md", SKILL)
    yaz(d + "/.claude/skills/damitma/references/ref.md", SKILL_REF)
    yaz(d + "/.claude/skills/damitma/evals/e.json", '{"q": "?"}')
    yaz(d + "/.claude/skills/seans-bitimi/SKILL.md", "# S\n")
    yaz(d + "/.claude/skills/x/SKILL.md", "# x\n")
    yaz(d + "/.claude/skills/x-y/SKILL.md", "# x-y\n")
    yaz(d + "/.claude/skills/Buyuk/SKILL.md", "# Buyuk\n")
    yaz(d + "/.claude/skills/yok-skill/notlar.md", "# skill md'si yok\n")
    yaz(d + "/.claude/settings.json", '{"gizli": "sır", "x": [1,2]}')
    yaz(d + "/.mcp.json", '{"mcp": 1}')
    yaz(d + "/veri/a.json", JSON_GECERLI)
    yaz(d + "/veri/nan.json", JSON_NAN)
    yaz(d + "/veri/skaler.json", JSON_SKALER)
    yaz(d + "/veri/b.jsonl", JSONL)
    yaz(d + "/veri/bozuk.jsonl", JSONL_BOZUK)
    yaz(d + "/veri/bom.jsonl", JSONL_BOM)
    yaz(d + "/veri/crlf.jsonl", JSONL_CRLF)
    yaz(d + "/veri/bos.jsonl", "")
    for ad, ic in JSON_BOZUKLAR.items():
        yaz(d + "/veri/bozuk/" + ad, ic)
    yaz(d + "/bin/crlf.md", CRLF)
    yaz(d + "/bin/cr.md", CR_ONLY)
    yaz(d + "/bin/bom.md", BOM)
    yaz(d + "/bin/bos.md", "")
    yaz(d + "/bin/satir-sonsuz.md", "# Sonsuz\nson satır")
    yaz(d + "/bin/gecersiz1.md", b"# Ge\xffcersiz\nmetin\n")
    yaz(d + "/bin/gecersiz2.md", b"abc \xe2\x82 x\n")
    yaz(d + "/bin/gecersiz3.md", b"abc \xe2\x82")
    yaz(d + "/bin/gecersiz4.md", b"abc \xed\xa0\x80 x")
    yaz(d + "/bin/gecersiz5.md", b"\xc0\xaf")
    yaz(d + "/bin/gecersiz6.json", b'{"a": "\xff"}')
    yaz(d + "/bin/diger.txt", "metin dosyası, hedef dışı\n")
    yaz(d + "/bin/uzun.md", "# Uzun\n" + ("kelime " * 3000) + "\n")
    yaz(d + "/bin/ayni.md", "# Aynı\nmetin\n\nmetin\n\nmetin\n")
    # 5000+ satır → CSV kesme uyarısı
    yaz(d + "/bin/cok-url.md", "# URL\n" + "".join("https://e.com/u%d\n" % i for i in range(5200)))
    # rastgele (tohumlu) parçalardan üretilmiş metinler: elle yazılmış tarayıcıların sınır davranışı
    import random
    parcalar = ["m.", "md.", "V", "K-", "[[", "]]", "[", "]", "|", "#", "http://", "https://", "x.md", "core/", "wiki/", "/", "../", "./", "~/sistem/jarvis/", "C:/JARVIS/", "/jarvis/",
                "12", "123", "1234", "007", "a", "b", "ab", "s", "'", "-", ".", "_", " ", "  ", "\t", "pano", "skill", "damitma", "x-y", "vardiya", "ana", "sira", "katman", "1", "2",
                "kapsul", "zarf", "sema", "ç", "ı", "İ", "Ş", "ö", "é", "٣", "²", "2026-08-16", "13-09", "2026-13-01", "abcdef0", "deadbeef", "commit ", "git", "(", ")", "`", "\"", "tip:", "kaynak:",
                ".json", ".jsonl", ".py", ".sh", ".ps1", ".svg", ".d2", "yol.md", "@", "\\", ">", "*", "+", "~~~", "```", "yle", "dan", "lar", "lik", "siz", "ken", "mis", "mus", "ne", "ya", "lerin", "dir", "sı", "!", "?", ",", ";", ":", "…", "\u00a0"]
    for tohum in range(int(os.environ.get("FUZZ_N", "6"))):
        rnd = random.Random(1000 + tohum)
        satirlar = []
        for _ in range(350):
            satirlar.append("".join(rnd.choice(parcalar) for _ in range(rnd.randint(0, 14))))
        yaz(d + "/bin/fuzz-%d.md" % tohum, "\n".join(satirlar) + "\n")
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", "ilk", tarih="2026-08-01T10:00:00+03:00")
    yaz(d + "/core/pano.md", PANO + "ek satır\n")
    yaz(d + "/wiki/a.md", WIKI_A + "\nek\n")
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", "ikinci", tarih="2026-08-05T12:30:00+03:00")
    git(d, "mv", "kuyruk/k.md", "kuyruk/k-yeni.md")
    git(d, "mv", "wiki/b.md", "wiki/b-yeni.md")
    git(d, "commit", "-q", "-m", "ad", tarih="2026-09-01T08:00:00+03:00")
    git(d, "mv", "kuyruk/k-yeni.md", "kuyruk/k-son.md")
    yaz(d + "/kuyruk/k-son.md", "# K son\nküçük değişiklik\n")
    yaz(d + "/yeni-dosya.md", "# Yeni\n")
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", "ad2", tarih="2026-09-02T09:00:00+03:00")
    # takip edilmeyen dosya (görünmemeli)
    yaz(d + "/izlenmeyen.md", "# İzlenmeyen\n")


def gercek_kopya(d):
    """Gerçek deponun jarvis/ içeriği (git ls-files) → geçici git deposu (iki commit)."""
    os.makedirs(d)
    r = subprocess.run(["git", "ls-files", "-z", "jarvis"], cwd=KOK, stdin=subprocess.DEVNULL, capture_output=True)
    dosyalar = [x.decode("utf-8") for x in r.stdout.split(b"\0") if x]
    for f in dosyalar:
        k = os.path.join(KOK, f)
        if not os.path.isfile(k):
            continue
        h = os.path.join(d, f[len("jarvis/"):])
        os.makedirs(os.path.dirname(h), exist_ok=True)
        shutil.copyfile(k, h)
    git(d, "init", "-q")
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", "ilk", tarih="2026-08-01T10:00:00+03:00")
    # ikinci commit: birkaç dosyada değişiklik (ilk/son commit ayrışsın)
    n = 0
    for f in sorted(dosyalar):
        if f.endswith(".md") and n < 20:
            h = os.path.join(d, f[len("jarvis/"):])
            if os.path.isfile(h):
                open(h, "ab").write(b"\n")
                n += 1
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", "ikinci", tarih="2026-09-10T10:00:00+03:00")


# --------------------------------------------------------------------------- karşılaştırma
def maskele(s, taban):
    for b in {taban, taban.replace("\\", "/"), taban.replace("/", "\\"), taban.replace("\\", "\\\\")}:
        s = s.replace(b, "<B>")
    s = s.replace("\r\n", "\n")
    s = re.sub(r'("sure_sn": )[0-9.eE+-]+', r"\1<S>", s)
    return s


def sqlite_dok(yol):
    con = sqlite3.connect(yol)
    out = []
    for ad, tur, sql in con.execute("SELECT name, type, sql FROM sqlite_master ORDER BY type, name"):
        out.append("## %s %s\n%s" % (tur, ad, sql))
        if tur in ("table", "view") and not ad.startswith("sqlite_"):
            kolon = [c[1] for c in con.execute("PRAGMA table_info(%s)" % ad)] if tur == "table" else None
            cur = con.execute("SELECT * FROM %s" % ad)
            ad_kol = [c[0] for c in cur.description]
            satirlar = cur.fetchall()
            if ad == "uretim":
                # zaman/süre/betik-sha/sürüm maskeli
                m = []
                for r in satirlar:
                    r = list(r)
                    for i, k in enumerate(ad_kol):
                        if k in ("uretim_zamani", "sure_sn", "python_surumu", "script_sha"):
                            r[i] = "<M>"
                    m.append(tuple(r))
                satirlar = m
            if tur == "view":
                # görünümün kendi ORDER BY'ı var; eşit sıralı satırlarda sıra belirsiz olabilir → sıralayıp karşılaştır
                satirlar = sorted(satirlar, key=lambda r: repr(r))
            else:
                satirlar = sorted(satirlar, key=lambda r: repr(r))
            out.append(repr(ad_kol))
            for r in satirlar:
                out.append(repr(tuple((type(v).__name__, v) for v in r)))
    con.close()
    return "\n".join(out)


def dosyalar(kok):
    sonuc = {}
    for dp, dn, fn in os.walk(kok):
        if ".git" in dn:
            dn.remove(".git")
        for f in fn:
            p = os.path.join(dp, f)
            sonuc[os.path.relpath(p, kok).replace("\\", "/")] = p
    return sonuc


def icerik_al(p, taban):
    if p.endswith(".sqlite"):
        try:
            return sqlite_dok(p)
        except sqlite3.DatabaseError:
            return "<sqlite okunamadi> " + repr(open(p, "rb").read()[:50])
    b = open(p, "rb").read()
    try:
        s = b.decode("utf-8")
    except UnicodeDecodeError:
        return repr(b)
    return maskele(s, taban)


def calistir(komut, cwd):
    r = subprocess.run(komut, cwd=cwd, env=ENV, stdin=subprocess.DEVNULL, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", "replace"), r.stderr.decode("utf-8", "replace")


FARK = []
SAYAC = 0


def durum(ad, kur, argumanlar, izle, py_traceback=False):
    """kur(dizin): sandbox'ı kurar; argumanlar(dizin) -> argv listesi; izle: karşılaştırılacak alt dizinler (taban göre)."""
    global SAYAC
    if os.environ.get("DURUM_FILTRE") and os.environ["DURUM_FILTRE"] not in ad:
        return
    SAYAC += 1
    kok = tempfile.mkdtemp(prefix="bt-fark-")
    sabit = os.path.join(kok, "sabit")
    kur(sabit)
    sonuc = {}
    for tur, komut in (("py", [sys.executable, PY]), ("rs", [RUST])):
        d = os.path.join(kok, tur)
        shutil.copytree(sabit, d)
        # git'in "dubious ownership" vb. sorunları olmasın diye yalnız kopya
        kod, so, se = calistir(komut + argumanlar(d), d)
        so, se = maskele(so, d), maskele(se, d)
        dos = {}
        for alt in izle:
            for rel, p in sorted(dosyalar(os.path.join(d, alt)).items()) if os.path.isdir(os.path.join(d, alt)) else []:
                dos[alt + "/" + rel] = icerik_al(p, d)
        sonuc[tur] = (kod, so, se, dos)
    py, rs = sonuc["py"], sonuc["rs"]
    ayrik = []
    if py[0] != rs[0]:
        ayrik.append("çıkış kodu py=%s rs=%s" % (py[0], rs[0]))
    if py[1] != rs[1]:
        ayrik.append("stdout farklı:\n--py--\n%s\n--rs--\n%s" % (py[1][:1500], rs[1][:1500]))
    if py[2] != rs[2]:
        if py_traceback:
            ayrik.append("[MESRU] stderr (traceback) farklı; py: %r | rs: %r" % (py[2][-200:], rs[2][:200]))
        else:
            ayrik.append("stderr farklı:\n--py--\n%s\n--rs--\n%s" % (py[2][:1500], rs[2][:1500]))
    for k in sorted(set(py[3]) | set(rs[3])):
        a, b = py[3].get(k), rs[3].get(k)
        if a != b:
            if a is None or b is None:
                ayrik.append("dosya yalnız bir tarafta: %s (py=%s rs=%s)" % (k, a is not None, b is not None))
            else:
                al, bl = a.split("\n"), b.split("\n")
                n = 0
                for x, y in zip(al, bl):
                    if x != y:
                        break
                    n += 1
                ayrik.append("dosya farklı: %s (ilk fark satır %d)\n  py: %s\n  rs: %s" % (k, n, (al[n] if n < len(al) else "<yok>")[:600], (bl[n] if n < len(bl) else "<yok>")[:600]))
    resmi = [a for a in ayrik if not a.startswith("[MESRU]")]
    print("%-46s kod=%s/%s dosya=%d %s" % (ad, py[0], rs[0], len(py[3]), "OK" if not resmi else "FARK"))
    for a in ayrik:
        print("    " + a.replace("\n", "\n    "))
    if resmi:
        FARK.append(ad)
    shutil.rmtree(kok, ignore_errors=True)


def main():
    global SAYAC
    if not os.path.exists(RUST):
        print("Rust ikilisi yok: " + RUST)
        sys.exit(2)

    # --- fixture: sandbox kökü = depo; çıktı dizini deponun dışında (oto-silinen kök içinde)
    def a_repo_cikti(d):
        return ["--repo", d + "/repo", "--cikti", d + "/cikti"]

    def kur_depo(d):
        os.makedirs(d)
        fixture(d + "/repo")

    def kur_depo_cekim(d):
        os.makedirs(d)
        fixture(d + "/repo")
        yaz(d + "/cikti/bronz/cekim-olay.jsonl", CEKIM)

    def kur_depo_eski(d):
        os.makedirs(d)
        fixture(d + "/repo")
        yaz(d + "/cikti/baglam.sqlite", "eski sqlite")
        yaz(d + "/cikti/baglam.sqlite.tmp", "eski tmp")
        yaz(d + "/cikti/baglam.jsonl", "eski\n")
        yaz(d + "/cikti/gorunum/v_x_olcum.csv", "eski\n")

    durum("fix: --repo --cikti", kur_depo, a_repo_cikti, ["cikti"])
    durum("fix: --sessiz", kur_depo, lambda d: a_repo_cikti(d) + ["--sessiz"], ["cikti"])
    durum("fix: cekim-olay bronz", kur_depo_cekim, a_repo_cikti, ["cikti"])
    durum("fix: eski çıktı + .tmp üzerine yazma", kur_depo_eski, a_repo_cikti, ["cikti"])
    durum("fix: --cikti yok → <repo>/veri", kur_depo, lambda d: ["--repo", d + "/repo"], ["repo/veri"])
    durum("fix: önek kısaltma --rep/--cik/--ses", kur_depo, lambda d: ["--rep", d + "/repo", "--cik", d + "/cikti", "--ses"], ["cikti"])
    durum("fix: --repo=... --cikti=...", kur_depo, lambda d: ["--repo=" + d + "/repo", "--cikti=" + d + "/cikti"], ["cikti"])
    durum("fix: göreli --repo/--cikti (cwd)", kur_depo, lambda d: ["--repo", "repo", "--cikti", "cikti"], ["cikti"])
    durum("fix: iç içe yeni çıktı dizini", kur_depo, lambda d: ["--repo", d + "/repo", "--cikti", d + "/a/b/c"], ["a"])

    # --- hata yolları
    def kur_bos(d):
        os.makedirs(d)

    def kur_git_degil(d):
        os.makedirs(d + "/x")
        yaz(d + "/x/a.md", "# a\n")

    def kur_bos_depo(d):
        os.makedirs(d + "/r")
        git(d + "/r", "init", "-q")

    def kur_commitsiz(d):
        os.makedirs(d + "/r")
        git(d + "/r", "init", "-q")
        yaz(d + "/r/a.md", "# a\n")
        git(d + "/r", "add", "-A")

    def kur_silinmis(d):
        os.makedirs(d + "/r")
        git(d + "/r", "init", "-q")
        yaz(d + "/r/a.md", "# a\n")
        yaz(d + "/r/b.md", "# b\n")
        git(d + "/r", "add", "-A")
        git(d + "/r", "commit", "-q", "-m", "x", tarih="2026-08-01T10:00:00+03:00")
        os.remove(d + "/r/b.md")

    def kur_yalniz_hedefsiz(d):
        os.makedirs(d + "/r")
        git(d + "/r", "init", "-q")
        yaz(d + "/r/a.txt", "x\n")
        git(d + "/r", "add", "-A")
        git(d + "/r", "commit", "-q", "-m", "x", tarih="2026-08-01T10:00:00+03:00")

    def kur_skillsiz(d):
        os.makedirs(d + "/r")
        git(d + "/r", "init", "-q")
        yaz(d + "/r/a.md", "# a\nskill damitma\n")
        git(d + "/r", "add", "-A")
        git(d + "/r", "commit", "-q", "-m", "x", tarih="2026-08-01T10:00:00+03:00")

    durum("hata: olmayan --repo", kur_bos, lambda d: ["--repo", d + "/yok", "--cikti", d + "/c"], ["c"])
    durum("hata: git deposu değil", kur_git_degil, lambda d: ["--repo", d + "/x", "--cikti", d + "/c"], ["c"])
    durum("hata: boş depo (izlenen yok)", kur_bos_depo, lambda d: ["--repo", d + "/r", "--cikti", d + "/c"], ["c"])
    durum("hata: commit'siz depo", kur_commitsiz, lambda d: ["--repo", d + "/r", "--cikti", d + "/c"], ["c"], py_traceback=True)
    durum("hata: izlenen ama silinmiş dosya", kur_silinmis, lambda d: ["--repo", d + "/r", "--cikti", d + "/c"], ["c"], py_traceback=True)
    durum("kenar: hedef uzantısız depo", kur_yalniz_hedefsiz, lambda d: ["--repo", d + "/r", "--cikti", d + "/c"], ["c"])
    durum("kenar: skills dizini yok", kur_skillsiz, lambda d: ["--repo", d + "/r", "--cikti", d + "/c"], ["c"])

    # --- Python'da yakalanmamış istisna (kayıp vekil çifti sqlite'a yazılamaz): çıkış kodu + stdout eşit olmalı
    def kur_vekil(d):
        os.makedirs(d + "/r")
        git(d + "/r", "init", "-q")
        yaz(d + "/r/v.json", '"\\ud800"')
        git(d + "/r", "add", "-A")
        git(d + "/r", "commit", "-q", "-m", "x", tarih="2026-08-01T10:00:00+03:00")

    durum("çökme: kayıp vekil JSON", kur_vekil, lambda d: ["--repo", d + "/r", "--cikti", d + "/c"], [], py_traceback=True)

    # --- argparse
    for ad, arg in (("--help", ["--help"]), ("-h", ["-h"]), ("bilinmeyen bayrak", ["--bogus"]), ("eksik değer", ["--repo"]),
                    ("--sessiz=1", ["--sessiz=1"]), ("konumsal arg", ["x"]), ("belirsiz önek", ["--"]), ("-- ayırıcı", ["--", "x"])):
        durum("argparse: " + ad, kur_bos, lambda d, a=arg: a, ["."])

    # --- gerçek repo içeriği
    def kur_gercek(d):
        os.makedirs(d)
        gercek_kopya(d + "/repo")

    durum("GERÇEK repo içeriği kopyası", kur_gercek, a_repo_cikti, ["cikti"])
    durum("GERÇEK repo: ikinci koşu üzerine yazma", lambda d: (kur_gercek(d), os.makedirs(d + "/cikti")), a_repo_cikti, ["cikti"])

    print("\n=== baglam-tablo: %d durum, %d fark %s" % (SAYAC, len(FARK), FARK if FARK else ""))
    sys.exit(1 if FARK else 0)


if __name__ == "__main__":
    main()
