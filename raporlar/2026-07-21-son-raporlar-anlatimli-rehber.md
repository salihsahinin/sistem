# Son Günlerin Raporları

> 17–21 Temmuz 2026 · JARVIS çalışma günlüğü · sana sade dille anlatan rehber

Bu belge, son birkaç günde yazdırdığın **22 raporu** teknik olmayan bir dille sana anlatıyor. Her rapor için dört soruya cevap veriyorum: **ne sordun**, **özünde ne çıktı**, **hangi karar/öneri oluştu** ve **neden önemli**. Amaç, o günlerin kafandaki resmini tek oturuşta geri getirmek — dosyaları tek tek açmadan.

Kısaltmaları ve sürekli geçen terimleri (m.16, atlas, ingest, Katman-1/2, CC/Cowork/Fable...) her raporda tekrar açıklamıyorum; hepsi belgenin sonundaki **Ortak Sözlük** bölümünde toplu duruyor. Bir rapora özel, nadir bir terim varsa onu o raporun altında kısaca not düştüm.

---

## Büyük resim: bu günlerde neyin peşindeydin

Raporlar dağınık görünse de aslında **üç ana damarda** akıyor:

- **Kendini otomatikleştirmek (skill damarı).** Tekrar tekrar aynı şekilde tarif ettiğin işleri (karar verme, araştırma koşma, çelişki kontrolü) "skill" denen yeniden kullanılabilir modüllere dönüştürme fikri. Nasıl üretilir, nasıl seçilir, nasıl kendi verinden madenlenir — hepsi bu damarda.
- **Altyapıyı tasarlamak (mimari damarı).** JARVIS'in belleği, pointer sistemi, kontrol paneli/arayüzü, gece çalışması, ekip liderleri, oturumlar arası süreklilik. "Nasıl büyürüz de boğulmayız" sorusu.
- **Zemini sağlamlaştırmak (felsefe + öğrenme damarı).** Tüzük kurallarını Wittgenstein/Russell gibi mantık felsefesine oturtma, bir okuma listesi çıkarma; ve paralel öğrenme derslerin (token ekonomisi, uzun bağlam).

Ve neredeyse her raporda **aynı sonuç deseni** tekrarlıyor — o kadar ki bir imza haline geldi:

> "Şimdi büyük bir şey inşa etme. Önce ölç. Kanıt gelince en küçük eklemeyi yap. Geri-alınabilir olanı önce dene."

Ajanların karşıt-görüş (antitez) koşumları defalarca senin fikirlerini *çürütmedi* ama *kapsamını daralttı* ve çoğu şeyin "zaten tüzükte var" olduğunu gösterdi. Bu, dağınıklık değil; olgunlaşma işareti.

---

## 17 Temmuz — Skill'ler, yüzeyler ve otomasyon vizyonu

#### Skill'i bir sisteme dökmek

### Bir "skill" nasıl üretilir — metodoloji notları
Kaynak: `raporlar/2026-07-17-skill-nasil-olusturulur.md`
- **Ne sordun:** Tekrar eden iş kalıplarını (örneğin karar-verme hattını) skill'e çevirmek istiyorsun; bu skill'lerin ve özellikle skill *kombinasyonlarının* doğru nasıl üretileceğini araştırdık.
- **Özünde ne çıktı:** Bir skill aslında tek bir `SKILL.md` dosyası: üstte "ne zaman tetiklenir" açıklaması, altta emir kipiyle adımlar. İki kritik nokta var. Birincisi, skill'i tetikleyen şey açıklama metnidir — "ne yapar + ne zaman kullanılır", hatta "şu durumda KULLANMA" net yazılmalı. İkincisi sezgiye aykırı üretim sırası: önce doküman değil, **önce test (eval)** yazılır; skill'siz deneyip boşluğu görürsün, sonra en küçük gövdeyi yazarsın. Commit gibi geri-alması zor adımlar ayrı bir skill'e konur ve kendiliğinden çalışması kapatılır — "kazara commit atmasın" endişenin koda dökülmüş hali.
- **Karar/öneri:** Karar yok, ama net tasarım: `karar-hatti` gibi bileşik işler tek dev skill olmamalı; küçük çocuk-skill'ler + onları sırayla çağıran bir orkestratör olmalı. Her skill yayına girmeden test edilmeli.
- **Neden önemli:** K-016 kartının (skill üretim hattı) somut yol haritası. Tekrarlayan kalıplarını güvenli, denetlenebilir otomasyona çevirmenin temeli.
- **Terimler:** *eval* = skill'in işe yarayıp yaramadığını ölçen test senaryoları; *progressive disclosure* = bilgiyi kademeli açma (önce özet, tetiklenince gövde); *orkestratör* = küçük skill'leri sırayla çağıran koordinatör.

### Tekrar eden işlerin envanteri — skill fikir kutusu
Kaynak: `raporlar/2026-07-17-skill-fikri-kutusu.md`
- **Ne sordun:** "Defalarca aynı şekilde tarif ettiğim bağlam-kümelerini bir fikir kutusunda topla, örnek skill önerileri ver."
- **Özünde ne çıktı:** Önce bir kural önerildi: senin tekrar tekrar aynı kalıpla tarif ettiğin işler otomatik "skill adayı" sayılsın; bir skill'in değeri kabaca `tekrar sıklığı × elle yapma maliyeti`. Altı iş kalıbı tespit edildi (3-model karar üretimi, dış tarama/atlas, çelişki kontrolü, talimatı mantığa çevirme, damıtma/arşivleme, vardiya teslimi). Üçü için tam skill iskeleti çizildi.
- **Karar/öneri:** İlk üretilecekler `karar-modeli` ve `atlas-kosum` (o gün elle en çok yapılan ikisi). Kayıt/commit adımı ayrı `/karar-kaydet`'e konmalı. Her yeni skill 20-sorgulu tetik testinden geçmeli.
- **Neden önemli:** Bu kutu K-016'nın besleme kaynağı oldu — ve bu iki skill (`karar-modeli`, `atlas-kosum`) sonradan gerçekten üretildi. Yani bu rapor doğrudan üretime döndü.

#### Yüzey tutarlılığı ve otomasyon vizyonu

