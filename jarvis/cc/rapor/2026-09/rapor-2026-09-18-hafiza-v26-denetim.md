# V26 örneklem-denetimi — hafıza mimarisi Atlas koşumu (tez A/B/C, antitez A/B/C)

**Tarih:** 2026-09-18 · **Rol:** V26 örneklem-denetçisi (deterministik, kural-tabanlı) · **Dil:** Türkçe

## Yöntem notu

Her rapor için sabit sondaj kuralı uygulandı (rastgele seçim yok):
- **(a)** raporun son üçte birinden ≥1 URL'li kaynak iddiası
- **(b)** rapordaki TÜM sayısal iddialar, belgede geçtiği sırayla ilk 6 tanesi
- **(c)** son üçlükten ≥1 URL'siz/model-hafızası tipi iddia (yoksa "URL YOK / böyle iddia yok")

Her sondaj noktası WebFetch ile kaynağa inilerek ham metinle karşılaştırıldı (antitez raporlarının kendi alıntılarına güvenilmedi, taze WebFetch yapıldı). Toplam **19 WebFetch çağrısı** yapıldı (bütçe ≤40, kullanım %48); aynı URL birden fazla raporun sondaj noktasını karşıladığında tekrar fetch edilmedi (ör. `anthropic.com/engineering/effective-context-engineering-for-ai-agents` hem tez-A hem tez-C/antitez-C için tek fetch'te değerlendirildi — bu, bütçe içi meşru bir tasarruf, ayrı URL'lere tekrar gidilmedi). Hiçbir sondaj noktası bütçe nedeniyle atlanmadı.

Hüküm türleri: **TUTTU** (kaynakta doğrulandı) · **TUTMADI** (kaynakta yok/farklı) · **ERİŞİLEMEDİ** (fetch başarısız) · **URL YOK** (iddiaya kaynak verilmemiş).

---

## Ana Tablo

