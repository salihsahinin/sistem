# İB-69 aile-1 — ANTİTEZ (m.40b v0.2)

AS-OF: 2026-08-31 · Ajan: İB-69 aile-1 ANTİTEZ işçisi · Kapsam: 5 tez raporu + `cc/gorev-2026-08-31-ib69-matris-kosum-atlas.md` (emir) çapraz-okuma; web kullanılmadı (gerekmedi, kırılma noktaları iç-tutarsızlık ve emir-rapor çelişkisiyle bulundu).

Görev: destekleyici kanıt aranmadı, yalnız kırılma noktası arandı. 6 çürütme + 4 "SAĞLAM KALDI".

---

## Çürütme 1 — "Toplama LLM'siz deterministik olabilir" (Karar 65) kaçış yolu gösterilmedi

**HEDEF İDDİA:** `cc/gorev-2026-08-31-ib69-matris-kosum-atlas.md:10` — "toplama/indirgeme kuralları (satır/sütun özetleri; LLM'siz deterministik toplama, Karar 65)" şemanın ZORUNLU alanı sayılıyor. `cc/rapor-2026-08-31-ib69-a1-literatur.md:37` kendisi de itiraf ediyor: "LLM hücresi... serbest-metin çıktısıdır — doğrudan ortalanamaz, önce bir skorlayıcı/rubrik ile skalere indirgenmesi (ör. LLM-judge puanı) gerekir."

**KIRILMA:** Emir "LLM'siz deterministik toplama" istiyor ama tez raporlarının HİÇBİRİ hücre çıktısı serbest-metinken bunun nasıl LLM'siz yapılacağını GÖSTERMİYOR. İki somut iç-emsal (`cc/rapor-2026-08-31-ib69-a1-ic-emsal.md`) incelendiğinde: İB-49 d2-eval gerçekten LLM'siz deterministik (çünkü hücre çıktısı zaten yapılandırılmış — `.d2` dosyası, derleme kodu, precision/recall) ama İB-07 description-eval hücre çıktısı da aslında zaten TİPLİ (`secilen_skill`: 14 sabit etiketten biri) — yani her iki "deterministik toplama" emsali de GİRDİYİ zaten tipli/kapalı-küme zorlayarak elde ediyor, serbest-metin çıktıyı LLM-judge'sız indirgeyen TEK bir emsal YOK. Emrin "LLM'siz" şartı yalnız çıktı baştan tipli zorlanırsa tutar; bu, iddianın kendisini değil, iddianın ÖN-KOŞULUNU (hücre sözleşmesi tipli olmalı) gizliyor.

**GÜCÜ:** SINIRLAYICI — iddia YANLIŞ değil ama gizli bir ön-koşula (çıktı tipi zorlaması) bağlı; bu ön-koşul şemanın "zorunlu alan" listesinde AYRI maddelenmemiş.

