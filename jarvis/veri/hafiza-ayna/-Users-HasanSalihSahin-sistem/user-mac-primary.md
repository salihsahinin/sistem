---
name: user-mac-primary
description: Salih 2026-09-22'den beri Windows 11'de çalışır (C:\sistem\sistem, Herdr + Windows Terminal); Mac'e dönüş planı yok (10-16). Klavye Turkish-QWERTY-PC; 'ctrl' kısayolu Mac döneminden ⌘ alışkanlığı taşıyabilir, sistem ayarı değiştirmeden önce teyit et.
metadata: 
  node_type: memory
  type: user
  originSessionId: f14bd4b6-9bf6-400a-a6c5-4c80719230f9
  modified: 2026-10-17T15:13:47.135Z
---

Salih 2026-08-15: "artık Mac kullanıyorum, ekstra belirtmedikçe Mac kullanacağım." Windows PC yolları (C:\JARVIS, C:\dev\...) bayat; jarvis `~/jarvis`, firstmate `~/dev/firstmate`, deneme `~/dev/wf-deneme`. Klavye düzeni Turkish-QWERTY-PC — `|` gibi karakterler tmux/CLI tarif ederken tuşa değil karaktere/alternatif tuşa göre anlat.

**Ek (2026-09-22, makine devri):** Mac laptop şirkete teslim edildi (09-21); Salih şimdilik **Windows 11**'de (Git Bash + Claude Code masaüstü). Depo `C:\sistem\sistem` (zip'ten açıldı, iç içe `sistem\sistem`; Mac'teki `~/sistem`), harness anahtarı `C--sistem-sistem`. Windows'a özgü: `python3` Store yönlendiricisi → `~/bin/python3` shim; symlink'ler (CLAUDE.md → AGENTS.md ×7, ogren skill ×4, kaynak-kodu ×4) Developer Mode açılana dek düz metin dosya; hook testleri sabit Mac yolları yüzünden kısmen düşer (KURULUM §4). Salih 09-22: "Mac'e şimdilik geri dönmeyeceğim" → Windows süresiz varsayılan; `kaynak-kodu/no-mistakes` symlink hedefi Windows ev dizinine çevrildi (Mac'e dönüşte geri alınır).

**Ek (2026-10-16):** Salih "mace dönüş planım henüz yok"; Herdr 0.9.4 Windows Terminal içinde (PowerShell penceresinde yapıştırma çalışmadı), worktree'ler `C:\sistem\wt\`. Mac geçişi gerekçesiyle tasarım kararı verilmez.

**How to apply:** komut/yol/kısayol tariflerinde Windows 11 + Git Bash/PowerShell varsay; Windows'a özgü notları (PowerShell, **bom**, schtasks) yalnız açıkça istenirse ver.

**Ek (2026-08-16, seans-7 — Salih'in kendi ifadesi):** "ctrl space diye aklıma kaydedip düşündüğüm için mac'te yazdığımı unutup" — Windows alışkanlığıyla **'ctrl' ≈ 'cmd' (⌘)** der. Vaka: 'ctrl-space'i spotlight'a bağla' → Jarvis Ctrl-Space'e bağladı, yanlış anlaşıldı, geri alındı (Spotlight = ⌘-Space). Kural: kısayol/klavye ifadelerinde 'ctrl' geçince Mac'te ⌘ olarak oku; **sistem ayarı değiştirmeden önce tek cümleyle teyit et** (geri alması ucuz ama karışıklık pahalı). Veri kaydı: `veri/tartisma-notu.jsonl` TN-002 (kapandı). İlgili: [[feedback-dosya-teslimi-finder]].
