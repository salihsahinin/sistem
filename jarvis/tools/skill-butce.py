#!/usr/bin/env python3
"""skill-butce.py — SKILL description BÜTÇE ölçer (İB-77 S-C bulgusu: bütçe 7.379/7.380 char,
ölçen araç yoktu). STDLIB ONLY, deterministik (yalnız disk).

Ne yapar: `<repo>/.claude/skills/*/SKILL.md` (proje hazinesi) + `~/.claude/skills/*/SKILL.md`
(kullanıcı-düzeyi) altındaki her SKILL.md'nin YAML frontmatter'ındaki `description:` alanının
karakter uzunluğunu sayar. Symlink'ler gerçek yola (os.path.realpath) çözülür ve aynı gerçek
dosya iki kez sayılmaz (proje kaydı önceliklidir — ilk görülen kazanır).

Frontmatter okuma: yaml paketi YOK, basit satır-tarayıcı. Dosyanın ilk satırı `---` olmalı;
ikinci `---` frontmatter'ı kapatır. Bu blok içinde `description:` ile başlayan satır aranır.
Tek-satır biçim: `description: metin` → değer aynen (tırnaklar soyulur). Çok-satırlı YAML blok
skaler biçimi (`description: >` ya da `description: |`) desteklenir: description satırından
sonra gelen, description'dan daha girintili satırlar birleştirilir (`>` katlamalı-stil için tek
boşlukla, `|` blok-stil için '\n' ile birleştirilir; ayrım kabaca yapılır, kesin YAML semantiği
hedeflenmez — stdlib-only sınırı m.39 ile yazılı).

Token yaklaşımı: char/4,1 (kaynak: core/skill-uretim-semasi.md:64 — "4,1 char/token — çevrim
ÖLÇÜLDÜ", Salih /context 08-20, KB-19 Karar 33).

Çıktı (insan): tablo — skill adı · kaynak (proje/kullanıcı) · char · ~token · kümülatif char;
sonda TOPLAM char / bütçe (varsayılan 7380, core/skill-uretim-semasi.md:64 — "7.380 char") /
kalan pay / en uzun 5 description. --json: tek nesne (AXI: stdout TEK JSON nesnesi)
{arac, surum, git_head, toplam_char, butce, kalan, skill_n, satirlar:[...]}.

--aday <char>: eklenmek istenen yeni description uzunluğunu verir; "sığar mı, sığmazsa hangi
skill'lerden toplam kaç char kısaltılmalı" satırı basar — deterministik minimal küme: description
uzunluğuna göre AZALAN sırada (eşitlikte ad'a göre artan/ikincil) en uzunlardan başlayarak, gereken
fazlalık kapanana dek skill biriktirir.

Çıkış kodu: 0 bütçe içinde (--aday ile de sığıyorsa) · 3 bütçe AŞIMI (FAIL-LOUD, stderr tek satır)
· 2 girdi hatası (taranacak dizin/dosya okunamadı ya da hiç skill bulunamadı).

Kullanım:
  python3 tools/skill-butce.py [--repo <yol>] [--butce 7380] [--aday <char>] [--json] [--sessiz]
"""
import argparse
import json
import os
import re
import subprocess
import sys

SURUM = "1.0.0"
ARAC = "skill-butce"
VARSAYILAN_BUTCE = 7380
CEVRIM = 4.1  # char/token — core/skill-uretim-semasi.md:64


def _frontmatter_satirlari(yol):
    """Dosyanın --- ... --- arası frontmatter satırlarını döndürür (yoksa None)."""
    try:
        with open(yol, encoding="utf-8", errors="replace") as fh:  # üçüncü-parti skill dosyası UTF-8 olmayabilir (09-22: lavish SKILL.md cp1252 `—`); sayım bozulmaz, çökmez
            satirlar = fh.read().split("\n")
    except OSError:
        return None
    if not satirlar or satirlar[0].strip() != "---":
        return None
    for i in range(1, len(satirlar)):
        if satirlar[i].strip() == "---":
            return satirlar[1:i]
    return None


def description_oku(yol):
    """SKILL.md'den description değerini (tek satıra birleştirilmiş) döndürür; yoksa ''."""
    fm = _frontmatter_satirlari(yol)
    if fm is None:
        return None
    desc_re = re.compile(r"^description:\s*(.*)$")
    for idx, s in enumerate(fm):
        m = desc_re.match(s.strip())
        if not m:
            continue
        deger = m.group(1).strip()
        girinti_taban = len(s) - len(s.lstrip())
        if deger in (">", "|", ">-", "|-", ">+", "|+"):
            katlamali = deger.startswith(">")
            ayrac = " " if katlamali else "\n"
            parcalar = []
            for devam in fm[idx + 1:]:
                if not devam.strip():
                    if not katlamali:
                        parcalar.append("")
                    continue
                girinti = len(devam) - len(devam.lstrip())
                if girinti <= girinti_taban:
                    break
                parcalar.append(devam.strip() if katlamali else devam[girinti_taban + 1:] if len(devam) > girinti_taban else devam.strip())
            return ayrac.join(p for p in parcalar).strip()
        # tek satır — tırnak soy
        if len(deger) >= 2 and deger[0] == deger[-1] and deger[0] in "\"'":
            deger = deger[1:-1]
        return deger
    return ""


