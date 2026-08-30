#!/usr/bin/env python3
"""katman-hatti.py — silver/gold katmanını BRONZ'dan uçtan uca YENİDEN üretir (sabit sıra; hat + temel adımlar STDLIB ONLY;
yalnız opsiyonel --parquet adımları `duckdb` ister).

Neden: `baglam-tablo.py` veri/baglam.sqlite'ı tmp→replace ile SIFIRDAN yazar → sonradan eklenen silver tabloları (karar_borcu, prompt…)
kaybolur. Çözüm: her türetilmiş tablo kendi BRONZ kaynağından deterministik yeniden yüklenir (functional data engineering: saf/idempotent
görev + iki damga kod SHA + girdi SHA — cc/rapor-2026-08-16-2.md B3-1). Sıra sözleşmedir; yeni yükleyici bu listeye EKLENİR (additive).

Sıra: 1) baglam-tablo.py (silver çekirdek + gold görünümler) → 2) karar-borcu-tablo.py (silver karar_borcu; bronz veri/karar-borcu.jsonl)
      → 3) prompt-tablo.py (bronz veri/bronz/prompt-olay.jsonl ← transkript; silver prompt; gold v_son_50_prompt)
      → 4) ambar-tablo.py (bronz veri/bronz/kosum-olay.jsonl ← alt-ajan transkriptleri; ambar amb_* tabloları/görünümleri; martlar v_amb_*)
      → 4b) deneyim-tablo.py (ambar koşum olguları → silver deneyim [model-kuşağı zorunlu] + v_deneyim_ozet/cift + deneyim_fts; KB-44 (a) İB-44)
      → 5) hareket-tablo.py (bronz veri/bronz/hareket-olay.jsonl ← transkript araç çağrıları; silver hareket; gold v_hareket_gunluk/v_son_hareketler
           + raporlar/hareket-gunlugu-*.md)
      → 5b) baglam-seyir.py (transkript usage → bronz baglam-olay.jsonl; silver baglam_olay; gold v_baglam_seyri/v_baglam_gunluk — KB-50/52 (a) İB-22; uyarı kanalı)
      → 6) tarama-plan.py (tarama-yöntemi plan-regresyon testi: EQP sınıfı ↔ beklenti; salt-okur, kaynak DB değişmez → veri/tarama-plan.jsonl; uyarı modu — ihlal hat düşürmez, KB-58;
           uyarıları stderr'e yazar → hat bunları çıkış 0'da da yankılar; olcum'dan ÖNCE koşar ki son adım kanonda kalsın)
      → 7) silver-saglik.py (Karar 58: anahtar_kaydi JOIN · kayit.gecerlilik bayrakları · T-Ç/T-B/T-A · v_guncel_* · silver_kuyruk; uyarı kanalı, hat düşürmez; --kapi yalnız ritüellerde)
      → 7a) erisim-fts.py (FTS5 kayit_fts + erisim_genisletme; İB-20 eval 4 yöntem → veri/erisim-eval.jsonl + v_erisim_eval; KB-43 (a) İB-43)
      → 7b) hat-içi HİJYEN (ANALYZE + PRAGMA optimize → sqlite_stat1; KB-53 (a) İB-26; yükleyici değil, --atla hijyen ile atlanır)
      → 8) katman-olcum.py (ölçüm/test/sözleşme/freshness → veri/katman-olcum.jsonl append-only) — SON ADIM (kanon core/veri-muhendisligi-katmani.md §8 S3, Salih A 08-17).
      → VARSAYILAN AÇIK (Karar 83 B2, Salih imzası 08-30 — İB-33 k=3 ölçümüyle Karar 63 şartı doldu; şerh: soğuk ayak purge'süz): ambar-parquet.py
        (silver/ambar → veri/parquet/*.parquet kolon-bazlı türev; DuckDB ister, yoksa çıkış 4 = "atlandı" sayılır, hat düşmez) → kolon-olcum.py
        (satır↔kolon ölçüm kütüğü). Kapatma: --parquet-yok.
KİRA (Karar 83 A2, PK-5/PK-7): eşzamanlı iki katman-hatti koşumu son-yazan-kazanır riskini taşır → veri/.kira-katman-hatti.json adlandırılmış
kirası alınır (TTL 600 sn m.29, pilotta kalibre; ölü-sahip süpürülür, sahip="salih" kirası ASLA süpürülmez); 60 sn içinde alınamazsa çıkış 5.
Kullanım: python3 tools/katman-hatti.py [--repo <yol>] [--atla baglam,karar,prompt,ambar,deneyim,hareket,seyir,tarama,saglik,erisim,hijyen,olcum,parquet,kolon-olcum]
          [--snapshot YYYY-MM-DD] [--parquet-yok]
Çıkış: ilk FAIL-LOUD adımın kodu (0 = tümü tamam); 5 = kira alınamadı (60 sn bekleme sonrası); 2 = bilinmeyen --atla adı (stderr'de listelenir, hiçbir adım koşmaz; FAIL-LOUD); adım durumu
`adim_durumu()` ile karara bağlanır (0 → OK; ATLANDI_KODLARI'ndaki kod → ATLANDI, hat düşmez; diğer → KOD n, hat düşer). --atla ile çıkarılan
(bilinen) adımlar döngü öncesi `[atla ] <ad>` satırıyla yankılanır. Deneysel m.29 (2026-08-16, seans-7).
"""
import argparse, json, os, subprocess, sys, time

