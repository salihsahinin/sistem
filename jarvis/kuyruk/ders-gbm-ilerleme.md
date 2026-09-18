# GBM Ders İlerlemesi (gradient boosting, sıfırdan)

Harita: `raporlar/2026-08/gradient-boosting-sifirdan-ders-2026-08-25.html` · Yöntem: sohbette partisyon partisyon; her partisyon = tanım → mekanizma → elle örnek → kontrol sorusu.

## Kalibrasyon (2026-08-25)
- Türev: biliyor · Ortalama: biliyor · Varyans: unutmuş (P3'te yeniden kurulacak)
- Model eğitme deneyimi: yok (D bloğu pratik ağırlıklı işlenecek)
- Tempo: P1 hızlı

## Durum
| partisyon | durum | not |
|---|---|---|
| P1 örnek/feature/etiket | KAPANDI (2026-08-25) | grain sorusu doğru; leakage sorusunda düzeltme yapıldı (anchor günü tanımı verildi) |
| P2 model=fonksiyon, F(x)=c | KAPANDI (2026-08-25) | kontrol sorusunda "x" cevabı düzeltildi — F(x)=c aslında x'i hiç okumuyor |
| P3 hata ölçümü + varyans | KAPANDI (2026-08-26) | 6 mikro-adıma bölündü (26'da "yavaş anlat" istendi, dünkü hızlı sürüm yeniden yapıldı): toplama başarısız (cancellation) → mutlak değer → mutlak değerin köşe sorunu → E(c) formülü → türevle c=1.2 → c=ortalama kanıtı + varyans=1.36 yeniden inşa edildi. Kontrol hatası: "hepsi 1.2 olsa varyans" sorusuna 0.24 cevabı verildi, doğrusu 0 — düzeltildi, ardından "varyans neden bu tanıma cevap veriyor" sorusu derinlemesine açıklandı |
| P4 ezber vs genelleme | KAPANDI (2026-08-26) | 4 mikro-adım: ezberci model (E=0) tuzağı → eğitim/doğrulama ayrımı (G6 örneği) → k-fold fikri (kullanıcı kendi buldu, train/test bölmesi doğru refleksti) → küçük veride tek-bölme dengesizliği (4.94 vs 4.0) → zaman-bazlı split gerekliliği (i.i.d. varsayımının neden geçersiz olduğu, kullanıcı doğru kapattı) |
| P5 karar ağacı (Blok B, tümü) | KAPANDI (2026-08-26) | tek-soru-iki-grup fikri (6.80→1.17) → split arama (4 aday elle tarandı, kazanan doğrulandı) → "sağ grup neden kötü" (varyans bağı, kullanıcı doğru cevapladı) → sınırsız bölmenin ezberciye (P4) dönüştüğü gösterildi → durdurma kuralları (derinlik/min-yaprak/min-kazanç) tanıtıldı. Ara konu: CatBoost model kurma sorusu (T1-T5 dikkat noktaları + 8 adımlı plan + parametre önerisi) — ayrı not olarak aşağıda durur, derse karışmadı |
| **BLOK C — Boosting** | KAPANDI (2026-08-27) | Tamamı G1-G5 üzerinde elle: P9 artık tanımı (Model1'in tahminleri, y-tahmin farkı, işaret=yön) → P10 Model2'yi artığa fit etme, split-arama HATASI yapıldı (6-9 eşiği önerildi, kullanıcı "nasıl hesapladın" diye sorunca 4 aday tam tarandı, gerçek kazanan 1-2 arası (0.80) olduğu ortaya çıktı — dürüstçe düzeltildi) → doğru eşikle Model1+Model2 toplamı (G1/G3 artık=0'a düştü, ezber alarmı verdi kullanıcı doğru yakaladı) → P11 öğrenme oranı η=0.5 ile frenleme (G1/G3 artık sıfıra düşmüyor, toplam hata 0.80→0.89 ama gerekçeli) → 2-model uçtan uca akış (eğitim G4 vs kullanım G7, y bilinen/bilinmeyen ayrımı) → iki ağacın farklı eşiklerinin gösterimi → P12 gradient adının kanıtı (L(F)=(1/2)(y-F)², türev, negatif-gradyan=artık, işaret mantığı G4 üzerinden kanıtlandı) |
| **BLOK D — Pratik GBM başlıyor** | | |
| P13 frenler (hiperparametreler) | AÇIK (2026-08-27) | Kullanıcı isteği: hiperparametre SEÇİMİ için ayrı, detaylı vaka çalışması (grid search + doğrulama hatası kavramı somut örnekle) — P13'ün genişletilmiş kapsamı olarak işleniyor, ayrı partisyon açılmadı |
| P14 kütüphane farkları (CatBoost'a özel) | KAPANDI (2026-08-27) | simetrik ağaçlar (elle depth=2 örneğiyle karşılaştırma) → ordered boosting (sızıntı örneği, sıralı-eğitim mantığı) → NULL yönetimi (bağlama göre öğrenilen yön) → kategorik kodlama (hatırlatma). Kontrol sorusu kullanıcı tarafından kendi cevaplandı: ortak tema = P4 ezber/genelleme geriliminin farklı kanallarda (kapasite kısıtı vs bilgi-sızıntısı kısıtı) tekrarı |
| P15 metrikler | KAPANDI (2026-08-27) | MSE (P3'e bağlandı) → precision/recall@k (trim-genel senaryo) → **kullanıcı düzeltmesi: gerçek iş bağlamı haftalık toplu ihale (20 araç/hafta), sorgu=trim değil (trim,ihale) — her arabanın TEK kazananı var** → Hit Rate@k yeniden kuruldu → NDCG elle inşa edildi (DCG, IDCG, normalize etme), tek-pozitiflik özel durumunda IDCG=1 kanıtlandı → "+1" ispatı (log2(1)=0, sıfıra bölme) + log tabanının tasarım-tercihi olduğu dürüstçe ayrıştırıldı + NDCG açılımı (N/D/C/G, her harf ayrı ayrı) |
| **BLOK E — Bizim problem başlıyor** | | |
| P16 ranking (LTR) — ihale bağlamına göre | KAPANDI (2026-08-28) | Etiket basitleştirildi (sale_car_raw.buyer_id direkt okuma, pencere taraması yok) → group_id=araba tasarımı → QuerySoftMax mekanizması → **3 tam matematiksel ispat elle yapıldı:** (1) softmax formülü — pozitiflik/monotonluk/toplam-1 kanıtı, sigma'sız versiyon + Euler sayısı neden (kendi türevi kendisi, mismatched-base sayısal karşılaştırmasıyla gösterildi) (2) Loss=−log(P) — maksimum olabilirlik ilkesinden, çarpım→toplam (log) → işaret çevirme (min/max eşdeğerliği) ispatlarıyla (3) artık=etiket−P — tam türev (log sadeleştirme hamlesi, kazanan/kazanmayan için ayrı ayrı, sayısal doğrulama). Doğrulama değerleri nasıl seçilir (yan soru) — 3'lü split (eğitim/doğrulama/test), walk-forward notu |
| **P17 uçtan uca uygulama planı** | AÇIK (2026-08-28) | Tüm ders senteziyle kapanış; Python temelleri kursu P17 sonrası AYRI bir mini-blok olarak başlayacak (kullanıcı notu, zayıf Python bilgisi) |

## Konu-arası not: CatBoost model kurma planı (2026-08-26)
Ders dışı, ayrı bir konuşma dalı — dersle karışmadı, ders bitince ya da paralel ele alınabilir.
- T1-T5 dikkat noktaları: geçmişe-koşum sadakati (member/sale_car_raw/market_list tarihçesizliği), snapshot-arası korelasyon, havuz tavanı, kimlik ezberi, parametre kayması
- 8 adımlı plan: ölçüm turu → as_of_date + T1 düzeltmeleri → 8-12 snapshot → etiket join → feature triyajı → 3 taban çizgisi (rastgele/popülerlik/mevcut SQL) → CatBoost v1 → iş metriği
- Fikir önerileri: F1 (iki aşamalı model, seri+trim), F2 (ML öncesi ağırlık geri-testi), F3 (trim-tarafı feature eksikliği) öncelikli; F4-F9 ikincil not
- Sıradaki tek adım: pozitif oranı + havuz tavanı ölçen sorgu (yazılmadı, bekliyor)

## Not: P-sonrası uygulama fikirleri (2026-08-26, ders bitince değerlendirilecek)
Jarvis'in kendi veri katmanı (bronz/silver/gold) GBM için aday veri üretiyor:
- Skill tetikleme doğruluğu tahmini (`hareket-olay.jsonl` → doğru/yanlış tetikleme etiketi)
- Bağlam-şişmesi/context-trajectory tahmini (turn sayısı, araç türü dağılımı → kapanış eşiği regresyonu)
- Anakronizm-denetim yanlış-pozitif ayıklama (433 bronz satır, 114 ihlal/319 uyarı zaten etiketli gibi duruyor — en hazır veri, ilk model denemesi için aday)
- Görev başına token tüketim tahmini (m.25 −%30 hedefine hizmet)
Sıra: önce P1-P17 dersini bitir (model eğitme deneyimi yok, varyans P3'te yeniden kurulacak), sonra en hazır veri olan anakronizm-ayıklama üzerinde ilk uygulamalı model denemesi.

## Anlatılacaklar kuyruğu — P17 sonrası açılan konular (2026-08-29)
P1-P17 tamamlandı (bkz. yukarıdaki durum tablosu), sentetik veri + CatBoost pratiği bitti (QuerySoftMax → YetiRank, ders dışı ama fiilen koşuldu, bkz. `kuyruk/ders-gbm/`). Ders sonrası soru-cevap akışında açılan, henüz P-numarası verilmemiş, sıradaki oturumda ELLE (P3/P9-P12 disipliniyle: tanım→mekanizma→somut örnek→ispat) işlenecek konular:

- **Uplift modeli (2026-08-29 talebi):** "rekabeti diri tutmak için hangi galerilere promosyon" sorusundan doğdu — ters-sıralamanın neden bunu cevaplamadığı (item-özel uyumsuzluk ≠ genel pasiflik) zaten anlatıldı, kısa bir "nasıl yapılır" da verildi (nedensel çıkarımın imkansız problemi, rastgele A/B deneyi, T-learner iki-CatBoost-modeli, Qini eğrisi) — ama BU, hızlı/özet geçişti, dersin "yavaş, elle, ispatlı" standardında DEĞİL. Sıradaki oturumda: (1) nedensel çıkarımın imkansız problemini küçük somut bir örnekle (G1-G5 tarzı, 5 galeri) yeniden kur, (2) rastgele deney tasarımını elle simüle et (sentetik veri gibi), (3) T-learner'ı iki küçük ağaçla elle hesapla, (4) Qini eğrisini elle bir kaç noktayla çiz. Akraba: F7 (CatBoost tangent'indeki ileri fikir, aynı konu).
