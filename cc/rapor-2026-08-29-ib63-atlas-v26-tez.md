# V26 ÖRNEKLEM-DENETİMİ — IB-63 tez raporları (A ve B)

**AS-OF: 2026-08-29** (tüm kaynak çekimleri bu tarihte yapıldı)
**Denetçi:** V26 örneklem-denetçisi (kural-tabanlı, deterministik) · **Rol:** yalnız sondaj-doğrulama, üretim yok
**Denetlenen dosyalar:**
`/Users/HasanSalihSahin/jarvis/cc/rapor-2026-08-29-ib63-atlas-tez-a.md` (315 satır)
`/Users/HasanSalihSahin/jarvis/cc/rapor-2026-08-29-ib63-atlas-tez-b.md` (384 satır)

---

## KIRPMA BEYANI (örneklem nasıl seçildi)

Seçim rastgele değil, sabit kuralla yapıldı (deterministik tasarım ilkesi):

**(a) Son üçte birdeki İLK kaynak-URL'li iddia — sınır hesabı:**
- **tez-a:** 315 satır → son üçte bir = satır **211–315**. Satır 211'den itibaren ilk URL taşıyan iddia = **satır 213** (KOŞUL KUTUSU K-14, *Build Systems à la Carte*, Definition 3.1). Satır 209'daki `bazel/issues/14294` URL'si sınırın (211) DIŞINDA kaldığı için kapsam dışı bırakıldı.
- **tez-b:** 384 satır → son üçte bir = satır **257–384**. Satır 257'den itibaren ilk URL taşıyan iddia = **satır 258–259** (Anthropic mühendislik yazısı, %90,2 karşılaştırması).

**(b) Görev emrinde adı geçen karar-taşıyan sondajlar** aynen alındı (tez-a 3 adet, tez-b 3 adet).

**Toplam sondaj: 8** (rapor başına 4). Sondaj dışı kalan iddialar denetlenmemiştir; bu rapor tam doğrulama değil, örneklem denetimidir.

**Yöntem notu:** Alıntı eşleşmeleri, LLM özeti üzerinden değil, kaynağın ham gövdesi indirilerek (`curl` + `pdftotext -layout` + dizgi araması) sınandı. Böylece "birebir mi" sorusu dönüştürme kaybından bağımsız cevaplandı. İndirilen ham kaynaklar: `/private/tmp/claude-501/-Users-HasanSalihSahin-jarvis/c2e5f984-3d73-4e11-9b9c-0024a427d82d/scratchpad/v26/`

---

## SONDAJ TABLOSU — RAPOR A (formal temel)

| # | Sondaj | İddia (raporda) | Kaynağa iniş | Sonuç |
|---|---|---|---|---|
| A1 | **Son üçte bir · ilk URL'li iddia** (satır 213–224) | BSaLC §3.6 Definition 3.1 doğruluk tanımı + çevrimsizlik ön-koşulu, birebir alıntı | PDF indirildi, metin katmanı çıkarıldı; `Definition 3.1 (Correctness)` §3.6, PDF s. 79:11 | **TUTTU** |
| A2 | **Bernstein üç-koşul formülasyonu** — alıntılandığı metin birebir eşleşiyor mu | Wikipedia *Parallel computing* + IUSB B424 ders notu (İKİNCİL damgalı) | Wikipedia ham wikitext + IUSB HTML çekildi | **TUTTU** |
| A3 | **Bazel / Make hermetiklik tanım alıntısı** | `bazel.build/basics/hermeticity`, `bazel.build/docs/sandboxing`, GNU Make §5.4.1 | Üç sayfa da canlı çekildi, dizgi araması | **TUTTU** |
| A4 | **"conflict" tanımının VT kaynağındaki birebir hali** | BHG Bölüm 2.1 "Histories", s.28 | `ccontrol.zip` (22,9 MB) indirildi → `IMAGES/CHAPTER2.PDF` → metin | **TUTTU** |

