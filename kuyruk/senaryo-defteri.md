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

### 2026-07-13 · K-017/K-018 · bilgi-açığı kapama sırası
- **Bağlam:** dispatch + remote control 07-13'te tesadüfen öğrenildi; sistematik yeni-özellik taraması yok — geri-dönüşü pahalı açık (Salih tespiti, 2. oturum).
- **Model A (tarama önce: K-017 CC koşumu → sonra Model-A paketi):** ~1 CC koşumu + 1 inceleme oturumu · kalite 8/10 — sonraki araç kararları tam bilgiyle | **Model B (araçları hemen kur, tarama sonra):** hızlı · körü körüne benimseme riski, dispatch↔K-009 çelişkisi çözümsüz | **Model C (hepsini 15 Tem sonrasına ertele):** sıfır maliyet · açık büyür → ✅ A
- **Seçim:** A (Salih, 07-13 2. oturum — "bu iş bitince model a da yapılacaklar listesinde") — görünürlük: aynı oturum + bu kayıt
- **Gözlem (koşum sonrası):** koşuldu 07-14 — 70 bulgu (58/12/0), ~2,4M token · ~8,5 dk · 78 ajan; **konfig: Fable ultraworkflow (en yüksek efor, Salih beyanı — ilk koşum bilinçli maksimum; token gözlemi efor-parametreli okunur)**; kalite [türetilmiş]: yüksek — 12 hata doğrulamada yakalandı, adaylar panoya dağıtıldı
- **Ders:** bilgi-açığı sınıfı karar = araştırma-önce (m.40b); tarama tek-seferlik değil tekrar eden ihtiyaç — periyodik tarama kararı K-017 inceleme oturumuna aday

### 2026-07-14 · P0-P6 · partisyon planı onayı
- **Bağlam:** 07-14 kapanışında sunulan kronolojik partisyon planı (P1=15 Tem paralel · P2=16-20 Tem K-015+K-018 · P3=otonomi kapısı ~Ağu başı · P4=ölçüm+deney Ağu · P5=Jarvis v1+demo ≤10 Eki · P6=K-004 Kas) karar masasında.
- **Seçenekler:** olduğu-gibi onay | onay + P5 minimum-demo sabitlemesi (kayma riskine karşılık) | revizyon | veto → ✅ onay + sabitleme
- **Seçim:** Salih (07-14 sabah, Katman 1 — yön kararı): "kronolojik partisyon" çerçevesi teyit + önerilen sabitleme kabul. Plan dosyası: `raporlar/partisyon-plani-P0-P6-2026-07-14.md` (ilk sunumda dosyaya inmemişti — kalıcılık dersi orada kayıtlı).
- **İlk tahminler (deneysel damga, m.39 — Brier için):** P1 DONE-tanımıyla kapanır: 0.80 · P2 20 Tem'e dek kapanır: 0.65 · P3 kapısı Ağu ilk haftasında açılır: 0.60 · P5 minimum demo ≤10 Eki: 0.60
- **Gözlem:** her partisyon kapanışında tahmin-vs-gerçek buraya.
- **Ders:** kritik sunum, sunulduğu vardiyada dosyaya iner (V43 ailesi — kapsül özeti tek başına kalıcılık değildir).

### 2026-07-15 · şerit düzeni · öğrenme şeridi + öncelik revizyonu (P1 yeniden şekillendi)
- **Bağlam:** Salih günaydın emri: öğrenme oturumları şeridi + PortRisk 3. öncelik + Atlas'la müfredat araştırması. m.16 çelişki raporu sunuldu (P1 B-kanadı boşa düşer + P4 ölçüm girdisi gecikir, kritik yolda tampon yok).
- **Seçenekler:** PortRisk bugün yine açılır (P1 aynen, ✅ Carvis önerisiydi) | B kanadı öğrenmeye devredilir | Carvis'e devir → Salih üçüncü yolu seçti: "birkaç gün odak sadece öğrenme + Jarvis; ölçüm bankı önemli olmaya başlayınca 3. oturum olarak tasarlanır."
- **Seçim:** Salih (Katman 1 — yön kararı; 07-15 günaydın oturumu). P1 revize: ilk paralel deneme JARVIS+öğrenme çiftiyle, tetik = müfredat DONE. Plan: `raporlar/paralel-yapilanma-plani-2026-07-15-v2.md`. Kabul edilen risk: P4 itilmesi (kayıtlı).
- **Gözlem:** bekliyor (ilk JARVIS+öğrenme paralel günü + P4 açılış tarihi).
- **Ders:** öneri reddi de veridir — Salih odak-bölünmesini P4 riskinden pahalı fiyatladı; Brier notu: P1 "DONE-tanımıyla kapanır: 0.80" tahmini eski DONE-tanımıyla ölçülemez, revize DONE ile ölçülecek.

