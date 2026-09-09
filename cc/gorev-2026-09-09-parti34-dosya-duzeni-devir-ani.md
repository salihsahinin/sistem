# Görev Emri — Parti 3-4 dosya düzeni (`cc/` + `raporlar/`) + devir-anı loglayıcı (İB-75 ortak ilk adım) — Opus 5 medium lider

*Derleyen: Carvis/Fable (ana-sıra), gorev-emri-derleme, 2026-09-09 ~12:30. Kaynak: Salih Katman-1 emri + ağaç onayı 09-09 ("dosya düzeni … gezilebilir, anlaşılabilir; artık kullanılmayan dosyaları uygun klasörlerde topla" · "ağaç formatı için onay veriyorum") · plan `kuyruk/dosya-duzeni-plani-2026-09-09.md` (parti 1-2 TAMAM 289f53c) · İB-75 raporu §4 devir-anı yüklemi + §8 "üç modelin ortak ilk adımı = yüklemin loglanması" · Karar 89 (Opus lider medium) · Karar 90 (tek koşumluk ölçüm, fazla test yok). Rejim: maliyet-öncelikli (mekanik taşıma). Salih 09-09 12:2x: "gelen görev devrine yeni teslim görevi oluştur (icra edilmesi gereken görev varsa)".*

## KİMLİK
gorev_adi:        parti34-dosya-duzeni-devir-ani
rol:              lider (Opus 5 medium) + işçi (Sonnet low/medium)
cagri_kosulu:     Karar 89 rejimi 2. koşumu; Opus yan-oturumu açılınca (prompt `cc/prompt-2026-09-09-opus-lider-parti34.md`)
rejim:            maliyet-öncelikli
model:            lider Opus 5 medium · işçi Sonnet (U1a/U1b/U2 low-medium) · hakem YOK (mekanik iş; doğrulama = script kapıları)
kosum_profili:    Fable yazdı (KB-02). Lider Opus medium 1 çağrı, bağlam ≈30k, çıktı 4-6k `[?]`. İşçi Sonnet 3 birim × 12-18 araç çağrısı (taşıma işi çağrı-yoğun; tavan 20), işçi dönüşü ≤2k, toplam ≈60-80k out `[?]`. Fren: ajan ≤36/wf · çağrı ≤54/ajan (m.46).

## GİRDİLER
plan:                 `kuyruk/dosya-duzeni-plani-2026-09-09.md` (hedef ağaç + parti tablosu)
envanter_cc:          git ls-files cc → üst seviye: rapor-* 194 · gorev-* 119 · pipeline-* 16 · devir-* 4 · prompt-* 3 · tekil (defter.md, README.md, oran-*, karar-onerisi-*, 1 .py) · alt dizinler workflow/ 15 · d2-eval/ 15 · denetci-kalibrasyon/ 13 · kanit-bulucu/ 11
envanter_raporlar:    git ls-files raporlar → tarihli konu raporları 2026-07: 78 · 2026-08: 73 · 2026-09: 13 · vardiya-teslim-* 47 · seans-teslim-* 26 · hareket-gunlugu-* 23 · gorsel-* 11 · masa-* 9 · jarvis-* 8 · paralel/zihin/yuzey/son/skill tekiller · usage/ 3
sabit_yol_yazanlar:   raporlar/: 15 script + 2 hook + 5 SKILL.md · cc/: 18 script + 6 SKILL.md (tam liste: `grep -ln "raporlar/" tools/*.py .claude/hooks/*.sh .claude/skills/*/SKILL.md` ve `grep -ln "cc/rapor\|cc/gorev\|cc/devir\|cc/pipeline" tools/*.py .claude/skills/*/SKILL.md`)
ledger_kaynak:        `veri/karar-borcu.jsonl` içinde cc/ + raporlar/ pointer 138
devir_ani_yuklemi:    İB-75 raporu §4 (`raporlar/2026-09-09-ib75-baglam-devri-ekip-lideri.md`, m.38 boolean; E2 = 600.000 `[?]`) · veri: `veri/gorunum/v_baglam_seyri.csv` (oturum_kisa, max_baglam, tur_128k_ustu …) + `veri/bronz/baglam-olay.jsonl`

