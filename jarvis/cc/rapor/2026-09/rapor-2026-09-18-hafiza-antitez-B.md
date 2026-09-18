# Atlas Antitez Raporu — Aile B (akademik ajan-hafıza literatürü, 2025-2026)

**Tarih:** 2026-09-18
**Rol:** Atlas ANTİTEZ (Devil's Advocate) — yalnız iddia listesi verildi, gerekçe/kaynak bilinmeden ¬T arandı.
**Disiplin:** her kaynak URL'li + AS-OF (yayın · çekim 2026-09-18) + model kuşağı; ≥2 makale WebFetch ile gövdeden açıldı.

---

## İddia 1 — Dört-katmanlı taksonomi evrensel değil, yapı-tabanlı alternatif eksenler var

**¬T arandı:** taksonominin evrensel/standart olduğuna dair kanıt.
**Bulunan:** CoALA çerçevesi (arXiv:2309.02427, Princeton) semantik/epizodik/prosedürel ayrımını LLM ajanlarına formalize etmiş; LangChain/LangGraph dokümantasyonu ve Mem0 "State of AI Agent Memory 2026" raporu aynı üçlüyü (+working) benimsiyor — geniş endüstri benimsemesi var. Ama bu, iddiayı çürütmüyor: "Anatomy of Agentic Memory" (arXiv:2602.19320, çekim 2602.19320v1) kendi "yapı-odaklı" (Lightweight-Semantic / Entity-Centric / Episodic-Reflective / Structured-Hierarchical) dörtlü eksenini sunuyor ve "Rather than advocating a single 'best' design, we provide a diagnostic framework" diyor — CoALA eksenine dayanmayan bağımsız bir eksen. Ayrıca Aralık 2025 survey'i "Memory in the Age of AI Agents" (arXiv:2512.13564) geleneksel taksonomiyi yetersiz bulup Factual/Experiential/Working üçlüsünü öneriyor.
**AS-OF / kuşak:** 2602.19320 (Şub 2026, model-agnostik taksonomi çalışması); 2512.13564 (Ara 2025 survey).
**Hüküm (TEZ hakkında): ÇÜRÜTÜLEMEDİ** — geniş benimseme bulundu ama bağımsız alternatif eksenler de doğrulandı; tez tam desteklendi, ¬T bulunamadı.

## İddia 2 — EvolveMem, LoCoMo/GPT-4o'da %25,7 rölatif F1 kazancı (0,543 vs 0,432)

**¬T arandı:** ham makalede farklı/çelişen sayı, bağımsız tekrar-üretim veya çürütme.
**Bulunan:** arXiv:2605.13941 (HTML gövde, doğrudan açıldı) Tablo 2: EvolveMem F1 0.543, SimpleMem 0.432, rölatif %25,7 — birebir eşleşiyor. Bağımsız tekrar-üretim ya da çürütme bulunamadı (makale Mayıs 2026, taze; henüz takip/replikasyon literatürü yok).
**AS-OF / kuşak:** arXiv:2605.13941, 13 Mayıs 2026, GPT-4o.
**Hüküm: ÇÜRÜTÜLEMEDİ** (sayı doğrulandı, ¬T yok).

## İddia 3 — EvolveMem GPT-5.1'de %36,8 genel, temporal'de %98,9 kazanç

**Bulunan:** aynı makale Tablo 2, GPT-5.1: EvolveMem F1 0.572 vs SimpleMem 0.418 → %36,8; temporal 0.541, +%98,9 rölatif. Birebir eşleşiyor.
**AS-OF / kuşak:** arXiv:2605.13941, GPT-5.1.
**Hüküm: ÇÜRÜTÜLEMEDİ.**

## İddia 4 — EvolveMem MemBench'te GPT-4o %67,9, GPT-5.1 %71,4; baseline'ı %18,9 geçer

**Bulunan:** aynı makale Tablo 3: GPT-4o 67.9% vs baseline 57.1% → %18,9 rölatif; GPT-5.1 71.4% vs baseline 64.3% → %11,0 (GPT-5.1 için iddiadaki "%18,9" rakamı yalnız GPT-4o satırına ait, GPT-5.1'e genellenmemeli — iddia metni bunu zaten GPT-4o'ya bağlıyor, tutarlı).
**Hüküm: ÇÜRÜTÜLEMEDİ.**

## İddia 5 — Nemori format hatası: Qwen-2.5-3B %30,38, gpt-4o-mini %17,91

**Bulunan:** arXiv:2602.19320 (HTML gövde) Tablo 4 birebir: gpt-4o-mini %17.91, Qwen-2.5-3B %30.38; "Silent Failure" olarak adlandırılıyor (malformed JSON/hallucinated keys → yazma başarısızlığı).
**Hüküm: ÇÜRÜTÜLEMEDİ.**

## İddia 6 — F1 semantik kaliteyle uyuşmaz (AMem sıra 4, F1 0,116)

**Bulunan:** aynı makale Tablo 3: "AMem achieves solid semantic performance (Rank 4 across prompts)… yet penalized by F1 (Rank 5, Score 0.116)" — iddiadaki "sıra 4" semantik sıralamaya, F1 0.116 ayrı metriğe ait; birebir doğrulandı.
**Hüküm: ÇÜRÜTÜLEMEDİ.**

## İddia 7 — Hafıza inşa maliyeti 1,3M-7,04M token; MemoryOS 32+ sn/tur

**¬T arandı:** farklı sayı raporlayan bağımsız ölçüm.
**Bulunan:** MemoryOS latency için KAYNAKLAR ARASI ÇELİŞKİ var — "MemForest" karşılaştırması ~2440 sn/soru (13.7× MemForest'in 178 sn'sine göre), RealMem benchmark'ı ise Add Memory Time 14.755 sn + 9201 token/çağrı raporluyor; başka bir kaynak "mostly longer than 17 seconds per case" diyor. "32+ saniye" rakamının hangi kaynaktan geldiği tek bir birincil makalede doğrulanamadı — orijinal MemoryOS makalesinde (arXiv:2506.06326) LoCoMo F1 %49,11 iyileşme raporlanıyor ama aranan gecikme rakamı bulunamadı; "1,3M-7,04M token" rakamı da hiçbir kaynakta birebir doğrulanamadı.
**AS-OF / kuşak:** arXiv:2506.06326 (Mayıs 2025, GPT-4o-mini); karşılaştırma kaynağı MemForest (arXiv:2605.23986, çekim); RealMem (arXiv:2601.06966).
**Hüküm: DARALDI** — bileşen iddialar (yüksek gecikme, yüksek token maliyeti) yönü doğru ama kesin rakamlar ("32+ sn", "1,3M-7,04M token") birincil kaynakta doğrulanamadı; farklı kaynaklar farklı sayı veriyor (14,8 sn – 2440 sn arası geniş aralık).

## İddia 8-11 — Governed Shared Memory (arXiv:2606.24535) sonuçları

- **8. Trust-level-1 arızası:** doğrulandı — Tablo 3, trust=1 ajan "successfully fetched a fleet-1 row"; GET-by-id yolunda scope kontrolü eksik.
- **9. Dedup-önce-çelişki sırası → tespit %49'a düşer:** doğrulandı — "detection rate, all fact-runs (n=200)" = 0.490; senkron dedup kapısı asenkron detektörden önce yazıyı reddediyor.
- **10. Kısmi fleet-filtresi, kesişim-dışı probların %43,9'u kısıtlı satırı gösteriyor:** doğrulandı — semantik arama kesişim-dışı tespit oranı 0.439.
- **11. Doğru yönetişimde sızıntı 0/80, görünürlük %97,5:** doğrulandı — "0/80 (95% Wilson [0.000, 0.046])" ve "117/120 = 0.975".

**Bulunan (hepsi):** arXiv:2606.24535 HTML gövdesi doğrudan açılıp sayılar birebir teyit edildi.
**AS-OF / kuşak:** arXiv:2606.24535, Haziran 2026, MemClaw/ArgusFleet üretim harness.
**Hüküm (8-11): ÇÜRÜTÜLEMEDİ** (dördü de).

## İddia 12 — İnsan-onayı frenlerinin kendini-geliştiren hafızadaki etkisine dair güncel-kuşak somut kanıt yok

**¬T arandı:** insan-onaylı/frenli kendini-geliştiren hafıza için somut deneysel ölçüm (risk azaltma oranı, arıza farkı vb.).
**Bulunan:** SSGM makalesi (arXiv:2603.11768, HTML gövde açıldı) tam olarak bu boşluğu doğruluyor — "Rather than a specific software implementation, SSGM provides a rigorous theoretical architecture" ve üç hipotez (H1-H3) "henüz yürütülmemiş… gelecek araştırma gündemi" olarak sunuluyor; deneysel veri yok. Safety survey'i (arXiv:2606.23075) da somut insan-onayı ölçümü değil, yalnız "co-located scanners saldırıların yalnız %2,5'ini engelliyor" gibi dolaylı/otomatik-savunma bulgusu veriyor; insan-döngü mekanizmasının etkisine dair sayı yok. "A Survey of Self-Evolving Agents" (arXiv:2507.21046) yalnız normatif öneri sunuyor ("approval gates… implemented olmalı"), ölçüm değil.
**AS-OF / kuşak:** arXiv:2603.11768 (Mar 2026, kavramsal); arXiv:2606.23075 (Haz 2026, ampirik ama insan-onayı ölçmüyor); arXiv:2507.21046 (Tem 2025, normatif).
**Hüküm: ÇÜRÜTÜLEMEDİ** — boşluk aranan üç makalede de doğrulandı, karşıt somut ölçüm bulunamadı.

---

## Özet Tablo

| # | Hüküm | Not |
|---|---|---|
| 1 | ÇÜRÜTÜLEMEDİ | geniş benimseme var ama bağımsız alternatif eksenler de doğrulandı |
| 2 | ÇÜRÜTÜLEMEDİ | 0.543/0.432, %25,7 birebir |
| 3 | ÇÜRÜTÜLEMEDİ | %36,8 / temporal %98,9 birebir |
| 4 | ÇÜRÜTÜLEMEDİ | %67,9/%71,4, %18,9 (yalnız GPT-4o) birebir |
| 5 | ÇÜRÜTÜLEMEDİ | %30,38 / %17,91 birebir |
| 6 | ÇÜRÜTÜLEMEDİ | Rank4/F1 0.116 birebir |
| 7 | **DARALDI** | yön doğru, kesin rakamlar ("32+ sn", "1,3-7,04M token") birincil kaynakta doğrulanamadı; kaynaklar arası 14,8-2440 sn geniş aralık |
| 8 | ÇÜRÜTÜLEMEDİ | trust=1 arızası Tablo 3'te birebir |
| 9 | ÇÜRÜTÜLEMEDİ | %49 (n=200) birebir |
| 10 | ÇÜRÜTÜLEMEDİ | %43,9 birebir |
| 11 | ÇÜRÜTÜLEMEDİ | 0/80, %97,5 birebir |
| 12 | ÇÜRÜTÜLEMEDİ | boşluk 3 kaynakta da doğrulandı |

**Açılan kaynak sayısı (gövde WebFetch):** arXiv:2605.13941, 2602.19320, 2606.24535, 2603.11768, 2606.23075, 2609.05441 = **6 makale** gövdeden açıldı (ayrıca 2506.06326, 2606.18829, 2507.21046 yalnız arama/özet düzeyinde tarandı, 2606.18829 PDF-binary nedeniyle gövde okunamadı — 403/format bayrağı).

**403/format bayrağı:** arXiv:2606.24535 ilk denemede PDF-binary format nedeniyle okunamadı, HTML sürümüyle (v1) başarıyla açıldı. arXiv:2606.18829 (GateMem) hem PDF hem tekrar denemede binary kaldı — bu makale bu turda doğrulanamadı.
