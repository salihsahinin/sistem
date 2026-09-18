#!/usr/bin/env python3
"""karar-masasi · deterministik masa üretici (İB-88 P1, Karar 96; deneysel m.29).
Girdi: kalem spec'i (JSON, şema SKILL.md'de). Çıktı: DaisyUI karar masası HTML (7.-12. masa biçimi) +
kalıcı kopya. Aynı spec → aynı HTML (rastgelelik yok). Kanona yazmaz.

Kullanım: python3 masa-uret.py <spec.json> [--repo ~/jarvis] [--kuru]   (--kuru: dosya yazmaz, doğrulama basar)
P2 (İB-88, 09-15): opsiyonel `giris` alanı (tetik öncesi giriş cümlesi); test `masa-uret-test.py` (E1-E3, masa-12 eşdeğerlik);
eski masayı spec'e döken tersine araç `masa-spec-cikar.py`.
Çıkış kodları: 0 üretildi · 2 spec hatası (öneri ilk sırada değil, kalem id çift, zorunlu alan eksik) · 3 masa no çakışması
"""
import argparse, html, json, pathlib, re, sys

SABLON = pathlib.Path(__file__).resolve().parent.parent / "sablon.html"

def e(s):  # HTML kaçış; <strong>/<code> gibi güvenli etiketlere izin (spec yazarı Jarvis)
    return s if re.search(r"</?(strong|code|em|br)\b", s or "") else html.escape(s or "")

def dogrula(spec):
    hatalar = []
    for z in ("no", "tarih", "baslik", "tetik", "kalemler"):
        if z not in spec: hatalar.append(f"zorunlu alan eksik: {z}")
    idler = [k.get("id") for k in spec.get("kalemler", [])]
    if len(idler) != len(set(idler)): hatalar.append("kalem id çift")
    for k in spec.get("kalemler", []):
        sec = k.get("secenekler", [])
        if not sec: hatalar.append(f"{k.get('id')}: seçenek yok")
        oneri = [i for i, s in enumerate(sec) if s.get("oneri")]
        if oneri and oneri[0] != 0: hatalar.append(f"{k.get('id')}: önerilen seçenek ilk sırada değil (m.40 eki)")
        for s in sec:
            if not s.get("value"): hatalar.append(f"{k.get('id')}: value boş")
    return hatalar

def kalem_html(k):
    coklu = bool(k.get("coklu"))
    fn = "kuyruklaCoklu" if coklu else "kuyrukla"
    tip = "checkbox" if coklu else "radio"
    sec = []
    for s in k["secenekler"]:
        cls = "opt oneri" if s.get("oneri") else "opt"
        sec.append(f'''        <label class="{cls} block p-3 rounded bg-base-200 cursor-pointer"><input type="{tip}" name="secim" value="{html.escape(s["value"])}"> <strong>{e(s["etiket"])}</strong>
          <div class="text-sm opacity-80 mt-1">{e(s.get("aciklama", ""))}</div></label>''')
    buton = "Seçimi kuyruğa yaz" if coklu else "Beyanı kuyruğa yaz"
    return f'''
  <!-- {k["id"]} -->
  <section class="card bg-base-100 shadow-md" data-lavish-question="{k["id"]}">
    <div class="card-body">
      <h2 class="card-title">{k["id"]} · {e(k["baslik"])} <span class="badge badge-outline">{e(k.get("rozet", ""))}</span></h2>
      <p class="text-sm opacity-80"><strong>Ne demek:</strong> {e(k.get("ne_demek", ""))}</p>
      <form onsubmit="event.preventDefault(); {fn}(this,'{k["id"]}',{html.escape(json.dumps(k["baslik"][:40], ensure_ascii=False), quote=True)});">
      <div class="space-y-2">
{chr(10).join(sec)}
      </div>
      <button type="submit" class="btn btn-primary btn-sm mt-3">{buton}</button> <span class="text-xs opacity-60 durum"></span>
      </form>
    </div>
  </section>'''

def uret(spec):
    kanit = "".join(f'          <tr><td>{e(r["bulgu"])}</td><td>{e(r["deger"])}</td><td>{e(r.get("kaynak",""))} · <strong>{e(r.get("etiket",""))}</strong></td></tr>\n' for r in spec.get("kanit", []))
    hakem = f'''
  <section class="card bg-base-100 shadow-md hakem"><div class="card-body"><h2 class="card-title text-lg">Hakem / kanıt notu</h2><p class="text-sm opacity-80">{e(spec["hakem"])}</p></div></section>''' if spec.get("hakem") else ""
    kalemler = "".join(kalem_html(k) for k in spec["kalemler"])
    n = len(spec["kalemler"])
    sablon = SABLON.read_text(encoding="utf-8")
    return (sablon.replace("{{NO}}", str(spec["no"])).replace("{{TARIH}}", spec["tarih"]).replace("{{BASLIK}}", e(spec["baslik"]))
            .replace("{{N}}", str(n)).replace("{{GIRIS}}", e(spec.get("giris", ""))).replace("{{TETIK}}", e(spec["tetik"])).replace("{{ONCE}}", e(spec.get("once_yapildi", "—")))
            .replace("{{ASOF}}", e(spec.get("asof", ""))).replace("{{KANIT}}", kanit).replace("{{HAKEM}}", hakem)
            .replace("{{KALEMLER}}", kalemler).replace("{{KARAR_NO}}", e(spec.get("karar_no", "sonraki Karar")))
            .replace("{{KAYNAK_HTML}}", f"kaynak-kodu/lavish/masa-{spec['no']}-{spec['tarih']}.html")
            .replace("{{KALICI}}", f"raporlar/masa/masa-{spec['no']}-karar-yuzeyi-{spec['tarih']}.html"))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("spec"); ap.add_argument("--repo", default=str(pathlib.Path.home() / "jarvis")); ap.add_argument("--kuru", action="store_true")
    a = ap.parse_args(); repo = pathlib.Path(a.repo)
    spec = json.load(open(a.spec, encoding="utf-8"))
    hatalar = dogrula(spec)
    if hatalar:
        print("SPEC HATASI: " + " · ".join(hatalar)); sys.exit(2)
    kalici = repo / "raporlar" / "masa" / f"masa-{spec['no']}-karar-yuzeyi-{spec['tarih']}.html"
    calisma = repo / "kaynak-kodu" / "lavish" / f"masa-{spec['no']}-{spec['tarih']}.html"
    mevcut = sorted(repo.glob("raporlar/masa/masa-*-karar-yuzeyi-*.html"))
    if not a.kuru and kalici.exists() and not spec.get("ustune_yaz"):
        print(f"MASA NO ÇAKIŞMASI: {kalici} var (ustune_yaz: true ile geç)"); sys.exit(3)
    metin = uret(spec)
    form_n = metin.count("data-lavish-question=")
    if a.kuru:
        print(f"kuru: {len(metin)} B · kalem {len(spec['kalemler'])} · form {form_n} · mevcut masa {len(mevcut)}"); return
    calisma.parent.mkdir(parents=True, exist_ok=True); kalici.parent.mkdir(parents=True, exist_ok=True)
    calisma.write_text(metin, encoding="utf-8"); kalici.write_text(metin, encoding="utf-8")
    print(f"üretildi: {calisma}\nkalıcı: {kalici}\nkalem {len(spec['kalemler'])} · form {form_n} · {len(metin)} B")

if __name__ == "__main__":
    main()
