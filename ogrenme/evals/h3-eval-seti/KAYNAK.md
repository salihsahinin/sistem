# Kaynak damgası (m.39, md.49)

- Soru metinleri: aynı GSM8K havuzundan 10 vaka (bkz. [`../h1-eval-seti/KAYNAK.md`](../h1-eval-seti/KAYNAK.md), pointer m.20) — 2'si bilinen gerçek hatalar (Josh ev, Carlos limon ağacı; bkz. `../regresyon-seti.yaml`), 8'i çeşitli.
- Prompt: aynı H1 prompt'u yeniden kullanılıyor (`file://../h1-eval-seti/prompt.txt`, pointer).
- Yargıç assert türü (`llm-rubric`) ve provider override söz dizimi canlı doğrulandı: promptfoo docs, AS-OF 2026-09-14.
- Çift-değerlendirme akışı (kutu 4, H3): Salih'in elle puanı, yargıcın verdiğini GÖRMEDEN önce verilmeli — bkz. `AKIS.md`.
