---
name: feedback-rust-icra-kodu-test-degil
description: "Salih 10-16: \"Rust'a geçiş\" = md/Lean'deki görevi icra eden Rust kodu; kod yazmış olmak için gereksiz test kodu değil"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 351e6dbd-f569-425f-a10a-c1c3f9dce97b
  modified: 2026-10-16T19:18:54.269Z
---

Rust'a geçiş, bir md ya da Lean dosyasındaki görevi aynı işi yapan Rust koduyla değiştirmektir. Rust satırı saymak için test kodu yazmak bu değildir.

**Why:** Salih 2026-10-16: "kod yazmış olmak için gereksiz test kodları yazarak rust yazmayı kast etmedim".
**How to apply:** Hafıza ya da kanon geçişinde Rust payı icra kodudur. Test yalnız `.claude/rules/tools.md` eşiğinde yazılır (engelleyen hook, taşımada tek fark testi). Basit koda yeni birim testi yazılmaz. Geçiş otomatik ilerler, Salih'e yalnız karar düşünce gidilir ([[feedback-icra-listesi-onaysiz-devam]]).
