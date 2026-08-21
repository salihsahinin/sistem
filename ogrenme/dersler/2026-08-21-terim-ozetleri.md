# Terim Özetleri — 36 başlık, her biri 5 cümle

*2026-08-21 · Salih'in verdiği liste · Carvis/Opus 5 · her madde tam 5 cümle.*

**Köken damgası:** `[K]` = bu oturumlarda konuştuk (derinliği değişir) · `[Y]` = bizde kaydı yok, genel bilgi.
Derin malzeme varsa satır sonunda adres verildi. Normalizasyon ailesi için ayrıntı: `ogrenme/dersler/2026-08-21-tablo-normalizasyonu.md`.

---

## A. Araçlar

### VS Code `[Y]`
Microsoft'un açık kaynak kod düzenleyicisi; Electron tabanlı olduğu için Mac, Linux ve Windows'ta aynı arayüzü verir. Gücü çekirdeğinden değil eklenti ekosisteminden gelir — Python, SQL, Docker, Git entegrasyonlarının hepsi eklenti olarak kurulur. Remote-SSH ve Dev Containers eklentileriyle kod uzak makinede ya da konteynerde çalışırken düzenleyici yerelde kalır; veri mühendisliğinde sık kullanılan düzen budur. Yerleşik Git arayüzü commit/branch/merge işlerini görselleştirir ama altta çalışan şey yine `git` komutlarıdır. Ağır IDE'lere (PyCharm, IntelliJ) göre daha hafiftir; karşılığında derin dil analizi ve refactoring araçları eklentiye bağımlıdır.

### DBeaver `[Y]`
JDBC sürücüleri üzerinden neredeyse her veritabanına bağlanan evrensel SQL istemcisi; PostgreSQL, MySQL, Oracle, Redshift, Snowflake, SQLite aynı arayüzden yönetilir. Şema ağacı, veri düzenleyici, ER diyagramı ve sorgu geçmişi tek pencerede toplanır — DBA aracı değil, geliştirici/analist aracıdır. Sorgu planını (`EXPLAIN`) görselleştirebilir; performans çalışmalarında planı okumak için ayrı araç açmaya gerek kalmaz. Community sürümü ücretsizdir; NoSQL kaynakları ve bazı bulut entegrasyonları ücretli sürümdedir. Kurumsal ortamlarda tipik kullanım, VPN üzerinden şirket veritabanına bağlanıp ad-hoc sorgu koşturmaktır.

### Claude `[K]`
Anthropic'in büyük dil modeli ailesi; bu projede Claude Code arayüzü üzerinden terminalde ve masaüstü uygulamasında çalışıyor. Sohbet kutusundan farkı, dosya okuma/yazma, komut çalıştırma ve alt-ajan başlatma yetkisinin olmasıdır — yani sadece metin üretmez, iş yapar. Davranışı `CLAUDE.md` gibi sözleşme dosyaları, skill'ler ve hook'larla belirlenir; bu repoda kural kaynağı kanon dosyalarıdır. Bağlam penceresi sınırlıdır, bu yüzden durumun dosyalarda tutulması (kapsül/günlük deseni) tesadüf değil zorunluluktur. Model seçimi işin ağırlığına göre değişir: ağır muhakeme üst modelde, tekrarlı işçilik alt modelde koşar.

### Slack `[Y]`
Kanal tabanlı kurumsal mesajlaşma aracı; iletişim kişiye değil konuya (kanala) göre organize edilir. Thread (konu dalı) mantığı, bir mesajın altındaki tartışmayı ana akıştan ayırır — kanalın okunabilir kalmasının tek yolu budur. Entegrasyonlar üzerinden CI sonuçları, alarm ve deploy bildirimleri kanala düşer; böylece operasyon iletişimiyle sistem olayları aynı yerde birleşir. Arama, kurumsal hafızanın fiilî deposudur: karar niye böyle alındı sorusunun cevabı çoğu şirkette eski thread'lerde durur. Bildirim ayarları disiplin gerektirir; varsayılan ayarlarla sürekli kesinti üreten bir araca dönüşür.

### Sublime Text `[Y]`
C++ ile yazılmış, çok hızlı açılan ve devasa dosyaları takılmadan gezen ticari metin düzenleyici. Çoklu imleç, `Goto Anything` (Cmd+P) ve güçlü regex arama-değiştirme özellikleriyle tanınır; log ve CSV gibi büyük düz metinlerde VS Code'dan belirgin biçimde hızlıdır. IDE değildir: derleme, hata ayıklama, dil sunucusu gibi işler eklentiyle (Package Control) sınırlı biçimde gelir. Lisans ücretlidir ama süresiz deneme sürümü çalışır. Tipik kullanım biçimi ana editör olarak değil, "şu 2 GB'lık dosyaya bakayım" aracı olarak yanınızda durmasıdır.

