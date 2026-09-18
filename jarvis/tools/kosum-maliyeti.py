#!/usr/bin/env python3
"""kosum-maliyeti.py — Claude Code transkript-JSONL'inden usage/maliyet tablosu (İB-08 icrası, 2026-08-21).

Yol kararı: AB-3 kısa atlası (cc/rapor/2026-08/rapor-2026-08-21-ab3-usage.md) — yol (i) JSONL-parse SÜRDÜRÜLÜR;
format resmen "internal, sürümler arası değişir" (code.claude.com/docs/en/sessions) olduğundan bu betik
SESSİZ yanlış sayı üretmek yerine FAIL-LOUD çalışır (2.1.169 stub-only regresyonu emsali: issue 66486).

Ne yapar:
  1. ~/.claude/projects/<proje>/*.jsonl dosyalarını tarar; assistant kayıtlarından
     gün × model × (ana/yan-ajan) kırılımında koşum + token toplamları çıkarır.
  2. FAIL-LOUD şema freni:
     - hiç .jsonl yoksa → çıkış 2
     - assistant kaydında message.usage ya da model eksikse → şema-ihlal sayacı; oran > %1 → çıkış 1
     - >50 KB olduğu hâlde 0 assistant kaydı taşıyan dosya → "stub şüphesi" listesi (2.1.169 sınıfı); ≥1 dosya → çıkış 1
  3. Model-düşümü izi: --beklenen <model> verilirse ANA-zincir (isSidechain=false) koşumlarında
     beklenen-dışı model sayısını raporlar (yan-ajanlar alt modelde koşar, normaldir — ayrı sayılır).
  4. Çapraz-doğrulama (AB-3 sertleştirme #2): --dogrula <claude-p-json> ile
     `claude -p --output-format json` çıktısındaki usage/session_id alanları aynı oturumun
     JSONL toplamıyla kıyaslanır (resmî arayüz ↔ iç format tutarlılık örneklemi).

Koşum:
  python3 tools/kosum-maliyeti.py [--proje -Users-HasanSalihSahin-sistem-jarvis] [--gun 7]
                                  [--beklenen claude-fable-5] [--csv veri/gorunum/v_usage_gunluk.csv]
                                  [--dogrula /yol/claude-p-cikti.json]
Çıkış kodları: 0 temiz · 1 şema-freni tetiklendi (sayılar ŞÜPHELİ damgalı basılır) · 2 veri yok.
stdlib-only. Rakam damgası (m.39): tüm sayılar bu koşumun transkript dosyalarından; kestirim yok.
"""
import argparse, csv, glob, json, os, sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone

ESIK_STUB_BAYT = 50_000      # bu boyutun üstünde 0 assistant kaydı → stub şüphesi (2.1.169 sınıfı)
ESIK_IHLAL_ORAN = 0.01       # assistant kayıtlarında şema-ihlal oranı eşiği

def tara(dosyalar, gun_sinir):
    """Dönüş: (tablo, saf_toplam, sayaçlar). tablo[(gün, model, zincir)] = {kosum,in,out,cr,cc}"""
    tablo = defaultdict(lambda: {"kosum": 0, "input": 0, "output": 0, "cache_read": 0, "cache_create": 0})
    oturum = defaultdict(lambda: {"input": 0, "output": 0})  # sessionId → toplam (--dogrula için)
    say = {"dosya": 0, "satir": 0, "assistant": 0, "ihlal": 0, "parse_hata": 0, "stub_suphesi": []}
    for f in dosyalar:
        say["dosya"] += 1
        a_sayisi = 0
        try:
            with open(f, encoding="utf-8") as fh:
                for line in fh:
                    say["satir"] += 1
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        r = json.loads(line)
                    except json.JSONDecodeError:
                        say["parse_hata"] += 1
                        continue
                    if r.get("type") != "assistant":
                        continue
                    a_sayisi += 1
                    say["assistant"] += 1
                    m = r.get("message") or {}
                    u = m.get("usage") or {}
                    model, ts = m.get("model"), r.get("timestamp")
                    if not model or not ts or "output_tokens" not in u:
                        say["ihlal"] += 1
                        continue
                    gun = ts[:10]
                    if gun_sinir and gun < gun_sinir:
                        continue
                    zincir = "yan" if r.get("isSidechain") else "ana"
                    h = tablo[(gun, model, zincir)]
                    h["kosum"] += 1
                    h["input"] += u.get("input_tokens", 0)
                    h["output"] += u.get("output_tokens", 0)
                    h["cache_read"] += u.get("cache_read_input_tokens", 0)
                    h["cache_create"] += u.get("cache_creation_input_tokens", 0)
                    sid = r.get("sessionId")
                    if sid:
                        oturum[sid]["input"] += u.get("input_tokens", 0)
                        oturum[sid]["output"] += u.get("output_tokens", 0)
        except OSError as e:
            print(f"HATA: {f} okunamadı: {e}", file=sys.stderr)
            say["ihlal"] += 1
            continue
        if a_sayisi == 0 and os.path.getsize(f) > ESIK_STUB_BAYT:
            say["stub_suphesi"].append(os.path.basename(f))
    return tablo, oturum, say

