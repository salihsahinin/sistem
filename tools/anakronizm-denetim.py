#!/usr/bin/env python3
"""anakronizm-denetim.py — ANAKRONİZM FRENİ deterministik denetimi (Karar 68, Salih Katman-1 2026-08-26: "sistemde anakronizm YASAK").
STDLIB ONLY, Python ≥3.9. Kanıt: cc/rapor/2026-08/rapor-2026-08-26-2.md (m.40b wf_9030bba4; yapı-taşları: Google 'timeless documentation' yasak-kelime
listesi [C-YT3] · Vale `conditional` "kalıp varsa aynı kapsamda tarih olmalı" deseni [C-YT4] · Microsoft Learn zorunlu `ms.date` damga-varlığı kapısı
[C-YT5] · actions/stale eşik-tabanlı bayatlama [C-YT6] · Wikipedia {{As of}} → makine-listelenebilir kuyruk [C-YT8] · RFC 9111 tazelik aritmetiği
[B-YT6]). "Hazırı temel al": Vale (Go ikilisi, +1 araç zinciri → KB kalemi) yerine aynı kural stdlib regex'le; Türkçe kalıp listesi hiçbir kaynakta
yok (kör nokta) → burada YAZILDI, deneysel m.29 (yanlış-pozitif oranı ölçülünce kalibre).

ANAKRONİZM (çalışma tanımı): zaman-bağımlı iddianın (sürüm · skor · fiyat · "en güncel/en güçlü" · SDK durumu · kanon kaydı) geçerli olduğu ZAMAN
belirtilmeden bugünün durumu gibi sunulması. Üç kanal: ESKİ KAYIT · MODEL HAFIZASI · KONUŞMA. Bu script yalnız DOSYA katmanını denetler (KONUŞMA
kanalı için kural wiki/anakronizm-freni.md; MODEL HAFIZASI için kesim tablosu veri/model-kesim.jsonl + seans-açılış bloğu).

Üç denetim (hepsi deterministik; aynı dosya → aynı çıktı):
  D1 ZAMAN-ÇİVİ (paragraf kapsamı, Vale-conditional deseni): paragrafta zaman-çivileyen kalıp (Türkçe liste aşağıda; Google 12-grup çevirisi)
     ∨ sürüm/skor kalıbı (v1.2 · %12,5 · "sürüm 3") VAR ama aynı paragrafta ISO tarih (YYYY-MM-DD / YYYY-MM) ∨ "AS-OF" ∨ "(çekim …)" ∨ yıl+ay YOK
     → İHLAL. Kod blokları ve tablo-başlıkları hariç; `--kalip-listesi` ile liste yazdırılır.
  D2 DAMGA-VARLIĞI (ms.date deseni): denetlenen dosyanın ilk 12 satırında en az bir tarih (YYYY-MM-DD ∨ "Kayıt: …" ∨ "AS-OF" ∨ "son teyit") yoksa
     → İHLAL (dosya damgasız).
  D3 BAYATLIK (stale deseni): dosyadaki "son teyit: YYYY-MM-DD" ∨ "AS-OF YYYY-MM-DD" ∨ "Güncelleme: YYYY-MM-DD" damgalarının EN YENİSİ ile bugün
     arasındaki yaş > eşik (varsayılan 90 gün; sınıf-başına eşik KB kalemi) → BAYAT-ADAY (ihlal değil, KUYRUK; m.8 gereği silme yok).

Grain: veri/anakronizm-denetim.jsonl — 1 satır = 1 BULGU {ts, kod_sha, kosum_id, denetim ∈ {D1,D2,D3}, seviye ∈ {İHLAL,UYARI,KUYRUK}, dosya, satir, kalip, ornek, yas_gun, not};
Kalibrasyon (08-26 taban ölçümü, 201 dosya): ilk kalıp seti 1.665 D1 üretti (yanlış-pozitif: "Katman-1" tier kalıbı, çıplak yüzdeler, "mevcut/güncel") →
daraltıldı: sürüm/skor kalıbı tarihsiz paragrafta = İHLAL (çıkış 3); zaman-çivi sözcüğü = UYARI (çıkış kodunu bozmaz; sayı raporlanır, eşik KB kalemi).
append-only. Gold: veri/gorunum/v_bayat_aday.csv (D3 kuyruğu, üzerine yazılır — türetilmiş görünüm).

Kullanım: python3 tools/anakronizm-denetim.py [--repo <yol>] [--dosya <yol> ...] [--kapsam wiki,raporlar,cc,core] [--esik-gun 90]
                                              [--bugun 2026-08-26] [--json] [--kuru] [--sessiz] [--kalip-listesi]
Varsayılan kapsam: wiki/*.md + core/*.md + son 30 günün raporlar/**/*.md ve cc/rapor/**/*.md (git-izlenen). Çıkış: 0 temiz · 3 D1/D2 ihlali var
(D3 yalnız kuyruk) · 2 repo yok. Deneysel m.29 (2026-08-26, Carvis). Additive-only.
"""
import argparse, json, os, re, subprocess, sys
from datetime import date, datetime, timezone, timedelta

