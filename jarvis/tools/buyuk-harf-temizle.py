#!/usr/bin/env python3
"""buyuk-harf-temizle.py — "büyük harf = kod" kuralı temizliği (Salih 09-15 yan-görevi 2, onay "onay, önce kuru diff koş").
Kural: kanonda tamamı büyük harfli sözcük ya KISALTMADIR (beyaz liste, dokunulmaz) ya da backtick içinde makine-jetonudur
(`DONE`, `BAYAT`); vurgu yalnız kalın harftir. Kök neden: yüklenen bağlamda 1.590 caps sözcük (19-35‰), model çoğunluk üslubunu
taklit ediyor (rapor raporlar/2026-09/buyuk-harf-vurgu-analizi-2026-09-15.md + defter 09-15 hook arızası).

Sınıflar:  durum-jetonu (DURUM kümesi: KAPANDI, BAYAT, DONE, PROBE …) → `JETON`  ·  vurgu (geri kalan ≥4 harfli caps) → **küçük harf**
           (ardışık vurgu sözcükleri tek kalın span: "TEK SORU" → **tek soru**); YAML ön-blok satırlarında (description …) kalın işareti
           konmaz, yalnız küçültülür (kapi-denetim regex'leri `kullanma[:;]` biçimini arar).
Korunur:  kod blokları, satır-içi kod, URL, `aynen: "…"` Salih alıntıları, tire/alt-çizgi/nokta bitişik tanımlayıcılar, beyaz liste.
Kapsam:   --katman sicak (CLAUDE.md · core/*.md · .claude/skills/*/SKILL.md · .claude/rules/*.md · ~/.claude/CLAUDE.md · hafıza *.md)
          · ilik (+ KILAVUZ.md · wiki/*.md · .claude/skills/*/references/*.md · .claude/skills/README.md)
          · ogrenme (09-17: ogrenme/README+mufredat · <şerit>/README · ilerleme · dersler/*.md · *-seti/*.md — yan oturumun canlı bağlamı) · hepsi. Soğuk katman (raporlar/cc/arşiv) yazılmaz (tarihçe).
Kullanım: python3 tools/buyuk-harf-temizle.py [--katman sicak|ilik|hepsi] [--kuru] [--uygula] [--diff <yol>] [--goster N] [--json]
Çıkış:    0 (kuru: değişiklik listelendi / uygula: yazıldı) · 2 hata. Türkçe küçültme: İ→i, I→ı (Python lower() 'İ'yi bozar).
"""
import argparse, difflib, json, pathlib, re, sys, collections
import harness_anahtar

IZ = set("""AS-OF DAG MCP OWASP YAML JSON JSONL YML CSV HTML HTTP HTTPS PDF SVG PNG CI CD API SQL URL URI CLI GUI IDE SDK LLM RAG AXI GNHF OCR USD EUR TRY CV
HITL ASR NDCG MAP MRR GSM8K SWE UK AISI AWS DEA GCP MIT OCW README HEAD MEMORY CLAUDE JARVIS JARVİS FRIDAY CARVIS ATLAS OPUS SONNET HAIKU FABLE GPT KB MB GB
FIFO LIFO SHA UTC TR EN ID UID DNS TLS SSH OAUTH NEMO NLP ML AI ETL ELT DBT SPARK MLOPS LTR PR PRS CTR ROC AUC F1 REGEX BPE ROPE KV SFT RLHF CVE CVSS CWE UTF
İB EK SKILL SCRIPTLER KILAVUZ IAM DRFR NOOP CEO PC MAC VS UTF-8 SCD LUD OWL OBO SKOS SEMVER PEP RIPPLE DDQ DAMA NL GA ASCII OCR NLI RRF BM25 FTS SQLITE
COVE DAG CI/CD OKR KPI ROI SLA SLO SRE QA UX UI CSS JS TS PY SH MD TXT HTML5 LAVISH DAISYUI""".split())
DURUM = set("""DONE PASS FAIL WARN ERROR TODO RED YOK RET KAPANDI AKTİF BEKLEYEN BLOKE BAYAT TAZE SÜPERSEDE EMEKLİ DÜŞTÜ SAĞLAM DARALDI FLAG SNAPSHOT DONDU KISMİ TUTTU İMZALANDI
DAYANAKSIZ DESTEKLİ ÇELİŞİR TEMİZ İHLAL RET ŞÜPHE YOK HATA ANALYZE KALAN BEKLET ONAR GEÇTİ YARIM PROBE PLAN TEACH CLOSE TODO DOĞRU
YANLIŞ ERTELENDİ SÜPERSEDE-EDİLDİ KAPALI DEVAM DURDU ONAYLI ONAYSIZ EKSİK PASİF HAZIR TAMAM YARIM-DONE""".split())
CAPS = re.compile(r"(?<![\w./\-*_])[A-ZÇĞİÖŞÜ]{4,}(?![\w./\-_])")
TRLOW = str.maketrans({"İ": "i", "I": "ı"})


