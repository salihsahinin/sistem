#!/usr/bin/env python3
"""fark-anakronizm-denetim.py — anakronizm-denetim.py (Python) ↔ anakronizm-denetim (Rust) fark testi.
Aynı kum havuzunun (git repo) iki taze kopyasında iki uygulamayı koşar; çıkış kodu, stdout, stderr ve yazılan dosyalar karşılaştırılır.
Python betiği kum/jarvis/tools/ altına kopyalanır (varsayılan repo = betik konumunun üst dizini); Rust için CLAUDE_PROJECT_DIR = kum/jarvis.
Maskelenenler: ts damgası (saat), kum yolu. Python'da yakalanmamış istisna (çıkış 1) durumunda yalnız çıkış kodu + stdout karşılaştırılır."""
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile

DEPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
PY_ARAC = os.path.join(DEPO, "jarvis", "tools", "anakronizm-denetim.py")
if not os.path.exists(PY_ARAC):
    PY_ARAC = os.path.join(DEPO, "arsiv", "kod", "python", "tools", "anakronizm-denetim.py")
RUST_EXE = os.environ.get("RUST_EXE", "C:/tmp/tgt/release/anakronizm-denetim.exe")
ENV_GIT = {"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t",
           "GIT_AUTHOR_DATE": "2026-09-01T10:00:00+03:00", "GIT_COMMITTER_DATE": "2026-09-01T10:00:00+03:00"}


def git(cwd, *a):
    e = dict(os.environ, **ENV_GIT)
    subprocess.run(["git", *a], cwd=cwd, stdin=subprocess.DEVNULL, capture_output=True, check=True, env=e)


# ---------------------------------------------------------------- içerik
SOZ = ["şu an", "ŞU AN", "şu anda", "Şu Anda", "şimdilik", "ŞİMDİLİK", "şimdilik", "hâlâ", "HÂLÂ", "hala", "HALA", "artık", "ARTIK", "henüz", "HENÜZ", "yakında",
       "YAKINDA", "son zamanlarda", "en güncel", "EN GÜNCEL", "en güçlü", "EN GÜÇLÜ", "en son sürüm", "en yeni", "EN YENİ", "bugün itibarıyla", "BUGÜN İTİBARIYLA",
       "bugün itibariyla", "bugün itibarıyla", "bu yazının yazıldığı", "yeni sürüm", "YENİ SÜRÜM", "desteklenmiyor", "DESTEKLENMİYOR", "resmî SDK'sı yok", "resmî sdk'si yok",
       "RESMÎ SDK'SI YOK", "resmi sdk'sı yok", "henüz yok", "HENÜZ YOK", "şu anlar", "arıtık", "artıkça", "xhala", "hala_", "halaş", "halaŞ",
       "v1.2", "v1.2.3", "V2.0", "sürüm 3", "Sürüm3", "SÜRÜM 4", "sürüm", "pass@1", "PASS@10", "skor: 85", "SKOR 85,5%", "doğruluk=%12", "Doğruluk %9,5",
       "recall 99", "nDCG: 0,8", "NDCG 12", "F1 90", "f1: 100%", "başarı %77", "BAŞARI 33", "başarılı 55", "skorlar:%12", "skor", "skor 1234",
       "2026-09-01", "2026-09", "2026-9-1", "AS-OF", "as of", "AS OF", "ASOF", "as-of", "çekim 2026", "çekimi tarihi 2026", "ÇEKİMİ 2025", "çekim tarihi2026",
       "son teyit", "SON-TEYİT", "son-teyit", "son  teyit", "Kayıt: 2026", "KAYIT:2026", "kayıt: 2026", "12-31", "12-31x", "12-31 ", "12-310", "1-12", "09/2026", "9-2026", "13/2026",
       "Ocak 2026", "ŞUBAT 2026", "şubat 2026", "Mart2026", "Nisan  2026", "MAYIS 2026", "Haziran 2026", "Temmuz 2026", "Ağustos 2026", "AĞUSTOS 2026", "Eylül 2026", "Ekim 2026",
       "EKİM 2026", "Kasım 2026", "KASIM 2026", "Aralık 2026", "ARALIK 2026", "Jan 2026", "JANUARY '26", "Feb 26", "March 2026", "SEPT 26", "Octİ 26", "Noıv 2026", "Dec 12", "Decİ 2026",
       "dec 1", "Mayıs", "2024", "2099", "1999", "20260", "x2026", "2026x", "a_2026", "2026_", "٢٠٢٦-٠٩-٠١", "2026-٠٩-01",
       "alpha", "beta", "metin", "kelime", "ŞİMDİLİKX", "ışık", "İŞTE", "ıİiI", "ſ", "\u212a",
       "e\u0301", "a\u0327", "ş\u0301u an", "şu\u0301 an", "x\u0301artık", "artık\u0301", "artık\u200d", "\u200dartık", "artık‿", "‿artık", "ⅷartık", "artık²", "²artık", "artık½",
       "```", "|---|---|", "| a | b |", "# Başlık", "- madde", "tutarlı", "ÇÖĞÜŞİ"]
