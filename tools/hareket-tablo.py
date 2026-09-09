#!/usr/bin/env python3
"""hareket-tablo.py — Carvis'in TÜM HAREKETLERİNİ (araç çağrılarını) transkriptten repoya indirir: BRONZ → SİLVER → GOLD + insan-yüzü günlük (STDLIB ONLY).

Neden: Okunabilirlik ilkesi (Salih Katman-1, 2026-08-17; CLAUDE.md §2): "çalışma şeklini, kaynak kodlarını, yazılarını, TÜM hareketlerini
anlayıp okuyup analiz edebilmeliyim … hepsi açık kaynak ve bilgisayarımda kolayca herkese ulaşılabilir olmalı." Oturum transkriptleri
(`~/.claude/projects/<proje>/*.jsonl`) repo DIŞINDA ve JSON'dur — okunmaz. Bu script her araç çağrısını (yazdı / düzenledi / okudu / koştu /
aradı / ajan gönderdi / skill çağırdı / workflow başlattı / web'e baktı) düz satıra çevirir ve repoya yazar.

BRONZ (kaynak-konform, ham + provenans; append-only): `veri/bronz/hareket-olay.jsonl` — 1 satır = 1 araç çağrısı {hareket_id (tool_use id, tekil),
  ts, oturum, arac, girdi_ozet (ham argümanın kısaltılmışı; kod/metin gövdesi KOPYALANMAZ — yalnız hedef), sonuc (tamam/hata/yok), model, kaynak_dosya}.
SİLVER (1:1 grain, tipli, tekil): `veri/baglam.sqlite` tablosu `hareket` — TR zaman, oturum-içi sıra, Türkçe fiil, hedef dosya (repo-göreli), repo_ici.
  Sözleşme `veri/sozlesme/hareket.json` (additive-only). Testler: unique(hareket_id) · not_null(arac) · accepted_values(fiil).
GOLD (iş-konform, tek tanım): `v_hareket_gunluk` (gün × oturum × fiil sayımı) · `v_son_hareketler` (son 300) · `v_okuma_orani` (İB-29: aralık↔bütün okuma; KB-53 (a)) → `veri/gorunum/*.csv`
  + İNSAN-YÜZÜ: `raporlar/hareket/hareket-gunlugu-YYYY-MM-DD.md` (o günün her seansı: saat · fiil · hedef · sonuç; ad arama anahtarıyla başlar).
Kullanım: python3 tools/hareket-tablo.py [--tarih YYYY-MM-DD] [--tum] [--kuru] [--sessiz] [--proje-dizin <yol>] [--repo <yol>]
  --tum: bronzdaki HER gün için günlük dosyası üretir (geriye dönük). Varsayılan: yalnız bugün (TR).
Sınır: md.49 — yalnız jarvis transkriptleri; alt-ajan koşumları ambar-tablo.py'de (amb_olgu_kosum), burada ana oturumun kendi çağrıları.
Deneysik m.29 (2026-08-17, seans-8). Katman hattı: tools/katman-hatti.py adım 5.
"""
import argparse, csv, glob, json, os, re, sqlite3, subprocess
from collections import Counter, defaultdict
from datetime import datetime, timezone, timedelta

TR = timezone(timedelta(hours=3))
HOME = os.path.expanduser("~")
FIIL = {"Write": "yazdı", "Edit": "düzenledi", "MultiEdit": "düzenledi", "NotebookEdit": "düzenledi", "Read": "okudu", "Bash": "koştu",
        "Grep": "aradı", "Glob": "aradı", "Agent": "ajan gönderdi", "Task": "ajan gönderdi", "Skill": "skill çağırdı", "Workflow": "workflow başlattı",
        "WebFetch": "web'e baktı", "WebSearch": "web'e baktı", "TodoWrite": "görev listesi", "TaskCreate": "görev listesi", "TaskUpdate": "görev listesi",
        "TaskList": "görev listesi", "TaskGet": "görev listesi", "TaskOutput": "görev listesi", "TaskStop": "görev listesi", "AskUserQuestion": "sordu",
        "SendMessage": "mesaj yolladı", "ToolSearch": "araç aradı", "EnterPlanMode": "plan modu", "ExitPlanMode": "plan modu", "Monitor": "izledi"}
