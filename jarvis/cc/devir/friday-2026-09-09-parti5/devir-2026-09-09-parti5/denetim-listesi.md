# Çelişki / tekrar denetim listesi — parti 5 (AS-OF 2026-09-09)

Friday mevcut README'leri OKUYAMAZ (Karar 91, okuma-izin hook'u); envanter yalnız **varlıklarını** ve kök README + KILAVUZ başlıklarını verir. Aşağısı bu yüzden *denetim iddiası* değil, **Fable'ın yerleştirmeden önce bakması gereken noktalar** listesidir. Her satır: risk → kontrol.

| # | Risk | Nerede | Kontrol (Fable) |
|---|---|---|---|
| 1 | Klasör haritası tekrarı | `KILAVUZ.md` yeni bölüm ↔ kök `README.md` | Bölüm "ne var" demiyor, "hangi soruya hangi dosya" diyor; harita satırı yok — doğrula (D3). |
| 2 | Üst README ile ay README çakışması | `cc/gorev/README.md` ↔ `cc/gorev/YYYY-MM/README.md` | Üst README zaten ad desenini tanımlıyorsa ay README'sindeki "ad deseni doğrulanmadı" cümlesi ÇIKARILMALI. |
| 3 | Aynısı rapor tarafında | `cc/rapor/README.md` ↔ `cc/rapor/YYYY-MM/README.md` | Aynı kontrol; ham/insan-yüzü ayrımı iki yerde farklı tanımlanmış olabilir. |
| 4 | Aynısı teslim tarafında | `raporlar/README.md` ↔ `raporlar/YYYY-MM/README.md` | Üst README "vardiya-teslim-* ad cascade'i sürüyor" diyor; ay README'lerinde `YYYY-AA-GG-<konu>.md` yazdım — cascade hâlâ sürüyorsa üst metinle uyumlanmalı. |
| 5 | Ritüel adı | 9 README'nin "Üretici" satırı | "seans/vardiya kapanış ritüeli" yazdım; Jarvis'te ritüelin kanonik adı farklıysa tek sözcük düzeltmesi yeter. |
| 6 | Parti numarası atfı | ay README'lerinin "Üretici" satırı | `cc/*` için parti 3, `raporlar/*` için parti 4 dedim (envanter başlıklarından); plan dosyası başka diyorsa düzelt. |
| 7 | Tüzük yolu | KILAVUZ bölümü tablosu | `core/tuzuk-v0.md` yazdım (kök README'ye göre); Jarvis'te yol değiştiyse tabloyu güncelle. |
| 8 | Bütçe | `KILAVUZ.md` | Bölüm 1.185 B; KILAVUZ 13,5 KB + bu = ~14,7 KB < 16 KB tavanı (envanterdeki rakamlarla). |
