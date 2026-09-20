---
name: feedback-ses-ekran-kaydi-onay
description: Salih 2026-08-26 — ses ve ekran kaydı kullanmadan önce haber ver + onay al; sormadan yakalama yok
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c274360b-ef81-4d8f-ac89-99abce901ea4
  modified: 2026-08-26T07:46:50.931Z
---

Salih'in kuralı (2026-08-26, aynen): "bundan sonra ses ve ekran kaydı kullanacağın zaman bana haber verilip benden onay alınmalı."

Kapsam: ekran görüntüsü/video yakalama (`screencapture`, ffmpeg avfoundation ekran girdisi, üçüncü-parti kayıt araçları) ve mikrofon/ses yakalama (`rec`, `sox`, ffmpeg ses girdisi, OpenSuperWhisper tetikleme). Önce ne yakalayacağımı ve niçin gerektiğini söylerim, açık "evet" gelmeden komutu çalıştırmam.

**Why:** Tetikleyen olay — Obsidian kurulumunu ona göstermek için `screencapture` çalıştırdım, sormadan. Komut Ekran Kaydı izni olmadığı için başarısız oldu, görüntü üretilmedi; ihlal niyet düzeyinde kaldı. Ekran ve mikrofon Salih'in fiziksel çevresini örnekler (odada başkası, açık başka pencereler, üçüncü-şahıs verisi) — bu yüzden `git push` (m.9) ve md.49 ile aynı fren sınıfında.

**How to apply:** "Göstermek için lazım" tek başına gerekçe değil — teslim usulü (CLAUDE.md §5) zaten tam dosya yolu + `open -R` + doğrudan açılan tür diyor; doğrulama için ekran yakalamak yerine deterministik kontrole düş (`pgrep`, config dosyasını oku, CLI çıktısı). Kayıt gerçekten gerekiyorsa tek cümleyle sor, onayı bekle; onay verilse bile o onay o seferliktir, sonraki kayda genişletilmez. Deterministik sigorta (`.claude/settings.json` → `permissions.ask`) Salih onayına bağlı, henüz kurulmadı — kayıt: [[feedback-dosya-teslimi-finder]] usulüyle aynı hatta, karar bloğu `kuyruk/senaryo-defteri.md` Karar 70.
