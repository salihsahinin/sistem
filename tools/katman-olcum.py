#!/usr/bin/env python3
"""katman-olcum.py — Jarvis veri-mühendisliği katmanı: ÖLÇÜM + VERİ-TESTİ + FRESHNESS + ŞEKİL-SÖZLEŞMESİ (STDLIB ONLY, Python ≥3.9).

Kanon: core/veri-muhendisligi-katmani.md (deneysel m.29). Kanıt: cc/rapor-2026-08-16-2.md (AB-YT4 oran yerel ölçülür · AB-YT6
şekil↔içerik sözleşmesi + additive-only + FAIL-LOUD preflight · CD-YT1 freshness sözleşmesi · CD-YT2 test çekirdeği [unique ·
not_null · accepted_values · relationships] sonuçları APPEND-ONLY kütüğe · CD-YT6 COST tabanı).

Grain (world-model §2 kuralı): veri/katman-olcum.jsonl — 1 satır = 1 ÖLÇÜM OLGUSU {ts, kod_sha, girdi_sha, koşum_id, katman, nesne, metrik,
deger, birim, sonuc, not}. Uzun format; append-only (m.8: silinmez); tekrar-üretilebilir (aynı HEAD + aynı disk → aynı değerler; ts hariç).

Katmanlar (yüklem = koşul, ad değil): BRONZ = git-izlenen md/jsonl/json + koşum kütükleri (provenans = commit) · SİLVER = veri/baglam.sqlite
conformed tablolar (1:1, tipli, tekil, agrege-olmayan) · GOLD = veri/gorunum/*.csv + SQL görünümler (tek-tanım metrik).

Kullanım: python3 tools/katman-olcum.py [--repo <yol>] [--simdi 2026-08-16T02:00:00] [--sozlesme-yaz] [--kuru] [--sessiz]
Çıkış: 0 tamam · 3 veri-testi ERROR · 4 sözleşme KIRICI · 5 freshness ERROR (yüksek kod baskın). Uyarılar (warn) çıkışı değiştirmez.\nEk (08-22, KB-53 (a) İB-25): erişim testleri T1 (tarama-plan noktasal SCAN=0) · T2 (sqlite_stat1 ∧ tazelik; WARN) · T3 (dbstat b-ağacı derinliği, bilgi olgusu).
"""
import argparse, csv, glob, json, os, sqlite3, subprocess, sys
from datetime import datetime, timezone, timedelta

# --- deneysel m.29 sabitler (ilk 3 koşumda kalibre) ---
FRESH = {"bronz": {"warn_gun": 3, "error_gun": 14}, "silver": {"warn_gun": 3, "error_gun": 14}, "gold": {"warn_gun": 7, "error_gun": 30}}
SOZLESME_TABLOLAR = ["dosya", "kayit", "referans", "anahtar", "karar_borcu", "karar_borcu_kaynak", "prompt", "amb_olgu_kosum", "amb_olgu_tahmin", "amb_olgu_kosum_sonuc",
                     "anahtar_kaydi", "silver_kuyruk", "silver_saglik_son", "silver_karantina_aday", "baglam_olay", "erisim_genisletme"]  # silver-sağlık (İB-42, 08-22)