def tr_lower(s):
    return s.translate(TRLOW).lower()


def korunan_araliklar(metin):
    """(bas, bit) listesi: kod blokları, satır-içi kod, URL'ler, aynen alıntıları."""
    ar = []
    for m in re.finditer(r"```.*?```", metin, re.S): ar.append(m.span())
    for m in re.finditer(r"`[^`\n]*`", metin): ar.append(m.span())
    for m in re.finditer(r"https?://\S+", metin): ar.append(m.span())
    for m in re.finditer(r"aynen:?\s*[\"“][^\"”]*[\"”]", metin): ar.append(m.span())
    # script-ayrıştırılan makine desenleri (pano-akis.py · sicak-katman-fifo.py): pano bölüm başlıkları + kart kapanış satırı
    for m in re.finditer(r"^## (AKTİF|BEKLEYEN|BLOKE)\s*$", metin, re.M): ar.append(m.span())
    for m in re.finditer(r"\*\*K-\d+\s+KAPANDI\s+\(", metin): ar.append(m.span())
    return ar


def yaml_satirlari(metin):
    if not metin.startswith("---\n"):
        return set()
    bit = metin.find("\n---", 4)
    if bit < 0:
        return set()
    return set(range(0, metin[:bit].count("\n") + 2))


OZEL = {"SALİH": "Salih", "TÜRKÇE": "Türkçe", "İNGİLİZCE": "İngilizce", "FİNDER": "Finder", "GİTHUB": "GitHub", "ANTHROPİC": "Anthropic",
        "OBSİDİAN": "Obsidian", "COWORK": "Cowork", "KUN": "Kun", "CHEN": "Chen", "PORTRİSK": "PortRisk", "WİNDOWS": "Windows", "DOCKER": "Docker"}


EN = set("""INDEX MEDIUM UNIQUE REGISTER LIKE AUTOMATIC JOIN FIRST DESCRIPTION IDK ORIGIN LIMIT INLINE IMPORT INPUT OUTPUT INSERT UPDATE
DELETE SELECT WHERE DISTINCT PRIMARY STRING INTEGER NULL TRUE FALSE PARTITION FILTER SPLIT HIGH LOW WIP LINK LIST LINE PIPELINE
SKILL SKILLS BUILD SHIP SCOUT SYNTHESIS REVIEW VERIFY COMMIT PUSH PULL MERGE BRANCH MAIN DIFF PATCH WORKTREE HOOK HOOKS SETTINGS
ENGINEERING MINING DRIFT RIPPLE EDIT EDITS WRITE READ LOSSLESS LOSSY ENCODING CODEC PRIORITY SURVIVORSHIP RESTRICT CASCADE
NOTIFICATION ISSUE ISSUES ARTIFACT CONTEXT WINDOW PROMPT PROMPTS SYSTEM ASSISTANT USER TOOL TOOLS AGENT AGENTS TRIGGER
WORKFLOW GUARDRAIL GUARDRAILS SANDBOX PERMISSION MEMORY THINKING FIRST-CLASS FAIL LOUD INDEXED IMC RUNTIME POINTER ESI
MISLEADING SUPERSEDED LICENSE DEFAULT PUBLIC PRIVATE ACTIVE DIRTY CLEAN""".split())


def sozcuk_cevir(w):
    """Tek caps sözcük (kesme eki / tire bileşiği dahil) → küçük/özel-ad biçimi; İngilizce sözcükte I→i, Türkçede I→ı."""
    kok, _, ek = w.partition("'")
    if kok in OZEL:
        return OZEL[kok] + (("'" + tr_lower(ek)) if ek else "")
    parcalar = []
    for p in kok.split("-"):
        parcalar.append(p.lower() if (p in EN and not re.search(r"[ÇĞİÖŞÜ]", p)) else tr_lower(p))
    return "-".join(parcalar) + (("'" + tr_lower(ek)) if ek else "")


