# Sistem özeti (Salih için) · AS-OF 2026-10-28 · üretici `durum ozet` (Karar 122; kaynak `ortak/durum-olay.jsonl` + seans kayıtları)

Bu dosya her seans kapanışında yeniden üretilir. Elle düzenlenmez. Görsel: `ortak/graf/akis-<alan>.svg`.

## jarvis

**Konum:** seans `2026-10-27-jarvis` (kapandı 2026-10-27). Hedef: Salih: video (Claude mods, 3 fikir) analizi; iki mod kurulur: jarvis-oda (lobi eşgörevi, Fable planlar / Haiku-Sonnet-Opus uygular, çok-ajanlı) + jarvis-graf (akış grafı paneli); plansız icra + siber güvenlik dışı + otomasyon odağı kaydı. Hedef tutuldu.

**Son seansta ne değişti**
- Video (Instagram, 45 sn) karelerden çözüldü: oturumlar arası mesajlaşma, Claude Code içi ajan panosu, zorluğa göre model yönlendirme.
- Karar 126 deftere yazıldı: fikir = plansız icra, siber güvenlik konusu ve örneği yok, odak otomasyon + human-in-the-loop (commit 4c6cdf4).
- jarvis-oda modu yazıldı ve çalıştı: oda, plan, görev dağıtımı (kolay→Haiku, orta→Sonnet, zor→Opus), işçi raporu, öneri-karar kapısı, pano (mods/jarvis-oda).
- jarvis-oda v0.2: anlık paralel işçi sayısı değişken (maksParalel, kuyruk, panoda −/+) ve ortak sohbet (Salih/Jarvis/tüm işçiler, #N adresleme) (commit 0bce6f4).
- jarvis-graf modu yazıldı: akış grafı pane (SVG bantlar hedef/iş/seans, filtre, düğüm detayı, HTML aç, durum graf) (mods/jarvis-graf).
- Duman testi geçti: Haiku işçisi görevi bitirdi, sohbete cevap verdi, öneri bıraktı, Jarvis [oda] mesajıyla uyandı.
- Kurulum: ~/.claude/settings.json CLAUDE_CODE_PLUGIN_DIRS iki mod yolu; README kurulum bölümü (commit a0a950f).
- Modlar lobi MCP kullanmaz; durum $.store/$.state içinde yerel.
- Kanon kopyası jarvis/mods/ (görünür klasör); kaynak-kodu/README.md satırı eklendi.

**Hangi karar verildi**
- Karar 126: Fikir plan taslağı değil doğrudan icra; siber güvenlik konusu ve örneği kullanılmaz; odak otomasyon ve human-in-the-loop; Jarvis üç mod fikrini kendi önerisi olarak üretebilir.

**Senin kararını bekleyen**
- Karar 126 kural adayının kök md.13'e imzası.
- 21 bayat worktree'nin kapatılması (Karar 95 EK).
- Mod iterasyon fark listesi (oda: rapor görünümü, sohbet balonu, oda geçmişi; graf: tıklanabilir SVG, lejant, kırıntı yolu).

**Sapma:** Modlar kuruldu ve çalıştı; Salih 'istediğim seviyede değil, itere edilmeli' dedi. İterasyon fark listesi Salih'ten bekler.

Kayıt: `jarvis/raporlar/seans/seans-teslim-2026-10-28-claude-modlari-oda-graf-karar-126.json`

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

**Bekler (girdisi açık)**
- #35 Karar 118 M1: atlas-kosum doğrudan kodlu akışa geçer (pilot şartı kalktı): emir şeması JSON/Lean + Workflow + Rust V26/done + JSON teslim bekler: #21.
- #36 Karar 119 EK-1: 'kullan' 4 araç çıktı eşitliği ölçülmeden arşive; '?' 11 araç yeniden tarama kararı bekler: #22.

Görsel: `ortak/graf/akis-jarvis.svg` · kaynak `ortak/graf/akis-jarvis.d2`

## span

**Sırada (girdileri tamam)**
- #16 claude-mods öğrenme şeridi. Sonraki adım: ogren ile şerit aç: Claude Code modları (status line, pane, slash komutu, hook, toast); sistemde mod fikir yapısı; uygulanacak mod → Jarvis devri.

Görsel: `ortak/graf/akis-span.svg` · kaynak `ortak/graf/akis-span.d2`

