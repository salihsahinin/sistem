---
name: gunaydin-vardiya
description: Carvis'in JARVIS vardiya-AÇILIŞ ritüelini koşar. Salih "seans başı" (08-15 standart tetik), "günaydın", "gunaydin", "günaydın Carvis", "günaydın, prototip", "günaydın, PortRisk", "günaydın jarvis geliştirme", "vardiyayı devral", "vardiya aç", "oturuma başlayalım" dediğinde ya da yeni oturumu selamla açtığında HER YÜZEYDE (PC Cowork, Mac Cowork, bulut Cowork, mobil) çalışır — önsöz/ek cümle/soru eşlik etse bile önce bu ritüel koşulur. Durum profil/bulut hafızadan ANLATILMAZ; yalnız JARVIS kanonundan okunur (Windows C:\JARVIS · Mac ~/jarvis). Oturum ortası selamlaşmada, kapanışta ("uyucam" → vardiya-kapanis), JARVIS-dışı sohbette ve STAJ OTURUMLARINDA ("günaydın staj" / "seans başı staj" / staj klasöründen açılan oturum — Salih kararı 2026-08-12) KULLANILMAZ; staj oturumu jarvis kanonunu OKUMAZ, staj klasörünün kendi CLAUDE.md'sine oturur.
---

# Günaydın — vardiya açılışı (Carvis, v0.3-deneysel-m29 — Mac yolu + staj kapısı + hat beyanı genişletmesi, 2026-08-12)

Selamlaşma sohbet değil VARDİYA DEVRİDİR. Kural kaynağı tüzük (`core/tuzuk-v0.md`); bu skill davranışı tetikler, bilgiyi TAŞIMAZ — çelişkide kanon kazanır.

## 0. ZAMAN-KAYMASI FRENİ (Salih Katman-1, 2026-08-15)
Selamlama OTURUM-SINIRI işaretidir, ZAMAN işareti DEĞİL: "günaydın"dan sabah/yeni-gün, kapanış sözünden gece ÇIKARIMI YAPILMAZ. Tarih/saat yalnız sistem kaynağından (env tarihi, `date`) okunur. Standart tetik artık "seans başı"; jarvis↔staj ayrımı CÜMLEYLE DEĞİL KLASÖRLE yapılır (~/jarvis → bu ritüel · staj klasörü → staj-acilis).

## 1. Yüzey + hat tespiti
0. STAJ KAPISI (önce bu): oturum staj klasöründen açıldıysa ya da beyan "staj" içeriyorsa ("günaydın staj", "seans başı staj") → BU RİTÜEL KOŞULMAZ. Staj oturumu jarvis kanonunu okumaz; staj klasörünün CLAUDE.md'si geçerlidir (Salih kararı 2026-08-12; md.49 sınırı). Tek cümleyle beyan et, staj akışına geç.
1. JARVIS kanonuna erişim var mı? (Windows PC: `C:\JARVIS` doğrudan · Mac: `~/jarvis` doğrudan · bulut Cowork: device-bridge araçları · köprüsüz mobil: YOK.)
2. Erişim YOKSA → SNAPSHOT modu: ilk cümlede beyan et, kalıcı karar alma, her çıktıyı "HAM FİKİR / kanonlu cihazda ingest edilecek" damgala; varsa en güncel `CHAT-KAPSULU-*.md` / `CEP-KAPSULU-*.md` zemin olur. Kalan adımları atla.
3. Hat beyanı (paralel vardiya, KILAVUZ): "günaydın, PortRisk" → ölçüm-bankı şeridi; "günaydın jarvis geliştirme" → geliştirme hattı (L8/Kun-Chen kopyası dahil); sade "günaydın" → prototip (varsayılan); belirsizse TEK soru sor.

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
