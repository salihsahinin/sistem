# Kaynak damgası (m.39, md.49)

- Soru metinleri: aynı GSM8K havuzundan 10 vaka (bkz. [`../h1-eval-seti/KAYNAK.md`](../h1-eval-seti/KAYNAK.md), pointer m.20) — 2'si bilinen gerçek hatalar (Josh ev, Carlos limon ağacı; bkz. `../regresyon-seti.yaml`), 8'i çeşitli.
- Sorular Türkçeye çevrildi (Salih 09-14 talebi: elle puanlama için okunabilir olsun) — sayılar/mantık orijinaliyle birebir, yalnız dil çevirisi; İngilizce orijinaller h1/h2'de değişmeden duruyor.
- Prompt: aynı H1 prompt'u yeniden kullanılıyor (`file://../h1-eval-seti/prompt.txt`, pointer).
- Yargıç assert türü (`llm-rubric`) ve provider override söz dizimi canlı doğrulandı: promptfoo docs, AS-OF 2026-09-14.
- Çift-değerlendirme akışı (kutu 4, H3): Salih'in elle puanı, yargıcın verdiğini **görmeden** önce verilmeli — bkz. `AKIS.md`.
