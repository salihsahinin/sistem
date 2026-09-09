# Araç ve Model Entegrasyonu — insan yüzü

> Kaynak: `raporlar/2026-07-26-arac-entegrasyonu.md` · Register: kavrayış · Compiler: **AÇIK** (F1-F9)
> **UYARI: Bu dosya karar kaynağı DEĞİLDİR.** Katman-1 kararı teknik kayıttan alınır. Her maddenin sonunda kaynak bölüm var.
> ⚠️ **Geçerlilik tarihi: 26 Temmuz 2026.** Bu ailede sürüm ve yıldız rakamları **haftalar içinde bayatlar**; yapısal bulgular (kim hangi dosyayı okuyor, izin varsayılanları, protokol yerleşimi) uzun ömürlüdür.

---

## 1. Tek cümlede

*"Denetçi başka model, işçi ucuz model"* sezgin **ölçülmüş olarak doğru** — ama gerekçesi tasarruf değil **hata bağımsızlığı**; ve eklenebilecek 7 aracın biri ölü, ikisi kategori değiştirmiş, üçü Claude Code'un ikizi, biri de zaten yerleşik olan bir yeteneği tekrarlıyor.

---

## 2. Ne bulduk

### ① Sezgi doğru — ama "başka model" yetmiyor, "başka aile" gerekiyor

- **İddia:** Çapraz-aile doğrulama, aynı-aile doğrulamadan üstün; o da öz-doğrulamadan üstün. 37 model × 9 benchmark: *"çapraz-aile doğrulama özellikle etkili… çözücü ile doğrulayıcı benzedikçe fayda azalıyor."*
- **Mekanizma:** Öz-tercih sapması **aile düzeyine yayılıyor** — hakem, aynı sağlayıcının akraba modellerine de not şişiriyor. Sapma **−%38 ile +%90** arasında, ve kaynağı modelin kendi çıktısının düşük perplexity'si ⇒ **mimari bir tercih, düzeltilebilir bir prompt hatası değil**.
- **Neye dayanıyor:** İkincil (abstract katmanı).
- **Ne kadar güveniyoruz:** Sıralamaya orta-yüksek. **Büyüklüğe düşük:** farkın puan cinsinden ne kadar olduğu birincil metinde kaldı, **erişilemedi**.
- **Ne yapmamız gerekiyor:** Opus'a Sonnet denetletmek sapmayı **kısmen taşır**. Denetçi **başka aileden** olmalı.
- → `arac-entegrasyonu §1.1`

### ② Ama bağımsızlık satın alınamıyor

- **İddia:** İki model birlikte hata yaptığında **%60 oranında aynı yanlış cevapta buluşuyorlar**. Ve kritik olan: *"büyük ve daha isabetli modeller, mimarileri ve sağlayıcıları farklı olsa bile yüksek korelasyonlu hata yapıyor."*
- **Neye dayanıyor:** İkincil, 350+ model.
- **Ne kadar güveniyoruz:** Orta-yüksek — **ve bu oturumda bağımsız bir ölçümle yakınsıyor** (*"9 hakem ≈ 2 bağımsız oy"*). İki ayrı çalışma, aynı sonuç.
- **Ne yapmamız gerekiyor:** **Çapraz-sağlayıcı denetçi bir kalkan değil, ikinci bir süzgeç.** Ondan mutlak koruma bekleme.
- → `arac-entegrasyonu §1.2`

### ③ Jüriyi büyütme, çeşitlendir

- **İddia:** Çok-ajanlı toplulaştırmada **2 heterojen ajan, 16 homojen ajanı geçiyor** — 8 kat ajan azalması.
- **Neye dayanıyor:** İkincil.
- **Ne kadar güveniyoruz:** Orta.
- **Ne yapmamız gerekiyor:** Jüri büyütmek yerine **çeşitlendir**. Bu, hem kalite hem maliyet açısından aynı yöne gidiyor.
- → `arac-entegrasyonu §1.3`

### ④ Maliyet gerekçesi zayıf — merdiven zaten aile içinde var

