#!/usr/bin/env python3
"""bayat-cekim.py — D3 BAYATLIK KUYRUĞU BOŞALTMA (anakronizm M6; KB-68 (a) Karar 69 EK; İB-52) — STDLIB ONLY, deterministik.

Politika (Salih 08-26, KB-68 a): tek eşik 90 gün (anakronizm-denetim varsayılanı) + seans kapanışında N=3 yeniden-çekim + silver
`kayit.cekim_tarihi/kaynak_tarihi` (baglam-tablo.py türetir). Ders: Wikipedia "As of 2010" alt-kategorisinde hâlâ 3.126 açık sayfa —
kuyruk boşaltma adımı olmayan bayatlık kuyruğu büyür. SİLME YOK (m.8): yeniden-çekim damga tazeler ya da yeni sürüm satırı açar.

Grain: veri/bronz/cekim-olay.jsonl — 1 satır = 1 YENİDEN-ÇEKİM OLAYI {ts, kod_sha, kosum_id, dosya_id, cekim_tarihi, kaynak_tarihi, sonuc, not}
  sonuc ∈ {teyit: iddialar hâlâ geçerli, dosyaya dokunulmadı (damga bronz'dan tazelenir) · guncellendi: dosya düzeltildi (yeni sürüm
  satırı; commit ayrı) · sonlandi: iddia artık geçersiz, dosyaya gecerli_bitis/emekli notu düşüldü}. Append-only; bronz ham kalır.
Tüketenler: baglam-tablo.py (kayit.cekim_tarihi = max(son_commit, en yeni olay)) · anakronizm-denetim.py D3 (olay damgası dosya-içi
damgalarla birlikte sayılır → kuyruktan düşer).

Modlar:
  --liste [--n 3]      v_bayat_aday.csv'den yaş sırasıyla ilk N dosya + o dosyaların SON anakronizm koşumundaki D1 bulguları (yeniden-
                       çekilecek iddialar). Yazmaz. Yeniden-çekimin kendisi canlı kaynak işidir (M3: kanıt tarihi cevaba yazılır).
  --kaydet <dosya> --sonuc teyit|guncellendi|sonlandi [--kaynak-tarihi YYYY-MM-DD] [--not "..."]   → 1 olay satırı.
  --olcum [--n 3]      kapanış ölçüm satırları → veri/katman-olcum.jsonl (katman=bronz · nesne=v_bayat_aday.csv · metrik bayat_kuyruk_n,
                       cekim_bugun_n, cekim_hedef_n) — seans-kapanis adım 6f; kuyruk boşsa 0 yazılır (uydurma yok, m.39).
Kullanım: python3 tools/bayat-cekim.py (--liste | --kaydet D --sonuc S | --olcum) [--n 3] [--bugun YYYY-MM-DD] [--repo <yol>]
Çıkış: 0 tamam · 2 girdi hatası. Deneysel m.29 (2026-08-29, Carvis, yan icra oturumu). Kayıt: tools/SCRIPTLER.md.
"""
import argparse, csv, hashlib, json, os, subprocess, sys
from datetime import date, datetime, timezone, timedelta

SONUC = {"teyit", "guncellendi", "sonlandi"}


def sh(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True).stdout.strip()


def kuyruk_oku(repo):
    yol = os.path.join(repo, "veri", "gorunum", "v_bayat_aday.csv")
    if not os.path.exists(yol):
        return [], ""
    raw = open(yol, encoding="utf-8").read()
    satirlar = [r for r in csv.DictReader(raw.splitlines()) if r.get("dosya") and not r["dosya"].startswith("#")]
    satirlar.sort(key=lambda r: (-int(r.get("yas_gun") or 0), r["dosya"]))
    return satirlar, hashlib.sha1(raw.encode("utf-8")).hexdigest()


def son_d1_bulgular(repo, dosyalar):
    """anakronizm-denetim.jsonl son kosum_id'sinin D1 bulguları, dosya → [satır: kalıp]."""
    yol = os.path.join(repo, "veri", "anakronizm-denetim.jsonl")
    out = {d: [] for d in dosyalar}
    if not os.path.exists(yol):
        return out
    son, kayitlar = None, []
    with open(yol, encoding="utf-8") as fh:
        for line in fh:
            try:
                o = json.loads(line)
            except json.JSONDecodeError:
                continue
            kayitlar.append(o); son = o.get("kosum_id", son)
    for o in kayitlar:
        if o.get("kosum_id") == son and o.get("denetim") == "D1" and o.get("dosya") in out:
            out[o["dosya"]].append("%s: %s [%s]" % (o.get("satir"), o.get("kalip"), o.get("seviye")))
    return out


def bugun_olaylari(repo, bugun):
    yol = os.path.join(repo, "veri", "bronz", "cekim-olay.jsonl")
    n = 0
    if os.path.exists(yol):
        with open(yol, encoding="utf-8") as fh:
            for line in fh:
                try:
                    o = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if (o.get("cekim_tarihi") or "")[:10] == bugun.isoformat():
                    n += 1
    return n


