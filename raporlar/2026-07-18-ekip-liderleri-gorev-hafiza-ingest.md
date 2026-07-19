# Ekip Liderleri: Görev-Dağılımı + Kategorizasyon + Lider-Başına Kişisel Hafıza & Ingest — Rapor (TARTIŞMA)

> **Mod:** rapor · KARAR YOK · commit onaylı (Salih 07-18); nihai karar = Fable (m.41). Kaynak: Salih 07-18 — "ilerde ekip liderleri oluşturup kişiselleştireceğiz; ekip liderleri nasıl bir görev-dağılımına sahip olmalı ve kategorizasyon nasıl yapılmalı; ekip liderleri için kişiselleştirilmiş hafıza modeli ve ingest mekanizmaları kullanacağız demiştik, bunu nasıl yapabileceğimizi araştır; çift yönlü atlas çalıştır; rapor oluştur." Çift-atlas: TEZ (aebd607d — ekip-lideri tasarımı, KOŞUYOR) + ANTİTEZ (a095e822 — flat/paylaşılan-hafıza, KOŞUYOR). **Rapor 14 (ingest-aile) doğrudan devamı: kişisel-ingest = ailenin ajan/rol-başına örneği.**

---

## 0. BLUF
Ekip-liderleri = Carvis (CEO) ile işçi-ajanlar arasında **orchestrator/supervisor katmanı**; görev-dağılımı = hiyerarşik ayrıştır→delege→topla (span: lider→işçi **3-5**, Carvis→lider **≤5-7** — klasik-yönetim ∧ Anthropic yakınsaması). Kişisel-hafıza + kişisel-ingest = **rapor 14 sentezinin ajan-başına uygulaması**: tek paylaşılan hafıza/ingest-BİÇİMİ + lider-rolüne göre **held-out-hak-edilmiş parametrizasyon** (N izole sistem değil; kombinatoryal N+M+R, N×M×R değil).
**★ Antitezin ayrımı (crux — raporun en değerli çıkarımı): geçici-ayrıştırma (görev-anında subagent) ≠ kalıcı-kişiselleştirilmiş-lider.** İlki bugün kanıtlı + düşük-taahhüt (bu oturumun atlas-fan-out'u = prototip); ikincisi (kategorize + izole-hafıza + özel-ingest) **held-out-kanıt bekler** → *"ŞİMDİ değil — ÖLÇ — kanıt gelince minimum ekle"* (m.5/YAGNI). ★ Kanon-uyarısı: m.30 (ajan-kanonu) bugün BLOKE (K-009/K-010) → bu TASARIM, canlı-inşa emri değil (m.13); otonomi Salih'te.

## 1. Salih'in fikri (çekirdek)
- **Ekip liderleri + kişiselleştirme:** her lider bir işçi-ajan ekibini yönetir; kişiselleştirilir.
- **İki soru:** (a) görev-dağılımı nasıl olmalı? (b) kategorizasyon nasıl yapılmalı?
- **Kişiselleştirilmiş hafıza modeli + ingest mekanizması** (lider-başına) — "demiştik" (önceki bağlam: rapor 14 ingest-aile + m.30b).

## 2. Görev-dağılımı + kategorizasyon (TEZ — aebd607d placeholder + JARVIS ön-taslak)
**JARVIS ön-tasarım (üç-katman köprü, m.17):** `Salih → Carvis (CEO/orkestratör) → EKİP LİDERLERİ (supervisor) → işçi-ajanlar`. Carvis Salih'in emrini ayrıştırır → kategoriye göre lidere delege eder → lider alt-ayrıştırır → işçilere dağıtır → toplar/sentezler → Carvis'e döner. (= orchestrator-worker deseni; bu oturumun kendisi = Carvis'in atlas-şeritlerini fan-out etmesi = prototip.)
- **Kategorizasyon ekseni (öneri, 3 aday):**
  - **İŞLEV-başına (öneri ✅):** araştırma-lideri · kod-lideri · inceleme/red-team-lideri · damıtma/wiki-lideri. JARVIS'te ZATEN var olan tekrarlayan roller (atlas · build · review · damıtma) → doğal harita, düşük-yeni-yapı.
  - **DOMAIN-başına:** PortRisk-lideri · wiki-lideri · öğrenme-lideri.
  - **PROJE-başına:** her flagship/proje bir lider.
- **Görev-dağılımı ilkeleri:** ayrıştır-delege-topla; lider işçiye **tek-net-adım** verir (m.17 köprü + strong-style, rapor 13); span-of-control = fan-out sınırı (rapor 12 concurrency deseni).

**Atlas TEZ (aebd607d) — dört-ayak yerleşik desene oturuyor:**
- **Orchestrator-worker/supervisor:** lider sorguyu ayrıştır→3-5 işçiye **detaylı-brief**le delege→paralel-yürüt→sentezle→denetle. Anthropic çok-ajan-araştırma tek-ajana karşı **+%90.2** (⚠~15× token; yalnız paralel/salt-okunur genişlik-işinde); **delegasyon-kalitesi = brief-kalitesi** (m.17 köprü birebir). LangGraph **supervisor-of-supervisors** = Carvis→lider→işçi; CrewAI hierarchical (manager-ajan önden-delegasyon+inceleme); Swarm hand-off = fonksiyon-devri.
- **★ Span-of-control (kaç lider — çarpıcı yakınsama):** klasik Graicunas/Urwick **4-5 ast** ∧ Anthropic **3-5 alt-ajan** birebir örtüşüyor. Ölçekleme-bilimi (⚠doğrulanmadı): ~**7-optimum** sonra bozulma; **yetenek-doygunluğu** (tek-ajan baseline >~%45 ise koordinasyon NEGATİF); **hata-yayılımı bağımsız 17.2× vs merkezi 4.4×** → **merkezi lider = HATA-FRENİ** (rapor 1 denetim-basamağını haklı çıkarır). **Öneri: lider→işçi 3-5, Carvis→lider ≤5-7.** Her lider ~15× token+gecikme → yalnız proje-ölçekli/paralel işe (m.25 freni doğru).
- ⚠ **Karşı-kanıt (TEZ'in dürüst kaydı):** "self-organizing > tasarlanmış-hiyerarşi" bazı görevlerde → kategorizasyon **görev-şekline KOŞULLU**, evrensel-kazanç değil (ANTİTEZ §4'ün ana-kozu; sentez §5'te ayrıştırılır).

## 3. Lider-başına kişisel hafıza modeli + ingest (TEZ — aebd607d placeholder + JARVIS ön-taslak)
**★ Rapor 14 sentezinin ajan-başına uygulaması.** İki riskli-uç: N izole-hafıza/ingest (fragmentasyon, rapor 15-antitez) ↔ tek-tip herkese (rol-körü). Sentez: **tek paylaşılan BİÇİM + lider-rolüne göre parametrizasyon, held-out-hak-edilmiş.**
- **Kişisel hafıza (lider-başına):** ortak-substrat = git-as-truth (kanon herkese ortak) + **lider-özel partisyon** (persona/rol-belleği + episodik: geçmiş görevleri + prosedürel: kendi playbook'u). Grain'ler rapor 8: episodik/semantik/prosedürel ayrı işlenir; A-MEM/CoALA modüler-bellek. **İzolasyon değil PARTİSYON** (kanon paylaşımlı, rol-belleği özel) → antitezin fragmentasyon-itirazını karşılar.
- **Kişisel ingest (lider-başına):** rapor 14 matrisi `(model×amaç)` → **`(model×amaç×ROL)`** genişler: araştırma-lideri→derin-kaynak/Adaptive-RAG · kod-lideri→spec+codebase · inceleme-lideri→diff+bağlam · damıtma-lideri→delta/ACE. Her lider ortak ingest-BİÇMİN bir parametrizasyonu; yeni-özel-ingest yalnız **held-out ölçümle hak edilince** (rapor 14 terfi-testi + m.5).

**Atlas TEZ (aebd607d) — hafıza + ingest motorları:**
- **Bellek taksonomisi = CoALA** (working/episodik/semantik/prosedürel = **rapor 8 grain'leri birebir**) + **MemGPT/Letta** (core/recall/archival = **m.22 sıcak/soğuk**) + **Generative-Agents** (retrieval = recency×importance×relevance + **reflection = damıtma-döngüsü**; importance = "Ekrana gel" filtresi) + **A-MEM** (Zettelkasten = **wiki [[link]]**).
- **Kişiselleştirme:** **MAPLE** (Memory/Learning/Personalization = AYRI-alt-ajanlar, farklı zaman-ölçeği; Learning-asenkron/Personalization-gerçek-zamanlı; +%14.6 ⚠doğrulanmadı) + **PersonaAgent** (persona = rol-sistem-prompt'u belleği+aksiyonu **KOŞULLAR**, kapalı-döngü = kişisel-hafıza+kişisel-ingest TEK-çerçeve). **★ Her ekip-lideri = bir persona.**
- **★ İzolasyon (öneri = HİBRİT dual-tier):** özel **rol-belleği** (kişiselleştirme, izole) + **paylaşımlı-blackboard** (kanon/durum-kapsülü TEK-KAYNAK, erişim-kontrollü) → antitezin fragmentasyon+SSOT+poisoning itirazını uzlaştırır (Collaborative/Governed-Shared-Memory; m.20 pointer + m.22 katman ile izomorf).
- **★ Kişisel-ingest = rapor 14 ailesine ÜÇÜNCÜ eksen `(model×amaç×ROL)`:** rol-koşullu retrieval; **ortak-biçim SABİT** (m.20/22/34/[S/O/T]) + rol-parametresi; ayrı-varyant **yalnız held-out-hak-edilince** → kombinatoryal **N+M+R** (eksen-kompozisyonu), N×M×R değil (CACE-freni). Anthropic context-engineering ("bağlam=bütçe", ajan-güdümlü-retrieval) = policy-gövdesi.

**Ekip-lideri = dört-parçalı spesifikasyon (sentez):** (1) orchestrator-worker görev-dağılımı · (2) işlev-başına kategorizasyon (span 3-5) · (3) CoALA-dört-modül + MemGPT-hiyerarşi + reflection, hibrit-izolasyon (MAPLE-persona) · (4) rol-eksenli ingest, held-out-hak-edilmiş. **Tek cümle:** *Ekip-lideri = "kendi rol-belleğini taşıyan bir supervisor-persona"; kişiselleştirme paylaşılan-biçmin parametrizasyonudur, held-out ile hak edilir.*

## 4. ANTİTEZ (çift-atlas karşıt-şerit — a095e822 döndü) — Red-Team
> **Çerçeve:** m.37 karşıt-temel girdisi; steelman. **★★ En değerli çıkarım: tez İKİ ekseni karıştırıyor** — (1) **geçici ayrıştırma** (görev-anında subagent açma) = savunulabilir, kanıtlı; (2) **kalıcı, kategorize, kişiselleştirilmiş lider + izole-hafıza + özel-ingest** = zayıf-destekli. Antitezin darbesi **eksen-2'ye**, eksen-1'e değil.

**Top karşı-argümanlar:**
- **★ Hiyerarşik-lider muhtemelen yanlış:** Cognition "don't build multi-agents" (bağlam-parçalanması + çelişen-örtük-kararlar → tek-iş-parçacıklı üstün, Flappy-Bird örneği); **MAST** (Berkeley, 1600+ iz, κ=0.88): MAS hatalarının ~%76'sı **koordinasyon/tasarımdan** (spec %44 + ajan-yanlış-hizalanma %32), ajan-zekasından değil — lider-hiyerarşisi tam bu katmanı EKLER; tek-güçlü-ajan eşit-token'da multi-hop'ta çoklu-ajanı geçiyor (⚠2026-cutoff-sonrası); orkestratör = tek-nokta-arıza + bağlam-darboğazı (50+ ara-sonuç→pencere taşar); **self-organizing emergent roller tasarlanmış-hiyerarşiyi geçiyor** (⚠cutoff-sonrası); **context-rot çok-ajanda AMPLIFY** (A'nın çürüğü B'ye yer-gerçeği).
- **★ Per-lider kişisel-hafıza muhtemelen yanlış:** SSOT tutarlılık için üstün; izole-hafıza = fragmentasyon + senkron-yükü; poisoning çok-ajanda otomatik yayılır (yatay/dikey/zamansal) — **iki-yönlü keser** (izole=N-kat-bakım/ıraksama, paylaşılan=tek-noktadan-bulaşma) → çözüm "**kapsamlı-paylaşım + namespace-izolasyon + erişim-kontrolü**", saf-silo değil; **persona minimal doğruluk-kazancı, kırılgan/önyargı-üretici** (kişiselleştirme çoğu kez kozmetik).
- **★ Kategorizasyon + özel-ingest premature:** sabit-taksonomi = erken-soyutlama (roller emergent olmalı, homojen-başla→işletimde-farklılaş); **N-lider×özel-ingest = CACE** (Sculley: değiştir-her-şeyi-değiştirir, süper-lineer entanglement/bakım) — **rapor 14 antiteziyle YAKINSAK** (özel-ingest yalnız held-out-hak-edilince).

**Steelman (tez GERÇEKTEN sağlam nerede):** ① gerçek span/bağlam-sınırı (Anthropic çok-ajan-araştırma **%90.2**, ⚠doğrulanmamış — yalnız genişlik-öncelikli/salt-okunur/paralel işte); ② gerçek birleştirilemez rol-uzmanlığı (AgentGroupChat-V2: 2-ajan %32.5→5-ajan %53.5, uzmanlaşma ölçekle iyileşir); ③ denetlenebilirlik/hata-atfı gerçek kazanç (MAST "verification" kategorisi).

## 5. Sentez (diyalektik — a095e822)
**★ Ayrıştırıcı değişken: görevin gerçek PARALELLEŞTİRİLEBİLİRLİĞİ + bağlanma-sıkılığı** (Amdahl-benzeri kapalı-form sınır; ⚠MARL/uzamsal ortamlardan transfer, analojik).
- **TEZ kazanır:** yüksek-paralel + salt-okunur-genişlik (araştırma/tarama, Anthropic %90.2) · gerçek birleştirilemez darboğaz-rolleri · denetlenebilirlik-zorunlu · ölçek büyük (tek-pencere işi taşımıyor).
- **ANTİTEZ kazanır:** sıkı-bağlı/yazma-ağırlıklı/ardışık iş (kodlama, tek-artefakt → Cognition tek-iş-parçacıklı) · iş-fungible (herkes-her-şeyi) · tutarlılık-kritik (SSOT) · kanıt-yok (emergent>dayatılmış) · persona-kazancı-ispatlanmamış.
- **★ Diyalektik çözüm (rapor 15 üst-cümlesi):** *Geçici-ayrıştırmayı (görev-anında subagent) kanıtla benimse; kalıcı-kişiselleştirilmiş-lider + izole-hafıza + özel-ingest'i VARSAYILAN yapma — yalnız (a) paralelleştirilemez darboğaz-rolleri + (b) held-out'ta ispatlanmış persona/ingest kazancı + (c) denetlenebilirlik-zorunluluğu BİRLİKTE doğrulandığında hak ettir. Varsayılan = tek parametrik ingest + kapsamlı-paylaşılan-hafıza (namespace-izolasyonlu) + emergent rol; sapma kanıtla gelir.*
- **★ m.30 pratik sonucu:** m.30 BLOKE (K-009/K-010) iken kalıcı-lider mimarisine KİLİTLENME — premature-abstraction cezası bloke-dönemde en yüksek + kanıt-tabanı 2026-cutoff-sonrası/doğrulanmamış. **Geçici subagent deseni bugün zaten kullanılabilir, düşük-taahhüt** (bu oturumun atlas-fan-out'u = kanıt/prototip).
- **5-antitez meta-deseniyle tutarlı:** "ŞİMDİ değil — ÖLÇ — kanıt gelince minimum ekle" (YAGNI + m.5). Özel-ingest → rapor 14 held-out-kapısına bağlanır; rapor 14 iç-gerilimi (m.30(b) aile ↔ m.21/m.34 tek-şema) burada somutlaşır.

## 6. Kanon bağı (ön-taslak)
- **m.30 (ajan-kanonu, BLOKE K-009/K-010):** ekip-liderleri m.30'un tam konusu; **m.30(b) "her ajan farklı özütleme algoritması taşıyabilir" = kişisel-ingest tezinin kanon-çekirdeği** (rapor 14 iç-gerilimi burada somutlaşır). Bugün BLOKE → tasarım-hazır, otonomi Salih/Fable.
- **m.17 (köprü):** Carvis→lider→işçi = köprünün çok-katmanlı hâli; feedback en verimli halde işçiye ulaşır.
- **m.25 (görev-ölçek):** küçük-iş direkt, proje-ölçek→lidere-delege; ekip-lideri = "ajan-atama"nın ölçeklenmiş hâli.
- **m.31 (yetki):** lider = Katman-2 (yapar+kaydeder, veto=revert); publish/para/kanon = Katman-1 Salih. Lider Salih'in yetkisini DEVRALMAZ.
- **rapor 1** (otonomi-merdiveni: lider-otonomisi HITL→HOTL) · **rapor 14** (ingest-aile: kişisel-ingest = held-out-hak-edilmiş parametrizasyon) · **rapor 8** (bellek-grain'leri) · **rapor 13** (lider→işçi tek-net-adım, strong-style) · **rapor 12** (fan-out/span concurrency + gözetim-katmanları).

## 7. Açık sorular (Salih/Fable — KARAR ALINMADI)
- Kategorizasyon ekseni: İŞLEV mi (araştırma/kod/inceleme/damıtma) / DOMAIN mi / PROJE mi — yoksa hibrit mi?
- Kaç ekip-lideri (span-of-control)? Sabit mi, ölçekle-büyür mü?
- Kişisel-hafıza: izole mi, paylaşılan-git + rol-partisyonu mu (öneri)?
- Kişisel-ingest ne zaman "hak edilir" (rapor 14 held-out eşiği) — yoksa baştan rol-başına mı?
- Ekip-liderleri m.30 (BLOKE) açılışına mı bağlı, yoksa bugün tek-atış/gözetimli prototip mi?
- Lider bir Claude Code subagent-type mı, ayrı-session mı, skill-orkestratör mü (rapor 3/4 bağı)?