- **İddia:** Fiyatlar (26 Temmuz 2026, milyon token başına giriş/çıkış): **Opus 5 = 5/25 · Sonnet 5 = 2/10 · Haiku 4.5 = 1/5**. Önbellek okuma taban girdinin **0,1 katı**; batch **%50 indirimli**.
- **Neye dayanıyor:** Birincil.
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** Opus'tan Haiku'ya **5 kat**, Opus'tan Sonnet'e **2,5 kat** ucuzluk var — **sağlayıcı değiştirmeden**. ⇒ **Çapraz-sağlayıcıya geçmenin gerekçesi tasarruf DEĞİL, hata bağımsızlığı olmalı.**
- → `arac-entegrasyonu §1.4`

### ⑤ ⭐ Çapraz-sağlayıcının gizli maliyeti

- **İddia:** Anthropic'in OpenAI-uyumlu katmanı **üretim için önerilmiyor** — resmî cümle: *"Bu uyumluluk katmanı öncelikle model yeteneklerini test etmek ve karşılaştırmak içindir, çoğu kullanım için uzun vadeli ya da üretime hazır bir çözüm olarak değerlendirilmiyor."*
- **Somut kayıplar:** `strict` yok sayılıyor ⇒ araç JSON şemaya uyma garantisi yok. `response_format` yok sayılıyor. **Prompt caching desteklenmiyor** ⇒ uzun kanon bağlamı olan bir sistemde girdi maliyeti **10 katına** çıkabilir. Ve **desteklenmeyen alanlar hata vermeden SESSİZCE düşüyor**.
- **Neye dayanıyor:** Birincil. **Ve antitez bunu doğruladı** — kaynağı birebir okudu.
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** Her sağlayıcıya **kendi API'siyle** gidilmeli; çeviri bir geçit katmanının işi.
- → `arac-entegrasyonu §1.5`

### ⑥ "Açık kaynak" ile "yerel" iki ayrı karar

- **İddia:** Aynı ölçüm harness'ında: frontier %88,0 · büyük açık ağırlıklı modeller %71-74 · **tüketici donanımı sınıfı %40,0**.
- **Neye dayanıyor:** Birincil (aynı harness).
- **Ne kadar güveniyoruz:** Yüksek — ama bir uyarıyla: **standardize harness ile satıcı harness'ı arasındaki fark 10-30 puan**. Model kartlarındaki skorlar senin sisteminde alacağın skor **değil**.
- **Ne yapmamız gerekiyor:** Büyük açık modeller frontier'a yaklaşıyor — **ama onlar yerelde koşmuyor, API'den alınıyor**. Bu iki kararı karıştırma.
- → `arac-entegrasyonu §1.6`

**Ve uzun ufukta açık büyüyor:** araç sayısı arttıkça **%7-85**, araç yanıtı uzadıkça **%7-91**, çok turlu konuşma uzadıkça **%13-40** performans düşüşü. Kısa ufukta %40-50 başarı gösteren bir görev, uzun etkileşim geçmişine gömüldüğünde **%10'un altına** düşebiliyor — hem de ilgili bilgi bağlamda dururken.

### ⑦ Yerelin tartışmasız kazandığı tek katman

- **İddia:** **Gömme (embedding)** modelleri 137M-677M boyutunda; bu boyutlar CPU'da bile koşar, ~1 GB RAM ister.
- **Neye dayanıyor:** İkincil.
- **Ne kadar güveniyoruz:** Orta-yüksek.
- **Ne yapmamız gerekiyor:** **Yerelin en net kazandığı katman budur** — ve veri hiç dışarı çıkmıyor. Vault indeksleme için doğrudan aday.
- → `arac-entegrasyonu §1.7`

⚠️ **Ama nicemleme kalite kaybı için tarafsız tablo yok:** aracın kendi dokümanında **tablo yok**; üçüncü taraf ölçümler dağınık (%1-5 · 1,6 puan · **7,8 puan** · <%1). ⇒ **Kararı modele göre ver, kurala göre değil.**

### ⑧ ⭐⭐ Hızlı çıkarım sorusu: büyük ölçüde "hayır"

- **İddia:** Gerçek oturum izlerinde (**357.161 LLM turu, 432.510 araç kaydı, 43 geliştirici**) duvar saati şöyle ayrışıyor: **insan düşünme %92,3 · araç yürütme %4,8 · LLM üretimi %3,3**.
- **Neye dayanıyor:** Bağımsız, açık iz veri seti; depo README'sinin metodoloji notu birinci elden doğruluyor.
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** **Hızlı çıkarımın dokunabileceği dilim, toplam sürenin otuzda biri.**
- → `arac-entegrasyonu §2.1`

