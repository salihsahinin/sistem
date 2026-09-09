#!/usr/bin/env python3
"""prompt-dosya.py — İB-79 PROMPT-BAŞI DETERMİNİSTİK DOSYA SEÇİMİ (Karar 88 M12 (a), Salih 2026-09-09; STDLIB ONLY, LLM yok).

UserPromptSubmit hook'undan çağrılır (`.claude/hooks/userprompt-dosya.sh`). Prompt metnini `core/prompt-dosya-tablosu.tsv`
ile eşler; eşleşen her satır için kaynağın YALNIZ tanımlı parçasını (satır aralığı / madde / karar / ledger satırı / kart / uyarı)
stdout'a basar → Claude Code bunu bağlama ekler. Aynı prompt → aynı dosya seti (CLAUDE.md §6 deterministik tasarım).
Her eşleşme `veri/bronz/prompt-dosya-olay.jsonl`e tek satır düşer (hareket kütüğü ailesi; ölçüm: isabet oranı, bayt).

Tablo (TSV, '#' yorum): anahtar<TAB>kaynak<TAB>not
  anahtar : Python regex, büyük/küçük harf duyarsız; ilk yakalama grubu kaynak şablonuna {1} olarak girer
  kaynak  : yol:a-b          → dosyanın a..b satırları
            tuzuk:{1}        → core/tuzuk-v0.md'de "{1}. **" ile başlayan madde (tek satır, ≤BUDGET)
            defter:{1}       → kuyruk/senaryo-defteri.md'de "**Karar {1} (" ile başlayan blok başı + 3 satır
            ledger:{1}       → veri/karar-borcu.jsonl'de borc_id == {1} satırı (baslik · durum · not)
            pano:{1}         → core/pano.md'de "| {1} |" ile başlayan kart satırı
            son:<glob>:N     → glob'a uyan ad-sırasına göre SON dosyanın ilk N satırı
            bolum:yol:## X:N → yol içinde "## X" başlığından itibaren N satır
            uyari:<metin>    → dosya okumaz, metni basar
Bütçe: eşleşme başına ≤ PARCA_BAYT, prompt başına ≤ TOPLAM_BAYT (KB-50 bağlam bütçesi); aşan parça kesilir "…[kesildi]".
Kullanım: echo '{"prompt":"…"}' | python3 tools/prompt-dosya.py [--tablo YOL] [--repo YOL] [--kuru] [--json]
Çıkış kodu her zaman 0 (hook prompt'u asla engellemez)."""
import argparse, datetime, glob, json, os, re, sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARCA_BAYT = 1500
TOPLAM_BAYT = 4000


def tablo_oku(yol):
    satirlar = []
    with open(yol, encoding="utf-8") as f:
        for ham in f:
            s = ham.rstrip("\n")
            if not s or s.startswith("#"):
                continue
            p = s.split("\t")
            if len(p) < 2:
                continue
            satirlar.append({"anahtar": p[0], "kaynak": p[1], "not": p[2] if len(p) > 2 else ""})
    return satirlar


def _oku(repo, yol):
    tam = os.path.join(repo, yol)
    if not os.path.exists(tam):
        return None
    with open(tam, encoding="utf-8", errors="replace") as f:
        return f.read().split("\n")


def kaynak_getir(repo, kaynak):
    """Kaynak şablonunu çöz → (etiket, metin) ya da None."""
    if kaynak.startswith("uyari:"):
        return ("UYARI", kaynak[6:])
    if kaynak.startswith("tuzuk:"):
        n = kaynak[6:]
        L = _oku(repo, "core/tuzuk-v0.md") or []
        for s in L:
            if s.startswith(f"{n}. **"):
                return (f"core/tuzuk-v0.md m.{n}", s)
        return None
    if kaynak.startswith("defter:"):
        n = kaynak[7:]
        L = _oku(repo, "kuyruk/senaryo-defteri.md") or []
        for i, s in enumerate(L):
            if s.startswith(f"**Karar {n} ("):
                return (f"kuyruk/senaryo-defteri.md Karar {n}", "\n".join(L[i:i + 4]))
        return None
    if kaynak.startswith("ledger:"):
        n = kaynak[7:]
        tam = os.path.join(repo, "veri", "karar-borcu.jsonl")
        if not os.path.exists(tam):
            return None
        with open(tam, encoding="utf-8") as f:
            for ham in f:
                try:
                    r = json.loads(ham)
                except ValueError:
                    continue
                if r.get("borc_id") == n:
                    return (f"ledger {n}", f"{r.get('baslik','')} · durum={r.get('durum','')} · not={r.get('not','')}")
        return None
    if kaynak.startswith("pano:"):
        n = kaynak[5:]
        L = _oku(repo, "core/pano.md") or []
        for s in L:
            if s.startswith(f"| {n} |"):
                return (f"core/pano.md {n}", s)
        return None
    if kaynak.startswith("son:"):
        _, g, n = kaynak.split(":", 2)
        adaylar = glob.glob(os.path.join(repo, g))
        if not adaylar:
            return None
        # deterministik "son": dosya adındaki YYYY-MM-DD (Karar 68 AS-OF damgası) → sonra ad; mtime KULLANILMAZ (klon-bağımsız)
        def _tarih(y):
            m = re.search(r"(\d{4}-\d{2}-\d{2})", os.path.basename(y)); return (m.group(1) if m else "", os.path.basename(y))
        yol = os.path.relpath(sorted(adaylar, key=_tarih)[-1], repo)
        L = _oku(repo, yol) or []
        return (f"{yol}:1-{n}", "\n".join(L[:int(n)]))
    if kaynak.startswith("bolum:"):
        _, yol, baslik, n = kaynak.split(":", 3)
        L = _oku(repo, yol) or []
        for i, s in enumerate(L):
            if s.startswith(baslik):
                return (f"{yol} '{baslik}'", "\n".join(L[i:i + int(n)]))
        return None
    m = re.match(r"^(.+):(\d+)-(\d+)$", kaynak)
    if m:
        yol, a, b = m.group(1), int(m.group(2)), int(m.group(3))
        L = _oku(repo, yol)
        if L is None:
            return None
        return (f"{yol}:{a}-{b}", "\n".join(L[a - 1:b]))
    return None


