# Tez F1 — Claude Code Subagent (.claude/agents/*.md) Resmî Sözleşmesi

**AS-OF 2026-09-17, canlı** — kaynaklar https://code.claude.com/docs/en/sub-agents ve https://code.claude.com/docs/en/hooks üzerinden WebFetch ile canlı çekildi; sayfa içeriği zaman içinde değişebilir.

**Yöntem notu:** WebFetch aracı sayfayı ham HTML olarak değil, işlenmiş/özetlenmiş metin olarak döndürüyor. Aşağıdaki alıntılar bu işlenmiş çıktıdan alınmıştır; sayfanın birebir ham metniyle karakter-karakter eşleştiği doğrulanamaz (araç sınırlaması). Bu nedenle yapısal/olgusal iddialar D, alıntı-birebirliği garanti edilemeyen ama içerik doğrulanan yerler D (belirtilen ihtiyatla) olarak işaretlendi.

## İddialar

**İ1 — Frontmatter alan listesi**
D · https://code.claude.com/docs/en/sub-agents · "name, description... tools, disallowedTools, model, effort, permissionMode" (Frontmatter Fields Reference tablosu)
Zorunlu: `name`, `description`. Opsiyonel: `tools`, `disallowedTools`, `model`, `effort`, `permissionMode`, `maxTurns`, `skills`, `mcpServers`, `hooks`, `memory`, `background`, `isolation`, `color`, `initialPrompt`, `omitClaudeMd`, `experimental`.

**İ2 — `name` alanı kısıtı**
D · https://code.claude.com/docs/en/sub-agents · "Cannot contain `:` (reserved for plugin-scoped identifiers)"
Küçük harf + tire; `:` yasak (plugin-kapsam öneki için ayrılmış).

**İ3 — `description` token bütçesi ve amaç**
D · https://code.claude.com/docs/en/sub-agents · "descriptions count toward the 15,000-token limit"
Tüm alt-ajan `description` alanları toplamda 15.000 token sınırına dahil; aşınca başlangıç uyarısı çıkar ama yükleme devam eder.

**İ4 — Otomatik tetiklenme mekanizması**
D · https://code.claude.com/docs/en/sub-agents · "Claude automatically delegates based on... description field"
Ana model, kullanıcı isteğinin görev tanımını alt-ajanın `description` metniyle ve mevcut bağlamla eşleştirerek otomatik devretmeye karar verir.

**İ5 — "use proactively" kalıbı**
D · https://code.claude.com/docs/en/sub-agents · "Include phrases like 'use proactively' to encourage automatic delegation"
Örnek: `description: ... Use proactively after code changes.` — bu kalıp otomatik/proaktif çağrılma olasılığını artırır (garanti değil, teşvik).

**İ6 — `tools`/`disallowedTools` sırası**
D · https://code.claude.com/docs/en/sub-agents · "disallowedTools removing... Applied before tools resolution"
`disallowedTools`, `tools` çözümlemesinden önce uygulanır; miras alınan ya da belirtilen listeden çıkarır.

**İ7 — `model` alanı değerleri**
D · https://code.claude.com/docs/en/sub-agents · "sonnet, opus, haiku, fable, full ID... or inherit"
Kısayol adı, tam model ID'si ya da `inherit` (üst oturumun modelini seçer) kabul edilir.

**İ8 — Model çözümleme sırası**
D · https://code.claude.com/docs/en/sub-agents · "Per-invocation model parameter (highest priority)"
Sıra: (1) çağrı-anı `model` parametresi, (2) alt-ajan frontmatter `model`, (3) `CLAUDE_CODE_SUBAGENT_MODEL` ortam değişkeni, (4) ana oturumun modeli.

**İ9 — Explore/Plan model tavanı**
D · https://code.claude.com/docs/en/sub-agents · "Explore: inherits parent model, capped at Opus"
`Explore` üst modeli miras alır ama Claude API'de Opus ile sınırlanır; `Plan` sınırsız miras alır.

**İ10 — `effort` alanı kapsamı**
D · https://code.claude.com/docs/en/sub-agents · "overrides the session's effort level... when that subagent is active"
`effort` yalnız o alt-ajan aktifken oturum effort seviyesini geçersiz kılar; ana konuşmayı ya da diğer alt-ajanları etkilemez.