### OpenVPN Connect `[Y]`
OpenVPN protokolüyle şifreli tünel kuran resmî istemci uygulaması; makineyi mantıksal olarak şirket ağının içine taşır. Bağlandığında yerel makineye kurum ağından bir IP verilir, böylece dışarıya kapalı veritabanları ve iç servisler erişilebilir hâle gelir. Profil dosyası (`.ovpn`) sunucu adresi, sertifika ve şifreleme ayarlarını taşır; kimlik doğrulama genelde sertifika + kullanıcı/parola, çoğu kurumda ek olarak MFA ile yapılır. "Split tunnel" ayarında yalnız kurum trafiği tünelden geçer, "full tunnel" ayarında tüm internet trafiği kurumdan çıkar — hangisinin açık olduğu hem performansı hem gizliliği etkiler. Bağlantı koptuğunda açık veritabanı oturumları da düşer; uzun süren sorgularda bu, işin ortada kalmasının en sık sebebidir.

---

## B. SQL ve veritabanı temelleri

### SQL `[K]`
İlişkisel veriyi sorgulamak ve değiştirmek için kullanılan bildirimsel (declarative) dil: **ne** istediğinizi yazarsınız, **nasıl** bulunacağına motorun optimizer'ı karar verir. Yazım sırası (`SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY`) ile mantıksal işlem sırası farklıdır; motor önce `FROM`/`JOIN`, sonra `WHERE`, sonra gruplama, en sonda `SELECT` ve `ORDER BY` uygular. Bu yüzden `SELECT`'te verdiğiniz takma ad `WHERE`'de kullanılamaz ama `ORDER BY`'da kullanılabilir. Standart (ANSI SQL) ortak bir çekirdek tanımlar, ama her motor kendi lehçesini ekler — pencere fonksiyonları, `UPSERT` sözdizimi ve tarih fonksiyonları motorlar arasında farklıdır. Öğrenirken en verimli yol, sorguyu yazıp `EXPLAIN` ile motorun ne yaptığına bakmaktır; dilin kendisi kolay, plan okumak zordur.

### CTE (Common Table Expression) `[K]`
`WITH ad AS (SELECT …)` biçiminde tanımlanan, yalnız o sorgu boyunca yaşayan adlandırılmış ara sonuç. Asıl kazancı okunabilirliktir: iç içe geçmiş alt sorguları yukarıdan aşağı okunan adımlara çevirir. Aynı CTE birden çok kez referans edilebilir; bazı motorlar onu her seferinde yeniden hesaplar, bazıları (ör. materialize kararına göre) bir kez hesaplayıp saklar — performans farkı buradan doğar. `WITH RECURSIVE` biçimi kendi kendine referans vererek hiyerarşi gezinmeyi sağlar: bir taban sorgu, bir de kendini besleyen adım sorgusu ile ağaç/graf yapıları (organizasyon şeması, ürün ağacı) düzleştirilir. Özyinelemede durdurma koşulunu yazmak zorunludur; yoksa sorgu sonsuz döner.

### Upsert `[K]`
"Varsa güncelle, yoksa ekle" işleminin tek ifadede yapılması: PostgreSQL/SQLite'ta `INSERT … ON CONFLICT DO UPDATE`, MySQL'de `ON DUPLICATE KEY UPDATE`. Anlamı benzersizlik kısıtına bağlıdır — çakışma, bir `PRIMARY KEY` ya da `UNIQUE` indeks ihlali olduğunda tetiklenir; kısıt yoksa upsert de yoktur. Önce `SELECT` yapıp sonra `INSERT`/`UPDATE` seçmekten üstünlüğü atomikliktir: iki adım arasında başka bir oturumun aynı satırı yazması yarış koşulu üretir, upsert bunu tek işlemde kapatır. `MERGE` daha genel bir ifadedir (eşleşen/eşleşmeyen satırlar için ekleme, güncelleme ve silmeyi birlikte tanımlar) ve ambar yüklerinde tercih edilir. Veri hattı tarafında upsert, aynı partiyi iki kez koşturmanın veriyi bozmamasını sağlayan idempotentliğin en yaygın aracıdır.

