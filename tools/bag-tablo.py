#!/usr/bin/env python3
"""bag-tablo.py — TİPLİ-BAĞ KATMANI, ilk adım (KB-61 → Karar 74 M-1 (b), 2026-08-29): silver `bag` tablosu — STDLIB ONLY, deterministik.

Hüküm (Salih, Karar 74 M-1): tipli-bağ ilk adım YALNIZ süpersede (`prov:wasRevisionOf`) + bitemporal alan; silver additive; tip
ataması KURAL-tabanlı (LLM atamaz — Karar 65 determinizm). Destek/itiraz/genişletme (CiTO) ve türetme (OpenLineage) tipleri SONRA
(ihtiyaç İB-48 odak panolarında görülünce; masa Salih tetiğinde).

Grain: 1 satır = 1 TİPLİ BAĞ (kaynak → hedef); yön PROV: KAYNAK = yeni sürüm, HEDEF = eski sürüm ("kaynak wasRevisionOf hedef").
Kurallar (deterministik; her satır `kural` kolonunda kimliğini taşır):
  R1 anahtar-kaydı emekliliği : anahtar_kaydi(rol=guncel) → anahtar_kaydi(rol=emekli, replaced_by=güncel değer), aynı anahtar_id.
                                gecerli_bas = emeklinin gecerli_bitis günü (takas günü). Kaynak: core/baglam-anahtar-kaydi.md §3.
  R2 anahtar.replaced_by      : anahtar(replaced_by hedefi) → anahtar(eski) (SCD-2; bugün 0 satır — alan boş; kural hazır durur).
  R3 damıtma arşiv-pointer'ı  : sıcak/ılık dosyadaki index satırı (kayit; metin 'ARŞİVE İNDİ' | 'arşive indi' | 'tam metin' |
                                'Arşiv index' | 'arşivi' içerir) → `kuyruk/arsiv/...` hedefi (satır çözülürse kayit, yoksa dosya).
                                gecerli_bas = arşiv dosya adındaki tarih (damıtma günü). Kaynak dosya arşiv/raporlar/cc DEĞİL.
Bitemporal (M4 / KB-61): gecerli_bas / gecerli_bitis = OLAY zamanı (valid) · kayit_zamani / gecersiz_zamani = KAYIT zamanı (transaction;
  ilk ACILDI ts / KAPANDI ts — kütük `veri/bag-olay.jsonl` append-only yeniden-oynatılır, silver-kuyruk deseni Karar 58).
  as-of(t_v, t_k) = gecerli_bas ≤ t_v ∧ (gecerli_bitis IS NULL ∨ gecerli_bitis > t_v) ∧ kayit_zamani ≤ t_k ∧ (gecersiz_zamani IS NULL ∨ > t_k).
  Bu koşumda türetilmeyen ama kütükte açık bağ → KAPANDI olayı + tabloda gecersiz_zamani dolu satır olarak KALIR (silme yok, m.8).
Çıktı: silver `bag` (+ `v_bag`, `v_bag_ozet`) · gold veri/gorunum/v_bag.csv, v_bag_ozet.csv · kütük veri/bag-olay.jsonl.
Graf: tools/pointer-graf.py `bag` satırlarını tablo→tablo kenarı (tip etiketli) olarak panoya ve kenar listesine taşır.
Kullanım: python3 tools/bag-tablo.py [--repo <yol>] [--sessiz] [--kuru]   (hat adımı `bag`: saglik SONRASI, erisim ÖNCESİ)
Çıkış: 0 tamam · 2 DB yok/gerekli tablo yok. Deneysel m.29 (2026-08-29, Carvis, yan icra oturumu). Additive-only.
"""
import argparse, csv, hashlib, json, os, re, sqlite3, subprocess, sys
from datetime import datetime, timezone, timedelta

TIP = "wasRevisionOf"
KUTUK = os.path.join("veri", "bag-olay.jsonl")
RX_ARSIV = re.compile(r"ARŞİVE İNDİ|arşive indi|tam metin|Arşiv index|arşivi\b", re.U)
RX_TARIH = re.compile(r"(\d{4}-\d{2}-\d{2})")
DDL = """
CREATE TABLE IF NOT EXISTS bag (
  bag_id TEXT PRIMARY KEY, tip TEXT, kaynak_tur TEXT, kaynak_id TEXT, hedef_tur TEXT, hedef_id TEXT, kural TEXT,
  gecerli_bas TEXT, gecerli_bitis TEXT, kayit_zamani TEXT, gecersiz_zamani TEXT,
  aciklama TEXT, kaynak_dosya TEXT, kod_sha TEXT, snapshot_tarih TEXT, kosum_id TEXT
);
CREATE INDEX IF NOT EXISTS ix_bag_kaynak ON bag(kaynak_tur, kaynak_id);
CREATE INDEX IF NOT EXISTS ix_bag_hedef ON bag(hedef_tur, hedef_id);
"""
GORUNUMLER = [
    ("v_bag", "SELECT * FROM bag ORDER BY kural, kaynak_id, hedef_id"),
    ("v_bag_ozet", "SELECT kural, tip, kaynak_tur, hedef_tur, COUNT(*) AS n, SUM(gecersiz_zamani IS NULL) AS acik, MIN(gecerli_bas) AS en_eski_olay, MAX(gecerli_bas) AS en_yeni_olay FROM bag GROUP BY 1,2,3,4 ORDER BY 1"),
]


