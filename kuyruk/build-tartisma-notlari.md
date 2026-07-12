# Build Tartışma Notları — K-013 + Rakip Analizi Bulguları
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

## Tüzük adayları (Katman 1 — yalnız tartışmada)
- **Taze-oturum promote ilkesi** (personal-os D-004): "kalıcılaştırma kararı, içeriği üreten oturumda verilemez" — dış-mahkeme desenimizin (MİDAS v6.1) genelleştirilmiş hali.
- **weekly-taste-sync gerekçesi**: davranış-kuralı değişikliği günlük değil ritimli+onaylı patch'le ("günlük döngü ruh haline over-fit eder") — m.23'ü bağımsız doğruluyor; kural-değişim ritmi fikri alınabilir.

## Ajan dönemi defteri (K-009/K-010 açılınca gündeme gelir; şimdi dokunulmaz)
- Loop guardrails: 3 tur · 10 dk · sıfır-ilerleme-durdur (personal-os) + tur limiti/bütçe tavanı (saha standardı).
- Heartbeat maliyet deseni: script veri toplar → LLM yalnız akıl yürütür (~7x ucuz).
- Rol-başına model katmanlama + "ucuz model ≠ ucuz iş" ölçülmüş dersi (Haiku analitik işte daha çok tur → toplam token daha kötü) — #24b formülünün girdisi.
- Karar kuralı: paralellik kazancı > koordinasyon vergisi ise takım, değilse tek güçlü ajan.
- Beads/gastown: ajan-yazılabilir pano + worktree izolasyonu + rol-adlı kalıcı kimlikler (m.30 ile uyumlu).

## Rakip analizi özeti — jimcen33/personal-os (tam metin: bu bölüm)
**Ne:** MIT lisanslı, 0-star TEMPLATE repo (v0.3.0, son push 06-20); "solo founder file-first LLM wiki + Cowork OS". Çalışan kısım: 23KB CLAUDE.md anayasası + AGENTS.md şeması + 17 SKILL.md + DECISIONS.md (D-001..014, reddedilen alternatiflerle). İçerik katmanları TAMAMEN BOŞ (.gitkeep). "Her gün kullanıyorum" iddiası doğrulanamadı.
**Örtüşmeler:** pointer ilkesi ("point to resource files, don't inline") · hot.md = durum-kapsulü ikizi · Karpathy-wiki kökü · Inbox+Queue = fikir kutusu+seçim turu · onay kapısı ("never auto-file ambiguous") · anti-sycophancy (Skeptic skill) · karar kaydı.
**Onlarda olup bizde olmayan (değerlendirmeli):** Quality Gate+expiry (DEĞER) · taze-oturum promote (DEĞER) · Zone C SOP şablonu (DEĞER) · frontmatter+lint 7 kontrolü/çürüme denetimi (DEĞER, büyüyünce) · Disposable Noise (DEĞER) · Spotlight skorlu-sessizlik (kısmi — sayısal rubrik tek kullanıcıda sahte-kesinlik) · AGENTS.md (şimdilik gürültü) · workstation katmanlama (nötr) · run-log.jsonl+loop guardrails (değerli ama erken).
**Bizde olup onlarda olmayan (farklılaşma):** Patron-CEO yetki anayasası (32+1 madde, Katman 1/2, veto=revert) · commit-disiplini-hafıza (onlarda git sadece dağıtım) · pano+vardiya+ajan raporları (onlar kütüphane, biz İŞ YÜRÜTME şirketi) · gerekçeli seçim turu + kapsam dondurma + negatif-ROI kararları · tek-kullanıcı/lider koruması + çelişki kapısı · fiili üretim kanıtı (canlı repo vs boş şablon).
**Sonuç:** Bizim eksik olmayan şeyi (yetki+iş yürütme) hiç denememiş; bizim kurmadığımız şeyi (bilgi-hijyeni yönetişimi) olgun kurgulamış. Alınacak ≤3 fikir yukarıda ilgili adımlara dağıtıldı (Quality Gate → adım 2 · promote ilkesi → tüzük adayı · Zone C → adım 3).
