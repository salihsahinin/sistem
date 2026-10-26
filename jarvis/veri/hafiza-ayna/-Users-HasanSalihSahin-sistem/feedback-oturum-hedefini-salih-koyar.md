---
name: feedback-oturum-hedefini-salih-koyar
description: "Salih 2026-10-26: Salih'le yapılan oturumun hedefini/konusunu Salih koyar; Jarvis seans düğümüne baştan hedef yazmaz. Önceden verilen hedef yalnız sistem-içi otomasyon oturumlarında."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 4b1f454e-8921-45e4-bf12-ada7ec6e463d
  modified: 2026-10-26T14:59:52.237Z
---

Salih'le yapılan bir oturumda neyin konuşulacağını ve hedefi oturumun başından Salih planlar. Jarvis `durum seans-ac --hedef` ile kendi türettiği hedefi seans düğümüne **yazmaz**; hedef alanı Salih beyan edene kadar boş kalır. Hedef önceden yalnız sistemin kendi içindeki otomasyon oturumlarında (ajan→ajan devir) verilebilir.

**Why:** 2026-10-26 ikinci seansta Jarvis seans düğümüne "Portal Parkur kapatılır" hedefini önceden yazdı; Salih bunu yanlış buldu: oturumun planı onundur, graf düğümü Jarvis'in varsayımını değil Salih'in beyanını taşımalı. (Karar 99 M10'daki "SIRADA'dan türetip teyide sun" uygulaması bu beyanla daralır: teyide sunulabilir, kütüğe yazılamaz.)

**How to apply:** `seans-ac` hedefsiz koşulur; Salih hedefi söyleyince kütüğe işlenir. Açılış brifinde hedef önerisi ancak soru cümlesi olarak durur. İlgili: [[feedback-urun-ayri-repo]], [[feedback-seans-basi-tetik-gunaydin-degil]].
