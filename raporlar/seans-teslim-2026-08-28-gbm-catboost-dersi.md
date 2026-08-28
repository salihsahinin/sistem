# Seans Teslim Raporu — 2026-08-28 — GBM/CatBoost dersi (paralel oturum)

*Not: bu, jarvis pointer-sistemi/karar hattının DEVAMI DEĞİL — Salih'in kendi iş projesi (galeri-ihale skorlama modeli, CatBoost) için ayrı bir öğrenme/hazırlık oturumu. Aynı gün (2026-08-28) başka bir jarvis oturumu (V86'nın kaynağı) paralel çalışıyordu; H4 kuralına göre bu kapanış yalnız kendi dosyalarını (`kuyruk/ders-gbm*`, bu rapor, fikir-kutusu V87 satırı, rutin pipeline türevleri) hedefliyor.*

## Bugün gerçekten ne değişti

- **`galeri_scoring_compute.sql` + rapor SQL'inin ağırlıklı-toplam skorlama tasarımı derinlemesine eleştirildi** (paralel/çoklama, RANK vs CUME_DIST, notr_dolgu/MNAR riski, kademe iskontosu) — sonuç: elle ağırlık yerine GBM/CatBoost ile öğrenilmiş sıralamaya geçiş kararı doğrulandı.
- **GBM'in tamamı sıfırdan, elle hesaplarla kuruldu** (P1-P17, kuyruk/ders-gbm-ilerleme.md'de tam iz): örnek/feature/etiket ayrımı → model=fonksiyon → hata ölçümü/varyans → ezber-genelleme → karar ağacı split-arama → boosting (artık, öğrenme oranı, gradyan ispatları) → hiperparametre grid-search vakası → metrikler (MSE, precision/recall, NDCG — ispatlı) → ranking/LTR (QuerySoftMax) → uçtan uca plan.
- **İş bağlamı oturum içinde düzeltildi**: "trim başına genel sıralama" varsayımından "haftalık toplu ihale, her araç tek kazanan, sorgu=(trim,ihale-haftası)" gerçeğine geçildi — etiket tasarımı (`sale_car_raw.buyer_id` doğrudan okuma) ve QuerySoftMax seçimi bu düzeltmeye göre yeniden kuruldu.
- **Sentetik veri seti + gerçek CatBoost koşumu** (`kuyruk/ders-gbm/`): 2.880 satır, 288 araç-grubu, 40 galeri, gömülü gerçek kural (kademe hiyerarşisi + bütçe×tazelik ETKİLEŞİMİ + gürültü kolonları). Kullanıcı kendi eliyle (rehberlikle) Python/pandas/CatBoost kodunu yazdı, çalıştırdı, yorumladı.
- **QuerySoftMax modeli eğitildi**: test setinde Hit Rate@1=%58.3, Hit@5=%93.75, taban çizgilerini (rastgele/popülerlik) ezici farkla geçti; feature importance kademe hiyerarşisini ve bütçe×tazelik etkileşimini doğru yakaladı (etkileşim artışı +1.24, ağırlıklı toplamın yapısal olarak üretemeyeceği bir sonuç).
- **Ekip kararıyla YetiRank + dereceli relevans (4-3-2-1-0) skalasına geçildi**: relevans kolonu ayrı script'le (`03_relevans_ekle.py`) üretildi, YetiRank eğitildi — QuerySoftMax'ı her metrikte geçti (Hit@1 %66.7, NDCG doğrulama 0.91).
- **Gerçek bir sızıntı hatası yakalanıp düzeltildi** (bkz. fikir-kutusu V87): `relevans` kolonu `DISARI` listesine eklenmeyi unuttu, model NDCG=1.0'a 4 iterasyonda ulaştı — kullanıcı "0.86 gibi bir şey beklerdik" refleksiyle yakaladı, kök neden teşhis edilip düzeltildi.
- **YetiRank'in mekanizması** (pairwise + ΔNDCG ağırlıklandırma) elle, tam sayısal örnekle (14 çift, sigmoid+ΔDCG hesabı) kuruldu — bir önceki basitleştirilmiş varsayımın (sezgisel net_artık) gerçek hesapla **çeliştiği** görüldü ve dürüstçe düzeltildi (G018'in net etkisi pozitif çıktı, ilk sezgi yanlıştı).
- **Devam promptu yazıldı**: Salih'in gerçek veri setleriyle yeni bir oturumda aynı çerçeveyi (group_id=araç, feature triyajı, zaman-bazlı 3'lü bölme, YetiRank+relevans, "kod ben yazarım" çalışma şekli) uygulaması için portatif bir özet hazırlandı.

## Hangi karar verildi (kaynak + gerekçe + geri-açma)

