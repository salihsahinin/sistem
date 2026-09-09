#!/usr/bin/env python3
"""anahtar-denetim.py — Bağlam Anahtar Kaydı v1 (core/baglam-anahtar-kaydi.md §2) DETERMİNİSTİK denetimi.

Emekli değerlerin (ve varyantlarının) git-izlenen markdown dosyalarındaki KALINTI referanslarını katman bazında sayar
(sıcak = ihlal, ılık = uyarı, soğuk = tarihçe), izinli tarihçe-kalıplarını ayırır, kayıt bütünlüğünü denetler
(damgasız/halefsiz/çevrimli/çift-güncel). LLM yok; yalnız sayım — anlamsal yargı Salih triyajına.
Yazar: salt-okur (yalnız kayıt dosyası + git-izlenen .md dosyaları okunur; hiçbir dosyaya yazmaz).
Kullanım: python3 tools/anahtar-denetim.py [--repo <kök>] [--kayit core/baglam-anahtar-kaydi.md] [--anahtar <id>]
          [--goster N] [--ilik-uyari k1] [--ilik-eylem k2] [--json] [--sessiz]
Çıkış: 0 temiz · 1 sıcak ihlal ∨ bütünlük hatası (FAIL-LOUD) · 2 kullanım hatası.
"""
import sys, os, re, json, subprocess, unicodedata, argparse

TR = str.maketrans({'ı':'i','İ':'i','ğ':'g','Ğ':'g','ü':'u','Ü':'u','ş':'s','Ş':'s','ö':'o','Ö':'o','ç':'c','Ç':'c'})

def norm(s):
    return unicodedata.normalize('NFC', s).translate(TR).lower()

def _katman_yerel(yol):
    """ESKİ yerel tanım (08-15 → 08-29): yalnız baglam-tablo.py bulunamazsa yedek. Tek-tanım kuralı (İB-42 kalanı, 08-29): katman = silver
    `dosya.katman` üreticisi `baglam-tablo.katman_bul` — iki tanım ayrışınca T-Ç3 (silver-saglik) ile bu denetim farklı sayıyordu.
    Bilinen farklar (kayıt): kuyruk/gelen-* eski tanımda soğuk, silver'da ılık · kök CEP-/CHAT-KAPSULU-* eski tanımda soğuk, silver'da ılık.
    Ek sınıflar (08-29 yeni seans, test listesi): Clippings/ · tools/*.md · veri/sozlesme/*.md · cc/karar-onerisi-* · kök-dışı README.md · .claude-dışı SKILL.md — eski ılık, silver soğuk."""
    if yol == 'CLAUDE.md' or yol.startswith('core/') or (yol.startswith('.claude/skills/') and yol.endswith('/SKILL.md')):
        return 'sicak'
    if yol.startswith(('raporlar/', 'cc/rapor-', 'cc/gorev-', 'ogrenme/')) or yol.startswith('model de'):
        return 'soguk'
    if yol.startswith(('arsiv/', 'kuyruk/gelen-')):
        return 'soguk'
    if re.match(r'^(CEP-KAPSULU-|CHAT-KAPSULU-|secim-turu-|PARALEL-VARDIYA-ILK-DENEME)', yol):
        return 'soguk'
    return 'ilik'


def _katman_bul_yukle():
    try:
        import importlib.util
        yol = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'baglam-tablo.py')
        spec = importlib.util.spec_from_file_location('baglam_tablo', yol); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        return m.katman_bul
    except Exception:
        return None


_KATMAN_BUL = _katman_bul_yukle()


def katman(yol):
    """TEK TANIM: silver ile aynı (baglam-tablo.katman_bul); 'yapisal' bu denetimde geçmez (.md tarar). Yedek: eski yerel tanım + stderr uyarısı."""
    if _KATMAN_BUL is not None:
        k = _KATMAN_BUL(yol)
        return k if k in ('sicak', 'ilik', 'soguk') else 'soguk'
    print('UYARI: baglam-tablo.katman_bul yüklenemedi — eski yerel katman tanımı kullanılıyor (tek-tanım kuralı askıda)', file=sys.stderr)
    return _katman_yerel(yol)

def git_md(repo):
    try:
        out = subprocess.run(['git', '-c', 'core.quotepath=off', 'ls-files', '-z'], cwd=repo, capture_output=True, check=True).stdout
    except Exception as e:
        print(f"FAIL-LOUD: git ls-files başarısız ({e})", file=sys.stderr); sys.exit(2)
    return [p for p in out.decode('utf-8', 'replace').split('\0') if p.endswith('.md')]

