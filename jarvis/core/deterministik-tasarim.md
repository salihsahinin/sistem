# Deterministik tasarım — kapsamlı kural (core, 2026-09-10; kaynak: Salih 08-17 Katman-1 beyanı + Karar 65 08-22 + Salih 09-10 kapsam daraltması)

*Bu dosya CLAUDE.md §6'daki tek-satır pointer'ın gövdesidir. Salih 09-10 (Katman-1, aynen): "jarviste genel olarak konuşmalarımda deterministlik ilkesi fazla vurgulanıyor ve konudan bağımsız her konuşmamda dikkat ediliyor. bu durumu değiştirelim. context windowda fazla baskın. hafıza katmanında daha düşük bir katmana atılabilir veya sadece spesifik iş türleri yapılırken kullanılacak şekilde tanımlanabilir." → **ikisi** birden uygulandı: gövde bu dosyaya (alt katman), CLAUDE.md'de kapsam listeli tek satır (iş-tetikli). Karar 92 EK.*

## 1. Kural (08-17 metni aynen; kapsamı §2 ile sınırlı)
Aynı girdi → aynı yol. Rastgelelik / olasılık beyanı / çok-örneklem "dağılım" / ajan-tartıştırma **tasarım aracı** değildir; tekrarlı iş kodda; tekrar-üretim kayıtla sağlanır. Karar 65 (08-22): determinizm önceliği — deterministik yol varsa stokastik yol seçilmez.

## 2. Nerede uygulanır (iş türü tetikleri — yalnız bunlarda vurgulanır)
1. **Script / araç yazımı** (`tools/`, skill `scripts/`, hook): idempotens + aynı girdi aynı çıktı (`tools/AXI-STANDARDI.md` A4).
2. **Ölçüm ve katman koşumları** (katman-hatti, silver/gold türetimi, hareket kütüğü, anakronizm denetimi): yeniden türetim el birleştirmesi olmadan (Karar 77).
3. **Ajan emri derleme + pipeline/workflow tasarımı**: dallar yazılı, tetik yüklemi boolean, "hakeme sor / dağılım çıkar" tasarım aracı değil.
4. **Kanon ölçüm iddiaları** (m.29/m.39 rakam): tekrar-üretilebilir kayıt yoksa `[?]`.

## 3. Nerede vurgulanmaz (09-10 daraltması)
Sohbet, öğretim, karar sunumu, rapor anlatımı, günlük iş planlaması, Salih sorularına cevap. Bu bağlamlarda ilke sessizdir: ne gerekçe cümlesi olarak yazılır ne de her seçeneğe "deterministik mi" süzgeci uygulanır. Bir tasarım kararında stokastik seçenek masaya gelirse §1 yalnız o kalemde, tek cümleyle anılır.

## 4. Bağlı kayıtlar
CLAUDE.md §6 (pointer satırı) · tüzük Karar 65 (`arsiv/kuyruk-arsiv/` 08-22 arşivi) · `wiki/anakronizm-freni.md` (Karar 68, ayrı kural) · hafıza notu `feedback-claude-md-kisa-tut` (08-17 paketi; 09-10 daraltma işlendi).
