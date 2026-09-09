"""Masa gündemi md → Lavish HTML yüzeyi (deterministik, LLM yok).
Kullanım: python3 tools/masa-html.py <gundem.md> <cikti.html>
Yapı: '### ' başlıkları kart olur; '- **(x) ...**' satırları seçenek satırı; '(a) ÖNERİLEN' vurgulanır.
v0.2 (09-08, 9. masa; Lavish 'input' playbook): her kartta radyo (seçenek harfi) + not alanı + "Hükmü kuyruğa al"
düğmesi → window.lavish.queuePrompt TEK çağrı (radyo değişimi kuyruğa YAZMAZ). Lavish yoksa (dosya doğrudan
açıldıysa) düğme hükmü panoya kopyalar. Karar 87 masa-aracı notu: hüküm ancak "Send to Agent" ile ajana düşer."""
import re, sys, html

src, dst = sys.argv[1], sys.argv[2]
md = open(src, encoding="utf-8").read()

def inline(s):
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    return s

cards, head, pre = [], None, []
cur = None
for line in md.split("\n"):
    if line.startswith("# "):
        head = line[2:].strip(); continue
    if line.startswith("### ") or line.startswith("## "):
        cur = {"title": line.lstrip("# ").strip(), "body": [], "opts": [], "level": 3 if line.startswith("### ") else 2}
        cards.append(cur); continue
    if cur is None:
        if line.strip(): pre.append(line)
        continue
    if line.startswith("- ") or re.match(r"^\d+\. ", line):
        cur["opts"].append(line)
    elif line.strip():
        cur["body"].append(line)

def opt_letter(txt):
    m = re.match(r"^\**\((\w)\)", txt)
    return m.group(1) if m else None

def opt_html(o, qid):
    txt = re.sub(r"^(- |\d+\. )", "", o)
    rec = "ÖNERİLEN" in txt
    cls = "opt rec" if rec else "opt"
    let = opt_letter(txt)
    radio = f'<input type="radio" name="{qid}" value="{let}"> ' if let else ""
    return f'<li class="{cls}"><label>{radio}{inline(txt)}</label></li>'

out = [f"""<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(head or 'Masa')}</title>
<style>
:root{{--bg:#f6f4ee;--card:#fff;--ink:#1d1d1b;--mute:#5d5b55;--line:#dcd8cc;--rec:#e8f3e5;--recb:#3e7a3a;--acc:#8a4b1f}}
body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}}
main{{max-width:980px;margin:0 auto;padding:24px 18px 80px}}
h1{{font-size:22px;margin:0 0 8px}} .pre{{color:var(--mute);font-size:13px;border-left:3px solid var(--line);padding:6px 12px;margin:10px 0}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 18px;margin:16px 0}}
.card h2{{font-size:17px;margin:0 0 6px;color:var(--acc)}} .card h3{{font-size:16px;margin:0 0 6px}}
.body{{color:var(--mute);font-size:14px;margin:0 0 8px}}
ul{{list-style:none;padding:0;margin:0}} .opt{{padding:8px 10px;border:1px solid var(--line);border-radius:8px;margin:6px 0;font-size:14px}}
.opt.rec{{background:var(--rec);border-color:var(--recb)}} code{{background:#efece3;padding:0 4px;border-radius:4px;font-size:13px}}
.hint{{font-size:13px;color:var(--mute);margin:0 0 14px}}
.opt label{{display:block;cursor:pointer}} .opt input{{margin-right:6px}}
.hukum{{display:flex;gap:8px;margin-top:8px;flex-wrap:wrap}} .hukum textarea{{flex:1;min-width:200px;min-height:34px;font:13px/1.4 inherit;border:1px solid var(--line);border-radius:6px;padding:4px 8px}}
.hukum button{{background:var(--acc);color:#fff;border:0;border-radius:6px;padding:6px 12px;font-size:13px;cursor:pointer}} .hukum .ok{{font-size:12px;color:var(--recb);align-self:center}}
@media (max-width:600px){{main{{padding:14px 10px}} .card{{padding:10px 12px}}}}
</style></head><body><main>
<h1>{html.escape(head or 'Masa')}</h1>
<p class="hint">Yeşil kutu = önerilen. Her kalemde radyoyu seç ve/veya not yaz, sonra <b>Hükmü kuyruğa al</b>; kuyruk yalnız "Send to Agent" / "Send &amp; End" ile bana düşer (Karar 87 araç notu). Kaynak md: <code>{html.escape(src)}</code></p>
<script>
function hukum(f,qid){{const fd=new FormData(f);const sec=fd.get('sec')||'';const not=(fd.get('not')||'').trim();
 if(!sec&&!not){{return}}const metin=qid+' hükmü: '+(sec?'('+sec+')':'')+(not?' '+not:'');
 if(window.lavish&&window.lavish.queuePrompt){{window.lavish.queuePrompt(metin,{{tag:'hukum',text:metin,element:f,queueKey:qid,data:{{kalem:qid,secenek:sec,not:not}}}});}}
 else{{navigator.clipboard&&navigator.clipboard.writeText(metin);}}
 const ok=f.querySelector('.ok');ok.textContent='kuyrukta: '+metin;}}
</script>"""]
for p in pre:
    out.append(f'<div class="pre">{inline(p)}</div>')
for c in cards:
    tag = "h2" if c["level"] == 2 else "h3"
    out.append(f'<section class="card"><{tag}>{inline(c["title"])}</{tag}>')
    for b in c["body"]:
        out.append(f'<p class="body">{inline(b)}</p>')
    qid = c["title"].split(" · ")[0].strip() if " · " in c["title"] else None
    if c["opts"] and qid and c["level"] == 3:
        out.append(f'<form data-lavish-question="{html.escape(qid)}" onsubmit="event.preventDefault();hukum(this,\'{html.escape(qid)}\')">')
        out.append("<ul>" + "".join(opt_html(o, "sec") for o in c["opts"]) + "</ul>")
        out.append('<div class="hukum"><textarea name="not" placeholder="not / kendi cümlen (isteğe bağlı)"></textarea><button type="submit">Hükmü kuyruğa al</button><span class="ok"></span></div></form>')
    elif c["opts"]:
        out.append("<ul>" + "".join(opt_html(o, None) for o in c["opts"]) + "</ul>")
    out.append("</section>")
out.append("</main></body></html>")
open(dst, "w", encoding="utf-8").write("\n".join(out))
print("yazıldı", dst, len(cards), "kart")
