"""Masa gündemi md → Lavish HTML yüzeyi (deterministik, LLM yok).
Kullanım: python3 masa_html.py <gundem.md> <cikti.html>
Yapı: '### ' başlıkları kart olur; '- **(x) ...**' satırları seçenek satırı; '(a) ÖNERİLEN' vurgulanır."""
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

def opt_html(o):
    txt = re.sub(r"^(- |\d+\. )", "", o)
    rec = "ÖNERİLEN" in txt
    cls = "opt rec" if rec else "opt"
    # alt seçenekler '· (b) ...' ile aynı satırda olabilir → noktalarla ayır
    return f'<li class="{cls}">{inline(txt)}</li>'

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
@media (max-width:600px){{main{{padding:14px 10px}} .card{{padding:10px 12px}}}}
</style></head><body><main>
<h1>{html.escape(head or 'Masa')}</h1>
<p class="hint">Yeşil kutu = önerilen. Her kalemde hükmünü kutuya not olarak yaz (a/b/c ya da kendi cümlen); "Send &amp; End" ile bana döner. Kaynak md: <code>{html.escape(src)}</code></p>"""]
for p in pre:
    out.append(f'<div class="pre">{inline(p)}</div>')
for c in cards:
    tag = "h2" if c["level"] == 2 else "h3"
    out.append(f'<section class="card"><{tag}>{inline(c["title"])}</{tag}>')
    for b in c["body"]:
        out.append(f'<p class="body">{inline(b)}</p>')
    if c["opts"]:
        out.append("<ul>" + "".join(opt_html(o) for o in c["opts"]) + "</ul>")
    out.append("</section>")
out.append("</main></body></html>")
open(dst, "w", encoding="utf-8").write("\n".join(out))
print("yazıldı", dst, len(cards), "kart")
