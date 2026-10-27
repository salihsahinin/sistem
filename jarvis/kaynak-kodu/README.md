# Kaynak Kodu — Jarvis'in kaynak haritası (görünür kapı)

*Açık kaynak ilkesi (Salih 2026-08-17, Katman-1): Jarvis'in davranışını belirleyen her şey bu klasörde okunur metin olarak yaşar; Salih kaynak kodunu istediği an okuyabilir. Bu klasör bir HARİTA + KAPIDIR: kodun kendisi burada değil, adresi burada. `claude` = gizli `.claude/` klasörünün kendisi (bağ/alias; Finder gizli klasörleri göstermediği ve Obsidian nokta-klasörleri saymadığı için açıldı). Kural: bu harita KONUM listeler, dosya değil — yeni konum açılırsa buraya satır düşer. **Gizli klasör YOK (Salih Katman-1, 2026-08-18):** Jarvis'in kullandığı her nokta-dizin için (1) burada görünür kapı (bağ) + (2) README satırı + (3) dizinin kendisi Finder'da görünür — `defaults write com.apple.finder AppleShowAllFiles -bool true && killall Finder` (08-18'de uygulandı; değer 1). Bugünkü nokta-dizinler: `~/jarvis/.claude` (skill/hook/ayar) · `~/.claude` (Claude Code kullanıcı düzeyi: skill'ler, projeler/transkriptler) · `~/.no-mistakes` (kapı aracı) · `~/jarvis/.secrets` (sır; içerik gizli KALIR, klasör görünür) · `~/jarvis/.obsidian` (Obsidian ayarı) · `.git` (git; araç dizini, kapı gerekmez).*

## Nasıl açarım (Finder)
- Bu klasör: `open ~/jarvis/kaynak-kodu` — içindeki `claude` bağına çift tıkla → skill'ler, hook'lar, ayarlar.
- Doğrudan skill'ler: `open ~/jarvis/.claude/skills`
- Gizli dosyaları Finder'da KALICI görmek istersen (senin tercihin, sistem ayarı): Finder'dayken **⌘ ⇧ .** (Command-Shift-Nokta) — bir kez basınca açık kalır, tekrar basınca kapanır.
- Obsidian'da `.py`/`.sh` görmek için: Ayarlar → Files & Links → "Detect all file extensions".

## Dil kuralı (Salih 2026-08-17)
Kaynak dosyalar **Türkçe**: SKILL.md'ler, ajan tanımı (`research-agent.md` = ATLAS, 08-17'de çevrildi; İngilizce aslı `kuyruk/arsiv-atlas-taban-metni-en-2026-07-13.md`), hook'lar, kural/şema dosyaları, script docstring/yorum/çıktı mesajları, wiki sayfaları. Türkçe OLMAYAN ve öyle kalan: kod tanımlayıcıları ve Python/SQL/JSON anahtar sözcükleri · üçüncü-parti araç skill'leri (`~/.claude/skills/` gh-axi, lavish, chrome-devtools-axi, no-mistakes — repo dışı, bizim değil) · commit mesajları (tüzük m.10) · alıntılanan İngilizce kaynak metinler (üstüne Türkçe özet konur; örn. `wiki/kokenler-karpathy-llm-wiki.md`) · Claude Code'un kendi ürettiği dosyalar (`.claude/RESUME.md` gibi).

