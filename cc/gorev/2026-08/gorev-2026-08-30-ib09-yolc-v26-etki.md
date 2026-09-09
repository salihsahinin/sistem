# Görev Emri — İB-09: Yol-C V26-yakalama etkisi ölçümü (opus/sonnet pin kararına girdi)

*Derleyen: Carvis ana-sıra (Fable), 2026-08-30 karar-masası oturumu. Tetik: Karar 83 E2 (Salih imzası 08-30). Koşum yeri: sıradaki icra oturumu; bu emir HAZIRLANDI, KOŞULMADI.*

- **Görev / hedef:** V26 kural-tabanlı denetimin (birincil-kaynak sondajı) yakalama gücü hakem MODELİNE ne kadar bağlı: aynı denetim girdilerinde Opus-5 ↔ Sonnet-5 denetçi çiftinin yakalama farkını ölçmek; çıktı, işçi-model pin kararının (opus/sonnet) girdisidir.
- **Girdi (yeniden-koşum, yeni araştırma DEĞİL):** geçmiş V26 koşum dosyalarından örneklem — `cc/rapor-2026-08-29-ib63-atlas-*.md` + `cc/rapor-2026-08-29-ib53-atlas-v26-*.md` sınıfından, bilinen-sonuçlu ≥2 vaka (İB-63'te antitez-B K-DÜŞÜŞ yakalanmıştı = pozitif kontrol; tez-tarafı 8/8 PASS = negatif kontrol).
- **Yöntem:** her vaka × {Opus-5, Sonnet-5} denetçi → aynı V26 talimatı, aynı örneklem kuralı (son-üçlük 1/3); alanlar: `yakalanan_ihlal: liste` · `K_dusus: evet/hayır`. Karşılaştırma tablosu: model × vaka × yakalama; fark satırları tek tek pointer'lı.
- **İzinli aksiyonlar:** Read (geçmiş koşum dosyaları) · Agent işçi çağrıları · kütük `veri/v26-model-etki.jsonl` (append). **Yasak:** web araması (girdi donmuş geçmiş koşumlar) · kanon/pin değişikliği (karar Salih'in).
- **Koşucu sınıfı:** denetçi çifti Opus-5 (effort orta) ↔ Sonnet-5 (effort orta); vaka başına 2 işçi; ≥2 vaka → ≥4 koşum, tavan 8 (fren 36 altı).
- **Maliyet tahmini (yalnız işçi; m.29 kaba):** 4-8 denetçi koşumu × ~20-40k ≈ **150-300k işçi-token** `[?]`.
- **Durma koşulu (done-yüklemi):** ≥2 vaka × 2 model kütükte ∧ pozitif kontrol (K-DÜŞÜŞ vakası) her iki modelde etiketlendi ∧ fark tablosu + pin-kararı girdi paragrafı yazıldı.
- **Teslim:** `raporlar/2026-08-30-ib09-yolc-v26-etki.md`; pin hükmü YOK (Salih'e girdi, m.31).
- **Emir konumu + erişim (m.46a):** `cc/gorev-2026-08-30-ib09-yolc-v26-etki.md` · main · koşum anındaki HEAD künyeye yazılır.
