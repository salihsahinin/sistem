# ogrenme/ — Öğrenme Oturumları Şeridi (Şerit 2; deneysel m.29)

> **Açıklama notu:** Salih emri 07-15 günaydın: "cowork öğrenme oturumlarım olsun — araştırma sonucu en çok öğrenmem gereken konuları önce baştan sona 0'dan anlatan, sonra sistemimizde nasıl kullanacağımıza dair 3 farklı model sunan (birini önererek) bir sistem; konular uygun partisyonlarla." Şerit tanımı: `raporlar/paralel-yapilanma-plani-2026-07-15-v2.md`. Format deneysel — ilk 2 oturumdan sonra kalibre edilir.

## Yapı
- `mufredat.md` — partisyonlu müfredat (kaynak: Atlas raporu `cc/rapor-2026-07-15-1.md`, Carvis damıtır). Partisyon = 1 oturum (1,5–3 saat), bağımlılık-sıralı, her birinin DONE'u yazılı.
- `dersler/YYYY-MM-DD-partisyon-adi.md` — oturum başına ders kaydı.

## Oturum protokolü → `ogren` skill'i (İB-89, 2026-09-15; Karar 96 M2 A2)
Öğrenme yan-oturumunun tamamı `.claude/skills/ogren/SKILL.md` v0.2'dedir: açılış (kurs README + `ilerleme.md`) → `PROBE` → `PLAN` DAG → `TEACH` kutu (sektör başlığı AS-OF; pratik = Salih'in eli, `DONE` yalnız Salih beyanıyla) → `CLOSE` (ders kaydı + ilerleme + branch commit + PR, Karar 95). Tetik: "seans başı, <şerit>" (sade "seans başı" ana-sıra ritüelidir). Seri sonu ürün turu usulü `.claude/skills/ogren/references/urun-turu.md` (Karar 94 EK-1..4; Salih beyanları aynen defterde). Eski format v2 protokol metni (07-15 → 09-15, adım 0-6) `arsiv/ogrenme-oturum-protokolu-v2-2026-09-15.md`. Sabit frenler `.claude/rules/ogrenme.md` (yalnız `ogrenme/**` ile yüklenir).

## Matematik kuralı (Karar 73, Salih Katman-1, 2026-08-29)
- Her öğrenme dersinde **en az 1 matematik-bağlantılı içerik** bulunur; yeni öğrenme deseni/metrik **formülüyle** yazılır (tanım + sembol tablosu + elle işletilmiş sayısal örnek). Kanon gövdesi: [core/varlik-felsefesi.md](../core/varlik-felsefesi.md) §2.
- Kurs şeritleri bu klasörün altındadır: [baglam-modelleme/](baglam-modelleme/README.md) (bağlam penceresinin matematiksel modellemesi, 11 kutu / 5 seri DAG, Salih emri 09-18, tetik "seans başı, baglam") · [guvenlik/](guvenlik/README.md) (ajan güvenliği, 6 hafta, Karar 94 EK-3 09-14, tetik "seans başı, guvenlik") · [evals/](evals/README.md) (LLM/ajan değerlendirme mühendisliği, 7 hafta, Karar 94 M2 09-11, tetik "seans başı, evals") · [mit-6006/](mit-6006/README.md) (MIT 6.006 birebir kursu; BK-1) · [mit-6042j/](mit-6042j/README.md) (MIT 6.042J ayrık matematik, birebir + "neden" görevi; BK-2 — 6.006'nın ön-koşulu) · [mat-felsefesi/](mat-felsefesi/README.md) (matematik felsefesi serisi).

## Sınırlar
- Bu şerit kanon/kural değiştirmez; çıktısı ders kaydı + karar adayıdır.
- Öğretme akış-modu kuralına tabi: Salih akıştaysa teori ertelenir, iş bitince dönülür.
- Müfredat güncellemesi (partisyon ekleme/çıkarma) Atlas koşumu ya da Salih emriyle; sıra değişikliği Carvis Katman-2.
- [problem-cozme/](problem-cozme/seri-tasarimi-v1.md) — problem çözme eğitim serisi v1 (2026-09-09; 9 başlık A-I × L0-L3, AI-çağı öncelikli, §5 AI kuralı: çözümde AI kapalı, tutor/doğrulama modu; v0 arşiv-pointer; gerekçe Atlas 09-09).

> **Ad eşitliği (Karar 93, 2026-09-10):** bu dizindeki tarihli dosyalarda geçen **Carvis = Jarvis** (Salih'le konuşan ajanın 09-10 öncesi adı); sistem/repo kastedilirken "depo"/"kanon". Halef-sözlük: `core/baglam-anahtar-kaydi.md` anahtar `carvis-rol-adi` → `jarvis-ajan-adi`.

> **Karar 105 (2026-09-21):** öğrenme şeritleri alan ajanlarına taşınıyor (T3 Salih eli, `git mv`): `evals/` (Turing) · `guvenlik/` (Saltzer) · `baglam/` (Shannon; eski `dersler/` → `baglam/ogrenme/dersler-2026-07/`) · `hesaplama/` (Euler; mit-6006 + mit-6042j + mat-felsefesi). Bu kökte kalan: `kaynaklar/` (ortak, alan ajanlarına salt-okur) · `problem-cozme/` · `mufredat.md` · `anlama-kapisi.md` · `loop-eng-yol-haritasi.md` (Jarvis öğretim-tasarımı). Ders iskeleti Jarvis'ten `<alan>/cc/gelen/ders-<hafta>.md` ile gider.
