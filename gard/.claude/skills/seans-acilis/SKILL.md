---
name: seans-acilis
description: Alan ajanının seans-AÇILIŞ ritüeli. Salih "seans başı" dediğinde koşar; konum akış grafından okunur (`durum oturum-basi` → `durum seans-ac`), md kapsül/pano okunmaz (dondu, Karar 122); profil/bulut hafızadan anlatılmaz. Kullanılmaz; "seans başı, <şerit>" (→ ogren; açılış brifi yine önce koşar), oturum-ortası selamlaşmada, kapanışta ("seans bitimi" → seans-kapanis), Jarvis/Friday oturumunda.
---

# Seans başı — alan ajanı açılışı (v0.2, 2026-10-25; Karar 122 graf + JSON; v0.1 09-21 Karar 105 Friday kopyası)

Kaynak: `sablonlar/ajan-iskelet/claude-ayar/skills/seans-acilis/SKILL.md` (doğurucu her alan ajanına kopyalar; değişiklik şablonda yapılır, kopyalar yenilenir). Hüküm `jarvis/lean/Kanon/AkisGraf.lean`.

1. **Zaman-kayması freni:** selamlama zaman işareti değil; tarih yalnız `date`'ten.
2. **Konum (graf dili, Karar 122):** `C:\sistem\sistem\target\release\durum.exe oturum-basi --alan <alan>` (ikili ana kopyada; kütük cwd'den yukarı bulunan `ortak/durum-olay.jsonl`, worktree'de worktree kopyası). Çıktı: `KONUM` (son seans, hedefi, tutuldu mu) · `SIRADA` (girdileri tamam işler) · `bekler<-#n` (girdisi açık) · `HEDEF` düğümleri · graf pointer'ı. Ayrıntı gerekirse `--json` ya da `durum graf --alan <alan> --metin` (kenar listesi). `core/durum-kapsulu.md` ve `core/pano.md` **dondu**: okunmaz, yazılmaz; tarihçe için arşiv.
3. **Oku (sırayla, tamamı):** `AGENTS.md` → `core/desenler.md` → her şeridin `ogrenme/<şerit>/ilerleme.md` (sıradaki hafta + önceki dersin `## Kalan`) → `cc/gelen/` içinde geri-dönüşü olmayan ders iskeleti / devir birimi var mı (`cc/giden/<id>-geri-donus.md` yoksa `BEKLİYOR`) → gerekirse `kuyruk/senaryo-defteri.md` son 5 kayıt → son seans kaydı `raporlar/seans/seans-teslim-<tarih>-<etiket>.json` (konum satırının işaret ettiği; `sonraki_ilk_is` + `salih_karar`).
3b. **Devir kimliği:** devir birimi ya da ders iskeleti devralınırken `cc/gelen/.aktif-devir` dosyasına kimliği yaz (tek satır); geri-dönüş yazılınca sil. Kütük her satıra bu kimliği ekler.
4. **Canlı-oturum kapısı:** `git log -3 -- .` — son commit ≤15 dk ∧ kütükte açık seans (`KONUM … AÇIK`) varsa "paralel oturum şüphesi" beyan et; commit yalnız `git add <yol>`.
5. **Kök kanon kontrolü:** `ls ../AGENTS.md ../sablonlar/skills/ogren/SKILL.md` ikisi de var mı; yoksa dur, Salih'e söyle. `jarvis/**`, `friday/**`, diğer alan dizinleri okunmaz (hook keser; denemeyi sapma olarak yazma, tasarımdır).
6. **Seansı aç:** `durum seans-ac --alan <alan> --hedef "<tek cümle>"` — hedef Salih açılışta beyan ettiyse aynen, yoksa `SIRADA` ilk işten türetilir ve brifte teyide sunulur. Komut oturum adını verir (`<tarih>-<alan>`); kapanışta gerekir, brife yaz.
7. **Brif (tek ekran):** tek satır konum · sırada/bekler · şerit başına sıradaki hafta ve pratik `KALAN` · bekleyen iskelet/devir · Salih'te bekleyen hükümler (`salih_karar`) · bu seansın hedef cümlesi · oturum adı.
8. **Model beyanı:** oturum Sonnet 5 varsayılan; Salih "bugün Opus" dediyse brifte tek satır `eskalasyon: Opus (Salih beyanı)` ve teslim kaydına `sayaclar.model`.
9. Salih şerit adı verdiyse ("seans başı, evals") brif sonrası `ogren` skill'ine geç; ders iskeleti `cc/gelen/`'de yoksa `## Kalan`'dan devam, yeni hafta açma.
10. Frenler: karar verme · kanon yazma · `main`'e push (kendi oturum dalına push + PR serbest, EK-5) · pratik = Salih'in eli.