def main():
    ap = argparse.ArgumentParser(description="D3 bayatlık kuyruğu boşaltma (İB-52)")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--liste", action="store_true"); ap.add_argument("--olcum", action="store_true")
    ap.add_argument("--kaydet", metavar="DOSYA"); ap.add_argument("--sonuc", choices=sorted(SONUC))
    ap.add_argument("--kaynak-tarihi", default=None); ap.add_argument("--not", dest="not_", default="")
    ap.add_argument("--n", type=int, default=3); ap.add_argument("--bugun", default=None)
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)
    bugun = date.fromisoformat(a.bugun) if a.bugun else date.today()
    head = sh(["git", "rev-parse", "--short", "HEAD"], repo) or "-"
    ts = datetime.now(timezone(timedelta(hours=3))).replace(microsecond=0).isoformat()
    kosum_id = "bayat-cekim:%s:%s" % (head, bugun.isoformat())
    kuyruk, girdi_sha = kuyruk_oku(repo)

    if a.kaydet:
        if not a.sonuc:
            print("HATA: --kaydet için --sonuc zorunlu (teyit|guncellendi|sonlandi)", file=sys.stderr); return 2
        rel = os.path.relpath(os.path.abspath(a.kaydet), repo) if os.path.isabs(a.kaydet) else a.kaydet
        if not os.path.exists(os.path.join(repo, rel)):
            print("HATA: dosya yok: %s" % rel, file=sys.stderr); return 2
        if a.kaynak_tarihi:
            try:
                date.fromisoformat(a.kaynak_tarihi)
            except ValueError:
                print("HATA: --kaynak-tarihi YYYY-MM-DD olmalı", file=sys.stderr); return 2
        olay = {"ts": ts, "kod_sha": head, "kosum_id": kosum_id, "dosya_id": rel, "cekim_tarihi": bugun.isoformat(),
                "kaynak_tarihi": a.kaynak_tarihi, "sonuc": a.sonuc, "not": a.not_}
        yol = os.path.join(repo, "veri", "bronz", "cekim-olay.jsonl")
        os.makedirs(os.path.dirname(yol), exist_ok=True)
        with open(yol, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(olay, ensure_ascii=False) + "\n")
        print("cekim-olay: %s → %s (cekim %s, kaynak %s) · sonraki: katman-hatti (silver damga) + anakronizm-denetim (kuyruk)"
              % (rel, a.sonuc, bugun.isoformat(), a.kaynak_tarihi or "-"))
        return 0

    hedef = kuyruk[:a.n]
    if a.liste or not a.olcum:
        print("bayat-cekim · bugün %s · HEAD %s · D3 kuyruk %d dosya · hedef N=%d → %d" % (bugun.isoformat(), head, len(kuyruk), a.n, len(hedef)))
        d1 = son_d1_bulgular(repo, [h["dosya"] for h in hedef])
        for h in hedef:
            print("  %s  (yaş %s gün, damga %s)" % (h["dosya"], h.get("yas_gun"), h.get("en_yeni_damga")))
            for b in d1.get(h["dosya"], [])[:8]:
                print("      D1 %s" % b)
            if not d1.get(h["dosya"]):
                print("      D1 bulgusu yok (yalnız damga tazeleme adayı)")
        if not hedef:
            print("  kuyruk boş — yeniden-çekim yok (0 aday; uydurma yok)")
    if a.olcum:
        olgular = []
        for metrik, deger, nt in (("bayat_kuyruk_n", len(kuyruk), "D3 kuyruğu (eşik %s gün)" % (kuyruk[0].get("esik_gun") if kuyruk else "90")),
                                  ("cekim_hedef_n", len(hedef), "N=%d politikası (KB-68 a)" % a.n),
                                  ("cekim_bugun_n", bugun_olaylari(repo, bugun), "bugün yazılan cekim-olay satırı")):
            olgular.append({"ts": datetime.now(timezone.utc).isoformat(), "kod_sha": head, "girdi_sha": girdi_sha or "-", "kosum_id": kosum_id,
                            "katman": "bronz", "nesne": "v_bayat_aday.csv", "metrik": metrik, "deger": float(deger), "birim": "adet",
                            "sonuc": "PASS" if metrik != "cekim_bugun_n" or deger >= min(len(hedef), a.n) else "WARN", "not": nt})
        with open(os.path.join(repo, "veri", "katman-olcum.jsonl"), "a", encoding="utf-8") as fh:
            for o in olgular:
                fh.write(json.dumps(o, ensure_ascii=False) + "\n")
        print("ölçüm: " + " · ".join("%s=%d [%s]" % (o["metrik"], o["deger"], o["sonuc"]) for o in olgular) + " → veri/katman-olcum.jsonl")
    return 0


if __name__ == "__main__":
    sys.exit(main())
