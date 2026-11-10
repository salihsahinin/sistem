#!/usr/bin/env python3
"""kural-sayaci.py — EŞZAMANLI KURAL SAYISI sayacı (KB-50 (a), Salih imzası 08-21 Karar 61: bağlam bütçesi kural seti — "eşzamanlı kural sayısı ≤100";
icra İB-23, 2026-08-22 seans-14). STDLIB ONLY, deterministik (yalnız disk).

Ne sayar: bir oturumun BAŞINDA bağlamda duran kural-taşıyıcı dosyalardaki KURAL BİRİMLERİ — varsayılan küme: CLAUDE.md (her oturum) +
SessionStart hook çıktısı (brif; kural satırı sayılmaz, yalnız boyut raporlanır) + `--skill <ad>` ile o skill'in SKILL.md'si (çağrılınca yüklenir).
Kural birimi (yazılı, dar tanım — m.39 uydurma yok): madde satırı (`- ` · `N. ` · `* `) ∨ kalın-başlı cümle (`**…**` ile başlayan satır) ∨ içinde
ZORUNLULUK işareti taşıyan satır (YASAK · ZORUNLU · yalnız · asla · her · ≤ · ≥ · m.NN · md.NN · Katman-1/2). Başlık/boş/tablo-ayraç satırları sayılmaz.
Aynı satır birden çok işaret taşısa da 1 birim (satır grain). Sınır (yazılı): cümle-içi birden çok kural tek sayılır; anlatı satırı işaret
taşıyorsa fazla sayılır — sayı satır-grain KESTİRİMİDİR (iki yönlü yanlılık: ↓ cümle-içi çoklu kural tek · ↑ işaretli anlatı satırı sayılır); eşik (100) m.29 deneysel, ≥10 koşumda kalibre.

Çıktı: dosya başına birim · toplam · eşik hükmü; `--json`; `--kutuk` ile veri/kural-sayim.jsonl'e APPEND (grain: 1 satır = 1 dosya × 1 koşum).
Çıkış: 0 · 1 eşik AŞIMI (uyarı modu DEĞİL: sayı bütçe kuralıdır; hat dışı elle koşum) · 2 dosya yok.
Kullanım: python3 tools/kural-sayaci.py [--repo <yol>] [--dosya CLAUDE.md ...] [--skill seans-acilis ...] [--esik 100] [--json] [--kutuk]
"""
import argparse, hashlib, json, os, re, subprocess, sys
from datetime import datetime, timezone

ISARET = re.compile(r"(YASAK|ZORUNLU|yaln[ıi]z|asla|\bher\b|≤|≥|\bm\.\d+|\bmd\.\d+|Katman-[12]|KURAL|kural)", re.I)
MADDE = re.compile(r"^\s*(?:[-*•]|\d+[.)])\s+\S")
KALIN = re.compile(r"^\s*\*\*[^*]+\*\*")
BASLIK = re.compile(r"^\s*#{1,6}\s")


def say(yol):
    try:
        with open(yol, encoding="utf-8") as fh:
            satirlar = fh.read().split("\n")
    except OSError:
        return None
    n, ornek = 0, []
    for ln, s in enumerate(satirlar, 1):
        t = s.strip()
        if not t or BASLIK.match(s) or t.startswith("|---") or t.startswith("```"):
            continue
        if MADDE.match(s) or KALIN.match(s) or ISARET.search(t):
            n += 1
            if len(ornek) < 3:
                ornek.append("%d: %s" % (ln, t[:70]))
    return {"dosya": os.path.relpath(yol), "satir": len(satirlar), "byte": sum(len(x.encode("utf-8")) + 1 for x in satirlar), "kural_birimi": n, "ornek": ornek}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.getcwd())
    ap.add_argument("--dosya", nargs="*", default=["CLAUDE.md"], help="sayılacak kural dosyaları (varsayılan CLAUDE.md)")
    ap.add_argument("--skill", nargs="*", default=[], help="çağrılacak skill adları (.claude/skills/<ad>/SKILL.md eklenir)")
    ap.add_argument("--esik", type=int, default=100, help="KB-50 (a) eşiği (deneysel m.29)")
    ap.add_argument("--json", action="store_true"); ap.add_argument("--kutuk", action="store_true")
    a = ap.parse_args(); repo = os.path.abspath(a.repo)
    dosyalar = list(a.dosya) + [".claude/skills/%s/SKILL.md" % s for s in a.skill]
    sonuc, eksik = [], []
    for d in dosyalar:
        r = say(os.path.join(repo, d))
        (sonuc if r else eksik).append(r or d)
    if eksik:
        print("[HATA] dosya yok: %s" % ", ".join(eksik), file=sys.stderr); sys.exit(2)
    hook = os.path.join(repo, ".claude", "hooks", "session-start.sh"); hook_byte = None
    if os.path.exists(hook):
        try:
            hook_byte = len(subprocess.run(["bash", hook], cwd=repo, capture_output=True, stdin=subprocess.DEVNULL, timeout=20).stdout)
        except Exception:
            hook_byte = None
    toplam = sum(r["kural_birimi"] for r in sonuc)
    hukum = "AŞIM" if toplam > a.esik else "OK"
    ts = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    try:
        head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip()
    except Exception:
        head = "?"
    if a.json:
        print(json.dumps({"ts": ts, "head": head, "dosyalar": sonuc, "hook_cikti_byte": hook_byte, "toplam": toplam, "esik": a.esik, "hukum": hukum}, ensure_ascii=False, indent=1))
    else:
        print("kural-sayacı @ %s · eşik %d (KB-50 a, m.29) · hook çıktısı %s byte" % (head, a.esik, hook_byte))
        for r in sonuc:
            print("  %-45s %4d birim / %4d satır / %6d byte" % (r["dosya"], r["kural_birimi"], r["satir"], r["byte"]))
        print("  TOPLAM %d → %s" % (toplam, hukum) + ("" if hukum == "OK" else " — KB-50 (a): kural sayısı ≤%d; damıtma/birleştirme gerekir" % a.esik))
    if a.kutuk:
        with open(os.path.join(repo, "veri", "kural-sayim.jsonl"), "a", encoding="utf-8") as fh:
            for r in sonuc:
                fh.write(json.dumps({"ts": ts, "head": head, "dosya": r["dosya"], "kural_birimi": r["kural_birimi"], "satir": r["satir"], "byte": r["byte"],
                                     "esik": a.esik, "toplam": toplam, "hukum": hukum, "hook_cikti_byte": hook_byte}, ensure_ascii=False) + "\n")
    sys.exit(1 if hukum == "AŞIM" else 0)


if __name__ == "__main__":
    main()
