#!/usr/bin/env python
"""fark-ambar-tablo.py — jarvis/tools/ambar-tablo.py (Python) ile Rust ikilisini (ambar-tablo) karşılaştırır.
Her durumda aynı kum havuzunun iki kopyası hazırlanır; çıkış kodu, stdout, stderr ve yazılan tüm dosyalar
(sqlite: tablo/görünüm dökümü, zaman damgası sütunları maskeli; metin: CRLF→LF) karşılaştırılır.
Kullanım: python fark-ambar-tablo.py   (RUST_EXE ortam değişkeni ya da C:/tmp/tgt/release/ambar-tablo.exe)"""
import json, os, re, shutil, sqlite3, subprocess, sys, tempfile

KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
PY_ARAC = os.path.join(KOK, "jarvis", "tools", "ambar-tablo.py")
RUST = os.environ.get("RUST_EXE", "C:/tmp/tgt/release/ambar-tablo.exe")

SEMA = """
CREATE TABLE prompt (prompt_id TEXT, oturum_id TEXT, sira INTEGER, tur TEXT, sonraki_skill TEXT, sonraki_model TEXT, uzunluk_kar INTEGER, kelime INTEGER, metin_kisa TEXT, ts_utc TEXT, ts_tr TEXT, yuklendi_head TEXT);
CREATE TABLE karar_borcu (borc_id TEXT, kume TEXT, katman INTEGER, karar_sahibi TEXT, durum TEXT, tur TEXT, masa_sirasi INTEGER, kayit_tarihi TEXT, snapshot_tarih TEXT, snapshot_sha TEXT, baslik TEXT);
CREATE TABLE anahtar (anahtar_id TEXT, tur TEXT, deger TEXT, durum TEXT, replaced_by TEXT, gecerli_bas TEXT, ilk_gorulme TEXT, gecerli_bitis TEXT, referans_sayisi INTEGER, sicak_referans_sayisi INTEGER);
CREATE TABLE referans (kayit_id TEXT, ref_deger TEXT, ref_turu TEXT, hedef_var INTEGER);
CREATE TABLE kayit (kayit_id TEXT, dosya_id TEXT, tarih_iso TEXT);
CREATE TABLE dosya (dosya_id TEXT, katman TEXT, tur TEXT, baslik TEXT, ilk_commit TEXT, boyut_bytes INTEGER);
INSERT INTO prompt VALUES ('p1','o1',1,'komut','atlas, fable','opus',10,2,'ilk prompt','2026-08-20T10:00:00Z','2026-08-20T13:00:00','abc'),
 ('p2','o1',2,'soru','fable','sonnet',20,3,'ikinci, "tırnaklı"','2026-08-21T10:00:00Z','2026-08-21T13:00:00','abc'),
 ('p3','o2',1,'komut',NULL,NULL,5,1,'üçüncü satır','2026-08-22T10:00:00Z','2026-08-22T13:00:00','abc'),
 ('p4','o2',2,'komut','atlas','opus',5,1,'dört','2026-08-22T11:00:00Z','2026-08-22T14:00:00','abc');
INSERT INTO karar_borcu VALUES ('b1','k1',1,'Salih','açık','karar',1,'2026-08-01','2026-08-20','sha1','Başlık bir'),
 ('b2','k1',2,'Jarvis','açık','icra',2,'2026-08-02','2026-08-20','sha1','Başlık iki'),
 ('b3','k2',1,'Salih (ve)','kapandı','karar',3,'2026-08-03','2026-08-20','sha1','Başlık üç');
INSERT INTO anahtar VALUES ('a1','tur','d1','aktif',NULL,NULL,'2026-01-01',NULL,3,1),('a2','tur','d2','eski','a1','2026-01-02','2026-01-01','2026-02-01',0,0);
INSERT INTO dosya VALUES ('d1','L1','teslim','Teslim 1','2026-08-01',100),('d2','L1','teslim','Teslim 2','2026-08-05',200),('d3','L2','rapor','Rapor','2026-08-06',50);
INSERT INTO kayit VALUES ('k1','d1','2026-08-01'),('k2','d2','2026-08-05');
INSERT INTO referans VALUES ('k1','x','ref',1),('k2','y','ref',0);
"""


def yaz(yol, metin, mod="w"):
    os.makedirs(os.path.dirname(yol), exist_ok=True)
    with open(yol, mod, encoding="utf-8", newline="") as f:
        f.write(metin)


