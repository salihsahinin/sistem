# Hareket günlüğü — 2026-10-05 (Jarvis'in araç çağrıları; kaynak transkript → `tools/hareket-tablo.py`; HEAD `a97b383`)

*Okunabilirlik ilkesi (Salih 08-17): Jarvis'in o gün YAPTIĞI her şey — dosya yazma/düzenleme, komut, okuma, arama, ajan/skill/workflow çağrısı — burada düz satır. Hedef gösterilir, içerik gösterilmez (içerik dosyanın kendisinde ya da git log'da). Makine-yüzü: silver `hareket` (`veri/baglam.sqlite`), gold `veri/gorunum/v_hareket_gunluk.csv` · `v_son_hareketler.csv`; bronz `veri/bronz/hareket-olay.jsonl`. Toplam bugün: 8 çağrı, 1 oturum.*

## Oturum `c6a2e28a` — 15:47:21→15:47:37 · 8 çağrı · model fable-5-1 · hata 0
**Özet:** koştu 4 · okudu 3 · skill çağırdı 1

| # | saat | fiil | hedef | sonuç |
|---|---|---|---|---|
| 1 | 15:47:21 | skill çağırdı | seans-acilis | tamam |
| 2 | 15:47:26 | okudu | core\durum-kapsulu.md [bütün] | tamam |
| 3 | 15:47:26 | okudu | core\pano.md [bütün] | tamam |
| 4 | 15:47:27 | koştu | Açılış kapılarını koştur (K1 canlı-oturum, K2 manifest, K3 silver) ⟨(python3 tools/acilis-kapilari.py 2>&1 ¦¦ python tools/acilis-kapilari.py 2>&1) ¦ head -60⟩ | tamam |
| 5 | 15:47:29 | koştu | Ajan dönüş klasörlerini ve core dizinini listele ⟨cd /c/sistem/sistem && ls */cc/giden/ 2>/dev/null ¦ head -60; ls jarvis/core/ ¦ head -80⟩ | tamam |
| 6 | 15:47:35 | koştu | Silver katmanını tazele (K3 bayat kapısı) ⟨python3 tools/katman-hatti.py 2>&1 ¦ tail -8⟩ | yok |
| 7 | 15:47:36 | okudu | core\baglam-anahtar-kaydi.md [bütün] | yok |
| 8 | 15:47:37 | koştu | Ajan kanonlarının boyutunu ve mevcut hook olaylarını ölç ⟨cd /c/sistem/sistem && wc -c */AGENTS.md jarvis/core/*.md 2>/dev/null ¦ tail -40; ls jarvis/.claude/hooks 2>/dev/null; grep -n "UserPromptSubmit\¦Inst…⟩ | yok |

