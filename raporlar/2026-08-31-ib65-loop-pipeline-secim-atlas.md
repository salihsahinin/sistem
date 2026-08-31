# İB-65 — Loop ↔ Pipeline ↔ Hibrit seçim ölçütleri + iç-içe (nested) loop kompozisyonu atlası

## KÜNYE

| alan | değer |
|---|---|
| Emir | `cc/gorev-2026-08-30-ib65-loop-pipeline-secim-atlas.md` |
| HEAD (koşum anı) | `f08209b` |
| AS-OF | 2026-08-31 |
| Koşum biçimi | m.40b tam kontrat: tez ×3 (A/B/C) → CoVe-Factored antitez → V26 kural-tabanlı örneklem → maskeli hakem → sentez |
| Lider ajan | bu koşum (Opus sınıfı) |
| İşçi ajan sayısı | 9 (A×2, B×2, C×2 — ilk üçü arka planda koştu ve tekrar edildi; antitez ×1, hakem ×1) · tavan 12 · AŞILMADI |
| İşçi model sınıfı | A/B/C + antitez = Sonnet-5 · hakem = Opus-5 |
| Ham raporlar | `cc/rapor-2026-08-31-ib65-A.md` · `-B.md` · `-C.md` · `-antitez.md` · `-hakem.md` |
| Yasak beyanı | kod/kanon değişikliği YAPILMADI · `git add/commit/push` YAPILMADI · koşum-biçimi HÜKMÜ verilmedi (öneri üretildi, karar masada, m.31) |

**Koşum daraltmaları (BEYAN, m.39):** (i) A/B/C ilk turu arka planda koştu, dosya yazımı görülmeyince senkron tekrar edildi → aynı üç dosyaya iki koşum yazdı, diskteki nihai içerik son yazan koşumundur; iddia numaraları bu sentezde diskteki nihai metne göredir. (ii) V26 örneklemi ayrı işçiye verilmedi, lider ajan 3 doğrudan `WebFetch` sondajıyla yaptı (ajan tavanı freni). (iii) C ailesi `cc/workflow/*.js` iç içeriklerini açmadı; `veri/gorunum/v_loop_aday.csv`'nin 271 satırından 1 temsilci alındı.

---

## 1. A+B BİRİNCİL KAYNAK TABLOSU (hakem etiketli)

10 kaynak, hepsi URL + AS-OF damgalı; etiket maskeli hakemin hükmüdür (`cc/rapor-2026-08-31-ib65-hakem.md`).

| # | Kaynak (URL) | Tür | AS-OF | Taşıdığı iddia | Etiket |
|---|---|---|---|---|---|
| K1 | https://kubernetes.io/docs/concepts/architecture/controller/ | resmî-dok | 2026-08-31 | Controller = "non-terminating control loop", current→desired state | **D** |
| K2 | https://beam.apache.org/documentation/basics/ | resmî-dok/spec | 2026-08-31 | PCollection bounded ∨ unbounded; watermark = tamamlanma tahmini; trigger = yayın anı | **D** |
| K3 | https://beam.apache.org/documentation/programming-guide/ | resmî-dok | 2026-08-31 | Window/Watermark/Trigger birleşik model; "batch = unbounded'ın tamamlanmış hâli" | **K** (son formülasyon yorum) |
| K4 | https://www.cs.cornell.edu/fbs/publications/DefLiveness.pdf (Alpern & Schneider 1985) | akademik (birincil) | 2026-08-31 | safety = limit-kapalı, liveness = yoğun; her property = safety ∧ liveness kesişimi | **D** |
| K5 | https://fstar-lang.org/tutorial/book/part2/part2_well_founded.html | resmî-dok | 2026-08-31 | well-founded = sonsuz azalan dizi yok; azalan *measure* → terminasyon | **K** (sayfa "measure" der, "ranking function" formal tanımı yok — V26 sondajı) |
| K6 | https://docs.temporal.io/workflow-execution/limits | resmî-dok | 2026-08-31 | Event History tavanı 51.200 event / 50 MB (uyarı 10.240 / 10 MB) | **D** |
| K7 | https://docs.temporal.io/design-patterns/continue-as-new | resmî-dok | 2026-08-31 | Continue-As-New: state taşıyıp history sıfırlama = sınırsız koşumun bütçe freni | **D** |
| K8 | https://docs.temporal.io/child-workflows | resmî-dok | 2026-08-31 | Child Workflow ayrı Event History; parent başına ≤1000 child | **D** (¬ denemesi başarısız) |
| K9 | https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/deferring.html | resmî-dok (Airflow 3.3.1) | 2026-08-31 | Deferrable operator worker slotunu triggerer'a bırakır; sensor `mode='reschedule'` ∨ `deferrable=True` | **D** |
| K10 | https://code.claude.com/docs/en/scheduled-tasks | resmî-dok | 2026-08-31 | `/loop` sabit-interval ∨ self-paced; `ScheduleWakeup(stop:true)`; ~20 dk fallback; ≤50 task/oturum; min 1 dk; 7 gün expiry; `loop.md` 25.000 byte kesim | **D** (V26'da alıntı düzeyinde birebir teyit) |

