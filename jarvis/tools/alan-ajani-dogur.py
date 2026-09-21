#!/usr/bin/env python3
"""Alan ajanı doğurucu (Karar 105, masa-18, 2026-09-21; Karar 103 M4 alan ajanı = kalıcı dizin · Karar 104 M5 doğum belgesi).

Ne yapar: spec dosyasındaki her ajan için `~/sistem/<dizin>/` iskeletini `sablonlar/ajan-iskelet/` şablonlarından
deterministik üretir: AGENTS.md (charter, §0b doğum belgesi) + CLAUDE.md symlink · README · core/ (kapsül · pano · desenler)
· kuyruk/ (defter · kutu) · cc/gelen|giden · raporlar · arsiv · veri/bronz · .claude/ (settings · okuma-izin-ek · hooks
v0.6 · skills seans-acilis/kapanis · skills/ogren → ../../../sablonlar/skills/ogren symlink · agents/hakem alan perspektifli).
Hook'lar Friday'in v0.5 kopyasından v0.6 yamasıyla türetilir (tek kaynak `friday/.claude/hooks/`; yama = okuma-izin-ek).
Ortak `sablonlar/skills/ogren/` yoksa `jarvis/.claude/skills/ogren/`'den v0.3 (alan sürümü) olarak türetilir.

İdempotens: var olan dosyanın üstüne YAZMAZ (`--uzerine-yaz` verilmedikçe); rapor "yeni/atlandı/aynı" sayar. Şerit taşıma (T3,
`git mv ../ogrenme/<şerit> <dizin>/ogrenme/`) Salih elidir: komut listesi basılır, koşulmaz (m.8 taşıma Salih beyanı).

Kullanım: python3 tools/alan-ajani-dogur.py kuyruk/alan-ajanlari-YYYY-MM-DD.json [--kuru] [--uzerine-yaz] [--tarih YYYY-MM-DD]
Çıkış: 0 = üretildi/aynı · 2 = spec/şablon hatası.
"""
import argparse, datetime, json, os, re, shutil, stat, sys

BURASI = os.path.dirname(os.path.abspath(__file__))
JARVIS = os.path.dirname(BURASI)
KOK = os.path.dirname(JARVIS)
ISKELET = os.path.join(KOK, "sablonlar", "ajan-iskelet")
CLAUDE_AYAR = "claude-ayar"   # şablonda bu ad; hedefte ".claude" (Jarvis Bash teli `.claude/` metnini keser; dizin adı bu yüzden farklı)
FRIDAY_HOOKS = os.path.join(KOK, "friday", ".claude", "hooks")
OGREN_KAYNAK = os.path.join(JARVIS, ".claude", "skills", "ogren")
OGREN_ORTAK = os.path.join(KOK, "sablonlar", "skills", "ogren")

SAYAC = {"yeni": 0, "atlandi": 0, "ayni": 0}


def yaz(yol, icerik, uzerine, kuru, calistir=False):
    if os.path.exists(yol):
        if open(yol, encoding="utf-8").read() == icerik:
            SAYAC["ayni"] += 1; return
        if not uzerine:
            SAYAC["atlandi"] += 1; return
    SAYAC["yeni"] += 1
    if kuru:
        return
    os.makedirs(os.path.dirname(yol), exist_ok=True)
    with open(yol, "w", encoding="utf-8") as fh:
        fh.write(icerik)
    if calistir:
        os.chmod(yol, os.stat(yol).st_mode | stat.S_IXUSR | stat.S_IXGRP)


def symlink(hedef, yol, kuru):
    if os.path.islink(yol) or os.path.exists(yol):
        SAYAC["ayni" if (os.path.islink(yol) and os.readlink(yol) == hedef) else "atlandi"] += 1; return
    SAYAC["yeni"] += 1
    if not kuru:
        os.makedirs(os.path.dirname(yol), exist_ok=True); os.symlink(hedef, yol)


