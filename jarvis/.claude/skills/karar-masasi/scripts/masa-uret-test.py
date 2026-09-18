#!/usr/bin/env python3
"""karar-masasi · deterministik test (İB-88 P2, 09-15): evals/evals.json E1-E3'ü koşar.
E1 spec-doğrulama (öneri ikinci sırada → çıkış 2, dosya yok) · E2 determinizm (aynı spec iki üretim bayt-eşit, form = kalem, önerilen ilk label)
· E3 masa-12 eşdeğerlik (elle masa → masa-spec-cikar → masa-uret; form/label/checkbox/kanıt sayımı + kuyrukla fonksiyonları birebir + büyük-harf ihlali elle-yazımdan fazla değil).
Kullanım: python3 masa-uret-test.py [--repo ~/sistem/jarvis] [--masa raporlar/masa/masa-12-karar-yuzeyi-2026-09-15.html]
Çıkış: 0 hepsi geçti · 1 en az biri düştü. Kanona yazmaz; geçici dizinde üretir.
"""
import argparse, json, pathlib, re, subprocess, sys, tempfile
BURASI = pathlib.Path(__file__).resolve().parent
URET, CIKAR = BURASI / "masa-uret.py", BURASI / "masa-spec-cikar.py"
IZ = set("DONE PASS FAIL AS-OF PROBE PLAN TEACH CLOSE DAG MCP OWASP YAML JSON HTML CSV PDF SVG CI API SQL URL CLI IDE SDK LLM RAG "  # Carvis = Jarvis (eski ad, Karar 93)
         "README HEAD MEMORY CLAUDE JARVIS JARVİS FRIDAY CARVIS ATLAS OPUS SONNET HAIKU FABLE KB MB FIFO SHA İB EK SKILL KILAVUZ "
         "KALAN BEKLET ONAR GEÇTİ RET SCRIPTLER HİÇBİRİ".split())

def caps(t):
    t = re.sub(r"<script>.*?</script>", "", t, flags=re.S); t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"aynen:\s*[\"“][^\"”]*[\"”]", " ", t)
    return sorted({w for w in re.findall(r"(?<![\w./-])[A-ZÇĞİÖŞÜ]{4,}(?![\w./-])", t) if w not in IZ})

def fn(t, ad):
    m = re.search(r"function " + ad + r"\(.*?\n}\n", t, re.S); return m.group(0) if m else None

def uret(spec_yolu, repo):
    return subprocess.run([sys.executable, str(URET), str(spec_yolu), "--repo", str(repo)], capture_output=True, text=True)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--repo", default=str(pathlib.Path.home() / "sistem" / "jarvis"))
    ap.add_argument("--masa", default="raporlar/masa/masa-12-karar-yuzeyi-2026-09-15.html")
    a = ap.parse_args(); repo = pathlib.Path(a.repo); elle_yol = repo / a.masa
    T = pathlib.Path(tempfile.mkdtemp(prefix="masa-test-")); sonuc = []
    def kayit(ad, ok, not_=""): sonuc.append(ok); print(f"  [{'PASS' if ok else 'FAIL'}] {ad}" + (f" — {not_}" if not_ else ""))
    # spec: elle masadan çıkar
    r = subprocess.run([sys.executable, str(CIKAR), str(elle_yol), "--karar", "Karar 96"], capture_output=True, text=True)
    if r.returncode != 0:
        print("çıkarıcı düştü:", r.stderr); sys.exit(1)
    spec = json.loads(r.stdout); spec_yolu = T / "spec.json"; spec_yolu.write_text(r.stdout, encoding="utf-8")
    h = elle_yol.read_text(encoding="utf-8")
    # E1
    bad = json.loads(r.stdout); s0 = bad["kalemler"][0]["secenekler"]; s0[0], s0[1] = s0[1], s0[0]
    bad_yolu = T / "bad.json"; bad_yolu.write_text(json.dumps(bad, ensure_ascii=False), encoding="utf-8")
    r1 = uret(bad_yolu, T / "r0")
    kayit("E1 öneri ikinci sırada → çıkış 2 + mesaj", r1.returncode == 2 and "ilk sırada değil" in r1.stdout)
    kayit("E1 dosya yazılmadı", not (T / "r0" / "raporlar").exists())
    # E2
    cikti = []
    for i in (1, 2):
        rr = uret(spec_yolu, T / f"r{i}")
        if rr.returncode != 0: print("üretim düştü:", rr.stdout); sys.exit(1)
        cikti.append((T / f"r{i}" / "raporlar" / "masa" / f"masa-{spec['no']}-karar-yuzeyi-{spec['tarih']}.html").read_bytes())
    g = cikti[0].decode("utf-8")
    kayit("E2 iki üretim bayt-eşit", cikti[0] == cikti[1])
    kayit("E2 form sayısı = kalem sayısı", g.count("data-lavish-question=") == len(spec["kalemler"]), f"{g.count('data-lavish-question=')}/{len(spec['kalemler'])}")
    bolumler = re.findall(r'<section class="card bg-base-100 shadow-md" data-lavish-question=.*?</section>', g, re.S)
    ilk_oneri = all(re.search(r'<div class="space-y-2">\s*<label class="opt oneri', b) for b in bolumler if "opt oneri" in b)
    kayit("E2 önerili kalemlerde önerilen ilk label", ilk_oneri)
    # E3
    for ad, desen in (("form", "data-lavish-question="), ("label", '<label class="opt'), ("checkbox", 'type="checkbox"'), ("kanıt satırı", "<tr><td>")):
        kayit(f"E3 {ad} sayısı elle = üretilen", g.count(desen) == h.count(desen), f"{g.count(desen)}/{h.count(desen)}")
    kayit("E3 kuyrukla birebir", fn(g, "kuyrukla") == fn(h, "kuyrukla"))
    kayit("E3 kuyruklaCoklu birebir", fn(g, "kuyruklaCoklu") == fn(h, "kuyruklaCoklu"))
    # E4 (09-18 arızası: başlıkta kesme işareti → onsubmit JS bozuluyordu; masa-13 M3/M12/M13 tıklanınca sayfa çöktü)
    import html as _html
    onsubmit = [_html.unescape(m) for m in re.findall(r'onsubmit="([^"]*)"', g)]
    js_ok = all(re.fullmatch(r"event\.preventDefault\(\); kuyrukla(?:Coklu)?\(this,'M\d+',\"(?:[^\"\\\\]|\\\\.)*\"\);", o) for o in onsubmit)
    kayit("E4 onsubmit JS dizesi kesme işaretine dayanıklı", js_ok and len(onsubmit) == len(spec["kalemler"]), f"{len(onsubmit)} form")
    cu, ce = caps(g), caps(h)
    kayit("E3 büyük-harf ihlali elle-yazımı aşmıyor", set(cu) <= set(ce), f"üretilen {cu} · elle {ce}")
    print(f"sonuç: {sum(sonuc)}/{len(sonuc)} · üretilen {len(cikti[0])} B / elle {len(h.encode())} B · spec {spec_yolu.stat().st_size} B · geçici {T}")
    sys.exit(0 if all(sonuc) else 1)

if __name__ == "__main__":
    main()