### ACID `[K]`
Bir işlemin (transaction) taşıması beklenen dört garanti: Atomicity, Consistency, Isolation, Durability. **Atomicity** işlemin ya tamamen uygulanmasını ya hiç uygulanmamasını sağlar — yarıda kesilen para transferi diye bir şey olmaz. **Consistency** işlem bittiğinde tüm kısıtların (PK, FK, CHECK) hâlâ geçerli olmasıdır; kuralı veritabanı zorlar, uygulama koduna güvenilmez. **Isolation** eşzamanlı işlemlerin birbirinin yarım işini görmemesidir ve seviyelere ayrılır (read uncommitted → serializable); gevşettikçe hız artar, dirty/non-repeatable/phantom read riskleri sırayla açılır. **Durability**, commit dönen bir işlemin elektrik kesilse de kaybolmamasıdır ve pratikte write-ahead log (WAL) ile sağlanır.

### Primary key · Foreign key · Index `[K]`
**Birincil anahtar**, bir satırı tek anlamda belirleyen sütun(lar)dır; aday anahtarlar arasından seçilir ve seçilmeyenlere `UNIQUE` konmazsa tekrar sızar. **Yabancı anahtar**, bir tablodaki değerin başka tablodaki anahtara işaret etmesini zorunlu kılar; kaynaksız satır yazılmasını motor engeller (`FOREIGN KEY constraint failed`). **İndeks** ise bir kısıt değil erişim yapısıdır: genelde B-ağacı, sıralı tutulan bir kopya sayesinde motor tabloyu baştan sona taramak yerine (`SCAN`) doğrudan arama yapar (`SEARCH`). Anahtarlar doğruluk içindir, indeksler hız içindir — karıştırılmasının sebebi, çoğu motorun birincil anahtar için otomatik indeks oluşturmasıdır. İndeksin bedeli yazmadadır: her `INSERT`/`UPDATE` indeksi de günceller, o yüzden "her sütuna indeks" bir optimizasyon değil yavaşlatmadır.

### Partition · Cluster `[K]` *(bu oturumda ölçüm sınırı olarak geçti)*
**Bölümleme (partition)**, mantıksal olarak tek tabloyu fiziksel olarak parçalara ayırmaktır — genelde tarihe göre (`2026-01`, `2026-02` gibi). Kazancı **bölüm budamadır**: `WHERE tarih = '2026-01-15'` sorgusu diğer bölümlere hiç dokunmaz, taranan veri baştan küçülür. **Kümeleme (cluster/sort key)** ise bölüm içindeki satırların belirli bir sütuna göre sıralı yerleştirilmesidir; kolonsal depolarda bu, blok başına min/max damgalarının dar olmasını ve blokların atlanabilmesini sağlar. İkisi farklı sorulara cevap verir: bölümleme "hangi dosyaları hiç açmayayım", kümeleme "açtığım dosyanın hangi bloklarını okumayayım". Yanlış anahtar seçimi ikisini de işe yaramaz hâle getirir; ölçütü sorgunun `WHERE` deseni belirler, tablonun anlamı değil.

### Tablo normalizasyonu `[K]` → `2026-08-21-tablo-normalizasyonu.md`
Bir tabloyu, aynı gerçeğin birden fazla yerde yazılı olmasını ortadan kaldıracak biçimde daha küçük tablolara bölme işlemi. Ölçütü estetik değil matematikseldir: her bölme, **fonksiyonel bağımlılıklardan** (X → Y: X'i aynı olan iki satırın Y'si de aynı olmak zorunda) türetilir. Kural tek cümleye iner — `X → Y` varsa ve `X` o tablonun anahtarı değilse, `Y` gereksiz tekrar ediyordur ve bölünmelidir. Merdiven sırayla çıkılır: 1NF (hücrede tek değer), 2NF (bileşik anahtarın parçasına bağlılık yasak), 3NF (başka sıradan sütuna bağlılık yasak), BCNF (her belirleyici anahtar olmalı), 4NF (bağımsız iki çoklu gerçek ayrılır). Ödülü ölçüldü: normalize edilmiş şemada bir fiyat güncellemesi 1 satıra dokunuyor, düz tabloda 578 satıra.