## Kaynak kodu nerede (repo içi)
| Bileşen | Yol | Ne | Nasıl okunur |
|---|---|---|---|
| Oturum sözleşmesi | `CLAUDE.md` | Her oturumun otomatik okuduğu davranış sözleşmesi (v2, ≤80 satır) | düz metin; kural numaraları (m.NN) tüzüğe işaret eder |
| Kanon (kurallar) | `core/tuzuk-v0.md` + `core/*.md` | Tüzük 46+ madde; şema/kural dosyaları (ajan-metodolojisi, skill-üretim, skill-tetikleme, halüsinasyon-paketi, şema-sıkıştırma, anahtar-kaydı, ingest, veri-katmanı, world-model) | her kural dosyası kendi başlığıyla; `.d2` dosyaları grafiklerin kaynağı |
| Durum | `core/durum-kapsulu.md` · `core/pano.md` | Şu an neredeyiz + kartlar (üzerine yazılır) | ilk 40 satır yeter |
| Modlar (Claude Code function hooks) | `mods/<mod>/` (`jarvis-oda`, `jarvis-graf`) | Claude Code arayüzüne pane/araç/komut ekleyen hooks modülleri (Karar 126, 2026-10-27); canlı kopya `~/.claude/dev-mods/` | `mods/README.md` tablo → `hooks/register.tsx` (tek dosya), `types/index.d.ts` durum sözleşmesi |
| Skill'ler (16) | `.claude/skills/<ad>/SKILL.md` (+ `scripts/` `evals/` `references/`) | Jarvis'in tetiklenebilir davranış paketleri: seans-acilis, seans-kapanis, damitma, gorev-emri-derleme, atlas-kosum, pipeline-kosum, karar-hatti, karar-modeli, karar-kaydet, celiski-kapisi, lojik-ceviri, yol-planla, sinav-grill, skill-kapisi, halusinasyon-engelleyici, wiki-sayfa-yaz | önce frontmatter `description` (tetik yüzeyi), sonra adımlar; `scripts/` Python (stdlib) |
| **no-mistakes** (üçüncü-parti kapı aracı; 08-18 ilk kullanım) | `kaynak-kodu/no-mistakes` → `~/.no-mistakes/` (gizli nokta-klasör; aracın kendi ev dizini — bizim seçimimiz değil): `config.yaml` (ajan/izin/auto_fix ayarları) · `repos/c674481304c5.git` (jarvis'in yerel bare gate'i; `git remote no-mistakes`) · `worktrees/c674481304c5/` (pipeline ajanının çalıştığı kopya — izin istemleri buradan gelir) · `logs/<run-id>/*.log` (adım logları) · `state.sqlite` (koşum durumu) · `bin/no-mistakes` (ikili v1.48.0); skill: `~/.claude/skills/no-mistakes/SKILL.md` | Her adım (review/test/document/lint/pr) ayrı `claude` CLI ajanı açar; PR merge Salih'te | önce `config.yaml`, sonra ilgili koşumun `review.log` |
| Hook'lar | `.claude/hooks/session-start.sh` · `pretool-core-tel.sh` · `pretool-ajan-fren.sh` (08-29, İB-54) | Açılışta kapsül+pano+yetki bandı enjekte eder · Bash ile `core/`/`CLAUDE.md`/`.claude/` yazımına tökezleme-teli · Agent fan-out freni: oturum başına sayaç, UYARI 36 (bronz olay) / DURDUR 72 (exit 2), rejim etiketli, `JARVIS_FREN_KAPALI=1` Salih beyanıyla geçer; test `tools/testler/test_fren_hook.py` | 20-30 satır bash; başındaki yorum gerekçeyi verir |
| Ayarlar | `.claude/settings.json` · `.claude/settings.local.json` · `.mcp.json` | İzinler (push = sor) + hook kaydı · yerel izinler · MCP sunucuları (context7) | JSON |
| Ajan tanımı | `.claude/agents/research-agent.md` | "atlas" araştırma ajanının sistem metni | markdown |
| Ajan tanımı | `.claude/agents/hakem.md` + `.claude/agent-memory/hakem/` | "hakem" maskeli bağımsız değerlendirici (salt-okur, V26 zorunlu; Karar 103 M1 · İB-108, 09-20) + usul-hafızası | markdown |
| **Obsidian okuma yüzeyi** (2026-08-26) | `kaynak-kodu/obsidian` → `.obsidian/` (gitignore'lu; ayar dosyaları kişisel) | Jarvis deposunu Obsidian vault'u olarak okuma ayarı: varsayılan görünüm = okuma modu, `[[wiki-link]]` takibi + backlink + graf, gürültülü veri klasörleri indeks dışı (`app.json` → `userIgnoreFilters`). Vault kaydı 2026-08-12'de açılmıştı, ayarlar 08-26'da yazıldı. ~~Tamamlayıcı: QLMarkdown QuickLook eklentisi~~ (EMEKLİ 08-26 Karar 72 — md açma yüzeyi tek: Obsidian; kaldırma Salih el işi) | `app.json` (okuma davranışı) → `appearance.json` (yazı boyu/tema); `workspace.json` OKUNMAZ (Obsidian üretir) |
| Kalıcı script'ler | `tools/*.py` (indeks: `tools/SCRIPTLER.md`) | Bağlam→DB hattı (baglam-tablo, katman-hatti, prompt-tablo, karar-borcu-tablo, ambar-tablo), hareket kütüğü (hareket-tablo → `raporlar/hareket-gunlugu-*.md`: Jarvis'in her araç çağrısı, günlük), ölçüm (katman-olcum, olcum-dortlu), denetim (anahtar-denetim, verify-push), sunum üreticileri (sunum-son50, sunum-proof-of-work), kolon katmanı (ambar-parquet, kolon-olcum — OPSİYONEL, `duckdb` ister, KB-55 hükmüne dek; testler `tools/testler/`, stdlib unittest) | her dosyanın başındaki Türkçe docstring: ne yapar · nasıl koşar · hangi kurala dayanır |
| Şablonlar | `core/sablonlar/` | Görev emri / görev fonksiyonu / rapor / hasat / seans-teslim iskeletleri | markdown |
| Veri | `veri/` (`veri/README.md`) | Bronz kütükler (`bronz/`, `*.jsonl`) · silver `baglam.sqlite` (gitignore, script'le yeniden üretilir) · gold `gorunum/*.csv` · sözleşmeler `sozlesme/` · opsiyonel kolon türevi `parquet/` (gitignore; `--parquet` bayrağıyla üretilir) | önce README, sonra `python3 tools/katman-hatti.py` |
| Görev/rapor kanalı | `cc/` | Ajan görev emirleri (`gorev-*`), ajan raporları (`rapor-*`), pipeline manifestleri, `cc/workflow/` (koşulan Workflow script'lerinin kopyaları — çalışma şeklinin kodu) | emir → rapor eşleşmesi tarih-numarayla; workflow script'i = hangi ajan hangi sırayla |

## Repo DIŞINDA yaşayan ama davranışı etkileyenler (açık-kaynak ilkesine göre BORÇ — burada listeli, hedef: repoya ya da buraya)
| Ne | Yol | Not |
|---|---|---|
| Global Claude Code ayarı | `~/.claude/settings.json` | model (Fable), effort, 3 axi SessionStart hook'u (gh-axi, chrome-devtools-axi, lavish-axi) |
| Jarvis'in oturumlar-arası hafızası | `~/.claude/projects/-Users-HasanSalihSahin-jarvis/memory/` (`MEMORY.md` + dosyalar) | kullanıcı/feedback/proje notları — kanon DEĞİL, hatırlatıcı |
| Global skill'ler | `~/.claude/skills/` (gh-axi, lavish, chrome-devtools-axi → `~/.agents/skills/`; no-mistakes) | üçüncü-parti araç skill'leri |
| Bulut skill kopyaları | claude.ai (anthropic-skills: gunaydin-vardiya, vardiya-kapanis — emekli adlar; hizalama, dev-run-planner) | repo'daki seans-acilis/seans-kapanis'in ESKİ (emekli) adlı kopyaları; **KALDIRILACAK** (Salih 08-17 KB-10 H6: tek kaynak repo; Salih eli claude.ai'da) |
| Oturum transkriptleri | `~/.claude/projects/<proje>/*.jsonl` | bronz kaynak (prompt-tablo/ambar-tablo buradan okur); repo dışı, kişisel |

## Okuma sırası önerisi
1. `CLAUDE.md` (5 dk) → 2. `core/tuzuk-v0.md` başlıklar → 3. bir skill: `.claude/skills/seans-acilis/SKILL.md` → 4. hook'lar → 5. `tools/SCRIPTLER.md` "Beraber okuma" sırası (derece.py en kısa).

| **Lavish çalışma dizini** (Karar 92 M2, 2026-09-10) | `kaynak-kodu/lavish` → `.lavish/` (gitignore; lavish-axi masa yüzeyi çalışma alanı) | Karar masası HTML burada üretilir, her masa sonunda kalıcı kopya `raporlar/masa/masa-N-karar-yuzeyi-YYYY-MM-DD.html` | HTML; Finder çift tık |

> **Ad eşitliği (Karar 93, 2026-09-10):** bu dizindeki tarihli dosyalarda geçen **Carvis = Jarvis** (Salih'le konuşan ajanın 09-10 öncesi adı); sistem/repo kastedilirken "depo"/"kanon". Halef-sözlük: `core/baglam-anahtar-kaydi.md` anahtar `carvis-rol-adi` → `jarvis-ajan-adi`.

| Alt-ajan okuma kilidi (İB-83, 2026-09-10) | `.claude/hooks/pretool-altajan-okuma.sh` (+ `-test.sh` 9 vaka) | Alt-ajan (`agent_id` var) transkript · kapsül/pano/defter/kutu/MEMORY · kütükler · Friday · dış projeleri OKUYAMAZ; RED → `veri/bronz/altajan-okuma-olay.jsonl` | bash |
