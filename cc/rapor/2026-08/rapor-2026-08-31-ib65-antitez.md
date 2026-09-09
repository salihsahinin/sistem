# İB-65 Atlas — ANTİTEZ Raporu (Aşama-2, CoVe-Factored)

**Künye:** antitez işçisi · model sonnet · AS-OF 2026-08-31 · araç çağrısı: 1 ToolSearch + 1 Bash + 8 web (6 WebSearch + 4 WebFetch, biri Bölüm3 Bash içinde birleşik) ≈ 10 çağrı (bütçe 16, aşılmadı).

Not: Tez raporları AÇILMADI/OKUNMADI; yalnız emirde verilen iddia metinleri kullanıldı (çıpalama freni korundu).

---

## BÖLÜM 1 — A ailesi

### A-z1 — Kubernetes level-triggered terminolojisi
**ÇÜRÜTÜLEMEDİ (SAĞLAM).** Terminoloji resmî Kubernetes kaynaklarında GEÇİYOR ve iddia edilen anlamda kullanılıyor.
- Kaynak: `kubernetes/community` — `contributors/devel/sig-architecture/api-conventions.md` (ve `kubernetes/kubernetes` `docs/design/principles.md`, release-1.2/1.3): "Kubernetes functionality must be **level-based**... Edge-triggered behavior must be just an optimization." "the system is **level-based rather than edge-triggered**, and should assume an Open World."
- URL: https://github.com/kubernetes/community/blob/main/contributors/devel/sig-architecture/api-conventions.md ; https://github.com/kubernetes/kubernetes/blob/release-1.2/docs/design/principles.md
- Değerlendirme: iddianın "watch olayları ipucu, otoriter bildirim değil" formülasyonu dokümanın "system not required to touch base at 5 before changing status to 3" ifadesiyle örtüşüyor. A-z1 çürütülemedi.

### A-z2 — Durable execution vs DAG-orkestrasyon formal ayrım
**DARALTILDI.** Nötr (vendor-dışı) akademik kaynak BULUNAMADI; bulunan kaynaklar vendor blog/dokümanları (Restate, Hatchet, Inngest, Diagrid, Astronomer) + iki arXiv makalesi (SerPyTor, Distributed Speculative Execution) — bunlar da vendor-yakın/uygulama odaklı, "formal" bir ayrım kanıtlamıyor.
- Bulunan çerçeve: DAG-tabanlı = "execution path build-time'da tanımlı, düğümler/kenarlar sabit"; durable execution = "ara durumu ayrı store'da persist edip checkpoint'ten devam etme" — bu bir MÜHENDİSLİK/UYGULAMA ayrımı, resmi/akademik "formal" (kuramsal ispat) bir ayrım değil.
- Ayrıca bir kaynak açıkça "workflow systems are some of the earliest adopters of durable execution... these are not mutually exclusive — durable execution can be implemented within DAG-based systems" diyor — yani A-z2'nin "FORMAL/kuramsal ayrım" iddiası ZAYIFLADI: pratikte bu iki kavram örtüşebiliyor/iç içe geçebiliyor, keskin formal ayrım kanıtı yok.
- Sonuç: iddia tam çürütülmedi ama "FORMAL" sıfatı DAYANAKSIZ kaldı → DARALTILDI (mühendislik-pratiği ayrımına indirgendi).

