#!/usr/bin/env python3
"""tarama-plan.py — TARAMA-YÖNTEMİ plan-regresyon testi + tarama sözlüğü (SQLite EXPLAIN QUERY PLAN; STDLIB ONLY, Python 3.9).
Pipeline cc/pipeline-2026-08-18-tarama-yontemleri.md SH-1; kanıt cc/rapor-2026-08-18-3.md (S1 katalog, S2 seçim kuralı, S3 tasarım).
KB-53 İB-25 ("noktasal sorgu SCAN olmaz" testi) bu araçla kapsanır. Deneysel m.29.

Ne yapar: tanımlı sorgu setini (noktasal N* · agregasyon A* · skip-scan adayı S* · LIKE önek L* · indekssiz join J* · OR O* · sıralı R*)
silver DB'de EXPLAIN QUERY PLAN ile çalıştırır, planı NORMALİZE eder (SQLite test takımı `do_eqp_test` gevşek-mod deseni — tam-metin
eşitliği DEĞİL: op + tablo + indeks/AUTOMATIC/COVERING/rowid bayrakları), TARAMA SINIFI çıkarır ve BEKLENTİ ile karşılaştırır:
  sınıf ∈ {SEARCH, SEARCH-ROWID, SCAN, SCAN-COVERING, MULTI-INDEX-OR, AUTOMATIC-INDEX, SKIP-SCAN}; bayrak TEMP-BTREE.
İki durum kaydedilir: (1) DB olduğu gibi (sqlite_stat1 var/yok), (2) DB'nin GEÇİCİ KOPYASINDA ANALYZE sonrası — kaynak DB DEĞİŞTİRİLMEZ
(ANALYZE/PRAGMA optimize hijyeni KB-53 İB-26 / KB-58 Salih hükmünde). Sürüm damgası TAM (`sqlite_source_id()`; Apple derlemesi ↔ sqlite.org
tarihi farkı — rapor-3 kör noktası). Çıktı: append-only veri/tarama-plan.jsonl (grain: 1 satır = sorgu × stat1-durumu) + stdout tablo.

Sinyaller (rapor-3 B-YT3/C-YT5): AUTOMATIC-INDEX → kalıcı indeks ADAYI (uyarı) · noktasal sorguda SCAN → İHLAL · TEMP-BTREE → indeks-sıralı
erişim fırsatı (bilgi) · SKIP-SCAN yalnız stat1 ile (bilgi). stderr uyarıları (çıkış 0): `UYARI:` = ihlal · `BEKLENTİ DIŞI: <sorgu>(<durum>) <sınıf> ∉ {…}`
= sınıf beklenti kümesinde değil (uyum=false) · `HATA:` = EXPLAIN'de düşen sorgu (kütükte sonuc=HATA satırı, traceback yok; şema kayması).
Kaynak DB salt-okur URI ile açılır (mode=ro). Çıkış kodu: 0 tamam (uyarılar stderr'de) · 2 DB yok/açılamıyor, bilinmeyen sorgu adı ya da
çalışan sorguların TÜMÜ HATA · 3 ihlal YALNIZ --sert ile (beklenti-dışılık --sert'i etkilemez; hat düşürmez varsayılanı; KB-58 (b) seçeneği).

Kullanım: python3 tools/tarama-plan.py [--repo <yol>] [--db veri/baglam.sqlite] [--cikti veri/tarama-plan.jsonl] [--sorgu N1,A2]
                                       [--analizsiz] [--sert] [--sessiz] [--kuru]
"""
import argparse, json, os, re, shutil, sqlite3, subprocess, sys, tempfile, urllib.request
from datetime import datetime, timezone, timedelta

