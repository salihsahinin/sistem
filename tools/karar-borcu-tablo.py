#!/usr/bin/env python3
"""karar-borcu-tablo.py — açık karar-borcu envanterini (veri/karar-borcu.jsonl) makine-okur tabloya yükler.

Grain bildirimi (world-model §2 kuralı): 1 satır = 1 AÇIK KARAR KALEMİ (Salih hükmü ya da Jarvis icrası bekleyen);
kapanınca `karar` sürecine (1 satır = 1 hüküm) akar — bu tablo hükmün ÖN-DURUMUdur.
Boyutlar: zaman (kayit_tarihi/snapshot) · dosya (kaynak pointer → baglam `dosya`/`kayit`) · katman (1/2) · anahtar (kume/tur).

Yaptıkları (STDLIB ONLY, deterministik):
  1. veri/karar-borcu.jsonl okur, şema doğrular (zorunlu alanlar; enum'lar).
  2. Her kaynak pointer'ı (dosya:satır) DİSKTE doğrular: dosya var mı, satır var mı, satır metnini alır (topraklama — F1 destek-kontrolü;
     "DAYANAKSIZ ≠ YANLIŞ": bulunamayan pointer FAIL-LOUD listelenir, sessiz düşmez).
  3. baglam.sqlite varsa `kayit` tablosuna (dosya_id + satır aralığı) bağlar → kayit_id (conformed dosya boyutu).
  4. Tabloları yazar: `karar_borcu` + `karar_borcu_kaynak` (baglam.sqlite içine; yoksa veri/karar-borcu.sqlite) + görünüm
     `v_karar_borcu_ozet` + CSV `veri/gorunum/v_karar_borcu.csv` (izlenen, küçük).
Kullanım: python3 tools/karar-borcu-tablo.py [--repo <yol>] [--girdi veri/karar-borcu.jsonl] [--sessiz] [--kuru]
Çıkış kodu: 0 tamam · 2 girdi/şema hatası · 3 kırık pointer var (tablo yine yazılır, kırıklar raporlanır).
Deneysel m.29 (2026-08-16, Jarvis). Additive-only: alan silinmez/yeniden adlandırılmaz.
"""
import argparse, csv, json, os, sqlite3, subprocess, sys
from datetime import date

ZORUNLU = ["borc_id", "baslik", "kume", "tur", "katman", "karar_sahibi", "durum", "kayit_tarihi", "kaynak"]
TUR = {"Katman-1-kural", "silme-birlestirme", "yon-degisimi", "serh-damga", "kapanis-hukmu", "para-dis", "rol",
       "deger-tercihi", "olcek-pilot", "icra-borcu", "ingest-borcu", "kalibrasyon-borcu"}
DURUM = {"İMZASIZ", "BEKLET", "Salih'te", "masaya", "kısmen-kapandı", "kapandı", "belirsiz", "icra-sırada"}
SAHIP = {"Salih", "Jarvis", "Salih+Jarvis"}


def git_head(repo):
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "?"


