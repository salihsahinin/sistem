# m.37 TASLAK — Karar-modeli kuralı (İMZA BEKLİYOR)

> Üretim: 2026-07-13 sabah oturumu. Salih: "imza işini sonraki oturuma bırakıyorum, dosya kalsın." İmzalanınca tüzüğe m.37 olarak girer, bu dosya arşive iner.

**Madde metni (öneri):**
Ölçek eşiğini geçen her kararda (Katman 1 kararları + Katman 2 proje/build ölçekli işler) Carvis 3 seçeneği **matematiksel temelli modellerle** — token×zaman×beklenen-kalite parametreleriyle sayısal — karşılaştırır ve önerileni işaretler; su-bardağı alt-kararlar muaf. Her kararın seçilen modeli + gerçekleşen sonucu `kuyruk/senaryo-defteri.md`'ye işlenir (ingest hammaddesi); tahminler bu veriyle kalibre edilir. **Yakınsama:** bir iş sınıfı "tek promptta çözülür" olgunluğuna ulaştığında (örn. eğitilmiş ajanlar + hazır loop tasarımı tek komutla çıktı veriyor) o sınıf için model-üretimi durur, defterdeki kombinasyon doğrudan uygulanır — optimizasyon hamleleri minimize edilir (Salih, 07-13).

**Format örneği:** Model A (tek Opus vardiyası): ~80K token · ~1 sa · kalite 8/10 · Model B (Haiku keşif + Opus icra): ~50K · ~1.5 sa · 7.5/10 · Model C (3 paralel Haiku + Opus sentez): ~120K · ~40 dk · 8.5/10 → ✅ öneri + tek satır gerekçe.

**Bağlı fikir:** V39 kombinasyon-dizisi deneyi (fikir kutusu) — kararların 1-2-3 seçimleri proje başına dizi üretir (1-3-2-2-1-...), diziler sonuçla skorlanır.

**Çelişki raporu özeti (m.16 gereği sunuldu, 07-13):** "her karar" harfiyen uygulanırsa m.25/m.31 su-bardağı kuralıyla çarpışır + optimizasyon aracı anti-optimizasyona döner → kapsam ölçek-eşiği üstü kararlarla sınırlandı; Salih bu kapsamı sözlü kabul etti, imza bekliyor.


## Kronolojik partisyon — V39/m.37 çerçevesini hayata geçirme adımları (Salih talebi, 07-13)

- **A1 — Zemin (İLK ADIM; sonraki oturum AÇILIŞINA yerleşti):** alt-küme: (a) yerel .git onarımı — temiz klon indir, bozuk .git değiştirilir (mount index'i tutarsız yazıyor, 07-13 tespiti); (b) m.37 taslağını oku → imzala ya da revize (bu dosya); (c) `kuyruk/senaryo-defteri.md`'yi şablonla aç (karar · 3 model tahmini · seçim · gerçekleşen token/süre/kalite); (d) sıfır-noktası kaydı: 07-13 sabah kararları geriye dönük ilk satır. Tahmin: ~15-20 dk. Konum gerekçesi: A2+ tüm fazlar imzaya bağımlı — K-015 loop-eng çalışması BAŞLAMADAN imza atılmalı ki o oturumun kararları deftere aksın; "masada 3 karar" açılış bloğuyla aynı dakikalara oturur.
- **A2 — Elle veri fazı:** ölçek-eşiği kararlarında 3-model formatı fiilen uygulanır; ilk sahne = K-015 (loop-eng Faz 2+4 kararları) + K-002 (PortRisk Sprint 1 kararları). Her karar deftere. Mevcut önceliğe İŞ EKLEMEZ — mevcut işlerin karar anlarına format giydirir.
- **A3 — Otomatik evaluator zemini:** PortRisk done-tanımı makine-ölçülebilir (pytest + metrik; K-002 zaten üretiyor) + koşum-başına token/süre sayacı (V30 sayaçlarıyla aynı aile).
- **A4 — Loop yeteneği:** K-015 loop-eng Faz 2 (/goal) + Faz 4 (Routine) — ilk /goal koşumu = ilk otomatik iterasyon verisi; cc/ kanalının ilk görev emri adayıyla ÇAKIŞIYOR (tek taşla iki borç).
- **A5 — Yeniden-inşa deneyi (TETİKLİ: K-009/K-010):** 1 inşa + ~10 veri koşumu, farklı kombinasyon dizileri; koşum-başına token tavanı + tur limiti şart.
- **A6 — Desen çıkarımı + transfer testi:** biriken veriden öğrenme modeli-deseni → sonraki projede transfer hipotezi ölçülür (V23 disiplini), sonra yakınsama.

Sıralama zaten mevcut öncelik şeridiyle uyumlu: A2-A4, K-015/K-002'nin içinden geçer (paralel yük değil); yalnız A1 yeni ve açılışa kondu.
