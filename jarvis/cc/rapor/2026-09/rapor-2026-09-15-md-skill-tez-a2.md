# Tez A2 — md→skill atlas koşumu (2026-09-15, Sonnet işçi, AS-OF 2026-09-15)

# TEZ Raporu — Çok-proje bağlam ayrımı ve talimat-dosyası hiyerarşisi (A2)

## (1) Claude Code — CLAUDE.md katmanları
Resmî belge (code.claude.com/docs/en/memory, AS-OF 2026-09-15) dört-beş katmanlı bir yükleme sırası tanımlıyor, GENİŞTEN DARA doğru: **managed/kurumsal** (`/Library/Application Support/ClaudeCode/CLAUDE.md` vb., ya da `managed-settings.json` içinde `claudeMd` anahtarı) → **kullanıcı** (`~/.claude/CLAUDE.md`) → **proje** (`./CLAUDE.md` veya `./.claude/CLAUDE.md`) → **yerel** (`./CLAUDE.local.md`). Belge açıkça "bu tablo yükleme sırasında, en geniş kapsamdan en dara doğru — proje talimatı bağlamda kullanıcı talimatından SONRA görünür" diyor; yani hepsi ÇAKIŞMAZ, ÜST ÜSTE BİNMEZ — hepsi birleştirilip (concatenate) bağlama konur, en son okunan (proje/yerel) en yüksek etkili öncelik kazanır çünkü modelin "en yakın zamanda okuduğu" olur.

Alt-dizin CLAUDE.md dosyaları **lazy**: çalışma dizini ve üstündeki tüm CLAUDE.md/CLAUDE.local.md dosyaları oturum AÇILIŞINDA yüklenir; çalışma dizini ALTINDAKİ alt-dizinlerin CLAUDE.md'leri ise Claude o alt-dizindeki dosyaları OKUDUĞUNDA devreye girer — önceden yüklenmez.

`@path/to/import` sözdizimi: göreli yollar İÇİNDE BULUNDUĞU dosyaya göre çözülür (çalışma dizinine göre değil); iç içe import'lar desteklenir, **maksimum derinlik 4 hop**; kod bloğu/backtick içindeki `@` atlanır (literal kalır). İçe aktarılan dosyalar YİNE launch'ta bağlama girer — yani import organizasyon kolaylığı sağlar ama TOKEN TASARRUFU sağlamaz (belge bunu açıkça söylüyor).

**Boyut önerisi — resmî:** CLAUDE.md başına hedef **200 satırın altı**; 4 MiB üstü dosya tamamen atlanır. Daha kısa dosyalar daha yüksek uyum (adherence) veriyor, belge bunu doğrudan iddia ediyor. Ayrı olarak auto-memory `MEMORY.md` dosyası için sert bir okuma sınırı var: **ilk 200 satır VEYA 25 KB** (hangisi önce gelirse) — bu farklı bir mekanizma (Claude'un kendi yazdığı notlar), CLAUDE.md'den ayrı.
Kaynak: https://code.claude.com/docs/en/memory (AS-OF 2026-09-15)

Not: Claude Code **AGENTS.md'yi okumuyor**; bunun yerine CLAUDE.md içine `@AGENTS.md` import ya da symlink öneriliyor. Aynı sayfa.

## (2) AGENTS.md standardı ve diğer harness'ler
AGENTS.md artık **Agentic AI Foundation** (Linux Foundation altında) tarafından yönetiliyor; başlangıçta OpenAI/Codex öncülüğünde, şimdi 30+ ajan tarafından okunuyor (Codex, Copilot, Cursor, Gemini CLI, Jules, Aider, Zed, Windsurf, Devin).
Kaynak: https://agents.md/ (AS-OF 2026-09-15)

**Codex:** üç katman — kullanıcı-geneli `~/.codex/AGENTS.md`, proje kökü `AGENTS.md`, alt-dizin `AGENTS.md`/`AGENTS.override.md` (yol-kapsamlı override). Ev dizini + kök + çalışma dizini dosyaları birleştirilir, varsayılan **32 KiB bütçe** (`project_doc_max_bytes`) sınırında kesilir. [?] Bu rakam WebSearch özetinden geldi, birincil Codex belgesini AÇMADIM — doğrulanmamış, ikincil kaynak riski taşıyor.

**Cursor:** AGENTS.md'yi doğrudan okuyor + kendi `.cursor/rules/*.mdc` sistemi var; her `.mdc` dört tipten biri (always / glob-eşleşmeli / açıklama-tabanlı akıllı / manuel). Kurallar alt-dizinlerde genişler; Team/Enterprise'da dashboard "Team Rules" proje kurallarının ÜSTÜNDE.

**Gemini CLI:** kendi `GEMINI.md` dosyası var; aynı dizinde hem `GEMINI.md` hem `AGENTS.md` varsa **GEMINI.md kazanır**; AGENTS.md okuması `settings.json`'daki `context.fileName` dizisine EKLENMEDİKÇE devreye girmiyor. Aşağı-doğru (downward) tarama: mevcut klasörden alt-dizinlere recursive.

Ortak desen: (a) global/kullanıcı katmanı en geniş-en düşük öncelikli, proje/alt-dizin en dar-en yüksek öncelikli; (b) neredeyse tüm harness'lerde "en yakına en çok ağırlık" ilkesi tekrarlanıyor; (c) hiçbiri resmi belgede kesin bir "satır sayısı" limiti dayatmıyor — Claude Code'un 200-satır önerisi kendine özgü.
Kaynak (WebSearch özeti, birincil sayfalar açılmadı — ikincil, [?] işaretli): morphllm.com/agents-md-guide, eastondev.com Codex yazısı, Gemini CLI için medium.com/@google-cloud serisi. AS-OF 2026-09-15.

## (3) Git worktree — Claude Code yerleşik desteği
Resmî belge (code.claude.com/docs/en/common-workflows) VAR olduğunu doğruluyor: `claude --worktree <isim>` (kısa `-w`) komutu her worktree için ayrı checkout + ayrı branch açar; repo'da en az bir commit gerekiyor (yoksa `git rev-parse failed` hatası). Ayrı bir sayfa (`/docs/en/worktrees`) temizlik, `.worktreeinclude` (gitignore'lu config senkronu) ve git-dışı VCS desteğini kapsıyor — BU sayfayı doğrudan AÇMADIM, yalnız pointer'ını gördüm.
Kaynak: https://code.claude.com/docs/en/common-workflows (AS-OF 2026-09-15, birincil, AÇILDI)

