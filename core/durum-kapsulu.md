# Durum Kapsülü

*Her oturumun İLK okuduğu dosya. Üzerine yazılır; arşiv değildir.*

**Güncelleme:** 2026-07-12 build oturumu kapanışı (Carvis yazdı)

## Şu an
**K-012 KAPANDI — JARVIS kurulumu bitti.** 5 build adımı canlı: CLAUDE.md v1 (bootstrap gitti) · KILAVUZ.md v1 · wiki standardı + 2 sayfa + hasat şablonu + test kuyruğu · pano v2 · köken-izi #1. K-013+V25 araştırması kapandı (`raporlar/2026-07-12-K013-ekosistem-arastirmasi.md`). **Push otomasyonu canlı:** `.secrets/github-pat` (dar kapsam, ~10 Ekim'de ölür — o gün hatırlat). KILAVUZ okuma borcu Salih'te.

## Son kararlar (07-12 build; detay: vardiya-teslim-2026-07-12-build.md + git log)
DONE kuralı resmileşti · çürüdü-işareti (30g→BAYAT, düşme Salih onaylı) · gürültü listesi + "araştır bakayım" istisnası · örnek-damıtma (sayfaya damıtılmış 1 örnek, ham senaryo pointer'la) · pano yetki alanı · PAT geri-açma · Salih tezi #0 + ölçüm-öncelikli strateji KAYITLI (kanonlaşma tartışması bekliyor).

## Açık borçlar
- **SONRAKİ OTURUM ANA İŞİ: tartışma oturumu** — `kuyruk/build-tartisma-notlari.md` 3 blok: tüzük adayları (taze-oturum promote + kural-değişim ritmi) · tez #0 kanonlaştırma · skill kararları. Salih emri: kuyruk bitmeli (PortRisk nihai Jarvis'le hızlı bitirilecek, yeni vizyon projeleri gelecek).
- Günaydın scheduled görevi tazele + **tetik-tarama satırı ekle** (TETİKLİ/UFUK maddelerin gelmiş tetiği var mı — çürüme koruması, Salih 07-12).
- K-014 (yeni): Claude chat instructions güncellemesi — tetik: tartışma kuyruğu bitince ("nihai Jarvis").
- Wiki kuyruğu: çelişki kapısı sayfası (örnekler taze) · sonra ilk-parti kalanı.
- Tetikli: K-011 taşıma (Salih gün seçince) · N matematiği (dış-chat) · V28 (etiket 1/10) · V27 · K-004 (Kasım).

## Sonraki ilk iş
**Tartışma oturumu (3 blok) → günaydın tazeleme → K-002 PortRisk Sprint 1** (tek aktif kart; pytest yeşil + push, commit Salih'in; ilk hasat-etiketli görev).

## Teknik not (operasyon)
Git index mount'ta bozulabiliyor: çözüm `rm -f .git/index` → `export GIT_INDEX_FILE=/tmp/jarvis-index` → `git read-tree HEAD` (her oturumda yeniden kurulur). Mount çift-görünüm: dosya yazımından sonra bash tarafında doğrula, öyle commit'le.

## Sınırlar
Otomasyon/canlı ajan yok (K-009/K-010) · diğer vault'lara yazım yok · core/ yalnız Salih kararıyla · m.33 ayıklık sorgusu yok · tek-flagship PortRisk (m.13).
