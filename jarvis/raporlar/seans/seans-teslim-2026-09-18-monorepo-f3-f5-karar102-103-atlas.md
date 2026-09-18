# Seans teslimi — 2026-09-18 seans-3 (Fable ana-sıra, ~14:40 → ~19:4x): monorepo F3-F5 · Karar 101 EK-2 / 102 / 103 · iki Atlas koşumu · masa-15/16/17

*Şablon `core/sablonlar/seans-teslim.md` (beş soru). Rakamlar git log + bildirim sayaçları; deneysel m.29. Yüzey: Claude Code masaüstü, cwd `~/sistem/jarvis`, worktree kapalı. Açılış hedefi: "F4 kanon paketini masa-15 olarak hazırlamak" → `TUTTU` ve aşıldı (F5 + iki Atlas + masa-16/17).*

## 1. Bugün gerçekten ne değişti
- **Monorepo geçişi bitti (Karar 101 F2-F5):** Salih eli F2 (1.318 dosya `jarvis/`, subtree Friday, GitHub `sistem`); F3 yol düzeltme (yol-tasi 31 dosya + 7 elle; hook'lar Jarvis 14/14, Friday v0.5 34/34; gitignore ayrımı; K1 `git rev-parse` + alan sütunu); F4 kanon paketi (masa-15 (a) + 2 not: kök `AGENTS.md` v0.1 Kun Chen harmanlı 22 satır, `CLAUDE.md` symlink'leri, `jarvis/AGENTS.md` v3, `friday/AGENTS.md` v0.3, tüzük EK-2, protokol EK-4, kök `sablonlar/`, `bin/hook-dispatch.sh` çift-koşum frenli); F5 kanıt: Friday bağlamına yüklenen kanon = global + kök + friday, Jarvis satırı 0.
- **Karar 102:** literatür-önce; model-sürümü damgası zorunlu; Karar 91 EK-2'ye (d) ölçütü.
- **Atlas 1/2 perspektif partisyonu:** 4 aile, 48 iddia, 33/8/7; hüküm: yalnız hakem ayrılmalı (D); refactor tek iş-parçacığı (D); öğretim/antitez/planlama belirsiz; alt-ajan ≠ kalıcı ajan (kalıcı = dizin); 4 m.16 çelişki.
- **Karar 103 (masa-16, 5/5):** hakem kalıcı ajan · eskalasyon deseni (Karar 89 revize) · tek-yazar kuralı · **alan ajanı = kalıcı dizin, öğrenme + ürün aynı ajanda** (Karar 93 M7-1 süpersede) · Friday tur-6 paketi + yanlış-pozitif sayacı.
- **Atlas 2/2 hafıza mimarisi:** 3 aile, 36 iddia, 27/7/2; eşleme 4 korunmalı · 2 eklenmeli · 1 değişmeli (kapsül sessiz-düşme) · 1 belirsiz; insan onayı getirisi literatürde ölçülmemiş.
- Masa-17 hazırlandı, Salih bakmadı, kapatıldı (kalıcı kopya duruyor).
- Yan: Friday `seans-acilis` 4. adım düzeltildi; hafıza dizini kaydı güncellendi; öğrenme yan oturumu (baglam şeridi) yeni düzende worktree açık, branch `origin/main` ile eşit çalıştı.

## 2. Hangi karar verildi
Karar 101 EK-2 (F4 paketi, masa-15) · Karar 102 (sohbet, aynen alıntı) · Karar 103 (masa-16). Kaynak/gerekçe/geri-açma defterde. Geri-açma: Karar 101 → Friday bağlamında Jarvis satırı > 0 (F5: 0); Karar 103 M4 → ilk alan ajanı (`guvenlik/`) 2 derste öğretim kalitesinde sapma.

## 3. Aday kalan fikirler (karar değil)
Masa-17 dört kalemi · Friday modeli (a/b/c) · PR ölçütü "yapan ≠ onaylayan" tek cümle (Salih: henüz kalıcı değil) · eskalasyon dersi `ogrenme/` kaydı · Kun Chen 27 satır tam metni harmanı.

## 4. Sonraki ilk iş
Masa-17 hükümleri → Karar 103 icra borçları sırayla: İB-108 hakem ajanı → eskalasyon kuralı → tek-yazar satırı → `guvenlik/` alan ajanı charter'ı → tur-6 emri. Yan oturum baglam şeridi PR'ı gelince merge (ana-sıra).

## 5. Yeniden-açma koşulu
Friday hook yanlış-pozitif oranı ≥ %20 (3 tur) → ayrıştırıcı revize · dispatcher çift-koşum gözlenirse F5 tekrar · kapsül sessiz-düşme freni öncesi düşen madde kaybı gözlenirse M1 acil.

## Ölçümler
- Commit: 14 (`2e13dc4` → kapanış); push'lu: `2600872`, `499337c`, `afb05c6`, `569d41a`, `9b0df02`; bekleyen 5 + kapanış.
- Ajan koşumları: 18 alt-ajan (2 Atlas) · ≈1,56M alt-ajan token · ≈72 dk; tahmin↔gerçek: 1/2 tahmin yok (ilk), 2/2 tahmin 600-900k/25-35 dk → gerçek ≈700k/≈40 dk (süre +14%).
- Hasat kontrol listesi (§6e): (1) kural adayları ingest'te (defter Karar 102/103, masa-17 spec) · (2) açık pipeline yok; Friday tur-6 "sahada değil, emir bekliyor" · (3) tahmin↔gerçek bu raporda (ambar satırı: bkz. kosum-maliyeti) · (4) paralel oturum: Friday (16:07 açık, çakışma 0) + baglam yan oturumu (branch, çakışma 0).
- Araç-çıktısı aşımı: yok (alt-ajan dönüşleri ≤1,5k).
- Boyut-tetiği: defter 97 KB+ / 48 KB (aşım, önceki seanslardan; damıtma adayı) · jarvis AGENTS.md 7.184 B / 7 KB (16 B).
- Diğer kapı satırları aşağıda eklenir (hareket, skill-eşik, silver-sağlık, bayat-çekim, kural-sayacı, test, bağlam-seyri).

## Kapı satırları (kapanış koşumu ~19:5x)
- hareket-tablo: `PASS` (bugünün günlüğü `raporlar/hareket/hareket-gunlugu-2026-09-18.md`).
- skill-esik: 6 çift · yeni-pencere sapması 0 (atlas-kosum × Sonnet n=47, medyan 8.957 tok / 188 sn).
- bayat-çekim: kuyruk 0 · çekilen 0/3.
- silver-sağlık kapısı: çıkış 0 · `WARN` 1 (yetim aday 514 > eşik 351) · aday: kapandı-tarihçe 107, T-A ön-eleme 500/9.425; Salih triyajı.
- kural-eşiği: **119** (eşik 100; jarvis md + 5 skill) → damıtma tetiği.
- bağlam-seyri: bu oturumun satırı henüz silver'da değil (transkript kapanışta yazılır); önceki seans 09-15: max 507k, 128k+ 281 tur. Bu seans uzun-koşum sınıfı (iki Atlas + masa); hasat kontrol listesi yukarıda.
- test-kapısı: 130 test · `FAIL` 0 · skip 7.
- katman-hatti: 15 `PASS`; K3 `TAZE`.
- Workflow koşumu: yok (Agent aracı kullanıldı; script kopyası gerekmedi).
- boyut-tetiği: kapsül 11,2 KB / 8 KB (28 satır ≤ 40) → FIFO/damıtma ilk boş seans (masa-17 M1 ile birlikte).
