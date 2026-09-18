#!/usr/bin/env python3
"""anahtar-cascade.py — emekli anahtar yayılımı (İB-90, Karar 96 M2 A3, 2026-09-15). Kural: core/baglam-anahtar-kaydi.md
§1 ilke 5-9 (emeklilik = damga + halef; yayılım = AÇIK yeniden-yazım, deterministik grep-cascade; "diff üret → onay" modeli,
%100 otomatik değil) + §3 protokol (BACKWARD sıra) + Karar 93 EK deseni (ad-eşitliği: dizin README bloğu).
Denetim `tools/anahtar-denetim.py`'nin fonksiyonlarını yeniden kullanır (tek tanım kuralı); kendisi yalnız ÜRETİR ve
--onay verilmeden hiçbir kanon dosyasına yazmaz.

Alt komutlar:
  kaydet  --anahtar <id> --eski <değer> --yeni <değer> --tarih YYYY-MM-DD --gerekce "…" [--kaynak "…"] [--tur tetik|skill_adi|yuzey|kavram|kart|dosya]
          [--varyant v …] [--izinli regex …] → §2 şemasında yeni anahtar ∨ mevcut anahtara `emekli` satırı olarak JSON basar (stdout).
          Kayıt dosyasına yazmaz: core/ kanonu Edit aracıyla, Katman-1 sınıfıysa Salih imzasıyla (rules/tools.md).
  tara    --anahtar <id> [--katman sicak|ilik|hepsi] → kalıntı satırları + önerilen yeniden-yazım (eski→yeni) diff önizlemesi; dosya yazmaz.
  uygula  --anahtar <id> [--katman sicak|ilik] --onay → önizlemedeki satırları yeniden yazar (izinli kalıp taşıyan satırlar ATLANIR);
          soğuk katman (tarihçe) hiçbir zaman yazılmaz. --onay yoksa yalnız sayım basar.
  readme  --anahtar <id> → Karar 93 EK K2 deseni: emekli değeri barındıran her kök dizinin README eşleniğinde
          "<eski> = <yeni> (eski ad/değer)" bağlama satırı var mı; eksikler listelenir (yazmaz).
Kullanım: python3 tools/anahtar-cascade.py <altkomut> … [--repo ~/sistem/jarvis] [--json]
Çıkış: 0 temiz/üretildi · 1 kalıntı var (tara/readme) ∨ uygula --onay'sız kalıntı · 2 kullanım/kayıt hatası.
"""
import argparse, importlib.util, json, os, pathlib, re, sys

BURASI = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("anahtar_denetim", BURASI / "anahtar-denetim.py")
AD = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(AD)   # norm · katman · git_md · load_registry · compile_patterns


def kayit_yolu(repo):
    return repo / "core" / "baglam-anahtar-kaydi.md"


def anahtar_bul(reg, aid):
    for a in reg.get("anahtarlar", []):
        if a.get("anahtar_id") == aid:
            return a
    return None


def kalintilar(repo, a, katmanlar):
    """Emekli değer + varyantların git-izlenen .md/.py/.sh/.json dosyalarındaki satırları (izinli kalıp ayrık)."""
    out = []
    dosyalar = [p for p in AD.git_md(repo)]
    # anahtar-denetim yalnız .md sayar; skill/hook/script yüzeyleri de sıcaktır (Karar 93 EK K3) → ek uzantılar
    try:
        import subprocess
        hepsi = subprocess.run(["git", "-c", "core.quotepath=off", "ls-files", "-z"], cwd=repo, capture_output=True, check=True).stdout.decode("utf-8", "replace").split("\0")
        dosyalar = sorted({p for p in hepsi if p.endswith((".md", ".py", ".sh", ".json", ".html"))})
    except Exception:
        pass
    kayit_rel = "core/baglam-anahtar-kaydi.md"   # kaydın kendisi tarihçe/damga yeridir, kalıntı sayılmaz (anahtar-denetim ile aynı)
    for e in a.get("emekli", []):
        vals = [e["deger"]] + list(e.get("varyantlar", []))
        pats = list(zip(vals, AD.compile_patterns(vals)))
        izin = [re.compile(AD.norm(k), re.I) for k in e.get("izinli_kaliplar", [])]
        for yol in dosyalar:
            if yol == kayit_rel:
                continue
            k = AD.katman(yol)
            if k not in katmanlar:
                continue
            kod = not yol.endswith(".md")   # .py/.sh/.json/.html: tanımlayıcı/regex olabilir → yalnız rapor, uygula yazmaz
            try:
                metin = open(repo / yol, encoding="utf-8", errors="replace").read()
            except Exception:
                continue
            for i, satir in enumerate(metin.split("\n"), 1):
                n = AD.norm(satir)
                eslesen = next((v for v, p in pats if p.search(n)), None)
                if eslesen is None:
                    continue
                izinli = any(z.search(n) for z in izin)
                out.append({"yol": yol, "satir": i, "katman": k, "kod": kod, "izinli": izinli, "eski": eslesen, "yeni": e["replaced_by"], "metin": satir})
    return out


