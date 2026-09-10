# World-Model Tasarımı v1 — Jarvis = Galaxy Veri Şeması (deneysel m.29)

*G-W1 sentezi (Jarvis/Fable, 2026-08-16; Salih emri 08-15 seans-3: "Jarvis'i galaxy data schema şeklinde world-model tasarımıyla inşa edeceğiz; birim veri = x birim bağlam"). Kanıt tabanı: `cc/rapor/2026-08/rapor-2026-08-15-8.md` (S-8: galaxy/WM/x/OLAP — 95 tez iddiası, hakem 20/33/6/1) + `cc/rapor/2026-08/rapor-2026-08-15-9.md` (S-9: parquet→özütleme — hakem 6/16/2/0). Her ilke rapor yapı-taşı (YT) damgası taşır; damgasız ilke YOK. Emsalsizlik şerhi: "kişisel markdown kanonu = boyutsal şema" aktarımının literatürde emsali ARANDI-BULUNAMADI (S-8 A/D kör) — bu tasarım öncü deneme, tüm sabitler deneysel m.29.*

## 1. Çekirdek kararlar (mimari)
1. **Gerçek kaynak = olay kütüğü, model = türetilmiş görünüm.** Git log + koşum kayıtları Jarvis'in event-store'udur; world-model bunların ÜZERİNE kurulan türetilmiş katmandır, kaynak-doğruluğun yerini almaz (S8-A-YT5; ingest v2 "kapsül=SNAPSHOT" ilkesiyle UYUMLU). Replay/temporal-query yetenek olarak korunur; işletim varsayılanı güncel-durum.
2. **Taban ilişkisel kalır (SQLite/V-1); graf motoru ayrıştırılmaz.** Desen-eşleme sınıfı sorgular ilişkisel çekirdekte çözülür; 42,9k kenar, ölçülmüş OOM/performans eşiklerinin çok altında (S8-D-YT6). Kleene*/yol-bulma gerekirse ayrı katman olarak eklenir — bugün gerek yok.
3. **Ham blok gerçek kaynak; matris/küp/gömme türetilmiş ve KAYIPLI görünümlerdir.** (birim × özellik) design-matrix ancak açık vektörleştirme adımıyla türetilir (S8-D-YT8). OLAP küp cebiri serbest-metin alanına ham devrolmaz — yalnız sayısal metriklere, dondurulmuş boyut-altkümesiyle (S8-A-YT8 GİRMEZ).
4. **Varsayılan şema parçalanmaz.** Nitelik-başına-tablo (anchor/6NF) yalnız ÖLÇÜLMÜŞ dar-alan sorgu profili için açılır (+14×↔−13× koşullu; S8-A-YT4).

## 2. Grain + bus matrix (galaxy'nin iskeleti)
- **"Markdown blok" tek başına grain DEĞİLDİR** — v0'daki beyan `kayit` tablosunun grain'idir. Kural: önce İŞ SÜRECİ seç, sonra o sürecin grain'ini tek cümleyle bildir, boyut/olgu ondan sonra (S8-A-YT1, D-YT2). İnşa bir seferde bir süreç satırı (S8-A-YT3).
- **Bus matrix v1 (yazılı; satır = süreç, sütun = boyut):**

| Süreç (grain bildirimi) | zaman/seans | dosya | anahtar | skill | katman | model |
|---|---|---|---|---|---|---|
| ingest (1 satır = 1 zarf kaydı) | ✓ | ✓ | ✓ | | ✓ | |
| damıtma (1 satır = 1 kayıt-triyajı) | ✓ | ✓ | ✓ | ✓ | ✓ | |
| skill-koşumu (1 satır = 1 çağrı sözleşmesi) | ✓ | | ✓ | ✓ | | ✓ |
| araştırma-koşumu (1 satır = 1 işçi-dönüşü) | ✓ | ✓ | | | | ✓ |
| karar (1 satır = 1 hüküm) | ✓ | ✓ | ✓ | | | |
| karar-borcu (1 satır = 1 AÇIK karar kalemi — hükmün ön-durumu; kapanınca `karar` satırına akar; Salih imzası 08-17 masa KB-07) | ✓ | ✓ | ✓ (küme/katman) | | ✓ | |
| commit (1 satır = 1 commit; niyet-etiketi doğrulanmadan boyut sayılmaz — S8-A-YT5b) | ✓ | ✓ | | | | |

