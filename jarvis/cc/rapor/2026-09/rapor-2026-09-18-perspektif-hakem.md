# Maskeli Hakem Raporu — Perspektife Göre Ajan Sınırı

**Tarih:** 2026-09-18 · **Rol:** maskeli hakem (bağımsız; üretici koşumların devamı değil) · **Girdi:** 4 aile × (tez + antitez) + V26 örneklem denetimi = 9 rapor, 48 iddia
**Hakem kendi sondajı:** 3 WebFetch (aşağıda `[hakem-fetch]` işaretli) · **AS-OF:** tüm çekimler 2026-09-18

## 0. Uygulanan usul kuralları

- **Maskeli kıyas:** iddialar "tez/antitez" etiketiyle değil, iddia + kanıt olarak kıyaslandı.
- **Antitez-D normalizasyonu:** antitez-D `ÇÜRÜDÜ` etiketini "antitezin kendisi çürüdü, tez ayakta" anlamında kullanmış; bu raporda `ÇÜRÜTÜLEMEDİ`ye çevrildi.
- **V26 tavanı:** `TUTMADI` ≥1 olan raporların (tez-C, antitez-A, antitez-B, antitez-C, antitez-D) bulguları en fazla **K**.
- **V26 kaynak-eşleşme hataları → X:** Plan-and-Act %82 / Routine %41→96, "Ephemeral Cognition" → 2603.04722, FRAMES yön hatası, `sub-agents` doküman alıntıları ("isolation is by design", "varsayılan inherit").
- **Kuşak:** güncel = 2025-Q3 sonrası ∧ 4.x+/5 sınıfı model. AS-OF damgasız ya da model-sürümsüz iddia en fazla K, **tasarım girdisi olarak düşer**.
- **AYRILMALI eşiği:** ≥2 bağımsız güncel-kuşak kaynak; yoksa BELİRSİZ.

### Hakemin kendi ham-kaynak sondajları

| # | URL | Bulgu | Etki |
|---|---|---|---|
| H1 | `https://cognition.com/blog/multi-agents-working` | Sayfada yayın tarihi **04.22.26** açıkça var; "we found this technique to work best when the coding and review agents **do not share any context beforehand**"; "average of 2 bugs per PR, of which roughly 58% are severe"; "Smart Friend" alıntısı birebir. Anılan modeller: Sonnet 4.5, Opus-4.5, SWE-1.5/1.6, Mythos, GPT. | tez-A #6/#7/#8 → **D**, güncel kuşak; antitez-A'nın "[?] yayın tarihi belirsiz" şerhi → **X** |
| H2 | `https://code.claude.com/docs/en/sub-agents` | `model` alanının varsayılanı **`inherit` DEĞİL**; belge "When you omit it, Claude Code picks the model in the subagent model order" diyor ve 4 adımlı çözümleme sırasını veriyor. "Agents cannot access each other's memory directories… by design" cümlesi **belgede yok**. `MEMORY.md` ilk 200 satır/25KB birebir var. Fork: "The exception is a fork, which inherits the parent conversation instead of starting fresh" — `/subtask` ile başlatılan **istisna**, varsayılan değil. | V26 #25/#26/#33 doğrulandı; antitez-B #4, #11 daralmaları ve tez-D #5 → **X** |
| H3 | `https://arxiv.org/html/2604.02460v1` | 5000 token, FRAMES: Gemini 2.5-Pro **SAS 0.700 > Sequential 0.680**; Qwen3-30B 0.260 > 0.252; DeepSeek-R1-70B 0.455 > 0.394; Gemini 2.5-Flash 0.545 > 0.524. Sonuç: "SAS is the strongest default architecture for multi-hop reasoning". | antitez-C #4 `ÇÜRÜDÜ` hükmü ters veriye dayanıyor → **X**; tez-C #4 ayakta (V26 tavanı gereği K, hakem fetch'iyle fiilen D) |

---

## (i) Perspektif × Hüküm Tablosu

Gerekçe sınıfları: **BK** bağlam kirlenmesi · **YÖ** yapan≠ölçen · **YT** yetki · **ML** maliyet · **PR** paralellik.

