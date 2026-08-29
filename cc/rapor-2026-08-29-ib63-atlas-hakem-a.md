# İB-63 / Aile A — MASKELİ HAKEM VERDİKTİ (formal paralellik koşulları)

## Künye
- **Tarih:** 2026-08-29 · **Rol:** Maskeli hakem (üretici koşumların devamı değil; kıyas kimliğe değil İDDİA+KANIT'a göre)
- **Girdiler:** `scratchpad/ib63-hakem-a/rapor-1.md` (TEZ: 40 iddia, 4 alan — Bernstein/BHG/DAG/build) · `rapor-2.md` (ANTİTEZ: kırpılmış 10 iddia üzerinde 38 karşı-kanıt, 24 URL)
- **Sondaj durumu:** İki taraf da bağımsız denetçi sondajından geçti. Rapor-1: Bernstein üç-koşulu, hermetiklik, conflict-tanımı alıntıları birebir. Rapor-2: MAST (150 iz, κ=0.88), Thinking-Machines (1000→80), PostgreSQL kilit-terfisi, CPI² birebir. **Sondaj-dışı kalan yük-taşıyan alıntı:** rapor-2'nin ČVUT "necessary but not sufficient" slaytı (Kalem 8'de işlendi).
- **Yöntem:** Her karar-taşıyan kalemde üç düzey ayrıldı: **GEREKLİ** (bunsuz güvenlik yok mu) ↔ **YETERLİ** (tek başına güvence veriyor mu) ↔ **UYGULANABİLİR** (deterministik olarak denetlenebilir mi). Kritik gözlem doğrulandı: rapor-2'nin çürütmeleri neredeyse tamamen YETERLİLİK mutlaklarına vuruyor; rapor-2'nin kendi dürüstlük notu da bunu teslim ediyor ("Bulguların hiçbiri ayrıklık koşullarının gerekliliğini çürütmez"). Ayrıca R2'ye verilen 10-iddia listesi, rapor-1'in metninde zaten korunumlu (hedged) olan bazı önermeleri mutlaklaştırmış (ör. rapor-1 K-1 açıkça "YETERLİ, gerek değil" der; İddia 1 bunu "kök/yeterli" mutlağına çevirir) — bu mutlakların düşmesi rapor-1'in kendi metnini her yerde düşürmez.

## Verdikt tablosu

