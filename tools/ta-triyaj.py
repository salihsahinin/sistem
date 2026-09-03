#!/usr/bin/env python3
"""ta-triyaj.py — T-A-ÖNELEME KATMANLI TRİYAJ (Karar 83 B3 (a); Salih 09-03). STDLIB ONLY, LLM YOK.

Soru: T-A-ÖNELEME testi (tools/silver-saglik.py::t_a) bir koşumda ≤500 aday çift üretir (max_cift_kayit; ihlal
  toplamı çok daha büyük olabilir — bkz. veri/silver-saglik.jsonl "not") ve LLM koşumu (öneleme kararı) ayrı
  tetiktir, pahalı. Karar 83 B3 (a): "T-A 500 çift → KATMANLI TRİYAJ: deterministik ön-sınıflandırma + şiddet-
  sıralı ilk ~20 sonraki masaya". Bu araç yalnız SIRALAR/SEÇER, ÖNELEMEZ (öneleme kararı ayrı, LLM'li adım).

GİRDİ: veri/baglam.sqlite::silver_karantina_aday — t_a()'nın yazdığı GERÇEK 500 çift (cift_id, anahtar_terim,
  kayit_id_a/b, dosya_a/b, blok_turu, uzunluk_a/b [karakter, k.metin uzunluğu — t_a() zaten hesaplıyor, İCAT
  EDİLMEDİ], kosum_id). veri/silver-saglik.jsonl'deki `ornek` alanı yalnız İLK 10'u taşır (Sonuclar.ekle:
  `list(ornek)[:10]`) — 500 çiftin tamamı için TEK kaynak sqlite tablosudur. En son kosum_id = tablodaki
  MAX(rowid)'in kosum_id'si (INSERT OR REPLACE PRIMARY KEY cift_id; tek kosum_id kaldıysa doğrudan o). jsonl
  yalnız künye (ts/snapshot/head) için okunur.
  t_a() kodu (silver-saglik.py) zaten aynı-dosya çiftini ELER (da==db skip) ve varsayılan ayni_blok_turu=True
  ile blok türü farklıysa ELER — yani 500 çift zaten ÇAPRAZ-DOSYA ∧ AYNI-BLOK-TÜRÜ'dür; gruplama anahtar_terim
  bazlı yapıldığından (grup.setdefault(at, ...)) "çapraz-anahtar" sınıfı bu veri kümesinde hiç OLUŞMAZ.

ÖN-SINIFLANDIRMA (deterministik, dosya yoluna bakan kural — model yargısı değil): dosya_a/dosya_b'nin İLK dizin
  bileşeni (kök dosyalar için "kök") eşit mi:
    ayni-ust-klasor   → ör. ikisi de .claude/skills/... altında
    capraz-ust-klasor → ör. core/... vs .claude/skills/...

ŞİDDET FORMÜLÜ (bu koşumda SEÇİLEN — alternatifler + gerekçe altta, nihai onay Fable/Salih'e bırakılır, m.40 eki):
    uzunluk_toplam = uzunluk_a + uzunluk_b   (t_a()'nın kendi ürettiği karakter uzunlukları)
    tekrar_sayisi(anahtar_terim) = bu 500-çiftlik kümede AYNI anahtar_terim'i taşıyan çift sayısı (o terimin
                                    500-çift içindeki fan-out'u — gerçek DB-geneli grup büyüklüğü değil, YALNIZ
                                    yazılan 500 üzerinden bir alt-küme sayımı; 500 sınırı kırparsa hafif eksik
                                    kalabilir)
    siddet = uzunluk_toplam × tekrar_sayisi
  ALTERNATİFLER (görev emrinde "uzunluk-farkı × tekrar-sayısı gibi" dendi — İKİ seçenek denendi, TOPLAM seçildi):
    (a) uzunluk_FARKI × tekrar_sayısı — |uzunluk_a-uzunluk_b| küçükse (iki kayıt neredeyse eş boy) düşük şiddet
        verir; ama tam kopya/paralel-eş metin çiftleri (en çok emek kaybı riski) TAM BURADA yoğunlaşır — farkı
        küçük olan çiftleri en ALTA iter, istenenin TERSİ bir sıralama olur.
    (b) uzunluk_TOPLAMI × tekrar_sayısı [SEÇİLEN] — "ne kadar metin taşınıyor" sorusuna cevap verir, eş-boy
        kopyaları da CEZALANDIRMAZ; büyük+küçük asimetrik çiftler de büyük tarafın ağırlığıyla öne çıkar.
  Nihai onay masaya bırakılır; formül script'te TEK yerde (triyaj() içinde) değişebilir.

ÇIKTI: insan-okur tablo (varsayılan) ya da --json (A1: {"ok", "kosum_id", "toplam_cift", "ilk_20":[...]}).
Kullanım: python3 tools/ta-triyaj.py [--db veri/baglam.sqlite] [--saglik veri/silver-saglik.jsonl] [--json] [--n 20]
Çıkış: 0 tamam · 2 girdi/T-A verisi yok. Deneysel m.29 (2026-09-03, işçi-ajan, Karar 83 B3 (a) icrası).
"""
import argparse, json, os, sqlite3, sys
from collections import Counter