| Perspektif | Hüküm | Gerekçe sınıfı | Destek (güncel / eski) | En güçlü kaynak · AS-OF · model | Etiket |
|---|---|---|---|---|---|
| **İcra · araştırma** (salt-okur bilgi toplama) | **AYRILMALI** | PR + BK + ML | **2** / 2 | `cognition.com/blog/multi-agents-working` · yayın 2026-04-22, çekim 2026-09-18 · Sonnet 4.5 / Opus-4.5 / SWE-1.6 `[hakem-fetch H1]`; ikinci güncel: `code.claude.com/docs/en/sub-agents` · 2026-09-18 · Opus 5/Sonnet 5 `[H2]`; eski: Anthropic multi-agent-research (2025-06-13, Opus 4+Sonnet 4, +%90.2) | **D** |
| **İcra · refactor/taşıma** (kod yazma) | **KALMALI** (tek iş-parçacığı; paralel-yazan swarm hayır) | BK + YT | **2** / 2 | `cognition.com/blog/multi-agents-working` · 2026-04-22 · Sonnet 4.5/SWE-1.6 — paralel-yazan swarm hükmü korunuyor `[H1]`; ikinci güncel: `anthropic.com/engineering/building-c-compiler` · 2026-02-05 · Opus 4.6 — paralel yazma ancak izolasyon+kilit+dış-oracle ile, paylaşılan bağlamla değil (V26 #22 TUTTU) | **D** |
| **İcra · doküman üretimi** | **BELİRSİZ** | — (gerekçe kaynakta yok) | 0 / 1 | En yakın: Anthropic CitationAgent (üretimden sonra ayrı geçiş) · 2025-06-13 · Opus 4/Sonnet 4 — atıf ekleme, doküman üretimi değil | **K** |
| **İcra · ölçüm** (benchmark/metrik koşumu) | **BELİRSİZ** | YÖ (yalnız değerlendirme ucu için) | 0 / 1 | Anthropic LLM judge · 2025-06-13 · Opus 4/Sonnet 4 — ölçümü **yorumlayan** ayrı, ölçümü **koşan** ajan için kanıt yok | **K** |
| **İcra · hakem kurma** (meta-orkestrasyon) | **BELİRSİZ** | — | 0 / 0 | Hiçbir kaynakta bu perspektif ele alınmamış — **DAYANAKSIZ** | **X** |
| **Hakem / değerlendirici** | **AYRILMALI** | **YÖ** + BK | **2** / 2 | `cognition.com/blog/multi-agents-working` · 2026-04-22 · Sonnet 4.5/Opus-4.5 — "coding and review agents **do not share any context beforehand**", 2 hata/PR, %58 şiddetli `[H1]`; ikinci güncel: `code.claude.com/docs/en/sub-agents` · 2026-09-18 · Opus 5 — `code-reviewer` alt-ajanı `tools: Read, Grep, Glob` (yazma yetkisi yok) `[H2]`; eski: Anthropic CitationAgent + LLM judge (2025-06-13) | **D** |
| **Antitez / red-team** | **BELİRSİZ** | YÖ + BK (iddia edilen) | **0** / 1 | `deepwatch.com/glossary/red-team-agent-in-agentic-ai-mdr` — yayın tarihi **yok**, model damgası **yok** → AS-OF'suz, tasarım girdisi olarak düşer (V26 #27 TUTTU ama antitez-B raporu tavanlı). Akademik debate kanıtı 7-8B eski kuşak (2605.00914) → tasarım girdisi değil | **K** |
| **Planlama** | **BELİRSİZ** | PR (gerekçe kaynaklarda açık değil) | **1** / 2 | `cognition.com/blog/multi-agents-working` · 2026-04-22 — "map-reduce-and-manage" yönetici-çocuk deseni `[H1]`; `cursor.com/blog/plan-mode` · **2025-10-07** (V26 #23: tarih sayfada açık) — ayrımın **gerekçesi verilmemiş**, yalnız sonuç bildirilmiş; HN anekdotu (2026-07-30, Opus plan + Sonnet 5 kod) ikincil → K. Plan-and-Act %82 / Routine %41→96 → **X** (V26 #11: kaynak yanlış eşleşmiş) | **K** |
| **Gözetim / orkestrasyon** | **AYRILMALI** | PR + BK + ML | **2** / 2 | `code.claude.com/docs/en/sub-agents` + `agent-sdk/subagents` · 2026-09-18 · Opus 5 — orkestratör + izole alt-ajan mimarisi birinci sınıf; Opus 5 için `MAX_SUBAGENT_SPAWN_DEPTH`=3, `MAX_CONCURRENT_SUBAGENTS`=20, `maxBudgetUsd` (V26 #21 TUTTU) `[H2]`; ikinci güncel: Cognition map-reduce-and-manage · 2026-04-22 `[H1]`; eski: Anthropic lead agent (2025-06-13) | **D** |
| **Öğretim / tutor** | **BELİRSİZ** | (kalıcı hafıza gerekçesi; perspektif gerekçesi değil) | **0** / 1 | `arxiv.org/abs/2604.26962` DeepTutor · v1 2026-04-10 / v3 2026-07-09 · **model belirtilmemiş** → model-sürümsüz, en fazla K; antitez-D daraltması: makale mevcut ajan çerçevelerini doğrudan eleştirmiyor. Karşı-kanıt (güncel, D): `sub-agents` belgesinde tutor'a özgü ajan sınıfı **yok**, `memory` role-agnostik `[H2]` | **K** |

**Çelişki notu (saklanmıyor):** "İcra · araştırma AYRILMALI" hükmü ile tez-C/K3 bulgusu (`2604.02460`, güncel kuşak: Gemini 2.5-Pro, DeepSeek-R1-70B, Qwen3-30B) **kısmen çelişir**. K3 eşit düşünme-token bütçesinde **sıralı** çok-ajan zincirinin tek-ajandan üstün olmadığını gösteriyor (4 modelin 4'ünde de SAS üstün `[H3]`). Ayrımın lehindeki kanıt **paralel fan-out + izole bağlam** için; **sıralı zincir** için kanıt tersine. Tasarım sonucu: ayrım paralel okuma/araştırma fan-out'unda gerekçeli, sıralı devir zincirinde gerekçesiz.

---

## (ii) Alt-Ajan vs Kalıcı Ajan

Ana kaynak: `https://code.claude.com/docs/en/sub-agents` (çekim 2026-09-18, Opus 5/Sonnet 5/Haiku/Fable alias'ları) `[hakem-fetch H2]` ve `https://code.claude.com/docs/en/agent-sdk/subagents` (V26 #7/#21 TUTTU).

| Boyut | Alt-ajan (subagent) | Kalıcı ajan (`memory` alanlı / ana oturum) | Kaynak · AS-OF · etiket |
|---|---|---|---|
| **Hafıza** | Varsayılan yok: "Each subagent starts with a fresh, isolated context window. It doesn't see your conversation history, the skills you've already invoked, or the files Claude has already read." | `memory: user\|project\|local` → `~/.claude/agent-memory/<ad>/` · `.claude/agent-memory/<ad>/` · `.claude/agent-memory-local/<ad>/`; `MEMORY.md`'nin ilk **200 satır ya da 25KB**'ı (hangisi önce) sistem promptuna eklenir | `sub-agents` · 2026-09-18 · Opus 5 kuşağı · **D** `[H2]`, V26 #14/#32 TUTTU |
| **Hafıza — çapraz görünürlük** | Dizinler ajan adına göre ayrı; **ancak** "Agents cannot access each other's memory directories… by design" cümlesi güncel belgede **yok** | — | V26 #25/#33 `TUTMADI` + `[H2]` → **X** (mekanizma makul, alıntı dayanaksız) |
| **Kimlik** | Adlandırılmış tanım dosyası var, örnek sürekliliği yok; her çağrı yeni örnek. İstisna: **fork** — "The exception is a fork, which inherits the parent conversation instead of starting fresh", `/subtask` ile başlatılır | Aynı adlandırılmış tanım + kalıcı bilgi deposu; kimlik dosyada, süreçte değil | `sub-agents` · 2026-09-18 · **D** `[H2]`. "Fork v2.1.232'den beri varsayılan" iddiası (antitez-B #11) ikincil kaynağa dayanıyor, belge fork'u **istisna** olarak tarif ediyor → **X** |
| **Yetki** | İki katmanlı filtre: her alt-ajandan kaldırılan araçlar (`AskUserQuestion`, `ExitPlanMode`, `Workflow`…) + arka-plan alt-ajanı için dar liste; `tools` allowlist / `disallowedTools` denylist, `mcp__<server>` deseni; `permissionMode` ayrı | Bellek etkinse `Read`, `Write`, `Edit` **otomatik** açılır (kendi bellek dosyasını yönetebilsin diye); fork ana konuşmanın tam araç havuzunu alır | `sub-agents` · 2026-09-18 · **D** `[H2]`, V26 #32 TUTTU |
| **Oturum** | Ana konuşmanın cwd'sinde başlar; `cd` çağrılar arası kalıcı değil; `isolation: worktree` ile izole kopya. Yalnız **son mesaj** ebeveyne döner, ara adımlar sızmaz | Kalıcı olan **dizin**, süreç değil: kalıcı ajanın koşumu da çağrı ömrüyle sınırlı | `agent-sdk/subagents` · 2026-09-18 · **D**, V26 #7 TUTTU |
| **Maliyet** | Çok-ajan ≈ **15×**, tek ajan ≈ **4×** sohbet token'ı; alt-ajana ucuz model yönlendirme (`haiku`) ile maliyet kontrolü; Opus 5 için `maxBudgetUsd` + derinlik 3 + eşzamanlılık 20 tavanları | Her çağrıda ≤200 satır/25KB `MEMORY.md` sabit ek token yükü; tekrar-keşif tasarrufu **ölçülmemiş** `[?]` | Anthropic multi-agent-research · 2025-06-13 · Opus 4/Sonnet 4 (**eski kuşak**) · **D** (V26 #2/#16/#34 TUTTU); tavanlar `agent-sdk/subagents` 2026-09-18 · **D** |

**Yapısal fark özeti:** alt-ajan = *bağlam izolasyonu + tek dönüş kanalı + kısıtlanabilir yetki*, kalıcı ajan = *adlandırılmış kalıcı dosya deposu + kendi deposunu yazma yetkisi*. Süreç kalıcılığı **hiçbir üründe yok**; "kalıcı ajan" pratikte kalıcı **dizin**tir. **DESTEKLİ**, D.

---

## (iii) Model Katmanlaması Bulgusu

İncelenen pratik: *"en güçlü model yalnız orkestratör, kalıcı liderler orta model, işçiler ucuz model."*

**Destekleyen kanıt**

| Kanıt | AS-OF | Model | Etiket |
|---|---|---|---|
| "a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by **90.2%**" | yayın 2025-06-13, çekim 2026-09-18 | Opus 4 (lider) + Sonnet 4 (işçi) — **eski kuşak** | **D** (V26 #3/#6/#15/#19/#24/#34 altı kez TUTTU) |
| "upgrading to Claude Sonnet 4 is a larger performance gain than doubling the token budget on Claude Sonnet 3.7" — model kalitesi > token bütçesi | 2025-06-13 | Sonnet 3.7 → Sonnet 4 — **eski kuşak** | **D** |
| "Control costs by routing tasks to faster, cheaper models like Haiku" + per-alt-ajan `model` alanı (`sonnet`/`opus`/`haiku`/`fable`, `claude-opus-5`, `claude-sonnet-5`) | 2026-09-18 | **güncel kuşak** | **D** `[H2]` |
| HN pratisyen anekdotu: "Opus for planning at high effort and Sonnet 5 for coding at max effort" | 2026-07-30 | Opus + Sonnet 5 — güncel | **K** (ikincil anekdot, birincil açılmadı) |
| morphllm: "You almost never want Haiku as your main session model — you want it as the model your subagents run on" | 2026-09 | Haiku 4.5 | **K** (açılmadı) |

**Çürüten / daraltan kanıt**

| Kanıt | AS-OF | Model | Etiket |
|---|---|---|---|
| **"Smart Friend" — ters yön:** "let the primary/smaller model decide when a situation was tricky enough to be worth consulting the smarter/expensive model" — sabit hiyerarşi değil, **talep-üzerine eskalasyon**; Cognition mekanizmayı kusursuz da sunmuyor ("the model deciding when to delegate isn't the smarter one") | yayın 2026-04-22, çekim 2026-09-18 | Sonnet 4.5 / Opus-4.5 / SWE-1.6 — **güncel kuşak** | **D** `[H1]` |
| Cognition, büyük-model-karar + küçük-model-apply katmanlamasını **denedi ve terk etti**: "the small model frequently misinterpreted instructions due to subtle ambiguities, causing incorrect edits" | 2025-06-12 | belirtilmemiş — eski | **K** (model damgasız) |
| Belgede model seçimi **risk/önem** eksenine göre örneklenmiş ("use a more capable model for high-stakes reviews"), perspektife göre **otomatik atama yok**; varsayılan `inherit` **değil**, 4 adımlı çözümleme sırası uygulanır | 2026-09-18 | Opus 5 kuşağı | **D** `[H2]`; antitez-B'nin "varsayılan inherit" daraltması → **X** |
| Anthropic kendi ürününde en güçlü modeli **lider** yapıyor, "orta model lider" değil | 2025-06-13 | Opus 4 lider | **D** |

**Hüküm:**
1. *"İşçiler ucuz model"* → **DESTEKLİ**, güncel kuşakta ürün düzeyinde birinci sınıf mekanizma (per-ajan `model` alanı + maliyet tavanı). **D**.
2. *"En güçlü model orkestratör"* → **DESTEKLİ ama yalnız eski kuşakta ölçülü** (%90.2, Opus 4/Sonnet 4, 2025-06). Güncel kuşakta aynı düzeni **ölçen** kaynak bulunamadı; Cognition'ın güncel-kuşak pratiği **ters yönde** (ucuz varsayılan + eskalasyon). **ÇELİŞİR**.
3. *"Kalıcı liderler orta model"* → **DAYANAKSIZ**. Hiçbir kaynak kalıcı lider katmanına orta model atanmasını ne savunuyor ne ölçüyor; tez-D'nin kendisi de "doğrudan çürüten kaynak bulunamadı, doğrudan destekleyen de yok" diyor. **X**.

---

## (iv) Reddedilen / Geri Alınan Ayrımlar

| # | Ayrım | Kim | Gerekçe | Tarih | Model | Etiket |
|---|---|---|---|---|---|---|
| 1 | Paralel-yazan çoklu ajan (kod yazımı) | Cognition/Devin | "parallel sub-agents is inherently fragile, doomed by context isolation that leads to conflicting decisions" (Flappy Bird örneği) | 2025-06-12 | belirtilmemiş | **D** (V26 tez-A 0 TUTMADI) |
| 2 | (1)'in **kısmi geri alımı** | Cognition/Devin | Paralel-yazan swarm hükmü korunuyor; çalışan dar sınıf: tek-iş-parçacıklı yazma + ayrı-bağlamlı inceleme, map-reduce-and-manage, Smart Friend | **2026-04-22** | Sonnet 4.5 / Opus-4.5 / SWE-1.6 | **D** `[H1]` |
| 3 | Büyük-model-karar + küçük-model-apply | Cognition/Devin | Küçük model ince belirsizlikleri yanlış yorumladı, hatalı düzenleme üretti | 2025-06-12 | belirtilmemiş | **K** (model damgasız) |
| 4 | Basit sorguda 50 alt-ajan doğurma / tekrar | Anthropic | Erken arıza; düzeltmeyle çözüldü, ayrım terk edilmedi | 2025-06-13 | Opus 4/Sonnet 4 | **K** |
| 5 | Sıkı-bağımlı işte paylaşılan-bağlamlı paralel ajan | Anthropic (C-compiler) | "Every agent would hit the same bug, fix that bug, and then overwrite each other's changes" → çözüm izolasyon + kilit + dış-oracle, paylaşılan bağlamı artırmak değil | 2026-02-05 | Opus 4.6 | **D** (V26 #22 TUTTU) |
| 6 | "AutoGen → AG2 + Agent Framework ikiye ayrıldı" | (iddia) | **Kronoloji yanlış:** AG2 çatallanması 2024-11, Ekim 2025 olayı bakım-modu + Semantic Kernel birleşimi | 2025-10 / 2026-06-18 | model bağımsız | **X** (nedensellik yanlış çerçevelenmiş) |
| 7 | "Fork v2.1.232'den (2026-08-13) beri varsayılan" | (iddia) | Birincil değişiklik güncesi açılamadı; resmî belge fork'u `/subtask` ile başlatılan **istisna** olarak tarif ediyor | iddia 2026-08-13 | — | **X** `[H2]` |
| 8 | "Ephemeral Cognition" ayrımı (2603.04722) | (iddia) | Terim kaynakta **hiç geçmiyor**; makale ilgisiz klinik-metafor çerçevesi | 2026-03 | — | **X** (V26 #12/#30) |
| 9 | Task-Decoupled Planning %82 token tasarrufu / Routine %41→%96 | (iddia) | Kaynak yanlış eşleşmiş (Plan-and-Act makalesinde bu rakamlar yok; makalenin sonucu WebArena-Lite %53.94) | 2025-03 | — | **X** (V26 #11/#13) |

---

## (v) Hayatta-Kalma Özeti (48 iddia)

| Aile | Sağlam çekirdek | Daralan | Düşen | Toplam |
|---|---|---|---|---|
| **A** — sektör öncülleri | **10** | 2 (#3 sıkı-bağımlılık kapsamı, #5 "genel kural" formülasyonu) | 0 | 12 |
| **B** — pratisyen sistemler | **10** | 1 (#10 AutoGen kronolojisi) | 1 (#12 "hiçbiri red-team tanımlamıyor" evrensel-olumsuzu) | 12 |
| **C** — akademik/benchmark | **5** | 3 (#3 token çarpanı mimari-özgü, #6 heterojenlik koşullu, #7 orkestrasyon kazancı kurulum-özgü) | 4 (#9 TDP, #10 Ephemeral Cognition, #11 sayısal kanıt yok, #12 tutor doğrulanmamış) | 12 |
| **D** — ajan sınıfları / model katmanı | **8** | 2 (#6 çözümleme sırası sürüm-bağımlı, #10 DeepTutor çerçeve eleştirisi yok) | 2 (#5 bellek-izolasyonu alıntısı kaynakta yok, #12 gövde erişilemezliği yanlış) | 12 |
| **Toplam** | **33** | **8** | **7** | **48** |

**Aile kalitesi:** A ve B adversarial baskıya en dayanıklı (20/24 sağlam) — çünkü iddialar doğrudan birincil ürün belgesi/mühendislik yazısına çıpalı. C en kırılgan (5/12) — iddiaların çoğu arama-motoru özetinden türetilmiş, V26 üç ayrı kaynak-eşleşme hatası buldu.

---

## (vi) İç Ölçüme Kalan Büyüklükler (BELİRSİZ satırlar için)

| BELİRSİZ satır | Ölçülecek büyüklük | Ölçüm tasarımı | Karar eşiği |
|---|---|---|---|
| **İcra · doküman üretimi** | Aynı ajanın üretip biçimlendirdiği rapor vs ayrı biçimlendirme ajanı: Salih'in düzeltme sayısı / teslim | ≥10 teslimlik A/B; bağımlı değişken: teslim başına Salih düzeltmesi + ilk-ekran kabul oranı | Ayrı ajan düzeltmeyi ≥%30 azaltırsa AYRILMALI |
| **İcra · ölçüm** | Ölçümü koşan ajanın kendi ölçümünü raporlarken sapma oranı | `veri/gorunum/` sayılarının bağımsız ikinci koşumla karşılaştırılması, n≥20 rakam | Sapma >%5 ise ölçen ≠ raporlayan ayrılır |
| **İcra · hakem kurma** | Hakem emrini yazan ajanın beklentisinin hakem hükmüne sızma oranı | Maskeli vs maskesiz hakem, aynı girdi; hüküm dağılımı farkı | Hüküm dağılımı farkı anlamlıysa maske zorunlu (bu koşumda maske **zaten** uygulandı) |
| **Antitez / red-team** | Ayrı kalıcı red-team ajanı vs aynı ajanda antitez turu: bulunan gerçek kusur sayısı / token | Aynı 10 karar üzerinde iki kurulum; bağımlı değişken: Salih'in "geçerli itiraz" saydığı bulgu sayısı | Ayrı ajan ≥1.5× geçerli itiraz üretirse AYRILMALI |
| **Planlama** | Plan-önce ayrı bağlam vs aynı bağlamda plan: plan-sapması (planlanan adım / gerçekleşen adım) | ≥15 görevlik karşılaştırma; `cc/pipeline/` manifestlerinden ölçülebilir | Sapma ≥%25 azalırsa AYRILMALI |
| **Öğretim / tutor** | Kalıcı öğrenci modeli (ders-arası hafıza) ile ilerleme hızı | `ogrenme/` şeritlerinde `PROBE` skorlarının ders-arası seyri, hafızalı vs hafızasız | `PROBE` skor artışı hafızalı kurulumda anlamlı yüksekse AYRILMALI |
| **Kalıcı ajan maliyeti** | `MEMORY.md` sabit ek token yükü vs tekrar-keşif tasarrufu (hiçbir kaynakta ölçülmemiş `[?]`) | Bellekli/belleksiz alt-ajan çiftinin çağrı başına toplam token'ı | Tasarruf < sabit yük ise bellek kapatılır |

---

## (vii) m.16 Çelişki Bölümü (yalnız işaretleme; çözülmüyor)

1. **"Hakem = alt-ajan" varsayımı ile (i) tablosu çelişiyor.** Hakem/değerlendirici AYRILMALI hükmü **D** ve gerekçesi *yapan≠ölçen + önceden bağlam paylaşmama* (`[H1]`: "do not share any context beforehand"). Alt-ajan bu şartı sağlıyor (izole bağlam, tek dönüş kanalı) **ancak** yapısal olarak ebeveynin emrini alıyor; emri yazanın beklentisi maskelenmediğinde `yapan≠ölçen` ihlal olur. Kanon `cc.md` "yapan ≠ ölçen" diyor ama hakemi alt-ajan olarak konumlandırıyor — bu koşumda maske elle uygulandı, **mekanizma değil usul olarak**. İşaretlenir.
2. **"Köle ≠ üst-orkestratör ≠ domain-lider" üç katmanlı rol modeli ile model katmanlaması bulgusu çelişiyor.** Kanon (Karar 89 / `cc.md`): Fable ana-sıra → Opus 5 **kalıcı lider** → Sonnet işçi. (iii)-3 hükmü: *"kalıcı liderler orta model"* için **hiçbir destekleyici kaynak yok** (**X**, DAYANAKSIZ). Ölçülmüş tek düzen ters yönde: en güçlü model **lider**, orta model **işçi** (Opus 4 lider + Sonnet 4 işçi, +%90.2, eski kuşak). Üç katmanlı model ataması dış kanıtla değil iç tercihle duruyor — işaretlenir.
3. **Güncel kuşak, sabit hiyerarşiden uzaklaşıyor.** Cognition'ın 2026-04 güncel-kuşak pratiği (`[H1]` Smart Friend) **ucuz model varsayılan + talep-üzerine eskalasyon**; kanonun sabit üç katmanı bu yönle çelişir. Çözülmedi, işaretlendi.
4. **"Ana-sıra ajan proje işini kendisi yapmaz" (jarvis AGENTS.md §1) ile "İcra · refactor KALMALI" hükmü gerilimde.** Kod yazımının tek iş-parçacığında kalması gerektiği **D** etiketli; kanon icrayı aşağı devrediyor. Çelişki, ayrımın **paralellik** boyutunda değil **yazma yetkisinin dağıtılması** boyutunda. İşaretlenir.

---

## (viii) Masa Kalemi Taslağı — İlk Ayrılacak Perspektif

**Kalem:** Hangi perspektif önce ayrı ajana/bağlama çıkarılsın?
**Kanıt durumu:** AYRILMALI hükmü **D** etiketiyle üç satırda: hakem/değerlendirici, gözetim/orkestrasyon, icra·araştırma. Gözetim/orkestrasyon ve icra·araştırma **zaten ayrılmış** (Jarvis ana-sıra + Atlas/işçi alt-ajanları). Ayrılmamış tek **D** satırı: **hakem/değerlendirici**.

### Seçenek 1 — Kalıcı, bağlam paylaşmayan hakem ajanı *(öneri)*

- **Ne demek:** Üretici koşumdan **önce** hiçbir bağlam görmeyen, ayrı tanımlı, salt-okur bir hakem ajanı; emri yazanın beklentisi kendisine verilmez (maskeli), yalnız çıktı + ham kaynaklar verilir.
- **Ne yaparım:** `.claude/agents/` altında hakem tanımı (`tools: Read, Grep, Glob, WebFetch`, yazma yok, `model` risk eksenine göre); emir şablonuna "beklenti maskesi" satırı; `cc/rapor/` çıktı şeması sabit; V26 sondajı hakem girdisine zorunlu bağlanır.
- **Artı:** Tek **D** etiketli, iki bağımsız güncel-kuşak kaynakla (`[H1]` Cognition 2026-04-22 + `[H2]` Claude Code belgesi 2026-09-18) desteklenen boşluk. Ölçülmüş getiri var: 2 hata/PR, %58 şiddetli. Yazma yetkisi yok → geri-alınamaz iş riski sıfır. Bu koşumun kendisi mekanizmanın çalıştığının kanıtı: maskeli hakem 48 iddiadan 7'sini düşürdü, 8'ini daralttı.
- **Eksi:** Ek token (Anthropic ölçümü: çok-ajan ≈15× sohbet); hakem kendi kaynak-eşleşme hatasını yapabilir (bu koşumda antitez raporlarının 5'i `TUTMADI` aldı) → V26 sondajı zorunlu kalır, yani maliyet iki katmanlı.

### Seçenek 2 — Ayrı ajan değil, aynı ajanda "temiz-bağlam hakem turu"

- **Ne demek:** Ayrı ajan tanımı yok; üretici ajan işini bitirince bağlamı sıfırlanmış yeni bir tur açılır ve yalnız çıktı + kaynaklar yüklenir.
- **Ne yaparım:** `seans-kapanis`/skill akışına "hakem turu" adımı eklenir; ayrı ajan dosyası, ayrı model, ayrı yetki yok.
- **Artı:** En ucuz; yeni kanon dosyası gerektirmez; `[H1]` gerekçesinin özünü (önceden bağlam paylaşmamak) kısmen sağlar.
- **Eksi:** `yapan≠ölçen` yalnız **usul** düzeyinde sağlanır, **yetki** düzeyinde değil — aynı ajan hem yazma yetkili hem hakem; maske gerçek değil beyan. Kanıt bu kurulumu ölçmüyor (Cognition ölçümü **ayrı ajan + paylaşılmamış bağlam** üzerinde).

### Seçenek 3 — Ertele, önce iç ölçüm koş

- **Ne demek:** Hüküm verilmez; (vi)'daki hakem-ölçümü (maskeli vs maskesiz hüküm dağılımı) koşulur, sonra karar.
- **Ne yaparım:** ≥10 kararlık A/B kurulur, `veri/` altına ölçüm hattı yazılır.
- **Artı:** Rakam Salih'in kendi verisinden gelir, dış kuşak farkı sorunu kalkar.
- **Eksi:** En güçlü kanıtlı (**D**) satırın icrasını geciktirir; ölçümün kendisi hakem ajanını zaten gerektiriyor (döngüsel).

**Öneri:** Seçenek 1. Gerekçe: (i) tablosunda **AYRILMALI + D** olup henüz ayrılmamış tek perspektif; iki bağımsız güncel-kuşak kaynak eşiğini geçen tek boşluk; yazma yetkisi olmadığı için geri-alınamaz iş riski taşımıyor.

---

## Halüsinasyon Freni — İddia Etiketleri

| İddia | Etiket |
|---|---|
| Hakem/değerlendirici ayrı bağlam gerektirir (yapan≠ölçen) | **DESTEKLİ** (2 güncel + 2 eski kaynak, D) |
| Gözetim/orkestrasyon ayrı ajan gerektirir | **DESTEKLİ** (2 güncel, D) |
| Paralel-yazan kod ajanı çalışmaz (paylaşılan bağlamda) | **DESTEKLİ** (2 güncel, D) |
| Alt-ajan = izole bağlam + tek dönüş kanalı + kısıtlanabilir yetki | **DESTEKLİ** (birincil belge, D) |
| "İşçiler ucuz model" | **DESTEKLİ** (güncel, D) |
| "En güçlü model yalnız orkestratör" | **ÇELİŞİR** (eski kuşakta ölçülü; güncel kuşak pratiği ters yönde) |
| "Kalıcı liderler orta model" | **DAYANAKSIZ** (X, hiçbir kaynak) |
| Antitez/red-team ayrı kalıcı ajan sınıfıdır | **DAYANAKSIZ** tasarım girdisi olarak (tek kaynak AS-OF'suz + model damgasız, K) |
| Planlama ayrı ajana çıkarılmalı | **DAYANAKSIZ** (gerekçe hiçbir birincil kaynakta verilmemiş; sayısal destek X'e düştü) |
| Tutor ayrı ajan sınıfıdır | **DAYANAKSIZ** tasarım girdisi olarak (model-sürümsüz kaynak, K; karşı-kanıt D) |
| Alt-ajanlar birbirinin belleğini göremez ("by design" alıntısı) | **DAYANAKSIZ** (alıntı belgede yok, X) |
| Ephemeral Cognition / TDP %82 / Routine %41→96 | **DAYANAKSIZ** (X, kaynak-eşleşme hatası) |

---

**Kaynak açma bilançosu:** hakem kendi sondajı 3 WebFetch (kota 8'in altında); geri kalan tüm hükümler verilen 9 rapor + V26 denetimi üzerinden. Repo'nun başka dosyası okunmadı.
