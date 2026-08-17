# Arşiv — KILAVUZ bölümleri (damıtma 2026-08-17, KB-37 Salih A)

*m.8: silme yok. Cowork/geçiş döneminin operasyon tarifleri (Cowork emekli 08-12; CC-geçiş tamamlandı; mobil köprü = Cowork mobil) birebir buraya indi; KILAVUZ'da her biri tek satır pointer olarak yaşar. Kural niteliğindeki cümleler zaten tüzük/CLAUDE.md'de. Soğuk katman.*

## Üçlü sohbet düzeni — CC köprüsü (Salih kararı 07-12; m.17'nin ilk uygulaması; deneysel m.29)
- **Roller:** Salih = nihai karar verici · Carvis = köprü (görev emrini derler, CC çıktısını KENDİ değerlendirmesiyle sunar — kör aktarım yasak) · CC = uygulayıcı. Her iki seans hattında da geçerli.
- **Kanal:** dosya tabanlı — `cc/` klasörü (akış + şablon: `cc/README.md`). Carvis emri yazar → Salih CC'ye "dosyayı oku ve uygula" der → CC raporunu `cc/`ye yazar → Carvis yorumlar → Salih karar verir.
- **Sınır:** CC canlı ajan DEĞİL (K-010 delinmez, tetik Salih'te) · CC core/'a ve public portrisk'e iç-mutfak yazmaz · CC commit atmaz (m.9).


## CC kanal modeli kararı (Salih, 2026-07-13 günaydın)
ŞİMDİ = **Model 1** (dosya-kanalı: `cc/` görev emri + rapor; Carvis köprü, tetik Salih'te). HEDEF = **Model 3** (headless: CC'nin programatik çağrılması). Geçiş koşulu (m.38 lojik formu): (Salih Orca-ADE'yi öğrendi ∧ loop-eng öğrenimi tamamlandı ∧ K-009 otomasyon açık ∧ Model-3 diğer eksikleri kapatıldı) → Model 3'e geçilir; koşullardan HERHANGİ biri sağlanmadıkça (¬hepsi) Model 1 sürer. Model 2 (elle-yapıştır) reddedildi — V27 düşük-sürtünme hedefiyle ters.


## CC-geçiş düzeni — S2 hibrit-matris (Salih imzası 08-01 masa-2, K1-24-a; md.9 glide-path revizesi; bağlayıcı kayıt senaryo-defteri)
Hedef "tam geçiş" DEĞİL, matris-optimumu: 10 iş-sınıfından CC'nin alternatifsiz olduğu 4'ü (ölçüm + otomasyon dahil) CC'de koşar · kanon yazımı (G1) md.8 imzalı ana-sıra-CC profili kurulana dek Cowork'te kalır · iki yüzeyde de yapılabilen 3 çatal (G2 ritüel · G7 Salih-okuma · G10 mobil) E5 ergonomi ölçümü yapılmadan TAŞINMAZ — E5 = çatalların karar kapısı, ölçümsüz çatal taşınmaz. Aşama yapısı korunur: aşama 1-2 izinli · aşama 3 ayrı imza · aşama 4 öncesi CC'de tek deneme seansı + 2 ölçüm (oturum-değiştirme sayısı, bağlam doluluğu). "Hangi yüzeyde yapalım?" sorusunun cevabı tercihe değil TABLOYA bakar. Gerekçe-disiplini (K1-24-b): kanon gerekçesi = "iç matris 3 çatal gösterdi", dış görüş atfı YOK. İlk ölçüm adayı: G2 ritüel (iki skill repoda, A/B hazır).


## Mobil Köprü Protokolü (Dilim 2.1; Salih kararı 07-19 — rapor-1 Adım 0'ın icrası; deneysel m.29)
*Amaç: PC başında değilken (yol, yatak, oyun arası) sistemle çalışmanın standart yolu. Omurga: git-as-truth — üç zıt-temelli modelin ortak yakınsaması (rapor 1 triangülasyon #1): mobil katman git'in ÜSTÜNE oturur, yerine geçmez. 07-18 koşusu (17 rapor, branch'e) bu protokolün ilk tam canlı örneğidir.*

**Kanal seçim tablosu — "mobildeyim, ne yapmak istiyorum?"**
- **Fikir düştü** → chat/mobil Claude (snapshot yüzey): fikir-kutusu-adayı formatında yaz; "HAM FİKİR / PC'de ingest edilecek" damgası. Dönüşte ana-sıra ingest eder.
- **SES-POC (Dilim 2.2, deneysel m.29):** aynı kanal, yazmak yerine telefon klavyesinin dikte tuşuyla KONUŞ; mesaj başına `SES-POC` öneki + niyet sınıfını SÖYLEME (triyajı sistem yapacak — ölçüm bu); transkripti DÜZELTME, ham bırak (WER referansı ingest anında Salih-düzeltmesiyle çıkar). Dönüş ritüelinde ana-sıra "ses-poc ölçümü" adımıyla WER+triyaj-başarısını deftere işler. **Toplama modu (Salih emri 07-19): PASİF — özel test oturumu YAPILMAZ; örnekler doğal kullanımda birikir (oyun arası, seyahat, çalışma); ölçüm vardiyasının tetiği örnek sayısı değil Salih beyanıdır.**
- **Araştırma koşturmak istiyorum** → mobil CC yan-oturum: çift-atlas kuralı (tez + antitez), rapor ÜRETİR; **commit `claude/`-önekli branch'e** (bulunabilirlik — Salih izni 07-18 emsali), kanon dosyalarına DOKUNMAZ. Cevaplanmamış soru rapora gömülür, mobilde karar biriktirilmez (07-17 kuralı).
- **Karar almak istiyorum** → yalnız ana-sıra (m.41: ana-sıra ∧ Fable ∨ Salih-imza). Mobil yüzeyde kanon imzası YOK; istisna = açık yazılı Salih beyanı, dönüşte ana-sıra kaydeder.
- **PC'de acil iş** → Remote Control (ilk kurulum K-018'de bekliyor; kurulana dek: kısa not bırak, ana-sıra devralır).

**Dönüş ritüeli (üç adım):** (1) ana-sıraya "raporları oku" — branch süzgeçten geçer, merge yalnız Fable süzgeciyle (m.41); (2) süzgeç verdicti + soru triyajı sunulur, kararlar ana-sırada alınır; (3) disk senkronu — gece scripti zaten eşitler, gündüz gerekirse dosya-düzeyi senkron Carvis'te.

**Mobil CC açılış komutu (kopyala-yapıştır; 07-19 eki):** telefonda Claude → Code → `salihsahinin/jarvis` → yeni oturum → ilk mesaj:
> "Mobil yan-oturum (m.41). Önce `core/durum-kapsulu.md` + `core/pano.md` oku (hook bandı geldiyse özetle yetin). Kurallar: çift-atlas (tez + antitez=¬), rapor `claude/`-önekli branch'e, kanon dosyalarına DOKUNMA, karar biriktirme — cevaplanmamış soru rapora gömülür. Görev: <işi buraya yaz>."
Dönüşte ana-sıraya "raporları oku" demen yeter (dönüş ritüeli).
**Yüzey beyanı kısayolu (07-19 eki, m.41 uygulaması):** açılış komutu ZORUNLU DEĞİL — okuma sırası otomatiktir (CLAUDE.md + SessionStart hook). Komutun tek işi yüzey beyanı: mobil CC'de **Fable açık + "Fable, ana sıra" beyanı → oturum ANA-SIRA sayılır** (karar alır, m.16/m.37 işletir); beyan yoksa varsayılan = yan-oturum kuralları. Yapısal kilit her durumda geçerli: CC'de `core/` yazımı modelden bağımsız kilitli — ana-sıra-mobil karar ALIR, kanon YAZIMI dönüşte işlenir (kilidi Fable'a gevşetmek ayrı tüzük kararı, açık soru). Effort önerisi: günlük icra/ana-sıra medium · karar-yoğun (imza/süzgeç) high · atlas işçileri default. Hook bulut ortamında İLK KEZ bu gece gözlemlenecek — band gelmezse not düş, protokol yine geçerli (CLAUDE.md otomatik okunur).

**Güvenceler:** mobil üretim daima HAM/öneri statüsünde (m.41) · CC yüzeyinde core/ + CLAUDE.md + .claude/ yazımı yapısal kilitli (Dilim-1 paketi) · damga yalnız gönüllü beyanla (m.33) · sabah taze-başlangıç zinciri: gece-senkron scripti → SessionStart hook (canlı kapsül+pano+yetki bandı).