def ust_klasor(yol):
    yol = (yol or "").replace("\\", "/")
    p = [x for x in yol.split("/") if x]
    return p[0] if len(p) > 1 else "kök"


def son_kosum_kunye(dosya):
    """silver-saglik.jsonl içinde EN SON kosum_id'nin T-A-ÖNELEME satırı — yalnız künye (ts/snapshot/head) için."""
    en_son = None
    if not os.path.exists(dosya):
        return None
    with open(dosya, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except json.JSONDecodeError:
                continue
            if o.get("test_id") != "T-A-ONELEME":
                continue
            if en_son is None or o.get("ts", "") >= en_son.get("ts", ""):
                en_son = o
    return en_son


def cift_oku(db_yolu, kosum_id=None):
    con = sqlite3.connect("file:%s?mode=ro" % db_yolu, uri=True)
    try:
        if kosum_id is None:
            r = con.execute("SELECT kosum_id FROM silver_karantina_aday ORDER BY rowid DESC LIMIT 1").fetchone()
            kosum_id = r[0] if r else None
        rows = con.execute("""SELECT anahtar_terim, kayit_id_a, kayit_id_b, dosya_a, dosya_b, blok_turu, uzunluk_a, uzunluk_b
                               FROM silver_karantina_aday WHERE kosum_id=?""", (kosum_id,)).fetchall()
    finally:
        con.close()
    return kosum_id, rows


def triyaj(rows, n):
    ciftler = [{"anahtar_terim": at, "kayit_a": ka, "kayit_b": kb, "dosya_a": da, "dosya_b": db, "blok_turu": bt,
                "uzunluk_a": la, "uzunluk_b": lb} for (at, ka, kb, da, db, bt, la, lb) in rows]
    tekrar = Counter(c["anahtar_terim"] for c in ciftler)
    for c in ciftler:
        c["sinif"] = "ayni-ust-klasor" if ust_klasor(c["dosya_a"]) == ust_klasor(c["dosya_b"]) else "capraz-ust-klasor"
        c["tekrar_sayisi"] = tekrar[c["anahtar_terim"]]
        c["uzunluk_toplam"] = c["uzunluk_a"] + c["uzunluk_b"]
        c["siddet"] = c["uzunluk_toplam"] * c["tekrar_sayisi"]
    ciftler.sort(key=lambda c: (-c["siddet"], c["anahtar_terim"], c["dosya_a"], c["dosya_b"]))
    for i, c in enumerate(ciftler, 1):
        c["sira"] = i
    return ciftler[:n], len(ciftler)


def main():
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ap = argparse.ArgumentParser(description="T-A-ÖNELEME katmanlı triyaj (Karar 83 B3 (a))")
    ap.add_argument("--db", default=os.path.join(repo, "veri", "baglam.sqlite"))
    ap.add_argument("--saglik", default=os.path.join(repo, "veri", "silver-saglik.jsonl"))
    ap.add_argument("--n", type=int, default=20)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if not os.path.exists(a.db):
        print("HATA: silver yok: %s" % a.db, file=sys.stderr)
        return 2
    kosum_id, rows = cift_oku(a.db)
    if not rows:
        print("HATA: silver_karantina_aday boş (T-A koşumu yapılmamış)", file=sys.stderr)
        return 2
    kunye = son_kosum_kunye(a.saglik) or {}

    ilk_n, toplam = triyaj(rows, a.n)

    if a.json:
        print(json.dumps({"ok": True, "kosum_id": kosum_id, "ts": kunye.get("ts"), "snapshot": kunye.get("snapshot"),
                           "head": kunye.get("head"), "toplam_cift": toplam, "ilk_n": len(ilk_n), "ilk_20": ilk_n}, ensure_ascii=False, indent=1))
        return 0

    print("T-A-ÖNELEME triyaj — kosum_id=%s snapshot=%s toplam_cift=%d ilk=%d" % (kosum_id, kunye.get("snapshot"), toplam, len(ilk_n)))
    print("%-4s %-18s %8s %-24s %s" % ("sıra", "sınıf", "şiddet", "anahtar_terim", "A ↔ B"))
    for c in ilk_n:
        print("%-4d %-18s %8d %-24s %s ↔ %s" % (c["sira"], c["sinif"], c["siddet"], c["anahtar_terim"], c["dosya_a"], c["dosya_b"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
