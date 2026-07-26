# Antitez Turu ve Hakemlik — A22–A32

*Kayıt: 2026-07-26 · Carvis (CC, yan-oturum m.41) · Talep: "antitez aşamasını koşmadıysan koş, tüm ailelerin iddia listelerini sınatmadıysan sınat"*

**Protokol:** m.40b v0.2 Aşama 2. Antitez ajanlarına **yalnız çıplak iddia listesi** verildi — gerekçe, kaynak, rakam ve kanıt etiketleri BİLEREK verilmedi (CoVe-Factored çıpalama freni). Hakemlik Carvis'te; üretici ≠ doğrulayıcı.

> **DURUM:** A22–A24 turu kapandı (§2). A25–A27 · A28–A30 · A31–A32 **koşuyor**. A5–A21 için önce iddia listesi çıkarımı koşuyor (§1.3 sapma kaydı).

---

## 1. TURUN KENDİ SINIRLARI — hükümlerden ÖNCE okunmalı

### 1.1 ⚠️ Antitez ajanı HİÇ ARAÇ ÇAĞIRMADI

`A22-A24 antitez turu → tool_uses = 0`

⇒ Tüm saldırı **modelin kendi eğitim bilgisinden** yapıldı; hiçbir karşı-örnek birincil kaynaktan doğrulanmadı.
⇒ **Sonuç:** antitezin **mantıksal** saldırıları (iç çelişki, aşırı-genelleme, ölçüm-kapsam uyuşmazlığı) tam güçtedir — bunlar zaten kaynak gerektirmez. Ama **olgusal karşı-örnekleri** (`moment.js`, `request`, CBAM, HBS vaka yöntemi, db-benchmark polars sonuçları) **`[K-hatırlama]`** düzeyindedir, `[D]` değil.
⇒ Hakemlikte bu ayrım uygulandı: **mantıksal saldırı → hüküm değiştirir · olgusal karşı-örnek → borç açar, hüküm değiştirmez.**

*Not: erişim haritası ajana verilmişti ∧ WebSearch yasaklanmıştı (sayaç dolu). Yani araç kullanmaması kısmen brifingin sonucudur — kendi hatam olarak kayda geçer.*

### 1.2 ⚠️ Aynı-aile hakemliği

`antitez_modeli ∈ aynı_aile(tez_modeli)`
A19'un kendi bulgusu: `öz_tercih_sapması → aile_düzeyine_yayılır`; çapraz-**aile** doğrulama çapraz-modelden üstün.
⇒ **Bu turdan çıkan hiçbir `⊨S` damgası "sağ kaldı" anlamına gelmez.** Doğru okunuşu: **"aynı-aile hakemi karşısında sağ kaldı."**

### 1.3 ⚠️ Protokol sapması — A5–A21

`A5..A21 → iddia_listesi tez_anında SAKLANMADI`
⇒ Antitez için listeler **sonradan çıkarılıyor** (ayrı ajan).
⇒ Risk: çıkarıcı iddiayı **yumuşatabilir ∨ çarpıtabilir**. Açık talimat verildi (*"zayıflatma yapma, aşırı-genelleme varsa koru"*) ama araya giren katman **gerçektir**.
⇒ **Kalıcı ders:** `iddia_listesi ∈ tez_çıktısının_ZORUNLU_parçası`. A22 sonrası bu zaten uygulanıyor; eski üç raporda yoktu.

---

## 2. A22–A24 HAKEMLİK

### 2.1 ⭐ ÇÜRÜTÜLDÜ — ve düzeltme gerekiyor

**H1 — İddia 22 ("tek vaka okuma transfer üretmez") ÇÜRÜDÜ. Ve bu bizim İÇ TUTARSIZLIĞIMIZ.**
Antitez: kaynağın kendi verisi `tek_analog → ~%10-30 transfer` gösteriyor, **sıfır değil**.
**Hakem: HAKLI ∧ dahası bizim kendi raporumuz da öyle diyor.** Tech-stack §5.3 aynen: *"kaynak analog yokken ~%10; **tek** analogla ~%30; ipucuyla ~%80"*.
⇒ **İddia listesi kendi raporunu yanlış özetlemiş.** Gerçek iddia: `tek_vaka → transfer DÜŞÜK ∧ ≠ sıfır` ∧ `şema_tümevarımı ⇔ karşılaştırma`.
⇒ **DÜZELTİLECEK:** tech-stack §5.4 iddia ④ ∧ L9 (P109 zaten doğru yazılmış — orada `~%30` var).

**H2 — İddia 16 ("PYTHONHASHSEED olmadan HİÇBİR koşum yeniden üretilebilir değildir") DARALDI.**
Antitez: `hash_sırası → yalnız hash-duyarlı kod yollarını etkiler`; saf numpy/pandas sayısal hattı (sabit sütun sırası, array-tabanlı) **bağımsız olabilir**.
**Hakem: HAKLI.** Bizim kendi ölçümümüz (R27) zaten mekanizmayı `set`-sıralaması üzerinden gösteriyor — yani **koşul zaten `set` kullanımıdır**, evrensel değil.
⇒ **DÜZELTİLECEK:** `hiçbir_koşum` → `hash-sırasına duyarlı kod yolu içeren her koşum`.

**H3 — İddia 18 ("DVC'nin getirisi SIFIRDIR") DARALDI.**
Antitez: uzak depolama olmasa da `dvc repro` yerel önbellekleme (değişmeyen aşamaları atlama) ∧ pipeline DAG'ı sağlar.
**Hakem: HAKLI.** Bizim gerekçemiz (R17) deponun kendi *"takım + bulut"* vurgusuna dayanıyordu — bu **değeri azaltır, sıfırlamaz**.
⇒ **DÜZELTİLECEK:** `getiri = 0` → `getiri AZALMIŞ ∧ 98 paketlik maliyeti karşılamıyor`. **Hüküm (ALINMAZ) değişmiyor**, gerekçesi düzeliyor.

**H4 — İddia 4 ("indirme sayısı bakım aktifliğini GÜÇLÜ ve monotonik öngörür") DARALDI.**
Antitez: `moment.js` bakım-moduna geçtiği hâlde indirmeler devasa kaldı; `request` deprecated ilan edildikten sonra yıllarca yüksek kaldı ⇒ **ekosistem ataleti**.
**Hakem: KISMEN HAKLI ∧ önemli.** Bizim ölçümümüz (R/M2) **katman-agregası**dır — top-500'de terk %8,6, rastgelede %54,2. Bu **dağılım** iddiasıdır, **paket-başına garanti** değil. Antitezin örnekleri tam da en üst katmandaki **aykırı değerlerdir** ve agregayı çürütmez — ama iddianın *"güçlü öngörür"* ifadesi paket-başına okunmaya açıktır.
⇒ **DÜZELTİLECEK:** `indirme → bakım_öngörür` ifadesine **"toplu düzeyde, paket-başına garanti değil"** kaydı eklenecek.
⚠️ Karşı-örnekler `[K-hatırlama]` — doğrulanmadı. Ama mekanizma (bağımlılık ataleti) **bizim kendi M7 bulgumuzla uyumlu** (*"çoğu alt-proje terk edilmiş bağımlılığı hiç değiştirmiyor"*) ⇒ **kabul edilir.**

### 2.2 ⭐⭐ EN DEĞERLİ BULGU — antitez bizi YANLIŞ ANLADI, ve sebebi BİZİM

**H5 — İddia 24, antitezin *"en net çürütmem"* dediği yerde ÇÜRÜMEDİ. Antitez cümleyi TERS okudu.**

Bizim iddia: *"Sonucu bilinen bir kararı okumak, sonuç yanlılığı nedeniyle süreç değerlendirmesini sistematik bozar; **sonuç kapatılmadan okuma öğretici değildir**."*
Kastedilen ayrıştırma: `[sonuç kapatılmadan] [okuma]` = **sonuç GÖRÜNÜRKEN okumak** ⇒ öğretici değil.
Antitezin okuduğu: *"sonuç açıklanmadan okuma öğretici değildir"* ⇒ ve haklı olarak HBS vaka yöntemini karşı-örnek gösterdi — o yöntem sonucu **bilerek saklar**.