**ONARIM:** "Toplama LLM'siz deterministik olabilir" cümlesine "ANCAK VE ANCAK hücre-sözleşmesi (İB-69 şema madde) çıktıyı kapalı-küme etikete/sayıya zorluyorsa" koşulu eklenmeli; serbest-metin hücre için toplama adımı ya LLM-judge (ek maliyet+gürültü, m.6 gerilimi literatür §5-2'de zaten not edilmiş) ya da regex/kural-tabanlı çıkarım (kırılgan) olarak AYRI dallanmalı.

---

## Çürütme 2 — Maliyet modeli |A|×|B|×300k: taban gnhf çok-turlu koşum, matris hücresi tek-Agent çağrısı — 2 mertebe fark gizleniyor

**HEDEF İDDİA:** `cc/gorev-2026-08-31-ib69-matris-kosum-atlas.md:5` — "gnhf iterasyon tabanı ~300k (önbellek-okumalı birim, 08-30 e2e715 vakası) → hücre-çarpımı maliyet modeli şemanın ZORUNLU alanı." `cc/rapor-2026-08-31-ib69-a1-eksen-esleme.md:88` bu tabanı doğrudan `T` (birim hücre maliyeti) olarak kullanıyor: "`T` = ölçülmüş iç-seviye taban maliyeti (gnhf: 300k...)".

**KIRILMA:** 300k rakamının kaynağı (`raporlar/2026-08-31-ib66-...md:132`) AÇIKÇA gnhf'nin kendisi için: "gnhf iterasyon tabanı ~300k token... **işçi/gnhf koşumları içindir**." Bu, çok-turlu, kendi bağlamını taşıyan, birden fazla araç-çağrısı içeren bir CLI koşumunun (L1 seviyesi) birim maliyeti — promptfoo/İB-07/İB-49 tipi bir matris hücresi ise TEK bir prompt/tek bir Agent çağrısıdır (`cc/rapor-2026-08-31-ib69-a1-arac-promptfoo-optuna.md:7` "her prompt × provider × test kombinasyonu" — tek istek/yanıt). Aynı raporun kendi hook alıntısı (`.claude/hooks/pretool-ajan-fren.sh` başlığı) "ajan/wf p50 12 çağrı" der — yani bir işçi-ajan koşumu ORTALAMA 12 araç-çağrısı yapar; gnhf'nin 300k'lık birimi büyük olasılıkla BUNUN ÜSTÜNDE bir toplam. Eksen-esleme raporu İB-07 örneğinde (§4, 14×60=840 hücre) `T`=300k koyarsa toplam ≈840×300k≈252M token çıkar — bu, gerçek İB-07 koşumunun (45/60 satır, `raporlar/2026-08-30-ib07-description-eval.md`) bilinen ölçeğiyle (tek ajan-fren tavanı 72-144 çağrıda kesiliyor, yani toplam iş birkaç yüz bin-birkaç milyon token mertebesinde, YÜZ MİLYON değil) 2 kat büyüklük mertebesi uyuşmazlığı gösterir. Eksen-esleme raporu bu tutarsızlığı FARK ETMEDEN `T`=gnhf-tabanı kullanıyor (§5, "T = ölçülmüş iç-seviye taban maliyeti (gnhf: 300k...)" ifadesi hiçbir yerde "hücre tek-Agent-çağrısıysa T çok daha küçüktür" uyarısı taşımıyor).

**GÜCÜ:** ÖLDÜRÜCÜ — şemanın "zorunlu alan" ilan ettiği maliyet formülü, taban rakamının hangi birim için ölçüldüğünü karıştırıyor; formül doğru (`toplam≈|dış|×M_dış+|dış|×|iç|×T`) ama `T` yanlış kaynaktan alınırsa sonuç 1-2 mertebe yanlış çıkar.

**ONARIM:** `T` iki ayrı sabit olarak ayrılmalı: `T_gnhf` (~300k, çok-turlu CLI koşumu) ve `T_agent` (tek Agent/Task çağrısı, ölçülmesi gereken YENİ bir sayı — hook başlığındaki "p50 12 çağrı" ipucundan tahmin edilebilir ama BAĞIMSIZ ölçülmeli); şema maddesi hangi hücre-tipi için hangi sabitin kullanılacağını AÇIKÇA seçtirmeli.

---

## Çürütme 3 — SH/Hyperband "erken-durdurma" için LLM matrisinde ara-değer (intermediate value) hiç tanımlanmadı

**HEDEF İDDİA:** `cc/rapor-2026-08-31-ib69-a1-eksen-esleme.md:39` — "ELENEBILIR(X) ↔ (∃ kısmi_skor: hücreler(X) SIRALANABİLİR) ∧ (dusuk_performans_alt_kume(X) ATILABILIR)" ve §5'te SH indirim formülü (`|iç|×η/(η-1)`) matris maliyetine doğrudan uygulanabilir gibi sunuluyor.

**KIRILMA:** Optuna'nın `SuccessiveHalvingPruner`i (`cc/rapor-2026-08-31-ib69-a1-arac-promptfoo-optuna.md:38`) `trial.report(intermediate_value, step)` gerektirir — yani bir eğitim döngüsünün ORTASINDA okunabilir bir kısmi-performans sinyali (epoch başına val-loss). Tek-atış bir LLM tamamlanması (bir prompt → bir yanıt) için böyle bir ara-adım YOK: yanıt ya tamamlanmıştır ya değildir, "yarı-tamamlanmış yanıtın kalite skoru" tanımsız bir kavramdır (streaming token'ların yarısını okuyup skor vermek anlamsızdır). `∃ kısmi_skor` öncülü LLM-matris hücresi için hiçbir raporda SOMUTLANMADI — literatür raporu bile (§3) SH'yi yalnız ML-hiperparametre bağlamında tanımlıyor, LLM-tek-atış bağlamına aktarımını hiç sınamıyor. Eksen-esleme raporunun kendisi §3'te bunu KISMEN fark ediyor ("SH kullanılan matris GERÇEK NESTED-LOOP DEĞİLDİR... masaya gitmeli") ama §5'teki indirim formülünü YİNE DE "mümkündür" diye sunmaya devam ediyor — iki bölüm arasında çelişki var: §3 SH-matris eşlemesini geçersiz ilan ediyor, §5 aynı SH'nin maliyet indirimini sanki geçerliymiş gibi hesaplıyor.

