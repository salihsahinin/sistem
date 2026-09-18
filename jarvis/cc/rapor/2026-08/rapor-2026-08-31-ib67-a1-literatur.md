# Antitez Literatür Taraması — IB-67 A1 (2026-08-31)

Künye: AS-OF 2026-08-31 · aile A1 · model sonnet · rejim maliyet-öncelikli · yöntem: adversarial WebSearch taraması (arXiv/ACL/NeurIPS-ICSE-FSE ağırlıklı, açık web).

## A67-1 (İB-53) — Kod-satırı+diyagram-geometri ortak IR, markdown-yerli, araç-bağımsız

Sorgular (birebir):
1. "source-location-preserving intermediate representation diagram code traceability file:line"
2. "bidirectional source mapping diagram to code SourcetrailDB SARIF Sprotty trace"
3. "literate diagram intermediate representation markdown native tool-independent layout geometry source position"

Bulunan en-yakın-komşular (arama-sonucu, açılmadı):
- SourcetrailDB (GitHub, CoatiSoftware) — kod-indeksleme DB'si, bakımsız; diyagram-layout geometrisi taşımıyor.
- Numbat / Pyrrha (Quarkslab blog) — SourcetrailDB'nin yeni mapping aracı; yine kod-tarafı, layout yok.
- Source map format spec (tc39.es/ecma426) — JS transpile bidirectional mapping, diyagram değil.
- lcodemaps (GitHub, abulka) — "Literate Code Maps": kaynak koddan diyagram üretme metodolojisi; markdown-yerli mi, IR şeması paylaşılıyor mu belirsiz [?].
- "A Parse-Then-Place Approach for Generating Graphic Layouts from Textual Descriptions" (arXiv 2308.12700) — metinden layout IR'si, kod-satırı referansı bileşeni yok görünüyor [?].
- USPTO patentleri (source-level debugging of intermediate code) — kod↔kod satır eşleme, diyagram bileşeni yok.

Yenilik durumu: **KISMİ**. Parçalar dağınık halde var: (a) kod-satırı↔ara-temsil eşleme (SourcetrailDB/source maps/debug info) çözülmüş bir problem; (b) metinden diyagram-layout IR'si (parse-then-place, Vega/VegaProf profiling IR) ayrı bir hat olarak var. Aramalar, bu ikisini AYNI şemada, markdown-yerli ve araç-bağımsız biçimde birleştiren yayınlanmış bir sistem GÖSTERMEDİ — ama negatif kanıt zayıf: SourcetrailDB/Sprotty/mdast-unist Point/Pandoc sourcepos gibi somut emsal isimleri arama sonuçlarında doğrudan karşılaştırmalı olarak çıkmadı (yalnız SourcetrailDB kısmen çıktı), yani tarama bu adaylara karşı tam eşleşme testi YAPAMADI.

Etiket: **DAYANAKSIZ** (iddia çürütülmedi ama "yok" hükmü de tam doğrulanamadı — mdast/unist Point, Pandoc sourcepos, SARIF, Sprotty trace ile doğrudan karşılaştırma bu turda elde edilemedi; ek tur gerekir).

## A67-2 (İB-49) — D2 için LLM benchmark yokluğu + metin-sayma vs SQL-devri + biçim↔verimlilik farkı

Sorgular (birebir):
1. "LLM benchmark D2 diagram language generation DSL Mermaid PlantUML Graphviz"
2. "LLM graph reasoning text vs SQL tool-offloading structural questions"
3. "graph serialization format token efficiency LLM input representation comparison"
4. (ek) ""D2" diagram language LLM benchmark evaluation Terrastruct dataset"

Bulunan en-yakın-komşular (arama-sonucu):
- **MermaidSeqBench** (arXiv 2511.14967) — NL-to-Mermaid sequence diagram benchmark; D2 DEĞİL.
- **OmniDiagram** (arXiv 2604.05514) — "Unified Diagram Code Generation via Visual Interrogation Reward"; kapsadığı diller [?] (D2 adı arama özetinde geçmedi).
- **M3²Bench** — LaTeX/Mermaid/PlantUML 17k örnek, D2 yok.
- **DW-Bench** (arXiv 2604.18964) — LLM'lerin veri-ambarı graf-topolojisi akıl yürütmesi; tool-use (SQL benzeri) tek-hop sorularda neredeyse mükemmel, çok-hop kompozisyonda %30-40 düşüyor — "SQL'e devretme daha iyi çalışır" örüntüsüyle UYUMLU ama D2 veya %96 vs %100 rakamlarıyla eşleşmiyor.
- **"Lost in Serialization"** (arXiv 2511.10234) — LLM graf-akıl yürütücülerinin serileştirme biçimine göre varyans/genelleme sorunu; doğrudan ilgili.
- Token-verimlilik: List-of-Edges/Structured-YAML en verimli (<3000 token), JSON-LD en verimsiz (>13000 token); CSV>HTML karşılaştırmasında CSV en verimli. **ONTO** (arXiv 2604.17512) JSON'a göre %46-51 token azaltımı — "insan-okunur ↔ LLM-verimli" gerilimiyle ilgili somut sayısal emsal (bizim 5,5× rakamıyla aynı değil ama aynı eksende).
- GraphLLM: yapısal bilgiyi encode ederek bağlam uzunluğunu %96,45 azaltıyor (D2 farklı bir mekanizma — yine de "yapısal temsil ile token tasarrufu" bulgusu zaten literatürde var).