### Query debugging ve performans optimizasyonu `[K]`
Başlangıç noktası sorgunun kendisi değil **sorgu planıdır**: `EXPLAIN` / `EXPLAIN ANALYZE` motorun hangi tabloyu tarayacağını (`SCAN`), hangi indeksi kullanacağını (`SEARCH`), join'i nasıl kuracağını ve satır sayısını nasıl tahmin ettiğini gösterir. En sık kök neden üçtür: eksik/yanlış indeks, istatistiklerin bayat olması (`ANALYZE` koşulmamış — tahmin bozulunca optimizer yanlış plan seçer) ve sorgunun indeksi kullanılamaz hâle getirmesi (`LIKE '%x%'`, sütun üzerinde fonksiyon, tip uyuşmazlığı). Ölçüm birimi süre değil **iş**tir: taranan satır/byte, okunan sayfa, spill (belleğe sığmayıp diske taşma) ve join'in build tarafının boyutu. Optimizasyon yaparken tek değişken değiştirilir ve tekrar ölçülür; iki değişikliği birden yapmak, hangisinin işe yaradığını ölçülemez kılar. En yaygın yanılgı "JOIN yavaştır" teşhisidir — nokta sorgusunda JOIN'in maliyeti mikrosaniyedir, yavaşlık genelde indeks eksikliğindendir.

---

## C. Ambar mimarisi

### Transactional DB ↔ Analytic DB (DWH) `[K]`
İşlem veritabanı (OLTP), çok sayıda küçük ve eşzamanlı yazma için tasarlanır: satır bazlı depolama, güçlü kısıtlar, kısa transaction'lar, milisaniyelik nokta sorguları. Analitik veritabanı (ambar/DWH) az sayıda ama devasa okuma için tasarlanır: kolon bazlı depolama, sıkıştırma, paralel tarama, saniyeler süren agregasyonlar. Şema hedefleri de zıttır — OLTP 3NF'e gider (tek gerçek, ucuz güncelleme), ambar denormalize boyutlara gider (ucuz tarama). Ambardaki tekrar tehlikesizdir çünkü ambar **kaynak değil türevdir**; bozulursa OLTP'den yeniden üretilir. Bu ayrımı somutlaştıran ölçüm bu oturumda yapıldı: aynı analitik iş yükü satır-deposunda 374 ms, kolonsal motorda 3.5 ms sürdü (~107×).

### OLTP ↔ OLAP `[K]`
OLTP (Online Transaction Processing) günlük operasyonun kendisidir: sipariş oluşturma, ödeme alma, stok düşme — kısa, sık, satır bazlı işlemler. OLAP (Online Analytical Processing) o operasyonun üstüne sorulan sorulardır: kategori × şehir kırılımında ciro, dönemsel trend, kohort davranışı. OLTP'de başarı ölçütü işlem/saniye ve gecikme, OLAP'ta taranan byte ve sorgu maliyetidir. Aynı sistemde ikisini birden koşturmak klasik hatadır: analitik sorgu OLTP'nin kilitlerini ve önbelleğini işgal eder, ikisi birden yavaşlar. Standart çözüm ayırmaktır — OLTP kaynak kalır, veri bir hatla ambara taşınır ve analiz orada yapılır.

### Data warehouse şemaları: star · snowflake · galaxy `[K]` *(galaxy `[Y]`)*
Üçünün de ortak çekirdeği **fact** (ölçülen olay: satış, tıklama) ve **dimension** (olayın niteliği: ürün, müşteri, tarih) ayrımıdır. **Yıldız şema** bir fact tablosunun etrafına denormalize boyutları dizer; sorgu tek seviye join yapar, analistin yazması ve motorun koşması en kolay biçimdir. **Kar tanesi (snowflake)** boyutları da normalize eder (ürün → kategori → departman); depolama azalır, join sayısı ve sorgu karmaşıklığı artar — genelde ancak boyut devasa ya da paylaşımlıysa tercih edilir. **Galaksi (fact constellation)** birden fazla fact tablosunun aynı boyutları paylaştığı yapıdır; "satış" ve "iade" fact'leri aynı `d_urun`/`d_tarih`'i kullanır, buna uyumlu boyut (conformed dimension) denir. Seçim ölçüldüğünde ortaya çıkan sonuç şuydu: kolonsal motorda kararın birimi tablo değil sütundur — düşük kardinaliteli sütunu gömmek satır başına ~0.3 byte, yüksek kardinaliteli sütunu gömmek ~3.1 byte.