def bag_id(tip, kt, ki, ht, hi):
    return hashlib.sha1(("%s|%s|%s|%s|%s" % (tip, kt, ki, ht, hi)).encode("utf-8")).hexdigest()[:12]


def kural_r1(con):
    out = []
    rows = con.execute("SELECT kaydi_id, anahtar_id, rol, deger, replaced_by, gecerli_bas, gecerli_bitis FROM anahtar_kaydi").fetchall()
    guncel = {(r[1], r[3]): r for r in rows if r[2] == "guncel"}
    for r in rows:
        if r[2] != "emekli" or not r[4]:
            continue
        g = guncel.get((r[1], r[4]))
        if not g:
            continue
        out.append(("anahtar_kaydi", g[0], "anahtar_kaydi", r[0], "R1", (r[6] or g[5] or "")[:10] or None,
                    "%s: '%s' → '%s' (emeklilik takası)" % (r[1], r[3], r[4]), "core/baglam-anahtar-kaydi.md"))
    return out


def kural_r2(con):
    out = []
    for aid, rep, bitis in con.execute("SELECT anahtar_id, replaced_by, gecerli_bitis FROM anahtar WHERE replaced_by IS NOT NULL AND replaced_by<>''"):
        out.append(("anahtar", rep, "anahtar", aid, "R2", (bitis or "")[:10] or None, "anahtar.replaced_by (SCD-2)", "veri/baglam.sqlite anahtar"))
    return out


def kural_r3(con):
    out, gorulen = [], set()
    sql = """SELECT k.kayit_id, k.dosya_id, r.ref_deger, r.hedef_yol, k.metin, k.cekim_tarihi
             FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id
             WHERE r.ref_turu='dosya_pointer' AND r.hedef_var=1 AND r.hedef_yol LIKE 'kuyruk/arsiv/%'
               AND k.dosya_id NOT LIKE 'kuyruk/arsiv/%' AND k.dosya_id NOT LIKE 'raporlar/%' AND k.dosya_id NOT LIKE 'cc/%'
             ORDER BY k.kayit_id, r.konum"""
    for kid, dosya, ref, hedef, metin, cekim in con.execute(sql).fetchall():
        if not RX_ARSIV.search(metin or ""):
            continue
        satir = None
        m = re.search(r":(\d+)(?:-\d+)?\s*$", (ref or "").strip().strip("`"))
        if m:
            satir = int(m.group(1))
        htur, hid = "dosya", hedef
        if satir is not None:
            r = con.execute("SELECT kayit_id FROM kayit WHERE dosya_id=? AND satir_bas<=? AND satir_son>=? ORDER BY sira LIMIT 1", (hedef, satir, satir)).fetchone()
            if r:
                htur, hid = "kayit", r[0]
        anahtar = (kid, htur, hid)
        if anahtar in gorulen:
            continue
        gorulen.add(anahtar)
        mt = RX_TARIH.search(os.path.basename(hedef))
        out.append(("kayit", kid, htur, hid, "R3", mt.group(1) if mt else (cekim or None),
                    "damıtma index satırı → arşiv (%s)" % (ref or "").strip("`")[:80], dosya))
    return out


