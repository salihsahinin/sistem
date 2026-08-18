#!/usr/bin/env python3
"""katman-hatti.py — silver/gold katmanını BRONZ'dan uçtan uca YENİDEN üretir (sabit sıra; STDLIB ONLY).

Neden: `baglam-tablo.py` veri/baglam.sqlite'ı tmp→replace ile SIFIRDAN yazar → sonradan eklenen silver tabloları (karar_borcu, prompt…)
kaybolur. Çözüm: her türetilmiş tablo kendi BRONZ kaynağından deterministik yeniden yüklenir (functional data engineering: saf/idempotent
görev + iki damga kod SHA + girdi SHA — cc/rapor-2026-08-16-2.md B3-1). Sıra sözleşmedir; yeni yükleyici bu listeye EKLENİR (additive).

Sıra: 1) baglam-tablo.py (silver çekirdek + gold görünümler) → 2) karar-borcu-tablo.py (silver karar_borcu; bronz veri/karar-borcu.jsonl)
      → 3) prompt-tablo.py (bronz veri/bronz/prompt-olay.jsonl ← transkript; silver prompt; gold v_son_50_prompt)
      → 4) ambar-tablo.py (bronz veri/bronz/kosum-olay.jsonl ← alt-ajan transkriptleri; ambar amb_* tabloları/görünümleri; martlar v_amb_*)
      → 5) katman-olcum.py (ölçüm/test/sözleşme/freshness → veri/katman-olcum.jsonl append-only)
      → 6) tarama-plan.py (tarama-yöntemi plan-regresyon testi: EQP sınıfı ↔ beklenti; salt-okur, kaynak DB değişmez → veri/tarama-plan.jsonl; uyarı modu — ihlal hat düşürmez, KB-58;
           uyarıları stderr'e yazar → hat bunları çıkış 0'da da yankılar, yoksa ihlal yalnız kütükte kalırdı).
Kullanım: python3 tools/katman-hatti.py [--repo <yol>] [--atla baglam,karar,prompt,ambar,hareket,olcum,tarama] [--snapshot YYYY-MM-DD]
Çıkış: ilk FAIL-LOUD adımın kodu (0 = tümü tamam). Deneysel m.29 (2026-08-16, seans-7).
"""
import argparse, os, subprocess, sys, time

ADIMLAR = [
    ("baglam", ["tools/baglam-tablo.py", "--sessiz"]),
    ("karar", ["tools/karar-borcu-tablo.py", "--sessiz"]),
    ("prompt", ["tools/prompt-tablo.py", "--sessiz"]),
    ("ambar", ["tools/ambar-tablo.py", "--sessiz"]),
    ("hareket", ["tools/hareket-tablo.py", "--sessiz"]),
    ("olcum", ["tools/katman-olcum.py"]),
    ("tarama", ["tools/tarama-plan.py", "--sessiz"]),  # tarama-yöntemi plan-regresyon testi (uyarı modu; salt-okur, ~1 sn; KB-53 İB-25 / KB-58)
]
UYARI_KANALI_ADIMLAR = {"tarama"}  # çıkış 0'da bile stderr'i uyarı kanalı olan adımlar (UYARI/BEKLENTİ DIŞI/HATA satırları hatta görünür)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--atla", default="", help="virgüllü adım adları (baglam,karar,prompt,ambar,hareket,olcum,tarama)")
    ap.add_argument("--snapshot", default=None, help="karar-borcu-tablo/olcum için tarih (determinizm)")
    a = ap.parse_args(); repo = os.path.abspath(a.repo); atla = set(x for x in a.atla.split(",") if x)
    kod = 0
    for ad, cmd in ADIMLAR:
        if ad in atla:
            print(f"[atla ] {ad}"); continue
        args = list(cmd)
        if a.snapshot and ad in ("karar",): args += ["--snapshot", a.snapshot]
        if a.snapshot and ad == "olcum": args += ["--simdi", a.snapshot + "T00:00:00"]
        t0 = time.time()
        r = subprocess.run([sys.executable] + args, cwd=repo, capture_output=True, text=True)
        dt = time.time() - t0
        durum = "OK" if r.returncode == 0 else f"KOD {r.returncode}"
        print(f"[{durum:6}] {ad:7} {dt:5.1f}s  {' '.join(args)}")
        if r.stdout.strip() and (r.returncode != 0 or ad == "olcum"):
            print("        " + r.stdout.strip().replace("\n", "\n        ")[:2000])
        if r.returncode != 0 or (ad in UYARI_KANALI_ADIMLAR and r.stderr.strip()):
            print("        STDERR: " + r.stderr.strip()[-600:])
        if r.returncode != 0:
            kod = kod or r.returncode
            if ad in ("baglam",):  # çekirdek düşerse aşağısı anlamsız
                break
    sys.exit(kod)


if __name__ == "__main__":
    main()
