---
name: feedback-maliyet-tahmini-alt-model
description: "Salih 08-29 — Jarvis kendi (ana-sıra) koşumları için token/maliyet tahmini yapmaz; tahmin yalnız alt-model/işçi-ajan koşumları için yapılır, çıkarım oradan"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0fa78c95-8e3c-4e7a-8f68-60b6d04f6a0c
  modified: 2026-08-29T08:43:14.120Z
---

Salih (2026-08-29, icra borcu listesi sunumunda): "maliyet tahminlerini kendi koşumların için yapman saçma, alt modeller için yapıp çıkarım yapabilirsin."

**Why:** Ana-sıra modelin kendi koşumu için verdiği token/maliyet kestirimi ölçülmemiş varsayımdır (m.39: rakam kaynaklı olmalı); alt-model koşumları ise bütçe/effort parametreleriyle deterministik sınırlanır ve usage kaydından ölçülür — kestirim orada anlamlıdır.

**How to apply:** İş listesi/plan tablolarında "maliyet" sütunu yalnız işçi-ajan/atlas/Workflow koşumları için doldurulur (bütçe × effort × ajan sayısı); Jarvis'in kendi yapacağı iş için süre/token tahmini **yazılmaz** — "kod/deterministik, ana-sıra" gibi sınıf etiketi yeter. İlgili: [[feedback-token-kisinti-yuzde30]] (işçi bütçesi 10-15, effort düşük-orta).
