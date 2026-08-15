# Hat-6 Nihai Karar Önerisi — model×effort · jarvis→DB · kendini-geliştiren düğüm (Salih'e)

*Carvis/Fable, 2026-08-16 seans-5 (G-6 sentez; Salih emri seans-2 "Hat-6 genişledi" + plan-A onayı). Rejim: sentez-yalnız — yeni scout AÇILMADI (ekonomi −%30; kanıt tabanı: rapor-1..5 + rapor-8/9 + V-1 koşum verileri + bu vardiyanın ölçülmüş koşumları). Kanıt boşluğu olan hücreler [BOŞLUK] damgalı. Karar katmanı: üçü de Katman-1 (kural/kanon) — hüküm Salih'te; öneriler m.6 (kibarca tavsiye + gerekçe).*

## K1 — jarvis→DB: V-1 tablosunun rolü
**Durum:** V-1 v1 canlı (37,7k kayıt · idempotent · 3 galaxy görünümü). Şu an YALNIZ-OKUR analitik katman.
**Seçenekler (m.37):**
- **(a) Yalnız-okur kalsın** — maliyet 0; kazanç: denetim/ölçüm sorguları (bugünkü hâl).
- **(b) ÖNERİLEN: yazım-anı ölçüm-kapısı** — ingest/damıtma hattına "her yazımda kolon istatistiği + NDV + token/birim" üretimi bağlanır (world-model §5.4 yazıcı-sözleşmesi; S9-CD-YT3 kanıtlı). Maliyet: damitma/ingest adımına ~1 script çağrısı (+~5 sn/koşum, token ≈0 — script işi); kazanç: x-ölçümü ve boyut-tetiği FLAG'leri elle değil tablodan; §6 ölçüm işlerinin (NDV · tekrar-oranı · dil-çarpanı) altyapısı hazır olur.
- **(c) Tam medallion (bronz/silver/gold katmanları DB'de)** — [BOŞLUK] gold-katman kazancı satıcı-blog düzeyi (S9-CD-kör), ölçülmüş gerekçe yok; ertelenmeli.
**Gerekçe (b):** parquet-felsefesi transferinin tek "bugün bedava" parçası istatistik-katmanı sözleşmesidir; lossy adımlar (özüt) zaten MDL+QA-eval kapısına bağlı. Riski düşük, geri-alması ucuz (script satırı).

## K2 — model×effort boyutları: koşum-profili standardı
**Durum:** eko-rejim bu vardiyada fiilen model×effort kullandı (işçi medium / hakem high / V26 low) — sonuç: S-8 devamı 743k, S-9 769k, Hat-5 449k token; kalite: V26 denetimleri TUTUYOR, hakem hükümleri dolu. Tam-şerit emsali (S-6: 16 işçi hepsi yüksek-efor) ~1M+ idi. Kaba gözlem: **eko-profil ~%40-55 token, hüküm-kalitesi gözle görülür düşüş YOK** [BOŞLUK: sistematik A/B kıyası yapılmadı — tek-vardiya gözlemi].
**Seçenekler:**
- **(a) ÖNERİLEN: şablon alanı kalıcılaşsın** — `gorev-fonksiyonu.md` ÇIKTI-SÖZLEŞMESİ'ne `model_effort_profili: {rol → model×effort}` + `rejim: kalite-öncelikli | maliyet-öncelikli` alanı; m.40b koşumlarında rejim etiketi zorunlu (zaten manifest kuralı, şablona iner). Her ampirik hücre (model, sürüm, tarih) damgası rapor-5 C-YT8 gereği ZATEN zorunlu — profil alanı bunun koşum-tarafı simetriği.
- **(b) Serbest kalsın (koşum-başına elle)** — esneklik; ama bu vardiyada 3 koşum profili elle yeniden türetildi (Y1-tipi tekrar).
**Gerekçe (a):** kural zaten fiilen var (ekonomi-rejim kaydı afb41d4); şablona inmesi tekrarı keser. Maliyet: şablon +2 satır.

## K3 — kendini-geliştiren düğüm akışı: ilk pilot
**Durum:** kural çatısı KURULDU (world-model §3: öz-model düğümü yalnız koşum-kaydı türevi · içe-bakış tek başına düğüm kuramaz · tazeleme damgası + basınç sayacı · durum-denkliği testi yalnız sonlu alt-alanlarda). Akış henüz koşmadı.
**Seçenekler:**
- **(a) ÖNERİLEN: dar pilot — skill-koşum düğümleri** — kaynak: skill-fikir-kutusu ölçüm tablosu + kapı sicilleri (zaten kayıtlı, yapısal); düğüm = skill × (koşum-sayısı, DRFR, son-güncelleme); doğrulayıcı = kayıt satırları (içe-bakış yok). Maliyet: ~1 koşum (script + görünüm); 10-koşum kalibrasyon zaten bu veriyi istiyor.
- **(b) Geniş pilot (pano/kart yaşam-döngüsü durum-denkliği)** — daha zengin ama önce sonlu durum-soyutlaması TASARIM işi ister (S8-B-YT3 şartı); ikinci adım olarak dursun.
- **(c) Süreç-keşfi (process mining) katmanı** — [BOŞLUK] fayda ölçülmemiş (S8-B-YT8); m.29 deneysel damgayla ancak (a)+(b) sonrası.
**Gerekçe (a):** en ucuz, verisi hazır, world-model §3 frenlerinin ilk sahada testi.

## Bağlı açık işler (karar değil, hatırlatma)
- W-1 §6 ölçüm sırası: NDV → tekrar-oranı → dil-çarpanı → sort-key → durum-denkliği (K1-b kabulüyse ilk üçü otomatikleşir).
- F1e hazine-sabiti (7962 > 7200 char): tetik-yüzeyi aşındırmadan kapanmıyor — 7200 m.29 kalibrasyon kalemi (öneri: /context ölçümüyle yeniden türet).
- Sözlük Skill Hazinesi: DONDU — yol-planla girişi Salih talimatı bekliyor.
