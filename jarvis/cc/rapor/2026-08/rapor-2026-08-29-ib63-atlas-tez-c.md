# İB-63 Atlas — Tez C (İÇ ENVANTER): İş birimlerinin OKUMA/YAZMA ayak-izi + fren envanteri + çakışma-matrisi taslağı

*Üretici: İç-envanter ajanı (Aile C, repo-içi analiz; web kullanılmadı). AS-OF 2026-08-29. Emir: `cc/gorev-2026-08-29-ib63-paralel-pipeline-atlas.md` §Aile-C. Bu rapor HAM VERİDİR — karar içermez; hüküm karar masasında.*

## 0. Sayım özeti (kaynaklı)

| Sayı | Ne | Kaynak |
|---|---|---|
| **22** | Ledger-açık borç satırı (17 İB + 5 KB) | `sqlite3 veri/baglam.sqlite "SELECT COUNT(*) FROM karar_borcu WHERE durum NOT IN ('kapandı')"` → 22 |
| **10** | Kapsül "paralel havuz" kalemi (İB-47·51·54·55·56·57·58·59·60·61) | `core/durum-kapsulu.md:23` |
| **7** | Havuz kaleminden ledger'da HİÇ satırı olmayan (İB-55..İB-61) | `veri/karar-borcu.jsonl` 116 satır, son borc_id İB-54 (`grep -o '"borc_id"' \| sort -u`) |
| **≈30** | Benzersiz açık iş-birimi (22 ledger-açık + İB-55..61 [7] + İB-63 bu koşum; İB-54 iki listede aynı) | üstteki üç satırın birleşimi |
| **13** | Loop-sınıfı birim (aşağıda §2) | `.claude/skills/` + `.claude/hooks/` + `tools/` listelemesi |
| **16** | katman-hatti temel hat adımı (+3 opsiyonel parquet) | `tools/katman-hatti.py:32-59` |
| **20** | `baglam.sqlite`'a dokunan script (okur+yazar karışık) | `grep -l "baglam.sqlite" tools/*.py` → 20 dosya |
| **0** | tools/ altında dosya-kilidi/lease mekanizması | `grep -rln "flock\|fcntl\|lockf\|\.lock" tools/*.py` → boş |

**Envanter çelişki notu (karar değil, tespit):** İB-47 ve İB-51 kapsülde havuz kalemi (`core/durum-kapsulu.md:23`) ama ledger'da `durum='kapandı'` (sqlite sorgusu). Karar 76 devir satırı "ledger jsonl satırları paralel oturumun ilk koşumunda senkronlanır" diyor (`kuyruk/senaryo-defteri.md:243`) — senkron henüz koşmamış. Sonuç: kapsülün önerdiği "koşum-önü ledger kontrolü" havuz İB'lerinin 7'si için **boş döner**, 2'si için **yanlış (kapandı) döner**.

DONDUR9 devri (`kuyruk/masa-gundemi-DONDUR9-2026-08-29.md:8` D5: 16 kalem) YENİ iş-birimi açmadı — tümü mevcut adreslere (K2-c · İB-08 · İB-04 · İB-60 · İB-61 · İB-12 · İB-09 · K-020 · BAKIM-KK · K-010) devredildi; ayak-izleri o adreslerin satırlarında sayılır.

## 1. PİPELİNE/İB ayak-izi envanteri

Sütunlar: OKUR · YAZAR · silver (`baglam.sqlite`) dokunuşu · commit atar mı · kanon-yüzeyi (core/, CLAUDE.md, tüzük) yazar mı. Kaynak = tanımın çıkarıldığı satır; script'i olan işlerde gerçek open/write çağrıları esas.

### 1a. Paralel havuz (kapsül satırı, 10 kalem)

