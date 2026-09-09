#!/usr/bin/env python3
"""kod-envanter.py — Jarvis'te ÇALIŞAN KODUN dil envanteri + kurulu araç-zinciri + başlangıç-gecikmesi ölçümü (STDLIB ONLY, Python ≥3.9).

Neden var (dil-seçimi pipeline'ı, 2026-08-26 seans-16; emir cc/gorev/2026-08/gorev-2026-08-26-1.md · manifest cc/pipeline/pipeline-2026-08-26-dil-secimi-ekosistem.md):
"hangi durumda hangi dil" sorusu ÖLÇÜMSÜZ tartışılmaz (m.35, m.39). 07-30'daki dil raporu elle sayılmış 126 satıra dayanıyordu; 08-26'da
elle sayım 8.583 satır çıktı. Bu script sayımı DETERMİNİSTİK ve tekrar-üretilebilir yapar: aynı HEAD + aynı makine → aynı envanter (gecikme
ölçümü hariç; o makine-bağımlıdır ve öyle damgalanır). Karar 65 (determinizm önceliği) + "hazırı temel al" (git ls-files, wc mantığı; sıfırdan
tokenizer yok).

Grain (world-model §2 kuralı): veri/kod-envanter.jsonl — 1 satır = 1 ÖLÇÜM OLGUSU
  {ts, kod_sha, kosum_id, grup, nesne, metrik, deger, birim, not}
  grup ∈ {envanter, ucuncu_parti, arac_zinciri, gecikme} · uzun format · append-only (m.8: silinmez) · tekrar-üretilebilir alanlar HEAD'e bağlı.

Ne sayar:
  1. envanter      — git-izlenen dosyalar uzantıya göre DİL sınıfına ayrılır (py js ts sh ps1 sql go rs cue …); katman etiketi:
                     kod / konfig / kanon-metin / veri. Dosya sayısı + satır sayısı; kod için dizin kırılımı (tools/ · .claude/ · cc/workflow/ · ogrenme/ · diğer).
  2. ucuncu_parti  — Python dosyalarının en-üst-düzey import'ları; stdlib dışı olanlar listelenir (stdlib tespiti: importlib.util.find_spec
                     ile modül yolu sys.base_prefix altında mı / builtin mi — Python 3.9'da sys.stdlib_module_names yok).
  3. arac_zinciri  — hangi çalıştırıcılar kurulu (go cargo rustc cue pkl nickel jsonnet opa dhall node deno bun uv python3 sqlite3 rg duckdb treehouse gnhf …) + sürüm ilk satırı.
  4. gecikme       — başlangıç gecikmesi (n koşum, MEDYAN + MİN, ms): yerel exe taban · bash · sqlite3 · python3 boş · python3+stdlib · node boş ·
                     PreToolUse teli (örnek Bash girdisiyle) · SessionStart hook · tipik tools/ script'i. --gecikme-yok ile atlanır.

Kullanım: python3 tools/kod-envanter.py [--repo <yol>] [--n 10] [--gecikme-yok] [--json] [--kuru] [--sessiz]
  --json   : stdout'a TEK JSON nesnesi (makine-okur; axi deseni — ilerleme/uyarı stderr'e). İnsan-yüzü tablo yalnız --json yokken.
  --kuru   : bronz satırı yazmaz.
Çıkış kodu: 0 tamam · 2 git/repo yok. Uyarılar çıkışı değiştirmez.
Deneysel m.29 (2026-08-26, Carvis). Additive-only: alan silinmez/yeniden adlandırılmaz.
"""
import argparse, importlib.util, json, os, re, shutil, statistics, subprocess, sys, time
from datetime import datetime, timezone, timedelta

