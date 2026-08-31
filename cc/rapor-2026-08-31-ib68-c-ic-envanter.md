# İB-68 C2 iç envanter — 7 aday, çalışan-kanıt taraması

*Künye: AS-OF 2026-08-31, aile C2 (ürün-adayı ayağı), model sonnet, işçi-ajan koşumu, rejim maliyet-öncelikli. Kaynak: repo-içi Read/Grep/Bash, web YOK.*

## ① Gözlemlenebilir nested-loop koşucusu
- **Mekanizma:** `tools/gnhf-izle.py` gnhf worktree'sindeki `.gnhf/runs/<run>/iteration-N.jsonl` stream-json dosyalarını canlı okunur satıra çevirir (tail-f benzeri).
- **Pointer:** `tools/gnhf-izle.py:1-30`; kullanım raporları `raporlar/2026-08-31-ib66-*.md`, `raporlar/2026-08-31-ib65-*.md`.
- **Kanıt:** e600a7 koşumu 3M token tavan + 3/3 iterasyon 0 arızayla bitti (`raporlar/2026-08-31-k010-a3-loop-1.md:12-13`); ib66 atlası 6 işçi + 1 hakem ajanla koştu.
- **Taşıma-maliyeti:** (1) gnhf worktree bağımlılığını genelleştir (şu an `~/jarvis-gnhf-worktrees/*` sabit); (2) stream-json şeması Claude Code sürümüne bağlı, versiyon kilidi gerekir; (3) çıktı formatı repo-terminoloji Türkçe, ürün için i18n; (4) hata/timeout senaryosu için test yok, eklenmeli.

## ② paralel-kapı + manifest rejimi
- **Mekanizma:** `tools/paralel-kapi.py` `veri/manifest/*.json` birim-manifestlerini Bernstein koşuluyla (yazar∩yazar=∅ vb.) çiftler halinde PK-1..12 kurallarına göre hükme bağlar (PARALEL-SERBEST/SIRALI/RED/BEKLE), deterministik dalga planı üretir.
- **Pointer:** `tools/paralel-kapi.py:1-15`; manifest: `veri/manifest/*.json` (17 dosya).
- **Kanıt:** `raporlar/2026-08-30-paralel-kademe-pilot.md`: 8 birim/28 çift matrisi, N=1→2→3 kademe koşuldu, çakışma 0, kapı çıkışı 0, ~14 eşzamanlı ajan darboğazsız.
- **Taşıma-maliyeti:** (1) manifest şeması İB-63 PROTOTİP-1'e özgü, jenerikleştirme; (2) "sahada-diğer-oturum" (PK-12) tespiti repo-özel dosya kilidi mantığı, genel kilit mekanizmasına bağlanmalı; (3) kademe/dalga planlayıcı LLM'siz ama Bernstein testi grain=dosya, alt-dosya bölüm granülü yok; (4) `--json`/AXI arayüzü var ama CLI paketleme (pip/npm) yapılmamış.

## ③ karar-masası deseni
- **Mekanizma:** Lavish tabanlı yapılandırılmış karar toplantısı — kart başına `queueKey` (mükerrer-gönderim güvenli), seçenek başına açıklama-bloğu, öneri-rozetli ama ön-seçimsiz (m.6 kör-onay freni), serbest-mesaj kanalı.
- **Pointer:** `kuyruk/arsiv/senaryo-defteri-arsiv-2026-08-29.md:41`, uygulama izi `kuyruk/gelen-2026-08-30-a1-sayac-karar.md:14`.
- **Kanıt:** "7 karttan 5'i tek turda hükme bağlandı" (ölçülmüş, tek koşum); ayrı/genel bir `masa-kalemi` modülü/script YOK — desen anlatı+Lavish kullanımı olarak kayıtlı, kod-çekirdeği repo'da bulunmadı `[?]`.
- **Taşıma-maliyeti:** (1) desen kod değil, Lavish UI konvansiyonu — ürünleştirmek için gerçek bileşen yazılmalı; (2) queueKey/mükerrer-gönderim güvenliği mekanizması belgelenmemiş, tersine mühendislik gerekir; (3) hüküm-sonrası kayıt-durumu gösterimi elle güncellendi (rapor: "eksik" notu) — otomasyon yok; (4) m.6/m.40 formatı JARVIS-özel kural dili, jenerik UI kopyalanmalı.