- **Model sınıfı: CatBoostRanker + YetiRank + dereceli relevans** — kaynak: ekip kararı (kullanıcı beyanı) + bu oturumda sentetik veride ölçülerek doğrulandı (QuerySoftMax'a karşı üstünlük, tüm metriklerde). Geri-açma koşulu: gerçek log-kapsamı ölçümü `relevans=1` seviyesinin MNAR riskini doğrularsa, o seviye düşürülüp 4-3-2-0'a dönülebilir.
- **Etiket kaynağı: `sale_car_raw.buyer_id` doğrudan okuma, pencere taraması YOK** — kaynak: "sorgu=araç, tek kazanan" iş gerçeğinin netleşmesi. Eski 30-günlük-pencere tasarımı terk edildi.
- **group_id = araç (sale_id+car_id), hafta DEĞİL** — kaynak: kullanıcının "aynı hafta iki araç kazanan galeri" kontrol sorusunu doğru cevaplaması; tasarım zaten doğru kurulmuştu, teyit edildi.

## Hangi fikir aday kaldı (karar DEĞİL)

- **V87 (fikir-kutusu)**: feature-triyaj hijyeni — yeni kolon eklendiğinde DISARI/whitelist denetimi otomatikleştirilsin mi. Gerçek CatBoost pipeline kurulurken değerlendirilecek.
- **"1" (detaya baktı) relevans seviyesinin log-kapsamı MNAR riski** — ölçülmedi, gerçek veride önce ölçülüp sonra karar verilecek (kutuya girmedi, doğrudan devam promptuna not düşüldü).

## Sonraki ilk iş

Salih, yeni bir oturumda (portatif prompt hazır) kendi gerçek veri setleriyle: (1) veri tanıtımı, (2) group_id/feature-triyaj/zaman-bölmesi gerçek veriye uyarlama, (3) `relevans` etiketinin gerçek tablolardan türetilmesi, (4) log-kapsamı MNAR ölçümü, (5) ilk gerçek model eğitimi. Çalışma şekli sabit: kod kullanıcı tarafından yazılıyor, Carvis rehberlik ediyor.

## Neyi yeniden açmak için hangi koşul gerekir

Bu ders serisi (P1-P17) kanonik bir jarvis kararı değil — Salih'in kişisel öğrenme/iş-hazırlık hattı (m.15 "CV projeleri Jarvis içinde geliştirilir" sınıfına yakın). Yeniden açma koşulu yok; sadece devam promptu üzerinden sürer.

---

## Hasat

1. **Özütler:**
   - Bir modelleme derinliğinde "elle doğrula" disiplini (P3'ten P16'ya kadar her formülün önce elle ispatlanması) hem doğru mekanik anlayışı hem de İKİ gerçek hatayı (split-arama kısayolu, sızıntı bug'ı) canlı olarak yakalattı — kısayol almadan tam hesap yapmanın somut kazancı.
   - Kullanıcının "model eğitme sürecini kendim yapmak istiyorum" sınırı net çizildi ve saygı gösterildi (kod kullanıcıda, rehberlik Carvis'te) — CV/iş-projesi bağlamında bu ayrımın işlediği bir örnek.
   - İş bağlamı netleşmesi (trim-genel → haftalık-ihale-tekil-kazanan) modelleme kararlarının (etiket, group_id, loss function) hepsini geriye dönük değiştirdi — erken iş-bağlamı doğrulamasının maliyeti, geç doğrulamadan çok daha ucuz.
2. **Wiki-delta:** yok bu oturumda (jarvis kavram sözlüğüne değil, dış bir ML projesine dair).
3. **Verilebilir miydi (V20):** kısmen — sentetik veri üretimi ve YetiRank'in matematiksel ispatları bir araştırma-ajanına devredilebilirdi, ama kullanıcının "elle, adım adım, kontrol sorularıyla" öğrenme talebi bunu bilinçli olarak dışladı (doğru tercih, öğretim amacı farklı).
4. **Token×zaman etiketi:** çok/uzun — çok uzun, çok derin (matematiksel ispat ağırlıklı) bir tek-oturumluk ders serisi; beklenti tuttu (kullanıcı sürekli "devam" ile ilerlemeyi onayladı, kopma yok).

## Boyut-tetiği

`fikir-kutusu.md` zaten aşımdaydı (bu oturumdan ÖNCE, 30,2 KB / 20 KB bütçe) — V87 eklenmesiyle aşım büyüdü, damıtma bu oturumun kapsamı dışında (paralel oturumun sahip olduğu dosya, tek-satır ekleme dışında dokunulmadı).

## Araç-çıktısı notu (KB-50 a)

Bu oturumda birkaç Bash çıktısı (CatBoost eğitim logları, feature importance tabloları) ~1-3k token aralığında kaldı, 10k eşiğini aşan tekil araç çıktısı olmadı — özet+pointer kuralı ihlali yok.