Yenilik durumu: **KISMİ→DÜŞTÜ (parça bazında)**. D2'ye özel LLM benchmark'ı için doğrudan bir yayın BULUNAMADI (bu alt-iddia ayakta — YOK-bulundu). Ama "graf-yapısal soru çözümünde tool-offload (SQL-vari) yaklaşımın metin-sayma yaklaşımından daha güvenilir olduğu" ve "biçim seçiminin LLM verimliliğinde büyük (kat mertebesinde) fark yarattığı" alt-iddiaları TEK TEK zaten yayınlanmış literatürle örtüşüyor (DW-Bench, Lost-in-Serialization, ONTO, GraphLLM). Birleşim (D2 + bu iki bulgu + %96/%100/5,5× spesifik rakamları) hâlâ özgün görünüyor ama bileşenler yeni değil.

Etiket: **KISMİ / DESTEKLİ-alt-iddialar-DAYANAKSIZ-birleşim** — "D2 için benchmark yok" kısmı DESTEKLİ (YOK-bulundu); "tool-offload > metin-sayma" ve "biçim↔verimlilik farkı" mekanizma-iddiaları olarak DAYANAKSIZ (zaten bilinen bulgu sınıfı, D2'ye özgü değil).

## A67-3 (İB-63/paralel-kapı) — Bernstein koşullarıyla LLM-siz/deterministik koşum-önü eşzamanlılık kapısı

Sorgular (birebir):
1. "Bernstein conditions parallel LLM agents write conflict detection"
2. "declarative manifest concurrency multi-agent orchestration file conflict prevention gate"
3. "agent-eval agentops deterministic pre-run gate concurrency LLM pipeline read-write set disjoint"
4. (ek) "CoAgent concurrency control multi-agent systems read-write set arxiv 2606.15376"

Bulunan en-yakın-komşular (arama-sonucu):
- **CoAgent: Concurrency Control for Multi-Agent Systems** (arXiv 2606.15376) — Bernstein-türü klasik eşzamanlılık kontrolünü LLM-ajanlarına DOĞRUDAN uyarlıyor; MTPO adlı protokol, ama read-set'leri "geniş ve statik-çıkarılamaz" kabul ediyor ve LLM'İ conflict-yargısına DAHİL ediyor (bizim iddiamız tam tersi: LLM'siz, BEYAN-EDİLMİŞ manifestten deterministik hüküm). Bu doğrudan komşu ve KISMEN çelişiyor: "klasik Bernstein koşulları LLM-ajanlara fit değil" diyorlar, biz ise "beyan-edilmiş manifestle fit edilebilir" diyoruz — konu aynı, çözüm farklı.
- **"Position: Multi-Agent Systems Should Prioritize Concurrency Control"** (arXiv 2608.18092) — pozisyon makalesi, alanın kendisinin olgunlaşmadığını iddia ediyor; bizim "kapı yok" iddiamızı DOLAYLI destekliyor.
- **ATM: CID-Brokered Pre-Write Admission for Multi-Agent Code Co-Synthesis** (arXiv 2607.00041) — "pre-write admission" ibaresi bizim "koşum-önü kapı" kavramına çok yakın; içerik detayı bu turda açılmadı [?].
- **LatticeMind** (arXiv 2608.08236) — conflict-aware memory, ama write-time LLM-reconciliation kullanıyor (LLM'siz değil).
- "one-writer-per-module" + git-worktree izolasyonu (Augment Code guide) — pratikte disjoint-write kuralı zaten kullanılıyor ama BEYAN-EDİLMİŞ manifest + Bernstein-formülasyonu ile deterministik hüküm mekanizması olarak literatürde adlandırılmamış.

Yenilik durumu: **KISMİ**. Konu (LLM-ajan eşzamanlılığı, Bernstein-türü koşullar) AKTİF bir araştırma alanı — CoAgent ve Position-paper aynı ayı/yılda (2606-2608, yani 2026) yayınlanmış, alan sıcak. Ancak bulunan çalışmaların hepsi ya LLM'İ conflict-çözümüne DAHİL ediyor (CoAgent, LatticeMind) ya da runtime/optimistic kontrol öneriyor; "koşum-ÖNCESİ, saf deterministik, LLM'siz, beyan-edilmiş-manifest-tabanlı" kapı biçimi bu taramada AYNI ISIM VE BİÇİMDE bulunamadı — ama ATM (pre-write admission) ismi çok yakın durduğu için ayrı bir tur şart.

Etiket: **DAYANAKSIZ** ("yenilik" iddiası CoAgent ile aynı problem uzayında rakip bir çözüm bulunduğu için savunmasız hale geldi; "LLM-siz deterministik" farkı iddia edilebilir ama ATM'nin içeriği görülmeden kesin hüküm verilemez).

## Özet tablo

| Aday | Durum | Etiket |
|---|---|---|
| A67-1 | KISMİ | DAYANAKSIZ (ek tur gerekli — SARIF/Sprotty/mdast doğrudan karşılaştırılamadı) |
| A67-2 | KISMİ (alt-iddia ayrımlı) | KISMİ — "D2 benchmark yok" DESTEKLİ, mekanizma-iddiaları DAYANAKSIZ |
| A67-3 | KISMİ | DAYANAKSIZ (CoAgent aynı problem uzayında rakip; ATM içeriği görülmedi) |

Not: Bu tur bütçe-sınırlı (9+2=11 WebSearch), açılmayan URL'ler "arama-sonucu" olarak işaretlendi, hiçbir URL/DOI uydurulmadı. `[?]` işaretli hücreler ek tur gerektirir.
