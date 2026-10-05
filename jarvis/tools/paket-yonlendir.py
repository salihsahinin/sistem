#!/usr/bin/env python3
"""paket-yonlendir.py — BAĞLAM PAKETİ YÖNLENDİRİCİSİ (Karar 112, Salih 2026-10-05; deneysel m.29; STDLIB ONLY, LLM yok).

Ne bu: tek ajanda (Jarvis) konuya göre bağlam. UserPromptSubmit hook'undan çağrılır (`.claude/hooks/userprompt-dosya.sh`,
prompt-dosya.py'den sonra). Mesajı `core/baglam-paketleri.json` ile eşler ve bağlama KISA bir yönerge basar: aktif paket ·
alt-ajan kademesi · ayrım düzeyi · okunacak adresler · geçişte kapsül yazımı. Dosya gövdesi BASILMAZ; adresi Jarvis Read ile açar
(tam metin, kesilme yok). Aynı (mesaj, durum) → aynı çıktı.

Kural sırası (ilk tutan kazanır):
  k. komut      'paket: kapat|sıfırla|durum'
  a. açık önek  '<paket-id>: ...'
  b. tetik      en çok tetik regex'i tutan paket; eşitlikte aktif paket, sonra manifest sırası;
                aktif paketin puanı ≥ en iyi puan ise aktif pakette kalınır
  c. yapışkan   hiçbiri tutmadıysa aktif pakette kal
  d. sessiz     aktif paket de yoksa çıktı yok (genel sohbet = yalnız çekirdek)

Durum: oturum başına `.claude/hooks/state/paket-<oturum>.json` ({aktif, yuklu[], gecis}); git'e girmez.
Modlar: (varsayılan) stdin hook JSON → yönerge · `--denetle` manifest bütünlüğü (yol var mı · bütçe · regex · kademe).
Kullanım: echo '{"prompt":"veri: silver bayat","session_id":"s"}' | python3 tools/paket-yonlendir.py [--kuru] [--json]
          python3 tools/paket-yonlendir.py --denetle
Çıkış: hook modunda her zaman 0 (prompt'u asla engellemez) · --denetle: 0 temiz · 1 ihlal · 2 manifest okunamadı.
Yazar (eklemeli): durum dosyası · `veri/bronz/paket-olay.jsonl` (karar başına tek satır). `--kuru` ikisini de yazmaz."""
import argparse, datetime, json, os, re, sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SURUM = "0.1"
KOMUTLAR = {"kapat": "kapat", "yok": "kapat", "sıfırla": "sifirla", "sifirla": "sifirla", "durum": "durum"}


def katla(metin):
    """Türkçe-duyarlı küçük harf (İ→i, I→ı); tetikler küçük harfle yazılır."""
    return metin.replace("İ", "i").replace("I", "ı").lower()


def ara(desen, metin, bastan=False):
    """Deseni iki katlamada dener: Türkçe (İ→i, I→ı) ve düz lower() (büyük harfli 'SILVER' gibi İngilizce sözcükler için)."""
    for k in (katla(metin), metin.lower()):
        try:
            e = re.match(desen, k) if bastan else re.search(desen, k)
        except re.error:
            return None
        if e:
            return e
    return None


def manifest_oku(yol):
    with open(yol, encoding="utf-8") as f:
        return json.load(f)


def adres_coz(repo, adres):
    """'yol' ya da 'yol:a-b' → (yol, bayt) ; dosya yoksa (yol, None)."""
    m = re.match(r"^(.+):(\d+)-(\d+)$", adres)
    yol = m.group(1) if m else adres
    tam = os.path.normpath(os.path.join(repo, yol))
    if not os.path.isfile(tam):
        return yol, None
    if not m:
        return yol, os.path.getsize(tam)
    with open(tam, encoding="utf-8", errors="replace") as f:
        satirlar = f.read().split("\n")
    return yol, len("\n".join(satirlar[int(m.group(2)) - 1:int(m.group(3))]).encode("utf-8"))


