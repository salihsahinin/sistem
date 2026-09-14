# H3 DONE — çift-değerlendirme akışı (kutu 4: bağımsızlık şartı)

Amaç: aynı 10 vakayı hem sen (insan) hem de yargıç LLM bağımsız puonlasın, sonra Cohen κ (kutu 6) ile karşılaştıralım.

## Adım 1 — kör çıktı üretimi (yargı yok)
```bash
cd ogrenme/evals/h3-eval-seti
npx promptfoo@latest eval -c promptfooconfig-plain.yaml -o kor-ciktilar.json
npx promptfoo@latest view
```
Tarayıcıda açılan arayüzde her vakanın **modelin ürettiği tam cevabını** (muhakeme + sonuç) oku. Henüz hiçbir PASS/FAIL/puan yok — sadece ham çıktı var.

## Adım 2 — SEN elle puanla (yargıcı görmeden)
`elle-puanlama.md` dosyasını aç, 10 satırın her biri için modelin nihai cevabının doğru olup olmadığına **kendi başına** karar ver (doğru/yanlış), "Senin kararın" sütununu doldur. Bu adımı bitirmeden adım 3'e geçme — geçersen bağımsızlık bozulur (kutu 4).

## Adım 3 — yargıç LLM koşumu
```bash
npx promptfoo@latest eval -c promptfooconfig.yaml -o yargic-sonuc.json
```
Bu, `llm-rubric` ile aynı 10 vakayı puanlar (pass=doğru, fail=yanlış).

## Adım 4 — bana ilet
Doldurduğun `elle-puanlama.md`'yi ve adım 3'ün özet çıktısını (terminaldeki PASS/FAIL satırı ya da `yargic-sonuc.json`) paylaş; Cohen κ'yı hesaplayıp ders kaydına ve `ilerleme.md`'ye işlerim.
