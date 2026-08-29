#!/usr/bin/env python3
"""loop-dedektor.py — KURAL-TABANLI LOOP DEDEKTÖRÜ (İB-60; EK-6 masası F4 → Karar 78 / m.43 2. rev; Karar 65 determinizm). STDLIB ONLY, LLM YOK.

Soru: Carvis'in araç-çağrı dizileri (silver `hareket`) içinde OTURUMLAR ARASI tekrar eden GÖREV dizileri var mı? m.43: "aynı adım kümesi
oturumlar arası ≥N kez tekrar ettiğinde otomatik skill ADAYI olur" — 2. rev (Karar 78, Salih 08-29): tekrar-BİRİMİ = GÖREV, eşik N=3,
pencere son 90 gün (m.43 (a) "sayaç son-90-gün pencereli"). Bu araç yalnız SAYAR ve ADAY yazar; skill inşası ayrı karardır (m.13, K-016).

GÖREV İMZASI (deterministik normalizasyon — içerik değil, hedef sınıfı):
  Bash  → çağrılan program zinciri: `python3 tools/X.py`→`py:X` · `python3 -` (heredoc)→`py:inline` · `git <alt>`→`git:<alt>` · `sqlite3`→`sqlite3` · diğer ilk sözcük (≤3 öğe, sıralı)
  Read/Edit/Write → `<arac>:<yol-sınıfı>` (repo-göreli ilk dizin; `core/durum-kapsulu.md`/`core/pano.md` gibi tekil kanon dosyaları AYNEN;
                    `.claude/skills` ikinci düzey; repo dışı → `dış`)
  Agent → `Agent:<tip>` ([köşeli] etiket) · Skill → `Skill:<ad>` · Workflow/diğer → araç adı
LOOP ADAYI = n-gram (n=2..5) ardışık görev imzası; aynı oturumdaki tekrar 1 sayılır; k_W = pencere içinde dizinin geçtiği FARKLI oturum sayısı
  (core/skill-uretim-semasi.md Z1 `k_W` ile aynı tanım: oturumlar-arası; özdeş ↔ varyant ayrı imza). durum: ADAY (k_W ≥ N) · ESIK-ALTI.
  `skill_ici=1`: dizide Skill çağrısı var YA DA geçişlerin ≥yarısı bir Skill çağrısını izleyen 8 adım içinde (ritüel/skill icrası) → zaten skill kapsamında (bilgi; aday değil). Alt-dizi bastırma: daha uzun bir ADAY dizinin
  içinde aynı k_W ile geçen kısa dizi `kapsanan=1` işaretlenir (liste şişmesin; silinmez).
ÇIKTI: veri/gorunum/v_loop_aday.csv (tam liste; imza_sha8 ile idempotent) · veri/loop-dedektor.jsonl (append-only koşum özeti: head, W, N,
  oturum sayısı, aday sayısı, ilk 5 aday) · `--kutu`: ADAY ∧ ¬skill_ici ∧ ¬kapsanan satırlarını kuyruk/skill-fikir-kutusu.md
  "## m.43 sayaçları" altına imza_sha8 ile TEK KEZ düşer — yalnız n≥3 diziler (m.43 "adım KÜMESİ"; inşa değil).
Kullanım: python3 tools/loop-dedektor.py [--repo <yol>] [--db veri/baglam.sqlite] [--n 3] [--pencere-gun 90] [--bugun YYYY-MM-DD] [--kutu] [--sessiz]
Çıkış: 0 tamam · 2 girdi yok. Deneysel m.29 (2026-08-29, Carvis, icra devam oturumu). Kayıt: tools/SCRIPTLER.md.
"""
import argparse, csv, hashlib, json, os, re, sqlite3, subprocess, sys
from datetime import date, datetime, timedelta, timezone

TEKIL_KANON = {"CLAUDE.md", "core/durum-kapsulu.md", "core/pano.md", "core/tuzuk-v0.md", "kuyruk/senaryo-defteri.md", "fikir-kutusu.md",
               "kuyruk/skill-fikir-kutusu.md", "tools/SCRIPTLER.md", "veri/README.md", "wiki/README.md", "KILAVUZ.md"}
BASH_RX = re.compile(r"⟨(.*)⟩", re.S)
SKILL_PENCERE = 8  # bir Skill çağrısından sonraki 8 adım o skill'in icra penceresi sayılır (deneysel m.29 [?])


def yol_sinifi(yol):
    if not yol:
        return "?"
    yol = yol.replace("\\", "/")
    if yol.startswith("/") or yol.startswith("~"):
        return "dış"
    yol = yol.split(" [")[0].strip()
    if yol in TEKIL_KANON:
        return yol
    p = [x for x in yol.split("/") if x]
    if not p:
        return "?"
    if p[0] in (".claude", "cc", "kuyruk", "veri") and len(p) > 2:
        return p[0] + "/" + p[1]
    return p[0] if len(p) > 1 else "kök"


