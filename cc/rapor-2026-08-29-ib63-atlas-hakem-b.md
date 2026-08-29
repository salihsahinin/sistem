# HAKEM RAPORU — İB-63 Aile B (ajan-orkestrasyon çakışma pratiği)

## KÜNYE
- **Rol:** Maskeli Hakem B (üretici koşumların devamı değil; kimliğe değil İDDİA+KANIT'a bakar)
- **Tarih:** AS-OF 2026-08-29 · **Web:** KAPALI (yalnız verilen iki dosya + denetçi sondaj beyanı)
- **Girdiler:** `rapor-1.md` (TEZ, 45 iddia, 25 desen) · `rapor-2.md` (ANTİTEZ, 10 kırpılmış iddia üzerine ¬T)
- **Sondaj durumu (bağımsız denetçiden):**
  - **rapor-1: TAM GEÇTİ** — arXiv %19,8/%41,7/N=716 dokuz bileşeniyle, SQLite tek-yazar, GH Actions şemaları birebir.
  - **rapor-2: K-DÜŞÜŞ** — NFSv4 grace-period tırnaklı alıntısı ne RFC 8881'de ne atıf verilen blogda mevcut (özü RFC'de duruyor, alıntı kaynak-atamasız). Kural gereği rapor-2'nin TÜM bulguları K-damgalı. Tutan 6 sondaj: arXiv %26,8+%15,1 bileşenleri, Inngest 2025-06-06, GH #9252 personel kabulü, git lockfile.h "eski VEYA yeni".
- **K-kuralı uygulaması (bu raporda):** rapor-2'nin sondajla TEYİTLİ kalemleri normal ağırlıkta tartıldı; teyitsiz kalemleri ([arama-özeti] dahil) yalnız DARALTMA gerekçesi olarak kullanıldı, hiçbir kalem yalnız teyitsiz kanıtla DÜŞÜRÜLMEDİ. Aşağıda teyitsiz-kaynaklı her daraltma **(K)** ile işaretlidir.

---

## VERDİKT TABLOSU

| # | Kalem | Verdikt | Belirleyici kanıt |
|---|---|---|---|
| ① | Worktree izolasyonunun gerçek değeri | **DARALDI** | erteleme çekirdeği iki raporda ortak; "yapısal çoğunluk" yarısı DÜŞTÜ (%41,9 azınlık — sondaj-teyitli); .git yarışı fail-stop (lockfile.h — sondaj-teyitli) |
| ② | SQLite tek-yazar + kuyruk/busy_timeout | **SAĞLAM** | rapor-1 sondajı tam; karşı-yol (BEGIN CONCURRENT) K-damgalı VE rapor-2'nin kendi beyanıyla ana-hat dışı → hükmü değiştirmez, dipnot olur |
| ③ | Atomic-rename'in bayat-okuma kapsamı | **DARALDI** | "bayat-okumaya yeterli" alt-iddiası DÜŞTÜ: lockfile.h "old OR new" (sondaj-teyitli) — eski içeriği görmek bayat okumanın tanımı; mekanizma yırtık-okuma korumasına daraldı |
| ④ | Sıralama↔dışlama çift-ekseni + Inngest kapsamı | **DARALDI** | çift-eksen CI'da SAĞLAM (şema sondajı tam); "ajan platformlarında dışlama YOK" kategorik hükmü Inngest 2025-06-06 ile (sondaj-teyitli) daraldı — VAR ama eşit dağılmamış, teyitli örnek TEK |
| ⑤ | CI concurrency-group güvenilirliği | **DARALDI** | GH #9252 çift-koşum, personel-kabullü, kök-neden yayımsız (sondaj-teyitli); sıra-garantisi-yokluğu (K) yalnız daraltma katkısı |
| ⑥ | Yol-bazlı ayrık yazım + tek-birleştirici | **DARALDI** | yol-ayrımı yarısı karşı-kanıtsız + yapısal-çakışma verisiyle destekli; "tek-birleştirici her ölçekte" yarısı hacim-eşikli daraltma aldı (K: SubmitQueue, Mergify — satıcı-bayraklı) |

**Sayım: 1 SAĞLAM · 5 DARALDI · 0 DÜŞTÜ (kalem düzeyi) · 0 ÇELİŞKİLİ · 0 KARARSIZ.** Alt-iddia düzeyinde 3 DÜŞÜŞ (aşağıda "DÜŞEN" bölümünde).

