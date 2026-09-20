---
name: oturum-acma-worktree-beyani
description: "Salih 2026-09-18 — her oturum-açma talimatında (Friday dahil) worktree AÇIK/KAPALI + sebep yazılır; Jarvis Fable ana-sıra worktree'siz açılır"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7b351190-3da0-497d-b909-e520561c17eb
  modified: 2026-09-18T08:30:45.051Z
---

Salih (2026-09-18 seans açılışı, aynen): "bundan sonra friday dahil tüm oturumlar için worktree formatının açık olup olmaması gerektiğini sebebiyle belirt (oturum açmak için talimat verdiğinde). jarvis fable ana oturum worktree seçili olmadan açılıyor belirteyim."

**Why:** 09-15 vakası: yan oturum ana checkout'ta çalışınca PR #4 ana-sıranın 17 push'lanmamış commit'ini taşıdı (Karar 95 EK). Worktree seçimi oturum açılırken yapılır; sonradan düzeltilemez. Salih her açılışta neyi seçeceğini talimatta görmek istiyor.

**How to apply:** oturum açma talimatı verirken tek satır "worktree: AÇIK/KAPALI — sebep". Tablo (kaynak `wiki/paralel-oturum-protokolu.md` §5 EK-2):
- Jarvis Fable ana-sıra `~/jarvis` → **KAPALI** (kanon, kapsül, silver sqlite, merge ve push ana checkout'ta; worktree'de kapsül yazımı ana-sıraya düşmez).
- `~/jarvis` yan oturum (öğrenme şeridi, Sonnet/Opus yan iş, gnhf) → **AÇIK** (ana checkout'un yarım işine dokunmaz; branch + PR; ilk iş `git fetch origin && git rebase origin/main`).
- Friday `~/friday` → **KAPALI** (ayrı repo, tek oturum, kapsül kendi core'una yazar, PR hattı yok, dönüş dosyayla). İstisna: aynı anda ikinci Friday oturumu → **açık**.
- Staj `~/staj başlangıç` → **KAPALI** (remote yok, tek oturum). İstisna aynı.
Genel kural: worktree yalnız aynı checkout'u paylaşan ikinci oturum varsa açılır. İlgili: [[feedback-parallel-sessions-keep-talking]], [[project-ekip-lideri-ayri-repo]].
