# Atlas TEZ — Aile C: Pratisyen Kişisel-Ajan Hafıza Pratikleri

AS-OF (çekim): 2026-09-18. Araştırmacı: atlas (tez rolü). Kapsam: hazır kişisel ajan hafıza büyütme pratikleri (Kun Chen ve benzerleri, çok-ajanlı hafıza izolasyonu, denenip geri alınan desenler, ölçülmüş getiri).

## 1. Kaynak Listesi (açılan = WebFetch ile gerçekten okunan)

| # | Kaynak | URL | Yayın tarihi | Çekim | Model/harness | Açıldı mı |
|---|---|---|---|---|---|---|
| K1 | Kun Chen, "Your AGENTS.md is a Neural Net" | https://blog.kunchenguid.com/p/your-agentsmd-is-a-neural-net | belirtilmemiş (2026 içi, [?]) | 2026-09-18 | Claude Code + özel araç ("backpass", "lavish-axi") | EVET (WebFetch) |
| K2 | Jitpal Kocher / Wire Blog, "What 466 AGENTS.md files teach about context engineering" (MSR 2026) | https://usewire.io/blog/agents-md-466-projects-context-engineering/ | 2026-05-18 | 2026-09-18 | ampirik repo taraması, ajan-agnostik | EVET (WebFetch) |
| K3 | Anthropic, "Effective context engineering for AI agents" | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | 2025-09-29 | 2026-09-18 | Claude Code (genel) | EVET (WebFetch) |
| K4 | orchestrator.dev, "Claude Code & Agent Memory: Best Practices for 2026" | https://orchestrator.dev/blog/2026-04-06--claude-code-agent-memory-2026/ | 2026-04-06 | 2026-09-18 | Claude Code v2.1.92 | EVET (WebFetch) |
| K5 | Simon Willison, notes/tags (llm-memory, claude-code) | https://simonwillison.net/tags/llm-memory/ , https://simonwillison.net/2026/Jul/3/ | 2026-07 (not) | 2026-09-18 | Claude Code, model-override alt-ajan kuralı | KISMEN (WebSearch özeti; doğrudan not sayfası fetch edilmedi — düşük güven) |
| K6 | Gloaguen ve ark., "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?" (ETH Zürih SRI Lab) | https://arxiv.org/abs/2602.11988 | 2026-02 | 2026-09-18 | Claude Code+Sonnet 4.5, Codex+GPT-5.2/GPT-5.1-Mini, Qwen Code+Qwen3-30B | EVET (WebFetch, yalnız abstract — tam metin PDF açılmadı) |
| K7 | Serhii Zhabskyi (samplex), "How we made AI agents actually use their lessons" (AgentsMesh) | https://dev.to/samplex_283d61d7a/how-we-made-ai-agents-actually-use-their-lessons-4gm3 | belirtilmemiş (2026 içi, [?]) | 2026-09-18 | belirtilmemiş model; PreToolUse/PostToolUse hook mekanizması | EVET (WebFetch) |
| K8 | Ben Bartholomew, Hindsight, "Your Claude Code Subagents Don't Share What They Learn" | https://hindsight.vectorize.io/blog/2026/05/06/claude-code-subagents-shared-memory | 2026-05-06 | 2026-09-18 | Claude Code subagent mimarisi | EVET (WebFetch) |
| K9 | claude-mem docs, "Context Engineering" | https://docs.claude-mem.ai/context-engineering | belirtilmemiş | 2026-09-18 | claude-mem (Claude Code eklentisi) | EVET (WebFetch) — sayfa claude-mem'e özgü tetik/bütçe/arşiv verisi İÇERMİYOR (genel compaction anlatımı); ürün-özgü iddia bu kaynaktan ÇIKARILAMADI |

403/paywall: yok. arXiv 2602.11988 tam metni (PDF/HTML) fetch edilmedi, yalnız abstract sayfası okundu — sayısal bulgular (%3, %20+, %4) abstract'tan alınmıştır, tam metinde ek detay olabilir [?].

## 2. Pratik Tablosu