def bash_imza(hedef):
    m = BASH_RX.search(hedef or "")
    cmd = m.group(1) if m else (hedef or "")
    zincir = []
    # heredoc gövdeleri (<<'EOF' … EOF) imzaya girmez: işaretçiden sonlandırıcı satıra kadar atlanır
    hd = re.compile(r"<<-?\s*['\"]?(\w+)['\"]?")
    temiz = ""; rest = cmd
    while True:
        m2 = hd.search(rest)
        if not m2:
            temiz += rest; break
        temiz += rest[:m2.start()] + "\n"  # heredoc sonrası komut ayrı segment
        son = re.search(r"\n%s\s*(\n|$)" % re.escape(m2.group(1)), rest[m2.end():])
        if not son:
            break
        rest = rest[m2.end() + son.end():]
    for parca in re.split(r"[;&|\n]+", temiz):
        tok = parca.strip().split()
        tok = [t for t in tok if t]
        i = 0
        while i < len(tok) and (tok[i] in ("cd", "S=", "sudo", "time", "nohup") or "=" in tok[i] and not tok[i].startswith("-")) :
            i += 2 if tok[i] == "cd" else 1
        if i >= len(tok):
            continue
        t = tok[i]
        if t in ("python3", "python", ".venv/bin/python"):
            hedef_py = next((x for x in tok[i + 1:] if x.endswith(".py")), None)
            imza = "py:" + os.path.basename(hedef_py).replace(".py", "") if hedef_py else "py:inline"
        elif t == "git":
            alt = next((x for x in tok[i + 1:] if not x.startswith("-")), "?")
            imza = "git:" + alt
        else:
            imza = os.path.basename(t)
        if imza not in zincir:
            zincir.append(imza)
        if len(zincir) >= 3:
            break
    return "Bash:" + "+".join(zincir) if zincir else "Bash:-"


def imza(arac, hedef, dosya):
    if arac == "Bash":
        return bash_imza(hedef)
    if arac in ("Read", "Edit", "Write", "NotebookEdit"):
        return "%s:%s" % (arac, yol_sinifi(dosya or hedef))
    if arac == "Agent":
        m = re.match(r"\[([^\]]+)\]", hedef or "")
        return "Agent:" + (m.group(1) if m else "?")
    if arac == "Skill":
        return "Skill:" + ((hedef or "?").split()[0] if hedef else "?")
    return arac


