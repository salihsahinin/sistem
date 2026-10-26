# Sistem özeti (Salih için) · AS-OF 2026-10-26 · üretici `durum ozet` (Karar 122; kaynak `ortak/durum-olay.jsonl` + seans kayıtları)

Bu dosya her seans kapanışında yeniden üretilir. Elle düzenlenmez. Görsel: `ortak/graf/akis-<alan>.svg`.

## jarvis

**Konum:** seans `2026-10-26-jarvis` (kapandı 2026-10-26). Hedef: Portal x Mirror's Edge tarzı birinci şahıs parkur+portal oyununun Godot ile açık kaynak referanslardan inşası; WhatsApp videosuyla görsel/mekanik eşleşmeye kadar iterasyon. Hedef tutuldu.

**Son seansta ne değişti**
- projects/portal-parkur doğdu: Godot 4.7.2 oyunu, 11 commit (11888f4 → 9abebce), 9 otomatik mekanik testi geçer (test.bat).
- Portal görüntüleme ve teleport: VojtaStruhar/godot-portals-plugin (MIT) çalışma zamanı yerleştirmeyle; oval maske, yüzeye sığdırma, duvar istisnası, portal içinden atış.
- Parkur: duvar koşusu, dikey tırmanış, mantle, vault, kayma, çömelme, iniş; eller, seviye, sesler kodla üretilir.
- Kamera profili: ham 1:1 fare, F4 canlı ayar paneli (user://ayarlar.cfg).
- Hareket katmanları: Source AirAccelerate bunny hop; MW2019 tık-kayma, slide cancel, inişte kayma; Shift sprint, çift Shift taktik.
- Minecraft modeli varsayılan: azalea-rs/azalea azalea-physics portu (20 tick, 0.42 zıplama, 0.546/0.91 atalet, blok kayganlığı); yatay ×3, dikey ×1.5 ölçek; zincir bonusu.
- Harita: Minecraft bhop sunucu tarzı kurs (seviye_bhop.gd) varsayılan; çatı+portal haritası F4 seviye=1.
- Dying Light makinede kurulu değil; ayar dosyası okunamadı. Ticari kod decompile edilmedi (EULA).
- Godot 4.7.2 C:\tools\godot altında; referans klonlar projects/portal-parkur/referans (git dışı).
- Hafıza: project-portal-parkur.md, feedback-bash-heredoc-tek-tirnak.md (tek tırnaklı heredoc bu Bash aracında çöker).

**Hangi karar verildi**
- Portal Parkur kaynak kararı: Ticari oyun ikilileri decompile edilmez; mekanikler açık kaynak karşılıklarından kurulur.

**Senin kararını bekleyen**
- Oyunun hedef tanımı (hangi oyunun hangi mekaniği; tek model mi katmanlı mı).
- Push beyanı (bugünkü 12 commit origin'e atılmadı).

**Sapma:** Oyun v1 bitti; sonraki promptlar hedefi genişletti (Dying Light bakış, CS bhop, MW2019 kayma, Minecraft fiziği, bhop kursu). Salih bağlamın karıştığını beyan etti; temiz tanım sonraki seansta.

Kayıt: `jarvis/raporlar/seans/seans-teslim-2026-10-26-portal-parkur-oyunu.json`

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
- #44 oyun tanımı karışık (ME/Portal → DL/CS/MW → Minecraft bhop kursu katmanları üst üste). Sonraki adım: sonraki seans: Salih temiz oyun tanımını verir, Jarvis katmanları o tanıma göre ayıklar (projects/portal-parkur, F4 model/seviye anahtarları).

**Bekler (girdisi açık)**
- #35 Karar 118 M1: atlas-kosum doğrudan kodlu akışa geçer (pilot şartı kalktı): emir şeması JSON/Lean + Workflow + Rust V26/done + JSON teslim bekler: #21.
- #36 Karar 119 EK-1: 'kullan' 4 araç çıktı eşitliği ölçülmeden arşive; '?' 11 araç yeniden tarama kararı bekler: #22.

Görsel: `ortak/graf/akis-jarvis.svg` · kaynak `ortak/graf/akis-jarvis.d2`

## span

**Sırada (girdileri tamam)**
- #16 claude-mods öğrenme şeridi. Sonraki adım: ogren ile şerit aç: Claude Code modları (status line, pane, slash komutu, hook, toast); sistemde mod fikir yapısı; uygulanacak mod → Jarvis devri.

Görsel: `ortak/graf/akis-span.svg` · kaynak `ortak/graf/akis-span.d2`