| # | Kalem | Gerekli? | Yeterli? | Uygulanabilir? | HÜKÜM |
|---|---|---|---|---|---|
| A | Çakışma tanımı (aynı öğe + ≥1 yazma) + BHG Teorem 2.1 (küresel çevrimsizlik ⟺ seri-denklik) + §2.5 taşınabilirlik | — (tanım/teorem) | model-içi: evet | evet (graf + çevrim testi) | **SAĞLAM** (model-içi; rapor-2'de tek karşı-kanıt yok) |
| 1 | R/W-kümesi ayrıklığı koşulunun statüsü | disjonksiyon olarak evet-yakını: çakışan çift → (ayrık ∨ sıralı) | HAYIR tek başına; 4 ek şartla evet | evet (kesişim testi / kilit matrisi) | **DARALDI** |
| 2 | Hermetiklik / tam-beyan varsayımı | evet (kümeler eksikse 1 hükümsüz) | HAYIR (statik garanti edilemez) | zorlamayla kısmen (sandbox, çift-koşum) | **DARALDI** |
| 3 | Granülerlik seçiminin etkisi | granül beyanı gerekli | "dosya-düzeyi yeter" mutlağı DÜŞTÜ | evet, granül açık yazılırsa | **DARALDI** |
| 4 | Kesişimsiz-ama-sıralı durumlar (dış yan etki) | model-kapsam maddesi gerekli | "sıralama yalnız kesişimden" mutlağı DÜŞTÜ | evet, dış-etki öğeleştirilirse | **DARALDI** |
| 5 | DAG çerçevesinin sınırları | kenar-tam grafta antizincir gerekli | tek başına HAYIR (dinamik graf, kaynak, retry) | evet, 3 ek alanla | **DARALDI** |
| 6 | LLM-ajan "görünmez okuma kümesi" | koşullar sağlanırsa çerçeve taşınır | "doğrudan uygulanır" DÜŞTÜ | 3 koşulla evet | **DARALDI** |
| 7 | okur∩okur güvenliği | — | mutlak biçimi değil, daraltılmış biçimi | evet | **DARALDI** (rapor-2'nin kendi hükmüyle uyumlu) |
| 8 | Bernstein "yeterli" (IUSB, sondajlı) vs "gerekli ama yetersiz" (ČVUT, sondajsız) | — | — | — | **ÇELİŞKİLİ** — çerçeve ayrımıyla çözüldü (aşağıda) |

**Sayım: 1 SAĞLAM · 7 DARALDI · 1 ÇELİŞKİLİ (çözümlü) · 0 KARARSIZ.** Mutlak-biçim olarak DÜŞEN alt-iddialar: 5 (listede "DÜŞEN/DARALAN" bölümünde).

---

## Kalem kalem gerekçe + daraltılmış formlar (manifest kural-taslağına AYNEN girecek)

### Kalem 1 — Ayrıklık koşulu: gerekli mi, yeterli mi?
- **GEREKLİ düzeyi:** Mutlak gereklilik değil — alternatifi rapor-1'in kendi K-2'sinde var (happens-before ile sıralama) ve BHG §2.5 komütatif işlem sınıfı için çakışma tanımının daraltılabileceğini söyler. Ama **disjonksiyon** (ayrık ∨ sıralı) gereklilik-yakını muhafazakâr çekirdektir; karşı-örnek yalnız egzotik sınıf (aynı değeri yazan / komütatif işlemler). Rapor-2 bunu açıkça teslim eder.
- **YETERLİ düzeyi:** Tek başına HAYIR. Rapor-2'nin isabetli vuruşları: kümeler tam değilse (Kalem 2), granül yanlışsa (Kalem 3), etki model-dışıysa (Kalem 4), hedef değer-doğruluğu değil zaman/kaynaksa (CPI², Pathfinder) hüküm çöker.
- **Hakem düzeltmesi (rapor-2 aşımı):** İddia 5 m.1'deki write-skew örneği ÜÇ kümeli Bernstein'ı ÇÜRÜTMEZ — write skew'de r1(x)∩w2(x) ≠ ∅, yani Bernstein koşul (2) zaten ihlaldedir; örnek yalnız "yazma-kümeleri ayrıksa yeter" (Snapshot Isolation'ın first-committer-wins kuralı) zayıf biçimini çürütür. Üç-küme kuralı bu örnekte hasar almaz.

```KURAL-TASLAK-1
İki birim A,B için paralel-izin ⟺
  [ yazar(A) ∩ (okur(B) ∪ yazar(B)) = ∅  ∧  yazar(B) ∩ okur(A) = ∅ ]
  ∨  aralarında beyan edilmiş sıra kenarı var.
Bu test yalnız şu 4 şart altında hüküm taşır: kümeler TAM (Kural-2),
granül beyanlı (Kural-3), etki model-içi (Kural-4), hedef değer-doğruluğu.
Şartlardan biri düşerse varsayılan hüküm: SERİ.
```

### Kalem 2 — Hermetiklik / tam-beyan
- **GEREKLİ:** Evet — beyan eksikse Kural-1'in girdisi yalan söyler (Bazel: beyan-dışı girdi → yanlış artımlı build; netcdf `.mod` gizli yan-ürün vakası).
- **YETERLİ / statik garanti:** HAYIR. Rapor-2'nin en sağlam bulgusu: dinamik bağımlılık sınıfı ("it is impossible to compute the dependency graph before the build starts" — à la Carte §2.2), sandbox'ın konak ortamı gizlemediği beyanı, nondeterminizm kaynakları (timestamp/build-ID), ccache direct-mode kaçağı. Rapor-1 zaten "(ii) formal teorinin dışındadır" diye işaretlemişti — burada iki rapor ÇATIŞMAZ, tamamlar.
- **UYGULANABİLİR:** Zorlamayla — beyan-dışı erişimi sessiz başarıdan gürültülü hataya çeviren yalıtım + çift-koşum doğrulaması.

```KURAL-TASLAK-2
Tam-beyan VARSAYILMAZ, ZORLANIR:
(a) beyan-dışı okuma/yazma girişimi hata üretmeli (yalıtılmış çalışma alanı)
    ya da birim seri sınıfına düşmeli;
(b) beyan-dışı erişimin sessizce başarılı olabildiği ortamda Kural-1 hükmü GEÇERSİZDİR;
(c) koşum sırasında keşfedilen bağımlılık = graf değişikliği → paralel-izinler
    yeniden değerlendirilir (restart kabul edilir);
(d) yazar-kümesi yan-ürünleri DE kapsar (gizli çıktı = beyan ihlali).
```

### Kalem 3 — Granülerlik
- İki yönlü, belgeli etki: **kaba granül → sahte çakışma** (PostgreSQL kilit-terfisi → serialization failure artışı; false sharing), **yanlış/yüzeysel granül → kaçak çakışma** (Fowler semantic conflict: metin düzeyinde temiz, davranış düzeyinde bozuk), **ince granül → yönetim maliyeti** (Anthropic 4×/15× token). "Dosya-düzeyi yeterlidir" mutlağı DÜŞTÜ; çerçevenin granül-parametrikliği ayakta.
- **Kritik ek (Cerone, chopping):** bir parçalamanın doğruluğu ÇİFTE değil SİSTEME bağlıdır — sisteme `lookup2` eklemek, önceden doğru parçalamayı yanlışlar. Hüküm çift-bazlı saklanamaz.

```KURAL-TASLAK-3
okur/yazar kümeleri GRANÜL beyanıyla gelir (dosya | bölüm/satır | kayıt | kavram);
denetim granülü = beyan granülü. Kaba granül sahte çakışma (gereksiz serileştirme/iptal),
granül-uyumsuzluğu kaçak çakışma (bozulma) üretir.
Parçalama hükmü sistem-bağımlıdır: koşuma yeni birim eklendiğinde
mevcut paralel-izinler ÇİFT bazında değil KOŞUM bazında yeniden denetlenir.
```

### Kalem 4 — Kesişimsiz-ama-sıralı (dış yan etki)
- Rapor-2 fenomeni sağlam belgeler: COPS (ayrık anahtarlar, kullanıcı-görünür sıralama zorunlu), transactional outbox (DB+broker ikili-yazma), Jepsen (serializability gerçek-zaman sırası vermez). "Sıralama yalnız kesişimden doğar" mutlağı DÜŞTÜ.
- **Hakem notu:** COPS örneğinde çakışma aslında ÜÇÜNCÜ tarafın (okuyucunun) okuma kümesi üzerinden vardır — ikili ayrıklık analizinin küresel tarihçeye (Kalem A, Teorem 2.1) yükseltilmemesi hatasıdır; formalizmi değil, çift-bazlı kısayolu düşürür. Dış yan etki (mesaj/push/ödeme) ise gerçek model-dışıdır ve ancak öğeleştirilerek içeri alınır.

```KURAL-TASLAK-4
Kesişim testi yalnız MODELE DAHİL kümeler üzerinde hüküm verir.
(a) Model-dışı etki (mesaj, push, dış API, kullanıcıya görünür durum) taşıyan birim
    bu etkiyi bir yazma-ÖĞESİ olarak beyan eder (gerekiyorsa sıra/atomiklik kenarıyla);
    beyan edemiyorsa paralel-izin alamaz (varsayılan SERİ).
(b) Öğeler-arası değişmez (invariant) varsa, o değişmezi kuran/okuyan her birim
    ilgili öğelerin TÜMÜNÜ okur-kümesine yazar.
(c) Tekrar-deneme yapan birim idempotency anahtarını graf-DIŞI kalıcı defterde tutar.
```

### Kalem 5 — DAG çerçevesi
- **GEREKLİ:** Kenarları tam grafta çevrimsizlik + antizincir tek çizelge kuralı olarak ayakta; rapor-2'nin kendi notu: "DAG + antizincir, veri bağımlılığı düzeyinde doğru bir çerçevedir; çürüyen kısım 'yeterli' nitelemesidir."
- **YETERLİ değil:** (a) düğüm sayısı koşum öncesi bilinmeyebilir (Airflow dynamic task mapping) ve graf koşarken değişir (Bazel restarting scheduler); (b) graf yalnız VERİ bağımlılığını taşır — kaynak/kilit/öncelik etkileşimi grafın dışında sistemi düşürebilir (Mars Pathfinder: graf temiz, öncelik ters çevrimi reset attırdı); (c) retry kimliği graf çözmez.

```KURAL-TASLAK-5
Çevrimsiz graf + antizincir, kenarları TAM ve DOĞRU grafta geçerlidir; ek şartlar:
(a) koşum-anı görev üretimi izinliyse çizelge dondurulmaz — graf değişiminde
    yeniden değerlendirme/restart zorunlu;
(b) graf kenarları yalnız veri bağımlılığıdır; paylaşılan kaynak/kilit/kota
    ayrı bir kısıt alanında beyan edilir (kaynak-çekişmesi çakışma sayılmaz
    ama süre-sınırlı işte doğruluk hatasına dönüşebilir);
(c) yeniden-deneme/iptal kimliği graf dışı kalıcı defterde (Kural-4c).
```

### Kalem 6 — LLM-ajan işlerine uygulanabilirlik koşulu
- **"Doğrudan uygulanır" DÜŞTÜ.** Rapor-2'nin üç belgeli gediği: (i) ajan arızaları R/W-kümesi dilinde değil iletişim/bağlam dilinde ölçülüyor (MAST: bağlam kaybı, bilgi saklama, adım tekrarı); (ii) determinizm ön-koşulu ham hâliyle düşük (Thinking-Machines: eş-kullanıcı yükü "girdi olmayan ama çıktıyı değiştiren" gizli girdi); (iii) paylaşılan-bağlam alanları paralelleşmez (Anthropic beyanı).
- **Hakem düzeltmeleri (rapor-2 aşımı):** Anthropic'in "iki alt-ajan aynı konuyu araştırdı" örneği GÜVENLİK ihlali değil VERİM kaybıdır — Bernstein hükmü (bozulma yok) o vakada doğrudur; çerçeve verim vaadi hiç vermemişti. Thinking-Machines yazısının kendisi de belirlenimsizliğin YENİLEBİLDİĞİNİ gösterir (batch-invariant çekirdekler) — ön-koşul ölümcül değil, maliyetli. MAST'ın "bilgi saklama"sı ise formal dilde eksik akış-kenarıdır: çerçeveyi çürütmez, ajanlar-arası bilgi akışının görünür kanala (dosya/artefakt) zorlanması gerektiğini kanıtlar.

```KURAL-TASLAK-6
Formal çerçeve ajan işlerine ancak ÜÇ KOŞULLA uygulanır:
(1) İş-birimi, dosya/artefakt-düzeyi okur-yazar beyanlı göreve indirgenir;
    ajanlar-arası bilgi akışı YALNIZ beyan edilen artefaktlar üzerinden yapılır
    (konuşma-içi/bağlam-içi aktarım okuma kümesine girmez, dolayısıyla yasaktır)
    ve yalıtım (ayrı çalışma kopyası) ile zorlanır.
(2) Ajanın görünmez girdileri (model durumu, örnekleme, eş-yük, tarih) manifest'te
    'belirlenimsiz-girdi' damgasıyla açık taşınır; doğruluk tekrar-üretim varsayımıyla
    değil KAYIT + doğrulama kapısıyla sağlanır.
(3) Paralel-izin yalnız GÜVENLİK hükmüdür (bozulma yok), VERİM hükmü değildir;
    tekrar-işi önlemek için kapsam-ayrımı (hangi birim hangi soruyu/alanı kapsar)
    ayrıca beyan edilir.
```

### Kalem 7 — okur∩okur
Rapor-2'nin kendi daraltması hakemce ONAYLANDI ve bir ek aldı. Daraltılmış form (rapor-2'den aynen + ek):