# Sorgu seti: ad → (açıklama, SQL, parametreler, beklenen sınıflar {stat1 yok}, beklenen sınıflar {stat1 var}, ihlal_ise_ne)
# beklenti = kabul edilen sınıflar kümesi; "noktasal" işaretli sorgularda SCAN/SCAN-COVERING = İHLAL.
SORGULAR = {
    "N1": ("noktasal PK (kayit_id=?)", "SELECT metin FROM kayit WHERE kayit_id=?", ("x",), {"SEARCH"}, {"SEARCH"}, "noktasal"),
    "N2": ("noktasal dosya+satır aralığı", "SELECT kayit_id FROM kayit WHERE dosya_id=? AND satir_bas<=? AND satir_son>=?", ("core/durum-kapsulu.md", 12, 12), {"SEARCH"}, {"SEARCH"}, "noktasal"),
    "N3": ("noktasal referans (tür,değer)", "SELECT kayit_id FROM referans WHERE ref_turu=? AND ref_deger=?", ("kart", "K-015"), {"SEARCH"}, {"SEARCH"}, "noktasal"),
    "N4": ("noktasal karar_borcu (borc_id=?)", "SELECT baslik FROM karar_borcu WHERE borc_id=?", ("KB-43",), {"SEARCH"}, {"SEARCH"}, "noktasal"),
    "N5": ("rowid aralığı (TID range karşılığı)", "SELECT count(*) FROM kayit WHERE rowid BETWEEN ? AND ?", (1000, 2000), {"SEARCH-ROWID"}, {"SEARCH-ROWID"}, "noktasal"),
    "A1": ("tam sayım (seq/index-only scan)", "SELECT count(*) FROM kayit", (), {"SCAN-COVERING", "SCAN"}, {"SCAN-COVERING", "SCAN"}, "agregasyon"),
    "A2": ("dosya×token agregasyon (Q1)", "SELECT dosya_id, count(*), sum(token_kestirim) FROM kayit GROUP BY 1", (), {"SCAN", "SCAN-COVERING"}, {"SCAN", "SCAN-COVERING"}, "agregasyon"),
    "A3": ("indekssiz kolon filtresi (seq scan + filtre)", "SELECT count(*) FROM kayit WHERE blok_turu=?", ("tablo_satiri",), {"SCAN"}, {"SCAN"}, "agregasyon"),
    "S1": ("skip-scan adayı: bileşik indeksin 2. kolonu", "SELECT count(*) FROM referans WHERE ref_deger=?", ("K-015",), {"SCAN-COVERING", "SCAN"}, {"SKIP-SCAN"}, "skip"),
    "L1": ("LIKE önek (dosya_id LIKE 'core/%')", "SELECT count(*) FROM kayit WHERE dosya_id LIKE ?", ("core/%",), {"SCAN-COVERING", "SCAN", "SEARCH"}, {"SCAN-COVERING", "SCAN", "SEARCH"}, "like"),
    "L2": ("önek = aralık yüklemi (LIKE alternatifi)", "SELECT count(*) FROM kayit WHERE dosya_id >= ? AND dosya_id < ?", ("core/", "core0"), {"SEARCH"}, {"SEARCH"}, "noktasal"),
    "J1": ("indekssiz kolonda join (otomatik indeks sinyali)", "SELECT count(*) FROM dosya d JOIN kayit k ON k.bolum_yolu = d.baslik", (), {"AUTOMATIC-INDEX", "SCAN", "SEARCH"}, {"AUTOMATIC-INDEX", "SCAN", "SEARCH"}, "join"),
    "O1": ("iki indeksli koşulun OR'u (MULTI-INDEX OR)", "SELECT count(*) FROM referans WHERE kayit_id=? OR (ref_turu=? AND ref_deger=?)", ("x", "kart", "K-015"), {"MULTI-INDEX-OR", "SEARCH"}, {"MULTI-INDEX-OR", "SEARCH"}, "or"),
    "R1": ("indeks-sıralı erişim (ORDER BY indeks kolonu)", "SELECT dosya_id FROM kayit ORDER BY dosya_id, sira LIMIT 5", (), {"SCAN-COVERING", "SCAN", "SEARCH"}, {"SCAN-COVERING", "SCAN", "SEARCH"}, "sirali"),
}
IHLAL_TURLERI = {"noktasal"}  # bu türde SCAN/SCAN-COVERING = ihlal (KB-53 İB-25 T1)


def git_head(repo):
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip() or "-"
    except Exception:
        return "-"


