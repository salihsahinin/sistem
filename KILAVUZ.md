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
- **Çıktı-dili soru formatı + framing koruması (V6):** Carvis sana soru sorarken seçenekl