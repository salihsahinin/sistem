# KURULUM — yeni makinede kaldığın yerden devam (2026-09-21, Salih emri: "bilgisayarı şirkete teslim edeceğim; sonraki Windows ya da Mac olabilir")

*Envanter bu makineden çıkarıldı (macOS 26.6.2, 2026-09-21 ~10:3x, `brew`/`npm`/`pip`/`ls` sayımı). AS-OF damgalı; sürümler o güne aittir, kurulumda güncelini al.*

## 0. Sıra (30 dk `[?]`)
1. Git + GitHub girişi → `git clone https://github.com/salihsahinin/sistem.git ~/sistem` (remote private; `gh auth login`).
2. Node ≥ 22 → `npm i -g @anthropic-ai/claude-code lavish-axi gh-axi chrome-devtools-axi quota-axi tasks-axi gnhf @mermaid-js/mermaid-cli`.
3. Python 3.13 → `pip3 install pandas numpy` (sqlite3 Python'la gelir).
4. Harness global dosyaları: `sablonlar/harness/claude-global-CLAUDE.md` → `~/.claude/CLAUDE.md` · `sablonlar/harness/claude-global-settings.json` → `~/.claude/settings.json` (birebir kopya, §3).
5. Claude Code masaüstü uygulamasını aç, cwd `~/sistem/jarvis`, worktree kapalı, "seans başı". SessionStart hook'u brifi basar; K3 "silver bayat" der → `python3 tools/katman-hatti.py` (silver sqlite gitignore'da, ~12 sn yeniden türetilir).
6. Hook testleri: `bash jarvis/.claude/hooks/pretool-altajan-okuma-test.sh` · `cd friday && bash .claude/hooks/okuma-izin-test.sh` · her alan ajanında `bash .claude/hooks/okuma-izin-test.sh` (39/0 beklenir). Hook'lara `chmod +x` gerekebilir.
7. Ev yolu farklıysa (`/Users/HasanSalihSahin` ≠ yeni): §4.