ADIMLAR = [
    ("baglam", ["tools/baglam-tablo.py", "--sessiz"]),
    ("karar", ["tools/karar-borcu-tablo.py", "--sessiz"]),
    ("prompt", ["tools/prompt-tablo.py", "--sessiz"]),
    ("ambar", ["tools/ambar-tablo.py", "--sessiz"]),
    ("deneyim", ["tools/deneyim-tablo.py", "--sessiz"]),  # epizodik deneyim katmanı: amb_olgu_kosum ⋈ hüküm → deneyim + kuşak damgası + çift görünümü + deneyim_fts (KB-44 a, İB-44)
    ("hareket", ["tools/hareket-tablo.py", "--sessiz"]),
    ("seyir", ["tools/baglam-seyir.py", "--sessiz"]),  # bağlam kompozisyonu: transkript usage → bronz/silver/gold (KB-50/52 a, İB-22; uyarı kanalı)
    ("tarama", ["tools/tarama-plan.py", "--sessiz"]),  # tarama-yöntemi plan-regresyon testi (uyarı modu; salt-okur, ~1 sn; KB-53 İB-25 / KB-58)
    ("saglik", ["tools/silver-saglik.py", "--sessiz"]),  # silver-sağlık: bayrak + güncel görünüm + kuyruk (Karar 58 / İB-42; uyarı modu — kapı yalnız --kapi ile seans-kapanis/damitma)
    ("bag", ["tools/bag-tablo.py", "--sessiz"]),  # tipli-bağ katmanı ilk adım (KB-61 → Karar 74 M-1 b): silver `bag` (yalnız wasRevisionOf; R1/R2/R3 kural-tabanlı) + bitemporal kütük; saglik SONRASI (anahtar_kaydi), graf ÖNCESİ (kenar tipi)
    ("erisim", ["tools/erisim-fts.py", "--insa", "--eval", "--sessiz"]),  # erişim katmanı: FTS5 indeks + İB-20 eval (KB-43 a / Karar 60; saglik SONRASI — gecerlilik bayrağı)
    ("graf", ["tools/pointer-graf.py", "--sessiz", "--d2-dizin", "graf/", "--kirik", "--render", "2",
              "--d2", "graf/pointer-sistemi-v0-tam.d2", "--kenar-listesi", "graf/pointer-sistemi-v0-kenarlar.txt"]),
    # ↑ pointer-graf türetimi (İB-48 3/3, Karar 67 G1; uyarı kanalı). --d2/--kenar-listesi = LLM/makine katmanı METİN türevleri
    #   (tam.d2 + kenarlar.txt) her koşumda tazelenir; tam.svg render'ı HATTA GİRMEZ (dev arşiv panosu; elle: d2 --layout=elk)
    ("obsidian-harita", ["tools/obsidian-harita.py", "--sessiz"]),  # Karar 72 EK (Salih seçimi A): silver referans → graf/obsidian-harita*.md (gitignore'lu türev; backtick pointer kütlesi Obsidian grafiğine, gövdelere dokunmadan)
    ("loop", ["tools/loop-dedektor.py", "--sessiz"]),  # İB-60 (Karar 78 m.43 2. rev): hareket → görev n-gram → k_W ADAY listesi (v_loop_aday; kutu yazımı yalnız --kutu ile, hatta değil)
    ("anakronizm", ["tools/anakronizm-denetim.py", "--sessiz"]),  # anakronizm lint (KB-67 a / Karar 69): UYARI kanalı; İHLAL=çıkış 3 hattı DÜŞÜRMEZ, sayılır — kapı sertleşmesi iterasyonla, Salih masası
    ("olcum", ["tools/katman-olcum.py"]),  # SON ADIM kalır (kanon §8 S3: "katman-hatti son adımı katman-olcum.py"); yeni yükleyici bunun ÜSTÜNE eklenir
]
UYARI_KANALI_ADIMLAR = {"tarama", "saglik", "seyir", "anakronizm", "graf", "tarama-duckdb"}  # çıkış 0'da bile stderr'i uyarı kanalı olan adımlar (UYARI/BEKLENTİ DIŞI/HATA satırları hatta görünür)
UYARI_KODLARI = {"anakronizm": {3}}  # KB-67 a: bu kodlar 'UYARI' etiketi alır, hat düşmez (İHLAL sayılır-raporlanır; pre-commit yok)
# Opsiyonel kolon katmanı (pipeline kolon-katmani SH-1/SH-2; Karar 63 KB-55: k=3 soğuk-ölçüme dek varsayılan kapalı)
PARQUET_ADIMLAR = [
    ("parquet", ["tools/ambar-parquet.py", "--sessiz"]),
    ("kolon-olcum", ["tools/kolon-olcum.py", "--sessiz"]),
    ("tarama-duckdb", ["tools/tarama-plan-duckdb.py", "--sessiz"]),  # DuckDB/parquet plan-sınıfı denetimi (İB-38, KB-58 a; uyarı modu; zone-map footer simülasyonu)
]
ATLANDI_KODLARI = {"parquet": {4}, "tarama-duckdb": {4}}  # duckdb yoksa ambar-parquet / tarama-duckdb 4 döner → hat düşmez, "atlandı" sayılır


