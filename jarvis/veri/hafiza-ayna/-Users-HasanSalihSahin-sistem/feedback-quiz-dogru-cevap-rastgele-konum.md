---
name: feedback-quiz-dogru-cevap-rastgele-konum
description: "ogren skill'inde (PROBE/TEACH çoktan seçmeli sorular) doğru cevap hep aynı şıkka (a) denk gelmemeli, konum rastgele olmalı"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8e00e0dc-e89f-4d1f-a098-d73ee63e63bb
  modified: 2026-09-11T11:00:24.932Z
---

`ogren` skill'i ile üretilen çoktan seçmeli sorularda (`PROBE` ve `TEACH` fazları, format: 4 şık a-d + e bilmiyorum) doğru cevabın şık konumu (a/b/c/d) rastgele dağıtılmalı. 2026-09-11'de evals H2 dersinde Salih fark etti: art arda gelen sorularda doğru cevap neredeyse hep "a" idi, bu da soruyu okumadan şık konumuna göre tahmin etmeyi mümkün kılıyordu — quiz'in ölçtüğü şeyi geçersiz kılan bir tasarım hatası.

**Why:** Sabit konum örüntüsü, gerçek anlama yerine örüntü tanımayı ödüllendirir; PROBE'un anlayış sınırını doğru tespit etmesi ve TEACH'in gerçek pekiştirmeyi doğrulaması için şıkların konumu her soruda bağımsız/rastgele olmalı.

**How to apply:** Her yeni çoktan seçmeli soru yazarken doğru cevabın hangi şıkta (a/b/c/d) olacağına önceden karar vermeden, seçenekleri oluştur ve doğru olanı rastgele bir konuma yerleştir — art arda birkaç soruda aynı konumun tekrarlanmadığından kabaca emin ol. `.claude/skills/ogren/SKILL.md`'ye kalıcı kural olarak eklenmesi Salih'in onayına bağlı (Katman-1/skill dosyası); bu not [[feedback-ders-elle-pratik-adimi]] ile aynı derste (evals H2) çıktı, ikisi de ogren skill'inin olgunlaşma notları.