def satir(**kw):
    return json.dumps(kw, ensure_ascii=False) + "\n"


def transkript(proje):
    """Alt-ajan transkript fikstürleri (çeşitli yollar/biçimler)."""
    def a(yol, icerik, meta=None):
        yaz(os.path.join(proje, *yol.split("/")), icerik)
        if meta is not None:
            yaz(os.path.join(proje, *yol.split("/"))[:-6] + ".meta.json", meta)
    usr = lambda c, ts=None: satir(type="user", timestamp=ts, message={"content": c})
    ast = lambda ts, model="claude-opus-9", usage=None, content=None: satir(type="assistant", timestamp=ts, message={"model": model, "usage": usage or {}, "content": content or []})
    u1 = {"input_tokens": 10, "output_tokens": 200, "cache_read_input_tokens": 30, "cache_creation_input_tokens": 5}
    a("sess1/subagents/wf_aaa/agent-a1.jsonl",
      usr("ROL: TEZ — kıdemli yazar aile B koş\nikinci satır   boşluklu\ttab", "2026-08-10T10:00:00.000Z")
      + ast("2026-08-10T10:01:30.500Z", usage=u1, content=[{"type": "tool_use"}, {"type": "text"}, {"type": "tool_use"}])
      + "bozuk json satırı\n\n"
      + ast("2026-08-10T10:03:00Z", model="claude-haiku-1", usage={"input_tokens": "7", "output_tokens": 3.9, "cache_read_input_tokens": None}),
      '{"agentType": "atlas"}')
    a("sess1/subagents/wf_aaa/agent-a2.jsonl",
      usr([{"type": "text", "text": "ROL: ANTİTEZ\nsonra"}], "2026-08-10T10:00:00+00:00") + ast("2026-08-10T10:05:00+00:00", usage=u1),
      '{"agentType": "general"}')
    a("sess1/subagents/wf_aaa/deep/er/agent-a3.jsonl", usr("ROL: HAKEM — x aile ABC.", "2026-08-10T11:00:00Z") + ast("2026-08-10T11:00:10Z", usage=u1), "bozuk meta")
    a("sess1/subagents/wf_bbb/agent-b1.jsonl", usr("ROL: V26 son", "2026-08-11 09:00:00") + ast("2026-08-11T09:00:05Z"))
    a("sess1/subagents/agent-c1.jsonl", usr("serbest metin aile Q", "2026-08-12T00:00:00Z") + ast("2026-08-12T00:00:01Z", usage={"output_tokens": 5}, content=[{"type": "tool_use"}]))
    a("sess2/subagents/agent-ünicode.jsonl", usr("Ünİcode ROL: Ş ğ\r\nsatır", "2026-08-13T00:00:00Z") + ast(None, content="metin"))
    a("sess2/subagents/agent-bos.jsonl", "\n\nnot json\n")
    a("sess2/subagents/agent-dolu-ama-zamansiz.jsonl", satir(type="user", message={"content": [{"type": "text"}]}) + satir(type="assistant", message=None))
    a("sess2/subagents/wf_ccc/agent-d1.jsonl", usr("ROL:", "2026-08-14T00:00:00Z") + usr("ikinci user", "2026-08-14T00:00:01Z") + ast("2026-08-14T00:00:02Z", model="m2"))
    a("sess3/subagents/.gizli/agent-g.jsonl", usr("gizli", "2026-08-14T00:00:00Z"))
    a("sess3/subagents/agent-yanlis.txt", "x")
    yaz(os.path.join(proje, "sess3", "kok-dosya.txt"), "x")


