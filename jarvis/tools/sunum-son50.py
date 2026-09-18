#!/usr/bin/env python3
"""sunum-son50.py — 'Son 50 prompt' gold görünümünden tek-dosya HTML sunum üretir (mobil uyumlu; dış bağımlılık yok; STDLIB ONLY).
Girdi: veri/gorunum/v_son_50_prompt.csv (+ silver `prompt` sayımları) · Çıktı: raporlar/YYYY-MM/son-50-prompt-SUNUM.html (--tarih'ten türeyen ay dizini; sabit ad; Spotlight'ta 'son-50' aramasının İLK sonucu olsun diye ad anahtarla başlar, tarih içeride)
Mobil: dokunmatik kaydırma (tablo içinde başlayan kaydırma tabloyu kaydırır, slaydı değil) · büyük ileri/geri düğmeleri · 100dvh · dar ekranda ikincil kolonlar gizli (oturum/sıra/model/kar) · yazı clamp().
Kullanım: python3 tools/sunum-son50.py [--tarih YYYY-MM-DD] [--repo <yol>] · sonra: open -R <dosya> + open <dosya>
"""
import argparse, csv, html, os, sqlite3, subprocess
from datetime import datetime, timezone, timedelta

TR = timezone(timedelta(hours=3))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--tarih", default=None)
    a = ap.parse_args(); R = os.path.abspath(a.repo); tarih = a.tarih or datetime.now(TR).strftime("%Y-%m-%d")
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=R, capture_output=True, text=True).stdout.strip()
    rows = list(csv.DictReader(open(os.path.join(R, "veri", "gorunum", "v_son_50_prompt.csv"), encoding="utf-8")))
    con = sqlite3.connect(os.path.join(R, "veri", "baglam.sqlite"))
    n_prompt, n_oturum, ilk, son = con.execute("select count(*), count(distinct oturum_id), min(tarih_tr), max(tarih_tr) from prompt").fetchone()
    tur = con.execute("select tur,count(*) from prompt where prompt_id in (select prompt_id from v_son_50_prompt) group by 1 order by 2 desc").fetchall()
    con.close()
    e = lambda s: html.escape(str(s if s not in (None, "") else "—"))
    tr = "".join(
        f"<tr><td class='n'>{e(r['n'])}</td><td class='nw'>{e(r['tarih_tr'])}<span class='m-only'> {e(r['saat_tr'])}</span></td><td class='nw hide-m'>{e(r['saat_tr'])}</td>"
        f"<td class='mono hide-m'>{e(r['oturum_kisa'])}</td><td class='n hide-m'>{e(r['sira'])}</td>"
        f"<td><span class='tag t-{e(r['tur']).replace('/', '-')}'>{e(r['tur'])}</span></td>"
        f"<td class='mono small hide-s'>{e(r['sonraki_skill'])}</td><td class='small hide-m'>{e((r['sonraki_model'] or '—').replace('claude-', ''))}</td>"
        f"<td class='n hide-m'>{e(r['uzunluk_kar'])}</td><td class='p'>{e(r['metin_kisa'])}</td></tr>\n" for r in rows)
    tur_html = "".join(f"<li><b>{e(k)}</b> {v}</li>" for k, v in tur)
    page = f"""<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>Son 50 Prompt — sunum</title>
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="dark">
<style>
:root{{--bg:#0f1115;--fg:#e8e6e1;--muted:#9aa0a6;--acc:#f2b134;--acc2:#4fb0c6;--card:#181b22;--line:#2a2f3a;--pad:clamp(14px,4vw,64px)}}
*{{box-sizing:border-box}} html,body{{margin:0;background:var(--bg);color:var(--fg);font:16px/1.45 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif;-webkit-text-size-adjust:100%}}
.deck{{height:100vh;height:100dvh;overflow:hidden;position:relative}}
.slide{{position:absolute;inset:0;padding:calc(env(safe-area-inset-top) + 3vh) var(--pad) calc(env(safe-area-inset-bottom) + 76px);display:none;flex-direction:column;overflow:auto;-webkit-overflow-scrolling:touch}}
.slide.on{{display:flex}}
h1{{font-size:clamp(26px,5.5vw,56px);margin:0 0 .3em;line-height:1.1}} h2{{font-size:clamp(19px,3.4vw,34px);margin:0 0 .6em;color:var(--acc)}}
p,li{{font-size:clamp(14px,1.9vw,21px);max-width:70ch}} .lead{{font-size:clamp(16px,2.6vw,26px)}}
.muted{{color:var(--muted)}} .kicker{{letter-spacing:.14em;text-transform:uppercase;font-size:11px;color:var(--acc2);margin-bottom:1em}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:14px;margin-top:.8em}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px;min-width:0}}
.card h3{{margin:0 0 .4em;font-size:17px;color:var(--acc)}} .card p{{margin:0;font-size:14px;color:#cfd3d8;max-width:none}}
.flow{{display:flex;flex-wrap:wrap;gap:12px;align-items:stretch;margin-top:.8em}} .flow .card{{flex:1 1 220px}} .arrow{{align-self:center;color:var(--acc);font-size:26px;flex:0 0 auto}}
.tablewrap{{overflow:auto;border:1px solid var(--line);border-radius:10px;flex:1 1 auto;min-height:40vh;background:var(--card);-webkit-overflow-scrolling:touch}}
table{{border-collapse:collapse;width:100%;font-size:13px}} th,td{{padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top;text-align:left;white-space:nowrap}}
th{{position:sticky;top:0;background:#1f232c;color:var(--acc);z-index:1}} td.p{{white-space:normal;min-width:30ch;max-width:70ch}} td.n{{text-align:right;color:var(--muted)}} .mono{{font-family:ui-monospace,Menlo,monospace}} .small{{font-size:12px;color:var(--muted)}} .nw{{white-space:nowrap}}
.tag{{display:inline-block;padding:1px 8px;border-radius:999px;font-size:11px;background:#2a2f3a;color:#dfe3e8;white-space:nowrap}} .t-emir{{background:#3b2f0e;color:#f2b134}} .t-soru{{background:#0f2f3a;color:#4fb0c6}} .t-onay-devam{{background:#123322;color:#7fd8a5}} .t-durdur{{background:#3a1616;color:#ff8f8f}} .t-seans-acilis,.t-seans-kapanis{{background:#2b2542;color:#c9b8ff}}
.foot{{margin-top:auto;padding-top:.8em;color:var(--muted);font-size:12px}}
.m-only{{display:none}}
.nav{{position:fixed;left:0;right:0;bottom:0;padding:10px var(--pad) calc(10px + env(safe-area-inset-bottom));display:flex;justify-content:space-between;align-items:center;gap:12px;background:linear-gradient(to top,rgba(15,17,21,.98),rgba(15,17,21,.6));z-index:5}}
.nav button{{min-width:44px;min-height:44px;padding:8px 18px;border-radius:999px;border:1px solid var(--line);background:#1f232c;color:var(--fg);font-size:16px;cursor:pointer;touch-action:manipulation}}
.nav button:active{{background:#2a2f3a}} .nav .pos{{color:var(--muted);font-size:13px;text-align:center}}
kbd{{border:1px solid var(--line);border-radius:4px;padding:0 5px;font-size:11px}}
@media (max-width:820px){{ .hide-m{{display:none}} .m-only{{display:inline;color:var(--muted)}} table{{font-size:12px}} td.p{{min-width:22ch}} th,td{{padding:6px 6px}} }}
@media (max-width:480px){{ .hide-s{{display:none}} h1{{font-size:26px}} .kicker{{font-size:10px}} .card{{padding:12px 14px}} .flow .card{{flex-basis:100%}} .arrow{{transform:rotate(90deg);align-self:center;margin:-4px auto}} }}
@media (prefers-reduced-motion:no-preference){{ .slide.on{{animation:fade .18s ease}} @keyframes fade{{from{{opacity:.4}}to{{opacity:1}}}} }}
</style></head><body><div class="deck" id="deck">

<section class="slide on">
<div class="kicker">JARVIS · veri-mühendisliği katmanı · {tarih}</div>
<h1>Son 50 Prompt</h1>
<p class="lead">Salih'in JARVIS'e verdiği son 50 komutun <b>doğrulanmış, sorgulanabilir</b> tablosu — sohbet dökümü değil, veri.</p>
<p class="muted">Bu tablo ne işe yarar: (1) neyi, ne zaman, hangi oturumda istediğini <b>tek bakışta</b> görürsün; (2) hangi komutun hangi <b>skill'i</b> tetiklediğini ve hangi <b>modelin</b> cevapladığını gösterir; (3) komut türlerinin dağılımını (emir / soru / onay / durdur…) verir — JARVIS'i nasıl yönettiğinin ölçümü; (4) her satır ham kaynağına (oturum transkripti) geri-eşlenir — sonradan sorgulanabilir, silinmez.</p>
<div class="foot">Kaynak: {n_prompt} prompt · {n_oturum} jarvis oturumu · {ilk} → {son} · gold görünüm <span class="mono">v_son_50_prompt</span> · HEAD {head} · Gezinme: sağa/sola kaydır ya da alttaki düğmeler; klavyede <kbd>→</kbd> <kbd>←</kbd></div>
</section>

<section class="slide">
<div class="kicker">nasıl üretildi</div>
<h2>Bronz → Silver → Gold (katman = koşul, ad değil)</h2>
<div class="flow">
<div class="card"><h3>BRONZ · ham + provenans</h3><p>Oturum transkriptleri (koşum kütüğü, repo dışı) taranır; yalnız <b>gerçek Salih prompt'ları</b> alınır (araç çıktısı, sistem mesajı, skill enjeksiyonu dışlanır). Ham metin <b>değiştirilmez</b>; append-only; tekil anahtar = kaynak uuid.<br><span class="mono small">veri/bronz/prompt-olay.jsonl</span></p></div>
<div class="arrow">→</div>
<div class="card"><h3>SİLVER · 1:1, tipli, tekil, test edilmiş</h3><p>Zaman UTC/TR'ye çevrilir, oturum sırası verilir, tür sınıflandırılır (heuristik, deneysel), sonraki asistanın modeli + tetiklenen skill eklenir. Şekil-sözleşmesi + 3 test: <b>unique · not_null · accepted_values → PASS</b>.<br><span class="mono small">baglam.sqlite → prompt · veri/sozlesme/prompt.json</span></p></div>
<div class="arrow">→</div>
<div class="card"><h3>GOLD · tek tanım, iş sorusu</h3><p>"Son 50 prompt" tek bir SQL görünümünde tanımlı; CSV + bu sunum ondan türer. Agregasyon (tür dağılımı) yalnız burada.<br><span class="mono small">v_son_50_prompt · veri/gorunum/v_son_50_prompt.csv</span></p></div>
</div>
<p class="muted" style="margin-top:1em">Üretici: <span class="mono">tools/prompt-tablo.py</span> (stdlib; deterministik — aynı transkript + aynı kod → aynı tablo). Hat: <span class="mono">tools/katman-hatti.py</span>. Yakalanan iki hata: çatal-oturumlarda aynı uuid'li prompt tekrarı (→ bronz tekilleştirme) · sistem-enjekte "Continue…/Usage limit" mesajları (→ filtre).</p>
</section>

<section class="slide">
<div class="kicker">tablo</div>
<h2>Son 50 prompt (en yeni üstte)</h2>
<div class="tablewrap" id="tw"><table>
<thead><tr><th>#</th><th>tarih</th><th class="hide-m">saat</th><th class="hide-m">oturum</th><th class="hide-m">sıra</th><th>tür</th><th class="hide-s">tetiklenen skill</th><th class="hide-m">model</th><th class="hide-m">kar</th><th>prompt (kısa)</th></tr></thead>
<tbody>{tr}</tbody></table></div>
<div class="foot">Kolonlar: oturum = transkript kimliği (ilk 8) · sıra = o oturumdaki kaçıncı prompt · tür = heuristik sınıf · model = prompt'a cevap veren asistan modeli · kar = karakter · tam metin silver tablosunda. Dar ekranda oturum/sıra/model/kar gizlidir; tablo yana ve aşağı kaydırılabilir.</div>
</section>

<section class="slide">
<div class="kicker">okuma</div>
<h2>Son 50'de ne görünüyor</h2>
<div class="grid">
<div class="card"><h3>Tür dağılımı</h3><ul style="margin:0;padding-left:1.1em">{tur_html}</ul></div>
<div class="card"><h3>Ne anlatıyor</h3><p>Komutların çoğu <b>emir</b> ("araştır / atlasları koş / entegre et") ve <b>onay/devam</b> — yönetim ritmi: emir ver → koşum → onayla. "durdur" satırları limit/hesap kesintilerini işaretler; açılış/kapanış satırları vardiya sınırlarını verir.</p></div>
<div class="card"><h3>Sınırlar (dürüstlük)</h3><p>Tür sınıflandırması kural-tabanlı ve <b>deneysel</b>; "diğer" kovası var. Yalnız jarvis oturumları (staj dizini taranmadı). Model alanı ilk asistan cevabının modelidir. Sayılar m.39 damgalı: kaynağı transkript, üretim anı HEAD SHA.</p></div>
<div class="card"><h3>Sonraki adım</h3><p>Aynı hat her seans kapanışında yeniden koşar (yeni prompt'lar bronza <b>eklenir</b>, tablo ve bu sunum yeniden türer). Tür sözlüğü 3 koşumdan sonra ölçümle kalibre edilir.</p></div>
</div>
</section>

</div>
<div class="nav"><button id="prev" aria-label="önceki">‹ geri</button><span class="pos" id="pos"></span><button id="next" aria-label="sonraki">ileri ›</button></div>
<script>
(function(){{
const s=[...document.querySelectorAll('.slide')];let i=0;const pos=document.getElementById('pos');
function go(k){{i=Math.max(0,Math.min(s.length-1,k));s.forEach((e,j)=>e.classList.toggle('on',j===i));pos.textContent=(i+1)+' / '+s.length;s[i].scrollTop=0;}}
document.getElementById('prev').onclick=()=>go(i-1);document.getElementById('next').onclick=()=>go(i+1);
document.addEventListener('keydown',e=>{{if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown'){{e.preventDefault();go(i+1);}}if(e.key==='ArrowLeft'||e.key==='PageUp'){{e.preventDefault();go(i-1);}}}});
let sx=0,sy=0,inTable=false;
const deck=document.getElementById('deck');
deck.addEventListener('touchstart',e=>{{const t=e.touches[0];sx=t.clientX;sy=t.clientY;inTable=!!e.target.closest('.tablewrap');}},{{passive:true}});
deck.addEventListener('touchend',e=>{{if(inTable)return;const t=e.changedTouches[0];const dx=t.clientX-sx,dy=t.clientY-sy;if(Math.abs(dx)>60&&Math.abs(dx)>Math.abs(dy)*1.5){{go(dx<0?i+1:i-1);}}}},{{passive:true}});
go(0);
}})();
</script></body></html>"""
    outdir = os.path.join(R, "raporlar", tarih[:7]); os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, "son-50-prompt-SUNUM.html")  # ad arama anahtarıyla BAŞLAR (Spotlight ilk sonuç); tarih dosyanın içinde ve dizininde
    open(out, "w", encoding="utf-8").write(page)
    print(out, len(page.encode()), "bytes;", len(rows), "satır")


if __name__ == "__main__":
    main()
