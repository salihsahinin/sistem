#!/usr/bin/env python3
"""silver-saglik.py — SİLVER SAĞLIK: bayrak + güncel-görünüm + tespit-damgalı kuyruk (Karar 58 = KB-39/40/41 (a); İB-42 icrası).

Ne yapar (STDLIB ONLY, Python ≥3.9, SQLite ≥3.25; deterministik — aynı HEAD + aynı disk + aynı kütük → aynı tablo/görünüm, yalnız ts farklı):
  0. Bağlam Anahtar Kaydı'nı (core/baglam-anahtar-kaydi.md ```json bloğu) silver'a JOIN eder → `anahtar_kaydi` tablosu
     (1 satır = 1 DEĞER: güncel/emekli/aday; replaced_by · gecerli_bas/bitis · izinli_kaliplar) — eski İB-16.
     `kayit` tablosuna TÜRETİLMİŞ kolonlar ekler (additive; baglam-tablo.py DB'yi sıfırdan yazdığı için her koşumda yeniden türetilir):
     gecerlilik ∈ {guncel, tarihce, emekli-kalinti, celiski-kaybeden, karantina} · gecerlilik_neden (kural kimliği) · tespit_tarihi (kuyruk damgası).
     Silver satırı SİLİNMEZ/düşürülmez; bronz DOKUNULMAZ; düzeltme bronz'da → yeniden üretim (world-model §1).
  1. T-Ç çelişki testleri (SQL/kural; şiddet kural dosyasından): T-C1 tam-bir güncel · T-C2 aralık örtüşmesi · T-C3 emekli kalıntı
     (sıcak error / ılık warn; `anahtar-denetim.py` ile TEK TANIM — norm + compile_patterns içe aktarılır) · T-C4a/b/c karar_borcu
     · T-C5 zarf bitiş dolu∧boş · T-C6 kaynak+birim denetimi (katsayı listesi).
  2. T-B bayatlık yüklemleri — yalnız ADAY üretir, karar vermez (çıkarma Salih kapısından): SUPERSEDED · MISLEADING · YETİM · KAPANDI;
     korumalar: min-N sürüm + muafiyet kancası (kural dosyası `muafiyet`); pencere birimi SEANS (teslim dosyası sayısı).
  3. T-A anlamsal ön-eleme (deterministik huni) → `silver_karantina_aday` çiftleri; LLM ÇAĞRILMAZ (prompt: veri/sozlesme/silver-saglik-kanit-bulucu-prompt.md).
  4. Görünümler: v_guncel_kayit · v_guncel_anahtar · v_guncel_karar · v_silver_kuyruk · v_silver_kuyruk_ozet · v_silver_saglik_son (+ küçük CSV'ler).
  5. Kütük: veri/silver-saglik.jsonl APPEND-ONLY (grain: 1 satır = 1 test × 1 koşum) · veri/silver-kuyruk.jsonl OLAY-KAYNAKLI (ACILDI/KAPANDI;
     tespit_tarihi = ilk ACILDI; kuyruk yaşı/drenaj buradan).
  6. --test: canary (bilinen ihlal tohumlu geçici DB → ilgili test FAIL vermeli; dbt unit-test deseni C-YT2).
Kullanım: python3 tools/silver-saglik.py [--repo <yol>] [--kapi] [--sessiz] [--kuru] [--snapshot YYYY-MM-DD] [--test] [--json]
Çıkış: 0 tamam (uyarı modu: ihlaller yazılır, hat düşmez — C-EK-3 "önce uyarı aşaması") · 6 = --kapi ile T-Ç error ihlali (seans-kapanis/damitma kapısı)
       · 2 girdi/şema hatası · 7 canary FAIL. Deneysel m.29 (2026-08-22, seans-14, Carvis). Additive-only.
"""
import argparse, csv, glob, hashlib, importlib.util, json, os, re, shutil, sqlite3, subprocess, sys, tempfile
from datetime import date, datetime, timezone

KURAL_YOLU = "veri/sozlesme/silver-saglik-kurallar.json"
KAYIT_YOLU = "core/baglam-anahtar-kaydi.md"
LOG_YOLU = "veri/silver-saglik.jsonl"
KUYRUK_YOLU = "veri/silver-kuyruk.jsonl"
ACIK_DURUM = ("İMZASIZ", "BEKLET", "Salih'te", "masaya", "kısmen-kapandı", "belirsiz", "icra-sırada")


# ---------------------------------------------------------------- yardımcılar
def sha1_hex(b):
    return hashlib.sha1(b).hexdigest()


def git_head(repo):
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "?"


def anahtar_denetim_modulu(repo):
    """TEK TANIM: norm/compile_patterns/load_registry/integrity anahtar-denetim.py'den içe aktarılır (T-Ç3 ikinci tanım yazılmaz)."""
    yol = os.path.join(repo, "tools", "anahtar-denetim.py")
    spec = importlib.util.spec_from_file_location("anahtar_denetim", yol)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def kurallari_oku(repo):
    yol = os.path.join(repo, KURAL_YOLU)
    try:
        with open(yol, encoding="utf-8") as fh:
            k = json.load(fh)
    except (OSError, json.JSONDecodeError) as e:
        sys.exit("[HATA] kural dosyası okunamadı: %s (%s)" % (KURAL_YOLU, e))
    gerekli = ("testler", "pencere", "muafiyet", "supersede_damga", "yetim", "on_eleme", "katsayilar", "min_n_surum")
    eksik = [g for g in gerekli if g not in k]
    if eksik:
        sys.exit("[HATA] kural dosyasında eksik alan: %s" % ", ".join(eksik))
    return k


def seans_tarihleri(repo):
    """SEANS sayacı: raporlar/seans/seans-teslim-*.md + raporlar/vardiya/vardiya-teslim-*.md dosya adlarındaki tarihler (1 dosya = 1 seans); sıralı liste."""
    out = []
    for p in glob.glob(os.path.join(repo, "raporlar", "seans", "seans-teslim-*.md")) + glob.glob(os.path.join(repo, "raporlar", "vardiya", "vardiya-teslim-*.md")):
        m = re.search(r"(\d{4}-\d{2}-\d{2})", os.path.basename(p))
        if m:
            out.append(m.group(1))
    return sorted(out)


def yas_seans(seanslar, tarih_iso):
    """Hedef tarihten SONRA kaç seans geçti (tarih > hedef). Tarihsiz → None (yaş bilinmiyor; m.39 '—')."""
    if not tarih_iso:
        return None
    t = tarih_iso[:10]
    return sum(1 for s in seanslar if s > t)