### CC oturumu Cowork gibi nasıl açılır — okuma sırası + yetki
Kaynak: `raporlar/2026-07-17-cc-okuma-sirasi.md`
- **Ne sordun:** "CC'den de Cowork'teki gibi konuşabilmem için bir okuma sırası mı yapsak?" Yani CC oturumunda da Carvis'in aynı bağlam ve kişilikle açılmasını istiyorsun.
- **Özünde ne çıktı:** Önemli bir netleştirme: Cowork ile Claude Code ayrı ürünler; ikisi de CLAUDE.md okur ama Cowork, Claude Code'un hook/ayar sistemini çalıştırmaz. Asıl kavramsal ayrım: istediğin şey *yetkinlik* tutarlılığı (her yüzeyde aynı Carvis, aynı bilgi) — bu doğru; ama bunu *yetki* tutarlılığıyla karıştırmamak lazım. Yetkinlik her yerde aynı olmalı, ama yetki (kanon yazma hakkı) yüzeye göre daraltılmalı ve ajan bunu kendi kendine yükseltememeli.
- **Karar/öneri:** Okuma sırası için SessionStart hook önerildi ("mimari, talimattan güçlüdür — hook unutmaz"). Yetki için yapısal kilit: CC/web yüzeyinde `core/`, `CLAUDE.md`, tüzük yazımı "deny", git push "ask".
- **Neden önemli:** Bu rapor doğrudan uygulandı — CLAUDE.md'deki güncel m.41 satırı ("SessionStart hook her CC açılışında kapsül+pano+yetki-bandı enjekte eder") bu önerinin hayata geçmiş hali. Nitekim bu oturum da o hook'la açıldı.
- **Terimler:** *macaroon / daraltılmış-yetki* = ana kimliğin her yüzeyde kısıtlı bir kopyasını verme; *confused-deputy* = düşük yetkili yüzeyin, yüksek yetkili ajanı kandırıp yasak iş yaptırması riski.

### Sesle ve telefondan geliştirme vizyonu — mimari + 3 model
Kaynak: `raporlar/2026-07-17-otomasyon-vizyon-mimarisi-3model.md`
- **Ne sordun:** Nihai hedefin ("LoL oynarken konuşarak, seyahatteyken telefondan senkron geliştirme") için hazır çözümlerin taranması ve bu mimariyi hangi sırayla kuracağımızın 3 modelle sunulması.
- **Özünde ne çıktı:** Vizyon üç katman: L1 sesle-kod, L2 mobil-süreklilik, L3 telefondan-sesle. Ana bulgu: **mobil-süreklilik bugün büyük ölçüde hazır** — Remote Control, Routines, Cowork web+mobil gibi resmi araçlar var ve JARVIS'in git tabanlı kapsül devri zaten sağlam bir taban. Ses ise en riskli ve en son gelecek katman; oyunda asıl darboğaz gecikme değil "pencere odağı" (tam ekran oyun sesi yutar), çözümü ses kanalını ayrı cihaza taşımak.
- **Karar/öneri:** Öneri = Model B (ölçüm-önce omurga), A'nın "bedavayı önce al" sırası ve C'nin "gözetimsiz adımdan önce güvenlik kapısı" katkısıyla harmanlanmış. İlk adımlar: L2'yi "mobil köprü protokolü" olarak yaz (ucuz), ses için ölçümlü küçük bir deneme, otomasyondan önce PreToolUse güvenlik kapısı.
- **Neden önemli:** En büyük uzun-vadeli hedefinin bugün ne kadarının ulaşılabilir olduğunu netleştiriyor ve K-009 (otomasyon) açılışına hazır soru listesi bırakıyor.
- **Terimler:** *WER* = ses tanımanın kelime hata oranı; *triangülasyon* = birbirine zıt modellerin aynı sonuçta buluşması = yüksek güven; *PreToolUse hook* = her araç çağrısından önce izin ver/reddet/sor diyen güvenlik katmanı.

### Dünkü CC tartışmalarının haritası (dizin)
Kaynak: `raporlar/2026-07-17-cowork-CC-tartisma-INDEX.md`
- **Ne sordun:** CC tarafında açtığın bir dizi tartışma raporunu tek yerden bulabilmen için içindekiler/harita.
- **Özünde ne çıktı:** 16 civarı rapor tek tek özetlenip dört kümeye ayrılıyor (skill üretimi, CC yüzeyi, otomasyon vizyonu, kararlar konsolu). Hepsi tartışma/aday; hiçbiri kanona yazılmadı. Ayrıca önemli bir kural netleşti: "çift atlas" dediğin şey = bir tez + onun tam zıttını savunan bir antitez.
- **Karar/öneri:** Karar yok — bu bir navigasyon dosyası. Somut çıktı: dış araştırma şeritlerinin kapandığının ilanı ve "çift atlas = tez + antitez" tanımının netleşmesi.
- **Neden önemli:** Bir oturumda üretilen çok sayıda dağınık raporu tek erişim noktasında toplayıp açık soruları listeleyerek, sonraki karar oturumunun gündemini hazırlıyor.

#### Öğrenme

### Öğrenme dersi P1: Token ekonomisi — bağlam bir maliyettir
Kaynak: `ogrenme/dersler/2026-07-17-P1-token-ekonomisi.md`
- **Ne sordun:** "Günaydın, öğrenme" ile başlattığın paralel öğrenme şeridinin dersi. Konu: modele verilen bağlamın neden para/işlem maliyeti ürettiği.
- **Özünde ne çıktı:** Bağlam uzadıkça maliyet kareyle (n²) büyür; girdi ve çıktı ayrı fiyatlanır; tekrar eden başlangıç (prefix) önbelleğe alınıp ucuza okunabilir — ama başlangıç değişirse önbellek bozulur, o yüzden açılış kararlı tutulmalı. JARVIS'in pointer sistemi ve kararlı açılışı bu yüzden aslında birer **maliyet-mühendisliği aracı**. Ölçülmüş çarpıcı sayı: Türkçe metin İngilizceye göre ~**1.89×** daha fazla token yiyor. Senin katkın da kaydedildi: kararlı-açılış ile büyüyen wiki arasındaki gerilimi işaret ettin.
- **Karar/öneri:** Okuma sırası için Model B (kararlı-prefix) önerildi; nihai karar ana oturuma bırakıldı (öğrenme oturumu kanona yazmaz). Ders senin onayınla DONE oldu.
- **Neden önemli:** JARVIS'in tüm bilgi mimarisinin (pointer, katmanlı yerleşim, kararlı açılış) sadece düzen değil, aynı zamanda para/token tasarrufu olduğunu gösteriyor.

---

## 18 Temmuz — En yoğun gün: skill matematiği, mimari ve felsefe

Bu tek gün, belgenin en kalabalık bölümü (13 rapor). Üç damarda topladım.

#### Skill ve optimizasyon matematiği

