# Seans teslim — galeri-sıralama sentetik veri + CatBoost YetiRank hattı (2026-08-31)

**Hat:** jarvis-dışı iş şeridi (m.15 / md.49 sınıfı — Otonet galeri-scoring).
**Yüzey:** Claude Code masaüstü, ana-sıra, Opus 5.
**Çalışma alanı:** `kuyruk/galeri-siralama/` — **COMMIT'LENMEZ** (Karar 73 EK freni,
`.gitignore:39`). Bu rapor o klasörün *dışına* çıkan tek kayıttır ve yöntem düzeyindedir;
şirketin üretim şema ayrıntısı (kolon sözlüğü, eşleme tablosu) bilerek klasörün içinde
bırakılmıştır (md.49).

---

## Bugün gerçekten ne değişti

Salih'in isteği: gerçek veri gelmeden (Karar 83 E1: CSV'ler hâlâ gelmedi) **sentetik
veriyle uçtan uca sıralama hattı** kurmak, süreci öğreterek ve koşumları Salih'e yaptırarak.

**Üretilen (11 script + 3 doküman + 1 HTML yüzey, hepsi commit dışı klasörde):**

| dosya | işlev |
|---|---|
| `01_uret.py` | sentetik evren üreticisi (tohum 42, deterministik); `--v2` soğuk-başlangıç kohortları · `--uzun` ~2 yıllık takvim · `--tohum N` |
| `02_birlestir.py` | 4 ham tablo → tek eğitim tablosu; snapshot **as-of join** (`merge_asof backward`) |
| `03_egit.py` | zaman-oransal bölme → CatBoost YetiRank → 4 taban çizgisi + segment kırılımı; bayraklar `--segment --normalize --agirlik --ikili --logsuz --tuzak --sizinti --hizli` |
| `04_agac_bak.py` | eğitilmiş ağaçları tek tek okur (bölmeler · 64 yaprak · satır izi · CTR listesi) |
| `05_agac_html.py` + `sozluk_kolon.py` | 4 sekmeli tek-dosya HTML (genel bakış · 552 ağaç · sıralama sonucu · 64 kolonun sözlüğü) |
| `06_segment_analiz.py` | hangi feature kombinasyonlarında örnek var/yok + segment bazlı model performansı |
| `07_kesif_kotasi.py` | ilk-N'de soğuk başlangıca k slot ayırmanın bedel/kazanç tablosu |
| `08_ablasyon.py` | müdahaleleri sırayla koşup **güven aralıklı** karşılaştırma; `--topla` diskteki modellerden tabloyu eğitimsiz üretir |
| `09_cok_tohum.py` | birkaç bağımsız tohumu havuzlar (güç artırma) |
| `10_ayrim_analizi.py` | "teklif verir" ↔ "satın alır" ayrımı (grup içi AUC) + tek-sonuç/huni testi |
| `ortak.py` | sürüm bayrakları + veri klasörü adı tek kaynaktan |
| `bulgular-model-eksikleri.md` | **ekip notu**, 453 satır, 15 bölüm — aşağıdaki bulguların kalıcı kaydı |

**Sentetik evren:** 5 marka × 4 seri × 3 trim = 60 trim · 420–1.018 galeri · haftada
3 gün + gün-içi 2. oturum · oturumda 20 lot sırayla · grup = **bir lot** · aday havuzu ~55.
Etiket Salih'in 5 kademesi (4 kazandı ⊂ 3 ikinci ⊂ 2 teklif ⊂ 1 baktı ⊂ 0 yok), huni
tutarlı üretiliyor. Zaman sadakati: sayaçlar lot lot as-of, 10 hafta ısınma, sızıntı yok.

### Ölçülen bulgular

**(1) Model çalışıyor ve elle skoru geçiyor.** v1: HR@1 0,768 vs elle-ağırlıklı skor 0,691
vs popülerlik 0,144 vs rastgele 0,021. Tavan (üretim kuralını bilseydik) 0,838 → model
erişilebilir iyileştirmenin **%52'sini** aldı.

