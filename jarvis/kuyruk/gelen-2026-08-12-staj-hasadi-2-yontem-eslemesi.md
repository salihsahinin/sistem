# Staj hasadı 2 (2026-08-12): JARVIS yöntemlerinin dış-alan doğrulaması

*Kaynak: staj oturumu 2026-08-12, kapanış turu (analytic-database tespit görevi + oturum kapanışı). Kaydeden: Carvis, staj yüzeyi. Statü: Katman-2 ingest — kanon DEĞİŞMEDİ, aday kayıtları düşüldü.*

*Kardeş dosya: `gelen-2026-08-12-staj-hasadi.md` (aynı gün, görsel artefakt doğrulama). O dosya düzenlenmedi; bu, kapsamı dışında bıraktığı kalemleri taşır.*

## Sınır kaydı (md.49)

İzin: Salih, 2026-08-12 seans kapanışı — *"jarvis bağlamında jarvisi geliştirirken işimize yarayacak olanları da jarvis dosyasına ingestle."*

Taşınan: **yalnız yöntem ve kendi kanonumuza dair gözlem.** Şirket şeması / gerçek veri / iç doküman taşınmadı — bu turda üretilmedi de (ETL malzemesi kurgu `araclar` tablosu üzerinden gitti). Ham vaka staj tarafında: `~/staj başlangıç/gunluk/2026-08-12.md`.

---

## 1. ★ Ana bulgu: JARVIS kanonu, veritabanı literatürüyle bağımsız yakınsamış

Salih'in 11 Ağu görevi (*"analytic database temelinde hangi bulgulara sahibiz"*) kanon taramasıyla koştu: `raporlar/` 140+ dosya · `kuyruk/` · `wiki/` · `cc/` · `tools/`. Çıkan asıl şey taşınabilir sermaye listesi değil — **kanonun, o literatürü hiç okumadan aynı yere düştüğü noktalar.**

