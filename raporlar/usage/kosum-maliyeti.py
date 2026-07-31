#!/usr/bin/env python3
"""kosum-maliyeti.py — CC oturum transkriptinden koşum maliyeti cikarir.

Kaynak: ~/.claude/projects/<proje>/<session_id>.jsonl (CC'nin kendi yazdigi kayit)
Komut koşturmaz, /usage'a bagimli degildir, salt-okurdur.

Kullanim:
  python kosum-maliyeti.py <session_id|jsonl-yolu>   -> tek oturum
  python kosum-maliyeti.py --all                     -> tum oturumlar (ozet)
  python kosum-maliyeti.py --line <session_id>       -> defter satiri (tek satir)
"""
import json, sys, glob, os, collections

PROJ = os.path.expanduser("~/.claude/projects/C--JARVIS")

# $ / 1M token. Kaynak: claude-api skill fiyat tablosu (2026-07-31).
# cache write 5m = 1.25x girdi, 1h = 2.0x girdi, cache read = 0.1x girdi.
PRICE = {
    "claude-opus-5":    (5.0,  25.0),
    "claude-opus-4-8":  (5.0,  25.0),
    "claude-fable-5":   (10.0, 50.0),
    # Sonnet 5 = 3/15. Belgede "tanitim 2/10" yaziyor AMA motorun kendi
    # costUSD'si liste fiyatini uyguluyor: 2026-07-31 canli kalibrasyon,
    # in=2 cc=10343(1h) cr=29147 out=4 -> motor $0.0708681, 3/15+2.0x ile
    # BIREBIR ayni (7 hane). Tanitim fiyati varsayimi YANLISLANDI. [D]
    "claude-sonnet-5":  (3.0,  15.0),
    "claude-haiku-4-5": (1.0,  5.0),
    "claude-haiku-4-5-20251001": (1.0, 5.0),   # tarihli varyant; kayitlarda gecti
    "claude-opus-4-7":  (5.0,  25.0),
    "claude-opus-4-6":  (5.0,  25.0),
    "claude-sonnet-4-6":(3.0,  15.0),
}

WEB_SEARCH_USD = 0.01   # $10 / 1000 arama

def files_for(path):
    """Ana transkript + ONUN alt-ajan transkriptleri.
    KRITIK: alt-ajanlar <oturum-id>/subagents/agent-*.jsonl altinda yasiyor ve
    ana .jsonl'de HIC gorunmuyor (isSidechain hep False). Sadece kok dizini
    taramak fan-out'lu kosumlarda maliyetin buyuk kismini kacirir."""
    base = path[:-6] if path.endswith(".jsonl") else path
    return [path] + sorted(glob.glob(os.path.join(base, "subagents", "*.jsonl")))

def collect(path):
    agg = collections.defaultdict(lambda: dict(inp=0, c5=0, c1h=0, cr=0, out=0,
                                               calls=0, ws=0, sub=0))
    meta = dict(first=None, last=None, effort=None, cwd=None, branch=None,
                ver=None, sid=None, nsub=0)
    fl = files_for(path)
    meta["nsub"] = len(fl) - 1
    for fp in fl:
        _collect_one(fp, agg, meta, is_sub=(fp != path))
    return agg, meta

def _collect_one(path, agg, meta, is_sub):
    for line in open(path, encoding="utf-8", errors="replace"):
        if '"usage"' not in line:
            continue
        try:
            d = json.loads(line)
        except Exception:
            continue
        m = d.get("message")
        if not isinstance(m, dict) or "usage" not in m:
            continue
        u, model = m["usage"], m.get("model") or "?"
        if model == "<synthetic>":
            continue
        a = agg[model]
        a["inp"]   += u.get("input_tokens", 0)
        a["cr"]    += u.get("cache_read_input_tokens", 0)
        a["out"]   += u.get("output_tokens", 0)
        cc = u.get("cache_creation") or {}
        c5  = cc.get("ephemeral_5m_input_tokens", 0)
        c1h = cc.get("ephemeral_1h_input_tokens", 0)
        if not (c5 or c1h):            # cache_creation yoksa toplami 5m say
            c5 = u.get("cache_creation_input_tokens", 0)
        a["c5"]  += c5
        a["c1h"] += c1h
        a["calls"] += 1
        if is_sub:
            a["sub"] += 1
        st = u.get("server_tool_use") or {}
        a["ws"] += st.get("web_search_requests", 0)
        ts = d.get("timestamp")
        if ts:
            meta["first"] = min(meta["first"] or ts, ts)
            meta["last"]  = max(meta["last"] or ts, ts)
        for k, f in (("effort","effort"), ("cwd","cwd"), ("branch","gitBranch"),
                     ("ver","version"), ("sid","sessionId")):
            if d.get(f):
                meta[k] = d[f]
    return agg, meta