**(2) Ortalama metrik segment zaafını GİZLİYOR.** Kazananın kademesine göre HR@1:
trim geçmişi olan 0,841 (lotların %90,6'sı) · seri 0,125 · marka 0,000 · sadece-teklif 0,000.
Genel skor tamamen büyük segmentin sayısı.

**(3) Soğuk başlangıç: model ayırt EDİYOR, sadece aşağı koyuyor.** Soğuk adaylar
*arasında* HR@1 0,412 (rastgele 0,036 → 11× iyi); tüm havuzda aynı kazananın sırası 11,0.
Yerleştirme **istatistiksel olarak doğru**: soğuk satırların kazanma oranı %0,15, genel
taban %1,80 — 12 kat düşük. Sorun modelde değil hedefte (ortalama NDCG ≠ keşif).

**(4) Üç model-tarafı müdahale de tabanı GEÇMEDİ.** `--segment` (signal_source feature),
`--normalize` (grup içi yüzdelik), `--agirlik 4` (soğuk-kazananlı lotlara group_weight);
tekli ve birleşik 6 konfig, test 1.420 lot. En büyük fark 0,0076, gürültü eşiği ±0,022 →
**ayırt edilemez** ve altı konfigin altısı da tabanın altında.

**(5) Çözüm çıktı tarafında: keşif kotası.** İlk 5 slotun 2'si soğuk başlangıca ayrılırsa
HR@1 ve HR@3'e **sıfır maliyet**, HR@5'te −3,3 puan, soğuk kazananın ilk 5'e girme oranı
0,679 → **0,868**. k=3'te HR@3 bozuluyor → diz noktası k=2. (380 ve 1.420 lotta iki kez
doğrulandı.) Bu bir model değil **ürün** kararıdır.

**(6) Model "teklif verir" ile "satın alır"ı ayırt ediyor — hem de daha iyi.**
Grup içi AUC: teklif ayrımı 0,904 · **alım ayrımı (4 vs 2-3) 0,949** · kazanan↔sıradan
teklifçi 0,968. Tek zayıf hücre kazanan↔ikinci 0,811 — problemin tabanı (ikinci,
kazananla aynı profilde; fark ihalenin kurası).

**(7) Model tek sonuç aramıyor, huninin tamamını öğreniyor.** Beş kademede ortalama sıra
monoton (34,1 → 24,4 → 11,9 → 3,2 → 1,6); **kazananı gruptan çıkarınca** kalan 0/1/2/3
için NDCG@3 = 0,835; tepe keskinliği 0,245 (sivri değil, kısa liste). En zayıf halka
`1 vs 0` (AUC 0,701) — görüntüleme logu en gürültülü sinyal.

**(8) Dereceli etiket (0-4) tutulmalı — gerekçe doğruluk değil SAĞLAMLIK.** İkili (0/1)
etiketle HR@1 birebir aynı (0,6690), derinlik metrikleri gürültü içinde; ama gürültü
kolonlarının önem sırası dereceli 41/63 ve 31/63 iken ikilide **15/63 ve 7/63**. Grup başına
bilgi taşıyan pozitif satır 1 → ~20 farkı, model boşluğu gürültüyle dolduruyor.

---

## Hangi karar verildi (kaynak + gerekçe + geri-açma)

**Katman-1 kanon kararı YOK.** Bu şerit jarvis-dışı iş; kararlar iş-tarafı tasarım
kararlarıdır ve Salih beyanıyla alınmıştır:

1. **Grup = lot (tek araç), (trim × ihale) değil** — Salih seçimi "a".
   *Gerekçe:* `sale_car_raw.buyer_id` araç bazında; grain'i yukarı çekmek bilgi atar.
   Ölçüm: (ihale, trim) gruplarının %14,2'sinde aynı trimden birden fazla araç var.
   *Geri-açma:* `02_birlestir.py`'de `group_id`'yi `trim + ihale_id` yapmak ~15 dk.
2. **Dataset A + Dataset B kolonları BİRLİKTE kullanılacak** — Salih beyanı.
   *Gerekçe:* B'de payı olup paydası A'da olan 9 kolon var; B tek başına sessizce yanlış
   söyler. *Geri-açma:* yok, tek yönlü kısıt.

---

## Hangi fikir ADAY kaldı (karar DEĞİL)

