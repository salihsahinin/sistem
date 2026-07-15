#!/usr/bin/env python3
"""verify-push — push-dogrulama loop'unun deterministik dogrulayicisi (loop-eng Faz 2).

Y kosulu: ∀f∈D: origin ≡ mount — yani calisma agacindaki HER dosya origin'deki
son commit'le birebir ayni VE lokal HEAD origin'le esit VE commit'lenmemis
degisiklik yok. Saglanirsa "VERIFY-PUSH: PASS" + exit 0; saglanmazsa teshis
listesi + exit 1. /goal evaluator'inin bakacagi kriter budur (deterministik).

Kullanim: python tools/verify-push.py [repo-koku]   (varsayilan: bu dosyanin ust klasoru)
"""
import os
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def git(args, cwd):
    return subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True)


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))
    failures = []

    # 0) fetch — origin'in guncel halini al
    r = git(["fetch", "origin", "--quiet"], root)
    if r.returncode != 0:
        print("VERIFY-PUSH: FAIL")
        print(f"- fetch basarisiz: {r.stderr.strip()}")
        sys.exit(1)

    # dal adi (main varsayma — tespit et)
    branch = git(["rev-parse", "--abbrev-ref", "HEAD"], root).stdout.strip()
    upstream = f"origin/{branch}"

    # 1) commit'lenmemis degisiklik var mi? (mount'ta olup push'ta olmayan icerik)
    r = git(["status", "--porcelain"], root)
    dirty = [l for l in r.stdout.splitlines() if l.strip()]
    if dirty:
        failures.append(f"commit'lenmemis degisiklik ({len(dirty)} dosya): "
                        + ", ".join(l[3:] for l in dirty[:10]))

    # 2) HEAD ↔ origin esit mi? (ahead = push eksik, behind = mount bayat)
    r = git(["rev-list", "--left-right", "--count", f"{upstream}...HEAD"], root)
    if r.returncode != 0:
        failures.append(f"{upstream} cozulemedi: {r.stderr.strip()}")
    else:
        behind, ahead = (int(x) for x in r.stdout.split())
        if ahead:
            failures.append(f"push eksik: HEAD {ahead} commit onde ({upstream}'e gore)")
        if behind:
            failures.append(f"mount bayat: HEAD {behind} commit geride — pull gerekli")

    # 3) calisma agaci ↔ origin dosya-bazli fark (V43 sinifi: icerik sapmasi)
    r = git(["diff", "--name-only", upstream], root)
    diff_files = [l for l in r.stdout.splitlines() if l.strip()]
    if diff_files:
        failures.append(f"origin≢mount ({len(diff_files)} dosya): " + ", ".join(diff_files[:10]))

    if failures:
        print("VERIFY-PUSH: FAIL")
        for f in failures:
            print(f"- {f}")
        sys.exit(1)

    print(f"VERIFY-PUSH: PASS (dal: {branch}, HEAD == {upstream}, agac temiz)")
    sys.exit(0)


if __name__ == "__main__":
    main()