**Ve iş yükünün şekli bunu daha da kötüleştiriyor:** medyan önek ~120 bin token, medyan çıktı ~200 token ⇒ girdi çıktıyı **294 kat** aşıyor. Hesap: tur başına decode farkı **~0,3 saniye**; ölçülen ilk token gecikmesi ise **1,54 saniye** — farkın **beş katı**. ⇒ **4 katlık decode üstünlüğü bu iş sınıfında ölçülemez hâle geliyor.**

⚠️ **Bu hesap bizim türetmemiz, ölçüm değil.** *"Token/saniye artışı ajan görev süresini %X kısaltır"* biçiminde kontrollü bir deney **yok**.

### ⑨ Ve görünürdeki çelişkinin çözümü

- **Durum:** Başka bir çalışma *"LLM çıkarımı toplam koşum süresinin %71-98'i"* diyor.
- **Çözüm:** **Çelişki gerçek değil, payda farkı.** O ölçüm **insansız benchmark koşumları**; iz verisi ise **insanın döngüde olduğu** gerçek oturumlar.
- **Ne yapmamız gerekiyor:** **İnsan devredeyken hız neredeyse önemsiz; ajan otonom koşarken model süresi gerçekten baskın.** Bu ayrım, hızlı çıkarımın nereye konacağını belirliyor.
- → `arac-entegrasyonu §2.3`

### ⑩ Üç ek engel — ve ikisi doğrulandı

- **Birinci engel:** Claude Code **rastgele bir OpenAI-uyumlu sağlayıcıyı sürücü model olarak kabul etmiyor**. ⇒ Hızlı sağlayıcılar bu sisteme ancak **araç seviyesinde taşeron** olarak girer. ✔ **Antitez doğruladı.**
- **İkinci engel:** Turların **%95,7'si** önbellek isabeti alıyor; sağlayıcı değiştirmek 120 bin token'lık öneği **soğuk prefill'e** zorlar. ⇒ **Hızlı çıkarım konuşmanın ortasına serpiştirilmemeli**, kendi başına duran işlere verilmeli. ✔ **Antitez doğruladı.**
- **Üçüncü engel:** Kalite uçurumu sağlayıcıda değil **model ailesinde** — bir kodlama benchmark'ında 42,70 karşısında 16,20 (~2,6 kat). ⇒ Hızlı sağlayıcıya geçmek *"aynı işi daha hızlı"* değil, **"farklı bir zekâ sınıfıyla daha hızlı"** demek.
- → `arac-entegrasyonu §2.4`

### ⑪ ⭐ İzin modeli asimetrisi — en tehlikeli bulgu

- **İddia:** Alternatif bir terminal ajanının dokümanı açıkça şöyle diyor: *"İzinlerin çoğu varsayılan olarak `allow`."* Yalnız üç şey kısıtlı.
- **Neye dayanıyor:** Birincil.
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** ⚠️ **Bu deponun Dilim-1 yapısal kilidi YALNIZ Claude Code'da geçerlidir.** Aynı depo başka bir ajanla açılırsa **kilit yoktur.**
- → `arac-entegrasyonu §3.2`

⚠️ **Ve çeviri sessizce hatalı olabilir:** o araçta `*` işareti `/` dahil her karakteri eşliyor; Claude Code ise glob kullanıyor (`**` ayrı anlam taşır). ⇒ `core/**` → `core/*` çevirisi **kilitte delik bırakabilir** — ve bu, elle yapılan ve **sessiz başarısız olan** bir işlem.

### ⑫ ⭐ Worktree'ler izin onaylarını paylaşıyor

- **İddia:** *"Bir worktree kendi dosyalarını ve dalını alır, ama deponun `.git` dizinini, proje kapsamlı eklentileri ve **kaydedilmiş izin onaylarını** ana checkout ile paylaşır."*
- **Neye dayanıyor:** Birincil. **Antitez bunu doğruladı ve ayrıca güvenlik açısından önemli diye işaretledi.**
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** Bir worktree'de verilen *"bir daha sorma"* onayı **tüm paralel ajanları bağlar**. Dilim-1 kilidi settings-deny ile yapısal olduğu için ayakta; ama **kalıcı onayla genişletilen her izin, tüm paralel yüzeye sessizce yayılır**.
- → `arac-entegrasyonu §3.6`

