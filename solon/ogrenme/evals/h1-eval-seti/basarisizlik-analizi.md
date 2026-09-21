# H1 koşum hata analizi — 2/20 faıl (2026-09-11, kutu 5 regresyon seti bağı)

Model: `anthropic:messages:claude-haiku-4-5-20251001`. Sonuç: 18/20 `PASS` (%90).

## Vaka A — yüzde artışının tabanı
- Soru: Josh $80.000'a ev alıyor, $50.000 tamirat yapıyor, değer %150 artıyor. Kâr?
- Beklenen: 70000 (referans: artış orijinal alım fiyatına $80.000 uygulanır → yeni değer 200.000, kâr 200.000−130.000).
- Model cevabı: 195000 (artışı toplam maliyete $130.000 uyguladı → 325.000−130.000).
- Kök neden: "değeri %150 artırdı" cümlesindeki referans tabanın (alım fiyatı mı, toplam maliyet mi) belirsizliğini yanlış çözdü. Hesap hatası değil, çerçeveleme hatası.

## Vaka B — başabaş (break-even) sonrası kâra geçiş
- Soru: $90 maliyetli ağaç, yılda $7,5 net kazanç. Kaç yılda "kâr etmeye başlar"?
- Beklenen: 13 (12. yıl sonunda başabaş, kâra geçiş 13. yılda).
- Model cevabı: 12 (bölme işlemini doğru yaptı, +1 break-even mantığını uygulamadı).
- Kök neden: "ne zaman gerçekten kâra geçilir" sınır-durumunu (tam başabaş ≠ kâr) atladı.

## Regresyon seti adayı
Her iki vaka da `contains` ile yakalandı ama *neden* yanlış olduğunu açıklamadı — bu yüzden H3-H4'teki LLM-as-judge/rubrik ihtiyacının somut gerekçesi. Model/prompt değiştiğinde bu iki vaka regresyon seti olarak tekrar koşulabilir: `h1-eval-seti/eval-seti.yaml`'daki 3. ve 13. vakalar (Josh, Carlos).
