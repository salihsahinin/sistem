---
name: seans-acilis
description: Friday'in seans-AÇILIŞ ritüeli. Salih "seans başı" dediğinde koşar; durum yalnız bu reponun kanonundan okunur (kapsül → pano → cc/gelen bekleyen devir), profil/bulut hafızadan ANLATILMAZ. KULLANILMAZ; oturum-ortası selamlaşmada, kapanışta ("seans bitimi" → seans-kapanis), Jarvis oturumunda (Jarvis'in kendi ritüeli var).
---

# Seans başı — Friday açılışı (v0.1, 2026-09-09; Jarvis seans-acilis'in küçük kopyası)

1. **Zaman-kayması freni:** selamlama zaman işareti DEĞİL; tarih yalnız `date`'ten.
2. **Oku (sırayla, tamamı):** `CLAUDE.md` → `core/durum-kapsulu.md` → `core/pano.md` → `cc/gelen/` içinde geri-dönüşü olmayan devir birimi var mı (`cc/giden/<devir_id>-geri-donus.md` yoksa BEKLİYOR) → `core/desenler.md` (tamamı; ≤3 KB düz liste, başlık yapısı yok — 09-10 A9) → gerekirse `kuyruk/senaryo-defteri.md` son 5 kayıt.
2b. **Devir kimliği (kütük v0.3, tur-2 B1):** bir devir birimini devralırken `cc/gelen/.aktif-devir` dosyasına `devir_id` yaz (tek satır); geri-dönüş notu yazılınca dosyayı sil. Kütük her satıra bu kimliği ekler; sayaç `devir_id` ile alınır.
3. **Canlı-oturum kapısı:** `git log -3` — son commit ≤15 dk ∧ kapsülde kapanış kaydı yoksa "paralel oturum şüphesi" beyan et; commit yalnız `git add <yol>`.
4. **Kök kanon kontrolü (Karar 101, 09-18; `kanon/` bağı emekli):** `ls ../AGENTS.md ../sablonlar/geri-donus-v0.md` ikisi de var mı; yoksa dur, Salih'e söyle (depo kökü bozuk). `jarvis/**` okunmaz, tam metin pointer'ları (m.NN) kök md özleriyle yetinir.
5. **Brif (tek ekran):** tek satır durum · bekleyen devir birimleri · Salih'te bekleyen hükümler · bu seansın tek cümlelik hedefi (kapsül "Sonraki ilk iş"ten).
6. Frenler: karar verme · kanon yazma · push yok · Jarvis yolu okuma (hook keser; denemeyi sapma olarak yazma, tasarımdır).
