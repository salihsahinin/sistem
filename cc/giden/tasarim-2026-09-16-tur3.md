# Tasarım diyaloğu — tur 3 (Friday → Salih → Jarvis, AS-OF 2026-09-16)

Hüküm yok (m.31). Bu tur A1 formatının (md + lojik blok) ilk canlı koşumu. Aşağıdaki gözlemler bu tek koşuma dayanıyor (n = 1).

## (a) A1 lojik bloğu — işleyen ve bana yetmeyen

**İşleyenler (kanıtıyla):**
- **`DONE` çıktı başına** — m.42(h) karşılaştırması tek bakışta bitti: C1–C4'ün her biri amaçta bir karşılık buldu, çelişki çıkmadı. Tur-1 ve tur-2'de bu karşılaştırma bir sapma üretmişti.
- **`KAPALI_GÖZ_ÖZETİ`** — doğrudan işe yaradı: C1 §3b'deki deny listesi, Jarvis üst düzey girdilerini bu alanın gösterdiği envanterden aldı. Alan olmasaydı listeyi uydurmam ya da boş bırakmam gerekirdi.
- **`NİÇİN_ŞİMDİ`** — C2'nin neden bu turda istendiği (İB-83'ün Friday eşleniği) bloktan okunabildi; tur-2'de bu bilgi yalnız bağlamdaydı.
- **`ÖLÇEN`** — (d) sayımını "benim sayımım, doğrulama Jarvis'in" diye çerçevelemek için doğrudan dayanak oldu.
- **md → json türevi** — alan alan karşılaştırdım, çelişki yok. B2 (tur-2) bu turda tekrarlamadı.

**Yetmeyenler — bağlayıcı olması gereken bilgi, bağlayıcı olmayan düz yazıda kalmış:**

| # | Bilgi | Nerede duruyor | Neden sorun |
|---|---|---|---|
| a1 | Açılacak **URL** | `gorev-2026-09-16-tur3.md:71` (Gerekçe, "bağlayıcı değil") | Blok kaynağı yalnız adıyla anıyor ("R-permissions"). Bağlayıcı metne göre hangi adresi açacağım yazılı değil. Önerilen alan: `KAYNAKLAR: - R-permissions: <url>`. |
| a2 | **Oturum durumu** ("seans-acilis koşma, kapsülü yeniden okuma") | `:3` (giriş paragrafı) | Bu cümle kütük v0.3'ün `devir_id` mekanizmasını fiilen devre dışı bıraktı (bkz. b1). İşletimsel etkisi olan bir talimat bloğun dışında. Önerilen alan: `OTURUM: devam \| yeni` + `AÇILIŞ_ADIMLARI`. |
| a3 | **Kapanış adımları** (kapsül, pano, defter, commit, son mesaj) | `:74` (Gerekçe) | `DONE C4` bunların bir kısmını sayıyor (kapsül, pano), defter ve commit ise yalnız düz yazıda. Önerilen alan: `KAPANIŞ:` listesi ya da `DONE C4`'e eklenmesi. |
| a4 | **"Emir-kaynaklı sapma" tanımı** | `DONE C3` (d) yalnız adıyla anıyor | Geçiş ölçüsünün sayım birimi tanımsız: bir dalı (D1–D4) izlemek sapma mı, bir belirsizliği yorumlamak sapma mı? Sayım yapanın yorumuna kalıyor (bkz. d). |
| a5 | **Açılış kartı** | hiçbir yerde | `DONE C4` "pano kartı `BİTEN`" istiyor, ama bu devir için panoda kart yoktu. Kartı açmak örtük izinle benim işim oldu. Blok bunu söylemiyor. |

Küçük not (json türevi): `olcen` alanı `yetki` altına düşmüş, `kimlik` ya da `gorev` altında olması beklenirdi; `kapali_goz_ozeti` iki yolu tek bir dizede taşıyor, liste değil. İkisi de bu turda bir soruna yol açmadı.

## (b) Bu koşumda yeni eksik / çelişki

**b1 — Kütük v0.3'ün `devir_id` alanı bu devirde boş kaldı.** `hareket-kutuk.sh:36` kimliği `cc/gelen/.aktif-devir` dosyasından okuyor; o dosyayı `seans-acilis` md.2b yazıyor (`.claude/skills/seans-acilis/SKILL.md:10`). Emir `seans-acilis`'i koşmamamı söyledi (`:3`) ve `cc/gelen/` yazma izninde değil. Dosyayı yazmadım; bu turun kütük satırlarında `devir_id: ""` var. Sayacı tur-2'deki gibi zaman damgasıyla ayırdım. B1 (tur-2) düzeltmesi, "oturum devam ediyor" hâlinde işlemiyor.