def muaf_mi(dosya_id, muafiyet, otomatik_muaf):
    if dosya_id in otomatik_muaf:
        return True
    for on in muafiyet.get("dosya_onek", []):
        if dosya_id.startswith(on):
            return True
    for ic in muafiyet.get("dosya_icerir", []):
        if ic in dosya_id:
            return True
    return False


def kapanis_tarihi(kapanis_kaniti, kayit_tarihi):
    """kapanis_kaniti metnindeki ilk 'AA-GG' → 2026-AA-GG (yıl: kayıt tarihinin yılı); yoksa kayit_tarihi."""
    yil = (kayit_tarihi or "2026")[:4]
    m = re.search(r"(?<!\d)(\d{2})-(\d{2})(?!\d)", kapanis_kaniti or "")
    if m and 1 <= int(m.group(1)) <= 12 and 1 <= int(m.group(2)) <= 31:
        return "%s-%s-%s" % (yil, m.group(1), m.group(2))
    return kayit_tarihi


# ---------------------------------------------------------------- şema (additive)
DDL = """
CREATE TABLE IF NOT EXISTS anahtar_kaydi (
  kaydi_id TEXT PRIMARY KEY, anahtar_id TEXT, tur TEXT, rol TEXT, deger TEXT, deger_norm TEXT,
  gecerli_bas TEXT, gecerli_bitis TEXT, replaced_by TEXT, gerekce TEXT, varyantlar TEXT, izinli_kaliplar TEXT,
  kaldirma_en_erken TEXT, kaynak TEXT, kayit_dosyasi TEXT
);
CREATE TABLE IF NOT EXISTS silver_kuyruk (
  kuyruk_id TEXT PRIMARY KEY, tip TEXT, hedef_tur TEXT, hedef_id TEXT, dosya_id TEXT, neden TEXT, eylem TEXT,
  tespit_tarihi TEXT, yas_gun INTEGER, yas_seans INTEGER, siddet TEXT, snapshot_tarih TEXT, kosum_id TEXT
);
CREATE TABLE IF NOT EXISTS silver_karantina_aday (
  cift_id TEXT PRIMARY KEY, anahtar_terim TEXT, kayit_id_a TEXT, kayit_id_b TEXT, dosya_a TEXT, dosya_b TEXT,
  blok_turu TEXT, uzunluk_a INTEGER, uzunluk_b INTEGER, kosum_id TEXT
);
CREATE TABLE IF NOT EXISTS silver_saglik_son (
  test_id TEXT PRIMARY KEY, ad TEXT, sinif TEXT, siddet TEXT, ihlal INTEGER, sonuc TEXT, ornek TEXT, not_ TEXT,
  kosum_id TEXT, snapshot_tarih TEXT, head TEXT
);
"""
GORUNUMLER = [
    ("v_guncel_kayit", """CREATE VIEW IF NOT EXISTS v_guncel_kayit AS
SELECT k.kayit_id, k.dosya_id, d.katman, k.sira, k.bolum_yolu, k.blok_turu, k.satir_bas, k.satir_son, k.metin, k.metin_kisa,
       k.token_kestirim, k.tarih_iso, k.gecerlilik, k.gecerlilik_neden, k.tespit_tarihi
FROM kayit k JOIN dosya d ON d.dosya_id=k.dosya_id
WHERE k.gecerlilik='guncel' AND d.katman IN ('sicak','ilik')
ORDER BY k.dosya_id, k.sira"""),
    ("v_guncel_anahtar", """CREATE VIEW IF NOT EXISTS v_guncel_anahtar AS
SELECT a.anahtar_id, a.tur, a.deger AS guncel_deger, a.gecerli_bas, a.kaynak,
       (SELECT COUNT(*) FROM anahtar_kaydi e WHERE e.anahtar_id=a.anahtar_id AND e.rol='emekli') AS emekli_sayisi,
       (SELECT GROUP_CONCAT(e.deger, ' | ') FROM anahtar_kaydi e WHERE e.anahtar_id=a.anahtar_id AND e.rol='emekli') AS emekli_degerler,
       s.referans_sayisi AS gozlenen_referans, s.sicak_referans_sayisi AS gozlenen_sicak_referans
FROM anahtar_kaydi a LEFT JOIN anahtar s ON s.tur='anahtar_terim' AND s.deger=a.deger_norm
WHERE a.rol='guncel'
ORDER BY a.anahtar_id"""),
    ("v_guncel_karar", """CREATE VIEW IF NOT EXISTS v_guncel_karar AS
SELECT b.borc_id, b.baslik, b.kume, b.tur, b.katman, b.karar_sahibi, b.durum, b.kayit_tarihi, b.yas_gun, b.bagimlilik, b.oneri
FROM karar_borcu b
WHERE b.durum IN ('İMZASIZ','BEKLET','Salih''te','masaya','kısmen-kapandı','belirsiz','icra-sırada')
  AND NOT EXISTS (SELECT 1 FROM silver_kuyruk q WHERE q.hedef_tur='karar_borcu' AND q.hedef_id=b.borc_id AND q.tip LIKE 'T-C4%')
ORDER BY b.katman, b.borc_id"""),
    ("v_silver_kuyruk", """CREATE VIEW IF NOT EXISTS v_silver_kuyruk AS
SELECT tip, hedef_tur, hedef_id, dosya_id, neden, eylem, tespit_tarihi, yas_gun, yas_seans, siddet
FROM silver_kuyruk ORDER BY tip, tespit_tarihi, hedef_id"""),
    ("v_silver_kuyruk_ozet", """CREATE VIEW IF NOT EXISTS v_silver_kuyruk_ozet AS
SELECT tip, siddet, COUNT(*) AS n, MIN(tespit_tarihi) AS en_eski_tespit, MAX(yas_gun) AS en_yasli_gun,
       ROUND(AVG(yas_gun),1) AS ort_yas_gun, SUM(CASE WHEN yas_gun>30 THEN 1 ELSE 0 END) AS n_30gun_ustu
FROM silver_kuyruk GROUP BY tip, siddet ORDER BY tip"""),
    ("v_silver_saglik_son", """CREATE VIEW IF NOT EXISTS v_silver_saglik_son AS
SELECT test_id, sinif, siddet, ihlal, sonuc, ornek, not_, kosum_id, snapshot_tarih, head FROM silver_saglik_son
ORDER BY CASE sinif WHEN 'celiski' THEN 0 WHEN 'bayatlik' THEN 1 ELSE 2 END, test_id"""),
]
CSV_GORUNUMLER = ["v_silver_saglik_son", "v_silver_kuyruk_ozet", "v_silver_kuyruk", "v_guncel_anahtar"]


