# Hareket günlüğü — 2026-09-20 (Jarvis'in araç çağrıları; kaynak transkript → `tools/hareket-tablo.py`; HEAD `3019e7f`)

*Okunabilirlik ilkesi (Salih 08-17): Jarvis'in o gün YAPTIĞI her şey — dosya yazma/düzenleme, komut, okuma, arama, ajan/skill/workflow çağrısı — burada düz satır. Hedef gösterilir, içerik gösterilmez (içerik dosyanın kendisinde ya da git log'da). Makine-yüzü: silver `hareket` (`veri/baglam.sqlite`), gold `veri/gorunum/v_hareket_gunluk.csv` · `v_son_hareketler.csv`; bronz `veri/bronz/hareket-olay.jsonl`. Toplam bugün: 3 çağrı, 1 oturum.*

## Oturum `2f73aa04` — 16:53:22→16:53:32 · 3 çağrı · model fable-5-1 · hata 0
**Özet:** koştu 2 · skill çağırdı 1

| # | saat | fiil | hedef | sonuç |
|---|---|---|---|---|
| 1 | 16:53:22 | skill çağırdı | seans-acilis | tamam |
| 2 | 16:53:27 | koştu | Açılış kapılarını koştur, tarih ve kuyruk listesini al ⟨python3 tools/acilis-kapilari.py 2>&1 ¦ head -40; echo ---; date; echo ---; ls -t kuyruk/ ¦ head -20⟩ | tamam |
| 3 | 16:53:32 | koştu | Silver'ı tazele; kapsül, pano ve masa-17 dosyalarını oku ⟨python3 tools/katman-hatti.py 2>&1 ¦ tail -5; echo ---KAPSUL; cat core/durum-kapsulu.md; echo ---PANO; cat core/pano.md; echo ---MASA17; ls -la raporl…⟩ | yok |

