---
name: project-ekip-lideri-ayri-repo
description: "Friday artık ayrı repo değil; monorepo ~/sistem içinde friday/ dizini (Karar 101, 2026-09-18). Kanonu kök AGENTS.md + friday/AGENTS.md; jarvis/** kapalı."
metadata: 
  node_type: memory
  type: project
  originSessionId: a2f39e9d-af01-4657-b795-82568b722ce9
  modified: 2026-09-18T13:15:33.702Z
---

Friday (Opus 5 medium domain-lider) 2026-09-09 Karar 91 ile ayrı repo `~/friday` olarak doğdu; **2026-09-18 Karar 101** ile monorepo `~/sistem/friday/` altına subtree ile taşındı (tarih korundu). `kanon/` symlink emekli; Friday kural kaynağı kök `~/sistem/AGENTS.md` (16-18 madde) + `friday/AGENTS.md`. `jarvis/**` (Jarvis `core/` dahil) Friday'e kapalı: hook `okuma-izin.sh` v0.5 + deny `Read(~/sistem/jarvis/**)`. F5 kanıtı 09-18: Friday bağlamına Jarvis satırı 0.

**Why:** Salih, devir akışındaki dosya kopyalama sürtünmesini kaldırmak ve "N ajan + ortak kanon" modeline geçmek için monorepo'ya karar verdi; bağlam izolasyonu repo sınırı yerine cwd + hook + deny ile sağlanıyor.

**How to apply:** Friday oturumu `~/sistem/friday` cwd, worktree kapalı, main, pathspec-only, push yok, PR yok; emir `friday/cc/gelen/` + `send_message`; dönüş `cc/giden/`. Yeni ajan doğumu `sablonlar/charter-iskeleti.md` + Karar 91 EK-2 koşulu. Eski `~/friday` → `~/arsiv-friday-2026-09-18`. Bkz. [[feedback-oturum-acma-worktree-beyani]].