### A-z3 — Kaskad kontrol benzetmesi + "yakıt enjeksiyonu"
**KISMEN ÇÜRÜTÜLDÜ.**
- Kaskad kontrol tanımı (Control Engineering, ScienceDirect, LibreTexts, MATLAB/Simulink dersleri) doğrulandı: "İç ve dış loop'lar EŞZAMANLI/SÜREKLİ çalışır (concurrently), iç loop dış loop'un aktüatörü gibi davranır"; iç loop dış loop'tan ~3x hızlı olmalı. **Hiçbir kaynak iç loop'un TERMINATE ettiğini söylemiyor** — aksine "concurrently run" ve "continuous-time control systems" vurgusu var.
- Bu, ¬-tezin ilk yarısını DOĞRULAR: "kaskad kontrol İKİ SÜREKLİ döngüdür, iç döngü terminate etmez" — orijinal A-z3 iddiasındaki benzetme (iç pipeline'ın well-founded ranking function ile terminate etmesi = kaskad kontrol) YAPISAL OLARAK YANLIŞ eşleme: klasik kaskad kontrolde iç döngü sonlanmaz, sürekli çalışır; well-founded/terminating bir iç süreç kaskad kontrolün DEĞİL, başka bir desenin (örn. nested/hiyerarşik sonlu görev) örneğidir.
- "Yakıt enjeksiyonu formal kanıt tekniği değildir" kısmı için doğrudan bir kaynak aranmadı (bu bir iç terminoloji/metafor, literatürde "fuel"/"yakıt" terimi well-founded induction'da resmi bir teknik olarak GEÇMEZ — bilinen formal teknikler: well-founded recursion, structural induction, ranking function/variant function (Floyd-Hoare); "fuel" bazı fonksiyonel dillerde (Coq/Agda) sonlu-adım-sayacı olarak GERÇEKTEN kullanılır ama bu ayrı bir teknik, "kaskad kontrol formalizasyonu" değil).
- Sonuç: kaskad-kontrol benzetmesi ÇÜRÜTÜLDÜ (iç döngü terminate etmiyor iddiası kaynaklarla doğrulandı); "yakıt enjeksiyonu formal teknik değil" iddiası ARANAMADI/nötr kaynakla teyit edilemedi ama bilinen isim (fuel-based termination, Coq/Agda) farklı bir literatüre ait — kaskad kontrolle iddia edildiği gibi birleştirilmesi DAYANAKSIZ.

---

## BÖLÜM 2 — B ailesi

### B-z1 — Temporal 1000 child workflow sınırı
**ÇÜRÜTÜLEMEDİ, AMA EK BİLGİYLE GENİŞLETİLDİ.**
- `docs.temporal.io/child-workflows`: "a single Parent should not spawn more than **1,000** Child Workflow Executions." — B-z1 iddiası BİREBİR DOĞRU.
- `docs.temporal.io/workflow-execution/limits`: ayrıca "Temporal enforces a maximum number of incomplete Activities, Child Workflows, Signals, or Cancellation requests per Workflow Execution (by default, **2,000** for each type of operation)" — bu farklı bir eşik (eş-zamanlı TAMAMLANMAMIŞ child sayısı = 2000, config edilebilir `NumPendingChildExecutionsLimit`), toplam ömür-boyu 1000 önerisiyle ÇELİŞMİYOR, TAMAMLAYICI.
- Sonuç: B-z1 ÇÜRÜTÜLEMEDİ (SAĞLAM) — rakam resmî dokümanda birebir var.

### B-z2 — Airflow max_active_runs / max_active_tasks (güncel sürüm)
**ÇÜRÜTÜLEMEDİ (SAĞLAM).**
- Kaynak: `airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html` — sürüm **3.3.1**.
- `max_active_runs_per_dag`: "The maximum number of active DAG runs per DAG." (default 16) — DAG-başına eşzamanlı DagRun.
- `max_active_tasks_per_dag` / DAG-level `max_active_tasks`: "The maximum number of task instances allowed to run concurrently in each dag run." (default 16) — DAG içi eşzamanlı task.
- B-z2 iddiası (parametre adları/anlamları) BİREBİR doğrulandı, sürüm 3.3.1 olarak teyitli.

### B-z3 — Claude Code'da loop↔pipeline eşdeğeri yok
**ÇÜRÜTÜLDÜ.**
- Web taraması (pubnub, boringbot, hidekazu-konishi, inference.net rehberleri): Claude Code/Agent SDK'da adım-bağımlılığı modelleyen mekanizmalar VAR: subagent zincirleme ("chaining dependent steps"), hook lifecycle noktaları (PreToolUse, PostToolBatch, TaskCreated/TaskCompleted, SubagentStop vb. — deterministik kontrol noktaları), "Dynamic Workflows fan-out", "SDK workflows" büyüme yolu.
- Bu, ¬-tezin iddia ettiği gibi "DAG/adım-bağımlılığı" işlevine karşılık gelen gerçek mekanizmaların (hooks zinciri + subagent kompozisyonu + Dynamic Workflows) var olduğunu gösteriyor.
- Not: "DAG" terimi doğrudan kaynaklarda geçmiyor (arama sonucu bunu açıkça belirtti), ama işlevsel eşdeğer (sıralı/koşullu adım bağımlılığı, kontrol noktaları) mevcut → orijinal "eşdeğeri YOKTUR" iddiası ÇÜRÜTÜLDÜ.

---

## BÖLÜM 3 — C ailesi ayak-izi doğrulaması (Bash, web yok)

| # | Kontrol | Sonuç |
|---|---|---|
| 1 | `veri/manifest/*.json` sayısı | DOĞRULANDI — 17 |
| 2 | `"tur"` dağılımı | DOĞRULANDI — 16 pipeline (15+1, ikinci satır aynı dosyada ek alanlı tekrar) + 1 loop |
| 3 | 8 script/doküman dosyası (katman-hatti.py, hareket-tablo.py, silver-saglik.py, loop-dedektor.py, bag-tablo.py, erisim-fts.py, gnhf-izle.py, SCRIPTLER.md) | DOĞRULANDI — hepsi VAR |
| 4 | `cc/workflow/*.js` sayısı | YANLIŞ (gerçek değer: 14, iddia edilen 13 değil) |
| 5 | 4 manifest (ib-65-loop-pipeline-atlas, ib-66-gozlemlenebilir-nested-loop, loop-kapanis-bu-oturum, sahada-damitma-s22) | DOĞRULANDI — hepsi VAR |
| 6 | `"İTERASYON SONU"` satırı `tools/gnhf-izle.py` | DOĞRULANDI — satır 49 |
| 7 | AJAN_TAVAN/DALGA rakamları | DOĞRULANDI — `cc/workflow/fren-sablonu.js` ve `...idempotens-m40b-wf...js`: `AJAN_TAVAN: 36, DALGA_TAVAN: 12` birebir eşleşiyor (ib-39-atlas.json'da da "AJAN_TAVAN 36 / DALGA 12" metni var) |
| 8 | `veri/gorunum/v_loop_aday.csv` satır sayısı | DOĞRULANDI — 271 |

---

## ÖZET (m.40b hayatta-kalma metriği)

- **SAĞLAM (çürütülemedi):** A-z1, B-z1, B-z2 → 3
- **DARALTILDI (kısmen zayıfladı):** A-z2 → 1
- **ÇÜRÜTÜLDÜ (tam/kısmen):** A-z3 (kaskad-kontrol eşlemesi), B-z3 → 2
- **Bölüm 3 ayak-izi:** 7/8 DOĞRULANDI, 1/8 YANLIŞ (madde 4: `cc/workflow/*.js` = 14, iddia edilen 13 değil)