def donustur(metin, say):
    ar = korunan_araliklar(metin); yaml = yaml_satirlari(metin)
    satir_bas = [0] + [m.end() for m in re.finditer(r"\n", metin)]
    def satir_no(pos):
        import bisect
        return bisect.bisect_right(satir_bas, pos) - 1
    def korunur(a, b):
        return any(x <= a and b <= y for x, y in ar)
    out = []; i = 0
    # ardışık caps sözcükleri (tek boşlukla ayrılmış; kesme eki dahil) grupla — ≥3 harf (Salih 09-15: "VAR", "SANA" da şikâyet)
    # tire bileşiği (ZAMAN-KAYMASI) tek sözcük; sonda nokta yalnız dosya-uzantısı ise (README.md) dışlanır, cümle sonu noktası değil
    W = r"[A-ZÇĞİÖŞÜ]{3,}(?:-[A-ZÇĞİÖŞÜ]{2,})*(?:'[A-ZÇĞİÖŞÜ]{1,4})?"
    tok = re.compile(r"(?<![\w./\-*_'])" + W + r"(?:[ ]" + W + r")*(?!\w|[/\-_']|\.\w)")
    for m in tok.finditer(metin):
        a, b = m.span()
        if korunur(a, b):
            continue
        kelimeler = m.group(0).split(" ")
        sb = metin.rfind("\n", 0, a) + 1; satir = metin[sb:metin.find("\n", a) if metin.find("\n", a) >= 0 else len(metin)]
        kalin_ic = metin[sb:a].count("**") % 2 == 1          # açık bir **…** span'ının içindeyiz → iç içe ** yok
        baslik = satir.lstrip().startswith("#")
        duz = kalin_ic or baslik or (satir_no(a) in yaml)     # kalın işareti konmayan bağlamlar
        parcalar = []; grup = []
        def grup_bos():
            nonlocal grup
            if grup:
                s = " ".join(sozcuk_cevir(w) for w in grup)
                if baslik and re.fullmatch(r"#+\s*(\d+\.\s*)?", metin[sb:a]):   # başlık başındaki sözcük → ilk harf büyük
                    s = s[:1].upper() + s[1:]
                parcalar.append(s if duz else f"**{s}**"); say["vurgu"] += len(grup); grup = []
        degisti = False
        for w in kelimeler:
            kok = w.split("'")[0]
            if kok in IZ:
                grup_bos(); parcalar.append(w)
            elif kok in DURUM and not baslik:
                grup_bos(); parcalar.append(f"`{w}`"); say["durum"] += 1; degisti = True
            elif kok in DURUM and baslik:
                grup_bos(); s = tr_lower(w)
                if re.fullmatch(r"#+\s*(\d+\.\s*)?", metin[sb:a]): s = s[:1].upper() + s[1:]   # yalnız başlık başında büyük ilk harf
                parcalar.append(s); say["durum"] += 1; degisti = True
            else:
                grup.append(w); degisti = True
        grup_bos()
        if not degisti:
            continue
        yeni = " ".join(parcalar)
        # "**a** **b**" → tek span değil; ardışık vurgu zaten tek grupta; durum+vurgu karışımı ayrı kalır
        out.append(metin[i:a]); out.append(yeni); i = b
    out.append(metin[i:])
    return "".join(out)