def kum(hedef, durum):
    """durum: ad → fikstür varyantı."""
    repo = os.path.join(hedef, "repo")
    proje = os.path.join(hedef, "proje")
    os.makedirs(repo)
    env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t", GIT_AUTHOR_DATE="2026-01-01T00:00:00Z", GIT_COMMITTER_DATE="2026-01-01T00:00:00Z")
    if durum != "gitsiz":
        subprocess.run(["git", "init", "-q"], cwd=repo, stdin=subprocess.DEVNULL, env=env)
        yaz(os.path.join(repo, "a.txt"), "a\n")
        subprocess.run(["git", "add", "."], cwd=repo, stdin=subprocess.DEVNULL, env=env)
        subprocess.run(["git", "commit", "-q", "-m", "x"], cwd=repo, stdin=subprocess.DEVNULL, env=env)
    os.makedirs(proje)
    if durum != "bos-proje":
        transkript(proje)
    for d in ("bronz", "sozlesme", "gorunum"):
        if not (durum == "sozlesmesiz" and d == "sozlesme") and not (durum == "gorunumsuz" and d == "gorunum") and not (durum == "bronzsuz" and d == "bronz"):
            os.makedirs(os.path.join(repo, "veri", d), exist_ok=True)
    if durum != "dbsiz":
        con = sqlite3.connect(os.path.join(repo, "veri", "baglam.sqlite"))
        sema = SEMA if durum != "promptsuz" else SEMA.replace("CREATE TABLE prompt", "CREATE TABLE xprompt").replace("INSERT INTO prompt", "INSERT INTO xprompt")
        con.executescript(sema)
        if durum == "eski-sonuc":  # wf_id kolonsuz eski tablo
            con.executescript("CREATE TABLE amb_olgu_kosum_sonuc (kosum_id TEXT PRIMARY KEY, sonuc TEXT, kaynak TEXT, aciklama TEXT, system_time TEXT, kod_sha TEXT);")
        con.commit(); con.close()
    b = os.path.join(repo, "veri", "bronz")
    if durum in ("dolu", "dolu2", "eski-sonuc", "sozlesmeli"):
        yaz(os.path.join(b, "kosum-olay.jsonl"), "# baslik\n" + satir(kosum_id="wf_aaa:a1", wf_id="wf_aaa", agent_id="a1", agent_type="eski", oturum="s", kaynak_dosya="x", yuklendi_head="h", yuklendi_ts="t") + satir(kosum_id="wf_zzz:z1", wf_id="wf_zzz", agent_id="z1", agent_type=None, oturum="s", kaynak_dosya="y", aile="A", rol="TEZ", output_tokens=7, input_tokens=1, cache_creation_input_tokens=2, sure_sn=3.5, arac_cagrisi=1, yuklendi_head="h", yuklendi_ts="t") + satir(kosum_id="wf_zzz:z1", wf_id="wf_zzz", agent_id="z1", agent_type="ikinci", oturum="s", kaynak_dosya="y", yuklendi_head="h", yuklendi_ts="t"))
        yaz(os.path.join(b, "tahmin-olay.jsonl"), "# başlık\n" + satir(tahmin_id="t1", gorev_emri_dosya="g.md", gorev_emri_satir=3, rol="TEZ", model_sinifi="sonnet", effort="m", tahmin_cikti_min=100, tahmin_cikti_max=300, tahmin_arac_min=0, tahmin_arac_max=2, tahmin_sure_min_sn=10, tahmin_sure_max_sn=200, tahmin_serbest_metin="serbest", tahmin_formul_mu=False, tahmin_kaynagi="k", wf_id="wf_aaa", yuklendi_ts="t", yuklendi_head="h")
             + satir(tahmin_id="t2", rol="ANTİTEZ", wf_id="wf_aaa", tahmin_cikti_min=1, tahmin_cikti_max=2, tahmin_formul_mu=1, tahmin_arac_min=1, tahmin_arac_max=1, tahmin_sure_min_sn=1, tahmin_sure_max_sn=2)
             + satir(tahmin_id="t3", rol="HAKEM", wf_id="wf_yok", tahmin_cikti_min=1, tahmin_cikti_max=0))
        yaz(os.path.join(b, "kosum-sonuc.jsonl"), satir(kosum_id="wf_aaa:a1", sonuc="PASS", kaynak="o", aciklama="a", yuklendi_ts="t", yuklendi_head="h")
             + satir(kosum_id="wf_bbb", sonuc="FAIL", yuklendi_ts="t") + satir(kosum_id="wf_bbb:b1", sonuc="XX", supersedes="eski")
             + satir(kosum_id="eski", sonuc="PASS") + satir(kosum_id="x", sonuc="PASS", wf_id="wf_kayip", supersedes=""))
        yaz(os.path.join(repo, "veri", "tartisma-notu.jsonl"), satir(not_id="n1", tarih="2026-08-20", konu="Konu", tetikleyen="t", cevap_ozeti="c", acik_soru="?", katman=1, durum="açık", oturum="o1", kaynak_kuyruk="kq", prompt_id=["p1", "p2", "pYOK"]) + satir(not_id="n2", tarih="2026-08-21", konu="K2"))
    if durum in ("dolu2",):
        yaz(os.path.join(b, "kosum-olay.jsonl"), "")  # boş mevcut dosya (başlık yok)
    if durum == "bozuk-jsonl":
        yaz(os.path.join(b, "kosum-olay.jsonl"), "{bozuk\n")
    if durum == "sozlesmeli":
        for ad in ("amb_olgu_kosum", "amb_olgu_tahmin", "amb_olgu_kosum_sonuc"):
            yaz(os.path.join(repo, "veri", "sozlesme", ad + ".json"), "{}")
    if durum == "csv-ozel":
        yaz(os.path.join(repo, "veri", "tartisma-notu.jsonl"), satir(not_id="n1", tarih="2026-08-20", konu='Satır\nsonu, "q"', durum=None))
    return repo, proje


