# Tez Ajanı — Aile A (formal temel): İki iş biriminin GÜVENLE PARALEL koşulmasının klasik formal koşulları

**AS-OF:** 2026-08-29 (tüm çekimler bu tarihte yapıldı; canlı doküman sayfaları — Bazel/Make/Nix — değişebilir)
**Ajan:** ATLAS (research-agent), IB-63 Aile A
**Soru:** İki hesaplama/iş biriminin güvenle paralel koşulabilmesinin klasik formal koşulları nelerdir? (① paralel programlama ② veritabanı eşzamanlılık kontrolü ③ DAG çizelgeleme ④ build sistemleri)

## 0. Yöntem ve kaynak erişim notu

- **Birincil metin indirilebilen kaynaklar (tam metin elde, alıntılar bu metinlerden):** Bernstein-Hadzilacos-Goodman kitabı (yazarların ücretsiz bıraktığı 1987 baskısı, `ccontrol.zip` → `CHAPTER2.PDF`, `CHAPTER3.PDF`), Berenson vd. 1995 (Microsoft TR-95-51 PDF), Kwok & Ahmad 1999 (ACM CSUR ön-baskı PDF), Mokhov vd. 2018 "Build Systems à la Carte" (MSR PDF), GNU Make el kitabı, Bazel dokümanları, C++ taslak standardı.
- **ERİŞİLEMEYEN / BAYRAKLI:**
  - **Bernstein 1966 orijinal makale (IEEE Xplore, doc 4038883): tam metin PAYWALL** — çekim boş gövde döndürdü. Formüller bu yüzden ikincil kaynaklardan (Wikipedia + IUSB ders notu) alınmıştır, İKİNCİL olarak işaretlidir.
  - **Feautrier, "Bernstein's Conditions", Encyclopedia of Parallel Computing (Springer 2011): PAYWALL**; açık-erişim HAL kopyası (hal-01930890) **Anubis bot-koruması ile 403**.
  - **Karp & Miller 1966 (SIAM J. Appl. Math.): PAYWALL** — yalnız yayıncı özeti/arama özeti üzerinden, doğrudan sayfa çekimi yapılamadı; ilgili iddia İKİNCİL damgalı.
  - **Adya (MIT PMG) tezi ve ICDE-2000 makalesi: `pmg.csail.mit.edu` bu makineden BAĞLANTI KURULAMADI** (curl: connect fail; ayrıca ilk denemede 403). Adya'nın G0/G1/G2 formalizmi bu raporda **kullanılmadı**; yalnız varlığı işaret edildi.
  - **Kahn 1962 ve Eswaran vd. 1976 (ACM DL): künye doğrulandı (dblp/ACM DL kayıt sayfası), tam metin çekilmedi.**
- **Alıntı kuralı:** `>` ile verilen İngilizce cümleler kaynak metinden AYNEN alınmıştır, bölüm/sayfa beyanıyla. Türkçe karşılıkları ATLAS çevirisidir. Küme formülleri kaynakta düz metin olduğunda standart matematiksel gösterime çevrilmiştir (bu işaretlidir).
- **Türetilmiş ifade:** "[TÜRETİM]" damgalı satırlar kaynakta birebir bulunmayan, kaynak tanımlardan mantıksal olarak çıkarılan ifadelerdir.

---

## ① Paralel programlama teorisi — Bernstein koşulları

### KOŞUL KUTUSU K-1 — Bernstein Koşulları (bu alanın ADI olan koşul)

**Ad:** Bernstein's conditions / Bernstein koşulları.
**Orijinal kaynak:** A. J. Bernstein, "Analysis of Programs for Parallel Processing", *IEEE Transactions on Electronic Computers*, EC-15(5): 757-763, Ekim 1966. https://ieeexplore.ieee.org/document/4038883/ — **tam metin paywall (bayrak)**.

