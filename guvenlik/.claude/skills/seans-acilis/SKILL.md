---
name: seans-acilis
description: Alan ajanının seans-AÇILIŞ ritüeli. Salih "seans başı" dediğinde koşar; durum yalnız bu dizinin kanonundan okunur (kapsül → pano → şerit ilerlemesi → cc/gelen bekleyen ders iskeleti), profil/bulut hafızadan anlatılmaz. Kullanılmaz; "seans başı, <şerit>" (→ ogren; açılış brifi yine önce koşar), oturum-ortası selamlaşmada, kapanışta ("seans bitimi" → seans-kapanis), Jarvis/Friday oturumunda.
---

# Seans başı — alan ajanı açılışı (v0.1, 2026-09-21; Karar 105; Friday seans-acilis'in alan kopyası)

1. **Zaman-kayması freni:** selamlama zaman işareti değil; tarih yalnız `date`'ten.
2. **Oku (sırayla, tamamı):** `AGENTS.md` → `core/durum-kapsulu.md` → `core/pano.md` → `core/desenler.md` → her şeridin `ogrenme/<şerit>/ilerleme.md` (sıradaki hafta + önceki dersin `## Kalan`) → `cc/gelen/` içinde geri-dönüşü olmayan ders iskeleti / devir birimi var mı (`cc/giden/<id>-geri-donus.md` yoksa `BEKLİYOR`) → gerekirse `kuyruk/senaryo-defteri.md` son 5 kayıt.
2b. **Devir kimliği:** devir birimi ya da ders iskeleti devralınırken `cc/gelen/.aktif-devir` dosyasına kimliği yaz (tek satır); geri-dönüş yazılınca sil. Kütük her satıra bu kimliği ekler.
3. **Canlı-oturum kapısı:** `git log -3 -- .` — son commit ≤15 dk ∧ kapsülde kapanış kaydı yoksa "paralel oturum şüphesi" beyan et; commit yalnız `git add <yol>`.
4. **Kök kanon kontrolü:** `ls ../AGENTS.md ../sablonlar/skills/ogren/SKILL.md` ikisi de var mı; yoksa dur, Salih'e söyle. `jarvis/**`, `friday/**`, diğer alan dizinleri okunmaz (hook keser; denemeyi sapma olarak yazma, tasarımdır).
5. **Brif (tek ekran):** tek satır durum · şerit başına sıradaki hafta ve pratik `KALAN` · bekleyen iskelet/devir · Salih'te bekleyen hükümler · bu seansın tek cümlelik hedefi (kapsül "Sonraki ilk iş"ten; Salih açılışta beyan ettiyse aynen).
6. **Model beyanı:** oturum Sonnet 5 varsayılan; Salih "bugün Opus" dediyse brifte tek satır `eskalasyon: Opus (Salih beyanı)` ve teslim raporuna aynı satır.
7. Salih şerit adı verdiyse ("seans başı, evals") brif sonrası `ogren` skill'ine geç; ders iskeleti `cc/gelen/`'de yoksa `## Kalan`'dan devam, yeni hafta açma.
8. Frenler: karar verme · kanon yazma · push yalnız Salih beyanıyla · pratik = Salih'in eli.
