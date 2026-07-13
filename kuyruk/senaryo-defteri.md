# Senaryo Defteri

> m.37'nin operasyonel eki (açılış: 2026-07-13 günaydın, A1c). Ölçek-eşiği üstü her karar bir blok: karar bağlamı + 3 model tahmini + seçim + koşum-sonrası gözlem. Kayıt birimi ayrımı (V39 NİHAİ FORM): SEÇİM = kontrol edilen kısım; 4-tuple (model · token · zaman · kalite) = koşum-başına GÖZLEM satırı — iki bağlı çift: maliyet çifti (token↔zaman) + bilgi çifti (seçim↔gelişim-katkısı). Kalite türetilmiş — credit-assignment olgunlaşana dek boş/tahmini kalabilir (ŞERH 4). Format deneysel damgalı (m.29); görünürlük şerti: her blok Salih'e sunulduğu oturuma işaret eder.

## Kayıt şablonu
### [tarih] · [kart/iş] · karar adı
- **Bağlam:** tek satır.
- **Model A:** ~token · ~süre · beklenen kalite | **Model B:** ... | **Model C:** ... → ✅ öneri + tek satır gerekçe
- **Seçim:** X (kim: Salih onayı / Carvis Katman-2) — görünürlük: hangi oturumda sunuldu
- **Gözlem (koşum sonrası):** token gerçek · süre gerçek · kalite [türetilmiş]
- **Ders:** tek satır (ingest hammaddesi)

---

## Sıfır-noktası — geriye dönük ilk kayıtlar (A1d, 07-13)

### 2026-07-13 · A5 · veri-koşumu sayısı kararı
- **Bağlam:** yeniden-inşa deneyinde koşum sayısı sabit mi, kurallı mı?
- **Model A (sabit 10):** öngörülebilir bütçe · veri-israfı riski (iyileşme durmuşsa boşa koşum) | **Model B (ardışık-deney: pilot 5 [1 referans + 4 tek-nokta değişimi] → 3'erli partiler → devam: son parti >%5 başarı-skoru iyileşmesi → tavan 15):** bütçe-duyarlı, durma kurallı · hafif karmaşıklık | **Model C (iyileşme sürene dek sınırsız):** maksimum veri · V28 bütçe koruması yok → ✅ B
- **Seçim:** B (Carvis, Katman 2 — Salih yetki devri 07-13) — görünürlük: 07-13 oturumu + bu kayıt; eşikler deneysel (m.29), A7 denetimine tabi
- **Gözlem:** henüz koşum yok (tetik: K-009/K-010)
- **Ders:** sabit sayı yerine durma-kuralı = Salih anti-overfit kalıbının (V42) sayısal karşılığı

### 2026-07-13 · hafıza-denetimi · süpürme sınırı kararı
- **Bağlam:** biyoloji-kökenli terimler hafızadan nasıl temizlenir?
- **Model A (tam süpürme + tek pointer):** yoğunluk sıfır · terminoloji çevirisi maliyeti tek seferlik | **Model B (iki-sınıf: teknik kalır, dekoratif gider):** literatür dili korunur · yoğunluk kısmen sürer, tekrar riski kapanmaz | **Model C (pointer'sız tam süpürme):** en temiz · dış-arama anahtarı kaybolur → ✅ A
- **Seçim:** A (Salih, 07-13 günaydın — ilk seçim yanlış-enter, ikinci turda bilinçli teyit)
- **Gözlem:** uygulandı (commit 884d900); kalite gözlemi = sonraki oturumlarda model-düşümü tekrarı olup olmadığı
- **Ders:** hipotez kaydı düştü — düşüm↔hafıza bağı doğrulanmadı; gözlem sütunu bunu ölçecek

### 2026-07-13 · paralel yapılanma · başlangıç tarihi kararı
- **Bağlam:** paralel şerit düzeni (JARVIS + PortRisk + chat) ne zaman başlar? (Salih yetki devri: "başlangıç tarihine karar vermek sana kalmış")
- **Model A (bugün):** erken veri · yarın sınav, bant genişliği bölünür | **Model B (15 Temmuz, sınav ertesi):** tam dikkat, talimat hazır · 2 gün gecikme | **Model C (loop-eng bitince):** olgun başlangıç · PortRisk keyfî gecikir (m.36c ihlal ruhu) → ✅ B
- **Seçim:** B (Carvis, Katman 2) — görünürlük: paralel plan raporu + bu kayıt; chat şeridi bugün, Cowork paralel denemesi 15 Temmuz
- **Gözlem:** bekliyor (15 Temmuz koşumu)
- **Ders:** —