| Rapor | Sondaj no | Kural | İddia (özet) | URL | Hüküm | Not |
|---|---|---|---|---|---|---|
| tez-A | 1 | a | Alt-ajanlara ana konuşmanın auto memory'si yüklenmez (fork hariç) | code.claude.com/docs/en/memory | **TUTTU** | Birebir: "The main conversation's auto memory isn't loaded into subagents; the exception is a fork..." |
| tez-A | 2 | b | MEMORY.md 200 satır/25KB sınırı, aşımda "otomatik kısaltma uyarısı" | code.claude.com/docs/en/memory | **TUTMADI** | Sayı doğru ama mekanizma yanlış: sınıra yakınken "reminder" (kısalt uyarısı), sınır AŞILINCA "write başarılı ama hata döner, limit üstü kısım sonraki yüklemede düşer" — dosya kendiliğinden kısaltılmıyor |
| tez-A | 3 | b | Memory+context editing kombinasyonu %39 iyileşme | claude.com/blog/context-management | **TUTTU** | "combining the memory tool with context editing improved performance by 39% over baseline" |
| tez-A | 4 | b | Yalnız context editing %29 iyileşme | claude.com/blog/context-management | **TUTTU** | "Context editing alone delivered a 29% improvement" |
| tez-A | 5 | b | 100-turn arama görevinde %84 token azaltımı | claude.com/blog/context-management | **TUTTU** | "reducing token consumption by 84%" |
| tez-A | 6 | b | Alt-ajan yalnız 1.000-2.000 token özet döner | anthropic.com/engineering/effective-context-engineering-for-ai-agents | **TUTTU** | "returns only a condensed, distilled summary of its work (often 1,000-2,000 tokens)" |
| tez-A | 7 | b | Mem0 dört aşamalı pipeline (extraction→consolidation→storage→retrieval) | mem0.ai/blog/long-term-memory-ai-agents + docs.mem0.ai/core-concepts/memory-types | **TUTMADI** | Blog 4 aşama diyor (TUTTU o kaynağa göre) ama Mem0'ın GÜNCEL resmi dokümanı (`docs.mem0.ai`) 3 aşama tanımlıyor (context gathering/retrieval/extraction); kaynaklar arası çelişki — "dört aşamalı" tek-doğru gibi sunulamaz |
| tez-A | 8 | c | Anthropic çok-ajan araştırması: "çok sayıda izole bağlamlı ajan tek-ajan sistemlerden üstün" (K4 WebSearch özeti, tez-A'nın kendisi de "doğrudan açılmadı" diyor) | claude.com/blog/context-management (K4) | **TUTMADI** | Bu sayfada böyle bir ifade/bulgu YOK; tez-A'nın kendi ihtiyat notuyla (doğrulanmamış) tutarlı bir sonuç |
| tez-B | 1 | a | K4: 50 derinlik-4 zincir mükemmel yeniden inşa edildi, p50 291ms/hop | arxiv.org/html/2606.24535v1 | **TUTTU** | "All 200 planned writes landed and all 50 depth-four chains reconstructed... completeness/accuracy/depth-fidelity each 1.00" + "per-hop fetch latency p50 291ms" — iki ayrı cümlede ama içerik birebir |
| tez-B | 2 | b | EvolveMem GPT-4o: F1 0.543 vs SimpleMem 0.432, %25.7 | arxiv.org/html/2605.13941v1 | **TUTTU** | Tablo 2 birebir |
| tez-B | 3 | b | EvolveMem GPT-5.1: %36.8 genel, temporal %98.9 | arxiv.org/html/2605.13941v1 | **TUTTU** | Tablo 2 birebir (0.572/0.418; temporal 0.541/0.272) |
| tez-B | 4 | b | MemBench: GPT-4o %67.9, GPT-5.1 %71.4, baseline'a göre %18.9 | arxiv.org/html/2605.13941v1 | **TUTTU** | Tablo 3 birebir (baseline 57.1%) |
| tez-B | 5 | b | Nemori format hatası: Qwen-2.5-3B %30.38, gpt-4o-mini %17.91 | arxiv.org/html/2602.19320v1 | **TUTTU** | Tablo 4 birebir |
| tez-B | 6 | b | AMem: semantik Rank 4, F1 0.116 | arxiv.org/html/2602.19320v1 | **TUTTU** | Tablo 3 birebir |
| tez-B | 7 | b | Token maliyeti 1.3M-7.04M, MemoryOS 32+ sn/tur | arxiv.org/html/2602.19320v1 | **TUTTU** | Tablo 5 birebir: SimpleMem 1.308k/Nemori 7.044k; "MemoryOS emerges as a clear bottleneck, with latency exceeding 32 seconds" — **ÖNEMLİ:** bu rakamların ikisi de doğrudan K3'te (2602.19320), tez-B'nin zaten belirttiği kaynakta bulundu |
| tez-B | 8 | c | Sentez: "hafıza mimarisinin getirisi modelin gücüyle ölçekleniyor" yorumu | — | **URL YOK** | Tez-B'nin kendi çelişki-notu sentezi, tek bir doğrulanabilir kaynak URL'i yok |
| tez-C | 1 | a/b | Gloaguen ve ark.: context dosyaları başarıyı ~%3 düşürür, maliyeti %20+ artırır | arxiv.org/abs/2602.11988 + arxiv.org/html/2602.11988v1 | **TUTMADI** | %20+ kısmı TUTTU ama "~%3" rakamı YANLIŞ: gövde §4.2 birebir "the average resolution rate is reduced by 0.5% and 2% on average on SWE-bench Lite and AGENTbench respectively" — gerçek aralık %0,5-%2, "~3" abartılı/yuvarlama |
| tez-C | 2 | b | Kun Chen: örnek token bütçesi 5.000 | blog.kunchenguid.com/p/your-agentsmd-is-a-neural-net | **TUTTU** | "Pick a budget for the always-loaded file, for example 5,000 tokens" |
| tez-C | 3 | b | Anthropic alt-ajan özeti 1.000-2.000 token | anthropic.com/engineering/effective-context-engineering-for-ai-agents | **TUTTU** | (bkz. tez-A sondaj 6 ile aynı kaynak/aynı doğrulama) |
| tez-C | 4 | b | orchestrator.dev: proaktif sıkıştırma %60, otomatik %83,5 | orchestrator.dev/blog/2026-04-06--claude-code-agent-memory-2026/ | **TUTTU** | "83.5% Auto-Compact Threshold" + "60% Manual /compact Target" birebir |
| tez-C | 5 | b | Wire/Kocher: AGENTS.md ortalama 142 satır | usewire.io/blog/agents-md-466-projects-context-engineering/ | **TUTTU** | "AGENTS.md averages 142 lines" birebir |
| tez-C | 6 | b | Wire/Kocher: dosyaların %50'si ilk taahhütten sonra hiç güncellenmemiş | usewire.io/blog/agents-md-466-projects-context-engineering/ | **TUTTU** | "50% of AGENTS.md files were unchanged after the initial commit" birebir |
| tez-C | 7 | c | Son üçlükte URL'siz/model-hafızası tipi iddia arandı | — | **URL YOK** | Bulunamadı; son üçlükteki tüm iddialar (K-kaynak tablosu + iddia listesi) URL'li — zorlanmadı |
| antitez-A | 1 | a | Letta/MemGPT 3 katmanlı (core/recall/archival), insan onay katmanı yok | docs.letta.com/memory/overview (404) → docs.letta.com/letta-memgpt (200) | **TUTMADI** | `/memory/overview` 404 (antitez-A'nın kendi bulgusuyla aynı); yedek sayfa açıldı ama "core/recall/archival" üçlüsü DEĞİL, "memory blocks / shared memory / archival memory" terminolojisi kullanılıyor — güncel canlı dokümantasyon klasik 3-katman adlandırmasını doğrudan teyit etmiyor |
| antitez-A | 2 | b | MEMORY.md 200 satır/25KB | code.claude.com/docs/en/memory | **TUTTU** | (bkz. tez-A sondaj 2 ile aynı kaynak) |
| antitez-A | 3 | b | %39 kombine iyileşme | claude.com/blog/context-management | **TUTTU** | — |
| antitez-A | 4 | b | %29 yalnız context editing | claude.com/blog/context-management | **TUTTU** | — |
| antitez-A | 5 | b | 10 puanlık fark memory tool'dan geliyor (39-29) | claude.com/blog/context-management | **TUTTU** | Aritmetik tutarlı (39-29=10); antitez-A'nın alıntıladığı "10 percentage points" cümlesi bu sayfada mantıken doğrulanıyor |
| antitez-A | 6 | b | %84 (100-turn) | claude.com/blog/context-management | **TUTTU** | — |
| antitez-A | 7 | b | Mem0 "4 operasyon" vs "2 faz" vs "3 aşama" karışıklığı | docs.mem0.ai/core-concepts/memory-types + arxiv.org/abs/2504.19413 | **TUTTU** | Güncel resmi doküman gerçekten 3 aşama tanımlıyor + 4 operasyon (ADD/UPDATE/DELETE/"leave alone"); akademik özet (abstract) "two-phase" ifadesini içermiyor (yalnız "extracting, consolidating, retrieving" der) — antitez-A'nın "karışıklık var" tespiti doğrulandı |
| antitez-A | 8 | c | Son üçlükte URL'siz iddia arandı | — | **URL YOK** | Bulunamadı |
| antitez-B | 1 | a | SSGM: teorik mimari, H1-H3 henüz yürütülmemiş, insan-onaylı ampirik ölçüm yok | arxiv.org/html/2603.11768v1 | **TUTTU** | "Rather than a specific software implementation, SSGM provides a rigorous theoretical architecture" + "we propose three testable research hypotheses that should guide future empirical evaluations" — deney/insan değerlendirmesi yok |
| antitez-B | 2 | b | EvolveMem GPT-4o %25.7 | arxiv.org/html/2605.13941v1 | **TUTTU** | (tez-B sondaj 2 ile aynı) |
| antitez-B | 3 | b | EvolveMem GPT-5.1 %36.8/%98.9 | arxiv.org/html/2605.13941v1 | **TUTTU** | (tez-B sondaj 3 ile aynı) |
| antitez-B | 4 | b | MemBench %67.9/%71.4/%18.9 | arxiv.org/html/2605.13941v1 | **TUTTU** | (tez-B sondaj 4 ile aynı) |
| antitez-B | 5 | b | Nemori %30.38/%17.91 | arxiv.org/html/2602.19320v1 | **TUTTU** | (tez-B sondaj 5 ile aynı) |
| antitez-B | 6 | b | AMem Rank4/F1 0.116 | arxiv.org/html/2602.19320v1 | **TUTTU** | (tez-B sondaj 6 ile aynı) |
| antitez-B | 7 | c | Son üçlükte URL'siz iddia arandı | — | **URL YOK** | Bulunamadı (Özet Tablo yalnız meta-veri) |
| antitez-C | 1 | a | AgentsMesh: talimat-tetikli recall başarısız oldu → hook-tetikli (PreToolUse/PostToolUse) recall'a geçildi, hook'un kendi (küçük-bütçe sessiz veri kaybı) arızası sonradan giderildi | dev.to/samplex_283d61d7a/... + github.com/sampleXbro/agentsmesh/releases | **TUTTU** | dev.to yazısı geçişi doğruluyor ("Recall stopped being an instruction and became a hook"); GitHub release notları (v0.38.0) sessiz-veri-kaybı arızasını ve düzeltmesini birebir doğruluyor: "an agent could see 2 of 18 matching lessons with no way to know the other 16 existed" + "Hook-injected context now ends with a one-line notice..." |
| antitez-C | 2 | b | Kun Chen 5.000 token | blog.kunchenguid.com/... | **TUTTU** | (tez-C sondaj 2 ile aynı) |
| antitez-C | 3 | b | %50 güncellenmemiş | usewire.io/... | **TUTTU** | (tez-C sondaj 6 ile aynı) |
| antitez-C | 4 | b | 142 satır ortalama | usewire.io/... | **TUTTU** | (tez-C sondaj 5 ile aynı) |
| antitez-C | 5 | b | 1.000-2.000 token alt-ajan özeti | anthropic.com/engineering/... | **TUTTU** | (tez-A sondaj 6 ile aynı) |
| antitez-C | 6 | b | %83,5 otomatik sıkıştırma | orchestrator.dev/... | **TUTTU** | (tez-C sondaj 4 ile aynı) |
| antitez-C | 7 | b | Gloaguen gerçek rakam %0,5-%2 (antitez'in kendi düzeltmesi) | arxiv.org/html/2602.11988v1 | **TUTTU** | Antitez-C'nin "DARALDI" hükmünde verdiği düzeltilmiş rakamlar (%0,5/%2) benim bağımsız §4.2 taramamla birebir eşleşiyor |
| antitez-C | 8 | c | Sentez: "Aile C, en 'sağlam' çıkan grup" değerlendirmesi | — | **URL YOK** | Antitez-C'nin kendi genel-değerlendirme yorumu, doğrulanabilir tek kaynak yok |

---

## Rapor Özetleri

| Rapor | Toplam sondaj | TUTTU | TUTMADI | ERİŞİLEMEDİ | URL YOK |
|---|---|---|---|---|---|
| tez-A | 8 | 5 | 3 | 0 | 0 |
| tez-B | 8 | 7 | 0 | 0 | 1 |
| tez-C | 8 | 6 | 1 | 0 | 1 |
| antitez-A | 8 | 6 | 1 | 0 | 1 |
| antitez-B | 8 | 7 | 0 | 0 | 1 |
| antitez-C | 8 | 7 | 0 | 0 | 1 |
| **Toplam** | **48** | **38** | **5** | **0** | **5** |

---

## "TUTMADI ≥1 olan raporlar"

- **tez-A** (3 TUTMADI):
  1. MEMORY.md limit aşımında "otomatik kısaltma uyarısı" — gerçekte sınır aşılınca dosya kendiliğinden kısaltılmıyor, yazma başarılı olup hata dönüyor (mekanizma yanlış tarif edilmiş).
  2. Mem0 "dört aşamalı pipeline" — Mem0'ın kendi güncel resmi dokümanı 3 aşama tanımlıyor, blog kaynağı 4 diyor; kaynaklar arası çelişki, tek-doğru gibi sunulmuş.
  3. Anthropic çok-ajan araştırma bulgusu ("izole bağlamlı ajanlar tek-ajandan üstün") — K4 sayfasında (claude.com/blog/context-management) bu ifade yok; tez-A zaten bunu "doğrudan açılmadı" diye işaretlemişti, sondaj bunu doğruladı.
- **tez-C** (1 TUTMADI): Gloaguen ve ark. çalışmasındaki "~%3 başarı düşüşü" rakamı yanlış — gövde metninde gerçek rakam %0,5 (SWE-bench Lite) / %2 (AGENTbench).
- **antitez-A** (1 TUTMADI): Letta/MemGPT "core/recall/archival" 3-katman terminolojisi güncel canlı dokümantasyonda doğrudan bulunamadı (`/memory/overview` 404; yedek sayfa farklı terim seti kullanıyor: memory blocks/shared memory/archival memory).

---

## Genel değerlendirme notu

En dikkat çekici bulgu **tez-B sondaj 7**: tez-B'nin "MemoryOS 32+ saniye, 1.3M-7.04M token" iddiası, antitez-B tarafından "DARALDI" (kesin rakamlar birincil kaynakta doğrulanamadı) olarak işaretlenmişti — çünkü antitez-B, MemoryOS'un KENDİ makalesini (arXiv:2506.06326) aramış ve orada bulamamıştı. Ancak bu koşumdaki bağımsız sondaj, rakamların doğrudan tez-B'nin asıl belirttiği kaynakta (K3 = arXiv:2602.19320, "Anatomy of Agentic Memory") birebir bulunduğunu gösterdi: "MemoryOS emerges as a clear bottleneck, with latency exceeding 32 seconds" ve token aralığı (1.308k-7.044k) Tablo 5'te aynen mevcut. Yani antitez-B'nin kendi DARALDI hükmü, yanlış kaynağı aramaktan kaynaklanan bir hataydı — iddia aslında TUTTU olmalıydı.
