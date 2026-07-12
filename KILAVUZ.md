# KILAVUZ.md — JARVIS Kullanım Kılavuzu (v1)

> **Açıklama notu:** K-012 build adım 2 çıktısı (2026-07-12; m.26: anlama-kapısı yerine kılavuz — Salih buradan okur, takıldığı yerde Carvis izah eder). Format deneysel-damgalı başlar (m.29), kullanım verisiyle kalibre edilir. Kural kaynağı her zaman tüzük; burası "nasıl kullanılır" yüzeyidir.

## Oturum nasıl işler
- **"günaydın"** → vardiya açılışı: kapsül + pano okunur, kısa teslim özeti + tek net sıradaki iş sunulur.
- İş sırasında ne söylersen görev olarak devralınır (m.25); küçük iş direkt yapılır, proje ölçekli işe kart/ajan — ölçek-tercihi Carvis'te.
- **Kapanış** ("end of day" / "bitiriyorum" / "uyucam"): vardiya teslim + kapsül güncellenir + push atılır. Carvis kapanışı kendi de önerebilir (V11 — fiilen yerleşik davranış).
- Push'lar Carvis'ten otomatik gider (`.secrets/github-pat`); her karar ayrı commit, [damıtma]/[icra] etiketli (V5).

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

## Durum görünürlüğü (m.18)
Her iş cevabının sonunda insan-yüzü tek satır (`▸ Şu an · Sıra · Açık`); "şu an ne yapıyoruz" dersen anlaşılır dilde detaylı durum raporu dosyası üretilir; makine-yüzü kapsül/pano/şablonlarda yaşar.
