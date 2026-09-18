# K-013 (+V25) — Jarvis-Benzeri Ekosistem Araştırması
*2026-07-12 · İki paralel ajan koşusu (repo taraması + skill/loop/hiyerarşi pratikleri) · Carvis sentezi başta, ham raporlar altta.*

## Carvis sentezi — build'i etkileyen 5 bulgu

1. **LLM-wiki v2 çözülmüş (build adım 3'ü DOĞRUDAN etkiler):** Karpathy deseninin topluluk v2'si (rohitg00 gist) confidence-scoring + bayat-iddia süpersede + çelişki tespiti içeriyor — çelişki kapımızın wiki-düzeyi hali. **Öneri: adım 3'te wiki yazım standardını yazmadan önce v2 gist 1 saatlik okuma.** (Geç-keşif riskinin ta kendisi — K-013'ü build önüne almak doğru çıktı.)
2. **Pointer sistemimiz (m.20) bağımsız doğrulandı:** resmi skill "progressive disclosure" ilkesi birebir aynı — metadata hep yüklü, gövde tetiklenince, detay alt-dosyada. Kendi icadımız sektör standardıymış; CLAUDE.md tam sürümünde (adım 1) bu hizayı not düşmeye değer.
3. **Pano v2 için tek en değerli kaynak: Beads (Yegge):** kanban kartlarına makine-okur alan (ID, bağımlılık, durum) → ajanlar pano üzerinden koordine olur. Adım 4 şablon güncellemesinde tarih/yaş alanının yanına ID+bağımlılık alanı eklemek ucuz ve ajan dönemine hazırlık.
4. **"Done yazılamayan iş devredilmez" her yerde ortak ilke:** loop güvenliğinin üç ayağı = done tanımı + tur limiti + bütçe tavanı. KILAVUZ'a (adım 2) aday kural: kartta DONE yoksa kart açılmaz (zaten fiilen uyguluyoruz, resmileşir).
5. **V13/token-zaman sorusunun saha cevabı:** resmi formül YOK; herkes tur limiti + rol-başına model seçimiyle dolaylı bütçeliyor. Ölçülmüş ders: ucuz model ≠ ucuz iş (Haiku analitik işte daha çok tur → toplam token DAHA kötü). Karar kuralı: paralellik kazancı > koordinasyon vergisi ise takım, değilse tek güçlü ajan. #24b alternatif formülümüzle uyumlu — V13 tasarım oturumu için ön-borç kapandı.