def sema_hazirla(con):
    con.executescript(DDL)
    kolonlar = {r[1] for r in con.execute("PRAGMA table_info(kayit)")}
    for ad, tip in (("gecerlilik", "TEXT"), ("gecerlilik_neden", "TEXT"), ("tespit_tarihi", "TEXT")):
        if ad not in kolonlar:
            con.execute("ALTER TABLE kayit ADD COLUMN %s %s" % (ad, tip))
    for _ad, sql in GORUNUMLER:
        con.execute(sql)
    # her koşumda yeniden türetilir (idempotent; kaynak bronz + kural dosyası)
    con.execute("DELETE FROM anahtar_kaydi"); con.execute("DELETE FROM silver_kuyruk")
    con.execute("DELETE FROM silver_karantina_aday"); con.execute("DELETE FROM silver_saglik_son")
    con.execute("UPDATE kayit SET gecerlilik=NULL, gecerlilik_neden=NULL, tespit_tarihi=NULL")


# ---------------------------------------------------------------- Adım 0: anahtar kaydı → silver
def anahtar_kaydini_yukle(con, reg, ad_mod, kayit_dosyasi):
    rows = []
    for a in reg.get("anahtarlar", []):
        aid = a.get("anahtar_id") or "?"
        g = a.get("guncel") or {}
        rows.append(("%s|guncel|%s" % (aid, g.get("deger", "")), aid, a.get("tur"), "guncel", g.get("deger", ""), ad_mod.norm(g.get("deger", "")),
                     g.get("gecerli_bas"), None, None, None, "[]", "[]", None, g.get("kaynak"), kayit_dosyasi))
        for rol in ("emekli", "aday"):
            for e in a.get(rol, []) or []:
                rows.append(("%s|%s|%s" % (aid, rol, e.get("deger", "")), aid, a.get("tur"), rol, e.get("deger", ""), ad_mod.norm(e.get("deger", "")),
                             None, e.get("tarih"), e.get("replaced_by") if isinstance(e.get("replaced_by"), str) else (json.dumps(e.get("replaced_by"), ensure_ascii=False) if e.get("replaced_by") else None),
                             e.get("gerekce"), json.dumps(e.get("varyantlar", []), ensure_ascii=False), json.dumps(e.get("izinli_kaliplar", []), ensure_ascii=False),
                             e.get("kaldirma_en_erken"), None, kayit_dosyasi))
    con.executemany("INSERT OR REPLACE INTO anahtar_kaydi VALUES (%s)" % ",".join("?" * 15), rows)
    return len(rows)


# ---------------------------------------------------------------- testler
class Sonuclar:
    def __init__(self, kurallar):
        self.tanim = {t["id"]: t for t in kurallar["testler"]}
        self.liste = []   # (test_id, ihlal, ornek[], not)
        self.kuyruk = []  # dict'ler
        self.bayrak = {}  # kayit_id → (gecerlilik, neden)

    def ekle(self, test_id, ihlal, ornek=(), not_=""):
        self.liste.append((test_id, int(ihlal), list(ornek)[:10], not_))

    def kuyruga(self, tip, hedef_tur, hedef_id, dosya_id, neden, eylem, yas_seans_=None):
        self.kuyruk.append({"tip": tip, "hedef_tur": hedef_tur, "hedef_id": hedef_id, "dosya_id": dosya_id, "neden": neden, "eylem": eylem, "yas_seans": yas_seans_})

    def bayrakla(self, kayit_id, gecerlilik, neden):
        # öncelik: emekli-kalinti > celiski-kaybeden > karantina (ilk yazan kazanmaz; sıralı öncelik)
        oncelik = {"emekli-kalinti": 3, "celiski-kaybeden": 2, "karantina": 1}
        eski = self.bayrak.get(kayit_id)
        if eski is None or oncelik[gecerlilik] > oncelik[eski[0]]:
            self.bayrak[kayit_id] = (gecerlilik, neden)


def t_c1_c2(con, S):
    """T-C1 tam-bir güncel + damgasız yok · T-C2 emekli.tarih ≤ güncel.gecerli_bas (örtüşme yok)."""
    c1, c2, o1, o2 = 0, 0, [], []
    for (aid,) in con.execute("SELECT DISTINCT anahtar_id FROM anahtar_kaydi ORDER BY anahtar_id"):
        guncel = con.execute("SELECT deger, gecerli_bas FROM anahtar_kaydi WHERE anahtar_id=? AND rol='guncel' AND (gecerli_bitis IS NULL OR gecerli_bitis='')", (aid,)).fetchall()
        if len(guncel) != 1:
            c1 += 1; o1.append("%s:güncel=%d" % (aid, len(guncel)))
        elif not guncel[0][1]:
            c1 += 1; o1.append("%s:damgasız" % aid)
        bas = guncel[0][1] if len(guncel) == 1 else None
        for deger, bitis in con.execute("SELECT deger, gecerli_bitis FROM anahtar_kaydi WHERE anahtar_id=? AND rol='emekli' ORDER BY deger", (aid,)):
            if not bitis:
                c2 += 1; o2.append("%s/%s:bitişsiz-emekli" % (aid, deger))
            elif bas and bitis > bas:
                c2 += 1; o2.append("%s/%s:%s>%s" % (aid, deger, bitis, bas))
    S.ekle("T-C1", c1, o1); S.ekle("T-C2", c2, o2)


def t_c3(con, S, reg, ad_mod, kural):
    """Emekli değer KALINTISI sıcak/ılık kayit'ta (izinli kalıp hariç) — anahtar-denetim ile aynı norm/kalıp; kayit-grain."""
    kayit_dosyasi = KAYIT_YOLU
    satirlar = con.execute("""SELECT k.kayit_id, k.dosya_id, d.katman, k.metin FROM kayit k JOIN dosya d ON d.dosya_id=k.dosya_id
                              WHERE d.katman IN ('sicak','ilik') AND k.metin IS NOT NULL AND k.dosya_id<>? ORDER BY k.dosya_id, k.sira""", (kayit_dosyasi,)).fetchall()
    metin_norm = [(kid, did, kat, ad_mod.norm(m)) for kid, did, kat, m in satirlar]
    sicak, ilik, os_, oi = 0, 0, [], []
    for a in reg.get("anahtarlar", []):
        aid = a.get("anahtar_id")
        for e in a.get("emekli", []) or []:
            vals = [e.get("deger", "")] + list(e.get("varyantlar", []))
            pats = ad_mod.compile_patterns(vals)
            allow = [re.compile(ad_mod.norm(p), re.I) for p in e.get("izinli_kaliplar", [])]
            for kid, did, kat, nl in metin_norm:
                n = sum(len(p.findall(nl)) for p in pats)
                if not n or any(al.search(nl) for al in allow):
                    continue
                neden = "T-C3:%s/%s" % (aid, e.get("deger"))
                if kat == "sicak":
                    sicak += 1; os_.append(kid); S.bayrakla(kid, "emekli-kalinti", neden)
                    S.kuyruga("T-B-MISLEADING", "kayit", kid, did, neden, "yeniden yaz → '%s' (replaced_by) ya da izinli-kalıp damgası" % e.get("replaced_by"))
                else:
                    ilik += 1; oi.append(kid); S.bayrakla(kid, "emekli-kalinti", neden)
    S.ekle("T-C3-sicak", sicak, os_); S.ekle("T-C3-ilik", ilik, oi)


