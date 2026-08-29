# Sentetik galeri-sıralama veri seti — sözlük

**AS-OF 2026-08-28.** Üretim: `01_uret.py` (tohum 42, deterministik) → `02_birlestir.py`.
Gerçek karşılığı: `galeri_scoring_veri_sozlugu_1.xlsx` (Dataset A · dealer 105 kolon,
Dataset B · trim_dealer 120 kolon, Rapor CSV 65 kolon). Burada 6 tablo / 73 kolon var —
**yapı aynı, kolon sayısı temel seviyeye indirilmiş.**

---

## 0. Problem tek cümlede

> Bir ihale oturumunda sırayla satılan 20 aracın her biri için, o oturumdaki ~54 aday
> galeriyi "bu aracı alma ihtimaline göre" sırala.

| kavram | bu veri setinde karşılığı |
|---|---|
| **grup (query)** | bir **lot** = bir araç (`lot_id`). Her grupta ~54 satır. |
| **aday (document)** | o oturuma katılan bir galeri (`galeri_id`) |
| **etiket (relevance)** | `relevans` 0–4 |
| **kayıp** | YetiRank (dereceli alakayı kullanır) |
| **zaman** | `tarih` — bölme zaman bazlı yapılır, rastgele DEĞİL |

**Etiket hunisi iç içedir** (üretimde bu garanti edilir):

```
4 kazandı   ⊂  3 ikinci  ⊂  2 teklif verdi  ⊂  1 detaya baktı  ⊂  0 hiçbir etkileşim
```

4 olan mutlaka teklif de vermiştir, detaya da bakmıştır. Gerçek dağılım:

| relevans | anlamı | pay |
|---|---|---|
| 0 | hiç etkileşim yok | %62,8 |
| 1 | detaya baktı, teklif vermedi | %19,9 |
| 2 | teklif verdi, ilk ikiye giremedi | %13,6 |
| 3 | ikinci oldu | %1,85 (lot başına tam 1) |
| 4 | kazandı | %1,85 (lot başına tam 1) |

---

## 1. Tablolar ve grain