def main():
    p = argparse.ArgumentParser(description="Transkript-JSONL usage tablosu (FAIL-LOUD; İB-08)")
    p.add_argument("--proje", default="-Users-HasanSalihSahin-sistem-jarvis",
                   help="~/.claude/projects altındaki proje dizini adı; 'HEPSI' = tüm projeler")
    p.add_argument("--gun", type=int, default=7, help="son N gün (0 = tümü)")
    p.add_argument("--beklenen", default=None, help="ana-zincirde beklenen model (düşüm izi)")
    p.add_argument("--csv", default=None, help="gold CSV çıktısı (ör. veri/gorunum/v_usage_gunluk.csv)")
    p.add_argument("--dogrula", default=None, help="claude -p --output-format json çıktı dosyası")
    a = p.parse_args()

    kok = os.path.expanduser("~/.claude/projects")
    desen = os.path.join(kok, "*" if a.proje == "HEPSI" else a.proje, "*.jsonl")
    dosyalar = sorted(glob.glob(desen))
    if not dosyalar:
        print(f"FAIL-LOUD: hiç transkript bulunamadı: {desen}", file=sys.stderr)
        return 2

    gun_sinir = None
    if a.gun:
        gun_sinir = (datetime.now(timezone.utc) - timedelta(days=a.gun)).strftime("%Y-%m-%d")

    tablo, oturum, say = tara(dosyalar, gun_sinir)

    fren = []
    oran = (say["ihlal"] / say["assistant"]) if say["assistant"] else 0.0
    if say["assistant"] == 0:
        fren.append("assistant kaydı 0 — format değişmiş ya da stub-only olabilir (2.1.169 sınıfı)")
    if oran > ESIK_IHLAL_ORAN:
        fren.append(f"şema-ihlal oranı %{oran*100:.1f} > %{ESIK_IHLAL_ORAN*100:.0f} ({say['ihlal']}/{say['assistant']})")
    if say["stub_suphesi"]:
        fren.append(f"stub şüphesi ({len(say['stub_suphesi'])} dosya >50KB, 0 assistant): {', '.join(say['stub_suphesi'][:3])}…")

    baslik = f"# usage tablosu · {say['dosya']} dosya · {say['assistant']} assistant kaydı · pencere: son {a.gun or 'tüm'} gün"
    if fren:
        baslik += "  [ŞÜPHELİ — fren tetiklendi]"
    print(baslik)
    print(f"{'gün':<12}{'model':<24}{'zincir':<7}{'koşum':>7}{'input':>10}{'output':>10}{'cache_rd':>12}{'cache_cr':>10}")
    for (gun, model, zincir) in sorted(tablo):
        h = tablo[(gun, model, zincir)]
        print(f"{gun:<12}{model:<24}{zincir:<7}{h['kosum']:>7}{h['input']:>10}{h['output']:>10}{h['cache_read']:>12}{h['cache_create']:>10}")

    if a.beklenen:
        sapma = {(g, m): tablo[(g, m, "ana")]["kosum"] for (g, m, z) in tablo
                 if z == "ana" and m != a.beklenen}
        if sapma:
            print(f"\nMODEL-DÜŞÜMÜ İZİ (ana-zincir, beklenen={a.beklenen}):")
            for (g, m), n in sorted(sapma.items()):
                print(f"  {g}  {m}  {n} koşum")
        else:
            print(f"\nmodel-düşümü izi: ana-zincir tamamen {a.beklenen} (pencere içinde)")

    if a.csv:
        os.makedirs(os.path.dirname(a.csv), exist_ok=True)
        with open(a.csv, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["gun", "model", "zincir", "kosum", "input_tok", "output_tok", "cache_read_tok", "cache_create_tok"])
            for (gun, model, zincir) in sorted(tablo):
                h = tablo[(gun, model, zincir)]
                w.writerow([gun, model, zincir, h["kosum"], h["input"], h["output"], h["cache_read"], h["cache_create"]])
        print(f"\nCSV yazıldı: {a.csv}")

    if a.dogrula:
        try:
            with open(a.dogrula, encoding="utf-8") as fh:
                d = json.load(fh)
        except (OSError, json.JSONDecodeError) as e:
            print(f"FAIL-LOUD: --dogrula dosyası okunamadı: {e}", file=sys.stderr)
            return 1
        sid = d.get("session_id")
        du = d.get("usage") or {}
        if not sid or "output_tokens" not in du:
            print("FAIL-LOUD: --dogrula çıktısında session_id/usage yok — resmî arayüz şeması da değişmiş", file=sys.stderr)
            return 1
        j = oturum.get(sid)
        print(f"\nÇAPRAZ-DOĞRULAMA oturum {sid}:")
        if j is None:
            print("  UYARI: bu session JSONL taramasında bulunamadı (pencere dışı ya da yazılmamış — 2.1.169 sınıfı şüphe)")
            fren.append("çapraz-doğrulama: session JSONL'de yok")
        else:
            print(f"  resmî arayüz output={du.get('output_tokens')} ↔ JSONL toplam output={j['output']}"
                  f"  {'UYUŞUR' if du.get('output_tokens', -1) <= j['output'] else 'UYUŞMAZ — format sapması şüphesi'}")
            if du.get("output_tokens", -1) > j["output"]:
                fren.append("çapraz-doğrulama: resmî usage > JSONL toplamı")

    if fren:
        print("\nFREN RAPORU (sayılar ŞÜPHELİ damgalı kullanılmalı):", file=sys.stderr)
        for f_ in fren:
            print(f"  - {f_}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
