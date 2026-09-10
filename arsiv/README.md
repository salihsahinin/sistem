# arsiv/ — tek çatı

Repo-genel arşiv kökü (dosya düzeni planı, parti 2, 2026-09-09). Alt dizinler:

- **kurulus-2026-07/** — kök seviye kuruluş dosyaları (parti 1, Fable doldurur; bu partide boş olabilir).
- **kuyruk-arsiv/** — eski `kuyruk/arsiv/` (damıtma/yeniden-yazım arşivleri: defter, kutu, pano, KILAVUZ, ölçüm-bankı arşiv dosyaları; tarihli, `-YYYY-MM-DD.md` adlandırma).
- **karantina/** — İB-72 BAYAT-DOSYA KARANTİNA MEKANİZMASI hedefi (eski `kuyruk/arsiv/karantina/`); dizin yapısı korunarak taşınan dosyalar, BAKMA-GEREK-YOK bayraklı; envanter `python3 tools/karantina.py --liste`, denetim `--denetle`, kayıt `veri/karantina.jsonl`.
- **chat-model-degisikligi/** — model-değişikliği chat arşivi (parti 1).

Kural: m.8 silme yasağı — hiçbir dosya buradan silinmez, yalnız taşınır/pointer'la işaret edilir. Adres arayan pointer önce bu README'ye, sonra ilgili alt dizine iner.

> **Ad eşitliği (Karar 93, 2026-09-10):** bu dizindeki tarihli dosyalarda geçen **Carvis = Jarvis** (Salih'le konuşan ajanın 09-10 öncesi adı); sistem/repo kastedilirken "depo"/"kanon". Halef-sözlük: `core/baglam-anahtar-kaydi.md` anahtar `carvis-rol-adi` → `jarvis-ajan-adi`.