TESTLER = [  # (ad, tür, sql → ihlal sayısı, şiddet)
    ("kayit.kayit_id unique", "unique", "SELECT COUNT(*) FROM (SELECT kayit_id FROM kayit GROUP BY kayit_id HAVING COUNT(*)>1)", "error"),
    ("kayit.dosya_id not_null", "not_null", "SELECT COUNT(*) FROM kayit WHERE dosya_id IS NULL OR dosya_id=''", "error"),
    ("kayit.dosya_id → dosya", "relationships", "SELECT COUNT(*) FROM kayit k LEFT JOIN dosya d ON d.dosya_id=k.dosya_id WHERE d.dosya_id IS NULL", "error"),
    ("referans.kayit_id → kayit", "relationships", "SELECT COUNT(*) FROM referans r LEFT JOIN kayit k ON k.kayit_id=r.kayit_id WHERE k.kayit_id IS NULL", "error"),
    ("dosya.katman accepted_values", "accepted_values", "SELECT COUNT(*) FROM dosya WHERE katman NOT IN ('sicak','ilik','soguk','yapisal')", "error"),
    ("anahtar.anahtar_id unique", "unique", "SELECT COUNT(*) FROM (SELECT anahtar_id FROM anahtar GROUP BY anahtar_id HAVING COUNT(*)>1)", "error"),
    ("karar_borcu.borc_id unique", "unique", "SELECT COUNT(*) FROM (SELECT borc_id FROM karar_borcu GROUP BY borc_id HAVING COUNT(*)>1)", "error"),
    ("karar_borcu.durum accepted_values", "accepted_values", "SELECT COUNT(*) FROM karar_borcu WHERE durum NOT IN ('İMZASIZ','BEKLET','Salih''te','masaya','kısmen-kapandı','kapandı','belirsiz','icra-sırada')", "warn"),
    ("karar_borcu_kaynak.borc_id → karar_borcu", "relationships", "SELECT COUNT(*) FROM karar_borcu_kaynak x LEFT JOIN karar_borcu b ON b.borc_id=x.borc_id WHERE b.borc_id IS NULL", "error"),
    ("karar_borcu_kaynak.satir_var (kırık pointer)", "singular", "SELECT COUNT(*) FROM karar_borcu_kaynak WHERE satir_var=0 OR dosya_var=0", "warn"),
    ("prompt.prompt_id unique", "unique", "SELECT COUNT(*) FROM (SELECT prompt_id FROM prompt GROUP BY prompt_id HAVING COUNT(*)>1)", "error"),
    ("amb_olgu_kosum.kosum_id unique", "unique", "SELECT COUNT(*) FROM (SELECT kosum_id FROM amb_olgu_kosum GROUP BY kosum_id HAVING COUNT(*)>1)", "error"),
    ("amb_olgu_prompt ↔ prompt 1:1", "relationships", "SELECT ABS((SELECT COUNT(*) FROM amb_olgu_prompt)-(SELECT COUNT(*) FROM prompt))", "error"),
    ("amb_olgu_tahmin.tahmin_id unique", "unique", "SELECT COUNT(*) FROM (SELECT tahmin_id FROM amb_olgu_tahmin GROUP BY tahmin_id HAVING COUNT(*)>1)", "error"),
    ("amb_olgu_tahmin.wf_id → amb_olgu_kosum", "relationships", "SELECT COUNT(*) FROM amb_olgu_tahmin t WHERE t.wf_id IS NOT NULL AND NOT EXISTS (SELECT 1 FROM amb_olgu_kosum k WHERE k.wf_id=t.wf_id)", "error"),
    ("amb_olgu_tahmin bant tutarlılığı (min≤max)", "singular", "SELECT COUNT(*) FROM amb_olgu_tahmin WHERE (tahmin_cikti_min>tahmin_cikti_max) OR (tahmin_arac_min>tahmin_arac_max) OR (tahmin_sure_min_sn>tahmin_sure_max_sn) OR (tahmin_girdi_min>tahmin_girdi_max)", "error"),
    ("amb_olgu_kosum_sonuc.sonuc accepted_values", "accepted_values", "SELECT COUNT(*) FROM amb_olgu_kosum_sonuc WHERE sonuc NOT IN ('PASS','FAIL')", "error"),
    ("amb_olgu_kosum_sonuc.kosum_id → amb_olgu_kosum", "relationships", "SELECT COUNT(*) FROM amb_olgu_kosum_sonuc s LEFT JOIN amb_olgu_kosum k ON k.kosum_id=s.kosum_id WHERE k.kosum_id IS NULL", "error"),
]


def sh(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True).stdout.strip()