def dokum(repo):
    """Repo altındaki dosyalar: ad → normalize içerik."""
    sonuc = {}
    maske = re.compile(r'"yuklendi_ts": "[^"]*"')
    for k, _, dosyalar in os.walk(repo):
        if ".git" in k.split(os.sep):
            continue
        for f in dosyalar:
            y = os.path.join(k, f); rel = os.path.relpath(y, repo).replace("\\", "/")
            if f.endswith((".sqlite", ".sqlite-journal")):
                if f.endswith(".sqlite"):
                    sonuc[rel] = sqlite_dokum(y)
                continue
            m = open(y, "rb").read().decode("utf-8", "replace").replace("\r\n", "\n")
            sonuc[rel] = maske.sub('"yuklendi_ts": "T"', m)
    return sonuc


def sqlite_dokum(y):
    con = sqlite3.connect(y)
    cikti = []
    for ad, tur in con.execute("SELECT name, type FROM sqlite_master WHERE name NOT LIKE 'sqlite_%' ORDER BY name").fetchall():
        cur = con.execute(f"SELECT * FROM {ad}")
        cols = [d[0] for d in cur.description]
        sat = []
        for r in cur.fetchall():
            sat.append(repr(tuple("<ZAMAN>" if c in ("system_time", "yuklendi_ts") and v is not None and ad.startswith("amb_olgu") else v for c, v in zip(cols, r))))
        cikti.append(f"{tur} {ad} {cols}\n  " + "\n  ".join(sorted(sat)))
        if tur == "table":
            cikti.append("  " + repr(con.execute(f"SELECT sql FROM sqlite_master WHERE name='{ad}'").fetchone()[0].split()))
    con.close()
    return "\n".join(cikti)


def kos(cmd, cwd):
    p = subprocess.run(cmd, cwd=cwd, stdin=subprocess.DEVNULL, capture_output=True)
    return p.returncode, p.stdout.decode("utf-8", "replace").replace("\r\n", "\n"), p.stderr.decode("utf-8", "replace").replace("\r\n", "\n")


# (ad, kum durumu, argümanlar (repo/proje yer tutucu), [ardışık ikinci koşu], stderr kıyaslanır mı)
DURUMLAR = [
    ("tam", "dolu", ["--repo", "{R}", "--proje-dizin", "{P}"], False, True),
    ("tam-iki-kosu", "dolu", ["--repo", "{R}", "--proje-dizin", "{P}"], True, True),
    ("sessiz", "dolu", ["--repo", "{R}", "--proje-dizin", "{P}", "--sessiz"], False, True),
    ("kuru", "dolu", ["--repo", "{R}", "--proje-dizin", "{P}", "--kuru"], False, True),
    ("kuru-bronzsuz", "bronzsuz", ["--repo", "{R}", "--proje-dizin", "{P}", "--kuru"], False, True),
    ("bos-mevcut", "dolu2", ["--repo", "{R}", "--proje-dizin", "{P}"], False, True),
    ("temiz", "temiz", ["--repo", "{R}", "--proje-dizin", "{P}"], False, True),
    ("temiz-iki-kosu", "temiz", ["--repo", "{R}", "--proje-dizin", "{P}"], True, True),
    ("bos-proje", "bos-proje", ["--repo", "{R}", "--proje-dizin", "{P}"], False, True),
    ("proje-yok", "temiz", ["--repo", "{R}", "--proje-dizin", "{P}/yok"], False, True),
    ("gitsiz", "gitsiz", ["--repo", "{R}", "--proje-dizin", "{P}"], False, True),
    ("eski-sonuc", "eski-sonuc", ["--repo", "{R}", "--proje-dizin", "{P}"], False, True),
    ("sozlesmeli", "sozlesmeli", ["--repo", "{R}", "--proje-dizin", "{P}"], False, True),
    ("csv-ozel", "csv-ozel", ["--repo", "{R}", "--proje-dizin", "{P}"], False, True),
    ("kisaltma", "temiz", ["--rep", "{R}", "--proje", "{P}", "--ses"], False, True),
    ("yardim", "temiz", ["-h"], False, True),
    ("bilinmeyen", "temiz", ["--yok"], False, True),
    ("deger-eksik", "temiz", ["--repo"], False, True),
    # Python'da yakalanmamış istisna: yalnız çıkış kodu + stdout
    ("sozlesme-dizini-yok", "sozlesmesiz", ["--repo", "{R}", "--proje-dizin", "{P}"], False, False),
    ("gorunum-dizini-yok", "gorunumsuz", ["--repo", "{R}", "--proje-dizin", "{P}"], False, False),
    ("prompt-tablosu-yok", "promptsuz", ["--repo", "{R}", "--proje-dizin", "{P}"], False, False),
    ("bozuk-bronz", "bozuk-jsonl", ["--repo", "{R}", "--proje-dizin", "{P}"], False, False),
    ("repo-yok", "temiz", ["--repo", "{R}/yok", "--proje-dizin", "{P}"], False, False),
    ("db-yok", "dbsiz", ["--repo", "{R}", "--proje-dizin", "{P}"], False, False),
]