- **Conformed boyut = bağlam-anahtar-kaydı.** Uyum koşulu: aynı ad + aynı domain; tam kopya gerekmez, katman-başına daraltılmış (shrunken) görünüm meşru (S8-A-YT2, D-YT1). Kararlılık kendiliğinden gelmez — anahtar-kaydının emeklilik/damga disiplini şart (S8-A-YT7). Görünüm: `v_boyut_anahtar`.
- **`referans` tablosu = factless-fact/M2M köprü.** Galaxy statüsüne geçiş koşulu ÖLÇÜLEBİLİR: referans zaman grain'i kazanırsa (hangi commit/seansta doğdu) ikinci olgu tablosu olur (S8-A-YT2, D-YT3). İlk ölçüm (v1, 08-16): zamanlı %7,6 (3.587/47.388) → bugün KÖPRÜ, hedef metrik izlenir. Görünüm: `v_olgu_referans` (zaman_grain kolonu).
- **Niteleyici korunur:** referans kayıtları katman/tarih/tür taşır ⇒ çıplak-üçlü/3B-tensör düzleştirmesi kayıplıdır; n-ary/property-graph biçimi kalır (S8-D-YT4). Olay kaydı çok-nesnelidir — vaka-kimliği sütunu EKLENMEZ, nesne-referans kümesi korunur (OCEL; S8-B-YT4).

## 3. Learned world-model katmanı (koşum-kaydı türevi)
- **Birim = GEÇİŞ, yalnız durum değil:** önceki-durum→eylem→sonraki-durum; kenar birinci-sınıf varlık (S8-B-YT1).
- **Kapsama > temizlik:** FAIL kayıtları, iptal dalları, retry zincirleri şemanın ZORUNLU satırı — yalnız-başarı korpusundan çıkan model bozulma anında çöker (S8-B-YT2).
- **Öz-model düğümü yalnız koşum-kaydından türer;** modelin içe-bakış beyanı tek başına düğüm kuramaz (~%20 güvenilirlik; S8-B-YT6). Beyan edilen yetenek-sınırı ↔ fiili davranış AYRI satırlar + karşılaştırma görünümü (S8-B-YT7).
- **Donmuş model sömürülür → tazeleme kuralı:** düğümde son-güncelleme damgası + "kaç karar yaslandı" sayacı (optimizasyon-basıncı); graf koşum kayıtlarıyla güncellenmeden üzerine optimize edilmez (S8-B-YT5).
- **Kalite ölçüsü = durum-denkliği testi, çıktı-doğruluğu DEĞİL;** yalnız sonlu durum-soyutlamalı alt-alanlarda (pano-durumu, kapı-ağacı, kart yaşam-döngüsü) tanımlı — açık-uçlu markdown yüzeyine taşınamaz (S8-B-YT3).
- **KGE/gömme:** yalnız doğrulayıcı-kapılı ADAY-ÜRETİCİ; 10³ ölçekte kanıt YOK, kanonu doğrudan besleyemez (S8-D-YT5 + kör). Süreç-keşfi katmanı: meşru ama fayda ölçülmemiş — deneysel m.29, çekirdek şart değil (S8-B-YT8).