def denetle(man, repo):
    """Manifest bütünlüğü → ihlal listesi (boş = temiz)."""
    ihlal, gorulen = [], set()
    kademeler = man.get("kademeler", {})
    for ad in ("agir_is", "oncelik"):
        try:
            re.compile(man.get(ad, ""))
        except re.error as e:
            ihlal.append(f"{ad}: regex bozuk ({e})")
    for p in man.get("paketler", []):
        pid = p.get("id", "")
        if not re.fullmatch(r"[a-zçğıöşü-]+", pid):
            ihlal.append(f"{pid!r}: id küçük harf/tire olmalı")
        if pid in gorulen or pid in KOMUTLAR or pid == "paket":
            ihlal.append(f"{pid}: id çakışması")
        gorulen.add(pid)
        if p.get("kademe") not in kademeler:
            ihlal.append(f"{pid}: kademe tanımsız ({p.get('kademe')})")
        for t in p.get("tetik", []):
            try:
                re.compile(t)
            except re.error as e:
                ihlal.append(f"{pid}: tetik regex bozuk {t!r} ({e})")
            if t != katla(t):
                ihlal.append(f"{pid}: tetik küçük harfli olmalı {t!r}")
        toplam = 0
        for a in p.get("cekirdek", []):
            yol, bayt = adres_coz(repo, a)
            if bayt is None:
                ihlal.append(f"{pid}: çekirdek adresi kırık {a}")
            else:
                toplam += bayt
        if toplam > man.get("butce_bayt", 0):
            ihlal.append(f"{pid}: çekirdek {toplam} B > bütçe {man.get('butce_bayt')} B")
        for a in p.get("pointer", []):
            if adres_coz(repo, a)[1] is None:
                ihlal.append(f"{pid}: pointer kırık {a}")
    return ihlal


def yonlendir(prompt, man, durum):
    """Saf karar: (prompt, manifest, durum) → karar sözlüğü. Durumu değiştirmez."""
    paketler = {p["id"]: p for p in man.get("paketler", [])}
    aktif = durum.get("aktif") if durum.get("aktif") in paketler else None
    m = ara(r"^\s*paket\s*:\s*([a-zçğıöşü]+)", prompt, bastan=True)
    if m and m.group(1) in KOMUTLAR:
        return {"kural": "k", "komut": KOMUTLAR[m.group(1)], "paket": aktif, "onceki": aktif, "tutan": []}
    m = ara(r"^\s*([a-zçğıöşü-]+)\s*:", prompt, bastan=True)
    if m and m.group(1) in paketler:
        return {"kural": "a", "paket": m.group(1), "onceki": aktif, "tutan": [m.group(1) + ":"]}
    puan, tutan = {}, {}
    for pid, p in paketler.items():
        bulunan = []
        for t in p.get("tetik", []):
            e = ara(t, prompt)
            if e:
                bulunan.append(e.group(0))
        puan[pid], tutan[pid] = len(bulunan), bulunan
    en_iyi = max(puan.values(), default=0)
    if en_iyi > 0:
        if aktif and puan[aktif] >= en_iyi:
            secilen = aktif
        else:
            secilen = next(pid for pid in paketler if puan[pid] == en_iyi)
        return {"kural": "b", "paket": secilen, "onceki": aktif, "tutan": tutan[secilen]}
    if aktif:
        return {"kural": "c", "paket": aktif, "onceki": aktif, "tutan": []}
    return {"kural": "d", "paket": None, "onceki": None, "tutan": []}


