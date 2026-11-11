> **İNGEST EDİLDİ · 2026-08-17** (masa KB-08/09/10, Salih imzası → `wiki/paralel-oturum-protokolu.md` + seans-acilis §1.4-1.5 + KILAVUZ; kural adayları KURAL oldu). Bu dosya tarihçe.

# COWORK DEVİR DOSYASI — PARALEL OTURUM KAYNAK ÇAKIŞMASI + İKİ EPİSTEMİK BULGU

> **HAM FİKİR / ingest edilecek.** Bu dosyayı staj hattındaki Carvis oturumu hazırladı; kanon değildir, ingest edilene kadar hiçbir maddesi kural sayılmaz.
> **Hazırlayan:** Carvis / staj oturumu — Claude Opus 5 · **Talep eden:** Salih · **Tarih:** 2026-08-12
> **md.49 beyanı:** Bu dosyada şirket şeması, gerçek veri veya iç doküman YOKTUR. İçerik yalnız **yöntem** düzeyindedir — staj işi bunların gözlendiği laboratuvardır, konusu değil. Kaynak olay kaydı: `~/staj başlangıç/gunluk/2026-08-12.md`.

---

## §0 — Niye bu dosya var

2026-08-12 staj gününde iki Cowork oturumu aynı çalışma ağacında paralel koştu. Gün içinde üç şey gözlendi; üçü de staj konusuna değil, **JARVIS'in kendi işletim biçimine** dair. Bu yüzden staj günlüğünde değil burada durmaları gerekiyor.

Üçünün ortak paydası: *JARVIS'in mevcut doktrini bu vakaları adlandırmıyor.*

---

## §1 — BULGU 1: Paralel vardiya protokolü çalışma-zamanı kaynağını kapsamıyor

### Olay

İki oturum, birbirinden habersiz, aynı makinede aynı işi kurdu. Oturum A `airflow-docker/` altına bir Airflow yığını ayağa kaldırdı. Oturum B (bu oturum) ayrı bir klasöre ikinci bir Airflow yığını kurdu. B'nin web servisi kalkarken:

```
Bind for 0.0.0.0:8080 failed: port is already allocated
```

B'nin beş servisi sağlıklı ayağa kalktı, altıncısı kalkamadı. Çakışma ancak **kurulum bittikten sonra**, çalışma anında fark edildi.

Ek israf: iki oturum aynı öğrenme adımlarını iki kez koştu ve aynı aracın aynı tuzağına (`list-runs -d` argüman değişikliği) ayrı ayrı takıldı.

### Doktrindeki boşluk

Mevcut paralel oturum kuralı (staj `CLAUDE.md`; JARVIS tarafında `KILAVUZ` paralel vardiya protokolü) **dosya/kanon** çakışmasını düzenliyor:
- yan oturum mevcut dosyayı düzenlemez, yeni dosya açar
- her vardiya kapsülde yalnız kendi satırını günceller

Gerekçe mekanik ve doğru: iki oturum aynı ağaçtadır, son yazan diğerini sessizce ezer, git yakalamaz.

**Ama aynı mekanik gerekçe, dosya olmayan paylaşılan kaynaklar için de geçerli ve orada kural yok:**

| Kaynak | Çakışma biçimi | Git yakalar mı |
|---|---|---|
| TCP portu | ikinci bağlama reddedilir | hayır |
| konteyner adı | ikinci `run` reddedilir | hayır |
| Docker volume / ağ | biri diğerinin verisini siler (`down -v`) | hayır |
| daemon durumu | biri motoru kapatır, diğerinin işi ölür | hayır |
| paylaşılan yerel DB / soket | sessiz durum bozulması | hayır |

Son satır bugün ayrıca gerçekleşti: bir oturum Docker motorunu bilerek kapattı (ders amaçlı), diğer oturumun ayakta bıraktığı konteynerler o anda öldü.

### Önerilen kural (taslak — onay bekliyor)

> **Paylaşılan kaynak freni.** Yan oturum bir servis/konteyner/port ayağa kaldırmadan önce mevcut durumu okur (`docker ps`, `lsof -i :PORT`) ve çakışma görürse **kurmaz, bildirir.** Aynı işi ikinci kez kurmak yerine mevcut olanı kullanır.
>
> **Motoru kapatma freni.** Paylaşılan bir daemon (Docker motoru vb.) yalnız diğer hatta iş kalmadığı doğrulandıktan sonra kapatılır.

### Neden JARVIS'e ait

Paralel vardiya JARVIS'in kendi kararı (m.36 revizyonu). Bugünkü çakışma o kararın ilk saha arızası. `PARALEL-VARDIYA-ILK-DENEME.md` zaten "deneme yapılıp aksaklıklar kaydedilince arşive iner" diyor — **bu, kaydedilecek aksaklıktır.**

---

## §2 — BULGU 2: Bozuk ortamda gözlenen davranıştan kural çıkarmak

### Olay