FIIL_ENUM = sorted(set(FIIL.values()) | {"MCP aracı", "araç"})


def sh(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True).stdout.strip()


def kisa_yol(p, repo):
    if not p: return None, None, False
    ap = os.path.abspath(os.path.expanduser(p)) if not p.startswith("/") else p
    if ap.startswith(repo + os.sep):
        return ap[len(repo) + 1:], ap[len(repo) + 1:], True
    return ap.replace(HOME, "~"), None, False


def girdi_ozet(arac, inp, repo):
    """Argümanı hedefe indirger; kod/metin gövdesi kopyalanmaz (bronz = hedef, içerik değil)."""
    inp = inp or {}
    dosya = None; repo_ici = False
    if arac in ("Write", "Edit", "MultiEdit", "NotebookEdit", "Read"):
        h, dosya, repo_ici = kisa_yol(inp.get("file_path") or inp.get("notebook_path"), repo)
        if arac == "Read":  # İB-29 (KB-53 (a)): aralık (offset/limit) ↔ bütün okuma sayacı — bronz özete ek, içerik yok
            if inp.get("offset") is not None or inp.get("limit") is not None:
                h = "%s [aralık %s+%s]" % (h, inp.get("offset") if inp.get("offset") is not None else 0, inp.get("limit") if inp.get("limit") is not None else "∞")
            else:
                h = "%s [bütün]" % h
    elif arac == "Bash":
        c = re.sub(r"\s+", " ", (inp.get("command") or "")).strip()
        h = (inp.get("description") or "").strip() + " ⟨" + c[:150] + ("…" if len(c) > 150 else "") + "⟩"
        m = re.search(r"(?:>>?|tee|cat >|python3 - <<|git mv|git add|git commit)", c)
        repo_ici = "~/jarvis" in c or c.startswith("cd ~/jarvis") or "jarvis" in c
    elif arac in ("Grep", "Glob"):
        h = f"{inp.get('pattern','')}  ({kisa_yol(inp.get('path'), repo)[0] or '.'})"
    elif arac in ("Agent", "Task"):
        h = f"[{inp.get('subagent_type') or inp.get('agentType') or 'agent'}] {inp.get('description') or (inp.get('prompt') or '')[:100]}"
    elif arac == "Skill":
        h = f"{inp.get('skill')} {inp.get('args') or ''}".strip()
    elif arac == "Workflow":
        sc = inp.get("script") or ""; m = re.search(r"name:\s*['\"]([^'\"]+)", sc)
        h = m.group(1) if m else (inp.get("name") or inp.get("scriptPath") or "script")
    elif arac in ("WebFetch",):
        h = inp.get("url", "")
    elif arac in ("WebSearch",):
        h = inp.get("query", "")
    elif arac == "AskUserQuestion":
        qs = inp.get("questions") or []; h = "; ".join((q.get("question") or "")[:80] for q in qs if isinstance(q, dict))
    elif arac == "SendMessage":
        h = f"→ {inp.get('to','')}"
    elif arac.startswith("mcp__"):
        h = arac.split("__")[-1] + " " + json.dumps({k: (str(v)[:60]) for k, v in list(inp.items())[:3]}, ensure_ascii=False)
    else:
        h = json.dumps({k: (str(v)[:60]) for k, v in list(inp.items())[:3]}, ensure_ascii=False)
    return (h or "")[:300], dosya, repo_ici


