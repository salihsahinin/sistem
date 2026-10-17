# Durum Kapsülü

*Her oturumun **ilk** okuduğu dosya. Üzerine yazılır; arşiv değildir. Bütçe ≤8 KB / ≤40 satır. FIFO (İB-80; Karar 104 M1): aşımda en eski madde `arsiv/kapsul-YYYY-MM-DD.md`'ye iner (silme yok) ve buraya tek satır **kesildi:** bildirimi düşer. **Karar 113 M2 (10-14):** açık iş artık burada değil, `ortak/durum-olay.jsonl` kütüğünde; bu dosya geçiş dönemi pointer'ıdır.*

**Güncelleme:** 2026-10-14 seans-10 `KAPANDI` (Opus 5.5, Salih tam yetki; 10-09 → 10-14). Kod tabanlı sistem: Lean + Rust + ortak durum kütüğü (Karar 112 EK-2 + Karar 113). Teslim `raporlar/seans/seans-teslim-2026-10-14-kod-tabanli-sistem.md`.
**kesildi (10-14):** Karar 112 v0 · seans-7/8 (Karar 106-111) · Windows devri · bitirme tezi Atlas · eski "Sonraki ilk iş" 0-4 → `arsiv/kapsul-2026-10-14.md`. Önceki: `arsiv/kapsul-2026-10-09.md` · `arsiv/kapsul-2026-09-28.md` · `arsiv/kapsul-2026-09-22.md`.

## Şu an
- **Karar 113 (10-14) kod tabanlı sistem:** kural = Lean 4 spec (`lean/`), çalışan kod = Rust (kök `Cargo.toml`; crate'ler `kod/skill-kapi` · `kod/durum` · `kod/hook`); md bağlama girmez, rapor md'si kalabilir. Ajanlar mesaj yazmaz, `ortak/durum-olay.jsonl`'deki kendi alan kaydından iş türetir (`durum oturum-basi --alan <ajan>`). Her sohbet kendi dalı + PR, birleştirme Salih. Test oranı düşer (metinler durum #5). Pilot ajan Sage (durum #2).
- **Ortam:** Herdr 0.9.4 + OMP 18.10.4 (`C:\tools\omp\omp.exe`; Herdr penceresi AppData'yı görmüyor → durum #8). Jarvis ve ajanlar Herdr çalışma alanlarında; worktree'ler `C:\sistem\wt\`. `gunluk/` günlük kısa-soru yüzeyi.
- **Karar 112 EK-2:** paket seçimi ana modelde, niyet başına (`tools/paket-yonlendir.py --sec`), cevap sonunda `[paket]` etiketi; Salih düzeltmesi `--duzeltme`.

## Açık borçlar
- **Salih el işleri:** iç içe klasör taşıma · Markdown Preview Enhanced · bitirme tezi kararı (ertelendi) · Jev waitlist · LinkedIn metinleri · deney tasarımı `PROBE` soru 1 · veri bilimi şeridinin evi.
- **Boyut:** defter 70+/48 KB aşım (damıtma) · jarvis AGENTS.md 7.167/7.168 · memory 4.006/4.096.
- **Mekanik:** Friday hook v0.6 + tur-6 emri (Karar 103 (5)) · Python → Rust kalanı ≈13,4M token `[?]`.

## Sonraki ilk iş
0. Kökte `target/release/durum.exe oturum-basi --alan jarvis` (yoksa `cargo build --release -p durum`); kayıt #8 → #1 → #2 sırası.
1. Seans hedefi yoklaması: 10-09 hedefi raporlar `TUTTU`, öğrenme konusu seçildi ama ders `PROBE`'da kaldı → kısmi.
