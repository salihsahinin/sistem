---
name: seans-acilis
description: Carvis'in JARVIS vardiya-AÇILIŞ ritüelini koşar. Salih "seans başı" (standart tetik), "vardiyayı devral", "vardiya aç", "oturuma başlayalım" dediğinde ya da yeni oturumu açılış beyanıyla başlattığında HER YÜZEYDE çalışır — önsöz/soru eşlik etse bile önce ritüel. Selamlama sözü zaman işareti DEĞİLDİR ve tek başına tetik DEĞİLDİR; durum yalnız JARVIS kanonundan okunur (profil/bulut hafızadan ANLATILMAZ). KULLANILMAZ; oturum-ortası selamlaşmada, kapanışta ("seans bitimi" → seans-kapanis), JARVIS-dışı sohbette ve STAJ OTURUMLARINDA ("seans başı staj" / staj klasörü — ayrım klasörle; staj oturumu kendi CLAUDE.md'sine oturur).
---

# Seans başı — vardiya açılışı (Carvis, v0.5-deneysel-m29 — ad: gunaydin-vardiya → seans-acilis [Salih Katman-1 08-15]; v0.4: emekli-tetik temizliği 08-15; v0.3: Mac yolu + staj kapısı 08-12)

Selamlaşma sohbet değil VARDİYA DEVRİDİR. Kural kaynağı tüzük (`core/tuzuk-v0.md`); bu skill davranışı tetikler, bilgiyi TAŞIMAZ — çelişkide kanon kazanır.

## 0. ZAMAN-KAYMASI FRENİ (Salih Katman-1, 2026-08-15)
Selamlama OTURUM-SINIRI işaretidir, ZAMAN işareti DEĞİL: açılış sözünden sabah/yeni-gün, kapanış sözünden gece ÇIKARIMI YAPILMAZ. Tarih/saat yalnız sistem kaynağından (env tarihi, `date`) okunur. Standart tetik "seans başı" (eski selamlama tetikleri EMEKLİ — `core/baglam-anahtar-kaydi.md` §2; selamlama tek başına ritüeli tetiklemez, Salih emri 08-15); jarvis↔staj ayrımı CÜMLEYLE DEĞİL KLASÖRLE yapılır (~/jarvis → bu ritüel · staj klasörü → staj-acilis).

## 1. Yüzey + hat tespiti
0. STAJ KAPISI (önce bu): oturum staj klasöründen açıldıysa ya da beyan "staj" içeriyorsa ("seans başı staj") → BU RİTÜEL KOŞULMAZ. Staj oturumu jarvis kanonunu okumaz; staj klasörünün CLAUDE.md'si geçerlidir (Salih kararı 2026-08-12; md.49 sınırı). Tek cümleyle beyan et, staj akışına geç.
1. JARVIS kanonuna erişim var mı? (Mac: `~/jarvis` doğrudan [varsayılan yüzey] · Windows PC: `C:\JARVIS` doğrudan · bulut claude.ai: origin klonu üzerinden · köprüsüz mobil: YOK.)
2. Erişim YOKSA → SNAPSHOT modu: ilk cümlede beyan et, kalıcı karar alma, her çıktıyı "HAM FİKİR / kanonlu cihazda ingest edilecek" damgala; varsa en güncel `CHAT-KAPSULU-*.md` / `CEP-KAPSULU-*.md` zemin olur. Kalan adımları atla.
3. Hat beyanı (paralel vardiya, KILAVUZ): "seans başı, PortRisk" → ölçüm-bankı şeridi; "seans başı jarvis geliştirme" → geliştirme hattı (L8/Kun-Chen kopyası dahil); sade "seans başı" → prototip (varsayılan); belirsizse TEK soru sor.
4. CANLI-OTURUM ŞÜPHESİ (kural-adayı, `kuyruk/gelen-2026-08-15-paralel-oturum-vaka-2.md`; deneysel): son commit ≤15 dk ∧ kapsülde o vardiyanın kapanış kaydı yok → brifte "paralel-oturum şüphesi" beyan et; diğer oturumun manifestte SAHADA görünen işini ikinci kez koşma, onun dosyalarına yazma; hat paylaşımını Salih'e tek soruyla sor.

## 2. Kanon okuma (cevaptan ÖNCE, sırayla)
1. `CLAUDE.md` — oturum kuralları + güncel okuma-sırası (otomatik gelmediyse dosyadan oku; skill'deki liste eskirse CLAUDE.md kazanır).
2. `core/durum-kapsulu.md` — ORIGIN KLONUNDAN doğrula: `.git/config`teki origin URL ile bulut konteynerde clone at, mount ile diff'le. Mount'ta git komutu YASAK (okuma dahil); klon bulutta serbest.
3. `core/pano.md` — AKTİF/BEKLEYEN/BLOKE + "Ekrana gel" filtresi.
4. `raporlar/usage/senkron-log.jsonl` — son satır: senkron sayacı ilerledi mi, arıza var mı (arıza → sayaç sıfırlanmaz ama kök-neden raporlanır).
5. Kapsülün işaret ettiği son vardiya-teslim raporu (devir borçları buradan).
6. Gerekirse pointer'la in: fikir-kutusu · senaryo-defteri · cc/defter — hepsi kapsül/CLAUDE.md adresliyorsa.

## 3. Açılış brifi (çıktı formatı, m.18)
- İnsan-yüzü TEK SATIR durum, sonra kısa brif: sayaç/sicil durumu · kapsülün "sonraki ilk iş" listesi · Salih'te bekleyen kararlar · devir borçları. Çıplak veri; övgü-merci yok (m.7).
- İlk iş bir Salih kararıysa seçenekli sun: ölçek-eşiği üstüyse 3-model karşılaştırması (m.37: token×zaman×beklenen-kalite, sayısal, önerilen işaretli) + yansız soru dili (V6). Cevap sonucu değiştirmeyecekse soru sorma (m.4).
- Sonrasında söylenen her şey görev olarak devralınır (m.25); kapasite cevabı üç halden biri: yaparım / yapamam(+neden) / proje gerekir(+kart, kaba token×zaman) — "bakarız" yasak.

## 4. Sabit frenler
- Ne derse emirdir; tek fren çelişki kapısı (m.16): önce çelişki+artı/eksi+plan raporu, sonra emir.
- Yasaklar: günlük-özüt/ruh-hali/psikolog (m.23) · ayıklık sorgusu (m.33) · otomatik silme (m.8).
- Yazamayan yüzeyde karar kaydı üretme; damgalı not bırak, ana vardiya ingest eder.

## Gotchas
- **Önsöz tuzağı:** Salih selamla birlikte soru/önsöz yazarsa modelin içeriğe atlaması — ritüel HER ZAMAN önce (2026-07-23 arızasının kökü).
- **Profil-hafıza tuzağı:** ayarlardaki kişiselleştirme metni bayat snapshot'tır; durum oradan anlatılmaz.
- **Bayat kapsül (V4):** kapsül tarihi eskiyse körü körüne çapalanma — son teslim raporu + git log ile çapraz kontrol et, tutarsızlığı brifte söyle.
- Model değişimi yaşanmış oturumdan devir varsa: şerhli-klasör protokolü (KILAVUZ) — şerhli içerik kanon sayılmaz.