---

## KALEM KALEM GEREKÇE + DARALTILMIŞ FORMLAR

### ① Worktree izolasyonu — DARALDI

İki rapor çekirdekte ANLAŞIYOR: worktree çalışma ağacı + index + HEAD'i ayırır, `.git`/refs/nesne deposu paylaşılır (git dokümanı + Claude Code + Codex, üç bağımsız birincil kaynak); dosya izolasyonu birleştirme-anı çakışmasını yok etmez, ERTELER. İzolasyonun çakışma oranına etkisini ölçen çalışma YOK — bu boşluğu iki taraf da beyan ediyor. Rapor-2'nin fail-stop daraltması sondaj-teyitli lockfile.h alıntısına oturuyor: paylaşılan `.git` üzerindeki yarış veri bozmaz, komut hatası üretir. Rapor-2'nin işaret ettiği pratik iş-kaybı vakaları (#55724/#47266) K-damgalı; suçu orkestratörün otomatik-silme davranışına atar — daraltma katkısı olarak alındı (K).

**DARALTILMIŞ FORM (kural taslağına aynen):**
> Worktree izolasyonu dosya-düzeyi çakışmayı ÇÖZMEZ, birleştirme anına ERTELER; değeri çalışma-alanı hijyeni ve yarım-iş karışmasının önlenmesidir. Paylaşılan `.git` üzerindeki eşzamanlı git yazımları veri bozmaz, fail-stop komut hatası üretir → git yazımlarına retry/backoff şart, worktree'yi otomatik silen temizlik başarısız commit'te ÇALIŞTIRILMAZ (K). Metinsel çakışma oranları bağlam-bağımlıdır: ajan-içi %19,8 / çapraz-ajan %41,7 (açık-kaynak, 2024-12–2025-07, top-10 depo %91,4 yanlılığı, çapraz N=115) — Jarvis'e sabit katsayı olarak TAŞINMAZ, yön göstergesi olarak taşınır. Yapısal çakışmalar (%41,9: modify/delete + add/add) azınlıktır ama sıfır değildir: ajanlar dosyanın varlığında bile anlaşamaz.

### ② SQLite tek-yazar hükmü — SAĞLAM

Rapor-1'in hükmü sondajdan tam geçti: WAL'da tek yazar; okurlar serbest; ağ dosya sisteminde çalışmaz; `busy_timeout` süre dolunca yine `SQLITE_BUSY` döner → kuyruklama uygulama işidir. Rapor-2'nin karşı-yolu (BEGIN CONCURRENT / OCC) sondaj-teyitli listede YOK, dolayısıyla K-damgalı; üstelik rapor-2'nin KENDİ beyanı hükmü kurtarıyor: ana hatta birleşmedi, dal derlemesi gerekir, Turso üretim-dışı, Bedrock bağı doğrulanamadı, "Jarvis için pratik sonuç değişmiyor". K-kuralı gereği teyitsiz kanıt düşürme yapamaz; burada daraltma bile ancak dipnot düzeyinde: hükme "ana-hat SQLite" niteleyicisi eklendi, işlevsel içerik değişmedi.

**GEÇERLİ FORM (kural taslağına aynen):**
> `veri/baglam.sqlite` üzerinde N ajan koşarken okurlar serbest, YAZAR TEKTİR (ana-hat SQLite, WAL dahil). Yazımlar tek uygulama-seviyesi kuyruktan geçer + `busy_timeout` ayarlanır; süre dolumu yine `SQLITE_BUSY` demektir, kuyruk sorumluluğu uygulamadadır. Veritabanı ASLA ağ dosya sisteminde tutulmaz. (Dipnot, K-damgalı: çok-yazarlı OCC yolu — BEGIN CONCURRENT — ana-hat dışında belgelidir; ana-hat birleşirse hüküm yeniden tartılır.)

### ③ Atomic-rename'in bayat-okuma kapsamı — DARALDI

