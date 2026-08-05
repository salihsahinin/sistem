#!/usr/bin/env python3
# olcum-dortlu.py — P6 enstrümantasyon (K-015 / L8)
# Kaynak: <repo>/.gnhf/runs/*/gnhf.log (birincil) + ~/.no-mistakes/state.sqlite (şema keşfi)
# Çıktı: koşum-başına dörtlü (token · duvar-saati · iterasyon · sonuç), markdown blok.
# --append: bloğu senaryo-defterine yazar (mükerrer runId#pid atlanır). m.39: eksik alan [?].
# Kullanım:
#   python C:\JARVIS\tools\olcum-dortlu.py                 # önizleme (stdout)
#   python C:\JARVIS\tools\olcum-dortlu.py --append        # deftere yaz
#   python C:\JARVIS\tools\olcum-dortlu.py --repo C:\dev\baska-repo

import argparse, json, re, sqlite3, sys
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

def any_ts(v):
    """ISO string | epoch s | epoch ms → datetime; olmazsa None."""
    if v is None:
        return None
    if isinstance(v, (int, float)):
        try:
            return datetime.fromtimestamp(v / 1000 if v > 1e12 else v, tz=timezone.utc)
        except (OSError, OverflowError, ValueError):
            return None
    try:
        return ts(str(v))
    except ValueError:
        return None

def nm_block():
    """no-mistakes state.sqlite → koşum-başına dörtlü.
    Kaynak (şema keşfi 2026-08-05): runs + agent_invocations (token, duration_ms)
    + step_results (adım) + step_rounds (tur). Eksik alan [?] (m.39)."""
    if not NM_DB.is_file():
        return f"- no-mistakes: `{NM_DB}` yok.\n", []
    lines, keys = [], []
    try:
        db = sqlite3.connect(f"file:{NM_DB.as_posix()}?mode=ro", uri=True)
        runs = db.execute(
            "select id, branch, status, pr_url, pr_state, created_at, updated_at"
            " from runs order by created_at").fetchall()
        for rid, branch, status, pr_url, pr_state, c_at, u_at in runs:
            keys.append(f"nm#{rid}")
            inv = db.execute(
                "select count(*), sum(input_tokens), sum(output_tokens),"
                " sum(cache_read_tokens), sum(fresh_input_tokens), sum(duration_ms)"
                " from agent_invocations where run_id=?", (rid,)).fetchone()
            n_inv, t_in, t_out, t_cr, t_fresh, inv_ms = inv
            n_step = db.execute("select count(*), sum(duration_ms) from step_results"
                                " where run_id=?", (rid,)).fetchone()
            n_round = db.execute(
                "select count(*) from step_rounds where step_result_id in"
                " (select id from step_results where run_id=?)", (rid,)).fetchone()[0]
            t0, t1 = any_ts(c_at), any_ts(u_at)
            wall = f"{(t1 - t0).total_seconds():.0f} sn" if t0 and t1 else "[?]"
            ajan = f"{inv_ms/1000:.0f}" if isinstance(inv_ms, (int, float)) else "[?]"
            tok = (f"in {fmt_int(t_in)} (cache-read {fmt_int(t_cr)},"
                   f" taze {fmt_int(t_fresh)}) / out {fmt_int(t_out)}") if n_inv else "[?] (invocation yok)"
            sonuc = f"{status or '[?]'}" + (f" · PR {pr_state or '[?]'}: {pr_url}" if pr_url else "")
            lines.append(
                f"| `nm#{rid}` | no-mistakes/{branch or '[?]'}"
                f" | {n_step[0]} adım / {n_round} tur / {n_inv} çağrı"
                f" | {wall} (ajan {ajan} sn) | {tok} | {sonuc} |")
        db.close()
    except sqlite3.Error as err:
        return (f"- no-mistakes: sqlite okunamadı ({err}) — şema değişmiş olabilir;"
                " betik güncellenmeli, eksik alan [?] (m.39).\n", [])
    if not lines:
        return "- no-mistakes: runs tablosu boş.\n", []
    hdr = ("| koşum | araç/dal | iterasyon | duvar-saati | token | sonuç |\n"
           "|---|---|---|---|---|---|\n")
    return hdr + "\n".join(lines) + "\n", keys

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
    g_block, g_keys = gnhf_block(Path(a.repo))
    n_block, n_keys = nm_block()
    keys = g_keys + n_keys
    block = (f"\n### Ölçüm dörtlüsü — {today} (betik: tools/olcum-dortlu.py, P6)\n\n"
             f"{g_block}\n{n_block}")
    print(block)

    if a.append:
        defter = Path(a.defter)
        text = defter.read_text(encoding="utf-8", errors="replace") if defter.is_file() else ""
        new_keys = [k for k in keys if k not in text]
        if not new_keys:
            print(">> Deftere yazılmadı: tüm koşumlar zaten kayıtlı (mükerrer koruması).")
            return
        # satır-bazlı filtre: defterde kayıtlı koşum satırları tekrar yazılmaz
        kept = []
        for ln in block.splitlines():
            m = re.match(r"^\| `([^`]+)`", ln)
            if m and m.group(1) in text:
                continue
            kept.append(ln)
        with defter.open("a", encoding="utf-8") as fh:
            fh.write("\n".join(kept) + "\n")
        print(f">> Deftere yazıldı: {defter} ({len(new_keys)} yeni koşum; mükerrerler atlandı).")

if __name__ == "__main__":
    main()
