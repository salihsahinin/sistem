---
name: feedback-parallel-sessions-keep-talking
description: "Salih uzun workflow koşan oturumu açık bırakıp ikinci terminal oturumu açar ve orada konuşmaya devam eder — ikinci oturum kapatılmaz, yan-hat alır; ritüel canlı-oturum kontrolü yapmalı"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1620e67b-d1dc-48c2-bced-080dfb43b3e7
  modified: 2026-08-15T17:40:08.923Z
---

Salih, bir oturumda uzun bir Workflow (m.40b çift-atlas, ~40 dk) çalışırken ikinci bir terminal oturumu açıp "seans başı" der ve **orada** konuşmaya devam eder (2026-08-15 20:22, seans-2 Hat-3 koşarken seans-3 açıldı). İkinci oturuma "kapat" önerisi getirmek yanlış; beklenen davranış: ikinci oturum canlı kalır, konuşulan oturum olur ve önceki oturumun sahadaki işine (aynı manifest satırı, aynı hedef dosyalar) **dokunmadan** yeni bir hat alır.

**Why:** Salih bekleme süresini boşa harcamak istemiyor; workflow'lar arka planda koşarken yeni sezgi/görev üretiyor. Ayrıca önceki oturum kapanış ritüeli koşmadan açık kalabiliyor — "çok taze commit" paralel oturumun işaretidir, kapalı sayılmaz.

**How to apply:** gunaydin-vardiya brifinde son commit ≤15 dk ∧ kapanış kaydı yoksa "paralel-oturum şüphesi" beyan et ve tek soru sor (hangi oturum hangi hattı alıyor); cevap gelene dek workflow/ajan başlatma ve diğer oturumun sahadaki dosyalarına yazma. Aynı manifest satırı "**sahada**" ise ikinci kez koşma. Kayıt: `kuyruk/gelen-2026-08-15-paralel-oturum-vaka-2.md`. İlgili: [[user-mac-primary]]
