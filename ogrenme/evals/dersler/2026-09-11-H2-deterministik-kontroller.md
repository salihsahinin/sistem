# Deterministik kontroller: exact/contains/regex/JSON-şema · araç-parametre doğrulaması · maliyet-gecikme — ders 2 (2026-09-11; ogren v0.1)

## Ön-bağlam
H1 dersinden taşınan (aynı oturum, yeniden PROBE edilmedi):
- assert/unit test kavramı: DOĞRU (kutu 1)
- eval ≠ test, `contains` metriği: DOĞRU (kutu 2, 6, 7 — fiilen YAML'da yazıp koşturdu)
- accuracy (temel) biliniyor; **precision/recall sınırı H1'de zaten bulunmuştu: bilinmiyor** (H1 S5) — bu derste sıfırdan işlenecek.
- Cost/Latency/Tokens rakamlarını H1 promptfoo çıktısında GÖRDÜ ("Cost: $0.00066", "Latency: 1.9s") ama henüz tanımlı değil.

## Anlayış haritası
| İplik | Seviye | Kanıt (soru no) |
|---|---|---|
| Regex | yok | S1 |
| JSON şema | temel | S2 (tahmin ✓), S3 (pratik ✗) |
| Araç-parametre doğrulaması | ileri (tavan) | S4 (✓), S7 (✓) |
| Maliyet/gecikme metrikleri | ileri (tavan) | S5 (✓), S6 (✓) |
| precision/recall/F1 | temel (H1'den taşınan) | H1-S4 (accuracy ✓), H1-S5 (precision/recall ✗) |

## Plan
DAG görseli: sohbetteki mcp__visualize çıktısı.

Düğüm listesi (≤8):
1. Regex nedir (sıfırdan)
2. Regex ile eval assert (`type: regex`)
3. JSON şema pratik uygulama (promptfoo'da tip kontrolü)
4. Precision & recall tanımı + 2×2 tablo (İplik "temel"i aşar)
5. F1 skoru formülü
6. Elle 2×2 örnek (Karar 73)
7. Araç-parametre assert türü (kısa — İplik zaten ileri seviyede, pratik promptfoo söz dizimi eklenir)
8. İlk "kırmızı" vaka bilerek üretme + haftalık DONE tanıtımı

## Düğümler
### Kutu 1 — Regex nedir
- Akıl-adımı: regex = kalıba uyup uymadığını kontrol eden söz dizimi; contains'ten farkı: alt-metin değil yapısal kalıp arar.
- Örnek: `^[0-9]+$` — "68" eşleşir, "68 dolar" eşleşmez.
- Soru: `^[0-9]+$`, "yaklaşık 70000" ile eşleşir mi? → Cevap: a (hayır, baştan itibaren yalnızca rakam değil). Sonuç: **DOĞRU**.

### Kutu 2 — Regex ile eval assert (`type: regex`)
- Akıl-adımı: promptfoo'da `assert: - type: regex, value: <kalıp>`; contains sabit alt-metin arar, regex yapı/kalıp arar. (Canlı doğrulandı: promptfoo docs 2026-09-11.)
- Örnek: `value: "\d{4}"` → herhangi bir 4 haneli sayı.
- Soru: herhangi bir 4 haneli yıl kontrolü hangi assert? → Cevap: a. Sonuç: **DOĞRU**.

### Kutu 3 — JSON şema pratik uygulama (`type: is-json`)
- Akıl-adımı: `is-json` geçerli JSON mu diye bakar; opsiyonel `value` şema verirse tip/zorunlu-alan kontrolü de yapar. (Canlı doğrulandı.)
- Örnek: şema `sonuc: number, required` — `{"sonuc":68}` PASS, `{"sonuc":"68"}` FAIL.
- Soru: `{"sonuc":"68"}` (metin) ne olur? → Cevap: a (FAIL, tip uyuşmazlığı). Sonuç: **DOĞRU**.

### Kutu 4 — Precision & recall tanımı + 2×2 tablo
- Akıl-adımı: 2×2 tablo (TP/FP/FN/TN); precision=TP/(TP+FP), recall=TP/(TP+FN).
- Örnek: spam filtresi TP=15,FP=5,FN=3 → precision=0,75, recall≈0,833.
- Soru: TP=8,FP=2 → precision? → Cevap: a (0,8). Sonuç: **DOĞRU**.

### Kutu 5 — F1 skoru
- Akıl-adımı: F1 = 2×(precision×recall)/(precision+recall), harmonik ortalama; precision=recall ise F1 de aynı değer.
- Örnek: spam filtresi precision 0,75/recall 0,833 → F1≈0,79.
- Soru 1: precision=recall=0,8 → Cevap verilen: d (yanlış). Düzeltme yapıldı (adım adım: 2×0,64/1,6=0,8).
- Soru 2 (tekrar, farklı sayı): precision=recall=0,6 → Cevap: a (0,6). Sonuç: **AÇIK** (ilk denemede yanlış, düzeltmeyle doğru).
- Ek örnek (Salih istedi, precision/recall'un ayrışması): arama motoru — Durum A (5 sonuç, hepsi doğru) precision=1,0/recall=0,1; Durum B (500 sonuç, 40 doğru, gerçek 50) precision=0,08/recall=0,8.

### Kutu 6 — Elle 2×2 örnek (Karar 73)
- Sembol tablosu + tam 2×2: TP=6,FP=4,FN=2,TN=8 (halüsinasyon-dedektörü senaryosu, 20 çıktı).
- Precision=0,6, Recall=0,75, F1≈0,667 (hepsi elle hesaplandı).
- Soru: TP=7, gerçek toplam pozitif=10 → FN? → Cevap: a (3). Sonuç: **DOĞRU**.

### Kutu 7 — Araç-parametre assert türü (`type: is-valid-function-call`)
- Akıl-adımı: promptfoo'da araç çağrısının kendi şemasına uyup uymadığını `is-valid-function-call` kontrol eder (kutu 3'teki is-json mantığının araç-çağrısı versiyonu).
- Örnek: `getWeather(sehir:string)` beklerken `getWeather({"sehir":34})` → tip uyuşmazlığı.
- Soru: bu durumda sonuç ne? → Cevap: a (FAIL). Sonuç: **DOĞRU**.

### Kutu 8 — İlk "kırmızı" vaka bilerek üretme
- Akıl-adımı: bilerek FAIL vermesi beklenen vaka = eval altyapısının/assert'in gerçekten çalıştığının kanıtı (TDD "red" aşamasının eval karşılığı).
- Örnek: beklenen değeri kasıtlı yanlış yazmak (23+45=?→"999"), FAIL çıkarsa assert çalışıyor demektir.
- Soru: kırmızı vaka eklemenin amacı? → Cevap: a. Sonuç: **DOĞRU**.
- Salih notu: art arda sorularda doğru cevap hep "a" idi, şık konumu tahmin edilebilir hale geldi → hafızaya kalıcı düzeltme olarak işlendi (feedback-quiz-dogru-cevap-rastgele-konum), bundan sonra rastgele dağıtılacak.

## AÇIK düğümler
- Kutu 5: F1 formülünü ilk denemede yanlış uyguladı (pay/payda karıştı), 2. denemede farklı sayılarla düzeltti.

## Salih notu
- Kutu 5 sonrası: precision/recall ayrımını netleştiren ek karşıt-örnek istendi (arama motoru A/B durumu) — verildi.
- Kutu 8 sonrası: quiz sorularında doğru cevabın hep "a" olması eleştirildi → hafızaya kalıcı kural olarak işlendi (feedback-quiz-dogru-cevap-rastgele-konum), bundan sonraki tüm ogren sorularında şık konumu rastgele olacak.

## Kalan
(yok — 8/8 düğüm işlendi)

## DONE (haftalık çıktı)
- `h2-eval-seti/`: aynı 20 GSM8K vakası (pointer: h1-eval-seti/KAYNAK.md) + 1 bilerek-kırmızı vaka (21 toplam).
- 3 deterministik assert türü dağıtıldı: `contains`×7 (+1 kırmızı vaka) · `regex`×7 · `equals`+`transform`×6.
- Prompt güncellendi: model artık "SONUC: <sayı>" ile bitiriyor (regex/equals'ın güvenilir çalışması için).
- Koşum henüz Salih tarafından çalıştırılmadı — beklenti: 20/21 PASS, vaka 21 (2+2=999 iddiası) FAIL (bu FAIL, assert altyapısının çalıştığının kanıtı).