## 1. Uygulamalar (bu makinede kurulu, işte kullanılan)
| Uygulama | Ne için | Kurulum |
|---|---|---|
| Claude Code masaüstü (Code sekmesi) + CLI `claude` (npm 2.1.273) | tüm ajan oturumları; Jarvis Fable, Friday Opus, alan ajanları Sonnet | claude.com/claude-code; hesap girişi |
| VS Code | md/.d2 okuma yüzeyi (Karar 80) | code.visualstudio.com |
| WezTerm | terminal (hook testleri, script'ler) | brew cask `wezterm` / Windows: wezterm.org |
| Google Chrome | Lavish karar masaları (`http://127.0.0.1:4387`), tarayıcı araçları | — |
| DB Browser for SQLite | `veri/baglam.sqlite` bakışı (isteğe bağlı) | brew cask |
| QLMarkdown, OpenSuperWhisper | Finder md önizleme, ses→metin (isteğe bağlı, Mac) | brew cask |
| Obsidian | emekli (Karar 80); `.obsidian/` gitignore'da | — |

## 2. Komut satırı araçları
| Araç | Sürüm (AS-OF) | Kullanım | Kur |
|---|---|---|---|
| git | 2.50 | depo; `user.name salihsahinin`, `user.email 185700233+salihsahinin@users.noreply.github.com` | sistem paketi |
| gh + `gh-axi` | 0.1.33 | PR/issue; SessionStart hook'u | brew `gh` + npm |
| `lavish-axi` | 0.1.59 | karar masası yüzeyi (`kaynak-kodu/lavish/*.html`) | npm |
| `chrome-devtools-axi` | 0.1.29 | tarayıcı otomasyonu | npm |
| `quota-axi`, `tasks-axi`, `gnhf` | 0.1.30 / 0.2.5 / 0.1.45 | kota, görev, gece işi (Karar 84) | npm |
| `@mermaid-js/mermaid-cli`, `d2`, graphviz | 11.17 / brew | görsel üretimi (`graf/`, `raporlar/gorsel-*`) | npm / brew |
| Python 3.13 + pandas 3.0.5, numpy 2.5.2 | — | `tools/*.py` (katman-hatti, silver-saglik, hareket-tablo, alan-ajani-dogur…) | brew/python.org + pip |
| sqlite3 CLI | sistem | silver sorguları (`v_guncel_kayit`, `v_okuma_orani`) | sistem paketi |
| jq, tmux, neovim, treehouse, merve | brew | yardımcı | isteğe bağlı |
| `promptfoo` | kurulu **değil** (evals H1-H3 npx ile koştu) | Solon eval setleri | `npx promptfoo@latest` |

Global skill'ler (`~/.claude/skills/` ve `~/.agents/skills/`: lavish · gh-axi · chrome-devtools-axi · no-mistakes) axi paketleriyle gelir; `no-mistakes` ayrı kurulum (`~/.no-mistakes/`; yeni makinede yeniden kur, remote `no-mistakes` bu yüzden görünür).

## 3. Harness dosyaları (repo dışı, kopyaları `sablonlar/harness/`)
- `~/.claude/CLAUDE.md` — kullanıcı düzeyi talimat (≤25 satır, Karar 96 M1). Kopya: `sablonlar/harness/claude-global-CLAUDE.md`.
- `~/.claude/settings.json` — model/effort (Fable xhigh), dil Türkçe, SessionStart hook'ları (gh-axi · chrome-devtools-axi · lavish-axi), tam ekran TUI. Kopya: `sablonlar/harness/claude-global-settings.json`.
- `~/.claude/projects/<anahtar>/memory/` — Jarvis oto-hafızası; **aynası repoda** `jarvis/veri/hafiza-ayna/-Users-HasanSalihSahin-sistem/` (Karar 104 M3). Yeni makinede anahtar ev yoluna göre değişir (§4); aynayı yeni anahtarın `memory/` dizinine kopyala.
- `~/.claude/keybindings.json` yok (varsayılan). Türkçe-Q klavye.

## 4. Ev yolu farklıysa (Windows ya da farklı kullanıcı adı)
- Sabit `/Users/HasanSalihSahin` geçen kod/ayar dosyaları (09-21 sayımı: 6): `jarvis/tools/yol-tasi.py` (kendisi taşıyıcı) · `jarvis/tools/alan-ajani-dogur.py` (test yolu üretimi) · `jarvis/.claude/settings.local.json` · `jarvis/.claude/hooks/pretool-altajan-okuma-test.sh` · `friday/.claude/hooks/okuma-izin-test.sh` · alan ajanı test dosyaları (üreticiyle yeniden üretilir). Hafıza anahtarı `-Users-HasanSalihSahin-sistem` geçenler: `sicak-katman-fifo.py` · `prompt-tablo.py` · `ambar-tablo.py` · `hafiza-ayna.py` · `kosum-maliyeti.py`. Yöntem: `tools/yol-tasi.py` sınıfı tek kuru koşum + `--uygula` (Karar 101 F3 emsali), ardından hook testleri.
- **Windows:** hook'lar ve `bin/hook-dispatch.sh` bash ister → Git Bash ya da WSL2 (Ubuntu) altında çalıştır; Claude Code'u WSL içinde kur (yollar `/home/<ad>/sistem`). Symlink'ler (`CLAUDE.md → AGENTS.md`, `.claude/skills/ogren`) için `git config core.symlinks true` klonlamadan **önce**; NTFS'te symlink için geliştirici modu. `sed -i ''` (BSD) kullanan tek satırlar GNU'da `sed -i` olur (tools içinde yok, yalnız sohbet komutlarında).
- **Windows fiili kurulum (2026-09-22, Fable; Git Bash + Claude Code masaüstü, WSL yok):** depo `C:\sistem\sistem` (zip'ten; iç içe dizin sonra düzeltilecek). Yapılanlar: `core.filemode=false` + `core.autocrlf=false` (repo-yerel; 89 sahte mod/CRLF değişikliği) · geliştirici modu + `core.symlinks=true` + 15 symlink yeniden checkout · `~/bin/python3` shim (Store'un `python3.exe` yönlendiricisi "Python bulunamadı" exit 49 verip hook'ları susturuyordu) · Graphviz PATH'e elle · `~/.claude/settings.json` şablondan (eski Orca kopyası `.bak-windows-orca-2026-08-04`) · hafıza aynası → `~/.claude/projects/C--sistem-sistem/memory/` (anahtar `C--sistem-sistem`). Hook testleri artık yol-bağımsız: test dosyaları `SISTEM=$(cd .. && pwd -W || pwd)` + `EV` ile kurulur; `okuma-izin.sh` "ev dışı serbest" kuralına depo-kökü şartı eklendi (Windows'ta depo ev altında değil); `pretool-altajan-okuma.sh` friday yolunu depo kökünden türetir + `C:/` sürücü öneki yol adayı. 6 takım 14/34/39×4 yeşil. Kalan: `kaynak-kodu/no-mistakes` symlink'i Mac mutlak yolunda (kırık) · `jarvis/.venv` Mac artığı · silver türetimi 56 sn (Mac 12 sn).
- **Mac:** birebir; yalnız kullanıcı adı farkı §4 ilk madde.

## 5. Repoya girmeyen veri (gitignore) — yeniden üretilir ya da ayrıca taşınır
| Yol | Boyut | Ne yapılır |
|---|---|---|
| `jarvis/veri/baglam.sqlite` | 379 MB | `python3 tools/katman-hatti.py` yeniden türetir (deterministik, Karar 77) |
| `jarvis/veri/erisim-vektor.sqlite` + `erisim-vektor-bge.npy` + `erisim-vektor-e5.npy` | ~1 GB | İB-78/erişim hattı; `tools/erisim-*.py` ile yeniden üretim (model indirir); acil değil |
| `ogrenme/kaynaklar/mit-6006-s20/`, `mit-6042j-f10/` | 81 + 77 MB | MIT OCW arşivleri; künye `ogrenme/kaynaklar/*-KUNYE.md`'deki kaynaktan yeniden indir ya da harici diske kopyala (Euclid'in ders kaynağı) |
| `jarvis/.lavish/` (`kaynak-kodu/lavish`) | 388 KB | masa HTML'leri; kalıcı kopya `jarvis/raporlar/masa/` repoda, kayıp yok |
| `jarvis/.secrets/` | — | yok; sır dosyası kullanılmıyor (AS-OF) |
| `**/.venv/` | — | `jarvis/.venv` boş sanal ortam; gereksiz |
| **`~/staj başlangıç/`** | 9,6 MB, 29 commit, **remote yok** | md.49: şirket verisi; bilgisayar şirkete dönüyor — kalmasını istiyorsan **bugün** harici diske/özel repoya kopyala, Jarvis deposuna girmez |

## 6. Kaldığın yer
Kapsül `jarvis/core/durum-kapsulu.md` (seans-5 kapandı 09-21 ~16:0x, push'landı) · teslim raporu `jarvis/raporlar/seans/seans-teslim-2026-09-21-bitirme-tezi-atlas.md` (önceki: `…-karar104-105-alan-ajanlari-hakem.md`) · ajan tablosu kök `README.md` · her ajanın kuruluş satırı kendi `README.md`'sinde.
- **Bitirme tezi (Salih'in tezi, 09-21):** Atlas raporu `jarvis/raporlar/2026-09/2026-09-21-bitirme-tezi-ai-matematik-atlas.md` (Ö1-Ö6 öneriler; karar Salih'te) · ham 16 rapor `jarvis/cc/rapor/2026-09/rapor-2026-09-21-bitirme-*` · harness hafızasında `user-bitirme-tezi-matematik-muhendisligi.md` (ayna §3).
- **Yeni makinede ilk oturum:** `cd sistem/jarvis` → "seans başı" (kapsül + `tools/acilis-kapilari.py`; K3 silver `BAYAT` çıkar, `tools/katman-hatti.py` ~12 sn tazeler; canlı transkript sayısı 0'dan başlar, K1 `TEMİZ` beklenir).
