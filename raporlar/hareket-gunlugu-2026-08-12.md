# Hareket günlüğü — 2026-08-12 (Carvis'in araç çağrıları; kaynak transkript → `tools/hareket-tablo.py`; HEAD `416334f`)

*Okunabilirlik ilkesi (Salih 08-17): Carvis'in o gün YAPTIĞI her şey — dosya yazma/düzenleme, komut, okuma, arama, ajan/skill/workflow çağrısı — burada düz satır. Hedef gösterilir, içerik gösterilmez (içerik dosyanın kendisinde ya da git log'da). Makine-yüzü: silver `hareket` (`veri/baglam.sqlite`), gold `veri/gorunum/v_hareket_gunluk.csv` · `v_son_hareketler.csv`; bronz `veri/bronz/hareket-olay.jsonl`. Toplam bugün: 7 çağrı, 1 oturum.*

## Oturum `ee6c99ff` — 21:35:43→21:36:53 · 7 çağrı · model fable-5 · hata 0
**Özet:** okudu 3 · koştu 3 · skill çağırdı 1

| # | saat | fiil | hedef | sonuç |
|---|---|---|---|---|
| 1 | 21:35:43 | skill çağırdı | gunaydin-vardiya ana oturum Cowork'ten terminale taşınıyor — vardiya devri + firstmate öğrenme oturumu | tamam |
| 2 | 21:35:58 | okudu | core/durum-kapsulu.md | tamam |
| 3 | 21:35:59 | okudu | core/pano.md | tamam |
| 4 | 21:35:59 | koştu | Read last sync-log lines and recent git history ⟨tail -n 3 /Users/HasanSalihSahin/jarvis/raporlar/usage/senkron-log.jsonl 2>/dev/null; echo "---"; git -C /Users/HasanSalihSahin/jarvis log --oneline -…⟩ | tamam |
| 5 | 21:36:09 | okudu | raporlar/vardiya-teslim-2026-08-12-l8-mac.md | tamam |
| 6 | 21:36:10 | koştu | List firstmate repo contents and read README head ⟨ls -la ~/dev/firstmate/ 2>/dev/null && echo "===README===" && head -n 80 ~/dev/firstmate/README.md 2>/dev/null⟩ | tamam |
| 7 | 21:36:53 | koştu | Check firstmate state/config changes and tmux sessions ⟨ls -la ~/dev/firstmate/state/ ~/dev/firstmate/config/ 2>/dev/null; echo "===tmux==="; tmux ls 2>&1; echo "===state içerik örnekleri==="; find ~/dev/fi…⟩ | tamam |