AYRAC = [" ", " ", " ", "\n", "\n", "\n\n", "\t", "\u00a0", "\x1c", "\u2003", ", ", ". ", ": ", " - ", "(", ")", "\r\n", "\r", "\u3000", "\x0b", "\x0c", "\u2028", "\x85"]


def gurultu(rnd, n_par):
    """Rastgele (sabit tohum) paragraflar."""
    out = []
    for _ in range(n_par):
        k = rnd.randint(1, 9)
        s = ""
        for _ in range(k):
            s += rnd.choice(SOZ) + rnd.choice(AYRAC)
        out.append(s)
        out.append(rnd.choice(["\n\n", "\n\n", "\n", "\n \n", "\n\t\n", "\n\u00a0\n", "\n\x1c\n"]))
    return "".join(out)


def kum_kur(yol):
    j = os.path.join(yol, "jarvis")
    os.makedirs(j)
    git(j, "init", "-q")
    git(j, "config", "core.autocrlf", "false")
    git(j, "config", "core.quotepath", "false")

    def yaz(rel, veri):
        p = os.path.join(j, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as f:
            f.write(veri if isinstance(veri, bytes) else veri.encode("utf-8"))

    yaz("wiki/temiz.md", "# Temiz\n\nKayıt: 2026-09-01\n\nsürüm 3 (2026-09-01) ile gelen v1.2 değişikliği.\n")
    yaz("wiki/damgasiz.md", "# Damgasız\n\nşu an en güncel sürüm kullanılıyor.\n\nv2.1 çıktı.\n")
    yaz("wiki/bos.md", "")
    yaz("wiki/sadece-bosluk.md", "\n\n   \n\t\n")
    yaz("wiki/kod-blogu.md", "# T\n2026-09-01\n\n```\nşu an v1.0 skor: 85\n```\n\nartık tamam\n\n  ```py\nhala v9.9\n```\n\nhenüz\n")
    yaz("wiki/tablo.md", "2026-09-01\n\n|---|---|\n| şu an | v1.2 |\n\n  |---| şimdilik\n\n| a | b |\n|---|---|\n| skor 5 | x |\n")
    yaz("wiki/uzun.md", "2026-01-01\n\n" + ("şimdilik çok uzun satır ğüşiöç " * 20) + "\n\n" + "x" * 300 + " v1.1\n")
    yaz("wiki/crlf.md", "# Başlık\r\n\r\nşu an v1.0\r\n\r\n2026-09-02 tarihli\r\nartık\r\n")
    yaz("wiki/cr.md", "# Başlık\r\rşu an v1.0\r\r2026-09-02\r")
    yaz("wiki/bom.md", b"\xef\xbb\xbf# Ba\xc5\x9fl\xc4\xb1k\n\n\xc5\x9fu an\n")
    yaz("wiki/gecersiz-utf8.md", b"2026-09-01\n\nbad \xff\xfe \xed\xa0\x80 \xc3 \xe2\x82 \xf0\x9f\x98 son\n\nv1.2 \x80x\n")
    yaz("wiki/Türkçe-ad.md", "# Ad\n\nşimdilik\n")
    yaz("wiki/bayat.md", "Güncelleme: 2026-01-01\nson teyit: 2026-03-04\n\n2025-12-31 eski\n")
    yaz("wiki/gelecek.md", "2030-01-01\n2026-09-01\n")
    yaz("wiki/gecersiz-tarih.md", "2026-02-30\n0000-01-01\n2026-13-01\n٢٠٢٦-٠٩-٠١\n2026-02-28\n")
    yaz("wiki/sadece-gelecek.md", "2031-05-05 gelecek\n")
    yaz("wiki/damga-13.md", "\n" * 12 + "2026-09-01\n")
    yaz("wiki/damga-12.md", "\n" * 11 + "2026-09-01\n")
    yaz("wiki/cekimli.md", "AS-OF 2026-01-02\n\nşu an\n")
    yaz("wiki/cekimli2.md", "Kayıt: 2026\n")
    yaz("wiki/cekimsiz.md", "başlık yok\n")
    yaz("wiki/ayni.md", "2026-09-01\n")
    yaz("wiki/ic/derin.md", "şimdilik v1.2\n")
    yaz("wiki/not.txt", "şimdilik v1.2\n")
    yaz("wiki/ozel-etiketli.md", "2026-09-01 " + "v1.2 " * 3 + "\n\nskor: %50\n")
    yaz("core/a.md", "başlık\n\nhenüz yok\n")
    yaz("core/sablonlar/s.md", "şu an\n")
    yaz("core/alt/sablonlar/s2.md", "şu an\n")
    yaz("core/sablonlar2/x.md", "şu an\n")
    yaz("core/2026-09-03-x.md", "şu an\n")
    yaz("raporlar/2026-09-03-a.md", "şu an v1.2\n\nson teyit: 2026-05-01\n")
    yaz("raporlar/2026-09-03-eski.md", "şu an v1.2\n\nson teyit: 2025-05-01\n")
    yaz("raporlar/2026-07-01-sinir.md", "x\n")
    yaz("raporlar/2026-08-21-sinir.md", "x 2026-08-21\n")
    yaz("raporlar/2026-08-20-sinir.md", "x 2026-08-20\n")
    yaz("raporlar/tarihsiz.md", "şu an v1.2\n")
    yaz("raporlar/alt/2026-09-10-b.md", "2026-09-10\n")
    yaz("raporlar/alt/2026-09-12.txt", "txt\n")
    yaz("cc/rapor/rapor-2026-09-05-x.md", "artık\n\nv3.0\n")
    yaz("cc/rapor/rapor-tarihsiz.md", "artık\n")
    yaz("cc/rapor/2026-01-01-eski.md", "artık\n")
    yaz("cc/notlar-2026-09-05.md", "artık\n")
    yaz("cc/baska.md", "artık\n")
    yaz("diger/x.md", "şu an\n")
    yaz("README.md", "şu an\n")
    # rastgele gürültü dosyaları (sabit tohum): her kalıp ailesi, ayraçlar, birleştirici işaretler
    rnd = random.Random(20260917)
    for i in range(12):
        yaz("wiki/gurultu-%02d.md" % i, ("2026-09-01\n\n" if i % 3 == 0 else "") + gurultu(rnd, 60))
    for i in range(4):
        yaz("core/gurultu-%02d.md" % i, gurultu(rnd, 60))
    git(j, "add", "-A")
    # izlenmeyen dosyalar
    yaz("wiki/izlenmeyen.md", "şu an\n")
    yaz("veri/bronz/.tutucu", "")
    os.makedirs(os.path.join(j, "veri", "gorunum"), exist_ok=True)
    git(j, "commit", "-q", "-m", "ilk")
    os.makedirs(os.path.join(j, "tools"), exist_ok=True)
    shutil.copy(PY_ARAC, os.path.join(j, "tools", "anakronizm-denetim.py"))
    return j


def cekim_yaz(j, satirlar):
    p = os.path.join(j, "veri", "bronz", "cekim-olay.jsonl")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "wb") as f:
        f.write(satirlar if isinstance(satirlar, bytes) else satirlar.encode("utf-8"))


