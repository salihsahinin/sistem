#!/usr/bin/env python3
"""prompt-tablo.py — Salih'in prompt'larını BRONZ → SİLVER → GOLD hattından geçirir (STDLIB ONLY; veri-mühendisliği katmanı v1).

BRONZ (kaynak-konform, ham + provenans): oturum transkriptleri (`~/.claude/projects/<proje>/*.jsonl` = koşum kütüğü, repo dışı) taranır;
  Salih'in GERÇEK prompt'ları (user-role metin; araç-sonucu / komut-çıktısı / task-notification / skill enjeksiyonu / özet-devam HARİÇ) olduğu gibi
  `veri/bronz/prompt-olay.jsonl`'a APPEND edilir (tekilleştirme anahtarı = kaynak uuid; ham metin DEĞİŞTİRİLMEZ; provenans: kaynak dosya + uuid + ts).
SİLVER (1:1 grain, tipli, tekil, agrege-olmayan, türetilmiş): `veri/baglam.sqlite` tablosu `prompt` (1 satır = 1 prompt): tip dönüşümü (ts→UTC/TR),
  kategorize (tur — heuristik, deneysel m.29), sıra, sonraki-asistan modeli + tetiklenen skill (aynı oturumdaki bir sonraki asistan turundan).
GOLD (iş-konform, tek-tanım): SQL görünümü `v_son_50_prompt` → `veri/gorunum/v_son_50_prompt.csv` + insan-yüzü `raporlar/<tarih>-son-50-prompt.md`.
Sözleşme: `veri/sozlesme/prompt.json` (şekil; additive-only). Testler: unique(prompt_id) · not_null(metin) · accepted_values(tur).
Kullanım: python3 tools/prompt-tablo.py [--proje-dizin <yol>] [--repo <yol>] [--n 50] [--kuru] [--sessiz]
Sınır: md.49 — yalnız BU projenin (jarvis) transkriptleri; staj dizini taranmaz. Deneysel m.29 (2026-08-16, seans-7).
"""
import argparse, csv, glob, json, os, re, sqlite3, subprocess, sys
from datetime import datetime, timezone, timedelta

TR = timezone(timedelta(hours=3))
DISLA = ("<", "Base directory for this skill", "This session is being continued", "[Request interrupted", "[Usage limit", "Continue from where you left off", "Caveat:")  # sistem-enjekte user-mesajları Salih prompt'u DEĞİLDİR
TUR_ENUM = ["seans-acilis", "seans-kapanis", "durdur", "onay/devam", "emir", "soru", "geri-bildirim", "diger"]


def sh(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True).stdout.strip()


def metin_cek(msg):
    c = (msg or {}).get("content")
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        if any(isinstance(x, dict) and x.get("type") == "tool_result" for x in c):
            return None
        parts = [x.get("text", "") for x in c if isinstance(x, dict) and x.get("type") == "text"]
        return "\n".join(parts) if parts else None
    return None


def gercek_prompt(t):
    s = t.strip()
    return bool(s) and not any(s.startswith(p) if p != "Base directory for this skill" else p in s[:80] for p in DISLA)


def tur_tahmin(s):
    l = s.lower()
    if l.startswith("seans başı") or "seans başı" in l[:40]: return "seans-acilis"
    if "seans bitimi" in l[:40] or l.startswith(("kapat", "bitiriyorum")): return "seans-kapanis"
    if re.search(r"\b(dur|durdur|şimdilik dur|burda çalışma|iptal)\b", l) and len(l) < 120: return "durdur"
    if len(l) <= 40 and re.search(r"\b(devam|evet|tamam|onay|push at|olur|peki|hadi|başla)\b", l): return "onay/devam"
    if l.startswith(("yeni görev", "görev", "proje", "yeni proje")) or re.search(r"\b(araştır|atlasları koş|yaz|çıkar|oluştur|derle|entegre et|kur|hazırla|güncelle|sil|ekle|render et|gönder|aç|göster|kaldır|çevir|devral|resume et|geç|taşı|düzelt|kapat)\b", l): return "emir"
    if "?" in l or re.search(r"\b(mı|mi|mu|mü)(yız|yiz|yuz|yüz|sın|sin|sınız|siniz|dır|dir|dur|dür|ydı|ydi|yım|yim|yum|yüm)?\b|\b(nedir|neden|nasıl|hangi|kaç|ne)\b", l): return "soru"
    if re.search(r"\b(yanlış|hata|beğenmedim|olmadı|doğru değil|şöyle olmalı|kural)\b", l): return "geri-bildirim"
    return "diger"