## 4. x tanımı (birim veri ↔ birim bağlam)
- **x TEK SKALER DEĞİL — 4 ölçü ailesi:** token/birim · güvenilir-birim/pencere · sıkıştırma-oranı · sorgu-başına maliyet. Şemada her ölçü (min, medyan, maks, kaynak, görev) beşlisi + model_id+görev+tarih damgası; damgasız kapasite sayısı SAKLANMAZ (S8-C-YT1, C-YT5). Tek "x değeri" alanı yasak.
- **Maliyet çift eksen:** token/birim VE doğruluk/birim; oran yalnız aynı görev+model içinde türetilmiş görünüm (S8-C-YT2).
- **x İTHAL EDİLMEZ:** dışarıdaki tüm oranlar satıcı-ölçümü + karşılıklı itiraz altında; x, baglam.sqlite üzerinde KENDİ sorgu-setiyle ölçülür; dışarıdan giren her oran provenans damgası (kim ölçtü + koşum + COI) taşır (S8-A-YT6, C-YT8 GİRMEZ).
- **Kök-kısıt "birim/pencere tavanı" değil, ilgili-birim-oranı × erişim kipi:** bağlamı daraltmak doğruluğu YÜKSELTEBİLİR (79k→9,6k: %73,2→%83,6); önden-yükleme ↔ hedef-güdümlü arama iki ayrı kip (S8-C-YT4). Birim sınırı YAPISAL (blok grain doğru tarafta; sabit-boyut parçalama yasak — S8-C-YT3).
- **İlk iç ölçüm (v1, `v_x_olcum`):** ana blok tiplerinde token/birim medyanı 47-61 (madde 49 · paragraf 61 · tablo-satırı 47; bytes/4 kestirimi). ŞERH: Türkçe dil-çarpanı ölçülmemiş (~1,5× sistematik kayma olasılığı; S8-C-kör) — dil-çarpanı alanı açık.

## 5. Özütleme optimizasyonu (parquet felsefesi → ingest v2 / damıtma / kapsül)
*Transfer sınırı (S9-AB-kör): tüm Parquet kanıtı tipli-tablo verisinden; mekanizmalar YAPILANDIRILMIŞ alanlara (anahtar/tip/referans) uygulanır — serbest blok gövdesine uygulanacağı KANITSIZ. Her mekanizma lossless/lossy etiketi taşır.*
1. **Katman ayrımı [lossless]:** sıkıştırma-birimi ≠ okuma-birimi ≠ paralellik-birimi; V-1'de eşleme: blok≈page · alan-sütunu≈column chunk · dosya/seans-dilimi≈row group (S9-AB-YT1).
2. **Sözlük varsayılan-ama-eşikli [lossless]:** anahtar/kavram/tip alanları dictionary-encode (312 anahtar = düşük-kardinalite adayı); şişerse ham değere düşme kuralı YAZICIDA/ingest hattında yaşar (S9-AB-YT2). Anahtar-kaydı v1 zaten kavram-düzeyi sözlük — bu ilkenin kanonlaşmış hâli.
3. **Encoding-önce-codec-koşullu [lossless→lossy sırası]:** önce yapısal tekilleştirme (anahtar/pointer/dedup), LLM-özeti/genel sıkıştırma SONRA ve yalnız soğuk katmanda; ters sıra ölçülü marjinal kazanç bırakır (S9-AB-YT3). Sıcak/sorgu-anı katmanına genel sıkıştırma girmez.
4. **İstatistik katmanı = yazıcı-sözleşmesi [lossless]:** her ingest yazımında kolon istatistiği üretilir (formata güvenilmez; S9-CD-YT3); çift eksen — min/maks sıralı alanlara + üyelik-indeksi sırasız anahtarlara (S9-AB-YT4); yalnız düşük-seçicilikli sorgu sınıfları için (bedava değil; S9-AB-YT5).
5. **Sort-key zorunlu tasarım kararı [lossless]:** kayıtlar en sık filtrelenen anahtara göre kümelenmiş yazılır — tek hamlede hem tekrar-verimi hem atlama etkinliği (S9-AB-YT6, CD-YT2). V-1 aday sort-key: dosya_id+sira (mevcut) · alternatif katman+tarih ölçülecek.
6. **Kararlı-önek + delta [lossless]:** volatil içerik her zaman sona, üst katman dondurulur (S9-AB-YT7; K-019 sabit-önek ilkesinin ölçülmüş genellemesi).
7. **Artımlı devir gerekçesi "ucuzluk", "doğruluk" DEĞİL [lossy]:** ≈%90 token tasarrufu ~4-6 puan doğruluk vergisiyle gelir; doğruluk-kritik sorguda ham katmana yükselme yolu AÇIK tutulur (S9-AB-YT8; şema-sıkıştırma v1 "cevaplanamaz beyanıyla ham'a yüksel" ilkesiyle AYNI hüküm — çapraz doğrulandı).
8. **Lossy özütün kabul kapısı = yerel QA-eval [lossy]:** orta-oran ekstraktif özüt sinyal-gürültü kazancı verebilir; agresif %90+ rejim ölçülü kayıp bölgesi; Jarvis damıtmasının kayıp profili TRANSFER EDİLEMEZ, yerel ölçüm şart (S9-CD-YT6). MDL kabul çekirdeği (şema-sıkıştırma v1) karar verir, QA-eval davranışsal kapıdır — iki kapı TAMAMLAYICI.
9. **Compaction bilinçli politika [lossless]:** "ucuz yaz sonra topla" bedava değil — üç yönlü amplifikasyon ödünleşimi (S9-CD-YT4). Küçük korpusta row-group küçük tutulur (S9-CD-YT1).
10. **GİRMEZ:** gzip-oranı = bilgi-yoğunluğu göstergesi (çürük kanıt; NCD yalnız dedup-adayı olarak ayrı test edilir — S9-CD-YT8) · ajan-benchmark sayıları değer olarak (S8-C-YT8) · petabayt-ölçeği kazanç rakamlarının yerel benchmark'sız devri (S9-CD-kör: hepsi "yerel ölçüm bekleyen hipotez").

