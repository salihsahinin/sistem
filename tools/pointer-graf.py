#!/usr/bin/env python3
"""pointer-graf.py — Jarvis POINTER SİSTEMİNİN grafını silver'dan DETERMİNİSTİK türetir (P0/P2, pipeline
cc/pipeline-2026-08-22-pointer-graf-d2.md; Salih emri 08-22 "pointer sistemimizin … graflar için güncel dosya tipinde grafını oluştur").

Ne yapar: veri/baglam.sqlite'ı okur → graf MODELİ (düğüm/kenar, tipli) → veri/graf/pointer-sistemi-model.json
          + --d2 ile şema-düzeyi D2 dosyası (graf/pointer-sistemi-v0.d2) üretir. Aynı silver → aynı çıktı
          (düğüm/kenar sabit sırada; zaman damgası yalnız meta alanında, gövdede yok — git-diff dostu).
Ne yapmaz: graf MOTORU kurmaz (world-model: taban ilişkisel kalır); LLM çağırmaz (Karar 65 determinizm);
          render etmez (render = `d2 --layout=elk graf/pointer-sistemi-v0.d2 graf/pointer-sistemi-v0.svg`, çağıran koşar).
Düğüm türleri: tablo (silver; PK sütunları + satır sayısı) · referans_turu (11) · anahtar_turu (6) · dosya_katmani (4) ·
          hat_katmani (bronz/silver/gold) · ilke (m.20/21/22/8 — kanon SABİTİ, pointer'lı) · kronoloji (kuruluş adımları — kanon SABİTİ).
Kenar türleri: fk (PK→FK) · pointer_hedef (referans türü → hedef sınıfı; çözümlü/kırık sayısı) · supersede (anahtar.replaced_by) ·
          turetir (bronz→silver→gold; uretim provenansı) · ilke_uygular (ilke → mekanizma) · kronoloji_sonra (adım → adım).
Çıkış kodu: 0 tamam · 2 DB yok/okunamadı · 3 boş tablo · 4 render determinizmi BOZUK (FAIL-LOUD).
Kullanım: python3 tools/pointer-graf.py [--db veri/baglam.sqlite] [--json veri/graf/pointer-sistemi-model.json] [--d2 graf/pointer-sistemi-v0.d2]
"""
import argparse, json, os, sqlite3, subprocess, sys, datetime

# ---- kanon SABİTLERİ (elle; her biri kaynak pointer'lı — silver'dan türetilemeyen ilke/kronoloji bilgisi) ----
ILKELER = [
    ("m20", "m.20 pointer ilkesi", "özet + ADRES; detay sıcak bağlama taşınmaz, karar anında pointer izlenir", "core/tuzuk-v0.md m.20 · wiki/pointer-sistemi.md"),
    ("m21", "m.21 dönüş yolu", "özet kısalır, pointer DÜŞMEZ (bağlam-detay ölçekleme)", "core/tuzuk-v0.md m.21"),
    ("m22", "m.22 arşiv pointer", "bayat kayıt silinmez, arşive iner, pointer arşiv adresine güncellenir", "core/tuzuk-v0.md m.22"),
    ("m8",  "m.8 silme yasağı → süpersede", "kayıt silinmez; yeni kayıt eskisini süpersede eder (anahtar.replaced_by, SCD-2)", "core/tuzuk-v0.md m.8 · core/baglam-anahtar-kaydi.md §3"),
    ("adres", "adresli-erişim kuralı (08-18)", "kayit_id = yol#satır#sha8 → SEARCH USING INDEX; tarif+testler+hijyen, sarmalayıcı yok", "KILAVUZ.md tasarım-ilkeleri · kuyruk/senaryo-defteri.md Karar 62"),
]
KRONOLOJI = [
    ("k0711", "2026-07-11", "tüzük m.20-22 imzalandı (pointer ilkesi kanon)", "core/tuzuk-v0.md"),
    ("k0712", "2026-07-12", "PAT kararı: yalnız pointer izlendi — kanonik örnek", "wiki/pointer-sistemi.md"),
    ("k0718", "2026-07-18", "pointerlar-arası iletişim raporu: typed-link graf Model A ÖNERİ (karar yok)", "raporlar/2026-07-18-pointer-sistemi-iletisim-kategorizasyon.md"),
    ("k0724", "2026-07-24", "graf-mühendisliği raporu: %92,5 graf-yetim; elle index bayatlar → türetilmiş", "raporlar/2026-07-24-serit2-graph-engineering.md"),
    ("k0815", "2026-08-15", "silver katmanı: kayit_id adres PK, referans/anahtar tabloları (veri katmanı v1)", "cc/pipeline-2026-08-15-baglam-silver-katmani.md · veri/README.md"),
    ("k0817", "2026-08-17", "hafıza mimarisi Beyan 9 (wiki + veri teknikleri; vektör ertelendi)", "kuyruk/arsiv/senaryo-defteri-arsiv-2026-08-21.md:26"),
    ("k0818", "2026-08-18", "adresli-erişim kuralı + tarama/kolon katmanları (Karar 62-64)", "kuyruk/senaryo-defteri.md:173-175"),
    ("k0822", "2026-08-22", "pointer sisteminin grafı (D2) — bu türetim; Karar 65 determinizm-önceliği", "cc/pipeline-2026-08-22-pointer-graf-d2.md"),
]
# referans türü → hedef sınıfı (pointer'ın NEREYE çözüldüğü)
REF_HEDEF = {
    "dosya_pointer": ("dosya", "yol → dosya (hedef_var ile çözümlü/kırık)"),
    "wiki_link": ("anahtar_turu:wiki_sayfa", "[[sayfa]] → wiki sayfası (anahtar kaydı)"),
    "tuzuk_madde": ("anahtar_turu:tuzuk_madde", "m.N → tüzük maddesi (anahtar kaydı)"),
    "v_no": ("anahtar_turu:v_no", "V-n → kural/öneri numarası (anahtar kaydı)"),
    "kart": ("anahtar_turu:kart", "K-NNN → pano kartı (anahtar kaydı)"),
    "skill_adi": ("anahtar_turu:skill", "skill adı → hazine"),
    "anahtar_terim": ("anahtar_turu:anahtar_terim", "terim → anahtar kaydı"),
    "url": ("dis:url", "dış kaynak (repo dışı)"),
    "sha": ("dis:git", "git commit/blob (provenans)"),
    "tarih": ("dis:zaman", "zaman damgası (as-of)"),
    "etiket": ("dis:etiket", "#etiket (serbest sınıflandırma)"),
}
FK = [  # (kaynak_tablo.sütun, hedef_tablo.sütun)
    ("kayit.dosya_id", "dosya.dosya_id"),
    ("referans.kayit_id", "kayit.kayit_id"),
    ("referans.hedef_yol", "dosya.dosya_id"),
    ("karar_borcu_kaynak.borc_id", "karar_borcu.borc_id"),
    ("karar_borcu_kaynak.dosya_id", "dosya.dosya_id"),
    ("karar_borcu_kaynak.kayit_id", "kayit.kayit_id"),
    ("json_kayit.dosya_id", "dosya.dosya_id"),
    ("anahtar.replaced_by", "anahtar.anahtar_id"),
]
TABLO_PK = {"kayit": "kayit_id", "dosya": "dosya_id", "referans": None, "anahtar": "anahtar_id",
            "karar_borcu": "borc_id", "karar_borcu_kaynak": None, "hareket": "hareket_id", "prompt": "prompt_id",
            "json_kayit": None, "uretim": None}
