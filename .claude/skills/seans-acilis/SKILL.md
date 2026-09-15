---
name: seans-acilis
description: Jarvis'in (ajan; eski ad Carvis) depo seans-AÇILIŞ ritüelini koşar. Salih "seans başı" (standart tetik), "seansı devral", "seans aç", "oturuma başlayalım" dediğinde her yüzeyde çalışır — önsöz/soru eşlik etse bile önce ritüel. Selamlama zaman işareti değildir ve tek başına tetik değildir; durum yalnız JARVIS kanonundan okunur (profil/bulut hafızadan anlatılmaz). kullanılmaz; oturum-ortası selamlaşmada, kapanışta ("seans bitimi" → seans-kapanis), JARVIS-dışı sohbette, staj oturumlarında ("seans başı staj" — ayrım klasörle; staj kendi CLAUDE.md'sine oturur).
---

# Seans başı — seans açılışı (Jarvis, v0.5-deneysel-m29 — ad: gunaydin-vardiya → seans-acilis [Salih Katman-1 08-15]; v0.4: emekli-tetik temizliği 08-15; v0.3: Mac yolu + staj kapısı 08-12)

Selamlaşma sohbet değil **seans** **devridir**. Kural kaynağı tüzük (`core/tuzuk-v0.md`); bu skill davranışı tetikler, bilgiyi **taşımaz** — çelişkide kanon kazanır.

## 0. Zaman-kayması freni (Salih Katman-1, 2026-08-15)
Selamlama **oturum-sınırı** işaretidir, **zaman** işareti **değil**: açılış sözünden sabah/yeni-gün, kapanış sözünden gece **çıkarımı** **yapılmaz**. Tarih/saat yalnız sistem kaynağından (env tarihi, `date`) okunur. Standart tetik "seans başı" (eski selamlama tetikleri `EMEKLİ` — `core/baglam-anahtar-kaydi.md` §2; selamlama tek başına ritüeli tetiklemez, Salih emri 08-15); jarvis↔staj ayrımı **cümleyle değil klasörle** yapılır (~/jarvis → bu ritüel · staj klasörü → staj-acilis).

