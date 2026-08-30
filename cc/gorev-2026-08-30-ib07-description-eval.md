# Görev Emri — İB-07: Description-eval tam koşumu (K-016 borcu; KB-20 kapanış girdisi)

*Derleyen: Carvis ana-sıra (Fable), 2026-08-30 karar-masası oturumu. Tetik: Karar 83 E2 (Salih imzası 08-30: "ikisini sıradaki icra oturumuna emirle"). Koşum yeri: sıradaki icra oturumu; bu emir HAZIRLANDI, KOŞULMADI.*

- **Görev / hedef:** 16-skill hazinesinin description alanlarının tetikleme doğruluğunu ölçmek: 20 sorgu × 3 tekrar × 14 skill (ritüel-dışı hazine) — her sorguda "hangi skill tetiklenmeli" altın etiketi ile modelin seçtiği skill karşılaştırılır; sonuç = skill-başına P/R + karışan çiftler tablosu.
- **Girdi:** `.claude/skills/*/SKILL.md` description alanları (kaynak tek: hazine) · altın sorgu seti `veri/sozlesme/description-eval-sorgular.json` (YOKSA ilk adım: 20 sorguyu Carvis türetir — skill başına ≥1 pozitif + 6 negatif/sınır sorgu; dosyaya yazılır, deterministik yeniden-koşum için sabitlenir).
- **Yöntem (deterministik çatı):** her (sorgu, tekrar) → işçi ajana YALNIZ sorgu + 14 description verilir (skill gövdesi verilmez); işçi tek alan doldurur: `secilen_skill: ad ∨ HİÇBİRİ`. Harness karşılaştırır, kütüğe yazar (`veri/description-eval.jsonl`, append; koşum kimliği ts).
- **İzinli aksiyonlar:** Read (hazine + sorgu seti) · Agent/Workflow işçi çağrıları · kütük yazımı. **Yasak:** description DEĞİŞTİRMEK (ölçüm turu; değişiklik önerisi rapora, icrası ayrı commit + skill-kapisi).
- **Koşucu sınıfı (#24):** işçi Haiku 4.5 ∨ Sonnet 5, effort düşük, araçsız tek-alan dönüş (≤200 token); −%30 rejimi `[rejim: maliyet-öncelikli]`.
- **Maliyet tahmini (yalnız işçi; m.29 kaba):** 60 işçi çağrısı (20×3) × ~3-5k girdi + ≤0,2k çıktı ≈ **200-320k işçi-token** `[?]`; ana-sıra maliyeti yazılmaz (Salih 08-29 kuralı).
- **Durma koşulu (done-yüklemi):** kütükte 60 satır ∧ skill-başına P/R tablosu yazıldı ∧ karışan-çift listesi (n≥2 karışma) çıkarıldı ∧ KB-20 kapanış önerisi tek paragraf.
- **Teslim:** `raporlar/2026-08-30-ib07-description-eval.md` (tablo + karışan çiftler + öneri; her rakam kütük satırından).
- **Emir konumu + erişim (m.46a):** `cc/gorev-2026-08-30-ib07-description-eval.md` · main · koşum anındaki HEAD künyeye yazılır.
