# Hakem paketi — maskeli (2026-09-15). Üç konu ailesi; her ailede iki taraf (P/Q) rastgele atanmış, hangisi tez hangisi antitez belirtilmemiş.


## Aile A1 — hafıza md → skill taşıma / progressive disclosure

### Taraf P
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


### Taraf Q
1. Skill metadata'sı (`name`+`description`) başlangıçta ~100 token/skill maliyetle her zaman sistem promptuna yüklenir.
2. SKILL.md gövdesi yalnız Claude'un talebi skill'in `description`'ıyla eşleştirmesi sonucu, bash ile okunduğunda bağlama girer.
3. Anthropic SKILL.md gövdesi için 5k token altını öneriyor; bunun üstü ayrı referans dosyalarına bölünmeli.
4. Skill'e bağlı script'lerin kaynak kodu asla bağlama girmez, yalnız çalıştırma çıktısı girer.
5. CLAUDE.md/system prompt statik ve her promptta tam yükken, SKILL.md koşullu ve yalnız tetiklendiğinde yüklenir — bu, iki mekanizma arasındaki temel yapısal fark.
6. Resmî kaynaklar "şu içerik türü CLAUDE.md'de kalır, şu türü skill'e taşı" diye kesin bir kural tablosu vermiyor; yalnız "deterministik/koşullu/tekrarlanan" ile "sübjektif/tek-seferlik" ayrımı var.
7. SkillsBench (2026-02, 40 yazar) kuratörlü skill kullanımında ortalama +16.2 puan pass-rate artışı ölçtü, ama 84 görevden 16'sında negatif etki gösterdi.
8. SkillsBench'e göre kendinden-üretilen (self-generated) skill'ler ortalamada fayda sağlamıyor (~0 / -1.3pp).
9. SkillsBench'e göre 2-3 modüllü odaklı skill setleri optimal (+18.6pp); 4+ skill veya monolitik/kapsamlı dokümantasyon "context overload" ile negatif getiriye dönüşüyor.
10. "Kun Chen, Program Bench, 2026-06, rastgele internet skill'i performansı düşürür" iddiası kaynak taramasında doğrulanamadı — BULUNAMADI, muhtemel yanlış atıf.
11. Bulunan tek doğrulanabilir Kun Chen kaynağı (2026-06 X gönderisi) skill'ler değil, Claude Code harness performansı hakkında — konudan bağımsız.
12. Anthropic'in resmî skill-creator aracında CLAUDE.md içeriğini tarayıp skill'e "extract eden" belgelenmiş, adlandırılmış bir akış yok; bu iddia [?] kestirim/karışıklık olabilir.


## Aile A2 — çok-proje md hiyerarşisi

### Taraf P
## Antitez Raporu — Çok-proje md hiyerarşisi (A2)

**Bütçe:** 4 araç çağrısı (2 birincil WebFetch + 2 WebSearch doğrulama). AS-OF 2026-09-15.

### Genel bulgu
11 iddianın çoğu resmi belgede (code.claude.com/docs/en/memory, erişim 2026-09-15) BİREBİR doğrulandı — ¬T bulunamadı, **çürütülemedi**. Gerçek zayıf noktalar yalnız 2 yerde: "en son=en etkili" ölçüm iddiası ve "resmi belge deseni destekliyor" iddiası.

**Madde 1 — kısmen çürütüldü [?].** Belge sırayı doğruluyor ("instructions closer to where you launched Claude are read last") ama bunun DAHA ETKİLİ olduğuna dair hiçbir ölçüm/deney sunmuyor. Aksine belge şunu söylüyor: "Claude treats [CLAUDE.md/memory] as context, not enforced configuration… no guarantee of strict compliance, especially for vague or conflicting instructions" ve "if two rules contradict each other, Claude may pick one arbitrarily." Yani "en son okunan = en etkili" varsayımdır, ölçülmüş bir iddia değildir — belge çelişkide rastgele seçim olabileceğini bile kabul ediyor. Bu A2'nin en zayıf halkası.

**Madde 2 — çürütülemedi.** Belge tam olarak doğruluyor: alt-dizin CLAUDE.md'leri "instead of loading them at launch, they are included when Claude reads files in those subdirectories."

**Madde 3 — çürütülemedi.** "maximum depth of four hops" ve "imported files still load and enter the context window at launch" — iddia birebir doğru, "token tasarrufu sağlamaz" kısmı da teyitli.

**Madde 4 — çürütülemedi.** "target under 200 lines… Claude Code skips a file over 4 MiB" — birebir.

**Madde 5 — çürütülemedi.** "first 200 lines of MEMORY.md, or the first 25KB, whichever comes first."

**Madde 6 — çürütülemedi.** "Claude Code reads CLAUDE.md, not AGENTS.md… create a CLAUDE.md that imports it" ya da symlink — birebir.

**Madde 7 — çürütülemedi, güçlendi.** WebSearch (Linux Foundation basın bülteni, linuxfoundation.org) teyit ediyor: AAIF (Agentic AI Foundation) Aralık 2025'te kuruldu, AGENTS.md OpenAI öncülüğünde Ağustos 2025'te başlayıp Linux Foundation'a devredildi; 2026 ortası 60.000+ repo, 20+ araç desteği bildiriliyor [kaynak ikincil arama özeti, birincil belge açılmadı — bütçe sınırı].

