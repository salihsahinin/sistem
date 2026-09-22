#!/usr/bin/env python3
"""acilis-kapilari.py — seans-acilis §1.4 / §1.5 / §2.3b deterministik açılış kapıları (İB-91, Karar 96 M2 A4, 2026-09-15).
Kural kaynağı: wiki/paralel-oturum-protokolu.md §1 (canlı-oturum kapısı, Karar 57 resume eki) · seans-acilis §1.5 (koşum-önü
manifest kapısı, KB-08) · Karar 62 İB-27 (silver tazelik). Script TESPİT eder, koşmaz (katman-hatti'yi çağırmaz, kanona yazmaz).

Kapılar:
  K1 canlı-oturum : son commit yaşı ≤15 dk ∧ kapsül 'Güncelleme' satırı o commit'ten eski → ŞÜPHE; ek sinyaller: ≤15 dk içinde
                    yazılmış oturum transkripti sayısı (~/.claude/projects/<proje>/*.jsonl), açık worktree'ler, son 24 saatte
                    main-dışı dallara giren commit'ler. Son 5 commit yaşıyla listelenir (resume eki: tanınmayan commit → devir notu).
  K2 manifest     : --is "<anahtar>" verilirse cc/pipeline/pipeline-*.md + git log -15 içinde arar → "zaten koşmuş/koşuyor" adayları;
                    verilmezse manifestlerde SAHADA/AÇIK durum satırları listelenir.
  K3 silver       : veri/baglam.sqlite uretim.git_head_sha ≠ HEAD → BAYAT (tarif: python3 tools/katman-hatti.py).
Kullanım: python3 tools/acilis-kapilari.py [--repo ~/sistem/jarvis] [--is "<anahtar>"] [--dk 15] [--json]
Çıkış: 0 tüm kapılar temiz · 1 en az bir kapı uyarı (ŞÜPHE ∨ koşmuş-aday ∨ BAYAT) · 2 repo/git okunamadı.
Çıktı ≤ ~1,5 KB (KB-50 bağlam bütçesi); rakamlar sayım, kestirim yok.
"""
import pathlib, argparse, datetime as dt, glob, json, os, pathlib, re, sqlite3, subprocess, sys


def sh(cmd, cwd):
    try:
        return subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, timeout=20).stdout.strip()
    except Exception:
        return ""