GOSTER_SUTUN = {  # şema-düzeyi D2'de gösterilecek sütunlar (hepsi değil — okunurluk)
    "kayit": ["kayit_id", "dosya_id", "sira", "bolum_yolu", "satir_bas", "satir_son", "zarf_tip"],
    "dosya": ["dosya_id", "dizin", "katman", "tur", "blob_sha", "son_commit"],
    "referans": ["kayit_id", "ref_turu", "ref_deger", "hedef_var", "hedef_yol"],
    "anahtar": ["anahtar_id", "tur", "deger", "durum", "replaced_by", "gecerli_bas", "gecerli_bitis"],
    "karar_borcu": ["borc_id", "tur", "durum", "bagimlilik"],
    "karar_borcu_kaynak": ["borc_id", "dosya_id", "satir", "kayit_id"],
    "hareket": ["hareket_id", "oturum_id", "arac", "dosya", "yuklendi_head"],
    "prompt": ["prompt_id", "oturum_id", "sonraki_skill", "yuklendi_head"],
    "json_kayit": ["dosya_id", "json_yolu", "deger"],
    "uretim": ["uretim_zamani", "git_head_sha", "script_sha", "kayit_id_kume_sha"],
}

def tr(n):  # 48957 → "48.957"
    return f"{n:,}".replace(",", ".")

