# K-019 Taslak — Boyut-izleme + sabit-bütçe kuralı (KILAVUZ adayı)

*Statü: İMZA BEKLİYOR (Katman-1 — kural yazımı, m.31). Hazırlayan: Carvis, 2026-07-22 günaydın vardiyası. Kaynak: K-017/E3 (CC 200-satır bağlam-uyum eşiği) + P1 devri 07-17 (prefix-ölçeklenme sigortası: önek = sabit-boyutlu bütçe, büyüme soğuk katmana).*

## Önerilen kural (KILAVUZ'a eklenecek blok)

**Sıcak-dosya bütçesi:** Her oturum açılışında okunan dosyalar sabit boyut-bütçeli yaşar. Bütçe aşımı hata değil TETİKTİR: aşan dosya ilk boş vardiyada damıtılır (silme yok — tam metin arşiv dosyasına iner, sıcakta özüt + pointer kalır, m.8/m.34).

| Dosya | Bütçe | 07-22 fiili | Durum |
|---|---|---|---|
| core/durum-kapsulu.md | 8 KB | 5,8 KB | ✓ |
| core/pano.md | 12 KB | 9,2 KB | ✓ |
| fikir-kutusu.md | 20 KB | 37,3 KB | **AŞIM ×1,9 → damıtma taslağı hazır** |
| kuyruk/senaryo-defteri.md | 48 KB | 41,2 KB | ✓ (izlemede — en hızlı büyüyen) |
| CLAUDE.md | 8 KB | 5,8 KB | ✓ |
| KILAVUZ.md | 16 KB | 13,7 KB | ✓ (izlemede) |

**İşleyiş:** (1) Vardiya kapanışında kapanan Carvis bu tabloya tek bakış atar (`ls -l` yeter); aşan dosya varsa teslim raporuna "boyut-tetiği: <dosya>" satırı düşer. (2) Damıtma her zaman ayrı vardiyada, Salih imzalı planla yapılır (bkz. kutu-damıtma taslağı — ilk emsal). (3) Bütçeler deneysel damgalıdır (m.29): iki damıtma turundan sonra kalibre edilir. (4) Prefix-ölçeklenme ilkesi geneli bağlar: bir bilgi ne kadar kararlı olursa olsun boyutu yüzünden soğuk katmanda kalabilir — sıcaklık kararlılıkla değil, oturum-başına-gereklilikle ölçülür.

## Gerekçe (özet)
Kapsül/pano/kutu her oturumun önekinde: her KB, her oturumda tekrar ödenen kira. Kutu 37 KB'a çıktı — tek dosya, oturum açılışının en pahalı kalemi. Sabit bütçe + tetik, "fark edilmeden şişme" sınıfını (V4 bayat-kapsül ailesinin boyut hali) kapatır.

## Karar istenen
- [ ] Bütçe tablosu bu değerlerle kabul / değerleri Salih revize eder
- [ ] Kural KILAVUZ'a "Boyut-izleme" bölümü olarak girer
