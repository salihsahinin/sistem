# KILAVUZ.md — JARVIS Kullanım Kılavuzu (v1)

> **Açıklama notu:** K-012 build adım 2 çıktısı (2026-07-12; m.26: anlama-kapısı yerine kılavuz — Salih buradan okur, takıldığı yerde Carvis izah eder). Format deneysel-damgalı başlar (m.29), kullanım verisiyle kalibre edilir. Kural kaynağı her zaman tüzük; burası "nasıl kullanılır" yüzeyidir.

## Oturum nasıl işler
- **"günaydın"** → vardiya açılışı: kapsül + pano okunur, kısa teslim özeti + tek net sıradaki iş sunulur.
- İş sırasında ne söylersen görev olarak devralınır (m.25); küçük iş direkt yapılır, proje ölçekli işe kart/ajan — ölçek-tercihi Carvis'te.
- **Kapanış** ("end of day" / "bitiriyorum" / "uyucam"): vardiya teslim + kapsül güncellenir + push atılır. Carvis kapanışı kendi de önerebilir (V11 — fiilen yerleşik davranış).
- **Bağlam-şişme çağrısı (Salih emri 07-19):** Carvis, oturum bağlamının şiştiğini ve kalite riskini gördüğünde bunu KENDİLİĞİNDEN belirtir; vardiya kapanışı + yeni seans önerir (kapanış = teslim raporu + kapsül tazeleme; yeni seans kapsülden devralır — m.27 hattı).
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

## Model-değişimli oturum protokolü (Salih imzası, 2026-07-13 — kural, deneysel değil)
Oturum ortasında model değişikliği yaşanırsa o oturumun orijinalliği bozulmuş sayılır: ingest'i kanon-yüzeyine değil şerhli klasöre yazılır — `model değişikliği ile orijinalliği bozulmuş olan chat/ingest-YYYY-MM-DD.md`. Buradaki içerik ŞERHLİ KOPYA statüsündedir; çelişki durumunda commit'li kanon (fikir kutusu / kuyruk / kapsül) kazanır. Şerhli içeriğin karar statüsü kazanması için ayık/temiz oturumda taranıp normal kanon yoluna işlenmesi gerekir. Gerekçe: bağlam hijyeni (07-13 vakasının standartlaşması).