### Yakınsayan skill-kombinasyon formülü ve kategorizasyon
Kaynak: `raporlar/2026-07-18-yakinsayan-formul-kategorizasyon.md`
- **Ne sordun:** "Davranışlarıma rastgele kombinasyon uygulayarak skill geliştireceğiz ama zamanla *yakınsayan* (kararlı bir sonuca oturan) bir formül olmalı; kaldıraç, tekrar eden talimatları doğru kategorize etmek."
- **Özünde ne çıktı:** Skill'leri körlemesine rastgele denemek yavaş ve garantisiz. Rapor iki fikri birleştiriyor: (1) talimatları tek uzun listede değil dört bağımsız eksende sınıflandırmak, arama alanını küçültür; (2) seçim için rastgele/genetik yerine "belleği ve olasılık modeli olan" istatistiksel yöntemler (Thompson Sampling gibi) kullanmak — bunların matematiksel olarak kanıtlı yakınsaması var. Ödül, kalite-token-zaman üçlüsünün dengeli birleşimi olarak tanımlanıyor; kalite eşiğin altına düşerse skor sıfırlanır (ucuza kaçıp kaliteyi feda etmeyi engeller).
- **Karar/öneri:** Karar yok. Öneri: 4-eksenli kategorizasyon iskeleti + bütçe-farkında istatistiksel seçim formülü. Senin "azalan deneme oranı" sezgin matematiksel olarak doğrulandı.
- **Neden önemli:** Tüzüğün m.35 (farklılaşma) tezinin matematiksel omurgası — skill üretimini "rastgele deneme"den "kanıtlı yakınsayan sisteme" taşıyor. En büyük risk olarak "durağan-olmama" (model/görevler değişince garantilerin bozulması) işaretlendi.
- **Terimler:** *facet/eksen* = tek hiyerarşi yerine bağımsız birkaç sınıflama ekseni; *bandit* = sınırlı denemeyle en iyi seçeneği bulma problemi; *regret/pişmanlık* = en iyi seçimle yapılan seçim arasındaki fark, zamanla sıfıra inerse sistem yakınsıyordur.

### Skill desenlerini eldeki veriden madenleme
Kaynak: `raporlar/2026-07-18-skill-desenleri-veriden-madenleme.md`
- **Ne sordun:** "Öğrenme desenleri gibi, eldeki tekrar eden verilerle skill desenleri de oluşturabiliriz; nasıl yapacağımızı araştır."
- **Özünde ne çıktı:** Öğrenme şeridinin "araştırmadan ders üretme" makinesini al, girdisini değiştir: dış araştırma yerine JARVIS'in kendi iç verisi (git-log, senaryo-defteri, raporlar). Tüm literatür aynı 3 adımda buluşuyor: tekrarı tespit et → soyutla → doğrula ve kütüphaneye ekle. Kritik kural: bir iş ancak üç sinyal birden varsa skill olur — yeterli tekrar VE korpusu gerçekten kısaltması VE ne aşırı-genel ne aşırı-özel bir şablon olması. Ve önemli bir ayrım: öğrenme dersleri *bilgi* üretir, skill'ler *çalıştırılabilir politika* üretmeli.
- **Karar/öneri:** Karar yok. Çıktı: JARVIS verisine uyarlanmış 7 aşamalı madenleme boru hattı. En kritik bulgu bir kanon riski: m.34'ün "katman şişince yeniden özütle" kuralı, aslında "her şeyi baştan yazınca detay kaybı" tuzağına düşebiliyor; çözüm, damıtmayı madde-bazlı *fark* (delta) olarak yapmak.
- **Neden önemli:** Bu rapor keşif tarafını (madenleme), yukarıdaki yakınsayan-formül raporu ise seçim tarafını verir; ikisi birleşince tam döngü: keşfet → soyutla → seç → dondur → geri-besle. JARVIS'in skill'lerini dışarıdan kopyalamak yerine kendi verisinden üretmesinin haritası.
- **Terimler:** *madenleme* = veriden tekrar eden desenleri otomatik çıkarma; *MDL (en kısa açıklama)* = bir skill'in, maliyeti dahil, korpusu gerçekten kısaltıp kısaltmadığının kanıtlanabilir ölçütü; *skill-sprawl* = kontrolsüz çoğalan, işe yaramayan skill birikimi.

