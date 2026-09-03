# İcra yan-oturumu prompt'u — 2026-09-03 akşam (derleyen: Carvis/Fable ana oturum, HEAD 7339271)

*Salih bu dosyanın "PROMPT" bölümünü kopyalayıp Cowork'ta açacağı yeni oturuma yapıştırır. Çıktı ana oturuma (Fable) devir dosyasıyla döner; push ana oturumdan atılır.*

## Kurulum kararı (Fable planlayıcı; Salih hükmü masa M1'de kayda geçer)

| Alan | Karar | Gerekçe |
|---|---|---|
| **Klasör** | `~/jarvis` (aynı çalışma ağacı, worktree YOK) | U1 galeri birimi `kuyruk/galeri-siralama/` + `../ders-gbm/.venv`'e bağlı; 08-31 Opus icra emsali de `~/jarvis`'teydi. Çakışma freni: H4 `git add <yol>`, paralel-kapi. Worktree yalnız gnhf/sensiz koşumda (E-1). |
| **Model** | **Sonnet 5** (`claude-sonnet-5`) | Karar 85/86: işçi = Sonnet, karar yetkisi sıfır; ikinci Fable = 2× Fable tokeni (D2-b 09-02'de RET). Planlama bu dosyada Fable'ca bitti; oturumun işi orkestrasyon + koşum. |
| **Effort** | **medium** (işçi ajanlar **low**) | Karar 86 D2: "Sonnet low-medium". Orkestre eden oturum medium (manifest/kapı okuması), işçi CASE'leri kapalı uçlu → low. High sonucu değiştirmez (m.4). |
| **Biçim** | **PIPELINE** — loop DEĞİL, nested loop DEĞİL | Birimler sonlu + done-yüklemli (İB-65 M1 yüklem-ağacı: tetik=seans, iterasyon ayak izi sabit → pipeline). Loop yalnız değişmez-koruma sınıfı (Karar 86 D2); nested → katman-fren sayacı (İB-76) açıkken tek atlası bile zor bitiriyor (08-31 devir §2). Kademe N 1→2→3, aile ≤3, işçi SENKRON. |
| **Fren** | ajan-fren UYARI 72 / DURDUR 144 (hook env varsayılanı) | DURDUR'a çarparsa devir notu yazıp DURUR; eşik oynatmak Katman-1. |

**m.16 çelişki notu:** Karar 86 D2(a) "icra = TEK Fable ana oturumu + Sonnet işçi pipeline'ı" der; Salih 09-03 akşam paralel Cowork icra oturumu istedi. Uzlaştıran okuma: Karar 84 EK(2) "izlenen nöbet → AYRI OTURUM, prompt Carvis'ten" + Karar 86 D2 Salih notu "Fable bağlamı büyüdü, Sonnet'e devret". Oturum **Sonnet** olduğu sürece D2(a)'nın ruhu (Fable tek planlayıcı, Sonnet işçi) korunur; **Fable** seçilirse D2(b) canlanır → masa hükmü gerekir. Hüküm masa **M1**.

---

## PROMPT (buradan aşağısını yapıştır)

seans başı jarvis geliştirme — İCRA YAN-OTURUMU (Sonnet 5, effort medium). Kurallar önce:

1. **Yetki (m.41):** Sen yan-oturumsun ve İŞÇİ-ORKESTRATÖRSÜN; KARAR ALMAZSIN, kanona (`core/`, `CLAUDE.md`, tüzük, kapsül, pano, `.claude/`) YAZMAZSIN. `git push` YASAK (m.9). Ana oturum (Fable) CANLI → her commit `git add <dosya-yolu>`; `git add -A` YASAK (H4). Kanonla çelişki ya da tanımsız seçim görürsen o birimi DURDUR, devir notuna yaz, sonraki birime geç — soru sorma, tahmin yürütme.
2. **Token (Salih 08-15):** işçi-ajan = Sonnet, effort low, bütçe 10-15 araç çağrısı; eşzamanlı aile ≤3; kademe N 1→2→3. Tek araç çıktısı >~10k token bağlama dökülmez → dosyaya yaz + pointer (KB-50). ≥15 satır python → scratchpad'de `.py` dosyası, heredoc değil (Karar 77).
3. **Koşum-önü kapı:** başlamadan `git log -15` + `veri/manifest/*.json` oku. Her birim için ÖNCE manifest yaz (`veri/manifest/<birim>.json`, İB-63 şeması — örnek `ib-58-erisim-fts-axi.json`), sonra `python3 tools/paralel-kapi.py` (kullanım `tools/SCRIPTLER.md`); SIRALI/RED/BEKLE diyorsa uy. Ayak izi çakışan birimler aynı anda koşmaz.
4. **Anakronizm (Karar 68):** her rapor AS-OF damgalı; her rakam kaynaklı (m.39); deneysel damga (m.29). Atıf/URL yoğun çıktı yok bu listede → halüsinasyon zinciri gerekmez.

**İş listesi (kademe sırası; hepsi karar-gerektirmeyen icra borcu, kaynak `core/durum-kapsulu.md` "Sonraki ilk iş" + `veri/karar-borcu.jsonl`):**

**Kademe 1 (N=1 → 2):**
- **U1 · Galeri şeridi yarım birim (jarvis-DIŞI, md.49; `kuyruk/galeri-siralama/` COMMIT'LENMEZ — Karar 73 EK).** Reçete `cc/devir-2026-09-02-opus-galeri-yaprak-doluluk.md` §2 (bash bloğu aynen) + §2'deki 2 risk uyarısı (indeks/kolon çakışması; SHAP belleği → `--lot 60`). Done: `yeni-trim.html` üretildi ∧ 4 sekme dolu ∧ ekip notuna §18 yazıldı (SHAP↔Spearman tablosu + odak-galeri okuması). Teslim: tam mutlak yol + `open -R`. §6'daki 5 soruya CEVAP VERME — masa kalemi (M6).
- **U2 · İB-71 baseline: kod/md oranı ölçümü (m.39).** Yeni script `tools/kod-orani-olcum.py` (stdlib, LLM yok, AXI A1/A2/A7: `--json`, çıkış sözlüğü, FAIL-LOUD): (i) repo envanteri — uzantıya göre dosya/satır/bayt (`md` · `py/sh/sql` · `json/jsonl/csv` · diğer), `.git`/`veri/bronz`/`veri/gorunum` hariç; (ii) bağlam-penceresi proxy'si — `veri/bronz/hareket-olay.jsonl` son 3 günde Read/cat/sed ile açılan dosyaların türe göre dağılımı (okunan satır varsa onunla ağırlıklı); (iii) sonuç `veri/kod-orani.jsonl`e 1 satır (tarih, git_head, iki oran) + `raporlar/2026-09-03-ib71-kod-orani-baseline.md`. Done: script `--json` çalışıyor ∧ unittest `tools/testler/test_kod_orani.py` ≥3 test yeşil ∧ SCRIPTLER satırı ∧ rapor. Tur önerisi YAZMA (Fable/masa işi).

**Kademe 2 (U1+U2 bitince; N ≤ 2):**
- **U3 · İB-72 bayat-dosya karantina mekanizması (D8 sırası 72 ilk).** Tescil yetkisi Salih'te — sen yalnız MEKANİZMAYI kur, dosya tescil ETME. (i) `veri/karantina.jsonl` şeması: `{yol, tescil_tarihi, salih_beyani, neden, git_head}`; (ii) `tools/karantina.py` — `--ekle <yol> --beyan "<Salih sözü>"` (dosyayı `kuyruk/arsiv/karantina/<yol>` altına `git mv`, satır ekle; silme YOK m.8) · `--liste` · `--denetle` (katman-hatti ingest yolları ve `erisim-fts.py --insa` girdilerinin karantina dizinini okumadığını doğrular, okuyorsa FAIL-LOUD); (iii) `tools/katman-hatti.py` + `tools/erisim-fts.py` tarama yollarına `kuyruk/arsiv/karantina/` dışlaması (en küçük diff; mevcut dışlama listesi varsa ona ekle); (iv) `tools/testler/test_karantina.py` ≥3 test; (v) SCRIPTLER + `veri/README.md` satırı. Done: testler yeşil ∧ `--denetle` PASS ∧ mevcut 82 test hâlâ yeşil (`python3 -m unittest discover -s tools/testler -p 'test_*.py'`).
- **U4 · İB-70 ilk kod-optimizasyon turu (RAPOR, kod değişikliği YOK).** Kapsam: `tools/*.py` · `.claude/hooks/*.sh` (salt-okur) · `cc/workflow/`. Her dosya için: satır sayısı, tekrar eden yardımcılar, ölü kod, en pahalı yol (silver okuma/yazma), önerilen değişiklik + risk. Çıktı `raporlar/2026-09-03-ib70-kod-optimizasyon-tur1.md` (tablo; ≤120 satır). Tur aralığı ÖNERME — masa kalemi.

**Kademe 3 (U3+U4 bitince; N ≤ 3):**
- **U5 · T-A katmanlı triyaj scripti (Karar 83 B3; defter satır 195 "B3 (a)").** Girdi: `tools/silver-saglik.py` T-A-ONELEME çiftleri (`veri/silver-saglik.jsonl` son koşum ∨ script'in ürettiği aday listesi). `tools/ta-triyaj.py`: deterministik ön-sınıflandırma (aynı-dosya/aynı-anahtar/çapraz-dosya sınıfları + şiddet puanı = uzunluk-farkı × tekrar-sayısı gibi ölçülebilir, LLM yok) → şiddet-sıralı ilk 20 → `raporlar/2026-09-03-ta-triyaj-ilk20.md`. Done: script `--json` ∧ ilk-20 tablosu ∧ ≥2 test. Şiddet formülü belirsizse RAPORDA formülü yaz, seçimi masaya bırak.
- **U6 · İB-04 wiki: 2 sayfa** (`wiki-sayfa-yaz` skill'i; 6-blok şablon + index + [[link]]): `gnhf.md` ve `lavish.md` (mevcut sayfalar: `wiki/README.md`; `no-mistakes.md` var, tekrar yazma). Kaynak: KILAVUZ + Karar 84/84-EK + `~/.agents/skills/lavish/SKILL.md`. Done: 2 sayfa + index satırı.
- **U7 · İB-64a/b/c görev emirleri DERLEME (koşum YOK)** — `gorev-emri-derleme` skill'i; kaynak ledger satırları (`grep 'İB-64' veri/karar-borcu.jsonl`) + K-010 kartı (`core/pano.md`, salt-okur) + `kuyruk/k010-zincir-2026-08-29.md`. Çıktı `cc/gorev-2026-09-03-ib64{a,b,c}-*.md` (m.40b tam kontrat: yapan≠ölçen · V26 kotası · ≥2 birincil kaynak). Done: 3 emir dosyası künyeli.

**KOŞULMAYACAK (bilgi):** erisim-fts AXI (İB-58/3) manifest `tamam`, commit f3240ad — kapsül satırı bayat; atlama. İB-73 eğitim serisi, İB-75 ekip-lideri, damıtma → Fable/masa.

**Teslim usulü (her birim):** rapor Türkçe, künyeli, AS-OF damgalı → yolu yukarıda; manifest `durum` güncelle; birim başına ayrı `[icra]` commit (`git add <yol>`, mesaj İngilizce m.10, sonuna `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`); testler kırıksa commit ATMA, devir notuna yaz.

**Kapanış:** tüm birimler bitince (ya da fren/engel nedeniyle durunca) DEVİR DOSYASI: `cc/devir-2026-09-03-sonnet-icra-cowork.md` — biten/kalan tablo (birim · durum · rapor · commit sha), fren sayacı son değeri, devir notları, masaya çıkan sorular. Push ATMA; "devir hazır" de ve DUR. Seans-kapanış ritüeli KOŞMA (ana oturumun işi).

---

## Ana oturum (Fable) dönüş kontrol listesi
- [ ] Devir + raporlar okunur, çelişki kapısı
- [ ] U2 oranları İB-71 ledger'a; U3 ilk tescil adayı (gorsellestir arşivi) masa M10 hükmüne bağlanır
- [ ] U5 ilk-20 tablosu sonraki masaya
- [ ] Commit'ler doğrulanır → push Salih beyanıyla
