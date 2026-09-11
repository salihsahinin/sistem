# Galeri sıralama modeli — nihai sürüm: kümeler, model girdileri, kota kuralı ve başarı ölçümü

*Ekibe not, 2026-09-10. Tüm rakamlar 14 Temmuz – 4 Eylül extract'i üzerinde, üç zaman kesimli geriye dönük testten; canlı sonuç değil.*

## 1. Kısaca ne değişti
İhale × trim başına 30 galerilik öneri listesini üreten CatBoost sıralayıcıya üç ekleme yapıldı:
1. Trimler 15 "araç tipi" kümesine ayrıldı; modele trimin kümesi ve galerinin o kümeye geçmiş teklif payı eklendi.
2. Listeye "en az 3 soğuk galeri" kuralı geldi (soğuk = daha önce hiç teklif vermemiş galeri).
3. Galeri tarafında kümeleme denendi, işe yaramadı, modele girmiyor; neden aşağıda.

Sonuç: aktif galerilerde isabet +1,7 / +1,9 puan, soğuk galerilerde +2,3 puan, toplam isabet korundu.

## 2. Kümeler nasıl oluşuyor, kaç tane
**Küme = araç tipi.** Marka ölçüt değil; Renault Clio ile Dacia Sandero aynı kümede, Fiat Egea dizel-otomatik ile Egea benzin-düz vites ayrı kümede.