### ⑬ ⭐ Talimat katmanı birleşebilir — okunan kısım için

- **İddia:** Tek bir markdown talimat katmanı birden çok aracı besleyebilir. **Üç bağımsız üreticiden, üç ayrı kanıt:** Anthropic köprüyü resmen belgeliyor (`@AGENTS.md` içe aktarımı ya da symlink) · alternatif bir araç köprüyü **ters yönde yerleşik** sunuyor · bir üçüncüsünün kaynak kodunda dosya adı alanı **dizi kabul ediyor**.
- **Ve vahşi doğada ölçüldü:** 32 depo tarandı. En güçlü artefakt bir depoda **bir dosya, üç ad** — gerçek dosya artı iki symlink, md5'leri birebir aynı. ⇒ **Senin sorunun bu depoda çözülmüş hâlde duruyor.**
- **Neye dayanıyor:** Birincil, üç ayrı üreticiden.
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** Tek komut: `ln -s CLAUDE.md AGENTS.md`. Bu **23 aracın okuyabileceği bir yüzey açar ve hiçbir mevcut davranışı değiştirmez** — çünkü yön korunuyor, `CLAUDE.md` kanonik kalıyor. Windows'ta symlink yönetici hakkı istediği için alternatif: `AGENTS.md` içine tek satır `@CLAUDE.md`.
- → `arac-entegrasyonu §3.4` · `§4.1`

⚠️ **Ama mutlak hâliyle yanlıştı — ve bunu kendi tablomuz söylüyordu.** Antitez, *"tek markdown katmanı paylaşılabilir"* iddiasının **mutlak biçimde** yazıldığını ve **kendi komşu önermeleriyle çeliştiğini** gösterdi: aynı bölümün tablosu zaten *"yürütülebilir yüzey %0"* diyor. ⇒ Doğru kapsam: **okunan katman %100 paylaşılır, yürütülebilir katman %0.** Ve taşınmayan şey **izin kilidinin ta kendisi**.

### ⑭ Protokol yönü sabit değilmiş

- **İddia (düzeltildi):** *"Doğru soru MCP destekliyor mu değil, ACP'de hangi yönde duruyor: çağıran mı, çağrılan mı."*
- **Ne değişti:** Bu çerçeve her aracın **sabit bir yön** taşıdığını varsayıyordu. Antitez düzeltti: `claude mcp serve` ile **Claude Code hem istemci hem sunucu** olabiliyor.
- **Ne kadar güveniyoruz:** Düzeltmeye yüksek.
- **Ne yapmamız gerekiyor:** Yön bir **araç özelliği değil, bir kurulum tercihi**. Soru yeniden yazılır: *"bu araç hangi yönde duruyor"* değil, **"bu kurulumda hangi yönde durmasını istiyorum"**. ⇒ Ayrımın pratik değeri **artıyor** — artık bir kısıt değil, bir **tasarım kaldıracı**.
- → `arac-entegrasyonu §3.5`

### ⑮ Yıldız sayısı olgunluk ölçütü olarak bozuk — kanıtı elimizde

- **İddia:** Bir araç **35,1k yıldızla öldü** (*"artık aktif olarak bakılmıyor ve tüm kullanıcılar için salt okunur"*). Bir başkası **82,1k yıldızla kategori değiştirdi** — artık kodlama ajanı değil, ajanları koşturan bir kontrol merkezi. Bir üçüncüsü **47,7k yıldızla durdu** (son sürüm Şubat, 442 açık PR, MCP desteği yok). Buna karşılık **220 açık konuyla** en temiz hijyene sahip olan araç bunların hiçbiri değil.
- **Neye dayanıyor:** Birincil (depo durumları).
- **Ne kadar güveniyoruz:** Yüksek — **ve bu, tech-stack raporundaki yıldız bulgusunun bağımsız bir tekrarıdır**.
- **Ne yapmamız gerekiyor:** **Olgunluk ölçütü: son commit tarihi × sürüm kadansı × açık konu/PR birikimi.** Bu üçlüde sıralama **tamamen değişiyor**.
- → `arac-entegrasyonu §3.3`