**Tanımlar** (Wikipedia "Parallel computing", Bernstein's conditions alt-bölümü — İKİNCİL, aynen):
> "For P_i, let I_i be all of the input variables and O_i the output variables, and likewise for P_j."

Ders-notu formülasyonu (Indiana Univ. South Bend, B424 "Dependency Analysis" — İKİNCİL, aynen):
> "I_i - the set of memory locations read by process P_i" · "O_i - the set of memory locations altered by process P_i" · "Two processes P_1 and P_2 can be executed in the same time if the output of one does not intersect the input or output of the other."

**KOŞUL (küme cebri):** P_i ve P_j paralel koşulabilir ⟸

```
(1)  I_j ∩ O_i = ∅      → ihlali: akış (flow / true) bağımlılığı
(2)  I_i ∩ O_j = ∅      → ihlali: anti-bağımlılık (anti-dependency)
(3)  O_i ∩ O_j = ∅      → ihlali: çıktı bağımlılığı (output dependency)
```

Wikipedia'daki adlandırma (aynen):
> "Violation of the first condition introduces a flow dependency, corresponding to the first segment producing a result used by the second segment." · "The second condition represents an anti-dependency, when the second segment produces a variable needed by the first segment." · "The third and final condition represents an output dependency: when two segments write to the same location, the result comes from the logically last executed segment."

**Kuvvet:** Bu koşullar **YETERLİ**, gerek değil. IUSB notu aynen: "Bernstein (1966) determined sufficient conditions..." — yani koşullar sağlanıyorsa paralellik güvenlidir; sağlanmıyorsa program yine de doğru olabilir (ör. iki yazma aynı değeri yazıyorsa).
**Sıkıştırılmış hâl:** "İki eşzamanlı hesaplama aynı veriye erişmemelidir, eğer erişenlerden en az biri o veriye YAZIYORSA."

### KOŞUL KUTUSU K-2 — Aynı koşulun modern normatif yeniden ifadesi (C++ bellek modeli)

**Kaynak:** C++ çalışma taslağı [intro.races] — https://eel.is/c++draft/intro.races (aynen):
> [intro.races]/2: "Two expression evaluations **conflict** if one of them modifies a memory location or starts or ends the lifetime of an object in a memory location and the other one reads or modifies the same memory location or starts or ends the lifetime of an object occupying storage that overlaps with the memory location."
> [intro.races]/17: "The execution of a program contains a **data race** if it contains two potentially concurrent conflicting actions, at least one of which is not atomic, and neither happens before the other... Any such data race results in undefined behavior."

**KOŞUL:** Güvenli paralellik ⟺ ∀ çakışan (conflicting) eylem çifti (a,b) için: `a happens-before b` ∨ `b happens-before a` ∨ her ikisi de atomik.
[TÜRETİM] K-1'in genelleştirilmesi: Bernstein statik küme-ayrıklığı ister; C++ modeli ayrıklık YOKSA bile **sıralama ilişkisi (happens-before)** kurulmuşsa güvenli sayar. Yani: `ayrıklık ∨ sıralama`.

### Çakışma tespiti deterministik olarak nasıl yapılır (alan ①)

1. **Statik (derleyici, tam deterministik):** Bernstein kümeleri döngü indislerine bağlı dizi erişimleri için doğrudan hesaplanamadığından, bağımlılık **testleri** kullanılır — GCD testi, Banerjee testi (https://en.wikipedia.org/wiki/Banerjee_test), ve afin (doğrusal) indisler için **tam (exact)** sonuç veren Omega testi: W. Pugh, "The Omega test: a fast and practical integer programming algorithm for dependence analysis", *CACM* 35(8): 102-114, 1992 — PDF: http://www.cs.umd.edu/~pugh/papers/omega.pdf. Bu testler `∃` bir tamsayı çözümü var mı sorusunu (Presburger aritmetiği / tamsayı programlama) çözerek `I ∩ O = ∅` sorusunu karara bağlar.
2. **Dinamik (koşum-anı):** Erişilen adreslerin gerçek okuma/yazma kümesi kaydedilir; çakışma = aynı adrese en az biri yazma olan iki erişim + aralarında happens-before yok (K-2). Bu, verilen bir koşum izi için deterministiktir (aynı iz → aynı karar).
3. **Sınır (dürüstlük notu):** Keyfi programlar için "bu iki blok bağımsız mı" sorusu genelde karar verilemezdir; pratik araçlar ya muhafazakâr (aşırı-yaklaşık, false positive) ya da iz-bazlıdır. Bu, aşağıdaki ④ alanının neden **beyan edilmiş girdi** (declared inputs) çözümüne kaydığını açıklar.

---

## ② Veritabanı eşzamanlılık kontrolü — serializability

Bu alanın standart formal referansı: **P. A. Bernstein, V. Hadzilacos, N. Goodman, *Concurrency Control and Recovery in Database Systems*, Addison-Wesley 1987** (kısaca BHG). Yazarlar baskısı tükendiği için kitabı ücretsiz bıraktı; tam PDF: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/05/ccontrol.zip (arşiv içinde `IMAGES/CHAPTER2.PDF`, `CHAPTER3.PDF`). Künye: https://dl.acm.org/doi/book/10.5555/17299. **Aşağıdaki alıntılar bu PDF'lerden birebir çıkarılmıştır.**

### KOŞUL KUTUSU K-3 — "Çakışma (conflict)" tanımı — BHG Bölüm 2.1 "Histories", s.28 (aynen)

> "Two operations are said to conflict if they both operate on the same data item and at least one of them is a Write. Thus, Read(x) conflicts with Write(x), while Write(x) conflicts with both Read(x) and Write(x). If two operations conflict, their order of execution matters."

**Küme cebri hâli** [TÜRETİM, K-1 ile aynı biçim]: iki işlem p, q çakışır ⟺ `item(p) = item(q) ∧ (p ∈ W ∨ q ∈ W)`. Yani ② alanının çakışma tanımı ① alanının Bernstein koşullarının ihlaliyle BİREBİR aynıdır (aynı öğe + en az biri yazma).

### KOŞUL KUTUSU K-4 — Tarihçe (history) = kısmi sıra — BHG Bölüm 2.1, s.29 (aynen, OCR düzeltilmiş gösterim)

> "let T = {T_1, T_2, ..., T_n} be a set of transactions. A complete history H over T is a partial order with ordering relation <_H where:
> 1. H = ∪ⁿ_{i=1} T_i;
> 2. <_H ⊇ ∪ⁿ_{i=1} <_i; and
> 3. for any two conflicting operations p, q ∈ H, either p <_H q or q <_H p."

Kritik nokta: **çakışmayan işlemler kısmi sırada SIRASIZ kalabilir** — paralellik tam olarak buradan doğar; çakışan her çift ise sıralanmak ZORUNDADIR.

### KOŞUL KUTUSU K-5 — Serileştirilebilirlik Teoremi — BHG Bölüm 2.3, Teorem 2.1 (aynen)

SG tanımı (s.32, aynen):
> "The serialization graph (SG) for H, denoted SG(H), is a directed graph whose nodes are the transactions in T that are committed in H and whose edges are all T_i → T_j (i≠j) such that one of T_i's operations precedes and conflicts with one of T_j's operations in H."

> **"Theorem 2.1: (The Serializability Theorem) A history H is serializable iff SG(H) is acyclic."**

**KOŞUL:** Eşzamanlı koşum güvenlidir (= bir seri koşuma denk) ⟺ çakışma-grafı ÇEVRİMSİZ.
İspatın anahtar adımı (aynen): "Since SG(H) is acyclic it may be topologically sorted." — yani ② alanı, ③ alanının (topolojik sıra) doğrudan tüketicisidir.

### KOŞUL KUTUSU K-6 — İki-fazlı kilitleme (2PL): çevrimi ÖNLEYEN çevrimiçi protokol — BHG Bölüm 3.2-3.3 (aynen)

Kilit çakışması (s.50, aynen):
> "Two locks pl_i[x] and ql_j[y] conflict if x = y, i ≠ j, and operations p and q are of conflicting type."

Basic 2PL kuralları (s.50, aynen):
> "1. When it receives an operation p_i[x] from the TM, the scheduler tests if pl_i[x] conflicts with some ql_j[x] that is already set. If so, it delays p_i[x]... If not, then the scheduler sets pl_i[x], and then sends p_i[x] to the DM.
> 2. Once the scheduler has set a lock for T_i, say pl_i[x], it may not release that lock at least until after the DM acknowledges that it has processed the lock's corresponding operation, p_i[x].
> 3. Once the scheduler has released a lock for a transaction, it may not subsequently obtain any more locks for that transaction (on any data item)."

> **"Theorem 3.6: Every 2PL history H is serializable."**

**Anlamı:** K-5 çevrim-yokluğunu POST-HOC (tüm tarihçe bilindikten sonra) sınar; 2PL aynı güvenceyi **çevrimiçi ve deterministik** olarak, kural (3) ile (büyüme/küçülme fazı ayrımı) sağlar.

### KOŞUL KUTUSU K-7 — İzolasyon seviyeleri: yasaklanan fenomenler (ANSI SQL eleştirisi)

**Kaynak:** H. Berenson, P. Bernstein, J. Gray, J. Melton, E. O'Neil, P. O'Neil, "A Critique of ANSI SQL Isolation Levels", *Proc. ACM SIGMOD 95*, s.1-10. PDF: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-95-51.pdf — **tam metin elde**; aşağıdaki formüller Bölüm 3-4'ten AYNEN:

> P0: w1[x]...w2[x]...(c1 or a1)  **(Dirty Write)**
> P1: w1[x]...r2[x]...(c1 or a1)  **(Dirty Read)**
> P2: r1[x]...w2[x]...(c1 or a1)  **(Fuzzy or Non-Repeatable Read)**
> P3: r1[P]...w2[y in P]...(c1 or a1)  **(Phantom)**
> P4: r1[x]...w2[x]...w1[x]...c1  **(Lost Update)**
> A5A: r1[x]...w2[x]...w2[y]...c2...r1[y]...(c1 or a1)  **(Read Skew)**
> A5B: r1[x]...r2[y]...w1[y]...w2[x]...(c1 and c2 occur)  **(Write Skew)**

Makalenin kendi uyarısı (Remark 3 ve 5, aynen): "ANSI SQL isolation should be modified to require P0 for all isolation levels." · "ANSI SQL isolation phenomena are incomplete. There are a number of anomalies that still can arise."

**KOŞUL biçimi:** Bir izolasyon seviyesi, **yasaklanan fenomen kümesi** olarak tanımlanır: L ⊨ H ⟺ H, L'nin yasak listesindeki hiçbir örüntüyü içermez. SERIALIZABLE, K-5 anlamında çevrimsizliktir; ara seviyeler ise çevrimlerin BAZI türlerine izin verir (ör. Snapshot Isolation A3'ü yasaklar ama A5B write skew'e izin verir — makale Remark 9).

**Serializability'nin ilk formal kaynağı:** K. P. Eswaran, J. N. Gray, R. A. Lorie, I. L. Traiger, "The Notions of Consistency and Predicate Locks in a Database System", *CACM* 19(11): 624-633, Kasım 1976 — https://dl.acm.org/doi/10.1145/360363.360369 (künye doğrulandı; tam metin çekilmedi). İki-fazlı kilitleme kuralı ("bir kilit bıraktıktan sonra yeni kilit isteyemez") bu makalede ortaya konmuştur.

### Çakışma tespiti deterministik olarak nasıl yapılır (alan ②)

1. **Graf sınaması (SGT):** Çakışan işlem çiftlerinden kenar üret → SG(H) → çevrim ara (DFS/Kahn). Deterministik; ama tüm tarihçeyi gerektirir, çevrimiçi kullanımda kenar-ekleme başına çevrim testi maliyetlidir.
2. **Kilit uyumluluk matrisi (2PL):** Çakışma, sabit bir tablo aramasıyla (read/write × read/write) karar verilir; kural (1) çakışan kilitleri eşzamanlı tutmaz. Tamamen deterministik, çevrimiçi, tarihçe bilgisi gerektirmez — bedeli: kilitlenme (deadlock) riski (BHG Bölüm 3.2: "An important and unfortunate property of 2PL schedulers is that they are subject to deadlocks.").
3. **Genelleme:** BHG Bölüm 2.5 (aynen): "since the proof of Theorem 2.1 only depends on the notion of conflict, not on the nature of the operations, it remains unchanged too. That is, a history is SR iff its SG is acyclic." → Read/Write dışı işlem türleri için "çakışma" tanımını genişletmek yeterlidir; teorem değişmez. **Bu, teorinin ajan/görev birimlerine taşınabilirliğinin formal dayanağıdır.**
4. Uygulamadan bağımsız (implementation-independent) daha ince formalizm: Adya-Liskov-O'Neil "Generalized Isolation Level Definitions" (ICDE 2000) DSG + G0/G1a/G1b/G1c/G2 fenomenleri — https://pmg.csail.mit.edu/pubs/adya00generalized-abstract.html — **BU MAKİNEDEN ERİŞİLEMEDİ (bağlantı hatası/403); içeriği bu raporda kullanılmadı.**

---

## ③ Dataflow / görev-grafı çizelgeleme — DAG'da paralellik

### KOŞUL KUTUSU K-8 — DAG modeli ve öncelik kısıtı

**Kaynak:** Y.-K. Kwok, I. Ahmad, "Static Scheduling Algorithms for Allocating Directed Task Graphs to Multiprocessors", *ACM Computing Surveys* 31(4): 406-471, Aralık 1999. Künye: https://dl.acm.org/doi/10.1145/344588.344618 · Tam metin PDF: https://www.dcc.fc.up.pt/~ines/aulas/0708/CG/papers/kwok.pdf (Bölüm 2 "The DAG Scheduling Problem", s.410-411, aynen):

> "A node in the DAG represents a task which in turn is a set of instructions which must be executed sequentially without preemption in the same processor."
> "The edges in the DAG, each of which is denoted by (n_i, n_j), correspond to the communication messages and precedence constraints among the nodes."
> "The source node of an edge is called the parent node while the sink node is called the child node. A node with no parent is called an entry node and a node with no child is called an exit node."
> **"The precedence constraints of a DAG dictate that a node cannot start execution before it gathers all of the messages from its parent nodes."**

### KOŞUL KUTUSU K-9 — İki düğüm ne zaman paralel koşar (kesin koşul)

[TÜRETİM — K-8'in öncelik kısıtından doğrudan]: G = (V, E) DAG'ında `⇝` erişilebilirlik (yönlü yol) ilişkisi olsun. `⇝` bir kısmi sıradır (DAG olduğu için yansımasız, geçişli, çevrimsiz).

```
n_i ∥ n_j  (güvenle paralel)  ⟺  ¬(n_i ⇝ n_j)  ∧  ¬(n_j ⇝ n_i)
```

Yani: **paralel koşabilen düğüm kümeleri = kısmi sıranın ANTİZİNCİRLERİDİR (antichain)**; karşılaştırılamaz (incomparable) düğümler paraleldir. Bir zamanda koşan düğüm kümesi S ⊆ V geçerlidir ⟺ S bir antizincirdir ve S'nin her elemanının tüm ataları tamamlanmıştır.

**Kritik ön-varsayım (ve bu ailenin gerçek riski):** Bu koşul yalnız **E, gerçek veri bağımlılıklarının TAMAMINI içeriyorsa** güvenlidir. E eksikse (beyan edilmemiş bağımlılık) graf yalan söyler; ⇝ ilişkisi Bernstein ihlalini görmez ve paralel koşum bozulur. Yani K-9, K-1'e indirgenir: **kenar var ⟺ Bernstein koşulu ihlal edilmiş.**

### KOŞUL KUTUSU K-10 — Topolojik sıra (linear extension)

- **Tanım/algoritma kaynağı:** A. B. Kahn, "Topological sorting of large networks", *CACM* 5(11): 558-562, Kasım 1962 — https://dl.acm.org/doi/10.1145/368996.369025 · künye doğrulaması: https://dblp.org/rec/journals/cacm/Kahn62.html (tam metin ACM DL'de, çekilmedi).
- **Kural:** Topolojik sıra, kısmi sıra `⇝`'nin bir doğrusal genişlemesidir: her (u,v) ∈ E için u, v'den önce gelir. Bir DAG'ın topolojik sıralaması vardır ⟺ graf çevrimsizdir; Kahn algoritması giriş-derecesi 0 olan düğümleri kuyruğa alır — **kuyruk boşalıp düğüm kaldıysa çevrim vardır** (deterministik çevrim tespiti).
- **③ ile ② arasındaki köprü (kaynak beyanlı):** BHG Teorem 2.1 ispatı topolojik sıralamayı doğrudan kullanır (Bölüm 2.3, aynen: "Since SG(H) is acyclic it may be topologically sorted... Let H_s be the serial history T_{i1} T_{i2} ... T_{im}").

### KOŞUL KUTUSU K-11 — Belirlenimlilik (determinacy) teoremi — dataflow kökeni

- **Kaynak:** R. M. Karp, R. E. Miller, "Properties of a Model for Parallel Computations: Determinacy, Termination, Queueing", *SIAM J. Appl. Math.* 14(6), Kasım 1966 — https://epubs.siam.org/doi/10.1137/0114108 — **PAYWALL (bayrak); doğrudan sayfa çekilemedi.**
- **İddia (İKİNCİL, yayıncı/arama özetinden):** hesaplama grafı modelinde "each such computation graph represents a unique computation, determined independently of operation times" — yani düğümlerin süreleri ve çizelgeleme ne olursa olsun sonuç AYNIDIR. Bu, paralel çizelgelemenin "güvenli" olmasının formal anlamıdır: **çizelge-bağımsız belirlenimlilik**.

### Çakışma tespiti deterministik olarak nasıl yapılır (alan ③)

1. **Erişilebilirlik / geçişli kapanış:** TC(G) hesapla (Warshall / DFS); `n_i ∥ n_j ⟺ (i,j) ∉ TC ∧ (j,i) ∉ TC`. Tam deterministik, O(V·E) veya matris çarpımı sınıfı.
2. **Kahn algoritması ile hem sıralama hem çevrim tespiti** aynı geçişte.
3. **Kenar üretimi = ①'in problemi:** Kenarların doğru üretilmesi (yani hangi görev çiftinin bağımlı olduğu) grafın kendisinde çözülmez; okuma/yazma kümelerinden (K-1) ya da beyandan (④) gelir.

---

## ④ Build sistemlerinde hedef bağımsızlığı — hermetiklik

### KOŞUL KUTUSU K-12 — Make: paralel-doğruluk koşulu (bu alanın en net tek cümlesi)

**Kaynak:** GNU Make el kitabı, §5.4.1 "Disabling Parallel Execution" — https://www.gnu.org/software/make/manual/html_node/Parallel-Disable.html (Edition 0.77, make 4.4.1; aynen):

> **"If a makefile completely and accurately defines the dependency relationships between all of its targets, then make will correctly build the goals regardless of whether parallel execution is enabled or not. This is the ideal way to write makefiles."**

Kaçış valfi (aynen): "If the .NOTPARALLEL special target with no prerequisites is specified anywhere then the entire instance of make will be run serially, regardless of the parallel setting."

**KOŞUL:** `paralel koşum ≡ seri koşum` ⟸ bağımlılık ilişkisi **tam (complete)** ve **doğru (accurate)**. Bu, K-9'un ön-varsayımının belge-düzeyinde beyanıdır.

### KOŞUL KUTUSU K-13 — Bazel: hermetiklik

**Kaynak:** https://bazel.build/basics/hermeticity (aynen):
> "When given the same input source code and product configuration, a hermetic build system always returns the same output by isolating the build from changes to the host system."
> "Hermetic build systems treat tools as source code. They download copies of tools and manage their storage and use inside managed file trees."
> "**Parallel execution**: For given input and output, the build system can construct a graph of all actions to calculate efficient and parallel execution."

**Kaynak:** https://bazel.build/docs/sandboxing (aynen):
> "Bazel's file system sandbox runs processes in a working directory that only contains known inputs, such that compilers and other tools don't see source files they should not access, unless they know the absolute paths to them."
> "Without action sandboxing, Bazel doesn't know if a tool uses undeclared input files (files that are not explicitly listed in the dependencies of an action). When one of the undeclared input files changes, Bazel still believes that the build is up-to-date and won't rebuild the action. This can result in an incorrect incremental build."

**KOŞUL (küme cebri) [TÜRETİM, K-1'in dosya düzeyine izdüşümü]:** İki hedef/eylem A ve B paralel derlenebilir ⟺

```
(a)  inputs(A), outputs(A) TAM beyan edilmiş (hermetiklik: gerçek erişim ⊆ beyan)
(b)  outputs(A) ∩ inputs(B) = ∅   ∧   outputs(B) ∩ inputs(A) = ∅     [akış/anti bağımlılık yok]
(c)  outputs(A) ∩ outputs(B) = ∅                                      [çıktı bağımlılığı yok]
(d)  A ∉ deps*(B)  ∧  B ∉ deps*(A)                                    [K-9: antizincir]
```

(c)'nin araç-düzeyinde zorlanması: Bazel iki eylem aynı çıktı dosyasını üretirse derlemeyi hata ile durdurur ("file is generated by these conflicting actions") — örnek kayıt: https://github.com/bazelbuild/bazel/issues/14294. Yani (c) statik olarak, koşum öncesi, deterministik biçimde sınanır.

### KOŞUL KUTUSU K-14 — Build doğruluğunun formal tanımı (kuram)

**Kaynak:** A. Mokhov, N. Mitchell, S. Peyton Jones, "Build Systems à la Carte", *Proc. ACM Program. Lang.* 2(ICFP), Article 79, Eylül 2018 — PDF: https://www.microsoft.com/en-us/research/uploads/prod/2018/03/build-systems.pdf (§3.6 "Correctness of a Build System", Definition 3.1, aynen):

> "The build result is correct if the following two conditions hold:
> • result and store agree on inputs, that is, for all input keys k ∈ I: getValue k result == getValue k store. In other words, no inputs were corrupted during the build.
> • The result is consistent with the tasks, i.e. for all non-input keys k ∈ O, the result of recomputing the corresponding task matches the value stored in the result: getValue k result == compute task result.
> A build system is correct if it produces a correct result for any given tasks, key and store."

Çevrimsizlik ön-koşulu (aynen):
> "It is hard to satisfy the above definition of correctness given a task description with cycles. All build systems discussed in this paper are correct only under the assumption that the given task description is acyclic."

Ve ayrıca (§2.1, aynen): "if the dependency graph is acyclic then each task needs to be executed at most once."
Doğruluk tanımının belirlenimsiz görevler için ayarlanması gerektiği de açıkça yazılıdır (aynen): "The presented definition of correctness needs to be adjusted to accommodate non-deterministic tasks..."

### Dosya düzeyi bağımlılık ÇIKARIMI (inference) — nasıl

1. **Derleyici-güdümlü (Make sınıfı):** GNU Make el kitabı §4.14 "Generating Prerequisites Automatically" — https://www.gnu.org/software/make/manual/html_node/Automatic-Prerequisites.html (aynen): "most modern C compilers can write these rules for you, by looking at the `#include` lines in the source files. Usually this is done with the '-M' option to the compiler." Örnek çıktı (aynen): "main.o : main.c defs.h". Önerilen desen (aynen): "for each source file `name.c` there is a makefile `name.d` which lists what files the object file `name.o` depends on."
2. **Sandbox-güdümlü (Bazel sınıfı):** Bağımlılık ÇIKARILMAZ, **BEYAN EDİLİR**; sandbox beyan-dışı erişimi fiziksel olarak imkânsız kılar (yukarıdaki alıntı). Beyan eksikse eylem çalışma dizininde dosyayı bulamaz ve **hemen hata verir** — bu, "eksik kenar"ı sessiz yanlışlıktan gürültülü hataya çeviren mekanizmadır.
3. **İçerik-hash güdümlü (Nix sınıfı):** Girdi kapanımı hash'lenir; belirlenimlilik ikinci bir derleme ile sınanır — Nix el kitabı "Verifying Build Reproducibility" (`nix-build ... --check --keep-failed`), çıktılar farklıysa "derivation may not be deterministic" hatası: https://nix.dev/manual/nix/2.34/advanced-topics/diff-hook.html — **NOT: bu sayfa doğrudan çekilmedi, arama özetinden alındı; alıntı parçası doğrulanmamış sayılmalıdır (İKİNCİL).**

### Çakışma tespiti deterministik olarak nasıl yapılır (alan ④)

| Mekanizma | Ne yakalar | Deterministik mi | Kaynak |
|---|---|---|---|
| Bağımlılık grafı + topolojik sıra | K-9 antizincir ihlali | Evet | Make §5.4.1, Bazel hermeticity |
| Çıktı-çakışması kontrolü | `outputs(A) ∩ outputs(B) ≠ ∅` | Evet, koşum öncesi | bazel #14294 |
| Sandbox | beyan edilmemiş GİRDİ | Evet (erişim engellenir → hata) | bazel/docs/sandboxing |
| `-M` / `.d` dosyaları | başlık düzeyinde gerçek girdi kümesi | Evet (derleyici üretir) | make §4.14 |
| Yeniden-derle + karşılaştır (`--check`) | belirlenimsizlik / gizli girdi | Evet (iki koşum, fark) | Nix diff-hook (İKİNCİL) |

---

## SENTEZ — dört alanın TEK ortak koşulu

Dört alan da aynı çekirdeği farklı sözlükle söyler:

```
BİRİMLER A, B GÜVENLE PARALEL  ⟺
   (i)   W(A) ∩ (R(B) ∪ W(B)) = ∅   ∧   W(B) ∩ R(A) = ∅        [Bernstein, K-1]
   (ii)  R(·), W(·) kümeleri TAM ve DOĞRU beyan edilmiş         [hermetiklik, K-12/K-13]
   (iii) bağımlılık grafı ÇEVRİMSİZ ve A ∥ B antizincirinde     [K-5, K-9, K-10, K-14]
   —— ya da (i) sağlanmıyorsa: aralarında bir SIRALAMA zorlanmış [happens-before K-2 / 2PL K-6]
```

- (i) ihlali = "çakışma"; ② alanının conflict tanımı (K-3) ile ①'in Bernstein ihlali AYNI önermedir.
- (ii) formal teorinin dışındadır — teori kümeleri VERİLMİŞ sayar; pratikte hatalar buradan çıkar (Bazel'in "undeclared input" uyarısı, Make'in "completely and accurately" şartı).
- (iii) küresel tutarlılık koşuludur: ikili bağımsızlık yetmez, grafın bütünü çevrimsiz olmalıdır (K-5 çevrim = seri denklik yok).
- Yasak fenomenler (K-7) gösterir ki **paralellik-güvenliği ikili bir anahtar değil, bir MERDİVENDİR**: hangi çakışma sınıfına izin verildiği seçilerek daha zayıf ama daha hızlı rejimler tanımlanabilir; her seviye "hangi anomali örüntüsü yasak" olarak formalize edilir.

---

## İDDİALAR

1. Bernstein koşullarının orijinal kaynağı A. J. Bernstein'ın 1966 tarihli "Analysis of Programs for Parallel Processing" makalesidir (*IEEE Trans. Electronic Computers* EC-15(5):757-763) ve tam metni IEEE Xplore'da paywall arkasındadır — https://ieeexplore.ieee.org/document/4038883/
2. Bernstein koşulları üç küme-ayrıklığıdır: I_j ∩ O_i = ∅, I_i ∩ O_j = ∅, O_i ∩ O_j = ∅ — https://en.wikipedia.org/wiki/Parallel_computing
3. Bu üç koşulun ihlalleri sırasıyla akış (flow) bağımlılığı, anti-bağımlılık ve çıktı bağımlılığı adını alır — https://en.wikipedia.org/wiki/Parallel_computing
4. Bernstein'ın koşulları paralel koşum için YETERLİ koşullardır (gerek değil) — https://www.cs.iusb.edu/~danav/teach/b424/depend.html
5. C++ standardı iki değerlendirmeyi "conflict" sayar: biri bir bellek konumunu değiştiriyor ve diğeri aynı konumu okuyor ya da değiştiriyorsa — https://eel.is/c++draft/intro.races
6. C++ standardında veri yarışı, "potansiyel olarak eşzamanlı, çakışan, en az biri atomik olmayan ve aralarında happens-before bulunmayan" iki eylemdir ve tanımsız davranış üretir — https://eel.is/c++draft/intro.races
7. Afin dizi indisleri için bağımlılık (yani I∩O boş mu) sorusu Omega testiyle tam olarak (exact) karara bağlanabilir; kaynak W. Pugh, CACM 35(8):102-114, 1992 — http://www.cs.umd.edu/~pugh/papers/omega.pdf
8. Bernstein-Hadzilacos-Goodman kitabının 1987 baskısının tamamı yazarlarca ücretsiz yayımlanmıştır ve bölüm PDF'leri indirilebilir — https://www.microsoft.com/en-us/research/wp-content/uploads/2016/05/ccontrol.zip
9. BHG Bölüm 2.1'de çakışma tanımı aynen şudur: iki işlem aynı veri öğesi üzerinde çalışıyorsa ve en az biri Write ise çakışırlar — https://www.microsoft.com/en-us/research/wp-content/uploads/2016/05/ccontrol.zip (CHAPTER2.PDF, s.28)
10. BHG'de tarihçe (history) bir KISMİ SIRADIR ve yalnız çakışan işlem çiftlerinin sıralanması zorunludur; çakışmayanlar sırasız kalabilir — aynı kaynak, CHAPTER2.PDF s.29 koşul (3)
11. BHG Teorem 2.1 (Serileştirilebilirlik Teoremi): bir tarihçe serileştirilebilirdir ⟺ serileştirme grafı çevrimsizdir — aynı kaynak, CHAPTER2.PDF s.33
12. SG(H)'nin düğümleri H'de commit olmuş işlemler, kenarları ise T_i'nin bir işleminin T_j'nin bir işleminden önce gelip onunla çakıştığı çiftlerdir — aynı kaynak, CHAPTER2.PDF s.32
13. Teorem 2.1'in ispatı çevrimsiz grafın topolojik sıralanabilirliğine dayanır, yani veritabanı teorisi doğrudan DAG topolojik sırasını kullanır — aynı kaynak, CHAPTER2.PDF s.33
14. BHG Bölüm 2.5'e göre Teorem 2.1 yalnız "çakışma" kavramına dayandığı için Read/Write dışındaki işlem türlerine, çakışma tanımı genişletilerek, DEĞİŞMEDEN taşınır — aynı kaynak, CHAPTER2.PDF
15. Basic 2PL üç kuralla tanımlanır ve üçüncü kural (bir kilit bırakıldıktan sonra yeni kilit alınamaz) protokolün adını verir — aynı kaynak, CHAPTER3.PDF s.50
16. BHG Teorem 3.6: her 2PL tarihçesi serileştirilebilirdir — aynı kaynak, CHAPTER3.PDF
17. 2PL çizelgeleyicileri kilitlenmeye (deadlock) açıktır; bu, çevrimiçi determinizmin bedelidir — aynı kaynak, CHAPTER3.PDF Bölüm 3.2
18. Serializability ve iki-fazlı kilitleme kavramlarının birincil kaynağı Eswaran, Gray, Lorie, Traiger, CACM 19(11):624-633, 1976'dır — https://dl.acm.org/doi/10.1145/360363.360369
19. Berenson vd. 1995, ANSI SQL izolasyon fenomenlerini işlem-dizisi formülleriyle yeniden tanımlar: P0 w1[x]...w2[x], P1 w1[x]...r2[x], P2 r1[x]...w2[x], P3 r1[P]...w2[y in P] — https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-95-51.pdf
20. Aynı makale P4 (Lost Update) r1[x]...w2[x]...w1[x]...c1, A5A (Read Skew) ve A5B (Write Skew) r1[x]...r2[y]...w1[y]...w2[x] anomalilerini ekler ve ANSI fenomen listesinin EKSİK olduğunu (Remark 5) belirtir — aynı URL
21. Aynı makaleye göre ANSI SQL izolasyonu tüm seviyelerde P0'ı (Dirty Write) yasaklamalıdır, ama etmez (Remark 3) — aynı URL
22. Adya-Liskov-O'Neil'in uygulamadan bağımsız izolasyon formalizmi (DSG, G0/G1/G2) bu koşumda ERİŞİLEMEDİ (pmg.csail.mit.edu bağlantı hatası/403) ve rapora dahil edilmedi — https://pmg.csail.mit.edu/pubs/adya00generalized-abstract.html
23. Kwok & Ahmad (ACM CSUR 31(4), 1999) DAG öncelik kısıtını aynen şöyle tanımlar: bir düğüm, ebeveyn düğümlerinden gelen tüm mesajları toplamadan çalışmaya başlayamaz — https://www.dcc.fc.up.pt/~ines/aulas/0708/CG/papers/kwok.pdf
24. Aynı kaynakta DAG düğümü, aynı işlemcide kesintisiz ve sırayla çalışması gereken bir komut kümesi (görev) olarak tanımlanır — aynı URL
25. Optimal DAG çizelgeleme genel hâlde NP-tamdır, bu yüzden literatür sezgisel algoritmalara yönelmiştir — https://dl.acm.org/doi/10.1145/344588.344618
26. [TÜRETİM] İki DAG düğümü güvenle paraleldir ⟺ ikisi arasında hiçbir yönde yönlü yol yoktur, yani erişilebilirlik kısmi sırasında bir antizincir oluştururlar — dayanak: madde 23'teki öncelik kısıtı
27. Topolojik sıralama algoritmasının birincil kaynağı A. B. Kahn, CACM 5(11):558-562, 1962'dir — https://dl.acm.org/doi/10.1145/368996.369025 (künye: https://dblp.org/rec/journals/cacm/Kahn62.html)
28. Karp & Miller 1966 hesaplama-grafı modelinde sonucun işlem sürelerinden BAĞIMSIZ olarak tek (belirlenimli) olduğunu kanıtlar; makale paywall arkasındadır ve bu iddia yayıncı özeti üzerinden İKİNCİL olarak kaydedilmiştir — https://epubs.siam.org/doi/10.1137/0114108
29. GNU Make el kitabı §5.4.1: bir makefile tüm hedefleri arasındaki bağımlılık ilişkilerini eksiksiz ve doğru tanımlıyorsa, make hedefleri paralel koşum açık olsun olmasın DOĞRU inşa eder — https://www.gnu.org/software/make/manual/html_node/Parallel-Disable.html
30. Aynı sayfada `.NOTPARALLEL` özel hedefi, paralellik ayarından bağımsız olarak tüm make örneğini seri koşturur — aynı URL
31. GNU Make §4.14'e göre dosya düzeyinde bağımlılık, derleyicinin `-M` seçeneğiyle `#include` satırlarına bakılarak otomatik ÇIKARILIR ve `name.d` dosyalarına yazılır — https://www.gnu.org/software/make/manual/html_node/Automatic-Prerequisites.html
32. Bazel hermetikliği "aynı kaynak kodu ve ürün yapılandırması verildiğinde, derlemeyi ana makinedeki değişikliklerden yalıtarak her zaman aynı çıktıyı döndürmek" olarak tanımlar — https://bazel.build/basics/hermeticity
33. Bazel'e göre paralel koşum, verili girdi ve çıktılardan tüm eylemlerin grafının kurulabilmesi sayesinde mümkündür — https://bazel.build/basics/hermeticity
34. Bazel sandbox'ı, süreçleri yalnız BİLİNEN girdileri içeren bir çalışma dizininde koşturur — https://bazel.build/docs/sandboxing
35. Bazel dokümantasyonu açıkça belirtir: sandbox olmadan beyan edilmemiş girdi dosyaları görülmez ve bu YANLIŞ artımlı derlemeye yol açar — https://bazel.build/docs/sandboxing
36. Bazel'de iki eylemin aynı çıktı dosyasını üretmesi ("file is generated by these conflicting actions") derlemeyi durduran bir hatadır; bu, Bernstein'ın O_i ∩ O_j = ∅ koşulunun araç düzeyinde zorlanmasıdır — https://github.com/bazelbuild/bazel/issues/14294
37. "Build Systems à la Carte" (ICFP 2018) build doğruluğunu iki koşulla formalize eder: girdiler bozulmamıştır ve her girdi-olmayan anahtar için yeniden hesaplama depodaki değerle aynıdır — https://www.microsoft.com/en-us/research/uploads/prod/2018/03/build-systems.pdf
38. Aynı makale, ele aldığı tüm build sistemlerinin yalnız görev tanımı ÇEVRİMSİZ olduğu varsayımı altında doğru olduğunu açıkça yazar — aynı URL
39. Aynı makale, doğruluk tanımının belirlenimsiz (non-deterministic) görevler için ayrıca ayarlanması gerektiğini belirtir — aynı URL
40. Nix, `--check` bayrağıyla bir türevi yeniden inşa edip çıktıları karşılaştırarak belirlenimsizliği tespit eder; bu iddia doğrudan sayfa çekimiyle değil arama özetiyle alınmıştır (İKİNCİL, doğrulanmadı) — https://nix.dev/manual/nix/2.34/advanced-topics/diff-hook.html

---

## Geçerlilik ve sınırlar

- **Geçerlilik:** 2026-08-29. Klasik teoremler (Bernstein 1966, Karp-Miller 1966, Eswaran 1976, BHG 1987, Kahn 1962) zamana bağlı değildir; **Bazel/Make/Nix doküman alıntıları canlı sayfalardır ve değişebilir** (Make alıntısı Edition 0.77 / make 4.4.1 sürümündendir).
- **Sınır 1:** Bernstein 1966 ve Karp-Miller 1966 için birincil metin okunamadı (paywall); bu iki maddede formüller/ifadeler ikincil kaynaklardan alınmıştır ve öyle işaretlenmiştir.
- **Sınır 2:** Adya formalizmi erişilemediği için ② alanının "uygulamadan bağımsız izolasyon tanımları" ayağı EKSİKTİR; bu, ileri bir koşumda tamamlanmalıdır.
- **Sınır 3:** K-9 ve K-13'teki küme-cebri ifadeleri kaynaklarda birebir bu biçimde yazılı değildir; kaynak tanımlardan türetilmiş ve [TÜRETİM] damgasıyla ayrılmıştır.
- **Kullanılmayan/atılan hat:** dinamik yarış-dedektörleri (vektör saat, FastTrack sınıfı) için birincil kaynak doğrulanmadığından rapora alınmadı — uydurma yerine boşluk bırakıldı.