def q(cur, sql):
    return cur.execute(sql).fetchall()

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--db", default="veri/baglam.sqlite")
    ap.add_argument("--json", default="veri/graf/pointer-sistemi-model.json")
    ap.add_argument("--d2", default=None, help="TAM şema-düzeyi tek-pano D2 (ör. graf/pointer-sistemi-v0-tam.d2) — büyük, arşiv amaçlı")
    ap.add_argument("--d2-dizin", default=None, help="ÇOK-PANOLU çıktı dizini: genel + silver + pointer + ilke + kronoloji (ör. graf/) — okunur kademeleme")
    ap.add_argument("--render", type=int, default=0, metavar="N", help="panoları d2 --layout=elk ile SVG'ye çevir; N≥2 ise her panoyu N kez render edip sha256 eşitliğini ölç (Karar 65 kaydı) → graf/pointer-sistemi-v0-uretim.json")
    ap.add_argument("--kenar-listesi", default=None, help="LLM-okunur düz kenar listesi (script-üretimli, deterministik; ör. graf/pointer-sistemi-v0-kenarlar.txt)")
    ap.add_argument("--sessiz", action="store_true")
    a = ap.parse_args()
    if not os.path.exists(a.db):
        print(f"HATA: DB yok: {a.db}", file=sys.stderr); return 2
    con = sqlite3.connect(a.db); cur = con.cursor()
    try:
        tablolar = [r[0] for r in q(cur, "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
    except Exception as e:
        print(f"HATA: DB okunamadı: {e}", file=sys.stderr); return 2
    nodes, edges = [], []
    def node(nid, kind, label, **props):
        nodes.append({"id": nid, "kind": kind, "label": label, **props})
    def edge(src, etype, dst, label="", **props):
        edges.append({"from": src, "type": etype, "to": dst, "label": label, **props})

    # --- tablolar (silver) ---
    sayim = {}
    for t in tablolar:
        n = q(cur, f"SELECT count(*) FROM {t}")[0][0]
        sayim[t] = n
        kolonlar = [r[1] for r in q(cur, f"PRAGMA table_info({t})")]
        pk = TABLO_PK.get(t, None)
        grup = "ambar" if t.startswith("amb_") else "silver"
        node(f"tablo:{t}", "tablo", t, satir=n, pk=pk, kolonlar=kolonlar, grup=grup)
    if sayim.get("kayit", 0) == 0:
        print("HATA: kayit tablosu boş — silver üretilmemiş (FAIL-LOUD)", file=sys.stderr); return 3
    for src, dst in FK:
        st, sc = src.split("."); dt, dc = dst.split(".")
        if st in sayim and dt in sayim:
            et = "supersede" if (st == dt == "anahtar") else "fk"
            edge(f"tablo:{st}", et, f"tablo:{dt}", f"{sc} → {dc}", sutun=sc, hedef_sutun=dc)

    # --- referans türleri (pointer'lar) ---
    for rt, n in q(cur, "SELECT ref_turu, count(*) FROM referans GROUP BY 1 ORDER BY 1"):
        hv = q(cur, f"SELECT sum(hedef_var=1), sum(hedef_var=0) FROM referans WHERE ref_turu='{rt}' AND hedef_var IS NOT NULL")[0]
        cozumlu, kirik = (hv[0] or 0), (hv[1] or 0)
        node(f"ref:{rt}", "referans_turu", rt, sayi=n, cozumlu=cozumlu, kirik=kirik)
        edge("tablo:referans", "icerir", f"ref:{rt}", f"{tr(n)}")
        hedef, aciklama = REF_HEDEF.get(rt, ("dis:diger", "?"))
        lbl = aciklama + (f" · {tr(cozumlu)} çözümlü / {tr(kirik)} KIRIK" if (cozumlu or kirik) else "")
        if hedef.startswith("anahtar_turu:"):
            edge(f"ref:{rt}", "pointer_hedef", f"anahtar:{hedef.split(':',1)[1]}", lbl, cozumlu=cozumlu, kirik=kirik)
        elif hedef == "dosya":
            edge(f"ref:{rt}", "pointer_hedef", "tablo:dosya", lbl, cozumlu=cozumlu, kirik=kirik)
        else:
            node(hedef, "dis", hedef.split(":",1)[1])
            edge(f"ref:{rt}", "pointer_hedef", hedef, lbl)

    # --- anahtar türleri (çözümleme hedefi + süpersede) ---
    for tur, n, dep, rep in q(cur, "SELECT tur, count(*), sum(durum='deprecated'), sum(replaced_by IS NOT NULL AND replaced_by<>'') FROM anahtar GROUP BY 1 ORDER BY 1"):
        node(f"anahtar:{tur}", "anahtar_turu", tur, sayi=n, deprecated=dep or 0, supersede_li=rep or 0)
        edge("tablo:anahtar", "icerir", f"anahtar:{tur}", f"{tr(n)}")

    # --- dosya katmanları (sıcak/ılık/soğuk/yapısal) ---
    for katman, n in q(cur, "SELECT katman, count(*) FROM dosya GROUP BY 1 ORDER BY 1"):
        node(f"katman:{katman}", "dosya_katmani", katman, sayi=n)
        edge("tablo:dosya", "icerir", f"katman:{katman}", f"{tr(n)}")

    # --- hat katmanları (lineage) ---
    n_dosya = sayim.get("dosya", 0)
    gold = sorted(f for f in os.listdir("veri/gorunum") if f.endswith(".csv")) if os.path.isdir("veri/gorunum") else []
    node("hat:bronz", "hat_katmani", "bronz (git-izlenen md/json/jsonl)", sayi=n_dosya)
    node("hat:silver", "hat_katmani", "silver (veri/baglam.sqlite)", sayi=sum(sayim.values()))
    node("hat:gold", "hat_katmani", "gold (veri/gorunum/*.csv)", sayi=len(gold), dosyalar=gold)
    edge("hat:bronz", "turetir", "hat:silver", "tools/katman-hatti.py (sıfırdan, idempotent)")
    edge("hat:silver", "turetir", "hat:gold", "v_* görünümler → CSV")
    edge("hat:silver", "uretim_provenansi", "tablo:uretim", "git_head_sha · script_sha · kayit_id_kume_sha")

    # --- ilkeler + kronoloji (kanon sabitleri) ---
    for iid, ad, ozet, kaynak in ILKELER:
        node(f"ilke:{iid}", "ilke", ad, ozet=ozet, kaynak=kaynak)
    edge("ilke:m20", "ilke_uygular", "tablo:kayit", "kayit_id = ADRES (yol#satır#sha8)")
    edge("ilke:m20", "ilke_uygular", "tablo:referans", "pointer → hedef")
    edge("ilke:m21", "ilke_uygular", "tablo:referans", "dönüş yolu: pointer düşmez")
    edge("ilke:m22", "ilke_uygular", "tablo:dosya", "arşiv yolu güncellenir")
    edge("ilke:m8", "ilke_uygular", "tablo:anahtar", "replaced_by / gecerli_bitis (SCD-2)")
    edge("ilke:adres", "ilke_uygular", "tablo:kayit", "SEARCH USING INDEX")
    onceki = None
    for kid, tarih, ad, kaynak in KRONOLOJI:
        node(f"kron:{kid}", "kronoloji", f"{tarih} · {ad}", tarih=tarih, kaynak=kaynak)
        if onceki: edge(onceki, "kronoloji_sonra", f"kron:{kid}", "")
        onceki = f"kron:{kid}"

    # --- deterministik sıralama + meta ---
    nodes.sort(key=lambda x: (x["kind"], x["id"]))
    edges.sort(key=lambda x: (x["from"], x["type"], x["to"], x["label"]))
    uretim = q(cur, "SELECT uretim_zamani, git_head_sha FROM uretim ORDER BY uretim_zamani DESC LIMIT 1")
    try:
        head = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode().strip()
    except Exception:
        head = None
    meta = {"uretici": "tools/pointer-graf.py", "db": a.db, "silver_uretim": uretim[0][0] if uretim else None,
            "silver_git_head": uretim[0][1] if uretim else None, "git_head": head,
            "uretim_zamani": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
            "dugum_sayisi": len(nodes), "kenar_sayisi": len(edges), "sema": "pointer-graf-model v0 (deneysel m.29)",
            "not": "gövde deterministik (sıralı); yalnız meta.uretim_zamani değişir"}
    os.makedirs(os.path.dirname(a.json) or ".", exist_ok=True)
    with open(a.json, "w", encoding="utf-8") as f:
        json.dump({"meta": meta, "nodes": nodes, "edges": edges}, f, ensure_ascii=False, indent=1)
    if not a.sessiz:
        print(f"model → {a.json} · düğüm {len(nodes)} · kenar {len(edges)} · silver {meta['silver_git_head']} · HEAD {head}")

    if a.d2:
        yaz_d2(a.d2, nodes, edges, sayim, meta)
        if not a.sessiz:
            print(f"d2 (tam) → {a.d2}  (render: d2 --layout=elk {a.d2} {a.d2[:-3]}.svg)")
    yollar = []
    if a.d2_dizin:
        yollar = yaz_panolar(a.d2_dizin, nodes, edges, sayim, meta)
        if not a.sessiz:
            print("d2 panolar → " + " · ".join(yollar) + "  (render: her biri için d2 --layout=elk X.d2 X.svg)")
    if a.kenar_listesi:
        yaz_kenar_listesi(a.kenar_listesi, nodes, edges, meta)
        if not a.sessiz: print(f"kenar listesi → {a.kenar_listesi}")
    if a.render and yollar:
        kayit = render_et(yollar, a.render, meta)
        if not a.sessiz:
            print("render → " + " · ".join(f"{os.path.basename(k['svg'])}: {k['determinizm']} ({k['genislik']}×{k['yukseklik']})" for k in kayit["panolar"]) + f"  · kayıt {kayit['dosya']}")
        if any(k["determinizm"] != "BİREBİR" for k in kayit["panolar"]): return 4
    return 0

def d2id(s):  # D2 anahtarı: nokta/iki-nokta/boşluk yok
    return s.replace(":", "_").replace(".", "_").replace(" ", "_").replace("-", "_")

def yaz_d2(yol, nodes, edges, sayim, meta):
    N = {n["id"]: n for n in nodes}
    L = []
    L.append(f"# Jarvis POINTER SİSTEMİ — şema-düzeyi graf v0 (türetilmiş görünüm; ham kaynak silver/bronz)")
    L.append(f"# üretici: tools/pointer-graf.py · silver {meta['silver_git_head']} · HEAD {meta['git_head']} · düğüm {meta['dugum_sayisi']} · kenar {meta['kenar_sayisi']}")
    L.append("# render: d2 --layout=elk <bu dosya> <çıktı.svg>  (ELK: deterministik yerleşim — Karar 65)")
    L.append("direction: right")
    L.append("vars: { d2-config: { layout-engine: elk } }")
    L.append("classes: {")
    L.append("  tablo: { style: { fill: \"#F4F4F4\"; stroke: \"#444444\"; font-size: 14 } }")
    L.append("  pointer: { style: { fill: \"#E8F0FE\"; stroke: \"#1A56DB\" } }")
    L.append("  anahtar: { style: { fill: \"#FFF4E5\"; stroke: \"#B45309\" } }")
    L.append("  hat: { style: { fill: \"#ECFDF5\"; stroke: \"#047857\"; bold: true } }")
    L.append("  ilke: { shape: hexagon; style: { fill: \"#FDF2F8\"; stroke: \"#9D174D\" } }")
    L.append("  kron: { shape: page; style: { fill: \"#FFFFFF\"; stroke: \"#6B7280\"; font-size: 12 } }")
    L.append("  dis: { shape: cloud; style: { fill: \"#FAFAFA\"; stroke: \"#9CA3AF\" } }")
    L.append("  kirik: { style: { stroke: \"#DC2626\"; stroke-dash: 3 } }")
    L.append("  supersede: { style: { stroke: \"#B45309\"; stroke-dash: 5 } }")
    L.append("  fk: { style: { stroke: \"#444444\" } }")
    L.append("  turetir: { style: { stroke: \"#047857\"; stroke-width: 3 } }")
    L.append("}")
    # --- hat (lineage) üst bağlam ---
    L.append("hat: \"VERİ HATTI (lineage)\" {")
    for hid in ["hat:bronz", "hat:silver", "hat:gold"]:
        n = N[hid]; L.append(f"  {d2id(hid.split(':')[1])}: \"{n['label']} · {tr(n['sayi'])}\" {{ class: hat }}")
    L.append("}")
    # --- silver tabloları (sql_table) ---
    L.append("silver: \"SİLVER (veri/baglam.sqlite) — PK = ADRES\" {")
    for n in [x for x in nodes if x["kind"] == "tablo" and x["grup"] == "silver"]:
        t = n["label"]; kol = GOSTER_SUTUN.get(t, n["kolonlar"][:6])
        L.append(f"  {t}: \"{t} · {tr(n['satir'])} satır\" {{")
        L.append("    shape: sql_table")
        for c in kol:
            kisit = ""
            if c == n["pk"]: kisit = " { constraint: primary_key }"
            elif any(f"{t}.{c}" == s for s, _ in FK): kisit = " { constraint: foreign_key }"
            L.append(f"    {c}: TEXT{kisit}")
        L.append("  }")
    amb = [x for x in nodes if x["kind"] == "tablo" and x["grup"] == "ambar"]
    if amb:
        L.append(f"  ambar: \"AMBAR olgu tabloları · {len(amb)} tablo · {tr(sum(x['satir'] for x in amb))} satır\" {{ class: tablo }}")
    L.append("}")
    # --- pointer türleri + anahtar türleri + dosya katmanları ---
    L.append("pointer: \"REFERANS TÜRLERİ (pointer'lar) — referans tablosundan\" {")
    for n in [x for x in nodes if x["kind"] == "referans_turu"]:
        ek = f" · {tr(n['cozumlu'])} çözümlü / {tr(n['kirik'])} KIRIK" if (n["cozumlu"] or n["kirik"]) else ""
        L.append(f"  {d2id(n['label'])}: \"{n['label']} · {tr(n['sayi'])}{ek}\" {{ class: pointer }}")
    L.append("}")
    L.append("anahtar_kaydi: \"ANAHTAR KAYDI (çözümleme hedefi; süpersede zinciri)\" {")
    for n in [x for x in nodes if x["kind"] == "anahtar_turu"]:
        L.append(f"  {d2id(n['label'])}: \"{n['label']} · {tr(n['sayi'])}\" {{ class: anahtar }}")
    L.append("}")
    L.append("dosya_katmani: \"DOSYA KATMANLARI (sıcak/ılık/soğuk/yapısal)\" {")
    for n in [x for x in nodes if x["kind"] == "dosya_katmani"]:
        L.append(f"  {d2id(n['label'])}: \"{n['label']} · {tr(n['sayi'])}\" {{ class: tablo }}")
    L.append("}")
    L.append("dis: \"REPO DIŞI HEDEFLER\" {")
    for n in [x for x in nodes if x["kind"] == "dis"]:
        L.append(f"  {d2id(n['label'])}: \"{n['label']}\" {{ class: dis }}")
    L.append("}")
    L.append("ilke: \"POINTER İLKESİ (kanon sabiti)\" {")
    for n in [x for x in nodes if x["kind"] == "ilke"]:
        L.append(f"  {d2id(n['id'].split(':')[1])}: \"{n['label']}\\n{n['ozet']}\" {{ class: ilke; tooltip: \"{n['kaynak']}\" }}")
    L.append("}")
    L.append("kronoloji: \"KURULUŞ KRONOLOJİSİ (07-11 → 08-22)\" {")
    L.append("  direction: down")
    for n in [x for x in nodes if x["kind"] == "kronoloji"]:
        L.append(f"  {d2id(n['id'].split(':')[1])}: \"{n['label']}\" {{ class: kron; tooltip: \"{n['kaynak']}\" }}")
    L.append("}")
    # --- kenarlar ---
    def ref(nid):
        k, v = nid.split(":", 1)
        return {"tablo": f"silver.{v}" if not v.startswith("amb_") else "silver.ambar", "ref": f"pointer.{d2id(v)}",
                "anahtar": f"anahtar_kaydi.{d2id(v)}", "katman": f"dosya_katmani.{d2id(v)}", "hat": f"hat.{d2id(v)}",
                "dis": f"dis.{d2id(v)}", "ilke": f"ilke.{d2id(v)}", "kron": f"kronoloji.{d2id(v)}"}[k]
    gorulen = set()
    for e in edges:
        if e["type"] == "icerir":  # kapsayıcı ilişkisi zaten iç içe gösterildi
            continue
        key = (ref(e["from"]), ref(e["to"]), e["type"], e["label"])
        if key in gorulen: continue
        gorulen.add(key)
        cls = {"fk": "fk", "supersede": "supersede", "turetir": "turetir", "uretim_provenansi": "turetir"}.get(e["type"], None)
        if e["type"] == "pointer_hedef" and e.get("kirik", 0): cls = "kirik"
        lbl = e["label"].replace('"', "'")
        ek = f" {{ class: {cls} }}" if cls else ""
        L.append(f"{key[0]} -> {key[1]}: \"{lbl}\"{ek}" if lbl else f"{key[0]} -> {key[1]}{ek}")
    os.makedirs(os.path.dirname(yol) or ".", exist_ok=True)
    with open(yol, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")

def d2_surum():
    try:
        return subprocess.check_output(["d2", "--version"], stderr=subprocess.STDOUT).decode().strip().split()[0]
    except Exception:
        return "bilinmiyor"

def _bas(meta, baslik, yon="right"):
    return [f"# Jarvis POINTER SİSTEMİ — {baslik} (türetilmiş görünüm; ham kaynak silver/bronz)",
            f"# üretici: tools/pointer-graf.py · silver {str(meta['silver_git_head'])[:7]} · HEAD {meta['git_head']} · d2 {d2_surum()} · render: d2 --layout=elk (ELK bundled; TALA girmez; determinizm yerel sha256 ile ölçülür — Karar 65)",
            "# içerik katmanı: düğüm/kenar = silver'dan script türetimi (LLM yazmaz); ilke/kronoloji = kanon SABİTİ (pointer'lı, script içinde); yorum katmanı = bu # satırları",
            f"direction: {yon}",
            "classes: {",
            "  kutu: { style: { fill: \"#F4F4F4\"; stroke: \"#444444\"; font-size: 16; border-radius: 6 } }",
            "  pointer: { style: { fill: \"#E8F0FE\"; stroke: \"#1A56DB\"; border-radius: 6 } }",
            "  anahtar: { style: { fill: \"#FFF4E5\"; stroke: \"#B45309\"; border-radius: 6 } }",
            "  hat: { style: { fill: \"#ECFDF5\"; stroke: \"#047857\"; bold: true; border-radius: 6 } }",
            "  ilke: { shape: hexagon; style: { fill: \"#FDF2F8\"; stroke: \"#9D174D\" } }",
            "  kron: { shape: page; style: { fill: \"#FFFFFF\"; stroke: \"#6B7280\" } }",
            "  dis: { shape: cloud; style: { fill: \"#FAFAFA\"; stroke: \"#9CA3AF\" } }",
            "  kirik: { style: { stroke: \"#DC2626\"; stroke-dash: 3; font-size: 14 } }",
            "  supersede: { style: { stroke: \"#B45309\"; stroke-dash: 5 } }",
            "  fk: { style: { stroke: \"#444444\"; font-size: 14 } }",
            "  turetir: { style: { stroke: \"#047857\"; stroke-width: 3 } }",
            "  uygular: { style: { stroke: \"#9D174D\"; stroke-dash: 2; font-size: 14 } }",
            "}"]

def yaz_panolar(dizin, nodes, edges, sayim, meta):
    """Çok-panolu (kademeli) çıktı: genel bakış + 4 ayrıntı. Her pano bağımsız .d2; sıralama deterministik."""
    os.makedirs(dizin, exist_ok=True)
    N = {n["id"]: n for n in nodes}
    K = lambda kind: [x for x in nodes if x["kind"] == kind]
    refs, anahtarlar, katmanlar, ilkeler, kron, dis = K("referans_turu"), K("anahtar_turu"), K("dosya_katmani"), K("ilke"), K("kronoloji"), K("dis")
    tablolar = [x for x in nodes if x["kind"] == "tablo" and x["grup"] == "silver"]
    amb = [x for x in nodes if x["kind"] == "tablo" and x["grup"] == "ambar"]
    n_ref = sum(x["sayi"] for x in refs); n_kirik = sum(x["kirik"] for x in refs); n_anahtar = sum(x["sayi"] for x in anahtarlar)
    yollar = []
    # ---------------- PANO 0: GENEL BAKIŞ ----------------
    katman_ozet = " · ".join(f"{x['label']} {tr(x['sayi'])}" for x in katmanlar)
    L = _bas(meta, "GENEL BAKIŞ (pano 0/4) — ayrıntı panoları: silver · pointer · ilke · kronoloji", "down")
    L += [
      "hat: \"VERİ HATTI (lineage)\" {",
      f"  bronz: \"BRONZ\\ngit-izlenen md/json/jsonl · {tr(N['hat:bronz']['sayi'])} dosya\" {{ class: hat }}",
      f"  silver: \"SİLVER · veri/baglam.sqlite\\n{len(tablolar)} tablo · {tr(sum(x['satir'] for x in tablolar))} satır · PK = ADRES (yol#satır#sha8)\" {{ class: hat; link: \"pointer-sistemi-v0-silver.svg\" }}",
      f"  gold: \"GOLD · veri/gorunum\\n{tr(N['hat:gold']['sayi'])} CSV görünüm\" {{ class: hat }}",
      "  bronz -> silver: \"tools/katman-hatti.py\\nsıfırdan, idempotent\" { class: turetir }",
      "  silver -> gold: \"v_* görünümler\" { class: turetir }",
      "}",
      f"pointer: \"POINTER'LAR (referans tablosu)\\n{len(refs)} tür · {tr(n_ref)} referans · {tr(n_kirik)} KIRIK\" {{ class: pointer; link: \"pointer-sistemi-v0-pointer.svg\" }}",
      f"anahtar: \"ANAHTAR KAYDI\\n{len(anahtarlar)} tür · {tr(n_anahtar)} anahtar · süpersede zinciri (replaced_by, SCD-2)\" {{ class: anahtar; link: \"pointer-sistemi-v0-pointer.svg\" }}",
      f"dosya: \"DOSYALAR · {tr(sayim.get('dosya',0))}\\nkatman: {katman_ozet}\" {{ class: kutu }}",
      f"ambar: \"AMBAR olgu tabloları · {len(amb)} tablo · {tr(sum(x['satir'] for x in amb))} satır\" {{ class: kutu }}",
      f"dis: \"REPO DIŞI HEDEFLER\\nurl · git sha · zaman · etiket\" {{ class: dis }}",
      f"ilke: \"POINTER İLKESİ (kanon)\\nm.20 özet+adres · m.21 dönüş yolu · m.22 arşiv · m.8 süpersede · adresli erişim\" {{ class: ilke; link: \"pointer-sistemi-v0-ilke.svg\" }}",
      f"kron: \"KURULUŞ KRONOLOJİSİ\\n{kron[0]['tarih']} → {kron[-1]['tarih']} · {len(kron)} adım\" {{ class: kron; link: \"pointer-sistemi-v0-kronoloji.svg\" }}",
      "hat.silver -> pointer: \"referans.kayit_id → kayit (FK)\" { class: fk }",
      f"pointer -> anahtar: \"m.N · V-n · K-NNN · [[wiki]] · skill · terim → çözümleme\" {{ class: fk }}",
      f"pointer -> dosya: \"dosya_pointer → yol ({tr(N['ref:dosya_pointer']['cozumlu'])} çözümlü / {tr(N['ref:dosya_pointer']['kirik'])} KIRIK)\" {{ class: kirik }}",
      "pointer -> dis: \"url · sha · tarih · etiket\"",
      "anahtar -> anahtar: \"replaced_by = prov:wasRevisionOf (süpersede)\" { class: supersede }",
      "hat.silver -> dosya: \"kayit.dosya_id → dosya (FK)\" { class: fk }",
      "hat.silver -> ambar: \"koşum/tahmin olguları\" { class: fk }",
      "ilke -> hat.silver: \"uygular: kayit_id = ADRES · pointer→hedef · arşiv · SCD-2\" { class: uygular }",
      "kron -> ilke: \"07-11 imza → 08-22 graf\" { class: uygular }",
    ]
    yol = os.path.join(dizin, "pointer-sistemi-v0-genel.d2"); open(yol, "w", encoding="utf-8").write("\n".join(L) + "\n"); yollar.append(yol)
    # ---------------- PANO 1: SİLVER tabloları (PK/FK) ----------------
    L = _bas(meta, "SİLVER TABLOLARI — PK/FK (pano 1/4)", "right")
    for n in tablolar:
        t = n["label"]; kol = GOSTER_SUTUN.get(t, n["kolonlar"][:6])
        L.append(f"{t}: \"{t} · {tr(n['satir'])} satır\" {{")
        L.append("  shape: sql_table")
        for c in kol:
            kisit = ""
            if c == n["pk"]: kisit = " { constraint: primary_key }"
            elif any(f"{t}.{c}" == s for s, _ in FK): kisit = " { constraint: foreign_key }"
            L.append(f"  {c}: TEXT{kisit}")
        L.append("}")
    for src, dst in FK:
        st, sc = src.split("."); dt, dc = dst.split(".")
        if st in sayim and dt in sayim:
            cls = "supersede" if st == dt == "anahtar" else "fk"
            L.append(f"{st}.{sc} -> {dt}.{dc}: \"{'süpersede' if cls=='supersede' else 'FK'}\" {{ class: {cls} }}")
    yol = os.path.join(dizin, "pointer-sistemi-v0-silver.d2"); open(yol, "w", encoding="utf-8").write("\n".join(L) + "\n"); yollar.append(yol)
    # ---------------- PANO 2: POINTER türleri → hedefler ----------------
    L = _bas(meta, "POINTER TÜRLERİ → ÇÖZÜMLEME HEDEFLERİ (pano 2/4)", "right")
    L.append("pointer: \"REFERANS TÜRLERİ (referans.ref_turu)\" {")
    for n in refs:
        ek = f"\\n{tr(n['cozumlu'])} çözümlü / {tr(n['kirik'])} KIRIK" if (n["cozumlu"] or n["kirik"]) else ""
        L.append(f"  {d2id(n['label'])}: \"{n['label']} · {tr(n['sayi'])}{ek}\" {{ class: pointer }}")
    L.append("}")
    L.append("anahtar: \"ANAHTAR KAYDI (anahtar.tur)\" {")
    for n in anahtarlar:
        L.append(f"  {d2id(n['label'])}: \"{n['label']} · {tr(n['sayi'])}\" {{ class: anahtar }}")
    L.append("}")
    L.append(f"dosya: \"dosya tablosu · {tr(sayim.get('dosya',0))}\" {{ class: kutu }}")
    L.append("dis: \"REPO DIŞI\" {")
    for n in dis:
        L.append(f"  {d2id(n['label'])}: \"{n['label']}\" {{ class: dis }}")
    L.append("}")
    L.append("anahtar -> anahtar: \"replaced_by = prov:wasRevisionOf (süpersede, SCD-2)\" { class: supersede }")
    for e in edges:
        if e["type"] != "pointer_hedef": continue
        src = f"pointer.{d2id(e['from'].split(':',1)[1])}"
        k, v = e["to"].split(":", 1)
        dst = {"anahtar": f"anahtar.{d2id(v)}", "tablo": "dosya", "dis": f"dis.{d2id(v)}"}[k]
        cls = "kirik" if e.get("kirik", 0) else "fk"
        lbl = e["label"].split(" · ")[0].replace('"', "'")
        L.append(f"{src} -> {dst}: \"{lbl}\" {{ class: {cls} }}")
    yol = os.path.join(dizin, "pointer-sistemi-v0-pointer.d2"); open(yol, "w", encoding="utf-8").write("\n".join(L) + "\n"); yollar.append(yol)
    # ---------------- PANO 3: İLKE → mekanizma ----------------
    L = _bas(meta, "POINTER İLKESİ → MEKANİZMA (pano 3/4)", "right")
    for n in ilkeler:
        L.append(f"{d2id(n['id'].split(':')[1])}: \"{n['label']}\\n{n['ozet']}\" {{ class: ilke; tooltip: \"{n['kaynak']}\" }}")
    for t in ["kayit", "referans", "dosya", "anahtar"]:
        if t in sayim: L.append(f"{t}: \"{t} · {tr(sayim[t])}\" {{ class: kutu }}")
    for e in edges:
        if e["type"] != "ilke_uygular": continue
        L.append(f"{d2id(e['from'].split(':')[1])} -> {e['to'].split(':')[1]}: \"{e['label']}\" {{ class: uygular }}")
    yol = os.path.join(dizin, "pointer-sistemi-v0-ilke.d2"); open(yol, "w", encoding="utf-8").write("\n".join(L) + "\n"); yollar.append(yol)
    # ---------------- PANO 4: KRONOLOJİ ----------------
    L = _bas(meta, "KURULUŞ KRONOLOJİSİ (pano 4/4)", "down")
    onceki = None
    for n in kron:
        kid = d2id(n["id"].split(":")[1])
        L.append(f"{kid}: \"{n['label']}\" {{ class: kron; tooltip: \"{n['kaynak']}\" }}")
        if onceki: L.append(f"{onceki} -> {kid}")
        onceki = kid
    yol = os.path.join(dizin, "pointer-sistemi-v0-kronoloji.d2"); open(yol, "w", encoding="utf-8").write("\n".join(L) + "\n"); yollar.append(yol)
    return yollar

def yaz_kenar_listesi(yol, nodes, edges, meta):
    """LLM-okunur İKİNCİ GÖRÜNÜM: adlandırılmış incident/kenar listesi (C-YT4: kodlama sabit kurallı, script-üretimli; D2 kaynağı LLM'e verilmez)."""
    N = {n["id"]: n for n in nodes}
    L = [f"# Jarvis pointer sistemi — kenar listesi (LLM-okunur görünüm; üretici tools/pointer-graf.py; silver {str(meta['silver_git_head'])[:7]}; düğüm {len(nodes)} · kenar {len(edges)})",
         "# biçim: KAYNAK --tip[etiket]--> HEDEF ; sıralama sabit (from,type,to,label); sayılar silver'dan",
         "", "## DÜĞÜMLER (kind · id · label · sayı)"]
    for n in nodes:
        sayi = n.get("satir", n.get("sayi", ""))
        L.append(f"{n['kind']} · {n['id']} · {n['label']}" + (f" · {tr(sayi)}" if sayi != "" else ""))
    L += ["", "## KENARLAR"]
    for e in edges:
        L.append(f"{e['from']} --{e['type']}" + (f"[{e['label']}]" if e['label'] else "") + f"--> {e['to']}")
    os.makedirs(os.path.dirname(yol) or ".", exist_ok=True)
    open(yol, "w", encoding="utf-8").write("\n".join(L) + "\n")

def render_et(yollar, n_kosum, meta):
    """Panoları d2 --layout=elk ile SVG'ye çevirir; her panoyu n_kosum kez render edip sha256 eşitliğini ölçer (C-YT2/B-YT7); üretim kaydı yazar (A-YT2)."""
    import hashlib, re, shutil, tempfile
    kayit = {"d2_surum": d2_surum(), "layout": "elk", "n_kosum": n_kosum, "silver_git_head": meta["silver_git_head"], "git_head": meta["git_head"],
             "olcum_zamani": meta["uretim_zamani"], "not": "aynı .d2 × aynı d2 sürümü × aynı motor → SVG sha256 eşitliği; sürümler-arası eşitlik BEKLENMEZ (A-YT2)", "panolar": []}
    for d2yol in yollar:
        svg = d2yol[:-3] + ".svg"
        shalar = []
        for i in range(max(1, n_kosum)):
            hedef = svg if i == 0 else os.path.join(tempfile.gettempdir(), f"pg_{os.path.basename(svg)}.{i}")
            r = subprocess.run(["d2", "--layout=elk", d2yol, hedef], capture_output=True, text=True)
            if r.returncode != 0:
                print(f"HATA: d2 render başarısız: {d2yol}\n{r.stderr[-400:]}", file=sys.stderr); sys.exit(4)
            shalar.append(hashlib.sha256(open(hedef, "rb").read()).hexdigest())
            if i > 0: os.remove(hedef)
        svgtxt = open(svg, encoding="utf-8").read()
        w = re.search(r'width="(\d+)"', svgtxt); h = re.search(r'height="(\d+)"', svgtxt)
        kayit["panolar"].append({"d2": d2yol, "svg": svg, "sha256": shalar[0], "determinizm": "BİREBİR" if len(set(shalar)) == 1 else f"FARKLI ({len(set(shalar))} ayrı sha)",
                                 "genislik": int(w.group(1)) if w else None, "yukseklik": int(h.group(1)) if h else None})
    kayit["dosya"] = os.path.join(os.path.dirname(yollar[0]) or ".", "pointer-sistemi-v0-uretim.json")
    with open(kayit["dosya"], "w", encoding="utf-8") as f:
        json.dump(kayit, f, ensure_ascii=False, indent=1)
    return kayit

if __name__ == "__main__":
    sys.exit(main())
