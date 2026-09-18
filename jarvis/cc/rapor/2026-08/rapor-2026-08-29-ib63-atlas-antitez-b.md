# ANTİTEZ RAPORU — İB-63 Aile B (ajan-orkestrasyon çakışma pratiği)

**AS-OF: 2026-08-29** · Ajan: ATLAS (antitez rolü, açık devil's advocate) · Dil: Türkçe · Web: serbest

## 0. Kapsam ve kırpma beyanı

- Bana **yalnız iddialar** verildi; tez raporunun gövdesi verilmedi (kör antitez).
- **Kırpma:** 45 iddialık asıl listeden karar-taşıyan **10** iddiaya kırpıldı. Kırpmayı ben yapmadım, görev emriyle geldi. Sonuç: kırpılan 35 iddia için bu raporda **hiçbir hüküm yoktur** — "çürütülmedi" diye okunamaz, **incelenmedi**.
- Rolüm tek yönlü: her iddianın **değilini (¬T)** savunacak kanıt aradım. Bu rapor dengeli bir literatür taraması DEĞİLDİR; tezle eşleştirilip tartılması gerekir.

**Skor:** ÇÜRÜDÜ 2 · DARALDI 8 · ÇÜRÜTEMEDİM 0 · ARANMADI 0

**Alıntı güven notu:** Doğrudan `WebFetch` ile çekilen sayfalardan gelen tırnak-içi alıntılar `[çekildi]`, yalnız arama sonucu özetinden gelenler `[arama-özeti]` ile işaretlendi. `[arama-özeti]` olanlar ham kaynaktan birebir doğrulanmadı — kullanmadan önce çekilmeli.

**Erişim bayrakları:** ResearchGate ve ScienceDirect bağlantıları (Ghiotto ve ark. tam metni, Elsevier makalesi) **denenmedi** — paywall beklendiği için maliyet harcanmadı. arXiv sayfaları açıktı. 403 alınan sayfa olmadı.

---

## İDDİA 1 — Worktree izolasyonu çakışmayı ertelemekten ibarettir; %20-40 bandı; çakışmaların büyük bölümü yapısal

### HÜKÜM: **DARALDI** (iddianın ikinci yarısı çürüdü, birinci yarısı ayakta ve hatta güçlendi)

**Karşı-kanıt 1 — "büyük bölümü yapısal" YANLIŞ; yapısal olanlar azınlıkta.**
İddianın dayandığı ölçümün kendisi tersini söylüyor. arXiv 2607.04697 (gönderim 2026-07-06, revizyon 07-07), Bulgular bölümü:

> "specifically, modify/delete conflicts account for 26.8% (one agent has updated a file while the other has removed it) and add/add conflicts account for 15.1%" `[çekildi]`

26.8 + 15.1 = **%41.9**. Yani yapısal çakışmalar **azınlık**; kalan ~%58 satır-içi içerik çakışması. Aynı makalenin özeti bunu "nearly 42% of conflicts" diye yapısal olarak damgalıyor `[çekildi]`. "Büyük bölümü yapısal" iddiası bu rakamla **çürüktür** — ve bu, tezin kendi kaynağıdır.
URL: https://arxiv.org/abs/2607.04697 · https://arxiv.org/html/2607.04697v1

**Karşı-kanıt 2 — oranların "şişkin" olduğu tezini ARADIM, bulamadım; makale tersini beyan ediyor.**
Antitez rolüm gereği metodolojik şişkinlik kanıtı aradım. Makale kendini şöyle konumluyor: sonuçlar "a conservative lower bound" `[çekildi]`. Yani şişkinlik değil, **alt sınır** iddiası. Bu, iddia 1'in %20-40 bandını zayıflatmıyor, **güçlendiriyor** — antitez burada başarısız.

**Karşı-kanıt 3 — ama örneklem yanlılığı belgeli (kısmi başarı).**
Aynı makale, Threats to Validity bölümü:

> "Internal Validity. The total number of co-active pairs is extremely biased toward a very small subset of highly active repositories (the top ten account for 91.4% of all raw pairs)." `[çekildi]`

> "External Validity. The findings reported here are constrained by the AIDev-pop dataset: open-source projects and five agent profiles, all over a fixed time frame (December 2024–July 2025)." `[çekildi]`

> "Construct Validity. We treat temporal co-activity as a proxy for the occurrence of concurrent work" `[çekildi]`

Üç sınır: (a) ham çiftlerin %91.4'ü 10 depodan — normalizasyon yapılmış ama taban dar; (b) yalnız açık kaynak, 5 ajan profili, Aralık 2024–Temmuz 2025 penceresi; (c) çakışma değil, **zamansal örtüşme** vekil değişken olarak alınmış. Ayrıca örneklem **747 çift** — "very large-scale" nitelemesine karşın merge-replay tabanı küçük. Jarvis'e (tek depo, tek sahip, kapalı iş akışı) doğrudan aktarım bu üç sınır yüzünden **desteklenmiyor**.

**Karşı-kanıt 4 — farklı ölçümde AI PR'ları daha AZ hasar veriyor.**
Mergify "State of Merge Queues 2026" (200.000+ merge, 477 organizasyon, 90 gün; benchmark 153.000 merge / 160 organizasyon):

> "AI-assisted PRs broke main 1.9% of the time, against 4.4% for pull requests with no detectable AI assistance" `[çekildi]`

Bu metrik "main'i kırma", "metinsel çakışma" değil — **aynı şey değil**, doğrudan çürütme sayılmaz. Ama "ajan paralelliği daha tehlikelidir" genellemesine karşı ölçülü bir denge noktasıdır.
URL: https://mergify.com/reports/state-of-merge-queues-2026

**Karşı-kanıt 5 — bant genişliği metodolojiye çok duyarlı.**
İkinci bir 2026 çalışması (AgenticFlict, gönderim 2026-04-04, rev. 05-12): 142K+ AI PR, 59K+ depo, 29K+ çakışmalı PR = **%27.67** çakışma oranı `[çekildi]`; ajana göre Copilot %15.43, Codex %32.31 `[arama-özeti]`. Yani "%20-40" tek bir sayı değil, **ajan seçimine göre iki kattan fazla oynayan** bir aralık. Bandı sabit bir sistem sabiti gibi kullanmak yanlış.
URL: https://arxiv.org/abs/2604.03551

**Kalan:** "Worktree izolasyonu çakışmayı birleştirme anına erteler" önermesini çürütecek — izolasyonun çakışmayı ihmal-edilebilir kıldığını gösteren — ölçüm **bulamadım**. Makale zaten worktree kullanmadan `git merge-tree` ile replay yapıyor `[çekildi]`, yani izolasyonun etkisini ölçen bir çalışma yok. Bu boşluk hem tez hem antitez için açıktır.

**Aramalar:** "measured merge conflict rate parallel AI coding agents same repository study 2026 percent" · "Ghiotto nature of merge conflicts percentage empirical study"

---

## İDDİA 2 — Worktree'ler paylaşılan .git yüzünden tam bağımsız değildir (index/refs/objects yarışları)

### HÜKÜM: **DARALDI** (yarış var ama belgeli biçimde *fail-stop*; bozulma değil)

**Karşı-kanıt 1 — git'in kilit API'si belgeli garanti verir: yarış = komut hatası, veri bozulması değil.**
Git kaynak ağacı `lockfile.h`, başlık yorumu (birincil kaynak):

> "When we want to change a file, we create a lockfile `<filename>.lock`, write the new file contents into it, and then rename the lockfile to its final destination `<filename>`." `[çekildi]`

O_CREAT|O_EXCL ile "notice and fail if somebody else has already locked the file, then atomically rename the lockfile to its final destination to commit the changes and unlock the file." `[çekildi]`

Okuyucular için açık garanti:

> "Please note that lockfiles only block other writers. Readers do not block, but they are guaranteed to see either the old contents of the file or the new contents of the file (assuming that the filesystem implements `rename(2)` atomically)." `[çekildi]`

Bayat kilit temizliği de belgeli: atexit(3) ve sinyal işleyicisiyle "we remember the lockfiles we have created in a linked list" `[çekildi]`.
URL: https://raw.githubusercontent.com/git/git/master/lockfile.h

Sonuç: "yarış olabilir" doğru, ama sonucu **yarım yazılmış index/ref değil, `-1` dönen bir komut**. İddia "tam bağımsız değildir" derken bozulma imâ ediyorsa, o kısım çürüktür.

**Karşı-kanıt 2 — worktree başına ayrım belgeli ve nettir.**
`git-worktree(1)`, DETAILS bölümü:

> "in the linked worktree `git rev-parse --git-path HEAD` returns `/path/main/.git/worktrees/test-next/HEAD` ... while `git rev-parse --git-path refs/heads/master` uses `$GIT_COMMON_DIR` ... since refs are shared across all worktrees, except `refs/bisect`, `refs/worktree` and `refs/rewritten`." `[çekildi]`

HEAD ve index worktree'ye **özel**; refs paylaşımlı. Yani "index yarışı" iddiası worktree'ler arasında zaten geçersiz — her worktree'nin kendi index'i var. Yarış yüzeyi **yalnız refs + objects**'e daralır.
URL: https://git-scm.com/docs/git-worktree

**Karşı-kanıt 3'ün BAŞARISIZLIĞI — açık bir "güvenlidir" garantisi YOK.**
`git-worktree(1)` sayfasını eşzamanlılık garantisi için taradım: "concurrent" kelimesi **hiç geçmiyor**; `lock` yalnız `git worktree lock` (prune koruması) bağlamında geçiyor `[çekildi]`. Yani iddianın çekirdeği — "belgeli bir bağımsızlık garantisi yok" — **ayakta kalıyor**.

**Karşı-kanıt 4'ün TERSİ — sahada iş kaybı raporları iddiayı destekliyor.**
Antitez ararken iddiayı destekleyen iki açık issue çıktı (dürüstlük gereği kaydediyorum): anthropics/claude-code #55724 "parallel agents lose work due to git lock contention + auto-cleanup" ve #47266 "worktree fail due to git config lock race condition". Bunlarda kayıp git bozulmasından değil, **ajan koşucusunun commit başarısız olunca worktree'yi otomatik silmesinden** doğuyor `[arama-özeti]`. Bu, suçu git'ten alıp orkestratöre veriyor — iddia 2'yi daraltan ama iddia 2'nin pratik sonucunu doğrulayan bir ayrım.
URL: https://github.com/anthropics/claude-code/issues/55724 · https://github.com/anthropics/claude-code/issues/47266

**Net daraltma:** "Worktree'ler tam bağımsız değildir" → **doğru, ama** yarışın sonucu belgeli olarak *fail-stop*'tur; bozulma riski değil, **yeniden-deneme (retry/backoff) gereksinimi** doğurur. Ayrı `clone` bu yüzeyi tamamen kaldırır (ayrı .git, ayrı kilit ad-uzayı) `[arama-özeti]`.

**Aramalar:** "git worktree shared .git directory index.lock race condition concurrent" · "git documentation lock file index.lock O_EXCL atomicity guarantee concurrent processes safe corruption"

---

## İDDİA 3 — SQLite WAL'da yazar TEKTİR; doğru desen kuyruk + busy_timeout

### HÜKÜM: **DARALDI** (belgeli çok-yazarlı yol VAR, ama ana hatta değil)

**Karşı-kanıt 1 — BEGIN CONCURRENT: belgeli, çalışan, çok-yazarlı.**
SQLite'ın kendi dokümanı (hctree/begin-concurrent dalı):

> "BEGIN CONCURRENT allows multiple writers to process write transactions simultanously if the database is in 'wal' or 'wal2' mode, although the system still serializes COMMIT commands." `[çekildi]`

Çakışma tespiti: "the system checks whether or not any of the database pages that the transaction has read have been modified since the BEGIN CONCURRENT was opened" `[çekildi]`; çakışma varsa "an SQLITE_BUSY_SNAPSHOT error is returned. At this point, all the client can do is ROLLBACK the transaction." `[çekildi]`

Yani "ikinci yazar SQLITE_BUSY alır ve tek çare kuyruk" ifadesi eksik: **iyimser eşzamanlılık (OCC)** ile iki yazar paralel ilerleyebilir, yalnız COMMIT serileşir. Desen "kuyruk" değil, **"paralel çalış + çakışırsan rollback+retry"**dir.
URL: https://sqlite.org/hctree/doc/begin-concurrent/doc/begin_concurrent.md

**Karşı-kanıt 2 — çakışmayı şema tasarımıyla düşürmek belgeli.**
Aynı doküman: farklı tablolara dokunan işlemler asla çakışmaz; monoton artan INTEGER PRIMARY KEY'den kaçın, rastgele değer kullan; timestamp indekslerine dikkat; yazmaları örtüşmeyen anahtar aralıklarına dağıt `[çekildi]`. Yani çakışma oranı **tasarım değişkeni**, sabit değil.

**Karşı-kanıt 3 — üretimde kullanan var (kısmi).**
Expensify/Bedrock issue #218 (2017-06-14):

> "Bedrock creates a CONCURRENT transaction for every query, which doesn't allow schema changes." `[çekildi]`

Bedrock, Expensify'ın üretim veritabanı katmanıdır; issue sayfası üretim beyanını **açıkça yazmıyor** — bu bağı issue'dan doğrulayamadım, bayraklıyorum. Ama "her sorgu için CONCURRENT transaction" ifadesi, özelliğin deneysel-oyuncak olmadığını, gerçek bir kod tabanının varsayılanı olduğunu gösteriyor.
URL: https://github.com/Expensify/Bedrock/issues/218

**Karşı-kanıt 4 — Turso MVCC (2025-10-06): SQLITE_BUSY'yi kaldırma iddiası, ama üretim değil.**

> "When concurrent writes are used, we achieve up to 4x the write throughput of SQLite, while also removing the dreaded `SQLITE_BUSY` error." `[çekildi]`

Turso kendi beyanı: MVCC "currently in an early technology preview stage, indicating it is intended for experimental use and evaluation, rather than production use." `[çekildi]`
URL: https://turso.tech/blog/beyond-the-single-writer-limitation-with-tursos-concurrent-writes

**Ayakta kalan:** BEGIN CONCURRENT **ana hatta (mainline) birleşmedi**; ayrı dalda `[arama-özeti — doğrulama: dokümanın kendisi `sqlite.org/hctree/` altında, ana doküman ağacında değil]`. hctree prototipi "advanced enough to experiment with ... but is incomplete" `[arama-özeti]`. Turso açıkça üretim-dışı.

**Net daraltma:** "SQLite'ta yazar tektir" → **varsayılan/ana-hat SQLite için doğru**; "tek çare kuyruk + busy_timeout" → **yanlış**, belgeli ikinci bir yol (OCC + rollback/retry, wal2) var ama bugün dal derlemesi gerektiriyor. Jarvis için pratik sonuç değişmiyor (dal derlemesi maliyeti), ama iddia **koşulsuz** kurulamaz.

**Aramalar:** "SQLite BEGIN CONCURRENT multiple writers 2025 production HCTree" · "Expensify Bedrock SQLite BEGIN CONCURRENT production use"

---

## İDDİA 4 — flock yerelde güvenilir, NFS'te ve stale-lock'ta belgeli biçimde kırılır

### HÜKÜM: **DARALDI** (NFS kısmı 20 yıllık ölçüde eskimiş; stale-lock için belgeli kurtarma var)

**Karşı-kanıt 1 — flock NFS'te 2005'ten beri çalışıyor.**
`flock(2)` man sayfası, NOTES:

> "Since Linux 2.6.12, NFS clients support flock() locks by emulating them as fcntl(2) byte-range locks on the entire file." `[çekildi]`

Sonuç: "fcntl(2) and flock() locks do interact with one another over NFS" `[çekildi]`. Karşılaştırma için aynı sayfa: "Up to Linux 2.6.11, flock() does not lock files over NFS" `[çekildi]` — yani "NFS'te kırılır" **Linux 2.6.11 ve öncesinin** doğrusu. AS-OF 2026'da bu 20 yıllık bir bilgi.

Ayrıca yerel-davranış isteyen için belgeli kaçış: "Since Linux 2.6.37, the kernel supports a compatibility mode that allows flock() locks (and also fcntl(2) byte region locks) to be treated as local" — `local_lock` mount seçeneği `[çekildi]`.
URL: https://man7.org/linux/man-pages/man2/flock.2.html

**Karşı-kanıt 2 — stale-lock için protokol düzeyinde belgeli kurtarma (NFSv4/4.1).**
RFC 8881 (NFSv4.1): kilitler istemci çapında tek bir **lease**'e bağlıdır; lease yenilenmezse kilitler iptale tabidir. Sunucu yeniden başlarsa istemciler özel bir **grace period** içinde kilitlerini güvenle geri alır (reclaim) `[arama-özeti]`. NFSv4.1'de `RECLAIM_COMPLETE` ile istemci reclaim bitişini bildirir, sunucu beklemeyi kısaltır `[arama-özeti]`.
Grace period'ın amacı doğrudan stale-lock/steal senaryosudur: "to give the clients enough time to notice that the server has rebooted, and to reclaim their existing locks without danger of having somebody else steal the lock from them" `[arama-özeti]`.
URL: https://datatracker.ietf.org/doc/rfc8881/ · https://www.rfc-editor.org/rfc/rfc8881.pdf · https://jtlayton.wordpress.com/2011/12/05/activeactive-nfs-on-clustered-filesystems-lock-recovery-and-grace-period/

Bu, "stale lock çözümsüzdür" iddiasını doğrudan çürütür: **lease + grace period** tam olarak stale-lock'un belgeli çözümüdür (süreç ölürse lease yenilenmez → kilit düşer).

**Ayakta kalan (iddiayı kurtaran):** Poettering, "On the Brokenness of File Locking": POSIX kilitlerinin NFS-güvenli olduğu varsayılsa da "there are still many NFS implementations around where locking is not properly implemented" ve kritik cümle — "there is no way to properly detect whether file locking works on a specific NFS mount (or any mount) or not" `[arama-özeti]`. Ayrıca Samba/NFS çakışma vakası: yerel çekirdeğin çakışmadığını sandığı kilitleri NFS sunucusunun çakışmış sayıp reddetmesi `[arama-özeti]`.
URL: https://0pointer.de/blog/projects/locking.html · https://utcc.utoronto.ca/~cks/space/blog/linux/NFSSambaLockingII

**Net daraltma:** "NFS'te kırılır" → **modern Linux + NFSv4'te mekanizma vardır ve belgelidir**; kalan risk "uygulama kalitesi ve tespit edilemezlik"tir. Doğru ifade: *"flock NFS'te çalışır ama çalıştığını doğrulayamazsın"* — kategorik kırılma değil, **doğrulanamazlık**. Bu, Jarvis gibi tek-makine/yerel-disk senaryosunda pratik olarak **konu dışıdır**.

**Aramalar:** "flock NFS advisory lock reliability documented failure stale lock POSIX" · "NFSv4 lease-based locking state recovery grace period solves stale lock RFC 8881"

---

## İDDİA 5 — Atomic-rename, POSIX yerel FS'te bayat-okumaya karşı YETERLİ korumadır

### HÜKÜM: **ÇÜRÜDÜ** (dört ayrı belgeli delik)

**Karşı-kanıt 1 (öldürücü) — rename'in garantisi "yırtık okuma yok"tur, "bayat okuma yok" DEĞİL.**
Git'in kendi kilit API'si, garantiyi birebir şöyle yazıyor:

> "Readers do not block, but they are guaranteed to see either the **old contents** of the file or the new contents of the file" `[çekildi, vurgu benim]` — `lockfile.h` başlık yorumu

"Eski içeriği görmek" **bayat okumanın tanımıdır**. Yani atomic-rename yırtık/yarım okumayı engeller; bayatlığı engellemez. İddia, iki farklı özelliği birbirine karıştırıyor. Bu tek alıntı iddiayı çürütmeye yeter.
URL: https://raw.githubusercontent.com/git/git/master/lockfile.h

**Karşı-kanıt 2 — açık fd rename'den etkilenmez: okuyucu ESKİ inode'da takılı kalır.**
`rename(2)` man sayfası:

> "If newpath already exists, it will be atomically replaced, so that there is no point at which another process attempting to access newpath will find it missing." `[çekildi]`

fakat aynı sayfa:

> "Open file descriptors for oldpath are also unaffected" `[çekildi]`

Uzun-yaşayan bir okuyucu (tam da ajan senaryosu) dosyayı bir kez açıp fd'yi tutuyorsa, rename sonrası **süresiz olarak eski içeriği okumaya devam eder**. Atomic-rename bunu görmez bile.
URL: https://man7.org/linux/man-pages/man2/rename.2.html

**Karşı-kanıt 3 — çapraz-aygıt: desen sessizce çalışmaz (EXDEV).**
Aynı man sayfası, EXDEV: "oldpath and newpath are not on the same mounted filesystem. (Linux permits a filesystem to be mounted at multiple points, but rename() does not work across different mount points, even if the same filesystem is mounted on both.)" `[çekildi]`

Pratik sonuç: geçici dosya `/tmp`'de (çoğu Mac/Linux kurulumda ayrı mount / tmpfs), hedef proje dizinindeyse **rename başarısız olur** ve kod büyük olasılıkla kopyala-üzerine-yaz'a düşer — ki bu atomik değildir. "tmp'ye yaz sonra taşı" deseni, tmp'nin **hedefle aynı dosya sisteminde** olmasını şart koşar; iddia bu şartı içermiyor.

**Karşı-kanıt 4 — çökme dayanıklılığı için dizin fsync şart; yoksa belgeli veri kaybı.**
PostgreSQL commit'i "Avoid unlikely data-loss scenarios due to rename() without fsync": eski WAL dosyaları geri dönüştürülüp doldurulduğunda içerikleri fdatasync ediliyor ama **içeren dizin fsync edilmiyordu**; OS/donanım çökmesi dosyayı eski adıyla ama yeni içerikle bırakabiliyor, WAL replay onu oynatmıyor `[arama-özeti]`. Genel kural: rename normal işleyişte atomiktir, **çökmeye karşı atomik değildir**; rename sonrası dizin fd'sinin fsync'lenmesi gerekir `[arama-özeti]`.
URL: https://www.postgresql.org/message-id/E1adrE0-0001Os-CD%40gemulon.postgresql.org · https://github.com/npm/write-file-atomic/issues/64 ("Rename atomicity is not enough")

**Karşı-kanıt 5 — NFS'te rename'in kendi çökme penceresi var.**
`rename(2)` man sayfası, bilinen sorun: "If the server does the rename operation and then crashes, the retransmitted RPC which will be processed when the server is up again causes a failure" `[çekildi]`.

**Sonuç:** İddia 5, dört bağımsız belgeli delikle çürüktür. Doğru formülasyon: *atomic-rename yırtık okumaya karşı yeterlidir; bayat okumaya, çökme dayanıklılığına ve çapraz-mount'a karşı DEĞİLDİR.* Bayatlık için ayrıca sürüm/nesil damgası + yeniden-okuma veya koşullu-yazma gerekir (bkz. İddia 10).

**Aramalar:** "atomic rename not enough durability directory fsync crash rename POSIX"

---

## İDDİA 6 — Sıralama ve karşılıklı-dışlama İKİ AYRI, birbirine indirgenemez eksendir

### HÜKÜM: **DARALDI** (en az iki olgun tasarımda dışlama, anahtarlı sıralamaya İNDİRGENMİŞ)

**Karşı-kanıt 1 — Restate Virtual Objects: TEK primitif (anahtar) her iki ekseni birden veriyor.**
Restate dokümanı: Virtual Object'ler "stateful and key-addressable — each object instance has a unique ID and persistent state" `[çekildi]`; handler'lar ikiye ayrılır — **exclusive** handler'lar `ObjectContext` alır ve "allow read/write access to object state" `[çekildi]`, **shared** handler'lar `handlers.object.shared(...)` ile sarılıp `ObjectSharedContext` kullanır `[çekildi]`.
Eşzamanlılık modeli: anahtar başına **intrinsic lock** — "at most one request can run at the same time for a given key, and any additional request will be enqueued in a per-key queue" `[arama-özeti]`.

Burada **sıralama** (anahtar başına FIFO kuyruk) ve **dışlama** (anahtar başına tek yazar) *aynı primitiften* çıkıyor. İki ayrı eksen değil, **tek eksenin (anahtar) iki yüzü**. Bu, "indirgenemez" iddiasının doğrudan karşı-örneğidir.
URL: https://docs.restate.dev/develop/ts/overview/ · https://docs.restate.dev/foundations/key-concepts

**Karşı-kanıt 2 — Temporal'da ayrı bir kaynak-grubu primitifi YOK; mutex sıralamadan türetiliyor.**
Temporal'ın resmî Go örneği `samples-go/mutex`: mutex workflow "demonstrates an ability to lock/unlock a particular resource within a particular Temporal namespace so that other workflows within the same namespace would wait until a resource lock is released" `[arama-özeti]`. Mekanizma tamamen sıralama primitifleriyle kurulu: "acquire-lock-event" / "request-lock-event" sinyal kanalları, `SignalWithStartWorkflow`, ve iş akışı bir "acquire-lock-event" gelene dek bloke `[arama-özeti]`.
Yani olgun bir orkestratör, dışlamayı **birinci sınıf bir eksen olarak sunmadan**, saf sıralama + mesajlaşmayla üretiyor.
URL: https://pkg.go.dev/github.com/temporalio/samples-go/mutex · https://github.com/temporalio/samples-go

**İddiayı kurtaran kalıntı (dürüstlük payı):** Aynı Temporal dokümanı indirgemenin **bedelini** de yazıyor: sinyalleri sırayla işleyerek koordinasyon mümkündür "however the logic might become too complex if you need to lock two or more resources at the same time" `[arama-özeti]`. Yani **çoklu kaynak** durumunda (deadlock, kilit sırası) tek eksene indirgeme pratikte çöküyor — iddia 6 burada ayakta kalıyor.

**Net daraltma:** "İkisi birbirine indirgenemez" → **tek kaynak / anahtar-bölümlenebilir işte indirgenebilir ve endüstride indirgeniyor** (Restate: anahtar; Temporal: mutex-workflow). İndirgenemezlik **çoklu-kaynak kilitlemede** başlıyor. Jarvis'in kaynakları (bir SQLite dosyası, bir dizin, bir defter) çoğunlukla anahtar-bölümlenebilir olduğundan, "iki eksen şart" savı burada **kanıt yükünü karşılamıyor**.

**Aramalar:** "Restate virtual objects exclusive handlers single-writer per key queue ordering documentation" · "Temporal mutex workflow pattern implement mutual exclusion using workflow signals sample"

---

## İDDİA 7 — LLM-ajan sistemlerinde kaynak-grubu/dışlama ekseni BUGÜN EKSİKTİR

### HÜKÜM: **ÇÜRÜDÜ** (sevk edilmiş, belgeli, ajan-orkestratöründe yerleşik)

**Karşı-kanıt — Inngest: Singleton Functions + anahtarlı concurrency; AgentKit aynı platformda koşuyor.**

Inngest changelog, **2025-06-06**:

> "Singleton Functions is a new Flow Control feature that allows exclusive execution of an Inngest function." `[çekildi]`

Rate limiting'den farkı: singleton "discard events (or cancel runs) only if an execution is already running" `[çekildi]`.
URL: https://www.inngest.com/changelog/2025-06-06-singleton-functions

Doküman düzeyinde tam olarak istenen iki özellik:
- **Adlandırılmış dışlama anahtarı:** singleton, `key` ile yapılandırılır — "A unique key expression to which the limit is applied, evaluated for each triggering event using the Common Expression Language (CEL)" `[arama-özeti]`. Örnek: `event.data.user_id` → kullanıcı başına tek koşum.
- **İki mod:** "skip" (çalışanı koru, yeniyi at) ve "cancel" (en yeni olay mutlaka işlensin) `[arama-özeti]`.
- **Granülerlik ayrımı belgeli:** "Concurrency set to 1 ensures that only a single step of a given function is running at a time, [while] Singleton Functions ensure that only a single **run** of a given function is happening at a time." `[arama-özeti]` — yani iki ayrı dışlama düzeyi sunuluyor.
URL: https://www.inngest.com/docs/guides/singleton · https://www.inngest.com/docs/reference/functions/singleton · https://www.inngest.com/docs/guides/flow-control · https://www.inngest.com/docs/guides/concurrency

**Bu bir LLM-ajan orkestratörüdür, genel iş-akışı motoru değil:** AgentKit, Inngest'in çok-ajanlı çerçevesidir — "Build multi-agent networks in TypeScript with deterministic routing" `[arama-özeti]` — ve AgentKit ağları **aynı flow-control eksenini** kullanır: ağlar "concurrency limits using a concurrency key (e.g., `event.data.user_id`)" ile yapılandırılır `[arama-özeti]`.
URL: https://agentkit.inngest.com/ · https://agentkit.inngest.com/advanced-patterns/multitenancy · https://github.com/inngest/agent-kit

**Ek karşı-örnek:** Restate, ajan bağlamını açıkça hedefleyerek anahtar başına tek-yazar sunuyor — Virtual Object kullanımı: "Implement consistent state machines, session state, or agent context and memory" `[çekildi]`. Yani ajan durumu için dışlama, ürünün **reklamı yapılan** kullanım senaryosudur.
URL: https://docs.restate.dev/foundations/key-concepts · https://restate.dev/blog/durable-coding-agent-with-restate-and-modal

**Sonuç:** "Bu eksen ajan sistemlerinde eksiktir" iddiası, en az bir ürün (Inngest/AgentKit, 2025-06'dan beri sevkte) ve bir ikincisi (Restate) tarafından çürütülüyor. Doğru ifade: eksen **eksik değil, seçilen yığında yok**. Jarvis kendi orkestratörünü yazıyorsa bu bir *kurulum tercihi* sorunudur, *literatür boşluğu* değil — ve hazır tasarımlar (CEL anahtarı + skip/cancel modu) doğrudan örnek alınabilir (KILAVUZ "hazırı temel al").

**Aramalar:** "Inngest concurrency key singleton agent orchestration AgentKit mutual exclusion" · "Inngest docs singleton mode concurrency key flow control singleton workflow"

---

## İDDİA 8 — En belgeli güvenli desen: yol-bazlı ayrık yazım alanları + tek-birleştirici (merge queue)

### HÜKÜM: **DARALDI** (tek-birleştirici, ölçekte belgeli darboğaz; endüstri onu terk etmiyor ama SERİLİĞİ terk ediyor)

**Karşı-kanıt 1 — Uber SubmitQueue: seri kuyruk ölçeklenmediği için inşa edildi.**
SubmitQueue'nun amacı "always green mainline" `[arama-özeti]`. Kritik nokta ölçekleme cümlesi: "To scale to thousands of changes per day while ensuring serializability, the planner engine **speculates** on outcomes of pending changes ... and executes their corresponding builds in parallel" `[arama-özeti]`. "Rather than validating changes one at a time, SubmitQueue speculatively rebases and validates multiple changes in parallel against predicted future states of HEAD" `[arama-özeti]`.

Yani saf "tek-birleştirici, teker teker" deseni günde binlerce değişiklikte **yetersiz** olduğu için, üstüne spekülatif paralel doğrulama katmanı gerekmiştir. İddia "tek-birleştirici en iyi belgeli desendir" derken, en iyi belgeli uygulamanın **tek-birleştiriciliği simüle eden ama serileştirmeyen** bir sistem olduğunu atlıyor: "the illusion of a single queue" `[arama-özeti]`.
URL: https://github.com/uber/submitqueue · https://blog.acolyer.org/2019/04/18/keeping-master-green-at-scale/

**Karşı-kanıt 2 — ölçülü bekleme kuyrukları darboğazı gösteriyor.**
Mergify "State of Merge Queues 2026" (200.000+ merge / 477 organizasyon / 90 gün):
- Bekleme süresi: açık kaynak medyan **5 dk**, özel medyan **8 dk**, özel **p90 = 63 dk** `[çekildi]`
- Verim: özel medyan **3.1 merge/aktif gün**, p90 **13 merge/aktif gün** `[çekildi]`
- Bozuk-main oranı takım büyüklüğüyle **~16x** ölçekleniyor: 2-5 mühendiste %0.8, 40+ mühendiste %12.5 `[çekildi]`

p90'da bir saatlik kuyruk beklemesi, "ajanlar beklemez" senaryosunda tek-birleştiricinin maliyetini somutlaştırıyor. Ayrıca bozuk-main oranının takım (yani eşzamanlı yazar) sayısıyla süper-lineer artması, **paralel yazar sayısının kendisinin** risk değişkeni olduğunu gösteriyor — desen değil, ölçek.
URL: https://mergify.com/reports/state-of-merge-queues-2026

**Karşı-kanıt 3 — argüman var ama ÖLÇÜM yok (bayrak).**
"Merge Queues Were Built for Humans. Agents Don't Wait" (2026-06-30), Hashimoto'dan aktarım: "You constantly rebase. Merge queues solves that to a certain extent...but then if you 10x that, conservatively...and then if you 100 or 1,000x that, I think it gets completely untenable." `[çekildi]`
**Ama** yazının kendisi bu rakamları reddediyor: bunlar "hype-cycle hypotheticals, not measurements. The direction is the point." `[çekildi]` Yazı ajan PR hacmi, çakışma oranı veya kuyruk verimi için **hiçbir ölçüm içermiyor** `[çekildi]`. Bu yüzden bunu kanıt değil, **hipotez** olarak işaretliyorum. Yazar ayrıca darboğazın kuyruğun kendisi değil, ajan ölçeğine göre boyutlanmamış CI hattı olduğunu savunuyor `[çekildi]` — bu, iddia 8'i kısmen **savunur**.
URL: https://julien.danjou.info/blog/merge-queues-built-for-humans/

**Çürütemediğim yarı:** İddianın "yol-bazlı ayrık yazım alanları" kısmına karşı **hiçbir karşı-kanıt bulamadım**. Bunun kötü ölçeklendiğine dair belgeli bir vaka çıkmadı; aksine İddia 1'in verisi (yapısal çakışmaların %41.9'u modify/delete + add/add) dosya-yolu düzeyinde ayrıştırmanın çakışmaların büyük dilimini keseceğini ima ediyor. Bu yarı **ayakta**.

**Net daraltma:** Desen "yol-ayrımı + tek-birleştirici" değil, **"yol-ayrımı + serileştirme YANILSAMASI (spekülatif paralel doğrulama)"** olarak yazılmalı. Düşük hacimde (Jarvis ölçeği) fark yok; yüksek hacimde seri kuyruk belgeli darboğaz.

**Aramalar:** "Uber SubmitQueue paper merge queue does not scale serialization bottleneck speculation"

---

## İDDİA 9 — CI concurrency-group'ları mutual-exclusion için ÜRETİM-KANITLI mekanizmadır

### HÜKÜM: **DARALDI** (iki ayrı belgeli açık: çift-koşum raporu + sıralama garantisi yokluğu)

**Karşı-kanıt 1 (doğrudan) — concurrency group'un aynı workflow'u İKİ KEZ koşturduğu rapor, GitHub personelince kabul edilmiş, kök-neden yayımlanmamış.**
GitHub community Discussion **#9252**, başlık: "Concurrency group appears to have race condition and allow same workflow to run twice."
- Tarih: **2021-12-23**, bildiren: josmartin
- Gözlem: `cancel-in-progress: false` ile tek koşum garanti edilmesi gerekirken — "I frequently see 2 of the jobs running at the same time" `[çekildi]`. Ekran görüntüleri iki işin (debian-buster / debian-bullseye, sonra ubuntu-focal / ubuntu-hirsute) eşzamanlı koştuğunu belgeliyor `[çekildi]`.
- Ek arıza: aynı concurrency grubundaki bazı işler açıklamasız "skipped" işaretlenmiş `[çekildi]`.
- GitHub yanıtı (**2022-02-04**, ethomson): "Thanks for letting us know @josmartin, I've asked the team to look into this." `[çekildi]`
- **Görünür başlıkta çözüm ya da kök-neden analizi yok** `[çekildi]`.

Bu, iddianın tam kalbine iner: "üretim-kanıtlı" denen mekanizmanın **karşılıklı dışlamayı ihlal ettiği** kamuya açık, satıcı tarafından kabul edilmiş bir vaka var.
URL: https://github.com/orgs/community/discussions/9252

**Karşı-kanıt 2 — concurrency group SIRA garantisi vermez (belgeli).**
GitHub community Discussion #199398: "Older workflow runs overriding newer deployments when pushing multiple commits quickly." İki PR arka arkaya merge edildiğinde, önce başlayan ama deploy işine geç ulaşan eski koşum, daha erken biten yeni deploy'un üzerine yazabiliyor; "There is no guarantee that the latest push will be published" `[arama-özeti]`.
Genel formülasyon: "The concurrency feature in GitHub Actions doesn't inherently guarantee order - it primarily controls which workflows execute simultaneously." `[arama-özeti]`
URL: https://github.com/orgs/community/discussions/199398

Bu ikinci nokta önemli: karşılıklı dışlama sağlansa bile **son-yazan-kazanır** sırası garanti değil. Bayat yazma (stale write) riski mekanizmanın içinde kalıyor.

**Ayakta kalan:** Mekanizma yaygın kullanımda ve çoğu durumda çalışıyor; #9252 tek ve eski (2021) bir rapor, kalıcı/yaygın bir hata olduğuna dair sürekli kanıt bulamadım. "Üretim-kanıtlı" nitelemesi tümden yıkılmıyor.

**Net daraltma:** "Üretim-kanıtlı mutual-exclusion" → **"pratikte işe yarayan, ama (a) satıcı tarafından kabul edilmiş bir çift-koşum yarışı raporu bulunan ve (b) sıralama garantisi TANIM GEREĞİ olmayan"** mekanizma. Kritik dışlama için tek başına yeterli sayılamaz; idempotent iş + sürüm kontrolü ile birlikte kullanılmalı.

**Aramalar:** "GitHub Actions concurrency group race condition bug deployments not guaranteed order"

---

## İDDİA 10 — Bayat-okuma gerçek ve belgelidir; yeniden-okuma protokolü gerektirir

### HÜKÜM: **DARALDI** (problem gerçek — ama "yeniden-okuma protokolü gerektirir" yanlış; otomatik çözen belgeli mekanizmalar var)

**Karşı-kanıt 1 — Koşullu yazma (OCC): bayat durumu YAZMA anında otomatik yakalar, yeniden-okuma protokolü gerekmez.**
AWS S3 dokümanı, "How to prevent object overwrites with conditional writes":

> "You can use the `If-Match` header to compare the ETag value of an object in an Amazon S3 bucket with one that you provide during the `WRITE` operation. If the ETag values don't match, the operation fails." `[çekildi]`

Eşzamanlı yazarlar için davranış birebir tanımlı:

> "If multiple conditional writes or copies occur for the same object name, the first write operation to finish succeeds. Amazon S3 then fails subsequent writes with a `412 Precondition Failed` response." `[çekildi]`

Ayrıca silme yarışı için ayrı kod: "You can also receive a `409 Conflict` response in the case of concurrent requests if a delete request to an object succeeds before a conditional write operation on that object completes" ve If-Match'te silinmiş nesne için `404 Not Found` `[çekildi]`.

Mekanizma önemi: ajan başta okuduğu durumun ETag'ini taşır; durum değişmişse **yazma reddedilir**. Ajanın "arada bir yeniden oku" protokolü işletmesine gerek yok — bayatlık *fail-closed* olarak yakalanır. Bu, iddianın "yeniden-okuma protokolü gerektirir" kısmının doğrudan karşı-örneğidir.
URL: https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-writes.html

**Karşı-kanıt 2 — Ajan araç katmanında bu zaten OTOMATİK uygulanıyor.**
Claude Code'un Edit/Write araçları, okumadan sonra dosya değişmişse yazmayı reddediyor: "File has been modified since read" / "File has been unexpectedly modified" hataları `[arama-özeti]`. Yani en yaygın kod-ajanı yığınında bayat-yazma freni **araç sözleşmesine gömülü**; ajanın protokol işletmesi gerekmiyor, araç zorluyor.
URL: https://github.com/anthropics/claude-code/issues/10437 · https://github.com/anthropics/claude-code/issues/28383

**Karşı-kanıt 3 — SQLite'ta aynı fikir veritabanı düzeyinde belgeli.**
BEGIN CONCURRENT: commit anında "the system checks whether or not any of the database pages that the transaction has read have been modified since the BEGIN CONCURRENT was opened" `[çekildi]`; bayatsa `SQLITE_BUSY_SNAPSHOT` `[çekildi]`. Yani **okunan sayfaların bayatlığı** motor tarafından otomatik denetleniyor.
URL: https://sqlite.org/hctree/doc/begin-concurrent/doc/begin_concurrent.md

**İddiayı KURTARAN kalıntı (önemli):** Bu otomatik mekanizmaların kendileri de hatalı olabiliyor ve hata **sessiz bayat okuma** yönünde. anthropics/claude-code issue **#60684**: "`Read` tool returns 'file unchanged' after external on-disk edits, serving a stale cached snapshot" `[arama-özeti]`. Ayrıntı: bayatlık denetimi "appears to track only edits made by the assistant's own tools, not modifications to the file on disk from other sources (IDE save, another terminal, another process)" — dosya iki Read arasında dışarıdan değişirse ikinci Read "değişmemiş" deyip güncel içeriği vermiyor, ajan **bayat görüntü üzerinde çalışıyor** `[arama-özeti]`.
URL: https://github.com/anthropics/claude-code/issues/60684

Bu, tam da İB-63'ün senaryosudur: **kardeş ajanın yazdığı** değişiklik "başka bir süreç" sayılır ve denetimden kaçar.

**Net daraltma:** "Bayat-okuma gerçektir" → **doğru ve belgeli**. "Yeniden-okuma protokolü gerektirir" → **yanlış**; doğru çözüm ailesi **koşullu yazma / sürüm-damgalı CAS**'tır (S3 If-Match/412, SQLITE_BUSY_SNAPSHOT, Edit'in mtime denetimi) — bu, protokolü ajandan alıp **kaynağa** koyar. Kalan risk, denetimin **kapsamının dar olması** (yalnız kendi yazmalarını izlemesi); Jarvis için çıkarım: bayatlık damgası ajanın kendi izine değil, **dosyanın/satırın gerçek sürümüne** (hash/mtime/ETag) bağlanmalı.