**İ11 — `skills` alanı davranışı**
D · https://code.claude.com/docs/en/sub-agents · "Full skill content injected (not just description)"
Listelenen skill'lerin tam içeriği (yalnız açıklaması değil) başlangıçta bağlama enjekte edilir.

**İ12 — `memory` alanı kapsamları**
D · https://code.claude.com/docs/en/sub-agents · "user (~/.claude/agent-memory/), project (.claude/agent-memory/), or local"
Üç seçenek: `user`, `project`, `local` (`.claude/agent-memory-local/`); kalıcı hafıza konumunu belirler.

**İ13 — `hooks` alanı kapsamı**
D · https://code.claude.com/docs/en/sub-agents · "Lifecycle hooks... scoped to this subagent only"
Frontmatter içindeki `hooks` yalnız o alt-ajana özeldir; PreToolUse/PostToolUse/Stop tipleri desteklenir.

**İ14 — `color`, `background`, `isolation`, `initialPrompt`, `omitClaudeMd`, `experimental` alanları var mı**
D · https://code.claude.com/docs/en/sub-agents · tam örnek bloklarda (Complete Example) hepsi listelendi
Var: `color` (8 sabit renk), `background: true/false`, `isolation: worktree`, `initialPrompt` (yalnız `--agent`/ana oturum modunda), `omitClaudeMd: true` (yönetilen politika dosyaları yine yüklenir), `experimental.cacheTtl` (prompt cache ömrü, örn. `5m`/`1h`).

**İ15 — Alt-ajan ana konuşma geçmişini görmez**
D · https://code.claude.com/docs/en/sub-agents · "Conversation history ❌ No — only the delegation prompt Claude writes"
Fork olmayan alt-ajanlar taze/izole bağlamla başlar; önceki mesajları değil yalnız devretme (delegation) istemini görür.

**İ16 — CLAUDE.md yüklenir mi**
D · https://code.claude.com/docs/en/sub-agents · "CLAUDE.md files ✅ Yes (except Explore/Plan)... omitClaudeMd: true to skip"
`~/.claude/CLAUDE.md`, proje CLAUDE.md, `CLAUDE.local.md` tam hiyerarşiyle yüklenir (Explore/Plan hariç); `omitClaudeMd: true` ile atlanabilir ama yönetilen politika dosyaları yine yüklenir.

**İ17 — Claude Code sistem promptu alt-ajana geçmez**
D · https://code.claude.com/docs/en/sub-agents · "Subagent's own markdown body... NOT the Claude Code system prompt"
Alt-ajanın sistem promptu yalnız kendi markdown gövdesi + ortam bilgisidir; ana Claude Code sistem promptu miras alınmaz.