def atla_sec(secim):
    """--atla virgüllü listesi → (bilinen adım adları, bilinmeyen adlar); virgül çevresi boşluk kırpılır. Bilinmeyen ad sessizce
    'atlandı' sayılmaz — çağıran stderr'e listeler ve çıkış 2 verir (FAIL-LOUD; --tablo/--sorgu ile aynı kural)."""
    adlar = [x.strip() for x in secim.split(",") if x.strip()]
    bilinen = {ad for ad, _ in ADIMLAR + PARQUET_ADIMLAR} | {"hijyen"}
    return [x for x in adlar if x in bilinen], [x for x in adlar if x not in bilinen]


KIRA_YOLU = os.path.join("veri", ".kira-katman-hatti.json")  # PK-7 adlandırılmış kira (Karar 83 A2; gitignore-sınıfı geçici dosya)
KIRA_TTL_S = 600  # m.29: ölçümsüz ilk değer, pilotta kalibre (İB-63 cevaplanmamış soru 3)


def kira_al(repo):
    """Adlandırılmış kira (PK-5 silver tek-yazar + PK-7): dosya varsa ve TTL taze ise bekle (60 sn) → çıkış 5 ("dene-geç" değil,
    kuyruğa iade çağıranın). Ölü-sahip (TTL aşımı) süpürülür; sahip="salih" kirası ASLA süpürülmez (PK-7, Salih kilidi)."""
    yol = os.path.join(repo, KIRA_YOLU); t0 = time.time()
    while True:
        try:
            fd = os.open(yol, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, json.dumps({"sahip": "katman-hatti", "pid": os.getpid(), "ts": time.time()}).encode()); os.close(fd)
            return yol
        except FileExistsError:
            try:
                with open(yol) as f: k = json.load(f)
            except Exception:
                k = {}
            if k.get("sahip") != "salih" and time.time() - float(k.get("ts", 0) or 0) > KIRA_TTL_S:
                try: os.remove(yol)
                except FileNotFoundError: pass
                continue
            if time.time() - t0 > 60:
                print("[KIRA] %s dolu (sahip=%s pid=%s) — eşzamanlı katman-hatti koşulmaz (PK-5); sonra yeniden dene" %
                      (KIRA_YOLU, k.get("sahip"), k.get("pid")), file=sys.stderr)
                sys.exit(5)
            time.sleep(2)


