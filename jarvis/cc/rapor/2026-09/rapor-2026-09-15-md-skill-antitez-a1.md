# Antitez ¬A1 — md→skill atlas koşumu (2026-09-15, Sonnet, CoVe-Factored: yalnız iddia listesi verildi)

# Antitez Raporu — Hafıza md → Skill Taşıma (A1)

**Yöntem notu:** 7 araç çağrısı, 4 birincil kaynak açıldı (Anthropic resmi Skills sayfaları x2, SkillsBench arXiv makalesi, Kun Chen'in gerçek blog yazısı). Gerekçeler verilmediği için yalnız iddia metinlerine karşı kanıt arandı.

## Çürütülen / zayıflatılan iddialar

**İddia 1 (¬T1) — "~100 token/skill" rakamı birincil kaynakta yok.** Anthropic'in resmi `platform.claude.com` Skills sayfası (AS-OF 2026-09-15) yalnız şunu söylüyor: *"At startup, only the metadata (name and description) from all Skills is pre-loaded."* — spesifik bir token sayısı vermiyor. "~100 token" rakamı üçüncü-parti blog/medium kaynaklarından geliyor (Paragon, dev.to, Medium — WebSearch sonuçları), Anthropic'in kendi metni değil. Dolayısıyla iddia 1'in *mekanizması* doğru ama *rakamı* doğrulanamadı kaynak zincirinde — tahmini [?] olarak işaretlenmeli.
Kaynak: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices (AS-OF 2026-09-15)

**İddia 3 — "5k token altı" önerisi birebir yok, farklı ölçü kullanılıyor.** Resmi best-practices sayfası **"Keep SKILL.md body under 500 lines for optimal performance"** diyor — token değil SATIR sınırı. 500 satır kabaca 4-7k token'a denk gelebilir ama bu bir çıkarım, Anthropic'in kendi ifadesi değil. İddia 3'ün kaynak atfı gevşek: doğru büyüklük mertebesinde ama yanlış birim/kaynak.
Kaynak: aynı URL, "Token budgets" bölümü.

**İddia 10 — Kun Chen/ProgramBench atfı doğrudan yanlış, "muhtemel yanlış atıf" hükmü DOĞRULANDI (antiteze karşı kanıt bulunamadı, orijinal şüphe teyit oldu).** Kun Chen'in kendi blog yazısı ("Evaluating the Effectiveness of Programming Languages for Agents", blog.kunchenguid.com) incelendiğinde: ProgramBench, ajanların **programlama dili seçimini** (Rust/TypeScript/serbest seçim vb.) ölçen bir kıstas — skill'ler, Android Skills repo'su veya "%5 token artışı" ile hiçbir ilgisi yok. Antitez olarak bu iddiayı çürütmeye çalıştım, tam tersi güçlendi: iddia 10 zaten "doğrulanamadı" diyordu, ben de doğrulayamadım — **çürütülemedi**, hatta pekişti.
Kaynak: https://blog.kunchenguid.com/p/evaluating-the-effectiveness-of-programming (AS-OF 2026-09-15)

## Çürütülemeyen / pekişen iddialar

**İddia 9 — 2-3 modül optimal, 4+ negatif — birebir doğrulandı, karşı-kanıt bulunamadı.** SkillsBench makalesi (arXiv 2602.12670) net: *"Tasks with 2–3 Skills show the largest improvement (+18.6pp), while 4+ Skills provide only +5.9pp benefit"* ve kapsamlı dokümanlar *"–2.9pp"* negatif etki gösteriyor. **Çürütülemedi.**
Kaynak: https://arxiv.org/html/2602.12670v1, §"2–3 skills are optimal" (AS-OF 2026-09-15)

**İddia 7 (görev sayısı hariç) — genel yön doğrulandı, ama rakamlarda kaynak-içi tutarsızlık var.** Farklı ikincil kaynaklar (emergentmind, alphaXiv, WebSearch özetleri) 84/86/87 görev arasında geziniyor; makalenin kendisi (arXiv) "84 tasks" final set diyor, "86" ön-eleme adayı sayısı. Bu, iddianın kendi hassasiyetine karşı küçük ama gerçek bir kusur — **kısmen çürütüldü** (rakam değil ama kaynak-tutarlılığı bakımından).

**İddia 6, 11 — çürütülemedi.** Resmi sayfa CLAUDE.md kavramından hiç bahsetmiyor (o Claude Code'a özgü, Skills dokümantasyonu farklı ürün yüzeyi); "içerik nerede kalır" için kesin kural gerçekten yok. skill-creator skill'inin bu oturumdaki tanımında da adlandırılmış bir "CLAUDE.md'den skill'e taşı" akışı geçmiyor.

## En güçlü antitez: metodolojik confound (T7/T9'un temel dayanağına karşı)

SkillsBench'in kendi **Limitations** bölümü (§5.1) şunu itiraf ediyor: *"Skills context arttırıyor; yapısal faydanın 'daha fazla context'ten ayrı ölçülmesi gerekli"* (causal control sorunu). Bu kritik: SkillsBench **skill-var vs skill-yok** ölçüyor, **CLAUDE.md'de-aynı-içerik vs SKILL.md'de-aynı-içerik** ölçmüyor. Yani "hafızayı skill'e taşımak token tasarrufu + performans kazancı getirir" savının temel dayanağı — SkillsBench'in +16.2pp'si — aslında "prosedürel bilgi eklemenin faydası" ölçüyor, "nereye eklendiğinin" faydasını değil. Bu, tezin (A1) kilit mekanizma iddiasına karşı **çürütülemeyen** bir boşluk: mevcut birincil kaynaklar, CLAUDE.md'de kalsaydı aynı bilginin daha kötü sonuç vereceğini göstermiyor.

**Genel sonuç:** Tez A1'in performans dayanağı (iddia 9) sağlam; token-muhasebesi dayanağı (iddia 1, 3) kaynak hassasiyeti bakımından zayıf; Kun Chen atfı (iddia 10) gerçekten hatalı; ama en temel "taşıma işe yarar mı" sorusu SkillsBench tarafından **doğrudan test edilmemiş** — kendi limitasyon bölümünün itirafı.