## 1. Yüzey + hat tespiti
0. **staj kapısı** (önce bu): oturum staj klasöründen açıldıysa ya da beyan "staj" içeriyorsa ("seans başı staj") → BU **ritüel** **koşulmaz**. Staj oturumu jarvis kanonunu okumaz; staj klasörünün CLAUDE.md'si geçerlidir (Salih kararı 2026-08-12; md.49 sınırı). Tek cümleyle beyan et, staj akışına geç.
1. JARVIS kanonuna erişim var mı? (Mac: `~/jarvis` doğrudan [varsayılan yüzey] · Windows PC: `C:\JARVIS` doğrudan · bulut claude.ai: origin klonu üzerinden · köprüsüz mobil: `YOK`.)
2. Erişim **yoksa** → `SNAPSHOT` modu: ilk cümlede beyan et, kalıcı karar alma, her çıktıyı "**ham fikir** / kanonlu cihazda ingest edilecek" damgala; varsa en güncel `CHAT-KAPSULU-*.md` / `CEP-KAPSULU-*.md` zemin olur. Kalan adımları atla.
3. Hat beyanı (paralel seans, KILAVUZ): "seans başı, PortRisk" → ölçüm-bankı şeridi; "seans başı jarvis geliştirme" → geliştirme hattı (L8/Kun-Chen kopyası dahil); sade "seans başı" → prototip (varsayılan); "seans başı, <öğrenme şeridi>" (evals · guvenlik · mit-6006 · mit-6042j · mat-felsefesi) → BU **ritüel koşulmaz**, `ogren` skill'i (İB-89, 09-15); belirsizse **tek** soru sor.
4. **canlı-oturum** **kapısı** (**kural** — Salih imzası 08-17 KB-08; kaynak `wiki/paralel-oturum-protokolu.md` §1; **resume eki** Karar 57: her resume'da da koşar): **`python3 tools/acilis-kapilari.py`** (İB-91) → K1 satırı `ŞÜPHE` ise brifte "paralel-oturum şüphesi" beyan et, Salih'e **tek** soru ("başka oturum açık mı?"), diğer oturumun işini ikinci kez koşma, dosyalarına yazma, commit'ler `git add <yol>` (H4). Son 5 commit yaşıyla listelenir; tanınmayan commit varsa devir-notu, karar-no/pointer oradan devralınır.
5. **koşum-önü** **manifest kapısı** (**kural** — KB-08): Workflow/atlas/pipeline açmadan **`python3 tools/acilis-kapilari.py --is "<konu>"`** → K2 **koşmuş-aday** ise manifest/commit'i oku, devral, koşma (vaka-3: 518k mükerrer).

## 2. Kanon okuma (cevaptan önce, sırayla)
1. `CLAUDE.md` — oturum kuralları + güncel okuma-sırası (otomatik gelmediyse dosyadan oku; skill'deki liste eskirse CLAUDE.md kazanır).
2. `core/durum-kapsulu.md` — **origin klonundan** doğrula: `.git/config`teki origin URL ile bulut konteynerde clone at, mount ile diff'le. Mount'ta git komutu **yasak** (okuma dahil); klon bulutta serbest.
3. `core/pano.md` — AKTİF/BEKLEYEN/BLOKE + "Ekrana gel" filtresi.
3b. **Silver tazelik kapısı (KB-54 A, Karar 62):** tespit otomatik (SessionStart brifi `SİLVER: … TAZE | BAYAT` + `tools/acilis-kapilari.py` K3); `BAYAT` → `python3 tools/katman-hatti.py` (~12 sn, idempotent) bu adımda; atlanırsa adresli erişim yanlış satır getirir (08-18 vakası 25/27). Worktree'de K3 `YOK` normaldir (öğrenme oturumu koşmaz).
3c. **Adresli erişim kuralı (KB-53 A, Karar 62; KILAVUZ tasarım-ilkeleri satırı; İB-28):** kanon okurken adres biliniyorsa **aralık** oku (`Read offset/limit` ∨ `sed -n 'a,bp'`), anahtar biliniyorsa silver'dan blok çek (`sqlite3 veri/baglam.sqlite` — `v_guncel_kayit`; kayit_id sha8'i getirme anında yeniden hesaplanır, tutmuyorsa dosyaya düş + bayrak); dosya **bütünü** yalnız adres yokken (kapsül/pano gibi tamamı okunması gereken küçük dosyalar hariç). Oran `v_okuma_orani`'nda sayılır (İB-29) — düşük aralık-oranı ince-tutkal (KB-53 b) kararını masaya döndürür.
4. ~~senkron-log okuma~~ `EMEKLİ` (Karar 88 M9, Salih 09-09): gece-senkron Karar 81 ile iptal, gece işi gnhf şeridinde (Karar 84); kütük `raporlar/usage/senkron-log.jsonl` arşiv-pointer olarak durur, okunmaz.
5. Kapsülün işaret ettiği son seans-teslim raporu (devir borçları buradan).
6. Gerekirse pointer'la in: fikir-kutusu · senaryo-defteri · cc/defter — hepsi kapsül/CLAUDE.md adresliyorsa.

## 3. Açılış brifi (çıktı formatı, m.18)
- İnsan-yüzü **tek satır** durum, sonra kısa brif: sayaç/sicil durumu · kapsülün "sonraki ilk iş" listesi · Salih'te bekleyen kararlar · devir borçları. Çıplak veri; övgü-merci yok (m.7).
- İlk iş bir Salih kararıysa seçenekli sun: ölçek-eşiği üstüyse 3-model karşılaştırması (m.37: token×zaman×beklenen-kalite, sayısal, önerilen işaretli) + yansız soru dili (V6). Cevap sonucu değiştirmeyecekse soru sorma (m.4).
- Sonrasında söylenen her şey görev olarak devralınır (m.25); kapasite cevabı üç halden biri: yaparım / yapamam(+neden) / proje gerekir(+kart, kaba token×zaman) — "bakarız" yasak.
- **Seans hedefi (deneme — m.29; KB-47 A, Salih 08-21, 5 seans sonra mini-değerlendirme):** brifin sonunda tek cümlelik **açık** **hedef** yer alır — Salih açılışta beyan ettiyse aynen, etmediyse 'sonraki ilk iş'ten türetilip teyide sunulur; kapanışta hedef yoklanır (tutmadıysa sapma tek cümle kayda). Sprint Goal işlevi, ad Sprint **değil** (KB-49 ailesi).

## 4. Sabit frenler
- Ne derse emirdir; tek fren çelişki kapısı (m.16): önce çelişki+artı/eksi+plan raporu, sonra emir.
- Yasaklar: günlük-özüt/ruh-hali/psikolog (m.23) · ayıklık sorgusu (m.33) · otomatik silme (m.8).
- Yazamayan yüzeyde karar kaydı üretme; damgalı not bırak, ana seans ingest eder.
- **Bağlam bütçesi (KB-50 A, Karar 61; İB-46):** tek araç çıktısı >~10k token bağlama dökülmez — dosyaya yaz, özet + pointer ver (ör. büyük `cat`/workflow çıktısı); alt-ajan dönüşü ≤2k; eşzamanlı kural sayısı ≤100 (`tools/kural-sayaci.py`). Uzun koşumda (Workflow/atlas) hasat kontrol listesi seans-kapanis §6e'dedir.

## Gotchas
- **Önsöz tuzağı:** Salih selamla birlikte soru/önsöz yazarsa modelin içeriğe atlaması — ritüel **her zaman** önce (2026-07-23 arızasının kökü).
- **Profil-hafıza tuzağı:** ayarlardaki kişiselleştirme metni bayat snapshot'tır; durum oradan anlatılmaz.
- **Bayat kapsül (V4):** kapsül tarihi eskiyse körü körüne çapalanma — son teslim raporu + git log ile çapraz kontrol et, tutarsızlığı brifte söyle.
- Model değişimi yaşanmış oturumdan devir varsa: şerhli-klasör protokolü (KILAVUZ) — şerhli içerik kanon sayılmaz.
