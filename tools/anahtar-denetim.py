#!/usr/bin/env python3
"""anahtar-denetim.py — Bağlam Anahtar Kaydı v1 (core/baglam-anahtar-kaydi.md §2) DETERMİNİSTİK denetimi.

Emekli değerlerin (ve varyantlarının) git-izlenen markdown dosyalarındaki KALINTI referanslarını katman bazında sayar
(sıcak = ihlal, ılık = uyarı, soğuk = tarihçe), izinli tarihçe-kalıplarını ayırır, kayıt bütünlüğünü denetler
(damgasız/halefsiz/çevrimli/çift-güncel). LLM yok; yalnız sayım — anlamsal yargı Salih triyajına.
Kullanım: python3 tools/anahtar-denetim.py [--repo <kök>] [--kayit core/baglam-anahtar-kaydi.md] [--anahtar <id>]
          [--goster N] [--json] [--ilik-uyari k1] [--ilik-eylem k2]
Çıkış: 0 temiz · 1 sıcak ihlal ∨ bütünlük hatası (FAIL-LOUD) · 2 kullanım hatası.
"""
import sys, os, re, json, subprocess, unicodedata

TR = str.maketrans({'ı':'i','İ':'i','ğ':'g','Ğ':'g','ü':'u','Ü':'u','ş':'s','Ş':'s','ö':'o','Ö':'o','ç':'c','Ç':'c'})

def norm(s):
    return unicodedata.normalize('NFC', s).translate(TR).lower()

def katman(yol):
    if yol == 'CLAUDE.md' or yol.startswith('core/') or (yol.startswith('.claude/skills/') and yol.endswith('/SKILL.md')):
        return 'sicak'
    if yol.startswith(('raporlar/', 'cc/rapor-', 'cc/gorev-', 'ogrenme/')) or yol.startswith('model de'):
        return 'soguk'
    if yol.startswith(('kuyruk/arsiv', 'kuyruk/gelen-')):
        return 'soguk'
    # kök snapshot/tarihçe dosyaları (bayat kapsüller, ilk-deneme talimatı, seçim turu) = tarihçe
    if re.match(r'^(CEP-KAPSULU-|CHAT-KAPSULU-|secim-turu-|PARALEL-VARDIYA-ILK-DENEME)', yol):
        return 'soguk'
    return 'ilik'

def git_md(repo):
    try:
        out = subprocess.run(['git', '-c', 'core.quotepath=off', 'ls-files', '-z'], cwd=repo, capture_output=True, check=True).stdout
    except Exception as e:
        print(f"FAIL-LOUD: git ls-files başarısız ({e})"); sys.exit(2)
    return [p for p in out.decode('utf-8', 'replace').split('\0') if p.endswith('.md')]

def load_registry(path):
    text = open(path, encoding='utf-8').read()
    m = re.search(r'```json\s*\n(.*?)\n```', text, re.S)
    if not m:
        print("FAIL-LOUD: kayıtta ```json bloğu yok"); sys.exit(2)
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError as e:
        print(f"FAIL-LOUD: kayıt JSON hatası: {e}"); sys.exit(2)

def integrity(reg):
    errs = []
    guncel_map = {}
    ids = set()
    for a in reg.get('anahtarlar', []):
        aid = a.get('anahtar_id')
        if not aid: errs.append("anahtar_id boş"); continue
        if aid in ids: errs.append(f"{aid}: çift anahtar_id")
        ids.add(aid)
        g = a.get('guncel') or {}
        if not g.get('deger'): errs.append(f"{aid}: guncel.deger boş")
        if not g.get('gecerli_bas'): errs.append(f"{aid}: damgasız güncel (gecerli_bas yok)")
        gv = norm(g.get('deger', ''))
        if gv:
            if gv in guncel_map and guncel_map[gv] != aid:
                errs.append(f"{aid}: tekillik tip-b — aynı güncel değer '{g['deger']}' {guncel_map[gv]} anahtarında da")
            guncel_map[gv] = aid
        for e in a.get('emekli', []):
            if not e.get('deger'): errs.append(f"{aid}: emekli.deger boş")
            if not e.get('tarih'): errs.append(f"{aid}: damgasız emekli '{e.get('deger')}'")
            rb = e.get('replaced_by')
            if not rb or isinstance(rb, list): errs.append(f"{aid}: halefsiz/çoklu replaced_by '{e.get('deger')}'")
            elif norm(rb) == norm(e.get('deger', '')): errs.append(f"{aid}: çevrim — replaced_by kendisi '{rb}'")
            elif norm(rb) != gv: errs.append(f"{aid}: replaced_by '{rb}' ≠ güncel '{g.get('deger')}' (zincir derinliği >1?)")
            if norm(e.get('deger', '')) == gv: errs.append(f"{aid}: emekli değer güncel değerle aynı")
    return errs

def compile_patterns(vals):
    pats = []
    for v in vals:
        v = norm(v).strip()
        if not v: continue
        # kelime sınırı: baş/son alfanümerik değilse gevşek
        pats.append(re.compile(r'(?<![\w-])' + re.escape(v) + r'(?![\w])', re.I))
    return pats

