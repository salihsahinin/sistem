#!/usr/bin/env python3
"""atlas-derle.py — m.40b Workflow koşumunun HAM yapısal çıktısını (journal.jsonl + ajan transkriptleri) MEKANİK
rapor dosyasına derler (Jarvis yorumu YOK; sentez ayrı bölümde elle eklenir).

Kural kaynağı: .claude/skills/atlas-kosum/SKILL.md (adım 5 V26 KURAL-TABANLI seçim — Salih imzası 08-17; adım 6-7
hakem + D/K/X etiket) · core/ajan-metodolojisi.md §4 MODEL HİYERARŞİSİ (KB-02: tahmin↔gerçekleşen tablosu) ·
CLAUDE.md §2 okunabilirlik (üreten kaynak repoda; scratchpad derle.py'ler 08-16'da silinmişti — bu dosya kalıcı hâli).

Girdi (Workflow aracının oturum dizini):
  <wf-dizin>/journal.jsonl            — {"type":"result","agentId":..,"result":{...}} satırları (tez/antitez/V26/hakem)
  <wf-dizin>/agent-<id>.jsonl         — ajan transkripti (ilk user mesajı = prompt → aile+rol; usage → token; timestamp → süre)
  <wf-dizin>/agent-<id>.meta.json     — {"agentType","model"}
Aşama tespiti sonuç ANAHTARLARINDAN (deterministik): claims→tez · rebuttals→antitez · checks→V26 · verdicts→hakem.
Aile tespiti: prompt'taki "aile X" kalıbı; yoksa result.family baştaki büyük harfler.

Koş:
  python3 tools/atlas-derle.py --wf <wf-dizin> --emir cc/gorev/YYYY-MM/gorev-YYYY-MM-DD-N.md --cikti cc/rapor/YYYY-MM/rapor-YYYY-MM-DD-N.md \
      --baslik "Rapor başlığı" [--tahmin "rol:model:çıktı-token-tahmini" ...] [--sessiz]
Çıkış: 0 tamam · 2 girdi yok/okunamadı · 3 hiç result satırı yok (FAIL-LOUD).
stdlib-only, Python 3.9.
"""
import argparse, glob, json, os, re, sys
from datetime import datetime

STAGE_BY_KEY = (("claims", "tez"), ("rebuttals", "antitez"), ("checks", "v26"), ("verdicts", "hakem"))
STAGE_ORDER = {"tez": 0, "antitez": 1, "v26": 2, "hakem": 3}
STAGE_AD = {"tez": "TEZ", "antitez": "ANTİTEZ", "v26": "V26", "hakem": "HAKEM"}


def _url(s):
    return bool(re.match(r"^https?://", s or ""))


def _numeric(fig, txt):
    """V26 kural (b): sayısal iddia — figure rakam içerir ∨ metinde % / n= / × / pp kalıbı (JS ile birebir aynı)."""
    return bool(fig and fig != "-" and re.search(r"\d", fig)) or bool(re.search(r"\d+\s?%|\bn\s?=\s?\d|\d+\s?×|\d+\s?pp\b", txt or ""))


