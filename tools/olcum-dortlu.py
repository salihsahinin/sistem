#!/usr/bin/env python3
# olcum-dortlu.py — P6 enstrümantasyon (K-015 / L8)
# Kaynak: <repo>/.gnhf/runs/*/gnhf.log (birincil) + ~/.no-mistakes/state.sqlite (şema keşfi)
# Çıktı: koşum-başına dörtlü (token · duvar-saati · iterasyon · sonuç), markdown blok.
# --append: bloğu senaryo-defterine yazar (mükerrer runId#pid atlanır). m.39: eksik alan [?].
# Kullanım:
#   python C:\JARVIS\tools\olcum-dortlu.py                 # önizleme (stdout)
#   python C:\JARVIS\tools\olcum-dortlu.py --append        # deftere yaz
#   python C:\JARVIS\tools\olcum-dortlu.py --repo C:\dev\baska-repo

import argparse, json, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

DEFTER = Path(r"C:\JARVIS\kuyruk\senaryo-defteri.md")
NM_DB = Path.home() / ".no-mistakes" / "state.sqlite"

def ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))

def parse_gnhf_log(log_path):
    """gnhf.log tek dosyada birden çok segment içerir (resume append eder).
    Segment = run:start ... run:complete. Segment listesi döner."""
    segs, cur = [], None
    for line in log_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        ev = e.get("event")
        if ev == "run:start":
            cur = {"run_id": e.get("runId"), "pid": e.get("pid"),
                   "agent": e.get("agent"), "start": e.get("timestamp"),
                   "max_iter": e.get("maxIterations"), "max_tok": e.get("maxTokens"),
                   "iters": [], "abort_reason": None, "end": None, "final": {}}
        elif cur is None:
            continue
        elif ev == "agent:run:end":
            cur["iters"].append({
                "n": e.get("iteration"), "ms": e.get("elapsedMs"),
                "in": e.get("inputTokens"), "out": e.get("outputTokens"),
                "cache_r": e.get("cacheReadTokens"), "cache_c": e.get("cacheCreationTokens"),
                "ok": e.get("success")})
        elif ev in ("agent:run:aborted",):
            cur["iters"].append({"n": e.get("iteration"), "ms": e.get("elapsedMs"),
                                 "in": None, "out": None, "cache_r": None, "cache_c": None,
                                 "ok": False, "reason": e.get("reason")})
        elif ev == "orchestrator:abort":
            cur["abort_reason"] = e.get("reason")
        elif ev == "run:complete":
            cur["end"] = e.get("timestamp")
            cur["final"] = {k: e.get(k) for k in
                            ("status", "iterations", "successCount", "failCount",
                             "totalInputTokens", "totalOutputTokens", "commitCount")}
            segs.append(cur)
            cur = None
    if cur is not None:  # yarım segment (koşum sürüyor / çökmüş)
        cur["final"] = {"status": "[?] segment kapanmamış"}
        segs.append(cur)
    return segs

def fmt_int(v):
    return f"{v:,}".replace(",", ".") if isinstance(v, int) else "[?]"

def gnhf_block(repo):
    runs_dir = repo / ".gnhf" / "runs"
    if not runs_dir.is_dir():
        return f"- gnhf: `{runs_dir}` yok — koşum kaydı bulunamadı.\n", []
    lines, keys = [], []
    for run_dir in sorted(runs_dir.iterdir()):
        log = run_dir / "gnhf.log"
        if not log.is_file():
            continue
        for s in parse_gnhf_log(log):
            key = f"{s['run_id']}#{s['pid']}"
            keys.append(key)
            f = s["final"]
            wall = "[?]"
            if s.get("start") and s.get("end"):
                wall = f"{(ts(s['end']) - ts(s['start'])).total_seconds():.0f} sn"
            agent_ms = sum(i["ms"] for i in s["iters"] if isinstance(i.get("ms"), int))
            cache_r = sum(i["cache_r"] for i in s["iters"] if isinstance(i.get("cache_r"), int))
            reason = s["abort_reason"] or "-"
            sonuc = (f"{f.get('status', '[?]')} · başarı {f.get('successCount', '[?]')}"
                     f"/{f.get('iterations', '[?]')} · commit {f.get('commitCount', '[?]')}"
                     + (f" · sebep: {reason}" if reason != "-" else ""))
            lines.append(
                f"| `{key}` | gnhf/{s['agent']} | {f.get('iterations', '[?]')}"
                f" | {wall} (ajan {agent_ms/1000:.0f} sn)"
                f" | in {fmt_int(f.get('totalInputTokens'))} (cache-read {fmt_int(cache_r)})"
                f" / out {fmt_int(f.get('totalOutputTokens'))}"
                f" | {sonuc} |")
    if not lines:
        return "- gnhf: runs klasörü var ama ayrıştırılabilir segment yok.\n", []
    hdr = ("| koşum#pid | araç | iterasyon | duvar-saati | token | sonuç |\n"
           "|---|---|---|---|---|---|\n")
    return hdr + "\n".join(lines) + "\n", keys

def nm_block():
    if not NM_DB.is_file():
        return f"- no-mistakes: `{NM_DB}` yok.\n"
    out = []
    try:
        db = sqlite3.connect(f"file:{NM_DB.as_posix()}?mode=ro", uri=True)
        rows = db.execute("select name, type from sqlite_master"
                          " where type in ('table','view') order by name").fetchall()
        out.append("no-mistakes şema keşfi (state.sqlite, read-only):")
        for name, typ in rows:
            try:
                n = db.execute(f'select count(*) from "{name}"').fetchone()[0]
            except sqlite3.Error:
                n = "[?]"
            cols = [r[1] for r in db.execute(f'pragma table_info("{name}")').fetchall()]
            out.append(f"- `{name}` ({typ}, {n} satır): {', '.join(cols) or '[?]'}")
        db.close()
        out.append("Dörtlü çıkarımı: şema yukarıda — token alanı yoksa PR-gövdesi-parse'ına"
                   " düşülür (teslim §5), eksik alan [?] (m.39).")
    except sqlite3.Error as err:
        out.append(f"- no-mistakes: sqlite açılamadı ({err}) — daemon'u durdurup"
                   " tekrar dene ya da dosyayı kopyalayıp oku.")
    return "\n".join(out) + "\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=r"C:\dev\wf-deneme")
    ap.add_argument("--defter", default=str(DEFTER))
    ap.add_argument("--append", action="store_true")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    today = datetime.now().strftime("%Y-%m-%d")
    g_block, keys = gnhf_block(Path(a.repo))
    block = (f"\n### Ölçüm dörtlüsü — {today} (betik: tools/olcum-dortlu.py, P6)\n\n"
             f"{g_block}\n{nm_block()}")
    print(block)

    if a.append:
        defter = Path(a.defter)
        text = defter.read_text(encoding="utf-8", errors="replace") if defter.is_file() else ""
        new_keys = [k for k in keys if k not in text]
        if not new_keys:
            print(">> Deftere yazılmadı: tüm koşumlar zaten kayıtlı (mükerrer koruması).")
            return
        with defter.open("a", encoding="utf-8") as fh:
            fh.write(block)
        print(f">> Deftere yazıldı: {defter} ({len(new_keys)} yeni koşum).")

if __name__ == "__main__":
    main()
