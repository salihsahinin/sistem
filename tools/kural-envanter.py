#!/usr/bin/env python3
"""kural-envanter.py — KURAL ENVANTERİ + DETERMİNİSTİK KÜMELEME (İB-51 adım 1-2; KB-66 Salih notu, Karar 74 M-7: "önce deterministik
envanter+kümeleme, atlas sonra"). STDLIB ONLY; LLM yok (Karar 65: router/etiketleyici LLM girmez).

Soru: sisteme yazılmış kurallar NEREDE yaşıyor, hangi yükleme anında bağlama giriyor, hangi görev sınıfına ait — böylece "her kural her
konuşmada yüklenir" maliyetine karşı görev-sınıfı → kural alt-kümesi eşlemesi kurulabilsin.

Kural birimi = tools/kural-sayaci.py `say()` tanımı (satır grain: madde ∨ kalın-başlı ∨ zorunluluk işareti; m.39 kestirim, iki yönlü yanlılık).
Taşıyıcı sınıfı (yükleme anı; deterministik, dosya yoluyla):
  T0 her-oturum     CLAUDE.md (otomatik yüklenir; hook brifi yalnız byte)
  T1 ritüel-skill   .claude/skills/seans-acilis, seans-kapanis (her seansta tetiklenir)
  T2 çağrı-skill    diğer skill SKILL.md'leri (yalnız çağrılınca)
  T3 kanon-pointer  core/tuzuk-v0.md + core/*.md kural dosyaları + KILAVUZ.md (pointer'la okunur; m.20)
  T4 wiki           wiki/*.md (SOP/Gotchas taşır; başvuru)
Görev sınıfı etiketi (çok-etiketli, anahtar-kelime kuralı; sınıf kimliği her satırda okunur — kural değişirse sayı değişir, m.29):
  ritüel · git · karar · ajan-koşum · veri-hattı · kanon-bakım · teslim · zaman · üslup-yasak · genel (eşleşmeyen)
Çıktı: veri/gorunum/v_kural_envanter.csv (1 satır = 1 kural birimi; ÜZERİNE yazılır, türev) · veri/gorunum/v_kural_envanter_ozet.csv
       (taşıyıcı × sınıf: birim, byte) · veri/kural-envanter.jsonl (APPEND-ONLY; 1 satır = 1 taşıyıcı × koşum özeti).
Kullanım: python3 tools/kural-envanter.py [--repo <yol>] [--sessiz] [--kuru]     Çıkış: 0 · 2 kural-sayaci.py yok.
Deneysel m.29 (2026-08-29, Carvis, yan icra oturumu). Kayıt: tools/SCRIPTLER.md.
"""
import argparse, csv, glob, hashlib, importlib.util, json, os, re, subprocess, sys
from datetime import datetime, timezone, timedelta

SINIF = [  # (ad, regex) — sıra = rapor sırası; bir satır birden çok sınıfa düşebilir
    ("ritüel", r"seans|açılış|kapanış|kapsül|brif|ritüel|SessionStart"),
    ("git", r"\bcommit|\bpush\b|\bgit\b|pathspec|PR\b|worktree"),
    ("karar", r"\bkarar|\bmasa\b|Katman-1|imza|çelişki|m\.16|m\.37|m\.40|Salih (tek|kararı)|BEKLET"),
    ("ajan-koşum", r"\bajan|skill|[Ww]orkflow|atlas|pipeline|işçi|effort|token|bütçe|alt-ajan|koşum"),
    ("veri-hattı", r"silver|bronz|gold|katman-hatti|sqlite|parquet|\btablo|şema|sözleşme|FTS|ambar|görünüm"),
    ("kanon-bakım", r"pointer|arşiv|damıt|süpersede|m\.8\b|m\.20|m\.21|m\.22|\bwiki|ingest|emekli|anahtar kayd"),
    ("teslim", r"teslim|\brapor|Finder|open -R|HTML|PDF|ilk ekran|mobil|Lavish|Obsidian"),
    ("zaman", r"AS-OF|anakronizm|tarih|damga|kesim|bayat|zaman"),
    ("üslup-yasak", r"YASAK|övgü|ruh|psikolog|ayıklık|m\.7\b|m\.23|m\.33|metafor|köle"),
]
RX = [(ad, re.compile(r, re.I)) for ad, r in SINIF]
CORE_KURAL = ["core/tuzuk-v0.md", "KILAVUZ.md", "core/ajan-metodolojisi.md", "core/skill-uretim-semasi.md", "core/skill-tetikleme-semasi.md",
              "core/halusinasyon-paketi.md", "core/sema-sikistirma.md", "core/baglam-anahtar-kaydi.md", "core/ingest-semasi.md",
              "core/veri-muhendisligi-katmani.md", "core/world-model-tasarimi.md", "core/varlik-felsefesi.md"]
RITUEL = {"seans-acilis", "seans-kapanis"}


