#!/usr/bin/env python3
"""ambar-tablo.py — BAĞLAM VERİ AMBARI v0 (deneysel m.29; wiki/baglam-veri-ambari.md tanımı): aynı SQLite'ta AYRI şema (önek `amb_`).

Ayrım = erişim-tasarımı (Stonebraker&Çetintemel 2005): ambar tabloları yıldız/galaxy grain'li, MATERYALİZE, iki zaman sütunlu (bitemporal —
system_time = üretim/commit anı, valid_time = olgunun gerçek anı; SQL:2011 ayrımı). Operasyonel taban (V-1) elle dokunulmaz; ambar ondan ve
bronz kütüklerden DETERMİNİSTİK türer (kod SHA + girdi SHA). Kanıt: cc/rapor/2026-08/rapor-2026-08-16-3.md (AB-YT1/YT2/YT4/YT5/YT6, CD-YT1/YT2/YT8).

BRONZ (yeni): veri/bronz/kosum-olay.jsonl — işçi-ajan koşum olayları (Workflow + Agent alt-ajan transkriptleri: ~/.claude/projects/<proje>/**/subagents/**/agent-*.jsonl);
  1 satır = 1 ajan koşumu {wf_id, agent_id, agent_type, aile/rol (ilk prompt'tan), model(ler), ts_bas, ts_son, sure_sn, token in/out/cache_read/cache_create, arac_cagrisi, oturum}.
BRONZ (KB-02/03, 08-21): veri/bronz/tahmin-olay.jsonl — üst modelin alt-model koşum TAHMİNLERİ (1 satır = 1 (görev-emri, rol) tahmini; aile-BAĞIMSIZ granülarite;
  bu script yalnız OKUR — üretim elle/emir-derleme anında). Silver: amb_olgu_tahmin. Gold: v_kosum_tahmin_sapma (JOIN wf_id + rol_norm deterministik CASE —
  amb_olgu_kosum.rol serbest metindir) · v_skill_kosum (KB-03 dar pilot; iki dürüst blok: ana-sıra prompt sayımı + yalnız KESİN agent_type→skill eşlemesi
  [atlas→atlas-kosum]; kayıplı haritalama GÖMÜLMEZ).
BRONZ (Karar 52, 08-21 — ÖNERİ-damgalı): veri/bronz/kosum-sonuc.jsonl — koşum hükmü (done-yüklemi PASS/FAIL, orkestratör teslim-al adımında yazar;
  transkriptten türetilemez). Silver: amb_olgu_kosum_sonuc. v_skill_kosum vekil bloğunda sonuc_n (kaç koşumun hükmü var) + fail_n — 0 ≠ veri-yok
  ayrımı sonuc_n ile korunur. Nihai Katman-1 şema imzası AÇIK (deneysel m.29).
SİLVER/AMBAR (materyalize): amb_olgu_kosum (grain: 1 satır = 1 işçi-ajan koşumu; OTel gen_ai.usage.* adları eşleme sözlüğü olarak, kolon değil)
  · amb_olgu_prompt (1 satır = 1 Salih prompt'u; valid_time = ts, system_time = yükleme) · amb_olgu_karar_borcu (1 satır = 1 açık kalem snapshot'ı; valid_from = kayit_tarihi)
  · amb_boyut_anahtar (SCD-2 görünüm: gecerli_bas/gecerli_bitis/guncel_mi — Kimball asgari 3) · amb_kopru_olay_nesne (factless + qualifier — OCEL event_object; referans'tan)
  · amb_boyut_vardiya (teslim dosyalarından).
GOLD martları: v_amb_kosum_maliyet (workflow başına ajan/token/süre) · v_amb_acilis_brifi (as-of tek satır: HEAD · açık karar-borcu · son ölçüm oranı · son prompt · son teslim).
Kullanım: python3 tools/ambar-tablo.py [--repo] [--proje-dizin] [--kuru] [--sessiz]   (katman-hatti.py içinde prompt'tan sonra koşar)
"""
import argparse, csv, glob, json, os, re, sqlite3, subprocess, sys
import harness_anahtar
from datetime import datetime, timezone

TOKEN_ALANLAR = ("input_tokens", "output_tokens", "cache_read_input_tokens", "cache_creation_input_tokens")