**b2 — Kilidin başlık yorumu ile Bash dalı farklı şey söylüyor.** `okuma-izin.sh:4` "izinli kökler dışı → exit 2" diyor. `:33-41` ise Bash için yalnız Jarvis'e ait yazılışları aday yapıyor. Bash ile Jarvis olmayan repo dışı her yol geçiyor (C2 Z1). Buna staj alanı (md.49) da dahil.

**b3 — Kullanıcı düzeyi talimat ile Friday sözleşmesi git akışında ayrışıyor.** `~/.claude/CLAUDE.md` (Karar 95/96) şunu diyor: "yan oturum kendi branch'inde çalışır … seans sonunda push + PR açar". Friday'in `CLAUDE.md` §5'i ve `settings.json` deny listesi ise push'u kesiyor; Friday bugüne kadar `main` üzerinde commit etti. Friday'in "yan oturum" sayılıp sayılmadığı yazılı değil. Bu turda Friday sözleşmesine uydum: `main`, push yok.

**b4 — Kullanıcı düzeyi üslup kuralı ile repo metinleri ayrışıyor.** `~/.claude/CLAUDE.md` bütünü büyük harfli vurguyu yalnız kısaltmaya ya da backtick içindeki durum jetonuna bırakıyor ("`VAR` gibi"). Friday'in `CLAUDE.md`'si, `core/rol.md` ve emir blokları ise bu biçimi yoğun kullanıyor (örn. "dosya `VAR`", "`SICAK`", "`YOK`"). Bu turun çıktılarında kendi metnimi kurala göre düzelttim; kanon ve emir metinlerine dokunmadım.

**b5 — Belge alt sayfası araçla okunamadı.** `settings-reference` sayfası kırpılmış döndü, yalnız dizin satırı geldi (C1 §0). 1-derinlik kuralı sayfayı açmaya izin veriyor, ama araç madde gövdesini getirmedi. Büyük referans sayfaları için B5 kuralı tek başına yetmiyor; bir "bölüm çapası" (`#permissions-blockreadsoutsideworkingdirectories`) ile hedefli okuma gerekebilir.

## (c) Sorular (≤5, bilgi soruları)

1. Friday bir "yan oturum" mu sayılıyor — Karar 95'in branch + PR akışı Friday reposuna da uygulanıyor mu, yoksa Friday §5'in "push yok, `main`" kuralı mı geçerli (b3)?
2. "Oturum devam ediyor" hâlinde `.aktif-devir` dosyasını kim yazmalı — emri yazan Jarvis mi (dosyayı emirle birlikte bırakarak), yoksa Friday mi (o zaman `cc/gelen/.aktif-devir` yazma iznine girmeli) (b1)?
3. Jarvis'in İB-83 kilidi alt-ajana hangi Friday dosyalarını okutuyor — işçinin Friday'in kapsülünü ve defterini görmemesi de bir hedef mi (C2 §2, Ö3)?
4. Jarvis'in `okuma-izin-test.sh` koşumu C2'deki Z1–Z3 vakalarını da kapsayacak mı (Ö1)?
5. `settings-reference` maddesinin gövdesini almak için Jarvis tarafında başka bir okuma yolu var mı (b5)?

## (d) Sapma sayımı (Friday'in sayımı; doğrulama Jarvis'in — `ÖLÇEN`)

**Bu devirde emir-kaynaklı `[sapma]` sayısı: 0.**

Sayılmayan ama işaretlediğim üç durum (a4'teki tanım boşluğu yüzünden açık yazıyorum):
1. `settings-reference` sayfasını açtım — B5'in 1-derinlik kuralı içinde, `YASAK` listesinin istisnası. Sapma değil.
2. `cc/gelen/.aktif-devir` dosyasını yazmadım — md emrine uygun davrandım; sonucu (b1) bir mekanizma eksiği, emirden sapma değil.
3. Bu devrin pano kartını kendim açıp kapattım — örtük izin (m.42(h)). Sapma değil.

Seri: tur-1 **2** · tur-2 **1** · tur-3 **0**. Geçiş ölçüsüne göre (arka arkaya 2 devirde 0) A1 → A2 için **1/2**.

Çekince: 0'ın bir kısmı a1–a3'ten geliyor. Bağlayıcı olmayan düz yazıyı talimat gibi okudum. Düz yazıyı yok sayan bir okuyucu URL'yi bloktan bulamaz ve bir sapma üretirdi. Ölçü, bağlayıcı metnin eksiğini değil, benim okuma biçimimi ölçmüş olabilir.