Alt-iddia "bayat-okumaya karşı yeterli koruma" DÜŞTÜ ve düşüş sondaj-teyitli kanıtla: lockfile.h "guaranteed to see either the OLD contents or the new contents" — eski içeriği görmek bayat okumanın ta kendisidir. Not: rapor-1'in kendi gövdesi (iddia 19-21) bu sınırı zaten doğru çiziyordu ("yarım dosya penceresi oluşmaz" — yeterlilik iddiası kırpılmış iddia listesinin ürünü görünüyor); yani düşüş rapor-1'in gövdesini değil, keskinleştirilmiş formu vurdu. Rapor-2'nin ek delikleri: EXDEV/aynı-FS şartı ve fsync (her ikisi rapor-1'de de bağımsızca mevcut → çapraz-doğrulanmış), açık-fd'nin rename'i hiç görmemesi ve çökmede dizin-fsync gereği (K — yalnız daraltma katkısı).

**DARALTILMIŞ FORM (kural taslağına aynen):**
> Write-then-swap (hedefle AYNI dizinde geçici dosya → `rename`/`os.replace`) yalnız BÜTÜNLÜK garantisidir: okuyucu ya eski ya yeni TAM içeriği görür, yırtık/yarım okuma olmaz. TAZELİK garantisi DEĞİLDİR: eski içeriği görmek meşru sonuçtur; açık fd tutan uzun-ömürlü okuyucu takası hiç görmez (K). Şartlar: geçici dosya hedefle aynı dosya sisteminde; dayanıklılık için `flush()`+`fsync()` ayrı adım (çökme-dayanıklılığı için dizin-fsync — K). Bayatlığa karşı ayrıca sürüm damgası (hash/mtime) + koşullu yazma gerekir; bkz. çekirdek madde 4.

### ④ Sıralama↔dışlama çift-ekseni + Inngest'in gerçek kapsamı — DARALDI

Çift-eksenin CI'daki varlığı SAĞLAM: `needs`/`depends_on` (sıralama) ile `concurrency`/`resource_group` (dışlama) ayrı bildirimsel kavramlardır — GH Actions şema sondajı birebir tuttu, dört orkestratör tablosu birincil dokümanlı. Kategorik "ajan-platformlarında dışlama ekseni YOK" hükmü ise daraldı: Inngest Singleton Functions (2025-06-06) sondaj-teyitli — eksen en az bir ajan-orkestratöründe birinci-sınıf mekanizma olarak SEVKTE. Ancak rapor-2'nin "ÇÜRÜDÜ" hükmü de olduğu gibi alınamaz: AgentKit bağı ve CEL-anahtar/skip-cancel ayrıntıları [arama-özeti] (K), Restate/Temporal indirgeme örnekleri K-damgalı ve rapor-2'nin kendi teslimiyle çoklu-kaynak kilitlemede çöküyor. Cevap: eksen ajan-platformlarında artık VAR ama teyitli örnek TEKTİR ve eşit dağılmamıştır — Claude Code agent teams'te dosya-çakışması hâlâ mekanizmasız KURALDIR (rapor-1, birincil doküman).

**DARALTILMIŞ FORM (kural taslağına aynen):**
> Sıralama (bildirimsel, statik, döngüsüz DAG) ve karşılıklı dışlama (adlandırılmış kaynak grubu) iki AYRI eksendir ve olgun orkestrasyonda ikisi de açıkça bildirilir; tek-anahtara bölünebilir işte tek primitife indirgenebilirlik K-damgalı bir istisnadır ve çoklu-kaynak kilitlemede geçersizleşir. Ajan-platformlarında dışlama ekseni "yok" DEĞİL "eşit dağılmamış"tır: en az bir platformda (Inngest, 2025-06) birinci-sınıf; Jarvis'in kullandığı yığında (Claude Code agent teams) mekanizma değil kuraldır → Jarvis dışlamayı kendi katmanında KURMAK zorundadır; hazır tasarım (dışlama anahtarı + skip/cancel modu) örnek alınır (K), "hazırı temel al".

### ⑤ CI concurrency-group güvenilirliği — DARALDI

"Tek koşum garantisi" belgeli ve yaygın-pratik; ama sondaj-teyitli #9252 vakası (2021, `cancel-in-progress: false` altında çift-koşum, GitHub personelince kabul, kök-neden yayımlanmamış) "üretim-KANITLI mutlak mutex" nitelemesini kırıyor. Sıra-garantisi-yokluğu (#199398) K-damgalı — yalnız daraltma katkısı. Rapor-2'nin kendi teslimi de ölçülü: tek ve eski rapor, kalıcı/yaygın arıza kanıtı yok.

