# Tez A1 — md→skill atlas koşumu (2026-09-15, Sonnet işçi, AS-OF 2026-09-15)

# TEZ Raporu — A1: CLAUDE.md/AGENTS.md içeriğini SKILL'e taşıma ("progressive disclosure" iddiası)

## (1) Resmî yükleme modeli

Anthropic'in resmî Agent Skills genel bakış sayfasına göre (WebFetch ile açıldı) sistem üç katmanlı: **Level 1 — Metadata (her zaman yüklü):** YAML frontmatter'daki `name` + `description`, başlangıçta sistem promptuna girer, ~100 token/skill. **Level 2 — Instructions (tetiklenince yüklenir):** SKILL.md gövdesi, Claude bash ile `cat SKILL.md` çalıştırıp okuduğunda bağlama girer; önerilen sınır **5k token altı**. **Level 3 — Resources/code (gerektikçe):** ek dosyalar yalnız referans verildiğinde okunur, script'ler bash ile çalışır ve yalnız ÇIKTISI bağlama girer, kodun kendisi girmez.
[Agent Skills — Claude Platform Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), AS-OF 2026-09-15 (çekim tarihi).

`name` alanı ≤64 karakter (küçük harf/rakam/tire, "anthropic"/"claude" yasak), `description` ≤1024 karakter, ikisi de XML etiketi içeremez, ikisi de ZORUNLU alan. Aynı kaynak.

CLAUDE.md farkı: dokümanda doğrudan CLAUDE.md karşılaştırması yok ama örtük fark net — CLAUDE.md/system prompt HER ZAMAN tam metniyle bağlamda oturur (statik yük); SKILL.md yalnız tetiklendiğinde girer (koşullu yük). Anthropic mühendislik blog yazısı bunu "Claude'un VM'inde dosya sistemi erişimiyle... context'i baştan tüketmek yerine kademeli yükleme" diye çerçeveliyor.
[Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills), AS-OF 2026-09-15.

Bu blog yazısından WebFetch çıktısı: örnek olarak form-doldurma talimatlarının ayrı `forms.md`'ye taşınıp SKILL.md'nin "lean" (yalın) tutulması gösteriliyor — somut sayısal ölçüt (token eşiği, "şu boyutu geçerse taşı" kuralı) yazıda YOK; ilke niteliğinde.

## (2) Hangi içerik skill'e, hangisi CLAUDE.md'de kalmalı

Resmî kaynaklar keskin bir "şu tip içerik oraya gider" tablosu vermiyor; skill-creator SKILL.md'sinden (WebFetch, GitHub raw) çıkan ölçüt: **skill'e uygun** = deterministik/tekrarlanan iş akışları, "objectively verifiable outputs" (dosya dönüşümleri, veri çıkarma), koşullu bilgi (ör. çerçeve seçimine göre değişen referans dosyalar), araç-zinciri/script'ler. **Skill'e uygun değil** = sübjektif değerlendirme (yazı stili, tasarım beğenisi gibi tek-seferlik yargılar), tek-adımlık basit görevler.
[skill-creator SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md), AS-OF 2026-09-15.

Bu ölçüt CLAUDE.md'de KALMASI gerekenleri dolaylı tanımlıyor: her zaman geçerli kimlik/yetki/davranış kuralları (koşulsuz, her promptta lazım) — tam da JARVIS'in kendi CLAUDE.md'sinin içeriği (Katman-1 yetki, teslim usulü). Koşullu/nadiren-lazım prosedür ise skill adayı. Ancak bu benim çıkarımım — kaynak bunu net formüle etmiyor, [?] işaretliyorum.

## (3) Ölçülmüş kazanç/zarar

**SkillsBench** (2026-02-13, 40 yazar, ilk 10'da Xiangyi Li, Wenbo Chen, Yimin Liu... — listede "Kun Chen" YOK, en yakın isim "Xiaokun Chen"):
- Kuratörlü (insan yazımı) skill'ler ortalama pass rate'i **+16.2 puan** artırıyor; alanlar arası büyük varyans (Healthcare +51.9pp, Software Engineering +4.5pp); 84 görevden 16'sında NEGATİF etki.
- Kendinden-üretilen (self-generated) skill'ler ortalama **+0 / -1.3pp** — model kendi prosedürünü güvenilir yazamıyor.
- **2-3 modüllü odaklı skill'ler: +18.6pp (optimal)**; 4+ skill veya kapsamlı/monolitik dokümantasyon yüklendiğinde keskin düşüş ve negatif getiri — "context overload" (bağlam aşırı yükü) nedeniyle.
[SkillsBench — emergentmind özeti](https://www.emergentmind.com/papers/2602.12670), AS-OF 2026-02-13 (yayın) / 2026-09-15 (çekim). Not: bu emergentmind ÖZET sayfası, birincil arXiv makalesi (2602.12670) değil — ikincil kaynak, rakamlar K (kestirim/aktarım) düzeyinde işaretlenmeli.

**"Kun Chen, Program Bench, 2026-06" iddiası: BULUNAMADI.** İki ayrı arama turunda ("Program Bench", "ProgramBench") bu isimde bir kaynak/makale/repo çıkmadı. Bulunan tek Kun Chen materyali, 2026-06 tarihli bir X gönderisi — ama konusu skill'ler değil, **Claude Code harness'inin OpenCode/Cursor CLI'ye kıyasla performansı** hakkında.
[Kun Chen X gönderisi](https://x.com/kunchenguid/status/2065345999682568593), AS-OF 2026-06 (gönderi tarihi, X içeriği erişilemedi/WebFetch denenmedi — sadece arama snippet'i). Emirdeki "rastgele internet skill'i performansı düşürür" iddiası muhtemelen SkillsBench'in monolitik-skill/context-overload bulgusuyla KARIŞTIRILMIŞ ya da yanlış atfedilmiş. Bu satır bir uyarı: kaynak adı ve tarih doğrulanamadı, iddia sahibi/tam başlık teyit edilemedi.

## (4) skill-creator'ın "CLAUDE.md'den çıkarma" akışı

`skill-creator/SKILL.md` (GitHub raw, WebFetch ile açıldı) içinde **CLAUDE.md'den direktif çıkarıp skill'e dönüştüren ayrı, adlandırılmış bir akış YOK**. Doküman genel skill-oluşturma sürecini (workflow sorgulama → klasör iskeleti → SKILL.md formatlama → kaynakları paketleme) tanımlıyor; CLAUDE.md'yi kaynak olarak tarayan özel bir adım belgelenmemiş.
[skill-creator SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md), AS-OF 2026-09-15.

---

## İDDİA LİSTESİ

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
