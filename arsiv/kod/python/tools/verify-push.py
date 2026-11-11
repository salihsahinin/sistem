#!/usr/bin/env python3
"""verify-push — push-doğrulama loop'unun deterministik doğrulayıcısı (loop-eng Faz 2).

Y koşulu: ∀f∈D: origin ≡ mount — yani çalışma ağacındaki HER dosya origin'deki
son commit'le birebir aynı VE lokal HEAD origin'le eşit VE commit'lenmemiş
değişiklik yok. Sağlanırsa "VERIFY-PUSH: PASS" + exit 0; sağlanmazsa teşhis
listesi + exit 1. /goal evaluator'ının bakacağı kriter budur (deterministik).

Kullanım: python tools/verify-push.py [repo-kökü]   (varsayılan: bu dosyanın üst klasörü)
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

    # 0) fetch — origin'in güncel hâlini al
    r = git(["fetch", "origin", "--quiet"], root)
    if r.returncode != 0:
        print("VERIFY-PUSH: FAIL")
        print(f"- fetch başarısız: {r.stderr.strip()}")
        sys.exit(1)

    # dal adı (main varsayma — tespit et)
    branch = git(["rev-parse", "--abbrev-ref", "HEAD"], root).stdout.strip()
    upstream = f"origin/{branch}"

    # 1) commit'lenmemiş değişiklik var mı? (mount'ta olup push'ta olmayan içerik)
    r = git(["status", "--porcelain"], root)
    dirty = [l for l in r.stdout.splitlines() if l.strip()]
    if dirty:
        failures.append(f"commit'lenmemiş değişiklik ({len(dirty)} dosya): "
                        + ", ".join(l[3:] for l in dirty[:10]))

    # 2) HEAD ↔ origin eşit mi? (ahead = push eksik, behind = mount bayat)
    r = git(["rev-list", "--left-right", "--count", f"{upstream}...HEAD"], root)
    if r.returncode != 0:
        failures.append(f"{upstream} cozulemedi: {r.stderr.strip()}")
    else:
        behind, ahead = (int(x) for x in r.stdout.split())
        if ahead:
            failures.append(f"push eksik: HEAD {ahead} commit önde ({upstream}'e göre)")
        if behind:
            failures.append(f"mount bayat: HEAD {behind} commit geride — pull gerekli")

    # 3) çalışma ağacı ↔ origin dosya-bazlı fark (V43 sınıfı: içerik sapması)
    r = git(["diff", "--name-only", upstream], root)
    diff_files = [l for l in r.stdout.splitlines() if l.strip()]
    if diff_files:
        failures.append(f"origin≢mount ({len(diff_files)} dosya): " + ", ".join(diff_files[:10]))

    if failures:
        print("VERIFY-PUSH: FAIL")
        for f in failures:
            print(f"- {f}")
        sys.exit(1)

    print(f"VERIFY-PUSH: PASS (dal: {branch}, HEAD == {upstream}, ağaç temiz)")
    sys.exit(0)


if __name__ == "__main__":
    main()