def bronz_topla(proje_dizin):
    olaylar = []
    for f in sorted(glob.glob(os.path.join(proje_dizin, "*.jsonl"))):
        oturum = os.path.basename(f).replace(".jsonl", "")
        rows = []
        for l in open(f, encoding="utf-8", errors="replace"):
            try: rows.append(json.loads(l))
            except json.JSONDecodeError: continue
        # sonraki asistan turu (model + skill) için sıralı tarama
        for i, d in enumerate(rows):
            if d.get("type") != "user" or d.get("isSidechain"): continue
            t = metin_cek(d.get("message"))
            if t is None or not gercek_prompt(t): continue
            model, skills = None, []
            for e in rows[i + 1:]:
                if e.get("type") == "user":
                    tt = metin_cek(e.get("message"))
                    if tt is not None and gercek_prompt(tt): break
                if e.get("type") == "assistant":
                    m = e.get("message") or {}; model = model or m.get("model")
                    for x in m.get("content") or []:
                        if isinstance(x, dict) and x.get("type") == "tool_use" and x.get("name") == "Skill":
                            skills.append((x.get("input") or {}).get("skill", "?"))
            olaylar.append({"uuid": d.get("uuid"), "ts": d.get("timestamp"), "oturum": oturum, "kaynak_dosya": f, "metin": t,
                            "sonraki_model": model, "sonraki_skill": skills})
    # aynı uuid birden çok transkriptte (çatal/devam oturumu kopyası) görülebilir → İLK görülen kalır (bronz tekil anahtar = uuid)
    gorulen, tekil = set(), []
    for o in olaylar:
        if o["uuid"] in gorulen: continue
        gorulen.add(o["uuid"]); tekil.append(o)
    return tekil


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--proje-dizin", default=os.path.expanduser("~/.claude/projects/-Users-HasanSalihSahin-jarvis"))
    ap.add_argument("--n", type=int, default=50); ap.add_argument("--kuru", action="store_true"); ap.add_argument("--sessiz", action="store_true")
    ap.add_argument("--tarih", default=None, help="rapor dosya adı tarihi (YYYY-MM-DD); varsayılan bugün TR")
    a = ap.parse_args(); repo = os.path.abspath(a.repo)
    head = sh(["git", "rev-parse", "--short", "HEAD"], repo)
    tarih = a.tarih or datetime.now(TR).strftime("%Y-%m-%d")

    # --- BRONZ ---
    olaylar = bronz_topla(a.proje_dizin)
    bdir = os.path.join(repo, "veri", "bronz"); byol = os.path.join(bdir, "prompt-olay.jsonl")
    mevcut = set()
    if os.path.exists(byol):
        for l in open(byol, encoding="utf-8"):
            if l.startswith("{"):
                try: mevcut.add(json.loads(l)["uuid"])
                except Exception: pass
    yeni = [o for o in olaylar if o["uuid"] not in mevcut]
    if not a.kuru:
        os.makedirs(bdir, exist_ok=True)
        if not os.path.exists(byol):
            with open(byol, "w", encoding="utf-8") as fh:
                fh.write("# veri/bronz/prompt-olay.jsonl — BRONZ: Salih prompt olay kütüğü (ham metin DEĞİŞTİRİLMEZ; append-only; tekil anahtar uuid; provenans kaynak_dosya+ts). Üretici tools/prompt-tablo.py. md.49: yalnız jarvis transkriptleri.\n")
        with open(byol, "a", encoding="utf-8") as fh:
            for o in yeni:
                fh.write(json.dumps({**o, "kaynak_dosya": os.path.basename(o["kaynak_dosya"]), "yuklendi_head": head}, ensure_ascii=False) + "\n")

    # --- SİLVER ---
    hepsi = []
    if os.path.exists(byol):
        for l in open(byol, encoding="utf-8"):
            if l.startswith("{"): hepsi.append(json.loads(l))
    if a.kuru: hepsi = hepsi + [{**o, "kaynak_dosya": os.path.basename(o["kaynak_dosya"])} for o in yeni]
    # oturum içi sıra + tipler
    _g, _t = set(), []
    for o in hepsi:
        if o["uuid"] in _g: continue
        _g.add(o["uuid"]); _t.append(o)
    hepsi = _t
    hepsi.sort(key=lambda o: (o["ts"] or ""))
    sira = {}
    satirlar = []
    for o in hepsi:
        sira[o["oturum"]] = sira.get(o["oturum"], 0) + 1
        try:
            tu = datetime.fromisoformat(o["ts"].replace("Z", "+00:00")); ttr = tu.astimezone(TR)
        except Exception:
            tu = ttr = None
        m = o["metin"]
        satirlar.append({"prompt_id": o["uuid"], "ts_utc": o["ts"], "ts_tr": ttr.isoformat() if ttr else None, "tarih_tr": ttr.strftime("%Y-%m-%d") if ttr else None,
                         "oturum_id": o["oturum"], "oturum_kisa": o["oturum"][:8], "sira": sira[o["oturum"]], "metin": m,
                         "metin_kisa": re.sub(r"\s+", " ", m.strip())[:140], "uzunluk_kar": len(m), "kelime": len(m.split()),
                         "tur": tur_tahmin(m), "sonraki_model": o.get("sonraki_model"), "sonraki_skill": ",".join(o.get("sonraki_skill") or []) or None,
                         "kaynak_dosya": o["kaynak_dosya"], "yuklendi_head": o.get("yuklendi_head") or head})
    db = os.path.join(repo, "veri", "baglam.sqlite")
    testler = []
    if not a.kuru:
        con = sqlite3.connect(db)
        con.executescript("""
        CREATE TABLE IF NOT EXISTS prompt (
          prompt_id TEXT PRIMARY KEY, ts_utc TEXT, ts_tr TEXT, tarih_tr TEXT, oturum_id TEXT, oturum_kisa TEXT, sira INTEGER,
          metin TEXT, metin_kisa TEXT, uzunluk_kar INTEGER, kelime INTEGER, tur TEXT, sonraki_model TEXT, sonraki_skill TEXT,
          kaynak_dosya TEXT, yuklendi_head TEXT
        );
        DELETE FROM prompt;
        CREATE VIEW IF NOT EXISTS v_son_50_prompt AS
          SELECT ROW_NUMBER() OVER (ORDER BY ts_utc DESC) AS n, tarih_tr, substr(ts_tr,12,5) AS saat_tr, oturum_kisa, sira, tur,
                 sonraki_skill, sonraki_model, uzunluk_kar, metin_kisa, prompt_id
          FROM prompt ORDER BY ts_utc DESC LIMIT 50;
        """)
        con.executemany("INSERT INTO prompt VALUES (:prompt_id,:ts_utc,:ts_tr,:tarih_tr,:oturum_id,:oturum_kisa,:sira,:metin,:metin_kisa,:uzunluk_kar,:kelime,:tur,:sonraki_model,:sonraki_skill,:kaynak_dosya,:yuklendi_head)", satirlar)
        con.commit()
        # sözleşme (şekil) — ilk kez yoksa yaz
        sdir = os.path.join(repo, "veri", "sozlesme"); os.makedirs(sdir, exist_ok=True); syol = os.path.join(sdir, "prompt.json")
        if not os.path.exists(syol):
            cols = [{"ad": r[1], "tip": r[2] or "ANY", "not_null": bool(r[3]), "pk": bool(r[5])} for r in con.execute("PRAGMA table_info(prompt)")]
            json.dump({"tablo": "prompt", "surum": "1.0.0-deneysel-m29", "katman": "silver", "grain": "1 satır = 1 Salih prompt'u (jarvis transkriptleri)", "kolonlar": cols,
                       "kural": "additive-only; kırıcı = silme/tip/kısıt/yeniden-ad"}, open(syol, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        # testler
        for ad, sql, sev in [("prompt.prompt_id unique", "SELECT COUNT(*) FROM (SELECT prompt_id FROM prompt GROUP BY prompt_id HAVING COUNT(*)>1)", "error"),
                             ("prompt.metin not_null", "SELECT COUNT(*) FROM prompt WHERE metin IS NULL OR metin=''", "error"),
                             ("prompt.tur accepted_values", f"SELECT COUNT(*) FROM prompt WHERE tur NOT IN ({','.join('?'*len(TUR_ENUM))})", "error")]:
            n = con.execute(sql, TUR_ENUM if "accepted" in ad else ()).fetchone()[0]
            testler.append((ad, n, "PASS" if n == 0 else sev.upper()))
        # --- GOLD ---
        gold = con.execute("SELECT * FROM v_son_50_prompt").fetchall(); cols = [d[0] for d in con.execute("SELECT * FROM v_son_50_prompt").description]
        con.close()
        gdir = os.path.join(repo, "veri", "gorunum"); os.makedirs(gdir, exist_ok=True)
        with open(os.path.join(gdir, "v_son_50_prompt.csv"), "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh); w.writerow(cols); w.writerows(gold)
        # insan-yüzü tablo
        L = [f"# Son {min(a.n,50)} prompt — Salih (gold görünüm `v_son_50_prompt`; {tarih}, HEAD `{head}`)\n",
             f"*Hat: BRONZ `veri/bronz/prompt-olay.jsonl` ({len(hepsi)} olay; kaynak: {len(set(o['oturum'] for o in hepsi))} jarvis oturum transkripti) → SİLVER `prompt` tablosu (`veri/baglam.sqlite`; sözleşme `veri/sozlesme/prompt.json`; testler {', '.join(f'{t[0]} {t[2]}' for t in testler)}) → GOLD `v_son_50_prompt` (`veri/gorunum/v_son_50_prompt.csv`). Üretici `tools/prompt-tablo.py`. `tur` heuristik sınıflandırma (deneysel m.29). Tam metin silver tablosunda: `sqlite3 veri/baglam.sqlite \"select metin from prompt where prompt_id='…'\"`.*\n",
             "| # | tarih | saat | oturum | sıra | tür | tetiklenen skill | model | kar | prompt (kısa) |", "|---|---|---|---|---|---|---|---|---|---|"]
        for r in gold[:a.n]:
            n_, tarih_, saat, ot, sira_, tur, sk, mdl, uz, kisa, pid = r
            L.append(f"| {n_} | {tarih_} | {saat} | `{ot}` | {sira_} | {tur} | {sk or '—'} | {(mdl or '—').replace('claude-','')} | {uz} | {kisa.replace('|','¦')} |")
        # tür dağılımı (gold içi küçük agregat)
        from collections import Counter
        cnt = Counter(r[5] for r in gold[:a.n]); L.append("\n**Tür dağılımı (son %d):** " % min(a.n,50) + " · ".join(f"{k} {v}" for k, v in cnt.most_common()))
        skc = Counter(s for r in gold[:a.n] for s in (r[6] or "").split(",") if s); L.append("**Tetiklenen skill'ler:** " + (" · ".join(f"{k} {v}" for k, v in skc.most_common()) or "—"))
        ryol = os.path.join(repo, "raporlar", f"{tarih}-son-50-prompt.md")
        open(ryol, "w", encoding="utf-8").write("\n".join(L) + "\n")
    if not a.sessiz:
        print(f"bronz: {len(olaylar)} gerçek prompt bulundu ({len(yeni)} yeni, {len(mevcut)} mevcut) · silver: {len(satirlar)} satır · gold: son {a.n}" + (" (kuru)" if a.kuru else f" → veri/gorunum/v_son_50_prompt.csv + raporlar/{tarih}-son-50-prompt.md"))
        for t in testler: print(f"  [{t[2]}] {t[0]} ihlal {t[1]}")


if __name__ == "__main__":
    main()