def olc_bronz(repo):
    files = [f for f in sh(["git", "ls-files", "-z"], repo).split("\0") if f.endswith((".md", ".jsonl", ".json"))]
    byt = 0; klasor = {}
    for f in files:
        try: b = os.path.getsize(os.path.join(repo, f))
        except OSError: b = 0
        byt += b; k = f.split("/")[0] if "/" in f else "."; klasor[k] = klasor.get(k, 0) + 1
    son = sh(["git", "log", "-1", "--format=%cI"], repo)
    return {"dosya": len(files), "byte": byt, "token_kestirim": byt // 4, "son_commit": son, "klasor": klasor}


def olc_silver(repo):
    yol = os.path.join(repo, "veri", "baglam.sqlite")
    if not os.path.exists(yol):
        return None
    con = sqlite3.connect(yol)
    tablolar = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
    gorunumler = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='view' ORDER BY name")]
    satir = {t: con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0] for t in tablolar}
    try:
        u = con.execute("SELECT uretim_zamani, git_head_sha FROM uretim ORDER BY uretim_zamani DESC LIMIT 1").fetchone()
    except sqlite3.Error:
        u = None
    metin_byte = con.execute("SELECT COALESCE(SUM(LENGTH(metin)),0) FROM kayit").fetchone()[0] if "kayit" in tablolar else 0
    con.close()
    return {"byte": os.path.getsize(yol), "tablolar": satir, "gorunum_sayisi": len(gorunumler), "gorunumler": gorunumler,
            "uretim_zamani": u[0] if u else None, "girdi_sha": u[1] if u else None, "kayit_metin_byte": metin_byte}


def olc_gold(repo):
    out = {}
    for f in sorted(glob.glob(os.path.join(repo, "veri", "gorunum", "*.csv"))):
        n = sum(1 for _ in open(f, encoding="utf-8", errors="replace")) - 1
        out[os.path.basename(f)] = {"byte": os.path.getsize(f), "satir": max(n, 0), "mtime": datetime.fromtimestamp(os.path.getmtime(f), tz=timezone.utc).isoformat()}
    return out


def testleri_kos(repo):
    yol = os.path.join(repo, "veri", "baglam.sqlite")
    if not os.path.exists(yol):
        return []
    con = sqlite3.connect(yol); res = []
    for ad, tur, sql, sev in TESTLER:
        try:
            n = con.execute(sql).fetchone()[0]; sonuc = "PASS" if n == 0 else ("ERROR" if sev == "error" else "WARN")
        except sqlite3.Error as e:
            n, sonuc = None, f"SKIP({str(e)[:40]})"
        res.append({"test": ad, "tur": tur, "ihlal": n, "siddet": sev, "sonuc": sonuc})
    con.close(); return res


def sozlesme_yaz(repo):
    yol = os.path.join(repo, "veri", "baglam.sqlite"); d = os.path.join(repo, "veri", "sozlesme"); os.makedirs(d, exist_ok=True)
    con = sqlite3.connect(yol); yazilan = []
    for t in SOZLESME_TABLOLAR:
        cols = [{"ad": r[1], "tip": r[2] or "ANY", "not_null": bool(r[3]), "pk": bool(r[5])} for r in con.execute(f"PRAGMA table_info({t})")]
        if not cols: continue
        s = {"tablo": t, "surum": "1.0.0-deneysel-m29", "katman": "silver", "grain": "-", "kolonlar": cols,
             "kural": "additive-only: kolon EKLEME serbest; silme/tip değişimi/kısıt kaldırma = KIRICI (yeni sürüm + emeklilik damgası)"}
        p = os.path.join(d, f"{t}.json"); json.dump(s, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1); yazilan.append(p)
    con.close(); return yazilan