CEKIM_IYI = "\n".join([
    "# yorum", "", "   ",
    json.dumps({"dosya_id": "wiki/bayat.md", "cekim_tarihi": "2026-09-10T10:00:00+03:00"}),
    json.dumps({"dosya_id": "wiki/bayat.md", "cekim_tarihi": "2026-08-01"}),
    json.dumps({"dosya_id": "wiki/cekimsiz.md", "cekim_tarihi": "2026-01-05"}),
    json.dumps({"dosya_id": "wiki/cekimsiz.md", "cekim_tarihi": "2026-01-02"}),
    json.dumps({"dosya_id": "wiki/ayni.md", "cekim_tarihi": "2031-01-01"}),
    json.dumps({"dosya_id": "wiki/cekimli.md", "cekim_tarihi": "20260101"}),
    json.dumps({"dosya_id": "wiki/cekimli2.md", "cekim_tarihi": "2026-W02-3"}),
    json.dumps({"dosya_id": "wiki/ic/derin.md", "cekim_tarihi": "2026-W02"}),
    json.dumps({"dosya_id": "wiki/temiz.md", "cekim_tarihi": "2026W021"}),
    json.dumps({"dosya_id": "wiki/uzun.md", "cekim_tarihi": "2026-W53-1"}),
    json.dumps({"dosya_id": "wiki/tablo.md", "cekim_tarihi": "2026-02-30"}),
    json.dumps({"dosya_id": "wiki/crlf.md", "cekim_tarihi": ""}),
    json.dumps({"dosya_id": "wiki/crlf.md"}),
    json.dumps({"dosya_id": "", "cekim_tarihi": "2026-01-01"}),
    json.dumps({"dosya_id": None, "cekim_tarihi": "2026-01-01"}),
    json.dumps({"dosya_id": 5, "cekim_tarihi": "2026-01-01"}),
    json.dumps({"dosya_id": True, "cekim_tarihi": "2026-01-01"}),
    json.dumps({"dosya_id": "wiki/cr.md", "cekim_tarihi": 0}),
    json.dumps({"dosya_id": "wiki/cr.md", "cekim_tarihi": None}),
    json.dumps({"dosya_id": "wiki/cr.md", "cekim_tarihi": []}),
    json.dumps({"dosya_id": "raporlar/2026-09-03-eski.md", "cekim_tarihi": "2026-09-01"}),
    json.dumps({"dosya_id": "raporlar/2026-08-20-sinir.md", "cekim_tarihi": "2026-09-30"}),
    "{bozuk json", "not json", "[", "{}", "nul", "NaNx",
    '{"dosya_id": "wiki/damgasiz.md", "cekim_tarihi": "2026-09-1"}',
    '{"dosya_id": "wiki/damgasiz.md", "cekim_tarihi": "2026-09-01 extra"}',
    '{"dosya_id": "wiki/bos.md", "cekim_tarihi": "0000-01-01"}',
    '{"dosya_id": "wiki/bos.md", "cekim_tarihi": "٢٠٢٦-٠٩-٠١"}',
]) + "\n"