### A1 — Build Systems à la Carte, Definition 3.1
Kaynak: https://www.microsoft.com/en-us/research/uploads/prod/2018/03/build-systems.pdf (HTTP 200, 728.559 bayt) · AS-OF 2026-08-29
Kaynaktaki gerçek metin (§3.6 *Correctness of a Build System*, Definition 3.1):
> "The build result is correct if the following two conditions hold: • result and store agree on inputs, that is, for all input keys k ∈ I : getValue k result == getValue k store. In other words, no inputs were corrupted during the build. • The result is consistent with the tasks, i.e. for all non-input keys k ∈ O, the result of recomputing the corresponding task matches the value stored in the result: getValue k result == compute task result. A build system is correct if it produces a correct result for any given tasks, key and store."

Raporun eşlik eden iki alıntısı da bulundu:
- "It is hard to satisfy the above definition of correctness given a task description with cycles. All build systems discussed in this paper are correct only under the assumption that the given task description is acyclic." — TUTTU
- "The presented definition of correctness needs to be adjusted to accommodate non-deterministic tasks" — TUTTU
- §2.1 alıntısı "if the dependency graph is acyclic then each task needs to be executed at most once" — TUTTU (kaynakta: "Note that if the dependency graph is acyclic then each task needs to be executed at most once.")

**Sonuç: TUTTU.** Bölüm adı (§3.6), tanım numarası (Definition 3.1) ve alıntı gövdesi birebir.

### A2 — Bernstein üç-koşul formülasyonu
Kaynak-1: https://en.wikipedia.org/wiki/Parallel_computing (ham wikitext, HTTP 200) · AS-OF 2026-08-29
Kaynaktaki gerçek metin: "For ''P''<sub>''i''</sub>, let ''I''<sub>''i''</sub> be all of the input variables and ''O''<sub>''i''</sub> the output variables, and likewise for ''P''<sub>''j''</sub>."
Koşullar kaynakta, raporla **aynı sırada**: `I_j ∩ O_i = ∅` · `I_i ∩ O_j = ∅` · `O_i ∩ O_j = ∅`
Adlandırma cümleleri (üçü de birebir bulundu): "Violation of the first condition introduces a flow dependency, corresponding to the first segment producing a result used by the second segment. The second condition represents an anti-dependency, when the second segment produces a variable needed by the first segment. The third and final condition represents an output dependency: when two segments write to the same location, the result comes from the logically last executed segment."

Kaynak-2: https://www.cs.iusb.edu/~danav/teach/b424/depend.html (HTTP 200) · AS-OF 2026-08-29
Kaynaktaki gerçek metin: "Bernstein (1966) determined sufficient conditions for processes or threads to be executed simultaneously." · "I i - the set of memory locations read by process P i ." · "O i - the set of memory locations altered by process P i ." · "Two processes P 1 and P 2 can be executed in the same time if the output of one does not intersect the input or output of the other."

**Sonuç: TUTTU.** Rapor bu metinleri İKİNCİL damgasıyla verdiği ve Bernstein 1966 aslını paywall olarak bayrakladığı için atıf zinciri de tutarlı. Ek gözlem (sapma değil): Wikipedia'nın adlandırma cümleleri için verdiği dipnot Roosta 2000'dir, Bernstein 1966 değil; rapor bu cümleleri zaten "Wikipedia'daki adlandırma" diye sunmuş, Bernstein'a atfetmemiştir.

### A3 — Bazel / Make hermetiklik
https://bazel.build/basics/hermeticity (HTTP 200) · AS-OF 2026-08-29 — üç alıntı da birebir:
> "When given the same input source code and product configuration, a hermetic build system always returns the same output by isolating the build from changes to the host system."
> "Hermetic build systems treat tools as source code. They download copies of tools and manage their storage and use inside managed file trees."
> "Parallel execution : For given input and output, the build system can construct a graph of all actions to calculate efficient and parallel execution."

https://bazel.build/docs/sandboxing (HTTP 200) — iki alıntı da birebir:
> "Bazel's file system sandbox runs processes in a working directory that only contains known inputs, such that compilers and other tools don't see source files they should not access, unless they know the absolute paths to them."
> "Without action sandboxing, Bazel doesn't know if a tool uses undeclared input files (files that are not explicitly listed in the dependencies of an action). When one of the undeclared input files changes, Bazel still believes that the build is up-to-date and won't rebuild the action. This can result in an incorrect incremental build."

