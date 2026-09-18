#!/usr/bin/env python3
"""tetik-denetim.py — Skill-TETİKLENME şemasının (core/skill-tetikleme-semasi.md v1) DETERMİNİSTİK Kapı-Ö denetimi.
Bir görev emri/raporu dosyasındaki "## SKILL TETİKLERİ" bloğunu okur; her çağrı için: (1) skill hazinede VAR mı, (2) 9 alan dolu mu,
(3) yan-etkili (disable-model-invocation:true) skill → cagri_kipi literal ∧ alt-ajandan çağrılmıyor mu, (4) tetik_kosulu'nda derece ifadesi
("gerekirse/uygunsa/mümkünse") var mı, iç içe koşul derinliği ≤2 mi, (5) hata_yolu retry ≤3 + FAIL-LOUD mu, (6) done_yuklemi derece değil mi.
Kullanım: python3 tetik-denetim.py <emir.md> [--repo <kök>] [--json]   Çıkış: 0 geçti · 1 sert kapı düştü · 2 kullanım hatası · 3 blok yok.
LLM'e kalan: koşulun ANLAMI (K2), bağlam yeterliliği, sıra/handoff kalitesi — script yalnız yapısal sinyal üretir.
"""
import sys, os, re, json, glob

FIELDS = ['skill','tetik_kosulu','cagri_kipi','girdi','baglam','yan_etki_damgasi','done_yuklemi','hata_yolu','sira','kayit']

