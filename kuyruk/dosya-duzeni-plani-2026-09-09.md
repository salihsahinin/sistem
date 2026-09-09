# Dosya düzeni planı — gezilebilir ağaç (Salih emri + ağaç onayı 2026-09-09, Katman-1)

*Salih beyanı aynen: "jarvisin dosya düzeni şu an çok dağınık (benim görüntülemem için) bunu düzenli ve içinde gezilebilir, anlaşılabilir bir hale getirip artık kullanılmayan dosyaları buna uygun klasörlerde toplamamız lazım" · "ağaç formatı için onay veriyorum". Yöntem: `git mv` (tarihçe korunur, silme YOK — m.8); parti başına `pointer-kayma.py` + `karar-borcu-tablo.py` + `katman-hatti.py` + test kapısı; sabit-yol yazan script'ler taranıp güncellenir. Yüzey: VS Code (md + d2 görüntüleyici, 09-09). Envanter (git ls-files, 09-09): cc 387 · raporlar 307 · veri 133 · kuyruk 89 · tools 69 · .claude 49 · ogrenme 40 · wiki 26 · core 25 · graf 23; kök 28 kalem (10 gevşek md).*

## Hedef ağaç (onaylı)
```
~/jarvis
├── README.md · CLAUDE.md · KILAVUZ.md · LICENSE · fikir-kutusu.md · AGENTS.md   (kök: yalnız bunlar)
├── core/        kanon (tüzük, kapsül, pano, şemalar, prompt-dosya tablosu)
├── kuyruk/      canlı defter, kutular, gelen'ler, masa gündemleri, skill-deneme, ders-gbm
├── arsiv/       TEK ÇATI — kurulus-2026-07/ · kuyruk-arsiv/ (eski kuyruk/arsiv) · karantina/ (İB-72) · chat-model-degisikligi/
├── cc/          gorev/YYYY-MM/ · rapor/YYYY-MM/ · devir/ · prompt/ · pipeline/ · workflow/ · d2-eval/ · denetci-kalibrasyon/ · kanit-bulucu/
├── raporlar/    seans/ · vardiya/ · hareket/ · masa/ · gorsel/ · usage/ · (konu raporları YYYY-MM/)
├── ogrenme/     kurslar + kaynaklar/ (eski Clippings)
├── wiki/ · veri/ · tools/ · graf/ · .claude/ · kaynak-kodu/ · paylasim/
```
Her klasörde 5 satırlık `README.md`: ne var · nasıl gezilir · üretici script · arşiv kuralı.

## Partiler
| # | Kapsam | Sabit-yol dokunuşu | Durum |
|---|---|---|---|
| 1 | kök 8 gevşek md → `arsiv/kurulus-2026-07/` · "model değişikliği… chat/" → `arsiv/chat-model-degisikligi/` · `Clippings/` → `ogrenme/kaynaklar/` · `Başlıksız.canvas` (izlenmiyor) → Salih siler | `tools/anahtar-denetim.py` kök-dosya regex + Clippings sınıfı · `tools/baglam-tablo.py` MODEL_KLASOR_ONEK · CLAUDE.md §7 tek satır · KILAVUZ | 09-09 Fable |
| 2 | `kuyruk/arsiv/*` (30) → `arsiv/kuyruk-arsiv/` · `kuyruk/arsiv/karantina/` → `arsiv/karantina/` — TAMAMLANDI 09-09 Sonnet işçi | `karantina.py` (2 yol) · `kod-orani-olcum.py` DISLA · `kod-envanter.py` yedek · `pointer-kayma.py` glob · `bag-tablo.py` LIKE · `anahtar-denetim.py` prefix · 3 test dosyası · `veri/karantina.jsonl` yol alanı · md pointer'ları (`kuyruk/arsiv/` → `arsiv/kuyruk-arsiv/`, sed) | 09-09 Sonnet işçi |
| 3 | `cc/` 387 → `gorev/YYYY-MM` · `rapor/YYYY-MM` · `devir/` · `prompt/` | ledger `kaynak` alanları · silver dosya_id · `hareket-tablo.py`? · gorev-emri-derleme teslim adresi (`cc/rapor-YYYY-MM-DD-N.md` → `cc/rapor/YYYY-MM/…`) | Opus İB-75 devri SONRASI |
| 4 | `raporlar/` 307 → alt-klasörler | `hareket-tablo.py` (hareket-gunlugu yolu) · seans-kapanis/acilis SKILL · `masa-html.py` · kapsül pointer'ları | parti 3 ile |
| 5 | README'ler + KILAVUZ "nerede ne var" + CLAUDE.md §7 | — | her parti sonunda |

## Silver / pointer etkisi
Taşınan dosyanın `dosya_id`'si değişir → silver eski kayıtlar YETİM adayına düşer (T-B-YETİM bugün 385); katman-hatti yeni yolu yeniden ingest eder, eski kayıt süpersede zinciriyle bağlanır (KB-61 b). Parti sonunda `silver-saglik.py --kapi` exit 0 şart; YETİM artışı teslim raporuna sayı olarak düşer (m.39).
