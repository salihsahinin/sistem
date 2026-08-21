#!/usr/bin/env python3
"""skill-esik.py — SKILL EŞİK KURALI koşucusu (Salih imzası 2026-08-21, defter Karar 51; kural kaynağı core/ajan-metodolojisi.md §4).

Kural (imzalı, aynen): bir skill×model çifti v_skill_kosum'da n≥10'a ulaştığında medyan token/süre bandı hesaplanır; yeni koşum bandın
2× üstüne çıkarsa seans kapanışında SAPMA satırı raporlanır. OTOMATİK kural değişikliği YOK — her eşik/kural değişikliği ölçüm + Salih imzasıyla.

Deterministik: aynı DB → aynı çıktı; medyan statistics.median; LLM yok. Veri kaynağı v1: amb_olgu_kosum'un KESİN skill eşlemesi
(agent_type='atlas' → atlas-kosum — v_skill_kosum vekil kanalıyla aynı kural; kayıplı haritalama YOK). Kanal genişledikçe (kosum-sonuc /
gorev_emri bağı) kaynak listesi additive büyür. Çıkış 0 = koşum tamam (sapma VARLIĞI hata değildir — rapor aracı); 2 = DB yok (FAIL-LOUD).
Kullanım: python3 tools/skill-esik.py [--repo <yol>] [--esik-n 10] [--carpan 2.0] [--saat 24]
  --saat: "yeni koşum" penceresi (son N saat) — pencere içi sapmalar SAPMA-YENİ, dışındakiler yalnız sayım. Deneysel m.29.
"""
import argparse, os, sqlite3, statistics, sys
from datetime import datetime, timedelta, timezone

ESLEME = {"atlas": "atlas-kosum"}  # yalnız KESİN eşleme (v_skill_kosum vekil kanalı kuralı)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--esik-n", type=int, default=10)
    ap.add_argument("--carpan", type=float, default=2.0)
    ap.add_argument("--saat", type=float, default=24.0)
    a = ap.parse_args()
    db = os.path.join(os.path.abspath(a.repo), "veri", "baglam.sqlite")
    if not os.path.exists(db):
        print(f"HATA: {db} yok", file=sys.stderr); sys.exit(2)
    esik_ts = (datetime.now(timezone.utc) - timedelta(hours=a.saat)).isoformat()
    con = sqlite3.connect(db)
    gruplar = {}
    for agent_type, skill in ESLEME.items():
        for m, tok, sure, ts, kid in con.execute(
                "SELECT modeller, output_tokens, sure_sn, valid_time_bas, kosum_id FROM amb_olgu_kosum WHERE agent_type=?", (agent_type,)):
            gruplar.setdefault((skill, m), []).append((tok, sure, ts, kid))
    con.close()
    sapma_yeni = 0
    for (skill, model), satirlar in sorted(gruplar.items()):
        n = len(satirlar)
        if n < a.esik_n:
            print(f"[ATLA ] {skill} × {model}: n={n} < eşik {a.esik_n} — medyan hesaplanmaz (kural gereği)")
            continue
        med_tok = statistics.median(s[0] for s in satirlar if s[0] is not None)
        sureler = [s[1] for s in satirlar if s[1] is not None]
        med_sure = statistics.median(sureler) if sureler else None
        asanlar = [s for s in satirlar if (s[0] is not None and med_tok and s[0] > a.carpan * med_tok)
                   or (s[1] is not None and med_sure and s[1] > a.carpan * med_sure)]
        yeniler = [s for s in asanlar if (s[2] or "") >= esik_ts]
        print(f"[BANT ] {skill} × {model}: n={n} · medyan {med_tok:.0f} tok / {med_sure:.0f} sn · "
              f"{a.carpan}× üstü toplam {len(asanlar)} · son {a.saat:.0f} saatte {len(yeniler)}")
        for tok, sure, ts, kid in yeniler:
            sapma_yeni += 1
            print(f"[SAPMA-YENİ] {skill} × {model} · {kid} · {tok} tok (medyan×{tok / med_tok:.1f}) · {ts} → teslim raporuna satır")
    if not gruplar:
        print("[BOŞ  ] kesin skill eşlemeli koşum verisi yok (ESLEME kanalları boş)")
    print(f"skill-esik: {len(gruplar)} çift tarandı · yeni-pencere sapması {sapma_yeni} · kural: Karar 51 (otomatik değişiklik YOK)")
    sys.exit(0)


if __name__ == "__main__":
    main()
