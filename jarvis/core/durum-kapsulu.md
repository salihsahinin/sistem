# Durum Kapsülü

*Her oturumun **ilk** okuduğu dosya. Üzerine yazılır; arşiv değildir. Bütçe ≤8 KB / ≤40 satır. FIFO (İB-80; Karar 104 M1): aşımda en eski madde `arsiv/kapsul-YYYY-MM-DD.md`'ye iner (silme yok) ve buraya tek satır **kesildi:** bildirimi düşer. **Karar 113 M2 (10-14):** açık iş artık burada değil, `ortak/durum-olay.jsonl` kütüğünde; bu dosya geçiş dönemi pointer'ıdır.*

**Güncelleme:** 2026-10-18 seans-11 ikinci kapanış `KAPANDI` (Opus 5.5). Karar 118-120 birleşti (PR #22-#25); sistem revizyonu bitti, yön öğrenme → ürün. Teslim `raporlar/seans/seans-teslim-2026-10-18-karar118-120-ogrenmeye-gecis.md`.
**kesildi (10-17):** seans-10 Şu an/Açık borçlar → `arsiv/kapsul-2026-10-17.md` · memory "Maliyet tahmini" satırı → `arsiv/memory-arsivi-2026-10-17.md`. Önceki: `arsiv/kapsul-2026-10-14.md`.

## Şu an
- **Yön (Salih 10-17):** sistem işi yan şeritte (omp + PR kontrolü); seans gövdesi öğrenme → ürün (Karar 94 EK ürün turu). PortRisk ve tek-flagship emekli (Karar 118 M3).
- **Kod tabanı (Karar 113 + 117 + 118 M2):** kural = Lean 4 (`lean/Kanon/`), icra = Rust (`kod/`, ikililer `target/release/`); aynı işin yalnız son sürümü bakımda, Python karşılığı arşive iner (#22). Yeni araçtan önce hazır-karşılık kapısı (Karar 119, kök md.12).
- **Bağlam sırası (Karar 117):** `@` içe aktarma ebeveynden sonra pre-order; denetim `target/release/baglam denetle <dosya>`; `Read` → PostToolUse hook'u sırayla ekler.
- **Yan oturum:** omp parti 2 bitti → PR #26 açık (6 araç). Worktree `C:\sistem\wt\omp-rust-p2`.

## Açık borçlar
- **Boyut:** defter 48 KB tavanı aşık (damıtma tetiği) · jarvis AGENTS.md 7.157/7.168.
- **Küçük:** tel sertleştirme (`sed -i`, `git show >`) · bayat-çekim kuyruğu 4 · `katman-hatti` `duckdb` yok (çıkış 3).
- **Aday:** hook kanarya probu · `sema-sikistirma` §1 Rust · `SkillTetik` yasak 1/6/7.

## Sonraki ilk iş
0. Kökte `target/release/durum.exe oturum-basi --alan jarvis`; açık: #9 #20 #21 #22.
1. **Salih öğrenme şeridini seçer** (#9 veri bilimi/deney tasarımı · `span/` claude-mods · bitirme tezi · yeni konu) → o klasörde "seans başı, <şerit>".
2. Yan şerit: PR #26 kontrol + Türkçe özet → "birleştir #26"; ardından #22 arşiv PR'ı.