def preflight(repo):
    yol = os.path.join(repo, "veri", "baglam.sqlite"); d = os.path.join(repo, "veri", "sozlesme")
    if not (os.path.exists(yol) and os.path.isdir(d)): return []
    con = sqlite3.connect(yol); res = []
    for p in sorted(glob.glob(os.path.join(d, "*.json"))):
        s = json.load(open(p, encoding="utf-8"))
        if "tablo" not in s: continue  # kural/şartname JSON'ları (ör. silver-saglik-kurallar.json) şekil sözleşmesi değildir
        t = s["tablo"]
        canli = {r[1]: (r[2] or "ANY") for r in con.execute(f"PRAGMA table_info({t})")}
        kirici, ek = [], []
        for c in s["kolonlar"]:
            if c["ad"] not in canli: kirici.append(f"{t}.{c['ad']} SİLİNMİŞ")
            elif canli[c["ad"]] != c["tip"]: kirici.append(f"{t}.{c['ad']} tip {c['tip']}→{canli[c['ad']]}")
        for k in canli:
            if k not in {c["ad"] for c in s["kolonlar"]}: ek.append(f"{t}.{k} (additive, sözleşmeye eklenmeli)")
        res.append({"tablo": t, "kirici": kirici, "additive_ek": ek, "sonuc": "KIRICI" if kirici else ("EK" if ek else "PASS")})
    con.close(); return res


def gun_farki(iso, simdi):
    if not iso: return None
    try:
        t = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        if t.tzinfo is None: t = t.replace(tzinfo=timezone.utc)
        return (simdi - t).total_seconds() / 86400.0
    except Exception:
        return None


def freshness(bronz, silver, gold, simdi, head):
    out = []
    def hukum(k, gun):
        if gun is None: return "BİLİNMİYOR"
        if gun > FRESH[k]["error_gun"]: return "ERROR"
        if gun > FRESH[k]["warn_gun"]: return "WARN"
        return "PASS"
    g = gun_farki(bronz["son_commit"], simdi); out.append({"katman": "bronz", "nesne": "git HEAD", "yas_gun": g, "sonuc": hukum("bronz", g)})
    if silver:
        g = gun_farki(silver["uretim_zamani"], simdi); h = hukum("silver", g)
        if silver["girdi_sha"] and head and not head.startswith(silver["girdi_sha"][:7]) and h == "PASS": h = "WARN"
        out.append({"katman": "silver", "nesne": "baglam.sqlite", "yas_gun": g, "sonuc": h, "not": f"girdi_sha {silver['girdi_sha']} ↔ HEAD {head}"})
    for ad, v in gold.items():
        g = gun_farki(v["mtime"], simdi); out.append({"katman": "gold", "nesne": ad, "yas_gun": g, "sonuc": hukum("gold", g)})
    return out


