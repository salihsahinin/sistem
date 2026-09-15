#!/usr/bin/env python3
"""Bağlam-uzayı → skill adayı madenciliği (deterministik; Salih emri 2026-09-15, Kun Chen L8 deseni:
"koşullu, her zaman gerekmeyen bilgi hafıza dosyasından skill'e taşınır — progressive disclosure").

Her md bölümü (## / ### başlık altı) için dört sinyal ölçülür, skor üretilir, rapor yazılır:
  K  koşulluluk   : koşul/tetik dili yoğunluğu (‰) — "ise, dediğinde, tetik, yalnız, kullan/kullanma, → , ∧ ∨"
  P  prosedür     : numaralı/adımlı liste uzunluğu (≥3 adım = prosedür)
  B  boyut        : bayt (her seans yüklenen katmanda maliyet = bayt × seans)
  O  okunma       : hareket tablosunda o dosyanın Read sayısı / toplam seans (düşük ⇒ nadiren gerekli)
Skor = B/1000 × (0,5 + K/50) × (1 + P/5) × (1 − O_norm)  — deneysel m.29; katsayılar kalibre edilmemiş [?].
Sıcak katman (her seans yüklenen) bölümleri "S" bayrağı alır: taşıma kazancı en yüksek orada.
Kanona yazmaz; rapor md üretir. Ölçüm, karar değil — aday listesi karar masasına gider (skill-kapisi K0'a giriş).

Kullanım: python3 tools/baglam-skill-aday.py [--cikti raporlar/...md] [--min-bayt 600]
"""
import argparse, re, pathlib, sqlite3, datetime

SICAK = {"CLAUDE.md", "core/durum-kapsulu.md", "core/pano.md", ".claude/skills/seans-acilis/SKILL.md",
         ".claude/skills/seans-kapanis/SKILL.md", "KILAVUZ.md"}
DOSYALAR = ["CLAUDE.md", "KILAVUZ.md"] + sorted(str(p) for p in pathlib.Path("core").glob("*.md")) \
           + sorted(str(p) for p in pathlib.Path("wiki").glob("*.md")) \
           + [".claude/skills/seans-acilis/SKILL.md", ".claude/skills/seans-kapanis/SKILL.md", "ogrenme/README.md"]
KOSUL = re.compile(r"\b(ise|dediğinde|olduğunda|tetik\w*|yalnız|kullan(ma|ılmaz|ıl)?\b|gerekirse|varsa|yoksa|önce|sonra|→|∧|∨|¬|KULLANMA|YASAK|zorunlu)\b", re.I)
ADIM = re.compile(r"^\s*(\d+[.)]|[-*]\s+\*\*\w)", re.M)

def bolumler(metin):
    parcalar = re.split(r"^(#{2,3} .+)$", metin, flags=re.M)
    out = []
    if parcalar[0].strip():
        out.append(("(başlıksız giriş)", parcalar[0]))
    for i in range(1, len(parcalar), 2):
        out.append((parcalar[i].strip("# ").strip(), parcalar[i + 1] if i + 1 < len(parcalar) else ""))
    return out

def okuma_sayaci():
    try:
        con = sqlite3.connect("veri/baglam.sqlite")
        seans = con.execute("select count(distinct oturum_kisa) from hareket").fetchone()[0] or 1
        rows = con.execute("select dosya, count(*) from hareket where arac='Read' and dosya is not null group by dosya").fetchall()
        return {d: n for d, n in rows}, seans
    except Exception:
        return {}, 1

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--cikti"); ap.add_argument("--min-bayt", type=int, default=600)
    a = ap.parse_args()
    okuma, seans = okuma_sayaci()
    adaylar = []
    for f in DOSYALAR:
        p = pathlib.Path(f)
        if not p.exists():
            continue
        metin = p.read_text(encoding="utf-8", errors="ignore")
        n_read = sum(n for d, n in okuma.items() if d and d.endswith(f))
        o_norm = min(1.0, n_read / max(seans, 1))
        for baslik, govde in bolumler(metin):
            b = len(govde.encode())
            if b < a.min_bayt:
                continue
            kelime = max(1, len(govde.split()))
            k = 1000 * len(KOSUL.findall(govde)) / kelime
            pr = len(ADIM.findall(govde))
            skor = (b / 1000) * (0.5 + k / 50) * (1 + pr / 5) * (1 - 0.8 * o_norm)
            adaylar.append((skor, f, baslik, b, round(k, 1), pr, n_read, f in SICAK))
    adaylar.sort(reverse=True)
    bugun = datetime.date.today().isoformat()
    out = [f"# Bağlam-uzayı → skill adayları ({bugun}; deneysel m.29, katsayılar kalibre edilmemiş [?])", "",
           f"*Üreten `tools/baglam-skill-aday.py` · {len(DOSYALAR)} dosya · bölüm ≥{a.min_bayt} B · seans sayısı (hareket) {seans}. "
           "Skor = boyut × koşulluluk × prosedür × (1 − okunma). S = her seans yüklenen sıcak katman (taşıma kazancı en yüksek). "
           "Bu liste ADAY listesidir; her aday `skill-kapisi` K0-K3 ağacından geçer (Kun Chen deseni: koşullu bilgi → skill; progressive disclosure).*", "",
           "| # | skor | S | dosya | bölüm | bayt | koşul ‰ | adım | Read n |", "|---|---|---|---|---|---|---|---|---|"]
    for i, (skor, f, baslik, b, k, pr, n, sicak) in enumerate(adaylar[:40], 1):
        out.append(f"| {i} | {skor:5.1f} | {'S' if sicak else ''} | `{f}` | {baslik[:60]} | {b} | {k} | {pr} | {n} |")
    top_s = sum(x[3] for x in adaylar if x[7])
    out += ["", f"Sıcak katman toplam aday bayt: {top_s} · aday sayısı {len(adaylar)} (ilk 40 gösterildi).", "",
            "## Okuma kuralı", "- Yüksek skor + S: her seans yüklenen ama koşullu/prosedürel içerik → skill'e taşıma adayı (bağlam tasarrufu = bayt × seans).",
            "- Yüksek skor, S değil, Read n düşük: zaten lazy; skill'e çevirmenin kazancı 'tetiklenebilirlik' (doğru anda otomatik yüklenme), bağlam değil.",
            "- Düşük koşul ‰ + yüksek bayt: durum/tarihçe bloğu → skill değil, damıtma/arşiv adayı (m.8, İB-81 hattı)."]
    metin = "\n".join(out) + "\n"
    if a.cikti:
        pathlib.Path(a.cikti).write_text(metin, encoding="utf-8"); print(f"yazıldı: {a.cikti} · aday {len(adaylar)}")
    else:
        print(metin)

if __name__ == "__main__":
    main()
