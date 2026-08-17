# K-019 Taslak — Boyut-izleme + sabit-bütçe kuralı (KILAVUZ adayı)

*Statü: **İMZALANDI (Salih, 07-22)** — iki şerhle: (1) bütçe temeli soruldu → cevap aşağıda "Bütçelerin temeli" bölümünde; rakamlar deneysel-damgalı (m.29/m.39), Salih tespiti kayıtta: teknoloji (context penceresi/fiyat) ve bütçe değiştikçe TABLO REVİZE EDİLİR — revizyon tetiği kurala gömüldü. (2) Kural KILAVUZ'a işlendi 07-22.* *Hazırlayan: Carvis, 2026-07-22 günaydın vardiyası. Kaynak: K-017/E3 (CC 200-satır bağlam-uyum eşiği) + P1 devri 07-17 (prefix-ölçeklenme sigortası: önek = sabit-boyutlu bütçe, büyüme soğuk katmana).*

## Önerilen kural (KILAVUZ'a eklenecek blok)

**Sıcak-dosya bütçesi:** Her oturum açılışında okunan dosyalar sabit boyut-bütçeli yaşar. Bütçe aşımı hata değil TETİKTİR: aşan dosya ilk boş seansta damıtılır (silme yok — tam metin arşiv dosyasına iner, sıcakta özüt + pointer kalır, m.8/m.34).

| Dosya | Bütçe | 07-22 fiili | Durum |
|---|---|---|---|
| core/durum-kapsulu.md | 8 KB | 5,8 KB | ✓ |
| core/pano.md | 12 KB | 9,2 KB | ✓ |
| fikir-kutusu.md | 20 KB | 37,3 KB | **AŞIM ×1,9 → damıtma taslağı hazır** |
| kuyruk/senaryo-defteri.md | 48 KB | 41,2 KB | ✓ (izlemede — en hızlı büyüyen) |
| CLAUDE.md | 8 KB | 5,8 KB | ✓ |
| KILAVUZ.md | 16 KB | 13,7 KB | ✓ (izlemede) |

**İşleyiş:** (1) Seans kapanışında kapanan Carvis bu tabloya tek bakış atar (`ls -l` yeter); aşan dosya varsa teslim raporuna "boyut-tetiği: <dosya>" satırı düşer. (2) Damıtma her zaman ayrı seansta, Salih imzalı planla yapılır (bkz. kutu-damıtma taslağı — ilk emsal). (3) Bütçeler deneysel damgalıdır (m.29): iki damıtma turundan sonra kalibre edilir. (4) Prefix-ölçeklenme ilkesi geneli bağlar: bir bilgi ne kadar kararlı olursa olsun boyutu yüzünden soğuk katmanda kalabilir — sıcaklık kararlılıkla değil, oturum-başına-gereklilikle ölçülür.

## Bütçelerin temeli (Salih sorusu 07-22'ye cevap — dürüst kayıt)
Rakamlar ÖLÇÜMDEN türetilmedi; iki sezgisel çıpanın bileşimi (m.39 deneysel damga): (1) sağlıklı dosyalar için mevcut boyut ×~1,4 pay (büyüme alanı bırakır ama "fark edilmeden ikiye katlanma"yı yakalar), (2) kutu için rol-sözleşmesi hedefi (tek-satır formatına dönerse ~10-12KB eder → 20KB bütçe iki kat pay bırakır). Üçüncü çıpa P5 dersiyle geldi: sıcak dosyalar oturum-önekinde = her KB her oturumda tekrar ödenen kira; MEMORY.md sert-200 emsali "bütçe aşımı sessiz veri kaybına dönüşmeden yakalanmalı" diyor. **Revizyon tetiği (Salih şerhi):** context-penceresi/fiyat ekonomisi ya da Jarvis bütçesi anlamlı değişirse tablo yeniden türetilir; ayrıca her iki damıtma turunda bir kalibrasyon zaten kuralda. **Ek satır (07-22 denetim bulgusu):** kapsül için KB bütçesinin yanına SATIR kapısı: ≤40 satır — SessionStart hook `sed 1,40p` ile basıyor, aşan kuyruk CC yüzeyinde sessizce düşer.

## Gerekçe (özet)
Kapsül/pano/kutu her oturumun önekinde: her KB, her oturumda tekrar ödenen kira. Kutu 37 KB'a çıktı — tek dosya, oturum açılışının en pahalı kalemi. Sabit bütçe + tetik, "fark edilmeden şişme" sınıfını (V4 bayat-kapsül ailesinin boyut hali) kapatır.

## Karar istenen
- [ ] Bütçe tablosu bu değerlerle kabul / değerleri Salih revize eder
- [ ] Kural KILAVUZ'a "Boyut-izleme" bölümü olarak girer