def t_c4(con, S):
    rows = con.execute("SELECT borc_id, baslik, durum, bagimlilik, kapanis_kaniti FROM karar_borcu ORDER BY borc_id").fetchall()
    ids = {r[0] for r in rows}
    acik = [r for r in rows if r[2] in ACIK_DURUM]
    # (a) aynı normalize başlık
    grup = {}
    for r in acik:
        anahtar = re.sub(r"\s+", " ", (r[1] or "").strip().lower())[:120]
        grup.setdefault(anahtar, []).append(r[0])
    cift = [v for v in grup.values() if len(v) > 1]
    a_ornek = ["|".join(v) for v in cift]
    for v in cift:
        for b in v:
            S.kuyruga("T-C4a", "karar_borcu", b, None, "aynı başlık: %s" % "|".join(v), "birleştir ya da başlığı ayrıştır")
    S.ekle("T-C4a", sum(len(v) for v in cift), a_ornek)
    # (b) kırık bağımlılık
    kirik = []
    for r in acik:
        bag = r[3] or ""
        hedefler = [h for h in re.split(r"[\s,;|]+", bag) if h and re.match(r"^(KB|İB|IB|K)-?\d", h)]
        for h in hedefler:
            if h not in ids:
                kirik.append("%s→%s" % (r[0], h)); S.kuyruga("T-C4b", "karar_borcu", r[0], None, "bağımlılık yok: %s" % h, "bağımlılığı düzelt")
    S.ekle("T-C4b", len(kirik), kirik)
    # (c) kapanış kanıtı 'Karar NN' ama açık — yalnız kapandı-sınıfı kanıt (kısmen-kapandı/BEKLET hükümleri kanıtta 'BEKLET/kısmi' der)
    c = []
    for r in acik:
        kan = r[4] or ""
        if re.search(r"Karar \d+", kan) and r[2] not in ("kısmen-kapandı", "BEKLET") and not re.search(r"BEKLET|kısm[iî]|tetik|bekler|koşullu|icra İB", kan, re.I):
            c.append(r[0]); S.kuyruga("T-C4c", "karar_borcu", r[0], None, "kanıtta hüküm var, durum açık: %s" % kan[:80], "durumu eşitle ya da kanıtı ayır")
    S.ekle("T-C4c", len(c), c)


def t_c5(con, S):
    rows = con.execute("SELECT anahtar_terim, dosya_id, bitisli, bitissiz FROM v_celiski_adayi").fetchall()
    ornek = ["%s@%s" % (r[0], r[1]) for r in rows]
    for at, did, _b, _bs in rows:
        for (kid,) in con.execute("""SELECT k.kayit_id FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id
                                     WHERE r.ref_turu='anahtar_terim' AND r.ref_deger=? AND k.dosya_id=? AND k.zarf_json IS NOT NULL
                                       AND k.zarf_gecerli_bitis IS NOT NULL AND k.zarf_gecerli_bitis<>'' AND k.zarf_gecerli_bitis<>'-'""", (at, did)):
            S.bayrakla(kid, "celiski-kaybeden", "T-C5:%s" % at)
            S.kuyruga("T-B-MISLEADING", "kayit", kid, did, "T-C5 bitişli taraf (%s)" % at, "emekli damgası / zarfı eşitle")
    S.ekle("T-C5", len(rows), ornek)


def t_c6(repo, S, kural):
    ihlal, ornek, kalibresiz = 0, [], 0
    for k in kural.get("katsayilar", []):
        yol = os.path.join(repo, k.get("kanon_dosya", ""))
        try:
            with open(yol, encoding="utf-8") as fh:
                metin = fh.read()
        except OSError:
            ihlal += 1; ornek.append("%s:dosya-yok" % k.get("id")); continue
        if not re.search(k.get("kanon_regex", "(?!)"), metin):
            ihlal += 1; ornek.append("%s:ifade-bulunamadı(drift)" % k.get("id")); continue
        if k.get("durum") not in ("kalibre", "kalibre-edilmemis", "tasinmaz"):
            ihlal += 1; ornek.append("%s:damgasız" % k.get("id")); continue
        if k.get("durum") == "kalibre-edilmemis":
            kalibresiz += 1
    S.ekle("T-C6", ihlal, ornek, "kalibre-edilmemiş damgalı sabit: %d/%d" % (kalibresiz, len(kural.get("katsayilar", []))))