def sabit_bugun(a):
    return ["--bugun", "2026-10-20"] + a


# (ad, argv-şablonu, ön-eylem(j), tekrar sayısı)
def durumlar():
    R = "{J}"
    out = []

    def d(ad, args, on=None, tekrar=1, env=None):
        out.append((ad, args, on, tekrar, env))
    d("varsayilan-repo", ["--bugun", "2026-10-20"])
    d("varsayilan-bugunsuz-kuru-sessiz", ["--kuru", "--sessiz"])
    d("repo-acik", ["--repo", R, "--bugun", "2026-10-20"])
    d("repo-gorece", ["--repo", R + "/wiki/..", "--bugun", "2026-10-20"])
    d("json", ["--repo", R, "--bugun", "2026-10-20", "--json"])
    d("json-kuru", ["--repo", R, "--bugun", "2026-10-20", "--json", "--kuru"])
    d("kuru", ["--repo", R, "--bugun", "2026-10-20", "--kuru"])
    d("sessiz", ["--repo", R, "--bugun", "2026-10-20", "--sessiz"])
    d("json-sessiz", ["--repo", R, "--bugun", "2026-10-20", "--json", "--sessiz"])
    d("tekrar-ekleme", ["--repo", R, "--bugun", "2026-10-20"], tekrar=2)
    d("kalip-listesi", ["--kalip-listesi"])
    d("kalip-listesi-gecersiz-repo", ["--kalip-listesi", "--repo", "/yok/yok", "--bugun", "bozuk"])
    d("muafiyet-yok", ["--repo", R, "--bugun", "2026-10-20", "--muafiyet-yok", "--kuru"])
    d("muafiyet-yok-json", ["--repo", R, "--bugun", "2026-10-20", "--muafiyet-yok", "--json"])
    for k in ["wiki", "wiki,core", "wiki/", "core", "raporlar", "cc", "cc/rapor", " wiki , cc ", ",", ",,", "wi", "w", "diger", "xyz", "raporlar/alt", "wiki//", "core/sablonlar"]:
        d("kapsam[%s]" % k, ["--repo", R, "--bugun", "2026-10-20", "--kapsam", k, "--kuru"])
    d("kapsam-bos-metin", ["--repo", R, "--bugun", "2026-10-20", "--kapsam", "", "--kuru"])
    for e in ["0", "1", "10", "30", "89", "90", "91", "200", "-1", "-999", "+5", " 7 ", "1_0", "999999999999999999999"]:
        d("esik[%s]" % e, ["--repo", R, "--bugun", "2026-10-20", "--esik-gun", e, "--json", "--kuru"])
    d("esik-gecersiz", ["--repo", R, "--esik-gun", "abc"])
    d("esik-eksik", ["--repo", R, "--esik-gun"])
    d("esik-0-yaz", ["--repo", R, "--bugun", "2026-10-20", "--esik-gun", "0"])
    for b in ["2026-09-20", "20260920", "2026-W38-3", "2026W383", "2026-W38", "2026W38", "2026-W53-1", "2020-W53-7", "2026-02-30", "bozuk", "2026-9-20", "0001-01-10",
              "0001-02-10", "0001-01-01", "9999-12-31", "0000-01-01", "2026-09-20T10:00", "٢٠٢٦-٠٩-٢٠", "2026-09-20 ", "", "2026-00-10", "2026-W00-1", "2026-W01-8", "2026-W01-0", "20260", "2026-09"]:
        d("bugun[%s]" % b, ["--repo", R, "--bugun", b, "--json", "--kuru"])
        d("bugun-kapsamsiz-dosya[%s]" % b, ["--repo", R, "--bugun", b, "--dosya", "wiki/bayat.md", "--kuru"])
    d("bugun-erken-dosya", ["--repo", R, "--bugun", "2026-01-15", "--json"])
    d("bugun-eski", ["--repo", R, "--bugun", "2025-01-15", "--json"])
    d("dosya-tek", ["--repo", R, "--bugun", "2026-10-20", "--dosya", "wiki/damgasiz.md"])
    d("dosya-cok", ["--repo", R, "--bugun", "2026-10-20", "--dosya", "wiki/damgasiz.md", "--dosya", "wiki/temiz.md", "--dosya", "raporlar/2026-09-03-a.md", "--dosya", "yok.md", "--json"])
    d("dosya-tekrar", ["--repo", R, "--bugun", "2026-10-20", "--dosya", "wiki/damgasiz.md", "--dosya", "wiki/damgasiz.md", "--json"])
    d("dosya-mutlak", ["--repo", R, "--bugun", "2026-10-20", "--dosya", R + "/wiki/damgasiz.md", "--dosya", R + "/raporlar/2026-09-03-a.md", "--json"])
    d("dosya-mutlak-disarida", ["--repo", R, "--bugun", "2026-10-20", "--dosya", "{S}/baska.md", "--json", "--kuru"], on="baska")
    d("dosya-mutlak-yok", ["--repo", R, "--bugun", "2026-10-20", "--dosya", R + "/yok.md", "--json", "--kuru"])
    d("dosya-gorece-nokta", ["--repo", R, "--bugun", "2026-10-20", "--dosya", "./wiki/damgasiz.md", "--dosya", "wiki/../wiki/temiz.md", "--json", "--kuru"])
    d("dosya-dizin", ["--repo", R, "--bugun", "2026-10-20", "--dosya", "wiki", "--json", "--kuru"])
    d("dosya-kapsam-yoksay", ["--repo", R, "--bugun", "2026-10-20", "--dosya", "wiki/damgasiz.md", "--kapsam", "core", "--json", "--kuru"])
    d("dosya-izlenmeyen", ["--repo", R, "--bugun", "2026-10-20", "--dosya", "wiki/izlenmeyen.md", "--dosya", "README.md", "--json", "--kuru"])
    d("dosya-bos-metin", ["--repo", R, "--bugun", "2026-10-20", "--dosya", "", "--json", "--kuru"])
    d("dosya-ters-bolu", ["--repo", R, "--bugun", "2026-10-20", "--dosya", "wiki\\damgasiz.md", "--dosya", "raporlar\\2026-09-03-a.md", "--json", "--kuru"])
    d("dosya-turkce-ad", ["--repo", R, "--bugun", "2026-10-20", "--dosya", "wiki/Türkçe-ad.md", "--json", "--kuru"])
    d("dosya-gecersiz-utf8", ["--repo", R, "--bugun", "2026-10-20", "--dosya", "wiki/gecersiz-utf8.md", "--dosya", "wiki/bom.md", "--dosya", "wiki/crlf.md", "--dosya", "wiki/cr.md", "--json", "--kuru"])
    d("dosya-damga-sinir", ["--repo", R, "--bugun", "2026-10-20", "--dosya", "wiki/damga-13.md", "--dosya", "wiki/damga-12.md", "--dosya", "wiki/bos.md", "--dosya", "wiki/sadece-bosluk.md", "--json", "--kuru"])
    d("dosya-gecersiz-tarih", ["--repo", R, "--bugun", "2026-10-20", "--dosya", "wiki/gecersiz-tarih.md", "--dosya", "wiki/gelecek.md", "--dosya", "wiki/sadece-gelecek.md", "--json", "--kuru"])
    d("dosya-kod-tablo-uzun", ["--repo", R, "--bugun", "2026-10-20", "--dosya", "wiki/kod-blogu.md", "--dosya", "wiki/tablo.md", "--dosya", "wiki/uzun.md", "--json", "--kuru"])
    d("dosya-muaf-arasi", ["--repo", R, "--bugun", "2026-10-20", "--dosya", "raporlar/2026-09-03-eski.md", "--dosya", "cc/notlar-2026-09-05.md", "--dosya", "core/2026-09-03-x.md", "--dosya", "wiki/2026-09-03-y.md", "--json", "--kuru"])
    # cekim-olay
    d("cekim-iyi", ["--repo", R, "--bugun", "2026-10-20", "--json"], on="cekim-iyi")
    d("cekim-iyi-metin", ["--repo", R, "--bugun", "2026-10-20"], on="cekim-iyi")
    d("cekim-crlf", ["--repo", R, "--bugun", "2026-10-20", "--json", "--kuru"], on="cekim-crlf")
    d("cekim-bos", ["--repo", R, "--bugun", "2026-10-20", "--json", "--kuru"], on="cekim-bos")
    d("cekim-gecersiz-utf8", ["--repo", R, "--bugun", "2026-10-20", "--json", "--kuru"], on="cekim-utf8")
    d("cekim-dizin", ["--repo", R, "--bugun", "2026-10-20", "--json", "--kuru"], on="cekim-dizin")
    d("cekim-liste-satir", ["--repo", R, "--bugun", "2026-10-20", "--json", "--kuru"], on="cekim-liste")
    d("cekim-null-satir", ["--repo", R, "--bugun", "2026-10-20", "--json", "--kuru"], on="cekim-null")
    d("cekim-dize-satir", ["--repo", R, "--bugun", "2026-10-20", "--json", "--kuru"], on="cekim-dize")
    d("cekim-sayi-tarih", ["--repo", R, "--bugun", "2026-10-20", "--json", "--kuru"], on="cekim-sayitarih")
    d("cekim-dosyaid-liste", ["--repo", R, "--bugun", "2026-10-20", "--json", "--kuru"], on="cekim-idliste")
    d("cekim-dosyaid-sayi", ["--repo", R, "--bugun", "2026-10-20", "--json", "--kuru"], on="cekim-idsayi")
    d("cekim-bom", ["--repo", R, "--bugun", "2026-10-20", "--json", "--kuru"], on="cekim-bom")
    # repo sorunları
    d("repo-yok", ["--repo", "{S}/yok-dizin", "--bugun", "2026-10-20"])
    d("repo-yok-dosya", ["--repo", "{S}/yok-dizin", "--bugun", "2026-10-20", "--dosya", "a.md"])
    d("repo-git-degil", ["--repo", "{S}/duz", "--bugun", "2026-10-20"], on="duz")
    d("repo-git-degil-dosya", ["--repo", "{S}/duz", "--bugun", "2026-10-20", "--dosya", "a.md", "--json"], on="duz")
    d("repo-git-degil-dosya-kuru", ["--repo", "{S}/duz", "--bugun", "2026-10-20", "--dosya", "a.md", "--json", "--kuru"], on="duz")
    d("repo-git-degil-dosya-veri", ["--repo", "{S}/duz", "--bugun", "2026-10-20", "--dosya", "a.md", "--json"], on="duz-veri")
    d("repo-veri-yok-kuru", ["--repo", "{S}/duz", "--bugun", "2026-10-20", "--dosya", "a.md", "--kuru"], on="duz")
    d("repo-dosya-degil", ["--repo", "{S}/duz/a.md", "--bugun", "2026-10-20", "--dosya", "a.md"], on="duz")
    d("repo-commitsiz", ["--repo", "{S}/bos-git", "--bugun", "2026-10-20", "--dosya", "a.md", "--json"], on="bos-git")
    d("repo-commitsiz-varsayilan", ["--repo", "{S}/bos-git", "--bugun", "2026-10-20"], on="bos-git")
    d("veri-gorunum-var", ["--repo", R, "--bugun", "2026-10-20"], on="gorunum-dosya")
    d("csv-var-uzerine-yaz", ["--repo", R, "--bugun", "2026-10-20"], on="csv-var")
    d("jsonl-var-ekle", ["--repo", R, "--bugun", "2026-10-20"], on="jsonl-var")
    d("jsonl-var-crlf-sonu", ["--repo", R, "--bugun", "2026-10-20"], on="jsonl-eksik-nl")
    # argparse
    d("yardim", ["-h"])
    d("yardim-uzun", ["--help"])
    d("yardim-dar", ["--help"], env={"COLUMNS": "60"})
    d("bilinmeyen", ["--yok"])
    d("kisaltma", ["--rep", R, "--bug", "2026-10-20", "--ku", "--es", "5"])
    d("kisaltma-belirsiz", ["--k"])
    d("esittir", ["--repo=" + R, "--bugun=2026-10-20", "--esik-gun=3", "--kuru", "--json"])
    d("konumsal", ["wiki/a.md"])
    d("deger-eksik", ["--repo"])
    d("negatif-esik-kisa", ["--esik-gun", "-5", "--repo", R, "--bugun", "2026-10-20", "--kuru"])
    d("bugun-dosya-yok-bos-liste", ["--repo", R, "--bugun", "2026-10-20", "--kapsam", "yokyok", "--json"])
    return out