- **Keşif kotası k=2** — bedel/kazanç tablosu ölçüldü, hüküm ürün tarafında (Salih/ekip).
- **`signal_source` gerçek veride feature olarak verilsin** — sentetikte ayırt edilebilir
  fayda ölçülemedi; gerçek veride yeniden ölçülmeli.
- **Görüntüleme logunun (etiket 1) iş değeri** — `--logsuz` bayrağı hazır, koşulmadı.
  Log toplama maliyetinin gerekçesi bu koşumdan çıkacak.
- **Ayrı model + Reciprocal Rank Fusion** — elenmiş değil, yedek (kalibrasyonsuz birleştirme
  mümkün; kota daha az bakım yükü istediği için önde).
- **`--agirlik` bırakılsın** — genel performansı bozdu, soğuk segmentte karşılığını vermedi.

---

## Sonraki ilk iş

1. **`03_egit.py --v2 --uzun --logsuz` + `10_ayrim_analizi.py` ile karşılaştırma** —
   görüntüleme logunun izole değeri. Üç etiket tasarımı: dereceli / logsuz / ikili.
2. **`09_cok_tohum.py --v2 --uzun --tohumlar 42,43,44,45,46`** (~100 dk arka plan) —
   ablasyon hükmünü havuzlanmış örneklemle kesinleştirir. Beklenti: hüküm değişmez.
3. **Gerçek CSV'ler geldiğinde** (Karar 83 E1 bekleme sürüyor): `06_segment_analiz.py`'nin
   segment tanımlarını türetilmiş yerine gerçek `signal_source` kolonuyla değiştir; geri
   kalan hat aynen koşar.

---

## Neyi yeniden açmak için hangi koşul gerekir

- **Grup tanımı (lot ↔ trim×ihale):** gerçek veride aynı oturumda aynı trimden çoklu araç
  oranı %14'ün belirgin üstüne çıkarsa.
- **Model-tarafı müdahaleler:** çok-tohumlu koşum (madde 2) ±0,05 hassasiyette bir
  müdahaleyi tabanın ÜSTÜNDE gösterirse.
- **Ayrı model + RRF:** kota k=2 ürün tarafında reddedilirse.

---

## Hasat