def main():
    argv = sys.argv[1:]
    def opt(name, default=None):
        if name in argv:
            i = argv.index(name); return argv[i+1] if i+1 < len(argv) else default
        return default
    repo = os.path.abspath(opt('--repo', os.getcwd()))
    kayit = opt('--kayit', 'core/baglam-anahtar-kaydi.md')
    filt = opt('--anahtar')
    goster = int(opt('--goster', 12))
    k1 = int(opt('--ilik-uyari', 1)); k2 = int(opt('--ilik-eylem', 10))
    as_json = '--json' in argv
    kayit_path = os.path.join(repo, kayit)
    reg = load_registry(kayit_path)
    errs = integrity(reg)
    files = git_md(repo)
    texts = {}
    for f in files:
        try:
            with open(os.path.join(repo, f), encoding='utf-8') as fh: texts[f] = fh.read().split('\n')
        except Exception:
            texts[f] = None
    report = {'kayit': kayit, 'butunluk_hatalari': errs, 'anahtarlar': [], 'sonuc': 'TEMİZ'}
    hot_viol_total = 0
    for a in reg.get('anahtarlar', []):
        aid = a['anahtar_id']
        if filt and aid != filt: continue
        entry = {'anahtar_id': aid, 'tur': a.get('tur'), 'guncel': (a.get('guncel') or {}).get('deger'), 'emekli': [], 'aday': []}
        for kind in ('emekli', 'aday'):
            for e in a.get(kind, []):
                vals = [e.get('deger', '')] + list(e.get('varyantlar', []))
                pats = compile_patterns(vals)
                allow = [re.compile(norm(p), re.I) for p in e.get('izinli_kaliplar', [])]
                cnt = {'sicak': {'ihlal': 0, 'izinli': 0}, 'ilik': {'ihlal': 0, 'izinli': 0}, 'soguk': {'ihlal': 0, 'izinli': 0}}
                hits = []
                for f, lines in texts.items():
                    if lines is None or f == kayit: continue
                    kat = katman(f)
                    for ln, line in enumerate(lines, 1):
                        nl = norm(line)
                        n = sum(len(p.findall(nl)) for p in pats)
                        if not n: continue
                        izinli = any(al.search(nl) for al in allow)
                        cnt[kat]['izinli' if izinli else 'ihlal'] += n
                        if not izinli and kat != 'soguk':
                            hits.append({'dosya': f, 'satir': ln, 'katman': kat, 'n': n, 'metin': line.strip()[:140]})
                dosya_sayisi = len({h['dosya'] for h in hits})
                item = {'deger': e.get('deger'), 'replaced_by': e.get('replaced_by'), 'tarih': e.get('tarih'), 'sayim': cnt,
                        'sicak_ihlal_dosya': sorted({h['dosya'] for h in hits if h['katman'] == 'sicak'}),
                        'ilik_ihlal_dosya': sorted({h['dosya'] for h in hits if h['katman'] == 'ilik'}),
                        'ornek': hits[:goster]}
                if kind == 'emekli':
                    hot_viol_total += cnt['sicak']['ihlal']
                    il = cnt['ilik']['ihlal']
                    item['ilik_hukum'] = 'EYLEM' if il >= k2 else ('UYARI' if il >= k1 else 'temiz')
                entry[kind].append(item)
        report['anahtarlar'].append(entry)
    if hot_viol_total or errs:
        report['sonuc'] = 'İHLAL'
    if as_json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
    else:
        print(f"=== anahtar-denetim — kayıt {kayit} — {len(files)} md dosya")
        if errs:
            print("BÜTÜNLÜK HATALARI:"); [print("  - " + x) for x in errs]
        for e in report['anahtarlar']:
            print(f"\n## {e['anahtar_id']} [{e['tur']}] güncel='{e['guncel']}'")
            for kind, label in (('emekli', 'EMEKLİ'), ('aday', 'ADAY (sayılır, ihlal üretmez)')):
                for it in e[kind]:
                    c = it['sayim']
                    print(f"  {label}: '{it['deger']}' → '{it['replaced_by']}' ({it.get('tarih') or 'tarihsiz'})")
                    print(f"    sıcak: ihlal {c['sicak']['ihlal']} / izinli {c['sicak']['izinli']} · ılık: ihlal {c['ilik']['ihlal']} / izinli {c['ilik']['izinli']}"
                          + (f" [{it.get('ilik_hukum')}]" if kind == 'emekli' else '') + f" · soğuk(tarihçe): {c['soguk']['ihlal'] + c['soguk']['izinli']}")
                    if it['sicak_ihlal_dosya']: print(f"    sıcak ihlal dosyaları: {', '.join(it['sicak_ihlal_dosya'])}")
                    if it['ilik_ihlal_dosya']: print(f"    ılık ihlal dosyaları: {', '.join(it['ilik_ihlal_dosya'])}")
                    for h in it['ornek']:
                        print(f"      - {h['dosya']}:{h['satir']} [{h['katman']}] {h['metin']}")
        print(f"\n=== SONUÇ: {report['sonuc']} (sıcak ihlal toplam {hot_viol_total}; bütünlük hatası {len(errs)})")
    sys.exit(1 if report['sonuc'] == 'İHLAL' else 0)

if __name__ == '__main__':
    main()