def kira_birak(yol):
    try: os.remove(yol)
    except (FileNotFoundError, TypeError): pass


def adimlari_sec(parquet=False, atla=()):
    """Koşulacak adım listesi (ad, komut): temel hat + (parquet bayrağıyla) kolon katmanı; --atla adları çıkarılır."""
    atla = set(atla)
    secili = list(ADIMLAR)
    if parquet:  # kolon katmanı olcum'un ÖNÜNE girer (kanon §8 S3: olcum SON ADIM kalır; parquet_uretim satırları olcum testine görünür — İB-31, 08-29)
        i = next((n for n, (ad, _) in enumerate(secili) if ad == "olcum"), len(secili))
        secili = secili[:i] + list(PARQUET_ADIMLAR) + secili[i:]
    return [(ad, cmd) for ad, cmd in secili if ad not in atla]


def yorumlayici_sec(repo, ad):
    """Adım yorumlayıcısı: parquet adımları (duckdb ister) repo-içi `.venv/bin/python` varsa onunla koşar (Karar 63 KB-55 'venv';
    İB-30 'duckdb venv yolu hat'a bağlanır', 08-29); yoksa sys.executable → ambar-parquet çıkış 4 → ATLANDI (hat düşmez)."""
    if ad in {x for x, _ in PARQUET_ADIMLAR}:
        venv_py = os.path.join(repo, ".venv", "bin", "python")
        if os.path.exists(venv_py):
            return venv_py
    return sys.executable


def adim_durumu(ad, returncode):
    """Adım çıkış kodu → (durum etiketi, hat düşer mi). 0 → ('OK', False); ATLANDI_KODLARI[ad] içindeki kod → ('ATLANDI', False)
    (ör. parquet 4 = duckdb/eklenti yok, opsiyonel katman atlanır); UYARI_KODLARI[ad] içindeki kod → ('UYARI', False)
    (ör. anakronizm 3 = İHLAL var, KB-67 a: sayılır ama hat düşmez); diğer her kod → ('KOD n', True) = FAIL-LOUD, hat çıkış kodu olur."""
    if returncode == 0:
        return "OK", False
    if returncode in ATLANDI_KODLARI.get(ad, set()):
        return "ATLANDI", False
    if returncode in UYARI_KODLARI.get(ad, set()):
        return "UYARI", False
    return "KOD %d" % returncode, True


