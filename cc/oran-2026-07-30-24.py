#!/usr/bin/env python3
"""oran.py — her CC oturumu icin API-suresi / duvar-suresi orani + maliyet.

API suresi transkriptte SAKLANMIYOR (durationMs yalniz hook kayitlarinda).
Yeniden kurulum: her 'assistant' kaydinin zaman damgasi ile onu ONCELEYEN
kaydin damgasi arasindaki fark = o isteğin API suresi (dusunme+uretim).
Alt-ajanlarin API sureleri TOPLANIR (paralel fan-out'ta CC de boyle sayar).
Kalibrasyon: bilinen iki /usage noktasiyla (07-15 loop, 07-17 sozluk) karsilastirilir.
"""
import json, sys, glob, os, collections
from datetime import datetime

PROJS = [os.path.expanduser("~/.claude/projects/"+d) for d in ("C--JARVIS","C--JARVIS-cc","C--JARVIS-raporlar")]
PRICE = {
    "claude-opus-5": (5.0, 25.0), "claude-opus-4-8": (5.0, 25.0),
    "claude-fable-5": (10.0, 50.0), "claude-sonnet-5": (3.0, 15.0),
    "claude-haiku-4-5": (1.0, 5.0), "claude-haiku-4-5-20251001": (1.0, 5.0),
    "claude-opus-4-7": (5.0, 25.0), "claude-opus-4-6": (5.0, 25.0),
    "claude-sonnet-4-6": (3.0, 15.0),
}
WS_USD = 0.01
CAP_S = 1800.0   # tek bir API isteği icin ust sinir (idle/resume kirlenmesine karsi)

def _undo(a, u):
    a["inp"] -= u.get("input_tokens", 0); a["cr"] -= u.get("cache_read_input_tokens", 0)
    a["out"] -= u.get("output_tokens", 0)
    cc = u.get("cache_creation") or {}
    c5 = cc.get("ephemeral_5m_input_tokens", 0); c1h = cc.get("ephemeral_1h_input_tokens", 0)
    if not (c5 or c1h): c5 = u.get("cache_creation_input_tokens", 0)
    a["c5"] -= c5; a["c1h"] -= c1h; a["n"] -= 1

def ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))

def scan(path):
    """tek dosya -> (api_s, wall_s, first, last, capped_n, tokens, cost, models, nreq)"""
    recs = []
    seen = {}             # (requestId, message.id) — ayni usage 2-3 kez yaziliyor
    agg = collections.defaultdict(lambda: dict(inp=0, c5=0, c1h=0, cr=0, out=0, ws=0, n=0))
    for line in open(path, encoding="utf-8", errors="replace"):
        try:
            d = json.loads(line)
        except Exception:
            continue
        t = d.get("timestamp")
        if t:
            recs.append((ts(t), d.get("type")))
        m = d.get("message")
        if isinstance(m, dict) and "usage" in m:
            model = m.get("model") or "?"
            if model == "<synthetic>":
                continue
            key = (d.get("requestId"), m.get("id"))
            u = m["usage"]
            prev = seen.get(key)
            if prev is not None:
                if u.get("output_tokens", 0) <= prev[1].get("output_tokens", 0):
                    continue
                _undo(agg[prev[0]], prev[1])      # onceki kismi kaydi geri al
            seen[key] = (model, u)
            a = agg[model]
            a["inp"] += u.get("input_tokens", 0)
            a["cr"] += u.get("cache_read_input_tokens", 0)
            a["out"] += u.get("output_tokens", 0)
            cc = u.get("cache_creation") or {}
            c5 = cc.get("ephemeral_5m_input_tokens", 0); c1h = cc.get("ephemeral_1h_input_tokens", 0)
            if not (c5 or c1h):
                c5 = u.get("cache_creation_input_tokens", 0)
            a["c5"] += c5; a["c1h"] += c1h; a["n"] += 1
            a["ws"] += (u.get("server_tool_use") or {}).get("web_search_requests", 0)
    if not recs:
        return None
    recs.sort(key=lambda r: r[0])
    api = 0.0; capped = 0
    for i in range(1, len(recs)):
        if recs[i][1] == "assistant":
            g = (recs[i][0] - recs[i-1][0]).total_seconds()
            if g > CAP_S:
                g = CAP_S; capped += 1
            if g > 0:
                api += g
    wall = (recs[-1][0] - recs[0][0]).total_seconds()
    cost = 0.0; unpriced = []
    for model, a in agg.items():
        if model not in PRICE:
            unpriced.append(model); continue
        pin, pout = PRICE[model]
        cost += (a["inp"]*pin + a["c5"]*pin*1.25 + a["c1h"]*pin*2.0
                 + a["cr"]*pin*0.1 + a["out"]*pout) / 1e6 + a["ws"]*WS_USD
    tin = sum(a["inp"]+a["c5"]+a["c1h"]+a["cr"] for a in agg.values())
    tout = sum(a["out"] for a in agg.values())
    nreq = sum(a["n"] for a in agg.values())
    return dict(api=api, wall=wall, first=recs[0][0], last=recs[-1][0], capped=capped,
                tin=tin, tout=tout, cost=cost, models=set(agg), nreq=nreq, unpriced=unpriced)

def session(path):
    base = path[:-6]
    subs = sorted(glob.glob(os.path.join(base, "subagents", "**", "*.jsonl"), recursive=True))
    main = scan(path)
    if not main:
        return None
    r = dict(main)
    r["nsub"] = len(subs); r["api_main"] = main["api"]; r["api_sub"] = 0.0
    r["wall_main"] = main["wall"]
    for s in subs:
        x = scan(s)
        if not x:
            continue
        r["api_sub"] += x["api"]
        r["tin"] += x["tin"]; r["tout"] += x["tout"]; r["cost"] += x["cost"]
        r["nreq"] += x["nreq"]; r["models"] |= x["models"]; r["capped"] += x["capped"]
        r["first"] = min(r["first"], x["first"]); r["last"] = max(r["last"], x["last"])
    r["api"] = r["api_main"] + r["api_sub"]
    r["wall"] = (r["last"] - r["first"]).total_seconds()
    r["sid"] = os.path.basename(path)[:8]
    r["ratio"] = r["api"] / r["wall"] if r["wall"] > 0 else None
    return r

if __name__ == "__main__":
    rows = []
    for PROJ in PROJS:
     for p in sorted(glob.glob(os.path.join(PROJ, "*.jsonl"))):
        r = session(p)
        if r:
            r["proj"]=os.path.basename(PROJ); rows.append(r)
    rows.sort(key=lambda r: r["first"])
    print(f"{'sid':<9}{'baslangic':<17}{'API dk':>8}{'duvar dk':>10}{'oran':>7}"
          f"{'  $':>9}{'giris K':>10}{'cikis K':>9}{'ist':>5}{'alt':>5}  modeller")
    for r in rows:
        print(f"{r['sid']:<9}{r['first'].strftime('%m-%d %H:%M'):<17}"
              f"{r['api']/60:>8.1f}{r['wall']/60:>10.1f}{(r['ratio'] or 0):>7.2f}"
              f"{r['cost']:>9.2f}{r['tin']/1000:>10.0f}{r['tout']/1000:>9.1f}"
              f"{r['nreq']:>5}{r['nsub']:>5}  {'+'.join(sorted(m.replace('claude-','') for m in r['models']))}")
    print(f"\nTOPLAM: ${sum(r['cost'] for r in rows):.2f} · {len(rows)} oturum")
