# ANTİTEZ RAPORU — Aile A (statik/durumsuz lider) — IB-75

**Künye:** Rol: Antitez işçisi (Devil's Advocate). Tarih: 2026-09-09. Araç çağrısı: 9. Birincil kaynak açma: 3 (cognition.com/blog, arxiv.org/pdf/2503.13657, research.google/blog).

## İddia Başına Hüküm

**A1** (statik dosya-içi rol tanımı yeterlidir) — **DARALTILDI**
- K: MAST taksonomisi "specification issues" (belirsiz/eksik rol tanımı) 3 ana kategoriden biri; 5 popüler açık-kaynak MAS çerçevesinde (HyperAgent, AppWorld, AG2, ChatDev, MetaGPT) 150 iz üzerinden ampirik olarak belgelendi — D — https://arxiv.org/abs/2503.13657 — AS-OF 2025-03 (çekim 2026-09-09). Kesin yüzde MAST PDF'inden çıkarılamadı (sıkıştırılmış metin) — `[?]`.

**A2** (description/çağrı-koşulu güvenilir rota-ipucu) — **DARALTILDI**
- K: İki-atlama (hop) zincirinde her atlama %95 rota doğruluğuyla bile uçtan uca doğruluk ~%90'a düşüyor; hatalar birikimli — D — https://www.patronus.ai/ai-agent-development/ai-agent-routing — AS-OF çekim 2026-09-09 (yayın tarihi sayfada görünmedi, `[?]`).
- K: "En maliyetli başarısızlıklar tipik olarak belirsiz alan sınırlarında yanlış-yönlendirmeden kaynaklanır" — D — aynı kaynak.
- Karşı-not: aynı kaynak LLM-tabanlı yönlendiricilerin >%90 doğruluk + <%3 yanlış-geçiş oranına ulaşabildiğini de söylüyor — bu A2'yi kısmen destekler, tam çürütme değil, DARALTMA olarak işaretlendi.

**A3** (alt-ajan varsayılan durumsuzdur ve bu tercih edilir) — **DARALTILDI**
- K: Cognition'ın "Flappy Bird" örneği: paralel alt-ajanlar birbirinin bağlamını görmediği için çelişen örtük kararlar üretiyor (biri Mario arka planı, öbürü oyun-dışı kuş çiziyor) — D — https://cognition.com/blog/dont-build-multi-agents — AS-OF 2025-06-12.
- Doğrudan alıntı: "Share context, and share full agent traces, not just individual messages." — bu, "durumsuzluk tercih edilir" önermesinin TERSİNİ savunuyor.

**A4** (öğrenen/hafızalı lidere gerek yok, dosya-düzenle+yeniden-yükle yeterli) — **ÇÜRÜTÜLDÜ (kısmi, sayısal)**
- K: ReasoningBank (Google Research) — deneyimden öğrenen hafıza katmanı eklenen ajan, hafızasız temel ajana göre WebArena'da +%8.3, SWE-Bench-Verified'da +%4.6 başarı oranı artışı; ayrıca SWE-Bench-Verified'da görev başına ~3 adım daha az — D — https://research.google/blog/reasoningbank-enabling-agents-to-learn-from-experience/ — AS-OF 2026-04-21.
- Not: Bu, "statik lider" değil "statik AJAN" karşılaştırması; A4'ün "liderin öğrenmesine gerek yok" iddiasına dolaylı ama net karşı-kanıt (öğrenen bileşen ekleme somut kazanç veriyor).

**A6** (delegasyon varsayılan kapalı olmalı) — **ÇÜRÜTÜLEMEDİ**
- Bu iddiayı doğrudan yanlışlayan/daraltan kaynak arama bütçesi içinde bulunamadı. "Delegasyon varsayılan açık olmalı" yönünde ölçümlü bir karşı-çalışmaya rastlanmadı — meşru sonuç: bu iddia mevcut taramada sağlam çekirdek sayılabilir.

**A10** (supervisor deseninde tam mesaj geçmişi devri iyi çalışır) — **DARALTILDI**
- K: Cognition, yalnız "individual messages" değil "full agent traces" paylaşımı gerektiğini savunuyor — tam mesaj geçmişi devrinin TEK BAŞINA yeterli olmadığını ima ediyor (mesaj ≠ iz) — D — https://cognition.com/blog/dont-build-multi-agents — AS-OF 2025-06-12.
- K: MAST'ın "inter-agent misalignment" kategorisi (150 iz, 5 popüler çerçeve, kappa=0.88 yüksek anlaşma) supervisor dahil desenlerde gerçek başarısızlıkları ampirik belgeliyor — D — https://arxiv.org/abs/2503.13657 — AS-OF 2025-03.

**A11/A12** (durum-tutan orkestratör ∨ araç-olarak-ajan — ikisi de iyi çalışan kurulu desenler) — **DARALTILDI**
- K: Aynı MAST verisi bu desenleri kullanan gerçek popüler çerçevelerde (ChatDev, MetaGPT, AG2, AppWorld, HyperAgent) sistematik başarısızlık kalıpları belgeliyor; "iyi çalışır" iddiası koşulsuz değil — D — https://arxiv.org/abs/2503.13657 — AS-OF 2025-03.

## Açılan Kaynaklar (WebFetch ile fiilen açılan)
1. https://cognition.com/blog/dont-build-multi-agents (2025-06-12)
2. https://arxiv.org/abs/2503.13657 + https://arxiv.org/pdf/2503.13657 (2025-03, PDF sıkıştırma nedeniyle sayısal tablo tam çıkarılamadı)
3. https://research.google/blog/reasoningbank-enabling-agents-to-learn-from-experience/ (2026-04-21)
(github.com/multi-agent-systems-failure-taxonomy/MAST açıldı ama içerik boş/navigasyon döndü — sayılmadı)

## AÇIK SORULAR
- AÇIK SORU: MAST'ın 14 başarısızlık modunun tam yüzde dağılımı (özellikle "specification issues" payı) PDF sıkıştırmasından çıkarılamadı; HuggingFace MAD veri setinden doğrudan sayısal tablo çekilmedi (bütçe dışı kaldı).
- AÇIK SORU: A6 (delegasyon varsayılan kapalı) için doğrudan karşı-kanıt bulunamadı — ayrı bir taramada "agent tool permission default" / "sub-agent autonomous delegation risk" hattı denenebilir.
- AÇIK SORU: Patronus.ai rota-doğruluk rakamlarının (%90, <%3) yayın tarihi sayfada görünmedi — AS-OF yalnız çekim tarihiyle işaretlendi, kaynağın kendi tarihi doğrulanmadı.
