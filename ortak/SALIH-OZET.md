# Sistem özeti (Salih için) · AS-OF 2026-10-31 · üretici `durum ozet` (Karar 122; kaynak `ortak/durum-olay.jsonl` + seans kayıtları)

Bu dosya her seans kapanışında yeniden üretilir. Elle düzenlenmez. Görsel: `ortak/graf/akis-<alan>.svg`.

## jarvis

**Konum:** seans `2026-10-30-jarvis` (kapandı 2026-10-30). Hedef: Salih: fork oturumu kapanış sorusu; 2026-10-28-jarvis açık seansının kapatılması + Sokrates v1 devir borçları (Salih fark listesi, tek-turlu yapay zekâ kararı). Hedef tutuldu.

**Son seansta ne değişti**
- Fork sorusu cevaplandı: fork seansı ana oturumdan kapanmıştı, 'seans bitimi' gerekmedi; Salih fork'u sildi.
- 2026-10-28-jarvis (Lex #503) seansı diskteki hasat dosyasıyla geç kapatıldı (0eafa9c).
- Sokrates kimlik kararı kanona (core/sokrates-ajani.md §9) ve ürün reposuna (SURUM.md) yazıldı.
- #22 bitti: yan oturum PR #28 açtı; 11 Python aracı ve 8 hook gövdesi arsiv/kod/python altına taşındı, hook'lar yalnız Rust ikilisini çağırıyor; main'e birleşti (a3fd2ff), push'landı.
- Deney tasarımı probe soru 1 (p=0.03) yeniden soruldu, cevap gelmedi.
- 21 bayat worktree sayıldı: hepsi birleşmiş, main'e girmemiş commit 0, kirli dosya yalnız bronz kütük; kaldırma kararı Salih'te.

**Hangi karar verildi**
- Sokrates tek-turlu kimlik sorusunda karakterde kalır: 'Yapay zekâ mısın, dürüst ol' sorusunda tek turda bile karakter bozulmaz; v0.4 kuralı kesin, tuzak koşumundaki dürüst cevap ihlal.
- Karar 118 M2 icrası (PR #28): Rust karşılığı fark testini geçen Python araçları ve hook gövdeleri arşive indi; arşiv konumu kök arsiv/kod/python (emirdeki jarvis/arsiv yerine, tek arşiv yeri).

**Senin kararını bekleyen**
- Deney tasarımı probe soru 1 (p=0.03) şıkkı.
- Veri bilimi şeridinin evi: yeni ajan mı Calc altında mı (#9).
- 21 bayat worktree kaldırılsın mı (öneri: kaldır, dallar kalır).
- Kanon/README dosyalarındaki python3 tarifleri PR #28 sonrası güncellensin mi (Katman-1).

**Sapma:** Sokrates fark listesi gelmedi; Salih 'şimdilik yeterli' dedi, v1.3 beklemede. Seans ortasında #22 Python arşiv PR'ı eklendi ve bitti.

Kayıt: `jarvis/raporlar/seans/seans-teslim-2026-10-31-fork-kapanis-py-arsiv-pr28.json`

**Sırada (girdileri tamam)**
- #9 veri bilimi şeridi evi + deney tasarımı PROBE. Sonraki adım: Salih kararı: yeni ajan mı Calc altında mı; PROBE soru 1 (p=0.03) cevap bekliyor.
- #20 Python araçlarının Rust'a taşınması (Karar 117 EK-3, 5b): 59 araç, 7 parti. Sonraki adım: parti 1 omp'de (worktree omp-rust-p1); sonra parti 2-7 sırayla.
- #21 Karar 118 M1: atlas kodla pilot (emir şeması + Workflow + Rust V26/done + JSON teslim). Sonraki adım: sonraki gerçek araştırma görevinde koş.
- #31 Karar 103 M6: hakem şablonu v0 core/'a alınır (canlı test + başarı ölçüsü kapısı kalktı). Sonraki adım: sablonlar/ajan-iskelet/claude-ayar/agents/hakem.md.tmpl + .claude/agents/hakem.md → core/ şablon satırı; defter M6 notu güncelle.
- #32 Karar 102/103 (2): belirsiz perspektifler (doküman · ölçüm · hakem-kurma · antitez · planlama · öğretim) iç ölçüm beklemeden hükme bağlanır. Sonraki adım: varsayılan: alan ajanının alt-ajanı, hakem ayrı; Kanon/AlanAjani.lean + AGENTS satırı.
- #33 Karar 113 M3: md'siz koşum (oturum başı = kütük özeti, CLAUDE.md asgari) Sage pilotu beklemeden tüm alan ajanlarına. Sonraki adım: alan ajanı AGENTS.md'leri asgari + hook brifi durum oturum-basi; Karar 113 M2 'kanon metinleri pilot sonucuna bağlı' notu kapanır.
- #34 Karar 114 M5: core/ kural dosyalarının (kalan ~13, 224 KB) Lean modülüne taşınması; sıklık ölçümü yok, sırayla. Sonraki adım: envanter: lean/Kanon/*.lean.md karşılığı olmayan core/ dosyaları; parti başına PR.
- #36 Karar 119 EK-1: 'kullan' 4 araç çıktı eşitliği ölçülmeden arşive; '?' 11 araç yeniden tarama kararı. Sonraki adım: raporlar/2026-10-17-hazir-karsilik-denetimi.md listesinden 4+11 kalem; arşiv PR'ı (#22 ile birlikte).
- #37 m.29 eşik kalibrasyonları masa beklemeden sabitlenir: 128K bağlam seyri (KB-52) · skill-eşik n>=10 medyan 2x (Karar 51) · bayat-çekim 90 gün (Karar 69). Sonraki adım: Kanon/Butce.lean + Sabitler.lean sabitleri; 'Salih masasında' notları kapanır.
- #38 Karar 86 D8 / K-020 eval deseni (2 ucuz ön-ölçüm koşulu): koşul kalkar; desen ya uygulanır ya emekli. Sonraki adım: ilk V39 koşumu yoksa emekli kaydı; varsa M2 harness genellemesi doğrudan.
- #39 defterdeki ölçüm şartlı geri-açma cümleleri (Karar 103/104 M1-M2, 112, 113, 114 M5, 115) Karar 123'e göre sadeleştirilir. Sonraki adım: her cümle: 'arıza görülürse' biçimine; tek [damıtma] commit.
- #45 akış grafı HTML tasarımı optimizasyonu (Salih: istediğim tam olmadı, ileride optimize edeceğim; şimdilik açıklama yüzeyi değil). Sonraki adım: Salih tasarım kararını verir; başlangıç Karar 125 kaydı + tools/akis-graf-html.py.
- #47 jarvis-oda v0.2 + jarvis-graf v0.1 kuruldu, duman testi geçti; Salih: istenen seviyede değil. Sonraki adım: Salih fark listesi verir, Jarvis mods/ üzerinde itere eder.
- #48 Öğrenme kutusu: ispat-arama algoritmaları (best-first/A*, MCTS+policy/value, HTPS, expert iteration, PRM+test-time compute, FunSearch/AlphaEvolve) ve search-then-distill döngüsü; kaynak Lex #503 dk 10-30 (Moitra 14:20, 18:54). Sonraki adım: Salih istediğinde ogren şeridinde kutu kutu; önce canlı doğrulama (AS-OF).
- #71 jarvis-oda v0.4: oda_gorev_ver ajan alanı (rol ajanı işçi, yapan≠ölçen odada görünür); yan oturum yazdı, commit 7e78afb. Sonraki adım: ana oturum yeniden başlatılınca hakem turunu ajan:hakem ile odada koş; canlı doğrulama.

**Bekler (girdisi açık)**
- #35 Karar 118 M1: atlas-kosum doğrudan kodlu akışa geçer (pilot şartı kalktı): emir şeması JSON/Lean + Workflow + Rust V26/done + JSON teslim bekler: #21.

Görsel: `ortak/graf/akis-jarvis.svg` · kaynak `ortak/graf/akis-jarvis.d2`

## span

**Sırada (girdileri tamam)**
- #16 claude-mods öğrenme şeridi. Sonraki adım: ogren ile şerit aç: Claude Code modları (status line, pane, slash komutu, hook, toast); sistemde mod fikir yapısı; uygulanacak mod → Jarvis devri.

Görsel: `ortak/graf/akis-span.svg` · kaynak `ortak/graf/akis-span.d2`

## sage

**Konum:** seans `2026-10-30-sage` (açık). Hedef: Aksiyom ve postülat kavramlarını açıklamak (Salih sorusu).

Görsel: `ortak/graf/akis-sage.svg` · kaynak `ortak/graf/akis-sage.d2`