def frontmatter(text):
    m = re.match(r'^---\n(.*?)\n---', text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            km = re.match(r'^([A-Za-z_-]+):\s*(.*)$', line)
            if km: fm[km.group(1)] = km.group(2).strip()
    return fm

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    as_json = '--json' in sys.argv
    repo = sys.argv[sys.argv.index('--repo')+1] if '--repo' in sys.argv else os.getcwd()
    if not args: print(__doc__); sys.exit(2)
    text = open(args[0], encoding='utf-8').read()
    m = re.search(r'^##\s*SKILL TETİKLERİ.*?$(.*?)(?=^##\s|\Z)', text, re.S | re.M)
    if not m:
        print("SKILL TETİKLERİ bloğu YOK (emirde skill çağrılmıyorsa 'yok' yazılmalı)"); sys.exit(3)
    block = m.group(1)
    if re.match(r'^\s*(-\s*)?yok\s*$', block.strip(), re.I):
        print("SKILL TETİKLERİ: yok — çağrı bloğu gerekmiyor"); sys.exit(0)
    # çağrıları böl: her "- skill:" ile başlayan parça
    parts = re.split(r'^\s*-\s*skill:\s*', block, flags=re.M)[1:]
    skills = {os.path.basename(os.path.dirname(f)): f for f in glob.glob(os.path.join(repo, '.claude', 'skills', '*', 'SKILL.md'))}
    R = {'calls': [], 'sonuc': 'GEÇTİ'}
    hard_fail = False
    for p in parts:
        lines = ('skill: ' + p).splitlines()
        f = {}
        for ln in lines:
            km = re.match(r'^\s*([a-z_]+):\s*(.*)$', ln)
            if km: f[km.group(1)] = km.group(2).strip()
        name = re.split(r'[\s#(]', f.get('skill','').strip('`'))[0]
        gates = []
        def gate(gid, ok, msg, hard=True):
            gates.append({'id': gid, 'ok': bool(ok), 'hard': hard, 'msg': msg})
        exists = name in skills
        gate('O1-var', exists, f"skill `{name}` hazinede " + ("VAR" if exists else "YOK — çağrı kurulamaz (K1)"))
        missing = [k for k in FIELDS if not f.get(k)]
        gate('O2-alanlar', not missing, "9 alan dolu" if not missing else f"eksik alan: {missing} — sözleşme tek seferde tam olmalı")
        kip = f.get('cagri_kipi','').lower()
        gate('O3-kip', kip.startswith(('literal','ortuk','örtük','yasak')), f"cagri_kipi={kip or '-'} (literal|ortuk|yasak)")
        yan_etkili = False; alt_ajan = bool(re.search(r'alt-ajan|subagent|fork|işçi', (f.get('baglam','')+' '+f.get('sira','')), re.I))
        if exists:
            fm = frontmatter(open(skills[name], encoding='utf-8').read())
            yan_etkili = fm.get('disable-model-invocation','').lower() == 'true'
        if yan_etkili:
            gate('O4-TY-literal', kip.startswith('literal'), "yan-etkili (T-Y) skill → cagri_kipi literal " + ("✓" if kip.startswith('literal') else "DEĞİL — YASAK"))
            gate('O4-TY-anasira', not alt_ajan, "T-Y skill alt-ajandan/işçiden çağrılmıyor " + ("✓" if not alt_ajan else "— YASAK (önyüklenemez)"))
        tk = f.get('tetik_kosulu','')
        derece = re.search(r'gerekirse|uygunsa|mümkünse|icap ederse|isteğe bağlı|if needed|when appropriate', tk, re.I)
        gate('O5-derece-yok', not derece, "tetik_kosulu boolean " + ("✓" if not derece else f"✗ derece ifadesi: '{derece.group(0)}'"))
        depth = max([0]+[tk[:i].count('(')-tk[:i].count(')') for i in range(len(tk))]) if tk else 0
        nested = len(re.findall(r'\beğer\b|\bise\b|→', tk))
        gate('O5-icice', depth <= 2 and nested <= 3, f"iç içe koşul derinliği {depth} (≤2) · koşul-işareti {nested} (≤3)", hard=False)
        neg = bool(re.search(r'ÇAĞIRMA|çağırma|KULLANMA|yasak|¬', tk))
        gate('O5-negatif', neg, "negatif tetik yazılı " + ("✓" if neg else "— 'Z ise ÇAĞIRMA' eksik"), hard=False)
        hy = f.get('hata_yolu','')
        rm = re.search(r'retry\s*[≤<=]*\s*(\d+)', hy)
        gate('O6-retry', (rm is not None and int(rm.group(1)) <= 3), f"retry {'≤'+rm.group(1) if rm else 'YOK'} (≤3)")
        gate('O6-failloud', bool(re.search(r'FAIL-?LOUD|fail loud|sessiz düşüş yasak', hy, re.I)), "FAIL-LOUD " + ("✓" if re.search(r'FAIL-?LOUD|fail loud', hy, re.I) else "YOK"))
        dy = f.get('done_yuklemi','')
        gate('O7-done-boolean', not re.search(r'iyi bir|kaliteli|yeterince|mümkün olduğunca|başarılı olur', dy, re.I), "done_yuklemi boolean " + ("✓" if not re.search(r'iyi bir|kaliteli|yeterince', dy, re.I) else "✗ derece ifadesi"))
        yd = f.get('yan_etki_damgasi','').lower()
        gate('O8-damga', bool(re.search(r'salt-okur|eklemeli|yıkıcı', yd)), f"yan_etki_damgasi={yd or 'YOK → yıkıcı varsayılır'}", hard=False)
        hf = [g for g in gates if g['hard'] and not g['ok']]
        if hf: hard_fail = True
        R['calls'].append({'skill': name, 'gates': gates, 'sonuc': 'GEÇTİ' if not hf else 'BLOKE'})
    R['sonuc'] = 'GEÇTİ' if not hard_fail else 'BLOKE'
    if as_json: print(json.dumps(R, ensure_ascii=False, indent=1))
    else:
        for c in R['calls']:
            print(f"== çağrı `{c['skill']}` — {c['sonuc']}")
            for g in c['gates']: print(f"  [{'✓' if g['ok'] else ('✗' if g['hard'] else '△')}] {g['id']}: {g['msg']}")
        print(f"=== SONUÇ: {R['sonuc']} ({len(R['calls'])} çağrı)")
    sys.exit(0 if not hard_fail else 1)

if __name__ == '__main__':
    main()