def git_head(repo):
    try:
        return subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], cwd=repo, capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return '?'

def load_registry(path):
    try:
        text = open(path, encoding='utf-8').read()
    except OSError as e:
        print(f"FAIL-LOUD: kayıt dosyası okunamadı: {path} ({e})", file=sys.stderr); sys.exit(2)
    m = re.search(r'```json\s*\n(.*?)\n```', text, re.S)
    if not m:
        print("FAIL-LOUD: kayıtta ```json bloğu yok", file=sys.stderr); sys.exit(2)
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError as e:
        print(f"FAIL-LOUD: kayıt JSON hatası: {e}", file=sys.stderr); sys.exit(2)

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
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--repo', default=os.getcwd(), help='repo kökü (varsayılan: cwd)')
    ap.add_argument('--kayit', default='core/baglam-anahtar-kaydi.md', help='anahtar kaydı dosyası, repo-göreli (varsayılan core/baglam-anahtar-kaydi.md)')
    ap.add_argument('--anahtar', default=None, help='yalnız bu anahtar_id filtrelenir')
    ap.add_argument('--goster', type=int, default=12, help='anahtar başına örnek satır sayısı (varsayılan 12)')
    ap.add_argument('--ilik-uyari', type=int, default=1, help='ılık ihlal UYARI eşiği (varsayılan 1)')
    ap.add_argument('--ilik-eylem', type=int, default=10, help='ılık ihlal EYLEM eşiği (varsayılan 10)')
    ap.add_argument('--json', action='store_true', help="axi-standardı (İB-58): stdout = TEK makine-okur JSON nesnesi; insan satırları stderr'e")
    ap.add_argument('--sessiz', action='store_true', help='insan satırlarını basma')
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)
    kayit = a.kayit
    filt = a.anahtar
    goster = a.goster
    k1 = a.ilik_uyari; k2 = a.ilik_eylem
    insan = sys.stderr if a.json else sys.stdout  # axi: makine kanalı stdout, insan kanalı stderr
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
    for rec in reg.get('anahtarlar', []):
        aid = rec['anahtar_id']
        if filt and aid != filt: continue
        entry = {'anahtar_id': aid, 'tur': rec.get('tur'), 'guncel': (rec.get('guncel') or {}).get('deger'), 'emekli': [], 'aday': []}
        for kind in ('emekli', 'aday'):
            for e in rec.get(kind, []):
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
    cikis = 1 if report['sonuc'] == 'İHLAL' else 0
    report['arac'] = 'anahtar-denetim'; report['surum'] = '0.2'; report['git_head'] = git_head(repo); report['cikis'] = cikis
    if a.json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
    if not a.sessiz:
        print(f"=== anahtar-denetim — kayıt {kayit} — {len(files)} md dosya", file=insan)
        if errs:
            print("BÜTÜNLÜK HATALARI:", file=insan); [print("  - " + x, file=insan) for x in errs]
        for e in report['anahtarlar']:
            print(f"\n## {e['anahtar_id']} [{e['tur']}] güncel='{e['guncel']}'", file=insan)
            for kind, label in (('emekli', 'EMEKLİ'), ('aday', 'ADAY (sayılır, ihlal üretmez)')):
                for it in e[kind]:
                    c = it['sayim']
                    print(f"  {label}: '{it['deger']}' → '{it['replaced_by']}' ({it.get('tarih') or 'tarihsiz'})", file=insan)
                    print(f"    sıcak: ihlal {c['sicak']['ihlal']} / izinli {c['sicak']['izinli']} · ılık: ihlal {c['ilik']['ihlal']} / izinli {c['ilik']['izinli']}"
                          + (f" [{it.get('ilik_hukum')}]" if kind == 'emekli' else '') + f" · soğuk(tarihçe): {c['soguk']['ihlal'] + c['soguk']['izinli']}", file=insan)
                    if it['sicak_ihlal_dosya']: print(f"    sıcak ihlal dosyaları: {', '.join(it['sicak_ihlal_dosya'])}", file=insan)
                    if it['ilik_ihlal_dosya']: print(f"    ılık ihlal dosyaları: {', '.join(it['ilik_ihlal_dosya'])}", file=insan)
                    for h in it['ornek']:
                        print(f"      - {h['dosya']}:{h['satir']} [{h['katman']}] {h['metin']}", file=insan)
        print(f"\n=== SONUÇ: {report['sonuc']} (sıcak ihlal toplam {hot_viol_total}; bütünlük hatası {len(errs)})", file=insan)
    sys.exit(cikis)

if __name__ == '__main__':
    main()
