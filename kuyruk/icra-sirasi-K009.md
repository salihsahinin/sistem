# K-009 İcra Sırası — birleşik kuyruk (2026-07-19)

*(Salih emri: raporlardaki yapılacak/incelenecek kalemleri mevcut işlem sırasına optimize entegre et. Sıralama ölçütü: bağımlılık > geri-alınabilirlik/güvenlik (G4<G5) > kaldıraç. Kaynaklar: K-009 gündemi + rapor 1/3/7/10/12 + süzgeç 07-19.)*

**Dilim 0 — bugün, masada:**
0.1 m.42 imzası (gündem madde 2; taslak `kuyruk/m42-taslak-ajan-yetki.md`) — Salih.
0.2 Ev dosyaları AÇILDI ✓ (skill-kutusu · POP · icra-sırası — bu commit).
0.3 PC senkron `/goal` (2 dk) — Salih terminali.

**Dilim 1 — ilk otomasyon paketi (Karar 1+2 imzalı; hepsi iki-yönlü kapı):**
1.1 PreToolUse kilidi: yazım + test (core/ DENY · push ASK · raporlar/cc/kuyruk ALLOW) — O4.
1.2 SessionStart hook (CC-tarafı) + yetki-banner + CLAUDE.md CC satırı (rapor 3 kararı; aynı paket).
1.3 Kararlı-prefix kapsam KARARI (gündem madde 3) — otomasyon promptları yazılırken alınır (Carvis çerçevesi: sınıf = koşum deseni; Salih onayı).
1.4 JSONL usage-log asgarisi (gündem madde 6; rapor 10 daraltılmış hali — dosya-temelli, panel YOK) — her otomasyon koşumu iz bırakır.
1.5 İlk gözetimsiz dilim: gecelik senkron — mekanizma seçimi m.37 üç-model koşumuyla (gündem madde 4; adaylar Routine / lokal scheduled; karşıt-temel şartlı) → PreToolUse SONRASI canlıya.

**Dilim 2 — köprü + ses (Karar 3 sırası):**
2.1 L2 mobil-köprü protokolü — KILAVUZ 1 sayfa (rapor 1 Adım 0).
2.2 Ses PoC: niyet-yakalama/triyaj kapsamı, ölçümlü (WER+gecikme+görev-başarı → defter) — O2.

**Dilim 3 — skill hattı (K-016; tetik Salih'te — "skill araştırmasına geleceğiz" 07-19):**
3.1 K-016 açılış kararı + ilk skill: S-A karar-modeli (eval-önce akış) → S-B atlas-kosum → S-G karar-hatti.
3.2 "Tekrarlayan-küme→skill" kuralı imzası (imza masası #3).
3.3 Madenleme pilotu (rapor 8; küçük, elle-tetik).

**Dilim 4 — tetikli/bekleyen:**
4.1 Gece-araştırma tek-atış pilotu (PreToolUse-sonrası; sert-bütçe+tur-tavanı freni) — rapor 12.
4.2 İmza-masası kalemleri #2-#6 (tüzük oturumu; süzgeç raporu listesi).
4.3 Kitap kararı (PI önerisi) — Salih, acele yok.
4.4 K-019 boş vardiya (O14) · K-010 tasarım paketi (held-out şartlı, rapor 15) — kendi tetiklerinde.
