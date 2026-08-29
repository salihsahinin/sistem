# İB-63 / Aile A — ANTİTEZ RAPORU (formal paralellik koşulları)

**Tarih:** 2026-08-29 · **Ajan:** ATLAS (antitez rolü, açık devil's advocate) · **Görev:** verilen 10 iddianın DEĞİLİNİ (¬T) savunacak belgeli karşı-kanıt aramak.
**AS-OF damgası:** tüm web kaynakları 2026-08-29'da çekildi; alıntılar o günkü sayfa/PDF metnindendir. Kaynakların kendi yayın tarihleri her maddede ayrıca yazılıdır (anakronizm freni, Karar 68).

## 0. Kırpma beyanı
Gönderen taraf listeyi **40 iddiadan karar-taşıyan 10 iddiaya** kırparak bana verdi. Kırpmayı ben yapmadım; kırpılan 30 iddianın içeriği bana gösterilmedi, dolayısıyla bu rapor **yalnız 10 iddia için** geçerlidir ve kırpılan kümede karşı-kanıt bulunup bulunmadığı hakkında hiçbir şey söylemez. Kaynaklar bilerek verilmedi; tüm URL'ler bu koşumda sıfırdan bulundu.

## 1. Yöntem ve doğrulama
- Araç: WebSearch + WebFetch; PDF'ler `curl` ile indirilip `pdftotext` ile düz metne çevrildi (WebFetch ikili PDF'i okuyamadı), alıntılar **ham metinden** grep ile çıkarıldı.
- Örneklem denetimi (V26, kural-tabanlı): çıktının son üçte birindeki kaynak iddiaları + **tüm sayısal iddialar** ikinci kez ham kaynaktan doğrulandı — MAST yüzdeleri/κ, Thinking Machines 1000/80/78/102/992-8, Anthropic 4×/15×, PostgreSQL granülerlik-terfisi cümlesi, CPI² 200 ms/40 ms ve 0,63× rakamları `curl`+`grep` ile birebir teyit edildi (aşağıda "doğrulandı" ibaresi taşıyanlar).
- Erişilemeyenler (bayrak): oneTBB "Controlling Chunking" sayfası **HTTP 404**; ACM DL ve Springer tam metinleri **paywall** (yalnız açık erişim sürümleri kullanıldı); DeepDyve **paywall**.

---

## İDDİA 1 — "Kök koşul üç ayrıklık şartıdır; DB/DAG/build kuralları bunun yeniden ifadesidir"
**HÜKÜM: ÇÜRÜDÜ** (yeterlilik iddiası olarak). Ayrıklık koşulları literatürde **gerekli ama yeterli değil** diye adlandırılır ve kapsamadığı en az dört çakışma sınıfı belgelidir.

1. **Koşulun kendisi "yeterli değil" diye işaretli.** Kaynak: ÇVUT B4M35PAP Advanced Computer Architectures ders notu, slayt başlığı *"Bernstein's conditions of parallelism"* (slayt 18-19). Ham PDF metninden birebir: `"Bernstein's conditions are necessary conditions of parallelization, but not sufficient …"` ve devamı `"All source (even indirect) dependencies Pi (i<j) of Pj have to be executed!"` — URL: https://cw.fel.cvut.cz/b181/_media/courses/b4m35pap/lectures/09_parallelism_b4m35pap-en.pdf (ders dönemi b181 = 2018/19).
2. **Kaynak-çekişmesi sınıfı (CPU/önbellek/bellek yolu) formalizmin dışındadır.** Kaynak: Zhang, Tune, Hagmann, Jnagal, Gokhale, Wilkes, *CPI²: CPU performance isolation for shared compute clusters*, EuroSys 2013 — bölüm: Abstract ve §1 Introduction. Birebir: `"Linux has few defenses against performance interference in shared resources such as processor caches and memory buses, so applications in a cloud can experience unpredictable performance caused by other programs' behavior."` ve §1'den saha örneği: `"1/66 of user traffic for an application in a cluster had a latency of more than 200 ms rather than 40ms for more than 1 hr"` (doğrulandı, PDF ham metni). Ayrıca §6'da kısma sonrası `"median victim production job's CPI is reduced to 0.63× it's pre-throttling value"` (doğrulandı). URL: https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/40737.pdf
3. **Yazma kümeleri ayrık olsa da anlam düzeyinde çakışma.** Kaynak: Martin Fowler, *SemanticConflict* (bliki). Birebir: `"By a semantic conflict I mean a situation where Jez and I make changes which can be safely merged on a textual level but cause the program to behave differently"`. URL: https://martinfowler.com/bliki/SemanticConflict.html
4. **Idempotens-dışı yan etki.** Kaynak: Stripe API Reference, bölüm *Idempotent requests*. Birebir: `"The API supports idempotency for safely retrying requests without accidentally performing the same operation twice."` ve kısıt: `"You can remove keys from the system automatically after they're at least 24 hours old. We generate a new request if a key is reused after the original is pruned."` — yani güvenlik küme-ayrıklığından değil, harici bir anahtar-defterinden gelir. URL: https://docs.stripe.com/api/idempotent_requests
5. **Donanım granülerliğinde sahte çakışma (false sharing).** Kaynak: Oracle *Sun Studio 12: OpenMP API User's Guide*, §6.2.1 "What Is False Sharing?". Birebir: `"This situation is called false sharing. If this occurs frequently, performance and scalability of an OpenMP application will suffer significantly."` URL: https://docs.oracle.com/cd/E19205-01/819-5270/aewcy/index.html

