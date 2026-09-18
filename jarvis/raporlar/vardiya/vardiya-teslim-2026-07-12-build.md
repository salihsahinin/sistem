# Vardiya Teslim Raporu — 2026-07-12 (build oturumu)

## Biten
- **K-012 KAPANDI:** 5 build adımı (CLAUDE.md v1 · KILAVUZ v1 · wiki standardı + [[token-x-zaman]] + [[pointer-sistemi]] + hasat şablonu + test kuyruğu · pano v2 · köken-izi #1). Kurulum bitti.
- **K-013+V25 KAPANDI:** ekosistem araştırması + personal-os rakip analizi → 5 build-bulgusu; hepsi tartışma kuyruğunda, kanona sormadan hiçbir şey girmedi.
- **Push otomasyonu:** dar kapsamlı PAT `.secrets/`de (90 gün, ~10 Ekim ölür); 07-12 "token diske yazılmaz" kararı Salih onayıyla geri-açıldı.
- Oturum içi kararlar (Salih): DONE kuralı resmileşti · çürüdü-işareti (30 gün → BAYAT, düşme Salih onayıyla) · gürültü listesi + "araştır bakayım" istisnası · örnek-damıtma kuralı · pano yetki alanı · V25→K-013 birleşimi.

## Hasat (şablonun ilk koşusu — bu vardiya üzerinde)
**Görev:** K-012 build + K-013 · **Damga:** beyansız
1. **Özütler:** (a) Operasyon: mount çift-görünüm tuzağı — yazım sonrası doğrulama commit'ten önce (pointer-sistemi Gotchas'a işlendi). (b) Operasyon: git index mount'ta tekrar tekrar bozuluyor → çözüm `rm .git/index` + `GIT_INDEX_FILE=/tmp/...` + `git read-tree HEAD` (oturum-başı kurulmalı, kalıcı değil). (c) Desen: K-013'ü build önüne alma emri isabetli çıktı — v2-gist geç-keşfi önlendi; "araştırma-önce" deseni doğrulandı. (d) Davranış verisi: Salih seçenek sunulduğunda önce netleştirme sorusu soruyor — soru formatı cevap-yerine-soru dönüşüne açık tasarlanmalı (V6 hattı).
2. **Wiki-delta:** çelişki kapısı sayfası kuyruğun başında (örnekler tazeyken, sonraki oturum adayı).
3. **Verilebilir miydi (V20):** araştırma ajanlara verildi (3 koşu, isabetli); kanon yazımı Carvis'te kaldı — doğru, kanon yüzeyi devredilmez.
4. **Token×zaman etiketi:** kombinasyon token:ÇOK · zaman:UZUN (tam vardiya, ~15 commit) · beklenti: KISMEN tuttu (index arızaları + mount senkronu süreyi şişirdi). [V28 etiketi 1/10]

## Devir — sonraki vardiyanın sırası (Salih 07-12 kapanış kararları)
1. **Tartışma oturumu (ANA İŞ):** kuyruğun 3 bloğu — tüzük adayları · tez #0 kanonlaştırma · skill kararları. Gerekçe (Salih): "PortRisk nihai Jarvis'le hızlıca bitirilecek; yeni vizyonda yeni projeler — PortRisk'in oluşturulma yolu Jarvis ideasından farklı."
2. Günaydın görevini tazele (+ tetik-tarama satırı: gelmiş tetik var mı — TETİKLİ/UFUK çürüme koruması).
3. K-002 PortRisk Sprint 1 (ilk hasat-etiketli görev; commit Salih'in).
- Tetikli: instructions güncellemesi (tetik: tartışma kuyruğu bitince = "nihai Jarvis") — pano K-014.