**Hakem hükmü: iddia AYAKTA. Ama bu bir zafer değil, bir ARIZA kaydıdır.**
⇒ Yetkin bir okuyucu, önerme formunda yazılmış bir cümleyi **tam tersine** anladı.
⇒ Sebep: **olumsuzlamanın kapsamı belirsiz** — `¬(kapatılmış) ∧ okuma` mı, `kapatılmış ∧ ¬okuma` mı, Türkçe yüzeyde ayrışmıyor.

> **⭐ Bu, A31'in kendi bulgusunun CANLI VAKASIDIR.** A31 tam olarak şunu söylüyordu: *"olumsuzlamanın kapsamı doğal dilde belirsiz olduğunda kod SESSİZCE yanlış dalı seçer."* Burada kod değil **bir model** seçti — ve yanlış seçti.
> ⇒ Yani lojik→kod raporunun uyardığı tuzak, **o rapor yazılmadan önce bizim kendi metnimizde zaten mevcuttu.**
> ⇒ **DÜZELTİLECEK:** iddia yeniden yazılacak — *"Sonuç GÖRÜNÜR durumdayken okumak öğretici değildir; sonuç kapatılarak okumak (tahmin → aç → skorla) öğreticidir."*
> ⇒ **Ve kural:** önerme formunda `¬` kullanılan her cümlede **kapsam parantezle sabitlenecek**. Bu, V76'nın (notasyona kod-karşılığı sütunu) yanına giren ikinci somut kuraldır.

### 2.3 ⭐ İÇ TUTARSIZLIK — antitez haklı, kabul ediliyor

