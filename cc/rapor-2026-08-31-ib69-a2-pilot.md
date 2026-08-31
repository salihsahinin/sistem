# İB-69 / AİLE-2 (d) — PİLOT TASARIMI + AİLE-1 AÇIK-UÇ CEVAPLARI

**Künye:** rol tez-d (İB-69 AİLE-2, (d) şeridi) · AS-OF 2026-08-31 · model sonnet-5 `[rejim: maliyet-öncelikli]` · **KOŞULMADI — yalnız tasarım.** Hiçbir prototip inşa edilmedi, hiçbir matris koşulmadı, hiçbir kanon/manifest/tools dosyası değiştirilmedi. Tek yazılan dosya budur.

**Okunan dosyalar:**
- `raporlar/2026-08-31-ib69-matris-a1-formalizasyon.md` (tam, 235 satır)
- `raporlar/2026-08-30-ib07-description-eval.md` (tam, 58 satır)
- `veri/manifest/ib-07-description-eval.json` (tam)
- `veri/sozlesme/description-eval-sorgular.json` (ilk 14 sorgu görüldü, q01-q14)
- `veri/description-eval.jsonl` (ilk 2 satır — gerçek alan adları buradan alındı)
- `raporlar/2026-08-31-k010-a3-loop-1.md` (satır 1-30, özellikle 12-13 — 300k teyidi için)
- `raporlar/2026-08-31-ib65-loop-pipeline-secim-atlas.md` (satır 230-255 — karar-masası kalemi formatı için)

---

## A) PİLOT TASARIMI — İB-07 sorgu×model alt-matrisi

### A.1 Eksen sözleşmesi (aile-1 §1 EKSEN şeması, alan alan doldurulmuş)

```
EKSEN #1:
  ad        : "sorgu_id"
  tip       : kategorik
  degerler  : ["q06","q07","q08","q09","q10"]
              [GERÇEK id'ler — veri/sozlesme/description-eval-sorgular.json;
               İB-07'nin kesintide bıraktığı 15 eksik satırın (q06-q20 tekrar3)
               İLK 5'i — pilot, açık borcu doğrudan hedefler, uydurma sorgu yok]
  rol       : dis   [§A.2 gerekçeli]
  kaynak    : dosya — veri/sozlesme/description-eval-sorgular.json

EKSEN #2:
  ad        : "model"
  tip       : kategorik
  degerler  : ["claude-haiku-4-5-20251001", "[?]"]
              [1. değer İB-07'nin fiilen kullandığı TAM snapshot id (kısa ad değil,
               veri/description-eval.jsonl:1 `isci_model` alanı doğrular);
               2. değer için repo-genelinde başka bir TAM API snapshot id
               ARANDI (grep -rhoE 'claude-[a-z0-9.]+-[0-9]{8}' .) — BULUNAMADI,
               dolayısıyla [?] — karşılaştırma modeli Katman-1 seçimi bekliyor]
  rol       : ic   [§A.2 gerekçeli]
  kaynak    : sabit (bu rapor önerisi) + Salih onayı (2. model adı)

MATRIS:
  eksenler       : [sorgu_id, model]
  tekrar         : 3   [T4 tekrar-varyansı ölçülebilsin diye; İB-07 deseniyle tutarlı]
  erken_durdurma : yok
  hucre_tipi     : tek_cagri
```

Ö1 (tamlık) sağlanıyor: iki eksen de ≥1 değer taşıyor, biri dış biri iç. Ö2 (yalanlanabilirlik) sağlanıyor: planlanan hücre kümesi `sorgu_id × model × tekrar` dosyadan türetilir — bu raporun düz metninden değil, `veri/sozlesme/description-eval-sorgular.json` + Salih'in onaylayacağı 2. model adından.

### A.2 Dış/iç eksen kararı (aile-1 §6, Ö-A > Ö-B > Ö-C sırasıyla)