**Madde 8 — çürütülemedi.** WebSearch: `claude --worktree <isim>` (kısa `-w`) v2.1.49'da (Şubat 2026) eklenmiş yerleşik komut, `.claude/worktrees/` altında yeni worktree+branch açıyor — iddiayla örtüşüyor [ikincil kaynak; code.claude.com/docs/en/worktrees birincil olarak açılmadı, bütçe sınırı].

**Madde 9 — çürütülemedi.** Belge birebir: "a gitignored CLAUDE.local.md only exists in the worktree where you created it" ve auto-memory "shared across worktrees."

**Madde 10 — çürütülemedi, gerilim teyitli.** Resmi belge olay-tetikli ekleme öneriyor ("Claude makes the same mistake a second time" → CLAUDE.md'ye ekle). Kun Chen blogu ise "haftalık toplu düzenleme" + "~5000 token sabit bütçe" savunuyor, anlık tekil düzeltmeyi değil ("evidence comes from transcripts, not from anecdotes," "batch before you update"). İki kaynak GERÇEKTEN farklı ritim öneriyor — iddia doğru, ama bu bir çelişki değil, tamamlayıcı farklı ölçek (Anthropic: ne eklenir: eşik-kuralı; Kun Chen: ne zaman eklenir: ritim-kuralı) olarak da okunabilir [?].

**Madde 11 — kısmen çürütüldü.** Resmi belgede "global md minimal, proje md = birikmiş dersler" çerçevesi DOĞRUDAN yok; belge sadece kapsam tablosu veriyor (yönetilen/kullanıcı/proje/yerel), "proje md nöral-ağ gibi kod yoluyla gelişir" metaforu YALNIZ Kun Chen'e ait, Anthropic hiç böyle bir dil kullanmıyor. Yani desen resmi belgede "karşılık bulmuyor" — Kun Chen'in kendi çerçevesi, Anthropic'in onayı değil.

### Sınanmayan nokta
"Tek global md'nin çok-proje ortamında zararı (yanlış projede yanlış kural) belgelenmiş mi" — iki birincil kaynakta da BULUNAMADI; ne Anthropic ne Kun Chen bu riski ölçüyor/örnekliyor. Bu boşluk A2'nin en savunmasız varsayımı: çok-proje riski iddia edilen ama hiçbir kaynakta ölçülmemiş bir zarar.

### Sonuç
10/11 madde çürütülemedi (resmi/ikincil kaynaklarla teyitli). Gerçek kırılma: (a) madde 1'in "en etkili" kısmı ölçümsüz varsayım, (b) madde 11'in resmi-belge-onayı iddiası abartılı, (c) çok-proje zararı hiçbir yerde belgelenmemiş — A2 tezinin kanıt-dışı en kırılgan noktaları burada.


### Taraf Q
1. Claude Code CLAUDE.md yükleme sırası: managed → kullanıcı → proje → yerel, en dar kapsam bağlamda en son (en etkili) konumda (code.claude.com/docs/en/memory).
2. Çalışma dizini ve üstündeki CLAUDE.md/CLAUDE.local.md dosyaları oturum açılışında; çalışma dizini ALTINDAKİ alt-dizin CLAUDE.md'leri yalnız o dizindeki dosya okunduğunda (lazy) yüklenir.
3. `@path` import göreli yolu, içinde bulunduğu dosyaya göre çözer; iç içe import derinliği en fazla 4 hop; import edilen içerik yine launch'ta bağlama girer (token tasarrufu sağlamaz).
4. Resmî öneri: CLAUDE.md dosyası başına hedef 200 satırın altı; 4 MiB üstü dosya tamamen atlanır.
5. Auto-memory `MEMORY.md` için ayrı bir sınır var: ilk 200 satır ya da 25 KB (hangisi önce dolarsa).
6. Claude Code AGENTS.md'yi doğrudan okumaz; `@AGENTS.md` import ya da symlink ile köprüleniyor.
7. AGENTS.md standardı artık Agentic AI Foundation (Linux Foundation) yönetiminde, Codex/Cursor/Copilot/Gemini CLI/Jules dahil 30+ araç tarafından okunuyor.
8. Gemini CLI: aynı dizinde GEMINI.md ve AGENTS.md birlikte varsa GEMINI.md önceliklidir; AGENTS.md ancak `context.fileName` ayarına eklenirse okunur. [?] ikincil kaynak.
9. Claude Code'da `claude --worktree <isim>` yerleşik komutu ayrı checkout+branch açar; repo'da en az 1 commit şart, yoksa hata verir (resmî belge, birincil doğrulandı).
10. Worktree'ler arası: gitignore'lu CLAUDE.local.md yalnız oluşturulduğu worktree'de vardır; auto-memory ise aynı repo'nun tüm worktree'lerinde PAYLAŞILIR (machine-local).
11. Resmî Anthropic belgesi "Claude aynı hatayı ikinci kez yaptığında CLAUDE.md'ye ekle" desenini doğrudan öneriyor — Kun Chen L8 videosunun/blogunun deseniyle örtüşüyor ama YÖNTEMDE farklı: Kun Chen anlık değil, kanıta dayalı HAFTALIK toplu (batched) düzenleme + sabit token bütçesi öneriyor.
12. Codex'in `~/.codex/AGENTS.md` + proje kökü + alt-dizin üç katmanlı hiyerarşisi ve 32 KiB varsayılan bütçesi yalnız ikincil kaynaktan geldi, birincil Codex belgesi açılmadı — [?] doğrulanmamış.


## Aile A3 — skill = kalıp-prompt, deterministik icra

### Taraf P
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


### Taraf Q
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