- **Girdi:** ihalelerde görülmüş 506 trim. Her trim 8 özellikle tanımlanır: segment (B/C/D/J/LCV), kasa (hatchback, sedan, station, SUV, van), motor hacmi, yakıt, vites, ticari mi, açılış fiyatı dilimi (5 dilim: 790 bin / 990 bin / 1,19 M / 1,49 M TL sınırları), motor gücü (HP).
- **Eksik özellik:** trim adından ayrıştırılır, olmazsa arabam.com katalog eşleşmesinden, olmazsa aynı marka-serinin çoğunluğundan doldurulur. Yine boşsa "bilinmiyor" diye ayrı bir küme YAPILMAZ: trim yalnız bildiği özelliklerle en yakın kümeye atanır (maskeli uzaklık). Bu sayede yeni ya da eksik tanımlı trim de küme alır.
- **Yöntem:** Ward bağlantılı hiyerarşik kümeleme (birbirine en yakın trimleri adım adım birleştiren, rastgelelik içermeyen yöntem), özellikleri tam olan 436 trimle kurulur; kalan 70 trim maskeli atamayla küme alır.
- **Küme sayısı 15.** Seçim ölçütü: yakıt ve vites bilgisi gizlenince trimlerin yine aynı kümeye düşme oranı (k=15'te %69,5, yerel tepe) ve modeldeki isabet. Örnek kümeler: B segment benzinli otomatik hatchback (Clio, Sandero, Polo; 55 trim, en kalabalık) · C sedan benzinli otomatik (Megane sedan, City, Corolla) · C dizel otomatik (Egea dizel, Megane dCi) · B SUV benzinli (Bayon, C3 Aircross) · hibrit · LCV ticari (Doblo, Combo) · elektrikli (Tesla, Corsa-e; 10 trim, en küçük).
- **Yeni trim geldiğinde:** kümeleme yeniden yapılmaz; trim, kayıtlı 15 merkeze bildiği özelliklerle atanır. Katalog geneli trim tablosu gelirse aynı script aynı 8 özellikle genişler.

**Galeri kümesi yok.** Galeriler de kümelendi (B2B teklif geçmişi, ilan envanteri, ilan ölçeği ve bölge blokları; 27 davranış kümesi + 7 bölge kümesi; ardışık ihalelerde %88 aynı kümede kalıyor). Ama kümenin "hangi araç tipini sever" bilgisi ihaleden ihaleye tekrar etmiyor (yarı-bölme tutarlılığı 0,25-0,40; sıralama rastgeleden ayırt edilemiyor) ve modelin mevcut 305 kolonu soğuk galeriyi kümeden daha iyi sıralıyor. Yedi farklı biçimde denendi, hiçbiri katkı vermedi. Sebep veri hacmi: 33 ihale, galeri başına medyan 2 teklif olayı. Kümeler kayıtta; 12 aylık galeri geçmişi gelirse yeniden değerlendirilir.

## 3. CatBoost modeli neyi girdi alıyor
- **Satır:** (ihale, trim, galeri) üçlüsü. **Hedef:** galerinin o trime etkileşim düzeyi (2 = teklif ve üstü pozitif).
- **Kayıp fonksiyonu:** YetiRank (sıralama kaybı; her ihale × trim grubunda galerileri birbirine göre sıralamayı öğrenir, mutlak olasılık değil). 200 iterasyon, derinlik 6, öğrenme hızı 0,1.
- **Girdi kolonları:** mevcut extract'in 305 kolonu (galeri aktivite, satın alma, fiyat, bölge, ilan, trim pazar bilgileri; `signal_source` ve 34 sızıntılı kolon dışarıda) + 3 yeni kolon:
  - `trim_kume` (kategorik, 1-15): trimin araç tipi kümesi.
  - `gal_tekpay_tk`: galerinin bu ihaleden ÖNCEKİ teklif olayları içinde bu kümenin payı. Örnek: galeri geçmişte 10 teklif verdi, 4'ü B hatchback kümesine → bu kümenin trimlerinde 0,4.
  - `gal_tek_n`: galerinin önceki teklif olayı sayısı (log).
- **As-of kuralı (kritik):** her galeri özelliği yalnız o ihalenin tarihinden önceki verilerle hesaplanır. Eğitim penceresinin tamamından hesaplanan bir özellik, satırın kendi etiketini taşır ve testte olmayan bir isabet gösterir; bu hata üç kez yakalanıp düzeltildi. İmzası: özellik önem sırasında aniden 1'e fırlayan kolon.
- **Modelin bu kolonları kullanma biçimi:** küme numarası tek başına neredeyse kullanılmıyor (308 kolonda 162-228. sıra); iş yapan `gal_tekpay_tk` (46-80. sıra). Yani model "bu araç tipi" etiketini değil, "bu galeri bu araç tipine ne kadar gider" oranını kullanıyor. Kazancın sıcak galeri × yeni trim diliminde en yüksek olması bundan: galeri o trimi hiç görmemiş olsa da trimin kümesine olan geçmişiyle eşleşiyor.

## 4. Kota kuralı: "en az 3 soğuk galeri"
- Model listeyi üretir (ilk 30). Listedeki soğuk galeri sayısı 3'ün altındaysa, listedeki en düşük skorlu sıcak galeriler çıkarılır, yerine liste dışındaki en yüksek skorlu soğuk galeriler alınır. Listede zaten 3+ soğuk varsa hiçbir şey değişmez.
- Neden: model soğuk galeride "geçmiş teklif payı = 0" görüp onu "teklif vermez" diye öğreniyor; soğuk galeri listeye giremiyor. Oysa soğuk galerilerin bir kısmı teklif veriyor (test döneminde pozitiflerin %38'i).
- Neden 3: kota 0'dan 20'ye kadar tarandı. Toplam isabet 4 koltuğa kadar sabit, 5. koltuktan itibaren her koltuk net kayıp. 3 koltuk toplamı korur, soğuk galeri isabetini göreli %22 artırır. İş önceliği soğuk galeriyse 4 üst sınır.

## 5. Başarı nasıl ölçüldü, nasıl ölçülecek
**Düzenek:** üç zaman kesimi (18 Ağustos, 25 Ağustos, 1 Eylül). Her kesimde model kesim öncesi ihalelerle eğitilir, kesim sonrası ihalelerde ölçülür. Ölçü **Recall@30**: ihale × trim çiftinde gerçekten teklif veren galerilerin, önerilen ilk 30'a girenlerinin payı. Altı dilimde ayrı raporlanır (sıcak/soğuk galeri × bilinen/yeni trim). Kabul kuralı: üç kesimde aynı yönde fark; tek kesimdeki artı karar değildir.

Üç kesim birleşik, yüzde puan (pozitif = gerçek teklif veren galeri sayısı):

| Dilim | pozitif | eski model (M0) | + trim kümesi (M4b) | + kota 3 (nihai) |
|---|---|---|---|---|
| hepsi | 5.454 | 34,9 | 35,9 | 35,8 |
| sıcak galeri × bilinen trim | 1.522 | 43,2 | 44,9 | 44,2 |
| sıcak galeri × yeni trim | 2.524 | 42,6 | 44,5 | 43,5 |
| soğuk galeri × bilinen trim | 521 | 11,3 | 10,9 | 14,4 |
| soğuk galeri × yeni trim | 887 | 12,7 | 10,3 | 11,8 |
| soğuk galeri, ilanı olan | 657 | 4,6 | 2,7 | 4,7 |

Okuma: trim kümesi sıcak galeride kazandırır, soğuk galeride kaybettirir; kota soğuk kaybını geri alır ve üstüne çıkar, sıcaktan yarım-bir puan verir. Toplam eski modelin bir puan üstünde.

**Canlıda ölçüm önerisi:** her ihale kapandıktan sonra o ihalenin listeleri için aynı Recall@30 altı dilimde hesaplanır ve kesim listesine yeni fold olarak eklenir; ayrıca "listeye kotayla giren soğuk galerilerden kaçı teklif verdi" sayısı ayrı izlenir. Ayrı A/B gerekmez; kesim sayısı büyüdükçe kabul kuralı aynı kalır.

**Şerhler:** mutlak rakamlar extract'teki bazı kolonlar yüzünden şişkin olabilir (çift-oturum günlerinde sabah satırının akşamı görmesi şüphesi data ekibine soruldu); model kıyasları geçerli. 1 Eylül kesimi az ihale içerir, soğuk dilimlerinde tek tek sayılar gürültülüdür.

## 6. Nihai yöntem, harmanlanmış (terim açıklamalı)
Tüm denemelerin harmanı; her parça hangi denemeden geldi:
1. **Trim kümesi v2** (script 25): 8 boyut, Ward k=15, maskeli atama; yeni/eksik trim de küme alır. Katalog gelirse aynı script (k sabit, merkezler `trim_kume_v2_merkez.json`).
   *Ward:* hiyerarşik kümeleme yöntemi, en yakın grupları adım adım birleştirir, rastgele başlangıç içermez. *k=15:* küme sayısı. *Maskeli atama:* trimin bilmediği özellik uzaklık hesabından çıkarılır, bilinen özelliklerle en yakın küme merkezi seçilir. *Merkez:* her kümenin ortalama özellik vektörü; yeni trim bu 15 merkezden en yakınına gider.
2. **M4b ranker** (29b/30/34): M0'ın 305 kolonu + `trim_kume` + `gal_tekpay_tk` (galerinin bu trim kümesine as-of teklif payı) + `gal_tek_n`. Kazanç sıcak galeride: +1,7 / +1,9 puan, üç fold aynı yön. Her galeri özelliği ihale bazında as-of.
   *M0:* mevcut model, yalnız extract kolonları. *M4b:* M0 + üç küme kolonu; bugünkü nihai model. *Ranker:* sıralama modeli, gruptaki galerileri birbirine göre sıralar. *As-of:* özellik yalnız ihale tarihinden önceki veriden hesaplanır. *Fold:* zaman kesimi; kesim öncesi eğitim, sonrası test. *Sıcak galeri:* kesim öncesi en az bir teklif olayı olan galeri.
3. **Soğuk galeri koltuk kotası** (52-54): kural "en az k soğuk", k=3 (ya da 4), soğuk sıralayıcı M4b skoru. Soğuk galeri "asla teklif vermez" yerine listeye girer; toplam korunur.
   *Soğuk galeri:* kesim öncesi hiç teklif olayı olmayan galeri (ilanı olabilir). *Koltuk:* ilk 30 listesindeki yer. *Soğuk sıralayıcı:* soğuk galerileri kendi aralarında sıralarken kullanılan skor; burada M4b'nin kendi skoru.
4. **Galeri kümeleme YOK** (34-51): üç katman, davranış kümesi, aktiflik oranı, lift, hücre düşürme, soğuk puan; hiçbiri 2'nin üstüne katkı vermedi; galeri düzeyi 305 kolon soğuk galeriyi kümeden iyi sıralıyor. Kümeler kayıtta, veri büyürse yeniden açılır.
   *Üç katman:* galeriyi B2B geçmişi / yalnız ilan / yalnız bölge verisine göre üç ayrı kümelemeye sokmak. *Davranış kümesi:* galerileri hangi araç tiplerine teklif verdiklerine göre kümelemek. *Aktiflik oranı:* kümedeki galerilerin teklif verme oranı. *Lift:* kümenin bir araç tipine oranı ÷ kümenin genel oranı, yani "beklenenden ne kadar fazla". *Hücre:* (galeri kümesi × trim kümesi) çifti. *Soğuk puan:* küme oranı × ilan ölçeğinden türetilen, işe yaramayan soğuk sıralayıcı.
5. **Ölçüm düzeneği sabit:** üç fold (18 Ağu, 25 Ağu, 1 Eyl), altı dilim, Recall@30; kabul = üç fold aynı yön. Tek fold'daki artı karar değildir.
   *Recall@30:* gerçekten teklif veren galerilerin ilk 30 öneriye girme payı. *Dilim:* galeri sıcak/soğuk × trim bilinen/yeni kombinasyonu; her dilim ayrı raporlanır çünkü kazanç ve kayıp farklı dilimlerde olur.
6. **Yeniden açma koşulları:** 12 aylık galeri teklif geçmişi (soğuk dilim küçülür, galeri kümesi × araç tipi ilişkisi ölçülebilir olur) · katalog geneli trim tablosu · trim düzeyinde tüm ilan verisi (bugün 4.324 ilanlı galerinin 1.500'ünde var).
