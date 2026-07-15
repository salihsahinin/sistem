# Build Tartışma Notları — K-013 + Rakip Analizi Bulguları

> **KUYRUK KAPANDI (Salih, 2026-07-12 tartışma oturumu — 3 blok tamam).** Blok 1: m.34 (katmanlı ingest, taze-oturum revizyonuyla) + kural-değişim ritmi RED. Blok 2: m.35 (tez #0 çapa) + m.36 (ilk-prototip fazı, K-015). Blok 3: skill-yazım standardı KILAVUZ'a girdi (deneysel) · eval kuralı kabul (yeni skill eval'le doğar; geriye dönük eval soğuk kuyruk; hizalama kökeni: kayıt geçerli — 07-07 Salih tanımı, Yağız'ınki dev-run-planner) · superpowers şimdi alınmaz — Salih vizyon kaydı: "prototip bitince ilk ajan kurulur, onunla proje geliştirilir, şirket büyürken paket göz önünde bulundurulur" → K-009/K-010 açılış gündemine işlendi. Carvis şerhi: K-010'un "temel katman 2 hafta sorunsuz" ön-koşulu yürürlükte; "prototip bitince hemen ilk ajan" o güne sıkışırsa çelişki kapısı koşulur. **K-014 TETİKLENDİ.** Dosya arşive hazır (düşme Salih onayıyla, m.8).
*ÖNERİ DOSYASI (imzasız) — 2026-07-12. Hiçbir satır karar değildir; Salih emri: "bulguları not al, sormadan ekleme-çıkarma yapma." Her madde ilgili build adımında birlikte tartışılıp tek tek karara bağlanır. Kaynaklar: raporlar/2026-07-12-K013-ekosistem-arastirmasi.md + personal-os rakip analizi (bu dosyanın eki).*

## 0. Salih'in farklılaşma tezi (07-12, kendi sözleriyle — kanon adayı, tartışmada işlenecek)
"Bizi marjinal ve iyi kılan şey: token-zaman parametrelerine göre matematiksel modelleri KOMBİNASYONLAMAMIZ (mikro işlem kararlarında). Model, çıktıların iterasyonundan öğrenerek ilerleyecek; farklı kombinasyonlar için beklenen-başarı oranı, beklenen-süre, beklenen-token tüketimine göre projeden projeye veya kalan zamana göre hareket edebileceğiz."
→ Kanondaki kökleri zaten var: m.17 (araç seti), m.29 (fitting yolu), m.31 (3-kart), V15, V28, token×zaman dipnotu. Yeni katkı: **kombinasyon-başına üçlü beklenti vektörü (başarı/süre/token) + kalan-zamana göre politika seçimi** — bu formülasyon henüz hiçbir maddede yazılı değil. Araştırma bunu destekliyor: sahada resmi formül YOK (boşluk tespiti), herkes kaba tur-limitiyle idare ediyor → gerçek farklılaşma alanı.


**Ek (Salih, 07-12 devam):** "İlk projelerde daha fazla veri toplarsak daha sağlam temel kurarız → ilk projeler token ve zamandan FEDAKARLIK yapacak şekilde (ölçüm öncelikli) tasarlanır; görece küçük başlayıp proje büyüklüğü kademeli artırılır." → V28'in ~10-görev etiketleme ön-koşuluyla birleşiyor: deney tasarımı stratejisi. Carvis şerhi (çelişki taraması): "küçük projeler" YENİ artefakt açmak olarak okunursa m.13 tek-flagship ile çelişir; görev-düzeyinde okunursa (PortRisk sprintleri zaten küçük görevlere bölünüyor, her görev etiketlenir) çelişki yok — tartışmada netleştirilecek.

## Adım 1 (CLAUDE.md) tartışma maddeleri
- Pointer sistemimiz (m.20) = resmi "progressive disclosure" ilkesiyle birebir; bağımsız doğrulama. Not düşülsün mü, düşülmesin mi? (Bilgi değeri var, işlev değeri tartışılır.)

## Adım 2 (KILAVUZ.md) tartışma maddeleri
- **"Done yazılamayan iş devredilmez / kartta DONE yoksa kart açılmaz"** — sahada evrensel ilke (loop güvenliğinin 3 ayağı: done + tur limiti + bütçe tavanı). Fiilen uyguluyoruz; resmileşsin mi?
- **Disposable Noise listesi** (personal-os): "neyi DOSYALAMAYIZ" negatif listesi — fikir kutusu gürültü barajı, 1 paragraf maliyet.
- **Quality Gate + 30-gün expiry** (personal-os): kalıcı katmana giriş için 4-soru barajı; geçemeyen kuyrukta 30 gün sonra otomatik çürür. DİKKAT: otomatik-çürüme m.8 (otomatik silme yasağı) ile gerilimli — ancak "çürüdü İŞARETİ + Salih onayıyla düşme" olarak uyarlanabilir.

## Adım 3 (wiki mekanizmaları) tartışma maddeleri
- **LLM-wiki v2 gist okuması adım 3'ün ÖN-İŞİ** (confidence scoring + bayat-iddia süpersede + çelişki tespiti — çelişki kapısının wiki-düzeyi hali). Tek onaylanmış ekleme adayı; Salih 07-12 "doğru sıraya koy" varsayımıyla uyumlu.
- **Zone C sayfa şablonu** (personal-os): wiki sayfası = özet değil SOP — "Core Question → adım adım prosedür → Failure Modes → Critical Review"; "özet yazıyorsan dur" refleksi.
- **Gotchas bölümü** (resmi skill pratiği): sayfa/skill-başına biriken hata-tuzak listesi = ingest defterinin sayfa karşılığı.

## Adım 4 (pano/kapsül şablonları) tartışma maddeleri
- **Beads deseni**: kartlara makine-okur alan (ID, bağımlılık, durum) → ajan dönemi hazırlığı, ucuz ek. (m.18a makine-yüzü ile aynı hat.)

## Tüzük adayları (Katman 1 — yalnız tartışmada) — **KARARA BAĞLANDI (Salih, 07-12 tartışma oturumu)**
- **Taze-oturum promote ilkesi** → Salih revizyonuyla KABUL = **m.34 katmanlı ingest** (taze-oturum şartı düştü: Carvis aynı oturumda hazırlayabiliyorsa beklenmez; mekanizma = pointer'lı katmana oku-üstüne-ekle + şişen katman derine özütlenir).
- **weekly-taste-sync / kural-değişim ritmi** → **REDDEDİLDİ** (Salih: "sıkıntı gördüğümde dile getirir, tüzükten düzenleriz — başka modele gerek yok"; m.5 sorun-güdümlü düzen kalır).
- **Tez #0** → KANONLAŞTI = **m.35** (çapa tüzükte, tam formülasyon wiki kuyruğunda); "küçük projeler" okuması = tasarım-görevi düzeyi, m.13 çelişkisi YOK (m.36).
- **PortRisk ertelemesi** → **m.36 ilk-prototip fazı kuralı** + K-015 kartı (yaşayan liste).

## Ajan dönemi defteri (K-009/K-010 açılınca gündeme gelir; şimdi dokunulmaz)
- **Salih notu (07-12):** "Looplara gelince söyleyeceğim — Karpathy'nin loop yöntemi gibi yöntemleri de öğrenip kullanmamız lazım." K-009 açılış gündemine.
- **Salih vizyonu (07-12 tartışma, blok 3):** ajanlar proje proje başlar — prototip bitince ilk ajan kurulur, onunla proje geliştirilir; şirket büyütülürken superpowers desenleri (TDD · sistematik debugging · subagent-driven development) göz önünde bulundurulur.
- Loop guardrails: 3 tur · 10 dk · sıfır-ilerleme-durdur (personal-os) + tur limiti/bütçe tavanı (saha standardı).
- Heartbeat maliyet deseni: script veri toplar → LLM yalnız akıl yürütür (~7x ucuz).
- Rol-başına model katmanlama + "ucuz model ≠ ucuz iş" ölçülmüş dersi (Haiku analitik işte daha çok tur → toplam token daha kötü) — #24b formülünün girdisi.
- Karar kuralı: paralellik kazancı > koordinasyon vergisi ise takım, değilse tek güçlü ajan.
- Beads/gastown: ajan-yazılabilir pano + worktree izolasyonu + rol-adlı kalıcı kimlikler (m.30 ile uyumlu).
- **Salih formülasyonu (07-15, Faz 3 dersinden tümevarım — ajan-yetki modeli, kanon adayı):** Loop/ajan tanımı "ne yapacağını" değil "SADECE ne yapabileceğini" söyler (pozitif yetki listesi); esnek görevlerde yapabilecekler + açık kırmızı çizgiler birlikte tanımlanır. Şirket otoriterdir; otoriterlik kademelidir (Carvis → ekip liderleri → işçiler): her katman bir alttakine "hatalarını TOPARLAYABİLECEĞİ seviyede" özgürlük verir. Sıkı sınır iş potansiyelini kısar, gevşek sınır hata olasılığını artırma fedakârlığıyla daha çok iş yaptırır — oran deneysel başlar, optimize edilir; Salih sezgisi: ekip liderlerine de KATI sınırla başlanır. Gevşetme gerekçesi: proje ölçeği + token-zaman kısıtının öne çıkması → risk kademeli artırılır. Tümevarım dersi: token-zamana göre optimizasyon her kombinasyon için bir RİSK HESABI üretir; o risk bilinçli kabullenilir.
- **Carvis şerhi (07-15, m.6 — karar Salih'te):** (a) Bu, m.31'in (Katman 2 = yapar+kaydeder, veto=revert) ajan hiyerarşisine GENELLEMESİ — "toparlanabilir hata sınırında özgürlük" zaten Carvis yetkisinin tanımı; iç tutarlı. (b) Düzeltme önerisi: gevşetmenin birincil gerekçesi ölçek olmamalı — ölçek büyüdükçe hata MALİYETİ de büyür; doğru koşul bileşik: sicil(a) ∧ geri-alınabilir(hata-sınıfı) ∧ token-zaman-baskısı → Gevşet(a); tek başına ölçek gevşetme gerekçesi değil. Lojik çekirdek (m.38): Özgürlük(a) ≤ Toparlanabilirlik(hata(a)). (c) m.37 genişleme adayı: model karşılaştırmasına 4. boyut RİSK = hata-olasılığı × hata-maliyeti × geri-alma-maliyeti; P19 Brier kalibrasyonu bu tahminlerin denetim aracı. (d) Katı-başlangıç sezgisine katılıyorum: sıkı→gevşek yönü ucuz ve kanıt-temelli, gevşek→sıkı yönü olay-sonrası olur (Faz 3 "mimari > talimat" dersiyle aynı hat). K-009 açılış gündemi + tüzük adayı.

- **Salih (07-12, adım 3 tartışması):** (a) Örnek-damıtma sorusu → kural: sayfa başına 1 kanonik damıtılmış örnek, ham senaryo raporda pointer'la (standarda deneysel damgayla girdi). (b) SOP+model-eşleme onayı: SOP'lar ileride hedef-model parametresi taşır (Fable prosedür yazar, Sonnet uygular) — #17 UFUK hattıyla aynı, ilk partide parametre YOK. (c) Çelişki kapısı maliyet uyarısı: kontrol her zaman dar kapsamlı (karar anı + dokunulan yüzey); ajan döneminde kategori-bazlı doğru ajanlara dağıtılır — "tüm projeyi tara" yasak sınıfı.

## Rakip analizi özeti — jimcen33/personal-os (tam metin: bu bölüm)
**Ne:** MIT lisanslı, 0-star TEMPLATE repo (v0.3.0, son push 06-20); "solo founder file-first LLM wiki + Cowork OS". Çalışan kısım: 23KB CLAUDE.md anayasası + AGENTS.md şeması + 17 SKILL.md + DECISIONS.md (D-001..014, reddedilen a
## Uygulanamayan desenler için mekanizma-seçim modelleri (07-12 4. oturum; Salih sorusu, karar ALINMADI — K-009/K-010 açılış gündemi malzemesi)
**İlke (Salih onaysız, Carvis önerisi):** ajan/skill/araştırma rakip değil sıralı — araştırma ilk adım (V36), sınıfı desenin NE DEVRETTİĞİ belirler (devretme merdiveni genellenmesi): doğrulama→skill · durma koşulu→/goal · zaman tetiği→Routine · kalıcı bağlam/kimlik→ajan · hiçbiri→altyapı.
**Üç model (token×zaman; K-013 bağlamlı):**
- **A "Ucuz tarama önce" (AZ/KISA):** desen-başına tek ucuz araştırma koşumu (kısa-çıktı sözleşmesi); inşa yalnız hazır-örnek kanıtıyla. Dayanak: Beads dersi. Risk: özgün sorunda kör.
- **B "Eşik-kapılı sınıf seçimi" (ORTA/ORTA):** A-filtre + merdivenle sınıf + tur-limitli pilot. Dayanak: "küçük pilot" + "başarısızlığı sisteme kodla" (resmi). Beklenti: başarı yüksek.
- **C "Ajan-önce" (ÇOK/UZUN):** desen-başına defterli ajan. K-013 verisi karşı: takım ~3-4x token; kural "paralellik kazancı > koordinasyon vergisi". En yüksek gelişim, ufka en riskli.
**Carvis önerisi: A→B hattı; C yalnız kanıtlı paralellik kazancında.** Karar Salih'te, K-009 açılışında.
(canlı repo vs boş şablon).
**Sonuç:** Bizim eksik olmayan şeyi (yetki+iş yürütme) hiç denememiş; bizim kurmadığımız şeyi (bilgi-hijyeni yönetişimi) olgun kurgulamış. Alınacak ≤3 fikir yukarıda ilgili adımlara dağıtıldı (Quality Gate → adım 2 · promote ilkesi → tüzük adayı · Zone C → adım 3).