```KURAL-TASLAK-7
"Okur∩okur, yazarların yokluğunda ve okumaların atomik olduğu granülerlikte
paralel-güvenlidir." EK: 'yazar' kümesi SİSTEM-yazarlarını da kapsar
(temizlik/damıtma/arşivleme/vacuum sınıfı bakım işleri yazar sayılır;
salt-okur şerit, bakım şeridiyle eşzamanlıysa sürüm/anlık-görüntü disiplinine tabidir).
```
(Not: rapor-2'nin PG hot-standby kanıtı zaten okur-YAZAR çakışmasıdır — vacuum yazardır; daraltılmış formu çürütmez, destekler.)

### Kalem 8 — Kaynak çelişkisi: "yeterli" (IUSB) vs "gerekli ama yetersiz" (ČVUT)
İki ikincil kaynak sözcük düzeyinde ters konuşur; ČVUT alıntısı sondaj-dışıdır (doğrulanmamış sayılır). Çözüm çerçeve ayrımıdır: **ikili bellek-semantiği düzeyinde** üç-küme ayrıklığı YETERLİdir (gerekli değil — aynı değeri yazan çift karşı-örnek); **tüm-program düzeyinde** ikili sınama tek başına yetersizdir çünkü dolaylı (geçişli) bağımlılıklar ve üçüncü-taraf okurlar da kapatılmalıdır (ČVUT'un "all indirect dependencies" notu = Kalem A'nın küresel çevrimsizliğine geri düşer). Manifest muhafazakâr okumayı alır: ikili test, ancak küresel kapanım (tüm çiftler + geçişlilik) altında hüküm verir. HÜKÜM: ÇELİŞKİLİ-ÇÖZÜMLÜ; kural değişikliği doğurmaz (Kural-1 + Kalem A zaten kapsıyor).

---

## HAYATTA KALAN ÇEKİRDEK — "Jarvis manifest-şeması hangi alanları taşımalı"

1. **`okur[]` + `yazar[]` (yan-ürünler dahil) + `sira[]` kenarları.** Çekirdek hüküm: çakışan çift (aynı öğe + en az biri yazma) ya AYRIK ya SIRALI olmalı; hüküm formülü Kural-Taslak-1. Bu, dört alanın (Bernstein / BHG conflict / DAG kenarı / build beyanı) sondajdan geçmiş ortak paydasıdır ve antitez gereklilik düzeyine dokunamamıştır.
2. **`granul` alanı** (dosya | bölüm | kayıt | kavram) — kümeler hangi birimde sayılıyor; denetim aynı granülde yapılır; terfi/birleştirme davranışı açık yazılır (Kural-Taslak-3).
3. **`zorlama_modu` + `beyan_disi_politikasi` (hata | seri) + `dogrulama`** — tam-beyan varsayım değil zorlama+doğrulama rejimidir: yalıtılmış çalışma kopyası, beyan-dışı erişimde gürültülü hata, gerektiğinde çift-koşum karşılaştırması (Kural-Taslak-2).
4. **`dis_etki[]` + `idempotency_anahtari`** — model-dışı etki ya yazma-öğesi olarak içeri alınır ya birim seri sınıfına düşer; retry kimliği graf-dışı kalıcı defterde; öğeler-arası değişmez varsa ilgili öğelerin tümü okur-kümesine girer (Kural-Taslak-4).
5. **`deps[]` + `dinamik_kesif` (yasak | restart) + `kaynak_kisiti[]`** — küresel çevrimsizlik + antizincir çizelge kuralı; graf koşumda değişirse yeniden değerlendirme; kaynak/kilit çekişmesi ayrı alan (Kural-Taslak-5). Hüküm çift-bazlı değil KOŞUM-bazlı saklanır — yeni birim eklemek eski izinleri geçersizleyebilir (Cerone).
6. **Ajan-özel üçlü: `kapsam_beyani` + `belirlenimsiz_girdi[]` + `dogrulama_kapisi`** — paralel-izin güvenlik verir, verim vermez; görünmez girdiler damgalanır; doğruluk kayıt+kapıyla sağlanır; ajanlar-arası akış yalnız beyan edilen artefaktlardan (Kural-Taslak-6/7). (Jarvis kanonundaki "tekrar-üretim varsayılmaz, kayıtla sağlanır" ilkesiyle birebir uyumlu.)

## DÜŞEN / DARALAN

**DÜŞEN mutlaklar (5):**
1. "Ayrıklık tek başına kök/yeterli koşuldur" — zaman/kaynak/yan-etki/anlam eksenleri dışarıda (CPI², Fowler, Stripe, false sharing).
2. "Tam beyan verilirse tespit tamamen statik yapılır" — dinamik bağımlılık sınıfı grafı koşum öncesi kurdurmaz (à la Carte §2.2).
3. "Sıralama zorunluluğu yalnız küme-kesişiminden doğar" — COPS/outbox/Jepsen.
4. "İzolasyon seviyeleri çakışma-güvenliğini tek başına çözer" — write skew (SI'ya isabetli), read-only anomaly, PG SERIALIZABLE'ın seri-koşumda oluşmayacak hataları; uygulama değişmezi ayrı ayak.
5. "Formal çerçeve LLM-ajanlara DOĞRUDAN uygulanır" — yalnız Kural-Taslak-6 koşullarıyla uygulanır.

**DARALAN (kural-taslağına giren formlar):** Kural-Taslak-1…7 yukarıda AYNEN verildi; manifest-şeması taslağına bu bloklar değişmeden aktarılabilir.

**Hakem tespit ettiği antitez-aşımları (kayda geçsin):** write-skew örneği üç-kümeli Bernstein'a değil yalnız W∩W-ayrıklığına vurur (r∩w zaten ihlalde); Anthropic tekrar-iş örneği güvenlik değil verim bulgusudur; CPI² değer-doğruluğunu değil performans yalıtımını vurur (süre-sınırlı sistemler hariç — Pathfinder oradaki gerçek köprüdür); PG hot-standby kanıtı okur∩okur değil okur∩sistem-yazarı vakasıdır.