def normalize_plan(satirlar):
    """EQP detay satırlarını gevşek-mod normalize eder: op + nesne + bayraklar; süslü ayrıntı (parantez içi koşul) atılır,
    yalnız SKIP-SCAN göstergesi 'ANY(' korunur. Dönüş: (normalize satır listesi, sınıf, bayraklar)."""
    norm, siniflar, bayraklar = [], [], set()
    for d in satirlar:
        d = d.strip()
        if d.startswith("MULTI-INDEX OR"):
            norm.append("MULTI-INDEX OR"); siniflar.append("MULTI-INDEX-OR"); continue
        if d.startswith("INDEX ") and d[6:].strip().isdigit():
            continue  # MULTI-INDEX OR alt başlıkları
        if "USE TEMP B-TREE" in d:
            bayraklar.add("TEMP-BTREE"); norm.append("USE TEMP B-TREE"); continue
        m = re.match(r"^(SCAN|SEARCH)\s+(\S+)(.*)$", d)
        if not m:
            norm.append(re.sub(r"\(.*\)", "", d).strip()); continue
        op, nesne, kalan = m.group(1), m.group(2), m.group(3)
        skip = "ANY(" in kalan
        if "AUTOMATIC" in kalan:
            sinif = "AUTOMATIC-INDEX"; etiket = "USING AUTOMATIC INDEX"
        elif "INTEGER PRIMARY KEY" in kalan:
            sinif = "SEARCH-ROWID" if op == "SEARCH" else "SCAN"; etiket = "USING INTEGER PRIMARY KEY"
        elif "COVERING INDEX" in kalan:
            sinif = "SKIP-SCAN" if skip else ("SCAN-COVERING" if op == "SCAN" else "SEARCH")
            im = re.search(r"COVERING INDEX (\S+)", kalan); etiket = "USING COVERING INDEX " + (im.group(1) if im else "?")
        elif "USING INDEX" in kalan:
            sinif = "SKIP-SCAN" if skip else ("SEARCH" if op == "SEARCH" else "SCAN")
            im = re.search(r"USING INDEX (\S+)", kalan); etiket = "USING INDEX " + (im.group(1) if im else "?")
        else:
            sinif = "SEARCH" if op == "SEARCH" else "SCAN"; etiket = ""
        siniflar.append(sinif)
        norm.append((op + " " + nesne + " " + etiket + (" [ANY]" if skip else "")).strip())
    # birleşik sınıf: MULTI-INDEX-OR > AUTOMATIC-INDEX > SKIP-SCAN > (dış döngü = ilk satır) sırasıyla baskın
    if "MULTI-INDEX-OR" in siniflar: sinif = "MULTI-INDEX-OR"
    elif "AUTOMATIC-INDEX" in siniflar: sinif = "AUTOMATIC-INDEX"
    elif "SKIP-SCAN" in siniflar: sinif = "SKIP-SCAN"
    elif siniflar: sinif = siniflar[0]
    else: sinif = "BILINMIYOR"
    return norm, sinif, sorted(bayraklar)


def plan_al(con, sql, params):
    satirlar = [r[3] for r in con.execute("EXPLAIN QUERY PLAN " + sql, params).fetchall()]
    return normalize_plan(satirlar)


def stat1_var(con):
    return bool(con.execute("SELECT count(*) FROM sqlite_master WHERE name='sqlite_stat1'").fetchone()[0])


