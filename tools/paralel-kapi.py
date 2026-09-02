#!/usr/bin/env python3
"""paralel-kapi.py — Koşum-önü paralellik kapısı (İB-63 PK-11; v0-deneysel m.29, 2026-08-30). LLM YOK (Karar 65).

Ne bu: `veri/manifest/*.json` birim-manifestlerini (İB-63 PROTOTİP-1 şeması) okur, her çift için Bernstein koşulunu
(yazar∩yazar=∅ ∧ yazar∩okur=∅ ∧ okur∩yazar=∅) ve PK-1..12 kural listesini uygular; çift başına hüküm verir:
  PARALEL-SERBEST · SIRALI(neden) · RED(neden) · BEKLE(PK-12: diğer oturumun ayak-izine dokunuyor)
ve planlı birimleri deterministik dalgalara (aynı anda koşabilecek kümeler) böler; `--kademe N` ile dalga genişliği
N'e kısılır (kademeli paralellik artışı: 1 → 2 → 3 …).

Grain: birim çifti (dosya granülü; `#bolum` eki aynı dosyada farklı bölüm = ayrık, PK-3 — belirsizlik dosya granülüne terfi).
Kaynak adlandırma: düz yol ∨ glob (`cc/rapor-*.md`, `veri/*`) · `git@<sha>:yol` = DEĞİŞMEZ SNAPSHOT (asla çakışmaz, PK-8 sürüm-damgalı okuma)
· `web` = dış girdi (çakışmaz; PK-2 uyarısı üretir).
Modlar: (yok) insan çıktısı stdout · `--json` tek JSON nesnesi stdout (AXI A1) · `--kademe N` · `--manifest-dizin` · `--repo`.
Çıkış (AXI A2): 0 RED yok · 1 manifest bütünlük hatası (eksik alan, bilinmeyen `sira`, çevrim) · 2 kullanım · 3 RED var (plan yine üretilir, RED çiftler ayrı dalgaya).
Kayıt: hüküm listesi çıktıda; kalıcı kayıt çağıranın (rapor/teslim). `durum` alanı `canli-diger-oturum` olan birim PLANLANMAZ, yalnız kısıt üretir (PK-12).
"""
import argparse, fnmatch, glob, json, os, subprocess, sys
from itertools import combinations

ARAC, SURUM = 'paralel-kapi', '0.1'
ZORUNLU = ['birim_id', 'tur', 'pist', 'okur', 'yazar', 'granul', 'sira', 'silver', 'kanon_yuzeyi', 'dis_etki']

def git_head(repo):
    try:
        return subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], cwd=repo, capture_output=True, text=True).stdout.strip()
    except Exception:
        return '?'

def yukle(dizin):
    birimler, hatalar = {}, []
    for yol in sorted(glob.glob(os.path.join(dizin, '*.json'))):
        try:
            b = json.load(open(yol, encoding='utf-8'))
        except Exception as e:
            hatalar.append(f'{os.path.basename(yol)}: JSON okunamadı ({e})'); continue
        eksik = [k for k in ZORUNLU if k not in b]
        if eksik:
            hatalar.append(f'{os.path.basename(yol)}: eksik alan {eksik}'); continue
        if b['birim_id'] in birimler:
            hatalar.append(f"{b['birim_id']}: çift tanım"); continue
        b['_dosya'] = os.path.basename(yol)
        birimler[b['birim_id']] = b
    for bid, b in birimler.items():
        for s in b['sira']:
            if s not in birimler:
                hatalar.append(f'{bid}: sira → bilinmeyen birim {s}')
    durum = {}
    def dfs(u, yol):
        durum[u] = 1
        for v in birimler[u]['sira']:
            if v not in birimler: continue
            if durum.get(v) == 1: hatalar.append(f'sira çevrimi: {" → ".join(yol + [v])}'); return
            if durum.get(v) is None: dfs(v, yol + [v])
        durum[u] = 2
    for u in birimler:
        if durum.get(u) is None: dfs(u, [u])
    return birimler, hatalar

