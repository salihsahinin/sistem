# İB-69 / AİLE-1 — MATRİS-KOŞUM ŞEMASI v0 (formalizasyon + emsal)

**Künye:** emir `cc/gorev-2026-08-31-ib69-matris-kosum-atlas.md` · HEAD `fed8b31` (`git rev-parse --short HEAD`, koşum anı) · **AS-OF 2026-08-31** · zincir m.40b v0.2 (5 tez → antitez → V26 → maskeli hakem → sentez) · **8 Agent çağrısı** (7 işçi Sonnet-5 `[rejim: maliyet-öncelikli]`, 1 hakem Opus-5) · aile-başına ajan tavanı 10, aşılmadı · **AİLE-2 KOŞULMADI** (ayrı sıralı birim).

## DÜZELTME NOTU (Karar 86 D7-⑦, 2026-09-02 — aile-2 hakem bulguları; m.8: satır silinmedi)

Aile-2 raporu (`raporlar/2026-08-31-ib69-matris-a2-kurallastirma.md` §6.1, satır 259-265) bu şemaya dört şerh düşmüştür. Satırdaki asıl metin DEĞİŞTİRİLMEDİ; aşağıdaki dört madde ayrı şerhtir, üstteki tanımların yerine geçmez:

1. **§4 `T_gnhf ≈ 300k` damgası** (bu belgede satır 116) — "**ÖLÇÜLDÜ**" YANLIŞ damga. Doğrusu: "**TÜRETİLDİ, ÖLÇÜLMEDİ**" — kaynak 2 iterasyonun TOPLAMINI (535k) ölçtü, 535k ÷ 2 = 267,5k; "~300k" bu değerden **%12,1 yukarı yuvarlanmıştır**; n=2, tek vaka. Kaynak: `raporlar/2026-08-31-k010-a3-loop-1.md:12`, aile-2 §6.1 madde 1.
2. **§4'e (bu belgede satır 110-144) F-1 eklenmeli** — çağrı maliyeti toplamsaldır: çarpan **1,00** + sabit oturum tabanı **27** (n=1); KAPI-2'nin doğru sınırı **≤143**'tür (hook `n >= 144`'te bloke eder). Aile-2 §6.1 madde 2.
3. **§6.1 Ö-A'ya (bu belgede satır 181) kapsam şerhi** — matris-İÇİ hücrelerin ortak append-only kütüğe yazması Ö-A'nın (PK-10 AYAK İZİ) kapsamı DIŞINDADIR (paralel-kapı birim-ARASI çalışır, hücre-arası değil); POSIX kısa-satır append atomikliği VARSAYILDI, doğrulanmadı `[?]`. Aile-2 §6.1 madde 3.
4. **§2'ye (bu belgede satır 75-77) açıklık** — `cikti.tip = sema` durumunda deterministik toplama (T1-T5) YALNIZ enum/sayı alt-alanları üzerinde tanımlıdır; serbest-metin alt-alanları (örn. İB-67'nin `en_yakin_komsu`, `kanit_url`'ü) kütükte taşınır ama T1-T5'e GİRMEZ. Aile-2 §6.1 madde 4.

---

