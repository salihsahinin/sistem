# Homebase → JARVIS Taşıma Tespiti — 2026-07-15 (Salih emri: "taşınması gerekenleri tespit et")

> **Açıklama notu:** Tespit raporudur — taşıma İCRASI Salih onayı bekler (Katman 1'e yakın: kanon-yerleşimi kararı). Yöntem: kopyala + Homebase'te yerine tek satır pointer bırak ("JARVIS'e taşındı → yol"); silme yok (m.8). Homebase bu oturumda mount'landı, tam dosya listesi tarandı.

## A — TAŞINMALI (JARVIS'in aktif işine doğrudan girdi)
| # | Homebase dosyası | Hedef | Gerekçe |
|---|---|---|---|
| 1 | `[C] Loop Engineering.md` (wiki) | `wiki/loop-engineering.md` | K-015 madde-3'ün wiki sayfası; Faz 2/4 kapanış satırları buraya işlenecek. Wiki'nin ana rolü JARVIS'te (#5) |
| 2 | `[C] Loop Engineering — Yol Haritası.md` | `ogrenme/loop-eng-yol-haritasi.md` | Faz 2+4 aktif iş planı (Faz 0-1 DONE kayıtlı); öğrenme şeridinin ilk hazır müfredat parçası — Atlas müfredatıyla birleşir |
| 3 | `[C] Loop Engineering — Sonrası.md` (backlog, 8 madde) | `kuyruk/loop-eng-backlog.md` | Backlog kuralı ("3 aktif madde bitmeden açılmaz") kuyruk disipliniyle aynı; K-009 gündemine komşu |
| 4 | `[C] Looplara Baslangic — Blog Transkripti (TR).md` | `ogrenme/kaynaklar/` | Faz 0'ın kaynak metni; öğrenme oturumlarının kaynak-arşivi başlangıcı |
| 5 | `[C] Sondevir Paketi - Anlama Kapisi.md` | `ogrenme/anlama-kapisi.md` | Öğretme deseninin tanım belgesi — `ogrenme/README.md` protokolünün kaynağı; şeridin yanında yaşamalı |
| 6 | `[C] Orca — LLM Wiki.md` | `wiki/orca.md` | Orca = K-009 tetik-mekanizması adayı (K-017/E1); karar öncesi dış-araştırma zemini (m.40b) |
| 7 | `[C] Utopik Jarvis - Fikir ve Proje Havuzu.md` | `kuyruk/utopik-havuz.md` | V29 vizyon havuzu; loop-eng wiki'si #14/#24/#25'e atıf yapıyor — atıf zinciri JARVIS içinde kapanmalı. K-019 damıtma vardiyasında fikir-kutusuyla ilişkisi netleşir |
| 8 | `[C] Jarvis Ingest Defteri.md` | `kuyruk/arsiv-ingest-defteri-homebase.md` | İngest şeması v1 zaten DONE (07-12); defter tarihçe değeri taşır — arşiv-değerli taşıma |
| 9 | `[C] Carvis Sozlugu.md` | `wiki/sozluk.md` — **süpürme şartlı** | Sözlük kanonu wiki'ye; taşınırken 07-13 bağlam-hijyeni süpürmesinden geçirilir (biyoloji-kökenli terim varsa nötr forma) |
| 10 | `LLM Wiki Starter/00 LLM Wiki — original idea (Karpathy).md` | `wiki/kokenler-karpathy-llm-wiki.md` | Wiki standardının köken belgesi; köken-izi disipliniyle uyumlu |

## B — KALIR (Homebase kanonu ayrı yaşar)
- **01 Daily Logs/** — m.23 (günlük-özüt kullanımı yasak); JARVIS'e taşınması zaten yasaklı sınıf.
- **Kendini-Analiz hattı + Kişiselleştirme profilleri** — chat/kişisel yüzeyin işi; K-014 süreci profilleri zaten oradan yönetiyor.
- **02 Projects/07 LOBİ/** — ayrı proje, kendi CLAUDE.md/tüzüğü var.
- **MİDAS dosyaları (v5-v7 + analizler)** — finans şeridi; PortRisk ölçüm-bankı açılınca pointer yeterli, kopya gereksiz.
- **Devir paketleri, korpus, kılavuzlar, staj/kariyer dosyaları** — Homebase tarihçesi/bağımsız işler.
- `[C] JARVIS Cep Kapsulu 2026-07-10.md` — bayat (JARVIS'te 07-11 sürümü var); Homebase'te arşive inmeli, taşınmaz.

## C — YAN TESPİTLER (taşıma değil, not)
1. **portrisk çift kopya riski:** Homebase içinde `02 Projects/04 .../portrisk/` (venv'li, ~450MB'ın ana yükü) VAR; paralel-vardiya talimatı ise `C:\Users\sasah\dev\portrisk`'i işaret ediyor. Hangisi canlı? K-002 açılmadan netleşmeli — yanlış kopyada çalışmak commit tarihçesini böler.
2. **Homebase CLAUDE.md kadans bölümü bayat** (bilinen borç, JARVIS CLAUDE.md'de kayıtlı); taşıma icrasında taşınan her dosyanın yerine pointer + CLAUDE.md'ye tek satır "loop-eng/wiki hattı JARVIS'e taşındı" notu düşülmeli.
3. **Envanter (K-015 icra notu, 07-15):** CC 2.1.209 (native, win32-x64), doctor temiz, auto-update açık, **Remote Control mevcut** (`claude.ai/code` + mobil — K-018'in ilk kurulum maddesi fiilen hazır). `/effort` ayrı komutu doğrulanmadı; efor seçimi /model menüsünden (Salih koşumu bunu teyit etti: "opus high").

## İcra önerisi (onay beklerim)
Tek vardiyalık iş (~30 dk): A listesi kopyalanır → 9 no'lu süpürmeden geçer → Homebase'e pointer'lar yazılır → JARVIS'te commit/push. K-021 müfredat damıtmasından ÖNCE yapılırsa Atlas raporu + loop-eng haritası tek müfredatta birleştirilebilir.
