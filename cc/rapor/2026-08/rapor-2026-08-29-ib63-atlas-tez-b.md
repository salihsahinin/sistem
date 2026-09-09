# TEZ RAPORU — Aile B: Aynı depoda çoklu ajan/otomasyon çakışma yönetimi

**AS-OF: 2026-08-29** (tüm iddialar bu tarihte canlı çekilen kaynaklara dayanır; teknoloji ve dokümanlar değişir)
**Ajan:** ATLAS (tez ajanı, Aile B) · **Emir:** IB-63 · **Web:** serbest
**Kanıt kuralı:** her iddia URL'li; tırnak içi metin ham kaynaktan alınmış ve bölümü beyan edilmiştir; kestirim `[?]` ile işaretlidir.

---

## 0. Dalga protokolü — ayrıştırma beyanı

**Koşacağım varsayılan hat:** "git worktree ile paralel ajan" blog literatürü.
**Muhtemel bulgu:** Her ajana bir worktree ver, çakışma biter — ölçümsüz, birincil kaynaksız tavsiye yığını. (İlk aramada tam olarak bu çıktı: 8 sonucun 8'i blog/pazarlama içeriği.)
**Boşluklar → paralel hatlar:**
- **Boşluk A:** worktree'nin BELGELİ sınırı ne? → git birincil dokümanı + iki harness'ın (Claude Code, OpenAI Codex) kendi dokümanı.
- **Boşluk B:** worktree paylaşılan `.git`'i izole ETMEZ — o zaman alt-katmanda kim kilitliyor? → git `lockfile` API kaynağı, `flock(2)/(1)`, lease/fencing literatürü.
- **Boşluk C:** "bayat okuma" bir dosya-sistemi semantiği sorusu → POSIX `rename`, `os.replace`, SQLite kilit modeli.
- **Boşluk D:** rakam nerede? → hakemli/ön-baskı ölçüm çalışmaları + CI orkestratörlerinin bildirim şemaları.
**Sentez sonucu:** A/B/C yakınsıyor (aynı mekanizma zinciri: izolasyon → kilit → atomik takas). D bağımsız ve en değerli katman: worktree'nin çözmediği şeyi sayıyla gösteriyor.

---

## ① git worktree izolasyonu: harness'lar nasıl kullanıyor, sınırı ne

### Mekanizma (birincil kaynak: git dokümanı)

`git worktree`, tek bir depo nesne-deposunu paylaşan birden çok çalışma dizini açar. Git dokümanının **DESCRIPTION** bölümü:

> "The new worktree is linked to the current repository, sharing everything except per-worktree files such as `HEAD`, `index`, etc."
> — https://git-scm.com/docs/git-worktree

Yani izolasyon **çalışma ağacı + `index` + `HEAD`** düzeyindedir; nesne deposu ve `refs/` PAYLAŞILIR. **REFS** bölümü:

> "In general, all pseudo refs are per-worktree and all refs starting with `refs/` are shared. Pseudo refs are ones like `HEAD` which are directly under `$GIT_DIR` instead of inside `$GIT_DIR/refs`. There are exceptions, however: refs inside `refs/bisect`, `refs/worktree` and `refs/rewritten` are not shared."
> — https://git-scm.com/docs/git-worktree

**Git'in kendi karşılıklı-dışlama kuralı** (aynı-branch kısıtı), **OPTIONS / `-f`, `--force`** bölümünde:

> "By default, `add` refuses to create a new worktree when _<commit-ish>_ is a branch name and is already checked out by another worktree, or if _<path>_ is already assigned to some worktree but is missing (for instance, if _<path>_ was deleted manually). This option overrides these safeguards."
> — https://git-scm.com/docs/git-worktree

Deneysellik uyarısı **BUGS** bölümünde duruyor:

> "Multiple checkout in general is still experimental, and the support for submodules is incomplete. It is NOT recommended to make multiple checkouts of a superproject."
> — https://git-scm.com/docs/git-worktree

### Harness-1: Claude Code (birinci-parti doküman)

Claude Code'da worktree bir CLI bayrağı, bir araç (`EnterWorktree`) ve bir ajan-frontmatter alanı (`isolation: worktree`) olarak üç yerde kurumsallaşmış:

> "Pass `--worktree` or `-w` with a name to create an isolated worktree and start Claude in it. By default, the worktree is created under `.claude/worktrees/<name>/` at your repository root, on a new branch named `worktree-<name>`"
> — https://code.claude.com/docs/en/worktrees (bölüm: *Start Claude in a worktree*)

Kritik olan: doküman worktree'nin **neyi izole etmediğini** açıkça yazıyor. *What worktrees share with the main checkout* bölümü:

> "**The repository's `.git` directory**: git commands in a worktree write to the main repository's shared `.git` directory, and sandboxing allows those writes, so commands such as `git commit` work from inside a worktree with the sandbox enabled."
> — https://code.claude.com/docs/en/worktrees

Aynı bölüm iki paylaşım daha sayıyor: proje-kapsamlı eklentiler ve izin onayları ("choosing 'Yes, and don't ask again' for a Bash command in a worktree session saves the rule to the main checkout's `.claude/settings.local.json`").

Dosya-sistemi izolasyonu **harness tarafından zorlanıyor** — yani git'e güvenilmiyor, ayrıca kapı konuyor. *How Claude Code enforces isolation* bölümü dört denetim sayıyor:

> "**File edits**: Claude Code blocks an `Edit`, `Write`, or `NotebookEdit` that targets a path in the main checkout."
> "**Git redirects**: Claude Code blocks a Bash or Monitor command that redirects git into the main checkout. The redirect can come through `git -C`, `--git-dir`, a `GIT_DIR` or `GIT_WORK_TREE` variable, or a `cd` into the main checkout before running git."
> "**Command shape**: Claude Code blocks a Bash or Monitor command it can't verify stays inside the worktree, even when the command runs no git at all. ... You can't turn this check off."
> — https://code.claude.com/docs/en/worktrees

Ve worktree'nin kendisi **kiralanıyor** (bkz. ②):

> "While an agent is running, Claude Code holds a `git worktree lock` on its worktree so that concurrent cleanup can't remove it, and releases the lock when the agent finishes."
> — https://code.claude.com/docs/en/worktrees (bölüm: *Clean up subagent and background-session worktrees*)

Gitignore'lu dosyaların kopyalanması `.worktreeinclude` ile:

> "The file uses `.gitignore` syntax. Only files that match a pattern and are also gitignored are copied, so tracked files are never duplicated."
> — https://code.claude.com/docs/en/worktrees

### Harness-2: OpenAI Codex (birinci-parti doküman)

> "Each worktree has its own copy of every file in your repo but they all share the same metadata (`.git` folder)."
> "Git prevents the same branch from being checked out in more than one worktree at a time." (hata: `fatal: 'feature/a' is already used by worktree at '<WORKTREE_PATH>'`)
> "Codex only copies ignored files that match `.worktreeinclude`; it doesn't copy other local files that Git doesn't track."
> "Codex keeps your most recent 15 Codex-managed worktrees"
> — https://learn.chatgpt.com/codex/environments/git-worktrees

**Yakınsama notu (yüksek güven):** İki bağımsız harness, aynı mekanizmayı (worktree + `.worktreeinclude` + saklama/temizlik politikası) aynı adla uygulamış. Bu, uzlaşıdan öte bir *arayüz standardı* oluşumudur.

### Sınır: worktree çakışmayı yok etmez, ERTELER

Paylaşılan `.git` yüzünden eşzamanlı git yazımları hâlâ çarpışır. Uygulama raporu (blog — kanıt hiyerarşisinde düşük katman, ölçüm İÇERMİYOR, öyle işaretliyorum):

> gözlenen hatalar: `"fatal: Unable to create '.git/index.lock'"`, `"Another git process seems to be running in this repository"`, `"cannot lock ref 'refs/heads/feature-x'"`; azaltma: git yazımlarını `flock` sarmalayıcıyla sıraya sokmak.
> — https://berry.sh/posts/codex-worktrees-git-locking/ · **bayrak:** blog, ölçüm/yeniden-üretim yordamı yok.

Asıl sınır ise mantıksal: dosya izolasyonu, **aynı işlevi** değiştiren iki ajanın birleştirme anındaki çakışmasını engellemez — çakışma PR/merge aşamasına taşınır. Bunun rakamı ④'te.

---

## ② dosya-kilidi / lease / advisory-lock desenleri ve tuzakları

### flock(2): tavsiye niteliğinde, açık-dosya-tanımına bağlı

**NOTES** bölümü:
> "flock() places advisory locks only; given suitable permissions on a file, a process is free to ignore the use of flock() and perform I/O on the file."

**DESCRIPTION** bölümü:
> "Locks created by flock() are associated with an open file description (see open(2)). This means that duplicate file descriptors (created by, for example, fork(2) or dup(2)) refer to the same lock."

**HISTORY** bölümü (NFS tuzağının tam metni):
> "Up to Linux 2.6.11, flock() does not lock files over NFS (i.e., the scope of locks was limited to the local system)."
> "Since Linux 2.6.12, NFS clients support flock() locks by emulating them as fcntl(2) byte-range locks on the entire file. This means that fcntl(2) and flock() locks do interact with one another over NFS."
> — https://man7.org/linux/man-pages/man2/flock.2.html

`flock(1)` (kabuk sarmalayıcısı) iki uyarı daha ekliyor:
> "Some filesystems (e. g. NFS and CIFS) have a limited implementation of flock(2) and flock may always fail."
> "flock does not detect deadlock."
> — https://man7.org/linux/man-pages/man1/flock.1.html

Pratik desen (aynı sayfadan, tek-örnek koşumu için): `[ "${FLOCKER}" != "$0" ] && exec env FLOCKER="$0" flock -en "$0" "$0" "$@"` — script kendi kendisinin kilit dosyası olur. Bekleme `-w/--wait` (kesirli saniye kabul eder), bloklamama `-n/--nonblock`, başarısızlık çıkış kodu varsayılan `1`.

### Kilit-dosyası + atomik takas: git'in `lockfile` API'si (en temiz belgeli desen)

Git'in kaynak başlığı deseni birinci ağızdan tarif ediyor (`lockfile.h`, dosya başı yorum bloğu):

> "Mutual exclusion and atomic file updates. When we want to change a file, we create a lockfile `<filename>.lock`, write the new file contents into it, and then rename the lockfile to its final destination `<filename>`. We create the `<filename>.lock` file with `O_CREAT|O_EXCL` so that we can notice and fail if somebody else has already locked the file, then atomically rename the lockfile to its final destination to commit the changes and unlock the file."

Bayat-kilit (stale lock) çözümü — **süreç ölümüne dayanıklılık**:

> "Automatic cruft removal. If the program exits after we lock a file but before the changes have been committed, we want to make sure that we remove the lockfile. This is done by remembering the lockfiles we have created in a linked list and setting up an `atexit(3)` handler and a signal handler that clean up the lockfiles."

Okuyucu garantisi (③ ile köprü):

> "Please note that lockfiles only block other writers. Readers do not block, but they are guaranteed to see either the old contents of the file or the new contents of the file (assuming that the filesystem implements `rename(2)` atomically)."
> — https://raw.githubusercontent.com/git/git/master/lockfile.h

**Tuzak:** `atexit`/sinyal işleyicisi `SIGKILL`'i ve makine çökmesini yakalayamaz; kalan `.git/index.lock` sonraki her yazmayı bloke eder ve **elle** silinmesi gerekir:

> "If the editing process is terminated or becomes unresponsive, the index.lock file can be left behind... This orphaned index.lock file will prevent other Git processes from editing the repository."
> — https://learn.microsoft.com/en-us/azure/devops/repos/git/git-index-lock

Git'in worktree yönetim dosyaları için bayat-kayıt toplayıcısı ayrı çalışır (`git worktree prune`, `gc.worktreePruneExpire`) — https://git-scm.com/docs/git-worktree

### Kiralama (lease): süreli kilit + yenileme

Kubernetes'in `coordination.k8s.io/Lease` nesnesi kanonik biçim:

> "Distributed systems often have a need for _leases_, which provide a mechanism to lock shared resources and coordinate activity between members of a set."
> alanlar: `holderIdentity`, `leaseDurationSeconds`, `renewTime`; kullanım: "only one instance of the component should be actively running while the other instances are on stand-by"
> — https://kubernetes.io/docs/concepts/architecture/leases/

**Kiralamanın temel tuzağı — Kleppmann'ın argümanı:** kira zaman aşımıyla düşer ama süreç bunu bilmez:

> "if the GC pause lasts longer than the lease expiry period, and the client doesn't realise that it has expired, it may go ahead and make some unsafe change."
> "GC can pause a running thread at _any point_, including the point that is maximally inconvenient for you (between the last check and the write operation)."
> Çözüm: "a fencing token is simply a number that increases (e.g. incremented by the lock service) every time a client acquires the lock." — depolama katmanı daha düşük token'lı yazımı reddeder.
> — https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html

**Ajan dünyasında bu tam olarak uygulanmış:** Claude Code, worktree kilidini bir kiralama gibi işletiyor ve sahibi ölünce kirayı **süpürgeyle geri alıyor**:

> "The sweep also releases a lock Claude Code set for a session whose process has exited, so a killed background session doesn't leave its worktree permanently locked. The sweep never releases a lock you set yourself with `git worktree lock`."
> — https://code.claude.com/docs/en/worktrees

Ayırt edici tasarım detayı: makinenin koyduğu kilit geri alınabilir, **insanın koyduğu kilit asla** geri alınmaz. (Jarvis açısından: Katman-1/Katman-2 ayrımının kilit-düzeyindeki karşılığı.)

Ajan-içi görev talebi de kilitle korunuyor:
> "Task claiming uses file locking to prevent race conditions when multiple teammates try to claim the same task simultaneously."
> — https://code.claude.com/docs/en/agent-teams (bölüm: *Assign and claim tasks*)

---

## ③ bayat-okuma (stale read): atomic-rename / write-then-swap ve SQLite

### POSIX `rename()` garantisi — desenin temeli

**DESCRIPTION** bölümü (dosyalar için):
> "In this case, a link named _new_ shall remain visible to other threads throughout the renaming operation and refer either to the file referred to by _new_ or _old_ before the operation began."
> — https://pubs.opengroup.org/onlinepubs/9699919799/functions/rename.html

Yani okuyucu ya ESKİ tam içeriği ya YENİ tam içeriği görür; "yarım dosya" ve "dosya yok" penceresi oluşmaz. Bu, `write-then-swap`'ın (geçici dosyaya yaz → `rename` ile takas et) tek dayanağıdır.

Standart kütüphane karşılığı:
> "If successful, the renaming will be an atomic operation (this is a POSIX requirement)." — `os.replace()`
> — https://docs.python.org/3/library/os.html

**Tuzak-1 (aynı dosya sistemi):** "The operation may fail if _src_ and _dst_ are on different filesystems" — aynı sayfa. Geçici dosya HEDEFLE AYNI dizinde açılmalı; `/tmp`'ye yazıp taşımak atomikliği bozar.
**Tuzak-2 (atomiklik ≠ dayanıklılık):** takas görünürlüğü atomiktir ama diske inme garantisi değildir; `fsync` gerekir ve tampon boşaltma ayrı adımdır:
> "If you're starting with a buffered Python file object _f_, first do `f.flush()`, and then do `os.fsync(f.fileno())`, to ensure that all internal buffers associated with _f_ are written to disk." — https://docs.python.org/3/library/os.html
**Tuzak-3 (dosya sistemine bağımlılık):** git'in kendi notu garantiyi koşullu veriyor — "assuming that the filesystem implements `rename(2)` atomically" (https://raw.githubusercontent.com/git/git/master/lockfile.h).

### SQLite eşzamanlılık modeli

Tek-yazar kuralı ve okur-yazar ayrışması, **WAL dokümanı**:
> "WAL provides more concurrency as readers do not block writers and a writer does not block readers." (bölüm 1. Overview)
> "However, since there is only one WAL file, there can only be one writer at a time." (bölüm 2.2. Concurrency)
> — https://sqlite.org/wal.html

WAL'ın ağ dosya sistemi yasağı (aynı sayfa):
> "All processes using a database must be on the same host computer; WAL does not work over a network filesystem." (bölüm 1)
> "The wal-index greatly improves the performance of readers, but the use of shared memory means that all readers must exist on the same machine. This is why the write-ahead log implementation will not work on a network filesystem." (bölüm 2.2)

Rollback-journal modundaki kilit durumları ve tek-RESERVED kuralı:
> "Only a single RESERVED lock may be active at one time, though multiple SHARED locks can coexist with a single RESERVED lock."
> "An EXCLUSIVE lock is needed in order to write to the database file. Only one EXCLUSIVE lock is allowed on the file and no other locks of any kind are allowed to coexist."
> "SQLite uses POSIX advisory locks to implement locking on Unix." — ve bunlar "known to be buggy or even unimplemented on many NFS implementations"; tavsiye: "Your best defense is to not use SQLite for files on a network filesystem."
> — https://sqlite.org/lockingv3.html

Çakışma anındaki pratik davranış (`SQLITE_BUSY` yönetimi):
> "sets a busy handler that sleeps for a specified amount of time when a table is locked" · "The handler will sleep multiple times until at least 'ms' milliseconds of sleeping have accumulated" · sonra "the handler returns 0 which causes sqlite3_step() to return SQLITE_BUSY."
> — https://sqlite.org/c3ref/busy_timeout.html

**Jarvis'e doğrudan sonuç:** `veri/baglam.sqlite` üzerinde N ajan koşuyorsa, okurlar serbest ama **yazar tek**; ikinci yazar `SQLITE_BUSY` alır. Doğru çözüm bir uygulama-seviyesi kuyruk + `busy_timeout`, "her ajan kendi yazsın" değil. Ve veritabanı asla ağ paylaşımında tutulmamalı.

---

## ④ çoklu-ajan çakışma vakaları/ölçümleri ve orkestratör bildirim şemaları

### En güçlü ölçüm: 33.596 ajan PR'ı, 2.807 depo (hakemsiz ön-baskı, ama yöntemi açık)

**Kaynak:** George Xu, Arjun Subramanian, Nithilan Karthik, *AI Agent Pull Requests on GitHub: Frequency, Structure, and Merge Conflict Rates*, arXiv:2607.04697v2, 7 Temmuz 2026 — https://arxiv.org/abs/2607.04697
**Bayrak:** ön-baskı (hakem süreci beyan edilmemiş); veri penceresi Aralık 2024–Temmuz 2025 (bölüm 7 *External Validity*). Aşağıdaki rakamlar PDF'ten doğrudan okundu (ilk WebFetch dönüşümü rakamları çıkaramamıştı; PDF sayfa okumasıyla teyit edildi).

**Eş-etkinlik yaygınlığı (bölüm 5.1, Tablo 1):**
| Pencere k (gün) | Depo eş-etkinlik | PR eş-etkinlik |
|---|---|---|
| 0 | %40,2 [%38,4–42,0] | %79,4 [%79,0–79,9] |
| ±1 | %50,7 | %93,3 |
| ±3 | %52,2 | %94,3 |
| ±7 | %53,4 [%51,5–55,2] | %95,0 |

Ajan dağılımı (bölüm 5.1): OpenAI Codex 21.799 PR, GitHub Copilot 4.970, Devin 4.827, Cursor 1.541, Claude Code 459.

**Çakışma oranları (bölüm 5.3, gerçek üç-yollu merge tekrarı, N=716 değerlendirilebilir çift / 747):**
> "**Intra-Agent Pairs** (601 evaluable out of 625): 19.8% textual conflict rate (119/601, 95% CI [16.8%, 23.2%])."
> "**Cross-Agent Pairs** (115 evaluable out of 122): 41.7% textual conflict rate (48/115, 95% CI [33.1%, 50.9%])."
> — arXiv:2607.04697v2, bölüm 5.3

**Çakışmanın yapısı (bölüm 5.3, Tablo 2):** çakışma tipi — content %57,6 · modify/delete %26,8 · add/add %15,1 · diğer %0,5. Çakışan dosya kategorisi — kaynak kod %84,4 · varlık %5,1 · config & CI %4,0 · bağımlılık manifesti & lockfile %3,9 · doküman %2,6.

Yazarların yorumu (bölüm 6.1) — bu raporun ana dersi:
> "The textual conflict rate for identical agent instances was 19.8%, indicating that currently deployed agents do not have even the most basic level of horizontal awareness. Agents operate independently and in isolation, without knowledge that other agents of the same type are simultaneously accessing and altering the same files."
> Ve: "approximately 42% of conflict signals are structural (modify/delete or add/add reports), indicating that agents are not only editing the same lines, but also disagreeing about whether a file should exist at all."

**Ölçüm yöntemi (bölüm 4.2) — Jarvis'te yeniden üretilebilir:** boş bare depo → iki PR head'ini `refs/pull/N/head` ile çek → `git merge-base` → **`git merge-tree --write-tree $C_A $C_B`**; çıkış 0 = temiz, 1 = çakışma. Çalışma dizinine dokunmadığı için paralel/çok-iş parçacıklı koşulabilir.

**Ölçek uyarıları (bölüm 7):** yalnız metinsel katman ölçülüyor ("conservative lower bound"); ham çiftlerin %91,4'ü en aktif on depodan geliyor (bu yüzden depo başına tek çift örneklenmiş); cross-agent örneklem küçük (N=115).

**İkincil atıf (doğrudan doğrulanmadı — 2607.04697 bölüm 3 üzerinden aktarım):** Ogenrwot & Businge, *AgenticFlict*: "27.67% of agentic PRs conflicted with their bases". Bu rakamı ikincil kaynaktan aktarıyorum; asıl makaleye gidilmedi.

### İkinci ölçüm: kilitsiz (CRDT) koordinasyon

**CodeCRDT**, arXiv:2510.18893 (18 Ekim 2025) — https://arxiv.org/abs/2510.18893
> mekanizma: "observation-driven coordination pattern where agents coordinate by monitoring a shared state with observable updates and deterministic convergence"; "Using Conflict-Free Replicated Data Types (CRDTs), CodeCRDT enables lock-free, conflict-free concurrent code generation"
> ölçüm: 600 deneme (6 görev × 50 koşum × 2 mod); "up to 21.1% speedup on some tasks", "up to 39.4% slowdown on others", "100% convergence with zero merge failures", anlamsal çakışma "5-10%".

**Ders:** CRDT *metinsel* birleştirme başarısızlığını sıfırlıyor (%100 yakınsama) ama **anlamsal** çakışmayı sıfırlamıyor (%5-10) — ve paralellik kazancı görevden göreve işaret değiştiriyor (+%21,1 / −%39,4). Yani "çakışmasız birleştirme" ≠ "doğru sonuç" ve ≠ "daha hızlı".

### Üçüncü ölçüm: paralel ajanın maliyeti ve koordinasyon arızaları

Anthropic mühendislik yazısı — https://www.anthropic.com/engineering/multi-agent-research-system
> "multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2%"
> "agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats"
> koordinasyon arızası, birebir: "subagents misinterpreted the task or performed the exact same searches as other agents. For instance, one subagent explored the 2021 automotive chip crisis while 2 others duplicated work investigating current 2025 supply chains"
> erken hata: "spawning 50 subagents for simple queries"
> kapsam sınırı: "some domains that require all agents to share the same context or involve many dependencies between agents are not a good fit for multi-agent systems today. For instance, most coding tasks involve fewer truly parallelizable tasks than research"

### Orkestratörlerin bağımlılık/dışlama bildirim şemaları

Dört sistem, iki ayrı eksen kullanıyor: **sıralama (DAG)** ve **karşılıklı dışlama (mutex)**.

| Sistem | Sıralama bildirimi | Karşılıklı dışlama |
|---|---|---|
| GitHub Actions | `jobs.<job_id>.needs` — "To run jobs sequentially, you can define dependencies on other jobs using the `jobs.<job_id>.needs` keyword." | `concurrency` — "Use `concurrency` to ensure that only a single job or workflow using the same concurrency group will run at a time." Sıradaki iş `pending`'e düşer. — https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax |
| GitLab CI | `needs` — aşama sırasını kırar, DAG kurar: "Execute jobs earlier than the stage ordering."; artefakt erişimi `needs` ile sınırlanır | `resource_group` — pipeline'lar arası dışlama; işlem kipleri: `unordered` (varsayılan), `oldest_first`, `newest_first`, `newest_ready_first` — https://docs.gitlab.com/ci/resource_groups/ |
| Docker Compose | `depends_on` — "Compose creates services in dependency order"; ters yönde "Compose removes services in dependency order" | (yok; hazırlık koşulu var) `service_started` / `service_healthy` / `service_completed_successfully`; uyarı: "With short syntax, Compose does not wait for dependency services to be 'healthy' before starting a dependent service." — https://docs.docker.com/reference/compose-file/services/ |
| Apache Airflow | `>>` / `<<`, `set_upstream`/`set_downstream`, `chain()`, `cross_downstream()`; DAG = "directed acyclic graph" | (bu sayfada belgelenmiyor — `pools`/`max_active_tasks` bu sayfada geçmiyor) — https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html |
| Claude Code agent teams | paylaşılan görev listesi: "a pending task with unresolved dependencies cannot be claimed until those dependencies are completed"; tamamlanınca otomatik açılır | görev talebinde dosya kilidi; dosya çakışması için **kural**, mekanizma değil: "Two teammates editing the same file leads to overwrites. Break the work so each teammate owns a different set of files." — https://code.claude.com/docs/en/agent-teams |

**Desen okuması:** Olgun orkestratörlerin hiçbiri "bağımlılığı çalışma zamanında keşfet" demiyor; hepsi **bildirimsel, statik, döngüsüz** bir graf istiyor ve dışlamayı **adlandırılmış kaynak grubu** üzerinden veriyor (`concurrency group`, `resource_group`). Ajan sistemlerinde eksik olan tam da bu: 2607.04697'nin "horizontal awareness" dediği şey, CI dünyasında 10+ yıldır `needs` + `resource_group` olarak çözülmüş durumda.

---

## DESEN TABLOSU

| # | Desen | Nerede belgeli | Sınır / tuzak | URL |
|---|---|---|---|---|
| 1 | Worktree izolasyonu (çalışma ağacı + `index` ayrı, nesne deposu ortak) | git dokümanı, DESCRIPTION/REFS | `.git`, `refs/`, nesne deposu PAYLAŞILIR; submodule desteği eksik, "still experimental" (BUGS) | https://git-scm.com/docs/git-worktree |
| 2 | Aynı-branch kilidi (git'in kendi mutex'i) | git dokümanı OPTIONS `-f`; Codex dokümanı | `--force` ile devre dışı bırakılabilir → koruma gönüllü | https://git-scm.com/docs/git-worktree · https://learn.chatgpt.com/codex/environments/git-worktrees |
| 3 | Harness worktree bayrağı (`--worktree`, `isolation: worktree`) | Claude Code dokümanı | worktree "taze checkout"tur: bağımlılık/ortam ayrıca kurulmalı | https://code.claude.com/docs/en/worktrees |
| 4 | `.worktreeinclude` (gitignore'lu dosyaları taşı) | Claude Code + Codex dokümanları | yalnız gitignore'lu VE desene uyan dosyalar; `**/` desenleri tümüyle yok sayılan dizine ulaşmaz | https://code.claude.com/docs/en/worktrees |
| 5 | Yol-kapısı zorlaması (ana checkout'a yazmayı harness engeller) | Claude Code, *How Claude Code enforces isolation* | `git -C`/`GIT_DIR`/heredoc gibi kaçış yolları ayrı ayrı kapatılmak zorunda; "command shape" denetimi kapatılamaz | https://code.claude.com/docs/en/worktrees |
| 6 | Worktree kirası + bayat-kira süpürgesi | Claude Code, *Clean up subagent...* | `-p` koşumları kilit bırakır; insanın koyduğu kilit süpürülmez | https://code.claude.com/docs/en/worktrees |
| 7 | Kilit dosyası `O_CREAT\|O_EXCL` + `rename` ile commit | git `lockfile.h` | `SIGKILL`/çökme → yetim `index.lock`, elle silme gerekir | https://raw.githubusercontent.com/git/git/master/lockfile.h |
| 8 | Yetim kilit tanılama/kurtarma | Azure DevOps / git index.lock kılavuzu | "git süreci koşuyor mu" kontrolü el yordamı; otomatik TTL yok | https://learn.microsoft.com/en-us/azure/devops/repos/git/git-index-lock |
| 9 | `flock(2)` advisory lock | flock(2) NOTES/DESCRIPTION | tavsiye niteliğinde (uymayanı bağlamaz); fd paylaşımında aynı kilit | https://man7.org/linux/man-pages/man2/flock.2.html |
| 10 | `flock(1)` ile komut serileştirme | flock(1) DESCRIPTION/EXAMPLES | NFS/CIFS'te "may always fail"; kilitlenme (deadlock) tespiti YOK; `-w` yoksa süresiz bekler | https://man7.org/linux/man-pages/man1/flock.1.html |
| 11 | Kiralama (TTL + `renewTime` + `holderIdentity`) | Kubernetes Leases | süre dolarken duraklayan sahip kirayı düştüğünü bilmez | https://kubernetes.io/docs/concepts/architecture/leases/ |
| 12 | Fencing token (artan sayaç, depoda doğrulama) | Kleppmann, *How to do distributed locking* | depolama katmanının token'ı denetlemesi ŞART; yalnız kilit servisi yetmez | https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html |
| 13 | write-then-swap (aynı dizine geçici dosya + `rename`) | POSIX `rename` DESCRIPTION; `os.replace` | farklı dosya sistemi → başarısız; atomiklik ≠ dayanıklılık (`fsync` ayrı); FS'in atomik `rename` uygulaması varsayılır | https://pubs.opengroup.org/onlinepubs/9699919799/functions/rename.html · https://docs.python.org/3/library/os.html |
| 14 | SQLite WAL (okur-yazar ayrışması) | sqlite.org/wal.html §1, §2.2 | tek yazar; ağ dosya sisteminde ÇALIŞMAZ (paylaşımlı bellek `-shm` gerekir) | https://sqlite.org/wal.html |
| 15 | SQLite kilit merdiveni (SHARED→RESERVED→PENDING→EXCLUSIVE) | sqlite.org/lockingv3.html | tek RESERVED; POSIX advisory kilitleri NFS'te "buggy or even unimplemented" | https://sqlite.org/lockingv3.html |
| 16 | `busy_timeout` (uyu-ve-tekrar dene) | sqlite3_busy_timeout | süre dolunca yine `SQLITE_BUSY`; kuyruk/geri-çekilme uygulama işi | https://sqlite.org/c3ref/busy_timeout.html |
| 17 | Bildirimsel DAG: `needs` / `depends_on` / `>>` | GH Actions, GitLab, Compose, Airflow | Compose kısa sözdizimi hazır-olmayı BEKLEMEZ; sıralama ≠ dışlama | https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax · https://docs.gitlab.com/ci/yaml/ · https://docs.docker.com/reference/compose-file/services/ · https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html |
| 18 | Adlandırılmış kaynak grubu ile dışlama (`concurrency`, `resource_group`) | GH Actions `concurrency`; GitLab `resource_group` (4 işlem kipi) | grup adını yanlış seçmek dışlamayı ya çok geniş ya işlevsiz yapar; varsayılan kip `unordered` sıra garantisi vermez | https://docs.gitlab.com/ci/resource_groups/ |
| 19 | Hazırlık koşulu (`service_healthy`, `service_completed_successfully`) | Compose `depends_on` uzun sözdizimi | sağlık denetimi tanımlı değilse koşul kurulamaz | https://docs.docker.com/reference/compose-file/services/ |
| 20 | Posta kutusu / mesajla koordinasyon (paylaşılan dosya yerine) | Claude Code agent teams, *Architecture* | alıcı başına JSON dosyası; yazma başarısız olursa mesaj gitmez; bozuk kayıt ayıklanır | https://code.claude.com/docs/en/agent-teams |
| 21 | Görev-listesi claim + dosya kilidi + görev bağımlılığı | Claude Code agent teams | görev durumu gecikirse bağımlı görevler tıkanır (belgeli sınır) | https://code.claude.com/docs/en/agent-teams |
| 22 | Dosya-sahipliği bölümlemesi (her ajana ayrı dosya kümesi) | Claude Code agent teams, *Avoid file conflicts* | mekanizma değil KURAL; zorlayıcı yok → 2607.04697'deki %19,8 tam bu boşluk | https://code.claude.com/docs/en/agent-teams |
| 23 | CRDT ile kilitsiz yakınsama | CodeCRDT, arXiv:2510.18893 | metinsel çakışmayı sıfırlar, anlamsal çakışmayı sıfırlamaz (%5-10); hız kazancı görevden göreve −%39,4'e kadar düşebilir | https://arxiv.org/abs/2510.18893 |
| 24 | Merge-replay ile çakışma ÖLÇÜMÜ (`git merge-tree --write-tree`) | arXiv:2607.04697 bölüm 4.2 | yalnız metinsel katman; build/anlamsal çakışmayı görmez (alt sınır) | https://arxiv.org/abs/2607.04697 |
| 25 | `flock` sarmalayıcıyla git yazımlarını serileştirme (worktree'lerde) | berry.sh blog | **bayrak: blog, ölçüm yok**; tüm git yazımlarını tek boğaza sokar → paralellik kazancını kısar | https://berry.sh/posts/codex-worktrees-git-locking/ |

**Desen sayısı: 25.**

---

## İDDİALAR

1. git worktree, çalışma ağacını ve `index`i ajanlar arasında ayırır ama nesne deposunu ve `refs/`i paylaştırır — "sharing everything except per-worktree files such as `HEAD`, `index`, etc." (https://git-scm.com/docs/git-worktree).
2. Git, aynı branch'in iki worktree'de çıkarılmasını varsayılan olarak reddeder, ama `--force` bu korumayı kaldırır (https://git-scm.com/docs/git-worktree).
3. Git dokümanının BUGS bölümü çoklu checkout'u hâlâ "still experimental" sayar ve superproject için önermez (https://git-scm.com/docs/git-worktree).
4. Claude Code dokümanı, worktree içindeki git komutlarının ana deponun paylaşılan `.git` dizinine yazdığını açıkça beyan eder — yani worktree git meta-verisini izole ETMEZ (https://code.claude.com/docs/en/worktrees).
5. OpenAI Codex dokümanı aynı mimariyi bağımsız olarak doğrular: "Each worktree has its own copy of every file in your repo but they all share the same metadata (`.git` folder)" (https://learn.chatgpt.com/codex/environments/git-worktrees).
6. Codex varsayılan olarak yalnız en son 15 Codex-yönetimli worktree'yi saklar, yani worktree başına disk maliyeti bir saklama politikası gerektirecek kadar büyüktür (https://learn.chatgpt.com/codex/environments/git-worktrees).
7. Claude Code izolasyonu git'e bırakmaz; dört ayrı denetimle (dosya düzenleme, çalışma dizini, git yönlendirmesi, komut şekli) ana checkout'a yazmayı harness düzeyinde bloke eder (https://code.claude.com/docs/en/worktrees).
8. Claude Code, `git -C`, `--git-dir`, `GIT_DIR`, `GIT_WORK_TREE` ve `cd` üzerinden yapılan git yönlendirmelerini ayrı ayrı engellemek zorundadır — bu, yol-tabanlı izolasyonun kaçış yüzeyinin geniş olduğunun kanıtıdır (https://code.claude.com/docs/en/worktrees).
9. Claude Code, koşan ajanın worktree'sinde `git worktree lock` tutar ve ajan bitince bırakır — yani worktree bir kiralanmış kaynak olarak işletilir (https://code.claude.com/docs/en/worktrees).
10. Claude Code'un süpürgesi, süreci ölmüş bir oturumun bıraktığı kilidi geri alır ama kullanıcının elle koyduğu kilidi asla almaz — makine kirası geri alınabilir, insan kilidi alınamaz (https://code.claude.com/docs/en/worktrees).
11. `flock()` yalnızca tavsiye niteliğinde kilit koyar; uymayan bir süreç dosyaya serbestçe yazabilir (flock(2) NOTES, https://man7.org/linux/man-pages/man2/flock.2.html).
12. Linux 2.6.11'e kadar `flock()` NFS üzerinde kilitlemez; 2.6.12'den itibaren NFS istemcileri bunu tüm dosya üzerinde `fcntl(2)` bayt-aralığı kilidi olarak taklit eder (flock(2) HISTORY, https://man7.org/linux/man-pages/man2/flock.2.html).
13. `flock(1)` kılavuzu NFS ve CIFS'te aracın "may always fail" olabileceğini ve kilitlenme (deadlock) tespiti yapmadığını açıkça yazar (https://man7.org/linux/man-pages/man1/flock.1.html).
14. Git'in kilit deseni "`.lock` dosyasını `O_CREAT|O_EXCL` ile aç → yaz → `rename` ile hedefe taşı" üçlüsüdür ve karşılıklı dışlama ile atomik güncellemeyi tek mekanizmada birleştirir (https://raw.githubusercontent.com/git/git/master/lockfile.h).
15. Git kilitleri yalnız yazarları bloke eder; okuyucular bloklanmaz ve dosyanın ya eski ya yeni tam içeriğini görmeleri garanti edilir — bu garanti dosya sisteminin `rename(2)`'yi atomik uygulaması varsayımına bağlıdır (https://raw.githubusercontent.com/git/git/master/lockfile.h).
16. Git yetim `index.lock` bırakırsa sonraki tüm yazma işlemleri bloke olur ve kurtarma elle silmedir; TTL tabanlı otomatik kurtarma yoktur (https://learn.microsoft.com/en-us/azure/devops/repos/git/git-index-lock).
17. Kubernetes kiralamaları `holderIdentity`, `leaseDurationSeconds` ve `renewTime` üçlüsüyle ifade edilir ve lider seçimi için tek-aktif-örnek garantisi sağlar (https://kubernetes.io/docs/concepts/architecture/leases/).
18. Süreli kilitler tek başına güvenli değildir: sahip bir GC/duraklama sırasında kiranın düştüğünü fark etmeden yazabilir, bu yüzden artan "fencing token" ve depolama katmanında token denetimi gerekir (https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html).
19. POSIX `rename()`, hedef adın yeniden adlandırma boyunca kesintisiz görünür kalacağını ve ya eski ya yeni dosyayı göstereceğini garanti eder — write-then-swap deseninin tek dayanağı budur (https://pubs.opengroup.org/onlinepubs/9699919799/functions/rename.html).
20. Python `os.replace()` bu garantiyi doğrudan taşır ("If successful, the renaming will be an atomic operation (this is a POSIX requirement)") ama farklı dosya sistemleri arasında başarısız olabilir (https://docs.python.org/3/library/os.html).
21. Atomik takas görünürlük garantisidir, dayanıklılık garantisi değildir; tamponlu yazımda önce `flush()` sonra `os.fsync()` gerekir (https://docs.python.org/3/library/os.html).
22. SQLite WAL kipinde okurlar yazarı, yazar okurları bloke etmez, ama tek WAL dosyası olduğu için aynı anda yalnız bir yazar olabilir (https://sqlite.org/wal.html §1, §2.2).
23. WAL paylaşımlı bellek gerektirdiğinden tüm süreçler aynı makinede olmalıdır ve WAL ağ dosya sisteminde çalışmaz (https://sqlite.org/wal.html §1, §2.2).
24. SQLite'ın rollback kipinde aynı anda yalnız tek bir RESERVED kilidi aktif olabilir ve yazmak için EXCLUSIVE gerekir (https://sqlite.org/lockingv3.html).
25. SQLite belgesi POSIX advisory kilitlerinin birçok NFS uygulamasında hatalı ya da hiç uygulanmamış olduğunu söyler ve ağ dosya sisteminde SQLite kullanmamayı önerir (https://sqlite.org/lockingv3.html).
26. `sqlite3_busy_timeout` uyu-ve-tekrar-dene stratejisidir ve süre dolduğunda çağrı yine `SQLITE_BUSY` döner — yani kuyruklama sorumluluğu uygulamadadır (https://sqlite.org/c3ref/busy_timeout.html).
27. 33.596 ajan PR'ı ve 2.807 depoluk örneklemde, PR'ların %79,4'ü başka bir ajan PR'ıyla tam zamansal örtüşme içinde açıktır; ±7 günlük pencerede bu oran %95,0'a çıkar (arXiv:2607.04697v2, bölüm 5.1 ve Tablo 1, https://arxiv.org/abs/2607.04697).
28. Aynı ajanın ürettiği eş-etkin PR çiftlerinde gerçek üç-yollu merge tekrarıyla ölçülen metinsel çakışma oranı %19,8'dir (119/601, %95 GA [%16,8–23,2]) (arXiv:2607.04697v2, bölüm 5.3).
29. Farklı ajanların ürettiği çiftlerde aynı oran %41,7'ye çıkar (48/115, %95 GA [%33,1–50,9]) — yani çapraz-ajan çakışması ajan-içi çakışmanın yaklaşık iki katıdır (arXiv:2607.04697v2, bölüm 5.3).
30. Çakışmaların yaklaşık %42'si yapısaldır (modify/delete %26,8 + add/add %15,1): ajanlar yalnız aynı satırı değiştirmiyor, dosyanın var olup olmaması konusunda anlaşamıyor (arXiv:2607.04697v2, Tablo 2 ve bölüm 6.1).
31. Çakışan dosyaların %84,4'ü kaynak kod, yalnız %3,9'u bağımlılık manifesti/lockfile'dır — "çakışma çoğunlukla lockfile'dan gelir" varsayımı bu veriyle yanlışlanır (arXiv:2607.04697v2, Tablo 2).
32. Bu oranlar yalnız metinsel katmanı ölçtüğü için yazarlarca "conservative lower bound" ilan edilmiştir; build ve anlamsal çakışmalar sayılmamıştır (arXiv:2607.04697v2, bölüm 2 ve 7).
33. Çakışma ölçümü `git merge-tree --write-tree` ile çalışma dizinine dokunmadan yapılabilir; çıkış kodu 0 temiz, 1 çakışma demektir (arXiv:2607.04697v2, bölüm 4.2).
34. CRDT tabanlı kilitsiz koordinasyon 600 denemede %100 yakınsama ve sıfır birleştirme hatası verirken anlamsal çakışmayı %5-10 düzeyinde bırakır ve hız etkisi +%21,1 ile −%39,4 arasında değişir (arXiv:2510.18893, https://arxiv.org/abs/2510.18893).
35. Anthropic'in ölçümünde çok-ajanlı sistem tek ajana göre %90,2 daha iyi sonuç verirken yaklaşık 15 kat token harcar (https://www.anthropic.com/engineering/multi-agent-research-system).
36. Aynı yazıda belgelenen somut koordinasyon arızası, üç alt-ajandan ikisinin aynı aramayı tekrarlamasıdır — yani çakışma yalnız dosya düzeyinde değil, iş düzeyinde de oluşur (https://www.anthropic.com/engineering/multi-agent-research-system).
37. Anthropic, paylaşılan bağlam ve ajanlar-arası bağımlılık gerektiren alanların bugün çok-ajanlı sistemlere uygun olmadığını ve kodlama görevlerinin araştırmadan daha az gerçekten paralelleştirilebilir olduğunu beyan eder (https://www.anthropic.com/engineering/multi-agent-research-system).
38. GitHub Actions bağımlılığı `needs` ile bildirir, karşılıklı dışlamayı ise ayrı bir kavramla — `concurrency` grubuyla — sağlar ve sıradaki işi `pending` durumuna düşürür (https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).
39. GitLab `needs` ile aşama sırasını kırıp DAG kurar, `resource_group` ile pipeline'lar arası dışlama sağlar ve dört işlem kipi sunar: `unordered` (varsayılan), `oldest_first`, `newest_first`, `newest_ready_first` (https://docs.gitlab.com/ci/resource_groups/).
40. Docker Compose `depends_on` kısa sözdizimi yalnız başlatma sırası verir, hazır-olmayı BEKLEMEZ; beklemek için `service_healthy` veya `service_completed_successfully` koşulu gerekir (https://docs.docker.com/reference/compose-file/services/).
41. Airflow bağımlılıkları `>>`/`<<`, `set_upstream`/`set_downstream` ve `chain()` ile bildirimsel olarak kurar ve grafın döngüsüz olmasını şart koşar (https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html).
42. Claude Code agent teams, eşzamanlı görev talebindeki yarışı dosya kilidiyle çözer ve bağımlılığı çözülmemiş bekleyen bir görevin talep edilmesini engeller (https://code.claude.com/docs/en/agent-teams).
43. Aynı doküman, aynı dosyayı düzenleyen iki takım arkadaşının üzerine-yazmaya yol açtığını kabul eder ve çözümü mekanizma değil kural olarak verir: işi dosya sahipliğine göre böl (https://code.claude.com/docs/en/agent-teams).
44. Claude Code agent teams ajanlar-arası iletişimi paylaşılan dosya yerine alıcı başına JSON posta kutusuyla yapar ve mesajı ancak yazma başarılıysa "gönderildi" sayar (https://code.claude.com/docs/en/agent-teams).
45. Aynı doküman takım büyüklüğü için 3-5 arkadaş önerir ve daha fazlasında koordinasyon yükünün ve çakışma olasılığının arttığını, getirinin azaldığını beyan eder (https://code.claude.com/docs/en/agent-teams).

---

## GÜVEN KATMANLARI

**Yüksek güven (birincil doküman + çapraz doğrulanmış):** ①'in mekanizma anlatımı (git dokümanı + iki bağımsız harness dokümanı yakınsıyor); ②'nin `flock` ve `lockfile` kısmı (man page + git kaynak kodu); ③'ün tamamı (POSIX + Python + SQLite birincil dokümanları); ④'ün şema tablosu (dört orkestratörün kendi dokümanı).

**Orta güven (tek çalışma, ön-baskı, hakem beyanı yok):** 27-33 numaralı iddialar (arXiv:2607.04697). Yöntem şeffaf ve yeniden üretilebilir, güven aralıkları verilmiş; ama tek çalışma, tek veri kümesi (AIDev-pop), Aralık 2024–Temmuz 2025 penceresi ve cross-agent örneklemi N=115.

**Düşük güven / işaretli:** iddia 34 (CodeCRDT — tek çalışma, sentetik görevler, hız sonucu işaret değiştiriyor); tablo satırı 25 (berry.sh blogu — ölçüm yok).

## BULUNAMAYAN / DOĞRULANAMAYAN (dürüstlük kaydı)

- **"N ajan tek repoda" için kontrollü deney:** aranan biçimde (N'yi değiştirip çakışma oranını ölçen bir deney) bulunamadı. Eldeki en iyi şey gözlemsel: 2607.04697 gerçek GitHub PR'larını tekrar-birleştiriyor, N'yi kontrol etmiyor. Bu bir literatür boşluğudur; yazarların kendi sonuç bölümü de bunu istiyor: "Research going forward should develop programmatic orchestration mechanisms, define formalized live workspace communication protocols for active agents".
- **POSIX `fcntl` kilitlerinin bilinen "aynı süreçte herhangi bir fd kapanınca tüm kilitler düşer" tuzağı:** bu koşumda ham alıntıyla doğrulanamadı; iddia listesine ALINMADI.
- **Airflow'un `pools`/`max_active_tasks` karşılıklı dışlama mekanizmaları:** çekilen DAG kavram sayfasında geçmiyor; başka sayfada olabilir ama doğrulanmadı, tabloda "belgelenmiyor" olarak işaretlendi.
- **AgenticFlict'in %27,67 rakamı:** yalnız ikincil aktarımla (2607.04697 bölüm 3) elde edildi; asıl makale doğrulanmadı.
- **403 / paywall:** bu koşumda hiçbir kaynakta 403 veya ödeme duvarıyla karşılaşılmadı. İki teknik engel oldu ve ikisi de aşıldı: (a) `docs.claude.com` → `code.claude.com` 301 yönlendirmesi, (b) `developers.openai.com` → `learn.chatgpt.com` 308 yönlendirmesi ve ardından `/docs/codex/...` yolunda 404 (doğru yol `/codex/environments/git-worktrees`). Ayrıca arXiv PDF'i metin dönüşümünde rakam vermedi; PDF sayfa okumasıyla doğrudan alındı.

## GEÇERLİLİK

**AS-OF 2026-08-29.** Şu durumlarda yeniden değerlendirilmeli: (a) git'in çoklu-checkout desteği "experimental" damgasını kaybederse, (b) harness'lar worktree ötesi bir eşzamanlılık ilkeli getirirse (ör. `.git` yazımlarını kendileri serileştirirse), (c) 2607.04697'nin ölçümü daha geniş/daha yeni veriyle yinelenirse — özellikle veri penceresi 2024-12/2025-07 olduğu için ajan davranışı o tarihten bu yana değişmiş olabilir.