### Medallion mimarisi (bronze · silver · gold) `[K]`
Veri hattını, veriyi olgunluk seviyesine göre üç katmana ayıran düzen; adı Databricks'ten gelir ama deseni motordan bağımsızdır. **Bronze** ham veridir: kaynaktan geldiği gibi, dokunulmadan, geçmişiyle birlikte saklanır — hatalı olsa bile saklanır, çünkü tek doğru kopyadır. **Silver** temizlenmiş ve entegre katmandır: tipler düzeltilir, tekilleştirme yapılır, kaynaklar ortak anahtarlarla birleştirilir, burada normalizasyon disiplini işler. **Gold** sunum katmanıdır: iş sorularına doğrudan cevap veren, denormalize, çoğu zaman önceden toplanmış tablolar/martlar. Katmanların değeri yeniden üretilebilirlikte yatar — gold bozulursa silver'dan, silver bozulursa bronze'dan üretilir, bu yüzden alt katmanlara asla elle müdahale edilmez.

### AWS Redshift `[K]`
Amazon'un yönetilen, MPP (massively parallel processing) mimarili analitik veri ambarı; veri düğümlere dağıtılır ve sorgu paralel koşar. Depolama **kolon bazlıdır**: sorgunun dokunmadığı sütunlar diskten hiç okunmaz ve tekrarlı değerler sözlük/RLE ile sıkıştığından tarama maliyeti düşer. İki tasarım anahtarı performansı belirler — **distribution key** (satırların düğümlere nasıl dağıldığı; yanlış seçim veri kayması ve düğümler arası trafik üretir) ve **sort key** (blok içi sıralama; blok atlamayı sağlar). RA3 düğüm tipinde hesaplama ve depolama ayrışır, depolama S3 tabanlı yönetilen katmana taşınır; ayrıca Serverless seçeneği kapasite yönetimini tamamen kaldırır. Yükleme deseni klasiktir: veri önce S3'e yazılır, sonra `COPY` ile paralel içeri alınır (`UNLOAD` ile geri yazılır).

### Redshift ↔ S3 (Spectrum, göl-ambar sınırı) `[K]`
S3, Redshift'in hem giriş kapısı hem uzun süreli deposudur: veri hattı çıktısını (genelde Parquet olarak) S3'e yazar, Redshift `COPY` ile paralel olarak içeri alır. **Redshift Spectrum**, veriyi hiç içeri almadan doğrudan S3 üzerindeki dosyalara SQL koşturmayı sağlar; harici şema Glue Data Catalog'da tanımlanır. Bu, sık sorgulanan sıcak veriyi ambarda, seyrek sorgulanan geçmişi S3'te tutan katmanlı bir maliyet stratejisi kurar. Spectrum'da performansın anahtarı dosya düzenidir: kolonsal biçim (Parquet), makul dosya boyutu ve S3 önek yapısına göre bölümleme — bunlar olmadan sorgu gereksiz byte tarar. Sınır şudur: Spectrum okuma içindir ve ambar içi tablolar kadar hızlı değildir; sıcak yol için veri yine içeri alınır.

### ETL ↔ ELT `[K]`
İkisi de aynı üç adımı içerir — Extract (kaynaktan çek), Transform (dönüştür), Load (hedefe yaz) — fark dönüşümün **nerede** yapıldığındadır. **ETL** klasik düzendir: dönüşüm ayrı bir işleme sunucusunda yapılır, ambara yalnız temizlenmiş sonuç yazılır; ambar depolaması pahalıyken mantıklıydı. **ELT** modern düzendir: ham veri önce ambara/göle yüklenir, dönüşüm ambarın kendi hesaplama gücüyle SQL olarak yapılır (dbt bu yaklaşımın en yaygın aracıdır). ELT'nin üstünlüğü, ham verinin saklanması sayesinde dönüşümün her zaman yeniden koşturulabilmesi ve hatanın geri alınabilmesidir — medallion mimarisi tam olarak bunun düzenidir. ETL bugün hâlâ iki durumda tercih edilir: hassas verinin ambara hiç girmemesi gerektiğinde (maskeleme öncesi) ve kaynak sistemin biçimi ambara doğrudan yüklenemeyecek kadar yabancı olduğunda.

### Apache Airflow `[Y]`
Veri hatlarını kod olarak (Python) tanımlayıp zamanlayan ve izleyen açık kaynak iş akışı orkestratörü. Temel birimi **DAG**'dır (yönlü çevrimsiz graf): görevler ve aralarındaki bağımlılıklar tanımlanır, Airflow sırayı ve paralelliği kendisi çözer. Mimarisi scheduler (ne zaman ne koşacak), executor/worker (işi koşan) ve metadata veritabanından (durum kaydı) oluşur; arayüz koşum geçmişini, başarısız görevleri ve yeniden deneme durumunu gösterir. Kritik kavramlar: `schedule` (cron ifadesi), **backfill** (geçmiş dönemleri sonradan koşturma), **idempotentlik** (aynı görevin iki kez koşmasının sonucu bozmaması) ve sensörler (dış koşulu bekleme). Airflow işi kendisi yapmaz, yaptırır — ağır dönüşümü ambara/Spark'a devretmek, Airflow'u yalnız orkestratör olarak kullanmak yerleşik iyi pratiktir.

