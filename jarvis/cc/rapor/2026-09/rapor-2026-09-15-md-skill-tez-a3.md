# Tez A3 — md→skill atlas koşumu (2026-09-15, Sonnet işçi, AS-OF 2026-09-15)

# TEZ Raporu — Skill'ler: Deterministik ve Denetlenebilir İcra (Aile A3)

## (1) Script'lerin rolü, frontmatter, yürütme sözleşmesi

Anthropic'in resmi "Skill authoring best practices" sayfası (platform.claude.com, AS-OF 2026-09-15, doğrudan WebFetch ile okundu) "Advanced: Skills with executable code" başlığı altında script'lerin rolünü açıkça "Prefer scripts for deterministic operations: Write `validate_form.py` rather than asking Claude to generate validation code" diye tanımlıyor. Üç serbestlik derecesi (high/medium/low freedom) tanımlanıyor: low-freedom = "Run exactly this script... Do not modify"; bu, deterministik adımların betiğe kilitlenmesinin resmi gerekçesi. Ayrıca "Solve, don't defer" ilkesi (hata koşullarını script içinde ele al, Claude'a bırakma) ve "voodoo constants" (Ousterhout) karşıtlığı, "plan-validate-execute" deseni (structured plan dosyası → script ile doğrula → uygula → verify) auditability'yi artıran somut pratikler. Script "execute" (çalıştır) vs "read as reference" (oku) ayrımı açıkça talimat metninde belirtilmeli deniyor.

Frontmatter zorunlu alanlar yalnız `name` ve `description` (resmi Agent Skills spesifikasyonu, aynı sayfa). `disable-model-invocation`, `allowed-tools`, `context: fork`, `model`, `agent`, `user-invocable`, `disallowed-tools`, `paths` gibi alanlar Claude Code'a özgü genişletmeler — bunlar code.claude.com/docs/en/skills sayfasından WebFetch özetiyle geldi (bu fetch ham metin değil, küçük-model özetiydi; bir yerinde yazım hatası fark ettim ("derε"), bu yüzden tam alan-listesi ve syntax detayları için [?] işaretliyorum, doğrulama tam sayfa okuması gerektirir). Genel doğrulanabilir bulgu: `disable-model-invocation:true` skill'i Claude'un otomatik çağırmasını engelleyip yalnız `/skill-adı` ile kullanıcı-tetikli hale getiriyor (GitHub issue #43809 başlığından da teyitli — "Skills with disable-model-invocation: true cannot be invoked by subagents"), `allowed-tools` ise skill aktifken araçlara ön-onay veriyor ama başka araçları engellemiyor (deny-rule ile eşleştirilmesi gerekiyor).

## (2) Girdi/çıktı şeması ve workflow-tipi skill'ler

Resmi belge yapılandırılmış JSON şema/tipini SKILL.md içinde zorunlu kılan bir mekanizma TANIMLAMIYOR — bunun yerine "Template pattern" (çıktı formatı için serbest-metin şablon, "ALWAYS use this exact template structure") ve "Create verifiable intermediate outputs" deseni var: ara çıktı bir dosyaya (`changes.json` örneği) yazılır, script ile validate edilir, sonra uygulanır. Yani "workflow tipi" skill kavramı resmi belgede yoktu; onun yerine "Workflows and feedback loops" bölümü var — checklist + validator-fix-repeat döngüsü. Skill vs hooks/agents/workflow farkı (Claude Code tarafı, [?] işaretli özet): hooks = event-tabanlı deterministik handler (otomatik, skill'in parçası değil); subagent/agent = izole context + kendi izin seti; workflow = birden çok skill'i sıralı çağıran, state paylaşan kullanıcı-tanımlı orkestrasyon; skill'in kendisi varsayılan olarak inline (paylaşılan konuşma bağlamında) çalışıyor, `context: fork` ile izole subagent bağlamına geçiyor — determinizm asıl hooks'ta (otomatik/olay-güdümlü, model kararına bağlı değil) ve script yürütmede (kod = deterministik), skill metninin kendisi hâlâ model-yorumlu.

## (3) Ölçüm / benchmark / skill-doctor / npx skills

Anthropic'in `skill-creator` SKILL.md'si (raw.githubusercontent.com/anthropics/skills, AS-OF 2026-09-15, doğrudan WebFetch ile okundu) 4 modlu bir döngü tanımlıyor: Create → Eval → Improve → Benchmark; "with_skill" vs "baseline" paralel test, dört alt-ajan (Executor/Grader/Comparator/Analyzer), "variance analizi: assertion tutarlılığı, yüksek varyans evallerini tespit et" açıkça yazılı — yani run-to-run variance ölçümü VAR ama resmi belgede sayısal/yayınlanmış bir "skill kullanımı X% varyansı azaltır" rakamı GÖRMEDİM (WebSearch sonuçlarında da yok). Resmi best-practices sayfası da net: "There is not currently a built-in way to run these evaluations" — yani standart, yayınlanmış bir tutarlılık-benchmarkı Anthropic tarafında YOK, kullanıcı kendi eval sistemini kurmalı.

WebSearch'te bulunan (fetch edilmedi, ikincil kaynak, flag: doğrulanmamış) "SkillsBench" (84 görev, 11+ alan, deterministik verifier, LLM-judge yok) bir benchmark olarak anılıyor ancak resmi Anthropic belgesi/repo'suyla doğrudan teyit edemedim — kaynak sayfası açılmadı, [?].

Warp `skill-doctor` (docs.warp.dev, WebSearch özeti, doğrudan açılmadı — [?]): geçmiş ajan konuşmalarını (Claude Code/Codex/Warp) tarayıp verimlilik + kod-kalitesi rubriğiyle puanlıyor, skill'lere somut diff öneriyor; yerel çalışıyor, transkript yüklemiyor. Kurulum: `npx skills add https://github.com/warpdotdev/common-skills --skill skill-doctor`.

Vercel `npx skills` (vercel-labs/skills, WebSearch özeti, doğrudan açılmadı — [?]): GitHub-tabanlı skill registry/paket-yöneticisi (`npx skills find`, `npx skills add`), skills.sh dizin+leaderboard; herhangi bir SKILL.md içeren public repo geçerli kaynak.

## (4) "Skill'i skill'den üretme" akışı

Resmi belge iki yol tanımlıyor: (a) skill-creator SKILL.md'sindeki "Transkript/MD'den Skill Üretme" — konuşma geçmişinden yanıt çıkarma → boşluk doldurma → taslak SKILL.md → bundled resources organizasyonu; (b) best-practices sayfasındaki "Develop Skills iteratively with Claude" — Claude A (yazar) + Claude B (test-kullanıcı) döngüsü: görevi skill'siz yap → tekrar eden bağlamı tanı → Claude A'dan skill üretmesini iste → conciseness/bilgi-mimarisi incele → Claude B ile test et → gözlemle geri dön. Kalite kapısı olarak resmi checklist var (açıklama spesifik mi, 500 satır altı mı, en az 3 eval, Haiku/Sonnet/Opus ile test) ama otomatik/zorunlu bir "kapı" script'i resmi belgede tanımlı değil — skill-creator'ın kendi eval pipeline'ı (assertion pass/fail, grading.json) en yakın somut kalite-kapısı örneği.

## İDDİA LİSTESİ

1. Resmi Anthropic belgesi, deterministik/kırılgan işlemler için script yazmayı ("low freedom") açıkça tavsiye ediyor (platform.claude.com/.../best-practices, AS-OF 2026-09-15).
2. SKILL.md zorunlu frontmatter alanları yalnızca `name` ve `description`'dır (aynı kaynak).
3. `disable-model-invocation:true` skill'in otomatik model-tetiklemesini engelleyip yalnız kullanıcı-komutuyla çalışmasını sağlar (GitHub issue #43809 başlığı + WebSearch özeti).
4. `allowed-tools` skill aktifken araç ön-onayı verir ama başka araçları bloklamaz (WebSearch özeti).
5. Resmi belge, "plan-validate-execute" desenini hata-erken-yakalama/denetlenebilirlik için önerir (aynı kaynak, doğrudan okunmuş metin).
6. Resmi belgede şu an yerleşik/otomatik bir eval çalıştırma mekanizması yoktur; kullanıcı kendi sistemini kurar (aynı kaynak, alıntı: "There is not currently a built-in way").
7. skill-creator'ın eval pipeline'ı Executor/Grader/Comparator/Analyzer dört alt-ajanla ve "with_skill vs baseline" paralel karşılaştırmayla çalışır (raw.githubusercontent.com/anthropics/skills SKILL.md, AS-OF 2026-09-15).
8. skill-creator yüksek-varyanslı ("flaky") assertion'ları tespit eden bir varyans-analizi adımı içerir, ama yayınlanmış sayısal bir tutarlılık-artışı rakamı bulunamadı [?].
9. Warp skill-doctor geçmiş ajan transkriptlerini yerel olarak puanlayıp skill diff'i önerir; iddia ikincil kaynağa (WebSearch özeti) dayanır, doğrudan sayfa açılmadı [?].
10. Vercel `npx skills` GitHub-tabanlı açık bir skill paket-yöneticisi/registry'sidir; iddia ikincil kaynağa dayanır, doğrudan sayfa açılmadı [?].
11. "SkillsBench" adlı 84 görevlik deterministik-verifier benchmark WebSearch sonuçlarında anıldı ama kaynağı doğrudan doğrulanmadı [?].
12. Claude Code'a özgü `context: fork`, `agent:`, `paths:`, `user-invocable` alanlarının tam syntax ve davranışı yalnız özetlenmiş bir WebFetch'ten geldi, ham sayfa metniyle teyit edilmedi [?].