Ek resmî kaynaklar (tabloda sayılmayan, ikincil rol): https://docs.temporal.io/encyclopedia/retry-policies (**D**) · https://docs.prefect.io/v3/how-to-guides/workflows/write-and-run (**D**) · https://docs.dagster.io/guides/automate/declarative-automation (**X** — aşağıya bak) · https://airflow.apache.org/docs/apache-airflow/2.4.0/concepts/dynamic-task-mapping.html (**K**, sürüm bayat).

**Hakem dağılımı (23 iddia):** D 12 · K 8 · X 3. m.40b hayatta-kalma: SAĞLAM 12 · DARALDI 8 · DÜŞTÜ 3.

### 1.1 DÜŞEN (X) üç iddia — tasarım gerekçesi olarak KULLANILAMAZ

1. **Kaskad-kontrol benzetmesi (X).** "Dış reconciliation loop + iç terminate eden pipeline = kaskad kontrol" YANLIŞ: kaskad kontrolde iç döngü de SÜREKLİDİR, terminate etmez. "Bütçe yakıtı enjeksiyonu" formal bir kanıt tekniği değildir. → S1 taslağı bu benzetmeye DAYANMAZ; bütçe kalıtımı tek-sayaç kuralıyla (aşağıda 3.2) kurulur.
2. **Dagster `use_sensors: true` zorunluluğu (X).** V26 sondajı: sayfada böyle bir ayar YOK; gereken, varsayılan automation condition sensor'ün UI'dan etkinleştirilmesidir. → V26 İHLAL kaydı.
3. **"Claude Code'da pipeline/DAG eşdeğeri yok" (X).** Çürütüldü: hooks zinciri, subagent zincirleme ve Dynamic Workflows adım-bağımlılığı sağlıyor; ayrıca `/goal` (koşul-tabanlı), `Channels` (olay-itmeli), Routines (cloud, min 1 sa), Desktop scheduled task (min 1 dk) ayrı yüzeyler olarak resmî dokümanda listeli.

### 1.2 V26 kural-tabanlı örneklem (son-üçlükten 1/3, birincil-kaynak sondajı)

Örneklem: A ailesinin son üçlüğünden 1 (K5) + B ailesinin son üçlüğünden 2 (Dagster otomasyon koşulları, Claude Code tavanları). Sondaj lider ajanın 3 doğrudan `WebFetch` çağrısıyla yapıldı.

| örneklem | sonuç |
|---|---|
| K5 (well-founded / ranking function) | KISMİ — well-founded tanımı birebir var; "ranking function" adlandırması kaynakta yok ("measure") → **İHLAL-HAFİF (terminoloji)** |
| Dagster on_cron/eager/on_missing + default sensor | Koşullar ve sensör DOĞRULANDI; `use_sensors: true` KAYNAKTA YOK → **İHLAL (uydurulmuş ayar adı)** |
| Claude Code 50 task / 1 dk / 7 gün / 25.000 byte / `ScheduleWakeup(stop:true)` / ~20 dk fallback | HEPSİ birebir doğrulandı → **İHLAL YOK** |

**Toplam ihlal: 1 tam + 1 hafif / 3 örneklem.**

### 1.3 Kuramdan çıkan altı ayırt edici eksen (SAĞLAM çekirdek)

