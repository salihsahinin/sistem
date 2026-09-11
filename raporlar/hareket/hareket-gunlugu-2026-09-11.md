# Hareket günlüğü — 2026-09-11 (Jarvis'in araç çağrıları; kaynak transkript → `tools/hareket-tablo.py`; HEAD `b786059`)

*Okunabilirlik ilkesi (Salih 08-17): Jarvis'in o gün YAPTIĞI her şey — dosya yazma/düzenleme, komut, okuma, arama, ajan/skill/workflow çağrısı — burada düz satır. Hedef gösterilir, içerik gösterilmez (içerik dosyanın kendisinde ya da git log'da). Makine-yüzü: silver `hareket` (`veri/baglam.sqlite`), gold `veri/gorunum/v_hareket_gunluk.csv` · `v_son_hareketler.csv`; bronz `veri/bronz/hareket-olay.jsonl`. Toplam bugün: 5 çağrı, 1 oturum.*

## Oturum `72eb3a58` — 09:46:32→09:46:58 · 5 çağrı · model fable-5-1 · hata 0
**Özet:** koştu 4 · skill çağırdı 1

| # | saat | fiil | hedef | sonuç |
|---|---|---|---|---|
| 108 | 09:46:32 | skill çağırdı | seans-kapanis | tamam |
| 109 | 09:46:48 | koştu | Canlı-oturum kapısı: git durumu ve kapsülün galeri satırı ⟨cd ~/jarvis && git log -3 --format='%h %ci %s' ¦ cut -c1-140 && git status --short ¦ head -20 && echo ---KAPSUL--- && grep -n 'Güncelleme\¦GALERİ' cor…⟩ | tamam |
| 110 | 09:46:51 | koştu | Kapsülün galeri şeridi satırını tam oku ⟨cd ~/jarvis && grep -n 'GALERİ ŞERİDİ' core/durum-kapsulu.md ¦ cut -c1-900; echo; wc -c core/durum-kapsulu.md; wc -l core/durum-kapsulu.md⟩ | tamam |
| 111 | 09:46:57 | koştu | Kapanış kapıları: hareket kütüğü, bayat-çekim, katman hattı, skill eşiği, silver sağlık, kural sayacı, bağlam seyri ⟨cd ~/jarvis && { echo "== hareket-tablo"; python3 tools/hareket-tablo.py 2>&1 ¦ tail -4; echo "== bayat-cekim"; python3 tools/bayat-cekim.py --liste 2…⟩ | yok |
| 112 | 09:46:58 | koştu | Birim-test kapısı ⟨cd ~/jarvis && python3 -m unittest discover -s tools/testler -p 'test_*.py' 2>&1 ¦ tail -4⟩ | yok |

