#!/usr/bin/env python3
"""caps-say.py — pre-commit telinin sayacı: stdin'deki markdown metninde "büyük harf = kod" kuralını bozan sözcük sayısını basar
(tools/buyuk-harf-temizle.py donustur() ile aynı süzgeç; tek tanım). Kullanım: git show :yol | python3 tools/git-hooks/caps-say.py <repo-kök>
Çıkış: stdout = sayı (0 temiz); kod 0."""
import collections, importlib.util, pathlib, sys

kok = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
spec = importlib.util.spec_from_file_location("bh", kok / "tools" / "buyuk-harf-temizle.py")
bh = importlib.util.module_from_spec(spec); spec.loader.exec_module(bh)
say = collections.Counter()
bh.donustur(sys.stdin.read(), say)
print(say["vurgu"] + say["durum"])