## BAĞLAM-MANİFESTİ
eager:            bu emir · plan dosyası · İB-75 raporu §4 (yalnız yüklem bölümü, ~40 satır)
lazy:             sabit-yol grep sonuçları (U1 başında) · `tools/pointer-kayma.py --help` · `tools/katman-hatti.py` adım listesi (U2'de adım eklerken)
butce:            lider ≤30k · işçi ≤15k girdi · toplam çıktı ≤80k `[?]`

## SINIRLAR
kapsamda:         **U1a `cc/`:** `cc/rapor-YYYY-MM-DD-*.md` → `cc/rapor/YYYY-MM/` · `cc/gorev-YYYY-MM-DD-*.md` → `cc/gorev/YYYY-MM/` · `cc/devir-*` → `cc/devir/` · `cc/prompt-*` → `cc/prompt/` · `cc/pipeline-*` → `cc/pipeline/` · tekiller (`defter.md`, `README.md`, `oran-*`, `karar-onerisi-*`, `.py`) YERİNDE; alt dizinler (workflow/ d2-eval/ denetci-kalibrasyon/ kanit-bulucu/) YERİNDE. **U1b `raporlar/`:** `seans-teslim-*` → `raporlar/seans/` · `vardiya-teslim-*` → `raporlar/vardiya/` · `hareket-gunlugu-*` → `raporlar/hareket/` · `masa-*` → `raporlar/masa/` · `gorsel-*` → `raporlar/gorsel/` · `jarvis-*` → `raporlar/jarvis/` · tarihli konu raporları `YYYY-MM-DD-*` → `raporlar/YYYY-MM/` · `usage/` yerinde · tekiller (paralel/zihin/yuzey/son-50/skill) → en yakın sınıf, kararsızsa `raporlar/diger/`. Dosya ADLARI değişmez (yalnız dizin). Hepsi `git mv`. **U1c sabit yollar:** `tools/*.py` + `.claude/hooks/*.sh` içindeki `cc/`/`raporlar/` yolları yeni yapıya (glob'lar recursive: `raporlar/**/hareket-gunlugu-*.md`; YAZAN script'ler yeni alt dizine yazar: `hareket-tablo.py` → `raporlar/hareket/`, `sunum-son50.py` → `raporlar/YYYY-MM/`, gorev-emri teslim adresi `cc/rapor/YYYY-MM/`) · ledger `kaynak` 138 pointer · md pointer'ları (`kuyruk/`, `wiki/`, `arsiv/`, `fikir-kutusu.md`, `KILAVUZ.md`, `README.md`, `tools/SCRIPTLER.md`) · her yeni alt dizine 3-5 satır `README.md`. **U2 devir-anı loglayıcı:** `tools/devir-ani.py` (stdlib): İB-75 §4 yüklemini `v_baglam_seyri` + `baglam-olay` üzerinden oturum başına hesaplar → `veri/bronz/devir-ani-olay.jsonl` (ts, oturum, max_baglam, tur_128k_ustu, yuklem_sonucu bool, tetikleyen_koşul, E2) — ATEŞLEMEZ, yalnız loglar; `katman-hatti.py`'ye adım (uyarı kanalı, hat düşürmez); 3 test (`tools/testler/test_devir_ani.py`: eşik altı False · eşik üstü True · determinizm); `tools/SCRIPTLER.md` satırı.
kapsam_disi:      `core/`, `CLAUDE.md`, `.claude/skills/*/SKILL.md`, `.claude/hooks/*.sh` YAZIMI (Bash teli + m.41: yan-oturum kanona yazmaz) → bu dosyalardaki gerekli yol değişikliklerini devir notunda "ana-sıra uygular" listesi olarak ver (dosya:satır · eski → yeni); `veri/` altındaki bronz/silver/gold içeriği (katman-hatti kendisi yeniden türetir); `arsiv/` (parti 1-2 bitti); `ogrenme/`; devir-anı yükleminin ATEŞLENMESİ / lider kuruluşu (masa-10 hükmü); E2 eşiğini değiştirmek (Q2 Salih'te — 600.000 `[?]` sabit, kaynağı rapora pointer).
araclar:          git mv · Read/Grep/Edit (tools/, kuyruk/, wiki/, arsiv/, raporlar/, cc/ serbest) · `python3 tools/pointer-kayma.py --ref HEAD` · `python3 tools/karar-borcu-tablo.py` · `python3 -m unittest discover -s tools/testler -p 'test_*.py'` · `python3 tools/katman-hatti.py` · `python3 tools/silver-saglik.py --kapi` · sqlite3 salt-okur
degismezler:      silme YOK (m.8; yalnız git mv) · dosya adı değişmez · `git add <yol>` / `git mv` (başka oturumlar açık; `git add -A` YASAK) · commit parti başına ayrı, mesaj İngilizce `[icra] …`, push YOK (m.9) · işçi çağrıları SENKRON · parti bitmeden kapı: testler yeşil ∧ pointer-kayma KIRIK 0 ∧ karar-borcu kırık 0 ∧ silver-saglik --kapi exit 0 (YETİM sayısı raporlanır, engel değil) · rakam kaynaklı, kestirim `[?]` · uydurma yok

## DALLAR
D1: eğer bir script'in yolu kanon dosyasında (core/.claude) tanımlıysa → script değiştirilmez, devir notuna "ana-sıra uygular" satırı; aksi → işçi düzeltir.
D2: eğer katman-hatti parti sonrası exit≠0 ∧ neden taşınan yol → yol düzeltilir, yeniden koşulur (≤3 tur); neden başka → DUR, devir notuna, o parti commit'lenmez.
D3: eğer pointer-kayma bir dosyada KAYMIŞ pointer verir ∧ öneri tek → uygula; öneri yok → devir notuna "elle" listesi.
D4: eğer U2 için `v_baglam_seyri` yüklemin istediği bir alanı taşımıyorsa → alan `baglam-olay.jsonl`'den türetilir; türetilemiyorsa yüklemin o koşulu `[?]` damgalı `None` döner, script düşmez.
D-KATMAN1: taşıma sırasında bir dosyanın "artık kullanılmıyor → karantina" adayı olduğu görülürse → TAŞIMA YAPILMAZ, devir notuna aday listesi (tescil yetkisi Salih, İB-72).

## ÇIKTI SÖZLEŞMESİ
halusinasyon_derecesi: H = 0 (`derece.py` aktif değişken yok: atıf/kaynak/sayısal iddia üretimi yok, çıktı = dosya taşıma + script; v8 doğrulayıcı var) → GEREKMEZ; `halusinasyon-engelleyici` çağrılmaz.
cikti_bicimi:     (1) parti-3 commit (cc/) · (2) parti-4 commit (raporlar/) · (3) U2 commit (devir-ani.py + test + katman-hatti adımı + SCRIPTLER) · (4) `cc/devir/devir-2026-09-09-opus-parti34.md` (geri-dönüş şeması İB-75 §6): biten/kalan tablo · "ana-sıra uygular" listesi (core/.claude yol değişiklikleri, dosya:satır) · YETİM önce/sonra · karantina adayları · ajan sayacı · sapmalar.
done_yuklemi:     cc/ üst seviyede yalnız tekiller + alt dizinler kaldı ∧ raporlar/ üst seviyede yalnız usage/ + alt dizinler ∧ tüm alt dizinlerde README ∧ testler yeşil ∧ pointer-kayma KIRIK 0 ∧ karar-borcu kırık 0 ∧ silver-saglik --kapi exit 0 ∧ devir-ani-olay.jsonl ≥1 satır ∧ kanon yazımı = 0 ∧ devir dosyası VAR.
done_olcumu:      DRFR — 9 koşul tek tek.
yeniden_deneme:   3

## KANONDA-BİLİNENLER
- Parti 1-2 (289f53c): kök 6 dosya, `arsiv/` tek çatı; 9 script yeniden yollandı; ders: blanket `sed` plan cümlesini bozdu (parti-2 işçisi elle düzeltti) → yol değişimini `sed` ile değil dosya-dosya doğrulayarak yap; `kuyruk/arsiv/karantina` önce çevrildi (çift dönüşüm freni).
- Hareket kütüğü (`hareket-tablo.py`) her seans `raporlar/hareket-gunlugu-*.md` YAZAR; taşıma sonrası yazma yolu değişmezse günlükler eski konuma düşer → U1c zorunlu.
- Silver `dosya_id` = yol; taşıma sonrası eski kayıtlar YETİM adayı (bugün 385); katman-hatti yeniden ingest eder; sayı raporlanır, engel değil (plan §Silver).
- İB-75 §8: A/B/C üç modelin ortak ilk adımı devir-anı yükleminin loglanması; §4 yüklem E2 = 600.000 `[?]` (Q2 Salih'te); masa-10 D seçeneği (doğrudan hedef) tartışılıyor — U2 buna da hizmet eder (ölçüm aygıtı).
- Karar 90: tek koşumluk ölçüm yeter; U2 fazladan test üretmez (3 test tavan).
- GEÇMİŞ YÖRÜNGE: `deneyim-tablo.py --benzer "dosya taşıma git mv pointer"` koşulmadı (mekanik iş, benzer yörünge aranmadı — deneyim: 0, uydurma yok).

## SKILL TETİKLERİ
yok (işçiler Agent aracıyla doğrudan; skill çağrısı yok).

## Teslim
Commit'ler + `cc/devir/devir-2026-09-09-opus-parti34.md` (emir yolu kazanır — Karar 88 M7 ⑤). Manifest: `veri/manifest/u9-parti34-dosya-duzeni.json` (`tur: pipeline`; yazar: cc/**, raporlar/**, tools/*.py, tools/testler/test_devir_ani.py, tools/SCRIPTLER.md, veri/karar-borcu.jsonl, kuyruk/*.md, wiki/*.md, arsiv/**, README.md, KILAVUZ.md, fikir-kutusu.md; okur: veri/gorunum, veri/bronz).

## DİNAMİK EK
tarih: 2026-09-09 ~12:30 · HEAD: 289f53c · tetikleyen: Salih "gelen görev devrine yeni teslim görevi oluştur" · paralel oturumlar AÇIK (H4) · halusinasyon_derecesi: 0.