### Kararlara "geri-alınabilirlik" notu eklemek ve planları sıralamak
Kaynak: `raporlar/2026-07-18-geri-alinabilirlik-plan-optimizasyonu.md`
- **Ne sordun:** "Geriye-dönük maliyeti (rework) önlemek için kararlarımıza geri-alınabilirliğini de not alalım; bu notlardan ileride faydalanıp planları önem sırasına dizeriz." Ayrıca 3 model istedin.
- **Özünde ne çıktı:** "Bu karar ne kadar kolay geri alınır" bilgisi tüzükte zaten örtük duruyor (m.31 pahalı-geri-almayı zaten sana bırakır); sen bunu açık, kayıtlı, plan-sıralayan bir alana çevirmek istiyorsun. En önemli bulgu: geri-alınabilirlik **iki ayrı işe** koşulur ve karıştırılmamalı — KAPI (kim onaylar, ertelenir mi) ve SIRA (ucuz/geri-alınabilir olanı önce yap). Geri-alınabilir kararlarda hızlı davran, geri-alınamazlarda en kötü durumu koru.
- **Karar/öneri:** Karar yok. Öneri: senaryo-defterine bir "Geri-alınabilirlik" alanı (iki-yönlü/tek-yönlü kapı + etki-alanı + geri-alma maliyeti) ve iki ayrı sıralama formülü. Bir uyarı da var: "erken iş her zaman ucuzdur" inancının ampirik desteği zayıf; rework'ü asıl azaltan şey geri-bildirim döngüsü ve tersinirlik tasarımı.
- **Neden önemli:** Karar disiplinini sezgiden temellenmiş kurala taşıyor; JARVIS'in zaten sahada yaptığını açık bir kurala çeviriyor.
- **Terimler:** *iki-yönlü / tek-yönlü kapı* = geri dönülebilir / dönülemez karar (Amazon'un Type-2/Type-1 ayrımı); *blast-radius* = yanlış çıkarsa etkileyeceği alanın genişliği; *LRM (son sorumlu an)* = bir kararı ertelemenin bir alternatifi öldüreceği son an.

### Planlanmış optimizasyon fikirleri — ertelenmiş iyileştirmeler kuyruğu
Kaynak: `raporlar/2026-07-18-planlanmis-optimizasyon-fikirleri.md`
- **Ne sordun:** "İleride optimizasyon gerektiğinde neler yapabileceğimizi konuştuk; bunlar için 'Planlanmış Optimize Etme Fikirleri' diye bir kutu oluşturalım."
- **Özünde ne çıktı:** Tüzük zaten "erken optimize etme, sorun çıkınca yap" (m.5) diyor; bu blok, ertelenmiş iyileştirmeleri kaybetmeden bir kuyrukta tutuyor. 14 madde (O1-O14) tek tabloda, her biri tetik-koşulu, kazanç ve maliyetle etiketli. Kritik ayrım: "taşıyan borç" (ertelendikçe her seferinde sürtünme biriktirir → erken tetiklenmeli) ile "saf spekülatif fikir" (beklerken bedava, çoğu asla gerçekleşmez → budanır).
- **Karar/öneri:** Karar yok. Çıktı: 14 maddelik optimizasyon-listesi + iki katmanlı tetik formülü + kuyruk-hijyeni kuralları (periyodik denetim, "drop = silme değil damga").
- **Neden önemli:** "Ne inşa edilecek" (skill kutusu) ile "ne zaman olgunlaştırılacak" (bu blok) sorularını ayırıyor; aynı anda çok sayıda fikri boğulmadan yönetmeni sağlıyor.
- **Terimler:** *POP* = bu raporun önerdiği "Planlanmış Optimizasyon" kutusu; *YAGNI* = "gerekmeyeni önceden yapma"; *cost-of-delay* = gecikmenin maliyeti.

#### Sistem ve mimari

### JARVIS arayüzü: çok sayfalı kontrol paneli ve "konuşarak inşa modu"
Kaynak: `raporlar/2026-07-18-jarvis-arayuz-cok-sayfa-mod.md`
- **Ne sordun:** Arayüz koşan ajanları/model/çaba/görev/kullanım tablosunu göstersin; hem ortak sayfalar hem sana özel sayfalar olsun; "Konuşarak İnşa Modu 1" farklı bir tasarım taşısın — yöntemini çift atlasla araştır.
- **Özünde ne çıktı:** Arayüz, tek bir veri kaynağının (git kayıtları + kullanım günlüğü) farklı sayfalara yansıması olarak tasarlanmalı; her sayfa aynı verinin bir görünümü. Koşan-ajan tablosu için sıfırdan bir şey kurmaya gerek yok — Claude Code zaten model/çaba/maliyet sinyallerini yayınlıyor, bunları bir günlüğe yazıp okumak yeter. "Konuşarak İnşa Modu" ise oyun oynarken bakılan sesli-öncelikli, tek bakışta okunan bir "ikinci ekran" gibi.
- **Karar/öneri:** Karar yok. Ama kendi antitezi net: gözlemlenebilirlik sayfasını **şimdi inşa etme, ertele** — çünkü izlenecek canlı ajan henüz yok. "Oyun oynarken ciddi kod yazma" iddiasını düşür; sesi sadece "fikir yakalama/triyaj" gibi kolay işlere daralt.
- **Neden önemli:** "Kontrol paneli" vizyonunu somutlaştırıyor ve iki fazla-uzanan iddiayı dürüstçe frenliyor.
- **Terimler:** *glanceable/calm arayüz* = 1-2 saniyede okunan, dikkat çalmayan yüzey; *JSONL* = her satırı ayrı JSON kaydı olan eklemeli günlük; *YAGNI* = ihtiyaç yokken inşa etme.

### Pointerlar-arası iletişim ve pointer türlerinin sınıflandırılması
Kaynak: `raporlar/2026-07-18-pointer-sistemi-iletisim-kategorizasyon.md`
- **Ne sordun:** "Veri arttıkça bağlam şişmesini önlemek için pointer sayısı artacak; pointerlar arasında bağ kurmayı kolaylaştıran bir sistem gerekiyor ve pointer türleri sınıflandırılabilir." Çift atlas + 3 model.
- **Özünde ne çıktı:** Notların birbirine bağlanması üzerine olgun literatür var (Zettelkasten, hub-notları, GraphRAG); JARVIS'in panosu ve wiki-indeksi zaten birer "hub-not". Çözüm: bağların **tiplenmesi** ("destekler / çürütür / genişletir / yerine-geçer" gibi adlandırılmış oklar), böylece sadece belirli ilişkiler üzerinden gezinilir.
- **Karar/öneri:** Karar yok. Öneri = tipli-bağ grafiği, mevcut wiki + git üstüne. Ama antitez daha da ileri gidiyor: şu an korpus zaten bağlam penceresine sığdığı için **belki hiç graf kurmaya gerek yok**; asıl değerli tek bağ türü `yerine-geçer` (denetlenebilirlik için). Özet: şimdi + tek-ajanken düz kal, ölç; ölçek + çok-ajan gelince minimum tipli bağ ekle.
- **Neden önemli:** JARVIS'in şişme-önleme omurgasının ölçek büyüdüğünde nasıl ayakta kalacağını çözüyor ve "erken soyutlama kurma" disiplinini pekiştiriyor.
- **Terimler:** *Zettelkasten* = fişli-not sistemi; *hub-not / MOC* = ilgili notları toplayan indeks-not; *embedding* = metnin anlamını temsil eden sayısal vektör (benzerlikle erişim sağlar); *holizm/atomizm* = anlam bütünden mi yoksa tek tek parçalardan mı gelir tartışması.

### Gece-araştırma sistemi ve JARVIS'i geceleri en iyi kullanma
Kaynak: `raporlar/2026-07-18-gece-arastirma-sistemi-kullanim.md`
- **Ne sordun:** İki şey: (1) geceleri yaptırdığın araştırma sonsuz olduğundan alanları öncelik-partisyonlarına ayır, her konuyu ne derinliğe kadar bildiğimizi takip et, belli noktadan sonra derin kaynaklara in, sonuç senin diline indirgensin; (2) JARVIS'i geceleri en iyi nasıl kullanırsın.
- **Özünde ne çıktı:** İki sezgin de bilimde olgun karşılıklara oturuyor. Sistem dört parça: öncelik sırası → kapsam-derinlik haritası → eskalasyon (yalnız belirsizlik kararı değiştiriyorsa derine in) → indirgeme (derin bulguyu önce-sonuç + sade dille sana çevir). Durma kuralı: bir sonraki adımın beklenen faydası maliyetini aşmıyorsa dur. "Gece" için en uygun işler düşük-etkili ve geri-alınabilir olanlar (araştırma, taslak); yüksek-etkili işler (main'e merge, para) gündüze ve senin onayına.
- **Karar/öneri:** Karar yok. Tasarım: gece = "gece öner, sabah onayla". Antitez iki düzeltme getiriyor: (1) "8 saatlik tek uzun koşum" yanlış birim — çok sayıda kısa, bağımsız, otomatik-doğrulanan iş kullan; (2) sonsuz araştırmanın freni "doygunluk" değil, sert bütçe + tur-tavanı olmalı.
- **Neden önemli:** Gece vardiyası fikrini somut, güvenli ve maliyeti kontrollü bir düzene çeviriyor; K-009 açılışının ön-koşullarını netleştiriyor.
- **Terimler:** *BLUF* = sonucu ilk cümlede verme; *VOI/bilgi değeri* = bir araştırmanın beklenen faydasının maliyetini aşıp aşmadığı; *blast-radius* = işin ters gitmesi halinde zararın büyüklüğü; *worktree* = deponun izole bir çalışma kopyası (gece işi main'e değmeden orada koşar).

### Oturum yaşam-döngüsü, Cowork↔CC senkronu ve senkron-skill
Kaynak: `raporlar/2026-07-18-seans-yasam-dongusu-senkron-skill.md`
- **Ne sordun:** "'Günaydın' ve 'gün-sonu' skill'lerini hem Cowork'ten hem CC'den senkron çalışacak hale getirip 'seans başla/bitir' gibi bir dile çevirebiliriz; senkronumuza yardımcı bir skill de olabilir."
- **Özünde ne çıktı:** Yeni ritüel icat etmeye gerek yok; mevcut set "çek → çalış → kontrol noktası → gönder" omurgasına diziliyor. Mimariyi belirleyen kritik gerçek: Cowork, Claude Code'un hook sistemini çalıştırmıyor; dolayısıyla iki yüzeyde de çalışan taşınabilir katman ancak **skill** olabilir, hook yalnız CC tarafında sigortadır. İki yüzey arası süreklilik, sohbet geçmişiyle değil, git'teki durum-kapsülünün "Sonraki ilk iş" satırıyla sağlanır.
- **Karar/öneri:** Karar yok. Antitez net: "seans başla/bitir" ritüelini tut ama bir *kontrol listesi* olarak — yeni bir komut dili (senk/nokta/odak gibi uydurma fiiller) icat etme, çünkü LLM doğal dili zaten anlıyor. Tek cümle: "Ritüeli tut (fiilsiz checklist), komut-dilini at, senkronu tek git-deposuna indirge."
- **Neden önemli:** İki çalışma yüzeyi arasında iş devrini bozmadan sürdürmenin mimarisini çiziyor; hangi parçanın skill, hangisinin hook olacağını netleştiriyor.
- **Terimler:** *drift / drift-repair* = işin planından sapması / sapmayı adlandırıp yeniden hizalanma; *ortak-zemin (grounding)* = "yaptım" demek yerine "şunu anladım, X varsaydım, doğru mu?" diyerek anlaşıldığını kanıtlama; *DSL* = işe özel komut dili.

### Ekip liderleri: görev dağılımı, kişisel hafıza ve ingest
Kaynak: `raporlar/2026-07-18-ekip-liderleri-gorev-hafiza-ingest.md`
- **Ne sordun:** "İleride ekip liderleri oluşturup kişiselleştireceğiz; bu liderler nasıl bir görev-dağılımına sahip olmalı, her lider için kişiselleştirilmiş hafıza + ingest nasıl kurulur?"
- **Özünde ne çıktı:** Ekip liderleri, Carvis (CEO) ile işçi-ajanlar arasında bir orkestratör katmanı olur; görev "ayrıştır → delege et → topla" biçiminde akar. Bir liderin yöneteceği ast sayısı, klasik yönetim bilimi ve Anthropic bulgularının şaşırtıcı biçimde örtüştüğü **3-5** civarında tutulur. Kişisel hafıza tam izolasyon değil "bölme" olmalı: kanon herkese ortak, rol-belleği özel. En değerli çıkarım: iki şeyi karıştırma — geçici ayrıştırma (iş anında alt-ajan açmak, bugün kanıtlı ve düşük-riskli) ≠ kalıcı, kişiselleştirilmiş lider (kanıt bekleyen, riskli).
- **Karar/öneri:** Karar yok. Diyalektik sonuç: geçici ayrıştırmayı bugün benimse; kalıcı-kişiselleştirilmiş-lider'i varsayılan yapma — ancak gerçek bir darboğaz ve testle kanıtlanmış kazanç birlikte doğrulanırsa "hak ettir". Uyarı: ajan-kanonu (m.30) bugün bloke olduğundan kalıcı-lider mimarisine kilitlenme.
- **Neden önemli:** JARVIS'in gelecekteki çok-ajanlı yapısını hazırlıyor ve "erken soyutlama cezası" en yüksekken kilitlenmemeyi öğütlüyor.
- **Terimler:** *orkestratör-worker* = üst-ajanın görevi bölüp işçi-ajanlara dağıtması; *span-of-control* = bir liderin doğrudan yöneteceği ast sayısı; *persona* = ajana rol/kişilik veren bellek; *held-out test* = ayrı tutulan veriyle bir iyileştirmenin gerçekten kazandırdığını kanıtlama.

#### Felsefi temel ve okuma

### Tractatus 5.5262 + Russell karşıtlığı → "temel önerme" mimarisi
Kaynak: `raporlar/2026-07-18-tractatus-temel-onerme-kesisim.md`
- **Ne sordun:** Wittgenstein'ın Tractatus 5.5262 maddesinin fotoğrafını verip "bunu zıt yönüyle (Russell gibi) 2 atlasla araştır; buradan tüzükteki 'temel önermeler' için nihai kesişimleri çıkar" dedin.
- **Özünde ne çıktı:** Önce çevirideki bir tuzak düzeltildi (parantez bir çıkarım değil, bir sayım ifadesi). Asıl gerilim: Tractatus "temel önermeler bağımsızdır" der ama "bir nokta aynı anda kırmızı ve yeşil olamaz" örneği bu bağımsızlığı çökertir — kitabı içeriden yıkan meşhur sorun. Russell ayrı bir yerden itiraz eder: tekil olguları saysan da "işte hepsi bu" demeden dünyayı betimleyemezsin. Raporun özü: bu yapı JARVIS tüzüğüyle birebir eşleşiyor — tüzük "formda Tractatus, yönetimde Russell/Quine".
- **Karar/öneri:** Karar yok. Merkezi tez dört-yollu bir eşleme: atomcu form → m.38, bağımsızlık sorunu → m.16 (çelişki-kapısı), kapanış/genellik sorunu → m.41 (taban kendini içeriden kapatamaz = Salih/Fable otoritesi), tek-temel riski → m.37 (karşıt-temel). Yani Tractatus'u çökerten iki varsayıma karşı tüzük zaten yapısal panzehir taşıyor.
- **Neden önemli:** m.16, m.38, m.41 ve m.37'nin neden *birlikte* gerekli olduğunu 20. yüzyıl mantık felsefesiyle açıklıyor — "tüzük sezgisel değil, temellenmiş" iddiasını güçlendiriyor.
- **Terimler:** *temel önerme* = daha basite indirgenemeyen, tek olgu ileri süren cümle (rapor bunu tüzük maddelerine benzetiyor); *renk-dışlama sorunu* = "aynı nokta hem kırmızı hem yeşil olamaz"ın, bağımsızlık varsayımını çökertmesi; *mantıksal atomizm* = dünyanın en küçük bağımsız olgulardan kurulu olduğu görüşü.

### Tractatus 6.321 (nedensellik = sınıf-adı) → ingest algoritma ailesi
Kaynak: `raporlar/2026-07-18-tractatus-ingest-nedensellik-aile.md`
- **Ne sordun:** Tractatus 6.321 fotoğrafını verip "bağlamı ingest etme şeklimizi 'nedensellik yasası' gibi düşünürsek, farklı modeller ve amaçlar için farklı ingest algoritmalarımız olur; bunu mantıksal olarak ZIT yönlerde (tez + antitez) atlasla araştır" dedin.
- **Özünde ne çıktı:** 6.321 der ki "nedensellik yasası" tek bir yasa değil, aynı biçimi paylaşan bir yasalar *ailesinin* ortak adı. Senin eşlemen oturuyor: JARVIS'in bağlam işleme yöntemi de tek evrensel algoritma değil, ortak bir disiplini paylaşan ama (model × amaç)'a göre farklılaşan bir aile. Tez tarafı bunu destekliyor (karar-için, üretim-için, öğrenme-için ingest gerçekten farklı olmalı). Antitez sert bir red-team yapıyor: N×M ayrı işlem hattı kurmak "boru hattı ormanı" ve bakım borcu yaratır; olgun yerler "tek altın yol" kurar. Sentez: **tek paylaşılan ingest-biçimi + bağlam-başına parametreler**; bir varyant ancak testle genellemesi kanıtlanınca ayrı biçime terfi eder.
- **Karar/öneri:** Karar yok. Sonuç cümlesi: "Naif tez (peşinen N×M ayrı hat) çürük; disiplinli tez (tek biçimden, ölçümle hak edilmiş, geri-alınabilir varyant) ayakta." Ayrıca bir uyarı: mühendislik kararını felsefi bir alıntının prestijinden türetme — 6.321 harita/retorik, asıl dayanak ölçüm olmalı.
- **Neden önemli:** Bir iç kanon-gerilimini açığa çıkarıyor (m.30b "her ajan farklı özütleme" ile m.21/m.34 "tek şema" yan yana duruyor) ve bunu "farklı algoritma = tek şemanın testle hak edilmiş parametreleri" diye uzlaştırıyor.
- **Terimler:** *ingest* = bağlamı modele işlenebilir biçimde içeri alma/özütleme; *tez/antitez/sentez* = bir görüş, zıddı ve birleşimi (iki atlas zıt yönde koşturuldu); *RAG* = modele dış bilgi getirme; *No Free Lunch* = her göreve uyan tek en iyi yöntem yoktur, yöntem göreve bağlıdır.

### idea-boost skill incelemesi — dış bir skill'den ilham notu
Kaynak: `raporlar/2026-07-18-idea-boost-skill-inceleme-tartisma-notu.md`
- **Ne sordun:** "Araştırma sonucunu ve yorumları Cowork'te tartışmak üzere rapor oluştur." Konu: GitHub'daki `idea-boost` adlı küçük açık-kaynak skill — art arda atılan yarım fikirleri 7 adımlı tek geçişte işleyip fikir-havuzuna tek girdi olarak kaydeden bir akış.
- **Özünde ne çıktı:** En güçlü itiraz: otomatik tetiği ("2+ hızlı mesaj") çok düşük eşikli, sıradan sohbette yanlış ateşler; ve en değerli adımı (mevcut notlara kaynak-işaretiyle bağlama) kaynak yoksa uydurma pointer üretir — kendi vaadini ihlal eder. Ana hüküm net: bu skill **kurulmaz, sadece ilham alınır** (V25 altın kuralı) — çünkü yedi adımının JARVIS'te zaten neredeyse birebir karşılığı var (topla=fikir-kutusu, bağla=pointer, itiraz=çelişki-kapısı...). Yani skill, Carvis'in elle yaptığı işin dışarıda bağımsız yazılmış hali.
- **Karar/öneri:** Karar yok (tartışma notu). İlham alınacak iki gerçek eksik: (1) itirazı karar katmanından fikir katmanına indir (kutuya giren her fikir bir satırlık itiraz notuyla girsin), (2) adlandırılmış bir seri-işleme mini-protokolü. Her ikisi de önce deneysel-damgalı başlar, kural-statüsü senin imzana kalır.
- **Neden önemli:** "Kaliteli hazır skill'lerden yalnız ilham alınır, kurulum bize aittir" ilkesinin ilk canlı uygulama vakası; ayrıca senin fikir-giriş disiplininin dışarıda bağımsız keşfedildiğini gösteriyor (tasarımların bilinen ailelere oturuyor).
- **Terimler:** *V25 (altın kural)* = hazır skill kurulmaz, sadece ilham alınır; *graceful degrade* = bir girdi eksikse çökmek yerine düzgünce atlama; *bank/bankalama* = fikri havuza tek girdi olarak kaydetme.

### Tractatus ayarında JARVIS-geliştirme okuma listesi
Kaynak: `raporlar/2026-07-18-jarvis-gelistirme-okuma-listesi.md`
- **Ne sordun:** "Tractatus ayarında, JARVIS'i geliştirirken işime yarayacak başka bir kitap alacağım; bu tarz kitapları araştır, gerekirse atlas koş, listele."
- **Özünde ne çıktı:** Bu bir okuma listesi. "Tractatus ayarı" = sadece iyi değil, *yapı-üretken* kitap: bir tasarım sorusuna (bellek, pointer, karar, ekip-lideri) yapısal-eşleme çıkarabildiğin, az temelden çok yapı üreten eser. İki soy tarandı: felsefe (Frege, Russell, Gödel, geç-Wittgenstein, Quine, Austin, Searle...) ve sistemler/bilim (Ashby, Wiener, Beer, Shannon, Simon, Meadows, Alexander, Pearl...). Her kitap için çekirdek fikir + JARVIS-ilgisi + zorluk verilmiş; ama bu eşlemeler Carvis'in yorumu, kesin atıf değil.
- **Karar/öneri:** Karar yok (kitap seçimi senin — değer/tercih kararı). Net tavsiye: tek kitap alacaksan **Philosophical Investigations (geç-Wittgenstein)** — çünkü Tractatus'la yaptığın işin ikinci yarısı (atomizmi yazarının kendisi çürütür) ve "aile-benzerliği / sabit-kategori karşıtlığı" son raporlarının felsefi kalbi. "Mühendislik" istersen sıradaki adaylar: Simon (Sciences of the Artificial), Pearl (nedensellik), Beer (VSM).
- **Neden önemli:** Tasarım kararlarına felsefi/sistemsel bir zemin sağlıyor ve seni tek bir satın-alma kararına indirgeyip her JARVIS-kavramını en çok konuşan kitapla eşleştiriyor.
- **Terimler:** *yapı-üretken* = az temelden çok türetilmiş yapı çıkarabilen eser; *VSM (Beer)* = her örgütün 5 özyinelemeli sistemden oluştuğu model (ekip-lideri katmanına eşlendi); *extended mind* = dışsal araç bilişsel role girince zihnin parçası olur ("beyin=wiki, hafıza=git log"un temeli).

---

## 19 Temmuz — Süzgeç ve uzun bağlam dersi

### Fable süzgeci: 17 CC raporunun gözden geçirilmesi
Kaynak: `raporlar/2026-07-19-fable-suzgec-17-rapor.md`
- **Ne sordun:** 17-18 Temmuz'da CC yan-oturumları 17 araştırma raporu üretmişti; bu belge onların hepsini tek tek "Fable süzgecinden" geçirip hangisinin bulgusunun kabul, hangisinin daraltıldığı ya da ertelendiği kararını veriyor. (Senin 07-19 emrin: her rapor ana-sıra denetiminden geçsin.)
- **Özünde ne çıktı:** Her rapora bir etiket verildi — KABUL / ŞERHLİ-KABUL / DARALTILDI / ERTELENDİ. Kritik ilke: hiçbir etiket "hemen inşa et" emri değil. Carvis kendi yetkisindeki kararları (skill kutusuna ayrı dosya, karar defterine geri-alınabilirlik alanı, CC'ye SessionStart hook...) burada damgaladı; yalnız senin verebileceğin kanon kararlarını ayrı bir "İmza Masası" listesine ayırdı. Bazı iddialar reddedildi: "sesle ciddi inşa" düştü (ses yalnız niyet-yakalama), graf/embedding altyapısı kurulmayacak (mevcut ölçekte düz pointer kazanıyor).
- **Karar/öneri:** 16 raporun her biri için verdict verildi; Carvis kendi yetkisindekileri o gün damgaladı, sana yedi maddelik öncelikli İmza Masası bıraktı (başında m.42 ajan-yetki kanunu).
- **Neden önemli:** Bu, yan-oturumların ürettiği ham fikir yığınının kanona kontrolsüz sızmasını engelleyen filtre — "öneri üretmek" ile "kanonu kilitlemek" arasındaki yetki ayrımını (m.41) fiilen uyguluyor.
- **Terimler:** *süzgeç* = yan-oturum raporlarının, ana-sıra + Fable koşarken kanona alınabilir bulgulara ayıklanması; *KABUL/ŞERHLİ/DARALTILDI/ERTELENDİ* = bulgu etiketleri; *İmza Masası* = yalnız senin karara bağlayabileceğin kanon maddelerinin bekleme listesi; *supersedes/yerine-geçer* = bir notun eskisinin yerini aldığını gösteren bağ.

### Öğrenme dersi P3: RoPE, uzun bağlam ve "ortada kaybolma"
Kaynak: `ogrenme/dersler/2026-07-19-P3-rope-context.md`
- **Ne sordun:** "Günaydın, öğrenme P3" ile üçüncü dersi başlattın; konu, dil modellerinin metindeki kelime sırasını nasıl kodladığı ve uzun metinlerde neden bilgi kaybettiği.
- **Özünde ne çıktı:** Model, kelimelerin yerini eski yöntemde sabit bir "konum tablosu"yla tutar; tablo bittiği yerde (ör. 1024. kelimede) çöker. **RoPE** denen yöntem bunun yerine kelime vektörlerini konuma göre döndürür, böylece model sadece kelimeler arası *göreli* mesafeyi görür. Uzun metinde iki büyük sorun var: **"ortada kaybolma"** (başı ve sonu iyi hatırlanır, ortası çukura düşer — U eğrisi) ve **"bağlam çürümesi"** (metin uzadıkça performansın tedrici bozulması). Bu üçünün birleşimi, JARVIS'te sıcak bağlamın neden ~200 satırla sınırlı tutulduğunun mekanik nedenini açıklıyor.
- **Karar/öneri:** JARVIS'in hafıza düzeni için "kısa çekirdek + pointer" modeli (Model B) önerildi — mevcut m.20/m.34 kurallarıyla zaten hizalı. Dersi "hepsini okudum, istendiği kadar anladım" diyerek onayladın, DONE oldu.
- **Neden önemli:** JARVIS'in "neden her şeyi belleğe yüklemiyoruz da kısa özet + adres kullanıyoruz" tasarımının artık deneysel değil, dil modeli davranışına dayalı mekanik bir gerekçesi var.
- **Terimler:** *RoPE (dönel konum gömme)* = kelime vektörünü konuma göre "saat ibresi gibi" döndürüp modele göreli mesafeyi öğreten yöntem; *lost-in-the-middle* = uzun metinde ortadaki bilginin kaybolması; *context rot* = metin uzadıkça performansın kademeli bozulması; *KV-cache* = bir sonraki dersin (P2) konusu, modelin daha önce hesapladığını saklayıp bütçe kazanması.

---

## 21 Temmuz — "Grill me": kendini sınatma mekanizması

### "Grill me" skill'i araştırması
Kaynak: `raporlar/2026-07-21-grill-me-skill-arastirma.md`
- **Ne sordun:** "Grill me" adlı skill'in ne olduğunu araştırmamı istedin; bu yan-oturum bir araştırma ajanıyla web ve repo taraması yapıp raporladı.
- **Özünde ne çıktı:** "Grill me" hem somut bir Claude Code skill'i hem de altındaki genel bir teknik. Somut skill, Matt Pocock adlı bir eğitmenin `github.com/mattpocock/skills` deposunda, MIT lisanslı ve viral olmuş; **Anthropic'in resmi skill'i değil**, topluluk kaynaklı ama resmi skill formatını kullanıyor. Mekanizma: hedefini (plan/karar/fikir) bir karar ağacı gibi modelleyip, **tek seferde tek soru** sorarak, çevreden bulunabilen "gerçekleri" sana sormadan bulup yalnız gerçek yargı gerektiren "kararları" sana bırakarak seni ısrarla sorguluyor; sen "anlaştık" demeden hiçbir şey inşa etmiyor. Yaratıcısı bunu "etkileşimli rubber ducking" (sesli düşünme) diye tanımlıyor; değeri ajanı akıllandırmak değil, tam da yavaşlamanın önemli olduğu yerde kasıtlı sürtünme yaratmak. Rapor bunun senin öğrenme şeridinle kesiştiğini gösteriyor: şerit bilinçle pasif-okumaya geçmiş ve "gerçek anlama ölçümü ertelendi" borcunu kendine yazmıştı — grill-me tam bu boşluğu dolduruyor.
- **Karar/öneri:** Rapor iki karar yüzeyi açıyor ama kilitlemiyor (senin işin): (1) pasif-okuma varsayılanını bozmadan üstüne "isteğe bağlı doğrulama geçişi" olarak grill-me eklemek; (2) ya Pocock'un skill'ini kurmak ya da K-016 eval-önce akışıyla JARVIS'e özel bir "sınav/grill" skill'i üretmek. Bugün bedelsiz kullanılabilecek yol: rapordaki hazır-yapıştır Türkçe şablon, bir derste hemen denenebilir. Uyarı: `.claude/` yazımı bu yan-oturumda kilitli olduğundan skill *kurulumu* ana-sıra/senin işin.
- **Neden önemli:** Öğrenme şeridinin bilerek ertelediği "gerçekten anladın mı" ölçümü boşluğuna doğrudan, hazır bir çözüm sunuyor; P3 dersindeki borçla birebir bağlanıyor.
- **Terimler:** *grill/grill me* = bir fikri ısrarlı, karşıt sorularla stres testine sokma ("sıkı sorguya çekme"); *fact vs decision* = ajan olguları kendi bulur, yalnız yargı gerektiren kararları sana sorar; *onay kapısı* = sen "anlaştık" demeden hiçbir şey uygulanmaz; *testing effect* = bilgiyi hafızadan aktif çekmenin, yeniden okumaktan daha kalıcı öğrenme sağlaması (grill-me'nin bilişsel temeli); *sycophancy* = modelin kullanıcıya hak verme eğilimi (bu yüzden "erken onaylama yok, kaynağa alıntı zorunlu" kuralı sert tutuluyor). Not: rapor, dayandığı çok yeni bir akademik makaleyi "akran değerlendirmesi görmemiş, ihtiyatlı oku" diye işaretliyor.

---

## Tekrarlayan temalar — bu günlerin özeti tek bakışta

- **"Şimdi değil, ölç, minimum ekle."** Neredeyse her raporun antitezi buraya çıktı. Fikirlerin yanlış değil; çoğu zaman ya erken ya da zaten mevcut sistemin içinde.
- **Tasarımların bilinen ailelere oturuyor.** Pointer sistemin Zettelkasten'e, karar disiplinin karar-teorisine, ekip-liderin yönetim bilimine, ingest fikrin bağlam-mühendisliğine denk düşüyor. Bu, "sağlam zeminde yürüyorsun" demek.
- **Yetkinlik ile yetkiyi ayırmak.** Her yüzeyde aynı Carvis (yetkinlik), ama yüzeye göre daraltılmış yazma hakkı (yetki). Bu ayrım hem CC okuma-sırası hem Fable süzgeci raporlarının ortak omurgası ve fiilen uygulandı.
- **Felsefe süs değil, temel.** Tractatus eşlemeleri tüzüğün "sezgisel değil, temellenmiş" olduğunu gösteriyor; okuma listesi de bir sonraki kitabı (Philosophical Investigations) bu işin devamı olarak işaret ediyor.
- **Skill'ler kendi verinden çıkacak.** Madenleme (keşif) + yakınsayan formül (seçim), skill'leri dışarıdan kopyalamak yerine kendi geçmişinden üretmenin tam döngüsünü kuruyor.
- **Öğrenme dersleri mimariyi doğruluyor.** P1 (token maliyeti) ve P3 (uzun bağlam) dersleri, JARVIS'in kısa-çekirdek + pointer tasarımının neden mecburiyet olduğunu mekanik olarak kanıtlıyor.

---

## Ortak Sözlük

Raporlarda sürekli geçen terimler ve kısaltmalar. (Her rapora özel nadir terimler ilgili bölümün altında.)

#### Kişiler ve yüzeyler
- **Carvis** — sen (Salih) CEO iken, şirketin CEO'su rolündeki asistan; bu belgeyi hazırlayan.
- **Cowork** — Fable modeliyle koşan ana çalışma yüzeyi; kanonun sahibi (ana-sıra).
- **CC (Claude Code)** — repoyu gören ama kanonu kilitleyemeyen yan-oturum; öneri üretir. Bu belge bir CC oturumunda hazırlandı.
- **Fable / Opus** — modeller; Fable ana oturumu, Opus çoğu yan-oturumu koşturur.
- **atlas** — bir konuyu derinlemesine tarayan araştırma ajanı/koşumu. **çift atlas** = biri tez, biri onun tam zıttını (antitez) savunan iki paralel şerit.
- **şerit** — paralel çalışan bir iş kolu (araştırma şeridi, öğrenme şeridi gibi).

#### Karar ve yetki
- **Katman 1 / Katman 2** — karar yetkisi seviyeleri. Katman 1 yalnız sana ait (kanon/kural, silme, para, yayın, değer tercihi). Katman 2 Carvis'e ait (yapar + kaydeder + commit'ler; itirazın = geri alma).
- **kanon** — resmi, onaylı kurallar (tüzük + core/ dosyaları); yalnız senin kararınla değişir.
- **İmza Masası** — kanona girmesi için senin imzanı bekleyen maddelerin listesi.
- **çelişki kapısı (m.16)** — bir yeni karar önceki bir kararla çelişiyorsa, karar alınmadan önce çelişki + artı/eksi + plan raporu sunulur.

#### Bilgi mimarisi
- **pointer (m.20)** — "1 satır özet + adres"; detay başka dosyada durur, gerektiğinde oraya gidilir. Bağlamı şişmeden tutmanın temel aracı.
- **ingest / özütleme** — ham bilgiyi (belge, rapor, kaynak) modele işlenebilir biçimde içeri alma.
- **damıtma** — bilgiyi öz haline sıkıştırma; commit etiketlerinde `[damıtma]` olarak geçer (`[icra]` = fiili iş).
- **durum-kapsülü** — "şu an neredeyiz + sonraki ilk iş" bilgisini tutan, üstüne yazılan devir dosyası; her oturumun ilk okuduğu şey.
- **pano** — iş kartlarının (aktif/bekleyen/bloke) tek bakışta görüldüğü tahta.
- **sıcak / soğuk katman (m.22)** — aktif iş sıcak bağlamda, uzak-ufuk soğuk katmanda pointer'la durur.
- **git-as-truth** — tek doğruluk kaynağı git; makine ölse bile durum git'te yaşar, oturumlar arası devir bununla olur.

#### Skill dünyası
- **skill** — belirli bir işi standart adımlarla yaptıran, yeniden kullanılabilir talimat paketi (`SKILL.md` dosyası + tetikleme açıklaması).
- **eval** — skill'in işe yarayıp yaramadığını ölçen test senaryoları; "önce eval, sonra gövde" kuralı.
- **hook** — oturum açılış/kapanışında (ya da araç çağrısından önce) otomatik çalışan deterministik script; yalnız CC tarafında var, Cowork'te yok.
- **orkestratör** — küçük skill'leri sırayla çağıran koordinatör skill.

#### Kartlar (pano iş kalemleri)
- **K-009** — otomasyon/otonomi kartı (gece senkron, otomatik koşum). **K-010** — canlı ajan sicili. **K-016** — skill üretim hattı ("önce eval" akışı). **K-019** — boş-vardiya bakım paketi. **K-020** — ölçüm/koşum altyapısı.

#### Sık geçen tüzük maddeleri
- **m.5** — sorun çıkınca optimize et, erken değil. **m.13** — tek flagship (PortRisk); canlı demoya kadar başka ürün inşa edilmez → "hiçbir rapor inşa emri değil" bundan. **m.30** — ajan-kanonu (şu an bloke). **m.31** — karar yetkisi (Katman 1/2). **m.34** — katmanlı ingest / bağlam-çökmesi yasağı. **m.35** — skill farklılaşma tezi. **m.37** — karşıt-temelli 3-model karar yöntemi. **m.38** — doğal dili mantık bağlaçlarına çevirme. **m.41** — yüzey yetkisi (CC yan-oturum, kanon yazamaz). **m.42** — ajan-yetki kanunu (aday).

#### Güven etiketleri
- **D / K / X** — kaynak güven damgaları: **D** = birincil kaynaktan doğrulandı, **K** = arama/ikincil (teyit gerekir), **X** = doğrulanamadı.
- **V-numaraları (V24, V25, V54...)** — fikir-kutusundaki numaralı kayıtlar/kurallar (ör. V25 = "hazır skill kurulmaz, ilham alınır").
- **⚑ dürüstlük bayrağı** — atlas raporlarının kendi belirttiği sınırlar (erişilemeyen kaynak, doğrulanmamış rakam vb.).