def kaynak_ayir(k):
    """(dosya, bolum, tur) — tur: 'snapshot' | 'dis' | 'dosya'"""
    if k.startswith('git@'): return (k, None, 'snapshot')
    if k in ('web', 'stdin'): return (k, None, 'dis')
    if '#' in k:
        d, b = k.split('#', 1); return (d, b, 'dosya')
    return (k, None, 'dosya')

def kesisir(a, b):
    """iki kaynak adı aynı öğeye dokunuyor mu (glob iki yönlü; snapshot/dış asla)."""
    da, ba, ta = kaynak_ayir(a); db, bb, tb = kaynak_ayir(b)
    if ta != 'dosya' or tb != 'dosya': return False
    pa = da + '*' if da.endswith('/') else da
    pb = db + '*' if db.endswith('/') else db
    if not (pa == pb or fnmatch.fnmatch(pa, pb) or fnmatch.fnmatch(pb, pa)): return False
    if ba and bb and ba != bb: return False
    return True

def cakisma(x, y):
    """Bernstein ihlal listesi: (tür, öğe_x, öğe_y)."""
    out = []
    for ax in x['yazar']:
        for ay in y['yazar']:
            if kesisir(ax, ay): out.append(('yazar∩yazar', ax, ay))
        for oy in y['okur']:
            if kesisir(ax, oy): out.append(('yazar∩okur', ax, oy))
    for ox in x['okur']:
        for ay in y['yazar']:
            if kesisir(ox, ay): out.append(('okur∩yazar', ox, ay))
    return out

def canli(b): return str(b.get('durum', '')).startswith('canli')
def tamamlandi(b): return str(b.get('durum', '')).startswith(('tamam', 'kapandi'))

def tur_turet(b):
    """Saf fonksiyon (LLM YOK, deterministik) — manifestin `tur` alanını mevcut alanlardan TÜRETİR.

    Öncelik 1 — MATRİS: `matris` anahtarı ∨ adı 'eksen' veya 'hucre' ile başlayan herhangi bir üst
    alan varsa (İB-69 a1 şeması, raporlar/2026-08-31-ib69-matris-a1-formalizasyon.md §1/§3 — EKSEN/HUCRE
    blokları, alan adları `eksenler`, `hucre_tipi`, `hucre_anahtari` …) → 'matris'.

    Öncelik 2 — Model-1 karar tablosu (raporlar/2026-08-31-ib65-loop-pipeline-secim-atlas.md §5.1),
    üç yüklem manifestin şu alanlarından okunur (kaynak belgede yüklem→alan eşlemesi LİTERAL VERİLMEMİŞ;
    aşağıdaki eşleme bu koşumda seçilen PROXY'dir — AÇIK SORU, Salih onayı gerekir):
      Y1 SÜREKLİ?              ← tetik_turu ∉ {None, 'seans'} (yalnız 'seans' tek-turlu/oturum-tetikli sayılır)
      Y2 tekrar-sayısı bilinir? ← dis_tavan alanı dolu (§232: hibrit/loop için dış-tavan zorunlu alanı)
      Y3 iç-sıra sabit?        ← iterasyon_ayak_izi == 'sabit' (PK-10 kuralı zaten 'sabit'/'buyuyen' ayrımı kullanıyor)
    ¬Y1 ∧ Y3 → pipeline · Y1 ∧ ¬Y2 ∧ ¬Y3 → loop · Y1 ∧ Y3 → hibrit · aksi tüm kombinasyonlar → belirsiz (masaya).
    """
    if 'matris' in b or any(k.startswith('eksen') or k.startswith('hucre') for k in b):
        return 'matris'
    y1 = b.get('tetik_turu') not in (None, 'seans')
    y3 = b.get('iterasyon_ayak_izi') == 'sabit'
    y2 = b.get('dis_tavan') is not None
    if not y1 and y3:
        return 'pipeline'
    if y1 and not y2 and not y3:
        return 'loop'
    if y1 and y3:
        return 'hibrit'
    return 'belirsiz'