## ④ kanıt-kapılı otonomi merdiveni A1-A4
- **Mekanizma:** K-010 zinciri — dört kapı (A1 5 pilot koşum · A2 tatbikat-kaydı · A3 goal/loop 3 ayak · A4 denetim-çatalı), her kapı ölçülmüş kanıt-paketiyle ilerler, GO hükmü yalnız Salih (m.31).
- **Pointer:** `kuyruk/k010-zincir-2026-08-29.md:1-56`.
- **Kanıt:** durum satırında A1 5/5 KESİN, A2 kapı tamam, A3 2/3 (goal 1 OK + loop 1 OK, uzun-loop 1/3), A4 bekliyor — kısmen çalışır, tam kapanmamış.
- **Taşıma-maliyeti:** (1) kapı eşikleri (5/3/3 koşum sayıları) JARVIS'in kendi olgunluk hükmü, ürün için eşik yeniden tanımlanmalı; (2) "koşum-bazlı sayaç" elle güncellenen tablo, otomatik durum-makinesi değil; (3) A4 çatal-hükmü tasarımı henüz yok (`İB-64b` bekliyor); (4) Salih-imza kapısı (m.31) insan-onay adımı — ürün akışına UI/API olarak modellenmeli.

## ⑤ gnhf-izle sınıfı ajan-konuşma izleyicisi (①'den ayrı, izleyici bileşeni)
- **Mekanizma:** aynı script `tools/gnhf-izle.py` — worktree keşfi (`en_yeni_worktree()`), satır kısaltma (`kisalt()`), stdlib-only, salt-okur, LLM YOK.
- **Pointer:** `tools/gnhf-izle.py:20-30` (yardımcı fonksiyonlar), `:52` (`main()`), toplam 92 satır.
- **Kanıt:** çıkış kodu sözleşmesi var (0 tamam/2 bulunamadı); gerçek koşumda kullanıldığı ①'deki rapor referanslarıyla doğrulanıyor — izleyici tek başına ayrı ölçüm/test dosyası yok `[?]`.
- **Taşıma-maliyeti:** (1) `.gnhf/runs/` dizin yapısı gnhf-özel, genel ajan-runner soyutlaması gerekir; (2) tail-f mantığı `glob` polling, event-driven değil (verimsiz olabilir); (3) format sadece Claude Code stream-json'a bağlı, başka sağlayıcı desteklenmiyor; (4) test/CI kapsamı yok.

## ⑥ repo-freni paketi (policy-as-code)
- **Mekanizma:** `.claude/settings.json` deny/ask listeleri (core/CLAUDE.md/.claude yazımına Edit/Write engeli, git push/screencapture için sor) + PreToolUse hook `pretool-core-tel.sh`: Bash komutunu regex'le tarar (`>`, `mv/cp/rm/sed -i`, `git checkout/reset` → `core/|CLAUDE.md|.claude/` hedefliyse) ve exit 2 ile bloklar.
- **Pointer:** `.claude/settings.json:1-30`; `.claude/hooks/pretool-core-tel.sh:1-24` (tam dosya 24 satır, gösterilen).
- **Kanıt:** hook kendini "tökezleme-teli, sınır değil" olarak tanımlıyor (yorum satırı); canlı PASS vakası K-010 A2 kanıtında referans veriliyor (`raporlar/...A2 kanıt 3/3` — PreToolUse canlı PASS vakası) ama bu ajanın bütçesinde doğrudan doğrulanmadı `[?]`.
- **Taşıma-maliyeti:** (1) regex-tabanlı tel, kaçırdığı desen olabilir diye belgeli — sertleştirme (allowlist/sandbox) gerekir üretim için; (2) macOS/Windows python3/python ikili-yol seçimi taşınabilirlik yükü; (3) settings.json + hook script ayrı dosyalar, tek paket haline getirilmeli; (4) Agent-matcher hook'u (`pretool-ajan-fren.sh`) ayrıca incelenmedi.