**GÜCÜ:** ÖLDÜRÜCÜ (SH'nin LLM-matrise DOĞRUDAN uygulanabilirliği için) / SINIRLAYICI (rapor kendi içinde bunu kısmen itiraf ediyor, ama tutarsızlığı çözmüyor).

**ONARIM:** LLM matrisinde "ara-değer" ancak proxy-skor (ucuz/hızlı bir ön-tarama modeli ya da kural-tabanlı örneklem — İB-65/66'daki "V26 kural-tabanlı örneklem" emsali `cc/rapor-2026-08-31-ib69-a1-ic-emsal.md:11`) ile YENİDEN TANIMLANMALI; SH'nin klasik "epoch-ortası val-loss" sinyali yerine "ucuz-proxy-skor → pahalı-tam-değerlendirme" iki-kademeli (tam SH değil, basit eşik-filtreleme) modeli önerilmeli, formül (`η/(η-1)`) düşürülmeli çünkü rung/bracket mekanizması yok.

---

## Çürütme 4 — Ortak jsonl şeması: hücre kimliği/idempotency anahtarı VAR SAYILIYOR ama alan olarak zorunlu kılınmadı

**HEDEF İDDİA:** `cc/rapor-2026-08-31-ib69-a1-ic-emsal.md:26-36` önerilen şema: `kosum_id, ts, git_head, eksen_degerleri, tekrar, sonuc, model, toplama_yontemi, kosum_durumu`.

**KIRILMA:** Aynı raporun §4'ü (satır 38-42) tam olarak bunun EKSİKLİĞİNİ İB-07 vakasıyla gösteriyor: "eksen kombinasyonlarının TAM KÜMESİ... hiçbir yerde deklaratif olarak durmuyordu" ve "kütükte her satırın BİRİNCİL ANAHTARI... olması" gerektiğini söylüyor — ama önerilen şema tablosunda (§3) `eksen_degerleri` bir OBJE olarak tanımlı, TEKİL/BİRİNCİL ANAHTAR olarak işaretli değil, ayrıca `kosum_id` "İB-49/denetçi'de yok" diye zaten opsiyonel-fiili. Yani rapor kendi §4 dersini kendi §3 şema tablosuna GERİ TAŞIMIYOR: önerilen şemada `birincil_anahtar` (örn. `hash(eksen_degerleri)` ya da `sorgu_id+tekrar` composite) diye AYRI ve ZORUNLU bir alan yok; `--eksik`/`--resume` modu da "harness'e eklenmeli" deniyor ama şemaya alan olarak düşmüyor (resume sorgusu için `birincil_anahtar` alanı olmadan "planlanan küme − mevcut = eksik" farkı hesaplanamaz, tam da §4'ün şikayet ettiği İB-07 arızası tekrarlanır).

**GÜCÜ:** SINIRLAYICI — şema önerisi doğru yöne gidiyor ama kendi teşhis ettiği hastalığın ilacını (idempotency/birincil-anahtar alanı) reçeteye yazmıyor.

**ONARIM:** Şemaya `hucre_anahtari` (string, `eksen_degerleri`'nin deterministik serileştirmesinden türetilen hash ya da birleşik-anahtar) ZORUNLU alan olarak eklenmeli; ayrıca AS-OF/model-sürümü (bkz. Çürütme 5) ve token-maliyeti (bkz. Çürütme 2) alanları da eksik.

---

## Çürütme 5 — Ortak şemada model SÜRÜMÜ ve AS-OF/veri-tazeliği ayrımı yok — yalnız "model" adı var

**HEDEF İDDİA:** `cc/rapor-2026-08-31-ib69-a1-ic-emsal.md:32` — `model` alanı "string, evet (zorunlu)... eksik, ortak şemaya zorunlu eklenmeli" diyerek şemaya EKLİYOR ama yalnız model ADINI ekliyor.

**KIRILMA:** CLAUDE.md m.6 "Anakronizm YASAK" ilkesi (bu emrin bağlı olduğu kanon) zaman-bağımlı her iddianın AS-OF damgalı olmasını şart koşuyor; bir LLM matris-koşumunda hücre sonucu MODEL SÜRÜMÜNE (ör. "Sonnet" vs "Sonnet-5", API snapshot tarihi) duyarlıdır — aynı `model: "sonnet"` etiketiyle iki farklı tarihte koşulan hücreler farklı ağırlıklarla üretilmiş olabilir, bu da matrisin "aynı girdi → aynı çıktı" (m.6 deterministik-tasarım) varsayımını SESSİZCE bozar. Önerilen şemada `model` alanı var ama `model_surumu`/`api_snapshot` ya da hücre-bazlı `AS-OF` alanı YOK — yalnız satır-genel `ts` var, bu da "kayıt ne zaman yazıldı" bilgisidir, "model hangi sürümdü" bilgisi değildir.

**GÜCÜ:** SINIRLAYICI — kanonun kendi m.6/m.29 ilkesiyle doğrudan çelişen bir eksiklik, ama kolay onarılır.

**ONARIM:** Şemaya `model_surumu` (API-tarihli snapshot id, örn. `claude-sonnet-4-5-20250929` deseni) ayrı zorunlu alan olarak eklenmeli; `model` adı tek başına sürüm-kimliği taşımaz.

---

## Çürütme 6 — Kaynak denetimi: literatür raporunda DESTEKLİ etiketli ama açılmamış URL var

**HEDEF İDDİA:** `cc/rapor-2026-08-31-ib69-a1-literatur.md:23` (successive halving tanımı) — "[DESTEKLİ: WebSearch özeti, medium.com/@vireshj kaynağı — '...' — AS-OF 2026-08-31; **URL bu oturumda WebFetch ile açılmadı, yalnız WebSearch snippet'i**, bu yüzden [?] işaretiyle sınırlı güven]".

**KIRILMA:** Bu tek cümle içinde ETİKET ÇELİŞKİSİ var: başta "[DESTEKLİ: ...]" yazıyor ama cümlenin kendisi "URL açılmadı, [?] işaretiyle sınırlı güven" diyor. Raporun kendi kaynak-listesi tablosu (§ Kaynak listesi, satır "WebSearch özeti — medium.com/@vireshj") bunu doğru şekilde "HAYIR (yalnız arama snippet'i)" olarak işaretliyor — yani METİN İÇİ etiket (DESTEKLİ) ile TABLO etiketi (HAYIR/açılmadı) TUTARSIZ. Bir okuyucu yalnız metin gövdesini tarayıp "DESTEKLİ" etiketine güvenirse (rapor formatının vaadi budur: "DESTEKLİ = doğrulandı"), açılmamış bir ikincil-kaynak snippet'ini birincil-kaynak gibi okur.

**GÜCÜ:** ZAYIF (tekil, kendi içinde düzeltici parantez taşıyor, tablo doğru) — ama görev emrindeki "6. Kaynak denetimi" maddesinin TAM olarak aradığı sınıf hata.

**ONARIM:** Etiket sözlüğüne üçüncü bir durum eklenmeli: `[DESTEKLİ-İKİNCİL: yalnız arama-snippet'i, birincil kaynak açılmadı]` — mevcut ikili (DESTEKLİ / [?]) SH tanımı gibi "kısmen doğrulanmış" durumları zorla DESTEKLİ'ye düşürüyor.

---

## SAĞLAM KALDI (çürütülemeyen iddialar)

1. **PK-10 dosya-çakışması önceliği** (`cc/rapor-2026-08-31-ib69-a1-eksen-esleme.md` §2, "(iv) en üstte") — `tools/paralel-kapi.py:113` kodunda fiilen uygulanan bir kural olarak doğrudan doğrulandı; verimlilik tercihinin güvenlik kısıtını geçemeyeceği gerekçesi sağlam, alternatif bir kırılma bulunamadı.

2. **İB-07 eksen-eşleme sonucu (skill DIŞ, sorgu×tekrar İÇ)** (`...eksen-esleme.md` §4) — 4 ölçütle çapraz test edilmiş, `veri/description-eval.jsonl` şemasıyla (append-only, çakışmasız) tutarlı; kırılma noktası aranmasına rağmen bulunamadı — tek zayıflık (ajan-freni kesintisinin eksen-sırasından bağımsız olduğu tespiti) raporun KENDİSİ tarafından zaten [?] olarak işaretlenmiş, yani rapor kendi sınırını biliyor.

3. **Toplam maliyetin eksen-sırasından bağımsızlığı** (`toplam ≈ |X|×|Y|×T`, eksen-esleme §5) — çarpma işleminin değişme özelliği matematiksel olarak trivial-doğru; yalnız KURULUM maliyetinin dış/iç seçimine duyarlı olduğu iddiası da doğru ve İB-66 çarpım kuralıyla tutarlı (bkz. Çürütme 2 — burada kırılan `T`'nin SAYISAL DEĞERİ, formülün KENDİSİ değil).

4. **Hyperband birincil-kaynak alıntısı** (`cc/rapor-2026-08-31-ib69-a1-literatur.md` §3, arxiv 1603.06560) — URL fiilen açılmış (WebFetch EVET), alıntı birebir ("over an order-of-magnitude speedup", "adaptive resource allocation and early-stopping") kaynakla eşleşiyor; bu tekil iddia için kırılma bulunamadı.

## Özet dağılım
6 çürütme: 2 ÖLDÜRÜCÜ (Çürütme 2 maliyet-tabanı karışıklığı, Çürütme 3 SH-ara-değer yokluğu) · 3 SINIRLAYICI (Çürütme 1 toplama ön-koşulu, Çürütme 4 idempotency-anahtarı eksik, Çürütme 5 model-sürümü eksik) · 1 ZAYIF (Çürütme 6 etiket tutarsızlığı). 4 iddia SAĞLAM KALDI.
