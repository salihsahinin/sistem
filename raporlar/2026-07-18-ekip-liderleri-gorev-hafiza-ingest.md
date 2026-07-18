# Ekip Liderleri: Görev-Dağılımı + Kategorizasyon + Lider-Başına Kişisel Hafıza & Ingest — Rapor (TARTIŞMA)

> **Mod:** rapor · KARAR YOK · commit onaylı (Salih 07-18); nihai karar = Fable (m.41). Kaynak: Salih 07-18 — "ilerde ekip liderleri oluşturup kişiselleştireceğiz; ekip liderleri nasıl bir görev-dağılımına sahip olmalı ve kategorizasyon nasıl yapılmalı; ekip liderleri için kişiselleştirilmiş hafıza modeli ve ingest mekanizmaları kullanacağız demiştik, bunu nasıl yapabileceğimizi araştır; çift yönlü atlas çalıştır; rapor oluştur." Çift-atlas: TEZ (aebd607d — ekip-lideri tasarımı, KOŞUYOR) + ANTİTEZ (a095e822 — flat/paylaşılan-hafıza, KOŞUYOR). **Rapor 14 (ingest-aile) doğrudan devamı: kişisel-ingest = ailenin ajan/rol-başına örneği.**

---

## 0. BLUF
Ekip-liderleri = Carvis (CEO) ile işçi-ajanlar arasında **orchestrator/supervisor katmanı**; görev-dağılımı = hiyerarşik ayrıştır→delege→topla. Kişisel-hafıza + kişisel-ingest = **rapor 14 sentezinin ajan-başına uygulaması**: tek paylaşılan hafıza/ingest-BİÇİMİ + lider-rolüne göre **held-out-hak-edilmiş parametrizasyon** (N izole sistem değil). ★ Kanon-uyarısı: m.30 (ajan-kanonu) bugün BLOKE (K-009/K-010) → bu TASARIM, canlı-inşa emri değil (m.13); otonomi Salih'te.

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
- **Görev-dağılımı ilkeleri:** ayrıştır-delege-topla; lider işçiye **tek-net-adım** verir (m.17 köprü + strong-style, rapor 13); span-of-control = fan-out sınırı (rapor 12 concurrency deseni). *[Atlas TEZ aebd607d: supervisor/manager-agent, LangGraph/CrewAI/AutoGen/Swarm, hand-off, span-of-control buraya.]*

## 3. Lider-başına kişisel hafıza modeli + ingest (TEZ — aebd607d placeholder + JARVIS ön-taslak)
**★ Rapor 14 sentezinin ajan-başına uygulaması.** İki riskli-uç: N izole-hafıza/ingest (fragmentasyon, rapor 15-antitez) ↔ tek-tip herkese (rol-körü). Sentez: **tek paylaşılan BİÇİM + lider-rolüne göre parametrizasyon, held-out-hak-edilmiş.**
- **Kişisel hafıza (lider-başına):** ortak-substrat = git-as-truth (kanon herkese ortak) + **lider-özel partisyon** (persona/rol-belleği + episodik: geçmiş görevleri + prosedürel: kendi playbook'u). Grain'ler rapor 8: episodik/semantik/prosedürel ayrı işlenir; A-MEM/CoALA modüler-bellek. **İzolasyon değil PARTİSYON** (kanon paylaşımlı, rol-belleği özel) → antitezin fragmentasyon-itirazını karşılar.
- **Kişisel ingest (lider-başına):** rapor 14 matrisi `(model×amaç)` → **`(lider-rolü×amaç)`** genişler: araştırma-lideri→derin-kaynak/Adaptive-RAG · kod-lideri→spec+codebase · inceleme-lideri→diff+bağlam · damıtma-lideri→delta/ACE. Her lider ortak ingest-BİÇMİN bir parametrizasyonu; yeni-özel-ingest yalnız **held-out ölçümle hak edilince** (rapor 14 terfi-testi + m.5). *[Atlas TEZ aebd607d: MemGPT/Letta per-agent memory, persona-memory, role-conditioned ingest, agent-personalization buraya.]*

## 4. ANTİTEZ (çift-atlas karşıt-şerit — a095e822 placeholder)
*[Hiyerarşik-lider YANLIŞ savı: flat/swarm daha iyi, orchestrator/koordinasyon-vergisi, "don't build multi-agent" (Cognition), tek-güçlü-ajan çoklu-ekipten güvenilir, hiyerarşi tek-nokta-arıza · kişisel-hafıza-per-lider YANLIŞ: paylaşılan-tek-hafıza, fragmentasyon/senkron-yükü, persona-hype · kategorizasyon+kişisel-ingest premature (emergent-roller, held-out-hak; N-lider×özel-ingest=CACE). Steelman + SENTEZ buraya — a095e822 dönünce.]*

## 5. Sentez (diyalektik — a095e822 dönünce tamamlanır)
*[Tez hangi ölçekte kazanır (gerçek span/bağlam-sınırı aşınca, gerçek rol-uzmanlığı farkı büyükse) / antitez hangi koşulda (bugün, tek-güçlü-ajan yeterken, kanıt yokken); "ŞİMDİ değil, ÖLÇ, kanıt gelince minimum lider/özel-ingest ekle" motifi (5-antitez meta-deseni). Rapor 14 iç-gerilimiyle (m.30b aile↔m.21/m.34 tek-şema) bağ.]*

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
