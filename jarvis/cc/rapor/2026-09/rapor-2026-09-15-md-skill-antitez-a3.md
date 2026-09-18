# Antitez ¬A3 — md→skill atlas koşumu (2026-09-15, Sonnet, CoVe-Factored: yalnız iddia listesi verildi)

## ANTİTEZ Raporu — A3 (skill = kalıp-prompt, deterministik/denetlenebilir icra)

**AS-OF: 2026-09-15.** Birincil kaynaklar açıldı: code.claude.com/docs/en/skills, platform.claude.com/…/best-practices.

**1. "Deterministik/kırılgan işlemler için script tavsiyesi"** — ÇÜRÜTÜLEMEDİ. Best-practices sayfası açıkça "Low freedom… Use when: Operations are fragile and error-prone, consistency is critical" diyor ve "Prefer scripts for deterministic operations: Write `validate_form.py` rather than asking Claude to generate validation code" ekliyor. Tez doğrulandı, karşı kanıt yok.

**2. "Zorunlu frontmatter yalnız name+description"** — ÇÜRÜTÜLEMEDİ (platform.claude.com sayfası: "The SKILL.md frontmatter requires two fields: name… description…"). Ancak nüans: code.claude.com/docs/en/skills sayfası Claude Code'a özgü ek alanlar listeliyor (`disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `context`, `agent`, `background`, `paths`, `shell`) — bunlar *isteğe bağlı*, zorunluluk iddiasını bozmuyor ama "yalnız iki alan var" izlenimini tek doküman sınırlı bırakıyor (iki farklı ürün yüzeyi: platform API vs Claude Code).

**3. disable-model-invocation** — ÇÜRÜTÜLEMEDİ. Doküman: "Set to `true` to prevent Claude from automatically loading this skill. Use for workflows you want to trigger manually with `/name`." Örnekte deploy skill'i bu bayrakla veriliyor; gerekçe: "You don't want Claude deciding to deploy because your code looks ready." T doğru.

**4. allowed-tools önceden-onay verir, başka araç bloklamaz** — ÇÜRÜTÜLEMEDİ, dolaylı doğrulandı. Tanım: "Tools Claude can use without asking permission during the turn… The grant clears when you send your next message." Blokaj işlevi ayrı bir alana (`disallowed-tools`: "removed from Claude's available pool") atanmış — bu ayrım tezi destekliyor: allowed-tools yalnız izin, yasaklama değil.

**5. "plan-validate-execute" denetlenebilirlik için önerilir** — ÇÜRÜTÜLEMEDİ, güçlü kanıt bulundu. Best-practices: "The 'plan-validate-execute' pattern catches errors early by having Claude first create a plan in a structured format, then validate that plan with a script before executing it." Gerekçe listesi: "Catches errors early… Machine-verifiable… Clear debugging." Tam olarak denetlenebilirlik çerçevesinde sunuluyor.

**6. Yerleşik otomatik eval yok, kullanıcı kurar** — KISMEN ÇÜRÜTÜLDÜ [?]. Best-practices sayfası kelimesi kelimesine: "There is not currently a built-in way to run these evaluations. Users can create their own evaluation system." Platform seviyesinde doğru. Ama Anthropic'in kendi `skill-creator` eklentisi (anthropics/skills repo) tam otomatik dört-ajanlı eval hattı sağlıyor (bkz. madde 7) — yani "resmi" bir mekanizma VAR, sadece platformun çekirdeğine değil ayrı bir skill/plugin'e gömülü. Sınır: platform-native ≠ Anthropic-native.

**7. Executor/Grader/Comparator/Analyzer, with_skill vs baseline** — ÇÜRÜTÜLEMEDİ. WebSearch sonuçları (github.com/anthropics/skills, tessl.io blog) bu dört rolü ve "baseline is always without_skill" ifadesini doğruluyor. Ancak bu birincil kaynak WebFetch ile TEK TEK açılıp doğrulanmadı — arama motoru özeti [?], doğrudan GitHub dosyası okunmadı (bütçe kısıtı).

**8. Varyans-analizi var ama yayınlanmış sayısal tutarlılık-artışı rakamı yok** — KISMEN ÇÜRÜTÜLDÜ. skill-creator "aggregating benchmark results with variance analysis" sunuyor (adım var) — tezin ilk yarısı doğru. Ama SkillsBench (arXiv 2602.12670, akademik/bağımsız/Anthropic-bağlantılı olabilir) somut rakam yayınladı: "Curated Skills raise the average pass rate from 33.9% to 50.5% (+16.6pp)". Bu bir pass-rate artışıdır, tutarlılık/varyans-azalma rakamı DEĞİL — dolayısıyla iddianın "tutarlılık artışı rakamı yok" kısmı hâlâ ayakta, ama "hiç sayısal ölçüm yok" izlenimi yanlış: performans-ortalaması ölçülmüş, sadece run-to-run varyans/Pass^k rakamı bu fetch'te doğrulanamadı [?].

**9. Determinizm hook/script'te, skill metni model-yorumlu** — ÇÜRÜTÜLEMEDİ. Dokümanların tüm "low freedom" ve "solve, don't defer" bölümleri bunu doğruluyor; skill metninin kendisi bir talimat, yürütmesi model-bağımlı — hook/script harici determinizm sağlıyor.

**10. Skill'in kendisinin (prompt kalıbının) tutarlılık artırdığına dair yayınlanmış run-to-run ölçüm yok** — ZAYIF ÇÜRÜTME [?]. SkillsBench, skill'li/skill'siz koşumları 7.308 trajectory üzerinde karşılaştırıyor ve "Pass^3… remains low across all conditions" buluyor (WebSearch sentezinden, birincil metin tam okunmadı) — bu tam olarak "skill kullanımıyla run-to-run tutarlılık ölçümü" örneği olabilir, ama sonuç düşük kalıyor yani skill'in tutarlılığı garanti ETMEDİĞİni gösteriyor — tezi zayıflatmıyor, aksine destekliyor. Net çürütme bulunamadı.

**Genel değerlendirme:** A3 tezinin çekirdek iddiaları (skill = model-yorumlu prompt kalıbı; gerçek determinizm script/hook'ta yaşar; resmi dokümantasyon bunu örtük biçimde önerir) birincil kaynaklarla güçlü doğrulandı, çürütülemedi. Tek gerçek gedik: "yerleşik eval yok" iddiası platform-genel doğru ama Anthropic'in kendi skill-creator'ı fiili bir otomatik-eval hattı sunuyor — bu bir sınır-durumu, tam çürütme değil.

Sources:
- [Claude Code Skills docs](https://code.claude.com/docs/en/skills)
- [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [SkillsBench arXiv abstract](https://arxiv.org/abs/2602.12670)
- [anthropics/skills skill-creator SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) [?, doğrudan açılmadı]