def hukum(x, y):
    sira = (y['birim_id'] in x['sira']) or (x['birim_id'] in y['sira'])
    if x['kanon_yuzeyi'] or y['kanon_yuzeyi']:
        kim = [b['birim_id'] for b in (x, y) if b['kanon_yuzeyi']]
        if canli(x) or canli(y):
            c = cakisma(x, y)
            if c: return 'BEKLE', f'PK-12 + PK-6: canlı kanon-yüzeyli birim {kim} ile çakışma {[(t, a) for t, a, _ in c][:3]}'
            return 'PARALEL-SERBEST', f'PK-6 kanon-yüzeyli {kim} canlı ama ayak-izi ayrık (yalnız snapshot okuma)'
        return 'SIRALI', f'PK-6 kanon yüzeyi {kim} her şeyle sıralı + Salih imza hattı'
    if x['silver'] == 'yazar' and y['silver'] == 'yazar':
        return ('SIRALI', 'PK-5 silver tek-yazar (sira kenarı var)') if sira else ('RED', 'PK-5 silver tek-yazar: iki silver-yazar paralel olamaz, sira kenarı yok')
    if x.get('dislama_grubu') and x.get('dislama_grubu') == y.get('dislama_grubu'):
        return 'SIRALI', f"PK-7 kira: aynı dışlama grubu '{x['dislama_grubu']}'"
    c = cakisma(x, y)
    if c:
        ozet = '; '.join(f'{t}: {a} ~ {b}' for t, a, b in c[:3]) + (' …' if len(c) > 3 else '')
        if sira: return 'SIRALI', f'PK-1 sira kenarı; çakışma {ozet}'
        if canli(x) or canli(y): return 'BEKLE', f'PK-12 diğer oturumun ayak-izi: {ozet}'
        return 'RED', f'PK-1 çakışma, sira kenarı yok: {ozet} → seri koş ya da sira ekle'
    if x['tur'] == 'loop' and y['tur'] == 'loop':
        if x.get('iterasyon_ayak_izi') == 'buyuyen' or y.get('iterasyon_ayak_izi') == 'buyuyen':
            return 'SIRALI', 'PK-10 büyüyen iterasyon ayak-izi (v0: seri)'
    if sira: return 'SIRALI', 'sira kenarı (ayak-izi ayrık olsa da beyan edilmiş sıra)'
    return 'PARALEL-SERBEST', 'Bernstein 3/3 ∅'

def birim_uyarilari(b):
    u = []
    if b.get('belirlenimsiz_girdi') and not b.get('dogrulama_kapisi'):
        u.append('PK-2: belirlenimsiz girdi var, dogrulama_kapisi yok')
    if b.get('dis_etki') and not b.get('idempotency_anahtari'):
        u.append('PK-9: dış etki var, idempotency_anahtari yok → seri-sınıf')
    if b['tur'] == 'loop' and not b.get('durma_kosulu'):
        u.append('durma_kosulu eksik (loop için zorunlu)')
    if 'model-çıktısı' in (b.get('belirlenimsiz_girdi') or []) and not b.get('kapsam_beyani'):
        u.append('kapsam_beyani eksik (ajan-birim için zorunlu)')
    if b.get('zorlama_modu', 'yok') == 'yok' and not canli(b):
        u.append('PK-4: zorlama_modu yok — hermetiklik varsayılıyor')
    return u

def dalgalar(birimler, ciftler, kademe):
    """Deterministik açgözlü dalga planı: öncelik → birim_id sırası; sira öncülleri önceki dalgada; dalga içi çiftler PARALEL-SERBEST; genişlik ≤ kademe."""
    H = {}
    for c in ciftler: H[(c['a'], c['b'])] = H[(c['b'], c['a'])] = c['hukum']
    planli = [b for b in birimler.values() if not canli(b)]
    bekleyen = sorted(b['birim_id'] for b in planli if any(H.get((b['birim_id'], o['birim_id'])) == 'BEKLE' for o in birimler.values() if canli(o)))
    aday = sorted((b for b in planli if b['birim_id'] not in bekleyen), key=lambda b: (b.get('oncelik', 5), b['birim_id']))
    yerlesti, dalga_no, plan = {}, 0, []
    while len(yerlesti) < len(aday):
        dalga_no += 1; dalga = []
        for b in aday:
            bid = b['birim_id']
            if bid in yerlesti: continue
            if any(s not in yerlesti or yerlesti[s] >= dalga_no for s in b['sira'] if s in birimler and not canli(birimler[s])): continue
            if any(H.get((bid, d)) != 'PARALEL-SERBEST' for d in dalga): continue
            if kademe and len(dalga) >= kademe: continue
            dalga.append(bid)
        if not dalga:
            plan.append({'dalga': dalga_no, 'birimler': [], 'not': 'ilerleme yok — kalanlar bekleyen/çevrim'}); break
        for bid in dalga: yerlesti[bid] = dalga_no
        plan.append({'dalga': dalga_no, 'birimler': dalga})
    return plan, bekleyen