def mevcut_nesneler(con):
    return {r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type IN ('table','view')").fetchall()}


def sorgu_calisir(con, sql, params, nesneler):
    """Sorgunun tabloları DB'de yoksa (küçük/eksik silver) ATLANDI."""
    for t in re.findall(r"\bFROM\s+(\w+)|\bJOIN\s+(\w+)", sql, flags=re.I):
        ad = t[0] or t[1]
        if ad not in nesneler:
            return False, "tablo yok: " + ad
    return True, ""


def salt_okur_ac(db):
    """Kaynak DB'yi SALT-OKUR URI ile açar (mode=ro): yanlışlıkla ANALYZE/yazma denemesi sessizce DB'yi değiştirmez, hata verir;
    dosya yoksa boş DB de yaratılmaz. Açılamazsa sqlite3.Error yükselir (çağıran çıkış 2'ye çevirir)."""
    return sqlite3.connect("file:%s?mode=ro" % urllib.request.pathname2url(os.path.abspath(db)), uri=True)


def kos(db, secili, analiz):
    """DB'de (ve istenirse geçici ANALYZE kopyasında) planları toplar; satır listesi döner. Kaynak DB değişmez (salt-okur bağlantı).
    Sorgu EXPLAIN'de düşerse (şema kayması: kolon adı vb.) traceback yerine sonuc=HATA satırı yazılır, kalan sorgular sürer.
    Geçici kopya ve bağlantılar her durumda (hata dahil) kapatılır/silinir. DB açılamazsa sqlite3.Error yükselir."""
    con = salt_okur_ac(db)
    kon2, tmpdir, satirlar = None, None, []
    try:
        surum, kaynak_id = con.execute("SELECT sqlite_version(), sqlite_source_id()").fetchone()
        nesneler = mevcut_nesneler(con)
        durumlar = [("oldugu-gibi", con, stat1_var(con))]
        if analiz:
            tmpdir = tempfile.mkdtemp(prefix="tarama-plan-")
            kopya = os.path.join(tmpdir, "analiz.sqlite")
            shutil.copyfile(db, kopya)
            kon2 = sqlite3.connect(kopya); kon2.execute("ANALYZE"); kon2.commit()
            durumlar.append(("analiz-kopya", kon2, True))
        for ad in secili:
            acik, sql, params, bek0, bek1, tur = SORGULAR[ad]
            for durum_adi, c, s1 in durumlar:
                olur, neden = sorgu_calisir(c, sql, params, nesneler)
                temel = {"sorgu": ad, "aciklama": acik, "durum": durum_adi, "stat1": s1, "tur": tur}
                if not olur:
                    satirlar.append(dict(temel, sonuc="ATLANDI", neden=neden)); continue
                try:
                    norm, sinif, bayrak = plan_al(c, sql, params)
                except sqlite3.Error as e:
                    satirlar.append(dict(temel, sonuc="HATA", neden=str(e) or type(e).__name__)); continue
                beklenti = bek1 if s1 else bek0
                uyum = sinif in beklenti
                ihlal = (tur in IHLAL_TURLERI) and sinif in ("SCAN", "SCAN-COVERING")
                sinyal = []
                if sinif == "AUTOMATIC-INDEX": sinyal.append("kalici-indeks-adayi")
                if "TEMP-BTREE" in bayrak: sinyal.append("indeks-sirali-erisim-firsati")
                if sinif == "SKIP-SCAN": sinyal.append("skip-scan-aktif(stat1)")
                if ihlal: sinyal.append("IHLAL:noktasal-tarama")
                satirlar.append(dict(temel, sonuc="OK", sinif=sinif, plan=" | ".join(norm), bayrak=bayrak, beklenti=sorted(beklenti),
                                     uyum=uyum, ihlal=ihlal, sinyal=sinyal))
    finally:
        con.close()
        if kon2 is not None:
            kon2.close()
        if tmpdir:
            shutil.rmtree(tmpdir, ignore_errors=True)
    return satirlar, surum, kaynak_id


def main():
    ap = argparse.ArgumentParser(description="SQLite tarama-yöntemi plan-regresyon testi (EQP normalize + beklenti; kaynak DB değişmez)")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--db", default="veri/baglam.sqlite")
    ap.add_argument("--cikti", default="veri/tarama-plan.jsonl")
    ap.add_argument("--sorgu", default="", help="virgüllü alt küme (N1,A2,…); boş = hepsi")
    ap.add_argument("--analizsiz", action="store_true", help="geçici ANALYZE kopyasını atla (yalnız olduğu-gibi durum)")
    ap.add_argument("--sert", action="store_true", help="ihlal varsa çıkış 3 (varsayılan: uyarı, çıkış 0)")
    ap.add_argument("--sessiz", action="store_true")
    ap.add_argument("--kuru", action="store_true", help="kütüğe yazma")
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)
    yol = lambda p: p if os.path.isabs(p) else os.path.join(repo, p)
    db, cikti = yol(a.db), yol(a.cikti)
    if not os.path.exists(db):
        print("HATA: silver DB yok: %s" % db, file=sys.stderr); return 2
    istenen = [x.strip() for x in a.sorgu.split(",") if x.strip()]
    bilinmeyen = [x for x in istenen if x not in SORGULAR]
    if bilinmeyen:
        print("HATA: bilinmeyen sorgu adı: %s (geçerli: %s)" % (", ".join(bilinmeyen), ", ".join(SORGULAR)), file=sys.stderr); return 2
    secili = istenen or list(SORGULAR)
    try:
        satirlar, surum, kaynak_id = kos(db, secili, analiz=not a.analizsiz)
    except sqlite3.Error as e:
        print("HATA: silver DB açılamadı/hazırlanamadı: %s — %s" % (db, e or type(e).__name__), file=sys.stderr); return 2
    tz = timezone(timedelta(hours=3))
    ortak = {"ts": datetime.now(tz).isoformat(timespec="seconds"), "git_head": git_head(repo), "sqlite": surum, "sqlite_source_id": kaynak_id,
             "damga": "deneysel m.29; sınıf = EQP normalize (do_eqp_test gevşek modu); analiz-kopya = geçici kopyada ANALYZE, kaynak DB değişmez"}
    kayitlar = [dict(ortak, **s) for s in satirlar]
    if not a.kuru:
        with open(cikti, "a", encoding="utf-8") as fh:
            for k in kayitlar:
                fh.write(json.dumps(k, ensure_ascii=False) + "\n")
    ihlaller = [k for k in kayitlar if k.get("ihlal")]
    uyumsuzlar = [k for k in kayitlar if k["sonuc"] == "OK" and not k["uyum"]]
    hatalar = [k for k in kayitlar if k["sonuc"] == "HATA"]
    if not a.sessiz:
        print("%-4s %-13s %-6s %-16s %-6s %s" % ("sorgu", "durum", "stat1", "sınıf", "uyum", "plan / sinyal"))
        for k in kayitlar:
            if k["sonuc"] != "OK":
                print("%-4s %-13s %-6s %-16s %-6s %s" % (k["sorgu"], k["durum"], "-", k["sonuc"], "-", k["neden"])); continue
            print("%-4s %-13s %-6s %-16s %-6s %s%s" % (k["sorgu"], k["durum"], "var" if k["stat1"] else "yok", k["sinif"], "✓" if k["uyum"] else "✗",
                                                     k["plan"][:90], ("  ← " + ",".join(k["sinyal"])) if k["sinyal"] else ""))
        print("tarama-plan: %d satır → %s (%s) · sqlite %s (%s) · ihlal %d · beklenti-dışı %d · hata %d · HEAD %s" % (
            len(kayitlar), os.path.relpath(cikti, repo), "KURU" if a.kuru else "eklendi", surum, kaynak_id[:10], len(ihlaller), len(uyumsuzlar),
            len(hatalar), ortak["git_head"]))
    if hatalar:
        print("HATA: %d sorgu EXPLAIN'de düştü (şema kayması?): %s" % (
            len(hatalar), " · ".join("%s(%s): %s" % (k["sorgu"], k["durum"], k["neden"]) for k in hatalar)), file=sys.stderr)
        if not any(k["sonuc"] == "OK" for k in kayitlar):
            print("HATA: çalışan sorguların tümü düştü; kütük yazıldı, çıkış 2", file=sys.stderr); return 2
    if ihlaller:
        print("UYARI: %d noktasal sorgu tarama (SCAN) planına düştü: %s" % (len(ihlaller), ", ".join(sorted({k["sorgu"] for k in ihlaller}))), file=sys.stderr)
    for k in uyumsuzlar:
        print("BEKLENTİ DIŞI: %s(%s) %s ∉ {%s}" % (k["sorgu"], k["durum"], k["sinif"], ", ".join(k["beklenti"])), file=sys.stderr)
    if ihlaller and a.sert:
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