UZANTI_DIL = {
    ".py": ("python", "kod"), ".js": ("javascript", "kod"), ".mjs": ("javascript", "kod"), ".ts": ("typescript", "kod"),
    ".sh": ("shell", "kod"), ".bash": ("shell", "kod"), ".zsh": ("shell", "kod"), ".ps1": ("powershell", "kod"),
    ".sql": ("sql", "kod"), ".go": ("go", "kod"), ".rs": ("rust", "kod"), ".cue": ("cue", "kod"), ".pkl": ("pkl", "kod"),
    ".rego": ("rego", "kod"), ".jsonnet": ("jsonnet", "kod"), ".ncl": ("nickel", "kod"), ".dhall": ("dhall", "kod"),
    ".json": ("json", "konfig"), ".yaml": ("yaml", "konfig"), ".yml": ("yaml", "konfig"), ".toml": ("toml", "konfig"),
    ".md": ("markdown", "kanon-metin"), ".jsonl": ("jsonl", "veri"), ".csv": ("csv", "veri"), ".d2": ("d2", "kanon-metin"),
    ".html": ("html", "kanon-metin"), ".svg": ("svg", "kanon-metin"),
}
KOD_DIZIN_SIRASI = ("tools/", ".claude/", "cc/workflow/", "ogrenme/", "raporlar/", "cc/")
ARACLAR = ["go", "cargo", "rustc", "cue", "pkl", "nickel", "jsonnet", "opa", "dhall", "node", "deno", "bun", "uv", "python3", "sqlite3",
           "rg", "duckdb", "treehouse", "gnhf", "gh", "git", "jq"]


def sh(cmd, cwd=None, inp=None):
    return subprocess.run(cmd, cwd=cwd, input=inp, capture_output=True, text=True)


def git_dosyalar(repo):
    r = sh(["git", "ls-files", "-z"], repo)
    if r.returncode != 0:
        return None
    return [f for f in r.stdout.split("\0") if f]


def disla_dizinlerini_yukle(repo):
    """M14 (Karar 88): DISLA_DIZIN tek kaynaktan — tools/kod-orani-olcum.py modülünü importlib ile (dosya adı
    tire içerdiği için düz import olmaz) yükleyip aynı sabiti kullanır, tekrar tanımlamaz. Modül yüklenemezse
    (dosya taşındı/bozuldu) yalnız karantina dizinine düşen dar bir yedek kümeyle devam eder (fail-soft)."""
    yol = os.path.join(repo, "tools", "kod-orani-olcum.py")
    try:
        spec = importlib.util.spec_from_file_location("kod_orani_olcum_disla_kaynak", yol)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return set(mod.DISLA_DIZIN)
    except Exception:
        return {os.path.join("arsiv", "karantina")}


def disla_uygula(dosyalar, disla_kume):
    """git-izlenen dosya listesinden DISLA_DIZIN altına düşenleri süzer (arsiv/karantina dahil, İB-72/M14)."""
    sonuc = []
    for f in dosyalar:
        if any(f == d or f.startswith(d + "/") for d in disla_kume):
            continue
        sonuc.append(f)
    return sonuc


def satir_say(yol):
    try:
        with open(yol, "rb") as fh:
            return sum(1 for _ in fh)
    except OSError:
        return 0


def kod_dizini(yol):
    for d in KOD_DIZIN_SIRASI:
        if yol.startswith(d):
            return d.rstrip("/")
    return "diger"


def envanter(repo, dosyalar):
    """Dil × katman × dizin sayımı. Deterministik (git ls-files sırası + sıralı dict)."""
    dil = {}
    dizin = {}
    for f in dosyalar:
        ext = os.path.splitext(f)[1].lower()
        if ext not in UZANTI_DIL:
            continue
        ad, katman = UZANTI_DIL[ext]
        n = satir_say(os.path.join(repo, f))
        d = dil.setdefault(ad, {"katman": katman, "dosya": 0, "satir": 0})
        d["dosya"] += 1; d["satir"] += n
        if katman == "kod":
            k = dizin.setdefault(kod_dizini(f), {})
            kk = k.setdefault(ad, {"dosya": 0, "satir": 0})
            kk["dosya"] += 1; kk["satir"] += n
    return dict(sorted(dil.items())), {k: dict(sorted(v.items())) for k, v in sorted(dizin.items())}


IMPORT_RE = re.compile(r"^\s*(?:import\s+([A-Za-z_][\w\.]*)|from\s+([A-Za-z_][\w\.]*)\s+import)", re.M)