def eslestir(prompt, tablo, repo):
    """Deterministik: tablo sırası, ilk eşleşme; anahtar başına tek parça."""
    parcalar = []
    for t in tablo:
        try:
            m = re.search(t["anahtar"], prompt, re.IGNORECASE)
        except re.error:
            continue
        if not m:
            continue
        kaynak = t["kaynak"]
        if "{1}" in kaynak:
            if not m.groups() or m.group(1) is None:
                continue
            kaynak = kaynak.replace("{1}", m.group(1))
        sonuc = kaynak_getir(repo, kaynak)
        if sonuc is None:
            parcalar.append({"anahtar": t["anahtar"], "kaynak": kaynak, "etiket": None, "metin": "", "not": t["not"]})
            continue
        etiket, metin = sonuc
        if len(metin.encode("utf-8")) > PARCA_BAYT:
            metin = metin.encode("utf-8")[:PARCA_BAYT].decode("utf-8", "ignore") + " …[kesildi]"
        parcalar.append({"anahtar": t["anahtar"], "kaynak": kaynak, "etiket": etiket, "metin": metin, "not": t["not"]})
    return parcalar


def cikti_yaz(parcalar):
    out, toplam, gorulen = [], 0, set()
    for p in parcalar:
        if p["etiket"] is None or p["etiket"] in gorulen:  # aynı parça iki anahtardan geldiyse tek basılır
            continue
        gorulen.add(p["etiket"])
        blok = f"### [prompt-dosya] {p['etiket']}\n{p['metin']}\n"
        b = len(blok.encode("utf-8"))
        if toplam + b > TOPLAM_BAYT:
            out.append(f"### [prompt-dosya] {p['etiket']} — bütçe aşımı, adres verildi, gövde basılmadı")
            continue
        toplam += b
        out.append(blok)
    return "\n".join(out), toplam


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=KOK)
    ap.add_argument("--tablo", default=None, help="varsayılan core/prompt-dosya-tablosu.tsv")
    ap.add_argument("--kuru", action="store_true", help="kütüğe yazma")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    tablo_yol = a.tablo or os.path.join(a.repo, "core", "prompt-dosya-tablosu.tsv")
    try:
        girdi = json.loads(sys.stdin.read() or "{}")
    except ValueError:
        girdi = {}
    prompt = girdi.get("prompt", "") or ""
    oturum = girdi.get("session_id", "")
    if not os.path.exists(tablo_yol) or not prompt.strip():
        return 0
    tablo = tablo_oku(tablo_yol)
    parcalar = eslestir(prompt, tablo, a.repo)
    metin, toplam = cikti_yaz(parcalar)
    if a.json:
        print(json.dumps({"parcalar": parcalar, "toplam_bayt": toplam}, ensure_ascii=False))
    elif metin:
        print(metin)
    if parcalar and not a.kuru:
        kutuk = os.path.join(a.repo, "veri", "bronz", "prompt-dosya-olay.jsonl")
        os.makedirs(os.path.dirname(kutuk), exist_ok=True)
        ts = datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(timespec="seconds")
        with open(kutuk, "a", encoding="utf-8") as f:
            for p in parcalar:
                f.write(json.dumps({"ts": ts, "oturum": oturum, "anahtar": p["anahtar"], "kaynak": p["kaynak"],
                                    "etiket": p["etiket"], "bayt": len(p["metin"].encode("utf-8")),
                                    "prompt_uzunluk": len(prompt)}, ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