https://www.gnu.org/software/make/manual/html_node/Parallel-Disable.html (HTTP 200) — bölüm başlığı sayfada "5.4.1 Disabling Parallel Execution" olarak doğrulandı:
> "If a makefile completely and accurately defines the dependency relationships between all of its targets, then make will correctly build the goals regardless of whether parallel execution is enabled or not. This is the ideal way to write makefiles."
> "If the .NOTPARALLEL special target with no prerequisites is specified anywhere then the entire instance of make will be run serially, regardless of the parallel setting."

Ek olarak §4.14 alıntıları (`-M`, `main.o : main.c defs.h`, `name.d`) de https://www.gnu.org/software/make/manual/html_node/Automatic-Prerequisites.html sayfasında birebir bulundu.

**Sonuç: TUTTU.**

### A4 — "conflict" tanımının VT kaynağındaki birebir hali
Kaynak: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/05/ccontrol.zip (HTTP 200, 22.879.588 bayt) → `IMAGES/CHAPTER2.PDF` · AS-OF 2026-08-29
Kaynaktaki gerçek metin (OCR gürültüsü aynen korunmuştur — "conjlict" tarayıcı hatasıdır):
> "Two operations are said to conjlict if they both operate on the same data item and at least one of them is a Write. Thus, Read(x) conflicts with Write(x), while Write(x) conflicts with both Read(x) and Write(x). If two operations conflict, their order of execution matters."

**Sayfa denetimi (rapordaki sayfa beyanları ayrıca sınandı):** PDF sayfa akışı basılı sayfa numaralarıyla eşlendi.

| Rapordaki beyan | Gerçek basılı sayfa | Sonuç |
|---|---|---|
| conflict tanımı s.28 | 28 (`28 CHAPTER 2 I SERIALIZABILITY THEORY` başlıklı sayfa) | TUTTU |
| complete history / kısmi sıra s.29 | 29 | TUTTU |
| SG tanımı s.32 | 32 | TUTTU |
| Teorem 2.1 + "topologically sorted" s.33 | 33 | TUTTU |