OKUMA_ARALIK_RX = re.compile(r"(sed\s+-n\s+['\"]?\d+(,\d+)?p|\bhead\s+(-n\s*)?-?\d+|\btail\s+(-n\s*)?[-+]?\d+|\bawk\s+['\"]NR\s*[<>=]|\bhead\s+-c\s*\d+)")
OKUMA_BUTUN_RX = re.compile(r"(^|[;&|]\s*)cat\s+[^|<>;&]+\.(md|py|json|jsonl|txt|sh|sql|d2|csv)\b")


def okuma_tipi(arac, inp):
    """İB-29 (KB-53 (a) Karar 62): okuma hareketini 'aralik' | 'butun' | None olarak sınıflar — deterministik, yalnız argümandan.
    Read: offset∨limit → aralik, yoksa butun · Bash: sed -n 'a,bp' / head -n / tail -n / awk NR / head -c → aralik; 'cat <dosya>' → butun;
    başka Bash (grep/python/git…) → None (okuma sayılmaz). Ölçüm girdisi: ince-tutkal (KB-53 b) kararı düşük aralık-oranında masaya döner."""
    inp = inp or {}
    if arac == "Read":
        return "aralik" if (inp.get("offset") is not None or inp.get("limit") is not None) else "butun"
    if arac == "Bash":
        c = inp.get("command") or ""
        if OKUMA_ARALIK_RX.search(c):
            return "aralik"
        if OKUMA_BUTUN_RX.search(c):
            return "butun"
    return None