def uygula(karar, prompt, man, durum, repo):
    """Kararı duruma işler → (yeni durum, yönerge metni, kütük alanları)."""
    yeni = {"aktif": durum.get("aktif"), "yuklu": list(durum.get("yuklu", [])), "gecis": int(durum.get("gecis", 0))}
    kapsul_dizin = man.get("kapsul_dizin", "core/paket-kapsul")
    esik = int(man.get("esik_gecis", 3))
    if karar["kural"] == "d":
        return yeni, "", None
    if karar["kural"] == "k":
        komut, onceki = karar["komut"], karar["onceki"]
        if komut == "durum":
            metin = (f"### [paket] durum: aktif {onceki or 'yok'} · yüklü {', '.join(yeni['yuklu']) or 'yok'} · "
                     f"geçiş {yeni['gecis']}/{esik}")
        elif komut == "kapat":
            yeni["aktif"] = None
            metin = "### [paket] kapatıldı: genel sohbet (yalnız çekirdek)."
            if onceki:
                metin += f" Önce çıkan paketin kapsülünü yaz → {kapsul_dizin}/{onceki}.md"
        else:
            yeni = {"aktif": None, "yuklu": [], "gecis": 0}
            metin = "### [paket] sıfırlandı: aktif yok, yüklü yok, geçiş 0 (pencere temizliği ya da sıkıştırma sonrası)."
        return yeni, metin, {"kural": "k", "paket": None, "onceki": onceki, "komut": komut}
    pid, onceki = karar["paket"], karar["onceki"]
    p = next(x for x in man["paketler"] if x["id"] == pid)
    agir = ara(man.get("agir_is") or r"(?!)", prompt)
    oncelik = ara(man.get("oncelik") or r"(?!)", prompt)
    kademe = "fable" if oncelik else p["kademe"]
    kademe_ad = man["kademeler"].get(kademe, kademe)
    ayrim = "alt-ajan" if agir else "ayni-pencere"
    degisti = pid != onceki
    ilk = pid not in yeni["yuklu"]
    if degisti and onceki:
        yeni["gecis"] += 1
    yeni["aktif"] = pid
    cekirdek_bayt = 0
    if not degisti:
        metin = f"### [paket] {pid} (aktif; kural {karar['kural']}) · alt-ajan kademesi {kademe_ad}"
        if oncelik:
            metin += f" (öncelik beyanı: \"{oncelik.group(0)}\")"
        if agir:
            metin += (f" · ağır iş (\"{agir.group(0)}\"): alt-ajana ver, `model: {kademe}`, paket adreslerini emre koy, "
                      f"ana pencereye ≤2k özet")
    else:
        neden = {"a": "açık önek", "b": "tetik: " + ", ".join(karar["tutan"])}.get(karar["kural"], karar["kural"])
        s = [f"### [paket] {pid} · {p.get('ad', '')} (kural {karar['kural']}: {neden})"]
        km = f"- alt-ajan kademesi: {kademe_ad}"
        if oncelik:
            km += f" (öncelik beyanı: \"{oncelik.group(0)}\"; paket varsayılanı {man['kademeler'].get(p['kademe'], p['kademe'])})"
        km += f": yalnız alt-ajana giden işte `model: {kademe}`. Oturum modelini Salih seçer, hatırlatma yapılmaz."
        s.append(km)
        if agir:
            s.append(f"- ayrım: alt-ajan (ağır iş sözcüğü \"{agir.group(0)}\"): paket adreslerini alt-ajan emrine koy, "
                     f"ana pencereye ≤2k özet dönsün.")
        else:
            s.append("- ayrım: aynı pencere.")
        adresler = []
        for a in p.get("cekirdek", []):
            _, bayt = adres_coz(repo, a)
            cekirdek_bayt += bayt or 0
            adresler.append(a if bayt is not None else f"{a} [kırık]")
        if not adresler:
            s.append("- oku: çekirdek dosya yok; pointer'dan adresle ilerle.")
        elif ilk:
            s.append(f"- oku (ilk yükleme, {cekirdek_bayt} B, cevaptan önce Read ile): " + " · ".join(adresler))
        else:
            s.append("- oku: çekirdek bu oturumda yüklendi (" + " · ".join(adresler) + "); pencerede yoksa yeniden oku.")
        if p.get("pointer"):
            s.append("- pointer (gerekince): " + " · ".join(p["pointer"]))
        if p.get("skill"):
            s.append("- ilgili skill: " + " · ".join(p["skill"]))
        kapsul = f"{kapsul_dizin}/{pid}.md"
        if os.path.isfile(os.path.join(repo, kapsul)):
            s.append(f"- konu kapsülü var, oku: {kapsul}")
        if onceki:
            s.append(f"- geçiş {yeni['gecis']}/{esik}: önce çıkan paketin kapsülünü yaz (nerede kaldık · sıradaki adım) → "
                     f"{kapsul_dizin}/{onceki}.md")
        if yeni["gecis"] >= esik:
            s.append(f"- [eşik] {yeni['gecis']} geçiş: açık kapsülleri yaz, Salih'e pencere temizliği (/clear) öner; "
                     f"temizlikten sonra 'paket: sıfırla'.")
        if ilk:
            yeni["yuklu"].append(pid)
        metin = "\n".join(s)
    olay = {"kural": karar["kural"], "paket": pid, "onceki": onceki, "gecis": yeni["gecis"], "ilk_yukleme": bool(degisti and ilk),
            "cekirdek_bayt": cekirdek_bayt, "kademe": kademe, "ayrim": ayrim, "tutan": karar["tutan"]}
    return yeni, metin, olay


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=KOK)
    ap.add_argument("--manifest", default=None, help="varsayılan core/baglam-paketleri.json")
    ap.add_argument("--durum-dizin", default=None, help="varsayılan .claude/hooks/state")
    ap.add_argument("--kuru", action="store_true", help="durum ve kütük yazılmaz")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--denetle", action="store_true", help="manifest bütünlük denetimi")
    a = ap.parse_args()
    man_yol = a.manifest or os.path.join(a.repo, "core", "baglam-paketleri.json")
    if a.denetle:
        try:
            man = manifest_oku(man_yol)
        except (OSError, ValueError) as e:
            print(f"HATA: manifest okunamadı: {man_yol} ({e})", file=sys.stderr)
            return 2
        ihlal = denetle(man, a.repo)
        if a.json:
            print(json.dumps({"arac": "paket-yonlendir", "surum": SURUM, "cikis": 1 if ihlal else 0,
                              "paket_n": len(man.get("paketler", [])), "ihlal": ihlal}, ensure_ascii=False))
        else:
            for i in ihlal:
                print(f"İHLAL {i}")
            print(f"paket {len(man.get('paketler', []))} · ihlal {len(ihlal)}")
        return 1 if ihlal else 0
    try:
        girdi = json.loads(sys.stdin.buffer.read().decode("utf-8", "replace") or "{}")
        man = manifest_oku(man_yol)
    except (OSError, ValueError):
        return 0
    prompt = girdi.get("prompt", "") or ""
    oturum = re.sub(r"[^A-Za-z0-9_-]", "", girdi.get("session_id", "") or "") or "oturumsuz"
    if not prompt.strip():
        return 0
    durum_dizin = a.durum_dizin or os.path.join(a.repo, ".claude", "hooks", "state")
    durum_yol = os.path.join(durum_dizin, f"paket-{oturum}.json")
    try:
        with open(durum_yol, encoding="utf-8") as f:
            durum = json.load(f)
    except (OSError, ValueError):
        durum = {}
    karar = yonlendir(prompt, man, durum)
    yeni, metin, olay = uygula(karar, prompt, man, durum, a.repo)
    if a.json:
        print(json.dumps({"arac": "paket-yonlendir", "surum": SURUM, "cikis": 0, "karar": karar, "durum": yeni,
                          "metin": metin}, ensure_ascii=False))
    elif metin:
        print(metin)
    if olay and not a.kuru:
        os.makedirs(durum_dizin, exist_ok=True)
        with open(durum_yol, "w", encoding="utf-8") as f:
            json.dump(yeni, f, ensure_ascii=False)
        kutuk = os.path.join(a.repo, "veri", "bronz", "paket-olay.jsonl")
        os.makedirs(os.path.dirname(kutuk), exist_ok=True)
        ts = datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(timespec="seconds")
        with open(kutuk, "a", encoding="utf-8") as f:
            f.write(json.dumps(dict({"ts": ts, "oturum": oturum}, **olay, prompt_uzunluk=len(prompt)), ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    sys.exit(main())
