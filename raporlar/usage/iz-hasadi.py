#!/usr/bin/env python3
"""iz-hasadi.py -- CC oturum transkriptlerinden damitilmis metrik hasadi (görev: cc/gorev-2026-08-01-3.md)

Kaynak: ~/.claude/projects/<proje>/<sid>.jsonl (ana transkript, salt-okur).
Alt-ajan dosyalari (subagents/**) bu hasatta AYRI oturum SAYILMAZ; yalniz
`alt_ajan_var_mi` bayragini besler (ana-oturum tur/ctx/hata sayimlari yalniz
ana transkript uzerindendir -- 08-01-2 §1.1'deki tanimla ayni kapsam).

Kullanim:
  python iz-hasadi.py                    -> tum JARVIS-iliskili projeler, jsonl'e yazar
  python iz-hasadi.py --line <sid>       -> tek oturum, stdout'a tek JSON satiri (doğrulama icin)
"""
import json, sys, os, glob, statistics

BASE = os.path.expanduser("~/.claude/projects")
OUT = r"C:\JARVIS\raporlar\usage\iz-hasadi-2026-08.jsonl"

PROJECTS = [
    "C--JARVIS",
    "C--JARVIS-cc",
    "C--JARVIS-raporlar",
    "C--Users-sasah-AppData-Local-Temp-claude-C--JARVIS-27ccc0d8-e96c-4464-b26e-ddf7c3b4e753-scratchpad-hook-deney",
    "C--Users-sasah-AppData-Local-Temp-claude-C--JARVIS-9a4206e9-12df-40b1-b86e-f6c41be6467b-scratchpad",
]

# kosum-maliyeti.py PRICE tablosuyla birebir (30-24 senkron; degistirmeden kopyalandi)
PRICE = {
    "claude-opus-5":    (5.0,  25.0),
    "claude-opus-4-8":  (5.0,  25.0),
    "claude-fable-5":   (10.0, 50.0),
    "claude-sonnet-5":  (3.0,  15.0),
    "claude-haiku-4-5": (1.0,  5.0),
    "claude-haiku-4-5-20251001": (1.0, 5.0),
    "claude-opus-4-7":  (5.0,  25.0),
    "claude-opus-4-6":  (5.0,  25.0),
    "claude-sonnet-4-6":(3.0,  15.0),
}


def ctx_of(usage):
    inp = usage.get("input_tokens", 0)
    cr = usage.get("cache_read_input_tokens", 0)
    cc = usage.get("cache_creation") or {}
    c5 = cc.get("ephemeral_5m_input_tokens", 0)
    c1h = cc.get("ephemeral_1h_input_tokens", 0)
    if not (c5 or c1h):
        c5 = usage.get("cache_creation_input_tokens", 0)
    return inp + c5 + c1h + cr


def has_subagents(sid_dir):
    if not os.path.isdir(sid_dir):
        return False
    sub = os.path.join(sid_dir, "subagents")
    if not os.path.isdir(sub):
        return False
    return len(glob.glob(os.path.join(sub, "**", "*.jsonl"), recursive=True)) > 0