**H6 — İddia 25 ile İddia 2 arasında çifte standart var.**
Antitez: İddia 2, çerçevelerin (ADR/Radar/ATAM) etkinliğinin ölçülmediğini söyleyerek **şüpheci bir standart** uyguluyor. İddia 25 ise kalibrasyon skorlamasının *"tek pratik mekanizma"* olduğunu **aynı titizlikte kanıt sunmadan** ve **daha güçlü** bir kesinlikle iddia ediyor.
**Hakem: TAM İSABET. Kabul ediliyor.**
⇒ Kalibrasyon eğitiminin **mimari karar öğrenimine transferi ölçülmemiştir** — ve bunu bizim kendi raporumuz da söylüyor (A24 boşluk #4: *"Mimari kararlarda Brier-skorlu tahmin eğitimi denenmemiş"*), ama **iddia listesine bu kayıt taşınmamış.**
⇒ **DÜZELTİLECEK:** iddia 25 → `kalibrasyon_skorlaması = insan_kolaylaştırıcısız_nesnel_veri_üretebilen BİLİNEN_TEK_pratik_mekanizma` ∧ `[?] transferi mimariye ölçülmedi` ∧ `"tek" = bulunabilen tek, kanıtlanmış tek DEĞİL`.
⇒ Bu, tech-stack §7'deki **Model C önerisinin** dayanağını zayıflatır. Model C hâlâ önerilir — ama gerekçesi *"en iyi kanıtlı"* değil, zaten yazdığımız gibi **"tek uygulanabilir"**. Şerh güçlendirilecek.

### 2.4 ÇÜRÜTÜLEMEDİ — ⊨S (aynı-aile şerhiyle)

| İddia | Antitez sonucu |
|---|---|
| **21** — DP mesleklerde varyansın <%1'ini açıklar; yazılım mimarisi için ölçüm yok | **"en sağlam, en spesifik, en doğrulanabilir iddia"** ⇒ **⊨S** |
| **14** — in-sample Sharpe, denenen varyant sayısı olmadan yorumlanamaz | Literatürle güçlü örtüşme ⇒ **⊨S** |
| **15** — Parquet'in baskın gerekçesi dtype bütünlüğü | Çürütülemedi ∧ ayrıca antitez bunu **11'e karşı silah** olarak kullandı |
| **17** — naif look-ahead testi eşiklenmiş sinyalde işe yaramaz | Çürütülemedi |
| **3, 6, 9** | Çürütülemedi **ama doğrulanamadı da** ⇒ `⊨S değil`, **açık nötr** |

### 2.5 ▲ ANTİTEZİN BİZE KARŞI HAKLI OLDUĞU BİR NOKTA DAHA

**H7 — İddia 11 (polars) bir saman-adama saldırıyor olabilir.**
Antitez: İddia 15'in kendi mantığı (*"parquet'in gerekçesi hız değil dtype bütünlüğü"*) **polars'a geri uygulanırsa**, polars'ın asıl argümanı da hız değil **şema katılığı, lazy-evaluation'da erken tip hatası, Arrow bellek modeli, null-semantiği tutarlılığı**dır. İddia 11 polars'ı **kimsenin ciddi olarak savunmadığı bir hız argümanıyla** çürütüyor olabilir.
**Hakem: HAKLI ∧ ince bir yakalama.** Bizim ölçümümüz (R13) **hız** ekseninde `[D]`'dir ∧ geçerlidir. Ama **hüküm** (*"şimdi alınmaz"*) yalnız hız eksenine dayanıyor ⇒ **eksik gerekçe.**
⇒ **DÜZELTİLECEK:** R13'ün hükmüne şerh — *"hız ekseninde ölçüldü; şema-katılığı ∧ null-semantiği ekseni ÖLÇÜLMEDİ"* ⇒ yeni borç.
⚠️ Antitezin *"db-benchmark'ta polars groupby kat kat hızlı"* karşı-iddiası: **kendi ölçümümüz (R13, bu makinede, 1,26M satır) bunu göstermiyor** — ve antitez **kendi belirsizliğini dürüstçe işaretledi** (*"emin değilim"*). `[D]` ölçüm `[K-hatırlama]`yı yener ⇒ **rakam korunur**, ama ölçek bağımlılığı kaydı güçlendirilir (bizim ölçümümüz **1,26M satır**; db-benchmark ölçekleri farklıdır).

### 2.6 REDDEDİLEN SALDIRILAR

| Antitez iddiası | Hakem hükmü |
|---|---|
| **İddia 1 için:** *"innovation token bir ampirik hipotez değil, sezgisel bütçeleme kuralıydı; yanlışlanabilirlik standardı uygulanamaz"* | **REDDEDİLDİ.** Standart tezin kendisine değil, **tezin kullanılış biçimine** uygulandı. Bir sezgisel kural karar gerekçesi olarak kullanılıyorsa (ki JARVIS'te olacaktı) sonucunun ölçülüp ölçülmediği **meşru sorudur**. Ayrıca antitezin *"iddia da simetrik biçimde vagü"* eleştirisi haklı ⇒ küçük düzeltme: *"post-hoc ayarlanabilir"* iddiası bir **örnekle** desteklenecek (savunucuların *"boring bir liste değil, ekibin beceri setine göre değişir"* ifadesi zaten elimizde). |
| **İddia 12/17 için:** *"purged CV / embargo bu boşluğu dolduruyor, iddia görmezden geliyor"* | **REDDEDİLDİ — protokol gereği.** Antitez yalnız iddia listesini gördü; kaynak rapor (§6.6 R35) purged CV'yi **ölçülmüş sonuçlarla** zaten kapsıyor (`naif R² +0,85 ↔ purged −1,2`). Bu, antitezin **bilmesi mümkün olmayan** bir bilgiydi ⇒ eksiklik iddiada değil, **iddia listesinin dar olmasındadır**. *Yine de kayda değer: iddia listesi, raporun en güçlü bulgusunu dışarıda bırakmış.* |
| **İddia 8 için:** *"Prime Video tek vaka, 'ölçülmüş' statüsüne yükseltilemez"* | **KISMEN KABUL.** Bizim dayanağımız o vaka değil, **kohort çalışmasıydı** (registered report, ICSME 2023). Ama iddia metni bunu belirtmiyor ⇒ **iddia yeniden yazılacak**, dayanak açık edilecek. |

---

## 3. ÇIKAN DÜZELTME LİSTESİ

| # | Dosya | Ne değişecek |
|---|---|---|
| **K1** | tech-stack §5.4 ④ | `tek_vaka → transfer üretmez` → `transfer DÜŞÜK (~%30), sıfır değil` (H1) |
| **K2** | tech-stack §6.9 ⑦ | `hiçbir koşum` → `hash-sırasına duyarlı kod yolu içeren koşum` (H2) |
| **K3** | tech-stack §6.9 ⑨ + §6.8 | `DVC getirisi = 0` → `azalmış; 98 paketi karşılamıyor` (H3) |
| **K4** | tech-stack §3.4 ④ | `güçlü öngörür` → `+ toplu düzeyde, paket-başına garanti değil` (H4) |
| **K5** | tech-stack §5.4 ⑥ | ⭐ olumsuzlama kapsamı düzeltilecek + parantezle sabitlenecek (H5) |
| **K6** | tech-stack §5.4 ⑦ + §7 Model C | `tek pratik mekanizma` → `bulunabilen tek`; transfer `[?]` şerhi (H6) |
| **K7** | tech-stack §6.8 polars satırı | Hüküm korunur; `şema-katılığı ekseni ölçülmedi` borcu eklenir (H7) |
| **K8** | tech-stack §3.4 ⑧ | Dayanak (kohort çalışması) iddia metnine taşınacak |
| **K9** | LOJIK P109 | Zaten doğru (`~%30` var) — **değişmeyecek**, ama iddia listesiyle tutarlılık kaydı düşülecek |
| **K10** | Yeni kural | `¬` içeren her önermede **kapsam parantezle sabitlenir** (H5'ten türetildi) |

---

## 4. TURUN META-BULGUSU

**M1 — İddia listesi, raporun kendisinden DAHA ZAYIF çıktı.**
Üç bağımsız vakada (H1 `~%30`, H6 transfer şerhi, §2.6 purged CV) **iddia listesi, kaynak raporun kendi kaydını yanlış ya da eksik özetledi.**
⇒ `antitez(iddia_listesi) ≠ antitez(rapor)`
⇒ **Sonuç: iddia listesi tez ajanının kendi elinden çıkmalı ∧ rapordan sonradan türetilmemeli.** §1.3'ün dersi buradan ikinci kez geliyor — ama bu sefer **listeler tez anında yazılmış olduğu hâlde** oldu. Yani sorun yalnız türetme değil, **özetleme adımının kendisi**.

**M2 — Antitezin en değerli çıktısı çürütme değil, YANLIŞ ANLAMA oldu (H5).**
Bir hakemin metni ters okuması, metnin **kendi belirsizliğinin ölçümüdür**. Bu, kavrayış-deltası ölçmenin (F9) beklenmedik ama işleyen bir vekilidir.
⇒ **V80 adayı:** *"Antitez ajanının yanlış anladığı her cümle, o cümlenin yeniden yazılması gereken yerdir."*

**M3 — Araçsız antitez ucuz ∧ mantıksal eksende tam güçlü, olgusal eksende zayıf.**
`tool_uses = 0` ∧ `subagent_tokens ≈ 25k` — bu turun **en ucuz** ailesiydi ∧ **en çok düzeltme** üretti (10 madde).
⇒ **V81 adayı:** antitezi **iki koşumda** ayır — (a) araçsız *mantık antitezi* (ucuz, iç tutarlılık + aşırı-genelleme), (b) araçlı *olgu antitezi* (pahalı, karşı-örnek avı). Bu tur (a)'ydı ∧ getirisi yüksekti.

---

---

## 5. A25–A27 HAKEMLİK — ⭐ TURUN EN SERT SONUCU

**Bu antitez araç kullandı** (`tool_uses = 48`): `code.claude.com/docs/en/*.md` ham `curl` ile çekildi ∧ kurulu `cli.js` grep'lendi.
⇒ **Kanıt sınıfı `[D]`.** §1.1'in kaveatı bu aileye UYGULANMAZ.
⇒ Ve sonuç ağır: **teslim edilmiş bir raporda gerçek hatalar bulundu.**

### 5.1 ⛔ ÇÜRÜTÜLDÜ — rapor düzeltilecek

**H8 — `is_error` iddiası ÇÜRÜTÜLDÜ (⊨X, çözülmedi).**
Bizim iddia (P117): `subtype ∈ {error_max_turns, error_max_budget_usd}` ⇒ `is_error = FALSE`. Dayanak: kurulu `cli.js` v2.1.42'de `is_error:!1`.
Antitez: `agent-sdk/python.md` birebir — *"`is_error`: `True` when the conversation ended in an error state. **Always `True` on the `error_*` subtypes.**"*
**Hakem: DOĞRUDAN ÇELİŞKİ, çözülmedi ⇒ `⊨X`.**
Olası uzlaştırmalar (hiçbiri doğrulanmadı): ① minifiye kod okumam yanlıştı · ② CLI'nin iç üretim yolu ile SDK'nın belgelenmiş sözleşmesi farklı katmanlar · ③ sürüm kayması (kurulu v2.1.42 ↔ doküman ~v2.1.217).
⇒ **PRATİK SONUÇ:** *"limit-ölümlerini `is_error` ile filtreleyemezsin"* tavsiyem **artık güvenilmez**. Filtreleme yazacaksan **`subtype`'a bak** — bu her iki senaryoda da doğru kalır. Tavsiye korunur, **gerekçesi düşer**.

**H9 — Prompt cache iddiası ÇÜRÜTÜLDÜ.**
Bizim iddia (P126): *"Alt-ajanlar prompt cache'ten yararlanamaz."*
Antitez, `prompt-caching.md`'den birebir: *"It builds its own cache, **starting with no cache hits on its first call and warming up across its own turns.**"*
**Hakem: ANTİTEZ HAKLI. İddia fazla güçlüydü.**
⇒ Doğrusu: `alt_ajan → İLK çağrıda cache_isabeti = 0` ∧ `sonraki turlarda KENDİ cache'ini ısıtır` ∧ `TTL = 5dk (ana konuşmanın 1 saati yerine)`.
⇒ **"10 ajan = 10x alt sınırdır" çıkarımı kısmen ayakta** — ama yalnız **kısa ömürlü** alt-ajanlar için. Uzun ömürlü alt-ajan kendi cache'ini ısıtır ⇒ **§8'in "az sayıda uzun ömürlü > çok sayıda kısa ömürlü" tavsiyesi GÜÇLENİYOR**, çünkü mekanizma artık daha net.

**H10 — Eşzamanlılık iddiası ÇÜRÜTÜLDÜ.**
Bizim iddia (P127): *"Bağlayıcı sınır 20 değil **10**'dur."*
Antitez: `sub-agents.md` ∧ `env-vars.md` → `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` varsayılanı **20** olarak belgelenmiş; `MAX_TOOL_USE_CONCURRENCY` (10) **ayrı bir mekanizma**; `agent-view.md`'deki *"10 sessions ≈ 10x quota"* ise **üçüncü** ve tamamen farklı bir şey (kota tüketim kuralı, sert sınır değil).
**Hakem: ANTİTEZ HAKLI — üç sayıyı birleştirmişim.**
⇒ Doğrusu: `belgelenmiş_alt_ajan_eşzamanlılık_sınırı = 20` · `paralel_araç+alt_ajan_yürütme_sınırı = 10` · `10_oturum ≈ 10× kota` (sınır değil, tüketim).
⇒ **§9'un dalga zarfı (10 ajan) hâlâ savunulabilir** — ama gerekçesi *"sert sınır"* değil, **kota tüketimi ∧ yürütme kapısı**. Gerekçe düzeltilir, sayı korunur.

**H11 — ⛔ Explore/Plan iddiası DESTEKSİZ ÇIKTI.**
Bizim iddia (P134/U1): *"Explore ∧ Plan sürdürülemez, uzun işlerde kullanılmamalı"* — ve bunu **"ÇOK YÜKSEK değer, maliyet sıfır"** diye ilk sıraya koymuştum.
Antitez: `sub-agents.md`'de bu istisnaya dair **hiçbir kayıt yok**; istisna tutulan tek şey CLAUDE.md/git-status yüklememeleri.
**Hakem: ⚠️ CİDDİ. Öncül desteksiz.**
⇒ Bu, A27 ajanının aktardığı bir iddiaydı ∧ ben **doğrulamadan** U1 olarak öne çıkardım. Antitez dokümanı okudu ∧ bulamadı.
⇒ **U1 tavsiyesi ASKIYA ALINIYOR** — `[?]` damgalı. Doğrulanana kadar *"Explore/Plan kullanma"* diye bir kural **çıkarılmayacak**.

### 5.2 DARALDI

| # | İddia | Daralma |
|---|---|---|
| **H12** | `Stopped` yalnız üç yolla girilir | `agent-view.md`: **makine kapanması → Failed**, Stopped değil. Makine kapanması da "dışarıdan süreç sonlandırma"dır ⇒ **"yalnız" çerçevesi bu kenar-durumda çatlıyor.** Ayrıca antitez haklı bir ayrım daha yaptı: **agent-view oturum durumu ≠ alt-ajan task durumu** — iddia ikisini birleştiriyor olabilir |
| **H13** | `claude agents` alt-ajanları **hiç** göstermez | Fallback var: *"If `claude agents` prints a count followed by your configured subagents and then exits, agent view is unavailable"* ⇒ **belirli koşulda gösterir**. Ana tablo iddiası doğru (*"Subagents… aren't listed as separate rows"*), **"hiç" yanlış** |
| **H14** | Hata subtype'lı mesajda `result` alanı **şemadan tamamen yoktur** | **TS için doğru**; **Python dataclass tüm varyantları tek şekle düzleştiriyor** ⇒ `result` alanı **var, `None`**. İddia dil belirtmiyor ⇒ yarısı yanlış |
| **H15** | `isApiErrorMessage` **tek keskin ayırt edici** | Coupling **kaynak kodda doğrulandı** (`kjq()` hardcoded `stop_reason:"stop_sequence"` + `CY()` `isApiErrorMessage:!0`) ⇒ ⊨D. Ama **"tek"** süperlatifi doğrulanamadı — alan başka bağlamlarda da kullanılıyor |
| **H16** | Ebeveyne **yalnız son assistant metin bloğu** geçer | Özü doğru, formülasyon **abartılı-dar**: aktarılan *"biriken kısmi çıktı + hata notu"*, tek blok değil |

### 5.3 ⊨S — çürütülemedi, DOKÜMANLA DOĞRULANDI

| İddia | Antitez sonucu |
|---|---|
| **İki ortogonal eksen** (durum ↔ süreç canlılığı); `∙` sonlanma değil | *"tam isabet"* — `agent-view.md` ikisini ayrı tablolarda listeliyor ⇒ **⊨S ⊨D** |
| **WebSearch 200/oturum, ortak sayaç, sessiz boş dönüş** | *"tam örtüşüyor"* — `tools-reference.md` birebir doğruladı ⇒ **⊨S ⊨D** ⭐ |
| **RETRY_WATCHDOG = takas, saatlerce asılı kalabilir** | *"tam doğruluyor"* — `env-vars.md` birebir ⇒ **⊨S ⊨D** |
| **Resume tam bağlamı korur** | *"exactly where it stopped"* ⇒ **⊨S ⊨D** |
| **Checkpoint ≠ dayanıklılık; git tek gerçek kontrol noktası** | *"dokümanın kendi çerçevesi bu"* ⇒ **⊨S ⊨D** ⭐ |

### 5.4 Test edilemeyenler
`12, 13, 14, 16, 17` (API token-bucket · ITPM kovaları · Batch) → **`platform.claude.com` erişim listesinde değildi** ⇒ ne doğrulandı ne çürütüldü.
`21, 22, 23` (Temporal/durable execution teorisi) → kapsam dışı, birincil kaynaklar kapalı.

---

## 6. A28–A30 HAKEMLİK

*Bu antitez de araçsızdı (`tool_uses = 0`) ⇒ §1.1 kaveatı geçerli.*

### 6.1 ⛔ ÇÜRÜTÜLDÜ — yokluk iddiaları düştü

**H17 — İddia 17 ("özetleme bilgi kaybını ölçen HİÇBİR çalışma yok") ÇÜRÜTÜLDÜ.**
Antitez: QAGS · SummaC · FactCC (özet sadakati metrikleri) · LLMLingua (sıkıştırmanın downstream kaybı) — *"tek karşı-örnekle değil, koca bir alt-alanla"*.
**Hakem: HAKLI.** `[K-hatırlama]` ama alan adları spesifik ∧ tutarlı ⇒ kabul.
⇒ **DÜZELTİLECEK:** `hiçbir çalışma yok` → `bizim aradığımız kanalda bulunamadı; sadakat-metriği literatürü mevcut ∧ taranmadı`. **Bu bir `[ARANAMADI]` vakasıdır ∧ biz `bulunamadı` yazmışız** — tam olarak V73'ün uyardığı hata.

**H18 — İddia 6 ("negatif talimat için HİÇBİR ölçülmüş kanıt yok") ÇÜRÜTÜLDÜ.**
Antitez: Kassner & Schütze (ACL 2020) — modellerin olumsuzlamaya duyarsızlığını **doğrudan ölçüyor**.
**Hakem: HAKLI.** Aynı hata sınıfı (H17 ile) ⇒ aynı düzeltme.

**H19 — İddia 3 ("çok-ajanlı persona rol-oynama SİSTEMATİK olarak daha kötü") ÇÜRÜTÜLDÜ.**
Antitez: Du, Li, Torralba, Tenenbaum, Mordatch — multiagent debate GSM8K/MMLU'da tek-ajan CoT tabanını **artırıyor**. *"Sistematik iddiası tek karşı-örnekle çöker."*
**Hakem: HAKLI.** Ayrıca antitezin ikinci gözlemi daha keskin: **iddia 1 hafif bir "etkisiz" iddiasıyken, iddia 3 aynı aileden çok daha güçlü bir "sistematik zarar" iddiasına sıçrıyor — bağımsız gerekçe olmadan.**
⇒ **DÜZELTİLECEK:** `sistematik olarak daha kötü` → `ölçülen bazı kurulumlarda belirgin biçimde daha kötü`.

**H20 — İddia 24 ("süreç metrikleri SIFIR kanıt") ÇÜRÜTÜLDÜ (kısmi).**
Antitez: test-zamanı hesaplama ölçekleme çalışmaları (pass@k, araç-adım sayısı ↔ başarı) **en azından korelasyonel** kanıt sunuyor.
**Hakem: HAKLI.** Normatif sonuç (*"karar vermede kullanma"*) korelasyon≠nedensellik gerekçesiyle **ayakta**; ama `sıfır kanıt` ifadesi **abartı**.

### 6.2 ⭐ İÇ TUTARSIZLIKLAR — üçü de kabul

**H21 — İddia 21 vs 10/11/13: ÇİFTE STANDART.**
Antitez: *"n=5-20'de herhangi bir korelasyon anlamsızdır, raporlanmamalı"* derken, aynı rapor `%30-70`, `16×`, `~7×` gibi kesin rakamları **aynı şüphecilikle sorgulamıyor**.
**Hakem: TAM İSABET, kabul.** Ayrıca antitezin ikinci noktası da doğru: küçük-N korelasyon **bastırılmaz, güven aralığıyla raporlanır** (pilot çalışma pratiği) — *"raporlanmamalı"* aşırı.

**H22 — İddia 24 vs 19: AYNI EŞİK İKİ YERDE FARKLI.**
İddia 19 tekrar-örneklemeyi (**bir süreç müdahalesi**) meşruiyet artırıcı sayarken, iddia 24 süreç metriklerini toptan kanıtsız ilan ediyor.
**Hakem: KABUL.**

**H23 — İddia 12'nin kanıt türü karışması.**
Antitez: izolasyon+özet bir **mimari tasarım tavsiyesidir**, olgusal konsensüs değil; blackboard/paylaşılan-bellek mimarileri de var. Ve daha keskin: **bu tercih 13'teki maliyet kaygısından türüyor, 14'teki başarısızlık kanıtından DEĞİL** — yani maliyet-güdümlü gerekçe güvenilirlik-güdümlüymüş gibi sunuluyor. **12, 14'ten mantıksal olarak ÇIKMIYOR.**
**Hakem: TAM İSABET, kabul.** Bu, raporda zaten `⚠️ ürün-tasarım kararıdır, RCT DEĞİLDİR` diye işaretlenmişti (Q13) — ama **iddia listesine bu şerh taşınmamış.** M1'in üçüncü vakası.

### 6.3 Diğer daralmalar
`18` ("pairwise HER ZAMAN daha güvenilir") ⇒ objektif zeminli görevlerde (birim testi, tam eşleşme) rubrik üstün olabilir; pairwise **ikisi de kötüyken sahte tercih dayatır**. **DARALDI.**
`19` ⇒ tekrar örnekleme **rassal varyansı** azaltır, **sistematik yanlılığı azaltmaz**; üç oy aynı yanlılığı paylaşıyorsa **sahte-çoğulluk**. **Önemli daralma, kabul.**
`20, 22, 23, 25, 26` ⇒ hepsi mutlak niceleme nedeniyle koşullu hâle geldi. Özellikle `25` (*"n=1 ASLA meşru değil"*) ⇒ **ikili/felaket-türü farkta n=1 yeterlidir** (*"her seferinde çöküyor, düzeltme çözüyor"* mühendislik standardıdır). **Kabul.**
`10` ⇒ `%30-70` aralığı *"o kadar geniş ki neredeyse her gözlemi doğrular"* ⇒ **sahte kesinlik**. **Kabul.**

### 6.4 ⊨S
`8` (uzun/alakasız içerik riski — hedge'li olduğu için sağlam) · `14` (başarısızlıkların en büyük kategorisi görev tasarımı) · `11` (iddia edilen ↔ etkin bağlam farkı, görev-tipi kaydıyla) · `4` (atıf zorunluluğunun nedensel kanıtı yok — **antitez bunu güçlendirdi**: salt prompt-seviyesi *"kaynak göster"* talimatı, retrieval olmadan, **yeni bir halüsinasyon alt-türü** (uydurma atıf) üretebiliyor)

---

## 7. A31–A32 HAKEMLİK

*Araç kullandı (`tool_uses = 21`): Rust RFC, CBMC, SPARK, pyrsistent, icontract, Hypothesis, LogicBench/RuleTaker/FOLIO/miniF2F/IFEval/zod depoları.*

### 7.1 ⛔ ÇÜRÜTÜLDÜ

**H24 — İddia 7 ("`t`/`t+1` mutasyonla ifade edilirse invariant kontrolü İMKÂNSIZ hâle gelir") ÇÜRÜTÜLDÜ.**
Antitez: `pyrsistent` — *"All methods that would normally mutate it instead return a new copy… The original structure is left untouched."* + event sourcing.
**Hakem: HAKLI. "İmkânsız" savunulamaz.**
⇒ **DÜZELTİLECEK:** `imkânsız hâle gelir` → `naif mutasyon-temelli stilde kaybolur; kalıcı/immutable veri yapıları ∨ event sourcing ile korunur`. **Ve bu, tablodaki "doğrusu" sütununu GÜÇLENDİRİR** — çözüm zaten oradaydı, iddia metni fazla mutlaktı.

**H25 — İddia 5 ("DbC kütüphane-seviyesindedir") DARALDI.**
Antitez: **SPARK** kendini *"a programming language, a verification toolset and a design method"* olarak tanımlıyor ⇒ **dil-seviyesi DbC GERÇEKTEN VAR** (Ada/SPARK, Eiffel).
**Hakem: HAKLI.** İddia yalnız **Python/Java/JS decorator ekosistemi** için doğru.

**H26 — İddia 1 ("`[?]`/`⊨X` ayrımı GERİ ALINAMAZ biçimde kaybolur") DARALDI.**
Antitez: Rust RFC 0243 — `Option<T>` ile `Result<T,E>` yapısal olarak eşdeğer ama **farklı semantik amaçlarla** kullanılıyor ⇒ `[?] → Option::None`, `⊨X → Result::Err(Contradiction)` ile **ayrım hiç kaybolmadan taşınabilir**.
**Hakem: HAKLI ∧ ince.** Kayıp bir **doğa yasası değil, bir tasarım tercihinin sonucu**. *"Geri alınamaz"* kelimesi özellikle savunulamaz.
⇒ **Ama iddianın pratik değeri ARTIYOR:** kayıp kaçınılmaz değilse, **kaçınmak bir KARARDIR** — ve V76 (notasyona kod-karşılığı sütunu) tam olarak o kararı şimdiden vermektir.

**H27 — İddia 4 ("model-checking yalnız SPEC üzerinde çalışır") KISMEN ÇÜRÜTÜLDÜ.**
Antitez: **CBMC** *"is a Bounded Model Checker for C and C++ **programs**"* ⇒ soyut spec değil **doğrudan kodu** doğruluyor.
**Hakem: HAKLI.** Ayrıca antitezin ikinci noktası daha derin: CBMC **"Bounded"**dır (döngüleri sınırlı açar) ⇒ *"epistemik olarak daha güçlü"* **koşulsuz değil**; PBT ile **aynı sınıf** açık uçluluğu paylaşıyor, fark **nicelik** (tüketici ↔ rastgele), **nitelik değil**.
⇒ **DÜZELTİLECEK:** `ispat ↔ güven` ayrımı **12. iddia için de yumuşatılacak**.

**H28 — İddia 14 ("belirsizlik etiketlerinin koda taşınması HİÇ ÖLÇÜLMEMİŞ") KISMEN ÇÜRÜTÜLDÜ.**
Antitez: iddia **hangi soruyu sorduğu konusunda kayıyor** — dar okuma (*"LLM bunu nasıl taşıyor"*) ayakta; geniş okuma (*"belirsizlik/hata ayrımının koda taşınması"*) **yanlış**: Option/Maybe monadları, Rust Option↔Result, SQL üç-değerli mantık — **40+ yıllık literatür**.
**Hakem: HAKLI ∧ antitezin kendi ironisi de yerinde:** *"iddia kendi eleştirdiği muğlaklığı kendi işliyor."*
⇒ **DÜZELTİLECEK:** iddia **dar okumaya sabitlenecek** — `LLM'in bir spec'teki belirsizlik etiketini koda taşıma DAVRANIŞI ölçülmemiştir` (tip-teorik ayrımın kendisi değil).

### 7.2 ⭐ ANTİTEZ İKİ ÖNGÖRÜMÜ ÇÜRÜTTÜ — ve bunu dürüstçe söyledi

Brifingte iki iç çelişki adayı işaret etmiştim. Antitez ikisini de test etti ∧ **tutmadığını raporladı**:

**H29 — "İddia 9 ile 10 çelişiyor" öngörüm YANLIŞ.**
Antitez: farklı granülaritede çalışıyorlar — 9 **agregat** boşluğu (derlenme ↔ doğruluk), 10 **dar alt-tipi** (*"sözdizimsel geçerli AMA anlamca yanlış"*) hedefliyor. **İkisi de doğru olabilir.**
**Hakem: ANTİTEZ HAKLI, öngörüm düşer.**

**H30 — "17 çözülmemişken 18 hüküm kuruyor, meşru mu?" öngörüm YANLIŞ.**
Antitez: **18, 17'den bağımsız bir eksende** — 17 *"ne kadar biçimsellik performansı nasıl etkiler"* (ampirik/derece), 18 *"biçimsel formun işlevi nedir"* (kavramsal/amaç). **18, 17'nin çözümsüzlüğüne rağmen ayakta kalır.**
**Hakem: ANTİTEZ HAKLI, öngörüm düşer.**
⇒ Ayrıca antitez `17`'ye daha iyi bir çerçeve önerdi: *"çelişki değil, muhtemelen ters-U şeklinde tekdüze-olmayan bir ilişki"* (az biçimsellik → belirsizlik kaybı; çok biçimsellik → dağılım-dışı sözdizimi kaybı; ortada optimum). **Kabul — `⊨X` etiketi `[?] non-monotonic ilişki` olarak değişecek.**

> **Bu iki madde bu turun en sağlıklı sonucudur.** Hakem (ben) iki çelişki tahmin etti, antitez ikisini de **çürüttü ∧ çürüttüğünü söyledi**. Bir antitez ajanının *"aradığın çelişki yok"* diyebilmesi, protokolün **çalıştığının** kanıtıdır — evet-adamı olsaydı ikisini de "buldum" derdi.

### 7.3 ⊨S
`3` (PBT = güven, ispat değil) — **Hypothesis'in kendi tanımıyla doğrulandı ⇒ en sağlam duran iddia**
`11` (kategori-bazlı hata tablosu yok) — üç benchmark deposu tarandı, karşı-örnek çıkmadı ⇒ **en dirençli yokluk iddiası**
`15` (metodoloji var, rakam erişilemez) — **IFEval bunu birebir doğruladı**: metodoloji var, README'de rakam yok
`13, 16, 17, 18` — çürütülemedi

### 7.4 ▲ Antitezin kendi dürüstlük kaydı — aynen taşınıyor
> *"4 yokluk iddiasından 1'i (14) kapsam-daraltma yoluyla kısmen çürütüldü; 3'ü (8, 10, 11) **erişim duvarları nedeniyle test edilemedi** — ne doğrulandı ne çürütüldü. Bu, 'boş aramayı kanıt-yok diye yorumlama' uyarısının tam olarak öngördüğü tuzak: **erişim engeli ile gerçek yokluk ayırt edilemiyor**, ve bu ayrımsızlığın kendisi rapor edilmesi gereken bir bulgu."*

⇒ **Bu, V73'ün (`⊨A` = aranamadı etiketi) ÜÇÜNCÜ bağımsız gerekçesidir.** Üç ayrı aile aynı eksiği işaret etti.

---

## 8. GENİŞLETİLMİŞ DÜZELTME LİSTESİ

| # | Dosya | Ne değişecek | Ağırlık |
|---|---|---|---|
| K1–K10 | tech-stack · LOJIK | §3'teki liste | — |
| **K11** | ajan-durma §3, P117 | `is_error = false` → **⊨X, çözülmedi**; tavsiye `subtype`'a sabitlenir | ⭐ **yüksek** |
| **K12** | ajan-durma §8, P126 | `cache'ten yararlanamaz` → `ilk çağrıda isabet 0, sonra kendi cache'ini ısıtır, 5dk TTL` | ⭐ **yüksek** |
| **K13** | ajan-durma §8, P127 | `bağlayıcı sınır 10` → üç ayrı mekanizma ayrıştırılır; zarf korunur, gerekçe düzelir | ⭐ **yüksek** |
| **K14** | ajan-durma §11 U1, P134 | **Explore/Plan iddiası ASKIYA** — `[?]`, doğrulanmadan kural çıkarılmaz | ⭐⭐ **kritik** |
| K15 | ajan-durma §0, P114 | `Stopped yalnız 3 yol` → makine kapanması istisnası + oturum/task ayrımı | orta |
| K16 | ajan-durma §1, P115 | `claude agents HİÇ göstermez` → fallback istisnası | düşük |
| K17 | ajan-durma §3, P117 | `result alanı yok` → TS'de yok, Python'da `None` | orta |
| K18 | ajan-durma §4, P121 | `tek keskin ayırt edici` → coupling ⊨D, "tek" süperlatifi düşer | düşük |
| **K19** | araştırma-promptu §2.5 ⑧ | `özetleme kaybını ölçen HİÇBİR çalışma yok` → **`[ARANAMADI]`** | ⭐ **yüksek** |
| **K20** | araştırma-promptu §3.7 ⑥ | `negatif talimat için HİÇBİR kanıt yok` → **`[ARANAMADI]`** | ⭐ **yüksek** |
| **K21** | araştırma-promptu §3.7 ③ | `sistematik olarak daha kötü` → `bazı kurulumlarda belirgin daha kötü` | ⭐ **yüksek** |
| K22 | araştırma-promptu §4.6 ④ + Q30 | `korelasyon raporlanmamalı` → `CI ile birlikte raporlanır`; çifte standart kaydı | orta |
| K23 | araştırma-promptu §4.6 ⑦ | `sıfır kanıt` → `nedensel kanıt yok, korelasyonel kanıt var` | orta |
| K24 | araştırma-promptu §2.5 ③ (Q13) | Kanıt-türü şerhi **iddia listesine taşınacak**; `12, 14'ten çıkmıyor` kaydı | orta |
| K25 | araştırma-promptu §4.6 ② | Tekrar örnekleme **rassal varyansı** azaltır, **sistematik yanlılığı azaltmaz** | orta |
| K26 | araştırma-promptu §4.6 ⑧ | `n=1 ASLA meşru değil` → ikili/felaket farkta meşru | orta |
| **K27** | lojik-kod §1.3 + §1.5 ⑦ | `imkânsız hâle gelir` → `naif stilde kaybolur; immutable/event sourcing ile korunur` | ⭐ **yüksek** |
| K28 | lojik-kod §1.5 ⑤ | DbC kapsamı Python/JS ekosistemine daraltılır (SPARK/Eiffel istisnası) | orta |
| K29 | lojik-kod §1.5 ① | `geri alınamaz` düşer → **tasarım tercihi**; V76'nın gerekçesi güçlenir | orta |
| K30 | lojik-kod §1.5 ④ + §2.7 ④ | Model-checking kodu da doğrulayabilir (CBMC); `bounded` sınırı eklenir; `ispat↔güven` 12 için de yumuşar | ⭐ **yüksek** |
| K31 | lojik-kod §2.7 ⑥ | Yokluk iddiası **dar okumaya sabitlenir** (LLM davranışı, tip teorisi değil) | ⭐ **yüksek** |
| K32 | lojik-kod §2.6 L17 | `⊨X çelişki` → `[?] ters-U / non-monotonic ilişki` | orta |

---

## 9. TURUN İKİNCİ META-BULGUSU

**M4 — ⭐ ARAÇLI ANTİTEZ, ARAÇSIZ ANTİTEZDEN NİTELİKÇE FARKLI.**

| Tur | Araç | Token | Sonuç |
|---|---|---|---|
| A22–A24 | **0** | 25k | Mantıksal saldırı güçlü; olgusal karşı-örnekler `[K-hatırlama]` |
| A28–A30 | **0** | 25k | Aynı profil — iç tutarsızlıklar mükemmel, karşı-örnekler doğrulanmamış |
| **A25–A27** | **48** | 127k | ⛔ **Teslim edilmiş raporda 4 gerçek hata buldu** (H8-H11) |
| A31–A32 | 21 | 46k | Karışık — hem doküman kanıtı hem kavramsal daraltma |

⇒ **`araçlı_antitez` maliyeti ~5× ∧ getirisi NİTELİKÇE farklı.** Araçsız tur **iç tutarsızlık** bulur; araçlı tur **olgusal yanlış** bulur.
⇒ **V81 kesinleşti:** antitez **iki koşumda** ayrılmalı — (a) *mantık antitezi* (ucuz, araçsız, iç tutarlılık) · (b) *olgu antitezi* (pahalı, araçlı, doküman/kod karşılaştırması). **İkisi de gerekli, biri diğerinin yerini tutmuyor.**

**M5 — En pahalı hata sınıfı: DOĞRULANMADAN ÖNE ÇIKARILAN TAVSİYE.**
H11 (Explore/Plan) tek bir alt-ajan iddiasına dayanıyordu ∧ ben onu **"ÇOK YÜKSEK değer, maliyet sıfır"** diye listenin başına koydum ∧ **doğrulamadım**.
⇒ **Kural adayı:** `tavsiye_sırası = 1` ⇒ `dayanağı BAĞIMSIZ doğrulanmış olmalı`. Listenin başı, en az doğrulanmış maddenin yeri değildir.

**M6 — Antitez "çelişki yok" diyebildi (H29, H30).**
⇒ Protokol **evet-adamı üretmiyor**. Bu, `⊨S` damgalarına güven için gereken tek yapısal kanıttır.

---

## 9b. ⭐ CANLI ÖLÇÜM — TAKSONOMİDE OLMAYAN BİR SONLANMA MODU

*2026-07-26 15:56 UTC, A5–A21 antitez turları koşarken ölçüldü. Bu, A25 taksonomisine EKLENMESİ gereken yeni bir vakadır.*

**Gözlem:** üç antitez ajanı da `15:10–15:11` arasında son kaydını yazdı ∧ **45 dakika boyunca hiçbir yeni kayıt düşmedi.**
İki örnek, 45 saniye arayla: `boyut`, `satır sayısı`, `mtime` — **üçü de birebir aynı** ⇒ `büyüme = 0`.

**Son kayıt imzası (üçünde de aynı):**
`type = assistant` ∧ `content = ['text']` ∧ `isApiErrorMessage = None` ∧ `stop_reason = None`
⇒ `¬API_ölümü` (P121'in 17-vakalık sınıfı değil) ∧ `¬araç_ortası_ölüm` (`tool_use` değil)
⇒ **Metin ürettiler, sonra sustular.**

**Ve kritik olan:** `SendMessage` üçüne de **`"had no active task"`** döndürdü.
⇒ `ajan = ölü` ∧ `ajan ≠ çalışıyor`
⇒ **AMA HİÇBİR `task_notification` GELMEDİ.** Ne `completed`, ne `failed`, ne `stopped`.

### Hüküm — P114/P122'ye EK

`sonlanma_modu = SESSİZ ÖLÜM`: ajan durur ∧ aktif görevi kalmaz ∧ **hiçbir bildirim üretmez.**

⇒ **A25 taksonomisi eksik.** §3'teki tablo `SDK → 5 durum` ∧ `UI → 3 değer` diyordu; bu vaka **dördüncü ve kayıtsız** bir durumdur: *bildirim üretmeyen sonlanma*.
⇒ **Teşhis kılavuzu (§4) bu vakayı YAKALAYAMAZ** — kılavuz `<status>` alanından başlıyor, ama burada `<status>` hiç doğmuyor.
⇒ **Eklenmesi gereken adım:** `bildirim_yok ∧ süre > beklenen` ⇒ **transkript mtime'ını ve satır sayısını ÖRNEKLE**, bildirimi bekleme.

### Neden nöbetçi devreye girmedi

`CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS` belgelenmiş varsayılanı **600.000 ms (10 dk)**; ajanlar **45 dk** sessizdi ∧ abort edilmediler.
⇒ **C2 borcunun faturası:** kurulu ikili **v2.1.42**, dokümanlar **~v2.1.217**; A25 bu değişkenin kurulu ikilide **grep'te çıkmadığını** ölçmüştü.
⇒ **Koruma mekanizması bu sürümde YOK.** Raporda "geçerli olmayabilir" diye yazılmıştı; **artık ölçüldü: geçerli değil.**

### Kurtarma

`SendMessage` ⇒ üçü de sürdürüldü, **tam bağlamıyla** (P133 doğrulandı, üçüncü kez).
`ara_metin` ⇒ **üçünde de mevcuttu** ⇒ **V69 ("iskelet-önce") üçüncü kez karşılığını verdi.** Kesilme anında iş diskteydi, kayıp sıfır.

### ⭐ DÜZELTME — dürtme sonrası teşhis değişti

`SendMessage` gönderildi ⇒ **üçü de ~30 saniyede döndü** (`34s · 32s · 29s`) ∧ **üçü de tam raporla**.
Üçüncüsünün ilk cümlesi: *"Donmuş değilim — önceki turda tam sonucu ürettim ve döndürdüm."*
İkincisi: *"Bu teslim önceki turda tamamlanmış çalışmanın tekrarıdır."*

⇒ **`hesaplama = BİTMİŞTİ (15:11)`** ∧ **`teslim = OLMADI`**
⇒ **Teşhis düzeltilir: bu bir HESAPLAMA asılması DEĞİL, bir TESLİM arızasıdır.**

`ajan → nihai_metnini_üretti` ∧ `ajan → durdu` ∧ `task_notification = ∅`
⇒ İş **45 dakika boyunca diskte hazır bekledi** ∧ ebeveyn (ben) **beklemeye devam etti**.

**Bu, kayıp modunu değiştirir:**
- `hesaplama_asılması` ⇒ iş **yapılmamıştır**, sürdürme onu **yaptırır**
- `teslim_arızası` ⇒ iş **yapılmıştır**, sürdürme onu yalnız **taşır** — ve maliyeti ~30 saniyedir

⇒ **Pratik sonuç:** bir ajan beklenenden uzun sürdüğünde **önce dürt, sonra endişelen.** Maliyet 30 saniye; alternatif 45 dakika boş bekleme.
⇒ Ve `tool_uses = 0` üçünde de: dürtme sonrası **hiç araç çağırmadılar**, yalnız hafızalarındakini yazdılar — teslim arızası teşhisinin ikinci kanıtı.

### Bu vakanın kendi dersi

> **`bildirim_yokluğu ≢ çalışıyor`.**
> Bütün oturum boyunca bildirim bekledim; bu üç ajan için bildirim **hiç gelmeyecekti**. Bekleme süresi uzadıkça "hâlâ çalışıyor" varsayımı güçleniyordu — ve bu varsayım **yanlıştı**.
> ⇒ Bu, P73'ün (*"kaynak tükendi ≡ iş bitti"* hatası) **kardeşidir**: *"bildirim yok ≡ iş sürüyor"*.
> ⇒ **Kural adayı (V82):** uzun koşumlarda bildirim beklenmez, **transkript büyümesi periyodik örneklenir**. Ölçüm iki `stat` çağrısı; maliyeti sıfır.

---

## 9c. A5–A21 HAKEMLİK — tur kapandı

⚠️ **Kaveat:** üç tur da dürtme sonrası `tool_uses = 0` ile döndü; araç kanıtları **kesinti ÖNCESİ** turda toplanmıştı. Kaynak-kod ∧ doküman alıntıları o turdan geliyor ∧ spesifiktir ⇒ kabul edilir. Araçsız kalan kısımlar §1.1 kaveatına tabidir.

### 9c.1 ⛔ KAYNAK KODLA ÇÜRÜTÜLENLER — en sert sonuçlar

**H31 — A7/25 ("hafıza dosyası SESSİZCE kırpılır") ÇÜRÜTÜLDÜ.**
Antitez, `cli.js`'ten: `FZ=200` aşıldığında ajanın sistem promptuna **otomatik, sayısal uyarı** ekleniyor — *"WARNING: MEMORY.md is N lines (limit: 200)…"*
**Hakem: ANTİTEZ HAKLI. "Sessizce" YANLIŞ.** ⇒ **DÜZELTİLECEK (K33):** `sessizce kırpılır` → `kırpılır ∧ ajana sayısal uyarı verilir`. Risk **düşer**: ajan kırpılmayı bilir.

**H32 — A5/3 ("heartbeat göndermeyen iş durdurulamaz") ÇÜRÜTÜLDÜ.**
`cli.js`: `TaskStop` **`task_id` ile durdurur**, heartbeat/işbirliği şartı yok.
**Hakem: HAKLI, bu sistem için.** ⇒ **K34:** iddia genel dağıtık-sistem teorisinde geçerli, **Claude Code'da geçerli DEĞİL**. Kapsam ayrılacak.

**H33 — ⚠️ A8/31 ("eksen başına optimum ≈ 4") CİDDİ ŞÜPHE ALTINDA.**
Antitez: *"kaynaksız; muhtemelen çalışma belleği kapasitesi (Cowan) alanından yanlış nakil."*
**Hakem: ŞÜPHE HAKLI ∧ bu bir TAVSİYEYDİ.** Kategori şeması önerisinin tek somut sayısı buydu.
⇒ **K35 ⭐:** `optimum ≈ 4` **`[?]` damgalanacak** ∧ dayanağı bulunana kadar **kural olarak yazılmayacak.** *(H11/Explore-Plan ile aynı hata sınıfı: doğrulanmadan öne çıkarılan sayı.)*

**H34 — A5/4 (asılma nöbetçisi senkron alt-ajanlara uygulanmıyor) — DAYANAK BULUNAMADI.**
Antitez `cli.js`'te `watchdog`, `idleAgent`, `stuckDetection`, `hungTask`, `healthCheck` terimlerinin **hiçbirini** bulamadı.
**Hakem: §9b ile YAKINSIYOR.** İki bağımsız ölçüm aynı sonuca varıyor: **bu sürümde asılma nöbetçisi YOK.** ⇒ C2 borcu **kapandı, olumsuz yönde**.

### 9c.2 ⛔ DOKÜMANLA ÇÜRÜTÜLENLER — A12 ailesi ağır hasar aldı

| # | İddia | Antitez bulgusu | Hüküm |
|---|---|---|---|
| **H35** | Cihazlar arası oturum sürekliliği **kapatılmış bir özelliktir** | `mobile.md`: **"Sessions persist across devices"** | ⛔ **ÇÜRÜTÜLDÜ. K36** — iddia tersine döndü |
| **H36** | Yerel süreç kapanır ∨ ağ kısa kopar ⇒ oturum **sona erer** | `agent-view.md`: arka-plan oturumu terminal kapansa ∧ ağ kısa kesilse **hayatta kalıyor**; yalnız tam kapanma bitiriyor | ⛔ **ÇÜRÜTÜLDÜ (büyük ölçüde). K37** |
| **H37** | Oturum devri **tek yönlüdür** (web→terminal, tersi yok) | Desktop app **"Continue in"** yerel→web itebiliyor | ⛔ **KISMEN ÇÜRÜTÜLDÜ. K38** |
| **H38** | A15/47: yayımlama eşiğini **ajan kendi başına geçemez** | `routines.md`: **onaysız push/PR mümkün** | ⛔ **ÇÜRÜTÜLDÜ. K39 ⭐** — bu bir GÜVENLİK varsayımıydı |
| H39 | A12/22 (config buluta taşınmıyor) ∧ A12/24 (koşum sırasında onay yok) | Dokümanla **teyit edildi** | ⊨S ⊨D |

> **⚠️ K39 ayrıca işaretleniyor:** *"ajan yayımlama eşiğini kendi geçemez"* bir **güvenlik gerekçesiydi**. Doküman aksini söylüyorsa, bu varsayıma dayanan her tasarım kararı **yeniden okunmalı**.

### 9c.3 Mantıksal çürütmeler

**H40 — A15/43 ("kimlik doğrulamaması, iki davanın sonucunu belirleyen TEK kural") ÇÜRÜTÜLDÜ.** *"asla" + "tek kural" nedenselliği; çok-faktörlü testler normdur."* ⇒ **K40.**
**H41 — A11/12 ("her koşulda mevcuttur") ÇÜRÜTÜLDÜ** — mutlak niceleme; birebir-alıntı sistemi karşı-örnek. ⇒ **K41.**
**H42 — A12/25 ("bilişsel mümkünlük HİÇBİR kanıtla desteklenmemiş") ÇÜRÜTÜLDÜ** — görev-değiştirme-maliyeti literatürü **var**; *"kanıtsızlık" yanlış çerçeveleme.* ⇒ **K42.** *(H17/H18 ile aynı sınıf: `[ARANAMADI]` → `bulunamadı` hatası, dördüncü vaka.)*
**H43 — A14/35 (arama uzayı döngüsüz çizgelerle sınırlı) KISMEN ÇÜRÜTÜLDÜ** — çok-turlu mimariler **döngü içerir**. ⇒ **K43.**
**H44 — A16/3 ("araçların erişebildiği azami katman YALNIZ referans bütünlüğü") ÇÜRÜTÜLDÜ** — `doctest` ∧ `nbval` **davranışsal doğruluk** denetliyor. ⇒ **K44.**
**H45 — A21/44 ("tek markdown katmanı paylaşılabilir") mutlak hâliyle ÇÜRÜTÜLDÜ** — kendi komşuları (45–47) tarafından iç-tutarsız kılınıyor. ⇒ **K45.** *(Bu, kod-entegrasyonu raporunun kendi §3.4 hükmüyle — "paylaşılabilir yüzey %100, yürütülebilir yüzey %0" — zaten uyumlu; iddia listesi fazla mutlak yazılmış. M1'in dördüncü vakası.)*
**H46 — A21/48 (protokolde çağıran/çağrılan ayrımı) DARALDI** — `claude mcp serve` ile Claude Code **hem istemci hem sunucu** olabiliyor ⇒ rol sabit değil. ⇒ **K46.**

### 9c.4 ⊨S ⊨D — birincil kaynakla doğrulananlar

| İddia | Kaynak |
|---|---|
| **A16/1** — Markdown'da "sözdizimi hatası" kavramı yoktur | **CommonMark spec birebir**: *"Any sequence of characters is a valid CommonMark document"* ∧ *"nothing in Markdown counts as a 'syntax error'"* ⭐ |
| **A19/32** — OpenAI-uyumlu katman üretime uygun değil ∧ önbellek yok | `platform.claude.com` birebir: *"not considered a long-term or production-ready solution"* + *"Prompt caching is not supported"* |
| **A20/40** — genel OpenAI-uyumlu sağlayıcı sürücü olarak kabul edilmiyor | `llm-gateway-protocol.md` |
| **A20/41** — sağlayıcı değişimi önbelleği sıfırlıyor | `prompt-caching.md` |
| **A21/51** — kalıcı izin onayları worktree'ler arasında paylaşılıyor | `settings.md` ⭐ *(güvenlik açısından önemli)* |
| A7/18, A7/19 | `sub-agents.md` ile teyit |

### 9c.5 ⚠️ YARGI-ÇEVRESİ BOŞLUĞU — Salih için kritik

Antitez: **A11 (10, 11, 12, 14, 15) ∧ A15 (43, 44, 46, 47, 48, 49) hiçbiri ülke belirtmiyor.**
`Türkiye (TMK m.24-25)` ↔ `ABD (eyalet-bazlı right of publicity, CFAA)` ↔ `AB (Persönlichkeitsrecht, DSM metin-madenciliği istisnaları)` arasında **maddi farklılık var**.
⇒ *"Salih'in Türkiye bağlamı düşünülürse bu boşluk özellikle kritik ve teze karşı en kolay itiraz noktalarından biri."*
⇒ **K47 ⭐:** hukuk ailelerinin **tüm hükümlerine yargı-çevresi damgası** eklenecek; damgasız hüküm **kullanılmayacak.**

### 9c.6 Test edilemeyenler — dürüstlük kaydı
`A18 bloğu (18–26) TAMAMEN test edilemedi` — akademik kanallar 403. Antitezin kendi ifadesi: *"Bu bir kapasite itirafıdır, iddiaların doğruluğu hakkında hüküm değildir."*
`A6 (10–17)` çoğunlukla çürütülemedi ama **doğrulanamadı** da — istatistik iddiaları standart teoriyle uyumlu, bağımsız kanıt yok.
⇒ **`⊨S` değil, `açık nötr`.**

---

## 10. AÇIK

- ✅ **Tüm antitez turları KAPANDI** — A5–A32, on iki aile grubu
- **K1–K47 düzeltmeleri UYGULANMADI** — PC oturumu Adım Sıfır'da uygulayacak (`cc/gorev-2026-07-26-1.md`)
- **En acil dört madde — hepsi aynı hata sınıfı: DOĞRULANMADAN ÖNE ÇIKARILAN TAVSİYE**
  - **K14** — Explore/Plan sürdürülemezliği: dayanak yok, tavsiye **askıda**
  - **K35** — "eksen başına 4 kategori": kaynaksız, muhtemel yanlış-alan nakli, **askıda**
  - **K39** — "ajan yayımlama eşiğini kendi geçemez": doküman aksini söylüyor, bu bir **güvenlik varsayımıydı**
  - **K47** — hukuk hükümlerinde yargı-çevresi damgası yok; Türkiye bağlamı için **kritik**
- `⊨S` damgaları **aynı-aile şerhiyle** verilecek (§1.2); A25–A27 ∧ A31–A32'nin doküman-doğrulamalı `⊨S`'leri bu şerhten **muaf** (kanıt modelden değil kaynaktan geldi)
- `⊨S` damgaları **aynı-aile şerhiyle** verilecek (§1.2)