### ⑯ Bir aracın çekirdek yeteneği zaten yerleşikse, eklemek net negatif

- **İddia:** Paralel worktree yöneticisi olarak öne çıkan aracın varlık nedeni, Claude Code'un artık **yerleşik yaptığı** şey: worktree bayrağı, alt-ajanlar için worktree izolasyonu, worktree yapılandırma dosyaları, agent view.
- **Neye dayanıyor:** Birincil.
- **Ne kadar güveniyoruz:** Yüksek.
- **Ne yapmamız gerekiyor:** **Eklenecek aracın çekirdek yeteneği mevcut aracın yerleşik yeteneğiyle örtüşüyorsa, ekleme net negatiftir.** Üstelik günlük sürüm temposu ayrı bir bakım vergisi.
- → `arac-entegrasyonu §3.6`

**Ve bir hatırlatma, kendi kanonumuzdan:** bu araç hakkında **kendi wiki sayfamız 2026-07-09'da yazılmış** ve o günkü uyarısı bugün de geçerli: *"Senin darboğazın hiçbir zaman araç eksikliği olmadı; gönderilmiş çıktı."*

### ⑰ Ve bir öz-düzeltme kaydı

Bir alt-ajan, oturum ortamında bir dizin adı gördüğü için *"bir router kurulu, maliyeti ~sıfır"* sonucuna vardı. **Doğrulama yanlış çıktı:** o dizin bu bulut oturumunun **proxy'siydi**, içinde yalnız sertifikalar vardı, ilgili komut **yoktu**.

⇒ Öneri geçerliliğini korudu, ama **maliyet iddiası düştü**. Bu, **dizin adından yapılan çıkarımın nasıl yanlış gidebileceğinin canlı örneği** ve bu oturumun kendi doğrulama disiplininin bir yakalaması. → `arac-entegrasyonu §0`

---

## 3. Ne bulamadık

### Aradık, bulamadık

| Ne | Not |
|---|---|
| **Aynı-aile ile çapraz-aile doğrulama farkının puan cinsinden büyüklüğü** | Sıralama doğrulandı, **büyüklük birincil metinde kaldı**. A19'un en önemli açık sayısı. |
| **Nicemleme kalite kaybının tarafsız referans tablosu** | Aracın kendi dokümanında **tablo yok**; üçüncü taraf ölçümler dağınık. |
| **Araç eklemenin net getirisi üzerine dış ampirik çalışma** | **Yok.** Bizim hükmümüz yetenek örtüşmesi argümanına dayanıyor, ölçüme değil. |
| **A2A protokolü bu ekosistemde** | İncelenen **12 kodlama aracından hiçbiri** konuşmuyor. Protokol gerçek ve büyük, ama **yanlış katman**. |

### **Arayamadık** — bunlar yokluk hükmü DEĞİL

| Ne | Neden |
|---|---|
| **Çapraz-sağlayıcıya geçince prompt performansının ne kadar düştüğü** | Anthropic *"prompt'unu yeniden yazmayı düşün"* diyor ama **rakam vermiyor**. ⚠️ **Planın gizli maliyeti tam burada.** |
| **Hızlı sağlayıcının resmî fiyatı ve hız limitleri** | Kullanılan rakamlar ~8 ay eski üçüncü taraf veritabanından ⇒ **karar öncesi teyit edilmeli**. |

### Ölçmedik, türettik

*"Token/saniye artışı ajan görev süresini %X kısaltır"* biçiminde **kontrollü bir deney yok**. §2.2'deki hesap bizim türetmemiz — **ölçüm değil**. Bu ayrım korunmalı.

### Çelişkili, karar verilemez

Bir yerel modelin ajanik/kodlama skoru için dolaşan rakamlar **çelişkili** (bir kaynak %60,7 diyor, başkaları benzer bir sayıyı **farklı bir modele** atfediyor). ⇒ **Bu rakama dayanarak karar verilmemeli.**
Aynı şekilde hızlı çıkarım sağlayıcısının token/saniye rakamı için dolaşan üç farklı sayı var; **ölçen ve tarih belirtilmeden verilen en yüksek rakam kullanılmamalı**; savunulabilir bant 1.900-2.100.