**Aramalar:** "has been modified since read Claude Code Edit tool error file changed stale read protection" · AWS S3 conditional-writes dokümanı

---

## 11. Antitezin kendi sınırları (epistemik dürüstlük)

1. **Tek yönlü tasarım:** Yalnız ¬T arandı. Destekleyici kanıtları sistematik taramadım; bu rapor tek başına karar tabanı **değildir**.
2. **`[arama-özeti]` etiketli alıntılar** ham kaynaktan birebir doğrulanmadı (arama motorunun özetinden geldi). Karar-taşıyan kullanımdan önce çekilmeli. Özellikle: Ghiotto %10-20, Copilot/Codex oranları, Uber SubmitQueue cümleleri, NFSv4 grace-period cümleleri, Inngest singleton `key`/mod ayrıntıları, Temporal mutex ayrıntıları, Restate per-key kuyruk cümlesi.
3. **Doğrulayamadığım bağ:** Bedrock'un CONCURRENT transaction kullanımının **üretimde** olduğu, issue #218'den doğrulanamadı (yalnız kod davranışı beyanı var).
4. **Denenmeyen kaynaklar:** ResearchGate ve ScienceDirect (paywall beklentisi) açılmadı — Ghiotto ve ark. tam metni okunmadı; oradaki oran ikinci elden.
5. **Tarih riski:** arXiv 2607.04697 çok yeni (2026-07) ve v2; hakem süreci durumu bilinmiyor. Mergify raporu satıcı-kaynaklıdır (merge queue satan şirket) — **çıkar çatışması bayrağı**.
6. **Kırpma etkisi:** 35 iddia incelenmedi. Aile B'nin çakışma modeli bu 10 iddiaya indirgenirse eksik kalır.