def harvest_one(path, proje):
    sid = os.path.basename(path)[:-6]
    sid_dir = path[:-6]
    ts_ilk = ts_son = None
    entrypoint = None
    models = set()
    tur_sayisi = 0
    ctx_series = []
    is_error_sayisi = 0
    skills = set()
    agg = {}  # model -> dict for cost

    for line in open(path, encoding="utf-8", errors="replace"):
        line = line.strip()
        if not line:
            continue
        try:
            d = json.loads(line)
        except Exception:
            continue
        ts = d.get("timestamp")
        if ts:
            ts_ilk = ts if ts_ilk is None or ts < ts_ilk else ts_ilk
            ts_son = ts if ts_son is None or ts > ts_son else ts_son
        if entrypoint is None and d.get("entrypoint"):
            entrypoint = d["entrypoint"]

        t = d.get("type")
        if t == "assistant":
            m = d.get("message")
            if isinstance(m, dict):
                model = m.get("model")
                if model and model != "<synthetic>":
                    models.add(model)
                    tur_sayisi += 1
                    u = m.get("usage")
                    if isinstance(u, dict):
                        ctx_series.append(ctx_of(u))
                        a = agg.setdefault(model, dict(inp=0, c5=0, c1h=0, cr=0, out=0))
                        a["inp"] += u.get("input_tokens", 0)
                        a["cr"] += u.get("cache_read_input_tokens", 0)
                        a["out"] += u.get("output_tokens", 0)
                        cc = u.get("cache_creation") or {}
                        c5 = cc.get("ephemeral_5m_input_tokens", 0)
                        c1h = cc.get("ephemeral_1h_input_tokens", 0)
                        if not (c5 or c1h):
                            c5 = u.get("cache_creation_input_tokens", 0)
                        a["c5"] += c5
                        a["c1h"] += c1h
                content = m.get("content") if isinstance(m, dict) else None
                if isinstance(content, list):
                    for c in content:
                        if isinstance(c, dict) and c.get("type") == "tool_use" and c.get("name") == "Skill":
                            sk = (c.get("input") or {}).get("skill")
                            if sk:
                                skills.add(sk)
        elif t == "user":
            m = d.get("message")
            content = m.get("content") if isinstance(m, dict) else None
            if isinstance(content, list):
                for c in content:
                    if isinstance(c, dict) and c.get("type") == "tool_result" and c.get("is_error") is True:
                        is_error_sayisi += 1

    ctx_max = max(ctx_series) if ctx_series else None
    ctx_med = statistics.median(ctx_series) if ctx_series else None

    maliyet = 0.0
    unpriced = False
    for model, a in agg.items():
        if model not in PRICE:
            unpriced = True
            continue
        pin, pout = PRICE[model]
        maliyet += (a["inp"]*pin + a["c5"]*pin*1.25 + a["c1h"]*pin*2.0
                    + a["cr"]*pin*0.1 + a["out"]*pout) / 1_000_000
    maliyet_alan = None if not agg else round(maliyet, 4)

    return {
        "sid": sid,
        "proje": proje,
        "ts_ilk": ts_ilk,
        "ts_son": ts_son,
        "entrypoint": entrypoint,
        "modeller": sorted(models) if models else None,
        "tur_sayisi": tur_sayisi if tur_sayisi else None,
        "ctx_serisi_ozeti": {"max": ctx_max, "medyan": ctx_med} if ctx_series else {"max": None, "medyan": None},
        "is_error_sayisi": is_error_sayisi,
        "skill_cagrilari": sorted(skills),
        "alt_ajan_var_mi": has_subagents(sid_dir),
        "maliyet_usd_betik_v0_serhli": maliyet_alan,
        "maliyet_serh": ("kosum-maliyeti.py ile ayni motor; 30-24 SS6.1'in belgeledigi uc kusur "
                          "(usage-dedup yok, ic-ice alt-ajan/workflow kacagi, web-search sayilmaz) "
                          "duzeltilmedi -- rakam bilinen yonde SISIK, ciplak hukum tasimaz."
                          if maliyet_alan is not None else None),
        "maliyet_fiyatsiz_model_var_mi": unpriced,
    }


def all_session_files():
    out = []
    for proje in PROJECTS:
        proj_dir = os.path.join(BASE, proje)
        if not os.path.isdir(proj_dir):
            continue
        for fp in sorted(glob.glob(os.path.join(proj_dir, "*.jsonl"))):
            out.append((fp, proje))
    return out


def run_all():
    n = 0
    with open(OUT, "w", encoding="utf-8") as f:
        for fp, proje in all_session_files():
            row = harvest_one(fp, proje)
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
            n += 1
    print(f"{n} oturum -> {OUT}")


def find_path(sid):
    for proje in PROJECTS:
        cand = os.path.join(BASE, proje, sid + ".jsonl")
        if os.path.exists(cand):
            return cand, proje
    raise SystemExit(f"sid bulunamadi: {sid}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        run_all()
    elif args[0] == "--line":
        sid = args[1]
        fp, proje = find_path(sid)
        print(json.dumps(harvest_one(fp, proje), ensure_ascii=False, indent=2))
    else:
        print(__doc__)