| Eksen | LOOP kutbu | PIPELINE kutbu | Dayanak |
|---|---|---|---|
| E1 Terminasyon | sonlanmaz; drift oldukça yeniden tetiklenir | sonlanır; "done" durumu vardır | K1 (D) |
| E2 Formal özellik sınıfı | SAFETY ağırlıklı — korunan değişmez | LIVENESS ağırlıklı — ulaşılan hedef | K4 (D) |
| E3 Tetikleme | level-triggered: her turda durumu sıfırdan okur, kaçırılan olaya dayanıklı | adım-akışı: bir adımın çıktısı sonrakinin girdisi, adım bir kez koşar | A2 (**K** — terminoloji resmî K8s dokümanında geçmiyor ama community kaynağında doğrulandı) |
| E4 Veri sınırlılığı | unbounded (akış sürer, tamamlanma tahmindir) | bounded (girdi kümesi sabit, "tümü işlendi" kesin) | K2 (D) |
| E5 Terminasyon kanıtı | aranmaz; yerine kararlılık/yakınsama | azalan measure ile terminasyon kanıtlanır | K5 (K) |
| E6 Bütçe kompozisyonu | düz sayaç yetmez — history/iterasyon şişer, açık fren gerekir (Continue-As-New emsali) | adım sayısı yapısal olarak sınırlı | K6, K7 (D) |

---

## 2. C — İÇ ENVANTER SINIFLANDIRMASI (24 birim, pointer'lı)