def oku_jsonl(yol):
    satirlar = []
    with open(yol, encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                satirlar.append(json.loads(line))
            except json.JSONDecodeError as e:
                sys.exit(f"[HATA] {yol}:{i} JSON çözülemedi: {e}")
    return satirlar


DURUM_ESANLAM = {"masada": "masaya", "Salihte": "Salih'te", "kapandi": "kapandı", "icra-sirada": "icra-sırada"}  # yazım varyantı → tek enum (08-22: KB-59/60/61 "masada" hat kırdı)


def dogrula(kayitlar):
    hatalar, ids = [], set()
    for k in kayitlar:
        if k.get("durum") in DURUM_ESANLAM:
            print("[UYARI] %s: durum '%s' → '%s' (eşanlam normalize; kaynağı düzelt)" % (k.get("borc_id"), k["durum"], DURUM_ESANLAM[k["durum"]]), file=sys.stderr)
            k["durum"] = DURUM_ESANLAM[k["durum"]]
        for alan in ZORUNLU:
            if alan not in k or k[alan] in (None, "", []):
                hatalar.append(f"{k.get('borc_id','?')}: zorunlu alan eksik → {alan}")
        if k.get("borc_id") in ids:
            hatalar.append(f"{k['borc_id']}: mükerrer borc_id")
        ids.add(k.get("borc_id"))
        if k.get("tur") not in TUR:
            hatalar.append(f"{k.get('borc_id')}: tur enum-dışı → {k.get('tur')}")
        if k.get("durum") not in DURUM:
            hatalar.append(f"{k.get('borc_id')}: durum enum-dışı → {k.get('durum')}")
        if k.get("karar_sahibi") not in SAHIP:
            hatalar.append(f"{k.get('borc_id')}: karar_sahibi enum-dışı → {k.get('karar_sahibi')}")
        if str(k.get("katman")) not in {"1", "2"}:
            hatalar.append(f"{k.get('borc_id')}: katman 1|2 olmalı → {k.get('katman')}")
        if not isinstance(k.get("kaynak"), list):
            hatalar.append(f"{k.get('borc_id')}: kaynak liste olmalı")
    return hatalar


_dosya_onbellek = {}


def dosya_satirlari(repo, rel):
    if rel not in _dosya_onbellek:
        yol = os.path.join(repo, rel)
        try:
            with open(yol, encoding="utf-8", errors="replace") as fh:
                _dosya_onbellek[rel] = fh.read().split("\n")
        except OSError:
            _dosya_onbellek[rel] = None
    return _dosya_onbellek[rel]


def pointer_coz(repo, ptr):
    """'dosya:satır' → (dosya, satır|None, dosya_var, satir_var, metin).
    Ek (08-22): 'dosya:satır (açıklama)' / 'dosya §2 G1' / 'dosya Karar 66' gibi AÇIKLAMA KUYRUKLU pointer'larda ilk boşluğa kadarki parça
    yol olarak denenir (LLM-yazımı kaynak satırları; kanon biçim yine 'dosya:satır'). Dosya gerçekten yoksa FAIL-LOUD aynen kalır."""
    ptr = ptr.strip()
    if " " in ptr:
        bas = ptr.split(" ", 1)[0].rstrip(",;")
        adayi = bas.rsplit(":", 1)[0] if (":" in bas and bas.rsplit(":", 1)[1].isdigit()) else bas
        if os.path.exists(os.path.join(repo, adayi)):
            ptr = bas
    if ":" in ptr and ptr.rsplit(":", 1)[1].isdigit():
        dosya, satir = ptr.rsplit(":", 1)
        satir = int(satir)
    else:
        dosya, satir = ptr, None
    satirlar = dosya_satirlari(repo, dosya)
    if satirlar is None:
        return dosya, satir, 0, 0, ""
    if satir is None:
        return dosya, None, 1, 1, ""
    if 1 <= satir <= len(satirlar):
        return dosya, satir, 1, 1, satirlar[satir - 1][:240]
    return dosya, satir, 1, 0, ""


def kayit_id_bul(con, dosya, satir):
    if con is None or satir is None:
        return None
    try:
        r = con.execute("SELECT kayit_id FROM kayit WHERE dosya_id=? AND satir_bas<=? AND satir_son>=? ORDER BY sira LIMIT 1",
                        (dosya, satir, satir)).fetchone()
        return r[0] if r else None
    except sqlite3.Error:
        return None


def yas_gun(kayit_tarihi, snapshot):
    try:
        y, m, d = (int(x) for x in kayit_tarihi[:10].split("-"))
        return (snapshot - date(y, m, d)).days
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--girdi", default="veri/karar-borcu.jsonl")
    ap.add_argument("--snapshot", default=None, help="YYYY-MM-DD (varsayılan: bugün — determinizm için açık ver)")
    ap.add_argument("--sessiz", action="store_true")
    ap.add_argument("--kuru", action="store_true", help="yalnız doğrula, yazma")
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)
    girdi = os.path.join(repo, a.girdi)
    if not os.path.exists(girdi):
        sys.exit(f"[HATA] girdi yok: {girdi}")
    snapshot = date.fromisoformat(a.snapshot) if a.snapshot else date.today()
    sha = git_head(repo)

    kayitlar = oku_jsonl(girdi)
    hatalar = dogrula(kayitlar)
    if hatalar:
        print("[ŞEMA HATASI] " + "\n[ŞEMA HATASI] ".join(hatalar))
        sys.exit(2)

    db_yol = os.path.join(repo, "veri", "baglam.sqlite")
    ayri = not os.path.exists(db_yol)
    if ayri:
        db_yol = os.path.join(repo, "veri", "karar-borcu.sqlite")
    con = None if a.kuru else sqlite3.connect(db_yol)
    okur = sqlite3.connect(os.path.join(repo, "veri", "baglam.sqlite")) if not ayri else None

    kaynak_satirlari, kirik = [], []
    for k in kayitlar:
        for i, ptr in enumerate(k["kaynak"], 1):
            dosya, satir, dv, sv, metin = pointer_coz(repo, ptr)
            kid = kayit_id_bul(okur, dosya, satir)
            kaynak_satirlari.append((k["borc_id"], i, dosya, satir, metin, dv, sv, kid))
            if not (dv and sv):
                kirik.append(f"{k['borc_id']} → {ptr} ({'dosya yok' if not dv else 'satır yok'})")

    if not a.kuru:
        con.executescript("""
        CREATE TABLE IF NOT EXISTS karar_borcu (
          borc_id TEXT PRIMARY KEY, baslik TEXT, kume TEXT, tur TEXT, katman INTEGER, karar_sahibi TEXT, durum TEXT,
          kayit_tarihi TEXT, yas_gun INTEGER, secenekler TEXT, oneri TEXT, bagimlilik TEXT, kapanis_kaniti TEXT,
          masa_sirasi INTEGER, yururluk_aninda TEXT, icra_borcu TEXT, not_ TEXT, kaynak_sayisi INTEGER,
          snapshot_tarih TEXT, snapshot_sha TEXT
        );
        CREATE TABLE IF NOT EXISTS karar_borcu_kaynak (
          borc_id TEXT, sira INTEGER, dosya_id TEXT, satir INTEGER, satir_metin TEXT,
          dosya_var INTEGER, satir_var INTEGER, kayit_id TEXT
        );
        DELETE FROM karar_borcu; DELETE FROM karar_borcu_kaynak;
        CREATE VIEW IF NOT EXISTS v_karar_borcu_ozet AS
          SELECT kume, katman, karar_sahibi, durum, COUNT(*) AS n, MIN(kayit_tarihi) AS en_eski, MAX(yas_gun) AS en_yasli_gun
          FROM karar_borcu GROUP BY kume, katman, karar_sahibi, durum ORDER BY katman, kume, n DESC;
        """)
        for k in kayitlar:
            con.execute("INSERT INTO karar_borcu VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                k["borc_id"], k["baslik"], k["kume"], k["tur"], int(k["katman"]), k["karar_sahibi"], k["durum"],
                k["kayit_tarihi"], yas_gun(k["kayit_tarihi"], snapshot), k.get("secenekler", ""), k.get("oneri", ""),
                json.dumps(k.get("bagimlilik", []), ensure_ascii=False) if isinstance(k.get("bagimlilik"), list) else k.get("bagimlilik", ""),
                k.get("kapanis_kaniti", ""), k.get("masa_sirasi"), k.get("yururluk_aninda", ""), k.get("icra_borcu", ""),
                k.get("not", ""), len(k["kaynak"]), snapshot.isoformat(), sha))
        con.executemany("INSERT INTO karar_borcu_kaynak VALUES (?,?,?,?,?,?,?,?)", kaynak_satirlari)
        con.commit()
        # CSV görünüm (izlenen, küçük)
        gdir = os.path.join(repo, "veri", "gorunum")
        os.makedirs(gdir, exist_ok=True)
        with open(os.path.join(gdir, "v_karar_borcu.csv"), "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["borc_id", "kume", "katman", "karar_sahibi", "durum", "tur", "kayit_tarihi", "yas_gun", "masa_sirasi",
                        "yururluk_aninda", "baslik", "kaynak", "bagimlilik", "kapanis_kaniti"])
            for k in sorted(kayitlar, key=lambda x: (int(x["katman"]), x.get("masa_sirasi") or 999, x["borc_id"])):
                w.writerow([k["borc_id"], k["kume"], k["katman"], k["karar_sahibi"], k["durum"], k["tur"], k["kayit_tarihi"],
                            yas_gun(k["kayit_tarihi"], snapshot), k.get("masa_sirasi", ""), k.get("yururluk_aninda", ""), k["baslik"],
                            " | ".join(k["kaynak"]), " ".join(k.get("bagimlilik", [])) if isinstance(k.get("bagimlilik"), list) else k.get("bagimlilik", ""),
                            k.get("kapanis_kaniti", "")])
        con.close()

    if not a.sessiz:
        n1 = sum(1 for k in kayitlar if str(k["katman"]) == "1")
        print(f"karar-borcu: {len(kayitlar)} kalem (Katman-1 {n1} · Katman-2 {len(kayitlar)-n1}) · kaynak pointer {len(kaynak_satirlari)} · kırık {len(kirik)} · snapshot {snapshot} @ {sha} · db {'(kuru)' if a.kuru else os.path.relpath(db_yol, repo)}")
        for s in kirik:
            print("  [KIRIK POINTER] " + s)
    sys.exit(3 if kirik else 0)


if __name__ == "__main__":
    main()
