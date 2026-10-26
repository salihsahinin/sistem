---
name: feedback-urun-ayri-repo
description: "Salih 2026-10-26: Jarvis'in uzun vadede kullanmayacağı ürünler (oyun demosu gibi) sistem deposuna değil ayrı klasör + ayrı açık kaynak repoya gider; sistem reposu ürün inşa aracıdır."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 4b1f454e-8921-45e4-bf12-ada7ec6e463d
  modified: 2026-10-26T15:00:18.946Z
---

Jarvis'le üretilen bir ürün sistemin kendisi için değilse (Jarvis'in uzun vadede kullanacağı araç değilse), ürün `C:\sistem\sistem` deposuna girmez. Ürün kendi klasöründe (`C:\sistem\<urun>`), kendi git deposunda ve açık kaynak GitHub reposunda yaşar; push o repoya yapılır. Sistem deposu ürün inşa eden **araçtır**, ürünlerin ambarı değil. İlk uygulama: Portal Parkur oyun demosu 2026-10-26'da `projects/portal-parkur`'dan `C:\sistem\portal-parkur` + GitHub `salihsahinin/portal-parkur` reposuna taşındı; sistemde yalnız pointer README kaldı.

**Why:** Salih 2026-10-26: "tek bir repoda ve tek bir klasörde her şeyi buildleyeceğimize sistem reposu ürün buildlemek için bir araç olmalı." Ürün kodu sistem deposunu şişirir, bağlam karışır, açık kaynak paylaşımı zorlaşır.

**How to apply:** Yeni ürün isteğinde önce sor-değil-karar: sistem aracı mı, ürün mü? Ürünse `C:\sistem\<ad>` klasörü + `git init` + `gh repo create` (public) ile başla; sistem deposunda `projects/<ad>/README.md` pointer'ı yeter. Jarvis bağlamı (hareket kütüğü, seans kaydı) sistemde kalır. İlgili: [[project-portal-parkur]], [[feedback-oturum-hedefini-salih-koyar]].
