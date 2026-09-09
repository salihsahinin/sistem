#!/usr/bin/env python3
"""karantina.py — İB-72 BAYAT-DOSYA KARANTİNA MEKANİZMASI (STDLIB ONLY; LLM yok; m.8 silme yasağı: taşıma var,
silme YOK). Tescil yetkisi YALNIZ Salih'te — bu araç yalnız MEKANİZMAdır, hiçbir dosyayı kendiliğinden
karantinaya EKLEMEZ (Katman-1 kararı, Carvis çağıramaz).

Ne yapar: `--ekle` bir dosyayı `arsiv/karantina/<yol>` altına `git mv` ile taşır (dizin yapısı korunur;
silme yok, arşive iner — m.8) ve `veri/karantina.jsonl`e (APPEND-ONLY) tek satır ekler: {yol, tescil_tarihi,
salih_beyani, neden, git_head}. `--liste` mevcut tescilleri insan-okur sıralar. `--denetle` iki şeyi
DOĞRULAR: (a) gerçek repo-genel dosya-tarama noktasının (tools/kod-orani-olcum.py `repo_envanteri`;
İB-72 keşfi — bkz. docstring altı "Keşif notu") `arsiv/karantina/` dizinini TARAMADIĞINI (DISLA_DIZIN
kümesi üzerinden statik + canlı kontrol) — tarıyorsa FAIL-LOUD; (b) `veri/karantina.jsonl` şemasının geçerli
olduğunu (her satır 5 zorunlu alanı taşıyor mu).

Keşif notu (İB-72, 09-03): görev metni `katman-hatti.py` ve `erisim-fts.py`'yi aday gösteriyordu; ikisi de
GREP edildi (rglob/os.walk/glob yok) — katman-hatti.py bir ORKESTRATÖRdür (adım adı → alt-script çağırır),
erisim-fts.py SQLite FTS5 üzerinde çalışır, ikisi de dosya sistemini TARAMAZ. Repo-genelinde gerçek
os.walk ile tam-ağaç tarayan tek script `tools/kod-orani-olcum.py::repo_envanteri` (İB-71); `DISLA_DIZIN`
kümesine bu görevde `arsiv/karantina` eklendi (en küçük diff). `tools/kod-envanter.py` `git ls-files`
kullanır — git-tracked karantina dosyalarını YİNE SAYAR (kapsam dışı bırakılmadı; ayrı not, bu görevin
kapsamı değil).

Kullanım:
  python3 tools/karantina.py --ekle <yol> --beyan "<Salih sözü>" [--neden "<kısa gerekçe>"] [--repo <yol>] [--bugun YYYY-MM-DD] [--json]
  python3 tools/karantina.py --liste [--repo <yol>]
  python3 tools/karantina.py --denetle [--repo <yol>] [--json]

Çıkış: 0 tamam · 1 --denetle ihlali (tarama sızıntısı ∨ şema bozuk) · 2 girdi/kullanım hatası (dosya yok,
beyan boş, bilinmeyen bayrak).

Yan-etki (A6): `--ekle` YIKICI-DEĞİL taşıma sınıfı (git mv; içerik/kayıt kaybı yok) + `veri/karantina.jsonl`e
EKLEMELİ satır. `--liste`/`--denetle` salt-okur.

Kayıt: İB-72 (Salih 09-03), Carvis yan-oturum işçi-ajanı. Deneysel m.29.
"""
import argparse, importlib.util, json, os, subprocess, sys
from datetime import date, datetime, timezone

ALANLAR = ("yol", "tescil_tarihi", "salih_beyani", "neden", "git_head")


def hata(mesaj, kod=2):
    """FAIL-LOUD (A7): tek satır teşhis stderr'e, çıkış kodu A2 sözlüğüne göre (varsayılan 2 = kullanım)."""
    print(f"[HATA] {mesaj}", file=sys.stderr)
    sys.exit(kod)


def git_head(repo):
    try:
        r = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, capture_output=True, text=True, timeout=10)
        return r.stdout.strip() if r.returncode == 0 else "-"
    except OSError:
        return "-"


def kutuk_yolu(repo):
    return os.path.join(repo, "veri", "karantina.jsonl")


def kayitlari_oku(repo):
    yol = kutuk_yolu(repo)
    if not os.path.exists(yol):
        return []
    kayitlar = []
    with open(yol, encoding="utf-8") as fh:
        for i, satir in enumerate(fh, 1):
            satir = satir.strip()
            if not satir:
                continue
            try:
                kayitlar.append((i, json.loads(satir)))
            except json.JSONDecodeError as e:
                kayitlar.append((i, {"__bozuk__": str(e), "__ham__": satir}))
    return kayitlar