**DARALTILMIŞ FORM (kural taslağına aynen):**
> CI concurrency-group'u (GH `concurrency`, GitLab `resource_group`) pratik dışlama katmanıdır ama MUTLAK mutex sayılmaz: satıcı-kabullü, kök-nedeni yayımlanmamış bir çift-koşum vakası kayıtlıdır (GH #9252, 2021) ve sıra garantisi tanım gereği yoktur (K). Kritik dışlamada tek savunma hattı olamaz; her korunan iş İDEMPOTENT yazılır ve yazma anında sürüm/koşullu-yazma denetimiyle desteklenir.

### ⑥ Yol-bazlı ayrık yazım + tek-birleştirici — DARALDI

İki yarı ayrı tartıldı. **Yol-ayrımı yarısı:** rapor-2 açıkça "hiçbir karşı-kanıt bulamadım" diyor; üstelik sondaj-teyitli yapısal-çakışma verisi (%41,9) yol-düzeyi bölümlemenin çakışmaların büyük dilimini keseceğini destekliyor → bu yarı tam ayakta. **Tek-birleştirici yarısı:** yüksek hacimde seri kuyruğun darboğaz olduğu itirazı bütünüyle K-damgalı kaynaklara dayanıyor (SubmitQueue alıntıları [arama-özeti]; Mergify [çekildi] ama sondaj-teyitsiz VE satıcı çıkar-çatışması bayraklı; Hashimoto aktarımı yazarın kendi beyanıyla ölçüm değil hipotez) → düşürme yapamaz, hacim-eşikli daraltma yapar. Rapor-2'nin kendi teslimi: "düşük hacimde (Jarvis ölçeği) fark yok."

**DARALTILMIŞ FORM (kural taslağına aynen):**
> Yol-bazlı ayrık yazım alanları + tek-birleştirici, Jarvis ölçeğinde (tek depo, düşük hacim, tek karar verici) GEÇERLİ varsayılan desendir; yol-ayrımı yarısı karşı-kanıt almamıştır. Tek-birleştirici "her ölçekte seri kuyruk" diye yazılmaz: yüksek hacimde seri biçim belgeli darboğaz adayıdır (K: spekülatif paralel doğrulama literatürü, satıcı-bayraklı kuyruk ölçümleri) → kural hacim-eşiklidir; eşik aşımı bugünkü Jarvis için tetiklenmemiştir.

---

## HAYATTA KALAN ÇEKİRDEK
**Soru: Jarvis'te loop/pipeline eşzamanlılığı hangi mekanizmalarla korunmalı?**