def v26_secim(items, id_of, txt_of, url_of, fig_of, uygun=None):
    """SKILL adım 5: (a) son üçte-birden ilk URL'li iddia + (b) TÜM sayısal (URL'li) iddialar. Rastgele YOK.
    uygun: opsiyonel süzgeç — antitezde ÇÜRÜTÜLEMEDİ satırları örnekleme GİRMEZ (¬T'yi destekleyen kaynak yok demek zaten
    antitezin beyanı; 'TUTMUYOR' orada halüsinasyon değil tutarlılık — 08-17 wf_bb445659 A ailesi bulgusu)."""
    if uygun is not None:
        items = [it for it in items if uygun(it)]
    picks, seen = [], set()

    def add(it, why):
        i = id_of(it)
        if i in seen:
            return
        seen.add(i)
        picks.append((i, why))
    n = len(items)
    if not n:
        return picks
    for it in items[(n * 2) // 3:]:
        if _url(url_of(it)):
            add(it, "son-üçte-bir")
            break
    for it in items:
        if _numeric(fig_of(it), txt_of(it)) and _url(url_of(it)):
            add(it, "sayısal")
    return picks


def oku_json_satirlar(yol):
    with open(yol, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def ajan_kunye(wf_dizin, agent_id):
    """transkriptten: prompt (ilk user), model, usage toplamları, araç sayısı, süre."""
    k = {"agent_id": agent_id, "prompt": "", "model": "-", "agentType": "-", "out": 0, "in": 0, "cache_cr": 0, "cache_rd": 0,
         "arac": 0, "sure_sn": None, "mesaj": 0}
    meta = os.path.join(wf_dizin, f"agent-{agent_id}.meta.json")
    if os.path.exists(meta):
        try:
            m = json.load(open(meta, encoding="utf-8"))
            k["agentType"] = m.get("agentType", "-"); k["model"] = m.get("model", "-") or "-"
        except Exception:
            pass
    tr = os.path.join(wf_dizin, f"agent-{agent_id}.jsonl")
    if not os.path.exists(tr):
        return k
    ts = []
    for o in oku_json_satirlar(tr):
        m = o.get("message")
        if not isinstance(m, dict):
            continue
        if o.get("timestamp"):
            ts.append(o["timestamp"])
        if m.get("role") == "user" and not k["prompt"]:
            c = m.get("content")
            if isinstance(c, str):
                k["prompt"] = c
            elif isinstance(c, list):
                k["prompt"] = " ".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text")
        if m.get("role") == "assistant":
            k["mesaj"] += 1
            u = m.get("usage") or {}
            k["out"] += u.get("output_tokens", 0) or 0
            k["in"] += u.get("input_tokens", 0) or 0
            k["cache_cr"] += u.get("cache_creation_input_tokens", 0) or 0
            k["cache_rd"] += u.get("cache_read_input_tokens", 0) or 0
            if m.get("model") and k["model"] in ("-", None):
                k["model"] = m["model"]
            if isinstance(m.get("content"), list):
                for b in m["content"]:
                    if isinstance(b, dict) and b.get("type") == "tool_use":
                        k["arac"] += 1
    if len(ts) >= 2:
        try:
            a = datetime.fromisoformat(ts[0].replace("Z", "+00:00")); b = datetime.fromisoformat(ts[-1].replace("Z", "+00:00"))
            k["sure_sn"] = round((b - a).total_seconds())
        except Exception:
            pass
    return k


def aile_bul(prompt, family_field):
    m = re.search(r"aile ([A-Z]{1,3})\s*[:\)—-]", prompt or "")
    if m:
        return m.group(1)
    m = re.match(r"\s*([A-Z]{1,3})\b", family_field or "")
    return m.group(1) if m else "?"


def stage_bul(result):
    for key, st in STAGE_BY_KEY:
        if key in result:
            return st
    return "?"


def md_kacir(s):
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()


def derle(wf_dizin, emir, cikti, baslik, tahminler, sessiz):
    journal = os.path.join(wf_dizin, "journal.jsonl")
    if not os.path.exists(journal):
        print(f"FAIL-LOUD: journal yok: {journal}"); sys.exit(2)
    sonuc = [o for o in oku_json_satirlar(journal) if o.get("type") == "result" and isinstance(o.get("result"), dict)]
    if not sonuc:
        print("FAIL-LOUD: journal'da result satırı yok"); sys.exit(3)
    aileler = {}
    kunye = []
    for o in sonuc:
        r = o["result"]; aid = o.get("agentId", "")
        k = ajan_kunye(wf_dizin, aid)
        st = stage_bul(r); fam = aile_bul(k["prompt"], r.get("family", ""))
        k.update({"aile": fam, "rol": st})
        kunye.append(k)
        aileler.setdefault(fam, {})[st] = r
    fam_keys = sorted(aileler.keys())
    wf_id = os.path.basename(os.path.normpath(wf_dizin))
    # --- toplamlar
    top = {"tez": 0, "itiraz": 0, "ek": 0, "v26": {"TUTUYOR": 0, "TUTMUYOR": 0, "ERİŞİLEMEDİ": 0},
           "sag": 0, "dar": 0, "dus": 0, "cel": 0}
    L = []
    L.append(f"# {baslik}\n")
    L.append(f"*Emir: `{emir}` · Koşum: Workflow `{wf_id}` — {len(fam_keys)} aile × (tez → CoVe-Factored antitez [yalnız iddia satırları, kodla] → "
             f"V26 KURAL-TABANLI örneklem [son üçte-bir + tüm sayısal; Salih 08-17] → taraf-maskeli hakem) = {len(kunye)} işçi. "
             f"Ham yapısal çıktıdan MEKANİK derlendi (`tools/atlas-derle.py`; Jarvis yorumu yok; sentez ayrı bölüm). D birincil · K ikincil · X doğrulanamadı.*\n")
    # --- koşum künyesi tablosu (KB-02 tahmin↔gerçek)
    L.append("## Koşum künyesi — rol × model (KB-02 model hiyerarşisi: tahmin yalnız alt modeller için; üst model yalnız ölçülür)")
    L.append("| aile | rol | model | araç | asistan mesaj | çıktı-token | yeni-girdi (input+cache_cr) | cache-okuma | süre (sn) | tahmin (emir) |")
    L.append("|---|---|---|---|---|---|---|---|---|---|")
    tah = {}
    for t in tahminler or []:
        p = t.split(":", 2)
        if len(p) == 3:
            tah[(p[0], p[1])] = p[2]
    tot_out = tot_in = tot_rd = tot_arac = 0
    for k in sorted(kunye, key=lambda x: (x["aile"], STAGE_ORDER.get(x["rol"], 9))):
        mdl = (k["model"] or "-").replace("claude-", "")
        tt = tah.get((k["rol"], mdl.split("-")[0]), tah.get((k["rol"], "*"), "—"))
        L.append(f"| {k['aile']} | {STAGE_AD.get(k['rol'], k['rol'])} | {mdl} | {k['arac']} | {k['mesaj']} | {k['out']} | {k['in'] + k['cache_cr']} | {k['cache_rd']} | {k['sure_sn'] if k['sure_sn'] is not None else '-'} | {tt} |")
        tot_out += k["out"]; tot_in += k["in"] + k["cache_cr"]; tot_rd += k["cache_rd"]; tot_arac += k["arac"]
    L.append(f"| **Σ** | | | **{tot_arac}** | | **{tot_out}** | **{tot_in}** | **{tot_rd}** | | |\n")
    # --- aile bölümleri (önce sayım için hazırla)
    fam_L = []
    for fam in fam_keys:
        F = aileler[fam]
        tez, anti, v26, hak = F.get("tez"), F.get("antitez"), F.get("v26"), F.get("hakem")
        title = (tez or anti or hak or {}).get("family", fam)
        fam_L.append(f"\n---\n\n# Aile {fam} — {md_kacir(title)}\n")
        # V26 sonuçları → hangi taraf düştü
        dusen_taraf = set()
        v26_map = {}
        curutulemedi = {"¬" + x["target_id"] for x in (anti or {}).get("rebuttals", []) if x.get("verdict") == "ÇÜRÜTÜLEMEDİ"}
        tutarli_not = {}
        if v26:
            for c in v26.get("checks", []):
                v26_map[c["claim_id"]] = c
                top["v26"][c.get("result", "ERİŞİLEMEDİ")] = top["v26"].get(c.get("result", "ERİŞİLEMEDİ"), 0) + 1
                if c.get("result") == "TUTMUYOR":
                    if c["claim_id"] in curutulemedi:
                        tutarli_not[c["claim_id"]] = "ÇÜRÜTÜLEMEDİ satırı: kaynak ¬T'yi desteklemiyor = antitezin kendi beyanı → TUTARLI, düşürme YOK"
                    else:
                        dusen_taraf.add("antitez" if c["claim_id"].startswith("¬") else "tez")
        if hak:
            sv = hak.get("survival", {})
            top["sag"] += sv.get("saglam", 0); top["dar"] += sv.get("daraldi", 0); top["dus"] += sv.get("dustu", 0); top["cel"] += sv.get("celiskili", 0)
            fam_L.append("## Hakem: mekanizmaya girecek yapı-taşları")
            fam_L.append("| # | Yapı-taşı | Yerleşim | Güven | Kaynak |")
            fam_L.append("|---|---|---|---|---|")
            for i, b in enumerate(hak.get("building_blocks", []), 1):
                yer = md_kacir(b.get('placement'))
                if b.get('jarvis'):  # gorev-2 tipi koşumlar: teknik-sınıfı + Jarvis-eşleme (kullanıyoruz-eş / kısmi / eksik-aday / girmez)
                    yer += f" · **{md_kacir(b.get('jarvis'))}**"
                fam_L.append(f"| {fam}-YT{i} | {md_kacir(b.get('block'))} | {yer} | {b.get('confidence', '-')} | {md_kacir(b.get('source_url'))} |")
            fam_L.append("\n## Hakem: çift-başına hüküm")
            fam_L.append("| İddia | Hüküm | Hayatta kalan önerme | Gerekçe |")
            fam_L.append("|---|---|---|---|")
            for v in hak.get("verdicts", []):
                fam_L.append(f"| {v.get('claim_id')} | {v.get('verdict')} | {md_kacir(v.get('surviving_form'))} | {md_kacir(v.get('reason'))} |")
            fam_L.append(f"\n**Hayatta-kalma (aile {fam}): SAĞLAM {sv.get('saglam', 0)} · DARALDI {sv.get('daraldi', 0)} · DÜŞTÜ {sv.get('dustu', 0)} · ÇELİŞKİLİ {sv.get('celiskili', 0)}**\n")
            fam_L.append("## Hakem: kör noktalar")
            for b in hak.get("blind_spots", []):
                fam_L.append(f"- {b}")
        else:
            fam_L.append("## Hakem: (ÇIKTI YOK — koşum eksik; done-yüklemi SAĞLANMADI)")
        # V26
        fam_L.append("\n## V26 örneklem denetimi (KURAL-TABANLI seçim; TUTMUYOR ⇒ o tarafın tüm iddiaları K)")
        secim = []
        if tez:
            secim += [(i, w, "tez") for i, w in v26_secim(tez.get("claims", []), lambda c: c["id"], lambda c: c["claim"], lambda c: c.get("source_url"), lambda c: c.get("figure"))]
        if anti:
            secim += [(i, w, "antitez") for i, w in v26_secim(anti.get("rebuttals", []), lambda x: "¬" + x["target_id"], lambda x: x["negation"], lambda x: x.get("evidence_url"), lambda x: x.get("figure"), uygun=lambda x: x.get("verdict") != "ÇÜRÜTÜLEMEDİ")]
            # koşumda (eski script) ÇÜRÜTÜLEMEDİ satırları da denetlenmişse tabloda görünsün — tutarlılık notuyla
            for cid in curutulemedi:
                if cid in v26_map and not any(cid == s_[0] for s_ in secim):
                    secim.append((cid, "eski-kural (ÇÜRÜTÜLEMEDİ — sayılmaz)", "antitez"))
        if secim:
            fam_L.append("| iddia | taraf | seçim kuralı | sonuç | not |")
            fam_L.append("|---|---|---|---|---|")
            for cid, why, taraf in secim:
                c = v26_map.get(cid, {})
                notu = md_kacir(c.get('note', '-'))
                if cid in tutarli_not:
                    notu = "**" + tutarli_not[cid] + "** — " + notu
                fam_L.append(f"| {cid} | {taraf} | {why} | {c.get('result', 'DENETLENMEDİ')} | {notu} |")
        else:
            fam_L.append("- seçilebilir (URL'li) iddia yok")
        if dusen_taraf:
            fam_L.append(f"\n**⚠ V26 TUTMUYOR: {', '.join(sorted(dusen_taraf))} tarafının bu ailedeki TÜM iddiaları K'ya düşer (SKILL adım 5).**")
        # sayısal ama URL'siz iddialar (KAYNAKSIZ damgası)
        if tez:
            ks = [c["id"] for c in tez.get("claims", []) if _numeric(c.get("figure"), c.get("claim")) and not _url(c.get("source_url"))]
            if ks:
                fam_L.append(f"- Sayısal ama URL'siz tez iddiaları (KAYNAKSIZ → K/[?]): {', '.join(ks)}")
        # tez
        if tez:
            top["tez"] += len(tez.get("claims", []))
            fam_L.append(f"\n## Tez iddiaları (bütçe: {md_kacir(tez.get('budget_note', '-'))})")
            fam_L.append("| id | iddia | etiket | rakam | kapsam | yerleşim önerisi | kaynak |")
            fam_L.append("|---|---|---|---|---|---|---|")
            for c in tez.get("claims", []):
                lab = c.get("label", "-")
                if "tez" in dusen_taraf and lab == "D":
                    lab = "K (V26)"
                fam_L.append(f"| {c.get('id')} | {md_kacir(c.get('claim'))} | {lab} | {md_kacir(c.get('figure'))} | {md_kacir(c.get('scope'))} | {md_kacir(c.get('placement_suggestion', c.get('schema_suggestion', '-')))} | {md_kacir(c.get('source_url'))} |")
            if tez.get("gaps"):
                fam_L.append("\n**Tezin boşlukları (aranıp bulunamayan):** " + " · ".join(md_kacir(g) for g in tez["gaps"]))
            if tez.get("access_blocks"):
                fam_L.append("\n**Erişim engelleri:** " + " · ".join(md_kacir(g) for g in tez["access_blocks"]))
        else:
            fam_L.append("\n## Tez iddiaları: (ÇIKTI YOK)")
        # antitez
        if anti:
            top["itiraz"] += len(anti.get("rebuttals", [])); top["ek"] += len(anti.get("extra_counter_claims", []))
            fam_L.append(f"\n## Antitez itirazları (bütçe: {md_kacir(anti.get('budget_note', '-'))})")
            fam_L.append("| hedef | ¬T | öz-hüküm | rakam | kanıt | not |")
            fam_L.append("|---|---|---|---|---|---|")
            for x in anti.get("rebuttals", []):
                fam_L.append(f"| {x.get('target_id')} | {md_kacir(x.get('negation'))} | {x.get('verdict')} | {md_kacir(x.get('figure'))} | {md_kacir(x.get('evidence_url'))} | {md_kacir(x.get('note'))} |")
            if anti.get("extra_counter_claims"):
                fam_L.append("\n**Ek karşı-bulgular (tezde olmayan):**")
                fam_L.append("| id | iddia | etiket | rakam | kapsam | yerleşim | kaynak |")
                fam_L.append("|---|---|---|---|---|---|---|")
                for c in anti["extra_counter_claims"]:
                    fam_L.append(f"| {c.get('id')} | {md_kacir(c.get('claim'))} | {c.get('label')} | {md_kacir(c.get('figure'))} | {md_kacir(c.get('scope'))} | {md_kacir(c.get('placement_suggestion', c.get('schema_suggestion', '-')))} | {md_kacir(c.get('source_url'))} |")
        else:
            fam_L.append("\n## Antitez itirazları: (ÇIKTI YOK)")
    # --- sayım bloğu
    L.append("## Koşum sayımı")
    L.append(f"- Tez iddiası: {top['tez']} · itiraz: {top['itiraz']} · ek karşı-bulgu: {top['ek']}")
    L.append(f"- **Hayatta-kalma: SAĞLAM {top['sag']} · DARALDI {top['dar']} · DÜŞTÜ {top['dus']} · ÇELİŞKİLİ {top['cel']}** (aile başına yukarıda)")
    v = top["v26"]
    L.append(f"- V26 (kural-tabanlı): {sum(v.values())} denetim → TUTUYOR {v.get('TUTUYOR', 0)} · TUTMUYOR {v.get('TUTMUYOR', 0)} · ERİŞİLEMEDİ {v.get('ERİŞİLEMEDİ', 0)}")
    eksik = [f for f in fam_keys if "hakem" not in aileler[f]]
    L.append(f"- Done-yüklemi (∀ aile: tez∧antitez∧V26∧hakem): {'SAĞLANDI' if not eksik else 'SAĞLANMADI — eksik hakem: ' + ','.join(eksik)}")
    L.extend(fam_L)
    L.append("\n---\n\n## Sentez (Jarvis yorumu — mekanik derlemenin DIŞINDA; elle eklenir)\n\n_(bekliyor)_\n")
    metin = "\n".join(L) + "\n"
    os.makedirs(os.path.dirname(cikti) or ".", exist_ok=True)
    with open(cikti, "w", encoding="utf-8") as f:
        f.write(metin)
    if not sessiz:
        print(f"derlendi → {cikti} ({len(metin.encode('utf-8'))} B) · aileler {','.join(fam_keys)} · işçi {len(kunye)} · "
              f"hayatta-kalma {top['sag']}/{top['dar']}/{top['dus']}/{top['cel']} · V26 {v}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--wf", required=True, help="Workflow oturum dizini (journal.jsonl + agent-*.jsonl)")
    ap.add_argument("--emir", required=True); ap.add_argument("--cikti", required=True); ap.add_argument("--baslik", required=True)
    ap.add_argument("--tahmin", action="append", help="rol:model:tahmin (KB-02; ör. tez:opus:'10-15k çıktı')")
    ap.add_argument("--sessiz", action="store_true")
    a = ap.parse_args()
    sys.exit(derle(a.wf, a.emir, a.cikti, a.baslik, a.tahmin, a.sessiz))


if __name__ == "__main__":
    main()
