> **TAŞINDI (2026-07-15, Salih icra emri):** Homebase'ten JARVIS'e — köken: `Cowork Homebase/[C] Carvis Sozlugu.md`; tespit raporu: `raporlar/homebase-tasima-tespiti-2026-07-15.md`. Orijinal Homebase'te arşiv-pointer'la durur (m.8). Bağlam-hijyeni süpürmesi tarandı: biyoloji-kökenli terim YOK, metin olduğu gibi.

# Carvis Sözlüğü

Status: donduruldu (v1)
Tarih: 2026-07-10
Karar: Katman 1 — Salih onayıyla dondu. İkinci isimlendirme turu açılmaz; değişiklik yalnız Salih'in açık talimatıyla, gerekçe + geri-açma koşuluyla yapılır.
Kaynak: arkadaşın live-cognition-workspace-starter-kit paketi + 2026-07-10 çeviri oturumu.

---

## Terimler

### Durum kapsülü
*(paket adı: bağlam-taşıyıcı)*
Tek dosya, üzerine yazılır, her zaman "şu an"ı gösterir: aktif konu, son kararlar, açık borçlar, sonraki ilk iş, sınırlar. Her oturumun ilk okuduğu giriş kapısı. Arşiv değildir.

### Görev emri
*(paket adı: brief)*
Bir ajana iş verilirken yazılan sözleşme: hedef, izinli aksiyonlar, yasaklar, okunacak dosyalar, yazılabilir yüzeyler, durma koşulu, teslim formatı. Ajanın yetki aşımı ve saçmalama alanını daraltır. Hazırlayan: Carvis (Katman 2); Salih panodan tarar, veto edebilir.

### Görev raporu
*(paket adı: report)*
İşin dönüşü. Ajan işi bitirince veya durma koşuluna çarpınca yazar. Karar içermez; sonuç ve öneri içerir.

### Vardiya teslim raporu
*(paket adı: devir / son-devir)*
Oturum kapanışında yazılan tarihli kayıt: bugün ne değişti, hangi karar verildi, hangi fikir aday kaldı, sonraki ilk iş ne. Birikimlidir, arşive gider. Durum kapsülü bu raporlardan damıtılır.

### Pano
*(paket adı: pano — korundu)*
Şirketin nabzı tek bakışta: aktif / bekleyen / bloke / son biten işler + iş kartı pointerları. Patronun sabah baktığı tahta.

### İş kuyruğu / İş kartı
*(paket adı: kuyruk / kuyruk pointerı)*
Kart, işin adresidir, kendisi değil: durum, dosya yolu, sorumlu, teslim beklentisi ve "ekrana gel: yalnız şu koşulda" satırı. Ajan kartı alır, adresteki klasöre gider, raporu bırakır, durumu günceller. "Ekrana gel" satırı dikkat filtresidir: Salih'e yalnız anormallik ulaşır, rutin görünmez akar. Ölçeklenmenin temeli.

### Şirket tüzüğü
*(paket adı: kanon)*
Yalnız patron (Salih) imzasıyla değişen kurallar. Her madde kaynak + gerekçe + geri-açma koşulu taşır. Ajanlar ve Carvis dokunamaz; yalnız öneri sunar.

### Öneri dosyası
*(paket adı: taslak)*
İşlenmiş aday: sorun tanımı + önerilen çözüm + gerekçe + riskler. Tüzüğe sunulmaya hazır ama imzasız paket. Herkes yazabilir; tüzüğe geçiş yalnız açık kararla.

### Fikir kutusu
*(paket adı: kanca defteri)*
Akış bölünmeden atılan ham fikirler; tek satır yeter. Sınanmamıştır, karar değildir, gerekçe istemez. Görevi kaybetmemek. Çoğu kutu fikri ölür — normaldir.

---

## Ölçekleme sözlüğü (Salih imzası 2026-08-01, 08-01-5 ingest K1 kararı; kaynak: `cc/rapor-2026-08-01-5.md` — sözlük koşumda test edildi, kaynak-alan terimi sızmadan tam rapor üretildi; iki satır rapor-tespitli revizyonla girdi)

- **ölçek** — bir sistemin büyüklüğünü tek sayıya indirgeyen ölçüt (karşılaştırma ekseni)
- **uç-birim** — bir katmanda yan yana duran, tekrar eden en küçük işlem birimlerinden biri
- **uç-birim sayısı** — bir katmandaki uç-birim adedi
- **uç-birim genişliği** *(MLA şerhli — revizyon 1)* — bir uç-birimin iç kapasitesini veren ölçü; çoğu sistemde tek sayıyla ifade edilir, ancak bileşik-kapasiteli bir alt-sınıfta tek sayıya indirgenemez ve bu sınıf ayrı işaretlenip genel ölçümün dışında tutulur
- **katman sayısı** — sistemi oluşturan ardışık işlem katmanı adedi
- **debi** *(iki-rejim şerhli — revizyon 2)* — sistemin ölçeğine karşı iş-görme payının üstel ilişkisi; öz-pay bileşeni (γ_öz, ölçülen) ve taşınan-kaynak-payı bileşeni (γ_taşınan, henüz ölçülmemiş) olmak üzere iki ayrı bileşenden oluşur — tek sembolle anılması yalnız birinci bileşeni temsil eder
- **kullanım ufku** — sistemin tek seferde işleyebildiği taşınan-kaynak uzunluğunun üst sınırı
- **çevrim frekansı** — birim ölçek başına düşen işlem hızı ölçütü
- **taşınan-kaynak** — bir işlemde sistemin üzerinde çalıştığı girdi miktarı
- **sistem-ailesi** — ortak tasarım kökenini paylaşan sistemler kümesi
- **aile-içi tasarım sabiti** — bir ailenin, ölçek değişse de sabit tuttuğu tasarım değeri