| dosya | grain (bir satır = ) | satır | kolon | gerçek karşılığı |
|---|---|---|---|---|
| `galeriler.csv` | bir galeri | 420 | 9 | Dataset A'nın kimlik bloğu |
| `galeri_snapshot.csv` | (galeri × ay) | 3.360 | 11 | Dataset A'nın sahibinden bloğu, aylık foto |
| `ihaleler.csv` | bir ihale oturumu | 136 | 7 | *(gerçekte yok — Salih'in tarifinden eklendi)* |
| `lotlar.csv` | ihaledeki bir araç | 1.920 | 17 | araç/trim tarafı + Rapor CSV'nin trim bağlamı |
| `etkilesim.csv` | (lot × aday galeri) | 104.060 | 44 | Dataset B · trim_dealer |
| **`egitim_seti.csv`** | **(lot × aday galeri), hepsi birleşik** | **104.060** | **73** | **modele giren tablo** |
| `_gizli_tercihler.csv` | bir galeri (CEVAP ANAHTARI) | 420 | 8 | *(gerçekte yok — modeli sınamak için)* |

---

## 2. `galeriler.csv` — grain: bir galeri

| kolon | ne ölçer | tip | gerçek karşılığı |
|---|---|---|---|
| `galeri_id` | kimlik | metin | `dealer_id` |
| `galeri_adi` | unvan | metin | `dealer_name` |
| `sehir` / `bolge` | galerinin ili / bölgesi | metin | `city` / `region_name` |
| `uyelik_yasi_gun` | platforma katılalı kaç gün | gün | `tenure_days` |
| `alim_yetkisi` | alım yapma yetkisi var mı | bool | `can_buy` |
| `askiya_alinmis` | askıda mı | bool | `suspension_reason IS NOT NULL` |
| `alim_yapabilir` | yetki VE askıda değil | bool | `is_eligible` |
| `ilan_eslesmesi_var` | sahibinden kimliği tuttu mu | bool | `listing_match_found` |

> **`ilan_eslesmesi_var = False` olan galerilerin TÜM `*_ilan_*` ve `alim_butcesi`
> kolonları NULL'dır — 0 değil.** Bu galerilerin gerçekte bütçesi vardır ve üretimdeki
> gerçek kural onu kullanır; biz sadece göremeyiz. Gerçek sistemdeki 200/756 galeri
> durumunun birebir kopyası. NULL'ı 0 ile doldurursan bu galerileri sistematik olarak
> "stoksuz" ilan etmiş olursun.

---

## 3. `galeri_snapshot.csv` — grain: (galeri × ay)

Aylık çekilen sahibinden fotoğrafı. `NULL` = `ilan_eslesmesi_var = False`.

| kolon | ne ölçer | birim | gerçek karşılığı |
|---|---|---|---|
| `snapshot_tarihi` | fotoğrafın çekildiği gün | tarih | `market_anchor_date` |
| `aktif_ilan_adedi` | o an yayında kaç ilan | adet | `active_listing_cnt` |
| `ortalama_ilan_fiyati` | ilan fiyat seviyesi | TL | `avg_listing_price` |
| `ortalama_ilan_km` | ilanların ortalama km'si | km | `avg_listing_km` |
| `ortalama_ilan_model_yili` | ilanların ortalama model yılı | yıl | `avg_listing_year` |
| `ortalama_ilan_omru_gun` | ilan kaç günde kayboluyor | gün | `avg_listing_lifespan_days` |
| `stok_devir_hizi` | aylık stok devri | oran | `turnover_rate` |
| `aylik_satis_tutari` | aylık satış temposu | TL | `avg_monthly_sold_value` |
| `alim_butcesi` | **işaretli** alım kapasitesi | TL | `purchase_budget` |
| `ilan_seri_cesidi` | kaç farklı seri satıyor | adet | `listing_distinct_serie_cnt` |

> `alim_butcesi` **negatif olabilir**: galeri bir ayda çevirdiğinden fazla stok taşıyor
> demektir. Sıfıra kırpma — kırparsan "yeni stok yaptı" ile "hiç satmıyor" aynı görünür.

---

## 4. `ihaleler.csv` ve `lotlar.csv` — ihale tarafı

`ihaleler.csv`: `ihale_id`, `tarih`, `gun_adi` (Pzt/Çar/Cum), `gun_ici_oturum` (1 veya 2),
`hafta_no`, `lot_adedi` (=20), `katilimci_galeri_sayisi` (45–65).

`lotlar.csv` — grain: ihaledeki bir araç:

| kolon | ne ölçer | not |
|---|---|---|
| `lot_id` | **grup anahtarı** | `IH0042-L07` = 42. oturumun 7. aracı |
| `lot_sira` | oturum içi sıra 1–20 | sıralı dinamik burada |
| `marka` / `seri` / `trim` | araç kimliği | 5 marka × 4 seri × 3 trim = 60 trim |
| `model_yili`, `km`, `hasar_skoru` | araç durumu | |
| `muhammen_fiyat` | ihale başlangıç fiyatı | TL |
| `piyasa_medyan_fiyat` | trimin piyasa referansı | `market_trim_median_price` |
| `arac_sehri` | aracın bulunduğu il | mesafe/uzaklık hesabı için |
| `aday_galeri_sayisi` | gruptaki aday sayısı | `aday_sayisi` |
| `teklif_veren_sayisi` | kaç galeri teklif verdi | `market_trim_avg_bidders_per_car` |
| `_kazanan_galeri_id` | kazanan | **alt çizgi = eğitime girmez** |

> **Dikkat:** `marka`, `km`, `muhammen_fiyat` gibi araç kolonları **grup içinde sabittir** —
> 54 satırın hepsinde aynı değer. Sıralama modeli grup içi FARKLARDAN öğrenir, o yüzden
> bu kolonlar tek başlarına sıfır bilgi taşır. Değerleri ancak galeri tarafıyla
> ETKİLEŞİME girdiklerinde ortaya çıkar (`fiyat_orani`, `model_yili_farki`,
> `butce_yeterli_mi`, `ayni_sehir` gibi). Bunlar aşağıdaki "uyum" bloğudur.

---

## 5. `egitim_seti.csv` — modele giren tablo (73 kolon)

### 5.1 Anahtarlar ve etiket (7) — **hiçbiri feature değil**

| kolon | rol |
|---|---|
| `lot_id` | **grup anahtarı** (`group_id`) |
| `ihale_id`, `lot_sira`, `tarih`, `hafta_no` | zaman/bölme; `lot_sira` feature olarak da kullanılabilir |
| `galeri_id` | aday kimliği. **Feature yapma** — model galeri kimliğini ezberler (T4 kimlik ezberi). |
| `relevans` | **etiket** 0–4 |
| `kazandi` | `relevans == 4` türevi; iş metriği için, feature DEĞİL |
| `_gercek_skor` | üretimdeki gizli skor — teşhis için, **sızıntı** |
| `TUZAK_donem_sonu_toplam_alim` | **bilerek konan tuzak**, aşağıda |

### 5.2 Kademeli geçmiş — trim ⊂ seri ⊂ marka (9)

Gerçek Dataset B'nin ana fikri: aynı sinyal üç yakınlık kademesinde ölçülür.
Trim kademesi en dar ve en güçlü, marka en geniş ve en zayıf.

| kolon | ne ölçer | gerçek karşılığı |
|---|---|---|
| `trim_teklif_arac` | bu trim'de kaç araca teklif verdi | `bid_car_cnt_trim` |
| `trim_alim_arac` | bu trim'den kaç araç aldı | `bought_car_cnt_trim` |
| `trim_ikincilik` | bu trim'de kaç kez ikinci oldu | `runner_up_cnt_trim` |
| `trim_son_teklif_gun` | bu trim'e son teklifin üzerinden kaç gün | `days_since_last_bid_trim` |
| `seri_teklif_arac`, `seri_alim_arac` | seri kademesi | `*_serie` |
| `marka_teklif_arac`, `marka_alim_arac` | marka kademesi | `*_make` |
| `marka_son_alim_gun` | bu markadan son alımın üzerinden kaç gün | `days_since_last_purchase_make` |

> Kademeler **iç içedir**: trim sayacı seri sayacının, seri de marka sayacının alt
> kümesidir. `*_son_*_gun` kolonları "hiç olmadı" durumunda **NULL**'dır (0 değil).

### 5.3 Galeri geneli geçmiş (14) — Dataset A karşılığı

| kolon | ne ölçer | gerçek karşılığı |
|---|---|---|
| `teklif_verilen_arac` | toplam kaç araca teklif verdi | `bid_car_cnt` |
| `alinan_arac` | toplam kaç araç aldı | `bought_car_cnt` |
| `alim_donusum_orani` | alım / teklif | `purchase_rate` |
| `ikincilik_orani` | ikincilik / teklif | `runner_up_rate` |
| `ortalama_teklif_sirasi` | teklif verdiğinde ortalama kaçıncı sırada | `avg_bid_rank` |
| `sehir_disi_teklif_orani` | tekliflerinin kaçı başka ildeki araca | `remote_bid_rate` |
| `son_teklif_gun` | son teklifin üzerinden kaç gün | `days_since_last_bid` |
| `son_alim_gun` | son alımın üzerinden kaç gün | `days_since_last_purchase` |
| `aclik_farki_gun` | `son_alim_gun − son_teklif_gun` | `hunger_gap_days` |
| `alinan_fiyat_ort` | aldığı araçların ortalama fiyatı | `bought_price_avg` |
| `alinan_model_yili_ort` | aldığı araçların ortalama model yılı | `bought_model_year_p50` |
| `farkli_seri_sayisi` | kaç farklı seride teklif verdi | `distinct_serie_cnt` |
| `en_buyuk_seri_payi` | en çok teklif verdiği serinin payı | `top_serie_share` |
| `katildigi_ihale_sayisi` | kaç ihale oturumuna girdi | `auction_cnt` |

**Oranlar yumuşatılmamıştır** (gerçek sistemde de öyle): 2 araca teklif verip 1'ini alan
galeri `alim_donusum_orani = 0,50` gösterir. Her oranı kendi paydasıyla birlikte oku.

### 5.4 Uyum bloğu (11) — araç ile galeriyi ÇARPIŞTIRAN kolonlar

Sıralama sinyalinin çoğu buradadır; grup içinde değişen tek şey bunlar ve galeri geçmişi.

| kolon | ne ölçer | gerçek karşılığı |
|---|---|---|
| `ayni_sehir` / `ayni_bolge` | galeri ile araç aynı il/bölgede mi | `remote_bid_rate`'in çift hâli |
| `fiyat_orani` | `muhammen_fiyat / alinan_fiyat_ort` | `trim_price_to_dealer_median_ratio` |
| `model_yili_farki` | araç yılı − galerinin aldığı ortalama yıl | `model_year_gap` |
| `bu_trimde_ilani_var` | şu an bu trim'de vitrininde araç var mı | `is_listing_trim_now` |
| `raf_bos_gun` | bu trim'i satmış, yerine koymamış — kaç gündür boş | `restock_overdue_days` |
| `butce_yeterli_mi` | `alim_butcesi ≥ muhammen_fiyat` | `budget_covers_one_car` |
| `butce_arac_karsiligi` | bütçe kaç araç eder | `budget_units_affordable` |
| `ilan_fiyat_orani` | araç fiyatı / galerinin ilan fiyat seviyesi | `price_band_overlap_ratio` yerine |
| `muhammen_piyasa_orani` | ihale fiyatı piyasanın kaçta kaçı | `trim_bid_to_market_price_ratio` |
| `arac_yasi` | 2026 − model yılı | — |

### 5.5 Sıralı ihale dinamiği (3) — **gerçek sözlükte yok, Salih'in tarifinden**

20 araç sırayla satılıyor. Oturumun başında araç alan galerinin bütçesi ve istahı azalır.

| kolon | ne ölçer |
|---|---|
| `oturumda_onceki_alim` | bu oturumda, bu lottan ÖNCE kaç araç aldı |
| `oturumda_onceki_teklif` | bu oturumda, bu lottan ÖNCE kaç araca teklif verdi |
| `oturumda_kalan_lot` | `20 − lot_sira` (daha kaç araç var) |

Bu üçü, satırların **grup içinde bağımsız olmadığını** açığa çıkarır: aynı oturumun
lotları birbirini etkiler. Zaman bölmesinin ihale sınırından yapılması bu yüzden şart.

### 5.6 Gürültü (2) ve tuzak (1) — sınama kolonları

| kolon | amaç |
|---|---|
| `gurultu_1` | N(0,1), gerçek kuralda katsayısı **tam 0** |
| `gurultu_2` | U(0,100), katsayısı **tam 0** |
| `TUZAK_donem_sonu_toplam_alim` | galerinin TÜM dönem boyunca (gelecek dahil) aldığı araç sayısı |

Gürültü kolonları modelin ezberleyip ezberlemediğinin ölçüsüdür: önem sıralamasında
dibe yakın olmalılar. **Tam sıfıra inmezler** — sürekli bir kolon üzerinde ağaç her
zaman bir miktar bölme yapar; ölçüt "sıfır" değil, "gerçek sinyallerin çok altında".

`TUZAK_` kolonu klasik zaman sızıntısıdır: değeri geleceği içerir, eğitime sokulursa
test skoru sahte yükselir. `03_egit.py --tuzak` ile etkisi ölçülebilir.

---

## 6. Veriye gömülü GERÇEK KURAL (cevap anahtarı)

Model bunu bilmiyor; keşfetmeye çalışacak.

```
gercek_skor =
  + 2.0·ln(1+trim_alim_arac)              kademe 1 — en güçlü
  + 0.8·ln(1+seri_alim_arac)              kademe 2
  + 0.3·ln(1+marka_alim_arac)             kademe 3 — en zayıf
  + 1.6·gizli_marka_uyumu                 GÖZLENEMEZ (yalnız _gizli_tercihler.csv'de)
  − 1.5·|ln(muhammen/tercih_fiyat)|/esneklik    U ŞEKLİ — monoton değil
  + 1.0·ayni_sehir + 0.4·ayni_bolge
  + 1.5·(butce_yeterli VE son_teklif_gun≤14)    ETKİLEŞİM
  + 0.9·raf_bos_sinyali
  − 0.02·son_teklif_gun
  − 1.2·oturumda_onceki_alim              SIRALI DİNAMİK
  + 0.6·aktiflik  + 0.8·uzak_egilim·(1−ayni_sehir)
  + Gumbel(0, 0.9)                        bireysel gürültü
```

Beş öğretici özelliği:

1. **Kademe hiyerarşisi** (2,0 > 0,8 > 0,3) — mevcut sistemdeki `k_seri` / `k_marka`
   elle-ayar tartışmasının karşılığı. Burada doğru değerleri biliyoruz.
2. **Etkileşim** (`bütçe VE tazelik`) — ağırlıklı toplam bunu **yapısal olarak**
   yakalayamaz: yüksek bütçe tek başına ödül vermiyor, ancak tazelikle birlikte veriyor.
3. **U şekilli fiyat uyumu** — ne çok ucuz ne çok pahalı; monoton değil, ağaç gerekir.
4. **Sıralı dinamik** — satırlar i.i.d. değil.
5. **Gürültü kolonları** — ezberin kanıtı.

`_gizli_tercihler.csv` cevap anahtarıdır: `gizli_tercih_marka`, `gizli_tercih_fiyat`,
`gizli_aktiflik` … Model bunları hiç görmez; sayaçlardan dolaylı çıkarması beklenir.
Eğitim bittikten sonra "model gizli tercihi buldu mu" diye buradan bakılır.

---

## 7. Zaman sadakati — en önemli tasarım kararı

Bir lotun satırındaki **tüm** geçmiş sayaçları, o lot açılmadan önceki durumdur.
Simülasyon lot lot kronolojik ilerler: önce satır yazılır, **sonra** sayaç güncellenir.
Bu yüzden veri setinde zaman sızıntısı yoktur — tek istisna `TUZAK_` kolonudur.

- **Isınma:** takvim 2026-01-05'te başlar, eğitim setine 2026-03-16'dan itibaren yazılır.
  İlk ~10 hafta yalnız geçmiş biriktirir; soğuk başlangıç sayaçları sıfır olmasın diye.
- **Snapshot as-of join:** 12 Nisan'daki lot için 1 Nisan fotoğrafı kullanılır,
  1 Mayıs fotoğrafı **kullanılamaz**. `02_birlestir.py` bunu
  `pd.merge_asof(direction="backward")` ile yapar. Gecikme 0–30 gün, medyan 14.
- **Bölme:** eğitim ≤ 2026-07-05 · doğrulama 07-06…07-31 · test 08-01…08-28.
  Rastgele bölme burada **yanlıştır**: aynı ihalenin satırları eğitime ve teste
  dağılırsa model geleceği görmüş olur.

---

## 8. Gerçek sisteme göre BİLEREK atlananlar

Sentetik veri bunları taşımıyor; gerçek veriye geçerken karşına çıkacaklar:

| atlanan | gerçekte ne | neden atlandı |
|---|---|---|
| ilan kimliği çözümü | `raw_id` ilan anahtarı değil (bir ilan ~4,8 `raw_id`) | ETL detayı, model tarafını ilgilendirmiyor |
| üç ayrı saat | `date` / `loaded_at` (kullanılmaz) / `import_date` | burada tek zaman var |
| "kayboldu ≠ satıldı" | %18,6 relisting churn | `raf_bos_gun` gürültüsüz varsayıldı |
| fiyat kapsamı | `active_listing_price_coverage` | fiyatsız ilan yok sayıldı |
| sansür | `censored_listing_ratio` | ilan ömrü tam gözlemli varsayıldı |
| nötr dolgu 50 | ölçülemeyen bileşen 50. yüzdelik sayılır | model NULL'ı kendisi işliyor |
| `p_fiyat` RANK hatası | beraberlikte grubun en düşük sırası | rapor tarafı, model tarafı değil |
| seyreklik | Dataset B satırı ancak sinyal varsa oluşur | burada tam CROSS JOIN üretiliyor |

Son satır önemli: gerçek Dataset B **seyrek**tir, satır yokluğu "hiç ilgilenmemiş"
demektir. Sentetikte her (lot × aday galeri) çifti için satır var, çünkü `relevans = 0`
satırları sıralama modelinin negatif örnekleridir. Gerçek veride bu satırları
`CROSS JOIN` ile kendin üretmen gerekecek.