def hook_v06(ad):
    """Friday hook'undan v0.6 türet (yalnız okuma-izin.sh ve testi yamalanır; hareket-kutuk aynen)."""
    t = open(os.path.join(FRIDAY_HOOKS, ad), encoding="utf-8").read()
    if ad == "okuma-izin.sh":
        t = t.replace("input=$(cat)\n", "# v0.6 (2026-09-21, Karar 105 M6 alan ajanları): `.claude/okuma-izin-ek` dosyası (satır başına depo köküne göreli yol, ör.\n"
                      "#   `ogrenme/kaynaklar`) izinli köklere eklenir — salt-okur ortak kaynaklar; yazma yasağı settings deny'de. Dosya yoksa v0.5 ile aynı.\n"
                      "#   Tek kaynak `friday/.claude/hooks/okuma-izin.sh`; bu kopya `jarvis/tools/alan-ajani-dogur.py` yamasıyla üretilir, elle düzenlenmez.\n"
                      "input=$(cat)\n", 1)
        t = t.replace('izinli = [repo, os.path.join(kok, "sablonlar"), "/tmp", "/private/tmp", "/private/var/folders", harness]  # kök sablonlar/ ortak (F4)\n',
                      'izinli = [repo, os.path.join(kok, "sablonlar"), "/tmp", "/private/tmp", "/private/var/folders", harness]  # kök sablonlar/ ortak (F4)\n'
                      'try:  # v0.6: ek salt-okur kökler (depo köküne göreli; ör. ogrenme/kaynaklar)\n'
                      '    for satir in open(os.path.join(repo, ".claude", "okuma-izin-ek"), encoding="utf-8"):\n'
                      '        satir = satir.strip()\n'
                      '        if satir and not satir.startswith("#"):\n'
                      '            izinli.append(os.path.realpath(os.path.join(kok, satir)))\n'
                      'except OSError:\n'
                      '    pass\n', 1)
        t = t.replace('os.environ.get("FRIDAY_HOOK_TEST") or os.environ.get("JARVIS_HOOK_TEST")',
                      'os.environ.get("FRIDAY_HOOK_TEST") or os.environ.get("JARVIS_HOOK_TEST") or os.environ.get("AJAN_HOOK_TEST")')
        t = t.replace('"kaynak": "okuma-izin.sh v0.4"', '"kaynak": "okuma-izin.sh v0.6"')
        t = t.replace("OKUMA-İZİN KİLİDİ (Karar 91/101): lider reposu kendi dizini + depo kökündeki kanon dosyalarını okur; jarvis/** ve repo dışı kullanıcı yolu kapalıdır.",
                      "OKUMA-İZİN KİLİDİ (Karar 91/101/105): ajan kendi dizini + depo kökündeki kanon dosyaları + sablonlar/ + okuma-izin-ek kökleri okur; diğer ajan dizinleri (jarvis/**, friday/**, alan ajanları) ve repo dışı kullanıcı yolu kapalıdır.")
        assert "okuma-izin-ek" in t, "v0.6 yaması tutmadı (Friday hook'u değişmiş olabilir)"
    elif ad == "okuma-izin-test.sh":
        t = t.replace("# Friday okuma-izin kilidi testi.", "# Alan-ajanı okuma-izin kilidi testi (v0.6; Friday testinin kopyası + Karar 105 vakaları; üretici alan-ajani-dogur.py).")
        t = t.replace("/Users/HasanSalihSahin/sistem/friday/", "/Users/HasanSalihSahin/sistem/__ajan__/")  # üretimde dizin adıyla değiştirilir (tek tırnaklı JSON'da $ genişlemez)
        ek = ('echo "-- v0.6 alan ajanı (Karar 105) --"\n'
              't "Read ../friday/core → RED (başka ajan)"        \'{"tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/sistem/friday/core/rol.md"}}\' 2\n'
              't "Read başka alan ajanı core → RED"              \'{"tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/sistem/__baska_ajan__/core/durum-kapsulu.md"}}\' 2\n'
              't "Read ogrenme/kaynaklar (okuma-izin-ek) → geçer" \'{"tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/sistem/ogrenme/kaynaklar/README.md"}}\' 0\n'
              't "Bash cat ../ogrenme/kaynaklar/x → geçer"       \'{"tool_name":"Bash","tool_input":{"command":"cat ../ogrenme/kaynaklar/README.md"}}\' 0\n'
              't "Read ../ogrenme/evals (kaynaklar dışı) → RED"   \'{"tool_name":"Read","tool_input":{"file_path":"/Users/HasanSalihSahin/sistem/ogrenme/mufredat.md"}}\' 2\n'
              'echo "--------"')
        t = t.replace('echo "--------"', ek, 1)
    return t


