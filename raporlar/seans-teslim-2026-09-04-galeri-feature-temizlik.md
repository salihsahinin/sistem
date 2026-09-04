# Seans Teslim Raporu — 2026-09-04 (2. seans) · GALERİ ŞERİDİ: feature temizliği + ETL şema senkronu

*Yüzey: Claude Code masaüstü, Mac `~/jarvis` (ana-sıra; model seans içinde Sonnet 5 ↔ Fable 5.1 arası değişti — kanon kararı yok, tümü Salih hükmü). Hat: galeri şeridi, jarvis-DIŞI repo `~/Desktop/repo/data-company-vehicle-scoring` (m.15/md.49 — o repo'nun dosyaları jarvis'e commit'lenmez; burada yalnız pointer + hasat). Deneysel damgalı (m.29). Damga: beyansız (m.33).*

## 1. Bugün gerçekten ne değişti
**Jarvis-dışı repo (`data-company-vehicle-scoring`):**
- `src/agac_html.py` + `agac_html_sablon.html`: yeni **SHAP hiyerarşisi** sekmesi (korele kolon kümeleri; `shap_hierarchy.correlation_linkage` yeniden kullanıldı, matplotlib yerine JSON) · "Bugünkü ihale" gerçek-senaryo tablosuna distinct galeri listesi.
- `src/train.py`: `--exclude-features`, `--early-stopping-rounds`; `--feature-weights`'in budanan kolonlara göre otomatik filtresi (**gerçek hata:** CatBoost bilinmeyen kolon adında eğitimi durduruyordu, test edildi) · `load_data()`'da SQL↔Python **parity kapısı**.
- `src/features.py`: data-etl `6b3155e` senkronu — `CAT_FEATURES`'tan `city`/`body_config_name` çıktı; `REDUNDANT_FEATURES` (+`budget_covers_one_car`) → `DROP_COLS`; `engineer_features()` SQL'deki 22 türevi birebir üretiyor (`pct_rank_in_trim()` = pandas average-rank / NULL-olmayan sayı, SQL'in RANK()+(tie−1)/2 formülüyle eşit; girdisi çıktıda olmayan türev SQL değerini ezmez) · deneysel 15 `*_decay_*` kolonu kaldırıldı · `MARKET_RAW_COLS_REMOVED_IN_ETL` belgesi · "Coğrafi Eşleşme" grubu.
- `src/sozluk_kolon.py`: 30 yeni tanım. Yeni kalıcı script'ler: `feature_analiz.py` (seyreklik + kümeleme-sıralı korelasyon ısı haritası) · `feature_cift_siniflama.py` (dolu-satır kalıcılık testi) · `feature_liste_excel.py` (xlsx + HTML ikizi) · `overfit_kontrol.py`.
- Modeller (ayrı klasörler, üretim `models/YetiRank` DOKUNULMADI): `YetiRank_tuned` (depth 8+LR/2+rsm .5+budama → çöktü) · `tuned2` (yalnız budama 91 kolon) · `tuned3` (recency-decay, 3000 tavanla adil) · `temiz_a` (161 kolon + baskınlık kırpma; 176-kolonlu sızıntılı ilk koşum `…_176kolon_sizinti` olarak kenarda). `agac-semasi.html` 9 modelle yeniden üretildi (19,5 MB). Çıktılar `analiz/`.
- Testler: sentetik yeni-şema çerçevesinde 22 formül SQL'e eşit (max fark ≤ 4e-16) · eski `data.csv` (199 kolon) üzerinde hatasız · parity kapısı kasıtlı bozuk kolonu yakaladı. **Bu üç dosya COMMIT EDİLMEDİ — Salih onayı.**

**Jarvis:** kapsül · fikir-kutusu V92/V93 · build-tartışma 09-04 bloğu · wiki kuyruğu `korelasyon-kaliciligi` · hareket günlüğü 09-04 · bronz/silver/gold/ölçüm türevleri.

**"İlk plan = bitti değil" yoklaması:** açılışta plan yoktu — Salih'in ardışık soruları güdümledi (importance neden çarpık → düzeltmek için ne yapmalı → HTML sekme → retrain'ler → seyreklik/korelasyon → dolu-satır testi → Excel → ETL senkronu). Kapsüldeki 0a yarım birim (`16/17_yeni_trim`) bu seansta ELE ALINMADI (sapma, kayda geçti). Ayrı görsel: recency-decay SVG (`mcp__visualize`, dosya yok).

## 2. Hangi karar verildi (kaynak + gerekçe + geri-açma)
Hepsi Salih'in jarvis-dışı operasyonel kararları; jarvis kanon kararı YOK (senaryo-defteri girişi yok):
- **Retrain tabanı = `models/YetiRank` (477 ağaç)**, v1 (597) değil — Salih kuralı "yakınsa v1, 477 iyiyse o": GroupAUC 0.709 vs 0.646, yakın değil. Geri-açma: v1'in feature setiyle (dealer_genel_* olmadan) ayrı deneme.
- **Kombine ayar tek koşumda** (Salih) → çöktü (PFound 0.91→0.68, 136 ağaç); ardından **izole denemeler** (Salih onayı): tuned2 ≈ üretim, tuned3 < tuned2 (half-life=7 doğrulanmamış), temiz_a GroupAUC −0.026 / SHAP dağılımı hedefine ulaştı.
- **Hedef değişimi (Salih):** seyreklik çıkarma sebebi değil; **kalıcı** korelasyon tekilleştirilir, yapay olan tutulur; baskın feature'lar kırpılır. Uygulama: dolu-satır+erken/geç testi → KALICI 45 / SEMANTİK 56 / YAPAY 34 / BELİRSİZ 3.
- **4 semantik çift (Carvis kararı, Salih "öner ve uygula"):** `market_trim_sold_car_cnt` AT (sell_through_rate taşıyor) · `bought_price_avg_trim` AT (serie ⊇ trim) · `trim_price_p10/p90` AT (band türevleri + p50 yeter). Geri-açma: yeni extract'ta üçü zaten yok (ETL kaldırdı) — karar fiilen ETL'yle örtüştü.
- **(1) adımı atlandı, doğrudan (2)** (Salih "vakit kaybetmeyelim"): 161-kolon kırpmasız taban ölçülmedi → temiz_a'daki −0.026'nın temizlik/kırpma payı ayrışmadı.
- **Senkron yönü SQL→Python (Carvis):** SQL'in referans verdiği Python sürümü yok; `api.py` yalnız Python'a sahip. Geri-açma: ETL yazarının `features.py`'si bulunursa diff.

## 3. Hangi fikir ADAY kaldı (karar değil)
- V92 dolu-satır korelasyon testi · V93 türev-formül parity kapısı (fikir-kutusu).
- build-tartışma 09-04: group_id↔ETL çelişkisi · pct-rank dağılım sızıntısı · kanonik features.py kayıp · PairLogit>YetiRank · `trim_price_p50` gösterim kırığı.
- Half-life taraması (3/14 gün) · 161-kolon kırpmasız koşum · rsm/feature_weights ayrı ayrı izole.

## 4. Sonraki ilk iş
Kapsül 0a: (1) üç dosyanın commit'i (Salih onayı) · (2) group_id çelişkisi hükmü · (3) yeni extract gelince parity + gösterim kırığı + pct-rank test-içi hesap · (4) PairLogit denemesi. Jarvis tarafı 0: 9 masa kalemi değişmedi.

## 5. Yeniden açma koşulu
- Yeni `galeri_scoring_training_data` extract'i (eski `data.csv`: 199 kolon, yeni şema eğitilemez).
- Salih'in group_id hükmü (a/b) ya da ETL'den market kolonlarının dönüşü.
- View verisi birikince (bugün 494/687k satır) BELİRSİZ pencere çiftleri yeniden sınıflanır.

## 6. Hasat (`core/sablonlar/hasat.md`)
1. **Özütler:** (a) yüksek korelasyon tek başına "kopya" kanıtı değil — dolu-satır testinde 34/138 çift yapay çıktı, bir "birini at" önerim geri çekildi · (b) 657 pozitifle kombine regularizasyon early-stop'u 136 ağaçta kesiyor; değişkenler izole denenmeli · (c) `feature_weights` "cannot be parsed" uyarısı yalnız yeniden-yüklemede (kozmetik) — ilk teşhisim yanlıştı, düzelttim · (d) baskınlık kırpma amaca ulaştı (ilk-10 %65→%62, `dealer_genel_*` ilk-8'den çıktı) ama GroupAUC bedeli var; run-to-run oynama ~0.01 → 0.01'lik farklar gürültü · (e) ETL'nin "grup içinde sabit" gerekçesi bizim `group_id=trim_id`'ye uymuyor — iki repo aynı doküman farklı gruplama.
2. **Wiki-delta:** `korelasyon-kaliciligi` kuyruğa yazıldı; `stokastik-dusunce`/`silver-saglik` Gotchas'a tuzak yok.
3. **Verilebilir miydi (V20):** analiz script'leri + HTML ikizleri Sonnet işçiye verilebilirdi (deterministik, spec net); verilmedi — Salih'in her adımda soru-yönlendirmesi vardı, devir maliyeti kazancı aşardı. Retrain'ler ajan işi değil (süre-bağımlı, karar-bağımlı). ETL senkronu Fable planlayıcı işi olarak kaldı (formül eşitliği yargı gerektirdi).
4. **Token×zaman:** çok×uzun (tek oturum 2 gün, `v_baglam_seyri`: tur 199 · ilk 381k · max 581k · 128k üstü 199 tur · çıktı 294k). Beklenti: kısmen — retrain bekleme süreleri (4×~55 dk + 2×~40 dk) oturumu uzattı.