def main():
    ap = argparse.ArgumentParser(description="loop dedektörü (İB-60)")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--db", default=None); ap.add_argument("--n", type=int, default=3); ap.add_argument("--pencere-gun", type=int, default=90)
    ap.add_argument("--bugun", default=None); ap.add_argument("--kutu", action="store_true"); ap.add_argument("--sessiz", action="store_true")
    a = ap.parse_args(); repo = os.path.abspath(a.repo)
    db = a.db or os.path.join(repo, "veri", "baglam.sqlite")
    if not os.path.exists(db):
        print("HATA: silver yok: %s" % db, file=sys.stderr); return 2
    con = sqlite3.connect(db)
    if not con.execute("SELECT COUNT(*) FROM sqlite_master WHERE name='hareket'").fetchone()[0]:
        print("HATA: hareket tablosu yok — tools/hareket-tablo.py", file=sys.stderr); return 2
    bugun = date.fromisoformat(a.bugun) if a.bugun else date.today()
    esik_gun = (bugun - timedelta(days=a.pencere_gun)).isoformat()
    rows = con.execute("SELECT oturum_id, sira, arac, hedef, dosya, tarih_tr FROM hareket WHERE tarih_tr >= ? ORDER BY oturum_id, sira", (esik_gun,)).fetchall()
    oturumlar = {}
    for oid, sira, arac, hedef, dosya, tarih in rows:
        oturumlar.setdefault(oid, {"dizi": [], "tarih": tarih})
        oturumlar[oid]["dizi"].append(imza(arac, hedef, dosya))
        oturumlar[oid]["tarih"] = min(oturumlar[oid]["tarih"], tarih)
    # n-gram → {oturum: sayı}
    ngram = {}; skillde = {}
    for oid, o in oturumlar.items():
        d = o["dizi"]
        # ardışık özdeş tekrarı tek imzaya indir (aynı görevin peş peşe koşumu dizi değil, tekrar)
        d2 = [d[0]] if d else []
        for x in d[1:]:
            if x != d2[-1]:
                d2.append(x)
        son_skill = -99; pencere = []
        for idx, x in enumerate(d2):
            if x.startswith("Skill:"):
                son_skill = idx
            pencere.append(idx - son_skill <= SKILL_PENCERE)
        for n in range(2, 6):
            for i in range(len(d2) - n + 1):
                g = tuple(d2[i:i + n])
                e = ngram.setdefault(g, {})
                e[oid] = e.get(oid, 0) + 1
                if pencere[i]:
                    skillde[g] = skillde.get(g, 0) + 1
    kayit = []
    for g, e in ngram.items():
        kw = len(e)
        if kw < 2:
            continue
        tarihler = sorted(oturumlar[o]["tarih"] for o in e)
        kayit.append({"imza": " → ".join(g), "n": len(g), "k_W": kw, "toplam_tekrar": sum(e.values()), "ilk_tarih": tarihler[0], "son_tarih": tarihler[-1],
                      "skill_ici": int(any(x.startswith("Skill:") for x in g) or skillde.get(g, 0) * 2 >= sum(e.values())), "ornek_oturum": sorted(e)[0][:8], "_g": g})
    # kapsanan: daha uzun ADAY dizinin alt-dizisi ∧ aynı k_W
    adaylar = [k for k in kayit if k["k_W"] >= a.n]
    uzun = [(k["_g"], k["k_W"]) for k in adaylar]
    for k in kayit:
        g = k["_g"]; k["kapsanan"] = 0
        for ug, ukw in uzun:
            if len(ug) > len(g) and ukw == k["k_W"] and any(ug[i:i + len(g)] == g for i in range(len(ug) - len(g) + 1)):
                k["kapsanan"] = 1; break
        k["durum"] = "ADAY" if k["k_W"] >= a.n else "ESIK-ALTI"
        k["imza_sha8"] = hashlib.sha1(k["imza"].encode("utf-8")).hexdigest()[:8]
    kayit.sort(key=lambda k: (-k["k_W"], -k["n"], -k["toplam_tekrar"], k["imza"]))
    adaylar = [k for k in kayit if k["k_W"] >= a.n]
    kolonlar = ["imza_sha8", "durum", "k_W", "n", "toplam_tekrar", "skill_ici", "kapsanan", "ilk_tarih", "son_tarih", "ornek_oturum", "imza"]
    gd = os.path.join(repo, "veri", "gorunum"); os.makedirs(gd, exist_ok=True)
    with open(os.path.join(gd, "v_loop_aday.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=kolonlar, extrasaction="ignore"); w.writeheader()
        for k in kayit:
            w.writerow(k)
    temiz = [k for k in adaylar if not k["skill_ici"] and not k["kapsanan"]]
    kutuluk = [k for k in temiz if k["n"] >= 3]  # m.43 "adım KÜMESİ": 2-adımlık dizi kutuya girmez (deneysel m.29 [?])
    try:
        head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip()
    except Exception:
        head = "?"
    ts = datetime.now(timezone(timedelta(hours=3))).replace(microsecond=0).isoformat()
    ozet = {"ts": ts, "git_head": head, "bugun": bugun.isoformat(), "pencere_gun": a.pencere_gun, "N": a.n, "oturum_n": len(oturumlar), "hareket_n": len(rows),
            "ngram_n": len(kayit), "aday_n": len(adaylar), "aday_temiz_n": len(temiz), "kutuluk_n": len(kutuluk), "ilk5": [{"imza": k["imza"], "k_W": k["k_W"], "n": k["n"]} for k in temiz[:5]], "llm": "yok"}
    with open(os.path.join(repo, "veri", "loop-dedektor.jsonl"), "a", encoding="utf-8") as fh:
        fh.write(json.dumps(ozet, ensure_ascii=False) + "\n")
    yazilan = 0
    if a.kutu and kutuluk:
        kp = os.path.join(repo, "kuyruk", "skill-fikir-kutusu.md"); s = open(kp, encoding="utf-8").read()
        baslik = "## m.43 sayaçları"
        if baslik not in s:
            print("UYARI: kutuda '%s' başlığı yok — kutu yazılmadı" % baslik, file=sys.stderr)
        else:
            yeni = []
            for k in kutuluk:
                if k["imza_sha8"] in s:
                    continue
                yeni.append("- **loop-aday `%s`** (İB-60 dedektörü %s, k_W=%d/%d oturum, n=%d, tekrar %d, %s→%s): `%s` — m.43 ADAY (inşa ayrı karar; K-016/skill-kapisi)" % (
                    k["imza_sha8"], bugun.isoformat(), k["k_W"], len(oturumlar), k["n"], k["toplam_tekrar"], k["ilk_tarih"], k["son_tarih"], k["imza"]))
            if yeni:
                i = s.index(baslik); j = s.find("\n## ", i + len(baslik)); j = len(s) if j < 0 else j
                blok = s[i:j].rstrip("\n") + "\n" + "\n".join(yeni) + "\n"
                s = s[:i] + blok + s[j:]; open(kp, "w", encoding="utf-8").write(s); yazilan = len(yeni)
    if not a.sessiz:
        print("loop-dedektor @ %s · pencere %d gün (≥%s) · oturum %d · hareket %d · n-gram(k_W≥2) %d · ADAY(k_W≥%d) %d · temiz aday %d · kutuluk(n≥3) %d · kutuya yazılan %d" % (
            head, a.pencere_gun, esik_gun, len(oturumlar), len(rows), len(kayit), a.n, len(adaylar), len(temiz), len(kutuluk), yazilan))
        for k in temiz[:12]:
            print("  ADAY k_W=%2d n=%d tekrar=%3d  %s" % (k["k_W"], k["n"], k["toplam_tekrar"], k["imza"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
