# Sistem özeti (Salih için) · AS-OF 2026-11-11 · üretici `durum ozet` (Karar 122; kaynak `ortak/durum-olay.jsonl` + seans kayıtları)

Bu dosya her seans kapanışında yeniden üretilir. Elle düzenlenmez. Görsel: `ortak/graf/akis-<alan>.svg`.

## jarvis

**Konum:** seans `oda-202611101157-depo-denetimi-2026-11-10` (açık).

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
- #48 Öğrenme kutusu: ispat-arama algoritmaları (best-first/A*, MCTS+policy/value, HTPS, expert iteration, PRM+test-time compute, FunSearch/AlphaEvolve) ve search-then-distill döngüsü; kaynak Lex #503 dk 10-30 (Moitra 14:20, 18:54). Sonraki adım: Salih istediğinde ogren şeridinde kutu kutu; önce canlı doğrulama (AS-OF).
- #71 jarvis-oda v0.4: oda_gorev_ver ajan alanı (rol ajanı işçi, yapan≠ölçen odada görünür); yan oturum yazdı, commit 7e78afb. Sonraki adım: ana oturum yeniden başlatılınca hakem turunu ajan:hakem ile odada koş; canlı doğrulama.
- #83 Ders: depo dosya mimarisi, 8 kutu, düzeltme üzerinde öğretim (brif kuyruk/ders-dosya-mimarisi-2026-10-31.md). Sonraki adım: fork oturumunda 'seans başı, dosya-mimarisi' → ogren; kutu 4/5/8 kanon satırları Salih imzasıyla ana oturumda.
- #84 Ders: ontolojik encode, 8 kutu, düzeltme üzerinde öğretim (brif kuyruk/ders-ontolojik-encode-2026-11-01.md). Sonraki adım: fork oturumunda 'seans başı, ontolojik-encode' → ogren; Katman-1 kalemler (Lean üst tip, sözlük tanımları) Salih imzasıyla ana oturumda.
- #85 Bitirme tezi dersi: iki eklemli kol, 12 kutu (Mihelj Robotics B5/9/10 + NN/MPC/RL); kutu 1-8 kavramsal tamam, HTML sayfalar Mustafata2/robot_arm_control salih dalında. Sonraki adım: kutu 9 (Neural Network Dynamics Learning) alt adımlı; sonra 10-12; pratik: formülleri Python'da kurmak (Salih eli).
- #86 Müzik projeleri (şarkı yönlendirme melez + sembolik üretim + kalite bariyeri): 3 atlas + en olabilir sürüm brifi raporlar/2026-11/muzik-projeleri-en-olabilir-surum-2026-11-05.md. Sonraki adım: Salih başlama beyanı; ilk adım müzik kodlama şeması, sonra yerel analiz hattı (200-500 parça).
- #87 jarvis-oda v0.6 + jarvis-graf v0.2 canlı test ve ikinci iterasyon turu. Sonraki adım: Salih yeni oturumda /oda ve /graf dener (görev sınıfı, işçiye tıklama, sohbet kaydırma, düğüm detayı, HTML aç, oda_katil) ve fark listesi verir; Jarvis dis.ts-araclar.ts döngüsünü durum.ts'ye indirir; ortak/oda/ commit kararı Salih'te.
- #88 müzik projeleri ön-bilgi dersi: 13 kutu, kutu 1 sorusunda. Sonraki adım: Salih: kutu 1 sorusunu cevaplar, kutu 2den devam; kayıt jarvis/kuyruk/ders-muzik-on-bilgi-2026-11-05.md.
- #108 Depo denetimi inceleme listesi: Salih hükmü bekleyen kalemler (rapor §3 A3,A5,A6,B9-B13,C16-C21,D22-D28,E29-E39 ve §5.3 41-54). Sonraki adım: Salih kalem seçer; raporlar/2026-11/denetim-depo-2026-11-10.md §3 ve §5.3.

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