def on_eylem(j, ad, S):
    if ad is None:
        return
    p = os.path.join(j, "veri", "bronz", "cekim-olay.jsonl")
    if ad == "cekim-iyi":
        cekim_yaz(j, CEKIM_IYI)
    elif ad == "cekim-crlf":
        cekim_yaz(j, CEKIM_IYI.replace("\n", "\r\n"))
    elif ad == "cekim-bos":
        cekim_yaz(j, "")
    elif ad == "cekim-utf8":
        cekim_yaz(j, b'{"dosya_id": "wiki/bayat.md", "cekim_tarihi": "2026-09-10"}\n\xff\xfe\n')
    elif ad == "cekim-dizin":
        os.makedirs(p, exist_ok=True)
    elif ad == "cekim-liste":
        cekim_yaz(j, '[1, 2]\n')
    elif ad == "cekim-null":
        cekim_yaz(j, 'null\n')
    elif ad == "cekim-dize":
        cekim_yaz(j, '"abc"\n')
    elif ad == "cekim-sayitarih":
        cekim_yaz(j, '{"dosya_id": "wiki/bayat.md", "cekim_tarihi": 20260910}\n')
    elif ad == "cekim-idliste":
        cekim_yaz(j, '{"dosya_id": ["x"], "cekim_tarihi": "2026-09-10"}\n')
    elif ad == "cekim-idsayi":
        cekim_yaz(j, '{"dosya_id": 7, "cekim_tarihi": "2026-09-10"}\n{"dosya_id": "wiki/bayat.md", "cekim_tarihi": "2026-09-12"}\n')
    elif ad == "cekim-bom":
        cekim_yaz(j, b'\xef\xbb\xbf{"dosya_id": "wiki/bayat.md", "cekim_tarihi": "2026-09-10"}\n')
    elif ad == "baska":
        with open(os.path.join(S, "baska.md"), "w", encoding="utf-8", newline="\n") as f:
            f.write("şu an v1.1\n")
    elif ad in ("duz", "duz-veri"):
        os.makedirs(os.path.join(S, "duz"), exist_ok=True)
        with open(os.path.join(S, "duz", "a.md"), "w", encoding="utf-8", newline="\n") as f:
            f.write("şu an 2020-01-01 v1.1\n\nartık\n")
        if ad == "duz-veri":
            os.makedirs(os.path.join(S, "duz", "veri"), exist_ok=True)
    elif ad == "bos-git":
        d = os.path.join(S, "bos-git")
        os.makedirs(os.path.join(d, "veri"))
        git(d, "init", "-q")
        with open(os.path.join(d, "a.md"), "w", encoding="utf-8", newline="\n") as f:
            f.write("şu an\n")
    elif ad == "gorunum-dosya":
        os.makedirs(os.path.join(j, "veri"), exist_ok=True)
        shutil.rmtree(os.path.join(j, "veri", "gorunum"), ignore_errors=True)
        with open(os.path.join(j, "veri", "gorunum"), "w") as f:
            f.write("dosya")
    elif ad == "csv-var":
        os.makedirs(os.path.join(j, "veri", "gorunum"), exist_ok=True)
        with open(os.path.join(j, "veri", "gorunum", "v_bayat_aday.csv"), "w", newline="\n") as f:
            f.write("eski içerik\n")
    elif ad == "jsonl-var":
        with open(os.path.join(j, "veri", "anakronizm-denetim.jsonl"), "w", encoding="utf-8", newline="\n") as f:
            f.write('{"eski": 1}\n')
    elif ad == "jsonl-eksik-nl":
        with open(os.path.join(j, "veri", "anakronizm-denetim.jsonl"), "w", encoding="utf-8", newline="\n") as f:
            f.write('{"eski": 1}')


