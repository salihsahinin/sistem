# Atlas ANTİTEZ Raporu — Aile C (pratisyen kişisel-ajan hafıza pratikleri)

**Tarih:** 2026-09-18
**Rol:** Devil's-Advocate (ANTİTEZ) — yalnız iddia listesi verildi, gerekçesiz; ¬T aranıyor.
**Disiplin:** Rakam kaynaklı; kestirim `[?]`; tarih AS-OF damgalı; uydurma yasak.

---

## İddia 1 — Kun Chen: kullanıcı-md el-yazısı/durağan, proje-md eğitilen "sinir ağı"
**¬T arayışı:** Kaynağın kendisi (birincil) fetch edildi.
**Bulgu:** Blog birebir ayrımı yapıyor: "The user-level file is mine, and I handwrite it... These are preferences I own and they change rarely." / "The project-level file is actually a neural net... it's better to decide on a token budget and train it properly like a neural net."
**Kaynak:** blog.kunchenguid.com/p/your-agentsmd-is-a-neural-net — AS-OF çekim 2026-09-18, yayın tarihi sayfada verilmedi.
**Hüküm:** **ÇÜRÜTÜLEMEDİ** — birincil metin tezi birebir doğruluyor, karşı-kanıt yok.

## İddia 2 — Kun Chen: proje-md yazımı insan onayı olmadan gerçekleşmez
**Bulgu:** Aynı kaynak: "Nothing writes until I review. `backpass apply`... I accept or reject each."
**Kaynak:** aynı, AS-OF 2026-09-18.
**Hüküm:** **ÇÜRÜTÜLEMEDİ.** Not: bu Kun Chen'in KENDİ aracı için geçerli; pratisyenler arasında onaysız otomatik-yazan karşı-örnek arandı, GitHub arama turunda bulunamadı (süre kısıtı; kapsamlı tarama yapılmadı — `[?]`).

## İddia 3 — Kun Chen: sabit token bütçesi (örnek 5.000)
**Bulgu:** Birebir alıntı: "Pick a budget for the always-loaded file, for example 5,000 tokens." — "for example" ifadesi, 5.000'in evrensel/sabit bir kural değil, İLLÜSTRATİF örnek olduğunu gösteriyor.
**Hüküm:** **DARALDI** — sayı doğru alıntılanmış ama "sabit" niteliği zayıf: yazar açıkça "örneğin" diyor, zorunlu tek değer olarak sunmuyor.

## İddia 4 — 466 AGENTS.md'nin %50'si ilk taahhütten sonra hiç güncellenmemiş (2026-05)
**¬T arayışı:** MSR 2026 çalışmasına dayanan ikincil kaynak (Wire Blog) fetch edildi.
**Bulgu:** "50% of AGENTS.md files were unchanged after the initial commit." Yayın 2026-05-18, MSR 2026 (23rd Intl. Conf. on Mining Software Repositories) verisine dayanıyor.
**Kaynak:** usewire.io/blog/agents-md-466-projects-context-engineering/ — AS-OF çekim 2026-09-18.
**Hüküm:** **ÇÜRÜTÜLEMEDİ** — rakam ikincil kaynakta birebir doğrulandı; birincil MSR bildirisi ayrıca açılmadı (kapsam dışı kaldı, `[?]`).

## İddia 5 — Ortalama AGENTS.md uzunluğu 142 satır
**Bulgu:** Aynı kaynak: "AGENTS.md averages 142" lines, karşılaştırmalı olarak "CLAUDE.md averages 287 lines," "Copilot instructions average 310 lines."
**Hüküm:** **ÇÜRÜTÜLEMEDİ.**

## İddia 6 — Anthropic "structured note-taking" bağlam-dışı kalıcı not (2025-09)
**Bulgu:** Anthropic'in kendi mühendislik blogu ("Effective context engineering for AI agents") structured note-taking'i "agent regularly writes notes persisted to memory outside of the context window... pulled back into the context window at later times" olarak tanımlıyor; Pokémon-ajan örneği veriyor.
**Kaynak:** anthropic.com/engineering/effective-context-engineering-for-ai-agents — AS-OF çekim 2026-09-18 (WebSearch üzerinden, doğrudan fetch yapılmadı — tarih 2025-09 iddiası ayrıca doğrulanmadı, `[?]`).
**Hüküm:** **ÇÜRÜTÜLEMEDİ** — içerik doğrulandı; 2025-09 tarih damgası birincil sayfadan teyit edilmedi (zayıf nokta işaretlendi).