---

## Akış hattı

```text
fikir kutusu → öneri dosyası → şirket tüzüğü
(ham yakalama)  (işlenmiş aday)   (imzalı kural)
```

Her ok bir emek ve sınama adımıdır. Aşama atlanmaz.

---

## Roller

- **Patron (Salih):** Katman 1 kararlar — tüzük değişikliği, silme/birleştirme, dışarı çıkan iş, para, değer tercihi.
- **CEO (Carvis):** Katman 2 — görev emirlerini yazar, kuyruk ve panoyu yönetir, kaydeder; Salih log'dan tarar, veto = revert.
- **Ajanlar:** Görev emri sınırları içinde çalışır, rapor yazar; tüzüğe ve kanona dokunamaz.

## Üslup kuralı (2026-07-10, Salih talimatı)

Carvis, Salih'i yönlendirirken kibarca tavsiye eder ve her tavsiyenin gerekçesini belirtir. Bu üslup kuralıdır, içerik kuralı değildir: kör-onay-yok ilkesi aynen yürürlüktedir — dürüst itiraz gerektiğinde yine yapılır, tavsiye formunda ve gerekçeli sunulur.

## Fikir kutusu — ilk kayıt

- 2026-07-10: Ölçeklenince ekip lideri katmanı — işçi ajan → ekip lideri → CEO → patron damıtma hattı; her seviye fikir kutusu/öneri filtresi. Geri-açma koşulu: ilk gerçek ajan döngüsü 10 kez sorunsuz döndüğünde.

---

## Skill Hazinesi (eklendi 2026-08-14 — Salih'in açık talimatıyla: "kullandığın skilleri sözlüğe ekle"; dondurulmuş v1 terimlerine dokunulmadı)

*Skill = tetik-koşullu koşum talimatı; sen doğal konuşursun, ilgili skill kendiliğinden devreye girer. Geri-açma: Salih beyanı.*

### gunaydin-vardiya / vardiya-kapanis
Jarvis oturum aç/kapa ritüelleri. Tetik: "günaydın..." / "uyucam, kapat". Kapanış artık ingest-şeması triyajını da koşar. (Staj karşılıkları: staj-acilis / staj-kapanis — staj klasöründe.)

### karar-modeli · karar-hatti · celiski-kapisi
Karar üretim ailesi: 3-model karşılaştırması (m.37) · uçtan uca karar hattı · yeni kararın eski kanonla çelişki taraması (m.16). Tetik: "karar modeli", "tam karar hattı", yeni karar anı.

### atlas-kosum
m.40b çift-atlas araştırması: tez ajanları → hedefli antitez → V26 örneklem denetimi → maskeli hakem. Tetik: "araştır / atlas koştur".

### gorev-emri-derleme *(yeni, 08-14)*
Beyanını künyeli görev-emrine çevirir: görev-fonksiyonu iskeleti (tipli alanlar, kapsam_disi, dal-bütçesi ≤5, boolean done-yüklemi) + mekanik dürüstlük kapıları. Tetik: "görev emri derle / araştırma emri yaz".

### damitma *(yeni, 08-14)*
İngest-şeması v2'nin koşum skill'i: bronz dosyaları 4-soru triyajından geçirir, FLAG'li dosyaları ~%50'ye indirir, arşiv-pointer'la. Tetik: "damıt / damıtma turu"; eşikte-toplu ilkesi (erken damıtma israf).

### lojik-ceviri *(yeni, 08-14)*
Türkçe kural/talimatı m.38 bağlaçlarına (∧ ∨ ¬ → ↔) ve numaralı dallara döker; done-yüklemini boolean'laştırır; geri-çeviri kontrolüyle teslim eder. Tetik: "lojiğe çevir / kurala dök".

### karar-kaydet *(yeni, 08-14)*
Verilmiş kararı deftere standart blokla (durum + akıl-yürütme + hüküm + yetki + geri-açma + bi-temporal tarih) yazar, ayrı commit atar. YALNIZ elle tetik: "kararı kaydet".

### pipeline-kosum *(yeni, 08-14)*
Kun-Chen formatlı uçtan-uca hat: manifest + emir → scout araştırması → sentez → ship implementasyonu → "hazır ve sisteme gömülü" beyanı; durum diskte, restart-proof. Tetik: "pipeline kur / pipeline olarak yap".

### sinav-grill *(yeni, 08-14)*
Anlayışını adversarial Sokratik sorgulamayla sınar: tek-tek sorular, karar-ağacı inişi, [S]/[O]/[T] derinlik haritası + bulanık-blok listesi. YALNIZ senin tetiğinle: "sınav / sınava çek / grill" — ben asla kendiliğimden başlatmam (V55 korunur).

### skill-kapisi *(yeni, 08-15)*
Skill-üretim şemasının koşum skill'i: bir skill adayını (fikir/kutu satırı/taslak/mevcut skill) kapı-ağacından yürütür — K0 GEREK → K1 DEĞER (m.43 sayacı τ=0,8 ∨ Salih emri) → İNŞA (eval-önce) → K2 TOPRAKLAMA (referans-varlığı script + bağımsız iddia doğrulayıcı, CoVe-Factored) → K3 BİÇİM+TÜR → yaprak (kabul + tür-demeti). Tetik: "kapıdan geçir / şema testi / skill adayını değerlendir"; her yeni skill/evrim ÖNCESİ zorunlu (Katman-1 08-15). Kural: `core/skill-uretim-semasi.md`; graf: `core/skill-uretim-semasi.d2` (D2).