_TR = {"i": "[iıİI]", "u": "[uüUÜ]", "o": "[oöOÖ]", "s": "[sşSŞ]", "g": "[gğGĞ]", "c": "[cçCÇ]"}


def tr_regex(v):
    """ASCII-normalize edilmiş değeri Türkçe/ASCII her yazıma uyan regex'e çevirir (ı/i, ü/u, ş/s …)."""
    return "".join(_TR.get(ch, re.escape(ch)) if ch.isalpha() else re.escape(ch) for ch in AD.norm(v))


def yeniden_yaz(satir, eski, yeni):
    """eski→yeni, Türkçe/ASCII yazım farkına duyarsız, kelime sınırlı; büyük-küçük harf biçimi korunur."""
    def rep(m):
        s = m.group(0)
        if s.isupper(): return yeni.upper()
        if s[:1].isupper(): return yeni[:1].upper() + yeni[1:]
        if s.islower(): return yeni.lower()
        return yeni
    return re.sub(r"(?<![\w-])" + tr_regex(eski) + r"(?![\w])", rep, satir, flags=re.I)


def cmd_kaydet(a, repo):
    reg = AD.load_registry(str(kayit_yolu(repo)))
    if not (a.anahtar and a.eski and a.yeni and a.tarih and a.gerekce):
        print("kaydet: --anahtar --eski --yeni --tarih --gerekce zorunlu", file=sys.stderr); return 2
    if AD.norm(a.eski) == AD.norm(a.yeni):
        print("kaydet: çevrim — eski = yeni", file=sys.stderr); return 2
    satir = {"deger": a.eski, "varyantlar": a.varyant or [], "tarih": a.tarih, "gerekce": a.gerekce, "replaced_by": a.yeni,
             "izinli_kaliplar": ["emekli", "eski ad", "eski adı", "cascade", "anahtar_terim", "süpersede", "supersede", "→ " + AD.norm(a.yeni), "= " + AD.norm(a.yeni)] + (a.izinli or []),
             "kaldirma_en_erken": "seans+3"}
    mevcut = anahtar_bul(reg, a.anahtar)
    if mevcut:
        if AD.norm(mevcut["guncel"]["deger"]) != AD.norm(a.yeni):
            print(f"kaydet: mevcut anahtarın güncel değeri '{mevcut['guncel']['deger']}' ≠ --yeni '{a.yeni}' (zincir derinliği >1 yasak; önce güncel değeri değiştir)", file=sys.stderr); return 2
        cikti = {"anahtar_id": a.anahtar, "islem": "mevcut anahtara emekli satırı ekle (`emekli` dizisine)", "emekli_satiri": satir}
    else:
        cikti = {"anahtar_id": a.anahtar, "islem": "yeni anahtar (`anahtarlar` dizisine)", "kayit": {
            "anahtar_id": a.anahtar, "tur": a.tur, "guncel": {"deger": a.yeni, "gecerli_bas": a.tarih, "kaynak": a.kaynak or "Salih kararı (tarih/karar no yaz)"},
            "emekli": [satir], "aday": [], "not": ""}}
    cikti["sonraki"] = ["core/baglam-anahtar-kaydi.md §2 JSON bloğuna Edit ile ekle (Katman-1 sınıfıysa Salih imzası)", "python3 tools/anahtar-denetim.py (baseline)", f"python3 tools/anahtar-cascade.py tara --anahtar {a.anahtar}"]
    print(json.dumps(cikti, ensure_ascii=False, indent=1)); return 0