def hazine_tara(repo):
    """Proje + kullanıcı hazinelerini tarar; symlink gerçek-yol tekilleştirmesiyle liste döndürür."""
    kayitlar, gorulen_gercek = [], set()

    def dizin_tara(kok, kaynak):
        if not os.path.isdir(kok):
            return
        for ad in sorted(os.listdir(kok)):
            skill_md = os.path.join(kok, ad, "SKILL.md")
            if not os.path.isfile(skill_md):
                continue
            gercek = os.path.realpath(skill_md)
            if gercek in gorulen_gercek:
                continue
            gorulen_gercek.add(gercek)
            desc = description_oku(skill_md)
            if desc is None:
                continue
            kayitlar.append({"ad": ad, "kaynak": kaynak, "char": len(desc), "yol": skill_md})

    dizin_tara(os.path.join(repo, ".claude", "skills"), "proje")
    dizin_tara(os.path.join(os.path.expanduser("~"), ".claude", "skills"), "kullanici")
    return kayitlar


def minimal_kisaltma_kumesi(kayitlar, fazlalik):
    """Azalan char sırasında (eşitlikte ad artan) fazlalığı kapatan minimal küme."""
    sirali = sorted(kayitlar, key=lambda r: (-r["char"], r["ad"]))
    secilen, toplam = [], 0
    for r in sirali:
        if toplam >= fazlalik:
            break
        secilen.append(r)
        toplam += r["char"]
    return secilen, toplam


def git_head(repo):
    try:
        r = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True, timeout=10)
        return r.stdout.strip() or "?"
    except Exception:
        return "?"


def main():
    ap = argparse.ArgumentParser(description="Skill description bütçesi ölçer (char/token).")
    ap.add_argument("--repo", default=os.getcwd())
    ap.add_argument("--butce", type=int, default=VARSAYILAN_BUTCE, help="char bütçesi (varsayılan 7380, skill-uretim-semasi.md:64)")
    ap.add_argument("--aday", type=int, default=None, help="eklenecek yeni description uzunluğu (char)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--sessiz", action="store_true", help="yalnız çıkış kodu; insan tablosu basılmaz")
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)

    kayitlar = hazine_tara(repo)
    if not kayitlar:
        print("[HATA] hiç SKILL.md bulunamadı (.claude/skills/*/SKILL.md — proje ve kullanıcı)", file=sys.stderr)
        sys.exit(2)

    kayitlar_sirali = sorted(kayitlar, key=lambda r: (-r["char"], r["ad"]))
    kumulatif = 0
    satirlar = []
    for r in kayitlar_sirali:
        kumulatif += r["char"]
        satirlar.append({
            "ad": r["ad"], "kaynak": r["kaynak"], "char": r["char"],
            "token_yaklasik": round(r["char"] / CEVRIM, 1), "kumulatif": kumulatif,
        })

    toplam = sum(r["char"] for r in kayitlar)
    kalan = a.butce - toplam
    hukum_askin = toplam > a.butce
    head = git_head(repo)

    aday_satiri = None
    if a.aday is not None:
        if a.aday < 0:
            print("[HATA] --aday negatif olamaz", file=sys.stderr)
            sys.exit(2)
        yeni_toplam = toplam + a.aday
        if yeni_toplam <= a.butce:
            aday_satiri = "ADAY %d char SIĞAR — toplam %d + aday %d = %d ≤ bütçe %d (kalan %d)" % (
                a.aday, toplam, a.aday, yeni_toplam, a.butce, a.butce - yeni_toplam)
        else:
            fazlalik = yeni_toplam - a.butce
            secilen, kisaltilan_toplam = minimal_kisaltma_kumesi(kayitlar, fazlalik)
            ad_listesi = ", ".join("%s(%d)" % (r["ad"], r["char"]) for r in secilen)
            aday_satiri = ("ADAY %d char SIĞMAZ — toplam %d + aday %d = %d > bütçe %d; "
                            "gereken kısaltma ≥%d char, minimal küme (en uzundan): %s → toplam %d char kısaltılırsa sığar" % (
                                a.aday, toplam, a.aday, yeni_toplam, a.butce, fazlalik, ad_listesi, kisaltilan_toplam))

    if a.json:
        cikti = {
            "arac": ARAC, "surum": SURUM, "git_head": head,
            "toplam_char": toplam, "butce": a.butce, "kalan": kalan,
            "skill_n": len(kayitlar), "satirlar": satirlar,
        }
        if aday_satiri is not None:
            cikti["aday_char"] = a.aday
            cikti["aday_hukmu"] = aday_satiri
        print(json.dumps(cikti, ensure_ascii=False, indent=1))
    elif not a.sessiz:
        print("skill-bütçe @ %s · bütçe %d char (skill-uretim-semasi.md:64) · çevrim %.1f char/token" % (head, a.butce, CEVRIM))
        print("%-30s %-9s %6s %8s %10s" % ("skill", "kaynak", "char", "~token", "kümülatif"))
        for s in satirlar:
            print("%-30s %-9s %6d %8.1f %10d" % (s["ad"], s["kaynak"], s["char"], s["token_yaklasik"], s["kumulatif"]))
        print("TOPLAM %d char / bütçe %d / kalan %d → %s" % (toplam, a.butce, kalan, "AŞIM" if hukum_askin else "OK"))
        print("En uzun 5: " + ", ".join("%s(%d)" % (r["ad"], r["char"]) for r in kayitlar_sirali[:5]))
        if aday_satiri is not None:
            print(aday_satiri)

    if hukum_askin:
        print("[HATA] skill-bütçe AŞIM: toplam %d > bütçe %d" % (toplam, a.butce), file=sys.stderr)
        sys.exit(3)
    sys.exit(0)


if __name__ == "__main__":
    main()