### Microsoft Fabric `[Y]`
Microsoft'un veri hattı, ambar, göl, gerçek zamanlı analiz ve Power BI'ı tek SaaS çatısında birleştiren platformu. Depolama katmanı **OneLake**'tir: tüm iş yükleri aynı gölü ve Delta-Parquet biçimini paylaşır, böylece veri motorlar arasında kopyalanmak zorunda kalmaz. İçinde birden çok deneyim vardır — Data Factory (hat), Lakehouse (Spark tabanlı), Warehouse (T-SQL), KQL veritabanı (gerçek zamanlı) — hepsi aynı veriyi görür. Power BI tarafındaki **Direct Lake** modu, veriyi içe aktarmadan ya da DirectQuery'nin gecikmesine katlanmadan doğrudan Delta dosyalarından okur. Ayırt edici tarafı ürün değil paketlemedir: ayrı ayrı kurulan bileşenler yerine kapasite tabanlı tek faturalanan bir bütün sunar.

---

## D. Yazılım geliştirme pratiği

### Software Development (genel) `[Y]`
Yazılım geliştirme, kod yazmaktan çok **değişimi yönetme** disiplinidir; bir sistemin ömrü boyunca harcanan emeğin çoğu ilk yazıma değil sonraki değişikliklere gider. Bu yüzden okunabilirlik, test edilebilirlik ve geri alınabilirlik, zekice çözümlerden daha değerlidir. Çalışma döngüsü genellikle aynıdır: gereksinim → tasarım → uygulama → test → dağıtım → gözlem, ve gözlemden gelen bilgi tekrar başa döner. Veri mühendisliğinde bu döngünün farkı, çıktının yalnız kod değil **veri** olmasıdır — dolayısıyla testin konusu da veridir (şema sözleşmeleri, tazelik, satır sayısı, tekillik). İyi geliştirici ayırt edici özelliği, bir değişikliğin neyi bozabileceğini önceden söyleyebilmesidir.

### Agile metodolojiler `[K]` *(bizde masa kalemi olarak var)*
Uzun ve sabit planlar yerine kısa döngülerde çalışıp geri bildirimle yön düzeltme yaklaşımı; Agile Manifesto (2001) bunu dört değer ve on iki ilkeyle tanımlar. **Scrum** en yaygın çerçevedir: sabit uzunlukta sprint'ler, sprint hedefi, günlük kısa senkron, sprint sonunda gözden geçirme ve retrospektif. **Kanban** alternatif çerçevedir: sprint yoktur, iş sürekli akar, kontrol mekanizması **WIP limiti**dir (aynı anda kaç iş açık olabilir) ve ölçüt akış metrikleridir — throughput, cycle time, WIP, akış verimliliği. Metriklerin bir kısmı ölçülebilir ve dürüsttür (cycle time, throughput), bir kısmı tahmin oyununa dönüşür (story point, velocity) ve ekipler arası kıyaslamada yanıltır. Pratikte en çok işe yarayan tarafı törenler değil iki alışkanlıktır: işi küçük dilimlere bölmek ve her dilimi bitmiş (deploy edilebilir) hâle getirmek.

### SOLID `[Y]`
Nesne yönelimli tasarımda bağımlılıkları yönetmek için beş ilkenin baş harfleri. **S** (Single Responsibility) bir sınıfın değişmesi için tek bir sebep olmasını, **O** (Open/Closed) davranışın kod değiştirilmeden genişletilebilmesini ister. **L** (Liskov Substitution) alt sınıfın, üst sınıfın beklentilerini bozmadan onun yerine geçebilmesi; **I** (Interface Segregation) büyük arayüzler yerine kullanana özel küçük arayüzler demektir. **D** (Dependency Inversion) üst seviye mantığın somut ayrıntıya değil soyutlamaya bağlanmasıdır — veri tarafında karşılığı, iş mantığının "PostgreSQL"e değil "depo arayüzü"ne bağlanmasıdır. İlkeler amaç değil araçtır: hepsini birden uygulamak, çözdüğünden fazla dolaylılık üreten aşırı mühendisliğe dönüşebilir.