**Kapsam beyanı:** bu belge TASARIMDIR. Prototip inşa edilmedi, hiçbir matris koşulmadı, K-020 kararı VERİLMEDİ (bu rapor K-020'nin girdisidir, hüküm masada). Kanon dosyalarına (`core/`, `CLAUDE.md`, `kuyruk/`, `tools/`) dokunulmadı.

**Ham işçi raporları:**
- `cc/rapor-2026-08-31-ib69-a1-literatur.md` — (a) DOE / faktöriyel / parameter sweep
- `cc/rapor-2026-08-31-ib69-a1-arac-promptfoo-optuna.md` — (b1) promptfoo · Optuna
- `cc/rapor-2026-08-31-ib69-a1-arac-sweep-harness-temporal.md` — (b2) W&B Sweeps · lm-eval-harness · Temporal
- `cc/rapor-2026-08-31-ib69-a1-ic-emsal.md` — (c) iç emsaller (web'siz)
- `cc/rapor-2026-08-31-ib69-a1-eksen-esleme.md` — (d) nested-loop eksen eşlemesi
- `cc/rapor-2026-08-31-ib69-a1-antitez.md` · `cc/rapor-2026-08-31-ib69-a1-v26-ornekleme.md` · `cc/rapor-2026-08-31-ib69-a1-hakem.md`

---

## 0. Sorunun cevabı, tek paragraf

Salih'in gözlemi ("2x nested loop, 2 farklı sınıf prompt-değişkeniyle LLM çıktılarından matris — Python'da iki değişkenli nested loop'un sayı matrisi üretmesi gibi") literatürde **tam faktöriyel deney tasarımı** (full factorial design / DOE) ve mühendislikte **parameter sweep / grid sweep** adıyla çözülmüş bir sınıftır: eksen = faktör (factor), eksen değeri = seviye (level), hücre = koşu (run), aynı hücrenin yinelenmesi = tekrar (replicate); toplam koşu sayısı `∏|faktör_i| × tekrar` [DESTEKLİ: help.reliasoft.com/reference/experiment_design_and_analysis/doe/general_full_factorial_designs.html, AS-OF 2026-08-31]. Dışarıda dört araç sınıfı bunu deklaratif olarak çözmüş: **promptfoo** (`prompts × providers × tests` çarpımı, YAML), **Optuna** (`GridSampler` ile tam tarama + budayıcılar), **W&B Sweeps** (`method: grid` + `parameters` + `early_terminate`), **lm-evaluation-harness** (`--model × --tasks × --num_fewshot`, `--log_samples` ile hücre-başına jsonl), dayanıklı fan-out tarafında **Temporal** (child workflow + gather). Jarvis'te desen zaten üç kez FİİLEN koştu (İB-07 20×3 grid, İB-49 4 kol × N=5, atlas aile×şerit matrisi) — yani icat edilecek bir şey yok, **eksik olan tek şey ortak şemadır**. Bu belge o şemayı v0 olarak yazar. Kritik iki düzeltme hakemden geldi: (A) emrin `~300k` maliyet tabanı matris hücresi için YANLIŞ tabandır, model iki-tabanlı olmalıdır; (B) klasik successive halving tek-atış LLM hücresine UYGULANAMAZ, indirim yalnız deterministik kademe-filtresinden gelir.

---

## 1. ZORUNLU ALAN 1 — EKSEN TANIMI (değişken-sınıfı: tip + değer kümesi)

Eksenler koşum script'inin içine gömülmez; **ayrı deklaratif sözleşme dosyasında** durur (üç açılmış araç emsalinin üçü de böyle yapıyor: promptfoo `promptfooconfig.yaml`, Optuna `search_space` sözlüğü, W&B `sweep.yaml`). Öneri yol: `veri/sozlesme/<is>-eksen.json`.

```
EKSEN := {
  ad              : string                       [zorunlu; kütükte alan adı olur]
  tip             : enum{kategorik, sirali, sayisal_ayrik}   [zorunlu]
  degerler        : liste<atom>                  [zorunlu; TAM küme — kardinalite buradan sayılır,
                                                  metinden değil; resume farkı buradan hesaplanır]
  rol             : enum{dis, ic}                [zorunlu; seçim ölçütü §6]
  kaynak          : string                       [değerlerin nereden geldiği: dosya ∨ emir ∨ sabit]
}
MATRIS := {
  eksenler        : liste<EKSEN>  ∧  |eksenler| ≥ 2
  tekrar          : int ≥ 1                      [aynı hücrenin yinelenmesi; DOE "replicate"]
  erken_durdurma  : enum{yok, kademe_esigi}      [zorunlu bayrak — §5/§6 HÜKÜM 3]
  hucre_tipi      : enum{tek_cagri, gnhf_iterasyonu}         [zorunlu; maliyet tabanını seçer]
}
Ö1 (tamlık):  ∀e ∈ eksenler ( |e.degerler| ≥ 1 ) ∧ (∃e: e.rol = dis) ∧ (∃e: e.rol = ic)
Ö2 (yalanlanabilirlik): planlanan hücre kümesi = ∏(e.degerler) × tekrar — DOSYADAN türetilir,
      emir metnindeki düz yazıdan DEĞİL   [İB-07 dersi: 20×3×14 metni kütükten sorgulanamadı]
```

**Sık yapılan hata (hakem #20 tespiti):** İB-07'de "20 sorgu × 3 tekrar × **14 skill**" denmişti; gerçekte 14 skill koşum ekseni DEĞİL, `altin_etiket` **etiket uzayıdır** — matris 20×3 = **60 hücredir**, 840 değil. Eksen ile etiket-uzayı ayrımı Ö1'in denetlediği şeydir.

**Dış kaynak emsalleri (hepsi AS-OF 2026-08-31, WebFetch ile açıldı):**
| Araç | Eksen ifadesi | Dayanak |
|---|---|---|
| promptfoo | `prompts` × `providers` × `tests`, `{{var}}` Nunjucks enjeksiyonu, `defaultTest` | promptfoo.dev/docs/configuration/guide/ [DESTEKLİ] |
| Optuna | `GridSampler(search_space={param: [degerler]})`; küme tükenince çalışma durur | optuna.readthedocs.io/…/samplers/generated/optuna.samplers.GridSampler.html [DESTEKLİ] |
| W&B Sweeps | `method: grid` + `parameters: {p: {values: [...]}}` + `metric: {name, goal}` | docs.wandb.ai/guides/sweeps/define-sweep-configuration/ [DESTEKLİ] |
| lm-eval-harness | `--model` × `--tasks` × `--num_fewshot` | github.com/EleutherAI/lm-evaluation-harness [DESTEKLİ] |

---

## 2. ZORUNLU ALAN 2 — HÜCRE SÖZLEŞMESİ (girdi → çıktı TİPİ)

Salih'in sezgisi — *"döngü sayı döndürüyorsa matris"* — burada tipli alana bağlanır: **matris olma şartı, hücrenin TİPLİ bir değer döndürmesidir.** Serbest metin döndüren döngü matris üretmez, transkript üretir; ortalanamayan/karşılaştırılamayan çıktı satır-sütun özetine girmez (antitez çürütmesi #1, hakem SINIRLAYICI → şemaya kısıt olarak alındı).

```
HUCRE := {
  hucre_anahtari  : string   [ZORUNLU, TEKİL — eksen değerlerinin + tekrar'ın deterministik
                              serileştirmesi, örn. "sorgu=q07|tekrar=3"; idempotency ∧ resume
                              ∧ yinelenen-koşum tespiti bu tek alandan çıkar]
  hucre_tipi      : enum{tek_cagri, gnhf_iterasyonu}
  girdi           : {sablon_id, eksen_degerleri}   [aynı şablon, yalnız değişkenler değişir]
  cikti           : ÇIKTI_TİPİ
}
ÇIKTI_TİPİ ∈ {
  etiket   : kapalı küme (enum) — ör. İB-07 `secilen_skill` ∈ {14 skill} ∪ {HİÇBİRİ}
  sayi     : reel ∨ tam — ör. İB-49 `precision`, `recall`, `dogruluk`, `derleme_kodu`
  sema     : anahtarları önceden sabit obje — ör. {hukum: D|K|X, gerekce_sha}
                 > ⚠ DÜZELTME NOTU'na bak (madde 4)
}
Ö1 (tiplilik):  cikti.tip ∈ {etiket, sayi, sema}   ∧  ¬(cikti.tip = serbest_metin)
      ¬Ö1  →  bu bir MATRİS DEĞİLDİR; toplama LLM-yargıç gerektirir → §3 İSTİSNA dalı
Ö2 (kapalılık): cikti.tip = etiket → değer kümesi eksende ∨ sözleşmede AÇIKÇA yazılı
Ö3 (idempotency): aynı hucre_anahtari ile ikinci satır → yeni koşum DEĞİL, çakışma olayı
```

**Emsal kanıtı:** İB-07 hücresi tek alan döndürüyor (`secilen_skill`) ve harness `isabet`i deterministik hesaplıyor (`veri/description-eval.jsonl:1`); İB-49 hücresi tamamen sayısal ve harness LLM hiç çağırmıyor (`tools/d2-eval.py:1-4` docstring, `:110-113`). Atlas aile×şerit matrisi ise etiketli (D/K/X) ama **kütüğe hiç inmiyor** — rapor-gömülü tablo kalıyor; v0 şemasının kapattığı boşluk tam da budur.

---

## 3. ZORUNLU ALAN 3 — TOPLAMA / İNDİRGEME (LLM'siz DETERMİNİSTİK, Karar 65)

**Kural:** toplama, hücre koşumundan **AYRI bir adımdır** ve asla aynı çağrı içinde yapılmaz. Girdi = bronz jsonl kütük, çıktı = gold görünüm (`veri/gorunum/`). Hesap yalnız sayım / oran / marjinal ortalama / etkileşim farkıdır — aynı kütükten her koşumda aynı sayı çıkar (m.6 deterministik tasarım).

```
TOPLAMA (yalnız bu beş işlem):
  T1 satır özeti     : ∀a ∈ A: agg({h(a,b) : b ∈ B})           [DOE: A'nın ana etkisi]
  T2 sütun özeti     : ∀b ∈ B: agg({h(a,b) : a ∈ A})           [DOE: B'nin ana etkisi]
  T3 etkileşim       : h(a,b) − (satir_ort(a) + sutun_ort(b) − genel_ort)
  T4 tekrar varyansı : aynı hucre_anahtari'nın tekrarları arası yayılım [LLM örnekleme gürültüsü]
  T5 kapsama         : |yazılan hücre| / |planlanan hücre|      [kısmi-koşum göstergesi]
agg ∈ {sayim, oran, ortalama, medyan, cogunluk_oyu}   — hepsi LLM'siz.

KARAR 65 KOŞULLU FORMU (hakem tavsiyesi, şemaya bu haliyle girer):
  LLM'siz_toplama  ⟺  hücre_sözleşmesi_çıktıyı_tiplendiriyor        (§2 Ö1)
  ¬(§2 Ö1)  →  İSTİSNA DALI: LLM-yargıç AYRI bir hücre_tipi olarak beyan edilir,
               kendi maliyeti kütüğe yazılır, sonucu "deterministik" SAYILMAZ.
```

**Kırılan varsayım (literatür → LLM eşlemesi, açık beyan):** klasik DOE ana-etki/etkileşim hesabı skaler yanıt ve toplanabilirlik (additivity) varsayar; LLM hücresinde çıktı etiket olduğunda T3 (etkileşim) ancak orana çevrildikten sonra anlamlıdır, ham etiket üzerinde tanımsızdır. Ayrıca gürültü kaynağı ölçüm hatası değil **örnekleme/decoding rastgeleliğidir** — bu yüzden T4 (tekrar varyansı) opsiyonel değil, matrisin sağlık göstergesidir.

---

> ⚠ DÜZELTME NOTU'na bak (madde 2)

## 4. ZORUNLU ALAN 4 — MALİYET MODELİ (iki tabanlı + iki kapılı)

**HAKEM HÜKMÜ (A):** Emrin `~300k iterasyon tabanı (önbellek-okumalı gnhf birimi, 08-30 e2e715)` sabiti **matris hücresi için yanlış tabandır**. İB-66'nın kendi metni tabanı kapsamla sınırlıyor — taban "işçi/gnhf koşumları içindir" (`raporlar/2026-08-31-ib66-gozlemlenebilir-nested-loop-atlas.md:132`) ve o birim aynı raporun `:187` satırında **L1 = çok-turlu gnhf CLI iterasyonudur**. Matris hücresi ise üç iç emsalin üçünde de tek istek/yanıt ya da tek Agent çağrısıdır. Aynı sabiti iki farklı birime koymak ölçümün kapsam beyanını ihlal eder (m.29).

```
TANIM
  > ⚠ DÜZELTME NOTU'na bak (madde 1)
  T_gnhf  = 300k    [ÖLÇÜLDÜ, önbellek-okuma DAHİL; İB-66:132 · vaka e2e715, 08-30]
                    [?] ham ölçüm satırı `raporlar/2026-08-31-k010-a3-loop-1.md:12-13`
                        bu koşumda AÇILMADI — teyit borcu
  T_hucre = tek_cagri birim maliyeti                → **ÖLÇÜLMEDİ** (borç M-1)
  M_dis   = dış eksen değeri başına kurulum (bağlam/skill yükleme, önbellek yazımı)
  T       = (hucre_tipi = gnhf_iterasyonu) ? T_gnhf : T_hucre

KAPI 1 — TOKEN BÜTÇESİ
  toplam ≈ |dis| × M_dis  +  |dis| × |ic| × tekrar × T
  Ö1: toplam ≤ 0,8 × B_oturum  →  koşuma izin ver     [İB-66 §5.3 Şablon-1 biçimiyle aynı]
  ¬Ö1 → koşma; |ic| ∨ tekrar küçült ∨ Salih'e bildir

KAPI 2 — ÇAĞRI BÜTÇESİ  (token'dan BAĞIMSIZ; İB-07'yi kesen kapı BUDUR)
  N_cagri = |dis| × |ic| × tekrar
  Ö2: N_cagri + sayac_oturum ≤ DURDUR
      [`.claude/hooks/pretool-ajan-fren.sh:36-37,52` — sayaç OTURUM-genelinde kümülatif,
       güncel varsayılan DURDUR=144 / UYARI=72; İB-07'nin andığı "72=DUR" ESKİ eşik]
  ¬Ö2 → matrisi oturuma BÖL (kütük append-only + hucre_anahtari ile resume)

ERKEN-DURDURMA İNDİRİMİ (yalnız erken_durdurma = kademe_esigi ise; §5)
  toplam = N × T_ucuz  +  k × T_pahali ,  k = |{hücre : proxy_skor ≥ eşik}|
  eşik SABİT ∧ önceden yazılı  →  aynı girdi aynı k  (deterministik, bandit DEĞİL)

ÖLÇÜM BORCU M-1: ilk gerçek matris koşumunda her satır token_giris / token_cikis /
  token_onbellek_okuma / sure_ms yazar; T_hucre bu kütükten TÜRETİLİR, TAHMİNLE DOLDURULMAZ.
```

**Sayısal dayanak durumu:** İB-07'nin gerçek hücre maliyeti **ölçülmedi** — `raporlar/2026-08-30-ib07-description-eval.md:48-53` yalnız çağrı sayısı veriyor (51 işçi denemesi = 45 başarılı + 6 hook-reddi; lider ~65 kendi çağrısı), token/süre rakamı yok. Bu yüzden v0'da `T_hucre` sayısal değer taşımaz, borç taşır. Tek-tabanlı model REDDEDİLDİ: ya gnhf'yi hafife alır ya tek-çağrı hücresini 1-2 mertebe abartır ve asıl bağlayıcı kısıtı (çağrı sayacı) tamamen ıskalar.

---

## 5. ZORUNLU ALAN 5 — KÜTÜK STANDARDI (hücre → jsonl satırı, İB-49 harness deseni)

Tek dosya, **append-only**, satır = bir hücre koşumu. Üç iç emsalin alanlarının birleşimi + hakemin eklediği üç zorunlu alan:

| alan | tip | zorunlu | kaynağı / gerekçe |
|---|---|---|---|
| `hucre_anahtari` | string | **evet** | YENİ (hakem) — tekil anahtar; idempotency ∧ resume ∧ çakışma tespiti |
| `kosum_id` | string | evet | İB-07 (`veri/description-eval.jsonl:1`) |
| `ts` | ISO8601 | evet | üçünde de var |
| `git_head` | string (kısa sha) | evet | `tools/d2-eval.py:50`, `tools/denetci-kalibrasyon.py:76` — İB-07'de satır düzeyinde YOKTU |
| `eksen_degerleri` | obje `{eksen_ad: deger}` | evet | genelleme (İB-07 düz alanlar; d2-eval `kol,kosum,dosya`) |
| `tekrar` | int | evet | İB-07 |
| `hucre_tipi` | enum{tek_cagri, gnhf_iterasyonu} | **evet** | YENİ (hakem) — maliyet tabanını seçer |
| `model` | string | evet | **TAM API snapshot id** — kısa ad YASAK; İB-07 zaten doğru yapıyor: `claude-haiku-4-5-20251001` |
| `sonuc` | obje `{tip, deger}` | evet | üç emsalin farklı iç şemalarının genellemesi |
| `toplama_yontemi` | enum{llm, deterministik} | evet | YENİ — hiçbir emsalde satır düzeyinde yok, harness kendini belgeler |
| `token_giris` / `token_cikis` / `token_onbellek_okuma` / `sure_ms` | int | evet (M-1) | YENİ — `T_hucre` bu alanlardan türetilecek |
| `kosum_durumu` | enum{tam, kismi, planli} | evet | manifest'te var (`veri/manifest/ib-07-description-eval.json:5`), satırda yoktu |

```
RESUME KURALI (tek sorguyla çıkmalı — İB-07'de ELLE yapıldı, ders budur):
  kalan_is = manifest_anahtarlar  −  kütük_anahtarlar
  ∀ kesinti ( kütük append-only ∧ hucre_anahtari tekil → veri kaybı = ∅ ∧ kalan_is hesaplanabilir )
```
**Dış emsal:** lm-evaluation-harness `--log_samples` + `--output_path` ile hücre-başına örnek kaydı yazıyor [DESTEKLİ: github.com/EleutherAI/lm-evaluation-harness, AS-OF 2026-08-31] — per-sample jsonl'in tam alan şeması bu koşumda doğrulanamadı `[?]`.

---

## 6. (d) NESTED-LOOP EKSEN EŞLEMESİ — hangi eksen dış, hangisi iç

### 6.1 Dört ölçüt (m.38 formunda) + öncelik sırası

> ⚠ DÜZELTME NOTU'na bak (madde 3, Ö-A kapsam şerhi)

| # | Ölçüt | Karar yüklemi | Ölçülebilir tanım |
|---|---|---|---|
| Ö-A | **PK-10 AYAK İZİ** | `YAZAR_CAKISMASI(X) → X SIRALI` | aynı dosyaya yazan hücreler aynı turda paralel olamaz (`tools/paralel-kapi.py:113`: büyüyen ayak-izi → varsayılan SIRALI) |
| Ö-B | **BAĞIMSIZLIK** | `DIS(X) ↔ BAGIMSIZ(X) ∧ ¬BAGIMSIZ(Y)` | hücre sonucu başka hücrenin sonucunu okumuyorsa bağımsız (Bernstein koşulu) |
| Ö-C | **MALİYET / yeniden-kullanım** | `DIS(X) ↔ kurulum_paylasilir(X,Y) ∧ ¬kurulum_paylasilir(Y,X)` | X sabitlenince pahalı kurulum (bağlam yükleme, önbellek yazımı) iç eksen boyunca paylaşılıyor mu — `M_dis` bu eksende bir kez ödenir |
| Ö-D | **ERKEN-DURDURMA** | ölçüt DEĞİL → `kademe` bayrağı | §6.3 hükmü: dış/iç ikilisine gizlenmez, ayrı üçüncü sayaç |

**Çatışmada öncelik: Ö-A > Ö-B > Ö-C > (Ö-D düşürüldü).** Gerekçe: PK-10 ve bağımsızlık **yapısal/doğruluk** kısıtlarıdır (ihlali yanlış sonuç ya da bozuk dosya üretir); maliyet bir **verimlilik** tercihidir (ihlali pahalı ama doğru koşum verir); erken-durdurma ise ölçüt olmaktan çıkarıldı çünkü eksen rolü değil, ayrı bir bayrak.

### 6.2 Somut eşleme: İB-07 vakası
Matris 20 sorgu × 3 tekrar = 60 hücre (14 skill = etiket uzayı, eksen değil). Ö-A nötr (tek append-only kütük, çakışma yok) · Ö-B nötr (tüm hücreler bağımsız) · **Ö-C karar veriyor:** sorgu ekseni dış olursa aynı 14-skill listesi metni iç eksen boyunca yeniden kullanılır → **sorgu DIŞ, tekrar İÇ**. **Ama kesintiyi bu önlemezdi:** İB-07'yi kesen kısıt token değil **oturum-kümülatif ajan sayacıydı** ve `N_cagri = 60` eksen sırasından bağımsızdır. Doğru fren §4 KAPI 2'dir — hiçbir tez raporu bunu maliyet modeline koymamıştı.

### 6.3 İB-66 §5 uyum denetimi — "matris = 2 seviye" KOŞULLU
```
matris_2_seviye ↔ (her eksenin kendi sayacı) ∧ (her eksenin kendi durma yüklemi)
                  ∧ (∀ dış değeri: iç eksen TAM koşulur)      [İB-66 §5.1 (i)∧(ii)∧(iii)]

tam_faktoriyel ∧ ¬erken_durdurma  →  matris = 2 SEVİYE                       [D]
kademe_esigi ∨ budama             →  (iii) TAM KAPSAMA KIRILIR → 2 seviye DEĞİL:
    üçüncü sayaç (kademe) + BÜZÜLEN aday kümesi; İB-66 §5.2'nin hiçbir sınıfına
    girmiyor → YENİ ALT-TÜR → MASAYA (İB-65 S1 md.1.6 emsali)
```
**HAKEM HÜKMÜ (B):** klasik successive halving tek-atış LLM eval matrisine **UYGULANAMAZ**. Optuna'nın kendi dokümanı budamayı `trial.report(intermediate_value, step)` + `should_prune()` ile tanımlıyor [DESTEKLİ: optuna.readthedocs.io/…/SuccessiveHalvingPruner.html, AS-OF 2026-08-31; V26 bağımsız doğruladı] — tek-atış bir tamamlamada "adım" yoktur, yarım yanıtın kalite skoru tanımsızdır. `η/(η−1)` indirim formülü şemadan **ÇIKARILDI**. İndirim yalnız §4'teki iki kademeli deterministik eşik-filtresinden gelir (ucuz proxy tüm hücreleri, pahalı kademe yalnız eşiği geçenleri koşar) — bu bandit değil, m.6 ile uyumlu.

---

## 7. Birincil kaynaklar (AS-OF 2026-08-31) — 9 açıldı

| # | URL | WebFetch AÇILDI | Ne için |
|---|---|---|---|
| 1 | help.reliasoft.com/reference/experiment_design_and_analysis/doe/general_full_factorial_designs.html | **EVET** | faktör/seviye/koşu/tekrar tanımı; `Runs = ∏|faktör|` |
| 2 | arxiv.org/abs/1603.06560 (Hyperband, Li et al.) | **EVET** | bandit-tabanlı erken durdurma |
| 3 | promptfoo.dev/docs/configuration/guide/ | **EVET** | prompts×providers×tests matrisi, `{{var}}`, `defaultTest` |
| 4 | optuna.readthedocs.io/en/stable/reference/samplers/index.html | **EVET** | sampler ailesi |
| 5 | optuna.readthedocs.io/…/generated/optuna.pruners.SuccessiveHalvingPruner.html | **EVET** | rung/bracket, `min_resource`, `reduction_factor`; budama tetiği |
| 6 | optuna.readthedocs.io/…/samplers/generated/optuna.samplers.GridSampler.html | **EVET** | `search_space` tam faktöriyel + tükenme davranışı |
| 7 | docs.wandb.ai/guides/sweeps/define-sweep-configuration/ | **EVET** | `method`, `parameters`, `metric`, `early_terminate: hyperband` |
| 8 | github.com/EleutherAI/lm-evaluation-harness | **EVET** | `--model/--tasks/--num_fewshot`, `--log_samples`, `--output_path` |
| 9 | docs.temporal.io/develop/typescript/child-workflows | **EVET** | `executeChild` + `Promise.all` fan-out/gather, determinizm, `workflowId` idempotency |

**Açılmadı → `[?]`, DESTEKLİ damgası YOK:** Bergstra&Bengio 2012 (random search) · NIST e-Handbook (fractional factorial, ana-etki/etkileşim) · Optuna Study/Trial RDB şeması · HyperbandPruner/MedianPruner sayfaları · W&B agent/controller fan-out sayfası · lm-eval per-sample jsonl alan şeması · Temporal concurrency limiti/retry policy · `raporlar/2026-08-31-k010-a3-loop-1.md:12-13` (300k ham ölçüm kaydı).

---

## 8. Zincir sonucu ve açık uçlar

**Hakem D/K/X:** 26 iddia — **D=15 · K=4 · X=7**. Maske çalıştı: hem tezin hem antitezin aynı aritmetik hatası (İB-07 matris boyu) ayrı ayrı X aldı.
**V26 ihlali: 1** — `cc/rapor-2026-08-31-ib69-a1-literatur.md:22` successive-halving tanımı DESTEKLİ damgalı ama URL'si hiç açılmamış (yalnız WebSearch snippet'i). Denetlenen 4 iddiadan 3'ü DOĞRULANDI.
**Şemadan çıkarılanlar:** `η/(η−1)` SH indirim formülü (X) · tek-tabanlı maliyet modeli (X) · erken-durdurmanın eksen-seçim ölçütü olması (düşürüldü).

**AİLE-2'ye devredilen açık uçlar (aile-2 bu şemayı OKUYARAK çalışır):**
1. **M-1 ölçüm borcu** — `T_hucre` ölçülmedi; ilk gerçek matris koşumu bunu üretmeli, pilot tasarımı bu ölçümü zorunlu alan yapmalı.
2. **`kademe_esigi` alt-türü masaya** — kademeli matris İB-66 §5.2'nin hiçbir sınıfına girmiyor; yeni seviye alt-türü kararı Katman-1.
3. **K-020 birleşme kararı** — promptfoo/Optuna hazır mı, kendi harness mı: bu rapor girdi üretti, 3-model karşılaştırması aile-2'de.
4. **Manifest birim tipi** — matris-koşum `tur` alanına ek mi ayrı alan mı (aile-2 kapsamı).
5. **`[?]` 300k teyidi** — `raporlar/2026-08-31-k010-a3-loop-1.md:12-13` açılıp ham ölçüm doğrulanmalı.
6. **Uygun-iş envanteri** — aile-2'nin kendi done-yüklemi (≥10 iş sınıflandırma).
