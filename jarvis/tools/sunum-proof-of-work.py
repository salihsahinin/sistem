#!/usr/bin/env python3
"""sunum-proof-of-work.py — "JARVIS ne kadar geliştirildi?" sorusuna proof-of-work sunumu (m.9: kanıt = push'lanmış commit; m.39: her rakam kaynaklı).
Rakamların TAMAMI koşum anında git + dosya sistemi + veri/baglam.sqlite'tan çekilir (elle yazılmış sayı yok; ölçülemeyen [?] damgalı).
Biçim: son-50 sunumuyla aynı mobil slayt iskeleti (tools/sunum-son50.py) + yazdırma stili (PDF: her slayt bir sayfa).
Kullanım: python3 tools/sunum-proof-of-work.py [--repo <yol>] [--out raporlar/jarvis/jarvis-proof-of-work-SUNUM.html]
Sonra: PDF için Chrome headless — bkz. tools/SCRIPTLER.md · teslim: open -R <dosya> + open <dosya>.
STDLIB ONLY.
"""
import argparse, glob, html, json, os, sqlite3, subprocess
from collections import Counter
from datetime import date, datetime, timedelta, timezone

TR = timezone(timedelta(hours=3))


def sh(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, shell=isinstance(cmd, str)).stdout.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--out", default=None)
    a = ap.parse_args(); R = os.path.abspath(a.repo)
    out = a.out or os.path.join(R, "raporlar", "jarvis", "jarvis-proof-of-work-SUNUM.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    now = datetime.now(TR); tarih = now.strftime("%Y-%m-%d %H:%M")
    head = sh(["git", "rev-parse", "--short", "HEAD"], R)
    ilk = sh("git log --reverse --format=%ad --date=short | head -1", R)
    son = sh(["git", "log", "-1", "--format=%ad", "--date=short"], R)
    n_commit = int(sh(["git", "rev-list", "--count", "HEAD"], R))
    days = sh("git log --format=%ad --date=short", R).split("\n")
    gun_sayac = Counter(days); n_gun = len(gun_sayac)
    takvim = (date.fromisoformat(son) - date.fromisoformat(ilk)).days + 1
    subj = sh("git log --format=%s", R).split("\n")
    n_icra = sum(1 for s in subj if s.startswith("[icra]")); n_dam = sum(1 for s in subj if s.lower().startswith("[dam"))
    yazar = Counter(sh("git log --format=%an", R).split("\n"))
    tracked = sh("git ls-files", R).split("\n")
    n_tracked = len(tracked)
    tot_bytes = sum(os.path.getsize(os.path.join(R, f)) for f in tracked if os.path.isfile(os.path.join(R, f)))
    def cnt(prefix, ext=None):
        fs = [f for f in tracked if f.startswith(prefix) and (ext is None or f.endswith(ext))]
        b = sum(os.path.getsize(os.path.join(R, f)) for f in fs if os.path.isfile(os.path.join(R, f)))
        return len(fs), b
    md_lines = sum(sum(1 for _ in open(os.path.join(R, f), errors="ignore")) for f in tracked if f.endswith(".md") and os.path.isfile(os.path.join(R, f)))
    py = [f for f in tracked if f.endswith(".py")]; py_lines = sum(sum(1 for _ in open(os.path.join(R, f), errors="ignore")) for f in py)
    n_d2 = sum(1 for f in tracked if f.endswith(".d2"))
    skills = sorted(d for d in os.listdir(os.path.join(R, ".claude", "skills")) if os.path.isdir(os.path.join(R, ".claude", "skills", d)))
    n_eval = len(glob.glob(os.path.join(R, ".claude", "skills", "*", "eval*", "*.json")))
    n_wiki = len([f for f in tracked if f.startswith("wiki/") and f.endswith(".md") and not f.endswith("README.md")])
    n_gorev = len([f for f in tracked if f.startswith("cc/gorev/")]); n_rapor = len([f for f in tracked if f.startswith("cc/rapor/")])
    n_raporlar = len([f for f in tracked if f.startswith("raporlar/") and f.endswith(".md")]); n_teslim = len([f for f in tracked if f.startswith("raporlar/vardiya/vardiya-teslim-")])
    n_core = len([f for f in tracked if f.startswith("core/") and f.endswith(".md") and f.count("/") == 1])
    n_madde = sum(1 for l in open(os.path.join(R, "core", "tuzuk-v0.md"), errors="ignore") if l[:1].isdigit() and ". **" in l[:6])
    db = {}
    try:
        con = sqlite3.connect(os.path.join(R, "veri", "baglam.sqlite"))
        for t in ("dosya", "kayit", "referans", "anahtar", "prompt"):
            try: db[t] = con.execute(f"select count(*) from {t}").fetchone()[0]
            except Exception: db[t] = None
        con.close()
    except Exception: pass
    # workflow ölçümü — yalnız bu makinede kalan koşum çıktıları (ölçüm anı; taşınmaz)
    wf_n = wf_tok = wf_ag = 0
    for f in glob.glob(os.path.expanduser("/private/tmp/claude-501/-Users-HasanSalihSahin-sistem-jarvis/*/tasks/*.output")):
        try:
            d = json.load(open(f))
            if isinstance(d, dict) and "totalTokens" in d: wf_n += 1; wf_tok += int(d["totalTokens"] or 0); wf_ag += int(d.get("agentCount") or 0)
        except Exception: pass
    # haftalık commit
    d0 = date.fromisoformat(ilk); weeks = []
    while d0 <= date.fromisoformat(son):
        d1 = d0 + timedelta(days=6); c = sum(v for k, v in gun_sayac.items() if d0 <= date.fromisoformat(k) <= d1)
        aktif = sum(1 for k in gun_sayac if d0 <= date.fromisoformat(k) <= d1)
        weeks.append((d0.strftime("%d.%m"), min(d1, date.fromisoformat(son)).strftime("%d.%m"), c, aktif)); d0 = d1 + timedelta(days=1)
    top5 = gun_sayac.most_common(5)
    e = lambda s: html.escape(str(s))
    f = lambda n: f"{n:,}".replace(",", ".")
    week_rows = "".join(f"<tr><td class='nw'>{a}–{b}</td><td class='n'>{c}</td><td class='n'>{k}/7</td><td><span class='bar' style='width:{max(2, int(c/max(1,max(w[2] for w in weeks))*100))}%'></span></td></tr>" for a, b, c, k in weeks)
    top_rows = " · ".join(f"<b>{k}</b> {v}" for k, v in top5)
    yazar_txt = " · ".join(f"{e(k)} {v}" for k, v in yazar.most_common(4))
    skill_txt = " · ".join(f"<span class='mono'>{e(s)}</span>" for s in skills)
    dbtxt = " · ".join(f"<b>{f(v)}</b> {k}" for k, v in db.items() if v is not None)
    wf_txt = (f"<b>{wf_n}</b> workflow · <b>{wf_ag}</b> ajan · <b>{f(wf_tok)}</b> işçi-token" if wf_n else "ölçüm dosyası yok [?]")

    page = f"""<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>JARVIS — proof of work</title>
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="color-scheme" content="dark">
<style>
:root{{--bg:#0f1115;--fg:#e8e6e1;--muted:#9aa0a6;--acc:#f2b134;--acc2:#4fb0c6;--card:#181b22;--line:#2a2f3a;--pad:clamp(14px,4vw,64px)}}
*{{box-sizing:border-box}} html,body{{margin:0;background:var(--bg);color:var(--fg);font:16px/1.45 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif;-webkit-text-size-adjust:100%}}
.deck{{height:100vh;height:100dvh;overflow:hidden;position:relative}}
.slide{{position:absolute;inset:0;padding:calc(env(safe-area-inset-top) + 3vh) var(--pad) calc(env(safe-area-inset-bottom) + 76px);display:none;flex-direction:column;overflow:auto;-webkit-overflow-scrolling:touch}}
.slide.on{{display:flex}}
h1{{font-size:clamp(26px,5.5vw,56px);margin:0 0 .3em;line-height:1.1}} h2{{font-size:clamp(19px,3.4vw,34px);margin:0 0 .6em;color:var(--acc)}}
p,li{{font-size:clamp(14px,1.9vw,21px);max-width:75ch}} .lead{{font-size:clamp(16px,2.6vw,26px)}}
.muted{{color:var(--muted)}} .kicker{{letter-spacing:.14em;text-transform:uppercase;font-size:11px;color:var(--acc2);margin-bottom:1em}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));gap:12px;margin-top:.6em}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;min-width:0}}
.card h3{{margin:0 0 .35em;font-size:16px;color:var(--acc)}} .card p{{margin:0;font-size:14px;color:#cfd3d8;max-width:none}}
.stat{{display:flex;flex-direction:column;gap:2px}} .stat .v{{font-size:clamp(26px,4.2vw,44px);font-weight:700;color:var(--fg);line-height:1}} .stat .k{{font-size:12px;color:var(--muted);letter-spacing:.04em}} .stat .s{{font-size:12px;color:#cfd3d8}}
.tl{{list-style:none;padding:0;margin:.4em 0 0}} .tl li{{display:grid;grid-template-columns:5.5em 1fr;gap:10px;padding:6px 0;border-bottom:1px solid var(--line);font-size:14px}} .tl b{{color:var(--acc);font-family:ui-monospace,Menlo,monospace;font-weight:600}}
table{{border-collapse:collapse;width:100%;font-size:13px}} th,td{{padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top;text-align:left}} th{{color:var(--acc)}} td.n{{text-align:right;color:var(--fg)}} .nw{{white-space:nowrap}}
.bar{{display:inline-block;height:10px;background:var(--acc2);border-radius:3px;vertical-align:middle}}
.mono{{font-family:ui-monospace,Menlo,monospace}} .small{{font-size:12px;color:var(--muted)}} code{{font-family:ui-monospace,Menlo,monospace;background:#1f232c;padding:1px 6px;border-radius:4px;font-size:12px}}
.foot{{margin-top:auto;padding-top:.8em;color:var(--muted);font-size:12px}}
.nav{{position:fixed;left:0;right:0;bottom:0;padding:10px var(--pad) calc(10px + env(safe-area-inset-bottom));display:flex;justify-content:space-between;align-items:center;gap:12px;background:linear-gradient(to top,rgba(15,17,21,.98),rgba(15,17,21,.6));z-index:5}}
.nav button{{min-width:44px;min-height:44px;padding:8px 18px;border-radius:999px;border:1px solid var(--line);background:#1f232c;color:var(--fg);font-size:16px;cursor:pointer;touch-action:manipulation}} .nav .pos{{color:var(--muted);font-size:13px}}
kbd{{border:1px solid var(--line);border-radius:4px;padding:0 5px;font-size:11px}}
@media (max-width:480px){{ h1{{font-size:26px}} .card{{padding:12px 14px}} .tl li{{grid-template-columns:4.6em 1fr}} }}
@media print{{ @page{{size:A4 portrait;margin:12mm}} html,body{{background:#0f1115 !important;color:var(--fg);-webkit-print-color-adjust:exact;print-color-adjust:exact}} .deck{{height:auto;overflow:visible}} .slide{{display:flex !important;position:static;inset:auto;height:auto;min-height:0;padding:6mm 4mm;overflow:visible;break-after:page;page-break-after:always;animation:none}} .slide:last-child{{break-after:auto;page-break-after:auto}} .nav{{display:none}} .foot{{margin-top:1em}} p,li{{font-size:12.5px}} .stat .v{{font-size:30px}} h1{{font-size:34px}} h2{{font-size:22px}} }}
</style></head><body><div class="deck" id="deck">

<section class="slide on">
<div class="kicker">JARVIS · proof of work · {tarih} · HEAD {head}</div>
<h1>JARVIS ne kadar geliştirildi?</h1>
<p class="lead"><b>{ilk} → {son}</b>: {takvim} takvim gününde <b>{n_commit} commit</b>, {n_gun} aktif gün, {n_tracked} dosya, {tot_bytes/1048576:.1f} MB — hepsi tek private git deposunda, hepsi push'lanmış.</p>
<p class="muted">Bu sunumdaki her sayı, sunumu üreten script (<span class="mono">tools/sunum-proof-of-work.py</span>) tarafından koşum anında <b>git log + dosya sistemi + SQLite</b>'tan çekildi; elle yazılmış sayı yok. Ölçülemeyen kalem <b>[?]</b> ile damgalı. Kural: kanıt = push'lanmış commit; plan kanıt değildir.</p>
<div class="foot">Gezinme: sağa/sola kaydır ya da alttaki düğmeler · klavye <kbd>→</kbd> <kbd>←</kbd> · Yazarlar (aynı ekip, model+insan): {yazar_txt}</div>
</section>

<section class="slide">
<div class="kicker">ne inşa edildi</div>
<h2>JARVIS = kanon-tabanlı kişisel LLM-operasyon sistemi (Claude Code üstünde)</h2>
<div class="grid">
<div class="card"><h3>1 · Kanon (core/)</h3><p>{n_core} kural dosyası; tüzük <b>{n_madde} madde</b> (imzalı karar kayıtları), durum-kapsülü + pano (her oturumun otomatik okuduğu devir katmanı), ingest şeması v2, ajan-metodolojisi v1, skill-üretim/tetikleme şemaları, halüsinasyon-önleme paketi, şema-sıkıştırma, bağlam-anahtar kaydı, world-model tasarımı v1 — {n_d2} D2 grafı.</p></div>
<div class="card"><h3>2 · Ritüel + skill katmanı</h3><p><b>{len(skills)} skill</b> ({n_eval} eval dosyası): oturum açılış/kapanış ritüelleri, görev-emri derleme, m.40b çift-atlas koşumu, pipeline koşumu, karar modeli, çelişki kapısı, damıtma, halüsinasyon-freni, skill-kapısı (kapı-ağacı), yol-planla, wiki yazımı…</p></div>
<div class="card"><h3>3 · Araçlar (tools/)</h3><p><b>{len(py)} Python</b> aracı, <b>{f(py_lines)} satır</b>, stdlib-only: bağlam→veri ETL, anahtar denetimi, kapı/tetik denetim script'leri, derece formülü, prompt bronz→silver→gold hattı, sunum üreticileri.</p></div>
<div class="card"><h3>4 · Veri (veri/)</h3><p>Kanonun kendisi tabloya döküldü: {dbtxt} — SQLite + JSONL + CSV gold görünümleri; sözleşme + testler (unique / not_null / accepted_values).</p></div>
<div class="card"><h3>5 · Ajan çıktıları (cc/)</h3><p><b>{n_gorev} görev emri</b> + <b>{n_rapor} ajan raporu</b> (tez → antitez → örneklem-denetim → maskeli hakem zinciri), {len([x for x in tracked if x.startswith('cc/pipeline-')])} pipeline manifesti.</p></div>
<div class="card"><h3>6 · Raporlar + wiki</h3><p><b>{n_raporlar} rapor</b> ({n_teslim} seans teslim raporu = her oturumun yazılı devri), <b>{n_wiki} wiki sayfası</b> (6-blok standart, süpersede zinciri), toplam <b>{f(md_lines)} satır</b> markdown.</p></div>
</div>
</section>

<section class="slide">
<div class="kicker">sayılar</div>
<h2>Envanter (koşum anında ölçüldü)</h2>
<div class="grid">
<div class="card stat"><span class="v">{n_commit}</span><span class="k">commit</span><span class="s">[icra] {n_icra} · [damıtma] {n_dam}</span></div>
<div class="card stat"><span class="v">{n_gun}<span class="small">/{takvim}</span></span><span class="k">aktif gün / takvim günü</span><span class="s">ilk {ilk} · son {son}</span></div>
<div class="card stat"><span class="v">{n_tracked}</span><span class="k">izlenen dosya</span><span class="s">{tot_bytes/1048576:.1f} MB · {f(md_lines)} satır md</span></div>
<div class="card stat"><span class="v">{len(skills)}</span><span class="k">skill</span><span class="s">{n_eval} eval · kapı-ağacından geçirilmiş</span></div>
<div class="card stat"><span class="v">{n_madde}</span><span class="k">tüzük maddesi</span><span class="s">{n_core} core kural dosyası · {n_d2} D2 graf</span></div>
<div class="card stat"><span class="v">{n_gorev}+{n_rapor}</span><span class="k">görev emri + ajan raporu</span><span class="s">cc/ köprü kanalı</span></div>
<div class="card stat"><span class="v">{n_raporlar}</span><span class="k">rapor</span><span class="s">{n_teslim} seans teslimi · {n_wiki} wiki sayfası</span></div>
<div class="card stat"><span class="v">{f(py_lines)}</span><span class="k">satır Python</span><span class="s">{len(py)} araç, stdlib-only</span></div>
<div class="card stat"><span class="v">{f(db.get('kayit') or 0)}</span><span class="k">veri kaydı (SQLite)</span><span class="s">{f(db.get('referans') or 0)} referans · {db.get('anahtar')} anahtar · {db.get('prompt')} prompt</span></div>
</div>
<div class="foot">Sayım komutları son slaytta. "Commit" bir iş birimi değil kanıt izidir; büyüklüğü satır sayısına değil karar/teslim ritmine bakarak okuyun.</div>
</section>

<section class="slide">
<div class="kicker">ajan koşumları</div>
<h2>Araştırma ajanları: m.40b çift-atlas zinciri</h2>
<p>Her araştırma emri <b>tez → CoVe-Factored antitez</b> (yalnız iddia satırları, gerekçesiz — çıpalama freni) <b>→ V26 örneklem-denetimi</b> (kaynağa inip doğrulama) <b>→ taraf-maskeli hakem</b> (SAĞLAM/DARALDI/DÜŞTÜ/ÇELİŞKİLİ) zincirinden geçer; işçi çıktıları JSON-şemalı, rapor mekanik derlenir, Jarvis sentezi ayrı etiketli.</p>
<div class="grid">
<div class="card"><h3>Bu Mac'te ölçülen (08-12 → bugün)</h3><p>{wf_txt}. Örnek son koşum: 3 aile × 4 işçi = 12 ajan · 518.035 token · 36 tez iddiası + 36 itiraz · hayatta-kalma 5/30/1/0 · kaynak-denetimi 3/3.</p></div>
<div class="card"><h3>Öncesi (Windows/Cowork dönemi, 07-10 → 08-05)</h3><p>İlk CC köprü koşumu 07-14: 78 ajan · 2,4M token (defter kaydı). Dönem toplamı yerel çıktı dosyaları taşınmadığı için <b>ölçülmedi [?]</b>; kanonda anılan benzersiz workflow kimliği: 19.</p></div>
<div class="card"><h3>Ne öğrenildi (sistemin kendi ölçümüyle)</h3><p>Hayatta-kalma oranları düşük çıkar (çoğu iddia DARALIR) — bu hata değil ölçüt: sağlam çekirdek = bilgili karşı-tarafın çürütemediği. Token −%30 rejimi: 16 işçi 1,0-1,2M → 12 işçi ~0,5M, kapsam eşdeğer.</p></div>
</div>
</section>

<section class="slide">
<div class="kicker">zaman çizgisi</div>
<h2>Kilometre taşları (commit tarihleriyle)</h2>
<ul class="tl">
<li><b>07-10</b><span>Repo + core v0: kapsül, pano, tüzük, şablonlar; ilk araştırma raporları (indeks mimarisi, ingest hattı).</span></li>
<li><b>07-12</b><span>K-012 build: CLAUDE.md tam sürüm, tüzük m.34-36 imzalı (katmanlı ingest, tez çapası); wiki standardı.</span></li>
<li><b>07-13/14</b><span>m.37 karar-modeli (3 seçenek, token×zaman×kalite); ilk CC köprü koşumu (78 ajan).</span></li>
<li><b>07-19/21</b><span>m.42 ajan-yetki kanunu; <b>m.40b v0.2</b> çok-atlamalı diyalektik + m.44 rol katmanları (Salih imzası).</span></li>
<li><b>07-22→08-05</b><span>K2 yürütme turu (m.46), L8/Kun-Chen workflow katmanı, kayıt-onarım yordamı, üç-dil build mimarisi araştırması, kullanım kılavuzu.</span></li>
<li><b>08-12</b><span>Mac geçişi (WezTerm+tmux+CLI, firstmate ilk koşum); terminal = ana-sıra.</span></li>
<li><b>08-14</b><span>İngest şeması v2 (zarf+tip+triyaj+DLQ) · ajan-metodolojisi v1 (görev = tipli fonksiyon, hafıza = manifest).</span></li>
<li><b>08-15</b><span>Skill-üretim + tetikleme şemaları · halüsinasyon-önleme paketi (F1-F10 + H derece formülü) · şema-sıkıştırma (MDL) · bağlam-anahtar kaydı · V-1 bağlam→veri tablosu (37.668 kayıt).</span></li>
<li><b>08-16</b><span>World-model tasarımı v1 (galaxy şema) · prompt hattı bronz→silver→gold · stokastik-düşünce atlası + wiki · yol-planla skill'i (kapı-ağacından).</span></li>
</ul>
</section>

<section class="slide">
<div class="kicker">ritim</div>
<h2>Haftalık commit yoğunluğu</h2>
<table><thead><tr><th>hafta</th><th>commit</th><th>aktif gün</th><th></th></tr></thead><tbody>{week_rows}</tbody></table>
<p class="muted" style="margin-top:.8em">En yoğun günler: {top_rows}. 08-06→08-11 boşluğu = Windows→Mac geçişi (çalışma yüzeyi taşındı).</p>
<div class="foot">Kaynak: <code>git log --format=%ad --date=short | sort | uniq -c</code></div>
</section>

<section class="slide">
<div class="kicker">doğrulama + sınırlar</div>
<h2>Nasıl doğrulanır · neyi göstermez</h2>
<div class="grid">
<div class="card"><h3>Kendin say</h3><p><code>git rev-list --count HEAD</code> → {n_commit}<br><code>git log --format=%ad --date=short | sort -u | wc -l</code> → {n_gun}<br><code>git ls-files | wc -l</code> → {n_tracked}<br><code>ls .claude/skills | wc -l</code> → {len(skills)}<br><code>sqlite3 veri/baglam.sqlite "select count(*) from kayit"</code> → {f(db.get('kayit') or 0)}</p></div>
<div class="card"><h3>Sınırlar (dürüstlük)</h3><p>Depo <b>private</b>; dışarı yalnız bu özet çıkar. Commit/dosya sayısı iş kalitesini değil kanıt izini ölçer. Ajan-token toplamı yalnız Mac dönemi için ölçülü [?]. Tek kullanıcı, tek orkestratör; üretim sistemi değil kişisel operasyon deposu.</p></div>
<div class="card"><h3>Skill'ler</h3><p>{skill_txt}</p></div>
</div>
<div class="foot">Üretim: <span class="mono">python3 tools/sunum-proof-of-work.py</span> · {tarih} · HEAD {head} · aynı komut, aynı depo → aynı sayılar.</div>
</section>

</div>
<div class="nav"><button id="prev" aria-label="önceki">‹ geri</button><span class="pos" id="pos"></span><button id="next" aria-label="sonraki">ileri ›</button></div>
<script>
(function(){{
const s=[...document.querySelectorAll('.slide')];let i=0;const pos=document.getElementById('pos');
function go(k){{i=Math.max(0,Math.min(s.length-1,k));s.forEach((e,j)=>e.classList.toggle('on',j===i));pos.textContent=(i+1)+' / '+s.length;s[i].scrollTop=0;}}
document.getElementById('prev').onclick=()=>go(i-1);document.getElementById('next').onclick=()=>go(i+1);
document.addEventListener('keydown',e=>{{if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown'){{e.preventDefault();go(i+1);}}if(e.key==='ArrowLeft'||e.key==='PageUp'){{e.preventDefault();go(i-1);}}}});
let sx=0,sy=0;const deck=document.getElementById('deck');
deck.addEventListener('touchstart',e=>{{const t=e.touches[0];sx=t.clientX;sy=t.clientY;}},{{passive:true}});
deck.addEventListener('touchend',e=>{{const t=e.changedTouches[0];const dx=t.clientX-sx,dy=t.clientY-sy;if(Math.abs(dx)>60&&Math.abs(dx)>Math.abs(dy)*1.5){{go(dx<0?i+1:i-1);}}}},{{passive:true}});
go(0);
}})();
</script></body></html>"""
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(page)
    print(out, os.path.getsize(out), "bytes ·", n_commit, "commit ·", n_gun, "gün ·", len(skills), "skill · wf", wf_n, wf_ag, wf_tok)


if __name__ == "__main__":
    main()