# --- Türkçe zaman-çivileyen kalıplar (Google timeless-documentation 12 grubunun çevirisi + Jarvis vakaları; kaynak listesi yok → deneysel) ---
ZAMAN_CIVI = [
    r"\bşu an(da)?\b", r"\bşimdilik\b", r"\bhâlâ\b", r"\bhala\b", r"\bartık\b", r"\bhenüz\b", r"\byakında\b", r"\bson zamanlarda\b",
    r"\ben güncel\b", r"\ben güçlü\b", r"\ben son sürüm\b", r"\ben yeni\b", r"\bbugün itibar[ıi]yla\b", r"\bbu yazının yazıldığı\b",
    r"\byeni sürüm\b", r"\bdesteklenmiyor\b", r"\bresmî sdk'?s[ıi] yok\b", r"\bhenüz yok\b",
]
SURUM_SKOR = [r"\bv\d+\.\d+(\.\d+)?\b", r"\bsürüm\s*\d", r"\bpass@\d+\b", r"\b(?:skor|doğruluk|recall|nDCG|F1|başarı)\S*\s*[:=]?\s*%?\s?\d{1,3}(?:,\d+)?\s?%?"]
TARIH = [r"\b\d{4}-\d{2}(-\d{2})?\b", r"\bAS-?OF\b", r"\bas of\b", r"\bçekim(?:i)?\s*(?:tarihi)?\s*\d{4}", r"\bson[- ]teyit\b", r"\bKayıt:\s*\d{4}",
         r"\b\d{2}-\d{2}\b(?=[^\d])", r"\b(?:0?[1-9]|1[0-2])[-/]\d{4}\b", r"\b(?:Ocak|Şubat|Mart|Nisan|Mayıs|Haziran|Temmuz|Ağustos|Eylül|Ekim|Kasım|Aralık)\s+\d{4}\b",
         r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+'?\d{2,4}\b", r"\b20\d{2}\b"]
DAMGA = [r"\b(\d{4}-\d{2}-\d{2})\b"]
RX = lambda L: re.compile("|".join(L), re.I | re.U)
RX_CIVI, RX_SURUM, RX_TARIH, RX_DAMGA = RX(ZAMAN_CIVI), RX(SURUM_SKOR), RX(TARIH), re.compile(DAMGA[0])


def sh(cmd, cwd=None):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


def paragraflar(metin):
    """Paragraf = boş satırla ayrılan blok; kod blokları (```) atlanır. (başlangıç satır no, metin) döner."""
    out, buf, bas, kod = [], [], 1, False
    for i, satir in enumerate(metin.split("\n"), 1):
        if satir.strip().startswith("```"):
            kod = not kod; continue
        if kod:
            continue
        if satir.strip() == "":
            if buf:
                out.append((bas, "\n".join(buf))); buf = []
            bas = i + 1
        else:
            if not buf:
                bas = i
            buf.append(satir)
    if buf:
        out.append((bas, "\n".join(buf)))
    return out


def d1_zaman_civi(yol, metin):
    bulgular = []
    for bas, p in paragraflar(metin):
        if p.lstrip().startswith("|---"):
            continue
        civi = RX_CIVI.search(p); surum = RX_SURUM.search(p)
        if not (civi or surum):
            continue
        if RX_TARIH.search(p):
            continue
        m = surum or civi
        bulgular.append({"denetim": "D1", "seviye": "İHLAL" if surum else "UYARI", "dosya": yol, "satir": bas, "kalip": m.group(0),
                         "ornek": p.strip().replace("\n", " ")[:160], "yas_gun": None,
                         "not": ("sürüm/skor iddiası, paragrafta tarih/AS-OF yok" if surum else "zaman-çivi sözcüğü, paragrafta tarih yok (uyarı)")})
    return bulgular


def d2_damga_varligi(yol, metin):
    bas = "\n".join(metin.split("\n")[:12])
    if RX_TARIH.search(bas):
        return []
    return [{"denetim": "D2", "dosya": yol, "satir": 1, "kalip": "-", "ornek": bas.strip().replace("\n", " ")[:120], "yas_gun": None, "not": "ilk 12 satırda tarih damgası yok"}]


def cekim_olaylari(repo):
    """Bronz `veri/bronz/cekim-olay.jsonl` (tools/bayat-cekim.py yazar; İB-52) → {dosya_id: en yeni cekim_tarihi (date)}.
    Yeniden-çekim dosyaya dokunmadan damga tazeler; D3 bu damgayı dosya-içi damgalarla birlikte sayar (yoksa boş sözlük)."""
    out = {}
    yol = os.path.join(repo, "veri", "bronz", "cekim-olay.jsonl")
    if not os.path.exists(yol):
        return out
    with open(yol, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                o = json.loads(line); t = date.fromisoformat((o.get("cekim_tarihi") or "")[:10])
            except (json.JSONDecodeError, ValueError):
                continue
            d = o.get("dosya_id")
            if d and (d not in out or t > out[d]):
                out[d] = t
    return out


def d3_bayatlik(yol, metin, bugun, esik, cekim=None):
    tarihler = []
    for m in RX_DAMGA.finditer(metin):
        try:
            t = date.fromisoformat(m.group(1))
        except ValueError:
            continue
        if t <= bugun:
            tarihler.append(t)
    if cekim and cekim <= bugun:
        tarihler.append(cekim)  # İB-52: bronz yeniden-çekim damgası (dosya-dışı)
    if not tarihler:
        return []
    en_yeni = max(tarihler); yas = (bugun - en_yeni).days
    if yas <= esik:
        return []
    return [{"denetim": "D3", "dosya": yol, "satir": 0, "kalip": en_yeni.isoformat(), "ornek": "-", "yas_gun": yas, "not": "en yeni damga eşiği aştı → BAYAT-ADAY (yeniden-çekim kuyruğu; silme yok)"}]


def tarihli_muaf(yol):
    """Karar 88 M4 (Salih hükmü 2026-09-09): yol raporlar/ ∨ cc/ ile başlıyor ∧ dosya adı YYYY-MM-DD taşıyor → D1/D2 muaf
    (dosya adındaki tarih AS-OF damgası sayılır; rapor = o günün kaydı). core/ ve wiki/ bu muafiyetten HARİÇ."""
    return yol.startswith(("raporlar/", "cc/")) and re.search(r"\d{4}-\d{2}-\d{2}", os.path.basename(yol)) is not None


def varsayilan_kapsam(repo, bugun):
    r = sh(["git", "ls-files", "-z"], repo)
    if r.returncode != 0:
        return None
    files = [f for f in r.stdout.split("\0") if f.endswith(".md")]
    secim = []
    sinir = (bugun - timedelta(days=30)).isoformat()
    for f in files:
        if f.startswith("wiki/") or (f.startswith("core/") and "/sablonlar/" not in f):
            secim.append(f)
        elif f.startswith(("raporlar/", "cc/rapor/")):
            m = re.search(r"(\d{4}-\d{2}-\d{2})", f)
            if m and m.group(1) >= sinir:
                secim.append(f)
    return sorted(set(secim))


def main():
    ap = argparse.ArgumentParser(description="Anakronizm freni deterministik denetimi (D1 zaman-çivi · D2 damga-varlığı · D3 bayatlık)")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--dosya", action="append", help="tek dosya (tekrarlanabilir); verilirse kapsam yerine bunlar")
    ap.add_argument("--kapsam", default="", help="virgüllü ön-ek listesi (wiki,core,raporlar,cc); boşsa varsayılan")
    ap.add_argument("--esik-gun", type=int, default=90)
    ap.add_argument("--bugun", default=None, help="YYYY-MM-DD (varsayılan sistem tarihi)")
    ap.add_argument("--json", action="store_true"); ap.add_argument("--kuru", action="store_true"); ap.add_argument("--sessiz", action="store_true")
    ap.add_argument("--kalip-listesi", action="store_true")
    ap.add_argument("--muafiyet-yok", action="store_true", help="Karar 88 M4 tarihli-dosya muafiyetini kapat (eski davranış)")
    a = ap.parse_args()
    if a.kalip_listesi:
        print("ZAMAN-ÇİVİ:", " | ".join(ZAMAN_CIVI)); print("SÜRÜM/SKOR:", " | ".join(SURUM_SKOR)); print("TARİH (muaf kılar):", " | ".join(TARIH)); return 0
    repo = os.path.abspath(a.repo)
    bugun = date.fromisoformat(a.bugun) if a.bugun else date.today()
    if a.dosya:
        dosyalar = [os.path.relpath(os.path.abspath(f), repo) if os.path.isabs(f) else f for f in a.dosya]
    else:
        dosyalar = varsayilan_kapsam(repo, bugun)
        if dosyalar is None:
            print("HATA: git repo değil: %s" % repo, file=sys.stderr); return 2
        if a.kapsam:
            onek = tuple(x.strip() + "/" for x in a.kapsam.split(",") if x.strip())
            dosyalar = [f for f in dosyalar if f.startswith(onek) or any(f.startswith(o.rstrip("/")) for o in onek)]
    head = sh(["git", "rev-parse", "--short", "HEAD"], repo).stdout.strip() or "-"
    ts = datetime.now(timezone(timedelta(hours=3))).replace(microsecond=0).isoformat()
    kosum_id = "anakronizm:%s:%s" % (head, bugun.isoformat())
    bulgular = []
    cekim = cekim_olaylari(repo)
    n_muaf = 0
    for f in dosyalar:
        try:
            metin = open(os.path.join(repo, f), encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        muaf = (not a.muafiyet_yok) and tarihli_muaf(f)
        if muaf:
            n_muaf += 1
            bulgular += d3_bayatlik(f, metin, bugun, a.esik_gun, cekim.get(f))
        else:
            bulgular += d1_zaman_civi(f, metin) + d2_damga_varligi(f, metin) + d3_bayatlik(f, metin, bugun, a.esik_gun, cekim.get(f))
    for b in bulgular:
        b.update({"ts": ts, "kod_sha": head, "kosum_id": kosum_id})
    for b in bulgular:
        b.setdefault("seviye", "İHLAL" if b["denetim"] == "D2" else "KUYRUK")
    n1 = sum(1 for b in bulgular if b["denetim"] == "D1" and b["seviye"] == "İHLAL"); n1u = sum(1 for b in bulgular if b["denetim"] == "D1" and b["seviye"] == "UYARI")
    n2 = sum(1 for b in bulgular if b["denetim"] == "D2"); n3 = sum(1 for b in bulgular if b["denetim"] == "D3")
    if not a.kuru:
        with open(os.path.join(repo, "veri", "anakronizm-denetim.jsonl"), "a", encoding="utf-8") as fh:
            for b in bulgular:
                fh.write(json.dumps(b, ensure_ascii=False) + "\n")
        gd = os.path.join(repo, "veri", "gorunum"); os.makedirs(gd, exist_ok=True)
        with open(os.path.join(gd, "v_bayat_aday.csv"), "w", encoding="utf-8") as fh:
            fh.write("dosya,en_yeni_damga,yas_gun,esik_gun,bugun,kod_sha\n")
            for b in sorted((b for b in bulgular if b["denetim"] == "D3"), key=lambda x: -x["yas_gun"]):
                fh.write("%s,%s,%d,%d,%s,%s\n" % (b["dosya"], b["kalip"], b["yas_gun"], a.esik_gun, bugun.isoformat(), head))
    sonuc = {"ts": ts, "kod_sha": head, "kosum_id": kosum_id, "bugun": bugun.isoformat(), "dosya_sayisi": len(dosyalar), "tarihli_muaf": n_muaf, "D1_ihlal": n1, "D1_uyari": n1u, "D2": n2, "D3": n3,
             "bulgular": bulgular, "yazildi": not a.kuru}
    if a.json:
        print(json.dumps(sonuc, ensure_ascii=False, indent=1))
    elif not a.sessiz:
        print("ANAKRONİZM DENETİMİ · HEAD %s · bugün %s · %d dosya · tarihli-muaf %d · D1 İHLAL (tarihsiz sürüm/skor) %d · D1 UYARI (zaman-çivi) %d · D2 damgasız-dosya %d · D3 bayat-aday %d (eşik %d gün)" % (head, bugun, len(dosyalar), n_muaf, n1, n1u, n2, n3, a.esik_gun))
        onem = {"İHLAL": 0, "KUYRUK": 1, "UYARI": 2}
        for b in sorted(bulgular, key=lambda x: onem[x["seviye"]])[:60]:
            print("  [%s %s] %s:%s  %s  ← %s" % (b["denetim"], b["seviye"], b["dosya"], b["satir"], (b["kalip"] if b["denetim"] != "D3" else "yaş %d gün (damga %s)" % (b["yas_gun"], b["kalip"])), b["ornek"][:100]))
        if len(bulgular) > 60:
            print("  … +%d bulgu (veri/anakronizm-denetim.jsonl)" % (len(bulgular) - 60))
    return 3 if (n1 or n2) else 0


if __name__ == "__main__":
    sys.exit(main())
