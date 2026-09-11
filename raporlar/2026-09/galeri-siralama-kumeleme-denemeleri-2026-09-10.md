# Galeri sıralama — kümeleme denemeleri ve nihai yöntem (2026-09-09/10)

> **STAJ DÖNEMİ DOKÜMANI, jarvis-dışı içerik (md.49).** Şirket projesi `data-company-vehicle-scoring` için staj sürecinde yapılan çalışmanın kaydı; yalnız Jarvis reposunda tutulur, şirket reposuna girmez, Jarvis kanonuna karar olarak girmez. Sayılar deneysel (m.29), AS-OF 2026-09-10. Çalışma dizini `kuyruk/galeri-siralama/veri3/` (commit'lenmez); script numaraları o dizine göredir. Bağlam: şirket reposundaki `analiz/guncel-extract-kumeleme-2026-09-08.md` §0-8.

## 0. Nihai yöntem (tüm denemelerden harman)
Bkz. §5. Kısa hâli: **trim kümesi v2 (k=15, maskeli atama) + galerinin trim-kümesi teklif payı (M4b üçlüsü) + soğuk galeri koltuk kotası (en az k=3 soğuk, §4)**. Galeri kümeleme hiçbir biçimde katkı vermedi; galeri düzeyi 305 kolon soğuk galeriyi de kümeden iyi sıralıyor.

## 1. Soru ve düzenek
- Soru: ihale × trim için 30 galerilik listeyi sıralayan CatBoost ranker'a (YetiRank, Recall@30) kümeleme ne katar; özellikle soğuk galeri (B2B geçmişi yok) ve yeni trim için.
- Düzenek: üç zaman kesimi (18 Ağu, 25 Ağu, 1 Eyl), altı dilim (hepsi · sıcak G × sıcak T · sıcak G × yeni T · soğuk G × sıcak T · soğuk G × yeni T · soğuk G ilanlı), tüm galeri özellikleri ihale bazında as-of (09-09'da yakalanan üç sızıntı dersi).
- Veri: 33 ihale, 10.868 galeri, 506 trim, 5.382 teklif olayı (etiket ≥ 2); galeri başına medyan 2 olay, %89'unda 10'dan az.

## 2. Trim tarafı (işe yaradı)
- Trim kümesi v2: 8 boyut (segment, kasa, hacim, yakıt, vites, ticari, fiyat dilimi, güç), Ward k=15, "bilinmiyor" kategori değil, maskeli en-yakın-merkez atama; yakıt+vites gizlenince %69,5 aynı küme. Kartlar `trim_kume_v2_kartlar_k15.md`.
- Modelde M4b = M0 + trim_kume + gal_tekpay_tk (galerinin bu kümeye as-of teklif payı) + gal_tek_n. Üç fold: sıcak G × sıcak T **+1,7**, sıcak G × yeni T **+1,9**, üç fold aynı yön. Soğuk dilimlerde eksi (pay = 0 → "teklif vermez" öğreniliyor).
- Görsel: `raporlar/gorsel/gorsel-2026-09-10-trim-kume-v2-analiz.html`.

## 3. Galeri tarafı (yedi deneme, hepsi negatif)
| # | Deneme | Script | Sonuç |
|---|---|---|---|
| 1 | Üç katmanlı as-of galeri kümesi (M6b), m=10 | 34 | birleşik −0,8; 18 Ağu sıcak −5,4; kararsız |
| 2 | Aynı, öncül ağırlığı m=30 | 36-37 | sıcak kayıp yarıya indi ama M4b'nin 1,4-1,7 altında; fold yönü tutarsız → RET |
| 3 | Galeri kümeleme v3 (davranış vektörü + blok maskesi + bölge kümeleri) + Faz-1 küme sıralama modeli, hedef = hücre oranı | 40-42 | model = "küme genel oranı" (aktiflik); trim'e özgü sıralama yok. Kümeleme kendisi iyi: %88 kararlı, 4 B2B / 23 ilan / 7 bölge kümesi |
| 4 | Etkileşim teşhisi (varyans ayrışımı) | 43 | gk ana etkisi %43-52, tk %1, etkileşim ≈ %18-23 ama yarı-bölme Spearman 0,25-0,32 |
| 5 | Faz-1 hedef = lift (aktiflik çıkarılmış) | 46 | NDCG rastgeleden 0,01-0,03 üstte; Spearman ≤ 0,11 → tercih öğrenilemiyor |
| 6 | Hücre sayısını düşürme (T=15/10/5), yarı-bölme tutarlılığı | 47 | gk tercihi 0,31 → 0,40; modelin yönü (tk → gk) 0,26 → 0,16; eşik 0,5 altı |
| 7 | C: küme aktiflik oranı M4b'ye özellik (M7) + küme oranı × ölçekle soğuk kota | 50-51 | M7 her dilimde M4b altı; soğuk puan kotası soğuk dilimde ≈ 0 (küme oranı 10k soğuk galeriyi ayırmıyor) |

Ortak kök: 33 ihale, hücre başına 5-14 pozitif; küme×trim tercihi varsa bile bu örneklemde tekrarlanmıyor. Üç bağımsız ölçümle gösterildi (4, 5, 6). Galeri kümelerinin kendisi kayıt altında (`surum-v3-faz1-2026-09-10/`, görsel `raporlar/gorsel/gorsel-2026-09-10-galeri-kume-v3-analiz.html`); veri büyürse (12 aylık geçmiş) aynı script'lerle yeniden açılır. Salih kararı 09-10: data ekibinden bu istek alınmayacak.

## 4. Soğuk galeri koltuk kotası (işe yarayan tek galeri-tarafı kaldıraç)
Kural **"en az k soğuk"**: her ihale × trim listesi M4b'nin doğal ilk 30'u; içindeki soğuk galeri (cutoff öncesi B2B olayı olmayan) sayısı k'nın altındaysa en zayıf sıcaklar, M4b skoruna göre en iyi soğuklarla değiştirilir. k=0 = saf M4b. Soğuk sıralayıcı olarak M4b skoru M0'dan biraz iyi (k=3'te soğuk toplam 12,8 ve 11,6). "Sabit k soğuk + (30−k) sıcak" kuralı da tarandı; k=0'da soğuğu tamamen dışladığı için toplam 33,9'a düşüyor, k≥4'te iki kural aynı; tercih en_az. Script 52 (skor kaydı) · 53 (tarama, `53_kota_ozet.csv`) · 54 (görsel `raporlar/gorsel/gorsel-2026-09-10-kota-taramasi.html`).

Üç fold birleşik Recall@30, yüzde puan (sıcak pozitif 4.046, soğuk 2.065):

| k | hepsi | sıcak G | soğuk G | soğuk × sıcak T | soğuk × yeni T | soğuk ilanlı |
|---|---|---|---|---|---|---|
| 0 | 35,9 | 44,7 | 10,5 | 10,9 | 10,3 | 2,7 |
| 1 | 35,8 | 44,5 | 10,9 | 11,3 | 10,7 | 2,9 |
| 2 | 35,7 | 44,0 | 11,9 | 12,7 | 11,4 | 4,0 |
| **3** | **35,8** | **43,8** | **12,8** | **14,4** | **11,8** | **4,7** |
| 4 | 35,7 | 43,3 | 13,8 | 15,6 | 12,7 | 5,2 |
| 5 | 35,3 | 42,6 | 14,4 | 16,5 | 13,1 | 5,6 |
| 6 | 34,8 | 41,5 | 15,5 | 17,9 | 14,1 | 7,0 |
| 8 | 34,2 | 40,2 | 17,0 | 18,6 | 16,0 | 8,2 |
| 10 | 33,7 | 38,7 | 19,2 | 20,5 | 18,4 | 11,0 |

Eğrinin hareketi: toplam k≤4'te düz (−0,2), k=5'te −0,5, k=10'da −2,2; soğuk k=4'e kadar dik (+3,3), sonra eğim yarıya iniyor; sıcak her koltukta −0,5…−1. Marjinal takas (üç fold toplam pozitif): ilk dört koltuk başabaş bandı (koltuk başına soğuk +6…+14, sıcak −8…−19; net −5…+2, gürültü düzeyi), beşinci koltuktan itibaren her koltuk net eksi (−19, −28, −10, −23). Üç fold'un üçünde de k≤3 bölgesi düz, k≥5 iniş; seçim fold'a bağlı değil.

**Öneri: k=3** (toplamı korur, soğuk recall göreli +22%). Soğuk galeriyi öne almak iş önceliğiyse **k=4** üst sınır (toplam −0,2, soğuk +31%). k≥5 toplamdan açık ödün. Salih kararı: kota uygulanacak, sayı bu eğriden (09-10).

## 5. Nihai yöntem, harmanlanmış
Tüm denemelerin harmanı; her parça hangi denemeden geldi:
1. **Trim kümesi v2** (25): 8 boyut, Ward k=15, maskeli atama; yeni/eksik trim de küme alır. Katalog gelirse aynı script (k sabit, merkezler `trim_kume_v2_merkez.json`).
2. **M4b ranker** (29b/30/34): M0'ın 305 kolonu + `trim_kume` + `gal_tekpay_tk` (galerinin bu trim kümesine as-of teklif payı) + `gal_tek_n`. Kazanç sıcak galeride: +1,7 / +1,9 puan, üç fold aynı yön. **Her galeri özelliği ihale bazında as-of** (09-09 üç sızıntı vakası; pencere-bütünü hesap yasak).
3. **Soğuk galeri koltuk kotası** (52-54): kural en_az, k=3 (ya da 4), soğuk sıralayıcı M4b skoru. Soğuk galeri "asla teklif vermez" yerine listeye girer; toplam korunur.
4. **Galeri kümeleme YOK** (34-51): üç katman, davranış kümesi, aktiflik oranı, lift, hücre düşürme, soğuk puan — hiçbiri 2'nin üstüne katkı vermedi; galeri düzeyi 305 kolon soğuk galeriyi kümeden iyi sıralıyor. Kümeler kayıtta, veri büyürse yeniden açılır.
5. **Ölçüm düzeneği sabit:** üç fold (18 Ağu, 25 Ağu, 1 Eyl), altı dilim, Recall@30; kabul = üç fold aynı yön. Tek fold'daki artı karar değildir.
6. **Yeniden açma koşulları:** 12 aylık dealer geçmişi (soğuk dilim küçülür, küme×trim ölçülebilir olur; Salih 09-10: istek alınmayacak) · katalog trim tablosu · trim düzeyinde tüm ilan verisi.

## 6. Dosya dizini
`veri3/`: 25 (trim kümesi v2) · 29b/30 (M4b 3 fold) · 34-37 (M6b, m=30) · 40-45 (galeri kümeleme v3, Faz-1, teşhis, kartlar, görsel) · 46 (lift) · 47 (yarı-bölme) · 50-51 (C) · 52-54 (kota taraması) · `surum-v3-faz1-2026-09-10/` dondurulmuş kopya. Teslim raporları: `raporlar/seans/seans-teslim-2026-09-09-galeri-trim-kumeleme-model.md` ve bugünün seans teslimi.
