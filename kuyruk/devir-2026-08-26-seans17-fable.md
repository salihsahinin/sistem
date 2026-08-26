# Devir — seans-17 → Fable oturumu (2026-08-26)

*Salih beyanı (10:5x, aynen): "son kararların planlanması pushların atılması yeni tasarımlar fable modeller yapılır onay yok kalan iş fable'a".*
*Bu oturum: Claude Code masaüstü, **Opus 5** — "ana-sıra ∧ en güçlü model" şartının model ayağı SAĞLANMIYOR → kanon kararı alınmadı, Katman-1 dosyalara yazılmadı.*
*Kural zemini: oturum sözleşmesi §4 (m.41 GK-2) · yan-oturum karar almaz, devir dosyasıyla taşır.*

## Bu seansta YAPILAN (Katman-2, kapandı — tekrar koşulmasın)
| İş | Kanıt |
|---|---|
| Silver bayattı → `tools/katman-hatti.py` koştu, exit 0, `uretim.head = HEAD`, test/sözleşme PASS | hat çıktısı |
| Obsidian okuma yüzeyi: `.obsidian/app.json` + `appearance.json` yazıldı (okuma modu varsayılan · readableLineLength · font 17 · tema=system · `userIgnoreFilters`: veri/bronz, veri/gorunum, veri/parquet, arsiv/claude-izler) | commit `42e0b47` |
| Gizli-klasör kuralı (sözleşme §2): `kaynak-kodu/obsidian → ../.obsidian` kapısı + `kaynak-kodu/README.md` tablo satırı | commit `42e0b47` |
| QLMarkdown QuickLook eklentisi kuruldu: `brew` cask `qlmarkdown` 1.5.2 → `/Applications/QLMarkdown.app` + `/opt/homebrew/bin/qlmarkdown_cli`, exit 0 | brew çıktısı |
| Ders borcu açıldı (Salih emri): `kuyruk/ders-md-okuma-yuzeyi.md`, 4 partisyon (D1 QuickLook nedir · D2 izin adımı · D3 Obsidian refleksleri · D4 hangi araç ne zaman) | commit `42e0b47` |
| **Karar 70** deftere yazıldı: ses/ekran kaydı onay kapısı | commit `441e4a6` |

## Fable'a DEVREDİLEN (Katman-1 · kanon · push)

### F-1 · Karar 70 deterministik sigortası — `.claude/settings.json`
Kural şu an yalnız davranışsal (defter + Carvis hafızası). `permissions.ask` listesine eklenecek aday satırlar — mevcut tek satır `Bash(git push:*)`, desen birebir aynı:

    "Bash(screencapture:*)", "Bash(rec:*)", "Bash(sox:*)"

**Açık alt-karar:** `Bash(ffmpeg:*)` dahil edilsin mi? Geniş eşleşme — ses/ekranla ilgisiz video dönüştürmede de soracak. Carvis (Opus) okuması: dar tut, ffmpeg dışarıda; ihtiyaç doğarsa eklenir. Hüküm Fable'ın.
**Neden bu oturumda yapılmadı:** dosya Katman-1 ∧ PreToolUse teli (`.claude/hooks/pretool-core-tel.sh`) Bash yazımını engelliyor; telin etrafından dolaşılmadı.

### F-2 · Kapsül bayat — `core/durum-kapsulu.md`
Kapsül "SEANS-16 KAPANDI 08:3x · sonraki ilk iş 0 = KB-62..68 masası" diyor. Gerçek: masa **7/7 bitti** (`189d663` + `581fbb6`, Karar 69 + EK). Kapsüle devredilecek olgular:
- Karar 69 (KB-62..66 → a/a/a/b/a) + EK (KB-67/68 → a/a) — masa TAMAM; İB-51, İB-52 açıldı
- **Karar 70** ses/ekran kaydı onay kapısı (F-1 sigortası bekliyor)
- Seans-17 icrası: Obsidian okuma yüzeyi + QLMarkdown + ders borcu `kuyruk/ders-md-okuma-yuzeyi.md`
- Silver TAZE (`441e4a6` anına kadar koştu)

### F-3 · KB-66 artığı — oturum sözleşmesi satır-takası
`wiki/anakronizm-freni.md` pointer'ı §6'ya girecek; **çıkacak satırı Salih seçer**, sözleşmeye hâlâ dokunulmadı (bütçe ≤80 satır / ≤7 KB; bir satır girer, bir satır çıkar).

### F-4 · Push (m.9)
`main` origin'in **18 commit** önünde (bu seansın `42e0b47` + `441e4a6` dahil; devir commit'iyle 19). Salih beyanı "pushların atılması Fable" → push Fable oturumunda.

### F-5 · Kalan icra borcu
İB-50 (katman-hatti kosum-sonuc grain ERROR) · İB-51 (kural-kümeleme araştırma borcu) · İB-52 (silver additive `cekim_tarihi`/`kaynak_tarihi` + N=3 kapanış tazeleme; İB-50 ile ortak tur önerildi). Toplam karar-borcu 113 kalem (Katman-1 69 · Katman-2 44), snapshot `441e4a6`.

### F-6 · Boyut tetikleri (damıtma adayı)
fikir-kutusu 26,4/20 KB · KILAVUZ 17,7/16 KB.

## Uyarı: paralel oturum
Salih teyit etti — **başka oturum açık**. Bu seansta tüm commit'ler hedefli `git add <yol>` ile yapıldı (`git add -A` kullanılmadı, H4). Fable oturumu aynı disiplini sürdürmeli; `git log` + bu dosya okunmadan koşum açılmasın (koşum-önü manifest kapısı).

## Not: bu seansta düşen tel kaydı
Bu devir dosyasının ilk yazımında `pretool-core-tel.sh` **yanlış-pozitif** verdi: heredoc gövdesinde "install" kelimesi ile sözleşme dosyasının adı yan yana geçtiği için `\b(mv|cp|...|install)\b.*(core/|CLAUDE\.md|\.claude/)` deseni eşleşti — hedef dosya `kuyruk/` altında, korumalı değildi. Hook'un kendi talimatı uyarınca komut yeniden ifade edildi (Write aracı), telin etrafından dolaşılmadı. Desen iyileştirme adayı: `install` yalnız komut başında/`|`-sonrasında aransın.
