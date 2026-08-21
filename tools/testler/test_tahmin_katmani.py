#!/usr/bin/env python3
"""test_tahmin_katmani.py — tahmin↔gerçek ambar katmanı testleri (KB-02/03 icra; pipeline cc/pipeline-2026-08-21-tahmin-gercek-ambar.md SH-1).

Desen: test_kolon_katmani.py kalıbı — geçici repo'da küçük silver + bronz kur, GERÇEK script'i (tools/ambar-tablo.py) CLI olarak koştur,
üretilen görünüm/CSV/sözleşmeyi doğrula. Repo verisine DOKUNULMAZ. Koşum: python3 -m unittest discover -s tools/testler -p 'test_*.py' -v
"""
import csv, json, os, shutil, sqlite3, subprocess, sys, tempfile, unittest

ARACLAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def kos(script, *args):
    """Gerçek script'i alt-süreç olarak koştur (CLI sözleşmesi test edilir)."""
    return subprocess.run([sys.executable, os.path.join(ARACLAR, script), *args], capture_output=True, text=True)


def kucuk_repo(kok):
    """Geçici repo iskeleti: ambar-tablo.py'nin okuduğu tüm silver tabloların küçük alt-kümesi + bronz kütükler."""
    for d in ("veri/bronz", "veri/gorunum", "veri/sozlesme"):
        os.makedirs(os.path.join(kok, d), exist_ok=True)
    con = sqlite3.connect(os.path.join(kok, "veri", "baglam.sqlite"))
    con.executescript("""
    CREATE TABLE prompt (prompt_id TEXT, oturum_id TEXT, sira INT, tur TEXT, sonraki_skill TEXT, sonraki_model TEXT,
                         uzunluk_kar INT, kelime INT, metin_kisa TEXT, ts_utc TEXT, ts_tr TEXT, yuklendi_head TEXT);
    INSERT INTO prompt VALUES ('p1','o1',1,'emir','pipeline-kosum,gorev-emri-derleme','claude-fable-5',40,8,'pipeline kur','2026-08-21T09:00:00+00:00','2026-08-21 12:00:00','test123');
    CREATE TABLE karar_borcu (borc_id TEXT, kume TEXT, katman INT, karar_sahibi TEXT, durum TEXT, tur TEXT, masa_sirasi INT,
                              kayit_tarihi TEXT, snapshot_tarih TEXT, snapshot_sha TEXT, baslik TEXT);
    INSERT INTO karar_borcu VALUES ('KB-T1','test',1,'Salih','masaya','test',1,'2026-08-21','2026-08-21','test123','test kalemi');
    CREATE TABLE anahtar (anahtar_id TEXT, tur TEXT, deger TEXT, durum TEXT, replaced_by TEXT, gecerli_bas TEXT,
                          gecerli_bitis TEXT, ilk_gorulme TEXT, referans_sayisi INT, sicak_referans_sayisi INT);
    CREATE TABLE kayit (kayit_id TEXT, dosya_id TEXT, tarih_iso TEXT);
    CREATE TABLE referans (kayit_id TEXT, ref_deger TEXT, ref_turu TEXT, hedef_var INT);
    CREATE TABLE dosya (dosya_id TEXT, katman TEXT, tur TEXT, baslik TEXT, ilk_commit TEXT, boyut_bytes INT);
    """)
    con.commit(); con.close()
    # bronz koşum: aynı wf'de iki aile — tahmin aile-BAĞIMSIZ, gerçek aile-bazlı (JOIN yayılımı test edilir)
    ortak = {"agent_type": "atlas", "oturum": "o1", "modeller": "claude-opus-5", "ts_bas": "2026-08-21T09:00:00Z",
             "ts_son": "2026-08-21T09:05:00Z", "asistan_mesaj": 5, "input_tokens": 1000, "cache_read_input_tokens": 0,
             "cache_creation_input_tokens": 50000, "ilk_prompt_kisa": "test", "kaynak_dosya": "x", "yuklendi_head": "test123",
             "yuklendi_ts": "2026-08-21T09:06:00+00:00"}
    with open(os.path.join(kok, "veri", "bronz", "kosum-olay.jsonl"), "w", encoding="utf-8") as fh:
        fh.write("# test bronz koşum\n")
        fh.write(json.dumps({"kosum_id": "wf_test1:a1", "wf_id": "wf_test1", "agent_id": "a1", "aile": "A",
                             "rol": "Atlas TEZ araştırmacısı", "sure_sn": 300, "arac_cagrisi": 18, "output_tokens": 12000, **ortak}, ensure_ascii=False) + "\n")
        fh.write(json.dumps({"kosum_id": "wf_test1:a2", "wf_id": "wf_test1", "agent_id": "a2", "aile": "B",
                             "rol": "Atlas TEZ araştırmacısı", "sure_sn": 400, "arac_cagrisi": 22, "output_tokens": 20000, **ortak}, ensure_ascii=False) + "\n")
    # bronz tahmin: (1) bantlı TEZ (wf eşleşir) · (2) formül V26 (wf NULL — koşum-öncesi yazım deseni)
    with open(os.path.join(kok, "veri", "bronz", "tahmin-olay.jsonl"), "w", encoding="utf-8") as fh:
        fh.write("# test bronz tahmin\n")
        fh.write(json.dumps({"tahmin_id": "cc/gorev-test.md:TEZ", "gorev_emri_dosya": "cc/gorev-test.md", "gorev_emri_satir": 6,
                             "rol": "TEZ", "model_sinifi": "opus", "effort": "medium", "tahmin_cikti_min": 10000, "tahmin_cikti_max": 15000,
                             "tahmin_girdi_min": None, "tahmin_girdi_max": None, "tahmin_arac_min": 15, "tahmin_arac_max": 20,
                             "tahmin_sure_min_sn": 240, "tahmin_sure_max_sn": 360, "tahmin_serbest_metin": "10-15k · 15-20 araç · 4-6 dk",
                             "tahmin_formul_mu": False, "tahmin_kaynagi": "test", "wf_id": "wf_test1", "kaynak_rapor_dosya": None,
                             "kaynak_rapor_satir": None, "yuklendi_head": "test123", "yuklendi_ts": "2026-08-21T09:06:00+00:00"}, ensure_ascii=False) + "\n")
        fh.write(json.dumps({"tahmin_id": "cc/gorev-test.md:V26", "gorev_emri_dosya": "cc/gorev-test.md", "gorev_emri_satir": 6,
                             "rol": "V26", "model_sinifi": "sonnet", "effort": "low", "tahmin_cikti_min": None, "tahmin_cikti_max": None,
                             "tahmin_girdi_min": None, "tahmin_girdi_max": None, "tahmin_arac_min": None, "tahmin_arac_max": None,
                             "tahmin_sure_min_sn": None, "tahmin_sure_max_sn": None, "tahmin_serbest_metin": "≈0,7k × denetim",
                             "tahmin_formul_mu": True, "tahmin_kaynagi": "İB-19", "wf_id": None, "kaynak_rapor_dosya": None,
                             "kaynak_rapor_satir": None, "yuklendi_head": "test123", "yuklendi_ts": "2026-08-21T09:06:00+00:00"}, ensure_ascii=False) + "\n")


class TahminKatmaniTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp(prefix="tahmin-test-")
        cls.bos_proje = tempfile.mkdtemp(prefix="tahmin-test-proje-")  # alt-ajan transkripti yok
        kucuk_repo(cls.tmp)
        cls.r = kos("ambar-tablo.py", "--repo", cls.tmp, "--proje-dizin", cls.bos_proje, "--sessiz")
        cls.db = os.path.join(cls.tmp, "veri", "baglam.sqlite")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True); shutil.rmtree(cls.bos_proje, ignore_errors=True)

    def test_kosum_temiz_cikti(self):
        self.assertEqual(self.r.returncode, 0, f"stderr: {self.r.stderr}\nstdout: {self.r.stdout}")

    def test_silver_tahmin_yuklendi(self):
        con = sqlite3.connect(self.db)
        self.assertEqual(con.execute("SELECT COUNT(*) FROM amb_olgu_tahmin").fetchone()[0], 2)
        self.assertEqual(con.execute("SELECT tahmin_formul_mu FROM amb_olgu_tahmin WHERE rol='V26'").fetchone()[0], 1)
        con.close()

    def test_sapma_gorunumu_aile_yayilimi_ve_durumlar(self):
        # tahmin 1 satır (TEZ) → 2 sapma satırı (aile A BANDA, aile B ÜSTÜNDE); formül satırı FORMÜL + gerçek NULL
        con = sqlite3.connect(self.db)
        satirlar = con.execute("SELECT aile, cikti_durum, arac_durum, sure_durum FROM v_kosum_tahmin_sapma WHERE rol='TEZ' ORDER BY aile").fetchall()
        self.assertEqual(satirlar, [("A", "BANDA", "BANDA", "BANDA"), ("B", "ÜSTÜNDE", "ÜSTÜNDE", "ÜSTÜNDE")])
        self.assertEqual(con.execute("SELECT cikti_durum FROM v_kosum_tahmin_sapma WHERE rol='V26'").fetchone()[0], "FORMÜL")
        con.close()

    def test_skill_kosum_iki_blok(self):
        con = sqlite3.connect(self.db)
        # ana-sıra bloğu: virgüllü skill json_each ile atomik satırlara ayrılır
        skiller = {r[0] for r in con.execute("SELECT skill FROM v_skill_kosum WHERE kaynak='ana-sira-prompt'")}
        self.assertEqual(skiller, {"pipeline-kosum", "gorev-emri-derleme"})
        # vekil blok: yalnız KESİN eşleme (atlas → atlas-kosum); token/süre toplanır
        n, tok = con.execute("SELECT n, output_tokens FROM v_skill_kosum WHERE kaynak='ajan-kosum-vekil' AND skill='atlas-kosum'").fetchone()
        self.assertEqual((n, tok), (2, 32000))
        con.close()

    def test_gold_csv_ve_sozlesme(self):
        for ad in ("v_kosum_tahmin_sapma", "v_skill_kosum"):
            yol = os.path.join(self.tmp, "veri", "gorunum", f"{ad}.csv")
            self.assertTrue(os.path.exists(yol), f"{ad}.csv üretilmedi")
            with open(yol, encoding="utf-8") as fh:
                self.assertGreater(len(list(csv.reader(fh))), 1, f"{ad}.csv başlıktan ibaret")
        sz = os.path.join(self.tmp, "veri", "sozlesme", "amb_olgu_tahmin.json")
        self.assertTrue(os.path.exists(sz), "amb_olgu_tahmin.json sözleşmesi yazılmadı")
        self.assertEqual(json.load(open(sz))["tablo"], "amb_olgu_tahmin")


if __name__ == "__main__":
    unittest.main()
