# Paralel Yapılanma Planı — 2026-07-13 (Salih emri: "planını yap, raporu sun"; başlangıç tarihi yetkisi Carvis'e devredildi)

> **ARŞİV NOTU (07-15):** Bu plan revize edildi → güncel sürüm `paralel-yapilanma-plani-2026-07-15-v2.md` (öğrenme şeridi eklendi, PortRisk 3. önceliğe indi, P1 yeniden şekillendi). Dosya m.8 gereği silinmez.

## Neden şimdi
Salih 07-13: prototip süreci uzun; belirli aşamadan sonra bir yandan Jarvis'i geliştiren, bir yandan o anki projeyi inşa eden paralel yapıya geçilmeli. Altyapı zaten hazır: paralel-vardiya protokolü (KILAVUZ, 07-12) + `PARALEL-VARDIYA-ILK-DENEME.md` talimatı + m.36c (PortRisk=ölçüm-bankı, bloke değil).

## Şeritler (4 yüzey)
| # | Şerit | Yüzey | Açılış | İçerik | Kanon yetkisi |
|---|---|---|---|---|---|
| 1 | JARVIS vardiyası | Cowork oturum A | "günaydın" | prototip: loop-eng Faz 2+4 → K-009 → K-010 | TAM (kanon sahibi) |
| 2 | Ölçüm-bankı vardiyası | Cowork oturum B | "günaydın, PortRisk" | Sprint 1+ (çift mount; iç-mutfak public repoya ASLA yazılmaz) | kapsülde yalnız kendi satırı |
| 3 | Chat şeridi | Claude chat / telefon | CHAT-KAPSULU yükle | tartışma, fikir, öğrenim, karar-hazırlığı | SIFIR — çıktı = fikir-kutusu-adayı |
| 4 | Jarvis-DIŞI chat'ler | Claude chat | kapsülsüz | ders/sınav (örn. kısmi diferansiyel), gündelik | — (Jarvis bağlamı bilerek YÜKLENMEZ: bağlam hijyeni + token) |

## Senkron kuralları
1. Kapsülde her vardiya yalnız KENDİ satırını günceller; ayrı vardiya-teslim raporu; push öncesi pull (KILAVUZ 07-12 protokolü aynen).
2. Aynı dosyaya iki oturum eşzamanlı yazmaz; çakışmada Şerit 1 (kanon sahibi) kazanır.
3. Chat çıktıları YALNIZ Salih eliyle Cowork'e girer (fikir-kutusu-adayı formatı); otomatik akış yok (V27 tetiklenirse yeniden tasarlanır).
4. Her Cowork oturumu açılışta kapsülü okur (bayat-kapsül riski, V4).
5. Şerit 4 tamamen bağımsız: sınav chat'inde Jarvis konuşulmaz, Jarvis oturumunda sınav hazırlığı yapılmaz (dikkat bölünmesi iki yönde de maliyet).

## Başlangıç tarihi — m.37 karar formatı (senaryo-defterine işlendi)
- **Model A (bugün hemen):** erken veri · RİSK: yarın kısmi diferansiyel sınavı — Salih bant genişliği bölünür; loop-eng (Şerit 1'in işi) henüz başlamadı, iki şerit de yarım açılır.
- **Model B (15 Temmuz — sınav ertesi ilk tam gün):** talimat dosyası hazır, Salih tam dikkatle iki vardiyayı koşar; sınav önceliği korunur · maliyet: 2 gün gecikme. ✅
- **Model C (loop-eng Faz 2+4 bitince):** Şerit 1 olgun başlar · RİSK: PortRisk'i keyfî geciktirir (m.36c bloke-değil kuralına aykırı ruh).
- **KARAR (Carvis, Katman 2; m.37 görünürlük gereği burada sunuldu):** Model B — **15 Temmuz sabahı ilk paralel Cowork denemesi** ("günaydın" + ayrı oturum "günaydın, PortRisk"). Şerit 3 BUGÜN başlar (CHAT-KAPSULU hazır). Şerit 4 zaten bağımsız — bugün/yarın sınav chat'i serbest. 14 Temmuz Jarvis işi YOK (sınav günü). Veto = tarih değişir, plan değişmez.

## DONE tanımları
- İlk paralel gün DONE: iki vardiya da kendi teslim raporunu yazdı ∧ kapsül çakışmasız ∧ push'lar temiz.
- Chat şeridi denemesi DONE: ilk kapsüllü chat oturumu ≥1 fikir-kutusu-adayı üretti ∧ Cowork'e taşındı.
- Plan revizyon tetiği: herhangi bir senkron kuralı 2 kez ihlal olursa protokol yeniden masaya gelir.

## Riskler ve karşılıkları
- Bağlam çatallanması → tek kapsül + satır sahipliği (kural 1-2).
- Chat'te karar alma eğilimi → kapsül protokolü madde 1 (karar yok, aday var).
- Mount güvenilmezliği iki oturumda iki katına çıkar → V43 zorunlu: her kritik yazım push sonrası cmp ile origin-doğrulamalı.