def kutuk_oku(yol):
    """Yeniden oynat → {bag_id: (ilk ACILDI ts, son olay, kapanış ts, ham satır)}."""
    durum = {}
    if not os.path.exists(yol):
        return durum
    with open(yol, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                o = json.loads(line)
            except json.JSONDecodeError:
                continue
            b = o.get("bag_id")
            if not b:
                continue
            if o.get("olay") == "ACILDI":
                d = durum.get(b)
                durum[b] = (d[0] if d else o.get("ts"), "ACILDI", None, o)
            elif o.get("olay") == "KAPANDI" and b in durum:
                durum[b] = (durum[b][0], "KAPANDI", o.get("ts"), durum[b][3])
    return durum


def main():
    ap = argparse.ArgumentParser(description="tipli-bağ katmanı (KB-61 b): silver bag + bitemporal kütük")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--sessiz", action="store_true"); ap.add_argument("--kuru", action="store_true")
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)
    db = os.path.join(repo, "veri", "baglam.sqlite")
    if not os.path.exists(db):
        print("HATA: silver yok: veri/baglam.sqlite (önce baglam-tablo.py)", file=sys.stderr); return 2
    con = sqlite3.connect(db)
    tablolar = {r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    if not {"anahtar", "anahtar_kaydi", "kayit", "referans"} <= tablolar:
        print("HATA: gerekli tablolar eksik (anahtar/anahtar_kaydi/kayit/referans) — hat sırası: saglik SONRASI", file=sys.stderr); return 2
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip() or "-"
    ts = datetime.now(timezone(timedelta(hours=3))).replace(microsecond=0).isoformat()
    snapshot = ts[:10]; kosum_id = "bag:%s:%s" % (head, snapshot)
    turetilen = kural_r1(con) + kural_r2(con) + kural_r3(con)
    turetilen.sort(key=lambda r: (r[4], r[1], r[3]))
    kutuk_yolu = os.path.join(repo, KUTUK)
    onceki = kutuk_oku(kutuk_yolu)
    rows, olaylar, simdi = [], [], set()
    for kt, ki, ht, hi, kural, bas, acik, dosya in turetilen:
        b = bag_id(TIP, kt, ki, ht, hi); simdi.add(b)
        d = onceki.get(b)
        if d is None or d[1] == "KAPANDI":  # yeni ya da yeniden açılan
            olaylar.append({"ts": ts, "olay": "ACILDI", "bag_id": b, "tip": TIP, "kaynak_tur": kt, "kaynak_id": ki, "hedef_tur": ht, "hedef_id": hi,
                            "kural": kural, "gecerli_bas": bas, "kod_sha": head, "kosum_id": kosum_id})
            kayit_z = ts
        else:
            kayit_z = d[0]
        rows.append((b, TIP, kt, ki, ht, hi, kural, bas, None, kayit_z, None, acik, dosya, head, snapshot, kosum_id))
    for b, d in sorted(onceki.items()):
        if b in simdi or d[1] == "KAPANDI":
            if b not in simdi and d[1] == "KAPANDI":  # geçmişte kapanmış: tabloda tarihçe satırı olarak kalır
                o = d[3]; rows.append((b, o.get("tip", TIP), o.get("kaynak_tur"), o.get("kaynak_id"), o.get("hedef_tur"), o.get("hedef_id"), o.get("kural"),
                                       o.get("gecerli_bas"), None, d[0], d[2], "KAPANDI (kütük): bu koşumda türetilmedi", None, head, snapshot, kosum_id))
            continue
        o = d[3]  # açık ama artık türetilmiyor → KAPANDI
        olaylar.append({"ts": ts, "olay": "KAPANDI", "bag_id": b, "tip": o.get("tip", TIP), "kaynak_tur": o.get("kaynak_tur"), "kaynak_id": o.get("kaynak_id"),
                        "hedef_tur": o.get("hedef_tur"), "hedef_id": o.get("hedef_id"), "kural": o.get("kural"), "kod_sha": head, "kosum_id": kosum_id,
                        "neden": "bu koşumda kural türetmedi (kaynak değişti ya da kural değişti)"})
        rows.append((b, o.get("tip", TIP), o.get("kaynak_tur"), o.get("kaynak_id"), o.get("hedef_tur"), o.get("hedef_id"), o.get("kural"),
                     o.get("gecerli_bas"), None, d[0], ts, "KAPANDI: bu koşumda türetilmedi", None, head, snapshot, kosum_id))
    if a.kuru:
        print("bag (kuru): %d bağ (R1 %d · R2 %d · R3 %d) · yeni ACILDI %d · KAPANDI %d" % (
            len(rows), sum(1 for r in turetilen if r[4] == "R1"), sum(1 for r in turetilen if r[4] == "R2"), sum(1 for r in turetilen if r[4] == "R3"),
            sum(1 for o in olaylar if o["olay"] == "ACILDI"), sum(1 for o in olaylar if o["olay"] == "KAPANDI")))
        return 0
    con.executescript("DROP TABLE IF EXISTS bag;" + DDL)
    con.executemany("INSERT INTO bag VALUES (%s)" % ",".join("?" * 16), rows)
    for ad, sql in GORUNUMLER:
        con.execute("DROP VIEW IF EXISTS %s" % ad); con.execute("CREATE VIEW %s AS %s" % (ad, sql))
    con.commit()
    gd = os.path.join(repo, "veri", "gorunum"); os.makedirs(gd, exist_ok=True)
    for ad, _ in GORUNUMLER:
        cur = con.execute("SELECT * FROM %s" % ad); kol = [c[0] for c in cur.description]
        with open(os.path.join(gd, ad + ".csv"), "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh, lineterminator="\n"); w.writerow(kol)
            for r in cur.fetchall():
                w.writerow(["" if v is None else v for v in r])
    con.close()
    if olaylar:
        with open(kutuk_yolu, "a", encoding="utf-8") as fh:
            for o in olaylar:
                fh.write(json.dumps(o, ensure_ascii=False) + "\n")
    if not a.sessiz:
        print("bag: %d bağ (R1 %d · R2 %d · R3 %d) · açık %d · yeni ACILDI %d · KAPANDI %d · kütük %s · gold v_bag.csv/v_bag_ozet.csv" % (
            len(rows), sum(1 for r in rows if r[6] == "R1"), sum(1 for r in rows if r[6] == "R2"), sum(1 for r in rows if r[6] == "R3"),
            sum(1 for r in rows if r[10] is None), sum(1 for o in olaylar if o["olay"] == "ACILDI"), sum(1 for o in olaylar if o["olay"] == "KAPANDI"), KUTUK))
    return 0


if __name__ == "__main__":
    sys.exit(main())
