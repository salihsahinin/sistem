# Hareket günlüğü — 2026-11-10 (Jarvis'in araç çağrıları; kaynak transkript → `tools/hareket-tablo.py`; HEAD `217d138e`)

*Okunabilirlik ilkesi (Salih 08-17): Jarvis'in o gün YAPTIĞI her şey — dosya yazma/düzenleme, komut, okuma, arama, ajan/skill/workflow çağrısı — burada düz satır. Hedef gösterilir, içerik gösterilmez (içerik dosyanın kendisinde ya da git log'da). Makine-yüzü: silver `hareket` (`veri/baglam.sqlite`), gold `veri/gorunum/v_hareket_gunluk.csv` · `v_son_hareketler.csv`; bronz `veri/bronz/hareket-olay.jsonl`. Toplam bugün: 8 çağrı, 2 oturum.*

## Oturum `785218a6` — 14:43:15→14:44:00 · 6 çağrı · model fable-5-2 · hata 0
**Özet:** koştu 4 · skill çağırdı 1 · yazdı 1
**Yazılan/düzenlenen dosyalar (1):** `raporlar\seans\seans-teslim-girdi-2026-11-10.json`

| # | saat | fiil | hedef | sonuç |
|---|---|---|---|---|
| 25 | 14:43:15 | skill çağırdı | seans-kapanis | tamam |
| 26 | 14:43:19 | koştu | Kapanış öncesi depo durumu, durum aracı yardımı ve teslim şablonunu göster ⟨cd /c/sistem/sistem && git status -sb ¦ head -30; echo ---; git log --oneline -4 ¦ cat; echo ---; ./target/release/durum.exe --help 2>&1 ¦ head -30; e…⟩ | tamam |
| 27 | 14:43:30 | koştu | Kütükte mod iterasyonu kaydı ve commit'lenmemiş olayları ara ⟨cd /c/sistem/sistem && grep -c "" ortak/durum-olay.jsonl; grep -n -i "mod iterasyon\¦jarvis-oda\¦oda v0\¦graf v0" ortak/durum-olay.jsonl ¦ cut -c1-260…⟩ | tamam |
| 28 | 14:43:41 | koştu | Seans düğümünü aç, biten işi kapat, kalan işi kütüğe yaz ⟨cd /c/sistem/sistem && D=./target/release/durum.exe && $D listele --alan jarvis 2>&1 ¦ grep -E "^#?(46¦47¦71)\b¦#46¦#47¦#71" ¦ cut -c1-200; S=2026-11-…⟩ | tamam |
| 29 | 14:43:57 | yazdı | raporlar\seans\seans-teslim-girdi-2026-11-10.json | tamam |
| 30 | 14:44:00 | koştu | İşi kütükte kapat ve kapanış araçlarını sırayla koş ⟨cd /c/sistem/sistem && D=./target/release/durum.exe && S=2026-11-10-jarvis-mod && $D al 47 --oturum $S 2>&1 ¦ tail -1 && $D bitir 47 --oturum $S --kan…⟩ | yok |

## Oturum `b6e364d3` — 14:43:51→14:43:55 · 2 çağrı · model fable-5-2 · hata 0
**Özet:** skill çağırdı 1 · koştu 1

| # | saat | fiil | hedef | sonuç |
|---|---|---|---|---|
| 23 | 14:43:51 | skill çağırdı | seans-kapanis | tamam |
| 24 | 14:43:55 | koştu | Depo durumu, açık seans ve teslim şablonunu oku ⟨cd /c/sistem/sistem && date +%F\ %T && git status -sb ¦ head -5 && git status --short ¦ wc -l && git log --oneline -6 && ./target/release/durum.exe ot…⟩ | tamam |

