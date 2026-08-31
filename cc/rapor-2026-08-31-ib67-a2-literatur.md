# A2 — Antitez Literatür Taraması (İB-67)

**AS-OF:** 2026-08-31 · **Aile:** A2 (antitez) · **Model:** sonnet · **Rejim:** maliyet-öncelikli · **Ajan-tur bütçesi:** ≤15 araç çağrısı (kullanılan: ~10 WebSearch + 1 Write)

Yöntem: her aday için ≥3 bağımsız WebSearch sorgusu (arXiv/ACL/NeurIPS-ICSE-FSE/agent-eval-agentops odaklı). Açılmayan URL'ler için "arama-sonucu" ibaresi kullanıldı, "birincil kaynak" denmedi. Uydurma URL/DOI yok — tüm bağlantılar arama motorundan gelen ham sonuçlardır, doğrudan doğrulanmadı.

---

## A67-4 (gnhf vakaları)

İddia: "(a) ajanın kendi repo-güvenlik freniyle çarpışması + (b) önbellek-okumalı token bütçesinin iterasyon-tabanı olarak ölçülmesi (~300k/iterasyon taban) + ajan-turu-uykusu maliyet sınıfı."

**Sorgular (birebir):**
1. `LLM agent long-horizon token budget measurement per iteration`
2. `prompt cache read cost agentic loop measurement`
3. `agent guardrail self-collision policy conflict autonomous agent repository safety`

**En-yakın-komşu çalışmalar (arama-sonucu):**
- "Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks" — arXiv 2601.06007 (arama-sonucu)
- "BAGEN: Are LLM Agents Budget-Aware?" — arXiv 2606.00198 (arama-sonucu)
- "IterResearch: Rethinking Long-Horizon Agents with Interaction Scaling" — arXiv 2511.07327 (arama-sonucu)
- "ContextWeaver: Selective and Dependency-Structured Memory Construction for LLM Agents" — arXiv 2604.23069 (arama-sonucu)
- "AgentDoG 1.5: A Lightweight and Scalable Alignment Framework for AI Agent Safety and Security" — arXiv 2605.29801 (arama-sonucu)
- Genel bulgu: cache-read maliyeti standart girdinin ~%10-25'i (sağlayıcıya göre); ajan turlarında bağlam biriktikçe sonraki çağrılar daha pahalı — bu genel mekanizma yerleşik literatür.