| Pratisyen/Kaynak | Katmanlar | Yazma tetiği | Yazar / onay | Bütçe / sıkıştırma | Bayat kayıt | Çok-ajan izolasyonu |
|---|---|---|---|---|---|---|
| Kun Chen (K1) | Kullanıcı-global md (el yazısı, nadiren değişir) + proje md ("sinir ağı" gibi eğitilen) | **Toplu (batch)** — tekil olaydan sonra değil, veri kümesi birikince ("only when you have a batch of data can you identify what's truly a pattern vs just noise") | Ajan önerir (`backpass apply` → `lavish-axi` öneri listesi) + **insan onayı zorunlu** ("nothing writes until I review") | Sabit token tavanı (örnek: 5.000); yeni satır = eski satırın çıkarılması | Belirtilmemiş | N/A (tek ajan, iki katman: kullanıcı/proje) |
| Anthropic genel pratiği (K3) | CLAUDE.md + bağlam-dışı not (NOTES.md/to-do, "structured note-taking") + compaction özeti + alt-ajan özetleri | Bağlam limiti yaklaşınca (compaction eşik-tetikli); not tutma sürekli/göreve-bağlı | Ajan yazar (otomatik); insan onayı makalede belirtilmemiş | Compaction = özetleyip yeniden başlatma; alt-ajan yalnız 1.000-2.000 token özet döndürür | Belirtilmemiş | Alt-ajan mimarisi: ayrı bağlam, yalnız özet üst ajana döner |
| orchestrator.dev roundup (K4) | CLAUDE.md (statik/insan) + MEMORY.md (oto/dinamik) + Memory Tool (API ajanları) + Subagent Memory (v2.1.33+, ajan-başına kalıcı dizin) | Oturum içi otomatik yazım + periyodik insan gözden geçirme önerisi | Ajan yazar; insan periyodik denetler | CLAUDE.md <300 satır önerisi; proaktif sıkıştırma %60 doluluk, otomatik sıkıştırma %83,5 doluluk | Belirtilmemiş | Subagent-başına ayrı MEMORY.md dizini (v2.1.33+ ile) |
| Wire/Kocher 466-repo taraması (K2) | Her-zaman-okunan AGENTS.md (ort. 142 satır) + talep-üzerine API/tercih dokümanı + oturum-içi durum; 5 yazma-modu tipolojisi (betimleyici/kuralcı/yasaklayıcı/açıklayıcı/koşullu) | İlk commit ile birlikte; sonraki güncelleme çoğunlukla YOK | İnsan (dosya proje ile birlikte repoya taşınır) | Resmî bütçe kuralı gözlenmemiş; ampirik ortalama 142 satır | **%50'si ilk taahhütten sonra hiç güncellenmemiş** → "bağlam bozulması" | N/A (tek repo dosyası, çok-ajan konusu ele alınmıyor) |
| Simon Willison (K5, düşük güven) | Kişisel not/blog + proje AGENTS.md (dar/spesifik, örn. sandbox ağ sınırları) | Elle, karşılaşılan soruna göre | İnsan (kendisi yazıyor) | Dar tutma disiplini (yalnız çıkarımı-zor bilgi) | Belirtilmemiş | Alt-ajanlara model-override kuralı (Sonnet=asıl iş, Haiku=önemsiz düzenleme), karar/inceleme ana döngüde kalıyor |
| Serhii Zhabskyi / AgentsMesh (K7) | Ders dosyası: dosya/komut/sözleşmeyle ilişkili küçük kural grafiği | Önce talimat-tetikli (agent'a "derslerini kontrol et" denildi) → **hook-tetikli** (PreToolUse+PostToolUse, edit öncesi/sonrası otomatik enjeksiyon) | Belirtilmemiş (ajan/insan ayrımı net değil) | Belirtilmemiş | Belirtilmemiş | Belirtilmemiş |
| Hindsight / Ben Bartholomew (K8) | Paylaşımlı hafıza bankası — tüm subagent'lar + orkestratör TEK bankayı kullanır (Claude Code'un varsayılan subagent-başına izolasyonunun KIRILMASI) | Her turda geri-çağırma (recall) + oturum sonu transkript geri-yazma | Otomatik sistem (Hindsight katmanı) | Belirtilmemiş | Belirtilmemiş | KASITLI KIRMA: varsayılan izolasyon (K4'teki subagent-başına dizin) yerine paylaşım |
| claude-mem (K9) | Compaction genel ilkesi anlatılıyor; ürüne özgü katman/tetik/bütçe/arşiv bilgisi sayfada YOK | Belirtilmemiş (bu sayfadan çıkarılamadı) | Belirtilmemiş | Belirtilmemiş | Belirtilmemiş | Belirtilmemiş |

## 3. Denenip Geri Alınan Pratikler

1. **Talimat-tetikli ders hatırlatma → hook-tetikli recall** (K7): "Recall was instruction-gated — a rule told the agent to check its lessons before editing, then trusted it to actually do it. Models don't." Neden: model talimatı hatırlamayı unutuyor; PreToolUse/PostToolUse hook'una geçildi (deterministik enjeksiyon).
2. **Subagent-başına izole hafıza (Claude Code varsayılanı) → paylaşımlı hafıza bankası** (K8): Neden: paralel subagent'lar aynı bulguyu bağımsız yeniden keşfediyor, keşif izi son-mesaj dönüşünde kayboluyor.
3. **LLM-üretilen otomatik context dosyası (`/init` tarzı) → önerilmiyor / kaldırılması öneriliyor** (K6): Neden: ampirik ölçümde başarı oranını düşürüyor ve maliyeti artırıyor (bkz. §4).
4. **Tekil-olaydan sonra anlık CLAUDE.md güncelleme → toplu (batch) inceleme** (K1): Neden: "gürültü mü gerçek örüntü mü" ayrımı tek örnekle yapılamıyor.

## 4. Ölçülmüş Getiriler

- Gloaguen ve ark. (K6, arXiv 2602.11988, AS-OF yayın 2026-02 / çekim 2026-09-18; Claude Code+Sonnet 4.5, Codex+GPT-5.2/GPT-5.1-Mini, Qwen Code+Qwen3-30B): LLM-üretilen context dosyaları görev başarı oranını ortalama **~%3 düşürüyor**, çıkarım maliyetini **%20'den fazla artırıyor**; insan-yazılı/dar dosyalar başarıyı ortalama **~%4 artırıyor**. [Bu rakamlar yalnız abstract'tan alındı, tam metin doğrulanmadı — [?] işareti tam metin okunana dek geçerli.]
- orchestrator.dev (K4, 2026-04-06, Claude Code v2.1.92): otomatik sıkıştırma **%83,5** bağlam doluluğunda tetikleniyor, proaktif sıkıştırma **%60**'ta öneriliyor — bu bir ürün-davranışı tanımı, bağımsız ölçüm çalışması DEĞİL.
- Wire/Kocher (K2, MSR 2026, 2026-05-18, 466 AGENTS.md dosyası ampirik tarama): dosyaların **%50'si** ilk taahhütten sonra hiç güncellenmemiş; ortalama satır sayısı **142**.
- Hindsight (K8, 2026-05-06): "tekrarlayan keşifler yarısında azalır" iddiası VAR ancak makalede **rakamın kaynağı/ölçüm yöntemi belirtilmiyor** — nitel iddia, [?] damgalı, doğrulanmamış sayılmalı.
- Kun Chen (K1) ve orchestrator.dev (K4) genel "zamanla daha verimli hale geliyor" / "sessiz küçük iyileştirmeler" ifadeleri **rakamsız**, ölçüm çalışması değil.