def main():
    toplam = fark = 0
    for ad, durum, args, iki, stderr_karsilastir in DURUMLAR:
        kok = tempfile.mkdtemp(prefix="fark-amb-")
        try:
            tohum = os.path.join(kok, "tohum")
            kum(tohum, durum)
            sonuclar = []
            for ic in ("py", "rs"):
                d = os.path.join(kok, ic)
                shutil.copytree(tohum, d)
                R, P = os.path.join(d, "repo"), os.path.join(d, "proje")
                a = [x.replace("{R}", R).replace("{P}", P) for x in args]
                cmd = ["python", PY_ARAC] + a if ic == "py" else [RUST] + a
                r = kos(cmd, d)
                if iki:
                    r2 = kos(cmd, d)
                    r = (r[0], r[1] + "\n--2--\n" + r2[1], r[2] + r2[2], r2[0])
                # yol maskeleri
                mask = lambda s: s.replace(d, "<D>").replace(d.replace("\\", "/"), "<D>")
                sonuclar.append((r, dokum(R), mask))
            (rp, fp, mp), (rr, fr, mr) = sonuclar
            toplam += 1
            sorunlar = []
            if rp[0] != rr[0]: sorunlar.append(f"çıkış kodu py={rp[0]} rs={rr[0]}")
            if mp(rp[1]) != mr(rr[1]): sorunlar.append(f"stdout farklı\n  PY: {mp(rp[1])!r}\n  RS: {mr(rr[1])!r}")
            if stderr_karsilastir and mp(rp[2]) != mr(rr[2]): sorunlar.append(f"stderr farklı\n  PY: {mp(rp[2])[:600]!r}\n  RS: {mr(rr[2])[:600]!r}")
            if len(rp) > 3 and rp[3] != rr[3]: sorunlar.append(f"2. çıkış kodu py={rp[3]} rs={rr[3]}")
            if fp.keys() != fr.keys(): sorunlar.append(f"dosya kümesi farklı: yalnız py={sorted(fp.keys()-fr.keys())} yalnız rs={sorted(fr.keys()-fp.keys())}")
            for k in sorted(fp.keys() & fr.keys()):
                if fp[k] != fr[k]:
                    import difflib
                    dd = "\n".join(list(difflib.unified_diff(fp[k].split("\n"), fr[k].split("\n"), "py", "rs", lineterm="", n=0))[:14])
                    sorunlar.append(f"dosya farklı: {k}\n{dd}")
            if sorunlar:
                fark += 1
                print(f"[FARK] {ad}")
                for s in sorunlar: print("   ", s)
            else:
                print(f"[ESIT] {ad} (çıkış {rp[0]})")
        finally:
            shutil.rmtree(kok, ignore_errors=True)
    print(f"ambar-tablo: {toplam} durum, {fark} fark")
    return 1 if fark else 0


if __name__ == "__main__":
    sys.exit(main())