def cmd_ekle(a, repo, insan):
    if not a.beyan or not a.beyan.strip():
        hata("--beyan zorunlu (Salih sözü olmadan tescil yok — tescil yetkisi Katman-1)")
    kaynak_goreli = a.ekle
    kaynak_tam = os.path.join(repo, kaynak_goreli)
    if not os.path.isfile(kaynak_tam):
        hata(f"dosya yok: {kaynak_goreli}")
    hedef_goreli = os.path.join("arsiv", "karantina", kaynak_goreli)
    hedef_tam = os.path.join(repo, hedef_goreli)
    if os.path.exists(hedef_tam):
        hata(f"hedefte zaten dosya var: {hedef_goreli}")
    os.makedirs(os.path.dirname(hedef_tam), exist_ok=True)
    r = subprocess.run(["git", "mv", kaynak_goreli, hedef_goreli], cwd=repo, capture_output=True, text=True)
    if r.returncode != 0:
        hata(f"git mv başarısız: {r.stderr.strip()}", kod=1)
    tescil_tarihi = a.bugun or date.today().isoformat()
    kayit = {
        "yol": kaynak_goreli,
        "tescil_tarihi": tescil_tarihi,
        "salih_beyani": a.beyan.strip(),
        "neden": (a.neden or a.beyan).strip(),
        "git_head": git_head(repo),
    }
    with open(kutuk_yolu(repo), "a", encoding="utf-8") as fh:
        fh.write(json.dumps(kayit, ensure_ascii=False) + "\n")
    print(f"[TAMAM] {kaynak_goreli} -> {hedef_goreli} (jsonl'e eklendi)", file=insan)
    if a.json:
        print(json.dumps({"arac": "karantina", "cikis": 0, "kayit": kayit}, ensure_ascii=False))
    return 0


def cmd_liste(a, repo, insan):
    kayitlar = kayitlari_oku(repo)
    if not kayitlar:
        print("[BOŞ] veri/karantina.jsonl — henüz hiçbir tescil yok.", file=insan)
        if a.json:
            print(json.dumps({"arac": "karantina", "cikis": 0, "n": 0, "kayitlar": []}, ensure_ascii=False))
        return 0
    for i, k in kayitlar:
        if "__bozuk__" in k:
            print(f"  satir {i}: [BOZUK] {k['__bozuk__']}", file=insan)
            continue
        print(f"  {k.get('tescil_tarihi', '-')}  {k.get('yol', '-')}  — {k.get('salih_beyani', '-')}", file=insan)
    if a.json:
        print(json.dumps({"arac": "karantina", "cikis": 0, "n": len(kayitlar),
                           "kayitlar": [k for _, k in kayitlar]}, ensure_ascii=False))
    return 0


def _kod_orani_modulu(repo):
    """tools/kod-orani-olcum.py'yi yan-etkisiz İÇE AKTARIR (main() çağrılmaz — __name__ guard);
    canlı DISLA_DIZIN kümesini incelemek için (statik metin taramasından daha güvenilir)."""
    yol = os.path.join(repo, "tools", "kod-orani-olcum.py")
    if not os.path.isfile(yol):
        return None, f"tools/kod-orani-olcum.py bulunamadı: {yol}"
    spec = importlib.util.spec_from_file_location("_karantina_denetim_kod_orani", yol)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:  # modül import hatası da FAIL-LOUD'a girer, gizlenmez
        return None, f"import hatası: {e}"
    return mod, None


def cmd_denetle(a, repo, insan):
    sorunlar = []

    mod, mod_hata = _kod_orani_modulu(repo)
    hedef_dizin = os.path.join("arsiv", "karantina")
    if mod_hata:
        sorunlar.append(f"kod-orani-olcum.py incelenemedi: {mod_hata}")
    else:
        disla = getattr(mod, "DISLA_DIZIN", None)
        if disla is None:
            sorunlar.append("kod-orani-olcum.py DISLA_DIZIN sabiti bulunamadı (script değişmiş olabilir)")
        elif hedef_dizin not in disla:
            sorunlar.append(
                f"kod-orani-olcum.py DISLA_DIZIN kümesi '{hedef_dizin}' İÇERMİYOR — gerçek dosya-tarama "
                "noktası karantina dizinini TARIYOR (İB-72 ihlali)")

    kayitlar = kayitlari_oku(repo)
    for i, k in kayitlar:
        if "__bozuk__" in k:
            sorunlar.append(f"veri/karantina.jsonl satır {i}: JSON parse hatası ({k['__bozuk__']})")
            continue
        eksik = [alan for alan in ALANLAR if alan not in k]
        if eksik:
            sorunlar.append(f"veri/karantina.jsonl satır {i}: eksik alan(lar) {eksik}")

    if sorunlar:
        for s in sorunlar:
            print(f"[İHLAL] {s}", file=insan)
        if a.json:
            print(json.dumps({"arac": "karantina", "cikis": 1, "n_sorun": len(sorunlar),
                               "sorunlar": sorunlar}, ensure_ascii=False))
        sys.exit(1)

    print(f"[PASS] tarama-dışı doğrulandı ({hedef_dizin} DISLA_DIZIN'de) · "
          f"{len(kayitlar)} kayıt, şema tutarlı.", file=insan)
    if a.json:
        print(json.dumps({"arac": "karantina", "cikis": 0, "n_kayit": len(kayitlar)}, ensure_ascii=False))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--ekle", metavar="YOL")
    ap.add_argument("--beyan", metavar="METIN")
    ap.add_argument("--neden", metavar="METIN")
    ap.add_argument("--liste", action="store_true")
    ap.add_argument("--denetle", action="store_true")
    ap.add_argument("--bugun", metavar="YYYY-MM-DD")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--sessiz", action="store_true")
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)
    insan = sys.stderr if a.json else sys.stdout

    modlar = [bool(a.ekle), a.liste, a.denetle]
    if sum(modlar) != 1:
        hata("tam olarak biri gerekli: --ekle <yol> --beyan \"…\" | --liste | --denetle")

    if a.ekle:
        return cmd_ekle(a, repo, insan)
    if a.liste:
        return cmd_liste(a, repo, insan)
    if a.denetle:
        return cmd_denetle(a, repo, insan)


if __name__ == "__main__":
    sys.exit(main())