### 2026-07-15 · Atlas ilk koşumu · efor seçimi (Salih devri: "effort seçmek sana kalmış, bence yüksek")
- **Bağlam:** müfredat araştırması Opus'la koşulacak (Salih beyanı: token maliyeti); efor kademesi Carvis'te.
- **Model A (orta):** ~400-700K token · ~4-5 dk · kalite 6/10 — müfredat iskeletde kalır, kaynak derinliği zayıf | **Model B (yüksek):** ~1-1,5M token · ~6-8 dk · kalite 8/10 — eksen genişletme (Wave) + örneklem-denetim rahat çalışır | **Model C (maks/ultraworkflow):** ~2M+ token · ~8-10 dk · kalite 8,5/10 — K-017'de marjinal getirisi doğrulama katmanındaydı, o da artık örneklemli → ✅ B (maliyet/kalite dizi; Salih sezgisiyle uyumlu)
- **Seçim:** B — yüksek (Carvis, Katman 2) — görünürlük: 07-15 günaydın oturumu + görev emri `cc/gorev-2026-07-15-1.md`.
- **Gözlem (07-15, koşum sonrası):** süre ~25 dk · 13 ajan (K-017'nin 78'ine karşı) · token toplamı raporlanmadı (/usage istenmedi — ders) · kalite [türetilmiş]: yüksek — 0 DOĞRULANAMADI, 9 KISMEN düzeltmesi yakalandı, 19-partisyon müfredat kullanılabilir çıktı; Model B tahmini (8/10) tutarlı görünüyor, token kolonu boş kaldığı için maliyet çifti doğrulanamadı.
- **Ders:** fan-out'u ucuz modele (sonnet), sentez/denetim kararını pahalıya (Opus) veren iç-routing CC tarafında kendiliğinden doğru kuruldu — m.28/V39 routing ilkesinin dış teyidi; görev emri şablonuna /usage-raporu satırı eklenecek.

### 2026-07-15 · K-015 madde 3 / loop-eng Faz 4 · ilk Routine mekanizma seçimi
- **Bağlam:** Faz 2+3 kapandı; Faz 4 = ilk Routine. Homebase emekli → eski hedef (transkript pipeline) bayat. m.40b dış araştırma YAPILDI (code.claude.com/docs/routines): Routine bulutta koşar (PC kapalıyken de), repoyu GitHub'dan klonlar → lokale yapısal olarak DOKUNAMAZ, push varsayılan yalnız `claude/`-önekli dallara — "mimari > talimat" hazır örneği.
- **Model A (kalıcı günlük sabah-brifingi Routine):** ~15-30K token/gün · kurulum ~15 dk · kalite orta (yalnız origin'i görür, V43 yakalayamaz) · RİSK orta (kalıcı gözetimsiz koşum K-009 sınırına komşu) | **Model B (lokal scheduled task — gerçek-ağaç V43 nöbetçisi):** ~10-20K/koşum · kalite yüksek · RİSK yüksek (gözetimsiz lokal yazma = K-009'un kendisi; bugün açılmaz, K-009 açılış adayı) | **Model C (öğrenme-amaçlı: kur → 1 otomatik koşu gözle → duraklat / tek-seferlik):** ~15-25K tek koşum · ~30 dk toplam · kalite: Faz 4 DONE tam karşılanır · RİSK en düşük (kalıcı otomasyon kurulmaz, K-009 bloke korunur) → ✅ C. **NOT: RİSK sütunu bu blokta İLK KEZ (Salih ajan-yetki formülasyonu, 07-15 — m.37 4. boyut adayı sahada denenmiş oldu).**
- **Seçim:** C (Salih, 07-15 ana-sıra oturumu: "model c'den devam edeceğiz"). Mimari sınırlar: connector'lar çıkarılır · yalnız jarvis reposu · rapor-only prompt (pozitif yetki listesi) · claude/ push kısıtı korunur.
- **Gözlem:** bekliyor (ilk otomatik koşu — token/süre/kalite buraya).
- **Ders:** —