### Clean Code `[Y]`
Robert C. Martin'in kitabıyla yaygınlaşan, kodun **okuyan için** yazılması gerektiğini savunan pratikler bütünü. Somut kuralları vardır: anlamlı ve niyet belirten isimler, kısa ve tek iş yapan fonksiyonlar, yan etkilerin gizlenmemesi, yorum yerine kendini açıklayan kod, tekrarın (DRY) ayıklanması. Yorum konusundaki tez şudur — yorum çoğu zaman kötü ismin özrüdür; kalıcı olması gereken yorum "ne yapıyor" değil "neden böyle" açıklamasıdır. Kod incelemesi (code review) bu pratiklerin uygulandığı yerdir; asıl işlevi hata bulmak değil, kodun ikinci bir insan tarafından anlaşıldığını doğrulamaktır. Eleştirilen tarafı katı uygulanışıdır: her fonksiyonu 4 satıra indirmek, izlenmesi zor bir çağrı zinciri üretebilir — ölçüt kural sayısı değil, sonraki okuyanın işini kolaylaştırmaktır.

### TDD (Test Driven Development) `[Y]` *(bizde "eval-first" olarak benzer bir disiplin var)*
Testi koddan **önce** yazma pratiği; döngüsü kırmızı-yeşil-refactor olarak bilinir. Önce başarısız olan bir test yazılır (kırmızı), testi geçiren en basit kod yazılır (yeşil), sonra testler yeşil kalırken kod temizlenir (refactor). Asıl kazancı test kapsamı değil **tasarım baskısıdır**: önce testi yazmak, kodu dışarıdan kullanılabilir ve bağımlılıkları ayrıştırılmış olmaya zorlar. İkinci kazancı güvenli değişimdir — testler yeşilse refactor korkusuzca yapılır, bu da kodun zamanla çürümesini yavaşlatır. Her yerde uygun değildir: keşif amaçlı prototipte ve çıktısı belirsiz analitik işlerde önce test yazmak zorlaşır, veri tarafında karşılığı genellikle veri sözleşmesi testleridir (şema, tekillik, tazelik).

### Human in the loop `[K]` *(no-mistakes'in ask-user eskalasyonu bunun uygulaması)*
Otomatik bir sistemin belirli noktalarda kararı insana devretmesi; tam otonomi ile tam el işi arasındaki tasarım tercihidir. İyi kurulmuş bir HITL sisteminde insanın çağrıldığı an rastgele değil **kuralla** belirlenir: güven eşiği altındaki tahminler, geri alınamaz eylemler, maliyeti yüksek kararlar. İnsana sorulan şeyin karar verilebilir olması şarttır — bağlamı, seçenekleri ve her seçeneğin sonucunu göstermeyen bir onay ekranı, sorumluluğu devretmiş ama kaliteyi artırmamış olur. En bilinen başarısızlık biçimi **onay yorgunluğudur**: çok sık sorulan onaylar refleks hâline gelir ve gerçek riskli durum da körü körüne onaylanır. Bu yüzden ölçüt "insan ne kadar sık müdahale ediyor" değil, "insanın müdahalesi sonucu ne kadar değiştiriyor"dur.

### CI/CD `[K]`
**CI (Continuous Integration)**, her değişikliğin ana dala sık sık ve otomatik doğrulamayla katılmasıdır: push edildiğinde testler, linter ve derleme otomatik koşar. **CD** iki anlama gelir — Continuous Delivery (her değişiklik dağıtıma hazır hâle gelir, düğmeye insan basar) ve Continuous Deployment (testler geçtiğinde otomatik dağıtılır). Amaç hız değil **risk küçültmedir**: küçük ve sık değişiklikler, büyük ve seyrek sürümlerden daha kolay test edilir ve bozulduğunda daha kolay geri alınır. Tipik hat şu adımlardan oluşur: kurulum → lint → test → derleme/paketleme → staging'e dağıtım → duman testi → üretime dağıtım, aralarda onay kapıları. Veri tarafında karşılığı da vardır: dönüşüm kodunun testleri, şema değişikliği kontrolleri ve üretime çıkmadan örnek veri üzerinde koşum.

---

## E. Terminal, git ve sürüm kontrolü