## 7. Kapılar ve sayaçlar
- hareket-tablo: 7088 çağrı (36 yeni) · silver 6209 · `raporlar/hareket-gunlugu-2026-09-04.md` · 3 test PASS.
- silver-sağlık `--kapi`: **exit 0** · WARN 0 · aday: SÜPERSEDE 4 · YETİM 317/351 · KAPANDI 105 · T-A ön-eleme 7026 (500 yazıldı). Salih triyajı, karar değil.
- katman-hatti: PASS; WARN "ajan araç çağrısı > 54" ihlal 34 (bilgi).
- skill-eşik: 6 çift · yeni-pencere sapması 0 · bu seansta ajan koşumu yok (kosum-sonuc.jsonl'e satır düşmedi).
- kural-sayacı: 19/100 · boyut-tetiği: kapsül ölçümü §8 · bayat-çekim: kuyruk 0 · çekilen 0/3 · test-kapısı: 102 test · FAIL 0 · skip 7.
- uzun-koşum: max bağlam 581k (199 tur üstte). Araç-çıktısı aşımı: yok (SQL/features okumaları parçalı; 20 MB HTML hiç bağlama alınmadı).
- İngest sayaçları: giren 8 (2 fikir · 5 tartışma bulgusu · 1 wiki-delta) · ADD 8 · NOOP 0 · UPDATE 1 (kapsül galeri satırı) · geçersiz 0 · DLQ 0.

**Hasat kontrol listesi (KB-50/52):** (1) kalıcı kural/karar adayı ingest'e girdi mi → EVET (V92/V93, build-tartışma) · (2) açık pipeline/manifest T beyanı → jarvis pipeline'ı yok; galeri retrain'leri TAMAM, sonuçlar `analiz/` + config'lerde · (3) Workflow/ajan tahmin↔gerçek kaydı → koşum yok (n/a) · (4) paralel oturum → yok; devir gerekmedi.

## 8. Boyut-izleme
Kapsül: "Önceki" zinciri kısaltıldı; ölçüm 8011 → kısaltma sonrası ≤8.000 B / 25 satır (bütçe 8 KB/40). Pano 9,8/12 · **boyut-tetiği: `fikir-kutusu.md` 20,7/20 KB** (V92/V93 ile aştı — damıtma ilk boş seansta Salih-imzalı plan; aday: V86-V91 bloğunun arşive inmesi) · defter 45,9/48 · CLAUDE.md 6,98/7 (dokunulmadı) · KILAVUZ 13,8/16.
