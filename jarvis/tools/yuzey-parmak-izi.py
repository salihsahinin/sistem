#!/usr/bin/env python3
"""yuzey-parmak-izi.py — Bu oturumun YÜZEY parmak izini basar: hangi uygulama/giriş noktası, yetki seti eşit mi (STDLIB ONLY).

Neden: m.41 GEÇİŞ KAYDI-2 (Salih Katman-1, 2026-08-17, KB-34): "masaüstü uygulamasından (Cowork) açılan Claude ile terminalde çalışan Claude
TAMAMEN aynı yetki ve özelliklere sahipse Cowork ana-sıra olsun; model = en güçlü mevcut model (bugün Fable, yarın değişebilir)."
Yetki eşitliği VARSAYILMAZ, ÖLÇÜLÜR (deterministik tasarım): iki yüzeyde aynı script koşar, çıktılar yan yana konur; her satır eşitse koşul PASS.

Ne bakar (her satır bir kanıt; sır basmaz — token/anahtar değerleri MASKELİ):
  1. Giriş noktası: CLAUDE_CODE_ENTRYPOINT (cli | claude-desktop | …), __CFBundleIdentifier, CLAUDE_AGENT_SDK_VERSION, TERM_PROGRAM
  2. Repo: cwd git repo mu · HEAD · çalışma ağacı yazılabilir mi (scratch dosya; core/'a YAZMAZ) · origin uzak adresi var mı
  3. Ayar/kanon: .claude/settings.json var (hook kayıtları · push=ask) · hook dosyaları · skill sayısı · CLAUDE.md boyutu
  4. Kısıt işaretleri: sandbox/mount ipuçları (cwd yolu, /mnt, /sandbox, HOME dışı), python3/git/sqlite3 sürümleri
  5. Ortam değişkeni adları (değerler MASKELİ): CLAUDE_* listesi — iki yüzeyde ad kümesi karşılaştırılır
Kullanım: python3 tools/yuzey-parmak-izi.py [--json] [--repo <yol>]  → çıktıyı raporlar/yuzey-parmak-izi-<etiket>.txt'ye kaydet, öbür yüzeyle diff'le.
Karar kuralı (GK-2): git yaz+commit OK ∧ hook'lar mevcut ∧ skill sayısı eşit ∧ settings ask/deny eşit ∧ araç seti (ajan beyanı) eşit → yetki EŞİT.
Deneysel m.29 (2026-08-17, seans-8).
"""
import os, sys, json, subprocess, shutil, hashlib

def sh(cmd, cwd=None):
    try: return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=10).stdout.strip()
    except Exception as e: return f"[hata: {e}]"

def main():
    repo = os.path.abspath(sys.argv[sys.argv.index("--repo")+1]) if "--repo" in sys.argv else os.getcwd()
    r = {}
    env = os.environ
    r["giris"] = {"CLAUDE_CODE_ENTRYPOINT": env.get("CLAUDE_CODE_ENTRYPOINT"), "bundle": env.get("__CFBundleIdentifier"),
                  "sdk": env.get("CLAUDE_AGENT_SDK_VERSION"), "TERM_PROGRAM": env.get("TERM_PROGRAM"), "AI_AGENT": env.get("AI_AGENT"), "cwd": os.getcwd(), "HOME": env.get("HOME")}
    inrepo = sh(["git", "rev-parse", "--is-inside-work-tree"], repo) == "true"
    r["repo"] = {"git_repo": inrepo, "HEAD": sh(["git", "rev-parse", "--short", "HEAD"], repo) if inrepo else None,
                 "origin": (sh(["git", "remote", "get-url", "origin"], repo).split("@")[-1] if inrepo else None)}
    # yazılabilirlik: yalnız scratch dosyası (core/ ve CLAUDE.md'ye DOKUNMAZ)
    try:
        t = os.path.join(repo, ".yuzey-parmak-izi.tmp"); open(t, "w").write("x"); os.remove(t); r["repo"]["yazilabilir"] = True
    except Exception as e: r["repo"]["yazilabilir"] = f"HAYIR ({e})"
    st = os.path.join(repo, ".claude", "settings.json")
    try:
        s = json.load(open(st, encoding="utf-8")); perm = s.get("permissions", {})
        r["ayar"] = {"settings": True, "ask": perm.get("ask"), "deny": perm.get("deny"), "hook_olaylari": sorted((s.get("hooks") or {}).keys())}
    except Exception as e: r["ayar"] = {"settings": f"YOK/okunamadı ({e})"}
    hd = os.path.join(repo, ".claude", "hooks"); sk = os.path.join(repo, ".claude", "skills")
    r["kanon"] = {"hook_dosyalari": sorted(os.listdir(hd)) if os.path.isdir(hd) else None,
                  "skill_sayisi": len([d for d in os.listdir(sk) if os.path.isdir(os.path.join(sk, d))]) if os.path.isdir(sk) else None,
                  "CLAUDE_md_bayt": os.path.getsize(os.path.join(repo, "CLAUDE.md")) if os.path.exists(os.path.join(repo, "CLAUDE.md")) else None}
    r["kisit"] = {"mount_ipucu": any(p in os.getcwd() for p in ("/mnt/", "/sandbox", "/workspace")) or not os.getcwd().startswith(env.get("HOME", "/")),
                  "python3": sys.version.split()[0], "git": sh(["git", "--version"]), "sqlite3": bool(shutil.which("sqlite3")), "claude_cli": bool(shutil.which("claude"))}
    r["env_adlari"] = sorted(k for k in env if k.startswith(("CLAUDE", "AI_AGENT", "CLAUDECODE")))
    ozet = f"{r['giris']['CLAUDE_CODE_ENTRYPOINT']}|{r['giris']['bundle']}|repo={inrepo}|yaz={r['repo'].get('yazilabilir')}|ask={r.get('ayar',{}).get('ask')}|skill={r['kanon']['skill_sayisi']}|hook={r['kanon']['hook_dosyalari']}"
    r["parmak_izi_sha8"] = hashlib.sha256(ozet.encode()).hexdigest()[:8]
    if "--json" in sys.argv: print(json.dumps(r, ensure_ascii=False, indent=1)); return
    print("=== YÜZEY PARMAK İZİ (yetki-eşitliği karşılaştırması için) ===")
    for k, v in r.items(): print(f"{k}: {json.dumps(v, ensure_ascii=False)}")
    print("Karar kuralı (m.41 GK-2): iki yüzeyde 'repo/ayar/kanon/kisit' blokları eşit ∧ ajan araç seti eşit → yetki EŞİT.")

if __name__ == "__main__":
    main()