| İB | İş | OKUR | YAZAR | silver | commit | kanon | Kaynak |
|---|---|---|---|---|---|---|---|
| İB-47 | Vektör ölçüm kolu | silver `v_guncel_kayit` sınıfı bloklar (`erisim-vektor.py:56,199`) · altın soru seti | `veri/erisim-vektor.sqlite` (CREATE/INSERT `:48-129`; gitignore-türev) · `veri/erisim-eval.jsonl` APPEND (`:230`) · `veri/gorunum/v_erisim_vektor*.csv` (`:253-257`) | **okur** (yazmaz) | rapor+eval commit'i muhtemel [?] | HAYIR | `kuyruk/senaryo-defteri.md:158,213` · `tools/erisim-vektor.py` |
| İB-51 adım 3 | Kural-kümeleme devamı | 49 taşıyıcı dosya (core/ kuyruk/ .claude/ KILAVUZ) — salt-okur | `veri/gorunum/v_kural_envanter*.csv` (üzerine yaz) · `veri/kural-envanter.jsonl` APPEND (`kural-envanter.py:101-107`) · `cc/rapor-*` | HAYIR | EVET (önceki adımlar attı: ab5f5b6) | HAYIR (okur ama yazmaz) | `tools/kural-envanter.py` · git log ab5f5b6 |
| İB-54 tavan paketi (adım 3) | Rejim-etiketi kural satırı m.46(d) | `raporlar/2026-08-29-ib54-delinme-kok-neden.md` · silver amb_olgu_kosum (eşik tabanı) | **`core/tuzuk-v0.md`** (m.46(d) satırı) · defter kaydı | okur | EVET | **EVET (tüzük — Salih imzalı)** | ledger İB-54 satırı (sqlite) · `.claude/hooks/pretool-ajan-fren.sh:9-10` |
| İB-55 | A3 araç-güvence yazımı | rafa kalkan gece-loop m.16 raporu (defter 08-27/29 blokları) · gnhf+A2 güvenceleri | güvence metni — hedef dosya kanon sınıfı [?] (`core/` ajan-metodolojisi ya da K-010 hattı) | HAYIR [?] | EVET | **muhtemel EVET [?]** | `kuyruk/senaryo-defteri.md:236` |
| İB-56 | Codex kullanım-alanı araştırması (Fable-dışı) | dış kaynak (web) — repo'dan yalnız bağlam | `cc/rapor-*` | HAYIR | EVET | HAYIR | `kuyruk/senaryo-defteri.md:242` |
| İB-57 | Headless iş-sınıfı→yüzey eşleme | silver `hareket` tablosu + `cc/pipeline-*.md` manifest verisi | taslak rapor (`cc/`) — masaya döner | **okur** | EVET | HAYIR | `kuyruk/senaryo-defteri.md:237` |
| İB-58 | axi-standardı, ilk aday katman-hatti | `tools/katman-hatti.py` + axi emsalleri | **`tools/katman-hatti.py`** (yeniden biçim) + muhtemelen alt-script arayüzleri [?] | dolaylı (hattı değiştirir) | EVET | HAYIR | `kuyruk/senaryo-defteri.md:233` |
| İB-59 | firstmate başarı-tespiti ölçümü | hareket kütüğü + koşum verileri (silver) | ölçüm raporu · muhtemelen `veri/bronz/kosum-sonuc.jsonl` [?] | okur | EVET | HAYIR | `kuyruk/senaryo-defteri.md:234` |
| İB-60 | Kural-tabanlı loop-dedektörü (LLM'siz) | silver `hareket` dizileri | yeni `tools/*.py` + çıktı kütüğü [?] · çıktısı k_W görev-sayacını besler | **okur** | EVET | HAYIR | `kuyruk/senaryo-defteri.md:253` |
| İB-61 | Absorbe-teyit turu (~4 kalem, İB-14 deseni) | silver `v_guncel_kayit` tema-taraması + tüzük/kanon hedefli okuma | kanıt-pointer'lı tablo (`cc/rapor-*`) — hüküm Salih'e | **okur** | EVET | HAYIR (okur, yazmaz) | `kuyruk/senaryo-defteri.md:257` · DONDUR9:12 (İB-14 usulü) |

### 1b. Ledger-açık kalanlar (17 İB + 5 KB — sıkıştırılmış; ayak-izi sınıfıyla)

| Birim | Ayak-izi sınıfı | YAZAR (belirleyici) | kanon | Kaynak |
|---|---|---|---|---|
| İB-01 | Salih el işi (bulut skill kopyaları) — repo-DIŞI | — | HAYIR | sqlite ledger satırı |
| İB-03 | md.49 yazım turu | **`core/tuzuk-v0.md` + `core/pano.md`** | **EVET** | ledger |
| İB-04 | wiki kuyruğu (~12 sayfa) | `wiki/*.md` + `wiki/README.md` | HAYIR | ledger |
| İB-05 | erteleme kapsamı (karma paket: find-skills · lease · SKILL.md şerhleri + DONDUR9 D7 3 kalem) | `.claude/skills/` + kuyruk [?] | KISMEN [?] | ledger · DONDUR9:10 |
| İB-06 | kalibrasyon borçları (koşum-sayısı eşikli) | rapor + defter; skill parametre dosyaları [?] | HAYIR [?] | ledger |
| İB-07 | description-eval (20×3×14) | rapor + `veri/` eval kütüğü [?]; OKUR `.claude/skills/*` | HAYIR | ledger |
| İB-08 | usage-otomasyon yol seçimi (+R9-K5 dedup devri) | yeni `tools/` betiği + `kosum-maliyeti.py` | HAYIR | ledger · DONDUR9:38 |
| İB-09 | Yol-C V26-yakalama ölçümü (+R20-K1-m) | rapor | HAYIR | ledger · DONDUR9:138 |
| İB-11 | dosya düzeltme borçları (md.43 5 madde + 2 mini test) | dağınık — birden çok kanon-komşu dosya [?] | KISMEN [?] | ledger |
| İB-12 | B2/B7/B9 ölçümleri (+KL18-2, R20-K1-i devri) | rapor + ölçüm kütüğü | HAYIR | ledger · DONDUR9:7,137 |
| İB-13 | P6 betiği Mac uyarlaması | `tools/` (staj kesişimi) | HAYIR | ledger |
| İB-30 | katman-hatti `--parquet` varsayılanı | **`tools/katman-hatti.py`** | HAYIR | ledger |
| İB-36 | sqlite3_stmt_status sayaçları (opsiyonel) | `tools/tarama-plan.py` [?] | HAYIR | ledger |
| İB-39 | idempotens entegrasyonu araştırması | rapor | HAYIR | ledger |
| İB-42 | silver-sağlık paketi kalanı | `tools/silver-saglik.py` + silver türetilmiş kolonlar | HAYIR | ledger |
| İB-53 | görüntüleme katmanı (kalan aday Foam; Salih tetiği) | araç-konfig [?] | HAYIR | ledger · kapsül:12 |
| KB-17/26/27/31/34 | karar-masası kalemleri (koşum değil) | `kuyruk/senaryo-defteri.md` + hükümle tüzük/kanon | hüküm halinde EVET | ledger |

## 2. LOOP-sınıfı işler ayak-izi envanteri (13 birim)

Kaynak: script'lerin gerçek open/write çağrıları (grep + okundu). "Tetik" = ne zaman koşar.

| # | Loop | Tetik | OKUR | YAZAR | silver | commit | kanon | Kaynak |
|---|---|---|---|---|---|---|---|---|
| L1 | seans-acilis ritüeli | "seans başı" + HER RESUME | CLAUDE.md · kapsül · pano · `raporlar/usage/senkron-log.jsonl` · son teslim raporu · git log | — (yalnız BAYAT'ta L3'ü tetikler) | okur (ro) | HAYIR | HAYIR | `.claude/skills/seans-acilis/SKILL.md:21-29` |
| L2 | seans-kapanis ritüeli | "seans bitimi" | tüm sıcak dosyalar | `raporlar/seans-teslim-*.md` · **`core/durum-kapsulu.md`** · `kuyruk/senaryo-defteri.md` · `fikir-kutusu.md` · `kuyruk/build-tartisma-notlari.md` · `kuyruk/SINIFLANDIRILAMADI.md` · `wiki/README.md` kuyruğu · `veri/bronz/kosum-sonuc.jsonl` · `cc/workflow/` kopyası | yazar (L3-L7 aracılığıyla) | **EVET (karar başına) + push** | **EVET (kapsül=core/)** | `.claude/skills/seans-kapanis/SKILL.md:18-54` |
| L3 | katman-hatti (16 adım) | kapanış §6f sonrası · BAYAT tespiti · pipeline sonu | `~/.claude/projects/<proje>/*.jsonl` (repo-dışı transkript) · bronz jsonl'ler · kuyruk | **`veri/baglam.sqlite` SIFIRDAN (tmp→os.replace, `baglam-tablo.py:922-998`)** · bronz APPEND (prompt/kosum/hareket/baglam-olay) · `veri/gorunum/*.csv` · `graf/*` türevleri · `veri/{katman-olcum,tarama-plan,silver-saglik,silver-kuyruk,erisim-eval}.jsonl` | **TEK-YAZAR VARSAYIMLI YAZAR** | HAYIR (commit ritüelde) | HAYIR | `tools/katman-hatti.py:32-59` |
| L4 | hareket-tablo (hat adımı + §6b tekil) | kapanış · hat | transkript (repo-dışı) · bronz | `veri/bronz/hareket-olay.jsonl` APPEND (`:156`) · silver `hareket` (`:184`) · gold CSV (`:226`) · `raporlar/hareket-gunlugu-*.md` (`:249`) | **yazar** | HAYIR | HAYIR | `tools/hareket-tablo.py` |
| L5 | baglam-seyir (hat adımı `seyir`) | kapanış · hat | transkript usage | `veri/bronz/baglam-olay.jsonl` APPEND (`:80`) · silver `baglam_olay` (`:100`) · gold CSV (`:137`) | **yazar** | HAYIR | HAYIR | `tools/baglam-seyir.py` |
| L6 | silver-saglik (hat adımı + `--kapi` kapanışta) | kapanış §6d · hat | sqlite + kuyruk dosyaları | silver türetilmiş kolonlar (additive) · `veri/silver-saglik.jsonl` APPEND · `veri/silver-kuyruk.jsonl` olay-kaynaklı | **yazar** | HAYIR | HAYIR | `tools/silver-saglik.py:7-30,418` |
| L7 | bayat-cekim (§6f) | kapanış; **hat'tan ÖNCE koşmalı** | silver `v_bayat_aday` · `veri/anakronizm-denetim.jsonl` (`:45`) | `veri/bronz/cekim-olay.jsonl` APPEND (`:106-108`) · `veri/katman-olcum.jsonl` APPEND (`:134`) | okur | HAYIR | HAYIR | `tools/bayat-cekim.py` · seans-kapanis SKILL:51 ("Hat bu adımdan SONRA koşar") |
| L8 | skill-esik (§6c) | kapanış | silver `v_skill_kosum` — **salt-okur** (61 satır, write çağrısı yok) | — (SAPMA satırı teslim raporuna elle) | okur | HAYIR | HAYIR | `tools/skill-esik.py:26-35` |
| L9 | kural-sayaci (§6e) | kapanış | CLAUDE.md + çağrılan SKILL.md'ler + hook stdout (`:61`) | `veri/kural-sayim.jsonl` APPEND yalnız `--kutuk` ile (`:79`) | HAYIR | HAYIR | HAYIR | `tools/kural-sayaci.py` |
| L10 | gece-senkron.ps1 | schtasks DAILY 06:00 (Windows `C:\JARVIS` sabit) | git origin | **working tree (git pull --ff-only)** · `raporlar/usage/senkron-log.jsonl` · FAIL'de `SENKRON-UYARI.md`; ff-fail'de "HİÇBİR ŞEYE DOKUNMAZ" | HAYIR | pull = commit-index'e dokunur | HAYIR | `tools/gece-senkron.ps1:1-24`. Son log satırı **2026-08-04 FAIL-ff** (`raporlar/usage/senkron-log.jsonl` tail) — Mac-primary rejimde fiilen uykuda [?] |
| L11 | SessionStart hook | her oturum açılışı | git · sqlite **ro** (`mode=ro`, `:29`) · kapsül · `veri/model-kesim.jsonl` | — (yalnız stdout ≤2 KB) | okur (ro) | HAYIR | HAYIR | `.claude/hooks/session-start.sh` |
| L12 | pretool-core-tel hook | her Bash çağrısı | komut metni | — (yalnız exit 2) | HAYIR | HAYIR | HAYIR (koruyucu) | `.claude/hooks/pretool-core-tel.sh` |
| L13 | pretool-ajan-fren hook | **her Agent çağrısı (tüm oturumlarda)** | sayaç state | `veri/bronz/fren-olay.jsonl` APPEND (`:40-42`) · `.claude/hooks/state/ajan-fren-<sid>.json` (gitignore) | HAYIR | HAYIR | HAYIR | `.claude/hooks/pretool-ajan-fren.sh` |

**Loop'a özgü not (emirdeki ① tekrarlılık boyutu):** L3-L7'nin yazar-kümesi her iterasyonda AYNI paylaşılan dosyalara döner (baglam.sqlite + 8 append-jsonl); L13 ise oturum boyunca sürekli yazar. Çakışma tek-seferlik değil süreklidir — Karar 77'nin vaka sınıfı (paylaşılan türev-jsonl merge tuzağı, `seans-kapanis SKILL.md:61`) tam bu yüzden loop-kaynaklı.

## 3. Mevcut fren envanteri — neyi engelliyor / neyi ENGELLEMİYOR

| Fren | Mekanizma türü | ENGELLER | ENGELLEMEZ | Kaynak |
|---|---|---|---|---|
| **H4 yol-bazlı git add** | metinsel kural (koşum-anı denetimi yok) | canlı paralelde `git add -A` ile diğer oturumun yarım işinin YAYIMLANMASINI (commit anında, uyulursa) | iki işin aynı dosyaya YAZMASINI; yazım zaten olmuşsa dosya-içi karışmayı; unutulursa hiçbir şeyi (vaka-4 emsali: delinmiş) | `wiki/paralel-oturum-protokolu.md:10` · seans-kapanis SKILL:54 |
| **PreToolUse core-teli** | koşum-katmanı hook, matcher **yalnız Bash** | Bash yönlendirme/mv/cp/rm/sed-i/git-checkout ile `core/`·`CLAUDE.md`·`.claude/` yazımını (exit 2) | **Edit/Write araçlarıyla aynı yolların yazımını** — hook yorumu (satır 3-4) "settings-deny Edit/Write tutar" der, ama bugünkü `.claude/settings.json` `"deny": []` (BOŞ); kaçan Bash desenleri de olabilir ("tökezleme-teli, sınır değil") | `.claude/hooks/pretool-core-tel.sh:3-5,14-19` · `.claude/settings.json` |
| **Paralel-oturum protokolü (4 kural)** | metinsel usul + açılış/resume yoklaması | mükerrer koşumu (kural 2 uyulursa) · commit karışmasını (kural 4=H4) · kaynak/daemon çakışmasını (kural 3) | dosya-düzeyi yazar∩yazar tespitini (hiçbir kural dosya kümesi karşılaştırmaz); commit >15 dk önceyse canlı-oturum kapısı KÖR; manifest-grep varyant ıskalar (08-21 `ATLAS[- ]?V59` vakası) | `wiki/paralel-oturum-protokolu.md:5-14` |
| **İB-54 ajan fan-out sayaç-hook'u** | koşum-katmanı hook (Agent matcher), oturum-başına sayaç warn 36 / stop 72 | tek oturumda aşırı-uç Agent fan-out'unu (taahhüt anında, exit 2) | oturumlar-ARASI toplamı (sayaç session_id-bazlı) · Workflow ajanlarını (ayrı şablon `cc/workflow/fren-sablonu.js`, kopyalanırsa çalışır) · ajanların HANGİ DOSYALARA yazacağını (sayı sayar, ayak-izi bilmez) | `.claude/hooks/pretool-ajan-fren.sh:5-11,24-27` |
| **Koşum-önü manifest kapısı** | metinsel: `cc/pipeline-*.md` + `git log -15` okuması | manifesti YAZILMIŞ pipeline'ın ikinci koşumunu (vaka-3 518k sınıfı) | manifesti OLMAYAN işleri (havuz İB'lerinin çoğunun `cc/pipeline-*.md`'si yok — 16 manifest listelendi, havuz İB'leriyle eşleşen yok) · loop koşumlarını (katman-hatti'nin manifesti yok) · eşzamanlı BAŞLAYAN iki koşumu (okuma anında iz yoksa ikisi de "temiz" görür) | seans-acilis SKILL:19 · `ls cc/pipeline-*.md` |
| **Silver tazelik kapısı (KB-54)** | tespit-only (SessionStart BAYAT satırı + açılış §3b) | bayat silver'dan adresli okuma hatasını (koşum tarifiyle) | eşzamanlı çift hat koşumunu · okuma-sırasında-replace yarışını (yalnız "bayat" der, kilitlemez) | seans-acilis SKILL:25 · session-start.sh:32 |
| **Paylaşılan-jsonl merge SOP'u (Karar 77)** | metinsel kapanış usulü (post-hoc) | çakışmış türev-jsonl'de yanlış elle-merge'i ("üreticiyi yeniden koş") | çakışmanın OLUŞMASINI (teşhis+onarım usulü, önleme değil) | seans-kapanis SKILL:61 |
| **push-onay + verify-push** | harness `ask` kuralı + deterministik doğrulayıcı | Salih beyansız push'u (`"Bash(git push:*)"` ask) · yarım push'un "sayıldı" beyanını | push ÖNCESİ her şeyi (yazım+commit serbest) | `.claude/settings.json` ask listesi · `tools/verify-push.py` |
| **SQLite hijyen/tek-yazar düzeni** | yalnız SIRA disipliniyle (hat içi ardışık adımlar) | hat İÇİNDE çift yazımı (adımlar seri) | hat DIŞINDA hiçbir şeyi: **kilit/lease mekanizması YOK** (grep flock/fcntl/lockf → 0 dosya); iki oturum aynı anda hat koşarsa tmp→replace "son yazan kazanır" | `tools/katman-hatti.py` · grep sonucu §0 |

**Ortak boşluk (tüm frenlerin kesişimi):** Hiçbir mevcut fren, iki işin YAZAR-kümelerinin kesişimini koşum ÖNCESİ hesaplamaz — ayak-izi hiçbir yerde makine-okur biçimde beyan edilmiyor; tespit ancak commit anında (`git status`) ya da arıza sonrasında (vaka-1..5 serisi) oluyor.

## 4. Çakışma-matrisi taslağı (4 düzlem — en riskli 3'er somut çift)

Tür kısaltmaları: **Y∩Y** yazar∩yazar · **Y∩O** yazar∩okur · **SLV** silver tek-yazar ihlali · **CIX** commit-index yarışı.

### 4a. pipeline × pipeline

| # | Çift | Çakışan varlık | Tür | Bugün nasıl önleniyor |
|---|---|---|---|---|
| 1 | **İB-58 (axi-standardı) × İB-30 (--parquet varsayılanı)** | `tools/katman-hatti.py` — ikisi de AYNI dosyayı değiştirir | Y∩Y | **AÇIK.** İkisinin de manifesti yok; tek fren commit anında H4. (Kaynak: defter:233 · ledger İB-30) |
| 2 | **İB-47 (vektör kolu) × hat-dokunan herhangi bir İB (İB-58/İB-42)** | `veri/erisim-eval.jsonl` (İB-47 append, hat `erisim` adımı da append — `erisim-fts.py` hat:43) + `baglam.sqlite` (İB-47 okur, hat sıfırdan yazar) | Y∩Y + SLV(okuma yarışı) | **AÇIK** (yalnız Karar 77 post-hoc SOP'u). |
| 3 | **İB-54 adım 3 × İB-55 × İB-03** | kanon-yüzeyi: `core/tuzuk-v0.md` (m.46(d) · md.49 turu) + core/ güvence metni | Y∩Y (kanon) | **KISMEN:** Katman-1 "yalnız Salih imzasıyla" metinsel kapısı sıralamayı fiilen dayatır; makine freni ise yalnız Bash-teli — **Edit/Write için deny boş** (§3 satır 2). |

### 4b. loop × loop

| # | Çift | Çakışan varlık | Tür | Bugün nasıl önleniyor |
|---|---|---|---|---|
| 1 | **İki oturumun eşzamanlı katman-hatti koşumu** (ikisi de kapanışta ya da biri BAYAT tespitinde) | `veri/baglam.sqlite` — baglam-tablo tmp→os.replace SIFIRDAN yazım (`baglam-tablo.py:922-998`); kilit yok | **SLV (çekirdek vaka)** — son yazan kazanır, diğerinin gold/uretim sha'sı anında bayatlar | **AÇIK.** Tek emsal el kararı: 08-29 paralel oturuma "hat koşumu onlara bırakıldı" (defter:243) — kural değil, o güne özgü tercih. |
| 2 | **bayat-cekim ↔ katman-hatti sıra bağımlılığı iki oturumda ters düşerse** | `veri/bronz/cekim-olay.jsonl` → silver `kayit.cekim_tarihi` tazeliği (§6f: "Hat bu adımdan SONRA koşar") | Y∩O + sıra-kısıtı | **KISMEN:** sıra kuralı SKILL metninde (seans-kapanis:51); makine denetimi yok — oturum-A cekim yazarken oturum-B hat koşarsa damga bayat kalır. |
| 3 | **L13 ajan-fren (her Agent'ta `fren-olay.jsonl` append, TÜM oturumlar) × L2 kapanış commit süpürmesi** | `veri/bronz/fren-olay.jsonl` — repo-içi bronz, iki oturum eşzamanlı append + biri commit'ler | Y∩Y + CIX (Karar 77 sınıfı: `tarama-plan.jsonl` vakası b2b05897/aa05a9d1) | **KISMEN:** H4 + Karar 77 SOP'u (post-hoc); append'in kendisi engellenmiyor. |

Ek satır (uykuda ama kayıtlı): **L10 gece-senkron pull × canlı oturum kapanış commit'i** — CIX; ff-only fail-safe DOKUNMAZ (script satır 2 + son log 2026-08-04 FAIL-ff dirty_files:8) → fren VAR ama iş de yapmıyor; Mac karşılığı repo'da yok.

### 4c. loop × pipeline

| # | Çift | Çakışan varlık | Tür | Bugün nasıl önleniyor |
|---|---|---|---|---|
| 1 | **katman-hatti koşumu × silver-OKUYAN İB koşumu (İB-57/İB-60/İB-61/İB-47)** | `baglam.sqlite` — İB uzun sorgu/tarama ortasındayken hat os.replace ile dosyayı değiştirir | Y∩O (SLV okur tarafı) | **AÇIK.** Tazelik kapısı yalnız açılışta "BAYAT" der; koşum-ortası değişimi kimse tespit etmez, kilit yok. |
| 2 | **L2 seans-kapanis (kapsül+defter+pano yazımı, commit) × paralel İB oturumunun ledger/rapor yazımı** | `core/durum-kapsulu.md` satırları · `kuyruk/senaryo-defteri.md` · `veri/karar-borcu.jsonl` | Y∩Y + CIX | **KISMEN:** "yalnız kendi şeridinin satırları" (seans-kapanis:33) + H4 — metinsel; vaka-4 (karar-numarası çift kullanımı + 14 kırık pointer, wiki:7) bu frenin delinebildiğinin kayıtlı kanıtı. |
| 3 | **İB-58'in `tools/katman-hatti.py` yeniden-yazımı × hattın herhangi bir loop koşumu** (kapanış ya da BAYAT tetiği aynı anda) | çalışan script'in kaynak dosyası | Y∩O (yürütülebilir üstüne yazım) | **AÇIK.** Hiçbir fren "bu script şu an başka oturumca koşuyor" bilgisine sahip değil. |

### 4d. loop × ana-oturum

| # | Çift | Çakışan varlık | Tür | Bugün nasıl önleniyor |
|---|---|---|---|---|
| 1 | **Ana-oturumun Edit/Write ile core/ yazımı × kanon bütünlüğü** | `core/` · `CLAUDE.md` · `.claude/` | tek-taraflı yazım (koruma boşluğu) | **AÇIK (makine düzeyinde):** core-tel yalnız Bash matcher'lı; `.claude/settings.json` `"deny": []` → Edit/Write serbest. Koruma tamamen metinsel Katman-1 kuralı. |
| 2 | **L4/L5 transkript okuması × canlı ana-oturumun aynı transkripte yazması** | `~/.claude/projects/<proje>/*.jsonl` (repo-dışı) | Y∩O (canlı dosya okuma) | **KISMEN (yapısal):** JSONL append-only + `errors="replace"` + tekil `hareket_id` idempotens (`hareket-tablo.py:161-168`) → yarım satır düşer, sonraki koşum tamamlar; veri kaybı değil ama o koşumun bronz'u eksik olabilir [?]. |
| 3 | **L13 sayaç-state oturum-başına × uzun-yaşayan ana-oturum + alt-ajan zinciri** | `.claude/hooks/state/ajan-fren-<sid>.json` — sayaç session_id'ye bağlı; alt-ajanların kendi oturumları sayaca girer mi belirsiz **[?]** | fren-kapsamı belirsizliği (dosya çakışması değil) | **KISMEN:** `JARVIS_FREN_KAPALI=1` Salih-beyan kaçış yolu var (hook:10); kapsam sorusu ölçülmemiş. |

## 5. İDDİALAR (iç-analiz; hepsi pointer'lı — karar değil)

1. **Ayak-izi beyanı hiçbir yerde makine-okur değil.** 30 açık iş-biriminin ve 13 loop'un OKUR/YAZAR kümeleri yalnız bu rapor sınıfı elle-çıkarımla görülebiliyor; `cc/pipeline-*.md` manifestleri (16 adet) koşum-TARİHÇESİ tutuyor, yazar-kümesi alanı içermiyor. Sonuç: "yazar∩yazar=∅?" sorusu bugün hiçbir mekanizma tarafından sorulmuyor. (Kaynak: §1-§2 tabloları · `ls cc/pipeline-*.md`)
2. **Kanon-yüzeyi Edit/Write için makine-korumasız.** `pretool-core-tel.sh:3-5` "settings-deny yalnız Edit/Write tutar" varsayımıyla yazılmış; bugünkü `.claude/settings.json`'da `"deny": []`. Tel yalnız Bash'i tutuyor → core/ yazımının fiilî tek koruması metinsel Katman-1 kuralı. (Doğrulama: iki dosyanın birlikte okunması)
3. **`baglam.sqlite` "tek-yazar" varsayımı ancak hat-İÇİ sırayla ayakta.** 20 script dosyaya dokunuyor (`grep -l`); en az 6'sı yazar (baglam-tablo sıfırdan-replace, hareket-tablo, baglam-seyir, silver-saglik, bag-tablo, erisim-fts). Kilit/lease yok (flock grep = 0). Hat dışında tekil koşum + paralel oturum = son-yazan-kazanır yarışı; 08-29'da çakışma yalnız el kararıyla ("hat onlara bırakıldı", defter:243) önlendi.
4. **Ledger-senkron açığı koşum-önü kontrolü kör bırakıyor.** Kapsül havuzundaki 10 İB'den 7'sinin (İB-55..61) `karar_borcu`'nda satırı yok (`veri/karar-borcu.jsonl` son kayıt İB-54); İB-47/İB-51 ise ledger'da 'kapandı'. Kapsülün önerdiği "koşum-önü manifest/ledger kontrolü" (kapsül:23) bu kalemler için ya boş ya yanlış cevap veriyor. (Senkron borcu Karar 76'da kayıtlı: defter:243)
5. **Manifest kapısı loop'ları hiç kapsamıyor.** Kapı tanımı "Workflow/atlas/pipeline açmadan önce" (seans-acilis:19); katman-hatti/bayat-cekim/hareket-tablo koşumlarının manifesti yok, kapıdan geçmiyor — oysa en tekrarlı yazar bunlar (§2).
6. **Loop çakışması SÜREKLİ-risk sınıfı ve kayıtlı emsali var.** Paylaşılan append-jsonl'lerde (tarama-plan.jsonl vakası: 2 başarısız oturum, 3-4'er merge denemesi — seans-kapanis:61, Karar 77) çakışma yaşandı; SOP post-hoc teşhis usulü, önleyici değil. L13 (ajan-fren) her Agent çağrısında repo-içi bronz'a yazarak bu sınıfı her paralel oturumda yeniden üretiyor (`pretool-ajan-fren.sh:40-42`).
7. **Zamanlı tek loop (gece-senkron) Mac rejimiyle uyumsuz ve 25 gündür FAIL'de.** Script `C:\JARVIS` sabit yollu (gece-senkron.ps1:6), son log satırı 2026-08-04 FAIL-ff dirty_files:8 (`raporlar/usage/senkron-log.jsonl`); seans-acilis §2.4 hâlâ bu logu açılış adımı sayıyor. Mac karşılığı repo'da yok [?].
8. **Sıra-kısıtlı loop çifti tek yerde metinle tutuluyor.** bayat-cekim→katman-hatti sırası yalnız SKILL cümlesi (seans-kapanis:51); İB-58 hat'ı yeniden biçimlendirirken bu görünmez kısıtın taşınması gerekecek — sıra kısıtları da ayak-izi gibi beyan-dışı.
9. **Fren delinme emsalleri metinsel frenlerin tek başına yetmediğini gösteriyor:** vaka-3 (518k mükerrer workflow, manifest-kapısı öncesi), vaka-4 (resume-körlüğü: karar-numarası çakışması + 14 kırık pointer, H4 varken), manifest-grep varyant ıskalaması (08-21). Kaynak: `wiki/paralel-oturum-protokolu.md:3,7,14`.

*Rapor sonu. Tüm hücrelerdeki [?] işaretleri: script/tanım metninden kesin çıkarılamayan, tahmine düşmemek için boş bırakılan alanlar.*
