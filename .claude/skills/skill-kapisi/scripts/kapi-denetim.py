#!/usr/bin/env python3
"""kapi-denetim.py — Skill-üretim kapı-ağacının DETERMİNİSTİK kapıları (K2-R referans-varlığı · K3-F1..F4 biçim · tür-özel bayraklar).
Kural kaynağı: core/skill-uretim-semasi.md (v1, 2026-08-15). LLM'e bırakılan kapılar (K0/K1/K2-İ/K3-F5/şekil-FIRST) burada YOK — script yalnız
"yapısal dış sinyal"i üretir (C-YT3: kapı prompt'la kurulmaz). Kullanım:
    python3 kapi-denetim.py <skill-dizini|SKILL.md> [--json] [--repo <kök>]
Çıkış kodu: 0 = tüm SERT kapılar geçti · 1 = en az bir sert kapı düştü · 2 = kullanım hatası. Uyarılar (K) çıkış kodunu etkilemez.
"""
import sys, os, re, json, glob

def load(p):
    with open(p, encoding='utf-8') as f: return f.read()

def frontmatter(text):
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', text, re.S)
    if not m: return {}, text, False
    fm = {}
    cur = None
    for line in m.group(1).splitlines():
        km = re.match(r'^([A-Za-z_-]+):\s*(.*)$', line)
        if km:
            cur = km.group(1); fm[cur] = km.group(2).strip()
        elif cur and (line.startswith(' ') or line.startswith('\t')):
            fm[cur] = (fm[cur] + ' ' + line.strip()).strip()
    return fm, m.group(2), True

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    as_json = '--json' in sys.argv
    repo = None
    if '--repo' in sys.argv:
        repo = sys.argv[sys.argv.index('--repo') + 1]
    if not args:
        print(__doc__); sys.exit(2)
    target = args[0]
    skill_md = target if target.endswith('SKILL.md') else os.path.join(target, 'SKILL.md')
    if not os.path.isfile(skill_md):
        print(f"HATA: {skill_md} yok"); sys.exit(2)
    skill_dir = os.path.dirname(os.path.abspath(skill_md))
    skill_name = os.path.basename(skill_dir)
    if not repo:
        # .claude/skills/<n>/ → repo kökü iki üst
        cand = os.path.abspath(os.path.join(skill_dir, '..', '..', '..'))
        repo = cand if os.path.isdir(os.path.join(cand, '.claude')) else os.getcwd()

    text = load(skill_md)
    fm, body, has_fm = frontmatter(text)
    lines = text.splitlines()
    R = {'skill': skill_name, 'gates': [], 'warns': [], 'facets': {}}
    def gate(gid, ok, msg, hard=True):
        R['gates'].append({'id': gid, 'ok': bool(ok), 'hard': hard, 'msg': msg})
    def warn(msg): R['warns'].append(msg)

    # ---------- K3-F1 description ----------
    desc = fm.get('description', '')
    n = len(desc)
    gate('F1a-len', 0 < n <= 1024, f"description {n} char (≤1024; platform kesme 1536)")
    neg = bool(re.search(r'KULLANILMAZ|KULLANMA|kullanma[:;]|KULLANMAZ|Use when.*(?:not|don\'t)|DO NOT', desc))
    gate('F1b-negatif-tetik', neg, "negatif tetik (KULLANILMAZ/KULLANMA) " + ("var" if neg else "YOK"))
    third = not re.search(r'\b(ben|beni|bana|I can|I will|I help)\b', desc)
    gate('F1c-3.sahis', third, "3. şahıs " + ("✓" if third else "✗ (1. şahıs ifade)"))
    ne_zaman = bool(re.search(r'Tetik|tetik|dendiğinde|dediğinde|Kullan[: ]|Use when|ne zaman|WHEN', desc))
    gate('F1d-ne-zaman', ne_zaman, "NE-ZAMAN (tetik tarifi) " + ("var" if ne_zaman else "YOK"), hard=False)
    # hazine toplam bütçesi
    tot = 0; cnt = 0
    for f in glob.glob(os.path.join(repo, '.claude', 'skills', '*', 'SKILL.md')):
        fm2, _, _ = frontmatter(load(f)); tot += len(fm2.get('description', '')); cnt += 1
    budget_chars = 7380  # 0,9 × (%1 × 200k token = 2.000 token) × 4,1 char/token — çevrim ÖLÇÜLDÜ (Salih /context 2026-08-20: 15 yüklü skill 7.837 char ≈ 1,9k token; KB-19 Karar 33). 200k = en küçük pencereli koşucu (alt-model skill koşucuları, KB-03); pencere/politika değişimi Katman-1.
    R['facets']['hazine_desc_toplam'] = tot; R['facets']['hazine_skill_sayisi'] = cnt
    if tot > budget_chars:
        warn(f"F1e-hazine-bütçesi: {cnt} skill description toplamı {tot} char > {budget_chars} — platform en az çağrılanın description'ını sessizce düşürebilir; /context ile ölç ∨ kısalt")
    else:
        gate('F1e-hazine-butcesi', True, f"hazine {cnt} skill / {tot} char ≤ {budget_chars}", hard=False)

    # ---------- K3-F2 gövde ----------
    nl = len(lines)
    gate('F2a-satir', nl < 500, f"gövde {nl} satır (<500)")
    refdir = os.path.join(skill_dir, 'references')
    deep = []
    if os.path.isdir(refdir):
        for root, dirs, files in os.walk(refdir):
            if os.path.relpath(root, refdir).count(os.sep) >= 1: deep.append(root)
    gate('F2b-referans-derinlik', not deep, "references ≤1 seviye" if not deep else f"iç içe referans: {deep[:2]}")

    # ---------- K3-F3 evals ----------
    ev = os.path.join(skill_dir, 'evals', 'evals.json')
    if os.path.isfile(ev):
        try:
            E = json.loads(load(ev))
            tests = E.get('tests', E.get('cases', []))          # iki format: tests (07-21+) · cases (07-19 ritüel)
            de = E.get('description_eval', {})
            st = de.get('should_trigger', []) or [c for c in E.get('cases', []) if c.get('type') == 'pozitif']
            snt = de.get('should_not_trigger', []) or [c for c in E.get('cases', []) if c.get('type') == 'negatif']
            gate('F3a-eval-sayisi', len(tests) >= 3, f"evals: {len(tests)} test (≥3)")
            gate('F3b-description-eval', len(st) >= 5 and len(snt) >= 5, f"should_trigger {len(st)} / should_not {len(snt)} (≥5+5)")
        except Exception as e:
            gate('F3a-eval-sayisi', False, f"evals.json okunamadı: {e}")
    else:
        gate('F3a-eval-sayisi', False, "evals/evals.json YOK (eval-önce, K-016)")

    # ---------- K3-F4 adımlar + gotchas ----------
    steps = len(re.findall(r'^\s*\d+\.\s', body, re.M))
    bullets = len(re.findall(r'^\s*[-*]\s', body, re.M))
    gate('F4a-numarali-adim', steps >= 3 or bullets >= 5, f"numaralı adım {steps} (≥3) ∨ checklist maddesi {bullets} (≥5)")
    got = bool(re.search(r'^#+\s*(Gotchas|Tuzaklar|Frenler|Dikkat)', body, re.M | re.I))
    gate('F4b-gotchas', got, "Gotchas bölümü " + ("var" if got else "YOK"))

    # ---------- K2-R referans-varlığı ----------
    missing = []; checked = 0
    # dosya yolları (şablon/joker içerenler atlanır)
    for m in re.finditer(r'`([^`\s]+?\.(?:md|py|sh|json|yaml|yml|d2|txt|svg))`', text):
        p = m.group(1)
        if re.search(r'YYYY|MM-DD|<|>|\*|\{|N\.md|-N\b|\.\.\.', p): continue
        if p.startswith('~') or p.startswith('/') or p.startswith('C:'): continue
        cands = [os.path.join(repo, p), os.path.join(skill_dir, p)]
        checked += 1
        if not any(os.path.exists(c) for c in cands): missing.append(p)
    # tüzük maddeleri m.NN
    tuz = os.path.join(repo, 'core', 'tuzuk-v0.md')
    if os.path.isfile(tuz):
        arts = set(re.findall(r'^(\d+)\.\s+\*\*', load(tuz), re.M))
        for a in set(re.findall(r'\bm\.(\d+)[a-z]?\b', text)):
            checked += 1
            if a not in arts: missing.append(f"m.{a} (tüzükte madde yok)")
    # skill adları: backtick içindeki tire-li kelime, hazine'de yoksa UYARI (sert değil — çünkü her tire-li kelime skill değil)
    skills = {os.path.basename(os.path.dirname(f)) for f in glob.glob(os.path.join(repo, '.claude', 'skills', '*', 'SKILL.md'))}
    for tok in set(re.findall(r'`([a-z]+(?:-[a-z]+)+)`', text)):
        if tok in skills or tok == skill_name: continue
        if re.search(r'-(kosum|kapisi|modeli|hatti|derleme|kaydet|ceviri|vardiya|kapanis|yaz|grill|acilis)$', tok):
            warn(f"K2-R? `{tok}` skill adı gibi ama hazinede yok (referans mı, aday mı?)")
    gate('R-referans-varligi', not missing, f"{checked} referans denetlendi; eksik: {missing if missing else 'yok'}")

    # ---------- şekil tahmini (FIRST: R > O > Y > Ü) + tür-özel bayraklar ----------
    d_all = (desc + ' ' + body)
    # şekil tahmini DESCRIPTION'dan (skill adları çıkarılarak — "vardiya-kapanis kendi yazar" gibi atıflar ritüel sayılmasın)
    d_pos = re.split(r'KULLANILMAZ|KULLANMA[:;]|KULLANMAZ', desc)[0]   # yalnız pozitif tetik kısmı (negatif-tetik cümlesi şekil belirlemez)
    d_shape = re.sub(r'[a-z]+(?:-[a-z]+)+', ' ', d_pos)
    isR = bool(re.search(r'ritüel|oturum[- ]?sınır|seans başı|seans bitimi|vardiya[- ]?(?:AÇILIŞ|KAPANIŞ|açılış|kapanış)|SessionStart|Stop hook|kadans', d_shape, re.I))
    isO = bool(re.search(r'pipeline|orkestrat|alt-ajan|çocuk skill|zincir(?:le|i)|paralel araştırma|Workflow|uçtan uca', d_shape, re.I))
    # yan-etki: FİİLEN yapan ifadeler (yazar/atar/eder); "yazmaz/yapmaz/atmaz" hariç; örnek/alıntı içindeki "commit" sözcüğü sayılmaz
    yan_pos = re.search(r"commit atar|ayrı commit|commit'ler|commit eder|commit \+ push|git push|push'lar|publish|paylaş(?:ır|ım)|deftere .{0,15}yazar|kanon.{0,25}yazar|kapsül.{0,15}(?:tazele|günceller|yazar)|dosyaya yazar", d_all, re.I)
    yan_neg = re.search(r'commit yapmaz|commit atmaz|kanon yazmaz|yan-etki freni|dosya YAZMAZ|kaydetme/commit yapmaz', d_all)
    yan = bool(yan_pos) and not (yan_neg and not re.search(r'commit atar|ayrı commit|git push|commit \+ push', d_all))
    isY = yan
    shape = 'T-R' if isR else 'T-O' if isO else 'T-Y' if isY else 'T-Ü'
    R['facets']['sekil_tahmini'] = shape
    R['facets']['yan_etki_faseti'] = yan
    R['facets']['disable_model_invocation'] = fm.get('disable-model-invocation', 'false')
    R['facets']['context'] = fm.get('context', 'ana')
    R['facets']['user_invocable'] = fm.get('user-invocable', 'true')
    if shape == 'T-Y':
        gate('TY-disable-model-invocation', fm.get('disable-model-invocation', '').lower() == 'true', "yan-etkili birincil şekil → disable-model-invocation:true " + ("✓" if fm.get('disable-model-invocation','').lower()=='true' else "EKSİK"))
        gate('TY-m31', bool(re.search(r'm\.31|Katman[- ]1|onay', d_all)), "m.31 kapısı/onay atfı " + ("var" if re.search(r'm\.31|Katman[- ]1|onay', d_all) else "YOK"), hard=False)
    if shape in ('T-R', 'T-O') and yan:
        okb = bool(re.search(r'Salih|beyan|m\.31|onay', d_all))
        gate('TRO-yan-etki-beyan', okb, "yan-etki adımı Salih-beyanına/m.31'e bağlı " + ("✓" if okb else "YOK"))
    if shape == 'T-O':
        okp = bool(re.search(r'paralellik|bağımsız .{0,20}mi|ortak (?:çıktı|üretim)', d_all, re.I))
        gate('TO-paralellik-uygunluk', okp, "paralellik-uygunluk sorusu " + ("var" if okp else "YOK"), hard=False)
    if shape == 'T-R':
        okz = bool(re.search(r'zaman-?kayması|zaman yalnız sistem|selamlama .{0,30}zaman', d_all, re.I))
        gate('TR-zaman-freni', okz, "zaman-kayması freni " + ("var" if okz else "YOK"), hard=False)
    if shape == 'T-Ü':
        okc = bool(re.search(r'commit yapmaz|commit atmaz|yan-etki freni|kaydetme/commit yapmaz|karar ALMA', d_all))
        gate('TU-commit-yapmaz', okc, "\"commit yapmaz / yan-etki freni\" beyanı " + ("var" if okc else "YOK"), hard=False)

    hard_fail = [g for g in R['gates'] if g['hard'] and not g['ok']]
    R['sonuc'] = 'GEÇTİ' if not hard_fail else 'DÜŞTÜ'
    R['dusen_sert_kapilar'] = [g['id'] for g in hard_fail]
    if as_json:
        print(json.dumps(R, ensure_ascii=False, indent=1))
    else:
        print(f"== {skill_name} — {R['sonuc']} (şekil-tahmini {shape}; yan-etki {'var' if yan else 'yok'})")
        for g in R['gates']:
            print(f"  [{'✓' if g['ok'] else ('✗' if g['hard'] else '△')}] {g['id']}: {g['msg']}")
        for w in R['warns']: print(f"  [K] {w}")
    sys.exit(0 if not hard_fail else 1)

if __name__ == '__main__':
    main()
