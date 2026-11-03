# Mod iterasyonu 2026-11-03: jarvis-oda v0.5 + jarvis-graf v0.2 (Salih emri; Jarvis planı; Opus yazar)

Kaynak kanon: `jarvis/mods/jarvis-oda/hooks/register.tsx` (673 satır), `jarvis/mods/jarvis-graf/hooks/register.tsx` (268 satır), tipler `*/types/index.d.ts`. Motor API: `jarvis-oda/.claude-plugin/types/claude-code/index.d.ts`. Doğrulama: `claude plugin validate mods/<mod>`; canlı test: `claude --plugin-dir <yol>` ya da `~/.claude/dev-mods/<oturum>/<mod>/` kopyası.

## Motor gerçekleri (Jarvis okuması, bu tasarımı kısıtlar)
- `Svg isInteractive` yalnız hover/tooltip verir; tıklama olayı **yok**. Tıklanabilir düğüm = `Button`. Grafta tıklama, SVG'nin altındaki düğme ızgarasıyla yapılır.
- Pane gövdesini motor kaydırır (`ui.scroll`). Sohbetin sığmaması kod kesmesinden (`slice(-10)`): çözüm pencere durumu (offset) + "önceki / sonraki" düğmeleri, ya da tüm turlar + `rows` isteği.
- `$.ui.view({ agentId })` ana transkripti işçiye çevirir; işçi adı ya da yeşil `#N` etiketi bu çağrıyı tetikleyecek `Button` olmalı.
- `Link href="file:///..."` tıklamada dosyayı yüzeyin açtığı gibi açar; `cmd /c start` yolu kırılgandır (boşluk, Türkçe karakter, python3 yokluğu).
- Atomlar plugin başına; oda ↔ graf köprüsü için ortak kanal `$.store` değil **dosya**: `ortak/akis-graf.json` zaten var, oda görevine `isId` eklenir.
- `turn.step` / `tool.call` olayları `agentId` taşır; işçi akışı kaydı mevcut (`hareket`).

