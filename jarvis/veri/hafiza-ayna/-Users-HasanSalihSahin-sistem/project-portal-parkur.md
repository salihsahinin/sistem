---
name: project-portal-parkur
description: "Portal x Mirror's Edge tarzı Godot oyunu projesi (projects/portal-parkur); Godot yolu, test komutu, referans depolar"
metadata:
  node_type: memory
  type: project
  originSessionId: 3e1fa2e3-46fa-4ae6-8358-d2c748e49d92
  modified: 2026-10-26T00:28:32.968Z
---

Salih 2026-10-26: Instagram reel (splicedgames "Portal x Mirror's Edge") + WhatsApp mp4 referansıyla "birebir" bir parkur+portal oyunu istedi. v1 `C:\sistem\sistem\projects\portal-parkur` (Godot 4.7.2, `C:\tools\godot\Godot_v4.7.2-stable_win64.exe`; `oyna.bat` / `test.bat`; test = `PP_TEST=1 godot --path .` → `test_cikti/rapor.json`, 9 mekanik test).
Temel: VojtaStruhar/godot-portals-plugin (MIT, `addons/portals`) + DeiranZ parkur fikirleri; ticari oyun decompile edilmedi (EULA). Referans klonları `referans/` (git dışı). Hareket: Salih'in istekleriyle katmanlar eklendi: Dying Light bakış (ham 1:1 fare, F4 panel), CS bunny hop (Source AirAccelerate), MW2019 kayma/sprint, en son **Minecraft modeli varsayılan** (azalea-rs/azalea `azalea-physics` portu, `referans/azalea`); F4 `model` ile parkur modeline dönülür. Dying Light makinede kurulu değil; ayar dosyası okunamadı.

**Why:** Salih "tatmin olana kadar itere et" dedi; sonraki oturumlar aynı projede devam eder.
**How to apply:** İterasyon isteğinde README.md ve `betikler/` okunur; her değişiklikten sonra `test.bat` koşulur, ekran görüntüleri `test_cikti/*.png` ile görsel kontrol yapılır. Tek tırnak içeren heredoc bu Bash aracında bozuluyor → dosyalar Write ile yazılır ([[feedback-bash-heredoc-tek-tirnak]]).