def sh(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True).stdout.strip()


def ajan_ozeti(yol):
    rows = []
    for l in open(yol, encoding="utf-8", errors="replace"):
        try: rows.append(json.loads(l))
        except json.JSONDecodeError: continue
    if not rows: return None
    ts = [d["timestamp"] for d in rows if d.get("timestamp")]
    models, tok, arac, ilk = {}, {k: 0 for k in TOKEN_ALANLAR}, 0, None
    for d in rows:
        m = d.get("message") or {}
        if d.get("type") == "user" and ilk is None:
            c = m.get("content")
            ilk = c if isinstance(c, str) else (c[0].get("text", "") if isinstance(c, list) and c and isinstance(c[0], dict) else "")
        if d.get("type") == "assistant":
            if m.get("model"): models[m["model"]] = models.get(m["model"], 0) + 1
            u = m.get("usage") or {}
            for k in TOKEN_ALANLAR: tok[k] += int(u.get(k, 0) or 0)
            for x in m.get("content") or []:
                if isinstance(x, dict) and x.get("type") == "tool_use": arac += 1
    ilk = ilk or ""
    rol = re.search(r"ROL:\s*(.+?)(?:\s+—|\n|$)", ilk); aile = re.search(r"aile\s+([A-Z]{1,3})\b", ilk)
    try:
        t0 = datetime.fromisoformat(ts[0].replace("Z", "+00:00")); t1 = datetime.fromisoformat(ts[-1].replace("Z", "+00:00")); sure = (t1 - t0).total_seconds()
    except Exception:
        sure = None
    return {"ts_bas": ts[0] if ts else None, "ts_son": ts[-1] if ts else None, "sure_sn": sure, "modeller": ",".join(sorted(models)), "asistan_mesaj": sum(models.values()),
            "arac_cagrisi": arac, **tok, "rol": rol.group(1).strip()[:80] if rol else None, "aile": aile.group(1) if aile else None, "ilk_prompt_kisa": re.sub(r"\s+", " ", ilk)[:160]}