### Mac/Linux terminal komutları `[K]`
Kabuk (zsh/bash), komutları çalıştıran ve çıktılarını birbirine bağlayabilen metin arayüzüdür; gücü tek tek komutlardan değil **birleştirilebilirliklerinden** gelir. Temel gezinme ve dosya işlemleri: `ls` (listele; `-l` ayrıntı, `-a` gizliler), `cd`, `pwd`, `cp`, `mv`, `rm`, `mkdir`, `find`. İçerik ve arama: `cat`, `head`/`tail` (`tail -f` canlı log), `less`, `grep` (desen ara), `wc` (say), `sort`, `uniq`, `cut`, `sed`, `awk`. Bağlama işaretleri: `|` bir komutun çıktısını diğerine verir, `>` çıktıyı dosyaya yazar (`>>` ekler), `&` arka plana atar; `man <komut>` ve `<komut> --help` kılavuzu açar. macOS BSD tabanlıdır, Linux GNU — bu yüzden `sed -i`, `date` ve `ls` bayrakları iki sistemde farklı davranabilir; taşınabilir betik yazarken bu fark tuzaktır.

### Git: branch ve merge `[K]`
Git, projenin tarihçesini commit'lerden oluşan bir graf olarak tutar; **dal (branch)** bu grafta bir commit'i gösteren hareketli bir etikettir, kopya değildir — bu yüzden dal açmak neredeyse bedavadır. Çalışma düzeni: `git switch -c <dal>` ile dal aç, işini commit'le, sonra hedef dala dönüp `git merge <dal>` ile birleştir. **Merge** iki dalın ortak atasını bulup değişiklikleri birleştirir; iki taraf aynı satırlara dokunmuşsa **çakışma (conflict)** çıkar ve çözümü insan yapar, git dosyaya işaretleri koyup bekler. Alternatif `git rebase`, commit'leri hedef dalın ucuna yeniden oynayarak düz bir tarihçe üretir; paylaşılmış dalları rebase etmek başkalarının tarihçesini bozduğu için kaçınılan bir hatadır. Uzak depoda karşılığı **pull request**'tir: dal karşıya gönderilir, incelenir ve onaylandığında ana dala merge edilir — bu oturumda PR #2 tam olarak böyle kapatıldı.

### Git CLI kurulumu · git playground `[Y]`
macOS'ta git çoğu zaman Xcode Command Line Tools ile gelir (`xcode-select --install`) ya da Homebrew ile güncel sürüm kurulur (`brew install git`); doğrulama `git --version` ile yapılır. İlk kurulumdan sonra kimlik ayarlanır (`git config --global user.name` / `user.email`), aksi hâlde commit'ler sahipsiz görünür. Uzak depo erişimi için ya SSH anahtarı (`ssh-keygen`, sonra anahtarı GitHub'a ekleme) ya da GitHub CLI (`gh auth login`) kullanılır; parola ile HTTPS erişimi artık desteklenmiyor. **Git playground** için en yaygın kaynak `learngitbranching.js.org`'dur: dalları ve merge/rebase işlemlerini görsel olarak canlandırır, komutu yazarsınız grafın nasıl değiştiğini görürsünüz. Yerelde denemek için ise tek satır yeter — boş bir klasörde `git init`, birkaç dosya ve dal açıp merge/conflict senaryolarını gerçek repo riski olmadan yaşamak.

---

## F. Makine öğrenmesi kenarı

### Sigmoid `[K]`
Herhangi bir gerçek sayıyı (0, 1) aralığına sıkıştıran S biçimli fonksiyon: **σ(x) = 1 / (1 + e^(−x))**. Sıfırda 0.5 verir, büyük pozitiflerde 1'e, büyük negatiflerde 0'a yaklaşır; bu yüzden çıktısı "olasılık" gibi yorumlanabilir ve ikili sınıflandırmanın (lojistik regresyon) son katmanında kullanılır. Türevi σ(x)·(1−σ(x)) biçiminde kendi cinsinden yazılır, bu da geri yayılımda hesabı ucuzlatır. Zayıflığı **doygunluktur**: uçlarda türev sıfıra yaklaşır ve derin ağlarda gradyan kaybolur, bu yüzden ara katmanlarda yerini büyük ölçüde ReLU almıştır. Softmax ile karıştırılmamalıdır: sigmoid her çıktıyı bağımsız değerlendirir (çok etiketli sınıflandırmaya uygun), softmax ise çıktıları birbirine bağlar ve toplamlarını 1 yapar (tek etiketli çok sınıflı sınıflandırma).

---

## Kapanış notu

`[Y]` damgalı 14 başlık bu oturumlarda hiç konuşulmadı; yukarıdaki özetler genel bilgidir, senin bağlamınla (staj ortamı, kurum araçları) doğrulanmadı. Derinleştirmek istediğin başlığı söyle — normalizasyonda yaptığımız gibi, terim terim ve ölçümlü kurabiliriz.
