# Sistem özeti (Salih için) · AS-OF 2026-10-25 · üretici `durum ozet` (Karar 122; kaynak `ortak/durum-olay.jsonl` + seans kayıtları)

Bu dosya her seans kapanışında yeniden üretilir. Elle düzenlenmez. Görsel: `ortak/graf/akis-<alan>.svg`.

## jarvis

**Konum:** seans `2026-10-25-jarvis` (kapandı 2026-10-25). Hedef: CV geri bildirim turu (16 madde) + alan ajanı push teli + Karar 122 akış grafı ve JSON seans kaydı. Hedef tutuldu.

**Son seansta ne değişti**
- CV 16 geri bildirim maddesiyle yenilendi. Nihai dosya Downloads/HasanSalihSahin_CV.pdf (depo dışı, md.49).
- Alan ajanı push teli daraldı: main ve force push yasak, kendi dalına push ve PR serbest. Commit 74ff357.
- Span dalı push edildi, PR #27 açıldı ve birleşti. Commit 0a625bc.
- Karar 122 uygulandı: akış grafı, JSON seans kaydı, Salih özeti, kapsül ve pano dondu. Commit 3d2ea62.
- SessionStart brifi grafı okuyor. Commit 36735d4.
- Karar 123 uygulandı: ölçüm kapısı kalktı, kütük id çakışması kodlandı, 9 plan düğümü açıldı. Commit 7c700fd.
- Bu kayıt ilk JSON seans kaydıdır. md teslim raporu yazılmadı.

**Hangi karar verildi**
- Karar 122: Seanslar arası iletişim graf ve JSON temeline geçti. Salih tek md özet ve D2/SVG okur.
- Karar 123: Plan değil icra. Değişiklik ölçüm, pilot ya da plan taslağı beklemeden uygulanır.
- Push teli seçenek 1: Yan oturum kendi PR'ını açar, Jarvis birleştirir.

**Senin kararını bekleyen**
- #9 veri bilimi şeridi: yeni ajan mı, Calc altında mı.
- Hangi öğrenme şeridiyle devam edileceği.

**Sapma:** Hedef açılışta beyan edilmedi (seans CV ile açıldı); Karar 122/123 seans içinde eklendi. Ölçüm kapılı Karar 122 taslağı Salih'in uyarısıyla Karar 123'e çevrildi.

Kayıt: `jarvis/raporlar/seans/seans-teslim-2026-10-25-cv-push-teli-karar122-123.json`

**Sırada (girdileri tamam)**
- #9 veri bilimi şeridi evi + deney tasarımı PROBE. Sonraki adım: Salih kararı: yeni ajan mı Calc altında mı; PROBE soru 1 (p=0.03) cevap bekliyor.
- #20 Python araçlarının Rust'a taşınması (Karar 117 EK-3, 5b): 59 araç, 7 parti. Sonraki adım: parti 1 omp'de (worktree omp-rust-p1); sonra parti 2-7 sırayla.
- #21 Karar 118 M1: atlas kodla pilot (emir şeması + Workflow + Rust V26/done + JSON teslim). Sonraki adım: sonraki gerçek araştırma görevinde koş.
- #31 Karar 103 M6: hakem şablonu v0 core/'a alınır (canlı test + başarı ölçüsü kapısı kalktı). Sonraki adım: sablonlar/ajan-iskelet/claude-ayar/agents/hakem.md.tmpl + .claude/agents/hakem.md → core/ şablon satırı; defter M6 notu güncelle.
- #32 Karar 102/103 (2): belirsiz perspektifler (doküman · ölçüm · hakem-kurma · antitez · planlama · öğretim) iç ölçüm beklemeden hükme bağlanır. Sonraki adım: varsayılan: alan ajanının alt-ajanı, hakem ayrı; Kanon/AlanAjani.lean + AGENTS satırı.
- #33 Karar 113 M3: md'siz koşum (oturum başı = kütük özeti, CLAUDE.md asgari) Sage pilotu beklemeden tüm alan ajanlarına. Sonraki adım: alan ajanı AGENTS.md'leri asgari + hook brifi durum oturum-basi; Karar 113 M2 'kanon metinleri pilot sonucuna bağlı' notu kapanır.
- #34 Karar 114 M5: core/ kural dosyalarının (kalan ~13, 224 KB) Lean modülüne taşınması; sıklık ölçümü yok, sırayla. Sonraki adım: envanter: lean/Kanon/*.lean.md karşılığı olmayan core/ dosyaları; parti başına PR.
- #37 m.29 eşik kalibrasyonları masa beklemeden sabitlenir: 128K bağlam seyri (KB-52) · skill-eşik n>=10 medyan 2x (Karar 51) · bayat-çekim 90 gün (Karar 69). Sonraki adım: Kanon/Butce.lean + Sabitler.lean sabitleri; 'Salih masasında' notları kapanır.
- #38 Karar 86 D8 / K-020 eval deseni (2 ucuz ön-ölçüm koşulu): koşul kalkar; desen ya uygulanır ya emekli. Sonraki adım: ilk V39 koşumu yoksa emekli kaydı; varsa M2 harness genellemesi doğrudan.
- #39 defterdeki ölçüm şartlı geri-açma cümleleri (Karar 103/104 M1-M2, 112, 113, 114 M5, 115) Karar 123'e göre sadeleştirilir. Sonraki adım: her cümle: 'arıza görülürse' biçimine; tek [damıtma] commit.

**Bekler (girdisi açık)**
- #35 Karar 118 M1: atlas-kosum doğrudan kodlu akışa geçer (pilot şartı kalktı): emir şeması JSON/Lean + Workflow + Rust V26/done + JSON teslim bekler: #21.
- #36 Karar 119 EK-1: 'kullan' 4 araç çıktı eşitliği ölçülmeden arşive; '?' 11 araç yeniden tarama kararı bekler: #22.

Görsel: `ortak/graf/akis-jarvis.svg` · kaynak `ortak/graf/akis-jarvis.d2`

## span

**Sırada (girdileri tamam)**
- #16 claude-mods öğrenme şeridi. Sonraki adım: ogren ile şerit aç: Claude Code modları (status line, pane, slash komutu, hook, toast); sistemde mod fikir yapısı; uygulanacak mod → Jarvis devri.

Görsel: `ortak/graf/akis-span.svg` · kaynak `ortak/graf/akis-span.d2`

