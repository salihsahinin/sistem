# Ders kaydı — L8 gemi katmanı: WezTerm + tmux (Mac, elle koşum)

*Öğrenme-hattı kaydı (Şerit 2 formatının hafif hali — müfredat partisyonu değil, araç-alıştırması). Oturum: 2026-08-15, ana-sıra terminal (Carvis/Fable). Salih beyanı aynı gün: "artık Mac kullanıyorum, ekstra belirtmedikçe Mac." Klavye: Turkish-QWERTY-PC.*

## Ne öğrenildi (Salih koşarak)
- **[S] WezTerm** = sadece pencere; içinde tmux koşar, kendi kısayolları kullanılmaz. Config `~/.config/wezterm/wezterm.lua` (hot-reload).
- **[O] tmux** = üç şey: pane (böl) · window (sekme) · session (kalıcı — detach edince yaşar). Firstmate tayfayı tmux window'u olarak açtığı için ön-koşul.
- **Açılış komutu:** `tmux new -As jarvis -c ~/jarvis` → `claude`. Firstmate: `tmux new -As kaptan -c ~/dev/firstmate` → `claude`.
- Prefix **Ctrl-a** (conf). Bölme `|`/`-` conf'ta ama Türkçe klavyede `|` zor → varsayılanlar `%` (Shift-5) / `"` (Shift-2) kullanılır; ok-tuşu bind'ı öneri olarak verildi (Salih koşarsa conf'a girer).

## Ne oldu (hata → ders)
1. "Ctrl-a sağ ok" ile bölmeye çalışıldı — `|` karakteri ok sanıldı. Ders: kısayol tarifinde karakteri tuş adıyla yaz (Shift-5).
2. Tuş denerken `Ctrl-a d` (detach) ve `Ctrl-a c` (yeni window) basılmış → ekranda `[detached (from session jarvis)]`, oturumda 2 window kaldı (1: claude, 2: zsh). **Bozulma yok** — tam da tmux'un kalıcılık dersi: detach = kapanış değil. Geri dönüş aynı komut.

## Firstmate ilk ship koşumu (aynı oturum, 10:53→)
- Açılış: `tmux new -d -As kaptan -c ~/dev/firstmate && tmux switch-client -t kaptan` → `claude` (tmux İÇİNDEN yeni oturum = `-d` + `switch-client`; düz `tmux new` "sessions should be nested" der).
- Görev: notdefteri iskeleti (ship, no-mistakes, yolo=off, merge yok).
- **Bulgu 1 — bayat-kilit yanlış alarmı:** firstmate "başka oturum kilidi tutuyor (pid 4672)" dedi; 4672 = kendi `claude` başlatıcısı (CC 2.1.233 iki katman: launcher → bg-pty-host → oturum). Doğru bilgi verilince kilidi devraldı (`.lock` → 4442). Entegrasyon masası notu: firstmate ↔ yeni CC süreç-ağacı uyumu izlenecek.
- **Bulgu 2 — boş repo:** notdefteri'de commit yoktu → firstmate main'e boş bootstrap commit için onay istedi (kural 1 gereği), onaylandı (`e64e43e`), sonra tayfa spawn.
- **Bulgu 3 — tayfa nerede:** tayfa kaptanın oturumuna sekme olarak DEĞİL, ayrı `firstmate` tmux oturumuna (`2:fm-notdefteri-iskelet`) açılıyor. Kaptan'da `Ctrl-a n` "no next window" der; doğru yol `Ctrl-a s` → `firstmate` → `Ctrl-a 2`. Kural 4: bak, yazma.
- CC 2.1.233 oturum panosu (Esc ile düşülür; Enter aç / Space mesaj / Ctrl-x sil) tmux'tan ayrı üçüncü bir "sekme" katmanı — karışıklık kaynağı, kartta ayrıldı.

## Cep kartı (Mac)
```
tmux new -As jarvis -c ~/jarvis        # ana-sıra
tmux new -As kaptan -c ~/dev/firstmate # firstmate
tmux ls                                # oturumlar
Ctrl-a %  /  Ctrl-a "   böl (yan yana / alt alta)
Ctrl-a ok-tuşları veya h/j/k/l   pane geçişi
Ctrl-a c   n/p   1-9    sekme aç / gez ; sekme kapat = exit
Ctrl-a s                oturum listesi (jarvis ↔ kaptan)
Ctrl-a d                ayrıl — oturum yaşar
```

## Durum
- Bölme + sekme + ayrıl-dön alıştırması: DEVAM (bu kayıt açıkken).
- Sonraki: `kaptan` oturumunda firstmate'e `notdefteri` üstünde küçük scout görevi → akışı canlı izleme → entegrasyon masası.
- KILAVUZ l8-workflow'un firstmate/tmux satırları bayat ("Windows'ta yok", "tmux gerekmiyor") — Mac revizyonu borcu; bu kayıt ham girdi.