def yas_dk(ts_iso, simdi):
    try:
        t = dt.datetime.fromisoformat(ts_iso.strip())
        if t.tzinfo is None:
            t = t.replace(tzinfo=simdi.tzinfo)
        return int((simdi - t).total_seconds() // 60)
    except Exception:
        return None


def kapi_canli(repo, dk, simdi):
    r = {"kapi": "K1-canli-oturum"}
    log = sh('git log -5 --format="%h|%cI|%s"', repo)  # çift tırnak: Windows cmd.exe tek tırnağı soymaz (2026-09-22)
    if not log:
        r["durum"] = "HATA"; r["not"] = "git log okunamadı"; return r
    commits = []
    for l in log.splitlines():
        h, ci, s = l.strip("'").split("|", 2)
        # Karar 101 F4: monorepo — commit'in dokunduğu üst-dizin(ler) (jarvis · friday · kök) K1'de görünür; friday/ commit'i tanınır
        alan = sorted({(y.split("/", 1)[0] if "/" in y else "kök") for y in sh("git show --name-only --format= %s" % h, repo).splitlines() if y.strip()})
        commits.append({"sha": h, "yas_dk": yas_dk(ci, simdi), "konu": s[:70], "alan": "+".join(alan) or "?"})
    r["son5"] = commits
    son = commits[0]
    # kapsül güncelleme zamanı
    kap = ""
    try:
        t = (repo / "core" / "durum-kapsulu.md").read_text(encoding="utf-8")
        m = re.search(r"\*\*Güncelleme:\*\*\s*(\d{4}-\d{2}-\d{2})\s*~?(\d{1,2}):(\d{2})", t)
        if m:
            kap = f"{m.group(1)}T{int(m.group(2)):02d}:{m.group(3)}"
    except Exception:
        pass
    r["kapsul_guncelleme"] = kap or "?"
    kapsul_eski = False
    if kap:
        ci = sh("git log -1 --format=%cI", repo)
        try:
            kapsul_eski = dt.datetime.fromisoformat(kap) < dt.datetime.fromisoformat(ci).replace(tzinfo=None)
        except Exception:
            kapsul_eski = False
    r["kapsul_son_committen_eski"] = kapsul_eski
    # ek sinyaller
    kok = pathlib.Path.home() / ".claude" / "projects"
    slug = "-" + str(repo).strip("/").replace("/", "-")
    canli_tr = 0  # ana repo + worktree oturumları (proje dizini adı slug ile başlar)
    for f in (ff for d in kok.glob(slug + "*") for ff in d.glob("*.jsonl")) if kok.exists() else []:
        try:
            if (simdi.timestamp() - f.stat().st_mtime) <= dk * 60:
                canli_tr += 1
        except Exception:
            pass
    r["canli_transkript"] = canli_tr  # bu oturum dahil
    wt = [l for l in sh("git worktree list", repo).splitlines() if l.strip()]
    r["worktree"] = len(wt) - 1 if wt else 0
    # 09-17: yan oturum worktree'si main'in gerisindeyse eski kanon (Karar 97 öncesi caps) + eski hook yolları yüklenir →
    # model eski üslubu taklit eder, Stop hook sessiz düşer (guvenlik-2 vakası: 34/36 hook çağrısı "No such file"). Kanıt kapısı.
    r["worktree_geride"] = []
    for l in wt[1:]:
        yol = l.split()[0]
        geride = sh("git rev-list --count %s..main" % (l.split("[")[-1].rstrip("]") if "[" in l else "HEAD"), repo).strip() or "?"
        try:
            hook_eski = "CLAUDE_PROJECT_DIR" not in (pathlib.Path(yol) / ".claude" / "settings.json").read_text(encoding="utf-8")
        except Exception:
            hook_eski = None
        r["worktree_geride"].append((yol.rsplit("/", 1)[-1], geride, hook_eski))
    dallar = sh('git for-each-ref --format="%(refname:short)|%(committerdate:iso-strict)" refs/heads refs/remotes/origin', repo)
    taze_dal = []
    for l in dallar.splitlines():
        ad, ci = l.strip("'").split("|", 1)
        if ad in ("origin", "main") or ad.endswith("/main") or ad.endswith("HEAD"):
            continue
        y = yas_dk(ci, simdi)
        if y is not None and y <= 24 * 60:
            taze_dal.append(f"{ad}({y // 60}s)")
    r["taze_dal_24s"] = taze_dal[:6]
    suphe = (son["yas_dk"] is not None and son["yas_dk"] <= dk and kapsul_eski) or canli_tr >= 2
    r["durum"] = "ŞÜPHE" if suphe else "TEMİZ"
    r["not"] = ("son commit %s dk önce, kapsül kapanışı %s; canlı transkript %d (bu oturum dahil); worktree %d — başka oturum açık mı? TEK soru; git add <yol> (H4)"
                % (son["yas_dk"], "eski" if kapsul_eski else "güncel", canli_tr, r["worktree"])) if suphe else "son commit %s dk önce; canlı transkript %d" % (son["yas_dk"], canli_tr)
    for ad, geride, hook_eski in r["worktree_geride"]:
        if geride not in ("0", "?") or hook_eski:
            r["not"] += " · worktree %s main'in %s commit gerisinde%s → yan oturumu kapat, dalı merge et, main'den yeni worktree (Karar 95 EK)" % (
                ad, geride, " + hook yolları eski (CLAUDE_PROJECT_DIR yok)" if hook_eski else "")
    return r


def kapi_manifest(repo, anahtar):
    r = {"kapi": "K2-manifest"}
    mans = sorted(glob.glob(str(repo / "cc" / "pipeline" / "pipeline-*.md")))
    if anahtar:
        a = anahtar.lower()
        hits = [pathlib.Path(m).name for m in mans if a in pathlib.Path(m).read_text(encoding="utf-8", errors="ignore").lower()]
        logh = [l for l in sh('git log -15 --format="%h %s"', repo).splitlines() if a in l.lower()]
        r["anahtar"] = anahtar; r["manifest_eslesme"] = hits[:5]; r["gitlog15_eslesme"] = [l.strip("'")[:80] for l in logh[:5]]
        r["durum"] = "KOŞMUŞ-ADAY" if (hits or logh) else "TEMİZ"
        r["not"] = "manifest %d · git log -15 %d eşleşme → varsa devral, koşma (vaka-3: 518k mükerrer)" % (len(hits), len(logh))
    else:
        acik = []
        for m in mans:
            t = pathlib.Path(m).read_text(encoding="utf-8", errors="ignore")
            if re.search(r"(?i)\b(SAHADA|AÇIK|KOŞUYOR|YARIM)\b", t[:1500]):
                acik.append(pathlib.Path(m).name)
        r["manifest_sayisi"] = len(mans); r["acik_gorunen"] = acik[:6]; r["durum"] = "TEMİZ"
        r["not"] = "anahtar verilmedi; Workflow/atlas/pipeline açmadan --is \"<konu>\" ile koş"
    return r


def kapi_silver(repo):
    r = {"kapi": "K3-silver"}
    head = sh("git rev-parse HEAD", repo)
    db = repo / "veri" / "baglam.sqlite"
    if not db.exists():
        r["durum"] = "YOK"; r["not"] = "veri/baglam.sqlite yok (worktree ya da ilk kurulum) → öğrenme oturumu koşmaz; geliştirme oturumu python3 tools/katman-hatti.py"; return r
    try:
        c = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
        u = c.execute("SELECT git_head_sha, uretim_zamani FROM uretim ORDER BY uretim_zamani DESC LIMIT 1").fetchone()
    except Exception as e:
        r["durum"] = "HATA"; r["not"] = str(e)[:80]; return r
    taze = bool(u and head and u[0] == head)
    r["silver_sha"] = (u[0][:7] if u else "?"); r["head"] = head[:7]; r["uretim"] = (u[1][:16] if u else "?")
    r["durum"] = "TAZE" if taze else "BAYAT"
    r["not"] = "" if taze else "python3 tools/katman-hatti.py (~12 sn, idempotent; Karar 62 İB-27) — atlanırsa adresli erişim yanlış satır getirir"
    return r


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--repo", default=str(pathlib.Path(__file__).resolve().parent.parent))  # varsayılan = bu script'in jarvis kökü (Windows'ta ~/sistem yok, 2026-09-22)
    ap.add_argument("--is", dest="anahtar", default=""); ap.add_argument("--dk", type=int, default=15); ap.add_argument("--json", action="store_true")
    a = ap.parse_args(); repo = pathlib.Path(a.repo).expanduser().resolve()
    # Karar 101 (F3): jarvis/ artık monorepo alt-dizini; .git kökte → git rev-parse ile doğrula
    if subprocess.run(["git", "rev-parse", "--git-dir"], cwd=repo, capture_output=True).returncode != 0:
        print("repo okunamadı: %s" % repo); sys.exit(2)
    simdi = dt.datetime.now().astimezone()
    k = [kapi_canli(repo, a.dk, simdi), kapi_manifest(repo, a.anahtar), kapi_silver(repo)]
    uyari = any(x["durum"] in ("ŞÜPHE", "KOŞMUŞ-ADAY", "BAYAT") for x in k)
    if a.json:
        print(json.dumps({"zaman": simdi.isoformat(timespec="minutes"), "kapilar": k, "uyari": uyari}, ensure_ascii=False)); sys.exit(1 if uyari else 0)
    print("AÇILIŞ KAPILARI (İB-91) · %s · %s" % (simdi.strftime("%Y-%m-%d %H:%M"), repo))
    c = k[0]
    print("  [%s] K1 canlı-oturum — %s" % (c["durum"], c["not"]))
    for s in c["son5"]:
        print("        %s  %4s dk  [%s] %s" % (s["sha"], s["yas_dk"] if s["yas_dk"] is not None else "?", s.get("alan", "?"), s["konu"]))
    if c.get("taze_dal_24s"):
        print("        24 saatte main-dışı dal: " + " · ".join(c["taze_dal_24s"]))
    m = k[1]
    print("  [%s] K2 manifest — %s" % (m["durum"], m["not"]))
    for ad in ("manifest_eslesme", "gitlog15_eslesme", "acik_gorunen"):
        if m.get(ad):
            print("        %s: %s" % (ad, " · ".join(m[ad])))
    s = k[2]
    print("  [%s] K3 silver — silver %s / HEAD %s (%s) %s" % (s["durum"], s.get("silver_sha", "-"), s.get("head", "-"), s.get("uretim", "-"), s["not"]))
    sys.exit(1 if uyari else 0)


if __name__ == "__main__":
    main()
