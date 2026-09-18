# Görev emri — perspektif partisyonu: çok-ajanlı sistemde ajan sınırı hangi perspektife göre çizilir (Karar 102, 2026-09-18)

*Derleyen: Jarvis (Fable ana-sıra), S-K skill'i v1; iskelet `../../../sablonlar/gorev-fonksiyonu.md`. Koşum: `atlas-kosum` v0.2 diyalektiği (tez → antitez → maskeli hakem). Ham rapor `cc/rapor/2026-09/rapor-2026-09-18-perspektif-partisyonu-*.md`; insan-yüzü teslim `raporlar/2026-09/2026-09-18-perspektif-partisyonu.md`. Emir kazanır (Karar 88 M7 ⑤).*

```
## KİMLİK
gorev_adi:        perspektif-partisyonu-dis-tarama
rol:              lider (Opus 5 medium) → tez/antitez işçileri (Sonnet) → maskeli hakem (Opus 5 medium, ayrı çağrı)
cagri_kosulu:     Karar 102 hükmü: Friday'den ayrılacak perspektif(ler) literatür-önce belirlenir; iç ölçüm yalnız literatürün yetmediği noktada
rejim:            kalite-öncelikli (Katman-1 kararına girdi; pahalı geri-alma: ajan doğumu)
model:            işçi Sonnet 5 · lider/hakem Opus 5 medium (Karar 89); üst model Fable koşmaz, hakemlik sonrası masa hazırlar
kosum_profili:    aile 4 · tez 4 + antitez 4 + hakem 1 = 9 ajan · işçi başına effort düşük-orta, bağlam ≤40k, dönüş ≤2k token · tahmin: toplam çıkış 18-30k token [?], duvar-saati 15-30 dk [?] (KB-02; alt-modeller için; gerçekleşen koşum sonrası buraya)

## GİRDİLER
arastirma_sorusu: metin — "Çok-ajanlı kodlama/ajan sistemlerinde ajan sınırı hangi PERSPEKTİF ayrımına göre çiziliyor (icra · hakem/değerlendirici · antitez/red-team · araştırma · planlama · gözetim …)? Sektör öncülleri (Anthropic, OpenAI, Google DeepMind, Cognition, Kun Chen/firstmate sınıfı pratisyenler, büyük açık-kaynak çok-ajan çerçeveleri) ve 2025-2026 literatürü hangi ayrımları açıkça öneriyor, hangilerini reddediyor; her bulgu hangi model sürümü, hangi zaman dilimi, hangi kullanım biçimiyle üretilmiş?"
mevcut_duzen:     dosya — `../../../AGENTS.md` (kök kanon md.1: Jarvis ana-sıra, Friday tek domain-lider, işçiler tek görev) + `friday/AGENTS.md` §1 görev alanı (eager, ≤2 KB özet)
dogum_olcutu:     metin — Karar 91 EK-2: (a) kendi araç/kural seti ∨ (b) ≥3 devir/ay ∨ (c) bağımsız bağlam zorunluluğu ∨ (d) [Karar 102] sektör/literatür öncülünün AS-OF damgalı perspektif ayrımı

## BAĞLAM-MANİFESTİ
eager:            arastirma_sorusu · mevcut_duzen özeti · dogum_olcutu · kanonda-bilinenler bloğu (aşağıda)
lazy:             `cc/rapor/2026-09/rapor-2026-09-09-ib75-hakem.md` (ekip-lideri tasarımı hakem raporu; yalnız "hafıza/perspektif" bölümü, çelişki çıkarsa) · `cc/rapor/2026-08/rapor-2026-08-03-4.md` §I.5 Ç1-Ç12 (Kun Chen karşılaştırması; yalnız firstmate/secondmate sınıfı tanımı gerekince)
butce:            işçi ≤40k bağlam · dönüş ≤2k · toplam ≤120k [?]

## SINIRLAR
kapsamda:         (0) **ajan sınıfı ayrımı (Salih 16:5x eki):** alt-ajan (çağıran bağlamın içinde, geçici, hafızasız `Agent` çağrısı) ile kalıcı ajan (kendi dizini, kanonu, hafızası, oturumu) arasındaki yapısal fark literatür/pratikte nasıl çizilmiş; hangi iş hangisine gider; **öğrenme/öğretim oturumu** (bugün Jarvis worktree'sinde `ogren` skill'i) kalıcı ayrı ajan olmalı mı, kanıt · model dağılımı: Jarvis yalnız Fable, diğer kalıcı ajanlar Opus/Sonnet (Salih tahmini Opus) — öncüller lider/işçi model katmanlamasını nasıl kuruyor · (1) perspektif ayrımı taksonomisi: hangi öncül hangi rolleri AYRI ajan/bağlam olarak kurmuş (kanıt: belge, kod, sistem kartı, blog, konuşma; URL) · (2) her ayrımın gerekçesi (bağlam kirlenmesi · yapan≠ölçen · yetki · maliyet · paralellik) · (3) reddedilen/geri alınan ayrımlar (kim, neden) · (4) her bulguda AS-OF tablosu: kaynak tarihi · model sürümü/kuşağı · kullanım biçimi (üretim/deney/demo) · ölçek · (5) Friday'in görev alanına (araştırma · refactor/taşıma · doküman · ölçüm · hakem kurma) uygulanmış "ayrılmalı / kalmalı / belirsiz" hükmü, her hüküm ≥2 bağımsız kaynakla ya da "belirsiz → iç ölçüm" etiketiyle
kapsam_disi:      ajan charter'ı yazmak (Jarvis, masa sonrası) · Friday'i fiilen bölmek · hook/deny tasarımı · model seçimi (Karar 89 sabit) · staj/galeri örnekleri (md.49) · Jarvis iç kütüğünden sayım (Karar 102: iç ölçüm ikinci aşama, bu emrin dışında)
araclar:          WebSearch · WebFetch (birincil-kaynak açma kotası işçi başına ≥2, Karar 86 D3-iii) · Read (yalnız eager/lazy listesi) · rapor yazımı Write (yalnız kendi rapor yolu)
degismezler:      URL zorunlu · rakam kaynaklı, kestirim `[?]` · uydurma yasak, "bulunamadı" meşru · 403/paywall bayraklanır · **AS-OF damgasız iddia yok** (kaynak tarihi ∨ çekim tarihi) · **model-sürümü damgasız bulgu hakemde DÜŞER** (Karar 102 (3): eski kuşakla üretilmiş bulgu "o zaman böyle" notudur, doğrudan tasarım girdisi değil; kuşak eşiği: Karar 68 zaman-zemini, Sonnet/Opus/Fable 4.x öncesi = eski kuşak) · kanonda-bilinenler verili, yeniden araştırılmaz

## DALLAR (dal+koşul ≤5)
D1: eğer bir perspektif için ≥2 bağımsız güncel-kuşak kaynak "ayrı ajan/bağlam" diyorsa → hüküm AYRILMALI + gerekçe sınıfı + AS-OF satırı
D2: eğer kaynaklar çelişiyorsa ∨ yalnız eski-kuşak kaynak varsa → hüküm BELİRSİZ → "iç ölçüm" etiketi + ölçülecek büyüklük önerisi (Karar 102 (2))
D3: eğer bir öncül perspektifi ayırmayı açıkça reddediyorsa → RET kaydı: kim, gerekçe, tarih, model
D-KATMAN1: taksonomi kanonun rol katmanlarıyla (tüzük m.44: köle ≠ üst-orkestratör ≠ domain-lider) çelişirse → hakem raporunda "m.16 çelişki" bölümü; karar Salih'te, ajan çözmez

## ÇIKTI SÖZLEŞMESİ
halusinasyon_derecesi: H = 8 (eşik 7; v2 tazelik +3 · v3a atıf/URL +3 OVERRIDE · v5 bileşiklik +2 · v7a kapalı-kitap +2 · v8 doğrulayıcı −2) → halusinasyon-engelleyici TETİKLENİR (her iddia DESTEKLİ/DAYANAKSIZ/ÇELİŞİR etiketli; kaynak-topraklama + maskeli hakem bağımsız doğrulayıcı)
cikti_bicimi:     aile başına tez raporu + antitez raporu (≤2k token dönüş, tam metin dosyada) · hakem raporu: (i) perspektif × hüküm (AYRILMALI/KALMALI/BELİRSİZ) × gerekçe sınıfı × kaynak sayısı × AS-OF (tarih · model · kullanım) tablosu · (ii) RET listesi · (iii) iç-ölçüme kalan büyüklükler · (iv) m.16 çelişki bölümü · (v) masa kalemi taslağı (Friday'den ayrılacak ilk perspektif önerisi, seçenekli)
done_yuklemi:     hakem tablosunda Friday görev alanının 5 işi + hakem + antitez + planlama + gözetim + **öğrenme/öğretim** için hüküm satırı VAR ∧ alt-ajan/kalıcı-ajan ayrım tablosu (≥4 boyut: hafıza · kimlik · yetki · oturum) VAR ∧ model katmanlaması bulgusu AS-OF'lu ∧ her AYRILMALI satırı ≥2 URL + AS-OF + model sürümü taşıyor ∧ damgasız iddia sayısı = 0 ∧ RET listesi boş değilse her satır kaynaklı ∧ işçi başına açılan birincil kaynak ≥2
done_olcumu:      DRFR — yukarıdaki 5 koşul tek tek
yeniden_deneme:   3

## SKILL TETİKLERİ
- skill:              atlas-kosum
  tetik_kosulu:       emir teslim edildi ∧ K2 manifest kapısı "koşmuş-aday" DEĞİL; K2 koşmuş-aday ise ÇAĞIRMA (devral)
  cagri_kipi:         literal (ana-sıra Jarvis başlatır; işçiler skill'i çağırmaz)
  girdi:              arastirma_sorusu · aile ayrıştırması: A) sektör öncülleri (Anthropic/OpenAI/DeepMind sistem belgeleri, mühendislik blogları, ajan SDK'ları) · B) pratisyen sistemler (firstmate/Kun Chen, açık-kaynak çok-ajan orkestratörleri, "harness" yazarları) · C) akademik/benchmark literatürü 2025-2026 (multi-agent, LLM-as-judge ayrımı, adversarial/red-team ajan, planner-executor) · D) ajan sınıfları ve model katmanlaması (alt-ajan ≠ kalıcı ajan: hafıza/kimlik/yetki/oturum; öğretim/tutor ajanı vakası; lider-işçi model dağılımı pratikleri)
  baglam:             hedef = hakem tablosu; format = md tablo + URL; sınır = kapsam_disi; iddia ≠ gerekçe; işçi bağlamı geçmişsiz
  yan_etki_damgasi:   salt-okur × idempotent:h (web zamanla değişir) × dış-dünya:h (yalnız okuma)
  done_yuklemi:       yukarıdaki done_yuklemi
  hata_yolu:          işçi dönüşü şema dışı → lider düzeltir · web erişim engeli → bayrak + diğer kaynağa geç · retry ≤3 · FAIL-LOUD
  sira:               1/2 (2/2 = halusinasyon-engelleyici, hakem aşamasında)
  kayit:              execute_tool · tool.name=atlas-kosum · agent · error.type · model+sürüm · tarih → skill sayacı
- skill:              halusinasyon-engelleyici
  tetik_kosulu:       H = 8 ≥ 7 ∧ çıktı atıf/URL türü; tez/antitez aşamasında ÇAĞIRMA (yalnız hakem aşaması)
  cagri_kipi:         ortuk (hakem aşamasının usulü; ayrı çağrı gerektirmez)
  girdi:              tez+antitez raporları · kaynak listesi
  baglam:             her iddia DESTEKLİ/DAYANAKSIZ/ÇELİŞİR; damgasız → DAYANAKSIZ
  yan_etki_damgasi:   salt-okur × idempotent:e × dış-dünya:h
  done_yuklemi:       hakem raporunda etiketsiz iddia = 0
  hata_yolu:          etiketlenemeyen iddia → BELİRSİZ satırına düşer · sözleşme-ihlali → hakem düzeltir · retry ≤3 · FAIL-LOUD
  sira:               2/2
  kayit:              aynı

## KANONDA-BİLİNENLER (verili kabul et, üstüne koy)
- Jarvis = Salih'le konuşan ana-sıra ajan; tarihli metinlerdeki "Carvis" = Jarvis (eski ad Carvis); sistem/repo = depo/kanon (Karar 93 EK).
- Rol katmanları tüzük m.44: köle (Jarvis, Salih muhataplığı) ≠ üst-orkestratör (Jarvis'in koşum şapkası, domain-lider seviyesine kadar böler) ≠ domain-lider (Friday). Karar 89: Fable → Opus 5 lider medium → Sonnet işçi.
- Yapan ≠ ölçen kanonda (Karar 86 D3; hakem her zaman ayrı çağrı + maskeli). Karar 93 M7-1: alan ajanı = Jarvis alt-ajanı, ayrı repo yok; Friday yalnız bağımsız bağlam gerektiğinde. Karar 99 M6: hakem ajanı şablonu core'a girmeden önce canlı test (İB-108).
- Karar 101 (09-18): monorepo `~/sistem`, N ajan + ortak kanon; Friday = domain-lider, izolasyon cwd+hook+deny (F5 kanıtı: Friday bağlamında Jarvis satırı 0). Karar 102: literatür-önce, model-sürümü damgası zorunlu.
- Kun Chen/firstmate (rapor 2026-08-03-4 §I.5; firstmate AGENTS.md 09-18 taraması): firstmate = tek temas noktası, projeye yazmaz; secondmate = izole ev + charter, alan-kapsamlı; crewmate = tek görev; hard rule 4 "crewmate kaptana yazmaz". Bunlar verili; yeniden taranmaz, yalnız "perspektif ayrımı" gerekçesi aranır.
- Geçmiş yörüngeler (deneyim-tablo, 09-18): 5 benzer koşum, hepsi güncel kuşak, hüküm kaydı yok (wf_a08eccb1 08-15 aile B ajan mimarisi tez/antitez/hakem · wf_7277331e 08-21 aile C kompozisyon). Ölçülmüş profil yok → tahmin bantları `[?]`.
- m.40b antitez şeridi 08-14 raporunda koşulmadı (tek-şerit borcu); bu koşumda antitez zorunlu.
- Salih 09-18 16:5x eki (aynen): "öğrenme oturumlarımı da farklı kanon hazırlanmış farklı ajanla yapmak mantıklı mı bu bağlamda gözden geçirilmeli. jarvisin alt ajanı ile jarvis gibi ajanların yapısal olarak farkı doğru analiz edilmeli. planlanan hedefte bir tek jarvis fable model, diğer ajanlar opus veya sonnet model olabilir (tahminim opus daha iyi olacaktır). ve bu sistemde jarvis gibi ajanların kendi gelişen hafıza mimarilerinin olmasını nasıl tasarlayacağız bunu da araştırmalıyız" → ilk üçü aile D (bu emir); **gelişen hafıza mimarisi = zincirin 2. emri** (`gorev-2026-09-18-ajan-hafiza-mimarisi.md`, bu koşum bitince derlenir; girdi = bu raporun ajan-sınıfı tablosu).

## DİNAMİK EK
tarih: 2026-09-18 ~16:5x · HEAD 569d41a · tetikleyen: Salih beyanı (Karar 102, aynen defterde) · zaman-zemini Karar 68: bugün 2026-09-18; model kesimleri Fable 5.1 2026-01 · Opus 5 2026-05 · Sonnet 5 2026-01 · Haiku 4.5 2025-02 → "güncel kuşak" = 2025-Q3 sonrası yayımlanmış ∧ 4.x+ modelle üretilmiş
```
