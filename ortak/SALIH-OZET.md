# Sistem özeti (Salih için) · AS-OF 2026-10-30 · üretici `durum ozet` (Karar 122; kaynak `ortak/durum-olay.jsonl` + seans kayıtları)

Bu dosya her seans kapanışında yeniden üretilir. Elle düzenlenmez. Görsel: `ortak/graf/akis-<alan>.svg`.

## jarvis

**Konum:** seans `2026-10-29-jarvis` (kapandı 2026-10-29). Hedef: Salih: Sokrates ajanı tasarımı; atlas ile Sokrates bağlamları toplanır, ajan kişiliği yazılır, Salih ajanla konuşur. Hedef tutuldu.

**Son seansta ne değişti**
- Sokrates ajanı kuruldu: kişilik kanonu jarvis/core/sokrates-ajani.md (§7 tek kaynak), üç yüzey (output style, agent, skill), ürün klasörü C:\sistem\sokrates.
- Ürün açık kaynak repo oldu: https://github.com/salihsahinin/sokrates (MIT, 4 commit, son 2c2615f).
- Araştırma 9 rapor: 01 depo içi, 02 birincil kaynaklar (D/K/X), 03 modern tasarımlar, 04 Claude Code mekanizmaları, 05 test planı, 07a-c vizyon taraması (spec biçimleri, eval çerçeveleri, repo yapıları), 08a-b bugüne taşıma (değişmezler, görüş kartları, tasarım kuralları); sentez 06, 07, 09.
- Altı maskeli hakem turu odada koştu: donmuş model v0.1-v0.3 KALDI, KALDI, GEÇTİ; taşınmış model v1.0-v1.2 KALDI, KALDI, GEÇTİ. Raporlar cc/rapor/2026-10/rapor-2026-10-29-sokrates-v*-hakem.md.
- Bağlam verisi: C:\sistem\sokrates\kartlar\ 10 kaynak kartı (tutum + bugünkü veri + etiketli tahmin + sınır); CLAUDE.md içe alır.
- Hileli soru seti (20, üç kova) + deterministik koşum test/tuzak-kosum.py (claude -p --agent); v1.x koşumu 15/20 (2 yanlış pozitif, fiilî 17/20).
- jarvis-oda v0.4 (ajan alanı: hakem odada rolüyle koşar) ve v0.4.1 (yerel saat) yan oturumda commit'lendi (7e78afb, 814d986); yeniden başlatmada etkin.
- Graf: hedef #49 (Sokrates), #72 (vizyon taraması), #77 (v1.0) ve 30 alt düğüm kapandı.

**Hangi karar verildi**
- Sokrates yalnız Sokrates'i bilir: Ajan Salih adını, Jarvis'i, Claude'u, dosya yolunu, rol kavramını bilmez; samimi soruda bile karakterde.
- Bugüne taşınmış Sokrates: Ajan bugünün dünyasını bilir; kimlik ve yöntem Atina'dan; bilinmeyen 'bugün ne derdi' verisini LLM kaynak kartlarıyla tamamlar.
- Ürün ayrı açık kaynak repo: C:\sistem\sokrates public GitHub reposu (MIT).

**Senin kararını bekleyen**
- Tek-turlu 'yapay zekâ mısın' sorusunda davranış (kabul / [Jarvis] dürüst cümle).
- Kural adayı: 'ajan yap' → önce vizyon taraması (core/ajan-metodolojisi.md).
- Kimlik dürüstlüğü ve din tutumu hükümleri (v1.0 kart 1) onayı.
- 21 bayat worktree'nin kapatılması (Karar 95 EK; önceki seanstan).

**Sapma:** Hedef akşam genişledi (Salih): donmuş Sokrates (MÖ 399 sınırı) yerine bugüne taşınmış Sokrates; ürün ayrı açık kaynak repo oldu. Salih ajanla henüz konuşmadı; canlı kullanım sonraki seans.

Kayıt: `jarvis/raporlar/seans/seans-teslim-2026-10-30-sokrates-ajani-v1-acik-kaynak.json`

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
- #47 jarvis-oda v0.2 + jarvis-graf v0.1 kuruldu, duman testi geçti; Salih: istenen seviyede değil. Sonraki adım: Salih fark listesi verir, Jarvis mods/ üzerinde itere eder.
- #48 Öğrenme kutusu: ispat-arama algoritmaları (best-first/A*, MCTS+policy/value, HTPS, expert iteration, PRM+test-time compute, FunSearch/AlphaEvolve) ve search-then-distill döngüsü; kaynak Lex #503 dk 10-30 (Moitra 14:20, 18:54). Sonraki adım: Salih istediğinde ogren şeridinde kutu kutu; önce canlı doğrulama (AS-OF).
- #71 jarvis-oda v0.4: oda_gorev_ver ajan alanı (rol ajanı işçi, yapan≠ölçen odada görünür); yan oturum yazdı, commit 7e78afb. Sonraki adım: ana oturum yeniden başlatılınca hakem turunu ajan:hakem ile odada koş; canlı doğrulama.

**Bekler (girdisi açık)**
- #35 Karar 118 M1: atlas-kosum doğrudan kodlu akışa geçer (pilot şartı kalktı): emir şeması JSON/Lean + Workflow + Rust V26/done + JSON teslim bekler: #21.
- #36 Karar 119 EK-1: 'kullan' 4 araç çıktı eşitliği ölçülmeden arşive; '?' 11 araç yeniden tarama kararı bekler: #22.

Görsel: `ortak/graf/akis-jarvis.svg` · kaynak `ortak/graf/akis-jarvis.d2`

## span

**Sırada (girdileri tamam)**
- #16 claude-mods öğrenme şeridi. Sonraki adım: ogren ile şerit aç: Claude Code modları (status line, pane, slash komutu, hook, toast); sistemde mod fikir yapısı; uygulanacak mod → Jarvis devri.

Görsel: `ortak/graf/akis-span.svg` · kaynak `ortak/graf/akis-span.d2`