def ogren_ortak_hazirla(uzerine, kuru):
    """`sablonlar/skills/ogren/` yoksa jarvis kopyasından v0.3 alan sürümünü türet (yol/protokol satırları alan ajanına göre)."""
    for kokdizin, _d, dosyalar in os.walk(OGREN_KAYNAK):
        for f in dosyalar:
            kaynak = os.path.join(kokdizin, f); rel = os.path.relpath(kaynak, OGREN_KAYNAK)
            t = open(kaynak, encoding="utf-8").read()
            if rel == "SKILL.md":
                t = t.replace("# ogren — dört fazlı ders akışı + öğrenme oturum protokolü (v0.2, 2026-09-15; deneme v0.1 09-09 → hazine)",
                              "# ogren — dört fazlı ders akışı + öğrenme oturum protokolü (v0.3 ALAN SÜRÜMÜ, 2026-09-21, Karar 105; v0.2 09-15 Jarvis kopyası `jarvis/.claude/skills/ogren/` öğretim-tasarımı için kalır)\n\n"
                              "**Alan-ajanı farkı (Karar 103 EK 1 · Karar 105 M4):** bu skill alan ajanının dizininde (`~/sistem/<alan>/`) koşar; şerit yolları `ogrenme/<şerit>/` **bu dizine** görelidir; ders iskeleti (`PROBE` soruları · `PLAN` DAG · kutu başlıkları) Jarvis'ten `cc/gelen/ders-<hafta>.md` ile gelir — varsa aynen kullanılır, `PROBE`/`PLAN` üretilmez; yoksa önceki dersin `## Kalan` listesiyle devam edilir, **yeni hafta açılmaz** (Jarvis'e `cc/giden/` ile \"iskelet gerekli: <hafta>\" notu). Oturum: cwd alan dizini, worktree kapalı, main, pathspec-only; PR yok, push yalnız Salih beyanıyla (protokol §5 EK-4 Karar 105 satırı). `mcp__visualize` yoksa DAG `raporlar/gorsel-*.html` olarak elle yazılır.")
                t = t.replace("Yan oturum worktree + kendi branch'i; ilk iş `git fetch origin && git rebase origin/main` (protokol §5 EK).",
                              "Alan ajanında worktree yok: cwd `~/sistem/<alan>`, main; ilk iş `git log -3 -- .` canlı-oturum kapısı (seans-acilis).")
                t = t.replace("Sonra `git add ogrenme/<şerit>/…` + commit (İngilizce mesaj, m.10) + push + PR (`gh-axi pr create`, açıklamada \"yalnız bu oturumun commit'leri\"); merge ana-sıra Fable'da (Karar 95). Kapsül/pano/defter'e yazılmaz; `seans-kapanis` koşulmaz.",
                              "Sonra `git add ogrenme/<şerit>/…` + commit (İngilizce mesaj, m.10); push yalnız Salih beyanıyla, PR yok. Kapsül/pano/defter alan ajanının kendi `seans-kapanis` ritüelinde yazılır.")
            yaz(os.path.join(OGREN_ORTAK, rel), t, uzerine, kuru)


def doldur(sablon, d):
    def tek(m):
        k = m.group(1)
        if k not in d:
            sys.exit("[HATA] şablon anahtarı yok: {{%s}}" % k)
        return d[k]
    return re.sub(r"\{\{(\w+)\}\}", tek, sablon)


