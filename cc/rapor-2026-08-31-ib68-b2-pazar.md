# Pazar-Doğrulama Taraması — B68-2 / B68-6 / B68-3

**Künye:** AS-OF 2026-08-31 · aile B2 · model sonnet · rejim maliyet-öncelikli · 12 web araması, WebFetch açılmadı (yalnız arama-sonucu snippet'leri; "birincil kaynak" denmiyor).
**Uyarı:** Aşağıdaki hiçbir satırda tahmini fiyat/gelir rakamı YOK. Ücretli plan yalnız VAR/YOK olarak işaretli. Tüm URL'ler arama motoru sonuçlarından; açılıp doğrulanmadı → içerik ikinci-el özet, DAYANAKSIZ olabilir.

---

## B68-2 — Paralel-kapı + manifest rejimi (eşzamanlılık kapısı, Bernstein koşulu, worktree)

**Aramalar (3):**
1. "multi-agent coding orchestration tool Conductor Crystal Claude Squad git worktree manager"
2. "merge conflict prevention AI coding agents parallel file lock lease service 2026"
3. "Bazel Nx sandbox dependency declaration build system agent parallelism"

**Rakip listesi:**
| Ad | Ne yapıyor | URL | Not |
|---|---|---|---|
| Conductor (Melty Labs, YC S24) | macOS uygulaması, her ajanı ayrı git worktree'de paralel koşturur; checkpoint/rollback, çoklu-model karşılaştırma | https://madewithlove.com/blog/conductor-running-multiple-ai-coding-agents-in-parallel/ | ikinci-el özet |
| Claude Squad | açık kaynak, tmux + git worktree, terminal-native TUI, her göreve izole çalışma alanı | (arama snippet'i, doğrudan repo URL'i açılmadı) | [?] repo adresi teyitsiz |
| Crystal (Stravu) | paralel Codex/Claude Code worktree yöneticisi masaüstü app — **2026-02'de DEPRECATED**, kullanıcılar Nimbalyst'e yönlendirilmiş | https://nimbalyst.com/blog/best-tools-for-running-parallel-ai-coding-agents/ | pazar sinyali: kapanış = negatif sinyal |
| Nimbalyst | Crystal'ın genişletilmiş hâli; paralel oturum + görsel düzenleme (markdown/mockup/Excalidraw) | https://nimbalyst.com/blog/best-agent-management-tools-2026/ | ikinci-el özet |
| vibe-kanban | görev-panosu tarzı orkestrasyon (arama sonucunda adı geçti, detay yok) | — | [?] doğrulanmadı |
| agentree | her ajan oturumu için otomatik git worktree oluşturan araç | https://www.termdock.com/en/blog/git-worktree-conflicts-ai-agents | ikinci-el özet |
| Nx (task sandboxing) | 22.7 sürümünde gerçek dosya I/O'yu izleyip deklare edilenle karşılaştıran "task sandboxing"; deklare-dışı okuma/yazmayı ihlal olarak işaretliyor | https://nx.dev/blog/nx-22-7-release | **doğrudan Bernstein-benzeri kapı** — en yakın kavramsal rakip |
| Bazel | BUILD dosyasında deklare girdi/çıktı, hermetik sandbox, DAG tabanlı maksimum paralellik | https://www.gocodeo.com/post/how-bazel-works-dependency-graphs-caching-and-remote-execution | build-sistemi, ajan-spesifik değil |
| "AI mutex lock" deseni (blog, ürün değil) | lock-dosyası: sahip ajan, görev, base-commit SHA, expiration → lease benzeri | https://medium.com/@mustafa_16192/how-an-ai-mutex-lock-may-look-like-keeping-your-ai-agents-from-colliding-0bdce18d3359 | ürün değil, kavram makalesi |

**Pazar sinyali:** Conductor ücretli plan VAR (Pro/Teams/Enterprise katmanları arama snippet'inde geçti — rakam yazılmadı, yalnız varlık); ayrıca "app ücretsiz, yalnız API maliyeti" diyen çelişen kaynak da var → **ÇELİŞİR**, tek kaynaktan teyit edilmedi. Claude Squad/agentree açık-kaynak, ödeme kanıtı YOK → sinyalsiz. Crystal kapandı → negatif sinyal (talep sürdürülemedi ya da konsolidasyon). Nx task-sandboxing kurumsal üründe (Nx Cloud) gömülü — bağımsız fiyat sayfası aranmadı, [?].

**Rekabet yoğunluğu:** ORTA — worktree-tabanlı "paralel ajan çalıştırma" katmanında çok sayıda araç (Conductor/Claude Squad/Crystal-Nimbalyst/agentree/vibe-kanban) var; ancak B68-2'nin özgül iddiası olan **deklaratif dosya-beyanı + Bernstein çift-çift hüküm + deterministik dalga planı** hiçbir rakipte bire-bir görülmedi — en yakını Nx'in çalışma-zamanı I/O izleme + ihlal bayrağı (deklare-önce değil, deklare-sonra doğrulama) ve Bazel'in build-zamanı statik deklarasyonu.

**Etiket:** "Rakip yoğun ama mekanizma-eşleşmesi seyrek" → **DAYANAKSIZ** olarak iddia edilemez ki B68-2 bire-bir kopya olsun; kalabalık pazarda **konumlandırma farkı DESTEKLİ** (Nx/Bazel örneklerinden), ama "kimse yapmıyor" iddiası DAYANAKSIZ (worktree-izolasyon çok yaygın, sadece kapı-mekanizması farklı). `[?]` vibe-kanban ve Claude Squad repo adresleri ile yıldız sayıları doğrulanmadı.

---

## B68-6 — Repo-freni paketi (policy-as-code, hook tabanlı deny/ask)

**Aramalar (3):**
1. "AI agent guardrails product Invariant Labs Lakera NeMo Guardrails Guardrails AI pricing"
2. "Claude Code hooks policy deny list block tool call before execution ecosystem"
3. "OPA Conftest policy as code AI agent permission sandbox product 2026"

**Rakip listesi:**
| Ad | Ne yapıyor | URL | Not |
|---|---|---|---|
| Invariant Labs — Guardrails | LLM/MCP trafiği için kural-tabanlı korumalı katman, MCP sunucu tarama, "tool poisoning"/"rug pull" tespiti | https://invariantlabs.ai/guardrails | **2025-06'da Snyk tarafından SATIN ALINDI** — bağımsız ürün olarak kapandı/entegre oldu, güçlü sinyal (M&A çıkışı) |
| NVIDIA NeMo Guardrails | açık kaynak, Colang DSL ile 6 tip koruma, proxy mikroservis | (arama snippet, URL doğrudan açılmadı) | ödeme kanıtı YOK (açık kaynak, compute-only) → sinyalsiz |
| Guardrails AI | açık kaynak Python, RAIL + Pydantic ile çıktı doğrulama | (arama snippet) | sinyalsiz (açık kaynak) |
| Lakera Guard | ticari API, prompt-injection tespiti, katmanlı fiyatlandırma | https://veto.so/compare/ai-guardrails | ücretli plan VAR (katman var, rakam yok) |
| OPA / Conftest | politika-motoru, IaC/config test; ajan bağlamında "tool-calling katmanında OPA karar verir" deseni yaygınlaşıyor | https://codilime.com/blog/why-use-open-policy-agent-for-your-ai-agents/ | açık kaynak (CNCF), ödeme kanıtı YOK doğrudan; entegre ürünler (Strata Maverics) ücretli olabilir [?] |
| Strata Maverics AI Identity Gateway | gömülü OPA motoruyla MCP tool-call'larına ince-taneli politika | https://codilime.com/blog/why-use-open-policy-agent-for-your-ai-agents/ | [?] fiyat sayfası doğrulanmadı |
| Claude Code PreToolUse hook ekosistemi | regex/JSON tabanlı deny/ask/allow kararı, tool çalışmadan önce; 30 lifecycle event | https://code.claude.com/docs/en/hooks | Anthropic'in kendi ürünü — **B68-6'nın koştuğu platform, aynı zamanda potansiyel "yerleşik alternatif"** |

**Pazar sinyali:** Bu alan DOYGUN ve konsolide oluyor — Invariant Labs'ın Snyk'e satılması (kurulduktan <1 yıl sonra) güvenlik büyük oyuncularının bu kategoriyi satın-alarak kapattığının işareti. Lakera ücretli API kanıtlı. OPA/Conftest altyapı-katmanı olarak zaten CNCF standardı; "AI agent guardrails" spesifik ürünleri (Galileo, General Analysis, Fastio, futureagi gibi karşılaştırma-blogları) 2026'da çoğaldı → kategori ilgisi yüksek ama isim çeşitliliği de blog-SEO şişkinliği olabilir, [?].

**Rekabet yoğunluğu:** DOYGUN — hem kurumsal (Lakera, NeMo, Snyk/Invariant), hem açık-kaynak (OPA, Guardrails AI), hem de platform-gömülü (Claude Code hooks'un kendisi) çok sayıda dolgu var. B68-6'nın "hook + Türkçe/basit regex deny-ask listesi, repoya-özgü" konumlandırması bunların hepsinden DAHA DAR-KAPSAMLI ve kod-tabanına-gömülü; genel guardrail ürünleri LLM-çıktı/prompt-injection odaklı, B68-6 ise **araç-çağrısı-öncesi tool-call engelleme** — Claude Code'un kendi hook sistemiyle örtüşüyor (rakip değil, alt-katman).

**Etiket:** "Rakip yok" iddiası **ÇELİŞİR** (alan doygun); "Türkçe/repo-özel basit deny-ask + hook" spesifik bileşimi için doğrudan eşleşen ürün bulunamadı → o dar tanım DESTEKLİ ama kategori genel olarak doygun. `[?]` Claude Code hooks ekosisteminde üçüncü-parti "paket" (hazır deny-list kütüphanesi) olup olmadığı ayrıca aranmadı.

---

## B68-3 — Karar-masası deseni (insan-hüküm onay kuyruğu, kart-kart)

**Aramalar (3):**
1. "human-in-the-loop AI agent approval inbox HumanLayer pricing"
2. "Langfuse annotation queue Label Studio agent approval workflow review"
3. "agentic workflow human approval signal Temporal n8n Retool AI agent 2026"

**Rakip listesi:**
| Ad | Ne yapıyor | URL | Not |
|---|---|---|---|
| HumanLayer (YC F24) | ajanların hassas araç çağrısı öncesi insana Slack/Email/Discord üzerinden onay sorması; escalation, timeout, öğrenen auto-approve | https://humanlayer.systems/index-en.html | ücretli plan VAR (Starter ücretsiz 1000 op/ay + Premium/Enterprise — rakam yok) |
| Langfuse Annotation Queues | trace/session seviyesinde toplu insan değerlendirme kuyruğu, public API | https://langfuse.com/docs/evaluation/evaluation-methods/annotation-queues | değerlendirme-odaklı, "onay" değil "etiketleme/skorlama" — kısmi örtüşme |
| Label Studio (+ Langfuse entegrasyonu) | uzman-incelemeli, turn-by-turn trace review arayüzü | https://labelstud.io/integrations/ai-evaluation/langfuse/ | Enterprise sürüm ücretli (varlık VAR) |
| n8n AI Agent "Require approval" | 2.6 sürümünden itibaren araç bazında yerleşik onay adımı; Telegram/Slack/Gmail bildirimi | https://www.triggerworkflow.com/2026/08/n8n-human-in-the-loop-approval-guide.html | platform-gömülü özellik, bağımsız ürün değil |
| Temporal Signals (human-in-the-loop) | durable workflow'da Python signal ile insan onayı bekletme deseni | https://docs.temporal.io/ai-cookbook/human-in-the-loop-python | altyapı-parçası, kart-arayüzü sağlamıyor |
| Retool | Google agent-to-agent protokolüyle anıldı, onay-arayüzü detayı bulunamadı | — | [?] doğrulanmadı |

**Pazar sinyali:** HumanLayer — YC F24, seed-aşaması finansman aldığı ve 2025 gelirinin olduğu bildiriliyor (rakam bilerek yazılmıyor, kaynak ikinci-el/Latka — DAYANAKSIZ sayılabilir, doğrudan Crunchbase/HumanLayer açılmadı); ücretli plan VAR. Bu, **B68-3'ün doğrudan-isim rakibi** — "ajan kararını insana sun, onayla/reddet" çekirdek deseni aynı. Langfuse/Label Studio farklı kullanım (LLM-çıktı değerlendirme/etiketleme, canlı-operasyon onayı değil). n8n'in gömülü onayı geniş-platform özelliği, agentic-repo'ya özgü değil.

**Rekabet yoğunluğu:** ORTA — HumanLayer net bir doğrudan-rakip (isim + fiyat + ürün tanımı üçü de eşleşiyor); geri kalanlar (Langfuse/Label Studio/n8n/Temporal) bitişik-kategori, tam örtüşmüyor. B68-3'ün "kart-kart, seçenek-açıklamalı, mükerrer-gönderim güvenli, agentic-repo kararları" spesifiği HumanLayer'ın "tool-call onayı" ile örtüşüyor ama B68-3 daha geniş kapsamlı (kod/tasarım kararları, salt araç-çağrısı değil) — konumlandırma farkı olabilir, doğrulanmadı.

**Etiket:** "HumanLayer doğrudan rakip" **DESTEKLİ** (isim+ürün+fiyat üçlü eşleşme, ikinci-el kaynaklardan). "Pazar sinyalsiz" iddiası bu aile için **ÇELİŞİR** — HumanLayer'ın ücretli planı ve YC finansmanı var. `[?]` HumanLayer'ın gerçek MRR/kullanıcı sayısı teyit edilmedi (kaynak: getlatka.com — bağımsız veri toplayıcı, birincil değil).

---

## Özet tablo

| Aile | Rekabet yoğunluğu | En yakın rakip | Sinyal |
|---|---|---|---|
| B68-2 (paralel-kapı) | ORTA | Nx task-sandboxing (I/O ihlal bayrağı) | Conductor ücretli VAR (çelişik kaynak), Crystal kapandı |
| B68-6 (repo-freni) | DOYGUN | Claude Code hooks (platform-içi), Lakera/NeMo/OPA | Invariant Labs Snyk'e satıldı (M&A çıkışı), Lakera ücretli VAR |
| B68-3 (karar-masası) | ORTA | HumanLayer (isim eşleşmesi güçlü) | HumanLayer ücretli VAR + YC finansman izi |

**Genel [?] listesi:** vibe-kanban ve Claude Squad repo/yıldız sayıları, Nx Cloud fiyat sayfası, Strata Maverics fiyatlandırma, Retool onay-arayüzü detayı, HumanLayer gerçek kullanıcı/gelir rakamları (ikinci-el kaynak) — hiçbiri birincil kaynaktan teyit edilmedi.