**İ18 — Auto memory ve output style miras alınmaz**
D · https://code.claude.com/docs/en/sub-agents · "Output style ❌ No... Auto memory ❌ No"
Alt-ajan kendi sistem promptuyla çalışır (üst oturumun output style'ını yok sayar); üst oturumun otomatik hafızası yüklenmez.

**İ19 — Fork istisnası**
D · https://code.claude.com/docs/en/sub-agents · "Forks inherit the entire parent conversation including history, tools, and output style"
Fork tipi alt-ajanlar taze başlamaz; tüm üst konuşmayı (geçmiş, araçlar, output style) miras alır — İ15-İ18'in tersi.

**İ20 — SubagentStart/SubagentStop olayları ve matcher**
D · https://code.claude.com/docs/en/hooks · "SubagentStart | When a subagent is spawned" / "SubagentStop | When a subagent finishes"
İki olay da `agent_type` alanına göre eşleşme (matcher) filtrelenebilir (örn. `"Explore"`, `"Plan"`, özel ad, ya da plugin-kapsamlı `^my-plugin:reviewer$`).

**İ21 — Hook JSON'da agent_id/agent_type alanları**
D · https://code.claude.com/docs/en/hooks · "agent_id — Unique identifier... agent_type — Agent name"
`agent_id`: alt-ajan çağrısı içindeyken var olan benzersiz kimlik; `agent_type`: ajan adı (örn. `"Explore"`, `"security-reviewer"`); yalnız `--agent` kullanımında ya da alt-ajan içindeyken bu alanlar mevcut.

**İ22 — Alt-ajan içindeki araç olayları da agent_id/agent_type taşır**
D · https://code.claude.com/docs/en/hooks · "tool events... carry the agent_id and agent_type common input fields"
Alt-ajan bir araç çağırdığında `PreToolUse`/`PostToolUse`/`PostToolUseFailure`/`PermissionRequest`/`PermissionDenied` olayları da aynı ortak alanlarla (`agent_id`, `agent_type`) tetiklenir.

**İ23 — Sistem promptu gövdesi için resmî uzunluk tavsiyesi**
K · https://code.claude.com/docs/en/sub-agents · "No official length limit... consider: longer prompts consume subagent context"
Belge kesin bir uzunluk sınırı vermiyor; yalnız nitel öneri sunuyor (rol tanımıyla başla, çıktı biçimini belirt, kısıtları yaz, ayrıntılı prosedürleri `skills` alanına taşı). Bu iddiayı K (kısmen doğrulandı) işaretliyorum çünkü "resmî tavsiye" istenen ama somut sayısal eşik yok — yalnız yönerge var.

**İ24 — Açık tetikleme yöntemleri**
D · https://code.claude.com/docs/en/sub-agents · "@-mention guarantees that subagent runs" / "--agent code-reviewer"
Üç yol: doğal dil (Claude karar verir), `@"ad (agent)"` ile garanti çağrı, `--agent <ad>` veya settings'te `"agent"` ile oturum-geneli.

**İ25 — Alt-ajanlardan her zaman kaldırılan araçlar**
D · https://code.claude.com/docs/en/sub-agents · "Agent (at depth limit), AskUserQuestion, EndConversation..."
Derinlik sınırında `Agent`, ayrıca `AskUserQuestion`, `EndConversation`, `EnterPlanMode`, `ExitPlanMode` (permissionMode:plan hariç), `ScheduleWakeup`, `TaskOutput`, `WaitForMcpServers`, `Workflow` her zaman kaldırılır.

## Doğrulanamayan / bulunamayan noktalar
- Sayfanın ham HTML/markdown kaynağı doğrudan görülmedi; alıntılar WebFetch'in işlenmiş çıktısından alındı — birebir karakter eşleşmesi garanti edilmez (yöntem notuna bakınız).
- "resmî sözleşme" ifadesinin bir spesifikasyon/şema dosyası (JSON Schema vb.) olarak yayınlanıp yayınlanmadığı bu koşumda ayrıca aranmadı (bütçe dışı kaldı) — X.
- 403/erişim engeli yaşanmadı; her iki sayfa da başarıyla döndü.

## Jarvis için sonuç
1. Depodaki `.claude/agents/*.md` dosyaları frontmatter'da `skills`, `memory`, `hooks`, `omitClaudeMd`, `isolation` gibi alanları kullanabiliyorsa bunlar resmî olarak desteklenir (İ1, İ11-İ14) — atlas.md ve benzerlerinde bu alanlar denetlenebilir.
2. Alt-ajanlar Jarvis'in konuşma geçmişini, CLAUDE.md hariç auto-memory'sini ve output style'ını görmez (İ15, İ18) — "ajan bağımsız çalışır, başka ajan çıktısı görmez" talimatı resmî davranışla örtüşüyor.
3. CLAUDE.md tam hiyerarşisi (kullanıcı + proje + local) alt-ajana varsayılan olarak yüklenir (İ16) — bu, "bağımsız çalış" talimatının Salih'in global CLAUDE.md kuralları hâlâ geçerli anlamına geldiğini gösterir; `omitClaudeMd` açıkça set edilmedikçe.
4. `description` alanı 15.000 token toplam sınırına dahil (İ3) — depo genelinde çok sayıda alt-ajan eklenirse açıklama metinlerinin toplam uzunluğu izlenmeli.
5. Sistem promptu uzunluğu için sayısal resmî tavan yok (İ23, K) — depo bütçe kuralları (örn. CLAUDE.md ≤80 satır) kendi iç kararımız, Anthropic zorunluluğu değil.