Kaynak: `cc/rapor-2026-08-31-ib65-C.md`. Ayak-izi doğrulaması `cc/rapor-2026-08-31-ib65-antitez.md` Bölüm 3'te yapıldı: **8 maddenin 7'si DOĞRULANDI**; tek düzeltme → `cc/workflow/*.js` gerçekte **14** dosyadır (C'nin "13" beyanı YANLIŞ, aşağıda düzeltildi).

| # | birim | pointer | sınıf | done-yüklemi | insan-kapısı | idempotent |
|---|---|---|---|---|---|---|
| 1 | ib-04-wiki-ajan-metodolojisi | `veri/manifest/ib-04-wiki-ajan-metodolojisi.json` | PIPELINE | BİR-KEZ | H | E |
| 2 | ib-07-description-eval | `veri/manifest/ib-07-description-eval.json` | PIPELINE | BİR-KEZ | H | BİLİNMİYOR |
| 3 | ib-09-yolc-v26-etki | `veri/manifest/ib-09-yolc-v26-etki.json` | PIPELINE | BİR-KEZ | H | BİLİNMİYOR |
| 4 | ib-30-parquet-varsayilani | `veri/manifest/ib-30-parquet-varsayilani.json` | PIPELINE | BİR-KEZ | H | E |
| 5 | ib-39-atlas | `veri/manifest/ib-39-atlas.json` | PIPELINE | BİR-KEZ | H | BİLİNMİYOR |
| 6 | ib-55-a3-revizyon | `veri/manifest/ib-55-a3-revizyon.json` | PIPELINE | BİR-KEZ | H | E |
| 7 | ib-58-anahtar-denetim-argparse | `veri/manifest/ib-58-anahtar-denetim-argparse.json` | PIPELINE | BİR-KEZ | H | E |
| 8 | ib-58-erisim-fts-axi | `veri/manifest/ib-58-erisim-fts-axi.json` | PIPELINE | BİR-KEZ | H | E |
| 9 | ib-65-loop-pipeline-atlas | `veri/manifest/ib-65-loop-pipeline-atlas.json` | PIPELINE | BİR-KEZ | H | BİLİNMİYOR |
| 10 | ib-66-gozlemlenebilir-nested-loop | `veri/manifest/ib-66-gozlemlenebilir-nested-loop.json` | PIPELINE | BİR-KEZ | H | BİLİNMİYOR |
| 11 | ib-67-68-paper-urun-envanteri | `veri/manifest/ib-67-68-paper-urun-envanteri.json` | PIPELINE | BİR-KEZ | H | BİLİNMİYOR |
| 12 | ib-69-a1 | `veri/manifest/ib-69-a1.json` | PIPELINE | BİR-KEZ | H | BİLİNMİYOR |
| 13 | ib-69-a2 (`sira:["ib-69-a1"]`) | `veri/manifest/ib-69-a2.json` | PIPELINE | BİR-KEZ | H | BİLİNMİYOR |
| 14 | ib-a2-tatbikat | `veri/manifest/ib-a2-tatbikat.json` | PIPELINE | BİR-KEZ | H | E |
| 15 | masa83-hukum-icrasi | `veri/manifest/masa83-hukum-icrasi.json` | PIPELINE | BİR-KEZ | H | E |
| 16 | loop-kapanis-bu-oturum | `veri/manifest/loop-kapanis-bu-oturum.json` (manifest `tur:"loop"`) | **HİBRİT** | SÜREKLİ | H | E |
| 17 | sahada-damitma-s22 | `veri/manifest/sahada-damitma-s22.json` (manifest `tur:"pipeline"`) | **HİBRİT** | SÜREKLİ | H | BİLİNMİYOR |
| 18 | `tools/katman-hatti.py` (sabit 7-adımlı sıra) | `tools/SCRIPTLER.md` ~satır 110 | HİBRİT | SÜREKLİ | H (seans-kapanış tetiği) | E (`git_head_sha=HEAD` → no-op) |
| 19 | `tools/hareket-tablo.py` | `tools/SCRIPTLER.md` ~satır 134 | LOOP | SÜREKLİ | H | E (append-only, tekil id) |
| 20 | `tools/silver-saglik.py` | `tools/SCRIPTLER.md` ~satır 121 | LOOP | SÜREKLİ (invariant: "error 0") | H (`--kapi`) | BİLİNMİYOR |
| 21 | `tools/loop-dedektor.py` (90 gün kayan pencere) | `tools/SCRIPTLER.md` ~satır 109 | HİBRİT | SÜREKLİ | H (`--kutu`) | BİLİNMİYOR |
| 22 | `tools/bag-tablo.py` (bitemporal ACILDI/KAPANDI) | `tools/SCRIPTLER.md` ~satır 114 | HİBRİT | SÜREKLİ | H | E (append-only) |
| 23 | `tools/erisim-fts.py --insa` | `tools/SCRIPTLER.md` ~satır 125 | HİBRİT | SÜREKLİ | H | BİLİNMİYOR |
| 24 | `cc/workflow/*.js` — **14 dosya** (m.40b atlas workflow'ları) | `cc/workflow/` + `veri/manifest/ib-39-atlas.json` (AJAN_TAVAN 36 / DALGA 12) | HİBRİT | BİR-KEZ (workflow başına) | H | BİLİNMİYOR |

**Dağılım:** PIPELINE 15 · LOOP 2 · HİBRİT 7 · toplam 24 (eşik ≥20 SAĞLANDI).

**Manifest `tur` alanı mevcut durumu:** 17 manifest, `tur` alanı 17/17 DOLU, boş 0. Değerler: `"pipeline"` ×16, `"loop"` ×1. `"hibrit"` değeri HİÇ kullanılmıyor. Beyan ↔ türetim ayrışması 2 birimde: #16 (manifest `loop`, türetim HİBRİT) ve #17 (manifest `pipeline`, türetim HİBRİT). **Envanterin %29'u (7/24) mevcut iki-değerli şemaya sığmıyor** — S3'ün gerekçesi budur.

**İç-içe loop canlı vakası — gnhf nöbeti** (`tools/gnhf-izle.py`; antitez `grep -n "İTERASYON SONU"` ile satırın varlığını DOĞRULADI):
- **Dış döngü:** `en_yeni_worktree()` — `~/jarvis-gnhf-worktrees/*` altındaki en yeni worktree izlenir; iterasyon sayısı ÖNCEDEN BİLİNMEZ.
- **İç döngü/hat:** her `iteration-N.jsonl` — `assistant → tool_use → tool_result → result` turn-based sabit akışı.
- **Bütçe birimi:** iterasyon kapanışında `"■ İTERASYON SONU · <subtype> · maliyet $<total_cost_usd> · <num_turns> tur"`. Script kümülatif toplam TUTMUYOR — yalnız anlık basıyor. Dış bütçe elde toplanıyor (`kuyruk/k010-zincir-2026-08-29.md:55`).
- **Ders (emirde gömülü iki arıza):** commit-dili ve bütçe-birimi arızaları tam da bu eksikten doğuyor — **dış döngünün kendi sayacı yok**. S1 kuralı 3.2'nin doğrudan gerekçesi.

---

## 3. S1 — NESTED-LOOP KURAL TASLAĞI (m.38 lojik formu)

Semboller: `L` = dış döngü · `P` = iç hat · `done(P)` = iç bitiş yüklemi · `inv(L)` = dış değişmez · `N` = dış tur tavanı · `M` = iç adım tavanı · `B` = tek bütçe sayacı · `t` = tur indeksi.
Not: bu taslak, hakemin **X** verdiği kaskad-kontrol benzetmesine DAYANMAZ (bkz. §1.1/1).

**1. Kuruluş geçerliliği**
- 1.1 `nested(L,P) GEÇERLİ ↔ (1.2 ∧ 1.3 ∧ 1.4 ∧ 1.5)`
- 1.2 `done(P)` BOOLEAN ∧ sonlu adımda hesaplanabilir ∧ dış tur akışını BLOKLAMAZ
- 1.3 `inv(L)` her turun BAŞINDA ∧ SONUNDA ölçülür (level-triggered: durum sıfırdan okunur, olaya güvenilmez) — E3
- 1.4 `done(P) → ¬ihlal(inv(L))` — iç bitiş dış değişmezi bozmaz (kompozisyon şartı)
- 1.5 `∃ ölçü m: (∀ iç adım) m kesin azalır ∧ m well-founded` → `P` terminate eder — E5/K5
- 1.6 `¬1.5 → P bir LOOP'tur, P'yi iç hat olarak kullanma` (iç katman terminate etmiyorsa nested değil, iki-loop'tur → masa kararı)

**2. Sınıf ayrımı (dış ↔ iç)**
- 2.1 `sinif(X) = LOOP ↔ (done-yüklemi(X) SÜREKLİ ∧ ¬bilinir(tekrar-sayisi(X)))`
- 2.2 `sinif(X) = PIPELINE ↔ (done-yüklemi(X) BİR-KEZ ∧ sabit(ic-sira(X)))`
- 2.3 `sinif(X) = HİBRİT ↔ (done-yüklemi(X) SÜREKLİ ∧ sabit(ic-sira(X)))`
- 2.4 `¬(sinif(X) = LOOP ∧ sinif(X) = PIPELINE)` — sınıflar ayrık

**3. Bütçe KALITIMI (dış N × iç M çarpım freni)**
- 3.1 `toplam-is ≤ N × M` — tavan çarpımdır, toplam değil
- 3.2 `B TEK sayaçtır ∧ (∀ t) B_kalan := B_kalan − maliyet(t)` ∧ `¬(iç ve dış AYRI sayaç tutar)` ← gnhf arızasının doğrudan karşılığı
- 3.3 `dur(L) ← (B_kalan ≤ 0) ∨ (t ≥ N) ∨ (inv(L) sağlandı ∧ kararlı) ∨ Salih-durdurma`
- 3.4 `¬(3.3'ün hiçbir dalı) → devam(L)`
- 3.5 `M SABİTTİR` ∧ `derinlik(nested) ≤ 2`; `derinlik ≥ 3 → masa kararı ZORUNLU` (çarpım patlaması freni)
- 3.6 `B_kalan < maliyet_tahmin(t+1) → yeni tur BAŞLAMAZ` (yarım tur yasağı — Continue-As-New emsali K7: state taşınır, koşum kapatılır)

**4. İterasyon ayak-izi (İB-63 PK-10)**
- 4.1 `(∀ t) ayak-izi(t) DİSKE yazılır` — içerik: `{tur, HEAD_sha, maliyet, süre, done(P), inv(L), yazılan-yollar}`
- 4.2 `kapandi(t) ↔ yazildi(ayak-izi(t))` ∧ `¬yazildi(ayak-izi(t)) → ¬baslar(t+1)`
- 4.3 `ayak-izi(A) ∩ ayak-izi(B) ≠ ∅ → ¬paralel(A,B)` (paralel-kapı kuralı)

**5. Gözlem seviyesi**
- 5.1 `kutuk(dış tur) = TAM` (∀ t) — dış tur her zaman tam kaydedilir
- 5.2 `kutuk(iç adım) = TAM ↔ (hata ∨ t = 1 ∨ örneklemde)` ; aksi halde `= ÖZET` (token freni)
- 5.3 `gozlem-seviyesi ≠ karar-seviyesi` — kütük yazmak karar vermek değildir

**6. Yönetim partisyonu (Salih zemini — icra/karar/öğrenme)**
- 6.1 `karar-gerektirir(s) → s ∉ L ∧ s ∉ P ∧ s → karar-masası`
- 6.2 `ogrenme-uretir(s) → s → Salih oturumu` (otomasyona GÖMÜLMEZ)
- 6.3 `icra(s) → s ∈ İB-ledger ∧ gömülebilir(s, L ∨ P)`
- 6.4 `kurulabilir(L) ↔ (∀ s ∈ L) icra(s) ∧ ¬karar-gerektirir(s) ∧ ¬ogrenme-uretir(s)`
- 6.5 m.16 bağı: `m.38-uygulandi(bu taslak) → m.16-tarama(bu taslak)` — masaya çelişki kapısından geçerek gider

---

## 4. S2 — SEÇİM ÖLÇÜTLERİ: ÜÇ KARAR MODELİ (m.37)

Ortak sayım tabanı: 24 sınıflanmış birim + 17 manifest (§2). Sayısal değerler **deneysel `[?]` tahmindir** (m.29/m.39); token rakamları sınıflandırmayı yapan ALT-MODEL koşumu içindir.

### Model 1 — Yüklem-ağacı (boolean karar tablosu) · ÖNERİLEN ✅

Matematiksel temel: önerme lojiği / karar tablosu. Üç boolean yüklem → tek sınıf, dallar ayrık ve tüketici.

- `Y1 = (done-yüklemi SÜREKLİ)` · `Y2 = bilinir(tekrar-sayısı)` · `Y3 = sabit(iç-sıra)`
- `¬Y1 ∧ Y3 → PIPELINE` · `Y1 ∧ ¬Y2 ∧ ¬Y3 → LOOP` · `Y1 ∧ Y3 → HİBRİT` · kalan kombinasyonlar → **BELİRSİZ → masaya**

| eksen | değer |
|---|---|
| token | ~0 / birim — 3 yüklem manifestten okunur, script'le kararlaştırılabilir; LLM koşumu gerekmez `[?]` |
| zaman | < 1 sn / birim (deterministik) `[?]` |
| kalite | 24 birimin 24'ünü sınıfladı; 2 ayrışma yakalandı (#16, #17) — geriye-dönük uyum %92 (22/24 manifest beyanıyla uyumlu) `[?]` |
| risk | DÜŞÜK — deterministik, denetlenebilir, revert ucuz; kalan risk: 3 yüklemin manifestte YANLIŞ doldurulması (girdi hatası, sınıflandırıcı hatası değil) |

### Model 2 — Ağırlıklı skor + eşik (lineer fayda / MCDA)

Matematiksel temel: ağırlıklı toplamsal fayda. 6 eksen (E1-E6) her biri 0-1 puanlanır, ağırlıklı toplam iki eşikle üç sınıfa bölünür (`s < 0,35 → PIPELINE`, `0,35 ≤ s ≤ 0,65 → HİBRİT`, `s > 0,65 → LOOP`).

| eksen | değer |
|---|---|
| token | ~3-6k / birim — 6 eksenin puanlanması yargı gerektirir, LLM koşumu şart; 24 birim ≈ 100-150k `[?]` |
| zaman | ~20-40 sn / birim `[?]` |
| kalite | Sınır vakalarında Model 1'den zengin (derece bilgisi taşır) ama ağırlıklar KALİBRE DEĞİL; kalibrasyon için etiketli örneklem gerekir (bugün yok) |
| risk | ORTA-YÜKSEK — ağırlıklar keyfî, LLM puanlaması non-deterministik (deterministik-tasarım ilkesiyle ÇELİŞİR, CLAUDE.md §6); m.42(f) evaluator düşük-temperature şartı zorunlu olur |

### Model 3 — KARŞIT-TEMELLİ: Birleşik model — "sınıflandırma YAPMA"

Matematiksel temel: Beam'in birleşik-model tezi (K3) — batch, unbounded akışın tamamlanmış özel hâlidir. Karşıt önerme: **seçim problemi sahtedir**; her iş birimi TEK biçimde (reconciliation loop) modellenir, "pipeline" = tavanı `N=1` olan loop'un özel hâli.

- `(∀ birim X) model(X) = LOOP(N_X, M_X)` ; `PIPELINE(X) ≡ LOOP(N_X = 1, M_X)` ; `HİBRİT(X) ≡ LOOP(N_X > 1, M_X > 1)`
- `tur` alanı SİLİNİR, yerine iki SAYI gelir: `N` (dış tavan) ve `M` (iç tavan).

| eksen | değer |
|---|---|
| token | ~0 / birim sınıflandırma için (sınıflandırma yok) — ama her birim için `N`,`M` belirlenmesi gerekir `[?]` |
| zaman | ~0 sınıflandırma; ama 17 manifestin ŞEMASI değişir → geriye-dönük göç maliyeti `[?]` |
| kalite | Kavramsal olarak en temiz — §2'deki 2 ayrışma ve %29 sığmama SORUNU tamamen ortadan kalkar; E1/E4 eksenleri N ile ifade edilir |
| risk | YÜKSEK — geriye-dönük şema göçü (17 manifest + `tools/katman-hatti.py` hattı + `loop-dedektor.py`) çekirdek-şema kilitler → m.40(c)'ye göre YÜKSEK geriye-dönük-maliyet sınıfı; ayrıca `N=1` loop'unun "level-triggered her turda durumu sıfırdan oku" semantiği bir-kez-koşan işlerde ANLAMSIZ (E3 kaybolur) |

### Karşılaştırma ve öneri

| | token/birim `[?]` | zaman/birim `[?]` | kalite (24 birimde) | risk |
|---|---|---|---|---|
| M1 yüklem-ağacı ✅ | ~0 | <1 sn | 24/24 sınıfladı, 2 ayrışma yakaladı | DÜŞÜK |
| M2 ağırlıklı skor | 3-6k | 20-40 sn | derece taşır, kalibre değil | ORTA-YÜKSEK |
| M3 birleşik (karşıt) | ~0 | ~0 + göç | kavramsal olarak en temiz | YÜKSEK (şema göçü) |

**Öneri: Model 1.** Gerekçe — (i) deterministik-tasarım ilkesine (CLAUDE.md §6) tek uyan model; aynı girdi → aynı sınıf, LLM koşumu gerekmez. (ii) Mevcut manifest şemasına EK bir değer (`hibrit`) dışında dokunmaz → düşük geriye-dönük maliyet (m.40c DÜŞÜK sınıf, ucuz revert). (iii) BELİRSİZ dalı m.16/m.31 ile uyumlu bir kaçış kapısı bırakıyor — sınıflandıramadığını masaya gönderiyor, zorla etiketlemiyor. (iv) M3 kavramsal olarak üstündür ancak bugün YÜKSEK geriye-dönük-maliyet sınıfındadır; **M3 arşive alınmaz, İB-66'nın (gözlemlenebilir nested loop) girdisi olarak kuyrukta tutulur** — `N`/`M` çifti M1'in `tur` alanının YANINA opsiyonel alan olarak eklenebilir (§5.2).

---

## 5. S3 — MANİFEST `tur` ALANI: SEÇİM ŞEMASI + KARAR-MASASI KALEMİ TASLAĞI

### 5.1 Seçim şeması (Model 1 karar tablosu — manifest doldurma kuralı)

Manifest yazan her ajan/oturum üç yüklemi cevaplar; `tur` bunlardan TÜRETİLİR, elle seçilmez.

| Y1 SÜREKLİ? | Y2 tekrar-sayısı bilinir? | Y3 iç-sıra sabit? | → `tur` | envanterden örnek |
|---|---|---|---|---|
| H | — | E | `pipeline` | `ib-04-…`, `ib-69-a2` |
| E | H | H | `loop` | `tools/hareket-tablo.py`, `tools/silver-saglik.py` |
| E | — | E | `hibrit` **(YENİ DEĞER)** | `loop-kapanis-bu-oturum`, `tools/katman-hatti.py`, gnhf nöbeti |
| H | — | H | `belirsiz` → MASAYA | — |
| E | E | H | `belirsiz` → MASAYA | — |

Ek zorunlu alanlar (nested olan birimler için, S1 §3'ten):
- `tur = "hibrit" → dis_tavan (N) ZORUNLU ∧ ic_tavan (M) ZORUNLU ∧ butce_sayaci = "tek"`
- `tur ∈ {"loop","hibrit"} → durma_kosulu ≠ null` (bugün `sahada-damitma-s22`'de `idempotency_anahtari = null` — açık borç)
- `tur ∈ {"loop","hibrit"} → ayak_izi_yolu ZORUNLU` (S1 §4.1)

### 5.2 Karar-masası kalemi TASLAĞI (hüküm masada — m.31, bu atlas HÜKÜM VERMEZ)

> **Kalem adı:** Manifest `tur` alanı üç-değerli mi olsun, seçim kuralı deterministik yüklem-ağacı mı olsun?
>
> **Bağlam:** 24 sınıflanmış birimin 7'si (%29) mevcut iki-değerli (`pipeline`|`loop`) şemaya sığmıyor; 17 manifestin 2'sinde beyan ↔ türetim ayrışması var (`loop-kapanis-bu-oturum`, `sahada-damitma-s22`). Kaynak: bu atlas §2.
>
> **Öneri (Model 1):** (a) `tur` değer kümesi `{pipeline, loop, hibrit, belirsiz}` olsun; (b) değer üç boolean yüklemden (SÜREKLİ? / tekrar-sayısı-bilinir? / iç-sıra-sabit?) TÜRETİLSİN, elle seçilmesin; (c) `belirsiz` masaya düşsün; (d) `hibrit` birimlerde `dis_tavan`, `ic_tavan`, `butce_sayaci="tek"`, `ayak_izi_yolu` alanları zorunlu olsun.
>
> **Artı:** deterministik (aynı girdi → aynı sınıf), token maliyeti ~0, mevcut 15 pipeline manifestine dokunmaz, %29'luk boşluğu kapatır, gnhf bütçe-birimi arızasının yapısal karşılığını (tek sayaç) şemaya yazar.
> **Eksi:** 2 mevcut manifestin `tur` değeri düzeltilecek (`loop-kapanis-bu-oturum`: loop→hibrit; `sahada-damitma-s22`: pipeline→hibrit) — küçük göç; ayrıca `belirsiz` dalı masaya iş üretir.
> **Karşıt seçenek (Model 3):** `tur` alanı büsbütün kaldırılıp `(N, M)` sayı çiftiyle değiştirilir — kavramsal olarak daha temiz, ancak çekirdek şema göçü = YÜKSEK geriye-dönük-maliyet sınıfı (m.40c) → bugün ÖNERİLMİYOR, İB-66 girdisi olarak kuyrukta.
> **Bağlı borçlar:** `sahada-damitma-s22` `idempotency_anahtari = null` · `tools/gnhf-izle.py` kümülatif bütçe sayacı yok · `cc/workflow/*.js` (14 dosya) iç fren sabitleri (AJAN_TAVAN 36 / DALGA 12) manifest dışında.
> **m.16 kapısı:** bu kalem masaya çelişki-kapısından geçerek girer (S1 §6.5).

### 5.3 Yönetim partisyonunun şemaya yansıması

`icra → İB-ledger` · `karar → masa` · `öğrenme → Salih`. Şemadaki karşılığı: bir manifest `tur ∈ {loop, hibrit}` alabilmek için **§S1 6.4** sağlanmalıdır — loop'a gömülü hiçbir adım karar-gerektirmez ∧ öğrenme-üretmez. `belirsiz` dalı ve `derinlik ≥ 3` koşulu bu partisyonun otomatik kaçış kapılarıdır: sistem sınıflandıramadığında ya da fazla derinleştiğinde İCRA'yı durdurup MASA'ya döner.

---

## 6. DURMA KOŞULU DENETİMİ

| madde | durum |
|---|---|
| sentez yazıldı | ✅ bu dosya |
| A+B'de ≥8 birincil kaynak, URL + AS-OF damgalı, D/K/X etiketli | ✅ 10 kaynak (§1) — D 7, K 3 |
| C'de ≥20 birim sınıflandırıldı, pointer'lı | ✅ 24 birim (§2); ayak-izi 7/8 doğrulandı, 1 düzeltildi |
| seçim-kuralı 3 model, ≥1 karşıt-temelli, token×zaman×kalite×risk sayısal, önerilen işaretli | ✅ §4 (Model 3 karşıt-temelli; Model 1 önerildi) |
| nested-loop kural taslağı m.38 lojik formda | ✅ §3 (6 numaralı dal, ∧ ∨ ¬ → ↔) |
| karar-masası kalemi taslağı hazır | ✅ §5.2 |
| manifest `tur` seçim şeması | ✅ §5.1 |

**Sağlanmayan / eksik:** V26 örneklemi ayrı işçiye verilmedi (lider ajan yaptı, §KÜNYE-ii). Maskeleme sızıntısı AÇIK BEYAN edilmiştir (K2-k şerhi): ürün adları hakem materyalinde kaynak-kimliğini fiilen ele veriyor; hakem yargısı kaynak-güvenilirliği ekseninde bundan etkilenmiş olabilir.