def erisim_testleri(repo, head):
    """KB-53 (a) İB-25 — erişim-yolu testleri (T1-T3). T1: noktasal sorgu seti EQP'de SCAN yok → tarama-plan.py son koşumundan okunur
    (aynı hatta önce koşar; tek tanım orada) · T2: sqlite_stat1 var (katman-hatti hijyeni ANALYZE) ∧ uretim.git_head_sha = HEAD (tazelik)
    · T3: dbstat b-ağacı derinliği (bilgi satırı; dbstat yoksa 'yok'). Dönüş: (test listesi [test,tur,ihlal,sonuc], bilgi olguları [(nesne,metrik,deger,birim,not)])."""
    testler, bilgi = [], []
    yol = os.path.join(repo, "veri", "baglam.sqlite")
    # T1 — tarama-plan son koşumu (stat1-yok durumu; noktasal sınıf)
    tp = os.path.join(repo, "veri", "tarama-plan.jsonl"); son_ts, ihlal1, n1 = None, 0, 0
    if os.path.exists(tp):
        rows = []
        with open(tp, encoding="utf-8") as fh:
            for line in fh:
                try: rows.append(json.loads(line))
                except Exception: pass
        if rows:
            son_ts = max(r.get("ts", "") for r in rows)
            for r in rows:
                if r.get("ts") == son_ts and r.get("tur") == "noktasal" and r.get("durum") != "analiz-kopya":
                    n1 += 1
                    if str(r.get("sinif", "")).startswith("SCAN"): ihlal1 += 1
    testler.append({"test": "erisim T1 noktasal sorgu SCAN yok (tarama-plan son koşum, %d sorgu)" % n1, "tur": "erisim", "ihlal": ihlal1,
                    "sonuc": "PASS" if (n1 and ihlal1 == 0) else ("WARN" if n1 == 0 else "ERROR")})
    if not os.path.exists(yol):
        return testler, bilgi
    con = sqlite3.connect(yol)
    # T2 — stat1 ∧ tazelik
    try:
        stat1 = con.execute("SELECT COUNT(*) FROM sqlite_stat1").fetchone()[0]
    except sqlite3.Error:
        stat1 = 0
    try:
        u = con.execute("SELECT git_head_sha FROM uretim ORDER BY uretim_zamani DESC LIMIT 1").fetchone(); taze = bool(u and head and u[0].startswith(head))
    except sqlite3.Error:
        taze = False
    ihlal2 = (0 if stat1 > 0 else 1) + (0 if taze else 1)
    testler.append({"test": "erisim T2 sqlite_stat1 var (%d) ∧ uretim.head = HEAD (%s)" % (stat1, "evet" if taze else "HAYIR"), "tur": "erisim", "ihlal": ihlal2, "sonuc": "PASS" if ihlal2 == 0 else "WARN"})
    # T3 — dbstat derinlik (bilgi)
    try:
        for ad, derinlik, sayfa in con.execute("""SELECT name, MAX(LENGTH(path)-LENGTH(REPLACE(path,'/',''))) AS derinlik, COUNT(*) AS sayfa FROM dbstat
                                                  WHERE name IN ('kayit','ix_kayit_dosya','ix_kayit_dosya_satir','referans','ix_ref_kayit','ix_ref_tur_deger','anahtar','karar_borcu')
                                                  GROUP BY name ORDER BY name"""):
            bilgi.append((ad, "btree_derinlik", derinlik, "seviye", "dbstat; sayfa %d" % sayfa))
    except sqlite3.Error as e:
        bilgi.append(("dbstat", "btree_derinlik", None, "seviye", "dbstat yok: %s" % str(e)[:60]))
    con.close()
    return testler, bilgi


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--simdi", default=None, help="ISO zaman (determinizm/test); varsayılan şimdi (UTC)")
    ap.add_argument("--sozlesme-yaz", action="store_true", help="veri/sozlesme/*.json şekil sözleşmelerini canlı şemadan yaz (ilk kurulum / sürüm artışı)")
    ap.add_argument("--kuru", action="store_true"); ap.add_argument("--sessiz", action="store_true")
    a = ap.parse_args(); repo = os.path.abspath(a.repo)
    simdi = datetime.fromisoformat(a.simdi).replace(tzinfo=timezone.utc) if a.simdi else datetime.now(timezone.utc)
    head = sh(["git", "rev-parse", "--short", "HEAD"], repo)
    if a.sozlesme_yaz:
        for p in sozlesme_yaz(repo): print("sözleşme yazıldı:", os.path.relpath(p, repo))
    bronz, silver, gold = olc_bronz(repo), olc_silver(repo), olc_gold(repo)
    testler, pf = testleri_kos(repo), preflight(repo)
    et, ebilgi = erisim_testleri(repo, head); testler = testler + et  # KB-53 (a) İB-25 T1-T3
    fr = freshness(bronz, silver, gold, simdi, head)
    kosum_id = f"{simdi.strftime('%Y%m%dT%H%M%S')}-{head}"
    olgular = []
    def olgu(katman, nesne, metrik, deger, birim, sonuc="-", not_=""):
        olgular.append({"ts": simdi.isoformat(), "kod_sha": head, "girdi_sha": (silver or {}).get("girdi_sha"), "kosum_id": kosum_id,
                        "katman": katman, "nesne": nesne, "metrik": metrik, "deger": deger, "birim": birim, "sonuc": sonuc, "not": not_})
    olgu("bronz", "git md/jsonl/json", "dosya", bronz["dosya"], "adet"); olgu("bronz", "git md/jsonl/json", "byte", bronz["byte"], "byte")
    olgu("bronz", "git md/jsonl/json", "token_kestirim", bronz["token_kestirim"], "token", not_="bytes/4")
    if silver:
        olgu("silver", "baglam.sqlite", "byte", silver["byte"], "byte"); olgu("silver", "kayit.metin", "byte", silver["kayit_metin_byte"], "byte", not_="bronz-metin kopyası")
        for t, n in silver["tablolar"].items(): olgu("silver", t, "satir", n, "adet")
        olgu("gold", "sqlite view", "adet", silver["gorunum_sayisi"], "adet")
    for ad, v in gold.items(): olgu("gold", ad, "byte", v["byte"], "byte"); olgu("gold", ad, "satir", v["satir"], "adet")
    if silver and bronz["byte"]: olgu("oran", "silver/bronz", "byte_orani", round(silver["byte"] / bronz["byte"], 3), "x", not_="yerel ölçüm; k=3 koşumda eşik önerisi")
    gb = sum(v["byte"] for v in gold.values())
    if bronz["byte"]: olgu("oran", "gold/bronz", "byte_orani", round(gb / bronz["byte"], 3), "x")
    for t in testler: olgu("silver", t["test"], "veri_testi_ihlal", t["ihlal"], "adet", t["sonuc"], t["tur"])
    for (nesne, metrik, deger, birim, not_) in ebilgi: olgu("silver", nesne, metrik, deger, birim, "-", not_)
    for p in pf: olgu("silver", p["tablo"], "sozlesme_preflight", len(p["kirici"]), "kırıcı", p["sonuc"], "; ".join(p["kirici"] + p["additive_ek"])[:200])
    for f in fr: olgu(f["katman"], f["nesne"], "freshness_gun", None if f["yas_gun"] is None else round(f["yas_gun"], 2), "gün", f["sonuc"], f.get("not", ""))
    if not a.kuru:
        with open(os.path.join(repo, "veri", "katman-olcum.jsonl"), "a", encoding="utf-8") as fh:
            for o in olgular: fh.write(json.dumps(o, ensure_ascii=False) + "\n")
    if not a.sessiz:
        print(f"katman-ölçüm {kosum_id} · bronz {bronz['dosya']} dosya / {bronz['byte']/1048576:.1f} MB (≈{bronz['token_kestirim']/1e6:.2f}M token)"
              + (f" · silver {silver['byte']/1048576:.1f} MB (kayit.metin {silver['kayit_metin_byte']/1048576:.1f} MB; {sum(silver['tablolar'].values())} satır/{len(silver['tablolar'])} tablo; {silver['gorunum_sayisi']} view)" if silver else " · silver YOK")
              + f" · gold {len(gold)} csv / {gb/1048576:.2f} MB" + (f" · oran silver/bronz {silver['byte']/bronz['byte']:.2f}x" if silver and bronz['byte'] else ""))
        for t in testler: print(f"  [{t['sonuc']:5}] test {t['tur']:16} {t['test']} → ihlal {t['ihlal']}")
        for p in pf: print(f"  [{p['sonuc']:5}] sözleşme {p['tablo']}" + (f" → {p['kirici']}" if p['kirici'] else "") + (f" · ek: {p['additive_ek']}" if p['additive_ek'] else ""))
        for f in fr: print(f"  [{f['sonuc']:9}] freshness {f['katman']:6} {f['nesne']} yaş {f['yas_gun'] if f['yas_gun'] is None else round(f['yas_gun'],1)} gün {f.get('not','')}")
        print(f"  → {len(olgular)} olgu {'(kuru)' if a.kuru else 'veri/katman-olcum.jsonl'}")
    code = 0
    if any(t["sonuc"] == "ERROR" for t in testler): code = 3
    if any(p["sonuc"] == "KIRICI" for p in pf): code = 4
    if any(f["sonuc"] == "ERROR" for f in fr): code = 5
    sys.exit(code)


if __name__ == "__main__":
    main()