1. **Önce bölümleme, sonra kilit:** Her eşzamanlı loop/pipeline/ajana AYRIK dosya-yolu yazım alanı tahsis edilir ve bu KURAL değil MEKANİZMA olarak zorlanır (harness yol-kapısı / worktree + yazım-yolu denetimi). Çakışmaların %84,4'ü kaynak kodda ve %41,9'u yapısal — bölümleme en büyük dilimi baştan keser (sondaj-teyitli veri).
2. **Worktree = hijyen, birleştirme = tek kapı:** Worktree yarım-işlerin karışmasını önler ama çakışmayı birleştirmeye erteler; tüm birleştirmeler TEK-birleştirici noktadan (sıralı, Jarvis hacminde seri yeterli) geçer. Paylaşılan `.git` yazımları fail-stop'tur: git yazımına retry/backoff sarılır, başarısız commit'te worktree otomatik SİLİNMEZ (K).
3. **`baglam.sqlite`: tek-yazar disiplini:** Yazımlar tek uygulama-seviyesi kuyruk + `busy_timeout`; timeout dolumu kuyruğa iade demektir, "tekrar dene ve geç" değil; DB asla ağ dosya sisteminde tutulmaz (sondaj-teyitli).
4. **Durum dosyalarında bütünlük + tazelik AYRI mekanizma:** Bütünlük için write-then-swap (aynı dizinde geçici + rename, gerekince fsync); tazelik için sürüm damgası (hash/mtime) + koşullu yazma — yazan taraf okuduğu sürümün damgasını taşır, damga eşleşmezse yazma REDDEDİLİR. Protokol ajanın hafızasına değil kaynağın kendisine konur; damga ajanın kendi iz kaydına değil dosyanın gerçek sürümüne bağlanır (kardeş-ajan yazımı da yakalansın diye — K).
5. **Dışlama adlandırılır ve kiralanır:** Loop/pipeline sınıfı başına adlandırılmış kilit/kira: TTL + sahip kimliği + yenileme + ölü-sahip süpürgesi; makinenin koyduğu kilit süpürülebilir, insanın (Salih'in) koyduğu kilit ASLA süpürülmez. Hiçbir tekil dışlama katmanına (CI concurrency-group dahil — #9252) tek başına güvenilmez: korunan iş idempotent yazılır.
6. **Sıralama ayrı eksendir ve statiktir:** Adım bağımlılıkları çalışma zamanında keşfedilmez; bildirimsel, döngüsüz DAG olarak (needs-benzeri) önceden yazılır. Dışlama grubu adı ayrıca ve bilinçli seçilir — yanlış ad dışlamayı ya çok geniş ya işlevsiz yapar.

---

## DÜŞEN / DARALAN

**DÜŞEN (alt-iddia düzeyi):**
- **"Çakışmaların büyük bölümü yapısal"** — DÜŞTÜ. Yapısal = %41,9 (modify/delete %26,8 + add/add %15,1), azınlık; çoğunluk (%57,6) satır-içi içerik. Her iki tarafta sondaj-teyitli. (Not: rapor-1'in gövdesi "yaklaşık %42" diye doğru yazmıştı; "çoğunluk" formu kırpılmış iddia listesinde keskinleşmiş.)
- **"Atomic-rename bayat-okumaya yeterli"** — DÜŞTÜ. Sondaj-teyitli lockfile.h alıntısıyla: eski-veya-yeni garantisi bayat okumaya izindir. Mekanizma yırtık-okuma korumasına daraltıldı (kalem ③).
- **rapor-2'nin NFSv4 grace-period tırnaklı alıntısı** — DÜŞTÜ (kaynak-atamasız; K-düşüş tetikleyicisi). Özü RFC'de dursa da alıntı kanıt statüsünde kullanılamaz; flock/NFS itirazının bu bacağı hükümsüz. flock'un NFS'te 2.6.12+ emülasyonla çalıştığı bilgisi AYRICA rapor-1'de bağımsızca mevcut (çapraz-doğrulanmış) — ama Jarvis tek-makine/yerel-disk olduğundan NFS ekseni bütünüyle kapsam dışı.

**DARALAN (kalem düzeyi — daraltılmış formlar yukarıda aynen):**
- ① Worktree: "izolasyon çözümü" → "erteleme + fail-stop + bağlam-bağımlı oranlar".
- ③ Atomic-rename: "bayat-okuma koruması" → "yalnız bütünlük; tazelik ayrı mekanizma".
- ④ Dışlama ekseni: "ajan-platformlarında yok" → "var ama eşit dağılmamış; teyitli örnek tek; Jarvis'in yığınında kurulmalı".
- ⑤ Concurrency-group: "üretim-kanıtlı mutex" → "pratik katman; idempotenlik + koşullu yazmayla desteklenir".
- ⑥ Tek-birleştirici: "her ölçekte" → "hacim-eşikli; Jarvis ölçeğinde geçerli".
- (rapor-2 yönünde) "dışlama ekseni iddiası ÇÜRÜDÜ" hükmü → tek teyitli örnekle ancak DARALTMA'ya yeter; "sıralama↔dışlama indirgenebilir" karşı-tezi K-damgalı ve çoklu-kaynakta kendi beyanıyla çöker.

**Hakem notu (kayıt):** rapor-2'nin K-düşüşü tek alıntının kaynak-atamasızlığından; raporun iç dürüstlük aygıtı ([çekildi]/[arama-özeti] ayrımı, kendi başarısızlıklarını beyan) aksi yönde güçlüydü — K-damgası kalite yargısı değil, teyit-statüsü yargısıdır. Kırpılan 35 iddia bu hakemlikte de İNCELENMEMİŞ sayılır; verdiktler yalnız 6 karar-taşıyan kalemi bağlar.

*Rapor sonu — Maskeli Hakem B · AS-OF 2026-08-29 · web kapalı, yalnız dosya-içi kanıt + denetçi sondajı.*