def uret(spec, a):
    tarih = a.tarih
    for aj in spec["ajanlar"]:
        dizin = aj["dizin"]; hedef = os.path.join(KOK, dizin)
        seritler = " · ".join("`%s` (%s)" % (s["hedef"], s["durum"]) for s in aj["seritler"])
        serit_tablo = "| Şerit | Kaynak (T3 öncesi) | Hedef | Durum |\n|---|---|---|---|\n" + "\n".join(
            "| %s | `../%s` | `%s` | %s |" % (os.path.basename(s["kaynak"]), s["kaynak"], s["hedef"], s["durum"]) for s in aj["seritler"])
        pano = "\n".join("| %s | şerit: %s | sıradaki hafta kavramsal `DONE` + pratik Salih beyanı | %s | `%s/ilerleme.md` | her seans |"
                         % (os.path.basename(s["hedef"]), s["durum"], tarih, s["hedef"]) for s in aj["seritler"])
        d = {"AD": aj["ad"], "AD_BUYUK": aj["ad"].upper(), "ALAN_KISA": aj.get("alan_kisa", dizin), "AD_GEREKCE": aj["ad_gerekce"], "DIZIN": dizin, "ALAN": aj["alan"],
             "MODEL": spec["model"], "BAKIM": spec["bakim_maliyeti"], "KARAR": spec["karar"], "TARIH": tarih,
             "SERITLER": seritler, "SERIT_TABLO": serit_tablo, "URUN": aj["urun"], "HAKEM_PERSPEKTIFI": aj["hakem_perspektifi"],
             "PANO_SATIRLARI": pano}
        # şablon dosyaları (.tmpl → doldur; diğerleri aynen)
        for kokdizin, _dd, dosyalar in os.walk(ISKELET):
            for f in dosyalar:
                kaynak = os.path.join(kokdizin, f)
                rel = os.path.relpath(kaynak, ISKELET)
                if rel.startswith(CLAUDE_AYAR + os.sep):
                    rel = os.path.join(".claude", rel[len(CLAUDE_AYAR) + 1:])
                t = open(kaynak, encoding="utf-8").read()
                if rel.endswith(".tmpl"):
                    rel = rel[:-5]; t = doldur(t, d)
                yaz(os.path.join(hedef, rel), t, a.uzerine_yaz, a.kuru, calistir=rel.endswith(".sh"))
        # hook'lar (Friday'den yamalı)
        for ad in ("okuma-izin.sh", "okuma-izin-test.sh", "hareket-kutuk.sh"):
            t = hook_v06(ad)
            if ad == "okuma-izin-test.sh":
                baska = next((x["dizin"] for x in spec["ajanlar"] if x["dizin"] != dizin), "friday")
                t = t.replace("__baska_ajan__", baska).replace("__ajan__", dizin)
            yaz(os.path.join(hedef, ".claude", "hooks", ad), t, a.uzerine_yaz, a.kuru, calistir=True)
        # boş dizinler + symlink'ler
        for bos in ("cc/gelen", "cc/giden", "cc/rapor", "raporlar", "arsiv", "veri/bronz", "ogrenme"):
            yaz(os.path.join(hedef, bos, ".gitkeep"), "", a.uzerine_yaz, a.kuru)
        symlink("AGENTS.md", os.path.join(hedef, "CLAUDE.md"), a.kuru)
        symlink(os.path.join("..", "..", "..", "sablonlar", "skills", "ogren"), os.path.join(hedef, ".claude", "skills", "ogren"), a.kuru)
        yaz(os.path.join(hedef, ".claude", "agent-memory", "hakem", "MEMORY.md"),
            "# %s hakemi hafızası (yalnız usul dersleri; içerik hükmü girmez)\n\n- %s: doğum; ilk koşum sonrası kendi kalıp hataları buraya.\n" % (aj["ad"], tarih),
            a.uzerine_yaz, a.kuru)
    # T3 komut listesi (Salih eli)
    print("\n# T3 — Salih eli (git mv; m.8 taşıma beyanı). Sıra önemli değil; sonra tek commit `[icra] Decision 105 T3: move learning tracks into domain agents`:")
    print("cd ~/sistem")
    for aj in spec["ajanlar"]:
        for s in aj["seritler"]:
            print("git mv %s %s/%s" % (s["kaynak"], aj["dizin"], s["hedef"]))
    print("git commit -m \"[icra] Decision 105 T3: move learning tracks into domain agent directories\"   # git mv zaten stage'ler; -A yasak")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec"); ap.add_argument("--kuru", action="store_true"); ap.add_argument("--uzerine-yaz", action="store_true")
    ap.add_argument("--tarih", default=datetime.date.today().isoformat())
    a = ap.parse_args()
    try:
        spec = json.load(open(a.spec, encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        sys.exit("[HATA] spec okunamadı: %s" % e)
    for z in ("ajanlar", "model", "bakim_maliyeti", "karar"):
        if z not in spec:
            sys.exit("[HATA] spec alanı eksik: %s" % z)
    if not os.path.isdir(ISKELET):
        sys.exit("[HATA] şablon dizini yok: %s" % ISKELET)
    ogren_ortak_hazirla(a.uzerine_yaz, a.kuru)
    uret(spec, a)
    print("\nALAN-AJANI-DOGUR %s: ajan %d · dosya yeni %d · atlandı (var, farklı) %d · aynı %d%s" % (
        spec["karar"], len(spec["ajanlar"]), SAYAC["yeni"], SAYAC["atlandi"], SAYAC["ayni"], " · KURU" if a.kuru else ""))


if __name__ == "__main__":
    main()
