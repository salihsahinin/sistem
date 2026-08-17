> **ARŞİV (2026-08-17, Salih Katman-1 kararı):** "stokastik düşünceyi sisteme entegre etmek kötü bir karardı … LLM'ler ve makineler deterministik düşünür ve deterministik tasarlanmalı." `wiki/stokastik-dusunce.md` sayfasının 08-16 (E1 entegrasyonu, commit ac8f928) hâli aşağıda birebir; canlı sayfa emekli-güdüğe çevrildi. Buradaki "JARVIS hükmü" (seçici-stokastik hibrit) ve "SOP 7 kural" (ajanı stokastik düşündürme) REDDEDİLDİ; araştırma bulguları (rapor `cc/rapor-2026-08-16-1.md`) tarihçe olarak kalır. m.8: silinmedi, arşive indi. Karar kaydı: `kuyruk/senaryo-defteri.md` 08-17 bloğu Karar 5.

# stokastik-dusunce

**Üst blok:** Belirsizliği istisna değil VERİ sayan düşünme kipi: aynı girdi → tek çıktı değil dağılım; varyasyon dikkate alınır, rastgelelik kusur değil araçtır, olasılıksal tahmin ancak proper skorla değerlendirilir. Tek kanonik tanım yoktur (bilinen kör). · Durum: GÜNCEL · Son teyit: 2026-08-16 (S-1 atlas koşumu `wf_a08eccb1`; hayatta-kalma 5/30/1/0, V26 3/3) · Kaynaklar: `cc/rapor-2026-08-16-1.md` (24 hakem yapı-taşı + sentez) · `cc/gorev-2026-08-16-1.md` · Güven: orta (tek koşum, D-ağırlıklı yapı-taşları; JARVIS'in kendi rejimi [<50 olay, altın-cevapsız] literatürde ölçümsüz — transferler şerhli).

**Çekirdek:** Deterministik düşünce "bu adım şu sonucu verir" der; stokastik düşünce "bu adım şu DAĞILIMDAN bir sonuç verir — varyasyonu ölç, karar kuralını dağılıma kur" der. Kurucu çerçeve (Wild & Pfannkuch 1999) bunu tek hesap değil çok-boyutlu dispozisyon olarak tanımlar; merkezde **varyasyonu-dikkate-alma**. Üç çekirdek ayrım: (1) belirsizlik iki tür — aleatorik (indirgenemez) ↔ epistemik (veriyle indirgenir) ve bu ayrım MODELE GÖRELİDİR ("indirgenemez" = seçilen modelin artığı); (2) rastgelelik araçtır ama kazancı **hata-bütçesine koşulludur** (sınırlı hata kabul edersen ispatlı tasarruf [EQ: O(log n) vs n+1 bit]; sıfır-hata istersen kazanç yok — V26 tohumlu örneklemin ilkesel gerekçesi); (3) olasılık beyanı ancak **proper skorlama** (Brier/log) altında dürüsttür — skor tasarımı bozuksa "olasılık söyle" talimatı teşvik üretmez. **Kanonik damıtılmış örnek:** hekimlere "testin pozitif çıktığı hastada hastalık olasılığı" sorusu koşullu-olasılık formatında sorulunca 24'te 1 doğru; AYNI bilgi doğal-frekans formatında ("10.000 kişiden…") verilince 24'te 16 doğru — en güçlü kaldıraç eğitim değil TEMSİL FORMATIDIR; ders: ajana/insana olasılığı "p=0,7" değil "benzer 10 vakanın 7'si" biçiminde taşı.

**JARVIS hükmü (sentez, karar Salih'te):** seçici-stokastik hibrit — **üretim/keşif stokastik · orkestrasyon+doğrulama deterministik · tekrarlı iş kodda.** Dayanak: workflow-vs-agent kuralı (tek SAĞLAM mimari bulgu) + pass^k erozyonu (p=0,9 → k=8'de %57: stokastik ajanın tekrarlı-iş faturası) + çok-ajanlı tartışmanın eşleşmiş bütçede kaybetmesi (tek DÜŞTÜ) + n<50'de bandit/öğrenilmiş-yönlendirme ölçümsüzlüğü (seçim uzman-önselle). m.40b çift-atlas zaten bu hibrittir: bağımsız işçiler stokastik örnekleme, pipeline/maskeleme deterministik kod.

**SOP (ajanı stokastik düşündürme — protokol düzeyi, 7 kural; ince-ayar kapısı JARVIS'te kapalı):**
1. Örnek değil DAĞILIM iste (çağrı-başına örnek → model tek çıktıya çöker >%94; tek çağrıda JSON dağılım beyanı çalışır).
2. Güven skorunu üreticiden değil AYRI doğrulayıcı çağrıdan al; öz-değerlendirmede çıktıyı "kullanıcı girdisi" olarak yeniden çerçevele (sahiplik-yanlılığı %26'ya varan fazla-güven).
3. İnanç güncellenecekse kanıtı SIRALI ver, tek seferde yığma (sıralı kipte yaklaşık-Bayes, toplu kipte sapma).
4. Sayısal güveni Salih'e varsayılan GÖSTERME — kalibrasyonu o görev sınıfında ölçülmemişse kategorik/çekimser dil; model-üretimi olasılık "kaynaklı rakam" değildir → m.39 gereği [?] damgası.
5. Öz-düzeltme döngüsü kurma; düzeltme turu yalnız dış test/doğrulayıcı kapısıyla açılır (self-refine yanlış-onay %46,7).
6. Olasılığı doğal-frekans formatında taşı (prompt'ta da sunumda da).
7. n<50'de miskalibrasyon hükmü verme — "güç yetersiz" damgası; ECE ancak eşit-kütleli + debiased tahminciyle.

**Gotchas:**
- T=0 ≠ tekrarlanabilirlik: paylaşımlı API serving'de aynı prompt farklı çıktı verebilir (1000 koşum → 80 benzersiz) — "aynı prompt'u tekrar koşarım, aynısını alırım" varsayımı yasak; audit = koşum ÇIKTISINI logla (hafıza = git log ilkesiyle uyumlu).
- "Ajanları tartıştır" cazibesi: çok-ajanlı tartışma eşleşmiş hesap bütçesinde tek-ajan CoT/self-consistency'nin ALTINDA — ekonomi rejiminde yasak-varsayılan.
- Self-consistency yalnız sonlu-cevapta ve N=5-10'da doyar; tutarlı-yanılgıyı yakalamaz (üyeler bağımsız değilse ensemble ilkesi çöker — F4 şerhi).
- Havuzlanmış ortalama uygulayıcı-varyansını gizler (aynı müfredat: −23..+63 puan) — ajan/skill ölçümü ajan-başına + Wilson.
- Bu sayfadaki insan-deney kanıtlarının (format, eğitim) LLM'e transferi ölçülmemiş; Türkçe tamamen ölçümsüz — uygulamalar deneysel m.29 damgalı başlar.

**Süpersede zinciri:** —

**Bağlantılar:** [[adversarial-hayatta-kalma]] (üretici≠doğrulayıcı — SOP kural 2 ve 5'in koşum hali) · [[token-x-zaman]] (stokastik dal = bilinçli ×token bedeli; N× örnekleme ödünleşimi) · [[olcum-banki]] (Brier/skor kaydı buraya oturur) · aday: [[tahmin-defteri]] (E5 skill adayı, sayaç 1/3 — m.43).