## 5. İDDİA LİSTESİ (numaralı, tek cümle, gerekçesiz, ≤12)

1. Kun Chen kullanıcı-global md'yi el yazısı/nadiren-değişen, proje-md'yi ise toplu veriyle eğitilen bir "sinir ağı" olarak ayırır (K1).
2. Kun Chen'in sisteminde proje-md güncellemeleri insan onayı olmadan yazılmaz (K1).
3. Kun Chen sabit token bütçesi kullanır; örnek olarak 5.000 token verilir (K1).
4. 466 AGENTS.md dosyasının ampirik taramasında dosyaların %50'si ilk taahhütten sonra hiç güncellenmemiştir (K2, MSR 2026, 2026-05-18).
5. Aynı taramada AGENTS.md dosyalarının ortalama uzunluğu 142 satırdır (K2).
6. Anthropic'in "structured note-taking" pratiğinde ajan, bağlam penceresi dışında kalıcı not tutar ve bu notlar sonradan geri çekilir (K3, 2025-09-29).
7. Anthropic'in alt-ajan mimarisinde alt-ajan yalnızca 1.000-2.000 token özet döndürür, ayrıntılı iz üst ajana geçmez (K3).
8. orchestrator.dev'e göre Claude Code v2.1.33+ her alt-ajana kendi kalıcı MEMORY.md dizinini verir ve bu dizinler alt-ajanlar arasında görünmez (K4, 2026-04-06).
9. orchestrator.dev'e göre Claude Code'da otomatik sıkıştırma %83,5 bağlam doluluğunda tetiklenir (K4).
10. Gloaguen ve ark.'ın ampirik çalışmasında LLM-üretilen context dosyaları görev başarısını ortalama ~%3 düşürür ve çıkarım maliyetini %20'den fazla artırır (K6, arXiv 2602.11988, 2026-02).
11. AgentsMesh'in yazarına göre talimat-tetikli ders-hatırlatma modelin talimatı unutması nedeniyle başarısız olmuş, PreToolUse/PostToolUse hook-tetikli recall'a geçilmiştir (K7).
12. Hindsight, Claude Code'un varsayılan subagent-başına izole hafıza mimarisini kasıtlı olarak kırıp tüm subagent ve orkestratörün paylaştığı tek bir hafıza bankası kurar (K8, 2026-05-06).
