---
name: ogretim-iskeleti-ogren-sektor-basligi
description: "Salih 09-14 — tüm öğrenme şeritlerinde ders iskeleti = ogren v0.1 (`PROBE` → `PLAN` DAG → `TEACH` kutu → `CLOSE`); her hafta/kutu sektörün güncel İngilizce başlığıyla etiketlenir; görsel yalnız istekle, mekanizmayı simüle eden etkileşimli görsel"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 14da067d-1709-4923-8534-b33c61ec2b69
  modified: 2026-09-14T14:11:22.645Z
---

Salih (2026-09-14): "h1 h2 h3 anlatım/öğretim formatı (kutu kutu ve ilk başta bilgi ölçme turu) bana uygun … bu formatta eğitim yapalım; çalıştığım konuların sektörde günceldeki konu başlığı olarak isimlerini de belirt; her kutu için öğretici simülasyon görseli isteğime bağlı."

**Why:** H1-H3 evals derslerinde ogren skill'i (`PROBE` bilgi-ölçme turu + kutu kutu anlatım) ilk kez canlı koştu ve Salih'e uydu; sektör adı olmadan öğrenilen şey iş ilanı/ekip diliyle eşleşmiyordu; önceki `gorsellestir` skill'i (d2 akış şeması) reddedilmişti, yeni istek "mekanizmayı simüle eden" görsel.

**Birleştirilen 09-11 kuralları (dosyaları duruyor, indeksten bu satıra indi):** araç/format öğreten kutuda salt okuma yetmez, "şimdi sen dene" mini adımı; çoktan-seçmeli soruda doğru şık konumu rastgele dağıtılır.

**Büyük harf vurgusu yasak (Salih 09-15, "caps lock açık kelime vurgusu görmek istemiyorum"):** vurgu kalın harfle; tamamı büyük harf yalnız kısaltma. Kök neden: kanon/skill dosyaları 20-70‰ büyük-harf vurgu taşıyor, Sonnet bunu taklit ediyordu; fren = Stop hook `stop-buyuk-harf.sh`.

**How to apply:** Ders = `.claude/skills/ogren/SKILL.md` v0.1 iskeleti; kutu başlığının yanına "Sektör: *English Term* (kaynak)" yaz, AS-OF damgalı ve ders içinde canlı teyit (Karar 68); görsel ancak Salih "kutu N'i görselleştir" derse, `mcp__visualize` interactive ile adım adım simülasyon, kutu içi tek cümle, metin görsele atıflı. Kanon: `ogrenme/README.md` adım 6. İlgili: [[feedback-gorsel-mekanizma-degil-metin-kutusu]] [[feedback-gorsel-anlatim-atifli]] [[feedback-quiz-dogru-cevap-rastgele-konum]] [[feedback-ders-elle-pratik-adimi]]
