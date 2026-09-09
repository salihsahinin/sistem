---
name: seans-acilis
description: Carvis'in JARVIS seans-AÇILIŞ ritüelini koşar. Salih "seans başı" (standart tetik), "seansı devral", "seans aç", "oturuma başlayalım" dediğinde HER YÜZEYDE çalışır — önsöz/soru eşlik etse bile önce ritüel. Selamlama zaman işareti DEĞİLDİR ve tek başına tetik DEĞİLDİR; durum yalnız JARVIS kanonundan okunur (profil/bulut hafızadan ANLATILMAZ). KULLANILMAZ; oturum-ortası selamlaşmada, kapanışta ("seans bitimi" → seans-kapanis), JARVIS-dışı sohbette, STAJ oturumlarında ("seans başı staj" — ayrım klasörle; staj kendi CLAUDE.md'sine oturur).
---

# Seans başı — seans açılışı (Carvis, v0.5-deneysel-m29 — ad: gunaydin-vardiya → seans-acilis [Salih Katman-1 08-15]; v0.4: emekli-tetik temizliği 08-15; v0.3: Mac yolu + staj kapısı 08-12)

Selamlaşma sohbet değil SEANS DEVRİDİR. Kural kaynağı tüzük (`core/tuzuk-v0.md`); bu skill davranışı tetikler, bilgiyi TAŞIMAZ — çelişkide kanon kazanır.

## 0. ZAMAN-KAYMASI FRENİ (Salih Katman-1, 2026-08-15)
Selamlama OTURUM-SINIRI işaretidir, ZAMAN işareti DEĞİL: açılış sözünden sabah/yeni-gün, kapanış sözünden gece ÇIKARIMI YAPILMAZ. Tarih/saat yalnız sistem kaynağından (env tarihi, `date`) okunur. Standart tetik "seans başı" (eski selamlama tetikleri EMEKLİ — `core/baglam-anahtar-kaydi.md` §2; selamlama tek başına ritüeli tetiklemez, Salih emri 08-15); jarvis↔staj ayrımı CÜMLEYLE DEĞİL KLASÖRLE yapılır (~/jarvis → bu ritüel · staj klasörü → staj-acilis).

## 1. Yüzey + hat tespiti
0. STAJ KAPISI (önce bu): oturum staj klasöründen açıldıysa ya da beyan "staj" içeriyorsa ("seans başı staj") → BU RİTÜEL KOŞULMAZ. Staj oturumu jarvis kanonunu okumaz; staj klasörünün CLAUDE.md'si geçerlidir (Salih kararı 2026-08-12; md.49 sınırı). Tek cümleyle beyan et, staj akışına geç.
1. JARVIS kanonuna erişim var mı? (Mac: `~/jarvis` doğrudan [varsayılan yüzey] · Windows PC: `C:\JARVIS` doğrudan · bulut claude.ai: origin klonu üzerinden · köprüsüz mobil: YOK.)
2. Erişim YOKSA → SNAPSHOT modu: ilk cümlede beyan et, kalıcı karar alma, her çıktıyı "HAM FİKİR / kanonlu cihazda ingest edilecek" damgala; varsa en güncel `CHAT-KAPSULU-*.md` / `CEP-KAPSULU-*.md` zemin olur. Kalan adımları atla.
3. Hat beyanı (paralel seans, KILAVUZ): "seans başı, PortRisk" → ölçüm-bankı şeridi; "seans başı jarvis geliştirme" → geliştirme hattı (L8/Kun-Chen kopyası dahil); sade "seans başı" → prototip (varsayılan); belirsizse TEK soru sor.
4. CANLI-OTURUM KAPISI (KURAL — Salih imzası 08-17 masa KB-08; kaynak: `wiki/paralel-oturum-protokolu.md`): son commit ≤15 dk ∧ kapsülde o seansın kapanış kaydı yok → brifte "paralel-oturum şüphesi" beyan et; diğer oturumun manifestte SAHADA görünen işini ikinci kez koşma, onun dosyalarına yazma; hat paylaşımını Salih'e TEK soruyla sor ("başka oturum açık mı?"); canlıysa commit'ler `git add <yol>` ile (H4, `git add -A` yasak). **RESUME EKİ (Salih imzası 08-21, Karar 57 — arıza-4 dersi): bu kapı yalnız seans-açılışında değil HER RESUME'da koşar** — oturuma dönüşte ilk cevaptan önce `git log -5` + kapsül Güncelleme satırı okunur; tanınmayan commit varsa devir-notu düşülür, karar-numarası/pointer durumu ORADAN devralınır (~10 sn; atlanırsa vaka-4 sınıfı çakışma).
5. KOŞUM-ÖNÜ MANİFEST KAPISI (KURAL — Salih imzası 08-17 KB-08): Workflow/atlas/pipeline açmadan önce ilgili `cc/pipeline/pipeline-*.md` manifesti + `git log -15` okunur — "bu iş zaten koşmuş/koşuyor mu?" (vaka-3: 518k mükerrer koşum); koşmuşsa devral, koşma.

