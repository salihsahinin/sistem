#!/usr/bin/env python3
"""katman-hatti.py — silver/gold katmanını BRONZ'dan uçtan uca YENİDEN üretir (sabit sıra; STDLIB ONLY).

Neden: `baglam-tablo.py` veri/baglam.sqlite'ı tmp→replace ile SIFIRDAN yazar → sonradan eklenen silver tabloları (karar_borcu, prompt…)
kaybolur. Çözüm: her türetilmiş tablo kendi BRONZ kaynağından deterministik yeniden yüklenir (functional data engineering: saf/idempotent
görev + iki damga kod SHA + girdi SHA — cc/rapor-2026-08-16-2.md B3-1). Sıra sözleşmedir; yeni yükleyici bu listeye EKLENİR (additive).

Sıra: 1) baglam-tablo.py (silver çekirdek + gold görünümler) → 2) karar-borcu-tablo.py (silver karar_borcu; bronz veri/karar-borcu.jsonl)
      → 3) prompt-tablo.py (bronz veri/bronz/prompt-olay.jsonl ← transkript; silver prompt; gold v_son_50_prompt)
      → 4) ambar-tablo.py (bronz veri/bronz/kosum-olay.jsonl ← alt-ajan transkriptleri; ambar amb_* tabloları/görünümleri; martlar v_amb_*)
      → 5) katman-olcum.py (ölçüm/test/sözleşme/freshness → veri/katman-olcum.jsonl append-only).
      → OPSİYONEL (bayrak --parquet; varsayılan KAPALI — KB-55 Salih hükmüne dek): ambar-parquet.py (silver/ambar → veri/parquet/*.parquet
        kolon-bazlı türev; DuckDB ister, yoksa çıkış 4 = "atlandı" sayılır, hat düşmez) → kolon-olcum.py (satır↔kolon ölçüm kütüğü).
Kullanım: python3 tools/katman-hatti.py [--repo <yol>] [--atla baglam,karar,prompt,ambar,hareket,olcum,parquet,kolon-olcum]
          [--snapshot YYYY-MM-DD] [--parquet]
Çıkış: ilk FAIL-LOUD adımın kodu (0 = tümü tamam); 2 = bilinmeyen --atla adı (stderr'de listelenir, hiçbir adım koşmaz; FAIL-LOUD); adım durumu
`adim_durumu()` ile karara bağlanır (0 → OK; ATLANDI_KODLARI'ndaki kod → ATLANDI, hat düşmez; diğer → KOD n, hat düşer). --atla ile çıkarılan
(bilinen) adımlar döngü öncesi `[atla ] <ad>` satırıyla yankılanır. Deneysel m.29 (2026-08-16, seans-7).
"""
import argparse, os, subprocess, sys, time

ADIMLAR = [
    ("baglam", ["tools/baglam-tablo.py", "--sessiz"]),
    ("karar", ["tools/karar-borcu-tablo.py", "--sessiz"]),
    ("prompt", ["tools/prompt-tablo.py", "--sessiz"]),
    ("ambar", ["tools/ambar-tablo.py", "--sessiz"]),
    ("hareket", ["tools/hareket-tablo.py", "--sessiz"]),
    ("olcum", ["tools/katman-olcum.py"]),
]
# Opsiyonel kolon katmanı (pipeline kolon-katmani SH-1/SH-2; kanon kısıtı Beyan 9 "ölçüm tetikli" → varsayılan kapalı)
PARQUET_ADIMLAR = [
    ("parquet", ["tools/ambar-parquet.py", "--sessiz"]),
    ("kolon-olcum", ["tools/kolon-olcum.py", "--sessiz"]),
]
ATLANDI_KODLARI = {"parquet": {4}}  # duckdb yoksa ambar-parquet 4 döner → hat düşmez, "atlandı" sayılır


def atla_sec(secim):
    """--atla virgüllü listesi → (bilinen adım adları, bilinmeyen adlar); virgül çevresi boşluk kırpılır. Bilinmeyen ad sessizce
    'atlandı' sayılmaz — çağıran stderr'e listeler ve çıkış 2 verir (FAIL-LOUD; --tablo/--sorgu ile aynı kural)."""
    adlar = [x.strip() for x in secim.split(",") if x.strip()]
    bilinen = {ad for ad, _ in ADIMLAR + PARQUET_ADIMLAR}
    return [x for x in adlar if x in bilinen], [x for x in adlar if x not in bilinen]


def adimlari_sec(parquet=False, atla=()):
    """Koşulacak adım listesi (ad, komut): temel hat + (parquet bayrağıyla) kolon katmanı; --atla adları çıkarılır."""
    atla = set(atla)
    secili = list(ADIMLAR) + (list(PARQUET_ADIMLAR) if parquet else [])
    return [(ad, cmd) for ad, cmd in secili if ad not in atla]


def adim_durumu(ad, returncode):
    """Adım çıkış kodu → (durum etiketi, hat düşer mi). 0 → ('OK', False); ATLANDI_KODLARI[ad] içindeki kod → ('ATLANDI', False)
    (ör. parquet 4 = duckdb/eklenti yok, opsiyonel katman atlanır); diğer her kod → ('KOD n', True) = FAIL-LOUD, hat çıkış kodu olur."""
    if returncode == 0:
        return "OK", False
    if returncode in ATLANDI_KODLARI.get(ad, set()):
        return "ATLANDI", False
    return "KOD %d" % returncode, True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--atla", default="", help="virgüllü adım adları (%s)" % ",".join(ad for ad, _ in ADIMLAR + PARQUET_ADIMLAR))
    ap.add_argument("--snapshot", default=None, help="karar-borcu-tablo/olcum için tarih (determinizm)")
    ap.add_argument("--parquet", action="store_true", help="opsiyonel kolon katmanı: ambar-parquet + kolon-olcum (DuckDB gerekir)")
    a = ap.parse_args(); repo = os.path.abspath(a.repo)
    atla, bilinmeyen = atla_sec(a.atla)
    if bilinmeyen:
        print("HATA: bilinmeyen --atla adı: %s · geçerli adlar: %s" % (", ".join(bilinmeyen), ",".join(ad for ad, _ in ADIMLAR + PARQUET_ADIMLAR)),
              file=sys.stderr)
        sys.exit(2)
    for ad in atla:
        print(f"[atla ] {ad}")
    kod = 0
    for ad, cmd in adimlari_sec(parquet=a.parquet, atla=atla):
        args = list(cmd)
        if a.snapshot and ad in ("karar",): args += ["--snapshot", a.snapshot]
        if a.snapshot and ad == "olcum": args += ["--simdi", a.snapshot + "T00:00:00"]
        t0 = time.time()
        r = subprocess.run([sys.executable] + args, cwd=repo, capture_output=True, text=True)
        dt = time.time() - t0
        durum, duser = adim_durumu(ad, r.returncode)
        print(f"[{durum:7}] {ad:11} {dt:5.1f}s  {' '.join(args)}")
        if r.stdout.strip() and (r.returncode != 0 or ad == "olcum"):
            print("        " + r.stdout.strip().replace("\n", "\n        ")[:2000])
        if r.returncode != 0:
            print("        STDERR: " + r.stderr.strip()[-600:])
            if duser:
                kod = kod or r.returncode
            if ad in ("baglam",):  # çekirdek düşerse aşağısı anlamsız
                break
    sys.exit(kod)


if __name__ == "__main__":
    main()
