#!/usr/bin/env python3
"""pointer-kayma.py — damıtma/yeniden-yazım sonrası `dosya:satır` pointer'larının SESSİZ KAYMASINI yakalar.

Sorun (08-29 vakası, Karar 74 M-3 damıtması): satır numaraları kayınca `karar-borcu-tablo.py` yalnız DOSYA-SONU-DIŞI
pointer'ları kırık sayar (10 kırık); dosya içinde kalan ama BAŞKA içeriğe düşen pointer'lar sessiz geçer (2 kayma:
KB-36 kutu:29 V13→V38 · KB-38 defter:156 Karar 48→Karar 65). Bu script iki git durumunu satır-metni düzeyinde kıyaslar.

Yaptıkları (STDLIB ONLY, deterministik):
  1. `veri/karar-borcu.jsonl` (ya da --girdi) içindeki her `dosya:satır` pointer'ını okur (açıklama-kuyruklu biçim dahil).
  2. Satır metnini ESKİ ref'te (`git show <ref>:<dosya>`) ve ÇALIŞMA AĞACINDA alır; farklıysa KAYMIŞ, yeni dosyada satır yoksa KIRIK.
  3. Öneri: eski satırın ilk 60 karakterini yeni dosyada ve `arsiv/kuyruk-arsiv/*.md` içinde arar; TEK eşleşme varsa `→ dosya:satır` yazar
     (birden çoksa listeler, sıfırsa "ARANAMADI" — karar insana/Jarvis'e kalır, script yazmaz).
Kullanım: python3 tools/pointer-kayma.py --ref <damıtma-öncesi-sha> [--girdi veri/karar-borcu.jsonl] [--dosya a.md,b.md]
  --ref varsayılan HEAD (çalışma ağacı ↔ son commit). Damıtma SOP: tur commit'inden ÖNCE koş (ref=HEAD), ya da sonra ref=önceki sha.
  ŞART: girdi (pointer dosyası) ref'ten YENİ olmamalı — yeniden-pointer'lanmış girdiyi eski ref'le kıyaslamak sahte KAYMIŞ üretir
  (08-29 testi: düzeltilmiş jsonl ↔ 753e3a1 → 4 sahte; aynı jsonl ↔ HEAD → 0). Sonradan kıyas: `--girdi <(git show <sha>:veri/karar-borcu.jsonl)`.
Çıkış kodu: 0 temiz · 3 kayma/kırık var. Yazmaz; yalnız raporlar (yeniden-pointer kararı ayrı adım, m.8 arşiv-pointer).
Deneysel m.29 (2026-08-29, Jarvis, yan icra oturumu). Kayıt: tools/SCRIPTLER.md.
"""
import argparse, glob, json, os, subprocess, sys

ONEK = 60  # öneri araması için eski satırın karşılaştırılan ön-eki (karakter)


def git_satirlar(repo, ref, dosya):
    r = subprocess.run(["git", "show", f"{ref}:{dosya}"], cwd=repo, capture_output=True, text=True)
    return r.stdout.split("\n") if r.returncode == 0 else None


_yeni = {}


def yeni_satirlar(repo, dosya):
    if dosya not in _yeni:
        yol = os.path.join(repo, dosya)
        try:
            with open(yol, encoding="utf-8", errors="replace") as fh:
                _yeni[dosya] = fh.read().split("\n")
        except OSError:
            _yeni[dosya] = None
    return _yeni[dosya]


def pointer_ayir(ptr):
    """'dosya:satır [açıklama]' → (dosya, satır) | None — karar-borcu-tablo.py pointer_coz ile aynı kabul."""
    bas = ptr.strip().split(" ", 1)[0].rstrip(",;")
    if ":" in bas and bas.rsplit(":", 1)[1].isdigit():
        d, s = bas.rsplit(":", 1)
        return d, int(s)
    return None


def oneri_bul(repo, eski_metin, dosya):
    onek = eski_metin.strip()[:ONEK]
    if len(onek) < 20:
        return "ARANAMADI (ön-ek kısa)"
    adaylar = [dosya] + sorted(glob.glob(os.path.join(repo, "arsiv", "kuyruk-arsiv", "*.md")))
    bulunan = []
    for a in adaylar:
        rel = os.path.relpath(a, repo) if os.path.isabs(a) else a
        satirlar = yeni_satirlar(repo, rel)
        if not satirlar:
            continue
        for i, s in enumerate(satirlar, 1):
            if s.strip().startswith(onek):
                bulunan.append(f"{rel}:{i}")
    if not bulunan:
        return "ARANAMADI"
    return "→ " + bulunan[0] if len(bulunan) == 1 else "ÇOKLU " + " | ".join(bulunan[:4])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--girdi", default="veri/karar-borcu.jsonl")
    ap.add_argument("--ref", default="HEAD")
    ap.add_argument("--dosya", default="", help="virgüllü süzgeç; boş = tüm dosyalar")
    a = ap.parse_args()
    suzgec = {d.strip() for d in a.dosya.split(",") if d.strip()}
    eski = {}
    sorun = []
    toplam = 0
    with open(os.path.join(a.repo, a.girdi), encoding="utf-8") as fh:
        for raw in fh:
            raw = raw.strip()
            if not raw or raw.startswith("#"):
                continue
            k = json.loads(raw)
            for i, p in enumerate(k.get("kaynak", []), 1):
                ay = pointer_ayir(p)
                if not ay:
                    continue
                d, s = ay
                if suzgec and d not in suzgec:
                    continue
                toplam += 1
                if d not in eski:
                    eski[d] = git_satirlar(a.repo, a.ref, d)
                es, ys = eski[d], yeni_satirlar(a.repo, d)
                em = es[s - 1] if es and s <= len(es) else None
                ym = ys[s - 1] if ys and s <= len(ys) else None
                if em is None or em == ym:
                    continue  # ref'te dosya/satır yok = pointer ref'ten SONRA yazılmış (kayma değil) · eşitse temiz
                durum = "KIRIK" if ym is None else "KAYMIŞ"
                oneri = oneri_bul(a.repo, em, d) if em else "ARANAMADI (eski metin yok)"
                sorun.append((k["borc_id"], i, d, s, durum, (em or "")[:90], oneri))
    print(f"pointer-kayma: ref {a.ref} ↔ çalışma ağacı · pointer {toplam} · sorun {len(sorun)} "
          f"(KAYMIŞ {sum(1 for x in sorun if x[4]=='KAYMIŞ')} · KIRIK {sum(1 for x in sorun if x[4]=='KIRIK')})")
    for b, i, d, s, durum, em, on in sorun:
        print(f"  [{durum}] {b} #{i} {d}:{s}\n      eski: {em}\n      öneri: {on}")
    sys.exit(3 if sorun else 0)


if __name__ == "__main__":
    main()