## Mimari (Salih sonra soracak; burada tanımlı, kodda uygulanır)
Tek paket değil, iki mod kalır; her mod içinde **katmanlı dosya ayrımı**:
```
<mod>/hooks/register.tsx      yalnız kayıt: on(...) satırları, 60-100 satır
<mod>/src/durum.ts            veri modeli + atomlar + yükle/kaydet (saf fonksiyon, UI yok)
<mod>/src/araclar.ts          tool.call işleyicileri (oda) / dosya-süreç çağrıları (graf)
<mod>/src/metin.ts            oda_oku metni, işçi emri derleyici (saf)
<mod>/src/pano.tsx            ui.render ağacı; alt bileşenler: GorevSatiri, Sohbet, CanliAkis, Detay
<mod>/src/ortak.ts            saat(), kisa(), yol bulma (iki modda aynı içerik; kopya, paket yok)
```
Kural: `pano.tsx` durumu okur, yazmaz (yazım `araclar.ts` fonksiyonlarıyla). Her dosya başında 2 satır Türkçe amaç. `hooks.json` `modules` tek giriş kalır; `register.tsx` `src/` içini import eder (çalışmazsa Opus bunu ilk raporda yazar, tek dosyaya düşmez; bölünmüş import'un yüklendiğini `claude plugin validate` + canlı açılışla kanıtlar).

## A. jarvis-oda v0.5

A1. **İşçiye tıkla → işçinin sohbeti.** Görev satırındaki `#N` + başlık `Button` olur (`onPress: $.ui.view({ agentId })`); canlı akış satırındaki yeşil `#N` de aynı düğme. Ortak sohbette `işçi #N` adı da düğme. Üstte sabit "◀ ana sohbete dön" düğmesi yalnız bir işçi izlenirken görünür.
A2. **Sohbet kaydırma.** `sohbetPencere` durumu (`{ ofset: number, boy: number }`, varsayılan boy 12): "◀ önceki 12 · sonraki 12 ▶ · en son" düğmeleri; yeni mesaj geldiğinde pencere en sondaysa orada kalır. Aynı pencere mantığı canlı akış ve son olaylar için (`boy` 12 / 6). Pane açılışında `rows` isteği içerik kadar.
A3. **Dinamik pano.** Bölümler katlanır (`▸/▾` düğme, durum atomunda `acik: Set<bolum>`): görevler · öneriler · sohbet · canlı akış · olaylar. Varsayılan: görevler + sohbet açık.
A4. **Görev → iş düğümü köprüsü.** `OdaGorev.isId?: number`; `oda_gorev_ver` isteğe bağlı `isId` alır; verilmezse ve `durumKaydi: true` ise mod `durum.exe ac --alan jarvis --is <baslik> --sonraki <emir ilk cümle> --oturum <oda id>` koşturur, çıktıdaki `#id`'yi yazar; görev bitince `durum.exe bitir <id>`. Görev satırında `iş #id` düğmesi `$.ui.open({ id: 'jarvis-graf', focus: true })` + köprü dosyası `ortak/graf-secim.json` (`{ secili: "is:<id>", ts }`) yazar; graf modu bu dosyayı 2 sn'de bir okur, seçimi alır.
A5. **İş nodu sınıflandırması (bağlam karışması freni).** `oda_gorev_ver` zorunlu `sinif` alanı:
   - `izole`: emir tek başına yeter; işçi emri = yalnız emir + rapor şeması (plan turu **eklenmez**).
   - `planli`: son 3 plan turu eklenir (bugünkü varsayılan davranış).
   - `dosyali`: `dosyalar: string[]` zorunlu; emir başına "yalnız bu dosyalar okunur/yazılır" + yazma-izni listesi; işçi başka dosyaya `Edit/Write` yaparsa `tool.call` kancası reddeder (`deny`), hareket kaydına ✗ düşer.
   - `rol`: mevcut `ajan` yolu (bağlam yok, yapan ≠ ölçen).
   Ek alanlar: `done: string` (zorunlu, tek cümle), `butce?: number` (araç çağrısı tavanı, varsayılan sınıfa göre izole 10 · dosyali 15 · planli 20; aşımda işçiye uyarı mesajı düşer, 1.5× aşımda görev `hata`). Pano görev satırında `[sinif]` etiketi + çağrı sayacı `7/15`. `prompt.compose` metni Jarvis'e kuralı söyler: "görevi, işçinin sınıf dışı bağlama ihtiyaç duymayacağı kadar küçük böl; `dosyali`'de dosya listesi ≤ 4".
A6. Ad: `plugin.json` 0.5.0; README v0.5 paragrafı; kaynak başlık yorumu 2 satır.

## B. jarvis-graf v0.2

B1. **Görsel yeniden tasarım (seans şeritleri).** Satır = seans (y ekseni; açılış sırasına göre, her alan ayrı renk tonu); hedefler en üstte ayrı şerit; iş düğümü onu açan seansın satırına, x = açılış zamanı (lineer ölçek, gün çizgileri + tarih etiketi). Düğüm yarıçapı ≥ 7 px, iş numarası düğüm içinde; seans etiketi satır başında tam ad. Genişlik pane sütunu × 8 px, en az 900; yükseklik satır sayısı × 34 + 60. Kenarlar: `hizmet` mor ince, `girdi` kesik, `bitirdi` yeşil kalın. Üstte açıklama şeridi (renk → durum). Seçili düğüm beyaz halka.
B2. **Tıklanabilir ızgara.** SVG'nin altında, aynı seans sırasıyla satır başına bir `Box`: seans adı düğmesi + o seansın işleri `Button` (`#id` + 30 karakter). Tıklama `secili` yapar; SVG seçili halkayı çizer.
B3. **Detay paneli zengin.** Seçili iş için: etiket tam · sonraki eylem tam · durum + açılış/al/bitir yerel saat · oturumlar (her biri düğme → o seans seçilir) · kenarlar yönlü (girdi bekliyor / hizmet eder / açan seans) · **kütük olayları** `ortak/durum-olay.jsonl` (`id` eşleşen `ac/al/bitir/bayatla`, kanıt satırları) · hedefse ona hizmet eden işler listesi · etikette "Karar NNN" varsa `kuyruk/senaryo-defteri.md` paragrafı (ilk 600 karakter) · seans kaydı varsa `Link file://`. Seçili seans için: hedef cümle, tutuldu mu, açtığı/bitirdiği işler, teslim kaydı linki.
B4. **HTML aç onarımı.** `python3 tools/akis-graf-html.py` yerine `durum.exe` yoksa `py -3` → `python` → `python3` sırasıyla dener; çıktı yolunu `file://` URL'ye çevirip pane'de `Link` olarak gösterir (tıklama yüzeyin açtığı gibi açar) ve ayrıca `powershell -NoProfile -Command Start-Process -FilePath <yol>` dener; hata metni pane'de kalıcı (toast değil).
B5. **Oda köprüsü.** `ortak/graf-secim.json` izlenir (A4); varsa seçimi alır ve dosyayı siler. `/graf is:<id>` argümanı da seçer.
B6. Ad: `plugin.json` 0.2.0; README yenilenir.

## Done ve doğrulama (her madde için)
- `claude plugin validate mods/jarvis-oda` ve `mods/jarvis-graf` PASS çıktısı raporda.
- Canlı: yeni oturumda `/oda` + `oda_ac` + 2 görev (`izole` + `dosyali`, dosyali'de kapsam dışı Edit reddi görülür) + sohbet 20 mesaj kaydırma + işçiye tıklama; `/graf` + düğüm tıklama + detay + HTML Link açılışı. Ekran görüntüsü yolu raporda.
- Commit: karar başına ayrı, İngilizce, `[icra]`, pathspec `git add jarvis/mods/...`; yan oturum kendi dalında, sonunda PR; push Salih beyanıyla.

## Sıra
A2 → A1 → A3 → B4 → B1 → B2 → B3 → A5 → A4 → B5 → README/sürüm. Her blok bitince kısa rapor (ne değişti · doğrulama · açık soru); Salih fork oturumunda bakar, Jarvis planı revize eder.

## Ek (Salih, 2026-11-03 ikinci tur; ekran görüntüsü: graf paneli)
B7. **Kırmızı hata satırı.** Pane'de "ortak/akis-graf.json bulunamadı (cwd depo ya da jarvis/ olmalı)" graf yüklü olduğu hâlde görünüyor. Sebep: `yolBul` yalnız cwd ve cwd/.. 'ye bakıyor; cwd `jarvis/mods/...` gibi derin olunca bulamıyor ve `hata`yı yazıyor. Çözüm: cwd'den yukarı doğru her üst dizinde `ortak/akis-graf.json` ara (kök dahil); bulunan yol `gorunum.yol`'a yazılır ve sonraki yoklamalarda o yol kullanılır; bir kez bulunduysa yeniden arama başarısız olsa bile `hata` yazılmaz (yalnız ilk yüklemede hata gösterilir).
A7. **Sohbet akışında işçi ↔ iş sınıflandırması.** Ortak sohbet ve canlı akış satırları `[#N · <görev başlığı ilk 24> · <sinif>]` etiketi taşır; `kim` düğmesi (A1) yanında. Rapor satırı tıklanınca katlanır/açılır (satır içi `▸ rapor` düğmesi; açıkken tam metin, `Markdown` bileşeniyle). Jarvis ve Salih mesajları kendi renginde, işçi mesajları görev numarasının rengiyle (görev başına sabit renk paleti, 8 renk döner).
B8. **Dinamik HTML (tools/akis-graf-html.py + sablon).** Üstteki "bitmiş görevler" sırası tıklanabilir olur: her kutu tıklanınca detay paneli açılır (aynı veri: etiket, sonraki eylem, kütük olayları, hizmet ettiği hedef adı görünür etiket olarak, oturumlar). Hedef bağı her iş kutusunda `H<no> · <hedef ilk 30>` olarak yazılır. Üst özet şerit tam listeye genişletilebilir (`tümünü göster`). HTML'e isteğe bağlı **oda görünümü**: `jarvis-oda` `oda:<id>` kaydını `ortak/oda/<id>.json` olarak dışa yazar (her `odaKaydet`'te); HTML üretici bu dosya varsa "Oda" sekmesi ekler (görevler · sınıf · işçi raporları tıklanınca açılır · sohbet tam akış). Sıra: B7 hemen (A2'den önce), A7 A3'ten sonra, B8 B3'ten sonra.

## Ek 2 (Salih, 2026-11-03 üçüncü tur): iki yol yan yana + oturumlar arası mesaj
- **İş bölümü:** B8 HTML parçası (`jarvis/tools/akis-graf-html.py` + `akis-graf-html.sablon.html`) oda işçisine (`zor` → Opus) verildi; fork bu iki dosyaya dokunmaz. Oda dışa yazma şeması (fork yazar, A4 sonrası): `ortak/oda/<odaId>.json` = `Oda` tipi aynen (`turlar`, `gorevler`, `oneriler`, `maksParalel`), her `odaKaydet`'te.
- **C1. Stigmerjik dış kanal (fork, B5'ten sonra).** Dış oturumlar (fork, öğrenme sekmeleri, alan ajanları) odaya **dosya üzerinden** katılır: `ortak/oda/<odaId>/gelen.jsonl` satırı = `{ts, kim, tur: "sohbet"|"rapor"|"oneri", metin, gorevId?}`; oda modu 3 sn'de bir yeni satırları okuyup `turlar`a ekler (pano + Jarvis uyandırma aynı yol). Dış oturuma mesaj: `oda_sohbet` hedef `@<oturum-adı>` ise satırı `ortak/oda/<odaId>/giden.jsonl`'a yazar **ve** Claude Code `SendMessage` ile iletir (mod içinden mümkün değilse Jarvis'e "SendMessage ile ilet" sonucu döner). `oda_katil` aracı: dış oturum kendini `{oturum, rol, dosyalar}` ile kaydeder; panoda "dış işçi" satırı (gri ●, akış yok, rapor dosyadan). Bu, iç işçi (kanca) ile dış işçi (dosya) farkını tek panoda kapatır; stigmerji = ortak dosya.
- **Oturumlar arası mesaj bugün:** her masaüstü oturumunda `ListAgents` + `SendMessage` var; öğrenme sekmesi "bunu jarvis oturumuna gönder" deyince ilgili Claude `SendMessage(to: "mod geliştirme jarvis [fdfc39]")` çağırır. C1 bunun odaya düşen, dosyada kalıcı hâlidir.
- **C1 ek (Salih):** dış oturumlar tek görevlik işçi değil, kalıcı oturumdur; odada ad ve işaret ayrı: `işçi #N` yerine `oturum <ad>` (ör. `oturum claude-mods`), işaret ◆ (işçi ● / ✓ / ✗), ayrı bölüm "Oturumlar (kalıcı)" görev listesinin altında; sohbet satırında `kim` = oturum adı, rengi gri-mavi sabit. `oda_katil` kaydı `{oturum, rol, dosyalar, acilis}`; oturum kapanınca satır silinmez, "ayrıldı" olur.

## Kapanış (2026-11-03; fork + oda işçisi; push Salih beyanı bekler)
Commit'ler: 241e551 B7 · a9db6bd oda v0.5 · 650762f B8 HTML (oda işçisi) · c914d5a graf v0.2 · 599a043 C1 oda v0.6 · de338b5 README/sürüm. Doğrulama: plugin test oda 8/8, graf 4/4; tsc rc=0; validate PASS.
Sapmalar (fork raporu): src → `hooks/src` (motor tsconfig) · masaüstü `file://` Link çizmez → aç/kopyala/Explorer düğmeleri · `graf-secim.json` silinmez (fs silme yok), zaman damgasıyla işlenir · C1 oturum başına `gelen-<oturum>.jsonl` (tek yazar) · commit blok değil mod grubu başına.
Motor gerçekleri (eklenen): kabuksuz `process.run`'da `python3` Store yönlendiricisine düşer → `py -3` önce · `$` nesneye konmaz, dosyalar arası yalnız fonksiyon argümanı · atom `read/update` tanımlandığı modülde.
Açık: canlı yeni-oturum testi (Salih); iki yol karşılaştırması tek blok üzerinden (plan gövdesi "Ek 2").
