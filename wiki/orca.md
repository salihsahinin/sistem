> **TAŞINDI (2026-07-15, Salih icra emri):** Homebase'ten JARVIS'e — köken: `Cowork Homebase/[C] Orca — LLM Wiki.md`; tespit raporu: `raporlar/2026-07/homebase-tasima-tespiti-2026-07-15.md`. Orijinal Homebase'te arşiv-pointer'la durur (m.8).

# Orca — LLM Wiki

> Oluşturma: 2026-07-09 (Cowork, kurulum sırasında). Kaynaklar: onorca.dev resmi dokümantasyon (docs/terminal, docs/agents/claude-code, ana sayfa) + GitHub (stablyai/orca) + bağımsız incelemeler. Bu sayfa Salih'in "Jarvis" hattının bir parçası: Cowork = orkestra şefi, Claude Code = uygulayıcı, Orca = Claude Code'ların yaşadığı ev.

## 1. Orca nedir?

Orca, kendini **ADE** (Agent Development Environment — "ajan geliştirme ortamı"; IDE'nin ajan-öncelikli hâli: ortam senin için değil, sen + kod ajanların için tasarlanmış) olarak tanımlayan, açık kaynak (MIT lisanslı, ücretsiz) bir masaüstü uygulaması. Yapımcısı Stably (YC destekli); macOS, Windows ve Linux'ta çalışıyor; GitHub'da ~13 bin yıldız.

Tek cümlelik özü: **birden fazla terminal kod ajanını (Claude Code, Codex, Gemini, Cursor CLI vb.) yan yana, birbirine karışmadan çalıştırmak için kurulmuş kontrol merkezi.**

Somut örnek: normalde Claude Code'u tek bir terminal penceresinde açarsın; ikinci bir görev istediğinde ya bekler ya ikinci pencere açıp branch (dal — aynı reponun paralel çalışma kopyası) kaosuna girersin. Orca'da her göreve tek tıkla ayrı bir **worktree** açılır ve her worktree'de ayrı bir Claude Code koşar — üçü aynı anda üç farklı işi yapar, birbirinin dosyasına dokunmaz.

## 2. Çekirdek kavram: Worktree

**Git worktree** = aynı reponun diskte ayrı bir klasöre açılmış, kendi branch'inde yaşayan paralel çalışma kopyası. `git stash`/branch değiştirme derdi olmadan aynı projede iki işi fiziksel olarak ayırır.

Örnek (PortRisk üzerinden): ana klasörde `main` branch'i dururken, Orca "VaR modülü ekle" görevi için `portrisk-var` diye ikinci bir klasör + branch açar. Oradaki Claude Code istediği kadar dosya değiştirsin — senin `main`'in tertemiz kalır. Beğenirsen merge edersin (birleştirirsin), beğenmezsen klasörü silersin. Orca'nın tüm modeli bu ilkenin üstüne kurulu: **1 görev = 1 worktree = 1 ajan.**

## 3. Ana özellikler (ne işine yarar)

**Terminal:** VS Code'un kullandığı xterm.js tabanlı; Ghostty-tarzı (popüler bir hızlı terminal) split'ler (bölmeli ekran), scrollback araması, oturum geri yükleme. Yani Claude Code'un çıktısında `Ctrl/Cmd-F` ile arama yapabilirsin.

**Claude Code birinci-sınıf ajan:** Orca `~/.claude` klasörünü otomatik tanır — bir kere herhangi bir terminalden login olursan Orca ekstra ayar istemez. Status bar'da kullanım + rate-limit (kullanım kotası) yakınlığını gösterir; birden çok Claude hesabı arasında tek tıkla geçiş yapar.

**Diff görüntüleyici + Annotate AI Diff:** ajanın yaptığı değişikliği satır satır görürsün; herhangi bir satıra markdown yorum bırakıp toplu hâlde ajana geri gönderirsin. Örnek: Claude Code load.py'a 20 satır ekledi → sen 3 satıra "burada negatif ağırlık kontrolü eksik" notu düşersin → tek tıkla Claude'a döner.

**Design Mode + gömülü tarayıcı:** worktree başına gerçek bir Chromium penceresi; UI'daki bir öğeye tıklayınca HTML/CSS'i + ekran görüntüsü ajana gider (web projesi yapıyorsan işe yarar; PortRisk için şimdilik değil).

**Orca CLI + otomasyon:** ajanlar Orca'yı da komutla sürebilir (`orca worktree create` gibi); zamanlanmış otomasyonlar ve orchestration (bir ajanın diğer ajanlara iş dağıtması) var. Jarvis vizyonu için asıl kritik parça burası — Cowork/Claude'un "3 ajanı paralel sal, sonuçları karşılaştır" tarzı akışları buradan geçer.

**Mobil eş uygulama:** telefondan canlı ajan durumu izleme, hesap değiştirme, uzaktan devam ettirme.

**GitHub/Linear/Jira entegrasyonu:** PR inceleme, issue'dan worktree açma — uygulamadan çıkmadan.

## 4. Windows'ta shell (kabuk) meselesi — kurulum ekranındaki soru

Orca'nın "Default Shell" ayarı yalnızca **senin elle açtığın terminal panelerinin** hangi kabukla açılacağını belirler. Claude Code'un kendi çalışması bundan bağımsızdır: ajanı combobox'tan seçtiğinde Orca onu kendi başlatır. Yani bu seçim "Claude Code hangi shell'de koşar" sorusu değil, "ben boş bir terminal açınca ne görürüm" sorusudur.

Üç seçenek: **PowerShell** (modern Windows varsayılanı; her komut çalışır, `dir` de `ls` de anlar), **Command Prompt** (eski cmd.exe; bugün seçmek için sebep yok), **Git Bash** (Git for Windows'un bash'i; Unix-stili komutlar — internetteki çoğu öğretici Unix komutu verdiği için bazıları bunu sever). Docs'a göre **wsl** kuruluysa o da listeye düşer. Ayar sonradan Settings → Terminal'den her an değiştirilir; ayrıca tab çubuğundaki **+** menüsünden varsayılanı bozmadan tek seferlik başka shell'de tab açabilirsin — yani karar düşük riskli.

**Right-click davranışı:** "Paste on right-click" = sağ tık panodakini yapıştırır (klasik Windows terminal alışkanlığı; Ctrl+sağ tık menüyü açar). "Open context menu" = sağ tık normal menü açar.

## 5. Salih'in sistemindeki yeri

- **Cowork** = planlama/orkestrasyon + ritüel (good-morning, end-of-day, hizalama).
- **Claude Code** = uygulayıcı (PortRisk commit'leri, Benlik döngüleri).
- **Orca** = Claude Code oturumlarının çalıştığı yüzey; paralel ajan gerekince (ör. loop-eng Faz 2+ ve sonrası, PortRisk sprint'leri) worktree izolasyonu sağlar.

Dikkat noktası (koç şapkası): Orca güçlü bir *araç zenginliği* sunuyor — paralel 5 ajan, orchestration, otomasyon. Senin darboğazın hiçbir zaman araç eksikliği olmadı; gönderilmiş çıktı. Orca'yı "tek worktree, tek ajan, biten iş" modunda kullanmaya başla; paralellik ihtiyaç doğunca gelsin. Aksi hâlde bu da sistem-üstüne-sistem rafına gider.

## 6. Kaynaklar

- Resmi site + docs: https://www.onorca.dev / https://www.onorca.dev/docs
- Claude Code entegrasyonu: https://www.onorca.dev/docs/agents/claude-code
- Terminal ve Windows shell ayarları: https://www.onorca.dev/docs/terminal
- GitHub: https://github.com/stablyai/orca