**Sonuç:** "kök formal koşul" iddiası ancak *veri bağımlılığı* ekseninde ayakta kalır; zaman, kaynak, yan etki ve anlam eksenleri koşulun dışındadır.

---

## İDDİA 2 — "Kümeler önceden tam beyan edilebilirse tespit tamamen statik yapılabilir"
**HÜKÜM: ÇÜRÜDÜ** (öncülün gerçeklenemediği belgeli sınıflar var; hermetiklik verilmiş bir özellik değil, zorla dayatılan ve delinebilen bir özellik).

1. **Dinamik bağımlılık sınıfı: graf inşadan önce hesaplanamaz.** Kaynak: Mokhov, Mitchell, Peyton Jones, *Build Systems à la Carte*, ICFP 2018 — §2.2 "Excel: Dynamic Dependencies at the Cost of Minimality". Ham PDF metninden birebir: `"it is impossible to compute the dependency graph before the build starts"`; aynı bölüm: `"Dynamic dependencies complicate minimality. In the above example, B1 should only be recomputed if A1 or C1 change, but not if (say) A2 changes; but these facts are not statically apparent."` Aynı makale §2.4'te Bazel için: `"As of writing, it is not possible to express dynamic dependencies in user-defined build rules; however some of the pre-defined build rules require dynamic dependencies"`. URL: https://www.microsoft.com/en-us/research/wp-content/uploads/2018/03/build-systems-final.pdf
2. **Aşırı-yaklaşıklama zorunluluğu.** Aynı bölüm, birebir: `"Excel implements a conservative approximation to minimality: it recomputes a formula if (i) the formula statically mentions a changed cell, or (ii) the formula uses a function like INDIRECT whose dependencies are not statically visible"` — statik tespit, ancak kaba üst-sınır olarak mümkün.
3. **Sandbox sızdırır: konak ortam gizlenmiyor.** Kaynak: Bazel resmî dokümantasyonu, sayfa *Sandboxing*, bölüm "What sandboxing does" / "Reasons for sandboxing". Birebir (ham HTML'den): `"Sandboxing doesn't hide the host environment in any way. Processes can freely access all files on the file system."` ve `"Without action sandboxing, Bazel doesn't know if a tool uses undeclared input files (files that are not explicitly listed in the dependencies of an action)."` Ayrıca platform sınırı: `"Both the linux-sandbox and the darwin-sandbox do not work in a 'nested' scenario due to restrictions in the mechanisms provided by the operating systems."` URL: https://bazel.build/docs/sandboxing
4. **Hermetiklik tanımı bile ihlal listesiyle birlikte gelir.** Kaynak: Bazel, *Hermeticity*. Birebir: `"When given the same input source code and product configuration, a hermetic build system always returns the same output by isolating the build from changes to the host system."` — ihlal kaynakları arasında `"Actions or tooling that create files non-deterministically, usually involving build IDs or timestamps"` ve `"System binaries that differ across hosts"`. URL: https://bazel.build/basics/hermeticity
5. **Tespit edilemeyen bağımlılık, üretim aracında kabul edilmiş kusur.** Kaynak: ccache manual (latest), bölüm *Caveats*. Birebir: `"The direct mode fails to pick up new header files in some rare scenarios."` URL: https://ccache.dev/manual/latest.html

---

## İDDİA 3 — "Sıralama zorunluluğu yalnız küme-kesişiminden doğar"
**HÜKÜM: ÇÜRÜDÜ.**

1. **Ayrık anahtarlar, yine de sıralama zorunluluğu — ve "doğru sıra" diye bir şey yok.** Kaynak: Lloyd, Freedman, Kaminsky, Andersen, *Don't Settle for Eventual (COPS)*, SOSP 2011 — §3 içinde "Get Transactions in COPS-GT". Ham PDF metninden birebir: `"there is no correct canonical ordering of the ACL and the album entries"`; aynı paragraf: `"her get(ACL) might return the old ACL, which permitted anyone (including Eve) to read it, but her get(album contents) might return the 'friends only' version."` ACL ve albüm **farklı anahtarlardır** (kesişim boş), buna rağmen kullanıcı-görünür tutarlılık sıralama/işlem gerektirir. URL: https://www.cs.cmu.edu/~dga/papers/cops-sosp2011.pdf
2. **Dış dünya yan etkisi: ikili-yazma (dual write) sorunu.** Kaynak: microservices.io, *Transactional outbox* deseni, "Problem"/"Forces" bölümleri. Birebir: `"messages must be sent to the message broker in the order they were sent by the service"` ve `"if a service sends a message after committing the transaction there's no guarantee that it won't crash before sending the message"`. Veritabanı ile broker ayrık kaynaklardır; ayrıklık sıralamayı serbest bırakmaz, tersine ek mekanizma gerektirir. URL: https://microservices.io/patterns/data/transactional-outbox.html
3. **Seri-çevrilebilirlik gerçek-zaman sırasını korumaz.** Kaynak: Jepsen, *Serializability* modeli sayfası. Birebir: `"does not impose any real-time, or even per-process constraints"` ve `"serializability does not require a per-process order between transactions. A process can observe a write, then fail to observe that same write in a subsequent transaction."` — yani kesişim yokluğu "her zaman yeniden-sıralanabilir" demek değil; tersine, kesişim olduğunda bile gerçek-zaman sırası garanti edilmez. URL: https://jepsen.io/consistency/models/serializable

---

## İDDİA 4 — "DAG çevrimsizliği + antizincir seçimi paralel çizelgeleme için yeterlidir"
**HÜKÜM: ÇÜRÜDÜ.**

1. **Dinamik görev üretimi: düğüm sayısı ayrıştırma anında bilinmiyor.** Kaynak: Apache Airflow resmî dokümanı, *Dynamic Task Mapping*, giriş bölümü. Birebir: `"Dynamic Task Mapping allows a way for a workflow to create a number of tasks at runtime based upon current data, rather than the Dag author having to know in advance how many tasks would be needed."` URL: https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/dynamic-task-mapping.html
2. **Çalışma-zamanı yeniden başlatma zorunluluğu (graf koşarken değişir).** Kaynak: *Build Systems à la Carte* §2.4: `"the internal build engine can cope with them by using a restarting task scheduler"` ve `"Bazel is not minimal in the sense that it may restart a task multiple times as new dependencies are discovered and rebuilt"` — antizincir seçimi, koşum sırasında geçersizleşebilir. URL: https://www.microsoft.com/en-us/research/wp-content/uploads/2018/03/build-systems-final.pdf
3. **Öncelik ters çevrimi: bağımlılık grafı temiz, sistem yine de çöküyor.** Kaynak: Glenn E. Reeves (JPL, Mars Pathfinder yazılım ekibi lideri), *What really happened on Mars?* e-postası, 1997-12. Aktarılan metinde: yüksek öncelikli `bc_dist` görevi `pipeWrite()` üzerinde bloke olur; düşük öncelikli ASI/MET görevi `"had called select, which had called pipeIoctl()...and was preempted"`; `select` mekanizması `"a mutual exclusion semaphore to protect the 'wait list' of file descriptors"` yaratır; sonuçta `bc_sched` görevi `"determined that the bc_dist task had not completed its cycle (a hard deadline in the system)"` ve reset başlatır. URL: https://www.cs.ccsu.edu/~pelletie/local/risks/programming-software/pathfinder.html
4. **Yeniden-deneme/iptal, grafın dışında ayrı bir kimlik defteri gerektirir** — Stripe idempotency (bkz. İddia 1, madde 4).

**Not (dürüstlük):** DAG + antizincir, *veri bağımlılığı* düzeyinde doğru bir çerçevedir; çürüyen kısım "yeterli" nitelemesidir.

---

## İDDİA 5 — "İzolasyon seviyeleri çakışma-güvenliğini tek başına çözer"
**HÜKÜM: ÇÜRÜDÜ.**

1. **Write skew: ayrık yazma kümeleri, bozulan değişmez.** Kaynak: Cockroach Labs blog, *What write skew looks like*, "Write skew" bölümü. Birebir: `"each transaction maintained a consistent view of the database and its write set didn't overlap with any concurrent transaction's write set"` — sonuç yine de `"x and y have been swapped, an outcome not possible in either serial execution."` URL: https://www.cockroachlabs.com/blog/what-write-skew-looks-like/
2. **Salt-okur işlem anomalisi: güncelleyenler seri-çevrilebilir olsa bile okur bozuk durum görür.** Kaynak: Jepsen, *Snapshot Isolation* modeli sayfası; izin verilen olgular listesinde `"a read-only transaction anomaly"` ve `"partially disjoint write sets"` ibareleri geçer; ayrıca `"does not impose any real-time constraints"`. URL: https://jepsen.io/consistency/models/snapshot-isolation — birincil makale: Fekete, O'Neil, O'Neil, *A read-only transaction anomaly under snapshot isolation*, SIGMOD Record 2004, https://dl.acm.org/doi/abs/10.1145/1031570.1031573 (**paywall bayrağı:** tam metin ACM DL'de kapalı; DeepDyve kopyası da paywall — bu maddede yalnız Jepsen'in açık metnini alıntıladım).
3. **SERIALIZABLE bile seri koşumda oluşmayacak hataları üretir.** Kaynak: PostgreSQL resmî dokümanı, §13.2.3 "Serializable Isolation Level". Birebir (doğrulandı): `"it doesn't always prevent errors from being raised that would not occur in true serial execution. In particular, it is possible to see unique constraint violations caused by conflicts with overlapping Serializable transactions even after explicitly checking that the key isn't present before attempting to insert it."` URL: https://www.postgresql.org/docs/current/transaction-iso.html
4. **Uygulama-düzeyi çözüm zorunluluğu:** aynı bölümdeki toplam-örneği (class 1/class 2, SUM sonuçlarının karşılıklı eklenmesi) izolasyonun kendisinin değil, uygulama değişmezinin devrede olduğunu gösterir.

---

## İDDİA 6 — "Girdi/çıktı kesişimi boşsa iki hedef paralel derlenebilir"
**HÜKÜM: ÇÜRÜDÜ.**

1. **Beyan edilmemiş çıktı (gizli yan-ürün) paralel derlemeyi kırar — üretim vakası.** Kaynak: Unidata/netcdf-fortran GitHub issue #64, bildiren `zbeekman`, 2017-07-19. Rapor edilen hata metni birebir: `"f951: Fatal Error: Can't rename module file 'tests.mod0' to 'tests.mod': No such file or directory"` ve `"Fatal Error: Can't open module file 'tests.mod' for reading at (1): No such file or directory"` — hedeflerin beyan edilen çıktıları ayrık (.o dosyaları), ancak derleyicinin ürettiği `.mod` dosyası paylaşılan gizli çıktıdır. URL: https://github.com/Unidata/netcdf-fortran/issues/64
2. **Paylaşılan önbellek: bozuk nesne dosyası önbellekte kalır.** Kaynak: ccache manual (latest), *Troubleshooting → Corrupt object files* bölümü. Birebir: `"bad object file sneaks into the cache for some reason, it will of course stay bad"`. URL: https://ccache.dev/manual/latest.html
3. **Hermetik olmayan eylem → yanlış/kayıp önbellek isabeti.** Kaynak: Bazel, *Debugging remote cache hits for remote execution*, "Checking your build" bölümü. Birebir: `"A likely source of discrepancy is something non-hermetic in the build causing the actions to receive different action keys across the two runs."` URL: https://bazel.build/remote/cache-remote
4. **Beyan edilmemiş girdi.** Bazel *Sandboxing* (bkz. İddia 2, madde 3): beyan dışı girdi değişince Bazel derlemeyi güncel sanar → yanlış artımlı build.

---

## İDDİA 7 — "Dosya-düzeyi granülerlik yeterlidir"
**HÜKÜM: ÇÜRÜDÜ** (hem "çok kaba" hem "çok yüzeysel" yönünden).

1. **Kaba granülerlik → sahte serileştirme (ölçülü mekanizma).** Kaynak: PostgreSQL §13.2.3 "Serializable Isolation Level", performans önerileri listesi. Birebir (doğrulandı): `"When the system is forced to combine multiple page-level predicate locks into a single relation-level predicate lock because the predicate lock table is short of memory, an increase in the rate of serialization failures may occur."` ve `"A sequential scan will always necessitate a relation-level predicate lock. This can result in an increased rate of serialization failures."` URL: https://www.postgresql.org/docs/current/transaction-iso.html
2. **Donanımda aynı hata: birim = önbellek satırı olduğunda mantıkça bağımsız değişkenler çakışır.** Oracle §6.2.1 (bkz. İddia 1, madde 5): `"False sharing degrades performance when all of the following conditions occur. Shared data is modified by multiple processors. Multiple processors update data within the same cache line."` URL: https://docs.oracle.com/cd/E19205-01/819-5270/aewcy/index.html
3. **Metin-düzeyi granülerlik (dosya ya da satır) yetersiz — anlam düzeyi gerekiyor.** Fowler, *SemanticConflict*: `"changes which can be safely merged on a textual level but cause the program to behave differently"`. URL: https://martinfowler.com/bliki/SemanticConflict.html

---

## İDDİA 8 — "okur∩okur her zaman paralel-güvenlidir"
**HÜKÜM: DARALDI** (yalıtılmış iki saf okurun birbiriyle çakışmadığına dair karşı-kanıt **bulunamadı**; ancak "okur kümesi zararsızdır" genellemesi çürüdü — okurlar eşzamanlı yazarlar/temizlik karşısında versiyonlama, işaretleme ve iptal mekanizması gerektirir).

1. **Okuma, yazma ile eşzamanlı olduğunda yırtılır (load/store tearing).** Kaynak: Linux çekirdeği, `Documentation/memory-barriers.txt`, "COMPILER BARRIER" bölümü (ham metin satır ~1779). Birebir: `"prevents \"load tearing\" and \"store tearing,\" in which a single large access is replaced by multiple smaller accesses"`; devamında `"Please note that GCC really does use this sort of optimization"`. URL: https://raw.githubusercontent.com/torvalds/linux/master/Documentation/memory-barriers.txt
2. **Salt-okur işlem, güncelleyenler seri-çevrilebilirken bile imkânsız bir durum okuyabilir** (Fekete/O'Neil/O'Neil anomalisi; Jepsen SI sayfası — bkz. İddia 5, madde 2). Bu, okurun kendi başına versiyon/anlık-görüntü disiplinine tabi olması gerektiğinin belgesidir.
3. **Okurlar, yazar tarafındaki temizlikle çakışır ve iptal edilir.** Kaynak: PostgreSQL resmî dokümanı, §26.4.2 "Handling Query Conflicts". Birebir: `"These conflicts are hard conflicts in the sense that queries might need to be canceled and, in some cases, sessions disconnected to resolve them."` Listelenen sebepler arasında: `"Application of a vacuum cleanup record from WAL conflicts with standby transactions whose snapshots can still 'see' any of the rows to be removed."` URL: https://www.postgresql.org/docs/current/hot-standby.html
4. **PostgreSQL'in `SERIALIZABLE READ ONLY DEFERRABLE`'ı, okurun bedelsiz olmadığının kurumsal itirafıdır** — §13.2.3: `"If you explicitly request a SERIALIZABLE READ ONLY DEFERRABLE transaction, it will block until it can establish this fact. (This is the only case where Serializable transactions block but Repeatable Read transactions don't.)"`

**Daraltılmış doğru biçim:** "Okur∩okur, *yazarların yokluğunda ve okumaların atomik olduğu granülerlikte* paralel-güvenlidir."

---

## İDDİA 9 — "Formal koşullar iş-birimi tanımından bağımsızdır"
**HÜKÜM: ÇÜRÜDÜ.**

1. **Aynı iş, farklı granülerlikte parçalanınca doğruluk hükmü değişir — ve sistemdeki DİĞER işlere bağlıdır.** Kaynak: Cerone, Gotsman, Yang, *Transaction Chopping for Parallel Snapshot Isolation*, §1 Introduction (Şekil 1(a)-(c) tartışması). Ham PDF metninden birebir: `"This chopping is correct in that any client-observable behaviour of the resulting chains could be produced by the original unchopped transactions."` — ve hemen ardından: `"If we added the transaction lookup2 in Figure 1(c), which returns the sum of the accounts acct1 and acct2, then the chopping of transfer would become incorrect: by executing lookup2 a client could observe the state with amnt missing from both accounts."` URL: https://software.imdea.org/~andrea.cerone/works/PSIchopping.pdf (temel çalışma: Shasha, Llirbat, Simon, Valduriez, *Transaction chopping: algorithms and performance studies*, ACM TODS 20(3), 1995 — https://dl.acm.org/doi/10.1145/211414.211427, **paywall bayrağı**).
2. **Kaba birim → sahte serileştirme:** PostgreSQL granülerlik terfisi (İddia 7, madde 1) aynı olgunun ölçülü hâlidir.
3. **İnce birim → patlayan kontrol maliyeti (sayısal).** Kaynak: Anthropic Engineering, *How we built our multi-agent research system*, "token" tartışması bölümü. Birebir (doğrulandı): `"agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats."` URL: https://www.anthropic.com/engineering/multi-agent-research-system
4. **Erişilemedi (bayrak):** oneTBB "Controlling Chunking" (grainsize ~ komut sayısı eşiği) sayfası HTTP **404** verdi; ince-granülerlik ek-yükü için sayısal eşik alıntısı bu koşumda alınamadı.

---

## İDDİA 10 — "Bu formal çerçeve LLM-ajan iş akışlarına doğrudan uygulanabilir"
**HÜKÜM: ÇÜRÜDÜ.**

1. **Ajan sisteminde çakışmalar okuma/yazma kümesi diliyle değil, iletişim/bağlam diliyle ortaya çıkıyor — ve ölçülmüş.** Kaynak: Cemri, Pan, Yang ve ark., *Why Do Multi-Agent LLM Systems Fail?* (arXiv:2503.13657, 2025-03; NeurIPS 2025 posteri). §Taksonomi ve Ek A'dan birebir tanımlar: `"FM-1.4: Loss of conversation history - Unexpected context truncation, disregarding recent interaction history and reverting to an antecedent conversational state."`, `"FM-2.4: Information withholding - Failure to share or communicate important data or insights that an agent possess and could impact decision-making of other agents if shared."`, `"FM-1.3: Step repetition - Unnecessary reiteration of previously completed steps in a process"`. Sayısal (ham PDF metninden doğrulandı): 14 arıza kipi / 3 kategori; taban `"150 traces"`, uzman anlaşması `"κ = 0.88"`, `"over 20 hours of annotation per expert for these 150 traces"`; oranlar: adım tekrarı `"(FM-1.3, 15.7%)"`, bağlam kaybı `"context loss (FM-1.4, 2.80%)"`, bilgi saklama `"(FM-2.4, 0.85%)"`, akıl-yürütme/eylem uyuşmazlığı `"(FM-2.6, 13.2%)"`, eksik doğrulama `"(FM-3.2, 8.20%)"`. URL: https://arxiv.org/pdf/2503.13657
2. **Aynı girdi → aynı çıktı varsayımı LLM koşumunda geçerli değil (formalizmin determinizm ön-koşulu düşüyor).** Kaynak: Thinking Machines Lab, *Defeating Nondeterminism in LLM Inference* (2025-09), "Experiments / How nondeterministic are completions?" bölümü. Birebir (doğrulandı): `"we generate 80 unique completions, with the most common of these occuring 78 times"` (1000 koşum, sıcaklık 0); `"the completions are actually identical for the first 102 tokens! The first instance of diverging completions occurs at the 103rd token"`; `"992 of the completions go on to generate \"Queens, New York\" whereas 8 of the completions generate \"New York City\""`. Kök sebep aynı sayfada: `"from the perspective of an individual user, the other concurrent users are not an 'input' to the system but rather a nondeterministic property of the system"` — yani **başkasının yükü, senin okuma kümene girmeyen ama çıktını değiştiren gizli bir girdidir**. URL: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
3. **Paylaşılan bağlam gereksinimi, paralelleştirmeyi doğrudan engelliyor (sağlayıcı beyanı).** Anthropic Engineering, aynı yazı: `"some domains that require all agents to share the same context or involve many dependencies between agents are not a good fit for multi-agent systems today. For instance, most coding tasks involve fewer truly parallelizable tasks than research"` (doğrulandı). Ve fiilî çakışma örneği: `"one subagent explored the 2021 automotive chip crisis while 2 others duplicated work investigating current 2025 supply chains"` — girdi/çıktı kümeleri ayrık, iş yine de çakıştı (yinelenen emek). URL: https://www.anthropic.com/engineering/multi-agent-research-system

---

## Özet tablo

| # | İddia (kısaltılmış) | Hüküm | Karşı-kanıt sayısı |
|---|---|---|---|
| 1 | Üç ayrıklık şartı kök/yeterli koşul | ÇÜRÜDÜ | 5 |
| 2 | Tam beyan → tamamen statik tespit | ÇÜRÜDÜ | 5 |
| 3 | Sıralama yalnız kesişimden doğar | ÇÜRÜDÜ | 3 |
| 4 | DAG + antizincir yeterli | ÇÜRÜDÜ | 4 |
| 5 | İzolasyon seviyeleri tek başına çözer | ÇÜRÜDÜ | 4 |
| 6 | Kesişim boşsa paralel derlenebilir | ÇÜRÜDÜ | 4 |
| 7 | Dosya-düzeyi granülerlik yeterli | ÇÜRÜDÜ | 3 |
| 8 | okur∩okur her zaman güvenli | **DARALDI** | 4 |
| 9 | Birim tanımından bağımsız | ÇÜRÜDÜ | 3 (+1 erişilemedi) |
| 10 | LLM-ajanlara doğrudan uygulanır | ÇÜRÜDÜ | 3 |

**9 ÇÜRÜDÜ · 1 DARALDI · 0 ÇÜRÜTEMEDİM · 0 ARANMADI · 38 karşı-kanıt maddesi · 24 ayrı URL.**

## Antitezin kendi sınırı (karşı-tarafa dürüstlük payı)
- Bulguların hiçbiri ayrıklık koşullarının **gerekliliğini** çürütmez; hepsi **yeterlilik** iddiasını çürütür. Tez tarafı "gerekli koşul + ek sigortalar" biçiminde yeniden yazılırsa bu raporun kanıtlarının çoğu ona zarar vermez.
- İddia 8'de saf okur-okur çakışması için karşı-kanıt **bulunamadı** (arama yapıldı: "read-read conflict", "readers conflict with each other", "read-only anomaly", "load tearing", "hot standby query conflict"). Bu maddede hüküm ÇÜRÜDÜ değil DARALDI'dır.
- 4 kaynak paywall/404 nedeniyle birincil metinden alınamadı (Fekete 2004 tam metni, Shasha 1995 TODS tam metni, DeepDyve kopyası, oneTBB chunking sayfası); bunların yerine açık erişimli ikincil/eşdeğer birincil kaynaklar kullanıldı ve her biri yukarıda bayraklandı.
- Zaman damgası: bu rapordaki tüm web erişimi 2026-08-29'dadır; Bazel/PostgreSQL/Airflow/ccache/Stripe dokümanları "current/latest" sayfalarıdır ve sürüm değişiminde metinleri değişebilir.