- **Ö-A (PK-10 ayak izi):** nötr. Tüm hücreler tek append-only kütüğe (`veri/description-eval.jsonl` uzantısı ya da yeni dosya) yazıyor; hiçbir hücre başka bir hücrenin dosyasını okumuyor/üzerine yazmıyor → SIRALI zorunluluğu yok, eksen sırası bu ölçütten etkilenmez.
- **Ö-B (bağımsızlık):** nötr. Her hücre kendi `girdi = {sablon_id, sorgu_id, model}` ile bağımsız yanıt üretiyor, hiçbiri diğerinin çıktısını okumuyor.
- **Ö-C (maliyet/yeniden-kullanım) — KARAR VERİYOR:** model ekseni sabitlenince (tek model üstünde art arda 15 çağrı: 5 sorgu × 3 tekrar) sistem-promptundaki **sabit 14-skill listesi metni** (her çağrıda birebir aynı içerik, İB-07'nin de kullandığı desen) prompt-cache'e bir kez yazılır, kalan 14 çağrı önbellek-okuma ile döner; sorgu ekseni dış olsaydı model art arda değişeceği için her sorgu bloğunda cache yeniden ısınırdı (2 model arası geçiş = cache miss). **Karar: model DIŞ, sorgu_id İÇ.** (İB-07'nin kendi vakasında karar "sorgu dış / tekrar iç" idi çünkü orada tek model vardı ve paylaşılan kurulum tekrarlar arasındaydı; burada ikinci eksen eklendiğince paylaşım sınırı model sınırına taşınıyor — aynı ölçüt, farklı eksen çifti, tutarlı uygulama.)
- Not (aile-1 §6.2 dersi tekrarı): eksen sırası KAPI 2'yi (çağrı sayacı) etkilemez — `N_cagri = |dis|×|ic|×tekrar` sıradan bağımsızdır, yalnız M_dis paylaşımını etkiler.

### A.3 Hücre sözleşmesi

- **Girdi:** `{sablon_id: "ib07-secilen-skill-v1", eksen_degerleri: {model: <deger>, sorgu_id: <deger>}}` — aynı şablon (İB-07'nin 14-skill-listesi + sorgu metni), yalnız model ve sorgu değişkeni değişir.
- **Çıktı TİPİ:** `etiket` — kapalı küme, `secilen_skill ∈ {14 skill} ∪ {HİÇBİRİ}` (İB-07 ile birebir aynı şema, `veri/description-eval.jsonl:1` `secilen_skill` alanı). §2 Ö1 (tiplilik) sağlanıyor → bu bir MATRİS'tir, LLM-yargıç İSTİSNA dalına düşmez.
- **Toplama (§3'ün T1-T5'i):**
  - **T1 (sorgu bazlı satır özeti):** anlamlı — her sorgunun iki model arasında isabet oranı.
  - **T2 (model bazlı sütun özeti):** anlamlı — İB-07'nin asıl sorusu budur (model karşılaştırması).
  - **T3 (etkileşim):** **hesaplanabilir** — 2 model × 5 sorgu, isabet etiketi orana çevrildikten sonra (§3 kırılan-varsayım notu: ham etiket üzerinde tanımsız, oran üzerinde tanımlı) `h(a,b) − (satir_ort(a)+sutun_ort(b)−genel_ort)` hesaplanır; hangi sorgu hangi modelde orantısız kötü/iyi diye gösterir. 2×5 küçük hücre sayısı istatistiksel güç açısından zayıf ama T3 formülü tanımsız değildir.
  - **T4 (tekrar varyansı):** anlamlı ve zorunlu — tekrar=3 seçildi tam bunun için; örnekleme gürültüsünün model başına farklı olup olmadığını gösterir.
  - **T5 (kapsama):** anlamlı — `|yazılan|/30`, kesinti/resume göstergesi.

### A.4 Kütük satırı (§5'in 13 alanı, ÖRNEK damgalı)

```json
{"kosum_id": "ib69-a2-pilot:ÖRNEK:2026-08-31", "hucre_anahtari": "model=[?]|sorgu=q06|tekrar=1", "ts": "2026-08-31T00:00:00Z", "git_head": "ÖRNEK-sha7", "eksen_degerleri": {"model": "[?]", "sorgu_id": "q06"}, "tekrar": 1, "hucre_tipi": "tek_cagri", "model": "[?]", "sonuc": {"tip": "etiket", "deger": "karar-hatti"}, "toplama_yontemi": "deterministik", "token_giris": 0, "token_cikis": 0, "token_onbellek_okuma": 0, "sure_ms": 0, "kosum_durumu": "planli"}
```
(`token_*` ve `sure_ms` alanları ÖRNEK satırda 0 — gerçek koşumda M-1 borcunu kapatan değerler buraya yazılır; `sonuc.deger` ÖRNEK, gerçek altın etiket q06 için `veri/sozlesme/description-eval-sorgular.json`'da ayrıca doğrulanmalı.)

### A.5 Maliyet (kaba, m.29 — aile-1 §4 formülüyle)

```
N_hucre  = |dis| × |ic| × tekrar = 2 (model) × 5 (sorgu) × 3 (tekrar) = 30
N_cagri  = 30                                  [tek_cagri hücre tipi → 1 hücre = 1 çağrı]

KAPI 1 (token bütçesi): toplam ≈ 2×M_dis + 30×T_hucre
  T_hucre ÖLÇÜLMEDİ (M-1 borcu) → toplam SAYISAL VERİLEMEZ, yalnız parametrik:
  toplam ≈ 2×M_dis + 30×T_hucre    [Ö1 denetimi bu yüzden koşum ANINDA yapılmalı,
                                     tasarım anında değil]

KAPI 2 (çağrı sayacı, İB-07'yi kesen kapı — token'dan bağımsız, SAYIYLA denetlenir):
  N_cagri = 30
  DURDUR eşiği = 144 (.claude/hooks/pretool-ajan-fren.sh:36-37,52)
  30 / 144 ≈ %21 — bu şeridin TEK BAŞINA payı düşük.
  Ancak sayaç OTURUM-genelinde kümülatiftir (aile-1 §4 KAPI 2 notu); bu raporun
  yazıldığı oturumdaki güncel sayac_oturum değeri bu tasarım turunda ÖLÇÜLMEDİ
  (İB-69 emri "matris koşma" dediği için sayaç okunmadı). Güvenli koşum şartı:
  30 + sayac_oturum ≤ 144  →  sayac_oturum ≤ 114 olduğu sürece bu pilot tek
  oturumda tamamlanır; aşarsa kütük append-only olduğu için oturuma bölünür
  (§A.6 resume kuralı).
```

### A.6 Durma/resume yüklemi (m.38 formu)

```
kalan_is = { (model,sorgu,tekrar) : model∈{2 deger} ∧ sorgu∈{5 deger} ∧ tekrar∈{1,2,3} }
           − { hucre_anahtari ∈ kütük }
done ↔ |kalan_is| = 0
∀ kesinti ( kütük append-only ∧ hucre_anahtari tekil → veri kaybı = ∅ ∧
            kalan_is tek sorguyla (kütük − manifest_anahtarlar farkı) hesaplanır )
```
Kesinti hâlinde kalan_is: örn. KAPI-2 30. çağrıdan önce hook keserse (örn. 18. çağrıda durursa), kalan_is = kalınan hücrelerin kümesi = planlanan 30 − yazılan N; İB-07 dersi gereği bu fark ELLE değil kütük sorgusuyla (`hucre_anahtari` kümesi farkı) alınmalı.

### A.7 Koşum onayı MASADA

Salih'in onayı gereken tek karar: **2. modelin TAM API snapshot id'si** — bu rapor `[?]` bıraktı, koşum başlamadan önce dolmalı (aksi halde eksen tek değerli kalır, matris değil tekli-model listesi olur).

### A.8 Pilotun ölçüm çıktısı

Bu pilot koşulursa:
- **M-1 borcu (T_hucre) KAPANIR** — 30 hücrenin `token_giris/token_cikis/token_onbellek_okuma/sure_ms` alanları doğrudan bu koşumdan yazılır; `T_hucre` bu 30 satırın ortalaması/medyanı olarak TÜRETİLİR (aile-1 §4 son satırı: "TÜRETİLİR, TAHMİNLE DOLDURULMAZ" — pilot bunu ilk kez sağlar).
- Ayrıca İB-07'nin kendi açık borcunu (q06-q10'un eksik tekrar-3'ü) kısmen kapatır — ama İB-07'nin kendi 14-skill / 20-sorgu tam matrisini TAMAMLAMAZ, yalnız 2. model ekseniyle genişletilmiş küçük bir alt-küme koşar; İB-07'nin orijinal 60 hücresinin geri kalanı ayrı iştir.

---

## B) AİLE-1 §8'den DEVREDİLEN 6 AÇIK UÇ

1. **M-1 (`T_hucre` ölçüm borcu):** açık kalıyor, bu pilotla KAPANACAK biçimde tasarlandı (§A.8). Pilot koşulmadan sayı üretilemez, tasarım anında da üretilmedi (m.6, tahminle doldurma yasağı).
2. **`kademe_esigi` alt-türü:** açık kalıyor — İB-66 §5.2'nin hiçbir sınıfına girmiyor, aile-1 §6.3'ün tespit ettiği gibi yeni bir seviye alt-türü gerektiriyor; bu Katman-1 kararıdır (kanon şema değişikliği), (d) şeridinin yetkisi dışında.
3. **K-020 birleşme kararı (promptfoo/Optuna vs. kendi harness):** SEN VERME talimatına uyulur — hüküm masada; (b) şeridinin ürettiği 3-model karşılaştırması bekleniyor, bu rapor yalnız pilotun kendi harness'i (İB-07 deseni) ile uyumlu tasarlandığını not eder.
4. **Manifest matris birim tipi:** (c) şeridi işliyor; bu pilot açısından ŞART olan alanlar — `hucre_tipi`, `tekrar`, `erken_durdurma`, ve nested-birimlerin zorunlu kıldığı (İB-65 §5.1) `dis_tavan`/`ic_tavan`/`butce_sayaci`/`ayak_izi_yolu` benzeri alanlar eğer matris `tur` yeni bir değer alacaksa. Pilot kendisi `tur=pipeline` kapsamında kalabilir (tek-turlu, hibrit değil) — bu yüzden (c) şeridinin göç kararı bu pilotu BLOKE ETMEZ.
5. **`[?]` 300k ham ölçüm teyidi — TEYİT EDİLDİ (yaklaşık/dolaylı).** `raporlar/2026-08-31-k010-a3-loop-1.md:12` şu satırı taşıyor: *"tur-1 TEMİZ + İngilizce commit geçti; **token tavanı doldu** (535k/500k, 2 iterasyon) | **gnhf token birimi = önbellek-okuma DAHİL**; iterasyon tabanı ~300k."* Rakam GERÇEKTEN orada, birim gnhf İTERASYONU (aile-1'in ayırdığı `T_gnhf`, tek-çağrı hücre DEĞİL), önbellek-okuma AÇIKÇA dahil ("önbellek-okuma DAHİL" ibaresi birebir var). Şerh: bu "~300k" tek bir iterasyonun ölçümü değil, 535k/500k tavan aşımından (2 iterasyonda) geriye türetilmiş **yaklaşık** bir rakam (535k÷2≈267k, metinde "~300k" olarak yuvarlanmış) — yani doğrudan tek-satır ham ölçüm değil, dolaylı türetim. Aile-1'in T_gnhf tabanı için kullanımı (300k, önbellek dahil) İÇERİK olarak DOĞRU ve KAYNAKLI; kesinlik derecesi "~" işaretiyle zaten aile-1'in kendi metninde de korunmuş.
6. **Uygun-iş envanteri:** (a) şeridinde — atlanır.

---

## C) KARAR-MASASI KALEMİ TASLAĞI (İB-65 §5.2 formatında)

> **Kalem adı:** İB-07 sorgu×model pilot matrisi (5 sorgu × 2 model × 3 tekrar = 30 hücre) koşulsun mu, hangi kural paketiyle?
>
> **Bağlam:** İB-07 20×3×14 matrisi 45/60 hücrede ajan-freniyle (DURDUR=144, İB-07 koşumunda eski eşik 72) kesildi; kalan 15 hücreden ilk 5'i (q06-q10, tekrar3) bu pilotun sorgu ekseni. Aile-1 (`raporlar/2026-08-31-ib69-matris-a1-formalizasyon.md`) şemayı v0 olarak formalize etti ama M-1 (`T_hucre` ölçüm borcu) hâlâ açık — hiçbir gerçek matris koşumu token/süre kütüklemedi. Bu pilot hem borcu kapatmayı hem şemayı ilk kez canlı veriyle sınamayı hedefliyor.
>
> **Öneri:** pilot koşulsun; kural paketi = aile-1 §5 kütük standardının 13 alanı ZORUNLU (özellikle `token_giris/token_cikis/token_onbellek_okuma/sure_ms`, M-1 için) + §A.2'nin model-dış/sorgu-iç sırası + KAPI-2 denetimi koşum ANINDA güncel `sayac_oturum` ile yeniden yapılsın (bu rapor sayacı ölçmedi).
>
> **Artı:** N_cagri küçük (30, 144 eşiğinin ~%21'i) → tek oturumda güvenle bitebilir; M-1 borcunu ilk kez gerçek veriyle kapatır; İB-07'nin kendi açık 15 hücresinden 5'ini de kapsar (iki kuş); şema (aile-1 v0) ilk kez canlı sınanmış olur, K-020 kararına girdi sağlar (hangi hazır aracın alan şemasıyla ne kadar örtüştüğü somutlaşır).
>
> **Eksi:** 2. modelin TAM snapshot id'si eksik ([?]) — Salih onayı olmadan koşum başlayamaz; 5×2 küçük hücre sayısı T3 (etkileşim) için istatistiksel güç zayıf, yalnız gösterge niteliğinde; pilot İB-07'nin 60 hücrelik asıl borcunu kapatmaz, yalnız 5/15'ini.
>
> **Karşıt seçenek:** pilotu atla, doğrudan İB-07'nin kalan 15 hücresini (tek model, orijinal şema) tamamla — M-1 borcu bu şekilde kapanmaz (tek modelli koşum ikinci eksenin maliyet davranışını göstermez), ama daha basit ve daha hızlıdır (15 çağrı, tek eksen).
>
> **Bağlı borçlar:** M-1 (bu pilotla kapanması hedeflenen) · 2. model snapshot id seçimi (Katman-1/Salih) · `kademe_esigi` alt-türü kararı (bu pilotu ETKİLEMEZ, `erken_durdurma=yok` seçildi) · K-020 (bu pilotun sonucu girdi sağlar, karar bağımsız kalır).
>
> **m.16 kapısı:** bu kalem aile-1'in v0 şemasını UYGULAR, çelişmiyor — yeni kural/kanon değişikliği önermiyor, mevcut şemanın ilk canlı sınaması; kapı gerektirmiyor, doğrudan Salih onayına gidebilir.
