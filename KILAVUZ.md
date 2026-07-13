# KILAVUZ.md — JARVIS Kullanım Kılavuzu (v1)

> **Açıklama notu:** K-012 build adım 2 çıktısı (2026-07-12; m.26: anlama-kapısı yerine kılavuz — Salih buradan okur, takıldığı yerde Carvis izah eder). Format deneysel-damgalı başlar (m.29), kullanım verisiyle kalibre edilir. Kural kaynağı her zaman tüzük; burası "nasıl kullanılır" yüzeyidir.

## Oturum nasıl işler
- **"günaydın"** → vardiya açılışı: kapsül + pano okunur, kısa teslim özeti + tek net sıradaki iş sunulur.
- İş sırasında ne söylersen görev olarak devralınır (m.25); küçük iş direkt yapılır, proje ölçekli işe kart/ajan — ölçek-tercihi Carvis'te.
- **Kapanış** ("end of day" / "bitiriyorum" / "uyucam"): vardiya teslim + kapsül güncellenir + push atılır. Carvis kapanışı kendi de önerebilir (V11 — fiilen yerleşik davranış).
- Push'lar Carvis'ten otomatik gider (`.secrets/github-pat`); her karar ayrı commit, [damıtma]/[icra] etiketli (V5).

## Paralel vardiya protokolü (Salih kararı 2026-07-12 sabah; m.36 revizyonunun operasyonel devamı — deneysel damga m.29)
- **Model (m.36 2. rev hizası):** JARVIS projesi İKİ paralel Cowork chat'inde yürür — şirketin iki yarısı: **(1) Prototip vardiyası** (K-015 şeridi — loop-eng, K-009, K-010, ajan-defter; ÖNCELİK BU) ve **(2) Ölçüm-bankı vardiyası** (K-002 PortRisk — hasat/etiketleme verisi üretir; çatışmada prototip kazanır). Açılışta hangi hattaysan söylersin: "günaydın, prototip" (ya da sadece "günaydın" — varsayılan bu hat) / "günaydın, PortRisk" — günaydın taraması kapsülden o şeridin durumunu alır. Belirsizse Carvis sorar (tek soru).
- **Prototip vardiyası kurulumu:** her zamanki gibi `C:\JARVIS` mount'u (Homebase eklenebilir).
- **Ölçüm-bankı (PortRisk) vardiyası kurulumu:** oturum `C:\JARVIS` mount'uyla açılır + yanına `C:\Users\sasah\dev\portrisk` klasörü eklenir. İç-mutfak dosyası (CLAUDE.md, vardiya kuralı, teslim raporu) public portrisk reposuna ASLA yazılmaz — bağlam hep JARVIS'ten okunur, portrisk'e yalnız proje kodu/testi gider.
- **Senkron kuralı (çakışma önleme):** her vardiya kapanışta (a) kendi teslim raporunu `raporlar/`a AYRI dosya yazar (`YYYY-MM-DD-<hat>-teslim.md`), (b) kapsülde YALNIZ kendi şeridinin satırını günceller — diğer şeridin satırına dokunulmaz, (c) kendi commit'lerini atar/push'lar. İki oturum aynı anda açıksa push öncesi pull zorunlu.
- Misyon notu: senkron şimdilik elle yürür — K-009 otomasyonu açılınca bu disiplinin otomatikleşmesi beklenir (geçici kabul, Salih 07-12).

