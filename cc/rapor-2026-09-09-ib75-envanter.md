# Rapor — İç-envanter: Jarvis'te var olan bağlam devri mekanizmaları (2026-09-09)

Kaynak dizin: `/Users/HasanSalihSahin/jarvis`. Yalnız yerel dosya okuma; internet kullanılmadı.

## 1. Devir dosyaları (`cc/devir-*.md`)

Kaynak: `ls cc/devir-*.md`

Toplam: **3** dosya. Tarih aralığı: 2026-08-31 → 2026-09-03 (dosya adındaki tarihten; en yeni dosya bu üçü, başka devir dosyası yok).

- `cc/devir-2026-08-31-opus-icra.md`
- `cc/devir-2026-09-02-opus-galeri-yaprak-doluluk.md`
- `cc/devir-2026-09-03-sonnet-icra-cowork.md`

Bölüm başlıkları (`grep -n '^#'`), her dosya için ayrı liste:

**devir-2026-08-31-opus-icra.md** (23 başlık, çok-turlu/EK TUR yapısı):
ÖZET — ne bitti, ne kaldı · DURMA NEDENİ (ajan freni) · İB-59 ÖLÇÜM ÖZETİ · BİRİM BİRİM SONUÇLAR · KOŞUM-ÖNÜ KAPI KAYDI (paralel-kapi) · AÇIK SORULAR (Salih'e) · SONRAKİ OTURUMUN İLK İŞİ · EK TUR (E1-E6) · EK TUR 2 (F1-F4)

**devir-2026-09-02-opus-galeri-yaprak-doluluk.md** (7 başlık):
ÖZET — ne bitti, ne kaldı · YARIM KALAN İŞ (öncelik 1) · ANA BULGU · DİSKTEKİ DURUM (commit dışı) · SİLİNENLER (Salih emriyle) · SALİH'E AÇIK SORULAR · FABLE İÇİN İLK ÜÇ ADIM

**devir-2026-09-03-sonnet-icra-cowork.md** (5 başlık):
Biten/kalan tablo · Görev metniyle küçük sapmalar (kanon çelişkisi değil) · Diğer masaya çıkan sorular · Diskteki manifest durumu · Push

**Ortak başlık frekansı** (birebir metin eşleşmesi ölçüldü, işlevsel benzerlik ayrıca not edildi):
- "ÖZET — ne bitti, ne kaldı" → **2/3 dosyada birebir aynı metin** (08-31, 09-02); 09-03'te işlevsel eşdeğeri "Biten/kalan tablo" (farklı metin, aynı işlev) → işlevsel 3/3.
- "AÇIK SORULAR" teması → 08-31: "AÇIK SORULAR (hepsi Salih'e)", 09-02: "SALİH'E AÇIK SORULAR", 09-03: "Diğer masaya çıkan sorular" — **3 dosyada da var, metin birebir aynı değil**.
- "DİSKTEKİ DURUM" → 09-02: "DİSKTEKİ DURUM (hepsi commit dışı)", 09-03: "Diskteki manifest durumu" — **2/3, benzer metin**.
- "SONRAKİ … İLK İŞ/ADIM" → 08-31: "SONRAKİ OTURUMUN İLK İŞİ", 09-02: "FABLE İÇİN İLK ÜÇ ADIM" — **2/3**.
- 09-03'e özgü, diğer ikisinde yok: "Push" bölümü, "manifest durumu" bölümü.
- 08-31'e özgü, diğer ikisinde yok: "DURMA NEDENİ", "ÖLÇÜM ÖZETİ", "KOŞUM-ÖNÜ KAPI KAYDI", çok-turlu "EK TUR" yapısı (tek dosyada 3 tur birikmiş).

AÇIK SORU: Örneklem n=3; birebir metin şablonu (aynı başlık dizisi, aynı sırayla, aynı kelimelerle) hiçbir dosya çiftinde tam eşleşmiyor — ortak olan yalnız "özet + açık sorular + sıradaki iş" işlevsel iskeleti.

## 2. Manifest dosyaları (`veri/manifest/*.json`)

Kaynak: `ls veri/manifest/*.json` + `python3 -c` ile hepsini okuyup alan-frekansı sayımı.

Toplam: **26** manifest dosyası (`u8-ib75-baglam-devri-ekip-lideri.json` en yeni, bu görevin kendi manifesti).

Örnek dosya (`u8-ib75-baglam-devri-ekip-lideri.json`) tüm alanları:

| alan | tip (bu örnekte) | tek cümle |
|---|---|---|
| birim_id | str | birimin benzersiz kimliği |
| aciklama | str | birimin ne yaptığının serbest-metin açıklaması |
| tur | str (`"pipeline"`) | birim türü (pipeline/diğer) |
| pist | str | koşum pistinin adı (yan-oturum/ana-sıra ayrımı) |
| durum | str (`"kosuyor"`) | birimin şu anki durumu |
| oncelik | int | öncelik sırası (24/26 dosyada var) |
| okur | list[str] | birimin okuduğu dosya yolları |
| yazar | list[str] | birimin yazacağı dosya yolları |
| granul | str (`"dosya"`) | çakışma granülü (dosya/bölüm) |
| sira | list[str] | aşama sıralaması (bağımlılık zinciri) |
| dislama_grubu | null/str | birlikte koşulamayacak birim grubu |
| silver | str (`"yok"`) | silver-katman çıktısı var mı |
| commit_kapsami | list[str] | commit'e girecek dosya/glob'lar |
| kanon_yuzeyi | bool | kanon dosyasına yazım var mı |
| dis_etki | list[str] | dış-dünya etkisi (WebSearch/WebFetch vb.) |
| idempotency_anahtari | str | tekrar-koşumda "bitti" sayılma koşulu |
| zorlama_modu | str (`"yol-kapisi"`) | kapı uygulama biçimi |
| beyan_disi_politikasi | str (`"hata"`) | beyan dışı durumda ne yapılacağı |
| iterasyon_ayak_izi | str (`"sabit"`) | iterasyon büyüme deseni |
| tetik_turu | str (`"seans"`) | koşumu tetikleyen olay türü |
| durma_kosulu | null/str | ne zaman durulacağı |
| kapsam_beyani | str | biriminin kapsam sınırı beyanı |
| belirlenimsiz_girdi | (18 dosyada) | — bu örnekte yok, alan adı frekans tablosunda görülüyor |
| dogrulama_kapisi | (18 dosyada) | — bu örnekte yok |
| tur_not | str | (bu örnekte var) ek serbest-metin not |
| tur_beyan | (1 dosyada) | — bu örnekte yok |

**Alan-frekansı (26 manifest üzerinden, `python3 -c`, tam sayım):**
26/26 (tüm manifestlerde ortak, 21 alan): birim_id, aciklama, tur, pist, durum, okur, yazar, granul, sira, dislama_grubu, silver, commit_kapsami, kanon_yuzeyi, dis_etki, idempotency_anahtari, zorlama_modu, beyan_disi_politikasi, iterasyon_ayak_izi, tetik_turu, durma_kosulu, kapsam_beyani.

Ortak olmayanlar: oncelik 24/26 · belirlenimsiz_girdi 18/26 · dogrulama_kapisi 18/26 · tur_not 8/26 · tur_beyan 1/26.

## 3. `core/durum-kapsulu.md` (kapsül — seanslar arası devir birimi)

Kaynak: `wc -l`, `wc -c`, `grep -n '^#'`.

Boyut: **26 satır, 5570 bayt**.

Bölüm başlıkları:
- `# Durum Kapsülü` (satır 1)
- `## Şu an` (satır 6)
- `## Açık borçlar` (satır 16)
- `## Sonraki ilk iş` (satır 22)

## 4. `tools/paralel-kapi.py`

Kaynak: dosya başlığı (docstring), `sed -n '1,60p'`.

Ne yapıyor (≤3 cümle): `veri/manifest/*.json` birim-manifestlerini okur, her birim çifti için Bernstein koşulu (yazar∩yazar=∅ ∧ yazar∩okur=∅ ∧ okur∩yazar=∅) ve PK-1..12 kural listesini uygulayarak PARALEL-SERBEST / SIRALI / RED / BEKLE hükmü verir. Planlı birimleri deterministik "dalgalar"a (aynı anda koşabilecek kümeler) böler; `--kademe N` ile dalga genişliği kısılabilir. LLM kullanmıyor (Karar 65 — kural-tabanlı, deterministik).

Girdi: `veri/manifest/*.json` (zorunlu alanlar: birim_id, tur, pist, okur, yazar, granul, sira, silver, kanon_yuzeyi, dis_etki — bkz. bölüm 2 alan listesi). Çıktı: insan-okur stdout (varsayılan) veya `--json` ile tek JSON nesnesi; çıkış kodu 0 (RED yok) / 1 (manifest bütünlük hatası) / 2 (kullanım hatası) / 3 (RED var).

## 5. `core/sablonlar/` — devir/görev şablonları

Kaynak: `ls core/sablonlar/`

6 dosya:
- gorev-emri.md
- gorev-fonksiyonu.md
- gorev-raporu.md
- hasat.md
- seans-teslim.md
- vardiya-teslim.md

AÇIK SORU: Bunlardan hangisinin "bağlam devri"ne (yan-oturum/ekip-lideri arası devir) özgülendiği içerik okunmadan söylenemez — yalnız isim listesi çıkarıldı, içerik incelenmedi (bütçe kısıtı).

## 6. `veri/gorunum/v_baglam_seyri.csv`

Kaynak: `wc -l`, `head -1`, `tail -5`, kolon istatistiği.

Toplam satır: **90** (1 başlık + 89 veri satırı).

Kolonlar (12): oturum_kisa, tarih, ilk_saat, son_saat, tur, ilk_tur_baglam, max_baglam, son_baglam, tur_128k_ustu, toplam_cikti, toplam_thinking, yan_zincir_tur, model.

Ayrı seans/oturum sayısı: `oturum_kisa` kolonunda **89 benzersiz değer** (89 veri satırı = 89 benzersiz oturum_kisa → tekrar yok, satır=oturum birebir).

Son 5 satır (ham):
```
f14bd4b6,2026-08-15,10:17:47,11:12:46,66,59425,154272,154272,25,53085,13561,0,fable-5
d0e63fae,2026-08-15,00:08:11,23:58:31,331,42154,539038,539038,290,658025,213367,0,fable-5
914d8e47,2026-08-15,00:05:43,23:59:43,224,0,811860,811860,222,279335,77445,0,fable-5
7bb80b5e,2026-08-15,00:00:10,23:59:58,175,63353,285465,285465,136,260270,120101,0,fable-5
ee6c99ff,2026-08-12,10:01:23,21:38:47,327,37744,691492,691492,259,1171301,564647,0,fable-5
```

`max_baglam` sütunu tepe 5 değer (ham, tüm 89 satır üzerinden sıralı): 994390, 812606, 811860, 761289, 741963.

`tur_128k_ustu` sütunu tepe 5 değer (ham): 785, 710, 533, 508, 397.

## AÇIK SORULAR (özet)
1. Devir dosyası şablonu birebir tekrarlanmıyor (n=3, her biri farklı başlık seti) — ortak olan yalnız işlevsel iskelet (özet + açık sorular + sıradaki iş); bu "fiilî şema" değil, gevşek bir eğilim.
2. `core/sablonlar/` altındaki 6 dosyadan hangisinin devir amaçlı olduğu içerik okunmadan belirlenemedi (yalnız isim listesi çıkarıldı).
3. `v_baglam_seyri.csv` satır=oturum birebir eşleşiyor ama kolon `tur` (int, muhtemelen "tur sayısı") ile manifest'teki `tur` (str, "birim türü") aynı ad, farklı anlam — karışıklık riski, netleştirme bu görevin kapsamı dışında.