def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--repo', default=os.getcwd()); p.add_argument('--manifest-dizin', default='veri/manifest')
    p.add_argument('--kademe', type=int, default=0, help='dalga genişliği tavanı (0 = sınırsız)')
    p.add_argument('--json', action='store_true'); p.add_argument('--sessiz', action='store_true')
    a = p.parse_args()
    dizin = os.path.join(a.repo, a.manifest_dizin)
    if not os.path.isdir(dizin):
        print(f'HATA: manifest dizini yok: {dizin}', file=sys.stderr); sys.exit(2)
    birimler, hatalar = yukle(dizin)
    # Kapı v0.2 (PK): durum='tamam*'|'kapandi*' birimler dalga planından VE çakışma taramasından düşer —
    # yalnız canlı (tamamlanmamış) birimler taranır; sira/bütünlük denetimi (yukle) tüm birimler üzerinde kalır.
    tamam_birimler = {bid: b for bid, b in birimler.items() if tamamlandi(b)}
    canli_birimler = {bid: b for bid, b in birimler.items() if not tamamlandi(b)}
    ciftler = []
    for x, y in combinations(sorted(canli_birimler.values(), key=lambda b: b['birim_id']), 2):
        h, n = hukum(x, y); ciftler.append({'a': x['birim_id'], 'b': y['birim_id'], 'hukum': h, 'neden': n})
    uyarilar = {b: birim_uyarilari(birimler[b]) for b in sorted(birimler)}
    uyarilar = {k: v for k, v in uyarilar.items() if v}
    plan, bekleyen = dalgalar(canli_birimler, ciftler, a.kademe)
    red = sum(1 for c in ciftler if c['hukum'] == 'RED')
    cikis = 1 if hatalar else (3 if red else 0)
    sayim = {}
    for c in ciftler: sayim[c['hukum']] = sayim.get(c['hukum'], 0) + 1
    out = {'arac': ARAC, 'surum': SURUM, 'git_head': git_head(a.repo), 'cikis': cikis, 'birim_n': len(birimler),
           'planli_n': sum(1 for b in canli_birimler.values() if not canli(b)), 'tamam_birim_n': len(tamam_birimler),
           'kademe': a.kademe, 'hukum_sayim': sayim,
           'butunluk_hatalari': hatalar, 'ciftler': ciftler, 'uyarilar': uyarilar, 'dalgalar': plan, 'bekleyen': bekleyen}
    if a.json:
        print(json.dumps(out, ensure_ascii=False)); sys.exit(cikis)
    if not a.sessiz:
        print(f"=== paralel-kapi v{SURUM} @ {out['git_head']} — {len(birimler)} birim ({out['planli_n']} planlı) · kademe={a.kademe or '∞'} · hüküm sayımı {sayim}")
        print(f"tamam-birim düşüldü: {len(tamam_birimler)}")
        if hatalar: print('BÜTÜNLÜK HATALARI:'); [print('  - ' + h) for h in hatalar]
        print('\n## Çiftler')
        for c in ciftler: print(f"  {c['hukum']:16} {c['a']} × {c['b']} — {c['neden']}")
        if uyarilar:
            print('\n## Birim uyarıları'); [print(f'  {k}: ' + ' | '.join(v)) for k, v in uyarilar.items()]
        print('\n## Dalga planı'); [print(f"  dalga {d['dalga']}: {d['birimler']}" + (f" ({d['not']})" if d.get('not') else '')) for d in plan]
        if bekleyen: print(f'  BEKLEYEN (PK-12): {bekleyen}')
    sys.exit(cikis)

if __name__ == '__main__':
    main()