Her worktree'nin ayrı bağlamı/md'si olması: resmî belge (memory sayfası) worktree'ler için özel bir uyarı taşıyor — gitignore'lu `CLAUDE.local.md` yalnız OLUŞTURULDUĞU worktree'de var olur, paylaşılmaz; kişisel talimatları worktree'ler arası paylaşmak için ev dizininden import öneriliyor (`@~/.claude/my-project-instructions.md`). Auto-memory ise TERSİNE, repo bazlı paylaşılıyor: "tüm worktree'ler ve alt-dizinler AYNI git repo'sunun AYNI auto-memory dizinini paylaşır" (machine-local, makineler arası paylaşılmıyor).
İkincil kaynaklar (WebSearch özeti, [?] işaretli — açılmadı): v2.1.49'da (2026 Şubat) yerleşik desteğin geldiği, v2.1.218'de bir subagent/git-worktree izolasyon açığının düzeltildiği iddiaları — rakamlar/versiyon numaraları DOĞRULANMADI, ikincil blog kaynaklarından.

## (4) "Global md minimal, proje md = birikmiş ders" deseni
Resmî Claude Code belgesinde AYNI DESEN doğrudan var: "CLAUDE.md'ye şunları ekle: Claude aynı hatayı ikinci kez yaptığında, code review bir şey yakaladığında, aynı düzeltmeyi ikinci kez sohbete yazdığında" — yani anlık/olay-tetikli md güncellemesi resmen öneriliyor.
Kaynak: https://code.claude.com/docs/en/memory, "When to add to CLAUDE.md" bölümü (AS-OF 2026-09-15, birincil, AÇILDI).

Kun Chen'in blog yazısı (video ile aynı yazarın metin karşılığı — videonun kendisini AÇAMADIM, YouTube transkripti çekilemedi) FARKLI/DAHA KATI bir model öneriyor: proje-md'yi "nöral ağ ağırlığı" gibi ele al — **sabit token bütçesi** (örnek olarak 5000 token verilmiş, [?] örnek rakam, evrensel kural değil), kanıt sadece transkriptten (anekdot değil), TEK olaydan değil BİRDEN FAZLA oturumdan destek, adım başına ~5 düzenlemeyi aşma, ve haftalık TOPLU (batched) inceleme — yani "anında md'ye yaz" değil "haftada bir kanıtla gözden geçir" öneriyor. Bu, Anthropic'in resmi "hemen ekle" tavsiyesiyle KISMEN ÇELİŞİYOR — biri anlık, diğeri batched.
Kaynak: https://blog.kunchenguid.com/p/your-agentsmd-is-a-neural-net (AS-OF 2026-09-15, birincil, AÇILDI). Video kaynağı (youtube.com/watch?v=iQyg-KypKAA) doğrudan AÇILAMADI — WebFetch bu URL'ye denenmedi (transkript alma aracı yok, budget içinde atlandı) — BULUNAMADI/erişilmedi olarak işaretliyorum.

---

## İDDİA LİSTESİ
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
