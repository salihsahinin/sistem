# Tablo Normalizasyonu — sıfırdan, ölçümlü

*Ders notu · 2026-08-21 · Salih için, Carvis/Opus 5 · yöntem: her iddia ya tanımdan türetildi ya da yerel koşumla ölçüldü.*
*Betikler: `ogrenme/dersler/2026-08-21-normalizasyon-kod/` — hepsi bağımsız çalışır (`python3 <dosya>`), harici bağımlılık yok, bellek-içi SQLite kullanır.*
*Ölçüm şartı: tek makine (Mac), SQLite (satır-deposu), tek veri kümesi, eşzamanlılık yok. Sayılar **yön göstericidir**, evrensel sabit değildir; kolonsal motorda (DuckDB/Parquet/Snowflake) özellikle depolama rakamı değişir — bu not içinde nerede değişeceği işaretlendi.*

---

## 0. Bu notun kullanımı

Sıra önemli: 2. ve 3. bölümdeki iki terim (fonksiyonel bağımlılık, anahtar) oturmadan normal formlar ezber olur. Her bölümde aynı üç adım var — **cevapladığı soru → tanım → ölçülmüş örnek**.

12. bölüm (OLAP'ta optimum normalizasyon) diğerlerinden bağımsız okunabilir, ama 10. bölümdeki maliyet ölçümüne dayanıyor.

---

## 1. Neden var: tek geniş tablonun üç arızası

Örnek — her satır bir sipariş kalemi:

| siparis_no | urun_kod | adet | musteri_no | musteri_ad | musteri_sehir | sehir_plaka | urun_ad | urun_fiyat |
|---|---|---|---|---|---|---|---|---|
| 1 | K-10 | 2 | 100 | Ahmet Yılmaz | Ankara | 6 | Klavye | 450 |
| 1 | M-20 | 1 | 100 | Ahmet Yılmaz | Ankara | 6 | Mouse | 250 |
| 2 | K-10 | 1 | 100 | Ahmet Yılmaz | Ankara | 6 | Klavye | 450 |
| 3 | M-20 | 3 | 200 | Zeynep Kaya | İzmir | 35 | Mouse | 250 |

"Ahmet Yılmaz / Ankara / 6" üç kez, "Klavye / 450" iki kez yazılı. Bu tekrar üç somut arıza üretir *(betik: `01-anomaliler.py`)*:

**(a) Güncelleme anomalisi.** Klavye 500 TL oldu, `UPDATE` bir satıra çarptı:
```
urun_kod | urun_ad | farkli_fiyat_sayisi | fiyatlar
K-10     | Klavye  | 2                   | 500.0, 450.0
```
Veritabanı aynı ürün için iki gerçek taşıyor; hangisinin doğru olduğu bilinmiyor.

**(b) Silme anomalisi.** Zeynep'in tek siparişi silindi → müşteri kaydı da gitti (`kalan_zeynep_satiri = 0`). Silinmek istenen sipariş, kaybedilen müşteri.

**(c) Ekleme anomalisi.** Henüz sipariş vermemiş müşteri yazılamıyor:
```
NOT NULL constraint failed: siparis_duz.siparis_no
```

> **Kenar bilgi (SQLite):** `PRIMARY KEY` sütunlarına `NOT NULL` yazılmazsa SQLite NULL kabul eder — eski uyumluluk hatası. İlk denemede anomali görünmedi, `NOT NULL` eklenince göründü.

Üçünün de tek kökü var: **bir tabloda birden fazla türden gerçek saklanıyor** — sipariş, müşteri, şehir, ürün.

---

## 2. Fonksiyonel bağımlılık

### Cevapladığı soru
> "Bir sütunun değerini bilirsem, başka bir sütunun değerini kesin olarak bilir miyim?"

### Tanım

**X → Y** ("X, Y'yi belirler"):

> X sütununda aynı değeri taşıyan iki satır, Y sütununda farklı değer taşıyamaz.

"Fonksiyonel" matematikten gelir: fonksiyon aynı girdiye hep aynı çıktıyı verir — `f(Bilgisayar) = Prof. Demir`, her seferinde.

### Ölçme kalıbı *(betik: `02-bagimlilik-anahtar.py`)*

Bu notun tamamında kullanılan **tek** sorgu kalıbı budur:

```sql
SELECT <X>, COUNT(DISTINCT <Y>) FROM tablo GROUP BY <X> HAVING COUNT(DISTINCT <Y>) > 1;
```

Boş dönerse: veri, `X → Y` iddiasını **çürütmüyor**.

Örnek tablo:
```
ogrenci_no | ad     | bolum      | bolum_baskani
101        | Ahmet  | Bilgisayar | Prof. Demir
102        | Zeynep | Bilgisayar | Prof. Demir
103        | Mert   | Makine     | Prof. Kaya
104        | Elif   | Makine     | Prof. Kaya
```
```
bolum      | farkli_baskan
Bilgisayar | 1
Makine     | 1               → bolum → bolum_baskani çürütülmedi
```

### En kritik nokta: veri kanıtlamaz, yalnız çürütür

`ad → bolum` iddiası dört satırda "geçiyor" görünüyordu. Bir satır eklendi — `(105, Ahmet, Makine, ...)`:
```
ad     | farkli_bolum
Ahmet  | 2        ← ihlal
```

**Fonksiyonel bağımlılık veriden okunmaz, iş kuralından gelir.** Tasarımda sorulacak soru "bu tabloda öyle mi?" değil, **"kurallara göre başka türlü olabilir mi?"**dir.

### Yön

`X → Y` ile `Y → X` farklı iki iddiadır, biri diğerini gerektirmez. Bir profesör iki bölüme başkanlık edebiliyorsa `bolum_baskani → bolum` yoktur, ama `bolum → bolum_baskani` durur.

### Neden umursanır

Her fonksiyonel bağımlılık bir tekrar üretir. Bilgisayar bölümünde 500 öğrenci varsa "Prof. Demir" 500 kez yazılıdır. Bütün normalizasyon tek gözlemin üstüne kurulu:

> Bir tabloda `X → Y` varsa **ve** `X` o tablonun anahtarı **değilse**, `Y` gereksiz tekrar ediyordur.

---

## 3. Anahtar

### Cevapladığı soru
> "Bir satırı diğerlerinden ayırmak için hangi sütun(lar)a bakmam yeter?"

### Süper anahtar

Değeri satırın **bütün** sütunlarını belirleyen sütun kümesi — yani `X → (tüm sütunlar)`. Dikkat: bu, 2. bölümün ta kendisi. **Anahtar, sağ tarafında tablonun tamamı olan özel bir fonksiyonel bağımlılıktır.**

Ölçme kalıbı: *o sütunun farklı değer sayısı, satır sayısına eşit mi?*
```
satir | farkli_no | farkli_ad | farkli_bolum
5     | 5         | 4         | 2
```
- `ogrenci_no`: 5 = 5 → ayırt ediyor ✔
- `ad`: 4 ≠ 5 → ayırt etmiyor ✘
- `bolum`: 2 ≠ 5 → ayırt etmiyor ✘

Sezgi: **tekrar eden hiçbir şey anahtar olamaz.**

### Aday anahtar

Fazlalık taşımayan süper anahtar. `{ogrenci_no, ad}` süper anahtardır ama `ad` atılınca hâlâ çalıştığı için aday anahtar **değildir**; `{ogrenci_no}` aday anahtardır. Bir tabloda birden fazla aday anahtar olabilir (`tc_kimlik_no` ve `sicil_no` gibi).

### Birincil anahtar

Aday anahtarlardan **seçilen** tanesi (`PRIMARY KEY`). Seçilmeyen diğer aday anahtarlara `UNIQUE` konur — konmazsa tekrar sızar.

### Bileşik anahtar

Birden çok sütundan oluşan anahtar: `ders_kaydi(ogrenci_no, ders_kodu, not)` tablosunda ne biri ne öbürü tek başına yeter; ikisi birlikte belirler. Bazı normal form kuralları yalnız bu durumda anlam kazanır.

### Asal / asal olmayan sütun

- **Asal:** herhangi bir aday anahtarın parçası olan sütun.
- **Asal olmayan:** hiçbirinin parçası olmayan, "sadece bilgi taşıyan" sütun.

---

## 4. 1NF — hücrede kaç değer var?

**Tanım.** Tablo 1NF'tedir ⟺ (1) her hücrede tek değer, (2) tekrarlayan sütun grubu yok, (3) satırları ayıran bir anahtar var.

### İhlal 1 — hücrede liste *(betik: `03-1nf.py`)*

```
ogrenci_no | ad     | dersler
101        | Ahmet  | MAT1,FIZ2
102        | Zeynep | MAT10
103        | Mert   | FIZ2,MAT1
```
"MAT1 dersini kimler alıyor?" → `WHERE dersler LIKE '%MAT1%'`:
```
101 | Ahmet  | MAT1,FIZ2
102 | Zeynep | MAT10        ← YANLIŞ: Zeynep MAT1 almıyor
103 | Mert   | FIZ2,MAT1
```
Veritabanı yanlış cevap verdi ve bunu bildirmedi; `MAT1` metni `MAT10`'un içinde geçiyor. Elle düzeltmesi mümkün (`','||dersler||',' LIKE '%,MAT1,%'` → doğru sonuç), ama artık her sorguda bu kurgu tekrarlanmak zorunda; bir boşluk ya da büyük-küçük harf farkı sessizce yanlış sonuç üretir.

**Ölçülmüş ikinci maliyet — indeks kullanılamıyor:**
```
ayrı satırlarda :  SEARCH telefon USING INDEX ix_tel (numara=?)
tek hücrede CSV :  SCAN kisi_duz
```
`LIKE '%...%'` deseni indeks kullanamaz; hücre içindeki değerler indekslenemez.

**Üçüncü maliyet:** sayamazsın. "Kimin kaç dersi var?" için virgül saymak gerekir (`LENGTH(x)-LENGTH(REPLACE(x,',',''))+1`), boş hücre özel durumdur. Ayrı satırlarda soru `COUNT(*)` ile biter.

### İhlal 2 — tekrarlayan sütun grubu

`ders1, ders2, ders3`: dördüncü ders `ALTER TABLE` gerektirir · arama `OR` zinciri olur · hücrelerin çoğu `NULL` · ders sayısı sütun sayısıyla sınırlanır.

### "Atomik" bağlama bağlıdır

| Sütun | Atomik mi | Neden |
|---|---|---|
| `adres` (tek metin), şehir kırılımı raporlanıyorsa | Hayır | Şehri çıkarmak için string parçalanıyor |
| Aynı sütun, yalnız kargo etiketine basılıyorsa | Evet | Hiç parçalanmıyor |
| `dogum_tarihi` | Evet | Yıl gerekince `strftime`/`EXTRACT` var; bu tipin kendi işlemi |

**Ölçüt:** sorgularında o hücreyi parçalamak zorunda kalıyorsan atomik değildir.

---

## 5. 2NF — anahtarın tamamına mı, parçasına mı?

> **2NF yalnızca anahtarın bileşik olduğu tablolarda anlamlıdır.** Anahtar tek sütunsa, tablo 1NF olduğu anda 2NF'i de sağlar (parçası yoktur, kısmi bağımlılık tanımı gereği imkânsızdır).

**Kısmi bağımlılık:** asal olmayan bir sütunun, aday anahtarın **tamamına** değil bir **parçasına** bağlı olması.

### Örnek *(betik: `04-2nf.py`)*

```
ogrenci_no | ders_kodu | notu | ogrenci_ad | ders_ad     | kredi
101        | MAT1      | 75   | Ahmet      | Matematik I | 6
101        | FIZ2      | 60   | Ahmet      | Fizik II    | 5
102        | MAT1      | 90   | Zeynep     | Matematik I | 6
103        | MAT1      | 55   | Mert       | Matematik I | 6
103        | FIZ2      | 80   | Mert       | Fizik II    | 5
```
Anahtar `{ogrenci_no, ders_kodu}`. Her parça için ayrı test:

```
ogrenci_no | farkli_ad          ders_kodu | farkli_ders_ad | farkli_kredi
101        | 1                  FIZ2      | 1              | 1
102        | 1                  MAT1      | 1              | 1
103        | 1
→ ogrenci_no → ogrenci_ad      → ders_kodu → ders_ad, kredi
   (kısmi bağımlılık)             (kısmi bağımlılık)
```
Karşılaştırma — `notu` için anahtarın tamamı gerekiyor (`101` için iki farklı not var) → **tam bağımlılık**, doğru yerde duruyor.

**Zararı:**
```
MAT1 dersinin adı+kredisi : 3 satırda yazılı
Ahmet adı                 : 2 satırda yazılı
```
Kredi 6→7 yapıldı, `UPDATE` bir satıra çarptı → `MAT1 | 7,6`.

### Ayrıştırma reçetesi

> **Bağımlılığın sol tarafı yeni tablonun anahtarı olur, sağ tarafı oraya taşınır.**

| Bağımlılık | Yeni tablo |
|---|---|
| `ogrenci_no → ogrenci_ad` | `ogrenci(ogrenci_no, ad)` |
| `ders_kodu → ders_ad, kredi` | `ders(ders_kodu, ad, kredi)` |
| `(ogrenci_no, ders_kodu) → notu` | `kayit(ogrenci_no, ders_kodu, notu)` |

Sonuç: kredi değişikliği **tek** satır; `JOIN` eski görünümü tutarlı biçimde verir; ders almamış öğrenci (`104 Elif`) yaşayabiliyor.

**Resmi tanım:** 1NF'tedir ve hiçbir asal olmayan sütun, herhangi bir aday anahtarın gerçek bir parçasına bağlı değildir.

---

## 6. 3NF — anahtara mı, başka bir sütuna mı?

**Geçişli bağımlılık:** anahtar → B → C zinciri, B anahtar değil.

### Köprü: 2NF geçti, tekrar duruyor *(betik: `05-3nf-tarayici.py`)*

```
ogrenci_no | ad     | bolum      | bolum_baskani     ← anahtar tek sütun: 2NF otomatik
...
bolum      | bolum_baskani | kac_satirda_yazili
Bilgisayar | Prof. Demir   | 3
Makine     | Prof. Kaya    | 2
```

### Otomatik bağımlılık tarayıcısı

Tüm sütun çiftlerini 2. bölümdeki kalıpla tarayan döngü:
```
ogrenci_no    -> ad              (sol taraf anahtar mı? EVET)
ogrenci_no    -> bolum           (EVET)
ogrenci_no    -> bolum_baskani   (EVET)
ad            -> ogrenci_no      (EVET)   ← yanılsama, aşağıya bak
ad            -> bolum           (EVET)   ← yanılsama
bolum         -> bolum_baskani   (HAYIR ← tekrar kaynağı)
bolum_baskani -> bolum           (HAYIR ← tekrar kaynağı)
```
**Okuma:** sol tarafı anahtar olan satırlar normaldir (anahtar zaten her şeyi belirler). Sol tarafı anahtar **olmayanlar** aranan şeydir.

**İki uyarı:** (1) `ad → ogrenci_no` bu 5 satırda isim tekrarı olmadığı için çıktı; kural "isimler tekrar edebilir" diyorsa yoktur. (2) `bolum_baskani → bolum` de aynı şekilde kurala tabidir. **Tarayıcı aday üretir, karar vermez.**

### Tanım

**Kullanışlı hâli:** her `X → Y` için ya `X` süper anahtardır, ya `Y` asaldır.
`bolum → bolum_baskani`: ikisi de değil → **ihlal**.

**Ezber cümlesi:** her sütun *anahtara* (1NF), *anahtarın tamamına* (2NF), *yalnızca anahtara* (3NF) bağlı olmalı.

### Ayrıştırma ve ölçüm

`bolum(ad, baskan)` + `ogrenci(ogrenci_no, ad, bolum)`.

| "Bölüme yeni başkan" işlemi | Etkilenen satır |
|---|---|
| Bölmeden önce | **3** |
| Bölmeden sonra | **1** |

3 yerine 1 sadece hız değil: çok satırlı güncelleme yarıda kesilirse tablo tutarsız kalır. Yan kazanç: öğrencisi olmayan bölüm (`Elektrik`) artık var olabiliyor.

---

## 7. BCNF — 3NF'in bıraktığı kaçak

3NF'in "**ya da** `Y` asaldır" şartı bir kaçak kapısıdır: tablodaki bütün sütunlar asalsa 3NF hiçbir şeye itiraz edemez.

### Örnek *(betik: `06-bcnf-kayipsiz.py`)*

Kurallar: her hoca **tek** ders verir · bir derste **çok** hoca olabilir · bir öğrenci bir dersi **tek** hocadan alır.

```
ogrenci | ders | hoca
Ahmet   | MAT1 | Prof. Demir
Zeynep  | MAT1 | Prof. Demir
Mert    | MAT1 | Prof. Kaya
Ahmet   | FIZ2 | Prof. Ates
```
Aday anahtar taraması (4 satır):
```
satir | ogrenci | ders | hoca | ogrenci+ders | ogrenci+hoca | ders+hoca
4     | 3       | 2    | 3    | 4 ✔          | 4 ✔          | 3 ✘
```
İki aday anahtar: `{ogrenci, ders}` ve `{ogrenci, hoca}` → **üç sütun da asal** → 3NF sağlanıyor. Ama:
```
hoca        | farkli_ders | kac_satirda
Prof. Demir | 1           | 2            ← "Demir MAT1 verir" iki kez yazılı
```

**BCNF tanımı:** her `X → Y` için `X` süper anahtar olmalı. `hoca → ders`'te `hoca` süper anahtar değil → ihlal.

**Ayrıştırma:** `hoca_ders(hoca, ders)` + `ogrenci_hoca(ogrenci, hoca)` → tekrar biter, `JOIN` orijinali verir.

### Bedeli: bağımlılık koruma kaybı

`(ogrenci, ders) → hoca` kuralı iki tabloya dağıldı. Ahmet MAT1'i Demir'den alıyorken Kaya'ya da yazıldı:
```
INSERT INTO ogrenci_hoca VALUES ('Ahmet','Prof. Kaya');   → KABUL EDİLDİ
```
İhlal ancak `JOIN` edince görünüyor:
```
ogrenci | ders | kac_hoca
Ahmet   | MAT1 | 2
```

| | Kayıpsız bölme | Bağımlılık koruma |
|---|---|---|
| 3NF | Her zaman mümkün | Her zaman mümkün |
| BCNF | Her zaman mümkün | **Garanti yok** |

**Pratik kural:** 3NF'e kadar git, orada dur. Kalan BCNF ihlali gerçekten acı veriyorsa (çok satır × sık güncelleme) böl, ama kaybettiğin kuralı nereye taşıdığını yaz. BCNF ihlali ancak birden fazla örtüşen bileşik aday anahtar varsa çıkar; günlük şemaların çoğunda 3NF = BCNF'tir.

---

## 8. 4NF — bağımsız iki "çoklu gerçek"

*(betik: `07-4nf.py`)*

Çalışanın becerileri ve bildiği diller — ikisi de çoklu, birbirinden bağımsız. Tek tabloda her kombinasyon yazılmak zorunda:
```
Ahmet | Python | Ingilizce        2 beceri × 2 dil = 4 satır
Ahmet | Python | Almanca          3. beceri eklenince → 6 satır
Ahmet | SQL    | Ingilizce        (beceri başına dil sayısı kadar satır)
Ahmet | SQL    | Almanca
```
Büyüme `m × n`. Ayrıca satırlardan biri unutulursa tablo *var olmayan bir gerçeği* ifade eder ("Docker'ı sadece İngilizce biliyor").

İki ayrı tablo: 3 + 2 = **5 satır**; yeni dil **tek** `INSERT`. Büyüme `m + n`. 10 beceri + 5 dil olsaydı: 50 → 15 satır.

**Tanım (4NF):** Bir tabloda birbirinden bağımsız birden fazla çok-değerli gerçek bulunamaz.
**Testi:** *bir satır eklerken, ilgisiz başka bir sütun yüzünden birden fazla satır yazmak zorunda mıyım?*

*(5NF: üçlü ilişkilerin ikililere bölünebildiği nadir durum; adını bilmek yeter.)*

---

## 9. Ayrıştırmanın geçerliliği

### Kayıpsız birleşim

> Bir tabloyu A ve B'ye bölerken, **ortak sütunlar A'da veya B'de süper anahtar olmalıdır.**

Sağlanmazsa *(betik: `06-bcnf-kayipsiz.py`)*: `parca_a(ad, bolum)` + `parca_b(bolum, no)`, ortak sütun `bolum` hiçbirinde anahtar değil.
```
Orijinal: 3 satır          JOIN sonucu: 5 satır
                           Ahmet  | Makine | 102   ← uydurma
                           Zeynep | Makine | 103   ← uydurma
```
Veri kaybolmadı, **veri uyduruldu** — asıl tehlike budur.

5. bölümün reçetesi ("bağımlılığın sol tarafını yeni tablonun anahtarı yap") bu şartı otomatik sağlar.

### Bağımlılık koruma

Her kural tek bir tabloda denetlenebilir kalmalı (7. bölüm). Kalmıyorsa kuralı trigger'a, türetilmiş bir `UNIQUE`'e ya da uygulama koduna taşırsın — ücretsiz çözüm yok.

---

## 10. Bedeli — ölçüm

*(betik: `08-maliyet-olcum.py`)* Aynı veri iki kopya: 3NF (üç tablo) ve tek geniş tablo.
`kalem 300.000 · musteri 20.000 · urun 500`

**Tek satır okuma (OLTP tipi):**

| | Süre | Plan |
|---|---|---|
| 3NF (3 tablo JOIN) | **0.001 ms** | `SEARCH k USING INTEGER PRIMARY KEY` + 2 indeks araması |
| Geniş tablo | **0.001 ms** | `SEARCH genis USING INDEX ix_g_id` |

**Fark yok.** JOIN'in maliyeti "tablo sayısı" değil **taranan satır sayısı**dır.

> İlk ölçümde geniş tablo 3.7 ms çıkmıştı — `CREATE TABLE AS` ile üretilen tabloda indeks yoktu, motor 300 bin satır tarıyordu. Karşılaştırdığın iki tarafın aynı şartlarda olduğunu doğrulamadan ölçüm okunmaz.

**Analitik sorgu (kategori × şehir ciro):**

| | Süre |
|---|---|
| 3NF | 266.1 ms |
| Geniş tablo | 120.6 ms → **2.2× hızlı** |

```
[3NF]     SCAN k                              ← 300 bin satır
          SEARCH u USING INDEX (urun_kod=?)   ← her satır için
          SEARCH m USING INDEX (musteri_no=?) ← her satır için
[geniş]   SCAN genis                          ← hepsi bu
```

**Yazma (bir ürünün fiyatı değişti):**

| | Etkilenen satır | Süre |
|---|---|---|
| 3NF | **1** | 0.035 ms |
| Geniş tablo | **578** | 0.583 ms → **16×** |

---

## 11. Denormalizasyon

**Tanım:** okuma hızı için tekrarı bilerek geri getirmek.

> **Tekrarın kendisi değil, nasıl güncellendiği tehlikelidir.** Elle güncellenen tekrar anomali üretir; bir kaynaktan **türetilen** tekrar üretemez — kaynak tektir, kopya çıktıdır.

Güvenliden riskliye:

1. **`VIEW`** — tekrar yok, sadece sorguya isim. Hız kazancı da yok.
2. **Özet tablo / materialized view** — türetilmiş tekrar; tek sorumluluk *tazelik*.
3. **`GENERATED COLUMN` / trigger** — senkronizasyondan motor sorumlu.
4. **Elle çoğaltılan sütun** — yalnız 1-3 yetmediyse ve **ölçüldüyse**.

### Zamana bağlı değer tuzağı

1. bölümdeki örnekte fiyat `urun` tablosuna taşınınca, fiyat değişince **geçmiş siparişler de değişti**. Bu normalizasyon başarısı değil, modelleme hatasıdır:

- "Ürünün **güncel** fiyatı" → `urun` tablosunun özelliği
- "Satış **anındaki** birim fiyat" → siparişin kendi özelliği

Aynı görünen iki farklı gerçek. **Zamana bağlı değerler olayın yanına yazılır** (fatura adresi, kur, vergi oranı, satış fiyatı).

---

## 12. OLAP'ta optimum normalizasyon: yöntem ve metrikler

> **AÇIK BORÇ (Salih, 2026-08-21):** bu bölüm yüzeysel kaldı — anlaşılmadı. Diğer bölümlerdeki gibi *cevapladığı soru → tanım → ölçülmüş örnek* ritmiyle, terim terim yeniden yazılacak. Aşağıdaki içerik ve 12.5b ölçümleri o yazımın ham maddesidir.

OLTP'de cevap hazırdı: 3NF. OLAP'ta hazır cevap yok, çünkü tekrarın tehlikesi ortadan kalkıyor (ambar türevdir, kaynak değil) ve geriye saf bir **maliyet optimizasyonu** kalıyor. O yüzden burada "kural" değil **ölçüm prosedürü** kullanılır.

### 12.1 Normalizasyondan önceki karar: tanecik (grain)

Fact tablosunun taneciği bir cümleyle yazılır: *"Bir satır = bir sipariş kalemi"*. Yanlış tanecik hiçbir normalizasyon seviyesiyle kurtarılamaz; çift sayım oradan doğar.

**Doğrulama metriği:** `COUNT(*) = COUNT(DISTINCT <tanecik anahtarı>)`. Eşit değilse tanecik iddian yanlış.

### 12.2 Seçenek uzayı — tek eksende dört durak

| Şema | Ne demek | Tipik yeri |
|---|---|---|
| **3NF ambar** (Inmon tarzı) | Kaynağa yakın, tam ayrıştırılmış entegrasyon katmanı | Silver / entegrasyon |
| **Yıldız** (Kimball) | 1 fact + denormalize boyutlar | Gold — OLAP varsayılanı |
| **Kar tanesi** (snowflake) | Boyutun kendisi de bölünmüş | Boyut devasa ya da paylaşımlıysa |
| **OBT** (tek geniş tablo) | Boyutlar fact'e gömülü | Dar ve kararlı sorgu seti |

**Önemli çerçeve düzeltmesi:** modern ambarda "bir seviye seçilmez", **katman başına seviye** seçilir. Ham → entegre (3NF'e yakın) → sunum (yıldız/OBT). Sunum katmanındaki tekrar tehlikesizdir çünkü **yeniden üretilebilir**. Karar sorusu şuna dönüşür: *bu tablo kaynak mı, türev mi?*

### 12.3 Karar yöntemi: iş yükü güdümlü A/B ölçümü

1. **İş yükü envanteri.** Gerçek sorgu geçmişinden top-N sorgu + frekans ağırlığı çıkar (Snowflake `QUERY_HISTORY`, BigQuery `INFORMATION_SCHEMA.JOBS`, dbt manifest, Postgres `pg_stat_statements`). Tahminle değil, ağırlıkla çalışılır.
2. **Kısıtları yaz.** Tanecik · tarihsel doğruluk (SCD tipi) · tazelik SLA'sı. Bunlar optimizasyondan **önce** gelir; kısıt ihlal eden aday elenir, ne kadar hızlı olursa olsun.
3. **2-3 aday şema kur.** Örneklem üstünde (%1-10) — ama kardinalite ve seçicilik korunmalı, rastgele örneklem boyut kardinalitesini bozar.
4. **Aynı iş yükünü ikisinde koş**, metrikleri topla (12.4).
5. **Ağırlıklı maliyeti hesapla:**

   `Toplam = Σ_q (frekans_q × okuma_maliyeti_q) + tazeleme_maliyeti + depolama_maliyeti + düzeltme_maliyeti × düzeltme_olasılığı`

6. **Kararı ve yeniden açma koşulunu yaz:** "hangi metrik ne kadar değişirse bu karara yeniden bakılır" (ör. boyut tablosu 10⁶ satırı geçerse, ya da filtre sütunu kullanım oranı %40'ın altına düşerse).

### 12.4 Metrikler

| # | Metrik | Nasıl ölçülür | Neyi belirler |
|---|---|---|---|
| 1 | **Taranan byte / sorgu** | BigQuery `bytes_billed` · Snowflake `bytes_scanned` · DuckDB `EXPLAIN ANALYZE` | OLAP'ın asıl para birimi; satır değil byte |
| 2 | **Bölüm budama oranı** (pruned %) | Snowflake `partitions_scanned / partitions_total` | Gömülen filtre sütunu clustering/partition anahtarı olabiliyorsa denormalizasyon lehine **en güçlü** argüman |
| 3 | **p50 / p95 süre** | Sorgu geçmişi | Kullanıcı deneyimi; p95 eşzamanlılıkta bozulur |
| 4 | **Kredi / maliyet per sorgu** | Fatura, warehouse credit | En üst düzey karar metriği |
| 5 | **Join build tarafı boyutu** | Boyut satır sayısı × satır genişliği; spill oranı | Boyut belleğe sığıyorsa (broadcast/hash) join neredeyse bedava → **normalize kal** |
| 6 | **Boyut/fact kardinalite oranı** | `COUNT(dim)/COUNT(fact)` | Küçük boyut = ucuz join; büyük boyut = gömme pahalı |
| 7 | **Depolama artışı** | `byte/satır` farkı | Satır-deposunda ciddi; kolonsalda sözlük kodlamayla büyük ölçüde erir |
| 8 | **Düzeltme/tazeleme maliyeti** | Etkilenen satır sayısı × birim maliyet | Boyut düzeltmesi OBT'de fact'i yeniden yazdırır |
| 9 | **Yeniden üretim süresi** | ETL koşum süresi | Tazelik SLA'sını tutuyor mu |
| 10 | **Fan-out riski** | `OBT satır sayısı == fact satır sayısı` mı | Çoka-çok bir boyut gömülürse satır çoğalır → çift sayım |
| 11 | **Sorgu yazım hatası oranı** | Rework/hatalı rapor sayısı | OBT bunu düşürür; ölçülebilir ama yumuşak metrik |

### 12.5 Ölçülmüş örnek karar *(betik: `09-olap-sema-karar.py`)*

Aynı veri, iki şema: yıldız (fact + 2 boyut) ve OBT.
`fact 500.000 · d_urun 2.000 (%0.40) · d_musteri 50.000 (%10.0)`

**Ağırlıklı iş yükü:**

| Sorgu | Ağırlık | Yıldız | OBT | Kazanç |
|---|---|---|---|---|
| Q1 kategori × şehir ciro (2 boyut join) | 0.5 | 576.0 ms | 225.4 ms | 2.56× |
| Q2 marka ciro (1 boyut join) | 0.3 | 254.9 ms | 137.2 ms | 1.86× |
| Q3 segment + tarih filtreli sayım | 0.2 | 48.5 ms | 20.0 ms | 2.43× |
| **Ağırlıklı toplam** | | **374.2 ms** | **157.9 ms** | **2.37×** |

**Diğer eksenler:**

| | Yıldız | OBT |
|---|---|---|
| Depolama | 13.3 MB | 41.2 MB (**+%208**, +55.7 byte/satır) |
| Bir boyut düzeltmesi | **1** satır, 0.37 ms | **228** satır, 15.20 ms (**41×**) |

**Kararın okunuşu — ve asıl ders:**

- Okuma 2.37× OBT lehine; depolama ve düzeltme ciddi biçimde yıldız lehine.
- Ama **düzeltme maliyeti yalnız tablo KAYNAK ise gerçek maliyettir.** OBT gold katmanında türetilmiş bir tabloysa düzeltme "228 satır güncellemek" değil, "tabloyu yeniden üretmek"tir — ve o maliyet zaten ETL bütçesinde. O durumda karar **OBT lehine**.
- OBT'yi analistlerin doğrudan yazdığı **kaynak** tablo yaparsan, 41× ve %208 gerçek maliyet olur; karar **yıldız lehine** döner.

> Yani soru "ne kadar normalize edeyim" değil, **"bu tablonun kaynağı kim ve düzeltme kime fatura ediliyor"**dur.

**Bu ölçümün sınırları (dürüstlük şartı):** SQLite = satır-deposu, tek makine, eşzamanlılık yok, bölüm budama yok, sıkıştırma yok. Kolonsal motorda beklenen değişim: (a) depolama farkı erir — tekrarlı düşük-kardinaliteli metin sütunları sözlük/RLE ile sıkışır; (b) okuma farkı **büyüyebilir** — kolon budama sayesinde OBT'de yalnız gereken sütunlar okunur; (c) bölüm budama yeni bir eksen olarak devreye girer. Bu üç öngörünün ikisi 12.5b'de ölçüldü ve **biri yanlış çıktı**.

### 12.5b Aynı karar, kolonsal motorda *(betik: `10-olap-duckdb-olcum.py`, DuckDB 1.4.5 + Parquet/ZSTD)*

Aynı veri, aynı iş yükü, aynı ağırlıklar — tek fark motor ve depolama biçimi:

| Eksen | SQLite (satır-deposu) | DuckDB + Parquet (kolonsal) |
|---|---|---|
| Ağırlıklı okuma — yıldız | 374.2 ms | **3.5 ms** |
| Ağırlıklı okuma — OBT | 157.9 ms | **2.0 ms** |
| OBT'nin okuma avantajı | 2.37× | **1.77× (daraldı)** |
| Depolama farkı | +%208 · +55.7 byte/satır | +%98 · **+7.1 byte/satır** |
| Düzeltme maliyeti | 1 satır ↔ 228 satır (41×) | 0.01 MB ↔ 7.22 MB yeniden yazım (42×) |
| Ağırlıklı taranan byte | ölçülemez | yıldız 1.57 MB ↔ OBT 1.02 MB (1.54×) |

**Üç sonuç, üçü de karar değiştiriyor:**

**(1) Motor seçimi, şema seçiminden bir büyüklük mertebesi daha etkili.** Aynı iş yükü 374 ms → 3.5 ms, yani ~%100'lük değil ~100 KAT'lık fark. Şema tartışmasının kazandırdığı 2.37×, motor değişiminin kazandırdığı ~107× yanında küçük kalıyor. **Önce doğru motor, sonra şema.**

**(2) Denormalizasyonun okuma avantajı kolonsalda DARALIYOR** (2.37× → 1.77×). Sebebi: vektörize hash join'de küçük boyut tablosu neredeyse bedava, ve kolon budama zaten yıldız şemada da çalışıyor. Yani "OLAP = denormalize et" refleksi, kolonsal motorda satır-deposundakinden **daha zayıf** bir argüman.

**(3) Asıl karar metriği tablo değil, KARDİNALİTE.** Gömülen her boyut sütununun fact satırı başına maliyeti ayrı ayrı ölçüldü:

| Gömülen sütun | Farklı değer | Sıkıştırma | byte/satır |
|---|---|---|---|
| `musteri_ad` | 50.000 | 5.1× | **3.10** |
| `fiyat` | ~2.000 (float) | 1.4× | 1.12 |
| `urun_ad` | 2.000 | 1.6× | 1.07 |
| `sehir` | 81 | 1.0× | 0.88 |
| `marka` | 150 | 2.2× | 0.47 |
| `segment` | 5 | 1.1× | 0.34 |
| `kategori` | 12 | 1.6× | 0.31 |

Düşük kardinaliteli sütunları gömmek **satır başına 0.3 byte** — pratikte bedava. Yüksek kardinaliteli `musteri_ad`'ı gömmek 3.1 byte, yani 10 katı; toplam farkın tek başına %43'ü o sütundan geliyor.

> **Kolonsal ortamda karar birimi tablo değil sütundur:** "boyutu gömeyim mi" diye sorulmaz, "bu sütunu gömeyim mi" diye sorulur ve cevap sütunun kardinalitesinden okunur. Düşük kardinaliteli filtre/kırılım sütunlarını göm, yüksek kardinaliteli kimlik/ad sütunlarını boyutta bırak.

**Bu ölçümün de sınırları:** bölümleme (`PARTITION_BY`) yok — bölüm budama ölçülmedi; dosyalar `tarih, urun_kod` sıralı yazıldı, dolayısıyla Q3'ün tarih filtresi satır-grubu min/max budamasından kısmen faydalanmış olabilir (ayrıştırılmadı); eşzamanlılık ve bulut maliyet (kredi) eksenleri yok; tek koşum, soğuk önbellek ölçülmedi.

### 12.6 Başlangıç hipotezleri (ölçümle doğrulanacak, kural değil)

- Boyut belleğe sığıyorsa (kabaca < 10⁶ satır) → **yıldızda kal**; join maliyeti ihmal edilebilir.
- Bir boyut özniteliği sorguların büyük kısmında **filtre** olarak geçiyorsa ve bölümleme/kümeleme anahtarı olabiliyorsa → fact'e gömmeyi **ölç** (metrik 2 buna bakar).
- Yüksek kardinaliteli / serbest metin sütunu → **gömme**; sıkışmaz, taranan byte patlar.
- Boyut devasa (10⁸+, ör. kullanıcı) → kar tanesi ya da yalnız sık kullanılan birkaç özniteliğin gömülmesi.
- Sorgu seti dar ve kararlıysa → o set için **OBT/özet tablo** üret, genel şemayı bozma.
- Tarihsel doğruluk gerekiyorsa (SCD2) → gömülen öznitelik o andaki değeri **dondurur**. Satış anındaki fiyat için bu istenen davranıştır; "müşterinin güncel segmenti" için değildir.

### 12.7 Karar kaydı şablonu

```
Karar: <şema seçimi>
Tanecik: bir satır = ...
Kısıtlar: SCD tipi ... · tazelik SLA ... · fan-out kontrolü PASS/FAIL
Ölçüm (tarih, ortam): ağırlıklı okuma ... · depolama ... · tazeleme ...
Gerekçe: ...
Yeniden açma koşulu: <metrik> <eşik> aşarsa
```

---

## 13. Uçtan uca reçete

1. **Hücrelere bak.** Liste/CSV/JSON, `x1,x2,x3` sütunları → böl. **(1NF)**
2. **Anahtarı yaz.**
3. **Anahtar tek sütunsa** 5. adıma geç (2NF otomatik).
4. **Bileşikse**, her parçası için: *bu parça tek başına neyi belirliyor?* → taşı. **(2NF)**
5. **Kalan sütunlar arasında:** *X, Y'yi belirliyor mu?* Sol tarafı anahtar olmayan her bağımlılığı çıkar. **(3NF)**
6. **Her okun sol tarafı anahtar mı?** Değilse ve tekrar acıtıyorsa böl, kaybettiğin kuralı yaz. **(BCNF)**
7. **Bağımsız çoklu alanlar** ayrı tabloya. **(4NF)**
8. **Doğrula:** ortak sütun bir tarafta anahtar mı · `JOIN` orijinal satır sayısını veriyor mu.
9. **Sonra ölç.** Yavaşsa: önce indeks, sonra view, sonra özet tablo. Elle çoğaltma en son.
10. **OLAP ise** 12. bölümün prosedürü: tanecik → iş yükü → aday şemalar → ölçüm → ağırlıklı karar → yeniden açma koşulu.

---

## 14. Tüm formlar ve sözlük

| Form | Yasakladığı | Testi |
|---|---|---|
| 1NF | Hücrede birden fazla değer, tekrarlayan sütun grubu | Sorguda string parçalıyor muyum? |
| 2NF | Anahtarın *parçasına* bağlı sütun | Anahtar bileşikse: parça tek başına neyi belirliyor? |
| 3NF | Anahtar olmayan *başka bir sütuna* bağlı sütun | Sütundan sütuna ok var mı? |
| BCNF | Okun sol tarafının anahtar olmaması | Her belirleyici süper anahtar mı? |
| 4NF | Bağımsız iki çoklu gerçek | İlgisiz sütun yüzünden çok satır yazıyor muyum? |

| Terim | Tek satır |
|---|---|
| Fonksiyonel bağımlılık (X → Y) | X'i aynı olan iki satırın Y'si de aynı olmak zorunda |
| Süper anahtar | Satırın tüm sütunlarını belirleyen sütun kümesi |
| Aday anahtar | Fazlalık taşımayan süper anahtar |
| Birincil anahtar | Aday anahtarlardan seçilen |
| Bileşik anahtar | Birden fazla sütunlu anahtar |
| Asal sütun | Bir aday anahtarın parçası olan sütun |
| Kısmi bağımlılık | Bileşik anahtarın *parçasına* bağlılık |
| Geçişli bağımlılık | Anahtar → B → C, B anahtar değil |
| Kayıpsız birleşim | Bölünen tabloların JOIN'i orijinali *aynen* vermesi |
| Bağımlılık koruma | Her kuralın tek bir tabloda denetlenebilir kalması |
| Tanecik (grain) | "Bir satır = ..." cümlesi |
| Fact / dimension | Ölçülen olay / olayın niteliği |

---

## 15. Sık yapılan hatalar

1. **Yapay `id` koyup doğal anahtara `UNIQUE` koymamak** — tablo normal görünür, veri iki kez girer.
2. **Refleksle her şeyi bölmek** — tekrarı olmayan alanı ayırmak yalnız JOIN ekler.
3. **Zamana bağlı değeri referans tablosuna taşımak** — geçmiş kayıtlar geriye dönük değişir.
4. **Ambardaki tekrarı hata sanmak** — türetilmiş tekrar tehlikesizdir; soru "kaynak tek mi?".
5. **Ölçmeden denormalize etmek** — nokta sorgusunda JOIN maliyeti sıfıra yakın; "JOIN yavaş" çoğu zaman indeks eksikliğinin yanlış teşhisidir.
6. **OLAP'ta tanecik yazmadan şema tartışmak** — çift sayım oradan doğar, normalizasyon seviyesinden değil.

---

## Ek: betikler

`ogrenme/dersler/2026-08-21-normalizasyon-kod/`

| Dosya | Ne gösterir |
|---|---|
| `01-anomaliler.py` | Ekleme/silme/güncelleme anomalileri + 3NF ayrıştırması |
| `02-bagimlilik-anahtar.py` | Fonksiyonel bağımlılık ve anahtar testleri |
| `03-1nf.py` | Çok-değerli hücrenin ürettiği yanlış sonuç (`LIKE` tuzağı) |
| `04-2nf.py` | Kısmi bağımlılık testi + ayrıştırma |
| `05-3nf-tarayici.py` | Tüm sütun çiftlerini tarayan bağımlılık tarayıcısı |
| `06-bcnf-kayipsiz.py` | BCNF ihlali, bağımlılık koruma kaybı, uydurma satır üreten bölme |
| `07-4nf.py` | m×n şişmesi ve m+n çözümü |
| `08-maliyet-olcum.py` | 3NF ↔ denormalize okuma/yazma maliyeti |
| `09-olap-sema-karar.py` | **Yıldız ↔ OBT karar ölçümü** (ağırlıklı iş yükü + depolama + tazeleme) — kendi verinde yeniden kullanılabilir |
| `10-olap-duckdb-olcum.py` | **Aynı karar kolonsal motorda** (DuckDB+Parquet): sıkıştırılmış depolama · taranan byte (kolon budama) · sütun başına kardinalite maliyeti · dosya yeniden yazma. `<venv>/bin/python` ister |

Koşum: `python3 ogrenme/dersler/2026-08-21-normalizasyon-kod/09-olap-sema-karar.py`
