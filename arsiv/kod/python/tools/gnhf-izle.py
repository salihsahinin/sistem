#!/usr/bin/env python3
"""gnhf-izle.py — gnhf ajan koşumunun KONUŞMASINI insan-yüzü canlı izler (Karar 84 eki; v0-deneysel m.29, 2026-08-30).

Ne bu: gnhf worktree'sindeki `.gnhf/runs/<run>/iteration-N.jsonl` akış dosyalarını (claude stream-json) okunur satırlara
çevirir ve CANLI takip eder (tail -f benzeri; yeni iterasyon dosyası açılınca ona geçer). Salih'in "gnhf'nin koştuğu
konuşmayı göremiyorum" sorusunun cevabı — ham JSONL yerine: ajan metni, araç çağrıları (⚙ ad + komut/tanım) ve kısaltılmış
araç sonuçları.

Kullanım:
  python3 tools/gnhf-izle.py                # en yeni worktree'yi (~/sistem/jarvis-gnhf-worktrees/*) bulur, baştan basar, takipte kalır
  python3 tools/gnhf-izle.py --worktree <yol>
  python3 tools/gnhf-izle.py --gecmis       # yalnız mevcut içeriği bas, takip etme (çık)
Çıkış: 0 (--gecmis sonu ya da Ctrl-C) · 2 worktree/koşum bulunamadı. LLM YOK, stdlib-only, salt-okur.
"""
import argparse, glob, json, os, sys, time

KOK = os.path.expanduser("~/sistem/jarvis-gnhf-worktrees")


def en_yeni_worktree():
    adaylar = [d for d in glob.glob(os.path.join(KOK, "*")) if os.path.isdir(d)]
    return max(adaylar, key=os.path.getmtime) if adaylar else None


def kisalt(s, n=200):
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[:n] + "…"


def satir_bas(d):
    t = d.get("type")
    if t == "assistant":
        for c in d.get("message", {}).get("content", []):
            ct = c.get("type")
            if ct == "text" and c.get("text", "").strip():
                print("\n🗣  " + c["text"].strip())
            elif ct == "tool_use":
                g = c.get("input", {})
                oz = g.get("description") or g.get("command") or g.get("file_path") or ""
                print("  ⚙ %s — %s" % (c.get("name"), kisalt(oz, 140)))
    elif t == "user":
        for c in d.get("message", {}).get("content", []) if isinstance(d.get("message", {}).get("content"), list) else []:
            if c.get("type") == "tool_result":
                ic = c.get("content")
                if isinstance(ic, list):
                    ic = " ".join(b.get("text", "") for b in ic if isinstance(b, dict))
                print("    ↳ " + kisalt(ic or "", 160))
    elif t == "result":
        print("\n■ İTERASYON SONU · %s · maliyet $%s · %s tur" % (d.get("subtype"), d.get("total_cost_usd", "?"), d.get("num_turns", "?")))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--worktree", default=None)
    ap.add_argument("--gecmis", action="store_true", help="yalnız mevcut içerik; takip yok")
    a = ap.parse_args()
    wt = a.worktree or en_yeni_worktree()
    if not wt or not os.path.isdir(wt):
        sys.exit("[HATA] gnhf worktree bulunamadı (%s); --worktree ver" % KOK)
    kosular = sorted(glob.glob(os.path.join(wt, ".gnhf", "runs", "*")))
    if not kosular:
        sys.exit("[HATA] %s altında koşum yok" % wt)
    run = kosular[-1]
    print("=== gnhf-izle: %s ===" % run)
    gorulen = {}  # dosya -> okunan bayt
    try:
        while True:
            dosyalar = sorted(glob.glob(os.path.join(run, "iteration-*.jsonl")),
                              key=lambda p: int(p.rsplit("-", 1)[1].split(".")[0]))
            for f in dosyalar:
                if f not in gorulen:
                    print("\n═══ %s ═══" % os.path.basename(f)); gorulen[f] = 0
                with open(f, "rb") as fh:
                    fh.seek(gorulen[f]); yeni = fh.read()
                son = yeni.rfind(b"\n")  # yalnız TAM satırları işle; yarım satır sonraki tura kalır (bayt-güvenli)
                islenecek = yeni[: son + 1] if son >= 0 else b""
                gorulen[f] += len(islenecek)
                for l in islenecek.decode("utf-8", "replace").splitlines():
                    if l.strip():
                        try:
                            satir_bas(json.loads(l))
                        except json.JSONDecodeError:
                            pass  # bozuk satır atlanır (akış hatası)
            if a.gecmis:
                break
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[izleme bitti]")


if __name__ == "__main__":
    main()