| JARVIS kanonu | Bağımsız karşılığı (veri mühendisliği) |
|---|---|
| **m.8 çürüme kuralı** — satır silinmez, üstü çizilir + çürüten kaynak yazılır | **SCD Type 2** (Kimball): üzerine yazmak (Type 1) tarihi yok eder; yeni satır + yürürlük tarihi tarihi korur |
| "Granülerlik kontrolü = tek en değerli test" (S5-A3) | Kimball: **grain'i ilan etmek** tasarımın kilit adımı, boyutlar seçilmeden ÖNCE yapılır |
| **CoVe-Factored** (m.40b: antiteze iddia verilir, gerekçe verilmez) | Anthropic taze-bağlam inceleyicisi: alt-ajan *yalnız diff'i ve ölçütleri görür, üreten akıl yürütmeyi görmez* — iki bağımsız hattan aynı ilke |
| **Paralellik vergisi** (token×zaman: takım ≈ tek ajanın 3-4 katı; kazanç > koordinasyon vergisi değilse takım kurma) | Stonebraker 1985: shared-nothing tercih edilir **ama** dağıtık deadlock detector + çok-fazlı commit gerektirir — MPP'nin shuffle bedeli |
| **Adlandırılmış tripwire** deseni (`2026-07-10-arastirma-1-index-mimarisi.md`: "Mimari 1 şimdi, Mimari 3'e tripwire'larla") | "Ne zaman ayrı OLAP'a geçilir" sorusunun tarafsız sayısal eşiği **yoktur**; ölçülebilen şey girişimdir (kilit bekleme, autovacuum gecikmesi, replikada iptal, p99) |
| **m.20 pointer** — ham veri taşınmaz, adresi taşınır | **Geç materyalizasyon** (~3× ölçülmüş kazanç) ve ELT: dönüşümü veriyi taşıyarak değil, durduğu yerde yap |
| **m.39 rakam damgası** (GA'sız satır bankaya girmez) | Analitik raporlamanın kendi disiplini: sayının yanında n + kaynak + tazelik yoksa o sayı henüz bulgu değil |
| **Duvar-saati ≠ düşünme süresi** (bekleme süreyi şişirir, token yakmaz) | Kuyrukta bekleme (Redshift WLM varsayılan 5 slot · Snowflake 8) ≠ tarama maliyeti; yavaş sorgu ile sıra bekleyen sorgu ayrı teşhis |

**Neden JARVIS için değerli:** bunlar staj bilgisi değil, **kanonun dışarıdan sınanması**. Olgun bir mühendislik alanı aynı problemlere bağımsız olarak aynı cevapları vermiş. En güçlüsü ilk satır: m.8 ile SCD Type 2 aynı kararın iki alandaki hâli, ve ikisi de aynı gerekçeyle savunuluyor (kayıt "şu an doğru bildiğimiz"i değil "ne bilip ne zaman öğrendiğimiz"i tutar).

**Statü:** gözlem, ölçüm değil. Ölçüm bankına girmez (m.39). Wiki sayfası adayı — `[[adversarial-hayatta-kalma]]` ve `[[olcum-banki]]` sayfalarına "dış doğrulama" satırı olarak da düşürülebilir. Karar alınmadı.

**Kapsam dürüstlüğü:** eşleme tek yönlü kontrol edildi (kanon → literatür). Ters yön — literatürün söyleyip kanonun kaçırdığı şey — bu turda taranmadı. Aday sonraki tur.

---

## 2. Birleşik sayfa adayı güçlendi: "üretici aracın kendi beyanı kanıt sayılmaz"

Kardeş dosya bunu n=3 ile aday göstermişti. Aynı gün **4. yüzey** çıktı:

| # | Yüzey | Gösterge ne dedi | Gerçek |
|---|---|---|---|
| 1 | Görsel artefakt | dosya üretildi, hata yok | 96 px etiket örtüşmesi + 10 görünmez ok başı |
| 2 | Airflow JWT | 6 servis `healthy`, arayüz HTTP 200 | her task `Signature verification failed` ile öldü |
| 3 | Docker Desktop | pencere açık, süreçler listede | motor `/Volumes/` altındaki DMG kopyasından koşuyordu, VM ölüydü |
| 4 | Redshift `PRIMARY KEY` | tanım kabul edildi, hata yok | denetlenmiyor — ama sorgu planlayıcı ona inanıyor, yanlış sonuç makul görünüyor |

Ortak yüklem: **kapının kanıtı gösterge değil, koşum sonucu olmalı.** Dördünde de sistem "iyiyim" dedi ve iş yükü çalışmıyordu.

**JARVIS'e doğrudan dokunduğu yer — bu kritik:** m.41'in koşullu-kilit şerhi (30-6 ölçümü: *kilit ayar-dosyasının YÜKLENMESİNE bağlı*) **aynı sınıfın beşinci vakasıdır.** Deny kuralı `settings.json`'da yazılı olması onun yürürlükte olduğunun kanıtı değil; kanıt, engellenmesi gereken çağrının fiilen engellendiğini görmektir. K-010'un A2 kapısı (*"PreToolUse kilit canlı PASS"*) bunu zaten koşum olarak istiyor — yani kanon doğru kurulmuş, ama gerekçesi şimdi 5 bağımsız vakayla desteklenir hale geldi.

**Statü:** wiki sayfası adayı. Kardeş dosya "acele değil" demişti; n 3'ten 5'e çıktığı için **isimlendirme eşiği aşıldı** kanısındayım, ama sayfayı açmadım — kardeş oturumun bilinçli erteleme kararını tek taraflı bozmamak için. Karar JARVIS vardiyasına.

---

## 3. Paralel yazım deseni — sahada kanıtlandı

Bugün `gunluk/2026-08-12.md` dosyasına **dört ayrı oturum** yazdı (≈13:30 · ≈19:53 · ≈19:54 · ana hat). Tek dosya, tek çalışma ağacı, sıfır kayıp.

Çalışan kural: **ekleme-esaslı yazım** — kimse başkasının satırını silmez/düzenlemez, herkes ilgili bölümün ALTINA `— oturum ~HH:MM` çizgisiyle ekler. Yazmadan hemen önce dosya yeniden okunur.

Gerekçe mekanik ve JARVIS'in her paralel vardiyası için geçerli: **aynı çalışma ağacında son yazan diğerini sessizce ezer, git bunu çakışma olarak yakalamaz** (iki farklı klon değil, tek dosya üzerine ardışık yazım).

Bu turda ölçülen arıza: 0 kayıp, ama **1 doğruluk hatası** — ana hat, dosyanın tamamını okumadan "bugün tahmin çevrimi hiç koşmadı" yazdı; yan hat aslında 3 tahmin koşturmuştu. Düzeltildi. Ders: *ekleme güvenli, ama **iddia** yazmadan önce dosyanın tamamı okunur.*

**Statü:** `staj-kapanis` skill'ine kural olarak girdi (adım 1.1 + gotcha). JARVIS tarafında m.41 ailesine genelleme adayı.

---

## 4. Yol ayrımı — kanon borcu

Salih kararı 2026-08-12: staj çıktıları `~/staj başlangıç` (yerel git, **remote yok ve kurulmayacak**), JARVIS yalnız işletim kanonu. `jarvis/staj/` kapatıldı, içeriği taşındı, pano K-022 pointer'ı güncellendi.

Bu md.49'un operasyonel hâli — sınır beyanı artık dosya sistemiyle uygulanıyor, disiplinle değil.

**Borç:** `kuyruk/senaryo-defteri.md`'ye karar satırı düşülmedi. Gerekçe: defter ~141KB/48KB **FLAG** — damıtma açılmadan büyütmemeyi seçtim (m.34 hattı). Satır, damıtma vardiyasında düşülecek.

**İkinci gözlem:** skill'ler artık iki evde — `~/jarvis/.claude/skills/` ve `~/staj başlangıç/.claude/skills/` (`staj-acilis`, `staj-kapanis`). K-016'nın (JARVIS-yapımı skill turu) sayacına giren iki yeni skill; ayrıca "skill nerede yaşar" sorusu artık tek cevaplı değil. Kayıt düşüldü, karar alınmadı.

---

## Bağlar

[[adversarial-hayatta-kalma]] (dış doğrulama satırı adayı) · [[olcum-banki]] (m.39 karşılığı) · [[pointer-sistemi]] (m.20 ≡ geç materyalizasyon) · [[token-x-zaman]] (paralellik vergisi ≡ shared-nothing bedeli) · kardeş: `gelen-2026-08-12-staj-hasadi.md` · staj tarafı ham kayıt: `~/staj başlangıç/gunluk/2026-08-12.md`

---
*İNGEST EDİLDİ · 2026-08-21 damıtma turu (triyaj: NOOP — içerik karar-borcu kütüğünde izleniyor: ai2ai+ölçek-yasaları → KB-36 kutu-adayları [masada] · tavan-rejim → KB-27 Karar 39 · staj-hasadı → KB-10 H4/H6 kararı; bu dosya bronz kaynak olarak yerinde kalır, m.8).*