Teorem 2.1 kaynaktaki hâli: "Theorem 2.1: (The Serializability Theorem) A history H is serializable iff SG(H) is acyclic." · ispat içi: "Since SG(H) is acyclic it may be topologically sorted." — ikisi de birebir.
Tarihçe tanımının üç koşulu kaynakta birebir (OCR'de madde numarası "2. H = U:,rT,;" olarak bozulmuş, rapor bunu "OCR düzeltilmiş gösterim" beyanıyla vermiş).

**Sonuç: TUTTU.**

---

## SONDAJ TABLOSU — RAPOR B (ajan/otomasyon çakışma yönetimi)

| # | Sondaj | İddia (raporda) | Kaynağa iniş | Sonuç |
|---|---|---|---|---|
| B1 | **Son üçte bir · ilk URL'li iddia** (satır 258–259) | Anthropic: çok-ajan tek-ajanı %90,2 geçti; ~15× token | Sayfa canlı çekildi, dizgi araması | **TUTTU** |
| B2 | **arXiv merge-tekrarı ölçümü** (%19,8 · %41,7 · N=716 · yapısal-oran bileşenleri) | arXiv:2607.04697v2 §5.3, Tablo 2 | PDF indirildi, sayfa sayfa ayrıştırıldı | **TUTTU** |
| B3 | **SQLite WAL "tek yazar / SQLITE_BUSY"** resmî doküman cümlesi | sqlite.org/wal.html §1, §2.2 + busy_timeout | İki sayfa canlı çekildi | **TUTTU** |
| B4 | **GH Actions `needs` + `concurrency`** şema alanları | docs.github.com workflow-syntax | Sayfa canlı çekildi (2,0 MB) | **TUTTU** |

### B1 — Anthropic çok-ajanlı sistem yazısı
Kaynak: https://www.anthropic.com/engineering/multi-agent-research-system (HTTP 200, 205.221 bayt) · AS-OF 2026-08-29
Kaynaktaki gerçek metin:
> "We found that a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval."
> "In our data, agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats."
> "subagents misinterpreted the task or performed the exact same searches as other agents. For instance, one subagent explored the 2021 automotive chip crisis while 2 others duplicated work investigating current 2025 supply chains"
> "spawning 50 subagents for simple queries"
> "some domains that require all agents to share the same context or involve many dependencies between agents are not a good fit for multi-agent systems today. For instance, most coding tasks involve fewer truly parallelizable tasks than research"

Beş alıntının beşi de birebir. **Sonuç: TUTTU.**

### B2 — arXiv:2607.04697v2 merge-tekrarı ölçümü
Kaynak: https://arxiv.org/pdf/2607.04697v2 (HTTP 200, 709.707 bayt, 8 sayfa) · PDF künyesi: başlık "AI Agent Pull Requests on GitHub: Frequency, Structure, and Merge Conflict Rates", yazarlar George Xu; Arjun Subramanian; Nithilan Karthik, CreationDate 2026-07-08 · AS-OF 2026-08-29

**Bölüm konumu:** §5.3 başlığı PDF **sayfa 3**'te "5.3 RQ3 — The Rates & Taxonomies of Textual [Conflict]" olarak doğrulandı; oran maddeleri bu bölümün gövdesinde.

Kaynaktaki gerçek metin (PDF s.3, §5.3):
> "• Intra-Agent Pairs (601 evaluatable out of 625): 19.8% textual conflict rate (119/601, 95% CI [16.8%, 23.2%])."
> "• Cross-Agent Pairs (115 evaluatable out of 122): 41.7% textual conflict rate (48/115, 95% CI [33.1%, 50.9%])."

**N=716 doğrulaması (iki bağımsız yerde):**
- PDF s.3, §4.2: "found that 716 were evaluatable (therefore, 31 could not be evaluated because 25 had their PR reference force-deleted and 6 had no accessible merge base – thus, 95.8% of the possible sample set)"
- PDF s.5, Figure 2 başlığı: "from the 747-pair merge replay. Error bars are 95% Wilson intervals (𝑁 = 716 evaluable)."
- Aritmetik tutarlılık: 625 + 122 = 747 · 601 + 115 = 716 ✓

**Yapısal-oran bileşenleri (PDF s.4, Tablo 2) — raporun beş dosya kategorisinin beşi de birebir:**

| Tablo 2 (kaynak) | Rapordaki değer | Sonuç |
|---|---|---|
| content 57,6% | %57,6 | TUTTU |
| modify/delete 26,8% | %26,8 | TUTTU |
| add/add 15,1% | %15,1 | TUTTU |
| other 0,5% | %0,5 | TUTTU |
| Source code 84,4% | %84,4 | TUTTU |
| Other / assets 5,1% | varlık %5,1 | TUTTU |
| Config & CI 4,0% | %4,0 | TUTTU |
| Manifest & lockfile 3,9% | %3,9 | TUTTU |
| Docs & text 2,6% | doküman %2,6 | TUTTU |

Yapısal toplam: 26,8 + 15,1 = **41,9% ≈ "yaklaşık %42"** — kaynak s.6'da bağımsız olarak teyit ediyor: "42% of the conflicts were structural (modify/delete or add/add) whereas 58% were content-based merges."

"horizontal awareness" alıntısı (PDF s.5, §6.1) birebir doğrulandı: "The textual conflict rate for identical agent instances was 19.8%, indicating that currently deployed agents do not have even the most basic level of horizontal awareness. Agents operate independently and in isolation, without knowledge that other agents of the same type are simultaneously accessing and altering the same files."

**Sonuç: TUTTU.** Sondajın hedeflediği dört bileşenin (19,8 · 41,7 · N=716 · yapısal-oran) dördü de sayfa/tablo gösterilerek kaynakta bulundu.

**Sapma kaydı (sayısal değil, dizgi düzeyinde — K-düşüşü tetiklemez):** Rapor iki yerde alıntıyı birebir damgalamışken bir kelime kaydırmış:
1. Rapor: "…are structural (modify/delete or add/add **reports**)" → kaynak: "…(modify/delete or add/add **operations**)".
2. Rapor: "601 **evaluable** out of 625" / "115 **evaluable** out of 122" → kaynak: "**evaluatable**".
Her iki durumda da sayı, oran, güven aralığı ve payda değişmemiştir; anlam kayması yoktur.

### B3 — SQLite WAL tek yazar / SQLITE_BUSY
Kaynak: https://sqlite.org/wal.html (HTTP 200) · AS-OF 2026-08-29
Kaynaktaki gerçek metin:
> §1 Overview: "WAL provides more concurrency as readers do not block writers and a writer does not block readers."
> §1 Overview: "All processes using a database must be on the same host computer; WAL does not work over a network filesystem."
> §2.2 Concurrency: "Writers merely append new content to the end of the WAL file. Because writers do nothing that would interfere with the actions of readers, writers and readers can run at the same time. **However, since there is only one WAL file, there can only be one writer at a time.**"
> §2.2: "The wal-index greatly improves the performance of readers, but the use of shared memory means that all readers must exist on the same machine. This is why the write-ahead log implementation will not work on a network filesystem."

Kaynak: https://sqlite.org/c3ref/busy_timeout.html (HTTP 200) — birebir:
> "This routine sets a busy handler that sleeps for a specified amount of time when a table is locked. The handler will sleep multiple times until at least "ms" milliseconds of sleeping have accumulated. After at least "ms" milliseconds of sleeping, the handler returns 0 which causes sqlite3_step() to return SQLITE_BUSY."

Bölüm numarası beyanları (§1 Overview, §2.2 Concurrency) sayfanın kendi içindekiler listesiyle eşleşiyor. **Sonuç: TUTTU.**

### B4 — GitHub Actions `needs` + `concurrency`
Kaynak: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax (HTTP 200, 2.020.160 bayt) · AS-OF 2026-08-29
Kaynaktaki gerçek metin:
> `jobs`: "A workflow run is made up of one or more jobs, which run in parallel by default. To run jobs sequentially, you can define dependencies on other jobs using the jobs.<job_id>.needs keyword."
> `concurrency`: "Use concurrency to ensure that only a single job or workflow using the same concurrency group will run at a time."
> `pending` davranışı: "When a concurrent job or workflow is queued, if another job or workflow using the same concurrency group in the repository is in progress, the queued job or workflow will be pending."

Şema alanlarının varlığı sayfanın kendi alan dizininde de doğrulandı: `concurrency`, `jobs.<job_id>.needs`, `jobs.<job_id>.concurrency` ayrı ayrı listeleniyor — yani raporun "iki ayrı eksen" (sıralama vs. karşılıklı dışlama) okuması şema düzeyinde karşılığı olan bir ayrım. **Sonuç: TUTTU.**

---

## SONUÇ

| Rapor | Sondaj | TUTTU | TUTMADI | ERİŞİLEMEDİ | **Karar** |
|---|---|---|---|---|---|
| **tez-a** (formal temel) | 4 | 4 | 0 | 0 | **PASS** |
| **tez-b** (ajan/çakışma) | 4 | 4 | 0 | 0 | **PASS** |

**RAPOR A — PASS.** Dört sondajın dördü tuttu. Ek olarak denetlenen dört BHG sayfa beyanı (s.28/29/32/33) da birebir doğru çıktı. K-damgası tetiklenmedi.

**RAPOR B — PASS.** Dört sondajın dördü tuttu; karar-taşıyan sayısal çekirdek (%19,8 · %41,7 · N=716 · yapısal-oran bileşenleri) kaynakta sayfa ve tablo gösterilerek bire bir bulundu. İki dizgi-düzeyi sapma (`reports`/`operations`, `evaluable`/`evaluatable`) kayda geçirildi; sayı, oran, güven aralığı ve payda etkilenmediği için K-damgası tetiklenmedi.

**Kapsam sınırı:** Bu bir örneklem denetimidir. tez-a'da 40, tez-b'de 45 numaralı iddia listesinin sondaj dışı kalan kısmı DENETLENMEMİŞTİR; PASS damgası "denetlenen 8 sondaj tuttu" demektir, "tüm iddialar doğrudur" demek değildir. Her iki raporun kendi bayrakladığı erişilemeyen kaynaklar (tez-a: Bernstein 1966, Karp-Miller 1966, Adya, Nix diff-hook; tez-b: AgenticFlict) bu koşumda ayrıca test edilmedi.
