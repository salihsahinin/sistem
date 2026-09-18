#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
baglam-tablo.py — JARVIS bağlamını (git-izlenen .md/.json/.jsonl) veri tablosuna çevirir.
Şema v0 (deneysel m.29) · emir: cc/gorev/2026-08/gorev-2026-08-15-7.md · sözleşme: veri/README.md
STDLIB ONLY (Python 3.9). Çıktılar: veri/baglam.sqlite · veri/baglam.jsonl · veri/gorunum/*.csv

Koşum:  python3 tools/baglam-tablo.py            (repo kökü = tools/'un üstü)
        python3 tools/baglam-tablo.py --repo <yol> --cikti <veri-dizini>
Determinizm: aynı repo durumu → aynı kayit_id kümesi; tek zaman alanı `uretim.uretim_zamani`.
"""
import argparse
import csv
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone

SEMA_SURUMU = "v1"  # v1 (2026-08-16, W-1/SH-11): +3 galaxy görünümü (v_boyut_anahtar · v_olgu_referans · v_x_olcum); tablolar DEĞİŞMEDİ (additive)
CSV_SATIR_TAVANI = 5000
HEDEF_UZANTILAR = (".md", ".json", ".jsonl")
JSON_HARIC = {".claude/settings.json", ".mcp.json"}  # sır/ayar riski: yalnız `dosya`da adları

# ---------------------------------------------------------------------------
# Yardımcılar
# ---------------------------------------------------------------------------

def fail_loud(msg, kod=2):
    sys.stderr.write("HATA (FAIL-LOUD): %s\n" % msg)
    sys.exit(kod)


def git(repo, *args, check=True):
    p = subprocess.run(["git", "-c", "core.quotepath=off"] + list(args), cwd=repo,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and p.returncode != 0:
        raise RuntimeError("git %s başarısız: %s" % (" ".join(args), p.stderr.decode("utf-8", "replace")))
    return p


def sha1_hex(data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha1(data).hexdigest()


def git_blob_sha(data):
    """`git hash-object` ile birebir aynı değer (blob başlığı + içerik, sha1)."""
    h = hashlib.sha1()
    h.update(b"blob %d\0" % len(data))
    h.update(data)
    return h.hexdigest()


def token_kestirim(metin):
    n = len(metin.encode("utf-8"))
    return (n + 3) // 4


# Türkçe-ASCII katlama — uzunluk KORUNUR (offset'ler geçerli kalsın diye 1:1 harita)
_FOLD = {
    "ç": "c", "Ç": "c", "ğ": "g", "Ğ": "g", "ı": "i", "I": "i", "İ": "i", "i": "i",
    "ö": "o", "Ö": "o", "ş": "s", "Ş": "s", "ü": "u", "Ü": "u", "â": "a", "Â": "a",
    "î": "i", "Î": "i", "û": "u", "Û": "u",
}


def fold(metin):
    out = []
    for ch in metin:
        f = _FOLD.get(ch)
        if f is None:
            lo = ch.lower()
            f = lo if len(lo) == 1 else ch
        out.append(f)
    return "".join(out)


# ---------------------------------------------------------------------------
# Katman / tür kuralları (yol + ada göre; belirsizse diger)
# ---------------------------------------------------------------------------

MODEL_KLASOR_ONEK = "arsiv/chat-model-degisikligi"  # eski: "model değişikliği ile orijinalliği bozulmuş olan chat/" (parti 1 taşıması 2026-09-09)


def katman_bul(yol):
    ad = os.path.basename(yol)
    if yol.endswith((".json", ".jsonl", ".yaml", ".yml")):
        return "yapisal"
    if yol == "CLAUDE.md" or yol.startswith("core/"):
        return "sicak"
    if yol.startswith(".claude/skills/") and ad == "SKILL.md":
        return "sicak"
    if (yol.startswith("raporlar/") or yol.startswith("cc/rapor/") or yol.startswith("cc/gorev/")
            or yol.startswith("ogrenme/") or yol.startswith(MODEL_KLASOR_ONEK)
            or "/arsiv/" in ("/" + yol) or ad.startswith("arsiv-") or "-arsiv" in ad):
        return "soguk"
    if (yol.startswith("kuyruk/") or yol.startswith("wiki/") or yol == "fikir-kutusu.md"
            or yol.startswith("cc/pipeline/") or yol == "cc/defter.md"
            or ("/" not in yol and yol.endswith(".md"))
            or yol.startswith(".claude/") or yol == "cc/README.md"):
        return "ilik"
    return "soguk"


def tur_bul(yol):
    ad = os.path.basename(yol)
    adl = ad.lower()
    if yol in JSON_HARIC:
        return "diger"
    if yol == "CLAUDE.md":
        return "kanon"
    if yol == "core/durum-kapsulu.md" or "kapsulu" in adl or "kapsul" in adl:
        return "kapsul"
    if yol == "core/pano.md":
        return "pano"
    if yol.startswith("core/tuzuk"):
        return "tuzuk"
    if yol.startswith("core/"):
        return "kanon"
    if yol.startswith(".claude/skills/"):
        if "/evals/" in yol and yol.endswith(".json"):
            return "eval"
        return "skill"
    if yol == "wiki/sozluk.md":
        return "sozluk"
    if yol.startswith("wiki/"):
        return "wiki"
    if yol.startswith("kuyruk/"):
        if adl.startswith("gelen-"):
            return "gelen"
        if "fikir-kutusu" in adl:
            return "kutu"
        if "defter" in adl and "sema" not in adl:
            return "defter"
        return "kuyruk"
    if yol == "cc/defter.md":
        return "defter"
    if yol.startswith("cc/gorev/"):
        return "emir"
    if yol.startswith("cc/rapor/"):
        return "rapor"
    if yol.startswith("cc/pipeline/"):
        return "pipeline"
    if yol.startswith("raporlar/"):
        if adl.startswith("vardiya-teslim-"):
            return "teslim"
        if yol.endswith(".jsonl"):
            return "log"
        return "rapor"
    if yol.startswith("ogrenme/dersler/"):
        return "ders"
    if yol.startswith(MODEL_KLASOR_ONEK):
        return "log"
    if yol == "fikir-kutusu.md" or "fikir-kutusu" in adl:
        return "kutu"
    if "rapor" in adl:
        return "rapor"
    if yol.endswith(".jsonl"):
        return "log"
    return "diger"


# ---------------------------------------------------------------------------
# Git meta: tek geçişte ilk/son commit (yeniden-adlandırma zinciri dahil)
# ---------------------------------------------------------------------------

def git_meta(repo, yollar):
    """--name-status -M -c tek geçiş (-c: merge'de çözülen dosyalar da görünür): yol → (ilk_iso, son_iso).
    Rename zinciri geriye izlenir."""
    p = git(repo, "log", "--format=%x01%H %ct %cI", "--name-status", "-M", "-c", "--no-color")
    ilk_ct = {}   # yol -> (ct, iso)
    son_ct = {}
    rename_eski = defaultdict(list)  # yeni -> [(ct, eski)]
    cur = None
    for satir in p.stdout.decode("utf-8", "replace").split("\n"):
        if satir.startswith("\x01"):
            parca = satir[1:].split(" ", 2)
            if len(parca) == 3:
                cur = (int(parca[1]), parca[2])
            continue
        if not satir.strip() or cur is None:
            continue
        alan = satir.split("\t")
        durum = alan[0]
        if durum.startswith("R") and len(alan) >= 3:
            eski, yeni = alan[1], alan[2]
            rename_eski[yeni].append((cur[0], eski))
            hedefler = [yeni]
        elif len(alan) >= 2:
            hedefler = [alan[-1]]
        else:
            continue
        for y in hedefler:
            if y not in ilk_ct or cur[0] < ilk_ct[y][0]:
                ilk_ct[y] = cur
            if y not in son_ct or cur[0] > son_ct[y][0]:
                son_ct[y] = cur

    def ilk_zincir(y, gorulen):
        best = ilk_ct.get(y)
        for ct, eski in rename_eski.get(y, []):
            if eski in gorulen:
                continue
            gorulen.add(eski)
            b2 = ilk_zincir(eski, gorulen)
            if b2 is not None and (best is None or b2[0] < best[0]):
                best = b2
        return best

    sonuc = {}
    for y in yollar:
        ilk = ilk_zincir(y, {y})
        son = son_ct.get(y)
        sonuc[y] = (ilk[1] if ilk else "-", son[1] if son else "-")
    return sonuc


# ---------------------------------------------------------------------------
# Markdown blok ayrıştırıcı
# ---------------------------------------------------------------------------

RE_BASLIK = re.compile(r"^(#{1,6})[ \t]+(.*?)\s*#*\s*$")
RE_FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
RE_MADDE = re.compile(r"^(\s*)([-*+]|\d{1,3}[.)])\s+(.*)$")
RE_TABLO = re.compile(r"^\s*\|")
RE_ALINTI = re.compile(r"^\s{0,3}>")
RE_YATAY = re.compile(r"^\s{0,3}([-*_])(\s*\1){2,}\s*$")


def _blok(tur, bas, son, satirlar, derinlik=0):
    return {"blok_turu": tur, "satir_bas": bas, "satir_son": son,
            "metin": "\n".join(satirlar), "madde_derinlik": derinlik}


def md_bloklar(metin):
    """Ham metin → sıralı blok listesi (satır no 1-tabanlı)."""
    satirlar = metin.split("\n")
    n = len(satirlar)
    bloklar = []
    i = 0
    # frontmatter
    if n > 0 and satirlar[0].strip() == "---":
        for j in range(1, min(n, 200)):
            if satirlar[j].strip() in ("---", "..."):
                bloklar.append(_blok("frontmatter", 1, j + 1, satirlar[0:j + 1]))
                i = j + 1
                break
    para = []
    para_bas = 0

    def para_kapat():
        nonlocal para, para_bas
        if para:
            bloklar.append(_blok("paragraf", para_bas, para_bas + len(para) - 1, para))
            para = []
            para_bas = 0

    while i < n:
        s = satirlar[i]
        no = i + 1
        if not s.strip():
            para_kapat()
            i += 1
            continue
        m = RE_FENCE.match(s)
        if m:
            para_kapat()
            fence = m.group(1)
            j = i + 1
            kapandi = False
            while j < n:
                m2 = RE_FENCE.match(satirlar[j])
                if m2 and m2.group(1)[0] == fence[0] and len(m2.group(1)) >= len(fence) and not m2.group(2).strip():
                    kapandi = True
                    break
                j += 1
            son = j if kapandi else n - 1
            bloklar.append(_blok("kod", no, son + 1, satirlar[i:son + 1]))
            i = son + 1
            continue
        m = RE_BASLIK.match(s)
        if m:
            para_kapat()
            b = _blok("baslik", no, no, [s])
            b["seviye"] = len(m.group(1))
            b["baslik_metni"] = m.group(2).strip()
            bloklar.append(b)
            i += 1
            continue
        if RE_YATAY.match(s):
            para_kapat()
            bloklar.append(_blok("yatay_cizgi", no, no, [s]))
            i += 1
            continue
        if RE_TABLO.match(s):
            para_kapat()
            j = i
            ilk = True
            while j < n and RE_TABLO.match(satirlar[j]):
                if ilk:
                    # başlık satırı + (varsa) ayraç satırı tek blok
                    son = j
                    if j + 1 < n and re.match(r"^\s*\|?\s*:?-{2,}", satirlar[j + 1]) and RE_TABLO.match(satirlar[j + 1]):
                        son = j + 1
                    bloklar.append(_blok("tablo_baslik", j + 1, son + 1, satirlar[j:son + 1]))
                    j = son + 1
                    ilk = False
                    continue
                bloklar.append(_blok("tablo_satiri", j + 1, j + 1, [satirlar[j]]))
                j += 1
            i = j
            continue
        if RE_ALINTI.match(s):
            para_kapat()
            j = i
            while j < n and RE_ALINTI.match(satirlar[j]):
                j += 1
            bloklar.append(_blok("alinti", no, j, satirlar[i:j]))
            i = j
            continue
        m = RE_MADDE.match(s)
        if m:
            para_kapat()
            girinti = len(m.group(1).expandtabs(4))
            j = i + 1
            # devam satırları: boş olmayan, yeni madde/başlık/fence/tablo/alıntı olmayan, girintili satırlar
            while j < n:
                t = satirlar[j]
                if not t.strip():
                    break
                if RE_MADDE.match(t) or RE_BASLIK.match(t) or RE_FENCE.match(t) or RE_TABLO.match(t) \
                        or RE_ALINTI.match(t) or RE_YATAY.match(t):
                    break
                if len(t) - len(t.lstrip()) <= girinti:
                    break
                j += 1
            bloklar.append(_blok("madde", no, j, satirlar[i:j], girinti // 2))
            i = j
            continue
        if not para:
            para_bas = no
        para.append(s)
        i += 1
    para_kapat()
    return bloklar


# ---------------------------------------------------------------------------
# Zarf (ingest v2) ayrıştırma
# ---------------------------------------------------------------------------

ZARF_ZORUNLU = ("tip", "kaynak", "tarih", "hedef", "sema")


def _zarf_anahtar_normalize(k):
    k = fold(k.strip()).replace("_", "-").replace(" ", "-")
    return k


def zarf_ayristir(metin):
    """İlk `[tip: … | kaynak: … | …]` zarfını bul; köşeli-parantez derinliği sayarak kapat."""
    idx = metin.find("[tip:")
    if idx < 0:
        return None
    derinlik = 0
    son = -1
    for j in range(idx, len(metin)):
        c = metin[j]
        if c == "[":
            derinlik += 1
        elif c == "]":
            derinlik -= 1
            if derinlik == 0:
                son = j
                break
    if son < 0:
        return None
    ic = metin[idx + 1:son]
    alanlar = {}
    for parca in ic.split("|"):
        if ":" not in parca:
            continue
        k, v = parca.split(":", 1)
        k = _zarf_anahtar_normalize(k)
        if not k or " " in k:
            continue
        alanlar[k] = v.strip()
    zorunlu_var = all(k in alanlar for k in ZARF_ZORUNLU)
    return {"alanlar": alanlar, "tam": zorunlu_var, "ham": metin[idx:son + 1], "konum": idx}


# ---------------------------------------------------------------------------
# Referans çıkarımı
# ---------------------------------------------------------------------------

ANAHTAR_TERIMLER = [
    # (kanonik değer, katlanmış-metin üzerinde regex gövdesi)
    ("gunaydin", r"gunaydin"),
    ("seans basi", r"seans basi"),
    ("seans bitimi", r"seans bitimi"),
    ("uyucam", r"uyucam"),
    ("vardiya", r"vardiya"),
    ("kapsul", r"kapsul"),
    ("pano", r"pano"),
    ("tuzuk", r"tuzuk"),
    ("damitma", r"damitma"),
    ("ingest", r"ingest"),
    ("zarf", r"zarf"),
    ("atlas", r"atlas"),
    ("antitez", r"antitez"),
    ("hakem", r"hakem"),
    ("workflow", r"workflow"),
    ("pipeline", r"pipeline"),
    ("skill", r"skill"),
    ("halusinasyon", r"halusinasyon"),
    ("sema", r"sema"),
    ("staj", r"staj"),
    ("cowork", r"cowork"),
    ("terminal", r"terminal"),
    ("ana-sira", r"ana[- ]sira"),
    ("yan-oturum", r"yan[- ]oturum"),
    ("katman-1", r"katman[- ]1"),
    ("katman-2", r"katman[- ]2"),
    ("celiski", r"celiski"),
]
# Türkçe ek kuyruğu (katlanmış ASCII): kapsülden, vardiyayı, şemasının, skill'i… — "semantik", "panorama" GEÇMEZ
_EK = (r"(?:'?(?:s|(?:y|n|s)?(?:[aeiou]|[dt][ae]n?|l[ae]r|[iu]n|dir|dur|tir|tur|ki|ken|le|la|yle|yla|ce|ca"
       r"|l[iu]k?|s[iu]z|c[iu]|lik|luk|lig|lug|siz|suz|cik|cuk|mis|mus))*)?")
RE_ANAHTAR = [
    (deger, re.compile(r"(?<![a-z0-9])(?:" + govde + r")" + _EK + r"(?![a-z0-9])"))
    for deger, govde in ANAHTAR_TERIMLER
]

RE_TUZUK = re.compile(r"(?<![\w.])(md|m)\.(\d{1,3})([a-z]?)(?!\w)")
RE_VNO = re.compile(r"(?<![\w-])V(\d{1,3})(?![\w-])")
RE_KART = re.compile(r"(?<![\w-])K-(\d{3})(?![\w-])")
RE_WIKI = re.compile(r"\[\[([^\]\|#\n]+?)(?:[#|][^\]\n]*)?\]\]")
RE_URL = re.compile(r"https?://[^\s<>()\[\]\"'`]+")
RE_ETIKET = re.compile(r"\[(D|K|X|ARANAMADI|\?)\]")
RE_TARIH_TAM = re.compile(r"(?<![\d-])(20\d{2})-(\d{2})-(\d{2})(?![\d-])")
RE_TARIH_KISA = re.compile(r"(?<![\d-])(\d{2})-(\d{2})(?![\d-])")
RE_SHA = re.compile(r"(?<![0-9a-zA-Z_])(?=[0-9]*[a-f])([0-9a-f]{7,40})(?![0-9a-zA-Z_])")
RE_SHA_KOMSU = re.compile(r"commit|sha|git|head|revert|`|hash|blob|push|merge", re.I)
_YOL_KAR = r"[\w\-\.çğıöşüÇĞİÖŞÜâîû]"
RE_YOL = re.compile(r"(?<![\w/\\.@\-])(/?(?:" + _YOL_KAR + r"+/)*" + _YOL_KAR +
                    r"+\.(?:md|py|d2|svg|json|jsonl|sh|ps1))(?![\w/])")


def _tarih_gecerli(a, g):
    return 1 <= a <= 12 and 1 <= g <= 31


def tarih_ipucu_bul(metin):
    """(tarih_ipucu, tarih_iso): metindeki EN ERKEN konumdaki tarih; iso yalnız tam tarihse."""
    en = None
    for m in RE_TARIH_TAM.finditer(metin):
        if _tarih_gecerli(int(m.group(2)), int(m.group(3))):
            en = (m.start(), m.group(0), m.group(0))
            break
    for m in RE_TARIH_KISA.finditer(metin):
        a, b = int(m.group(1)), int(m.group(2))
        if not (_tarih_gecerli(a, b) or _tarih_gecerli(b, a)):
            continue
        if en is None or m.start() < en[0]:
            en = (m.start(), m.group(0), None)
        break
    if en is None:
        return None, None
    return en[1], en[2]


def _url_maskele(metin):
    """URL'leri aynı uzunlukta boşlukla maskele (yol regex'i URL içine girmesin)."""
    def rep(m):
        return " " * (m.end() - m.start())
    return RE_URL.sub(rep, metin)


def yol_normalize(ham):
    """Repo-içi göreli yola indirge: ~/sistem/jarvis/, /abs/…/jarvis/, C:/JARVIS/, ./, ../ önekleri düşer."""
    y = ham
    low = y.lower()
    for isaret in ("/jarvis/", "c:/jarvis/"):
        k = low.find(isaret)
        if k >= 0:
            y = y[k + len(isaret):]
            break
    else:
        for onek in ("~/sistem/jarvis/", "jarvis/", "./"):
            if y.startswith(onek):
                y = y[len(onek):]
        while y.startswith("../"):
            y = y[3:]
        y = y.lstrip("/")
    return y


def referanslar(metin, skill_re, skill_kume, repo_yollar, repo_adlar, repo_kok, dosya_dizin=""):
    """metin → [(ref_turu, ref_deger, ham, konum, hedef_var, hedef_yol)]; dosya_dizin = kaynak dosyanın dizini (göreli çözüm)"""
    out = []
    # tuzuk_madde
    for m in RE_TUZUK.finditer(metin):
        out.append(("tuzuk_madde", "%s.%s%s" % (m.group(1), int(m.group(2)), m.group(3)), m.group(0), m.start(), None, None))
    for m in RE_VNO.finditer(metin):
        out.append(("v_no", "V%d" % int(m.group(1)), m.group(0), m.start(), None, None))
    for m in RE_KART.finditer(metin):
        out.append(("kart", "K-%s" % m.group(1), m.group(0), m.start(), None, None))
    for m in RE_WIKI.finditer(metin):
        out.append(("wiki_link", m.group(1).strip(), m.group(0), m.start(), None, None))
    for m in RE_URL.finditer(metin):
        u = m.group(0).rstrip(".,;:!?)")
        out.append(("url", u, u, m.start(), None, None))
    for m in RE_ETIKET.finditer(metin):
        out.append(("etiket", m.group(1), m.group(0), m.start(), None, None))
    for m in RE_TARIH_TAM.finditer(metin):
        if _tarih_gecerli(int(m.group(2)), int(m.group(3))):
            out.append(("tarih", m.group(0), m.group(0), m.start(), None, None))
    # sha: 7-12 hex yalnız git-benzeri komşulukta; ≥13 hex doğrudan
    for m in RE_SHA.finditer(metin):
        h = m.group(1)
        if len(h) < 13:
            k1, k2 = max(0, m.start() - 40), min(len(metin), m.end() + 40)
            if not RE_SHA_KOMSU.search(metin[k1:k2]):
                continue
        out.append(("sha", h, h, m.start(), None, None))
    # dosya_pointer (URL maskeli metinde)
    maskeli = _url_maskele(metin)
    for m in RE_YOL.finditer(maskeli):
        ham = m.group(1)
        if ham.startswith(".") and "/" not in ham:
            continue  # ".md" gibi çıplak uzantı
        if ham.startswith("-"):
            continue  # "`gorev-…-11.md` + `-12.md`" kısaltmaları — yol değil
        if "…" in ham or ".." in ham.replace("../", ""):
            continue
        norm = yol_normalize(ham)
        var = 0
        hedef = None
        goreli = os.path.normpath(os.path.join(dosya_dizin, norm)) if dosya_dizin else norm
        if norm in repo_yollar or os.path.exists(os.path.join(repo_kok, norm)):
            var, hedef = 1, norm
        elif goreli in repo_yollar or os.path.exists(os.path.join(repo_kok, goreli)):
            var, hedef = 1, goreli  # kaynak dosyanın dizinine göreli (ör. SKILL.md → references/x.md)
        elif "/" not in norm and norm in repo_adlar:
            var, hedef = 1, repo_adlar[norm]  # çıplak ad → repo'daki ilk eş-adlı dosya
        out.append(("dosya_pointer", norm, ham, m.start(), var, hedef))
    # skill_adi — birebir (ASCII) eşleşme; re.I'nin ı/İ katlaması ("damıtma"≠"damitma") elenir
    for m in skill_re.finditer(metin):
        ad = m.group(1).lower()
        if ad in skill_kume:
            out.append(("skill_adi", ad, m.group(0), m.start(), None, None))
    # anahtar_terim (katlanmış metin, offset korunur)
    f = fold(metin)
    for deger, rx in RE_ANAHTAR:
        for m in rx.finditer(f):
            out.append(("anahtar_terim", deger, metin[m.start():m.end()], m.start(), None, None))
    return out


# ---------------------------------------------------------------------------
# JSON düzleştirme
# ---------------------------------------------------------------------------

def _jp(parca):
    return "/" + str(parca).replace("~", "~0").replace("/", "~1")


def json_duzlestir(obj, yol, out, satir_no):
    if isinstance(obj, dict):
        for k in obj:  # sıra korunur (json.load düzeni)
            json_duzlestir(obj[k], yol + _jp(k), out, satir_no)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            json_duzlestir(v, yol + _jp(i), out, satir_no)
    else:
        if obj is None:
            tip, deger = "null", ""
        elif isinstance(obj, bool):
            tip, deger = "boolean", "true" if obj else "false"
        elif isinstance(obj, (int, float)):
            tip, deger = "number", json.dumps(obj)
        else:
            tip, deger = "string", str(obj)
        out.append((satir_no, yol or "/", deger, tip))


# ---------------------------------------------------------------------------
# SQLite şema
# ---------------------------------------------------------------------------

DDL = """
CREATE TABLE dosya (
  dosya_id TEXT PRIMARY KEY, dizin TEXT, katman TEXT, tur TEXT,
  boyut_bytes INTEGER, satir_sayisi INTEGER, blob_sha TEXT,
  ilk_commit TEXT, son_commit TEXT, baslik TEXT, token_kestirim INTEGER,
  uzanti TEXT, okunabildi INTEGER
);
CREATE TABLE kayit (
  kayit_id TEXT PRIMARY KEY, dosya_id TEXT, sira INTEGER, bolum_yolu TEXT, blok_turu TEXT,
  satir_bas INTEGER, satir_son INTEGER, metin TEXT, metin_kisa TEXT, token_kestirim INTEGER,
  tarih_ipucu TEXT, tarih_iso TEXT,
  zarf_tip TEXT, zarf_kaynak TEXT, zarf_tarih TEXT, zarf_hedef TEXT, zarf_sema TEXT,
  zarf_onem TEXT, zarf_gecerli_bitis TEXT, zarf_json TEXT,
  madde_derinlik INTEGER
);
CREATE TABLE referans (
  kayit_id TEXT, ref_turu TEXT, ref_deger TEXT, ham TEXT, konum INTEGER,
  hedef_var INTEGER, hedef_yol TEXT
);
CREATE TABLE anahtar (
  anahtar_id TEXT PRIMARY KEY, tur TEXT, deger TEXT, kaynak_dosya TEXT,
  durum TEXT, replaced_by TEXT, gecerli_bas TEXT, gecerli_bitis TEXT,
  referans_sayisi INTEGER, sicak_referans_sayisi INTEGER, ilk_gorulme TEXT, son_gorulme TEXT
);
CREATE TABLE json_kayit (
  dosya_id TEXT, satir_no INTEGER, json_yolu TEXT, deger TEXT, deger_tipi TEXT
);
CREATE TABLE uretim (
  uretim_zamani TEXT, git_head_sha TEXT, dosya_sayisi INTEGER, kayit_sayisi INTEGER,
  referans_sayisi INTEGER, sema_surumu TEXT, script_sha TEXT,
  anahtar_sayisi INTEGER, json_kayit_sayisi INTEGER, sure_sn REAL, python_surumu TEXT,
  kayit_id_kume_sha TEXT, notlar TEXT
);
CREATE TABLE parquet_uretim (
  kosum_id TEXT, tablo TEXT, durum TEXT, satir INTEGER, byte INTEGER, ms REAL,
  git_head TEXT, uretim_ts TEXT, duckdb TEXT, neden TEXT
);
CREATE INDEX ix_kayit_dosya ON kayit(dosya_id, sira);
CREATE INDEX ix_kayit_dosya_satir ON kayit(dosya_id, satir_bas, satir_son);  -- KB-53 (a) İB-26: adresli erişim (dosya + satır aralığı) bileşik indeksi, 08-22
CREATE INDEX ix_ref_kayit ON referans(kayit_id);
CREATE INDEX ix_ref_tur_deger ON referans(ref_turu, ref_deger);
CREATE INDEX ix_json_dosya ON json_kayit(dosya_id);
"""

GORUNUMLER = [
    ("v_referans_sayim", """
CREATE VIEW v_referans_sayim AS
SELECT r.ref_turu, r.ref_deger, COUNT(*) AS toplam,
       SUM(CASE WHEN d.katman='sicak' THEN 1 ELSE 0 END) AS sicak,
       SUM(CASE WHEN d.katman='ilik'  THEN 1 ELSE 0 END) AS ilik,
       SUM(CASE WHEN d.katman='soguk' THEN 1 ELSE 0 END) AS soguk,
       COUNT(DISTINCT k.dosya_id) AS dosya_sayisi
FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id JOIN dosya d ON d.dosya_id=k.dosya_id
GROUP BY r.ref_turu, r.ref_deger
ORDER BY toplam DESC, r.ref_turu, r.ref_deger"""),
    ("v_anahtar_terim_dosya", """
CREATE VIEW v_anahtar_terim_dosya AS
SELECT r.ref_deger AS anahtar_terim, k.dosya_id, d.katman, d.tur, COUNT(*) AS sayi
FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id JOIN dosya d ON d.dosya_id=k.dosya_id
WHERE r.ref_turu='anahtar_terim'
GROUP BY r.ref_deger, k.dosya_id
ORDER BY r.ref_deger, sayi DESC, k.dosya_id"""),
    ("v_zarf_kayitlar", """
CREATE VIEW v_zarf_kayitlar AS
SELECT k.kayit_id, k.dosya_id, d.katman, k.bolum_yolu, k.zarf_tip, k.zarf_kaynak, k.zarf_tarih,
       k.zarf_hedef, k.zarf_sema, k.zarf_onem, k.zarf_gecerli_bitis, k.zarf_json, k.metin_kisa
FROM kayit k JOIN dosya d ON d.dosya_id=k.dosya_id
WHERE k.zarf_json IS NOT NULL
ORDER BY k.dosya_id, k.sira"""),
    ("v_dosya_envanter", """
CREATE VIEW v_dosya_envanter AS
SELECT dosya_id, dizin, katman, tur, boyut_bytes, satir_sayisi, token_kestirim,
       ilk_commit, son_commit, blob_sha, baslik
FROM dosya
ORDER BY katman, tur, dosya_id"""),
    ("v_bolum_yogunluk", """
CREATE VIEW v_bolum_yogunluk AS
SELECT dosya_id, bolum_yolu, COUNT(*) AS kayit_sayisi, SUM(token_kestirim) AS token,
       MIN(satir_bas) AS satir_bas, MAX(satir_son) AS satir_son
FROM kayit
GROUP BY dosya_id, bolum_yolu
ORDER BY dosya_id, MIN(sira)"""),
    ("v_kirik_pointer", """
CREATE VIEW v_kirik_pointer AS
SELECT r.ref_deger AS yol,
       CASE WHEN instr(r.ref_deger,'/')>0 THEN 'yol' ELSE 'ciplak_ad' END AS yol_bicimi,
       COUNT(*) AS sayi, COUNT(DISTINCT k.dosya_id) AS dosya_sayisi,
       MIN(k.dosya_id) AS ilk_dosya, MIN(r.kayit_id) AS ilk_kayit
FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id
WHERE r.ref_turu='dosya_pointer' AND r.hedef_var=0
GROUP BY r.ref_deger
ORDER BY sayi DESC, yol"""),
    ("v_celiski_adayi", """
CREATE VIEW v_celiski_adayi AS
SELECT r.ref_deger AS anahtar_terim, k.dosya_id,
       SUM(CASE WHEN k.zarf_gecerli_bitis IS NOT NULL AND k.zarf_gecerli_bitis<>'' AND k.zarf_gecerli_bitis<>'-' THEN 1 ELSE 0 END) AS bitisli,
       SUM(CASE WHEN k.zarf_gecerli_bitis IS NULL OR k.zarf_gecerli_bitis='' OR k.zarf_gecerli_bitis='-' THEN 1 ELSE 0 END) AS bitissiz
FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id
WHERE r.ref_turu='anahtar_terim' AND k.zarf_json IS NOT NULL
GROUP BY r.ref_deger, k.dosya_id
HAVING bitisli>0 AND bitissiz>0
ORDER BY anahtar_terim, k.dosya_id"""),
    # --- v1 galaxy görünümleri (W-1/SH-11, 2026-08-16; kanıt: cc/rapor/2026-08/rapor-2026-08-15-8.md A-YT2/D-YT1/D-YT3, tasarım: core/world-model-tasarimi.md) ---
    ("v_boyut_anahtar", """
CREATE VIEW v_boyut_anahtar AS
SELECT a.anahtar_id, a.tur, a.deger, a.durum, a.replaced_by,
       a.gecerli_bas, a.gecerli_bitis,
       a.referans_sayisi, a.sicak_referans_sayisi, a.ilk_gorulme, a.son_gorulme
FROM anahtar a
ORDER BY a.tur, a.anahtar_id"""),
    ("v_olgu_referans", """
CREATE VIEW v_olgu_referans AS
SELECT r.kayit_id, r.ref_turu, r.ref_deger, r.hedef_var, r.hedef_yol,
       k.dosya_id, d.katman, d.tur AS dosya_turu, k.bolum_yolu,
       COALESCE(k.tarih_iso, k.zarf_tarih) AS olay_tarihi,
       d.son_commit AS dosya_son_commit,
       CASE WHEN COALESCE(k.tarih_iso, k.zarf_tarih) IS NOT NULL THEN 'zamanli' ELSE 'zamansiz' END AS zaman_grain
FROM referans r
JOIN kayit k ON k.kayit_id = r.kayit_id
JOIN dosya d ON d.dosya_id = k.dosya_id"""),
    ("v_x_olcum", """
CREATE VIEW v_x_olcum AS
WITH sirali AS (
  SELECT d.katman, k.blok_turu, k.token_kestirim,
         ROW_NUMBER() OVER (PARTITION BY d.katman, k.blok_turu ORDER BY k.token_kestirim) AS rn,
         COUNT(*)     OVER (PARTITION BY d.katman, k.blok_turu) AS n
  FROM kayit k JOIN dosya d ON d.dosya_id = k.dosya_id
  WHERE k.token_kestirim IS NOT NULL
)
SELECT katman, blok_turu, MAX(n) AS birim_sayisi,
       MIN(token_kestirim) AS token_min,
       MAX(CASE WHEN rn = (n + 1) / 2 THEN token_kestirim END) AS token_medyan,
       MAX(token_kestirim) AS token_maks,
       ROUND(AVG(token_kestirim), 1) AS token_ortalama,
       SUM(token_kestirim) AS token_toplam,
       'bytes/4 kestirimi; Türkçe dil-çarpanı ölçülmemiş (rapor-8 C-kör)' AS olcum_serhi
FROM sirali
GROUP BY katman, blok_turu
ORDER BY katman, token_toplam DESC"""),
]


# ---------------------------------------------------------------------------
# Ana akış
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="JARVIS bağlam → veri tablosu (şema v0)")
    ap.add_argument("--repo", default=None, help="repo kökü (varsayılan: tools/'un üstü)")
    ap.add_argument("--cikti", default=None, help="çıktı dizini (varsayılan: <repo>/veri)")
    ap.add_argument("--sessiz", action="store_true")
    args = ap.parse_args()

    t0 = time.time()
    script_yolu = os.path.abspath(__file__)
    repo = os.path.abspath(args.repo) if args.repo else os.path.dirname(os.path.dirname(script_yolu))
    cikti = os.path.abspath(args.cikti) if args.cikti else os.path.join(repo, "veri")

    # D1: git ls-files başarısız → repo değil → DUR
    try:
        p = git(repo, "ls-files", "-z")
    except Exception as e:  # noqa
        fail_loud("`git ls-files` başarısız (repo değil?): %s" % e)
    tum_yollar = sorted(y for y in p.stdout.decode("utf-8", "surrogateescape").split("\0") if y)
    if not tum_yollar:
        fail_loud("`git ls-files` boş döndü — izlenen dosya yok")
    repo_yollar = set(tum_yollar)
    repo_adlar = {}
    for y in tum_yollar:
        ad = os.path.basename(y)
        repo_adlar.setdefault(ad, y)  # aynı ad → sözlük sırasında ilk yol
    hedef_yollar = [y for y in tum_yollar if y.lower().endswith(HEDEF_UZANTILAR)]

    head = git(repo, "rev-parse", "HEAD", check=False).stdout.decode().strip() or "-"
    meta = git_meta(repo, hedef_yollar)

    skill_adlari = sorted(d for d in os.listdir(os.path.join(repo, ".claude", "skills"))
                          if os.path.isfile(os.path.join(repo, ".claude", "skills", d, "SKILL.md"))) \
        if os.path.isdir(os.path.join(repo, ".claude", "skills")) else []
    skill_re = re.compile(r"(?<![\w-])(" + "|".join(re.escape(s) for s in skill_adlari) + r")(?![\w-])", re.I) \
        if skill_adlari else re.compile(r"(?!x)x")
    skill_kume = set(skill_adlari)

    notlar = {"utf8_hatasi": [], "json_hatasi": [], "kayit_id_cakisma": 0, "csv_kesildi": []}
    dosya_rows, kayit_rows, ref_rows, json_rows = [], [], [], []
    gorulen_id = set()

    for yol in hedef_yollar:
        tam = os.path.join(repo, yol)
        with open(tam, "rb") as fh:
            ham = fh.read()
        boyut = len(ham)
        blob = git_blob_sha(ham)
        ilk_c, son_c = meta.get(yol, ("-", "-"))
        uzanti = os.path.splitext(yol)[1].lower()
        dizin = yol.split("/")[0] if "/" in yol else "."
        okunabildi = 1
        try:
            metin = ham.decode("utf-8")
        except UnicodeDecodeError as e:
            metin = None
            okunabildi = 0
            notlar["utf8_hatasi"].append("%s: %s" % (yol, str(e)[:80]))
        if metin is not None:
            if metin.startswith("﻿"):
                metin = metin[1:]
            metin = metin.replace("\r\n", "\n").replace("\r", "\n")
            satir_sayisi = metin.count("\n") + (0 if metin.endswith("\n") or metin == "" else 1)
        else:
            satir_sayisi = ham.count(b"\n") + (0 if ham.endswith(b"\n") or not ham else 1)
        baslik = os.path.basename(yol)
        tur = tur_bul(yol) if okunabildi else "diger"
        katman = katman_bul(yol)

        if metin is not None and uzanti == ".md":
            m = re.search(r"^# +(.+?)\s*$", metin, re.M)
            if m:
                baslik = m.group(1).strip()
            bloklar = md_bloklar(metin)
            yol_stack = {}  # seviye -> metin
            for sira, b in enumerate(bloklar):
                if b["blok_turu"] == "baslik":
                    sev = b["seviye"]
                    for s in list(yol_stack):
                        if s >= sev:
                            del yol_stack[s]
                    yol_stack[sev] = b["baslik_metni"]
                bolum_yolu = " › ".join(yol_stack[s] for s in sorted(yol_stack) if s <= 3)
                mt = b["metin"]
                kid = "%s#%d-%d#%s" % (yol, b["satir_bas"], b["satir_son"], sha1_hex(mt)[:8])
                if kid in gorulen_id:  # D4
                    n = 2
                    while (kid + "~%d" % n) in gorulen_id:
                        n += 1
                    kid = kid + "~%d" % n
                    notlar["kayit_id_cakisma"] += 1
                gorulen_id.add(kid)
                kisa = re.sub(r"\s+", " ", mt).strip()[:200]
                t_ip, t_iso = tarih_ipucu_bul(mt)
                z = zarf_ayristir(mt)
                zt = zk = ztar = zh = zs = zo = zgb = zj = None
                if z is not None:
                    al = z["alanlar"]
                    if z["tam"]:
                        zt, zk, ztar, zh, zs = (al.get("tip"), al.get("kaynak"), al.get("tarih"),
                                                al.get("hedef"), al.get("sema"))
                        zo = al.get("onem")
                        zgb = al.get("gecerli-bitis")
                        zj = json.dumps(al, ensure_ascii=False, sort_keys=True)
                    else:  # D3
                        d = dict(al)
                        d["kismi"] = True
                        zj = json.dumps(d, ensure_ascii=False, sort_keys=True)
                kayit_rows.append((kid, yol, sira, bolum_yolu, b["blok_turu"], b["satir_bas"], b["satir_son"],
                                   mt, kisa, token_kestirim(mt), t_ip, t_iso,
                                   zt, zk, ztar, zh, zs, zo, zgb, zj, b["madde_derinlik"]))
                for (rt, rd, rh, rk, hv, hy) in referanslar(mt, skill_re, skill_kume, repo_yollar, repo_adlar, repo, os.path.dirname(yol)):
                    ref_rows.append((kid, rt, rd, rh, rk, hv, hy))
        elif metin is not None and uzanti in (".json", ".jsonl") and yol not in JSON_HARIC:
            duz = []
            try:
                if uzanti == ".json":
                    json_duzlestir(json.loads(metin), "", duz, None)
                else:
                    for no, satir in enumerate(metin.split("\n"), 1):
                        if not satir.strip():
                            continue
                        json_duzlestir(json.loads(satir), "", duz, no)
            except (ValueError, RecursionError) as e:
                notlar["json_hatasi"].append("%s: %s" % (yol, str(e)[:80]))
                duz = []
            for (no, jy, dg, tp) in duz:
                json_rows.append((yol, no, jy, dg, tp))
        dosya_rows.append((yol, dizin, katman, tur, boyut, satir_sayisi, blob, ilk_c, son_c, baslik,
                           (boyut + 3) // 4, uzanti.lstrip("."), okunabildi))

    # ---- anahtar tablosu (gözlenen) ----
    katman_of = {r[0]: r[2] for r in dosya_rows}
    son_commit_of = {r[0]: r[8] for r in dosya_rows}
    dosya_of_kayit = {r[0]: r[1] for r in kayit_rows}
    ref_say = defaultdict(int)
    ref_sicak = defaultdict(int)
    ref_dosyalar = defaultdict(set)
    for (kid, rt, rd, _h, _k, _hv, _hy) in ref_rows:
        d = dosya_of_kayit[kid]
        key = (rt, rd)
        ref_say[key] += 1
        if katman_of.get(d) == "sicak":
            ref_sicak[key] += 1
        ref_dosyalar[key].add(d)
    anahtar_rows = []
    eslesme = {"skill": "skill_adi", "kart": "kart", "tuzuk_madde": "tuzuk_madde", "v_no": "v_no",
               "anahtar_terim": "anahtar_terim", "wiki_sayfa": "wiki_link"}

    def _gorulme(key):
        tarihler = sorted(t for t in (son_commit_of.get(d, "-") for d in ref_dosyalar.get(key, ())) if t != "-")
        return (tarihler[0], tarihler[-1]) if tarihler else (None, None)

    def anahtar_ekle(tur, deger, kaynak):
        key = (eslesme[tur], deger)
        ilk, son = _gorulme(key)
        anahtar_rows.append(("%s:%s" % (tur, deger), tur, deger, kaynak, "gozlenen", None, None, None,
                             ref_say.get(key, 0), ref_sicak.get(key, 0), ilk, son))

    for s in skill_adlari:
        anahtar_ekle("skill", s, ".claude/skills/%s/SKILL.md" % s)
    for deger, _rx in ANAHTAR_TERIMLER:
        anahtar_ekle("anahtar_terim", deger, "-")
    wiki_sayfalar = {}
    for y in hedef_yollar:
        if y.startswith("wiki/") and y.endswith(".md"):
            wiki_sayfalar[os.path.splitext(os.path.basename(y))[0]] = y
    gozlenen = defaultdict(set)
    for (rt, rd) in ref_say:
        gozlenen[rt].add(rd)
    for k in sorted(gozlenen["kart"]):
        anahtar_ekle("kart", k, "core/pano.md")
    for k in sorted(gozlenen["tuzuk_madde"], key=lambda s: (s.split(".")[0], int(re.sub(r"\D", "", s.split(".")[1]) or 0), s)):
        anahtar_ekle("tuzuk_madde", k, "core/tuzuk-v0.md")
    for k in sorted(gozlenen["v_no"], key=lambda s: int(s[1:])):
        anahtar_ekle("v_no", k, "-")
    for k in sorted(set(wiki_sayfalar) | gozlenen["wiki_link"]):
        anahtar_ekle("wiki_sayfa", k, wiki_sayfalar.get(k, "-"))

    # ---- SQLite yaz (tmp → replace) ----
    os.makedirs(os.path.join(cikti, "gorunum"), exist_ok=True)
    db_yolu = os.path.join(cikti, "baglam.sqlite")
    tmp_yolu = db_yolu + ".tmp"
    if os.path.exists(tmp_yolu):
        os.remove(tmp_yolu)  # yalnız kendi geçici dosyamız
    con = sqlite3.connect(tmp_yolu)
    con.executescript(DDL)
    for _ad, sql in GORUNUMLER:
        con.execute(sql)
    con.executemany("INSERT INTO dosya VALUES (%s)" % ",".join("?" * 13), dosya_rows)
    con.executemany("INSERT INTO kayit VALUES (%s)" % ",".join("?" * 21), kayit_rows)
    con.executemany("INSERT INTO referans VALUES (?,?,?,?,?,?,?)", ref_rows)
    con.executemany("INSERT INTO anahtar VALUES (%s)" % ",".join("?" * 12), anahtar_rows)
    con.executemany("INSERT INTO json_kayit VALUES (?,?,?,?,?)", json_rows)

    # ---- İB-52 (KB-68 a, Karar 69 EK; anakronizm M4 kayıt şeması) — ADDITIVE iki kolon, türetilmiş ----
    # kaynak_tarihi = bloğun KENDİ taşıdığı tarih (yayın/olay: tarih_iso ∨ zarf_tarih; yoksa NULL = tarih taşımıyor).
    # cekim_tarihi  = ERİŞİM tarihi: dosyanın son commit günü ∨ bronz `veri/bronz/cekim-olay.jsonl`'daki (tools/bayat-cekim.py yazar)
    #                 en yeni yeniden-çekim günü — hangisi büyükse. Yeniden-çekim dosyaya DOKUNMADAN damga tazeler (m.8; churn yok).
    # DDL'e değil ALTER'la eklenir ki eski INSERT genişliği (21) ve JSONL dışa-aktarımı aynen kalsın (additive-only sözleşmesi).
    con.execute("ALTER TABLE kayit ADD COLUMN cekim_tarihi TEXT")
    con.execute("ALTER TABLE kayit ADD COLUMN kaynak_tarihi TEXT")
    _gun = "'[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]*'"
    con.execute("UPDATE kayit SET kaynak_tarihi = CASE WHEN tarih_iso GLOB %s THEN substr(tarih_iso,1,10) "
                "WHEN zarf_tarih GLOB %s THEN substr(zarf_tarih,1,10) END" % (_gun, _gun))
    con.execute("UPDATE kayit SET cekim_tarihi = (SELECT substr(d.son_commit,1,10) FROM dosya d WHERE d.dosya_id=kayit.dosya_id)")
    cekim_son = {}
    cekim_yolu = os.path.join(cikti, "bronz", "cekim-olay.jsonl")
    if os.path.exists(cekim_yolu):
        with open(cekim_yolu, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                try:
                    o = json.loads(line)
                except json.JSONDecodeError:
                    continue
                d, t = o.get("dosya_id"), (o.get("cekim_tarihi") or "")[:10]
                if d and t and t > cekim_son.get(d, ""):
                    cekim_son[d] = t
        for d, t in sorted(cekim_son.items()):
            con.execute("UPDATE kayit SET cekim_tarihi=? WHERE dosya_id=? AND (cekim_tarihi IS NULL OR cekim_tarihi<?)", (t, d, t))
    notlar["cekim_olay_dosya"] = len(cekim_son)

    kume_sha = sha1_hex("\n".join(sorted(r[0] for r in kayit_rows)))
    with open(script_yolu, "rb") as fh:
        script_sha = sha1_hex(fh.read())
    uretim_zamani = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    sure = round(time.time() - t0, 2)
    con.execute("INSERT INTO uretim VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (uretim_zamani, head, len(dosya_rows), len(kayit_rows), len(ref_rows), SEMA_SURUMU, script_sha,
                 len(anahtar_rows), len(json_rows), sure, sys.version.split()[0], kume_sha,
                 json.dumps(notlar, ensure_ascii=False, sort_keys=True)))
    con.commit()

    # ---- CSV görünümler ----
    for ad, _sql in GORUNUMLER:
        cur = con.execute("SELECT * FROM %s" % ad)
        kolonlar = [c[0] for c in cur.description]
        satirlar = cur.fetchall()
        csv_yolu = os.path.join(cikti, "gorunum", ad + ".csv")
        with open(csv_yolu, "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh, lineterminator="\n")
            w.writerow(kolonlar)
            for r in satirlar[:CSV_SATIR_TAVANI]:
                w.writerow(["" if v is None else v for v in r])
            if len(satirlar) > CSV_SATIR_TAVANI:
                w.writerow(["# UYARI: %d satırın ilk %d'i yazıldı; tam küme veri/baglam.sqlite %s" %
                            (len(satirlar), CSV_SATIR_TAVANI, ad)] + [""] * (len(kolonlar) - 1))
                notlar["csv_kesildi"].append("%s:%d" % (ad, len(satirlar)))
    if notlar["csv_kesildi"]:
        con.execute("UPDATE uretim SET notlar=?", (json.dumps(notlar, ensure_ascii=False, sort_keys=True),))
        con.commit()
    con.close()
    os.replace(tmp_yolu, db_yolu)

    # ---- JSONL (kayit tablosu; deterministik sıra) ----
    kolon = ["kayit_id", "dosya_id", "sira", "bolum_yolu", "blok_turu", "satir_bas", "satir_son", "metin",
             "metin_kisa", "token_kestirim", "tarih_ipucu", "tarih_iso", "zarf_tip", "zarf_kaynak", "zarf_tarih",
             "zarf_hedef", "zarf_sema", "zarf_onem", "zarf_gecerli_bitis", "zarf_json", "madde_derinlik"]
    with open(os.path.join(cikti, "baglam.jsonl"), "w", encoding="utf-8", newline="\n") as fh:
        for r in kayit_rows:
            fh.write(json.dumps(dict(zip(kolon, r)), ensure_ascii=False, sort_keys=True) + "\n")

    ozet = {"dosya": len(dosya_rows), "kayit": len(kayit_rows), "referans": len(ref_rows),
            "anahtar": len(anahtar_rows), "json_kayit": len(json_rows), "sure_sn": sure,
            "kayit_id_kume_sha": kume_sha, "git_head": head[:12], "utf8_hatasi": len(notlar["utf8_hatasi"]),
            "json_hatasi": len(notlar["json_hatasi"]), "kayit_id_cakisma": notlar["kayit_id_cakisma"],
            "csv_kesildi": notlar["csv_kesildi"], "cikti": cikti}
    if not args.sessiz:
        print(json.dumps(ozet, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