def stdlib_mi(mod):
    kok = mod.split(".")[0]
    if kok in sys.builtin_module_names:
        return True
    try:
        spec = importlib.util.find_spec(kok)
    except (ImportError, ValueError):
        return False
    if spec is None:
        return False
    if spec.origin in ("built-in", "frozen"):
        return True
    yol = spec.origin or (spec.submodule_search_locations and list(spec.submodule_search_locations)[0]) or ""
    taban = os.path.realpath(sys.base_prefix)
    return os.path.realpath(yol).startswith(taban) and "site-packages" not in yol


def ucuncu_parti(repo, dosyalar):
    """Python dosyalarının stdlib-dışı en-üst-düzey import'ları (yerel modül adları da 'stdlib-dışı' görünür → not'ta ayrılır)."""
    yerel = {os.path.splitext(os.path.basename(f))[0] for f in dosyalar if f.endswith(".py")}
    dis = {}
    for f in dosyalar:
        if not f.endswith(".py"):
            continue
        try:
            metin = open(os.path.join(repo, f), encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for m in IMPORT_RE.finditer(metin):
            mod = (m.group(1) or m.group(2)).split(".")[0]
            if mod in yerel or stdlib_mi(mod):
                continue
            dis.setdefault(mod, []).append(f)
    return {k: sorted(set(v)) for k, v in sorted(dis.items())}


def arac_zinciri():
    out = {}
    for a in ARACLAR:
        p = shutil.which(a)
        if not p:
            out[a] = {"kurulu": False, "yol": None, "surum": None}
            continue
        surum = None
        for bayrak in (["--version"], ["version"], ["-V"]):
            r = sh([a] + bayrak)
            s = (r.stdout or r.stderr).strip().splitlines()
            if r.returncode == 0 and s:
                surum = s[0][:80]; break
        out[a] = {"kurulu": True, "yol": p, "surum": surum}
    return out


def medyan_ms(cmd, n, cwd, inp=None):
    ts = []
    for _ in range(n):
        t = time.perf_counter(); subprocess.run(cmd, cwd=cwd, input=inp, capture_output=True); ts.append((time.perf_counter() - t) * 1000)
    return round(statistics.median(ts), 1), round(min(ts), 1)


def gecikme(repo, n):
    hook_girdi = json.dumps({"tool_name": "Bash", "tool_input": {"command": "echo merhaba"}, "cwd": repo}).encode()
    adaylar = [
        ("yerel-exe-taban", ["/usr/bin/true"], None),
        ("bash-bos", ["bash", "-c", "true"], None),
        ("sqlite3-select1", ["sqlite3", ":memory:", "select 1"], None),
        ("python3-bos", ["python3", "-c", "pass"], None),
        ("python3-stdlib-import", ["python3", "-c", "import json,os,re,sys,subprocess,pathlib,hashlib,datetime,sqlite3"], None),
        ("node-bos", ["node", "-e", ""], None),
        ("hook-pretool-core-tel", ["bash", ".claude/hooks/pretool-core-tel.sh"], hook_girdi),
        ("hook-session-start", ["bash", ".claude/hooks/session-start.sh"], None),
        ("tools-kural-sayaci", ["python3", "tools/kural-sayaci.py"], None),
    ]
    out = {}
    for ad, cmd, inp in adaylar:
        exe = cmd[0] if cmd[0].startswith("/") else shutil.which(cmd[0])
        if not exe or (len(cmd) > 1 and cmd[1].startswith((".claude", "tools")) and not os.path.exists(os.path.join(repo, cmd[1]))):
            out[ad] = {"medyan_ms": None, "min_ms": None, "not": "yok"}; continue
        med, mn = medyan_ms(cmd, n, repo, inp)
        out[ad] = {"medyan_ms": med, "min_ms": mn, "not": "n=%d" % n}
    return out


def main():
    ap = argparse.ArgumentParser(description="Jarvis kod envanteri + araç-zinciri + başlangıç-gecikmesi (stdlib-only)")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--n", type=int, default=10, help="gecikme ölçümü tekrar sayısı (medyan)")
    ap.add_argument("--gecikme-yok", action="store_true")
    ap.add_argument("--json", action="store_true", help="stdout'a tek JSON nesnesi (ilerleme stderr'e)")
    ap.add_argument("--kuru", action="store_true")
    ap.add_argument("--sessiz", action="store_true")
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)
    dosyalar = git_dosyalar(repo)
    if dosyalar is None:
        print("HATA: git repo değil: %s" % repo, file=sys.stderr); return 2
    dosyalar = disla_uygula(dosyalar, disla_dizinlerini_yukle(repo))
    head = sh(["git", "rev-parse", "--short", "HEAD"], repo).stdout.strip() or "-"
    tz = timezone(timedelta(hours=3))
    ts = datetime.now(tz).replace(microsecond=0).isoformat()
    kosum_id = "kod-envanter:%s:%s" % (head, ts[:10])

    dil, dizin = envanter(repo, dosyalar)
    dis = ucuncu_parti(repo, dosyalar)
    arac = arac_zinciri()
    gec = None if a.gecikme_yok else gecikme(repo, a.n)
    makine = sh(["sw_vers", "-productVersion"]).stdout.strip() or sh(["uname", "-sr"]).stdout.strip()

    olgular = []
    def olgu(grup, nesne, metrik, deger, birim, not_=""):
        olgular.append({"ts": ts, "kod_sha": head, "kosum_id": kosum_id, "grup": grup, "nesne": nesne, "metrik": metrik, "deger": deger, "birim": birim, "not": not_})
    for ad, d in dil.items():
        olgu("envanter", ad, "dosya", d["dosya"], "adet", d["katman"]); olgu("envanter", ad, "satir", d["satir"], "satir", d["katman"])
    for dz, diller in dizin.items():
        for ad, d in diller.items():
            olgu("envanter", "%s:%s" % (dz, ad), "satir", d["satir"], "satir", "kod dizin kırılımı; dosya=%d" % d["dosya"])
    olgu("ucuncu_parti", "python", "stdlib_disi_modul", len(dis), "adet", ", ".join(dis) if dis else "stdlib-only")
    for ad, v in arac.items():
        olgu("arac_zinciri", ad, "kurulu", 1 if v["kurulu"] else 0, "bool", v["surum"] or "")
    if gec:
        for ad, v in gec.items():
            if v["medyan_ms"] is not None:
                olgu("gecikme", ad, "baslangic_medyan", v["medyan_ms"], "ms", "%s · %s · min %.1f" % (v["not"], makine, v["min_ms"]))

    if not a.kuru:
        with open(os.path.join(repo, "veri", "kod-envanter.jsonl"), "a", encoding="utf-8") as fh:
            for o in olgular:
                fh.write(json.dumps(o, ensure_ascii=False) + "\n")

    sonuc = {"ts": ts, "kod_sha": head, "kosum_id": kosum_id, "makine": makine, "dil": dil, "kod_dizin": dizin, "ucuncu_parti": dis,
             "arac_zinciri": arac, "gecikme": gec, "olgu_sayisi": len(olgular), "yazildi": not a.kuru}
    if a.json:
        print(json.dumps(sonuc, ensure_ascii=False, indent=1)); return 0
    if a.sessiz:
        return 0
    print("KOD ENVANTERİ · HEAD %s · %s · %s" % (head, ts, makine))
    print("  dil                 katman        dosya    satır")
    for ad, d in sorted(dil.items(), key=lambda kv: (kv[1]["katman"], -kv[1]["satir"])):
        print("  %-19s %-12s %6d %8d" % (ad, d["katman"], d["dosya"], d["satir"]))
    print("  kod dizin kırılımı (satır):", " · ".join("%s=%s" % (dz, ",".join("%s %d" % (ad, v["satir"]) for ad, v in diller.items())) for dz, diller in dizin.items()))
    print("  python stdlib-dışı import:", ", ".join("%s (%d dosya)" % (k, len(v)) for k, v in dis.items()) if dis else "YOK (stdlib-only)")
    print("  araç-zinciri kurulu:", ", ".join(k for k, v in arac.items() if v["kurulu"]))
    print("  araç-zinciri YOK   :", ", ".join(k for k, v in arac.items() if not v["kurulu"]))
    if gec:
        print("  başlangıç gecikmesi (n=%d medyan ms):" % a.n, " · ".join("%s %.1f" % (k, v["medyan_ms"]) for k, v in gec.items() if v["medyan_ms"] is not None))
    print("  → %d olgu %s" % (len(olgular), "(kuru)" if a.kuru else "veri/kod-envanter.jsonl"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