def t_b(con, S, kural, seanslar, snapshot):
    pencere = int(kural["pencere"]["deger"]); muaf = kural["muafiyet"]
    # otomatik muafiyet: aktif anahtar kaynak dosyası + anahtar_kaydi kayıt dosyası
    oto = {r[0] for r in con.execute("SELECT DISTINCT kaynak_dosya FROM anahtar WHERE kaynak_dosya IS NOT NULL AND kaynak_dosya<>'-'")}
    oto.add(KAYIT_YOLU)
    # SUPERSEDED — dosya grain: sıcak/ılık başlık/ilk N blok damgalı
    rx = re.compile(kural["supersede_damga"]["baslik_regex"]); n_ilk = int(kural["supersede_damga"].get("ilk_blok_sayisi", 3))
    sup = []
    for did, kat, baslik in con.execute("SELECT dosya_id, katman, baslik FROM dosya WHERE katman IN ('sicak','ilik') ORDER BY dosya_id"):
        metinler = [baslik or ""] + [r[0] or "" for r in con.execute("SELECT metin FROM kayit WHERE dosya_id=? AND sira<=? ORDER BY sira", (did, n_ilk))]
        if any(rx.search(m) for m in metinler):
            sup.append(did); S.kuyruga("T-B-SUPERSEDED", "dosya", did, did, "süpersede damgası başlık/ilk %d blok" % n_ilk, "arşive indir + pointer bırak (m.8)")
    S.ekle("T-B-SUPERSEDED", len(sup), sup)
    # MISLEADING — T-C3 sıcak + T-C5 kuyruğa zaten yazıldı; burada sayılır
    mis = [q for q in S.kuyruk if q["tip"] == "T-B-MISLEADING"]
    S.ekle("T-B-MISLEADING", len(mis), [q["hedef_id"] for q in mis])
    # YETİM — soğuk dosya, 0 gelen bağ, yaş > pencere, muaf değil
    kb_kaynak_kol = None
    kols = [r[1] for r in con.execute("PRAGMA table_info(karar_borcu_kaynak)")]
    for ad in ("dosya", "dosya_yolu", "kaynak_dosya"):
        if ad in kols:
            kb_kaynak_kol = ad; break
    kb_dosyalar = {r[0] for r in con.execute("SELECT DISTINCT %s FROM karar_borcu_kaynak" % kb_kaynak_kol)} if kb_kaynak_kol else set()
    gelen = {r[0]: r[1] for r in con.execute("""SELECT r.hedef_yol, COUNT(*) FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id
                                                JOIN dosya d ON d.dosya_id=k.dosya_id WHERE r.ref_turu='dosya_pointer' AND r.hedef_var=1
                                                AND d.katman IN ('sicak','ilik') GROUP BY r.hedef_yol""")}
    esik = int(kural["yetim"].get("esik_gelen_bag", 0)); min_yas = int(kural["yetim"].get("min_yas_seans", pencere))
    yet, yas_bilinmeyen = [], 0
    for did, son_commit, tok in con.execute("SELECT dosya_id, son_commit, token_kestirim FROM dosya WHERE katman='soguk' ORDER BY dosya_id"):
        if muaf_mi(did, muaf, oto) or did in kb_dosyalar or gelen.get(did, 0) > esik:
            continue
        y = yas_seans(seanslar, son_commit)
        if y is None:
            yas_bilinmeyen += 1; continue
        if y > min_yas:
            yet.append(did); S.kuyruga("T-B-YETIM", "dosya", did, did, "gelen bağ %d ≤ %d ∧ yaş %d seans > %d (≈%s token)" % (gelen.get(did, 0), esik, y, min_yas, tok), "bağlantılandır (pointer) ya da pointer'a indir — SİLME DEĞİL", y)
    S.ekle("T-B-YETIM", len(yet), yet, "yaşı bilinmeyen (son_commit boş): %d" % yas_bilinmeyen)
    # Karar 83 B1 (Salih 08-30): aday sayısı > uyarı eşiği (medyan×1,5) → WARN kanalı; hattı düşürmez, pencere birimi KOŞUM
    uyari_esigi = int(kural["yetim"].get("uyari_esigi", 0))
    if uyari_esigi:
        asim = len(yet) if len(yet) > uyari_esigi else 0
        S.ekle("T-B-YETIM-UYARI", asim, yet[:5] if asim else (), "aday %d / eşik %d (medyan 234 × 1,5; Karar 83 B1, m.29)" % (len(yet), uyari_esigi))
    # KAPANDI — karar_borcu kapandı ∧ kapanış > pencere
    kap = []
    for bid, kayit_tarihi, kanit in con.execute("SELECT borc_id, kayit_tarihi, kapanis_kaniti FROM karar_borcu WHERE durum='kapandı' ORDER BY borc_id"):
        kt = kapanis_tarihi(kanit, kayit_tarihi); y = yas_seans(seanslar, kt)
        if y is not None and y > pencere:
            kap.append(bid); S.kuyruga("T-B-KAPANDI", "karar_borcu", bid, None, "kapanış %s, %d seans önce" % (kt, y), "tarihçe etiketi (ledger'da kalır, m.8)", y)
    S.ekle("T-B-KAPANDI", len(kap), kap)


def t_a(con, S, kural, kosum_id):
    oe = kural["on_eleme"]; katmanlar = tuple(oe.get("katman", ["sicak"])); rx = re.compile(oe.get("sinyal_regex", r"\d"), re.I)
    min_uz = int(oe.get("min_uzunluk", 80)); maxk = int(oe.get("max_cift_kayit", 500))
    q = """SELECT r.ref_deger, k.kayit_id, k.dosya_id, k.blok_turu, k.metin FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id
           JOIN dosya d ON d.dosya_id=k.dosya_id WHERE r.ref_turu='anahtar_terim' AND d.katman IN (%s) AND LENGTH(k.metin)>=?
           ORDER BY r.ref_deger, k.kayit_id""" % ",".join("?" * len(katmanlar))
    grup = {}
    for at, kid, did, bt, metin in con.execute(q, katmanlar + (min_uz,)):
        if not rx.search(metin or ""):
            continue
        grup.setdefault(at, {}).setdefault(kid, (did, bt, len(metin)))
    ciftler = []
    for at in sorted(grup):
        kayitlar = sorted(grup[at].items())
        for i in range(len(kayitlar)):
            for j in range(i + 1, len(kayitlar)):
                (ka, (da, ba, la)), (kb, (db, bb, lb)) = kayitlar[i], kayitlar[j]
                if da == db or (oe.get("ayni_blok_turu", True) and ba != bb):
                    continue
                ciftler.append((at, ka, kb, da, db, ba, la, lb))
    rows = [("%s|%s|%s" % (c[0], c[1], c[2]), c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], kosum_id) for c in ciftler[:maxk]]
    con.executemany("INSERT OR REPLACE INTO silver_karantina_aday VALUES (%s)" % ",".join("?" * 10), rows)
    S.ekle("T-A-ONELEME", len(ciftler), ["%s|%s|%s" % (c[0], c[1], c[2]) for c in ciftler], "yazılan çift %d/%d (max_cift_kayit); LLM koşumu ayrı tetik" % (len(rows), len(ciftler)))


