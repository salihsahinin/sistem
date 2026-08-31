# İB-69 AİLE-2 (a) — Açık işlerin matris-koşuma uygunluk envanteri

**Künye:** rol tez-a (işçi, salt-okur) · AS-OF 2026-08-31 · model claude-sonnet-5 (effort orta, rejim maliyet-öncelikli) · HEAD `c1f5c05` (koşum anı, `git rev-parse --short HEAD`) · dizin `/Users/HasanSalihSahin/jarvis`.

**Okunan kaynaklar:**
- `raporlar/2026-08-31-ib69-matris-a1-formalizasyon.md` (MATRİS-KOŞUM ŞEMASI v0, tam metin — §1 EKSEN, §2 HÜCRE SÖZLEŞMESİ Ö1 tiplilik, §4 maliyet iki kapısı, §6 Ö-A/Ö-B/Ö-C)
- `veri/karar-borcu.jsonl` (python3 sorgusuyla 27 kalemin tamamı tek tek çekildi: KB-17/26/27/31/34, İB-01/03/04/06/07/09/11/13/36/39/53/56/58/59/64a/64b/64c/65/66/67/68/69)
- `raporlar/2026-08-30-ib07-description-eval.md`, `raporlar/2026-08-30-ib09-yolc-v26-etki.md` (tam metin)
- `tools/d2-eval.py`, `tools/denetci-kalibrasyon.py`, `tools/erisim-kalibrasyon.py`, `tools/silver-saglik-kalibrasyon.py` (argparse alanları + eksen/eşik satırları grep+read ile açıldı)
- `core/skill-uretim-semasi.md:90-115`, `core/halusinasyon-paketi.md:20-40`, `core/sema-sikistirma.md:30-45`, `core/baglam-anahtar-kaydi.md` (k1/k2 alanı arama — satır bulunamadı, `[?]`), `core/world-model-tasarimi.md:45-65` (İB-06'nın beş alt-borcu için)
- `grep -rn "model×effort|KB-02"` → KB-02 KAPANDI (icra borcu tamam, `core/ajan-metodolojisi.md:36-37`) + `kuyruk/utopik-havuz.md:34` (madde 17, "sınıf-başına optimize wiki" — açık borç havuzunda DEĞİL, BUILD YOK'a tabi parkedilmiş fikir)

---

## Tablo (27+4 satır; borç-havuzu kalemleri + tool-türetilmiş 4 ek aday)

| iş kimliği | pointer | UYGUN/UYGUN-DEĞİL | eksen-A (n) | eksen-B (n) | çıktı-tipi | hücre_tipi | N_hücre | gerekçe (§2 Ö1) |
|---|---|---|---|---|---|---|---|---|
| KB-17 | `veri/karar-borcu.jsonl` (borc_id KB-17) | UYGUN-DEĞİL (ii) KARAR-GEREKTİREN | — | — | — | — | — | kalem-kalem imza/red; Katman-1 hükmü (Salih), matris değil oylama |
| KB-26 | aynı, KB-26 | UYGUN-DEĞİL (ii) KARAR-GEREKTİREN | — | — | — | — | — | m.37 v2 fıkralarının yürürlüğü Salih hükmüne kalmış tek karar |
| KB-27 | aynı, KB-27 | UYGUN-DEĞİL (i) TEK-ATIŞ | — | — | serbest_metin | — | — | "2 delinme vakasının kök-neden analizi" — sabit 2 örnek, tekrarlanabilir eksen yok |
| KB-31 | aynı, KB-31 | UYGUN-DEĞİL (ii) KARAR-GEREKTİREN | — | — | — | — | — | BEKLET-tetikli Katman-1 kararı (aile-dışı denetçi seçimi); tetik gerçekleşmedi |
| KB-34 | aynı, KB-34 | UYGUN-DEĞİL (i) TEK-ATIŞ | — | — | etiket (PASS/FAIL) | tek_cagri | 1 | `tools/yuzey-parmak-izi.py` tek koşumluk yetki karşılaştırması, eksen yok |
| İB-01 | aynı, İB-01 | UYGUN-DEĞİL (iv) İNSAN-GİRİŞİ | — | — | — | — | — | Salih'in tarayıcı girişi gerektiren manuel işlem |
| İB-03 | aynı, İB-03 | UYGUN-DEĞİL (i) TEK-ATIŞ | — | — | serbest_metin | — | — | 3 ayrı yazım/denetim işi, ortak eksen yok, tekrarsız |
| İB-04 | aynı, İB-04 | UYGUN-DEĞİL (iii) SERBEST-METİN | wiki-aday (11) | — | serbest_metin | — | — | her wiki sayfası kompoze düzyazı; tempo kuralı zaten oturum-başı 1-2 (matris değil sıra) |
| İB-06a — skill-kapısı τ/W/β/n_val | `core/skill-uretim-semasi.md:103` | UYGUN — eksen tanımı eksik/veri bekliyor | τ-grid (n≥3) | W-grid gün (n≥3) | sayi (precision/recall) | tek_cagri (LLM'siz) | ~9-16 | Ö1 sağlanır (etiket/sayı, bağımsız hücre, karar gerektirmez) AMA `erisim-kalibrasyon.py --grid` desenini tekrarlamak için ≥10 gerçek skill-kapısı koşum kaydı (şu an 2/10) gerekiyor — veri eşiği geçmeden grid koşulamaz |
| İB-06b — H formülü ağırlıkları | `core/halusinasyon-paketi.md:31` | UYGUN — eksen tanımı eksik/veri bekliyor | w_i varyant (n) | olay-kohortu | sayi (AUC/F1) | tek_cagri (LLM'siz) | [?] | aynı desen; ≥50 halüsinasyon-olayı biriktikten sonra (şu an 3/50) ağırlık-grid taraması yapılabilir |
| İB-06c — U-skoru damıtma | `core/sema-sikistirma.md:38` | UYGUN-DEĞİL (i) TEK-ATIŞ | — | — | sayi | — | — | eşik 5 damıtma koşumu (şu an 0/5); n çok küçük, grid için anlamlı hücre kümesi yok |
| İB-06d — anahtar-kaydı k1/k2 | `core/baglam-anahtar-kaydi.md:240` civarı `[?]` (k1/k2 tanım satırı bu koşumda bulunamadı) | UYGUN — eksen tanımı eksik/veri bekliyor | k1-grid | k2-grid | sayi | tek_cagri (LLM'siz) | [?] | desen İB-06a'yla aynı sınıf; 10 emeklilik eşiği (şu an 1/10); k1/k2'nin tanım satırı bu koşumda AÇILAMADI → `[?]` |
| İB-06e — world-model §6 ölçüm işleri | `core/world-model-tasarimi.md:57-61` | UYGUN-DEĞİL (i) TEK-ATIŞ | — | — | sayi/sema | — | — | 5 madde SIRALI beyan edilmiş ("1→2→3→4→5", her biri ~1 koşum) — bağımsızlık yok (Ö-B ihlali), zincir |
| İB-07 (kalan) | `raporlar/2026-08-30-ib07-description-eval.md:5-9` | UYGUN — hemen koşulabilir | sorgu q06-q20 (15) | tekrar (1, yalnız tekrar-3 eksik) | etiket (secilen_skill) | tek_cagri | 15 | matris zaten tanımlı (İB-49 emsali), kütük append-only, kalan hücreler yalnız 60-45=15; karar gerektirmiyor, hücreler bağımsız |
| İB-09 (genişletme) | `raporlar/2026-08-30-ib09-yolc-v26-etki.md:9-15` | UYGUN — eksen tanımı eksik | vaka (yeni ara-zorluk kümesi, n [?]) | model (Opus, Sonnet — 2) | etiket (K_dusus evet/hayır) | tek_cagri | n×2 | mevcut 2 vaka × 2 model = 4 hücre bitti (uç-durumlar); rapor kendi "ara-zorluk vakalarında ayrışma test edilmedi" diyor — yeni vaka kümesi seçilirse genişletilebilir matris, ama vaka listesi henüz TANIMLANMAMIŞ |
| İB-11 | `veri/karar-borcu.jsonl` (İB-11) | UYGUN-DEĞİL (iv) İNSAN-GİRİŞİ | — | — | — | — | — | kalan iki iş Salih'in kendi terminaline/eline bağlı (md.43 (d)(e) + Adım-0 managed-settings) |
| İB-13 | aynı, İB-13 | UYGUN-DEĞİL (ii)/(iv) | — | — | — | — | — | "dörtlü deftere" adımı md.49 kontrolü + Salih tetiği bekliyor, tek yazım |
| İB-36 | aynı, İB-36 | UYGUN-DEĞİL (i) TEK-ATIŞ | — | — | — | — | — | ctypes ile tek özellik implementasyonu (sqlite3_stmt_status), koşullu-opsiyonel; eksen yok |
| İB-39 | aynı, İB-39 | UYGUN-DEĞİL (ii) KARAR-GEREKTİREN | — | — | — | — | — | atlas KOŞTU, 8 masa kalemi Salih hükmünü bekliyor; kalan iş karar, koşum değil |
| İB-53 | aynı, İB-53 | UYGUN-DEĞİL (ii) KARAR-GEREKTİREN | — | — | — | — | — | (a)/(b)/(c)/(d) seçim Salih'e sunuldu, dönüşüm koşumu hükme bağlı |
| İB-56 | aynı, İB-56 | UYGUN-DEĞİL (iii) SERBEST-METİN | — | — | serbest_metin | — | — | "Codex ne için kullanılır" atlas araştırması — sentez raporu, toplanamaz |
| İB-58 (kalan) | `raporlar/2026-08-30...` `[?]` künye satırı bulunamadı; borç satırı `veri/karar-borcu.jsonl` (İB-58) | UYGUN — hemen koşulabilir | script (hareket-tablo, loop-dedektor — 2; erisim-fts PK-12 BEKLE nedeniyle dışarıda) | AXI madde A1-A8 (8) | etiket (UYUMLU/UYUMSUZ/N-A) | tek_cagri (LLM'siz, deterministik grep/argparse denetimi) | 16 | `tools/AXI-STANDARDI.md` A1-A8 checklist zaten var, katman-hatti/anahtar-denetim örneği geçti (2/4); kalan 2 script × 8 madde bağımsız, deterministik, karar gerektirmiyor |
| İB-59 | `veri/karar-borcu.jsonl` (İB-59) | UYGUN-DEĞİL (ii)/(iv) | — | — | serbest_metin | — | — | pilot iş seçimi Salih'e ait + ölçüm çıktısı "kalite gözlemi" serbest-metin (İB-07/09 raporlarındaki gibi) |
| İB-64a | aynı, İB-64a | UYGUN-DEĞİL (iii) SERBEST-METİN | — | — | serbest_metin | — | — | mevcut kanıtı araştırma-kapısı FORMATINA bağlama işi, yazım |
| İB-64b | aynı, İB-64b | UYGUN-DEĞİL (iii) SERBEST-METİN | — | — | serbest_metin | — | — | D4 tasarım kartı ön-koşulu; sentez metni |
| İB-64c | aynı, İB-64c | UYGUN-DEĞİL (iii) SERBEST-METİN | — | — | serbest_metin | — | — | ekip-lideri tasarım paketi; çift-atlas sentez metni |
| İB-65 | `cc/gorev-2026-08-30-ib65-loop-pipeline-secim-atlas.md` (emir hazır, KOŞULMADI) | UYGUN-DEĞİL (iii) SERBEST-METİN | — | — | sema (kısmen) + serbest_metin | — | — | çıktı = "seçim şeması + masa-kalemi taslağı" — şema düğümleri var ama sentez ağırlıklı, tek atlas koşumu |
| İB-66 | `cc/gorev-2026-08-31-ib66-gozlemlenebilir-nested-loop-atlas.md` | UYGUN-DEĞİL (iii) SERBEST-METİN | — | — | serbest_metin | — | — | ürün-taraması + tasarım raporu, atlas sentezi |
| İB-67 | `cc/gorev-2026-08-31-ib67-paper-aday-bulgu-envanteri.md` | UYGUN — eksen tanımı eksik | bulgu-adayı (8, emirde ön-liste) | kaynak-türü (akademik/patent/blog — [?] emirde netleşmemiş) | etiket (YENİ/BİLİNEN-VAR/KISMEN) | tek_cagri | ~16-24 [?] | 8 aday × doğrulama-ölçütü bağımsız hücreler, etiket çıktı; ikinci eksenin değer kümesi emirde AÇIK yazılı değil → §1 Ö2 (yalanlanabilirlik) için netleştirme borcu |
| İB-68 | `cc/gorev-2026-08-31-ib68-urun-aday-envanteri.md` | UYGUN — eksen tanımı eksik | ürün-adayı (8, emirde ön-liste) | pazar-doğrulama-ölçütü ([?] netleşmemiş) | etiket | tek_cagri | ~16-24 [?] | İB-67'nin ticari ikizi, aynı eksik: ikinci eksen değer kümesi yazılı değil |
| **EK-1** erişim-kalibrasyon genişletme | `tools/erisim-kalibrasyon.py:28,76-92` | UYGUN — hemen koşulabilir | `--grid` genişletme-ağırlığı (7 değer: 0,0.5,1,1.5,2,3,4) | yöntem (vektor-e5, vektor-bge, vektor-e5-i8, vektor-bge-i8, fts5+gen — 5) | sayi (recall5/mrr/ndcg10) | tek_cagri (LLM'siz — saf SQL/py) | ~35 | araç ZATEN matris-koşuyor (İB-43); yeni eksen-değeri eklemek mevcut şemaya uyar, karar gerektirmez, LLM maliyeti SIFIR |
| **EK-2** d2-eval yeni-kol | `tools/d2-eval.py:100-104` | UYGUN — hemen koşulabilir | `--kol` (mevcut kollar, İB-49'da 4) | sorular/kosum kimliği | sayi (precision/recall) | tek_cagri | değişken | İB-49 emsali zaten kanıtlı matris deseni; yeni kol eklemek eksen genişletmesi, kurulu harness |
| **EK-3** denetçi-kalibrasyon çoklu-paket | `tools/denetci-kalibrasyon.py:56-57` | UYGUN — eksen tanımı eksik | paket-kümesi (n [?]) | puanlama-yöntemi (`--puanla`, değer kümesi kodda taranmadı) | sayi | tek_cagri | [?] | İB-10 zaten KAPANDI (12/12 yakalama) — bu artık YENİ bir aday-paket kümesi tanımlanırsa yeniden koşulabilir bakım-matrisi; ikinci eksenin değer kümesi bu koşumda okunmadı |
| **EK-4** silver-sağlık pencere-taraması | `tools/silver-saglik-kalibrasyon.py:22` | UYGUN — hemen koşulabilir | `--pencere` (int grid, örn. 5/10/20/30) | zaman-dilimi (mevcut günlük kayıtlar) | sayi | tek_cagri (LLM'siz) | ~4×n_dilim | tek parametre (`--pencere`, varsayılan 10) — grid'e açmak deterministik, LLM'siz, mevcut kütükten türer |

**Bonus not (borç havuzunda DEĞİL, karıştırılmasın):** `kuyruk/utopik-havuz.md:34` madde 17 ("sınıf-başına optimize wiki + karakter") model×effort × wiki-varyantı ekseniyle en temiz matris-adayı GÖRÜNÜYOR ama "ŞİMDİLİK BUILD YOK" ile parke edilmiş bir fikir — açık icra borcu değil, KB-02 zaten KAPANDI (`core/ajan-metodolojisi.md:36-37`). Matrise girmek için önce Katman-1 fikir-onayı gerekir → UYGUN-DEĞİL (ii) sayılır, tabloya ana satır olarak eklenmedi.

---

## 1. UYGUN işlerin önceliklendirmesi (N_hücre küçük ∧ değer yüksek)

**Hemen koşulabilir (eksen + veri hazır):**
1. **İB-07 kalan 15 hücre** — N=15, KB-20 kapanışını doğrudan tamamlıyor (değer yüksek, borç zaten %75 bitmiş), tek engel oturum-ajan-sayacı (yeni oturumda sıfırlanır).
2. **İB-58 kalan 2×8=16 hücre** — N=16, LLM maliyeti sıfır (deterministik script denetimi), axi-standardı borcunu 2/4→4/4 kapatır.
3. **EK-1 erişim-kalibrasyon genişletme** — N≈35 ama LLM'siz/çok ucuz, mevcut harness'in doğrudan uzantısı, hemen koşulabilir.
4. **EK-4 silver-sağlık pencere-taraması** — küçük N, LLM'siz, hemen koşulabilir.
5. **EK-2 d2-eval yeni-kol** — kurulu harness, N kol-sayısına bağlı [?].

**Eksen tanımı eksik (önce netleştirme borcu, sonra koşum):**
6. İB-06a (skill-kapısı τ/W) — veri eşiği 2/10, henüz erken.
7. İB-06d (anahtar-kaydı k1/k2) — veri eşiği 1/10, henüz erken; ayrıca k1/k2 tanım satırı bu koşumda bulunamadı `[?]`.
8. İB-09 genişletme — yeni "ara-zorluk vaka" kümesi tanımlanmalı.
9. İB-67 / İB-68 — ikinci eksenin (doğrulama/pazar ölçütü) değer kümesi emirde açık yazılı değil, §1 Ö2 ihlali; netleştirilmeden koşulamaz.
10. İB-06b (H formülü) — veri eşiği 3/50, çok erken.
11. EK-3 denetçi-kalibrasyon — yeni paket kümesi + puanlama-yöntemi değer kümesi tanımlanmalı.

---

## 2. İB-06 özel açılım

İB-06 tek borç değil, **5 ayrı kalibrasyon-eşiği** taşıyor (`core/skill-uretim-semasi.md:103`, `core/halusinasyon-paketi.md:31`, `core/sema-sikistirma.md:38`, `core/baglam-anahtar-kaydi.md:240`, `core/world-model-tasarimi.md:57`):

| alt-borç | eşik | mevcut sayaç | eksen kümesi | N_hücre kaba tahmin |
|---|---|---|---|---|
| a) skill-kapısı τ/W/β/n_val | 10 koşum | 2/10 | τ-grid × W-grid (β/n_val muhtemelen sabit tutulur ilk turda) | ~9-16 (3×3 ila 4×4) |
| b) H formülü ağırlıkları (w_i) | ≥50 olay | 3/50 | w_i varyant-kümesi × olay-kohortu | [?] — ağırlık grid boyutu tanımlı değil |
| c) U-skoru damıtma | 5 koşum | 0/5 | — (n çok küçük, grid anlamsız) | 0 (UYGUN-DEĞİL) |
| d) anahtar-kaydı k1/k2 | 10 emeklilik | 1/10 | k1-grid × k2-grid | [?] — k1/k2 tanım satırı bulunamadı |
| e) world-model §6 (NDV→tekrar→dil-çarpanı→sort-key→durum-denkliği) | — | sırayla ~1 koşum/madde | yok (SIRALI zincir) | 0 (UYGUN-DEĞİL, Ö-B ihlali) |

**Toplam:** 5 alt-borçtan **2'si UYGUN-DEĞİL** (c, e — n çok küçük ya da sıralı bağımlılık), **3'ü UYGUN ama veri-eşiği koşullu** (a, b, d — hiçbiri şu an koşulabilir değil, hepsi gerçek-kullanım olaylarının birikmesini bekliyor). Yani İB-06 "en güçlü aday" olsa da **bugün hiçbir alt-kalemi hemen koşulamaz** — bu emirdeki beklentiyle çelişen bir bulgu, açıkça işaretlendi.

---

## 3. `[?]` işaretli belirsiz noktalar

- `core/baglam-anahtar-kaydi.md` içinde k1/k2 parametrelerinin tam tanım satırı bu koşumda bulunamadı (yalnız dosyanın başka bir bölümü — anahtar-listesi — açıldı); N_hücre ve eksen değer kümesi teyit edilemedi.
- İB-06b H formülü ağırlık-grid boyutu (kaç varyant taranacak) hiçbir kaynakta sayısal olarak yazılı değil.
- İB-09 genişletmesi için "yeni ara-zorluk vaka" adaylarının bir listesi bulunamadı — bu koşumda üretilmedi (uydurmamak için boş bırakıldı).
- İB-67/68 ikinci ekseninin (doğrulama-ölçütü / pazar-ölçütü) değer kümesi ilgili görev emirlerinde (`cc/gorev-2026-08-31-ib67...md`, `-ib68...md`) bu koşumda AÇILMADI — yalnız borç-havuzu özeti okundu, emir dosyalarının tam metni taranmadı (bütçe/effort kısıtı); N_hücre kaba tahmindir.
- EK-3 denetçi-kalibrasyon `--puanla` parametresinin kabul ettiği değer kümesi script içinde aranmadı (yalnız argparse satırı görüldü).
- İB-58'in kalan iş için tam pointer'lı bir rapor dosyası bulunamadı; yalnız `veri/karar-borcu.jsonl` özet satırı ve `tools/AXI-STANDARDI.md` referansı kullanıldı, dosyanın kendisi bu koşumda açılmadı.
