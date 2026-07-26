# Staj Hattı — Otonet/Otoplus (başlangıç: 11 Ağustos 2026)

*Kuruluş: 2026-07-25 vardiyası, Salih kararı ("staj hattını kur + P1 aç"). Kaynak: `raporlar/2026-07-24-serit5-staj-hazirligi-otonet.md` (tam gerekçe + kanıt etiketleri orada — pointer m.20). Pano kartı: K-022.*

## Oturum açılışı
Hat beyanı: **"günaydın, staj"** (paralel vardiya protokolü). Carvis bu beyanla K-022 + bu dosya + günün partisyonuna oturur; prototip şeridi gündeme girmez. Çevrim: tahmin yaz (Salih, çalıştırmadan) → doğrula (Carvis koşturur ya da Salih kendi koşturur) → cevap anahtarı en son → yanlışlar sınıflanır + tekrar kuyruğuna → kapanışta DONE durumu K-022'ye işlenir. Sınav setlerini (P1 15-sorgu vb.) Carvis üretir — pratik dosyalarındaki sorular sınavda tekrar KULLANILMAZ.

## İşin tanımı
Ekip agentic coding yapıyor — kod yazılmıyor, ajanlara yazdırılıyor. **Senin rolün doğrulama katmanı:** sessiz mantık hatası ve boş test tiyatrosunu yalnız insan okuması yakalıyor. Hedef: advanced-beginner okuma yeterliliği + rol netliği + öz-yeterlik + hazır soru repertuarı. Hedef DEĞİL: görev ustalığı (18 günde alınamaz).

## Okuma birimi = 5 adımlı çevrim (pazarlıksız)
1. **Tahmin yaz** — çalıştırmadan, cevaba bakmadan, yazılı
2. **Doğrula** — çalıştır / cevabı aç
3. **Farkı 1 cümleyle açıkla**
4. **Yanlışı kuyruğa at** — 2-3 gün sonra tekrar
5. **Üretim vergisi** — her 5 okunan artefakta 1 küçük değişiklik yaz

Adım 1 ve 3 olmadan plan "düşük fayda" kutusuna düşer.

## Takvim (kronolojik partisyonlar)
| P | Tarih | Konu | DONE |
|---|---|---|---|
| P0 | **GECİKMİŞ (plan 24 Tem) → bugün, ~1 sa** | Kalibrasyon | 10 SQL + 10 Python soğuk, yazılı tahmin → baseline % kayıtlı (`P0-kalibrasyon/`) |
| P1 | 25-28 Tem | SQL okuma | 15 sorgu, referanssız, ≤3 dk → **13/15 VE sessiz-hata 6/6** |
| P2 | 29 Tem-1 Ağu | Python okuma | 12 hücre → ≥10/12 · P1 bakım ≥4/5 |
| P3 | 2-3 Ağu | Kurumsal yöntem + AWS haritası | 30 terim kapalı kitap ≥24/30 · **ilk hafta 5 sorusu yazılı** (1.: "AWS'in inşası gibi" ne demek) |
| P4 | 4-6 Ağu | Operatör entegrasyonu | 3 tur: yazılı görev tarifi → soğuk oku → kabul/ret/düzelt gerekçeli → karşılaştır; 3/3 doğru karar VE ≥1 sessiz hata yakalanmış (yoksa enjekte et) |
| P5 | 7-8 Ağu | Tampon | yeni içerik yok; P1-P4 DONE'ları kapalı |
| P6 | 9-10 Ağu | Soğuk prova + iniş | 10 SQL + 8 Python + 15 terim tek oturum ≥%80; cramming yasak |
| — | **11 Ağu** | BAŞLANGIÇ | — |

## Pazarlıksız kurallar
Her artefakt 5-adımlı çevrimle · hiçbir konuya 3 günden fazla ara yok (10 dk soğuk dokunuş) · yeniden okuma / pasif izleme yok · sınavlar soğuk-görülmemiş-referanssız-yazılı · **eşik düşürülmez, kapsam küçültülür** · kötü gün minimum 15 dk, sıfır gün yok · günlük tavan 2,5 sa (dayanağı [X]) · kayma: 1 gün→tampon, 2 gün→kapsam, 3+ gün→plan P1+P3'e iner · her partisyon başında eğer-o-zaman planı · son 2 gün iniş.

## AWS/sertifika notu
DEA-C01 Exam Guide ücretsiz müfredat olarak P3'te okunur (~2 gün değil, harita düzeyinde). Sertifika sınavı Ekim-Kasım (K-004 penceresi). "raw/curated/serving" AWS dili değil — şirketin adlandırmasını sor.

## Açık sorular (rapor §11'den; şirkete/Salih'e)
"AWS'in inşası gibi" gerçek anlamı · hangi yığın/adlandırma · günlük gerçekçi pencere · şirket bilgisinin bu repoya yazılma sınırı (m.14 üçüncü-taraf).
