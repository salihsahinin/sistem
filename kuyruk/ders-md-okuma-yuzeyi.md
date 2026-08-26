# Ders borcu: MD okuma yüzeyi (Obsidian + QLMarkdown)

*Açılış: 2026-08-26, seans-17. Salih emri: "2'yi (QLMarkdown) nasıl kullanacağımı anlamadım, sonra öğretmek üzere not al."*
*Yöntem: sohbette partisyon partisyon; tanım → mekanizma → elle örnek → kontrol sorusu (GBM dersiyle aynı desen, bkz. `kuyruk/ders-gbm-ilerleme.md`).*

## Durum
| partisyon | durum | not |
|---|---|---|
| D1 QuickLook nedir, QLMarkdown ne yapar | **BEKLİYOR** (ders borcu) | asıl anlaşılmayan kısım; kurulum yapıldı, kullanım anlatılmadı |
| D2 İlk kullanım: izin verme adımı | BEKLİYOR | macOS 15+ uzantı onayı elle yapılır; Salih'in ekranında birlikte |
| D3 Obsidian okuma refleksleri | BEKLİYOR | ⌘O hızlı geçiş · ⌘⇧F depo araması · ⌘E mod değiştir · graf/backlink paneli |
| D4 Hangi araç ne zaman | BEKLİYOR | Finder'da tarama → QuickLook · kanon gezinme → Obsidian · yazma → VS Code |

## D1 için hazır malzeme (ders anında anlatılacak, şimdi okunması gerekmez)
- **QuickLook = macOS'un yerleşik "Space'e bas, önizle" mekanizması.** Finder'da bir dosya SEÇİLİ iken (açmadan) boşluk çubuğuna basınca çıkan pencere.
- **QLMarkdown = o pencereye .md yeteneği ekleyen uzantı.** Varsayılan macOS bir .md dosyasını düz metin gösterir (ham `#`, `|`, `[[...]]` işaretleriyle) — okunabilirlik sorununun Finder ayağı budur. Uzantı kurulunca aynı Space tuşu render'lanmış hâli gösterir: başlıklar, tablolar, kod blokları, Mermaid diyagramları.
- **Kurulum yapıldı:** brew cask `qlmarkdown` 1.5.2 → `/Applications/QLMarkdown.app` + `/opt/homebrew/bin/qlmarkdown_cli` (2026-08-26 10:4x).
- **Eksik adım (D2):** macOS 15+ uzantıyı kendiliğinden etkinleştirmez. Bir kez `QLMarkdown.app` açılır, ayrıca Sistem Ayarları > Genel > Giriş Öğeleri ve Uzantılar > Quick Look altında onay verilir. Bu adım Salih'in elinde (Katman-1 sınıfı değil ama GUI onayı Carvis'ten yapılmaz).
- **Doğrulama komutu (ders anında birlikte koşulur):** `qlmanage -p <dosya.md>` ya da Finder'da dosyayı seçip Space.

## Tetik
Salih "MD okuma dersini yapalım" / "QuickLook'u anlat" dediğinde. Tahmini süre 10-15 dk (D1+D2 birlikte, ekran başında).