# ---------------------------------------------------------------- koşturma
TS = re.compile(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\+03:00")


def maskele(s, S):
    s = s.replace("\r\n", "\n")
    for a in {S, S.replace("\\", "/"), S.replace("/", "\\"), S.replace("\\", "\\\\")}:
        s = s.replace(a, "<KUM>")
    return TS.sub("<TS>", s)


def agac(S):
    out = {}
    for kok, dizinler, dosyalar in os.walk(S):
        dizinler[:] = [d for d in dizinler if d != ".git"]
        for f in dosyalar:
            p = os.path.join(kok, f)
            rel = os.path.relpath(p, S).replace("\\", "/")
            if rel.startswith("jarvis/tools/") or rel.endswith("/anakronizm-denetim.py"):
                continue
            with open(p, "rb") as fh:
                out[rel] = maskele(fh.read().decode("utf-8", "replace"), S)
        for d in dizinler:
            if not os.listdir(os.path.join(kok, d)):
                out[os.path.relpath(os.path.join(kok, d), S).replace("\\", "/") + "/"] = ""
    return out


def kos(motor, S, args, env_ek, tekrar):
    j = os.path.join(S, "jarvis")
    argv = [a.replace("{J}", j.replace("\\", "/")).replace("{S}", S.replace("\\", "/")) for a in args]
    env = dict(os.environ)
    env.pop("COLUMNS", None)
    env.update(env_ek or {})
    env["PYTHONUTF8"] = "1"
    env["CLAUDE_PROJECT_DIR"] = j
    if motor == "py":
        cmd = [sys.executable, os.path.join(j, "tools", "anakronizm-denetim.py")] + argv
    else:
        cmd = [RUST_EXE] + argv
    sonuc = []
    for _ in range(tekrar):
        r = subprocess.run(cmd, cwd=S, stdin=subprocess.DEVNULL, capture_output=True, env=env)
        sonuc.append((r.returncode, maskele(r.stdout.decode("utf-8", "replace"), S), maskele(r.stderr.decode("utf-8", "replace"), S)))
    return sonuc


def main():
    kok = tempfile.mkdtemp(prefix="fark-anak-")
    sablon = os.path.join(kok, "sablon")
    os.makedirs(sablon)
    kum_kur(sablon)
    toplam, fark = 0, 0
    sapmalar = []
    try:
        for ad, args, on, tekrar, env in durumlar():
            toplam += 1
            sonuc = {}
            for motor in ("py", "rust"):
                S = os.path.join(kok, "c%d-%s" % (toplam, motor))
                shutil.copytree(sablon, S)
                on_eylem(os.path.join(S, "jarvis"), on, S)
                r = kos(motor, S, args, env, tekrar)
                sonuc[motor] = (r, agac(S))
            (rp, tp), (rr, tr) = sonuc["py"], sonuc["rust"]
            sorun = []
            for i, (a, b) in enumerate(zip(rp, rr)):
                if a[0] != b[0]:
                    sorun.append("çıkış %d: py=%s rust=%s" % (i, a[0], b[0]))
                if a[1] != b[1]:
                    sorun.append("stdout %d:\n--py--\n%s\n--rust--\n%s" % (i, a[1][:3000], b[1][:3000]))
                if a[2] != b[2]:
                    if a[0] == 1 and "Traceback" in a[2]:
                        sapmalar.append("%s: Python traceback (çıkış 1), stderr metni farklı (beklenen)" % ad)
                    else:
                        sorun.append("stderr %d:\n--py--\n%s\n--rust--\n%s" % (i, a[2][:3000], b[2][:3000]))
            if tp != tr:
                for k in sorted(set(tp) | set(tr)):
                    if tp.get(k) != tr.get(k):
                        sorun.append("dosya %s:\n--py--\n%s\n--rust--\n%s" % (k, (tp.get(k) or "<yok>")[:3000], (tr.get(k) or "<yok>")[:3000]))
            if sorun:
                fark += 1
                print("FARK [%s] %s" % (ad, args))
                for s in sorun:
                    print("   ", s.replace("\n", "\n    "))
            for S in [os.path.join(kok, "c%d-py" % toplam), os.path.join(kok, "c%d-rust" % toplam)]:
                shutil.rmtree(S, ignore_errors=True)
        print("anakronizm-denetim: %d durum, %d fark" % (toplam, fark))
        if sapmalar:
            print("meşru sapmalar (Python traceback, yalnız stderr metni):")
            for s in sapmalar:
                print("  -", s)
    finally:
        def _yaz(f, p, e):
            try:
                os.chmod(p, 0o700)
                f(p)
            except Exception:
                pass
        shutil.rmtree(kok, onerror=_yaz)
    return 1 if fark else 0


if __name__ == "__main__":
    sys.exit(main())