**Özütler (5):**
1. **Ölçü birimi yanlışsa iyileştirme çabası boşa gider.** "Soğuk başlangıç" kalıcı bir
   galeri özelliği değil, tahmin anındaki **satır durumu**. Kohort etiketiyle ölçünce uzun
   takvim segmenti *iyileştirmiş* gibi göründü; gerçekte kohort soğukluktan çıkmıştı
   (gerçekten soğuk kazanan lot 17 → 7'ye düştü). Düzeltme: kohort boyu sabit sayı değil
   **haftalık akış**.
2. **"Fark var mı" değil "fark gürültünün üstünde mi".** 49 lotluk bir kohortta %20'lik
   oranın %95 güven aralığı ±0,11; ±0,03 için ~680 lot gerekir. Ablasyon farkları 2-4 lota
   denk geliyordu. Güç ölçülmeden müdahale yorumlanmaz.
3. **Ortalama metrik segment zaafını gizler** — genel HR@1 büyük segmentin sayısıdır;
   her koşumda kırılım zorunlu olmalı.
4. **Bölme mantığı tek yerde tanımlanmalı.** Üç script'ten ikisi sabit tarihle bölmeye
   devam edince test kümesi 1.420 yerine 320 lot göründü; hata patlamadı, sessizce yanlış
   metrik üretti. (Karar 77 ailesinin metrik-tarafı kardeşi.)
5. **Dereceli etiketin faydası doğrulukta değil gürültü direncinde.** Aynı top-1'i
   4 kat daha az gürültüye uyarak vermek, 200 küsur kolonluk gerçek veride belirleyici olur.

**Wiki-delta (kuyruğa):** yok — şerit jarvis-dışı, kavramlar iş-tarafı. Genel-geçer olan
tek kalem özüt-2 (istatistiksel güç ↔ segment iddiası); `wiki/README.md` kuyruğuna
**aday** olarak düşürülebilir, bu turda yazılmadı.

**Verilebilir miydi (V20):** Ablasyon koşumları (6 konfig × ~3 dk) ve çok-tohumlu koşum
mekanik, işçi-ajana verilebilirdi. Verilmedi çünkü Salih koşumları kendisi yapmak istedi
(öğrenme amacı, açık talep). Bu bilinçli bir kapasite tercihidir, kayıp değil.

**Araç-çıktısı kuralı (KB-50 a):** ihlal yok — büyük çıktılar (Excel dökümü 50,6 KB)
dosyaya yazılıp pointer'la okundu.

---

## Ritüel ölçümleri

- **hareket-tablo:** bronz 5.146 çağrı (130 yeni) · silver 4.796 satır · 19 gün · 3/3 test PASS.
- **silver-sağlık kapısı:** **çıkış 0** (T-Ç çelişki yok). WARN: T-C3-ılık 109 · T-C6 1.
  Kuyruk adayları: SUPERSEDED 4 · YETİM 243 (eşik 351 altında, PASS) · KAPANDI 82 ·
  T-A ön-eleme 6.780 (500 yazıldı). **Aday kuyruğu karar değil, Salih triyajı.**
- **skill-eşik:** 6 çift · yeni-pencere sapması **0** · bant: atlas-kosum×opus-5 n=205
  medyan 26.524 tok/473 sn.
- **kural-sayacı:** 19 birim / 42 satır / 7.163 byte → **OK** (eşik 100).
- **bayat-çekim:** D3 kuyruk **0 dosya** → yeniden-çekim yok (uydurma yok).
- **token × zaman (V28):** bu oturum **380 tur · ilk-tur bağlamı ~64k · max bağlam 678.281 ·
  128k üstü 354 tur · toplam çıktı 900.357 token.**
  → **uzun-koşum: max bağlam 678.281 (354 tur üstte)** — kayıtlı en uzun koşum
  (önceki tepe 567.096). KB-52 politikası devrede, hasat kontrol listesi aşağıda.
- **boyut-tetiği:** `kuyruk/senaryo-defteri.md` **56,5/48 — AŞIM** (Karar 83 bloğu +
  bu blok) · `KILAVUZ.md` 16,8/16 aşım · `fikir-kutusu.md` 20,2/20 sınır aşımı ·
  `core/pano.md` 12,2/12 sınır aşımı · kapsül 6,8/8 ✓ · CLAUDE.md 6,9/7 ✓.
  **Damıtma tetiği 4 dosyada; ilk boş seansta Salih imzasıyla.**

## Hasat kontrol listesi (KB-52, uzun koşum zorunlu)

1. **Kalıcı kural/karar adayı ingest'e girdi mi?** Evet — 2 iş-tarafı karar bu raporda,
   5 aday fikir listelendi; kanon kuralı doğmadı (Katman-1 dokunuşu yok).
2. **Açık pipeline/manifest T beyanı aldı mı?** Konusuz — bu şerit manifest hattını
   kullanmadı (jarvis-dışı, paralel-kapı dışında).
3. **Workflow/ajan koşumlarının tahmin↔gerçek kaydı ambara düştü mü?** Konusuz —
   bu oturumda Workflow ve alt-ajan koşumu **yok** (Agent çağrısı 0).
4. **Paralel oturum devir notu / çakışma kaydı?** Kapanış anında canlı CLI oturumu yok
   (ps teyidi). Çalışma dizinindeki 47 değişik dosya **türev** (graf/ · veri/gorunum ·
   jsonl kütükler) ve bu ritüelin kendisi tarafından yeniden üretildi (Karar 77 usulü:
   merge denenmedi, üretici koşuldu).

## Açılış planı yoklaması (Karar 79 D3 / KL16-6)

**Açılış ritüeli KOŞULMADI** — oturum "seans başı" tetiğiyle değil, doğrudan iş talebiyle
açıldı; seans-hedefi beyan edilmedi. Dolayısıyla plan↔sonuç kıyası yapılamıyor.
**Sapma kaydı:** hedefsiz açılan uzun oturum (380 tur) — m.29 seans-hedefi denemesinin
sayacına bu oturum GİRMEZ.