**İlham-aday kısa listesi (kurulum yok, okuma sırasıyla):** LLM-wiki v2 gist (adım 3 öncesi) · jimcen33/personal-os (30 dk, birebir muadil rakip analizi) · Beads README (adım 4 öncesi) · superpowers desenleri (skill'leştirilmiş metodoloji fikri, tüzük maddesi olarak yeniden yazılır) · second-brain-starter'ın "script veri toplar → LLM akıl yürütür" maliyet deseni (K-009 açılınca ilk kural).

**Çürüyen/ertelenen:** ruflo, openclaw, gastown → kurulmaz, yalnız desen madeni; heartbeat/hook desenleri K-009 tetiğine bağlı.

---

## Ham Rapor 1 — Jarvis-benzeri GitHub projeleri
# JARVIS-Benzeri Kişisel AI Orkestrasyon Projeleri — Araştırma Raporu (2026-07-12)

Yıldız sayıları ~yaklaşıktır (API proxy önbelleği; canlı sayfa %5-15 daha yüksek olabilir). "Son itme" = son commit push tarihi.

## 1. İlgili Repolar ve Çalınacak Fikirler

### Doğrudan JARVIS/Homebase muadilleri

**1. [coleam00/second-brain-starter](https://github.com/coleam00/second-brain-starter)** — ~665 yıldız, oluşturma 2026-03-29. Claude Code + Agent SDK üstünde "ikinci beyin" kurduran skill: gereksinim şablonu → kişiselleştirilmiş 9-fazlı PRD (hafıza katmanı, hook'lar, proaktif heartbeat).
**Çalınacak:** (a) BOOTSTRAP.md deseni — ilk oturumda kullanıcıyı mülakata alan, SOUL/USER/HEARTBEAT dosyalarını doldurup kendini silen kurulum sihirbazı. (b) Proaktiflik seviyeleri (Observer/Advisor/Assistant/Partner) — Katman 1/2 ayrımının dörtlü versiyonu. (c) Heartbeat maliyet dersi: "Python veri toplar → Claude akıl yürütür" ~7x ucuz ($0.05 vs $0.38/koşu).

**2. [jimcen33/personal-os](https://github.com/jimcen33/personal-os)** — 0 yıldız ama JARVIS'e en yakın ikiz (oluşturma 2026-05-17, son itme 2026-06-20): "solo founder için file-first LLM wiki + Cowork OS", CLAUDE.md + AGENTS.md çift dosyalı, 5 katmanlı model.
**Çalınacak:** AGENTS.md ayrımı (ajan-davranış kuralları bağlamdan ayrı); 30 dakikada komple okunur, rakip analizi olarak birebir.

**3. [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)** — ~9.200 yıldız (2026-04-07). Obsidian + Claude Code kendini organize eden ikinci beyin; kaynak at → okur, bağlar, grafiğe dosyalar. Karpathy LLM Wiki deseninin en popüler uygulaması.
**Çalınacak:** ingest hattının çözülmüş hali — bağlama (linking) kuralları + dosyalama taksonomisi.

**4. [ar9av/obsidian-wiki](https://github.com/ar9av/obsidian-wiki)** — ~2.800 yıldız, son itme 2026-07-11 (çok aktif). Aynı desenin framework hali; kritik fark: her skill'in kendisi markdown — herhangi bir agent okuyup çalıştırabilir.
**Çalınacak:** "skill = düz markdown, ajan-agnostik"; tüzük/pano dosyalarının aynı zamanda çalıştırılabilir prosedür olması.

**5. [smixs/agent-second-brain](https://github.com/smixs/agent-second-brain)** — ~261 yıldız. Telegram sesli not → Obsidian + Todoist + günlük rapor.
**Çalınacak:** (a) Ebbinghaus-decay'li hafıza (eski bilgi sönümlenir/özetlenir). (b) Vault health scoring — bilgi tabanı sağlık puanı, bakım turu fikri.

**6. [Ramsbaby/jarvis](https://github.com/ramsbaby/jarvis)** — ~11 yıldız, son itme 2026-07-06. Kendini onaran AI ops platformu.
**Çalınacak:** (a) 7-Gate auditor harness — çelişki kapısının (m.16) genelleştirilmiş hali. (b) Maliyet şeffaflığı (7 günlük cron LLM maliyeti ölçülüp yayınlanıyor).

**7. [kcwoodfield/LifeOS-OSS](https://github.com/kcwoodfield/LifeOS-OSS)** — ~15 yıldız. current-work.md deseni = durum-kapsulu.md'nin muadili; fark: sürekli-güncelleme disiplini kurallaştırılmış.

### Orkestrasyon / hiyerarşik ajan altyapıları

**8. [gastownhall/gastown](https://github.com/gastownhall/gastown)** (Yegge) — ~17.000 yıldız, çok aktif. "Mayor" orkestratör + işçi ajanlar, her biri kendi git worktree'sinde.
**Çalınacak:** rol-adlı kalıcı ajan kimlikleri + iş sahipliğinin dosya sisteminde izolasyonu; CEO+ajanlar modelinin en olgun açık örneği.

**9. [gastownhall/beads](https://github.com/gastownhall/beads)** (Yegge) — ~25.000 yıldız. Git-destekli, ajanların kendilerinin açıp kapattığı issue/görev veritabanı.
**Çalınacak:** kanban'ın ajan-yazılabilir olması — kartlara makine-okur kimlik (ID, bağımlılık, durum) → ajanlar pano üzerinden koordine olur. Pano v2 için en değerli tek kaynak.

**10. [ruvnet/ruflo](https://github.com/ruvnet/ruflo)** — ~59.000 yıldız. Kurulmaz (JARVIS felsefesine ters); swarm topolojileri dokümantasyonu (hiyerarşik/mesh/pipeline) harita olarak okunur.

**11. [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)** — ~71.000 yıldız. "Bash is all you need": agent-harness'ı sıfırdan inşa eden eğitim reposu — "her şeyi kendim kurarım" kuralına birebir müfredat.

**12. [openclaw/openclaw](https://github.com/openclaw/openclaw)** — ~377.000 yıldız. Kurulmaz; dosya-adı sözleşmeleri (SOUL/MEMORY/günlük log) ekosistem ortak dili; heartbeat (30 dk kontrol turu) scheduled-loop referansı.

**13. [FlorianBruniaux/claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide)** — ~5.300 yıldız. agent-teams.md bölümündeki maliyet/koordinasyon karar tabloları: "subagent mı team mi" cevap anahtarı.

## 2. Skill Ekosistemi
[anthropics/skills](https://github.com/anthropics/skills) (~149K, resmi) · [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) (~64K) · [obra/superpowers](https://github.com/obra/superpowers) (~240K — skill'lerle kodlanmış çalışma disiplini; tüzüğün skill'leştirilmesi için ilham) · [wshobson/agents](https://github.com/wshobson/agents) (~37K).

İyi skill yazma (resmi best-practices): progressive disclosure (ad+açıklama hep yüklü ~100 token; gövde tetiklenince <5K; detay alt-dosyada) — **pointer sistemi (m.20) ile aynı ilke, bağımsız keşif**. SKILL.md <500 satır; açıklama = "ne yapar + ne zaman" (tetikleme isabetini bu belirler); en değerli bölüm "Gotchas" (skill-başına hata/tuzak listesi — ingest defterinin skill karşılığı).

## 3. Hiyerarşik Ajan Pratikleri: Model + Bütçe
- Rol-başına model katmanlama fiili standart: güçlü model = orkestratör/plan/inceleme; orta = işçi; ucuz = sınıflandırma/yönlendirme. Doğru yönlendirme "hepsi güçlü model"e göre %60-80 tasarruf.
- Ucuz model ≠ ucuz iş: ölçülmüş vaka — Haiku-işçili 37-ajan koşusu analitik işte daha çok tur → toplam token verimi DAHA KÖTÜ (her tur = bağlamın yeniden okunması).
- Bütçenin gerçek birimi: token × ajan sayısı × tur sayısı; 4-ajanlı takım aynı işte tek ajanın ~3-4 katı token. Duvar-saati kazancı yalnız iş gerçekten paralelleşiyorsa. Karar kuralı: **paralellik kazancı > koordinasyon vergisi ise takım, değilse tek güçlü ajan.** En yaygın emniyet: tur limiti.
- Subagent (rapor verip ölen işçi) vs team (birbirinin bulgusunu gören eşler) ayrımı.

## 4. Geç-Keşif Riskleri
1. **Karpathy LLM Wiki v2** ([rohitg00 gist](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2)): confidence scoring + bayat-iddia süpersede + çelişki tespiti — #16 uygulamasından ÖNCE okunmalı (1 saat, aylar kazandırır).
2. Hafıza dosya anatomisi çözüldü: SOUL/USER/MEMORY/daily-log + SessionStart-PreCompact-SessionEnd hook üçlüsü ortak şablon; okuma-sırası protokolümüz bunun elle hali.
3. "Pano = ajan hafızası" çözüldü (Beads) — kopya çekilecek şey, sıfırdan tasarlanacak değil.
4. Heartbeat maliyet deseni çözüldü: script veri toplar, LLM yalnız akıl yürütür.
5. Skill tetikleme/progressive-disclosure kuralları resmileşti — baştan uy.

Belirsizlik: yıldız/tarihler ungh.cc önbelleği ±%10; jimcen33/personal-os içeriği README/arama özetinden, satır satır doğrulanmadı.


---

## Ham Rapor 2 — Skill/loop/hiyerarşi pratikleri
# Skill/Plugin Ekosistemi + Loop Engineering + Hiyerarşi Pratikleri (2026-07-12)

Belirsiz/eskimiş olabilecek iddialar [?] işaretli.

## 1. Skill Ekosistemi
- Resmi: [anthropics/skills](https://github.com/anthropics/skills) (skill-creator dahil) · [Agent Skills engineering yazısı](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) · [best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) · [Claude Code skills docs](https://code.claude.com/docs/en/skills). SKILL.md artık açık standart: Codex CLI, Gemini CLI, Copilot, Cursor da destekliyor [topluluk iddiası].
- Marketplace katmanları: resmi Anthropic marketplace (~101 plugin, Mart 2026 [?]) · topluluk marketplace [?] · bağımsız dizinler (claudemarketplaces.com 21.700+ skill iddiası [şişik olabilir]; jeremylongshore 425 plugin/2.810 skill) · en etkili koleksiyon: [obra/superpowers](https://github.com/obra/superpowers) — TDD, sistematik debugging, subagent-driven development metodolojisi.
- Yapı/tetikleme: frontmatter zorunlu = name, description; tetikleme description üzerinden. Ek alanlar: disable-model-invocation (yalnız elle — commit/deploy gibi yan etkili işler), allowed-tools, disallowed-tools. Deterministik iş için skill'e script göm (model her seferinde kodu türetmesin).
- Test/eval (resmi skill-creator süreci): önce eval yaz (pozitif/negatif/edge), baseline ölç, minimum talimat, iterasyon; hedef 5+ pozitif + 2-3 negatif, %90+ geçiş. Modlar: Create/Eval/Improve/Benchmark + trigger tuning. Skill'i kullanacağın her modelle ayrı test et.

→ Uyarlama: skill-creator zaten kurulu — kendi skill'lere (ör. hizalama) 3'lü eval seti yazılır; superpowers kurulmaz, desenleri tüzük maddesi olarak yeniden yazılır.

## 2. Loop / Otomasyon
- Resmi çerçeve ([Getting started with loops](https://claude.com/blog/getting-started-with-loops), 06-30, tam metin): loop = stop koşulu sağlanana dek iş çevrimi. 4 tip: turn-based (devredilen: doğrulama) · goal-based /goal (devredilen: stop koşulu; evaluator YALNIZ Claude durmayı denediğinde kontrol eder — 07-07 düzeltmemizle uyumlu; evaluator küçük hızlı model, "hayır" gerekçesi sonraki tura yön verir) · time-based /loop lokal, /schedule bulut Routine (devredilen: tetikleyici) · proactive (devredilen: promptun kendisi).
- Resmi kalite/maliyet kuralları: doğrulamayı skill'le kodla, nicel kontrol en iyisi · taze bağlamlı ikinci agent'a review · başarısızlığı tekil düzeltme, sisteme kodla · büyük koşudan önce küçük pilot · /usage, /goal (argümansız = sayaç), /workflows ile izle.
- Yeni resmi içerik: [Dynamic workflows](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code) (06-02, research preview) · [Steering Claude Code](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more) (06-18: CLAUDE.md/skills/hooks/rules/subagents hangi katman ne zaman).
- Topluluk güvenlik pratikleri: üç koruma birlikte — tur limiti + bütçe tavanı + doğrulanabilir done. Drift: çoklu compaction spec'ten saptırır → orijinal görev tanımı compaction'ı atlatan kalıcı dosyada (= durum kapsülümüzün gerekçesi). Maliyet anekdotları: döngüde çocuk-agent doğurma bug'ı 5 dk'da 4M token; fatura sıçramaları [teyitsiz]. Sık polling pahalı — aralığı değişim hızına eşle.

→ Uyarlama: canlı agent yokken loop disiplini insan-döngüsü olarak kurulur: her kartta yazılı DONE + "N oturum sonra durdur/raporla" limiti; "done yazılamıyorsa kart açılmaz" tüzük/KILAVUZ adayı.

## 3. Hiyerarşi / Orchestrator
- Subagent = taze bağlamlı izole oturum; .claude/agents/*.md frontmatter'da model + araç kısıtı. Worktree izolasyonu: paralel yazma çakışmasını önler; "3 çözümü paralel dene, judge seçsin" resmi örnek.
- Model-per-role: plan/orkestrasyon güçlü, keşif ucuz, verification küçük model; 5-10x maliyet düşüşü iddiası [tek kaynak].
- Orchestrator döngüsü: clarify → plan → dispatch → verify; reviewer HER ZAMAN taze bağlamda.
- Rol başına bütçe: resmi formül YOK [boşluk tespiti] — herkes tur limiti + model seçimiyle dolaylı bütçeliyor; keşif görevlerine kısa çıktı sözleşmesi ("yalnız sonucu döndür") parent bağlamı korur.

→ Uyarlama: (1) ajan raporlarına rol-model eşlemesi yaz (Cowork Agent tool model parametresiyle bugün kurulabilir); (2) worktree'nin markdown karşılığı = pahalı işte önce kopya-klasörde taslak, veto=revert (m.31 zaten bu); (3) verify = ayrı taze-bağlam denetçi oturumu — v6.1 dış-mahkeme pratiğinin kanıtlanmış hali.

## Sentez
Skill'ler eval'lı mühendislik disiplini oldu; loop'lar "durma koşulu + doğrulayıcı + bütçe" tasarımına dönüştü. Ortak ilkeler JARVIS'e doğrudan çevrilir: done tanımı yazılamayan iş devredilmez · doğrulama işi yapandan ayrı ve taze bağlamda · her role en ucuz YETERLİ model · başarısızlık tekil düzeltilmez, sisteme kodlanır. Üçüncü parti kurulum zorunlu değil — desenler tüzük maddesi ve kendi SKILL.md'lerimiz olarak yeniden inşa edilir.