def cmd_tara(a, repo):
    reg = AD.load_registry(str(kayit_yolu(repo))); an = anahtar_bul(reg, a.anahtar)
    if not an:
        print(f"tara: anahtar yok: {a.anahtar}", file=sys.stderr); return 2
    katmanlar = {"sicak": ["sicak"], "ilik": ["ilik"], "hepsi": ["sicak", "ilik", "soguk"]}[a.katman]
    hits = kalintilar(repo, an, katmanlar)
    ihlal = [h for h in hits if not h["izinli"]]
    if a.json:
        print(json.dumps({"anahtar": a.anahtar, "kalinti": len(hits), "ihlal": len(ihlal), "satirlar": ihlal}, ensure_ascii=False)); return 1 if ihlal else 0
    say = {}
    for h in hits:
        say.setdefault(h["katman"], [0, 0]); say[h["katman"]][0 if h["izinli"] else 1] += 1
    print(f"CASCADE TARAMA · {a.anahtar} · " + " · ".join(f"{k}: ihlal {v[1]} / izinli {v[0]}" for k, v in sorted(say.items())))
    for h in ihlal[: a.goster]:
        if h["kod"]:
            print(f"  {h['yol']}:{h['satir']} [{h['katman']} · kod: uygula YAZMAZ, elle bak]\n    - {h['metin'].strip()[:150]}")
        else:
            print(f"  {h['yol']}:{h['satir']} [{h['katman']}]\n    - {h['metin'].strip()[:150]}\n    + {yeniden_yaz(h['metin'], h['eski'], h['yeni']).strip()[:150]}")
    if len(ihlal) > a.goster:
        print(f"  … +{len(ihlal) - a.goster} satır (--goster N)")
    if ihlal:
        print("  → uygula: python3 tools/anahtar-cascade.py uygula --anahtar %s --katman %s --onay   (soğuk asla yazılmaz; anlamı bozan satırı izinli kalıba al ya da elle yaz)" % (a.anahtar, "sicak" if "sicak" in katmanlar else "ilik"))
    return 1 if ihlal else 0


def cmd_uygula(a, repo):
    reg = AD.load_registry(str(kayit_yolu(repo))); an = anahtar_bul(reg, a.anahtar)
    if not an:
        print(f"uygula: anahtar yok: {a.anahtar}", file=sys.stderr); return 2
    if a.katman == "hepsi":
        print("uygula: soğuk katman (tarihçe) yazılmaz; --katman sicak|ilik", file=sys.stderr); return 2
    tum = [h for h in kalintilar(repo, an, [a.katman]) if not h["izinli"]]
    kod = [h for h in tum if h["kod"]]; hits = [h for h in tum if not h["kod"]]
    if kod:
        print(f"uygula: {len(kod)} kod satırı (.py/.sh/.json/.html) atlandı — tanımlayıcı/regex olabilir, elle: " + " · ".join(sorted({h['yol'] for h in kod})[:5]))
    if not a.onay:
        print(f"uygula: {len(hits)} md satırı yeniden yazılacak; --onay verilmedi (diff üret → onay modeli, §1 ilke 9)"); return 1 if hits else 0
    dosya = {}
    for h in hits:
        dosya.setdefault(h["yol"], []).append(h)
    yazilan = 0
    for yol, hs in dosya.items():
        p = repo / yol; satirlar = open(p, encoding="utf-8").read().split("\n")
        for h in hs:
            satirlar[h["satir"] - 1] = yeniden_yaz(satirlar[h["satir"] - 1], h["eski"], h["yeni"]); yazilan += 1
        open(p, "w", encoding="utf-8").write("\n".join(satirlar))
    print(f"uygula: {yazilan} satır / {len(dosya)} dosya yeniden yazıldı ({a.katman}); sonra: python3 tools/anahtar-denetim.py --anahtar {a.anahtar} → sıcak ihlal 0 ⇒ [icra] commit 'retire {a.anahtar}: {an['emekli'][-1]['deger']}→{an['guncel']['deger']}, cascade {len(dosya)} dosya'")
    return 0