def dosyalar(repo, katman):
    H = pathlib.Path.home()
    sicak = [repo / "CLAUDE.md", H / ".claude" / "CLAUDE.md"] + sorted((repo / "core").glob("*.md")) + sorted((repo / ".claude" / "skills").glob("*/SKILL.md")) \
        + sorted((repo / ".claude" / "rules").glob("*.md")) + sorted(pathlib.Path(harness_anahtar.memory_dizin()).glob("*.md"))  # makineye göre anahtar (2026-09-22)
    ilik = [repo / "KILAVUZ.md", repo / ".claude" / "skills" / "README.md"] + sorted((repo / "wiki").glob("*.md")) + sorted((repo / ".claude" / "skills").glob("*/references/*.md")) \
        + sorted((repo / ".claude" / "skills").glob("*/*.md"))
    # 09-17 (Salih "büyük harf sorunu sürüyor" analizi): öğrenme yan oturumu bu dosyaları her açılışta okur (ogren §0.2) —
    # kanon temiz ama bunlar kirli kalınca model oradaki üslubu taklit etti. Ders dosyaları tarihçe değil canlı bağlamdır.
    ogrenme = [repo / "ogrenme" / "README.md", repo / "ogrenme" / "mufredat.md"] + sorted((repo / "ogrenme").glob("*/README.md")) \
        + sorted((repo / "ogrenme").glob("*/ilerleme.md")) + sorted((repo / "ogrenme").glob("*/dersler/*.md")) \
        + sorted((repo / "ogrenme").glob("*/*-eval-seti/*.md")) + sorted((repo / "ogrenme").glob("*/*-seti/*.md"))
    sec = {"sicak": sicak, "ilik": ilik, "ogrenme": ogrenme, "hepsi": sicak + ilik + ogrenme}[katman]
    gor = set(); res = []
    for p in sec:
        if p.exists() and p.name != "SKILL.md" or (p.exists() and p.name == "SKILL.md"):
            if p.resolve() not in gor:
                gor.add(p.resolve()); res.append(p)
    return [p for p in res if p.exists()]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=str(pathlib.Path.home() / "sistem" / "jarvis")); ap.add_argument("--katman", default="sicak", choices=["sicak", "ilik", "ogrenme", "hepsi"])
    ap.add_argument("--kuru", action="store_true"); ap.add_argument("--uygula", action="store_true"); ap.add_argument("--diff", default="")
    ap.add_argument("--goster", type=int, default=6); ap.add_argument("--json", action="store_true")
    a = ap.parse_args(); repo = pathlib.Path(a.repo).expanduser().resolve()
    if a.uygula == a.kuru:
        print("--kuru ya da --uygula (tam biri)", file=sys.stderr); sys.exit(2)
    toplam = collections.Counter(); rapor = []; diff_parcalari = []
    for p in dosyalar(repo, a.katman):
        try:
            eski = p.read_text(encoding="utf-8")
        except Exception:
            continue
        say = collections.Counter(); yeni = donustur(eski, say)
        if yeni == eski:
            continue
        rel = str(p).replace(str(pathlib.Path.home()), "~")
        rapor.append({"dosya": rel, "vurgu": say["vurgu"], "durum": say["durum"]}); toplam.update(say)
        d = list(difflib.unified_diff(eski.splitlines(keepends=True), yeni.splitlines(keepends=True), fromfile=rel, tofile=rel, n=0))
        diff_parcalari.append("".join(d))
        if a.uygula:
            p.write_text(yeni, encoding="utf-8")
    diff_metin = "".join(diff_parcalari)
    if a.diff:
        dp = pathlib.Path(a.diff); dp.parent.mkdir(parents=True, exist_ok=True); dp.write_text(diff_metin, encoding="utf-8")
    if a.json:
        print(json.dumps({"katman": a.katman, "mod": "uygula" if a.uygula else "kuru", "dosya": len(rapor), "vurgu": toplam["vurgu"], "durum": toplam["durum"], "dosyalar": rapor, "diff": a.diff}, ensure_ascii=False)); return
    print(f"BÜYÜK-HARF TEMİZLİK · {a.katman} · {'UYGULANDI' if a.uygula else 'kuru'} · dosya {len(rapor)} · vurgu→kalın {toplam['vurgu']} · durum→`jeton` {toplam['durum']}" + (f" · diff {a.diff}" if a.diff else ""))
    for r in sorted(rapor, key=lambda x: -(x["vurgu"] + x["durum"]))[:40]:
        print(f"  {r['vurgu'] + r['durum']:4}  (vurgu {r['vurgu']}, durum {r['durum']})  {r['dosya']}")
    if len(rapor) > 40:
        print(f"  … +{len(rapor) - 40} dosya")
    ornek = [l for l in diff_metin.splitlines() if l.startswith(("-", "+")) and not l.startswith(("---", "+++"))][: 2 * a.goster]
    if ornek:
        print("  örnek satırlar:"); [print("   ", l[:160]) for l in ornek]


if __name__ == "__main__":
    main()