def bronz_kosum(proje_dizin):
    olaylar = []
    for yol in sorted(glob.glob(os.path.join(proje_dizin, "*", "subagents", "**", "agent-*.jsonl"), recursive=True)):
        parcalar = yol.split(os.sep)
        oturum = parcalar[parcalar.index("subagents") - 1]
        wf = next((p for p in parcalar if p.startswith("wf_")), None)
        agent_id = os.path.basename(yol)[len("agent-"):-len(".jsonl")]
        meta = {}
        my = yol[:-len(".jsonl")] + ".meta.json"
        if os.path.exists(my):
            try: meta = json.load(open(my))
            except Exception: meta = {}
        oz = ajan_ozeti(yol)
        if not oz: continue
        olaylar.append({"kosum_id": f"{wf or 'agent'}:{agent_id}", "wf_id": wf, "agent_id": agent_id, "agent_type": meta.get("agentType"), "oturum": oturum, "kaynak_dosya": os.path.relpath(yol, proje_dizin), **oz})
    return olaylar


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--proje-dizin", default=harness_anahtar.proje_dizin())  # makineye göre anahtar (2026-09-22)
    ap.add_argument("--kuru", action="store_true"); ap.add_argument("--sessiz", action="store_true")
    a = ap.parse_args(); repo = os.path.abspath(a.repo); head = sh(["git", "rev-parse", "--short", "HEAD"], repo)
    simdi = datetime.now(timezone.utc).isoformat()

    # --- BRONZ: koşum olayları (append-only, tekil kosum_id; kaynak transkript SONRADAN büyüyebilir → satır güncellenmez, yeni koşum eklenir) ---
    olaylar = bronz_kosum(a.proje_dizin)
    byol = os.path.join(repo, "veri", "bronz", "kosum-olay.jsonl"); mevcut = {}
    if os.path.exists(byol):
        for l in open(byol, encoding="utf-8"):
            if l.startswith("{"):
                d = json.loads(l); mevcut[d["kosum_id"]] = d
    yeni = [o for o in olaylar if o["kosum_id"] not in mevcut]
    if not a.kuru:
        os.makedirs(os.path.dirname(byol), exist_ok=True)
        if not os.path.exists(byol):
            open(byol, "w", encoding="utf-8").write("# veri/bronz/kosum-olay.jsonl — BRONZ: işçi-ajan koşum olayları (Workflow/Agent alt-ajan transkriptlerinden; 1 satır = 1 ajan koşumu; append-only; tekil anahtar kosum_id; token alanları ham usage). Üretici tools/ambar-tablo.py.\n")
        with open(byol, "a", encoding="utf-8") as fh:
            for o in yeni: fh.write(json.dumps({**o, "yuklendi_head": head, "yuklendi_ts": simdi}, ensure_ascii=False) + "\n")
    hepsi = list(mevcut.values()) + [{**o, "yuklendi_head": head, "yuklendi_ts": simdi} for o in yeni]

    # --- BRONZ: tahmin olayları (KB-02; veri/bronz/tahmin-olay.jsonl — bu script yalnız OKUR, üretim elle/emir anında) ---
    tyol = os.path.join(repo, "veri", "bronz", "tahmin-olay.jsonl"); tahminler = []
    if os.path.exists(tyol):
        for l in open(tyol, encoding="utf-8"):
            if l.startswith("{"): tahminler.append(json.loads(l))
    # --- BRONZ: koşum hükümleri (Karar 52, ÖNERİ-damgalı; bu script yalnız OKUR) ---
    hyol = os.path.join(repo, "veri", "bronz", "kosum-sonuc.jsonl"); hukumler = []
    if os.path.exists(hyol):
        for l in open(hyol, encoding="utf-8"):
            if l.startswith("{"): hukumler.append(json.loads(l))

    if a.kuru:
        print(f"(kuru) bronz koşum: {len(olaylar)} ajan koşumu ({len(yeni)} yeni) · wf sayısı {len({o['wf_id'] for o in olaylar if o['wf_id']})}"); return
    con = sqlite3.connect(os.path.join(repo, "veri", "baglam.sqlite"))
    con.executescript("""
    CREATE TABLE IF NOT EXISTS amb_olgu_kosum (
      kosum_id TEXT PRIMARY KEY, wf_id TEXT, agent_id TEXT, agent_type TEXT, oturum TEXT, aile TEXT, rol TEXT, modeller TEXT,
      valid_time_bas TEXT, valid_time_son TEXT, sure_sn REAL, asistan_mesaj INTEGER, arac_cagrisi INTEGER,
      input_tokens INTEGER, output_tokens INTEGER, cache_read_input_tokens INTEGER, cache_creation_input_tokens INTEGER,
      ilk_prompt_kisa TEXT, kaynak_dosya TEXT, system_time TEXT, kod_sha TEXT
    );
    DELETE FROM amb_olgu_kosum;
    DROP TABLE IF EXISTS amb_olgu_prompt;
    CREATE TABLE amb_olgu_prompt AS
      SELECT prompt_id, oturum_id, sira, tur, sonraki_skill, sonraki_model, uzunluk_kar, kelime, metin_kisa,
             ts_utc AS valid_time, yuklendi_head AS kod_sha, datetime('now') AS system_time FROM prompt;
    DROP TABLE IF EXISTS amb_olgu_karar_borcu;
    CREATE TABLE amb_olgu_karar_borcu AS
      SELECT borc_id, kume, katman, karar_sahibi, durum, tur, masa_sirasi, kayit_tarihi AS valid_from, NULL AS valid_to,
             snapshot_tarih AS system_time, snapshot_sha AS kod_sha, baslik FROM karar_borcu;
    CREATE VIEW IF NOT EXISTS amb_boyut_anahtar AS
      SELECT anahtar_id AS anahtar_sk, anahtar_id, tur, deger, durum, replaced_by,
             COALESCE(gecerli_bas, ilk_gorulme) AS gecerli_bas, gecerli_bitis,
             CASE WHEN gecerli_bitis IS NULL OR gecerli_bitis='' THEN 1 ELSE 0 END AS guncel_mi,
             referans_sayisi, sicak_referans_sayisi FROM anahtar;
    CREATE VIEW IF NOT EXISTS amb_kopru_olay_nesne AS
      SELECT r.kayit_id AS olay_id, r.ref_deger AS nesne_id, r.ref_turu AS qualifier, r.hedef_var, k.dosya_id, d.katman, k.tarih_iso AS valid_time
      FROM referans r JOIN kayit k ON k.kayit_id=r.kayit_id JOIN dosya d ON d.dosya_id=k.dosya_id;
    CREATE VIEW IF NOT EXISTS amb_boyut_vardiya AS
      SELECT dosya_id AS teslim_dosya, baslik, ilk_commit AS teslim_zamani, boyut_bytes FROM dosya WHERE tur='teslim' ORDER BY ilk_commit;
    CREATE VIEW IF NOT EXISTS v_amb_kosum_maliyet AS
      SELECT wf_id, COUNT(*) AS ajan, GROUP_CONCAT(DISTINCT modeller) AS modeller, MIN(valid_time_bas) AS bas, MAX(valid_time_son) AS son,
             ROUND(SUM(sure_sn)/60.0,1) AS ajan_dk_toplam, SUM(output_tokens) AS output_tokens, SUM(input_tokens) AS input_tokens,
             SUM(cache_read_input_tokens) AS cache_read, SUM(cache_creation_input_tokens) AS cache_create, SUM(arac_cagrisi) AS arac_cagrisi
      FROM amb_olgu_kosum GROUP BY wf_id ORDER BY bas DESC;
    CREATE VIEW IF NOT EXISTS v_amb_acilis_brifi AS
      SELECT (SELECT kod_sha FROM amb_olgu_kosum LIMIT 1) AS kod_sha,
             (SELECT COUNT(*) FROM amb_olgu_karar_borcu WHERE karar_sahibi LIKE 'Salih%' AND durum NOT IN ('kapandı')) AS acik_salih_karari,
             (SELECT COUNT(*) FROM amb_olgu_karar_borcu WHERE karar_sahibi='Jarvis' AND durum!='kapandı') AS acik_icra_borcu,
             (SELECT metin_kisa FROM amb_olgu_prompt ORDER BY valid_time DESC LIMIT 1) AS son_prompt,
             (SELECT valid_time FROM amb_olgu_prompt ORDER BY valid_time DESC LIMIT 1) AS son_prompt_zamani,
             (SELECT COUNT(*) FROM amb_olgu_prompt WHERE date(valid_time)=date('now')) AS bugun_prompt,
             (SELECT teslim_dosya FROM amb_boyut_vardiya ORDER BY teslim_zamani DESC LIMIT 1) AS son_teslim,
             (SELECT wf_id||' · '||ajan||' ajan · '||output_tokens||' out-token' FROM v_amb_kosum_maliyet LIMIT 1) AS son_kosum,
             (SELECT COUNT(*) FROM amb_boyut_anahtar WHERE guncel_mi=1) AS guncel_anahtar,
             (SELECT COUNT(*) FROM amb_kopru_olay_nesne) AS kopru_satiri;
    CREATE TABLE IF NOT EXISTS amb_olgu_tahmin (
      tahmin_id TEXT PRIMARY KEY, gorev_emri_dosya TEXT, gorev_emri_satir INTEGER, rol TEXT, model_sinifi TEXT, effort TEXT,
      tahmin_cikti_min INTEGER, tahmin_cikti_max INTEGER, tahmin_girdi_min INTEGER, tahmin_girdi_max INTEGER,
      tahmin_arac_min INTEGER, tahmin_arac_max INTEGER, tahmin_sure_min_sn INTEGER, tahmin_sure_max_sn INTEGER,
      tahmin_serbest_metin TEXT, tahmin_formul_mu INTEGER, tahmin_kaynagi TEXT, wf_id TEXT,
      kaynak_rapor_dosya TEXT, kaynak_rapor_satir TEXT, system_time TEXT, kod_sha TEXT
    );
    DELETE FROM amb_olgu_tahmin;
    CREATE TABLE IF NOT EXISTS amb_olgu_kosum_sonuc (
      kosum_id TEXT PRIMARY KEY, sonuc TEXT, kaynak TEXT, aciklama TEXT, system_time TEXT, kod_sha TEXT, wf_id TEXT
    );
    DELETE FROM amb_olgu_kosum_sonuc;
    CREATE VIEW IF NOT EXISTS v_kosum_tahmin_sapma AS
      WITH k AS (
        SELECT wf_id, aile,
          CASE WHEN rol LIKE '%ANTİTEZ%' THEN 'ANTİTEZ'
               WHEN rol LIKE '%TEZ%' THEN 'TEZ'
               WHEN rol LIKE '%V26%' THEN 'V26'
               WHEN rol LIKE '%HAKEM%' THEN 'HAKEM'
               ELSE NULL END AS rol_norm,
          modeller, output_tokens, input_tokens + cache_creation_input_tokens AS yeni_girdi_tokens, arac_cagrisi, sure_sn
        FROM amb_olgu_kosum WHERE wf_id IS NOT NULL)
      SELECT t.tahmin_id, t.wf_id, k.aile, t.rol, t.model_sinifi, k.modeller AS gercek_model,
             t.tahmin_cikti_min, t.tahmin_cikti_max, k.output_tokens AS gercek_cikti,
             CASE WHEN t.tahmin_formul_mu=1 THEN 'FORMÜL'
                  WHEN t.tahmin_cikti_min IS NULL THEN 'TAHMİN-YOK'
                  WHEN k.output_tokens IS NULL THEN 'GERÇEK-YOK'
                  WHEN k.output_tokens < t.tahmin_cikti_min THEN 'ALTINDA'
                  WHEN k.output_tokens > t.tahmin_cikti_max THEN 'ÜSTÜNDE' ELSE 'BANDA' END AS cikti_durum,
             ROUND(k.output_tokens*1.0/NULLIF(t.tahmin_cikti_max,0), 2) AS cikti_gercek_bolu_tahmin_ust,
             t.tahmin_arac_min, t.tahmin_arac_max, k.arac_cagrisi AS gercek_arac,
             CASE WHEN t.tahmin_arac_min IS NULL THEN 'TAHMİN-YOK' WHEN k.arac_cagrisi IS NULL THEN 'GERÇEK-YOK'
                  WHEN k.arac_cagrisi < t.tahmin_arac_min THEN 'ALTINDA'
                  WHEN k.arac_cagrisi > t.tahmin_arac_max THEN 'ÜSTÜNDE' ELSE 'BANDA' END AS arac_durum,
             t.tahmin_sure_min_sn, t.tahmin_sure_max_sn, ROUND(k.sure_sn,0) AS gercek_sure_sn,
             CASE WHEN t.tahmin_sure_min_sn IS NULL THEN 'TAHMİN-YOK' WHEN k.sure_sn IS NULL THEN 'GERÇEK-YOK'
                  WHEN k.sure_sn < t.tahmin_sure_min_sn THEN 'ALTINDA'
                  WHEN k.sure_sn > t.tahmin_sure_max_sn THEN 'ÜSTÜNDE' ELSE 'BANDA' END AS sure_durum,
             t.tahmin_girdi_min, t.tahmin_girdi_max, k.yeni_girdi_tokens AS gercek_yeni_girdi,
             t.tahmin_serbest_metin, t.gorev_emri_dosya
      FROM amb_olgu_tahmin t
      LEFT JOIN k ON k.wf_id = t.wf_id AND k.rol_norm = t.rol
      ORDER BY t.wf_id, t.rol, k.aile;
    DROP VIEW IF EXISTS v_skill_kosum;
    CREATE VIEW v_skill_kosum AS
      SELECT 'ana-sira-prompt' AS kaynak, TRIM(je.value) AS skill, p.sonraki_model AS model,
             COUNT(*) AS n, NULL AS output_tokens, NULL AS sure_dk, NULL AS sonuc_n, NULL AS fail_n
      FROM amb_olgu_prompt p, json_each('["'||REPLACE(TRIM(p.sonraki_skill), ',', '","')||'"]') je
      WHERE p.sonraki_skill IS NOT NULL AND TRIM(p.sonraki_skill) <> ''
      GROUP BY TRIM(je.value), p.sonraki_model
      UNION ALL
      SELECT 'ajan-kosum-vekil',
             CASE WHEN k.agent_type='atlas' THEN 'atlas-kosum' ELSE NULL END AS skill,
             k.modeller, COUNT(*), SUM(k.output_tokens), ROUND(SUM(k.sure_sn)/60.0,1),
             COUNT(s.kosum_id), SUM(CASE WHEN s.sonuc='FAIL' THEN 1 ELSE 0 END)
      FROM amb_olgu_kosum k LEFT JOIN amb_olgu_kosum_sonuc s ON s.kosum_id=k.kosum_id
      GROUP BY CASE WHEN k.agent_type='atlas' THEN 'atlas-kosum' ELSE NULL END, k.modeller
      ORDER BY kaynak, n DESC;
    """)
    # --- tartışma notları (bronz: veri/tartisma-notu.jsonl; pointer'lı, metin kopyalanmaz) ---
    tn = os.path.join(repo, "veri", "tartisma-notu.jsonl"); notlar = []
    if os.path.exists(tn):
        for l in open(tn, encoding="utf-8"):
            if l.startswith("{"): notlar.append(json.loads(l))
    con.executescript("""
    CREATE TABLE IF NOT EXISTS amb_olgu_tartisma_notu (
      not_id TEXT PRIMARY KEY, valid_time TEXT, konu TEXT, tetikleyen TEXT, cevap_ozeti TEXT, acik_soru TEXT, katman INTEGER, durum TEXT,
      oturum TEXT, prompt_sayisi INTEGER, kaynak_kuyruk TEXT, system_time TEXT, kod_sha TEXT
    );
    DELETE FROM amb_olgu_tartisma_notu;
    CREATE TABLE IF NOT EXISTS amb_kopru_not_prompt (not_id TEXT, prompt_id TEXT, sira INTEGER, qualifier TEXT);
    DELETE FROM amb_kopru_not_prompt;
    CREATE VIEW IF NOT EXISTS v_tartisma_notu AS
      SELECT n.not_id, n.valid_time AS tarih, n.durum, n.konu, n.acik_soru, n.prompt_sayisi,
             (SELECT GROUP_CONCAT(substr(p.ts_tr,12,5)||' '||p.tur||': '||substr(p.metin_kisa,1,60), ' ¦ ') FROM amb_kopru_not_prompt k JOIN prompt p ON p.prompt_id=k.prompt_id WHERE k.not_id=n.not_id) AS prompt_ozet
      FROM amb_olgu_tartisma_notu n ORDER BY n.valid_time DESC;
    """)
    for n in notlar:
        con.execute("INSERT INTO amb_olgu_tartisma_notu VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (n["not_id"], n["tarih"], n["konu"], n.get("tetikleyen"), n.get("cevap_ozeti"), n.get("acik_soru"), n.get("katman"), n.get("durum"), n.get("oturum"), len(n.get("prompt_id", [])), n.get("kaynak_kuyruk"), simdi, head))
        for i, pid in enumerate(n.get("prompt_id", []), 1):
            con.execute("INSERT INTO amb_kopru_not_prompt VALUES (?,?,?,?)", (n["not_id"], pid, i, "tartisma-konusu"))
    con.commit()
    con.executemany("INSERT INTO amb_olgu_kosum VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", [
        (o["kosum_id"], o["wf_id"], o["agent_id"], o["agent_type"], o["oturum"], o.get("aile"), o.get("rol"), o.get("modeller"), o.get("ts_bas"), o.get("ts_son"), o.get("sure_sn"),
         o.get("asistan_mesaj"), o.get("arac_cagrisi"), o.get("input_tokens"), o.get("output_tokens"), o.get("cache_read_input_tokens"), o.get("cache_creation_input_tokens"),
         o.get("ilk_prompt_kisa"), o.get("kaynak_dosya"), o.get("yuklendi_ts"), o.get("yuklendi_head")) for o in hepsi])
    con.commit()
    con.executemany("INSERT INTO amb_olgu_tahmin VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", [
        (t["tahmin_id"], t.get("gorev_emri_dosya"), t.get("gorev_emri_satir"), t.get("rol"), t.get("model_sinifi"), t.get("effort"),
         t.get("tahmin_cikti_min"), t.get("tahmin_cikti_max"), t.get("tahmin_girdi_min"), t.get("tahmin_girdi_max"),
         t.get("tahmin_arac_min"), t.get("tahmin_arac_max"), t.get("tahmin_sure_min_sn"), t.get("tahmin_sure_max_sn"),
         t.get("tahmin_serbest_metin"), 1 if t.get("tahmin_formul_mu") else 0, t.get("tahmin_kaynagi"), t.get("wf_id"),
         t.get("kaynak_rapor_dosya"), t.get("kaynak_rapor_satir"), t.get("yuklendi_ts"), t.get("yuklendi_head")) for t in tahminler])
    con.commit()
    # İB-50: wf-düzeyi hüküm köprüsü ('wf_' önekli kosum_id → wf_id kolonu) + süpersede (düzeltme satırı eskisini
    # güncel görünümden düşürür; bronz ham kalır — Karar 58 deseni). wf_id kolonu eski DB'de yoksa additive eklenir.
    if "wf_id" not in [r[1] for r in con.execute("PRAGMA table_info(amb_olgu_kosum_sonuc)")]:
        con.execute("ALTER TABLE amb_olgu_kosum_sonuc ADD COLUMN wf_id TEXT")
    susp = {h.get("supersedes") for h in hukumler if h.get("supersedes")}
    con.executemany("INSERT INTO amb_olgu_kosum_sonuc VALUES (?,?,?,?,?,?,?)", [
        (h["kosum_id"], h.get("sonuc"), h.get("kaynak"), h.get("aciklama"), h.get("yuklendi_ts"), h.get("yuklendi_head"),
         h.get("wf_id") or (h["kosum_id"] if h["kosum_id"].startswith("wf_") else None))
        for h in hukumler if h["kosum_id"] not in susp])
    con.commit()
    # sözleşme (ilk kez)
    syol = os.path.join(repo, "veri", "sozlesme", "amb_olgu_kosum.json")
    if not os.path.exists(syol):
        cols = [{"ad": r[1], "tip": r[2] or "ANY", "not_null": bool(r[3]), "pk": bool(r[5])} for r in con.execute("PRAGMA table_info(amb_olgu_kosum)")]
        json.dump({"tablo": "amb_olgu_kosum", "surum": "0.1.0-deneysel-m29", "katman": "ambar", "grain": "1 satır = 1 işçi-ajan koşumu (Workflow/Agent alt-ajanı)", "kolonlar": cols,
                   "kural": "additive-only; token kolonları OTel gen_ai.usage.* eşleme sözlüğüne bağlanır (kolon adı olarak gömülmez)"}, open(syol, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    tsyol = os.path.join(repo, "veri", "sozlesme", "amb_olgu_tahmin.json")
    if not os.path.exists(tsyol):
        cols = [{"ad": r[1], "tip": r[2] or "ANY", "not_null": bool(r[3]), "pk": bool(r[5])} for r in con.execute("PRAGMA table_info(amb_olgu_tahmin)")]
        json.dump({"tablo": "amb_olgu_tahmin", "surum": "0.1.0-deneysel-m29", "katman": "ambar", "grain": "1 satır = 1 (görev-emri, rol) tahmini — aile-BAĞIMSIZ (KB-02; gerçek aile-bazlı, JOIN v_kosum_tahmin_sapma'da)", "kolonlar": cols,
                   "kural": "additive-only; üst model (fable) satırlarında tahmin alanları NULL; formül tahminlerde bant NULL + tahmin_formul_mu=1"}, open(tsyol, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    hsyol = os.path.join(repo, "veri", "sozlesme", "amb_olgu_kosum_sonuc.json")
    if not os.path.exists(hsyol):
        cols = [{"ad": r[1], "tip": r[2] or "ANY", "not_null": bool(r[3]), "pk": bool(r[5])} for r in con.execute("PRAGMA table_info(amb_olgu_kosum_sonuc)")]
        json.dump({"tablo": "amb_olgu_kosum_sonuc", "surum": "0.1.0-ONERI-karar52", "katman": "ambar", "grain": "1 satır = 1 ajan koşumunun done-yüklemi hükmü (PASS/FAIL)", "kolonlar": cols,
                   "kural": "ÖNERİ-damgalı alan (Salih 08-21 Karar 52; nihai Katman-1 şema imzası AÇIK); hüküm orkestratörce teslim-al adımında yazılır, transkriptten türetilmez"}, open(hsyol, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    testler = []
    for ad, sql in [("amb_olgu_kosum.kosum_id unique", "SELECT COUNT(*) FROM (SELECT kosum_id FROM amb_olgu_kosum GROUP BY kosum_id HAVING COUNT(*)>1)"),
                    ("amb_olgu_kosum.output_tokens not_null", "SELECT COUNT(*) FROM amb_olgu_kosum WHERE output_tokens IS NULL"),
                    ("amb_olgu_prompt → prompt 1:1", "SELECT ABS((SELECT COUNT(*) FROM amb_olgu_prompt)-(SELECT COUNT(*) FROM prompt))"),
                    ("amb_kopru_not_prompt.prompt_id → prompt", "SELECT COUNT(*) FROM amb_kopru_not_prompt k LEFT JOIN prompt p ON p.prompt_id=k.prompt_id WHERE p.prompt_id IS NULL"),
                    ("amb_olgu_tahmin.tahmin_id unique", "SELECT COUNT(*) FROM (SELECT tahmin_id FROM amb_olgu_tahmin GROUP BY tahmin_id HAVING COUNT(*)>1)"),
                    ("amb_olgu_tahmin.wf_id → amb_olgu_kosum", "SELECT COUNT(*) FROM amb_olgu_tahmin t WHERE t.wf_id IS NOT NULL AND NOT EXISTS (SELECT 1 FROM amb_olgu_kosum k WHERE k.wf_id=t.wf_id)"),
                    ("amb_olgu_kosum_sonuc.sonuc accepted_values", "SELECT COUNT(*) FROM amb_olgu_kosum_sonuc WHERE sonuc NOT IN ('PASS','FAIL')"),
                    ("amb_olgu_kosum_sonuc → amb_olgu_kosum (kosum_id ∨ wf_id; İB-50)", "SELECT COUNT(*) FROM amb_olgu_kosum_sonuc s LEFT JOIN amb_olgu_kosum k ON k.kosum_id=s.kosum_id LEFT JOIN (SELECT DISTINCT wf_id FROM amb_olgu_kosum WHERE wf_id IS NOT NULL AND wf_id<>'') w ON w.wf_id=s.wf_id WHERE k.kosum_id IS NULL AND w.wf_id IS NULL")]:
        n = con.execute(sql).fetchone()[0]; testler.append((ad, n, "PASS" if n == 0 else "ERROR"))
    # GOLD CSV
    gdir = os.path.join(repo, "veri", "gorunum")
    for v in ("v_amb_kosum_maliyet", "v_amb_acilis_brifi", "v_tartisma_notu", "v_kosum_tahmin_sapma", "v_skill_kosum"):
        cur = con.execute(f"SELECT * FROM {v}"); cols = [d[0] for d in cur.description]
        with open(os.path.join(gdir, f"{v}.csv"), "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh); w.writerow(cols); w.writerows(cur.fetchall())
    brif = con.execute("SELECT * FROM v_amb_acilis_brifi").fetchone(); bcols = [d[0] for d in con.execute("SELECT * FROM v_amb_acilis_brifi").description]
    n_kosum = con.execute("SELECT COUNT(*), COUNT(DISTINCT wf_id) FROM amb_olgu_kosum").fetchone()
    con.close()
    if not a.sessiz:
        print(f"ambar v0: amb_olgu_kosum {n_kosum[0]} ajan koşumu / {n_kosum[1]} workflow ({len(yeni)} yeni bronz olay) · amb_olgu_tahmin {len(tahminler)} tahmin · amb_olgu_kosum_sonuc {len(hukumler)} hüküm (ÖNERİ) · amb_olgu_prompt · amb_olgu_karar_borcu · görünümler amb_boyut_anahtar/amb_kopru_olay_nesne/amb_boyut_vardiya · martlar v_amb_kosum_maliyet + v_amb_acilis_brifi + v_kosum_tahmin_sapma + v_skill_kosum (CSV)")
        for t in testler: print(f"  [{t[2]}] {t[0]} ihlal {t[1]}")
        print("  açılış-brifi martı: " + " · ".join(f"{k}={str(v)[:60]}" for k, v in zip(bcols, brif)))
    sys.exit(3 if any(t[2] == "ERROR" for t in testler) else 0)


if __name__ == "__main__":
    main()
