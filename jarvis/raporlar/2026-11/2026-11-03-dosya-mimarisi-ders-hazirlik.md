# Dosya mimarisi dersi hazırlık (3 tarama özeti; AS-OF 2026-10-31 koşum, kayıt 2026-11-03)

Seans `2026-10-31-jarvis` hedefi. Ders kendisi `../ogrenme/dosya-mimarisi/` altında fork oturumunda başladı; bu dosya üç alt-ajan taramasının damıtılmış hâlidir, ders kutuları buradan beslenir. Tam raporlar transkriptte, buraya yalnız karar değiştiren satırlar alındı.

## 1. Kutular (8; İngilizce sektör başlığı + kaynak)
1. **Screaming Architecture, feature vs layer layout** — cleancoder.com 2011-09-30; martinfowler.com PresentationDomainDataLayering.
2. **Monorepo workspace conventions** — turborepo.dev structuring-a-repository (apps/ + packages/, iç içe paket hata) · bazel.build external/overview (MODULE.bazel kök işaret) · doc.rust-lang.org cargo workspaces (tek Cargo.lock, `crates/*` düz) · packaging.python.org src-layout.
3. **Docs-as-code: ADR + Diátaxis** — learn.microsoft.com ADR (ms.date 2026-04-10; yalnız eklenir, superseded) · adr.github.io/madr 4.0.0 (`docs/decisions/NNNN-baslik.md`) · diataxis.fr.
4. **Information architecture for knowledge repos** — fortelabs.com PARA (Archives üst kova) · zettelkasten.de (atomik not, sabit kimlik, klasör yerine bağ) · johnnydecimal.com/concepts (10x10 sınırı sayfada yok, doğrulanmadı).
5. **Medallion data layering** — docs.databricks.com lakehouse/medallion (bronze ham + append, silver doğrulanmış, gold tüketim); dizin adı eşlemesi bizim çıkarımımız.
6. **Repository structure smells + folder linting** — ls-lint.org (ad kuralları, `.ls-lint.yml`) · alint 0.9.18 docs.rs (derinlik, dizin başına dosya; ikincil kaynak). Koku listesi için tek kanonik kaynak yok, derste "çıkarım" damgası.
7. **Agent context files** — agents.md (ajan README'si, en yakın dosya kazanır) · code.claude.com/docs/en/memory (CLAUDE.md <200 satır, `.claude/rules/`) · arXiv 2602.11988 (bağlam dosyası başarıyı artırmıyor, maliyet >%20) · arXiv 2601.20404 (süre/token düşük, tamamlama benzer).
8. **Archive, never delete; pointer discipline** — ADR superseded + PARA Archives + Zettelkasten kimlik birleşimi; çıkarım.

## 2. Öğretim yöntemi (kanıt satırları)
- Faded worked example: kutu 1-2 tam çözüm, 3-5 bir adım boş, 6-8 Salih yapar (Renkl; expertise reversal: probe yüksekse erken geç).
- Subgoal labels: her düzeltme 3 adlandırılmış adım (sorumluluk → hedef yer → bağımlılık güncelle) (Margulieux/Morrison).
- Self-explanation g=0,55: kutu sonu sorusu "bu düzeltme neden işe yarıyor, hangi yanlış kavram tuzak" (BPS meta-analiz).
- Contrasting cases: önce/sonra ağaç çifti, önce "fark ne?" (Schwartz-Bransford; yapı öğretimi için doğrudan deney yok).
- Kutu başına ≤3 dosya taşıma; koda dokunmadan "bu yapı hangi sorumluluğu taşımalı" adımı (SIGCSE 2024 own-smells; Koli 2016 redesign).
- Canlı refactor izlettirme etkisiz (ICER 2023, SIGCSE 2025): Salih kendi eliyle yapar.
- Görsel: yalnız şehir/graf ailesinde ölçülmüş kanıt (CodeCity ICSE 2011); treemap/ağaç-diff kanıtsız, dersin kendi önce/sonra geri-anlatımıyla ölçülür.
- Kutu şablonu: kavram (alt hedef etiketli) · kusur (önce/sonra) · düzeltme (fading) · doğrulama (kırık pointer kontrolü) · geri-anlatım · 4 satır mini-ADR (deneysel).

## 3. Ders nesnesi: depodaki 8 düzeltme (salt-okur denetim 2026-10-31; sayılar komut çıktısından)
1. `friday/.DS_Store` izleniyor → `git rm --cached` (gitignore izlenen dosyayı kapsamaz). md.14.
2. `calc/veri/bronz/.gitkeep`, `span/veri/bronz/.gitkeep` + `deci|sage|vega/veri/bronz/hareket-olay.jsonl` takipsiz, 4 ajanda izleniyor → commit. md.1, md.5.
3. `projects/portal-parkur/{.godot,test_cikti,referans}` (165 MB, 8 iç `.git/`) → `.gitignore`. Ürün = ayrı repo kararı.
4. 4 kırık Python pointer'ı (`jarvis/CLAUDE.md` §2-3 ×3, kök `AGENTS.md` ×1) → Rust adı; Katman-1, Salih imzası. md.7, Karar 118 M2.
5. Boş `jarvis/kuyruk/arsiv/` + 3 `.DS_Store` → Salih eli siler; m.8 "boş klasör kayıt değil" sınırı.
6. `jarvis/cc/` kökünde 2 `.py` + 2 `.md` → `git mv` (`arsiv/kod/python/`, `cc/rapor/2026-08/`). Plan parti 3.
7. 22 birleşmiş worktree (hepsi `--merged main`, behind 62-151) → `git worktree remove` + `git branch -d`; Salih beyanı. md.14.
8. `jarvis/CLAUDE.md` §7'ye `kod/ lean/ mods/ graf/ paylasim/`; kök `AGENTS.md`'ye `arsiv/kod/` + Rust workspace pointer'ı; 5 README eksiği (`core kod lean paylasim` + kök `bin sablonlar projects gunluk arsiv`). §8 bütçe içinde.

Ek bulgular: kök `veri/hafiza-ayna` boş manifest (hafiza-ayna yanlış anahtar) · `jarvis/CLAUDE.md` symlink jarvis kökünde yok, harness `AGENTS.md` okuyor `[?]` · en derin dizin 8 seviye `cc/devir/friday-2026-09-09-parti5/…` · `kaynak-kodu/no-mistakes` depo dışı mutlak symlink · alan ajanı `ogrenme/` 7'sinde gerçek dizin, symlink değil.