## 12. Özet tablo

| # | İddia (kısa) | Hüküm | Çürüten çekirdek kanıt |
|---|---|---|---|
| 1 | worktree erteler; %20-40; çoğu yapısal | DARALDI | yapısal = %41.9 (azınlık); makale "lower bound"; top-10 depo = %91.4 |
| 2 | worktree tam bağımsız değil | DARALDI | `lockfile.h`: O_EXCL + atomik rename → fail-stop, bozulma yok; index worktree'ye özel |
| 3 | SQLite tek yazar, çare kuyruk | DARALDI | BEGIN CONCURRENT (wal/wal2, OCC, BUSY_SNAPSHOT); Bedrock; Turso MVCC (üretim değil) |
| 4 | flock NFS'te kırılır | DARALDI | Linux 2.6.12+ flock→fcntl emülasyonu; 2.6.37 local_lock; NFSv4 lease+grace |
| 5 | atomic-rename bayat-okumaya yeter | **ÇÜRÜDÜ** | git: "see either the **old** contents or the new"; açık fd etkilenmez; EXDEV; dizin fsync |
| 6 | sıralama ⊥ dışlama, indirgenemez | DARALDI | Restate: tek anahtar → FIFO + tek-yazar; Temporal: mutex = workflow |
| 7 | ajan sistemlerinde dışlama ekseni yok | **ÇÜRÜDÜ** | Inngest Singleton Functions (2025-06-06) + CEL key + skip/cancel; AgentKit aynı platform |
| 8 | yol-ayrımı + tek-birleştirici en iyi | DARALDI | SubmitQueue: seri kuyruk ölçeklenmez → spekülasyon; p90 bekleme 63 dk |
| 9 | CI concurrency-group üretim-kanıtlı | DARALDI | GH #9252 çift-koşum (staff kabul, kök-neden yok); #199398 sıra garantisi yok |
| 10 | bayat-okuma yeniden-okuma protokolü ister | DARALDI | S3 If-Match/412 OCC; Edit mtime denetimi; ama #60684 denetim kapsamı dar |

---
**Rapor sonu.** ATLAS antitez koşumu · AS-OF 2026-08-29 · uydurma kaynak yok; çürütülemeyen yarılar açıkça işaretlendi.