## CC kanal modeli kararı (Salih, 2026-07-13 günaydın)
ŞİMDİ = **Model 1** (dosya-kanalı: `cc/` görev emri + rapor; Carvis köprü, tetik Salih'te). HEDEF = **Model 3** (headless: CC'nin programatik çağrılması). Geçiş koşulu (m.38 lojik formu): (Salih Orca-ADE'yi öğrendi ∧ loop-eng öğrenimi tamamlandı ∧ K-009 otomasyon açık ∧ Model-3 diğer eksikleri kapatıldı) → Model 3'e geçilir; koşullardan HERHANGİ biri sağlanmadıkça (¬hepsi) Model 1 sürer. Model 2 (elle-yapıştır) reddedildi — V27 düşük-sürtünme hedefiyle ters.

## Mobil Köprü Protokolü (Dilim 2.1; Salih kararı 07-19 — rapor-1 Adım 0'ın icrası; deneysel m.29)
*Amaç: PC başında değilken (yol, yatak, oyun arası) sistemle çalışmanın standart yolu. Omurga: git-as-truth — üç zıt-temelli modelin ortak yakınsaması (rapor 1 triangülasyon #1): mobil katman git'in ÜSTÜNE oturur, yerine geçmez. 07-18 koşusu (17 rapor, branch'e) bu protokolün ilk tam canlı örneğidir.*

**Kanal seçim tablosu — "mobildeyim, ne yapmak istiyorum?"**
- **Fikir düştü** → chat/mobil Claude (snapshot yüzey): fikir-kutusu-adayı formatında yaz; "HAM FİKİR / PC'de ingest edilecek" damgası. Dönüşte ana-sıra ingest eder.
- **SES-POC (Dilim 2.2, deneysel m.29):** aynı kanal, yazmak yerine telefon klavyesinin dikte tuşuyla KONUŞ; mesaj başına `SES-POC` öneki + niyet sınıfını SÖYLEME (triyajı sistem yapacak — ölçüm bu); transkripti DÜZELTME, ham bırak (WER referansı ingest anında Salih-düzeltmesiyle çıkar). Dönüş ritüelinde ana-sıra "ses-poc ölçümü" adımıyla WER+triyaj-başarısını deftere işler. **Toplama modu (Salih emri 07-19): PASİF — özel test oturumu YAPILMAZ; örnekler doğal kullanımda birikir (oyun arası, seyahat, çalışma); ölçüm vardiyasının tetiği örnek sayısı değil Salih beyanıdır.**
- **Araştırma koşturmak istiyorum** → mobil CC yan-oturum: çift-atlas kuralı (tez + antitez), rapor ÜRETİR; **commit `claude/`-önekli branch'e** (bulunabilirlik — Salih izni 07-18 emsali), kanon dosyalarına DOKUNMAZ. Cevaplanmamış soru rapora gömülür, mobilde karar biriktirilmez (07-17 kuralı).
- **Karar almak istiyorum** → yalnız ana-sıra (m.41: ana-sıra ∧ Fable ∨ Salih-imza). Mobil yüzeyde kanon imzası YOK; istisna = açık yazılı Salih beyanı, dönüşte ana-sıra kaydeder.
- **PC'de acil iş** → Remote Control (ilk kurulum K-018'de bekliyor; kurulana dek: kısa not bırak, ana-sıra devralır).

**Dönüş ritüeli (üç adım):** (1) ana-sıraya "raporları oku" — branch süzgeçten geçer, merge yalnız Fable süzgeciyle (m.41); (2) süzgeç verdicti + soru triyajı sunulur, kararlar ana-sırada alınır; (3) disk senkronu — gece scripti zaten eşitler, gündüz gerekirse dosya-düzeyi senkron Carvis'te.

**Güvenceler:** mobil üretim daima HAM/öneri statüsünde (m.41) · CC yüzeyinde core/ + CLAUDE.md + .claude/ yazımı yapısal kilitli (Dilim-1 paketi) · damga yalnız gönüllü beyanla (m.33) · sabah taze-başlangıç zinciri: gece-senkron scripti → SessionStart hook (canlı kapsül+pano+yetki bandı).

## Skill Standardı (K-016 açılışı 07-19; el kitabı: `raporlar/2026-07-17-skill-nasil-olusturulur.md` — burası özet, çelişkide rapor + code.claude.com/docs kazanır)
- **Eval-önce akış:** önce ≥3 senaryoluk `evals/evals.json` + baseline (skill'siz koşum), SONRA minimal gövde; description ince-ayarı EN SON. Eval'siz yayın YOK.
- **Description:** 3. şahıs · NE + NE ZAMAN (gerçek kullanıcı ifadeleriyle) + NEGATİF tetik ("X'te kullanma") · ≤1024 karakter.
- **Gövde:** <500 satır · emir-kipli numaralı adım · tek sorumluluk · "Gotchas" bölümü en yüksek sinyal · detay `references/` (bir seviye derin).
- **Yan-etki freni (★):** kayıt/commit/deploy adımı AYRI `disable-model-invocation: true` skill'e — muhakeme skill'i blok ÜRETİR, dosyaya YAZMAZ (m.31/m.9 koda gömülü).
- **Kompozisyon:** skill'ler birbirini literal çağırmaz; bileşik iş = `context: fork` orkestratör + küçük çocuk skill'ler + sabit-format handoff + fail-loud.
- **Yayın-öncesi:** 20-sorgu description eval (10 tetiklemeli + 10 tetiklemesiz) · çok-modelde test · versiyon damgası (`0.x-deneysel-m29`).
- **Ev:** `.claude/skills/<ad>/SKILL.md` (repo, git'e commit — dağıtım gece-senkron/pull ile).
