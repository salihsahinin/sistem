# V26 Örneklem Denetimi — Perspektif Ayrımı Araştırması (2026-09-18)

Rol: V26 örneklem-denetçisi (deterministik, kural-tabanlı). 8 rapor (tez A-D, antitez A-D) sondajlandı. Sondaj kuralı: (a) son üçlükten ≥1 URL'li iddia · (b) tüm sayısal iddialar (rapor başına ilk 6) · (c) son üçlükten ≥1 URL'siz/model-hafızası iddiası. WebFetch: 18/40 kullanıldı.

## Sondaj Tablosu

| Rapor | # | Kural | İddia (kısa) | URL | Hüküm | Not |
|---|---|---|---|---|---|---|
| tez-A | 1 | b | ~2 hata/PR, %58 şiddetli (Code-Review-Loop) | cognition.com/blog/multi-agents-working | TUTTU | birebir alıntı doğrulandı |
| tez-A | 2 | b | "15× more tokens" (çok-ajan vs sohbet) | anthropic.com/engineering/multi-agent-research-system | TUTTU | birebir |
| tez-A | 3 | b | "%90.2" (Opus4 lider+Sonnet4 işçi > tek-ajan Opus4) | anthropic.com/…/multi-agent-research-system | TUTTU | birebir |
| tez-A | 4 | a | Anthropic sıkı-bağımlı/paylaşılan-bağlam işlerde (çoğu kodlama) çok-ajanı uygun görmüyor | aynı | TUTTU | "most coding tasks involve fewer truly parallelizable tasks…not yet great at coordinating" |
| tez-A | 5 | c | "Smart Friend": küçük model kendi kararıyla büyük modele eskale eder | cognition.com/blog/multi-agents-working | TUTTU | birebir |
| tez-B | 6 | b | "%90.2" | anthropic.com/…/multi-agent-research-system | TUTTU | — |
| tez-B | 7 | a | Alt-ajan varsayılan hafızasız, yalnız son mesaj döner | code.claude.com/docs/en/sub-agents + agent-sdk/subagents | TUTTU | iki ayrı sayfada da doğrulandı |
| tez-B | 8 | c | K9 "Instructional Agents" tutor çok-ajan tasarımı | arxiv.org/abs/2508.19611 | TUTTU | başlık/konu/tarih (2025-08-27) doğrulandı |
| tez-B | ek | — | MetaGPT'de QA mühendisi rolü açık mı | github.com/FoundationAgents/MetaGPT | DARALDI | README'de PM/mimar/PM/mühendis var, "QA engineer" açıkça yok |
| tez-C | 9 | b | K2 sayıları (GSM-Hard 61.0/58.8, MMLU 66.7/60.7, Ministral 48.3/20.7/24.7) | arxiv.org/html/2605.00914v1 | TUTTU | tüm rakamlar birebir |
| tez-C | 10 | b | Sycophancy %85.5, terk %70 | aynı | TUTTU | birebir |
| tez-C | 11 | b | TDP %82 azalma, Routine %41→96 | arxiv.org/html/2503.09572v2 (K16 Plan-and-Act) | **TUTMADI** | Bu makalede "TDP", "%82" ya da "%41→96" hiç geçmiyor; makalenin sonucu WebArena-Lite %53.94 başarı — kaynak yanlış eşleştirilmiş |
| tez-C | 12 | a | "Ephemeral Cognition" kavramı (K11) | arxiv.org/pdf/2603.04722 | **TUTMADI** | Terim makalede hiç geçmiyor; makale "Model Medicine" klinik-metafor çerçevesi, konuyla ilgisiz |
| tez-C | 13 | c | K15 "TDP" kaynağı (rapor kendi de "doğrulanamadı" diyor) | URL YOK | **TUTMADI** | rapor kendi düşük-güvenini doğru bildirmiş, ama iddia b#11'de yine de tabloya "K16" ile karıştırılmış |
| tez-D | 14 | b | MEMORY.md ilk 200 satır/25KB sistem promptuna eklenir | code.claude.com/docs/en/sub-agents | TUTTU | birebir |
| tez-D | 15 | b | "%90.2" | anthropic.com/…/multi-agent-research-system | TUTTU | — |
| tez-D | 16 | b | "15×/4×" token çarpanı | aynı | TUTTU | birebir |
| tez-D | 17 | a | Model çözümleme sırası (parametre>frontmatter>env>ana model) | code.claude.com/docs/en/sub-agents | TUTTU | 4 adım birebir |
| tez-D | 18 | c | "Always-On Agents gövdesi çekilemedi, doğrulanamadı" | arxiv.org/abs/2606.30306 | BİLGİ | kaynak şu an tam erişilebilir (403 yok); rapor kendi belirsizliğini dürüst bildirmiş, ama antitez-D'nin "ÇÜRÜDÜ" hükmü doğru çıktı |
| antitez-A | 19 | b | "%90.2" | anthropic.com/…/multi-agent-research-system | TUTTU | — |
| antitez-A | 20 | b | "2 bugs/PR, %58 severe" | cognition.com/blog/multi-agents-working | TUTTU | — |
| antitez-A | 21 | b | Opus5 subagent limitleri varsayılan: depth=3, concurrency=20 | code.claude.com/docs/en/agent-sdk/subagents | TUTTU | birebir |
| antitez-A | 22 | a | Opus 4.6 Agent Teams / C-compiler örneği (2026-02-05) | anthropic.com/engineering/building-c-compiler | TUTTU | tarih, alıntı, Docker/kilit/GCC-oracle mekanizması doğrulandı |
| antitez-A | 23 | c | Cursor blog "yayın tarihi sayfada açık değil [?]" | cursor.com/blog/plan-mode | **TUTMADI** | sayfada tarih açıkça var: "7 Ekim 2025" |
| antitez-B | 24 | a/b | "%90.2" + paralellik/sıkıştırma alıntısı | anthropic.com/…/multi-agent-research-system | TUTTU | — |
| antitez-B | 25 | b | "MEMORY.md invisible…isolation is by design" | code.claude.com/docs/en/sub-agents | **TUTMADI** | Güncel ham metinde bu cümle yok ("Hayır, bu ifade dokümantasyonda geçmiyor") |
| antitez-B | 26 | b | model alanı varsayılanı "inherit" | code.claude.com/docs/en/sub-agents | **TUTMADI** | Güncel dok: "Hayır…varsayılan inherit değil, çözümleme sırası uygulanır" — doğrudan çelişiyor |
| antitez-B | 27 | c | Deepwatch red-team ajanı tanımı, ayrı kalıcı sınıf | deepwatch.com/glossary/red-team-agent… | TUTTU | birebir + "ayrı sınıf" çerçevesi doğrulandı |
| antitez-C | 28 | b | Gemini-2.5-Pro 5000 token: Sequential %66.0 > tek-ajan %60.0 (çok-ajan üstün) | arxiv.org/html/2604.02460v1 | **TUTMADI** | Ham veri TERS: SAS(tek-ajan)=70.0, Sequential=68.0 — tek-ajan daha yüksek; rakam+yön hatalı |
| antitez-C | 29 | b | Heterojenlik "universal antidote", 4 foundational model | arxiv.org/abs/2502.08788 | TUTTU | birebir, isim verilmediği de doğru |
| antitez-C | 30 | a | "Ephemeral Cognition" (K11) doğrulaması | arxiv.org/pdf/2603.04722 | **TUTMADI** | terim makalede yok (bkz. tez-C #12) |
| antitez-C | 31 | b | PETITE: %31.62/5277tok, MAD %28.97/23630tok, Self-Refine %27.59/15285tok, verimlilik 5.99/1.23 | arxiv.org/html/2604.08931 | TUTTU | tüm rakamlar birebir |
| antitez-D | 32 | b | Memory 200 satır/25KB + Read/Write/Edit otomatik açılır | code.claude.com/docs/en/sub-agents | TUTTU | — |
| antitez-D | 33 | b | "Agents cannot access each other's memory directories. This isolation is by design." | code.claude.com/docs/en/sub-agents | **TUTMADI** | aynı bulgu #25 ile — cümle güncel dokta yok |
| antitez-D | 34 | b | "%90.2" + Sonnet4/3.7 + 15×/4× | anthropic.com/…/multi-agent-research-system | TUTTU | — |
| antitez-D | 35 | a | Always-On Agents erişilebilirliği | arxiv.org/abs/2606.30306 | TUTTU | erişilebilir, 2026-06-29, yazarlar eşleşiyor |

## Rapor Başına Özet

| Rapor | Sondaj | TUTTU | TUTMADI | ERİŞİLEMEDİ/BİLGİ |
|---|---|---|---|---|
| tez-A | 5 | 5 | 0 | 0 |
| tez-B | 4 | 3 | 0 | 1 (DARALDI) |
| tez-C | 5 | 2 | 3 | 0 |
| tez-D | 5 | 4 | 0 | 1 (BİLGİ) |
| antitez-A | 5 | 4 | 1 | 0 |
| antitez-B | 4 | 2 | 2 | 0 |
| antitez-C | 4 | 2 | 2 | 0 |
| antitez-D | 4 | 3 | 1 | 0 |

## TUTMADI ≥1 olan raporlar (hakemde K'ya düşer)

- **tez-C**: K16/K15 (Task-Decoupled Planning, %82, %41→96) yanlış kaynağa bağlanmış; K11 "Ephemeral Cognition" terimi kaynakta yok.
- **antitez-A**: Cursor blog tarih-görünürlüğü iddiası yanlış (tarih sayfada açık).
- **antitez-B**: iki ayrı Claude Code doküman alıntısı ("isolation by design", "model varsayılanı inherit") güncel ham metinde bulunamadı.
- **antitez-C**: Gemini-2.5-Pro FRAMES rakamı ters aktarılmış (yön hatası: tek-ajan aslında üstün); "Ephemeral Cognition" kaynak-eşleşme hatası tez-C ile aynı kök.
- **antitez-D**: "isolation by design" alıntısı antitez-B ile aynı kaynak hatasını tekrarlıyor.

Tam dosya: `/Users/HasanSalihSahin/sistem/jarvis/cc/rapor/2026-09/rapor-2026-09-18-perspektif-v26-denetim.md`