---

## 4. Ne değişiyor

**Sıfır maliyetli, bugün yapılabilir:**

1. **`ln -s CLAUDE.md AGENTS.md`** — tek komut, **23 aracın okuyabileceği bir yüzey açar**, hiçbir mevcut davranışı değiştirmez. Yön önemli: `CLAUDE.md` kanonik kalır. Windows'ta alternatif: `AGENTS.md` içine `@CLAUDE.md`. → `§4.1`

**Düşük maliyetli, yüksek getirili — sırayla:**

2. **Alt-ajan `model:` / `effort:` merdiveni** — sıfır maliyet, ~1 saat, beklenen tasarruf %40-70 (kestirim). Anthropic'in kendi önerisi. → `§4.2`
3. **Tek bir çapraz-aile denetçi** — yalnız çelişki kapısı ve rapor doğrulama. **A19'un asıl kazancı budur.** → `§4.2`
4. **Yerel gömme** — vault indeksleme; yerelin tartışmasız kazandığı tek katman. → `§4.2`
5. **Ücretsiz bir ikinci görüş kanalı** — bağımsız ikinci görüş için en ucuz kapı (ücretsiz katman + sıfır kurulum). → `§4.2`
6. **Ölç, sonra genişlet** — yerele devredilecek her alt görev **önce ölçülür**. Tahminle devretme. → `§1.8`

**Rol → model eşlemesi:** üst orkestratör ve kanon kararları Opus'ta değişmez · **hakem/denetçi/çelişki kapısı farklı sağlayıcı ve farklı aileden** · işçi ve üretici Sonnet · mekanik iş (sınıflandırma, etiketleme, commit mesajı) Haiku, sonra yerel model **ölçülerek** · gömme ve indeksleme yerel · gizli veriye dokunan iş yerel · **ajanik kodlama yerelde YAPILMAZ**. → `§1.8`

**Hangi iş nereye — tek kural:** *çıktı token'ı binlerle ölçülüyorsa hızlı çıkarıma, kimse beklemiyorsa batch'e, geri kalan her şey Claude'da kalır.* → `§2.6`

**Şu an ALINMAZ, gerekçeli:** ölü araç · yerleşik yeteneği tekrarlayan worktree yöneticisi · onunla aynı işi yapan ikinci araç · durmuş ve MCP'siz araç · Claude Code'un iki ikizi · ana döngü için hızlı çıkarım sağlayıcıları · tedarik zinciri emsali olan self-host geçit. → `§4.4`

**⚠️ İki güvenlik uyarısı — bunlar karar değil, bilgi:**
- Başka bir ajanı **bu depoda** açarsan Dilim-1 kilidi **yoktur**, ve izin bloğunu elle çevirirken **glob anlambilimi sessizce farklıdır**. → `§3.2`
- Worktree'ler **kaydedilmiş izin onaylarını paylaşır** ⇒ birinde verilen kalıcı onay hepsini bağlar. → `§3.6`

**Ve yeni bir yön (K46'dan):** `claude mcp serve` ile Claude Code'un **sunucu tarafında** durduğu bir kurulum denenmedi. Protokol yönü artık bir kısıt değil **tasarım kaldıracı** olduğuna göre, bu denenmeye değer. → `§5`

---

## 5. Kontrol

*Bu raporu okuduktan sonra şu üç soruyu cevaplayabiliyor musun?*

1. **"Denetçi başka model olsun" kararını verdin. Hangi ölçüt "başka model"i yeterli kılmıyor, ve bu denetçiden **beklememen** gereken şey ne?**

2. **Hızlı çıkarım sağlayıcısı 4 kat hızlı decode veriyor. Bu üstünlüğün senin ana döngünde ölçülemez hâle gelmesinin üç ayrı sebebi ne — ve bu üstünlüğün gerçekten işe yaradığı tek iş sınıfı hangisi?**

3. **Bu depoda ikinci bir terminal ajanı açacaksın. Açmadan önce kontrol etmen gereken iki şey ne, ve neden ikisi de "sessiz başarısız" sınıfında?**
