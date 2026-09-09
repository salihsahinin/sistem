# KILAVUZ — Kun Chen L8 Yığınının BİREBİR KOPYASI: Kurulum + Diyaloglu Kullanım Senaryoları

> **İNGEST EDİLDİ · 2026-08-21 (İB-02 triyajı — bu şerhle birlikte okunur):** (1) **Kurulum katmanı (§0-3) SÜPERSEDE** — rapor Windows/WSL2 zemininde yazıldı; 08-12 L8 **Mac** geçişi (envanter 11/11 CANLI, Karar 35; KB-16: Windows klonu TERK) fiilî kurulumu Mac'te yaptı — kurulum kaydı `raporlar/vardiya-teslim-2026-08-12-l8-mac.md`. Config metinleri (tmux.conf/wezterm.lua) referans değerini korur. (2) **Kullanım katmanı (§4 S1-S15 + §5 kalıplar + §6 ritim) CANLI** — platform-bağımsız; entegrasyon-masası hazırlık dosyasının (KB-22/KB-29 borcu) ana malzemesi. (3) §7 `[?]` listesinin çoğu Mac kurulumuyla fiilen çözüldü; AGENTS symlink sorusu Karar 47 ile çözüldü (CC AGENTS.md tüketmiyor — statik levha; symlink/bakım tetiği = Codex girişi); telefon-SSH hâlâ açık. Dosya bronz kaynak olarak yerinde kalır (m.8).

*Salih emri (2026-08-05): **"birebir kopyalayacağız" — Kun Chen'in araçları VE arayüzleri kopyalanacak.** Bu rapor o emrin zemini üzerine yazıldı; alternatif/ikame tartışması açılmaz.*
*Kaynak: `raporlar/kaynak-L8-agentic-workflow-transkript.md` (video, zaman damgalı) + `cc/rapor-2026-08-03-4.md` §II.1 birincil-kaynak künyesi `[D-belge]` + P1/P2/P3/P6 saha kayıtları.*
*`[?]` = birincil kaynakta doğrulanmadı, ilk koşumda `--help`/README ile teyit edilir (m.39). Rakamlar `[deneysel m.29]`.*

---

## 0. Ne kopyalanıyor — tam liste

Videodaki 12 bileşenin **tamamı**, sırasıyla:

| # | Bileşen | Video sahnesi | Rolü |
|---|---|---|---|
| 1 | **WezTerm** | 3:49 | terminal emülatörü — her platformda aynı pencere |
| 2 | **tmux** | 5:09 | pano/sekme + **oturum kalıcılığı** (telefondan aynı oturuma bağlanma) |
| 3 | **Neovim** | 7:18 | klavye-odaklı editör |
| 4 | **4 harness** (Claude Code · Codex CLI · Pi · OpenCode) | 9:21 | ajan koşum ortamları |
| 5 | **Global + proje hafıza dosyası** (symlink'li) | 11:24 / 14:50 | tayfanın eğitimi |
| 6 | **npx skills + skill-creator** | 16:12 | koşullu talimatı bağlamdan çıkarma |
| 7 | **Ses girişi** (yerel whisper + initial-prompt sözlüğü) | 20:27 / 41:41 | ~3× hızlı giriş |
| 8 | **AXI** (github-axi, chrome-devtools-axi) | 22:12 | ajan-ergonomik araçlar; MCP yerine |
| 9 | **lavish** | 24:25 | etkileşimli plan artefaktı |
| 10 | **no-mistakes** | 28:29 | doğrulama boru hattı → PR |
| 11 | **gnhf** | 33:12 | durma-koşullu uzun koşum |
| 12 | **treehouse** | 36:20 | worktree havuzu |
| 13 | **firstmate** | 40:23 | birinci kaptan — tek muhatap |

**Zemin kararı (birebir kopyanın gereği):** Kun Chen'in düzeni POSIX + tmux üzerine kurulu; firstmate'in kendi belgesi de POSIX + tmux varsayıyor `[D-belge]`. Windows 11'de bu düzenin **birebir** karşılığı **WSL2 / Ubuntu**'dur — orada tmux gerçek tmux, firstmate native koşar, PR beklemeye gerek kalmaz. WezTerm Windows tarafında kalır ve WSL'e bağlanır; yani **pencere Windows'ta, gemi Linux'ta.**

Bugün Windows tarafında zaten kurulu olanlar (treehouse · gnhf · no-mistakes · lavish, P1-P2-P3'ten) **silinmez** (m.8) — deneme deposuyla birlikte oldukları yerde kalır; birebir yığın WSL2 içinde ikinci kez, tam sürümüyle kurulur.

---

## 1. Kurulum sırası

*Her adımın sonunda "bunu görürsen tamam" satırı var. Adımlar sırayla koşulur; bir adım yeşil olmadan sonrakine geçilmez.*

### K0 · Zemin — WSL2 Ubuntu
```powershell
# Windows PowerShell (yönetici)
wsl --install -d Ubuntu-24.04
wsl --set-default-version 2
wsl --list --verbose            # Ubuntu · Running · 2
```
```bash
# Ubuntu içinde
sudo apt update && sudo apt install -y build-essential git curl unzip ripgrep fd-find
git config --global user.name "salihsahinin"
git config --global user.email "salih.sahinin@gmail.com"
```
✅ **Tamam işareti:** `wsl -l -v` çıktısında Ubuntu VERSION=2.

### K1 · WezTerm (Windows tarafı)
```powershell
winget install wez.wezterm
```
Config: `C:\Users\sasah\.wezterm.lua` (§3.1'de tam metin).
✅ **Tamam:** WezTerm açılıyor ve **doğrudan WSL/Ubuntu shell'ine** düşüyor; config'de renk şemasını değiştirince **anında** yeniden yükleniyor (videodaki hot-reload davranışı, 5:00).

### K2 · tmux
```bash
sudo apt install -y tmux
```
Config: `~/.tmux.conf` (§3.2'de tam metin).
✅ **Tamam:** `tmux new -s ana` → üstte durum çubuğu; `prefix + d` ile ayrıl, `tmux attach -t ana` ile **aynı yere** dön.

### K3 · Neovim
```bash
sudo apt install -y neovim
git clone https://github.com/LazyVim/starter ~/.config/nvim
rm -rf ~/.config/nvim/.git
```
✅ **Tamam:** `nvim` açılıyor; `<Space>s` grep, `<Space>f` dosya bulma çalışıyor (videodaki iki kısayol, 8:38-8:48). Göreli satır numarası açık (§3.3).

### K4 · Harness'ler (dördü de)
```bash
# Claude Code
npm install -g @anthropic-ai/claude-code        # [?] paket adı kurulumda teyit
# Codex CLI
npm install -g @openai/codex                    # [?]
# OpenCode
curl -fsSL https://opencode.ai/install | bash   # [?]
# Pi
# kurulum satırı repo README'sinden alınır      # [?]
```
✅ **Tamam:** dördü de `--version` veriyor. Video düzeni: günlük iş Claude Code'da, ama **hiçbir talimat tek harness'e yazılmaz** (agent-agnostic ilkesi, 11:01).

### K5 · Hafıza dosyaları + symlink
```bash
mkdir -p ~/.claude ~/.agents
nvim ~/.claude/CLAUDE.md                 # global hafıza — 27 satır hedefi
ln -s ~/.claude/CLAUDE.md ~/.agents/AGENTS.md      # [?] diğer harness'lerin beklediği yol teyit edilir
# proje içinde:
cd ~/dev/portrisk && nvim CLAUDE.md && ln -s CLAUDE.md AGENTS.md
```
**Global dosyaya giren üç kural (videodan birebir, 12:49 / 14:09):**
```markdown
- Never use em dashes.
- When making technical decisions, don't give too much weight to development cost.
  (Models overestimate human dev time; this biases toward cheap, low-quality options.)
- When fixing bugs, always start by reproducing the bug end-to-end, as close to how
  an end user experiences it as possible. Unit tests alone are not sufficient.
```
✅ **Tamam:** `ls -l ~/.agents/AGENTS.md` symlink'i gösteriyor; global dosya ≤27 satır.

### K6 · Skills
```bash
npx skills add anthropics/skills --skill skill-creator     # [?] kaynak yolu teyit
npx skills list
```
✅ **Tamam:** `npx skills list` skill-creator'ı gösteriyor; ajana "bunu skill'e çıkar" dediğinde nasıl yapacağını biliyor.

### K7 · Ses girişi + terim sözlüğü
Video'nun aracı **OpenSuperWhisper** yalnız macOS'ta koşuyor `[D-belge]`. Arayüz birebir korunur (bas-konuş → yerel transkripsiyon → imlece yazım → **initial prompt ile sözcük dağarcığı**); Windows'ta bunu veren yerel-whisper uygulaması kurulur:
```powershell
# aday: WhisperWriter (yerel faster-whisper, kısayol tuşu, initial prompt alanı)  [?]
# aday: whisper.cpp + AutoHotkey kısayolu                                          [?]
```
**Sözcük dağarcığı alanına yazılacak liste (41:49'daki hile, bizim adlarımızla):**
```
JARVIS, Carvis, Salih, PortRisk, treehouse, gnhf, no-mistakes, lavish, firstmate,
AXI, WezTerm, tmux, Neovim, kapsül, pano, tüzük, vardiya, senaryo defteri, Otonet
```
✅ **Tamam:** "gnhf koşumunu başlat" dediğinde transkripsiyon **gnhf** yazıyor, "genef" değil.
⚠️ Kural (21:56): URL ve dosya yolu **yazılır**, söylenmez.

### K8 · AXI araçları
```bash
# katalog: https://axi.md  → github-axi ve chrome-devtools-axi kurulum satırları oradan  [?]
```
**Kural (24:02):** ajana araç verirken önce verimliliğine bak. Ölçüm `[D-belge]`: 425 koşum / 17 görev — *AXI %100 başarı @ $0,050/görev · CLI %86 @ $0,054 · MCP %82-87 @ $0,101-0,148.*
✅ **Tamam:** GitHub işleri MCP'den değil, AXI/CLI'dan geçiyor.

### K9 · lavish
```bash
npx skills add kunchenguid/lavish-axi --skill lavish
npx -y lavish-axi setup hooks
```
✅ **Tamam:** ajanda `/lavish` çalışıyor, tarayıcıda sayfa açılıyor.
⛔ `lavish-axi share` = public yayın — deny kilidi canlı (m.14/md.49); yayın gerekirse **sen** `--password` ile koşarsın.

### K10 · no-mistakes
```bash
curl -fsSL https://kunchenguid.github.io/no-mistakes/install.sh | sh    # [?] Linux satırı teyit
export NO_MISTAKES_TELEMETRY=0        # ~/.bashrc'ye — KURULUMDAN ÖNCE
no-mistakes doctor
```
✅ **Tamam:** `doctor` tam yeşil (git · gh · runner); `git remote -v` içinde `no-mistakes` hedefi görünüyor.

### K11 · gnhf
```bash
npm install -g gnhf
export GNHF_TELEMETRY=0               # ~/.bashrc'ye
gnhf --help                           # flag adlarını buradan sabitle
```
✅ **Tamam:** `--help` çıktısında durma koşulu ve tavan flag'leri görünüyor.
⚠️ Kalibrasyon (P1 ölçümü): token sayacı **cache okumalarını da sayıyor** — 150K tavan iş başlamadan doluyor. Tavanı **milyon bandında** tut.

### K12 · treehouse
```bash
curl -fsSL https://kunchenguid.github.io/treehouse/install.sh | sh     # [?] Linux satırı teyit
treehouse status
```
✅ **Tamam:** `treehouse` seni taze worktree'ye bırakıyor, `exit` ile havuza dönüyor.

### K13 · firstmate
```bash
cd ~/dev
git clone https://github.com/kunchenguid/firstmate
cd firstmate
claude                                # firstmate'i harness içinde koşarsın
```
İlk açılışta kurulum diyaloğu gelir (§4 S6). Komutları: `/ahoy` · `/bearings` · `/afk` · `/stow` · `/updatefirstmate`. Modları: `no-mistakes` (tam kapı) · `direct-PR` · `local-only` (+`yolo`). Durum: `state/<id>` append-only olay log'u + `data/captain.md` + `data/learnings.md`. Sessiz denetim: `bin/fm-watch.sh` `[D-belge]`.
✅ **Tamam:** firstmate tek cümlelik işi alıp **kendisi** tmux sekmesi açıyor, treehouse çağırıyor, ajan koşuyor.

---

## 2. Arayüz kopyası (config'ler)

### 2.1 `~/.wezterm.lua` (Windows tarafı)
```lua
local wezterm = require 'wezterm'
local config = wezterm.config_builder()

config.default_domain = { DomainName = 'WSL:Ubuntu-24.04' }   -- doğrudan gemiye düş
config.color_scheme = 'rose-pine-moon'                        -- videodaki şema (5:04)
config.font = wezterm.font 'JetBrains Mono'
config.font_size = 12.0
config.enable_tab_bar = false        -- sekmeleri tmux yönetir, WezTerm değil
config.window_padding = { left = 6, right = 6, top = 6, bottom = 0 }
config.window_close_confirmation = 'NeverPrompt'

return config
```
*Not (4:34): dosya Lua olduğu için koşullu/dinamik yazılabilir; kaydettiğin an hot-reload olur.*

### 2.2 `~/.tmux.conf`
```bash
set -g prefix C-a                  # Ctrl-a (Ctrl-b'den daha erişilebilir)
unbind C-b
bind C-a send-prefix

set -g mouse on
set -g base-index 1
setw -g pane-base-index 1
set -g renumber-windows on
set -g history-limit 50000
set -s escape-time 0
set -g default-terminal "tmux-256color"

# bölme — görsel tuşlar
bind | split-window -h -c "#{pane_current_path}"
bind - split-window -v -c "#{pane_current_path}"

# pano gezinme — vim yönü
bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R

# durum çubuğu — hangi sekmede ne var
set -g status-position top
set -g status-style "bg=default,fg=white"
set -g status-left "#[bold] #S "
set -g status-right " %H:%M "
setw -g window-status-current-format "#[reverse] #I:#W "
setw -g window-status-format " #I:#W "

bind r source-file ~/.tmux.conf \; display "config yeniden yüklendi"
```

**tmux tuş kartı (ezberlenecek 8 tuş):**

| Tuş | Ne yapar |
|---|---|
| `C-a \|` | panoyu dikey böl |
| `C-a -` | panoyu yatay böl |
| `C-a h/j/k/l` | panolar arası geç |
| `C-a c` | yeni sekme (window) |
| `C-a 1..9` | sekmeye atla |
| `C-a n` / `C-a p` | sonraki / önceki sekme |
| `C-a d` | oturumdan ayrıl (oturum yaşamaya devam eder) |
| `C-a [` | kaydırma/kopyalama modu (`q` ile çık) |

### 2.3 Neovim — videodaki iki davranış
`~/.config/nvim/lua/config/options.lua`:
```lua
vim.opt.number = true
vim.opt.relativenumber = true      -- 8:03'teki göreli satır numarası: "11k" ile 11 satır yukarı
```
Kısayollar LazyVim'de hazır gelir: `<Space>s` grep · `<Space>f` dosya bulma · `dd` satır sil · `u` geri al · `:q` çıkış.

---

## 3. Standart ekran düzeni

Her iş için aynı düzen (5:41'deki üçlü):

```
┌──────────────────────── tmux: sekme 1 "ana" ───────────────────────┐
│                          │                                        │
│   PANO A                 │   PANO B                               │
│   ajan (claude)          │   nvim / kod                           │
│                          │                                        │
│                          ├────────────────────────────────────────┤
│                          │   PANO C — serbest kabuk               │
│                          │   (git, treehouse status, log)         │
└────────────────────────────────────────────────────────────────────┘
sekme 2 = 2. iş · sekme 3 = 3. iş · sekme 0 = firstmate
```
Kurulum komutu (bir kez yazılır, sonra ezberdedir):
```bash
tmux new -s ana        # C-a |   ile böl,  C-a -  ile alt panoyu aç
```

---

## 4. KULLANIM SENARYOLARI (diyaloglu)

*Biçim: **▸ nerede** → **ne yazacaksın (birebir)** → **ne göreceksin** → **sonra ne diyeceksin**.*
*Ses simgesi 🎙 = konuşarak verilir. Klavye simgesi ⌨ = yazılarak (URL/yol içeriyorsa her zaman ⌨).*

---

### S1 · Sabah — gemiye biniş
**Durum:** güne başlıyorsun.

▸ **WezTerm'i aç.** Doğrudan Ubuntu shell'ine düşer.
```bash
tmux attach -t ana || tmux new -s ana
```
**Göreceğin:** dün bıraktığın panolar, çalışan ajanlar, yarım kalan çıktılar — hiçbiri kaybolmamış (6:06 kalıcılık).

▸ **Sekme 0'a geç** (`C-a 0`) — firstmate orada duruyor.
> 🎙 **Sen:** "Ahoy. Dün gece neler oldu, nerede kaldık, bugün ne var?"
> **firstmate:** dün biten koşumlar, açık PR'lar, bekleyen kararlar listesi.
> 🎙 **Sen:** "Önce PR'ları kapatalım, sonra yeni işleri dağıtırız."

*(firstmate açık değilse: `cd ~/dev/firstmate && claude` → `/ahoy`)*

---

### S2 · Belirsiz bir iş — plan turu (lavish)
**Durum:** PortRisk'te "risk paneli" istiyorsun ama nasıl görüneceği belli değil.

▸ **Sekme 1, PANO A:**
```bash
cd ~/dev/portrisk
treehouse                       # taze worktree'ye düşer
claude
```
> 🎙 **Sen:** "Portföy sayfasına bir risk paneli eklemek istiyorum. Volatilite, maksimum düşüş ve konsantrasyon riskini göstersin. Üç farklı tasarım seçeneği çıkar ve tartışalım."
>
> **Ajan:** *(lavish skill'i kurulu olduğu için otomatik lavish'e gider — video 25:53'te tersini yapmak için "don't use lavish" demek zorunda kaldı)*
> `Launching lavish editor…` → tarayıcıda sayfa açılır.

▸ **Tarayıcıda:** üç seçenek, projenin kendi tasarım diliyle çizilmiş. Kararı burada verirsin:
- 2. seçeneğin başlığına tıkla → not düş: *"bu doğru ama düşüş grafiği çok baskın"*
- 3. seçenekte "konsantrasyon" kartını işaretle → *"bunu 2'ye taşı"*
- Alttaki karar düğmelerinden **"Seçenek 2 + konsantrasyon kartı"** butonuna bas.

▸ **PANO A'ya dön** — geri bildirim ajana ulaşmıştır.
> **Ajan:** "Anladım — seçenek 2 tabanı, konsantrasyon kartı eklendi, düşüş grafiği ikincil. Planı güncelledim."
> 🎙 **Sen:** "Tamam, inşaata başla. Bitince no-mistakes koştur."

▸ **Sen artık buradan çıkarsın.** `C-a c` ile yeni sekme aç, başka işe geç.

---

### S3 · Hata düzeltme (global hafıza kuralının devreye girdiği yer)
**Durum:** "getiri hesabı yanlış" diye bir şikâyet var.

▸ **Sekme 2, PANO A:**
```bash
cd ~/dev/portrisk && treehouse && claude
```
> 🎙 **Sen:** "Aylık getiri tablosunda Şubat satırı yanlış çıkıyor. Önce hatayı uçtan uca yeniden üret, sonra düzelt."
>
> **Ajan:** *(global hafızadaki e2e kuralı zaten yüklü — 14:09)* "Uçtan uca senaryoyla yeniden ürettim: 2026-02 için beklenen %2,4, gelen %0,0. Kök neden: ay sonu tarihinde takvim günü kayması."
> 🎙 **Sen:** "Düzelt ve aynı senaryoyu regresyon testi olarak bırak."
> **Ajan:** "Düzeltildi, test eklendi, ikisi de yeşil."
> ⌨ **Sen:** `git push no-mistakes`

**Sonra:** hattı bekleme. Başka sekmeye geç. Hat bitince PR'a bakarsın (S8).

---

### S4 · Üç iş aynı anda (treehouse + tmux sekmeleri)
**Durum:** üç bağımsız küçük iş var.

▸ **Sekme 2:** `C-a c` → `cd ~/dev/portrisk && treehouse && claude`
> 🎙 "Getiri tablosundaki Şubat hatasını düzelt, uçtan uca yeniden üreterek başla. Bitince no-mistakes koştur."

▸ **Sekme 3:** `C-a c` → `cd ~/dev/portrisk && treehouse && claude`
> 🎙 "CSV dışa aktarma butonuna tarih aralığı seçici ekle. Bitince no-mistakes koştur."

▸ **Sekme 4:** `C-a c` → `cd ~/dev/portrisk && treehouse && claude`
> 🎙 "README'deki kurulum adımları bayat, gerçek adımlarla güncelle. Bitince no-mistakes koştur."

▸ **Kontrol — PANO C:**
```bash
treehouse status
```
```
1  ~/.treehouse/portrisk-4a1f/1   IN USE   (pid 20114)
2  ~/.treehouse/portrisk-4a1f/2   IN USE   (pid 20390)
3  ~/.treehouse/portrisk-4a1f/3   IN USE   (pid 20655)
4  ~/.treehouse/portrisk-4a1f/4   IDLE
```
**Kural (36:44):** aynı klasörde iki ajan koşturma. Her iş kendi worktree'sinde.
**Kim seni istiyor:** üst durum çubuğuna bak; sekme adı yanıp sönen iş dikkat istiyor. `C-a n` / `C-a 2` ile geç.
**Bitince:** sekmeyi kapat (`exit`) → treehouse kopyayı havuza iade eder, bir dahakine yeniden kullanır (38:37).

---

### S5 · Gece koşumu (gnhf)
**Durum:** yatacaksın, 7-8 saat boş.

▸ **Sekme 5, temiz repo şart:**
```bash
cd ~/dev/portrisk
git status                   # temiz olmalı; değilse commit/stash
gnhf --help                  # flag adlarını ilk seferde sabitle  [?]
```
▸ **Koşumu başlat** (üç şey zorunlu: hedef · durma koşulu · tavan):
```bash
gnhf "PortRisk'in uçtan uca test kapsamını yükselt. Her turda kapsamı ölç, \
en zayıf modülü seç, test yaz, testleri koştur, yeşilse commit at." \
  --stop-when "uçtan uca kapsam %80'in üstüne çıktı" \
  --max-iterations 25 \
  --max-tokens 3000000              # [?] flag adları --help ile teyit
```
**Göreceğin:** iterasyonlar ay simgeleriyle akar; token sayacı ve commit sayısı üstte (35:06).

▸ **Sabah — PANO C:**
```bash
git log --oneline gnhf/<dal>        # gece atılan commit'ler
cat .gnhf/runs/<id>/gnhf.log | tail -5
python /mnt/c/JARVIS/tools/olcum-dortlu.py --append --repo ~/dev/portrisk
```
**Kararı sen verirsin:** hangi commit kalır, hangisi düşer (35:21).

**Ne zaman gnhf DEĞİL:** durma koşulu yazılamayan hedefler. "Kodu güzelleştir" bir gnhf hedefi değildir; "kapsamı %80'e çıkar", "sayfa yükleme süresini 400ms altına indir", "7 yaşında bir çocuk gibi kullan, ilk takıldığın yeri bul-düzelt-tekrarla" gnhf hedefidir (34:36).

---

### S6 · firstmate — tek muhatap düzeni
**Durum:** artık sekmeleri sen açmayacaksın.

▸ **Sekme 0 · ilk kurulum:**
```bash
cd ~/dev/firstmate && claude
```
> 🎙 **Sen:** "PortRisk, JARVIS araçları ve staj projesi üzerinde çalışacağız."
> **firstmate:** "Kurulum: bu depolardaki kod değişikliklerinde ne kadar katı olayım? (full gates to PR / direct-PR / local-only)"
> 🎙 **Sen:** "**Full gates to PR.**" *(= her değişiklik no-mistakes hattından geçer — 42:10)*
> **firstmate:** "Anlaşıldı. İlk iş?"

▸ **Tek cümlelik iş ver (videodaki kalıp, 42:29):**
> 🎙 **Sen:** "Üç projenin de CLI'sına, kendini npm'deki son sürüme güncelleyen bir `update` komutu ekle."
>
> **firstmate:** "Bu üç paralel iş. Sekmeleri açıyorum, her biri için treehouse worktree'si alıyorum, ajanları koşturuyorum, sonra no-mistakes ile PR'ları hazırlayacağım."
> *(tmux sekmeleri kendiliğinden açılır — sen hiçbir şey yapmazsın)*

▸ **Beklerken ikinci konuyu aç (43:13'teki hamle):**
> 🎙 **Sen:** "Bu arada PortRisk'in son üç açık issue'suna bak, hangisi yapılabilir tartışalım."
> **firstmate:** "#87 en temiz — açık bir hata, tek dosyada. #91 tasarım kararı istiyor. #93 bayat."
> 🎙 **Sen:** "87'yi de al."

▸ **Uzaklaşırken:**
> ⌨ `/afk` — "gidiyorum, kendi başına ilerle"
> ⌨ `/bearings` — "durum nedir" (döndüğünde ilk komut)
> ⌨ `/stow` — işi güvenle park et
> ⌨ `/updatefirstmate` — kendini güncelle

**Durum sözlüğü:** firstmate her tayfa için `busy` / `idle` / `unknown` / `dead` verdiği verir; **`unknown` asla otomatik terfi etmez** — bilinmeyen durum iyi sayılmaz `[D-belge]`. (Bizdeki m.42(d) katı-başlangıç ilkesiyle aynı davranış.)

---

### S7 · Hafızayı hatadan büyütmek (15:49'un birebir uygulaması)
**Durum:** ajan aynı hatayı ikinci kez yaptı.

▸ **Hangi sekmedeysen, o anda:**
> 🎙 **Sen:** "Yine testleri `pytest` ile koşturdun; bu projede `make test` kullanıyoruz. Bunu düzelt ve **proje hafıza dosyasına yaz** ki bir daha aynı hatayı yapma."
> **Ajan:** "CLAUDE.md'ye ekledim: *Test komutu `make test`; doğrudan pytest çağrılmaz (ortam değişkenleri Makefile'da set ediliyor).*"

**Kural:** proje hafıza dosyası elle yazılmaz, **hatadan büyür**. Video'nun kendi cümlesi: *"You don't need any fancy memory system to do that. This markdown file is all it takes"* (16:08).

**Global dosyaya ne girer, projeye ne girer:**

| Global (`~/.claude/CLAUDE.md`, ≤27 satır) | Proje (`<repo>/CLAUDE.md`, uzun olabilir) |
|---|---|
| kişisel üslup tercihleri | repo düzeni, terminoloji |
| karar yanlılığı düzeltmeleri | önemli bileşenler nasıl çalışır |
| her projede geçerli çalışma kuralları | uçtan uca test nasıl koşulur, konvansiyonlar |

---

### S8 · Hafıza şişince skill'e çıkarmak (16:47'nin birebir diyaloğu)
**Durum:** proje hafıza dosyası büyüdü; içindeki e2e test talimatı her oturumda boşuna token yakıyor.

> 🎙 **Sen:** "AGENTS dosyamızdaki uçtan uca test talimatlarını proje seviyesinde bir skill'e çıkar."
> **Ajan:** *(skill-creator kurulu olduğu için nasıl yapacağını bilir)* "Talimatları `.claude/skills/e2e-testing/SKILL.md` dosyasına taşıdım, hafıza dosyasından çıkardım. Açıklama alanı: *'PortRisk'te uçtan uca test koşmak ve yazmak için — kod değişikliği doğrulanırken kullanılır.'*"

**Neden işe yarıyor (18:05):** ajan açılışta yalnız o tek satırlık açıklamayı yükler; gövdeyi ancak gerçekten test koşacağı zaman okur. Soru sorduğunda test talimatları bağlamda yer kaplamaz.

**Skill kurma disiplini (18:40-20:27 + bizim yıldız yasağımız):** internetten skill kurmadan önce SKILL.md okunur; yıldız sayısı ölçüt değildir; ölçülmemiş "ajanını sihirli şekilde iyileştirir" iddiaları alınmaz.

---

### S9 · PR'ı incelemek — risk etiketine göre (32:42)
**Durum:** no-mistakes "tüm kontroller geçti" dedi.

▸ **PANO C:**
```bash
gh pr view --web            # ya da firstmate'e: "PR'ı aç"
```
**PR gövdesinde göreceğin bölümler:** asıl niyet · ne değişti · nasıl test edildi · hat sırasında ne oldu · **kanıt artefaktı** (ekran görüntüsü / log / video) · **risk değerlendirmesi**.

**Karar kuralı:**

| Risk | Ne yaparsın |
|---|---|
| Düşük | Diff'e **bakmazsın**. Kanıta bak, merge et. |
| Orta | Yalnız hattın işaretlediği dosyalara bak. |
| Yüksek | Diff'i okursun; gerekirse ajana dönersin. |

> 🎙 **Sen (ajana, merge öncesi):** "Hattın kendi düzelttiği üç şeyi gördüm; ikincisi istediğim davranış değil. Şunu şöyle değiştir, sonra tekrar hattan geçir."

**Sahada ölçülen (P2, `[deneysel m.29]`):** hat başına ~[7-20 dk bandı] duvar-saati; koşum-1'de eksik testi **hat kendisi yazdı**, koşum-2'de niyet-test çelişkisinde **durup sordu**.

---

### S10 · Hat sana soru sorduğunda (eskalasyon)
**Durum:** TUI'de `ask-user` düştü.

▸ **no-mistakes TUI'sinde:**
```
🚨 Review + Test: intent conflicts with test contract.
   The change makes empty input return None, but tests assert 0.
   This is a product decision — it will not be silently patched.
   [approve] [fix] [skip]
```
> 🎙 **Sen:** "Boş girdi None dönmeli, doğru davranış bu. Testleri yeni sözleşmeye göre güncelle ve PR gövdesine bunu davranış değişikliği olarak yaz."
> ⌨ `fix` seç.

**Bu iyi haberdir:** hattın çalıştığının kanıtı. Mekanik eksiği kendi tamamlar; **niyete dokunan şeyi sana getirir.** (Bizdeki m.31 Katman-1/Katman-2 ayrımının makine karşılığı.)

---

### S11 · Araç ergonomisi — MCP yerine AXI/CLI (22:12)
**Durum:** ajan GitHub'a erişecek.

▸ **Kurulum kararı, bir kez:** GitHub MCP sunucusu **kullanılmaz**; `gh` CLI + github-axi kullanılır.
**Gerekçe rakamı `[D-belge]`:** aynı iş MCP'de ~3× token + 2× gecikme; AXI ölçümü 425 koşum / 17 görev üzerinden %100 başarı @ $0,050 ↔ MCP %82-87 @ $0,101-0,148.

▸ **Yeni bir araç/MCP eklemeden önce sorulacak tek soru:**
> 🎙 **Sen:** "Bu aracı eklemeden önce token maliyetini ölç: aynı işi CLI ile yapmakla kaç turda ve kaç token'da bitiyor?"

---

### S12 · Telefondan / başka cihazdan bağlanmak (6:24)
**Durum:** evde değilsin, koşumlar sürüyor.

▸ **Telefonda SSH istemcisi** (Termius / Blink) → WSL'e SSH `[?] port-forward kurulumu ayrı adım`:
```bash
tmux attach -t ana
```
**Göreceğin:** masaüstünde bıraktığın **tam olarak aynı ekran** — çalışan ajanlar, akan çıktılar.
> 🎙/⌨ **Sen (sekme 0, firstmate):** "Durum nedir?" (`/bearings`)

---

### S13 · JARVIS kanon vardiyası bu düzende
**Durum:** rapor/tüzük/karar işi — kod değil.

▸ **Sekme 0 (firstmate) yerine sekme 9 "jarvis":**
```bash
cd /mnt/c/JARVIS && claude
```
> 🎙 **Sen:** "Günaydın."
> **Carvis:** kapsül + pano → tek net sıradaki iş.

**Fark:** kanon işi kod hattından geçmez — no-mistakes/gnhf burada koşmaz (araçlar `~/dev` altındaki depolarda koşar). Kanon reposunda çalışan tek şey ajan + git.
**Ama arayüz aynı kalır:** aynı WezTerm, aynı tmux, aynı ses girişi, kararlar `/lavish` ile tıklanabilir sayfada verilir.

▸ **Karar sunumu (m.37, 3 model):**
> 🎙 **Sen:** "Bu kararı metin duvarı olarak verme, lavish ile aç."
> **Carvis:** üç model üç kart; her kartın altında imza/red/beklet düğmesi.
> *(Sen kartlara not düşer, seçer, karar deftere iner.)*

---

### S14 · Staj işi (Otonet, 11 Ağu)
**Durum:** rolün doğrulama katmanı.

▸ **Ayrı sekme, ayrı repo, ayrı worktree:**
```bash
cd ~/dev/otonet && treehouse && claude
```
> 🎙 **Sen:** "Bu PR'ı doğrulama gözüyle incele: niyet neydi, testler o niyeti gerçekten koruyor mu, kanıt var mı?"

**no-mistakes burada senin işinin makinesi:** hattın adım sırası (niyet çıkarımı → karşıt inceleme → kanıtlı test → doküman → lint) senin elle yapacağın denetimin şablonudur.
**Sınır:** staj verisi JARVIS'e taşınmaz (md.49) — desen gider, veri gelmez.

---

### S15 · Bir şey ters gittiğinde
**Altın kural (P2 dersi):** hüküm **log'dan** verilir, semptomdan değil.

| Belirti | Gerçek kök | Nereye bakılır |
|---|---|---|
| `wait for run within 5s` | daemon değil — **boş diff** (dalda gerçek değişiklik yok) | `~/.no-mistakes/logs/<run>/rebase.log` → "empty diff after rebase" |
| gnhf 2 dakikada durdu | tavan cache-read ile doldu | `.gnhf/runs/<id>/gnhf.log` → `max tokens reached` |
| "kurulmadı" sanısı | özet ekranı yanıltır | diske bak, kurulum yoluna git |
| Hook tetiklenmiyor | aynı SHA tekrar push'landı | boş commit ile yeniden tetikle |
| tmux'ta ok tuşları garip | `escape-time` | `~/.tmux.conf` → `set -s escape-time 0` |
| Türkçe karakter bozuk (Windows tarafı) | PowerShell BOM | `-Encoding utf8NoBOM` |

---

## 5. Diyalog kalıpları kütüphanesi

*Kopyala, kullan. Sol sütun ne zaman, sağ sütun birebir cümle.*

| Ne zaman | Ne diyeceksin |
|---|---|
| İş başlatırken (belirsiz) | "…istiyorum. Üç seçenek çıkar ve tartışalım." |
| İş başlatırken (belli) | "…yap. Bitince **no-mistakes koştur**." |
| Hata bildirirken | "… Önce hatayı **uçtan uca yeniden üret**, sonra düzelt." |
| Ajan yanlış yaptığında | "Bu yanlıştı. Düzelt ve **hafıza dosyasına yaz** ki bir daha yapma." |
| Hafıza şiştiğinde | "Şu bölümü proje seviyesinde bir **skill'e çıkar**." |
| Plan metin duvarıysa | "Metin duvarı verme, **lavish ile aç**." |
| Uzun iş verirken | "Hedef … · durma koşulu … · tavan … ile **gnhf** başlat." |
| Paralel iş açarken | "**treehouse**, sonra ajan; bitince no-mistakes." |
| firstmate'e iş verirken | tek cümle. Bölmeyi ona bırak. |
| Uzaklaşırken | `/afk` · dönünce `/bearings` |
| Yeni araç önerildiğinde | "Eklemeden önce **token maliyetini ölç**; CLI ile kaç turda bitiyor?" |
| PR geldiğinde | "**Risk değerlendirmesi** nedir?" — düşükse diff'e bakma |

---

## 6. Günlük ritim (videodaki çalışma şekli)

| Zaman | Ne |
|---|---|
| Sabah | `tmux attach` → sekme 0 → "Ahoy, nerede kaldık?" → gece commit'lerini seç |
| İlk blok | Belirsiz işleri **lavish** turundan geçir (zamanın **başı** senin) |
| Gün | firstmate'e cümlelerle iş ver; sekmeleri o açar. Sen ekranda **beklemezsin** |
| Toplama | PR'lar gelir → risk etiketine göre incele → merge (zamanın **sonu** senin) |
| Akşam | `olcum-dortlu.py --append` → ölçüm defteri |
| Yatarken | Uzun iş varsa **gnhf** — durma koşulu + tavan yazılı |

**Videonun kendi özeti (33:12):** zaman işin **başında** (planlama) ve **sonunda** (kalite eşiği) harcanır; ortası ajanındır. Ortayı ne kadar uzatırsan o kadar paralel iş açarsın.

---

## 7. Künye ve şerhler

**Bu rapor ne yapmadı:** karar almadı · kanon (`core/`, `CLAUDE.md`) yazmadı · kapsül/pano/senaryo-defteri güncellemedi (**ingest yok**) · alternatif/ikame önermedi (emir zemini: birebir kopya).

**`[?]` işaretli, ilk koşumda teyit edilecekler:**
1. `gnhf` tam CLI sözdizimi ve flag adları → `gnhf --help`
2. treehouse ve no-mistakes'in **Linux** kurulum satırları (kanonda doğrulanmış olan Windows/PowerShell satırlarıydı)
3. Harness kurulum paket adları (Claude Code / Codex CLI / Pi / OpenCode)
4. `~/.agents/AGENTS.md` symlink yolunun harness'lerce beklenen tam adresi
5. Windows tarafında yerel-whisper uygulamasının initial-prompt desteği
6. AXI araçlarının kurulum satırları (axi.md kataloğundan)
7. Telefondan WSL'e SSH kurulumu (port-forward adımı ayrı)

**`[D-belge]` (rapor-4 §II.1, 08-03 ölçüm anı):** firstmate komut seti ve modları · durum dörtlüsü `busy/idle/unknown/dead` · no-mistakes adım sırası (Review → Test → Docs → Lint → Push → PR → CI) · AXI 10 ilke ve benchmark rakamları · telemetri varsayılanları.

**Sahada ölçülmüş (P1/P2/P6, `[deneysel m.29]`):** gnhf iki durma modu · token sayacının cache-read dahil sayması · no-mistakes 2 uçtan uca koşum + eskalasyon · `tools/olcum-dortlu.py` dörtlü çıkarımı.

**Bilinen sapma (m.39):** transkriptin anlattığı no-mistakes adım granülerliği README'de birebir yok; "adversarial review" ve "rebase" terimleri README'de literal geçmiyor — §S9/S10'daki anlatım transkripte dayanıyor.

---

**Rapor sonu.**
