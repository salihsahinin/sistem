# Hareket günlüğü — 2026-08-29 (Carvis'in araç çağrıları; kaynak transkript → `tools/hareket-tablo.py`; HEAD `4745df9`)

*Okunabilirlik ilkesi (Salih 08-17): Carvis'in o gün YAPTIĞI her şey — dosya yazma/düzenleme, komut, okuma, arama, ajan/skill/workflow çağrısı — burada düz satır. Hedef gösterilir, içerik gösterilmez (içerik dosyanın kendisinde ya da git log'da). Makine-yüzü: silver `hareket` (`veri/baglam.sqlite`), gold `veri/gorunum/v_hareket_gunluk.csv` · `v_son_hareketler.csv`; bronz `veri/bronz/hareket-olay.jsonl`. Toplam bugün: 6 çağrı, 1 oturum.*

## Oturum `7ae8954e` — 01:27:57→01:28:10 · 6 çağrı · model fable-5 · hata 0
**Özet:** koştu 3 · okudu 2 · skill çağırdı 1

| # | saat | fiil | hedef | sonuç |
|---|---|---|---|---|
| 1 | 01:27:57 | skill çağırdı | seans-acilis | tamam |
| 2 | 01:28:01 | okudu | core/durum-kapsulu.md [bütün] | tamam |
| 3 | 01:28:02 | okudu | core/pano.md [bütün] | tamam |
| 4 | 01:28:03 | koştu | Git log son 5 commit + senkron log son satır ⟨git log -5 --oneline && tail -1 raporlar/usage/senkron-log.jsonl⟩ | tamam |
| 5 | 01:28:09 | koştu | Silver+gold türevlerini tazele (katman-hatti) ⟨python3 tools/katman-hatti.py 2>&1 ¦ tail -5⟩ | yok |
| 6 | 01:28:10 | koştu | Ek yüklenen kurs dosyasını listele ⟨ls -la "/Users/HasanSalihSahin/Downloads/6" && find "/Users/HasanSalihSahin/Downloads/6" -type f ¦ head -50⟩ | yok |

