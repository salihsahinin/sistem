# Sistem özeti (Salih için) · AS-OF 2026-10-26 · üretici `durum ozet` (Karar 122; kaynak `ortak/durum-olay.jsonl` + seans kayıtları)

Bu dosya her seans kapanışında yeniden üretilir. Elle düzenlenmez. Görsel: `ortak/graf/akis-<alan>.svg`.

## jarvis

**Konum:** seans `2026-10-26-jarvis-2` (kapandı 2026-10-26). Hedef: Salih açılışta hedef vermedi; seans boyunca verilen emirler: Portal Parkur'u proje olarak kapat, ürünü ayrı repoya taşı, akış grafını HTML'de göster, PR #26'yı birleştir.. Hedef tutuldu.

**Son seansta ne değişti**
- Portal Parkur oyun demosu proje olarak kapandı. İş #44 Salih beyanıyla tamam. Commit 3112d1e.
- Ürün ayrı depoya taşındı: C:\sistem\portal-parkur + https://github.com/salihsahinin/portal-parkur (public, MIT). Tarihçe git subtree split ile 10 commit. Sistemde pointer README. Commit b96c673.
- Karar 124 deftere yazıldı: ürün = ayrı klasör + ayrı açık kaynak repo; sistem deposu ürün inşa aracı. Commit e1c6786.
- Seans düğümünden Jarvis'in önceden yazdığı hedef kaldırıldı (durum-olay.jsonl satırı duzeltme alanıyla). Salih'le oturumda hedefi Salih koyar.
- Akış grafı HTML üreticisi doğdu: tools/akis-graf-html.py + sablon. Bantlar (oturum · hedef · kategori), x = icra sırası, tek sıra yay görünümü, geri/ileri bağ grupları, ASD-STE100 panel, file:// ayrıntı bağlantıları. Commit 3f05cae.
- Karar 125 deftere yazıldı: graf içinde graf, hedef = alt grafın kapağı, özyinelemeli; kırıntı yolu + katlı hedef rozeti; 3 seviyeli deneme kütüğüyle doğrulandı. Commit 2c0d3b9.
- Arıza düzeltildi: durum graf --json <yol> yolu yok sayıp ortak/akis-graf.json üzerine yazıyordu; ayrıştırıcı .json uzantılı değeri yol kabul eder. Gerçek graf kütükten geri üretildi. Commit 2c0d3b9.
- PR #26 (Karar 117 EK-3 parti 2, 6 Python aracı Rust'a) main'e birleşti; tek çakışma tools/SCRIPTLER.md iki taraf korunarak çözüldü; cargo build --release yeşil. Commit d946dd7.
- Hafıza: feedback-oturum-hedefini-salih-koyar, feedback-urun-ayri-repo, project-graf-icinde-graf-karar-125, feedback-graf-html-aciklama-yuzeyi-degil; project-portal-parkur KAPANDI.

**Hangi karar verildi**
- Karar 124: Jarvis'in uzun vadede kullanmayacağı ürünler ayrı klasör + ayrı açık kaynak repoda yaşar; sistem deposu ürün inşa aracıdır.
- Karar 125: Graf içinde graf: hedef = alt grafın kapağı, özyinelemeli; büyük resimde düğüm sayısı sınırsız.
- Oturum hedefi: Salih'le oturumda seans hedefini Salih koyar; Jarvis önceden yazmaz.

**Senin kararını bekleyen**
- Karar 124 ve 125 kök kanon satırları (imza).
- 21 bayat worktree'nin kapatılması (Karar 95 EK).
- ac --kategori alanı ve durum graf --html Rust işi açılsın mı.

**Sapma:** Jarvis seans düğümüne önceden hedef yazdı; Salih bunu yanlış buldu, hedef kaldırıldı. Graf HTML tasarımı Salih'in beklediğinin tamamını karşılamadı; Salih ileride optimize edecek, şimdilik açıklama yüzeyi değil.

Kayıt: `jarvis/raporlar/seans/seans-teslim-2026-10-26-portal-parkur-kapanis-graf-karar-124-125.json`

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
- #45 akış grafı HTML tasarımı optimizasyonu (Salih: istediğim tam olmadı, ileride optimize edeceğim; şimdilik açıklama yüzeyi değil). Sonraki adım: Salih tasarım kararını verir; başlangıç Karar 125 kaydı + tools/akis-graf-html.py.

**Bekler (girdisi açık)**
- #35 Karar 118 M1: atlas-kosum doğrudan kodlu akışa geçer (pilot şartı kalktı): emir şeması JSON/Lean + Workflow + Rust V26/done + JSON teslim bekler: #21.
- #36 Karar 119 EK-1: 'kullan' 4 araç çıktı eşitliği ölçülmeden arşive; '?' 11 araç yeniden tarama kararı bekler: #22.

Görsel: `ortak/graf/akis-jarvis.svg` · kaynak `ortak/graf/akis-jarvis.d2`

## span

**Sırada (girdileri tamam)**
- #16 claude-mods öğrenme şeridi. Sonraki adım: ogren ile şerit aç: Claude Code modları (status line, pane, slash komutu, hook, toast); sistemde mod fikir yapısı; uygulanacak mod → Jarvis devri.

Görsel: `ortak/graf/akis-span.svg` · kaynak `ortak/graf/akis-span.d2`