def bronz_topla(proje_dizin, repo):
    olaylar = []
    for f in sorted(glob.glob(os.path.join(proje_dizin, "*.jsonl"))):
        oturum = os.path.basename(f)[:-6]
        rows = []
        for l in open(f, encoding="utf-8", errors="replace"):
            try: rows.append(json.loads(l))
            except Exception: continue
        sonuc = {}
        for r in rows:  # tool_result → is_error haritası
            if r.get("type") == "user":
                for x in (r.get("message") or {}).get("content") or []:
                    if isinstance(x, dict) and x.get("type") == "tool_result":
                        sonuc[x.get("tool_use_id")] = "hata" if x.get("is_error") else "tamam"
        for r in rows:
            if r.get("type") != "assistant": continue
            msg = r.get("message") or {}
            for x in msg.get("content") or []:
                if not (isinstance(x, dict) and x.get("type") == "tool_use"): continue
                arac = x.get("name") or "?"; hid = x.get("id") or f"{oturum}:{r.get('uuid')}:{arac}"
                ozet, dosya, repo_ici = girdi_ozet(arac, x.get("input"), repo)
                olaylar.append({"hareket_id": hid, "ts": r.get("timestamp"), "oturum": oturum, "arac": arac, "girdi_ozet": ozet, "okuma_tipi": okuma_tipi(arac, x.get("input")),
                                "dosya": dosya, "repo_ici": repo_ici, "sonuc": sonuc.get(hid, "yok"), "model": msg.get("model"),
                                "kaynak_dosya": os.path.basename(f)})
    return olaylar


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--proje-dizin", default=os.path.expanduser("~/.claude/projects/-Users-HasanSalihSahin-jarvis"))
    ap.add_argument("--tarih", default=None); ap.add_argument("--tum", action="store_true"); ap.add_argument("--kuru", action="store_true"); ap.add_argument("--sessiz", action="store_true")
    a = ap.parse_args(); repo = os.path.abspath(a.repo)
    head = sh(["git", "rev-parse", "--short", "HEAD"], repo)
    bugun = a.tarih or datetime.now(TR).strftime("%Y-%m-%d")

    # --- BRONZ ---
    olaylar = bronz_topla(a.proje_dizin, repo)
    bdir = os.path.join(repo, "veri", "bronz"); byol = os.path.join(bdir, "hareket-olay.jsonl")
    mevcut = set()
    if os.path.exists(byol):
        for l in open(byol, encoding="utf-8"):
            if l.startswith("{"):
                try: mevcut.add(json.loads(l)["hareket_id"])
                except Exception: pass
    yeni = [o for o in olaylar if o["hareket_id"] not in mevcut]
    if not a.kuru:
        os.makedirs(bdir, exist_ok=True)
        if not os.path.exists(byol):
            open(byol, "w", encoding="utf-8").write("# veri/bronz/hareket-olay.jsonl — BRONZ: Carvis'in araç çağrısı olay kütüğü (1 satır = 1 çağrı; hedef var, içerik yok; append-only; tekil anahtar hareket_id). Üretici tools/hareket-tablo.py. Okunabilirlik ilkesi 08-17. md.49: yalnız jarvis transkriptleri.\n")
        with open(byol, "a", encoding="utf-8") as fh:
            for o in yeni: fh.write(json.dumps({**o, "yuklendi_head": head}, ensure_ascii=False) + "\n")

    # --- SİLVER ---
    hepsi, g = [], set()
    kaynak = (open(byol, encoding="utf-8") if os.path.exists(byol) else [])
    for l in kaynak:
        if l.startswith("{"):
            o = json.loads(l)
            if o["hareket_id"] not in g: g.add(o["hareket_id"]); hepsi.append(o)
    if a.kuru:
        for o in yeni:
            if o["hareket_id"] not in g: g.add(o["hareket_id"]); hepsi.append(o)
    hepsi.sort(key=lambda o: (o.get("ts") or "", o["oturum"]))
    sira, satirlar = Counter(), []
    for o in hepsi:
        sira[o["oturum"]] += 1
        try: ttr = datetime.fromisoformat(o["ts"].replace("Z", "+00:00")).astimezone(TR)
        except Exception: ttr = None
        arac = o["arac"]; fiil = FIIL.get(arac) or ("MCP aracı" if arac.startswith("mcp__") else "araç")
        satirlar.append({"hareket_id": o["hareket_id"], "ts_utc": o.get("ts"), "ts_tr": ttr.isoformat() if ttr else None,
                         "tarih_tr": ttr.strftime("%Y-%m-%d") if ttr else None, "saat_tr": ttr.strftime("%H:%M:%S") if ttr else None,
                         "oturum_id": o["oturum"], "oturum_kisa": o["oturum"][:8], "sira": sira[o["oturum"]], "arac": arac, "fiil": fiil,
                         "hedef": o.get("girdi_ozet"), "dosya": o.get("dosya"), "repo_ici": 1 if o.get("repo_ici") else 0, "sonuc": o.get("sonuc"),
                         "model": (o.get("model") or "").replace("claude-", "") or None, "kaynak_dosya": o.get("kaynak_dosya"), "yuklendi_head": o.get("yuklendi_head") or head,
                         "okuma_tipi": o.get("okuma_tipi")})
    testler, gunler = [], sorted({s["tarih_tr"] for s in satirlar if s["tarih_tr"]})
    if not a.kuru:
        db = os.path.join(repo, "veri", "baglam.sqlite"); con = sqlite3.connect(db)
        con.executescript("""
        CREATE TABLE IF NOT EXISTS hareket (
          hareket_id TEXT PRIMARY KEY, ts_utc TEXT, ts_tr TEXT, tarih_tr TEXT, saat_tr TEXT, oturum_id TEXT, oturum_kisa TEXT, sira INTEGER,
          arac TEXT NOT NULL, fiil TEXT, hedef TEXT, dosya TEXT, repo_ici INTEGER, sonuc TEXT, model TEXT, kaynak_dosya TEXT, yuklendi_head TEXT,
          okuma_tipi TEXT
        );
        DELETE FROM hareket;
        CREATE VIEW IF NOT EXISTS v_okuma_orani AS
          SELECT tarih_tr, oturum_kisa,
                 SUM(CASE WHEN okuma_tipi='aralik' THEN 1 ELSE 0 END) AS aralik,
                 SUM(CASE WHEN okuma_tipi='butun' THEN 1 ELSE 0 END) AS butun,
                 ROUND(1.0*SUM(CASE WHEN okuma_tipi='aralik' THEN 1 ELSE 0 END) / NULLIF(SUM(CASE WHEN okuma_tipi IN ('aralik','butun') THEN 1 ELSE 0 END),0), 3) AS aralik_orani,
                 SUM(CASE WHEN okuma_tipi='aralik' AND arac='Read' THEN 1 ELSE 0 END) AS read_aralik,
                 SUM(CASE WHEN okuma_tipi='butun' AND arac='Read' THEN 1 ELSE 0 END) AS read_butun
          FROM hareket WHERE okuma_tipi IS NOT NULL GROUP BY tarih_tr, oturum_kisa ORDER BY tarih_tr DESC, oturum_kisa;
        CREATE VIEW IF NOT EXISTS v_hareket_gunluk AS
          SELECT tarih_tr, oturum_kisa, fiil, COUNT(*) AS n, MIN(saat_tr) AS ilk, MAX(saat_tr) AS son,
                 SUM(CASE WHEN sonuc='hata' THEN 1 ELSE 0 END) AS hata, COUNT(DISTINCT CASE WHEN fiil IN ('yazdı','düzenledi') THEN dosya END) AS yazilan_dosya
          FROM hareket GROUP BY tarih_tr, oturum_kisa, fiil ORDER BY tarih_tr DESC, oturum_kisa, n DESC;
        CREATE VIEW IF NOT EXISTS v_son_hareketler AS
          SELECT ROW_NUMBER() OVER (ORDER BY ts_utc DESC) AS n, tarih_tr, saat_tr, oturum_kisa, sira, fiil, arac, hedef, sonuc, model, hareket_id
          FROM hareket ORDER BY ts_utc DESC LIMIT 300;
        """)
        kol = {r[1] for r in con.execute("PRAGMA table_info(hareket)")}
        if "okuma_tipi" not in kol:
            con.execute("ALTER TABLE hareket ADD COLUMN okuma_tipi TEXT")  # additive (eski DB'de)
        con.executemany("INSERT INTO hareket VALUES (:hareket_id,:ts_utc,:ts_tr,:tarih_tr,:saat_tr,:oturum_id,:oturum_kisa,:sira,:arac,:fiil,:hedef,:dosya,:repo_ici,:sonuc,:model,:kaynak_dosya,:yuklendi_head,:okuma_tipi)", satirlar)
        con.commit()
        sdir = os.path.join(repo, "veri", "sozlesme"); os.makedirs(sdir, exist_ok=True); syol = os.path.join(sdir, "hareket.json")
        if not os.path.exists(syol):
            cols = [{"ad": r[1], "tip": r[2] or "ANY", "not_null": bool(r[3]), "pk": bool(r[5])} for r in con.execute("PRAGMA table_info(hareket)")]
            json.dump({"tablo": "hareket", "surum": "1.0.0-deneysel-m29", "katman": "silver", "grain": "1 satır = 1 Carvis araç çağrısı (jarvis ana-oturum transkriptleri)",
                       "kolonlar": cols, "kural": "additive-only; kırıcı = silme/tip/kısıt/yeniden-ad"}, open(syol, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        for ad, sql, prm in [("hareket.hareket_id unique", "SELECT COUNT(*) FROM (SELECT hareket_id FROM hareket GROUP BY hareket_id HAVING COUNT(*)>1)", ()),
                             ("hareket.arac not_null", "SELECT COUNT(*) FROM hareket WHERE arac IS NULL OR arac=''", ()),
                             ("hareket.fiil accepted_values", f"SELECT COUNT(*) FROM hareket WHERE fiil NOT IN ({','.join('?'*len(FIIL_ENUM))})", FIIL_ENUM)]:
            n = con.execute(sql, prm).fetchone()[0]; testler.append((ad, n, "PASS" if n == 0 else "ERROR"))
        # --- GOLD ---
        gdir = os.path.join(repo, "veri", "gorunum"); os.makedirs(gdir, exist_ok=True)
        for v in ("v_hareket_gunluk", "v_son_hareketler", "v_okuma_orani"):
            cur = con.execute(f"SELECT * FROM {v}"); cols = [d[0] for d in cur.description]
            with open(os.path.join(gdir, f"{v}.csv"), "w", newline="", encoding="utf-8") as fh:
                w = csv.writer(fh); w.writerow(cols); w.writerows(cur.fetchall())
        con.close()
        # --- İNSAN-YÜZÜ günlük ---
        hedef_gunler = gunler if a.tum else [bugun]
        rdir = os.path.join(repo, "raporlar", "hareket"); os.makedirs(rdir, exist_ok=True)
        for gun in hedef_gunler:
            gs = [s for s in satirlar if s["tarih_tr"] == gun]
            if not gs and not a.tum: gs = []
            ot = defaultdict(list)
            for s in gs: ot[s["oturum_id"]].append(s)
            L = [f"# Hareket günlüğü — {gun} (Carvis'in araç çağrıları; kaynak transkript → `tools/hareket-tablo.py`; HEAD `{head}`)\n",
                 f"*Okunabilirlik ilkesi (Salih 08-17): Carvis'in o gün YAPTIĞI her şey — dosya yazma/düzenleme, komut, okuma, arama, ajan/skill/workflow çağrısı — burada düz satır. Hedef gösterilir, içerik gösterilmez (içerik dosyanın kendisinde ya da git log'da). Makine-yüzü: silver `hareket` (`veri/baglam.sqlite`), gold `veri/gorunum/v_hareket_gunluk.csv` · `v_son_hareketler.csv`; bronz `veri/bronz/hareket-olay.jsonl`. Toplam bugün: {len(gs)} çağrı, {len(ot)} oturum.*\n"]
            for oid, ss in sorted(ot.items(), key=lambda kv: kv[1][0]["ts_utc"] or ""):
                c = Counter(s["fiil"] for s in ss); yz = sorted({s["dosya"] for s in ss if s["dosya"] and s["fiil"] in ("yazdı", "düzenledi")})
                hata = sum(1 for s in ss if s["sonuc"] == "hata"); mdl = Counter(s["model"] for s in ss if s["model"]).most_common(1)
                L.append(f"## Oturum `{oid[:8]}` — {ss[0]['saat_tr']}→{ss[-1]['saat_tr']} · {len(ss)} çağrı · model {mdl[0][0] if mdl else '?'} · hata {hata}")
                L.append("**Özet:** " + " · ".join(f"{k} {v}" for k, v in c.most_common()) + (f"\n**Yazılan/düzenlenen dosyalar ({len(yz)}):** " + " · ".join(f"`{d}`" for d in yz) if yz else ""))
                L.append("\n| # | saat | fiil | hedef | sonuç |\n|---|---|---|---|---|")
                for s in ss:
                    L.append(f"| {s['sira']} | {s['saat_tr']} | {s['fiil']} | {(s['hedef'] or '').replace('|','¦')} | {s['sonuc']} |")
                L.append("")
            if not gs: L.append("_Bu gün için kayıt yok._")
            open(os.path.join(rdir, f"hareket-gunlugu-{gun}.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    if not a.sessiz:
        print(f"bronz: {len(olaylar)} çağrı tarandı ({len(yeni)} yeni, {len(mevcut)} mevcut) · silver: {len(satirlar)} satır · gün: {len(gunler)}" + (" (kuru)" if a.kuru else f" → gold CSV + raporlar/hareket/hareket-gunlugu-{'*' if a.tum else bugun}.md"))
        for t in testler: print(f"  [{t[2]}] {t[0]} ihlal {t[1]}")


if __name__ == "__main__":
    main()