## 6. İlk ölçüm işleri (sıralı; her biri ~1 koşum)
1. **NDV profili:** 433 dosya / 37,7k kayıt üzerinde kolon-başına kardinalite (sözlük-adayı ayrımı; S9 kör).
2. **Tekrar-oranı:** NearDup-benzeri iç ölçüm (dedup kanıtı dış korpustan devralınamaz; S9-AB-kör).
3. **Dil-çarpanı:** Türkçe token-fertility örneklemi (bytes/4 kestirimine düzeltme katsayısı; S8-C-kör).
4. **Sort-key kıyası:** mevcut ↔ katman+tarih kümelemesi, atlama-etkinliği ölçümü.
5. **Durum-denkliği pilotu:** pano-durumu alt-alanında tutarlılık testi (S8-B-YT3).

## 7. m.16 çelişki taraması (sonuç: 0 çelişki, 2 daraltma, 2 uyum-teyidi)
- **DARALTMA:** V-1 v0 "grain = markdown blok" beyanı → "kayit-tablosu grain'i" olarak daraltıldı (süreç-başına grain bildirimi eklendi; §2). Karar değişmedi, kapsamı netleşti.
- **DARALTMA:** fikir-kutusundaki "learned world model" satırı → §3'ün koşum-kaydı-türevi + doğrulayıcı-kapılı hükümlerine bağlandı (içe-bakış düğümü yasağı yeni fren).
- **UYUM:** ingest v2 "kapsül=SNAPSHOT, gerçek kaynak kuyruk+defter+git log" = §1.1 event-store kararı · şema-sıkıştırma v1 "ham'a yükselme" = §5.7 aynı hüküm.
- **UYUM:** m.20 pointer + m.22 katman + K-019 sabit-önek = projection-pushdown/tiering/prefix-cache karşılıkları (S-9 emri "kanonda bilinenler" bölümünde verili sayılmıştı; rapor bunları daraltmadı).

*Pointer'lar: koşum manifesti `cc/pipeline/pipeline-2026-08-15-baglam-silver-katmani.md` · görünümler `tools/baglam-tablo.py` (şema v1) · D2 graf `core/world-model-tasarimi.d2`.*