## Üçlü sohbet düzeni — CC köprüsü (Salih kararı 07-12; m.17'nin ilk uygulaması; deneysel m.29)
- **Roller:** Salih = nihai karar verici · Carvis = köprü (görev emrini derler, CC çıktısını KENDİ değerlendirmesiyle sunar — kör aktarım yasak) · CC = uygulayıcı. Her iki vardiya hattında da geçerli.
- **Kanal:** dosya tabanlı — `cc/` klasörü (akış + şablon: `cc/README.md`). Carvis emri yazar → Salih CC'ye "dosyayı oku ve uygula" der → CC raporunu `cc/`ye yazar → Carvis yorumlar → Salih karar verir.
- **Sınır:** CC canlı ajan DEĞİL (K-010 delinmez, tetik Salih'te) · CC core/'a ve public portrisk'e iç-mutfak yazmaz · CC commit atmaz (m.9).

## Emir ve soru dili
- Ne dersen emirdir; önceki kararla çelişki varsa önce çelişki raporu gelir (m.16).
- **Çıktı-dili soru formatı + framing koruması (V6):** Carvis sana soru sorarken seçenekleri somut SONUÇ örnekleriyle sunar ("A seçilirse şu olur") ve soru cümlesi yönlendirme içermez — seçenekler yansız yazılır; Carvis kendi önerisini ayrıca, gerekçesiyle işaretler (m.6).
- **Kapasite cevabı üç halden biri (#9):** "yaparım" (direkt yapılır) · "yapamam" (neden + ne gerekirdi) · "proje gerekir" (kart açılır, kaba token×zaman tahmini verilir). Belirsiz "bakarız" cevabı yasak.

## Kart ve kutu kuralları
- **DONE kuralı (Salih onayı 07-12):** yazılabilir, doğrulanabilir DONE tanımı olmayan kart açılmaz. İyi örnek: "pytest yeşil + push". Kötü örnek: "İngilizceyi geliştir". Loop dönemi karşılığı: durma koşulu yazılamayan loop kurulmaz.
- **Çürüdü-işareti (Salih onayı 07-12):** fikir kutusunda 30 gün işlenmeyen madde "BAYAT" damgalanır; düşme YALNIZ Salih onayıyla (m.8 otomatik-silme yasağı korunur).
- **Gürültü listesi (deneysel damga; Salih düzeltir):** kutuya DOSYALANMAZ → model/sürüm duyuruları (işimizi değiştiren somut yetenek yoksa) · kaynaksız tek-tweet prompt numaraları · "X aracı çıkmış" haber gürültüsü (yazılı tetiğimize dokunmuyorsa) · başkasının kurulumunun bütünüyle kopyası (V25 altın kuralı: desen alınır, kurulum alınmaz). **İSTİSNA (Salih, 07-12):** "araştır bakayım" emri listeyi ezer — istek üzerine her şey araştırılır; liste yalnız kutuya-kayıt filtresidir.

## Tasarım ilkeleri
- **Sürtünmesizlik (#18):** sık kullanılan her akışın çağrısı kolay olur ve çapası kurulur; yeni mekanizma tasarlarken ilk soru "bunu çağırmak kaç saniye sürer?"
- **Bayat-kapsül riski (V4):** kapsül kapanışta güncellenmezse sonraki vardiya yanlış yere çapalar — yanlış kapsül, boş kapsülden kötüdür; kapanış disiplini bu yüzden atlanmaz.
- **Metafor haritası (V12):** sistem terimleri tek metafor ailesinden gelir (şirket: vardiya, pano, tüzük, teslim raporu); yeni terim aile içinde türetilir, tanımı sözlüğe işlenir (sözlük v1 DONDU — ekleme yalnız Salih talimatıyla, m.3).

## Skill-yazım standardı (deneysel damga m.29; kaynak: resmi skill-creator + best-practices — K-013 raporu; Salih onayı 07-12)
- SKILL.md <500 satır — tetiklenince gövde bağlama komple yüklenir, bu ~5K token tavanı demek (resmi tavsiye; kullanım verimizle kalibre edilir).
- Açıklama alanı = "ne yapar + ne zaman kullanılır" — tetikleme isabetini bu belirler.
- Her skill'e **Gotchas bölümü**: skill-başına biriken hata/tuzak listesi (ingest defterinin skill karşılığı).
- Yan-etkili işler (commit, push, publish) `disable-model-invocation` ile yalnız elle tetiklenir — model kendi kendine çalıştıramaz.
- Deterministik iş skill'e script olarak gömülür (model kodu her seferinde yeniden türetmesin).
- **Eval kuralı (Salih onayı 07-12):** bundan sonra yazılan her JARVIS skill'i eval setiyle doğar — ≥5 pozitif + 2-3 negatif senaryo, %90+ geçiş hedefi (araç: skill-creator, kurulu). Mevcut skill'lere geriye dönük eval soğuk kuyrukta.
- Not: progressive disclosure ilkesi = m.20 pointer sistemiyle aynı kök (bağımsız doğrulama, K-013).

## Durum görünürlüğü (m.18)
Her iş cevabının sonunda insan-yüzü tek satır (`▸ Şu an · Sıra · Açık`); "şu an ne yapıyoruz" dersen anlaşılır dilde detaylı durum raporu dosyası üretilir; makine-yüzü kapsül/pano/şablonlarda yaşar.
