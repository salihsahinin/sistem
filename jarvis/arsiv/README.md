# arsiv/ — tek çatı

Repo-genel arşiv kökü (dosya düzeni planı, parti 2, 2026-09-09). Alt dizinler:

- **kurulus-2026-07/** — kök seviye kuruluş dosyaları (parti 1, Fable doldurur; bu partide boş olabilir).
- **kuyruk-arsiv/** — eski `kuyruk/arsiv/` (damıtma/yeniden-yazım arşivleri: defter, kutu, pano, KILAVUZ, ölçüm-bankı arşiv dosyaları; tarihli, `-YYYY-MM-DD.md` adlandırma).
- **karantina/** — İB-72 BAYAT-DOSYA KARANTİNA MEKANİZMASI hedefi (eski `kuyruk/arsiv/karantina/`); dizin yapısı korunarak taşınan dosyalar, BAKMA-GEREK-YOK bayraklı; envanter `python3 tools/karantina.py --liste`, denetim `--denetle`, kayıt `veri/karantina.jsonl`.
- **chat-model-degisikligi/** — model-değişikliği chat arşivi (parti 1).
- **AGENTS-statik-levha-2026-08-21.md** — eski Jarvis `AGENTS.md` statik işaret levhası (08-21, Karar 47: senkron bakım yok); dosya 09-18'de F4 kanon paketiyle arşive indi.
- **gorunum-2026-11-10/** — 11-10'da emekli edilen gold görünüm CSV'leri (`v_asof_eval`, `v_d2_eval` vb.; 15 dosya, kendi README'si var); 11-11'de arşive girdi.
- **kanon/** — emekli kanon parçaları: `m36-k005`, `portrisk` emekli kayıtları (10-17) ve tüzük m.08-m.16 / m.28-m.44 md sürümleri (md-Lean geçişi, 10-16/10-17).
- **kapsul-2026-09-10.md ... kapsul-2026-10-17.md** — dondurulan kapsül dosyaları (Karar 122: kapsül/pano dondu; durum kütükten okunur); 09-18'de `jarvis/` altına taşınırken arşive girdi.
- **md-lean-gecis/** — md → Lean/Rust geçişinde (10-16) yerini alan eski md sürümleri: kök `AGENTS`, `paralel-oturum-protokolu`.
- **memory-arsivi-2026-09-21.md, -09-22, -10-17, -10-25** — harness hafıza dizini byte-FIFO ile arşive inen satırlar (Karar 104 M1; kurallar canlı kullanıcı CLAUDE.md'de).
- **ogrenme-oturum-protokolu-v2-2026-09-15.md** — öğrenme oturum protokolü v2 (09-15); 09-18'de arşive indi.
- **worktree-kalinti-2026-11-10/** — 11-10 worktree temizliğinde silinen 9 worktree'nin commit'lenmemiş artıkları (yama + takipsiz dosya kopyaları). 11-11 denetiminde `sage/degisiklik.patch` ve `span/degisiklik.patch` 0 bayt olduğundan kaldırıldı (`wc -c` ile doğrulandı; içerik kaybı yok).
- **zamanlanmis-gorev/** — gece senkron zamanlanmış görev dosyaları (`JARVIS-gece-senkron-2026-10-16.xml`, `gece-senkron.ps1`); 11-10'da arşive girdi.
- **Not (11-11, E36):** `raporlar/2026-09/yol-tasi-kuru-2026-09-18.diff` ve `yol-tasi-uygula-2026-09-18.diff` bayt-eşitti (`cmp` aynı, 59.799 bayt); `kuru` kopyası kaldırıldı, `uygula` kaldı.

Kural: m.8 silme yasağı — hiçbir dosya buradan silinmez, yalnız taşınır/pointer'la işaret edilir. Adres arayan pointer önce bu README'ye, sonra ilgili alt dizine iner.

> **Ad eşitliği (Karar 93, 2026-09-10):** bu dizindeki tarihli dosyalarda geçen **Carvis = Jarvis** (Salih'le konuşan ajanın 09-10 öncesi adı); sistem/repo kastedilirken "depo"/"kanon". Halef-sözlük: `core/baglam-anahtar-kaydi.md` anahtar `carvis-rol-adi` → `jarvis-ajan-adi`.