## ⑦ hareket kütüğü + AXI standardı
- **Mekanizma:** `tools/hareket-tablo.py` oturum transkriptlerini (`~/.claude/projects/*/*.jsonl`) BRONZ→SİLVER→GOLD pipeline'ıyla repoya indirir; `tools/AXI-STANDARDI.md` (SALT-OKUR, değiştirilmedi) A1-A8 kurallarıyla `tools/*.py` araçlarının ajan-arayüzünü standardize eder (--json/--sessiz/--kuru/--repo bayrakları, çıkış kodu sözlüğü 0/1/2/3/4/6).
- **Pointer:** `tools/hareket-tablo.py:1-15`; `tools/AXI-STANDARDI.md:1-27` (tam dosya, salt-okur okundu).
- **Kanıt:** `veri/bronz/hareket-olay.jsonl` **5163 satır** (birebir ölçülmüş); AXI uyum envanteri (08-29 AS-OF): `tools/*.py` toplam **43**, `--json` olan **8**, `--sessiz` olan **30** (dosya içi ölçüm satırı, kaynaklı).
- **Taşıma-maliyeti:** (1) bronz kaynağı Claude Code'un kendi transkript formatına (~/.claude/projects) bağlı, başka araç sağlayıcıya taşınmaz; (2) silver katman `veri/baglam.sqlite` + sözleşme dosyası (`veri/sozlesme/hareket.json`) beraber taşınmalı; (3) AXI standardı 43 script'in yalnız 8'inde tam uygulanmış, geri kalanı ürün için tamamlanmalı; (4) insan-yüzü günlük (`raporlar/hareket-gunlugu-*.md`) Türkçe + JARVIS-terminolojili, i18n gerekir.

## Özet tablo

| Aday | Mekanizma (özet) | Repo-pointer | Çalışma-kanıtı | Taşıma-maliyeti (madde) |
|---|---|---|---|---|
| ① nested-loop koşucusu | stream-json canlı izleme | `tools/gnhf-izle.py:1-30` | e600a7: 3M tavan, 3/3 iterasyon 0 arıza | 4 |
| ② paralel-kapı+manifest | Bernstein çift-testi + dalga planı | `tools/paralel-kapi.py:1-15`, `veri/manifest/*.json` (17) | 8 birim/28 çift, N=1→3, çakışma 0 | 4 |
| ③ karar-masası deseni | Lavish kart+queueKey+açıklama-bloğu | `kuyruk/arsiv/senaryo-defteri-arsiv-2026-08-29.md:41` | 7 karttan 5'i tek turda hükme bağlandı | 4 |
| ④ A1-A4 kanıt-kapılı merdiven | 4 kapı, koşum-sayılı eşik, Salih GO | `kuyruk/k010-zincir-2026-08-29.md:1-56` | A1 5/5, A2 tamam, A3 2/3, A4 bekliyor | 4 |
| ⑤ gnhf-izle izleyici bileşeni | worktree keşfi+tail-f, LLM yok | `tools/gnhf-izle.py:20-52` | ①'deki koşum raporlarında kullanım izi; ayrı test yok `[?]` | 4 |
| ⑥ repo-freni (policy-as-code) | settings deny/ask + PreToolUse regex hook | `.claude/settings.json`, `.claude/hooks/pretool-core-tel.sh` | PASS vakası rapor referanslı, bu koşumda doğrulanmadı `[?]` | 4 |
| ⑦ hareket kütüğü+AXI | transkript→bronz/silver/gold + araç standardı | `tools/hareket-tablo.py:1-15`, `tools/AXI-STANDARDI.md` (tam) | 5163 satır bronz; AXI 43 script/8 --json | 4 |