# ---------------------------------------------------------------- kuyruk olay kütüğü + yazım
def kuyruk_kutugu_oku(yol):
    """Olay kütüğünü yeniden oynat → açık kuyruk {anahtar: tespit_tarihi}."""
    acik = {}
    if not os.path.exists(yol):
        return acik
    with open(yol, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                o = json.loads(line)
            except json.JSONDecodeError:
                continue
            anahtar = "%s|%s|%s" % (o.get("tip"), o.get("hedef_tur"), o.get("hedef_id"))
            if o.get("olay") == "ACILDI":
                acik.setdefault(anahtar, o.get("tespit_tarihi") or (o.get("ts") or "")[:10])
            elif o.get("olay") == "KAPANDI":
                acik.pop(anahtar, None)
    return acik


def yaz(con, repo, S, kurallar, kosum_id, snapshot, head, ts, kuru, sessiz, kayit_dosyasi):
    siddet = {t["id"]: t.get("siddet", "warn") for t in kurallar["testler"]}
    ad = {t["id"]: t.get("ad", "") for t in kurallar["testler"]}
    sinif = {t["id"]: t.get("sinif", "") for t in kurallar["testler"]}
    # bayraklar → kayit.gecerlilik
    onceki = kuyruk_kutugu_oku(os.path.join(repo, KUYRUK_YOLU))
    con.execute("""UPDATE kayit SET gecerlilik = CASE WHEN (SELECT katman FROM dosya d WHERE d.dosya_id=kayit.dosya_id)='soguk' THEN 'tarihce' ELSE 'guncel' END,
                   gecerlilik_neden = NULL, tespit_tarihi = NULL""")
    for kid, (g, neden) in sorted(S.bayrak.items()):
        tespit = onceki.get("%s|kayit|%s" % ("T-B-MISLEADING", kid)) or onceki.get("%s|kayit|%s" % ("T-C3", kid)) or snapshot
        con.execute("UPDATE kayit SET gecerlilik=?, gecerlilik_neden=?, tespit_tarihi=? WHERE kayit_id=?", (g, neden, tespit, kid))
    # kuyruk tablosu + olaylar
    simdi = {}
    rows = []
    for q in S.kuyruk:
        anahtar = "%s|%s|%s" % (q["tip"], q["hedef_tur"], q["hedef_id"])
        if anahtar in simdi:
            continue
        tespit = onceki.get(anahtar, snapshot)
        try:
            yas_gun = (date.fromisoformat(snapshot) - date.fromisoformat(tespit)).days
        except ValueError:
            yas_gun = None
        simdi[anahtar] = tespit
        rows.append((anahtar, q["tip"], q["hedef_tur"], q["hedef_id"], q["dosya_id"], q["neden"], q["eylem"], tespit, yas_gun, q.get("yas_seans"),
                     siddet.get(q["tip"], "aday"), snapshot, kosum_id))
    con.executemany("INSERT OR REPLACE INTO silver_kuyruk VALUES (%s)" % ",".join("?" * 13), rows)
    acilan = sorted(set(simdi) - set(onceki)); kapanan = sorted(set(onceki) - set(simdi))
    # test sonuçları
    son_rows, log_rows, hata_var = [], [], False
    for test_id, ihlal, ornek, not_ in S.liste:
        sv = siddet.get(test_id, "warn")
        sonuc = "PASS" if ihlal == 0 else ("ERROR" if sv == "error" else ("WARN" if sv == "warn" else "ADAY"))
        if sonuc == "ERROR":
            hata_var = True
        son_rows.append((test_id, ad.get(test_id, ""), sinif.get(test_id, ""), sv, ihlal, sonuc, json.dumps(ornek, ensure_ascii=False), not_, kosum_id, snapshot, head))
        log_rows.append({"ts": ts, "kosum_id": kosum_id, "head": head, "snapshot": snapshot, "test_id": test_id, "sinif": sinif.get(test_id, ""),
                         "siddet": sv, "ihlal": ihlal, "ornek": ornek, "sonuc": sonuc, "not": not_})
    con.executemany("INSERT OR REPLACE INTO silver_saglik_son VALUES (%s)" % ",".join("?" * 11), son_rows)
    if not kuru:
        con.commit()
        with open(os.path.join(repo, LOG_YOLU), "a", encoding="utf-8") as fh:
            for r in log_rows:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        if acilan or kapanan:
            with open(os.path.join(repo, KUYRUK_YOLU), "a", encoding="utf-8") as fh:
                for a in acilan:
                    q = next(x for x in S.kuyruk if "%s|%s|%s" % (x["tip"], x["hedef_tur"], x["hedef_id"]) == a)
                    fh.write(json.dumps({"ts": ts, "kosum_id": kosum_id, "olay": "ACILDI", "tip": q["tip"], "hedef_tur": q["hedef_tur"], "hedef_id": q["hedef_id"],
                                         "neden": q["neden"], "tespit_tarihi": snapshot}, ensure_ascii=False) + "\n")
                for k in kapanan:
                    tip, ht, hid = k.split("|", 2)
                    fh.write(json.dumps({"ts": ts, "kosum_id": kosum_id, "olay": "KAPANDI", "tip": tip, "hedef_tur": ht, "hedef_id": hid,
                                         "neden": "bu koşumda aday değil (kaynak düzeldi ya da kural değişti)", "tespit_tarihi": onceki.get(k)}, ensure_ascii=False) + "\n")
        # CSV (gold; küçük görünümler)
        gdir = os.path.join(repo, "veri", "gorunum"); os.makedirs(gdir, exist_ok=True)
        for g in CSV_GORUNUMLER:
            cur = con.execute("SELECT * FROM %s" % g)
            with open(os.path.join(gdir, g + ".csv"), "w", encoding="utf-8", newline="") as fh:
                w = csv.writer(fh); w.writerow([d[0] for d in cur.description]); w.writerows(cur.fetchall())
    return son_rows, hata_var, len(acilan), len(kapanan)


# ---------------------------------------------------------------- canary (--test)
def canary(repo, ad_mod, kurallar):
    """Bilinen ihlal tohumlu geçici DB + geçici kayıt → ilgili testler FAIL vermeli. Gerçek DB/kütüğe yazmaz."""
    tmp = tempfile.mkdtemp(prefix="silver-saglik-canary-")
    db = os.path.join(tmp, "canary.sqlite"); con = sqlite3.connect(db)
    con.executescript("""
    CREATE TABLE dosya (dosya_id TEXT PRIMARY KEY, dizin TEXT, katman TEXT, tur TEXT, boyut_bytes INTEGER, satir_sayisi INTEGER, blob_sha TEXT,
      ilk_commit TEXT, son_commit TEXT, baslik TEXT, token_kestirim INTEGER, uzanti TEXT, okunabildi INTEGER);
    CREATE TABLE kayit (kayit_id TEXT PRIMARY KEY, dosya_id TEXT, sira INTEGER, bolum_yolu TEXT, blok_turu TEXT, satir_bas INTEGER, satir_son INTEGER,
      metin TEXT, metin_kisa TEXT, token_kestirim INTEGER, tarih_ipucu TEXT, tarih_iso TEXT, zarf_tip TEXT, zarf_kaynak TEXT, zarf_tarih TEXT,
      zarf_hedef TEXT, zarf_sema TEXT, zarf_onem TEXT, zarf_gecerli_bitis TEXT, zarf_json TEXT, madde_derinlik INTEGER);
    CREATE TABLE referans (kayit_id TEXT, ref_turu TEXT, ref_deger TEXT, ham TEXT, konum INTEGER, hedef_var INTEGER, hedef_yol TEXT);
    CREATE TABLE anahtar (anahtar_id TEXT PRIMARY KEY, tur TEXT, deger TEXT, kaynak_dosya TEXT, durum TEXT, replaced_by TEXT, gecerli_bas TEXT,
      gecerli_bitis TEXT, referans_sayisi INTEGER, sicak_referans_sayisi INTEGER, ilk_gorulme TEXT, son_gorulme TEXT);
    CREATE TABLE karar_borcu (borc_id TEXT PRIMARY KEY, baslik TEXT, kume TEXT, tur TEXT, katman INTEGER, karar_sahibi TEXT, durum TEXT, kayit_tarihi TEXT,
      yas_gun INTEGER, secenekler TEXT, oneri TEXT, bagimlilik TEXT, kapanis_kaniti TEXT, masa_sirasi INTEGER, yururluk_aninda TEXT, icra_borcu TEXT,
      not_ TEXT, kaynak_sayisi INTEGER, snapshot_tarih TEXT, snapshot_sha TEXT);
    CREATE TABLE karar_borcu_kaynak (borc_id TEXT, sira INTEGER, dosya TEXT, satir INTEGER, metin TEXT, dosya_var INTEGER, satir_var INTEGER, kayit_id TEXT);
    CREATE VIEW v_celiski_adayi AS
    SELECT r.ref_deger AS anahtar_terim, k.dosya_id,
       SUM(CASE WHEN k.zarf_gecerli_bitis IS NOT NULL AND k.zarf_gecerli_bitis<>'' AND k.zarf_gecerli_bitis<>'-' THEN 1 ELSE 0 END) AS bitisli,
       SUM(CASE WHEN k.zarf_gecerli_bitis IS NULL OR k.zarf_gecerli_bitis='' OR k.zarf_gecerli_bitis='-' THEN 1 ELSE 0 END) AS bitissiz
    FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id WHERE r.ref_turu='anahtar_terim' AND k.zarf_json IS NOT NULL
    GROUP BY r.ref_deger, k.dosya_id HAVING bitisli>0 AND bitissiz>0;
    """)
    con.execute("INSERT INTO dosya VALUES ('core/x.md','core','sicak','md',1,1,'s','2026-08-01','2026-08-01','X',10,'.md',1)")
    con.execute("INSERT INTO dosya VALUES ('cc/soguk-eski.md','cc','soguk','md',1,1,'s','2026-07-01','2026-07-01','EskI',10,'.md',1)")
    con.execute("INSERT INTO dosya VALUES ('wiki/emekli-sayfa.md','wiki','ilik','md',1,1,'s','2026-07-01','2026-07-01','EMEKLİ AD → yeni',10,'.md',1)")
    con.execute("INSERT INTO kayit (kayit_id,dosya_id,sira,blok_turu,metin) VALUES ('k1','core/x.md',1,'paragraf','Bugün günaydın ile açılış yapılır.')")  # emekli kalıntı (izinsiz)
    con.execute("INSERT INTO kayit (kayit_id,dosya_id,sira,blok_turu,metin,zarf_json,zarf_gecerli_bitis) VALUES ('k2','core/x.md',2,'paragraf','kapsul kuralı 1 = zorunlu','{}','2026-08-01')")
    con.execute("INSERT INTO kayit (kayit_id,dosya_id,sira,blok_turu,metin,zarf_json,zarf_gecerli_bitis) VALUES ('k3','core/x.md',3,'paragraf','kapsul kuralı 2 = yasak','{}','')")
    con.execute("INSERT INTO referans VALUES ('k2','anahtar_terim','kapsul','kapsul',0,NULL,NULL)")
    con.execute("INSERT INTO referans VALUES ('k3','anahtar_terim','kapsul','kapsul',0,NULL,NULL)")
    con.execute("INSERT INTO karar_borcu (borc_id,baslik,durum,kayit_tarihi,bagimlilik,kapanis_kaniti) VALUES ('KB-1','Aynı kalem','masaya','2026-08-01','KB-9','')")
    con.execute("INSERT INTO karar_borcu (borc_id,baslik,durum,kayit_tarihi,bagimlilik,kapanis_kaniti) VALUES ('KB-2','aynı  kalem','icra-sırada','2026-08-01','','Karar 5: A')")
    con.execute("INSERT INTO karar_borcu (borc_id,baslik,durum,kayit_tarihi,bagimlilik,kapanis_kaniti) VALUES ('KB-3','Eski','kapandı','2026-07-01','','07-02 kapandı')")
    con.commit()
    reg = {"anahtarlar": [
        {"anahtar_id": "oturum-acilis-tetigi", "tur": "tetik", "guncel": {"deger": "seans başı", "gecerli_bas": "2026-08-15"},
         "emekli": [{"deger": "günaydın", "varyantlar": [], "tarih": "2026-08-16", "replaced_by": "seans başı", "izinli_kaliplar": ["günaydın vardiyası"]}]},  # T-C2: 08-16 > 08-15
        {"anahtar_id": "cift-guncel", "tur": "kavram", "guncel": {"deger": "a", "gecerli_bas": ""}, "emekli": []},  # T-C1 damgasız
    ]}
    kurallar = json.loads(json.dumps(kurallar)); kurallar["pencere"]["deger"] = 1; kurallar["yetim"]["min_yas_seans"] = 1
    S = Sonuclar(kurallar)
    sema_hazirla(con)
    anahtar_kaydini_yukle(con, reg, ad_mod, "canary")
    t_c1_c2(con, S); t_c3(con, S, reg, ad_mod, kurallar); t_c4(con, S); t_c5(con, S)
    t_b(con, S, kurallar, ["2026-08-10", "2026-08-20"], "2026-08-22")
    t_a(con, S, kurallar, "canary")
    got = {t: n for t, n, _o, _n in S.liste}
    beklenen = {"T-C1": 1, "T-C2": 1, "T-C3-sicak": 1, "T-C4a": 2, "T-C4b": 1, "T-C4c": 1, "T-C5": 1, "T-B-SUPERSEDED": 1, "T-B-YETIM": 1, "T-B-KAPANDI": 1, "T-B-MISLEADING": 2}
    fail = [(t, b, got.get(t)) for t, b in beklenen.items() if got.get(t) != b]
    ok = not fail
    print("=== silver-saglik CANARY (tohumlu ihlal → test FAIL vermeli) ===")
    for t in sorted(beklenen):
        print("  [%s] %-16s beklenen ihlal %d · bulunan %s" % ("PASS" if got.get(t) == beklenen[t] else "FAIL", t, beklenen[t], got.get(t)))
    print("  CANARY %s" % ("PASS" if ok else "FAIL: %s" % fail))
    con.close(); shutil.rmtree(tmp, ignore_errors=True)
    return ok


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description="silver sağlık: bayrak + güncel görünüm + kuyruk (Karar 58)")
    ap.add_argument("--repo", default=os.getcwd())
    ap.add_argument("--kapi", action="store_true", help="T-Ç error ihlalinde çıkış 6 (seans-kapanis/damitma kapısı); yoksa uyarı modu")
    ap.add_argument("--sessiz", action="store_true", help="yalnız özet satırı (stdout) + ihlaller (stderr, uyarı kanalı)")
    ap.add_argument("--kuru", action="store_true", help="DB/kütük yazma (geçici kopyada hesapla)")
    ap.add_argument("--snapshot", default=date.today().isoformat(), help="tespit/snapshot tarihi (deterministik koşum için sabitle)")
    ap.add_argument("--test", action="store_true", help="canary: tohumlu ihlal DB'sinde testler FAIL vermeli")
    ap.add_argument("--json", action="store_true", help="sonuçları JSON yaz")
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)
    ad_mod = anahtar_denetim_modulu(repo)
    kurallar = kurallari_oku(repo)
    if a.test:
        sys.exit(0 if canary(repo, ad_mod, kurallar) else 7)
    db = os.path.join(repo, "veri", "baglam.sqlite")
    if not os.path.exists(db):
        sys.exit("[HATA] silver yok: veri/baglam.sqlite (önce tools/katman-hatti.py)")
    reg = ad_mod.load_registry(os.path.join(repo, KAYIT_YOLU))
    butunluk = ad_mod.integrity(reg)
    calis_db = db
    tmp = None
    if a.kuru:
        tmp = tempfile.mkdtemp(prefix="silver-saglik-kuru-"); calis_db = os.path.join(tmp, "baglam.sqlite"); shutil.copyfile(db, calis_db)
    con = sqlite3.connect(calis_db)
    mevcut = {r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type IN ('table','view')")}
    eksik = [t for t in ("dosya", "kayit", "referans", "anahtar", "karar_borcu", "karar_borcu_kaynak", "v_celiski_adayi") if t not in mevcut]
    if eksik:
        sys.exit("[HATA] silver eksik nesne: %s (önceki hat adımı düşmüş olabilir — tools/katman-hatti.py çıktısına bak)" % ", ".join(eksik))
    head = git_head(repo)
    try:
        u = con.execute("SELECT kayit_id_kume_sha, git_head_sha FROM uretim ORDER BY uretim_zamani DESC LIMIT 1").fetchone()
    except sqlite3.Error:
        u = None
    girdi_sha = (u[0] if u else "?")
    with open(os.path.abspath(__file__), "rb") as fh:
        kod_sha = sha1_hex(fh.read())[:8]
    kosum_id = sha1_hex(("%s|%s|%s|%s" % (head, girdi_sha, a.snapshot, kod_sha)).encode())[:10]
    ts = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    seanslar = seans_tarihleri(repo)
    S = Sonuclar(kurallar)
    sema_hazirla(con)
    n_kaydi = anahtar_kaydini_yukle(con, reg, ad_mod, KAYIT_YOLU)
    t_c1_c2(con, S); t_c3(con, S, reg, ad_mod, kurallar); t_c4(con, S); t_c5(con, S); t_c6(repo, S, kurallar)
    t_b(con, S, kurallar, seanslar, a.snapshot); t_a(con, S, kurallar, kosum_id)
    if butunluk:
        S.ekle("T-C1", S.liste[0][1] + len(butunluk), S.liste[0][2] + butunluk, "anahtar-denetim bütünlük hataları dahil")
        S.liste.pop(0)
    son_rows, hata_var, n_acilan, n_kapanan = yaz(con, repo, S, kurallar, kosum_id, a.snapshot, head, ts, a.kuru, a.sessiz, KAYIT_YOLU)
    n_guncel = con.execute("SELECT COUNT(*) FROM v_guncel_kayit").fetchone()[0]
    n_bayrak = con.execute("SELECT COUNT(*) FROM kayit WHERE gecerlilik NOT IN ('guncel','tarihce')").fetchone()[0]
    n_kuyruk = con.execute("SELECT COUNT(*) FROM silver_kuyruk").fetchone()[0]
    con.close()
    if tmp:
        shutil.rmtree(tmp, ignore_errors=True)
    ozet = ("silver-saglik: koşum %s @ %s · anahtar_kaydi %d satır · v_guncel_kayit %d · bayraklı kayit %d · kuyruk %d (yeni %d · kapanan %d) · "
            "testler %d (ERROR %d · WARN %d · ADAY %d) · mod %s%s") % (
        kosum_id, head, n_kaydi, n_guncel, n_bayrak, n_kuyruk, n_acilan, n_kapanan, len(son_rows),
        sum(1 for r in son_rows if r[5] == "ERROR"), sum(1 for r in son_rows if r[5] == "WARN"), sum(1 for r in son_rows if r[5] == "ADAY"),
        "KAPI" if a.kapi else "uyarı", " · KURU" if a.kuru else "")
    if a.json:
        print(json.dumps({"ozet": ozet, "testler": [dict(zip(("test_id", "ad", "sinif", "siddet", "ihlal", "sonuc", "ornek", "not"), r[:8])) for r in son_rows]}, ensure_ascii=False, indent=1))
    else:
        print(ozet)
        if not a.sessiz:
            for r in son_rows:
                print("  [%-5s] %-16s %-8s ihlal %-5d %s %s" % (r[5], r[0], r[3], r[4], (r[1] or "")[:70], ("· " + r[7]) if r[7] else ""))
    for r in son_rows:
        if r[5] in ("ERROR", "WARN"):
            print("%s %s ihlal %d örnek %s" % (r[5], r[0], r[4], r[6][:200]), file=sys.stderr)
    sys.exit(6 if (a.kapi and hata_var) else 0)


if __name__ == "__main__":
    main()