## İddia 7 — Anthropic alt-ajan mimarisinde yalnız 1.000-2.000 token özet üst ajana döner
**Bulgu:** Anthropic'in multi-agent research system yazısına dayanan özetler: "Each subagent may use tens of thousands of tokens but returns only a condensed summary (typically 1,000-2,000 tokens) to the lead agent."
**Hüküm:** **ÇÜRÜTÜLEMEDİ** — sayı birebir eşleşiyor, ¬T bulunamadı.

## İddia 8 — Claude Code v2.1.33+ alt-ajan başına ayrı MEMORY.md dizini, dizinler karşılıklı görünmez
**Bulgu:** "Introduced in Claude Code v2.1.33 (February 2026)... `~/.claude/agent-memory/<name>/` (user), `.claude/agent-memory/<name>/` (project)... auto-injects first 200 lines." Hindsight'in kendi blogu (bkz. İddia 12) bunu doğrudan teyit ediyor: "every subagent invocation starts fresh... knowledge stays siloed inside each subagent."
**Hüküm:** **ÇÜRÜTÜLEMEDİ** — iki bağımsız kaynak (mimari doküman + Hindsight'in kendi pazarlama gerekçesi) izolasyonu doğruluyor; sürüm numarası (v2.1.33) birincil Anthropic değişim güncesinden teyit edilmedi (`[?]`).

## İddia 9 — Claude Code otomatik sıkıştırma %83,5 doluluk eşiğinde tetiklenir
**Bulgu:** Çoklu ikincil kaynak: "~83.5% of the total context window." `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` yalnız eşiği DÜŞÜRebiliyor, yükseltemiyor (üst sınır ~83%).
**Hüküm:** **ÇÜRÜTÜLEMEDİ** — resmi Anthropic dokümantasyonu değil, GitHub issue + üçüncü-parti blog konsensüsü; birincil kaynak (kod/resmi doküman) bulunamadı, rakam ikincil-kaynak düzeyinde kalır (`[?]`).

## İddia 10 — LLM-üretilen context dosyaları görev başarısını ~%3 düşürür, maliyeti %20+ artırır (arXiv 2602.11988, 2026-02)
**¬T arayışı:** Birincil kaynak (arXiv özet + HTML gövde) doğrudan açıldı; özellikle T'nin tersini (başarıyı ARTIRAN ölçüm) arandı.
**Bulgu — özet doğrulandı ama sayı DARALTILDI:** Özet: "providing context files does not generally improve task success rates, while increasing inference cost by over 20% on average... holds across different LLMs, coding agents, and for both LLM-generated and developer-committed context files." Gövde (§4.2) kesin rakam veriyor: "the average resolution rate is reduced by 0.5% and 2% on average on SWE-bench Lite and AGENTbench, respectively" — yani iddiadaki "~%3" rakamı BİREBİR değil; gerçek aralık %0,5–%2, iddia bunu yuvarlayarak aşmış.
**Karşı-kanıt arayışı (başarıyı artıran ölçüm):** Aynı makalede alt-bulgu var: "instructions in the context files are well followed by coding agents" — yani context dosyalarındaki AÇIK TALİMATLAR işe yarıyor; zarar veren kısım özellikle "repository overviews" (genel-bakış bölümleri). Bu, T'nin genellemesini kısmen zayıflatır (tüm context dosyası değil, belirli bölüm türü zararlı).
**Kaynak:** arxiv.org/abs/2602.11988 (özet) + arxiv.org/html/2602.11988v1 (§4.2, Tablo 2, Şekil 3) — gönderim 2026-02-12, revize 2026-06-23; AS-OF çekim 2026-09-18.
**Hüküm:** **DARALDI** — yön doğru (zarar var, maliyet +%20 doğru) ama iddianın "~%3" rakamı yanlış/yuvarlanmış (gerçek: %0,5–%2); ayrıca makale zararı bütün dosyaya değil "repository overview" bölümüne yüklüyor — iddia bunu ayrıştırmadan genelliyor.

## İddia 11 — AgentsMesh'te talimat-tetikli ders-hatırlatma başarısız oldu, hook-tetikli recall'a geçildi
**¬T arayışı:** Projenin kendi dev.to yazısı ve GitHub release notları tarandı.
**Bulgu:** Doğrulanabilen tek şey: "In Claude Code, recall is a `PreToolUse` hook. In tools without hooks, the agent runs the query at task start." — yani hook YALNIZ Claude Code gibi hook destekleyen araçlarda var; desteklemeyen araçlarda hâlâ görev-başı (instruction-benzeri) sorgu kullanılıyor — bu bir "geçiş" değil, ARAÇ YETENEĞİNE göre paralel iki mekanizma. Ayrıca release notları hook-tetikli recall'ın KENDİ sorunlarını gösteriyor: "the hook... said nothing when a recall budget was too small... an agent could see 2 of 18 matching lessons with no way to know the other 16 existed" — yani hook-tetikli yöntem de kusursuz değil, sessiz veri kaybı yaşamış ve SONRADAN düzeltilmiş (v0.35→v0.36).
**Kaynak:** dev.to/samplex_283d61d7a (500-lessons yazısı) + github.com/sampleXbro/agentsmesh release v0.35.0/v0.36.0 — AS-OF çekim 2026-09-18.
**Hüküm:** **DARALDI** — "talimat-tetikli başarısız oldu → hook'a geçildi" biçimindeki tek-yönlü göç anlatısı birincil kaynakta yok; gerçek tablo daha karışık (araç-yeteneğine göre ikisi bir arada + hook'un kendi arızası ayrıca giderilmiş). İddia gerçek ama basitleştirilmiş/yanlış nedensellik.

## İddia 12 — Hindsight, Claude Code'un varsayılan subagent-izolasyonunu kırıp paylaşımlı hafıza bankası kurar (2026-05)
**Bulgu:** Birincil kaynak (Hindsight'in kendi blogu) birebir: "every subagent invocation starts fresh, and even when you opt into the persistence features Claude Code does ship, knowledge stays siloed inside each subagent." Çözüm: "instead of N siloed MEMORY.md files, one per subagent, you get a single learning layer everything draws from."
**Kaynak:** hindsight.vectorize.io/blog/2026/05/06/claude-code-subagents-shared-memory — yayın 2026-05-06, AS-OF çekim 2026-09-18.
**Hüküm:** **ÇÜRÜTÜLEMEDİ** — birincil kaynak tezi birebir doğruluyor. Metodolojik uyarı: kaynak Hindsight'in KENDİ ürün-pazarlama yazısı; "izolasyon sorunu" tarifi ürünü satmaya hizmet eden çıkar-çatışmalı bir çerçeveleme olabilir — bağımsız/tarafsız ikinci kaynakla çapraz-doğrulanmadı (İddia 8'deki mimari-doküman dolaylı destekliyor ama Hindsight'in "sorun" çerçevesini değil, yalnız izolasyon OLGUSUNU teyit ediyor).

---

## Genel Değerlendirme

- 12 iddiadan **7'si ÇÜRÜTÜLEMEDİ** (1,2,4,5,6,7,8,9,12 — bazıları ikincil-kaynak zayıflığıyla), **3'ü DARALDI** (3,10,11), **0'ı ÇÜRÜDÜ**.
- Aile C, aile içinde en "sağlam" (solid) çıkan grup: pratisyen ölçümler (Kun Chen, AGENTS.md istatistikleri, Anthropic mimari dokümanları, Hindsight) çoğunlukla birincil kaynakta birebir doğrulanıyor.
- En belirgin aşınma İddia 10'da: popüler aktarımda "%3" yuvarlaması makalenin gerçek %0,5-%2 aralığını ve "yalnız repository-overview bölümü zararlı" nüansını kaybetmiş.
- İddia 11'de nedensellik ("başarısız oldu → geçildi") anlatısı birincil kaynakta doğrulanamadı; gerçek durum yetenek-bazlı paralel kullanım + hook'un kendi arızasının sonradan giderilmesi.