def cmd_readme(a, repo):
    reg = AD.load_registry(str(kayit_yolu(repo))); an = anahtar_bul(reg, a.anahtar)
    if not an:
        print(f"readme: anahtar yok: {a.anahtar}", file=sys.stderr); return 2
    ALT = {"core": "CLAUDE.md", ".claude": "kaynak-kodu/README.md", "tools": "tools/SCRIPTLER.md"}
    hits = kalintilar(repo, an, ["sicak", "ilik", "soguk"])
    # yalnız izinli-kalıpsız (bağlanmamış) kalıntı barındıran dizinler sayılır; README bloğu Karar 93 EK sınıfı ("her kombinasyonda bilinsin")
    # Salih kararıyla zorunludur, aksi hâlde FLAG (çıkış 0). --zorunlu ile çıkış 1.
    dizinler = sorted({h["yol"].split("/")[0] for h in hits if "/" in h["yol"] and not h["izinli"]})
    eski = [e["deger"] for e in an.get("emekli", [])]; yeni = an["guncel"]["deger"]
    bag = re.compile(r"(" + "|".join(re.escape(AD.norm(e)) for e in eski) + r")\s*(=|→|->|emekli|eski ad)", re.I)
    sonuc = []
    for d in dizinler:
        rd = ALT.get(d, f"{d}/README.md"); p = repo / rd
        if not p.exists():
            sonuc.append({"dizin": d, "readme": rd, "durum": "README-YOK"}); continue
        t = AD.norm(open(p, encoding="utf-8", errors="replace").read())
        sonuc.append({"dizin": d, "readme": rd, "durum": "PASS" if bag.search(t) else "EKSİK"})
    eksik = [s for s in sonuc if s["durum"] != "PASS"]
    if a.json:
        print(json.dumps({"anahtar": a.anahtar, "dizinler": sonuc, "eksik": len(eksik)}, ensure_ascii=False)); return 1 if eksik else 0
    print(f"README BAĞLAMA (Karar 93 EK K2 deseni) · {a.anahtar} · {' / '.join(eski)} = {yeni} · dizin {len(sonuc)} · eksik {len(eksik)}")
    for s in sonuc:
        print(f"  [{s['durum']:9}] {s['readme']}")
    if eksik:
        print(f"  → {'ZORUNLU' if a.zorunlu else 'FLAG'}: her eksik README'ye tek satır: \"{' / '.join(eski)} = {yeni} (eski değer; anahtar {a.anahtar}, kayıt core/baglam-anahtar-kaydi.md)\"")
    return 1 if (eksik and a.zorunlu) else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("komut", choices=["kaydet", "tara", "uygula", "readme"])
    ap.add_argument("--repo", default=str(pathlib.Path.home() / "sistem" / "jarvis")); ap.add_argument("--json", action="store_true")
    ap.add_argument("--anahtar"); ap.add_argument("--eski"); ap.add_argument("--yeni"); ap.add_argument("--tarih"); ap.add_argument("--gerekce"); ap.add_argument("--kaynak")
    ap.add_argument("--tur", default="kavram", choices=["tetik", "skill_adi", "yuzey", "kavram", "kart", "dosya"])
    ap.add_argument("--varyant", nargs="*"); ap.add_argument("--izinli", nargs="*")
    ap.add_argument("--katman", default="sicak", choices=["sicak", "ilik", "hepsi"]); ap.add_argument("--onay", action="store_true"); ap.add_argument("--goster", type=int, default=12)
    ap.add_argument("--zorunlu", action="store_true", help="readme: eksik README bloğu ihlal sayılsın (Karar 93 EK sınıfı Salih kararı)")
    a = ap.parse_args(); repo = pathlib.Path(a.repo).expanduser().resolve()
    if not kayit_yolu(repo).exists():
        print(f"kayıt dosyası yok: {kayit_yolu(repo)}", file=sys.stderr); sys.exit(2)
    sys.exit({"kaydet": cmd_kaydet, "tara": cmd_tara, "uygula": cmd_uygula, "readme": cmd_readme}[a.komut](a, repo))


if __name__ == "__main__":
    main()