Bir iş akışı motoru bozuk bir ortamda koştu (macOS'ta `fork()` sonrası segfault döngüsü). Koşumun bıraktığı durum tablosu okundu ve ondan bir **davranış kuralı** türetildi. Aynı iş temiz bir ortamda tekrarlandığında davranış farklı çıktı — türetilen kural yanlıştı. Bozuk koşumdaki tablo, motorun davranışı değil, gözetmen sürecin işi ortadan zorla sonlandırmasının **artefaktı**ydı.

Kritik ayrıntı: **ortamın bozuk olduğu gözlem anında zaten biliniyordu.** Yine de o koşumdan kural türetildi. Yani arıza "bilgi eksikliği" değil, *kısmen bozuk bir gözlemin bozulmamış kısmının hâlâ geçerli sayılması*.

### Genel biçim

> Bir gözlemin geçerliliği, gözlendiği ortamın sağlamlığına bağlıdır. Ortam bozukken **hangi kısmın bozulduğu bilinmez** — dolayısıyla hiçbir kısmı kanıt sayılamaz.

Yaygın yanlış sezgi: *"Hata mesajı X'te, demek ki X dışındaki her şey normal."* Bozuk ortamda bunun garantisi yok.

### JARVIS'e bağlanma noktaları

- **Ölçüm bankı:** her ölçüm kaydına *ortam sağlamlığı* alanı düşünülmeli — ölçümün alındığı koşum temiz miydi, yoksa retry/timeout/kill görmüş müydü. Bugünkü vaka, bu alan olmadan geçersiz bir ölçümün geçerli görünebileceğini gösteriyor.
- **Adversarial doğrulama:** doğrulayıcıya sorulan soruya bir kalem daha eklenebilir — *"bu bulgu hangi koşumdan geldi, o koşum sağlıklı bitti mi?"* Şu anki doğrulama iddianın içeriğini sınıyor, **üretildiği koşumun sıhhatini** sınamıyor.
- **D/K/X etiketleme:** bozuk ortamdan gelen gözlem D (doğrulanmış) sayılamaz; en fazla K. Bugünkü hata tam olarak bir K'yı D gibi kullanmaktı.

---

## §3 — BULGU 3: "Yeşil yalan söyler"in simetriği — kırmızı da yalan söyler

### Mevcut kanon maddesi (staj hattından, 08-11/08-12)

> Yeşil sağlık göstergesi, iş yükünün koştuğunun kanıtı değildir. "Ayağa kalktı" ≠ "çalışıyor".

Kaynak vaka: altı servis `healthy`, arayüz HTTP 200, ama her iş `Invalid auth token` ile ölüyordu — çünkü bir yapılandırma anahtarının bölüm adı yanlıştı ve **sessizce yok sayıldı**.

### Bugün eklenen simetrik vaka

Bir adım `failed` göründü. Doğal okuma: *kod çalıştı ve hata verdi.* Gerçek: **kodun tek satırı çalışmadı** — süreç ilk komuta gelmeden öldü, `failed` etiketini gözetmen mekanizma zaman aşımından sonra yazdı.

### Birleştirilmiş biçim (kanon adayı)

> **Durum etiketi kanıt değildir; log kanıttır.** Bu iki yönlü çalışır: *yeşil* işin koştuğunu kanıtlamaz, *kırmızı* da kodun koşup hata verdiğini kanıtlamaz. Etiketi yazan, işi yapan bileşen değil onu gözleyen bileşendir — ve gözleyen yanılabilir.

Doğrulama katmanı rolü açısından pratik sonucu: **hem başarı hem başarısızlık raporu log'a inilerek sınanır.** Şu anki repertuarda yalnız birincisi var.

---

## §4 — Ingest kararı için özet

| # | Bulgu | Nereye ait | Aksiyon adayı |
|---|---|---|---|
| 1 | Paralel vardiya, çalışma-zamanı kaynağını kapsamıyor | `KILAVUZ` paralel vardiya protokolü + `PARALEL-VARDIYA-ILK-DENEME.md` aksaklık kaydı | "paylaşılan kaynak freni" + "motoru kapatma freni" maddeleri |
| 2 | Bozuk ortamda gözlemden kural çıkarma | ölçüm bankı şeması · adversarial doğrulama · D/K/X | ölçüme *ortam sağlamlığı* alanı; doğrulayıcıya koşum-sıhhati sorusu |
| 3 | Durum etiketi ≠ kanıt (iki yönlü) | doğrulama katmanı repertuarı | mevcut "yeşil yalan söyler" maddesini iki yönlü hâle genişlet |

**Ölçülmüş sayı yok** — üçü de tek vakalı gözlem. 1 ve 3 mekanizması açık olduğu için doğrudan kurala çevrilebilir; 2 daha geniş bir iddia, ingest sırasında daraltılması gerekebilir.

## §5 — Açık uçlar

- Bulgu 1'in kural taslağı staj tarafında da yazılmadı (Salih onayı bekliyor). İki taraf aynı kuralı ayrı ayrı yazarsa metinler ayrışır — **tek kaynak JARVIS olmalı**, staj `CLAUDE.md` ona pointer versin.
- Bu dosya `~/jarvis`'e commit'lenmedi. JARVIS commit disiplini (m.10 İngilizce mesaj, `[damıtma]` etiketi, m.9 push) staj oturumundan uygulanmadı — bilerek: `staj-kapanis` ritüeli jarvis kanonuna yazmaz, push üretmez. **JARVIS oturumunda commit'lenecek.**
