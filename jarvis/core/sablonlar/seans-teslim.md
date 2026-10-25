# Şablon — Seans Teslim Raporu (eski ad: Seans Teslim Raporu; seans→seans, Salih 08-17)

**Süpersede (Karar 121 + 122, 2026-10-25):** teslim raporu artık md değil, yapılandırılmış JSON kayıt: girdi şablonu `../../../ortak/sablon/seans-teslim-girdi.json`, üretici `durum seans-kapat` (ölçümleri Rust ekler), kayıt `raporlar/seans/seans-teslim-<tarih>-<etiket>.json`, Salih özeti `ortak/SALIH-OZET.md`, graf `ortak/graf/`. Aşağıdaki beş soru JSON alanlarının tanımı olarak kalır (`ne_degisti` · `kararlar` · `adaylar` · `sonraki_ilk_is` · `yeniden_acma`); geçmiş md raporlar arşivde (m.8).

*(Sözlük: oturum kapanışında yazılan tarihli kayıt. Birikimli, arşive gider; durum kapsülü bunlardan damıtılır. Beş soru:)*

- **Bugün gerçekten ne değişti:**
- **Hangi karar verildi (kaynak + gerekçe + geri-açma):**
- **Hangi fikir aday kaldı (karar DEĞİL):**
- **Sonraki ilk iş:**
- **Neyi yeniden açmak için hangi koşul gerekir:**
