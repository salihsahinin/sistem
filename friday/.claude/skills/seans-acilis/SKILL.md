---
name: seans-acilis
description: Friday'in seans-AÇILIŞ ritüeli. Salih "seans başı" dediğinde koşar; konum akış grafından okunur (`durum oturum-basi --alan friday` → `durum seans-ac`), md kapsül/pano okunmaz (dondu, Karar 122); profil/bulut hafızadan anlatılmaz. Kullanılmaz; oturum-ortası selamlaşmada, kapanışta ("seans bitimi" → seans-kapanis), Jarvis oturumunda (Jarvis'in kendi ritüeli var).
---

# Seans başı — Friday açılışı (v0.2, 2026-10-25; Karar 122 graf + JSON; v0.1 09-09 Jarvis kopyası)

1. **Zaman-kayması freni:** selamlama zaman işareti değil; tarih yalnız `date`'ten.
2. **Konum (graf dili, Karar 122):** `C:\sistem\sistem\target\release\durum.exe oturum-basi --alan friday` → `KONUM` (son seans + hedef yoklaması) · `SIRADA` · `bekler<-#n` · `HEDEF`; ayrıntı `--json` ya da `durum graf --alan friday --metin`. `core/durum-kapsulu.md` ve `core/pano.md` **dondu**: okunmaz, yazılmaz.
3. **Oku (sırayla, tamamı):** `CLAUDE.md` → `cc/gelen/` içinde geri-dönüşü olmayan devir birimi var mı (`cc/giden/<devir_id>-geri-donus.md` yoksa `BEKLİYOR`) → `core/desenler.md` (tamamı; ≤3 KB düz liste) → son seans kaydı `raporlar/seans/seans-teslim-<tarih>-<etiket>.json` (`sonraki_ilk_is` + `salih_karar`) → gerekirse `kuyruk/senaryo-defteri.md` son 5 kayıt.
3b. **Devir kimliği (kütük v0.3, tur-2 B1):** bir devir birimini devralırken `cc/gelen/.aktif-devir` dosyasına `devir_id` yaz (tek satır); geri-dönüş notu yazılınca dosyayı sil. Kütük her satıra bu kimliği ekler.
4. **Canlı-oturum kapısı:** `git log -3 -- .` — son commit ≤15 dk ∧ kütükte açık seans varsa "paralel oturum şüphesi" beyan et; commit yalnız `git add <yol>`.
5. **Kök kanon kontrolü (Karar 101):** `ls ../AGENTS.md ../sablonlar/geri-donus-v0.md` ikisi de var mı; yoksa dur, Salih'e söyle. `jarvis/**` okunmaz.
6. **Seansı aç:** `durum seans-ac --alan friday --hedef "<tek cümle>"` (hedef: Salih beyanı aynen, yoksa `SIRADA` ilk işten; brifte teyide). Oturum adı kapanışta gerekir, brife yaz.
7. **Brif (tek ekran):** tek satır konum · sırada/bekler · bekleyen devir birimleri · Salih'te bekleyen hükümler · hedef cümlesi · oturum adı.
8. Frenler: karar verme · kanon yazma · `main`'e push (kendi oturum dalına push + PR serbest, EK-5) · Jarvis yolu okuma (hook keser; denemeyi sapma olarak yazma, tasarımdır).