def yukle_sayac(repo):
    yol = os.path.join(repo, "tools", "kural-sayaci.py")
    if not os.path.exists(yol):
        return None
    spec = importlib.util.spec_from_file_location("kural_sayaci", yol); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def birimler(m, repo, rel):
    """kural-sayaci ile AYNI birim kuralı (tek tanım): satır → (satır no, metin, byte)."""
    try:
        satirlar = open(os.path.join(repo, rel), encoding="utf-8").read().split("\n")
    except OSError:
        return []
    out = []
    for ln, s in enumerate(satirlar, 1):
        t = s.strip()
        if not t or m.BASLIK.match(s) or t.startswith("|---") or t.startswith("```"):
            continue
        if m.MADDE.match(s) or m.KALIN.match(s) or m.ISARET.search(t):
            out.append((ln, t, len(s.encode("utf-8")) + 1))
    return out


def tasiyicilar(repo):
    T = [("T0 her-oturum", "CLAUDE.md")]
    for p in sorted(glob.glob(os.path.join(repo, ".claude", "skills", "*", "SKILL.md"))):
        ad = os.path.basename(os.path.dirname(p)); rel = os.path.relpath(p, repo)
        T.append(("T1 ritüel-skill" if ad in RITUEL else "T2 çağrı-skill", rel))
    T += [("T3 kanon-pointer", d) for d in CORE_KURAL if os.path.exists(os.path.join(repo, d))]
    T += [("T4 wiki", os.path.relpath(p, repo)) for p in sorted(glob.glob(os.path.join(repo, "wiki", "*.md"))) if os.path.basename(p) not in ("README.md", "sozluk.md")]
    return T


def main():
    ap = argparse.ArgumentParser(description="kural envanteri + deterministik kümeleme (İB-51)")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--sessiz", action="store_true"); ap.add_argument("--kuru", action="store_true")
    a = ap.parse_args(); repo = os.path.abspath(a.repo)
    m = yukle_sayac(repo)
    if m is None:
        print("HATA: tools/kural-sayaci.py yok (birim tanımı oradan alınır)", file=sys.stderr); return 2
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip() or "-"
    ts = datetime.now(timezone(timedelta(hours=3))).replace(microsecond=0).isoformat()
    kosum_id = "kural-envanter:%s:%s" % (head, ts[:10])
    satirlar, ozet = [], {}
    for tas, rel in tasiyicilar(repo):
        for ln, t, b in birimler(m, repo, rel):
            sn = [ad for ad, rx in RX if rx.search(t)] or ["genel"]
            satirlar.append({"tasiyici": tas, "dosya": rel, "satir": ln, "byte": b, "siniflar": "|".join(sn), "isaret": "madde" if m.MADDE.match(t) else ("kalın" if m.KALIN.match(t) else "işaret"),
                             "metin_kisa": t[:90]})
            for s in sn:
                k = (tas, s); o = ozet.setdefault(k, {"birim": 0, "byte": 0}); o["birim"] += 1; o["byte"] += b
    top_tas = {}
    for r in satirlar:
        o = top_tas.setdefault(r["tasiyici"], {"birim": 0, "byte": 0, "dosya": set()}); o["birim"] += 1; o["byte"] += r["byte"]; o["dosya"].add(r["dosya"])
    if not a.kuru:
        gd = os.path.join(repo, "veri", "gorunum"); os.makedirs(gd, exist_ok=True)
        with open(os.path.join(gd, "v_kural_envanter.csv"), "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["tasiyici", "dosya", "satir", "byte", "siniflar", "isaret", "metin_kisa"], lineterminator="\n"); w.writeheader(); w.writerows(satirlar)
        with open(os.path.join(gd, "v_kural_envanter_ozet.csv"), "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh, lineterminator="\n"); w.writerow(["tasiyici", "sinif", "birim", "byte"])
            for (tas, s), o in sorted(ozet.items()):
                w.writerow([tas, s, o["birim"], o["byte"]])
        with open(os.path.join(repo, "veri", "kural-envanter.jsonl"), "a", encoding="utf-8") as fh:
            for tas, o in sorted(top_tas.items()):
                fh.write(json.dumps({"ts": ts, "kod_sha": head, "kosum_id": kosum_id, "tasiyici": tas, "dosya_sayisi": len(o["dosya"]), "birim": o["birim"], "byte": o["byte"],
                                     "siniflar": {s: ozet[(tas, s)]["birim"] for (t2, s) in ozet if t2 == tas}}, ensure_ascii=False) + "\n")
    if not a.sessiz:
        print("kural-envanter @ %s · %d birim · %d taşıyıcı dosya" % (head, len(satirlar), sum(len(o["dosya"]) for o in top_tas.values())))
        for tas, o in sorted(top_tas.items()):
            print("  %-18s %4d birim · %7d byte · %2d dosya" % (tas, o["birim"], o["byte"], len(o["dosya"])))
        print("  sınıf (tüm taşıyıcılar):", " · ".join("%s %d" % (s, sum(o["birim"] for (t2, s2), o in ozet.items() if s2 == s)) for s, _ in SINIF + [("genel", None)]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