def cost(model, a):
    if model not in PRICE:
        return None                       # [ARANAMADI] — fiyat bilinmiyor, uydurma yok
    pin, pout = PRICE[model]
    return ((a["inp"]*pin + a["c5"]*pin*1.25 + a["c1h"]*pin*2.0
             + a["cr"]*pin*0.1 + a["out"]*pout) / 1_000_000
            + a["ws"]*WEB_SEARCH_USD)

def dur_min(meta):
    if not (meta["first"] and meta["last"]):
        return None
    from datetime import datetime
    f = lambda s: datetime.fromisoformat(s.replace("Z", "+00:00"))
    return (f(meta["last"]) - f(meta["first"])).total_seconds() / 60

def report(path):
    agg, meta = collect(path)
    if not agg:
        print(f"{os.path.basename(path)}: usage kaydi YOK"); return 0.0
    tot = 0.0; unpriced = []
    print(f"\n=== {os.path.basename(path)[:8]}  cwd={meta['cwd']}  dal={meta['branch']}"
          f"  efor={meta['effort']}  cc={meta['ver']} ===")
    d = dur_min(meta)
    if d is not None:
        print(f"sure: {d:.1f} dk ({meta['first']} -> {meta['last']})")
    for model, a in sorted(agg.items()):
        c = cost(model, a)
        line = (f"  {model:<18} cagri={a['calls']:<4}(alt {a['sub']:<4}) ws={a['ws']:<3} giris={a['inp']:>9,} "
                f"cache-yaz5m={a['c5']:>10,} 1h={a['c1h']:>10,} "
                f"cache-oku={a['cr']:>11,} cikis={a['out']:>8,}")
        if c is None:
            unpriced.append(model); print(line + "   maliyet=[ARANAMADI: fiyat yok]")
        else:
            tot += c; print(line + f"   ${c:.4f}")
    print(f"  TOPLAM: ${tot:.4f}" + (f"  (+fiyatsiz: {','.join(unpriced)})" if unpriced else ""))
    return tot

def line(path):
    """cc/defter.md 'Token/Sure' kolonuna yapistirilabilir tek satir."""
    agg, meta = collect(path)
    tot = sum(c for c in (cost(m, a) for m, a in agg.items()) if c is not None)
    tin  = sum(a["inp"]+a["c5"]+a["c1h"]+a["cr"] for a in agg.values())
    tout = sum(a["out"] for a in agg.values())
    d = dur_min(meta)
    models = "+".join(sorted(agg))
    print(f"${tot:.2f} · {d:.0f} dk · giris {tin/1000:.0f}K / cikis {tout/1000:.1f}K "
          f"· {models} · efor {meta['effort']} · kaynak: transkript "
          f"(sid {(meta['sid'] or '?')[:8]}) [D]")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__); sys.exit(1)
    if args[0] == "--all":
        grand = 0.0
        for p in sorted(glob.glob(os.path.join(PROJ, "*.jsonl"))):
            grand += report(p)
        print(f"\n########  TUM OTURUMLAR TOPLAMI: ${grand:.2f}  ########")
    elif args[0] == "--line":
        t = args[1]
        line(t if t.endswith(".jsonl") else os.path.join(PROJ, t + ".jsonl"))
    else:
        t = args[0]
        report(t if t.endswith(".jsonl") else os.path.join(PROJ, t + ".jsonl"))