## 2. Kanon okuma (cevaptan ÖNCE, sırayla)
1. `CLAUDE.md` — oturum kuralları + güncel okuma-sırası (otomatik gelmediyse dosyadan oku; skill'deki liste eskirse CLAUDE.md kazanır).
2. `core/durum-kapsulu.md` — ORIGIN KLONUNDAN doğrula: `.git/config`teki origin URL ile bulut konteynerde clone at, mount ile diff'le. Mount'ta git komutu YASAK (okuma dahil); klon bulutta serbest.
3. `core/pano.md` — AKTİF/BEKLEYEN/BLOKE + "Ekrana gel" filtresi.
3b. **Silver tazelik kapısı (KB-54 A, Salih imzası 08-21, Karar 62):** `uretim.git_head_sha` ≠ git HEAD → brifte "silver bayat" uyarısı + `tools/katman-hatti.py` koşumu (~5-10 sn, idempotent); atlanırsa adresli erişim yanlış satır getirebilir (08-18 vakası: 25/27 blok uyuşmazlığı). **Tespit otomatik (İB-27, 08-22):** SessionStart hook brifinde `SİLVER: … → TAZE | BAYAT` satırı; BAYAT görülürse koşum bu adımda (hook koşmaz, yalnız söyler).
3c. **Adresli erişim kuralı (KB-53 A, Karar 62; KILAVUZ tasarım-ilkeleri satırı; İB-28):** kanon okurken adres biliniyorsa ARALIK oku (`Read offset/limit` ∨ `sed -n 'a,bp'`), anahtar biliniyorsa silver'dan blok çek (`sqlite3 veri/baglam.sqlite` — `v_guncel_kayit`; kayit_id sha8'i getirme anında yeniden hesaplanır, tutmuyorsa dosyaya düş + bayrak); dosya BÜTÜNÜ yalnız adres yokken (kapsül/pano gibi tamamı okunması gereken küçük dosyalar hariç). Oran `v_okuma_orani`'nda sayılır (İB-29) — düşük aralık-oranı ince-tutkal (KB-53 b) kararını masaya döndürür.
4. ~~senkron-log okuma~~ EMEKLİ (Karar 88 M9, Salih 09-09): gece-senkron Karar 81 ile iptal, gece işi gnhf şeridinde (Karar 84); kütük `raporlar/usage/senkron-log.jsonl` arşiv-pointer olarak durur, okunmaz.
5. Kapsülün işaret ettiği son seans-teslim raporu (devir borçları buradan).
6. Gerekirse pointer'la in: fikir-kutusu · senaryo-defteri · cc/defter — hepsi kapsül/CLAUDE.md adresliyorsa.

## 3. Açılış brifi (çıktı formatı, m.18)
- İnsan-yüzü TEK SATIR durum, sonra kısa brif: sayaç/sicil durumu · kapsülün "sonraki ilk iş" listesi · Salih'te bekleyen kararlar · devir borçları. Çıplak veri; övgü-merci yok (m.7).
- İlk iş bir Salih kararıysa seçenekli sun: ölçek-eşiği üstüyse 3-model karşılaştırması (m.37: token×zaman×beklenen-kalite, sayısal, önerilen işaretli) + yansız soru dili (V6). Cevap sonucu değiştirmeyecekse soru sorma (m.4).
- Sonrasında söylenen her şey görev olarak devralınır (m.25); kapasite cevabı üç halden biri: yaparım / yapamam(+neden) / proje gerekir(+kart, kaba token×zaman) — "bakarız" yasak.
- **Seans hedefi (DENEME — m.29; KB-47 A, Salih 08-21, 5 seans sonra mini-değerlendirme):** brifin sonunda tek cümlelik AÇIK HEDEF yer alır — Salih açılışta beyan ettiyse aynen, etmediyse 'sonraki ilk iş'ten türetilip teyide sunulur; kapanışta hedef yoklanır (tutmadıysa sapma tek cümle kayda). Sprint Goal işlevi, ad Sprint DEĞİL (KB-49 ailesi).

## 4. Sabit frenler
- Ne derse emirdir; tek fren çelişki kapısı (m.16): önce çelişki+artı/eksi+plan raporu, sonra emir.
- Yasaklar: günlük-özüt/ruh-hali/psikolog (m.23) · ayıklık sorgusu (m.33) · otomatik silme (m.8).
- Yazamayan yüzeyde karar kaydı üretme; damgalı not bırak, ana seans ingest eder.
- **Bağlam bütçesi (KB-50 A, Karar 61; İB-46):** tek araç çıktısı >~10k token bağlama dökülmez — dosyaya yaz, özet + pointer ver (ör. büyük `cat`/workflow çıktısı); alt-ajan dönüşü ≤2k; eşzamanlı kural sayısı ≤100 (`tools/kural-sayaci.py`). Uzun koşumda (Workflow/atlas) hasat kontrol listesi seans-kapanis §6e'dedir.

## Gotchas
- **Önsöz tuzağı:** Salih selamla birlikte soru/önsöz yazarsa modelin içeriğe atlaması — ritüel HER ZAMAN önce (2026-07-23 arızasının kökü).
- **Profil-hafıza tuzağı:** ayarlardaki kişiselleştirme metni bayat snapshot'tır; durum oradan anlatılmaz.
- **Bayat kapsül (V4):** kapsül tarihi eskiyse körü körüne çapalanma — son teslim raporu + git log ile çapraz kontrol et, tutarsızlığı brifte söyle.
- Model değişimi yaşanmış oturumdan devir varsa: şerhli-klasör protokolü (KILAVUZ) — şerhli içerik kanon sayılmaz.