def hijyen(repo, atla=""):
    """SQLite hijyeni (KB-53 (a), İB-26): ANALYZE (sqlite_stat1 deterministik; planlayıcı girdisi) + PRAGMA optimize; yükleyici DEĞİL, hat-içi tek adım.
    'hijyen' --atla ile atlanabilir; DB yoksa ATLANDI. Çıkış: 0 tamam · 1 hata (hat düşmez: uyarı kanalı)."""
    if "hijyen" in [x.strip() for x in atla.split(",") if x.strip()]:
        print("[atla  ] hijyen"); return 0
    import sqlite3
    db = os.path.join(repo, "veri", "baglam.sqlite")
    if not os.path.exists(db):
        print("[ATLANDI] hijyen        DB yok"); return 0
    t0 = time.time()
    try:
        con = sqlite3.connect(db); con.execute("ANALYZE"); con.execute("PRAGMA optimize"); con.commit()
        n = con.execute("SELECT COUNT(*) FROM sqlite_stat1").fetchone()[0]; con.close()
        print("[OK     ] hijyen %6.1fs  ANALYZE + PRAGMA optimize (sqlite_stat1 %d satır)" % (time.time() - t0, n)); return 0
    except Exception as e:
        print("[UYARI  ] hijyen %6.1fs  %s" % (time.time() - t0, e)); return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--atla", default="", help="virgüllü adım adları (%s)" % ",".join(ad for ad, _ in ADIMLAR + PARQUET_ADIMLAR))
    ap.add_argument("--snapshot", default=None, help="karar-borcu-tablo/olcum için tarih (determinizm)")
    ap.add_argument("--parquet", action="store_true", help="(geriye-uyum; Karar 83 B2'den beri varsayılan zaten AÇIK)")
    ap.add_argument("--parquet-yok", action="store_true", help="kolon katmanını kapat (Karar 83 B2: varsayılan AÇIK; duckdb yoksa zaten ATLANDI)")
    ap.add_argument("--json", action="store_true", help="axi-standardı (İB-58): stdout = TEK makine-okur JSON nesnesi; insan satırları/ilerleme stderr'e")
    a = ap.parse_args(); repo = os.path.abspath(a.repo)
    insan = sys.stderr if a.json else sys.stdout  # axi: makine kanalı stdout, insan kanalı stderr
    kayitlar = []; t_bas = time.time()
    atla, bilinmeyen = atla_sec(a.atla)
    if bilinmeyen:
        print("HATA: bilinmeyen --atla adı: %s · geçerli adlar: %s" % (", ".join(bilinmeyen), ",".join(ad for ad, _ in ADIMLAR + PARQUET_ADIMLAR)),
              file=sys.stderr)
        sys.exit(2)
    for ad in atla:
        print(f"[atla ] {ad}", file=insan); kayitlar.append({"adim": ad, "durum": "atla", "sure_s": 0.0, "kod": None, "uyari": False})
    kod = 0
    kira_yolu = kira_al(repo)  # Karar 83 A2: hat boyunca tek-yazar kirası (finally ile bırakılır)
    try:
        for ad, cmd in adimlari_sec(parquet=not a.parquet_yok, atla=atla):
            if ad == "olcum":
                kod = max(kod, hijyen(repo, a.atla))  # KB-53 (a) İB-26: ANALYZE + PRAGMA optimize (sqlite_stat1) — olcum T2 bunu ölçer
            args = list(cmd)
            if a.snapshot and ad in ("karar",): args += ["--snapshot", a.snapshot]
            if a.snapshot and ad == "olcum": args += ["--simdi", a.snapshot + "T00:00:00"]
            t0 = time.time()
            r = subprocess.run([yorumlayici_sec(repo, ad)] + args, cwd=repo, capture_output=True, text=True)
            dt = time.time() - t0
            durum, duser = adim_durumu(ad, r.returncode)
            uyari = bool(r.returncode != 0 or (ad in UYARI_KANALI_ADIMLAR and r.stderr.strip()))
            kayitlar.append({"adim": ad, "durum": durum, "sure_s": round(dt, 2), "kod": r.returncode, "uyari": uyari,
                             "stderr_son": r.stderr.strip()[-300:] if uyari else ""})
            print(f"[{durum:7}] {ad:11} {dt:5.1f}s  {' '.join(args)}", file=insan)
            if r.stdout.strip() and (r.returncode != 0 or ad == "olcum"):
                print("        " + r.stdout.strip().replace("\n", "\n        ")[:2000], file=insan)
            if uyari:
                print("        STDERR: " + r.stderr.strip()[-600:], file=insan)
            if duser:
                kod = kod or r.returncode
                if ad in ("baglam",):  # çekirdek düşerse aşağısı anlamsız
                    break
        if a.json:  # axi-standardı: tek satır JSON, alanlar sabit; head/kod_sha determinizm damgası
            try:
                head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip()
            except Exception:
                head = None
            print(json.dumps({"arac": "katman-hatti", "surum": "v1", "git_head": head, "cikis": kod, "sure_s": round(time.time() - t_bas, 2),
                              "adim_n": len(kayitlar), "ok_n": sum(1 for k in kayitlar if k["durum"] == "OK"), "uyari_n": sum(1 for k in kayitlar if k["uyari"]),
                              "adimlar": kayitlar}, ensure_ascii=False))
        sys.exit(kod)
    finally:
        kira_birak(kira_yolu)


if __name__ == "__main__":
    main()
