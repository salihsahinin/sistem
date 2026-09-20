---
name: feedback-gorsel-mekanizma-degil-metin-kutusu
description: Öğretim görsellerinde d2/flowchart kabul edilmiyor; gorsellestir skill'i 09-03 akşamı Salih emriyle silindi (arşiv kuyruk/arsiv/); görsel gerekirse mcp__visualize interaktif/illustrative rota
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e0839c9b-38fb-4725-a9dd-7403494cd6b5
  modified: 2026-09-03T10:49:06.106Z
---

Salih 09-03: 6.006 dersini işlerken tümevarım kanıtı için üretilen d2 flowchart'ları (metin kutuları + oklar, "surec" sınıfı, gorsellestir skill'i) yetersiz bulundu — "bakınca bir şey anlamıyorum", ardından "d2 formatı kullanma". Metin kutularını düz dille yeniden yazmak (Blok 3 2. deneme) de yetmedi; sorun format düzeyindeydi, içerik değil.

Çözüm: mcp__visualize (Imagine) ile illustrative/interactive HTML widget — mekanizmayı **uygulanan** bir metafor + tıklanabilir/adım adım somut örnekle gösterdi (domino zinciri = tümevarım mantığı, tıklanabilir "sıradaki öğrenciyi görüş" simülasyonu = somut sayı örneği). Bu kabul gördü (henüz açık onay gelmedi ama yön doğru sinyal aldı — izlenecek).

**Why:** Öğretim/kavratma amaçlı görsellerde Salih "referans diyagramı" (yapıyı belgeleyen kutu-ok şeması) değil, "sezgi diyagramı" (mekanizmayı hissettiren, tercihen etkileşimli) istiyor — Munzner ayrımıyla intuition vs reference diyagram, Salih intuition tarafını tercih ediyor.

**How to apply:** [[gorsellestir]] skill'i (d2/mermaid/vega-lite/tablo) yapısal/referans görseller için uygun (kavram haritası, karşılaştırma, sayısal veri). Öğretim/kanıt/mekanizma anlatımı istendiğinde (özellikle "öğreten görsel", "anla", ders/kavram canlandırma bağlamında) önce mcp__visualize illustrative+interactive rotasını düşün; d2 flowchart'ı yalnız Salih özellikle referans-tipi (yapı/süreç haritası) istediğinde kullan.


**Güncelleme 2026-09-03 22:10:** Salih "görselleştir skillini sil, beğenmedim" dedi; skill + tools/gorsellestir.py + testler `kuyruk/arsiv/gorsellestir-skill-2026-09-03/` altına indi, symlink kaldırıldı. Yukarıdaki "skill uygun" cümlesi artık geçersiz: görselleştir tetiği yok. Görsel gerekirse doğrudan mcp__visualize (illustrative/interactive) ya da düz anlatım; yeni bir görsel skill'i önermeden önce Salih tek canlı koşum görüp beğenmeli (v0.1→v0.3 üç düzeltmeye rağmen ret geldi).