**Değerlendirme:**
- (b) kısmı — "iterasyon-tabanlı token/cache-maliyet ölçümü": **KISMİ**. Mekanizma (cache-read indirimi, iterasyon başına maliyet artışı, bütçe-farkındalıklı ajan ölçümü) literatürde var (Don't Break the Cache, BAGEN). Ama "~300k/iterasyon somut taban" + "ajan-turu-uykusu (idle/wait) ayrı maliyet sınıfı" birleşimi arama sonuçlarında bulunamadı `[?]`.
- (a) kısmı — "ajanın kendi repo-güvenlik freniyle çarpışması" (self-collision with own guardrail, spesifik olay sınıfı olarak): arama sonuçlarında yok; genel "guardrail/policy conflict" literatürü var ama bu spesifik çatışma-olayı-sınıflandırması bulunamadı `[?]`.

**Yenilik durumu: KISMİ.** İddia etiketi: **KISMEN DESTEKLİ** (b'nin genel mekanizması bilinen alan) + **DAYANAKSIZ** (a'nın spesifik "self-collision" olay-sınıfı ve b'nin "~300k taban + uyku maliyet sınıfı" somutluğu için doğrudan kanıt yok, ama bunlar zaten olgu-kaydı niteliğinde, "yenilik iddiası" olarak zayıf çerçevelenmiş olabilir).

---

## A67-5 (İB-57)

İddia: "Çok-ajanlı geliştirme ortamında hangi iş sınıfının headless koşabileceğini ask_oran (AskUserQuestion sıklığı) türetilmiş, deterministik LLM'siz sınıflandırma proxy'si."

**Sorgular (birebir):**
1. `human-in-the-loop necessity prediction agent tasks clarification question rate`
2. `task automatability classification from interaction logs headless agent autonomy`
3. `clarification question frequency metric LLM agent autonomy proxy`

**En-yakın-komşu çalışmalar (arama-sonucu):**
- "HiL-Bench (Human-in-Loop Benchmark): Do Agents Know When to Ask for Help?" — arXiv 2604.09408 (arama-sonucu) — **en yakın komşu**: ask-rate'i doğrudan ölçüyor, "judgment, not capability" bulgusu; tam bilgiyle %75-89 pass@3, ne zaman soracağını bilmesi gerektiğinde %4-24'e düşüyor.
- "Levels of Autonomy for AI Agents Working Paper" — arXiv 2506.12469 (arama-sonucu) — involvement log/diary'den post-hoc otonomi-seviyesi sınıflandırması öneriyor; ask_oran'a çok yakın bir mekanizma.
- "Uncertainty-Aware Clarification in LLM Agents with Information Gain" — arXiv 2606.03135 (arama-sonucu) — mesaj-sıklığı 0.7-8.3/koşum aralığı, otonomi vekili olarak.
- "DeskCraft: Benchmarking Desktop Agents on Professional Workflows and Human-in-the-Loop Collaboration" — arXiv 2606.03103 (arama-sonucu)

**Değerlendirme:** Çekirdek fikir — "soru sorma sıklığından otonomi/uygunluk türetme" — literatürde güçlü paralellerle karşılanıyor (HiL-Bench doğrudan bunu ölçüyor; Levels-of-Autonomy log-tabanlı post-hoc sınıflandırma öneriyor). Ancak "deterministik, LLM'siz, iş-sınıfı headless-uygunluk proxy'si olarak ask_oran" somut kombinasyonu (metrik → otomatik headless/HITL-gerekli ikili karar kuralı) arama sonuçlarında birebir bulunamadı `[?]`.

**Yenilik durumu: KISMİ (DÜŞTÜ'ye yakın).** İddia etiketi: **KISMEN DESTEKLİ** — temel mekanizma (ask-rate → otonomi/başarı ilişkisi, log-tabanlı sınıflandırma) yerleşik; "deterministik LLM'siz proxy" formülasyonunun özgünlüğü zayıf, çünkü aynı sinyali kullanan komşu çalışmalar var.

---

## A67-6 (K-010 A1-A4)

İddia: "Ajan otonomisini takvimle değil KOŞUM-SAYILI kanıt kapılarıyla (A1 pilot, A2 tatbikat, A3 goal/loop, A4 denetim çatalı) kademelendiren ve 'go-gate ≠ reliability' ayrımını yapan kanıt-kapılı otonomi merdiveni."

**Sorgular (birebir):**
1. `staged autonomy levels AI agent deployment evidence gates pilot runs`
2. `evidence-based agent rollout governance progressive autonomy framework LLM agents`
3. `go-gate reliability distinction model release gating autonomy taxonomy`

**En-yakın-komşu çalışmalar (arama-sonucu):**
- "The Autonomy Gate: How Multi-Level Agent Evaluation Turns Human Approval Into Machine Approval" — vadim.blog (arama-sonucu) — doğrudan "insan onayını makine onayına çeviren" kademeli otonomi kapısı fikri.
- "Evidence-Driven Release Gates for LLM Sales Agents" — vadim.blog (arama-sonucu) — eval-pencereli PROMOTE/HOLD/ROLLBACK kararı; "kanıt biriktikçe otonomi kazanılır" mantığı A1-A4 yapısıyla doğrudan örtüşüyor.
- "Falsifiable Release Gates for Self-Improving Systems: Standing Invariants at Scale" — arXiv 2607.13070 (arama-sonucu) — capability-token + kontrol-halkası; sistem kendi politikasını yalnız sıkılaştırabilir, gevşetemez — otonomi-merdiveni fikrinin biçimsel bir versiyonu.
- "Scaling AI Agents in Engineering: From Pilot to Production Fleet" — Augment Code (arama-sonucu) — Sandbox → Controlled Pilot → Department-Wide → Enterprise-Wide, L0-L4 otonomi seviyeleri, "%40 müdahale gerektiren ajan üretime hazır değil" gibi somut go/no-go eşikleri.
- "CAGE-1: Control, Assurance, and Governance Evaluation for Enterprise Agentic AI" — arXiv 2607.03510 (arama-sonucu)

**Değerlendirme:** Bu üç adayın en zayıf özgünlük profiline sahip olanı. "Kademeli otonomi + kanıt-kapısı + go/no-go eşiği" hem akademik (Falsifiable Release Gates, CAGE-1) hem endüstriyel (Autonomy Gate, Evidence-Driven Release Gates, Augment Code pilot-to-production) literatürde doğrudan ve çok sayıda paralelle karşılanıyor. "Go-gate ≠ reliability" ayrımı da "gate as function of consequence" / PROMOTE-HOLD-ROLLBACK dilinde zaten var.

**Yenilik durumu: DÜŞTÜ.** İddia etiketi: **ÇELİŞİR** — mekanizmanın genel biçimi (koşum-sayılı kanıt kapıları ile kademeli otonomi, go/no-go eşiği) yayınlanmış çalışmalarda ve endüstri pratiğinde önceden var; A67-6'nın özgün payı olsa olsa JARVIS'e özgü A1-A4 adlandırması ve içerik detayı ile sınırlı, mekanizma düzeyinde değil.

---

## Özet tablo

| Aday | Yenilik durumu | İddia etiketi |
|---|---|---|
| A67-4 (gnhf) | KISMİ | KISMEN DESTEKLİ / DAYANAKSIZ (karma) |
| A67-5 (İB-57, ask_oran) | KISMİ (DÜŞTÜ'ye yakın) | KISMEN DESTEKLİ |
| A67-6 (K-010 A1-A4) | DÜŞTÜ | ÇELİŞİR |

Bulunamayan / doğrulanamayan noktalar `[?]` ile işaretlendi; hiçbir URL/DOI uydurulmadı, tümü arama motoru sonucu olarak etiketlendi.
