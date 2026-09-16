# Durum Kapsülü — Friday

*Her oturumun İLK okuduğu dosya. SICAK katman: üzerine yazılır, arşiv değildir. Bütçe ≤4 KB / ≤20 satır. FIFO: "Şu an" listesi en fazla 8 madde; 9. madde girince en eski `arsiv/kapsul-YYYY-MM-DD.md`'ye iner (silme yok). Tarihçe `raporlar/` + git log.*

**Güncelleme:** 2026-09-16 tur-3 — A1 formatının (md + lojik blok) ilk canlı koşumu bitti: S2 kapandı, kilit alt-ajan incelemesi, tasarım tur-3. İşçi 0, emir-kaynaklı sapma 0, Jarvis'e yazım 0.

## Şu an
- Tur-3 bitti (`cc/giden/devir-2026-09-16-tur3/`): S2 **D** — Read yol-bazlı deny belgeli; Bash'te Read deny tanınan dosya komutlarını kapsıyor, `Bash(...)` kuralı güvenlik sınırı değil. Tek satır `Read(~/jarvis/**)` symlink yüzünden `kanon/`'u da keser; işleyen biçim alt dizin listesi (kural adayı).
- C2: `okuma-izin.sh` `agent_id` okumuyor; yol kilidi işçide de tetiklenir (D), işçiye özgü dar alan yok (K). Statik zayıflıklar Z1 (Bash dalı Jarvis inkâr listesi, izin listesi değil) · Z2 (`cd` + göreli) · Z3 (dize kurgusu); öneri Ö1: test vakası, koşumu Jarvis'te.
- Tur-2 cevabı uygulandı (1380c7a): kütük v0.3 · A1 format · 301 ve 1-derinlik kuralları · FIFO'da madde birincil.
- Geçiş ölçüsü (emir-kaynaklı sapma/devir): 2 · 1 · 0 → A1 → A2 için 1/2.
- Açık, Salih/Jarvis'te: `.aktif-devir` oturum-devam hâlinde yazılmıyor (b1) · Friday git akışı Karar 95 ile ayrışıyor (b3) · Ö1–Ö4 · C1 §3b deny listesi.
- Kütük: v0.1 satırları denetim dışı; v0.3 ayrıştırıcısı komuttaki desen dizesini yol sanabiliyor (`/docs/en/`).
- Koşum sayacı 3/10 (desen yeniden-oluşumu 10'da).

## Sonraki ilk iş
0. `cc/gelen/tasarim-2026-09-16-tur3-cevap.md` gelince oku; hükümlere göre öneri notunu `cc/giden/`e yaz (`.claude/`, `settings.json` ve şemalara dokunma).
