# Durum Kapsülü

*Her oturumun **ilk** okuduğu dosya. Üzerine yazılır; arşiv değildir. Bütçe ≤8 KB / ≤40 satır. FIFO (İB-80; Karar 104 M1): aşımda en eski madde `arsiv/kapsul-YYYY-MM-DD.md`'ye iner (silme yok) ve buraya tek satır **kesildi:** bildirimi düşer. **Karar 113 M2 (10-14):** açık iş artık burada değil, `ortak/durum-olay.jsonl` kütüğünde; bu dosya geçiş dönemi pointer'ıdır.*

**Güncelleme:** 2026-10-17 seans-11 `KAPANDI` (Opus 5.5; 10-16 → 10-17). Karar 117: hafıza/kanon → Lean/Rust, bağlam sırası korunarak; 14 PR birleşti (#8-#21). Teslim `raporlar/seans/seans-teslim-2026-10-17-karar117-lean-rust-gecisi.md`.
**kesildi (10-17):** seans-10 Şu an/Açık borçlar (Karar 113 özeti, Herdr/OMP ortam notu, Karar 112 EK-2, Salih el işleri listesi) → `arsiv/kapsul-2026-10-17.md` · memory indeksi "Maliyet tahmini yalnız alt-model için" → `arsiv/memory-arsivi-2026-10-17.md` (kural kullanıcı CLAUDE.md'de). Önceki: `arsiv/kapsul-2026-10-14.md` · `arsiv/kapsul-2026-10-09.md`.

## Şu an
- **Kod tabanı (Karar 113 + 117):** kural = Lean 4 (`lean/Kanon/`, 31+ modül), icra = Rust (`kod/` crate'leri, ikililer `target/release/`), Python yedek. Açık iş `ortak/durum-olay.jsonl` (`durum oturum-basi --alan jarvis`).
- **Bağlam sırası (Karar 117):** `@` içe aktarma ebeveynden sonra pre-order (Claude Code 2.1.302 ölçümü B1-B8). Tüzük 29 blok (15 md parçası + Lean); `core/` Lean ekleri; denetim `target/release/baglam denetle <dosya>` (0 ihlal). `Read` → PostToolUse hook'u içe aktarılanları sırayla ekler; Bash'te `baglam genislet`.
- **Kök kanon md kalır**, maddeler Lean'e pointer (EK-1). Tüzük onay kuralı `Edit(core/tuzuk-v0*.md)`.
- **Yan oturumlar:** omp `C:\sistem\wt\omp-rust-p1` (Python → Rust parti 1/7, EK-3) canlı · span öğrenme şeridi `wt/span`.

## Açık borçlar
- **Boyut:** defter 101.796 B / 48 KB (damıtma tetiği) · jarvis AGENTS.md 7.157/7.168.
- **Küçük:** `MDL` kısaltma listesine (Salih onayı bekliyor) · bayat-çekim kuyruğu 4 (0/3 çekildi) · `katman-hatti` `ambar-parquet` adımı: `duckdb` yok (Windows venv kurulmamış; Karar 63) → çıkış 3, silver adımları geçiyor.
- **Aday:** hook kanarya probu · `sema-sikistirma` §1 Rust · `SkillTetik` yasak 1/6/7 · `~/.claude/CLAUDE.md` pointer.

## Sonraki ilk iş
0. Kökte `target/release/durum.exe oturum-basi --alan jarvis`; açık: #9 #15 #19 #20.
1. omp parti 1 PR'ı (8 araç): fark testleri → Türkçe özet → Salih "birleştir #N".
2. Parti 2 worktree + omp prompt (`raporlar/2026-10-17-rust-tasima-plani.md`).
